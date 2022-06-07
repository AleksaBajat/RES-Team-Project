import sys
sys.path.append('../')

import unittest
from Writer.Writer import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 10000

class TestWriter(unittest.TestCase):    

    def test_send(self):
        self.assertEqual(sendData("hello", ReceiveHost, ReceivePort), "hello")
        self.assertEqual(sendData("1", ReceiveHost, ReceivePort), "1")
        self.assertEqual(sendData(" ", ReceiveHost, ReceivePort), " ")
        self.assertEqual(sendData("", ReceiveHost, ReceivePort), "")
        self.assertEqual(sendData("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", ReceiveHost, ReceivePort), "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        self.assertEqual(sendData("]asd2K!@)32", ReceiveHost, ReceivePort), "]asd2K!@)32")
        self.assertEqual(sendData("jgioja;idj sf;i gdsauh aij39 dgsjg dsaij23 dsgna", ReceiveHost, ReceivePort), "jgioja;idj sf;i gdsauh aij39 dgsjg dsaij23 dsgna")


