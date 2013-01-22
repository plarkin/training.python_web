#!/usr/bin/env python

import socket 

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

f = open('tiny_html.html', 'r')
f_html = f.read()

def ok_response(body):
    return 'HTTP/1.1 200 OK\r\n\r\n' + body

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    if data: # if the connection was closed there would be no data
        print "received: %s, sending it back"%data
        send_f_html = ok_response(f_html)
        client.send(send_f_html)
        client.close()
    f.close()
