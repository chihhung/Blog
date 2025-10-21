# 我的個人部落格

這是一個使用 [Hugo](https://gohugo.io/) 靜態網站生成器建立的個人部落格，使用 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主題，並自動部署到 GitHub Pages。

## 🚀 網站連結

- **部落格網址**: [https://chihhung.github.io/Blog/](https://chihhung.github.io/Blog/)
- **GitHub 倉庫**: [https://github.com/chihhung/Blog](https://github.com/chihhung/Blog)

## 🛠️ 技術棧

- **靜態網站生成器**: Hugo v0.151.0 Extended
- **主題**: PaperMod
- **部署**: GitHub Pages
- **CI/CD**: GitHub Actions

## 📝 本地開發

### 1. 安裝 Hugo

使用 Chocolatey (Windows):

```powershell
choco install hugo-extended -y
```

### 2. 克隆專案

```bash
git clone https://github.com/chihhung/Blog.git
cd Blog
git submodule update --init --recursive
```

### 3. 本地預覽

```bash
hugo server --buildDrafts
```

然後在瀏覽器中訪問 `http://localhost:1313`

### 4. 建立新文章

```bash
hugo new content posts/新文章名稱.md
```

### 5. 建置靜態網站

```bash
hugo --minify
```

## 📁 專案結構

```text
Blog/
├── .github/
│   └── workflows/
│       └── hugo.yml         # GitHub Actions 工作流程
├── archetypes/              # 內容模板
├── content/                 # Markdown 內容檔案
│   ├── posts/              # 部落格文章
│   └── about.md            # 關於頁面
├── data/                   # 資料檔案
├── layouts/                # 版面模板
├── static/                 # 靜態檔案 (圖片、CSS、JS)
├── themes/
│   └── PaperMod/          # 主題檔案 (git submodule)
├── hugo.toml              # Hugo 配置檔案
└── README.md              # 專案說明
```

## 🎨 自訂主題

主題配置位於 `hugo.toml` 文件中，你可以根據需要修改：

- 網站標題和描述
- 選單項目
- 社群連結
- 色彩主題
- 其他 PaperMod 主題選項

## 📝 部署說明

這個部落格使用 GitHub Actions 自動部署到 GitHub Pages：

1. 推送代碼到 `main` 分支
2. GitHub Actions 自動觸發建置流程
3. Hugo 生成靜態檔案
4. 自動部署到 GitHub Pages

## 📄 授權

本專案使用 MIT 授權。

## 🙏 感謝

- [Hugo](https://gohugo.io/) - 快速、現代的靜態網站生成器
- [PaperMod](https://github.com/adityatelange/hugo-PaperMod) - 優雅的 Hugo 主題
- [GitHub Pages](https://pages.github.com/) - 免費靜態網站託管服務