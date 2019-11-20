from datetime import datetime, timedelta
from requests.exceptions import ConnectionError as RequestsConnectionError, Timeout, RequestException

import tmdbsimple

# Same key as built-in XML scraper
tmdbsimple.API_KEY = 'f090bb54758cabf231fb605d3e3e0468'

class TMDBMovieScraper(object):
    def __init__(self, source_settings, language):
        self.settings = source_settings
        self.language = language
        self._urls = None

    @property
    def urls(self):
        if not self._urls:
            self._urls = _load_base_urls(self.settings)
        return self._urls

    def search(self, title, year=None):
        try:
            response = tmdbsimple.Search().movie(query=title, year=year, language=self.language)
        except (Timeout, RequestsConnectionError, RequestException) as ex:
            return _format_error_message(ex)
        result = response['results']
        urls = self.urls
        for item in result:
            if item.get('poster_path'):
                item['poster_path'] = urls['preview'] + item['poster_path']
            if item.get('backdrop_path'):
                item['backdrop_path'] = urls['preview'] + item['backdrop_path']
        return result

    def get_details(self, uniqueids):
        media_id = uniqueids.get('imdb') or uniqueids.get('tmdb')
        details = self._gather_details(media_id)
        if not details:
            return None
        return self._assemble_details(*details)

    def _gather_details(self, media_id):
        movie = _get_movie(media_id, self.language)
        if not movie:
            return None

        # don't specify language to get all the artworks and English text for fallback
        movie_fallback = _get_movie(media_id)

        collection = _get_moviecollection(movie['belongs_to_collection'].get('id'), self.language) if \
            movie['belongs_to_collection'] else None
        collection_fallback = _get_moviecollection(movie['belongs_to_collection'].get('id')) if \
            movie['belongs_to_collection'] else None

        return movie, movie_fallback, collection, collection_fallback

    def _assemble_details(self, movie, movie_fallback, collection, collection_fallback):
        info = {
            'title': movie['title'],
            'originaltitle': movie['original_title'],
            'plot': movie.get('overview') or movie_fallback.get('overview'),
            'tagline': movie.get('tagline') or movie_fallback.get('tagline'),
            'studio': _get_names(movie['production_companies']),
            'genre': _get_names(movie['genres']),
            'country': _get_names(movie['production_countries']),
            'credits': _get_cast_members(movie['casts'], 'crew', 'Writing', ['Screenplay', 'Writer', 'Author']),
            'director': _get_cast_members(movie['casts'], 'crew', 'Directing', ['Director']),
            'premiered': movie['release_date']
        }

        if 'countries' in movie['releases']:
            certprefix = self.settings.getSetting('certprefix')
            certcountry = self.settings.getSetting('tmdbcertcountry').upper()
            for country in movie['releases']['countries']:
                if country['iso_3166_1'] == certcountry and country['certification']:
                    info['mpaa'] = certprefix + country['certification']
                    break

        trailer = _get_trailer(movie.get('trailers', {}), movie_fallback.get('trailers', {}))
        if trailer:
            info['trailer'] = trailer
        if collection:
            info['set'] = collection.get('name') or collection_fallback.get('name')
            info['setoverview'] = collection.get('overview') or collection_fallback.get('overview')
        if movie.get('runtime'):
            info['duration'] = movie['runtime'] * 60

        ratings = {'tmdb': {'rating': movie['vote_average'], 'votes': movie['vote_count']}}
        uniqueids = {'tmdb': movie['id'], 'imdb': movie['imdb_id']}
        cast = [{
                'name': actor['name'],
                'role': actor['character'],
                'thumbnail': self.urls['original'] + actor['profile_path']
                    if actor['profile_path'] else "",
                'order': actor['order']
            }
            for actor in movie['casts'].get('cast', [])
        ]
        available_art = _parse_artwork(movie_fallback, collection_fallback, self.urls, self.language)

        return {'info': info, 'ratings': ratings, 'uniqueids': uniqueids, 'cast': cast,
            'available_art': available_art}

def _get_movie(mid, language=None):
    details = 'trailers,releases,casts,' if language is not None else 'trailers,images'
    movie = tmdbsimple.Movies(mid)
    try:
        return movie.info(language=language, append_to_response=details)
    except (Timeout, RequestsConnectionError, RequestException) as ex:
        return _format_error_message(ex)

def _get_moviecollection(collection_id, language=None):
    if not collection_id:
        return None
    details = '' if language is not None else 'images'
    collection = tmdbsimple.Collections(collection_id)
    try:
        return collection.info(language=language, append_to_response=details)
    except (Timeout, RequestsConnectionError, RequestException) as ex:
        return _format_error_message(ex)


def _parse_artwork(movie, collection, urlbases, language):
    posters = _get_posters(movie['images']['posters'], urlbases, language)
    fanart = _get_images(movie['images']['backdrops'], urlbases, language)

    setposters = []
    setfanart = []
    if collection:
        setposters = _get_posters(collection['images']['posters'], urlbases, language)
        setfanart = _get_images(collection['images']['backdrops'], urlbases, language)

    return {'poster': posters, 'fanart': fanart, 'set.poster': setposters, 'set.fanart': setfanart}

def _get_posters(posterlist, urlbases, language):
    posters = _get_images(posterlist, urlbases, language)

    # Add backup English posters
    if language != 'en':
        posters.extend(_get_images(posterlist, urlbases, 'en'))

    # Add any poster if nothing set so far
    if not posters:
        posters = _get_images(posterlist, urlbases)

    return posters

def _get_images(imagelist, urlbases, language=None):
    result = []
    for img in imagelist:
        if language and img['iso_639_1'] and img['iso_639_1'] != language:
            continue
        result.append({
            'url': urlbases['original'] + img['file_path'],
            'preview': urlbases['preview'] + img['file_path'],
        })
    return result

def _get_date_numeric(datetime_):
    return (datetime_ - datetime(1970, 1, 1)).total_seconds()

def _load_base_urls(settings):
    urls = {}
    urls['original'] = settings.getSetting('originalUrl')
    urls['preview'] = settings.getSetting('previewUrl')
    last_updated = settings.getSetting('lastUpdated')
    if not urls['original'] or not urls['preview'] or not last_updated or \
            float(last_updated) < _get_date_numeric(datetime.now() - timedelta(days=30)):
        conf = tmdbsimple.Configuration().info()
        if conf:
            urls['original'] = conf['images']['base_url'] + 'original'
            urls['preview'] = conf['images']['base_url'] + 'w780'
            settings.setSetting('originalUrl', urls['original'])
            settings.setSetting('previewUrl', urls['preview'])
            settings.setSetting('lastUpdated', str(_get_date_numeric(datetime.now())))
    return urls

def _get_trailer(trailers, fallback):
    if trailers.get('youtube'):
        return 'plugin://plugin.video.youtube/?action=play_video&videoid='+trailers['youtube'][0]['source']
    if fallback.get('youtube'):
        return 'plugin://plugin.video.youtube/?action=play_video&videoid='+fallback['youtube'][0]['source']
    return None

def _get_names(items):
    return [item['name'] for item in items] if items else []

def _get_cast_members(casts, casttype, department, jobs):
    result = []
    if casttype in casts:
        for cast in casts[casttype]:
            if cast['department'] == department and cast['job'] in jobs:
                result.append(cast['name'])
    return result

def _format_error_message(ex):
    message = type(ex).__name__
    if hasattr(ex, 'message'):
        message += ": " + ex.message
    return {'error': message}
