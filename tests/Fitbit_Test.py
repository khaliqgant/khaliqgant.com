import os
import sys
import json
import unittest

# put apis in package path
pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../apis')))
import fitbit


class FitbitTest(unittest.TestCase):

    def setUp(self):
        pass

    def get_sleep_fixture(self):
        with open('fixtures/fitbit_sleep.json', 'r') as sleep:
            data = json.load(sleep)
            return data

    """
        Grab efficiency of Fitbit Sleep
    """
    def test_sleep(self):
        data = self.get_sleep_fixture()
        efficiency = fitbit.computeEfficiency(data)
        self.assertIsInstance(efficiency, float)


if __name__ == "__main__":
    unittest.main()
