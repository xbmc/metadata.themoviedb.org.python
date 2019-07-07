#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xbmcplugin
import xbmcgui
import xbmc
import xbmcaddon
import sys
try:
    import urlparse
    from urllib import unquote_plus
except ModuleNotFoundError:
    from urllib import parse as urlparse
    from urllib.parse import unquote_plus
import re
from datetime import datetime, timedelta

import resources.lib.tmdbsimple as tmdb
from resources.lib.imdbratings import get_imdb_ratinginfo

tmdb.API_KEY = 'f090bb54758cabf231fb605d3e3e0468'
ADDON = xbmcaddon.Addon()
ID = ADDON.getAddonInfo('id')
LANGUAGE = ADDON.getSetting('language')
HANDLE = int(sys.argv[1])

# log function
def log(msg):
    xbmc.log(msg='{addon}: {msg}'.format(addon=ID, msg=msg), level=xbmc.LOGDEBUG)

# get addon url params
def get_params():
    if not sys.argv[2]:
        return {}
    return dict(urlparse.parse_qsl(sys.argv[2].lstrip('?')))

def get_date_numeric(dt):
    return (dt-datetime(1970, 1, 1)).total_seconds()

# get urls and update them if they don't exist or they're too old
def load_base_urls():
    tmdburls = {}
    tmdburls['original'] = ADDON.getSetting('originalUrl')
    tmdburls['preview'] = ADDON.getSetting('previewUrl')
    lastUpdated = ADDON.getSetting('lastUpdated')
    if tmdburls['original'] == "" or tmdburls['preview'] == "" or not lastUpdated or \
            float(lastUpdated) < get_date_numeric(datetime.now() - timedelta(days=30)):
        conf = tmdb.Configuration().info()
        if conf:
            tmdburls['original'] = conf['images']['base_url'] + 'original'
            tmdburls['preview'] = conf['images']['base_url'] + 'w780'
            ADDON.setSetting('originalUrl', tmdburls['original'])
            ADDON.setSetting('previewUrl', tmdburls['preview'])
            ADDON.setSetting('lastUpdated', str(get_date_numeric(datetime.now())))
    return tmdburls

def search_movies(title, year=None):
    search = tmdb.Search()
    response = search.movie(query=title, year=year, language=LANGUAGE)
    return search.results

# find the youtube trailer in the list
def get_trailer(trailers, trailers_en):
    if trailers.get('youtube'):
        return 'plugin://plugin.video.youtube/?action=play_video&videoid='+trailers['youtube'][0]['source']
    if trailers_en.get('youtube'):
        return 'plugin://plugin.video.youtube/?action=play_video&videoid='+trailers_en['youtube'][0]['source']
    return ''

def get_set_id(colls):
    if colls and 'id' in colls:
        return colls['id']
    return None

# helper function to get the names from a list of dictionaries
def get_names(names):
    nms = []
    if names:
        for name in names:
            nms.append(name['name'])
    return nms

# get the cast list
def get_cast_members(casts, casttype, department, jobs):
    writers = []
    if casttype in casts:
        for cast in casts[casttype]:
            if cast['department'] == department and cast['job'] in jobs:
                writers.append(cast['name'])
    return writers

# add the found movies to the list
def add_movies(title, year=None):
    log('Find movie with title {title} from year {year}'.format(title=title, year=year))
    for movie in search_movies(title, year):
        if movie['poster_path']:
            liz = xbmcgui.ListItem(movie['title'],
                thumbnailImage=tmdburls['preview']+movie['poster_path'], offscreen=True)
        else:
            liz = xbmcgui.ListItem(movie['title'], offscreen=True)
        #liz.setProperty('relevance', '0.5')
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=str(movie['id']),
            listitem=liz, isFolder=True)

# get the movie info via tmdbsimple
def get_tmdb_movie(mid, getInfo=True, getTrailers=True, getReleases=True, getCast=True, getImages=True, language=None):
    movie = tmdb.Movies(mid)
    details = ''
    if getTrailers:
        details += 'trailers,'
    if getReleases:
        details += 'releases,'
    if getCast:
        details += 'casts,'
    if getImages:
        details += 'images,'
    try:
        movie.info(language=language, append_to_response=details)
        return movie
    except:
        return None

def get_tmdb_moviecollection(collection_id, language=None):
    if not collection_id:
        return None
    collection = tmdb.Collections(collection_id)
    try:
        collection.info(language=language, append_to_response='images')
        return collection
    except:
        return None

def parse_artworks(movie, collection):
    posters = [tmdburls['original'] + img['file_path']
        for img in movie.images['posters']
        if img['iso_639_1'] == LANGUAGE]

    # Add backup English posters
    if LANGUAGE != 'en':
        posters.extend(tmdburls['original'] + img['file_path']
            for img in movie.images['posters']
            if img['iso_639_1'] == 'en')

    # Add any poster if nothing set so far
    if not posters:
        posters = [tmdburls['original'] + img['file_path']
            for img in movie.images['posters']]

    fanart = [{'image': tmdburls['original'] + img['file_path'],
            'preview': tmdburls['preview'] + img['file_path']}
        for img in movie.images['backdrops']]

    setposters = []
    if collection:
        setposters = [tmdburls['original'] + img['file_path']
            for img in collection.images['posters']
            if img['iso_639_1'] == LANGUAGE]

        # Add backup English posters
        if LANGUAGE != 'en':
            setposters.extend(tmdburls['original'] + img['file_path']
                for img in collection.images['posters']
                if img['iso_639_1'] == 'en')

        # Add any poster if nothing set so far
        if not setposters:
            setposters = [tmdburls['original'] + img['file_path']
                for img in collection.images['posters']]

    setfanart = []
    if collection:
        setfanart = [tmdburls['original'] + img['file_path']
            for img in collection.images['backdrops']]

    return posters, fanart, setposters, setfanart

IMAGE_LIMIT = 30

# get the images from the movie info
def get_artworks(liz, movie, collection):
    posters, fanart, setposters, setfanart = parse_artworks(movie, collection)

    postercount = 0
    for poster in posters:
        if postercount >= IMAGE_LIMIT:
            break
        liz.addAvailableArtwork(poster, "poster")
        postercount += 1

    setcount = 0
    for poster in setposters:
        if setcount >= IMAGE_LIMIT:
            break
        liz.addAvailableArtwork(poster, "set.poster")
        setcount += 1

    if ADDON.getSetting('fanart') == 'true':
        fanarts = []
        for f_art in fanart:
            if len(fanart) >= IMAGE_LIMIT:
                break
            fanarts.append(f_art)
        liz.setAvailableFanart(fanarts)

        setcount = 0
        for f_art in setfanart:
            if setcount >= IMAGE_LIMIT:
                break
            liz.addAvailableArtwork(f_art, "set.fanart")
            setcount += 1

# get the details of the found movie
def get_details(mid):
    parsetrailer = ADDON.getSetting('trailer') == 'true'
    movie = get_tmdb_movie(mid, getImages=False, getTrailers=parsetrailer, language=LANGUAGE)
    if not movie:
        return False

    imdb_info = get_imdb_ratinginfo(movie.imdb_id)
    collection = get_tmdb_moviecollection(get_set_id(movie.belongs_to_collection), LANGUAGE) \
        if movie.belongs_to_collection else None

    # retrieve english version in case of a fallback and to get all the artworks
    movie_en = get_tmdb_movie(mid, getTrailers=parsetrailer, getReleases=False, getCast=False)
    collection_en = get_tmdb_moviecollection(get_set_id(movie.belongs_to_collection)) \
        if movie.belongs_to_collection else None

    return _get_details(movie, movie_en, imdb_info, collection, collection_en)

def _get_details(movie, movie_en, imdb_info, collection, collection_en):
    if ADDON.getSetting('keeporiginaltitle') == 'true':
        title = movie.original_title
    else:
        title = movie.title
    liz = xbmcgui.ListItem(title, offscreen=True)
    mpaa = ''
    if 'countries' in movie.releases:
        certprefix = ADDON.getSetting('certprefix')
        certcountry = ADDON.getSetting('tmdbcertcountry').upper()
        for c in movie.releases['countries']:
            if c['iso_3166_1'] == certcountry and c['certification']:
                mpaa = certprefix + c['certification']
                break

    trailer = get_trailer(movie.trailers, movie_en.trailers) \
        if hasattr(movie, 'trailers') else ''

    studios = get_names(movie.production_companies)
    if not ADDON.getSettingBool('multiple_studios'):
        studios = studios[:1]

    if collection:
        set_title = collection.name or collection_en.name
        set_overview = collection.overview or collection_en.overview
    else:
        set_title = None
        set_overview = None

    liz.setInfo('video',
        {'title': title,
            'originaltitle': movie.original_title,
            'top250': imdb_info['top250'],
            'plot': movie.overview if movie.overview else movie_en.overview,
            'tagline': movie.tagline if movie.tagline else movie_en.tagline,
            'duration': movie.runtime * 60,
            'mpaa': mpaa,
            'trailer': trailer,
            'genre': get_names(movie.genres),
            'country': get_names(movie.production_countries),
            'credits': get_cast_members(movie.casts, 'crew', 'Writing',
                ['Screenplay', 'Writer', 'Author']),
            'director': get_cast_members(movie.casts, 'crew', 'Directing', ['Director']),
            'set': set_title,
            'setoverview': set_overview,
            'studio': studios,
            'premiered': movie.release_date
    })

    if imdb_info['votes'] > 0:
        imdbDef = ADDON.getSetting('RatingS') == 'IMDb'
        liz.setRating("imdb", imdb_info['rating'], imdb_info['votes'], imdbDef)
        liz.setRating("tmdb", movie.vote_average, movie.vote_count, not imdbDef)
    else:
        liz.setRating("tmdb", movie.vote_average, movie.vote_count, True)
    liz.setUniqueIDs({'tmdb': movie.id, 'imdb': movie.imdb_id}, 'tmdb')
    cast = []
    for actor in movie.casts.get('cast', []):
        cast.append({'name': actor['name'],
            'role': actor['character'],
            'thumbnail': tmdburls['original']+actor['profile_path'] if actor['profile_path'] else "",
            'order': actor['order']})
    liz.setCast(cast)
    get_artworks(liz, movie_en, collection_en)

    xbmcplugin.setResolvedUrl(handle=HANDLE, succeeded=True, listitem=liz)
    return True

# find the id from the link if there is
def get_id(nfo):
    res = re.search(r'(themoviedb.org/movie/)([0-9]*)', nfo)
    if (res):
        return res.group(2)
    res = re.search(r'imdb....?/title/tt([0-9]+)', nfo)
    if (res):
        return 'tt' + res.group(1)
    res = re.search(r'imdb....?/Title\?t{0,2}([0-9]+)', nfo)
    if (res):
        return 'tt' + res.group(1)

# find and add the id from the link if there is
def find_id(nfo):
    Id = get_id(nfo)
    if Id:
        liz = xbmcgui.ListItem(offscreen=True)
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=Id, listitem=liz, isFolder=True)

def run():
    params = get_params()
    enddir = True
    if 'action' in params:
        global tmdburls
        tmdburls = load_base_urls()
        action = unquote_plus(params["action"])
        if action == 'find' and 'title' in params:
            add_movies(unquote_plus(params["title"]), params.get("year", None))
        elif action == 'getdetails' and 'url' in params:
            enddir = not get_details(unquote_plus(params["url"]))
        elif action == 'NfoUrl' and 'nfo' in params:
            find_id(unquote_plus(params["nfo"]))
        else:
            log("unhandled action: " + params['action'])
    else:
        log("No action in 'params' to act on")
    if enddir:
        xbmcplugin.endOfDirectory(HANDLE)
