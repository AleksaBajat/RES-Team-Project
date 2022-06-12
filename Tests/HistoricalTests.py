import unittest
import sys
import sqlite3
from unittest.mock import MagicMock, patch, Mock

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

    @patch('Historical.Historical.open_connection_and_reply', return_value="")
    @patch('Historical.Historical.receive_data', return_value="some data".encode("utf-8"))
    def test_reader(self,mock_data,mock_receive):
        connection = MagicMock(socket.socket)
        self.assertEqual(False,reader_connection(connection))
        mock_receive.return_value = "something"
        self.assertEqual(True,reader_connection(connection))


    @patch('Historical.Historical.connect_to_database')
    def test_send_sample_database(self,mock_data):
        mock_connection = MagicMock(sqlite3.Connection)
        mock_cursor = MagicMock(sqlite3.Cursor)
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.execute.return_value = Exception("Fail") ## NE RADI

        mock_data.return_value = mock_connection
        self.assertEqual("ERROR",send_sample_database(MagicMock()))

if __name__ == '__main__':
    unittest.main()