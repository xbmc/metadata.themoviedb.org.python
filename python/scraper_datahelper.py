import re
try:
    import urlparse
    from urllib import unquote_plus
except ImportError: # py2 / py3
    from urllib import parse as urlparse
    from urllib.parse import unquote_plus

# get addon params from the plugin path querystring
def get_params(argv):
    result = {'handle': int(argv[0])}
    if len(argv) < 2 or not argv[1]:
        return result

    result_list = [(key, unquote_plus(value)) for key, value in urlparse.parse_qsl(argv[1].lstrip('?'))]
    result.update(result_list)
    return result

def configure_scraped_details(details, settings):
    details = _configure_keeporiginaltitle(details, settings)
    details = _configure_trailer(details, settings)
    details = _configure_multiple_studios(details, settings)
    details = _configure_default_rating(details, settings)
    return details

def _configure_keeporiginaltitle(details, settings):
    if settings.getSettingBool('keeporiginaltitle'):
        details['info']['title'] = details['info']['original_title']
    return details

def _configure_trailer(details, settings):
    if details['info'].get('trailer') and not settings.getSettingBool('trailer'):
        del details['info']['trailer']
    return details

def _configure_multiple_studios(details, settings):
    if not settings.getSettingBool('multiple_studios'):
        details['info']['studio'] = details['info']['studio'][:1]
    return details

def _configure_default_rating(details, settings):
    imdb_default = bool(details['ratings'].get('imdb')) and settings.getSetting('RatingS') == 'IMDb'
    trakt_default = bool(details['ratings'].get('trakt')) and settings.getSetting('RatingS') == 'Trakt'
    default_rating = 'tmdb'
    if imdb_default:
        default_rating = 'imdb' 
    elif trakt_default:
        default_rating = 'trakt' 
    if default_rating not in details['ratings']:
        default_rating = list(details['ratings'].keys())[0] if details['ratings'] else None
    for rating_type in details['ratings'].keys():
        details['ratings'][rating_type]['default'] = rating_type == default_rating
    return details

def combine_scraped_details_info_and_ratings(original_details, additional_details):
    def update_or_set(details, key, value):
        if key in details:
            details[key].update(value)
        else:
            details[key] = value

    if additional_details:
        if additional_details.get('info'):
            update_or_set(original_details, 'info', additional_details['info'])
        if additional_details.get('ratings'):
            update_or_set(original_details, 'ratings', additional_details['ratings'])
    return original_details

def find_uniqueids_in_text(input_text):
    result = {}
    res = re.search(r'(themoviedb.org/movie/)([0-9]+)', input_text)
    if (res):
        result['tmdb'] = res.group(2)
    res = re.search(r'imdb....?/title/tt([0-9]+)', input_text)
    if (res):
        result['imdb'] = 'tt' + res.group(1)
    else:
        res = re.search(r'imdb....?/Title\?t{0,2}([0-9]+)', input_text)
        if (res):
            result['imdb'] = 'tt' + res.group(1)
    return result
