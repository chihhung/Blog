+++
date = '2026-05-29T10:00:00+08:00'
draft = false
title = 'Copilot CLI教學手冊'
tags = ['教學', 'AI開發', 'copilot-cli']
categories = ['教學']
+++

# GitHub Copilot CLI 教學手冊

> **版本**：基於 GitHub Copilot CLI **v1.0.80**（2026-08-14 發佈）  
> **GA 日期**：2026-02-25（v0.0.418 起正式 GA，2026-03-06 起主版號躍升至 1.0）  
> **適用對象**：資深工程師 / DevOps 工程師 / 架構師  
> **技術環境**：企業級 Web Application（Spring Boot 3.x / Vue 3 / 微服務架構）  
> **適用方案**：Copilot Free / Pro / Pro+ / Business / Enterprise（2026-06-01 起全面轉為 **Usage-based Billing / AI Credits** 計費，詳見第 9.4 節）  
> **最後更新**：2026-08-14

---

## 目錄

- [第 1 章：Copilot CLI 概述](#第-1-章copilot-cli-概述)
  - [1.1 什麼是 GitHub Copilot CLI](#11-什麼是-github-copilot-cli)
  - [1.2 與其他 AI 工具的差異比較](#12-與其他-ai-工具的差異比較)
    - [1.2.1 與 IDE Copilot 的互補關係](#121-與-ide-copilot-的互補關係)
    - [1.2.2 與同類 Agentic CLI 競品比較](#122-與同類-agentic-cli-競品比較)
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
  - [4.11 ACP（Agent Client Protocol）與 Copilot SDK](#411-acpagent-client-protocol與-copilot-sdk)
  - [4.12 OpenTelemetry 可觀測性](#412-opentelemetry-可觀測性)
  - [4.13 Rubber Duck 建設性批評代理](#413-rubber-duck-建設性批評代理)
  - [4.14 Remote Control 遠端控制](#414-remote-control-遠端控制)
  - [4.15 自訂模型供應商（Custom Model Provider）](#415-自訂模型供應商custom-model-provider)
  - [4.16 圖片、附件與語音輸入支援](#416-圖片附件與語音輸入支援)
  - [4.17 內建 Agent 系統](#417-內建-agent-系統)
  - [4.18 Sandbox 安全沙箱（本機／雲端）](#418-sandbox-安全沙箱本機雲端)
- [第 5 章：進階使用技巧（企業級）](#第-5-章進階使用技巧企業級)
  - [5.1 Prompt Engineering（CLI 版本）](#51-prompt-engineeringcli-版本)
  - [5.2 Context Engineering（讓 AI 更準）](#52-context-engineering讓-ai-更準)
  - [5.3 多步驟任務拆解（Task Chaining）](#53-多步驟任務拆解task-chaining)
  - [5.4 與其他工具整合](#54-與其他工具整合)
  - [5.5 Session 管理與對話引導](#55-session-管理與對話引導)
  - [5.6 多儲存庫工作流程](#56-多儲存庫工作流程)
  - [5.7 圖片驅動開發](#57-圖片驅動開發)
- [第 6 章：安全與治理](#第-6-章安全與治理)
  - [6.1 工具審批機制](#61-工具審批機制)
  - [6.2 YOLO Mode 說明與風險](#62-yolo-mode-說明與風險)
  - [6.3 企業治理策略](#63-企業治理策略)
    - [6.3.1 已知落差與業界安全研究（2026 年最新）](#631-已知落差與業界安全研究2026-年最新)
  - [6.4 Hooks 安全防護](#64-hooks-安全防護)
- [第 7 章：實戰案例](#第-7-章實戰案例)
- [第 8 章：最佳實務（Best Practices）](#第-8-章最佳實務best-practices)
  - [8.1 如何寫好 Prompt（CLI 版本）](#81-如何寫好-promptcli-版本)
  - [8.2 人機協作（Human-in-the-Loop）](#82-人機協作human-in-the-loop)
  - [8.3 適合與不適合使用的場景](#83-適合與不適合使用的場景)
  - [8.4 官方推薦工作流程（Explore → Plan → Review → Implement → Verify → Commit）](#84-官方推薦工作流程explore--plan--review--implement--verify--commit)
  - [8.5 Session 管理最佳實務](#85-session-管理最佳實務)
  - [8.6 權限管理最佳實務](#86-權限管理最佳實務)
  - [8.7 團隊協作與生產力量測](#87-團隊協作與生產力量測)
- [第 9 章：維運與升級](#第-9-章維運與升級)
  - [9.1 如何更新 Copilot CLI](#91-如何更新-copilot-cli)
  - [9.2 版本管理策略](#92-版本管理策略)
  - [9.3 常見問題（FAQ）](#93-常見問題faq)
  - [9.4 效能與成本考量](#94-效能與成本考量)
  - [9.5 自動更新與發佈頻道](#95-自動更新與發佈頻道)
- [第 10 章：附錄](#第-10-章附錄)
  - [10.1 常用指令速查表](#101-常用指令速查表)
  - [10.2 Prompt 範本合集](#102-prompt-範本合集)
  - [10.3 工具權限速查表](#103-工具權限速查表)
  - [10.4 環境變數](#104-環境變數)
  - [10.5 設定檔位置](#105-設定檔位置)
  - [10.6 版本演進里程碑](#106-版本演進里程碑)
  - [10.7 已移除與棄用項目](#107-已移除與棄用項目)
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
- **ACP 協定**：透過 Agent Client Protocol（ACP）標準開放介面，與第三方工具、IDE 或自動化系統整合（Public Preview）
- **OpenTelemetry 可觀測性**：原生支援 OTEL，追蹤 Agent Session、LLM 呼叫、工具執行的效能指標
- **Remote Control**：透過 `/remote` 遠端控制 CLI Session，支援跨裝置協作（已 GA）
- **自動模型選擇**：選擇 `auto` 模型讓 Copilot 自動選擇最佳可用模型（v1.0.32+）
- **位置記憶權限**：工具權限按目錄記憶，跨 Session 持久化（v1.0.37+）
- **Local / Cloud Sandbox**：`/sandbox enable` 本機沙箱隔離檔案系統與網路存取；`copilot --cloud` 於獨立雲端環境執行（皆為 Public Preview）
- **Rubber Duck 批評代理**：內建的「建設性批評者」代理，刻意使用與主 Session **不同的模型**進行交叉審查，降低共同盲點風險（已 GA，取代舊稱「Critic Agent」）
- **Infinite Sessions**：自動壓縮（Compaction）管理 Context，理論上無上限的長任務 Session，並支援 Session 側欄多工作階段管理
- **Copilot SDK**：六種語言（TypeScript/Python/Go/.NET/Rust/Java）皆已 GA，暴露與 CLI 相同的 Agent Runtime 供程式化整合
- **語音輸入**：本地端運作的語音轉文字輸入，錄音不上傳雲端（已 GA）
- **Prompt Scheduling**：`/every`、`/after` 可定期或延遲執行指定 Prompt

> ⚠️ **注意**：舊版的 GitHub CLI Copilot Extension（`gh copilot`）已正式退役，已由全新的 GitHub Copilot CLI（`copilot` 指令）取代。Copilot CLI 於 **2026-02-25 正式 GA**（v0.0.418），2026-03-06 起主版號躍升至 1.0，目前最新版本為 **v1.0.80**（2026-08-14），仍以近乎每週一版的節奏持續發佈。

### 核心定位

```
GitHub Copilot CLI = AI Agent + Terminal + GitHub 深度整合 + 多代理協作 + 擴充生態系 + ACP 開放標準 + Sandbox 安全隔離 + Copilot SDK 程式化引擎
```

> 📝 **關於 Agent HQ / Mission Control**：GitHub 自 2025-10 起推動「Agent HQ」策略，目標是讓 Copilot、Claude、Codex 等多家代理程式能在 GitHub.com、VS Code、手機、CLI 等同一介面下被「Mission Control」統一指派、監控與治理。這是 Copilot CLI 在市場上與其他純代理型競品最大的差異化定位——它不只是一個 Agent，更希望成為代理協作的控制樞紐。

### 支援模型一覽

> ⚠️ **模型版號更新極快**：GitHub Copilot 支援的模型清單幾乎每週都有異動（新增/棄用），以下為 **截至 2026-08-14 查證** 的快照，正式導入前請務必以 `/model` 指令查看當下清單為準，不建議在企業文件中寫死特定模型版號。

| 模型 | 類型 | 說明 | 適用場景 |
|------|------|------|----------|
| Claude Opus 4.5 | Anthropic | 官方最佳實務文件標示的建議預設，最強推理能力之一 | 複雜架構設計、困難除錯、深層重構 |
| Claude Sonnet 4.5 / 4.6 / **5** | Anthropic | 快速且高效；Sonnet 5 為 v1.0.67（2026-06-30）新增 | 日常編碼、例行任務 |
| Claude Opus 4.6 / 4.7 / 4.8 / **Opus 5** | Anthropic | 依序於各版本新增，Opus 4.8 於 v1.0.55（2026-05-28）上線、Opus 5 於 v1.0.75（2026-07-24）上線 | 最複雜的推理任務 |
| Claude Opus 4.8 Fast | Anthropic | 快速推理，v1.0.66 新增，**已取代並棄用 Opus 4.6 Fast** | 快速迭代 |
| Claude Haiku 4.5 | Anthropic | 輕量快速 | 簡單查詢 |
| **Claude Fable 5** | Anthropic | v1.0.61（2026-06-09）新增 | 一般開發工作 |
| GPT-5.2 Codex / GPT-5.3-Codex | OpenAI | 程式碼生成與審查專用 | 高量程式碼產出、交叉審查 |
| GPT-5.4 / GPT-5.4-Mini / GPT-5.5 / **GPT-5.6** | OpenAI | GPT-5.6 於 v1.0.70（2026-07-09）新增；一般用途子代理預設優先採用 GPT-5.4/5.5（若可用） | 進階分析、簡單任務（Mini） |
| Gemini 3 Pro / 3.5 Flash / **3.6 Flash** | Google | 3.6 Flash 於 v1.0.74（2026-07-23）新增 | 通用開發 |
| Grok 4.5 | xAI | v1.0.76（2026-07-29）新增 | 通用開發 |
| Kimi K2.7 Code / **Kimi K3** | Moonshot | K3 於 v1.0.79（2026-08-10）新增 | 程式碼生成 |
| **auto** | 自動選擇 | 降低速率限制、更低延遲與錯誤，且會依任務複雜度智慧選模 | **推薦**：系統自動最佳化 |
| 自訂模型（BYOK） | 自備 | 組織/企業自配模型供應商（OpenAI 相容 / Azure OpenAI / Anthropic） | 合規需求、私有部署 |

> 📝 **已棄用/移除的模型**（詳見 [10.7 已移除與棄用項目](#107-已移除與棄用項目)）：`gpt-5.1-codex` 系列（v1.0.15 移除）、`gemini-3-pro-preview`（v1.0.13 移除）、Claude Opus 4.6 Fast（v1.0.66 起以 Opus 4.8 Fast 取代）。
>
> 💡 **模型選擇建議**（根據[官方最佳實務](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices#select-your-preferred-model)逐字整理）：
> - **Auto**：「智慧選擇模型，基於即時系統健康狀態與模型效能，降低速率限制並提供更低延遲」（Reduced rate limiting and lower latency and errors）
> - **Opus 4.5**：「適合需要深度推理、複雜系統設計、細微 Bug 調查、大量上下文理解的任務」，官方文件標示為 Most capable but more costly
> - **Sonnet 4.5**：「適合速度與成本效率優先的例行任務，能有效處理大多數日常編碼工作」
> - **GPT-5.2 Codex**：「適合高量程式碼生成，也可作為其他模型產出的交叉審查工具」
> - v1.0.79 起，`/model` 選單改為分組顯示（Recent / Recommended / New），並改為 **Session-scoped**（僅影響當前 Session），需用 `/config model` 才能設定未來 Session 的預設模型
> - 使用 `/model plan`（或 `/model --plan`，v1.0.74+）可為 Plan Mode 單獨指定模型
> - 若組織或企業已配置自訂模型供應商（API Key），這些模型會出現在 `/model` 清單底部
> - Free / Student 方案（Token 制計費）僅能使用 `auto` 模型

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

### 1.2.2 與同類 Agentic CLI 競品比較

Copilot CLI 並非市場上唯一的終端原生 AI Agent，企業選型時常與 Claude Code、OpenAI Codex CLI、Gemini CLI 等工具並列評估。以下整理業界近期（2026 年上半年）評測普遍認同的差異點：

| 比較面向 | GitHub Copilot CLI | Claude Code | Gemini CLI |
|---------|---------------------|--------------|-------------|
| **生態整合定位** | 主打 **Agent HQ / Mission Control**：可統一管理多家代理程式（含 Claude、Codex）於 GitHub 介面 | 深度子代理編排（Sub-agent Orchestration）與工具鏈迭代能力強 | 免費可用門檻最低（任何 Google 帳號即可） |
| **多模型選擇** | 廣（Claude / GPT / Gemini / Grok / Kimi 等皆可選） | 以 Anthropic 模型為核心 | 以 Gemini 模型為核心 |
| **複雜多檔案重構** | 業界評測顯示涉及 10+ 檔案、具架構影響的變更時，錯誤率略高於對手 | 多篇評測（如 SWE-bench Verified）中領先，被視為深度推理標竿 | 中等 |
| **上手門檻/定價** | Pro 方案 $10/月即涵蓋自動完成、聊天、CLI（性價比常被列為優勢） | 需付費訂閱 | 免費層可用 |
| **企業治理與稽核** | 原生整合 GitHub Enterprise 的 Agent Control Plane（可視性、稽核、政策） | 依賴自建/第三方治理工具 | 依賴 Google Workspace 生態 |

> 📝 **市場地位參考**：Gartner 於 2026-05 首次發布《Enterprise AI Coding Agents Magic Quadrant》，GitHub 連續第三年被評為 Leader（Ability to Execute 項目最高），OpenAI Codex、Cursor 同列 Leader 象限。GitHub Copilot 服務組織數已達約 14 萬（年增近 3 倍）。企業選型時建議勿僅憑單一評測結論定案，應以自身程式庫規模、既有 GitHub 依賴程度、跨模型彈性需求作實測評估。

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

> 📝 **登入流程變更**（v1.0.77+）：本地互動式終端機（含無 TTY 情境，如 IDE 整合）預設改用**瀏覽器 OAuth 登入流程**；遠端/無頭（headless）環境仍預設使用 Device Code Flow（RFC 8628）。可用旗標強制指定：`copilot login --web-flow`（強制瀏覽器）或 `copilot login --device-code`（強制裝置碼），亦可加上 `--host <HOST>` 指定 GitHub Enterprise Server 主機。

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
>
> ✅ **GitHub Actions 免 PAT（v1.0.68+ / 2026-07-02 起）**：在 GitHub Actions 中執行 Copilot CLI **不再需要簽發長效 PAT**，改用內建的 `GITHUB_TOKEN`，只需在 workflow 中授予 `permissions: copilot-requests: write` 即可。此舉消除了長效 PAT 外洩風險，且 AI Credit 費用會直接歸屬組織帳單而非個人 Token 持有者，是企業 CI/CD 導入時應優先採用的作法（詳見 [10.7 已移除與棄用項目](#107-已移除與棄用項目)前的建議）。

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
| `multiple Copilot licenses detected` | 偵測到多個授權 | 參閱錯誤訊息中的直接連結解決（v1.0.36+） |
| `session rate limit` | Session 級速率限制 | 等待限制解除；使用 `/compact` 減少 Token 消耗（v1.0.34+） |
| `remote sessions blocked by policy` | 組織禁用遠端 Session | 聯繫組織管理員調整政策（v1.0.22+） |
| `sandbox policy denies this path` | 企業 Sandbox 政策鎖定了受限路徑 | 用 `/sandbox policy` 檢視有效政策；聯繫管理員調整，企業層級政策僅能收緊、不能放寬 |
| `AI credit limit reached` | 個人或組織 AI Credits 額度已用盡（2026-06 起計費模式變更） | 檢查 `/usage`；聯繫管理員調整組織 Credit 池，或等待下期額度重置 |
| managed settings 抓取失敗但仍可啟動 | v1.0.78+ 行為變更：抓取失敗改為 fail open | 確認網路可連線至企業設定端點；若需嚴格 fail closed，需另行設定 |

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

支援的指令檔類型（依探索優先順序）：

| 檔案類型 | 位置 | 作用範圍 |
|---------|------|---------|
| `copilot-instructions.md` | `~/.copilot/` | 全域（所有 Session） |
| `copilot-instructions.md` | `.github/` | 整個 Repository |
| `*.instructions.md` | `.github/instructions/**/` | 依 Path 匹配（模組化） |
| `AGENTS.md` | Git Root 或工作目錄 | Agent 行為定義 |
| `Copilot.md` | Repository 根目錄 | Repository 層級指令 |
| `GEMINI.md` | Repository 根目錄 | 相容格式（自動讀取） |
| `CODEX.md` | Repository 根目錄 | 相容格式（自動讀取） |

> 📝 **注意**：所有自訂指令檔會**合併使用**，而非基於優先順序覆蓋。Repository 指令始終優先於全域指令。指令應保持簡潔且可操作——過長的指令會稀釋效果。

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
| `postToolUse` | 工具執行**後**（成功時） | 記錄日誌、觸發通知 |
| `postToolUseFailure` | 工具執行**失敗時** | 錯誤記錄、告警通知（v1.0.15+） |
| `sessionStart` | Session 啟動時 | 注入額外 Context、環境檢查 |
| `sessionEnd` | Session 結束時 | 清理資源、發送摘要通知（v1.0.22+） |
| `preCompact` | Context 壓縮**前** | 儲存重要資訊 |
| `subagentStart` | 子代理啟動時 | 為子代理注入額外 Context |
| `agentStop` / `subagentStop` | Agent 完成時 | 清理資源、發送通知 |
| `notification` | Shell 完成、權限提示、Elicitation 對話框、Agent 完成 | 非同步通知（v1.0.18+） |
| `PermissionRequest` | 工具權限請求前 | 程式化批准或拒絕工具權限（v1.0.16+） |

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
> - `preToolUse` Hook 可以 **拒絕工具執行**（deny）或 **修改參數**（modifiedArgs/updatedInput）
> - Hook 支援 `ask` 權限決策，在工具執行前要求使用者確認
> - `postToolUse` 僅在工具成功時觸發；失敗時觸發 `postToolUseFailure`（v1.0.15+）
> - Hook 支援 **HTTP 模式**：可將 JSON Payload POST 至配置的 URL，而非執行本地命令（v1.0.35+）
> - Repository 層級的 Hook 僅在檔案夾信任確認後才會載入
> - Hook 設定相容 VS Code、Claude Code 和 CLI 三個平台，支援 PascalCase 和 camelCase 事件名稱
> - `sessionStart` 和 `sessionEnd` 在互動模式中每個 Session 只觸發一次（v1.0.22+）
> - Plugin Hook 接收 `PLUGIN_ROOT`、`COPILOT_PLUGIN_ROOT` 和 `CLAUDE_PLUGIN_ROOT` 環境變數（v1.0.26+）

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

Plugin 是 Copilot CLI **最高層級的擴充封裝單位**：官方定義為「A distributable package that extends Copilot's functionality」「A bundle of components in a single installable unit」。一個 Plugin 內部可以打包 MCP Server、LSP Server、自訂 Agent、**Skill**、Hook、甚至 Extension，形成可分享的完整功能模組。

> 📝 **與 Skill 的關係澄清**：Plugin 與 Skill **不是互相替代的兩種機制**，而是**包含關係**——Skill（見 [4.7](#47-skills-技能系統)）是 Plugin 可以攜帶的組成元件之一。若只需分享單一專門任務指令集，建立 Skill 即可；若要打包一整套跨團隊/跨專案的工具鏈（MCP + Agent + Skill + Hook 一次到位），才需要封裝成 Plugin。

### Plugin 管理指令

```bash
# 開啟 Plugin Marketplace
/plugin marketplace add

# Marketplace 子指令（v1.0.71+）
/plugin marketplace list
/plugin marketplace add <url>
/plugin marketplace remove <name>

# 從 GitHub Repo 安裝
/plugin install <github-repo-url>

# 從本機目錄安裝
/plugin install /path/to/plugin

# 從 SSH URL 安裝
/plugin install ssh://git@github.com/org/plugin.git

# 更新已安裝的 Plugin（可批次更新，v1.0.49+）
/plugin update
copilot plugin update --all

# 解除安裝
/plugin uninstall <name>

# 查看已安裝的 Plugin 清單
/plugin list

# 精細啟用/停用 Plugin 內個別元件（v1.0.76+）：plugins、instructions、agents、LSP servers、hooks
/plugins
```

### Plugin 結構

Plugin 使用 `plugin.json` 或 `.claude-plugin/plugin.json` / `.plugin/` 目錄結構，`name` 欄位為必填、需為 kebab-case 且 ≤64 字元：

```json
// plugin.json
{
  "name": "my-enterprise-plugin",
  "version": "1.0.0",
  "description": "企業內部開發輔助工具",
  "author": "Platform Team",
  "mcpServers": { ... },
  "lspServers": { ... },
  "agents": [ ... ],
  "skills": [ ... ],
  "hooks": { ... }
}
```

Marketplace 端則以 `marketplace.json` 描述可探索安裝的 Plugin 清單，供 `/plugin marketplace add` 引用。

> ✅ **Open Plugin Spec 支援**（v1.0.74+）：Copilot CLI 現支援業界通用的 **Open Plugin Spec v1** manifest 格式與 `mcp.json` 設定，降低跨工具（VS Code、Claude Code 等）重複封裝的成本。第一方 Plugin 會於 Session 啟動時自動更新到最新版本（v1.0.78+）。

### 預設 Marketplace

Copilot CLI 內建官方與社群精選的預設 Marketplace（實際名稱請以 `/plugin marketplace list` 當下顯示為準，因官方尚未在概念文件中窮舉固定清單）。可在 Repository 設定中定義 `extraKnownMarketplaces` 新增私有市集。

> 💡 **提示**：使用 `--plugin-dir` 旗標可在啟動時載入本地開發中的 Plugin，便於開發與測試；`COPILOT_PLUGIN_DIR_ONLY` 環境變數（v1.0.49+）可限制僅從指定目錄載入，適合鎖定環境的 CI/CD 場景。外部 Plugin 在 `/plugin list` 中會顯示在獨立的「External Plugins」區段。
>
> ⚠️ **供應鏈治理提醒**：Plugin／Marketplace 機制本質上是「安裝第三方可執行程式碼與設定」，企業導入時應比照套件管理（npm/Maven）供應鏈風險看待——建議限制可安裝來源、審查 `plugin.json` 內宣告的 MCP/Hook 權限範圍，詳見 [第 6 章：安全與治理](#第-6-章安全與治理)。

---

## 4.9 Extensions 擴充機制

Extensions 是比 Plugin 更輕量的擴充方式，可直接用 `@github/copilot-sdk` 為 Copilot 撰寫自訂工具和 Hook。官方指令參考頁確認互動式介面提供 `/extensions`（別名 `/extension`）管理指令；Plugin 自 v1.0.62 起也可隨附 Extension，並可透過 Plugin Marketplace 一併安裝。

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

> 📝 **注意**：可透過 Extension mode 設定控制擴充性。多個 Extension 的 Hook 會自動合併而非互相覆蓋（v1.0.11+）。此功能官方公開文件著墨較少，細節請以 `copilot help` 或 `/extensions` 指令內建說明為準。

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

- **自動學習**：Copilot 在工作過程中自動識別並儲存有用的模式（coding conventions、architectural patterns、cross-file dependencies）
- **跨 Session 查詢**：詢問過去的工作、修改過的檔案、建立的 PR
- **手動管理**：Copilot 使用 `store_memory` 工具記錄 Subject、Fact 和 Citations

```bash
# 詢問過去的工作記錄
> 我上次在哪個分支做了什麼修改？

# 查詢之前的 PR
> 顯示我最近建立的 PR 清單和摘要

# 管理記憶（v1.0.49+）
/memory show     # 檢視目前累積的記憶內容
/memory off      # 停用記憶功能
/memory on       # 重新啟用
```

### 發展時程

| 階段 | 時間 |
|------|------|
| Early Access（Pro / Pro+） | 2025-12-19 |
| Public Preview | 2026-01-15 |
| CLI GA 公告中列為正式功能 | 2026-02-25 |
| Pro / Pro+ 預設開啟 | 2026-03-04 |
| 支援 User Preferences（個人偏好記憶） | 2026-05-15 |
| `/memory on\|off\|show` 控制指令上線 | v1.0.49（2026-05-18） |

> ⚠️ **注意**：Memory 功能在非 Git Repository 中會優雅降級。若 Repository 不存在或無寫入權限，會顯示明確的錯誤提示。

---

## 4.11 ACP（Agent Client Protocol）與 Copilot SDK

ACP 是一個開放標準協定，允許第三方工具、IDE 或自動化系統將 Copilot CLI 當作 AI Agent 使用。**ACP 支援目前仍為 Public Preview**（官方原文："ACP support in GitHub Copilot CLI is in public preview and subject to change."），企業導入前應留意介面仍可能變動。

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

### Copilot SDK：六語言皆已 GA

**Copilot SDK 暴露與 Copilot CLI 完全相同的 Agent Runtime**，讓開發者可用程式化方式將 Copilot 的規劃、工具呼叫、檔案編輯能力內嵌進自己的應用程式，而不需開發者自行組裝 Agent Loop。時程演進非常快：

| 階段 | 時間 |
|------|------|
| Technical Preview | 2026-01-14 |
| Public Preview（開放 Copilot Free / 非 Copilot 用戶 / BYOK 企業） | 2026-04-02 |
| **GA（六語言同步）** | **2026-06-02** |

**安裝方式（依語言）：**

```bash
# Node.js / TypeScript
npm install @github/copilot-sdk

# Python
pip install github-copilot-sdk

# Go
go get github.com/github/copilot-sdk/go

# .NET
dotnet add package GitHub.Copilot.SDK

# Rust
cargo add github-copilot-sdk

# Java（Maven）
# com.github:copilot-sdk-java
```

> ⚠️ **重要相依關係**：所有語言 SDK 都透過 JSON-RPC 與「Copilot CLI 伺服器」通訊。**Node.js、Python、.NET 會自動內建捆綁 CLI 執行檔**，但 **Go、Java、Rust 版本需自行安裝 `copilot` CLI 並確保在 PATH 中可用**——換言之，SDK 目前仍是同一套 CLI Agent Runtime 的程式化外殼，並非完全脫鉤的獨立引擎。企業評估 SDK 導入時，仍需將 CLI 的版本管理、授權與治理策略一併納入考量。

**認證方式**：已登入 GitHub 使用者、OAuth GitHub App、環境變數（`COPILOT_GITHUB_TOKEN`/`GH_TOKEN`/`GITHUB_TOKEN`）、BYOK。計費模式與 CLI 相同（詳見第 9.4 節 AI Credits），Copilot Free 方案有限額可用。授權為 MIT License。

### AHP（Agent Host Protocol）：新興的另一協定，注意勿與 ACP 混淆

截至 2026-08 查證，Copilot CLI 出現了一個**仍在 Pre-release 階段**的新協定支援：`copilot --ahp`，可將 CLI 掛載到 Agent Host Protocol 主機（規格由 Microsoft/VS Code 陣營另行發布於 `microsoft.github.io/agent-host-protocol`，MIT License），讓多個終端機同時連上同一 Session 並即時觀看其對話串流；另有 `/ahp cloud <environment-id>`（掛載 Mission Control 雲端環境）與 `/ahp codespace <name>`（轉發 Codespace 的 copilotd port）等子指令。**AHP 與 ACP 是兩個不同協定**，前者是全新、仍在早期驗證階段的能力，尚未進入穩定版，建議企業列為「持續關注」而非現行可依賴的標準功能。

> 💡 **提示**：ACP 客戶端可透過 `session.ui.elicitation` 向使用者顯示互動式對話框，並可透過 `session.shell.exec` / `session.shell.kill` 執行與管理 Shell 指令。ACP 客戶端可切換 allow-all 權限模式、提供 MCP Server（stdio, HTTP, SSE）、註冊自訂 Slash Command，以及配置推理強度。

---

## 4.12 OpenTelemetry 可觀測性

Copilot CLI 底層與 Copilot SDK 共用同一套 OTEL 可觀測性管線，為 Agent Session、LLM 呼叫、工具執行提供追蹤能力。

> 📝 **範圍提醒**：OpenTelemetry 章節目前在官方「入門導覽」文件（`about-copilot-cli` / `use-copilot-cli`）中並未獨立列出，較完整的說明集中在 **Copilot SDK 的可觀測性文件**（`docs.github.com/en/copilot/how-tos/copilot-sdk/observability/opentelemetry`）。若企業主要透過互動式 CLI（而非 SDK）使用 Copilot，OTEL 追蹤能力仍可用，但建議以 `copilot help monitoring` 現場確認當下版本的揭露細節，而非假設所有指標都已在 CLI 文件中窮舉。

### 啟用 OpenTelemetry

```bash
# 查看 OpenTelemetry 配置說明
copilot help monitoring

# 啟用 OTEL 追蹤（透過環境變數設定 Exporter）
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
export OTEL_SERVICE_NAME="copilot-cli"
copilot
```

### 追蹤的 Span 類型

| Span 類型 | 說明 |
|-----------|------|
| **Agent Session** | 整個 Session 的生命週期 |
| **LLM Call** | 每次模型呼叫的延遲、Token 數 |
| **Tool Execution** | 工具執行的持續時間與結果 |
| **Sub-agent** | 子代理 Span（使用 INTERNAL kind） |
| **Hook Execution** | Hook 觸發記錄（以 Span Event 形式） |

### 觀測指標

| 指標 | 說明 |
|------|------|
| `github.copilot.time_to_first_chunk` | 首次串流回應的延遲（僅串流模式） |
| Token 消耗 | 每次 LLM 呼叫的 Input / Output Token 數 |
| 推理 Token | 支援模型的推理 Token 消耗（非零時顯示） |

> 💡 **提示**：此功能自 v1.0.4 起引入，v1.0.19-v1.0.20 持續強化。可搭配 Jaeger、Grafana Tempo 或其他 OTEL 相容的觀測平台使用。Span 命名於 v1.0.45 前後改採 **GenAI 語意慣例**（GenAI Semantic Conventions），MCP 工具呼叫統一以標準 `tool_call` Span 呈現；v1.0.61 起，OTLP Exporter（HTTPS）新增 **mTLS 與 Private CA** 支援，適合企業內網稽核環境。

---

## 4.13 Rubber Duck 建設性批評代理

> 📝 **正名提醒**：這項功能在早期版本（v1.0.18 起）曾以「Critic Agent」的實驗性型態出現，但 **官方目前正式名稱為「Rubber Duck」**，不建議在文件中繼續沿用「Critic Agent」這個非官方名稱。

Rubber Duck 是 Copilot CLI 內建的「建設性批評者」代理，官方定義逐字："Rubber duck is a built-in agent in GitHub Copilot CLI that acts as a constructive critic."

### 核心設計：刻意的異模型交叉審查

Rubber Duck 最關鍵的技術亮點在於它**刻意運行在與主 Session 不同的 AI 模型上**（例如主 Session 用 Claude，Rubber Duck 可能改用 GPT），官方理由是不同模型 "less likely to share the same blind spots, biases, or failure modes"——這比用同一模型自我審查更能發現真實問題。

### 運作流程

```mermaid
graph LR
    A[Agent 產生計畫/程式碼] --> B[Rubber Duck<br/>使用不同模型交叉審查]
    B --> C{發現問題？}
    C -->|是| D[依嚴重度分類：阻斷 / 非阻斷 / 建議]
    D --> A
    C -->|否| E[繼續執行]
```

### 使用方式

```bash
# 手動呼叫，針對特定問題徵詢意見
/rubber-duck What edge cases are missing?

# 查看／審查系統自動產生的 Skill 草稿變更
/chronicle skills review
```

- 非平凡（non-trivial）的變更完成後會**自動觸發**一次 Rubber Duck 審查
- 可用 `builtInAgents.rubberDuckAutoInvoke` 設定控制是否自動觸發（v1.0.60+）

### 版本演進

| 版本 | 日期 | 里程碑 |
|------|------|--------|
| v1.0.18 | 2026-04-01 | 以「Critic Agent」實驗性功能首次登場，僅支援 Claude 模型 |
| v1.0.41~ | 2026-05-05 | 正名為 Rubber Duck，開始支援 GPT Session（底層仍由 Claude 驅動，實驗性） |
| v1.0.49 | 2026-05-07 | 支援更多模型（模型限制持續放寬） |
| **v1.0.58** | **2026-06-02** | **預設啟用**，脫離實驗性狀態 |

> ⚠️ **已知限制**：官方文件明確標示 "currently only available if the main agent is using a Claude or GPT large language model"——若主 Session 使用 Gemini、Grok 等其他模型，Rubber Duck 可能無法使用，導入前建議先行驗證。

---

## 4.14 Remote Control 遠端控制

透過 `/remote` 指令，您可以在其他裝置或瀏覽器中遠端控制 CLI Session，實現跨裝置協作。官方定義："Remote control lets you monitor and steer a Copilot CLI session from GitHub.com or GitHub Mobile, even after you've stepped away from your machine." **此功能已於 2026-05-18 正式 GA**（涵蓋 Mobile、Web、VS Code；JetBrains 亦已支援）。

### 安全設計與限制

- 僅有**啟動該 Session 的同一 GitHub 帳號**能夠存取遠端控制
- 所有 Shell 指令、檔案操作、工具執行**仍在本機執行**，GitHub 端只接收 Session 事件串流，不代管實際運算
- 需 org/enterprise 政策開啟「Store local sessions in the Cloud → View and control」
- 本機須保持連線在線，Session 才能被遠端存取
- **僅限互動式 Session**，`--prompt`（`-p`）程式化模式不支援遠端控制
- 遠端可執行：回應權限請求、核准/拒絕計畫、送出新指令、切換模式、取消操作；但**斜線指令（如 `/allow-all`）不可從遠端介面使用**

### 啟用遠端控制

```bash
# 啟動帶有遠端控制功能的 Session
copilot --remote

# 在互動式介面中啟用/停用
/remote on
/remote off

# 查看目前遠端控制狀態（含連線狀態提示）
/remote
```

### 連線方式

```bash
# 從 --resume 選擇器連接遠端 Session
copilot --resume
# 在選擇器中會顯示遠端 Session

# 直接透過 Session ID 連接
copilot --connect <session-id>

# 恢復遠端 Session 時自動繼承 --remote 旗標
copilot --resume  # 自動繼承
```

### 使用場景

| 場景 | 說明 |
|------|------|
| 跨裝置接續 | 在桌機開始工作，手機或筆電接續 |
| 遠端協助 | 讓其他開發者遠端控制您的 CLI Session |
| Coding Agent 管理 | 遠端控制 Copilot Coding Agent 任務並提供引導 |

> 💡 **提示**：ACP 伺服器僅綁定 localhost，防止意外的網路暴露（v1.0.26+）。遠端 Session 被組織策略封鎖時會顯示清晰的提示訊息。

---

## 4.15 自訂模型供應商（Custom Model Provider）

Copilot CLI 支援連接您自己的模型供應商，取代 GitHub 託管的模型。這使您可以連接到 OpenAI 相容端點、Azure OpenAI、Anthropic，甚至本地運行的模型（如 Ollama）。

### 設定環境變數

| 環境變數 | 說明 |
|---------|------|
| `COPILOT_PROVIDER_BASE_URL` | 模型供應商 API 端點的基礎 URL |
| `COPILOT_PROVIDER_TYPE` | 供應商類型：`openai`（預設）、`azure`、`anthropic`。`openai` 類型適用於任何 OpenAI 相容端點（含 Ollama、vLLM） |
| `COPILOT_PROVIDER_API_KEY` | 供應商的 API 金鑰。不需要認證的供應商（如本地 Ollama）可省略 |
| `COPILOT_MODEL` | 使用的模型名稱（使用自訂供應商時**必填**） |

### 使用範例

```bash
# 連接本地 Ollama 實例
export COPILOT_PROVIDER_BASE_URL="http://localhost:11434/v1"
export COPILOT_PROVIDER_TYPE="openai"
export COPILOT_MODEL="llama3.1:70b"
copilot

# 連接 Azure OpenAI
export COPILOT_PROVIDER_BASE_URL="https://my-resource.openai.azure.com"
export COPILOT_PROVIDER_TYPE="azure"
export COPILOT_PROVIDER_API_KEY="your-azure-key"
export COPILOT_MODEL="gpt-4o"
copilot

# 連接自託管 Anthropic 端點
export COPILOT_PROVIDER_BASE_URL="https://my-anthropic-proxy.internal.com"
export COPILOT_PROVIDER_TYPE="anthropic"
export COPILOT_PROVIDER_API_KEY="your-api-key"
export COPILOT_MODEL="claude-sonnet-4-5"
copilot
```

### 模型要求

- **必須支援 Tool Calling**（Function Calling）：若模型不支援，CLI 會回傳錯誤
- **必須支援 Streaming**：串流回應為必要能力
- **建議 Context Window 至少 128k Token**：以獲得最佳結果

### 注意事項

| 特性 | 說明 |
|------|------|
| 內建子代理繼承 | `/review`、`/task`、explore、`/fleet` 等內建子代理會自動繼承您的供應商設定 |
| AI Credits 計費 | 使用自訂供應商時，AI Credit 成本估算會隱藏（因費用改由供應商端結算）。Token 使用量（輸入、輸出、快取）仍會顯示 |
| `/delegate` 限制 | `/delegate` 指令僅在同時登入 GitHub 時有效，因為它會將 Session 轉交給 GitHub 伺服器端 Copilot |
| 詳細設定說明 | 執行 `copilot help providers` 查看完整設定指南 |

> 💡 **企業應用場景**：企業可透過自訂模型供應商連接內部 AI Gateway，實現資料不出企業邊界的合規需求，同時享有 Copilot CLI 的完整工具鏈與 Agent 能力。

---

## 4.16 圖片、附件與語音輸入支援

Copilot CLI 支援視覺參考輸入，可將設計稿、截圖或圖表直接提供給 AI 分析；亦支援語音輸入取代打字。

### 輸入方式

| 方式 | 操作 | 適用場景 |
|------|------|---------|
| **拖放** | 直接將圖片拖放到 CLI 輸入區域 | 桌面操作 |
| **剪貼簿貼上** | `Ctrl + V`（圖片附件）/ `Alt + V`（圖片附件，另一組鍵位） | 截圖後快速輸入 |
| **檔案引用** | 在 Prompt 中使用 `@` 引用圖片檔案 | 引用設計稿或 Mockup |
| **程式化附加** | `--attachment` 旗標（`-p`/`--prompt` 模式，v1.0.44+） | CI/CD 或腳本化流程 |

**支援格式**：JPEG、PNG、GIF、WEBP、**PDF**、**HEIC**、**HEIF**——「available on all Copilot plans and are enabled by default」。

### 語音輸入（已 GA，v1.0.58+）

作為打字的替代方案，可直接對著麥克風口述 Prompt，**語音辨識在本地端運作，錄音內容不會上傳雲端**：

```bash
# 選擇並保存慣用的麥克風裝置（v1.0.71+）
/voice devices
```

### 使用範例

```bash
# 引用圖片檔案實作設計
> 根據 @mockup.png 實作這個頁面的 HTML/CSS，精確匹配佈局和間距

# 截圖分析錯誤
> [Ctrl+V 貼上錯誤截圖] 請分析這個錯誤訊息並提供修復方案

# UI 比對
> 比較 @design-v1.png 和 @design-v2.png 的差異，列出需要修改的 CSS 屬性
```

> 💡 **提示**：圖片輸入功能在處理 UI 開發、錯誤截圖分析、圖表理解等場景特別實用。搭配 Plan Mode 可以從設計稿直接規劃實作步驟。

---

## 4.17 內建 Agent 系統

Copilot CLI 內建一組專門化的 Agent，由 AI 模型自動判斷何時委派任務給最適合的子代理。

### 內建 Agent 清單

| Agent | 功能 | 運作方式 |
|-------|------|---------|
| **Explore** | 快速程式碼庫分析，在不汙染主 Context 的情況下回答程式碼相關問題 | 獨立 Context 運行 |
| **Task** | 執行指令（測試、建置等），成功時簡要摘要，失敗時完整輸出 | 自動摘要結果 |
| **General Purpose** | 處理複雜多步驟任務，需要完整工具集與高品質推理 | 獨立 Context，保持主對話清晰 |
| **Code Review** | 審查程式碼變更，「專注發現真正問題，最小化雜訊」（surfacing only genuine issues, minimizing noise） | 獨立 Context 運行 |
| **Research** | 跨程式碼庫、相關儲存庫和網路進行深度研究，產出帶有引用的詳細報告 | 深度搜尋與分析 |
| **Rubber Duck** | 作為建設性批評者，刻意使用與主 Session 不同的模型交叉審查（詳見 [4.13](#413-rubber-duck-建設性批評代理)） | 可用 `/rubber-duck` 手動呼叫，非瑣碎任務後亦會自動觸發 |

### Agent 使用方式

```bash
# 方式 1：使用 /agent 指令選擇
/agent

# 方式 2：在 Prompt 中自然呼叫
> 使用 refactoring agent 重構這段程式碼

# 方式 3：命令列選項指定
copilot --agent=backend-expert --prompt "重構 UserService"
```

### 自訂 Agent 層級

| 層級 | 位置 | 作用範圍 |
|------|------|---------|
| **系統層級** | 內建 | 最高優先權 |
| **使用者層級** | `~/.copilot/agents/` | 所有專案 |
| **Repository 層級** | `.github/agents/` | 當前專案 |
| **組織/企業層級** | 組織 `.github-private` Repository 的 `/agents/` 目錄 | 組織下所有專案 |

> ⚠️ **優先順序**：系統 Agent > Repository Agent > 組織 Agent。發生命名衝突時，高優先順序的 Agent 會覆蓋低優先順序的。

---

## 4.18 Sandbox 安全沙箱（本機／雲端）

Sandbox 是 GA 後新增的重要安全機制，讓 Copilot 在**隔離環境**中執行工具操作，降低 Agent 誤操作或惡意 Prompt Injection 造成的實際傷害。目前分為本機與雲端兩種型態，**皆屬 Public Preview**（官方原文："Cloud and local sandboxes for GitHub Copilot are in public preview and subject to change."）。

### 本機 Sandbox（Local Sandboxing）

```bash
# 啟用本機沙箱
/sandbox enable

# 檢視目前生效的 Sandbox 政策（路徑、拒絕清單、網路存取狀態，v1.0.79+）
/sandbox policy

# 針對單次 Session 開關 OS-level shell sandbox，不影響已存設定（v1.0.70+，適合搭配 -p）
copilot --sandbox
copilot --no-sandbox
```

本機 Sandbox 限制檔案系統存取範圍與網路存取，macOS/Linux 下對相對路徑與 symlink 的拒絕清單皆生效（Windows 目前無法依路徑拒絕）。macOS Keychain 存取預設關閉（更嚴格隔離），可視需求於 `/sandbox` 對話框重新啟用；也可選擇性開放 Sandbox 內存取 git/gh 憑證。

### 雲端 Sandbox（Cloud Sandboxing）

```bash
# 於獨立、雲端代管的隔離環境中執行 Session
copilot --cloud
```

### 企業層級 Sandbox 政策（v1.0.76+ / v1.0.79+）

| 能力 | 說明 |
|------|------|
| 強制收緊下限 | 企業可透過 Managed Settings 強制設定限制性 Sandbox 下限，**只能收緊、不能放寬**使用者自訂的 Sandbox 政策 |
| 鎖定欄位提示 | `/sandbox` 對話框會顯示哪些欄位是由組織強制鎖定 |
| Allow-Auto-Only 政策 | 企業可設定僅允許 `/allow-all auto`（自動安全判斷），但完全封鎖無條件 allow-all |
| 強制 Proxy | 企業可強制指定 Sandbox 對外請求的 Proxy URL，使用者仍可自控憑證 |
| MDM 整合 | 支援透過 macOS / Windows 原生 MDM（Mobile Device Management）強制執行 Sandbox 政策（v1.0.77+） |

> ⚠️ **重大設定鍵變更**（v1.0.79，Breaking Change）：`allowDevToolCaches` 已更名為 `allowDevToolAccess`；`sandbox.gitAuth` / `sandbox.ghAuth` 已遷移為 `sandbox.auth.git` / `sandbox.auth.gh`。**這兩項變更均無自動遷移機制**，舊 Key 會被靜默忽略，企業升級前務必手動更新設定檔並驗證 Sandbox 政策仍如預期生效。
>
> 💡 **企業導入建議**：Sandbox 是目前官方主推的「降低 Agent 操作風險而不犧牲自主性」機制，建議與 [第 6 章：安全與治理](#第-6-章安全與治理) 的 `--deny-tool` / Hooks 防護策略搭配使用，形成多層防禦（Defense in Depth）。

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

    B --> B1["copilot-instructions.md"]
    B --> B2["AGENTS.md"]
    B --> B3["instructions/*.md"]

    C --> C1["@ 引用檔案"]
    C --> C2["Prompt 中的描述"]
    C --> C3["對話歷史"]

    D --> D1["目錄結構"]
    D --> D2["pom.xml / package.json"]
    D --> D3["README.md"]
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

# 從 MCP Registry 搜尋並安裝 MCP Server（v1.0.64+ 為 /mcp registry；早期版本為引導式精靈，v1.0.25+）
/mcp registry
/mcp search    # 實驗性：搜尋 Registry 內可用的伺服器能力（v1.0.49+）

# 查看已配置的 MCP Server
/mcp
/mcp list

# 查看特定 MCP Server 的工具清單
/mcp show <server-name>

# 啟用 / 停用 MCP Server（跨 Session 持久化，v1.0.19+）
/mcp enable <name>
/mcp disable <name>

# 重新載入 MCP 設定
/mcp reload

# MCP OAuth 認證管理（v1.0.15+）
/mcp auth

# 非互動式 MCP 管理（v1.0.21+）
copilot mcp

# MCP 設定檔位置（v1.0.22+ 變更）
# .mcp.json（Repository 根目錄，唯一讀取的工作區 MCP 設定檔）
# ~/.copilot/mcp-config.json（使用者層級）
```

> ⚠️ **重要變更**（v1.0.22+）：CLI 現在**僅讀取 `.mcp.json`** 作為工作區 MCP 設定。`.vscode/mcp.json` 和 `.devcontainer/devcontainer.json` 已不再作為 MCP 設定來源。若偵測到 `.vscode/mcp.json` 但不存在 `.mcp.json`，會顯示遷移提示。

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

### GitHub MCP Registry（github.com/mcp）

GitHub 官方於 2025-09-16 推出集中化的 **MCP Registry**（`https://github.com/mcp`），定位為「Connect models to the real world」——一個可搜尋、可一鍵安裝的 MCP Server 目錄。截至 2026-08 查證約收錄 **219 個 MCP Server**（此數字會持續成長），涵蓋 Figma、Postman、HashiCorp、Dynatrace、Context7、Playwright、Chrome DevTools MCP 等知名工具。可在 CLI 內用 `/mcp registry` 或 `/mcp search` 探索並安裝，無需離開終端機。

### 內建 GitHub MCP Server 官方工具集（Toolsets）

Copilot CLI **內建** GitHub MCP Server，無需另行安裝；預設僅啟用**唯讀（Read-only）**工具集以降低風險與 Token 消耗。可用 `/mcp show github` 檢視狀態。官方定義 20 個標準 Toolset：

| Toolset | 說明 | 預設啟用 |
|---|---|:---:|
| `context` | 目前使用者/操作環境背景資訊 | ✅ |
| `repos` | 儲存庫操作 | ✅ |
| `issues` | Issue 管理 | ✅ |
| `pull_requests` | PR 管理 | ✅ |
| `users` | 使用者搜尋 | ✅ |
| `actions` | GitHub Actions / CI-CD 操作 | |
| `code_quality` | 程式碼品質工具 | |
| `code_security` | 程式碼掃描等安全工具 | |
| `secret_protection` | 密碼掃描等保護工具 | |
| `security_advisories` | 安全公告 | |
| `copilot` / `copilot_issue_intents` | Copilot 相關功能 / Issue 指派意圖 | |
| `dependabot` | Dependabot 整合 | |
| `discussions` | GitHub Discussions | |
| `gists` | Gist 管理 | |
| `git` | 低階 Git API 操作 | |
| `labels` | 標籤管理 | |
| `notifications` | 通知管理 | |
| `orgs` | 組織相關工具 | |
| `projects` | GitHub Projects 管理 | |
| `stargazers` | Star 管理 | |

**控制方式：**

```bash
# 新增指定工具集
copilot --add-github-mcp-toolset actions

# 啟用全部工具集
copilot --enable-all-github-mcp-tools

# 單一工具粒度控制
copilot --add-github-mcp-tool <tool-name>

# 完全停用內建 MCP Server
copilot --disable-builtin-mcps

# 唯讀模式：讀取限制優先於任何寫入請求，即便明確要求寫入也會被略過（高安全需求場景）
copilot --read-only
```

> 💡 **提示**：也可透過環境變數 `GITHUB_TOOLSETS` 控制。除官方 GitHub MCP Server 外，Copilot CLI 也支援連接任意第三方/自訂 MCP Server（遠端 HTTP、本地 Docker、本地二進位檔三種部署方式皆支援），不侷限於 GitHub 生態系。

## 5.5 Session 管理與對話引導

### Infinite Sessions：自動 Context 管理

官方將 Copilot CLI 的長任務能力定位為「**Infinite Sessions**」——不需擔心 Context 用盡，系統會透過智慧壓縮（Compaction）自動摘要對話歷史、同時保留關鍵資訊，因此原則上可無限期地在同一 Session 中持續工作。官方提示原文："If you ever need to manually trigger compaction, use `/compact`. This is rarely necessary since the system handles it automatically."

> 💡 **最佳實務**：雖然 Infinite Sessions 允許長時間運作，官方仍建議**保持 Session 聚焦**——處理不相關任務時改用 `/clear` 或 `/new` 重置 Context，而非在同一 Session 中無限累積，這能顯著提升回應品質，官方比喻為「像跟同事開始一段全新的對話」。

### Session 儲存結構

Copilot CLI 的 Session 資料儲存於以下結構：

```
~/.copilot/session-state/{session-id}/
├── events.jsonl      # 完整 Session 歷史記錄
├── workspace.yaml    # Session 中繼資料
├── plan.md           # 實作計畫（若有建立）
├── checkpoints/      # Context 壓縮歷史（Compaction）
└── files/            # 持久化產出物（非 Repo 內容）
```

### Session 檢查點管理

```bash
# 查看 Session 資訊
/session

# 查看壓縮檢查點清單
/session checkpoints

# 查看特定檢查點詳情
/session checkpoints 2

# 查看 Session 中的暫存檔案
/session files

# 查看目前實作計畫
/session plan
```

### Session 生命週期管理

Copilot CLI 提供完整的 Session 管理能力，支援連續工作與上下文保存：

```bash
# 繼續最近的 Session（偏好從目前工作目錄恢復，v1.0.35+）
copilot --continue

# 選擇並恢復歷史 Session（支援短 ID 前綴 7+ 字元，v1.0.32+）
copilot --resume
# Session 選擇器支援 / 搜尋過濾

# 以名稱恢復 Session（v1.0.35+）
copilot --resume=my-session-name

# 以名稱啟動 Session（v1.0.35+）
copilot --name "訂單模組重構"

# 直接連接遠端 Session（v1.0.32+）
copilot --connect <session-id>

# 在互動式介面中恢復 Session
/resume

# 開始新 Session（保留舊 Session 在背景）
/new

# 完全放棄目前 Session，重新開始
/clear

# /new 和 /clear 可帶 Prompt 直接開始新對話
/new 幫我分析 pom.xml 的依賴

# 重新命名 Session（不帶參數時自動從對話歷史生成名稱，v1.0.12+）
/rename 訂單模組重構
# 或
/session rename 訂單模組重構

# 匯出 / 分享 Session
/share              # 儲存為 Markdown 檔案
/share html         # 匯出為自包含的互動式 HTML 檔案（v1.0.15+）
/share gist         # 上傳為 GitHub Gist

# Session 使用統計（含 GitHub 風格的貢獻圖表，v1.0.35+）
/session

# Session 刪除管理（v1.0.35+）
/session delete          # 刪除指定 Session
/session delete-all      # 刪除所有 Session
# 或在 Session 選擇器中按 x 刪除

# 在 Session 選擇器中按 s 循環排序：相關性、最後使用、建立時間、名稱（v1.0.37+）
```

> 📝 **v1.0.35+ 行為變更**：
> - `--continue` 偏好恢復**目前工作目錄**的 Session，而非最近觸碰的 Session
> - 使用者設定現在儲存在 `~/.copilot/settings.json`，與 `config.json` 中的內部狀態分離
> - `/clear` 完全放棄目前 Session，`/new` 開啟新對話但保留舊 Session 在背景
> - `/cd` 在不同 Session 之間維持獨立的工作目錄
> - Session 選擇器顯示分支名稱、閒置/使用中狀態、支援改進的搜尋

### 多工作階段管理：Worktree / Fork / Rewind / Sessions Sidebar

GA 後新增了一組面向「同時處理多條並行工作」的能力，是企業多工開發情境下的重要新增功能：

```bash
# 建立/重用獨立 git worktree 並在其中啟動 Session（實驗性，v1.0.64+；-w 為簡寫）
copilot --worktree [name]
/worktree new
/new-worktree          # 建立新 worktree 並直接開新對話（實驗性）

# /worktree 保留未提交變更在原地；/move 則會把未提交變更一併搬過去（v1.0.71+ 拆分）
/move

# 控制 worktree 從 HEAD 或遠端預設分支啟動（v1.0.79+）
# 設定鍵：worktreeBaseRef

# 將目前 Session 分叉成獨立新 Session（v1.0.45+）
/fork
/branch          # 別名，比照 Claude Code 命名習慣（v1.0.64+）

# 回溯到對話歷史中的任一時間點，不只是上一個快照（v1.0.12+ 起支援 timeline picker）
/rewind
# 或按兩下 Esc（Double-Esc）快速回溯

# Session 側欄：管理多個並行 Session（v1.0.76+ 起實驗性，v1.0.78+ 起分頁化）
# 側欄快捷鍵：n 新建、x 關閉
```

> ⚠️ **注意**：`/worktree`、`/fork`、Sessions Sidebar 多屬近期新增（部分仍為實驗性/需 `/experimental on`），企業導入前建議先在非關鍵專案驗證行為，並留意這些功能會在檔案系統中建立額外的 git worktree 目錄（`<repo>.worktrees/` 下），需納入磁碟空間與 `.gitignore` 管理考量。

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

# 手動壓縮 Context（可帶自訂提示，v1.0.15+）
/compact
/compact 保留所有關於認證流程的對話

# 自動壓縮：當達到 Token 上限的 95% 時自動在背景執行
# 支援 preCompact hook 在壓縮前執行自訂邏輯

# /ask 指令：「一次性」查詢，不汙染 Context（v1.0.15+）
/ask 什麼是 SOLID 原則？
# 回覆完成後不保留在對話歷史中
```

> 💡 **提示**：自動壓縮在背景進行，不會中斷對話。壓縮後 Skill 仍然有效。擴展思維（extended thinking）在壓縮後也會被保留。`/ask` 適合用來查詢不需要保留在對話脈絡中的快速問題。

## 5.6 多儲存庫工作流程

Copilot CLI 提供靈活的多儲存庫工作流程，是微服務架構、Monorepo 或跨專案開發的關鍵差異化功能。

### 方式 1：從父目錄啟動

```bash
# 從包含多個 Repo 的父目錄啟動
cd ~/projects
copilot

# Copilot 可同時存取所有子目錄中的 Repository
# 適用於：微服務架構、跨 Repo 協調變更、重構共用模式
```

### 方式 2：使用 /add-dir 擴展存取範圍

```bash
# 從一個 Repo 啟動後，動態新增其他 Repo
copilot
/add-dir /Users/dev/projects/backend-service
/add-dir /Users/dev/projects/shared-libs
/add-dir /Users/dev/projects/documentation

# 查看目前已允許的目錄清單
/list-dirs
```

### 跨 Repo 工作流範例

```bash
# 跨三個 Repo 的 API 變更
> 我需要更新使用者認證 API。變更跨越：
  - @/projects/api-gateway（路由變更）
  - @/projects/auth-service（核心邏輯）
  - @/projects/frontend（客戶端更新）
  請先展示目前認證流程在三個 Repo 間的運作方式。
```

### 適用場景

| 場景 | 說明 |
|------|------|
| 跨模組重構 | 更新共用模式到所有使用位置 |
| API 契約變更 | 同時更新 Server 與 Client |
| 跨 Repo 文件 | 產出引用多個程式碼庫的文件 |
| 依賴升級 | 在 Monorepo 中統一升級依賴 |
| 微服務協調 | 協調多個微服務的介面變更 |

## 5.7 圖片驅動開發

利用 Copilot CLI 的圖片輸入能力，實現從設計稿到程式碼的快速轉換。

### 實務工作流程

```bash
# Step 1：輸入設計稿
> 根據 @mockup/login-page.png 實作登入頁面
  使用 Vue 3 + Tailwind CSS
  精確匹配佈局和間距

# Step 2：微調
> [Ctrl+V 貼上修改後截圖] 這個按鈕間距需要加大，其他都正確

# Step 3：遷移清單
> 執行 linter 並將所有錯誤寫入 `migration-checklist.md` 作為清單
  然後逐一修復，邊修邊打勾
```

### 適用場景

| 場景 | 說明 |
|------|------|
| 設計稿實作 | 從 Figma/XD 匯出的設計截圖直接實作 |
| Bug 截圖修復 | 從 QA 回報的截圖定位並修復問題 |
| UI 差異比對 | 比較設計稿與實作的視覺差異 |
| 圖表解讀 | 分析架構圖、流程圖並產出對應程式碼 |

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

### 互動式權限管理（v1.0.35+）

```bash
# 查看目前 allow-all 狀態
/allow-all show

# 啟用允許所有工具（需雙次 Esc 確認，v1.0.36+）
/allow-all on

# 關閉允許所有工具
/allow-all off
```

### 位置感知權限（v1.0.37+）

工具批准規則現在會考慮**工作目錄**：
- 批准規則在主 Session 和子代理之間**共享**
- 切換工作目錄時，先前對特定路徑的批准仍然有效
- CLI 在不同目錄啟動時會使用各自的權限設定
- **雙次 Esc 確認**：切換 allow-all 模式時需要按兩次 Esc 鍵確認，防止誤操作（v1.0.36+）

### 核准模式（Approval Modes，v1.0.51+/v1.0.78+）

```bash
# 切換核准模式：default（逐次詢問）/ assisted / allow-all / show
/permissions
/permissions default
/permissions reset      # 重置本 Session 記憶的核准
/reset-allowed-tools     # 重置已授予的工具權限（舊指令，功能相近）

# 半自動核准：由「安全判斷」模型自動放行低風險操作，仍攔截高風險操作
# 需先啟用實驗性模式（v1.0.69+ 起強制要求）
/experimental on
/allow-all auto
```

> ⚠️ **重要**：`/allow-all auto` 的安全判斷模型自 v1.0.78 起**不再可由使用者自行設定**，改為系統自動選擇，避免使用者刻意配置寬鬆的判斷模型以規避風控。企業如需完全禁止繞過人工核准，可透過 Managed Settings 設定 `permissions.disableBypassPermissionsMode`（v1.0.55+）直接**封鎖 allow-all / YOLO 模式的啟用**。

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

> ⚠️ **企業環境嚴禁使用 YOLO Mode**。如必須使用，應在 VM、Container 或沙箱環境中執行（建議搭配 [4.18 Sandbox](#418-sandbox-安全沙箱本機雲端) 而非完全依賴權限旗標）。企業可透過 `permissions.disableBypassPermissionsMode` 設定於組織層級**直接封鎖** YOLO / allow-all 模式的啟用，不必僅依賴開發者自律。

## 6.3 企業治理策略

### Copilot Policy 設定建議

| 政策 | 建議設定 | 說明 |
|------|---------|------|
| **Copilot CLI 存取** | 啟用（特定團隊） | 只對有需要的團隊開放 |
| **MCP Server** | 限制為白名單 | 只允許內部核準的 MCP |
| **模型選擇** | 限制可用模型 | 避免使用未經評估的模型 |
| **Trusted Directories** | 限制為專案目錄 | 避免存取系統目錄 |

### 6.3.1 已知落差與業界安全研究（2026 年最新）

導入 Copilot CLI（或任何 Agentic CLI 工具）前，企業安全團隊應了解以下幾項官方文件不會主動提醒、但業界研究已明確揭露的風險：

**① Content Exclusions 不涵蓋 CLI**：多篇資安分析明確指出，Business/Enterprise 方案的「內容排除規則」（Content Exclusions，用來阻擋 Copilot 存取特定檔案/路徑）**不適用於 Copilot CLI、Coding Agent，或 IDE 中的 Agent Mode**——這些「代理式」介面是既有內容排除規則的治理盲區。若組織依賴 Content Exclusions 保護機敏檔案，**必須額外針對 CLI 制定 Trusted Directories 與 `--deny-tool` 規則**，不能假設既有規則自動生效。（來源：CloudThat 企業導入分析）

**② TrustFall 類型漏洞（MCP 自動信任風險）**：Adversa AI 於 2026-05 揭露名為「TrustFall」的漏洞類別——Claude Code、Cursor、Gemini CLI、**Copilot CLI** 等主流 Agentic CLI，在使用者接受「資料夾信任」提示後，會自動核准並啟動該 Repository 內定義的 MCP Server（`.mcp.json`），而信任對話框往往「未明確提及即將啟動 MCP、未列舉將執行的檔案、無法單獨拒絕 MCP 而保留其餘信任授權」。已有實際案例（Miasma worm 曾在 Azure/durabletask 等 Microsoft Azure 儲存庫植入 `.mcp.json` 觸發自動執行）。**這是業界代理式 CLI 的共通問題，非 Copilot CLI 獨有**，但企業導入時務必納入風險清單：Clone 不受信任的 Repository 前，應先人工檢視是否存在 `.mcp.json`，再決定是否信任該目錄。（來源：Adversa AI / DarkReading / The Register）

**③ 密鑰外洩統計**：GitGuardian 研究顯示，啟用 GitHub Copilot 的公開儲存庫，密鑰洩露率達 **6.4%**，較所有公開儲存庫基線 4.6% 高出約 40%——AI 輔助編碼提升生產力的同時，也可能提升機敏資訊意外進入版本控制的機率，強化了「`postToolUse` Hook 稽核 + Pre-commit 密鑰掃描」的必要性（詳見 6.4 節）。

**④ Gartner「比例治理」原則**（2026-05）：Gartner 明確警告「對所有 AI 代理採取統一治理策略，將導致企業專案失敗率升高」，並預測 **到 2027 年，40% 企業將因未區分『代理的行動能力』與『被授予的存取範圍』而下架已部署的代理程式**。建議企業依代理的**自主權等級（Autonomy Level）**做比例治理——例如 Ask Mode（僅建議）、Plan Mode（需人工核准計畫）、Autopilot（自主執行）三種模式，應對應不同的信任邊界與稽核密度，而非用同一套規則管理。

**⑤ 業界治理框架參考**（非官方，但可作為實務補充）：

- **Maxim AI 五步框架**：(1) 盤點裝置上的代理程式與 MCP Server (2) 透過閘道路由代理流量並配置虛擬金鑰 (3) 套用防護機制偵測密鑰/PII 外洩 (4) 裝置層級集中允許/拒絕清單 (5) 透過 MDM 持續稽核部署，解決「Shadow AI」（未受控個人裝置上的 AI 使用）問題
- **Checkmarx 五大風險與九項對策**：風險含提示注入、不安全建議、密鑰外洩、依賴幻覺仿冒攻擊（AI 建議安裝不存在但被惡意搶注的套件名稱）、隱私合規；對策含人工審查、OWASP 標準、密鑰管理、開發者培訓、DevSecOps 整合、集中治理、限制第三方擴充、敏感程式碼使用政策、審查 MCP 資料流

> 📝 **本節資訊來源**：CloudThat、Adversa AI、DarkReading、The Register、GitGuardian（經 Maxim AI 引用）、Gartner 新聞稿（2026-05-26）、Maxim AI、Checkmarx，皆為 2026 年上半年至查證當下的公開研究，建議企業安全團隊定期關注最新揭露動態，不視為一次性檢查清單。

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
| **MCP OAuth 認證** | MCP Server 認證管理 | `/mcp auth`（v1.0.15+） |
| **Repository MCP 信任** | 僅在信任資料夾後載入 `.mcp.json` | 資料夾信任確認 |

> ⚠️ **已知限制**（[官方文件](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli#known-mcp-server-policy-limitations)）：CLI 目前**無法支援**以下組織級 MCP 政策：
> - 「MCP servers in Copilot」（控制是否允許使用 MCP）
> - 「MCP Registry URL」（控制允許的 MCP Registry 來源）

### UNC 路徑防護

自 v1.0.5 起，Copilot CLI 會 **自動封鎖網路路徑（UNC Path）**，防止透過 SMB 認證洩漏憑證。

### 背景任務安全（v1.0.33+）

```bash
# 背景任務（Ctrl+X → B）遵守 Session 的權限設定
# 不會新增額外的批准對話框
# 背景任務使用獨立的 Sub-agent，不共用主 Session 的對話歷史
```

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

## 8.4 官方推薦工作流程（Explore → Plan → Review → Implement → Verify → Commit）

根據 [GitHub 官方最佳實務文件](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices)逐字核對，處理複雜任務時官方建議的完整工作流其實是 **六個步驟**，比坊間常簡化引用的「四步驟」多了「Review（覆核計畫）」與「Verify（驗證結果）」兩個關鍵環節：

### Step 1：Explore（探索）

```bash
> Read the authentication files but don't write code yet
```

- 目的：在修改前，先完整理解現有系統，明確要求「先讀不寫」
- 建議：切換到 Ask Mode（不產生變更），或使用 `--agent=explore`

### Step 2：Plan（規劃）

```bash
/plan Implement password reset flow
```

- 官方原文重點："**Models achieve higher success rates when given a concrete plan to follow.**" 在 Plan Mode 下，Copilot 會先分析需求與程式庫、**主動提出釐清問題對齊需求**、建立含核取方塊的結構化計畫、存成 `plan.md`，並**等待你的核准**才會開始實作
- 按 `Shift+Tab` 切換 Plan Mode，或直接下 `/plan` 指令；可按 `Ctrl+Y` 在編輯器中檢視/編輯計畫
- **何時該用 Plan Mode**（官方場景表）：複雜多檔案變更、影響面廣的重構、新功能實作 → 建議使用；快速 Bug 修復、單一檔案變更 → 可跳過

### Step 3：Review（覆核計畫）

```bash
> Check the plan, suggest modifications
```

- 目的：人工審查 AI 提出的計畫是否合理，必要時要求調整範圍或補強遺漏的邊界條件

### Step 4：Implement（實作）

```bash
> Proceed with the plan
```

- 目的：按已核准的計畫逐步產生程式碼；大型任務可要求分階段實作，每步完成後用 `/diff` 確認

### Step 5：Verify（驗證）

```bash
> Run the tests and fix any failures
```

- 目的：官方明確將「執行測試並修復失敗」列為獨立步驟，而非隱含在 Commit 之前——避免未經驗證的程式碼直接進入提交流程
- 建議搭配 `/security-review`（見下方）在提交前先做一輪安全掃描

### Step 6：Commit（提交）

```bash
> Commit these changes with a descriptive message
```

- 目的：利用 Copilot 產生 Commit Message／PR 描述，人工做最終審查後提交
- 可搭配 `/pr` 建立 PR，`/review` 或 `/security-review` 做提交前最後把關

### 工作流程圖

```mermaid
graph LR
    A[Explore<br/>理解現狀] --> B[Plan<br/>設計方案]
    B --> R[Review<br/>覆核計畫]
    R --> C[Implement<br/>逐步實作]
    C --> V[Verify<br/>執行測試/修復]
    V --> D[Commit<br/>提交審查]
    D -->|需修正| C
    R -->|計畫不對| B
    B -->|資訊不足| A
    V -->|測試失敗| C
```

### 安全性審查指令（`/security-review`，全使用者開放 v1.0.64+）

```bash
# 對目前本機變更做安全審查，優先處理高風險發現
/security-review Review my current local changes for security issues. Prioritize high-severity findings and suggest remediations I can apply before opening a pull request.

# 用多模型交叉審查程式碼變更（可指定使用的模型）
/review Use Opus 4.5 and Codex 5.2 to review the changes in my current branch against main. Focus on potential bugs and security issues.
```

> 💡 **建議流程**：先處理 `/security-review` 標示的高風險發現、驗證修復，再進入一般的 PR 審查流程——這是官方文件明確建議的順序，避免安全問題與一般 Code Review 意見混雜處理。

## 8.5 Session 管理最佳實務

### 保持 Session 專注

官方建議每個 Session 聚焦於**單一目標**，而非在同一 Session 中混合不同任務：

| 做法 | 說明 |
|------|------|
| ✅ 一個 Session 一個目標 | 「重構認證模組」→ 完成後開新 Session |
| ✅ 適時壓縮 Context | 長 Session 中用 `/compact` 釋放空間 |
| ✅ 使用 `/ask` 做快速查詢 | 不污染主要 Context |
| ❌ 在同一 Session 處理多個不相關任務 | Context 混亂導致品質下降 |
| ❌ 等 Context 溢出才壓縮 | 應主動管理 |

### Session 命名規範

```bash
# 啟動時命名（便於後續 resume）
copilot --name "feat/jwt-auth-migration"

# 事後命名
/rename jwt-auth-migration

# 自動命名
/rename
# Copilot 根據對話內容自動產生名稱
```

### 長期任務拆分策略

```
大型任務（如 API 重構）
├── Session 1: Explore（探索現狀，產出分析報告）
├── Session 2: Plan（設計方案，產出 plan.md）
├── Session 3: Code - Part 1（核心邏輯）
├── Session 4: Code - Part 2（整合測試）
└── Session 5: Commit & PR
```

## 8.6 權限管理最佳實務

### 萬用字元權限模式

官方推薦使用萬用字元語法授予常用工具批量權限，避免反覆確認：

```bash
# 允許所有 git 子命令
copilot --allow-tool='shell(git:*)'

# 允許 npm 與 node 相關指令
copilot --allow-tool='shell(npm:*)' --allow-tool='shell(node:*)'

# 允許特定 MCP Server 的所有工具
copilot --allow-tool='github'

# 禁止危險操作
copilot --deny-tool='shell(git push --force)' --deny-tool='shell(rm -rf)'
```

### 企業環境推薦設定

```bash
# 企業開發者日常啟動指令
copilot \
  --allow-tool='shell(git:*)' \
  --allow-tool='shell(mvn:*)' \
  --allow-tool='shell(npm:*)' \
  --allow-tool='shell(docker:*)' \
  --deny-tool='shell(git push --force)' \
  --deny-tool='shell(rm -rf)' \
  --deny-tool='shell(kubectl delete)'
```

### 在 Custom Instructions 中定義預設權限

```markdown
<!-- .github/copilot-instructions.md -->
## 工具使用規範
- 允許：git、mvn、npm、docker 相關操作
- 禁止：git push --force、rm -rf /、kubectl delete namespace
- 所有資料庫操作需人工確認
- 不得修改 .env、secrets/、certs/ 目錄中的檔案
```

### AI Credit Session 額度上限（企業預算控管）

自 2026-06 計費模式改為 AI Credits（詳見第 9.4 節）後，官方新增可對**單一 Session 設定 AI Credits 上限**的能力，避免長時間或複雜任務無預警耗用超乎預期的預算：

```bash
# 於 Session 中設定/檢視額度上限（實際指令請以 /help 當下版本為準）
/limits
```

### 受信任 Repository 的組態鎖定（v1.0.70+）

受信任的 Repository 可透過 `.github/copilot/settings.json` **固定**模型、Reasoning Effort、Context Tier，並延伸 URL / MCP / Skill 的拒絕清單——這讓團隊可以把「核准過的設定」直接寫進版本控制，取代僅靠文件宣導的作法：

```json
// .github/copilot/settings.json
{
  "model": "claude-sonnet-4-5",
  "effortLevel": "medium",
  "contextTier": "standard",
  "denyUrls": ["*.internal-legacy.example.com"]
}
```

### 用 `/refine` 改寫雜亂的 Prompt（v1.0.70+）

```bash
# 把意識流式的口語需求，交給 Copilot 改寫成清楚的 Prompt 再送出
/refine 我想要那個訂單那邊那個重複扣款的問題查一下順便修掉
```

## 8.7 團隊協作與生產力量測

### 團隊指引建立建議

| 項目 | 說明 |
|------|------|
| Custom Instructions | 統一團隊程式碼風格、架構規範 |
| Prompt 範本庫 | 共享常用 Prompt（存於 `.github/prompts/`） |
| Agent 定義 | 為團隊角色定義專用 Agent |
| Hook 規範 | 統一安全稽核、日誌格式 |
| MCP Server | 統一整合工具（DB、Docker、監控） |

### 生產力量測指標

| 指標 | 量測方式 | 說明 |
|------|---------|------|
| Commit 頻率 | Git log 分析 | 每日 / 每週 Commit 次數變化 |
| PR 週期 | GitHub Insights | 從開 PR 到 Merge 的時間 |
| Code Review 回退率 | PR 統計 | AI 產生程式碼被退回修改的比例 |
| Session 利用率 | `/usage` 統計 | AI Credits 使用效率 |
| Bug 產出率 | Issue Tracker | AI 協助產生的程式碼之缺陷率 |

### 持續學習資源

| 資源 | 連結 | 說明 |
|------|------|------|
| GitHub Skills 互動課程 | [create-applications-with-the-copilot-cli](https://github.com/skills/create-applications-with-the-copilot-cli) | 官方 Hands-on 練習 |
| 官方最佳實務 | [cli-best-practices](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices) | 定期更新的實務指引 |
| Changelog | `/changelog` 或 [changelog.md](https://github.com/github/copilot-cli/blob/main/changelog.md) | 版本更新紀錄 |
| Community Discussions | [GitHub Discussions](https://github.com/github/copilot-cli/discussions) | 社群討論與回饋 |

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
npm install -g @github/copilot@1.0.80

# 在團隊文件中記錄版本
# docs/tool-versions.md
# - Copilot CLI: v1.0.80 (2026-08-14)
# - 上次升級日期：2026-08-14
# - 下次評估日期：2026-11-14
```

> ⚠️ **版本節奏提醒**：Copilot CLI 近半年來維持**近乎每週一版**的發佈節奏，且不時伴隨 Breaking Change（如 v1.0.79 的 Sandbox 設定鍵重命名）。企業若採「固定版本」策略，建議至少每季度重新評估一次，並在升版前先閱讀 [changelog.md](https://github.com/github/copilot-cli/blob/main/changelog.md) 的 Breaking Change 條目，而非直接跳版。

## 9.3 常見問題（FAQ）

| 問題 | 解決方案 |
|------|---------|
| Copilot 回應太慢 | 1. 檢查網路連線<br>2. 使用 `/compact` 壓縮 context<br>3. 切換到更快的模型 |
| Context 用完 | 使用 `/compact` 或開啟新 session |
| Agent 不準確 | 1. 改善 custom instructions<br>2. 使用 @ 引用相關檔案<br>3. 使用 Plan Mode |
| MCP Server 無法連線 | 1. `/mcp` 檢查狀態<br>2. 驗證 `.mcp.json` 設定<br>3. `/mcp reload` 重新載入 |
| 無法建立 PR | 1. 確認 GitHub Token 權限<br>2. 確認 Repository 權限 |
| 升級後行為改變 | 1. 檢查 Changelog（`/changelog`）<br>2. 更新 custom instructions |
| 遠端 Session 無法連線 | 1. 確認組織策略未封鎖<br>2. 使用 `--remote` 啟動<br>3. 確認 ACP 伺服器在 localhost |
| MCP OAuth 認證失敗 | 使用 `/mcp auth` 重新認證 |
| Session 排序混亂 | 在 Session 選擇器中按 `s` 切換排序方式 |
| 「Premium Requests」相關說明找不到了 | 2026-06-01 起已改為 AI Credits 計費模式（見第 9.4 節），請更新內部文件中殘留的 Premium Requests 用語 |
| AI Credits 用盡但沒有自動降級模型 | 新計費模式已取消額度用盡後的降級備援；用 `/usage` 確認額度、`/limits` 預先設定 Session 上限、聯繫管理員調整組織 Credit 池 |

## 9.4 效能與成本考量

> 🔴 **重大計費模式變革（2026-06-01 生效）**：GitHub Copilot **全面廢除 Premium Request Units（PRU）機制**，改採 **Usage-based Billing（GitHub AI Credits）**。若您的企業文件、預算試算表仍沿用「Premium Requests」概念，**必須立即更新**，因為配額估算方式、超額行為、方案內含額度都已完全不同。

### AI Credits 計費模式

- 計費單位改為 **GitHub AI Credits**（1 Credit = US$0.01），按 **Token 實際消耗量**（輸入／輸出／快取 Token，依各模型 API 公示費率折算）計費，取代舊制按「請求次數 × 模型乘數」的方式
- **程式碼自動完成（Inline Completions）與 Next-edit 建議不消耗 Credits**，維持免費
- **不再提供「額度用盡後自動降級模型」的備援體驗**——這是與舊制最大的行為差異，額度用盡後互動會直接中止，而非悄悄換成更弱的模型

### 方案與內含額度（截至 2026-08 查證）

| 方案 | 月費 | 內含 AI Credits | 備註 |
|------|------|------------------|------|
| Pro | $10/月 | $10 | 座位定價不變，月繳自動遷移 |
| Pro+ | $39/月 | $39 | 年繳用戶保留原定價至到期，可提前轉換並按比例退款 |
| Business | $19/使用者/月 | $19 | 企業方案 |
| Enterprise | $39/使用者/月 | $39 | 需另搭配 GitHub Enterprise Cloud（約 $21/使用者/月），實際總成本約 $60/使用者/月 |

> 📝 過渡期優惠：既有企業客戶於 2026 年 6-8 月獲得額外推廣額度（Business +$30、Enterprise +$70），屬一次性措施，企業預算規劃不應假設長期延續。

### 大上下文視窗對成本的影響（2026-06-04 起）

Copilot 新增 **100 萬 Token 上下文視窗**與可配置推理層級（VS Code / CLI / App 三處同步），可將整個大型 Monorepo 或長文件一次載入單一對話，但因計費已改為 Token 制，**使用大上下文視窗會顯著提高 AI Credit 消耗**。建議僅在真正需要跨大量檔案理解的任務中啟用大 Context Tier，日常任務維持預設層級（約 200K Token）。

### 節省 AI Credits 的方法

1. **合併相關任務到一次 Prompt**（而非多次小任務）
2. **使用 `/compact` 壓縮 Context**（減少 Token 消耗；Infinite Sessions 已會自動處理，非必要不需手動觸發）
3. **善用 Plan Mode**（一次規劃好再執行，避免反覆修改）
4. **使用 Custom Instructions**（減少每次 Prompt 的重複說明）
5. **謹慎使用大上下文視窗 / 高推理層級**（僅在真正需要時開啟）
6. **善用 `/limits` 為單一 Session 設定 AI Credit 上限**（見 8.6 節），避免長任務失控耗用預算
7. **`/chronicle cost-tips`**：取得個人化的 Token 用量與省成本建議

### 企業預算治理

- 管理員可透過**組織 Credit 池共享**與**預算控制**功能，集中管理團隊 AI Credits 用量，避免個別開發者超支
- 建議在 GitHub Actions 中改用內建 `GITHUB_TOKEN`（`permissions: copilot-requests: write`，見 3.4 節），讓 CI/CD 消耗的 Credits 直接歸屬組織帳單，便於成本歸因

### 監控使用量

```bash
# 在互動式介面中查看使用統計（含 Session 與週限額進度條）
/usage
# 顯示：AI Credits 使用量、session 時長、編輯行數、Token 統計

/context
# 顯示：Context Window 使用情況

# 個人化省成本建議
/chronicle cost-tips
```

## 9.5 自動更新與發佈頻道

### 自動更新機制

```bash
# 查看更新說明並執行更新
/update

# 查看更新說明（非互動式）
copilot update

# 檢查目前版本
copilot --version

# 升級（各平台）
/upgrade    # 互動式內建指令
```

### 發佈頻道（v1.0.29+）

| 頻道 | 說明 | 適用對象 |
|------|------|---------|
| **stable** | 穩定版（預設） | 一般使用者、企業環境 |
| **nightly** | 每日建置版 | 功能預覽、搶先體驗 |

```bash
# 安裝 nightly 頻道
npm install -g @github/copilot@nightly

# 查看 nightly 版本資訊
copilot --version
# 顯示如：1.0.40-nightly.2026.04.28

# 回到穩定版
npm install -g @github/copilot@latest
```

### 企業更新策略

| 策略 | 說明 | 建議 |
|------|------|------|
| **逐步推出** | 先在開發團隊測試，再推廣至全組織 | ✅ 推薦 |
| **版本固定** | CI/CD 環境鎖定特定版本 | ✅ 推薦 |
| **自動更新** | 開發機器使用 stable 頻道自動更新 | ⚠️ 需監控 |
| **Nightly 預覽** | 指定人員使用 nightly 提前驗證 | ✅ 推薦 |

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
| `/mcp registry` | 從 MCP Registry 搜尋並安裝伺服器（v1.0.64+） |
| `/lsp` / `/lsp show` | 查看 LSP Server 狀態 |
| `/security-review` | 安全漏洞審查，v1.0.64+ 起全使用者開放 |
| `/refine` | 將雜亂的口語 Prompt 改寫成清楚版本（v1.0.70+） |

#### Session 管理

| 指令 | 說明 |
|------|------|
| `/new [prompt]` | 開始新 Session（舊 Session 保留於背景） |
| `/clear [prompt]` | 完全放棄目前 Session |
| `/resume` | 恢復之前的 Session |
| `/rename <name>` | 重新命名目前 Session（不帶參數自動生成） |
| `/session` | 查看 Session 資訊（含貢獻圖表） |
| `/session delete` | 刪除指定 Session（v1.0.35+） |
| `/session delete-all` | 刪除所有 Session（v1.0.35+） |
| `/restart` | 熱重啟 CLI（保留 Session） |
| `/fork`（別名 `/branch`） | 將目前 Session 分叉成獨立新 Session（v1.0.45+） |
| `/worktree`（別名 `/move`） | 建立/切換 git worktree 並攜帶未提交變更（v1.0.66+，細節見 [5.5](#55-session-管理與對話引導)） |
| `/new-worktree` | 建立新 worktree 並直接開新對話（實驗性，v1.0.78+） |
| Session Sidebar：`n` / `x` | 側欄新建 / 關閉 Session（v1.0.76+ 起實驗性） |

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
| `/ask <question>` | 一次性查詢，不汙染 Context（v1.0.15+） |
| `/rewind` | 回溯到對話中的先前時間點（v1.0.38+） |
| `/bug` | 提交 Bug 報告（v1.0.15+） |
| `/continue` | 繼續先前的回應（v1.0.32+） |
| `/release-notes` | 產生版本發佈說明（v1.0.19+） |
| `/export` | 匯出 Session 內容（v1.0.23+） |
| `/reset` | 重置 CLI 狀態（v1.0.30+） |
| `/keep-alive` | 保持 Session 存活（v1.0.35+） |
| `/statusline` | 切換狀態列顯示（v1.0.37+） |
| `/footer` | 切換頁尾顯示（v1.0.37+） |
| `/env` | 查看環境變數資訊（v1.0.20+） |

#### Context 與記憶

| 指令 | 說明 |
|------|------|
| `/compact [hint]` | 手動壓縮 Context（可帶自訂提示） |
| `/context` | 查看 Token 使用量 |
| `/usage` | 查看 Session 使用統計（請求數、Token、程式碼變更量） |
| `/instructions` | 查看與切換 Custom Instructions 檔案 |
| `/skills` / `/skills add`（或 `copilot skill`） | 管理 Skills（v1.0.65+ 支援檔案/URL/目錄來源） |
| `/remote` | 遠端控制管理（已 GA，v1.0.25+ 起提供指令） |
| `/memory on\|off\|show` | 管理 Copilot Memory（v1.0.49+） |
| `/limits` | 設定/檢視 AI Credits Session 額度上限 |
| `/voice devices` | 選擇並保存語音輸入的麥克風裝置（v1.0.71+） |
| `/every` / `/after` | 定期／延遲排程執行 Prompt（Prompt Scheduling） |
| `/chronicle search\|cost-tips\|skills review` | 搜尋歷史 Session、省成本建議、審查自動產生的 Skill 草稿 |
| `/rubber-duck` | 手動呼叫 Rubber Duck 批評代理（見 [4.13](#413-rubber-duck-建設性批評代理)） |

#### 權限與安全

| 指令 | 說明 |
|------|------|
| `/yolo` / `/allow-all` | 啟用全部工具權限（**危險！**） |
| `/allow-all on\|off\|show\|auto` | 互動式權限管理（`auto` 為安全判斷自動放行，需 `/experimental on`，v1.0.35+/v1.0.69+） |
| `/permissions [default\|assisted\|allow-all\|show\|reset]` | 切換核准模式（v1.0.51+/v1.0.78+） |
| `/reset-allowed-tools` | 重置已授予的工具權限 |
| `/add-dir <path>` | 新增受信任目錄 |
| `/list-dirs` | 查看目前已允許的目錄清單 |
| `/cwd <path>` 或 `/cd <path>` | 切換工作目錄 |
| `/sandbox enable` | 啟用本機 Sandbox 隔離 |
| `/sandbox policy` | 檢視目前生效的 Sandbox 政策（v1.0.79+） |

#### 擴充與插件

| 指令 | 說明 |
|------|------|
| `/plugin` | Plugin 管理（install / update / uninstall / list） |
| `/plugin marketplace add\|list\|remove` | Marketplace 管理（v1.0.71+ 新增子指令） |
| `/plugins` | 精細啟用/停用 Plugin 內個別元件（plugins/instructions/agents/LSP/hooks，v1.0.76+） |
| `/extensions`（別名 `/extension`） | 查看、啟用、停用 Extensions |
| `/app` | 開啟 GitHub App 或瀏覽器 fallback（v1.0.62+） |

#### 輔助工具

| 指令 | 說明 |
|------|------|
| `/copy` | 複製最近一次回應到剪貼簿 |
| `/share` / `/share gist` | 匯出 Session 為 Markdown 或 Gist |
| `/share html` | 匯出為自包含互動式 HTML 檔案（v1.0.15+） |
| `/feedback` | 提交回饋 |
| `/changelog` | 查看版本更新日誌（支援 `last N`、`since <version>`、`summarize`） |
| `/version` | 顯示 CLI 版本並檢查更新 |
| `/update` | 查看更新說明並執行更新 |
| `/upgrade` | 執行 CLI 升級（v1.0.29+） |
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
| `Shift + Tab` | 三段循環模式：**standard → plan → autopilot**（官方指令參考頁確認之最新行為） |
| `Tab` | 向前循環模式 |
| `Esc` | 終止操作 / 拒絕工具 / 清除輸入 |
| `Double-Esc` | 開啟 Timeline Picker，可回溯到對話歷史**任一時間點**（不只上一個快照，等同 `/rewind`） |
| `Ctrl + T` | 切換顯示/隱藏推理過程 |
| `Ctrl + R` | 反向搜尋指令歷史（如 Bash） |
| `Ctrl + C` | 中斷執行 / 清除輸入 |
| `Ctrl + D` | 在空 Prompt 時退出 CLI |
| `Ctrl + Z` | 暫停 CLI（Unix，`fg` 恢復） |
| `Ctrl + L` | 清空畫面 |
| `Ctrl + X, Ctrl + E` | 在外部編輯器中編輯 Prompt |
| `Ctrl + X, B` | 將目前任務轉為背景執行（v1.0.33+） |
| `Ctrl + X, /` | Prompt 輸入中途執行斜線指令 |
| `Ctrl + Y` | 在終端編輯器中編輯 Plan |
| `Ctrl + G` | 在外部編輯器中編輯 / 關閉 UI 元素 |
| `Ctrl + F` / `Ctrl + B` | 頁面下 / 上捲動（Alt Screen） |
| `Ctrl + A` / `Ctrl + E` | 行首 / 行尾 |
| `Ctrl + K` | 刪除到行尾（游標在行尾時合併行） |
| `Ctrl + N` / `Ctrl + P` | 等同上 / 下方向鍵 |
| `Ctrl + O` | 展開最近 Timeline |
| `Ctrl + S` | Stash / Pop 目前 Prompt 內容（比照 Claude Code，v1.0.60+ 行為變更） |
| `Ctrl + V` / `Alt + V` | 從剪貼簿貼上附件 / 圖片附件 |
| `Ctrl + Enter` / `Ctrl + Q` | Agent 忙碌時將訊息排入佇列 |
| `Shift + Enter` / `Alt + Enter` | 輸入框內換行 |
| `$` | 把終端機交還給真正的互動式 Shell |
| `s` | 在 Session 選擇器中循環排序（v1.0.37+） |
| `j` / `k` | Vim 風格導航（上/下選擇，v1.0.34+） |
| `x` | 在 Session 選擇器中刪除 Session（v1.0.35+） |
| `n` | Sessions Sidebar 新建 Session（v1.0.76+） |
| `!<command>` | 直接執行 shell 指令 |
| `&<prompt>` | 等同 `/delegate`（非同步委派） |
| `@<path>` | 引用檔案內容（支援絕對/相對/父目錄/home 路徑） |
| `#` | 參照 GitHub Issue / PR / Discussion |

### 命令列選項

#### 執行模式

| 選項 | 說明 |
|------|------|
| `-p, --prompt "..."` | 程式化模式（執行完即退出） |
| `--continue` | 繼續最近的 Session（偏好目前目錄，v1.0.35+） |
| `--resume [id]` | 選擇恢復 Session（支援 Session ID / Task ID / 名稱） |
| `--connect <session-id>` | 直接連接遠端 Session（v1.0.32+） |
| `--name <name>` | 以名稱啟動 Session（v1.0.35+） |
| `--agent=<name>` | 使用指定 Agent |
| `--model <name>` | 指定模型 |
| `--mode <mode>` | 設定互動模式（ask / plan / autopilot，v1.0.30+） |
| `--autopilot` | 直接進入 Autopilot 模式（v1.0.30+） |
| `--plan` | 直接進入 Plan 模式（v1.0.30+） |
| `--effort, --reasoning-effort <level>` | 設定推理強度 |
| `--experimental` / `--no-experimental` | 啟用 / 停用實驗性功能 |
| `--remote` | 啟用遠端控制（已 GA） |
| `--banner` | 顯示啟動動畫 |
| `--print-debug-info` | 印出除錯資訊並退出（v1.0.27+） |
| `--session-idle-timeout <sec>` | Session 閒置逾時時間（v1.0.35+） |
| `--session-id=<id>` | 恢復已知 Session/Task，或以指定 UUID 開新 Session（v1.0.51+） |
| `-r` | `--resume` 的簡寫（v1.0.60+） |
| `-C <directory>` | 啟動前先切換工作目錄，比照 `git -C`（v1.0.43+） |
| `--worktree [name]` / `-w` | 建立或重用 git worktree 並在其中啟動 Session（實驗性，v1.0.64+） |
| `--attachment <path>` | 於 `-p`/`--prompt` 模式附加檔案（v1.0.44+） |
| `--cloud` | 於雲端代管的隔離 Sandbox 環境中執行 Session（Public Preview） |
| `--sandbox` / `--no-sandbox` | 針對單次 Session 開關本機 Shell Sandbox（v1.0.70+） |
| `--list-env` | 於 Prompt 模式記錄已載入的 Plugin/Agent/Skill/MCP Server（適合 CI 驗證環境設定） |
| `--ahp` | 掛載至 Agent Host Protocol 主機（新興協定，Pre-release，見 [4.11](#411-acpagent-client-protocol與-copilot-sdk)） |

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
| `--acp` | 啟動 ACP（Agent Client Protocol）伺服器（Public Preview） |
| `--server` | 伺服器模式 |
| `--config-dir <dir>` | ⚠️ **已棄用**（v1.0.40 起標示，v1.0.60 完成 Plugin 子指令傳遞），改用 `COPILOT_HOME` 環境變數 |
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
| `copilot help monitoring` | OpenTelemetry 監控說明（v1.0.4+） |
| `copilot login` | 子命令：登入 |
| `copilot version` | 子命令：查看版本 |
| `copilot update` | 子命令：更新 |
| `copilot plugin` | 子命令：Plugin 管理（非互動） |
| `copilot mcp` | 子命令：MCP 管理（非互動，v1.0.21+） |
| `copilot completion` | 子命令：Shell 自動完成設定（v1.0.12+） |

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
| `COPILOT_GH_HOST` | 指定 GitHub Enterprise Server 主機（v1.0.15+） |
| `COPILOT_AGENT_SESSION_ID` | 目前 Agent Session ID（自動設定於子進程，v1.0.20+） |
| `COPILOT_DISABLE_TERMINAL_TITLE` | 停用 CLI 自動設定的終端標題（v1.0.25+） |
| `COPILOT_PLUGIN_DIR_ONLY` | 限制僅從指定目錄載入 Plugin（v1.0.49+） |
| `COPILOT_ENABLE_HTTP2` | 設為 `1` 啟用 HTTP/2 傳輸（v1.0.57 起預設改為 HTTP/1.1 以提升可靠性） |
| `GITHUB_TOOLSETS` | 控制內建 GitHub MCP Server 啟用的工具集（見 [5.4](#54-與其他工具整合)） |

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
| `config.json` | `~/.copilot/config.json` | 全域設定（內部狀態） |
| `settings.json` | `~/.copilot/settings.json` | 使用者設定（v1.0.35+ 從 config.json 分離） |
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
| MCP 設定 | `.mcp.json` | 工作區 MCP 設定（**v1.0.22+ 唯一來源**） |
| ~~MCP 設定~~ | ~~`.vscode/mcp.json`~~ | ~~已棄用（v1.0.22+）~~ |
| ~~DevContainer MCP~~ | ~~`.devcontainer/devcontainer.json`~~ | ~~已不再作為 MCP 來源（v1.0.22+）~~ |

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
| **v1.0.11** | **2026-03-23** | MCP 政策封鎖警告；Monorepo 完整支援 |
| v1.0.12 | 2026-03-24 | `copilot completion`；`/rename` 自動命名 |
| v1.0.15 | 2026-03-28 | `/ask` 指令；`/share html`；MCP OAuth；`/bug`；`postToolUseFailure` Hook |
| v1.0.16 | 2026-03-30 | `PermissionRequest` Hook；程式化工具權限決策 |
| v1.0.18 | 2026-04-01 | Critic Agent（實驗性）；`notification` Hook |
| v1.0.19 | 2026-04-03 | `/release-notes`；OTEL 強化；MCP 啟用/停用持久化 |
| v1.0.20 | 2026-04-04 | `/env` 指令；OTEL 推理 Token 追蹤 |
| v1.0.21 | 2026-04-06 | `copilot mcp` 非互動式管理 |
| v1.0.22 | 2026-04-08 | `.mcp.json` 唯一 MCP 設定來源；`sessionEnd` Hook |
| v1.0.25 | 2026-04-12 | `/remote` 遠端控制；MCP Registry 安裝 |
| v1.0.26 | 2026-04-13 | ACP 綁定 localhost；Plugin Hook 環境變數 |
| v1.0.27 | 2026-04-14 | `--print-debug-info` 旗標 |
| v1.0.29 | 2026-04-17 | Nightly 發佈頻道；`/upgrade` 指令 |
| v1.0.30 | 2026-04-18 | `--mode`、`--autopilot`、`--plan` 旗標；`/reset` 指令 |
| v1.0.32 | 2026-04-21 | `--connect` 直接連接；`/continue`；短 Session ID |
| v1.0.33 | 2026-04-22 | `Ctrl+X → B` 背景任務 |
| v1.0.34 | 2026-04-23 | `j`/`k` Vim 導航 |
| v1.0.35 | 2026-04-24 | `--name`；`--session-idle-timeout`；`/session delete`；`/keep-alive`；`settings.json` 分離；`--continue` 偏好目前目錄 |
| v1.0.36 | 2026-04-25 | 雙次 Esc 確認 allow-all 切換 |
| v1.0.37 | 2026-04-27 | 位置感知權限；Session 排序（`s` 鍵）；`/statusline`；`/footer` |
| v1.0.38 | 2026-04-27 | `/rewind` 回溯指令 |
| v1.0.39 | 2026-04-28 | HTTP Hook 支援；穩定性與效能改進 |
| v1.0.40~44 | 2026-05-01~08 | `--attachment` 旗標；MCP `client_credentials` 無頭驗證；Autopilot 預設限制 5 次延續；`--config-dir` 標示棄用 |
| v1.0.45~48 | 2026-05-11~14 | `/fork` 指令；`/autopilot` 模式切換；OTEL 改採 GenAI 語意慣例 |
| **v1.0.49** | **2026-05-18** | `/memory on\|off\|show`；`/chronicle search`；`/rubber-duck` 手動呼叫；MCP `/mcp search`（實驗性） |
| v1.0.51~55 | 2026-05-20~28 | `--session-id`；自訂狀態列；`/security-review`；`preMcpToolCall` Hook；`/autopilot <objective>`（`/goal`）；Opus 4.8 上線 |
| **v1.0.58** | **2026-06-02** | **Rubber Duck 預設啟用**；`/every`/`/after` 排程；Copilot App 與 Copilot SDK（六語言）**同步 GA**；語音輸入 GA |
| v1.0.60~61 | 2026-06-05~09 | Anthropic 最大推理層級開放所有方案；`ctrl+s` 改為 Stash/Pop；`--config-dir` 走向棄用；Claude Fable 5 上線 |
| v1.0.62~65 | 2026-06-13~24 | Shell 工具改輕量 spawn；`/subagents`；`copilot skill`；企業 forward proxy Kerberos 驗證 |
| **v1.0.66** | **2026-06-30** | Claude Opus 4.8 Fast 上線，**同時棄用 Opus 4.6 Fast**；`/worktree`（`/move`）；`/pr auto`／`/pr automerge` |
| v1.0.67~69 | 2026-06-30~07-07 | Claude Sonnet 5 上線；`/delegate --base`；`/allow-all auto` 需實驗性模式 |
| **v1.0.70** | **2026-07-09** | GPT-5.6 上線；`--sandbox`/`--no-sandbox`；`/refine`；受信任 Repo 可鎖定模型/Effort/Context Tier 設定 |
| v1.0.71~74 | 2026-07-16~23 | Plan Mode 硬性封鎖工作區修改；Subagent 巢狀深度預設 6→4；`/voice devices`；Open Plugin Spec v1 支援 |
| **v1.0.75~76** | **2026-07-24~29** | Claude Opus 5、Grok 4.5 上線；`/plugins` 精細啟用/停用；Sessions Sidebar（實驗性） |
| v1.0.77~78 | 2026-07-30~08-03 | 瀏覽器 OAuth 登入成為本地預設；MDM 強制 Sandbox 政策；Timeline 顯示工具耗時；Managed Settings fail open |
| **v1.0.79** | **2026-08-10** | ⚠️ Sandbox 設定鍵 Breaking Change；`--plan` + `--mode autopilot` 組合；Kimi K3 上線；`/model` 改為分組顯示且 Session-scoped |
| **v1.0.80** | **2026-08-14** | **目前最新版**；模型設定更新 |

> 📝 **本表為精選里程碑**，並非逐版完整清單（v1.0.39 至 v1.0.80 之間實際發布約 40 個版本，多為修復與小幅強化）。完整版本紀錄請參閱 [changelog.md](https://github.com/github/copilot-cli/blob/main/changelog.md)。

## 10.7 已移除與棄用項目

| 項目 | 移除/棄用版本 | 替代方案 |
|------|---------|---------|
| `.vscode/mcp.json` 作為 MCP 設定來源 | v1.0.22 | 使用 `.mcp.json` |
| `.devcontainer/devcontainer.json` 作為 MCP 設定來源 | v1.0.22 | 使用 `.mcp.json` |
| `codex-mini` 模型 | v1.0.15 | 使用 `auto` 或其他可用模型 |
| `gpt-5.1-codex` / `gpt-5.1-codex-mini` / `gpt-5.1-codex-max` 模型 | v1.0.15 | 使用 GPT-5.2 Codex 或更新版本 |
| `gemini-3-pro-preview` 模型 | v1.0.13 | 使用 Gemini 3 Pro 或更新版本 |
| `--alt-screen` 旗標與 `alt_screen` 設定 | v1.0.12 | Alt Screen 現為永遠啟用 |
| 已棄用的 `marketplaces` Repository 設定 | v1.0.16 | 改用 `extraKnownMarketplaces` |
| `--config-dir` 旗標 | v1.0.40 標示棄用，v1.0.60 完成過渡 | 改用 `COPILOT_HOME` 環境變數 |
| Claude Opus 4.6 Fast 模型 | v1.0.66 | 改用 Claude Opus 4.8 Fast |
| Subagent 最大巢狀深度預設值（6） | v1.0.71 | 預設降為 4，可用 `subagents.maxDepth` 調整（最高 128） |
| `allowDevToolCaches` 設定鍵 | v1.0.79（**Breaking，無自動遷移**） | 改用 `allowDevToolAccess` |
| `sandbox.gitAuth` / `sandbox.ghAuth` 設定鍵 | v1.0.79（**Breaking，無自動遷移**） | 改用 `sandbox.auth.git` / `sandbox.auth.gh` |
| **Premium Requests（PRU）計費機制** | 2026-06-01（全面停用） | 改用 **AI Credits（Usage-based Billing）**，詳見第 9.4 節 |
| `o4-mini` 模型（已移除後重新新增） | 短暫移除 | 已重新可用 |
| `--yolo` 旗標（部分場景） | 未正式棄用 | 建議使用 `--allow-all-tools`；企業可用 `permissions.disableBypassPermissionsMode` 完全封鎖 |

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
- [ ] 定期更新 Copilot CLI 到最新版本（留意 Breaking Change，見 10.7）
- [ ] 確認第三方 MCP Server 政策與組織允許清單一致
- [ ] 確認 UNC 路徑防護已啟用（v1.0.5+ 預設啟用）
- [ ] Clone 不受信任的 Repository 前，先人工檢視是否存在 `.mcp.json`（TrustFall 風險，見 6.3.1）
- [ ] 不假設 Content Exclusions 涵蓋 CLI／Coding Agent／Agent Mode，另行制定 Trusted Directories 規則
- [ ] 評估啟用 [4.18 Sandbox](#418-sandbox-安全沙箱本機雲端) 作為多層防禦的一環
- [ ] GitHub Actions 中改用內建 `GITHUB_TOKEN`（`copilot-requests: write`），避免簽發長效 PAT

## 📊 日常使用檢查清單

- [ ] 使用 `/usage` 監控 AI Credits 消耗（2026-06 起計費模式已由 Premium Requests 改為 AI Credits）
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
- [ ] 評估 Copilot SDK（六語言已 GA）將 Agent 能力內嵌進自建應用程式
- [ ] 使用 `/worktree` / `/fork` 管理多條並行工作
- [ ] 建立團隊使用規範與最佳實務文件

---

> 📝 **文件維護**  
> - 本手冊基於 GitHub Copilot CLI **v1.0.80**（2026 年 8 月 14 日）撰寫，最後更新：2026 年 8 月 14 日
> - 官方 Repository：https://github.com/github/copilot-cli
> - 產品頁面：https://github.com/features/copilot/cli
> - 官方文件：https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli
> - 安裝指南：https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli
> - 使用指南：https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli
> - CLI 指令參考：https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
> - 最佳實務：https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices
> - Changelog：https://github.com/github/copilot-cli/blob/main/changelog.md
> - Copilot SDK：https://github.com/github/copilot-sdk
> - GitHub MCP Registry：https://github.com/mcp
> - GitHub Skills 互動課程：https://github.com/skills/create-applications-with-the-copilot-cli
> - 建議每季度檢視並更新本手冊內容，並優先核對 changelog.md 中的 Breaking Change 條目
> - 建議每季度檢視並更新本手冊內容

