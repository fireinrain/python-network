#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: rscrape2.py
@time: 2018/11/15 23:20
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
from urllib.parse import urljoin
from chapter11.rscrape1 import main
from selenium import webdriver


class WebdriverVisitor:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def GET(self, url):
        self.browser.get(url)
        yield from self.parse()
        if self.browser.find_elements_by_xpath('.//form'):
            yield self.submit_form, url

    def parse(self):
        # (Could also parse page.source with lxml yourself, as in scraper1.py)
        url = self.browser.current_url
        links = self.browser.find_elements_by_xpath('.//a[@href]')
        for link in links:
            yield self.GET, urljoin(url, link.get_attribute('href'))

    def submit_form(self, url):
        self.browser.get(url)
        self.browser.find_element_by_xpath('.//form').submit()
        yield from self.parse()


if __name__ == '__main__':
    main(WebdriverVisitor().GET)
    # a = "I am 刘朝阳"
    # a = bytes(a.encode("utf-8"))
    # print(len(a))
