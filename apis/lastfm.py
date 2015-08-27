import requests
import json
import calendar
import time
import humanize
from datetime import timedelta


def retrieve(api_key):
    """ retrieve lastFM activity """
    username = 'khaliqgant'
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user"\
        "=%s&api_key=%s&format=json" % (username, api_key)
    response = requests.get(url)
    listens = json.loads(response._content)
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
