import os
import ConfigParser


def grab():
    pwd = os.path.dirname(os.path.abspath(__file__))
    configParser = ConfigParser.RawConfigParser()
    configFilePath = '%s/config.txt' % pwd
    configParser.read(configFilePath)

    return configParser
