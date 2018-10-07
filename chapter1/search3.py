#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: search3.py
@time: 2018/10/7 0:52
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import http.client
import json
from urllib.parse import quote_plus

base_url = '/maps/api/geocode/json'
target_address = "207 N.Defiance St,Archbold, OH"


# 没使用代理。无法访问啊
# 谷歌地图api升级了，调用必须要api_key
def geocode(address):
    path = '{}?address={}&sensor=false'.format(base_url, quote_plus(address))
    # 连接到本地的一个代理端口
    connection = http.client.HTTPConnection('127.0.0.1', 1081)
    # 代理的网址为maps.google.com
    connection.set_tunnel('maps.google.com')

    connection.request('GET', path)
    raw_reply = connection.getresponse().read()
    print(raw_reply)

    reply = json.loads(raw_reply.decode('utf-8'))
    print(reply)
    print(reply['result'][0]['geometry']['location'])


if __name__ == '__main__':
    geocode(target_address)
