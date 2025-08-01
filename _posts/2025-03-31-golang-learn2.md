---
layout:     post
title:      "go语言学习笔记-part2"
subtitle:   "与其在宿舍睡觉，不如学点新东西"
date:       2025-05-26 12:00:00
author:     "hangyangjun"
header-img: "img/go.jpg"
tags:
    - 笔记
    - go
    - 学习
    - 书
    - 基础
---
> 参考资料：[《Go语言趣学指南》](https://huangz.works/gpwg/preview/lession1.html#id1)  

## 多语言文本
字符串字面量--使用双引号包起来的多个字符  
双引号会被推断为string类型，所以三种赋值操作结果是相同的  
没赋值时的零值是空字符串  

**原始字符串字面量**：  
字符串字面量可以包含转义字符，如果不想转义可以用` `` ` (反引号)包围文本  
还可以在代码里跨越文本行，打印时也会显示换行

### 字符、代码点、符文和字节

代码点：指分配给每个字符的唯一编号/Unicode的数值

`rune`（符文）类型用于表示单个**统一代码点（Unicode）**该类型也是int32类型的别名

`byte` 是uint8的别名 此类型可以表示二进制数据，也可表示ASCII（128个为unicode子集）定义的字符

--------------

虽然用%c进行输出，任意一种类型都行，但用别名rune可以表明数代表字符而不是数字
