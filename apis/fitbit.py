import ConfigParser
import os
import requests
from libraries import fitbit
import json

"""
    Fitbit API
    Docs: https://dev.fitbit.com/docs/
"""

def authenticate():
    global headers
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    configParser = ConfigParser.RawConfigParser()
    configFilePath = '%s/config.txt' % root
    configParser.read(configFilePath)

    old_token = {}
    old_token['access_token'] = configParser.get('fitbit', 'access_token')
    old_token['refresh_token'] = configParser.get('fitbit', 'refresh_token')

    fit = fitbit.Fitbit()
    creds = fit.RefAccessToken(old_token);

    # write in the new creds
    configParser.set('fitbit', 'access_token', creds['access_token'])
    configParser.set('fitbit', 'refresh_token', creds['refresh_token'])
    with open(configFilePath, 'wb') as configFile:
        configParser.write(configFile)

    # set the auth headers to be used
    headers = {'Authorization': 'Bearer ' + creds['access_token']}


def profile():
    url = 'https://api.fitbit.com/1/user/-/profile.json'
    response = requests.get(url, headers=headers)
    data = json.loads(response._content)


if __name__ == '__main__':
    authenticate()
    profile()
