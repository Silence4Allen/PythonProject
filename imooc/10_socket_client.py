# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         10_socket_client
# Description:  
# Author:       Allen
# Time:         2020/12/19 13:01
# ------------------------------------------------------------------------------
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    send_data = input()
    client.send(send_data.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))
