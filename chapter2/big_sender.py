#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: big_sender.py
@time: 2018/10/10 23:04
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
# IN 模块在win的平台是没有的，只有在linux平台才有
import IN, socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

if len(sys.argv) != 2:
    print('usage: big_sender.py host', file=sys.stderr)
    sys.exit(2)

hostname = sys.argv[1]
s.connect((hostname, PORT))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
try:
    s.send(b'#' * 65000)
except socket.error:
    print('The message did not make it')
    option = getattr(IN, 'IP_MTU', 14)  # constant taken from <linux/in.h>
    print('MTU:', s.getsockopt(socket.IPPROTO_IP, option))
else:
    print('The big message was sent! Your network supports really big packets!')
