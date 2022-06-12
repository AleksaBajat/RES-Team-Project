import sys
sys.path.append('../')
from Reader.CreateQuery import *
import unittest


class TestCreateQuery(unittest.TestCase):
    def test_get_query(self):
        self.assertEqual(get_query("1",0), "SELECT * FROM meterReadings")
        self.assertEqual(get_query("2","June"), "SELECT * FROM meterReadings WHERE month = 'June'")
        self.assertEqual(get_query("3",123), "SELECT * FROM meterReadings WHERE user_id = 123")
        self.assertEqual(get_query("4","Becej"), "SELECT * FROM meterReadings WHERE city = 'Becej'")
        self.assertEqual(get_query("5",5000), "SELECT * FROM meterReadings WHERE consumption >= 5000")
        self.assertEqual(get_query("6",5000), "SELECT * FROM meterReadings WHERE consumption < 5000")
        

if __name__ == '__main__':
    unittest.main()

