
import requests
import re

# get the movie info via imdb
def get_imdb_ratinginfo(id):
    top250 = 0
    votes = 0
    rating = 0
    r = requests.get('http://www.imdb.com/title/'+id+'/ratings')
    if r.status_code == 200:
        res = re.search(r'<p>(\d+).*?title\?user_rating\=.*?\">(.*?)</a>', r.text)
        if (res):
            votes = int(res.group(1).replace(',', ''))
            rating = float(res.group(2))
        res = re.search(r'\#(\d+).*?"/chart/top', r.text)
        if (res):
            top250 = res.group(1)
    return {'votes': votes, 'rating': rating, 'top250': top250}
