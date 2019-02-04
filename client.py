"""
1. Create Socket
2. Bind the socket to a particular port number
3. Listen to clients
4. Accept the connect
5. Communicate with the connection
6. Close the active connection
4. Close the server
"""
import socket

# create an socket
client_socket = socket.socket()

client_socket.connect(("localhost", 2000))

client_socket.sendall("Hello World from client".encode())

data = client_socket.recv(1000)

print(data.decode())

client_socket.close()
