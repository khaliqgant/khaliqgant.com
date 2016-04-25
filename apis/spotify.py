import requests
import json
import re
import helper


# https://developer.spotify.com/web-api/search-item/
def search(track, artist):
    """ retrieve spotify track information"""
    url = 'https://api.spotify.com/v1/search?q=%s+artist:%s&type=track' % \
        (track, artist)
    response = requests.get(url)
    tracks = json.loads(response._content)
    # let's keep it simple and grab the first item if available
    # sometimes from hypem tracks might be dissimilar, so let's make sure the
    # first one is similar at least
    if 'tracks' in tracks and len(tracks['tracks']['items']) > 0 and \
       helper.similar(tracks['tracks']['items'][0]['name'], track) > 0.5:
        return tracks['tracks']['items'][0]['external_urls']['spotify']
    else:
        return ''


def lookup(lastfms):
    """ Do a look up of the last 10 tracks """
    if len(lastfms[0]) > 0:
        for i, lf in enumerate(lastfms[0]):
            # only get 10 most recent
            if i < 10:
                artist = lf['artist']['#text'].replace(" ", "+")
                # remove special characters and then replace spaces with +
                track = re.sub('[^\sa-zA-Z0-9-_*.]', '', lf['name']) \
                    .replace(" ", "+")
                # TODO use async requests to send these requests all at once
                spotify = search(track, artist)
                lastfms[0][i]['spotify'] = spotify
            else:
                break

    # lookup now playing too
    if len(lastfms[1]) > 0:
        artist = lastfms[1]['artist']['#text'].replace(" ", "+")
        track = re.sub('[^\sa-zA-Z0-9-_*.]', '', lastfms[1]['name']) \
            .replace(" ", "+")
        spotify = search(track, artist)
        lastfms[1]['spotify'] = spotify

    return lastfms
