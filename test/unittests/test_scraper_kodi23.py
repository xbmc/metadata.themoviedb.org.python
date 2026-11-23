import unittest

from test.unittests import kodi_stubs

SEARCH = 'api.themoviedb.org/3/search/movie'
MOVIE = 'api.themoviedb.org/3/movie/550'


class _Kodi23(unittest.TestCase):
    """python/scraper.py's calls as Kodi 23 makes them, with Kodi's modules stood in for and the
    network faked"""

    def call(self, *params, settings=None, dataset='2026-11-16', rating=(8.8, 2000000), **answers):
        network = kodi_stubs.Network(dict(kodi_stubs.answers(), **answers))
        scraper, kodi, _ = kodi_stubs.load_scraper(self, settings, network)
        kodi.dataset, kodi.rating = dataset, rating
        kodi_stubs.run(scraper, *params)
        return kodi

    def search(self, **answers):
        return self.call('action=find', 'title=A Film', 'year=1999', **answers)

    def details(self, settings=None, **kwargs):
        return self.call('action=getdetails', 'url={"tmdb": "550"}', settings=settings, **kwargs)


class TestNoNotification(_Kodi23):
    """Kodi 23 reports a failed look-up itself"""

    def test_a_failed_search_shows_none(self):
        kodi = self.search(**{SEARCH: None})
        self.assertEqual([], kodi.notifications)
        self.assertTrue(any('error searching' in msg for msg in kodi.warnings()), kodi.warnings())

    def test_a_failed_details_call_shows_none(self):
        kodi = self.details(**{MOVIE: None})
        self.assertEqual([], kodi.notifications)
        self.assertTrue(kodi.warnings())
