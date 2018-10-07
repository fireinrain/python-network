#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: udp_local.py
@time: 2018/10/7 15:08
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import socket
from datetime import datetime
import threading

MAX_BYTES = 65535


def server(sport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', sport))
    print(f"server listenning at {sock.getsockname()}")
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print(f"the client at{address} say {text}")
        print(f"your data is {len(data)} bytes long")
        data = text.encode("ascii")
        sock.sendto(data, address)


def client(sport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data_text = f"the time is{datetime.now()}"
        data = data_text.encode('ascii')

        sock.sendto(data, ('127.0.0.1', sport))
        print(f"the os assigened me the address：{sock.getsockname()}")
        print(f"client at {sock.getsockname()}")
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print(f"the server:{address} reply data:{text}")


if __name__ == '__main__':
    port = 8000
    client_s = threading.Thread(target=client, args=[port, ])
    server_s = threading.Thread(target=server, args=[port, ])
    server_s.start()
    client_s.start()
    # task = [server_s,client_s]
    # for i in task:
    #     i.start()
    # for s in task:
    #     s.join()
