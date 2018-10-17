#!/usr/bin/env python
# encoding: utf-8
"""
@desc: ssl加密socket
@software: pycharm
@file: ssl_server.py
@time: 2018/10/17 23:36
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import ssl


def ssl_server(host, port, certfile, catfile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    pass
