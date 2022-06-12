import unittest
import sys
from unittest.mock import MagicMock, Mock, patch
sys.path.append('../')
from Client.ReaderConnection import *
from Client.WriterConnection import *
from Model.DataSample import *
from Model.Address import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 10000

class TestWriterConnection(unittest.TestCase):

    @patch('builtins.input', return_value=123)
    def test_getMeterId(self, input):
        self.assertEqual(get_meterId(), 123)

    @patch('builtins.input', return_value=321)
    def test_getUserId(self, input):
        self.assertEqual(get_userId(), 321)
    
    @patch('builtins.input', return_value=5000)
    def test_getConsumption(self, input):
        self.assertEqual(get_consumption(), 5000)

    @patch('builtins.input', return_value='Serbia')
    def test_getCountry(self, input):
        self.assertEqual(get_country(), 'Serbia')

    @patch('builtins.input', return_value='Becej')
    def test_getCity(self, input):
        self.assertEqual(get_city(), 'Becej')

    @patch('builtins.input', return_value='Zelena')
    def test_getStreet(self, input):
        self.assertEqual(get_street(), 'Zelena')

    @patch('builtins.input', return_value=47)
    def test_getStreetNumber(self, input):
        self.assertEqual(get_street_number(), 47)
#-----------------------------------------------------Fails
    @patch('builtins.input', return_value='aaa')
    def test_getMeterId2(self, input):
        self.assertRaises(TypeError,get_meterId())

    @patch('builtins.input', return_value='1da')
    def test_getUserId2(self, input):
        self.assertRaises(TypeError,get_userId())
    
    @patch('builtins.input', return_value='d')
    def test_getConsumption2(self, input):
        self.assertRaises(TypeError,get_consumption())

    @patch('builtins.input', return_value=3)
    def test_getCountry2(self, input):
        self.assertRaises(Exception,get_country())

    @patch('builtins.input', return_value=1)
    def test_getCity2(self, input):
        self.assertRaises(Exception,get_city())

    @patch('builtins.input', return_value=1)
    def test_getStreet2(self, input):
        self.assertRaises(Exception,get_street())

    @patch('builtins.input', return_value='a')
    def test_getStreetNumber2(self, input):
        self.assertRaises(TypeError,get_street_number())

    @patch('Client.WriterConnection.get_street_number',return_value=15)
    @patch('Client.WriterConnection.get_street',return_value="Bulevar")
    @patch('Client.WriterConnection.get_city',return_value="Novi Sad")
    @patch('Client.WriterConnection.get_country',return_value="Serbia")
    @patch('Client.WriterConnection.get_consumption',return_value=5000)
    @patch('Client.WriterConnection.get_userId',return_value=321)
    @patch('Client.WriterConnection.get_meterId',return_value=123)
    def test_get_message(self, mock_meterId,mock_userId,mock_consumption,mock_country,mock_city,mock_street,mock_streetNumber):   
        temp=DataSample(123,5000,321,Address("Serbia","Novi Sad","Bulevar",15))
        temp2=get_message()
       
        self.assertEqual(temp,get_message())



   
if __name__ == '__main__':
    unittest.main()