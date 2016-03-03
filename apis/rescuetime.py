import requests
import json

"""
    Rescuetime API
    @docs: https://www.rescuetime.com/apidoc
"""


def get(url):
    response = requests.get(url)
    productivity = json.loads(response._content)

    return productivity


def todaysProductivity(key):
    # get back top 3 activites
    url = 'https://www.rescuetime.com/anapi/data?key=%s&perspective=interval&'\
        'format=json&resolution_time=day&restrict_kind=overview' % (key)
    overall = get(url)
    top_activities = format_activities(overall)
    return top_activities


def retrieve(api_key, stats):
    if (stats == 'yesterday'):
        url = 'https://www.rescuetime.com/anapi/daily_summary_feed?key=%s' \
            % (api_key)
        response = requests.get(url)
        productivity = json.loads(response._content)
        formatted = format_yesterday(productivity)

    if (stats == 'today'):
        url = 'https://www.rescuetime.com/anapi/data?key=%s&format=json' \
            % (api_key)
        response = requests.get(url)
        productivity = json.loads(response._content)
        formatted = format_today(productivity)

    return formatted


def format_activities(data):
    #test url: https://www.rescuetime.com/anapi/data?key=B63DR36aZMcRDhXf4yJ3EzqUCqkeoe_p5Y6Pobf6&perspective=interval&format=json&resolution_time=day&restrict_kind=overview
    activities = []
    if (data['row_headers'][1] == "Time Spent (seconds)"):
        for i in range(0, 3):
            activity = {}
            activity['activity'] = data['rows'][i][3]
            activity['time'] = format(
                (float(data['rows'][i][1]) / 60 / 60), '.2f'
            )
            activities.append(activity)
    return activities
