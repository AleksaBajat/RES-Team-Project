from audioop import mul
import sys

sys.path.append('../')

import unittest
from unittest.mock import MagicMock, patch
from Writer.main import *
from Model.DataSample import *
from Model.Address import *



class TestWriter(unittest.TestCase):

    @patch('Writer.main.socket.socket')
    def test_send_data(self, mock_get_socket):

        self.assertEqual("SUCCESS", send_data("", 123, 123))
    
    @patch('Writer.main.socket.socket')
    def test_send_exception(self, mock_get_socket):
        mock_socket = MagicMock()
        mock_socket.connect.side_effect = Exception('Fail')
        mock_get_socket.return_value = mock_socket
       
        self.assertEqual('ERROR', send_data("SUCCESS", 123, 123))

    def test_receive_data(self):
        mock_connect = MagicMock(socket.socket)
        mock_connect.recv = MagicMock(return_value = pickle.dumps("SUCCESS"))
        
        self.assertEqual("SUCCESS", receive_data(mock_connect))

        temp = DataSample(1, 2, 3, Address(1, 2, 3, 4))
        mock_connect.recv = MagicMock(return_value = pickle.dumps(temp))
        self.assertEqual(temp, receive_data(mock_connect))
        
        mock_connect.recv = None
        self.assertEqual('ERROR', receive_data(mock_connect))

    def test_create_listener(self):
        mock_socket = MagicMock(socket.socket)
        mock_socket.accept = MagicMock(return_value = (1, 2))

        self.assertEqual((1, 2), create_listener(mock_socket))
    
    @patch('Writer.main.socket.socket')
    def test_start_service(self, mock_get_socket):
        mock_get_socket = None
        self.assertEqual('ERROR', start_service())

    @patch('Writer.main.receive_data')
    def test_multi_threaded_connection(self, mock_recv):
        self.assertRaises(Exception, multi_threaded_connection, None)
        self.assertEqual('SUCCESS', multi_threaded_connection(MagicMock()))

        mock_conn = MagicMock()
        mock_conn.send = None
        self.assertEqual('ERROR', multi_threaded_connection(mock_conn))


if __name__ == '__main__':
    unittest.main()
