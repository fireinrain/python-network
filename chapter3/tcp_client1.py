#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: tcp_client1.py
@time: 2018/10/12 23:23
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import time

from chapter3.tools import recvall


def tcp_client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f'客户端激活套接字：{sock.getsockname()}')

    sock.sendall(b"hi server, i am client")

    server_reply = recvall(sock, 1024)
    print(f"the server reply is {repr(server_reply)}")
    sock.close()


if __name__ == '__main__':
    tcp_client('127.0.0.1', 8000)
