from msilib.schema import Error
import socket
sendHost = "127.0.0.1" 
sendPort = 40000


def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_data(connection):
    try:
        data = connection.recv(1024)
        return data
    except Exception as e:
        print(e)
        return "Error"
        

def send_data(message, sendHost, sendPort):
    s = get_socket()                            # sending towards DumpBufer
    try:
        print("connecting to " + str(sendHost+":"+str(sendPort)))
        s.connect((sendHost, sendPort))
        s.send(message.encode("utf-8"))
        value = receive_data(s)
        value=value.decode("utf-8")
    except Exception as e:
        print(e)
    finally:
        s.close()
        return value

def connect_to_reader(option, parameter):
    message = option + ", " + parameter
    reply = send_data(message,sendHost,sendPort)    
    print(reply)
    return message
    
   
