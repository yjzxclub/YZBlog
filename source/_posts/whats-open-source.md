---
title: 什么是开源
categories:
  - [转载, Acfboy]
tags:
  - 转载
  - 开源
  - 趣闻杂谈
date: 2021-09-13 20:58:34
author: Acfboy
copyright: false
cover: https://www.luogu.com.cn/blog/Acfboy/kai-yuan-shi-shi-me-neng-chi-ma-post
---

以下是我们转载的文章。

<hr>

<p>引用的一些内容来源链接在文末给出</p>

<p>大家好，我是Acfboy,算法竞赛，<strong>开源软件</strong>和航空业的爱好者.</p>
<p>今天，开源软件在生活中的地位与日俱增，但在很多人的概念中，只有闭源软件，没有开源，所以，想通过这篇文章简单介绍介绍开源软件。</p>
<h2>开源是什么</h2>
<h3>开源软件的定义</h3>
<blockquote>
<p>开放源代码（Open source code）也称为源代码公开，指的是一种软件发布模式。一般的软件仅可取得已经过编译的二进制可执行档，通常只有软件的作者或著作权所有者等拥有程序的原始码。有些软件的作者会将原始码公开，此称之为“源代码公开”，但这并不一定符合“开放源代码”的定义及条件，因为作者可能会设定公开原始码的条件限制，例如限制可阅读原始码的对象、限制衍生品等。</p>
<p>——百度百科</p>
</blockquote>
<p>简单的来说，开源软件就是通过一定的许可协议开放源代码的软件。</p>
<p>最早源自开源运动之父RMS的<code>Copyleft</code>思想，这里的<code>left</code>不是“左”或“留下”，而与“著作权”中的<code>Copyright</code>相对应。</p>
<p>RMS：<img src="http://static.oschina.net/uploads/space/2015/0325/070300_M7m1_2306979.jpg" alt=""></p>
<p>从1989年第一个开源许可协议<code>GPL</code>被提出后，开源软件逐步发展，如今已经渗透到各行各业，你的手机，路由器，你谷的评测机，等等，都使用了按照<code>GPL</code>开源的<code>Linux</code>，其它的一些开源组件也广泛使用，如你谷显然用了<a href="https://www.mdui.org/">MDUI</a>,一个开源的前端框架。</p>
<p>程序猿们总是希望自己的软件能够安全使用，遇到问题能自己改或让人改，好奇时能看一看源代码。从这个角度来说，开源软件就像是送给程序员的礼物。</p>
<p>开源软件同样可以带来商业利益，如<a href="https://ubuntu.com/pricing">围绕Ubuntu展开的商业服务</a></p>
<h3>为什么要支持开源</h3>
<p>首先，开源软件有长期可依赖性，不大可能对你停止授权；对于一些源代码被阅读多的项目，安全性和稳定性是可以保证的；由于源代码开放，可定制程度高，易于学习（只要你足够厉害），也是其一大亮点。</p>
<p>前一段时间，美国搞了一个出口限制清单，限制软件对中国的授权，哈工大、北航等国内高校被禁止使用 MATLAB。</p>
<p>这个时候开源软件便体现出它独到的优越性，FSF（自由软件基金会），Apache基金会和Linux基金会都宣布已经发布的开源软件不会受美国清单的影响。</p>
<p>RMS说</p>
<blockquote>
<p>学校应该教授开源软件的使用，这是帮助他们在信息社会成为独立的人；保证社会不被高科技公司所垄断。教授闭源软件是在培养学生的依赖性，与学校的宗旨背道而驰。</p>
</blockquote>
<p>可见，我们都应该支持开源软件，随着开源软件商业生态逐渐形成，开源公司也能实现盈利，开源软件将成为计算机软件的未来。</p>
<h3>开源从何而来？</h3>
<p>最早的开源，可以从那场操作系统的战争中讲起。</p>
<p>1985年，微软发布了Windows1.0操作系统，图形界面的操作系统使电脑开始进入大众的视野，人们不需要再记住许许多多的命令(<del>但有的时候命令行真心方便</del>)就可以使用电脑。苹果紧随其后推出了它们的图形操作系统。</p>
<p>1990年，Windows 3发布，一个真正可用的大众操作系统，微软的黄金时代开始了。1997年，微软占据了90%的市场。直到现在，Windows仍然是大部分用户使用的操作系统。
但在微软和苹果打得不可开交的时候，他们没有注意到一名 21 岁的芬兰计算机科学专业学生出现了。十分偶然的，他彻底改变了一切。</p>
<p>哪些科技巨头忙着竞争的时候，开源和自由软件的先驱也雨后春笋般冒出来，其中之一便是Richard Matthew Stallman, RMS。</p>
<p>当时，Unix价格高昂，RMS创立了GNU，即"GNU is Not Unix"(<del>发现递归了吗</del>)</p>
<p>现在，回到那位大学生身上来，他负担不起Unix高昂的费用，但只有Unix才能让他自由地编程，于是，他决定——自己写一个。一不小心地，就改变了世界。</p>
<p>1991年10月5日，Linus Torvalds提交了第一个Linux内核，包含一万行代码。</p>
<p>如今，Linux已经包含两千万行代码，超过五千位贡献者，并且击败了微软，成为了统治世界的操作系统，在手机，路由器，服务器等设备上，运行着无数的Linux，我们每个人都成为了受益者。</p>
<p>Linus Torvalds为什么能成功？GPL起了很大的作用。</p>
<blockquote>
<p>微软和苹果这样的公司一直在试图建造软件大教堂，而 Linux 及类似的软件则提供了一个由不同议程和方法组成的巨大集市，集市比大教堂有趣多了。 </p>
<p>——Eric Raymond</p>
</blockquote>
<p>Linux的成功，从一定程度上带动了所有开源软件的发展。</p>
<p>开源的时代，开始了！</p>
<h2>开源许可证</h2>
<p>开源许可证是告诉使用者它们可以干什么，不可以干什么的一种方式，大概就是这么一段话：</p>
<pre><code class="language-text">我允许你们XXX，我许可你们XXXX，你们可以XXXX，但是，你们必须XXXX，如果你们XXXX了，你们就必须XXXX，对了，对于XXXX这些情况，我可不负责。

你要同意，就用，不同意就别用。如果你用了，但违反了许可证的要求，我可能会告你啊！</code></pre>
<h3>各大许可证简单介绍</h3>
<p>有一张图简单介绍了开源许可证：</p>
<p><img src="https://oscimg.oschina.net/oscnet/c2b6ea91513c375d64926f35effdf00e5db.jpg" alt=""></p>
<h4>GPL</h4>
<ul>
<li>可以任意演绎、分发、复制 </li>
<li>源码开放</li>
<li>衍生版本必须也使用GPL协议开源
<ul>
<li>LGPL允许用类库引用(link)方式使用LGPL类库而不需要开源商业软件的代码</li>
</ul></li>
</ul>
<p>Linux就是通过GPL开源的</p>
<h4>MIT</h4>
<ul>
<li>保留源作者版权声明</li>
<li>没有其它任何限制</li>
</ul>
<p>Gridea(洛谷日报曾介绍过的博客系统)通过MIT开源</p>
<h4>BSD</h4>
<p>(<a href="https://www.luogu.com.cn/user/127140">@BillZhou233</a>补充)BSD 许可证分为 BSD-2 和 BSD-3，前者大概等效于 MIT，后者在前者基础上追加了 <strong>不能以源作者的名字宣传你的衍生版本</strong> 这项规定，文章中的 BSD 许可证其实是指代的 BSD-3。</p>
<ul>
<li>保留版权声明</li>
<li>不能以源作者的名字宣传你的衍生版本</li>
<li>没有其它限制</li>
</ul>
<p>Chromium通过BSD开源</p>
<h4>Apache</h4>
<ul>
<li>可以任意演绎、复制、分发等</li>
<li>保留版权声明</li>
<li>二次开发必须写明修改内容</li>
</ul>
<h3>如何使用开源许可证</h3>
<p>作为作者</p>
<ul>
<li>
<p>在一级目录下，给出一个LICENSE（或COPYING）文件，里面就是这个许可证的全文。</p>
</li>
<li>
<p>在所有的源码头部，说明版权，说明许可。</p>
</li>
</ul>
<p>如图
<img src="https://oscimg.oschina.net/oscnet/adeef80f4b1f1d09cdc826df2801aa41f9a.png" alt=""></p>
<p>在开源许可证中，用下面的方式写版权是非常好的：版权属于<span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>×</mo><mo>×</mo><mo>×</mo></mrow><annotation encoding="application/x-tex">\times \times \times</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.66666em; vertical-align: -0.08333em;"></span><span class="mord">×</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 0.66666em; vertical-align: -0.08333em;"></span><span class="mord">×</span></span></span></span></span>和所有贡献者
<img src="https://5b0988e595225.cdn.sohucs.com/images/20200512/20408a1f6047475b99b4eca0e546367f.jpeg" alt=""></p>
<p>作为使用者，您应该说明引用了哪些其它开源项目，谷歌的浏览器在这一点是一个典范。</p>
<p><img src="https://oscimg.oschina.net/oscnet/eb01d85e208f7934457d71b078d72329244.png" alt=""></p>
<p><img src="https://oscimg.oschina.net/oscnet/7ef84fdce6cc84823ed88e69a3d137640d1.png" alt=""></p>
<h2>文档共享协议</h2>
<p>“醉翁之意不在酒，在乎山水之间也”</p>
<p>喜欢开源软件，喜欢的是开源精神，软件只是一个形式，文档和其它作品也有“开源”的协议。</p>
<h3>cc0协议</h3>
<p>最大限度地放弃知识产权，就是在法律限度内放弃了所有权利，洛谷首页挂的Blue的博客就是通过这种方式共享的。</p>
<p>(<em><a href="https://www.luogu.com.cn/user/383773">@EnderCrystal</a>补充</em>)但中国大陆法律规定不得放弃著作权，所以在这里CC0是无效的。而这样来看的话，Blue相当于按照CC0放弃了权利，但他却无法放弃责任。</p>
<h3>CC协议</h3>
<p>CC后面可以加上以下后缀改变授权方式。</p>
<ul>
<li>姓名标示（BY）：您可以自由复制、散布、展示及演出本作品；您必须按照作者或授权人所指定的方式，保留其姓名标示。</li>
<li>非商业性（NC）：您可以自由复制、散布、展示及演出本作品；您不得为商业目的而使用本作品。</li>
<li>禁止改作（ND）：你可以自由复制、散布、展示及演出本作品；您不得改变、转变或改作本作品。</li>
<li>相同方式分享（SA）：你可以自由复制、散布、展示及演出本作品；若您改变、转变或改作本作品，仅在遵守与本著作相同的授权条款下，您才能散布由本作品产生的衍生作品。</li>
</ul>
<p>如本文采用<a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>许可证进行许可。</p>
<h2>最后的话</h2>
<p>在我们学校的名人墙上，<strong>为自己赚钱写程序比尔盖茨，乔布斯昂首挺胸，而不拿钱的，为全人类做出巨大贡献的RMS，Linus Torvalds却不见踪影</strong>，这也体现了国内开源文化的短板</p>
<p>很快，明年，或再下一年，<code>Python</code>就要加入初中的课本了。</p>
<p>希望各位一线教师们，在传授<code>Python</code>语法的同时，也能顺便普及一些开源思想，普及一下GitHub这样的开源平台。</p>
<p>虽然美国现行法律不会影响开源软件的出口，但现在大量开源的使用，使我国的技术依然受制于人。</p>
<p>解决的办法，就是发展我们自己的开源平台和开源软件。</p>
<p>开源的愿望很美好，祝福开源的未来会更光明！</p>
<h2>参考</h2>
<ul>
<li>
<p>开源中国：<a href="https://baijiahao.baidu.com/s?id=1665536968387234930&amp;wfr=spider&amp;for=pc">从 Copyright 到 Copyleft，聊聊版权与开源协议</a></p>
</li>
<li>
<p>开源中国：<a href="https://www.sohu.com/a/394741563_827544">步进式解读Apache许可证 </a></p>
</li>
<li>
<p><a href="https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81/114160?fromtitle=%E5%BC%80%E6%BA%90&amp;fromid=20720669#viewPageContent">百度百科：开源</a></p>
</li>
</ul>
<ul>
<li>
<p>卫Sir：<a href="https://my.oschina.net/u/3799215/blog/4334195">从MIT协议谈契约精神</a></p>
</li>
<li>
<p>RedHat:<a href="https://www.redhat.com/en/command-line-heroes">Command Line Heros</a></p>
</li>
</ul>
<br>



> 原作者: Acfboy  
> 原文链接: <https://www.luogu.com.cn/blog/Acfboy/kai-yuan-shi-shi-me-neng-chi-ma-post>  
> 原文按照 [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议发布，转载请注明出处。  