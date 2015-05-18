# 用 Python 模拟键盘鼠标操作 - PyAutoGUI
## Outline
1. 缘起
2. PyAutoGUI 超简略入门

## 缘起: 如何输出到豆列?
iDoulist 项目中, `豆列-本地处理-豆列`的循环是基本考虑. 前文中通过使用 urllib + regular expression, 完成了抓取豆列信息的工作原型. 
但输出到豆列相比于抓取, 是更复杂的问题. 运用常识有以下几个思路
- urllib 模拟网页操作: 需要理解豆瓣网页操作机制. 看了看毫无头绪.
- 豆瓣 api: 经查并无开放豆列 api
- 模拟键盘鼠标重复操作: 看上去最麻烦, 但一定可行的方案 -- 另外也是大妈 QA 中给出的可选方案
经过一番 google, 又发现了 PyAutoGUI 这个库很适合模拟键盘鼠标操作. 于是决定原型用模拟键盘鼠标操作来写.

## PyAutoGUI 超简略入门
由于 [Controlling the Keyboard and Mouse with GUI Automation](https://automatetheboringstuff.com/chapter18/) 中已给出了相当详尽的入门教程, 这里不再叙述过多, 仅以 iDoulist 中用到的功能为例简单介绍.
1. 鼠标点击操作
`pyautogui.click(position)` position 为 `(x,y)` 形式
即点击屏幕上 (x,y) 位置
标准语法为
`pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')`
The button keyword argument can be 'left', 'middle', or 'right'.
2. 键盘按键操作
`pyautogui.press('enter') # 按 enter 键一次` 
`pyautogui.typewrite('Hello world!\n', interval=secs_between_keys) # 在当前位置书写 Hello world!换行符`
3. 寻找图片(辅助确定鼠标位置)
有了点击键盘鼠标的操作, 原则上我们已经能做非常多的事情.
但在现实生活中, 很多时候我们希望能让自己的代码更智能: 如在 iDoulist 中, 输出到豆列需要知道屏幕上 "添加到豆列" 按钮的位置. 最早的版本中, 采用了从屏幕直接读取当前位置的方式(即要求用户把鼠标放在按钮的位置, 程序运行时读取, 即得到了按钮的位置). 那么, 能不能自动化地确定按钮的位置呢? PyAutoGUI 可以做到这一点 :)
`pyautogui.locateOnScreen('output/add_button.png') # 这个函数的返回值是(x,y) 或 None`
`pyautogui.locateAllOnScreen(image, grayscale=False) # Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen.`
通过寻找按钮的截图, 我们实现了确定按钮位置.

## 小结
PyAutoGUI 可以模拟键鼠操作, 对我们进行自动化的重复性操作大有帮助.

### Reference
[Documentation](http://pyautogui.readthedocs.org/en/latest/)
[Controlling the Keyboard and Mouse with GUI Automation](https://automatetheboringstuff.com/chapter18/)