+++
date = '2025-10-14T19:55:00+08:00'
draft = false
title = '使用 Hugo 建立 GitHub 個人部落格完整指南'
tags = ['Hugo', 'GitHub Pages', '教學', '部落格']
categories = ['技術']
summary = '詳細說明如何使用 Hugo 和 GitHub Pages 建立個人部落格的完整流程'
+++

在這篇文章中，我將分享如何使用 Hugo 靜態網站生成器建立個人部落格，並部署到 GitHub Pages 的完整流程。

## 為什麼選擇 Hugo？

Hugo 是一個用 Go 語言編寫的靜態網站生成器，具有以下優點：

- ⚡ **極快的建置速度**：比其他靜態網站生成器快數倍
- 🎨 **豐富的主題**：有大量免費且美觀的主題可選擇
- 📝 **Markdown 支援**：使用 Markdown 編寫內容，簡單易學
- 🔧 **配置靈活**：支援多種配置格式和自訂選項
- 🚀 **易於部署**：與 GitHub Pages 完美整合

## 安裝步驟

### 1. 安裝 Hugo

Windows 使用者可以透過 Chocolatey 安裝：

```powershell
choco install hugo-extended -y
```

macOS 使用者可以透過 Homebrew 安裝：

```bash
brew install hugo
```

### 2. 建立新網站

```bash
hugo new site my-blog
cd my-blog
```

### 3. 添加主題

我推薦使用 PaperMod 主題，它簡潔美觀且功能完整：

```bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

### 4. 配置網站

編輯 `hugo.toml` 檔案，設定基本資訊和主題。

### 5. 建立內容

```bash
hugo new content posts/my-first-post.md
```

## GitHub Pages 部署

### 1. 建立 GitHub Actions 工作流程

在 `.github/workflows/` 目錄下建立 `hugo.yml` 檔案，設定自動部署流程。

### 2. 設定 GitHub Pages

在 GitHub 倉庫設定中：
1. 進入 Settings > Pages
2. Source 選擇 "GitHub Actions"
3. 推送代碼後會自動部署

## 本地開發

啟動開發伺服器：

```bash
hugo server --buildDrafts
```

然後在瀏覽器訪問 `http://localhost:1313`

## 小結

使用 Hugo 建立部落格的好處是：
- 載入速度快
- 安全性高（沒有資料庫）
- 免費託管（GitHub Pages）
- 版本控制（Git）
- 可離線編寫

下次我會分享如何自訂主題和添加更多功能！
