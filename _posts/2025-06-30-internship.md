---
layout:     post
title:      "实习日志"
subtitle:   "主要记录在某信息技术服务有限公司的实习经历"
date:       2025-06-30 12:00:00
author:     "hangyangjun"
header-img: "img/training.png"
tags:
    - 记录
    - 实习
    - java
---
## stage 1 上班之前
今天开会大概讲了一下，关于实习的流程，当然没有具体内容。  
只是关于实习打卡、报告、证明之类的要注意的事情。  
过几天还会分配指导老师

其实还是很想回家的，一个是因为想趁着暑假好好调整一下，再一个就是吃预制菜吃腻了，想吃家的味道。

## stage 2 第一步

首先是经历了一系列的信息不对等造成的小矛盾😇，当然我非常不擅长处理这些矛盾，好在有老师和同学们的帮助,信息差真的很致命  

了解到实习工作主要负责中端，我还是第一次知道有中端这个东西，看来有的学了  
吐槽：hr回复速度一度让我以为我断网了

## stage 3 第一天
### 安装开发环境
- [java 1.8](https://www.oracle.com/cn/java/)  
java1.8就是java8，我之前装的java21

- [maven](https://maven.apache.org/)  
项目管理工具，安装最麻烦的一个 跟随教程：[maven的下载与安装](https://blog.csdn.net/u012660464/article/details/114113349)

- [idea](https://www.jetbrains.com/idea/download/other.html)  
新下载了一个 2025的 IntelliJ IDEA 社区版

- [mysql](https://dev.mysql.com/downloads/mysql/)  
安装过了

- [navicat](https://www.navicat.com.cn/download/navicat-premium-lite)  
还得注册

- [xmind](https://xmind.cn/)  
思维导图软件，有网页版

### 作业
1.安装环境。  
2.http协议是什么。由几部分组成。  
3.http协议中，方法有哪些？header常见的属性有哪些什么作用？body是什么，怎么表述数据？  
4.Json数据能够表述哪几种数据类型？他的格式是什么样的？  

**HTTP协议**（HyperText Transfer Protocol，超文本传输协议）是用于在Web浏览器和服务器之间传输超文本（如HTML）的应用层协议。它基于客户端-服务器模型，采用请求-响应模式工作，默认使用TCP端口80（HTTPS使用443）。


|组成部分||
|----|----|
|请求行（Request Line）：|包含方法、URL和协议版本（如 GET /index.html HTTP/1.1）|  
|请求头（Headers）：|键值对形式，提供元信息（如 User-Agent: Chrome）|
|空行（CRLF）：|分隔头部和主体|   
|请求体（Body，可选）：|传输数据（如表单提交、JSON等）|

|响应结构类似||
|----|----|
|状态行（Status Line）：|包含协议版本、状态码和原因短语（如 HTTP/1.1 200 OK）|  
|响应头（Headers）：|如 Content-Type: text/html|
|空行||  
|响应体：|返回的资源内容（如HTML页面）。  


|HTTP方法（请求方法）：||
|----|----|
|GET：|获取资源（数据在URL中，无Body）|  
POST：|提交数据（数据在Body中）。  
PUT：|替换整个资源（幂等）。  
DELETE：|删除资源。  
PATCH：|部分更新资源。  
HEAD：|获取响应头（无Body）。  
OPTIONS：|查询服务器支持的通信选项。 


**常见Header属性及作用：**

|通用头：||  
|----|----|
Connection:| keep-alive（保持长连接）  
Cache-Control:| no-cache（控制缓存行为）  

|请求头：||
|----|----|  
Host: |example.com（指定服务器域名）  
User-Agent:| Mozilla/5.0（客户端信息）  
Accept: |application/json（声明可接收的数据类型）  
Content-Type:| application/x-www-form-urlencoded（Body数据格式）  

|响应头：||
|----|----|  
|Content-Type: |text/html（响应体数据类型）  
Set-Cookie: |id=123（设置Cookie）  
Location: |/new-page（重定向目标）  

**Body的作用与表述：**  
*作用：* 传输请求或响应的实际数据（如表单、文件、JSON等）  

*表述：*  
表单数据：application/x-www-form-urlencoded（键值对编码）  
JSON：application/json（如 {"name": "Alice"}）  
文件上传：multipart/form-data（多部分表单）  
二进制数据：application/octet-stream（如图片、PDF）  

**JSON的数据类型及格式**  
|JSON（JavaScript Object Notation）支持以下数据类型：||||
|----|----|----|----|
字符串（String）：|"name": |"Alice"|需用双引号  
数字（Number）：|"age": |25|整数或浮点数  
布尔值（Boolean）：|"isStudent": |true|true或false  
对象（Object）：|"person": |{"name": "Bob"}|键值对集合  
数组（Array）：|"hobbies": |["reading", "swimming"]|有序集合  
空值（Null）：|"middleName": |null|  


**JSON格式示例：**
```json
{
  "name": "Alice",
  "age": 25,
  "isStudent": true,
  "address": {
    "city": "New York",
    "zip": "10001"
  },
  "courses": ["Math", "Science"],
  "middleName": null
}
```

**特点**：  
键必须用双引号包裹  
数据以层级结构组织，支持嵌套  
轻量级，易于解析（广泛用于API数据交换）

## stage 4 继续

今天没什么事情，复习一下java，笔记我再单开一个博客好了  
还有maven也要学一下

### 培训1-接口学习

今天公司老师讲了一些东西，消化一下，还有一些作业

关于 spring boot 的接口传参  
还有 postman 工具

intellij idea 社区版新建spring boot项目很麻烦啊，只能装一个学习版了  
参考：  
- [IDEA 安装、破解和汉化教程【新】](https://www.cnblogs.com/N1ko/p/18020866)  
- [idea社区版本创建springboot项目的三种方式](https://developer.aliyun.com/article/1625955)


然后在idea里运行java还是遇到些许困难  
首先要解决的是jdk版本不匹配问题  
作业code—1换成jdk1.8就可以编译了

遇到的问题：
1. [无法检索应用程序 JMX 服务 URL](https://developer.aliyun.com/article/1346627)
2. [Java 包装类](https://www.cainiaojc.com/java/java-wrapper.html)
3. [安装commons-codec](https://blog.csdn.net/chujia1956/article/details/100674184)


运行起来之后  
地址：http://127.0.0.1:9001/api/v1/get-1  
下载了一个postman进行接口测试

.http 文件也可以进行接口调用

get传参  
可用地址或参数

post有多种传参方式  
params、请求体json、form-data

研究了一下apicontroller的方法，着手写接口练习  
直接复制粘贴，改改名字就好，最后一个传文件的接口还有些难度。不过在ai的指导下还是完成了所有功能，包括扩展的保存和对比md5功能

今天继续复习java基础，具体写在另一篇博客  
...  
最近这几天学java学的我头发要掉了

### 培训2-使用 Spring Boot 连接数据库
遇到的问题：
1. jdk版本问题
2. MySQL连接问题
3. 指定数据库方言

**依赖**  
- JPA 指 Java Persistence API，是Java EE 平台规范中用于管理Java 对象和关系数据库之间持久化数据的标准API。简单来说，JPA 提供了一种将Java 对象映射到数据库表的方式，使得开发者可以用操作对象的方式来操作数据库，而无需直接编写SQL语句。
- jpa-spec **动态拼接属性** 用于构造查询条件 [jpa-spec](https://github.com/wenhao/jpa-spec)
- Spring Web 提供web接口
- lombok 自动生成get set方法 构造方法
- MySQL Driver

Java与Oracle、PostgresSQL数据类型对应
| Java    | Oracle                      | PostgresSQL | MySQL              |
| ------- | --------------------------- | ----------- | ------------------ |
| Boolean | number(1)                   | boolean     | boolean            |
| Byte    | number(2)                   |             |                    |
| Short   | number(3)~number(4)         | int2        |                    |
| Integer | number(5)~number(9)         | int4        | integer            |
| Long    | number(10)~number(18)       | int8        | integer            |
| Float   | number(m,n)m:长度n:小数位数 | float4      | float              |
| Double  | number(m,n)m:长度n:小数位数 | float8      | double             |
| String  | varchar2                    | varchar     | text               |
| Date    | timestamp                   | timestamp   | datetime/timestamp |
| Byte[]  | blob ：二进制存储           |             | blob               |
| String  | clob：大文本存储            | text        | longtext           |

直接在AccountRepository写接口，甚至不用实现

留的关于数据库操作的任务算基本完成了，但是我这一知半解，java还真是难理解，感觉过一小会就会忘得一干二净。

### 其他培训
Spring Boot

angular

以及其他，以后再更新


## 提交规范

其实是 **Commit Message 的规范写法**，常见的一种叫 **Conventional Commits**。

核心就是在 Git 提交时，先写一个 **类型(type)**，再写简短的说明。比如：

* **feat:** 新功能（feature）
* **fix:** 修复 bug
* **docs:** 文档修改
* **style:** 代码格式调整（不影响逻辑）
* **refactor:** 重构（既不是新功能也不是修复 bug）
* **test:** 增加或修改测试
* **chore:** 构建过程或辅助工具的变动

好处：

1. 团队一眼就能看出提交的性质。
2. 自动生成更新日志（changelog）时更清晰。
3. 项目管理工具（比如 CI/CD）可以根据提交类型触发不同流程。

例子：

* `feat: 新增登录验证码功能` → 表示增加了一个功能。
* `fix: 修复密码重置接口超时问题` → 表示修了一个 bug。


**PRD（产品需求文档）** 是产品经理用来描述产品功能和需求的重要工具。它的主要目的是将产品的功能、特性等要求详细描述，以便设计人员和开发人员能够根据PRD文档直接开展工作。

## Shell脚本

**Shell 脚本就是一堆命令写在一个文件里，交给 Shell（命令解释器）一次性执行**。

在 Linux 里敲：

```bash
cd /var/log
tar -czf backup.tar.gz *.log
```

如果每天都要重复这些命令，就很麻烦。写成一个脚本：

```bash
#!/bin/bash
cd /var/log
tar -czf backup-$(date +%F).tar.gz *.log
```

保存为 `backup.sh`，然后 `bash backup.sh` 就能一键执行。

它的作用：

* **自动化**：重复的工作（日志清理、备份、部署）交给脚本。
* **运维必备**：批量操作服务器、监控进程、定时任务。
* **轻量灵活**：比写一个完整的程序简单，直接调用系统命令。

换句话说，Shell 脚本是运维和开发日常里最常见的“工具人”。

要不要我帮你写一个“日志自动归档”的简易 Shell 脚本例子？可以直接放在简历项目里点缀一下。

好，来个简洁版，既能看出思路，又不会太复杂：

```bash
#!/bin/bash
# 日志自动归档脚本 log_archive.sh

# 日志目录
LOG_DIR="/var/log/myapp"
# 归档目录
ARCHIVE_DIR="/var/log/myapp/archive"

# 确保归档目录存在
mkdir -p $ARCHIVE_DIR

# 把昨天的日志打包归档，并按日期命名
DATE=$(date -d "yesterday" +%F)
tar -czf $ARCHIVE_DIR/logs-$DATE.tar.gz $LOG_DIR/*.log 2>/dev/null

# 清理 30 天前的归档文件
find $ARCHIVE_DIR -name "*.tar.gz" -mtime +30 -exec rm {} \;

echo "[$(date +%F_%T)] 日志归档完成"
```

配合 **定时任务（crontab）**，比如每天凌晨 1 点跑一次：

```
0 1 * * * /bin/bash /path/to/log_archive.sh
```

这样：

* 日志每天都会被自动打包归档
* 保存 30 天，老的自动删掉
* 运维效率直接提升，不用人工管理

——这种小脚本放到简历里就能写成「编写 Shell 脚本实现日志自动归档，减少人工操作，提升运维效率约 20%」。

要不要我帮你把这个例子再精简成一行“简历项目亮点”，直接可以塞进你的经历？

## while
你提到的 `while ... do ... done` 是 Shell 脚本中的**循环结构**，用于重复执行一段命令，直到满足退出条件。它的基本语法是：

```bash
while 条件; do
  # 循环体：要重复执行的命令
done
```


### 核心作用
当 `while` 后面的“条件”为**真（成立）** 时，就会执行 `do` 和 `done` 之间的“循环体”，执行完后再次判断条件，直到条件为**假（不成立）** 时，循环结束。


### 结合你的例子理解
在之前的命令中：
```bash
awk ... /etc/passwd | while read user; do
  passwd -S $user | grep -q "NP" && echo "警告：用户 $user 可登录且密码为空"
done
```
这里的 `while read user` 是一种常见用法：
- `read user`：从管道（`|`）接收前面 `awk` 命令输出的内容（即用户名），每次读取一行，赋值给变量 `user`。
- `while read user`：只要能从管道中读到内容（即还有未处理的用户名），条件就为“真”，就会执行循环体。
- 循环体：检查当前 `user` 的密码状态，若为空密码则输出警告。
- 当所有用户名都处理完（管道中没有内容了），`read user` 会返回非 0 状态码（条件为“假”），循环结束。


### 简单示例
比如遍历输出 1~3 的数字：
```bash
i=1
while [ $i -le 3 ]; do  # 条件：i 小于等于 3
  echo $i
  i=$((i+1))  # i 自增 1
done
```
输出：
```
1
2
3
```


### 总结
`while ... do ... done` 是 Shell 中用于“重复执行命令”的循环结构，通过判断条件的真假来控制循环是否继续。在你的系统检查命令中，它的作用是**逐个处理前面筛选出的用户名**，实现批量检查的功能。