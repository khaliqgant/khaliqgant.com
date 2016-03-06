import os
import sys
import unittest


import keyHelper
pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import foursquare


class FoursquareTest(unittest.TestCase):

    def setUp(self):
        pass

    """
        Make sure what we send to the template has the write keys
        and is of the right type
    """
    def test_checkins(self):
        KEY = keyHelper.grabKey('foursquare')
        checkins = foursquare.retrieve(KEY)
        self.assertIn('data', checkins)
        self.assertIn('count', checkins)
        self.assertIsInstance(checkins['data'], list)
        self.assertIsInstance(checkins['count'], int)

    """ Ensure returns an int """
    def test_count(self):
        KEY = keyHelper.grabKey('foursquare')
        count = foursquare.todaysCount(KEY)
        self.assertEqual(type(1), type(count))


if __name__ == "__main__":
    unittest.main()
