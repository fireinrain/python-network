#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: srv_legacy2.py
@time: 2018/10/29 22:47
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import asyncore, asynchat, zen_utils


class ZenRequestHandler(asynchat.async_chat):
    def __init__(self, sock):
        asynchat.async_chat.__init__(sock)
        self.set_terminator(b'?')
        self.data = b''

    def collect_incoming_data(self, more_data):
        self.data += more_data

    def found_terminator(self):
        answer = zen_utils.get_answer(self.data + b'?')
        self.push(answer)
        self.initiate_send()
        self.data = b''


class ZenServer(asyncore.dispatcher):
    def handle_accept(self):
        sock, address = self.accept()
        ZenRequestHandler(sock)


if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    listener = zen_utils.create_srv_socket(address)
    server = ZenServer(listener)
    server.accepting = True
    asyncore.loop()
