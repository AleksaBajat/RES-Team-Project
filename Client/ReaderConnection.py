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

def send_data(message, send_host, send_port):
    s = get_socket()
    try:
        print("connecting to " + str(send_host + ":" + str(send_port)))
        s.connect((send_host, send_port))
        s.send(message.encode("utf-8"))
        value = receive_data(s)
        value=value.decode("utf-8")
        return value
    except Exception as e:
        print(e)
        s.close()



def connect_to_reader(option, parameter):
    try:
        message = option + ", " + parameter
        reply = send_data(message,sendHost,sendPort)
        print(reply)

    except Exception as e:
        print(e)
    
