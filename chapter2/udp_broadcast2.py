#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: udp_broadcast2.py
@time: 2018/10/11 22:52
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

MAX = 65535
PORT = 1060

if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
    s.bind(('', PORT))
    print('Listening for broadcasts at', s.getsockname())
    while True:
        data, address = s.recvfrom(MAX)
        print('The client at %r says: %r' % (address, data))

elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    network = sys.argv[2]
    s.sendto(b'Broadcast message!', (network, PORT))

else:
    print('usage: udp_broadcast.py server', file=sys.stderr)
    print('   or: udp_broadcast.py client <host>', file=sys.stderr)
    sys.exit(2)
