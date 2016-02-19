import requests
import json
import helper


def retrieve(token, append=False):
    """ retrieve foursquare (swarm) activity"""
    foursquares = get(token, append)
    checkins = foursquares['response']['checkins']['items']
    count = foursquares['response']['checkins']['count']

    # normalize timestamp
    for i, ch in enumerate(checkins):
        checkins[i]["_type"] = "foursquare"
        checkins[i]["timestamp"] = ch["createdAt"]

    return {"data": checkins, "count": count}


def todaysCount(token):
    epoch = helper.epoch_start()
    append = '&afterTimestamp=%s' % (epoch)
    checkins = get(token, append)
    count = len(checkins['response']['checkins']['items'])

    return count


def get(token, append=False):
    url = "https://api.foursquare.com/v2/users/self/checkins?oauth_token=%s&"\
        "v=20150727" % (token)
    if (append):
        url += append
    print(url)
    response = requests.get(url)
    foursquares = json.loads(response._content)

    return foursquares
