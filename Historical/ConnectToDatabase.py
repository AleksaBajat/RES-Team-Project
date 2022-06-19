import sqlite3

database = r"../database.db"

def connect_to_database(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)


def select_by_string(conn, string):
    try:
        cur = conn.cursor()
        cur.execute(string)

        rows = cur.fetchall()
        return rows
    except RuntimeError:
        return 'ERROR'


def open_connection_and_reply(string): 
    conn = connect_to_database(database)
    with conn:
        rows = select_by_string(conn, string)
        return_string=""
        for s in rows:
            return_string += str(s) + "\n"
        return return_string