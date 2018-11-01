#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: queuecrazy.py
@time: 2018/11/1 22:37
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import random, threading, time, zmq

B = 32


def ones_and_zeros(digits):
    return bin(random.getrandbits(digits)).lstrip("0b").zfill(digits)


def bitsource(zcontext, url):
    zsock = zcontext.socket(zmq.PUB)
    zsock.bind(url)
    while True:
        zsock.send_string(ones_and_zeros(B * 2))
        time.sleep(0.01)


def always_yes(zcontext, in_url, out_url):
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    isock.setsockopt(zmq.SUBSCRIBE, b'00')
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    while True:
        isock.recv_string()
        osock.send_string('Y')


def judge(zcontext, in_url, pythagoras_url, out_url):
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    for prefix in [b'01', b'10', b'11']:
        isock.setsockopt(zmq.SUBSCRIBE, prefix)
    psock = zcontext.socket(zmq.REQ)
    psock.connect(pythagoras_url)
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    unit = 2 ** (B * 2)
    while True:
        bits = isock.recv_string()
        n, m = int(bits[::2], 2), int(bits[1::2], 2)
        psock.send_json((n, m))
        sumsquares = psock.recv_json()
        osock.send_string('Y' if sumsquares < unit else 'N')


def pythagoras(zcontext, url):
    zsock = zcontext.socket(zmq.REP)
    zsock.bind(url)
    while True:
        numbers = zsock.recv_json()
        zsock.send_json(sum(n * n for n in numbers))


def tally(zcontext, url):
    zsock = zcontext.socket(zmq.PULL)
    zsock.bind(url)
    p = q = 0
    while True:
        decision = zsock.recv_string()
        q += 1
        if decision == 'Y':
            p += 4
        print(f"decision: {decision},p/q: {p/q}")


def start_thread(function, *args):
    thread = threading.Thread(target=function, args=args)
    thread.daemon = True
    thread.start()


def main(zcontext):
    pubsub = 'tcp://127.0.0.1:6700'
    reqreq = 'tcp://127.0.0.1:6701'
    pushpull = 'tcp://127.0.0.1:6702'

    start_thread(bitsource, zcontext, pubsub)
    start_thread(always_yes, zcontext, pubsub, pushpull)
    start_thread(judge, zcontext, pubsub, reqreq, pushpull)
    start_thread(pythagoras, zcontext, reqreq)
    start_thread(tally, zcontext, pushpull)
    time.sleep(30)


if __name__ == '__main__':
    # print(bin(12))
    # print(ones_and_zeros(12))

    main(zmq.Context())
