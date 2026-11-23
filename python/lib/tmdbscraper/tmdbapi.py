# -*- coding: UTF-8 -*-
#
# Copyright (C) 2020, Team Kodi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# pylint: disable=missing-docstring

"""Functions to interact with TMDb API."""

import unicodedata
from . import api_utils
try:
    import xbmc
except ModuleNotFoundError:
    # only used for logging HTTP calls, not available nor needed for testing
    xbmc = None
try:
    from typing import Optional, Text, Dict, List, Any  # pylint: disable=unused-import
    InfoType = Dict[Text, Any]  # pylint: disable=invalid-name
except ImportError:
    pass


HEADERS = (
    ('User-Agent', 'Kodi Movie scraper by Team Kodi'),
    ('Accept', 'application/json'),
)

TMDB_PARAMS = {'api_key': 'f090bb54758cabf231fb605d3e3e0468'}
BASE_URL = 'https://api.themoviedb.org/3/{}'
SEARCH_URL = BASE_URL.format('search/movie')
FIND_URL = BASE_URL.format('find/{}')
MOVIE_URL = BASE_URL.format('movie/{}')
COLLECTION_URL = BASE_URL.format('collection/{}')
CONFIG_URL = BASE_URL.format('configuration')

def log(message):
    if xbmc:
        xbmc.log(message, xbmc.LOGDEBUG)

def search_movie(query, year=None, language=None, page=None):
    # type: (Text) -> List[InfoType]
    """
    Search for a movie

    :param title: movie title to search
    :param year: the year to search (optional)
    :param language: the language filter for TMDb (optional)
    :param page: the results page to return (optional)
    :return: a list with found movies
    """
    query = unicodedata.normalize('NFC', query)
    log('using title of %s to find movie' % query)
    theurl = SEARCH_URL
    params = _set_params(None, language)
    params['query'] = query
    if page is not None:
        params['page'] = page
    if year is not None:
        params['year'] = str(year)
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(theurl, params=params)


def find_movie_by_external_id(external_id, language=None):
    # type: (Text) -> List[InfoType]
    """
    Find movie based on external ID

    :param mid: external ID
    :param language: the language filter for TMDb (optional)
    :return: the movie or error
    """
    log('using external id of %s to find movie' % external_id)
    theurl = FIND_URL.format(external_id)
    params = _set_params(None, language)
    params['external_source'] = 'imdb_id'
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(theurl, params=params)



def get_movie(mid, language=None, append_to_response=None, image_languages=None):
    # type: (Text) -> List[InfoType]
    """
    Get movie details

    :param mid: TMDb movie ID
    :param language: the language filter for TMDb (optional)
    :append_to_response: the additional data to get from TMDb (optional)
    :image_languages: the languages of the images to get, such as 'en,null' (optional)
    :return: the movie or error
    """
    log('using movie id of %s to get movie details' % mid)
    theurl = MOVIE_URL.format(mid)
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(theurl, params=_set_params(append_to_response, language, image_languages))


def get_collection(collection_id, language=None, append_to_response=None, image_languages=None):
    # type: (Text) -> List[InfoType]
    """
    Get movie collection information

    :param collection_id: TMDb collection ID
    :param language: the language filter for TMDb (optional)
    :append_to_response: the additional data to get from TMDb (optional)
    :image_languages: the languages of the images to get, such as 'en,null' (optional)
    :return: the movie or error
    """
    log('using collection id of %s to get collection details' % collection_id)
    theurl = COLLECTION_URL.format(collection_id)
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(theurl, params=_set_params(append_to_response, language, image_languages))


def get_movie_images(mid):
    # type: (Text) -> InfoType
    """
    Get all of a movie's images, in every language

    :param mid: TMDb movie ID
    :return: the images or error
    """
    log('using movie id of %s to get all its images' % mid)
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(MOVIE_URL.format(mid) + '/images', params=TMDB_PARAMS.copy())


def get_collection_images(collection_id):
    # type: (Text) -> InfoType
    """
    Get all of a movie collection's images, in every language

    :param collection_id: TMDb collection ID
    :return: the images or error
    """
    log('using collection id of %s to get all its images' % collection_id)
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(COLLECTION_URL.format(collection_id) + '/images', params=TMDB_PARAMS.copy())


def get_configuration():
    # type: (Text) -> List[InfoType]
    """
    Get configuration information

    :return: configuration details or error
    """
    log('getting configuration details')
    api_utils.set_headers(dict(HEADERS))
    return api_utils.SESSION.load_info(CONFIG_URL, params=TMDB_PARAMS.copy())


def _set_params(append_to_response, language, image_languages=None):
    params = TMDB_PARAMS.copy()
    if language is not None:
        params['language'] = language
    if append_to_response is not None:
        params['append_to_response'] = append_to_response
    if image_languages is not None:
        # Without it TMDb filters the images to the request's language, or to en-US when it has
        # none, so those without text (fanart, keyart) are left out
        params['include_image_language'] = image_languages
    return params
