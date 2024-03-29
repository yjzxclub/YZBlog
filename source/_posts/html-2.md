---
title: HTML：2——入门
categories:
  - [教程, HTML]
  - [计算机社, GCVillager]
tags:
  - 教程
  - HTML
date: 2021-09-08 13:34:48
author: GCVillager
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics>

## 一个简单的段落

在安装好VScode，新建好一个HTML文件之后，我们就可以开始了。  
HTML里有一个重要的概念——标签(tag)。一对标签可以为一段文字或者一张图片添加超链接，将文字设置为斜体，改变字号，等等。  
比如说，现在有这样一句话：“AMD YES!”
我们可以用`<p>`标签（段落标签）把它括起来，变成：

```HTML
<p>AMD YES!</p>
```

结果就是在屏幕上单行显示一个：  
>AMD YES!  

这一段文字有以下部分：  
**开始标签**——`<p>`。它被尖括号包围，表示这个标签从这里开始起作用。比如此处就是说，从这里开始是一个段落。  
**结束标签**——`</p>`。同样也是尖括号包围，与开始标签不同的是有一个斜杠，用于区分。这个斜杠是必不可缺的，不然会出问题。这表示着元素的结尾——在本例中即段落在此结束。  
**内容**——`AMD YES`。被`<p>`和`</p>`包围的部分就是内容，会被显示出来。显示的情况会根据包围它的标签和CSS中的描述决定。  
**元素**——`<p>AMD YES!</p>`。没错，这整个语句就是一个元素。开始标签、结束标签与内容相结合，便是一个完整的元素。  

## 元素嵌套

已知有一个元素`<strong>`，能够表示括起来的内容是重要的。  
假如我是AMD的忠实粉丝，要高喊“AMD YES”的YES这个词，该怎么处理`<p>`元素里面的东西呢？我们可以让元素嵌套。具体来说，就是元素里有一个元素。  

```HTML
<p>AMD <strong>YES!</strong></p>
```

显示结果就是这样：  
> AMD **YES!**

这里，`<p>`元素里嵌套了一个`<strong>`元素，达到了这样的效果。  
必须保证元素嵌套次序正确：本例首先使用 `<p>` 标签，然后是 `<strong>` 标签，因此要先结束 `<strong>` 标签，最后再结束 `<p>` 标签。  
比如，这样就是错误的：  

```HTML
<p>AMD <strong>YES!</p></strong>                      BAD!!!
```

或者说，假如我们假设`<p>`是( )，`<strong>`是[ ]，这样是可以的：  
\[ \] \( \[ \] \( \) \)  
但是这样就是不行的：  
\( \[ \) \]  
就是说，一对括号内可以插入一整对的括号，但是不能插入括号的左半部分或者右半部分。元素嵌套也是这样。
如果你不好好写，导致了嵌套问题，你可怜的浏览器就要自己猜测这是什么。那么就会变得乱七八糟。

## 空元素

有这么一些元素，因为里面不用写什么东西（也就是没有内容），所以就没有结束标签。这就是**空元素**。比如分割线元素`<hr>`：  

```HTML
<p>3.1415926535</p>
<hr>
<p>114514</p>
```

显示起来就是：
>3.1415926535  
>
>---
>
>114514

## 元素属性

有时候，元素可以有**属性**。  
由于GCVillager是伍六七的忠实粉丝，所以这里放一张伍六七的图。  

```HTML
<img src="https://yjzx-site.github.io/img/club-file/scissor-seven-picture.jpg" 
     alt=一张伍六七的图片 width="960px" height=540px>
```

效果大概是这样：（不过图片大小没改，不要在意）  

>![一张伍六七的图片](https://cdn.jsdelivr.net/gh/yjzx-site/yjzx-site.github.io/img/club-file/scissor-seven-picture.jpg)

我们暂时不深究`<img>`元素，等会再讲。这里就了解一下元素属性。可以看出，`<img>`标签有src、alt、width、height等属性，属性的属性值（也就是等号后面跟的东西）可以是字符串，也可以是数字，或者是带单位的数字（960px代表960像素）。不包含空格（以及 " ' \` = < > 字符）的简单属性值可以不使用引号，但是建议将所有属性值用引号括起来，这样的代码一致性更佳，更易于阅读。各个属性之间用空格分隔。  

## HTML文档

在你新建的HTML中输入英文感叹号，就能看到这样的东西：  
![自动补全](./automatic-completion.png)  
这时候，你可以通过上下键进行选择，然后按下Tab键补全一段内容。同样，当你输入HTML中的标签，比如`<strong>`，你只需要输入`<str`然后按下Tab，就可以补全成`<strong`。这时候，你再把右尖括号打上，就会自动补全成`<strong></strong>`，光标处于两个标签的中间，你只需要往里面打字就好了。这个功能可以大大提高我们写HTML和CSS的效率。  
刚刚我们打感叹号补全的内容是这样的：

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

由于GCVillager太懒了，这一段全部抄MDN，改了一点点。如果看不懂也没关系。  
>`<!DOCTYPE html>` — 文档类型。混沌初分，HTML 尚在襁褓（大约是 1991/92 年）之时，DOCTYPE 用来链接一些 HTML 编写守则，比如自动查错之类。DOCTYPE 在当今作用有限，仅用于保证文档正常读取。现在知道这些就足够了。  
`<html></html>` — `<html>` 元素。该元素包含整个页面的内容，也称作根元素。所有内容都必须写在`<html></html>`标签之间。  
`<head></head>` — `<head>` 元素。该元素的内容对用户不可见，其中包含例如面向搜索引擎的搜索关键字（keywords）、页面描述、CSS 样式表和字符编码声明等。  
`<meta charset="utf-8">` — 该元素指定文档使用 UTF-8 字符编码 ，UTF-8 包括绝大多数人类已知语言的字符。基本上 UTF-8 可以处理任何文本内容，还可以避免以后出现某些问题，没有理由再选用其他编码。  
`<title></title>` — `<title>` 元素。该元素设置页面的标题，显示在浏览器标签页上，也作为收藏网页的描述文字。  
`<body></body>` — `<body>` 元素。该元素包含期望让用户在访问页面时看到的内容，包括文本、图像、视频、游戏、可播放的音轨或其他内容。  

总之就是，`<head>`元素里的内容，除了`<title>`显示在标题栏里，没有一个是可以被用户看到的，但是它们各有用途。想要被用户看到的内容需要写在`<body>`里面。  

欲知后事如何，请听下回分解。
