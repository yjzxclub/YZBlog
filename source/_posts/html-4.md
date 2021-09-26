---
title: HTML：4——标签2
categories:
  - [教程, HTML]
tags:
  - 教程
  - HTML
date: 2021-09-08 13:34:51
author: GCVillager
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content>
- <https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/Getting_started>
- <https://developer.mozilla.org/zh-CN/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals>

## 列表

现在假设我要列出Mojang Studios的几个员工，就像下面这样，该怎么做呢？

> - Jens 'Jeb' Bergensten
> - Nathan 'Dinnerbone' Adams
> - Mikael 'Slicedlime' Hedberg

代码如下，如果你要写自己的列表可以照着这个写。列表里内容数量不限，只需要再加入`<li></li>`即可。

```HTML
<ul>
    <li>Jens 'Jeb' Bergensten</li>
    <li>Nathan 'Dinnerbone' Adams</li>
    <li>Mikael 'Slicedlime' Hedberg</li>
</ul>
```

这是**无序（unordered）列表**。还有**有序（ordered）列表**：

>噼哩噼哩番剧排行（某年某月某日记录的）
>
>1. 关于我转生变成史莱姆这档事 第二季
>2. 死神少爷与黑女仆
>3. 精灵幻想记
>4. 转生成为了只有乙女游戏破灭Flag的邪恶大小姐 第二季
>5. 侦探已死

代码其实就是把`<ul>`改成`<ol>`：

```HTML
<p>噼哩噼哩番剧排行（某年某月某日记录的）</p>
<ol>
    <li>关于我转生变成史莱姆这档事 第二季</li>
    <li>死神少爷与黑女仆</li>
    <li>精灵幻想记</li>
    <li>转生成为了只有乙女游戏破灭Flag的邪恶大小姐 第二季</li>
    <li>侦探已死</li>
</ol>
```

有时候我们还会需要嵌套列表：

>Mojang Studios
>
> - 臭写代码的  
>        1. Jens 'Jeb' Bergensten  
>        2. Nathan 'Dinnerbone' Adams
> - 画画的  
>        1. Markus 'Junkboy' Toivonen  
>        2. Ninni Landin

代码也一样，像这里的话，就是让两个无序列表成为有序列表的一个`<li>`元素。

```HTML
<p>Mojang Studios</p>
<ul>
    <li>
        <p>臭写代码的</p>  
        <ol>
            <li>Jens 'Jeb' Bergensten</li>  
            <li>Nathan 'Dinnerbone' Adams</li>
        </ol>
    </li>
    <li>
        <p>画抽象画的</p>  
        <ol>
            <li>Markus 'Junkboy' Toivonen</li>  
            <li>Ninni Landin</li>
        <ol>
    </li>
</ul>
```

如果你觉得看不懂的话，可以这么理解：把这一段：

```HTML
<p>臭写代码的</p>  
    <ol>
        <li>Jens 'Jeb' Bergensten</li>  
        <li>Nathan 'Dinnerbone' Adams</li>
    </ol>
<p>
```

看成一个`这是某一段文本`的话，就和一个无序列表一样了。

## 再谈属性

灯只有“开”和“关”两个状态（谁要是跟我说“为什么没有‘坏’这个状态”，我直接把他宰了），如果把“开”当成`True`，“关”当成`False`，那么只有`True`和`False`的东西，我们称之为布尔变量。HTML中的属性也有**布尔属性**。比如说HTML中的输入框`<input>`，我们可以用这样的代码让他不能输入：

```HTML
<input type="text" disabled>
```

也就是说，有的属性可以不需要打`="xxxx"`这一串，这些属性就是布尔属性。它相当于一个开关，比如说这里就是把“disable”这个开关打开。

还有的属性是用来辨识当前元素的。假如我开了一个网络小说网站，现在有一大堆`<p>`元素，其中有的是写的文章的自然段，有的是网站的一些其他文本。现在我要给所有网文自然段加上好看的Noto Sans CJK字体（当然这需要CSS），怎么让浏览器知道哪些文本应该改字体，哪些文本不需要呢？  
我们给这些`<p>`元素标记一下，有的标记成“自然段”，有的不标记，浏览器就知道标记了的`<p>`元素需要改字体。这里就要用到HTML的一个属性——`class`。`class`就是“类”的意思。HTML的每种元素都可以带`class`属性。回到我们之前说的`<p>`元素：  

```HTML
<p class="paragraph">了解清楚计算机社是全学校最垃圾的社团到底是一种怎么样的存在，是解决一切问题的关键。 可是……</p>
```

注：上述文本由已经通过图灵测试的狗屁不通文章生成器生成。  
还有，我并没有说class的属性一定要写paragraph，或者什么属性写成paragraph就会有好看的字体之类的。class属性的值是随你写的，至于有这个属性的元素到底会产生什么变化，也是你写的CSS决定的。  

一个元素还可以有多个类：

```HTML
<p class="paragraph book article">一段文字</p>
```

上面的`<p>`元素就有paragraph、book和article三个类。在CSS里写了每个类对应的样式之后，这段文本就会同时渲染这三种样式。（如果你问冲突了怎么办的话，请看CSS篇）

还有一个和这个很像的属性，它也是任何元素都可以用的，用来找到某个特定的元素。它就是`id`。在同一个HTML里，`id`的属性值必须是唯一的。假如你写了CSS，说`id="title"`的元素要加大字号，那么这个唯一的元素显示的样子就会改变。`id`还有一个用途，就是**页面内跳转**。（还是狗屁不通文章生成器，嘿嘿）  

```HTML
<h1>《996的自我修养》</h1>

<h2>第一章：什么是996？</h2>

<p>点击<a href="#charpter2">链接</a>直接跳到第二章</p>

<p>996的自我修养因何而发生？ 这样看来， 带着这些问题，我们来审视一下996的自我修养。 俾斯麦说过一句富有哲理的话，失败是坚忍的最后考验。我希望诸位也能好好地体会这句话。 问题的关键究竟为何？ 笛卡儿曾经提到过，读一切好书，就是和许多高尚的人谈话。这句话语虽然很短，但令我浮想联翩。 生活中，若996的自我修养出现了，我们就不得不考虑它出现了的事实。 带着这些问题，我们来审视一下996的自我修养。</p>

<p>拉罗什福科曾经说过，我们唯一不会改正的缺点是软弱。这句话语虽然很短，但令我浮想联翩。 希腊曾经提到过，最困难的事情就是认识自己。这似乎解答了我的疑惑。 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 996的自我修养，到底应该如何实现。 带着这些问题，我们来审视一下996的自我修养。 就我个人来说，996的自我修养对我的意义，不能不说非常重大。 本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。</p>

<p>一般来说， 别林斯基曾经说过，好的书籍是最贵重的珍宝。带着这句话，我们还要更加慎重的审视这个问题： 带着这些问题，我们来审视一下996的自我修养。 经过上述讨论， 一般来讲，我们都必须务必慎重的考虑考虑。 这样看来， 带着这些问题，我们来审视一下996的自我修养。 一般来讲，我们都必须务必慎重的考虑考虑。 996的自我修养，发生了会如何，不发生又会如何。 既然如何， 这样看来， 一般来说， 那么， 现在，解决996的自我修养的问题，是非常非常重要的。 所以， 总结的来说， 996的自我修养的发生，到底需要如何做到，不996的自我修养的发生，又会如何产生。 吉姆·罗恩曾经提到过，要么你主宰生活，要么你被生活主宰。带着这句话，我们还要更加慎重的审视这个问题： 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 996的自我修养因何而发生？ 就我个人来说，996的自我修养对我的意义，不能不说非常重大。 996的自我修养，发生了会如何，不发生又会如何。 俾斯麦说过一句富有哲理的话，对于不屈不挠的人来说，没有失败这回事。这启发了我， 克劳斯·莫瑟爵士说过一句富有哲理的话，教育需要花费钱，而无知也是一样。这启发了我， 莎士比亚在不经意间这样说过，抛弃时间的人，时间也抛弃他。带着这句话，我们还要更加慎重的审视这个问题： 经过上述讨论， 所谓996的自我修养，关键是996的自我修养需要如何写。 这样看来。</p>

<h2 id="#charpter2">第二章：如何开始996</h2>

<p>如果要996，你首先需要一个科技公司。取个名字，什么白渡、滕迅、啊狸叭叭都可以。</p>

```

`<p>点击<a href="#charpter2">链接</a>直接跳到第二章</p>`这一句的“链接”两字会被加上超链接，点击它，文本会直接跳转到第二章。你可以自己试试。（可能由于第二章标题已经出现在了视野中，你是看不到“跳转”的，那样的话就多加点废话进去）

## 空白

```HTML
<h1> 《 好 兄 弟 》 </h1>
<h1> 《       好      兄
     弟      》 </h1>
```

上面这两段HTML显示起来是一样的，都是：

> 《 好 兄 弟 》  

无论你在HTML元素的内容中使用多少空格(包括空白字符，包括换行)，渲染的时候，连续出现的空白符（包括回车）都会变成一个空格。没错，不管是带文本的元素之外，还是带文本的元素之内，都一样。

>那么为什么我们会在HTML元素的嵌套中使用那么多的空白呢? 答案就是为了可读性 —— 如果你的代码被很好地进行格式化，那么就很容易理解你的代码是怎么回事，反之就只有聚做一团的混乱.。在我们的HTML代码中，我们让每一个嵌套的元素以两个空格缩进。 你使用什么风格来格式化你的代码取决于你 (比如所对于每层缩进使用多少个空格)，但是你应该坚持使用某种风格。
>——GCV Ctrl+C Ctrl+V 自 MDN

## 实体引用

那我偏要打很多空格怎么办？  
也是可以解决的。如果你打了一个`&nbsp`，在解释的时候，就会变成空格。比如说这样一段：

```HTML
<p>啊&nbsp&nbsp&nbsp这</p>
```

它显示的时候就会有三个空格。  
同样还有别的问题，比如说，如果要打一个尖括号呢？如果直接打，是会被当成标签的。  
`&lt`就是左尖括号（小于号），`&gt`就是右尖括号（大于号）。比如说这个，前一句是错的，后一句就可以显示正确的样子：

```HTML
<p>HTML 中用 <p> 来定义段落元素。</p>           错的！
<p>HTML 中用 &lt;p&gt; 来定义段落元素</p>       对的！
```

上面这种用一串奇奇怪怪的东西代替一个字符的方式叫实体引用。这里有一个表格：  

<table>
 <thead>
  <tr>
   <th scope="col">原义字符</th>
   <th scope="col">等价字符引用</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>&lt;</td>
   <td>&amp;lt;</td>
  </tr>
  <tr>
   <td>&gt;</td>
   <td>&amp;gt;</td>
  </tr>
  <tr>
   <td>"</td>
   <td>&amp;quot;</td>
  </tr>
  <tr>
   <td>'</td>
   <td>&amp;apos;</td>
  </tr>
  <tr>
   <td>&amp;</td>
   <td>&amp;amp;</td>
  </tr>
 </tbody>
</table>

## 注释

如果你写了一段超级长的HTML，n年后维护的时候，你很有可能发现不知道你写了什么。因此，你当初需要写注释，来避免这种情况的发生。或者，你写了HTML给别人看，他看不懂你写了什么LJ玩意。这也需要你写注释。  
浏览器不会渲染注释的内容，用户也看不到它，只有看源码的人才能看到。  
把一段东西变成注释，只需要用`<!--`和`-->`把东西包起来。下面这段代码，由于第一句在注释外，第二句和第三句在注释内，所以只会显示“我在注释外！”。

```HTML
<p>我在注释外！</p>
<!-- 我在注释内！ -->
<!-- <p>我也在注释内！</p> -->
```

## 音视频

要是你可怜的网页没有音视频，大概很多人都会不感兴趣。所以，来学习嵌入音视频吧。  

### 视频

由于GCVillager是\_\_\_\_\_\_\_\_\_，所以这里还是放一个\_\_\_\_\_\_\_\_\_\_的视频。  

```HTML
<video controls>
  <source src="https://yjzx-site.github.io/img/club-file/scissor-seven-video.mp4" type="video/mp4">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="https://yjzx-site.github.io/img/club-file/scissor-seven-video.mp4">此链接</a>观看</p>
</video>
```

正常显示起来大概是这样，一个简易的播放器：

![视频播放器](4_video-demo.png)  

解释一下：`controls`是`video`元素的一个属性（还是布尔属性），选了之后会多出来一个栏，让用户可以拉进度条啊，调音量之类的。`source`就是字面意思，src里面就是视频的链接，`type`属性向浏览器说明了视频的格式。由于`video`元素是HTML5加的，如果别人在用IE之类的垃圾浏览器，可能看不了你的视频。这时候，剩下的内容叫后备内容，写了它，可以让那些用户至少还能把视频下过来看（记得提醒他们换浏览器）。  
假如你做了一个视频网站，有时候，可能你的某个小服务器维护啊之类的；或者因为mp4是有版权费的，有的浏览器买不起就不支持mp4，这时候就需要其他的视频源。

```HTML
<video controls>
  <source src="https://yjzx-site.github.io/img/club-file/scissor-seven-video.mp4" type="video/mp4">
  <source src="https://yjzx-site.github.io/img/club-file/scissor-seven-video.webm" type="video/webm">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="https://yjzx-site.github.io/img/club-file/scissor-seven-video.mp4">此链接</a>观看</p>
</video>
```

这样就有两个视频源了，如果第一个不行就默认第二个。你还可以写第三个第四个第五个第六个第七个第八个第九个第十个，只需要照着样子加在后面。  

### 其他视频属性

```HTML
<video controls width="400" height="400"
       autoplay loop muted preload="auto"
       poster="poster.png">
  <source src="https://yjzx-site.github.io/img/club-file/scissor-seven-video.mp4" type="video/mp4">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="https://yjzx-site.github.io/img/club-file/scissor-seven-video.mp4">此链接</a>观看</p>
</video>
```

`width`和`height`：和图片差不多，就是限定大小。方便嵌入到页面的某个部分，不打乱排版。  
`autoplay`：打开页面就自动播放。（当然可能会被浏览器阻止）  
`loop`：循环播放，就是放完再放。  
`muted`：默认静音。当然用户可以自己把声音打开（如果你加了`controls`控制条的话）  
`poster`：指向一张图片的链接，在视频播放前显示，可以做预览或者广告。不过在本例中，由于自动播放的存在，大概是看不到那张图片了。  
`preload`：可以用来缓存较大的文件。这个属性有三个选项：`none`不缓冲，`auto`页面加载后缓存媒体文件，`metadata`只缓存媒体文件的元数据。  

综合运用一下，假设我们要在网页靠上方的地方嵌入一个长条广告，人总是要恰饭的嘛。  

```HTML
<video width="800" height="100"
       autoplay loop muted preload="auto">
  <source src="ad.mp4" type="video/mp4">
  <p>广告加载失败。</p>
</video>
```

广告可以控制进度可能就不像广告了，所以删掉`controls`来删掉控制条。为了逼别人看，而且他浏览这个网页的时候让他一直能看到，就开`autoplay`和`loop`。广告有声音太吵了给人骂，所以静音（您做广告的时候不加声音不就好了吗？）。缓存的话……在这个例子里加和不加也没什么区别，因为自动播放了嘛，本来就是加载好就开始播放的。  

### 音频

音频和视频差不多。如下：

由于\_\_\_\_\_\_\_\_\_，所以\_\_\_\_\_\_\_\_\_\_。（不会还有人不会填这句话吧？）  

```HTML
<audio controls>
  <source src="https://yjzx-site.github.io/img/club-file/scissor-seven-music.mp3" type="audio/mp3">
  <source src="https://yjzx-site.github.io/img/club-file/scissor-seven-music.ogg" type="audio/ogg">
  <p>你的浏览器不支持 HTML5 音频，可点击<a href="https://yjzx-site.github.io/img/club-file/scissor-seven-music.mp3">此链接</a>收听。</p>
</audio>
```

效果如图：

![音频播放器](4_audio-demo.png)

不过有一点差异：没有`width`和`height`，也没有`poster`，原因很简单吧，音频又不能看。  

## `span`元素

现在先假设一下，有一个CSS，它可以让你所有带`red`类的文本变成红色，而且让所有带`hide`类的文本背景变成黑色（这样黑色文字就躲在阴影里看不见了）。现在我们要有这样的效果：

![span使用](4_span-usage.png)

如果直接给`<p>`上class，那么整个句子都会被渲染，那可不行。正确做法就是使用`span`。如下：  

```HTML
<p>这是一段<span class="red">奇怪</span>的文字，<span class="hide">这里你是看不见的</span></p>
```

当然你自己写HTML的时候是不会显示成图片里那样子的啦，毕竟你没加CSS嘛……以后再讲。  
