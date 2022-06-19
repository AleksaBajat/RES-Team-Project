import sqlite3
import sys
import unittest
from unittest.mock import MagicMock, patch



sys.path.append('../')
from Historical.ConnectToDatabase import select_by_string
from Historical.main import *

from Model.DataSample import DataSample
from Model.Address import Address


class TestHistorical(unittest.TestCase):
    def test_sql_query(self):
        mock_address = Address("Serbia","Novi Sad", "Dusana Danilovica", 24)
        mock_data = DataSample(1,30,1,mock_address)
        result = create_sql_write_query(mock_data)
        self.assertEqual(result, f'''INSERT INTO meterReadings VALUES(1,1,30,'Serbia','Novi Sad','Dusana Danilovica',24,'June')''')
 
        mock_address = Address("","", "", 0)
        mock_data = DataSample(0,0,0,mock_address)
        result = create_sql_write_query(mock_data)
        self.assertEqual(result, f'''INSERT INTO meterReadings VALUES(0,0,0,'','','',0,'June')''')

    def test_receive_data(self):
        mock_connect = MagicMock(socket.socket)
        mock_connect.recv = MagicMock(return_value=pickle.dumps("SUCCESS"))
        self.assertEqual("SUCCESS", receive_data(mock_connect))

        temp = DataSample(1, 2, 3, Address(1, 2, 3, 4))
        mock_connect.recv = MagicMock(return_value=pickle.dumps(temp))
        self.assertEqual(temp, receive_data(mock_connect))

        mock_connect.recv.side_effect = RuntimeError()
        self.assertEqual('ERROR', receive_data(mock_connect))

    def test_create_listener(self):
        mock_socket = MagicMock(socket.socket)
        mock_socket.accept = MagicMock(return_value=(1, 2))

        self.assertEqual((1, 2), create_listener(mock_socket))

    @patch('Historical.main.open_connection_and_reply', return_value="")
    @patch('Historical.main.receive_data', return_value="some data".encode("utf-8"))
    def test_reader(self,mock_data,mock_receive):
        connection = MagicMock(socket.socket)
        self.assertEqual(False,reader_connection(connection))
        mock_receive.return_value = "something"
        self.assertEqual(True,reader_connection(connection))

    @patch('Historical.main.receive_data')
    @patch('Historical.main.send_sample_database', return_value='ERROR')
    def test_writer_connection(self, mock_send, mock_receive):
        mock_receive.return_value = ['one', 'two', 'three']
        mock_send.return_value = 'ERROR'
        mock_socket = MagicMock(socket.socket)
        self.assertEqual('ERROR', writer_connection(mock_socket))
        mock_send.return_value = 'SUCCESS'
        self.assertEqual('SUCCESS', writer_connection(mock_socket))

    @patch('Historical.main.create_sql_write_query')
    @patch('Historical.main.connect_to_database')
    def test_send_sample_database(self,mock_data, mock_sql):

        mock_data.return_value = None
        self.assertRaises(Exception ,send_sample_database)
        self.assertEqual('ERROR', send_sample_database(MagicMock()))

        mock_data.return_value = MagicMock()
        self.assertEqual('SUCCESS', send_sample_database(MagicMock()))


    @patch('Historical.main.create_listener')
    @patch('Historical.main.get_socket')
    def test_listen(self, mock_get_socket, mock_listener):
        mock_listener.side_effect = RuntimeError()
        mock_socket = MagicMock()
        mock_socket.bind.execute.side_effect = RuntimeError("Fail")
        mock_get_socket.return_value = mock_socket
        mock_function = MagicMock()
        self.assertEqual('ERROR', listen('ip',123, mock_function))


class TestConnectToDataBase(unittest.TestCase):
    
    @patch('Historical.ConnectToDatabase.sqlite3')
    def test_connect_to_database(self, mock_connect):
        mock_connect.connect.return_value = 'conn'
        self.assertEqual('conn', connect_to_database('file'))
        self.assertNotEqual('wrong', connect_to_database('file'))

        mock_connect.connect.side_effect = Exception('Fail')
        self.assertEqual(None, connect_to_database('file'))
    
    def test_select_by_string(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = 'result'
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        self.assertEqual('result', select_by_string(mock_conn, ''))

        mock_conn.cursor.side_effect = RuntimeError()
        self.assertEqual('ERROR', select_by_string(mock_conn, ''))

    @patch('Historical.ConnectToDatabase.connect_to_database')
    @patch('Historical.ConnectToDatabase.select_by_string')
    def test_open_connection_and_reply(self, mock_select, mock_connect):
        mock_select.return_value = ['one', 'two', 'three']
        self.assertEqual('one\ntwo\nthree\n', open_connection_and_reply(''))


if __name__ == '__main__':
    unittest.main()