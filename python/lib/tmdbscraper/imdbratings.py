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
#
# IMDb ratings from script.module.imdbratings
# pylint: disable=missing-docstring

import time

import imdbratings

from . import get_imdb_id

try:
    import xbmc
except ModuleNotFoundError:
    xbmc = None

# Seconds to wait, once in an interpreter, for another interpreter's first load of the ratings
FIRST_LOAD_WAIT = 60
_waited = False


def get_details(uniqueids):
    """The IMDb rating of a film.

    Returns {'ratings': ...}; an empty dict when the film has no IMDb id or IMDb has no rating for
    it, which isn't a failure; or an error dict when no ratings are loaded (a first load not done,
    or the store unreadable), which fails the details call.
    """
    imdb_id = get_imdb_id(uniqueids)
    if not imdb_id:
        return {}

    rating = imdbratings.get_rating(imdb_id)
    # get_rating() gives None both for a film without a rating and when no ratings are loaded;
    # dataset_date() is None only for the second
    if not rating and imdbratings.dataset_date() is None:
        _wait_for_first_load()
        rating = imdbratings.get_rating(imdb_id)
        if not rating and imdbratings.dataset_date() is None:
            return {'error': 'the IMDb ratings are not loaded'}
    if not rating:
        return {}

    return {"ratings": {"imdb": {"rating": rating[0], "votes": rating[1]}}}


def _wait_for_first_load():
    """On a first run another interpreter may be loading the ratings: wait for them, once in this
    interpreter and within limits, so that its calls don't all fail meanwhile"""
    global _waited
    if _waited:
        return
    _waited = True
    monitor = xbmc.Monitor() if xbmc else None
    for _ in range(FIRST_LOAD_WAIT):
        if imdbratings.dataset_date() is not None:
            return
        if monitor:
            if monitor.waitForAbort(1):
                return
        else:
            time.sleep(1)
