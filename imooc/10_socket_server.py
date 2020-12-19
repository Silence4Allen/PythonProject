# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         10_socket_server
# Description:  
# Author:       Allen
# Time:         2020/12/19 13:01
# ------------------------------------------------------------------------------
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_socket(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        re_data = input()
        sock.send(re_data.encode('utf8'))


# 获取从客户端发送的数据
# 一次获取1k的数据
while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的连接
    client_thread = threading.Thread(target=handle_socket, args=(sock, addr))
    client_thread.start()
# server.close()
# sock.close()
