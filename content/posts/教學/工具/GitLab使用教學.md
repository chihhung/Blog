+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'GitLab使用教學'
tags = ['教學', '工具']
categories = ['教學']
+++
# GitLab 使用教學手冊

## 📋 目錄

1. [GitLab 基本介紹](#1-gitlab-基本介紹)
   - 1.1 [Git vs. GitLab - 基本概念](#11-git-vs-gitlab---基本概念)
   - 1.2 [為什麼選擇 GitLab？](#12-為什麼選擇-gitlab)
   - 1.3 [專案架構概覽](#13-專案架構概覽)
   - 1.4 [GitLab 核心功能詳解](#14-gitlab-核心功能詳解)

2. [專案工作流程說明](#2-專案工作流程說明)
   - 2.1 [環境準備](#21-環境準備)
   - 2.2 [Clone - 複製專案到本地](#22-clone---複製專案到本地)
   - 2.3 [Pull - 同步遠端更新](#23-pull---同步遠端更新)
   - 2.4 [Commit - 提交變更](#24-commit---提交變更)
   - 2.5 [Push - 推送變更到遠端](#25-push---推送變更到遠端)
   - 2.6 [Merge Request - 合併請求](#26-merge-request---合併請求)

3. [專案開發規範](#3-專案開發規範)
   - 3.1 [分支策略](#31-分支策略)
   - 3.2 [Commit Message 規範](#32-commit-message-規範)
   - 3.3 [Merge Request 流程](#33-merge-request-流程)
   - 3.4 [Code Review 要求](#34-code-review-要求)

4. [GitLab CI/CD 基本介紹](#4-gitlab-cicd-基本介紹)
   - 4.1 [CI/CD 概念說明](#41-cicd-概念說明)
   - 4.2 [GitLab CI/CD 架構](#42-gitlab-cicd-架構)
   - 4.3 [.gitlab-ci.yml 設定檔](#43-gitlab-ciyml-設定檔)
   - 4.4 [Java 專案 CI/CD 設定](#44-java-專案-cicd-設定)
   - 4.5 [常用 CI/CD 指令](#45-常用-cicd-指令)
   - 4.6 [本專案的 CI/CD 應用](#46-本專案的-cicd-應用)

5. [常見問題與解決方式](#5-常見問題與解決方式)
   - 5.1 [Merge 衝突處理](#51-merge-衝突處理)
   - 5.2 [錯誤回復方式](#52-錯誤回復方式)
   - 5.3 [分支管理問題](#53-分支管理問題)
   - 5.4 [權限和認證問題](#54-權限和認證問題)
   - 5.5 [效能和同步問題](#55-效能和同步問題)
   - 5.6 [CI/CD Pipeline 問題](#56-cicd-pipeline-問題)
   - 5.7 [團隊協作問題](#57-團隊協作問題)

6. [開發最佳實務建議](#6-開發最佳實務建議)
   - 6.1 [程式碼管理最佳實務](#61-程式碼管理最佳實務)
   - 6.2 [Code Review 最佳實務](#62-code-review-最佳實務)
   - 6.3 [測試最佳實務](#63-測試最佳實務)
   - 6.4 [安全性最佳實務](#64-安全性最佳實務)
   - 6.5 [效能最佳實務](#65-效能最佳實務)
   - 6.6 [文件化最佳實務](#66-文件化最佳實務)
   - 6.7 [團隊協作最佳實務](#67-團隊協作最佳實務)

7. [檢查清單](#7-檢查清單)
   - 7.1 [新進同仁入門檢查清單](#71-新進同仁入門檢查清單)
   - 7.2 [日常開發檢查清單](#72-日常開發檢查清單)
   - 7.3 [Merge Request 檢查清單](#73-merge-request-檢查清單)
   - 7.4 [CI/CD 檢查清單](#74-cicd-檢查清單)
   - 7.5 [發布檢查清單](#75-發布檢查清單)
   - 7.6 [緊急情況檢查清單](#76-緊急情況檢查清單)
   - 7.7 [定期維護檢查清單](#77-定期維護檢查清單)

8. [進階功能與整合](#8-進階功能與整合)
   - 8.1 [GitLab API 整合](#81-gitlab-api-整合)
   - 8.2 [第三方工具整合](#82-第三方工具整合)
   - 8.3 [自動化與 DevOps](#83-自動化與-devops)
   - 8.4 [安全性進階設定](#84-安全性進階設定)
   - 8.5 [效能優化](#85-效能優化)
   - 8.6 [災難恢復](#86-災難恢復)
   - 8.7 [GitLab Runner 深度配置](#87-gitlab-runner-深度配置)
   - 8.8 [多環境部署策略](#88-多環境部署策略)
   - 8.9 [容器化與 Kubernetes 整合](#89-容器化與-kubernetes-整合)
   - 8.10 [效能監控與分析](#810-效能監控與分析)
   - 8.11 [實際案例研究](#811-實際案例研究)
   - 8.12 [未來趨勢與發展](#812-未來趨勢與發展)

9. [附錄](#9-附錄)
   - 9.1 [聯絡資訊](#91-聯絡資訊)
   - 9.2 [參考資源](#92-參考資源)
   - 9.3 [工具推薦](#93-工具推薦)

10. [補充主題](#10-補充主題)
    - 10.1 [性能基準測試與優化](#101-性能基準測試與優化)
    - 10.2 [災難恢復演練](#102-災難恢復演練)
    - 10.3 [合規自動化](#103-合規自動化)
    - 10.4 [成本優化策略](#104-成本優化策略)

---

## 1. GitLab 基本介紹

### 1.1 Git vs. GitLab - 基本概念

#### Git

- **定義**：分散式版本控制系統（Distributed Version Control System）
- **功能**：追蹤檔案變更、分支管理、合併操作
- **特性**：本地操作、離線工作、完整歷史記錄

#### GitLab

- **定義**：基於 Git 的 Web 平台，提供完整的 DevOps 生命週期管理
- **功能**：程式碼託管、專案管理、CI/CD、Code Review、Issue 追蹤
- **優勢**：團隊協作、視覺化介面、自動化部署

### 1.2 為什麼選擇 GitLab？

#### 🎯 團隊協作優勢

- **統一平台**：從程式碼管理到部署，一站式解決方案
- **權限管控**：細緻的角色權限設定，確保專案安全
- **可視化**：直觀的 Web 介面，降低學習門檻

#### 🚀 開發效率提升

- **Merge Request**：標準化的程式碼審查流程
- **CI/CD 整合**：自動化測試與部署
- **Issue 追蹤**：需求管理與 Bug 追蹤

#### 🔒 企業級安全

- **存取控制**：多層次的安全防護
- **稽核記錄**：完整的操作歷史追蹤
- **備份機制**：資料安全保障

### 1.3 專案架構概覽

```text
GitLab 專案結構
├── 程式碼倉庫 (Repository)
├── 分支管理 (Branches)
├── 合併請求 (Merge Requests)
├── 議題追蹤 (Issues)
├── CI/CD 管道 (Pipelines)
├── Wiki 文件
└── 專案設定 (Settings)
```

#### 💡 實務建議

- 新進同仁建議先熟悉 GitLab Web 介面操作
- 了解專案的分支策略和命名規範
- 參與 Code Review 過程，學習團隊的程式碼品質標準

### 1.4 GitLab 核心功能詳解

#### 📋 Issue 管理

**功能說明**：Issue 是 GitLab 的任務追蹤系統，用於管理 Bug、功能需求、改善建議等

**主要特性**：

- **分類管理**：使用 Label 標籤分類 Issue 類型
- **指派責任**：指派給特定開發者處理
- **狀態追蹤**：Open、In Progress、Closed 等狀態
- **關聯功能**：可與 Merge Request、Commit 關聯

**使用範例**：

```markdown
# Issue 範例：修復登入功能錯誤

### 問題描述
使用者在登入時偶爾會遇到 500 錯誤

### 重現步驟
1. 開啟登入頁面
2. 輸入正確的帳號密碼
3. 點選登入按鈕
4. 有時會顯示 500 錯誤

### 預期行為
應該能正常登入系統

### 實際行為
偶爾出現 500 錯誤

### 環境資訊
- 瀏覽器：Chrome 120.0
- 作業系統：Windows 10
- 服務器：Production
```

#### 🏷️ Labels 標籤系統

**標籤類型**：

- **類型標籤**：`bug`、`feature`、`enhancement`、`documentation`
- **優先級**：`priority::high`、`priority::medium`、`priority::low`
- **狀態標籤**：`status::todo`、`status::in-progress`、`status::review`
- **模組標籤**：`frontend`、`backend`、`database`、`api`

**標籤使用策略**：

```text
標籤組合範例：
├── bug + priority::high + backend
├── feature + priority::medium + frontend
├── enhancement + priority::low + documentation
└── security + priority::critical + api
```

#### 🎯 Milestone 里程碑

**功能說明**：Milestone 用於組織和追蹤專案進度，通常對應版本發布

**使用方式**：

- **版本規劃**：v1.0.0、v1.1.0、v2.0.0
- **衝刺管理**：Sprint 1、Sprint 2、Sprint 3
- **功能分組**：使用者管理模組、付款系統、報表功能

**里程碑設定**：

```text
Milestone: v1.2.0
├── 開始日期：2024-02-01
├── 結束日期：2024-03-15
├── 描述：使用者體驗改善版本
├── 相關 Issues：15 個
└── 完成度：60%
```

#### 📊 Project 專案管理

**專案看板**：

```text
Kanban Board:
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   待辦事項     │  │   進行中      │  │   審查中      │  │   已完成      │
│              │  │              │  │              │  │              │
│ • Issue #123 │→ │ • Issue #124 │→ │ • MR !456    │→ │ • Issue #122 │
│ • Issue #125 │  │ • Issue #126 │  │ • MR !457    │  │ • Issue #121 │
│ • Issue #127 │  │              │  │              │  │ • Issue #120 │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```

**專案權限管理**：

| 角色 | 權限 | 說明 |
|------|------|------|
| Owner | 完整權限 | 專案擁有者，可管理所有設定 |
| Maintainer | 管理權限 | 可管理分支、標籤、專案設定 |
| Developer | 開發權限 | 可推送程式碼、建立 MR |
| Reporter | 檢視權限 | 可檢視程式碼、建立 Issue |
| Guest | 受限權限 | 僅可檢視公開內容 |

#### 👥 Group 群組管理

**群組階層**：

```text
組織架構：
Company Group
├── Frontend Team
│   ├── React Project
│   └── Vue Project
├── Backend Team
│   ├── API Gateway
│   └── Microservices
└── DevOps Team
    ├── CI/CD Tools
    └── Infrastructure
```

**群組優勢**：

- **權限繼承**：子專案自動繼承群組權限
- **統一設定**：CI/CD 變數、Runner 設定等
- **資源共享**：共用 Docker Registry、Package Registry

#### 📦 Package Registry

**支援類型**：

- **Maven Repository**：Java 套件管理
- **npm Registry**：Node.js 套件管理
- **Docker Registry**：容器映像檔管理
- **NuGet Gallery**：.NET 套件管理

**Maven 使用範例**：

```xml
<!-- pom.xml 設定 -->
<repositories>
    <repository>
        <id>gitlab-maven</id>
        <url>https://gitlab.company.com/api/v4/projects/123/packages/maven</url>
    </repository>
</repositories>

<distributionManagement>
    <repository>
        <id>gitlab-maven</id>
        <url>https://gitlab.company.com/api/v4/projects/123/packages/maven</url>
    </repository>
</distributionManagement>
```

#### 🔒 Security 安全功能

**安全掃描類型**：

- **SAST** (Static Application Security Testing)：靜態程式碼安全分析
- **DAST** (Dynamic Application Security Testing)：動態應用程式安全測試
- **Dependency Scanning**：相依性漏洞掃描
- **Container Scanning**：容器映像檔安全掃描
- **Secret Detection**：敏感資料洩漏檢測

**安全設定範例**：

```yaml
# .gitlab-ci.yml 安全掃描設定
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml

variables:
  SAST_JAVA_VERSION: "17"
  SECURE_LOG_LEVEL: "debug"

sast:
  stage: test
  variables:
    SAST_EXCLUDED_PATHS: "spec, test, tests, tmp"
```

#### 📝 Wiki 文件系統

**Wiki 功能**：

- **Markdown 支援**：完整的 Markdown 語法支援
- **版本控制**：Wiki 頁面也有版本歷史
- **協作編輯**：多人可同時編輯不同頁面
- **檔案上傳**：支援圖片和附件

**Wiki 結構範例**：

```text
Wiki 頁面結構：
├── Home (首頁)
├── 架構設計
│   ├── 系統架構圖
│   ├── 資料庫設計
│   └── API 設計
├── 部署指南
│   ├── 環境設定
│   ├── 部署流程
│   └── 監控配置
└── 開發規範
    ├── 編碼標準
    ├── Git 工作流程
    └── Code Review 指南
```

#### 🔧 GitLab Runner

**Runner 類型**：

- **Shared Runners**：GitLab.com 提供的共用執行器
- **Group Runners**：群組層級的專用執行器
- **Project Runners**：專案專用的執行器

**Runner 標籤**：

```yaml
# .gitlab-ci.yml 指定 Runner
build-job:
  stage: build
  tags:
    - docker
    - linux
    - java-17
  script:
    - mvn clean compile
```

**Runner 設定**：

```bash
# 註冊 Runner
sudo gitlab-runner register \
  --url https://gitlab.company.com/ \
  --registration-token PROJECT_TOKEN \
  --description "Java Build Runner" \
  --tag-list "java,maven,docker" \
  --executor docker \
  --docker-image maven:3.8.4-openjdk-17
```

#### 📊 Analytics 分析功能

**可用報表**：

- **Repository Analytics**：程式碼提交統計
- **CI/CD Analytics**：Pipeline 執行統計
- **Issue Analytics**：Issue 處理統計
- **Merge Request Analytics**：MR 審查統計

**效能指標**：

```text
DevOps 指標：
├── Lead Time：從需求到部署的時間
├── Deployment Frequency：部署頻率
├── Mean Time to Recovery：故障恢復時間
└── Change Failure Rate：變更失敗率
```

#### 🔗 Snippets 程式碼片段

**功能說明**：Snippets 用於分享程式碼片段、設定檔或小型腳本

**使用情境**：

- **程式碼範例**：分享常用的程式碼模板
- **設定檔**：分享設定檔範例
- **工具腳本**：分享自動化腳本
- **技術筆記**：記錄技術要點

**Snippet 範例**：

```java
// 常用的 Spring Boot 控制器模板
@RestController
@RequestMapping("/api/v1")
@Slf4j
public class BaseController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> health() {
        Map<String, String> status = Map.of(
            "status", "UP",
            "timestamp", Instant.now().toString()
        );
        return ResponseEntity.ok(status);
    }
}
```

#### 📋 Boards 專案看板

**看板類型**：

- **Issue Board**：Issue 管理看板
- **Epic Board**：Epic 管理看板（Enterprise 版本）
- **Milestone Board**：里程碑看板

**看板自訂**：

- **欄位設定**：可自訂看板欄位
- **篩選器**：依標籤、指派者、里程碑篩選
- **自動化**：設定自動移動規則

#### 💡 GitLab 功能使用建議

- **Issue 優先**：養成先建立 Issue 再開發的習慣
- **標籤統一**：團隊統一 Label 使用規範
- **里程碑規劃**：定期設定和檢視里程碑進度
- **安全掃描**：啟用所有適用的安全掃描功能
- **文件維護**：保持 Wiki 文件的即時更新
- **分析報表**：定期檢視分析報表優化開發流程

---

## 2. 專案工作流程說明

### 2.1 環境準備

#### 安裝必要工具

```bash
# 安裝 Git (Windows)
# 下載並安裝：https://git-scm.com/download/win

# 驗證安裝
git --version
```

#### 設定 Git 基本資訊

```bash
# 設定使用者資訊
git config --global user.name "您的姓名"
git config --global user.email "您的信箱@company.com"

# 設定預設編輯器
git config --global core.editor "code --wait"

# 設定換行符號處理（Windows）
git config --global core.autocrlf true
```

### 2.2 Clone - 複製專案到本地

#### 🎯 操作步驟

1. **取得專案 URL**
   - 進入 GitLab 專案頁面
   - 點選 "Clone" 按鈕
   - 複製 HTTPS 或 SSH URL

2. **執行 Clone 指令**

```bash
# HTTPS 方式（建議新手使用）
git clone https://gitlab.company.com/project-group/project-name.git

# SSH 方式（需先設定 SSH Key）
git clone git@gitlab.company.com:project-group/project-name.git

# Clone 到指定資料夾
git clone https://gitlab.company.com/project-group/project-name.git my-project
```

3. **進入專案目錄**

```bash
cd project-name
ls -la  # 查看專案檔案
```

#### ⚠️ 注意事項

- 首次 Clone 會下載完整的專案歷史
- 確保網路連線穩定，大型專案可能需要較長時間
- Clone 後檢查分支狀態：`git branch -a`

### 2.3 Pull - 同步遠端更新

#### 🎯 日常同步作業

```bash
# 檢查目前狀態
git status

# 拉取最新變更（建議每天開始工作前執行）
git pull origin main

# 拉取特定分支
git pull origin feature/new-feature

# 強制拉取（謹慎使用）
git pull --force origin main
```

#### 🔄 分支同步策略

```bash
# 切換到主分支並同步
git checkout main
git pull origin main

# 切換回開發分支並合併主分支更新
git checkout feature/my-feature
git merge main
```

#### 💡 最佳實務

- **每日同步**：每天開始工作前先執行 `git pull`
- **提交前同步**：Push 前確保本地是最新狀態
- **解決衝突**：遇到衝突時，請尋求資深同事協助

### 2.4 Commit - 提交變更

#### 🎯 提交流程

1. **檢查變更狀態**

```bash
# 查看檔案狀態
git status

# 查看具體變更內容
git diff
git diff --staged  # 查看已加入暫存區的變更
```

2. **加入暫存區**

```bash
# 加入特定檔案
git add src/main/java/com/example/Service.java

# 加入所有變更檔案
git add .

# 加入特定類型檔案
git add "*.java"
```

3. **執行提交**

```bash
# 提交變更
git commit -m "feat: 新增使用者註冊功能"

# 提交並開啟編輯器寫詳細說明
git commit
```

#### 📝 Commit Message 規範（請參考第3節）

#### ⚠️ 提交前檢查

- 確保程式碼可以編譯
- 執行相關測試
- 檢查是否包含敏感資訊（密碼、金鑰等）

### 2.5 Push - 推送變更到遠端

#### 🎯 推送流程

```bash
# 推送到對應的遠端分支
git push origin feature/my-feature

# 首次推送新分支
git push -u origin feature/my-feature

# 推送到主分支（需要權限）
git push origin main
```

#### 🔒 推送前檢查

```bash
# 確認推送目標
git remote -v
git branch -vv

# 檢查即將推送的提交
git log --oneline origin/feature/my-feature..HEAD
```

### 2.6 Merge Request - 合併請求

#### 🎯 建立 Merge Request

1. **在 GitLab Web 介面**
   - 推送分支後，GitLab 會顯示建立 MR 的提示
   - 點選 "Create merge request"

2. **填寫 MR 資訊**
   - **標題**：簡潔描述變更內容
   - **描述**：詳細說明變更原因、實作方式、測試結果
   - **指派審查者**：選擇適當的 Code Reviewer
   - **標籤**：加入相關標籤（feature、bugfix、hotfix等）

3. **MR 模板範例**

```markdown
### 變更摘要
簡要描述此次變更的內容和目的

### 變更類型
- [ ] 新功能
- [ ] Bug 修復
- [ ] 文件更新
- [ ] 重構
- [ ] 效能改善

### 測試說明
- [ ] 單元測試已通過
- [ ] 整合測試已通過
- [ ] 手動測試已完成

### 相關 Issue
關聯的 Issue 編號：#123

### 檢查清單
- [ ] 程式碼遵循專案規範
- [ ] 已進行自我 Code Review
- [ ] 已更新相關文件
- [ ] 沒有包含敏感資訊
```

---

## 3. 專案開發規範

### 3.1 分支策略

#### 🌳 Git Flow 分支模型

我們採用改良版的 Git Flow 策略：

```text
main (主分支)
├── develop (開發分支)
│   ├── feature/user-authentication (功能分支)
│   ├── feature/payment-system (功能分支)
│   └── feature/admin-dashboard (功能分支)
├── release/v1.2.0 (發布分支)
├── hotfix/critical-security-fix (緊急修復分支)
└── support/v1.1.x (維護分支)
```

#### 🎯 分支說明

| 分支類型 | 命名規則 | 用途 | 生命週期 |
|---------|---------|------|---------|
| `main` | `main` | 正式環境部署 | 永久 |
| `develop` | `develop` | 開發整合 | 永久 |
| `feature` | `feature/功能名稱` | 新功能開發 | 臨時 |
| `release` | `release/版本號` | 發布準備 | 臨時 |
| `hotfix` | `hotfix/修復描述` | 緊急修復 | 臨時 |
| `support` | `support/版本號` | 長期維護 | 長期 |

#### � 分支命名規範

```bash
# 功能分支
feature/user-login-page
feature/shopping-cart-api
feature/email-notification

# 修復分支
hotfix/login-security-vulnerability
hotfix/payment-gateway-timeout

# 發布分支
release/v2.1.0
release/v2.1.1-hotfix
```

#### 🔄 分支操作流程

1. **建立功能分支**

```bash
# 從 develop 建立新功能分支
git checkout develop
git pull origin develop
git checkout -b feature/user-profile-update
```

2. **完成功能開發**

```bash
# 提交變更
git add .
git commit -m "feat: 新增使用者資料更新功能"
git push -u origin feature/user-profile-update
```

3. **建立 Merge Request**

```bash
# 在 GitLab 建立 MR: feature/user-profile-update → develop
```

### 3.2 Commit Message 規範

#### 📋 Conventional Commits 格式

```text
<類型>[可選範圍]: <描述>

[可選正文]

[可選頁腳]
```

#### 🏷️ 提交類型

| 類型 | 說明 | 範例 |
|------|------|------|
| `feat` | 新功能 | `feat: 新增使用者註冊功能` |
| `fix` | Bug 修復 | `fix: 修復登入驗證錯誤` |
| `docs` | 文件更新 | `docs: 更新 API 文件` |
| `style` | 格式調整 | `style: 調整程式碼縮排` |
| `refactor` | 重構 | `refactor: 重構使用者服務類別` |
| `test` | 測試相關 | `test: 新增使用者服務單元測試` |
| `chore` | 建置/工具 | `chore: 更新 Maven 相依性` |
| `perf` | 效能改善 | `perf: 優化資料庫查詢效能` |
| `ci` | CI/CD | `ci: 更新 GitLab CI 設定` |
| `revert` | 回復提交 | `revert: 回復提交 abc123` |

#### 📝 Commit 範例

```bash
# 基本格式
git commit -m "feat: 新增使用者登入功能"

# 包含範圍
git commit -m "feat(auth): 新增 JWT 驗證機制"

# 重大變更
git commit -m "feat!: 重新設計 API 回應格式

BREAKING CHANGE: API 回應格式從 { data: {} } 改為 { result: {} }"

# 關聯 Issue
git commit -m "fix: 修復購物車數量計算錯誤

修復在商品數量為零時的計算問題

Fixes #123"
```

#### ⚠️ Commit 注意事項

- **原子性**：每個 commit 只包含一個邏輯變更
- **明確描述**：清楚說明「做了什麼」而非「怎麼做」
- **使用現在式**：「新增功能」而非「新增了功能」
- **英文優先**：英文 commit message 便於國際協作

### 3.3 Merge Request 流程

#### 🎯 MR 建立流程

1. **準備階段**

```bash
# 確保分支是最新的
git checkout feature/my-feature
git fetch origin
git rebase origin/develop
```

2. **建立 MR**
   - 進入 GitLab 專案頁面
   - 點選 "Merge Requests" → "New merge request"
   - 選擇來源分支和目標分支
   - 填寫 MR 資訊

3. **MR 標題規範**

```text
[類型] 簡短描述

範例：
[Feature] 新增使用者個人資料管理功能
[Bugfix] 修復購物車結算金額計算錯誤
[Hotfix] 緊急修復登入安全性漏洞
[Docs] 更新 API 使用說明文件
```

#### 📋 MR 描述模板

```markdown
### 📋 變更摘要
簡要描述此次變更的內容和目的

### 🏷️ 變更類型
- [ ] ✨ 新功能 (Feature)
- [ ] 🐛 Bug 修復 (Bugfix)  
- [ ] 🔥 緊急修復 (Hotfix)
- [ ] 📚 文件更新 (Documentation)
- [ ] 🎨 程式碼重構 (Refactoring)
- [ ] ⚡ 效能改善 (Performance)
- [ ] 🧪 測試相關 (Testing)

### 🧪 測試說明
- [ ] 單元測試已通過：`mvn test`
- [ ] 整合測試已通過：`mvn verify`
- [ ] 手動測試已完成
- [ ] 效能測試已完成（如適用）

### 📸 測試截圖
（如有 UI 變更，請提供截圖）

### 🔗 相關連結
- 相關 Issue：#123
- 設計文件：[連結]
- API 文件：[連結]

### ✅ 檢查清單
- [ ] 程式碼遵循專案編碼規範
- [ ] 已進行自我 Code Review
- [ ] 已更新相關文件
- [ ] 沒有包含敏感資訊（密碼、API Key 等）
- [ ] 已更新 CHANGELOG.md（如適用）
- [ ] 已考慮向後相容性
- [ ] 已檢查效能影響

### 📝 額外說明
（任何需要審查者特別注意的事項）
```

### 3.4 Code Review 要求

#### 👥 審查者指派

- **強制審查者**：至少 1 位資深開發者
- **建議審查者**：相關模組負責人
- **安全審查**：涉及安全性變更需指派安全專家

#### 🔍 Code Review 檢查重點

#### 功能性檢查

- [ ] 程式碼邏輯正確
- [ ] 符合需求規格
- [ ] 邊界條件處理
- [ ] 錯誤處理完整

#### 品質檢查

- [ ] 程式碼可讀性
- [ ] 命名規範一致
- [ ] 適當的註解
- [ ] 函式複雜度合理

#### 安全性檢查

- [ ] 輸入驗證
- [ ] 權限控制
- [ ] 敏感資料處理
- [ ] SQL 注入防護

#### 效能檢查

- [ ] 演算法效率
- [ ] 資料庫查詢優化
- [ ] 記憶體使用
- [ ] 快取策略

#### 🔄 Review 流程

1. **提交 Review**
   - 仔細檢查程式碼變更
   - 提供建設性意見
   - 標示 `Request Changes` 或 `Approve`

2. **回應 Review**
   - 及時回應審查意見
   - 修正問題後重新提交
   - 解釋設計決策（如需要）

3. **最終審查**
   - 確認所有意見已處理
   - 執行最終測試
   - 核准合併

#### 💡 Review 最佳實務

- **及時審查**：在 24 小時內完成審查
- **建設性意見**：提供具體的改善建議
- **學習態度**：將 Review 視為學習機會

---

## 4. GitLab CI/CD 基本介紹

### 4.1 CI/CD 概念說明

#### 🔄 持續整合 (Continuous Integration)

**定義**：開發者頻繁地將程式碼變更合併到主分支，每次合併都會觸發自動化建置和測試

**優點**：

- **早期發現問題**：快速識別程式碼衝突和錯誤
- **提高程式碼品質**：自動化測試確保品質標準
- **減少整合風險**：避免大量變更造成的整合困難

#### 🚀 持續部署 (Continuous Deployment)

**定義**：通過自動化測試的程式碼變更會自動部署到生產環境

**優點**：

- **快速交付**：縮短從開發到上線的時間
- **降低風險**：小批次部署減少失敗影響
- **提高效率**：自動化減少人工作業

### 4.2 GitLab CI/CD 架構

#### 🏗️ 核心組件

```yaml
GitLab CI/CD Pipeline
├── .gitlab-ci.yml (設定檔)
├── GitLab Runner (執行器)
├── Jobs (工作)
├── Stages (階段)
└── Artifacts (產出物)
```

#### 📋 Pipeline 階段設計

```text
Pipeline Stages:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Build     │→ │    Test     │→ │   Deploy    │→ │   Monitor   │
│             │  │             │  │             │  │             │
│ • 編譯程式碼  │  │ • 單元測試   │  │ • 部署到測試  │  │ • 健康檢查   │
│ • 相依性檢查  │  │ • 整合測試   │  │ • 部署到正式  │  │ • 效能監控   │
│ • 程式碼掃描  │  │ • 安全掃描   │  │ • 資料庫更新  │  │ • 錯誤追蹤   │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

### 4.3 .gitlab-ci.yml 設定檔

#### 🎯 基本結構

```yaml
# .gitlab-ci.yml
# GitLab CI/CD 設定檔範例

# 定義執行階段
stages:
  - build
  - test
  - deploy

# 全域變數
variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"
  MAVEN_CLI_OPTS: "--batch-mode --errors --fail-at-end --show-version"

# 快取設定
cache:
  paths:
    - .m2/repository/
    - target/

# 建置階段
build-job:
  stage: build
  image: maven:3.8.4-openjdk-17
  script:
    - echo "開始建置專案..."
    - mvn $MAVEN_CLI_OPTS compile
    - echo "建置完成！"
  artifacts:
    paths:
      - target/
    expire_in: 1 hour

# 測試階段
test-job:
  stage: test
  image: maven:3.8.4-openjdk-17
  script:
    - echo "執行單元測試..."
    - mvn $MAVEN_CLI_OPTS test
    - echo "測試完成！"
  artifacts:
    reports:
      junit:
        - target/surefire-reports/TEST-*.xml
    expire_in: 1 week
  coverage: '/Total.*?([0-9]{1,3})%/'

# 程式碼品質檢查
code-quality:
  stage: test
  image: maven:3.8.4-openjdk-17
  script:
    - echo "執行程式碼品質檢查..."
    - mvn $MAVEN_CLI_OPTS checkstyle:check
    - mvn $MAVEN_CLI_OPTS spotbugs:check
  allow_failure: true

# 部署到測試環境
deploy-staging:
  stage: deploy
  script:
    - echo "部署到測試環境..."
    - mvn $MAVEN_CLI_OPTS package -DskipTests
    - scp target/*.jar user@staging-server:/opt/app/
    - ssh user@staging-server "sudo systemctl restart app"
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

# 部署到正式環境
deploy-production:
  stage: deploy
  script:
    - echo "部署到正式環境..."
    - mvn $MAVEN_CLI_OPTS package -DskipTests
    - scp target/*.jar user@prod-server:/opt/app/
    - ssh user@prod-server "sudo systemctl restart app"
  environment:
    name: production
    url: https://app.example.com
  only:
    - main
  when: manual  # 需要手動觸發
```

### 4.4 Java 專案 CI/CD 設定

#### ☕ Maven 專案設定

```yaml
# Java Maven 專案完整範例
image: maven:3.8.4-openjdk-17

variables:
  MAVEN_OPTS: >
    -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
    -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=WARN
    -Dorg.slf4j.simpleLogger.showDateTime=true
    -Djava.awt.headless=true
  MAVEN_CLI_OPTS: >
    --batch-mode
    --errors
    --fail-at-end
    --show-version
    -DinstallAtEnd=true
    -DdeployAtEnd=true

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .m2/repository/

stages:
  - validate
  - build
  - test
  - quality
  - package
  - deploy

# 驗證階段
validate:
  stage: validate
  script:
    - mvn $MAVEN_CLI_OPTS validate

# 編譯階段
compile:
  stage: build
  script:
    - mvn $MAVEN_CLI_OPTS compile
  artifacts:
    paths:
      - target/classes/
    expire_in: 1 hour

# 單元測試
unit-test:
  stage: test
  script:
    - mvn $MAVEN_CLI_OPTS test
  artifacts:
    reports:
      junit:
        - target/surefire-reports/TEST-*.xml
      coverage_report:
        coverage_format: jacoco
        path: target/site/jacoco/jacoco.xml
  coverage: '/Total.*?([0-9]{1,3})%/'

# 整合測試
integration-test:
  stage: test
  script:
    - mvn $MAVEN_CLI_OPTS verify -DskipUTs=true
  artifacts:
    reports:
      junit:
        - target/failsafe-reports/TEST-*.xml

# 程式碼品質檢查
code-quality:
  stage: quality
  script:
    - mvn $MAVEN_CLI_OPTS checkstyle:check
    - mvn $MAVEN_CLI_OPTS pmd:check
    - mvn $MAVEN_CLI_OPTS spotbugs:check
  artifacts:
    reports:
      codequality: target/checkstyle-result.xml

# 安全掃描
security-scan:
  stage: quality
  script:
    - mvn $MAVEN_CLI_OPTS org.owasp:dependency-check-maven:check
  artifacts:
    reports:
      dependency_scanning: target/dependency-check-report.xml
  allow_failure: true

# 打包
package:
  stage: package
  script:
    - mvn $MAVEN_CLI_OPTS package -DskipTests
  artifacts:
    paths:
      - target/*.jar
    expire_in: 1 week
  only:
    - main
    - develop
```

### 4.5 常用 CI/CD 指令

#### 🔧 Pipeline 管理

```bash
# 查看 Pipeline 狀態
# 在 GitLab Web 介面：專案 → CI/CD → Pipelines

# 手動觸發 Pipeline
# 在 GitLab Web 介面：CI/CD → Pipelines → Run Pipeline

# 重新執行失敗的工作
# 在 Pipeline 詳細頁面點選 "Retry" 按鈕
```

#### 📊 Pipeline 監控

```bash
# 檢查 Pipeline 執行時間
# GitLab → 專案 → Analytics → CI/CD Analytics

# 查看測試覆蓋率
# GitLab → 專案 → CI/CD → Jobs → test-job → Coverage

# 下載 Artifacts
# GitLab → 專案 → CI/CD → Jobs → 特定工作 → Download artifacts
```

### 4.6 本專案的 CI/CD 應用

#### 🎯 專案特定設定

```yaml
# 本專案的 .gitlab-ci.yml 設定重點

# Java 17 + Maven 環境
image: maven:3.8.4-openjdk-17

# 專案相關變數
variables:
  APP_NAME: "java-tutorial"
  APP_VERSION: "${CI_COMMIT_TAG:-${CI_COMMIT_SHORT_SHA}}"

# 分支策略對應的部署
deploy-rules:
  - if: '$CI_COMMIT_BRANCH == "main"'
    variables:
      DEPLOY_ENV: "production"
  - if: '$CI_COMMIT_BRANCH == "develop"'
    variables:
      DEPLOY_ENV: "staging"
  - if: '$CI_COMMIT_BRANCH =~ /^feature\/.*/'
    variables:
      DEPLOY_ENV: "development"
```

#### 📋 工作流程整合

1. **開發者推送程式碼** → 觸發 Pipeline
2. **自動建置和測試** → 確保程式碼品質
3. **Code Review 通過** → 合併到目標分支
4. **自動部署** → 根據分支策略部署到對應環境
5. **監控和回饋** → 持續改善流程

#### 💡 最佳實務建議

- **失敗快速回饋**：優先執行快速測試，儘早發現問題
- **並行執行**：合理使用 Pipeline 並行功能提升效率
- **環境一致性**：確保 CI/CD 環境與本地開發環境一致
- **日誌管理**：適當的日誌輸出幫助問題排查

---

## 5. 常見問題與解決方式

### 5.1 Merge 衝突處理

#### 🔥 衝突產生原因

- 多位開發者同時修改相同檔案的相同區域
- 分支長時間未同步主分支
- 自動合併無法判斷正確的變更

#### 🛠️ 衝突解決步驟

#### 步驟 1：識別衝突

```bash
# 拉取最新變更時出現衝突
git pull origin main
# Auto-merging src/main/java/com/example/Service.java
# CONFLICT (content): Merge conflict in src/main/java/com/example/Service.java
# Automatic merge failed; fix conflicts and then commit the result.

# 查看衝突狀態
git status
# On branch feature/my-feature
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#   (use "git merge --abort" to abort the merge)
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#         both modified:   src/main/java/com/example/Service.java
```

#### 步驟 2：解決衝突

```java
// 衝突檔案內容示例
public class UserService {
    
<<<<<<< HEAD (當前分支)
    public User createUser(String name, String email) {
        // 你的變更
        User user = new User(name, email);
        user.setCreatedAt(new Date());
        return userRepository.save(user);
    }
=======
    public User createUser(String username, String emailAddress) {
        // 其他人的變更
        User user = new User(username, emailAddress);
        user.setStatus(UserStatus.ACTIVE);
        return userRepository.save(user);
    }
>>>>>>> main (主分支)
}
```

#### 步驟 3：手動合併

```java
// 合併後的正確版本
public class UserService {
    
    public User createUser(String name, String email) {
        // 合併兩個版本的變更
        User user = new User(name, email);
        user.setCreatedAt(new Date());
        user.setStatus(UserStatus.ACTIVE);
        return userRepository.save(user);
    }
}
```

#### 步驟 4：完成合併

```bash
# 將解決的檔案加入暫存區
git add src/main/java/com/example/Service.java

# 檢查所有衝突是否已解決
git status

# 完成合併提交
git commit -m "resolve: 解決使用者服務類別的合併衝突"

# 推送變更
git push origin feature/my-feature
```

#### 🧰 衝突解決工具

##### Visual Studio Code

```bash
# 安裝 GitLens 擴充功能
# VS Code 內建三方合併工具
code .  # 開啟專案，VS Code 會顯示衝突標記
```

##### 命令列工具

```bash
# 設定合併工具
git config --global merge.tool vimdiff
# 或使用 VS Code
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# 使用合併工具
git mergetool
```

### 5.2 錯誤回復方式

#### ⏪ 常見回復場景

#### 場景 1：回復最後一次提交

```bash
# 保留檔案變更，只回復提交
git reset --soft HEAD~1

# 完全回復提交和檔案變更
git reset --hard HEAD~1

# 回復提交但保留檔案在工作目錄
git reset --mixed HEAD~1  # 預設行為
```

#### 場景 2：回復特定提交

```bash
# 查看提交歷史
git log --oneline
# abc123f feat: 新增使用者登入功能
# def456g fix: 修復密碼驗證錯誤
# ghi789h docs: 更新 README

# 回復到特定提交
git reset --hard def456g

# 或建立反向提交（推薦）
git revert abc123f
```

#### 場景 3：回復檔案變更

```bash
# 回復工作目錄的檔案變更
git checkout -- src/main/java/com/example/Service.java

# 回復暫存區的檔案
git reset HEAD src/main/java/com/example/Service.java

# 從特定提交回復檔案
git checkout def456g -- src/main/java/com/example/Service.java
```

#### 場景 4：回復推送的提交

```bash
# 方法1：使用 revert（推薦）
git revert abc123f
git push origin main

# 方法2：強制推送（危險，需團隊同意）
git reset --hard HEAD~1
git push --force-with-lease origin main
```

### 5.3 分支管理問題

#### 🌿 分支問題排解

#### 問題 1：分支無法切換

```bash
# 錯誤：工作目錄有未提交的變更
git checkout main
# error: Your local changes to the following files would be overwritten by checkout

# 解決方案1：暫存變更
git stash
git checkout main
git stash pop  # 回到原分支後執行

# 解決方案2：提交變更
git add .
git commit -m "wip: 暫存工作進度"
git checkout main
```

#### 問題 2：分支追蹤錯誤

```bash
# 查看分支追蹤狀態
git branch -vv

# 設定上游分支
git branch --set-upstream-to=origin/feature/my-feature

# 或在推送時設定
git push -u origin feature/my-feature
```

#### 問題 3：刪除本地和遠端分支

```bash
# 刪除本地分支
git branch -d feature/completed-feature

# 強制刪除本地分支
git branch -D feature/abandoned-feature

# 刪除遠端分支
git push origin --delete feature/completed-feature

# 清理本地對遠端分支的參照
git remote prune origin
```

### 5.4 權限和認證問題

#### 🔐 常見認證問題

#### 問題 1：HTTPS 認證失敗

```bash
# 更新認證資訊
git config --global credential.helper store
git pull  # 會提示輸入使用者名稱和密碼

# 使用 Personal Access Token
# GitLab → User Settings → Access Tokens
# 生成 token 後當作密碼使用
```

#### 問題 2：SSH Key 設定

```bash
# 生成 SSH Key
ssh-keygen -t ed25519 -C "your.email@company.com"

# 複製公鑰到 GitLab
cat ~/.ssh/id_ed25519.pub
# 將內容貼到 GitLab → User Settings → SSH Keys

# 測試連線
ssh -T git@gitlab.company.com
```

#### 問題 3：權限不足

```bash
# 檢查專案權限
# GitLab → 專案 → Settings → Members

# 請求權限提升
# 聯繫專案維護者或管理員
```

### 5.5 效能和同步問題

#### ⚡ 效能優化

#### 問題 1：Clone 速度慢

```bash
# 淺層 Clone（只取最新提交）
git clone --depth 1 https://gitlab.company.com/project.git

# 後續需要完整歷史時
git fetch --unshallow
```

#### 問題 2：大檔案問題

```bash
# 使用 Git LFS 處理大檔案
git lfs install
git lfs track "*.jar"
git lfs track "*.war"
git add .gitattributes
git commit -m "chore: 設定 Git LFS 追蹤大檔案"
```

#### 問題 3：本地快取問題

```bash
# 清理無效的遠端分支參照
git remote prune origin

# 清理無效的本地分支
git branch --merged | grep -v "\*\|main\|develop" | xargs -n 1 git branch -d

# 垃圾回收和優化
git gc --aggressive
git repack -ad
```

### 5.6 CI/CD Pipeline 問題

#### 🔧 Pipeline 故障排除

#### 問題 1：Pipeline 失敗

```bash
# 檢查失敗的工作日誌
# GitLab → CI/CD → Pipelines → 點選失敗的 Pipeline → 點選失敗的 Job

# 常見失敗原因：
# - 測試失敗：檢查測試程式碼
# - 建置失敗：檢查相依性和設定
# - 部署失敗：檢查環境設定和權限
```

#### 問題 2：Runner 無法使用

```bash
# 檢查 Runner 狀態
# GitLab → Admin → Runners
# 或專案層級：Settings → CI/CD → Runners

# 重新註冊 Runner
sudo gitlab-runner register
```

#### 問題 3：變數設定錯誤

```bash
# 檢查 CI/CD 變數
# GitLab → 專案 → Settings → CI/CD → Variables

# 確認變數範圍：
# - Project level（專案層級）
# - Group level（群組層級）
# - Instance level（實例層級）
```

### 5.7 團隊協作問題

#### 👥 協作障礙解決

#### 問題 1：Merge Request 衝突

```bash
# 在本地解決衝突後更新 MR
git checkout feature/my-feature
git fetch origin
git rebase origin/main
# 解決衝突後
git push --force-with-lease origin feature/my-feature
```

#### 問題 2：Code Review 意見分歧

**解決策略**：

1. **技術討論**：在 MR 中詳細解釋設計決策
2. **離線溝通**：必要時進行面對面討論
3. **團隊共識**：遵循團隊既定的編碼規範
4. **妥協方案**：尋求雙方都能接受的解決方案

#### 問題 3：分支策略混亂

**預防措施**：

- 建立清楚的分支命名規範
- 定期清理過期分支
- 使用 GitLab 的分支保護功能
- 團隊培訓和文件化流程

#### 💡 問題預防建議

- **定期同步**：每日開始工作前先 `git pull`
- **小步提交**：避免一次性大量變更
- **描述清楚**：提供詳細的提交和 MR 描述
- **主動溝通**：遇到問題及時向團隊求助

---

## 6. 開發最佳實務建議

### 6.1 程式碼管理最佳實務

#### 📝 提交原則

##### 原子性提交

```bash
# ✅ 好的提交：單一功能
git commit -m "feat: 新增使用者登入驗證功能"

# ❌ 壞的提交：混合多個功能
git commit -m "feat: 新增登入功能、修復密碼錯誤、更新文件"
```

##### 提交頻率

- **每日至少一次**：確保工作進度不會遺失
- **功能完成時**：完整的功能點或修復
- **重大重構前**：保留重構前的可工作版本

##### 提交訊息品質

```bash
# ✅ 優質提交訊息
git commit -m "feat(auth): 實作 JWT 令牌驗證機制

- 新增 JwtTokenProvider 類別
- 實作令牌生成和驗證邏輯
- 新增令牌過期處理機制
- 更新安全設定配置

Fixes #123"

# ❌ 品質不佳的提交訊息
git commit -m "fix"
git commit -m "更新一些東西"
git commit -m "WIP"
```

#### 🌿 分支管理策略

##### 分支生命週期

```text
分支生命週期管理：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  創建分支     │ →  │  開發階段     │ →  │  合併關閉     │
│             │    │             │    │             │
│ • 從develop  │    │ • 定期同步   │    │ • Code Review│
│   分支建立   │    │ • 小步提交   │    │ • 測試通過   │
│ • 命名規範   │    │ • 功能測試   │    │ • 刪除分支   │
└─────────────┘    └─────────────┘    └─────────────┘
```

##### 分支維護

```bash
# 定期同步主分支
git checkout feature/my-feature
git fetch origin
git rebase origin/develop

# 清理已合併的本地分支
git branch --merged | grep -v "\*\|main\|develop" | xargs -n 1 git branch -d

# 查看遠端分支狀態
git remote show origin
```

### 6.2 Code Review 最佳實務

#### 👀 審查者角度

##### 審查重點

1. **功能正確性**

```java
// ✅ 檢查邊界條件
public List<User> getUsers(int page, int size) {
    if (page < 0 || size <= 0 || size > 100) {
        throw new IllegalArgumentException("Invalid pagination parameters");
    }
    // ...
}

// ❌ 缺少參數驗證
public List<User> getUsers(int page, int size) {
    return userRepository.findAll(PageRequest.of(page, size));
}
```

2. **安全性檢查**

```java
// ✅ 防止 SQL 注入
@Query("SELECT u FROM User u WHERE u.email = :email")
User findByEmail(@Param("email") String email);

// ❌ 存在 SQL 注入風險
@Query("SELECT u FROM User u WHERE u.email = '" + email + "'")
User findByEmail(String email);
```

3. **效能考量**

```java
// ✅ 批次處理
public void updateUsers(List<User> users) {
    userRepository.saveAll(users);  // 批次儲存
}

// ❌ 逐一處理
public void updateUsers(List<User> users) {
    for (User user : users) {
        userRepository.save(user);  // 效能較差
    }
}
```

#### 📝 審查意見表達

##### 建設性意見

```markdown
**✅ 建設性的 Review 意見**

「建議將這個方法拆分為更小的函式，提高可讀性和可測試性。例如：

\`\`\`java
public User createUser(UserDto dto) {
    validateUserData(dto);
    User user = mapToEntity(dto);
    return saveUser(user);
}
\`\`\`

**❌ 不具建設性的意見**

「這個方法太長了，請修改。」
```

##### 意見分類

- **🔴 Must Fix**：必須修正的問題（安全、功能錯誤）
- **🟡 Should Fix**：建議修正的問題（效能、可讀性）
- **🟢 Nice to Have**：可選的改善建議

#### 👨‍💻 被審查者角度

##### 回應策略

```markdown
# ✅ 積極回應
感謝建議！我已經按照您的建議重構了這個方法，並新增了相關的單元測試。

# 🔍 解釋設計決策
這裡我選擇使用快取機制是因為這個 API 會被頻繁調用，經過測試可以提升 60% 的效能。

# ❌ 消極回應
好的。
沒問題。
```

### 6.3 測試最佳實務

#### 🧪 測試策略

##### 測試金字塔

```text
測試金字塔：
        ┌─────────────┐
        │   E2E Tests │  ← 少量，高價值
        │   (端到端)   │
        ├─────────────┤
        │Integration  │  ← 適量，關鍵路徑
        │   Tests     │
        ├─────────────┤
        │ Unit Tests  │  ← 大量，快速回饋
        │  (單元測試)  │
        └─────────────┘
```

##### 單元測試實例

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    @DisplayName("應該成功建立新使用者")
    void shouldCreateUserSuccessfully() {
        // Given
        UserDto userDto = new UserDto("john@example.com", "John Doe");
        User expectedUser = new User("john@example.com", "John Doe");
        when(userRepository.save(any(User.class))).thenReturn(expectedUser);
        
        // When
        User result = userService.createUser(userDto);
        
        // Then
        assertThat(result.getEmail()).isEqualTo("john@example.com");
        assertThat(result.getName()).isEqualTo("John Doe");
        verify(userRepository).save(any(User.class));
    }
    
    @Test
    @DisplayName("當信箱已存在時應該拋出例外")
    void shouldThrowExceptionWhenEmailExists() {
        // Given
        UserDto userDto = new UserDto("john@example.com", "John Doe");
        when(userRepository.existsByEmail("john@example.com")).thenReturn(true);
        
        // When & Then
        assertThatThrownBy(() -> userService.createUser(userDto))
            .isInstanceOf(EmailAlreadyExistsException.class)
            .hasMessage("信箱已被使用: john@example.com");
    }
}
```

### 6.4 安全性最佳實務

#### 🔒 程式碼安全

##### 敏感資料管理

```yaml
# ✅ 使用環境變數
spring:
  datasource:
    url: ${DB_URL:jdbc:h2:mem:testdb}
    username: ${DB_USERNAME:sa}
    password: ${DB_PASSWORD:}

# ❌ 硬編碼敏感資料
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/prod
    username: admin
    password: admin123
```

##### 輸入驗證

```java
// ✅ 完整的輸入驗證
@RestController
public class UserController {
    
    @PostMapping("/users")
    public ResponseEntity<User> createUser(@Valid @RequestBody UserDto userDto) {
        // @Valid 會自動驗證 UserDto 的約束條件
        User user = userService.createUser(userDto);
        return ResponseEntity.ok(user);
    }
}

@Data
public class UserDto {
    @NotBlank(message = "信箱不能為空")
    @Email(message = "信箱格式不正確")
    private String email;
    
    @NotBlank(message = "姓名不能為空")
    @Size(min = 2, max = 50, message = "姓名長度必須在 2-50 字元之間")
    private String name;
}
```

##### 權限控制

```java
// ✅ 細緻的權限控制
@RestController
@RequestMapping("/api/admin")
@PreAuthorize("hasRole('ADMIN')")
public class AdminController {
    
    @GetMapping("/users")
    @PreAuthorize("hasAuthority('USER_READ')")
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }
    
    @DeleteMapping("/users/{id}")
    @PreAuthorize("hasAuthority('USER_DELETE')")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.ok().build();
    }
}
```

### 6.5 效能最佳實務

#### ⚡ 程式碼效能

##### 資料庫查詢優化

```java
// ✅ 使用投影和分頁
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    @Query("SELECT new com.example.dto.UserSummaryDto(u.id, u.name, u.email) " +
           "FROM User u WHERE u.active = true")
    Page<UserSummaryDto> findActiveUserSummaries(Pageable pageable);
    
    // 使用 @EntityGraph 避免 N+1 查詢
    @EntityGraph(attributePaths = {"roles", "profile"})
    Optional<User> findWithRolesAndProfileById(Long id);
}

// ❌ 查詢過多資料
public List<User> getAllUsers() {
    return userRepository.findAll(); // 可能返回大量資料
}
```

##### 快取策略

```java
// ✅ 適當使用快取
@Service
@CacheConfig(cacheNames = "users")
public class UserService {
    
    @Cacheable(key = "#id")
    public User getUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    @CacheEvict(key = "#user.id")
    public User updateUser(User user) {
        return userRepository.save(user);
    }
    
    @CacheEvict(allEntries = true)
    public void clearAllUsersCache() {
        // 清空所有使用者快取
    }
}
```

### 6.6 文件化最佳實務

#### 📚 程式碼文件

##### API 文件

```java
// ✅ 完整的 API 文件
@RestController
@RequestMapping("/api/users")
@Api(tags = "使用者管理", description = "使用者相關操作的 API")
public class UserController {
    
    @PostMapping
    @ApiOperation(value = "建立新使用者", notes = "建立一個新的使用者帳號")
    @ApiResponses({
        @ApiResponse(code = 201, message = "使用者建立成功"),
        @ApiResponse(code = 400, message = "請求參數錯誤"),
        @ApiResponse(code = 409, message = "信箱已存在")
    })
    public ResponseEntity<User> createUser(
        @ApiParam(value = "使用者資訊", required = true) 
        @Valid @RequestBody UserDto userDto) {
        
        User user = userService.createUser(userDto);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

##### JavaDoc 規範

```java
/**
 * 使用者服務類別，提供使用者相關的業務邏輯處理
 * 
 * @author 開發者姓名
 * @version 1.0
 * @since 2024-01-01
 */
@Service
@Transactional
public class UserService {
    
    /**
     * 根據 ID 查詢使用者
     * 
     * @param id 使用者 ID，不能為 null
     * @return 使用者實體
     * @throws UserNotFoundException 當使用者不存在時拋出
     * @throws IllegalArgumentException 當 ID 為 null 時拋出
     * @see User
     * @since 1.0
     */
    public User getUserById(@NonNull Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("使用者不存在: " + id));
    }
}
```

### 6.7 團隊協作最佳實務

#### 🤝 溝通協作

##### 技術決策文件

```markdown
# 技術決策記錄 (ADR-001): 選擇 Spring Boot 作為主要框架

### 狀態
接受

### 背景
需要選擇後端開發框架來建置企業級應用程式

### 決策
選擇 Spring Boot 2.7.x 作為主要後端框架

### 理由
- 豐富的生態系統和社群支援
- 優秀的自動設定功能
- 內建測試支援
- 團隊已有相關經驗

### 後果
- 學習曲線相對平緩
- 可快速啟動專案開發
- 需要定期更新相依性
```

##### 會議記錄

```markdown
# 技術 Review 會議記錄 - 2024/01/15

### 參與者
- 架構師：張三
- 後端開發：李四、王五
- 前端開發：趙六

### 討論議題
1. 使用者認證機制設計
2. API 設計規範
3. 資料庫設計檢討

### 決議事項
- [ ] 採用 JWT + Refresh Token 認證機制
- [ ] API 遵循 RESTful 設計原則
- [ ] 資料庫新增使用者活動記錄表

### 行動項目
- 李四：完成認證模組實作 (2024/01/20)
- 王五：更新 API 文件 (2024/01/18)
- 趙六：調整前端認證流程 (2024/01/22)
```

#### 📈 持續改善

##### 回顧會議

```markdown
# Sprint 回顧 - Week 3

### 做得好的地方
- Code Review 品質提升
- CI/CD Pipeline 穩定運行
- 團隊溝通更加順暢

### 需要改善的地方
- 測試覆蓋率需要提升
- 文件更新不夠及時
- 技術債務累積

### 改善行動
1. 設定測試覆蓋率目標為 80%
2. MR 必須包含文件更新
3. 每週分配 20% 時間處理技術債務
```

---

## 7. 檢查清單

### 7.1 新進同仁入門檢查清單

#### 🚀 環境設定

- [ ] **Git 安裝與設定**
  - [ ] 安裝 Git 並驗證版本：`git --version`
  - [ ] 設定使用者資訊：`git config --global user.name` 和 `user.email`
  - [ ] 設定編輯器：`git config --global core.editor`
  - [ ] 設定換行符號處理：`git config --global core.autocrlf true` (Windows)

- [ ] **GitLab 帳號設定**
  - [ ] 建立 GitLab 帳號
  - [ ] 設定 SSH Key 或確認 HTTPS 認證
  - [ ] 測試連線：`ssh -T git@gitlab.company.com` 或 Clone 測試專案
  - [ ] 加入專案團隊並確認權限

- [ ] **開發工具設定**
  - [ ] 安裝 VS Code 或慣用的 IDE
  - [ ] 安裝必要的擴充功能（GitLens、Checkstyle 等）
  - [ ] 設定程式碼格式化規則
  - [ ] 設定 Git 整合

#### 📚 學習與理解

- [ ] **文件閱讀**
  - [ ] 閱讀專案 README.md
  - [ ] 理解專案架構和技術棧
  - [ ] 熟悉專案的分支策略
  - [ ] 閱讀程式碼規範文件

- [ ] **流程熟悉**
  - [ ] 理解 Git Flow 分支模型
  - [ ] 熟悉 Commit Message 規範
  - [ ] 了解 Merge Request 流程
  - [ ] 了解 Code Review 標準

### 7.2 日常開發檢查清單

#### 🌅 開始工作

- [ ] **每日同步**
  - [ ] 切換到 develop 分支：`git checkout develop`
  - [ ] 拉取最新變更：`git pull origin develop`
  - [ ] 檢查是否有新的分支或標籤
  - [ ] 確認本地工作目錄乾淨：`git status`

- [ ] **分支管理**
  - [ ] 從最新的 develop 建立功能分支
  - [ ] 使用正確的分支命名規範
  - [ ] 設定上游分支：`git push -u origin feature/branch-name`

#### 💻 開發過程

- [ ] **程式碼品質**
  - [ ] 遵循專案的編碼規範
  - [ ] 確保程式碼可以正常編譯
  - [ ] 執行單元測試並確保通過
  - [ ] 執行程式碼靜態分析

- [ ] **提交實務**
  - [ ] 使用原子性提交（每次提交一個邏輯變更）
  - [ ] 遵循 Commit Message 規範
  - [ ] 避免提交敏感資訊（密碼、API Key 等）
  - [ ] 提交前檢查差異：`git diff --staged`

#### 🔄 提交和推送

- [ ] **提交前檢查**
  - [ ] 檢查提交內容：`git status` 和 `git diff`
  - [ ] 確保測試通過：`mvn test`
  - [ ] 檢查程式碼格式：`mvn checkstyle:check`
  - [ ] 確認沒有 TODO 或 FIXME 標記

- [ ] **推送流程**
  - [ ] 推送到遠端分支：`git push origin feature/branch-name`
  - [ ] 檢查 CI/CD Pipeline 狀態
  - [ ] 處理任何建置或測試失敗

### 7.3 Merge Request 檢查清單

#### 📝 建立 MR

- [ ] **MR 準備**
  - [ ] 確保分支基於最新的 develop
  - [ ] 解決與目標分支的衝突
  - [ ] 確認所有提交都是必要的
  - [ ] 壓縮或整理提交歷史（如需要）

- [ ] **MR 資訊**
  - [ ] 填寫清楚的標題和描述
  - [ ] 使用 MR 描述模板
  - [ ] 標記相關的 Issue
  - [ ] 指派適當的審查者
  - [ ] 設定適當的標籤

#### 👀 Code Review

- [ ] **自我檢查**
  - [ ] 進行自我 Code Review
  - [ ] 確認變更範圍合理
  - [ ] 檢查是否需要更新文件
  - [ ] 確認測試覆蓋率足夠

- [ ] **回應審查**
  - [ ] 及時回應審查意見
  - [ ] 積極討論設計決策
  - [ ] 修正所有必要的問題
  - [ ] 感謝審查者的意見

### 7.4 CI/CD 檢查清單

#### 🔧 Pipeline 監控

- [ ] **建置檢查**
  - [ ] 確認 Pipeline 成功執行
  - [ ] 檢查建置日誌是否有警告
  - [ ] 確認測試都通過
  - [ ] 檢查程式碼品質報告

- [ ] **部署檢查**
  - [ ] 確認部署到測試環境成功
  - [ ] 進行冒煙測試
  - [ ] 檢查應用程式健康狀態
  - [ ] 驗證核心功能正常

#### 🚨 問題處理

- [ ] **失敗處理**
  - [ ] 查看失敗的工作日誌
  - [ ] 識別失敗根本原因
  - [ ] 修正問題並重新執行
  - [ ] 通知相關團隊成員

### 7.5 發布檢查清單

#### 🎯 發布準備

- [ ] **發布前檢查**
  - [ ] 所有功能測試通過
  - [ ] 效能測試完成
  - [ ] 安全掃描無高風險問題
  - [ ] 文件已更新

- [ ] **發布執行**
  - [ ] 備份生產環境資料
  - [ ] 執行部署腳本
  - [ ] 驗證部署成功
  - [ ] 執行回歸測試

#### 🔙 發布後

- [ ] **監控檢查**
  - [ ] 監控應用程式效能
  - [ ] 檢查錯誤日誌
  - [ ] 確認使用者回饋
  - [ ] 準備回滾計畫（如需要）

### 7.6 緊急情況檢查清單

#### 🚨 生產問題

- [ ] **立即回應**
  - [ ] 評估問題嚴重程度
  - [ ] 通知相關團隊
  - [ ] 啟動緊急回應流程
  - [ ] 記錄問題時間軸

- [ ] **問題解決**
  - [ ] 建立 hotfix 分支
  - [ ] 快速修復問題
  - [ ] 執行緊急測試
  - [ ] 部署修復版本

#### 📊 事後檢討

- [ ] **問題分析**
  - [ ] 分析問題根本原因
  - [ ] 記錄解決過程
  - [ ] 識別改善機會
  - [ ] 更新流程文件

### 7.7 定期維護檢查清單

#### 🧹 每週維護

- [ ] **分支清理**
  - [ ] 刪除已合併的功能分支
  - [ ] 清理過期的遠端分支參照
  - [ ] 檢查長時間未更新的分支

- [ ] **效能檢查**
  - [ ] 檢查 CI/CD Pipeline 執行時間
  - [ ] 檢查測試執行效率
  - [ ] 檢查建置快取效果

#### 📈 每月檢討

- [ ] **團隊回顧**
  - [ ] 檢討開發流程效率
  - [ ] 分析常見問題
  - [ ] 討論改善建議
  - [ ] 更新最佳實務

---

## 📞 聯絡資訊

### 技術支援

- **GitLab 管理員**：<admin@company.com>
- **DevOps 團隊**：<devops@company.com>
- **技術支援熱線**：分機 1234

### 團隊協作

- **Slack 頻道**：#dev-team、#gitlab-support
- **團隊會議**：每週三 14:00-15:00
- **技術分享**：每月第一個週五

---

## 📚 參考資源

### 官方文件

- [GitLab 官方文件](https://docs.gitlab.com/)
- [Git 官方文件](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)

### 學習資源

- [Pro Git 電子書](https://git-scm.com/book)
- [GitLab CI/CD 教學](https://docs.gitlab.com/ee/ci/)
- [Git Flow 工作流程](https://nvie.com/posts/a-successful-git-branching-model/)

### 工具推薦

- [GitKraken](https://www.gitkraken.com/) - Git GUI 工具
- [Sourcetree](https://www.sourcetreeapp.com/) - 免費 Git GUI
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - VS Code 擴充功能

---

---

## 8. 進階功能與整合

### 8.1 GitLab API 整合

#### 🔗 REST API 使用

**認證方式**：

```bash
# 使用 Personal Access Token
curl --header "PRIVATE-TOKEN: your-token" \
     "https://gitlab.company.com/api/v4/projects"

# 使用 OAuth Token
curl --header "Authorization: Bearer your-oauth-token" \
     "https://gitlab.company.com/api/v4/projects"
```

**常用 API 範例**：

```bash
# 取得專案清單
curl --header "PRIVATE-TOKEN: your-token" \
     "https://gitlab.company.com/api/v4/projects?membership=true"

# 建立新 Issue
curl --request POST \
     --header "PRIVATE-TOKEN: your-token" \
     --header "Content-Type: application/json" \
     --data '{"title":"New Bug Report","description":"Bug description"}' \
     "https://gitlab.company.com/api/v4/projects/123/issues"

# 取得 Merge Request 清單
curl --header "PRIVATE-TOKEN: your-token" \
     "https://gitlab.company.com/api/v4/projects/123/merge_requests?state=opened"
```

#### 📊 Webhook 整合

**Webhook 設定**：

```json
{
  "url": "https://your-service.com/webhook",
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "wiki_page_events": true,
  "deployment_events": true,
  "job_events": true,
  "pipeline_events": true,
  "release_events": true
}
```

**Webhook 處理範例**：

```java
@RestController
@RequestMapping("/webhook")
@Slf4j
public class GitLabWebhookController {
    
    @PostMapping("/push")
    public ResponseEntity<String> handlePushEvent(
            @RequestHeader("X-Gitlab-Event") String event,
            @RequestBody Map<String, Object> payload) {
        
        log.info("收到 GitLab 事件: {}", event);
        
        if ("Push Hook".equals(event)) {
            String projectName = (String) ((Map) payload.get("project")).get("name");
            String ref = (String) payload.get("ref");
            log.info("專案 {} 的分支 {} 有新的 Push", projectName, ref);
            
            // 處理 Push 事件邏輯
            processPushEvent(payload);
        }
        
        return ResponseEntity.ok("處理完成");
    }
}
```

### 8.2 第三方工具整合

#### 🔧 IDE 整合

**VS Code 擴充功能**：

- **GitLab Workflow**：直接在 VS Code 中管理 Issue 和 MR
- **GitLens**：增強的 Git 功能
- **GitLab CI**：CI/CD 管道可視化

**IntelliJ IDEA 整合**：

```text
GitLab 外掛功能：
├── Clone 專案
├── 建立 Merge Request
├── 檢視 CI/CD 狀態
├── Issue 管理
└── Code Review
```

#### 📱 Slack 整合

**Slack 通知設定**：

```yaml
# .gitlab-ci.yml Slack 通知
variables:
  SLACK_WEBHOOK: "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"

notify-slack:
  stage: notify
  script:
    - |
      curl -X POST -H 'Content-type: application/json' \
      --data "{'text':'✅ Pipeline 成功完成: $CI_PROJECT_NAME ($CI_COMMIT_REF_NAME)'}" \
      $SLACK_WEBHOOK
  only:
    - main
  when: on_success

notify-slack-failure:
  stage: notify
  script:
    - |
      curl -X POST -H 'Content-type: application/json' \
      --data "{'text':'❌ Pipeline 失敗: $CI_PROJECT_NAME ($CI_COMMIT_REF_NAME)'}" \
      $SLACK_WEBHOOK
  only:
    - main
  when: on_failure
```

#### 🎫 Jira 整合

**Issue 關聯**：

```bash
# Commit message 關聯 Jira Issue
git commit -m "feat: 新增使用者登入功能

實作使用者登入驗證和 JWT Token 機制

PROJ-123"
```

**自動化工作流程**：

```text
Jira-GitLab 整合流程：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Jira Issue  │ →  │ GitLab MR   │ →  │ 自動更新     │
│ 建立        │    │ 關聯        │    │ Issue 狀態   │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 8.3 自動化與 DevOps

#### 🔄 GitOps 實踐

**GitOps 工作流程**：

```yaml
# .gitlab-ci.yml GitOps 部署
deploy-to-k8s:
  stage: deploy
  image: alpine/k8s:latest
  script:
    - echo "部署到 Kubernetes 集群"
    - kubectl apply -f k8s/
    - kubectl rollout status deployment/app-deployment
  environment:
    name: production
    url: https://app.example.com
  only:
    - main
```

**ArgoCD 整合**：

```yaml
# argocd-application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: java-tutorial-app
spec:
  project: default
  source:
    repoURL: https://gitlab.company.com/team/java-tutorial.git
    targetRevision: main
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

#### 📈 監控整合

**Prometheus + Grafana**：

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'gitlab-ci'
    static_configs:
      - targets: ['gitlab.company.com:9090']
    metrics_path: /metrics
    params:
      token: ['your-prometheus-token']
```

**應用程式監控**：

```java
// Spring Boot Actuator 整合
@RestController
public class MetricsController {
    
    private final MeterRegistry meterRegistry;
    
    @GetMapping("/api/users")
    public List<User> getUsers() {
        return Timer.Sample.start(meterRegistry)
            .stop(meterRegistry.timer("api.users.duration"))
            .recordCallable(() -> userService.getAllUsers());
    }
}
```

### 8.4 安全性進階設定

#### 🔐 進階權限管理

**分支保護規則**：

```text
主分支保護設定：
├── 推送權限：僅 Maintainer 以上
├── Merge Request 必要：是
├── 至少 2 位審查者：是
├── Pipeline 必須成功：是
├── 解決所有討論：是
└── 快進合併限制：是
```

**自動安全掃描**：

```yaml
# .gitlab-ci.yml 完整安全掃描
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml
  - template: Security/License-Scanning.gitlab-ci.yml
  - template: Security/Container-Scanning.gitlab-ci.yml

variables:
  SECURE_ANALYZERS_PREFIX: "registry.gitlab.com/gitlab-org/security-products/analyzers"
  SAST_EXCLUDED_ANALYZERS: "gosec,bandit"
  
security-scan:
  stage: test
  allow_failure: false
  artifacts:
    reports:
      sast: gl-sast-report.json
      dependency_scanning: gl-dependency-scanning-report.json
      secret_detection: gl-secret-detection-report.json
```

#### 🛡️ 合規性管理

**稽核日誌**：

- **使用者操作記錄**：登入、權限變更、專案存取
- **程式碼變更追蹤**：提交、分支、標籤操作
- **系統管理記錄**：設定變更、使用者管理

**資料保護**：

```yaml
# 資料備份策略
backup-policy:
  schedule: "0 2 * * *"  # 每日凌晨 2 點
  retention: "30d"       # 保留 30 天
  encryption: "AES-256"  # 加密儲存
  locations:
    - "s3://backup-bucket/gitlab"
    - "local://backup/gitlab"
```

### 8.5 效能優化

#### ⚡ Repository 效能優化

**大型檔案管理**：

```bash
# 設定 Git LFS
git lfs install
git lfs track "*.jar"
git lfs track "*.war"
git lfs track "*.pdf"
git lfs track "docs/*.png"

# 檢視 LFS 檔案
git lfs ls-files

# 清理 LFS 快取
git lfs prune
```

**Repository 清理**：

```bash
# 清理無效參照
git remote prune origin

# 垃圾回收
git gc --aggressive --prune=now

# 檢查 Repository 大小
git count-objects -vH
```

#### 🚀 CI/CD 效能優化

**Docker 層快取**：

```yaml
# .gitlab-ci.yml Docker 快取優化
build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build 
      --cache-from $CI_REGISTRY_IMAGE:latest 
      --tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA 
      --tag $CI_REGISTRY_IMAGE:latest .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
```

**並行作業**：

```yaml
# 並行測試執行
test:unit:
  stage: test
  script: mvn test -Dtest="**/unit/**"
  parallel: 3

test:integration:
  stage: test
  script: mvn test -Dtest="**/integration/**"
  parallel: 2
```

### 8.6 災難恢復

#### 🔄 備份策略

**自動化備份**：

```bash
#!/bin/bash
# gitlab-backup.sh

# 建立應用程式備份
gitlab-backup create

# 備份設定檔
tar -czf /backup/gitlab-config-$(date +%Y%m%d).tar.gz /etc/gitlab/

# 上傳到雲端儲存
aws s3 sync /var/opt/gitlab/backups/ s3://gitlab-backups/app/
aws s3 sync /backup/ s3://gitlab-backups/config/

# 清理舊備份（保留 30 天）
find /var/opt/gitlab/backups/ -name "*.tar" -mtime +30 -delete
```

#### 🆘 災難恢復流程

**恢復步驟**：

1. **評估損害程度**
2. **準備恢復環境**
3. **恢復應用程式資料**
4. **恢復設定檔**
5. **驗證系統功能**
6. **通知使用者**

**恢復指令**：

```bash
# 停止 GitLab 服務
gitlab-ctl stop puma
gitlab-ctl stop sidekiq

# 恢復備份
gitlab-backup restore BACKUP=backup-timestamp

# 恢復設定檔
tar -xzf gitlab-config-backup.tar.gz -C /

# 重新設定權限
gitlab-ctl reconfigure

# 啟動服務
gitlab-ctl start
```

### 8.7 GitLab Runner 深度配置

#### 🏃‍♂️ Runner 架構深入理解

**Runner 執行流程**：

```text
GitLab CI/CD 執行流程：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Git Push    │ →  │ Pipeline    │ →  │ Runner      │ →  │ Job         │
│ 觸發        │    │ 建立        │    │ 接收工作     │    │ 執行        │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Runner 類型詳解**：

| Runner 類型 | 用途 | 優缺點 | 適用場景 |
|------------|------|--------|---------|
| Shared Runners | 多專案共用 | 成本低，但可能排隊 | 小型專案、測試環境 |
| Group Runners | 群組專用 | 平衡成本和效能 | 團隊專案 |
| Project Runners | 專案專用 | 效能最佳，成本較高 | 大型專案、生產環境 |

#### 🔧 Runner 進階配置

**詳細配置檔範例**：

```toml
# /etc/gitlab-runner/config.toml
concurrent = 4
check_interval = 0
session_timeout = 1800

[session_server]
  session_timeout = 1800

[[runners]]
  name = "docker-runner-production"
  url = "https://gitlab.company.com/"
  token = "xxx"
  executor = "docker"
  
  [runners.custom_build_dir]
  [runners.cache]
    Type = "s3"
    Path = "cache"
    Shared = false
    [runners.cache.s3]
      ServerAddress = "s3.amazonaws.com"
      BucketName = "gitlab-ci-cache"
      BucketLocation = "us-east-1"
      Insecure = false
      
  [runners.docker]
    tls_verify = false
    image = "alpine:latest"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache", "/var/run/docker.sock:/var/run/docker.sock:rw"]
    shm_size = 0
    pull_policy = "if-not-present"
    
    # 資源限制
    cpus = "2.0"
    memory = "4g"
    
    # 網路設定
    network_mode = "bridge"
    
    # 安全設定
    security_opt = ["seccomp:unconfined"]
```

**多環境 Runner 配置**：

```bash
# 開發環境 Runner 註冊
sudo gitlab-runner register \
  --url https://gitlab.company.com/ \
  --registration-token DEV_TOKEN \
  --description "Development Runner" \
  --tag-list "dev,docker,java-11" \
  --executor docker \
  --docker-image maven:3.8.4-openjdk-11 \
  --docker-volumes /var/run/docker.sock:/var/run/docker.sock

# 生產環境 Runner 註冊
sudo gitlab-runner register \
  --url https://gitlab.company.com/ \
  --registration-token PROD_TOKEN \
  --description "Production Runner" \
  --tag-list "prod,kubernetes,java-17" \
  --executor kubernetes \
  --kubernetes-namespace gitlab-runner
```

#### 🐳 Docker Executor 優化

**最佳化的 Docker 配置**：

```yaml
# .gitlab-ci.yml Docker 優化
variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"

cache:
  key: "$CI_COMMIT_REF_SLUG"
  paths:
    - .m2/repository/
    - target/

build:
  stage: build
  image: maven:3.8.4-openjdk-17-slim
  services:
    - docker:20.10.16-dind
  before_script:
    - docker info
  script:
    - mvn clean compile
  artifacts:
    paths:
      - target/
    expire_in: 1 hour
```

#### ☸️ Kubernetes Executor 配置

**Kubernetes Runner 設定**：

```yaml
# kubernetes-runner.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gitlab-runner-config
data:
  config.toml: |
    [[runners]]
      name = "kubernetes-runner"
      url = "https://gitlab.company.com/"
      token = "xxx"
      executor = "kubernetes"
      
      [runners.kubernetes]
        namespace = "gitlab-runner"
        image = "alpine:latest"
        cpu_limit = "2"
        memory_limit = "4Gi"
        service_cpu_limit = "1"
        service_memory_limit = "2Gi"
        helper_cpu_limit = "500m"
        helper_memory_limit = "100Mi"
        
        # 節點選擇器
        node_selector = {"gitlab-runner" = "true"}
        
        # 污點容忍
        [[runners.kubernetes.node_tolerations]]
          key = "gitlab-runner"
          operator = "Equal"
          value = "true"
          effect = "NoSchedule"
```

### 8.8 多環境部署策略

#### 🌍 環境規劃架構

**標準環境配置**：

```text
環境架構圖：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Development │ →  │   Testing   │ →  │   Staging   │ →  │ Production  │
│ 開發環境      │    │   測試環境   │    │   預產環境   │    │   正式環境   │
│             │    │             │    │             │    │             │
│ • 快速迭代   │    │ • 自動測試   │    │ • 效能測試   │    │ • 高可用性   │
│ • 功能驗證   │    │ • 整合測試   │    │ • 使用者驗收  │    │ • 監控告警   │
│ • 除錯修復   │    │ • 迴歸測試   │    │ • 最終確認   │    │ • 災難恢復   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

#### 📋 環境配置管理

**配置檔分層管理**：

```yaml
# .gitlab-ci.yml 多環境配置
variables:
  SPRING_PROFILES_ACTIVE: "default"

.deploy_template: &deploy_template
  stage: deploy
  image: alpine/k8s:latest
  script:
    - envsubst < k8s/deployment.yaml | kubectl apply -f -
    - kubectl rollout status deployment/$APP_NAME

deploy:development:
  <<: *deploy_template
  variables:
    ENVIRONMENT: "development"
    SPRING_PROFILES_ACTIVE: "dev"
    REPLICAS: "1"
    RESOURCES_LIMITS_CPU: "500m"
    RESOURCES_LIMITS_MEMORY: "1Gi"
  environment:
    name: development
    url: https://dev.example.com
  only:
    - develop

deploy:testing:
  <<: *deploy_template
  variables:
    ENVIRONMENT: "testing"
    SPRING_PROFILES_ACTIVE: "test"
    REPLICAS: "2"
    RESOURCES_LIMITS_CPU: "1"
    RESOURCES_LIMITS_MEMORY: "2Gi"
  environment:
    name: testing
    url: https://test.example.com
  only:
    - main

deploy:staging:
  <<: *deploy_template
  variables:
    ENVIRONMENT: "staging"
    SPRING_PROFILES_ACTIVE: "staging"
    REPLICAS: "3"
    RESOURCES_LIMITS_CPU: "2"
    RESOURCES_LIMITS_MEMORY: "4Gi"
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - release/*
  when: manual

deploy:production:
  <<: *deploy_template
  variables:
    ENVIRONMENT: "production"
    SPRING_PROFILES_ACTIVE: "prod"
    REPLICAS: "5"
    RESOURCES_LIMITS_CPU: "4"
    RESOURCES_LIMITS_MEMORY: "8Gi"
  environment:
    name: production
    url: https://app.example.com
  only:
    - tags
  when: manual
```

#### 🔐 環境變數管理

**分層變數設定**：

```text
變數層級優先順序：
┌─────────────────┐  (最高優先級)
│ Job Variables   │
├─────────────────┤
│ Project Vars    │
├─────────────────┤
│ Group Variables │
├─────────────────┤
│ Instance Vars   │  (最低優先級)
└─────────────────┘
```

**環境變數範例**：

```yaml
# GitLab CI/CD Variables 設定

# 開發環境變數
ENVIRONMENT: development
DB_HOST: dev-db.company.com
DB_NAME: app_dev
REDIS_URL: redis://dev-redis.company.com:6379
LOG_LEVEL: DEBUG

# 生產環境變數
ENVIRONMENT: production
DB_HOST: prod-db.company.com
DB_NAME: app_prod
REDIS_URL: redis://prod-redis.company.com:6379
LOG_LEVEL: INFO

# 共用變數
APP_NAME: java-tutorial
DOCKER_REGISTRY: registry.company.com
```

#### 🚀 藍綠部署實作

**藍綠部署 Pipeline**：

```yaml
# 藍綠部署配置
stages:
  - build
  - test
  - deploy:blue
  - smoke:blue
  - switch:traffic
  - cleanup:green

deploy:blue:
  stage: deploy:blue
  script:
    - |
      # 部署到藍色環境
      kubectl apply -f k8s/blue/
      kubectl rollout status deployment/app-blue
      kubectl wait --for=condition=ready pod -l app=java-tutorial,env=blue
  environment:
    name: production-blue
    url: https://blue.app.example.com

smoke:test:blue:
  stage: smoke:blue
  script:
    - |
      # 對藍色環境進行冒煙測試
      curl -f https://blue.app.example.com/health
      curl -f https://blue.app.example.com/api/status
      
      # 執行關鍵功能測試
      newman run tests/smoke-tests.postman_collection.json \
        --env-var "base_url=https://blue.app.example.com"

switch:traffic:
  stage: switch:traffic
  script:
    - |
      # 切換流量到藍色環境
      kubectl patch service app-service -p '{"spec":{"selector":{"env":"blue"}}}'
      echo "流量已切換到藍色環境"
  when: manual
  environment:
    name: production
    url: https://app.example.com

cleanup:green:
  stage: cleanup:green
  script:
    - |
      # 清理舊的綠色環境
      kubectl delete deployment app-green || true
      kubectl delete service app-green-service || true
  when: manual
```

### 8.9 容器化與 Kubernetes 整合

#### 🐳 Docker 最佳實務

**多階段建置 Dockerfile**：

```dockerfile
# Multi-stage Dockerfile for Java application
FROM maven:3.8.4-openjdk-17-slim AS builder

WORKDIR /app
COPY pom.xml .
# 先複製 pom.xml 以利用 Docker 層快取
RUN mvn dependency:go-offline -B

COPY src ./src
RUN mvn clean package -DskipTests

# 第二階段：運行時映像檔
FROM openjdk:17-jre-slim

# 安全性：建立非 root 使用者
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# 複製建置產物
COPY --from=builder /app/target/*.jar app.jar

# 設定健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

# 使用非 root 使用者執行
USER appuser

EXPOSE 8080

# 使用 exec 形式避免 PID 1 問題
ENTRYPOINT ["java", "-jar", "app.jar"]
```

#### ☸️ Kubernetes 部署配置

**完整的 Kubernetes 資源定義**：

```yaml
# k8s/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: java-tutorial
  labels:
    name: java-tutorial

---
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: java-tutorial
data:
  application.yml: |
    server:
      port: 8080
    spring:
      profiles:
        active: ${SPRING_PROFILES_ACTIVE:prod}
      datasource:
        url: ${DB_URL}
        username: ${DB_USERNAME}
        password: ${DB_PASSWORD}
    logging:
      level:
        com.tutorial: ${LOG_LEVEL:INFO}

---
# k8s/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: java-tutorial
type: Opaque
data:
  db-password: <base64-encoded-password>
  jwt-secret: <base64-encoded-jwt-secret>

---
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: java-tutorial-app
  namespace: java-tutorial
  labels:
    app: java-tutorial
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  selector:
    matchLabels:
      app: java-tutorial
  template:
    metadata:
      labels:
        app: java-tutorial
    spec:
      containers:
      - name: app
        image: ${DOCKER_REGISTRY}/java-tutorial:${CI_COMMIT_SHA}
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "prod"
        - name: DB_URL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: db-url
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db-password
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        volumeMounts:
        - name: config
          mountPath: /app/config
      volumes:
      - name: config
        configMap:
          name: app-config

---
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: java-tutorial-service
  namespace: java-tutorial
spec:
  selector:
    app: java-tutorial
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP

---
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: java-tutorial-ingress
  namespace: java-tutorial
  annotations:
    kubernetes.io/ingress.class: "nginx"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  tls:
  - hosts:
    - app.example.com
    secretName: java-tutorial-tls
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: java-tutorial-service
            port:
              number: 80
```

#### 🔄 Helm Chart 管理

**Helm Chart 結構**：

```text
helm/java-tutorial/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-prod.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    ├── configmap.yaml
    ├── secret.yaml
    └── hpa.yaml
```

**Helm 部署 Pipeline**：

```yaml
# Helm 部署配置
deploy:helm:
  stage: deploy
  image: alpine/helm:latest
  script:
    - helm repo add stable https://charts.helm.sh/stable
    - helm dependency update ./helm/java-tutorial
    - |
      helm upgrade --install java-tutorial ./helm/java-tutorial \
        --namespace java-tutorial \
        --create-namespace \
        --values ./helm/java-tutorial/values-${ENVIRONMENT}.yaml \
        --set image.tag=${CI_COMMIT_SHA} \
        --set image.repository=${DOCKER_REGISTRY}/java-tutorial \
        --wait --timeout=600s
    - helm test java-tutorial --namespace java-tutorial

```

### 8.10 效能監控與分析

#### 📊 監控架構設計

**完整監控堆疊**：

```text
監控架構：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Application │ →  │ Prometheus  │ →  │  Grafana    │
│   Metrics   │    │  (收集)      │    │  (視覺化)    │
└─────────────┘    └─────────────┘    └─────────────┘
       ↓                    ↓                  ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    Logs     │ →  │ AlertManager│    │   Alerts    │
│ (ELK Stack) │    │   (告警)     │    │   (通知)     │
└─────────────┘    └─────────────┘    └─────────────┘
```

#### 🎯 應用程式監控設定

**Spring Boot Actuator 配置**：

```yaml
# application-prod.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: when-authorized
    metrics:
      enabled: true
  metrics:
    export:
      prometheus:
        enabled: true
    distribution:
      percentiles-histogram:
        http.server.requests: true
      slo:
        http.server.requests: 50ms,100ms,200ms,300ms,500ms,1s
```

**自訂 Metrics 範例**：

```java
@RestController
@Slf4j
public class UserController {
    
    private final UserService userService;
    private final MeterRegistry meterRegistry;
    private final Counter userCreationCounter;
    private final Timer userQueryTimer;
    
    public UserController(UserService userService, MeterRegistry meterRegistry) {
        this.userService = userService;
        this.meterRegistry = meterRegistry;
        this.userCreationCounter = Counter.builder("user.creation.count")
            .description("使用者建立次數")
            .register(meterRegistry);
        this.userQueryTimer = Timer.builder("user.query.duration")
            .description("使用者查詢時間")
            .register(meterRegistry);
    }
    
    @PostMapping("/users")
    public ResponseEntity<User> createUser(@RequestBody UserDto userDto) {
        try {
            User user = userService.createUser(userDto);
            userCreationCounter.increment("status", "success");
            return ResponseEntity.ok(user);
        } catch (Exception e) {
            userCreationCounter.increment("status", "error");
            throw e;
        }
    }
    
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return userQueryTimer.recordCallable(() -> {
            User user = userService.getUserById(id);
            return ResponseEntity.ok(user);
        });
    }
}
```

#### 📈 Grafana Dashboard 配置

**Dashboard JSON 範例**：

```json
{
  "dashboard": {
    "title": "Java Tutorial Application Metrics",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_server_requests_seconds_count[5m])",
            "legendFormat": "{{method}} {{uri}}"
          }
        ]
      },
      {
        "title": "Response Time",
        "type": "graph",
        "targets": [
          {
            "expr": "http_server_requests_seconds{quantile=\"0.95\"}",
            "legendFormat": "95th percentile"
          },
          {
            "expr": "http_server_requests_seconds{quantile=\"0.50\"}",
            "legendFormat": "50th percentile"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_server_requests_seconds_count{status=~\"4..|5..\"}[5m])",
            "legendFormat": "Error Rate"
          }
        ]
      },
      {
        "title": "JVM Memory Usage",
        "type": "graph",
        "targets": [
          {
            "expr": "jvm_memory_used_bytes{area=\"heap\"}",
            "legendFormat": "Heap Used"
          },
          {
            "expr": "jvm_memory_max_bytes{area=\"heap\"}",
            "legendFormat": "Heap Max"
          }
        ]
      }
    ]
  }
}
```

#### 🚨 告警規則設定

**Prometheus Alert Rules**：

```yaml
# alert-rules.yml
groups:
- name: java-tutorial-alerts
  rules:
  - alert: HighErrorRate
    expr: rate(http_server_requests_seconds_count{status=~"5.."}[5m]) > 0.1
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "應用程式錯誤率過高"
      description: "錯誤率超過 10% 已持續 2 分鐘"
      
  - alert: HighResponseTime
    expr: http_server_requests_seconds{quantile="0.95"} > 1
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "應用程式回應時間過長"
      description: "95% 回應時間超過 1 秒已持續 5 分鐘"
      
  - alert: HighMemoryUsage
    expr: (jvm_memory_used_bytes{area="heap"} / jvm_memory_max_bytes{area="heap"}) > 0.8
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "JVM 記憶體使用率過高"
      description: "Heap 記憶體使用率超過 80% 已持續 10 分鐘"
      
  - alert: ApplicationDown
    expr: up{job="java-tutorial"} == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "應用程式無法連接"
      description: "應用程式已無法連接超過 1 分鐘"
```

### 8.11 實際案例研究

#### 🏢 案例一：企業級 Java 微服務架構

**專案背景**：

- 大型電商平台後端系統
- 20+ 個微服務
- 日活躍用戶 100萬+
- 峰值 QPS 10,000+

**GitLab 實作架構**：

```text
GitLab 組織架構：
Company Group
├── Platform Team
│   ├── api-gateway
│   ├── config-server
│   └── service-discovery
├── Business Team
│   ├── user-service
│   ├── order-service
│   ├── payment-service
│   └── inventory-service
└── Infrastructure Team
    ├── monitoring
    ├── logging
    └── deployment-scripts
```

**Pipeline 策略**：

```yaml
# 微服務共用 Pipeline 模板
include:
  - project: 'platform/ci-templates'
    file: '/templates/microservice-pipeline.yml'

variables:
  SERVICE_NAME: "user-service"
  SERVICE_PORT: "8080"
  
stages:
  - validate
  - build
  - test
  - security-scan
  - package
  - deploy-dev
  - integration-test
  - deploy-staging
  - performance-test
  - deploy-prod

# 微服務特定配置
microservice:build:
  extends: .build-template
  variables:
    MAVEN_PROFILES: "microservice"
    
microservice:deploy:
  extends: .deploy-template
  variables:
    REPLICAS: "3"
    RESOURCES_CPU: "500m"
    RESOURCES_MEMORY: "1Gi"
```

**實際效益**：

- 部署時間從 2 小時縮短至 15 分鐘
- 程式碼品質問題減少 70%
- 生產環境事故減少 60%
- 開發效率提升 40%

#### 🏦 案例二：金融服務 CI/CD 合規實作

**合規要求**：

- SOX 法案遵循
- 四眼原則 (Four-eye principle)
- 變更記錄追蹤
- 安全掃描強制執行

**合規 Pipeline 設計**：

```yaml
# 金融合規 Pipeline
stages:
  - compliance-check
  - security-scan
  - code-review
  - approval
  - deploy

compliance:audit:
  stage: compliance-check
  script:
    - echo "檢查合規性要求"
    - python scripts/compliance-check.py
    - python scripts/sox-validation.py
  artifacts:
    reports:
      junit: compliance-report.xml

security:sast:
  stage: security-scan
  extends: .sast-template
  allow_failure: false  # 安全掃描必須通過

security:dependency:
  stage: security-scan
  extends: .dependency-scanning-template
  allow_failure: false

code:review:
  stage: code-review
  script:
    - echo "確認 Code Review 要求"
    - python scripts/verify-approvals.py --required=2
  rules:
    - if: '$CI_MERGE_REQUEST_TARGET_BRANCH_NAME == "main"'

deploy:production:
  stage: deploy
  script:
    - echo "部署到生產環境"
    - kubectl apply -f k8s/production/
  environment:
    name: production
  rules:
    - if: '$CI_COMMIT_TAG'
      when: manual
  needs:
    - compliance:audit
    - security:sast
    - security:dependency
```

#### 🎓 案例三：教育平台敏捷開發

**專案特色**：

- 快速原型開發
- 頻繁功能更新
- 多環境並行測試
- 學生作業自動評分

**教育導向 Pipeline**：

```yaml
# 教育平台特殊需求
stages:
  - build
  - test
  - deploy-preview
  - auto-grading
  - deploy-production

build:frontend:
  stage: build
  image: node:16
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

build:backend:
  stage: build
  image: maven:3.8.4-openjdk-17
  script:
    - mvn clean package
  artifacts:
    paths:
      - target/*.jar

deploy:preview:
  stage: deploy-preview
  script:
    - |
      # 每個 MR 建立預覽環境
      PREVIEW_URL="https://preview-${CI_MERGE_REQUEST_IID}.example.com"
      kubectl create namespace preview-${CI_MERGE_REQUEST_IID} || true
      envsubst < k8s/preview.yaml | kubectl apply -f -
      echo "預覽環境：$PREVIEW_URL"
  environment:
    name: preview/$CI_MERGE_REQUEST_IID
    url: https://preview-${CI_MERGE_REQUEST_IID}.example.com
    on_stop: cleanup:preview
  rules:
    - if: '$CI_MERGE_REQUEST_ID'

auto:grading:
  stage: auto-grading
  script:
    - python scripts/auto-grader.py
    - python scripts/plagiarism-check.py
  artifacts:
    reports:
      junit: grading-results.xml
  only:
    - /^assignment\/.*$/
```

**學習成果**：

- 學生提交作業到評分反饋時間從 24 小時縮短至 5 分鐘
- 程式碼抄襲檢測準確率 95%
- 教師工作量減少 60%
- 學生滿意度提升 85%

### 8.12 未來趨勢與發展

#### 🔮 新興技術整合

**AI/ML 在 DevOps 中的應用**：

```text
AI 輔助開發流程：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ 智慧 Code   │ →  │ 自動化測試   │ →  │ 預測性維護   │
│ Review      │    │ 案例生成     │    │ 和監控      │
└─────────────┘    └─────────────┘    └─────────────┘
```

**實際應用範例**：

```yaml
# AI 輔助的 Pipeline
ai:code-review:
  stage: analysis
  image: ai/code-analyzer:latest
  script:
    - ai-reviewer --language=java --output=review-report.json
    - python scripts/process-ai-feedback.py
  artifacts:
    reports:
      codequality: review-report.json

ai:test-generation:
  stage: test
  script:
    - ai-test-generator --source=src/main/java --output=src/test/java
    - mvn test -Dtest.pattern="*AIGenerated*"
  allow_failure: true

predictive:monitoring:
  stage: deploy
  script:
    - python scripts/anomaly-detection.py
    - python scripts/capacity-planning.py
  environment:
    name: production
```

#### 🌐 雲原生與邊緣運算

**GitOps 2.0 架構**：

```text
下一代 GitOps 架構：
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Source    │ →  │   GitOps    │ →  │  Multi-Cloud│
│   Control   │    │  Operator   │    │  Deployment │
└─────────────┘    └─────────────┘    └─────────────┘
       │                    │                  │
       ↓                    ↓                  ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Edge Nodes  │    │   Policy    │    │  Security   │
│ Management  │    │ Enforcement │    │ Compliance  │
└─────────────┘    └─────────────┘    └─────────────┘
```

#### 🔒 零信任安全模型

**未來安全架構**：

```yaml
# 零信任 Pipeline 安全
zero-trust:security:
  stage: security
  script:
    - identity-verification --service=gitlab-ci
    - network-policy-validation --cluster=production
    - runtime-security-scan --image=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - supply-chain-verification --sbom=sbom.json
  artifacts:
    reports:
      security: zero-trust-report.json

policy:enforcement:
  stage: governance
  script:
    - opa-policy-check --policies=security/policies/
    - compliance-validation --framework=sox,gdpr
    - risk-assessment --deployment=production
```

#### 🚀 Platform Engineering 演進

**內部開發者平台架構**：

```text
Developer Platform Stack:
┌─────────────────────────────────────────────────────┐
│                Developer Portal                      │
├─────────────────────────────────────────────────────┤
│           Service Catalog & Templates               │
├─────────────────────────────────────────────────────┤
│    GitLab CI/CD    │    GitOps     │   Monitoring    │
├─────────────────────────────────────────────────────┤
│        Kubernetes         │      Infrastructure     │
└─────────────────────────────────────────────────────┘
```

**自服務 Pipeline 模板**：

```yaml
# 平台工程師提供的標準模板
include:
  - project: 'platform/templates'
    file: '/java/microservice.yml'
  - project: 'platform/templates'
    file: '/security/compliance.yml'
  - project: 'platform/templates'
    file: '/deployment/kubernetes.yml'

# 開發者只需要配置業務相關參數
variables:
  SERVICE_NAME: "my-service"
  SERVICE_TYPE: "microservice"
  COMPLIANCE_LEVEL: "high"
  ENVIRONMENT_TIER: "production"

# 自動套用平台標準
platform:standards:
  extends: .platform-template
  variables:
    AUTO_SCALING: "enabled"
    MONITORING: "full"
    SECURITY_SCAN: "required"
```

#### 📊 可觀測性 3.0

**下一代監控架構**：

```yaml
# 統一可觀測性平台
observability:traces:
  stage: monitoring
  script:
    - jaeger-setup --service=$SERVICE_NAME
    - opentelemetry-config --auto-instrument=java
  environment:
    name: production

observability:metrics:
  stage: monitoring
  script:
    - prometheus-setup --service=$SERVICE_NAME
    - custom-metrics-config --business-kpis=true
  environment:
    name: production

observability:logs:
  stage: monitoring
  script:
    - elk-setup --service=$SERVICE_NAME
    - log-correlation --trace-id=true
  environment:
    name: production
```

#### 💡 持續創新建議

**組織文化發展**：

1. **學習型組織**：
   - 定期技術分享會
   - 失敗後分析 (Blameless Postmortem)
   - 實驗驅動的創新文化

2. **平台思維**：
   - 將 DevOps 工具視為產品
   - 內部客戶導向
   - 持續改善和反饋循環

3. **社群參與**：
   - 參與開源專案
   - 技術會議和研討會
   - 知識分享與交流

**技術評估框架**：

```markdown
# 新技術評估範本

## 技術概述
- 技術名稱：
- 解決的問題：
- 替代方案比較：

## 評估標準
- [ ] 技術成熟度
- [ ] 社群活躍度
- [ ] 學習成本
- [ ] 整合複雜度
- [ ] 維護成本
- [ ] 安全性考量

## 實驗計畫
- POC 時程：
- 成功指標：
- 風險評估：
- 回滾計畫：

## 決策建議
- 推薦指數：⭐⭐⭐⭐⭐
- 實施優先級：高/中/低
- 預期效益：
```

---

## 9. 附錄

### 9.1 聯絡資訊

#### 技術支援窗口

- **GitLab 管理員**：<admin@company.com>
- **DevOps 團隊**：<devops@company.com>
- **技術支援熱線**：分機 1234

#### 團隊協作平台

- **Slack 頻道**：#dev-team、#gitlab-support
- **團隊會議**：每週三 14:00-15:00
- **技術分享**：每月第一個週五

### 9.2 參考資源

#### 官方文件資源

- [GitLab 官方文件](https://docs.gitlab.com/)
- [Git 官方文件](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)

#### 學習資源連結

- [Pro Git 電子書](https://git-scm.com/book)
- [GitLab CI/CD 教學](https://docs.gitlab.com/ee/ci/)
- [Git Flow 工作流程](https://nvie.com/posts/a-successful-git-branching-model/)

#### 技術文章

- [GitLab 最佳實務指南](https://about.gitlab.com/handbook/)
- [DevOps 文化建立](https://www.atlassian.com/devops)
- [安全開發生命週期](https://owasp.org/www-project-integration-standards/)

### 9.3 工具推薦

#### Git GUI 工具

- [GitKraken](https://www.gitkraken.com/) - 功能強大的 Git GUI 工具
- [Sourcetree](https://www.sourcetreeapp.com/) - 免費的 Git GUI 工具
- [Git Extensions](https://gitextensions.github.io/) - Windows 平台 Git 工具

#### IDE 整合擴充功能

- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - VS Code Git 增強擴充功能
- [GitLab Workflow](https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow) - VS Code GitLab 整合
- [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) - Git 歷史檢視器

#### CLI 命令列工具

- [Hub](https://hub.github.com/) - GitHub 命令列工具
- [glab](https://gitlab.com/gitlab-org/cli) - GitLab 官方命令列工具
- [tig](https://jonas.github.io/tig/) - 文字模式的 Git 介面

#### 監控與分析工具

- [GitLab Insights](https://docs.gitlab.com/ee/user/project/insights/) - 專案洞察分析
- [Grafana](https://grafana.com/) - 監控儀表板
- [Prometheus](https://prometheus.io/) - 監控和警報工具

#### 安全工具

- [GitLab Security Dashboard](https://docs.gitlab.com/ee/user/application_security/security_dashboard/) - 安全儀表板
- [OWASP ZAP](https://owasp.org/www-project-zap/) - 安全測試工具
- [Snyk](https://snyk.io/) - 漏洞掃描工具

---

## 10. 補充主題

### 10.1 性能基準測試與優化

#### 🎯 Pipeline 效能基準

**基準測試指標**：

```yaml
# 效能基準測試 Pipeline
performance:benchmark:
  stage: test
  image: maven:3.8.4-openjdk-17
  script:
    # 建置效能測試
    - mvn clean package -Pperformance
    
    # JMeter 負載測試
    - jmeter -n -t tests/load-test.jmx -l results.jtl
    
    # K6 效能測試
    - k6 run --out json=performance.json tests/performance.js
    
    # 分析結果
    - python scripts/analyze-performance.py
  artifacts:
    reports:
      performance: performance-report.json
    paths:
      - performance-report.html
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_MERGE_REQUEST_ID'
      changes:
        - "src/**/*.java"
```

**效能監控範例**：

```java
// 效能監控註解
@RestController
@Timed(name = "api.controller", description = "API 控制器效能監控")
public class UserController {
    
    @GetMapping("/users")
    @Timed(name = "api.users.list", description = "用戶列表查詢時間")
    public ResponseEntity<List<User>> listUsers(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size) {
        
        // 記錄慢查詢
        Stopwatch stopwatch = Stopwatch.createStarted();
        try {
            List<User> users = userService.getUsers(page, size);
            return ResponseEntity.ok(users);
        } finally {
            Duration duration = stopwatch.elapsed();
            if (duration.toMillis() > 500) {
                log.warn("慢查詢檢測: 用戶列表查詢耗時 {}ms", duration.toMillis());
            }
        }
    }
}
```

### 10.2 災難恢復演練

#### 🚨 DR 演練自動化

**災難恢復 Pipeline**：

```yaml
# 災難恢復演練
dr:drill:
  stage: test
  script:
    # 模擬災難場景
    - python scripts/simulate-disaster.py --scenario=database-failure
    
    # 執行恢復程序
    - ansible-playbook playbooks/disaster-recovery.yml
    
    # 驗證恢復結果
    - python scripts/verify-recovery.py
    
    # 生成演練報告
    - python scripts/generate-dr-report.py
  environment:
    name: dr-testing
  when: manual
  only:
    variables:
      - $DR_DRILL == "true"
```

### 10.3 合規自動化

#### 📋 法規遵循檢查

**自動合規檢查**：

```yaml
# 合規性檢查 Pipeline
compliance:gdpr:
  stage: compliance
  script:
    - python scripts/gdpr-compliance-check.py
    - python scripts/data-privacy-scan.py
  artifacts:
    reports:
      compliance: gdpr-report.json

compliance:sox:
  stage: compliance
  script:
    - python scripts/sox-compliance-check.py
    - python scripts/financial-controls-audit.py
  artifacts:
    reports:
      compliance: sox-report.json

compliance:iso27001:
  stage: compliance
  script:
    - python scripts/iso27001-check.py
    - python scripts/security-controls-audit.py
  artifacts:
    reports:
      compliance: iso27001-report.json
```

### 10.4 成本優化策略

#### 💰 CI/CD 成本管控

**成本監控 Pipeline**：

```yaml
# 成本分析與優化
cost:analysis:
  stage: analysis
  script:
    # 分析 Runner 使用率
    - python scripts/runner-utilization.py
    
    # 分析建置時間和資源消耗
    - python scripts/build-cost-analysis.py
    
    # 產生成本優化建議
    - python scripts/cost-optimization-suggestions.py
  artifacts:
    reports:
      cost: cost-analysis-report.json
  only:
    - schedules

# 資源清理
cleanup:unused:
  stage: cleanup
  script:
    # 清理過期的 Docker 映像
    - docker image prune -f --filter "until=168h"
    
    # 清理舊的 Pipeline artifacts
    - python scripts/cleanup-old-artifacts.py --days=30
    
    # 清理未使用的 K8s 資源
    - kubectl delete pods --field-selector=status.phase=Failed
  only:
    - schedules
```

---

## 結語與持續改進

這份全面的 GitLab 使用教學手冊現在包含了：

### 📚 完整內容涵蓋

1. **基礎到進階**：從入門到專家級應用
2. **理論與實踐**：概念解釋配合實際範例
3. **最佳實務**：業界標準和團隊經驗
4. **未來導向**：新興趨勢和技術展望

### 🎯 實用價值

- **新進人員**：完整的入門指南和檢查清單
- **經驗開發者**：進階功能和優化技巧
- **團隊領導**：流程設計和最佳實務
- **DevOps 工程師**：自動化和監控策略

### 🔄 持續更新機制

建議建立以下更新流程：

1. **季度檢討**：評估文件內容是否符合實際需求
2. **工具更新**：跟隨 GitLab 版本更新調整內容
3. **經驗分享**：收集團隊使用經驗並持續改善
4. **社群回饋**：參考社群最佳實務和新趨勢

### 📈 成效追蹤

建議追蹤以下指標來評估文件效益：

- 新進人員上手時間
- 開發流程效率提升
- 程式碼品質改善
- 生產環境事故減少

> 💡 **記住**：工具和流程會不斷演進，最重要的是建立學習型團隊文化，持續改善和適應變化。

---

## 結語

這份 GitLab 使用教學手冊涵蓋了從基礎操作到進階整合的完整內容。隨著技術的不斷發展，建議團隊：

1. **持續學習**：關注 GitLab 的新功能和最佳實務
2. **定期檢討**：評估和優化現有的工作流程
3. **知識分享**：在團隊內分享經驗和技巧
4. **工具評估**：評估新工具和技術的導入可能性
5. **文件維護**：定期更新和完善團隊的開發規範

記住，工具只是手段，重要的是建立高效、安全、可維護的開發流程。希望這份手冊能幫助您和團隊更好地使用 GitLab，提升開發效率和程式碼品質。

### 📚 文件資訊

**文件名稱**：GitLab 使用教學手冊  
**版本**：2.0  
**最後更新**：2025年8月29日  
**維護者**：開發團隊  
**文件格式**：Markdown  
**授權**：內部使用  

### 📝 版本歷史

- **v2.0** (2025-08-29)：重大更新 - 新增 GitLab Runner 深度配置、多環境部署策略、容器化整合、效能監控、實際案例研究、性能基準測試、災難恢復演練、合規自動化、成本優化等內容
- **v1.1** (2025-08-28)：新增核心功能詳解、進階功能與整合章節，完善目錄結構
- **v1.0** (2024-01-15)：初版發布，包含基礎操作和規範

### 💬 意見回饋

如有任何建議、問題或發現錯誤，請透過以下方式聯繫：

- **Issue 追蹤**：在專案中建立 Issue


> 💡 這份文件會持續更新以反映最新的開發實務和工具功能。感謝您的使用和回饋！
