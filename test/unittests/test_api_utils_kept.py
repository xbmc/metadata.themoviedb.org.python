import time
import unittest
import unittest.mock as mock

from python.lib.tmdbscraper import api_utils


class TestKept(unittest.TestCase):
    def setUp(self):
        self.session = api_utils.Session()

    def test_an_answer_is_kept_for_the_same_key(self):
        fetch = mock.MagicMock(return_value={'id': 10, 'name': 'A Set'})
        self.assertEqual('A Set', self.session.kept(('set', 10), fetch)['name'])
        self.assertEqual('A Set', self.session.kept(('set', 10), fetch)['name'])
        self.assertEqual(1, fetch.call_count)

    def test_another_key_is_fetched(self):
        fetch = mock.MagicMock(return_value={'id': 10})
        self.session.kept(('set', 10, 'en-US'), fetch)
        self.session.kept(('set', 10, 'de-DE'), fetch)
        self.assertEqual(2, fetch.call_count)

    def test_an_error_is_not_kept(self):
        fetch = mock.MagicMock(side_effect=[{'error': 'timed out'}, {'id': 10}])
        self.assertIn('error', self.session.kept(('set', 10), fetch))
        self.assertEqual({'id': 10}, self.session.kept(('set', 10), fetch))

    def test_a_404_is_kept(self):
        fetch = mock.MagicMock(return_value={'error': 'not found', 'code': 404})
        self.session.kept(('set', 10), fetch)
        self.session.kept(('set', 10), fetch)
        self.assertEqual(1, fetch.call_count)

    def test_an_answer_is_fetched_again_once_too_old(self):
        fetch = mock.MagicMock(return_value={'id': 10})
        self.session.kept(('set', 10), fetch)
        later = time.monotonic() + self.session.keep_seconds + 1
        with mock.patch.object(api_utils.time, 'monotonic', return_value=later):
            self.session.kept(('set', 10), fetch)
        self.assertEqual(2, fetch.call_count)

    def test_the_oldest_answer_goes_beyond_the_limit(self):
        session = api_utils.Session(keep_most=2)
        fetch = mock.MagicMock(side_effect=lambda: {'id': fetch.call_count})
        for key in (1, 2, 3):
            session.kept(key, fetch)
        session.kept(1, fetch)  # gone: fetched again
        session.kept(3, fetch)  # kept
        self.assertEqual(4, fetch.call_count)

    def test_a_caller_changing_its_answer_leaves_the_kept_one(self):
        self.session.kept(('set', 10), lambda: {'images': {'posters': []}})['images']['posters'].append(1)
        self.assertEqual([], self.session.kept(('set', 10), None)['images']['posters'])

    def test_forgotten_answers_are_fetched_again(self):
        fetch = mock.MagicMock(return_value={'id': 10})
        self.session.kept(('set', 10), fetch)
        self.session.forget()
        self.session.kept(('set', 10), fetch)
        self.assertEqual(2, fetch.call_count)

    def test_each_session_keeps_its_own(self):
        fetch = mock.MagicMock(return_value={'id': 10})
        self.session.kept(('set', 10), fetch)
        api_utils.Session().kept(('set', 10), fetch)
        self.assertEqual(2, fetch.call_count)
