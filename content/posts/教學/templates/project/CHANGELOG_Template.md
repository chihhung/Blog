---
title: "變更日誌範本（CHANGELOG Template）"
date: 2026-05-18
draft: false
categories: ["教學"]
tags: ["專案管理", "範本", "軟體工程", "版本管理"]
---

# 變更日誌範本（CHANGELOG Template）

> **參照標準**：[Keep a Changelog 1.1.0](https://keepachangelog.com/) / [Semantic Versioning 2.0.0](https://semver.org/)  
> **文件用途**：記錄專案每個版本的顯著變更，讓使用者與開發者了解版本間的差異  
> **適用階段**：專案全生命週期（每次發版皆需更新）

---

## 📋 章節目錄

1. [文件資訊](#1-文件資訊)
2. [格式規範](#2-格式規範)
3. [變更類別定義](#3-變更類別定義)
4. [版本編號規則](#4-版本編號規則)
5. [撰寫規範](#5-撰寫規範)
6. [CHANGELOG 完整範本](#6-changelog-完整範本)
7. [自動化產生](#7-自動化產生)
8. [附錄](#8-附錄)

---

## 1. 文件資訊

### 📝 範本

| 項目 | 內容 |
|------|------|
| **文件名稱** | CHANGELOG.md |
| **位置** | 專案根目錄 |
| **格式** | Markdown（Keep a Changelog 格式） |
| **維護者** | {Release Manager / 開發團隊} |
| **更新時機** | 每次版本發布（Release） |

### 📖 使用說明

- CHANGELOG.md 置於專案根目錄，與 README.md 並列
- 每次 Release 前更新，不是每個 Commit 都記錄
- 記錄「對使用者有意義的變更」，非所有技術細節

### 💡 範例

CHANGELOG.md 通常長這樣的開頭：

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
```

---

## 2. 格式規範

### 📝 範本

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- {新功能描述}

## [{版本號}] - {YYYY-MM-DD}

### Added
- {新增功能}

### Changed
- {變更項目}

### Deprecated
- {即將移除的功能}

### Removed
- {已移除的功能}

### Fixed
- {修復的問題}

### Security
- {安全性修復}

[Unreleased]: {repo-url}/compare/v{版本}...HEAD
[{版本號}]: {repo-url}/compare/v{前版本}...v{版本}
```

### 📖 使用說明

- **[Unreleased]** 區塊永遠在最上方，收集尚未發布的變更
- 發版時將 [Unreleased] 內容移至新版本區塊
- 版本由新到舊排列（最新在最上面）
- 底部的連結區塊提供版本間的 diff 比較連結

### 💡 範例

見第 6 節完整範本。

---

## 3. 變更類別定義

### 📝 範本

| 類別 | 英文 | 定義 | 使用時機 |
|------|------|------|---------|
| **Added** | 新增 | 新功能 | 全新的功能或能力 |
| **Changed** | 變更 | 既有功能的行為變更 | 修改既有功能的行為（可能不向下相容） |
| **Deprecated** | 棄用 | 即將移除的功能 | 預告未來版本將移除 |
| **Removed** | 移除 | 已移除的功能 | 功能已不存在 |
| **Fixed** | 修復 | Bug 修復 | 修正不正確的行為 |
| **Security** | 安全 | 安全性相關修復 | CVE 修復、安全漏洞修補 |

### 📖 使用說明

- 六個類別完整涵蓋所有變更類型
- 每個版本不必有所有類別，只列有變更的類別
- **Security** 類別的項目建議同時附上 CVE 編號（如有）
- 類別順序固定：Added → Changed → Deprecated → Removed → Fixed → Security

### 💡 範例

| 變更描述 | 歸類為 |
|---------|--------|
| 新增批次請假匯入功能 | Added |
| 修改薪資計算邏輯（不含加班費） | Changed |
| 舊版報表 API `/api/v1/reports` 將在 v2.0 移除 | Deprecated |
| 移除已棄用的 `/api/v1/legacy-auth` 端點 | Removed |
| 修復跨月請假天數計算錯誤 | Fixed |
| 修補 JWT Token 未驗證過期時間的漏洞 | Security |

---

## 4. 版本編號規則

### 📝 範本

#### Semantic Versioning（語意化版本）

```
MAJOR.MINOR.PATCH
```

| 欄位 | 遞增時機 | 範例 |
|------|---------|------|
| **MAJOR** | 不向下相容的 API 變更 | 1.0.0 → 2.0.0 |
| **MINOR** | 向下相容的新功能 | 1.0.0 → 1.1.0 |
| **PATCH** | 向下相容的 Bug 修復 | 1.0.0 → 1.0.1 |

#### Pre-release 版本

| 格式 | 用途 | 範例 |
|------|------|------|
| {version}-alpha.{N} | 內部測試版 | 1.1.0-alpha.1 |
| {version}-beta.{N} | 公測版 | 1.1.0-beta.1 |
| {version}-rc.{N} | 候選發布版 | 1.1.0-rc.1 |

### 📖 使用說明

- MAJOR = 0 時為開發階段，API 可能隨時變更
- MAJOR ≥ 1 表示正式版，需遵守向下相容承諾
- CHANGELOG 中的版本號需與 Git Tag 一致
- 每次遞增高位版本號時，低位歸零（1.9.3 → 2.0.0）

### 💡 範例

| 情境 | 版本變化 | 說明 |
|------|---------|------|
| 新增員工自助查詢功能 | 1.0.0 → 1.1.0 | 新功能，向下相容 |
| 修復薪資計算錯誤 | 1.1.0 → 1.1.1 | Bug 修復 |
| 修改 API 回傳格式（Breaking） | 1.1.1 → 2.0.0 | 不向下相容變更 |
| 移除已棄用的端點 | 1.5.2 → 2.0.0 | Removal = Breaking Change |

---

## 5. 撰寫規範

### 📝 範本

#### 5.1 每條變更的格式

```markdown
- {動詞開頭的描述} ([#{issue-number}]({issue-url}))
```

#### 5.2 撰寫原則

| 原則 | 說明 | 好的範例 | 不好的範例 |
|------|------|---------|-----------|
| 以使用者角度撰寫 | 描述對使用者的影響 | 新增批次匯入請假功能 | 加了 BatchImportService |
| 動詞開頭 | 每條以動詞起始 | 修復跨月請假天數計算錯誤 | 跨月請假 bug |
| 附上 Issue 連結 | 可追溯至需求/Bug | 修復 #234 薪資四捨五入問題 | 修了一些 bug |
| 簡潔具體 | 一行描述一個變更 | 移除舊版登入 API `/v1/auth/legacy` | 清理程式碼 |

#### 5.3 不應記錄的內容

| 不記錄 | 原因 |
|--------|------|
| 純重構（無外部行為變更） | 使用者無感 |
| 修改 typo（非使用者可見） | 太瑣碎 |
| 開發依賴更新（devDependencies） | 使用者無感 |
| Merge commit | 非實質變更 |

### 📖 使用說明

- 目標讀者是「使用系統的人」而非「寫程式的人」
- 避免技術術語，用業務語言描述
- 每個版本的變更數量若過多（> 20 條），考慮分類加上簡要總結

### 💡 範例

**好的寫法：**
```markdown
### Fixed
- 修復跨月請假（如 1/30 ~ 2/2）天數計算為負數的問題 ([#234](https://...))
- 修復薪資明細匯出 Excel 時中文欄位名稱顯示亂碼 ([#251](https://...))
```

**不好的寫法：**
```markdown
### Fixed
- fix bug
- 修了一些問題
- Updated LeaveCalculationService.cs
```

---

## 6. CHANGELOG 完整範本

### 📝 範本

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- {開發中的新功能}

---

## [{version}] - {YYYY-MM-DD}

### Added
- {新增功能描述} ([#{N}]({url}))

### Changed
- {變更描述} ([#{N}]({url}))

### Fixed
- {修復描述} ([#{N}]({url}))

---

## [{previous-version}] - {YYYY-MM-DD}

### Added
- {新增功能描述}

---

[Unreleased]: {repo}/compare/v{version}...HEAD
[{version}]: {repo}/compare/v{previous-version}...v{version}
[{previous-version}]: {repo}/releases/tag/v{previous-version}
```

### 📖 使用說明

- 此為完整的 CHANGELOG.md 檔案範本
- 複製此範本作為新專案的起始 CHANGELOG
- [Unreleased] 持續收集尚未發版的變更
- 發版時：將 [Unreleased] 內容剪下 → 貼至新版本區塊 → 標上日期

### 💡 範例

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 員工行動裝置 App（iOS / Android）支援

---

## [1.1.0] - 2026-11-20

### Added
- 新增批次請假匯入功能，支援 Excel 格式上傳 ([#301](https://dev.azure.com/company/hrms/_workitems/edit/301))
- 新增部門假勤統計儀表板 ([#287](https://dev.azure.com/company/hrms/_workitems/edit/287))
- 新增 Email 通知範本自訂功能 ([#295](https://dev.azure.com/company/hrms/_workitems/edit/295))

### Changed
- 薪資計算引擎改用非同步處理，大幅提升月結計算效能 ([#310](https://dev.azure.com/company/hrms/_workitems/edit/310))
- 登入頁面 UI 改版，支援 RWD ([#288](https://dev.azure.com/company/hrms/_workitems/edit/288))

### Fixed
- 修復跨月請假（如 1/30 ~ 2/2）天數計算為負數的問題 ([#234](https://dev.azure.com/company/hrms/_workitems/edit/234))
- 修復薪資明細匯出 Excel 時中文欄位顯示亂碼 ([#251](https://dev.azure.com/company/hrms/_workitems/edit/251))
- 修復主管審核假單後通知未發送的問題 ([#267](https://dev.azure.com/company/hrms/_workitems/edit/267))

### Security
- 升級 System.Text.Json 至 8.0.5 修復 CVE-2024-43485 反序列化漏洞 ([#312](https://dev.azure.com/company/hrms/_workitems/edit/312))

---

## [1.0.1] - 2026-10-22

### Fixed
- 修復部分員工登入後頁面白屏問題（Session 序列化錯誤）([#256](https://dev.azure.com/company/hrms/_workitems/edit/256))
- 修復假額計算未排除到職日當天的問題 ([#258](https://dev.azure.com/company/hrms/_workitems/edit/258))

---

## [1.0.0] - 2026-10-15

### Added
- 假勤管理模組：線上請假、審核、假額管理
- 薪資管理模組：月薪計算、加班費、獎金
- 員工自助服務：個人資料查詢與修改
- Active Directory 整合 SSO 登入
- ERP 薪資資料拋轉介接
- 即時通知（系統通知 + Email）
- 角色權限管理（Admin / Manager / Employee）

---

[Unreleased]: https://dev.azure.com/company/hrms/_git/hrms/branchCompare?baseVersion=GTv1.1.0&targetVersion=GBmain
[1.1.0]: https://dev.azure.com/company/hrms/_git/hrms/branchCompare?baseVersion=GTv1.0.1&targetVersion=GTv1.1.0
[1.0.1]: https://dev.azure.com/company/hrms/_git/hrms/branchCompare?baseVersion=GTv1.0.0&targetVersion=GTv1.0.1
[1.0.0]: https://dev.azure.com/company/hrms/_git/hrms?version=GTv1.0.0
```

---

## 7. 自動化產生

### 📝 範本

#### 7.1 工具選項

| 工具 | 適用語言/平台 | 說明 |
|------|-------------|------|
| [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog) | Node.js | 依據 Conventional Commits 自動產生 |
| [auto-changelog](https://github.com/cookpete/auto-changelog) | Node.js | 依據 Git Log 產生 |
| [github-changelog-generator](https://github.com/github-changelog-generator/github-changelog-generator) | Ruby | 依據 GitHub PR/Issues 產生 |
| [Release Drafter](https://github.com/release-drafter/release-drafter) | GitHub Action | 自動草擬 Release Notes |
| [Versionize](https://github.com/versionize/versionize) | .NET | .NET 專用 Conventional Commits |

#### 7.2 CI/CD 整合範例

```yaml
# GitHub Action 範例
- name: Generate Changelog
  uses: conventional-changelog/conventional-changelog-action@v3
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    output-file: "CHANGELOG.md"
```

### 📖 使用說明

- 自動化產生需搭配嚴格的 Commit Convention（如 Conventional Commits）
- 建議半自動：工具產生初稿 → 人工潤飾 → 發布
- 純自動化產生的 CHANGELOG 可能過於技術導向，需調整措辭

### 💡 範例

使用 `conventional-changelog` CLI：

```bash
# 安裝
npm install -g conventional-changelog-cli

# 產生（追加模式）
conventional-changelog -p angular -i CHANGELOG.md -s

# 產生（全部重新產生）
conventional-changelog -p angular -i CHANGELOG.md -s -r 0
```

---

## 8. 附錄

### 📝 範本

#### 8.1 Keep a Changelog 核心原則

| 原則 | 說明 |
|------|------|
| 為人而寫 | 讀者是人，不是機器 |
| 每個版本一個條目 | 按版本分組 |
| 同類型變更分組 | 用六個類別分組 |
| 可連結 | 每個版本可連結至 diff |
| 最新在最前 | 倒序排列 |
| 顯示發布日期 | ISO 8601 格式 (YYYY-MM-DD) |
| 標示是否遵循 SemVer | 讓讀者知道版本策略 |

#### 8.2 常見問題

| 問題 | 答案 |
|------|------|
| 何時更新 CHANGELOG？ | 每個 PR 合併時更新 [Unreleased]，發版時移至版本區塊 |
| 誰負責維護？ | 每位開發者負責自己的 PR，Release Manager 負責發版整理 |
| 要記錄多詳細？ | 以使用者能理解的粒度，通常一個 Feature/Bug 一條 |
| 多語系怎麼處理？ | 建議使用英文撰寫（國際通用），或依團隊約定使用中文 |

### 📖 使用說明

- CHANGELOG 不是 Git Log 的複製品
- CHANGELOG 記錄的是「使用者關心的變更」
- 好的 CHANGELOG 能減少客服/支援工作量

### 💡 範例

**CHANGELOG vs Git Log 的差異：**

Git Log（技術導向）：
```
a1b2c3d refactor: extract PayrollEngine from PayrollService
d4e5f6g fix: null reference in LeaveCalculationService.cs line 42
g7h8i9j chore: update NuGet packages
```

CHANGELOG（使用者導向）：
```markdown
### Fixed
- 修復跨月請假天數計算錯誤，導致部分員工假額異常扣除
```

---

> 📌 **範本使用注意事項**
> 1. 本範本依據 Keep a Changelog 1.1.0 與 Semantic Versioning 2.0.0 標準編製
> 2. CHANGELOG.md 需於專案建立時即創建，不要等到發版才補
> 3. 建議搭配 Conventional Commits 規範，支援半自動化產生
> 4. 搭配「README 範本」使用，在 README 中連結至 CHANGELOG
> 5. 發版時同步更新：CHANGELOG.md → Git Tag → Release Notes
