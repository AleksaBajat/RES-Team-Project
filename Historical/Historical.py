import sqlite3
import sys
sys.path.append('../')

import pickle
import socket
from _thread import *

ReceiveHostBuffer = "127.0.0.1"
ReceivePortBuffer = 30000

ReceiveHostReader = "127.0.0.1"
ReceivePortReader = 50000

def connect_to_database(fileName):
    conn = None
    try:
        conn = sqlite3.connect(fileName)
    except Exception as e:
        print(e)

    return conn

def multi_threaded_connection(connection):
    with connection:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            data = pickle.loads(data)
            for sample in data:
                print("Received: {}".format(sample))
                db_connection = connect_to_database(r"../database.db");
                sql = f''' INSERT INTO meterReadings VALUES({sample.unitId},{sample.userId},{sample.consumption},'{sample.address.country}','{sample.address.city}','{sample.address.street}',{sample.address.street_number},'{sample.datetime}')'''
                cur = db_connection.cursor()
                cur.execute(sql)
                db_connection.commit()




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ReceiveHost, ReceivePort))
    while (True):
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn,))
