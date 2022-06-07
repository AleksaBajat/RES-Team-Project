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
        data = conn.recv(1024)

        print(data)
        sample = pickle.loads(data)
        print(str(sample))        # radi provere

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                            # slanje ka Dump buffer-u
            try:
                s.connect((SendHost, SendPort))
                s.send(pickle.dumps(sample))
            except Exception as e:
                print(e)
            finally:
                s.close()
                

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHost, ReceivePort))
    while(True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn, ))
        

