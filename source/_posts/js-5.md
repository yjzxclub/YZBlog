---
title: JS —— 循环结构
categories:
  - [教程, JS]
  - [计算机社, 尼泽·莫伯斯]
tags:
  - 教程
  - JS
date: 2021-10-28 08:35:00
author: 尼泽·莫伯斯
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/learn/JavaScript/Building_blocks/Looping_code>
- <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Loops_and_iteration>

有时候，我们需要完成一些重复的任务。比方说，现在我要按顺序输出 1 到 32 这些数字，要怎么做？曾经有个伟大的 GCVillager 手动写下了 32 行：

``` js 
console.log(1);
console.log(2);
console.log(3);
console.log(4);
console.log(5);
console.log(6);
console.log(7);
console.log(8);
console.log(9);
console.log(10);
console.log(11);
console.log(12);
console.log(13);
console.log(14);
console.log(15);
console.log(16);
console.log(17);
console.log(18);
console.log(19);
console.log(20);
console.log(21);
console.log(22);
console.log(23);
console.log(24);
console.log(25);
console.log(26);
console.log(27);
console.log(28);
console.log(29);
console.log(30);
console.log(31);
console.log(32);
```

我们肯定不能学他，毕竟要输出 1145141919810 行怎么办？所以就有了今天的主角——循环结构。

## for 循环

下面这个代码就可以解决开头的问题。

``` js
for (let i = 0; i < 32; i++) { // 还记得自增运算符吧
    console.log(i+1); // 想想为什么加一
}
```

我们可以这样看到循环的结构是这样的

``` js
for (初始化语句; 退出条件; 更新语句) {
    一些需要执行的代码;
}
```

可以看到这里的基本结构

1. 关键字for，后跟一些括号。
2. 在括号内，我们有三个项目，以分号分隔：
    - 初始化语句 - 通常我们会在这里声明一个数字变量，这个变量可以配合后面的更新语句来统计循环当前执行了的次数。它也有时被称为计数变量。
    - 退出条件 - 用来定义怎么退出循环。这个语句在每轮循环之前都会判断，如果满足条件就进入循环，如果不满足这个条件就退出循环。
    - 更新语句 - 在每轮循环结束的时候执行。它通常用于增加（或在某些情况下递减）计数器变量，使其更接近退出条件值。
3. 包含一些代码的花括号 - 每次循环时都会运行花括号里面的代码。

那么我们看下下面的代码：

``` js
let cats = ['Bill', 'Jeff', 'Pete', 'Biggles', 'Jasmin'];
let info = 'My cats are called ';

for (let i = 0; i < cats.length; i++) {
  info += cats[i] + ', ';
}

console.log(info);
```

这里每次都把 cats 里面的元素加到 info 的末尾，输出就是这样:

``` text
My cats are called Bill, Jeff, Pete, Biggles, Jasmin,
```

- 迭代器i从0开始（`let i = 0`）。
- 循环将会一直运行直到 i 不再小于 cats 数组的长度(`cats.length`)。
- 在循环中，我们将当前的 `cats[i]` 以及逗号和空格拼接 (`+=`)到 info 变量的末尾。 所以：
    - 在第一次运行中，i 为 0，所以 `cats[0] +'，'` 将被拼接到 info 上。
    - 在第二次运行中，i 为 1，所以 `cats[1] +'，'` 将被拼接到 info 上。
    - 每次循环运行后，i 都会加上 1，然后进程将再次启动，直到退出条件。
- 当等于 `cats.length` 时，循环将停止，浏览器将移动到循环下面的下一个代码位。

## 使用 break 退出循环

在循环当中，我们有时候需要在中途退出。还是上面的例子，如果我们需要找到 `cats` 数组里面的 Jeff 这个名字所在的下标，找到就退出，那可能就要写成这样

``` js
let cats = ['Bill', 'Jeff', 'Pete', 'Biggles', 'Jasmin'];
let cur;

for (let i = 0; i < cats.length; i++) {
    if ('Jeff' === cats[i] ) {
        cur = i;
        break;
    }
}

console.log(cur);
```

输出就是

``` text
i = 0
i = 1
1
```

其中循环执行到 `i = 1` 的时候，循环就因为满足了 if 的条件，然后被 break 语句退出了，没有执行到 `i < cats.length` 这个条件。

## 使用 continue 跳过迭代

continue语句以类似的方式工作，而不是完全跳出循环，而是跳过当前循环的下面部分，直接进入执行下一个循环。

比如说我们需要在遇到名字 `Jeff` 的时候不输出，就可以这么实现：

``` js
for (let i = 0; i < cats.length; i++) {
    if ('Jeff' === cats[i] ) {
        continue;
    }
    console.log(cats[i]);
}
```

输出

``` text
Bill
Pete
Biggles
Jasmin
```

这里在名称是 `Jeff` 的时候，`continue` 语句被执行，导致了后面的语句跳过去了，所以只有 `Jeff` 没有输出。

## while 和 do while 循环

除了 for 循环之外， JS 还有两种循环：while 和 do while 循环。while 循环只有在入口处包含一个条件判断语句，如果满足就会进入循环。

比如之前的那个打印 cats 数组内容的程序，使用 while 循环我们就可以写成这个样子：

``` js
let cats = ['Bill', 'Jeff', 'Pete', 'Biggles', 'Jasmin'];
let info = 'My cats are called ';

let i = 0;// 初始化语句被放在外面了，成了一个普通的声明变量
while (i < cats.length) { // 这里只有一个条件判断
    info += cats[i] + ', ';
    i++; // 更新变成了普通代码
}

console.log(info);
```

还有一个 do while 循环和它类似，不过条件判断是放在结尾的，也就是循环节结束之后判断是否继续循环。

``` js
let i = 0;
do {
    info += cats[i] + ', ';
    i++;
} while (i < cats.length);
```

## 小结

这里我们了解了程序的循环结构，这是用来执行一些重复性工作的好办法。

## 编程练习

现在回到开头的问题：请你帮助 GCVillager 把这个程序分别用 for, while, do while 循环实现。

把一个斐波那契数组算到第 45 个，这里我们给出了前两个，你需要自己计算每个数，并且存到数组里面，最后输出整个数组。(下标从 0 开始！)

```js
let fibonacci = [1, 1];
```
