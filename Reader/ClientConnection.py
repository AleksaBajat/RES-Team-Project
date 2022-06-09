from optparse import Option
from sqlite3 import paramstyle
from CreateQuery import *
import sys
import pickle

sys.path.append('../')

import json
import socket
from _thread import *

from Model.DataSample import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 40000

HistoricalHost="127.0.0.1"
HistoricalPort=30000

def getFromHistorical(string):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HistoricalHost, HistoricalPort)
    print("connecting to Historical on address " + str(HistoricalHost)+":"+str(HistoricalPort))
    sock.connect(server_address)

    try:
        sock.send(pickle.dumps(string.encode("utf-8")))
        reply = sock.recv(1024)
        return reply

    except Exception as e:
        print(e)
    finally:
        print('closing socet for Historical')
        sock.close()


def multi_threaded_connection(connection): 
    with connection:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data=(data.decode("utf-8"))                                                          
            option=data.split(',')[0]
            parameter=data.split(',')[1]
            parameter=parameter[1:]
            string=getQuery(option,parameter)
            
            reply=getFromHistorical(string)

            conn.sendall(reply)
        
      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHost, ReceivePort))
    print("Reader started")
    while(True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn, ))
        

