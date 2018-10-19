#!/usr/bin/env python
# encoding: utf-8
"""
@desc: ssl加密socket
@software: pycharm
@file: ssl_server.py
@time: 2018/10/17 23:36
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import ssl


def ssl_server(host, port, certfile, catfile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=catfile)
    context.load_cert_chain(certfile)

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((host, port))
    listener.listen(1)

    print(f"the server is listenning at {host}:{port}")
    raw_sock, address = listener.accept()
    print(f"connetc from:{repr(address)}")
    ssl_scok = context.wrap_socket(raw_sock, server_side=True)

    ssl_scok.sendall("simple is better than complex".encode('utf-8'))
    ssl_scok.close()


if __name__ == '__main__':
    ssl_server('127.0.0.1', 8000)
