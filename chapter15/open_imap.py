#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: open_imap.py
@time: 2018/12/7
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import getpass, sys
from imapclient import IMAPClient


def main():
    if len(sys.argv) != 3:
        print('usage: %s hostname username' % sys.argv[0])
        sys.exit(2)

    hostname, username = sys.argv[1:]
    c = IMAPClient(hostname, ssl=True)
    try:
        c.login(username, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
    else:
        print('Capabilities:', c.capabilities())
        print('Listing mailboxes:')
        data = c.list_folders()
        for flags, delimiter, folder_name in data:
            print('  %-30s%s %s' % (' '.join(flags), delimiter, folder_name))
    finally:
        c.logout()


if __name__ == '__main__':
    main()
