import socket
import pickle

SendHost = "127.0.0.1" 
SendPort = 20000

def SendMessage():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SendHost, SendPort))
        s.listen()
        while True:
            conn, addr = s.accept()
            conn.send(pickle.dumps("SUCCESS"))

SendMessage()