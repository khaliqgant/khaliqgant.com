import os
import sys
import unittest

import keyHelper

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import rescuetime

env = os.environ


class RescueTimeTest(unittest.TestCase):

    def setUp(self):
        pass

    """ Make sure the expected keys are there """
    def test_productivityResponse(self):
        KEY = keyHelper.grabKey('rescuetime')
        productivity = rescuetime.todaysProductivity(KEY, True)
        self.assertEqual(
            productivity['row_headers'][1], "Time Spent (seconds)"
        )
        self.assertEqual('row_headers' in productivity, True)
        self.assertEqual('rows' in productivity, True)

    """
        Make sure the response is formatted to what will be outputted in the
        template
    """
    def test_todaysProductivity(self):
        KEY = keyHelper.grabKey('rescuetime')
        productivity = rescuetime.todaysProductivity(KEY)
        self.assertEqual(type(productivity), type([]))


if __name__ == "__main__":
    unittest.main()