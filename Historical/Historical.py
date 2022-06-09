import sqlite3
import sys
import json
sys.path.append('../')

import pickle
import socket
from _thread import *
from ConnectToDatabase import *

ReceiveHostBuffer = "127.0.0.1"
ReceivePortBuffer = 30000

def multi_threaded_connection(connection):
    with connection:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            data = pickle.loads(data)
            if(isinstance(data,bytes)):
                print("Reader connected")
                data=data.decode("utf-8")
                reply= open_connection_and_reply(data)
                if(reply == ""):
                    conn.sendall("Database is empty".encode("utf-8"))
                else:
                    conn.sendall(reply.encode("utf-8"))
            else:
                print("DumpBuffer connected")
                for sample in data:
                    print("Received: {}".format(sample))
                    db_connection = connect_to_database(r"../database.db");
                    sql = f''' INSERT INTO meterReadings VALUES({sample.unitId},{sample.userId},{sample.consumption},'{sample.address.country}','{sample.address.city}','{sample.address.street}',{sample.address.street_number},'{sample.datetime}')'''
                    cur = db_connection.cursor()
                    cur.execute(sql)
                    db_connection.commit()




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHostBuffer, ReceivePortBuffer))
    print("Historical started!")
    while (True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn,))
