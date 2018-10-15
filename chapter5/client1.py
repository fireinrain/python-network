#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: client1.py
@time: 2018/10/15 22:31
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket


def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(('127.0.0.1', 9000))
    sock.connect(address)
    # 关闭套接字的读功能，即接受数据
    sock.shutdown(socket.SHUT_RD)
    sock.sendall('我是你大爷\n'.encode('utf-8'))
    sock.sendall('快接电话啊！\n'.encode('utf-8'))
    sock.sendall('please!!!!!!!\n'.encode('utf-8'))

    sock.close()


if __name__ == '__main__':
    client(('127.0.0.1', 8000))
