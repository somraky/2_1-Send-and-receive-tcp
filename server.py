#!/usr/bin/env python

import socket
import base64
TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024000  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    factorial = 1
    num = int(data)
    while num>1:
        factorial *= num
        num = num-1
    conn.send(str(factorial))  # echo
conn.close()
