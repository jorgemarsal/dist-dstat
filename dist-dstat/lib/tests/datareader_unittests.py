import unittest
from constants import *
from datareader import *

class TestDataReader(unittest.TestCase):
    def test1(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        dr = DataReader('%s/../data/dstat.csv' %cwd)
        self.assertEqual(dr.get_col(Name2Col.CPU_USR), [TODO])
        self.assertEqual(dr.get_col(Name2Col.NET_RECV), [TODO])
