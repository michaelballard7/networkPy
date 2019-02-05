import socket


def create_socket():
    client = socket.socket()
    client.connect(("localhost", 2000))  # do not forget to pass the tuple
    client.sendall("Hello world".encode())
    print("The Sever is communicating ")


create_socket()
