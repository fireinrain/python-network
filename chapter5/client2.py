#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: client2.py
@time: 2018/10/15 23:05
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import socket

from chapter5.server2 import header_struct


def put_block(sock, message):
    block_length = len(message)
    sock.send(header_struct.pack(block_length))
    sock.send(message)


def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    put_block(sock, b'Beautiful is better than ugly!')
    put_block(sock, b'simple is better than complex!')
    put_block(sock, b'Explicit is better than implicit!')
    put_block(sock, b'')
    sock.close()


if __name__ == '__main__':
    client(('127.0.0.1', 8000))
