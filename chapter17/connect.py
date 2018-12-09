#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: connect.py
@time: 2018/12/9
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from ftplib import FTP


def main():
    ftp = FTP('ftp.ibiblio.org')
    print("Welcome:", ftp.getwelcome())
    ftp.login()
    print("Current working directory:", ftp.pwd())
    ftp.quit()


if __name__ == '__main__':
    main()
