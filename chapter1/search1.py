#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: search1.py
@time: 2018/10/7 0:04
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from pygeocoder import Geocoder

if __name__ == '__main__':
    # business_geocoder = Geocoder(client_id='MY_CLIENT_ID', private_key='MY_PRIVATE_KEY')
    # business_geocoder.geocode('blah')  # business as usual

    target_address = "207 N.Defiance St,Archbold, OH"
    geocode = Geocoder()
    # 需要设置代理
    geocode.set_proxy("127.0.0.1:1081")
    print(geocode.geocode(address=target_address))
    # print(Geocoder.geocode(address=target_address))
