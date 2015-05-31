# Chinese & unicode in Python

## outline
- 中文元素编码引起的列表输出问题
- unicode 的用途之一: 正则表达式查找中文

## 中文元素编码引起的列表输出问题
我们常通过声明 `# -*- coding: utf-8 -*-` 在 py 中指定编码   
使用时, 有时会出现奇怪的现象. 经过详细测试发现主要表现为: 在 py 2.x 中**输出列表时, 中文仍然是以编码形式, 而非本身存在.**   
且不论 utf-8 还是 unicode 都是如此.   
但英文无此问题, 列表中也可正常输出.  
另外, py 3.x 中改变了对字符的处理方式, 无需注释 utf-8 即可正确  
实例:

```python
# -*- coding: utf-8 -*-
#import re

tag = '中文'
print tag
taglist = []
taglist.append([tag,2])
print taglist
print 'taglist[0]:', taglist[0]
print 'taglist[0][0]:', taglist[0][0]
utaglist = []
utaglist.append([unicode(tag, 'utf8') ,2])
print utaglist
print utaglist[0]
print utaglist[0][0]

tag = 'english'
print tag
taglist = []
taglist.append([tag,2])
print taglist
print 'taglist[0]:', taglist[0]
print 'taglist[0][0]:', taglist[0][0]
utaglist = []
utaglist.append([unicode(tag, 'utf8') ,2])
print utaglist
print utaglist[0]
print utaglist[0][0]

re_sample1 = 'test this is english'
re_sample2 = 'test这是一行中文.'
print re.search('test.*',re_sample1).group()
print str(re.findall('test.*',re_sample1))
print re.search('test.*',re_sample2).group()
print str(re.findall('test.*',re_sample2))
```

```
输出结果, in py 2.7.9

中文
[['\xe4\xb8\xad\xe6\x96\x87', 2]]
taglist[0]: ['\xe4\xb8\xad\xe6\x96\x87', 2]
taglist[0][0]: 中文
[[u'\u4e2d\u6587', 2]]
[u'\u4e2d\u6587', 2]
中文
english
[['english', 2]]
taglist[0]: ['english', 2]
taglist[0][0]: english
[[u'english', 2]]
[u'english', 2]
english
test this is english
['test this is english']
test这是一行中文.
['test\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe8\xa1\x8c\xe4\xb8\xad\xe6\x96\x87.']
```

程序中如何解决呢?  
避免输出中文列表, 而是一个一个变量输出, 即可避免此问题

```python
# -*- coding: utf-8 -*-

l = ['语文', '数学']
print l
for i in l:
    print i

# have fun: try to fake a chinese output list by string
fake_string = '['
i = 0 
while i < len(l):
    if i < len(l) - 1:
        fake_string += "'" + l[i] + "', "
    else:
        fake_string += "'" + l[i] + "']"
    i += 1
print fake_string
```

```
不同版本下的输出: 注意 py3 中 print 变为一个函数, 代码格式稍有变化
$ pyenv global 2.7.9
$ python unicode-test.py
['\xe8\xaf\xad\xe6\x96\x87', '\xe6\x95\xb0\xe5\xad\xa6']
语文
数学
['语文', '数学']
$ pyenv global 3.4.3 
$ python unicode-test.py
['语文', '数学']
语文
数学
['语文', '数学']
```


## unicode 用于正则表达式匹配中文
utf-8 通常用三个字符段共同表示一个汉字(UTF-8 是变长的，1-6个字节，少数是汉字每个占用3个字节，多数占用4个字节)   
而 unicode 则是一个字符表示一个汉字. 因此 unicode 用于正则表达式匹配中文更可靠(不会出现分属两个汉字的 utf-8 字节组合匹配的问题?)

通过查询对应字符的 unicode 码, 即可匹配中文字符.

## 小结
- 中文元素编码引起的列表输出问题: 用 py 3.x 是最简单的解决方案. py 2.x 下, 输出列表可能有问题, 输出元素可避免
- unicode 的用途之一: 正则表达式查找中文

## References
- [Pragmatic Unicode, by Ned Batchelder](http://nedbatchelder.com/text/unipain.html), [中文翻译 by yudun1989](http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue5/unipain.html)
- [正则表达式（二）：Unicode诸问题(上)](http://www.infoq.com/cn/news/2011/02/regular-expressions-unicode)
- [Python正则表达式匹配中文](http://blog.csdn.net/gatieme/article/details/43235791)