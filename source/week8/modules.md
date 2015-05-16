# Basics of Modules

## Outline 
- 一个来自实践的问题: 如何导入不同文件夹的文件作为 module?
  - 原型中把几个文件放置在同一个文件夹中, 避免了不同文件夹的访问方式问题
  ```
  import function0_UI
  import function0_input
  import function0_process
  import function0_output
  ```
  - It does not scale! 项目规模增大后并不是好选择. 应分开几个文件夹放置, 便于管理, 理解与使用
  - google 后, 迅速回到 py doc, 通读 Modules 章节后基本理解; 更多例子见 PEP 0328
```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
    Users of the package can import individual modules from the package, for example:
    `import sound.effects.echo`
    This loads the submodule sound.effects.echo. It must be referenced with its full name.
    `sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)`
    An alternative way of importing the submodule is:

    `from sound.effects import echo`
    This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:
    `echo.echofilter(input, output, delay=0.7, atten=4)`
    Yet another variation is to import the desired function or variable directly:

    `from sound.effects.echo import echofilter`
    Again, this loads the submodule echo, but this makes its function echofilter() directly available:
    `echofilter(input, output, delay=0.7, atten=4)`
    
  - 对于目前版本, 使用 import folder.module 格式即可, 还不需要进行相对引用.
  
```
iDoulist/                          Top-level package
      __init__.py 
      function0_MVP.py
      input/  
              __init__.py
              function0_input.py
              ...
      output/
              __init__.py
              function0_output.py
              ...
      ...
```

  ```
  import UI.function0_UI
  import input.function0_input
  import process.function0_process
  import output.function0_output
  ```
  ```
  from UI import function0_UI
  from input import function0_input
  from process import function0_process
  from output import function0_output
  ```

- 小结
   - 又一次从实践中遇到问题的学习过程
   - 两点老调重弹
     - 学习者不应幻想自己全都会 ---- 首先要接受事实, 接受随时可能发现新问题
       - 最基础的原则: 不应脱离现实
       - 另外, 接受"自己有很多不懂的地方"并不是坏事
       - 要有随时学习新事物的觉悟和信心
       - 行动方面(不只是编程呦!), 不要慌张, 先平静心态接受事实(也不过分解读), 再用自己的常识分解问题尝试解决
       - 也许应该总结为一种 "学习者态度"
     - 学习时的路径记录(常用姿势)
       - 过了一段时间, 感觉这次就又忘得差不多了..
       - 再记录一次, 常常 google - stackoverflow - python doc
       - 写下来贴显示器

## Ref.
- [Py doc](https://docs.python.org/2/tutorial/modules.html)
- [PEP 0328 -- Imports: Multi-Line and Absolute/Relative](https://www.python.org/dev/peps/pep-0328/)