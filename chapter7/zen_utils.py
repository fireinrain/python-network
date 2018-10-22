#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: zen_utils.py
@time: 2018/10/21 9:56
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket, time

aphorisms = {
    b'Beautiful is better than?': b'Ugly.',
    b'Explicit is better than?': b'Implicit.',
    b'Simple is better than?': b'Complex.'
}


def get_answer(aphorism):
    time.sleep(0.0)
    return aphorisms.get(aphorism, b'Error:unknown aphorism.')


def parse_command_line():
    return '127.0.0.1', 8000


def create_srv_socket(address):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print(f"listenning at：{address}")
    return listener


def accept_connections_forever(listener):
    while True:
        sock, address = listener.accept()
        print(f"accept connection from: {address}")
        handle_conversation(sock, address)


def handle_conversation(sock, address):
    try:
        while True:
            handle_request(sock)
    except EOFError as e:
        print(f"client socket to {address} has closed")
    except Exception as e:
        print(f"client:{address} error: {e}")
    finally:
        sock.close()


def handle_request(sock):
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)


def recv_until(sock, suffix):
    message = sock.recv(4096)
    if not message:
        raise EOFError("socket closed")
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise EOFError(f"recieved {message} the socket closed!")
        message += data
    return message


if __name__ == '__main__':
    print(parse_command_line())
