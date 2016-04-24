import requests
import json
import helper


def retrieve(token, append=False):
    """ retrieve foursquare (swarm) activity"""
    response = get(token, append)

    return parse(response)


def todaysCount(token):
    epoch = helper.epoch_start()
    append = '&afterTimestamp=%s' % (epoch)
    response = get(token, append)
    checkins = json.loads(response._content)
    count = len(checkins['response']['checkins']['items'])

    return count


def get(token, append=False, urlOnly=False):
    url = "https://api.foursquare.com/v2/users/self/checkins?oauth_token=%s&"\
        "v=20150727" % (token)
    if (append):
        url += append
    if urlOnly:
        return url
    response = requests.get(url)

    return response


def getUrl(token):
    return get(token, False, True)


def parse(response):
    foursquares = json.loads(response._content)
    checkins = foursquares['response']['checkins']['items']
    count = foursquares['response']['checkins']['count']

    # normalize timestamp
    for i, ch in enumerate(checkins):
        checkins[i]["_type"] = "foursquare"
        checkins[i]["timestamp"] = ch["createdAt"]

    return {"data": checkins, "count": count}
