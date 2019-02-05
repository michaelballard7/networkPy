import socket


def create_socket():
    server = socket.socket()
    server.bind(("", 2000))  # do not forget to pass the tuple
    server.listen()
    conn, addr = server.accept()
    print("The Sever is listening")

    data = conn.recv(1000)
    print(data)


create_socket()
