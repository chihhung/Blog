+++
date = '2026-03-26T17:57:36+08:00'
draft = false
title = 'Copilot CLI教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# GitHub Copilot CLI 教學手冊

> **版本**：基於 GitHub Copilot CLI **v1.0.11**（2026-03-23 發佈）  
> **GA 日期**：2026-02-25（v0.0.418 起正式 GA）  
> **適用對象**：資深工程師 / DevOps 工程師 / 架構師  
> **技術環境**：企業級 Web Application（Spring Boot 3.x / Vue 3 / 微服務架構）  
> **適用方案**：Copilot Free / Pro / Pro+ / Business / Enterprise  
> **最後更新**：2026-03-26

---

## 目錄

- [第 1 章：Copilot CLI 概述](#第-1-章copilot-cli-概述)
  - [1.1 什麼是 GitHub Copilot CLI](#11-什麼是-github-copilot-cli)
  - [1.2 與其他 AI 工具的差異比較](#12-與其他-ai-工具的差異比較)
  - [1.3 適用場景](#13-適用場景)
- [第 2 章：系統架構整合設計](#第-2-章系統架構整合設計)
  - [2.1 Copilot CLI 在企業架構中的角色](#21-copilot-cli-在企業架構中的角色)
  - [2.2 與開發流程整合](#22-與開發流程整合)
  - [2.3 Agentic Workflow 設計模式](#23-agentic-workflow-設計模式)
- [第 3 章：安裝與環境設定](#第-3-章安裝與環境設定)
  - [3.1 支援平台](#31-支援平台)
  - [3.2 前置需求](#32-前置需求)
  - [3.3 安裝步驟](#33-安裝步驟)
  - [3.4 身份驗證](#34-身份驗證)
  - [3.5 初始化設定](#35-初始化設定)
  - [3.6 常見錯誤與排除](#36-常見錯誤與排除)
- [第 4 章：核心功能教學](#第-4-章核心功能教學)
  - [4.1 自然語言轉指令](#41-自然語言轉指令)
  - [4.2 Agentic Workflow](#42-agentic-workflow)
  - [4.3 Codebase Context 分析](#43-codebase-context-分析)
  - [4.4 GitHub 整合](#44-github-整合)
  - [4.5 LSP 語言伺服器整合](#45-lsp-語言伺服器整合)
  - [4.6 Hooks 鉤子系統](#46-hooks-鉤子系統)
  - [4.7 Skills 技能系統](#47-skills-技能系統)
  - [4.8 Plugin 插件生態系](#48-plugin-插件生態系)
  - [4.9 Extensions 擴充機制](#49-extensions-擴充機制)
  - [4.10 Copilot Memory 跨 Session 記憶](#410-copilot-memory-跨-session-記憶)
  - [4.11 ACP（Agent Client Protocol）](#411-acpagent-client-protocol)
- [第 5 章：進階使用技巧（企業級）](#第-5-章進階使用技巧企業級)
  - [5.1 Prompt Engineering（CLI 版本）](#51-prompt-engineeringcli-版本)
  - [5.2 Context Engineering（讓 AI 更準）](#52-context-engineering讓-ai-更準)
  - [5.3 多步驟任務拆解（Task Chaining）](#53-多步驟任務拆解task-chaining)
  - [5.4 與其他工具整合](#54-與其他工具整合)
  - [5.5 Session 管理與對話引導](#55-session-管理與對話引導)
- [第 6 章：安全與治理](#第-6-章安全與治理)
  - [6.1 工具審批機制](#61-工具審批機制)
  - [6.2 YOLO Mode 說明與風險](#62-yolo-mode-說明與風險)
  - [6.3 企業治理策略](#63-企業治理策略)
  - [6.4 Hooks 安全防護](#64-hooks-安全防護)
- [第 7 章：實戰案例](#第-7-章實戰案例)
- [第 8 章：最佳實務（Best Practices）](#第-8-章最佳實務best-practices)
  - [8.1 如何寫好 Prompt（CLI 版本）](#81-如何寫好-promptcli-版本)
  - [8.2 人機協作（Human-in-the-Loop）](#82-人機協作human-in-the-loop)
  - [8.3 適合與不適合使用的場景](#83-適合與不適合使用的場景)
- [第 9 章：維運與升級](#第-9-章維運與升級)
  - [9.1 如何更新 Copilot CLI](#91-如何更新-copilot-cli)
  - [9.2 版本管理策略](#92-版本管理策略)
  - [9.3 常見問題（FAQ）](#93-常見問題faq)
  - [9.4 效能與成本考量](#94-效能與成本考量)
- [第 10 章：附錄](#第-10-章附錄)
  - [10.1 常用指令速查表](#101-常用指令速查表)
  - [10.2 Prompt 範本合集](#102-prompt-範本合集)
  - [10.3 工具權限速查表](#103-工具權限速查表)
  - [10.4 環境變數](#104-環境變數)
  - [10.5 設定檔位置](#105-設定檔位置)
  - [10.6 版本演進里程碑](#106-版本演進里程碑)
- [檢查清單（Checklist）](#檢查清單checklist)

---

# 第 1 章：Copilot CLI 概述

## 1.1 什麼是 GitHub Copilot CLI

GitHub Copilot CLI 是 GitHub 提供的**命令列 AI 代理工具**，讓開發者直接在終端機（Terminal）中使用 Copilot 的 AI 能力。它不僅是一個自然語言轉指令的工具，更是一個完整的 **AI Agent**，能夠：

- **理解自然語言**：將口語化的需求轉換為精確的 Shell / Git 指令
- **自主執行任務**：自動掃描 Codebase、產生程式碼、修復 Bug、建立 Pull Request
- **上下文管理**：自動讀取專案檔案結構與依賴關係，提供精準建議；支援**跨 Session 記憶**與**自動上下文壓縮**
- **GitHub 深度整合**：無需切換介面即可操作 PR、Issue、Actions、Discussions
- **多代理協作**：透過 `/fleet` 指揮多個子代理平行執行任務
- **非同步委派**：透過 `/delegate` 委派工作給 Copilot Coding Agent 背景執行
- **Autopilot 模式**：全自動完成任務，無需逐步確認
- **擴充生態系**：支援 Plugin、Extension、Skill、Hook、MCP Server、LSP Server
- **ACP 協定**：透過 Agent Client Protocol（ACP）標準開放介面，與第三方工具、IDE 或自動化系統整合
- **Copilot SDK**：基於相同的 Agentic Runtime，可用 SDK 為您的應用程式內建 AI Agent 能力

> ⚠️ **注意**：舊版的 GitHub CLI Copilot Extension（`gh copilot`）已正式退役，已由全新的 GitHub Copilot CLI（`copilot` 指令）取代。Copilot CLI 於 **2026-02-25 正式 GA**（v0.0.418），目前最新版本為 **v1.0.11**。

### 核心定位

```
GitHub Copilot CLI = AI Agent + Terminal + GitHub 深度整合 + 多代理協作 + 擴充生態系 + ACP 開放標準
```

### 支援模型一覽

| 模型 | 類型 | 說明 |
|------|------|------|
| **Claude Sonnet 4.5** | Anthropic | **預設模型**，平衡速度與品質 |
| Claude Sonnet 4 | Anthropic | 上一代 Sonnet，可透過 `/model` 切換 |
| Claude Sonnet 4.6 | Anthropic | 可透過 `/model` 切換 |
| Claude Opus 4.5 | Anthropic | 高品質推理 |
| Claude Opus 4.6 | Anthropic | 高品質推理 |
| Claude Opus 4.6 Fast | Anthropic | 快速推理（Preview） |
| Haiku 4.5 | Anthropic | 輕量快速 |
| GPT-5.1 | OpenAI | 通用能力 |
| GPT-5.1-Codex / Codex-Mini / Codex-Max | OpenAI | 程式碼專用 |
| GPT-5.2 / GPT-5.2-Codex | OpenAI | 進階推理 |
| GPT-5.4 | OpenAI | 進階推理（v0.0.422 新增） |
| GPT-5.4-Mini | OpenAI | 輕量快速（v1.0.7 新增） |

> 💡 **提示**：使用 `/model` 指令可即時切換模型。模型可用性取決於您的 Copilot 方案與組織政策。部分模型已棄用（如 GPT-5）。模型選擇器會依據使用者方案與組織政策，自動分為「可用」、「停用/封鎖」、「升級」三個分頁顯示。

## 1.2 與其他 AI 工具的差異比較

| 比較面向 | ChatGPT | IDE Copilot（VS Code） | Copilot CLI | Agent Framework（LangChain 等） |
|---------|---------|----------------------|-------------|-------------------------------|
| **介面** | Web / API | IDE 內嵌 | Terminal 命令列 | 程式碼 SDK |
| **操作方式** | 對話 | 自動補全 / Chat | 對話 + 自動執行 + Autopilot | API 驅動 |
| **檔案存取** | 無（需手動貼上） | 當前編輯器開啟檔案 | 整個專案目錄 + 跨目錄引用 | 自定義 |
| **執行能力** | 僅建議 | 僅建議（部分 Apply） | **直接執行** Shell / Git / 檔案操作 | 自定義 |
| **GitHub 整合** | 無 | 有（Extensions） | **原生深度整合**（MCP） | 需自行實作 |
| **自主性** | 被動回答 | 被動補全 | **主動代理**（Agentic / Autopilot / Fleet） | 高度自定義 |
| **Context 管理** | 手動 | 自動（有限） | **自動**（整個專案 + 跨 Session 記憶 + 自動壓縮） | 需自行設計 |
| **多代理** | 無 | 無 | **原生支援**（/fleet 平行子代理） | 需自己編排 |
| **擴充性** | 無 | Extensions | **Plugin + Skill + Hook + Extension + MCP + LSP** | 自定義 |
| **適合場景** | 通用問答 | 編碼輔助 | **DevOps / CLI 自動化 / 全流程** | 企業級 AI 系統 |

### 1.2.1 與 IDE Copilot 的互補關係

Copilot CLI 與 VS Code IDE Copilot 可以**無縫銜接**：

```bash
# 在 CLI 中使用 /plan 模式規劃任務
> /plan 重構 UserService 為 Clean Architecture

# 完成規劃後，切換到 VS Code 繼續
> /ide
# Copilot CLI 會自動在 VS Code 中開啟相關檔案
```

> 💡 **提示**：使用 `/ide` 指令可將 CLI Session 的上下文帶入 VS Code，實現 CLI → IDE 的無縫轉場。

## 1.3 適用場景

### 最適合使用 Copilot CLI 的場景

| 場景類型 | 說明 | 範例 |
|---------|------|------|
| **CLI 操作** | 不熟悉的 Shell 指令 | 「幫我找出佔用 8080 port 的 process」 |
| **Git 操作** | 複雜的 Git 工作流 | 「幫我 rebase 到 main 並解決衝突」 |
| **DevOps** | CI/CD Pipeline 管理 | 「建立一個 GitHub Actions workflow 跑 ESLint」 |
| **Backend 開發** | API 開發與除錯 | 「在 Spring Boot 專案新增一個 REST API」 |
| **Infra 管理** | 基礎設施操作 | 「幫我建立 Docker Compose 設定」 |
| **Code Review** | PR 審查與管理 | 「檢查 PR #123 的變更是否有安全問題」 |
| **Batch Job** | 批次作業開發 | 「幫我建立一個資料匯出的 Batch Job」 |
| **多代理協作** | 平行分工大型任務 | 「用 /fleet 平行重構前後端 API 和測試」 |
| **非同步委派** | 背景執行耗時任務 | 「/delegate 修復所有 Lint 錯誤並開 PR」 |
| **深度研究** | 技術調研與報告 | 「/research 比較 Redis 與 Memcached」 |

### 不適合的場景

- 需要圖形化介面的操作（如 UI 設計）
- 高度機密的資料處理（需注意資料外洩風險）
- 需要即時互動的 Debug Session（建議搭配 IDE Copilot）

---

# 第 2 章：系統架構整合設計

## 2.1 Copilot CLI 在企業架構中的角色

### 架構定位圖

```mermaid
graph TB
    subgraph "開發者工作站"
        DEV[開發者]
        CLI[GitHub Copilot CLI]
        IDE[VS Code + Copilot]
        TERM[Terminal]
    end

    subgraph "GitHub 平台"
        REPO[GitHub Repository]
        PR[Pull Requests]
        ISSUE[Issues]
        ACTIONS[GitHub Actions]
        MCP_GH[GitHub MCP Server]
    end

    subgraph "企業架構"
        subgraph "前端"
            VUE[Vue 3 + TypeScript]
            TAILWIND[Tailwind CSS]
            MFE[Micro-Frontend]
        end
        subgraph "後端"
            SPRING[Spring Boot 3.x]
            CLEAN[Clean Architecture]
            API_GW[API Gateway]
        end
        subgraph "基礎設施"
            DOCKER[Docker / Podman]
            K8S[Kubernetes]
            DB[(Oracle / DB2 / PostgreSQL)]
            MQ[Message Queue]
            CACHE[Redis Cache]
        end
    end

    subgraph "DevOps Pipeline"
        CI[CI/CD Pipeline]
        SCAN[程式碼掃描]
        TEST[自動測試]
        DEPLOY[自動部署]
    end

    DEV --> CLI
    DEV --> IDE
    CLI --> TERM
    CLI --> MCP_GH
    MCP_GH --> REPO
    MCP_GH --> PR
    MCP_GH --> ISSUE
    CLI --> ACTIONS
    CLI --> SPRING
    CLI --> VUE
    CLI --> DOCKER
    ACTIONS --> CI
    CI --> SCAN
    CI --> TEST
    CI --> DEPLOY

    style CLI fill:#ff6b6b,stroke:#333,stroke-width:3px,color:#fff
    style MCP_GH fill:#4ecdc4,stroke:#333,stroke-width:2px
```

## 2.2 與開發流程整合

### Git Flow 整合

```mermaid
sequenceDiagram
    participant Dev as 開發者
    participant CLI as Copilot CLI
    participant Git as Git
    participant GH as GitHub

    Dev->>CLI: 開始新功能開發
    CLI->>Git: git checkout -b feature/user-auth
    Dev->>CLI: 實作認證 API
    CLI->>CLI: 掃描 Codebase + 產生程式碼
    CLI->>Git: 自動 Commit（帶訊息）
    Dev->>CLI: 建立 PR
    CLI->>GH: 建立 PR + 自動 Summary
    CLI->>GH: 觸發 CI/CD
    Dev->>CLI: 檢查 PR 狀態
    CLI->>GH: 取得 CI 結果 + Review 建議
    Dev->>CLI: Merge PR
    CLI->>GH: Squash Merge + 刪除分支
```

### CI/CD Pipeline 整合

```mermaid
graph LR
    subgraph "開發階段"
        A[Copilot CLI<br/>產生程式碼] --> B[Copilot CLI<br/>產生測試]
    end
    subgraph "CI 階段"
        B --> C[GitHub Actions<br/>自動測試]
        C --> D[SonarQube<br/>程式碼掃描]
        D --> E[Security Scan<br/>弱掃]
    end
    subgraph "CD 階段"
        E --> F[Docker Build]
        F --> G[Stage 部署]
        G --> H[Production 部署]
    end

    style A fill:#ff6b6b,stroke:#333,color:#fff
    style B fill:#ff6b6b,stroke:#333,color:#fff
```

## 2.3 Agentic Workflow 設計模式

在企業環境中，Copilot CLI 提供三種 Agentic Workflow 模式：

### 2.3.1 Interactive Mode（互動模式）

逐步確認每個操作，適合敏感程式碼修改。

```mermaid
graph TD
    A[開發者輸入需求] --> B{Copilot CLI 分析}
    B --> C[Plan Mode<br/>建立執行計畫]
    C --> D[步驟 1：掃描現有程式碼]
    D --> E[步驟 2：產生新程式碼]
    E --> F[步驟 3：產生測試]
    F --> G[步驟 4：執行測試]
    G --> H{測試通過？}
    H -->|是| I[步驟 5：Commit + PR]
    H -->|否| J[自動修復]
    J --> G
    I --> K[完成]
```

### 2.3.2 Autopilot Mode（自動駕駛模式）

全自動完成任務，無需逐步確認。按 `Shift+Tab` 循環切換模式（Interactive → Plan → Autopilot）。

```mermaid
graph TD
    A[開發者輸入需求] --> B[Autopilot 自動分析]
    B --> C[自動規劃所有步驟]
    C --> D[自動執行所有步驟<br/>不需人工確認]
    D --> E{任務完成？}
    E -->|是| F[task_complete<br/>產生 Markdown 摘要]
    E -->|否| G[自動修復錯誤]
    G --> D
    F --> H[開發者審查結果]
```

> ⚠️ **注意**：Autopilot 模式需要先在權限對話框中確認允許的工具。API 錯誤時會自動停止，不會無限循環（v1.0.4+）。

### 2.3.3 Fleet Mode（艦隊模式）

透過 `/fleet` 指揮多個子代理**平行執行**任務，大幅縮短複雜任務的完成時間。

```mermaid
graph TD
    A[開發者輸入需求] --> B[Fleet 指揮官分析]
    B --> C[拆分為多個子任務]
    C --> D1[子代理 1<br/>前端 API 對接]
    C --> D2[子代理 2<br/>後端 Controller]
    C --> D3[子代理 3<br/>單元測試]
    C --> D4[子代理 4<br/>整合測試]
    D1 --> E[Fleet 指揮官驗證<br/>子代理工作結果]
    D2 --> E
    D3 --> E
    D4 --> E
    E --> F{所有子任務完成？}
    F -->|是| G[合併結果]
    F -->|否| H[重新分配失敗任務]
    H --> D1
    G --> I[完成]
```

```bash
# Fleet 模式使用範例
> /fleet 重構訂單模組：前端 API 對接、後端 CRUD、單元測試、E2E 測試，各自平行處理
```

> 💡 **提示**：在 Plan Mode 審核計畫時，系統會自動建議「autopilot + fleet」選項來加速可平行化的工作。

### 2.3.4 Delegate Mode（委派模式）

透過 `/delegate` 將任務非同步委派給 Copilot Coding Agent，在 GitHub 背景執行。

```mermaid
sequenceDiagram
    participant Dev as 開發者
    participant CLI as Copilot CLI
    participant Agent as Copilot Coding Agent
    participant GH as GitHub

    Dev->>CLI: /delegate 修復所有 ESLint 錯誤
    CLI->>CLI: Commit 未暫存變更至新分支
    CLI->>GH: 建立新分支 + 開啟 PR
    CLI->>Agent: 非同步委派任務
    Note right of Agent: 背景獨立執行
    Agent->>GH: 逐步 Commit 修復結果
    Agent->>GH: 更新 PR 狀態
    Dev->>CLI: 繼續其他工作...
    Dev->>CLI: /tasks 查看背景任務進度
    CLI->>GH: 查詢 Agent 狀態
```

```bash
# Delegate 使用範例
> /delegate 在 develop 分支上修復所有 SonarQube 發現的 Code Smell

# 快捷方式（& 前綴等同 /delegate）
> & 幫我把所有 Java 檔案的 System.out.println 改為 Logger
```

### 實務案例：企業級 API 開發 Agentic Workflow

```bash
# 使用程式化介面執行完整流程
copilot -p "在 Spring Boot 專案建立 /api/v1/users 的 CRUD API，
遵循 Clean Architecture，使用 JPA + PostgreSQL，
並產生 JUnit 5 測試，最後建立 PR" \
  --allow-tool='shell(mvn)' \
  --allow-tool='shell(git)' \
  --allow-tool='write'
```

---

# 第 3 章：安裝與環境設定

## 3.1 支援平台

| 平台 | 支援狀況 | 安裝方式 |
|------|---------|---------|
| **Windows** | ✅ 支援 | WinGet / MSI / npm |
| **macOS** | ✅ 支援 | Homebrew / npm / 安裝腳本 |
| **Linux** | ✅ 支援 | Homebrew / npm / 安裝腳本 |
| **WSL** | ✅ 支援 | 同 Linux（需注意 `/terminal-setup`） |
| **Codespaces** | ✅ 支援 | 預先安裝 |
| **SSH / Remote** | ✅ 支援 | Device Flow 登入 |

## 3.2 前置需求

- **GitHub 帳號**：需有 GitHub Copilot 訂閱（個人 / 組織 / 企業方案皆可；含 Copilot Free / Pro / Pro+ / Business / Enterprise）
- **Node.js 22+**（使用 npm 安裝時）
- **PowerShell v6+**（Windows 用戶）
- **Git**（若需使用 Plugin、Marketplace、`#` Issue/PR 參照等功能）
- **組織設定**：若透過組織取得 Copilot，需確認管理員已在組織或企業設定中啟用 Copilot CLI 政策
  - 參閱：[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization)

## 3.3 安裝步驟

### 方式 1：npm 安裝（所有平台，推薦）

```bash
# 安裝最新穩定版
npm install -g @github/copilot

# 安裝預發佈版本
npm install -g @github/copilot@prerelease
```

> ⚠️ **注意**：若 `~/.npmrc` 中設定了 `ignore-scripts=true`，需使用：
> ```bash
> npm_config_ignore_scripts=false npm install -g @github/copilot
> ```

### 方式 2：WinGet 安裝（Windows）

```powershell
# 安裝穩定版
winget install GitHub.Copilot

# 安裝預發佈版
winget install GitHub.Copilot.Prerelease
```

### 方式 3：Homebrew 安裝（macOS / Linux）

```bash
# 安裝穩定版
brew install copilot-cli

# 安裝預發佈版
brew install copilot-cli@prerelease
```

### 方式 4：安裝腳本（macOS / Linux）

```bash
# 使用 curl
curl -fsSL https://gh.io/copilot-install | bash

# 使用 wget
wget -qO- https://gh.io/copilot-install | bash

# 以 root 安裝到 /usr/local/bin
curl -fsSL https://gh.io/copilot-install | sudo bash

# 安裝指定版本到自訂目錄
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.369" PREFIX="$HOME/custom" bash
```

### 方式 5：直接下載

從 [GitHub Releases](https://github.com/github/copilot-cli/releases/) 下載對應平台的執行檔。自 v0.0.389 起，Release 頁面同時提供 MSI 安裝包（Windows）與平台專屬執行檔，並附帶 SHA256 校驗碼可供驗證完整性。

### 方式 6：Codespaces / DevContainers

在 GitHub Codespaces 環境中，Copilot CLI 已預先安裝。直接在 Terminal 輸入 `copilot` 即可啟動。

### 驗證安裝

```bash
# 查看安裝版本
copilot --version

# 查看二進位版本（不啟動完整 CLI）
copilot --binary-version
```

## 3.4 身份驗證

### 互動式登入（推薦）

```bash
# 啟動 Copilot CLI
copilot

# 首次啟動會提示登入，輸入：
/login
# 跟隨畫面指示完成 GitHub OAuth 驗證
```

### 使用 Personal Access Token（適合 CI/CD）

1. 前往 [Fine-grained personal access tokens](https://github.com/settings/personal-access-tokens/new)
2. 在「Permissions」中點選 **Add permissions**，選擇 **Copilot Requests**
3. 點選 **Generate token**
4. 設定環境變數（依優先順序）：

```bash
# 方式 1（最高優先）
export COPILOT_GITHUB_TOKEN="ghp_xxxxxxxxxxxx"

# 方式 2
export GH_TOKEN="ghp_xxxxxxxxxxxx"

# 方式 3
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
```

> 💡 **提示**：在 CI/CD 環境中建議使用 `COPILOT_GITHUB_TOKEN` 環境變數搭配 Secrets Manager。

## 3.5 初始化設定

### 基本設定

```bash
# 查看所有設定選項
copilot help config

# 設定檔位置（預設）
# ~/.copilot/config.json

# 變更設定檔位置
export COPILOT_HOME="$HOME/.my-copilot"
```

### 建議的企業初始設定

```json
// ~/.copilot/config.json 範例
{
  "model": "claude-sonnet-4-5",
  "theme": "dark",
  "autoCompact": true,
  "includeCoAuthoredBy": true,
  "effortLevel": "medium",
  "autoUpdatesChannel": "stable",
  "trustedDirectories": [
    "/home/dev/projects",
    "/workspace"
  ]
}
```

> 📝 **設定名稱變更**（v1.0.10 起）：設定鍵已統一改為 camelCase 格式（如 `includeCoAuthoredBy`、`effortLevel`、`autoUpdatesChannel`、`statusLine`），舊名稱亦仍相容。

## 3.6 常見錯誤與排除

| 錯誤訊息 | 可能原因 | 解決方案 |
|---------|---------|---------|
| `command not found: copilot` | 未正確安裝 | 重新安裝並確認 PATH |
| `Authentication failed` | Token 過期或無效 | 執行 `/login` 重新驗證 |
| `Policy not enabled` | 組織未啟用 CLI 政策 | 請管理員啟用 Copilot CLI 政策 |
| `Node.js version too old` | Node.js < 22 | 升級 Node.js 至 22+ |
| `Permission denied` | 檔案權限不足 | 使用 `sudo` 或修改安裝路徑 |
| `MCP server connection failed` | MCP 設定錯誤 | 檢查 `mcp-config.json`；執行 `/mcp` 查看狀態 |
| `classic PAT (ghp_) detected` | 使用了傳統 PAT | 改用 Fine-grained PAT 並加上 Copilot Requests 權限 |
| `Session file is corrupted` | 跨版本 Session 不相容 | 開啟新 Session（`/new`）或指定 `--resume` 選取功能正常的 Session |
| `Third-party MCP servers blocked` | 組織策略封鎖第三方 MCP | 請管理員更新 MCP 允許清單政策 |
| `/terminal-setup` 出現錯誤 | WSL 環境特殊路徑問題 | v1.0.10+ 已改善；更新至最新版 |

---

# 第 4 章：核心功能教學

## 4.1 自然語言轉指令

### Shell 指令生成

Copilot CLI 最基本的功能是將自然語言轉換為準確的 Shell 指令。

**範例 1：系統管理**

```
> 找出佔用 8080 port 的 process 並終止它

Copilot 建議：
$ lsof -i :8080 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

**範例 2：檔案操作**

```
> 找出 src 目錄下所有超過 500 行的 Java 檔案

Copilot 建議：
$ find src -name "*.java" -exec awk 'END{if(NR>500) print FILENAME": "NR" lines"}' {} \;
```

**範例 3：日誌分析**

```
> 分析最近 1 小時的 Spring Boot 日誌，找出所有 ERROR 等級的錯誤

Copilot 建議：
$ grep "ERROR" logs/application.log | awk -v d="$(date -d '1 hour ago' '+%Y-%m-%d %H')" '$0 >= d'
```

### Git 操作

**範例 1：分支管理**

```
> 建立一個新的 feature 分支，基於最新的 develop 分支

Copilot 執行：
$ git fetch origin
$ git checkout develop
$ git pull origin develop
$ git checkout -b feature/new-feature
```

**範例 2：Rebase 操作**

```
> 把目前分支 rebase 到 main，保持線性歷史

Copilot 執行：
$ git fetch origin
$ git rebase origin/main
```

**範例 3：Cherry-pick**

```
> 把 commit abc1234 從 hotfix 分支 cherry-pick 到 release 分支

Copilot 執行：
$ git checkout release
$ git cherry-pick abc1234
```

**範例 4：複雜 Git 操作**

```
> 互動式 rebase 最近 5 個 commit，合併成一個

Copilot 執行：
$ git rebase -i HEAD~5
```

## 4.2 Agentic Workflow

Copilot CLI 的 Agentic 模式能夠自主執行多步驟任務，是企業開發中最強大的功能。

### 自動產生程式碼

**範例：建立 Spring Boot REST Controller**

```
> 在 Spring Boot 專案中建立一個 UserController，實作 CRUD API，
  使用 Clean Architecture，包含 Service 層和 Repository 層

Copilot 會自動：
1. 掃描現有專案結構（找到 src/main/java 目錄）
2. 分析現有程式碼風格（包名、命名慣例）
3. 建立以下檔案：
   - UserController.java
   - UserService.java
   - UserServiceImpl.java
   - UserRepository.java
   - UserDTO.java
   - User.java (Entity)
4. 自動處理依賴注入和 Spring 註解
```

### 自動修 Bug

**範例：修復 NullPointerException**

```
> 應用程式在 UserService.getUserById 拋出 NullPointerException，
  請幫我找到原因並修復

Copilot 會自動：
1. 讀取 UserService.java 的程式碼
2. 分析可能的 null 來源
3. 檢查 Repository 回傳值
4. 添加適當的 null 檢查或 Optional 處理
5. 驗證修復（如果有測試的話，會執行測試）
```

### 自動產生測試

**範例：為現有 Service 類別產生測試**

```
> 為 UserService 產生完整的 JUnit 5 測試，包含正常流程和邊界案例，
  使用 Mockito 模擬 Repository

Copilot 會自動：
1. 讀取 UserService.java 的程式碼
2. 分析所有 public 方法
3. 產生 UserServiceTest.java：
   - @BeforeEach 設定
   - 正常案例測試
   - 邊界條件測試（null、空值、不存在的 ID）
   - Exception 測試
4. 執行測試確認通過
```

### Plan Mode（計畫模式）

在互動式介面中按 `Shift + Tab` 可切換到 Plan Mode。Copilot 會先建立結構化的實作計畫，再開始寫程式碼。

```
> [Plan Mode] 重構 UserService，將單體式的 Service 拆分成符合
  SOLID 原則的多個小 Service

Copilot Plan：
 ✅ Phase 1：分析現有 UserService（12 個 public 方法）
 ✅ Phase 2：識別職責（認證、Profile、Permission）
 ✅ Phase 3：建立 UserAuthService（登入、登出、驗證）
 ✅ Phase 4：建立 UserProfileService（查詢、更新 Profile）
 ✅ Phase 5：建立 UserPermissionService（權限管理）
 ✅ Phase 6：更新 UserController 的依賴注入
 ✅ Phase 7：遷移測試
 ✅ Phase 8：執行所有測試確認

是否開始執行？(Y/N)
```

## 4.3 Codebase Context 分析

### 專案理解能力

Copilot CLI 會自動讀取和理解專案結構：

```
> 分析這個專案的架構，告訴我主要的模組和它們之間的關係

Copilot 會讀取：
- pom.xml / build.gradle（依賴關係）
- 目錄結構（模組劃分）
- package-info.java（如果有的話）
- README.md / docs/
- .github/copilot-instructions.md（自訂指令）
```

### 使用 @ 引用特定檔案

```bash
# 在互動式介面中引用檔案
> 解釋 @src/main/java/com/tutorial/java/App.java 的功能

# 引用多個檔案
> 比較 @UserController.java 和 @AdminController.java 的差異

# 引用設定檔
> 根據 @pom.xml 的依賴，建議我該升級哪些套件
```

### 最佳化提問技巧

| 層級 | 提問方式 | 效果 |
|------|---------|------|
| ❌ 差 | 「幫我寫一個 API」 | 缺乏上下文，結果不精確 |
| ⚠️ 一般 | 「幫我在 UserController 加一個 GET API」 | 有基本方向，但細節不足 |
| ✅ 好 | 「在 @UserController.java 新增 GET /api/v1/users/{id}，回傳 UserDTO，使用 @UserService.java 的 findById 方法，錯誤時回傳 404」 | 具體、有引用、有預期結果 |
| 🌟 最佳 | 使用 Plan Mode 先討論再實作 | 多步驟複雜任務的最佳作法 |

### Custom Instructions（自訂指令）

Copilot CLI 支援多層級的自訂指令，用來告知 Copilot 你的專案慣例：

```markdown
<!-- .github/copilot-instructions.md -->
# 專案開發規範

## 架構
- 使用 Clean Architecture
- Controller -> Service -> Repository -> Entity

## 命名慣例
- 類別名：PascalCase
- 方法名：camelCase
- 常數：UPPER_SNAKE_CASE
- REST API 路徑：kebab-case

## 測試
- 使用 JUnit 5 + Mockito
- 測試覆蓋率需達 80%
- 命名格式：should_DoSomething_When_Condition

## 日誌
- 使用 Log4j2
- ERROR：系統錯誤
- WARN：業務異常
- INFO：關鍵操作
- DEBUG：開發除錯
```

支援的指令檔類型：

| 檔案類型 | 位置 | 作用範圍 |
|---------|------|---------|
| `copilot-instructions.md` | `.github/` | 整個 Repository |
| `*.instructions.md` | `.github/instructions/` | 依 Path 匹配 |
| `AGENTS.md` | 任何目錄 | Agent 行為定義 |

## 4.4 GitHub 整合

### 建立 Pull Request

```
> 將目前分支的變更建立一個 PR 到 develop 分支，
  自動產生 Summary 並加上 "feature" 標籤

Copilot 執行：
1. git push origin feature/user-auth
2. 建立 PR（含自動生成的 Summary）
3. 添加標籤
4. 指派 Reviewer（如果有設定）
```

### PR Summary 自動生成

```
> 為 PR #42 產生詳細的 Summary

Copilot 生成：
## Summary
本 PR 實作使用者認證模組，包含：
- JWT Token 認證機制
- Refresh Token 支援
- 角色權限控管（RBAC）

## Changes
- 新增 `AuthController.java`（4 個 API endpoint）
- 新增 `JwtTokenService.java`（Token 生成與驗證）
- 更新 `SecurityConfig.java`（Spring Security 設定）
- 新增 `AuthServiceTest.java`（23 個測試案例）

## Testing
- 單元測試：23/23 通過
- 整合測試：8/8 通過
```

### Issue 管理

```
# 列出分配給我的 Issue
> List all open issues assigned to me in my-org/my-repo

# 從 Issue 開始開發
> 我被指派了這個 Issue：https://github.com/my-org/my-repo/issues/42
  開始處理它，建立合適的分支名稱

# 建立新 Issue
> 在 my-org/my-repo 建立一個 Bug Report Issue，
  描述 UserService.getUserById 在 ID 不存在時拋出 500 而非 404

# 檢查 PR 的程式碼變更
> 檢查 PR https://github.com/my-org/my-repo/pull/57 的變更，
  回報任何嚴重的錯誤
```

### GitHub Actions 整合

```
# 查看 workflow
> 列出這個 repo 中所有的 Actions workflows

# 建立新 workflow
> 建立一個 GitHub Actions workflow，在 PR 上執行：
  1. Maven 編譯
  2. JUnit 測試
  3. SonarQube 分析
  4. 安全掃描
  若有錯誤則阻止 Merge

# 查看 workflow 執行結果
> 顯示上次 CI 執行的結果和錯誤日誌
```

## 4.5 LSP 語言伺服器整合

Copilot CLI 支援 Language Server Protocol（LSP），為程式碼提供智慧型功能，如跳轉到定義（go-to-definition）、懸停資訊（hover）、診斷（diagnostics）等。

### 安裝語言伺服器

Copilot CLI **不附帶任何 LSP 伺服器**（自 v0.0.400 移除了內建的 TypeScript 和 Python LSP），需自行安裝：

```bash
# TypeScript
npm install -g typescript-language-server

# Python（由 Plugin 或獨立安裝提供）
pip install python-lsp-server

# Java
# 使用 Eclipse JDT Language Server 或其他 LSP 實作
```

### LSP 設定檔

可在使用者層級或 Repository 層級配置 LSP 伺服器：

| 層級 | 設定檔位置 | 作用範圍 |
|------|-----------|---------|
| **使用者層級** | `~/.copilot/lsp-config.json` | 所有專案 |
| **Repository 層級** | `.github/lsp.json` | 特定專案 |

**設定範例：**

```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileExtensions": {
        ".ts": "typescript",
        ".tsx": "typescript"
      }
    },
    "java": {
      "command": "jdtls",
      "args": ["--stdio"],
      "fileExtensions": {
        ".java": "java"
      }
    }
  }
}
```

### 查看 LSP 狀態

```bash
# 在互動式介面中查看 LSP 狀態
/lsp

# 查看特定伺服器的詳細資訊
/lsp show
```

> 💡 **提示**：Plugin 也可以附帶 LSP Server 設定，安裝 Plugin 後會自動載入對應的 LSP 伺服器。可透過 `/lsp show` 確認已載入的伺服器清單。LSP 請求逾時已從 30 秒延長至 90 秒（v0.0.413+），可在 `lsp.json` 中自訂逾時。

---

## 4.6 Hooks 鉤子系統

Hooks 允許在 Agent 執行的關鍵時間點執行自訂 Shell 指令，實現驗證、日誌記錄、安全掃描或工作流自動化。

### Hook 事件類型

| Hook 事件 | 觸發時機 | 典型用途 |
|-----------|---------|---------|
| `preToolUse` | 工具執行**前** | 驗證指令安全性、修改參數、要求確認 |
| `postToolUse` | 工具執行**後** | 記錄日誌、觸發通知 |
| `sessionStart` | Session 啟動時 | 注入額外 Context、環境檢查 |
| `preCompact` | Context 壓縮**前** | 儲存重要資訊 |
| `subagentStart` | 子代理啟動時 | 為子代理注入額外 Context |
| `agentStop` / `subagentStop` | Agent 完成時 | 清理資源、發送通知 |

### Hook 設定檔位置

| 位置 | 作用範圍 |
|------|---------|
| `~/.copilot/hooks/` | 個人層級（所有專案） |
| `.github/hooks/` | Repository 層級 |
| `settings.json` / `settings.local.json` / `config.json` 內 | 混合設定 |

### Hook 設定範例

```json
// .github/hooks/hooks.json
{
  "hooks": {
    "preToolUse": [
      {
        "matcher": "shell",
        "command": "echo 'Tool about to execute: $TOOL_NAME'",
        "timeout": 10
      }
    ],
    "postToolUse": [
      {
        "matcher": "write",
        "command": "echo 'File written: $FILE_PATH' >> .copilot-audit.log"
      }
    ]
  }
}
```

> ⚠️ **重要**：
> - `preToolUse` Hook 可以 **拒絕工具執行**（deny）或 **修改參數**
> - Hook 支援 `ask` 權限決策，在工具執行前要求使用者確認
> - Repository 層級的 Hook 僅在檔案夾信任確認後才會載入
> - Hook 設定相容 VS Code、Claude Code 和 CLI 三個平台，支援 PascalCase 和 camelCase 事件名稱

---

## 4.7 Skills 技能系統

Skills 是可擴充的專門指令集，讓 Copilot 能執行特定領域的任務。

### Skill 檔案位置

| 位置 | 作用範圍 |
|------|---------|
| `~/.copilot/skills/` | 個人層級 |
| `~/.agents/skills/` | 個人層級（v1.0.11 新增，與 VS Code 一致） |
| `.agents/skills/` | Repository 層級 |
| `.github/skills/` | Repository 層級 |

### Skill 檔案格式

```markdown
<!-- .agents/skills/database-migration.md -->
---
name: database-migration
description: 執行資料庫 Migration 操作
allowed-tools:
  - shell(mvn)
  - shell(flyway)
  - write
---

# Database Migration Skill

你是資料庫 Migration 專家，負責：
1. 建立 Flyway migration 腳本
2. 驗證 Migration 相容性
3. 執行 Migration 並驗證結果
```

### Skill 管理指令

```bash
# 查看所有已載入的 Skills
/skills

# 新增 Skill
/skills add <path>

# 以 Slash Command 方式呼叫 Skill
/database-migration
```

> 💡 **提示**：Skill 名稱支援大寫字母、底線、點號和空格。未指定 name/description 時系統會自動從 Markdown 檔名推導。Frontmatter 中可使用 `disable-model-invocation` 控制模型是否能自動呼叫該 Skill。

---

## 4.8 Plugin 插件生態系

Plugin 是 Copilot CLI 最完整的擴充機制，可打包 MCP Server、LSP Server、Agent、Skill、Hook，形成可分享的功能模組。

### Plugin 管理指令

```bash
# 開啟 Plugin Marketplace
/plugin marketplace add

# 從 GitHub Repo 安裝
/plugin install <github-repo-url>

# 從本機目錄安裝
/plugin install /path/to/plugin

# 從 SSH URL 安裝
/plugin install ssh://git@github.com/org/plugin.git

# 更新已安裝的 Plugin
/plugin update

# 解除安裝
/plugin uninstall <name>

# 查看已安裝的 Plugin 清單
/plugin list
```

### Plugin 結構

Plugin 使用 `plugin.json` 或 `.claude-plugin/plugin.json` / `.plugin/` 目錄結構：

```json
// plugin.json
{
  "name": "my-enterprise-plugin",
  "version": "1.0.0",
  "description": "企業內部開發輔助工具",
  "mcpServers": { ... },
  "lspServers": { ... },
  "agents": [ ... ],
  "skills": [ ... ],
  "hooks": { ... }
}
```

### 預設 Marketplace

Copilot CLI 內建以下預設 Marketplace：
- **copilot-plugins**：官方插件市集
- **awesome-copilot**：社群精選插件

可在 Repository 設定中定義 `extraKnownMarketplaces` 新增私有市集。

> 💡 **提示**：使用 `--plugin-dir` 旗標可在啟動時載入本地開發中的 Plugin，便於開發與測試。外部 Plugin 在 `/plugin list` 中會顯示在獨立的「External Plugins」區段。

---

## 4.9 Extensions 擴充機制

Extensions 是輕量級的擴充方式（v1.0.3 起以實驗性功能提供），可以直接用 `@github/copilot-sdk` 為 Copilot 撰寫自訂工具和 Hook。

### Extension 管理

```bash
# 查看、啟用與停用 Extensions
/extensions

# 啟動時載入外部 Extension
copilot --plugin-dir /path/to/extension
```

### Extension 格式

Extension 可以是 CommonJS 模組（`extension.cjs`）或 ES Module，支援：
- 註冊自訂 Slash Command
- 提供自訂工具與 Hook
- 在 Session 啟動或加入時注入功能

> 📝 **注意**：可透過 Extension mode 設定控制擴充性。多個 Extension 的 Hook 會自動合併而非互相覆蓋（v1.0.11+）。

---

## 4.10 Copilot Memory 跨 Session 記憶

Copilot Memory 讓 Copilot 建立對 Repository 的持久理解，儲存編碼慣例、模式與偏好等「記憶」，減少每次 Session 都要重複解釋的負擔。

### 記憶運作方式

```mermaid
graph LR
    A[Session 1<br/>學到專案慣例] --> B[(Memory Store<br/>~/.copilot/memories)]
    C[Session 2<br/>回憶過去的工作] --> B
    D[Session 3<br/>記住 PR 與檔案] --> B
    B --> E[跨 Session<br/>持續累積知識]
```

### 記憶功能

- **自動學習**：Copilot 在工作過程中自動識別並儲存有用的模式
- **跨 Session 查詢**：詢問過去的工作、修改過的檔案、建立的 PR
- **手動管理**：Copilot 使用 `store_memory` 工具記錄 Subject、Fact 和 Citations

```bash
# 詢問過去的工作記錄
> 我上次在哪個分支做了什麼修改？

# 查詢之前的 PR
> 顯示我最近建立的 PR 清單和摘要
```

> ⚠️ **注意**：Memory 功能在非 Git Repository 中會優雅降級。若 Repository 不存在或無寫入權限，會顯示明確的錯誤提示。此功能屬實驗性質（v0.0.412+）。

---

## 4.11 ACP（Agent Client Protocol）

ACP 是一個開放標準協定，允許第三方工具、IDE 或自動化系統將 Copilot CLI 當作 AI Agent 使用。

### 啟動 ACP 伺服器

```bash
# 啟動 ACP 模式
copilot --acp

# ACP 模式支援的功能
# - 載入現有 Session
# - 管理 Agent / Plan / Autopilot 模式
# - 設定推理強度（reasoning effort）
# - 完整的 MCP 設定支援
# - 工具權限控制（--yolo, --allow-all 等）
```

### ACP 能力

| 能力 | 說明 |
|------|------|
| Session 管理 | 列出、建立、加入、恢復 Session |
| 模型切換 | 在 Session 中動態變更模型 |
| Slash Command | SDK 客戶端可註冊自訂 Slash Command |
| Elicitation | 向使用者顯示互動式表單 |
| Plan 模式 | 支援 Plan 審核與 Autopilot |
| Fleet 模式 | 支援平行子代理 |
| Skills / Plugins / MCP | 完整的擴充體系支援 |

### SDK 整合

```bash
# 安裝 Copilot CLI（即包含 SDK Runtime）
npm install -g @github/copilot

# 使用 Copilot SDK 為應用程式內建 Agent 能力
# 參閱：https://github.com/github/copilot-sdk
```

> 💡 **提示**：ACP 客戶端可透過 `session.ui.elicitation` 向使用者顯示互動式對話框，並可透過 `session.shell.exec` / `session.shell.kill` 執行與管理 Shell 指令。

---

# 第 5 章：進階使用技巧（企業級）

## 5.1 Prompt Engineering（CLI 版本）

### Prompt 設計原則

在 CLI 中撰寫 Prompt 的最佳實務：

| 原則 | 說明 | 範例 |
|------|------|------|
| **具體明確** | 指定技術棧、框架、命名 | 「使用 Spring Boot 3.x + JPA」而非「寫一個 API」 |
| **提供上下文** | 使用 @ 引用檔案 | 「參考 @UserController.java 的風格」 |
| **指定輸出格式** | 說明預期結果 | 「回傳 JSON 格式，包含 status 和 data」 |
| **分步驟** | 複雜任務拆解 | 使用 Plan Mode |
| **限制範圍** | 明確不要做什麼 | 「不要修改現有的測試」 |

### 企業級 Prompt 範本

**範本 1：API 開發**

```
在 @src/main/java/com/example/controller/ 新增 OrderController.java：
- 實作 POST /api/v1/orders（建立訂單）
- 使用 @OrderService.java 的 createOrder 方法
- Request Body 包含：customerId, items[], totalAmount
- 成功回傳 201 + OrderDTO
- 驗證失敗回傳 400 + ErrorResponse
- 使用 @Valid 驗證
- 添加 @Operation (Swagger) 註解
- 日誌使用 Log4j2
```

**範本 2：Bug 修復**

```
Bug 描述：當使用者同時發送多個下單請求時，庫存扣減出現 Race Condition。
相關檔案：@InventoryService.java, @OrderService.java
現象：庫存變成負數
要求：
1. 分析 Race Condition 的根因
2. 使用悲觀鎖或樂觀鎖修復
3. 新增對應的並發測試
4. 不要影響現有的單元測試
```

## 5.2 Context Engineering（讓 AI 更準）

### Context 優化策略

```mermaid
graph TD
    A[Context Engineering] --> B[靜態 Context]
    A --> C[動態 Context]
    A --> D[隱含 Context]

    B --> B1[copilot-instructions.md]
    B --> B2[AGENTS.md]
    B --> B3[instructions/*.md]

    C --> C1[@ 引用檔案]
    C --> C2[Prompt 中的描述]
    C --> C3[對話歷史]

    D --> D1[目錄結構]
    D --> D2[pom.xml / package.json]
    D --> D3[README.md]
```

### 建議的 Context 配置（企業級）

**Step 1：建立專案層級指令**

```markdown
<!-- .github/copilot-instructions.md -->

# 專案：企業級訂單管理系統

## 技術棧
- Java 21 + Spring Boot 3.x
- PostgreSQL 15 + JPA/Hibernate
- Redis 7.x（快取）
- Kafka（事件驅動）

## 架構規範
- Clean Architecture（4 層）
- Domain 層不依賴 Infrastructure
- 使用 Port/Adapter 模式

## API 規範
- RESTful API，版本化（/api/v1/）
- 回傳格式統一使用 ApiResponse<T>
- 錯誤碼：業務錯誤 4xxxx，系統錯誤 5xxxx
```

**Step 2：建立路徑專屬指令**

```markdown
<!-- .github/instructions/api-controllers.instructions.md -->
---
applyTo: "**/controller/**"
---

# Controller 層開發規範

- 只負責 HTTP 層的轉換與驗證
- 不包含業務邏輯
- 使用 @Valid 驗證 Request
- 使用 @Operation 產生 OpenAPI 文件
- 每個 endpoint 需有 @ApiResponse 定義
```

**Step 3：建立 Agent 定義**

```markdown
<!-- .github/agents/backend-expert.md -->
---
name: backend-expert
description: 後端開發專家
tools:
  - shell(mvn)
  - shell(git)
  - write
---

# Backend Expert Agent

你是一位資深 Java 後端工程師，專精於：
- Spring Boot 3.x 開發
- Clean Architecture 設計
- 高效能 API 開發
- 資料庫最佳化

## 工作原則
1. 所有程式碼必須有測試
2. 遵循 SOLID 原則
3. 使用 Log4j2 記錄關鍵操作
4. Controller 不直接存取 Repository
```

## 5.3 多步驟任務拆解（Task Chaining）

### 程式化介面的 Task Chaining

```bash
# Step 1：建立功能分支
copilot -p "建立一個名為 feature/order-api 的分支" \
  --allow-tool='shell(git)'

# Step 2：產生程式碼
copilot -p "在 Spring Boot 專案中實作 Order API 的 CRUD" \
  --allow-tool='write' \
  --allow-tool='shell(mvn)'

# Step 3：產生測試
copilot -p "為剛建立的 Order API 產生 JUnit 5 測試" \
  --allow-tool='write' \
  --allow-tool='shell(mvn test)'

# Step 4：建立 PR
copilot -p "Commit 所有變更並建立 PR 到 develop 分支" \
  --allow-tool='shell(git)'
```

### 使用腳本自動化

```bash
#!/bin/bash
# scripts/dev-workflow.sh - 自動化開發工作流

FEATURE_NAME=$1
DESCRIPTION=$2

echo "🚀 開始開發：${FEATURE_NAME}"

# 建立分支
copilot -p "建立 feature/${FEATURE_NAME} 分支" \
  --allow-tool='shell(git)'

# 實作功能
copilot -p "${DESCRIPTION}" \
  --allow-tool='write' \
  --allow-tool='shell(mvn)'

# 測試
copilot -p "執行所有測試，確認新功能沒有破壞現有功能" \
  --allow-tool='shell(mvn test)'

# 建立 PR
copilot -p "建立 PR，標題為 'feat: ${FEATURE_NAME}'，
  自動產生 Summary" \
  --allow-tool='shell(git)' \
  --allow-tool='shell(gh)'

echo "✅ 完成！"
```

## 5.4 與其他工具整合

### Docker 整合

```
> 為這個 Spring Boot 專案建立一個多階段 Dockerfile，
  使用 Eclipse Temurin JDK 21 作為 base image，
  最終映像使用 JRE，暴露 8080 port

> 建立 docker-compose.yml，包含：
  - Spring Boot 應用（2 個實例）
  - PostgreSQL 15
  - Redis 7
  - Nginx 作為 Load Balancer
```

### Kubernetes 整合

```
> 為應用程式建立 Kubernetes 部署清單：
  - Deployment（3 replicas）
  - Service（ClusterIP）
  - Ingress
  - ConfigMap（從 application.yml 轉換）
  - HPA（CPU > 70% 時自動擴展到 10）
```

### MCP Server 整合

```bash
# 在互動式介面中新增 MCP Server
/mcp add

# 查看已配置的 MCP Server
/mcp

# MCP 設定檔位置
# ~/.copilot/mcp-config.json
```

**MCP 設定範例：**

```json
{
  "mcpServers": {
    "github": {
      "type": "builtin"
    },
    "postgres-mcp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_URL": "postgresql://user:pass@localhost:5432/mydb"
      }
    },
    "docker-mcp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-docker"]
    }
  }
}
```

## 5.5 Session 管理與對話引導

### Session 生命週期管理

Copilot CLI 提供完整的 Session 管理能力，支援連續工作與上下文保存：

```bash
# 繼續最近的 Session
copilot --continue

# 選擇並恢復歷史 Session
copilot --resume
# Session 選擇器支援 / 搜尋過濾

# 在互動式介面中恢復 Session
/resume

# 開始新 Session（保留舊 Session 在背景）
/new

# 完全放棄目前 Session，重新開始
/clear

# /new 和 /clear 可帶 Prompt 直接開始新對話
/new 幫我分析 pom.xml 的依賴

# 重新命名 Session
/rename 訂單模組重構
# 或
/session rename 訂單模組重構

# 匯出 / 分享 Session
/share              # 儲存為 Markdown 檔案
/share gist         # 上傳為 GitHub Gist

# Session 使用統計
/session
```

> 📝 **v1.0.11 行為變更**：`/clear` 現在會完全放棄目前 Session，而 `/new` 則開啟新對話但保留舊 Session 在背景。`/cd` 在不同 Session 之間維持獨立的工作目錄。

### 對話引導（Steering the Conversation）

根據[官方文件](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli#steering-the-conversation)，您可以在 Copilot 思考時進行即時引導：

| 引導技巧 | 說明 |
|---------|------|
| **排隊訊息** | 在 Copilot 處理中發送後續訊息，引導方向或排隊附加指令 |
| **拒絕時給回饋** | 拒絕工具權限請求時，可同時提供替代建議，讓 Copilot 調整策略 |
| **中途 Esc** | 按 `Esc` 中斷目前操作並重新指引 |
| **Ctrl+C** | 中斷執行，Copilot 會保存對話狀態 |

### `#` 參照 GitHub 資源

自 v0.0.420 起，可直接輸入 `#` 來引用 GitHub Issue、Pull Request 和 Discussion：

```bash
# 引用 Issue（會顯示自動完成選單）
> 修復 #42 描述的 NullPointerException 問題

# 引用 PR
> 檢查 #57 的程式碼變更，報告潛在問題

# 引用 Discussion
> 總結 #100 中團隊討論的架構決策
```

### 自動 Context 管理

```bash
# 查看 Token 使用情況
/context

# 手動壓縮 Context
/compact

# 自動壓縮：當達到 Token 上限的 95% 時自動在背景執行
# 支援 preCompact hook 在壓縮前執行自訂邏輯
```

> 💡 **提示**：自動壓縮在背景進行，不會中斷對話。壓縮後 Skill 仍然有效。擴展思維（extended thinking）在壓縮後也會被保留。

---

# 第 6 章：安全與治理

## 6.1 工具審批機制

Copilot CLI 採用**逐步審批機制**（非 YOLO 模式下），每當它要使用可能修改或執行檔案的工具時，會詢問你的許可：

```
Copilot 想要執行：rm -rf ./build/

1. Yes（僅此次）
2. Yes, and approve 'rm' for the rest of the running session（本次 session 永久允許）
3. No, and tell Copilot what to do differently (Esc)（拒絕並指引）
```

> ⚠️ **重要**：選擇選項 2 會允許 Copilot 在整個 session 中使用該工具的**任何用法**。例如允許 `rm` 就等於允許 `rm -rf ./*`。

### 工具權限控制選項

| 選項 | 功能 | 安全等級 | 適用場景 |
|------|------|---------|---------|
| `--allow-all-tools` | 允許所有工具 | 🔴 低 | 受控環境 / CI |
| `--allow-tool='shell(mvn)'` | 允許特定指令 | 🟢 高 | 生產環境開發 |
| `--deny-tool='shell(rm)'` | 禁止特定指令 | 🟢 高 | 防止危險操作 |
| `--deny-tool='shell(git push)'` | 禁止 push | 🟢 高 | 防止意外推送 |
| 預設（無選項） | 每次詢問 | 🟢 最高 | 一般開發 |

### 企業建議的安全配置

```bash
# 開發環境：允許編譯和測試，禁止推送和刪除
copilot \
  --allow-tool='shell(mvn)' \
  --allow-tool='shell(gradle)' \
  --allow-tool='write' \
  --deny-tool='shell(rm)' \
  --deny-tool='shell(git push)' \
  --deny-tool='shell(git push --force)'

# CI/CD 環境：全自動但限制特定操作
copilot -p "執行測試並產生報告" \
  --allow-tool='shell(mvn test)' \
  --deny-tool='shell(rm)' \
  --deny-tool='shell(curl)' \
  --deny-tool='shell(wget)'
```

## 6.2 YOLO Mode 說明與風險

### 什麼是 YOLO Mode

YOLO Mode 等同於 `--allow-all-tools`，允許 Copilot 不經詢問即可執行所有操作。

```bash
# 啟用 YOLO Mode（互動式）
/yolo

# 或使用命令列選項
copilot --yolo
copilot --allow-all
```

### YOLO Mode 風險矩陣

| 風險類型 | 說明 | 嚴重度 |
|---------|------|--------|
| **資料刪除** | 可能執行 `rm -rf` | 🔴 嚴重 |
| **機密外洩** | 可能讀取 `.env` 並輸出到日誌 | 🔴 嚴重 |
| **Git 操作** | 可能執行 `git push --force` | 🟠 高 |
| **系統變更** | 可能修改系統設定檔 | 🟠 高 |
| **網路存取** | 可能下載不受信任的檔案 | 🟡 中 |

> ⚠️ **企業環境嚴禁使用 YOLO Mode**。如必須使用，應在 VM、Container 或沙箱環境中執行。

## 6.3 企業治理策略

### Copilot Policy 設定建議

| 政策 | 建議設定 | 說明 |
|------|---------|------|
| **Copilot CLI 存取** | 啟用（特定團隊） | 只對有需要的團隊開放 |
| **MCP Server** | 限制為白名單 | 只允許內部核準的 MCP |
| **模型選擇** | 限制可用模型 | 避免使用未經評估的模型 |
| **Trusted Directories** | 限制為專案目錄 | 避免存取系統目錄 |

### 資安控管措施

```mermaid
graph TD
    A[Copilot CLI 資安控管] --> B[輸入控管]
    A --> C[執行控管]
    A --> D[輸出控管]

    B --> B1[不在 Prompt 中包含密碼/金鑰]
    B --> B2[使用 .gitignore 排除敏感檔案]
    B --> B3[限制 Trusted Directories]

    C --> C1[禁用 YOLO Mode]
    C --> C2[使用 --deny-tool 限制危險指令]
    C --> C3[在 Container 中執行]

    D --> D1[Code Review 所有 AI 產出]
    D --> D2[SonarQube 掃描]
    D --> D3[安全掃描 Pipeline]
```

### 開發者安全守則

1. **永遠不要**在 Prompt 中包含密碼、API Key、Token 等機密資訊
2. **永遠不要**在 Home 目錄啟動 Copilot CLI
3. **永遠不要**在生產環境中使用 `--allow-all-tools`
4. **總是**審查 Copilot 建議的 Shell 指令再允許執行
5. **總是**在 Code Review 中注意 AI 產生的程式碼品質
6. **總是**使用 `--deny-tool` 禁止已知危險操作

## 6.4 Hooks 安全防護

利用 Hooks 系統建立自動化的安全防護網：

### 使用 preToolUse Hook 阻擋危險操作

```json
// .github/hooks/hooks.json
{
  "hooks": {
    "preToolUse": [
      {
        "matcher": "shell",
        "command": "python3 .github/hooks/validate-command.py",
        "timeout": 5,
        "permission": "deny"
      }
    ]
  }
}
```

```python
# .github/hooks/validate-command.py
import sys, os, json

# 從環境變數取得即將執行的指令
command = os.environ.get("TOOL_INPUT", "")

# 定義黑名單指令
BLACKLIST = [
    "rm -rf /", "rm -rf ~", "rm -rf .",
    "git push --force", "git reset --hard",
    "curl | bash", "wget | bash",
    "chmod 777", "dd if=",
]

for blocked in BLACKLIST:
    if blocked in command:
        print(f"BLOCKED: 危險指令被 Hook 攔截 - {blocked}", file=sys.stderr)
        sys.exit(1)

sys.exit(0)
```

### 使用 postToolUse Hook 記錄稽核日誌

```json
{
  "hooks": {
    "postToolUse": [
      {
        "matcher": "shell",
        "command": "echo \"$(date -Iseconds) | $USER | $TOOL_NAME | $TOOL_INPUT\" >> /var/log/copilot-audit.log"
      },
      {
        "matcher": "write",
        "command": "echo \"$(date -Iseconds) | FILE_WRITE | $FILE_PATH\" >> /var/log/copilot-audit.log"
      }
    ]
  }
}
```

### MCP Server 政策控管

| 政策 | 說明 | 設定方式 |
|------|------|---------|
| **第三方 MCP 封鎖** | 封鎖未經核準的第三方 MCP Server | 組織政策設定 |
| **MCP 允許清單** | 僅允許白名單中的 MCP Server | `MCP_ALLOWLIST` 實驗性旗標（v1.0.8+） |
| **MCP Registry 驗證** | 透過配置的 Registry 驗證 MCP Server | 組織政策 |

> ⚠️ **已知限制**（[官方文件](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli#known-mcp-server-policy-limitations)）：CLI 目前**無法支援**以下組織級 MCP 政策：
> - 「MCP servers in Copilot」（控制是否允許使用 MCP）
> - 「MCP Registry URL」（控制允許的 MCP Registry 來源）

### UNC 路徑防護

自 v1.0.5 起，Copilot CLI 會 **自動封鎖網路路徑（UNC Path）**，防止透過 SMB 認證洩漏憑證。

---

# 第 7 章：實戰案例

## 案例 1：Spring Boot 專案自動產生 API

### 場景描述

企業需要在訂單管理系統中新增客戶管理模組，包含 CRUD API、Service、Repository 和測試。

### 使用 Plan Mode

```
[Shift+Tab 切換到 Plan Mode]

> 在現有的 Spring Boot 專案中建立客戶管理模組。
  需求：
  1. Customer Entity：id, name, email, phone, address, createdAt, updatedAt
  2. REST API：
     - GET /api/v1/customers（分頁查詢）
     - GET /api/v1/customers/{id}
     - POST /api/v1/customers
     - PUT /api/v1/customers/{id}
     - DELETE /api/v1/customers/{id}
  3. 使用 Clean Architecture
  4. 使用 JPA + PostgreSQL
  5. 包含 Swagger 文件
  6. 包含完整 JUnit 5 + Mockito 測試
```

**Copilot Plan 輸出：**

```
📋 Implementation Plan

Phase 1: Domain Layer
  ├── 建立 Customer Entity
  ├── 建立 CustomerRepository Interface
  └── 驗證 Entity 映射

Phase 2: Service Layer
  ├── 建立 CustomerDTO
  ├── 建立 CustomerService Interface
  ├── 建立 CustomerServiceImpl
  └── 建立 CustomerMapper

Phase 3: API Layer
  ├── 建立 CustomerController
  ├── 建立 CreateCustomerRequest
  ├── 建立 UpdateCustomerRequest
  └── 設定 Swagger 標註

Phase 4: Testing
  ├── CustomerServiceTest（Unit Test）
  ├── CustomerControllerTest（MockMvc）
  └── CustomerRepositoryTest（DataJpaTest）

Phase 5: Documentation
  └── 更新 API 文件

預估產生 12 個檔案，約 1,200 行程式碼
```

### Copilot 產生的程式碼片段

**Customer Entity：**

```java
@Entity
@Table(name = "customers")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Customer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, unique = true, length = 255)
    private String email;

    @Column(length = 20)
    private String phone;

    @Column(length = 500)
    private String address;

    @CreationTimestamp
    @Column(updatable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;
}
```

**CustomerController：**

```java
@RestController
@RequestMapping("/api/v1/customers")
@RequiredArgsConstructor
@Tag(name = "Customer Management", description = "客戶管理 API")
public class CustomerController {

    private final CustomerService customerService;

    @GetMapping
    @Operation(summary = "分頁查詢客戶")
    public ResponseEntity<Page<CustomerDTO>> getCustomers(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size) {
        return ResponseEntity.ok(customerService.findAll(PageRequest.of(page, size)));
    }

    @GetMapping("/{id}")
    @Operation(summary = "根據 ID 查詢客戶")
    public ResponseEntity<CustomerDTO> getCustomer(@PathVariable Long id) {
        return ResponseEntity.ok(customerService.findById(id));
    }

    @PostMapping
    @Operation(summary = "建立客戶")
    public ResponseEntity<CustomerDTO> createCustomer(
            @Valid @RequestBody CreateCustomerRequest request) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(customerService.create(request));
    }

    @PutMapping("/{id}")
    @Operation(summary = "更新客戶")
    public ResponseEntity<CustomerDTO> updateCustomer(
            @PathVariable Long id,
            @Valid @RequestBody UpdateCustomerRequest request) {
        return ResponseEntity.ok(customerService.update(id, request));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "刪除客戶")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteCustomer(@PathVariable Long id) {
        customerService.delete(id);
    }
}
```

---

## 案例 2：自動修復 Bug + 產生測試

### 場景描述

線上環境回報：批量匯入客戶資料時，偶發 `DataIntegrityViolationException`。

### 操作流程

```
> 線上環境在批量匯入客戶資料時，偶發 DataIntegrityViolationException。
  相關檔案：@CustomerImportService.java
  
  請:
  1. 分析可能的根因
  2. 修復問題
  3. 產生回歸測試
```

**Copilot 分析結果：**

```
🔍 根因分析：

1. 讀取 CustomerImportService.java...
2. 發現問題在 batchImport() 方法：
   - 第 45 行：未檢查 email 是否已存在
   - 第 52 行：批量 saveAll() 未使用 Transaction
   - 高併發場景下可能出現 duplicate key 衝突

📝 修復方案：
1. 匯入前先檢查 email 重複
2. 使用 @Transactional 確保原子性
3. 加入 retry 機制處理 OptimisticLockException
```

**修復後新增的測試：**

```java
@Test
@DisplayName("should_HandleDuplicateEmails_When_BatchImport")
void shouldHandleDuplicateEmailsWhenBatchImport() {
    // Given
    List<CustomerImportDTO> batch = List.of(
        new CustomerImportDTO("Alice", "alice@example.com"),
        new CustomerImportDTO("Alice2", "alice@example.com")  // 重複 email
    );

    // When
    ImportResult result = customerImportService.batchImport(batch);

    // Then
    assertThat(result.getSuccessCount()).isEqualTo(1);
    assertThat(result.getFailedCount()).isEqualTo(1);
    assertThat(result.getErrors()).hasSize(1);
    assertThat(result.getErrors().get(0).getReason()).contains("duplicate email");
}

@Test
@DisplayName("should_RollbackAll_When_CriticalErrorOccurs")
void shouldRollbackAllWhenCriticalErrorOccurs() {
    // Given
    List<CustomerImportDTO> batch = createLargeBatch(1000);
    doThrow(new RuntimeException("DB connection lost"))
        .when(customerRepository).saveAll(anyList());

    // When & Then
    assertThrows(ImportException.class,
        () -> customerImportService.batchImport(batch));
    
    // 確認沒有部分資料被寫入
    assertThat(customerRepository.count()).isEqualTo(0);
}
```

---

## 案例 3：自動建立 PR + Summary

### 場景描述

完成認證模組開發後，需要建立 PR 並自動產生詳細的 Summary。

### 操作流程

```
> Commit 目前所有變更，使用 Conventional Commit 格式。
  然後建立 PR 到 develop 分支。
  PR 標題：feat: 實作 JWT 認證模組
  自動產生 Summary，包含：
  - 變更摘要
  - 修改的檔案清單
  - 測試結果
  - 部署注意事項
  指派 Reviewer：@tech-lead, @security-reviewer
  標籤：feature, security, needs-review
```

**Copilot 執行動作：**

```bash
# 1. Commit
git add -A
git commit -m "feat(auth): 實作 JWT 認證模組

- 新增 JWT Token 產生與驗證服務
- 新增 Spring Security 設定
- 新增認證相關 API endpoint
- 新增 23 個單元測試"

# 2. Push 分支
git push origin feature/jwt-auth

# 3. 建立 PR（透過 GitHub API）
# 自動生成以下 Summary...
```

**自動產生的 PR Summary：**

```markdown
## 📋 Summary

本 PR 實作 JWT 認證模組，為系統提供完整的身份驗證機制。

### 🔧 主要變更

| 類型 | 檔案 | 說明 |
|------|------|------|
| 新增 | `AuthController.java` | 認證 API（登入/登出/Refresh） |
| 新增 | `JwtTokenService.java` | JWT Token 管理 |
| 新增 | `SecurityConfig.java` | Spring Security 設定 |
| 新增 | `JwtAuthenticationFilter.java` | JWT 過濾器 |
| 修改 | `application.yml` | JWT 相關設定 |
| 新增 | `AuthServiceTest.java` | 認證測試（23 cases） |

### ✅ 測試結果
- 單元測試：23/23 ✅
- 整合測試：8/8 ✅
- 覆蓋率：87%

### ⚠️ 部署注意事項
1. 需設定環境變數：`JWT_SECRET`, `JWT_EXPIRATION`
2. 需在 Redis 中啟用 Token 黑名單功能
3. 資料庫需執行 migration：`V2__add_refresh_token_table.sql`

### 🔒 安全考量
- Token 有效期：Access Token 30 分鐘，Refresh Token 7 天
- 使用 RS256 演算法簽名
- Refresh Token 使用一次即失效（Rotation）
```

---

## 案例 4：Batch Job 開發輔助

### 場景描述

開發一個每日報表生成的 Batch Job（類似銀行 R91 類型），從多個資料表統計當日交易資料。

### 操作流程

```
> 建立一個 Spring Batch Job：
  名稱：DailyTransactionReportJob
  功能：
  1. 讀取當日所有交易（從 transactions 表）
  2. 按銀行代碼分組統計
  3. 產生 CSV 報表輸出到 /reports/ 目錄
  4. 發送統計摘要到指定 Email
  
  要求：
  - 使用 Spring Batch 5.x
  - 支持斷點續跑（Restartable）
  - 支持分區處理（Partitioning）大量資料
  - 記錄 Job 執行日誌
  - 加入 Retry 機制（最多 3 次）
  - 使用 @Scheduled 設定每日凌晨 2:00 執行
```

**Copilot 產生的核心程式碼：**

```java
@Configuration
@EnableBatchProcessing
public class DailyTransactionReportJobConfig {

    @Bean
    public Job dailyTransactionReportJob(
            JobRepository jobRepository,
            Step partitionStep,
            Step emailNotificationStep) {
        return new JobBuilder("dailyTransactionReportJob", jobRepository)
                .incrementer(new RunIdIncrementer())
                .start(partitionStep)
                .next(emailNotificationStep)
                .listener(new JobExecutionListener() {
                    @Override
                    public void beforeJob(JobExecution jobExecution) {
                        log.info("開始執行每日交易報表 Job: {}", 
                            LocalDate.now());
                    }
                    @Override
                    public void afterJob(JobExecution jobExecution) {
                        log.info("每日交易報表 Job 完成，狀態: {}",
                            jobExecution.getStatus());
                    }
                })
                .build();
    }

    @Bean
    public Step partitionStep(
            JobRepository jobRepository,
            Step processStep,
            Partitioner bankCodePartitioner) {
        return new StepBuilder("partitionStep", jobRepository)
                .partitioner("processStep", bankCodePartitioner)
                .step(processStep)
                .gridSize(10)
                .taskExecutor(new SimpleAsyncTaskExecutor())
                .build();
    }

    @Bean
    public Step processStep(
            JobRepository jobRepository,
            PlatformTransactionManager transactionManager) {
        return new StepBuilder("processStep", jobRepository)
                .<Transaction, TransactionSummary>chunk(1000, transactionManager)
                .reader(transactionReader(null))
                .processor(transactionProcessor())
                .writer(csvReportWriter(null))
                .faultTolerant()
                .retryLimit(3)
                .retry(DataAccessException.class)
                .build();
    }
}
```

---

# 第 8 章：最佳實務（Best Practices）

## 8.1 如何寫好 Prompt（CLI 版本）

### 黃金法則

```
     具體 + 有上下文 + 有預期結果 = 好 Prompt
```

### Prompt 品質等級

| 等級 | 範例 | 問題 |
|------|------|------|
| 🔴 差 | 「寫一個 API」 | 無上下文、無具體需求 |
| 🟠 一般 | 「寫一個使用者 CRUD API」 | 缺乏技術細節 |
| 🟡 好 | 「用 Spring Boot 寫使用者 CRUD API，使用 JPA」 | 缺乏架構指引 |
| 🟢 很好 | 「在 @UserController 新增 GET /api/v1/users/{id}，回傳 UserDTO，使用 Service 層，404 時回傳 ErrorResponse」 | 清晰、完整 |
| 🌟 最佳 | 使用 Plan Mode + Custom Instructions + @ 引用 | 企業級品質 |

### Prompt 結構範本

```
[任務目標]（一句話描述要做什麼）

[上下文]（參考哪些檔案，@ 引用）

[技術規範]（使用的框架、版本、設計模式）

[輸出要求]（格式、命名、結構）

[限制條件]（不要做什麼、邊界條件）

[驗證標準]（如何確認完成）
```

## 8.2 人機協作（Human-in-the-Loop）

### 建議的協作模式

```mermaid
graph TD
    A[需求分析] --> B{複雜度}
    B -->|簡單| C[直接 Prompt]
    B -->|中等| D[Plan Mode 先規劃]
    B -->|複雜| E[分步驟 + 人工審查]

    C --> F[Copilot 產生]
    D --> G[人工審查計畫]
    G --> F
    E --> H[Step 1: Copilot 產生]
    H --> I[人工 Review]
    I --> J[Step 2: Copilot 產生]
    J --> K[人工 Review]
    K --> L[...]

    F --> M[Code Review]
    L --> M
    M --> N[Merge]
```

### 何時應人工介入

| 場景 | 建議 | 原因 |
|------|------|------|
| 安全相關程式碼 | 🔴 必須人工審查 | AI 可能遺漏安全漏洞 |
| 資料庫 Migration | 🔴 必須人工審查 | 不可逆操作 |
| Git Force Push | 🔴 必須人工審查 | 可能覆蓋他人工作 |
| 一般 CRUD 程式碼 | 🟢 可信任 Copilot | 成熟模式 |
| 單元測試 | 🟢 可信任 Copilot | 容易驗證 |
| 複雜業務邏輯 | 🟠 需審查 | 業務正確性需人工判斷 |

## 8.3 適合與不適合使用的場景

### ✅ 非常適合使用 Copilot CLI 的場景

1. **脅手架程式碼**（Scaffolding）：新模組、新 API、新測試
2. **重複性工作**：多個相似的 Controller / Service 產生
3. **Git 操作**：複雜的 merge / rebase / cherry-pick
4. **DevOps 自動化**：建立 CI/CD pipeline、Dockerfile
5. **文件產生**：API 文件、README、CHANGELOG
6. **Code Review**：快速檢查 PR 的品質
7. **除錯輔助**：分析錯誤日誌、追蹤 Bug

### ❌ 不適合使用 Copilot CLI 的場景

1. **高機密系統**：涉及密碼、金鑰、PII 資料的操作
2. **複雜演算法**：需要深度數學/領域知識的演算法設計
3. **生產環境操作**：直接對生產 DB 的操作
4. **架構決策**：技術選型、架構設計需人工判斷
5. **法規遵循**：涉及合規要求的程式碼審查

---

# 第 9 章：維運與升級

## 9.1 如何更新 Copilot CLI

### 各平台升級指令

```bash
# npm
npm update -g @github/copilot

# WinGet (Windows)
winget upgrade GitHub.Copilot

# Homebrew (macOS / Linux)
brew upgrade copilot-cli

# 安裝腳本（重新執行即可）
curl -fsSL https://gh.io/copilot-install | bash
```

### 版本檢查

```bash
# 查看目前版本
copilot --version

# 查看可用更新
npm outdated -g @github/copilot
```

## 9.2 版本管理策略

| 環境 | 建議版本 | 更新頻率 |
|------|---------|---------|
| 開發環境 | Latest Stable | 每月更新 |
| CI/CD 環境 | 固定版本 | 每季度評估後更新 |
| 企業統一 | 經測試的穩定版 | 由 DevOps 團隊統一管理 |

### 企業版本管理建議

```bash
# 在 CI/CD 中鎖定版本
npm install -g @github/copilot@1.0.11

# 在團隊文件中記錄版本
# docs/tool-versions.md
# - Copilot CLI: v1.0.11 (2026-03-23)
# - 上次升級日期：2026-03-23
# - 下次評估日期：2026-06-23
```

## 9.3 常見問題（FAQ）

| 問題 | 解決方案 |
|------|---------|
| Copilot 回應太慢 | 1. 檢查網路連線<br>2. 使用 `/compact` 壓縮 context<br>3. 切換到更快的模型 |
| Context 用完 | 使用 `/compact` 或開啟新 session |
| Agent 不準確 | 1. 改善 custom instructions<br>2. 使用 @ 引用相關檔案<br>3. 使用 Plan Mode |
| MCP Server 無法連線 | 1. `/mcp` 檢查狀態<br>2. 驗證 `mcp-config.json` 設定 |
| 無法建立 PR | 1. 確認 GitHub Token 權限<br>2. 確認 Repository 權限 |
| 升級後行為改變 | 1. 檢查 Changelog<br>2. 更新 custom instructions |

## 9.4 效能與成本考量

### Premium Requests 配額

- 每次在互動式介面提交 Prompt 或程式化呼叫都會消耗 **Premium Request 配額**
- 不同模型的消耗乘數不同：
  - Claude Sonnet 4.5：1x
  - 其他模型：依定價而定

### 節省 Premium Requests 的方法

1. **合併相關任務到一次 Prompt**（而非多次小任務）
2. **使用 `/compact` 壓縮 context**（減少 Token 消耗）
3. **善用 Plan Mode**（一次規劃好再執行，避免反覆修改）
4. **使用 Custom Instructions**（減少每次 Prompt 的重複說明）

### 監控使用量

```bash
# 在互動式介面中查看使用統計
/usage
# 顯示：Premium Requests 使用量、session 時長、編輯行數、Token 統計

/context
# 顯示：Context Window 使用情況
```

---

# 第 10 章：附錄

## 10.1 常用指令速查表

### 啟動與基本操作

| 指令 | 說明 |
|------|------|
| `copilot` | 啟動互動式介面 |
| `copilot -p "..."` | 程式化呼叫（執行完即退出） |
| `copilot --continue` | 繼續上次的 session |
| `copilot --resume` | 選擇並恢復歷史 session |
| `copilot --model <model>` | 指定模型 |
| `copilot --agent=<name>` | 使用指定 Agent |

### 互動式 Slash 指令

#### 核心指令

| 指令 | 說明 |
|------|------|
| `/login` | 登入 GitHub |
| `/logout` | 登出 |
| `/model` 或 `/models` | 切換模型 |
| `/agent` | 選擇 / 切換 Custom Agent |
| `/mcp` | 管理 MCP Server |
| `/mcp add` | 新增 MCP Server |
| `/mcp show` / `/mcp show <name>` | 查看 MCP 狀態與工具清單 |
| `/mcp enable` / `/mcp disable` | 啟用 / 停用 MCP Server |
| `/mcp reload` | 重新載入 MCP 設定 |
| `/lsp` / `/lsp show` | 查看 LSP Server 狀態 |

#### Session 管理

| 指令 | 說明 |
|------|------|
| `/new [prompt]` | 開始新 Session（舊 Session 保留於背景） |
| `/clear [prompt]` | 完全放棄目前 Session |
| `/resume` | 恢復之前的 Session |
| `/rename <name>` | 重新命名目前 Session |
| `/session` | 查看 Session 資訊 |
| `/restart` | 熱重啟 CLI（保留 Session） |

#### 開發工作流

| 指令 | 說明 |
|------|------|
| `/pr` | 建立 / 查看 PR、修復 CI 失敗、處理 Review 回饋 |
| `/diff` | 檢視本次 Session 的變更（支援 17 種語言語法高亮） |
| `/undo` | 復原上一輪操作與檔案變更 |
| `/review` | 分析程式碼變更 |
| `/delegate [prompt]` | 非同步委派給 Copilot Coding Agent |
| `/research` | 深度研究並產出可匯出報告 |
| `/init` | 產生 Copilot Instructions 檔案 |

#### Context 與記憶

| 指令 | 說明 |
|------|------|
| `/compact` | 手動壓縮 Context |
| `/context` | 查看 Token 使用量 |
| `/usage` | 查看 Session 使用統計（請求數、Token、程式碼變更量） |
| `/instructions` | 查看與切換 Custom Instructions 檔案 |
| `/skills` / `/skills add` | 管理 Skills |

#### 權限與安全

| 指令 | 說明 |
|------|------|
| `/yolo` / `/allow-all` | 啟用全部工具權限（**危險！**） |
| `/reset-allowed-tools` | 重置已授予的工具權限 |
| `/add-dir <path>` | 新增受信任目錄 |
| `/cwd <path>` 或 `/cd <path>` | 切換工作目錄 |

#### 擴充與插件

| 指令 | 說明 |
|------|------|
| `/plugin` | Plugin 管理（install / update / uninstall / list） |
| `/plugin marketplace add` | 從 Marketplace 安裝 Plugin |
| `/extensions` | 查看、啟用、停用 Extensions |

#### 輔助工具

| 指令 | 說明 |
|------|------|
| `/copy` | 複製最近一次回應到剪貼簿 |
| `/share` / `/share gist` | 匯出 Session 為 Markdown 或 Gist |
| `/feedback` | 提交回饋 |
| `/changelog` | 查看版本更新日誌（支援 `last N`、`since <version>`、`summarize`） |
| `/version` | 顯示 CLI 版本並檢查更新 |
| `/update` | 查看更新說明並執行更新 |
| `/theme` | 主題選擇器（含 GitHub Dark/Light、色盲友善主題） |
| `/streamer-mode` / `/on-air` | 隱藏模型名稱和配額細節（直播模式） |
| `/experimental` / `/experimental on\|off` | 啟用 / 停用實驗性功能 |
| `/chronicle` | Standup 報告、技巧提示（實驗性） |
| `/terminal-setup` | 設定終端機多行輸入支援 |
| `/diagnose` | 診斷 Session 問題 |
| `#` | 參照 GitHub Issue / PR / Discussion |
| `?` | 快速幫助覆蓋（分組顯示快捷鍵與指令） |

### 快捷鍵

| 快捷鍵 | 說明 |
|--------|------|
| `Shift + Tab` | 向前循環模式（Ask → Plan → Autopilot → Shell） |
| `Tab` | 向前循環模式 |
| `Esc` | 終止操作 / 拒絕工具 / 清除輸入 |
| `Double-Esc` | 復原檔案變更到上一個快照 |
| `Ctrl + T` | 切換顯示/隱藏推理過程 |
| `Ctrl + R` | 反向搜尋指令歷史（如 Bash） |
| `Ctrl + C` | 中斷執行 |
| `Ctrl + D` | 在空 Prompt 時退出 CLI |
| `Ctrl + Z` | 暫停 CLI（Unix，`fg` 恢復） |
| `Ctrl + X, Ctrl + E` | 在外部編輯器中編輯 Prompt |
| `Ctrl + Y` | 在終端編輯器中編輯 Plan |
| `Ctrl + G` | 在外部編輯器中編輯 / 關閉 UI 元素 |
| `Ctrl + F` / `Ctrl + B` | 頁面下 / 上捲動（Alt Screen） |
| `Ctrl + A` / `Ctrl + E` | 行首 / 行尾 |
| `Ctrl + K` | 刪除到行尾（游標在行尾時合併行） |
| `Ctrl + N` / `Ctrl + P` | 等同上 / 下方向鍵 |
| `Ctrl + O` | 展開最近 Timeline |
| `Ctrl + S` | 執行指令（保留輸入） |
| `!<command>` | 直接執行 shell 指令 |
| `&<prompt>` | 等同 `/delegate`（非同步委派） |
| `@<path>` | 引用檔案內容（支援絕對/相對/父目錄/home 路徑） |
| `#` | 參照 GitHub Issue / PR / Discussion |

### 命令列選項

#### 執行模式

| 選項 | 說明 |
|------|------|
| `-p, --prompt "..."` | 程式化模式（執行完即退出） |
| `--continue` | 繼續最近的 Session |
| `--resume [id]` | 選擇恢復 Session（支援 Session ID 或 Task ID） |
| `--agent=<name>` | 使用指定 Agent |
| `--model <name>` | 指定模型 |
| `--effort, --reasoning-effort <level>` | 設定推理強度 |
| `--experimental` / `--no-experimental` | 啟用 / 停用實驗性功能 |
| `--banner` | 顯示啟動動畫 |

#### 工具權限

| 選項 | 說明 |
|------|------|
| `--allow-all-tools` / `--yolo` / `--allow-all` | 允許所有工具 |
| `--allow-tool='<spec>'` | 允許特定工具 |
| `--deny-tool='<spec>'` | 禁止特定工具 |
| `--allow-all-paths` | 允許存取所有路徑 |

#### 擴充整合

| 選項 | 說明 |
|------|------|
| `--additional-mcp-config '<json\|@file>'` | 附加 / 覆蓋 MCP 設定 |
| `--enable-all-github-mcp-tools` | 啟用所有 GitHub MCP 讀寫工具 |
| `--add-github-mcp-toolset <set>` | 新增 GitHub MCP 工具集 |
| `--add-github-mcp-tool <tool>` | 新增個別 GitHub MCP 工具 |
| `--disable-mcp-server <name>` | 停用指定 MCP Server |
| `--plugin-dir <path>` | 從本地目錄載入 Plugin |
| `--available-tools <list>` | 過濾可用工具 |
| `--excluded-tools <list>` | 排除特定工具 |

#### 顯示與輸出

| 選項 | 說明 |
|------|------|
| `--alt-screen on\|off` | 啟用 / 停用 Alt Screen Buffer |
| `--mouse` / `--no-mouse` | 啟用 / 停用滑鼠模式 |
| `--screen-reader` | 無障礙螢幕閱讀器模式 |
| `--output-format json` | 程式化模式輸出 JSONL 格式 |
| `--silent` | 靜默模式（抑制統計輸出） |
| `--share` / `--share-gist` | 非互動模式分享 Session |

#### 其他

| 選項 | 說明 |
|------|------|
| `--acp` | 啟動 ACP（Agent Client Protocol）伺服器 |
| `--server` | 伺服器模式 |
| `--config-dir <dir>` | 覆蓋設定檔目錄 |
| `--bash-env` | 在 Shell Session 中 source BASH_ENV |
| `--binary-version` | 查詢二進位版本（不啟動 CLI） |
| `--version` | 顯示版本 |

### 輔助指令

| 指令 | 說明 |
|------|------|
| `copilot help` | 顯示幫助 |
| `copilot help config` | 設定說明（含支援模型列表） |
| `copilot help environment` | 環境變數說明 |
| `copilot help logging` | 日誌等級說明 |
| `copilot help permissions` | 工具權限說明 |
| `copilot login` | 子命令：登入 |
| `copilot version` | 子命令：查看版本 |
| `copilot update` | 子命令：更新 |
| `copilot plugin` | 子命令：Plugin 管理（非互動） |

## 10.2 Prompt 範本合集

### 範本 1：Spring Boot API 開發

```
在現有 Spring Boot 專案中建立 {模組名稱} 的 REST API：

Entity：
- {欄位定義}

API：
- GET /api/v1/{resource}（分頁查詢，支援 filter）
- GET /api/v1/{resource}/{id}
- POST /api/v1/{resource}
- PUT /api/v1/{resource}/{id}
- DELETE /api/v1/{resource}/{id}

規範：
- 使用 Clean Architecture
- DTO 與 Entity 分離
- @Valid 驗證 Request
- @Operation Swagger 註解
- 統一 ErrorResponse 處理
- Log4j2 記錄關鍵操作

請同時產生 JUnit 5 + Mockito 測試。
```

### 範本 2：Bug 修復

```
Bug 描述：{問題描述}
重現步驟：{步驟}
相關檔案：@{file1}, @{file2}
線上日誌：{錯誤訊息}

請：
1. 分析根因
2. 提出修復方案（不影響現有功能）
3. 產生回歸測試
4. 說明修復可能的 Side Effect
```

### 範本 3：PR 建立

```
將目前分支變更建立 PR：
- 目標分支：{branch}
- 標題：{type}: {description}
- 自動產生 Summary（含變更摘要、測試結果、部署注意事項）
- 標籤：{labels}
- Reviewer：{reviewers}
```

### 範本 4：CI/CD Pipeline

```
建立 GitHub Actions workflow：
- 觸發條件：PR to {branch} + 手動觸發
- 步驟：
  1. Maven 編譯（JDK {version}）
  2. JUnit 測試
  3. JaCoCo 覆蓋率（最低 {percentage}%）
  4. SonarQube 靜態分析
  5. OWASP Dependency Check
  6. Docker 映像建置
- 失敗時通知 Teams
```

### 範本 5：資料庫操作

```
建立 Flyway migration 腳本：
- 版本：V{number}__{description}.sql
- 操作：{新增表/修改欄位/建立索引}
- 需考慮：
  - 與現有資料的相容性
  - 大資料量的加索引策略（CONCURRENTLY）
  - Rollback 方案
```

## 10.3 工具權限速查表

| 工具規範 | 說明 | 範例 |
|---------|------|------|
| `shell` | 所有 shell 指令 | `--allow-tool='shell'` |
| `shell(COMMAND)` | 特定指令 | `--allow-tool='shell(mvn)'` |
| `shell(git SUBCOMMAND)` | 特定 git 子命令 | `--deny-tool='shell(git push)'` |
| `write` | 檔案寫入權限 | `--allow-tool='write'` |
| `MCP_SERVER` | MCP server 全部工具 | `--allow-tool='github'` |
| `MCP_SERVER(tool)` | MCP server 特定工具 | `--deny-tool='github(delete_file)'` |

## 10.4 環境變數

### 認證相關

| 變數名稱 | 說明 | 優先順序 |
|---------|------|---------|
| `COPILOT_GITHUB_TOKEN` | GitHub Token（推薦，用於 CI/CD） | 1（最高） |
| `GH_TOKEN` | GitHub Token | 2 |
| `GITHUB_TOKEN` | GitHub Token（在 Agent Shell Session 中亦可使用） | 3 |
| `GITHUB_ASKPASS` | 認證輔助程式路徑 | - |
| `GH_HOST` | GitHub Enterprise 主機名稱（PAT / gh 認證模式） | - |

### 設定相關

| 變數名稱 | 說明 |
|---------|------|
| `COPILOT_HOME` | Copilot 設定檔目錄（預設 `~/.copilot`） |
| `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` | 額外的 Custom Instructions 目錄 |
| `COPILOT_CLI` | 值為 `1`，自動設定於子進程中（可供 Git Hook 偵測） |

### 網路與代理

| 變數名稱 | 說明 |
|---------|------|
| `HTTP_PROXY` / `HTTPS_PROXY` | HTTP/HTTPS 代理伺服器 |
| `NO_PROXY` | 排除代理的網域 |

### 顯示與行為

| 變數名稱 | 說明 |
|---------|------|
| `NO_COLOR` | 停用終端色彩輸出 |
| `USE_BUILTIN_RIPGREP` | 使用 PATH 中的 ripgrep 而非內建版本 |
| `BASH_ENV` | 搭配 `--bash-env` 旗標使用 |

## 10.5 設定檔位置

### 使用者層級設定

| 檔案 | 位置 | 說明 |
|------|------|------|
| `config.json` | `~/.copilot/config.json` | 全域設定 |
| `mcp-config.json` | `~/.copilot/mcp-config.json` | MCP Server 設定 |
| `lsp-config.json` | `~/.copilot/lsp-config.json` | LSP Server 設定 |
| `hooks/` | `~/.copilot/hooks/` | 個人 Hooks |
| `skills/` | `~/.copilot/skills/` | 個人 Skills |
| `agents/` | `~/.copilot/agents/` | 個人 Agent 定義 |
| `instructions/` | `~/.copilot/instructions/*.instructions.md` | 個人 Instructions（跨 Repository） |
| `~/.agents/skills/` | 個人 Skill 目錄（v1.0.11+） | 與 VS Code 一致 |

### Repository 層級設定

| 檔案 | 位置 | 說明 |
|------|------|------|
| `copilot-instructions.md` | `.github/copilot-instructions.md` | 專案 Instructions |
| `*.instructions.md` | `.github/instructions/` | 路徑專屬 Instructions |
| Agent 定義 | `.github/agents/` | 自訂 Agent |
| Skills | `.agents/skills/` 或 `.github/skills/` | 專案 Skills |
| Hooks | `.github/hooks/` | 專案 Hooks |
| `settings.json` | `.github/copilot/settings.json` | 專案設定（含 Marketplace 等） |
| `settings.local.json` | `.github/copilot/settings.local.json` | 本地專案設定 |
| LSP 設定 | `.github/lsp.json` | 專案 LSP Server 設定 |
| MCP 設定 | `.mcp.json` / `.vscode/mcp.json` | 工作區 MCP 設定 |
| DevContainer MCP | `.devcontainer/devcontainer.json` | DevContainer MCP 設定 |

### Agent 定義格式

| 檔案類型 | 位置 | 說明 |
|---------|------|------|
| `AGENTS.md` | 任何目錄 | Agent 行為定義 |
| `*.agent.md` | `.github/agents/` | VS Code 格式的 Agent 定義 |
| 遠端 Agent | 組織 `.github` Repository | 組織級 Agent 定義 |

> 📝 **Monorepo 支援**（v1.0.11+）：Custom Instructions、MCP Servers、Skills、Agents 現在會從工作目錄向上搜尋到 Git Root 的每一層目錄，完整支援 Monorepo 結構。

## 10.6 版本演進里程碑

| 版本 | 日期 | 重大事件 |
|------|------|---------|
| v0.0.329 | 2025-09-29 | 首次支援 Claude Sonnet 4.5；新增 `/model` 指令 |
| v0.0.342 | 2025-10-15 | 多行輸入（Kitty Protocol）；Session 格式改版 |
| v0.0.348 | 2025-10-21 | Token-by-token 串流輸出 |
| v0.0.349 | 2025-10-22 | 平行工具呼叫 |
| v0.0.353 | 2025-10-28 | Custom Agent 支援；`/delegate` 委派功能 |
| v0.0.374 | 2026-01-02 | 自動壓縮；子代理系統；`web_fetch` 工具 |
| v0.0.387 | 2026-01-20 | Plan Mode；`ask_user` 工具 |
| v0.0.389 | 2026-01-22 | `/diff` 指令；MCP OAuth 2.0；Plugin 生態系 |
| v0.0.396 | 2026-01-27 | `/init`、`/experimental`；Plugin Marketplace |
| v0.0.400 | 2026-01-30 | Autopilot 模式（實驗性）；`/theme` 指令 |
| v0.0.407 | 2026-02-11 | Alt Screen Buffer；`/instructions` 指令 |
| v0.0.411 | 2026-02-17 | Claude Sonnet 4.6；Autopilot 與 `/fleet` 開放所有使用者 |
| **v0.0.418** | **2026-02-25** | **🎉 正式 GA（General Availability）** |
| v1.0.2 | 2026-03-06 | 主版本號升至 1.0 |
| v1.0.3 | 2026-03-09 | Extensions（實驗性）；`/restart` 指令 |
| v1.0.5 | 2026-03-13 | `/pr` 指令；`/undo` 指令；`/extensions` 指令 |
| v1.0.10 | 2026-03-20 | 多 Session 並行（實驗性）；`/undo` 指令 |
| **v1.0.11** | **2026-03-23** | **目前最新版**；MCP 政策封鎖警告；Monorepo 完整支援 |

---

# 檢查清單（Checklist）

## 🔰 新手入門檢查清單

- [ ] 確認擁有 GitHub Copilot 訂閱（Free / Pro / Pro+ / Business / Enterprise）
- [ ] 安裝 Node.js 22+（如使用 npm 安裝）或使用 WinGet / Homebrew
- [ ] 安裝 Copilot CLI（`npm install -g @github/copilot`）
- [ ] 驗證安裝：`copilot --version` 確認版本
- [ ] 完成 GitHub 身份驗證（`/login`）
- [ ] 確認組織已啟用 Copilot CLI 政策（若為組織帳號）
- [ ] 在專案目錄中啟動 Copilot CLI 並信任該目錄
- [ ] 執行一個簡單的測試指令確認可用
- [ ] 執行 `/terminal-setup` 設定多行輸入（VS Code / Windows Terminal）
- [ ] 閱讀第 4 章核心功能教學

## 🔧 專案設定檢查清單

- [ ] 建立 `.github/copilot-instructions.md`（專案指令）
- [ ] 建立 `.github/instructions/` 目錄（路徑專屬指令）
- [ ] 建立 `.github/agents/` 目錄（自訂 Agent）
- [ ] 建立 `.agents/skills/` 目錄（專案 Skills）
- [ ] 設定 MCP Server（如需要）
- [ ] 設定 LSP Server（如需要，`.github/lsp.json`）
- [ ] 設定 Hooks（`.github/hooks/`）
- [ ] 確認 `.gitignore` 排除敏感檔案
- [ ] 在團隊文件中記錄 Copilot CLI 版本
- [ ] 考慮建立 `settings.json`（`.github/copilot/settings.json`）共享專案設定

## 🔒 安全檢查清單

- [ ] **禁止**在 Prompt 中包含密碼、API Key、Token
- [ ] **禁止**在 Home 目錄啟動 Copilot CLI
- [ ] **禁止**在生產環境中使用 `--allow-all-tools` / `--yolo`
- [ ] 設定 `--deny-tool` 禁止危險操作（rm、git push --force）
- [ ] 設定 `preToolUse` Hook 攔截高風險指令
- [ ] 設定 `postToolUse` Hook 記錄稽核日誌
- [ ] 所有 AI 產生的程式碼必須經過 Code Review
- [ ] CI/CD Pipeline 包含安全掃描步驟
- [ ] 定期更新 Copilot CLI 到最新版本
- [ ] 確認第三方 MCP Server 政策與組織允許清單一致
- [ ] 確認 UNC 路徑防護已啟用（v1.0.5+ 預設啟用）

## 📊 日常使用檢查清單

- [ ] 使用 `/usage` 監控 Premium Requests 消耗
- [ ] 使用 `/context` 監控 Token 使用量
- [ ] 適時使用 `/compact` 壓縮 Context
- [ ] 複雜任務使用 Plan Mode（Shift + Tab）
- [ ] 使用 `@` 引用相關檔案提供 Context
- [ ] 使用 `#` 直接參照 GitHub Issue / PR
- [ ] 審查每個工具執行請求
- [ ] 使用 `/diff` 審查本次 Session 的所有變更
- [ ] 使用 `/undo` 復原不理想的變更
- [ ] Code Review 所有 AI 產生的變更

## 🚀 進階使用檢查清單

- [ ] 建立團隊標準的 Custom Instructions
- [ ] 建立常用的 Prompt 範本庫
- [ ] 設定 Custom Agents 處理專門任務
- [ ] 建立 Skills 處理重複性專業任務
- [ ] 設定 Hooks 實作自動化安全防護與日誌
- [ ] 整合 MCP Server（GitHub、DB、Docker）
- [ ] 整合 LSP Server 提升程式碼智慧分析
- [ ] 評估 Plugin 生態系中的有用工具
- [ ] 建立自動化腳本（Task Chaining）
- [ ] 在 CI/CD 中使用程式化介面（`copilot -p`）
- [ ] 使用 `/delegate` 委派耗時任務至背景執行
- [ ] 使用 `/fleet` 平行化大型任務
- [ ] 使用 ACP 整合至其他工具或 IDE
- [ ] 使用 Copilot Memory 累積跨 Session 的專案知識
- [ ] 建立團隊使用規範與最佳實務文件

---

> 📝 **文件維護**  
> - 本手冊基於 GitHub Copilot CLI **v1.0.11**（2026 年 3 月 23 日）撰寫
> - 官方 Repository：https://github.com/github/copilot-cli
> - 產品頁面：https://github.com/features/copilot/cli
> - 官方文件：https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli
> - 安裝指南：https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli
> - 使用指南：https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli
> - 最佳實務：https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices
> - Changelog：https://github.com/github/copilot-cli/blob/main/changelog.md
> - Copilot SDK：https://github.com/github/copilot-sdk
> - GitHub MCP Registry：https://github.com/mcp
> - GitHub Skills 互動課程：https://github.com/skills/create-applications-with-the-copilot-cli
> - 建議每季度檢視並更新本手冊內容

