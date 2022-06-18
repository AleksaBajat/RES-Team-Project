from socket import socket
import sys
from unittest import mock
from unittest.mock import  MagicMock, patch
sys.path.append('../')
from Reader.CreateQuery import *
from Reader.main import *
import unittest


class TestCreateQuery(unittest.TestCase):
    def test_get_query(self):
        self.assertEqual(get_query("1",0), "SELECT * FROM meterReadings")
        self.assertEqual(get_query("2","June"), "SELECT * FROM meterReadings WHERE month = 'June'")
        self.assertEqual(get_query("3",123), "SELECT * FROM meterReadings WHERE user_id = 123")
        self.assertEqual(get_query("4","Becej"), "SELECT * FROM meterReadings WHERE city = 'Becej'")
        self.assertEqual(get_query("5",5000), "SELECT * FROM meterReadings WHERE consumption >= 5000")
        self.assertEqual(get_query("6",5000), "SELECT * FROM meterReadings WHERE consumption < 5000")


class TestReader(unittest.TestCase):
    
    def test_get_params(self):
        self.assertEqual(('1','0'),get_params("1, 0"))

    @patch('Reader.Reader.get_socket')
    def test_get_from_historical(self,mock_get_socket):
        mock_socket = MagicMock(socket.socket)
        mock_socket.recv = MagicMock(return_value = "aaa")
        mock_get_socket.return_value = mock_socket

        
        self.assertEqual(get_from_historical("bbb"),"aaa")

if __name__ == '__main__':
    unittest.main()

