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

def main():
    server = HttpServer.HttpServer()
    server.start()



if __name__ == '__main__':
    main()
