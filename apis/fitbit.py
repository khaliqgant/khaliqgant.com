import os
import sys
import requests
from libraries import fitbit
import json

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../config')))
import auth

"""
    Fitbit API
    Docs: https://dev.fitbit.com/docs/
"""


"""
    Authenticate
    Grab older tokens and try and refresh and set a global headers varaible
"""
def authenticate():
    global headers, authenticated
    configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config'))

    configFilePath = '%s/config.txt' % configPath
    configParser = auth.grab()

    old_token = {}
    old_token['access_token'] = configParser.get('fitbit', 'access_token')
    old_token['refresh_token'] = configParser.get('fitbit', 'refresh_token')

    fit = fitbit.Fitbit()
    try:
        creds = fit.RefAccessToken(old_token)

        # write in the new creds
        configParser.set('fitbit', 'access_token', creds['access_token'])
        configParser.set('fitbit', 'refresh_token', creds['refresh_token'])
        with open(configFilePath, 'wb') as configFile:
            configParser.write(configFile)

        # set the auth headers to be used
        headers = {'Authorization': 'Bearer ' + creds['access_token']}
        authenticated = True
    except Exception:
        headers = {}
        authenticated = False
        pass


def get(url, raw=False):
    data = {}
    try:
        response = requests.get(url, headers=headers)
        if raw:
            data = response._content
        else:
            data = json.loads(response._content)
    except requests.exceptions.RequestException as e:
        print e

    return data


def profile():
    url = 'https://api.fitbit.com/1/user/-/profile.json'
    data = get(url)

    return data


def activities_log(date):
    url = 'https://api.fitbit.com/1/user/-/activities/list.json' \
        '&user-id=-&afterDate=%s&offset=0&limit=10&sort=desc' % date
    print(url)
    data = get(url, True)
    print(data)


def recent_activities():
    url = 'https://api.fitbit.com/1/user/-/activities/recent.json'
    data = get(url)
    # the fitbit api isn't great here and doesn't return back the date
    # of the last excercise, just grab the most recent
    lastActivity = {}
    lastActivity['activity'] = data[0]['name']
    lastActivity['time'] = format(
        (float(data[0]['duration']) / 1000 / 60 / 60), '.2f'
    )

    return lastActivity


def steps(date):
    url = 'https://api.fitbit.com/1/user/-/activities/steps/date/%s/1d.json' \
        % date
    data = get(url)
    formatted = '{:,}'.format(
        int(data['activities-steps'][0]['value'])
    )

    return formatted


def calories(date):
    url = 'https://api.fitbit.com/1/user/-/activities/calories/date/%s/1d.json'\
        % date
    data = get(url)
    formatted = '{:,}'.format(
        int(data['activities-calories'][0]['value'])
    )

    return formatted


def sleep(date):
    url = 'https://api.fitbit.com/1/user/-/sleep/date/%s.json' % date
    data = get(url)
    sleep_data = {}
    asleep = format((float(data['summary']['totalMinutesAsleep']) / 60), '.2f')
    in_bed = format((float(data['summary']['totalTimeInBed']) / 60), '.2f')
    sleep_data['asleep'] = asleep
    sleep_data['in_bed'] = in_bed
    sleep_data['efficiency'] = computeEfficiency(data)

    return sleep_data


def computeEfficiency(data):
    records = data['summary']['totalSleepRecords']
    sleep_records = records - 1
    total = 0
    while (sleep_records >= 0):
        total = data['sleep'][sleep_records]['efficiency'] + total
        sleep_records = sleep_records - 1
    avg = format((float(total) / records), '.2f')

    return float(avg)


def stats(date):
    authenticate()
    all_stats = {}
    if authenticated:
        all_stats['steps'] = steps(date)
        all_stats['calories'] = calories(date)
        all_stats['sleep'] = sleep(date)
        all_stats['lastActivity'] = recent_activities()

    return all_stats


def todaysStats():
    todays = stats('today')

    return todays


if __name__ == '__main__':
    #authenticate()
    #recent_activities()
    #activities_log('2015-11-01')
    #profile()
    #sleep('2016-02-21')
