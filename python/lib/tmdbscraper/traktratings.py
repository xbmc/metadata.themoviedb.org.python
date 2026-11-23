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

"""Functions to interact with Trakt API."""

from __future__ import absolute_import, unicode_literals

from . import api_utils
from . import get_imdb_id
try:
    from typing import Optional, Text, Dict, List, Any  # pylint: disable=unused-import
    InfoType = Dict[Text, Any]  # pylint: disable=invalid-name
except ImportError:
    pass


HEADERS = (
    ('User-Agent', 'Kodi Movie scraper by Team Kodi'),
    ('Accept', 'application/json'),
    ('trakt-api-key', '5f2dc73b6b11c2ac212f5d8b4ec8f3dc4b727bb3f026cd254d89eda997fe64ae'),
    ('trakt-api-version', '2'),
    ('Content-Type', 'application/json'),
)

MOVIE_URL = 'https://api.trakt.tv/movies/{}'


def get_trakt_ratinginfo(uniqueids):
    imdb_id = get_imdb_id(uniqueids)
    result = {}
    if not imdb_id:
        # Trakt is asked by IMDb id: without one, don't ask for /movies/None
        return result
    url = MOVIE_URL.format(imdb_id)
    params = {'extended': 'full'}
    api_utils.set_headers(dict(HEADERS))
    movie_info = api_utils.SESSION.load_info(url, params=params)
    # A film Trakt doesn't know (404) has no Trakt rating, which isn't a failure; a request that
    # fails, after its retry, gives the caller its error
    if api_utils.is_not_found(movie_info):
        return result
    if 'error' in movie_info:
        return movie_info
    if(movie_info):
        if 'votes' in movie_info and 'rating' in movie_info:
            result['ratings'] = {'trakt': {'votes': int(movie_info['votes']), 'rating': float(movie_info['rating'])}}
        elif 'rating' in movie_info:
            result['ratings'] = {'trakt': {'rating': float(movie_info['rating'])}}
    return result
