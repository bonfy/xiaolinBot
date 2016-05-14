# Step1 - 获得页面并处理获得所要内容

## 环境准备

Python3.5 最好使用venv

另外需要两个必要的库： 

* [requests](https://github.com/kennethreitz/requests) : 一个封装了HTTP服务的python库
* [pyquery](https://github.com/gawel/pyquery) : 类似Jquery，使用非常方便

```bash
$ pip install requests
$ pip install pyquery
```

## 开始

### 实现第一个应用

我们第一个应用实现的功能主要如下：

1. 访问一个页面,这里我们以 糗事百科(http://www.qiushibaike.com/) 为例
2. 获得页面的内容
3. 进行简单的处理，获得我们需要的内容

```python

import requests
from pyquery import PyQuery as pq

__author__ = 'BONFY CHEN <foreverbonfy@163.com>'


SITE = 'http://www.qiushibaike.com/'
r = requests.get(SITE)
assert r.status_code == 200
d = pq(r.text)
contents = d("div .article")
for item in contents:
    i = pq(item)
    content = i("div .content").text()
    print(content)

```

### 结果

![结果](https://github.com/bonfy/xiaolinBot/blob/master/screen/step1-1.gif)

### 简单分析

1. 利用 requests.get 获得页面
2. assert 断言，如果网络问题 访问不到就退出
3. contents 利用 pyquery 获得所有文章 后续 读取 div class ＝ "content" 的为文本内容 （这里没有处理图片后续的讲解中会完善）
4. print 输出

### 完整代码 

补充模仿浏览器的Headers,详情见 [https://github.com/bonfy/xiaolinBot](https://github.com/bonfy/xiaolinBot)


