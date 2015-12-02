import requests_cache
import ConfigParser
import os

from flask import Flask, request, render_template
app = Flask(__name__)

# import custom apis
from apis import helper, github, foursquare, lastfm, citibike

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

    return render_template('home.html', activities=activities,
                           nowPlaying=nowPlaying)


@app.route('/citi')
def citi():
    home_east = configParser.get('citibike', 'home_east')
    home_west = configParser.get('citibike', 'home_west')
    school_return = configParser.get('citibike', 'school_return')
    work = configParser.get('citibike', 'work')

    citi_info = citibike.retrieve(home_east, home_west, school_return, work)
    # see if specific location is specified
    specific = request.args.get('loc')
    echo = request.args.get('echo')
    if (echo):
        #format response correctly
        print 'yo'

    if specific == "school":
        school = citi_info['school_return']
        citi_info = {}
        citi_info['school_return'] = school
    return render_template('bike.html', citi=citi_info)


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
