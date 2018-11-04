#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: wsgi_env.py
@time: 2018/11/4 20:39
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from pprint import pformat
from wsgiref.simple_server import make_server


def app(environ, start_response):
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    start_response('200 OK', list(headers.items()))
    yield 'Here is the WSGI environment:\r\n\r\n'.encode('utf-8')
    yield pformat(environ).encode('utf-8')


if __name__ == '__main__':
    http_server = make_server('', 8000, app)
    host, port = http_server.socket.getsockname()
    print(f"server on:{host} prot:{port}")
    http_server.serve_forever()
