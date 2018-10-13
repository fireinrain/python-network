#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: tcp_deadlock_client.py
@time: 2018/10/13 20:06
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import sys


def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = bytecount + 15

    message = b'this is 17 bytes!'
    print(f"正在传输17字节数据到服务器----")
    sock.connect((host, port))

    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print(f"{sent} bytes have send to server")
        sys.stdout.flush()
    print()
    # 关闭套接字的写功能，即不能使用send了
    sock.shutdown(socket.SHUT_WR)

    print(f"接收服务器发回来的数据----")
    recieved = 0
    while True:
        data = sock.recv(1024)
        if not recieved:
            print(f"the first data says:{repr(data)}")
        if not data:
            break
        recieved += len(data)
        print(f"{recieved} bytes have recieved --")
    print()
    sock.close()


if __name__ == '__main__':
    client('127.0.0.1', 8000, 1024*1024*1024*1024)
    # message = b'this is 17 bytes!'
    # print(len(message))
