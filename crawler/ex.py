# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         ex
# Description:  
# Author:       Allen
# Time:         2020/10/30 14:48
# -------------------------------------------------------------------------------
import socket
import urllib
from urllib import request


class Ex(object):
    def get(self, url='http://www.baidu.com'):
        resp = request.urlopen(url)
        print(resp.read().decode())

    def post(self, timeout=1):
        try:
            data = urllib.parse.urlencode({'word': 'hello'}).encode()
            response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=timeout)
            print(response.read().decode('utf8'))
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print('TIME OUT')
            else:
                print(e)


if __name__ == '__main__':
    e = Ex()
    # e.get()
    e.get_with_param()
