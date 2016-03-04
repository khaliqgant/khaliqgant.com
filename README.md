[![Build Status](https://travis-ci.org/khaliqgant/khaliqgant.svg?branch=master)](https://travis-ci.org/khaliqgant/khaliqgant)
[![Requirements Status](https://requires.io/github/khaliqgant/khaliqgant/requirements.svg?branch=master)](https://requires.io/github/khaliqgant/khaliqgant/requirements/?branch=master)

[khaliqgant.com](http://khaliqgant.com) - A [Flask](http://flask.pocoo.org/docs/0.10/) App
=====

My personal website

## Getting started
1. Make sure virtualenv is installed, if not run
    ```
    sudo pip install virtualenv
    ```
2. If just setting up the project run
    ```
    virtualenv venv
    ```
3. Otherwise, set the correct environment
    ```
    . venv/bin/activate
    ```
4. If starting up, install Flask
    ```
    sudo pip install Flask
    ```

## Deployment
* [Digital Ocean Tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)


## Feature Ideas
* Dynamically created playlists from Spotify, lastfm, hypem apis
```
Spotify API
Create playlist: https://developer.spotify.com/web-api/create-playlist/
Add Track to playlist: https://developer.spotify.com/web-api/add-tracks-to-playlist/
```
* Hook in NYC things to do using Date Director code
* Provide daily stats using movesapp, and fitbit

## API
* Grab all data from foursquare and last fm to see what I was doing and listening
to on that day
* Use ES to store everything to allow for easy querying and access
* Grab everything to filesystem in json?
* Sleep data
* Rescuetime data
* Pocket api (https://getpocket.com/developer/docs/v3/retrieve)
* Show fitbit most recent workout in activities

### Stats For The Day (Dashboard)
* # of Steps
* Commits
* Music listening habits, top artist
* How well slept night before, cross reference Fitbit and SleepCycle
* Email stats, sent, received etc
* Things could do, concerts, events, date director API (keep in node app)
* Moves: https://github.com/lysol/moves

## What will go in ES
* Foursquare checkins
* Rescue time data only goes back a certain # of months? Using `anapi` data
    * https://www.rescuetime.com/anapi/data?key=&perspective=interval&format=json&resolution_time=month&restrict_begin=2016-02-11&restrict_kind=efficiency
    * Above might be useful for various intervals to store in ES
    * https://www.rescuetime.com/anapi/data?key=&perspective=interval&format=json&resolution_time=month&restrict_begin=2016-02-11&restrict_kind=category
    * Useful to show on website for the month, or just the week
    * Store historical websites in ES sorted by date for private use, what did i browse most on this day
    or week or month
* Financial Data (related repo)
* P90X Data
* Integrate with [Zenobase | https://zenobase.com/#/]
* Sleep cycle data by date

## Roadmap
* Import all foursquare data
* Integrate Fitbit API
* Add in Pocket additions to activities, use the since parameter (https://getpocket.com/developer/docs/v3/retrieve)

## Todos
* Look into fitbit API more
* Get number of commits per day
