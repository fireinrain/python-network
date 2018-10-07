#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: search2.py
@time: 2018/10/7 0:33
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import requests


def geocoder(address):
    parameters = {"address": address, "sensor": "false"}
    query_url = 'http://maps.googleapis.com/maps/api/geocode/json'
    # 对于被GFW墙掉的网址，使用ss代理
    proxies = {
        'http': 'http://127.0.0.1:1081',
        'https': 'http://127.0.0.1:1081',
    }
    response = requests.get(query_url, params=parameters, proxies=proxies)

    json_response = response.json()
    print(json_response['result'][0]['geometry']['location'])


if __name__ == '__main__':
    geocoder("207 N.Defiance St,Archbold, OH")
