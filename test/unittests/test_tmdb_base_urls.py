import unittest
import unittest.mock as mock

from python.lib.tmdbscraper import tmdb


class _Settings:
    """The add-on's settings, where the image URLs are kept between calls"""

    def __init__(self, **values):
        self.values = values
        self.saved = {}

    def getSettingString(self, key):
        return self.values.get(key, '')

    def setSetting(self, key, value):
        self.values[key] = value
        self.saved[key] = value


def _date(**ago):
    return str(tmdb._get_date_numeric(tmdb.datetime.now() - tmdb.timedelta(**ago)))


STORED = {'originalUrl': 'https://stored/t/p/original', 'previewUrl': 'https://stored/t/p/w780'}


class TestBaseUrls(unittest.TestCase):
    def load(self, settings, configuration):
        with mock.patch.object(tmdb.tmdbapi, 'get_configuration',
                               return_value=configuration) as get_configuration:
            urls = tmdb._load_base_urls(settings)
        return urls, get_configuration.call_count

    def test_fresh_urls_are_used_without_asking(self):
        settings = _Settings(lastUpdated=_date(days=1), **STORED)
        urls, asked = self.load(settings, None)
        self.assertEqual({'original': STORED['originalUrl'], 'preview': STORED['previewUrl']}, urls)
        self.assertEqual(0, asked)

    def test_stale_urls_are_asked_for_and_saved(self):
        settings = _Settings(lastUpdated=_date(days=31), **STORED)
        urls, asked = self.load(settings, {'images': {'secure_base_url': 'https://new/t/p/'}})
        self.assertEqual({'original': 'https://new/t/p/original', 'preview': 'https://new/t/p/w780'},
                         urls)
        self.assertEqual(1, asked)
        self.assertEqual({'originalUrl', 'previewUrl', 'lastUpdated'}, set(settings.saved))

    def test_unchanged_urls_are_not_saved_again(self):
        settings = _Settings(lastUpdated=_date(days=31), **STORED)
        self.load(settings, {'images': {'secure_base_url': 'https://stored/t/p/'}})
        self.assertEqual({'lastUpdated'}, set(settings.saved))

    def test_a_failed_configuration_keeps_the_stored_urls(self):
        settings = _Settings(lastUpdated=_date(days=31), **STORED)
        urls, _ = self.load(settings, {'error': 'failed to reach the remote site'})
        self.assertEqual({'original': STORED['originalUrl'], 'preview': STORED['previewUrl']}, urls)
        self.assertEqual({}, settings.saved)

    def test_a_failed_configuration_without_stored_urls_gives_the_documented_base(self):
        settings = _Settings()
        urls, _ = self.load(settings, {'error': 'failed to reach the remote site'})
        self.assertEqual({'original': 'https://image.tmdb.org/t/p/original',
                          'preview': 'https://image.tmdb.org/t/p/w780'}, urls)
        self.assertEqual({}, settings.saved)

    def test_a_configuration_without_its_base_gives_the_documented_base(self):
        urls, _ = self.load(_Settings(), {'images': {}})
        self.assertEqual('https://image.tmdb.org/t/p/original', urls['original'])

    def test_a_date_that_isnt_a_number_is_stale(self):
        settings = _Settings(lastUpdated='0.x', **STORED)
        _, asked = self.load(settings, {'images': {'secure_base_url': 'https://stored/t/p/'}})
        self.assertEqual(1, asked)
