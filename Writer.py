from shutil import ExecError
import socket
from _thread import *
import json
from typing import final
from DataSample import *

ReceiveHost = "127.0.0.1" 
ReceivePort = 10101

SendHost = "127.0.0.1"
SendPort = 20202


def multi_threaded_connection(connection): 
    receiveData = [] 
    with connection:
        while True:
            data = conn.recv(100)
            if not data:
                break
            receiveData.append(data)                                                      # ako ima vise od 1024 bajta, spaja ih u jedan niz

        data = json.loads(b''.join(receiveData))                                                        # spaja niz bajtova u byte list
        sample = DataSample(**data)
        print("{} {} {} {}".format(sample.id, sample.potrosnja, sample.adresa, sample.korisnik))        # radi provere

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                            # slanje ka Dump buffer-u
            try:
                s.connect((SendHost, SendPort))
                s.send(json.dumps(sample.__dict__).encode('utf-8'))
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
        

