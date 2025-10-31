+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'github使用教學'
tags = ['教學', '工具']
categories = ['教學']
+++
# GitHub 使用教學手冊

## 📋 文件資訊

- **版本**: 2.0
- **更新日期**: 2025年8月29日
- **適用對象**: 新進開發同仁、團隊協作開發者
- **維護者**: 專案開發團隊

---

## 📚 目錄

1. [Git/GitHub 基礎概念](#1-gitgithub-基礎概念)
   - 1.1 [什麼是 Git？](#11-什麼是-git)
   - 1.2 [什麼是 GitHub？](#12-什麼是-github)
   - 1.3 [為何要使用？](#13-為何要使用)
   - 1.4 [版本控制的重要性](#14-版本控制的重要性)
   - 1.5 [團隊開發的挑戰](#15-團隊開發的挑戰)
   - 1.6 [Git 的解決方案](#16-git-的解決方案)
   - 1.7 [GitHub 的附加價值](#17-github-的附加價值)

2. [環境設定](#2-環境設定)
   - 2.1 [安裝 Git](#21-安裝-git)
   - 2.2 [設定個人資訊](#22-設定個人資訊)
   - 2.3 [GitHub 帳號設定](#23-github-帳號設定)
   - 2.4 [Personal Access Token 設定（替代方案）](#24-personal-access-token-設定替代方案)
   - 2.5 [Git 效能優化設定](#25-git-效能優化設定)

3. [基本操作流程](#3-基本操作流程)
   - 3.1 [Clone 專案](#31-clone-專案)
   - 3.2 [建立 Feature Branch](#32-建立-feature-branch)
   - 3.3 [Commit Message 撰寫規範](#33-commit-message-撰寫規範)
   - 3.4 [Push 到 Remote](#34-push-到-remote)
   - 3.5 [建立 Pull Request (PR)](#35-建立-pull-request-pr)
   - 3.6 [Code Review 流程](#36-code-review-流程)
   - 3.7 [Merge 規範](#37-merge-規範)

4. [Git 進階操作](#4-git-進階操作)
   - 4.1 [Interactive Rebase](#41-interactive-rebase)
   - 4.2 [Cherry-pick 操作](#42-cherry-pick-操作)
   - 4.3 [Git Bisect 除錯](#43-git-bisect-除錯)
   - 4.4 [Stash 暫存操作](#44-stash-暫存操作)
   - 4.5 [Submodule 子模組管理](#45-submodule-子模組管理)
   - 4.6 [Git Hooks 自動化](#46-git-hooks-自動化)
   - 4.7 [大型檔案處理 (LFS)](#47-大型檔案處理-lfs)

5. [日常工作流程建議](#5-日常工作流程建議)
   - 5.1 [每日工作開始前](#51-每日工作開始前)
   - 5.2 [避免衝突的最佳實務](#52-避免衝突的最佳實務)
   - 5.3 [分支管理策略](#53-分支管理策略)
   - 5.4 [工作流程檢查清單](#54-工作流程檢查清單)
   - 5.5 [團隊協作最佳實務](#55-團隊協作最佳實務)

6. [常見錯誤與解決方式](#6-常見錯誤與解決方式)
   - 6.1 [Merge Conflict（合併衝突）](#61-merge-conflict合併衝突)
   - 6.2 [錯誤的 Commit](#62-錯誤的-commit)
   - 6.3 [誤刪檔案恢復](#63-誤刪檔案恢復)
   - 6.4 [Push 被拒絕](#64-push-被拒絕)
   - 6.5 [忘記切換分支](#65-忘記切換分支)
   - 6.6 [Git 狀態混亂](#66-git-狀態混亂)
   - 6.7 [效能問題排除](#67-效能問題排除)
   - 6.8 [網路連線問題](#68-網路連線問題)

7. [專案專屬規範](#7-專案專屬規範)
   - 7.1 [分支命名規則](#71-分支命名規則)
   - 7.2 [Commit Message 標準](#72-commit-message-標準)
   - 7.3 [Pull Request 規範](#73-pull-request-規範)
   - 7.4 [Code Review 標準](#74-code-review-標準)

8. [GitHub 進階功能與協作工具](#8-github-進階功能與協作工具)
   - 8.1 [Issue 管理](#81-issue-管理)
   - 8.2 [Project 專案管理](#82-project-專案管理)
   - 8.3 [Wiki 文件系統](#83-wiki-文件系統)
   - 8.4 [Releases 版本發布](#84-releases-版本發布)
   - 8.5 [Discussions 社群討論](#85-discussions-社群討論)
   - 8.6 [Security 安全功能](#86-security-安全功能)
   - 8.7 [GitHub CLI 進階應用](#87-github-cli-進階應用)
   - 8.8 [GitHub Apps 與整合](#88-github-apps-與整合)
   - 8.9 [GitHub Copilot 整合](#89-github-copilot-整合)

9. [CI/CD 持續整合與部署](#9-cicd-持續整合與部署)
   - 9.1 [CI/CD 基礎概念](#91-cicd-基礎概念)
   - 9.2 [工作流程設定](#92-工作流程設定)
   - 9.3 [進階 CI 配置](#93-進階-ci-配置)
   - 9.4 [持續部署 (CD)](#94-持續部署-cd)
   - 9.5 [分支保護與自動化](#95-分支保護與自動化)
   - 9.6 [監控與通知](#96-監控與通知)
   - 9.7 [Secrets 與環境變數管理](#97-secrets-與環境變數管理)
   - 9.8 [最佳實務與注意事項](#98-最佳實務與注意事項)

10. [安全最佳實務](#10-安全最佳實務)
    - 10.1 [認證與授權](#101-認證與授權)
    - 10.2 [機密資訊管理](#102-機密資訊管理)
    - 10.3 [程式碼安全掃描](#103-程式碼安全掃描)
    - 10.4 [依賴套件安全](#104-依賴套件安全)
    - 10.5 [分支保護規則](#105-分支保護規則)
    - 10.6 [審計與監控](#106-審計與監控)

11. [VS Code Git 整合深度應用](#11-vs-code-git-整合深度應用)
    - 11.1 [Source Control 面板詳解](#111-source-control-面板詳解)
    - 11.2 [Git Graph 擴充功能](#112-git-graph-擴充功能)
    - 11.3 [GitLens 進階功能](#113-gitlens-進階功能)
    - 11.4 [Merge Conflict 解決工具](#114-merge-conflict-解決工具)
    - 11.5 [自動化工作流程設定](#115-自動化工作流程設定)

12. [附錄：常用指令清單](#12-附錄常用指令清單)
    - 12.1 [基本指令](#121-基本指令)
    - 12.2 [分支操作](#122-分支操作)
    - 12.3 [提交操作](#123-提交操作)
    - 12.4 [同步操作](#124-同步操作)
    - 12.5 [檢查與比較](#125-檢查與比較)
    - 12.6 [復原操作](#126-復原操作)
    - 12.7 [進階操作指令](#127-進階操作指令)
    - 12.8 [CI/CD 相關指令](#128-cicd-相關指令)

13. [檢查清單](#13-檢查清單)
    - 13.1 [新進員工設定檢查清單](#131-新進員工設定檢查清單)
    - 13.2 [日常開發檢查清單](#132-日常開發檢查清單)
    - 13.3 [Code Review 檢查清單](#133-code-review-檢查清單)
    - 13.4 [合併前檢查清單](#134-合併前檢查清單)
    - 13.5 [CI/CD 檢查清單](#135-cicd-檢查清單)
    - 13.6 [GitHub 功能使用檢查清單](#136-github-功能使用檢查清單)
    - 13.7 [緊急情況檢查清單](#137-緊急情況檢查清單)
    - 13.8 [安全檢查清單](#138-安全檢查清單)

14. [疑難排解與支援](#14-疑難排解與支援)
    - 14.1 [常見問題 FAQ](#141-常見問題-faq)
    - 14.2 [效能優化指南](#142-效能優化指南)
    - 14.3 [技術支援聯絡方式](#143-技術支援聯絡方式)
    - 14.4 [學習資源推薦](#144-學習資源推薦)

---

## 1. Git/GitHub 基礎概念

### 1.1 什麼是 Git？

Git 是一個**分散式版本控制系統**，幫助開發團隊：

- 追蹤程式碼的變更歷史
- 支援多人同時開發
- 管理不同功能分支
- 回復到任何歷史版本

### 1.2 什麼是 GitHub？

GitHub 是基於 Git 的**雲端程式碼託管平台**，提供：

- 遠端程式碼倉庫存儲
- 團隊協作工具（Pull Request、Issue）
- 程式碼審查功能
- 專案管理工具

### 1.3 為何要使用？

#### 🔍 版本控制的好處

- **追溯性**: 知道誰在什麼時候修改了什麼
- **備份性**: 程式碼安全存放在雲端
- **協作性**: 多人可同時開發不衝突
- **實驗性**: 可建立分支測試新功能

#### 💼 團隊協作優勢

- 統一的程式碼審查流程
- 清楚的變更歷史記錄
- 自動化測試整合
- 專案進度可視化

### 1.4 版本控制的重要性

版本控制系統是現代軟體開發不可或缺的工具：

- **歷史追蹤**: 完整記錄每次變更，可追溯任何時間點的程式碼狀態
- **協同合作**: 多人可同時在不同功能上開發，避免互相覆蓋
- **分支管理**: 可建立獨立分支進行實驗性開發，不影響主要程式碼
- **錯誤復原**: 當發現問題時，可快速回復到穩定版本

### 1.5 團隊開發的挑戰

沒有版本控制時，團隊開發會遇到許多問題：

- 💥 **程式碼衝突**: 多人同時修改同一檔案，容易互相覆蓋
- � **版本混亂**: 資料夾堆滿 `專案_v1`, `專案_final`, `專案_final_真的最終版`
- ❓ **追蹤困難**: 不知道誰在什麼時候改了什麼，為什麼要改
- 🐛 **問題定位**: 當發現 bug 時，難以確定是哪次修改造成的

### 1.6 Git 的解決方案

Git 透過以下機制解決團隊開發挑戰：

#### 分散式架構

- 每個開發者都有完整的程式碼庫副本
- 不依賴中央伺服器即可進行版本控制
- 離線也能提交變更和查看歷史

#### 分支策略

- 輕量級分支，建立和切換快速
- 支援複雜的分支合併策略
- 可並行開發多個功能

#### 變更追蹤

- 每次提交都有唯一識別碼
- 記錄誰、何時、為何做了變更
- 可輕鬆比較不同版本的差異

### 1.7 GitHub 的附加價值

GitHub 在 Git 基礎上提供了豐富的協作功能：

#### 協作工具

- **Pull Request**: 程式碼審查和討論平台
- **Issues**: 問題追蹤和任務管理
- **Projects**: 看板式專案管理
- **Wiki**: 協作文件撰寫

#### 自動化功能

- **GitHub Actions**: CI/CD 工作流程
- **Dependabot**: 依賴套件自動更新
- **CodeQL**: 程式碼安全掃描

#### 社群生態

- 開源專案託管
- 程式碼分享和學習
- 開發者社群互動

### �📝 實務案例

```text
情境：小明要修改登入功能
傳統方式：複製整個專案資料夾 → 容易混亂
Git 方式：建立 feature/login-improvement 分支 → 清楚管理
```

---

## 2. 環境設定

### 2.1 安裝 Git

#### Windows 系統

1. 下載 Git：[https://git-scm.com/download/win](https://git-scm.com/download/win)
2. 執行安裝檔，建議選項：
   - ✅ Git Bash Here
   - ✅ Git GUI Here
   - ✅ Associate .git* configuration files
3. 完成後開啟 PowerShell 驗證：

```powershell
git --version
```

#### macOS 系統

```bash
# 使用 Homebrew
brew install git

# 或使用 Xcode Command Line Tools
xcode-select --install
```

### 2.2 設定個人資訊

```bash
### 設定使用者名稱（顯示在 commit 中）
git config --global user.name "您的姓名"

### 設定電子郵件（建議使用公司信箱）
git config --global user.email "your.email@company.com"

### 驗證設定
git config --list
```

### 2.3 GitHub 帳號設定

#### 建立 GitHub 帳號

1. 前往 <https://github.com>
2. 點選 "Sign up" 註冊
3. 建議使用公司統一的命名規則

#### SSH 金鑰設定（推薦）

```bash
### 1. 產生 SSH 金鑰
ssh-keygen -t ed25519 -C "your.email@company.com"

### 2. 啟動 SSH agent
eval "$(ssh-agent -s)"

### 3. 新增金鑰到 agent
ssh-add ~/.ssh/id_ed25519

### 4. 複製公鑰內容
cat ~/.ssh/id_ed25519.pub
```

#### 在 GitHub 新增 SSH 金鑰

1. 登入 GitHub → Settings → SSH and GPG keys
2. 點選 "New SSH key"
3. 貼上公鑰內容並儲存
4. 測試連線：

```bash
ssh -T git@github.com
```

### 2.4 Personal Access Token 設定（替代方案）

如果無法使用 SSH，可使用 Token：

1. GitHub → Settings → Developer settings → Personal access tokens
2. 點選 "Generate new token"
3. 設定權限範圍（建議勾選 repo、workflow）
4. 複製 token（⚠️ 只會顯示一次）

### 📝 注意事項

- SSH 金鑰較安全且方便，建議優先使用
- Token 請妥善保存，不要提交到程式碼中
- 定期更新 Git 版本以確保安全性

### 2.5 Git 效能優化設定

#### 基本效能設定

```bash
### 啟用平行處理
git config --global pack.threads 0
git config --global index.threads 0

### 提升 push/fetch 效能
git config --global pack.packSizeLimit 2g
git config --global pack.windowMemory 256m

### 啟用檔案系統監控（Windows）
git config --global core.fsmonitor true
git config --global core.untrackedcache true
```

#### 大型專案優化

```bash
### 設定 partial clone（僅克隆需要的部分）
git clone --filter=blob:none <url>

### 設定淺層克隆（減少歷史記錄）
git clone --depth 1 <url>

### 僅下載指定分支
git clone --single-branch --branch <branch> <url>
```

#### 網路連線優化

```bash
### 增加緩衝區大小
git config --global http.postBuffer 524288000

### 設定連線超時
git config --global http.lowSpeedLimit 1000
git config --global http.lowSpeedTime 300

### 啟用 HTTP/2
git config --global http.version HTTP/2
```

---

## 3. 基本操作流程

### 3.1 Clone 專案

#### 第一次取得專案

```bash
### 使用 SSH（推薦）
git clone git@github.com:your-organization/project-name.git

### 使用 HTTPS
git clone <https://github.com/your-organization/project-name.git>

### 進入專案目錄
cd project-name
```

#### 設定遠端倉庫別名

```bash
### 查看目前遠端設定
git remote -v

### 新增上游倉庫（用於同步主分支）
git remote add upstream git@github.com:main-organization/project-name.git
```

### 3.2 建立 Feature Branch

#### 分支命名規範

我們專案採用以下命名規範：

```bash
### 功能開發
feature/功能名稱-簡短描述
feature/user-login-validation
feature/payment-integration

### 錯誤修復
bugfix/錯誤描述
bugfix/login-session-timeout
bugfix/payment-calculation-error

### 熱修復
hotfix/緊急修復描述
hotfix/security-vulnerability

### 文件更新
docs/文件類型
docs/api-documentation
docs/user-guide
```

#### 建立分支流程

```bash
### 1. 確保在主分支並取得最新版本
git checkout main
git pull origin main

### 2. 建立並切換到新分支
git checkout -b feature/user-profile-update

### 3. 確認目前分支
git branch
```

### 3.3 Commit Message 撰寫規範

#### 格式標準

我們採用 **Conventional Commits** 格式：

```text
<類型>[可選範圍]: <描述>

[可選本文]

[可選註腳]
```

#### 類型定義

| 類型 | 說明 | 範例 |
|------|------|------|
| `feat` | 新功能 | `feat: 新增使用者登入功能` |
| `fix` | 錯誤修復 | `fix: 修復登入頁面驗證問題` |
| `docs` | 文件變更 | `docs: 更新 API 文件` |
| `style` | 程式碼格式 | `style: 調整縮排格式` |
| `refactor` | 重構 | `refactor: 重構使用者服務邏輯` |
| `test` | 測試相關 | `test: 新增登入功能測試` |
| `chore` | 雜項任務 | `chore: 更新依賴套件版本` |

#### 撰寫範例

```bash
### ✅ 良好的 commit message
git commit -m "feat: 新增使用者密碼強度驗證功能

- 實作密碼複雜度檢查
- 新增密碼強度指示器
- 更新相關測試案例

Closes #123"

### ❌ 不良的 commit message
git commit -m "修改"
git commit -m "update code"
git commit -m "fix bug"
```

### 3.4 Push 到 Remote

#### 基本推送流程

```bash
### 1. 檢查工作目錄狀態
git status

### 2. 新增變更檔案
git add .                    # 新增所有變更
git add src/main/User.java   # 新增特定檔案

### 3. 提交變更
git commit -m "feat: 新增使用者註冊功能"

### 4. 推送到遠端分支
git push origin feature/user-registration

### 5. 首次推送設定上游分支
git push -u origin feature/user-registration
```

#### 推送前檢查清單

- [ ] 程式碼已通過本地測試
- [ ] Commit message 符合規範
- [ ] 沒有包含敏感資訊（密碼、API key）
- [ ] 程式碼已經過 lint 檢查

### 3.5 建立 Pull Request (PR)

#### PR 建立步驟

1. **推送分支後，GitHub 會顯示建立 PR 的提示**
2. **填寫 PR 資訊**：

```markdown
## 📋 變更摘要
簡述這個 PR 的目的和主要變更

## 🔧 變更內容
- [ ] 新增使用者註冊 API
- [ ] 實作 email 驗證功能
- [ ] 新增相關單元測試
- [ ] 更新 API 文件

## 🧪 測試
- [ ] 單元測試已通過
- [ ] 整合測試已通過
- [ ] 手動測試已完成

## 📸 截圖/影片
（如果是 UI 變更，請附上截圖）

## 🔗 相關 Issue
Closes #123
Related to #456
```

#### PR 標題規範

```text
[類型] 簡短描述 (#Issue編號)

範例：
[Feature] 新增使用者註冊功能 (#123)
[Bugfix] 修復登入驗證錯誤 (#456)
[Docs] 更新 API 使用說明 (#789)
```

### 3.6 Code Review 流程

#### 提交者責任

1. **自我檢查**：
   - 程式碼符合專案規範
   - 測試覆蓋率充足
   - 文件已更新

2. **指派審查者**：
   - 至少指派 2 位審查者
   - 包含資深開發者或架構師

#### 審查者責任

1. **檢查重點**：
   - 功能邏輯正確性
   - 程式碼品質與可讀性
   - 安全性考量
   - 效能影響

2. **回饋方式**：

   ```markdown
   # ✅ 建設性回饋
   建議將這個方法拆分為更小的函數，提高可讀性
   
   # ❌ 非建設性回饋
   這段程式碼不好
   ```

### 3.7 Merge 規範

#### Merge 方式選擇

| 方式 | 使用時機 | 優點 | 缺點 |
|------|----------|------|------|
| **Merge Commit** | 功能分支合併 | 保留分支歷史 | 歷史較複雜 |
| **Squash Merge** | 小型功能 | 歷史簡潔 | 失去詳細歷史 |
| **Rebase Merge** | 單一提交 | 線性歷史 | 需要經驗 |

#### 專案預設設定

我們專案採用 **Squash Merge**：

- 保持主分支歷史簡潔
- 每個功能一個提交
- 便於回溯和 cherry-pick

### 📝 完整開發流程範例

```text
完整開發流程範例：

1. 接到任務：開發使用者頭像上傳功能
2. 建立分支：git checkout -b feature/user-avatar-upload
3. 開發程式碼：實作上傳邏輯、API、測試
4. 提交變更：git commit -m "feat: 新增使用者頭像上傳功能"
5. 推送分支：git push origin feature/user-avatar-upload
6. 建立 PR：填寫完整的 PR 描述
7. 程式碼審查：修正審查者建議
8. 合併到主分支：使用 Squash Merge
9. 刪除分支：清理遠端和本地分支
```

---

## 4. Git 進階操作

### 4.1 Interactive Rebase

#### 什麼是 Interactive Rebase？

Interactive Rebase 是一個強大的 Git 功能，允許你重新整理 commit 歷史。

```bash
### 重新整理最近 3 個 commit
git rebase -i HEAD~3

### 重新整理到指定 commit
git rebase -i <commit-hash>
```

#### 常用操作

```text
pick    - 保留 commit
reword  - 修改 commit message
edit    - 修改 commit 內容
squash  - 合併到前一個 commit
fixup   - 合併到前一個 commit（不保留 message）
drop    - 刪除 commit
```

#### 實務範例

```bash
### 情境：合併多個小 commit 成一個功能 commit
git rebase -i HEAD~4

### 編輯器會開啟，修改為：
### pick 1234567 feat: 新增登入功能框架
### squash 2345678 feat: 加入密碼驗證
### squash 3456789 feat: 加入錯誤處理
### squash 4567890 feat: 新增單元測試

```

### 4.2 Cherry-pick 操作

#### 基本概念

Cherry-pick 可以選擇性地將某個 commit 應用到當前分支。

```bash
### 將特定 commit 應用到當前分支
git cherry-pick <commit-hash>

### 應用多個 commit
git cherry-pick <commit1> <commit2>

### 應用一個範圍的 commit
git cherry-pick <commit1>..<commit2>
```

#### 實務應用場景

```bash
### 場景1：緊急修復需要應用到多個分支
git checkout main
git cherry-pick <hotfix-commit-hash>

git checkout develop
git cherry-pick <hotfix-commit-hash>

### 場景2：選擇性合併功能
git checkout feature-branch
git cherry-pick <specific-feature-commit>
```

### 4.3 Git Bisect 除錯

#### 自動化問題定位

Git Bisect 使用二分搜尋法快速定位引入問題的 commit。

```bash
### 開始 bisect
git bisect start

### 標記當前版本為有問題的版本
git bisect bad

### 標記某個已知正常的版本
git bisect good <good-commit-hash>

### Git 會自動切換到中間的 commit
### 測試後標記結果
git bisect good  # 或 git bisect bad

### 重複直到找到問題 commit
### 結束 bisect
git bisect reset
```

#### 自動化測試腳本

```bash
### 使用腳本自動化 bisect
git bisect start HEAD <good-commit>
git bisect run ./test-script.sh

### test-script.sh 範例
#!/bin/bash
make test
if [ $? -eq 0 ]; then
    exit 0  # 測試通過
else
    exit 1  # 測試失敗
fi
```

### 4.4 Stash 暫存操作

#### 基本 Stash 操作

```bash
### 暫存當前變更
git stash

### 暫存包含新檔案
git stash -u

### 暫存並添加訊息
git stash push -m "暫存登入功能開發中的變更"

### 查看 stash 列表
git stash list

### 應用最近的 stash
git stash pop

### 應用特定的 stash
git stash apply stash@{1}

### 刪除 stash
git stash drop stash@{0}
```

#### 進階 Stash 技巧

```bash
### 僅 stash 特定檔案
git stash push -m "僅暫存設定檔" config.js

### 建立新分支並應用 stash
git stash branch new-feature-branch stash@{0}

### 查看 stash 的差異
git stash show -p stash@{0}
```

### 4.5 Submodule 子模組管理

#### 新增子模組

```bash
### 添加子模組
git submodule add <repository-url> <path>

### 例如
git submodule add <https://github.com/user/library.git> lib/library
```

#### 使用子模組

```bash
### Clone 包含子模組的專案
git clone --recursive <repository-url>

### 或先 clone 再初始化子模組
git clone <repository-url>
git submodule init
git submodule update

### 更新子模組
git submodule update --remote

### 更新特定子模組
git submodule update --remote lib/library
```

#### 子模組最佳實務

```bash
### 總是記錄子模組的具體版本
cd lib/library
git checkout <specific-commit-or-tag>
cd ../..
git add lib/library
git commit -m "更新library到v1.2.3"

### 移除子模組
git submodule deinit lib/library
git rm lib/library
rm -rf .git/modules/lib/library
```

### 4.6 Git Hooks 自動化

#### Pre-commit Hook

```bash
#!/bin/sh
### .git/hooks/pre-commit

### 檢查程式碼格式
if ! npm run lint; then
    echo "代碼格式檢查失敗，請修正後再commit"
    exit 1
fi

### 執行測試
if ! npm test; then
    echo "測試失敗，請修正後再commit"
    exit 1
fi

echo "Pre-commit 檢查通過"
```

#### Pre-push Hook

```bash
#!/bin/sh
### .git/hooks/pre-push

### 檢查分支命名規範
branch=$(git rev-parse --abbrev-ref HEAD)
valid_pattern="^(feature|bugfix|hotfix)\/[a-z0-9-]+$"

if [[ ! $branch =~ $valid_pattern ]]; then
    echo "分支名稱不符合規範: $branch"
    echo "請使用格式: feature/feature-name"
    exit 1
fi

echo "Pre-push 檢查通過"
```

### 4.7 大型檔案處理 (LFS)

#### 安裝和設定 Git LFS

```bash
### 安裝 Git LFS
git lfs install

### 追蹤特定類型的檔案
git lfs track "*.psd"
git lfs track "*.mp4"
git lfs track "*.zip"

### 查看追蹤的檔案類型
git lfs track

### 提交 .gitattributes
git add .gitattributes
git commit -m "設定 Git LFS 追蹤規則"
```

#### LFS 日常操作

```bash
### 查看 LFS 檔案
git lfs ls-files

### 檢查 LFS 狀態
git lfs status

### 手動添加大檔案到 LFS
git lfs track "large-file.zip"
git add large-file.zip
git commit -m "新增大型檔案"

### Clone 時不下載 LFS 檔案
git clone --filter=blob:none <url>
git lfs pull  # 需要時再下載
```

---

## 5. 日常工作流程建議

### 5.1 每日工作開始前

#### 同步主分支

```bash
### 1. 切換到主分支
git checkout main

### 2. 拉取最新變更
git pull origin main

### 3. 如果有設定 upstream，也同步上游
git fetch upstream
git merge upstream/main
```

#### 更新功能分支

```bash
### 1. 切換到功能分支
git checkout feature/your-feature

### 2. 合併主分支最新變更
git merge main

### 或使用 rebase（保持線性歷史）
git rebase main
```

### 5.2 避免衝突的最佳實務

#### 頻繁同步

```bash
### 建議每天至少執行一次
git checkout main
git pull origin main
git checkout feature/your-feature
git merge main
```

#### 小批次提交

```bash
### ✅ 好的實務：小而頻繁的提交
git add src/user/UserService.java
git commit -m "feat: 新增使用者驗證方法"

git add src/user/UserController.java
git commit -m "feat: 新增使用者 API 端點"

### ❌ 避免：一次大量提交
git add .
git commit -m "完成所有功能"
```

### 5.3 分支管理策略

#### 分支生命週期

```text
1. 建立分支    ←── 從最新的 main 分支建立
2. 開發階段    ←── 頻繁提交，定期同步 main
3. 完成開發    ←── 最終測試，準備 PR
4. Code Review ←── 修正建議，可能需要額外提交
5. 合併主分支  ←── Squash merge 到 main
6. 清理分支    ←── 刪除遠端和本地分支
```

#### 分支清理

```bash
### 查看所有分支
git branch -a

### 刪除已合併的本地分支
git branch -d feature/completed-feature

### 強制刪除本地分支
git branch -D feature/abandoned-feature

### 刪除遠端分支
git push origin --delete feature/completed-feature

### 清理已刪除的遠端分支參考
git fetch --prune
```

### 5.4 工作流程檢查清單

#### 開始新功能前

- [ ] 已同步最新的 main 分支
- [ ] 從 main 建立新的功能分支
- [ ] 分支名稱符合命名規範
- [ ] 已設定正確的上游分支

#### 開發過程中

- [ ] 定期提交小批次變更
- [ ] Commit message 符合規範
- [ ] 定期同步 main 分支變更
- [ ] 程式碼通過本地測試

#### 提交 PR 前

- [ ] 所有測試通過
- [ ] 程式碼符合風格指南
- [ ] 已更新相關文件
- [ ] PR 描述完整清楚

### 5.5 團隊協作最佳實務

#### 溝通規範

```markdown
📢 **團隊溝通原則**

1. **透明化**: 所有變更都應在相關的 issue 或 PR 中討論
2. **文件化**: 重要決策應記錄在 Wiki 或討論區
3. **及時反應**: 24小時內回應 PR review 請求
4. **建設性回饋**: 提供具體、可行的改進建議
```

#### 程式碼品質維護

```bash
### 每日程式碼品質檢查
### 1. 執行靜態分析
npm run lint
sonar-scanner

### 2. 檢查測試覆蓋率
npm run test:coverage

### 3. 依賴套件安全掃描
npm audit
```

#### 分支生命週期管理

```markdown
🔄 **分支管理流程**

1. **功能分支** (feature/*)
   - 生命週期: 1-2 週
   - 定期與 main 同步
   - 完成後立即刪除

2. **修復分支** (bugfix/*)
   - 生命週期: 3-5 天
   - 緊急修復可直接從 main 分支

3. **發布分支** (release/*)
   - 生命週期: 1-3 天
   - 僅允許 bug 修復和文件更新
```

#### 團隊規模化策略

```yaml
### 小型團隊 (2-5人)
workflow: "GitHub Flow"
review_required: 1
merge_strategy: "Squash and merge"

### 中型團隊 (6-15人)
workflow: "Git Flow"
review_required: 2
merge_strategy: "Create merge commit"
branch_protection: true

### 大型團隊 (15+人)
workflow: "GitHub Flow + Feature flags"
review_required: 2-3
merge_strategy: "Squash and merge"
automated_testing: true
```

#### 知識分享機制

```markdown
📚 **團隊學習計畫**

- **Code Review 學習**
  - 每週輪流擔任 review 導師
  - 分享最佳實務和常見問題

- **技術分享會**
  - 每月技術主題分享
  - Git 進階技巧工作坊

- **文件維護**
  - 每季更新開發指南
  - 新人 onboarding 流程優化
```

---

## 6. 常見錯誤與解決方式

### 6.1 Merge Conflict（合併衝突）

#### 發生原因

```text
當兩個分支修改了同一個檔案的同一行時，Git 無法自動合併
```

#### 解決步驟

```bash
### 1. 拉取最新變更時發生衝突
git pull origin main
### 輸出：Auto-merging failed; fix conflicts and then commit

### 2. 查看衝突檔案
git status
### 輸出：Unmerged paths: both modified: src/User.java

### 3. 編輯衝突檔案
### 檔案中會顯示：
### <<<<<<< HEAD
### 您的變更
### =======
### 其他人的變更
### >>>>>>> branch-name

### 4. 手動解決衝突（保留需要的程式碼）
### 刪除衝突標記，保留正確的程式碼

### 5. 標記衝突已解決
git add src/User.java

### 6. 完成合併
git commit -m "resolve: 解決 User.java 合併衝突"
```

#### 預防衝突的方法

```bash
### 方法1：使用 rebase 替代 merge
git checkout feature/your-feature
git rebase main

### 方法2：頻繁同步主分支
git checkout main
git pull origin main
git checkout feature/your-feature
git merge main

### 方法3：協調開發範圍
### 團隊內溝通避免同時修改相同檔案

```

### 6.2 錯誤的 Commit

#### 修改最後一次 commit message

```bash
### 如果還沒 push
git commit --amend -m "正確的 commit message"

### 如果已經 push（需要 force push，要小心）
git commit --amend -m "正確的 commit message"
git push --force-with-lease origin feature/your-branch
```

#### 取消最後一次 commit

```bash
### 保留變更，只取消 commit
git reset --soft HEAD~1

### 完全取消變更和 commit
git reset --hard HEAD~1

### 取消多次 commit
git reset --soft HEAD~3  # 取消最近3次
```

#### 從 commit 中移除檔案

```bash
### 從最後一次 commit 中移除檔案
git reset --soft HEAD~1
git reset HEAD path/to/unwanted/file
git commit -m "正確的 commit message"
```

### 6.3 誤刪檔案恢復

#### 恢復已刪除但未 commit 的檔案

```bash
### 查看被刪除的檔案
git status

### 恢復特定檔案
git checkout HEAD -- path/to/deleted/file

### 恢復所有被刪除的檔案
git checkout HEAD -- .
```

#### 恢復已 commit 的刪除

```bash
### 查找檔案被刪除的 commit
git log --oneline --follow -- path/to/deleted/file

### 從該 commit 的前一版本恢復檔案
git checkout <commit-hash>~1 -- path/to/deleted/file

### 提交恢復的檔案
git add path/to/deleted/file
git commit -m "restore: 恢復意外刪除的檔案"
```

### 6.4 Push 被拒絕

#### 原因與解決

```bash
### 常見錯誤訊息
! [rejected] main -> main (fetch first)

### 原因：遠端分支有新的變更
### 解決方法：
git pull origin main
git push origin main

### 如果有衝突，先解決衝突再 push

```

#### Force Push 的正確使用

```bash
### ❌ 危險：可能覆蓋他人變更
git push --force origin main

### ✅ 安全：只在沒有他人變更時強制推送
git push --force-with-lease origin feature/your-branch
```

### 6.5 忘記切換分支

#### 在錯誤分支上開發

```bash
### 情況：在 main 分支上做了變更，但還沒 commit
### 解決：移動變更到正確分支

### 1. 暫存目前變更
git stash

### 2. 建立或切換到正確分支
git checkout -b feature/correct-branch

### 3. 恢復變更
git stash pop
```

#### 在錯誤分支上 commit

```bash
### 情況：已經在 main 分支上 commit
### 解決：移動 commit 到正確分支

### 1. 建立新分支（包含錯誤的 commit）
git branch feature/correct-branch

### 2. 重置 main 分支
git reset --hard HEAD~1

### 3. 切換到正確分支
git checkout feature/correct-branch
```

### 6.6 Git 狀態混亂

#### 重置到乾淨狀態

```bash
### 查看目前狀態
git status

### 取消所有未暫存的變更
git checkout -- .

### 移除未追蹤的檔案
git clean -fd

### 取消已暫存的變更
git reset HEAD

### 完全重置到最後一次 commit
git reset --hard HEAD
```

### 📝 緊急求救指令

```bash
### 當一切都亂了，想回到安全狀態
git reflog                    # 查看所有操作歷史
git reset --hard HEAD@{n}     # 回到特定操作前的狀態

### 備份目前狀態再進行危險操作
git branch backup-$(date +%Y%m%d-%H%M%S)

### 查看誰修改了什麼
git blame path/to/file        # 查看每行的修改者
git log -p path/to/file       # 查看檔案的修改歷史
```

### 6.7 效能問題排除

#### Git 操作緩慢

```bash
### 診斷 Git 效能問題
git count-objects -v          # 檢查物件數量
git gc --aggressive           # 強制垃圾收集
git repack -a -d             # 重新包裝物件
```

#### 大型儲存庫優化

```bash
### 檢查大型檔案
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0,6)}' | \
  sort --numeric-sort --key=2 | \
  tail -20

### 清理無用的參考
git remote prune origin
git gc --prune=now

### 使用 partial clone 減少下載大小
git clone --filter=blob:limit=100k <url>
```

#### 網路連線問題診斷

```bash
### 測試連線
ssh -T git@github.com
ping github.com

### 檢查 SSL 設定
git config --global http.sslVerify false  # 臨時解決方案
git config --global http.sslBackend schannel  # Windows

### 使用 HTTP 替代 SSH（臨時）
git remote set-url origin <https://github.com/user/repo.git>
```

### 6.8 網路連線問題

#### SSH 連線問題

```bash
### 檢查 SSH 金鑰
ssh-add -l
ssh -T git@github.com

### 重新生成 SSH 金鑰
ssh-keygen -t ed25519 -C "your.email@example.com"
ssh-add ~/.ssh/id_ed25519

### SSH 設定檔 (~/.ssh/config)
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```

#### 代理伺服器設定

```bash
### HTTP 代理設定
git config --global http.proxy <http://proxy.company.com:8080>
git config --global https.proxy <http://proxy.company.com:8080>

### SOCKS 代理設定
git config --global http.proxy socks5://localhost:1080

### 取消代理設定
git config --global --unset http.proxy
git config --global --unset https.proxy
```

#### 防火牆問題解決

```bash
### 使用 HTTPS 替代 SSH
git config --global url."<https://github.com/".insteadOf> git@github.com:

### 測試不同埠號
ssh -T -p 443 git@ssh.github.com

### SSH 設定使用 443 埠
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
```

---

## 7. 專案專屬規範

### 7.1 分支命名規則

#### 強制規範

```text
格式：<類型>/<簡短描述>-<票號>

範例：
✅ feature/user-authentication-123
✅ bugfix/login-timeout-456
✅ hotfix/security-patch-789
✅ docs/api-documentation-012

❌ my-feature
❌ fix
❌ temp-branch
❌ test123
```

#### 分支類型定義

| 類型 | 用途 | 生命週期 | 合併目標 |
|------|------|----------|----------|
| `feature/*` | 新功能開發 | 中長期 | main |
| `bugfix/*` | 錯誤修復 | 短期 | main |
| `hotfix/*` | 緊急修復 | 即時 | main + release |
| `docs/*` | 文件更新 | 短期 | main |
| `refactor/*` | 程式碼重構 | 中期 | main |
| `test/*` | 測試相關 | 短期 | main |

### 7.2 Commit Message 標準

#### 強制格式

```text
<type>(<scope>): <subject>

<body>

<footer>
```

#### 詳細規範

```bash
### 標題行（必須）
### - 類型：feat, fix, docs, style, refactor, test, chore
### - 範圍：可選，如 auth, payment, user
### - 主旨：簡潔描述，現在式，小寫開頭，不超過50字

### 內容（可選）
### - 詳細說明變更內容
### - 說明為什麼而非怎麼做
### - 每行不超過72字

### 註腳（可選）
### - 破壞性變更：BREAKING CHANGE: 描述
### - 關閉 Issue：Closes #123, Fixes #456
### - 相關 Issue：Related to #789

```

#### 範例集

```bash
### 新功能
feat(auth): 新增 JWT token 驗證機制

實作基於 JWT 的使用者驗證系統：
- 新增 token 生成和驗證邏輯
- 整合到現有的登入流程
- 新增相關的單元測試

Closes #123

### 錯誤修復
fix(payment): 修復信用卡驗證邏輯錯誤

修正信用卡號碼驗證演算法，解決 Visa 卡無法通過驗證的問題

Fixes #456

### 文件更新
docs(api): 更新使用者 API 文件

- 新增新端點的說明
- 修正回應格式範例
- 更新錯誤代碼說明

### 重構
refactor(user): 重構使用者服務層邏輯

將使用者相關邏輯從控制器移至服務層，提高程式碼的可維護性和可測試性

### 破壞性變更
feat(api)!: 更新使用者 API 回應格式

BREAKING CHANGE: 使用者 API 的回應格式已改變，
請更新客戶端程式碼以配合新的格式
```

### 7.3 Pull Request 規範

#### PR 標題格式

```text
[<類型>] <簡短描述> (<票號>)

範例：
[Feature] 新增使用者二步驗證 (#123)
[Bugfix] 修復登入逾時問題 (#456)
[Hotfix] 修復支付安全漏洞 (#789)
```

#### PR 描述模板

```markdown
## 📋 變更摘要
<!-- 簡述這個 PR 的目的和主要變更 -->

## 🎯 相關 Issue
<!-- 例如：Closes #123, Fixes #456, Related to #789 -->

## 🔧 變更內容
<!-- 詳細列出所有變更 -->
- [ ] 新增功能 A
- [ ] 修改功能 B
- [ ] 移除功能 C
- [ ] 更新文件 D

## 🧪 測試
<!-- 說明如何測試這些變更 -->
- [ ] 單元測試已通過
- [ ] 整合測試已通過
- [ ] 手動測試已完成
- [ ] 效能測試已通過（如適用）

## 📱 截圖/影片
<!-- 如果是 UI 變更，請附上截圖或影片 -->

## ⚠️ 注意事項
<!-- 任何需要特別注意的事項 -->
- [ ] 需要資料庫遷移
- [ ] 需要環境變數配置
- [ ] 有破壞性變更
- [ ] 需要更新部署流程

## ✅ 檢查清單
- [ ] 程式碼符合專案編碼規範
- [ ] 已新增或更新相關測試
- [ ] 已更新相關文件
- [ ] 已通過所有 CI 檢查
- [ ] 已自我審查程式碼
```

### 7.4 Code Review 標準

#### 審查者檢查清單

#### 功能性檢查

- [ ] 程式碼邏輯正確
- [ ] 測試覆蓋率充足
- [ ] 錯誤處理適當
- [ ] 邊界條件考慮周全

#### 程式碼品質

- [ ] 命名清楚有意義
- [ ] 函數長度適中
- [ ] 重複程式碼已抽取
- [ ] 註解清楚有用

#### 安全性檢查

- [ ] 輸入驗證充分
- [ ] 沒有硬編碼敏感資訊
- [ ] 權限控制正確
- [ ] SQL 注入防護

#### 效能考量

- [ ] 沒有明顯效能問題
- [ ] 資料庫查詢優化
- [ ] 記憶體使用合理
- [ ] 非同步處理適當

#### 回饋規範

```markdown
### ✅ 良好的回饋範例

## 💡 建議
這個方法有點長，建議拆分為更小的函數提高可讀性：
```java

// 建議拆分
public void processUser(User user) {
    validateUser(user);
    saveUser(user);
    sendNotification(user);
}

```text

## ⚠️ 問題
這裡可能會有 NPE 的風險，建議加上 null 檢查：
```java

if (user != null && user.getEmail() != null) {
    // 處理邏輯
}

```text

## 🔒 安全性
這個 SQL 查詢容易受到 SQL 注入攻擊，請使用 PreparedStatement

### ❌ 避免的回饋方式
- "這段程式碼不好"
- "重寫"
- "錯誤"
```

### 7.5 分支保護規則

#### main 分支保護

```text
強制規則：
✅ 需要 Pull Request 才能合併
✅ 需要至少 2 位審查者同意
✅ 所有 CI 檢查必須通過
✅ 分支必須是最新版本
✅ 管理員也需要遵循規則

禁止操作：
❌ 直接推送到 main
❌ 強制推送
❌ 刪除分支
```

#### CI/CD 整合

```yaml
### .github/workflows/ci.yml 範例
name: CI

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up JDK 17
      uses: actions/setup-java@v3
      with:
        java-version: '17'
        distribution: 'temurin'
    - name: Run tests
      run: mvn test
    - name: Check code style
      run: mvn checkstyle:check
```

---

## 8. GitHub 進階功能與協作工具

### 8.1 Issue 管理

#### 什麼是 Issue？

Issue 是 GitHub 的任務追蹤系統，用於：

- 報告 Bug 和問題
- 請求新功能
- 討論改善建議
- 指派任務給團隊成員

#### 建立 Issue

```markdown
### Issue 範本
#### 問題描述
清楚描述遇到的問題或需求

#### 重現步驟
1. 進入登入頁面
2. 輸入錯誤密碼
3. 點選登入按鈕
4. 看到錯誤訊息

#### 預期結果
應該顯示清楚的錯誤訊息

#### 實際結果
顯示不明確的錯誤

#### 環境資訊
- 瀏覽器：Chrome 117
- 作業系統：Windows 11
- 版本：v2.1.0

#### 附加資訊
- [ ] 這是安全性相關問題
- [ ] 這會影響所有使用者
- [ ] 已檢查是否為重複問題
```

#### Issue 標籤系統

```text
標籤分類：

🐛 bug - 錯誤回報
✨ enhancement - 功能增強
📝 documentation - 文件相關
❓ question - 問題詢問
🚀 feature - 新功能
🔧 maintenance - 維護工作
🔒 security - 安全性問題
⚡ performance - 效能改善
🎨 ui/ux - 使用者介面
🧪 testing - 測試相關

優先度：
🔴 high priority - 高優先度
🟡 medium priority - 中優先度
🟢 low priority - 低優先度

狀態：
🚧 in progress - 進行中
👀 needs review - 需要審查
✅ ready - 準備就緒
❌ won't fix - 不予修復
```

#### Issue 指派與里程碑

```bash
### GitHub CLI 操作 Issues
gh issue create --title "修復登入錯誤" --body "詳細描述..." --label bug,high-priority

gh issue list --state open --assignee @me

gh issue view 123

gh issue close 123

gh issue reopen 123
```

### 8.2 Project 專案管理

#### GitHub Projects 介紹

GitHub Projects 提供看板式專案管理：

- **看板視圖**: 類似 Kanban 的工作流程管理
- **表格視圖**: 類似試算表的資料檢視
- **時程視圖**: 甘特圖式的時程規劃

#### 建立專案看板

```text
標準欄位設定：

📋 Backlog (待辦事項)
- 新建立的 Issues
- 尚未開始的任務

🚧 In Progress (進行中)
- 正在開發的功能
- 指派給開發者的任務

👀 Review (審查中)
- 等待 Code Review 的 PR
- 需要測試的功能

✅ Done (完成)
- 已合併的 PR
- 已解決的 Issues

🚀 Released (已發布)
- 已部署到生產環境的功能
```

#### 自動化工作流程

```yaml
### 專案自動化範例
name: 專案看板自動化

on:
  issues:
    types: [opened, closed]
  pull_request:
    types: [opened, closed, merged]

jobs:
  update-project:
    runs-on: ubuntu-latest
    steps:
    - name: 移動 Issue 到進行中
      if: github.event.action == 'opened'
      uses: alex-page/github-project-automation-plus@v0.8.1
      with:
        project: 專案開發看板
        column: In Progress
        repo-token: ${{ secrets.GITHUB_TOKEN }}
```

### 8.3 Wiki 文件系統

#### 設定專案 Wiki

Wiki 是專案的知識庫，用於：

- API 文件
- 開發指南
- 部署說明
- 常見問題 FAQ

#### Wiki 頁面結構

```markdown
### 專案 Wiki 首頁

## 📚 文件導航

### 開發相關
- [開發環境設定](開發環境設定)
- [程式碼風格指南](程式碼風格指南)
- [API 文件](API-文件)

### 部署運維
- [部署指南](部署指南)
- [監控設定](監控設定)
- [故障排除](故障排除)

### 專案管理
- [發布流程](發布流程)
- [會議記錄](會議記錄)
- [決策紀錄](決策紀錄)

## 🔗 外部連結
- [線上 Demo](https://demo.example.com)
- [API 文件](https://api.example.com/docs)
- [監控面板](https://monitoring.example.com)
```

#### Wiki 最佳實務

```markdown
### Wiki 撰寫指南

## 結構化內容
- 使用清楚的標題階層
- 提供目錄導航
- 加入相關連結

## 保持更新
- 定期檢查內容正確性
- 版本發布時更新文件
- 移除過時資訊

## 協作編輯
- 使用 Markdown 格式
- 提供編輯歷史
- 鼓勵團隊貢獻
```

### 8.4 Releases 版本發布

#### 語義化版本管理

```text
版本號格式：主版本.次版本.修補版本

範例：v2.1.3

主版本 (Major)：不相容的 API 變更
次版本 (Minor)：向下相容的功能新增
修補版本 (Patch)：向下相容的問題修正

標籤範例：
v1.0.0 - 第一個穩定版本
v1.1.0 - 新增功能
v1.1.1 - 錯誤修復
v2.0.0 - 重大更新
```

#### 建立 Release

```bash
### 建立標籤
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0

### 使用 GitHub CLI
gh release create v1.2.0 \
  --title "版本 1.2.0" \
  --notes "
## 🚀 新功能
- 新增使用者頭像上傳功能
- 新增批次匯出功能

## 🐛 錯誤修復
- 修復登入逾時問題
- 修復檔案上傳大小限制

## 🔧 改善項目
- 提升搜尋效能
- 優化使用者介面

## 📋 完整變更紀錄
查看所有變更：[v1.1.0...v1.2.0](https://github.com/owner/repo/compare/v1.1.0...v1.2.0)
" \
  --draft
```

#### Release Notes 最佳實務

```markdown
### Release Notes 範本

## 版本 v2.1.0 (2025-08-28)

### 🚀 新功能 (Features)
- **使用者管理**: 新增批次使用者匯入功能 (#123)
- **報表系統**: 新增自訂報表產生器 (#124)

### 🐛 錯誤修復 (Bug Fixes)
- **登入系統**: 修復 OAuth 登入逾時問題 (#125)
- **檔案上傳**: 修復大檔案上傳失敗問題 (#126)

### 🔧 改善項目 (Improvements)
- **效能優化**: 資料庫查詢效能提升 30% (#127)
- **使用者體驗**: 簡化設定流程 (#128)

### 💥 重大變更 (Breaking Changes)
- **API**: 移除 v1 API 支援，請升級到 v2 API
- **設定格式**: 配置檔案格式已更新，請參考遷移指南

### 📚 文件更新
- 更新 API 文件
- 新增部署指南
- 更新故障排除手冊

### 🔗 相關連結
- [完整變更清單](https://github.com/owner/repo/compare/v2.0.0...v2.1.0)
- [遷移指南](https://github.com/owner/repo/wiki/Migration-Guide-v2.1)
- [已知問題](https://github.com/owner/repo/issues?q=is%3Aissue+is%3Aopen+label%3A%22known+issue%22)

### 👥 貢獻者
感謝以下貢獻者的參與：
- @developer1 - 新功能開發
- @developer2 - 錯誤修復
- @tester1 - 測試與品質保證
```

### 8.5 Discussions 社群討論

#### 啟用 Discussions

Discussions 提供社群互動平台：

- 功能建議討論
- 技術問題問答
- 公告與更新
- 社群互動交流

#### 討論分類設定

```text
分類架構：

💡 Ideas (想法建議)
- 新功能建議
- 改善提案
- 創新想法

❓ Q&A (問題解答)
- 技術問題
- 使用疑問
- 最佳實務詢問

📢 Announcements (公告)
- 版本發布
- 重要更新
- 政策變更

🗣️ General (一般討論)
- 經驗分享
- 社群交流
- 其他話題
```

### 8.6 Security 安全功能

#### Security Advisories

```markdown
### 安全性公告管理

## 建立安全性公告
1. Repository → Security → Advisories
2. 填寫漏洞詳細資訊
3. 評估嚴重程度 (CVSS)
4. 設定修復時程
5. 通知相關使用者

## 私人漏洞回報
- 提供安全回報管道
- 協調負責任的漏洞披露
- 管理修復流程
```

#### Dependabot 依賴更新

```yaml
### .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "maven"
    directory: "/"
    schedule:
      interval: "weekly"
    assignees:
      - "security-team"
    reviewers:
      - "lead-developer"
    commit-message:
      prefix: "deps:"
      include: "scope"
```

#### 程式碼掃描設定

```yaml
### .github/workflows/codeql.yml
name: "CodeQL 安全掃描"

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '30 1 * * 1'

jobs:
  analyze:
    name: 分析程式碼
    runs-on: ubuntu-latest
    
    strategy:
      fail-fast: false
      matrix:
        language: [ 'java' ]
        
    steps:
    - name: 檢出程式碼
      uses: actions/checkout@v4
      
    - name: 初始化 CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}
        
    - name: 自動建構
      uses: github/codeql-action/autobuild@v3
      
    - name: 執行 CodeQL 分析
      uses: github/codeql-action/analyze@v3
```

### 8.7 GitHub CLI 進階應用

#### 批次操作範例

```bash
### 批次管理 Issues
gh issue list --state open --json number,title | \
  jq '.[] | select(.title | contains("bug")) | .number' | \
  xargs -I {} gh issue edit {} --add-label "priority:high"

### 批次管理 PR
gh pr list --state open --author "@me" --json number | \
  jq '.[].number' | \
  xargs -I {} gh pr merge {} --squash

### 專案統計
gh issue list --state all --json state | \
  jq 'group_by(.state) | map({state: .[0].state, count: length})'
```

### 8.8 GitHub Apps 與整合

#### 推薦的 GitHub Apps

```text
開發工具：
- SonarCloud - 程式碼品質分析
- Codecov - 測試覆蓋率
- Snyk - 安全漏洞掃描

專案管理：
- ZenHub - 進階專案管理
- Linear - 現代化問題追蹤
- Jira - 企業專案管理

通訊協作：
- Slack - 團隊通訊整合
- Microsoft Teams - 企業協作
- Discord - 社群互動

部署監控：
- Vercel - 前端部署
- Heroku - 應用程式託管
- DataDog - 應用程式監控
```

### 📝 GitHub 功能使用建議

#### 小型團隊 (2-5人)

- ✅ 使用 Issues 追蹤任務
- ✅ 簡單的 Project 看板
- ✅ Wiki 基本文件
- ✅ 定期 Releases

#### 中型團隊 (6-20人)

- ✅ 完整的 Issue 標籤系統
- ✅ 進階 Project 自動化
- ✅ Discussions 社群互動
- ✅ 安全性掃描工具

#### 大型團隊 (20人以上)

- ✅ 企業級專案管理
- ✅ 安全性公告管理
- ✅ 完整的 CI/CD 流程
- ✅ 第三方工具整合

### 8.9 GitHub Copilot 整合

#### GitHub Copilot 概述

GitHub Copilot 是由 GitHub 和 OpenAI 開發的 AI 程式碼助手，可以：

- 自動完成程式碼片段
- 生成單元測試
- 解釋程式碼功能
- 協助除錯和重構

#### 安裝和設定

```bash
### VS Code 擴充套件安裝
### 1. 開啟 VS Code
### 2. 安裝 "GitHub Copilot" 擴充套件
### 3. 登入 GitHub 帳號

### 檢查 Copilot 狀態
### Ctrl+Shift+P -> "GitHub Copilot: Show Output"

```

#### 基本使用技巧

```javascript
// 範例：Copilot 協助生成函數
// 輸入註解，Copilot 會建議實作
// Calculate the area of a circle given radius
function calculateCircleArea(radius) {
    // Copilot 會自動建議: return Math.PI * radius * radius;
}

// 生成測試案例
// 輸入: Write test for calculateCircleArea
// Copilot 會建議完整的測試程式碼
```

#### 最佳實務

```markdown
✅ **有效使用 Copilot**

1. **清楚的註解**: 詳細描述功能需求
2. **良好的命名**: 使用有意義的變數和函數名稱
3. **上下文提供**: 在相關程式碼附近工作
4. **審查建議**: 不要盲目接受所有建議

❌ **避免事項**

1. 不要完全依賴 Copilot
2. 不要跳過程式碼審查
3. 不要忽略安全性考量
4. 不要忘記測試生成的程式碼
```

#### 團隊使用規範

```yaml
### Copilot 使用指南
copilot_usage:
  review_required: true
  security_check: mandatory
  documentation: required
  testing: comprehensive

### 檔案類型限制
file_restrictions:
  - no_secrets: ["*.env", "*.key", "*.pem"]
  - review_needed: ["Dockerfile", "docker-compose.yml"]
  - careful_with: ["*.sql", "*.sh", "*.ps1"]
```

---

## 9. CI/CD 持續整合與部署

### 9.1 CI/CD 基礎概念

#### 什麼是 CI/CD？

#### 持續整合 (Continuous Integration, CI)

- 開發者頻繁將程式碼整合到主分支
- 每次整合都會觸發自動化測試
- 快速發現和修復整合問題

#### 持續部署 (Continuous Deployment, CD)

- 自動將通過測試的程式碼部署到生產環境
- 減少人為錯誤和部署時間
- 提高軟體交付速度

#### GitHub Actions 簡介

GitHub Actions 是 GitHub 提供的 CI/CD 平台：

- 基於事件驅動的工作流程
- 支援多種作業系統和語言
- 豐富的社群 Actions 生態系統
- 與 GitHub 深度整合

### 9.2 工作流程設定

#### 基本目錄結構

```text
.github/
└── workflows/
    ├── ci.yml          # 持續整合
    ├── cd.yml          # 持續部署
    ├── security.yml    # 安全檢查
    └── docs.yml        # 文件生成
```

#### 基本 CI 工作流程

```yaml
### .github/workflows/ci.yml
name: Continuous Integration

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: 測試與品質檢查
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        java-version: [17, 21]
    
    steps:
    - name: 檢出程式碼
      uses: actions/checkout@v4
      
    - name: 設定 Java ${{ matrix.java-version }}
      uses: actions/setup-java@v4
      with:
        java-version: ${{ matrix.java-version }}
        distribution: 'temurin'
        
    - name: 快取 Maven 依賴
      uses: actions/cache@v4
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        restore-keys: ${{ runner.os }}-m2
        
    - name: 執行測試
      run: mvn clean test
      
    - name: 生成測試報告
      uses: dorny/test-reporter@v1
      if: success() || failure()
      with:
        name: Maven Tests
        path: target/surefire-reports/*.xml
        reporter: java-junit
        
    - name: 程式碼覆蓋率
      run: mvn jacoco:report
      
    - name: 上傳覆蓋率到 Codecov
      uses: codecov/codecov-action@v3
      with:
        file: target/site/jacoco/jacoco.xml
        
  code-quality:
    name: 程式碼品質檢查
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
      
    - name: 設定 Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: 執行 Checkstyle
      run: mvn checkstyle:check
      
    - name: 執行 SpotBugs
      run: mvn spotbugs:check
      
    - name: SonarQube 分析
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      run: mvn sonar:sonar
```

### 9.3 進階 CI 配置

#### 多環境測試

```yaml
### .github/workflows/multi-env.yml
name: 多環境測試

on:
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: ${{ matrix.os }} - Java ${{ matrix.java }}
    runs-on: ${{ matrix.os }}
    
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        java: [17, 21]
        
    steps:
    - uses: actions/checkout@v4
    
    - name: 設定 Java ${{ matrix.java }}
      uses: actions/setup-java@v4
      with:
        java-version: ${{ matrix.java }}
        distribution: 'temurin'
        
    - name: 執行測試
      run: mvn clean test
      
    - name: 整合測試
      run: mvn verify -P integration-tests
```

#### 安全檢查工作流程

```yaml
### .github/workflows/security.yml
name: 安全檢查

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 6 * * 1'  # 每週一早上6點執行

jobs:
  security:
    name: 安全漏洞掃描
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: 設定 Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: OWASP 依賴檢查
      run: mvn org.owasp:dependency-check-maven:check
      
    - name: 上傳安全報告
      uses: actions/upload-artifact@v4
      if: always()
      with:
        name: security-reports
        path: target/dependency-check-report.html
        
    - name: CodeQL 分析
      uses: github/codeql-action/init@v3
      with:
        languages: java
        
    - name: 自動建構
      uses: github/codeql-action/autobuild@v3
      
    - name: 執行 CodeQL 分析
      uses: github/codeql-action/analyze@v3
```

### 9.4 持續部署 (CD)

#### 部署到測試環境

```yaml
### .github/workflows/deploy-staging.yml
name: 部署到測試環境

on:
  push:
    branches: [ develop ]

jobs:
  deploy:
    name: 部署測試環境
    runs-on: ubuntu-latest
    environment: staging
    
    steps:
    - uses: actions/checkout@v4
    
    - name: 設定 Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: 建構應用程式
      run: mvn clean package -DskipTests
      
    - name: 建構 Docker 映像
      run: |
        docker build -t ${{ vars.DOCKER_REGISTRY }}/app:staging-${{ github.sha }} .
        docker build -t ${{ vars.DOCKER_REGISTRY }}/app:staging-latest .
        
    - name: 登入 Docker Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ vars.DOCKER_REGISTRY }}
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
        
    - name: 推送 Docker 映像
      run: |
        docker push ${{ vars.DOCKER_REGISTRY }}/app:staging-${{ github.sha }}
        docker push ${{ vars.DOCKER_REGISTRY }}/app:staging-latest
        
    - name: 部署到 Kubernetes
      uses: azure/k8s-deploy@v1
      with:
        manifests: |
          k8s/staging/deployment.yaml
          k8s/staging/service.yaml
        images: ${{ vars.DOCKER_REGISTRY }}/app:staging-${{ github.sha }}
        kubeconfig: ${{ secrets.KUBE_CONFIG_STAGING }}
```

#### 生產環境部署

```yaml
### .github/workflows/deploy-production.yml
name: 部署到生產環境

on:
  release:
    types: [published]

jobs:
  deploy:
    name: 生產環境部署
    runs-on: ubuntu-latest
    environment: production
    
    steps:
    - uses: actions/checkout@v4
    
    - name: 設定 Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: 執行完整測試
      run: mvn clean verify
      
    - name: 建構應用程式
      run: mvn clean package -DskipTests
      
    - name: 建構 Docker 映像
      run: |
        docker build -t ${{ vars.DOCKER_REGISTRY }}/app:${{ github.ref_name }} .
        docker build -t ${{ vars.DOCKER_REGISTRY }}/app:latest .
        
    - name: 安全掃描映像
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: ${{ vars.DOCKER_REGISTRY }}/app:${{ github.ref_name }}
        format: 'sarif'
        output: 'trivy-results.sarif'
        
    - name: 上傳安全掃描結果
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: 'trivy-results.sarif'
        
    - name: 登入 Docker Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ vars.DOCKER_REGISTRY }}
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
        
    - name: 推送 Docker 映像
      run: |
        docker push ${{ vars.DOCKER_REGISTRY }}/app:${{ github.ref_name }}
        docker push ${{ vars.DOCKER_REGISTRY }}/app:latest
        
    - name: 藍綠部署
      uses: azure/k8s-deploy@v1
      with:
        strategy: blue-green
        manifests: |
          k8s/production/deployment.yaml
          k8s/production/service.yaml
        images: ${{ vars.DOCKER_REGISTRY }}/app:${{ github.ref_name }}
        kubeconfig: ${{ secrets.KUBE_CONFIG_PRODUCTION }}
        
    - name: 健康檢查
      run: |
        sleep 30
        curl -f ${{ vars.PRODUCTION_URL }}/health || exit 1
        
    - name: 通知部署結果
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        channel: '#deployments'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### 9.5 分支保護與自動化

#### 分支保護規則設定

```yaml
### 透過 GitHub API 或 Web 介面設定
分支保護規則 (main):
✅ 需要 Pull Request 才能合併
✅ 需要狀態檢查通過:
   - ci / test (ubuntu-latest, 17)
   - ci / test (ubuntu-latest, 21)
   - ci / code-quality
   - security / security
✅ 需要分支為最新版本
✅ 需要管理員審查
✅ 限制推送權限
```

#### 自動合併設定

```yaml
### .github/workflows/auto-merge.yml
name: 自動合併

on:
  pull_request:
    types: [labeled, unlabeled, synchronize, opened, edited, ready_for_review, reopened]

jobs:
  auto-merge:
    name: 自動合併 Dependabot PR
    runs-on: ubuntu-latest
    if: ${{ github.actor == 'dependabot[bot]' }}
    
    steps:
    - name: 自動核准 Dependabot PR
      uses: hmarr/auto-approve-action@v3
      with:
        github-token: ${{ secrets.GITHUB_TOKEN }}
        
    - name: 啟用自動合併
      uses: peter-evans/enable-pull-request-automerge@v3
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        pull-request-number: ${{ github.event.pull_request.number }}
        merge-method: squash
```

### 9.6 監控與通知

#### 部署監控

```yaml
### .github/workflows/monitor.yml
name: 生產監控

on:
  schedule:
    - cron: '*/5 * * * *'  # 每5分鐘檢查一次

jobs:
  health-check:
    name: 健康檢查
    runs-on: ubuntu-latest
    
    steps:
    - name: 檢查應用程式健康狀態
      run: |
        response=$(curl -s -o /dev/null -w "%{http_code}" ${{ vars.PRODUCTION_URL }}/health)
        if [ $response -ne 200 ]; then
          echo "健康檢查失敗: HTTP $response"
          exit 1
        fi
        
    - name: 檢查資料庫連線
      run: |
        response=$(curl -s -o /dev/null -w "%{http_code}" ${{ vars.PRODUCTION_URL }}/health/db)
        if [ $response -ne 200 ]; then
          echo "資料庫檢查失敗: HTTP $response"
          exit 1
        fi
        
    - name: 失敗通知
      if: failure()
      uses: 8398a7/action-slack@v3
      with:
        status: failure
        channel: '#alerts'
        text: '🚨 生產環境健康檢查失敗！'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

#### 效能監控

```yaml
### .github/workflows/performance.yml
name: 效能測試

on:
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * 1'  # 每週一凌晨2點

jobs:
  performance:
    name: 效能基準測試
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: 設定 Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        
    - name: 建構應用程式
      run: mvn clean package -DskipTests
      
    - name: 啟動應用程式
      run: |
        java -jar target/app.jar &
        sleep 30
        
    - name: JMeter 效能測試
      uses: rbhadti94/apache-jmeter-action@v0.5.0
      with:
        testFilePath: performance-tests/load-test.jmx
        outputReportsFolder: reports/
        
    - name: 上傳效能報告
      uses: actions/upload-artifact@v4
      with:
        name: performance-reports
        path: reports/
        
    - name: 效能回歸檢查
      run: |
        python scripts/performance-regression-check.py \
          --current reports/results.jtl \
          --baseline performance-baseline.json \
          --threshold 10
```

### 9.7 Secrets 與環境變數管理

#### Secrets 設定指南

```text
Repository Secrets (Settings → Secrets and variables → Actions):

🔑 必要 Secrets:
- DOCKER_USERNAME: Docker Registry 使用者名稱
- DOCKER_PASSWORD: Docker Registry 密碼
- SONAR_TOKEN: SonarQube 存取權杖
- SLACK_WEBHOOK: Slack 通知 Webhook URL
- KUBE_CONFIG_STAGING: 測試環境 Kubernetes 配置
- KUBE_CONFIG_PRODUCTION: 生產環境 Kubernetes 配置

🌍 環境變數:
- DOCKER_REGISTRY: Docker Registry 位址
- PRODUCTION_URL: 生產環境 URL
- STAGING_URL: 測試環境 URL
```

#### 環境特定設定

```yaml
### 環境設定範例
environments:
  staging:
    url: <https://staging.yourapp.com>
    secrets:
      - DATABASE_URL
      - API_KEY
    protection_rules:
      required_reviewers: 1
      
  production:
    url: <https://yourapp.com>
    secrets:
      - DATABASE_URL
      - API_KEY
      - SSL_CERT
    protection_rules:
      required_reviewers: 2
      deployment_branch_policy:
        protected_branches: true
```

### 9.8 最佳實務與注意事項

#### CI/CD 最佳實務

#### ✅ 建議做法

1. **快速回饋**

   ```yaml
   # 優化建構時間
   - name: 快取依賴
     uses: actions/cache@v4
     with:
       path: ~/.m2
       key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
   ```

2. **失敗快速**

   ```yaml
   strategy:
     fail-fast: true  # 任一工作失敗時立即停止
   ```

3. **並行執行**

   ```yaml
   jobs:
     test:
       # 獨立執行
     security:
       # 同時執行
     build:
       needs: [test, security]  # 等待前置工作完成
   ```

#### ❌ 避免做法

- 不要在 CI 中執行長時間運行的任務
- 不要忽略失敗的測試
- 不要在公開倉庫中暴露機密資訊
- 不要跳過程式碼審查流程

#### 安全性考量

```yaml
### 權限最小化原則
permissions:
  contents: read
  packages: write
  security-events: write

### 使用 GITHUB_TOKEN 而非個人存取權杖
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

### 固定 Action 版本
uses: actions/checkout@v4  # ✅ 具體版本
uses: actions/checkout@main  # ❌ 避免使用分支
```

#### 成本控制

```yaml
### 條件執行以節省資源
jobs:
  expensive-job:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    
  # 限制並行執行數量
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true
```

### 📝 CI/CD 實施檢查清單

#### 設定階段

- [ ] 建立 `.github/workflows/` 目錄
- [ ] 設定基本 CI 工作流程
- [ ] 配置必要的 Secrets
- [ ] 設定分支保護規則
- [ ] 整合程式碼品質工具

#### 測試階段

- [ ] 多版本 Java 測試
- [ ] 跨平台相容性測試
- [ ] 安全漏洞掃描
- [ ] 效能基準測試
- [ ] 整合測試自動化

#### 部署階段

- [ ] 測試環境自動部署
- [ ] 生產環境審查機制
- [ ] 回滾機制設定
- [ ] 健康檢查自動化
- [ ] 監控與告警設定

---

## 10. 安全最佳實務

### 10.1 認證與授權

#### SSH 金鑰管理

```bash
### 生成強度更高的 SSH 金鑰
ssh-keygen -t ed25519 -a 100 -C "your.email@example.com"

### 設定 SSH 金鑰密碼
ssh-keygen -p -f ~/.ssh/id_ed25519

### 限制 SSH 金鑰的使用範圍
### 在 GitHub 設定中選擇 "Restrict to specific repositories"
```

#### Personal Access Token 管理

```bash
### Token 最佳實務
✅ 設定最小權限範圍
✅ 設定 Token 有效期限
✅ 定期輪換 Token
✅ 使用環境變數存儲 Token
✅ 不要將 Token 提交到程式碼庫

### 環境變數設定
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"

### Git 設定使用 Token
git config --global credential.helper store
```

#### 雙因素驗證 (2FA)

```markdown
🔒 **啟用 2FA 步驟**

1. GitHub → Settings → Password and authentication
2. 選擇 "Enable two-factor authentication"
3. 使用 Authenticator App (推薦) 或 SMS
4. 儲存備用恢復碼

⚠️ **注意事項**
- 啟用 2FA 後，Git 操作需使用 Personal Access Token
- 妥善保管恢復碼
- 定期檢查授權的應用程式
```

### 10.2 機密資訊管理

#### .gitignore 設定

```gitignore
# 機密檔案
*.key
*.pem
*.p12
*.pfx
.env
.env.local
.env.*.local

# 配置檔案
config/secrets.yml
config/database.yml
application-prod.properties

# IDE 設定
.vscode/settings.json
.idea/

# OS 檔案
.DS_Store
Thumbs.db

# 日誌檔案
*.log
logs/

# 依賴套件
node_modules/
target/
build/
```

#### Git-secrets 工具

```bash
### 安裝 git-secrets
# macOS
brew install git-secrets

# Windows (使用 Git Bash)
git clone https://github.com/awslabs/git-secrets.git
cd git-secrets
make install

### 設定 git-secrets
git secrets --install
git secrets --register-aws

### 掃描現有儲存庫
git secrets --scan
git secrets --scan-history

### 自訂規則
git secrets --add 'password\s*=\s*.+'
git secrets --add 'api[_-]?key\s*=\s*.+'
```

#### 環境變數管理

```bash
### .env 檔案範本
# .env.example
DATABASE_URL=postgresql://localhost:5432/dbname
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
SMTP_PASSWORD=your_smtp_password

### 使用 direnv 管理環境變數
# 安裝 direnv
brew install direnv

# 在 .envrc 中設定
export DATABASE_URL="postgresql://..."
export API_KEY="..."

# 啟用 direnv
direnv allow
```

#### Secrets 掃描工具

```bash
### 使用 truffleHog 掃描
pip install truffleHog
trufflehog --regex --entropy=True <repository-url>

### 使用 GitGuardian
curl -sSL https://api.gitguardian.com/v1/scan | bash

### 使用 detect-secrets
pip install detect-secrets
detect-secrets scan > .secrets.baseline
detect-secrets audit .secrets.baseline
```

### 10.3 程式碼安全掃描

#### CodeQL 設定

```yaml
### .github/workflows/codeql.yml
name: "CodeQL 安全分析"

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '30 1 * * 1'

jobs:
  analyze:
    name: 分析程式碼
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'java', 'javascript' ]

    steps:
    - name: 檢出程式碼
      uses: actions/checkout@v4

    - name: 初始化 CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}
        queries: security-and-quality

    - name: 自動建構
      uses: github/codeql-action/autobuild@v3

    - name: 執行 CodeQL 分析
      uses: github/codeql-action/analyze@v3
      with:
        category: "/language:${{matrix.language}}"
```

#### SonarQube 整合

```yaml
### sonar-project.properties
sonar.projectKey=your-project-key
sonar.organization=your-organization
sonar.sources=src
sonar.tests=src/test
sonar.java.binaries=target/classes
sonar.coverage.jacoco.xmlReportPaths=target/site/jacoco/jacoco.xml

### .github/workflows/sonar.yml
name: SonarQube 分析

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  sonarqube:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: 設定 Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'

    - name: 快取 SonarQube 套件
      uses: actions/cache@v4
      with:
        path: ~/.sonar/cache
        key: ${{ runner.os }}-sonar

    - name: 執行測試和分析
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      run: mvn clean verify sonar:sonar
```

#### SAST 工具整合

```yaml
### 多種靜態分析工具
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    # SpotBugs
    - name: SpotBugs 分析
      run: mvn spotbugs:check

    # PMD
    - name: PMD 分析
      run: mvn pmd:check

    # Checkstyle
    - name: Checkstyle 檢查
      run: mvn checkstyle:check

    # OWASP Dependency Check
    - name: OWASP 依賴檢查
      run: mvn org.owasp:dependency-check-maven:check
```

### 10.4 依賴套件安全

#### Dependabot 設定

```yaml
### .github/dependabot.yml
version: 2
updates:
  # Maven 依賴更新
  - package-ecosystem: "maven"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
    open-pull-requests-limit: 10
    assignees:
      - "security-team"
    reviewers:
      - "lead-developer"
    commit-message:
      prefix: "deps"
      prefix-development: "deps(dev)"
      include: "scope"
    labels:
      - "dependencies"
      - "automated"

  # npm 依賴更新
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    versioning-strategy: increase

  # Docker 基礎映像更新
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

#### 依賴套件審計

```bash
### Maven 依賴安全檢查
mvn dependency:tree
mvn versions:display-dependency-updates
mvn org.owasp:dependency-check-maven:check

### npm 依賴安全檢查
npm audit
npm audit fix
npm audit fix --force

### 檢視漏洞詳情
npm audit --json
mvn dependency-check:check -Dformat=JSON
```

#### Snyk 整合

```yaml
### .github/workflows/snyk.yml
name: Snyk 安全掃描

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  snyk:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: 執行 Snyk 測試
      uses: snyk/actions/maven@master
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      with:
        args: --severity-threshold=high

    - name: 上傳結果到 GitHub
      uses: github/codeql-action/upload-sarif@v3
      if: always()
      with:
        sarif_file: snyk.sarif
```

### 10.5 分支保護規則

#### 完整分支保護設定

```yaml
### main 分支保護規則
branch_protection:
  required_pull_request_reviews:
    required_approving_review_count: 2
    dismiss_stale_reviews: true
    require_code_owner_reviews: true
    require_last_push_approval: true
    
  required_status_checks:
    strict: true
    contexts:
      - "ci / test (ubuntu-latest, 17)"
      - "ci / code-quality"
      - "security / codeql"
      - "security / dependency-check"
      
  enforce_admins: true
  required_linear_history: true
  allow_force_pushes: false
  allow_deletions: false
  required_conversation_resolution: true
  
  restrictions:
    users: []
    teams:
      - "core-team"
      - "senior-developers"
```

#### CODEOWNERS 設定

```text
### .github/CODEOWNERS
# 預設所有檔案的擁有者
*       @organization/core-team

# 特定目錄的擁有者
/src/main/java/security/    @organization/security-team
/src/main/resources/db/     @organization/database-team
/.github/workflows/         @organization/devops-team

# 特定檔案類型
*.sql                       @organization/database-team
Dockerfile                  @organization/devops-team
*.yml                       @organization/devops-team

# 文件維護
/docs/                      @organization/tech-writers
README.md                   @organization/product-team
```

#### 保護規則自動化

```yaml
### .github/workflows/branch-protection.yml
name: 檢查分支保護

on:
  pull_request:
    branches: [ main ]

jobs:
  check-protection:
    runs-on: ubuntu-latest
    steps:
    - name: 檢查 PR 標題格式
      uses: deepakputhraya/action-pr-title@master
      with:
        regex: '^\[.+\] .+'
        allowed_prefixes: 'Feature,Bugfix,Hotfix,Docs,Refactor'

    - name: 檢查 PR 描述
      uses: juliangruber/pr-body-check-action@v1
      with:
        contains: '## 📋 變更摘要'

    - name: 標籤檢查
      uses: mheap/github-action-required-labels@v2
      with:
        mode: exactly
        count: 1
        labels: "bug, enhancement, documentation"
```

### 10.6 審計與監控

#### 審計日誌收集

```yaml
### .github/workflows/audit.yml
name: 審計日誌

on:
  push:
    branches: [ main ]
  pull_request:
    types: [ opened, closed, merged ]
  workflow_dispatch:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
    - name: 記錄事件
      run: |
        echo "事件類型: ${{ github.event_name }}"
        echo "使用者: ${{ github.actor }}"
        echo "分支: ${{ github.ref }}"
        echo "提交: ${{ github.sha }}"
        echo "時間: $(date -u +"%Y-%m-%d %H:%M:%S UTC")"

    - name: 發送到日誌系統
      uses: fjogeleit/http-request-action@v1
      with:
        url: ${{ secrets.AUDIT_LOG_ENDPOINT }}
        method: 'POST'
        data: |
          {
            "event": "${{ github.event_name }}",
            "actor": "${{ github.actor }}",
            "repository": "${{ github.repository }}",
            "ref": "${{ github.ref }}",
            "sha": "${{ github.sha }}",
            "timestamp": "${{ github.event.head_commit.timestamp }}"
          }
```

#### 安全事件監控

```yaml
### .github/workflows/security-monitoring.yml
name: 安全監控

on:
  schedule:
    - cron: '0 */6 * * *'  # 每 6 小時執行一次

jobs:
  security-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: 檢查異常提交
      run: |
        git log --since="6 hours ago" --pretty=format:"%h - %an: %s" > recent_commits.txt
        
    - name: 檢查大型檔案
      run: |
        find . -type f -size +10M > large_files.txt
        
    - name: 檢查敏感關鍵字
      run: |
        grep -r "password\|secret\|api_key" --include="*.java" --include="*.properties" . || true
        
    - name: 生成安全報告
      if: always()
      run: |
        echo "# 安全檢查報告" > security_report.md
        echo "## 最近提交" >> security_report.md
        cat recent_commits.txt >> security_report.md
        
    - name: 上傳報告
      uses: actions/upload-artifact@v4
      with:
        name: security-report
        path: security_report.md
```

#### 存取權限審計

```bash
### 定期檢查存取權限
gh api /repos/:owner/:repo/collaborators | jq '.[].login'

### 檢查團隊成員
gh api /orgs/:org/teams/:team/members | jq '.[].login'

### 檢查部署金鑰
gh api /repos/:owner/:repo/keys

### 檢查 Webhooks
gh api /repos/:owner/:repo/hooks

### 檢查 Actions Secrets
gh secret list
```

#### 安全儀表板

```markdown
📊 **安全監控指標**

### 關鍵指標
- ✅ 依賴套件漏洞數量: 0 高風險
- ✅ 程式碼掃描問題: 2 中風險, 5 低風險
- ✅ 分支保護規則: 已啟用
- ✅ 雙因素驗證: 100% 團隊成員
- ✅ 金鑰輪換: 最後更新 30 天前

### 審計檢查
- [ ] 每月存取權限審查
- [ ] 每季安全政策更新
- [ ] 每年滲透測試
- [ ] 持續依賴套件監控
```

---

## 11. VS Code Git 整合深度應用

### 11.1 Source Control 面板詳解

#### 基本操作界面

```markdown
📁 **Source Control 面板功能**

🔄 **Changes 區域**
- 顯示所有修改的檔案
- 支援檔案分組 (修改/新增/刪除)
- 一鍵 stage/unstage 操作

📝 **Commit 區域**
- 快速提交訊息輸入
- Commit 和 Commit & Push 按鈕
- 顯示當前分支資訊

🌿 **Branch 管理**
- 分支切換和建立
- 遠端分支同步狀態
- Merge/Rebase 快捷操作
```

#### 進階檔案操作

```markdown
🔧 **右鍵選單功能**

- **Open File**: 開啟檔案查看完整內容
- **Open Changes**: 並排比較修改前後
- **Stage Changes**: 將檔案加入暫存區
- **Discard Changes**: 捨棄檔案修改
- **Ignore this extension**: 自動加入 .gitignore
```

### 11.2 Git Graph 擴充功能

#### 安裝和基本設定

```json
// settings.json
{
  "git-graph.showTags": true,
  "git-graph.showRemoteBranches": true,
  "git-graph.fetchOnStartup": true,
  "git-graph.showSignatureStatus": true
}
```

#### 視覺化分支管理

```markdown
📊 **Git Graph 功能特色**

🌐 **圖形化歷史**
- 清楚的分支和合併視圖
- 顏色區分不同分支
- 滑鼠懸停顯示詳細資訊

🔍 **進階篩選**
- 按作者篩選提交
- 按日期範圍篩選
- 按檔案路徑篩選

⚡ **快速操作**
- 右鍵建立分支
- 直接 cherry-pick 提交
- 一鍵 merge 或 rebase
```

### 11.3 GitLens 進階功能

#### 程式碼註解和歷史

```markdown
👁️ **GitLens 核心功能**

📝 **Blame 註解**
- 每行程式碼的作者和時間
- 懸停顯示完整提交資訊
- 快速跳轉到相關提交

🔍 **檔案歷史**
- 完整的檔案修改歷史
- 視覺化時間軸
- 快速比較不同版本

🌿 **分支比較**
- 分支間的差異檢視
- 提交統計和圖表
- 貢獻者分析
```

#### 自定義設定

```json
{
  "gitlens.blame.format": "${author} • ${date} • ${message}",
  "gitlens.blame.highlight.enabled": true,
  "gitlens.currentLine.enabled": true,
  "gitlens.hovers.currentLine.over": "line",
  "gitlens.views.repositories.files.layout": "tree"
}
```

### 11.4 Merge Conflict 解決工具

#### 三方合併編輯器

```markdown
⚔️ **衝突解決界面**

📍 **Current (HEAD)**
- 當前分支的變更
- 顯示為左側面板
- 標記為綠色

📍 **Incoming**
- 要合併進來的變更
- 顯示為右側面板
- 標記為藍色

📍 **Result**
- 最終合併結果
- 中間編輯面板
- 可手動編輯調整
```

#### 快速解決按鈕

```markdown
🔧 **一鍵解決選項**

- **Accept Current**: 保留當前分支的變更
- **Accept Incoming**: 採用傳入的變更
- **Accept Both**: 保留雙方的變更
- **Compare Changes**: 詳細比較差異
```

### 11.5 自動化工作流程設定

#### Git Hooks 整合

```bash
#!/bin/sh
### .git/hooks/pre-commit
### VS Code 可以自動執行的 Git Hooks

### 程式碼格式檢查
npm run lint || exit 1

### 自動格式化
npm run format

### 執行快速測試
npm run test:unit || exit 1

echo "Pre-commit 檢查完成 ✅"
```

#### 工作區設定範本

```json
// .vscode/settings.json
{
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.pruneOnFetch": true,
  "git.rebaseWhenSync": true,
  
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,
  
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

---

## 12. 附錄：常用指令清單

### 12.1 基本指令

#### 設定與查看

```bash
### 查看設定
git config --list
git config user.name
git config user.email

### 設定別名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit

### 查看說明
git help <command>
git <command> --help
```

#### 倉庫操作

```bash
### 初始化倉庫
git init

### 複製倉庫
git clone <url>
git clone <url> <directory>

### 查看遠端倉庫
git remote -v
git remote show origin

### 新增遠端倉庫
git remote add upstream <url>
```

### 12.2 分支操作

```bash
### 查看分支
git branch                    # 本地分支
git branch -r                 # 遠端分支
git branch -a                 # 所有分支

### 建立分支
git branch <branch-name>      # 建立但不切換
git checkout -b <branch-name> # 建立並切換
git switch -c <branch-name>   # 建立並切換（新語法）

### 切換分支
git checkout <branch-name>
git switch <branch-name>      # 新語法

### 刪除分支
git branch -d <branch-name>   # 安全刪除
git branch -D <branch-name>   # 強制刪除
git push origin --delete <branch-name>  # 刪除遠端分支

### 重新命名分支
git branch -m <new-name>      # 重新命名目前分支
git branch -m <old> <new>     # 重新命名指定分支
```

### 12.3 提交操作

```bash
### 查看狀態
git status
git status -s                 # 簡短格式

### 新增檔案
git add <file>                # 新增特定檔案
git add .                     # 新增所有變更
git add -A                    # 新增所有變更（包含刪除）
git add -p                    # 互動式新增

### 提交變更
git commit -m "message"       # 提交並附訊息
git commit -am "message"      # 新增並提交已追蹤檔案
git commit --amend            # 修改最後一次提交

### 查看歷史
git log                       # 詳細歷史
git log --oneline             # 簡潔歷史
git log --graph               # 圖形化歷史
git log -p                    # 顯示變更內容
git log --author="name"       # 特定作者
git log --since="2 weeks ago" # 時間範圍
```

### 12.4 同步操作

```bash
### 拉取變更
git fetch                     # 取得遠端變更（不合併）
git pull                      # 取得並合併
git pull --rebase             # 取得並 rebase

### 推送變更
git push                      # 推送到預設遠端
git push origin <branch>      # 推送到特定分支
git push -u origin <branch>   # 推送並設定上游
git push --force-with-lease   # 安全的強制推送

### 合併分支
git merge <branch>            # 合併指定分支
git merge --no-ff <branch>    # 強制建立合併提交
git merge --squash <branch>   # 壓縮合併
```

### 12.5 檢查與比較

```bash
### 檢查差異
git diff                      # 工作目錄 vs 暫存區
git diff --staged             # 暫存區 vs 最後提交
git diff HEAD                 # 工作目錄 vs 最後提交
git diff <branch1> <branch2>  # 比較分支

### 檢查檔案
git show <commit>             # 顯示特定提交
git show <commit>:<file>      # 顯示特定版本的檔案
git blame <file>              # 顯示每行的作者
```

### 12.6 復原操作

```bash
### 取消變更
git checkout -- <file>        # 復原工作目錄的檔案
git reset HEAD <file>         # 取消暫存
git reset --soft HEAD~1       # 取消提交（保留變更）
git reset --hard HEAD~1       # 取消提交（刪除變更）

### 回復提交
git revert <commit>           # 建立新提交來復原
git revert --no-commit <commit>  # 復原但不提交

### 暫存變更
git stash                     # 暫存變更
git stash pop                 # 恢復暫存
git stash list                # 查看暫存清單
git stash drop                # 刪除暫存
```

### 12.7 進階操作指令

```bash
### Rebase
git rebase <branch>           # 重新基於指定分支
git rebase -i HEAD~3          # 互動式 rebase
git rebase --continue         # 繼續 rebase
git rebase --abort            # 中止 rebase

### Cherry-pick
git cherry-pick <commit>      # 套用特定提交
git cherry-pick <start>..<end>  # 套用提交範圍

### 標籤
git tag                       # 查看標籤
git tag <tag-name>            # 建立標籤
git tag -d <tag-name>         # 刪除標籤
git push origin <tag-name>    # 推送標籤

### 清理
git clean -f                  # 刪除未追蹤檔案
git clean -fd                 # 刪除未追蹤檔案和目錄
git gc                        # 垃圾回收
```

### 12.8 CI/CD 相關指令

```bash
### GitHub CLI (gh)
gh auth login                 # 登入 GitHub
gh repo view                  # 查看倉庫資訊
gh pr list                    # 列出 Pull Requests
gh pr create                  # 建立 Pull Request
gh pr merge                   # 合併 Pull Request
gh workflow list              # 列出工作流程
gh workflow run               # 執行工作流程
gh run list                   # 列出執行記錄
gh run watch                  # 監看執行狀態

### Actions 本地測試 (act)
act                          # 執行所有工作流程
act push                     # 模擬 push 事件
act pull_request             # 模擬 PR 事件
act -l                       # 列出可用工作
act -n                       # 乾運行模式

### Docker 相關
docker build -t app:latest . # 建構映像
docker run -p 8080:8080 app  # 執行容器
docker logs <container-id>   # 查看日誌
docker exec -it <container> bash  # 進入容器
```

---

## 13. 檢查清單

### 13.1 新進員工設定檢查清單

#### 環境設定

- [ ] 已安裝 Git（版本 2.30 以上）
- [ ] 已設定 `user.name` 和 `user.email`
- [ ] 已建立 GitHub 帳號
- [ ] 已設定 SSH 金鑰或 Personal Access Token
- [ ] 已測試 GitHub 連線
- [ ] 已加入專案組織/團隊
- [ ] 已取得專案倉庫存取權限

#### 專案設定

- [ ] 已 clone 專案倉庫
- [ ] 已設定遠端倉庫別名
- [ ] 已閱讀 README.md
- [ ] 已閱讀貢獻指南
- [ ] 已設定本地開發環境
- [ ] 已執行初始測試確認環境正常

#### CI/CD 環境

- [ ] 已了解專案的 CI/CD 流程
- [ ] 已安裝必要的本地工具（Docker、kubectl 等）
- [ ] 已取得必要的環境存取權限
- [ ] 已了解部署流程和回滾機制

### 13.2 日常開發檢查清單

#### 開始新功能開發前

- [ ] 已同步最新的 main 分支
- [ ] 分支名稱符合命名規範
- [ ] 已確認相關 Issue 或需求
- [ ] 已規劃開發範圍和時程

#### 開發進行過程中

- [ ] 頻繁提交小批次變更
- [ ] Commit message 符合規範
- [ ] 定期同步 main 分支
- [ ] 程式碼通過本地測試
- [ ] 遵循程式碼風格指南

#### 提交 PR 之前

- [ ] 所有測試通過
- [ ] 程式碼已自我審查
- [ ] 已更新相關文件
- [ ] PR 描述完整
- [ ] 已指派適當的審查者
- [ ] CI 檢查通過

### 13.3 Code Review 檢查清單

#### 審查者職責

- [ ] 程式碼邏輯正確性
- [ ] 測試覆蓋率充足
- [ ] 程式碼可讀性和可維護性
- [ ] 效能考量
- [ ] 安全性檢查
- [ ] 是否遵循專案規範
- [ ] 文件是否更新

#### 提供建設性回饋

- [ ] 指出具體問題位置
- [ ] 說明問題原因
- [ ] 提供改善建議
- [ ] 語氣友善專業
- [ ] 區分意見和事實

### 13.4 合併前檢查清單

#### 最終確認

- [ ] 所有 CI 檢查通過
- [ ] 至少 2 位審查者同意
- [ ] 沒有未解決的對話
- [ ] 分支已更新到最新版本
- [ ] 沒有合併衝突
- [ ] 相關 Issue 已連結

#### 合併後清理

- [ ] 確認合併成功
- [ ] 刪除功能分支
- [ ] 更新本地分支
- [ ] 關閉相關 Issue
- [ ] 更新專案看板狀態

### 13.5 CI/CD 檢查清單

#### CI/CD 設定階段

- [ ] 建立 `.github/workflows/` 目錄
- [ ] 設定基本 CI 工作流程
- [ ] 配置必要的 Secrets
- [ ] 設定分支保護規則
- [ ] 整合程式碼品質工具

#### CI/CD 測試階段

- [ ] 多版本 Java 測試
- [ ] 跨平台相容性測試
- [ ] 安全漏洞掃描
- [ ] 效能基準測試
- [ ] 整合測試自動化

#### CI/CD 部署階段

- [ ] 測試環境自動部署
- [ ] 生產環境審查機制
- [ ] 回滾機制設定
- [ ] 健康檢查自動化
- [ ] 監控與告警設定

### 13.6 GitHub 功能使用檢查清單

#### Issue 管理

- [ ] 已設定 Issue 範本
- [ ] 建立標籤分類系統
- [ ] 指派責任人和里程碑
- [ ] 定期檢查和更新狀態

#### Project 專案管理

- [ ] 建立專案看板
- [ ] 設定自動化規則
- [ ] 定義工作流程狀態
- [ ] 定期更新進度

#### Wiki 文件維護

- [ ] 建立文件架構
- [ ] 定期更新內容
- [ ] 檢查連結有效性
- [ ] 版本發布時同步更新

#### Release 發布管理

- [ ] 遵循語義化版本規範
- [ ] 撰寫完整的 Release Notes
- [ ] 測試發布流程
- [ ] 通知相關使用者

### 13.7 緊急情況檢查清單

#### 發現重大問題時

- [ ] 立即通知團隊
- [ ] 評估影響範圍
- [ ] 暫停相關部署
- [ ] 建立 hotfix 分支
- [ ] 快速修復問題
- [ ] 加速 review 流程
- [ ] 部署修復版本
- [ ] 撰寫事後分析報告

#### 程式碼遺失或損壞時

- [ ] 不要恐慌
- [ ] 檢查 `git reflog`
- [ ] 嘗試從備份恢復
- [ ] 尋求資深同事協助
- [ ] 記錄問題和解決過程
- [ ] 檢討預防措施

#### CI/CD 流程失敗時

- [ ] 檢查失敗原因和日誌
- [ ] 確認是否為基礎設施問題
- [ ] 評估是否需要手動部署
- [ ] 通知相關團隊
- [ ] 記錄故障處理過程
- [ ] 優化 CI/CD 流程防止再次發生

---

## 📞 技術支援

### 聯絡資訊

- **技術主管**: [聯絡資訊]
- **資深開發者**: [聯絡資訊]
- **DevOps 團隊**: [聯絡資訊]
- **系統管理員**: [聯絡資訊]

### 有用資源

- [專案 Wiki](link-to-wiki)
- [API 文件](link-to-api-docs)
- [編碼規範](link-to-coding-standards)
- [CI/CD 監控面板](link-to-monitoring)
- [Git 官方文件](https://git-scm.com/doc)
- [GitHub 說明](https://docs.github.com)
- [GitHub Actions 文件](https://docs.github.com/en/actions)

### 常見問題快速解決

#### Git 問題

```bash
# 查看操作歷史
git reflog

# 恢復到安全狀態
git reset --hard HEAD@{n}

# 強制同步遠端
git fetch origin
git reset --hard origin/main
```

#### CI/CD 問題

```bash
# 本地測試 GitHub Actions
act

# 檢查工作流程狀態
gh run list

# 重新執行失敗的工作流程
gh run rerun <run-id>
```

---

**版權聲明**: 本文件為內部使用，請勿外流。如有問題請聯絡技術團隊。

**最後更新**: 2025年8月29日 - 版本 2.0
**主要更新內容**:

- 新增 Git 進階操作章節（Interactive Rebase、Cherry-pick、Bisect 等）
- 擴充安全最佳實務和機密資訊管理
- 詳細的 VS Code Git 整合應用指南
- 加入 GitHub Copilot 使用規範
- 增強效能優化和疑難排解章節
- 更新團隊協作最佳實務

### 13.8 安全檢查清單

#### 程式碼安全

- [ ] 無硬編碼密碼或 API 金鑰
- [ ] 機密資訊已加入 .gitignore
- [ ] 依賴套件安全掃描通過
- [ ] 程式碼掃描無高風險漏洞

#### 存取控制

- [ ] SSH 金鑰使用強密碼保護
- [ ] Personal Access Token 權限最小化
- [ ] 分支保護規則已啟用
- [ ] 二階段認證已開啟

#### 審計合規

- [ ] 所有變更都有完整的審計記錄
- [ ] 敏感操作需要多人審核
- [ ] 定期檢查存取權限
- [ ] 安全事件回應流程已建立

---

## 14. 疑難排解與支援

### 14.1 常見問題 FAQ

#### Q: Git 操作很慢怎麼辦？

#### A: 效能優化步驟

```bash
### 1. 檢查儲存庫大小
git count-objects -vH

### 2. 清理不必要的物件
git gc --aggressive --prune=now

### 3. 檢查是否有大型檔案
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0,6)}' | \
  sort --numeric-sort --key=2 | \
  tail -10

### 4. 考慮使用 Git LFS
git lfs migrate import --include="*.zip,*.pdf,*.png"
```

#### Q: 如何恢復誤刪的分支？

#### A: 分支恢復方法

```bash
### 1. 查看所有操作歷史
git reflog

### 2. 找到分支刪除前的 commit
git reflog | grep "分支名稱"

### 3. 從 commit 重新建立分支
git checkout -b 分支名稱 <commit-hash>

### 4. 推送恢復的分支
git push origin 分支名稱
```

#### Q: 合併衝突太複雜怎麼處理？

#### A: 複雜衝突處理策略

```bash
### 1. 中止當前合併
git merge --abort

### 2. 使用工具輔助合併
git mergetool

### 3. 分步驟解決衝突
git checkout --theirs <檔案>  # 使用對方版本
git checkout --ours <檔案>    # 使用我方版本

### 4. 手動編輯後標記為已解決
git add <已解決的檔案>
git commit
```

### 14.2 效能優化指南

#### 大型儲存庫克隆優化

```bash
### 部分克隆（減少初始下載時間）
git clone --filter=blob:none <url>
git clone --filter=tree:0 <url>

### 淺層克隆（僅下載最近的歷史）
git clone --depth 1 <url>

### 僅克隆單一分支
git clone --single-branch --branch main <url>
```

#### 日常操作優化

```bash
### 啟用檔案系統監控
git config core.fsmonitor true
git config core.untrackedCache true

### 設定合理的 pack 大小
git config pack.packSizeLimit 2g
git config pack.windowMemory 256m

### 啟用平行處理
git config pack.threads 0
git config index.threads 0
```

### 14.3 技術支援聯絡方式

#### 內部支援

- **Git 專家**: 資深開發工程師
- **GitHub 管理員**: DevOps 團隊
- **安全議題**: 資安團隊
- **工具問題**: IT 支援部門

#### 學習資源聯絡

- **新人培訓**: 請聯絡 HR 安排
- **進階課程**: 技術發展部
- **最佳實務分享**: 架構團隊

#### 緊急支援

```markdown
🚨 **緊急情況聯絡方式**

- 生產環境問題: 值班工程師 (24/7)
- 安全事件: 資安事件回應小組
- 系統故障: 基礎設施團隊
```

### 14.4 學習資源推薦

#### 官方文件

- [Git 官方教學](https://git-scm.com/docs/gittutorial)
- [GitHub 說明文件](https://docs.github.com)
- [GitHub Actions 文件](https://docs.github.com/en/actions)

#### 進階學習

- [Pro Git 書籍](https://git-scm.com/book)
- [GitHub Flow 指南](https://guides.github.com/introduction/flow/)
- [Git 最佳實務](https://www.atlassian.com/git/tutorials/comparing-workflows)

#### 實作練習

- [Learn Git Branching](https://learngitbranching.js.org/)
- [GitHub Learning Lab](https://lab.github.com/)
- [Katacoda Git 課程](https://www.katacoda.com/courses/git)

#### 團隊分享

```markdown
📚 **內部學習計畫**

- 每月技術分享會
- Git 進階工作坊
- Code Review 最佳實務討論
- 新工具和功能介紹
```

---

**版權聲明**: 本文件為內部使用，請勿外流。如有問題請聯絡技術團隊。

**最後更新**: 2025年10月17日 - 版本 2.1

**主要更新內容**:

- 新增 Git 進階操作章節（Interactive Rebase、Cherry-pick、Bisect 等）
- 擴充安全最佳實務和機密資訊管理
- 完善第 10 章安全最佳實務所有子章節（10.1-10.6）
- 詳細的 VS Code Git 整合應用指南
- 加入 GitHub Copilot 使用規範
- 增強效能優化和疑難排解章節
- 更新團隊協作最佳實務
- 修正目錄與內容完全對應

---

## 📝 文件維護記錄

| 版本 | 日期 | 更新者 | 主要更新內容 |
|------|------|--------|-------------|
| 2.1 | 2025-10-17 | GitHub Copilot | 補充完整第 10 章安全最佳實務，修正目錄對應 |
| 2.0 | 2025-08-29 | 專案開發團隊 | 新增進階章節，擴充 CI/CD 和安全內容 |
| 1.0 | 2025-06-01 | 專案開發團隊 | 初始版本發布 |
