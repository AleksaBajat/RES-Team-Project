import sys
sys.path.append('../')

import json
import socket
import time
from _thread import *

from Model.DataSample import *
from queue import Queue
import pickle

QUEUE_SIZE = 2

ReceiveHost = "127.0.0.1"
ReceivePort = 20000

SendHost = "127.0.0.1"
SendPort = 30000


def receive_data(connection):
    try:
        data = connection.recv(1024)
        sample = pickle.loads(data)
        print(str(sample))
        return sample
    except Exception as e:
        print(e)


def create_listener(s):
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    return (conn, addr)

def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def multi_threaded_connection(connection):
    sample = receive_data(connection)
    queue.put(sample)
    print("Received: {}".format(sample))

def get_from_queue(queue):
    if queue.qsize() >= QUEUE_SIZE:
            sock = get_socket()
            try:
                sock.connect((SendHost, SendPort))
                batch = []
                for i in range(QUEUE_SIZE):
                    batch.append(queue.get())
                sock.send(pickle.dumps(batch))
                
            except Exception as e:
                print(e)
                return False

            finally:
                sock.close()
                return True
    else:
        return False

def batch_sender(queue):
    while True:
        get_from_queue()
        time.sleep(2)


if __name__ == '__main__':
    print("DumpBuffer started:")
    s = get_socket()
    queue = Queue(0)
    start_new_thread(batch_sender, (queue,))
    s.bind((ReceiveHost, ReceivePort))
    while True:
        conn, addr = create_listener(s)
        start_new_thread(multi_threaded_connection, (conn,))





