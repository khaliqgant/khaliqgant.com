import os
import sys
import unittest


pwd = os.path.dirname(os.path.abspath(__file__))
# put apis in package path
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import rescuetime
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../config')))
import auth


class RescueTimeTest(unittest.TestCase):

    def setUp(self):
        pass

    """ Make sure the expected keys are there """
    def test_todaysProductivity(self):
        configParser = auth.grab()
        r_key = configParser.get('rescuetime', 'key')
        productivity = rescuetime.todaysProductivity(r_key, True)
        self.assertEqual(
            productivity['row_headers'][1], "Time Spent (seconds)"
        )
        self.assertEqual('row_headers' in productivity, True)
        self.assertEqual('rows' in productivity, True)
        assert 1 == 1


if __name__ == "__main__":
    unittest.main()
