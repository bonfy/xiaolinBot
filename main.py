# coding: utf-8

import requests
from pyquery import PyQuery as pq

__author__ = 'BONFY CHEN <foreverbonfy@163.com>'

####################
#
# Consts
#
####################

PROXIES = None
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/38.0.2125.122 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,'
              'application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}


####################
#
# main function
#
####################

def main():
    SITE = 'http://www.qiushibaike.com/'
    r = requests.get(SITE, proxies=PROXIES, headers=HEADERS)
    assert r.status_code == 200
    d = pq(r.text)
    contents = d("div .article")
    for item in contents:
        i = pq(item)
        content = i("div .content").text()
        print(content)

if __name__ == '__main__':
    main()
