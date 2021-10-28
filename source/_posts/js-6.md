---
title: JS —— 函数和方法
categories:
  - [教程, JS]
  - [计算机社, 尼泽·莫伯斯]
tags:
  - 教程
  - JS
date: 2021-10-28 08:35:03
author: 尼泽·莫伯斯
cover:
---

本文按照 Mozilla 贡献者基于 CC-BY-SA 2.5 协议发布的以下文章改编:

- <https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Building_blocks/Functions>
- <https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Building_blocks/Build_your_own_function>
- <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Functions>

在 JS 中另一个基本概念是函数, 它允许你在一个代码块中存储一段用于处理单任务的代码，然后在任何你需要的时候用一个简短的命令来调用，而不是把相同的代码写很多次。在本文中，我们将探索函数的基本概念，如基本语法、如何定义和调用、范围和参数。

## 函数的引入

现有有一个大于等于 2 的正整数 a ，现在我们需要判断这个数字是不是质数。质数是只有 1 和它自己两个因数的数。对于所有的大于 2 的数，我们需要枚举那些大于 2 小于等于根号 a 的所有数字，一一确定它们是不是 a 的因数，如果都找不到那么它肯定是质数。

``` js
let a = 114514; // 很明显这是个合数
let isPrime = false; // 一个 boolen ，记录是否为质数

if (a === 2) {
    isPrime = true;
} else {
    isPrime = true; // 先暂时赋值，如果后面没被覆盖肯定是质数
    for (let i = 2; i <= Math.sqrt(a); i++) {
        if (a % i === 0) {
            isPrime = false;
        }
    }
}

if (isPrime) {
    console.log("是质数。");
} else {
    console.log("不是质数。");
}
```

看起来很合理，但是如果有三个数，分别是 a, b, c。或者有三十个数，你是不是要把上面那个 if else 和循环都复制一下？这么做的话太麻烦了。所以我们有更好的方法：**函数 (function)** 。这就是上面写成函数的例子：

``` js
function judgePrime(a) {
    let isPrime = false;
    if (a === 2) {
        isPrime = true;
    } else {
        isPrime = true; // 先暂时赋值，如果后面没被覆盖肯定是质数
        for (let i = 2; i <= Math.sqrt(a); i++) {
            if (a % i === 0) {
                isPrime = false;
            }
        }
    }
    return isPrime;
}

let a = 114514, b = 17;

if (judgePrime(a)) {
    console.log(a + " 是质数。");
} else {
    console.log(a + " 不是质数。");
}

if (judgePrime(b)) {
    console.log(b + " 是质数。");
} else {
    console.log(b + " 不是质数。");
}
```

我们可以看出函数的结构：

``` js
function 函数名(参数) {
    // 主体代码块
    return;
}
```

一个函数定义（也称为函数声明，或函数语句）由一系列的 function 关键字组成，依次为：

- function 关键字。
- 函数的名称。
- 函数**参数列表**，包围在括号中并由逗号分隔。
- 定义函数的 JavaScript 语句，用大括号{}括起来。

比如我们从定义一个简单的乘方运算函数开始，这个函数可以得到给定数字的平方：

``` js
function square(number) {
  return number * number;
};
```

函数 square 使用了一个参数，叫作 number 。这个函数只有一个语句，它说明该函数将函数的参数 number 自乘（就是平方）后返回。函数的 return 语句确定了函数的返回值。返回值就像普通的数值一样。比如下面这个代码：

``` js
function square(number) {
  return number * number;
}
let x = square(3);
```

它执行了这样的操作：

- 声明一个 square 函数。
- 调用函数, 将 3 作为参数传给函数，此时函数的 number 变量的值变成了 3 。
- 程序继续向下运行，计算 number * number 的值。
- 将计算出来的值返回回来。
- 然后 `let x = square(3)` 就相当于 `let x = 9`，x 就变成了 9 了。

可以非常清楚的非常清楚地看到，调用函数的方式是在函数名后加上一对括号，括号中包含参数。如果有多个参数就可以用逗号分隔：

``` js
function add(a, b) {
    return a + b;
}
let x = add(1, 3); // x = 1 + 3
```

有些函数可以没有返回值，比如我有一个输出的函数：

``` js
function print(x) {
    console.log("你的参数是 " + x);
}
print(12);
print('aaa');
```

这种情况下面，函数将会返回默认值 `undefined`。

## 函数的特性

### 赋值

好像有点跑题，不过这个也是有关联的。

我们都知道那些基本数据是在赋值的时候，是可以被复制的：

``` js
> let val1 = 23;
undefined
> let val2 = val1; // val2 是 val1 的一个拷贝
undefined
> val1 = 11; // 修改 val1
11
> val2; // val2 没变
23
> let str1 = "abc"; // 下面同理
undefined
> let str2 = str1;
undefined
> str2 = "aaa";
'aaa'
> str1;
'abc'
> 
```

但是，不同于之前的那些基本数据，比如字符串和数字，数组和对象在使用 `=` 进行赋值的时候，其实没有进行复制，而是让两者指向**同一个**数组或者对象，就像是同一个数组或者对象有了两个名字，例如：

``` js
> let arr1 = [12, 22];
undefined
> let arr2 = arr1; // 两个其实是同一个
undefined
> arr1;
[ 12, 22 ]
> arr2;
[ 12, 22 ]
> arr2[1] = 1; // 直接修改，结果两个变量都变了，说明是指向同一个数组的
1
> arr1;
[ 12, 1 ]
> arr2;
[ 12, 1 ]
```

类似的，对象也是一样。如果要复制的话，可以使用 `Array.from()` 方法。

``` js
> let arr1 = [12, 22];
undefined
> let arr2 = Array.from(arr1);
undefined
> arr1;
[ 12, 22 ]
> arr2;
[ 12, 22 ]
> arr2[1] = 1;
1
> arr1; // 现在这个值没有变了
[ 12, 22 ]
> arr2;
[ 12, 1 ]
> 
```

### 参数

函数的参数传入之后，如果我们修改了参数，会发生什么？

直接跑一遍代码，清楚明了：

``` js
function test(x) {
    console.log("In function test, x = " + x);
    x = 3;
    console.log("After you changed, x = " + x);
}

let a = 1;
console.log("Before called the function, a = " + a);
test(a);
console.log("After called the function, a = " + a);
```

输出：

``` text
Before called the function, a = 1
In function test, x = 1
After you changed, x = 3
After called the function, a = 1
```

是不是非常清楚，函数 `test` 改了一个寂寞，最后 a 的值还是没变，其实函数的参数传递，就类似对每个参数进行了一次赋值，函数里面的变量和外面的不是同一个变量。类似的，如果传入的是**数组**和**对象**，情况就不太一样了：

``` js
function test(x) {
    console.log("In function test, x = " + x.join(','));
    x[0] = 3;
    console.log("After you changed, x = " + x.join(','));
}

let a = [1, 3, 5];
console.log("Before called the function, a = " + a.join(','));
test(a);
console.log("After called the function, a = " + a.join(','));
```

输出：

``` text
Before called the function, a = 1,3,5
In function test, x = 1,3,5
After you changed, x = 3,3,5
After called the function, a = 3,3,5
```

### 定义域

函数里面的定义的值不会占用掉外面的名称，更不会占用掉其他函数里面定义的变量名。比如说这个：

``` js
let x = "x global";

function test1() {
    let x = "x in test1()";
    console.log(x);
}

function test2() {
    let x = "x in test2()";
    console.log(x);
}

test1();
test2();
console.log(x);
```

输出：

``` text
x in test1()
x in test2()
x global
```

## 函数和对象

我们之前谈过了对象，现在是进一步扩充它的时候了。

### 函数作为值

函数可以被作为一个值赋值给一个变量：

``` js
function add(a, b) {
    return a + b;
}
let myadd = add;
let x = myadd(1, 3);
```

更加常用的是这么写：

``` js
let myadd = function (a, b) {
    return a + b;
}
```

这种情况下面会创造一个**匿名函数**，并且将这个函数赋值给 myadd 变量，使它的值成为一个函数，并且可以使用函数的方式调用。

### 方法

那么，既然函数可以赋值给普通变量，那么也可以赋值给一个对象成员了。一个函数成员叫做**方法**。，比如我们举个例子：

``` js
let cat = {
    name: "Ket",
    say: function() {
        console.log("My name is " + this.name);
    }
}
cat.say();
```

你也许在我们的方法里注意到了一些奇怪的地方， `this` 到底是什么？

`this` 指的是正在运行这个函数的对象。你可能会很奇怪为什么不能直接使用 `cat` 来代指而是用这个奇怪的关键字。这是因为对象是可以被复制 (更准确地说是**继承**) 的，这可以构造一个新的对象。如果直接使用 `cat` 就会导致这个代码不能指向被复制后的对象。我们以后会在进阶的 JS 里面提到。下面举个简单的例子， `Object.create()` 方法：

``` js
let cat1 = {
    name: "Ket",
    say: function() {
        console.log("My name is " + this.name);
    }
}
let cat2 = Object.create(cat1);
cat2.name = "Bill";
cat1.say();
cat2.say();

let badCat1 = { // 一个不好的例子
    name: "Steve",
    say: function() {
        console.log("My name is " + badCat1.name); 
    } 
};
let badCat2 = Object.create(badCat1);
badCat2.name = "重干是老鼠";
badCat1.say();
badCat2.say();
```

输出：

``` js
My name is Ket
My name is Bill
My name is Steve
My name is Steve
```

可以看到最后那个函数并没有指向正确的对象，导致输出了错误的值。

## 大家都是函数

那么，我们可以了解了，之前那些不明不白的什么 `console.log()` 什么 `join()` 什么 `split()` 什么 `Math.floor()`，通通都是函数或者方法，就和我们写出来的一样。

## 下一步

到了现在 JS 的基本语法你都已经掌握了，下面到了要拿这个新的工具去做点什么的时候了。

下一章： **DOM**！我们将会正式用 JS 去对网页做点事情。

## 练习

没啥好些的，接下来就直接是 DOM 了。我也累了，改天再更点啥吧。
