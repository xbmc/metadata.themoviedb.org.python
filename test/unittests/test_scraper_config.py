# pylint: disable=invalid-name,protected-access,too-many-lines
import unittest
from unittest.mock import MagicMock

from python import scraper_config

class TestScraperConfig(unittest.TestCase):
    def test_configure_rating_prefix(self):
        input_details = {'info': {'mpaa': "smash"}}
        input_settings = MagicMock(spec=['getSettingString'])
        input_settings.getSettingString.return_value = "prefix-"

        expected_output = {'info': {'mpaa': "prefix-smash"}}

        actual_output = scraper_config._configure_rating_prefix(input_details, input_settings)

        self.assertEqual(expected_output['info']['mpaa'], actual_output['info']['mpaa'])
        input_settings.getSettingString.assert_called_once_with('certprefix')

    def test_configure_rating_prefix__no_rating(self):
        input_details = {'info': {}}
        input_settings = MagicMock()

        expected_output = {'info': {}}

        actual_output = scraper_config._configure_rating_prefix(input_details, input_settings)

        self.assertEqual(expected_output['info'].get('mpaa'), actual_output['info'].get('mpaa'))


    def test_configure_keeporiginaltitle__true(self):
        original_title = "*original title of a movie"
        input_details = {'info': {'title': "title of a movie",
            'originaltitle': original_title}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'title': original_title}}

        actual_output = scraper_config._configure_keeporiginaltitle(input_details, input_settings)

        self.assertEqual(expected_output['info']['title'], actual_output['info']['title'])
        input_settings.getSettingBool.assert_called_once_with('keeporiginaltitle')

    def test_configure_keeporiginaltitle__false(self):
        title = "title of a movie"
        input_details = {'info': {'title': title,
            'originaltitle': "*original title of a movie"}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = False

        expected_output = {'info': {'title': title}}

        actual_output = scraper_config._configure_keeporiginaltitle(input_details, input_settings)

        self.assertEqual(expected_output['info']['title'], actual_output['info']['title'])
        input_settings.getSettingBool.assert_called_once_with('keeporiginaltitle')


    def test_configure_trailer__true(self):
        trailer = "path to trailer"
        input_details = {'info': {'trailer': trailer}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'trailer': trailer}}

        actual_output = scraper_config._configure_trailer(input_details, input_settings)

        self.assertEqual(expected_output['info']['trailer'], actual_output['info']['trailer'])
        input_settings.getSettingBool.assert_called_once_with('trailer')

    def test_configure_trailer__true_no_trailer(self):
        input_details = {'info': {}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        actual_output = scraper_config._configure_trailer(input_details, input_settings)

        self.assertIsNone(actual_output['info'].get('trailer'))

    def test_configure_trailer__false(self):
        input_details = {'info': {'trailer': "path to trailer"}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = False

        actual_output = scraper_config._configure_trailer(input_details, input_settings)

        self.assertIsNone(actual_output['info'].get('trailer'))
        input_settings.getSettingBool.assert_called_once_with('trailer')


    def test_configure_multiple_studios__true(self):
        studios = ["Studio 1", "Studio 2"]
        input_details = {'info': {'studio': studios}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'studio': studios}}

        actual_output = scraper_config._configure_multiple_studios(input_details, input_settings)

        self.assertListEqual(expected_output['info']['studio'], actual_output['info']['studio'])
        input_settings.getSettingBool.assert_called_once_with('multiple_studios')

    def test_configure_multiple_studios__true_no_studios(self):
        input_details = {'info': {'studio': []}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = True

        expected_output = {'info': {'studio': []}}

        actual_output = scraper_config._configure_multiple_studios(input_details, input_settings)

        self.assertListEqual(expected_output['info']['studio'], actual_output['info']['studio'])
        input_settings.getSettingBool.assert_called_once_with('multiple_studios')

    def test_configure_multiple_studios__false(self):
        studio1 = "Studio 1"
        input_details = {'info': {'studio': [studio1, "Studio 2"]}}
        input_settings = MagicMock(spec=['getSettingBool'])
        input_settings.getSettingBool.return_value = False

        expected_output = {'info': {'studio': [studio1]}}

        actual_output = scraper_config._configure_multiple_studios(input_details, input_settings)

        self.assertListEqual(expected_output['info']['studio'], actual_output['info']['studio'])
        input_settings.getSettingBool.assert_called_once_with('multiple_studios')


    def test_configure_default_rating__imdb(self):
        input_details = {'ratings': {'imdb': {'rating': 1, 'votes': 2}, 'themoviedb': {'rating': 1.1, 'votes': 3}}}
        input_settings = MagicMock(spec=['getSettingString'])
        input_settings.getSettingString.return_value = 'IMDb'

        expected_output = {'ratings': {
            'imdb': {'rating': 1, 'votes': 2, 'default': True},
            'themoviedb': {'rating': 1.1, 'votes': 3, 'default': False}
        }}

        actual_output = scraper_config._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
        input_settings.getSettingString.assert_called_once_with('RatingS')

    def test_configure_default_rating__imdb_no_imdb_fallback_to_tmdb(self):
        input_details = {'ratings': {'themoviedb': {'rating': 1.2, 'votes': 4}}}
        input_settings = MagicMock(spec=['getSettingString'])
        input_settings.getSettingString.return_value = 'IMDb'

        expected_output = {'ratings': {
            'themoviedb': {'rating': 1.2, 'votes': 4, 'default': True}
        }}

        actual_output = scraper_config._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])

    def test_configure_default_rating__tmdb(self):
        input_details = {'ratings': {'imdb': {'rating': 1, 'votes': 5}, 'themoviedb': {'rating': 1.3, 'votes': 6}}}
        input_settings = MagicMock(spec=['getSettingString'])
        input_settings.getSettingString.return_value = 'TMDb'

        expected_output = {'ratings': {
            'imdb': {'rating': 1, 'votes': 5, 'default': False},
            'themoviedb': {'rating': 1.3, 'votes': 6, 'default': True}
        }}

        actual_output = scraper_config._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
        input_settings.getSettingString.assert_called_once_with('RatingS')

    def test_configure_default_rating__tmdb_no_tmdb_fallback_to_imdb(self):
        input_details = {'ratings': {'imdb': {'rating': 1, 'votes': 7}}}
        input_settings = MagicMock(spec=['getSettingString'])
        input_settings.getSettingString.return_value = 'TMDb'

        expected_output = {'ratings': {
            'imdb': {'rating': 1, 'votes': 7, 'default': True}
        }}

        actual_output = scraper_config._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
        input_settings.getSettingString.assert_called_once_with('RatingS')

    def test_configure_default_rating__tmdb_no_ratings(self):
        input_details = {'ratings': {}}
        input_settings = MagicMock(spec=['getSettingString'])
        input_settings.getSettingString.return_value = 'TMDb'

        expected_output = {'ratings': {}}

        actual_output = scraper_config._configure_default_rating(input_details, input_settings)

        self.assertDictEqual(expected_output['ratings'], actual_output['ratings'])
