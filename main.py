# coding: utf-8

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
    results = m.transfer(url)
    return results


def PrepareData():
    results = []
    for (k, v) in SITES.items():
        results = results + AnyTransfer(k)
    return results


def main():
    print(PrepareData())


if __name__ == '__main__':
    main()
