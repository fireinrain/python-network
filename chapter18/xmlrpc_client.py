#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: xmlrpc_client.py
@time: 2018/12/10
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import xmlrpc.client


def main():
    proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:7001')
    print(proxy.addtogether('x', 'ÿ', 'z'))
    print(proxy.addtogether(20, 30, 4, 1))
    print(proxy.quadratic(2, -4, 0))
    print(proxy.quadratic(1, 2, 1))
    print(proxy.remote_repr((1, 2.0, 'three')))
    print(proxy.remote_repr([1, 2.0, 'three']))
    print(proxy.remote_repr({'name': 'Arthur',
                             'data': {'age': 42, 'sex': 'M'}}))
    print(proxy.quadratic(1, 0, 1))


if __name__ == '__main__':
    main()
