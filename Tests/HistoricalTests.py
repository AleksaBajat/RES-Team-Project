import unittest
import sys
from unittest.mock import MagicMock

sys.path.append('../')
from Historical.Historical import *

from Model.DataSample import DataSample
from Model.Address import Address


class TestHistorical(unittest.TestCase):
    def test_sql_query(self):
        mock_address = Address("Serbia","Novi Sad", "Dusana Danilovica", 24)
        mock_data = DataSample(1,30,1,mock_address)
        result = create_sql_write_query(mock_data)
        self.assertEqual(result, f'''INSERT INTO meterReadings VALUES(1,1,30,'Serbia','Novi Sad','Dusana Danilovica',24,'June')''')

    def test_receive_data(self):
        mock_connect = MagicMock(socket.socket)
        mock_connect.recv = MagicMock(return_value=pickle.dumps("SUCCESS"))

        self.assertEqual("SUCCESS", receive_data(mock_connect))

        temp = DataSample(1, 2, 3, Address(1, 2, 3, 4))
        mock_connect.recv = MagicMock(return_value=pickle.dumps(temp))

        self.assertEqual(temp, receive_data(mock_connect))

    def test_create_listener(self):
        mock_socket = MagicMock(socket.socket)
        mock_socket.accept = MagicMock(return_value=(1, 2))

        self.assertEqual((1, 2), create_listener(mock_socket))


if __name__ == '__main__':
    unittest.main()