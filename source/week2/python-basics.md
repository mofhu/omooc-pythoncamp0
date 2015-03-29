# Python basics

## Objectives

- Minimum thing to work with python for me (with basic skill of C)
- Method: an MVP first, fast iteration and editing in work

## Short Reminders

- Types: string, int, list, dict
- Function
- if/for
- Basic grammar and style


## Outline

### 1. Types
### 2. Function

- 2.1 objectives

  - 一个独立功能模块,封装便于反复使用
  - 利用参数和返回值(或全局变量)**传递数据**

- 2.2 grammar
  - define 
  
			def function(argv1[, argv...]):		
					body
  		 		[return value] 	

  - 注意冒号
  - local/global variables
  
### 3. if/for

- if

    	if secret_number == guess:
	    	A
    	elif secret_number > guess:
	    	B
    	else:
	    	C

- for in
	
		for i in list:
			do something
			
### 4. Basic grammar & style

- 缩进
  - python 使用缩进标记语法层次
  - 建议用四空格,不要用 tab 缩进

- 冒号
- 建议命名风格

  - 类命名使用单个词首字母大写，例如CamelCase，缩写的名称全部大写，例如：HTTPWriter，而不是：HttpWriter
  - 变量名：lowercase_with_underscores
  - 方法和函数名：lowercase_with_underscores
  - 常量：UPPERCASE_WITH_UNDERSCORES
  - 编译的正则表达式：name_re



## Resources
 
- [Quick figure](http://wiki.woodpecker.org.cn/moin/ZqQuickIntoPy)
- [Learning python the hard way](http://www.jb51.net/shouce/Pythonbbf/latest/index.html)
- [Python documentation](https://docs.python.org/3.4/index.html)
- [Python style guide](https://www.python.org/dev/peps/pep-0008/#indentation)