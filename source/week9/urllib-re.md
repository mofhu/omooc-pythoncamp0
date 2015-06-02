# 用 python 简单抓取网页的内容 - Urllib 和 正则表达式

## Outline
1. 缘起
2. urllib
3. re

## 缘起: iDoulist 项目的需求
项目首先需要获取豆列中的特定信息, 如内容的链接, 书名等.
考虑到后续处理难度, 链接是唯一的更易操作, 在原型中希望抓取链接.
起初试图使用著名的 Scrapy, 但发现无从下手. 
大妈给出了 `42 分钟建议`: **42 分钟无法了解并写出可用原型, 说明不适合当下的自己**.

## urllib
经过另一番搜索, 发现 py 自带的 urllib 似乎已经足可实现原型功能.
如何使用这个库抓取信息呢?
最简使用方法: (py 2.7.9)

```python
# import urllib2
response = urllib2.urlopen(url_link) #抓取link的网页信息(纯文本)
print response.read() #把网页信息打印出来
```

实例

```python
# import urllib2
response = urllib2.urlopen('http://www.douban.com/doulist/14090587/') # 抓取豆列的网页信息(测试中发现豆列的书籍内容都存放在网页)
s = re.findall('http://book.douban.com/subject/[0-9]*/', response.read()) # 用正则表达式匹配字符串, 找到豆列中的书籍链接
```

一个大坑, 和 findall 导出的对象格式有关, 见下面代码:

```python
# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

import re
import urllib2

book_url = 'https://api.douban.com/v2/book/1139336'

def response(book_url):
    response = urllib2.urlopen(book_url)
    raw_data = re.findall('"tags".*?]', response.read())
    print str(raw_data) # 错误的访问方式
    for i in raw_data: 
        print i # 正确的访问方式

response(book_url)
```

运行结果

```python
['"tags":[{"count":2143,"name":"C","title":"C"},{"count":1397,"name":"\xe7\xbc\x96\xe7\xa8\x8b","title":"\xe7\xbc\x96\xe7\xa8\x8b"},{"count":1363,"name":"c\xe8\xaf\xad\xe8\xa8\x80","title":"c\xe8\xaf\xad\xe8\xa8\x80"},{"count":802,"name":"\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba","title":"\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba"},{"count":714,"name":"\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1","title":"\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1"},{"count":666,"name":"\xe7\xbb\x8f\xe5\x85\xb8","title":"\xe7\xbb\x8f\xe5\x85\xb8"},{"count":468,"name":"programming","title":"programming"},{"count":408,"name":"\xe7\xbc\x96\xe7\xa8\x8b\xe8\xaf\xad\xe8\xa8\x80","title":"\xe7\xbc\x96\xe7\xa8\x8b\xe8\xaf\xad\xe8\xa8\x80"}]']
"tags":[{"count":2143,"name":"C","title":"C"},{"count":1397,"name":"编程","title":"编程"},{"count":1363,"name":"c语言","title":"c语言"},{"count":802,"name":"计算机","title":"计算机"},{"count":714,"name":"程序设计","title":"程序设计"},{"count":666,"name":"经典","title":"经典"},{"count":468,"name":"programming","title":"programming"},{"count":408,"name":"编程语言","title":"编程语言"}]
```

20150528 晚上都在折腾从上面的未识别 utf8如何到中文...

后续需要的测试: 如何匹配中文?


urllib 还可实现对网页的访问(request)等功能. 
ref: py doc urllib

## 正则表达式
抓取到网页信息之后, 下一步是从网页中提取指定信息.
这个步骤主要是进行模式匹配. 正则表达式是字符串匹配的基本工具.
python 中自带正则表达式模块 re.

`s = re.search('http://www.douban.com/doulist/[0-9]*/', input_url)`
匹配`/一串数字/`

`re.search('http://book.douban.com/people/.*?/do|http://book.douban.com/people/.*?/wish|http://book.douban.com/people/.*?/collect', doulist_url)`
判断豆瓣想读格式 xxx/do|wish|collect 

`i_book_num = re.search('\d+', i)`  
在 i 中寻找数字(书籍链接中的书号), 后续用来访问豆瓣 api

前导串(example in py doc)

```python
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'

>>> m = re.search('(?<=-)\w+', 'spam-egg')
>>> m.group(0)
'egg'
```





---
ref: 

- [py doc re](https://docs.python.org/2/library/re.html)
- [Python正则表达式-w3cschool.cc](http://www.w3cschool.cc/python/python-reg-expressions.html)
- [7 Python Regular Expressions Examples – Re Match Search FindAll](http://www.thegeekstuff.com/2014/07/python-regex-examples/), 
[中文翻译](http://blog.jobbole.com/74844/)
- [正则表达式入门教程](http://deerchao.net/tutorials/regex/regex.htm)