#!/usr/bin/env python
# encoding: utf-8
"""
@desc:广播端
@software: pycharm
@file: broadcaster.py
@time: 2018/10/11 23:00
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket, sys

dest = ('<broadcast>', 51423)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.sendto(b"hello", dest)

print("looking for replies: press Ctrl + c to stop ")
while 1:
    (buf, address) = s.recvfrom(2048)
    if not len(buf):
        break
    print
    "Revived from %s:%s" % (address, buf)
