#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: draft.py
@time: 2018/10/14 11:41
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

if __name__ == '__main__':
    import socket
    from pprint import pprint
    pprint(socket.has_ipv6)

    infolist = socket.getaddrinfo('baidu.com','www')
    pprint(infolist)

    print(socket.gethostbyname('baidu.com'))
    # print(socket.getfqdn('baidu.com'))

    print(socket.gethostbyaddr('127.0.0.1'))

    print(socket.getprotobyname('udp'))
    print(socket.getservbyport(22))
    print(socket.getservbyname('ssh'))
    socket.gethostbyname(socket.getfqdn())