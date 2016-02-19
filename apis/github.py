import requests
import json
from datetime import datetime
import helper


def retrieve():
    """ retrieve github activity"""

    # turn the response string into a json object
    activities = get()

    # normalize timestamp
    for i, ac in enumerate(activities):
        activities[i]["_type"] = "github"
        created = ac['created_at']
        timestamp = helper.iso8601_to_epoch(created)
        activities[i]["timestamp"] = timestamp
        activities[i]["time_string"] = datetime.fromtimestamp(timestamp)\
            .strftime('%A, %m/%d/%Y')

    return activities


def todaysCount():
    activities = get()
    count = 0
    for i, ac in enumerate(activities):
        created = ac['created_at']
        timestamp = helper.iso8601_to_epoch(created)
        if (datetime.fromtimestamp(timestamp).date() ==
                datetime.today().date()):

                if (ac['type'] == 'PushEvent'):
                    count += len(ac['payload']['commits'])
                else:
                    count += 1

    return count


def get():
    username = 'khaliqgant'
    url = "https://api.github.com/users/%s/events" % (username)
    response = requests.get(url)
    activities = json.loads(response._content)

    return activities
