#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: ssl_client.py
@time: 2018/10/17 23:37
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import ssl


def ssl_client(host, port, cafile=None):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_socket.connect((host, port))
    print(f"the client connect to server at:{host}:{port}")
    ssl_socket = context.wrap_socket(raw_socket, server_hostname=host)

    while True:
        data = ssl_socket.recv(1024)
        if not data:
            break
        print(f"data is：{repr(data.decode('utf-8'))}")


if __name__ == '__main__':
    ssl_client(host='127.0.0.1', port=8000)
