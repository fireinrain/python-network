#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: shell.py
@time: 2018/12/8
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import subprocess


def main():
    while True:
        args = input('] ').strip().split()
        if not args:
            pass
        elif args == ['exit']:
            break
        elif args[0] == 'show':
            print("Arguments:", args[1:])
        else:
            try:
                subprocess.call(args)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
