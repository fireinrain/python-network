#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: asciidl.py
@time: 2018/12/9
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import os
from ftplib import FTP


def main():
    if os.path.exists('README'):
        raise IOError('refusing to overwrite your README file')

    ftp = FTP('ftp.kernel.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel')

    with open('README', 'w') as f:
        def writeline(data):
            f.write(data)
            f.write(os.linesep)

        ftp.retrlines('RETR README', writeline)

    ftp.quit()


if __name__ == '__main__':
    main()
