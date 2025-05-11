---
layout:     post
title:      ""
subtitle:   ""
date:       2025-05- 12:00:00
author:     "hangyangjun"
header-img: "img/
tags:
    - 笔记
    - 记录
    - 学习
---

SSID，air，arp欺骗，网卡
研究老师留的课题，顺便把之前学习成果记录一下

# 无线局域网SSID搜索与探测（22）

主要是研究资料,找找文献

有点束手无策,请教一下ai:


## 摘要  
200字概述研究背景、核心方法、主要发现及安全意义，强调基于Kali Linux的实验验证
## 1. 引言
### 1.1 研究背景
- 全球WLAN设备数量统计（2020-2023年增长曲线图）
### 1.2 研究目标
- SSID探测的技术价值：网络审计、入侵检测、安全评估
## 2. 技术原理
### 2.1 802.11协议解析
（信标帧结构标注SSID字段位置）
### 2.2 SSID探测机制
主动探测-->Probe Request AP响应包含SSID
被动监听-->捕获Beacon帧 周期性广播SSID

### 2.3 Kali Linux工具链
airodump-ng工作流程
Wireshark过滤器：wlan.fc.type_subtype == 0x08

## 3. 实验设计与分析
### 3.1 实验环境
csv
设备,型号,配置
无线网卡,Alfa AWUS036ACH,支持802.11ac
测试AP,TP-Link Archer C7,隐藏SSID模式
操作系统,Kali Linux 2023.4,内核5.15.0
### 3.2 实验步骤
启用监听模式：airmon-ng start wlan0

捕获无线流量：airodump-ng wlan0mon

隐蔽SSID破解：aireplay-ng deauth攻击结合Probe响应分析

### 3.3 实验结果

（对比正常/隐藏SSID的捕获数据包数量统计表）

SSID类型	平均捕获时间	成功率
可见SSID	2.3s	100%
隐藏SSID	18.7s	83%
## 4. 安全防护建议
### 4.1 企业网络防护
禁用Probe Response帧

MAC地址过滤实施方案

### 4.2 检测技术演进
基于机器学习的异常SSID识别（技术演进路线图）

## 5. 研究结论
隐蔽SSID不能提供有效安全防护

2.4GHz频段探测成功率高5GHz频段37%

参考文献
[1] IEEE 802.11-2020. Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications
[2] Joshua Wright. 《无线网络安全攻防进阶》. 人民邮电出版社, 2018
[3] 实验数据集来源：Kali Linux官方文档及实验室测试数据


---

### 二、课程设计PPT大纲（图文结合）

**1. 封面页**（1页）  
- 标题：无线局域网SSID探测技术研究  
- 副标题：基于Kali Linux的网络安全分析  
- 作者/课程信息  

**2. 研究背景**（2页）  
- 图1：全球无线设备增长趋势（2018-2023）  
- 图2：常见SSID隐藏应用场景（企业/家庭/公共场所）  

**3. 技术原理**（3页）  
- 动图：802.11信标帧动态解析过程  
- 流程图：主动探测 vs 被动监听技术路径对比  
- Kali工具链架构图（airodump-ng+Wireshark协同工作）  

**4. 实验发现**（4页）  
- 表1：不同频段SSID探测成功率对比  
- 热力图：实验环境中AP信号强度分布  
- 关键结论：  
✓ 隐蔽SSID平均识别时间≤20秒  
✓ 5GHz频段需定向天线增强信号  

**5. 安全启示**（2页）  
- 企业网络防护方案拓扑图  
- 个人用户安全设置检查清单  

**6. 研究收获**（1页）  
- 技术层面：掌握802.11协议逆向分析方法  
- 实践层面：Kali Linux无线审计工具熟练度提升  

---

### 关键实施建议：
1. **图表制作**：使用Draw.io绘制协议解析图，PyPlot生成统计图表
2. **实验验证**：在封闭环境测试时记录视频片段（可选附加材料）
3. **学术规范**：确保所有引用标注格式统一（建议使用GB/T 7714标准）
4. **原创性强化**：通过对比不同厂商设备的探测差异增加独特发现







开始研究:

标准:
IEEE 802.11是现今无线局域网通用的标准，它是由电气和电子工程师协会（IEEE）所定义的无线网络通信的标准。

IEEE 802.11b  
其载波的频率为2.4GHz，可提供1、2、5.5及11Mbit/s的多重传送速度。它有时也被错误地被标为Wi-Fi。实际上Wi-Fi是一个商标,在2.4-GHz的ISM频段共有11个频宽为22MHz的频道可供使用，它是11个相互重叠的频段。IEEE 802.11b的后继标准是IEEE 802.11g

IEEE 802.11g
在2003年7月被通过。其载波的频率为2.4GHz（跟802.11b相同），共14个频段，802.11g的设备向下与802.11b兼容。
其后有些无线路由器厂商,将理论传输速度提升至108Mbit/s或125Mbit/s。

安全性

IEEE 802.11i是IEEE为了弥补802.11脆弱的安全加密功能（WEP，Wired Equivalent Privacy）而制定的修正案，其中定义了基于AES的全新加密协议CCMP（CTR with CBC-MAC Protocol）。Wi-Fi厂商采用802.11i的草案3为蓝图设计了一系列通信设备，随后称之为支持WPA（Wi-Fi Protected Access）的，这个协议包含了向前兼容RC4的加密协议TKIP（Temporal Key Integrity Protocol），它沿用了WEP所使用的硬件并修正了一些缺失，之后称将支持802.11i最终版协议的通信设备称为支持WPA2（Wi-Fi Protected Access 2）的。

参考:[IEEE 802.11_百度百科](https://baike.baidu.com/item/IEEE%20802.11/8447947)

802.11网络的基本元素

WLAN的组成
STA (Stations)：任何的无线终端设备（手机/PC/平板等）
AP （Access Point）：一种特殊的STA，无线接入点，负责信号收发与有线网络桥接
等，更上一级的设备

标识符
SSID(Service Set ID 服务集识别码)可以简单的理解为无线局域网络的名称 
BSSID(Basic Service Set Identifier)用来识别一个特定的无线网络，常与无线接入点（AP）的MAC地址相同
等等更大的集群或者其他细节不多赘述

参考：[IEEE 802.11协议基础知识整理_CSDN](https://blog.csdn.net/weixin_36178668/article/details/93622454)

SSID的作用
网络标识：区分同一区域内不同的无线网络
连接入口：用户通过选择SSID接入目标网络
管理依据：路由器通过SSID控制设备接入权限

SSID的技术特性
格式要求：
最大长度：32字节（支持ASCII字符，包括中文等Unicode字符）
区分大小写（例如“MyWiFi”与“mywifi”视为不同网络）
广播机制：
路由器通过信标帧（Beacon Frame） 周期性广播SSID（默认1秒/次）
隐藏SSID时，信标帧中SSID字段为空，但仍可通过探测请求/响应（Probe Request/Response） 捕获

SSID的网络安全意义
常见风险：
暴露信息：SSID命名可能泄露位置、用途等信息（如“440宿舍”）
钓鱼攻击：伪造同名SSID诱导用户连接（Evil Twin攻击）
隐藏SSID的局限性：通过airodump-ng工具仍可探测到隐藏SSID

SSID探测技术（基于Kali Linux）

被动监听：
通过捕获信标帧直接获取可见SSID：

```bash
airodump-ng wlan0mon --essid "目标SSID"
```

主动探测：
向隐藏SSID发送探测请求，触发AP响应：

```bash
aireplay-ng --deauth 10 -a AP_MAC wlan0mon  # 解除认证攻击迫使设备重连
```
正好此前自学了，Kali 中的 Aircrack-ng 这一套工具，买了一个USB网卡，假装“黑客”破解了自己手机的热点


参考文献
协议标准：IEEE 802.11-2020 第9章（管理帧结构）
Joshua Wright, Wireless Network Security: A Penetration Tester's Perspective（第4章 SSID探测技术）

研究要配合实践，首先启动vmware，打开之前下的KaliLinux


