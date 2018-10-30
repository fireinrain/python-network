#!/usr/bin/env python
# encoding: utf-8
"""
@desc: 使用 memcached
@software: pycharm
@file: squares.py
@time: 2018/10/30 22:54
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import memcache, random, time, timeit


def compute_square(mc, n):
    value = mc.get('sq:%d' % n)
    if value is None:
        time.sleep(0.001)  # pretend that computing a square is expensive
        value = n * n
        mc.set('sq:%d' % n, value)
    return value


def main():
    mc = memcache.Client(['192.168.11.117:11211'])

    def make_request():
        compute_square(mc, random.randint(0, 5000))

    print('Ten successive runs:')
    for i in range(1, 11):
        print(' %.2fs' % timeit.timeit(make_request, number=2000), end='')
    print()
    mc.set("user:19", "fuck apple!")
    value = mc.get("user:19")
    print(f"value: {value}")


if __name__ == '__main__':
    main()
