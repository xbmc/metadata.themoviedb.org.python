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


class TestAFailureEndsTheCall(_Kodi23):
    """A failure ends the call with succeeded=False, which Kodi 23 counts as a failed look-up and
    tries again at its next scan; finding nothing ends it with succeeded=True"""

    def test_a_search_that_finds_succeeds(self):
        kodi = self.search()
        self.assertEqual([True], kodi.ended)
        self.assertEqual(1, len(kodi.items))

    def test_a_search_that_finds_nothing_succeeds(self):
        kodi = self.search(**{SEARCH: {'total_pages': 0, 'results': []}})
        self.assertEqual([True], kodi.ended)
        self.assertEqual([], kodi.items)

    def test_a_failed_search_fails(self):
        self.assertEqual([False], self.search(**{SEARCH: None}).ended)

    def test_a_failed_page_2_fails_the_search(self):
        found = kodi_stubs.answers()[SEARCH]['results'][0]
        page_1 = {'total_pages': 2, 'results': [dict(found, title='Another', original_title='Another')]}
        kodi = self.search(**{SEARCH: page_1, SEARCH + '|page=2': None})
        self.assertEqual([False], kodi.ended)
        self.assertEqual([], kodi.items)

    def test_a_failed_details_call_fails(self):
        kodi = self.details(**{MOVIE: None})
        self.assertEqual([False], kodi.ended)
        self.assertEqual([], kodi.resolved)
