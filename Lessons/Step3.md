# Step3 - 适配器

## 爬虫中最经常遇到的问题

爬虫中最经常遇到的问题就是 我们需要对不同的网站上的内容进行抓取，但是抓取到的内容结构都是一样的，后续处理也是一样的，只是不同网站上展示我们要的内容的方式是不一样的，需要我们对各个网站逐一分析，构建需要的适配器去处理


## 实现一个简单的适配器

为了更通用地取匹配多个需要下载的网站，我们通常需要使用适配器，主程序中调用相同的方法，却可以对不同的网站进行下载。

实现适配器的方法有多种，这里因为没有用class，就简单的使用 importlib 中的 import_module 方法，也可以实现我们需要的功能

最简单实现：

先建立一个文件夹 extractors,里面建立三个文件： __init__.py, baisi.py, qiubai.py

__init__.py 不用写代码

baisi.py:

```python
def TransferPageToData_baisi(url):
    print('baisi', url)


transfer = TransferPageToData_baisi
```

qiubai.py

```
def TransferPageToData_qiubai(url):
    print('qiubai', url)

transfer = TransferPageToData_qiubai

```

然后将我们的main.py 修改成如下：

```python
# coding: utf-8

from pyquery import PyQuery as pq
from utils.common import GetMedia, GetPage
from importlib import import_module


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

if __name__ == '__main__':
    main()
```

然后我们运行

```cmd
$ python3 main.py
```

得到结果

![结果](https://github.com/bonfy/xiaolinBot/blob/master/screen/step3-1.gif)


## 简单说明：

其实我们这一种实现方式的关键就是 ：

1. extractors里面的适配器都返回同样的数据结构(上面我们只是print, 待会我们返回都是json 的list)
1. 利用transfer = XXXX 最后返回统一的函数名
1. 在主函数中 利用 m = import_module('.'.join(['extractors', key])) 直接获得模块，然后调用模块的transfer函数

这里我们简单的直接用 dict的key直接去配对我们的module了，如果更好一些可以对url正则去判断适配哪个适配器，这里不做扩展，感兴趣的朋友可以去看看[you-get](https://github.com/soimort/you-get)的实现方式

## 完善适配器

最后我们加入对各网站的解析，并返回一个list


baisi.py

```python
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
```

qiubai.py

```
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

```

main.py
```python
# coding: utf-8

from importlib import import_module


__author__ = 'BONFY CHEN <foreverbonfy@163.com>'


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
```

运行得到结果

![完整结果](https://github.com/bonfy/xiaolinBot/blob/master/screen/step3-2.gif)


## 完整代码 

详情见 [https://github.com/bonfy/xiaolinBot](https://github.com/bonfy/xiaolinBot/tree/step3)

如果大家觉得有用，也请不要吝啬Star 和 Like哦～