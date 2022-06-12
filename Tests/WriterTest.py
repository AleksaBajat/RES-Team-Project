from csv import writer
from logging import exception
import sys
from venv import create
sys.path.append('../')

import unittest
from unittest.mock import MagicMock, patch
from Writer.Writer import *
from Model.DataSample import *
from Model.Address import *


ReceiveHost = "127.0.0.1" 
ReceivePort = 10000

SendHost = "127.0.0.1" 
SendPort = 20000

ListenerHost = "127.0.0.1"
ListenerPort = 30000

class test_send_data(unittest.TestCase):
    @patch('Writer.Writer.get_socket')
    def test_send(self, mock_get_socket):
        mock_socket = MagicMock(socket.socket)
        mock_socket.recv = MagicMock(return_value = pickle.dumps("SUCCESS"))
        mock_get_socket.return_value = mock_socket

        self.assertEqual("SUCCESS", send_data("SUCCESS", ListenerHost, ListenerPort))
    
    @patch('Writer.Writer.get_socket')
    def test_send_exception(self, mock_get_socket):
        mock_socket = MagicMock(socket.socket)
        mock_socket.recv = MagicMock(return_value = pickle.dumps("SUCCESS"))
        mock_socket.connect('fsd', 84214)
        mock_get_socket.return_value = mock_socket
        self.assertRaises(Exception, send_data("SUCCESS", ListenerHost, ListenerPort))


class test_receive(unittest.TestCase):

    def test_receive(self):
        mock_connect = MagicMock(socket.socket)
        mock_connect.recv = MagicMock(return_value = pickle.dumps("SUCCESS"))
        
        self.assertEqual("SUCCESS", receive_data(mock_connect))


class test_create_listener(unittest.TestCase):

    def test_create_listener(self):
        mock_socket = MagicMock(socket.socket)
        mock_socket.accept = MagicMock(return_value = (1, 2))

        self.assertEqual((1, 2), create_listener(mock_socket))