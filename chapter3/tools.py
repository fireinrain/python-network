#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: tools.py
@time: 2018/10/12 23:15
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError(f"was expecing {length} bytes but only recieved"
                           f"{len(data)} before the socket closed")
        data += more
    return data
