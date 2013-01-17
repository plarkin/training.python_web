#mostly code from PyMOTW, but the number counting code is mine.
#plarkin week 1 assignment

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.4',50002)
print >>sys.stderr, 'starting up on %s port %s' % server_address

sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
	
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(3)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                data_tuple = ( tuple( int(i) for i in data.split() ) )
                data_return = str(sum(data_tuple))
                connection.sendall(data_return)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
