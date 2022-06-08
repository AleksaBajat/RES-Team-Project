import sys
sys.path.append('../')

import unittest
from Writer.Writer import *
from Model.DataSample import *
from Model.Address import *


ReceiveHost = "127.0.0.1" 
ReceivePort = 10000


class TestWriter(unittest.TestCase):    

    def test_send(self):
        s = DataSample(1, 1000, 1, Address('Serbia', "Novi Sad", 'Bulevar Oslobodjenja', 12))
        self.assertEqual(sendData(s, ReceiveHost, ReceivePort), s)
        
        s = DataSample(1324234, 1000, 1, Address('Serbaaaaaaaaaaaaaaaaaaaia', "Novi Saaaaaaaaaaaaaaaaaaaaaad", 'Bulevaaaaaaaaaaaaaaar Oslobodjenja', 12))
        self.assertEqual(sendData(s, ReceiveHost, ReceivePort), s)

        s = DataSample(1, 1000, 1, Address(1, 1, 1, 1))
        self.assertEqual(sendData(s, ReceiveHost, ReceivePort), s)

        s = DataSample(0, 0, 0, Address(1, 1, 1, 1))
        self.assertEqual(sendData(s, ReceiveHost, ReceivePort), s)

        self.assertEqual(sendData("SUCCES", ReceiveHost, ReceivePort), "SUCCES")
        self.assertEqual(sendData("ERROR", ReceiveHost, ReceivePort), "ERROR")
        self.assertEqual(sendData("   ", ReceiveHost, ReceivePort), "   ")
        
        s = DataSample(1, 1000, 1, Address('Serbia', "Novi Sad", 'Bulevar Oslobodjenja', 12))
        s2 = DataSample(1, 1000, 1, Address('Serbia', "Novi S1ad", 'Bulevar Oslobodjenja', 12))
        self.assertNotEqual(sendData(s, ReceiveHost, ReceivePort), s2)

        s = DataSample(1, 100, 1, Address('Serbia', "Novi Sad", 'Bulevar Oslobodjenja', 12))
        s2 = DataSample(1, 1000, 1, Address('Serbia', "Novi Sad", 'Bulevar Oslobodjenja', 12))
        self.assertNotEqual(sendData(s, ReceiveHost, ReceivePort), s2)

    def test_receive(self):
        pass