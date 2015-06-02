# Tag-cloud

## 豆列可视化

需求: 豆列的最大作用是进行专题化学习, 那么首先需要提炼出专题.  
但特别是对于较长的豆列, 或者是我们想导出的内容, 如何提炼出专题呢?

豆瓣书籍中, 大量用户标注的标签信息可以为我们所用, 绘制豆列的标签云.

一图胜千言, 标签云图片不仅高效输出了我们关注的内容的几个关键词, 精要地总结了豆列内容; 还是一种时尚炫酷的可视化方式.

## 工程化思路

- 抓取豆列中每本图书的标签及出现次数, 得到合并的各个标签及次数
- 用可视化工具输出

## 实现思路
1. 抓取一本书的标签 douban api 并测试
抓取标签信息中, 最方便的输入来自豆瓣 api. 
通过正则表达式整理, 即可取出合适的内容.

示例
```python
http://developers.douban.com/wiki/?title=guide
{"rating":{"max":10,"numRaters":335,"average":"7.0","min":0},"subtitle":"","author":["[日] 片山恭一"],"pubdate":"2005-1","tags":[{"count":132,"name":"片山恭一","title":"片山恭一"},{"count":62,"name":"日本","title":"日本"},{"count":57,"name":"日本文学","title":"日本文学"},{"count":37,"name":"小说","title":"小说"},{"count":32,"name":"满月之夜白鲸现","title":"满月之夜白鲸现"},{"count":15,"name":"爱情","title":"爱情"},{"count":8,"name":"純愛","title":"純愛"},{"count":8,"name":"外国文学","title":"外国文学"}],"origin_title":"","image":"http:\/\/img3.douban.com\/mpic\/s1747553.jpg","binding":"平装","translator":["豫人"],"catalog":"\n      ","pages":"180","images":{"small":"http:\/\/img3.douban.com\/spic\/s1747553.jpg","large":"http:\/\/img3.douban.com\/lpic\/s1747553.jpg","medium":"http:\/\/img3.douban.com\/mpic\/s1747553.jpg"},"alt":"http:\/\/book.douban.com\/subject\/1220562\/","id":"1220562","publisher":"青岛出版社","isbn10":"7543632608","isbn13":"9787543632608","title":"满月之夜白鲸现","url":"http:\/\/api.douban.com\/v2\/book\/1220562","alt_title":"","author_intro":"","summary":"那一年，是听莫扎特、钓鲈鱼和家庭破裂的一年。说到家庭破裂，母亲怪自己当初没有找到好男人，父亲则认为当时是被狐狸精迷住了眼，失常的是母亲，但出问题的是父亲……。","price":"15.00元"}
```

2. 合并多本书的标签: MVP
MVP 版本的信息传递采用列表, 每添加一个标签, 需要确认在已有标签列表中是否存在; 如已存在, 需要把count叠加; 如不存在, 则建立新标签名.

3. 可视化工具
选择条件主要是基于Python, 且考虑到项目需求不高, 并不需要很复杂的可视化工具.    
另外由于输入是已经整理过的标签, 也不需要进行中文分词操作   
google找到 [word cloud](https://github.com/amueller/word_cloud)

这一工具接口简单, 输出效果也完全可以满足我们的需要.
按照 [api接口的描述](http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html)
我们使用的标签数据正好适合使用word cloud 的 generate from frequency 功能.

为了匹配二者, 调整标签输出.

可视化时遇到的具体问题基本来自于中文:
- 中文编码问题, 详见[Unicode and Chinese in Python](unicode-chinese.md)
- 中文字体问题
- word cloud 实现算法时按顺序进行, 因此需要对标签输出进行排序

---
### Minor notes
py lib 目录位置在 pyenv.....中

---
Refs

[GitHub word cloud](https://github.com/amueller/word_cloud)    
[一个中文教程, 使用了另一个工具](http://reverland.org/python/2014/01/12/python/)
