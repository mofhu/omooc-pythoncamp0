# iDoulist Function 0 - input

## Outline
- **抓取库的选择**
  - 42 min rule
  - from scrapy to urllib2
- re basics
- 去重函数
  - `is` 与 `==` 在列表中的细节问题

## 抓取库的选择
- 大而全还是小而精简? 42 min rule may help
  - 实例: 需要选择一个合适的抓取库
  - 初步考虑是 scrapy, 最著名的 python 爬虫库
  - 答疑时, 大妈指出这个库可能过于庞大了, 学习成本可能较高
  - 组内讨论时, 乱入的大妈给出一个 **42 min 应做出原型**的参考标准
  - 最后实现功能 0 时, 选择了 urllib 库实现豆列网页抓取原型. 这个库使用起来相当简单, 熟悉用时约 4.2 min
  - 总结, 选择工具要考虑到自己水平, 根本任务是**解决问题**, 工程行为要围绕着明确目标进行!
    - 42 min 可作为一个参考. 
    - 本质: 需要有一个预设的 QC 节点, 到达节点时, 进行严格质控.

- urllib2
  - 抓取网页内容 `response = urllib2.urlopen(input_url)`
  - `response.read` 存储了网页内容(字符串)

## 正则表达式再探
- 本次使用了 `re.findall()`
- 功能是返回指定输入中出现的全部符合 re 的内容

# Reference
[Python爬虫入门三之Urllib库的基本使用](http://cuiqingcai.com/947.html)
[Python爬虫入门七之正则表达式](http://cuiqingcai.com/977.html)
[urllib2 - py doc](https://docs.python.org/2/library/urllib2.html)