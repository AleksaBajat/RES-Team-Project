from random import sample
import sys
sys.path.append('../')

import json
import socket
from _thread import *
import pickle
from Model.DataSample import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 10000

SendHost = "127.0.0.1"
SendPort = 20000

    

def receive_data(connection):
    data = connection.recv(1024)
    sample = pickle.loads(data)
    print(str(sample))
    return sample


def send_data(sample, sendHost, sendPort):
    s = get_socket()                            # sending towards DumpBufer
    try:
        s.connect((sendHost, sendPort))
        s.send(pickle.dumps(sample))
        value = s.recv(1024)
        value = pickle.loads(value)
        print(value)
        
    except Exception as e:
        print(e)
    finally:
        s.close()
        return value

def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def multi_threaded_connection(connection):
    sample = receive_data(connection)
    return_message = send_data(sample, SendHost, SendPort)
    connection.send(pickle.dumps(return_message))                    # sending return value back
    connection.close()


def create_listener(s):
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    return (conn, addr)

def start_service():
    s = get_socket()
    s.bind((ReceiveHost, ReceivePort))
    while(True):
        conn, addr = create_listener(s)
        start_new_thread(multi_threaded_connection, (conn, ))
            

if __name__ == '__main__':
    print("Writer started:")
    start_service()
