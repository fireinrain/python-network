#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: timeapp_raw.py
@time: 2018/11/5 22:46
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import time
from wsgiref.simple_server import make_server


def app(environ, start_reponse):
    host = environ.get('HTTP_HOST', '127.0.0.1')
    path = environ.get('PATH_INFO', '/')
    if ":" in host:
        host, port = host.split(':', 1)
    if "?" in path:
        path, query = path.split("?", 1)
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    if environ['REQUEST_METHOD'] != 'GET':
        start_reponse('501 Not implemented', headers)
        yield b'501 is not implemented'
    elif host != '127.0.0.1' or path != '/':
        start_reponse('404 not found', headers)
        yield b'404 not found'
    else:
        start_reponse('200 OK', headers)
        yield time.ctime().encode('ascii')


if __name__ == '__main__':
    http_server = make_server('', 8000, app)
    host, port = http_server.socket.getsockname()
    print(f"server on:{host} prot:{port}")
    http_server.serve_forever()
