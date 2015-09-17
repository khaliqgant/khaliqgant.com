import requests
import requests_cache
import json


def retrieve(home_east, home_west, school_return):
    """ retrieve citi bike info"""
    url = "http://api.citybik.es/citi-bike-nyc.json"
    # don't cache citi bike b/c need up to date info!
    with requests_cache.disabled():
        response = requests.get(url)
        bikes = json.loads(response._content)
        stats = {}
        for bike in bikes:
            if bike['number'] == int(home_east):
                stats['timestamp'] = bike['timestamp']
                stats['home_east'] = str(bike['bikes'])
            if bike['number'] == int(home_west):
                stats['home_west'] = str(bike['bikes'])
            if bike['number'] == int(school_return):
                stats['school_return'] = str(bike['bikes'])

    return stats
