#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: client.py
@time: 2018/10/22 23:50
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import random
import socket

from chapter7 import zen_utils


def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return
    for aphorism in random.sample(aphorisms, 3):
        sock.sendall(aphorism)
        print(aphorism, zen_utils.recv_until(sock, b'.'))
    sock.close()


if __name__ == '__main__':
    client(('127.0.0.1', 8000))
