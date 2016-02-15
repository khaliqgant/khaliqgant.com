import requests
import json
import calendar
import time
import humanize
from datetime import timedelta


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


def format_yesterday(productivity):
    return 'foo'


def format_today(productivity):
    return 'bar'
