import socket
import threading
import time
import types
import unittest
import unittest.mock as mock
from email.utils import formatdate
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from python.lib.tmdbscraper import api_utils


class _Handler(BaseHTTPRequestHandler):
    """Answers each path with its plan's steps in turn, the last repeated"""

    def log_message(self, *args):
        pass

    def do_GET(self):
        path = self.path.split('?')[0]
        self.server.hits[path] = self.server.hits.get(path, 0) + 1
        steps = self.server.plans[path]
        kind, *args = steps.pop(0) if len(steps) > 1 else steps[0]
        if kind == 'json':
            body = args[0].encode()
            self.send_response(200)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif kind == 'status':
            self.send_response(args[0])
            for name, value in (args[1] if len(args) > 1 else {}).items():
                self.send_header(name, value)
            self.send_header('Content-Length', '0')
            self.end_headers()
        elif kind == 'reset':
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                                       b'\x01\x00\x00\x00\x00\x00\x00\x00')
            self.connection.close()
        elif kind == 'short':
            self.send_response(200)
            self.send_header('Content-Length', '1000')
            self.end_headers()
            self.wfile.write(b'{"a": 1')
            self.wfile.flush()
            self.connection.shutdown(socket.SHUT_WR)
        elif kind == 'stall':
            time.sleep(args[0])


class TestFetch(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), _Handler)
        self.server.block_on_close = False
        self.server.plans, self.server.hits = {}, {}
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.url = 'http://127.0.0.1:{}'.format(self.server.server_address[1])
        self.waits = []
        self.session = api_utils.Session(timeout=0.5)
        wait = mock.patch.object(api_utils, '_stop_requested_during',
                                 side_effect=lambda seconds: self.waits.append(seconds))
        wait.start()
        self.addCleanup(wait.stop)
        headers = mock.patch.object(api_utils, 'HEADERS', {})
        headers.start()
        self.addCleanup(headers.stop)

    def load(self, path, *steps, **kwargs):
        self.server.plans[path] = list(steps)
        return self.session.load_info(self.url + path, **kwargs)

    def test_an_answer_is_parsed(self):
        self.assertEqual({'x': 1}, self.load('/a', ('json', '{"x": 1}')))
        self.assertEqual(1, self.server.hits['/a'])

    def test_a_5xx_is_tried_once_more(self):
        self.assertEqual({'x': 2}, self.load('/b', ('status', 503), ('json', '{"x": 2}')))
        self.assertEqual(2, self.server.hits['/b'])

    def test_a_429_waits_the_seconds_retry_after_asks(self):
        self.assertEqual({'x': 3}, self.load('/c', ('status', 429, {'Retry-After': '3'}),
                                             ('json', '{"x": 3}')))
        self.assertEqual([3.0], self.waits)

    def test_a_429_waits_until_the_date_retry_after_gives(self):
        later = formatdate(time.time() + 20, usegmt=True)
        self.assertEqual({'x': 4}, self.load('/d', ('status', 429, {'Retry-After': later}),
                                             ('json', '{"x": 4}')))
        self.assertEqual(1, len(self.waits))
        self.assertTrue(17 <= self.waits[0] <= 21, self.waits)

    def test_retry_after_is_kept_within_limits(self):
        session = api_utils.Session(retry_pause=1.0, max_retry_after=30)
        self.assertEqual(30, session._retry_after({'Retry-After': '100'}))
        self.assertEqual(1.0, session._retry_after({'Retry-After': '0'}))
        self.assertEqual(1.0, session._retry_after({'Retry-After': 'soon'}))
        self.assertEqual(1.0, session._retry_after({}))
        past = formatdate(time.time() - 60, usegmt=True)
        self.assertEqual(1.0, session._retry_after({'Retry-After': past}))

    def test_a_404_is_not_tried_again_and_keeps_its_code(self):
        answer = self.load('/e', ('status', 404))
        self.assertEqual(404, answer['code'])
        self.assertTrue(api_utils.is_not_found(answer))
        self.assertEqual(1, self.server.hits['/e'])

    def test_a_failure_isnt_not_found(self):
        answer = self.load('/f', ('status', 500))
        self.assertIn('error', answer)
        self.assertFalse(api_utils.is_not_found(answer))

    def test_a_reset_is_tried_once_more(self):
        self.assertEqual({'x': 5}, self.load('/g', ('reset',), ('json', '{"x": 5}')))
        self.assertEqual(2, self.server.hits['/g'])

    def test_a_body_cut_short_is_tried_once_more(self):
        self.assertEqual({'x': 6}, self.load('/h', ('short',), ('json', '{"x": 6}')))
        self.assertEqual(2, self.server.hits['/h'])

    def test_a_body_that_isnt_json_fails_after_a_retry(self):
        answer = self.load('/i', ('json', '<html>oops</html>'))
        self.assertIn('could not be read', answer['error'])
        self.assertEqual(2, self.server.hits['/i'])

    def test_a_stall_fails_after_a_retry(self):
        answer = self.load('/j', ('stall', 1.0))
        self.assertIn('failed to reach', answer['error'])
        self.assertEqual(2, self.server.hits['/j'])

    def test_the_default_is_given_for_a_failure(self):
        self.assertEqual({}, self.load('/k', ('status', 500), default={}))

    def test_the_api_keys_are_left_out_of_the_log(self):
        logs = []
        fake_xbmc = types.SimpleNamespace(LOGDEBUG=0, LOGINFO=1, LOGWARNING=2,
                                          log=lambda msg, level=0: logs.append(msg))
        api_utils.set_headers({'User-Agent': 'test', 'api-key': 'HEADERKEY', 'client-key': 'MINE'})
        with mock.patch.object(api_utils, 'xbmc', fake_xbmc):
            self.load('/l', ('status', 404), params={'api_key': 'URLKEY', 'q': 'x'})
        text = '\n'.join(logs)
        for key in ('URLKEY', 'HEADERKEY', 'MINE'):
            self.assertNotIn(key, text)
        self.assertIn('api_key=...', text)
        self.assertIn("'User-Agent': 'test'", text)
