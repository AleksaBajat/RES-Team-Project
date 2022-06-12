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

    

def receiveData(connection):
    data = connection.recv(1024)
    sample = pickle.loads(data)
    print(str(sample))
    return sample


def sendData(sample, sendHost, sendPort):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                            # sending towards DumpBufer
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


def multi_threaded_connection(connection):
    sample = receiveData(connection)
    return_message = sendData(sample, SendHost, SendPort)
    connection.send(pickle.dumps(return_message))                    # sending return value back
    connection.close()


def createListener(s):
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    return (conn, addr)

def startService():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ReceiveHost, ReceivePort))
        while(True):
            conn, addr = createListener(s)
            start_new_thread(multi_threaded_connection, (conn, ))
            

if __name__ == '__main__':
    print("Writer started:")
    startService()
