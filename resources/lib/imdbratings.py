import requests
import re

IMDB_RATINGS_URL = 'http://www.imdb.com/title/{}/ratings'
IMDB_RATING_VOTES_REGEX = re.compile(r'<p>(\d+).*?title\?user_rating\=.*?\">(.*?)</a>')
IMDB_TOP250_REGEX = re.compile(r'\#(\d+).*?"/chart/top')

# get the movie info via imdb
def get_imdb_ratinginfo(imdb_id):
    response = requests.get(IMDB_RATINGS_URL.format(imdb_id))
    return _parse_imdb_result(response.text if response.status_code == 200 else '')

def _parse_imdb_result(input_html):
    rating, votes = _get_imdb_rating_and_votes(input_html)
    top250 = _get_imdb_top250(input_html)

    return {'votes': votes, 'rating': rating, 'top250': top250}

def _get_imdb_rating_and_votes(input_html):
    match = re.search(IMDB_RATING_VOTES_REGEX, input_html)
    if (match):
        votes = int(match.group(1).replace(',', ''))
        rating = float(match.group(2))
        return rating, votes
    return (0, 0)

def _get_imdb_top250(input_html):
    match = re.search(IMDB_TOP250_REGEX, input_html)
    if (match):
        return match.group(1)
    return 0
