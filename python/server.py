# import http.server
from http.server import SimpleHTTPRequestHandler
import socketserver
from http import HTTPStatus


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()


# python3 server.py
# 127.0.0.1 - - [11/Apr/2017 11:36:49] "GET / HTTP/1.1" 200 -
# http :8000
'''
HTTP/1.0 200 OK
Date: Tue, 11 Apr 2017 15:36:49 GMT
Server: SimpleHTTP/0.6 Python/3.5.2

Hello world
'''