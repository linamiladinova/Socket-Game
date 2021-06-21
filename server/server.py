import socket
import os
from _thread import *
import threading

ServerSocket = socket.socket()
host = '130.204.10.84'
port = 6666
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)

global clients
clients = set()
global clients_lock
clients_lock = threading.Lock()


def threaded_client(connection):
    global clients
    global clients_lock
    clients.add(connection)
    connection.send(str.encode('Welcome to ShitChat!'))
    while True:
        data = connection.recv(1024)
        reply = data.decode('utf-8')
        if not data:
            break
        with clients_lock:
            for c in clients:
                c.sendall(str.encode(reply))
        connection.sendall(str.encode(reply))

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
