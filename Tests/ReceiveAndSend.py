import socket

ReceiveHost = "127.0.0.1" 
ReceivePort = 10000

def ReceiveAndSendMessage():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ReceiveHost, ReceivePort))
        s.listen()
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            conn.send(data)

ReceiveAndSendMessage()