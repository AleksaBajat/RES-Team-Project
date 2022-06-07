import sqlite3
from sqlite3 import Error
 
database = r"../database.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_by_string(conn, string):
    cur = conn.cursor()
    print("string za selekciju "+string)
    cur.execute(string)

    rows = cur.fetchall()
    return rows


def open_connection_and_reply(string): 
    conn = create_connection(database)
    with conn:
        rows = select_by_string(conn, string)

        return rows