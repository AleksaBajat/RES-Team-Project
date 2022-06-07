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


def multi_threaded_connection(connection):
    with connection:
            data = conn.recv(1024)

            sample = pickle.loads(data)


            queue.put(sample)
            print("Received: {}".format(sample))


def batch_sender(queue):
    while True:
        if queue.qsize() >= QUEUE_SIZE:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.connect((SendHost, SendPort))
                    batch = []
                    for i in range(QUEUE_SIZE):
                        #batch.append(json.dumps((queue.get()).__dict__).encode('utf-8'))
                        batch.append(queue.get())
                    print(len(batch))
                    sock.send(pickle.dumps(batch))
                except Exception as e:
                    print(e)
                finally:
                    sock.close()
        time.sleep(2)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    queue = Queue(0)
    start_new_thread(batch_sender, (queue,))
    s.bind((ReceiveHost, ReceivePort))
    print("DumpBuffer Started!")
    while True:
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn,))
