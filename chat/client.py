#!/usr/bin/python3

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "10.2.20.174" # Get local machine name
port = 12345                # Reserve a port for your service.
while True:
    s = socket.socket()
    s.connect((host, port))
    print (s.recv(1024))
    s.close()                     # Close the socket when done
