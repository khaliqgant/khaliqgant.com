import os
import sys
import unittest

import keyHelper

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import spotify


class SpotifyTest(unittest.TestCase):

    def setUp(self):
        pass

    """ Make sure empty lastfm arrays don't crash my site """
    def test_emptyLastfm(self):


    """ Make sure a non match song won't ruin EVERYTHING """
    def test_nonMatch(self):


    """ Make sure weird special characters won't mess with the search """
    def test_weirdChars(self):


if __name__ == "__main__":
    unittest.main()
