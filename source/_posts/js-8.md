---
title: JS —— 其他概念
categories:
  - [教程, JS]
  - [计算机社, 尼泽·莫伯斯]
tags:
  - 教程
  - JS
date: 2021-10-31 15:32:33
author: 尼泽·莫伯斯
cover:
---

经过了几个月自己写 JS 的几个项目，我觉得有几个概念也很有必要介绍一下。但是我没有那么多时间去重写教程了。所以就引用别人的链接好了。

这里我们补充一些其他的 JS 教程的链接。推荐去按顺序阅读它们。如果是英语的，可以点击网页右边的"English (US)"，将其换为"中文(简体)"

## 闭包

和大多数其他语言不一样，JS 的函数里面可以创建函数。这种函数叫做**闭包**，它有许多有意思的行为，有时候让许多操作变得简单。

见 <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Closures>

## 面向对象编程

面向对象是一个很重要的编程理念，在项目当中灵活使用面向对象的思想，有时候能够起到事半功倍的效果。

JS 是一个多范式编程语言，也支持面向对象的特性。这篇文章讲述了 JS 当中面向对象的各种方式，你可以一一了解它们。不过我建议对于**构造器函数了解本质即可**，真正在工程实践的时候**尽可能使用 Class**，因为后者语法更加简洁易懂，不容易出错。

<https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Objects>

Class 的介绍:

<https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes>

## 异步

异步设计可以说是 JS 当中的亮点。这也是因为 JS 经常需要遇到异步相关操作。异步有传统回调，Promise 和 async/await 三种方式。同样的道理，我们建议大家了解所有方法，但是尽量使用 async 来进行异步操作。

<https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous>

## 模块

模块可以用来和 class 结合，使得项目更加有逻辑性。我们建议在较大的项目上面使用模块来管理各个部分的逻辑。

<https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Modules>
