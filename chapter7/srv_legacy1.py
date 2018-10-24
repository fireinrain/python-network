#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: srv_legacy1.py
@time: 2018/10/24 22:37
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

import zen_utils


class ZenHandler(BaseRequestHandler):
    def handle(self):
        zen_utils.handle_conversation(self.request, self.client_address)


class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1


if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    server = ZenServer(address, ZenHandler)
    server.serve_forever()
