# 团队合作的一些考虑

## 团队协作基本守则

需要解决的问题：
  1. 共同协作完成同一个工程的代码；
  2. 讨论项目整体
  3. 每个人的进度更新/汇报；
  4. 解决个人无法解决的问题；
  5. 发现其它人负责代码段的bug；

在GitHub上协作，很容易解决上述几个问题：
  1. 通过Git，公共仓库可被同时编辑；用pull-request可以方便地整理不同人的代码输出
  2. 严谨的讨论通过issue/wiki/mailing list，即时性的讨论则用微信等即时工具
  3. 跟踪进度采用“每日三句话”方法。原则上可用wiki/issue进行，为便于查找使用wiki。同时建议在微信更新
  4. 出现问题时，立刻同时建立issue。至少不晚于每日三句话时。做到问题不过第二天发现。
  5. 发现互相依赖的代码段的问题时，建立issue，assign相关人解决。

## 在 GitHub 协作

GitHub提供了大量适合多人异步协作的工具，小队在我的安利之下逐渐熟悉相关工具：

1. Git
  - 使用 Branch 功能进行日常代码写作
  - 相关命令如 git -b ... [git basics](my link)
  - 常建立 dev/bug 等分支
  - 一般情况下要用 pull-request 更新master，不可直接pull 到master
  - ref: [liaoxuefeng's git tutorial](link)

2. Issue
  - 基本功能是提出一个需要讨论的话题；可能是bug/功能升级/要讨论的内容等等
  - issue的open/close状态对应是否解决
  - 结合assign功能可以分配给相关人执行
  - 可以在issue下随时进行讨论（任何人都可参与，不仅是项目成员）
  - issue可添加标签，并用milestone功能整合管理
  - 详细内容：[Mastering issue](github help)

3. Wiki
  - 一些通用介绍性文档（对readme的补充）适合放在wiki中
  - 如：项目如何使用的详细介绍，对不同系统的适应，等等

