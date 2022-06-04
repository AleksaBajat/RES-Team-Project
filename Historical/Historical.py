from shutil import ExecError
import socket
from _thread import *
import json
from typing import final
from Model.DataSample import *
import pickle

ReceiveHost = "127.0.0.1"
ReceivePort = 30000




def multi_threaded_connection(connection):
    with connection:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            data = pickle.loads(data)
            for sample in data:
                print("Received: {} {} {} {}".format(sample.id, sample.potrosnja, sample.adresa, sample.korisnik))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHost, ReceivePort))
    while (True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn,))


