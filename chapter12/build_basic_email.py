#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: build_basic_email.py
@time: 2018/11/19 23:27
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import email.message, email.policy, email.utils, sys

text = """Hello,
This is a basic message from Chapter 12.
 - Anonymous"""


def main():
    message = email.message.EmailMessage(email.policy.SMTP)
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test Sender <sender@example.com>'
    message['Subject'] = 'Test Message, Chapter 12'
    message['Date'] = email.utils.formatdate(localtime=True)
    message['Message-ID'] = email.utils.make_msgid()
    message.set_content(text)
    sys.stdout.buffer.write(message.as_bytes())


if __name__ == '__main__':
    main()
