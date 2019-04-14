#!/usr/bin/env python
# -*- coding:utf-8 -*-

# server.py
from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8001))
sock.listen(5)

while 1:
    print('Waiting for client connectiong.....')
    con, addr = sock.accept()
    print('......connected from ', addr)

    while 1:
        data = con.recv(1024)
        if not data:
            break
        print(data)
        con.send('[%s] %s' % (time.ctime(), data))
con.close()
sock.close()


