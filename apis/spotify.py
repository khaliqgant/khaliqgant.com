import requests
import requests_cache
import json
import re


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


def lookup(lastfms):
    """ Do a look up of the last 10 tracks """
    for i, lf in enumerate(lastfms[0]):
        # only get 10 most recent
        if i < 10:
            artist = lf['artist']['#text'].replace(" ", "+")
            # remove special characters and then replace spaces with +
            track = re.sub('[^\sa-zA-Z0-9-_*.]', '', lf['name']).replace(" ", "+")
            spotify = search(track, artist)
            lastfms[0][i]['spotify'] = spotify
        else:
            break

    # lookup now playing too
    artist = lastfms[1]['artist']['#text'].replace(" ", "+")
    track = re.sub('[^\sa-zA-Z0-9-_*.]', '', lastfms[1]['name']).replace(" ", "+")
    spotify = search(track, artist)
    lastfms[1]['spotify'] = spotify

    return lastfms
