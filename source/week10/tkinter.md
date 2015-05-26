# 用 Tkinter 进行 GUI 交互

## Tkinter 简介
Tkinter 是 Python 自带的模块, 可进行基本的 GUI (图形界面) 绘制

### 最基本的 UI 绘制
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

### 第二种画法, 使用类 (from py doc)

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

似乎使用类的画法封装更好; UI 元素较多时可能需要考虑.

### 第三种画法: ttk

ttk 是一个对 tk 的封装小工具.

一段典型代码(from ref. 1):

```python
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
# 通过 padding 绘制出一个矩阵, 再用 grid 参数把各个 UI 元素放到指定的行和列. 即可得到绘制整齐的 UI 界面

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# command命令用来指定调用的函数, 注意这个函数不能带参数, 因此参数要通过其它方式传递

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
```

---
### References

- [TkDocs-a first example](http://www.tkdocs.com/tutorial/firstexample.html)
- [Py doc: Tkinter](https://docs.python.org/2/library/tkinter.html)
- [W3C schoool ref](http://www.w3cschool.cc/python/python-gui-tkinter.html)
- [Python 下用 Tkinter 制作 GUI](http://pikipity.github.io/blog/python-tkinter.html)