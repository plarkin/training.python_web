#mostly code from PyMOTW, but the number counting code is mine.
#plarkin week 1 assignment

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.IPPROTO_IP)

# Connect the socket to the port where the server is listening
server_address = ('192.168.0.4',50002)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
	get_num = raw_input("number 1: "),raw_input("number 2: ")
	message = get_num[0]+" "+get_num[1]
	print >>sys.stderr, 'sending "%s"' % message
	sock.sendall(message)
	data = sock.recv(3)
	print >>sys.stderr, 'received "%s"' % data	
	# Look for the response
#	amount_received = 0
#	amount_expected = len(message)
	
#	while amount_received < amount_expected:
#		data = sock.recv(1)
#		amount_received += len(data)
#		print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
	

#number1 = int(raw_input("number 1: "))