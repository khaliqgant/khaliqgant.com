import requests
import requests_cache
import json
import ConfigParser
import os
from operator import itemgetter
from datetime import datetime
import calendar

from flask import Flask, render_template
app = Flask(__name__)
pwd = os.environ['PWD']


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
        activities[i]["type"] = "github"
        created = ac['created_at']
        timestamp = iso8601_to_epoch(created)
        activities[i]["timestamp"] = timestamp

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
        checkins[i]["type"] = "foursquare"
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

    # normalize timestamp
    for i, lf in enumerate(lastfms):
        lastfms[i]["type"] = "lastfm"
        if "date" in lf:
            lastfms[i]["timestamp"] = lf["date"]["uts"]
        else:
            lastfms[i]["timestamp"] = "1439170466"

    return lastfms


def sort(github, foursquare, lastfms):
    """ sort the activities by the timestamp key added in
        @source : http://stackoverflow.com/questions/72899/how-do-i-sort-a-
        list-of-dictionaries-by-values-of-the-dictionary-in-python
    """
    # combine the lists
    activities = github + foursquare + lastfms
    # sort the lists
    all = sorted(activities, key=itemgetter('timestamp'), reverse=True)

    return all


@app.route('/')
def index():
    gh_activities = github()
    fs_activities = foursquare()
    lastfms = lastFM()

    activities = sort(gh_activities, fs_activities, lastfms)

    return render_template('layout.html', activities=activities)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
