''' 
First you need to start the server then send the request from client
'''
import socket
import time
from random import randint

HOST = socket.gethostname()
PORT = 50007

serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((HOST, PORT))
serversocket.listen(1)

while True:
    clientsocket, address = serversocket.accept()
    print('Client connection accepted ', address)
    while True:
        try:
            data = str(randint(0, 9))
            print('Server sent:', data)
            clientsocket.send(data)    
            time.sleep(1)
        except socket.error, msg:
            print('Client connection closed', address)
            break

clientsocket.close()
