#-------------------------------------------------------------------------------
# Name:        Http Server Module
# Purpose:
#
# Author:      allen_su
#
# Created:     28/09/2014
# Copyright:   (c) allen_su 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__version__ = "1.0"

import BaseHTTPServer

class HttpServerRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Connection", "Keep-Alive")
        self.send_header("Content-Type","text/html")
        self.send_header("Pragma", "no-cache")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Content-Length", "0")
        self.end_headers()

class HttpServer:
    def start(self):
        httpd = BaseHTTPServer.HTTPServer(('',80), HttpServerRequestHandler)
        httpd.serve_forever()


