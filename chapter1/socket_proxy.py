#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: socket_proxy.py
@time: 2018/10/7 13:14
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import threading

source_host = '127.0.0.1'
source_port = 5002
desc_host = '127.0.0.1'
desc_port = 1081


def send(sender, recver):
    while 1:
        try:
            data = sender.recv(2048)
        except:
            break
            print("recv error")
        try:
            recver.sendall(data)
        except:
            break
            print("send error")
    sender.close()
    recver.close()


def proxy(client):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((source_host, source_port))
    threading.Thread(target=send, args=(client, server)).start()
    threading.Thread(target=send, args=(server, client)).start()


def main():
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxy_server.bind((desc_host, desc_port))
    proxy_server.listen(50)
    print("Proxying from %s:%s to %s:%s ..." % (source_host, source_port, desc_host, desc_port))
    while 1:
        conn, addr = proxy_server.accept()
        print("received connect from %s:%s" % (addr[0], addr[1]))
        threading.Thread(target=proxy, args=(conn,)).start()


if __name__ == '__main__':
    main()
