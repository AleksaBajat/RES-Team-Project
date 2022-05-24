import socket
from _thread import *

HOST = "127.0.0.1" 
PORT = 10101

def multi_threaded_connection(connection):  
    with connection:
        while True:
            data = conn.recv(1024)          #Trenutno prima samo stringove, tj bytes.
            if not data:
                break
            print(data)   
            


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while(True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn, ))
        

