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

def multi_threaded_connection(connection):
    with connection:
        data = connection.recv(1024)

        sample = pickle.loads(data)
        print(str(sample))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                            # sending towards DumpBufer
            try:
                s.connect((SendHost, SendPort))
                s.send(pickle.dumps(sample))
                value = s.recv(1024)
                value = pickle.loads(value)
                print(value)
                connection.send(pickle.dumps(value))                    # sending return value back

            except Exception as e:
                print(e)
            finally:
                s.close()
                

def createListener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ReceiveHost, ReceivePort))
        while(True):
            s.listen()
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            start_new_thread(multi_threaded_connection, (conn, ))


print("Writer started:")
createListener()