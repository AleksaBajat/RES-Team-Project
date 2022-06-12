import json
import socket
import sys
sys.path.append('../')
from Model.DataSample import *
from Model.Address import *
import pickle


def getMessage():
    print("Insert meter ID : ")
    meterId =input()
    print("Insert user ID :")
    userId = input()
    print("Insert meter consumption: ")
    consumption = input()
    print("Insert country: ")
    country = input()
    print("Insert city: ")
    city = input()
    print("Insert street: ")
    street = input()
    print("Insert street number: ")
    street_number = input()

    address = Address(country,city,street,street_number)

    message = DataSample(meterId, consumption, userId, address)
    
    return message

def connectToWriter():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ("127.0.0.1", 10000)
    print("connecting to " + str(server_address))
    sock.connect(server_address)

    try:   
        message = getMessage()
        sock.send(pickle.dumps(message))
           
    except Exception as e:
        print(e)
    finally:
        print('closing socket')
        sock.close()