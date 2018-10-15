#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: server1.py
@time: 2018/10/15 22:31
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket


def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)

    print(f"run the script in another window with -c to connect")
    print(f"the server listening at: {sock.getsockname()}")

    sc, sockname = sock.accept()
    print(f"accetp connection from: {sockname}")
    # 关闭套接字的写功能，即不能向客户端发数据
    sc.shutdown(socket.SHUT_WR)

    message = b''
    while True:
        more = sc.recv(1024)
        if not more:
            print(f"recieve 0 byte-end of file")
            break
        print(f"recieve {len(more)} bytes from the client")
        message += more
    print(f"message----->:")
    print(f"{message.decode('utf-8')}")
    sc.close()
    sock.close()


if __name__ == '__main__':
    server(('127.0.0.1', 8000))
