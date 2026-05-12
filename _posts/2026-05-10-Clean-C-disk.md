---
layout: post
title: C盘爆满？“硬盘刺客”CapabilityAccessManager
subtitle: 在 C:\ProgramData\Microsoft\Windows\CapabilityAccessManager 路径下，有一个名为 CapabilityAccessManager.db-wal 的文件，竟然悄悄膨胀到了几十 GB 甚至上百 GB！
date: 2026-05-10 12:00:00
author: hangyangjun
header-img: img/training.png
tags:
  - 记录
  - 清理
---
> 参考资料：[CapabilityAccessManager is devouring my hard drive - Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5815087/capabilityaccessmanager-is-devouring-my-hard-drive)

>总之是太久没有写新博客了，我想说最近太忙了，但其实都是借口，总之今天看着爆满的c盘，使用 **WizTree** 扫描后惊讶的发现有一个名为`CapabilityAccessManager.db-wal`的文件竟然有30多G。我这寸土寸金的C盘真实容不下这么大的文件，这个看起来也不像什么重要的文件，今天必须得给他干了！

然后查了一圈，得知这个文件主要记录应用请求位置、摄像头、麦克风之类的日志。
那是真没用。而且这个文件受到保护，没法简单删除。

所以经过一些测试，可行的清理方案如下：

### 第一步：进入 Windows 安全模式

1. **按住Shift** ，同时点击“重启”**
2. 稍后进入蓝色界面，依次选择：**疑难解答** > **高级选项** > **启动设置** > **重启**
3. 再次重启后，屏幕上会出现一个列表，按 **F4**，进入安全模式
### 第二步：打开管理员命令提示符

进入安全模式后，点击“开始”菜单，搜索 cmd
找到“命令提示符”后，**选择“以管理员身份运行”**

### 第三步：输入命令（直接复制）

在cmd窗口中，依次复制粘贴以下命令。**每粘贴一行，按一次回车键执行**。

1：获取目标文件夹的所有权
```bash
takeown /f "C:\ProgramData\Microsoft\Windows\CapabilityAccessManager" /r /d y
```

2：停止相关服务
```bash
net stop camsvc
```

3：给自己赋予权限
```bash
icacls "C:\ProgramData\Microsoft\Windows\CapabilityAccessManager" /grant administrators:F /t
```

4：删除**整个文件夹**
经过测试如果只删除日志文件，会造成部分功能异常。
放心，删除后只会造成一些相关权限设置被重置，相比c盘爆满不值一提。
```bash
rd /s /q "C:\ProgramData\Microsoft\Windows\CapabilityAccessManager"
```
### 第四步：大功告成，正常重启

全部执行完毕后，正常重启电脑即可。  

重启后检查c盘，现在我电脑的C盘终于变成蓝色了。

### 第五步：处理后患
当然，清理是一方面，而为了减少以后的工作，找出真相又是另一方面。

其实可以通过Windows自带的设置就能看出罪魁祸首，在设置>隐私和安全性>应用权限中：点开位置、摄像头、麦克风等，查看“最近的活动”中显示的应用程序，如果某个应用程序出现过多，那大概率就是他造成的。

对于我这台电脑，应该是[**Rainmeter**](https://www.rainmeter.net/)一直请求位置造成的，不确定具体的原因，所以我直接删除了这个软件，本就是为了日常监控内存占用和硬盘容量的，结果确实造成我c盘爆满的凶手，有点讽刺了。

还有，根据资料，如果是戴尔电脑，可能是预装的一款名为 SmartByte
的网络管理软件造成的。直接卸载即可，没有任何影响。