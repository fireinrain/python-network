#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: dns_basic.py
@time: 2018/10/14 13:03
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
# 需要安装dnspython3

import dns.resolver


def lookup(name):
    for qtype in ['A', 'AAAA', 'CNAME', 'MX', 'NS']:
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)


if __name__ == '__main__':
    # lookup('baidu.com')
    lookup('bilibili.com')