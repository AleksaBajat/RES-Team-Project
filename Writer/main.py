import sys
sys.path.append('../')

import socket
from _thread import *
import pickle

ReceiveHost = "127.0.0.1" 
ReceivePort = 10000

SendHost = "127.0.0.1"
SendPort = 20000

    

def receive_data(connection):
    try:
        data = connection.recv(1024)
        sample = pickle.loads(data)
        print(str(sample))
        return sample
    except Exception as e:
        return 'ERROR'


def send_data(sample, send_host, send_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((send_host, send_port))
        s.send(pickle.dumps(sample))
        message = 'SUCCESS'
        return message
    except Exception as e:
        print(e)
        message = 'ERROR'
        return message
    finally:
        s.close()

def multi_threaded_connection(connection):
    try:
        sample = receive_data(connection)
        return_message = send_data(sample, SendHost, SendPort)
        connection.send(pickle.dumps(return_message))                    # sending return value back
        connection.close()
        return 'SUCCESS'
    except Exception as e:
        connection.close()
        return 'ERROR'



def create_listener(s):
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    return conn, addr

def start_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ReceiveHost, ReceivePort))
        while True:
            conn, addr = create_listener(s)
            start_new_thread(multi_threaded_connection, (conn, ))
    except Exception as e:
        print('Writer exception with binding')
        return 'ERROR'
            

if __name__ == '__main__':
    print("Writer started:")
    start_new_thread(start_service,())
    x = input()
    while x!="x":
        x = input()
