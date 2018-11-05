#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: timeapp_webob.py
@time: 2018/11/5 23:17
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import time, webob
from wsgiref.simple_server import make_server



def app(environ, start_reponse):
    request = webob.Request(environ)
    if environ['REQUEST_METHOD'] != 'GET':
        response = webob.Response('501 is not implemented', status=501)
    elif request.domain != '127.0.0.1' or request.path != '/':
        response = webob.Response('404 NOT Found', status=404)
    else:
        response = webob.Response(time.ctime())
    return response(environ, start_reponse)


if __name__ == '__main__':
    http_server = make_server('', 8000, app)
    host, port = http_server.socket.getsockname()
    print(f"server on:{host} prot:{port}")
    http_server.serve_forever()
