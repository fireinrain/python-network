#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: tcp_deadlock_server.py
@time: 2018/10/13 20:05
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import sys


def server(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)

    print(f"the server is listening at： {sock.getsockname()}")
    while True:
        sc, sockname = sock.accept()
        print(f"开始处理来自：{sockname}的字节数据")

        n = 0
        while True:
            data = sc.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)
            n += len(data)
            print(f"\r {n} bytes have been processed so far ")
            sys.stdout.flush()
        print()
        sc.close()
        print(f"socket closed")


if __name__ == '__main__':
    server('127.0.0.1', 8000, 32)
