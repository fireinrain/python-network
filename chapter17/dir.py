#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: dir.py
@time: 2018/12/9
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from ftplib import FTP


def main():
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/academic/astronomy/')
    entries = []
    ftp.dir(entries.append)
    ftp.quit()

    print(len(entries), "entries:")
    for entry in entries:
        print(entry)


if __name__ == '__main__':
    main()
