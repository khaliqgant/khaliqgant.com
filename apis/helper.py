import calendar
from datetime import datetime


def iso8601_to_epoch(datestring):
    """
        iso8601_to_epoch - convert the iso8601 date into the unix epoch
        time
        @source : https://gist.github.com/squioc/3078803
    """
    return calendar.timegm(datetime.strptime(
        datestring, "%Y-%m-%dT%H:%M:%SZ").timetuple())


def sort(github, foursquare, lastfms):
    """ sort the activities by the timestamp key added in
        @source : http://stackoverflow.com/questions/72899/how-do-i-sort-a-
        list-of-dictionaries-by-values-of-the-dictionary-in-python
    """
    # combine the lists
    activities = github + foursquare + lastfms

    # sort the lists and make sure timestamp is an int so sorts properly
    all = sorted(activities, key=lambda t: int(t['timestamp']), reverse=True)

    return all
