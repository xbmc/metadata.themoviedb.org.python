def configure_scraped_details(details, settings):
    details = _configure_rating_prefix(details, settings)
    details = _configure_keeporiginaltitle(details, settings)
    details = _configure_trailer(details, settings)
    details = _configure_multiple_studios(details, settings)
    details = _configure_default_rating(details, settings)
    return details

def _configure_rating_prefix(details, settings):
    if details['info'].get('mpaa'):
        details['info']['mpaa'] = settings.getSettingString('certprefix') + details['info']['mpaa']
    return details

def _configure_keeporiginaltitle(details, settings):
    if settings.getSettingBool('keeporiginaltitle'):
        details['info']['title'] = details['info']['originaltitle']
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
    default_rating = 'themoviedb'
    if imdb_default:
        default_rating = 'imdb'
    elif trakt_default:
        default_rating = 'trakt'
    if default_rating not in details['ratings']:
        default_rating = list(details['ratings'].keys())[0] if details['ratings'] else None
    for rating_type in details['ratings'].keys():
        details['ratings'][rating_type]['default'] = rating_type == default_rating
    return details
