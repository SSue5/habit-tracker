# 习惯评分记录器（Electron + SQLite）

这是一个用 Electron 构建的个人习惯评分工具，数据存储在本地 SQLite 数据库中，支持跨平台运行。

## ✅ 功能

- 每天记录多个习惯的达成评分（0-10）
- 数据存储在本地 SQLite 数据库
- 显示评分历史表格

## 🚀 快速开始

1. 克隆项目并安装依赖：

```bash
git clone <your-repo-url>
cd habit-tracker-electron
npm install
```

2. 启动项目：

   ```
   npm start
   ```

## 📁 文件结构

```
.
├── main.js              # 主进程文件
├── preload.js           # 预加载脚本
├── renderer.js          # 渲染进程脚本
├── index.html           # 前端页面
├── package.json         # 项目配置文件
├── habit_tracker.db     # SQLite 数据库文件（运行时生成）
└── [README.md](http://_vscodecontentref_/1)            # 项目说明
```

## ✍️ 作者


## 版本

v1: 

默认五个习惯

输入分数

提交

问题：

增减习惯

习惯单独弹窗

评分存储
