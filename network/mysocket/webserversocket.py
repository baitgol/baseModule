#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

def handle_request(client):#处理请求函数
    buf = client.recv(1024)#接收请求的buf
    client.send("HTTP/1.1 200 OK\r\n\r\n")#浏览器使用的协议及返回状态码
    client.send("Hello, Web Server")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#定义web server socket
    sock.bind(('127.0.0.1',8888))
    sock.listen(5)

    while True:
        connection,address = sock.accept()#调用handle_request
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()