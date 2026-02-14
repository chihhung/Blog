+++
date = '2026-02-14T23:47:46+08:00'
draft = false
title = 'Github Copilot Cli教學手冊'
tags = ['教學', '工具','Copilot Cli']
categories = ['教學']
+++
# GitHub Copilot CLI 教學手冊

> **版本**：v3.0（2026 年 2 月）
> **適用對象**：資深工程師、DevOps 工程師、技術主管
> **適用平台**：Windows / macOS / Linux
> **前置條件**：具備 Git、Terminal 基礎操作能力；擁有 GitHub Copilot 授權
> **狀態**：GitHub Copilot CLI 目前為 Public Preview（含[資料保護](https://gh.io/dpa)），功能可能變更

---

## 目錄

- [1. GitHub Copilot CLI 架構說明](#1-github-copilot-cli-架構說明)
  - [1.1 Copilot CLI 架構概念](#11-copilot-cli-架構概念)
  - [1.2 與 GitHub Copilot IDE 版本的差異](#12-與-github-copilot-ide-版本的差異)
  - [1.3 三種使用模式](#13-三種使用模式)
  - [1.4 認證流程](#14-認證流程)
  - [1.5 CLI 與 GitHub 雲端服務關係](#15-cli-與-github-雲端服務關係)
  - [1.6 CLI 在企業環境中的位置](#16-cli-在企業環境中的位置)
- [2. 安裝與環境建置](#2-安裝與環境建置)
  - [2.1 系統需求](#21-系統需求)
  - [2.2 Windows 安裝方式](#22-windows-安裝方式)
  - [2.3 macOS 安裝方式](#23-macos-安裝方式)
  - [2.4 Linux 安裝方式](#24-linux-安裝方式)
  - [2.5 使用 npm 安裝（跨平台）](#25-使用-npm-安裝跨平台)
  - [2.6 驗證安裝成功](#26-驗證安裝成功)
  - [2.7 代理伺服器（Proxy）環境設定](#27-代理伺服器proxy環境設定)
  - [2.8 防火牆與網路限制處理](#28-防火牆與網路限制處理)
- [3. 基本設定與認證](#3-基本設定與認證)
  - [3.1 首次登入流程](#31-首次登入流程)
  - [3.2 使用 Personal Access Token 認證](#32-使用-personal-access-token-認證)
  - [3.3 企業 GitHub 組織授權](#33-企業-github-組織授權)
  - [3.4 CLI 設定檔說明](#34-cli-設定檔說明)
  - [3.5 信任目錄管理](#35-信任目錄管理)
  - [3.6 安全設定建議](#36-安全設定建議)
- [4. 開發應用方式](#4-開發應用方式)
  - [4.1 互動模式基本操作](#41-互動模式基本操作)
  - [4.2 計畫模式（Plan Mode）](#42-計畫模式plan-mode)
  - [4.3 程式化模式（Programmatic Mode）](#43-程式化模式programmatic-mode)
  - [4.4 檔案引用與上下文控制](#44-檔案引用與上下文控制)
  - [4.5 程式碼產生與重構](#45-程式碼產生與重構)
  - [4.6 測試程式產生](#46-測試程式產生)
  - [4.7 Dockerfile 與 CI/CD 產生](#47-dockerfile-與-cicd-產生)
  - [4.8 Git 操作與 PR 管理](#48-git-操作與-pr-管理)
  - [4.9 工具權限管理](#49-工具權限管理)
  - [4.10 團隊開發最佳實踐](#410-團隊開發最佳實踐)
- [5. 自訂與擴充功能](#5-自訂與擴充功能)
  - [5.1 自訂指令（Custom Instructions）](#51-自訂指令custom-instructions)
  - [5.2 自訂代理（Custom Agents）](#52-自訂代理custom-agents)
  - [5.3 技能（Skills）](#53-技能skills)
  - [5.4 Hooks](#54-hooks)
  - [5.5 AI 模型選擇](#55-ai-模型選擇)
  - [5.6 Copilot Memory](#56-copilot-memory)
- [6. 與 MCP（Model Context Protocol）串接方式](#6-與-mcpmodel-context-protocol串接方式)
  - [6.1 MCP 架構概念](#61-mcp-架構概念)
  - [6.2 內建 GitHub MCP Server](#62-內建-github-mcp-server)
  - [6.3 新增 MCP Server](#63-新增-mcp-server)
  - [6.4 自訂 MCP Server 開發](#64-自訂-mcp-server-開發)
  - [6.5 與企業內部 API 整合](#65-與企業內部-api-整合)
  - [6.6 MCP 安全與權限控管](#66-mcp-安全與權限控管)
- [7. DevOps 整合模式](#7-devops-整合模式)
  - [7.1 與 GitHub Actions 整合](#71-與-github-actions-整合)
  - [7.2 與 CI/CD Pipeline 整合](#72-與-cicd-pipeline-整合)
  - [7.3 容器化開發流程](#73-容器化開發流程)
  - [7.4 AI 輔助 Code Review](#74-ai-輔助-code-review)
  - [7.5 委派工作至 Copilot Coding Agent](#75-委派工作至-copilot-coding-agent)
  - [7.6 Commit Message 與 PR 最佳實務](#76-commit-message-與-pr-最佳實務)
- [8. 系統維護與治理](#8-系統維護與治理)
  - [8.1 CLI 版本管理策略](#81-cli-版本管理策略)
  - [8.2 企業升版流程](#82-企業升版流程)
  - [8.3 AI 使用紀錄稽核建議](#83-ai-使用紀錄稽核建議)
  - [8.4 使用權限控管](#84-使用權限控管)
  - [8.5 Session 管理](#85-session-管理)
  - [8.6 效能監控與成本控管](#86-效能監控與成本控管)
- [9. 企業導入最佳實踐](#9-企業導入最佳實踐)
  - [9.1 開發團隊使用規範](#91-開發團隊使用規範)
  - [9.2 AI 輔助開發風險](#92-ai-輔助開發風險)
  - [9.3 原始碼洩漏風險管理](#93-原始碼洩漏風險管理)
  - [9.4 Prompt 設計標準化](#94-prompt-設計標準化)
  - [9.5 AI 產出程式碼審核流程](#95-ai-產出程式碼審核流程)
  - [9.6 內部教育訓練建議](#96-內部教育訓練建議)
- [10. 風險與限制說明](#10-風險與限制說明)
  - [10.1 Copilot CLI 功能限制](#101-copilot-cli-功能限制)
  - [10.2 Premium Request 配額](#102-premium-request-配額)
  - [10.3 安全性考量](#103-安全性考量)
  - [10.4 網路依賴風險](#104-網路依賴風險)
  - [10.5 法規與合規性建議](#105-法規與合規性建議)
- [附錄 A：新進成員檢查清單](#附錄-a新進成員檢查清單)
- [附錄 B：常用指令速查表](#附錄-b常用指令速查表)
- [附錄 C：故障排除指南](#附錄-c故障排除指南)
- [附錄 D：ACP（Agent Client Protocol）](#附錄-dacpagent-client-protocol)
- [附錄 E：參考資源](#附錄-e參考資源)

---

## 1. GitHub Copilot CLI 架構說明

### 1.1 Copilot CLI 架構概念

GitHub Copilot CLI 是一個**獨立的命令列 AI 程式**，讓開發者直接在終端機中與 Copilot 互動。它具備代理（Agent）能力，可以讀取、修改、執行檔案，並與 GitHub.com 互動。

> **重要**：GitHub Copilot CLI 是獨立安裝的程式（`copilot` 指令），**不再**是 GitHub CLI（`gh`）的擴充套件。舊版 `gh copilot` 擴充已於 2025 年退役，由此獨立工具取代。

**核心架構元件：**

| 元件 | 說明 |
|---|---|
| **`copilot` 二進位執行檔** | 獨立安裝的命令列程式，無需依賴 GitHub CLI |
| **Copilot API** | GitHub 雲端 AI 服務，接收 Prompt 並回傳生成結果 |
| **LLM 模型** | 後端大型語言模型（預設 Claude Opus 4.5，可切換） |
| **MCP 整合層** | 內建 GitHub MCP Server，可擴充自訂 MCP Server |
| **認證層** | 透過 `/login` 指令或 PAT Token 認證 |
| **Session 管理** | 自動壓縮上下文，支援無限長度對話 |

```mermaid
graph TB
    subgraph "開發者工作站"
        A[開發者] --> B[Terminal / Shell]
        B --> C["copilot（獨立 CLI）"]
        C --> D[MCP Client]
        C --> E[Session Manager]
    end

    subgraph "GitHub 雲端服務"
        F[GitHub Authentication]
        G[Copilot API Gateway]
        H[AI Model Service<br/>Claude Opus 4.5 / Sonnet 4.5 / GPT-5.2 Codex]
        I[Usage & Billing<br/>Premium Requests]
    end

    subgraph "MCP Servers"
        J[GitHub MCP Server<br/>（內建）]
        K[自訂 MCP Server]
    end

    C -->|"認證"| F
    F -->|"授權驗證"| G
    C -->|"Prompt 請求"| G
    G -->|"模型推論"| H
    H -->|"生成回應"| G
    G -->|"回傳結果"| C
    G -->|"使用量記錄"| I
    D -->|"JSON-RPC"| J
    D -->|"JSON-RPC"| K

    style A fill:#e1f5fe
    style H fill:#fff3e0
    style F fill:#fce4ec
    style J fill:#c8e6c9
```

**運作原理：**

1. 開發者在終端機中執行 `copilot` 啟動互動式 Session
2. 確認信任當前目錄後，即可以自然語言輸入需求
3. Copilot 分析請求，可能讀取本地檔案、呼叫 MCP 工具、執行 Shell 指令
4. 需要修改檔案或執行指令時，會先徵求使用者同意
5. 自動管理對話上下文，接近限制時自動壓縮歷史記錄

### 1.2 與 GitHub Copilot IDE 版本的差異

| 比較項目 | Copilot IDE（VS Code 等） | Copilot CLI |
|---|---|---|
| **使用環境** | IDE 編輯器內 | 終端機 / 命令列 |
| **主要功能** | 程式碼自動補全、Chat、Inline Editing | 代理式開發：修改檔案、執行指令、建立 PR |
| **輸入方式** | 程式碼上下文 + 對話 | 自然語言 + `@file` 引用 |
| **輸出形式** | 程式碼片段、差異比對 | 直接建立/修改檔案、執行指令 |
| **代理能力** | Agent Mode（VS Code） | 完整代理：Plan → Code → Test → Commit → PR |
| **MCP 整合** | 透過 VS Code 設定 | 內建 GitHub MCP Server + `/mcp add` |
| **離線能力** | 無（需連線） | 無（需連線） |
| **適用場景** | 撰寫程式碼、即時補全 | 系統管理、DevOps、跨專案重構、自動化任務 |
| **Session 管理** | 依 Chat Window | 無限 Session + 自動壓縮 |
| **委派功能** | 無 | `/delegate` 可委派至 Copilot Coding Agent |

> **實務建議**：兩者互相補充而非替代。IDE 版適合即時程式碼補全和編輯，CLI 版適合系統管理、跨檔案/跨專案重構、自動化部署腳本、以及需要代理式執行的任務。建議團隊兩者同時導入。

### 1.3 三種使用模式

GitHub Copilot CLI 支援三種使用模式：

**1. 互動模式（Interactive Mode）— 預設模式**

```bash
# 啟動互動式 Session
copilot
```

在互動模式中，您可以持續與 Copilot 對話，要求它回答問題或執行任務。

**2. 計畫模式（Plan Mode）**

在互動模式中按 `Shift+Tab` 切換至計畫模式，或使用 `/plan` 指令。Copilot 會先分析需求、提出問題、建立結構化實作計畫，確認後才開始寫程式碼。

**3. 程式化模式（Programmatic Mode）**

```bash
# 單次提示執行
copilot -p "顯示本週的 commits 並摘要" --allow-tool 'shell(git)'

# 搭配腳本
./script-outputting-options.sh | copilot
```

適合 CI/CD Pipeline 和自動化腳本使用。

```mermaid
graph LR
    subgraph "使用模式"
        A["互動模式<br/>copilot"] --> B["對話式互動<br/>持續對話"]
        C["計畫模式<br/>Shift+Tab / /plan"] --> D["分析 → 計畫 → 確認 → 實作"]
        E["程式化模式<br/>copilot -p '...'"] --> F["單次執行<br/>自動化適用"]
    end

    style A fill:#e1f5fe
    style C fill:#fff3e0
    style E fill:#c8e6c9
```

### 1.4 認證流程

GitHub Copilot CLI 使用 **Device Flow** 進行認證：

```mermaid
sequenceDiagram
    participant Dev as 開發者
    participant CLI as copilot CLI
    participant GitHub as GitHub.com

    Dev->>CLI: copilot（首次啟動）
    CLI->>Dev: 提示使用 /login 指令
    Dev->>CLI: /login
    CLI->>GitHub: 請求 Device Code
    GitHub-->>CLI: 回傳 Device Code + URL
    CLI->>Dev: 顯示 "請前往指定 URL 輸入代碼"
    Dev->>GitHub: 瀏覽器登入並輸入代碼
    GitHub-->>Dev: 授權確認
    GitHub-->>CLI: 回傳 Access Token
    CLI->>CLI: 儲存認證資訊
    CLI-->>Dev: 認證成功，可開始使用
```

**替代認證方式 — Personal Access Token（PAT）：**

```bash
# 使用環境變數設定 PAT（依優先順序）
export GH_TOKEN="github_pat_xxxx"
# 或
export GITHUB_TOKEN="github_pat_xxxx"
```

> PAT 需在 [Fine-grained Token 頁面](https://github.com/settings/personal-access-tokens/new) 建立，並啟用 **「Copilot Requests」** 權限。

### 1.5 CLI 與 GitHub 雲端服務關係

```mermaid
graph LR
    subgraph "本地端"
        A["copilot CLI"] --> B[MCP Client]
    end

    subgraph "GitHub Cloud"
        C[GitHub.com API]
        D[Copilot Service]
        E[Model Hosting]
        F[Telemetry]
    end

    subgraph "MCP Servers"
        G[GitHub MCP Server<br/>（內建）]
        H[自訂 MCP Server]
    end

    A -->|"HTTPS 443"| C
    A -->|"HTTPS 443"| D
    D --> E
    D --> F
    B --> G
    B --> H
    G --> C

    subgraph "企業需開放的端點"
        I["github.com"]
        J["api.github.com"]
        K["copilot-proxy.githubusercontent.com"]
        L["default.exp-tas.com"]
    end

    style I fill:#e8f5e9
    style J fill:#e8f5e9
    style K fill:#e8f5e9
    style L fill:#e8f5e9
```

**必須開放的網路端點：**

| 端點 | 用途 | 埠號 |
|---|---|---|
| `github.com` | 認證與 API | 443 |
| `api.github.com` | GitHub REST/GraphQL API | 443 |
| `copilot-proxy.githubusercontent.com` | Copilot 推論服務 | 443 |
| `default.exp-tas.com` | 實驗設定服務 | 443 |
| `copilot-telemetry.githubusercontent.com` | 遙測資料 | 443 |
| `objects.githubusercontent.com` | 資源下載 | 443 |

### 1.6 CLI 在企業環境中的位置

```mermaid
graph TB
    subgraph "企業開發環境"
        subgraph "開發者工作站"
            A[VS Code + Copilot IDE]
            B["Terminal + copilot CLI"]
            C[Git Client]
        end

        subgraph "企業基礎設施"
            D[Proxy Server]
            E[Firewall]
            F[DNS Server]
        end

        subgraph "CI/CD Pipeline"
            G[GitHub Actions]
            H[Container Registry]
            I[Deployment Target]
        end
    end

    subgraph "GitHub Cloud"
        J[GitHub Repository]
        K[Copilot Service]
        L[GitHub API]
        M[Copilot Coding Agent]
    end

    subgraph "MCP Server（企業內部）"
        N[Internal API Gateway]
        O[Database Query Tool]
        P[Document Search]
    end

    B --> D --> E --> K
    A --> D
    C --> D --> J
    G --> L
    B -.->|"MCP Protocol"| N
    B -.->|"MCP Protocol"| O
    B -.->|"MCP Protocol"| P
    B -.->|"/delegate"| M

    style B fill:#bbdefb
    style K fill:#fff9c4
    style N fill:#c8e6c9
    style M fill:#e1bee7
```

> **實務案例**：在金融業環境中，Copilot CLI 通常部署於受管理的開發者工作站上，透過企業 Proxy 存取 GitHub 雲端服務。同時透過 MCP 串接內部知識庫，讓 AI 能參考企業內部標準和文件。使用 `/delegate` 可將任務委派至雲端 Copilot Coding Agent，自動建立 PR。

---

## 2. 安裝與環境建置

### 2.1 系統需求

| 需求項目 | 說明 |
|---|---|
| **作業系統** | Windows（需 PowerShell v6+）、macOS、Linux |
| **WSL** | Windows 上也支援透過 WSL 使用 |
| **GitHub 授權** | 需有效的 Copilot 訂閱（所有 Copilot 方案均可） |
| **網路** | HTTPS 連線至 GitHub |
| **Node.js**（僅 npm 安裝方式） | 22.x 或更新版本 |

> **注意**：Copilot CLI 是獨立二進位執行檔，透過 WinGet、Homebrew、安裝腳本安裝時**不需要** Node.js 或 GitHub CLI (`gh`)。

### 2.2 Windows 安裝方式

**使用 WinGet（建議）：**

```powershell
# 安裝正式版
winget install GitHub.Copilot

# 安裝預覽版
winget install GitHub.Copilot.Prerelease

# 安裝後驗證
copilot --version
```

> **注意**：Windows 環境需要 PowerShell v6 或更新版本。檢查版本：`$PSVersionTable.PSVersion`

**手動下載安裝：**

1. 前往 [GitHub Copilot CLI Releases](https://github.com/github/copilot-cli/releases/)
2. 下載適合您平台的執行檔
3. 解壓縮後將執行檔加入 PATH

### 2.3 macOS 安裝方式

**使用 Homebrew（建議）：**

```bash
# 安裝正式版
brew install copilot-cli

# 安裝預覽版
brew install copilot-cli@prerelease

# 驗證
copilot --version
```

**使用安裝腳本：**

```bash
# 使用 curl
curl -fsSL https://gh.io/copilot-install | bash

# 或使用 wget
wget -qO- https://gh.io/copilot-install | bash
```

**Apple Silicon (M 系列) 注意事項：**

```bash
# 確認架構
uname -m
# 預期輸出：arm64

# 確認 Homebrew 安裝在正確路徑
which brew
# 預期：/opt/homebrew/bin/brew
```

### 2.4 Linux 安裝方式

**使用 Homebrew（建議）：**

```bash
brew install copilot-cli
```

**使用安裝腳本：**

```bash
# 一般使用者安裝（預設安裝至 $HOME/.local/bin）
curl -fsSL https://gh.io/copilot-install | bash

# 以 root 安裝至 /usr/local/bin
curl -fsSL https://gh.io/copilot-install | sudo bash

# 指定版本與自訂安裝目錄
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.410" PREFIX="$HOME/custom" bash
```

**手動下載：**

前往 [GitHub Copilot CLI Releases](https://github.com/github/copilot-cli/releases/)，下載適合您平台的執行檔，解壓縮後放置於 PATH 中的目錄。

### 2.5 使用 npm 安裝（跨平台）

```bash
# 前提：需要 Node.js 22 或更新版本
node --version  # 需 >= 22.x

# 安裝正式版
npm install -g @github/copilot

# 安裝預覽版
npm install -g @github/copilot@prerelease
```

> **注意**：如果 `~/.npmrc` 中設定了 `ignore-scripts=true`，需使用：
>
> ```bash
> npm_config_ignore_scripts=false npm install -g @github/copilot
> ```

### 2.6 驗證安裝成功

```bash
# 檢查 Copilot CLI 版本
copilot --version

# 顯示說明
copilot -h

# 啟動互動模式（首次會引導登入）
copilot
```

**驗證檢查清單：**

- [ ] `copilot --version` 顯示正確版本
- [ ] `copilot -h` 顯示說明資訊
- [ ] `copilot` 可正常啟動互動模式
- [ ] 首次使用 `/login` 完成認證

### 2.7 代理伺服器（Proxy）環境設定

企業環境通常透過 Proxy 連線外部網路，需設定以下環境變數：

**Windows（PowerShell）：**

```powershell
# 設定系統環境變數（永久生效）
[System.Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://proxy.company.com:8080", "User")
[System.Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://proxy.company.com:8080", "User")
[System.Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1,.company.com", "User")

# 或在當前 Session 設定（暫時）
$env:HTTPS_PROXY = "http://proxy.company.com:8080"
$env:HTTP_PROXY = "http://proxy.company.com:8080"
$env:NO_PROXY = "localhost,127.0.0.1,.company.com"
```

**macOS / Linux：**

```bash
# 加入 ~/.bashrc 或 ~/.zshrc（永久生效）
export HTTPS_PROXY="http://proxy.company.com:8080"
export HTTP_PROXY="http://proxy.company.com:8080"
export NO_PROXY="localhost,127.0.0.1,.company.com"

# 套用設定
source ~/.bashrc
```

**需要認證的 Proxy：**

```bash
export HTTPS_PROXY="http://username:password@proxy.company.com:8080"
```

> **注意事項**：
> - Proxy 密碼含有特殊字元時需進行 URL Encoding（如 `@` → `%40`）
> - 部分企業使用 SSL Inspection，需額外設定 CA 憑證

### 2.8 防火牆與網路限制處理

**必須開放的防火牆規則：**

```
# 出站（Outbound）規則
目的地                                        埠號    通訊協定
─────────────────────────────────────────────────────────────
github.com                                    443     HTTPS
api.github.com                                443     HTTPS
copilot-proxy.githubusercontent.com           443     HTTPS
default.exp-tas.com                           443     HTTPS
copilot-telemetry.githubusercontent.com       443     HTTPS
objects.githubusercontent.com                 443     HTTPS
github-cloud.githubusercontent.com            443     HTTPS
```

**自訂 CA 憑證處理：**

```bash
# 如企業使用自簽 CA 憑證
# 方法一：設定 Node.js 環境變數（npm 安裝方式適用）
export NODE_EXTRA_CA_CERTS="/path/to/company-ca.crt"

# 方法二：設定 Git SSL 憑證
git config --global http.sslCAInfo /path/to/company-ca.crt
```

**防火牆測試腳本：**

```bash
#!/bin/bash
# test_connectivity.sh - 測試 Copilot CLI 所需的網路連線

ENDPOINTS=(
  "github.com"
  "api.github.com"
  "copilot-proxy.githubusercontent.com"
  "default.exp-tas.com"
  "copilot-telemetry.githubusercontent.com"
)

echo "=== GitHub Copilot CLI 網路連線測試 ==="
for endpoint in "${ENDPOINTS[@]}"; do
  if curl -s --connect-timeout 5 "https://${endpoint}" > /dev/null 2>&1; then
    echo "✅ ${endpoint} - 連線成功"
  else
    echo "❌ ${endpoint} - 連線失敗"
  fi
done
```

**PowerShell 版本：**

```powershell
# Test-CopilotConnectivity.ps1
$endpoints = @(
    "github.com",
    "api.github.com",
    "copilot-proxy.githubusercontent.com",
    "default.exp-tas.com",
    "copilot-telemetry.githubusercontent.com"
)

Write-Host "=== GitHub Copilot CLI 網路連線測試 ===" -ForegroundColor Cyan
foreach ($endpoint in $endpoints) {
    try {
        $result = Invoke-WebRequest -Uri "https://$endpoint" -TimeoutSec 5 -UseBasicParsing -ErrorAction Stop
        Write-Host "✅ $endpoint - 連線成功" -ForegroundColor Green
    } catch {
        Write-Host "❌ $endpoint - 連線失敗: $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

> **實務建議**：在企業導入前，先由 IT 基礎設施團隊執行上述測試腳本，確認所有端點均可存取。將測試結果留存作為導入前置作業的證明文件。

---

## 3. 基本設定與認證

### 3.1 首次登入流程

首次啟動 Copilot CLI 時，系統會引導您進行認證：

```bash
# 步驟 1：啟動 Copilot CLI
copilot

# 步驟 2：確認信任當前目錄
# 選擇：
# 1. Yes, proceed（僅本次 Session 信任）
# 2. Yes, and remember this folder for future sessions（永久信任）
# 3. No, exit (Esc)（離開）

# 步驟 3：如未登入，輸入 /login
/login

# 步驟 4：依螢幕指示開啟瀏覽器、輸入裝置代碼完成認證
```

> **安全提醒**：
> - 僅在您信任的目錄中啟動 Copilot CLI
> - 不建議從家目錄（Home Directory）啟動
> - 應避免在包含機密資料或不信任的可執行檔的目錄中使用

### 3.2 使用 Personal Access Token 認證

適用於 CI/CD 或無 GUI 環境：

**建立 Fine-grained PAT：**

1. 前往 [Fine-grained Personal Access Tokens](https://github.com/settings/personal-access-tokens/new)
2. 在 **Permissions** 中點選 **Add permissions**
3. 選擇 **Copilot Requests** 權限
4. 點選 **Generate token**

**設定環境變數：**

```bash
# 使用 GH_TOKEN（優先）或 GITHUB_TOKEN
export GH_TOKEN="github_pat_xxxxxxxxxxxx"

# 啟動 CLI（會自動使用環境變數中的 Token）
copilot
```

**在 CI/CD 中使用：**

```yaml
# GitHub Actions 範例
- name: Run Copilot CLI
  env:
    GH_TOKEN: ${{ secrets.COPILOT_PAT }}
  run: |
    copilot -p "Analyze the code changes" --allow-all-tools
```

> **安全提醒**：
> - Fine-grained Token 建議到期日設定不超過 90 天
> - 不在程式碼或設定檔中寫死 Token
> - 生產環境建議使用 GitHub App Token

### 3.3 企業 GitHub 組織授權

**組織管理員設定流程：**

1. 前往組織設定：`https://github.com/organizations/{org}/settings`
2. 導航至 **Copilot** → **Policies and features**
3. 確認 **Copilot CLI** 政策已設為 **Enabled**

> **重要**：如果組織擁有者或企業管理員停用了 Copilot CLI 政策，組織成員將無法使用 Copilot CLI。

**授權管理最佳做法：**

```
建議配置：
├── 開發團隊（Dev Team） ─────── Copilot 授權 ✅ + CLI 政策啟用
├── QA 團隊 ─────────────────── Copilot 授權 ✅ + CLI 政策啟用
├── DevOps 團隊 ─────────────── Copilot 授權 ✅ + CLI 政策啟用
├── 管理職 ──────────────────── 視需求 ⚠️
└── 外包人員 ────────────────── 需額外評估 ⚠️
```

### 3.4 CLI 設定檔說明

**Copilot CLI 設定檔位置：**

所有設定檔預設位於 `~/.copilot/` 目錄中。可透過設定 `XDG_CONFIG_HOME` 環境變數來更改位置。

| 設定檔 | 路徑 | 說明 |
|---|---|---|
| **主設定檔** | `~/.copilot/config.json` | 信任目錄清單、全域設定 |
| **MCP 設定檔** | `~/.copilot/mcp-config.json` | MCP Server 連線設定 |
| **自訂指令** | `~/.copilot/copilot-instructions.md` | 全域自訂指令 |
| **自訂代理** | `~/.copilot/agents/` | 自訂代理設定 |
| **Session 資料** | `~/.copilot/session-state/` | Session 歷史與狀態 |

**設定檔管理指令：**

```bash
# 查看設定說明
copilot help config

# 查看環境變數說明
copilot help environment

# 查看日誌設定
copilot help logging

# 查看權限設定
copilot help permissions
```

**Shell Alias 設定（提升效率）：**

```bash
# Bash / Zsh - 加入 ~/.bashrc 或 ~/.zshrc
alias cop='copilot'
alias copp='copilot -p'
```

```powershell
# PowerShell - 加入 $PROFILE
function cop { copilot @args }
function copp { copilot -p @args }

# 顯示 Profile 路徑
Write-Host $PROFILE
```

### 3.5 信任目錄管理

Copilot CLI 啟動時會確認您是否信任當前目錄。這是重要的安全機制。

**信任目錄選項：**

| 選項 | 說明 |
|---|---|
| **Yes, proceed** | 僅本次 Session 信任此目錄 |
| **Yes, and remember** | 永久信任此目錄（不再詢問） |
| **No, exit (Esc)** | 離開 Copilot CLI |

**管理已信任目錄：**

永久信任的目錄清單儲存在 `~/.copilot/config.json` 的 `trusted_folders` 陣列中。

```json
{
  "trusted_folders": [
    "/home/developer/projects/my-app",
    "/home/developer/projects/api-server"
  ]
}
```

> **安全提醒**：
> - 勿將家目錄加入信任清單
> - 僅信任您確定安全的專案目錄
> - 定期審查信任目錄清單

**在 Session 中新增信任目錄：**

```bash
# 新增目錄到當前 Session
/add-dir /path/to/other/project

# 列出當前可存取的目錄
/list-dirs

# 切換工作目錄
/cwd /path/to/directory
# 或
/cd /path/to/directory
```

### 3.6 安全設定建議

**Token 安全管理：**

```bash
# ❌ 不要這樣做
export GH_TOKEN="github_pat_xxxx"  # 寫在 .bashrc 中

# ✅ 建議做法：使用密鑰管理工具
# macOS - 使用 Keychain
security add-generic-password -a "github-copilot" -s "GH_TOKEN" -w "github_pat_xxxx"

# Linux - 使用 pass
pass insert github/copilot-token
export GH_TOKEN=$(pass show github/copilot-token)

# Windows - 使用 Credential Manager 或環境變數
```

**企業安全設定檢查清單：**

| 項目 | 建議 | 優先級 |
|---|---|---|
| Token 定期更換 | 每 90 天 | 高 |
| 啟用 2FA | 必須 | 高 |
| 使用 Fine-grained Token | 優先 | 高 |
| 限制信任目錄 | 僅信任必要目錄 | 高 |
| 設定工具權限 | 使用 `--deny-tool` 限制危險操作 | 高 |
| 記錄 AI 使用日誌 | 啟用 | 中 |
| 禁止在共用帳號使用 | 嚴格執行 | 高 |

---

## 4. 開發應用方式

### 4.1 互動模式基本操作

```bash
# 啟動互動模式
copilot

# 直接用自然語言提問或下達任務
# 範例提示：
```

**基本對話範例：**

```
> 這個專案的架構是什麼？請說明主要目錄結構
> 找出 src/main/java 中所有的 REST Controller
> 解釋 UserService.java 中的認證邏輯
```

**檔案操作範例：**

```
> 在 src/main/java/com/app/ 下建立 UserController.java，包含 CRUD 端點
> 修改 pom.xml，加入 Spring Security 依賴
> 重寫 README.md，讓新人更容易理解
```

**Shell 指令範例：**

```
> 列出 CPU 使用率最高的前 10 個程序
> 找出 port 8080 被哪個程序占用
> 清理所有停止的 Docker 容器和未使用的映像
```

**直接執行 Shell 指令（不透過 AI）：**

```bash
# 在互動模式中使用 ! 前綴直接執行 Shell 指令
!git status
!docker ps
!mvn clean compile
```

### 4.2 計畫模式（Plan Mode）

適合複雜的多檔案變更、重構或新功能開發。

```bash
# 方法一：在互動模式中按 Shift+Tab 切換至計畫模式
# 方法二：使用 /plan 指令
/plan 新增 OAuth2 認證，支援 Google 和 GitHub 登入
```

**計畫模式流程：**

1. Copilot 分析專案結構和需求
2. 提出釐清問題確認範圍
3. 建立結構化實作計畫（含檢查項目）
4. 將計畫儲存至 `plan.md`
5. 等待您確認後才開始實作

**計畫輸出範例：**

```markdown
# Implementation Plan: OAuth2 Authentication

## Overview
Add social authentication using OAuth2 with Google and GitHub providers.

## Tasks
- [ ] Install dependencies (passport, passport-google-oauth20, passport-github2)
- [ ] Create authentication routes in `/api/auth`
- [ ] Implement passport strategies for each provider
- [ ] Add session management middleware
- [ ] Create login/logout UI components
- [ ] Add environment variables for OAuth credentials
- [ ] Write integration tests
```

**何時使用計畫模式：**

| 適合使用 | 不需使用 |
|---|---|
| 複雜多檔案變更 | 快速 Bug 修復 |
| 大型重構 | 單一檔案修改 |
| 新功能開發 | 簡單查詢 |
| 跨模組變更 | 解釋程式碼 |

**最佳工作流程：Explore → Plan → Code → Commit**

```
> Read the authentication files but don't write code yet     # 探索
> /plan Implement password reset flow                        # 計畫
> （審閱計畫，提出修改建議）                                    # 審閱
> Proceed with the plan                                      # 實作
> Run the tests and fix any failures                         # 驗證
> Commit these changes with a descriptive message            # 提交
```

### 4.3 程式化模式（Programmatic Mode）

適合 CI/CD、自動化腳本、單次任務執行。

```bash
# 基本用法
copilot -p "顯示本週的 commits 並摘要" --allow-tool 'shell(git)'

# 允許所有工具（⚠️ 注意安全風險）
copilot -p "Revert the last commit" --allow-all-tools

# 限制特定工具
copilot -p "分析程式碼品質" --allow-tool 'shell' --deny-tool 'shell(rm)'

# 從腳本管道輸入
echo "Fix all lint errors in src/" | copilot --allow-tool 'write'
```

> **⚠️ 警告**：使用 `--allow-all-tools` 時，Copilot 擁有與您相同的檔案存取和指令執行權限，且無需事先取得您的同意。建議僅在受控環境（如容器、VM）中使用。

### 4.4 檔案引用與上下文控制

**使用 `@` 引用檔案：**

```
# 引用特定檔案作為上下文
> Explain @config/ci/ci-required-checks.yml
> Fix the bug in @src/app.js
> 根據 @docs/API.md 的規格，實作 UserController
```

輸入 `@` 後會自動顯示路徑建議，使用方向鍵選取後按 Tab 完成。

**上下文管理指令：**

```bash
# 查看目前上下文使用情況
/context

# 手動壓縮對話歷史
/compact

# 查看使用統計
/usage

# 清除對話、開始新話題
/clear
# 或
/new
```

**切換推論可見性：**

按 `Ctrl+T` 可顯示或隱藏模型的推論過程，觀察 Copilot 如何思考複雜問題。

### 4.5 程式碼產生與重構

**專案建立：**

```
# 建立完整的 Next.js 應用
> Use the create-next-app kit and tailwind CSS to create a next.js app.
> The app should be a dashboard built with data from the GitHub API.
> After creating the app, give me easy to follow instructions on how to build,
> run, and view the app in my browser.

# 建立 Spring Boot 專案骨架
> 建立一個 Spring Boot 3.4 + Java 21 的 REST API 專案，
> 包含 User CRUD 端點、JPA + PostgreSQL、Spring Security JWT 認證。
> 使用 Clean Architecture 目錄結構。
```

**程式碼重構：**

```
# 重構建議
> Suggest improvements to @src/services/UserService.java
> 重構這個專案中所有 class components 為 functional components with hooks

# 搭配計畫模式的重構
> /plan Migrate all class components to functional components with hooks
```

**Code Review：**

```bash
# 使用 /review 指令
/review

# 指定 Review 重點
> /review Use Opus 4.5 and Codex 5.2 to review the changes in my current branch
> against main. Focus on potential bugs and security issues.
```

### 4.6 測試程式產生

```
# 使用 TDD 工作流程
> Write failing tests for the user registration flow
# （審閱測試）
> Now implement code to make all tests pass
# （審閱實作）
> Commit with message "feat: add user registration"

# 產生 JUnit 測試
> 為 @src/main/java/com/app/UserService.java 撰寫 JUnit 5 測試案例，
> 包含正常和異常情境，使用 Mockito

# 產生 API 整合測試
> 使用 Spring MockMvc 為 UserController 的所有端點撰寫整合測試

# 產生 E2E 測試
> 使用 Playwright 撰寫使用者登入流程的 E2E 測試
```

### 4.7 Dockerfile 與 CI/CD 產生

```
# 產生最佳化 Dockerfile
> 為 Java 21 Spring Boot 應用撰寫多階段建置 Dockerfile，
> 使用 Eclipse Temurin 基底映像、非 root 使用者、健康檢查

# 產生 docker-compose.yml
> 撰寫 docker-compose.yml 開發環境，包含 app、postgres、redis、kafka

# 產生 GitHub Actions Workflow
> Branch off from main and create a GitHub Actions workflow that will run
> on pull requests. The workflow should run eslint, and if errors are found,
> the workflow should cause the PR check to fail.
> Push the new branch and create a pull request.
```

### 4.8 Git 操作與 PR 管理

Copilot CLI 可以直接操作 Git 和 GitHub：

```
# Git 操作
> Commit the changes to this repo
> Revert the last commit, leaving the changes unstaged
> Rebase this branch against main
> Resolve the merge conflicts in package.json
> What changes went into version 2.3.0?

# Pull Request 管理
> List my open PRs
> Create a PR for this branch with a detailed description
> Check the changes made in PR https://github.com/org/repo/pull/123.
> Report any serious errors.
> Merge all of the open PRs that I've created in org/repo
> Close PR #11 on org/repo

# Issue 管理
> List all open issues assigned to me in org/repo
> I've been assigned this issue: https://github.com/org/repo/issues/1234.
> Start working on this for me in a suitably named branch.
> Raise an improvement issue in org/repo about the file handling bug
```

### 4.9 工具權限管理

Copilot CLI 使用權限系統控制工具存取。當 Copilot 需要修改檔案或執行指令時，會要求您同意。

**權限選項：**

| 選項 | 說明 |
|---|---|
| **1. Yes** | 允許本次操作，下次再詢問 |
| **2. Yes, and approve TOOL for the rest of session** | 允許此工具在本次 Session 中不再詢問 |
| **3. No (Esc)** | 拒絕，並提供替代指示 |

**命令列預設權限：**

```bash
# 允許所有工具（⚠️ 高風險）
copilot --allow-all-tools
# 或
copilot --allow-all
# 或
copilot --yolo

# 允許特定工具
copilot --allow-tool 'shell(git)'
copilot --allow-tool 'shell(npm run:*)'
copilot --allow-tool 'write'

# 禁止特定工具
copilot --deny-tool 'shell(rm)'
copilot --deny-tool 'shell(git push)'

# 組合使用：允許所有但禁止危險操作
copilot --allow-all-tools --deny-tool 'shell(rm)' --deny-tool 'shell(git push)'

# 允許 MCP Server 工具
copilot --allow-tool 'My-MCP-Server'
copilot --deny-tool 'My-MCP-Server(dangerous_tool)'
```

**路徑權限：**

```bash
# 預設只能存取當前目錄和子目錄
# 允許所有路徑（⚠️ 高風險）
copilot --allow-all-paths

# 允許特定 URL
copilot --allow-url github.com

# 允許所有 URL
copilot --allow-all-urls
```

**重置已核准的工具：**

```bash
# 在互動模式中
/reset-allowed-tools
```

### 4.10 團隊開發最佳實踐

**Copilot CLI 使用規範建議：**

| 規範項目 | 說明 |
|---|---|
| **程式碼審核** | AI 產生的所有程式碼必須經過 Code Review |
| **Prompt 記錄** | 建議記錄重要的 Prompt 供團隊共享 |
| **不盲目信任** | 所有 AI 建議需理解後再接受 |
| **敏感資料** | 嚴禁在 Prompt 中包含密碼、金鑰等敏感資料 |
| **一致性** | 團隊統一 Copilot CLI 版本和設定 |
| **知識沉澱** | 將有效的 Prompt 模式整理為團隊知識庫 |
| **權限控管** | 避免使用 `--yolo`，明確指定允許的工具 |

> **實務建議**：建議每週舉辦一次「AI 輔助開發分享會」，讓團隊成員分享有效的 Prompt 和使用技巧，加速整體團隊的 AI 開發能力提升。

---

## 5. 自訂與擴充功能

### 5.1 自訂指令（Custom Instructions）

自訂指令讓您為 Copilot 提供額外上下文，包括專案規範、建置方式和偏好設定。所有自訂指令檔案會自動合併，無優先級覆蓋。

**支援的指令檔位置：**

| 位置 | 作用範圍 |
|---|---|
| `~/.copilot/copilot-instructions.md` | 全域（所有 Session） |
| `.github/copilot-instructions.md` | 當前專案 |
| `.github/instructions/**/*.instructions.md` | 當前專案（模組化） |
| `AGENTS.md`（Git 根目錄或工作目錄） | 當前專案 |
| `Copilot.md`、`GEMINI.md`、`CODEX.md` | 當前專案 |

**範例 — 專案自訂指令（`.github/copilot-instructions.md`）：**

```markdown
## Build Commands
- `mvn clean compile` - Build the project
- `mvn test` - Run all tests
- `mvn verify` - Run all checks

## Code Style
- Use Java 21+ features
- Follow Clean Architecture pattern
- Always add JavaDoc comments for public APIs
- Use Log4j2 for logging

## Workflow
- Run `mvn verify` after making changes
- Commit messages follow Conventional Commits format
- Create feature branches from `main`
```

> **提示**：自訂指令應保持簡潔和可操作。過長的指令可能降低效果。

### 5.2 自訂代理（Custom Agents）

自訂代理是 Copilot 的專用版本，針對特定工作流程最佳化。

**內建代理：**

| 代理名稱 | 功能 |
|---|---|
| **Explore** | 快速分析程式碼庫，不影響主要上下文 |
| **Task** | 執行建置和測試指令，成功時簡短摘要，失敗時完整輸出 |
| **Plan** | 分析相依性和結構，建立實作計畫 |
| **Code-review** | 專注於發現真正的問題，減少雜訊 |

**使用代理：**

```bash
# 方法一：使用 /agent 指令選擇
/agent

# 方法二：在提示中直接提及
> Use the refactoring agent to refactor this code block

# 方法三：命令列指定
copilot --agent=refactor-agent --prompt "Refactor this code block"
```

**建立自訂代理：**

自訂代理檔案放置位置：

| 位置 | 作用範圍 |
|---|---|
| `~/.copilot/agents/` | 所有專案 |
| `.github/agents/` | 當前專案 |
| `.github-private/agents/` | 組織或企業層級 |

### 5.3 技能（Skills）

技能讓您透過指令、腳本和資源增強 Copilot 執行專門任務的能力。

```
# 使用技能
> 使用 security-audit 技能檢查這個專案的安全性
```

更多資訊請參閱 [About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)。

### 5.4 Hooks

Hooks 讓您在代理執行的關鍵時間點執行自訂 Shell 指令，實現驗證、日誌記錄、安全掃描或工作流程自動化。

更多資訊請參閱 [About hooks](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks)。

### 5.5 AI 模型選擇

使用 `/model` 指令或 `--model` 命令列選項選擇模型：

```bash
# 在互動模式中切換模型
/model

# 命令列指定模型
copilot --model "claude-opus-4.5"
```

**可用模型與建議用途：**

| 模型 | 適用場景 | 說明 |
|---|---|---|
| **Claude Opus 4.5**（預設） | 複雜架構、困難除錯、細膩重構 | 最強大，使用較多  Premium Requests |
| **Claude Sonnet 4.5** | 日常程式碼撰寫、一般例行任務 | 快速且成本效益高 |
| **GPT-5.2 Codex** | 程式碼產生、Code Review、直接實作 | 適合審閱其他模型產生的程式碼 |

**使用建議：**

- **Opus 4.5**：適合需要深度推理、複雜系統設計、微妙 Bug 調查或大量上下文理解的任務
- **Sonnet 4.5**：處理日常程式碼工作，速度和成本效率兼顧
- **Codex**：適合大量程式碼產生，以及作為「第二意見」審閱其他模型的產出
- 可在 Session 中途使用 `/model` 切換模型

> **注意**：每次提交 Prompt 都會消耗 Premium Requests 配額，不同模型的乘數不同（如 `Claude Opus 4.5 (1x)`）。詳見 [Premium Requests 說明](https://docs.github.com/en/copilot/concepts/billing/copilot-requests)。

### 5.6 Copilot Memory

Copilot Memory 讓 Copilot 建立對專案的持久理解，儲存程式碼慣例、模式和偏好的「記憶」。這減少了重複解釋上下文的需求，讓未來的 Session 更有效率。

更多資訊請參閱 [About agentic memory for GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)。

---

## 6. 與 MCP（Model Context Protocol）串接方式

### 6.1 MCP 架構概念

MCP（Model Context Protocol）是一種開放標準，用於標準化 AI 模型與外部工具、資料來源之間的通訊。Copilot CLI **內建 MCP 支援**，預設即包含 GitHub MCP Server。

**MCP 核心概念：**

| 概念 | 說明 |
|---|---|
| **MCP Host** | AI 應用程式（Copilot CLI），負責接收使用者請求 |
| **MCP Client** | 內嵌於 Host 中的元件，管理與 Server 的連線 |
| **MCP Server** | 提供工具（Tools）、資源（Resources）、提示（Prompts）的服務 |
| **Transport** | 通訊層，支援 stdio 或 HTTP/SSE |
| **Tools** | Server 提供的可呼叫函式（如資料庫查詢、API 呼叫） |

```mermaid
graph TB
    subgraph "MCP Host（Copilot CLI）"
        A[使用者] --> B[copilot]
        B --> C[MCP Client]
    end

    subgraph "MCP Servers"
        D["GitHub MCP Server<br/>（內建）"]
        E[Database Server]
        F[Internal API Server]
        G[Document Server]
    end

    subgraph "資源"
        H[GitHub.com]
        I[(PostgreSQL)]
        J[REST API]
        K[Confluence]
    end

    C -->|"JSON-RPC"| D
    C -->|"JSON-RPC"| E
    C -->|"JSON-RPC"| F
    C -->|"JSON-RPC"| G

    D --> H
    E --> I
    F --> J
    G --> K

    style A fill:#e1f5fe
    style C fill:#fff3e0
    style D fill:#c8e6c9
    style E fill:#c8e6c9
    style F fill:#c8e6c9
    style G fill:#c8e6c9
```

### 6.2 內建 GitHub MCP Server

Copilot CLI 預設即包含 GitHub MCP Server，讓您可以直接與 GitHub.com 互動：

```
# 使用 GitHub MCP Server 的範例
> List my open PRs
> Create a PR for this branch with a detailed description
> Use the GitHub MCP server to find good first issues from org/repo
> List any Actions workflows in this repo that add comments to PRs
> Merge all of the open PRs that I've created in org/repo
```

> **提示**：在 Prompt 中明確提及「Use the GitHub MCP server」可以幫助 Copilot 選擇正確的工具。

### 6.3 新增 MCP Server

**方法一：使用互動指令（建議）：**

```bash
# 在互動模式中
/mcp add

# 填寫 MCP Server 詳細資訊，使用 Tab 切換欄位
# 按 Ctrl+S 儲存
```

**方法二：直接編輯設定檔：**

MCP Server 設定存放在 `~/.copilot/mcp-config.json`：

```json
{
  "mcpServers": {
    "database-query": {
      "command": "npx",
      "args": ["-y", "@company/mcp-database-server"],
      "env": {
        "DB_HOST": "db.company.com",
        "DB_PORT": "5432",
        "DB_NAME": "production_readonly"
      }
    },
    "internal-api": {
      "command": "python",
      "args": ["/opt/mcp-servers/api-server/main.py"],
      "env": {
        "API_BASE_URL": "https://api.internal.company.com",
        "API_KEY_FILE": "/etc/secrets/api-key"
      }
    }
  }
}
```

**使用 HTTP/SSE Transport 的遠端 MCP Server：**

```json
{
  "mcpServers": {
    "remote-api-server": {
      "url": "https://mcp.internal.company.com/sse",
      "headers": {
        "Authorization": "Bearer ${MCP_AUTH_TOKEN}"
      }
    }
  }
}
```

**管理 MCP Server：**

```bash
# 在互動模式中查看已設定的 MCP Server
/mcp

# 查看特定 MCP Server 的工具清單
# 選擇 Server 後即可查看
```

### 6.4 自訂 MCP Server 開發

**Node.js MCP Server 範例：**

```javascript
// mcp-server/index.js
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "company-tools",
  version: "1.0.0",
  description: "企業內部工具 MCP Server"
});

// 定義工具：查詢員工資訊
server.tool(
  "query-employee",
  "查詢員工資訊",
  {
    employeeId: z.string().describe("員工編號")
  },
  async ({ employeeId }) => {
    const response = await fetch(
      `${process.env.HR_API_URL}/employees/${employeeId}`,
      {
        headers: {
          "Authorization": `Bearer ${process.env.HR_API_TOKEN}`
        }
      }
    );
    const data = await response.json();

    return {
      content: [{
        type: "text",
        text: JSON.stringify(data, null, 2)
      }]
    };
  }
);

// 定義工具：檢查系統健康狀態
server.tool(
  "check-system-health",
  "檢查內部系統健康狀態",
  {
    systemName: z.string().describe("系統名稱")
  },
  async ({ systemName }) => {
    const response = await fetch(
      `${process.env.MONITOR_URL}/api/health/${systemName}`
    );
    const status = await response.json();

    return {
      content: [{
        type: "text",
        text: `系統 ${systemName} 狀態：${status.healthy ? '✅ 正常' : '❌ 異常'}\n延遲：${status.latency}ms`
      }]
    };
  }
);

// 啟動 Server
const transport = new StdioServerTransport();
await server.connect(transport);
```

**Python MCP Server 範例：**

```python
# mcp_server/main.py
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent
import httpx
import os
import json

server = Server("company-tools")

@server.tool()
async def query_database(query: str, database: str = "default") -> list[TextContent]:
    """
    執行唯讀 SQL 查詢（僅支援 SELECT）

    Args:
        query: SQL 查詢語句（僅限 SELECT）
        database: 資料庫名稱
    """
    if not query.strip().upper().startswith("SELECT"):
        return [TextContent(
            type="text",
            text="❌ 錯誤：僅允許 SELECT 查詢"
        )]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{os.environ['DB_PROXY_URL']}/query",
            json={"sql": query, "database": database},
            headers={"Authorization": f"Bearer {os.environ['DB_TOKEN']}"}
        )
        result = response.json()

    return [TextContent(
        type="text",
        text=json.dumps(result, indent=2, ensure_ascii=False)
    )]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### 6.5 與企業內部 API 整合

```mermaid
sequenceDiagram
    participant Dev as 開發者
    participant CLI as copilot CLI
    participant MCP as MCP Client
    participant GW as API Gateway
    participant API as Internal API
    participant Auth as Auth Server

    Dev->>CLI: "查詢客戶 A001 的帳戶餘額"
    CLI->>MCP: 識別需要呼叫 account-query 工具
    MCP->>Auth: 驗證 MCP Server Token
    Auth-->>MCP: Token 有效
    MCP->>GW: API Request（含認證標頭）
    GW->>API: 轉發請求
    API-->>GW: 回傳資料
    GW-->>MCP: 回傳結果
    MCP-->>CLI: 格式化結果
    CLI-->>Dev: "客戶 A001 帳戶餘額：NT$ 1,234,567"
```

**API Gateway 整合設定：**

```json
{
  "mcpServers": {
    "company-api": {
      "command": "node",
      "args": ["./mcp-servers/api-gateway-bridge/index.js"],
      "env": {
        "API_GATEWAY_URL": "https://gateway.company.com",
        "API_CLIENT_ID": "copilot-mcp-client",
        "API_CLIENT_SECRET_FILE": "/etc/secrets/api-client-secret",
        "ALLOWED_ENDPOINTS": "/api/v1/accounts,/api/v1/transactions,/api/v1/reports",
        "MAX_REQUESTS_PER_MINUTE": "30"
      }
    }
  }
}
```

### 6.6 MCP 安全與權限控管

**MCP 安全設計原則：**

| 原則 | 實作方式 |
|---|---|
| **最小權限** | 每個 MCP Server 僅存取必要的資源 |
| **認證隔離** | 不同 MCP Server 使用獨立的認證 Token |
| **唯讀優先** | 資料庫查詢 MCP Server 使用唯讀帳號 |
| **速率限制** | 設定每分鐘最大請求數 |
| **日誌記錄** | 記錄所有 MCP 工具呼叫 |
| **輸入驗證** | 所有工具輸入參數需驗證 |
| **工具權限** | 使用 `--deny-tool 'MCP-Server(tool)'` 限制特定工具 |

**安全設定範例：**

```json
{
  "mcpServers": {
    "secure-db-query": {
      "command": "node",
      "args": ["./mcp-servers/db-query/index.js"],
      "env": {
        "DB_CONNECTION": "readonly-replica.company.com",
        "DB_USER": "mcp_readonly",
        "DB_PASSWORD_FILE": "/etc/secrets/db-password",
        "ALLOWED_TABLES": "users,products,orders",
        "BLOCKED_COLUMNS": "password_hash,ssn,credit_card",
        "MAX_ROWS": "1000",
        "QUERY_TIMEOUT_MS": "5000",
        "AUDIT_LOG_PATH": "/var/log/mcp/db-query.log"
      }
    }
  }
}
```

> **實務建議**：在金融或醫療等高度監管的行業，建議在 MCP Server 前方加設 API Gateway，實施二次認證和資料遮蔽（Data Masking），確保敏感資料不會直接暴露給 AI 模型。

---

## 7. DevOps 整合模式

### 7.1 與 GitHub Actions 整合

**使用程式化模式在 CI/CD 中執行 Copilot CLI：**

```yaml
# .github/workflows/copilot-assisted-review.yml
name: Copilot Assisted Review

on:
  pull_request:
    types: [opened, synchronize]

permissions:
  contents: read
  pull-requests: write

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install Copilot CLI
        run: |
          curl -fsSL https://gh.io/copilot-install | bash

      - name: AI Code Review
        env:
          GH_TOKEN: ${{ secrets.COPILOT_PAT }}
        run: |
          copilot -p "Review the changes in this PR and summarize potential issues" \
            --allow-tool 'shell(git)' \
            --deny-tool 'shell(rm)' \
            --deny-tool 'shell(git push)'
```

**產生 GitHub Actions Workflow：**

```
# 在 Copilot CLI 互動模式中
> Branch off from main and create a GitHub Actions workflow that will run
> on pull requests, or can be run manually. The workflow should run eslint
> to check for problems. If errors are found, the workflow should cause the
> PR check to fail. Push the new branch and create a pull request.
```

### 7.2 與 CI/CD Pipeline 整合

**整合流程圖：**

```mermaid
graph LR
    subgraph "開發階段"
        A["程式碼撰寫<br/>Copilot IDE"] --> B["代理式開發<br/>copilot CLI"]
        B --> C[Commit & Push]
    end

    subgraph "CI Pipeline"
        C --> D[Build]
        D --> E[Unit Test]
        E --> F[SAST Scan]
        F --> G[Container Build]
    end

    subgraph "AI 輔助品質檢查"
        G --> H["AI Code Review<br/>copilot -p"]
        H --> I{通過?}
        I -->|是| J[Deploy to Staging]
        I -->|否| K[回饋給開發者]
    end

    subgraph "CD Pipeline"
        J --> L[Integration Test]
        L --> M[Performance Test]
        M --> N[Deploy to Production]
    end

    style A fill:#e1f5fe
    style B fill:#e1f5fe
    style H fill:#fff3e0
```

**Pipeline 腳本中使用 Copilot CLI：**

```bash
#!/bin/bash
# scripts/ci-copilot-checks.sh

# 使用 Copilot 生成變更日誌
generate_changelog() {
    local last_tag=$(git describe --tags --abbrev=0 2>/dev/null || echo "HEAD~10")
    local log=$(git log ${last_tag}..HEAD --oneline)

    copilot -p "根據以下 git log，產生結構化的 CHANGELOG 條目：${log}" \
        --allow-tool 'write' \
        --deny-tool 'shell(rm)'
}

# 使用 Copilot 分析程式碼品質
analyze_quality() {
    copilot -p "分析 src/ 目錄中的程式碼品質，報告潛在的 Bug 和效能問題" \
        --allow-tool 'shell(grep)' \
        --allow-tool 'shell(find)' \
        --deny-tool 'shell(rm)'
}

# 主流程
case "$1" in
    changelog) generate_changelog ;;
    analyze) analyze_quality ;;
    *) echo "Usage: $0 {changelog|analyze}"; exit 1 ;;
esac
```

### 7.3 容器化開發流程

```
# 使用 Copilot CLI 輔助容器化開發

# 1. 產生最佳化的 Dockerfile
> 為 Java 21 Spring Boot 應用產生 Production-ready Dockerfile，
> 包含健康檢查、非 root 使用者、多階段建置

# 2. Docker 故障排除
> Docker container 一直重啟，如何查看原因

# 3. 映像安全掃描
> 使用 Trivy 掃描 Docker 映像漏洞並產生 JSON 報告

# 4. Kubernetes 資源產生
> 為 Spring Boot 應用產生 Kubernetes Deployment、Service、Ingress YAML
```

### 7.4 AI 輔助 Code Review

**使用 `/review` 指令：**

```bash
# 在互動模式中
/review

# 指定 Review 範圍和重點
> /review Use Opus 4.5 and Codex 5.2 to review the changes in my current branch
> against main. Focus on potential bugs and security issues.
```

**PR Review 工作流程：**

```
# 查看 PR 變更並請 AI 分析
> Check the changes made in PR https://github.com/org/repo/pull/42.
> Report any serious errors you find in these changes.

# 針對特定安全性問題
> 審查 PR #42 的變更，特別注意：
> 1. SQL Injection 風險
> 2. XSS 漏洞
> 3. 認證和授權問題
> 4. 敏感資料洩漏
```

### 7.5 委派工作至 Copilot Coding Agent

使用 `/delegate` 指令或 `&` 前綴將任務委派至雲端 Copilot Coding Agent：

```bash
# 方法一：使用 /delegate 指令
/delegate complete the API integration tests and fix any failing edge cases

# 方法二：使用 & 前綴
& Add dark mode support to the settings page

# 方法三：在 Session 外委派
copilot -p "Update the documentation" --delegate
```

**委派後流程：**

1. Copilot 會要求 commit 未暫存的變更作為 checkpoint
2. 在新分支中建立 Draft Pull Request
3. Copilot Coding Agent 在雲端背景執行
4. 完成後請求您 Review
5. 提供 PR 和 Agent Session 的連結

**何時使用委派：**

| 適合委派 | 不適合委派 |
|---|---|
| 附帶任務 | 核心功能開發 |
| 文件更新 | 即時除錯 |
| 獨立模組重構 | 互動式探索 |
| 長時間執行的任務 | 需要即時回饋 |

### 7.6 Commit Message 與 PR 最佳實務

```
# 產生 Conventional Commit Message
> Commit these changes with a descriptive message following Conventional Commits format

# 建立 PR 並附帶詳細描述
> Create a PR for this branch with a detailed description

# Conventional Commit 格式範例
# feat(auth): 新增 JWT Token 刷新機制
# fix(api): 修正使用者查詢 N+1 問題
# docs(readme): 更新安裝說明
# refactor(service): 重構訂單處理邏輯
# test(user): 新增使用者註冊測試案例
# ci(pipeline): 加入 SonarQube 分析步驟
```

> **實務建議**：在 CI/CD Pipeline 中加入 Commit Message Lint（如 `commitlint`），搭配 Copilot CLI 產生的 Commit Message，確保所有提交訊息符合團隊規範。

---

## 8. 系統維護與治理

### 8.1 CLI 版本管理策略

**版本管理原則：**

| 策略 | 說明 |
|---|---|
| **統一版本** | 團隊內所有成員使用相同版本 |
| **延遲升級** | 新版發布後等待 1-2 週再升級 |
| **測試先行** | 升級前在測試環境驗證 |
| **記錄版本** | 在專案文件中記錄使用的版本 |

**版本管理指令：**

```bash
# 查看當前版本
copilot --version

# 升級至最新版
# Windows
winget upgrade GitHub.Copilot

# macOS / Linux (Homebrew)
brew upgrade copilot-cli

# npm
npm update -g @github/copilot

# 安裝腳本
curl -fsSL https://gh.io/copilot-install | bash

# 安裝特定版本（安裝腳本）
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.410" bash
```

**團隊版本管理腳本：**

```bash
#!/bin/bash
# scripts/check-copilot-version.sh

REQUIRED_VERSION="0.0.410"

CURRENT_VERSION=$(copilot --version 2>/dev/null | grep -oP '\d+\.\d+\.\d+')

if [ -z "$CURRENT_VERSION" ]; then
    echo "❌ Copilot CLI 未安裝"
    exit 1
fi

echo "✅ Copilot CLI 版本：$CURRENT_VERSION（要求：>= $REQUIRED_VERSION）"
```

### 8.2 企業升版流程

```mermaid
graph TD
    A[GitHub 發布新版] --> B[技術團隊評估]
    B --> C{有重大變更?}
    C -->|是| D[建立升級測試計畫]
    C -->|否| E[簡易測試]

    D --> F[在 Lab 環境測試]
    E --> F

    F --> G{測試通過?}
    G -->|是| H[發布升級通知]
    G -->|否| I[回報問題<br/>等待修復版]

    H --> J[先導團隊升級<br/>觀察 1 週]
    J --> K{穩定?}
    K -->|是| L[全面推廣升級]
    K -->|否| M[回滾 + 回報]

    L --> N[更新文件與設定]

    style A fill:#e1f5fe
    style L fill:#c8e6c9
    style M fill:#ffcdd2
```

**回滾策略：**

```bash
# Windows - 安裝特定版本
winget install GitHub.Copilot --version 0.0.xxx

# macOS / Linux - 使用安裝腳本指定版本
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.xxx" bash

# npm - 安裝特定版本
npm install -g @github/copilot@0.0.xxx
```

### 8.3 AI 使用紀錄稽核建議

**需記錄的稽核項目：**

| 稽核項目 | 記錄內容 | 保存期限 |
|---|---|---|
| 使用者身分 | GitHub 帳號、登入時間 | 1 年 |
| Session 資訊 | 啟動時間、持續時間 | 6 個月 |
| 模型使用 | 使用的模型、Premium Requests 消耗 | 6 個月 |
| MCP 呼叫 | 工具名稱、參數概要 | 1 年 |
| 錯誤事件 | 認證失敗、API 錯誤 | 1 年 |

**日誌設定：**

```bash
# 查看日誌設定說明
copilot help logging

# 設定環境變數啟用日誌
# （詳細設定請參考 copilot help logging 的輸出）
```

**Session 內使用統計：**

```bash
# 查看使用統計
/usage
# 顯示：Premium Requests 使用量、Session 時長、編輯行數、Token 使用分佈
```

### 8.4 使用權限控管

**權限控管矩陣：**

| 角色 | Copilot CLI | 工具權限建議 | MCP 存取 |
|---|---|---|---|
| **資深開發者** | ✅ 完整權限 | `--allow-tool 'shell' --allow-tool 'write'` | ✅ 完整 |
| **一般開發者** | ✅ 基本功能 | 預設（逐次核准） | ⚠️ 限定 |
| **實習生** | ✅ 基本功能 | 預設 + `--deny-tool 'shell(rm)'` | ❌ |
| **CI/CD Bot** | ✅ 程式化模式 | `--allow-tool 'shell(git)' --deny-tool 'shell(rm)'` | ⚠️ 限定 |

### 8.5 Session 管理

Copilot CLI 支援無限 Session，自動管理上下文：

**Session 管理指令：**

```bash
# 查看當前 Session 資訊
/session

# 查看 Session 檢查點
/session checkpoints

# 查看特定檢查點詳情
/session checkpoints 1

# 查看 Session 中建立的臨時檔案
/session files

# 查看當前計畫
/session plan

# 恢復之前的 Session
/resume
# 或命令列
copilot --resume

# 快速恢復最近關閉的 Session
copilot --continue
```

**Session 儲存位置：**

```
~/.copilot/session-state/{session-id}/
├── events.jsonl      # 完整 Session 歷史
├── workspace.yaml    # 中繼資料
├── plan.md           # 實作計畫（若有）
├── checkpoints/      # 壓縮歷史
└── files/            # 持久化檔案
```

**Session 最佳實踐：**

- 不相關的任務之間使用 `/clear` 或 `/new` 清除上下文
- 定期使用 `/context` 查看上下文使用情況
- 上下文接近 95% 時會自動壓縮，通常不需手動 `/compact`

### 8.6 效能監控與成本控管

**監控指標：**

| 指標 | 說明 | 建議 |
|---|---|---|
| Premium Requests 使用量 | 每月配額消耗 | 使用 `/usage` 追蹤 |
| 模型乘數 | 不同模型消耗不同 | 日常任務用 Sonnet 4.5 節省配額 |
| Session 時長 | 長 Session 可能降低品質 | 適時 `/clear` 重新開始 |
| MCP Server 回應時間 | 自訂 MCP Server 效能 | 設定 timeout |

**成本最佳化策略：**

1. 日常任務使用 **Sonnet 4.5**（較低的 Request 乘數）
2. 僅在需要深度推理時切換至 **Opus 4.5**
3. 定期（每月）檢視使用報表
4. 識別低使用率使用者，進行教育訓練或停用授權
5. 使用 `/delegate` 替代冗長的本地 Session

> **實務建議**：建議每季度進行一次 Copilot 使用效益評估，比較導入前後的開發效率指標（如 PR Merge 時間、Bug 修復速度），作為持續投資的依據。

---

## 9. 企業導入最佳實踐

### 9.1 開發團隊使用規範

**Copilot CLI 使用規範（建議納入團隊開發手冊）：**

| 編號 | 規範 | 等級 |
|---|---|---|
| R-01 | AI 產生的程式碼必須經過人工 Code Review | 強制 |
| R-02 | 禁止在 Prompt 中包含密碼、金鑰等機密資訊 | 強制 |
| R-03 | 禁止在 Prompt 中包含客戶個資 | 強制 |
| R-04 | AI 產生的程式碼需通過既有的 CI/CD 品質門檻 | 強制 |
| R-05 | 重要決策不可完全依賴 AI 建議 | 強制 |
| R-06 | 建立 `.github/copilot-instructions.md` 統一專案規範 | 強制 |
| R-07 | 避免使用 `--yolo` / `--allow-all-tools` | 強制 |
| R-08 | 將有效的 Prompt 模板分享至團隊知識庫 | 建議 |
| R-09 | 定期（每季）檢視 AI 使用效益 | 建議 |
| R-10 | 新人需完成 AI 工具培訓才可在正式專案使用 | 強制 |

### 9.2 AI 輔助開發風險

**風險矩陣：**

| 風險類型 | 風險描述 | 影響 | 機率 | 緩解措施 |
|---|---|---|---|---|
| **程式碼品質** | AI 產生包含 Bug 的程式碼 | 高 | 中 | Code Review + 自動化測試 |
| **安全性** | AI 產生有漏洞的程式碼 | 高 | 中 | SAST/DAST 掃描 + Security Review |
| **授權風險** | AI 產出與開源程式碼雷同 | 高 | 低 | 啟用 public code filter |
| **技能退化** | 過度依賴 AI 導致技能下降 | 中 | 中 | 定期技術分享 + 考核 |
| **資料洩漏** | Prompt 中含敏感資料 | 高 | 低 | 使用規範 + 自動化偵測 |
| **檔案損壞** | AI 修改錯誤檔案 | 高 | 低 | 限制信任目錄 + 工具權限控管 |
| **服務中斷** | GitHub 服務停機 | 中 | 低 | 建立離線備援工作流程 |

### 9.3 原始碼洩漏風險管理

**防範措施：**

```mermaid
graph TB
    subgraph "防護層"
        A[第一層：使用規範]
        B[第二層：技術控制]
        C[第三層：監控與稽核]
    end

    A --> A1[禁止在 Prompt 中貼上大量原始碼]
    A --> A2[禁止在 Prompt 中包含機密邏輯]
    A --> A3[使用偽代碼描述需求]

    B --> B1[啟用 GitHub 公開程式碼過濾]
    B --> B2[限制信任目錄範圍]
    B --> B3[MCP Server 資料遮蔽]
    B --> B4[使用 --deny-tool 限制危險操作]

    C --> C1[定期審核 AI 使用日誌]
    C --> C2[DLP 工具監控]
    C --> C3[異常使用告警]

    style A fill:#e8f5e9
    style B fill:#e3f2fd
    style C fill:#fff3e0
```

**Prompt 安全範例：**

```
# ❌ 不安全的 Prompt
> 修正這段包含資料庫密碼 'P@ssw0rd123' 的連線字串

# ✅ 安全的 Prompt
> 如何使用環境變數設定 JDBC 資料庫連線字串

# ❌ 不安全的 Prompt
> 解釋 @src/main/java/com/company/core/TradingEngine.java（含高度機密邏輯）

# ✅ 安全的 Prompt
> 如何實作交易引擎的冪等性（idempotency）設計
```

### 9.4 Prompt 設計標準化

**Prompt 設計原則：**

| 原則 | 說明 | 範例 |
|---|---|---|
| **明確性** | 清楚描述需求 | 「產生 Spring Boot REST API」而非「寫 API」 |
| **上下文** | 提供必要背景 | 「使用 Java 21 + Spring Boot 3.4」 |
| **限制** | 指定限制條件 | 「不使用 Lombok」 |
| **格式** | 指定輸出格式 | 「以 YAML 格式輸出」 |
| **安全** | 不含敏感資訊 | 使用變數佔位符而非真實值 |
| **檔案引用** | 使用 `@` 引用檔案 | 「修改 @src/app.js 中的 Bug」 |

**Prompt 模板範例庫：**

```markdown
## 團隊 Prompt 模板

### API 開發
> 使用 {framework} 建立 {resource} 的 REST API，
> 包含 CRUD 操作、輸入驗證、錯誤處理和 OpenAPI 文件。
> 使用 {language} {version}。

### 計畫式重構
> /plan 將所有 {pattern} 重構為 {new_pattern}，
> 遵循 SOLID 原則，確保所有測試通過。

### Code Review
> /review 審查當前分支相對於 main 的變更，
> 專注於安全性風險和效能問題。

### 測試案例
> 為 @{file_path} 中的 {class}.{method}() 方法撰寫 {test_framework} 測試案例，
> 包含以下情境：正常路徑、邊界值、異常情境。
> 使用 Arrange-Act-Assert 模式。
```

### 9.5 AI 產出程式碼審核流程

```mermaid
graph TD
    A[AI 產生程式碼] --> B[開發者自我審查]
    B --> C{通過自我檢查?}
    C -->|否| D[修改或重新產生]
    C -->|是| E[提交 Pull Request]

    E --> F[自動化檢查]
    F --> F1[CI Build]
    F --> F2[Unit Test]
    F --> F3[SAST Scan]
    F --> F4[Code Coverage]

    F1 & F2 & F3 & F4 --> G{自動化檢查通過?}
    G -->|否| H[修正問題]
    G -->|是| I[人工 Code Review]

    I --> J{Reviewer 核可?}
    J -->|否| K[修改並重新送審]
    J -->|是| L[合併至主分支]

    H --> E
    K --> E
    D --> A

    style A fill:#fff3e0
    style L fill:#c8e6c9
```

**AI 程式碼審核重點：**

1. **邏輯正確性**：AI 是否正確理解需求
2. **安全性**：是否有 SQL Injection、XSS 等漏洞
3. **效能**：是否有 N+1 查詢、記憶體洩漏等問題
4. **授權合規**：是否與公開程式碼雷同
5. **可維護性**：程式碼是否符合團隊風格
6. **測試覆蓋**：是否有對應的測試案例

### 9.6 內部教育訓練建議

**訓練計畫：**

| 階段 | 對象 | 內容 | 時長 |
|---|---|---|---|
| **Level 1** | 所有開發者 | 安裝、基本互動模式、安全規範 | 2 小時 |
| **Level 2** | 資深開發者 | Plan Mode、Custom Instructions、MCP 串接 | 4 小時 |
| **Level 3** | 技術主管 | 治理策略、成本管理、風險控管 | 2 小時 |
| **Level 4** | DevOps 工程師 | 程式化模式、CI/CD 整合、Coding Agent 委派 | 4 小時 |

**培訓教材建議架構：**

```
📁 training/
├── Level-1-基礎篇/
│   ├── 01-安裝與設定.md
│   ├── 02-互動模式基本操作.md
│   ├── 03-安全規範.md
│   └── exercises/
├── Level-2-進階篇/
│   ├── 01-Plan-Mode-與-Custom-Instructions.md
│   ├── 02-MCP-串接.md
│   ├── 03-Custom-Agents-與-Skills.md
│   └── exercises/
├── Level-3-管理篇/
│   ├── 01-治理策略.md
│   ├── 02-成本管理.md
│   └── 03-風險控管.md
└── Level-4-DevOps篇/
    ├── 01-程式化模式與CI-CD整合.md
    ├── 02-Coding-Agent-委派.md
    └── exercises/
```

> **實務建議**：建議每月舉辦一次「AI 開發工具使用分享會」，邀請團隊成員分享實際使用經驗和有效的 Prompt 模式。同時建立內部 Wiki 頁面，持續累積最佳實踐。

---

## 10. 風險與限制說明

### 10.1 Copilot CLI 功能限制

| 限制項目 | 說明 | 影響 |
|---|---|---|
| **需要網路連線** | 必須連線至 GitHub 雲端 | 離線時無法使用 |
| **Public Preview** | 功能可能變更 | 企業需評估穩定性風險 |
| **語言偏向** | 英文 Prompt 效果較中文佳 | 建議用英文撰寫技術 Prompt |
| **幻覺問題** | AI 可能產生看似合理但錯誤的回答 | 需人工驗證 |
| **即時性** | 訓練資料有截止日期 | 最新技術可能不準確 |
| **路徑偵測限制** | 複雜 Shell 結構中的路徑可能無法偵測 | 部分安全檢查可能失效 |
| **URL 偵測限制** | 環境變數中的 URL 可能無法偵測 | 部分 URL 權限檢查可能失效 |

### 10.2 Premium Request 配額

每次提交 Prompt（互動模式和程式化模式均計算）都會消耗 Premium Requests 配額。

| 模型 | 乘數 | 說明 |
|---|---|---|
| **Claude Opus 4.5** | 較高 | 最強大，消耗較多配額 |
| **Claude Sonnet 4.5** | 1x | 日常推薦，平衡效能與成本 |
| **GPT-5.2 Codex** | 依方案 | 適合程式碼產生和 Review |

**管理配額：**

```bash
# 查看目前使用量
/usage

# 切換至較低成本的模型
/model
# 選擇 Sonnet 4.5
```

### 10.3 安全性考量

**核心安全原則：**

| 原則 | 說明 |
|---|---|
| **信任目錄** | 僅在您信任的目錄中啟動 Copilot CLI |
| **工具核准** | 預設每個可能修改檔案的操作都需核准 |
| **路徑權限** | 預設只能存取當前目錄及子目錄 |
| **URL 權限** | 預設所有外部 URL 存取需核准 |
| **不提交機密** | Copilot 設計上會避免提交機密，但仍需人工確認 |

**安全風險緩解建議：**

1. **使用受限環境**：在 VM、Container 或專用系統中使用 `--allow-all-tools`
2. **明確工具權限**：使用 `--allow-tool` 和 `--deny-tool` 精確控制
3. **審查所有變更**：在接受前仔細檢查 Copilot 建議的操作
4. **限制信任目錄**：避免將家目錄加入信任清單
5. **定期審查**：定期檢視 `~/.copilot/config.json` 中的信任目錄

### 10.4 網路依賴風險

**風險評估：**

| 風險場景 | 影響 | 機率 | 緩解措施 |
|---|---|---|---|
| GitHub 全球服務中斷 | 完全無法使用 | 低 | 建立離線備援工作流程 |
| 企業網路故障 | 無法連線至 GitHub | 中 | 確保核心開發不完全依賴 AI |
| Proxy 問題 | 間歇性連線失敗 | 中 | 設定重試機制 |
| DNS 解析失敗 | 無法解析 GitHub 網域 | 低 | 設定備用 DNS |
| SSL 憑證問題 | 連線被拒絕 | 低 | 定期更新 CA 憑證 |

**離線備援計畫：**

1. 確保核心開發工作不完全依賴 Copilot CLI
2. 維護常用指令和工作流程的離線備忘錄
3. 建立本地開發文件和程式碼範本庫

### 10.5 法規與合規性建議

**適用法規與標準：**

| 法規/標準 | 相關要求 | Copilot CLI 對應 |
|---|---|---|
| **個資保護法** | 不得外洩個人資料 | 禁止在 Prompt 中包含個資 |
| **ISO 27001** | 資訊安全管理 | 建立 AI 工具使用政策 |
| **金管會資安規範** | 金融業資安要求 | 嚴格控管資料傳輸 |
| **GDPR**（歐盟） | 資料保護 | 注意資料傳輸至美國的合規性 |
| **軟體授權** | 著作權 | 啟用公開程式碼過濾 |

**合規建議：**

1. **資料在地化**：確認 GitHub 的資料儲存位置符合法規要求
2. **隱私權評估**：在導入前進行 DPIA（Data Protection Impact Assessment）
3. **合約審查**：確認 GitHub Enterprise 合約包含適當的資料保護條款
4. **使用政策**：制定並公布 AI 工具使用政策
5. **資料保護**：Copilot CLI Public Preview 已包含[資料保護協議](https://gh.io/dpa)
6. **定期合規檢查**：每半年進行一次 AI 工具合規性審查

> **實務建議**：在金融業或醫療業等高度監管環境中，建議在導入前與法遵部門（Compliance）和資安部門（Security）共同進行風險評估，取得書面核准後再進行全面推廣。

---

## 附錄 A：新進成員檢查清單

### 環境建置

- [ ] 確認作業系統符合需求（Windows 需 PowerShell v6+）
- [ ] 安裝 Copilot CLI（使用 WinGet / Homebrew / npm /安裝腳本）
- [ ] 執行 `copilot --version` 確認安裝成功
- [ ] 啟動 `copilot` 並使用 `/login` 完成認證
- [ ] 設定 Proxy（如適用）
- [ ] 執行網路連線測試腳本

### 認證與授權

- [ ] 確認擁有 GitHub Copilot 授權
- [ ] 確認組織 Copilot CLI 政策已啟用
- [ ] 確認認證成功（`/login` 完成）
- [ ] 啟用 2FA（雙因素認證）

### 安全規範

- [ ] 閱讀並簽署 AI 工具使用規範
- [ ] 完成 Level 1 培訓課程
- [ ] 了解 Prompt 安全原則（禁止含機密資訊）
- [ ] 了解信任目錄的意義和設定方式
- [ ] 了解工具權限核准機制
- [ ] 了解 AI 產出程式碼的審核流程

### 功能驗證

- [ ] 測試互動模式基本對話
- [ ] 測試 `@file` 檔案引用功能
- [ ] 測試 `/plan` 計畫模式
- [ ] 測試 `/review` Code Review
- [ ] 測試 MCP Server 連線（如適用）

### 團隊協作

- [ ] 確認專案已有 `.github/copilot-instructions.md`
- [ ] 加入團隊 Prompt 模板庫頻道
- [ ] 訂閱版本更新通知
- [ ] 了解問題回報流程

---

## 附錄 B：常用指令速查表

### 安裝與認證

| 指令 | 說明 |
|---|---|
| `winget install GitHub.Copilot` | Windows 安裝 |
| `brew install copilot-cli` | macOS / Linux 安裝 |
| `npm install -g @github/copilot` | npm 安裝（需 Node.js 22+） |
| `curl -fsSL https://gh.io/copilot-install \| bash` | 安裝腳本 |
| `copilot --version` | 查看版本 |
| `copilot -h` | 查看說明 |
| `copilot help config` | 設定說明 |
| `copilot help environment` | 環境變數說明 |
| `copilot help logging` | 日誌設定說明 |
| `copilot help permissions` | 權限說明 |

### 啟動與模式

| 指令 | 說明 |
|---|---|
| `copilot` | 啟動互動模式 |
| `copilot -p "prompt"` | 程式化模式（單次執行） |
| `copilot --resume` | 恢復之前的 Session |
| `copilot --continue` | 恢復最近關閉的 Session |
| `copilot --model "model-name"` | 指定模型 |
| `copilot --agent=name` | 指定自訂代理 |
| `Shift+Tab` | 切換計畫模式（互動模式中） |
| `Ctrl+T` | 切換推論可見性 |

### Slash 指令（互動模式中）

| 指令 | 說明 |
|---|---|
| `/login` | 登入 GitHub |
| `/model` | 選擇 AI 模型 |
| `/plan` | 建立實作計畫 |
| `/review` | 審查程式碼變更 |
| `/delegate` | 委派任務至 Copilot Coding Agent |
| `/agent` | 選擇自訂代理 |
| `/mcp` | 管理 MCP Server |
| `/mcp add` | 新增 MCP Server |
| `/context` | 查看上下文使用情況 |
| `/compact` | 手動壓縮對話歷史 |
| `/usage` | 查看使用統計 |
| `/session` | 查看 Session 資訊 |
| `/resume` | 恢復之前的 Session |
| `/clear` | 清除對話歷史 |
| `/new` | 開始新對話 |
| `/add-dir /path` | 新增信任目錄 |
| `/list-dirs` | 列出可存取的目錄 |
| `/cwd /path` | 切換工作目錄 |
| `/cd /path` | 切換工作目錄（同 /cwd） |
| `/reset-allowed-tools` | 重置已核准的工具 |
| `/feedback` | 提供回饋 |
| `/help` | 顯示說明 |
| `?` | 顯示指令列表 |

### 權限控制選項

| 選項 | 說明 |
|---|---|
| `--allow-all-tools` / `--allow-all` / `--yolo` | 允許所有工具（⚠️ 高風險） |
| `--allow-tool 'shell(git)'` | 允許特定 Shell 指令 |
| `--allow-tool 'shell(npm run:*)'` | 允許特定指令模式 |
| `--allow-tool 'write'` | 允許檔案寫入 |
| `--allow-tool 'MCP-Server'` | 允許 MCP Server 所有工具 |
| `--deny-tool 'shell(rm)'` | 禁止特定 Shell 指令 |
| `--deny-tool 'shell(git push)'` | 禁止特定 Git 操作 |
| `--deny-tool 'MCP-Server(tool)'` | 禁止 MCP Server 特定工具 |
| `--allow-all-paths` | 允許所有路徑（⚠️ 高風險） |
| `--allow-all-urls` | 允許所有 URL（⚠️ 高風險） |
| `--allow-url domain` | 允許特定域名 |

### 互動模式快捷操作

| 操作 | 說明 |
|---|---|
| `@path/to/file` | 引用檔案內容 |
| `!command` | 直接執行 Shell 指令 |
| `& prompt` | 委派至 Coding Agent |
| `Esc` | 停止當前操作 |
| `Ctrl+Y` | 檢視/編輯計畫 |

---

## 附錄 C：故障排除指南

### 常見問題與解決方案

| 問題 | 可能原因 | 解決方案 |
|---|---|---|
| `copilot` 指令找不到 | 未安裝或 PATH 未設定 | 重新安裝並確認 PATH |
| 認證失敗 | 未登入或 Token 過期 | 在互動模式中執行 `/login` |
| 連線逾時 | 網路或 Proxy 問題 | 檢查 `HTTPS_PROXY` 設定和防火牆規則 |
| 組織政策阻擋 | Copilot CLI 政策未啟用 | 請組織管理員啟用 Copilot CLI 政策 |
| MCP Server 連線失敗 | 設定檔錯誤或 Server 未啟動 | 檢查 `~/.copilot/mcp-config.json` 和 Server 日誌 |
| Premium Requests 耗盡 | 配額用完 | 切換至較低乘數的模型或等待配額重置 |
| 回應品質差 | Prompt 描述不夠清楚 | 改善 Prompt，使用 `@file` 提供上下文 |
| Session 上下文過大 | 持續長時間對話 | 使用 `/clear` 或 `/new` 重新開始 |
| PowerShell 版本不足 | Windows PowerShell 版本 < 6 | 升級至 PowerShell 7+：`winget install Microsoft.PowerShell` |

### 診斷指令

```bash
# 完整系統診斷
echo "=== 系統診斷 ==="
echo "OS: $(uname -a)"
echo "Copilot CLI: $(copilot --version 2>/dev/null || echo 'Not installed')"
echo ""
echo "Proxy:"
echo "  HTTP_PROXY: $HTTP_PROXY"
echo "  HTTPS_PROXY: $HTTPS_PROXY"
echo "  NO_PROXY: $NO_PROXY"
echo ""
echo "Connectivity:"
for endpoint in github.com api.github.com copilot-proxy.githubusercontent.com; do
  if curl -s --connect-timeout 5 "https://${endpoint}" > /dev/null 2>&1; then
    echo "  ✅ $endpoint"
  else
    echo "  ❌ $endpoint"
  fi
done
echo ""
echo "Config directory:"
ls -la ~/.copilot/ 2>/dev/null || echo "  ~/.copilot/ not found"
```

```powershell
# PowerShell 版系統診斷
Write-Host "=== 系統診斷 ===" -ForegroundColor Cyan
Write-Host "OS: $([System.Environment]::OSVersion.VersionString)"
Write-Host "PowerShell: $($PSVersionTable.PSVersion)"
try {
    Write-Host "Copilot CLI: $(copilot --version 2>$null)"
} catch {
    Write-Host "Copilot CLI: Not installed" -ForegroundColor Red
}

Write-Host "`nProxy:"
Write-Host "  HTTP_PROXY: $env:HTTP_PROXY"
Write-Host "  HTTPS_PROXY: $env:HTTPS_PROXY"

Write-Host "`nConnectivity:"
$endpoints = @("github.com", "api.github.com", "copilot-proxy.githubusercontent.com")
foreach ($endpoint in $endpoints) {
    try {
        $null = Invoke-WebRequest -Uri "https://$endpoint" -TimeoutSec 5 -UseBasicParsing -ErrorAction Stop
        Write-Host "  ✅ $endpoint" -ForegroundColor Green
    } catch {
        Write-Host "  ❌ $endpoint" -ForegroundColor Red
    }
}

Write-Host "`nConfig directory:"
if (Test-Path "$env:USERPROFILE\.copilot") {
    Get-ChildItem "$env:USERPROFILE\.copilot" | Format-Table Name, Length, LastWriteTime
} else {
    Write-Host "  ~/.copilot/ not found" -ForegroundColor Yellow
}
```

---

## 附錄 D：ACP（Agent Client Protocol）

Copilot CLI 支援 ACP 開放標準，讓您在任何支援此協議的第三方工具、IDE 或自動化系統中使用 Copilot CLI 作為 Agent。

更多資訊請參閱 [Copilot CLI ACP server](https://docs.github.com/en/copilot/reference/acp-server)。

---

## 附錄 E：參考資源

- [About GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)
- [Installing GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/install-copilot-cli)
- [Using GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli)
- [Best practices for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)
- [Adding custom instructions for Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/add-custom-instructions)
- [Using hooks with GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-hooks)
- [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/cli-command-reference)
- [GitHub Copilot CLI Repository](https://github.com/github/copilot-cli)
- [Copilot plans and pricing](https://github.com/features/copilot/plans)

---

> **文件維護資訊**
> - **建立日期**：2026-02-14
> - **最後更新**：2026-07-10
> - **負責團隊**：技術架構組
> - **審核週期**：每季度
> - **下次審核日**：2026-10-10
> - **重大變更**：v3.0 — 全面更新為獨立 Copilot CLI（舊版 `gh copilot` 擴充已退役）

