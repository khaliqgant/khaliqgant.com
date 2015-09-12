import requests
import json
import datetime


def retrieve(home_east,home_west,school_return):
    """ retrieve citi bike info"""
    url = "http://api.citybik.es/citi-bike-nyc.json"
    response = requests.get(url)
    bikes = json.loads(response._content)
    #print(datetime.datetime.strptime( "2015-09-12T14:44:59.798Z", "%Y-%m-%dT%H:%M:%S.%fZ" ))
    stats = {}
    for bike in bikes:
        if bike['idx'] == int (home_east):
            stats['timestamp'] = bike['timestamp']
            stats['home_east'] = str (bike['bikes'])
        if bike['idx'] == int (home_west):
            stats['home_west'] = str (bike['bikes'])
        if bike['idx'] == int (school_return):
            stats['school_return'] = str (bike['bikes'])

    return stats


