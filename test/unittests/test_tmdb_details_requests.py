import unittest
import unittest.mock as mock

from python.lib.tmdbscraper import api_utils, tmdb

NOT_FOUND = {'error': 'remote site unable to fulfill the request\nError code: 404', 'code': 404}
UNREACHABLE = {'error': 'failed to reach the remote site\nReason: timed out'}
MOVIE = 'trailers,images,releases,credits,keywords'


def image(language, path):
    return {'iso_639_1': language, 'file_path': path}


IMAGES = {'posters': [image('en', '/p_en.jpg'), image('de', '/p_de.jpg'), image(None, '/p_none.jpg')],
          'backdrops': [image('en', '/b_en.jpg'), image(None, '/b_none.jpg')],
          'logos': [image('en', '/l_en.png')]}
# Movie 3's only English logo is an SVG, which the add-on can't use; set 88 has posters only in
# Turkish and Chinese
MOVIE_IMAGES = {'3': dict(IMAGES, logos=[image('en', '/l_en.svg'), image('fr', '/l_fr.png')])}
SET_IMAGES = {88: {'posters': [image('tr', '/sp_tr.jpg'), image('zh', '/sp_zh.jpg')], 'backdrops': []}}
TEXT = {'en-US': ('An English plot.', 'An English tagline.', 'en1'),
        'de-DE': ('Eine deutsche Handlung.', 'Ein Slogan.', 'de1'),
        'nl-NL': ('', '', None)}
SET_TEXT = {'en-US': ('The Set', 'An English set.'), 'de-DE': ('Die Reihe', 'Eine Reihe.'),
            'nl-NL': ('De Reeks', '')}
SETS = {'1': 77, '3': None, '4': 88, '5': 77}


def by_language(images, languages):
    """The images include_image_language asks for"""
    if not languages:
        return images
    wanted = set(languages.split(','))
    return {kind: [i for i in found if (i['iso_639_1'] or 'null') in wanted]
            for kind, found in images.items()}


class _Settings:
    def getSettingString(self, key):
        return {'originalUrl': 'https://x/original', 'previewUrl': 'https://x/w780',
                'lastUpdated': str(tmdb._get_date_numeric(tmdb.datetime.now()))}[key]


class TestDetailsRequests(unittest.TestCase):
    """The TMDb requests made for a movie and its set, against a stand-in TMDb"""

    def setUp(self):
        self.calls = []
        self.failing = {}  # (kind, language) -> the error to answer with
        for name in ('get_movie', 'get_collection', 'get_movie_images', 'get_collection_images'):
            patch = mock.patch.object(tmdb.tmdbapi, name, side_effect=getattr(self, name))
            patch.start()
            self.addCleanup(patch.stop)
        left_out = mock.patch.object(api_utils, 'log_left_out')
        self.left_out = left_out.start()
        self.addCleanup(left_out.stop)
        # Each test asks afresh, with a session of its own: the add-on keeps answers for its
        # later calls
        session = mock.patch.object(api_utils, 'SESSION', api_utils.Session())
        session.start()
        self.addCleanup(session.stop)

    def get_movie(self, mid, language=None, append_to_response=None, image_languages=None):
        self.calls.append(('movie', language, append_to_response, image_languages))
        if ('movie', language) in self.failing:
            return self.failing[('movie', language)]
        plot, tagline, trailer = TEXT[language or 'en-US']
        movie = {'id': mid, 'title': 'Title ' + (language or 'en-US'), 'original_title': 'Title',
                 'overview': plot, 'tagline': tagline,
                 'trailers': {'youtube': [{'source': trailer}] if trailer else []}}
        if append_to_response and 'images' in append_to_response:
            movie['images'] = by_language(MOVIE_IMAGES.get(str(mid), IMAGES), image_languages)
        if append_to_response and 'credits' in append_to_response:
            collection = SETS.get(str(mid))
            movie.update(production_companies=[], production_countries=[], genres=[],
                         credits={'cast': [], 'crew': []}, release_date='2000-01-01',
                         keywords={'keywords': []}, releases={'countries': []}, runtime=100,
                         vote_average=7.0, vote_count=10, imdb_id='tt0000001',
                         spoken_languages=[], original_language='en',
                         belongs_to_collection={'id': collection} if collection else None)
        return movie

    def get_collection(self, collection_id, language=None, append_to_response=None,
                       image_languages=None):
        self.calls.append(('collection', language, append_to_response, image_languages))
        if ('collection', language) in self.failing:
            return self.failing[('collection', language)]
        name, overview = SET_TEXT[language]
        result = {'id': collection_id, 'name': name, 'overview': overview}
        if append_to_response == 'images':
            result['images'] = by_language(SET_IMAGES.get(collection_id, IMAGES), image_languages)
        return result

    def get_movie_images(self, mid):
        self.calls.append(('movie images', None, None, None))
        if ('movie images', None) in self.failing:
            return self.failing[('movie images', None)]
        return MOVIE_IMAGES.get(str(mid), IMAGES)

    def get_collection_images(self, collection_id):
        self.calls.append(('collection images', None, None, None))
        return SET_IMAGES.get(collection_id, IMAGES)

    def details(self, language, mid, fail=None):
        self.failing.update(fail or {})
        return tmdb.TMDBMovieScraper(_Settings(), language, 'us').get_details({'tmdb': str(mid)})

    def assertArt(self, details, kind, url):
        self.assertTrue(any(i['url'].endswith(url) for i in details['available_art'][kind]),
                        (kind, url, details['available_art'].get(kind)))

    def test_a_movie_in_a_set_one_request_each_with_text_free_images(self):
        details = self.details('en-US', 1)
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null'),
                          ('collection', 'en-US', 'images', 'en,xx,null')], self.calls)
        self.assertArt(details, 'fanart', '/b_none.jpg')
        self.assertArt(details, 'keyart', '/p_none.jpg')
        self.assertArt(details, 'set.fanart', '/b_none.jpg')
        self.assertEqual('The Set', details['info']['set'])
        self.assertEqual('An English plot.', details['info']['plot'])
        self.assertTrue(details['info']['trailer'].endswith('en1'))

    def test_a_movie_in_no_set_one_request(self):
        details = self.details('en-US', 2)
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null')], self.calls)
        self.assertNotIn('set', details['info'])

    def test_all_text_in_the_language_no_english_request_and_its_posters(self):
        details = self.details('de-DE', 1)
        self.assertEqual([('movie', 'de-DE', MOVIE, 'de,en,xx,null'),
                          ('collection', 'de-DE', 'images', 'de,en,xx,null')], self.calls)
        self.assertEqual('Eine deutsche Handlung.', details['info']['plot'])
        self.assertEqual('Die Reihe', details['info']['set'])
        self.assertArt(details, 'poster', '/p_de.jpg')

    def test_text_the_language_lacks_asked_for_in_english_only(self):
        details = self.details('nl-NL', 1)
        self.assertEqual([('movie', 'nl-NL', MOVIE, 'nl,en,xx,null'), ('movie', 'en-US', 'trailers', None),
                          ('collection', 'nl-NL', 'images', 'nl,en,xx,null'),
                          ('collection', 'en-US', None, None)], self.calls)
        self.assertEqual('An English plot.', details['info']['plot'])
        self.assertEqual('An English tagline.', details['info']['tagline'])
        self.assertTrue(details['info']['trailer'].endswith('en1'))
        self.assertEqual('De Reeks', details['info']['set'])
        self.assertEqual('An English set.', details['info']['setoverview'])
        self.assertArt(details, 'set.poster', '/p_en.jpg')

    def test_a_movie_tmdb_hasnt_gives_its_404(self):
        details = self.details('en-US', 1, fail={('movie', 'en-US'): NOT_FOUND})
        self.assertEqual(404, details.get('code'))
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null')], self.calls)

    def test_a_set_tmdb_no_longer_has_is_no_set(self):
        details = self.details('en-US', 1, fail={('collection', 'en-US'): NOT_FOUND})
        self.assertNotIn('error', details)
        self.assertNotIn('set', details['info'])
        self.left_out.assert_not_called()

    def test_an_unusable_logo_asks_for_every_image(self):
        details = self.details('en-US', 3)
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null'), ('movie images', None, None, None)],
                         self.calls)
        self.assertArt(details, 'clearlogo', '/l_fr.png')
        self.assertFalse(any(i['url'].endswith('.svg') for i in details['available_art']['clearlogo']))

    def test_a_set_without_usable_posters_asks_for_its_every_image(self):
        details = self.details('en-US', 4)
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null'),
                          ('collection', 'en-US', 'images', 'en,xx,null'),
                          ('collection images', None, None, None)], self.calls)
        self.assertArt(details, 'set.poster', '/sp_tr.jpg')

    # A part that fails, after its request's retry, is left out and logged; a 404 for an English
    # request made after the first is "nothing there", not a failure

    def test_failed_english_text_is_left_out(self):
        details = self.details('nl-NL', 1, fail={('movie', 'en-US'): UNREACHABLE})
        self.assertNotIn('error', details)
        self.assertEqual('', details['info']['plot'] or '')
        self.assertEqual('the English text', self.left_out.call_args[0][0])

    def test_english_text_gone_since_is_no_failure(self):
        details = self.details('nl-NL', 1, fail={('movie', 'en-US'): NOT_FOUND})
        self.assertNotIn('error', details)
        self.left_out.assert_not_called()

    def test_a_failed_set_is_left_out(self):
        details = self.details('en-US', 1, fail={('collection', 'en-US'): UNREACHABLE})
        self.assertNotIn('error', details)
        self.assertFalse(details['info'].get('set'))
        self.assertEqual('the set', self.left_out.call_args[0][0])

    def test_failed_english_set_text_is_left_out(self):
        details = self.details('nl-NL', 1, fail={('collection', 'en-US'): UNREACHABLE})
        self.assertNotIn('error', details)
        self.assertEqual('De Reeks', details['info']['set'])
        self.assertEqual("the set's English name and overview", self.left_out.call_args[0][0])

    def test_english_set_text_gone_since_is_no_failure(self):
        details = self.details('nl-NL', 1, fail={('collection', 'en-US'): NOT_FOUND})
        self.assertNotIn('error', details)
        self.assertEqual('De Reeks', details['info']['set'])
        self.left_out.assert_not_called()

    def test_failed_images_in_every_language_are_left_out(self):
        details = self.details('en-US', 3, fail={('movie images', None): UNREACHABLE})
        self.assertNotIn('error', details)
        self.assertEqual("the movie's images in other languages", self.left_out.call_args[0][0])

    # A set's answers are kept for its later movies

    def two_of_a_set(self, fail_first=None):
        """Movies 1 and 5, both of set 77, in turn, in one interpreter"""
        scraper = tmdb.TMDBMovieScraper(_Settings(), 'en-US', 'us')
        self.failing.update(fail_first or {})
        first = scraper.get_details({'tmdb': '1'})
        self.failing.clear()
        return first, scraper.get_details({'tmdb': '5'})

    def test_two_movies_of_a_set_ask_for_it_once(self):
        first, second = self.two_of_a_set()
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null'),
                          ('collection', 'en-US', 'images', 'en,xx,null'),
                          ('movie', 'en-US', MOVIE, 'en,xx,null')], self.calls)
        self.assertEqual('The Set', first['info']['set'])
        self.assertEqual('The Set', second['info']['set'])
        self.assertArt(second, 'set.fanart', '/b_none.jpg')

    # So are a movie's, for another copy or edition of it

    def test_a_movie_asked_for_again_is_answered_from_what_was_kept(self):
        scraper = tmdb.TMDBMovieScraper(_Settings(), 'en-US', 'us')
        first = scraper.get_details({'tmdb': '1'})
        second = scraper.get_details({'tmdb': '1'})
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null'),
                          ('collection', 'en-US', 'images', 'en,xx,null')], self.calls)
        self.assertEqual(first['info'], second['info'])
        self.assertEqual(first['available_art'], second['available_art'])

    def test_a_movie_in_another_language_is_asked_for(self):
        tmdb.TMDBMovieScraper(_Settings(), 'en-US', 'us').get_details({'tmdb': '1'})
        tmdb.TMDBMovieScraper(_Settings(), 'de-DE', 'us').get_details({'tmdb': '1'})
        self.assertEqual(2, [kind for kind, *_ in self.calls].count('movie'))

    def test_a_movie_that_failed_is_asked_for_again(self):
        scraper = tmdb.TMDBMovieScraper(_Settings(), 'en-US', 'us')
        self.failing[('movie', 'en-US')] = UNREACHABLE
        self.assertIn('error', scraper.get_details({'tmdb': '1'}))
        self.failing.clear()
        self.assertNotIn('error', scraper.get_details({'tmdb': '1'}))
        self.assertEqual(2, [kind for kind, *_ in self.calls].count('movie'))

    def test_a_set_that_failed_is_asked_for_again_by_the_next_movie(self):
        first, second = self.two_of_a_set(fail_first={('collection', 'en-US'): UNREACHABLE})
        self.assertEqual([('movie', 'en-US', MOVIE, 'en,xx,null'),
                          ('collection', 'en-US', 'images', 'en,xx,null'),
                          ('movie', 'en-US', MOVIE, 'en,xx,null'),
                          ('collection', 'en-US', 'images', 'en,xx,null')], self.calls)
        self.assertFalse(first['info'].get('set'))
        self.assertEqual('The Set', second['info']['set'])
