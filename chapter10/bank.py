#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: bank.py
@time: 2018/11/13 23:14
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import os, pprint, sqlite3
from collections import namedtuple


def open_database(path="bank.db"):
    new = not os.path.exists(path)
    db = sqlite3.connect(path)

    if new:
        c = db.cursor()
        c.execute("create table payment(id integer primary key ,debit text,credit text,dollars integer ,memo text)")
        add_payment(db, "brandon", "psf", 125, "regist from pycon")
        add_payment(db, "brandon", "liz", 120, "payment for write the code")
        add_payment(db, "sam", "brandon", 25, "gas money for the ride")
        db.commit()
    return db


def add_payment(db, debit, credit, dollars, memo):
    db.cursor().execute("insert into payment (debit,credit,dollars,memo) values (?,?,?,?)",
                        (debit, credit, dollars, memo))


def get_payment(db, account):
    c = db.cursor()
    c.execute("select * from payment where credit= ? or debit=? order by id", (account, account))

    Row = namedtuple("Row", [tup[0] for tup in c.description])
    return [Row(*row) for row in c.fetchall()]


if __name__ == '__main__':
    db = open_database()
    pprint.pprint(get_payment(db, "brandon"))
