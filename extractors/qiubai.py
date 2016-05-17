from pyquery import PyQuery as pq
from utils.common import (GetMedia, GetPage)


def TransferPageToData_qiubai(url):
    page = GetPage(url)
    results = []
    d = pq(page)
    contents = d("div .article")
    for item in contents:
        i = pq(item)
        pic_url = i("div .thumb img").attr.src
        if pic_url:
            pic_path = GetMedia(pic_url)
            dct = {
                'id': i.attr.id,
                'type': 'pic',
                'mediapath': pic_path,
                'content': i("div .content").text()
            }
        else:
            dct = {
                'id': i.attr.id,
                'type': 'text',
                # 'mediapath': '',
                'content': i("div .content").text()
            }
        results.append(dct)
    return results


transfer = TransferPageToData_qiubai
