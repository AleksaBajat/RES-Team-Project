import json
import socket
from Model.DataSample import *

def getMessage():
    print("Uneti ID brojila")
    ID=input()
    print("Uneti potrosnju brojila")
    potrosnja = input()
    print("Uneti ID korisnika ")
    korisnik=input()
    print("Uneti adresu brojila")
    adresa = input()

    message = {
        "Brojilo": {
            "ID": ID,
            "Potrosnja": potrosnja,
            "Korisnik": korisnik,
            "Adresa": adresa,
        }
    }

    message = DataSample(ID, potrosnja, korisnik, adresa)

    return json.dumps(message.__dict__).encode('utf-8')

def connectToWriter():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ("127.0.0.1", 10000)
    print("connecting to " + str(server_address))
    sock.connect(server_address)

    try:   
        message = getMessage()
        print("sending " + str(message))
        sock.send(message)
           
    except Exception as e:
        print(e)
    finally:
        print('closing socket')
        sock.close()