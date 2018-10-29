#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: srv_asyncio2.py
@time: 2018/10/29 22:18
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import asyncio, zen_utils


@asyncio.coroutine
def handle_conversation(reader, writer):
    address = writer.get_extra_info('peername')
    print(f"accept connection from:{address}")

    while True:
        data = b''
        while not data.endswith(b"?"):
            more_data = yield from reader.read(4096)
            if not more_data:
                if data:
                    print(f"client :{address} sent {repr(data)} but closed")
                else:
                    print(f"client:{address} closed socket normally")
                return
            data += more_data
        answer = zen_utils.get_answer(data)
        writer.write(answer)


if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_conversation, *address)
    server = loop.run_until_complete(coro)
    print(f"listenning @ :{address}")
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
