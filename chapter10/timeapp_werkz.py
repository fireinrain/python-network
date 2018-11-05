#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: timeapp_werkz.py
@time: 2018/11/5 23:31
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import time
from wsgiref.simple_server import make_server

from werkzeug.wrappers import Request, Response


@Request.application
def app(request):
    host = request.host
    if ":" in host:
        host, port = host.split(":", 1)
    if request.method != 'GET':
        return Response('501 is not implemented', status=501)
    elif host != '127.0.0.1' or request.path != '/':
        return Response('404 not found', status=404)
    else:
        return Response(time.ctime())


if __name__ == '__main__':
    http_server = make_server('', 8000, app)
    host, port = http_server.socket.getsockname()
    print(f"server on:{host} prot:{port}")
    http_server.serve_forever()
