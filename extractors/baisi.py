from pyquery import PyQuery as pq
from utils.common import (GetMedia, GetPage)


def TransferPageToData_baisi(url):
    page = GetPage(url)
    results = []
    d = pq(page)
    contents = d("div .g-mn .j-r-c .j-r-list ul li .j-r-list-c")
    for item in contents:
        i = pq(item)
        content = i("div .j-r-list-c-desc").text().strip()
        video_id = i("div .j-video-c").attr('data-id')
        pic_id = i("div .j-r-list-c-img img").attr('data-original')
        if video_id:
            print('video: ' + video_id)
            video_des = i("div .j-video").attr('data-mp4')
            video_path = GetMedia(video_des, media_type='video')
            dct = {
                "content": content,
                "id": video_id,
                "type": "video",
                "mediapath": video_path
            }
            results.append(dct)
        elif pic_id:
            print('pic: ' + pic_id)
            pic_path = GetMedia(pic_id)

            dct = {
                "content": content,
                "id": pic_id,
                "type": "pic",
                "mediapath": pic_path
            }
            results.append(dct)
    return results


transfer = TransferPageToData_baisi
