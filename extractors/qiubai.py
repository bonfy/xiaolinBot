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
        content = i("div .content").text()
        qiubai_id = i.attr.id
        print("qiubai:", qiubai_id)
        if pic_url:
            pic_path = GetMedia(pic_url)
            dct = {
                'id': qiubai_id,
                'type': 'pic',
                'mediapath': pic_path,
                'content': content
            }
        else:
            dct = {
                'id': qiubai_id,
                'type': 'text',
                # 'mediapath': '',
                'content': content
            }
        results.append(dct)
    return results


transfer = TransferPageToData_qiubai
