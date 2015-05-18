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
urllib 还可实现对网页的访问(request)等功能. 
ref: py doc urllib

## 正则表达式
抓取到网页信息之后, 下一步是从网页中提取指定信息.
这个步骤主要是进行模式匹配. 正则表达式是字符串匹配的基本工具.
python 中自带正则表达式模块 re.


ref: py doc re; linux user re guide
