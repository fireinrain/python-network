#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: manage.py
@time: 2018/11/15 23:18
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djbank.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)