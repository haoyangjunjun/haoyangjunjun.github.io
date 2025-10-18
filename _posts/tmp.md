# 随笔
国际化网站需解决时区问题，通常使用存储使用ut什么 时间，然后根据用户本地时间换算显示  

大部分知识必须经常使用才能记住并且熟练，比如现在我写markdown格式几乎不用思考，而对于写vue的东西却几乎什么也想不起来

未来的发展看似很好预测，但是时间久一点几乎是不可能进行预测的

DoH（DNS over HTTPS）是一种通过HTTPS协议进行DNS查询的方法，旨在增加DNS查询的安全性和隐私保护。传统的DNS查询是以明文形式传输的，极易受到劫持和监控的威胁。而DoH则通过加密的HTTPS通道传递DNS请求，从而有效防止了数据被第三方窃听或篡改。  
`https://doh.pub/dns-query`


# 投简历情况汇总
目前已投：6  
未沟通：5
意向：2.5？

## 绘景
保定 后端   5-10 k 
接口开发、数据库设计、性能调优、文档、java、python、sql、springboot
笔试-面试-培训-实习-转正  
java

## 中国人民财产保险秦皇岛分公司
本部信息技术岗  
系统开发、系统维护、项目推广、技术支持  
java、jsp、py、c#、php、Unix shell

## 增昀
研发工程师/实施工程师 不喜欢

## 保定云之家软件科技公司
erp实施 不咋着

## 北京华科诚信
好像在北京！    软件开发工程师     5-30w年  
java、sql

## 北京中科百谷
北京地区！       未投  
软件测试工程师 6-9k

## 微宝云信息技术开发河北有限公司
erp实施工程师   
电话沟通  像卖课的  需要去石家庄培训3个月  最终工作地点未知   不好









# 研究算法
```c++
class Solution { 
    public: 
    void wfs(vector<vector<int>>& heights, bool connect[200][200], int x, int y) { 
        int dx[4] = {-1, 1, 0, 0}; 
        int dy[4] = {0, 0, -1, 1}; 
        int hight = heights.size(), width = heights[0].size(); 
        for (int i = 0; i < 4; i++) { 
            int new_x = x + dx[i], new_y = y + dy[i]; 
            if (new_x >= 0 && new_x < width && new_y >= 0 && new_y < hight && heights[new_y][new_x] >= heights[y][x] && !connect[new_y][new_x]) { 
                connect[new_y][new_x] = true;
                wfs(heights, connect, new_x, new_y);
            } 
        } 
    } 
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) { 
        int dx[4] = {-1, 1, 0, 0}; 
        int dy[4] = {0, 0, -1, 1}; 
        int hight = heights.size(), width = heights[0].size(); 
        bool connect_pac[200][200] = {0}; 
        bool connect_atl[200][200] = {0}; stack<pair<int, int>> tovisit; 
        for (int i = 0; i < width; i++) { 
            if (!connect_pac[0][i]) { 
                connect_pac[0][i] = true; 
                wfs(heights, connect_pac, i, 0); 
            } 
            if (!connect_atl[hight-1][i]) { 
                connect_atl[hight-1][i] = true; 
                wfs(heights, connect_atl, i, hight-1); 
            } 
        }
        for (int i = 0; i < hight; i++) {
            if (!connect_pac[i][0]) { 
                connect_pac[i][0] = true; 
                wfs(heights, connect_pac, 0, i); 
            }
            if (!connect_atl[i][width-1]) { 
                connect_atl[i][width-1] = true; 
                wfs(heights, connect_atl, width-1, i);
            }
        } 
        vector<vector<int>> result; 
        for (int i = 0; i < hight; i++) { 
            for (int j = 0; j < width; j++) { 
                if (connect_atl[i][j] && connect_pac[i][j]) { 
                    vector<int> node = {i, j}; 
                    result.push_back(node);
                } 
            } 
        } 
        return result; 
    } 
};
```







\


初入公司，头衔是技术工程师，应该是参与前端和“中端”相关工作（后了解指系统中间层开发与维护），既新奇又充满挑战。全天紧凑安排：熟悉办公环境、学习协作流程、明确上下班时间。与HR沟通后签署协议，感受到职场规范的重要性。虽然对技术细节尚显陌生，但同事和同学耐心指导让我信心倍增。今日最大收获是打破了对“中端”的认知盲区，也深刻体会到职场中主动学习与沟通的关键性

熟悉办公环境、学习协作流程、明确上下班时间，与HR沟通后签署协议，感受到职场规范的重要性。虽然对技术细节尚显陌生，但是对于学习新知识我又很大热情

入职首日主要任务是搭建开发环境，从Java 1.8（即Java 8）、Maven到IntelliJ IDEA 2025社区版，逐一配置时深感工具链的复杂性，尤其是Maven的依赖管理让我反复排查路径问题。虽遇到Navicat注册的小波折，但通过团队分享的教程快速解决。过程中意识到：技术岗不仅需掌握代码，更要熟悉环境搭建与问题排查。今日收获不仅是工具熟练使用，更是对“独立解决问题”能力的初步锻炼，期待后续实操中进一步提升效率！


围绕 HTTP 协议和 JSON 数据展开深入学习。在 HTTP 协议方面，我清晰掌握了其由请求行、请求头等组成的结构，了解了不同方法的作用以及常见 Header 属性的功能，还明白了 Body 如何传输各类数据。对于 JSON 数据，我熟悉了它支持的多种数据类型以及规范的格式。这一系列学习让我对 Web 开发中的数据交互有了更系统、更深刻的认识，为后续参与实际项目开发打下了坚实基础，也让我对未来工作充满信心。


今日完成昨天的作业，属性http协议和json数据格式，外加复习了一下java，有点忘光光了。然后补发了一篇博客发在csdn上结果审核不通过，只能放在我自己的小网站上了。



今天上午参加培训，杜老师主要讲解了关于Java的springboot的不同接口的介绍，还有使用postman进行测试。然后留了一些作业，包括自己编写接口还有java基础的学习与使用。提高了我的java编程能力。

关于Java的springboot的安装，安装idea专业版，还是有点难找，还有使用postman进行接口测试，不太会。都通过查看相关教程进行解决

在本次Java后端开发实践中，我掌握了Spring Boot接口开发的核心流程，包括GET/POST请求理、参数传递、文件上传及MD5校验等关键技术。通过解决JDK版本兼容、依赖配置和流处理等实际问题，提升了调试与问题排查能力，对全栈开发流程有了更系统的认知，为后续项目实战打下坚实基础。


首先要解决的是jdk版本不匹配问题 作业code—1换成jdk1.8就可以编译了 遇到的问题： 无法检索应用程序 JMX 服务 URL Java 包装类 安装commons-codec 运行起来之后 地址：http://127.0.0.1:9001/api/v1/get-1 下载了一个postman进行接口测试 get传参 可用地址或参数 post有多种传参方式 params、请求体json、form-data 研究了一下apicontroller的方法，着手写接口练习 直接复制粘贴，改改名字就好，最后一个传文件的接口还有些难度。不过在ai的指导下还是完成了所有功能，包括扩展的保存和对比md5功能


今日不上班,继续学习有关java的知识,了解了maven的运作方式,学习到长期支持的java版本：8、11、17、21 JDK - java development kit 包含：代码编译器javac、运行环境jre、其他工具 编译器负责将java源文件编译为字节码文件(.class)给jre执行 jre中的jvm将字节码转换为不同设备上的机器码并执行 .java文件由类构成，类名应与文件同名，如下固定格式设置main方法class HelloWorld { public static void main(String[] args) { System.out,println("Hello,World!"); } }


今日主要学习,没有遇到什么问题,如果有的话,那就是java真的比python难很多,上手很困难.


实习第六天恰逢周日，本以为能稍作休息，但对知识的渴望让我主动投入到工作与学习中。运行 Java 项目，让我将理论与实践结合，对程序逻辑有了更直观理解。学习 Java 基础，加深了我对语言特性、语法规则的掌握，而了解 Maven 则为项目管理打开了新视角，明白了如何便捷地管理依赖、构建项目。


今天主要工作是运行 Java 项目，却在项目启动时遭遇依赖缺失报错。我先是仔细核对报错信息，锁定缺失的依赖项，随后查阅 Maven 官方文档，在项目的 pom.xml 文件中正确添加相应依赖坐标。经此过程，不仅解决了问题，还对 Maven 管理依赖机制有了更深认识，也让我在今后面对类似问题时，有了更清晰的解决思路 。


本周从职场认知到技术实操实现多维突破。从搭建 Java 开发环境、学习 HTTP 协议与 JSON 数据，到掌握 Spring Boot 接口开发，逐步构建起后端开发知识体系。通过解决 Maven 依赖、JDK 版本兼容等问题，深刻体会到主动学习与问题排查能力的重要性，也对团队协作和职场规范有了更直观认知。


完成开发环境搭建、Spring Boot 接口开发等任务，学习 Maven 依赖管理与 Java 基础。遇项目依赖缺失报错时，通过核对报错信息、查阅 Maven 文档添加坐标解决；JDK 版本不兼容问题，切换至 JDK 1.8 后编译成功。在 Postman 接口测试与文件上传接口编写中，借助教程和工具实践逐步掌握操作流程。


今日系统梳理 Java 基础语法，深入理解类与文件命名规范，掌握强制类型转换、变量声明（含基本类型与字符串操作）及条件循环结构。通过数组操作实践，对封装、继承、多态的面向对象特性有了初步认知。理论与代码示例结合的学习方式，让抽象概念变得具象，为后续开发实践奠定了扎实基础。


重点学习 Java 基础语法，包括类定义、变量类型、运算符及循环结构，实操数组复制与字符串拼接等功能。遇字符串索引计算逻辑不清晰问题，通过打印下标值与拆分字符串分步验证，理解了indexOf从零开始计数的机制；数组长度固定的特性则通过Arrays.copyOf方法实现动态扩展，加深了对数组操作的理解。

Day9 同昨日

Day10 2025-07-09 Wed
2025-07-10 17:36:26


2025-07-10 08:55:38


今日继续梳理 Java 基础语法，深入理解类与文件命名规范，掌握强制类型转换、变量声明（含基本类型与字符串操作）及条件循环结构。通过数组操作实践，对封装、继承、多态的面向对象特性有了初步认知。理论与代码示例结合的学习方式，让抽象概念变得具象，为后续开发实践奠定了扎实基础。



同昨日重点学习 Java 基础语法，包括类定义、变量类型、运算符及循环结构，实操数组复制与字符串拼接等功能。遇字符串索引计算逻辑不清晰问题，通过打印下标值与拆分字符串分步验证，理解了indexOf从零开始计数的机制；数组长度固定的特性则通过Arrays.copyOf方法实现动态扩展，加深了对数组操作的理解。

Day11 2025-07-10 Thu
2025-07-10 18:36:16


今天上午参加培训本次会议中，杜老师主要讲解了Spring Boot框架中不同类型接口的设计与实现方法，并演示了如何使用Postman工具对这些接口进行功能测试。此外，讲师还介绍了如何通过Java程序实现数据库的增删改查（CRUD）基础操作，并布置了相关练习任务，包括自主编写业务接口和巩固Java基础知识。这些实践内容有效提升了我的Java编程能力。


学习Spring Boot接口设计与实现、用Postman测试，了解Java实现数据库CRUD操作并完成接口编写与Java知识巩固任务。

Day12 2025-07-11 Fri
2025-07-11 21:40:22


学习并实现Spring Boot框架中不同类型接口的设计与实现方法，学习如何使用Postman工具对这些接口进行功能测试。此外，还学习了如何通过Java程序实现数据库的增删改查（CRUD）基础操作，研究并完成练习任务，包括自主编写业务接口和巩固Java基础知识。这些实践内容有效提升了我的Java编程能力。


学习Spring Boot接口设计与实现、用Postman测试，了解Java实现数据库CRUD操作并完成接口编写与Java知识巩固任务。

Day13 2025-07-12 Sat
2025-07-13 01:05:03


今日不上班,继续学习有关java的基础，具体的：实例对象 抽象的：类 面向对象的三步操作： 封装 继承 多态 int [] aa = {1, 2, 3};//完整int [] aa = new int[3] {1, 2, 3}; int [] bb = new int[3];//元素个数声明后无法更改 System.out.println(Arrays.toString(aa));//注意输出需转换 System.out.println(aa[0]);//通过索引访问 int [] cc = Arrays.copyOf(aa, 5);//复制数组，改变长度



今日不上班,继续学习有关java的基础，具体的：关于java类的继承：class Animal { //class+类名创建类 private String name = "66";//默认值,private时，外部获取会报错 int age = 5; public Animal (String name, int age) { //与类同名的构造方法，进行值的接收 this.name = name; this.age = age;//this代表实例 } void print () { System.out.println(name + age); } public String getName () {//getter函数，方便外部获取值 return this.name; } public void setName (String newValue1) { //setter函数 this.name = newValue1; } public void eat () {//更多功能 System.out.println("您的"+this.name+"正在吃屎！"); } } class Cat extends Animal public Cat(String name, int age) { super(name, age);//super 关键字：显式调用父类 Animal 的构造方法，将参数传递给父类初始化。 }


学习中未遇到什么问题，无非就是编译报错，少写个分号之类的

# 第2周 2025-07-07 至 2025-07-13

本周在 Java 基础与 Spring Boot 实践中稳步进阶。巩固了类、继承等面向对象知识，通过代码实例深化对封装、多态的理解；参与 Spring Boot 接口设计培训，掌握 Postman 测试及数据库 CRUD 操作，理论与实操结合让技术认知更系统，为后续开发积累了实用经验。

主要工作、遇到的问题及解决的
重点学习 Java 类继承、数组操作，参与 Spring Boot 接口设计与数据库操作练习。遇编译报错多因语法疏漏，如少写分号，通过逐行核对代码解决；对类继承中 super 关键字用法，结合父类构造方法实例调试理解其作用。



在 Java 基础与 Spring Boot 实践中稳步进阶。巩固了类、继承等面向对象知识，通过代码实例深化对封装、多态的理解；参与 Spring Boot 接口设计培训，掌握 Postman 测试及数据库 CRUD 操作，理论与实操结合让技术认知更系统，为后续开发积累了实用经验。


培训2-使用 Spring Boot 连接数据库JPA 指 Java Persistence API，是Java EE 平台规范中用于管理Java 对象和关系数据库之间持久化数据的标准API。简单来说，JPA 提供了一种将Java 对象映射到数据库表的方式，使得开发者可以用操作对象的方式来操作数据库，而无需直接编写SQL语句。 - jpa-spec 动态拼接属性 用于构造查询条件 [jpa-spec](https://github.com/wenhao/jpa-spec) - Spring Web 提供web接口 - lombok 自动生成get set方法 构造方法 - MySQL Driver.直接在AccountRepository写接口，甚至不用实现


遇到的问题： 1. jdk版本问题 2. MySQL连接问题 3. 指定数据库方言



今天培训，主要是讲用MyBatis在Spring Boot里操作数据库。上次用GPA的方法，这次换个方式。建项目时选好依赖，配置文件中需指定mapper的XML文件位置。通过接口（加@Mapper注解）声明方法，对应XML文件写SQL语句，二者需一一对，对应XML写SQL，还能装插件跳转，举了查数据的例子。




今日主要搭建了班级和学生表结构，初步构建了增删改查功能框架。配置 mapper 位置到接口与 XML 映射的逻辑。理解了 “接口 + XML” 的协作模式。实践中搭建班级和学生表的操作框架，让理论知识有了实践。虽未完成全部功能，但对增删改查的实现逻辑更清晰，也意识到插件辅助能提升效率。


今日主要搭建了班级和学生表结构，初步构建了增删改查功能框架。遇到 XML 与接口方法映射失败问题，检查后发现是命名不匹配，修正名称保持一致后解决。同时分页功能暂未实现，计划明天参考示例完善。​


今日不上班，继续学习java，深入了解了maven的运作方式，并且学习了一个github上的一个用vite+vue的项目，尝试改一下图片发现vite竟然这么方便，修改后效果瞬间出现。界面很美观，结构简单，确实很简单。



周日在GitHub上找了些开源项目进行学习，包括gedoor、MusicFree还有昨天的BOCCHI-THE-ROCK，我之前写过vue两个小网站（是很丑陋的那种）所以看到别人的项目，收获很多，也学习GitHubDesktop的使用


学习GitHubDesktop的使用，比git命令方便多了。


在GitHub上找了些开源项目进行学习，使用GitHubDesktop。还有默认情况下，所有的 HTML 元素有一个静态的位置，且是不可移动的。 如果需要改变，需要将元素的 position 属性设置为 relative, fixed, 或 absolute。今日收获很多，学到很多，理论与实操结合让技术认知更系统，为后续开发积累了实用经验。


学习中还是多有不会的地方，多多练习，并且查一些官方文档比较很有帮助。理论与实操结合让技术认知更系统，为后续开发积累了实用经验。

今天培训，主要是讲用html基础，包括css样式和js，但主要是css，这一部分的学习我感觉压力很小，因为我已经自己写过多个网站了，所以理解无压力。然后还有关于tomcat和bootstrap等基础。然后还有一个小作业，写个基础网站页面的css，主要是排版

网站的排版比较费劲，有时候会碰到css污染等问题，需要特别注意。
学习中还是多有不会的地方，多多练习，并且查一些官方文档比较很有帮助。理论与实操结合让技术认知更系统，为后续开发积累了实用经验。
















































