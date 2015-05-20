# 用 Tkinter 进行 GUI 交互

## Tkinter 简介
Tkinter 是 Python 自带的模块, 可进行基本的 GUI (图形界面) 绘制

```python
from Tkinter import *
def test_button():
	print 'iDoulist output'

root = Tk()
hello = Label(root, text = 'iDoulist') # 绘制一个标签
hello.pack()
test = Button(root, text = 'Output test', command = test_button) #绘制一个按钮, 点击则调用函数
test.pack()
root.mainloop()
```

另一种画法, 使用类 (from py doc)

```python
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
```

似乎使用类的画法封装更好; UI 元素较多时可能需要考虑用下面的画法.

References

- [Py doc: Tkinter](https://docs.python.org/2/library/tkinter.html)
- [W3C schoool ref](http://www.w3cschool.cc/python/python-gui-tkinter.html)
- [Python 下用 Tkinter 制作 GUI](http://pikipity.github.io/blog/python-tkinter.html)