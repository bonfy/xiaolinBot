# coding: utf-8

from pyquery import PyQuery as pq
from utils.common import GetMedia, GetPage

__author__ = 'BONFY CHEN <foreverbonfy@163.com>'


####################
#
# main function
#
####################

def qiushi():
    url = 'http://www.qiushibaike.com/pic/'
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


def main():
    qiushi()


if __name__ == '__main__':
    main()
