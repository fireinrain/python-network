#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: server2.py
@time: 2018/10/15 23:05
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket

import struct

header_struct = struct.Struct('!I')
print(header_struct.size)


def recvall(sock, length):
    bloccks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError(f'socket closed with {length} bytes left in this block')
        length -= len(block)
        bloccks.append(block)
    return b''.join(bloccks)


def get_block(sock):
    data = recvall(sock, header_struct.size)
    (block_length,) = header_struct.unpack(data)
    return recvall(sock, block_length)


def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    print(f"run the script in another window with -c to connect")
    print(f"the server listening at: {sock.getsockname()}")

    sc, sockname = sock.accept()
    print(f"accetp connection from: {sockname}")
    sc.shutdown(socket.SHUT_WR)
    while True:
        block = get_block(sc)
        if not block:
            break
        print(f"block says:{repr(block)}")
    sc.close()
    sock.close()

    pass


if __name__ == '__main__':
    server(('127.0.0.1', 8000))
