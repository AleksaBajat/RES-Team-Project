import socket


def connectToReader(opcija, parametar):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 40000)
    print("connecting to " + str(server_address))
    sock.connect(server_address)

    try:
        message = opcija + ", " + parametar
        sock.send(message.encode("utf-8"))
        reply = sock.recv(1024)
        print(reply.decode("utf-8"))

    except Exception as e:
        print(e)
    finally:
        print('closing socket')
        sock.close()
