#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: mscrape.py
@time: 2018/11/15 23:18
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import argparse, bs4, lxml.html, requests
from selenium import webdriver
from urllib.parse import urljoin

ROW = '{:>12}  {}'


def download_page_with_requests(base):
    session = requests.Session()
    response = session.post(urljoin(base, '/login'),
                            {'username': 'brandon', 'password': 'atigdng'})
    assert response.url == urljoin(base, '/')
    return response.text


def download_page_with_selenium(base):
    browser = webdriver.Firefox()
    browser.get(base)
    assert browser.current_url == urljoin(base, '/login')
    css = browser.find_element_by_css_selector
    css('input[name="username"]').send_keys('brandon')
    css('input[name="password"]').send_keys('atigdng')
    css('input[name="password"]').submit()
    assert browser.current_url == urljoin(base, '/')
    return browser.page_source


def scrape_with_soup(text):
    soup = bs4.BeautifulSoup(text)
    total = 0
    for li in soup.find_all('li', 'to'):
        dollars = int(li.get_text().split()[0].lstrip('$'))
        memo = li.find('i').get_text()
        total += dollars
        print(ROW.format(dollars, memo))
    print(ROW.format('-' * 8, '-' * 30))
    print(ROW.format(total, 'Total payments made'))


def scrape_with_lxml(text):
    root = lxml.html.document_fromstring(text)
    total = 0
    for li in root.cssselect('li.to'):
        dollars = int(li.text_content().split()[0].lstrip('$'))
        memo = li.cssselect('i')[0].text_content()
        total += dollars
        print(ROW.format(dollars, memo))
    print(ROW.format('-' * 8, '-' * 30))
    print(ROW.format(total, 'Total payments made'))


def main():
    parser = argparse.ArgumentParser(description='Scrape our payments site.')
    parser.add_argument('url', help='the URL at which to begin')
    parser.add_argument('-l', action='store_true', help='scrape using lxml')
    parser.add_argument('-s', action='store_true', help='get with selenium')
    args = parser.parse_args()
    if args.s:
        text = download_page_with_selenium(args.url)
    else:
        text = download_page_with_requests(args.url)
    if args.l:
        scrape_with_lxml(text)
    else:
        scrape_with_soup(text)


if __name__ == '__main__':
    main()
