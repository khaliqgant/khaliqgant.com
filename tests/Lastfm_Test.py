import os
import sys
import unittest

import keyHelper

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import lastfm
KEY = keyHelper.grabKey('lastfm', 'LASTFM_KEY')
SECRET = keyHelper.grabKey('lastfm', 'LASTFM_SECRET', 'secret')


class LastfmTest(unittest.TestCase):

    def setUp(self):
        pass

    """ Make sure count returns an int """
    def test_count(self):
        count = lastfm.todaysCount(KEY)
        self.assertIsInstance(count, int)

    """ Ensure response has proper props """
    def test_listens(self):
        listens = lastfm.retrieve(KEY)
        self.assertIsInstance(listens, list)

    def test_artists(self):
        artists = lastfm.topArtists(KEY, SECRET, '1month')
        self.assertIsInstance(artists, dict)
        self.assertIsInstance(artists['artist'], list)


if __name__ == "__main__":
    unittest.main()
