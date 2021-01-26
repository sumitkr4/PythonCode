# Streaming Client

import socket

HOST = socket.gethostname()
PORT = 50007

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((HOST, PORT))

while True:
    data = clientsocket.recv(1024)
    print (repr(data))

clientsocket.close()
