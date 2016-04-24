import requests
import requests_cache
import json


# https://developer.spotify.com/web-api/search-item/
def search(track, artist):
    """ retrieve spotify track information"""
    url = 'https://api.spotify.com/v1/search?q=%s+artist:%s&type=track' % \
            (track, artist)
    response = requests.get(url)
    tracks = json.loads(response._content)
    # let's keep it simple and grab the first item if available
    if len(tracks['tracks']['items']) > 0:
        return tracks['tracks']['items'][0]['external_urls']['spotify']
    else:
        return ''

