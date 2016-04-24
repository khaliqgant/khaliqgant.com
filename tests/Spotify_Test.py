import os
import sys
import unittest

pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import spotify


class SpotifyTest(unittest.TestCase):

    def setUp(self):
        pass

    """ Make sure empty lastfm arrays don't crash my site """
    def test_emptyLastfm(self):
        self.assertEqual([[], []],  spotify.lookup([[], []]))

    """ Make sure a non match song won't ruin EVERYTHING """
    def test_nonMatch(self):
        example = [{"artist": {"#text": "foo"}, "name": "bar"}]
        nowPlaying = {"artist": {"#text": "foo"}, "name": "bar"}
        lastfms = [example, nowPlaying]
        empty = spotify.lookup(lastfms)
        self.assertEqual(lastfms, empty)

    """ Make sure weird special characters won't mess with the search """
    def test_weirdChars(self):
        example = [{"artist": {"#text": "foo*Y#&$#Y*"}, "name": "bar@()SD()#"}]
        lastfms = [example, []]
        empty = spotify.lookup(lastfms)
        self.assertEqual(lastfms, empty)


if __name__ == "__main__":
    unittest.main()
