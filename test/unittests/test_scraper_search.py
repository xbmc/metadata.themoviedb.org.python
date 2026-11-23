import unittest

from test.unittests import kodi_stubs


class TestScraperSearch(unittest.TestCase):
    """python/scraper.py's search, with Kodi's modules stood in for and the network faked"""

    def setUp(self):
        self.scraper, self.kodi, self.network = kodi_stubs.load_scraper(self)

    def test_a_trailing_article_after_a_comma_is_dropped(self):
        self.assertEqual('matrix', self.scraper._strip_trailing_article('Matrix, The'))

    def test_a_title_ending_in_a_word_like_an_article_keeps_it(self):
        self.assertEqual('plan a', self.scraper._strip_trailing_article('Plan A'))
        self.assertEqual('the matrix', self.scraper._strip_trailing_article('The Matrix'))

    def test_plan_a_is_searched_as_plan_a(self):
        kodi_stubs.run(self.scraper, 'action=find', 'title=Plan A', 'year=2021')
        self.assertTrue(any('query=plan+a' in url for url in self.network.asked), self.network.asked)

    def test_a_search_lists_what_it_found(self):
        kodi_stubs.run(self.scraper, 'action=find', 'title=A Film', 'year=1999')
        self.assertEqual(['{"tmdb": "550"}'], self.kodi.items)
        self.assertEqual([True], self.kodi.ended)
