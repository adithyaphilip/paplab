#!/usr/bin/python           

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "0.0.0.0" # Get local machine name
print(host)
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send('Thank you for connecting'.encode())
   c.close()                # Close the connection

