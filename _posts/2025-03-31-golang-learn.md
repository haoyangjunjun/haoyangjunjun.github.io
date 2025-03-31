---
layout:     post
title:      "go语言学习笔记"
subtitle:   "与其在宿舍睡觉，不如学点新东西"
date:       2025-03-31 12:00:00
author:     "hangyangjun"
header-img: "img/go.jpg"
tags:
    - 笔记
    - go
    - 学习
---
> 参考资料：[《Go语言趣学指南》](https://huangz.works/gpwg/preview/lession1.html#id1)  

# 什么是 go

Go作为Google在2009年推出的语言，其被设计成一门应用于搭载 Web 服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。  

对于高性能分布式系统领域而言，Go 语言无疑比大多数其它语言有着更高的开发效率。它提供了海量并行的支持，这对于游戏服务端的开发而言是再好不过了。  

尽管 Go 正在数据中心大放异彩，但它的应用场景并不仅限于工作区域。  

**Go 是一门编译语言**  
Go 不仅像解释语言一样简单和有趣，它还拥有编译语言快如闪电的性能优势以及坚如磐石的可靠性，并且由于 Go 是一门只包含几种简单概念的小型语言，所以它学习起来也相对比较快。  
<br><br>

# 还是直接开始吧

经历了一些并不愉快的安装和配置环境变量环节后.... 
>如：  
go env -w GO111MODULE=on  
go env -w GOPROXY=https://goproxy.cn  

## 新建项目
初始化go模块  
`go mod init test`  

在项目根目录下创建一个名为 `main.go` 的文件，并输入以下代码：
```go
package main                        // 声明本代码所属的包
import "fmt"                        // 导入 fmt 包，使其可用（fmt是format的缩写）
func main() {                       // 声明一个名为 main 的函数
    fmt.Println("Hello, World!")    // 在屏幕上打印
}
```
终端输入：`go run main.go`  
成功输出: Hello, World!  
<br>

#### 解释
`package` 关键字声明了代码所属的包，在本例中这个包的名字就是 `main` 。 所有用 Go 编写的代码都会被组织成各式各样的包，并且每个包都对应一个单独的构想。 比如 Go 语言本身就提供了一个面向数学、压缩、加密、图像处理等领域的标准库。  

在 `package` 关键字之后， 代码使用了 `import` 关键字来导入自己将要用到的包。 一个包可以包含任意数量的函数。 比如 `math` 包就提供了诸如 Sin 、 Cos 、 Tan 和 Sqrt （平方根）等函数，而此处用到的 `fmt` 包则提供了用于格式化输入和输出的函数。 因为在屏幕上显示文本是一个非常常用的操作，所以 Go 使用了缩写 fmt 作为包名。 Gopher 们通常把这个包的名字读作“FŌŌMT!”，给人的感觉仿佛就像这个库是使用漫画书上的大爆炸字体撰写的一样。  

`func` 关键字用于声明函数，在本例中这个函数的名字就是 `main` 。 每个函数的体（body）都需要使用大括号 {} 实施包围，这样 Go 才能知道每个函数从何处开始，又在何处结束。  

**`main` 这一标识符（identifier）具有特殊意义。 当我们运行一个 Go 程序的时候，它总是从 `main` 包的 `main` 函数开始运行。 如果 `main` 不存在，那么 Go 编译器将报告一个错误，因为它无法得知程序应该从何处开始执行。**  

为了打印出一个由文本组成的行，例子中的代码使用了 `Println` 函数（其中 ln 为行的英文字母 line 的缩写）。 每次用到被导入包中的某个函数时，我们都需要在函数的名字前面加上包的名字以及一个点号作为前缀。 比如代码清单中的 `Println` 函数前面就带有 `fmt` 以及一个点号作为前缀，这是因为 `Println` 函数就是由被导入的 `fmt` 包提供的。 **Go 的这一特性可以让用户在阅读代码的时候立即弄清楚各个函数分别来源于哪个包。**  

#### 挑剔的左大括号`{`
左大括号和 `func` 关键字需放在相同的行，否则报错，因为编译器分不清在哪放分号  


## 来点计算吧！
>取模运算符 % 能够计算出两个整数相除所得的余数  

下例计算本人的体重在火星减少的重量  
>有趣的事实：火星上的一年相当于地球的 687 天，同一物体在火星上的重量只有地球上的 38% 。  

```go                          
package main

import "fmt"

// main is the function where it all begins.            
func main() {
    fmt.Print("My weight on the surface of Mars is ")
    fmt.Print(135.0 * 0.3783)
    fmt.Print(" 斤, and I would be ")
    fmt.Print(21 * 365 / 687)
    fmt.Print(" years old.")
}
```  
结果：My weight on the surface of Mars is 51.0705 斤, and I would be 11 years old.  

上面的代码清单会调用 `Print` 函数好几次, 另一种方法是调用 ***`Println`*** 函数，并向它传递一组由逗号分隔的参数, 如：(\n换行)
```go
fmt.Println("My weight on the surface of Mars is", 149.0*0.3783, "lbs, and I would be", 41*365.2425/687, "years old.")
```
#### 格式化输出: `Printf` 函数
```go
fmt.Printf("My weight on the surface of %v is %v lbs.\n", "Earth", 149.0)
```
`Printf` 接受的第一个参数总是**文本**，第二个参数则是**表达式**，而文本中包含的格式化变量 `%v` 则会在之后被替换成表达式的**值**。  
`%v`之外的格式化变量请[查看文档](https://pkg.go.dev/fmt)  
`Printf` 除了可以在句子的任意位置将格式化变量替换成指定的值之外，还能够调整文本的位置。 比如说，用户可以通过给定带有宽度的格式化变量 `%4v` ，将文本的长度填充至 4 个字符长。 当宽度为正数时，空格将被填充至文本左边，而当宽度为负数时，空格将被填充至文本右边：
```go
fmt.Printf("%-15v$%4v\n", "SpaceX", 94)
fmt.Printf("%-15v$%4v\n", "Virgin Galactic", 100)
上面这两行代码将打印出以下内容：
SpaceX         $  94
Virgin Galactic$ 100
```


