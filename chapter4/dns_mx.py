#!/usr/bin/env python
# encoding: utf-8
"""
@desc: 解析电子邮件域名
@software: pycharm
@file: dns_mx.py
@time: 2018/10/14 13:15
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import dns.resolver


def resolve_hostname(hostname, indent=''):
    indent += '   '
    answer = dns.resolver.query(hostname, 'A')
    if answer.rrset is not None:
        for recorde in answer:
            print(f"{indent} ,{hostname} has a A address:{recorde.address}")
        return

    answer = dns.resolver.query(hostname, 'AAAA')
    if answer.rrset is not None:
        for recorde in answer:
            print(f"{indent} ,{hostname} has a AAAA address:{recorde.address}")
        return

    answer = dns.resolver.query(hostname, 'CNAME')
    if answer.rrset is not None:
        recorde = answer[0]
        cname = recorde.address
        print(f"{indent},{hostname} has a alias name:{cname}")
        resolve_hostname(cname, indent)
        return
    else:

        print(f"error have no A, AAAA, CNAME record for {hostname}")


def resolve_email_domain(domain):
    try:
        answer = dns.resolver.query(domain, 'MX', raise_on_no_answer=False)
    except dns.resolver.NXDOMAIN:
        print(f"Error no such domain")
        return
    if answer.rrset is not None:
        records = sorted(answer, key=lambda record: record.preference)
        for record in records:
            name = record.exchange.to_text(omit_final_dot=True)
            print(f"Priority,{record.preference}")
            resolve_hostname(name)
    else:
        print(f"the domain has no MX record")
        print(f"attemping to resoleve the A,AAAA,CNAME record for the domain")
        resolve_hostname(domain)


if __name__ == '__main__':
    resolve_email_domain('qq.com')
