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
