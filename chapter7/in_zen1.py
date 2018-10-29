#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: in_zen1.py
@time: 2018/10/29 23:41
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket, sys, zen_utils

if __name__ == '__main__':
    sock = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = sys.stderr = open('log.txt', 'a', buffering=1)
    address = sock.getpeername()
    print(f"accept connection from {address}")
    zen_utils.handle_conversation(sock, address)
