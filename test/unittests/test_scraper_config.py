# pylint: disable=invalid-name,protected-access,too-many-lines,unused-argument
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
        input_settings = MagicMock(spec=[])

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


class TestPathSpecificSettings(unittest.TestCase):
    def test_getSettingString(self):
        input_settings_dict = {'setting': 'value'}
        input_logger = build_input_logger()

        expected_output = 'value'

        actual_output = build_path_settings(input_settings_dict, input_logger).getSettingString('setting')

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(input_logger.call_count, 0)

    def test_getSettingString__doesnt_exist(self):
        input_settings_dict = {}
        input_logger = build_input_logger()

        expected_output = ''

        actual_output = build_path_settings(input_settings_dict, input_logger).getSettingString('setting')

        self.assertEqual(expected_output, actual_output)
        input_logger.assert_called_once_with("requested setting (setting) was not found.")

    def test_getSettingBool__true(self):
        self._inner_test_getSettingBool__success(True, True)

    def test_getSettingBool__false(self):
        self._inner_test_getSettingBool__success(False, False)

    def _inner_test_getSettingBool__success(self, setting_value, expected_output):
        input_settings_dict = {'setting': setting_value}
        input_logger = build_input_logger()

        actual_output = build_path_settings(input_settings_dict, input_logger).getSettingBool('setting')

        self.assertEqual(expected_output, actual_output)
        self.assertEqual(input_logger.call_count, 0)

    def test_getSettingBool__bad_value(self):
        self._inner_test_getSettingBool__failure({'setting': 'zilch'},
            'failed to load value "zilch" for setting setting')

    def test_getSettingBool__doesnt_exist(self):
        self._inner_test_getSettingBool__failure({}, "requested setting (setting) was not found.")

    def _inner_test_getSettingBool__failure(self, input_settings_dict, fail_message):
        input_logger = build_input_logger()

        expected_output = False

        actual_output = build_path_settings(input_settings_dict, input_logger).getSettingBool('setting')

        self.assertEqual(expected_output, actual_output)
        input_logger.assert_called_once_with(fail_message)

def build_path_settings(input_settings_dict, input_logger):
    return scraper_config.PathSpecificSettings(input_settings_dict, input_logger)

def build_input_logger():
    def input_logger_fn(msg: str): pass
    return MagicMock(spec=input_logger_fn)
