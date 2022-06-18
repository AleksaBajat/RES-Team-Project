import sqlite3
from sqlite3 import Error
 
database = r"../database.db"

def connect_to_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_by_string(conn, string):
    cur = conn.cursor()
    cur.execute(string)

    rows = cur.fetchall()
    return rows


def open_connection_and_reply(string): 
    conn = connect_to_database(database)
    with conn:
        rows = select_by_string(conn, string)
        return_string=""
        for s in rows:
            return_string += str(s) + "\n"
        return return_string