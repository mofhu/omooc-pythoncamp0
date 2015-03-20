# Git learning log

## Objectives:

### minimal commands for git starter in terminal

### enough commands for git in terminal

Let's begin!

### at terminal

0. `git init`

	in right folder first.

1. `git add <file>`
	
	we can use "*", etc.

	eg. git add "*.md"

2. `git commit`

	need some details

	`git commit -m "the description of changes, will be shown in logs, so it's important"`

	`git commit -a -m "description"`

		commit all changes ONLY in files git has already managed. (i.e. not applied to files not added. so to apply all changes, using git add before git commit.)

3. `git status`

4. `git diff`

5. `git log`

6. on deleting 

	`git rm`

		`git checkout`  can be used for replacing files in working folder.

6. On resetting

	`git reset --hard commit_id`

		HEAD: this version

		HEAD^, HEAD^^, HEAD~100

		>normal commit id: commit 31dc03905a9866775fe45ac8ae22382c685ce66e

	`git log`

		to get commit id.

	`git reflog`

		to get to a later version.


### remote, push and pull

1. `git remote add origin <link>`

2. first push 
	
	`git push -u origin master`

	`git push origin master`

		for later pushes