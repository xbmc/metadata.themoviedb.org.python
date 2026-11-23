"""Stand-ins for Kodi's python modules and script.module.imdbratings, to import and run
python/scraper.py in a test, with the network faked at api_utils.SESSION.fetch()."""
import importlib
import json
import os
import re
import sys
import time
import types
import unittest.mock as mock

ADDON = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
PYTHON = os.path.join(ADDON, 'python')
NOT_FOUND = {'error': 'remote site unable to fulfill the request\nError code: 404', 'code': 404}
UNREACHABLE = {'error': 'failed to reach the remote site\nReason: timed out'}


def settings_defaults():
    """id -> default of each setting in the add-on's resources/settings.xml"""
    with open(os.path.join(ADDON, 'resources', 'settings.xml'), encoding='utf-8') as f:
        text = f.read()
    defaults = {}
    for m in re.finditer(r'<setting id="([^"]+)"[^>]*?(?:/>|>(.*?)</setting>)', text, re.S):
        default = re.search(r'<default>(.*?)</default>', m.group(2) or '', re.S)
        if default:
            value = default.group(1)
            defaults[m.group(1)] = value == 'true' if value in ('true', 'false') else value
    return defaults


class Settings(dict):
    def getSettingString(self, key):
        return str(self.get(key, ''))

    def getSettingBool(self, key):
        value = self.get(key, False)
        return value if isinstance(value, bool) else str(value).lower() == 'true'

    def getSettingInt(self, key):
        try:
            return int(self.get(key, 0))
        except ValueError:
            return 0

    def getSetting(self, key):
        return str(self.get(key, ''))

    def setSetting(self, key, value):
        self[key] = value


class InfoTag:
    def __init__(self):
        self.values = {}

    def __getattr__(self, name):
        if name.startswith(('set', 'add')):
            return lambda *a, **k: self.values.__setitem__(name, a[0] if len(a) == 1 else a)
        raise AttributeError(name)


class ListItem:
    def __init__(self, label='', offscreen=False):
        self.label = label
        self.tag = InfoTag()
        self.art = {}

    def getVideoInfoTag(self):
        return self.tag

    def setArt(self, art):
        self.art.update(art)

    def __getattr__(self, name):
        if name.startswith('set'):
            return lambda *a, **k: None
        raise AttributeError(name)


class Kodi:
    """Kodi's modules, stood in for, and what the add-on did with them"""

    def __init__(self, settings=None):
        self.notifications, self.resolved, self.ended, self.items, self.logs = [], [], [], [], []
        self.settings = Settings(settings_defaults())
        # Image URLs fresh in the add-on's settings, so that a call doesn't ask for TMDb's
        # configuration
        self.settings.update(originalUrl='https://image.tmdb.org/t/p/original',
                             previewUrl='https://image.tmdb.org/t/p/w780',
                             lastUpdated=str(time.time()))
        self.settings.update(settings or {})
        self.rating = (8.8, 2000000)  # script.module.imdbratings' answer, and its dataset's date
        self.dataset = '2026-11-16'

    def warnings(self):
        return [msg for level, msg in self.logs if level >= 2]

    def modules(self):
        kodi = self
        xbmc = types.ModuleType('xbmc')
        xbmc.LOGDEBUG, xbmc.LOGINFO, xbmc.LOGWARNING, xbmc.LOGERROR = 0, 1, 2, 3
        xbmc.log = lambda msg, level=0: kodi.logs.append((level, msg))
        xbmc.Actor = lambda *a, **k: a
        xbmc.InfoTagVideo = InfoTag
        xbmc.Monitor = lambda: types.SimpleNamespace(waitForAbort=lambda seconds=0: False,
                                                     abortRequested=lambda: False)
        xbmcgui = types.ModuleType('xbmcgui')
        xbmcgui.ListItem = ListItem
        xbmcgui.NOTIFICATION_WARNING = 'warning'
        xbmcgui.Dialog = lambda: types.SimpleNamespace(
            notification=lambda heading, message, *a, **k: kodi.notifications.append(message))
        xbmcplugin = types.ModuleType('xbmcplugin')
        xbmcplugin.setResolvedUrl = lambda handle, succeeded, listitem: kodi.resolved.append(
            (succeeded, listitem))
        xbmcplugin.endOfDirectory = lambda handle, succeeded=True, *a, **k: kodi.ended.append(
            succeeded)
        xbmcplugin.addDirectoryItem = lambda handle, url, listitem, isFolder=False: \
            kodi.items.append(url)
        xbmcaddon = types.ModuleType('xbmcaddon')
        settings = self.settings

        class Addon(Settings):
            def __init__(self, *a):
                Settings.__init__(self)
                self.update(settings)

            def getAddonInfo(self, key):
                return {'id': 'metadata.themoviedb.org.python'}.get(key, '')

        xbmcaddon.Addon = Addon
        xbmcvfs = types.ModuleType('xbmcvfs')
        xbmcvfs.translatePath = lambda path: path
        imdbratings = types.ModuleType('imdbratings')
        imdbratings.get_rating = lambda imdb_id: kodi.rating if kodi.dataset else None
        imdbratings.dataset_date = lambda: kodi.dataset
        return {'xbmc': xbmc, 'xbmcgui': xbmcgui, 'xbmcplugin': xbmcplugin,
                'xbmcaddon': xbmcaddon, 'xbmcvfs': xbmcvfs, 'imdbratings': imdbratings}


class Network:
    """Answers Session.fetch() from a dict: the url's host and path, or that and a part of its
    query joined by '|', to a JSON-able answer, a status code (int), or None for a failure to
    reach the site. Records the urls asked for."""

    def __init__(self, answers=None):
        self.answers = dict(answers or {})
        self.asked = []

    def fetch(self, req, parse=None, timeout=None):
        url = req.full_url
        self.asked.append(url)
        where = url.split('://', 1)[-1].split('?', 1)[0]
        query = url.split('?', 1)[1] if '?' in url else ''
        keys = [key for key in self.answers
                if key.split('|')[0] == where and all(part in query for part in key.split('|')[1:])]
        if not keys:
            return None, dict(UNREACHABLE)
        answer = self.answers[max(keys, key=len)]
        if answer is None:
            return None, dict(UNREACHABLE)
        if isinstance(answer, int):
            return None, {'error': 'remote site unable to fulfill the request\nError code: {}'.format(
                answer), 'code': answer}
        body = json.dumps(answer)
        return (parse(body) if parse else body), None


def image(language, path):
    return {'iso_639_1': language, 'file_path': path}


def movie(mid=550, collection=10):
    """A movie as TMDb answers the add-on's request for it"""
    return {'id': mid, 'title': 'A Film', 'original_title': 'A Film', 'overview': 'A plot.',
            'tagline': 'A tagline.', 'production_companies': [], 'production_countries': [],
            'genres': [{'name': 'Drama'}], 'release_date': '1999-10-15', 'runtime': 139,
            'vote_average': 8.4, 'vote_count': 30000, 'imdb_id': 'tt0137523',
            'spoken_languages': [{'iso_639_1': 'en'}], 'original_language': 'en',
            'belongs_to_collection': {'id': collection} if collection else None,
            'credits': {'cast': [], 'crew': []}, 'keywords': {'keywords': []},
            'releases': {'countries': []}, 'trailers': {'youtube': [{'source': 'abc'}]},
            'images': {'posters': [image('en', '/p.jpg'), image(None, '/k.jpg')],
                       'backdrops': [image('en', '/b.jpg'), image(None, '/f.jpg')],
                       'logos': [image('en', '/l.png')]}}


def answers():
    """A movie (550) in a set (10), with fanart.tv's art and a Trakt rating"""
    return {
        'api.themoviedb.org/3/movie/550': movie(),
        'api.themoviedb.org/3/collection/10': {
            'id': 10, 'name': 'A Set', 'overview': 'A set.',
            'images': {'posters': [image('en', '/sp.jpg')], 'backdrops': [image(None, '/sf.jpg')]}},
        'api.themoviedb.org/3/search/movie': {
            'total_pages': 1, 'results': [{'id': 550, 'title': 'A Film', 'original_title': 'A Film',
                                           'release_date': '1999-10-15', 'popularity': 10,
                                           'poster_path': None, 'backdrop_path': None}]},
        'webservice.fanart.tv/v3/movies/550': {'name': 'A Film', 'movieposter': [
            {'url': 'https://ftv/p.jpg', 'lang': 'en', 'likes': '1', 'id': '1'}]},
        'webservice.fanart.tv/v3/movies/10': {'name': 'A Set'},
        'api.trakt.tv/movies/tt0137523': {'rating': 8.5, 'votes': 100},
    }


def load_scraper(test, settings=None, network=None):
    """python/scraper.py, imported afresh for the test with Kodi's modules stood in for and the
    network faked. Returns (scraper module, Kodi, Network)."""
    kodi = Kodi(settings)
    network = network or Network(answers())
    modules = mock.patch.dict(sys.modules, kodi.modules())
    modules.start()
    test.addCleanup(modules.stop)
    for name in [n for n in sys.modules
                 if n in ('scraper', 'scraper_config', 'scraper_datahelper', 'lib')
                 or n.startswith('lib.')]:
        del sys.modules[name]  # the patch puts them back
    sys.path.insert(0, PYTHON)
    test.addCleanup(sys.path.remove, PYTHON)
    scraper = importlib.import_module('scraper')
    api_utils = sys.modules['lib.tmdbscraper.api_utils']
    # A session of the test's own, its requests answered by the network faked
    session = api_utils.Session()
    session.fetch = network.fetch
    patch = mock.patch.object(api_utils, 'SESSION', session)
    patch.start()
    test.addCleanup(patch.stop)
    return scraper, kodi, network


def run(scraper, *params):
    """scraper.run() for a call, as Kodi makes it: plugin://..., handle 1, ?query"""
    with mock.patch.object(sys, 'argv', ['plugin://metadata.themoviedb.org.python/', '1',
                                         '?' + '&'.join(params)]):
        scraper.run(sys.argv, 1)
