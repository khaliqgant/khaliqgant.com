import requests
import json
import re
import helper
import grequests

COUNT = 15


# https://developer.spotify.com/web-api/search-item/
def search(track, artist, urlOnly=False):
    """ retrieve spotify track information"""
    url = 'https://api.spotify.com/v1/search?q=%s+artist:%s&type=track' % \
        (track, artist)
    if urlOnly:
        return url
    response = requests.get(url)

    return parse(response, track)


def lookup(lastfms):
    urls = []
    tracks = []
    if len(lastfms[0]) > 0:
        for i, lf in enumerate(lastfms[0]):
            # only get 10 most recent
            if i < COUNT:
                artist = lf['artist']['#text'].replace(" ", "+")
                tracks.append(lf['name'])
                # remove special characters and then replace spaces with +
                track = re.sub('[^\sa-zA-Z0-9-_*.]', '', lf['name']) \
                    .replace(" ", "+")
                url = search(track, artist, True)
                urls.append(url)
            else:
                break
    spotifys = bulkSearch(urls, tracks)
    lastfms[0] = merge(spotifys, lastfms[0])

    # lookup now playing too
    if len(lastfms[1]) > 0:
        artist = lastfms[1]['artist']['#text'].replace(" ", "+")
        track = re.sub('[^\sa-zA-Z0-9-_*.]', '', lastfms[1]['name']) \
            .replace(" ", "+")
        spotify = search(track, artist)
        lastfms[1]['spotify'] = spotify

    return lastfms


def exception_handler(request, exception):
    print "Request failed"


def bulkSearch(urls, track_names):
    """ Async requests to spotify api and parse out the track """
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs, exception_handler=exception_handler)
    spotifys = []
    i = 0
    for resp in responses:
        spotifys.append(parse(resp, track_names[i]))
        i = i + 1

    return spotifys


def parse(response, track):
    """ Check for a tracks key, items and a similarity for the song search """
    try:
        tracks = json.loads(response._content)
        # let's keep it simple and grab the first item if available
        # sometimes from hypem tracks might be dissimilar, so let's make sure
        # the first one is similar at least
        if 'tracks' in tracks and len(tracks['tracks']['items']) > 0 and \
        helper.similar(tracks['tracks']['items'][0]['name'], track) > 0.4:
            return tracks['tracks']['items'][0]['external_urls']['spotify']
        else:
            return ''
    except Exception:
        return ''


def merge(spotifys, recents):
    """ put in the spotifys result in the array """
    for i, lf in enumerate(recents):
        # only get a number of most recent
        if i < COUNT:
            recents[i]['spotify'] = spotifys[i]
        else:
            break

    return recents
