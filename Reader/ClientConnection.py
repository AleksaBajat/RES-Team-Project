from optparse import Option
from sqlite3 import paramstyle
from CreateReply import *
import sys
sys.path.append('../')

import json
import socket
from _thread import *

from Model.DataSample import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 40000

SendHost = "127.0.0.1"
SendPort = 20000


def multi_threaded_connection(connection): 
    receiveData = [] 
    with connection:
        while True:
            data = conn.recv(100)
            if not data:
                break
            receiveData.append(data)                                                          
            receiveData=str(receiveData)
            option=receiveData.split(',')[0]
            parameter=receiveData.split(',')[1]
            print(option+"  "+parameter)
            reply=getReply(option,parameter)
            #conn.sendall(reply)
        
      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHost, ReceivePort))
    while(True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn, ))
        

