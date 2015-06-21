# 用 Python 抓取网页的特定内容 - Urllib 和 正则表达式

## Outline
1. 缘起
2. urllib2
3. re

## 缘起: iDoulist 项目的需求
项目首先需要获取豆列中的特定信息, 如内容的链接, 书名等.
考虑到后续处理难度, 链接是唯一的更易操作, 在原型中希望抓取链接.
起初试图使用著名的 Scrapy, 但发现无从下手. 

大妈给出了 `42 分钟建议`: **42 分钟无法了解并写出可用原型, 说明不适合当下的自己**.

## urllib2
经过另一番搜索, 发现 py 自带的 urllib2 似乎已经足可实现原型功能.
如何使用这个库抓取信息呢?
最简使用方法: (py 2.7.9)

```python
# import urllib2
response = urllib2.urlopen(url_link) #抓取link的网页信息(纯文本)
print response.read() #把网页信息打印出来
```

urllib 还可实现对网页的访问(request)等功能. 

ref: py doc urllib

## 正则表达式 (regular expression)
抓取到网页信息之后, 下一步是从网页中提取指定信息. 这个步骤主要是进行大量的字符串信息匹配, 正则表达式是字符串匹配的基本工具.  
正则表达式是什么呢? 一种表达世间万物的方式(大雾)...更具体地说, 程序员为了对大量字符串进行匹配, 比如今天匹配 apple, 明天匹配 orange, 后天匹配 apple 后面的 orange...单词无穷无尽, 实在是太麻烦了. 于是他们设计了一套复杂的匹配系统, 用各种匹配符来简化匹配操作.

python 中自带正则表达式模块 re. 常用函数 `re.match`, `re.search`, `re.findall`

re.MatchObject

基本实例:

1 basic example

```python
import re
print re.search('apple', 'apple')
print re.search('apple', 'orange')
match = re.search('apple', 'apple')
if match:
    print match.group() 
    
<_sre.SRE_Match object at 0x105d87308>
None
apple
```

2 re.search vs re.match

```python
import re
print re.search('apple', '1apple') #re.search 从字符串中查找, 任意位置开始都可以
print re.match('apple', '1apple') #re.match 只从字符串开始匹配

<_sre.SRE_Match object at 0x105d87238>
None
```

3 re.findall

```python
print re.findall('a', 'abdcai') #re.findall 返回一个列表

['a', 'a']
```

4 最基本的通配符

```
. (默认情况下)匹配除换行符 \n 以外的任意其它字符
\d 匹配数字
* 贪婪匹配零次或多次
? 吝啬匹配
| 逻辑或
[] 用于表示一组字符, 如 \d = [0-9]

print re.findall('ap..e', 'apple aplle apllo')
print re.findall('ap.*', 'apple aplle apllo') # *是贪婪匹配, 会直接匹配整行
print re.findall('ap.*?', 'apple aplle apllo') # 加上?之后则最少匹配了
print re.findall('ap.*? ', 'apple aplle apllo') # 加上?和 空格

['apple', 'aplle']
['apple aplle apllo']
['ap', 'ap', 'ap']
['apple ', 'aplle ']
```

5 

## iDoulist 正则表达式应用实例

```python
# import urllib2
response = urllib2.urlopen('http://www.douban.com/doulist/14090587/') # 抓取豆列的网页信息(测试中发现豆列的书籍内容都存放在网页)
s = re.findall('http://book.douban.com/subject/[0-9]*/', response.read()) # 用正则表达式匹配字符串, 找到豆列中的书籍链接
```

`s = re.search('http://www.douban.com/doulist/[0-9]*/', input_url)`  
匹配`/一串数字/`

`re.search('http://book.douban.com/people/.*?/do|http://book.douban.com/people/.*?/wish|http://book.douban.com/people/.*?/collect', doulist_url)`   
用吝啬匹配用户名, 用逻辑或判断豆瓣想读格式 xxx/do|wish|collect 

`i_book_num = re.search('\d+', i)`  
在 i 中寻找数字(书籍链接中的书号), 后续用来访问豆瓣 api

前导串, 可用于在提取同时去掉不需要的前导部分.(example in py doc)

```python
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'

>>> m = re.search('(?<=-)\w+', 'spam-egg')
>>> m.group(0)
'egg'
```

一个大坑, 和 findall 导出的对象格式和中文编码有关, 见 unicode 和中文编码章节


## 更多的正则表达式字符串处理例子

字符串处理是获取特定信息的基本手段. 在其它个人项目中也反复锤炼了基本技能...

1 flags: re.S 多行模式, 可匹配 \n 的多行输入

```
print re.findall('ap..e', 'app\ne aplle apllo')
print re.findall('ap..e', 'app\ne aplle apllo', flags=re.S)

['aplle']
['app\ne', 'aplle']
```

2 `re.split(pattern, string, maxsplit=0, flags=0)`: 用特定 pattern 分隔 string

3 提取特定字符串信息, 前导串可用于简单加工

```
i = 'player 162 action fold\nplayer 162 action check\n'
actions = re.findall('player 162 action .*?\n', i, flags=re.S)
print actions
​
actions = re.findall('(?<=player 162 action ).*?\n', i, flags=re.S)
print actions

['player 162 action fold\n', 'player 162 action check\n']
['fold\n', 'check\n']
```

### 小结:

这里的正则表达式都只是最简单的应用, 未用到复杂的匹配模式, 但原理是相通的. 正则表达式的语法相对来说比较晦涩, 因此, 这里希望通过相对较多的例子, 唤醒自己快速从已有例子修改, 形成可用的正则表达式.

---
References: 

- [py doc re](https://docs.python.org/2/library/re.html)
- [Python正则表达式 - w3cschool.cc](http://www.w3cschool.cc/python/python-reg-expressions.html)
- [7 Python Regular Expressions Examples – Re Match Search FindAll](http://www.thegeekstuff.com/2014/07/python-regex-examples/), 
[中文翻译](http://blog.jobbole.com/74844/)
- [正则表达式入门教程](http://deerchao.net/tutorials/regex/regex.htm)
- [Pragmatic Unicode, by Ned Batchelder](http://nedbatchelder.com/text/unipain.html), [中文翻译 by yudun1989](http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue5/unipain.html)
- [Python正则表达式匹配中文](http://blog.csdn.net/gatieme/article/details/43235791)

