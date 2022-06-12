import sys
sys.path.append("../")

import pickle
import socket
from _thread import *
from Historical.ConnectToDatabase import *

IP = "127.0.0.1"
DUMP_BUFFER_PORT = 30000
READER_PORT = 60000
DATABASE_PATH = r"../database.db"

def writer_connection(connection):
    data = receive_data(connection)
    for sample in data:
        print("Received: {}".format(sample))
        send_sample_database(sample)

def create_sql_write_query(sample):
    return f'''INSERT INTO meterReadings VALUES({sample.unitId},{sample.userId},{sample.consumption},'{sample.address.country}','{sample.address.city}','{sample.address.street}',{sample.address.street_number},'{sample.datetime}')'''

def send_sample_database(sample):
    try:
        db_connection = connect_to_database(DATABASE_PATH);
        sql = create_sql_write_query(sample)
        cur = db_connection.cursor()
        cur.execute(sql)
        db_connection.commit()
        return "Success"
    except:
        print("SQL Query failed execution.")
        return "Fail"


def reader_connection(connection):
    data = receive_data(connection)
    data = data.decode("utf-8")
    reply = open_connection_and_reply(data)
    if reply == "":
        connection.sendall("Database is empty".encode("utf-8"))
    else:
        connection.sendall(reply.encode("utf-8"))


def receive_data(connection):
    data = connection.recv(1024)
    sample = pickle.loads(data)
    print(str(sample))
    return sample


def create_listener(sock):
    sock.listen()
    conn, addr = sock.accept()
    return conn, addr



def listen(ip,port,worker_function):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        while True:
            conn,addr = create_listener(s)
            start_new_thread(worker_function, (conn,))


if __name__ == '__main__':
    start_new_thread(listen, (IP,READER_PORT,reader_connection))
    start_new_thread(listen, (IP,DUMP_BUFFER_PORT,writer_connection))
    print("Historical started!")
    input()
