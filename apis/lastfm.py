import requests
import json
import calendar
import humanize
import helper
import time
from datetime import datetime, date
from datetime import timedelta
from lastfmclient import LastfmClient


def retrieve(api_key):
    """ retrieve lastFM activity """
    listens = get(api_key)
    lastfms = listens['recenttracks']['track']

    # in case there isn't anything playing right now, set empty list
    nowPlaying = []
    # normalize timestamp
    for i, lf in enumerate(lastfms):
        lastfms[i]["_type"] = "lastfm"
        if "date" in lf:
            lastfms[i]["timestamp"] = lf["date"]["uts"]
            now_stamp = calendar.timegm(time.gmtime())
            elapsed = now_stamp - int(lf["date"]["uts"])
            lastfms[i]["elapsed"] = humanize\
                .naturaltime(timedelta(seconds=elapsed))
        else:
            lastfms[i]["timestamp"] = calendar.timegm(time.gmtime())
            nowPlaying = lastfms[i]

    return [lastfms, nowPlaying]


def todaysCount(api_key):
    epoch = helper.epoch_start()
    params = '&from=%s' % (epoch)

    listens = get(api_key, params)
    count = listens['recenttracks']['@attr']['total']

    return int(count)


def get(api_key, additional=False):
    username = 'khaliqgant'
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user"\
        "=%s&api_key=%s&format=json" % (username, api_key)
    if additional:
        url += additional
    response = requests.get(url)
    listens = json.loads(response._content)

    return listens


def topArtists(api_key, secret, period):
    api = LastfmClient(
        api_key=api_key,
        api_secret=secret,
        session_key=''
    )
    artists = api.user.get_top_artists('khaliqgant', None, None, period)

    return artists


def topAlbums(api_key, secret, period):
    api = LastfmClient(
        api_key=api_key,
        api_secret=secret,
        session_key=''
    )
    albums = api.user.get_top_albums('khaliqgant', None, None, period)

    return albums
