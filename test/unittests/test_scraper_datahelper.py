# pylint: disable=invalid-name,protected-access,too-many-lines
import unittest
from unittest.mock import MagicMock

from python import scraper_datahelper

# tests cover all functions, probably missing plenty of nuance

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


    def test_configure_keeporiginaltitle__true(self):
        original_title = "*original title of a movie"
        input_details = {'info': {'title': "title of a movie",
            'original_title': original_title}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'title': original_title}}

        actual_output = scraper_datahelper._configure_keeporiginaltitle(input_details, input_settings)

        self.assertEqual(expected_output['info']['title'], actual_output['info']['title'])
        input_settings.getSettingBool.assert_called_once_with('keeporiginaltitle')

    def test_configure_keeporiginaltitle__false(self):
        title = "title of a movie"
        input_details = {'info': {'title': title,
            'original_title': "*original title of a movie"}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = False

        expected_output = {'info': {'title': title}}

        actual_output = scraper_datahelper._configure_keeporiginaltitle(input_details, input_settings)

        self.assertEqual(expected_output['info']['title'], actual_output['info']['title'])
        input_settings.getSettingBool.assert_called_once_with('keeporiginaltitle')


    def test_configure_trailer__true(self):
        trailer = "path to trailer"
        input_details = {'info': {'trailer': trailer}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'trailer': trailer}}

        actual_output = scraper_datahelper._configure_trailer(input_details, input_settings)

        self.assertEqual(expected_output['info']['trailer'], actual_output['info']['trailer'])
        input_settings.getSettingBool.assert_called_once_with('trailer')

    def test_configure_trailer__true_no_trailer(self):
        input_details = {'info': {}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        actual_output = scraper_datahelper._configure_trailer(input_details, input_settings)

        self.assertIsNone(actual_output['info'].get('trailer'))

    def test_configure_trailer__false(self):
        input_details = {'info': {'trailer': "path to trailer"}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = False

        actual_output = scraper_datahelper._configure_trailer(input_details, input_settings)

        self.assertIsNone(actual_output['info'].get('trailer'))
        input_settings.getSettingBool.assert_called_once_with('trailer')


    def test_configure_multiple_studios__true(self):
        studios = ["Studio 1", "Studio 2"]
        input_details = {'info': {'studio': studios}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'studio': studios}}

        actual_output = scraper_datahelper._configure_multiple_studios(input_details, input_settings)

        self.assertListEqual(expected_output['info']['studio'], actual_output['info']['studio'])
        input_settings.getSettingBool.assert_called_once_with('multiple_studios')

    def test_configure_multiple_studios__true_no_studios(self):
        input_details = {'info': {'studio': []}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'studio': []}}

        actual_output = scraper_datahelper._configure_multiple_studios(input_details, input_settings)

        self.assertListEqual(expected_output['info']['studio'], actual_output['info']['studio'])
        input_settings.getSettingBool.assert_called_once_with('multiple_studios')

    def test_configure_multiple_studios__false(self):
        studio1 = "Studio 1"
        input_details = {'info': {'studio': [studio1, "Studio 2"]}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = False

        expected_output = {'info': {'studio': [studio1]}}

        actual_output = scraper_datahelper._configure_multiple_studios(input_details, input_settings)

        self.assertListEqual(expected_output['info']['studio'], actual_output['info']['studio'])
        input_settings.getSettingBool.assert_called_once_with('multiple_studios')


    def test_configure_default_rating__imdb(self):
        input_details = {'ratings': {'imdb': {'rating': 1, 'votes': 2}, 'tmdb': {'rating': 1.1, 'votes': 3}}}
        input_settings = MagicMock(spec=['getSetting'])
        input_settings.getSetting.return_value = 'IMDb'

        expected_output = {'ratings': {
            'imdb': {'rating': 1, 'votes': 2, 'default': True},
            'tmdb': {'rating': 1.1, 'votes': 3, 'default': False}
        }}

        actual_output = scraper_datahelper._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
        input_settings.getSetting.assert_called_once_with('RatingS')

    def test_configure_default_rating__imdb_no_imdb_fallback_to_tmdb(self):
        input_details = {'ratings': {'tmdb': {'rating': 1.2, 'votes': 4}}}
        input_settings = MagicMock(spec=['getSetting'])
        input_settings.getSetting.return_value = 'IMDb'

        expected_output = {'ratings': {
            'tmdb': {'rating': 1.2, 'votes': 4, 'default': True}
        }}

        actual_output = scraper_datahelper._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])

    def test_configure_default_rating__tmdb(self):
        input_details = {'ratings': {'imdb': {'rating': 1, 'votes': 5}, 'tmdb': {'rating': 1.3, 'votes': 6}}}
        input_settings = MagicMock(spec=['getSetting'])
        input_settings.getSetting.return_value = 'TMDb'

        expected_output = {'ratings': {
            'imdb': {'rating': 1, 'votes': 5, 'default': False},
            'tmdb': {'rating': 1.3, 'votes': 6, 'default': True}
        }}

        actual_output = scraper_datahelper._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
        input_settings.getSetting.assert_called_once_with('RatingS')

    def test_configure_default_rating__tmdb_no_tmdb_fallback_to_imdb(self):
        input_details = {'ratings': {'imdb': {'rating': 1, 'votes': 7}}}
        input_settings = MagicMock(spec=['getSetting'])
        input_settings.getSetting.return_value = 'TMDb'

        expected_output = {'ratings': {
            'imdb': {'rating': 1, 'votes': 7, 'default': True}
        }}

        actual_output = scraper_datahelper._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
        input_settings.getSetting.assert_called_once_with('RatingS')

    def test_configure_default_rating__tmdb_no_ratings(self):
        input_details = {'ratings': {}}
        input_settings = MagicMock(spec=['getSetting'])
        input_settings.getSetting.return_value = 'TMDb'

        expected_output = {'ratings': {}}

        actual_output = scraper_datahelper._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])


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
        input_model = '''<?xml version='1.0' encoding='utf-8'?>
https://www.imdb.com/title/tt0076759/
'''
        expected_output = {'imdb': 'tt0076759'}
        self._test_find_uniqueids_in_text(input_model, expected_output)

    def test_find_uniqueids_in_text__both_urls(self):
        input_model = '''<?xml version='1.0' encoding='utf-8'?>
https://www.imdb.com/title/tt0076759/
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
