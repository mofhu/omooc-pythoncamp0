# Tag-cloud

## 豆列可视化

豆列的最大作用是进行专题化学习, 那么首先需要提炼出专题.

书籍中的大量标签信息可以为我们所用, 绘制豆列的标签云.

## 工程化思路

- 抓取豆列中每本图书的标签及出现次数, 得到合并的各个标签及次数
- 用可视化工具输出

## 实现思路

1. 抓取一本书的标签 douban api 并测试
2. 输出一本书的标签: MVP

refs

https://github.com/amueller/word_cloud
http://reverland.org/python/2014/01/12/python/