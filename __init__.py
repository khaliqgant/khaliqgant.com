import requests_cache
import ConfigParser
import os

from flask import Flask, render_template
app = Flask(__name__)

# import custom apis
from apis import helper, github, foursquare, lastfm

pwd = os.path.dirname(os.path.abspath(__file__))

# cache requests because rate limiting and like, sooo much traffic to my site
requests_cache.install_cache(
    '%s/data/api' % pwd, backend='sqlite', expire_after=1800
)

# set config for api info
configParser = ConfigParser.RawConfigParser()
configFilePath = '%s/config.txt' % pwd
configParser.read(configFilePath)


@app.route('/')
def index():
    # get tokens from config
    token = configParser.get('foursquare', 'key')
    api_key = configParser.get('lastfm', 'api_key')

    gh_activities = github.retrieve()
    fs_activities = foursquare.retrieve(token)
    songs = lastfm.retrieve(api_key)
    lastfms = songs[0]
    nowPlaying = songs[1]

    activities = helper.sort(gh_activities, fs_activities, lastfms)

    return render_template('layout.html', activities=activities,
                           nowPlaying=nowPlaying)


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
