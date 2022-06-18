import sys
import pickle
import json
import socket
sys.path.append('../')

from CreateQuery import *
from _thread import *


ReceiveHost = "127.0.0.1" 
ReceivePort = 40000

HistoricalHost="127.0.0.1"
HistoricalPort=60000
    
def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def get_from_historical(string):
    sock=get_socket()
    server_address = (HistoricalHost, HistoricalPort)
    print("connecting to Historical on address " + str(HistoricalHost)+":"+str(HistoricalPort))
    sock.connect(server_address)

    try:
        sock.send(pickle.dumps(string.encode("utf-8")))
        reply = sock.recv(1024)

    except Exception as e:
        print(e)
        return "ERROR"
    finally:
        print('closing socket for Historical')
        sock.close()
        return reply


def get_params(data):
    option=data.split(',')[0]
    parameter=data.split(',')[1]
    parameter=parameter[1:]
    return option,parameter

def multi_threaded_connection(connection): 
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            data=(data.decode("utf-8"))                                                                     
            option,parameter=get_params(data)
            string=get_query(option,parameter)
            reply=get_from_historical(string)
            connection.sendall(reply)
        
      
def start_reader():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ReceiveHost, ReceivePort))
        print("Reader started!")
        while(True):
            s.listen()
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            start_new_thread(multi_threaded_connection, (conn, ))

if __name__ == '__main__':
    start_reader()
