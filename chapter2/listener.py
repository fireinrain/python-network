#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: listener.py
@time: 2018/10/11 23:07
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while 1:
    try:
        message, addr = s.recvfrom(8192)
        print("Got data from ", addr)
        s.sendto("I am here", addr)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
