#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: srv_asyncio01.py
@time: 2018/10/25 23:58
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import asyncio
import zen_utils


class ZenServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print(f"Accept connection from:{self.address}")

    def data_received(self, data):
        self.data += data
        if self.data.endswith(b'?'):
            answer = zen_utils.get_answer(self.data)
            self.transport.write(answer)
            self.data = b''

    def connection_lost(self, exc):
        if exc:
            print(f"client :{self.address} error:{repr(exc)}")
        elif self.data:
            print(f"client:{self.address} sent {self.data} then closed")
        else:
            print(f"client:{self.address} closed socket")


if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ZenServer, *address)
    server = loop.run_until_complete(coro)
    print(f"listenning at:{address}")

    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
