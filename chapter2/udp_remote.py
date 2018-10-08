#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: udp_remote.py
@time: 2018/10/8 23:36
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import random, socket, sys, argparse

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print(f"the server is listening at:{sock.getsockname()}")

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print(f"丢掉来自：{address}的包！！！")
            continue
        text = data.encode('utf-8')
        print(f"the client at {address} says {text}")
        message = f"your data is {len(data)} bytes long"
        sock.sendto(message.encode('utf-8'), address)


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))

    print(f'client socket name is {sock.getsockname()}')

    delay = 0.1
    text = "the message from client"
    data = text.encode('utf-8')
    while True:
        sock.send(data)
        print(f"waiting up to {delay} second for a reply")
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2
            if delay > 0.2:
                raise RuntimeError("I think the server is down")
            else:
                break
    print(f"the server say {data.decode('utf-8')}")


if __name__ == '__main__':
    choise = {'client': client, 'server': server}
    parser = argparse.ArgumentParser()
    parser.add_argument('role', choices=choise, help='which role to take')
    parser.add_argument('host', help='the server listen at')
    parser.add_argument('port', metavar='PORT', type=int, default=1060, help='udp port default is 1060')
    args = parser.parse_args()
    function = choise[args.role]
    function(args.host, args.p)
