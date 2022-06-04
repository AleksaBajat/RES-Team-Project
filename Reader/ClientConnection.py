from optparse import Option
from sqlite3 import paramstyle
import string
from CreateReply import *
import sys
import codecs
import string
sys.path.append('../')

import json
import socket
from _thread import *

from Model.DataSample import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 40000

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
            reply=getReply(option,parameter)
            

            conn.sendall(str(reply).encode("utf-8"))
        
      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHost, ReceivePort))
    while(True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn, ))
        

