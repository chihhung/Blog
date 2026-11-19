# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案概觀

Hugo（v0.151.0 Extended）+ PaperMod 主題（`themes/PaperMod`，git submodule）的個人技術部落格，語言為繁體中文（zh-TW），部署到 GitHub Pages（`https://chihhung.github.io/Blog/`）。幾乎所有工作都是撰寫／改版 `content/` 底下的長篇 Markdown 教學手冊與指引，而非程式碼。

## 常用指令

```powershell
git submodule update --init --recursive     # 首次 clone 後取得 PaperMod 主題
hugo server --buildDrafts                   # 本地預覽 http://localhost:1313/Blog/
hugo --minify                               # 正式建置到 public/（CI 也用這個）
hugo -d "$env:TEMP/hugo-check"              # 建到暫存目錄，供連結驗證，不污染 public/

# 單一文章檢查（皆以檔案路徑為參數）
pwsh ./check-md.ps1  -Path "content/posts/.../xxx.md"   # markdownlint 子集：MD009/010/022/023/040/058…
pwsh ./check-toc.ps1 -Path "content/posts/.../xxx.md"   # 檢查目錄錨點是否對應到標題
python tools/markdown/generate_toc.py "content/posts/.../xxx.md"            # 預覽 TOC
python tools/markdown/generate_toc.py "content/posts/.../xxx.md" --write    # 改寫 TOC-AUTO 區塊
python tools/markdown/generate_toc.py "content/posts/.../xxx.md" --verify-html "$env:TEMP/hugo-check/posts/.../index.html"
```

沒有測試套件；「驗證」= Hugo 建置成功 + 上述 lint／錨點檢查。Markdown lint 規則見 `.markdownlint.json`（MD013/033/036/041/032 已關閉，MD024 僅限同層）。

## 內容架構

- `content/posts/` — 已發布文章，依 `教學/`（AI開發、framework、工具、程式語言、分析與設計、templates…）、`指引/`、`prompts/`、`範本/` 分類，各子目錄有 `_index.md`。
- `content/doc/` — 未發布的原始文檔副本，**改文章時改 `content/posts/` 下的版本**，除非使用者明確指定 doc。
- Front matter 一律使用 TOML（`+++`），欄位：`date`、`draft`、`title`、`tags`、`categories`。`tags` 慣例為目錄路徑名稱（例如 `['教學', 'framework']`），可用 `update-tags-by-path.ps1` 依路徑批次重設（該腳本寫死 `d:\developer\repos\Blog\content\posts`）。
- 檔名多為中文且含空白；在 bash 中用 `git -c core.quotepath=off` 才能看到可讀路徑，並記得加引號。

## 版面客製（`layouts/`）

- `layouts/posts/list.html` — 遞迴列出所有子目錄文章（搭配 `hugo.toml` 的 `mainSections = ["posts"]`）。
- Mermaid：` ```mermaid ` 程式碼區塊由 `layouts/_default/_markup/render-codeblock-mermaid.html` 轉成 `<pre class="mermaid">`，`layouts/partials/extend_head.html` 從 jsDelivr 載入 mermaid@11 並依深淺色主題初始化；另有 `{{< mermaid >}}` shortcode。`fix-mermaid-*.ps1`、`test-mermaid*.{ps1,html}` 是排查 Mermaid 語法的一次性工具。
- `layouts/index.json` + `outputs.home = ["HTML","RSS","JSON"]` 提供站內搜尋索引（`content/search.md`）。
- `markup.goldmark.renderer.unsafe = true`：文章內可直接寫 HTML（例如 `<!-- TOC-AUTO-BEGIN -->` 註解標記）。

## 標題錨點（TOC 連結常見錯誤來源）

Hugo goldmark 以 GitHub 規則產生 heading ID：小寫、移除非字母數字／空白／`-`／`_` 的字元，空白逐一換成 `-`（不合併）。Emoji 變體選擇符（U+FE0F）與圈號數字（如 ②）會被丟掉。`check-toc.ps1` 的模擬並不完全精確，可能有誤報；最可靠的方式是建置到暫存目錄後用 `generate_toc.py --verify-html` 比對實際輸出的 id。

## 手冊改版慣例

多數大型手冊會隨上游工具版本改版（例如 `v3.0`），文件內含版本資訊表、附錄中的「修訂／驗證紀錄」與「待確認」小節，以及各章的審查與驗證清單。改版時延續該手冊既有的附錄結構與編號，不要另起格式。根目錄的 `expand_doc.py` 是以「錨點字串 + 插入內容」方式擴寫單一手冊的範例做法，大幅改版常用類似的一次性 Python 腳本處理，而非逐段手動編輯。

## 部署與 Git

- 推到 `main` 即觸發 `.github/workflows/hugo.yml` 建置並部署 Pages（`--baseURL` 於 CI 指定）。
- Commit 訊息慣例：`docs: update <手冊名稱>` / `docs: add <手冊名稱>`。
- `.github/hooks/auto-commit-push.ps1` 是 Stop hook：僅在 `.github/hooks/.auto-push-enabled` 存在時，於 session 結束自動 `git add -A`、commit 並 push。
- `public/`、`resources/_gen/`、`.hugo_build.lock` 為建置產物，已 gitignore，不要手動編輯。
