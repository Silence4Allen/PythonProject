# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         server
# Description:  
# Author:       Allen
# Time:         2020/10/9 09:01
# -------------------------------------------------------------------------------

from wsgiref.simple_server import make_server
from wsgi import handler


def main():
    server = make_server('localhost', 8001, handler)
    print('Serving HTTP on port 8001...')
    server.serve_forever()


if __name__ == '__main__':
    main()
