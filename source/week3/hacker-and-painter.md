# "Hacker and Painter"

Copyright [Frank Hu](https://github.com/Frank-the-Obscure), 2015


20150330

- finish outline v1.0 on paper
- photo here

20150331

- write v1.0
  - canvas函数语法不会用
  	 - google 一番,起初无收获,折腾了20min
  	 - 其实找到的 tk 官网也不错,但不如后来效率
  	 - 最后认识到应该在 CodeSkulptor 进行搜索,找到了官方文档
  - 发现 canvas 只能一次画一个图形
     - 因此要依靠 list or dict 与 for 循环来实现绘图
       - 多重 list 依靠 index 同步
       - 正解应该是面向对象编程,对象有三个方面的参数
       - 此次先用 basic skill 写也可
     - 最基本的版本完成,可以画出很多个圆圈了.
     
- while 死循环...
 - 类型不同的比较...i 被默认搞成了 str
 - 仍有问题,怀疑是 draw_handler 的毛病:似乎这个玩意一直在死循环
     - 经过测试果然如此! 其实并不是 while loop 的问题