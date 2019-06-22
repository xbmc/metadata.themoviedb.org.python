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
def get_trailer(trailers):
    if 'youtube' in trailers:
        for trailer in trailers['youtube']:
            return 'plugin://plugin.video.youtube/?action=play_video&videoid='+trailer['source']
    return ''

# find the set in the list
def get_set(colls):
    if colls and 'name' in colls:
        return colls['name']
    return ""

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

# get the images from the movie info
def get_artworks(liz, movie):
    found = False
    for img in movie.images['posters']:
        if img['iso_639_1'] == LANGUAGE:
            found = True
            liz.addAvailableArtwork(tmdburls['original']+img['file_path'], "poster")
    if LANGUAGE != 'en':
        for img in movie.images['posters']:
            if img['iso_639_1'] == 'en':
                found = True
                liz.addAvailableArtwork(tmdburls['original']+img['file_path'], "poster")
    if not found:
        for img in movie.images['posters']:
            liz.addAvailableArtwork(tmdburls['original']+img['file_path'], "poster")

    if ADDON.getSetting('fanart') == 'true':
        fanarts = []
        for img in movie.images['backdrops']:
            fanarts.append({'image': tmdburls['original']+img['file_path'],
                'preview': tmdburls['preview']+img['file_path']})
        liz.setAvailableFanart(fanarts)

# get the details of the found movie
def get_details(mid):
    parsetrailer = ADDON.getSetting('trailer') == 'true'
    movie = get_tmdb_movie(mid, getImages=False, getTrailers=parsetrailer, language=LANGUAGE)
    if movie:
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

        missingtrailer = (parsetrailer and not movie.trailers['youtube'])

        # retrieve english version in case of a fallback and to get all the artworks
        movie_en = get_tmdb_movie(mid, getTrailers=missingtrailer, getReleases=False, getCast=False)

        trailer = ""
        if missingtrailer:
            trailer = get_trailer(movie_en.trailers)
        elif parsetrailer:
            trailer = get_trailer(movie.trailers)

        imdb_info = get_imdb_ratinginfo(movie.imdb_id)

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
                'set': get_set(movie.belongs_to_collection) if \
                    movie.belongs_to_collection else get_set(movie_en.belongs_to_collection),
                'studio': get_names(movie.production_companies),
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
        if 'cast' in movie.casts:
            for actor in movie.casts['cast']:
                cast.append({'name': actor['name'],
                    'role': actor['character'],
                    'thumbnail': tmdburls['original']+actor['profile_path'] if actor['profile_path'] else "",
                    'order': actor['order']})
        liz.setCast(cast)
        get_artworks(liz, movie_en)
        liz.setProperty('video.date_added', '2016-01-01')
        xbmcplugin.setResolvedUrl(handle=HANDLE, succeeded=True, listitem=liz)

# add the found artworks to the list
def add_artworks(mid):
    movie_en = get_tmdb_movie(mid, getTrailers=False,
        getReleases=False, getCast=False)
    liz = xbmcgui.ListItem(movie.title, offscreen=True)
    get_artworks(liz, movie_en)
    xbmcplugin.setResolvedUrl(handle=HANDLE, succeeded=True, listitem=liz)

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
            get_details(unquote_plus(params["url"]))
            enddir = False
        elif action == 'getartwork' and 'id' in params:
            add_artworks(unquote_plus(params["id"]))
            enddir = False
        elif action == 'nfourl' and 'nfo' in params:
            find_id(unquote_plus(params["nfo"]))
    if enddir:
        xbmcplugin.endOfDirectory(HANDLE)
