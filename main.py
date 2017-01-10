# coding: utf-8

from importlib import import_module
import os


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
    results = m.transfer(url)
    return results


def PrepareData():
    results = []
    for (k, v) in SITES.items():
        results = results + AnyTransfer(k)
    return results


def CheckFolder():
    """检查文件夹，没有就创建

       检查 Folder: download/video & download/image
    """
    if not os.path.exists('download/video'):
        os.makedirs('download/video')
    if not os.path.exists('download/image'):
        os.makedirs('download/image')

def main():
    CheckFolder()
    print(PrepareData())


if __name__ == '__main__':
    main()
