import requests
import json
from datetime import datetime
import helper


def retrieve():
    """ retrieve github activity"""
    username = 'khaliqgant'
    url = "https://api.github.com/users/%s/events" % (username)
    response = requests.get(url)

    # turn the response string into a json object
    activities = json.loads(response._content)

    # normalize timestamp
    for i, ac in enumerate(activities):
        activities[i]["_type"] = "github"
        created = ac['created_at']
        timestamp = helper.iso8601_to_epoch(created)
        activities[i]["timestamp"] = timestamp
        activities[i]["time_string"] = datetime.fromtimestamp(timestamp)\
            .strftime('%A, %m/%d/%Y')

    return activities
