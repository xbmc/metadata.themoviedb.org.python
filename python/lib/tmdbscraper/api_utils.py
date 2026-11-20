# coding: utf-8
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

"""Functions to interact with various web site APIs."""

from __future__ import absolute_import, unicode_literals

import copy
import http.client
import json
import re
import threading
import time
from collections import OrderedDict

try:
    import xbmc
except ModuleNotFoundError:
    # only used for logging HTTP calls, not available nor needed for testing
    xbmc = None

# from pprint import pformat
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
try:
    from typing import Text, Optional, Union, List, Dict, Any  # pylint: disable=unused-import
    InfoType = Dict[Text, Any]  # pylint: disable=invalid-name
except ImportError:
    pass

HEADERS = {}
TIMEOUT = 15  # seconds, for connecting and for each read
RETRY_PAUSE = 1.0  # seconds before the one retry
MAX_RETRY_AFTER = 30  # the longest Retry-After honoured, in seconds
_KEY_IN_URL = re.compile(r'(api_?key=)[^&]+', re.IGNORECASE)


def set_headers(headers):
    HEADERS.clear()
    HEADERS.update(headers)


def load_info(url, params=None, default=None, resp_type = 'json'):
    # type: (Text, Optional[Dict[Text, Union[Text, List[Text]]]]) -> Union[dict, list]
    """
    Load info from external api

    :param url: API endpoint URL
    :param params: URL query params
    :default: object to return if there is an error
    :resp_type: what to return to the calling function
    :return: API response or default on error
    """
    if params:
        url = url + '?' + urlencode(params)
    if xbmc:
        xbmc.log('Calling URL "{}"'.format(_KEY_IN_URL.sub(r'\1...', url)), xbmc.LOGDEBUG)
        if HEADERS:
            # Without the keys: api-key, client-key (the user's own) and trakt-api-key
            xbmc.log(str({name: '...' if 'key' in name.lower() else value
                          for name, value in HEADERS.items()}), xbmc.LOGDEBUG)
    req = Request(url, headers=HEADERS)
    resp, error = fetch(req, json.loads if resp_type.lower() == 'json' else None)
    if error is None:
        return resp
    return default if default is not None else error


def fetch(req, parse=None, timeout=None):
    """Make a request, and try once more after a failure that may pass.

    :param req: the urllib Request
    :param parse: optional callable applied to the body, such as json.loads
    :param timeout: seconds allowed for connecting and for each read (default TIMEOUT)
    :return: (result, None), or (None, error dict) if the request failed. The error dict has
        'error', and 'code' when the server answered with an HTTP error status.
    """
    timeout = timeout or TIMEOUT
    for attempt in (1, 2):
        delay = RETRY_PAUSE
        try:
            with urlopen(req, timeout=timeout) as response:
                body = response.read().decode('utf-8')
            return (parse(body) if parse else body), None
        except HTTPError as e:  # before URLError, of which it is a kind
            error = {'error': 'remote site unable to fulfill the request\nError code: {}'.format(
                e.code), 'code': e.code}
            retry = e.code == 429 or 500 <= e.code <= 599
            if e.code == 429:
                delay = _retry_after(e.headers)
            e.close()
        except (OSError, http.client.HTTPException) as e:
            # URLError (no connection), resets, timeouts, and a body cut short
            error = {'error': 'failed to reach the remote site\nReason: {}'.format(
                getattr(e, 'reason', None) or e)}
            retry = True
        except ValueError as e:
            # a body that isn't JSON, such as a proxy's error page
            error = {'error': 'the remote site sent a reply that could not be read\nReason: {}'.format(e)}
            retry = True
        _log_failure(req.full_url, error['error'], attempt, retry)
        if attempt == 1 and retry and not _stop_requested_during(delay):
            continue
        return None, error


def is_not_found(response):
    """True for the error of a request the server answered 404: there is nothing there, which isn't
    a failure, as a lost connection or a 5xx is"""
    return isinstance(response, dict) and response.get('code') == 404


# Answers kept for the later calls of an interpreter, which Kodi runs the add-on in again: a set's,
# which each of its movies asks for
KEPT_SECONDS = 15 * 60
KEPT_MOST = 64
_kept = OrderedDict()
_kept_lock = threading.Lock()


def kept(key, fetch):
    """fetch()'s answer, or the one it gave for the same key in the last KEPT_SECONDS. An error
    isn't kept, but a 404 is: there is nothing there."""
    now = time.monotonic()
    with _kept_lock:
        entry = _kept.get(key)
        if entry and now - entry[0] < KEPT_SECONDS:
            _kept.move_to_end(key)
            return copy.deepcopy(entry[1])
    answer = fetch()
    if not (isinstance(answer, dict) and 'error' in answer) or is_not_found(answer):
        with _kept_lock:
            _kept[key] = (now, copy.deepcopy(answer))
            _kept.move_to_end(key)
            while len(_kept) > KEPT_MOST:
                _kept.popitem(last=False)
    return answer


def forget_kept():
    """Forgets every answer kept"""
    with _kept_lock:
        _kept.clear()


def _retry_after(headers):
    """Seconds a 429 answer asks to wait, within limits."""
    try:
        return min(MAX_RETRY_AFTER, max(RETRY_PAUSE, float(headers.get('Retry-After'))))
    except (AttributeError, TypeError, ValueError):
        return RETRY_PAUSE


def _stop_requested_during(seconds):
    """Wait, returning True early if Kodi asks the add-on to stop."""
    if xbmc:
        return xbmc.Monitor().waitForAbort(seconds)
    time.sleep(seconds)
    return False


def _log_failure(url, reason, attempt, retry):
    if xbmc:
        xbmc.log('[metadata.themoviedb.org.python] request failed{}: {} ({})'.format(
            ', trying again' if attempt == 1 and retry else '',
            _KEY_IN_URL.sub(r'\1...', url), reason.replace('\n', ' ')), xbmc.LOGWARNING)
