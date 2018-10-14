#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: www_ping.py
@time: 2018/10/14 12:20
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import socket, sys


def connect_to(hostname_or_ip):
    try:
        info_list = socket.getaddrinfo(
            hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
        )
    except socket.gaierror as e:
        print(f"name service failure:{e}")
        sys.exit(1)

    info = info_list[0]
    socket_args = info_list[0:3]
    print(socket_args)
    address = info[4]
    print(address)
    socket_args = socket_args[0][0:3]
    s = socket.socket(*socket_args)
    try:
        s.connect(address)
    except socket.error as e:
        print(f"network fail: {e}")
    else:
        print(f'success: host:{info[3]} is listenning at port 80')


if __name__ == '__main__':
    connect_to('baidu.com')


