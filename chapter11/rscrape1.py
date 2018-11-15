#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: rscrape1.py
@time: 2018/11/15 23:19
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import argparse, requests
from urllib.parse import urljoin, urlsplit
from lxml import etree


def GET(url):
    response = requests.get(url)
    if response.headers.get('Content-Type', '').split(';')[0] != 'text/html':
        return
    text = response.text
    try:
        html = etree.HTML(text)
    except Exception as e:
        print('    {}: {}'.format(e.__class__.__name__, e))
        return
    links = html.findall('.//a[@href]')
    for link in links:
        yield GET, urljoin(url, link.attrib['href'])


def scrape(start, url_filter):
    further_work = {start}
    already_seen = {start}
    while further_work:
        call_tuple = further_work.pop()
        function, url, *etc = call_tuple
        print(function.__name__, url, *etc)
        for call_tuple in function(url, *etc):
            if call_tuple in already_seen:
                continue
            already_seen.add(call_tuple)
            function, url, *etc = call_tuple
            if not url_filter(url):
                continue
            further_work.add(call_tuple)


def main(GET):
    parser = argparse.ArgumentParser(description='Scrape a simple site.')
    parser.add_argument('url', help='the URL at which to begin')
    start_url = parser.parse_args().url
    starting_netloc = urlsplit(start_url).netloc
    url_filter = (lambda url: urlsplit(url).netloc == starting_netloc)
    scrape((GET, start_url), url_filter)


if __name__ == '__main__':
    main(GET)
