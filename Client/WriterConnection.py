import json
from logging import raiseExceptions
import socket
import sys
from typing import Type
sys.path.append('../')
from Model.DataSample import *
from Model.Address import *
import pickle

SendHost = "127.0.0.1"
SendPort = 10000

def get_input():
    return input()

def get_meterId():
    x = get_input()
    try:
        if(isinstance(x,int)):
            return x
        else:
            raise TypeError
    except:
        print("MeterId must be an int")

def get_userId():
    x = get_input()
    try:
        if(isinstance(x,int)):
            return x
        else:
            raise TypeError
    except:
        print("UserId must be an int")

def get_consumption():
    x = get_input()
    try:
        if(isinstance(x,int)):
            return x
        else:
            raise TypeError
    except:
        print("Consumption must be an int")

def get_country():
    x = get_input()
    try:
        if(x.isalpha() and len(x)<60):
            return x
        else:
            raise Exception
    except Exception:
        print("Country has only letters. Max length - 60 letters")

def get_city():
    x = get_input()
    try:
        if(x.isalpha()):
            return x
        else:
            raise Exception
    except Exception:
        print("City has only letters.")
    

def get_street():
    x = get_input()
    try:
        if(x.isalpha()):
            return x
        else:
            raise Exception
    except Exception:
        print("Street has only letters.")

def get_street_number():
    x = get_input()
    try:
        if(isinstance(x,int)):
            return x
        else:
            raise TypeError
    except:
        print("Street number must be an int")


def get_message():
    print("Insert meter ID : ")
    meterId = get_meterId()
    print("Insert user ID :")
    userId = get_userId()
    print("Insert meter consumption: ")
    consumption = get_consumption()
    print("Insert country: ")
    country = get_country()
    print("Insert city: ")
    city = get_city()
    print("Insert street: ")
    street = get_street()
    print("Insert street number:")
    street_number = get_street_number()

    address = Address(country,city,street,street_number)

    message = DataSample(meterId, consumption, userId, address)
    
    return message


def connect_to_writer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:   
        sample = get_sample()
        server_address = (SendHost, SendPort)
        print("connecting to " + str(server_address))
sock.connect(server_address)  
        sock.send(pickle.dumps(sample))
        print('closing socket')
        sock.close()
    except Exception as e:
        print()
        print('closing socket')
        sock.close()
        
        