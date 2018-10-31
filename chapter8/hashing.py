#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: hashing.py
@time: 2018/10/31 22:46
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import hashlib


# 字母分片
def alpha_shard(word):
    if word[0] < 'g':
        return 'server0'
    elif word[0] < 'n':
        return 'server1'
    elif word[0] < 't':
        return 'server2'
    else:
        return 'server3'


# 哈希分片
def hash_shard(word):
    # 除以4求余
    return 'server%d' % (hash(word) % 4)


# md5信息摘要分片
def md5_shard(word):
    datat = word.encode('utf-8')
    return 'server%d' % (hashlib.md5(datat).digest()[-1] % 4)


if __name__ == '__main__':
    print(hash_shard("abc"))
    print(hash("abc") % 4)
    print(f"{(2/3):.2f}")

    words = None
    with open('/usr/share/dict/words', 'r') as file:
        words = file.read().split()
    for func in [alpha_shard, hash_shard, md5_shard]:
        d = {'server0': 0, "server1": 0, "server2": 0, "server3": 0}
        for word in words:
            d[func(word.lower())] += 1
        print(f"{func.__name__}[:-6]")

        for key, value in sorted(d.items()):
            print(f"{key} {value} {value/len(words):.2f}")
        print()
