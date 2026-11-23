import unittest

from test.unittests import kodi_stubs


class TestScraperDetails(unittest.TestCase):
    """python/scraper.py's details call, with Kodi's modules stood in for and the network faked"""

    def details(self, settings=None, **answers):
        network = kodi_stubs.Network(dict(kodi_stubs.answers(), **answers))
        scraper, kodi, _ = kodi_stubs.load_scraper(self, settings, network)
        kodi_stubs.run(scraper, 'action=getdetails', 'url={"tmdb": "550"}')
        return kodi

    def resolved(self, kodi):
        self.assertEqual(1, len(kodi.resolved))
        succeeded, item = kodi.resolved[0]
        self.assertTrue(succeeded)
        return item.getVideoInfoTag().values

    def test_all_parts_there(self):
        tag = self.resolved(self.details())
        self.assertEqual('A Set', tag['setSet'])

    def test_a_failed_trakt_rating_is_left_out_and_logged(self):
        kodi = self.details({'traktanyway': True}, **{'api.trakt.tv/movies/tt0137523': None})
        self.resolved(kodi)
        self.assertTrue(any('Trakt' in msg for msg in kodi.warnings()), kodi.warnings())

    def test_a_trakt_rating(self):
        tag = self.resolved(self.details({'RatingS': 'Trakt'}))
        self.assertEqual('trakt', tag['setRatings'][1])

    def test_failed_fanart_tv_art_fails_the_call(self):
        kodi = self.details(**{'webservice.fanart.tv/v3/movies/550': None})
        self.assertEqual([], kodi.resolved)
        self.assertTrue(any('fanart.tv' in msg for msg in kodi.warnings()), kodi.warnings())

    def test_a_failed_movie_request_fails_the_call(self):
        kodi = self.details(**{'api.themoviedb.org/3/movie/550': None})
        self.assertEqual([], [ok for ok, _ in kodi.resolved if ok])
