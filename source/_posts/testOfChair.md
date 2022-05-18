---
title: 一个小小测试
categories:
  - [计算机社, 尼泽·莫伯斯]
tags:
  - 公告
  - 期末
date: 2022-05-11 16:28:26
author: 尼泽·莫伯斯
cover:
---

# 地图 project

这是一个简单的团队合作的挑战项目，主要锻炼前端编程能力以及团队协作的能力。

## 需求介绍

Tux 前不久接到了一个任务，要做个小游戏。结果把这个事情忘记了，现在对面要看进度，但是它只画了一些地图。为了糊弄对方，现在需要你写个网页展示这些地图，假装这个游戏正在开发。

地图是一个 .zip 格式的文件，根目录下面有这么些文件

```text
wall.png
floor.png
start.png
end.png
mp1.txt
mp2.txt
...
mp*.txt
```

其中，`mp*.txt` 是地图，**可能有一个或者多个(最多九个，不用考虑两位数)**。`*.png` 则是一些图片文件，每一张 `32px*32px` 大小。这四个张用来显示地图。

mp*.txt 里面的内容是一个 N*M 的矩阵(N <= 20, M <= 20) (也就是最大面积 640\*640 像素)，大概看起来是这样的。(当然实际上肯定不是这样子的，不然就可以直接写成静态网页了)

```text
########
##....##
#..##..#
#S###.##
#...#.E#
########
```

其中 `#` 代表墙壁 (wall.png)，`.` 表示地板 (floor.png)， `S` 表示开始 (start.png)，`E` 表示结束 (end.png)。

你需要的是把它显示出来，每个字符对应成一张小型图片，这样排列成为一个二维的地图，比如这样子：

![maping](maping.png)

鉴于地图应该是存在本地，读档之后进行操作，那么我们的页面应该是要用户手动上传地图文件到页面，之后经过一系列操作，转到另一个显示地图的页面。

比如可以长这样

![drag file](dragfile.png)

显示地图的页面最好要支持多个地图。这是一种可能的 UI，通过一个轮播图片的形式来展示，左右按钮进行地图之间的切换。当然你也完全可以用更好的方法。

![preview](preview.png)

## 样例

这是用于测试的地图文件

[map.zip](map.zip)

## 帮助与提示

### 帮助

解析 zip 包需要用到一个叫做 zip.js 的库。鉴于对上传文件的解析操作过度复杂，而且也不属于前端基本功，我决定自己写好这一个函数，把 input 的 event 里面那个文件的引用传给这个函数，函数就可以把解析好的地图放进一个对象返回回去。这样可以方便大家开发。

一个用于参考的例子，示范了如何导入这个库并且使用，下载链接如下：

[下载](resolve.zip)

这是一个在线的页面，是上面的例子部署到 Github pages 上面 <https://yjzx-site.github.io/zipExample/>。选中自己的地图 zip，就可以看到材质和地图显示出来了。

这是个 async 函数，声明如下。需要加上 await 调用。

```js
/**
 * 
 * @typedef {Object} ResolvedMap
 * @param {ObjectURL} wall - 墙壁图片的引用，下同
 * @param {ObjectURL} floor
 * @param {ObjectURL} start
 * @param {ObjectURL} end
 * @param {Array<String>} maps - 每个 map 文件的内容的字符串，包括换行（最后文件尾也有换行）
 */

/**
 * 
 * @param {File} zipFile 
 * @returns {ResolvedMap}
 */
async function resolveFileToObject(zipFile) {
    /** waiting for further update */
}
```

一个返回值的例子

```js
{
    wall: [一个 ObjectURL，直接使用],
    floor: [同上],
    start: ,
    end: ,
    map: [
        "########\n##....##\n#..##..#\n#S###.##\n#...#.E#\n########",
        "########\n##....##\n#..##..#\n#S###.##\n#...#.E#\n########",
        ..
        .
    ]
}
```

### 提示

- 布局可以使用 bootstrap，可以通过直接下载到本地的方式引入，也可以使用 CDN (例如： <https://cdn.baomitu.com/>)
- ObjectURL 是一种文件引用，使用可以看 mdn [在web应用程序中使用文件](https://developer.mozilla.org/zh-CN/docs/Web/API/File/Using_files_from_web_applications#example.3a_using_object_urls_to_display_images)
- async 是个简单的异步方式 <https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Promises> 见 async 部分。

(待更新)

## 评分标准

每点 10 分。

### 功能 (60分)

- 能够拖进文件，并对这个文件进行操作
- 能够接受 Myfunc(提供的解析 zip 包函数) 的返回值，并且尝试解析
- 成功解析同时尝试打印到 div
- 成功打印到一个 div，并可正常显示
- 可以进行返回再上传新的地图
- 完整，与UI结合

### UI (40分)

- 有一个主页，显示上传控件
- 有一个轮播窗口，可以左右切换
- 可以显示当前文件名，有“返回上页”到按钮
- 要拥有一个美观的页面框架，不要裸控件
