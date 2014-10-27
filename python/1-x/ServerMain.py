#-------------------------------------------------------------------------------
# Name:        Windows Phone Server Main
# Purpose:
#
# Author:      allen_su
#
# Created:     28/09/2014
# Copyright:   (c) allen_su 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import HttpServer
import ssl,HttpsServer
import threading

def StartHttpServer():
    server = HttpServer.HttpServer()
    server.start()

def StartHttpsServer():
    httpd = BaseHTTPServer.HTTPServer(('',443), HttpsServerRequestHandler)
    httpd.socket = ssl.wrap_socket( httpd.socket, certfile='server.pem', server_side = True)
    httpd.serve_forever()

def main():
    http = threading.thread(StartHttpServer)
    https = threading.thread(StartHttpsServer)
    http.start()
    https.start()
    http.join()



if __name__ == '__main__':
    main()
