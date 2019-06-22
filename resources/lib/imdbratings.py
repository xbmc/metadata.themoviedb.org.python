import requests
import re

IMDB_RATINGS_URL = 'https://www.imdb.com/title/{}/'

IMDB_RATING_REGEX = re.compile(r'itemprop="ratingValue".*?>.*?([\d.]+).*?<')
IMDB_VOTES_REGEX = re.compile(r'itemprop="ratingCount".*?>.*?([\d,]+).*?<')
IMDB_TOP250_REGEX = re.compile(r'Top Rated Movies #(\d+)')

# get the movie info via imdb
def get_imdb_ratinginfo(imdb_id):
    response = requests.get(IMDB_RATINGS_URL.format(imdb_id))
    return _parse_imdb_result(response.text if response.status_code == 200 else '')

def _parse_imdb_result(input_html):
    rating = _get_imdb_rating(input_html)
    votes = _get_imdb_votes(input_html)
    top250 = _get_imdb_top250(input_html)

    return {'votes': votes, 'rating': rating, 'top250': top250}

def _get_imdb_rating(input_html):
    match = re.search(IMDB_RATING_REGEX, input_html)
    if (match):
        return float(match.group(1))
    return 0

def _get_imdb_votes(input_html):
    match = re.search(IMDB_VOTES_REGEX, input_html)
    if (match):
        return int(match.group(1).replace(',', ''))
    return 0

def _get_imdb_top250(input_html):
    match = re.search(IMDB_TOP250_REGEX, input_html)
    if (match):
        return int(match.group(1))
    return 0
