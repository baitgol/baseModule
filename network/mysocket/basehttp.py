#!/usr/bin/env python
# -*- coding:utf-8 -*-

import http.server
import urllib.parse
import time
from socketserver import ThreadingMixIn
import threading

class WebRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        print('post message')
        parsed_path = urllib.parse.urlparse(self.path)
        length = self.headers.getheader('content-length');
        nbytes = int(length)
        data = self.rfile.read(nbytes)
        cur_thread = threading.currentThread()
        print('Thread:%s\tdata:%s' % (cur_thread.getName(), data))
        for i in range(10) :
            print('%s:waiting...' % cur_thread.getName())
            time.sleep(1)


        message_parts = [ 'just a test']
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)

class ThreadingHttpServer( ThreadingMixIn, http.server.HTTPServer ):
    pass

if __name__ == '__main__':
    #server = BaseHTTPServer.HTTPServer(('0.0.0.0',18460), WebRequestHandler)
    server = ThreadingHttpServer(('0.0.0.0',18460), WebRequestHandler)
    ip, port = server.server_address
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.setDaemon(True)
    server_thread.start()
    print("Server loop running in thread:", server_thread.getName())
    while True:
        pass