#!/usr/bin/env python
# encoding: utf-8
"""
@desc: 不支持在win上的机器跑
@software: pycharm
@file: srv_async.py
@time: 2018/10/24 22:58
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import select
import zen_utils


def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event


def server(listener):
    sockets = {listener.fileno(): listener}
    address = {}
    bytes_recieved = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = address.pop(sock)
            rb = bytes_recieved.pop(sock, b'')
            sb = bytes_to_send(sock, b'')
            if rb:
                print(f"client {address} sent {rb} but then closed")
            elif sb:
                print(f"client {address} closed before we sent {sb}")
            else:
                print(f"client {address} closed normally")
            poll_object.unregister(fd)
            del sockets[fd]


        elif sock is listener:
            sock, address = sock.accept()
            print(f"accept connection from: {address}")
            sock.setblocking(False)
            sockets[sock.fileno()] = sock

            poll_object.register(sock, select.PULLIN)
        elif event & select.POLLIN:
            more_data = sock.recv(4096)
            if not more_data:
                sock.close()
                continue
            data = bytes_recieved.pop(sock, b'') + more_data
            if data.endswith(b"?"):
                bytes_to_send[sock] = zen_utils.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_recieved[sock] = data
        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)


if __name__ == '__main__':
    address = zen_utils.parse_command_line()
    listener = zen_utils.create_srv_socket(address)
    server(listener)
