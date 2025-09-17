# 习惯评分记录器（Streamlit + Google Sheet）

这是一个用 Streamlit 构建的个人习惯评分工具，数据实时写入 Google Sheets，实现跨设备云端记录。

## ✅ 功能
- 每天记录多个习惯的达成评分（0-10）
- 数据实时保存至 Google Sheet
- 显示评分历史表格

## 🚀 快速开始

1. 克隆项目并安装依赖：

```bash
pip install -r requirements.txt
```

2. 设置 Google Sheet：
- 在 [Google Cloud Console](https://console.cloud.google.com/) 中创建项目
- 启用 Google Sheets API
- 创建服务账号并下载 `credentials.json`
- 创建一个 Sheet 名为 `Habits`
- 邀请服务账号的 email 为协作者（编辑权限）

3. 启动项目：

```bash
streamlit run app.py
```

## 📁 文件结构

```
.
├── app.py               # 主程序
├── requirements.txt     # 依赖文件
├── credentials.json     # 你下载的 Google API 凭证（不要上传 GitHub）
└── README.md
```

## ✍️ 作者
由 ChatGPT 根据用户需求定制
