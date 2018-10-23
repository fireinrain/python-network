#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: srv_threaded.py
@time: 2018/10/23 23:20
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import zen_utils
from threading import Thread


def start_threads(listener, wokers=4):
    t = (listener,)
    for i in range(wokers):
        Thread(target=zen_utils.accept_connections_forever, args=t).start()


if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    listener = zen_utils.create_srv_socket(address)
    start_threads(listener)
