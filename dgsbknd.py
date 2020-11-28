# Git 创建仓库
# https://www.runoob.com/git/git-create-repository.html
# https://blog.csdn.net/weixin_42152081/article/details/80558282?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160635101819724816611948%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160635101819724816611948&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-80558282.first_rank_ecpm_v3_pc_rank_v2&utm_term=git&spm=1018.2118.3001.4449


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
# git log --pretty=oneline //一大串数字是 commit id

# 退回到上一个版本
# git reset --hard HEAD^

# 查看内容
# cat readme.txt

# 回到最新的版本
# git reset --hard 1094a//这里不能用HEAD而必须使用 commit id




# 使用 git clone 从现有 Git 仓库中拷贝项目
# git clone

# 显示当前的 git 配置信息
# git config



