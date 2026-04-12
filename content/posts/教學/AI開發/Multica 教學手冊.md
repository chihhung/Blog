+++
date = '2026-04-12T14:36:36+08:00'
draft = false
title = 'Multica 教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# Multica 教學手冊（企業級實戰版）

> **版本：** v0.1.26（2026-04-12）  
> **適用對象：** 資深工程師、架構師、DevOps 工程師、技術主管  
> **技術棧：** Go Backend + Next.js Frontend + PostgreSQL + Agent Daemon  
> **授權：** Multica Source Available License（非 SaaS/轉售可自由使用）  
> **文件等級：** 企業標準技術白皮書

---

## 目錄

- [第 1 章：Multica 概述](#第-1-章multica-概述)
  - [1.1 什麼是 Multica？](#11-什麼是-multica)
  - [1.2 核心設計理念](#12-核心設計理念)
  - [1.3 與傳統工具的差異比較](#13-與傳統工具的差異比較)
  - [1.4 適用場景](#14-適用場景)
  - [1.5 專案基本資訊](#15-專案基本資訊)
  - [1.6 授權模式說明](#16-授權模式說明)
- [第 2 章：系統架構設計（Enterprise Architecture）](#第-2-章系統架構設計enterprise-architecture)
  - [2.1 整體架構概覽](#21-整體架構概覽)
  - [2.2 技術棧詳解](#22-技術棧詳解)
  - [2.3 元件說明](#23-元件說明)
  - [2.4 企業整合架構](#24-企業整合架構)
  - [2.5 資料流向與通訊模型](#25-資料流向與通訊模型)
- [第 3 章：安裝與部署（Installation & Setup）](#第-3-章安裝與部署installation--setup)
  - [3.1 部署模式選擇](#31-部署模式選擇)
  - [3.2 Self-Hosted 快速部署（推薦）](#32-self-hosted-快速部署推薦)
  - [3.3 Self-Hosted 手動部署（Step-by-Step）](#33-self-hosted-手動部署step-by-step)
  - [3.4 環境變數設定](#34-環境變數設定)
  - [3.5 Production 部署（反向代理）](#35-production-部署反向代理)
  - [3.6 不使用 Docker 的手動部署](#36-不使用-docker-的手動部署)
  - [3.7 停止服務](#37-停止服務)
  - [3.8 切換至 Multica Cloud](#38-切換至-multica-cloud)
- [第 4 章：核心運作機制（Core Workflow）](#第-4-章核心運作機制core-workflow)
  - [4.1 任務生命週期（Issue Lifecycle）](#41-任務生命週期issue-lifecycle)
  - [4.2 Agent 自主執行流程](#42-agent-自主執行流程)
  - [4.3 任務排程與佇列機制](#43-任務排程與佇列機制)
  - [4.4 WebSocket 通訊流程](#44-websocket-通訊流程)
  - [4.5 Execution History 查詢](#45-execution-history-查詢)
- [第 5 章：AI Agent 整合（Claude Code / Codex）](#第-5-章ai-agent-整合claude-code--codex)
  - [5.1 支援的 AI Agent](#51-支援的-ai-agent)
  - [5.2 Agent CLI 安裝](#52-agent-cli-安裝)
  - [5.3 CLI 自動偵測機制](#53-cli-自動偵測機制)
  - [5.4 Agent 建立與設定](#54-agent-建立與設定)
  - [5.5 Prompt 設計策略（Agent 專用）](#55-prompt-設計策略agent-專用)
  - [5.6 多 Agent 協作模式](#56-多-agent-協作模式)
- [第 6 章：開發流程（Development Workflow）](#第-6-章開發流程development-workflow)
  - [6.1 完整開發流程](#61-完整開發流程)
  - [6.2 Issue 管理](#62-issue-管理)
  - [6.3 範例：Spring Boot API 開發流程](#63-範例spring-boot-api-開發流程)
  - [6.4 範例：Vue 前端功能開發流程](#64-範例vue-前端功能開發流程)
  - [6.5 與 Git Flow 整合](#65-與-git-flow-整合)
- [第 7 章：Skill（技能）機制設計](#第-7-章skill技能機制設計)
  - [7.1 Skill 概念](#71-skill-概念)
  - [7.2 Skill 類型](#72-skill-類型)
  - [7.3 Skill 定義與儲存](#73-skill-定義與儲存)
  - [7.4 範例：自動部署 Skill](#74-範例自動部署-skill)
  - [7.5 範例：Code Review Skill](#75-範例code-review-skill)
  - [7.6 範例：DB Migration Skill](#76-範例db-migration-skill)
  - [7.7 建立企業級 Skill Library](#77-建立企業級-skill-library)
- [第 8 章：多工作空間（Workspace）設計](#第-8-章多工作空間workspace設計)
  - [8.1 Workspace 概念](#81-workspace-概念)
  - [8.2 Workspace CLI 管理](#82-workspace-cli-管理)
  - [8.3 團隊隔離策略](#83-團隊隔離策略)
  - [8.4 權限控管（RBAC）](#84-權限控管rbac)
  - [8.5 多 Daemon Profile](#85-多-daemon-profile)
- [第 9 章：系統維運（Operations）](#第-9-章系統維運operations)
  - [9.1 Log 管理](#91-log-管理)
  - [9.2 Agent 狀態監控](#92-agent-狀態監控)
  - [9.3 監控架構](#93-監控架構)
  - [9.4 建議監控指標](#94-建議監控指標)
  - [9.5 錯誤處理與復原](#95-錯誤處理與復原)
  - [9.6 效能優化](#96-效能優化)
- [第 10 章：系統升級與擴展（Upgrade & Scaling）](#第-10-章系統升級與擴展upgrade--scaling)
  - [10.1 Multica 升級策略](#101-multica-升級策略)
  - [10.2 版本管理策略](#102-版本管理策略)
  - [10.3 Agent 水平擴展](#103-agent-水平擴展)
  - [10.4 高可用架構（HA）](#104-高可用架構ha)
  - [10.5 切換至 Multica Cloud](#105-切換至-multica-cloud)
- [第 11 章：安全設計（Security）](#第-11-章安全設計security)
  - [11.1 認證與授權](#111-認證與授權)
  - [11.2 Agent 權限隔離](#112-agent-權限隔離)
  - [11.3 憑證管理](#113-憑證管理)
  - [11.4 網路安全](#114-網路安全)
  - [11.5 SSDLC 整合](#115-ssdlc-整合)
- [第 12 章：最佳實務（Best Practices）](#第-12-章最佳實務best-practices)
  - [12.1 團隊導入策略](#121-團隊導入策略)
  - [12.2 Prompt Engineering 原則](#122-prompt-engineering-原則)
  - [12.3 Agent 使用規範](#123-agent-使用規範)
  - [12.4 常見錯誤與避免方式](#124-常見錯誤與避免方式)
  - [12.5 開發環境最佳實務](#125-開發環境最佳實務)
- [第 13 章：實戰案例（Case Study）](#第-13-章實戰案例case-study)
  - [13.1 案例：建立企業 Web 系統](#131-案例建立企業-web-系統)
  - [13.2 案例總結](#132-案例總結)
- [附錄 A：檢查清單（Checklist）](#附錄-a檢查清單checklist)
- [附錄 B：CLI 快速參考卡](#附錄-bcli-快速參考卡)
- [附錄 C：術語表（Glossary）](#附錄-c術語表glossary)

---

## 第 1 章：Multica 概述

### 1.1 什麼是 Multica？

Multica 是一個**開源的 AI Agent 管理平台**，核心理念是將 AI 編碼代理（如 Claude Code、Codex、OpenClaw、OpenCode）轉化為團隊中的「虛擬同事」。

> **"Your next 10 hires won't be human."** — Multica 官方標語

與傳統的 AI 對話工具不同，Multica 提供完整的**任務管理 + Agent 自主執行**基礎設施：

- Agent 擁有個人檔案，出現在看板上
- Agent 可以被指派 Issue、參與討論、建立任務
- Agent 遇到困難時主動回報 Blocker
- 每個解決方案自動轉化為可重用的「技能（Skill）」

### 1.2 核心設計理念

| 設計原則 | 說明 |
|---------|------|
| **Agent as Teammate** | AI Agent 不是工具，而是團隊成員 |
| **Task-Driven** | 以 Issue 為中心的任務驅動模式（類似 Linear / Jira） |
| **Autonomous Execution** | Agent 自主領取、執行、回報任務 |
| **Skill Compounding** | 技能累積，團隊能力隨時間複利成長 |
| **Vendor-Neutral** | 支援多種 AI Agent（Claude Code / Codex / OpenClaw / OpenCode） |
| **Self-Hosted First** | 可完全自部署，資料不離開企業環境 |

### 1.3 與傳統工具的差異比較

#### 與 AI 工具（Copilot / ChatGPT）差異

| 面向 | Copilot / ChatGPT | Multica |
|------|-------------------|---------|
| 互動模式 | 人類主動提問 → AI 回應 | 指派任務 → Agent 自主完成 |
| 任務管理 | 無 | 完整 Issue Lifecycle（backlog→done） |
| 協作能力 | 單人使用 | 多人 + 多 Agent 協作 |
| 技能累積 | 無（每次從頭開始） | Skill 自動累積與重用 |
| 進度追蹤 | 無 | 即時 WebSocket 進度串流 |
| 部署模式 | SaaS | Self-Hosted / Cloud 可選 |

#### 與任務管理工具（Jira / Linear）差異

| 面向 | Jira / Linear | Multica |
|------|---------------|---------|
| 執行者 | 人類工程師 | 人類 + AI Agent 並行 |
| 自動化 | 規則/Webhook 觸發 | Agent 自主感知並執行 |
| 程式碼生成 | 無 | Agent 直接寫 Code + 提 PR |
| 運行環境 | 無 | 內建 Runtime 管理 |
| 即時通訊 | 評論 | WebSocket 即時串流 |

### 1.4 適用場景

| 場景 | 說明 |
|------|------|
| 企業大型 Web 系統 | Spring Boot / Vue / 微服務架構 |
| 快速原型開發 | Agent 快速產出 MVP |
| 遺留系統重構 | Agent 輔助逐步遷移 |
| DevOps 自動化 | 部署、監控、日常維運任務 |
| 代碼審查 | Agent 自動進行 Code Review |
| 新人 Onboarding | Agent 輔助建立文件與教學 |

### 1.5 專案基本資訊

| 項目 | 資訊 |
|------|------|
| GitHub | [multica-ai/multica](https://github.com/multica-ai/multica) |
| 最新版本 | v0.1.26（27 個 Release） |
| Stars | 8,300+ |
| Forks | 1,100+ |
| 語言組成 | TypeScript 55% / Go 41.5% / MDX 1.3% / Shell 1.0% / CSS 0.8% / 其他 0.4% |
| 貢獻者 | 27+（含 @claude 作為 AI 貢獻者） |
| 授權 | Multica Source Available License |
| 官網 | [multica.ai](https://multica.ai) |
| Cloud 服務 | [multica.ai/app](https://multica.ai/app) |
| 社群 | [X (@multica_hq)](https://x.com/multica_hq) |
| 開源 Issues | 58+ 個 Issue / 64+ 個 Pull Request |

### 1.6 授權模式說明

Multica 採用 **Multica Source Available License**，具體規範如下：

| 使用場景 | 是否允許 |
|---------|---------|
| 企業內部自部署使用 | ✅ 允許 |
| 個人學習與研究 | ✅ 允許 |
| 基於 Multica 進行二次開發 | ✅ 允許 |
| 提供 Multica 作為 SaaS 服務 | ❌ 禁止 |
| 轉售 Multica 或其衍生產品 | ❌ 禁止 |

> **法務建議：** 企業導入前，建議法務團隊審閱完整 [LICENSE](https://github.com/multica-ai/multica/blob/main/LICENSE) 文件，確認商業使用不涉及 SaaS 或轉售行為。
>
> **實務建議：** Multica 適合中大型團隊（5+ 人），且需要有至少一位熟悉 Docker + Go + Node.js 的工程師負責維運。

---

## 第 2 章：系統架構設計（Enterprise Architecture）

### 2.1 整體架構概覽

```mermaid
graph TB
    subgraph "使用者層 (User Layer)"
        DEV[👨‍💻 開發人員]
        PM[📋 專案經理]
        ADMIN[🔧 系統管理員]
    end

    subgraph "前端層 (Frontend Layer)"
        WEB[Next.js 16 Web App<br/>App Router]
    end

    subgraph "後端層 (Backend Layer)"
        API[Go Backend<br/>Chi Router + sqlc]
        WS[WebSocket Server<br/>gorilla/websocket]
        AUTH[認證模組<br/>JWT + Magic Link]
        MIGRATE[Migration Engine<br/>自動遷移]
    end

    subgraph "資料層 (Data Layer)"
        DB[(PostgreSQL 17<br/>+ pgvector)]
        S3[S3 / Local Storage<br/>檔案儲存]
    end

    subgraph "Agent 運行層 (Agent Runtime Layer)"
        DAEMON1[Agent Daemon #1<br/>開發機 A]
        DAEMON2[Agent Daemon #2<br/>開發機 B]
        CLOUD_RT[Cloud Runtime<br/>雲端運行環境]
    end

    subgraph "AI Agent 層"
        CLAUDE[Claude Code]
        CODEX[Codex]
        OPENCLAW[OpenClaw]
        OPENCODE[OpenCode]
    end

    subgraph "外部整合 (External Integration)"
        GITHUB[GitHub / GitLab]
        CICD[CI/CD Pipeline]
        MONITOR[Monitoring System]
    end

    DEV --> WEB
    PM --> WEB
    ADMIN --> WEB

    WEB -->|REST API| API
    WEB -->|Real-time| WS

    API --> AUTH
    API --> DB
    API --> S3
    API --> MIGRATE

    WS -->|任務分派| DAEMON1
    WS -->|任務分派| DAEMON2
    WS -->|任務分派| CLOUD_RT

    DAEMON1 --> CLAUDE
    DAEMON1 --> CODEX
    DAEMON2 --> OPENCLAW
    CLOUD_RT --> OPENCODE

    DAEMON1 -->|Git Push| GITHUB
    GITHUB --> CICD
    API --> MONITOR
```

### 2.2 技術棧詳解

| 層級 | 技術 | 說明 |
|------|------|------|
| **Frontend** | Next.js 16（App Router） | SSR + Client Side，React 生態系 |
| **Backend** | Go（Chi router + sqlc + gorilla/websocket） | 高效能單二進制後端 |
| **Database** | PostgreSQL 17 + pgvector | 關聯式 + 向量搜尋支援 |
| **Agent Runtime** | 本地 Daemon 或雲端 Runtime | 執行 AI Agent CLI |
| **檔案儲存** | S3 / CloudFront / Local Fallback | 上傳附件與資產（支援本地檔案系統回退） |
| **認證** | JWT + Email Magic Link + Google OAuth | 安全認證 |

### 2.3 元件說明

#### 2.3.1 Multica Server（Go Backend）

- **REST API：** 處理所有 CRUD 操作（Issue / Agent / Workspace / Skill）
- **WebSocket Server：** 即時雙向通訊，任務狀態串流
- **sqlc：** 編譯期 SQL Type Safety（非 ORM）
- **Migration Engine：** 資料庫遷移自動執行
- **Health Check：** `GET /health → {"status":"ok"}`

#### 2.3.2 Agent Daemon

Daemon 是在開發者本機執行的背景程序：

1. 啟動時自動偵測已安裝的 AI Agent CLI（`claude`、`codex`、`openclaw`、`opencode`）
2. 向 Server 註冊 Runtime
3. 定期輪詢（預設 3 秒）Server 是否有新任務
4. 收到任務後建立隔離的工作目錄，啟動 Agent CLI 執行
5. 透過 WebSocket 即時回傳執行結果
6. 定期發送心跳（預設 15 秒）
7. 關閉時自動取消註冊所有 Runtime

#### 2.3.3 Web UI Dashboard

- 看板視圖（Board View）：Kanban 式任務管理
- Agent 檔案：每個 Agent 都有個人頁面
- Runtime 管理：查看所有連接的運行環境
- Skill Library：瀏覽與管理可重用技能
- 即時串流：WebSocket 即時顯示 Agent 執行進度

#### 2.3.4 AI Agent 支援

| Agent | CLI Command | 提供商 |
|-------|-------------|--------|
| Claude Code | `claude` | Anthropic |
| Codex | `codex` | OpenAI |
| OpenClaw | `openclaw` | 開源社群 |
| OpenCode | `opencode` | 開源社群 |

### 2.4 企業整合架構

```mermaid
graph LR
    subgraph "Multica Platform"
        MS[Multica Server]
        MD[Multica Daemon]
    end

    subgraph "版本控制"
        GH[GitHub Enterprise]
        GL[GitLab]
    end

    subgraph "CI/CD"
        GA[GitHub Actions]
        JK[Jenkins]
    end

    subgraph "資料庫"
        PG[(PostgreSQL)]
        ORA[(Oracle)]
        DB2[(DB2)]
    end

    subgraph "監控"
        PROM[Prometheus]
        GRAF[Grafana]
        ELK[ELK Stack]
    end

    MS -->|Webhook| GH
    MS -->|Webhook| GL
    GH -->|Trigger| GA
    GL -->|Trigger| JK
    MD -->|Git Push/PR| GH
    MS -->|Metrics| PROM
    PROM --> GRAF
    MS -->|Logs| ELK
    MS --> PG
```

> **實務建議：** 在銀行或金融業環境中，Multica Server 應部署在內部網路，Daemon 執行在開發者本機或專屬 Build Server，所有對外連線需經過企業 Proxy。

### 2.5 資料流向與通訊模型

```mermaid
flowchart LR
    subgraph "同步通訊"
        A[Web UI] -->|REST API / HTTP| B[Go Backend]
        B -->|SQL| C[(PostgreSQL)]
    end

    subgraph "非同步通訊"
        D[Agent Daemon] <-->|WebSocket| E[Go Backend]
        F[Web Browser] <-->|WebSocket| E
    end

    subgraph "檔案儲存"
        B -->|S3 SDK| G[S3 / CloudFront]
        B -->|OS File IO| H[Local Storage]
    end
```

**通訊協議說明：**

| 通訊路徑 | 協議 | 說明 |
|---------|------|------|
| Web UI → Backend | REST（HTTP/HTTPS） | CRUD 操作、認證、檔案上傳 |
| Web UI ↔ Backend | WebSocket（WS/WSS） | 即時任務進度、通知串流 |
| Daemon ↔ Backend | WebSocket（WS/WSS） | 任務分派、執行結果回傳、心跳 |
| Daemon → Git Host | Git Protocol / HTTPS | 程式碼推送、PR 建立 |
| Backend → PostgreSQL | TCP（postgres://） | 資料持久化 |
| Backend → S3 | HTTPS（S3 SDK） | 檔案儲存（Production） |
| Backend → Local FS | File IO | 檔案儲存（本地回退模式） |

> **實務建議：** 企業環境建議所有對外通訊走 TLS 加密。WebSocket 連線在使用反向代理時需特別設定 `Upgrade` 標頭，否則會導致即時功能失效。

---

## 第 3 章：安裝與部署（Installation & Setup）

### 3.1 部署模式選擇

| 模式 | 適用場景 | 複雜度 |
|------|---------|--------|
| **Multica Cloud** | 快速上手、小團隊 | ⭐ |
| **Self-Hosted（Docker）** | 企業環境、資料安全 | ⭐⭐ |
| **Self-Hosted（手動）** | 完全控制、特殊基礎設施 | ⭐⭐⭐ |
| **開發環境** | 貢獻者 / 二次開發 | ⭐⭐⭐ |

### 3.2 Self-Hosted 快速部署（推薦）

#### 前置條件

- Docker 及 Docker Compose
- 至少一個 AI Agent CLI（claude / codex）

#### 一鍵安裝

```bash
# 一鍵安裝：自動 clone repo、啟動 Docker Compose、安裝 CLI
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --local
```

完成後：

- **Frontend：** http://localhost:3000
- **Backend API：** http://localhost:8080
- 登入驗證碼（非 Production）：`888888`

```bash
# 安裝完成後
multica login          # 開啟瀏覽器認證
multica daemon start   # 啟動本地 Agent Runtime
```

### 3.3 Self-Hosted 手動部署（Step-by-Step）

#### Step 1：啟動 Server

```bash
# 1. Clone Repository
git clone https://github.com/multica-ai/multica.git
cd multica

# 2. 使用 make 自動部署（推薦）
make selfhost
# 自動完成：
# - 從 .env.example 建立 .env
# - 產生隨機 JWT_SECRET
# - 啟動 Docker Compose（PostgreSQL + Backend + Frontend）
```

或手動操作：

```bash
# 手動部署
cp .env.example .env

# 修改 .env：至少設定 JWT_SECRET
JWT_SECRET=$(openssl rand -hex 32)
# 將產生的 secret 寫入 .env

# 啟動服務
docker compose -f docker-compose.selfhost.yml up -d
```

#### Step 2：登入系統

1. 開啟 http://localhost:3000
2. 輸入 Email
3. 驗證碼輸入 `888888`（非 Production 環境）

#### Step 3：安裝 CLI 與啟動 Daemon

```bash
# macOS / Linux — Homebrew 安裝
brew tap multica-ai/tap
brew install multica

# 或從源碼編譯
git clone https://github.com/multica-ai/multica.git
cd multica
make build
cp server/bin/multica /usr/local/bin/multica
```

```bash
# 一鍵設定（推薦）
multica setup --local
# 自動完成：
# 1. 設定 CLI 連線至 localhost（8080/3000）
# 2. 開啟瀏覽器認證
# 3. 發現所有工作空間
# 4. 啟動 Daemon

# 自訂埠號（當預設埠號被佔用時）
multica setup --local --port 9090 --frontend-port 4000

# 或手動步驟
multica config local                # 設定連線至本地 Server
multica config local --port 9090 --frontend-port 4000  # 自訂埠號
multica login                       # 認證（開啟瀏覽器）
multica daemon start                # 啟動 Daemon
```

#### Step 4：驗證

```bash
# 檢查 Daemon 狀態
multica daemon status

# JSON 輸出
multica daemon status --output json
```

開啟 Web App → **Settings → Runtimes**，確認看到你的機器。

### 3.4 環境變數設定

#### Server 端必要變數

| 變數 | 說明 | 範例 |
|------|------|------|
| `DATABASE_URL` | PostgreSQL 連線字串 | `postgres://multica:multica@localhost:5432/multica?sslmode=disable` |
| `JWT_SECRET` | JWT 簽署金鑰（**必須更改**） | `openssl rand -hex 32` |
| `FRONTEND_ORIGIN` | 前端 URL（CORS 用） | `https://app.example.com` |
| `PORT` | Backend 埠號 | `8080` |
| `FRONTEND_PORT` | Frontend 埠號 | `3000` |
| `LOG_LEVEL` | 日誌等級 | `debug` / `info` / `warn` / `error` |

#### Email 認證（Production 必要）

| 變數 | 說明 |
|------|------|
| `RESEND_API_KEY` | Resend API 金鑰 |
| `RESEND_FROM_EMAIL` | 寄件者 Email（預設 `noreply@multica.ai`） |

#### Google OAuth（選用）

| 變數 | 說明 |
|------|------|
| `GOOGLE_CLIENT_ID` | Google OAuth Client ID |
| `GOOGLE_CLIENT_SECRET` | Google OAuth Client Secret |
| `GOOGLE_REDIRECT_URI` | OAuth 回呼 URL |

#### 檔案儲存（選用）

| 變數 | 說明 |
|------|------|
| `S3_BUCKET` | S3 Bucket 名稱 |
| `S3_REGION` | AWS Region（預設 `us-west-2`） |
| `CLOUDFRONT_DOMAIN` | CloudFront 域名 |
| `CLOUDFRONT_KEY_PAIR_ID` | CloudFront Key Pair ID |
| `CLOUDFRONT_PRIVATE_KEY` | CloudFront 私鑰（PEM 格式） |
| `COOKIE_DOMAIN` | CloudFront 認證 Cookie 的域名 |

> **注意：** 若未設定 S3 相關變數，Multica 會自動回退使用**本地檔案系統**（Local File Storage Fallback）儲存上傳檔案。此功能適用於開發環境或不需要分散式儲存的場景。

#### Daemon 端設定

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `MULTICA_DAEMON_POLL_INTERVAL` | `3s` | 輪詢間隔 |
| `MULTICA_DAEMON_HEARTBEAT_INTERVAL` | `15s` | 心跳間隔 |
| `MULTICA_AGENT_TIMEOUT` | `2h` | Agent 超時時間 |
| `MULTICA_DAEMON_MAX_CONCURRENT_TASKS` | `20` | 最大併行任務數 |
| `MULTICA_DAEMON_ID` | hostname | Daemon 唯一識別碼 |
| `MULTICA_DAEMON_DEVICE_NAME` | hostname | 裝置顯示名稱 |
| `MULTICA_AGENT_RUNTIME_NAME` | `Local Agent` | Runtime 顯示名稱 |
| `MULTICA_WORKSPACES_ROOT` | `~/multica_workspaces` | 工作空間根目錄 |
| `MULTICA_SERVER_URL` | `ws://localhost:8080/ws` | Daemon → Server WebSocket URL |
| `MULTICA_APP_URL` | `http://localhost:3000` | Frontend URL（CLI 登入用） |
| `MULTICA_CLAUDE_PATH` | 自動偵測 | Claude CLI 路徑 |
| `MULTICA_CLAUDE_MODEL` | 預設 | Claude 模型覆寫 |
| `MULTICA_CODEX_PATH` | 自動偵測 | Codex CLI 路徑 |
| `MULTICA_CODEX_MODEL` | 預設 | Codex 模型覆寫 |

> **注意：** Daemon 端變數也可透過 CLI Flag 設定，例如 `multica daemon start --poll-interval 5s --max-concurrent-tasks 10`。完整 Flag 清單請參考 [CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)。

### 3.5 Production 部署（反向代理）

#### Caddy（推薦）

```caddyfile
app.example.com {
    reverse_proxy localhost:3000
}

api.example.com {
    reverse_proxy localhost:8080
}
```

#### Nginx

```nginx
# Frontend
server {
    listen 443 ssl;
    server_name app.example.com;

    ssl_certificate     /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# Backend API + WebSocket
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate     /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket 支援（關鍵！）
    location /ws {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_read_timeout 86400;
    }
}
```

#### 環境變數設定（分離域名）

```bash
# Backend
FRONTEND_ORIGIN=https://app.example.com
CORS_ALLOWED_ORIGINS=https://app.example.com

# Frontend（Build 時設定）
REMOTE_API_URL=https://api.example.com
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_WS_URL=wss://api.example.com/ws
```

### 3.6 不使用 Docker 的手動部署

**前置條件：** Go 1.26+, Node.js 20+, pnpm 10.28+, PostgreSQL 17 + pgvector

```bash
# 1. 確保 PostgreSQL 已安裝 pgvector 擴充
psql -U postgres -c "CREATE EXTENSION IF NOT EXISTS vector;"

# 2. 編譯後端
make build

# 3. 執行資料庫遷移
DATABASE_URL="postgres://multica:multica@localhost:5432/multica?sslmode=disable" \
  ./server/bin/migrate up

# 4. 啟動後端
DATABASE_URL="postgres://multica:multica@localhost:5432/multica?sslmode=disable" \
  PORT=8080 \
  JWT_SECRET="your-secret-here" \
  ./server/bin/server

# 5. 編譯並啟動前端
pnpm install
pnpm build
cd apps/web
REMOTE_API_URL=http://localhost:8080 pnpm start
```

> **實務建議：** 企業環境強烈建議使用 Docker Compose 部署，以確保環境一致性。將 `.env` 存放在安全的 Secret Manager（如 HashiCorp Vault）中，不要提交至版本控制。

### 3.7 停止服務

#### 使用安裝腳本停止

```bash
# 透過安裝腳本停止所有服務
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --stop
```

#### 使用 Make 停止

```bash
# 停止 Docker Compose 服務（Backend + Frontend + PostgreSQL）
make selfhost-stop

# 停止本地 Daemon
multica daemon stop
```

#### 手動停止

```bash
# 停止 Docker Compose 服務
docker compose -f docker-compose.selfhost.yml down

# 停止 Daemon
multica daemon stop
```

> **注意：** `docker compose down` 僅停止容器，**不會刪除資料庫卷宗**。若需完全清除資料，使用 `docker compose down -v`（此操作不可逆）。

### 3.8 切換至 Multica Cloud

若已在使用 Self-Hosted 部署，希望切換至 [Multica Cloud](https://multica.ai)：

```bash
# 方式一：手動設定
multica config set server_url https://api.multica.ai
multica config set app_url https://multica.ai
multica login

# 方式二：透過安裝腳本（不帶 --local 參數會自動設定 Cloud）
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
```

> **注意：** 切換至 Cloud 後，本地的 Docker 服務不會自動停止。如不再需要，請手動停止，參考 [3.7 停止服務](#37-停止服務)。

---

## 第 4 章：核心運作機制（Core Workflow）

### 4.1 任務生命週期（Issue Lifecycle）

Multica 的任務狀態機定義如下：

```mermaid
stateDiagram-v2
    [*] --> backlog : 建立 Issue
    backlog --> todo : 移入待辦
    todo --> in_progress : Agent 領取 / 人工開始
    in_progress --> in_review : 提交 PR
    in_review --> done : Review 通過
    in_review --> in_progress : 需修改
    in_progress --> blocked : 遇到阻礙
    blocked --> in_progress : 解除阻礙
    in_progress --> cancelled : 取消
    todo --> cancelled : 取消
    backlog --> cancelled : 取消
    done --> [*]
    cancelled --> [*]
```

| 狀態 | 說明 | CLI 指令 |
|------|------|----------|
| `backlog` | 待排序 | `multica issue status <id> backlog` |
| `todo` | 待執行 | `multica issue status <id> todo` |
| `in_progress` | 執行中 | `multica issue status <id> in_progress` |
| `in_review` | 審查中 | `multica issue status <id> in_review` |
| `done` | 已完成 | `multica issue status <id> done` |
| `blocked` | 被阻擋 | `multica issue status <id> blocked` |
| `cancelled` | 已取消 | `multica issue status <id> cancelled` |

### 4.2 Agent 自主執行流程

```mermaid
sequenceDiagram
    participant PM as 專案經理
    participant Web as Multica Web UI
    participant Server as Multica Server
    participant Daemon as Agent Daemon
    participant Agent as AI Agent (Claude Code)
    participant GitHub as GitHub

    PM->>Web: 建立 Issue 並指派給 Agent
    Web->>Server: POST /api/issues (assignee: agent-id)
    Server->>Server: 將任務加入佇列 (enqueue)

    loop 每 3 秒輪詢
        Daemon->>Server: GET /api/tasks/poll
    end

    Server-->>Daemon: 返回任務詳情
    Daemon->>Daemon: 建立隔離工作目錄
    Daemon->>Agent: 啟動 CLI + 傳入任務 Prompt

    loop Agent 執行中
        Agent->>Daemon: 輸出進度（stdout/stderr）
        Daemon->>Server: WebSocket 即時串流
        Server->>Web: 即時更新 UI
    end

    Agent->>Daemon: 執行完成
    Daemon->>GitHub: git push + 建立 PR
    Daemon->>Server: 任務完成 (status: in_review)
    Server->>Web: 更新看板
    Web-->>PM: 通知：PR 已建立
```

### 4.3 任務排程與佇列機制

```mermaid
flowchart LR
    subgraph "任務佇列 (Task Queue)"
        Q1[Priority: Urgent]
        Q2[Priority: High]
        Q3[Priority: Normal]
        Q4[Priority: Low]
    end

    subgraph "Daemon 排程器"
        SCHED[Scheduler<br/>max_concurrent: 20]
    end

    subgraph "Agent Workers"
        W1[Claude Code #1]
        W2[Claude Code #2]
        W3[Codex #1]
    end

    Q1 --> SCHED
    Q2 --> SCHED
    Q3 --> SCHED
    Q4 --> SCHED

    SCHED --> W1
    SCHED --> W2
    SCHED --> W3
```

- **輪詢間隔：** 預設每 3 秒（可配置 `MULTICA_DAEMON_POLL_INTERVAL`）
- **最大併行數：** 預設 20 個任務（可配置 `MULTICA_DAEMON_MAX_CONCURRENT_TASKS`）
- **Priority：** urgent > high > normal > low
- **超時機制：** 預設 2 小時（`MULTICA_AGENT_TIMEOUT`）

### 4.4 WebSocket 通訊流程

```mermaid
sequenceDiagram
    participant Browser as Web Browser
    participant Server as Multica Server
    participant Daemon as Agent Daemon

    Browser->>Server: WS Connect (/ws)
    Server-->>Browser: Connected (Auth via JWT)

    Daemon->>Server: WS Connect (/ws)
    Server-->>Daemon: Connected (Auth via PAT)

    Note over Daemon: Agent 開始執行任務

    Daemon->>Server: message: { type: "progress", content: "正在分析需求..." }
    Server->>Browser: message: { type: "progress", content: "正在分析需求..." }

    Daemon->>Server: message: { type: "tool_call", tool: "file_write", path: "src/api.go" }
    Server->>Browser: message: { type: "tool_call", tool: "file_write" }

    Daemon->>Server: message: { type: "complete", status: "success" }
    Server->>Browser: message: { type: "complete", status: "success" }

    Note over Daemon: 每 15 秒心跳
    loop Heartbeat
        Daemon->>Server: ping
        Server-->>Daemon: pong
    end
```

### 4.5 Execution History 查詢

```bash
# 查看 Issue 的所有執行記錄
multica issue runs <issue-id>
multica issue runs <issue-id> --output json

# 查看特定執行的訊息日誌（工具呼叫、思考過程、錯誤）
multica issue run-messages <task-id>
multica issue run-messages <task-id> --output json

# 增量取得（只取序號 42 之後的訊息）
multica issue run-messages <task-id> --since 42 --output json
```

> **實務建議：** 在企業環境中，建議將 `MULTICA_DAEMON_POLL_INTERVAL` 設為 `5s`（降低 Server 負載），`MULTICA_DAEMON_MAX_CONCURRENT_TASKS` 根據機器資源設定（每個 Agent 約需 2-4GB RAM）。

---

## 第 5 章：AI Agent 整合（Claude Code / Codex）

### 5.1 支援的 AI Agent

Multica 官方支援以下 AI Agent CLI，Daemon 啟動時會自動偵測 PATH 中已安裝的 CLI：

| Agent | CLI | 安裝方式 | 特色 | 支援狀態 |
|-------|-----|---------|------|---------|
| **Claude Code** | `claude` | [官方文件](https://docs.anthropic.com/en/docs/claude-code) | Anthropic 旗艦級 Coding Agent | ✅ 官方支援 |
| **Codex** | `codex` | [GitHub](https://github.com/openai/codex) | OpenAI Coding Agent | ✅ 官方支援 |
| **OpenClaw** | `openclaw` | 開源社群 | 開源替代方案 | 🔄 社群支援 |
| **OpenCode** | `opencode` | 開源社群 | 開源替代方案 | 🔄 社群支援 |

> **注意：** 根據 [CLI and Daemon Guide](https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md)，**Claude Code** 與 **Codex** 是核心支援的 Agent，提供完整的 CLI 路徑覆寫與模型覆寫功能。OpenClaw 與 OpenCode 為相容性支援，由社群維護。至少需安裝其中一個 Agent CLI 才能啟動 Daemon。

### 5.2 Agent CLI 安裝

```bash
# Claude Code
npm install -g @anthropic-ai/claude-code

# 驗證安裝
which claude
claude --version

# Codex
npm install -g @openai/codex

# 驗證安裝
which codex
codex --version
```

### 5.3 CLI 自動偵測機制

Daemon 啟動時自動掃描 PATH 中的 Agent CLI，並為每個偵測到的 Agent 在每個被監控的 Workspace 中註冊 Runtime：

```bash
# 啟動 Daemon（自動偵測）
multica daemon start

# 查看偵測到的 Agent
multica daemon status
# 輸出範例：
# Status:     running
# PID:        12345
# Uptime:     2h30m
# Agents:     claude (v1.5.0), codex (v0.3.0)
# Workspaces: 2 watched

# JSON 格式（適合自動化腳本）
multica daemon status --output json
```

自訂 CLI 路徑（當 Agent 不在 PATH 中時）：

```bash
# 環境變數設定
export MULTICA_CLAUDE_PATH=/opt/tools/claude
export MULTICA_CODEX_PATH=/opt/tools/codex

# 模型覆寫
export MULTICA_CLAUDE_MODEL=claude-sonnet-4-20250514
export MULTICA_CODEX_MODEL=o3-mini

# 也可透過 Daemon Flag 設定
multica daemon start --poll-interval 5s --heartbeat-interval 30s --agent-timeout 4h
```

**Daemon 運作原理：**

1. 啟動時偵測已安裝的 Agent CLI，為每個 Agent 在每個監控中的 Workspace 註冊 Runtime
2. 以設定的間隔（預設 3s）輪詢 Server 是否有已認領（claimed）的任務
3. 收到任務後，建立隔離的工作目錄，啟動 Agent CLI，串流結果回傳
4. 定期發送心跳（預設 15s），讓 Server 知道 Daemon 仍然存活
5. 關閉時自動取消註冊所有 Runtime

### 5.4 Agent 建立與設定

#### Web UI 方式

1. 開啟 **Settings → Agents**
2. 點擊 **New Agent**
3. 選擇 Runtime（你的機器）
4. 選擇 Provider（Claude Code / Codex / OpenClaw / OpenCode）
5. 命名 Agent（將顯示在看板上）

#### CLI 方式

```bash
# 查看現有 Agent
multica agent list
```

### 5.5 Prompt 設計策略（Agent 專用）

為 Agent 設計高品質 Prompt 的原則：

```markdown
## Issue 建立範例（最佳 Prompt 格式）

### 標題
實作使用者登入 API（JWT 認證）

### 描述
#### 目標
實作 POST /api/v1/auth/login 端點，支援 Email + 密碼認證。

#### 技術要求
- 使用 Spring Boot 3.x + Spring Security
- JWT Token 有效期：24 小時
- Refresh Token 有效期：7 天
- 密碼使用 BCrypt 雜湊
- 輸入驗證（Email 格式、密碼長度 8+）

#### 預期交付物
1. LoginController.java
2. AuthService.java
3. JwtTokenProvider.java
4. 單元測試（覆蓋率 > 80%）
5. API 文件更新

#### 限制條件
- 不使用 Session，純 Stateless
- 遵循 Clean Architecture 分層
- 符合 OWASP 安全規範

#### 參考
- 現有程式碼：src/main/java/com/example/auth/
- API 規格：docs/api-spec.yaml
```

### 5.6 多 Agent 協作模式

```mermaid
flowchart TB
    subgraph "Multica Board"
        I1[Issue: 後端 API 開發]
        I2[Issue: 前端頁面開發]
        I3[Issue: 資料庫遷移]
        I4[Issue: Code Review]
    end

    subgraph "Agent Team"
        A1[🤖 Claude-Backend<br/>Claude Code]
        A2[🤖 Vue-Builder<br/>Codex]
        A3[🤖 DB-Admin<br/>Claude Code]
        A4[🤖 Reviewer<br/>Claude Code]
    end

    I1 -->|assign| A1
    I2 -->|assign| A2
    I3 -->|assign| A3
    I4 -->|assign| A4

    A1 -->|完成後| I4
    A2 -->|完成後| I4
    A3 -->|完成後| I1
```

**協作模式建議：**

| 模式 | 說明 | 適用場景 |
|------|------|---------|
| **串行模式** | Agent A 完成後，Agent B 接手 | 有依賴關係的任務 |
| **並行模式** | 多個 Agent 同時執行不同任務 | 獨立功能開發 |
| **Review 模式** | 專門的 Agent 負責 Code Review | 品質控管 |
| **混合模式** | 人類 + Agent 協作 | 複雜架構決策 |

> **實務建議：** 初期建議每個團隊使用 2-3 個 Agent，一個負責後端、一個負責前端、一個負責 Review。隨著 Skill 累積，再逐步增加 Agent 數量。

---

## 第 6 章：開發流程（Development Workflow）

### 6.1 完整開發流程

```mermaid
sequenceDiagram
    participant PM as 專案經理
    participant DEV as 開發人員
    participant Board as Multica Board
    participant Agent as AI Agent
    participant GH as GitHub
    participant CI as CI/CD

    PM->>Board: 建立 Issue<br/>(描述需求 + 驗收條件)
    PM->>Board: 指派給 Agent

    Board->>Agent: 自動分派任務
    Agent->>Agent: 分析需求
    Agent->>Agent: 撰寫程式碼
    Agent->>Agent: 執行測試
    Agent->>GH: git push + 建立 PR
    Agent->>Board: 狀態更新：in_review

    GH->>CI: 觸發 CI Pipeline
    CI->>CI: Build + Test + Scan
    CI-->>GH: 回報結果

    DEV->>GH: Code Review
    DEV->>GH: Approve + Merge
    GH->>CI: 觸發 Deploy
    DEV->>Board: 狀態更新：done
```

### 6.2 Issue 管理

```bash
# 建立 Issue
multica issue create \
  --title "實作使用者登入 API" \
  --description "使用 Spring Security + JWT 實作登入端點..." \
  --priority high \
  --assignee "Claude-Backend"

# 列出 Issue
multica issue list
multica issue list --status in_progress
multica issue list --priority urgent --assignee "Claude-Backend"
multica issue list --limit 20 --output json

# 查看 Issue 詳情
multica issue get <id>

# 更新 Issue
multica issue update <id> --title "新標題" --priority urgent

# 指派 / 取消指派
multica issue assign <id> --to "Claude-Backend"
multica issue assign <id> --unassign

# 變更狀態
multica issue status <id> in_progress

# Issue 評論
multica issue comment list <issue-id>
multica issue comment add <issue-id> --content "需要加入 Rate Limiting"
multica issue comment add <issue-id> --parent <comment-id> --content "收到，已處理"
multica issue comment delete <comment-id>
```

### 6.3 範例：Spring Boot API 開發流程

#### Step 1：建立 Issue

```bash
multica issue create \
  --title "實作 GET /api/v1/users/{id} 端點" \
  --description "$(cat <<'EOF'
## 需求
實作查詢單一使用者的 RESTful API。

## 技術規格
- Framework: Spring Boot 3.x
- Architecture: Clean Architecture
- 驗證: JWT Bearer Token
- Response Format: JSON (UserDTO)

## 驗收條件
1. 回傳正確的 UserDTO（不含密碼欄位）
2. 找不到時回傳 404
3. 未授權時回傳 401
4. 單元測試覆蓋率 > 80%
5. API 文件已更新

## 參考
- Entity: src/main/java/com/example/domain/User.java
- Repository: src/main/java/com/example/repository/UserRepository.java
EOF
)" \
  --priority high \
  --assignee "Claude-Backend"
```

#### Step 2：Agent 自動執行

Agent 收到任務後會自動：

1. Clone / Pull 最新程式碼
2. 分析現有程式碼結構
3. 建立以下檔案：
   - `UserController.java`
   - `GetUserUseCase.java`
   - `UserDTO.java`
   - `UserNotFoundException.java`
   - `UserControllerTest.java`
4. 執行 `mvn test` 驗證
5. 提交 PR

#### Step 3：Review 與合併

```bash
# 查看執行結果
multica issue runs <issue-id>
multica issue run-messages <task-id>
```

### 6.4 範例：Vue 前端功能開發流程

```bash
multica issue create \
  --title "實作使用者個人資料頁面" \
  --description "$(cat <<'EOF'
## 需求
建立使用者個人資料頁面，顯示並編輯個人資訊。

## 技術規格
- Framework: Vue 3 + TypeScript + Composition API
- UI: Tailwind CSS
- State: Pinia
- HTTP: Axios

## 頁面元件
1. UserProfile.vue - 主頁面
2. UserAvatar.vue - 頭像區塊
3. UserInfoForm.vue - 資訊編輯表單

## 路由
- /profile - 個人資料頁
- /profile/edit - 編輯模式

## 驗收條件
1. 元件正確渲染
2. 表單驗證（Email、手機格式）
3. 成功/失敗通知
4. 響應式設計（RWD）
5. 單元測試
EOF
)" \
  --priority normal \
  --assignee "Vue-Builder"
```

### 6.5 與 Git Flow 整合

```mermaid
gitgraph
    commit id: "main"
    branch develop
    checkout develop
    commit id: "dev-base"
    branch feature/user-api
    checkout feature/user-api
    commit id: "Agent: implement user API"
    commit id: "Agent: add tests"
    checkout develop
    merge feature/user-api
    branch feature/user-ui
    checkout feature/user-ui
    commit id: "Agent: implement profile page"
    commit id: "Agent: add RWD support"
    checkout develop
    merge feature/user-ui
    checkout main
    merge develop tag: "v1.0.0"
```

> **實務建議：** 建議使用 Trunk-Based Development 搭配 Feature Flag，Agent 的 PR 直接進入 `main` 分支。如果團隊使用 Git Flow，確保 Agent 知道該從 `develop` 分支建立 Feature Branch。

---

## 第 7 章：Skill（技能）機制設計

### 7.1 Skill 概念

Skill 是 Multica 的核心差異化功能：

- 每次 Agent 成功解決問題，其解法會被封裝為**可重用的 Skill**
- Skill 在整個團隊中共享
- 隨著時間推移，團隊的 Skill Library 不斷壯大
- 新的 Agent 可以直接使用已有的 Skill，無需從頭學習

```mermaid
flowchart LR
    subgraph "Skill 生命週期"
        CREATE[🆕 Agent 解決問題] --> EXTRACT[📦 自動萃取 Skill]
        EXTRACT --> STORE[💾 儲存至 Skill Library]
        STORE --> REUSE[♻️ 其他 Agent 重用]
        REUSE --> IMPROVE[📈 持續優化]
        IMPROVE --> STORE
    end
```

### 7.2 Skill 類型

| 類型 | 說明 | 範例 |
|------|------|------|
| **Code Pattern** | 常見程式碼模式 | CRUD API、DTO 轉換 |
| **Deployment** | 部署流程 | Docker Build、K8s Deploy |
| **Testing** | 測試策略 | 單元測試模板、E2E 測試 |
| **Review** | 審查規則 | Code Style、Security Check |
| **Migration** | 遷移腳本 | DB Schema Migration |
| **Documentation** | 文件生成 | API Doc、README |

### 7.3 Skill 定義與儲存

Multica 使用 `skills-lock.json` 管理 Skill 定義：

```json
{
  "skills": [
    {
      "name": "spring-boot-crud-api",
      "version": "1.0.0",
      "description": "建立 Spring Boot CRUD API（Clean Architecture）",
      "agent": "claude-code",
      "tags": ["spring-boot", "api", "crud"],
      "prompt_template": "...",
      "files_generated": [
        "Controller.java",
        "UseCase.java",
        "Repository.java",
        "DTO.java",
        "Test.java"
      ]
    }
  ]
}
```

### 7.4 範例：自動部署 Skill

```yaml
# Skill: auto-deploy-docker
name: auto-deploy-docker
description: 自動建置 Docker Image 並推送至 Registry
triggers:
  - issue_label: "deploy"
  - branch_pattern: "release/*"
steps:
  1. 檢查 Dockerfile 是否存在
  2. 執行 docker build
  3. 執行安全掃描（Trivy）
  4. 推送至 Container Registry
  5. 更新 K8s Deployment
```

### 7.5 範例：Code Review Skill

```yaml
# Skill: code-review-enterprise
name: code-review-enterprise
description: 企業級 Code Review 檢查
checklist:
  - security: OWASP Top 10 檢查
  - performance: N+1 查詢、記憶體洩漏
  - architecture: Clean Architecture 分層遵循
  - testing: 測試覆蓋率 > 80%
  - naming: 命名規範一致性
  - documentation: Javadoc / JSDoc 完整性
  - error_handling: 例外處理是否完善
```

### 7.6 範例：DB Migration Skill

```yaml
# Skill: db-migration
name: db-migration
description: 資料庫遷移腳本生成與執行
steps:
  1. 分析 Entity 變更
  2. 生成 Flyway/Liquibase Migration 腳本
  3. 本地執行遷移測試
  4. 驗證資料完整性
  5. 生成回滾腳本
```

### 7.7 建立企業級 Skill Library

```mermaid
graph TB
    subgraph "Skill Library 架構"
        subgraph "基礎層 (Foundation)"
            S1[CRUD API Generator]
            S2[DTO Mapper]
            S3[Exception Handler]
        end

        subgraph "業務層 (Business)"
            S4[金融交易 API]
            S5[報表生成器]
            S6[批次處理框架]
        end

        subgraph "維運層 (Operations)"
            S7[Docker Deploy]
            S8[DB Migration]
            S9[Log Analyzer]
        end

        subgraph "品質層 (Quality)"
            S10[Code Review]
            S11[Security Scan]
            S12[Performance Test]
        end
    end

    S1 --> S4
    S2 --> S4
    S3 --> S4
    S7 --> S8
```

> **實務建議：** 初期不要急著建立 Skill Library，讓 Agent 自然累積。經過 2-3 個 Sprint 後，再由資深工程師 Review 並標準化 Skill。定期清理低品質或過時的 Skill。

---

## 第 8 章：多工作空間（Workspace）設計

### 8.1 Workspace 概念

```mermaid
graph TB
    subgraph "企業 Multica 部署"
        subgraph "Workspace: 核心銀行系統"
            A1[Agent: Core-Backend]
            A2[Agent: Core-Frontend]
            I1[Issues & Board]
            SK1[Skill Library]
        end

        subgraph "Workspace: 行動銀行 App"
            A3[Agent: Mobile-API]
            A4[Agent: Mobile-UI]
            I2[Issues & Board]
            SK2[Skill Library]
        end

        subgraph "Workspace: 內部工具平台"
            A5[Agent: Tools-Dev]
            I3[Issues & Board]
            SK3[Skill Library]
        end
    end
```

每個 Workspace 擁有**完全獨立**的：

- Agent 配置
- Issue 看板
- Skill Library
- 設定
- 成員權限

### 8.2 Workspace CLI 管理

```bash
# 列出所有工作空間
multica workspace list
# 有 * 標記的為 Daemon 監控中

# 監控 / 取消監控工作空間
multica workspace watch <workspace-id>
multica workspace unwatch <workspace-id>

# 查看工作空間詳情
multica workspace get <workspace-id>
multica workspace get <workspace-id> --output json

# 列出成員
multica workspace members <workspace-id>
```

### 8.3 團隊隔離策略

| 策略 | 說明 | 適用場景 |
|------|------|---------|
| **按專案隔離** | 每個專案一個 Workspace | 多專案團隊 |
| **按環境隔離** | Dev / Staging / Prod 分開 | 嚴謹的環境管理 |
| **按團隊隔離** | 前端團隊 / 後端團隊分開 | 大型組織 |
| **混合模式** | 專案 + 環境組合 | 企業級部署 |

### 8.4 權限控管（RBAC）

| 角色 | 權限 |
|------|------|
| **Owner** | 完全控制（設定、成員管理、刪除） |
| **Admin** | 管理成員、Agent、設定 |
| **Member** | 建立/管理 Issue、使用 Agent |
| **Viewer** | 只讀（查看 Board 與 Issue） |

### 8.5 多 Daemon Profile

當需要連接多個 Workspace 或多個 Server 時：

```bash
# 建立 staging profile
multica --profile staging login
multica --profile staging daemon start

# 預設 profile 獨立運作
multica daemon start

# 每個 profile 有獨立的：
# ~/.multica/profiles/<name>/config
# ~/.multica/profiles/<name>/daemon.log
# ~/multica_workspaces/<name>/
```

> **實務建議：** 銀行環境建議按「專案 + 環境」建立 Workspace（如 `core-banking-dev`、`core-banking-staging`），並嚴格控管 Production Workspace 的存取權限。

---

## 第 9 章：系統維運（Operations）

### 9.1 Log 管理

#### Daemon Log

```bash
# 查看最近 50 行日誌
multica daemon logs

# 即時跟蹤（tail -f）
multica daemon logs -f

# 查看最近 100 行
multica daemon logs -n 100

# 日誌檔案位置
# ~/.multica/daemon.log
# Profile 模式：~/.multica/profiles/<name>/daemon.log
```

#### Server Log

```bash
# Docker Compose 日誌
docker compose -f docker-compose.selfhost.yml logs -f

# 只看後端日誌
docker compose -f docker-compose.selfhost.yml logs -f backend

# 設定日誌等級（.env）
LOG_LEVEL=debug  # debug, info, warn, error
```

### 9.2 Agent 狀態監控

```bash
# 查看 Daemon 狀態
multica daemon status
# 輸出：
# Status:     running
# PID:        12345
# Uptime:     3d 2h 15m
# Agents:     claude (v1.5.0), codex (v0.3.0)
# Workspaces: 3 watched
# Tasks:      2 running, 0 queued

# JSON 格式（適合自動化監控）
multica daemon status --output json
```

#### Health Check

```bash
# Server Health Check
curl http://localhost:8080/health
# 回傳：{"status":"ok"}

# 適合 Load Balancer 或 Prometheus 監控
```

### 9.3 監控架構

```mermaid
graph LR
    subgraph "Multica"
        SERVER[Go Backend]
        DAEMON[Agent Daemon]
    end

    subgraph "監控系統"
        PROM[Prometheus]
        GRAF[Grafana]
        ALERT[AlertManager]
    end

    subgraph "日誌系統"
        FLUENTD[Fluentd]
        ES[Elasticsearch]
        KIBANA[Kibana]
    end

    SERVER -->|/health + metrics| PROM
    DAEMON -->|daemon.log| FLUENTD
    SERVER -->|application.log| FLUENTD

    PROM --> GRAF
    PROM --> ALERT
    FLUENTD --> ES
    ES --> KIBANA
```

### 9.4 建議監控指標

| 指標 | 說明 | 告警閾值 |
|------|------|---------|
| `daemon_uptime` | Daemon 運行時間 | < 5 分鐘（異常重啟） |
| `task_queue_length` | 佇列中待處理任務 | > 50 |
| `task_execution_time` | 任務執行時間 | > 2 小時 |
| `agent_heartbeat` | Agent 心跳 | 超過 30 秒無心跳 |
| `websocket_connections` | WebSocket 連線數 | 異常斷線 |
| `db_connection_pool` | 資料庫連線池 | > 80% 使用率 |
| `api_response_time` | API 回應時間 | P99 > 2 秒 |

### 9.5 錯誤處理與復原

#### 常見錯誤處理

| 錯誤 | 原因 | 處理方式 |
|------|------|---------|
| Daemon 無法連線 | Server 未啟動 / 網路問題 | 檢查 Server 狀態，確認 URL 設定 |
| Agent 超時 | 任務過大 / Agent 卡住 | 增加 `MULTICA_AGENT_TIMEOUT`，拆分任務 |
| WebSocket 斷線 | 網路不穩 / Proxy 限制 | 檢查 Nginx `proxy_read_timeout` |
| DB 連線失敗 | PostgreSQL 未啟動 | `docker compose up -d postgres` |
| Task 失敗 | Agent CLI 錯誤 | 查看 `multica issue run-messages <task-id>` |

#### 災難復原

```bash
# 停止所有服務（使用 make）
multica daemon stop
make selfhost-stop

# 或手動停止
multica daemon stop
docker compose -f docker-compose.selfhost.yml down

# 備份資料庫
docker compose -f docker-compose.selfhost.yml exec postgres pg_dump -U multica multica > backup.sql

# 重新啟動
make selfhost
multica daemon start

# 或手動重啟
docker compose -f docker-compose.selfhost.yml up -d
multica daemon start

# 還原資料庫（如需要）
cat backup.sql | docker compose -f docker-compose.selfhost.yml exec -T postgres psql -U multica multica
```

> **注意：** `docker compose down` 僅停止容器並移除容器，但保留資料庫卷宗。使用 `docker compose down -v` 會同時刪除卷宗，**此操作不可逆**。

### 9.6 效能優化

| 優化項目 | 建議 |
|---------|------|
| **Daemon 輪詢** | 調整 `MULTICA_DAEMON_POLL_INTERVAL` 為 5-10s（降低 Server 負載） |
| **併行任務數** | 根據 CPU/RAM 調整 `MULTICA_DAEMON_MAX_CONCURRENT_TASKS` |
| **PostgreSQL** | 調整 `max_connections`、`shared_buffers`、`work_mem` |
| **WebSocket** | Nginx 設定 `proxy_read_timeout 86400` |
| **Docker** | 限制容器 CPU/Memory（`deploy.resources.limits`） |

> **實務建議：** 建議每週進行一次 DB 備份，每月進行一次完整的災難復原演練。Agent 日誌建議保留 30 天，超過的自動歸檔至 Object Storage。

---

## 第 10 章：系統升級與擴展（Upgrade & Scaling）

### 10.1 Multica 升級策略

#### CLI 升級

```bash
# 自動升級（偵測安裝方式：Homebrew 或手動）
multica update

# Homebrew 升級
brew upgrade multica
```

#### Server 升級

```bash
# 1. Pull 最新程式碼
cd multica
git pull

# 2. 重建並重啟（推薦，使用 make）
make selfhost

# 或手動重建
docker compose -f docker-compose.selfhost.yml up -d --build

# Migration 是冪等的，重複執行不會有副作用
# Migration 在 Backend 啟動時自動執行
```

### 10.2 版本管理策略

```mermaid
flowchart TD
    A[監控 GitHub Releases] --> B{是否為重大版本？}
    B -->|是| C[在 Staging 環境測試]
    B -->|否| D[直接在 Dev 環境升級]
    C --> E[執行回歸測試]
    D --> E
    E --> F{測試通過？}
    F -->|是| G[排程 Production 升級]
    F -->|否| H[回報 Issue / 等待修復]
    G --> I[執行升級]
    I --> J[驗證 Health Check]
    J --> K[監控 24 小時]
```

### 10.3 Agent 水平擴展

```mermaid
graph TB
    subgraph "Multica Server (單一)"
        SERVER[Go Backend + PostgreSQL]
    end

    subgraph "Agent Daemon 叢集"
        D1[Daemon #1<br/>Dev Machine A<br/>Claude Code x2]
        D2[Daemon #2<br/>Dev Machine B<br/>Codex x2]
        D3[Daemon #3<br/>Build Server<br/>Claude Code x4]
        D4[Daemon #4<br/>Cloud VM<br/>All Agents]
    end

    SERVER <-->|WebSocket| D1
    SERVER <-->|WebSocket| D2
    SERVER <-->|WebSocket| D3
    SERVER <-->|WebSocket| D4
```

**擴展方式：**

1. **增加 Daemon 數量：** 在更多機器上安裝 Daemon
2. **增加 Agent 數量：** 每個 Daemon 可以執行多個 Agent
3. **調整併行數：** 增加 `MULTICA_DAEMON_MAX_CONCURRENT_TASKS`
4. **專屬 Build Server：** 在高規格機器上部署專用 Daemon

### 10.4 高可用架構（HA）

```mermaid
graph TB
    subgraph "Load Balancer"
        LB[Nginx / HAProxy]
    end

    subgraph "Application Layer"
        WEB1[Frontend #1]
        WEB2[Frontend #2]
        API1[Backend #1]
        API2[Backend #2]
    end

    subgraph "Database Layer"
        PG_PRIMARY[(PostgreSQL Primary)]
        PG_REPLICA[(PostgreSQL Replica)]
    end

    subgraph "Agent Layer"
        D1[Daemon #1]
        D2[Daemon #2]
        D3[Daemon #3]
    end

    LB --> WEB1
    LB --> WEB2
    LB --> API1
    LB --> API2

    API1 --> PG_PRIMARY
    API2 --> PG_PRIMARY
    PG_PRIMARY -->|Streaming Replication| PG_REPLICA

    API1 <--> D1
    API1 <--> D2
    API2 <--> D3
```

> **實務建議：** 小團隊（< 10 人）單機部署即可。中型團隊（10-50 人）建議分離前後端和資料庫。大型團隊（50+ 人）才需要考慮完整 HA 架構。

### 10.5 切換至 Multica Cloud

若團隊決定從 Self-Hosted 遷移至 Multica Cloud 託管服務：

```bash
# 重新設定 CLI 指向 Cloud
multica config set server_url https://api.multica.ai
multica config set app_url https://multica.ai
multica login

# 或使用安裝腳本（不帶 --local 會自動設定 Cloud）
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
```

**遷移注意事項：**

| 項目 | 說明 |
|------|------|
| 資料遷移 | Cloud 與 Self-Hosted 的資料不互通，需手動重建 Issue 與 Agent |
| Daemon | 原有 Daemon 繼續監聽 Cloud Server，無需重裝 |
| 本地 Docker | 切換後本地 Docker 服務不會自動關閉，需手動 `make selfhost-stop` |
| Skill Library | 需在 Cloud 環境重新建立 |

> **實務建議：** 建議先在 Cloud 環境中完成基本設定與驗證後，再停止本地 Self-Hosted 服務，以確保無縫切換。

---

## 第 11 章：安全設計（Security）

### 11.1 認證與授權

| 認證方式 | 說明 | 適用場景 |
|---------|------|---------|
| **Email Magic Link** | 透過 Resend 發送驗證碼 | Production（需設定 RESEND_API_KEY） |
| **Google OAuth** | Google 帳號登入 | 支援 Google Workspace 的企業 |
| **Master Code** | 固定驗證碼 `888888` | 僅限非 Production 環境 |
| **JWT Token** | 90 天有效期 | 所有環境 |
| **Personal Access Token** | CLI / Daemon 認證 | Headless 環境 |

#### JWT 安全設定

```bash
# 產生強健的 JWT Secret（必須！）
JWT_SECRET=$(openssl rand -hex 32)

# 切勿使用預設值或簡單字串
# 切勿將 JWT_SECRET 提交至版本控制
```

### 11.2 Agent 權限隔離

```mermaid
flowchart TB
    subgraph "權限模型"
        WS[Workspace 隔離]
        AGENT[Agent 限定 Workspace]
        RUNTIME[Runtime 隔離執行]
        WORKDIR[隔離工作目錄]
    end

    WS --> AGENT
    AGENT --> RUNTIME
    RUNTIME --> WORKDIR
```

**隔離機制：**

1. **Workspace Level：** Agent 只能存取所屬 Workspace 的 Issue 與 Skill
2. **Runtime Level：** 每個任務在隔離的工作目錄中執行
3. **工作目錄：** `~/multica_workspaces/<workspace>/<task>/`
4. **CLI 權限：** Agent CLI 只能在指定目錄中操作

### 11.3 憑證管理

| 項目 | 建議做法 |
|------|---------|
| `JWT_SECRET` | 使用 Secret Manager（HashiCorp Vault / AWS Secrets Manager） |
| `DATABASE_URL` | 不在 `.env` 中存放明文密碼 |
| `RESEND_API_KEY` | 環境變數注入，不提交至 Git |
| `GOOGLE_CLIENT_SECRET` | 存放在 Secret Manager |
| Agent API Keys | 各開發者自行在本機設定 |

```bash
# .gitignore 中必須包含
.env
.env.local
.env.worktree
*.pem
*.key
```

### 11.4 網路安全

```bash
# Production 必須配置
# 1. TLS/SSL（透過反向代理）
# 2. CORS 限制
CORS_ALLOWED_ORIGINS=https://app.example.com

# 3. WebSocket 安全
# Nginx 配置 wss:// 而非 ws://
NEXT_PUBLIC_WS_URL=wss://api.example.com/ws

# 4. Rate Limiting（Nginx 層級）
# 5. Firewall 規則（只開放必要埠號）
```

### 11.5 SSDLC 整合

```mermaid
flowchart LR
    REQ[需求分析] --> DESIGN[安全設計]
    DESIGN --> CODE[安全編碼<br/>Agent + Review]
    CODE --> TEST[安全測試<br/>SAST + DAST]
    TEST --> DEPLOY[安全部署<br/>容器掃描]
    DEPLOY --> MONITOR[安全監控<br/>日誌分析]
    MONITOR --> REQ
```

| SSDLC 階段 | Multica 整合方式 |
|------------|-----------------|
| **需求分析** | Issue 中標注安全需求 |
| **安全設計** | Skill: Security Design Review |
| **安全編碼** | Agent 遵循 OWASP Guidelines |
| **安全測試** | CI/CD 整合 SAST/DAST 工具 |
| **安全部署** | Skill: Container Security Scan |
| **安全監控** | 整合 SIEM / Log 分析 |

> **實務建議：** 金融業環境中，Multica Server 必須部署在 DMZ 內網，所有對外連線經過企業 Proxy。Agent 的 API Key（如 Anthropic API Key）不應在 Server 端存放，而是保留在各開發者本機的 Daemon 設定中。

---

## 第 12 章：最佳實務（Best Practices）

### 12.1 團隊導入策略

```mermaid
flowchart LR
    P1[Phase 1<br/>試點<br/>2-3 人] --> P2[Phase 2<br/>擴展<br/>一個團隊]
    P2 --> P3[Phase 3<br/>全面導入<br/>多團隊]
    P3 --> P4[Phase 4<br/>優化<br/>Skill 標準化]
```

| 階段 | 目標 | 行動 |
|------|------|------|
| **Phase 1（第 1-2 週）** | 熟悉平台 | 安裝、設定、完成 5 個簡單 Issue |
| **Phase 2（第 3-4 週）** | 建立流程 | 一個團隊全面使用，累積 Skill |
| **Phase 3（第 2-3 月）** | 擴展規模 | 多團隊導入，建立規範 |
| **Phase 4（持續）** | 優化效率 | 標準化 Skill Library，效能調優 |

### 12.2 Prompt Engineering 原則

| 原則 | 說明 | 範例 |
|------|------|------|
| **具體明確** | 清楚描述輸入/輸出/限制 | ✅ "實作 POST /api/users，驗證 Email 格式" |
| **上下文充足** | 提供參考檔案與架構資訊 | ✅ "參考 UserRepository.java" |
| **可驗證** | 定義明確的驗收條件 | ✅ "單元測試覆蓋率 > 80%" |
| **適當粒度** | 任務不要太大也不要太小 | ✅ "一個 API 端點 + 測試" |
| **結構化** | 使用 Markdown 格式化 Issue | ✅ 標題/描述/驗收條件/參考 |

**反面範例（避免）：**

```
❌ "幫我寫一個使用者模組"  → 太模糊
❌ "重構整個後端架構"      → 太大
❌ "修個 Bug"             → 無上下文
```

### 12.3 Agent 使用規範

| 規範 | 說明 |
|------|------|
| **命名規範** | Agent 名稱反映職責（如 `Claude-Backend`、`Vue-Builder`） |
| **職責分離** | 不同 Agent 負責不同領域 |
| **Review 必要** | Agent 產出的程式碼必須經過人類 Review |
| **Skill 維護** | 定期 Review 並清理過時的 Skill |
| **安全邊界** | Agent 不可直接存取 Production 資料庫 |
| **成本控管** | 監控 Token 使用量，避免無效重試 |
| **任務粒度** | 保持 Issue 在 1-4 小時可完成的範圍 |

### 12.4 常見錯誤與避免方式

| 錯誤 | 原因 | 解決方式 |
|------|------|---------|
| Agent 產出低品質程式碼 | Prompt 不夠具體 | 完善 Issue 描述與驗收條件 |
| Agent 超時 | 任務太大或太複雜 | 拆分為更小的 Issue |
| Skill 混亂 | 缺乏管理 | 指派 Skill 管理員定期 Review |
| 資料庫效能下降 | pgvector 索引未優化 | 定期 `VACUUM ANALYZE` |
| WebSocket 斷線 | Proxy 配置不當 | 設定 `proxy_read_timeout 86400` |
| Daemon 無法啟動 | Agent CLI 未安裝 | 確認 `claude` / `codex` 在 PATH 中 |
| 認證失敗 | Token 過期 | 重新執行 `multica login` |

### 12.5 開發環境最佳實務

#### 一鍵開發環境

```bash
# 使用 make dev 一鍵啟動開發環境
make dev
# 自動完成：
# - 偵測環境（主目錄或 Worktree）
# - 建立 .env / .env.worktree
# - 檢查前置條件（Node.js、pnpm、Go、Docker）
# - 安裝 JavaScript 依賴
# - 確保共用 PostgreSQL 容器運行中
# - 建立應用程式資料庫（若不存在）
# - 執行所有 Migration
# - 啟動前後端服務
```

#### 開發模式架構

Multica 本地開發使用**共享 PostgreSQL 容器 + 資料庫級隔離**模型：

| 元素 | 主目錄（Main） | Worktree |
|------|---------------|----------|
| Env 檔案 | `.env` | `.env.worktree` |
| 資料庫 | `multica` | `multica_<branch>_<hash>` |
| PostgreSQL Port | `5432`（共用） | `5432`（共用） |
| Backend Port | `8080` | 自動產生 |
| Frontend Port | `3000` | 自動產生 |

```bash
# 功能分支開發（Git Worktree）
git worktree add ../multica-feature -b feat/my-change main
cd ../multica-feature
make dev

# 日常指令
make start-worktree    # 啟動
make stop-worktree     # 停止
make check-worktree    # 驗證
```

#### Make 指令參考

| 指令 | 說明 |
|------|------|
| `make dev` | 一鍵開發環境（自動偵測 Main/Worktree） |
| `make setup` | 設定環境（安裝依賴、建立 DB、Migration） |
| `make start` | 啟動前後端 |
| `make stop` | 停止前後端 |
| `make check` | 驗證（TypeScript typecheck + 單元測試 + Go 測試 + E2E 測試） |
| `make test` | 執行測試 |
| `make build` | 編譯後端二進制 |
| `make migrate-up` | 執行資料庫遷移 |
| `make migrate-down` | 回滾資料庫遷移 |
| `make db-up` | 啟動共用 PostgreSQL 容器 |
| `make db-down` | 停止共用 PostgreSQL 容器（保留卷宗） |
| `make selfhost` | 啟動 Self-Hosted 部署 |
| `make selfhost-stop` | 停止 Self-Hosted 部署 |
| `make daemon` | 啟動本地 Daemon |
| `make worktree-env` | 產生 Worktree 用 .env.worktree 檔案 |
| `make setup-main` | 明確設定主目錄環境 |
| `make start-main` | 啟動主目錄服務 |
| `make stop-main` | 停止主目錄服務 |
| `make check-main` | 驗證主目錄 |
| `make setup-worktree` | 明確設定 Worktree 環境 |
| `make start-worktree` | 啟動 Worktree 服務 |
| `make stop-worktree` | 停止 Worktree 服務 |
| `make check-worktree` | 驗證 Worktree |

#### 重要規則

```bash
# ⚠️ 重要：主目錄使用 .env，Worktree 使用 .env.worktree
# 切勿將 .env 複製到 Worktree 目錄——會意外指向主資料庫

# 提交前驗證
make check-main       # 主目錄
make check-worktree   # Worktree

# 完全清除（⚠️ 慎用，不可逆）
docker compose down -v  # 刪除所有本地 PostgreSQL 資料
```

> **實務建議：** 每個 Sprint 結束後安排 15 分鐘 "Agent Retrospective"，回顧 Agent 的表現、改善 Prompt 品質、更新 Skill Library。

---

## 第 13 章：實戰案例（Case Study）

### 13.1 案例：建立企業 Web 系統

#### 系統概要

- **後端：** Spring Boot 3.x（Clean Architecture）
- **前端：** Vue 3 + TypeScript + Tailwind CSS
- **資料庫：** PostgreSQL 17
- **CI/CD：** GitHub Actions
- **Agent 配置：** 3 個 Agent

#### 架構圖

```mermaid
graph TB
    subgraph "Multica Board"
        B[Issue Board]
    end

    subgraph "Agent Team"
        AB[🤖 Claude-Backend<br/>Spring Boot API]
        AF[🤖 Vue-Builder<br/>Vue 3 Frontend]
        AR[🤖 Code-Reviewer<br/>Code Review]
    end

    subgraph "開發產出"
        API[Spring Boot API<br/>Clean Architecture]
        UI[Vue 3 SPA<br/>Tailwind CSS]
        DB[(PostgreSQL 17)]
        TEST[Unit + E2E Tests]
    end

    subgraph "CI/CD"
        GHA[GitHub Actions]
        DOCKER[Docker Build]
        DEPLOY[Deploy to Staging]
    end

    B -->|指派| AB
    B -->|指派| AF
    B -->|指派| AR

    AB --> API
    AF --> UI
    AB --> TEST
    AF --> TEST

    API --> DB
    API -->|PR| GHA
    UI -->|PR| GHA
    GHA --> DOCKER
    DOCKER --> DEPLOY
```

#### Step 1：設定 Multica 環境

```bash
# 安裝 Multica CLI
brew install multica-ai/tap/multica

# 設定（使用 Self-Hosted）
multica setup --local

# 建立工作空間：enterprise-web-app
# 透過 Web UI: Settings → Workspaces → New
```

#### Step 2：建立 Agent 團隊

在 **Settings → Agents** 中建立：

| Agent 名稱 | Provider | 職責 |
|-----------|----------|------|
| Claude-Backend | Claude Code | 後端 API 開發 |
| Vue-Builder | Codex | 前端頁面開發 |
| Code-Reviewer | Claude Code | 程式碼審查 |

#### Step 3：建立 Issue（後端 API）

```bash
multica issue create \
  --title "實作用戶管理 CRUD API" \
  --description "$(cat <<'EOF'
## 目標
實作用戶管理的 RESTful API。

## 端點
| Method | Path | 描述 |
|--------|------|------|
| POST | /api/v1/users | 建立用戶 |
| GET | /api/v1/users/{id} | 查詢單一用戶 |
| GET | /api/v1/users | 查詢用戶列表（分頁） |
| PUT | /api/v1/users/{id} | 更新用戶 |
| DELETE | /api/v1/users/{id} | 刪除用戶 |

## 技術要求
- Spring Boot 3.x + Clean Architecture
- Spring Security JWT 認證
- Bean Validation
- PostgreSQL + JPA
- Flyway Migration
- Swagger / OpenAPI 文件

## 驗收條件
1. 所有端點正常運作
2. JWT 認證生效
3. 輸入驗證完整
4. 單元測試覆蓋率 > 80%
5. API 文件已生成
6. Flyway Migration 腳本已建立
EOF
)" \
  --priority high \
  --assignee "Claude-Backend"
```

#### Step 4：建立 Issue（前端頁面）

```bash
multica issue create \
  --title "實作用戶管理前端頁面" \
  --description "$(cat <<'EOF'
## 目標
建立用戶管理的前端頁面。

## 頁面
1. 用戶列表頁（/users）：表格 + 搜尋 + 分頁
2. 用戶詳情頁（/users/:id）：檢視用戶資訊
3. 新增用戶表單（/users/new）：建立新用戶
4. 編輯用戶表單（/users/:id/edit）：修改用戶資訊

## 技術要求
- Vue 3 + TypeScript + Composition API
- Tailwind CSS
- Pinia State Management
- Vue Router
- Axios HTTP Client
- Vee-Validate 表單驗證

## 驗收條件
1. 所有頁面正確渲染
2. 表單驗證完整
3. 成功/錯誤通知
4. RWD 支援
5. Loading 狀態
6. 元件測試
EOF
)" \
  --priority high \
  --assignee "Vue-Builder"
```

#### Step 5：建立 Issue（DB Migration）

```bash
multica issue create \
  --title "建立 Users 資料表 Migration" \
  --description "$(cat <<'EOF'
## 目標
建立 PostgreSQL users 資料表的 Flyway Migration。

## Schema
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'USER',
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

## 索引
- email (UNIQUE)
- status
- created_at

## 驗收條件
1. Migration 可成功執行
2. Rollback 腳本可用
3. 測試資料種子（Seed Data）已建立
EOF
)" \
  --priority urgent \
  --assignee "Claude-Backend"
```

#### Step 6：監控 Agent 執行

```bash
# 查看所有 Issue 執行狀態
multica issue list --status in_progress

# 查看特定 Issue 的執行記錄
multica issue runs <issue-id>

# 即時查看 Agent 輸出
multica issue run-messages <task-id>

# 增量查看（只看最新訊息）
multica issue run-messages <task-id> --since 100
```

#### Step 7：Code Review

```bash
# 建立 Review Issue
multica issue create \
  --title "Review: 用戶管理 API PR #42" \
  --description "請 Review PR #42 的程式碼品質、安全性、測試覆蓋率" \
  --priority high \
  --assignee "Code-Reviewer"
```

#### Step 8：CI/CD 整合

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main, develop]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
      - run: mvn clean verify
      - run: mvn jacoco:report

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint
      - run: npm run test
      - run: npm run build
```

### 13.2 案例總結

| 指標 | 結果 |
|------|------|
| 總 Issue 數 | 15 |
| Agent 完成 Issue | 12 |
| 人工完成 Issue | 3 |
| 平均任務完成時間 | 45 分鐘 |
| 首次 PR 通過率 | 73% |
| Skill 產出數 | 8 |
| 預估節省人天 | 5-8 天 |

> **實務建議：** 第一個專案不要期望 Agent 能完成所有工作。將 Agent 定位為「加速器」而非「替代品」。複雜的架構決策、業務邏輯確認仍需人類工程師主導。

---

## 附錄 A：檢查清單（Checklist）

### A.1 初次安裝清單

- [ ] Docker 與 Docker Compose 已安裝
- [ ] 至少一個 AI Agent CLI 已安裝（claude / codex）
- [ ] Multica Server 已啟動（`docker compose up -d`）
- [ ] 可存取 Web UI（http://localhost:3000）
- [ ] Multica CLI 已安裝（`brew install multica-ai/tap/multica`）
- [ ] 已完成認證（`multica login`）
- [ ] Daemon 已啟動（`multica daemon start`）
- [ ] Daemon 狀態正常（`multica daemon status`）
- [ ] Runtime 在 Web UI 中可見（Settings → Runtimes）

### A.2 Production 部署清單

- [ ] `JWT_SECRET` 已更改為強隨機值（`openssl rand -hex 32`）
- [ ] `APP_ENV` 已設定為 `production`（停用 Master Code `888888`）
- [ ] Email 認證已設定（Resend API Key）
- [ ] HTTPS/TLS 已設定（反向代理）
- [ ] CORS 已正確設定（`CORS_ALLOWED_ORIGINS`）
- [ ] WebSocket 代理已設定（`/ws` 路由 + `proxy_read_timeout 86400`）
- [ ] 資料庫備份已設定（定期排程）
- [ ] Log 集中管理已設定
- [ ] Health Check 監控已設定（`/health`）
- [ ] `.env` 不在版本控制中
- [ ] Firewall 規則已設定
- [ ] 檔案儲存已設定（S3 或確認使用 Local Fallback）

### A.3 Agent 配置清單

- [ ] Agent 已在 Web UI 中建立
- [ ] Agent 已指定 Runtime 與 Provider
- [ ] Agent 命名清楚反映職責
- [ ] Agent API Key 已在本機設定（不在 Server 端）
- [ ] Agent 測試任務已完成（建立一個測試 Issue 驗證）

### A.4 日常維運清單

- [ ] Daemon 狀態正常（每日）
- [ ] Server Health Check 正常（持續監控）
- [ ] 佇列無積壓（每日）
- [ ] 無超時或失敗任務（每日）
- [ ] 資料庫備份正常（每週）
- [ ] Multica 版本更新（每月評估）
- [ ] Skill Library Review（每 Sprint）

### A.5 安全檢查清單

- [ ] JWT Secret 為隨機強密碼（32+ bytes）
- [ ] `APP_ENV=production` 已設定（停用 Master Code）
- [ ] 所有通訊走 TLS/SSL
- [ ] Agent 在隔離工作目錄執行
- [ ] 敏感資訊不在 Git 中（`.env`、`.pem`、`.key`）
- [ ] RBAC 權限已正確設定
- [ ] 定期審計 Agent Operation Log
- [ ] Production 環境已關閉 Master Code（`APP_ENV=production`）
- [ ] CORS 僅允許受信任的域名
- [ ] WebSocket 使用 WSS（非 WS）
- [ ] Agent API Key 保留在本機 Daemon，不在 Server 端存放

---

## 附錄 B：CLI 快速參考卡

### 認證與設定

```bash
multica login                            # 瀏覽器認證
multica login --token                    # Token 認證（無頭環境）
multica auth status                      # 檢查認證狀態
multica auth logout                      # 登出
multica config show                      # 顯示設定（路徑、Server URL、App URL）
multica config local                     # 設定連線至本地 Server（預設埠號）
multica config local --port 9090 --frontend-port 4000  # 自訂埠號
multica config set server_url <url>      # 設定 Server URL
multica config set app_url <url>         # 設定 App URL
multica config set workspace_id <id>     # 設定預設 Workspace
multica setup                            # 一鍵設定（Cloud）
multica setup --local                    # 一鍵設定（Self-Hosted）
multica setup --local --port 9090 --frontend-port 4000  # 自訂埠號設定
```

### Daemon 管理

```bash
multica daemon start                     # 啟動 Daemon（背景執行）
multica daemon start --foreground        # 前台啟動（除錯用）
multica daemon start --poll-interval 5s  # 自訂輪詢間隔
multica daemon start --max-concurrent-tasks 10  # 自訂併行數
multica daemon start --agent-timeout 4h  # 自訂超時時間
multica daemon start --heartbeat-interval 30s  # 自訂心跳間隔
multica daemon stop                      # 停止 Daemon
multica daemon status                    # 查看狀態（PID、Agent、Workspace）
multica daemon status --output json      # JSON 格式狀態
multica daemon logs                      # 查看日誌（最近 50 行）
multica daemon logs -f                   # 即時跟蹤日誌
multica daemon logs -n 100               # 最近 100 行
```

### Workspace 管理

```bash
multica workspace list                   # 列出工作空間
multica workspace watch <id>             # 監控工作空間
multica workspace unwatch <id>           # 取消監控
multica workspace get <id>               # 查看詳情
multica workspace members <id>           # 列出成員
```

### Issue 管理

```bash
multica issue list                       # 列出 Issue
multica issue list --status in_progress  # 依狀態篩選
multica issue list --priority high       # 依優先級篩選
multica issue list --assignee "Name"     # 依指派人篩選
multica issue get <id>                   # 查看詳情
multica issue create --title "..." --description "..." --priority high --assignee "Agent"
multica issue update <id> --title "..."  # 更新
multica issue assign <id> --to "Agent"   # 指派
multica issue assign <id> --unassign     # 取消指派
multica issue status <id> in_progress    # 變更狀態
multica issue runs <id>                  # 執行記錄
multica issue run-messages <task-id>     # 執行訊息
```

### 其他

```bash
multica version                          # 版本資訊（含 commit hash）
multica version --output json            # JSON 格式版本資訊
multica update                           # 更新 CLI（自動偵測 Homebrew 或手動安裝）
multica agent list                       # 列出 Agent
multica --profile staging login          # 使用 Profile
multica --profile staging daemon start   # 以 Profile 啟動 Daemon
```

### 輸出格式

大多數指令支援 `--output` 參數：

```bash
multica issue list --output json         # JSON 格式（適合腳本自動化）
multica issue list --output table        # 表格格式（預設）
multica daemon status --output json      # JSON 格式狀態
multica workspace get <id> --output json # JSON 格式 Workspace 詳情
```

---

## 附錄 C：術語表（Glossary）

| 術語 | 英文 | 定義 |
|------|------|------|
| Agent | Agent | AI 編碼代理，能夠自主執行程式開發任務的 AI 實體。在 Multica 中，Agent 具有個人檔案、出現在看板上、可被指派任務。 |
| Daemon | Daemon | 在本地機器上執行的背景程序，負責偵測 Agent CLI、註冊 Runtime、輪詢並執行任務。 |
| Runtime | Runtime | 可執行 Agent 任務的計算環境。可以是本地機器（透過 Daemon）或雲端實例。每個 Runtime 回報可用的 Agent CLI。 |
| Workspace | Workspace | 工作空間，Multica 中的頂層組織單位。每個 Workspace 擁有獨立的 Agent、Issue、Skill 與設定。 |
| Issue | Issue | 任務單位，類似 Jira/Linear 的工單。包含標題、描述、優先級、指派人、狀態等屬性。 |
| Skill | Skill | 可重用的解決方案模板。Agent 成功解決問題後，其解法可被封裝為 Skill，供其他 Agent 重用。 |
| Board | Board | 看板視圖，以 Kanban 形式展示 Workspace 中的所有 Issue 與 Agent 狀態。 |
| Blocker | Blocker | 阻擋器，當 Agent 在執行任務中遇到無法自行解決的問題時，會主動回報 Blocker。 |
| Magic Link | Magic Link | 基於 Email 的無密碼認證方式，透過發送驗證碼至 Email 完成身份驗證。 |
| PAT | Personal Access Token | 個人存取令牌，用於 CLI/Daemon 在無頭環境中的認證。有效期 90 天。 |
| Profile | Profile | CLI 設定檔，支援在同一台機器上連接多個 Server 或 Workspace，每個 Profile 擁有獨立的設定、Daemon 狀態與工作目錄。 |
| pgvector | pgvector | PostgreSQL 的向量搜尋擴充，用於 Skill 的語義搜尋與相似度匹配。 |
| sqlc | sqlc | Go 的編譯期 SQL 工具，將 SQL 查詢轉換為型別安全的 Go 程式碼（非 ORM）。 |
| Worktree | Git Worktree | Git 的工作樹功能，允許在同一個 Repository 中同時開啟多個分支的工作目錄。Multica 開發環境完整支援此功能。 |
| Self-Hosted | Self-Hosted | 自部署模式，將 Multica Server 部署在企業自有的基礎設施上，資料完全不離開企業環境。 |
| Multica Cloud | Multica Cloud | Multica 官方提供的託管服務，免除自部署的維運負擔。訪問 [multica.ai/app](https://multica.ai/app)。 |

---

## 參考資源

| 資源 | 連結 |
|------|------|
| GitHub Repository | https://github.com/multica-ai/multica |
| 官方網站 | https://multica.ai |
| Multica Cloud | https://multica.ai/app |
| Self-Hosting Guide | https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md |
| Advanced Configuration | https://github.com/multica-ai/multica/blob/main/SELF_HOSTING_ADVANCED.md |
| AI Agent Setup Guide | https://github.com/multica-ai/multica/blob/main/SELF_HOSTING_AI.md |
| CLI & Daemon Guide | https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md |
| CLI Installation | https://github.com/multica-ai/multica/blob/main/CLI_INSTALL.md |
| Contributing Guide | https://github.com/multica-ai/multica/blob/main/CONTRIBUTING.md |
| Claude Code 文件 | https://docs.anthropic.com/en/docs/claude-code |
| Codex GitHub | https://github.com/openai/codex |
| X (Twitter) | https://x.com/multica_hq |

---

> **文件維護：** 本手冊基於 Multica v0.1.26 撰寫。建議每次 Multica 重大版本更新後，重新 Review 並更新相關章節。  
> **最後更新：** 2026-04-12

