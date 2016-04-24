import requests_cache
import os
import datetime
import argparse
import grequests
from functools import wraps
from flask import jsonify

from flask import Flask, request, render_template, Response
app = Flask(__name__)

# import custom apis
from apis import helper, github, foursquare, lastfm, citibike, \
    fitbit, rescuetime, spotify

from config import auth

pwd = os.path.dirname(os.path.abspath(__file__))

# cache requests because rate limiting and like, sooo much traffic to my site
# documentation: http://requests-cache.readthedocs.org/en/latest/api.html
requests_cache.install_cache(
    '%s/data/api' % pwd, backend='sqlite', expire_after=1800
)

# set config for api info
configParser = auth.grab()
run_health = True


@app.route('/')
def index():
    clear_cache = request.args.get('cache')
    if clear_cache == "clear_dat":
        requests_cache.core.clear()

    fq_token = configParser.get('foursquare', 'key')
    api_key = configParser.get('lastfm', 'key')
    lastfm_secret = configParser.get('lastfm', 'secret')
    r_key = configParser.get('rescuetime', 'key')

    today = datetime.datetime.now().strftime("%A, %B %d %Y")
    commits = github.todaysCount()
    songs = lastfm.todaysCount(api_key)
    checkins = foursquare.todaysCount(fq_token)
    productivity = rescuetime.todaysProductivity(r_key)

    health_stats = {}
    if run_health:
        health_stats = fitbit.todaysStats()

    return render_template('home.html', today=today, commits=commits,
                           songs=songs, checkins=checkins,
                           health_stats=health_stats, productivity=productivity
                           )


@app.route('/activities')
def activities():
    # get tokens from config
    token = configParser.get('foursquare', 'key')
    api_key = configParser.get('lastfm', 'key')

    gh_url = github.getUrl()
    fs_url = foursquare.getUrl(token)
    lastfm_url = lastfm.getUrl(api_key)

    urls = [gh_url, fs_url, lastfm_url]
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs)

    gh_activities = github.parse(responses[0])
    fs_activities = foursquare.parse(responses[1])
    songs = lastfm.parse(responses[2])
    lastfms = songs[0]
    nowPlaying = songs[1]

    activities = helper.sort(gh_activities, fs_activities['data'], lastfms)

    return render_template('activities.html', activities=activities,
                           nowPlaying=nowPlaying)


@app.route('/spotify')
def spotify_api():
    artist = request.args.get('artist')
    track = request.args.get('track')
    if artist and track:
        track = spotify.search(track, artist)
        return jsonify(song=track)



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
