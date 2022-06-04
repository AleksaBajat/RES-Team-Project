import json
import socket
from Model.DataSample import *


def connectToReader(y,z):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print("connecting to " + str(server_address))
    sock.connect(server_address)

    try:   
        message=y+","+z
        sock.send(message.encode("utf-8"))
        reply=sock.recv(1024)
        print(reply)
           
    except Exception as e:
        print(e)
    finally:
        print('closing socket')
        sock.close()