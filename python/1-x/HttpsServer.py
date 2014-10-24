#-------------------------------------------------------------------------------
# Name:        Https Server Module
# Purpose:
#
# Author:      allen_su
#
# Created:     28/09/2014
# Copyright:   (c) allen_su 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import BaseHTTPServer, SimpleHTTPServer
import ssl

class HttpsServerRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        file = open(r'response.txt')
        txt = file.read()
        print(len(txt))
        self.send_response(200)
        self.send_header("Content-Length", len(txt))
        self.send_header("Content-Type", "application/soap+xml; charset=utf-8")
        self.end_headers()
        self.wfile.write(txt)

    def do_GET(self):
        self.send_response(200)
        #self.send_header("Connection", "Keep-Alive")
        self.send_header("Content-Type","text/html")
        self.send_header("Pragma", "no-cache")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Content-Length", "0")
        self.end_headers()


httpd = BaseHTTPServer.HTTPServer(('',443), HttpsServerRequestHandler)
httpd.socket = ssl.wrap_socket( httpd.socket, certfile='server.pem', server_side = True)
httpd.serve_forever()

