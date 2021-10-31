---
title: HTML：6——表格
categories:
  - [教程, HTML]
  - [计算机社, GCVillager]
tags:
  - 教程
  - HTML
date: 2021-09-08 13:34:55
author: GCVillager
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Tables/Basics>

假设怺假冢穴的段长想要统计某个段的月考成绩，需要用到excel表格。在HTML中，也有表格，不过它并不是用来统计什么的，而是给人看的。

假设我们的GXH先生开发了一款很牛逼的软件卖钱（但是GXH先生肯定不会卖钱，他只会开源），就需要这样一个表格：

![GXH浏览器购买方案](./6_table-gxh-software.png)

这味也太冲了吧！

代码如下。你可以复制到你的浏览器里试一试：

```HTML
<table>
    <tr>
        <th colspan="3"><h2>GXH安全浏览器购买方案</h2></td>
    </tr>
    <tr>
        <th><h3>试用版</h3></td>
        <th><h3>高级版</h3></td>
        <th><h3>旗舰版</h3></td>
    </tr>
    <tr>
        <td>￥0</td>
        <td>￥114514（永久）</td>
        <td>￥1919810（永久）</td>
    </tr>
    <tr>
        <td>
            <ul>
                <li>✅使用GXH安全大脑新一代浏览器保护技术</li>
                <li>❌启用GXH安全卫士</li>
                <li>❌每天无限使用时间（限时30分钟）</li>
                <li>❌去广告</li>
                <li>❌会员尊享服务</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>✅使用GXH安全大脑新一代浏览器保护技术</li>
                <li>✅启用GXH安全卫士</li>
                <li>✅每天无限使用时间</li>
                <li>❌去广告</li>
                <li>❌会员尊享服务</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>✅使用GXH安全大脑新一代浏览器保护技术</li>
                <li>✅启用GXH安全卫士</li>
                <li>✅每天无限使用时间</li>
                <li>✅去广告</li>
                <li>✅会员尊享服务</li>
            </ul>
        </td>
    </tr>
</table>
```

然而你打开浏览器一看，却是一副凄惨的景象：

![GXH浏览器购买方案](./6_table-without-css.png)

为什么这个表格没有边框？！为什么这个表格没有居中？！  
表格在默认情况下就是无边框的，也没有居中。如果需要这样的效果，就得加入CSS。  
还记得怎么加入外部CSS文件吗？请将这个链接用导入CSS的方式加入你的HTML中：

```md
https://cdn.jsdelivr.net/gh/mdn/learning-area/html/tables/basic/minimal-table.css
```

如果你忘了的话，答案在下面：  

```HTML
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/mdn/learning-area/html/tables/basic/minimal-table.css">
```

加入到`<head>`元素内。

好的，这个表格显示正常了。然后我们来逐步学习表格。  

用`<table></table>`包住的内容就是表格内容。表格是有行和列的，我们需要一行行描述，然后描述每一行的单元格。  
我们用`<tr></tr>`描述一行，用`<td></td>`描述单元格。  

```HTML
<table>
    <tr>
        <td><h3>试用版</h3></td>
        <td><h3>高级版</h3></td>
        <td><h3>旗舰版</h3></td>
    </tr>
    <tr>
        <td>￥0</td>
        <td>￥114514（永久）</td>
        <td>￥1919810（永久）</td>
    </tr>
</table>
```

我们先写一下上面这个表格。这个表格就是原先那个表格的前两行，可以看出，table嵌套tr，tr嵌套td。多个tr并列，多个td并列。

首先写一个单元格：

```HTML
    <td><h3>试用版</h3></td>
```

然后，把同一行的其他单元格都加上来：

```HTML
        <td><h3>试用版</h3></td>
        <td><h3>高级版</h3></td>
        <td><h3>旗舰版</h3></td>
```

这样一行的内容就完成了，我们把它用tr包起来：

```HTML
    <tr>
        <td><h3>试用版</h3></td>
        <td><h3>高级版</h3></td>
        <td><h3>旗舰版</h3></td>
    </tr>
```

这样的一行还有很多：

```HTML
    <tr>
        <td><h3>试用版</h3></td>
        <td><h3>高级版</h3></td>
        <td><h3>旗舰版</h3></td>
    </tr>
    <tr>
        <td>￥0</td>
        <td>￥114514（永久）</td>
        <td>￥1919810（永久）</td>
    </tr>
```

最后用table标签包起来就完事了。  

按照刚刚的方法完成了下面的表格内容，你还有一个标题。还有一个问题：最上面的大标题。如果你按照同样的方法写，那么它会缩到最左边去。如果看看我的代码，就可以发现，在开始标签里面写一个`colspan="3"`就可以让这个单元格有三格的宽度。类似的还有`rowspan`属性，是描述单元格的高度的。  
还有一个小小的问题：看我的示例代码，用到了`<th>`。这是什么？和td有什么区别？其实它也是语义化的内容。th代表标题，td代表下面的内容。这不仅有利于看代码的人理解，也对CSS渲染有好处。  

