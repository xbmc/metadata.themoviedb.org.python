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
import io
import json
import re
import select
import ssl
import threading
import time
from collections import OrderedDict
from email.utils import parsedate_to_datetime

try:
    import xbmc
except ModuleNotFoundError:
    # only used for logging HTTP calls, not available nor needed for testing
    xbmc = None

# from pprint import pformat
from urllib.request import Request, getproxies, proxy_bypass, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode, urlsplit
try:
    from typing import Text, Optional, Union, List, Dict, Any  # pylint: disable=unused-import
    InfoType = Dict[Text, Any]  # pylint: disable=invalid-name
except ImportError:
    pass

HEADERS = {}
_KEY_IN_URL = re.compile(r'(api_?key=)[^&]+', re.IGNORECASE)
# How a kept connection the server has closed meanwhile shows when it is used
_CLOSED = (http.client.RemoteDisconnected, http.client.BadStatusLine,
           http.client.CannotSendRequest, ConnectionResetError, ConnectionAbortedError,
           BrokenPipeError, ssl.SSLEOFError, ssl.SSLZeroReturnError)


def set_headers(headers):
    HEADERS.clear()
    HEADERS.update(headers)


class Session(object):
    """The add-on's requests: each tried once more after a failure that may pass, answers kept a
    while for the later calls (kept()), and one connection kept open to each site.

    Kodi runs the add-on's calls in an interpreter it keeps for them (reuselanguageinvoker), so one
    instance, SESSION, serves them all.
    """

    def __init__(self, timeout=15, retry_pause=1.0, max_retry_after=30, keep_seconds=15 * 60,
                 keep_most=64):
        self.timeout = timeout  # seconds, for connecting and for each read
        self.retry_pause = retry_pause  # seconds before the one retry
        self.max_retry_after = max_retry_after  # the longest Retry-After honoured, in seconds
        self.keep_seconds = keep_seconds  # how long an answer is kept
        self.keep_most = keep_most  # how many answers are kept
        self._kept = OrderedDict()
        self._kept_lock = threading.Lock()
        self._connections = {}  # (scheme, host, port) -> connection
        self._connections_lock = threading.Lock()
        self._ssl_context = None
        self._proxies = None

    def load_info(self, url, params=None, default=None, resp_type='json'):
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
        resp, error = self.fetch(req, json.loads if resp_type.lower() == 'json' else None)
        if error is None:
            return resp
        return default if default is not None else error

    def fetch(self, req, parse=None, timeout=None):
        """Make a request, and try once more after a failure that may pass.

        :param req: the urllib Request
        :param parse: optional callable applied to the body, such as json.loads
        :param timeout: seconds allowed for connecting and for each read (default self.timeout)
        :return: (result, None), or (None, error dict) if the request failed. The error dict has
            'error', and 'code' when the server answered with an HTTP error status.
        """
        timeout = timeout or self.timeout
        for attempt in (1, 2):
            delay = self.retry_pause
            try:
                body = self._send(req, timeout).decode('utf-8')
                return (parse(body) if parse else body), None
            except HTTPError as e:  # before URLError, of which it is a kind
                error = {'error': 'remote site unable to fulfill the request\nError code: {}'.format(
                    e.code), 'code': e.code}
                retry = e.code == 429 or 500 <= e.code <= 599
                if e.code == 429:
                    delay = self._retry_after(e.headers)
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

    def kept(self, key, fetch):
        """fetch()'s answer, or the one it gave for the same key in the last keep_seconds: for the
        later calls of the interpreter, such as each movie of a set asking for the set. An error
        isn't kept, but a 404 is: there is nothing there."""
        now = time.monotonic()
        with self._kept_lock:
            entry = self._kept.get(key)
            if entry and now - entry[0] < self.keep_seconds:
                self._kept.move_to_end(key)
                return copy.deepcopy(entry[1])
        answer = fetch()
        if not (isinstance(answer, dict) and 'error' in answer) or is_not_found(answer):
            with self._kept_lock:
                self._kept[key] = (now, copy.deepcopy(answer))
                self._kept.move_to_end(key)
                while len(self._kept) > self.keep_most:
                    self._kept.popitem(last=False)
        return answer

    def forget(self):
        """Forgets every answer kept"""
        with self._kept_lock:
            self._kept.clear()

    def close(self):
        """Closes every connection kept open"""
        with self._connections_lock:
            kept_now = list(self._connections.values())
            self._connections.clear()
        for conn in kept_now:
            conn.close()

    def _send(self, req, timeout):
        """The body of a request's answer, on a connection kept open to its site. An error status
        raises HTTPError, as urlopen() does."""
        parts = urlsplit(req.full_url)
        scheme, host = parts.scheme.lower(), parts.hostname
        if scheme not in ('http', 'https') or not host or self._proxied(scheme, host):
            with urlopen(req, timeout=timeout) as response:
                return response.read()
        key = (scheme, host, parts.port)
        target = (parts.path or '/') + ('?' + parts.query if parts.query else '')
        headers = dict(req.header_items())
        body = req.data
        if body is not None and not any(name.lower() == 'content-type' for name in headers):
            headers['Content-Type'] = 'application/x-www-form-urlencoded'  # as urlopen() sends
        for fresh in (False, True):
            conn = None if fresh else self._kept_connection(key, timeout)
            reused = conn is not None
            if conn is None:
                conn = self._new_connection(scheme, host, parts.port, timeout)
            try:
                conn.request(req.get_method(), target, body=body, headers=headers)
                response = conn.getresponse()
            except _CLOSED:
                conn.close()
                if reused:
                    # The server closed it while it was kept: sent again on a new connection,
                    # which isn't the request's one retry
                    continue
                raise
            except BaseException:
                conn.close()
                raise
            if response.status >= 400:
                # The status comes with the headers, whatever the body does after them. Only a
                # connection with no body to drain is kept.
                if response.length == 0 and not response.will_close:
                    response.close()
                    self._keep(key, conn)
                else:
                    response.close()
                    conn.close()
                raise HTTPError(req.full_url, response.status, response.reason, response.headers,
                                io.BytesIO(b''))
            try:
                raw = response.read()
            except BaseException:
                conn.close()
                raise
            if response.will_close:
                conn.close()
            else:
                self._keep(key, conn)
            if 300 <= response.status < 400 and response.status != 304:
                # A redirect, which urlopen() follows
                with urlopen(req, timeout=timeout) as redirected:
                    return redirected.read()
            return raw

    def _kept_connection(self, key, timeout):
        """The connection kept open to a site, unless the server has closed it meanwhile"""
        with self._connections_lock:
            conn = self._connections.pop(key, None)
        if conn is None:
            return None
        # Readable while no answer is awaited: the server has closed it
        try:
            closed = conn.sock is None or bool(select.select([conn.sock], [], [], 0)[0])
        except (OSError, ValueError):
            closed = True
        if closed:
            conn.close()
            return None
        conn.timeout = timeout
        conn.sock.settimeout(timeout)
        return conn

    def _keep(self, key, conn):
        with self._connections_lock:
            other = self._connections.pop(key, None)
            self._connections[key] = conn
        if other is not None:
            other.close()

    def _new_connection(self, scheme, host, port, timeout):
        if scheme == 'https':
            if self._ssl_context is None:
                self._ssl_context = ssl.create_default_context()
            conn = http.client.HTTPSConnection(host, port, timeout=timeout, context=self._ssl_context)
        else:
            conn = http.client.HTTPConnection(host, port, timeout=timeout)
        try:
            conn.connect()
        except BaseException:
            conn.close()
            raise
        return conn

    def _proxied(self, scheme, host):
        """True when the system has a proxy for the site, which urlopen() goes through"""
        if self._proxies is None:
            self._proxies = getproxies()
        return scheme in self._proxies and not proxy_bypass(host)

    def _retry_after(self, headers):
        """Seconds a 429 answer asks to wait, within limits. Retry-After is a number of seconds or
        an HTTP date (RFC 9110, 10.2.3)."""
        value = headers.get('Retry-After') if headers else None
        try:
            seconds = float(value)
        except (TypeError, ValueError):
            try:
                seconds = parsedate_to_datetime(value).timestamp() - time.time()
            except (TypeError, ValueError, OverflowError, OSError):
                return self.retry_pause
        return min(self.max_retry_after, max(self.retry_pause, seconds))


# The one session, for all the add-on's calls in an interpreter
SESSION = Session()


def is_not_found(response):
    """True for the error of a request the server answered 404: there is nothing there, which isn't
    a failure, as a lost connection or a 5xx is"""
    return isinstance(response, dict) and response.get('code') == 404


def log_left_out(what, response):
    """Log a part of a movie's details left out because its request failed, after the retry: the
    movie is added without it, rather than without a word"""
    if xbmc:
        reason = (response or {}).get('error') or 'no answer'
        xbmc.log('[metadata.themoviedb.org.python] {} left out: {}'.format(
            what, reason.replace('\n', ' ')), xbmc.LOGWARNING)


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
