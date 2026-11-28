import json
import threading
import time
import unittest
import unittest.mock as mock
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from python.lib.tmdbscraper import api_utils


class _Handler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'  # keeps the connection open, as the sites do

    def log_message(self, *args):
        pass

    def setup(self):
        self.server.connections += 1
        super().setup()

    def do_GET(self):
        self.server.requests += 1
        answer = self.server.answers.pop(0) if self.server.answers else (200, False, False)
        status, close, say_close = answer[:3]
        if len(answer) > 3:
            # The status and these headers, then a body that doesn't come
            self.send_response(status)
            for name, value in answer[3].items():
                self.send_header(name, value)
            self.send_header('Content-Length', '100')
            self.end_headers()
            self.wfile.flush()
            time.sleep(2)
            self.close_connection = True
            return
        body = json.dumps({'path': self.path}).encode() if status == 200 else b''
        self.send_response(status)
        self.send_header('Content-Length', str(len(body)))
        if say_close:
            self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(body)
        self.wfile.flush()
        self.close_connection = close or say_close


class TestConnections(unittest.TestCase):
    def setUp(self):
        self.session = api_utils.Session()
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), _Handler)
        self.server.block_on_close = False
        self.server.connections = 0
        self.server.requests = 0
        self.server.answers = []
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = 'http://127.0.0.1:{}/'.format(self.server.server_address[1])
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.addCleanup(self.session.close)
        patcher = mock.patch.object(self.session, '_proxied', return_value=False)
        patcher.start()
        self.addCleanup(patcher.stop)

    def get(self, path):
        return self.session.load_info(self.url + path)

    def test_requests_to_a_site_share_one_connection(self):
        for path in ('a', 'b', 'c'):
            self.assertEqual({'path': '/' + path}, self.get(path))
        self.assertEqual(1, self.server.connections)

    def test_a_connection_is_kept_after_an_error_status(self):
        self.server.answers = [(404, False, False)]
        self.assertEqual(404, self.get('a')['code'])
        self.assertEqual({'path': '/b'}, self.get('b'))
        self.assertEqual(1, self.server.connections)

    def test_one_the_server_closed_is_replaced_before_use(self):
        self.server.answers = [(200, True, False)]  # closed after the answer, without saying so
        self.get('a')
        self.server_settle()
        self.assertEqual({'path': '/b'}, self.get('b'))
        self.assertEqual(2, self.server.connections)
        self.assertEqual(2, self.server.requests)

    def test_one_found_closed_as_it_is_used_is_sent_again_and_not_retried(self):
        self.server.answers = [(200, True, False)]
        self.get('a')
        self.server_settle()
        # As if the server closed it just after the check
        not_readable = mock.patch.object(api_utils.select, 'select', return_value=([], [], []))
        with not_readable, mock.patch.object(api_utils, '_log_failure') as failure:
            self.assertEqual({'path': '/b'}, self.get('b'))
        failure.assert_not_called()
        self.assertEqual(2, self.server.connections)
        self.assertEqual(2, self.server.requests)

    def test_one_the_server_says_it_closes_is_not_kept(self):
        self.server.answers = [(200, False, True)]
        self.get('a')
        self.get('b')
        self.assertEqual(2, self.server.connections)

    def test_closed_connections_are_opened_again(self):
        self.get('a')
        self.session.close()
        self.get('b')
        self.assertEqual(2, self.server.connections)

    def server_settle(self):
        """Lets the server's close reach the client"""
        threading.Event().wait(0.2)

    def test_an_error_status_is_had_though_its_body_stalls(self):
        self.server.answers = [(404, False, False, {})]
        started = time.monotonic()
        self.session.timeout = 1
        answer = self.get('a')
        self.assertEqual(404, answer.get('code'))
        self.assertLess(time.monotonic() - started, 1)
        self.assertEqual(1, self.server.requests)

    def test_a_429_whose_body_stalls_waits_as_it_asks(self):
        self.server.answers = [(429, False, False, {'Retry-After': '3'})]
        waits = []
        self.session.timeout = 1
        wait = mock.patch.object(api_utils, '_stop_requested_during',
                                 side_effect=lambda seconds: waits.append(seconds))
        with wait:
            self.assertEqual({'path': '/b'}, self.get('b'))
        self.assertEqual([3.0], waits)
        self.assertEqual(2, self.server.connections)  # the one with a body to drain isn't kept
