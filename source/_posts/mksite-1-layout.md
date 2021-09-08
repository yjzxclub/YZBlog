---
title: CSS进阶——布局
categories:
  - [教程, CSS进阶]
tags:
  - 教程
  - CSS进阶
date: 2021-09-08 21:12:19
author:
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Introduction>

本文基于 CC-BY-SA 4.0 协议发布。

## 前言

接下来，我们就要开始正经的网页实战了。我们将会把 HTML 和 CSS 综合起来，用来构建一些实际的网站，这样就可以真正做出能够看的网页了（要"能用"还少个 JavaScript）。

## 正常布局流

在搭建网页之前，先要了解的是布局。有这个概念，以后才可以统筹全局。

我们建议始终使用 CSS 方式进行布局，虽然看起来可能会有点麻烦，但是绝对比用 HTML 的 `table` 来进行所谓的排版好得多，因为表格会破坏网站的语义，导致维护困难。

正常布局流(normal flow)是指在不对页面进行任何布局控制时，浏览器默认的HTML布局方式。让我们快速地看一个HTML的例子：

``` html
<p>I love my cat.</p>

<ul>
  <li>Buy cat food</li>
  <li>Exercise</li>
  <li>Cheer up friend</li>
</ul>

<p>The end!</p>
```

显示起来应该是这样的:

![NP](1_normal-page.png)

一个朴实无华的网页。

在这里 HTML 元素完全按照源码中出现的先后次序显示——第一个段落、无序列表、第二个段落。

出现在另一个元素下面的元素被描述为块元素，与出现在另一个元素旁边的内联元素不同，内联元素就像段落中的单个单词一样。（你应该还记得之前的盒模型吧）。

注意：块元素内容的布局方向被描述为块方向。块方向在英语等具有水平书写模式(writing mode)的语言中垂直运行。它可以在任何垂直书写模式的语言中水平运行。对应的内联方向是内联内容（如句子）的运行方向。

当你使用 css 创建一个布局时，你正在离开正常布局流，但是对于页面上的多数元素，正常布局流将完全可以创建你所需要的布局。这也是为什么要保持 HTML 的良好结构的原因，不然就容易出现一些不好修复的问题。

下列布局技术会覆盖默认的布局行为：

- display 属性——标准的 value, 比如 block, inline 或者 inline-block 元素在正常布局流中的表现形式 (见 Types of CSS boxes). 接着是全新的布局方式，通过设置 display 的值, 比如 CSS Grid 和 Flexbox.
- 浮动——应用 float 值，诸如 `left` 能够让块级元素互相并排成一行，而不是一个堆叠在另一个上面。
- position 属性 — 允许你精准设置盒子中的盒子的位置，正常布局流中，默认为 `static` ，使用其它值会引起元素不同的布局方式，例如将元素固定到浏览器视口的左上角。
- 表格布局——表格的布局方式可以用在非表格内容上，可以使用 `display: table` 和相关属性在非表元素上使用。
- 是多列布局——这个 Multi-column layout 属性 可以让块按列布局，比如报纸的内容就是一列一列排布的。

看起来有点复杂，不过没有关系，下面我们会讲得更详细的。

## display 属性

在 css 中实现页面布局的主要方法是设定 display 属性的值。此属性允许我们更改默认的显示方式。正常流中的所有内容都有一个 display 的值，用作元素的默认行为方式。例如，英文段落显示在一个段落的下面，这是因为它们的样式是 `display:block` （也就是块级元素）。如果在段落中的某个文本周围创建链接，则该链接将与文本的其余部分保持内联，并且不会打断到新行。这是因为 `<a>` 元素默认为 `display:inline`，表现为内联元素。

您可以更改此默认显示行为。例如，`<li>` 元素默认为display:block，这意味着在我们的英文文档中，列表项显示为一个在另一个之下。如果我们将显示值更改为inline，它们现在将显示在彼此旁边，就像单词在句子中所做的那样。事实上，您可以更改任何元素的display值，这意味着您可以根据它们的语义选择 html 元素，而不必关心它们的外观。他们的样子是你可以改变的。

除了可以通过将一些内容从 block 转换为 inline（反之亦然）来更改默认表示形式之外，还有一些更大的布局方法以 display 值开始。但是，在使用这些属性时，通常需要调用其他属性。在讨论布局时，对我们来说最重要的两个值是 `display:flex` 和 `display:grid`。

## 弹性盒子(Flexbox)

Flexbox 是CSS 弹性盒子布局模块（Flexible Box Layout Module）的缩写。它被专门设计出来用于创建横向或是纵向的一维页面布局。要使用flexbox，你只需要在想要进行flex布局的父元素上应用display: flex ，所有直接子元素都将会按照flex进行布局。我们来看一个例子。

下面这些HTML标记描述了一个 `class` 为 `wrapper` 的容器元素，它的内部有三个<div>元素。它们在我们的英文文档当中，会默认地作为块元素从上到下进行显示。

现在，当我们把 `display: flex` 添加到它的父元素时，这三个元素就自动按列进行排列。这是由于它们变成了 flex 项(flex items)，按照 flex 容器（也就是它们的父元素）的一些 flex 相关的初值进行 flex 布局：它们整整齐齐排成一行，是因为父元素上 `flex-direction` 的初值是 `row` 。它们全都被拉伸至和最高的元素高度相同，是因为父元素上 `align-items` 属性的初值是 `stretch` 。这就意味着所有的子元素都会被拉伸到它们的 flex 容器的高度，在这个案例里就是所有 flex 项中最高的一项。所有项目都从容器的开始位置进行排列，排列成一行后，在尾部留下一片空白。

从 MDN 语言翻译成人话就是，给这个 `wrapper` 设置 `display: flex` 之后，它里面的子元素就会变成弹性盒子。根据弹性盒子的默认属性，子元素会被排成横着的一行，按照自己的大小自动排列，在后面留下空白。

``` css
.wrapper {
  display: flex;
}
```

``` html
<div class="wrapper">
  <div class="box1">One</div>
  <div class="box2">Two</div>
  <div class="box3">Three</div>
</div>
```

![Example1](1_flexexp1.png)

除了刚刚的属性，还有很多属性可以用在 flex items 上面。他们可以改变 flex 项在 flex 布局中占用宽/高的方式，允许它们通过伸缩来适应可用空间。

作为一个简单的例子，我们可以在我们的所有子元素上添加 flex 属性，并赋值为 `1` ，这会使得所有的子元素都伸展并填充容器，而不是在尾部留下空白。它们会调整自己的大小，直到占用相同宽度的空间。比如你的容器太小，它们就会把自己变小，刚好把容器填满。

``` css
.wrapper {
    display: flex;
}
.wrapper > div {
    flex: 1;
}
```

``` html
<div class="wrapper">
    <div class="box1">One</div>
    <div class="box2">Two</div>
    <div class="box3">Three</div>
</div>
```

![Example1](1_flexexp2.png)

## Grid 布局

Flex 排列单列的时候，固然是很不错的，但是你要排很多东西的时候，一列排不下，就需要用到 Grid。Grid 可以用来按行和列排列你的 HTML 元素。

同flex一样，你可以通过指定 display 的值来转到 grid 布局： `display: grid` 。下面的例子使用了与flex例子类似的HTML标记，描述了一个容器和若干子元素。除了使用 `display:grid` ，我们还分别使用 `grid-template-rows` 和 `grid-template-columns` 两个属性定义了一些行和列的轨道。定义了三个1fr的列，还有两个100px的行之后，无需再在子元素上指定任何规则，它们自动地排列到了我们创建的格子当中。

``` css
.wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 100px 100px;
    grid-gap: 10px;
}
```

``` html
<div class="wrapper">
    <div class="box1">One</div>
    <div class="box2">Two</div>
    <div class="box3">Three</div>
    <div class="box4">Four</div>
    <div class="box5">Five</div>
    <div class="box6">Six</div>
</div>
```

![grid](1_grid.png)

有了一个 grid 之后，你也可以显式地将元素摆放在里面，而不是依赖于浏览器进行自动排列。在下面的第二个例子里，我们定义了一个和上面一样的 grid ，但是这一次我们只有三个子元素。我们利用 `grid-column` 和 `grid-row` 两个属性来指定每一个子元素应该从哪一行/列开始，并在哪一行/列结束。这就能够让子元素在多个行/列上展开。

``` css
.wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 100px 100px;
    grid-gap: 10px;
}
.box1 {
    grid-column: 2 / 4;
    grid-row: 1;
}
.box2 {
    grid-column: 1;
    grid-row: 1 / 3;
}
.box3 {
    grid-row: 2;
    grid-column: 3;
}
```

``` html
<div class="wrapper">
    <div class="box1">One</div>
    <div class="box2">Two</div>
    <div class="box3">Three</div>
</div>
```

![Grid2](1_grid2.png)

这篇指南的其余部分介绍了其他的布局方式，它们与你的页面的主要布局结构关系不大，但是却能够帮助你实现特殊的操作。同时，只要你理解了每一个布局任务的初衷，你就能够马上意识到哪一种布局更适合你的组件。

## Float

把一个元素“浮动”(float)起来，会改变该元素本身和在正常布局流（normal flow）中跟随它的其他元素的行为。这一元素会浮动到左侧或右侧，并且从正常布局流(normal flow)中移除，这时候其他的周围内容就会在这个被设置浮动(float)的元素周围环绕。

float 属性有四个可选的值：

- `left` — 将元素浮动到左侧。
- `right` — 将元素浮动到右侧。
- `none` — 默认值, 不浮动。
- `inherit` — 继承父元素的浮动属性。

听起来有点绕，不过看个例子就懂了。下面 Show Code 。在下面这个例子当中，我们把一个 `<div>` 元素浮动到左侧，并且给了他一个右侧的 margin，把文字推开。这给了我们文字环绕着这个 `<div>` 元素的效果。

``` css
.box {
    float: left;
    width: 150px;
    height: 150px;
    margin-right: 30px;
}
```

``` html
<h1>Simple float example</h1>
<div class="box">Float</div>
<p> Lorem ipsum dolor sit amet, consectet（以下为了节省纸张保护树木省略）……</p>
```

![Float](1_float.png)

## 表格布局

首先声明，对于一个现代的网站，不要表格对整个网页进行布局，除非想给某些上古时代的伟大遗产做支持，因为表格会破坏网站的语义。出于历史遗留原因，我们也略微带过这样的形式。

一个 `<table>` 标签之所以能够像表格那样展示，是由于 CSS 默认给 `<table>` 标签设置了一组 table 布局属性。当这些属性被应用于排列非 `<table>` 元素时，这种用法被称为“使用 CSS 表格”。

让我们来看一个例子。首先，创建 HTML 表单的一些简单标记。每个输入元素都有一个标签，我们还在一个段落中包含了一个标题。为了进行布局，每个标签/输入对都封装在 `<div>` 中。

``` html
<form>
  <p>First of all, tell us your name and age.</p>
  <div>
    <label for="fname">First name:</label>
    <input type="text" id="fname">
  </div>
  <div>
    <label for="lname">Last name:</label>
    <input type="text" id="lname">
  </div>
  <div>
    <label for="age">Age:</label>
    <input type="text" id="age">
  </div>
</form>
```

``` css
html {
  font-family: sans-serif;
}
form {
  display: table;
  margin: 0 auto;
}
form div {
  display: table-row;
}
form label, form input {
  display: table-cell;
  margin-bottom: 10px;
}
form label {
  width: 200px;
  padding-right: 5%;
  text-align: right;
}
form input {
  width: 300px;
}
form p {
  display: table-caption;
  caption-side: bottom;
  width: 300px;
  color: #999;
  font-style: italic;
}
```

![](1_table.png)

## 多列布局

多列布局模组给了我们 一种把内容按列排序的方式，就像文本在报纸上排列那样。由于在web内容里让你的用户在一个列上通过上下滚动来阅读两篇相关的文本是一种非常低效的方式，那么把内容排列成多列可能是一种有用的技术。

要把一个块转变成多列容器(multicol container)，我们可以使用  `column-count` 属性来告诉浏览器我们需要多少列，也可以使用 `column-width` 来告诉浏览器以至少某个宽度的尽可能多的列来填充容器。

在下面这个例子中，我们从一个 `class` 为 `container` 的 `<div>` 容器元素里边的一块 HTML 开始。

我们指定了该容器的 `column-width` 为200像素，这让浏览器创建了尽可能多的200像素的列来填充这一容器。接着他们共同使用剩余的空间来伸展自己的宽度。

``` HTML
<div class="container">
    <h1>Multi-column layout</h1>
    <p>节约纸张人人有责</p>
</div>
```

``` css
.container {
    column-width: 200px;
}
```

![](1_multi.png)

## 最后

布局总算是讲完了，这么多内容要一下子掌握是不可能的，有个大概印象，知道以后搞网页要查什么资料就行。接下来我们会给出更具体的例子给大家，希望能够起到作用。
