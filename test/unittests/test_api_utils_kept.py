import time
import unittest
import unittest.mock as mock

from python.lib.tmdbscraper import api_utils


class TestKept(unittest.TestCase):
    def setUp(self):
        api_utils.forget_kept()
        self.addCleanup(api_utils.forget_kept)

    def test_an_answer_is_kept_for_the_same_key(self):
        fetch = mock.MagicMock(return_value={'id': 10, 'name': 'A Set'})
        self.assertEqual('A Set', api_utils.kept(('set', 10), fetch)['name'])
        self.assertEqual('A Set', api_utils.kept(('set', 10), fetch)['name'])
        self.assertEqual(1, fetch.call_count)

    def test_another_key_is_fetched(self):
        fetch = mock.MagicMock(return_value={'id': 10})
        api_utils.kept(('set', 10, 'en-US'), fetch)
        api_utils.kept(('set', 10, 'de-DE'), fetch)
        self.assertEqual(2, fetch.call_count)

    def test_an_error_is_not_kept(self):
        fetch = mock.MagicMock(side_effect=[{'error': 'timed out'}, {'id': 10}])
        self.assertIn('error', api_utils.kept(('set', 10), fetch))
        self.assertEqual({'id': 10}, api_utils.kept(('set', 10), fetch))

    def test_a_404_is_kept(self):
        fetch = mock.MagicMock(return_value={'error': 'not found', 'code': 404})
        api_utils.kept(('set', 10), fetch)
        api_utils.kept(('set', 10), fetch)
        self.assertEqual(1, fetch.call_count)

    def test_an_answer_is_fetched_again_once_too_old(self):
        fetch = mock.MagicMock(return_value={'id': 10})
        api_utils.kept(('set', 10), fetch)
        later = time.monotonic() + api_utils.KEPT_SECONDS + 1
        with mock.patch.object(api_utils.time, 'monotonic', return_value=later):
            api_utils.kept(('set', 10), fetch)
        self.assertEqual(2, fetch.call_count)

    def test_a_caller_changing_its_answer_leaves_the_kept_one(self):
        api_utils.kept(('set', 10), lambda: {'images': {'posters': []}})['images']['posters'].append(1)
        self.assertEqual([], api_utils.kept(('set', 10), None)['images']['posters'])
