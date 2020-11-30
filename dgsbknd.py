# Git 创建仓库
# 1、CSDN Git教程(完整)
# https://blog.csdn.net/weixin_42152081/article/details/80558282?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160635101819724816611948%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160635101819724816611948&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-80558282.first_rank_ecpm_v3_pc_rank_v2&utm_term=git&spm=1018.2118.3001.4449
# 2、菜鸟git简明指南
# https://www.runoob.com/manual/git-guide/
# 3、菜鸟教程
# https://www.runoob.com/git/git-create-repository.html

# 显示当前的 git 配置信息(加“--global”针对所有仓库)
# git config --global

# 设置名字和Email地址。
# $ git config --global user.name "Your Name"
# $ git config --global user.email "email@example.com"

# 查看用户名和密码
# $ git config user.name
# $ git config user.email

# $ mkdir learngit //创建一个名叫learngit的空目录
# $ cd learngit //把learngit设置为当前目录
# $ pwd //查看当前目录

# 初始化
# git init ***目录

# 添加文件到暂存区。
# git add

# 查看仓库当前的状态
# git status

# 查看修改文件情况
# git diff readme.txt

# 将暂存区内容提交到仓库中。
# git commit -m “文件名”
# git push -u origin master  //

# 查看历史记录
# git log 
# git log --oneline //l历史记录简洁版
# git log --pretty=oneline //一大串数字是 commit id

# 退回到上一个版本
# git reset --hard HEAD^

# 查看内容
# cat readme.txt

# 回到最新的版本
# git reset --hard 1094a//这里不能用HEAD而必须使用 commit id

# 把readme.txt文件在工作区的修改全部撤销。
# git checkout -- readme.txt

# git reset命令既可以回退版本，也可以把暂存区的修改回退到工作区
# git reset HEAD readme.txt
# git checkout -- readme.txt

# 删除test.txt
# rm test.txt
# git commit -m "132"

# 重命名
# git mv

# 生成ssh
 # ssh-keygen

# 删去原有的远程源
# git remote rm origin

# 添加远程源
# git remote add origin git@github.com:dgsbknd/new.git
# git remote add origin git@github.com:dgsbknd/hellowrld.git

# 提交到远程源
# git branch -M main
# 第一次
# git push -u origin main
# git push origin master

# 使用 git clone 从现有 Git 仓库中拷贝项目
# git clone https://github.com/dgsbknd/new.git
# git clone /path/to/repository
# git clone username@host:/path/to/repository

# 生成其他分支 feature_x 并转入
# git checkout -b feature_x
# 生成分支
# git branch testing

# 切换回主分支：
# git checkout master

# 列出分支
# git branch

# 再把新建的分支删掉：
# git branch -d feature_x


# 更新本地仓库到最新改动
# git pull

# 合并其他分支到你的当前分支
# git merge 

# 手动合并
# git add <filename>

# 查看俩个分支的差异性
# git diff main feature_x

# 标签
# git log  //获取id标签前10位

# 创建一个叫做 1.0.0 的标签
# git tag 1.0.0 524c8435dd

# 图形化
# gitk

# 彩色的 git 输出
# git config color.ui true

# 显示历史记录时，每个提交的信息只显示一行
# git config format.pretty oneline

# 交互式添加文件到暂存区
# git add -i

# 从远程获取代码
# git fetch

