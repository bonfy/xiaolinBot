import os
import requests


################################
#
# Consts
#
################################

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


################################
#
# requests Operation
#
################################


def GetPage(url, proxies=PROXIES, headers=HEADERS):
    r = requests.get(url, proxies=proxies, headers=headers)
    assert r.status_code == 200
    return r.text


def GetMedia(
        url, proxies=PROXIES, headers=HEADERS, chunk_size=512,
        media_type='pic'):
    r = requests.get(url, proxies=proxies, headers=headers, stream=True)
    filename = 'download/' + media_type + '/' + os.path.basename(url)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
    return filename
