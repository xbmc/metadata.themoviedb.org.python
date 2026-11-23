import re
from datetime import datetime, timedelta
from . import api_utils, tmdbapi

class TMDBMovieScraper(object):
    def __init__(self, url_settings, language, certification_country, search_language=""):
        self.url_settings = url_settings
        self.language = language
        self.certification_country = certification_country
        if(search_language == ""):
            self.search_language = language
        else:
            self.search_language = search_language
        self._urls = None

    @property
    def urls(self):
        if not self._urls:
            self._urls = _load_base_urls(self.url_settings)
        return self._urls

    def search(self, title, year=None):

        def exact_title(item):
            wanted = title.lower()
            return ((item.get('title') or '').lower() == wanted or
                    (item.get('original_title') or '').lower() == wanted)

        def named_as_asked(item):
            return _same_title(item.get('title'), title) or _same_title(item.get('original_title'), title)

        def released_in_year(item):
            return bool(year) and (item.get('release_date') or '').startswith(year)

        def is_best(item):
            return named_as_asked(item) and (not year or released_in_year(item))

        search_media_id = _parse_media_id(title)
        if search_media_id:
            if search_media_id['type'] == 'tmdb':
                result = _get_movie(search_media_id['id'], None, True)
                if 'error' in result:
                    return result
                result = [result]
            else:
                result = tmdbapi.find_movie_by_external_id(search_media_id['id'], language=self.search_language)
                if 'error' in result:
                    return result
                result = result.get('movie_results')
        else:
            response = tmdbapi.search_movie(query=title, year=year, language=self.search_language)
            if 'error' in response:
                return response
            result = response['results']
            # Page 2 too, unless page 1 has the title exactly as asked, of the year asked, with a
            # popularity above 5: a title that matches only without its punctuation may not be it
            if response['total_pages'] > 1:
                bests = [item for item in result if exact_title(item) and is_best(item) and
                         (item.get('popularity') or 0) > 5]
                if not bests:
                    response = tmdbapi.search_movie(query=title, year=year, language=self.search_language, page=2)
                    if 'error' in response:
                        api_utils.log_left_out("the search's page 2", response)
                    else:
                        result += response['results']
        urls = self.urls

        if result:
            # A result named as asked comes first, then one first released in the year asked, then
            # one whose title is exactly as asked rather than only without its punctuation ("A-B"
            # before "A B"). TMDb matches the year against any of a movie's release dates, and its
            # own order can put Part 1 (2010) before Part 2 (2011) for "Part 2" in 2011. Kodi takes
            # the first result. Among the best, the most popular first; otherwise TMDb's order is
            # kept.
            result = sorted(result, key=lambda item: (
                not named_as_asked(item), not released_in_year(item), not exact_title(item),
                -(item.get('popularity') or 0) if is_best(item) else 0))

        for item in result:
            if item.get('poster_path'):
                item['poster_path'] = urls['preview'] + item['poster_path']
            if item.get('backdrop_path'):
                item['backdrop_path'] = urls['preview'] + item['backdrop_path']
        return result

    def get_details(self, uniqueids):
        media_id = uniqueids.get('tmdb')
        if not media_id:
            imdb_id = uniqueids.get('imdb')
            if not imdb_id:
                return None

            find_results = tmdbapi.find_movie_by_external_id(imdb_id)
            if 'error' in find_results:
                return find_results
            if find_results.get('movie_results'):
                movie = find_results['movie_results'][0]
                media_id = movie['id']
            if not media_id:
                return None

        details = self._gather_details(media_id)
        if not details:
            return None
        if details.get('error'):
            return details
        return self._assemble_details(**details)

    def _image_languages(self):
        """The images to ask TMDb for: in the add-on's language, in English, and without text."""
        languages = []
        for lang in ((self.language or 'en').split('-')[0], 'en', 'xx', 'null'):
            if lang not in languages:
                languages.append(lang)
        return ','.join(languages)

    def _gather_details(self, media_id):
        image_languages = self._image_languages()
        # One request brings the text in the chosen language, and the images wanted
        movie = _get_movie(media_id, self.language, image_languages=image_languages)
        if not movie or movie.get('error'):
            return movie
        # A part that fails, after the request's own retry, is left out and logged: the movie is
        # added without it
        failed = _fill_from_all_images(movie, lambda: tmdbapi.get_movie_images(media_id),
                                       ('posters', 'backdrops', 'logos'))
        if failed:
            api_utils.log_left_out("the movie's images in other languages", failed)

        # English text for what the chosen language lacks. TMDb answers in en-US when a request has
        # no language, so for en-US another request would only repeat the first.
        movie_fallback = {}
        if self.language != ENGLISH and (not movie.get('overview') or not movie.get('tagline') or
                                         not (movie.get('trailers') or {}).get('youtube')):
            movie_fallback = tmdbapi.get_movie(media_id, language=ENGLISH, append_to_response='trailers')
            if api_utils.is_not_found(movie_fallback):
                # Gone since the first request: no English text, which isn't a failure
                movie_fallback = {}
            elif not movie_fallback or 'error' in movie_fallback:
                api_utils.log_left_out('the English text', movie_fallback)
                movie_fallback = {}

        collection = None
        collection_fallback = None
        if movie['belongs_to_collection']:
            collection_id = movie['belongs_to_collection'].get('id')
            # One request, in the chosen language, with the images wanted
            collection = _get_moviecollection(collection_id, self.language, image_languages)
            if api_utils.is_not_found(collection):
                # TMDb no longer has the set: no set, which isn't a failure
                collection = None
            elif not collection or 'error' in collection:
                api_utils.log_left_out('the set', collection)
                collection = None
            else:
                failed = _fill_from_all_images(
                    collection, lambda: tmdbapi.get_collection_images(collection_id),
                    ('posters', 'backdrops'))
                if failed:
                    api_utils.log_left_out("the set's images in other languages", failed)
                # English only for what the chosen language lacks
                if self.language != ENGLISH and (not collection.get('name') or
                                                 not collection.get('overview')):
                    collection_fallback = _get_moviecollection(
                        collection_id, ENGLISH, image_languages, with_images=False)
                    if api_utils.is_not_found(collection_fallback):
                        # Gone since the first request: no English text, which isn't a failure
                        collection_fallback = None
                    elif not collection_fallback or 'error' in collection_fallback:
                        api_utils.log_left_out("the set's English name and overview",
                                               collection_fallback)
                        collection_fallback = None

        return {'movie': movie, 'movie_fallback': movie_fallback, 'collection': collection,
            'collection_fallback': collection_fallback}

    def _assemble_details(self, movie, movie_fallback, collection, collection_fallback):
        collection_fallback = collection_fallback or {}
        info = {
            'title': movie['title'],
            'originaltitle': movie['original_title'],
            'plot': movie.get('overview') or movie_fallback.get('overview'),
            'tagline': movie.get('tagline') or movie_fallback.get('tagline'),
            'studio': _get_names(movie['production_companies']),
            'genre': _get_names(movie['genres']),
            'country': _get_names(movie['production_countries']),
            'credits': _get_cast_members(movie.get('credits', movie.get('casts', {})), 'crew', 'Writing', ['Screenplay', 'Writer', 'Author']),
            'director': _get_cast_members(movie.get('credits', movie.get('casts', {})), 'crew', 'Directing', ['Director']),
            'premiered': movie['release_date'],
            'tag': _get_names(movie.get('keywords', {}).get('keywords', []))
        }

        if 'countries' in movie.get('releases', {}):
            certcountry = self.certification_country.upper()
            for country in movie.get('releases', {}).get('countries', []):
                if country['iso_3166_1'] == certcountry and country['certification']:
                    info['mpaa'] = country['certification']
                    break

        trailer = _parse_trailer(movie.get('trailers', {}), movie_fallback.get('trailers', {}))
        if trailer:
            info['trailer'] = trailer
        if collection:
            info['set'] = collection.get('name') or collection_fallback.get('name')
            info['setoverview'] = collection.get('overview') or collection_fallback.get('overview')
        if movie.get('runtime'):
            info['duration'] = movie['runtime'] * 60

        ratings = {'themoviedb': {'rating': float(movie['vote_average']), 'votes': int(movie['vote_count'])}}
        uniqueids = _parse_uniqueids(movie)
        cast = [{
                'name': actor['name'],
                'role': actor['character'],
                'thumbnail': self.urls['original'] + actor['profile_path']
                    if actor['profile_path'] else "",
                'order': actor['order']
            }
            for actor in movie.get('credits', movie.get('casts', {})).get('cast', [])
        ]
        available_art = _parse_artwork(movie, collection, self.urls, self.language)
        original_language = _parse_original_language(movie)

        _info = {'set_tmdbid': movie['belongs_to_collection'].get('id')
            if movie['belongs_to_collection'] else None}

        return {'info': info, 'ratings': ratings, 'uniqueids': uniqueids, 'cast': cast,
            'available_art': available_art, '_info': _info, 'original_language': original_language}

def _parse_original_language(movie):
    first_spoken_language = next(iter(movie.get('spoken_languages', [])), {}).get('iso_639_1')
    return first_spoken_language or movie.get('original_language')

_PUNCTUATION = re.compile(r'[^\w\s]')

def _title_forms(text):
    """A title's forms to compare: lower case, with punctuation dropped, and as spaces.

    So "Harry Potter and the Deathly Hallows: Part 2" matches "... Hallows Part 2", "Spider-Man"
    matches "spider man", and "M*A*S*H" matches "mash".
    """
    text = text.lower()
    return {' '.join(_PUNCTUATION.sub('', text).split()),
            ' '.join(_PUNCTUATION.sub(' ', text).split())}

def _same_title(a, b):
    return bool(a) and bool(b) and not _title_forms(a).isdisjoint(_title_forms(b))

def _parse_media_id(title):
    if title.startswith('tt') and title[2:].isdigit():
        return {'type': 'imdb', 'id':title} # IMDB ID works alone because it is clear
    title = title.lower()
    if title.startswith('tmdb/') and title[5:].isdigit(): # TMDB ID
        return {'type': 'tmdb', 'id':title[5:]}
    elif title.startswith('imdb/tt') and title[7:].isdigit(): # IMDB ID with prefix to match
        return {'type': 'imdb', 'id':title[5:]}
    return None

def _parse_uniqueids(movie):
    uniqueids = {'tmdb': str(movie['id'])}
    if movie.get('imdb_id'):
        uniqueids['imdb'] = movie['imdb_id']
    return uniqueids

# TMDb's default language: it answers a request with no language as if it had asked for this
ENGLISH = 'en-US'

def _usable(images, kind):
    """The images of a kind the add-on can use: it skips SVGs."""
    return [img for img in images.get(kind, []) if not img['file_path'].endswith('.svg')]

def _fill_from_all_images(data, get_all_images, kinds):
    """Give the kinds of image with none usable in the languages asked those in every language.

    The art takes an image in any language when there is none in the add-on's language or English
    (_build_image_list_with_fallback()). The images asked for with include_image_language leave
    those out, so they are asked for again, only when needed: about one movie or set in twenty.

    Returns None, or an error dict if the request for every image failed.
    """
    images = data.get('images') or {}
    lacking = [kind for kind in kinds if not _usable(images, kind)]
    if not lacking:
        return None
    all_images = get_all_images()
    if api_utils.is_not_found(all_images):
        return None
    if not all_images or 'error' in all_images:
        return _failed('the images in every language', all_images)
    for kind in lacking:
        images[kind] = all_images.get(kind, [])
    data['images'] = images
    return None

def _failed(what, response):
    """The error dict for a part of the details that couldn't be had, after its request's retry"""
    # Without the part's HTTP status: only the movie's own 404 means TMDb has no such movie
    reason = (response or {}).get('error', 'no answer')
    return {'error': 'failed to get {}: {}'.format(what, reason)}

def _get_movie(mid, language=None, search=False, image_languages=None):
    details = None if search else \
        'trailers,images,releases,credits,keywords' if language is not None else \
        'trailers,images'
    return tmdbapi.get_movie(mid, language=language, append_to_response=details,
                             image_languages=None if search else image_languages)

def _get_moviecollection(collection_id, language=None, image_languages=None, with_images=True):
    if not collection_id:
        return None
    return tmdbapi.get_collection(collection_id, language=language,
                                  append_to_response='images' if with_images else None,
                                  image_languages=image_languages if with_images else None)

def _parse_artwork(movie, collection, urlbases, language):
    if language:
        # Image languages don't have regional variants
        language = language.split('-')[0]
    posters = []
    landscape = []
    logos = []
    fanart = []
    keyart = []

    if 'images' in movie:
        posters = _build_image_list_with_fallback(movie['images'].get('posters', []), urlbases, language)
        landscape = _build_image_list_with_fallback(movie['images'].get('backdrops', []), urlbases, language)
        logos = _build_image_list_with_fallback(movie['images'].get('logos', []), urlbases, language)
        fanart = _build_list_without_titles(movie['images'].get('backdrops', []), urlbases)
        keyart = _build_list_without_titles(movie['images'].get('posters', []), urlbases)

    setposters = []
    setlandscape = []
    setfanart = []
    setkeyart = []
    if collection and 'images' in collection:
        setposters = _build_image_list_with_fallback(collection['images'].get('posters', []), urlbases, language)
        setlandscape = _build_image_list_with_fallback(collection['images'].get('backdrops', []), urlbases, language)
        setfanart = _build_list_without_titles(collection['images'].get('backdrops', []), urlbases)
        setkeyart = _build_list_without_titles(collection['images'].get('posters', []), urlbases)

    return {'poster': posters, 'landscape': landscape, 'fanart': fanart,
        'set.poster': setposters, 'set.landscape': setlandscape, 'set.fanart': setfanart,
        'clearlogo': logos, 'keyart': keyart, 'set.keyart': setkeyart}

def _build_image_list_with_fallback(imagelist, urlbases, language, language_fallback='en'):
    images = _build_image_list(imagelist, urlbases, [language])

    # Add backup images
    if language != language_fallback:
        images.extend(_build_image_list(imagelist, urlbases, [language_fallback]))

    # Add any images if nothing set so far
    if not images:
        images = _build_image_list(imagelist, urlbases)

    return images

def _build_list_without_titles(imagelist, urlbases):
    return _build_image_list(imagelist, urlbases, ['xx', None])

def _build_image_list(imagelist, urlbases, languages=[]):
    result = []
    for img in imagelist:
        if languages and img['iso_639_1'] not in languages:
            continue
        if img['file_path'].endswith('.svg'):
            continue
        result.append({
            'url': urlbases['original'] + img['file_path'],
            'preview': urlbases['preview'] + img['file_path'],
            'lang': img['iso_639_1']
        })
    return result

def _get_date_numeric(datetime_):
    return (datetime_ - datetime(1970, 1, 1)).total_seconds()

# TMDb's documented image base, used when its configuration can't be read
TMDB_IMAGE_BASE = 'https://image.tmdb.org/t/p/'

def _load_base_urls(url_settings):
    urls = {}
    urls['original'] = url_settings.getSettingString('originalUrl')
    urls['preview'] = url_settings.getSettingString('previewUrl')
    last_updated = url_settings.getSettingString('lastUpdated')
    try:
        stale = float(last_updated) < _get_date_numeric(datetime.now() - timedelta(days=30))
    except ValueError:
        stale = True
    if urls['original'] and urls['preview'] and not stale:
        return urls
    conf = tmdbapi.get_configuration()
    base = None
    if conf and 'error' not in conf:
        base = (conf.get('images') or {}).get('secure_base_url')
    if not base:
        # Rather than fail the call: the URLs stored, or TMDb's documented base. Nothing is
        # saved, so a later call asks TMDb again.
        if urls['original'] and urls['preview']:
            return urls
        return {'original': TMDB_IMAGE_BASE + 'original', 'preview': TMDB_IMAGE_BASE + 'w780'}
    fetched = {'original': base + 'original', 'preview': base + 'w780'}
    # Each setSetting() saves the add-on's settings, which interpreters running at once share:
    # save the URLs only when they have changed
    if fetched != urls:
        url_settings.setSetting('originalUrl', fetched['original'])
        url_settings.setSetting('previewUrl', fetched['preview'])
    url_settings.setSetting('lastUpdated', str(_get_date_numeric(datetime.now())))
    return fetched

def _parse_trailer(trailers, fallback):
    if trailers.get('youtube'):
        return 'plugin://plugin.video.youtube/play/?video_id='+trailers['youtube'][0]['source']
    if fallback.get('youtube'):
        return 'plugin://plugin.video.youtube/play/?video_id='+fallback['youtube'][0]['source']
    return None

def _get_names(items):
    return [item['name'] for item in items] if items else []

def _get_cast_members(casts, casttype, department, jobs):
    result = []
    if casttype in casts:
        for cast in casts[casttype]:
            if cast['department'] == department and cast['job'] in jobs and cast['name'] not in result:
                result.append(cast['name'])
    return result
