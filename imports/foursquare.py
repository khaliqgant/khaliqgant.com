import ConfigParser
import os
import sys

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import foursquare

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

configParser = ConfigParser.RawConfigParser()
configFilePath = '%s/config.txt' % root
configParser.read(configFilePath)


def bulk_import():
    token = configParser.get('foursquare', 'key')
    response = foursquare.retrieve(token)
    print(response)


if __name__ == '__main__':
    bulk_import()
