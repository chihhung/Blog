# 我的個人部落格

這是一個使用 [Hugo](https://gohugo.io/) 靜態網站生成器建立的個人部落格，使用 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主題，並自動部署到 GitHub Pages。

## 🚀 網站連結

- **部落格網址**: [https://chihhung.github.io/Blog/](https://chihhung.github.io/Blog/)
- **GitHub 倉庫**: [https://github.com/chihhung/Blog](https://github.com/chihhung/Blog)

> ⚠️ **重要提醒**: 本網站使用 Hugo + GitHub Actions 部署，請確保 GitHub Pages 設定中的 Source 為 "GitHub Actions"

## 🛠️ 技術棧

- **靜態網站生成器**: Hugo v0.151.0 Extended
- **主題**: PaperMod
- **部署**: GitHub Pages
- **CI/CD**: GitHub Actions
- **內容管理**: Markdown
- **語言**: 繁體中文 (zh-TW)

## 📚 內容分類

部落格內容依照不同主題分類，方便閱讀與管理：

### 教學文章 (`posts/教學/`)

- **程式語言**: Bash, C#, Java, JavaScript, TypeScript, Python, SQL, PowerShell, HTML5/CSS3
- **Framework**: Angular, React, Vue3, Spring Boot, Spring Framework, Thymeleaf, PrimeNG, PrimeVue
- **開發工具**: Git, GitHub, GitLab, Jenkins, Maven, IntelliJ IDEA, VS Code, Vim, Podman, JMeter
- **分析與設計**: OOAD, UML, DFD, Design Pattern, Clean Code, Clean Architecture, DDD, Refactoring, Spec-Kit

### 專案指引 (`posts/指引/`)

- **專案管理**: 專案啟動、品質管理、風險管理、溝通管理、敏捷開發、金融合規
- **設計開發**: 架構設計、系統設計、前後端開發、資料庫設計、程式寫作、Code Review、重構、測試、壓測、安全、UI/UX
- **需求分析**: 系統分析、客戶需求訪談

### 開發範本 (`posts/prompts/`)

- **需求分析**: 業務需求收集、功能需求分析、使用者故事撰寫、安全需求識別、UI/UX 設計指引
- **設計開發**: API 設計、系統架構設計、軟體架構設計、資料庫設計、設計指引
- **測試驗收**: 測試策略制定、自動化測試
- **部署運維**: CI/CD 流程

### 專案範本 (`posts/範本/`)

- 系統分析階段標準範本清單
- 系統設計階段標準範本清單
- 架構轉換專案計畫範本
- 文件目錄範例

## 📊 專案統計

- **總文章數**: 96+ 篇
- **主分類**: 4 個（教學、指引、範本、prompts）
- **子分類**: 11 個
- **總頁面數**: 346 頁
- **建置狀態**: ✅ 成功

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
│       └── hugo.yml              # GitHub Actions 工作流程
├── archetypes/                   # 內容模板
│   └── default.md
├── content/                      # Markdown 內容檔案
│   ├── doc/                      # 文檔目錄（未發布）
│   │   ├── prompts/             # 開發範本文檔
│   │   ├── 指引/                # 專案指引文檔
│   │   ├── 教學/                # 教學文章文檔
│   │   └── 範本/                # 專案範本文檔
│   ├── posts/                    # 已發布的部落格文章
│   │   ├── prompts/             # 開發範本（需求分析、設計開發、測試驗收、部署運維）
│   │   ├── 指引/                # 專案指引（專案管理、設計開發、需求分析）
│   │   ├── 教學/                # 教學文章（程式語言、Framework、工具、分析與設計）
│   │   └── 範本/                # 專案範本
│   └── about.md                  # 關於頁面
├── data/                         # 資料檔案
├── i18n/                         # 國際化檔案
├── layouts/                      # 自訂版面模板
│   ├── _default/
│   │   └── _markup/
│   ├── partials/
│   │   └── extend_head.html     # 自訂 head 擴展
│   ├── posts/
│   │   └── list.html            # 文章列表頁面（支援遞迴顯示子目錄）
│   └── shortcodes/
│       └── mermaid.html         # Mermaid 圖表支援
├── public/                       # 生成的靜態網站（由 Hugo 建置）
├── resources/                    # Hugo 資源快取
├── static/                       # 靜態檔案（圖片、CSS、JS）
├── themes/
│   └── PaperMod/                # 主題檔案 (git submodule)
├── hugo.toml                     # Hugo 配置檔案
└── README.md                     # 專案說明
```

## 🎨 自訂主題

主題配置位於 `hugo.toml` 文件中，你可以根據需要修改：

- 網站標題和描述
- 選單項目
- 社群連結
- 色彩主題
- 主要內容區段（mainSections = ["posts"]）
- 分類和標籤（taxonomies）
- 其他 PaperMod 主題選項

### 自訂功能

- **遞迴文章列表**: 自訂 `layouts/posts/list.html`，支援顯示所有子目錄的文章
- **Mermaid 圖表**: 透過 shortcode 支援 Mermaid 圖表渲染
- **多層級分類**: 支援 4 個主分類和 11 個子分類的內容組織

## 📝 部署說明

這個部落格使用 GitHub Actions 自動部署到 GitHub Pages：

1. 推送代碼到 `main` 分支
2. GitHub Actions 自動觸發建置流程
3. Hugo 生成靜態檔案
4. 自動部署到 GitHub Pages

### 建置配置

- **Hugo 版本**: v0.151.0 Extended
- **建置命令**: `hugo --minify`
- **建置時間**: ~2-3 秒
- **輸出目錄**: `public/`

## 🔧 內容管理

### 文章組織結構

所有文章使用 Markdown 格式撰寫，並依照主題分類：

- 使用 TOML frontmatter 定義文章元數據（標題、日期、標籤、分類等）
- 每個子目錄都有 `_index.md` 作為導航頁面
- 支援草稿模式（`draft = true`）

### 新增文章

1. 在對應的子目錄下建立新的 `.md` 檔案
2. 添加 Hugo frontmatter（或使用 `hugo new` 指令）
3. 撰寫文章內容
4. 設定 `draft = false` 以發布文章

### 格式規範

專案已進行完整的 Markdown 格式優化：

- ✅ 修正 34,246 處格式問題
- ✅ 標準化列表縮排（MD007）
- ✅ 優化標題格式（MD022、MD036）
- ✅ 添加程式碼區塊語言標記（MD040）
- ✅ 標準化檔案結尾換行（MD047）
- ✅ 修正連結格式（MD051 部分修正）

## � 問題排查

### 常見問題

**Q: 本地預覽時看不到子目錄的文章？**

A: 確認 `hugo.toml` 中有設定 `mainSections = ["posts"]`，並且使用了自訂的 `layouts/posts/list.html`。

**Q: GitHub Pages 部署後 CSS 樣式錯誤？**

A: 確認 `hugo.toml` 中的 `baseURL` 設定正確，應為 `https://chihhung.github.io/Blog/`。

**Q: 文章分類或標籤不顯示？**

A: 檢查文章 frontmatter 中的 `categories` 和 `tags` 是否正確設定。

**Q: Markdown Linter 顯示 MD051 錯誤？**

A: 這是錨點驗證警告，不影響網站功能。主要因為中文標題和特殊符號導致。

## �📄 授權

本專案使用 MIT 授權。

## 🙏 感謝

- [Hugo](https://gohugo.io/) - 快速、現代的靜態網站生成器
- [PaperMod](https://github.com/adityatelange/hugo-PaperMod) - 優雅的 Hugo 主題
- [GitHub Pages](https://pages.github.com/) - 免費靜態網站託管服務
- [GitHub Copilot](https://github.com/features/copilot) - AI 程式設計助手

## 📧 聯絡方式

如有問題或建議，歡迎透過以下方式聯絡：

- 建立 [GitHub Issue](https://github.com/chihhung/Blog/issues)
- Pull Request 歡迎

---

最後更新日期: 2025-10-31
