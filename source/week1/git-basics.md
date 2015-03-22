# Git Basics

## Quick Reminders

* Set up: `git init`
* Change and commit: `git add <file>`, `git commit -am "description"`
* Find changes: `git status`, `git diff`, `git log`
* Branch and tag: `git branch (branch)`, `git checkout`, `git merge <branch>`, `git branch -d <branch>`, `git tag <tag-name>`
* Reset: `git reset --hard commit_id`
* Remote: `git remote add origin <link>`, `git clone <link>`
* Push and pull: `git push -u origin master`, `git push origin master`

A portable version of basic commands (not by me): [Git cheet sheet](git-cheat-sheet.png)


## Objectives:

* Minimal commands for Git starter in command line interface

* Enough commands for Git/GitHub

Let's begin!

## Main
### Git and GitHub
- Git 是一个分布式版本管理系统
- Git & GitHub 高效解决了多人协作开发的问题,在开源圈的应用尤为成功,或许算是当前最主流高效的开发方式

### Local

1. `git init`

	in right folder first.

2. `git add <file>`
	
	we can use "*", etc.

	eg. git add "*.md"

3. `git commit`

	need some details

	`git commit -m "the description of changes, will be shown in logs, so it's important"`

	`git commit -am (or -a -m) "description"`

	commit all changes ONLY in files git has already managed. (i.e. not applied to files not added. so to apply all changes, using git add before git commit.)

	git add and git commit

	[details](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013745374151782eb658c5a5ca454eaa451661275886c6000)

4. `git status`

5. `git diff`

6. `git log`

7. On deleting 

	`git rm` deleting file do not deleting it in git.

	`git checkout` can be used for replacing files in working folder.

8. On resetting

	`git reset --hard commit_id`

	HEAD: this version
	HEAD^, HEAD^^, HEAD~100

	>normal commit id: commit 31dc03905a9866775fe45ac8ae22382c685ce66e

	`git log`
	to get commit id.

	`git reflog`
	to get to a later version.

 9. Branching

	`git branch <branch name>`: list (without argument) and add new branch

	`git checkout`

	short command for branch and checkout: `git checkout -b <branch name>`

	`git merge <name>`: merge a branch to branch in use.

	`git branch -d <name>`: deleting a branch

	branching with conflicts: need to add later

	general branching strategy: master-dev-bugs & features

10. Tagging

	`git tag <tag-name>`

### Remote, push and pull

1. From local to remote: `git remote add origin <link>`; from remote to local: `git clone <link>`; detals `git remote -v`

2. Push 

	first push: `git push -u origin master`

	for later pushes: `git push origin master`

### GitHub
- Fork 
- Push request

## References and Resources
* [Git tutorial @ liaoxuefeng's blog](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
* [Git cheet sheet](http://www.git-tower.com/blog/assets/2013-05-22-git-cheat-sheet/cheat-sheet-large01.png)

