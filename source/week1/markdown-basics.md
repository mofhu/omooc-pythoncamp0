# Markdown Basics


## Quick Reminders
* 标题 #
* 引用 >
* 粗体斜体 成对*
* 列表 - 或 1.
* 代码块 成对 `
* 链接 \[显示文字](链接)
* 反义符 \


## Main
- Basics
- More

### Basics
* 不同级别标题

    `# 的个数是不同级别的标题(1-6)`

    ># 1级标题
## 2级标题

* 引用

	`> 表示引用`
	>\>引用内容

* 粗体和斜体

	`一个 * 或 _ 表示斜体,两个表示粗体`
	
    \*\***粗体**\*\*, \_\___粗体__\_\_
    
    \**斜体*\*, \__斜体_\_

* 列表

    `- 或 * 表示无序列表, "1. " "2. "表示有序列表`
    1. `1. GitHub`   
    2. `2. Zhihu`

	* \-苹果			
	* \-橘子
	* \-香蕉

	`note: 1. GitHub 和 Mou 对列表的实现效果似乎不同; 2. 用 - 与粗斜体易区分,且按键方便,优先.`

* 嵌套列表

	`[space][space]即可表示嵌套一层`

* 代码框

	`` 一对 ` 表示一段代码, 一对 ``` 表示代码块`` 
	>插入一段`代码`
	
    插入一段\`代码\`

* 链接

	`[显示的链接文字](链接地址)`
	>[Frank Hu @ GitHub](https://github.com/Frank-the-Obscure)	
	`[Frank Hu @ GitHub](https://github.com/Frank-the-Obscure)`

* 反义符 

	反斜杠 \ 是 Markdown 中的反义符
 
### More
* 删除线(strikethrough)

    `成对波浪线~~删除文字~~`
	>~~删除文字~~

* 表格

	`使用----||||绘制表格`
	
	|Number|Name|
	
	|-|-|
	
	|1|Frank|
	
	|2|Tom|
	
    ```
    |Number| Name|
	|1|Frank|
	|2|Tom|
	```
* 待办事项(GitHub Flavored Markdown)

	`[ ] 或 [x]表示未完成未完成的任务,可嵌套`
	
	
	 - [ ] Issue 1
	 - [ ] Fix 2
	 
	

## References and Resources

* [GitHub markdown basics](https://help.github.com/articles/markdown-basics/)
* [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)
* [Writing on GitHub](https://help.github.com/articles/writing-on-github/)
* [Mou](http://25.io/mou/)
* Markdown 语法细节规定并不完全,目前不同 Markdown 编辑器的实现(扩展?)也时常不同,因此不必太过苛求细节,目前以 GitHub Flavored Markdown 为主要框架即可.