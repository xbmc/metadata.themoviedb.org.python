import sys
import unittest
import unittest.mock as mock


class TestIMDBRatings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake = mock.MagicMock()

        fake_module = mock.patch.dict(sys.modules,
                {"imdbratings": cls.fake})

        fake_module.start()
        cls.addClassCleanup(fake_module.stop)

        # Complicated because be have a name collision:
        # "python.lib.tmdbscraper.imdbratings" and
        # "script.module.imdbratings".
        import python.lib.tmdbscraper.imdbratings
        cls.imdbratings = python.lib.tmdbscraper.imdbratings

    def setUp(self):
        self.fake.reset_mock()

    def test_known_title(self):
        self.fake.get_rating.return_value = (8.6, 1315176)
        self.assertEqual(
            {'ratings': {'imdb': {'votes': 1315176, 'rating': 8.6}}},
            self.imdbratings.get_details({'imdb': 'tt0076759', 'tmdb': '11'}))
        self.fake.get_rating.assert_called_once_with('tt0076759')

    def test_unknown_title(self):
        self.fake.get_rating.return_value = None
        self.assertEqual({},
                         self.imdbratings.get_details({'imdb': 'tt9999999'}))
        self.fake.get_rating.assert_called_once_with('tt9999999')

    def test_no_imdb_id(self):
        self.assertEqual({}, self.imdbratings.get_details({'tmdb': '11'}))
        self.fake.get_rating.assert_not_called()

    def _not_loaded(self, dates, ratings):
        """The ratings not loaded at first: dataset_date() answers dates in turn, then the last"""
        dates = list(dates)
        self.fake.dataset_date.side_effect = lambda: dates.pop(0) if len(dates) > 1 else dates[0]
        self.fake.get_rating.side_effect = list(ratings)
        self.imdbratings._waited = False
        # setUp's reset_mock() keeps side effects
        self.addCleanup(self.fake.reset_mock, side_effect=True)

    def test_ratings_not_loaded(self):
        self._not_loaded([None], [None, None])
        with mock.patch.object(self.imdbratings, 'FIRST_LOAD_WAIT', 3),                 mock.patch.object(self.imdbratings.time, 'sleep') as sleep:
            self.assertIn('error', self.imdbratings.get_details({'imdb': 'tt0076759'}))
        self.assertEqual(3, sleep.call_count)

    def test_ratings_loaded_during_the_wait(self):
        self._not_loaded([None, None, '2026-11-16'], [None, (8.6, 1315176)])
        with mock.patch.object(self.imdbratings.time, 'sleep') as sleep:
            self.assertEqual(
                {'ratings': {'imdb': {'votes': 1315176, 'rating': 8.6}}},
                self.imdbratings.get_details({'imdb': 'tt0076759'}))
        self.assertEqual(1, sleep.call_count)

    def test_waits_once(self):
        self._not_loaded([None], [None] * 4)
        with mock.patch.object(self.imdbratings, 'FIRST_LOAD_WAIT', 2),                 mock.patch.object(self.imdbratings.time, 'sleep') as sleep:
            self.imdbratings.get_details({'imdb': 'tt0076759'})
            self.assertIn('error', self.imdbratings.get_details({'imdb': 'tt0080684'}))
        self.assertEqual(2, sleep.call_count)
