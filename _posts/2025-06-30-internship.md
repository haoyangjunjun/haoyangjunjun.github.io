---
layout:     post
title:      "实习日志"
subtitle:   "主要记录在某信息技术服务有限公司的实习经历"
date:       2025-06-30 12:00:00
author:     "hangyangjun"
header-img: "img/training.png"
tags:
    - 记录
    - 学习
    - 实习
    - java
---
## stage 1 上班之前
今天开会大概讲了一下，关于实习的流程，当然没有具体内容。  
只是关于实习打卡、报告、证明之类的要注意的事情。  
过几天还会分配指导老师

其实还是很想回家的，一个是因为想趁着暑假好好调整一下，再一个就是吃预制菜吃腻了，想吃家的味道。

## stage 2 迈出第一步

首先是经历了一系列的信息不对等造成的小矛盾😇，当然我非常不擅长处理这些矛盾，好在有老师和同学们的帮助  
最后是由于人手不足，公司实习转为**线上**了，倒也不错，时间上安排自由些。  

了解到实习工作主要负责中端，我还是第一次知道有中端这个东西，看来有的学了  
吐槽：hr的回复速度让我一度以为我断网了

## stage 3 第一天上班
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
竟然还得注册

- [xmind](https://xmind.cn/)  
思维导图软件，有网页版

### 今日作业
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

## stage 4 继续学习

今天没什么事情，复习一下java，笔记我再单开一个博客好了  
还有maven也要学一下

今天公司老师讲了一些东西，消化一下，还有一些作业

关于 spring boot 的接口传参  
还有 postman 工具

intellij idea 社区版新建spring boot项目很麻烦啊，只能装一个学习版了  
参考：  
[IDEA 安装、破解和汉化教程【新】](https://www.cnblogs.com/N1ko/p/18020866)  
[idea社区版本创建springboot项目的三种方式](https://developer.aliyun.com/article/1625955)

### 接口学习

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

get传参  
可用地址或参数

post有多种传参方式  
params、请求体json、form-data

研究了一下apicontroller的方法，着手写接口练习  
直接复制粘贴，改改名字就好，最后一个传文件的接口还有些难度。不过在ai的指导下还是完成了所有功能，包括扩展的保存和对比md5功能

今天继续复习java基础，具体写在另一篇博客








