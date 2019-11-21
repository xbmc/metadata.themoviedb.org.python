# pylint: disable=invalid-name,protected-access,too-many-lines
import unittest

from python.lib.tmdbscraper import get_imdb_id

class TestScraperTMDBScraper(unittest.TestCase):
    def test_get_imdbid_from_uniqueids(self):
        input_model = {'imdb': 'tt1234', 'tmdb': '4321'}
        expected_output = 'tt1234'

        actual_output = get_imdb_id(input_model)

        self.assertEqual(expected_output, actual_output)

    def test_get_imdbid_from_uniqueids__no_imdb(self):
        input_model = {'tmdb': '4321'}

        actual_output = get_imdb_id(input_model)

        self.assertIsNone(actual_output)

    def test_get_imdbid_from_uniqueids__malformed_imdb(self):
        input_model = {'imdb': '4321'}

        actual_output = get_imdb_id(input_model)

        self.assertIsNone(actual_output)
