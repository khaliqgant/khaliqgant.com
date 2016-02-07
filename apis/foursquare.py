import requests
import json


def retrieve(token, append=False):
    """ retrieve foursquare (swarm) activity"""
    url = "https://api.foursquare.com/v2/users/self/checkins?oauth_token=%s&"\
        "v=20150727" % (token)
    if (append):
        url += append
    response = requests.get(url)
    foursquares = json.loads(response._content)
    checkins = foursquares['response']['checkins']['items']
    count = foursquares['response']['checkins']['count']

    # normalize timestamp
    for i, ch in enumerate(checkins):
        checkins[i]["_type"] = "foursquare"
        checkins[i]["timestamp"] = ch["createdAt"]

    return {"data": checkins, "count": count}
