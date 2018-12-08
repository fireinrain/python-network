#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: sftp_get.py
@time: 2018/12/8
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import argparse, functools, paramiko


class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


def main(hostname, username, filenames):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AllowAnythingPolicy())
    client.connect(hostname, username=username)  # password='')

    def print_status(filename, bytes_so_far, bytes_total):
        percent = 100. * bytes_so_far / bytes_total
        print('Transfer of %r is at %d/%d bytes (%.1f%%)' % (
            filename, bytes_so_far, bytes_total, percent))

    sftp = client.open_sftp()
    for filename in filenames:
        if filename.endswith('.copy'):
            continue
        callback = functools.partial(print_status, filename)
        sftp.get(filename, filename + '.copy', callback=callback)
    client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy files over SSH')
    parser.add_argument('hostname', help='Remote machine name')
    parser.add_argument('username', help='Username on the remote machine')
    parser.add_argument('filename', nargs='+', help='Filenames to fetch')
    args = parser.parse_args()
    main(args.hostname, args.username, args.filename)
