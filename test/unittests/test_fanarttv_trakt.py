import unittest
import unittest.mock as mock

from python.lib.tmdbscraper import api_utils, fanarttv, traktratings

NOT_FOUND = {'error': 'remote site unable to fulfill the request\nError code: 404', 'code': 404}
UNREACHABLE = {'error': 'failed to reach the remote site\nReason: timed out'}


def fanart(name, path):
    return {'name': name, 'moviebackground': [
        {'url': 'https://assets.fanart.tv/fanart/' + path, 'id': '1', 'likes': '1'}]}


class _Provider(unittest.TestCase):
    """Answers load_info() by url"""

    def setUp(self):
        self.answers = {}
        load_info = mock.patch.object(api_utils.SESSION, 'load_info', side_effect=self.load_info)
        self.load_info = load_info.start()
        self.addCleanup(load_info.stop)
        left_out = mock.patch.object(api_utils, 'log_left_out')
        self.left_out = left_out.start()
        self.addCleanup(left_out.stop)

    def load_info(self, url, params=None, default=None, resp_type='json'):
        return self.answers.get(url, UNREACHABLE)


class TestFanartTV(_Provider):
    MOVIE = 'https://webservice.fanart.tv/v3/movies/550'
    SET = 'https://webservice.fanart.tv/v3/movies/10'

    def art(self):
        return fanarttv.get_details({'tmdb': '550'}, '', 'en', '10').get('available_art', {})

    def test_the_art_of_the_movie_and_its_set(self):
        self.answers = {self.MOVIE: fanart('A Film', 'm.jpg'), self.SET: fanart('A Set', 's.jpg')}
        art = self.art()
        self.assertIn('fanart', art)
        self.assertIn('set.fanart', art)

    def test_no_art_for_the_movie_404_is_no_failure(self):
        self.answers = {self.MOVIE: NOT_FOUND, self.SET: fanart('A Set', 's.jpg')}
        art = self.art()
        self.assertNotIn('fanart', art)
        self.assertIn('set.fanart', art)
        self.left_out.assert_not_called()

    def test_a_failed_request_for_the_movie_leaves_out_only_its_art(self):
        self.answers = {self.MOVIE: UNREACHABLE, self.SET: fanart('A Set', 's.jpg')}
        art = self.art()
        self.assertNotIn('fanart', art)
        self.assertIn('set.fanart', art)
        self.assertEqual("fanart.tv's art for the movie", self.left_out.call_args[0][0])

    def test_a_failed_request_for_the_set_leaves_out_only_its_art(self):
        self.answers = {self.MOVIE: fanart('A Film', 'm.jpg'), self.SET: UNREACHABLE}
        art = self.art()
        self.assertIn('fanart', art)
        self.assertNotIn('set.fanart', art)
        self.assertEqual("fanart.tv's art for the set", self.left_out.call_args[0][0])


class TestTrakt(_Provider):
    URL = 'https://api.trakt.tv/movies/tt0137523'

    def test_a_rating(self):
        self.answers = {self.URL: {'rating': 8.5, 'votes': 100}}
        self.assertEqual({'ratings': {'trakt': {'votes': 100, 'rating': 8.5}}},
                         traktratings.get_trakt_ratinginfo({'imdb': 'tt0137523'}))

    def test_without_an_imdb_id_trakt_isnt_asked(self):
        self.assertEqual({}, traktratings.get_trakt_ratinginfo({'tmdb': '550'}))
        self.load_info.assert_not_called()

    def test_a_film_trakt_doesnt_know_has_no_rating(self):
        self.answers = {self.URL: NOT_FOUND}
        self.assertEqual({}, traktratings.get_trakt_ratinginfo({'imdb': 'tt0137523'}))

    def test_a_failed_request_gives_its_error(self):
        self.assertIn('error', traktratings.get_trakt_ratinginfo({'imdb': 'tt0137523'}))
