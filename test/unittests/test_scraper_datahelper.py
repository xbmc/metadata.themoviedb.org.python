# pylint: disable=invalid-name,protected-access,too-many-lines
import unittest

from python import scraper_datahelper

class TestScraperDatahelper(unittest.TestCase):
    def test_get_params__find_encoded_with_year(self):
        input_model = ('1', "?action=find&title=%5bRec%5d%202&year=2009")
        expected_output = {'handle': 1, 'action': 'find', 'title': "[Rec] 2", 'year': '2009'}

        actual_output = scraper_datahelper.get_params(input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_get_params__find_encoded_without_year(self):
        input_model = ('1', "?action=find&title=%5bRec%5d%202")
        expected_output = {'handle': 1, 'action': 'find', 'title': "[Rec] 2"}

        actual_output = scraper_datahelper.get_params(input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_get_params__empty_string(self):
        input_model = ('1', '')
        expected_output = {'handle': 1}

        actual_output = scraper_datahelper.get_params(input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_get_params__no_string(self):
        input_model = ('1')
        expected_output = {'handle': 1}

        actual_output = scraper_datahelper.get_params(input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_get_params__some_random_querystring(self):
        input_model = ('1', "?acorns=nested&fragile=Faces%20Around%20The%20World%202&howsit=elliot")
        expected_output = {'handle': 1, 'acorns': 'nested', 'fragile': "Faces Around The World 2",
            'howsit': 'elliot'}

        actual_output = scraper_datahelper.get_params(input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_get_params__some_random_querystring_with_percent(self):
        input_model = ('1', "?acorns=%25100%20nested")
        expected_output = {'handle': 1, 'acorns': '%100 nested'}

        actual_output = scraper_datahelper.get_params(input_model)

        self.assertDictEqual(expected_output, actual_output)


    def test_combine_scraped_details_info_and_ratings(self):
        input_model1 = {'info': {'bit': 1}, 'ratings': {'w1': {'rating': 1, 'votes': 2}}}
        input_model2 = {'info': {'gob': 'bog'}, 'ratings': {'w2': {'rating': 3, 'votes': 4}}}

        expected_output = {'info': {'bit': 1, 'gob': 'bog'},
            'ratings': {'w1': {'rating': 1, 'votes': 2}, 'w2': {'rating': 3, 'votes': 4}}}

        actual_output = scraper_datahelper \
            .combine_scraped_details_info_and_ratings(input_model1, input_model2)

        self.assertDictEqual(expected_output, actual_output)

    def test_combine_scraped_details_info_and_ratings__empty_additional(self):
        input_model1 = {'info': {'bit': 1}, 'ratings': {'w1': {'rating': 1, 'votes': 2}}}
        input_model2 = {}

        expected_output = {'info': {'bit': 1}, 'ratings': {'w1': {'rating': 1, 'votes': 2}}}

        actual_output = scraper_datahelper \
            .combine_scraped_details_info_and_ratings(input_model1, input_model2)

        self.assertDictEqual(expected_output, actual_output)

    def test_combine_scraped_details_info_and_ratings__empty_original(self):
        input_model1 = {}
        input_model2 = {'info': {'gob': 'bog'}, 'ratings': {'w2': {'rating': 3, 'votes': 4}}}

        expected_output = {'info': {'gob': 'bog'}, 'ratings': {'w2': {'rating': 3, 'votes': 4}}}

        actual_output = scraper_datahelper \
            .combine_scraped_details_info_and_ratings(input_model1, input_model2)

        self.assertDictEqual(expected_output, actual_output)

    def test_combine_scraped_details_info_and_ratings__additional_includes_junk(self):
        input_model1 = {'info': {'bit': 1}, 'ratings': {'w1': {'rating': 1, 'votes': 2}}}
        input_model2 = {'info': {'gob': 'bog'}, 'ratings': {'w2': {'rating': 3, 'votes': 4}},
            'junk': {'frankly': "I'm supposed to be on the road righ now"}}

        expected_output = {'info': {'bit': 1, 'gob': 'bog'},
            'ratings': {'w1': {'rating': 1, 'votes': 2}, 'w2': {'rating': 3, 'votes': 4}}}

        actual_output = scraper_datahelper \
            .combine_scraped_details_info_and_ratings(input_model1, input_model2)

        self.assertDictEqual(expected_output, actual_output)

    def test_combine_scraped_details_info_and_ratings__overwrite_info_and_rating(self):
        input_model1 = {'info': {'bit': 1}, 'ratings': {'w1': {'rating': 1, 'votes': 2}}}
        input_model2 = {'info': {'gob': 'bog', 'bit': 11},
            'ratings': {'w2': {'rating': 3, 'votes': 4}, 'w1': {'rating': 11, 'votes': 12}}}

        expected_output = {'info': {'bit': 11, 'gob': 'bog'},
            'ratings': {'w1': {'rating': 11, 'votes': 12}, 'w2': {'rating': 3, 'votes': 4}}}

        actual_output = scraper_datahelper \
            .combine_scraped_details_info_and_ratings(input_model1, input_model2)

        self.assertDictEqual(expected_output, actual_output)


    def test_find_uniqueids_in_text__xml_with_appended_url(self):
        input_model = '''<?xml version='1.0' encoding='utf-8'?>
<movie></movie>
https://www.imdb.com/title/tt0076759/
'''
        expected_output = {'imdb': 'tt0076759'}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__xml_with_embedded_url(self):
        input_model = '''<?xml version='1.0' encoding='utf-8'?>
<movie>
    <url>https://www.imdb.com/title/tt0076759/</url>
</movie>
'''
        expected_output = {'imdb': 'tt0076759'}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__xml_no_url(self):
        input_model = '''<?xml version='1.0' encoding='utf-8'?>
<movie></movie>
'''
        expected_output = {}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__just_url(self):
        input_model = '''https://www.imdb.com/title/tt0076759/
'''
        expected_output = {'imdb': 'tt0076759'}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__just_both_urls(self):
        input_model = '''https://www.imdb.com/title/tt0076759/
https://www.themoviedb.org/movie/11-star-wars
'''
        expected_output = {'imdb': 'tt0076759', 'tmdb': '11'}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__empty(self):
        input_model = ''
        expected_output = {}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__lorem_ipsum(self):
        input_model = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        expected_output = {}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__fakeout_text(self):
        input_model = 'not the imdb id tt1234\r\ntmdb what 4321'
        expected_output = {}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def _test_find_uniqueids_in_text(self, input_model, expected_output):
        actual_output = scraper_datahelper.find_uniqueids_in_text(input_model)
        self.assertDictEqual(expected_output, actual_output)
