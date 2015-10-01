import time
import unittest
from dstatcontroller import *

class TestDstatController(unittest.TestCase):
    def test1(self):
        dc = DstatController(['localhost'])
        dc.start_dstat()
        time.sleep(5)
        dc.stop_dstat()
        self.assertEqual(dc.fetch_csvs(), ['/tmp/dstatout/localhost/tmp/dstat.csv'])



