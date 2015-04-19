# Blackjack

Coursera project week 7

## 简述

- 用三个类(card, hand, deck)实现21点
- 代码实践中体会 OOP 的`实现`细节
  - 因整体思路 coursera 已给,主要是在实现
  - Working with classes!
  - 迷信地先学习 OOP 的基本思路和实现细节
- 200行`代码量`(因框架是 coursera 已有,实现量大约是100行)


## Notes

1. 抽象原则和 OOP 体会
   - 完成抽象层构建后,后续内容全部可在抽象层完成,可无视代码实现细节
   - 此即 OOP 的作用之一
   - 中间有一个诱惑是把 Deck 用 Hand 方法实现,仔细想来不妥
     - 想实现要调用 Hand.list 才可,但 Hand.list 只用来存数据,不应被设计为方法,方法只使用 \__str__ 和 返回值
    - 更合理的思路是用 Card 分别实现 Hand 和 Deck
      - 逻辑更清晰,减少了三者的耦合.这样构建的 Deck 更容易复用
      
2. 类型要匹配: 只能通过 Class.list 来建立一个列表
   - 如果试图用 self = [] 就会出错: self 的类型是 Class, 而不是 list!
   - 测试可用 print type(sth)

3. 调用方法的格式
   - 中间出现一次奇怪的 bug, 表现为方法返回值不对  
   - 与 coursera template 的正对照比较之后发现, 问题出在调用方法的格式上:
     - 正确 an_instance.method()
     - 错误 an_instance.method
     - 这个错误最坑爹之处在于语法不会报错(在 codeskulptor中),但方法没有执行,即导致返回值错误.
