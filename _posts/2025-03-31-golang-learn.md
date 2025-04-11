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

# 新建项目
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
成功输出: **Hello, World!**  
<br>

## 解释
`package` 关键字声明了代码所属的包，在本例中这个包的名字就是 `main` 。 所有用 Go 编写的代码都会被组织成各式各样的包，并且每个包都对应一个单独的构想。 比如 Go 语言本身就提供了一个面向数学、压缩、加密、图像处理等领域的标准库。  

在 `package` 关键字之后， 代码使用了 `import` 关键字来导入自己将要用到的包。 一个包可以包含任意数量的函数。 比如 `math` 包就提供了诸如 Sin 、 Cos 、 Tan 和 Sqrt （平方根）等函数，而此处用到的 `fmt` 包则提供了用于格式化输入和输出的函数。 因为在屏幕上显示文本是一个非常常用的操作，所以 Go 使用了缩写 fmt 作为包名。 Gopher 们通常把这个包的名字读作“FŌŌMT!”，给人的感觉仿佛就像这个库是使用漫画书上的大爆炸字体撰写的一样。  

`func` 关键字用于声明函数，在本例中这个函数的名字就是 `main` 。 每个函数的体（body）都需要使用大括号 {} 实施包围，这样 Go 才能知道每个函数从何处开始，又在何处结束。  

**`main` 这一标识符（identifier）具有特殊意义。 当我们运行一个 Go 程序的时候，它总是从 `main` 包的 `main` 函数开始运行。 如果 `main` 不存在，那么 Go 编译器将报告一个错误，因为它无法得知程序应该从何处开始执行。**  

为了打印出一个由文本组成的行，例子中的代码使用了 `Println` 函数（其中 ln 为行的英文字母 line 的缩写）。 每次用到被导入包中的某个函数时，我们都需要在函数的名字前面加上包的名字以及一个点号作为前缀。 比如代码清单中的 `Println` 函数前面就带有 `fmt` 以及一个点号作为前缀，这是因为 `Println` 函数就是由被导入的 `fmt` 包提供的。 **Go 的这一特性可以让用户在阅读代码的时候立即弄清楚各个函数分别来源于哪个包。**  

## 挑剔的左大括号`{`
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

上面的代码清单会调用 `Print` 函数好几次, 另一种方法是调用 ***`Println`*** 函数，并向它传递*一组由**逗号**分隔的参数*, 如：(\n换行)
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
// 上面这两行代码将打印出以下内容：
// SpaceX         $  94
// Virgin Galactic$ 100
```  

## 常量和变量
两个新的关键字 `const` 和 `var` ，它们分别用于声明`常量`和`变量`
```go
// 例：How long does it take to get to Mars?
    const lightSpeed = 299792 // km/s 常量 光速
    var distance = 56000000   // km 变量 地火距离
    fmt.Println(distance/lightSpeed, "seconds") // 打印出“186 seconds”
    distance = 401000000  //地火最远距离
    fmt.Println(distance/lightSpeed, "seconds") // 打印出“1337 seconds”
```  
``常量`` 是**不能修改**的，否则编译器报错  
``变量`` 必须先**声明**后使用。  
### 一次声明多个变量
```go
var (
     distance = 56000000
     speed = 100800
)
或者
var distance, speed = 56000000, 100800
```
### 赋值增量快捷方式
`a*=b` == `a=a*b`  或 `+=` 和 `++` `--`等不过多赘述  
<font color=yellow>**Go并不支持 ``++count`` 这样的前置加法操作**  </font>  

## 生成随机数
使用rand包，但是是伪随机
```go
package main

import (
    "fmt"
    "math/rand"//导入包 调用 Intn 函数的时候只需要使用包名 rand 作为前缀即可，不需要使用整个导入路径。
)

func main() {                  //搞个1-10的随机数
    var num = rand.Intn(10) + 1//此处不加1触发典型的计算机编程错误：差一错误（off-by-one error）
    fmt.Println(num)
}
```  
## 循环和分支
>注意: 某些编程语言对于`真`的定义比较宽松。比如 Python 和 JavaScript 就把空文本 "" 和数字零看作是`假`， 但是 Ruby 和 Elixir 却把这两个值看作是`真`。    
<font color=yellow>对于 Go 来说， `true` 是唯一的`真`值， 而 `flase` 则是唯一的`假`值。</font>  

```go
package main

import (
    "fmt"
    "strings" //导包
)

func main() {
    fmt.Println("You find yourself in a dimly lit cavern.")
    var command = "walk outside"
    var exit = strings.Contains(command, "outside")  //Contains 函数来检查变量是否包含“outside”，返回布尔变值
    fmt.Println("You leave the cave:", exit)
 }
```

### 比较

== 相等
!= 不相等
\< 小于
\> 大于
\<= 小于等于
\>= 大于等于。
在此不赘述  
如：`var minor = age < 18` 变量 minor为布尔值  

>注意： JavaScript 和 PHP 都提供了特殊的三等号（threequals）运算符来实现严格的相等性检查。 在这些语言中， 宽松检查 "1" == 1 的结果为真， 而严格检查 "1"  ===  1 的结果则为假。 Go 只提供了一个相等运算符， 并且它不允许直接比较文本和数字。  

### `if` 判断
```go
var command = "go east"
    if command == "go east" {           // 检查命令是否为“go east”
         fmt.Println("You head further up the mountain.")
    } else if command == "go inside" {  // 在第一次检查为假之后，检查命令是否为“go inside”
         fmt.Println("You enter the cave where you live out the rest of your life.")
    } else {                            // 如果前两次检查都为假，那么执行第三个分支
         fmt.Println("Didn't quite get that.")
    }
```  
>注意：不要试图用赋值操作符 = 来代替相等运算符 ==  
**`else` 等需要与上一`if`或`else if`的`}`写在同一行**

逻辑运算符 `||` 代表“逻辑或”，而逻辑运算符 `&&` 则代表“逻辑与” `!` "非"  

**短路逻辑**： 如果位于 `||` 运算符之前的第一个条件为真，那么位于运算符之后的条件就可以被忽略  
<br>  

### `switch` 分支判断
```go
var command = "go inside"
switch command {    // 将命令和给定的多个分支进行比较
case "go east":
    fmt.Println("You head further up the mountain.")
case "enter cave", "go inside":     // 使用逗号分隔可选值
    fmt.Println("You find yourself in a dimly lit cavern.")
default:        //默认 当没有case触发
    fmt.Println("Didn't quite get that.")
}
```
**case 可用逗号分隔可选值**， 且与C不同的，switch后不加（括号）  
**也可在每个分支中单独设置比较条件**  `case zhu == 6`
>在 C、Java、JavaScript 等语言中， 下降是 switch 语句各个分支的默认行为。 
Go需要显式地使用 fallthrough 关键字才会引发下降。也就是不用break了。

### `for` 循环
```go
package main       //倒计时
import (
    "fmt"
    "time"
)

func main() {
    var count = 10              // 声明并初始化
    for count > 0 {             // 为循环设置条件
        fmt.Println(count)
        time.Sleep(time.Second) // sleep 一秒
        count--                 // 每次循环之后将计数器的值减一，以免产生无限循环
    }
    fmt.Println("Liftoff!")
}
```
**也可以不设条件，在循环内部判断break**  

## 变量作用域
Go 的作用域通常会随着大括号 {} 的出现而开启和结束  
### 变量简短声明：
```go
var count = 10
count := 10            //二者等价
```
**简短声明还可以用在一些 `var` 关键字无法使用的地方(if fo switch)**
但包作用域不允许使用简短声明  

```go
for count := 10; count > 0; count-- {
    fmt.Println(count)
}    // 随着循环结束，count 变量将不再处于作用域之内。
```
为了代码的可读性考虑， 声明变量的位置和使用变量的位置应该尽可能地贴近。  
简短声明还可以在 `if` 语句里面声明新的变量,如：`if num := rand.Intn(3); num == 0 {`  
也可以用在 `switch` 语句里面。`switch num := rand.Intn(10); num {`包括`case`和`default`  

尽管狭窄的作用域有助于减少脑力负担，但过分约束变量将损害代码的可读性。 在遇到这种问题的时候，我们应该根据具体情况逐步实施重构，直到代码的可读性能够满足我们的要求为止。如果代码重复是由变量声明引起的， 那么变量可能就是被约束得太紧了。  

## 总结小练习
```go
package main

import (
	"fmt"
	"math/rand"
)

func main() { // 声明一个名为 main 的函数
	fmt.Printf("太空公司           飞行天数       飞行类型       价格（百万美元）\n")
	for i:=10 ; i>0 ; i--{
		company := ""
		switch i:=rand.Intn(3) ;i{
		case 0:
			company = "Virgin Galactic"
		case 1:
			company = "SpaceX"
		case 2:
			company = "Space Adventures"
		}
		speed := rand.Intn(15)+16
		days := 62100000/speed/3600/24   
		types := "单程"
		type1 := 1
		if j:=rand.Intn(2) ;j==0 {
			types = "往返"
			type1 = 2
		}
		price := (36+speed-16)*type1  //价格这里踩坑了，一开始计算带一个比例系数，结果一直等于零，原来是忘了转换float，结果0.几的都成零了QAQ
		fmt.Printf("%-20v%-15v%-13v%-10v\n",company,days,types,price)
    }
}

输出：
太空公司           飞行天数       飞行类型       价格（百万美元）
SpaceX              24             单程           49        
Space Adventures    29             单程           44
Space Adventures    32             单程           42
Virgin Galactic     31             往返           86
Virgin Galactic     35             往返           80
Virgin Galactic     26             往返           94
SpaceX              34             单程           41
Space Adventures    34             往返           82
SpaceX              24             往返           98
Virgin Galactic     31             单程           43
```

# 类型
## 浮点数
>IEEE-754 标准 储存浮点数  [csdn:简读+案例=秒懂](https://blog.csdn.net/weixin_47713503/article/details/108699001)  

go编译器可以自动判断类型，带小数点的会被设置为`float64`类型  
`days := 365.2425`  或  `var days float64 = 365.2425`  是同等的  
如果变量为整数，需要**显式指定**，若定义变量未赋值，则默认为**0**（零值zero value）

go中默认浮点为 `floar64` 也就是**双精度**，占用**8字节**，另一种`float32` **单精度** **4字节** (当数据量很大时，可以用精度换空间)
```go
	f64 := math.Pi        //很直观的例子
	var f32 float32 = math.Pi
	fmt.Print(f64,f32)
```
### 输出
使用 `Printf` 指定位数格式化输出，如  `fmt.Printf("%4.2f",f64)`   
**注意：此时`4`为输出宽度（限制最少输出*字符*，左补`空格` 若想补`0`则需要：`%04.2`），`2`为小数精度**  
`%f` 默认**6位小数**

### 不精确
计算机中浮点数常常出现**舍入错误**，这会造成浮点数不够“精确”  
可以通过**限制输出位数**解决（或者干脆别用）  
或者先计算乘法，来提高精度

### 比较
在两个浮点数（0.1+0.2）中本应是**0.3**的结果变成了**0.30000000000000004**
可以通过计算两个浮点数之间的差值，判断二者是否相等
```go
    f64 := 0.1
    f64 += 0.2
    fmt.Println(f64 == 3)
    fmt.Println(math.Abs(f64-0.3)<0.0001)    //Abs是计算绝对值
```
单个操作引发浮点数错误的上限值被称为机械最小值，对于float64值为2<sup>-52</sup>，float32为<sup>-23<sup>  

但是浮点数的错误**累计**的很快，所以处理好**容差**很重要。  
## 整数
很难想象go竟然有**10种整数类型**。  

|  类型 |  取值范围  | 内存占用 | 
|:---:|:---|:---:|
|int8 |-128至127|8位（1字节）|
|uint8|0至255|8位（1字节）|
|int16|-32768至32767|16位（2字节）|
|uint16|0至65535|16位（2字节）|
|int32|-2147483648至2147483647|32位（4字节）|
|uint32|0至4294967295|32位（4字节）|
|int64|-9223372036854775808至9223372036854775807|64位（8字节）|
|uint64|0至18446744073709551615|64位（8字节）|
|int|自动选择，但是并不能想当然等同于int64或int32||
|uint|自动选择，同上||


### 检测类型
**使用`Printf`函数提供的格式化变量`%T`查看指定变量的类型**  
```go
days := 365.2425
fmt.Printf("%T,%[1]v\n",days)       //避免代码重复
```
**`[1]`加入第二个格式化变量中，来重复使用第一个格式化变量的值**  

### 8位的`uint8`有什么用?
层叠样式表（CSS）刚好需要0~255来表示红绿蓝三原色，也就是用uint8最合适不过了，既可以避免**出现错误值**，也可以**减少存储空间**  

### go语言中的16进制数字
CSS通过16进制指定颜色，16进制有个好处，一个数字正好对应4个二进制位，2个16进制数字刚好对应1字节，所以非常方便。  

go语言中，16进制数字需带有 `0x` 前缀  
```go
var red, green, blue uint8 = 0, 141, 213  //等同于
var red, green, blue uint8 = 0x00, 0x8d, 0xd5

fmt.Printf("%02x %02x %02x",red, green, blue)  //02这里是零填充，左补0，对齐格式（color: #008dd5）
```
**可用`%x`或`%X`打印16进制**  

### 整数回绕
虽然整数不会出现精度问题，但是其取值范围有限，超出则会发生整数回绕现象（wrap around）  
简单来说就是 uint8 = 255 时再加 1 ，又回到 0 了  
或者int8 = 127 ++ 之后 等于 -128  

二进制格式化变量：`%b`  

这个原因就不具体解释了，在机组和数电中都学的比较清楚了  

##### 时间回绕
基于Unix的操作系统都使用协调世界时（UTC）1970.1.1以来的秒数来表示时间，但是对于int32来说这个时间不能超过2038年，好在我们还有int64，足够用到292277026596年

## 大数
>你是否觉得浮点不准，整数太小？快来试试大数吧！  

```go
var distance int64 = 41.3e12    //用指数形式写出到比邻星的距离（km）
```
但是对于到仙女星系的距离，uint64也不够用了（浮点数可以）  
### 我们需要big包
提供以下三种**类型**
- 存储大整数的 `big.Int`
- 存储任意精度浮点数 `big.Float`
- 存储如1/3的分数 `big.Rat`  

#### 使用

`big.Int` 类型 需要在等式的每个部分都被使用，基本方法为使用 `NewInt` 函数，接受一个`int64`类型输入，返回`big.Int`类型输出。  
```go
import("math/big")
...
lightSpeed := big.NewInt(299792)
```
超过`int64`取值上限时，给定一个 `string` 创建值：  
```go
distance := new(big.Int)
distance.SetString("2400000000000000000000",10)
```
这段代码创建`big.Int`变量后，调用`SetString`**方法**设置数值，其第二个参数是**10进制**的意思  

*不理解的部分无需在意，后面会讲到*  
```go
second := new(big.Int)//终于可以精确计算
second.Div(distance,lightSpeed)  //打印出需要的秒数
```
虽然精确，但是代价是麻烦和比较慢  

#### 常量有点不一样

有趣的是，声明一个不带类型的常量，超过int最大值时，与处理变量变得不同了起来
go语言不会推断其类型，而是直接标识为无类型（untyped） 如：  
```go
const distance = 2400000000000000000  //不会报错
```
除了用 const 进行声明，在程序里每个字面量值（literal value）也都是常量，也就是说如果数值很大也可以直接使用。如：  
```go
fmt.Println("Andromeda Galaxy is",240000000000000000/299792/86400,"light days away.") //打印结果正确
```
对用常量和字面量的计算都将在 **编译** 时执行，由于编译器也是go写的，所以在底层，无类型的数值常量由big包提供支持，也就不会像int型溢出之类的  

注意：尽管编译器用big包处理无类型数值常量，但是常量无法与big.Int值互换，如直接打印distance常量将引发溢出错误：  
```go
const distance = 240000000000000000000000
fmt.Println(distance)// int溢出
```
非常大常量很好，但是无法取代big包，就是说无类型常量被用作函数参数的时候，必须转换为有类型变量。  

## 多语言文本

