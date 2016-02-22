import requests_cache
import ConfigParser
import os
import datetime
import argparse
from functools import wraps

from flask import Flask, request, render_template, Response
app = Flask(__name__)

# import custom apis
from apis import helper, github, foursquare, lastfm, citibike, fitbit

pwd = os.path.dirname(os.path.abspath(__file__))

# cache requests because rate limiting and like, sooo much traffic to my site
# documentation: http://requests-cache.readthedocs.org/en/latest/api.html
requests_cache.install_cache(
    '%s/data/api' % pwd, backend='sqlite', expire_after=1800
)
#requests_cache.core.clear()

# set config for api info
configParser = ConfigParser.RawConfigParser()
configFilePath = '%s/config.txt' % pwd
configParser.read(configFilePath)
run_health = True


@app.route('/')
def index():
    token = configParser.get('foursquare', 'key')
    api_key = configParser.get('lastfm', 'api_key')
    today = datetime.datetime.now().strftime("%A, %B %d %Y")
    commits = github.todaysCount()
    songs = lastfm.todaysCount(api_key)
    checkins = foursquare.todaysCount(token)
    health_stats = {}
    if run_health:
        health_stats = fitbit.todaysStats()

    return render_template('home.html', today=today, commits=commits,
                           songs=songs, checkins=checkins,
                           health_stats=health_stats)


@app.route('/activities')
def activities():
    # get tokens from config
    token = configParser.get('foursquare', 'key')
    api_key = configParser.get('lastfm', 'api_key')

    gh_activities = github.retrieve()
    fs_activities = foursquare.retrieve(token)
    songs = lastfm.retrieve(api_key)
    lastfms = songs[0]
    nowPlaying = songs[1]

    activities = helper.sort(gh_activities, fs_activities['data'], lastfms)

    return render_template('activities.html', activities=activities,
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
    if specific == "school":
        school = citi_info['school_return']
        citi_info = {}
        citi_info['school_return'] = school
    return render_template('bike.html', citi=citi_info)


@app.route('/projects')
def projects():
    return render_template('projects.html')


def check_auth(username, password):
    uname = configParser.get('auth', 'user')
    passw = configParser.get('auth', 'pass')
    return username == uname and password == passw


def fail():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return fail()
        return f(*args, **kwargs)
    return decorated


@app.route('/api')
@requires_auth
def api():
    return render_template('api.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fitbit')
    args = parser.parse_args()

    if (args.fitbit == 'false'):
        run_health = False

    app.run(debug=True)
    app.run()
