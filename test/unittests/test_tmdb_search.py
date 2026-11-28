import unittest
import unittest.mock as mock

from python.lib.tmdbscraper import api_utils, tmdb

UNREACHABLE = {'error': 'failed to reach the remote site\nReason: timed out'}


class _Settings:
    def getSettingString(self, key):
        return {'originalUrl': 'https://x/original', 'previewUrl': 'https://x/w780',
                'lastUpdated': str(tmdb._get_date_numeric(tmdb.datetime.now()))}[key]


def result(mid, title, released, popularity, original_title=None):
    return {'id': mid, 'title': title, 'release_date': released, 'popularity': popularity,
            'original_title': original_title or title, 'poster_path': None, 'backdrop_path': None}


class TestSearch(unittest.TestCase):
    """TMDBMovieScraper.search()'s order, with canned TMDb answers in TMDb's order. Kodi takes the
    first result."""

    def setUp(self):
        self.pages = {}  # (query, year, page) -> TMDb's answer
        self.asked = []
        search_movie = mock.patch.object(tmdb.tmdbapi, 'search_movie', side_effect=self.search_movie)
        search_movie.start()
        self.addCleanup(search_movie.stop)
        left_out = mock.patch.object(api_utils, 'log_left_out')
        self.left_out = left_out.start()
        self.addCleanup(left_out.stop)

    def search_movie(self, query, year=None, language=None, page=None):
        self.asked.append((query, year, language, page))
        return self.pages[(query, year, page or 1)]

    def answer(self, query, year, *results, page=1, total_pages=1):
        self.pages[(query, year, page)] = {'total_pages': total_pages, 'results': list(results)}

    def ids(self, query, year=None, search_language=''):
        scraper = tmdb.TMDBMovieScraper(_Settings(), 'en-US', 'us', search_language)
        return [r['id'] for r in scraper.search(query, year)]

    def test_part_2_before_part_1_for_its_year(self):
        self.answer('harry potter and the deathly hallows part 2', '2011',
                    result(12444, 'Harry Potter and the Deathly Hallows: Part 1', '2010-11-17', 25.4),
                    result(12445, 'Harry Potter and the Deathly Hallows: Part 2', '2011-07-12', 25.6))
        self.assertEqual([12445, 12444], self.ids('harry potter and the deathly hallows part 2', '2011'))

    def test_the_year_asked_before_a_more_popular_remake(self):
        self.answer('the crazies', '1973', result(29427, 'The Crazies', '2010-02-26', 30.0),
                    result(27420, 'The Crazies', '1973-03-16', 8.0))
        self.assertEqual([27420, 29427], self.ids('the crazies', '1973'))

    def test_a_title_with_punctuation_matches_one_without(self):
        self.answer('spider man', '2002', result(634649, 'Spider-Man: No Way Home', '2021-12-15', 100.0),
                    result(557, 'Spider-Man', '2002-05-01', 50.0))
        self.assertEqual([557, 634649], self.ids('spider man', '2002'))

    def test_the_original_title_counts(self):
        self.answer('mash', '1970', result(99999, 'Mash Up', '1970-01-01', 3.0),
                    result(636, 'MASH', '1970-01-25', 12.0, 'M*A*S*H'))
        self.assertEqual([636, 99999], self.ids('mash', '1970'))

    def test_the_title_asked_without_a_year(self):
        self.answer('alien', None, result(679, 'Aliens', '1986-07-18', 60.0),
                    result(348, 'Alien', '1979-05-25', 50.0))
        self.assertEqual([348, 679], self.ids('alien'))

    def test_the_most_popular_among_the_best(self):
        self.answer('hamlet', '1990', result(10688, 'Hamlet', '1990-12-19', 9.0),
                    result(10689, 'Hamlet', '1990-05-01', 12.0))
        self.assertEqual([10689, 10688], self.ids('hamlet', '1990'))

    def test_tmdbs_order_kept_when_none_is_named_as_asked(self):
        self.answer('nothing alike', '2000', result(1, 'First', '1999-01-01', 1.0),
                    result(2, 'Second', '2001-01-01', 9.0), result(3, 'Third', '1998-01-01', 5.0))
        self.assertEqual([1, 2, 3], self.ids('nothing alike', '2000'))

    def test_the_exact_title_before_one_that_matches_only_without_its_punctuation(self):
        self.answer('a-b', '2022', result(1, 'A B', '2022-01-01', 50.0),
                    result(2, 'A-B', '2022-01-01', 20.0))
        self.assertEqual([2, 1], self.ids('a-b', '2022'))

    def test_page_2_when_page_1_has_only_a_title_without_its_punctuation(self):
        self.answer('a-b', '2022', result(1, 'A B', '2022-01-01', 50.0), total_pages=2)
        self.answer('a-b', '2022', result(2, 'A-B', '2022-01-01', 20.0), page=2, total_pages=2)
        self.assertEqual([2, 1], self.ids('a-b', '2022'))
        self.assertEqual(2, len(self.asked))

    def test_no_page_2_when_page_1_has_the_exact_title(self):
        self.answer('a-b', '2022', result(2, 'A-B', '2022-01-01', 20.0), total_pages=2)
        self.assertEqual([2], self.ids('a-b', '2022'))
        self.assertEqual(1, len(self.asked))

    def test_page_2_in_the_search_language(self):
        self.answer('a film', '1999', result(1, 'Another Film', '1999-01-01', 1.0), total_pages=2)
        self.answer('a film', '1999', result(2, 'A Film', '1999-01-01', 9.0), page=2, total_pages=2)
        self.assertEqual([2, 1], self.ids('a film', '1999', search_language='de-DE'))
        self.assertEqual(['de-DE', 'de-DE'], [language for _, _, language, _ in self.asked])

    def test_a_failed_page_2_keeps_page_1(self):
        self.answer('a film', '1999', result(1, 'Another Film', '1999-01-01', 1.0), total_pages=2)
        self.pages[('a film', '1999', 2)] = UNREACHABLE
        self.assertEqual([1], self.ids('a film', '1999'))
        self.assertEqual("the search's page 2", self.left_out.call_args[0][0])
