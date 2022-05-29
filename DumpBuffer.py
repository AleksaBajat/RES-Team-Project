import json
import socket
import time
from _thread import *

from DataSample import *
from queue import Queue
import pickle

ReceiveHost = "127.0.0.1"
ReceivePort = 20000

SendHost = "127.0.0.1"
SendPort = 30000


def multi_threaded_connection(connection):
    with connection:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = json.loads(data)
            sample = DataSample(**data)
            queue.put(sample)
            print("Received: {} {} {} {}".format(sample.id, sample.potrosnja, sample.adresa, sample.korisnik))


def batch_sender(queue):
    while True:
        if queue.qsize() >= 7:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.connect((SendHost, SendPort))
                    batch = []
                    for i in range(7):
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
