---
title: Markdown 教程
categories:
  - [教程, Markdown]
tags:
  - 教程
  - Markdown
date: 2021-09-08 13:15:09
author:
cover:
---

Markdown 是一种轻量级的标记语言，兼容 HTML ，常常用来编写一些简单的带格式文本。它格式简单易懂，并且贴近自然语言，适合编写简单的文档（而不是用 Word）。

## 标题

让我们先从标题开始。Markdown 的标题是从 `#` 开始的，一共分成六级。一般情况下，一级标题只用一次，作为一个文章的大标题，然后各种标题按照级别嵌套，有点像语文书里面有些带小标题的文章。

<table><thead><tr><th>Markdown语法</th>  <th>预览效果</th></tr></thead> <tbody><tr><td><code ># 标题 1</code></td> <td><h1 data-toc-skip="" >标题 1</h1></td></tr> <tr><td><code >## 标题 2</code></td>  <td><h2 data-toc-skip="" >标题 2</h2></td></tr> <tr><td><code >### 标题 3</code></td> <td><h3 data-toc-skip="" >标题 3</h3></td></tr> <tr><td><code >#### 标题 4</code></td> <td><h4 >标题 4</h4></td></tr> <tr><td><code >##### 标题 5</code></td> <td><h5 >标题 5</h5></td></tr> <tr><td><code >###### 标题 6</code></td>  <td><h6 >标题 6</h6></td></tr></tbody></table>

大概就是这样子了。一般情况下面我们在标题的 `#` 和标题之间打上一个空格，防止有时候一些编辑器不兼容。

## 段落和换行

Markdown 中的段落之间是需要至少一行空行来分割的。如果直接换行而没有空行，就会导致这两段实际上是一段，然后就不会换行。比如下面的例子

<table>
<th>Markdown</th> <th>显示效果</th>
<tr>

<td>
<p>我是第一段。</p><p>我是第二段。</p><p>我是第三段。<br>我也是第三段。</p>
</td>
<td>
<p>我是第一段。</p>
<p>我是第二段。</p>
<p>我是第三段。
我也是第三段。</p>
</td>
</tr>
</table>


如果要在紧挨着的两行之间换行，需要在前一行的末尾打两个空格，或者在末尾加上 HTML 的 `<br>` ，就像下面这样

```
我是第四段。<br>
我也是第四段。
```

## 强调语法

Markdown 里面可以给字加上**粗体**或者*斜体*来进行强调，或者也可以***粗体和斜体***。比如这样

```markdown
Markdown 里面可以给字加上**粗体**或者*斜体*来进行强调，或者也可以***粗体和斜体***。
```

## 引用语法

要创建块引用，请在段落前添加一个 > 符号。

```markdown
> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut

```

渲染效果如下所示：

> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut

块引用可以包含多个段落。为段落之间的空白行添加一个 > 符号。

```markdown
> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
>
>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
```

渲染效果如下：

>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
>
>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut


块引用可以嵌套。在要嵌套的段落前添加一个 >> 符号。

``` markdown
>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
>
>>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
```

渲染效果如下：

>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
>
>>  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut

## 列表语法

Markdown 的列表语法有有序列表和无序列表。有序列表是带数字的列表，就像这样

<table ><thead ><tr><th>Markdown语法</th> <th>预览效果</th></tr></thead> <tbody><tr><td><code >
        1. First item<br>
        2. Second item<br>
        3. Third item<br>
        4. Fourth item
      </code></td> <td><ol><li>First item</li> <li>Second item</li> <li>Third item</li> <li>Fourth item</li></ol></td></tr> <tr><td><code >
          1. First item<br>
          1. Second item<br>
          1. Third item<br>
          1. Fourth item
        </code></td>  <td><ol><li>First item</li> <li>Second item</li> <li>Third item</li> <li>Fourth item</li></ol></td></tr> <tr><td><code >
          1. First item<br>
          8. Second item<br>
          3. Third item<br>
          5. Fourth item
        </code></td>  <td><ol><li>First item</li> <li>Second item</li> <li>Third item</li> <li>Fourth item</li></ol></td></tr> <tr><td><code >
          1. First item<br>
          2. Second item<br>
          3. Third item<br>
          &nbsp;&nbsp;&nbsp;&nbsp;1. Indented item<br>
          &nbsp;&nbsp;&nbsp;&nbsp;2. Indented item<br>
          4. Fourth item
        </code></td>  <td><ol><li>First item</li> <li>Second item</li> <li>Third item
            <ol><li>Indented item</li> <li>Indented item</li></ol></li> <li>Fourth item</li></ol></td></tr></tbody></table>

无序列表是由 `-` （减号）开头的，和有序列表格式一样

<table ><thead ><tr><th>Markdown语法</th> <th>预览效果</th></tr></thead> <tbody><tr><td><code>
        - First item<br>
        - Second item<br>
        - Third item<br>
        - Fourth item
      </code></td> <td><ul><li>First item</li> <li>Second item</li> <li>Third item</li> <li>Fourth item</li></ul></td></tr> <tr></table>

##  Markdown 代码语法

Markdown 的代码用一对 \` （键盘左上角那个点号）来包裹，比如 `code` 就可以用 \`code\` 来指定。（这里之所以能直接打出这个符号是因为用了转义）。

如果需要多行代码则要通过一行独立的三个 \`\`\` 来开始，再一行独立的 \`\`\` 结束。比如下面的

> \`\`\`  
> 我是一个跨行代码  
> \`\`\`  

显示出来就是

``` markdown
我是一个跨行代码
```

还可以在首行的三点之后打上高亮的语言。

## 链接和图片

链接和图片都很简单。下面是示例

``` markdown

这是一个链接 [Markdown语法](https://markdown.com.cn)
这是另一个链接 <https://https://markdown.com.cn>
这是一个图片![一个图片](文件名或者 URL)

```

显示出来就是

这是一个链接 [Markdown语法](https://markdown.com.cn)  
这是另一个链接 <https://https://markdown.com.cn>  
这是一个图片（图片没指定，所以显示不了）。

## 分割线

直接打三个以上的 `---` （减号） 或者 `___`（下划线）。

---

___

## 转义

可以在特殊字符前面加上反斜杠（`\`)来进行转义，比如

```markdown
一个没有了的\*\*强调\*\*，一个没有了的\*斜体\*。
```

一个没有了的\*\*强调\*\*，一个没有了的\*斜体\*。

## 结尾

大概就是这样子了，应该没啥问题。部分内容参考自 <https://markdown.com.cn/> ，有啥问题也可以去查这个网站。
