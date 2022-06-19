import pickle
import socket
import sys
import unittest

from Model.DataSample import DataSample

sys.path.append('../')

from unittest.mock import MagicMock, patch
from Model.Address import Address

from DumpBuffer.main import receive_data
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

    @patch('Client.ReaderConnection.get_socket')
    def test_get_from_queue(self):
        mock_queue      = MagicMock(Queue)
        mock_queue.qsize= MagicMock(return_value=7)
        mock_queue.get  = MagicMock(return_value="sample")  

        mock_socket= MagicMock(socket.socket)
        mock_socket.send=MagicMock()

        self.assertEqual(True,get_from_queue(mock_queue))

        mock_queue.qsize=MagicMock(return_value=1)
        self.assertEqual(False,get_from_queue(mock_queue))

        self.assertEqual(False,get_from_queue(mock_queue))

if __name__ == '__main__':
    unittest.main()