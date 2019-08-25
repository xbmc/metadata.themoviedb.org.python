import json
import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from lib.tmdbscraper.tmdb import TMDBMovieScraper
from lib.tmdbscraper.imdbratings import get_details as get_imdb_details
from scraper_datahelper import combine_scraped_details_info_and_ratings, configure_scraped_details, \
    find_uniqueids_in_text, get_params

ADDON = xbmcaddon.Addon()
ID = ADDON.getAddonInfo('id')
LANGUAGE = ADDON.getSetting('language')

scraper = TMDBMovieScraper(ADDON, LANGUAGE)

def log(msg, level=xbmc.LOGDEBUG):
    xbmc.log(msg='{addon}: {msg}'.format(addon=ID, msg=msg), level=level)

def search_for_movie(title, year, handle):
    log('Find movie with title {title} from year {year}'.format(title=title, year=year), xbmc.LOGINFO)
    search_results = scraper.search(title, year)
    if not search_results:
        return
    if 'error' in search_results:
        header = "The Movie Database Python error searching with web service TMDB"
        xbmcgui.Dialog().notification(header, search_results['error'], xbmcgui.NOTIFICATION_WARNING)
        log(header + ': ' + search_results['error'], xbmc.LOGWARNING)
        return

    for movie in search_results:
        listitem = xbmcgui.ListItem(movie['title'], offscreen=True)
        if year:
            listitem.setInfo('video', {'year': year})
        if movie['poster_path']:
            listitem.setArt({'thumb': movie['poster_path']})
        uniqueids = {'tmdb': str(movie['id'])}
        xbmcplugin.addDirectoryItem(handle=handle, url=json.dumps(uniqueids),
            listitem=listitem, isFolder=True)

# Low limit because a big list of artwork can cause trouble in some cases
# (a column can be too large for the MySQL integration),
# and how useful is a big list anyway? Not exactly rhetorical, this is an experiment.
IMAGE_LIMIT = 10

def add_artworks(listitem, artworks):
    for poster in artworks['poster'][:IMAGE_LIMIT]:
        listitem.addAvailableArtwork(poster['url'], "poster", poster['preview'])

    for poster in artworks['set.poster'][:IMAGE_LIMIT]:
        listitem.addAvailableArtwork(poster['url'], "set.poster", poster['preview'])

    if ADDON.getSettingBool('fanart'):
        fanart_to_set = [{'image': image['url'], 'preview': image['preview']}
            for image in artworks['fanart'][:IMAGE_LIMIT]]
        listitem.setAvailableFanart(fanart_to_set)

        for fanart in artworks['set.fanart'][:IMAGE_LIMIT]:
            listitem.addAvailableArtwork(fanart['url'], "set.fanart", fanart['preview'])

def get_details(input_uniqueids, handle):
    details = scraper.get_details(input_uniqueids)
    if not details:
        return False
    if 'error' in details:
        header = "The Movie Database Python error with web service TMDB"
        xbmcgui.Dialog().notification(header, details['error'], xbmcgui.NOTIFICATION_WARNING)
        log(header + ': ' + details['error'], xbmc.LOGWARNING)
        return False

    imdbinfo = get_imdb_details(details['uniqueids'])
    if 'error' in imdbinfo:
        header = "The Movie Database Python error with website IMDB"
        log(header + ': ' + imdbinfo['error'], xbmc.LOGWARNING)
    else:
        details = combine_scraped_details_info_and_ratings(details, imdbinfo)

    details = configure_scraped_details(details, ADDON)

    listitem = xbmcgui.ListItem(details['info']['title'], offscreen=True)
    listitem.setInfo('video', details['info'])
    listitem.setCast(details['cast'])
    listitem.setUniqueIDs(details['uniqueids'], 'tmdb')
    add_artworks(listitem, details['available_art'])

    for rating_type, value in details['ratings'].items():
        listitem.setRating(rating_type, value['rating'], value['votes'], value['default'])

    xbmcplugin.setResolvedUrl(handle=handle, succeeded=True, listitem=listitem)
    return True

def find_uniqueids_in_nfo(nfo, handle):
    uniqueids = find_uniqueids_in_text(nfo)
    if uniqueids:
        listitem = xbmcgui.ListItem(offscreen=True)
        xbmcplugin.addDirectoryItem(handle=handle, url=json.dumps(uniqueids), listitem=listitem, isFolder=True)

def run():
    params = get_params(sys.argv[1:])
    enddir = True
    if 'action' in params:
        action = params["action"]
        if action == 'find' and 'title' in params:
            search_for_movie(params["title"], params.get("year"), params['handle'])
        elif action == 'getdetails' and 'url' in params:
            enddir = not get_details(json.loads(params["url"]), params['handle'])
        elif action == 'NfoUrl' and 'nfo' in params:
            find_uniqueids_in_nfo(params["nfo"], params['handle'])
        else:
            log("unhandled action: " + action, xbmc.LOGWARNING)
    else:
        log("No action in 'params' to act on", xbmc.LOGWARNING)
    if enddir:
        xbmcplugin.endOfDirectory(params['handle'])

if __name__ == '__main__':
    run()
