---
layout:     post
title:      "在GitHub Pages部署Vue CLI创建的静态网站并实现自动部署"
subtitle:   "基于vue的小网站-保定介绍，主要介绍github pages的使用方法"
date:       2025-09-18 12:00:00
author:     "hangyangjun"
header-img: "img/vue-baoding.png"
tags:
    - 笔记
    - 记录
    - github
    - vue
---

>由超能豆包beta提供指导  
网站地址：[Baoding-introduction-Vue-homework](https://haoyangjunjun.github.io/Baoding-introduction-Vue-homework)  
源码地址：[Baoding-introduction-Vue-homework](https://github.com/haoyangjunjun/Baoding-introduction-Vue-homework)  

## 1. 准备工作

首先确保你的开发环境中已经安装了Node.js：
```bash
# 检查Node.js版本
node -v
# 检查npm版本
npm -v
```

如果没有安装，请先下载并安装Node.js（推荐LTS版本）。

## 2. 项目配置

### 2.1 配置vue.config.js
在Vue CLI创建的项目根目录下找到或创建`vue.config.js`文件：

```javascript
module.exports = {
  // 关键配置：解决GitHub Pages路径问题
  publicPath: './',
  // 打包输出目录（默认就是dist，可省略）
  outputDir: 'dist',
  // 可选：关闭语法检查，避免不必要的报错
  lintOnSave: false
}
```

### 2.2 本地测试运行
确保项目能在本地正常运行：
```bash
# 安装依赖
npm install

# 本地运行测试
npm run serve
```

访问终端显示的本地地址（通常是http://localhost:8080）确认网站正常运行。

## 3. 创建GitHub仓库并推送代码

### 3.1 在GitHub上创建仓库
1. 登录GitHub账号
2. 点击右上角"+"图标，选择"New repository"
3. 填写仓库名称（如my-vue-website）
4. 选择"Public"或"Private"
5. 点击"Create repository"

### 3.2 推送本地代码到GitHub
可以使用命令行：
```bash
# 初始化Git仓库（如果还没有初始化）
git init

# 添加远程仓库
git remote add origin https://github.com/<username>/<REPO_NAME>.git

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit"

# 推送代码到GitHub
git push -u origin main
```

或者使用GitHub Desktop（更简单的图形界面方式）：
1. 打开GitHub Desktop
2. 点击"File" → "Add Local Repository"
3. 选择你的Vue项目文件夹
4. 点击"Publish repository"
5. 确认仓库名称和设置，点击"Publish"

## 4. 配置GitHub Actions自动部署

### 4.1 生成Personal Access Token
1. 登录GitHub，点击右上角头像 → "Settings"
2. 在左侧栏找到"Developer settings" → "Personal access tokens"
3. 点击"Generate new token"
4. 填写Note（如"GitHub Pages Deploy"）
5. 勾选"workflow"权限
6. 点击"Generate token"
7. 复制生成的token（**重要：离开页面后将无法再次查看**）

### 4.2 添加密钥到仓库
1. 进入你的GitHub仓库 → "Settings"
2. 在左侧栏找到"Security" → "Actions"
3. 在"Secrets and variables"下，点击"Repository secrets"
4. 点击"New repository secret"
5. Name: `GH_PAGES_TOKEN`
6. Value: 粘贴刚才生成的Personal Access Token
7. 点击"Add secret"

### 4.3 创建GitHub Actions工作流文件
1. 在项目根目录下创建`.github/workflows`文件夹
2. 在该文件夹下创建`deploy.yml`文件（文件名可以自定义）
3. 添加以下内容：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main  # 当main分支有推送时触发

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'  # 使用最新LTS版本
          
      - name: Install dependencies
        run: npm install
        
      - name: Build project
        run: npm run build
        
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GH_PAGES_TOKEN }}
          publish_dir: ./dist  # Vue CLI打包输出目录
```

4. 提交并推送这个文件到GitHub：
```bash
git add .
git commit -m "Add GitHub Actions workflow"
git push
```

## 5. 配置GitHub Pages

1. 进入你的GitHub仓库 → "Settings"
2. 在左侧栏找到"Pages"
3. 在"Source"部分，从下拉菜单中选择：
   - Branch: `gh-pages`
   - Folder: `/ (root)`
4. 点击"Save"
5. 等待几分钟，GitHub Pages会部署你的网站

## 6. 访问你的网站

部署完成后，你可以通过以下地址访问你的Vue网站：
```
https://<username>.github.io/<REPO_NAME>/
```

例如：`https://john-doe.github.io/my-vue-website/`

## 7. 自动部署验证

每次你向`main`分支推送代码时，GitHub Actions都会自动运行工作流：
1. 拉取最新代码
2. 安装依赖
3. 构建项目
4. 部署到GitHub Pages

你可以在仓库的"Actions"标签页中查看工作流的运行状态。

## 常见问题解决

1. **页面空白或资源加载失败**：
   - 确保`vue.config.js`中设置了`publicPath: './'`
   - 检查浏览器控制台的错误信息

2. **GitHub Actions工作流失败**：
   - 检查工作流日志，查看具体错误信息
   - 确保Node.js版本兼容
   - 检查依赖安装是否成功

3. **GitHub Pages显示404**：
   - 等待几分钟，部署可能需要时间
   - 检查`gh-pages`分支是否存在
   - 确认GitHub Pages设置正确

4. **路由问题**：
   - 如果使用Vue Router，确保使用`hash`模式或配置正确的`base`路径

这样，你就完成了Vue CLI创建的静态网站在GitHub Pages上的部署，并实现了代码推送后的自动部署功能。


# 地址问题和图片加载问题


你的图片地址错误是因为 **资源路径没有包含仓库名称**，导致GitHub Pages无法正确找到图片。解决方法如下：


### 问题原因
GitHub Pages的访问路径结构是：  
`https://<用户名>.github.io/<仓库名称>/<资源路径>`  

你的图片地址目前是 `https://haoyangjunjun.github.io/img/top3.bf509d34.jpg`，缺少了仓库名称（比如你的仓库名是 `Baoding-introduction-Vue-homework`），正确路径应该是：  
`https://haoyangjunjun.github.io/Baoding-introduction-Vue-homework/img/top3.bf509d34.jpg`  


### 解决步骤（确保所有资源路径自动包含仓库名）

#### 1. 调整项目配置文件（关键）
根据你的项目类型（Vue CLI 或 Vite），修改配置文件，让打包后的资源路径自动带上仓库名称：

##### 若使用 Vue CLI（`vue.config.js`）：
```javascript
module.exports = {
  // 生产环境路径：自动添加仓库名（替换为你的仓库名）
  publicPath: process.env.NODE_ENV === 'production' 
    ? '/Baoding-introduction-Vue-homework/'  // 仓库名必须正确，前后斜杠不能少
    : '/',  // 开发环境保持根路径
  outputDir: 'dist'
}
```

##### 若使用 Vite（`vite.config.js`）：
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  // 生产环境路径：自动添加仓库名
  base: process.env.NODE_ENV === 'production' 
    ? '/Baoding-introduction-Vue-homework/'  // 替换为你的仓库名
    : '/',
  build: {
    outDir: 'dist'
  }
})
```


#### 2. 在代码中正确引用图片
确保你在Vue组件中引用图片时，使用 **相对路径** 或 **Vue的资源引用方式**，避免硬编码绝对路径：

##### 正确示例：
```vue
<!-- 方法1：相对路径（推荐） -->
<img src="./img/top3.bf509d34.jpg" alt="示例图片">

<!-- 方法2：使用require（适用于Vue CLI） -->
<img :src="require('@/assets/img/top3.bf509d34.jpg')" alt="示例图片">

<!-- 方法3：使用import（适用于Vite） -->
<script setup>
import top3Img from '@/assets/img/top3.bf509d34.jpg'
</script>
<template>
  <img :src="top3Img" alt="示例图片">
</template>
```

##### 错误示例（避免）：
```vue
<!-- 不要写死绝对路径！ -->
<img src="https://haoyangjunjun.github.io/img/top3.bf509d34.jpg" alt="错误路径">
```


#### 3. 重新构建并部署
修改配置后，重新打包并推送代码，GitHub Actions会自动部署更新后的版本：
```bash
# 本地打包（确认dist文件夹中的资源路径是否已包含仓库名）
npm run build

# 推送代码触发自动部署
git add .
git commit -m "修复资源路径"
git push
```


### 验证
部署完成后，检查图片路径是否自动变为：  
`https://haoyangjunjun.github.io/Baoding-introduction-Vue-homework/img/top3.bf509d34.jpg`  

如果仍有问题，可通过浏览器控制台（F12）查看「网络」面板，确认图片请求的具体路径，进一步排查是否配置正确。








这个问题是由于 Vue Router 的路由模式和基础路径配置不正确导致的，特别是在 GitHub Pages 这种非根域名部署场景下。具体原因和解决方法如下：


### 问题根源
1. **路由基础路径（base）未配置**  
   你的网站部署在 `https://haoyangjunjun.github.io/Baoding-introduction-Vue-homework/`（二级路径），但 Vue Router 默认使用根路径（`/`），导致点击链接时会跳转到 `https://haoyangjunjun.github.io/xxx`（忽略仓库名）。

2. **路由模式可能使用了 history 模式**  
   history 模式需要服务器配置支持，而 GitHub Pages 无法直接兼容，可能导致刷新时跳转异常。


### 解决步骤

#### 1. 配置 Vue Router 的基础路径（关键）
找到你的路由配置文件（通常是 `src/router/index.js` 或 `src/router/index.ts`），添加 `base` 配置，值为你的仓库名称：

```javascript
import { createRouter, createWebHashHistory } from 'vue-router'
// 注意：推荐使用 createWebHashHistory（hash模式），避免history模式的服务器问题

const router = createRouter({
  // 关键配置：设置基础路径为仓库名称
  history: createWebHashHistory('/Baoding-introduction-Vue-homework/'),
  // 如果坚持用history模式（不推荐），需写成：
  // history: createWebHistory('/Baoding-introduction-Vue-homework/'),
  
  routes: [
    // 你的路由配置
    {
      path: '/',
      name: 'Home',
      component: () => import('@/views/Home.vue')
    },
    {
      path: '/introduction',  // 路由路径保持不变
      name: 'Introduction',
      component: () => import('@/views/Introduction.vue')
    }
  ]
})

export default router
```

- `base` 的值必须与仓库名称完全一致，且前后都有斜杠（`/仓库名/`）。
- 推荐使用 `createWebHashHistory`（hash模式，URL 带 `#`），避免 history 模式在 GitHub Pages 上的刷新 404 问题。


#### 2. 检查链接跳转方式
确保在组件中使用 `router-link` 跳转，而不是原生 `<a>` 标签，避免硬编码路径：

```vue
<!-- 正确：使用 router-link -->
<router-link to="/">首页</router-link>
<router-link to="/introduction">介绍页</router-link>

<!-- 错误：不要用原生a标签 -->
<a href="/">首页</a>  <!-- 会跳转到根域名，导致错误 -->
```


#### 3. 同步调整项目打包路径（与之前配置保持一致）
确保 `vue.config.js`（Vue CLI）或 `vite.config.js`（Vite）的 `publicPath`/`base` 与路由的 `base` 一致：

##### Vue CLI（vue.config.js）：
```javascript
module.exports = {
  publicPath: '/Baoding-introduction-Vue-homework/',  // 和路由base保持一致
  outputDir: 'dist'
}
```

##### Vite（vite.config.js）：
```javascript
export default defineConfig({
  base: '/Baoding-introduction-Vue-homework/',  // 和路由base保持一致
  // ...其他配置
})
```


#### 4. 重新部署
修改后重新打包并推送代码，触发 GitHub Actions 自动部署：

```bash
# 本地测试（可选）
npm run serve  # 确认本地跳转正常

# 打包
npm run build

# 推送代码
git add .
git commit -m "修复路由路径问题"
git push
```


### 效果验证
部署完成后：
- 首页地址应为：`https://haoyangjunjun.github.io/Baoding-introduction-Vue-homework/#/`（hash模式带 `#`）
- 介绍页地址应为：`https://haoyangjunjun.github.io/Baoding-introduction-Vue-homework/#/introduction`
- 点击链接时，URL 会包含仓库名称，不会跳转到根域名或其他网站。


如果仍有问题，检查路由配置中是否有硬编码的绝对路径（如 `window.location.href = '/'`），替换为 `this.$router.push('/')`（Vue2）或 `useRouter().push('/')`（Vue3）即可。