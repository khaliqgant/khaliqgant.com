import ConfigParser
import os
import sys
import time
import json
import argparse

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import foursquare



def init():
    global parser, token, path, root
    parser = argparse.ArgumentParser()
    parser.add_argument('--bulk')
    parser.add_argument('--update')

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    configParser = ConfigParser.RawConfigParser()
    configFilePath = '%s/config.txt' % root
    configParser.read(configFilePath)
    token = configParser.get('foursquare', 'key')

    path = root + "/data/foursquare/"


def bulk_export():
    total_responses = float("inf")

    # prep vars for import
    offset = 0
    number = 200
    iterations = 0

    while(total_responses > 0):
        append = "&offset=%s&limit=%s" % (offset, number)
        time.sleep(10)

        response = foursquare.retrieve(token, append)
        timestamp = str(response['data'][0]['createdAt']) + ".json"
        write_file = path + timestamp
        with open(write_file, 'w') as output_file:
            json.dump(response, output_file)
        # store responses just once
        if (iterations == 0):
            total_responses = response['count']
        offset += number
        total_responses -= number
        iterations += 1


def grabLatest():
    number = 200
    # grab newst file
    files = sorted(os.listdir(path))
    latest = files[-1]
    # put one second past to not grab an entry that already exists
    last_timestamp = latest[:-5]
    append = "&limit=%s&afterTimestamp=%s" % (number, int(last_timestamp) + 1)
    response = foursquare.retrieve(token, append)
    if (len(response['data'])):
        timestamp = str(response['data'][0]['createdAt']) + ".json"
        write_file = path + timestamp
        with open(write_file, 'w') as output_file:
            json.dump(response, output_file)
    else:
        print ("No newer checks to grab!")

if __name__ == '__main__':
    init()
    args = parser.parse_args()

    if (args.bulk == 'true'):
        bulk_export()

    if (args.update == 'true'):
        grabLatest()

