# Step2 - 代码优化

## 简介

这篇我们简要的讨论一下代码优化，这里主要讨论两点

1. 过程到函数
2. 加入对media的处理
3. PEP8

我们在Step1中的编码是面向过程的，这个不利于复用，所以我们简单的将我们前面的代码函数化，方便以后扩展及别人的调用

另外，Python代码最好符合PEP8规范，方便自己和别人阅读

## 编码


### 创建 utils/common.py

```python
import os
import requests

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
```

这里主要封装了两个方法： GetPage 与 GetMedia

GetPage: 传入页面url 获得 整个页面

GetMeida: 传入图片或者视频的url， 下载媒体文件到 download/pic 或者  download/video（主要为了后续支持百思不得姐的视频）

### main.py 更改为：

```python
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


def main():
    qiushi()


if __name__ == '__main__':
    main()
```

### 运行结果：

![结果](https://github.com/bonfy/xiaolinBot/blob/master/screen/step2-2.gif)


## PEP8

```
$ pip install pep8
$ pep8 xiaolinBot
```
然后如果有不符合规范的代码，会显示提示，然后去更改就行了

![PEP8](https://github.com/bonfy/xiaolinBot/blob/master/screen/step2-1.gif)


## 完整代码 

详情见 [https://github.com/bonfy/xiaolinBot](https://github.com/bonfy/xiaolinBot/tree/step2)