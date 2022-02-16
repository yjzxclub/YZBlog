---
title: 使用Github Pages搭建个人博客
categories:
  - [教程, Github]
  - [计算机社, GCVillager]
tags:
  - 教程
  - Github
date: 2022-02-16 16:23:12
author: GCVillager
cover:
copyright: false
---

来源：https://www.cnblogs.com/sqchen/p/10757927.html
暂未获得作者授权且不知道是否允许转载，如有侵权请联系gcv8040@qq.com。	

## 一、环境准备

使用Github Pages搭建个人博客，一劳永逸，可以让我们更加专注于博客的撰写。博客的更新是通过将新建或改动的博客放在指定文件夹并推送到远程Github仓库来完成的，所以我们本地需要有Git环境，如果还没有安装Git，可以看下面的文章：

1.  [安装Git](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137396287703354d8c6c01c904c7d9ff056ae23da865a000)
2.  [Git关联远程GitHub仓库](https://www.cnblogs.com/jiechn/p/4615520.html)

## 二、搭建博客

### 1、新建仓库

![](20190423153247380.png)

以`username.github.io`作为仓库名字。

### 2、本地克隆

本地创建文件夹，用于存放远程仓库，打开所创建的文件夹，右键选择`git bash here`，表示在当前目录打开`git bash`程序，然后执行如下命令，将刚才创建的仓库克隆到本地：

`git clone https://github.com/AmazingChen/amazingchen.github.io.git`

如果`步骤1`中创建仓库时，没有勾选`Initialize this repository with a README`，将有如下提示：

![](20190423155056500.png)

warning，可以忽略，或手动在远程仓库创建一个`readme.md`，然后重新`clone`。

### 3、新建主页

在仓库文件夹下创建`index.html`：
```
<!DOCTYPE html>
<html>
	<head>

	</head>
	<body>
	<p>hello, my first page!</p>
	</body>
</html>

```

### 4、推送到远程仓库

在仓库文件夹下，右键选择`git bash here`，然后执行命令：

```
git add --all
git commit -m "add index.html"
git push origin master
```

### 5、验证

成功push到远程仓库后，访问 `username.github.io`，看到如下界面，就表示成功通过Github Pages搭建了个人的博客。

![](20190423155722798.png)

## 三、更换主题

上面裸奔的博客主页，跟原始人类一样，你一定不满意，我们穿越几千年文明，直接站在巨人的肩膀上，选一套主题吧。

Github Pages基于Jekyll构建，**[Jekyll](http://jekyllcn.com/)** 可以帮助我们把纯文本转换为静态博客网站，实现一劳永逸。

你可以在[JekyllThemes](http://jekyllthemes.org/page5/)找到喜欢的主题，也可以在其他地方找。

**"I want you, [Vno-Jekyll](https://github.com/onevcat/vno-jekyll)."** 我选择Vno。

### 1、下载主题

![](20190423160921693.png)

下载后，首先将我们仓库文件夹下的文件清空，但是要保留`.git`文件夹：

![](20190423161305626.png)

然后将下载的主题压缩包解压到仓库文件夹下，结果如下：

![](20190423161425422.png)

访问 [Jekyll-目录结构](http://jekyllcn.com/docs/structure/) 详细了解每个文件夹的功能：

```
├── _config.yml
├── _drafts
|   ├── begin-with-the-crazy-ideas.textile
|   └── on-simplicity-in-technology.markdown
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   └── post.html
├── _posts
|   ├── 2007-10-29-why-every-programmer-should-play-nethack.textile
|   └── 2009-04-26-barcamp-boston-4-roundup.textile
├── _site
├── .jekyll-metadata
└── index.html
```

### 2、搭建Jekyll环境

只有主题文件是不够的，我们需要搭建Jekyll环境，通过遵循Jekyll的规范，让Jekyll帮助我们生成静态网站。

（1） 安装Ruby：[Ruby安装教程](https://www.ruby-lang.org/zh_cn/documentation/installation/)  
注：需要安装带有devkit的版本哦！  

（2）打开CMD，执行命令安装Jekyll：

```gem install jekyll```

（3）进入仓库文件夹，执行命令：

```bundle install```

注意，必须进入仓库文件夹下再执行上述命令，否则会有如下提示，表示bundle找不到gemfile文件：

![](20190423163300527.png)
> Rails 3中引入Bundle来管理项目中的所有Gem依赖，该命令只能在一个含有Gemfile的目录下执行，`bundle install` 命令将尝试更新系统中已存在的gem包。更多参考：[bundle install 命令](https://blog.csdn.net/huaishu/article/details/38778777)

（4）启动Jekyll服务

```bundle exec jekyll serve```


启动Jekyll服务时，可能会遇到如下错误：

```  Conversion error: Jekyll::Converters::Scss encountered an error
    while converting 'css/main.scss':
                    Invalid GBK character "\xE2" on line 10
jekyll 3.4.0 | Error:  Invalid GBK character "\xE2" on line 10
```

很明显，是编码问题，参考网上方法[解决 Invalid GBK character "\xE2" 过程中的发现](https://yangaijun.com/2017/04/05/problem-solved.html)，找到`D:\RailsInstaller\Ruby2.3.3\lib\ruby\gems\2.3.0\gems\sass-3.7.2\lib\sass.rb`文件，在`require后`追加：

```Encoding.default_external = Encoding.find('utf-8')```

然后重新启动Jekyll服务，看到如下打印，表示启动成功：

![](2019042316455187.png)

（5）验证

访问 `http://127.0.0.1:4000`，当你发现你的博客首页从一个原始人变成光鲜亮丽的现代人时，表示博客主题已经应用成功了。

（6）推送到远程仓库

做完上述操作后，由于还没有将修改提交到远程仓库，所以当你访问`username.github.io`时，你看到的还是一个光溜溜的原始人，执行以下命令完成进化吧皮卡丘：

```
git add .
git commit -m "apply theme"
git push origin master
```

成功推送到远程仓库后，等待几分钟，访问`username.github.io`，OK，成功。天黑请闭眼，有问题请留言。

## 四、发布博客

在仓库文件夹下，进入`_posts`目录，所有的文章都必须放在`_posts`文件夹下，访问 [Jekyll-目录结构](http://jekyllcn.com/docs/structure/) 详细了解每个文件夹的功能。

以markdown文档为例，按照如下格式创建md文件。

`yyyy-MM-dd-filename.md`

![](20190423165839423.png)

完成后push到远程仓库，即可完成更新。

## 五、修改主题

将网站的信息改成自己的，修改`_config.yml`文件：

```
# Basic
title: 陈贤靖
subtitle: 井与陆地，海和岛屿。
description: Android Developer.
creator: <a href="http://onev.cat">@onevcat</a>

url: "https://amazingchen.github.io/#blog"

permalink: /:year/:month/:title/

# Format
highlighter: rouge

# supported colors: blue, green, purple, red, orange or slate. If you need clear, leave it empty.
# cover_color: red

# The blog button should not be removed.
blog_button:
    title: Blog
    description: Visit blog

# Navigation buttons in the front page.
nav:
    - {title: Projects, description: My Projects, url: 'https://github.com/AmazingChen/VHabit'}
    # - {title: Another Button, description: A button, url: 'http://example.com'}

# Pagination
plugins: [jekyll-paginate]
paginate: 10
paginate_path: "page/:num/"

# Comment
comment:
    disqus: vno-jekyll
    # duoshuo: 
    
# Social
social:
    github: AmazingChen
    mail: shixianjingla@gmail.com

# Google Analytics
ga:
    # id: your_ga_id
    # host: your_host


```

如果你对这套主题不太满意，并且具备web基础，可以动手修改。

![](20190423170433644.png)

如果不想博客数据被人轻易获取，建议将github仓库设置为私有。

![](20190423172927155.png)

修改之后，我的博客长这样：[陈贤靖](https://amazingchen.github.io/)

![](1304055-20190423204105158-1779179352.png)
![](1304055-20190423204340426-955895345.png)

完。