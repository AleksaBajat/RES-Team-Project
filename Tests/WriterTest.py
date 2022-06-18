from csv import writer
from logging import exception
import sys
from venv import create
sys.path.append('../')

import unittest
from unittest.mock import MagicMock, patch
from Writer.main import *
from Model.DataSample import *
from Model.Address import *



class test_Writer(unittest.TestCase):
    @patch('Writer.main.get_socket')
    def test_send_data(self, mock_get_socket):
        mock_socket = MagicMock(socket.socket)
        mock_socket.recv = MagicMock(return_value = pickle.dumps("SUCCESS"))
        mock_get_socket.return_value = mock_socket

        self.assertEqual("SUCCESS", send_data("SUCCESS", 123, 123))
    
    @patch('Writer.main.get_socket')
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
    
    @patch('Writer.main.get_socket')
    def test_start_service(self, mock_get_socket):
        mock_get_socket = None
        self.assertEqual('ERROR', start_service())

if __name__ == '__main__':
    unittest.main()
