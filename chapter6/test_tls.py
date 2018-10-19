#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: test_tls.py
@time: 2018/10/19 23:17
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import socket
import ssl
import sys, textwrap
import ctypes
from pprint import pprint


def open_tls(context, address, server=False):
    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if server:
        raw_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        raw_sock.bind(address)
        raw_sock.listen(1)
        say("server is listen at ", address)
        raw_client_sock, addr = raw_sock.accept()
        say("get a connetction from ", addr)
        return context.wrap_socket(raw_client_sock, server_side=True)
    else:
        say("address we want to talk to ", address)
        raw_sock.connect(address)
        return context.wrap_socket(raw_sock)


def say(title, *words):
    print(fill(title.ljust(36, '.')) + ' ' + ' '.join(str(w) for w in words))


def fill(text):
    return textwrap.fill(text, subsequent_indent='   ', break_long_words=False, break_on_hyphens=False)


if __name__ == '__main__':
    pass
