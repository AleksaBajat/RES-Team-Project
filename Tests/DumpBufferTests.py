from asyncio import start_server
from inspect import getframeinfo
import pickle
import socket
import sys
import unittest
sys.path.append('../')

from unittest.mock import MagicMock, patch
from Model.Address import Address
from Model.DataSample import DataSample

from DumpBuffer.main import multi_threaded_connection, receive_data, start_service
from DumpBuffer.main import create_listener
from DumpBuffer.main import get_from_queue
from DumpBuffer.main import Queue



class TestDumpBuffer(unittest.TestCase):

    def test_receive(self):
        mock_connect = MagicMock(socket.socket)

        #test message
        mock_connect.recv = MagicMock(return_value=pickle.dumps("SUCCESS"))
        self.assertEqual("SUCCESS", receive_data(mock_connect))

        #test DataSample
        temp = DataSample(1, 2, 3, Address(1, 2, 3, 4))
        mock_connect.recv = MagicMock(return_value=pickle.dumps(temp))
        self.assertEqual(temp, receive_data(mock_connect))

        #test None value
        mock_connect.recv = MagicMock(return_value=None)
        self.assertRaises(Exception, receive_data(mock_connect))



    def test_create_listener(self):
        mock_socket = MagicMock(socket.socket)
        mock_socket.accept = MagicMock(return_value=(1, 2))

        self.assertEqual((1, 2), create_listener(mock_socket))


    @patch('Client.ReaderConnection.socket.socket')
    def test_get_from_queue(self, mock_s):
        mock_queue = MagicMock(Queue)
        mock_connect = MagicMock()
        mock_connect.connect = MagicMock()
        mock_s.return_value = mock_connect
        mock_queue.get.return_value = 1
        mock_queue.qsize.return_value = 10
        self.assertEqual(True,get_from_queue(mock_queue))

        mock_queue.qsize=MagicMock(return_value=1)
        self.assertEqual(False,get_from_queue(mock_queue))

        mock_queue.get = None
        mock_queue.qsize=MagicMock(return_value=10)
        self.assertRaises(Exception, get_from_queue)
        self.assertEqual('ERROR', get_from_queue(mock_queue))

    @patch('Client.ReaderConnection.socket.socket')
    def test_start_service(self, mock_socket):
        mock_socket = None
        self.assertRaises(Exception, start_server)
        self.assertEqual('ERROR', start_service(Queue(0)))

    @patch('Client.ReaderConnection.receive_data')
    def test_multi_threaded_connection(self, mock_receive):
        mock_receive = None
        self.assertRaises(Exception, multi_threaded_connection)
        self.assertEqual('ERROR', multi_threaded_connection(MagicMock()))


if __name__ == '__main__':
    unittest.main()