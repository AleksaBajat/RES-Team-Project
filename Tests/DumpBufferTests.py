import sys
import unittest

sys.path.append('../')

from unittest.mock import MagicMock

from Model.Address import Address

from DumpBuffer.DumpBuffer import *



class TestDumpBuffer(unittest.TestCase):

    def test_receive(self):
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