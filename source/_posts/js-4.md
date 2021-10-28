---
title: JS —— 分支结构
categories:
  - [教程, JS]
  - [计算机社, 尼泽·莫伯斯]
tags:
  - 教程
  - JS
date: 2021-10-28 08:34:58
author: 尼泽·莫伯斯
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Control_flow_and_error_handling>
- <https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Building_blocks/conditionals>

基础的数据结构，我们了解不少了。现在到了去用它们做点什么的时候了。

加速！这里我们要开始讲一个基础结构——分支结构。

## 开始之前

人类（以及其他的动物）无时无刻不在做决定，这些决定都影响着他们的生活，从小事（“我应该吃一片还是两片饼干”）到重要的大事（“我应该留在我的祖国，在我父亲的农场工作；还是应该去美国学习天体物理学”）。

条件语句结构允许我们来描述在 JS 中这样的选择，从不得不作出的选择（例如：“一片还是两片”）到产生的结果或这些选择（也许是“吃一片饼干”可能会“仍然感觉饿”，或者是“吃两片饼干”可能会“感觉饱了，但妈妈会因为我吃掉了所有的饼干而骂我”。）

![cookie](4_cookie-choice-small.png)

## 布尔值

在正式开始分支结构之前，我们要讲下**布尔值(Boolean)**，这是进行条件判断的基础，分支和循环结构都要用到。

布尔值也是一种类型，和我们之前讲过的数字和字符串一样。不同的是它只有两个值: `true` 和 `false`。分别对应 "真" 和 "假"。

``` js
> true;
true
> false;
false
> 
```

一般情况下我们也不会这样用布尔值，而是采用一些比较运算和逻辑运算来得到，就像下面这样。

``` js  
> 1 === 1; //1 和 1 相等，正确，是 true
true
> 1 === 0; //1 和 0 不相等
false
> true && true; // And 运算符
true
> true && false; // 必须两个都是 true 才是 true
false
> 
```

## 比较运算

比较运算符是一个**二元运算符**，意思是左右两边分别需要一个运算数，就像之前我们讲过的四则运算一样。不过比较运算的结果不是普通的数字，而是一个布尔值，即 `true` 和 `false` 。

``` js
> 1 + 2; // 四则运算，结果是数字
3
> 1 < 2; // 比较运算的结果是布尔值
true
> 1 > 2; // 1 小于 2 是假命题，所以 false
false
> 
```

通过这里，我们可以很明显的看出，比较运算有这两个特点：

- 如果表达式成立，那么值为 true
- 如果表达式不成立，那么值为 false

和数学类似，我们有大于，小于，等于这些比较运算符。不同的是，我们的大于等于和小于等于是 `>=` 和 `<=`，因为键盘打不出来数学里那个。而等于一般使用 `===`，这样不会和赋值 `=` 混淆。常用的比较运算符有这些：

<table class="standard-table">
 <caption>比较运算符</caption>
 <thead>
  <tr>
   <th scope="col">运算符</th>
   <th scope="col">描述</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Equality">等于 Equal</a> (<code>==</code>)</td>
   <td>
    <p>如果两边操作数相等时返回true。</p>
   </td>
  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Inequality">不等于 Not equal</a> (<code>!=</code>)</td>
   <td>如果两边操作数不相等时返回true</td>
  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Identity">全等 Strict equal</a> (<code>===</code>)</td>
   <td>两边操作数相等且类型相同时返回true。</td>
  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Nonidentity">不全等 Strict not equal</a> (<code>!==</code>)</td>
   <td>两边操作数不相等或类型不同时返回true。</td>

  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Greater_than_operator">大于 Greater than</a> (<code>&gt;</code>)</td>
   <td>左边的操作数大于右边的操作数返回true</td>

  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Greater_than_or_equal_operator">大于等于 Greater than or equal</a> (<code>&gt;=</code>)</td>
   <td>左边的操作数大于或等于右边的操作数返回true</td>

  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Less_than_operator">小于 Less than</a> (<code>&lt;</code>)</td>
   <td>左边的操作数小于右边的操作数返回true</td>

  </tr>
  <tr>
   <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Less_than_or_equal_operator">小于等于 Less than or equal</a> (<code>&lt;=</code>)</td>
   <td>左边的操作数小于或等于右边的操作数返回true</td>

  </tr>
 </tbody>
</table>

下面是一些示例，可以看到它们和预期的结果是符合的：

``` js
> 1 + 2 >= 3;
true
> 569 < 123;
false
> 123 === 123;
true
> 2 * 3 === 3 + 3;
true
> 2 * 3 !== 3 + 3;
false
> 
```

字符串也可以使用比较运算，它们之间的比较使用的是**字典序**，由于日常应用的时候基本只需要判断字符串之间是否相等，所以这里不详细提及字典序大小的比较。

``` js
> "aaa" === 'aaa'; // 相等
true
> "aaa" !== "bbb"; // 不相等
true
> 'aaa' > 'bbb'; // 字典序
false
> 'aaa' <= 'bbb';
true
> 
```

你可能会注意到，上面我给出的示例只用了全等号(`===`)和不全等号(`!==`)，而没有使用普通的等于和不等于。事实上我们提倡尽可能使用三个等号组成的全等号，因为它可以避免 JS 过于宽松的自动类型转换带来的一些容易造成错误的问题。看看下面的代码：

``` js
> "0" == 0; // 自动类型转换
true
> "0" === 0; // 禁止了自动类型转换
false
> 123 != "123";
false
> 123 !== "123";
true
```

这里等于号和不等号遇到了一些问题：它把一个字符串和一个数字进行了转换，然后认为它们是相等的。这可能会导致你的程序出现一些难以排查的错误，所以尽可能避免它们。

## 逻辑运算

在进行比较运算的时候，我们可能会需要将多个条件连起来，我们假设有这三个变量需要判断：

- `num1` 大于 0 ，小于 100 。
- `num2` 可以被 2 整除或者可以被 3 整除。
- `num3` 既不被 5 整除，又不被 4 整除。

这就需要使用逻辑运算，将多个表达式组合起来，然后得到想要的结果。逻辑运算符有三种：

| 运算符 | 描述 | 示例 |
| ----- | ---  | ----|
| 与 ( `&&` ) | 当两边表达式值都为 true 时为 true，否则为 false | `true && true === true`<br>`true && false === false` |
| 或 ( `\|\|` ) | 当两边表达式值有一个为 true 时为 true，否则为 false | `true \|\| false === true`<br>`false \|\| flase === false` |
| 非 ( `!` )  | 当后面的值是 true 是为 false，反之为 true | `!true === false`<br>`!false === true` |

因此上面我们提到的例子可以这么写：

``` js
num1 > 0 && num1 < 100;
num2 % 2 === 0 || num2 % 3 === 0;
!(num3 % 5 === 0 || num3 % 4 === 0);
```

前面两个应该比较好理解，第三个为什么要带个括号呢？答案是运算符优先级问题。括号的作用是让括号里面的东西先算，这个学过数学都知道，放在这里也是一样的。如果我们去掉这个括号，就相当于下面这样：

``` js
!num3 % 5 === 0 || num3 % 4 === 0);
(!num3 % 5 === 0) || num3 % 4 === 0;
```

可以看到是左边的那个非运算符先算，再到后边的或运算符，就出错了。运算符优先级是这样：先算 `!`，再算 `&&` ，最后算 `||`，同级别从左到右。如果写程序的时候个别优先级不了解，那就多打几个括号，最多丑点。

## if 语句

前面讲了这么多逻辑，现在有请我们的主角出场吧：就是 **if 语句** ！有了它，你就可以在程序里面根据不同的条件，去做出一系列的决定。以下是它的伪代码表示：

``` js
if (一个表达式或者值) {
  如果这个表达式结果是 true ，那么执行这里的内容;
  可以有很多句;
} else {
  如果值是 false ，那么执行这里的内容;
  也可以有很多句;
}
```

关键字 if，并且后面跟随括号。  
要测试的条件，放到括号里（通常是“这个值大于另一个值吗”或者“这个值存在吗”）。这个条件会利用比较运算符（我们会在最后的模块中讨论）进行比较，并且返回 true 或者 false 。  
一组花括号，在里面我们有一些代码——可以是任何我们喜欢的代码，并且只会在条件语句返回 true 的时候运行。一般情况下前一个大括号和  if 在同一行，后一个单独一行，这样比较美观，也可以避免 JS 自动加入分号的机制造成的问题。  
关键字 else 。  
另一组花括号，在里面我们有一些代码——可以是任何我们喜欢的代码，并且当条件语句返回值不是 true 的话，它才会运行。  

这段代码真的非常易懂——它说“如果（if）条件（condition）返回true，运行代码A，否则（else）运行代码B”

注意：你不一定需要else和第二个花括号——下面的代码也是符合语法规则的：

``` js
if (一个表达式) {
  如果这个表达式结果是 true ，那么执行这里的内容;
}
```

多个条件代码可以使用 `else if`，你可以用它来进行多个条件的判断。

```js
if (一个表达式) {
  如果这个表达式结果是 true ，那么执行这里的内容;
} else if (一个表达式) {
  如果前一个表达式是 false ，这个表达式结果是 true ，那么执行这里的内容;
} else if (一个表达式) {
  如果前面的表达式都是 false ，这个表达式结果是 true ，那么执行这里的内容;
} else {
  如果前面都是 false ，那么执行这里的内容;
}
```

if 语句也可以嵌套：

``` js
if (一个表达式) {
  一些语句;
  if (一个表达式){
    一些语句;
  }
  一些语句;
}
```

有时候你可能会看到 if…else 语句没有写花括号，像下面的速记风格：

``` js
if (一个表达式) 一行代码;
else 一行代码;
```

这是完全有效的代码，但不建议这样使用——因为如果有花括号进行代码切割的话，整体代码被切割为多行代码，更易读和易用。

## switch 语句

在需要多重分支时可以使用基于一个数字或字符串的 switch 语句：

``` js
let x = 1;
switch (x) {
    case 0:
        console.log(0);
        break;
    case 1:
        console.log(1);
        break;
    default:
        console.log("default");
}
```

因为 switch 语句本质是跳到指定的标签开始执行，所以每个 case 结尾需要加上 `break` 语句用来退出，否则它会一直按顺序执行，运行到后面的代码，比如这样。

``` js
let x = 1;
switch (x) {
    case 0:
        console.log(0);
    case 1:
        console.log(1);
    default:
        console.log("default");
}
```

输出就变成了

``` fakecode
1
default
```

## 一些例子

现在已经到了比较复杂的程序，所以我们就不再直接使用交互式解释器来运行我们的代码了。接下来的所有例子都会是一个单独的 JS 文件，你可以加到 HTML 里面通过浏览器运行，然后在控制台查看输出。

假设有一个年份，变量名叫做 year，现在要你判断它是否是闰年。

1582年以来的置闰规则：

- 普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
- 世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）。

写成程序就是这样

``` js
// 实际情况需要配合输入，这个以后在讲 DOM 的时候会了解
let year = 2021; 

// 先判断最特殊的
if (year % 4 !== 0) {
    console.log("不是闰年");
} else if (year % 400 === 0) {
    console.log("是闰年");
} else if (year % 100 === 0) {
    console.log("不是闰年")
} else {
    // 现在只能是被 4 整除的了
    console.log("是闰年");
}
```

当然你也可以按照别的顺序进行判断。就像这个例子。只要答案是对的就可以。

``` js
if (year % 4 === 0) {
    if (year % 100 === 0 && year % 400 !== 0) {
        console.log("不是闰年");
    } else {
        console.log("是闰年");
    }
} else {
    console.log("不是闰年");
}
```

给定一个数组，然后从小到大排序数组里面的数字并输出，用空格分隔：

``` js
let myArray = [3, 1, 2];

if (myArray[0] > myArray[1]) {
    let temp = myArray[0];
    myArray[0] = myArray[1];
    myArray[1] = temp;
}
if (myArray[1] > myArray[2]) {
    let temp = myArray[1];
    myArray[1] = myArray[2];
    myArray[2] = temp;
}
if (myArray[0] > myArray[2]) {
    let temp = myArray[0];
    myArray[0] = myArray[2];
    myArray[2] = temp;
}
// 最后还要比较一下 (自己想想为什么)
if (myArray[0] > myArray[1]) {
    let temp = myArray[0];
    myArray[0] = myArray[1];
    myArray[1] = temp;
}
console.log(myArray);
```

这里写成这样是为了演示分支，下章循环结构我们会有更简便的方法。实际上 JS 的数组还有一个自带的方法 `.sort()`，可以从小到大排序数组里面的内容。

``` js
let myArray = [3, 1, 2];
myArray.sort();
console.log(myArray);
```

## 码风

貌似我们之前的 if 语句都是这样的：

``` js
if () {
    //do something
} else if () {
    //do something
} else {
    //do something
}
```

其实 if 还可以写而成这样

``` js
if ()
{
    //do something
}
else if ()
{
    //do something
}
else
{
    //do something
}
```

我们可以看到这里的开头大括号放在了下一行。其实其他的语言有很多也是这么写的。但是 JS 里面不推荐这么写，因为 JS 有个**自动插入分号**的机制，这本来是为了你万一忘记打分号也能正常运行程序用的，但是有时候会带来一点不愉快的事情：

``` js
return 
{
    statues : true
};
```

看起来你是想要返回一个对象，然而这种机制导致它实际上是这样的意思：

``` js
return; // BAD!!!
{
    statues : true;
};
```

你可以看到它直接返回了，而后面那个对象就没有了。所以还是要这么写：

``` js
return {
    statues : true
};
```

为了统一风格，我们就把所有的开头大括号不换行了。

## 练习

还记得 Tux 么？之前它让你写了一个计算 BMI 的程序，现在它要你去把这个程序改一下，判断 Tux 的 BMI 是不是正常的。

下面是程序的开头，你要用给出的体重 (变量 `weight` ) 和身高 (变量 `height` ) 来计算 BMI，同时判断 BMI 水平，输出“偏瘦”(小于18.5) “正常” (在 18.5-23.9 之间)和 “偏胖” (大于 23.9)。（BMI=体重/身高^2）

``` js
let weight = 82;
let height = 1.61;
```
