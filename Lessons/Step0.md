# Step0 - 概述

## 功能描述

看到Twitter上有好多定时更新笑话集锦的帐号，觉得自己也可以试试，就申请了 [@xiaolintemple](https://twitter.com/xiaolintemple) 这个号，利用爬虫定时更新笑话

目前主要笑话来源于 百思不得姐 以及 糗事百科，后期还可以继续扩展

## 先上效果图

![效果图](https://github.com/bonfy/xiaolinBot/blob/master/screen/step0.gif)

## 用到的模块和知识点

### 软件

* [Mongodb](https://www.mongodb.com/) : Nosql数据库

### python第三方库

* [requests](https://github.com/kennethreitz/requests) : 一个封装了HTTP服务的python库
* [pyquery](https://github.com/gawel/pyquery) : 类似Jquery，使用非常方便
* [schedule](https://github.com/dbader/schedule) : job scheduling Python库
* [pymongo](https://github.com/gawel/pyquery) : Mongodb的python库
* [twython](https://github.com/ryanmcgrath/twython) : 封装的twitter库

### 适配器

这里会用到适配器，通配各种网站的爬虫代码，方便扩展更多网站

## 目的

主要目的有两个：

1. 个人总结。以前码完代码之后，也不会总结，也许过段时间再回过头来再看代码，总会觉得遗漏掉了一些什么，当初怎么想，为什么这么写之类的，也想利用这个机会好好总结一下。
2. 这次写的比较细，如果能给刚开始写爬虫的朋友一些借鉴的话，那也算是快事一件。也欢迎大家pull request，一起交流

## 项目地址

Github地址： [https://github.com/bonfy/xiaolinBot](https://github.com/bonfy/xiaolinBot)

欢迎大家一起交流