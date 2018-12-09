#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: binaryul.py
@time: 2018/12/9
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from ftplib import FTP
import sys, getpass, os.path


def main():
    if len(sys.argv) != 5:
        print("usage:", sys.argv[0],
              "<host> <username> <localfile> <remotedir>")
        exit(2)

    host, username, localfile, remotedir = sys.argv[1:]
    prompt = "Enter password for {} on {}: ".format(username, host)
    password = getpass.getpass(prompt)

    ftp = FTP(host)
    ftp.login(username, password)
    ftp.cwd(remotedir)
    with open(localfile, 'rb') as f:
        ftp.storbinary('STOR %s' % os.path.basename(localfile), f)
    ftp.quit()


if __name__ == '__main__':
    main()
