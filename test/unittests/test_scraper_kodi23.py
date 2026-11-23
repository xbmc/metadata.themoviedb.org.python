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


class TestAPartThatFailsFailsTheCall(_Kodi23):
    """A part that can't be had after its request's retry fails the details call, so that Kodi 23
    tries the movie again at its next scan. A 404 is "nothing there": the movie is added without
    the part."""

    SET = 'api.themoviedb.org/3/collection/10'
    FANART_MOVIE = 'webservice.fanart.tv/v3/movies/550'
    FANART_SET = 'webservice.fanart.tv/v3/movies/10'
    TRAKT = 'api.trakt.tv/movies/tt0137523'
    GERMAN = {'language': 'de-DE'}
    # In German, without a plot, so that English is asked for
    GERMAN_MOVIE = {MOVIE + '|language=de-DE': dict(kodi_stubs.movie(), overview='', tagline='')}

    def assertFails(self, kodi):
        self.assertEqual([False], kodi.ended)
        self.assertEqual([], kodi.resolved)

    def assertResolved(self, kodi):
        self.assertEqual([], kodi.ended)
        self.assertEqual([True], [ok for ok, _ in kodi.resolved])

    def test_the_set_fails(self):
        self.assertFails(self.details(**{self.SET: None}))

    def test_the_set_is_gone(self):
        self.assertResolved(self.details(**{self.SET: 404}))

    def test_the_english_text_fails(self):
        self.assertFails(self.details(self.GERMAN, **dict(self.GERMAN_MOVIE, **{MOVIE + '|language=en-US': None})))

    def test_the_english_text_is_gone(self):
        self.assertResolved(self.details(self.GERMAN, **dict(self.GERMAN_MOVIE, **{MOVIE + '|language=en-US': 404})))

    def test_fanart_tv_fails_for_the_movie(self):
        self.assertFails(self.details(**{self.FANART_MOVIE: None}))

    def test_fanart_tv_fails_for_the_set(self):
        self.assertFails(self.details(**{self.FANART_SET: None}))

    def test_fanart_tv_has_no_art(self):
        self.assertResolved(self.details(**{self.FANART_MOVIE: 404, self.FANART_SET: 404}))

    def test_a_failed_trakt_rating_is_left_out(self):
        self.assertResolved(self.details({'traktanyway': True}, **{self.TRAKT: None}))

    def test_trakt_doesnt_know_it(self):
        self.assertResolved(self.details({'traktanyway': True}, **{self.TRAKT: 404}))

    def test_imdb_ratings_not_loaded_are_left_out(self):
        self.assertResolved(self.details({'RatingS': 'IMDb'}, dataset=None, rating=None))

    def test_imdb_has_no_rating_for_it(self):
        self.assertResolved(self.details({'RatingS': 'IMDb'}, rating=None))
