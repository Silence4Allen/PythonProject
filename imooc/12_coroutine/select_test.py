# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         select_test
# Description:  
# Author:       Allen
# Time:         2020/12/21 10:56
# ------------------------------------------------------------------------------
"""
epoll并不代表一定比select好
a.在并发高、连接活跃度不是很高的情况下，epoll比select好
b.在并发不是很高、同时连接很活跃的情况下，select比epoll好
"""
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)  # 使用非阻塞io完成http请求
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send('GET {} HTTP/1.1\r\nHOST:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
