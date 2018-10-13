#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: server2.py
@time: 2018/10/13 20:55
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket

from chapter3.tools import recvall

if __name__ == '__main__':
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # # 为该程序绑定端口
    # sock.bind(('127.0.0.1', 9000))
    # sock.listen(1)
    #
    # while True:
    #     sc, sockname = sock.accept()
    #     client_message = recvall(sc, 16)
    #     print(f"16字节数据：{repr(client_message)}")
    #     sc.sendall(b'hi I am server')
    #     sc.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 9000))
    sock.listen(1)

    # 这里的sock是监听套接字
    print(f"the tcp_server is listening at :{sock.getsockname()}")
    while True:
        # 这里的sc是主动套接字
        sc, sockname = sock.accept()
        # sockname为客户端的address地址
        print(f"we have accept a new connection from {sockname}")
        print(f"socket name: {sc.getsockname()}")
        # 客户端的套接字对
        print(f"socket peer: {sc.getpeername()}")
        client_message = recvall(sc, 16)
        print(f"16字节数据：{repr(client_message)}")
        sc.sendall(b'hi I am server')
        sc.close()
        print(f"服务器完成响应，socket关闭")
        print(f"------------------------------------------------")




