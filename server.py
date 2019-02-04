
""" 
1. Create Socket
2. Bind the server socket to a particular port number
3. Listen to clients
4. Accept the connect
5. Communicate with the connection
6. Close the active connection
4. Close the server
"""
import socket

server_socket = socket.socket()

server_socket.bind(("", 2000))
print("Server is bound to port number")

server_socket.listen()
print("Server is listening for clients")

conn, addr = server_socket.accept()

print("Client from address", addr)

data = conn.recv(1000)

conn.sendall("Hey from server".encode())

# data is translated in bytes to send across the network
print(data)
print("Decoded data")
# this decodes into a string
print(data.decode())

# close all the connections
conn.close()
server_socket.close()
