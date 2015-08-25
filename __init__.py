import requests
import requests_cache
import json
import ConfigParser
import os
from datetime import datetime, timedelta
import calendar
import time
import humanize

from flask import Flask, render_template
app = Flask(__name__)
pwd = os.path.dirname(os.path.abspath(__file__))


# cache requests because rate limiting and like, sooo much traffic to my site
requests_cache.install_cache(
    '%s/data/api' % pwd, backend='sqlite', expire_after=1800
)

# set config for api info
configParser = ConfigParser.RawConfigParser()
configFilePath = '%s/config.txt' % pwd
configParser.read(configFilePath)


def iso8601_to_epoch(datestring):
    """
        iso8601_to_epoch - convert the iso8601 date into the unix epoch time
        @source : https://gist.github.com/squioc/3078803
    """
    return calendar.timegm(datetime.strptime(
        datestring, "%Y-%m-%dT%H:%M:%SZ").timetuple())


def github():
    """ retrieve github activity"""
    username = 'khaliqgant'
    url = "https://api.github.com/users/%s/events" % (username)
    response = requests.get(url)

    # turn the response string into a json object
    activities = json.loads(response._content)

    # normalize timestamp
    for i, ac in enumerate(activities):
        activities[i]["_type"] = "github"
        created = ac['created_at']
        timestamp = iso8601_to_epoch(created)
        activities[i]["timestamp"] = timestamp
        activities[i]["time_string"] = datetime.fromtimestamp(timestamp)\
            .strftime('%A, %m/%d/%Y')

    return activities


def foursquare():
    """ retrieve foursquare (swarm) activity"""
    token = configParser.get('foursquare', 'key')
    url = "https://api.foursquare.com/v2/users/self/checkins?oauth_token=%s&"\
        "v=20150727" % (token)
    response = requests.get(url)
    foursquares = json.loads(response._content)
    checkins = foursquares['response']['checkins']['items']

    # normalize timestamp
    for i, ch in enumerate(checkins):
        checkins[i]["_type"] = "foursquare"
        checkins[i]["timestamp"] = ch["createdAt"]

    return checkins


def lastFM():
    """ retrieve lastFM activity """
    username = 'khaliqgant'
    api_key = configParser.get('lastfm', 'api_key')
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


def sort(github, foursquare, lastfms):
    """ sort the activities by the timestamp key added in
        @source : http://stackoverflow.com/questions/72899/how-do-i-sort-a-
        list-of-dictionaries-by-values-of-the-dictionary-in-python
    """
    # combine the lists
    activities = github + foursquare + lastfms

    # sort the lists and make sure timestamp is an int so sorts properly
    all = sorted(activities, key=lambda t: int(t['timestamp']), reverse=True)

    return all


@app.route('/')
def index():
    gh_activities = github()
    fs_activities = foursquare()
    songs = lastFM()
    lastfms = songs[0]
    nowPlaying = songs[1]

    activities = sort(gh_activities, fs_activities, lastfms)

    return render_template('layout.html', activities=activities,
                           nowPlaying=nowPlaying)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
