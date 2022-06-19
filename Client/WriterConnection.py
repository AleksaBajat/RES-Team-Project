import socket
import sys
sys.path.append('../')
from Model.DataSample import DataSample
from Model.Address import Address
import pickle

SendHost = "127.0.0.1"
SendPort = 10000

def get_input():
    return input()

def get_meter_id():
    x = get_input()
    try:
        if x.isnumeric():
            return x
        else:
            raise TypeError
    except TypeError:
        print("MeterId must be an int")
        return "Error"

def get_user_id():
    x = get_input()
    try:
        if x.isnumeric():
            return x
        else:
            raise TypeError
    except TypeError:
        print("UserId must be an int")
        return "Error"

def get_consumption():
    x = get_input()
    try:
        if x.isnumeric():
            return x
        else:
            raise TypeError
    except TypeError:
        print("Consumption must be an int")
        return "Error"

def get_country():
    x = get_input()
    try:
        if x.isalpha() and len(x)<60:
            return x
        else:
            raise RuntimeError
    except RuntimeError:
        print("Country has only letters. Max length - 60 letters")
        return "Error"

def get_city():
    x = get_input()
    try:
        if x.isalpha():
            return x
        else:
            raise RuntimeError
    except RuntimeError:
        print("City has only letters.")
        return "Error"

def get_street():
    x = get_input()
    try:
        if x.isalpha():
            return x
        else:
            raise RuntimeError
    except RuntimeError:
        print("Street has only letters.")
        return "Error"  
def get_street_number():
    x = get_input()
    try:
        if x.isnumeric():
            return x
        else:
            raise RuntimeError
    except RuntimeError:
        print("Street number must be an int")
        return "Error"

def get_sample():
    print("Insert meter ID : ")
    meter_id = get_meter_id()
    print("Insert user ID :")
    user_id = get_user_id()
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

    if(meter_id=="Error" or user_id=="Error" or consumption=="Error" or country=="Error" or city=="Error" or street=="Error" or street_number=="Error"):
        raise Exception("Values not entered corectly")

    address = Address(country,city,street,street_number)

    sample = DataSample(meter_id, consumption, user_id, address)
    
    return sample


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
        print(e)
        print('closing socket')
        sock.close()
        
        