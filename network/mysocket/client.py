#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *


#clint

sock=socket(AF_INET,SOCK_STREAM)
sock.connect(('127.0.0.1', 8001))

data = 'hello!'
sock.send(data)
data2 = sock.recv(2014)
print(data2)

sock.close()


   

