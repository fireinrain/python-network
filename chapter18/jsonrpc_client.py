#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: jsonrpc_client.py
@time: 2018/12/10
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from jsonrpclib import Server


def main():
    proxy = Server('http://localhost:7002')
    print(proxy.lengths((1, 2, 3), 27, {'Sirius': -1.46, 'Rigel': 0.12}))


if __name__ == '__main__':
    main()
