#!/usr/bin/env python
# encoding: utf-8
"""
@desc: udp  广播
@software: pycharm
@file: udp_broadcast.py
@time: 2018/10/11 22:19
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket, threading

MAX_BUFF = 65535


def server(ip, port):
    """
    服务端
    :param ip:
    :param port:
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"the server is listening at:{sock.getsockname()}")
    while True:
        data, address = sock.recvfrom(MAX_BUFF, )
        text = data.encode('utf-8')
        print(f"the client says:{text} @:{address}")


def client(broadcast_ip, port):
    """
    客户端
    :param broadcast_ip:
    :param port:
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    text = "broadcast message"
    sock.sendto(text.encode('utf-8'), (broadcast_ip, port))
    print("the client has send message")


if __name__ == '__main__':
    server_a = threading.Thread(target=server, args=['127.0.0.1', 8000])
    server_a.start()

    server_b = threading.Thread(target=server, args=['127.0.0.1', 9000])
    server_b.start()

    client_a = threading.Thread(target=client, args=['10.8.2.255', 1060])
    client_a.start()
    client_a.join()
