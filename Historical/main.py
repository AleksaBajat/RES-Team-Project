import sys
sys.path.append("../")

import pickle
import socket
from _thread import start_new_thread
from Historical.ConnectToDatabase import connect_to_database
from Historical.ConnectToDatabase import open_connection_and_reply

IP = "127.0.0.1"
DUMP_BUFFER_PORT = 30000
READER_PORT = 60000
DATABASE_PATH = r"../database.db"

def writer_connection(connection):
    data = receive_data(connection)
    response = 'SUCCESS'
    for sample in data:
        print("Received: {}".format(sample))
        if send_sample_database(sample) == 'ERROR':
            response = 'ERROR'
    return response

def create_sql_write_query(sample):
    return f'''INSERT INTO meterReadings VALUES({sample.unit_id},{sample.user_id},{sample.consumption},'{sample.address.country}','{sample.address.city}','{sample.address.street}',{sample.address.street_number},'{sample.datetime}')'''

def send_sample_database(sample):
    try:
        db_connection = connect_to_database(DATABASE_PATH)
        sql = create_sql_write_query(sample)
        cur = db_connection.cursor()
        cur.execute(sql)
        db_connection.commit()
        return "SUCCESS"
    except RuntimeError:
        print("SQL Query failed execution.")
        return "ERROR"


def reader_connection(connection):
    data = receive_data(connection)
    data = data.decode("utf-8")
    reply = open_connection_and_reply(data)
    if reply == "":
        connection.sendall("Query result is empty".encode("utf-8"))
        return False
    else:
        connection.sendall(reply.encode("utf-8"))
        return True

def receive_data(connection):
    try:
        data = connection.recv(1024)
        sample = pickle.loads(data)
        print(str(sample))
        return sample
    except RuntimeError:
        return 'ERROR'


def create_listener(sock):
    sock.listen()
    conn, addr = sock.accept()
    return conn, addr

def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def listen(ip,port,worker_function):
    try:
        s = get_socket()
        s.bind((ip, port))
        while True:
            conn,addr = create_listener(s)
            start_new_thread(worker_function, (conn,))
    except RuntimeError:
        return 'ERROR'


if __name__ == '__main__':
    start_new_thread(listen, (IP,READER_PORT,reader_connection))
    start_new_thread(listen, (IP,DUMP_BUFFER_PORT,writer_connection))
    print("Historical started!")
    input()
