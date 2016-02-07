import ConfigParser
import os
import sys
import time
import json

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import foursquare

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

configParser = ConfigParser.RawConfigParser()
configFilePath = '%s/config.txt' % root
configParser.read(configFilePath)


def bulk_export():
    token = configParser.get('foursquare', 'key')
    total_responses = float("inf")

    # prep vars for import
    offset = 0
    number = 200
    iterations = 0
    path = root + "/data/foursquare/"

    while(total_responses > 0):
        append = "&offset=%s&limit=%s" % (offset, number)
        time.sleep(10)

        response = foursquare.retrieve(token, append)
        id = response['data'][0]['id'] + ".json"
        write_file = path + id
        with open(write_file, 'w') as output_file:
            json.dump(response, output_file)
        # store responses just once
        if (iterations == 0):
            total_responses = response['count']
        offset += number
        total_responses -= number
        iterations += 1


if __name__ == '__main__':
    bulk_export()
