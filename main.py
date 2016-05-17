# coding: utf-8

from pyquery import PyQuery as pq
from utils.common import GetMedia, GetPage
from importlib import import_module


__author__ = 'BONFY CHEN <foreverbonfy@163.com>'


####################
#
# main function
#
####################

SITES = {
    'qiubai': 'http://www.qiushibaike.com/',
    'baisi': 'http://www.budejie.com/'
}


def AnyTransfer(key, sites=SITES):
    m = import_module('.'.join(['extractors', key]))
    url = sites[key]
    m.transfer(url)


def main():
    for (k, v) in SITES.items():
        AnyTransfer(k)


def qiushi():
    url = 'http://www.qiushibaike.com/'
    page = GetPage(url)
    d = pq(page)
    contents = d("div .article")
    for item in contents:
        i = pq(item)
        pic_url = i("div .thumb img").attr.src
        content = i("div .content").text()
        id = i.attr.id
        if pic_url:
            pic_path = GetMedia(pic_url)
            print('pic - {id}: {content} \npic下载到{pic_path}'.format(
                id=id, content=content, pic_path=pic_path))
        else:
            print('text - {id}: {content}'.format(id=id, content=content))


if __name__ == '__main__':
    main()
