#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: jsonrpc_server.py
@time: 2018/12/10
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def lengths(*args):
    """Measure the length of each input argument.
    Given N arguments, this function returns a list of N smaller
    lists of the form [len(arg), arg] that each state the length of
    an input argument and also echo back the argument itself.
    """
    results = []
    for arg in args:
        try:
            arglen = len(arg)
        except TypeError:
            arglen = None
        results.append((arglen, arg))
    return results


def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(lengths)
    print("Starting server")
    server.serve_forever()


if __name__ == '__main__':
    main()
