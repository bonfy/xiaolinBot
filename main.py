# coding: utf-8

import requests
from pyquery import PyQuery as pq

__author__ = 'BONFY CHEN <foreverbonfy@163.com>'


SITE = 'http://www.qiushibaike.com/'
r = requests.get(SITE)
assert r.status_code == 200
d = pq(r.text)
contents = d("div .article")
for item in contents:
    i = pq(item)
    content = i("div .content").text()
    print(content)
