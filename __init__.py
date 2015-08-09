import requests
import requests_cache
import json
import calendar
import ConfigParser
import os

pwd = os.environ['PWD']

configParser = ConfigParser.RawConfigParser()
configFilePath = '%s/config.txt' % pwd
configParser.read(configFilePath)

from flask import Flask, render_template

app = Flask(__name__)

# cache requests because rate limiting and like, sooo much traffic to my site
requests_cache.install_cache(
    '%s/data/api' % pwd, backend='sqlite', expire_after=180
)


def UTC_to_epoch(timestamp):
    """
        Convert UTC timestamp to epoch timestamp
        @source: http://stackoverflow.com/questions/24027863/
                    convert-a-utc-time-to-epoch
    """
    epoch = calendar.timegm(timestamp.utctimetuple())
    return epoch


def github():
    """ retrieve github activity"""
    username = 'khaliqgant'
    url = "https://api.github.com/users/%s/events" % (username)
    response = requests.get(url)

    # turn the response string into a json object
    activities = json.loads(response._content)

    return activities


def foursquare():
    """ retrieve foursquare (swarm) activity"""
    token = configParser.get('foursquare', 'key')
    url = "https://api.foursquare.com/v2/users/self/checkins?oauth_token=%s&"\
        "v=20150727" % (token)
    response = requests.get(url)
    foursquares = json.loads(response._content)
    return foursquares['response']['checkins']['items']


def lastFM():
    """ retrieve lastFM activity """
    username = 'khaliqgant'
    api_key = configParser.get('lastfm', 'api_key')
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user"\
        "=%s&api_key=%s&format=json" % (username, api_key)
    response = requests.get(url)
    #for attr, value in response.__dict__.iteritems():
        #print attr
        #print value
    listens = json.loads(response._content)
    return listens['recenttracks']['track']


def sort(github, foursquare):
    """ sort the activities by the created_at || createdAt date """
    #print type(github)
    #print type(foursquare)
    # combine the lists
    all = [g for f in zip(github, foursquare) for g in f]
    # now sort the lists by created_at
    #print all
    return


@app.route('/')
def index():
    gh_activities = github()
    fs_activities = foursquare()
    lastfms = lastFM()
    activities = sort(gh_activities, fs_activities)
    #print activities
    return render_template('layout.html', gh_activities=gh_activities,
                           fs_activities=fs_activities, lastfms=lastfms)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
