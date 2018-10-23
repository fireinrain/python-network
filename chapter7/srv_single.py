#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: srv_single.py
@time: 2018/10/23 22:58
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import zen_utils

if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    listener = zen_utils.create_srv_socket(address)
    zen_utils.accept_connections_forever(listener)
