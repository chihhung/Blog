+++
date = '2026-03-24T14:39:10+08:00'
draft = false
title = 'Oh My Openagent（Oh My OpenCode, OMO）教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# oh-my-openagent（Oh My OpenCode, OMO）教學手冊

> **版本**：v2.0｜**最後更新**：2026-03-24  
> **對應 OMO 版本**：v3.12.3（154 releases）  
> **適用對象**：資深工程師、架構師、技術主管  
> **定位**：企業級 AI Agent Harness 教學手冊  
> **GitHub**：[https://github.com/code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)  
> **官網**：[https://ohmyopenagent.com/](https://ohmyopenagent.com/)

---

## 📑 目錄

- [第 1 章：總覽（Overview）](#第-1-章總覽overview)
- [第 2 章：系統架構設計（Architecture）](#第-2-章系統架構設計architecture)
- [第 3 章：安裝與環境建置（Installation）](#第-3-章安裝與環境建置installation)
- [第 4 章：設定與專案初始化（Configuration）](#第-4-章設定與專案初始化configuration)
- [第 5 章：Agent 系統詳解（Discipline Agents）](#第-5-章agent-系統詳解discipline-agents)
- [第 6 章：開發流程（ultrawork / Plan / Build）](#第-6-章開發流程ultrawork--plan--build)
- [第 7 章：Web Application 實戰](#第-7-章web-application-實戰)
- [第 8 章：測試與品質（Testing & Quality）](#第-8-章測試與品質testing--quality)
- [第 9 章：維運與除錯（Maintenance）](#第-9-章維運與除錯maintenance)
- [第 10 章：升級與版本管理（Upgrade）](#第-10-章升級與版本管理upgrade)
- [第 11 章：安全（SSDLC）](#第-11-章安全ssdlc)
- [第 12 章：團隊導入策略（Enterprise Adoption）](#第-12-章團隊導入策略enterprise-adoption)
- [第 13 章：最佳實務（Best Practices）](#第-13-章最佳實務best-practices)
- [第 14 章：常見問題（FAQ）](#第-14-章常見問題faq)
- [第 15 章：附錄（Appendix）](#第-15-章附錄appendix)
- [檢查清單（Checklist）](#檢查清單checklist)

---

## 第 1 章：總覽（Overview）

### 1.1 什麼是 oh-my-openagent（OMO）

oh-my-openagent（簡稱 OMO，又稱 Oh My OpenCode）是由 [code-yeongyu](https://github.com/code-yeongyu) 開發的 **OpenCode 增強插件（Plugin）**，以 TypeScript 編寫（94.2%），專為將 [OpenCode](https://github.com/anomalyco/opencode)（開源終端 AI 編碼代理）升級為一個具備**紀律型多代理協作（Discipline Agents）**能力的 AI 開發團隊。

> **重要**：OMO 並非一個獨立框架，而是 **OpenCode 的插件**。它透過 OpenCode 的插件系統運行，並與 Claude Code 完全相容——所有 Claude Code 的 hooks、commands、skills、MCPs 和 plugins 都可以直接使用。

**核心統計（截至 2026 年 7 月）**：

| 指標 | 數值 |
|------|------|
| GitHub Stars | 42.9k |
| Forks | 3.2k |
| Contributors | 165 |
| Releases | 154 |
| 最新版本 | v3.12.3 |
| 授權方式 | SUL（Sisyphus Use License） |
| 主要語言 | TypeScript (94.2%), HTML (5.3%) |

**核心特性**：

| 特性 | 說明 |
|------|------|
| Discipline Agents | 內建專業 Agent：Sisyphus（編排）、Hephaestus（深度工作）、Prometheus（規劃）、Oracle（驗證）等 |
| ultrawork / ulw | 一鍵啟動所有 Agent 協作，任務不完成不停止 |
| Hash-Anchored Edits | LINE#ID 內容雜湊驗證每次修改，零 stale-line 錯誤 |
| Background Agents | 同時啟動 5+ 個專家 Agent 平行工作 |
| Category-Based Routing | 基於任務類別（visual、deep、quick、ultrabrain）自動匹配最佳模型 |
| Skills 系統 | 技能攜帶專屬 MCP 伺服器，按需啟動 |
| Claude Code 相容 | 完全支援 hooks、commands、skills、MCPs、plugins |
| 多模型編排 | Claude / GPT / Kimi / GLM / Gemini，不鎖定單一供應商 |
| /init-deep | 自動生成分層 AGENTS.md，實現精準上下文注入 |

### 1.2 OMO 的設計理念

OMO 的核心理念可以用一句話概括：

> "Models get cheaper every month. Smarter every month. No single provider will dominate. We're building for that open market, not their walled gardens."

OMO 不綁定任何單一模型供應商，而是**編排所有模型的優勢**：

| 模型 | 用途 |
|------|------|
| Claude Opus 4.6 | 複雜編排、推理 |
| Kimi K2.5 | 編排替代方案 |
| GLM-5 | 編排備選 |
| GPT-5.4 | 推理、Agent 任務（xhigh/high/medium variants） |
| GPT-5.3-codex | 深度自主工作（Hephaestus） |
| Gemini 3.1 Pro | 創意任務 |
| Minimax | 速度需求 |

### 1.3 與傳統 AI Coding 工具差異

| 面向 | GitHub Copilot | Claude Code | Cursor | OMO |
|------|---------------|-------------|--------|-----|
| 互動方式 | 行內補全 / Chat | 終端 Agent | IDE 內建 | Multi-Agent 編排 |
| 上下文管理 | 單檔案 / @workspace | CLAUDE.md | .cursorrules | 分層 AGENTS.md + /init-deep |
| Agent 模型 | 單一 Agent | 單一 Agent | 單一 Agent | Discipline Agents（10+ 專家） |
| 模型支援 | OpenAI / Claude | Claude only | 多模型 | 任意模型（自動路由） |
| 自動化程度 | 被動建議 | 半自動 | 半自動 | ultrawork 全自動（不停止直到完成） |
| 編輯精度 | 標準 | 標準 | 標準 | Hash-Anchored（LINE#ID 驗證） |
| 平行能力 | 否 | 有限 | 否 | Background Agents（5+ 平行） |
| 開源 | 否 | 否 | 否 | 是（SUL License） |
| 適合場景 | 個人加速 | 個人/小團隊 | 個人/小團隊 | 企業級團隊協作 |

### 1.4 與 Agent Framework 比較

| 面向 | AutoGPT | CrewAI | Devin | OMO |
|------|---------|--------|-------|-----|
| 定位 | 通用 AI Agent | Multi-Agent 框架 | AI 軟體工程師 | AI Agent Harness（OpenCode 插件） |
| 聚焦 | 任務自動化 | 任務編排 | 軟體開發 | 軟體開發（終端原生） |
| Agent 設計 | 自定義 | Role-based | 封閉 | Discipline Agents（專家角色） |
| 模型鎖定 | 部分 | 部分 | 完全 | 無（多模型編排） |
| 編輯精度 | 低 | 低 | 中 | 高（Hashline） |
| 企業適用性 | 低 | 中 | 中 | 高（Hook 安全、權限控管） |
| 社群生態 | 活躍 | 成長中 | 封閉 | 活躍（42.9k Stars, 165 Contributors） |

### 1.5 適用場景

#### 企業級應用

- 金融系統（銀行核心系統、交易平台）開發
- 大型 Web Application（微服務架構）
- 需要多代理協作的複雜專案
- SSDLC 合規要求的開發流程
- 多語言/多框架混合專案

#### 團隊開發

- 大型 codebase 重構與遷移
- 自動化 code review 與品質控管
- 平行功能開發（Branch + Background Agents）
- 持續整合/持續交付（CI/CD）整合

#### 個人開發者

- 快速原型開發（ultrawork 一鍵啟動）
- 全端專案自動化
- 開源專案維護

> **使用者評價**：  
> "It made me cancel my Cursor subscription." — Arthur Guiot  
> "Knocked out 8000 eslint warnings with Oh My Opencode, just in a day" — Jacob Ferrari  
> "If Claude Code does in 7 days what a human does in 3 months, Sisyphus does it in 1 hour." — B, Quant Researcher

---

## 第 2 章：系統架構設計（Architecture）

### 2.1 OMO 整體架構圖

```mermaid
graph TB
    subgraph Developer["👨‍💻 開發者"]
        CLI["OpenCode Terminal / CLI"]
    end

    subgraph OMO["oh-my-openagent Plugin"]
        Core["OMO Core Engine<br/>(TypeScript)"]
        
        subgraph Agents["Discipline Agents"]
            Sisyphus["🏛️ Sisyphus<br/>Main Orchestrator"]
            Hephaestus["🔨 Hephaestus<br/>Deep Worker"]
            Prometheus["📋 Prometheus<br/>Strategic Planner"]
            Oracle["🔮 Oracle<br/>Verifier"]
            Atlas["🗺️ Atlas<br/>Multi-Task Orchestrator"]
            Librarian["📚 Librarian<br/>Docs/Code Search"]
            Explore["🔍 Explore<br/>Fast Codebase Grep"]
            Looker["👁️ Multimodal Looker<br/>Visual Analysis"]
            Metis["🧠 Metis<br/>Plan Consultant"]
            Momus["📝 Momus<br/>QA Reviewer"]
        end

        subgraph Features["核心功能"]
            Ultrawork["⚡ ultrawork / ulw"]
            Hashline["🔗 Hash-Anchored Edits"]
            BgAgents["🖥️ Background Agents"]
            Skills["🎯 Skills System"]
            Hooks["🪝 Hooks (25+)"]
            MCPs["🔌 Built-in MCPs"]
            TodoEnf["✅ Todo Enforcer"]
            RalphLoop["🔁 Ralph Loop"]
            IntentGate["🚪 IntentGate"]
        end

        subgraph Tools["工具層"]
            LSP["LSP Integration"]
            AST["AST-Grep"]
            Tmux["Tmux Terminal"]
            Session["Session Manager"]
        end

        Context["Context Manager<br/>AGENTS.md / /init-deep"]
    end

    subgraph Models["LLM 模型層"]
        Claude["Claude Opus 4.6"]
        GPT54["GPT-5.4"]
        GPT53["GPT-5.3-codex"]
        Kimi["Kimi K2.5"]
        GLM["GLM-5"]
        Gemini["Gemini 3.1 Pro"]
    end

    subgraph Integration["整合層"]
        Git["Git / GitHub"]
        CICD["CI/CD Pipeline"]
        ClaudeCode["Claude Code 相容<br/>Hooks / Skills / MCPs"]
    end

    CLI --> Core
    Core --> Agents
    Core --> Features
    Core --> Tools
    Core --> Context
    Sisyphus -->|"delegates"| Hephaestus
    Sisyphus -->|"plans with"| Prometheus
    Sisyphus -->|"verifies via"| Oracle
    Sisyphus -->|"orchestrates"| Atlas
    Agents --> Models
    Agents --> Integration
```

### 2.2 Discipline Agents 設計

OMO 的 Agent 設計遵循「紀律型代理」（Discipline Agents）原則——每個 Agent 都針對特定模型的優勢進行調校，不做「通用 Agent」。

| Agent | 主模型 | 備選模型 | 職責 | 特色 |
|-------|--------|---------|------|------|
| **Sisyphus** | Claude Opus 4.6 | Kimi K2.5 / GLM-5 | 主編排器，規劃、委派、驅動任務完成 | 積極平行執行，不會中途停止 |
| **Hephaestus** | GPT-5.3-codex | — | 自主深度工作者，端到端執行 | 不需手把手指導，自行探索與實作 |
| **Prometheus** | Claude Opus 4.6 | Kimi K2.5 / GLM-5 | 戰略規劃者，面談式需求分析 | /start-work 觸發，建立完整計劃 |
| **Oracle** | GPT-5.4 high | — | 架構驗證、除錯 | ULW-Loop 強制驗證 |
| **Atlas** | Claude Sonnet | GPT-5.4 medium fallback | 多任務編排，Final Verification Wave | 管理 Boulder 持續執行 |
| **Metis** | GPT-5.4 high | — | 計劃顧問，QA 場景可執行性檢查 | 與 Prometheus 協作 |
| **Momus** | GPT-5.4 xhigh | — | QA 審查，場景可執行性驗證 | 模型路由 + QA 場景 |
| **Librarian** | — | — | 文件/程式碼搜尋 | 整合 Exa Web Search |
| **Explore** | — | — | 快速程式碼 grep | 輕量級搜尋 |
| **Multimodal Looker** | GPT-5.4 medium | — | 圖像分析、視覺理解 | HEIC/RAW/PSD 自動轉換 |
| **Sisyphus Junior** | — | GPT-5.4 / GPT-5.3-codex | 輕量編排 | GPT 特定路由 |

### 2.3 Category-Based Model Routing

Sisyphus 委派子任務時，不指定模型，而是指定**任務類別（Category）**，系統自動匹配最佳模型：

```mermaid
flowchart TD
    Sisyphus["Sisyphus 委派任務"] --> Category["指定任務類別"]
    
    Category -->|"visual-engineering"| VE["Frontend, UI/UX, Design"]
    Category -->|"deep"| Deep["自主研究 + 執行<br/>GPT-5.3-codex medium"]
    Category -->|"quick"| Quick["單檔修改, Typo"]
    Category -->|"ultrabrain"| UB["困難邏輯, 架構決策<br/>GPT-5.4 xhigh"]
    Category -->|"unspecified-high"| UH["一般高強度任務<br/>GPT-5.4 high"]
    Category -->|"business-logic"| BL["商業邏輯<br/>自定義分類"]
    
    VE --> Model1["自動匹配模型"]
    Deep --> Model2["自動匹配模型"]
    Quick --> Model3["自動匹配模型"]
    UB --> Model4["自動匹配模型"]
```

#### 模型 Fallback 鏈

Sisyphus 主鏈：
```
claude-opus-4-6 max → k2p5 → kimi-k2.5 → gpt-5.4 medium → glm-5 → big-pickle
```

> **設計原理**：Agent 說「需要什麼類型的工作」，Harness 挑選對應模型。`ultrabrain` 類別現在預設路由到 GPT-5.4 xhigh。使用者無需手動配置。

### 2.4 Hook 系統架構

OMO 提供 25+ 個內建 Hooks，在 Agent 生命週期的各個節點注入自定義行為：

```mermaid
sequenceDiagram
    participant User as 使用者
    participant Hook as Hook System
    participant Agent as Agent
    participant Tool as Tool

    User->>Agent: 送出請求
    Hook->>Agent: chat.params Hook（注入上下文）
    Hook->>Agent: chat.message Hook（處理訊息）
    Agent->>Tool: 呼叫工具
    Hook->>Tool: tool.pre Hook（工具前處理）
    Tool-->>Agent: 回傳結果
    Hook->>Agent: tool.post Hook（工具後處理）
    Agent-->>User: 回傳結果
    Hook->>Agent: session.idle Hook（閒置處理）
```

主要 Hook 類別：

| Hook 類別 | 說明 | 範例 |
|-----------|------|------|
| Context Injection | 自動注入 AGENTS.md、README | `context-injector` |
| Agent Behavior | 控制 Agent 行為 | `comment-checker`, `todo-enforcer` |
| Model Override | 模型切換 | `ultrawork-model-override` |
| Tool Enhancement | 工具增強 | `hashline-read-enhancer`, `hashline-edit` |
| Session Management | 會話管理 | `todo-continuation`, `ralph-loop` |
| Security | 安全控管 | `blocked-operations`, URL scheme validation |

### 2.5 與 Claude Code 生態整合

OMO 100% 相容 Claude Code 生態系統：

```mermaid
graph LR
    subgraph ClaudeCodeEcosystem["Claude Code 生態"]
        CCHooks["Hooks"]
        CCCommands["Commands"]
        CCSkills["Skills"]
        CCMCPs["MCPs"]
        CCPlugins["Plugins"]
    end

    subgraph OMO_Enhancements["OMO 增強"]
        DAgents["Discipline Agents"]
        UltraW["ultrawork"]
        HashL["Hashline Edits"]
        BgAg["Background Agents"]
        OMOHooks["25+ OMO Hooks"]
        OMOSkills["OMO Skills"]
    end

    ClaudeCodeEcosystem -->|"完全相容"| OMO_Enhancements
```

> **注意**：OMO 從 oh-my-opencode 改名為 oh-my-openagent（v3.11.0），兩個套件名稱都支援。配置檔偵測同時支援 `oh-my-opencode.json(c)` 和 `oh-my-openagent.jsonc`。

---

## 第 3 章：安裝與環境建置（Installation）

### 3.1 前置需求

| 軟體 | 需求 | 說明 |
|------|------|------|
| OpenCode | 最新版 | Go 語言編寫的終端 AI 編碼代理（必須先安裝） |
| Node.js | 18+ | 插件執行環境 |
| Bun | 最新版 | OMO 的構建與打包工具 |
| Git | 2.30+ | 版本控制 |
| tmux | 建議安裝 | 完整終端整合功能（REPL、Debugger、TUI） |

#### 可選但建議的訂閱方案

OMO 的 ultrawork 功能搭配以下訂閱即可良好運作：

| 服務 | 費用（美元/月） | 用途 |
|------|----------------|------|
| ChatGPT Subscription | $20 | GPT-5.x 模型（Hephaestus / Oracle） |
| Kimi Code Subscription | $0.99（限時） | Kimi K2.5（Sisyphus 備選） |
| GLM Coding Plan | $10 | GLM-5（Sisyphus 備選） |

> 若使用 pay-per-token，Kimi 和 Gemini 模型費用較低。

### 3.2 安裝步驟

#### 方法 1：讓 AI Agent 安裝（推薦）

將以下 Prompt 貼入你的 LLM Agent（Claude Code、AmpCode、Cursor 等）：

```
Install and configure oh-my-opencode by following the instructions here:
https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

#### 方法 2：手動安裝

```bash
# Step 1: 安裝 OpenCode（如尚未安裝）
# macOS / Linux
curl -fsSL https://opencode.ai/install.sh | bash

# Windows（PowerShell）
irm https://opencode.ai/install.ps1 | iex

# Step 2: 透過 OpenCode 安裝 OMO 插件
# 在 OpenCode 設定中加入插件
# 編輯 ~/.config/opencode/opencode.json 或 opencode.jsonc
```

將 `"oh-my-opencode"` 加入 `plugin` 陣列：

```jsonc
{
  "plugin": [
    "oh-my-opencode"
  ]
}
```

```bash
# Step 3: 啟動 OpenCode 驗證插件載入
opencode --version
# 插件應自動載入
```

#### 方法 3：從 LLM Agent 取得安裝指南

```bash
curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

### 3.3 安裝後驗證

```bash
# 執行 Doctor 指令檢查安裝狀態
# 在 OpenCode 會話中輸入：
/doctor

# Doctor 會檢查：
# - 插件版本
# - 已載入的 Agent
# - 模型連線狀態
# - LSP 伺服器與擴展偵測
# - 配置路徑
```

### 3.4 配置檔位置

OMO 使用 JSONC（JSON with Comments）格式，支援兩個層級的配置：

| 層級 | 路徑 | 說明 |
|------|------|------|
| 專案級 | `.opencode/oh-my-opencode.jsonc` | 專案特定配置（優先） |
| 專案級（替代） | `.opencode/oh-my-opencode.json` | JSON 格式 |
| 使用者級 | `~/.config/opencode/oh-my-opencode.jsonc` | 全域配置 |
| 使用者級（替代） | `~/.config/opencode/oh-my-opencode.json` | JSON 格式 |

> **Windows 補充**：Windows 上使用 `%LOCALAPPDATA%\opencode\` 或 `XDG_CONFIG_HOME` 環境變數指定的路徑。OMO v3.12.0+ 支援 `XDG_CONFIG_HOME` 在 Windows 上的使用。

### 3.5 Model Setup（Agent-Model Matching）

OMO 的 Agent-Model 匹配內建於安裝指南中。核心匹配規則：

```jsonc
// .opencode/oh-my-opencode.jsonc
{
  // Agent 模型覆蓋（可選，預設已由 OMO 自動匹配）
  "agents": {
    "sisyphus": {
      "model": "claude-opus-4-6"  // 預設：Claude Opus 4.6
    },
    "hephaestus": {
      "model": "gpt-5.3-codex"   // 預設：GPT-5.3 Codex
    },
    "oracle": {
      "model": "gpt-5.4"         // 預設：GPT-5.4
    }
  },

  // Background Tasks 並行限制
  "background_tasks": {
    "concurrency": 5  // 最多 5 個背景 Agent 同時執行
  }
}
```

### 3.6 常見安裝問題排除

| 問題 | 原因 | 解決方案 |
|------|------|---------|
| 插件未載入 | OpenCode 配置未加入 plugin | 在 `opencode.json` 的 `plugin` 陣列加入 `"oh-my-opencode"` |
| `pluginVersion is null` | 版本偵測問題 | 使用 `/doctor` 檢查，升級至 v3.12.0+ |
| 模型連線失敗 | API Key 未設定 | 在 OpenCode 設定中配置對應 Provider |
| Windows 彈出視窗 | `Bun.spawn` 問題 | OMO v3.9.0+ 已修復（`windowsHide`） |
| Cache 版本過期 | 舊版 cache | 執行 `/doctor` 自動修復或手動清除 cache |
| 配置無法儲存 | 權限或路徑問題 | 檢查 `~/.config/opencode/` 目錄權限 |

---

## 第 4 章：設定與專案初始化（Configuration）

### 4.1 JSONC 配置檔完整範例

```jsonc
// .opencode/oh-my-opencode.jsonc
// OMO 配置檔 - 支援註解與尾隨逗號
{
  // === Agent 配置 ===
  "agents": {
    // 覆蓋 Agent 模型（通常無需手動設定）
    "sisyphus": {
      "model": "claude-opus-4-6",
      "temperature": 0.3
    },
    "hephaestus": {
      "model": "gpt-5.3-codex"
    },
    // 自定義 Agent
    "custom_agents": {
      "banking-expert": {
        "name": "Banking Domain Expert",
        "model": "claude-opus-4-6",
        "system_prompt": "You are an expert in banking domain...",
        "permissions": ["read_files", "write_files"]
      }
    }
  },

  // === Skills 配置 ===
  "skills": {
    "enabled": [
      "playwright",      // 瀏覽器自動化
      "git-master",      // 原子提交、rebase surgery
      "frontend-ui-ux"   // 設計優先 UI
    ]
  },

  // === Hooks 配置 ===
  "disabled_hooks": [
    // 停用特定 Hook（預設全部啟用）
    // "hashline_edit"   // v3.10.0+ hashline_edit 預設停用
  ],

  // === Disabled Tools ===
  "disabled_tools": [
    // 停用特定工具
  ],

  // === Background Tasks ===
  "background_tasks": {
    "concurrency": 5,
    "stale_timeout_ms": 1200000,    // 20 分鐘
    "session_wait_ms": 60000        // 1 分鐘
  },

  // === Circuit Breaker（v3.12.0+）===
  "circuit_breaker": {
    "enabled": true,
    "max_consecutive_calls": 10
  },

  // === 實驗性功能 ===
  "experimental": {
    "aggressive_truncation": false,
    "auto_resume": false,
    "hashline_edit": false     // 需要手動啟用
  }
}
```

### 4.2 AGENTS.md 與 /init-deep

`AGENTS.md` 是 OMO 理解專案的核心文件。OMO 提供 `/init-deep` 指令自動生成**分層** AGENTS.md：

```bash
# 在 OpenCode 會話中執行
/init-deep
```

生成的分層結構：

```
project/
├── AGENTS.md                  ← 專案級上下文
├── src/
│   ├── AGENTS.md              ← src 目錄上下文
│   └── components/
│       └── AGENTS.md          ← 組件級上下文
├── tests/
│   └── AGENTS.md              ← 測試相關上下文
└── infra/
    └── AGENTS.md              ← 基礎設施上下文
```

Agent 會自動讀取相關層級的 AGENTS.md，**無需手動管理上下文注入**。

#### AGENTS.md 撰寫範例（企業級）

```markdown
# Project: Enterprise Banking Portal

## Overview
企業銀行入口網站，提供帳戶管理、轉帳、報表等功能。
服務 500 萬用戶，日均交易量 200 萬筆。

## Tech Stack
- **Backend**: Java 21 + Spring Boot 3.2 + Spring Security 6
- **Frontend**: Vue 3 + TypeScript + Tailwind CSS
- **Database**: Oracle 19c（主）+ Redis（快取）
- **Message Queue**: Apache Kafka
- **API Style**: RESTful + OpenAPI 3.0

## Architecture
- Clean Architecture（DDD）
- 微服務架構（12 services）

## Coding Standards
- Java: Google Java Style Guide
- No Lombok（公司規範）
- Constructor Injection only
- All dates: java.time.*

## Security Requirements
- OWASP Top 10 防護
- JWT 認證 + OAuth2
- AES-256 加密
- Rate Limiting

## Testing
- 單元測試覆蓋率 ≥ 80%
- JUnit 5 + Mockito
```

> **重要原則**：
> - 控制在 500-1000 行以內，避免浪費 Token
> - 不放敏感資訊（密碼、Key、內部 URL）
> - 使用 `/init-deep` 自動生成，人工微調

### 4.3 Skills 設計

Skills 不只是 Prompt——每個 Skill 可攜帶自己的 MCP 伺服器，按需啟動：

```
.opencode/skills/
├── playwright/
│   └── SKILL.md          # 瀏覽器自動化技能
├── git-master/
│   └── SKILL.md          # Git 原子提交、rebase
├── frontend-ui-ux/
│   └── SKILL.md          # 設計優先 UI
└── custom-banking/
    └── SKILL.md          # 自定義銀行業技能
```

也可放在使用者全域目錄：`~/.config/opencode/skills/*/SKILL.md`

#### SKILL.md 範例

```markdown
# Skill: Banking Domain Expert

## Description
專精銀行業務邏輯的開發技能，涵蓋帳戶管理、轉帳、監管合規。

## System Instructions
- 所有金額計算使用 BigDecimal
- 遵循 ACID 事務要求
- 敏感操作需要雙重驗證

## MCP Servers
- banking-api-docs: 內部 API 文件查詢

## Permissions
- read_files
- write_files
- run_tests
```

### 4.4 Prompt Template 設計

透過 Hooks 和 Agent 配置精細控制行為：

```jsonc
// .opencode/oh-my-opencode.jsonc
{
  "agents": {
    "sisyphus": {
      // 自定義系統提示追加
      "system_prompt_append": "When working on this banking project:\n1. Always use BigDecimal for amounts\n2. Enforce ACID transaction boundaries\n3. Log all state-changing operations"
    }
  }
}
```

### 4.5 Built-in MCP 伺服器

OMO 內建三個 MCP 伺服器，隨 Agent 自動可用：

| MCP | 功能 | 用途 |
|-----|------|------|
| **websearch (Exa)** | 網路搜尋 | 查找文件、API 參考、Stack Overflow |
| **context7** | 官方文件查詢 | 查找框架/庫的最新官方文件 |
| **grep_app** | GitHub 程式碼搜尋 | 搜尋 GitHub 上的程式碼範例 |

> **注意**：Skill-Embedded MCPs 是 OMO 的獨特設計——MCP 伺服器跟隨 Skill 按需啟動，任務完成後自動關閉，不會持續佔用上下文窗口。

---

## 第 5 章：Agent 系統詳解（Discipline Agents）

### 5.1 Sisyphus — 主編排器

Sisyphus 是 OMO 的核心 Agent，負責接受使用者請求、規劃任務、委派給專家 Agent，並驅動任務至完成。

**命名由來**：如同希臘神話中的薛西弗斯推石上山，永不放棄——Sisyphus 不會中途停止。

| 屬性 | 值 |
|------|-----|
| 主模型 | Claude Opus 4.6 (max variant) |
| 備選模型 | Kimi K2.5 → GPT-5.4 medium → GLM-5 |
| 角色 | 主編排器（Orchestrator） |
| 特色 | 積極平行委派、不停止直到完成、GPT-native 支援（v3.11.0+） |

**Sisyphus 工作流程**：

```mermaid
flowchart TD
    Input["使用者輸入"] --> IntentGate["IntentGate<br/>分析真實意圖"]
    IntentGate --> Plan["制定執行計劃"]
    Plan --> Delegate["委派子任務<br/>（指定 Category）"]
    
    Delegate -->|"deep"| Hephaestus["Hephaestus<br/>深度自主工作"]
    Delegate -->|"ultrabrain"| Oracle["Oracle<br/>驗證/推理"]
    Delegate -->|"visual-engineering"| FE["前端 Agent"]
    Delegate -->|"quick"| Quick["快速修復"]
    
    Hephaestus --> Collect["收集結果"]
    Oracle --> Collect
    FE --> Collect
    Quick --> Collect
    
    Collect --> Verify["Oracle 驗證"]
    Verify -->|"通過"| Complete["✅ 完成"]
    Verify -->|"未通過"| Delegate
```

**GPTPhus（v3.11.0+）**：Sisyphus 現在原生支援 GPT-5.4，使用 8-block 架構的專屬 Prompt。對於 OpenAI-only 設定的使用者，依然能獲得完整的 Sisyphus 編排體驗。

### 5.2 Hephaestus — 深度自主工作者

| 屬性 | 值 |
|------|-----|
| 主模型 | GPT-5.3-codex |
| 角色 | 自主深度工作者 |
| 特色 | 給目標不給步驟，自行探索 codebase 並端到端執行 |

**命名由來**：希臘鍛造之神赫淮斯托斯——「The Legitimate Craftsman」。Anthropic 封鎖 OpenCode 後的回應，Hephaestus 刻意使用 GPT 系列。

```mermaid
flowchart LR
    Goal["目標"] --> Explore["自行探索<br/>Codebase"]
    Explore --> Research["研究模式"]
    Research --> Implement["端到端實作"]
    Implement --> Verify["自我驗證"]
    Verify -->|"完成"| Result["交付成果"]
    Verify -->|"需修正"| Research
```

> **最佳實務**：Hephaestus 最適合「給目標，不給步驟」的任務——例如「重構這個模組以支援多租戶」而非「在 XXX 檔案的第 YYY 行加入 ZZZ」。

### 5.3 Prometheus — 戰略規劃者

| 屬性 | 值 |
|------|-----|
| 主模型 | Claude Opus 4.6 |
| 備選模型 | Kimi K2.5 / GLM-5 |
| 角色 | 戰略規劃者 |
| 觸發方式 | `/start-work` 指令 |
| 特色 | 面談模式：提問 → 釐清範圍 → 建立完整計劃，支援 `--worktree`（v3.9.0+） |

**使用流程**：

```bash
# 在 OpenCode 會話中
/start-work

# Prometheus 會以面談方式：
# 1. 提問釐清需求
# 2. 識別範圍與模糊點
# 3. 建立驗證過的執行計劃
# 4. 計劃確認後才開始執行
```

**Worktree 支援（v3.9.0+）**：

```bash
# 指定 Worktree，平行開發不衝突
/start-work --worktree /path/to/feature-branch
```

### 5.4 Oracle — 驗證者

| 屬性 | 值 |
|------|-----|
| 主模型 | GPT-5.4 high |
| 角色 | 架構驗證、除錯 |
| 特色 | ULW-Loop 強制驗證（v3.11.0+：Oracle 驗證變為強制） |

**ULW-Loop Oracle 驗證（v3.11.0+）**：

```mermaid
flowchart TD
    Task["ultrawork 任務執行"] --> Self["Agent 自我檢查"]
    Self --> Oracle["Oracle 強制驗證"]
    Oracle -->|"驗證通過"| Complete["✅ 任務完成"]
    Oracle -->|"驗證失敗"| Retry["重試<br/>（追蹤 Session）"]
    Retry --> Task
```

> v3.11.0 後，ULW-Loop 的 Oracle 驗證變為**強制性**。任務可能需要更長時間完成，但完成信心度顯著提升。

### 5.5 Atlas — 多任務編排器

Atlas 負責管理多個 Boulder（大型任務單元），包含 Final Verification Wave 確保所有任務完成：

```mermaid
flowchart TD
    Plan["Prometheus 計劃"] --> Atlas["Atlas 編排"]
    Atlas --> B1["Boulder 1<br/>（帳戶服務）"]
    Atlas --> B2["Boulder 2<br/>（轉帳服務）"]
    Atlas --> B3["Boulder 3<br/>（通知服務）"]
    
    B1 --> FVW["Final Verification Wave"]
    B2 --> FVW
    B3 --> FVW
    
    FVW -->|"全部通過"| Approve["等待使用者確認"]
    FVW -->|"有失敗"| Retry["重試失敗 Boulder"]
```

### 5.6 Background Agents

OMO 支援同時啟動多個 Agent 在背景執行：

```mermaid
graph TB
    Main["主 Sisyphus Session"] -->|"delegate"| BG1["Background Agent 1<br/>（後端開發）"]
    Main -->|"delegate"| BG2["Background Agent 2<br/>（前端開發）"]
    Main -->|"delegate"| BG3["Background Agent 3<br/>（測試撰寫）"]
    Main -->|"delegate"| BG4["Background Agent 4<br/>（文件更新）"]
    Main -->|"delegate"| BG5["Background Agent 5<br/>（Code Review）"]
    
    BG1 -->|"完成通知"| Main
    BG2 -->|"完成通知"| Main
    BG3 -->|"完成通知"| Main
    BG4 -->|"完成通知"| Main
    BG5 -->|"完成通知"| Main
```

**配置**：

```jsonc
{
  "background_tasks": {
    "concurrency": 5,           // 最多 5 個平行 Agent
    "stale_timeout_ms": 1200000 // 20 分鐘超時
  }
}
```

**特性（v3.12.x）**：
- Circuit Breaker 防止子 Agent 無限迴圈
- Target-aware loop detection（v3.12.1）
- 被取消的子任務自動釋放配額（v3.12.0）
- 兄弟任務執行時延遲清理（v3.12.0）

---

## 第 6 章：開發流程（ultrawork / Plan / Build）

### 6.1 ultrawork — 一鍵啟動

**ultrawork（或 ulw）** 是 OMO 最強大的功能——輸入一個詞，所有 Agent 啟動，任務不完成不停止。

```bash
# 在 OpenCode 會話中
ultrawork

# 或簡寫
ulw
```

ultrawork 背後的運作：

```mermaid
flowchart TD
    ULW["ultrawork 啟動"] --> Sisyphus["Sisyphus 接管"]
    Sisyphus --> Plan["制定計劃"]
    Plan --> Parallel["平行委派"]
    
    Parallel --> H["Hephaestus 深度工作"]
    Parallel --> O["Oracle 驗證"]
    Parallel --> BG["Background Agents"]
    
    H --> Todo["Todo Enforcer 監控"]
    O --> Todo
    BG --> Todo
    
    Todo -->|"Agent 閒置"| Yank["強制拉回繼續"]
    Todo -->|"全部完成"| Ralph["Ralph Loop 確認 100%"]
    
    Ralph -->|"未 100%"| Sisyphus
    Ralph -->|"100% 完成"| Done["✅ 完成"]
```

### 6.2 /ulw-loop（Ralph Loop）

Ralph Loop 是 ultrawork 的自參考迴圈機制——Agent 持續工作直到 100% 完成：

```bash
# 啟動 Ralph Loop
/ulw-loop

# Agent 會不斷自我檢查：
# → 任務是否 100% 完成？
# → 是否有遺漏的邊界情況？
# → 測試是否全部通過？
# → 直到確認完全完成才停止
```

**v3.9.0 改進**：
- 完成偵測範圍限定為迴圈啟動後的訊息
- 防止無限重新觸發的 in-flight guard
- Session reset 與 TUI 切換的競態條件修復

**v3.11.0 改進**：
- Oracle 驗證變為強制步驟
- 明確的 Oracle session tracking
- 驗證失敗時的 parent session retry

### 6.3 /start-work — 規劃先行

```bash
# 啟動 Prometheus 規劃
/start-work

# Prometheus 會：
# 1. 像真正的工程師一樣面談你
# 2. 識別範圍和模糊點
# 3. 建立詳細的驗證計劃
# 4. 等你確認後才開始執行

# 支援 Worktree（v3.9.0+）
/start-work --worktree /path/to/feature
```

### 6.4 /init-deep — 深度初始化

```bash
# 自動生成分層 AGENTS.md
/init-deep

# 效果：在整個專案的各層目錄生成 AGENTS.md
# Agent 自動讀取相關上下文
# 對 Token 效率和 Agent 效能都有顯著幫助
```

### 6.5 Hash-Anchored Edits（Hashline）

OMO 的 Hashline 系統解決了「Harness Problem」——大多數 Agent 失敗不是模型問題，而是編輯工具問題。

```
# Agent 讀取檔案時，每行附帶內容雜湊：
11#VK| function hello() {
22#XJ|   return "world";
33#MB| }
```

Agent 編輯時引用這些標籤。若檔案自上次讀取後已變更，雜湊不匹配則**拒絕編輯**，防止損壞。

**效果**：Grok Code Fast 1 的成功率從 6.7% 提升至 68.3%。

```jsonc
// 啟用 Hashline Edit（v3.10.0+ 預設停用）
{
  "experimental": {
    "hashline_edit": true
  }
}
```

**Hashline 操作模型**（v3.8.5 三操作模型）：
- `replace`：替換指定行範圍
- `insert`：在指定位置插入
- `delete`：刪除指定行範圍

### 6.6 Plan Mode vs Build Mode

| 特性 | Plan Mode | Build Mode |
|------|-----------|------------|
| 觸發 | 預設模式 | ultrawork / 確認後切換 |
| 檔案操作 | 僅讀取、分析 | 讀取 + 寫入 + 修改 |
| 適用 | 需求分析、架構設計、方案評估 | 程式碼實作、重構、Bug 修復 |
| 安全性 | 最高（不修改任何檔案） | 需搭配 Git branch + Review |
| Agent | Prometheus 為主 | Sisyphus + 全團隊 |

### 6.7 Git 整合流程

```mermaid
gitgraph
    commit id: "init"
    branch develop
    checkout develop
    commit id: "develop-base"
    
    branch feature-transfer-api
    checkout feature-transfer-api
    commit id: "feat-domain-model"
    commit id: "feat-transfer-svc"
    commit id: "feat-controller"
    commit id: "test-transfer"
    commit id: "docs-api"
    
    checkout develop
    merge feature-transfer-api id: "PR-merged"
    
    branch release-v1-2-0
    checkout release-v1-2-0
    commit id: "bump-version"
    
    checkout main
    merge release-v1-2-0 id: "v1.2.0"
```

**Skills: git-master**

OMO 內建 `git-master` Skill，支援：
- 原子提交（Atomic Commits）
- Rebase surgery
- 智慧合併衝突解決

> **企業最佳實務**：
> - Hephaestus 的 auto-commit 行為已在 v3.9.0 移除——Agent 不會未經允許自動提交
> - 使用 `start-work` 的 `auto_commit` 配置來控制提交行為
> - 每步完成都手動確認後 commit

---

## 第 7 章：Web Application 實戰

### 7.1 實戰場景：企業帳戶管理系統

以下用一個完整的「帳戶管理系統」示範 OMO 如何協助開發。

#### 系統需求

- 帳戶 CRUD
- 帳戶餘額查詢
- 轉帳功能
- 交易紀錄查詢

### 7.2 Step 1：使用 Prometheus 規劃

```bash
/start-work

# Prometheus 面談：
> 我需要開發一個帳戶管理系統，使用 Clean Architecture + Spring Boot 3.2，
> 包含帳戶 CRUD、餘額查詢、轉帳功能。資料庫使用 PostgreSQL。

# Prometheus 會提問：
# 「轉帳需要支援預約轉帳嗎？」
# 「需要多幣別支援嗎？」
# 「並發轉帳的隔離級別需求？」
# ...然後建立完整計劃
```

**Prometheus 規劃輸出**：

```
📋 Plan: 帳戶管理系統

## 1. Domain Model
- Account (Entity)
- Transfer (Entity)
- AccountStatus (Value Object)

## 2. API 設計
GET    /api/v1/accounts          → 帳戶列表
POST   /api/v1/accounts          → 建立帳戶
GET    /api/v1/accounts/{id}     → 帳戶詳情
POST   /api/v1/transfers         → 執行轉帳
GET    /api/v1/transfers         → 轉帳記錄

## 3. 安全考量
⚠️ 轉帳必須使用 DB Transaction + 悲觀鎖
⚠️ 需要 Rate Limiting
⚠️ 金額伺服器端驗證

## 4. 預估範圍
- 新增 3 Controller
- 新增 2 Service + Interface
- 新增 2 Repository
- 新增 2 Flyway Migration
- 新增 15+ 測試案例

確認此計劃？(y/n)
```

### 7.3 Step 2：ultrawork 執行

確認計劃後，Sisyphus 接管並平行委派：

```bash
# 確認計劃後
ultrawork

# Sisyphus 自動：
# 1. 委派 Hephaestus → 後端 Domain + Service
# 2. 平行委派 Background Agent → Controller + DTO
# 3. 委派 Background Agent → 測試生成
# 4. Oracle 驗證所有產出
```

### 7.4 後端開發產出（Spring Boot）

**Domain Layer — Entity**：

```java
package com.company.banking.domain.entity;

import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * 帳戶實體 - Domain Layer 核心物件
 */
public class Account {
    private final Long id;
    private final String accountNumber;
    private String holderName;
    private BigDecimal balance;
    private AccountStatus status;
    private final LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    public Account(Long id, String accountNumber, String holderName,
                   BigDecimal balance, AccountStatus status,
                   LocalDateTime createdAt, LocalDateTime updatedAt) {
        this.id = id;
        this.accountNumber = accountNumber;
        this.holderName = holderName;
        this.balance = balance;
        this.status = status;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    /**
     * 執行扣款 - Domain Logic
     */
    public void debit(BigDecimal amount) {
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("扣款金額必須大於零");
        }
        if (this.balance.compareTo(amount) < 0) {
            throw new InsufficientBalanceException(
                "帳戶餘額不足：餘額=" + this.balance + ", 扣款=" + amount);
        }
        this.balance = this.balance.subtract(amount);
        this.updatedAt = LocalDateTime.now();
    }

    /**
     * 執行入帳 - Domain Logic
     */
    public void credit(BigDecimal amount) {
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("入帳金額必須大於零");
        }
        this.balance = this.balance.add(amount);
        this.updatedAt = LocalDateTime.now();
    }

    // Getters
    public Long getId() { return id; }
    public String getAccountNumber() { return accountNumber; }
    public String getHolderName() { return holderName; }
    public BigDecimal getBalance() { return balance; }
    public AccountStatus getStatus() { return status; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
}
```

**Application Layer — Use Case**：

```java
package com.company.banking.application.usecase;

import com.company.banking.domain.entity.Account;
import com.company.banking.domain.repository.AccountRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;

/**
 * 轉帳用例 - Application Layer
 */
@Service
public class TransferUseCase {

    private final AccountRepository accountRepository;

    public TransferUseCase(AccountRepository accountRepository) {
        this.accountRepository = accountRepository;
    }

    @Transactional
    public TransferResult execute(Long fromAccountId, Long toAccountId,
                                   BigDecimal amount) {
        // 悲觀鎖避免 Race Condition
        Account fromAccount = accountRepository
            .findByIdWithLock(fromAccountId)
            .orElseThrow(() -> new AccountNotFoundException(fromAccountId));

        Account toAccount = accountRepository
            .findByIdWithLock(toAccountId)
            .orElseThrow(() -> new AccountNotFoundException(toAccountId));

        // Domain Logic
        fromAccount.debit(amount);
        toAccount.credit(amount);

        accountRepository.save(fromAccount);
        accountRepository.save(toAccount);

        return new TransferResult(
            fromAccount.getAccountNumber(),
            toAccount.getAccountNumber(),
            amount,
            fromAccount.getBalance()
        );
    }
}
```

**Presentation Layer — Controller**：

```java
package com.company.banking.presentation.controller;

import com.company.banking.application.usecase.TransferUseCase;
import com.company.banking.presentation.dto.ApiResponse;
import com.company.banking.presentation.dto.TransferRequest;
import com.company.banking.presentation.dto.TransferResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/transfers")
@Tag(name = "Transfer", description = "轉帳管理 API")
public class TransferController {

    private static final Logger log = LoggerFactory.getLogger(TransferController.class);
    private final TransferUseCase transferUseCase;

    public TransferController(TransferUseCase transferUseCase) {
        this.transferUseCase = transferUseCase;
    }

    @PostMapping
    @Operation(summary = "執行轉帳", description = "從來源帳戶轉帳至目標帳戶")
    public ResponseEntity<ApiResponse<TransferResponse>> transfer(
            @Valid @RequestBody TransferRequest request) {

        log.info("Transfer request: from={}, to={}, amount={}",
            request.fromAccountId(), request.toAccountId(), request.amount());

        var result = transferUseCase.execute(
            request.fromAccountId(),
            request.toAccountId(),
            request.amount());

        return ResponseEntity.ok(ApiResponse.success(
            new TransferResponse(
                result.fromAccountNumber(),
                result.toAccountNumber(),
                result.amount(),
                result.remainingBalance())));
    }
}
```

### 7.5 前端開發產出（Vue 3 + TypeScript）

```vue
<!-- views/TransferView.vue -->
<script setup lang="ts">
import { ref, computed } from 'vue'
import { useTransferApi } from '@/composables/useTransferApi'
import { useNotification } from '@/composables/useNotification'

interface TransferForm {
  fromAccountId: number | null
  toAccountId: number | null
  amount: string
}

const form = ref<TransferForm>({
  fromAccountId: null,
  toAccountId: null,
  amount: ''
})

const { transfer, loading, error } = useTransferApi()
const { showSuccess, showError } = useNotification()

const isValid = computed(() => {
  return form.value.fromAccountId !== null
    && form.value.toAccountId !== null
    && parseFloat(form.value.amount) > 0
    && form.value.fromAccountId !== form.value.toAccountId
})

async function handleSubmit() {
  if (!isValid.value) return
  try {
    const result = await transfer({
      fromAccountId: form.value.fromAccountId!,
      toAccountId: form.value.toAccountId!,
      amount: parseFloat(form.value.amount)
    })
    showSuccess(`轉帳成功！剩餘餘額：${result.remainingBalance}`)
    resetForm()
  } catch (err) {
    showError('轉帳失敗：' + (err as Error).message)
  }
}

function resetForm() {
  form.value = { fromAccountId: null, toAccountId: null, amount: '' }
}
</script>

<template>
  <div class="max-w-md mx-auto p-6">
    <h1 class="text-2xl font-bold mb-6">帳戶轉帳</h1>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div>
        <label class="block text-sm font-medium mb-1">來源帳戶</label>
        <AccountSelector v-model="form.fromAccountId" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">目標帳戶</label>
        <AccountSelector v-model="form.toAccountId" :exclude="form.fromAccountId" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">轉帳金額</label>
        <input v-model="form.amount" type="number" min="1" step="1"
               class="w-full border rounded-lg px-3 py-2" placeholder="請輸入金額" />
      </div>
      <div v-if="error" class="text-red-600 text-sm bg-red-50 p-3 rounded">{{ error }}</div>
      <button type="submit" :disabled="!isValid || loading"
              class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700
                     disabled:bg-gray-400 disabled:cursor-not-allowed">
        <span v-if="loading">處理中...</span>
        <span v-else>確認轉帳</span>
      </button>
    </form>
  </div>
</template>
```

### 7.6 DB Migration

```sql
-- Flyway: V20240301__create_transfer_tables.sql
CREATE TABLE accounts (
    id              BIGSERIAL PRIMARY KEY,
    account_number  VARCHAR(20) NOT NULL UNIQUE,
    holder_name     VARCHAR(100) NOT NULL,
    balance         DECIMAL(18, 2) NOT NULL DEFAULT 0.00,
    status          VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_balance_non_negative CHECK (balance >= 0),
    CONSTRAINT chk_status CHECK (status IN ('ACTIVE', 'FROZEN', 'CLOSED'))
);

CREATE TABLE transfer_records (
    id                  BIGSERIAL PRIMARY KEY,
    from_account_id     BIGINT NOT NULL REFERENCES accounts(id),
    to_account_id       BIGINT NOT NULL REFERENCES accounts(id),
    amount              DECIMAL(18, 2) NOT NULL,
    status              VARCHAR(20) NOT NULL DEFAULT 'COMPLETED',
    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_amount_positive CHECK (amount > 0),
    CONSTRAINT chk_different_accounts CHECK (from_account_id != to_account_id)
);

CREATE INDEX idx_transfer_from ON transfer_records(from_account_id);
CREATE INDEX idx_transfer_to ON transfer_records(to_account_id);
CREATE INDEX idx_transfer_created ON transfer_records(created_at);
```

### 7.7 OMO 開發流程摘要

```mermaid
flowchart LR
    A["1. /start-work<br/>Prometheus 規劃"]
    --> B["2. 確認計劃<br/>人工審核"]
    --> C["3. ultrawork<br/>全團隊平行執行"]
    --> D["4. Oracle 驗證<br/>品質檢查"]
    --> E["5. 人工 Review<br/>PR Merge"]
```

---

## 第 8 章：測試與品質（Testing & Quality）

### 8.1 OMO 自動測試生成

ultrawork 執行時，Background Agent 會自動生成測試：

```java
package com.company.banking.application.usecase;

import com.company.banking.domain.entity.*;
import com.company.banking.domain.repository.AccountRepository;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.*;
import org.mockito.junit.jupiter.MockitoExtension;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("轉帳用例測試")
class TransferUseCaseTest {

    @Mock
    private AccountRepository accountRepository;

    @InjectMocks
    private TransferUseCase transferUseCase;

    private Account fromAccount;
    private Account toAccount;

    @BeforeEach
    void setUp() {
        fromAccount = new Account(1L, "ACC001", "張三",
            new BigDecimal("10000.00"), AccountStatus.ACTIVE,
            LocalDateTime.now(), LocalDateTime.now());
        toAccount = new Account(2L, "ACC002", "李四",
            new BigDecimal("5000.00"), AccountStatus.ACTIVE,
            LocalDateTime.now(), LocalDateTime.now());
    }

    @Nested
    @DisplayName("正向測試")
    class HappyPath {
        @Test
        @DisplayName("應該成功執行轉帳 - 當餘額充足時")
        void should_transfer_successfully_when_balance_sufficient() {
            when(accountRepository.findByIdWithLock(1L))
                .thenReturn(Optional.of(fromAccount));
            when(accountRepository.findByIdWithLock(2L))
                .thenReturn(Optional.of(toAccount));

            TransferResult result = transferUseCase.execute(
                1L, 2L, new BigDecimal("3000.00"));

            assertThat(result.amount()).isEqualByComparingTo("3000.00");
            assertThat(result.remainingBalance()).isEqualByComparingTo("7000.00");
            verify(accountRepository, times(2)).save(any());
        }
    }

    @Nested
    @DisplayName("負向測試")
    class ErrorCases {
        @Test
        @DisplayName("應該拋出例外 - 當來源帳戶不存在時")
        void should_throw_when_from_account_not_found() {
            when(accountRepository.findByIdWithLock(999L))
                .thenReturn(Optional.empty());
            assertThatThrownBy(() ->
                transferUseCase.execute(999L, 2L, new BigDecimal("1000.00")))
                .isInstanceOf(AccountNotFoundException.class);
        }

        @Test
        @DisplayName("應該拋出例外 - 當餘額不足時")
        void should_throw_when_insufficient_balance() {
            when(accountRepository.findByIdWithLock(1L))
                .thenReturn(Optional.of(fromAccount));
            when(accountRepository.findByIdWithLock(2L))
                .thenReturn(Optional.of(toAccount));
            assertThatThrownBy(() ->
                transferUseCase.execute(1L, 2L, new BigDecimal("99999.00")))
                .isInstanceOf(InsufficientBalanceException.class);
        }
    }

    @Nested
    @DisplayName("邊界值測試")
    class BoundaryTests {
        @Test
        @DisplayName("應該成功 - 當轉帳全部餘額時")
        void should_succeed_when_transfer_entire_balance() {
            when(accountRepository.findByIdWithLock(1L))
                .thenReturn(Optional.of(fromAccount));
            when(accountRepository.findByIdWithLock(2L))
                .thenReturn(Optional.of(toAccount));
            TransferResult result = transferUseCase.execute(
                1L, 2L, new BigDecimal("10000.00"));
            assertThat(result.remainingBalance()).isEqualByComparingTo("0.00");
        }

        @Test
        @DisplayName("應該成功 - 當轉帳最小金額 0.01 時")
        void should_succeed_when_transfer_minimum_amount() {
            when(accountRepository.findByIdWithLock(1L))
                .thenReturn(Optional.of(fromAccount));
            when(accountRepository.findByIdWithLock(2L))
                .thenReturn(Optional.of(toAccount));
            TransferResult result = transferUseCase.execute(
                1L, 2L, new BigDecimal("0.01"));
            assertThat(result.remainingBalance()).isEqualByComparingTo("9999.99");
        }
    }
}
```

### 8.2 Comment Checker

OMO 內建 Comment Checker Hook，自動偵測並拒絕 AI 生成的低品質註解（"AI slop"）——確保程式碼讀起來像資深工程師寫的。

### 8.3 SonarQube 整合

```yaml
# .github/workflows/quality.yml
name: Quality Check
on: [pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Tests with Coverage
        run: mvn verify jacoco:report
      - name: SonarQube Analysis
        run: mvn sonar:sonar
      - name: Quality Gate
        run: |
          if [ "$QUALITY_GATE_STATUS" != "OK" ]; then
            echo "Quality Gate FAILED"
            exit 1
          fi
```

> **實務建議**：OMO 自動生成的測試作為起點，團隊仍需 Review 完整性。金融核心邏輯的測試建議人工撰寫。

---

## 第 9 章：維運與除錯（Maintenance）

### 9.1 /doctor — 診斷工具

```bash
# 在 OpenCode 會話中執行
/doctor

# Doctor 會檢查：
# ✅ Plugin 版本
# ✅ 已偵測的 LSP 伺服器和擴展（v3.12.0+ 動態偵測）
# ✅ Agent 載入狀態
# ✅ 模型連線
# ✅ 配置路徑
# ✅ 自動更新設定
```

**v3.12.0 改進**：Doctor 現在顯示**實際偵測到的 LSP 伺服器和擴展**，而非硬編碼的計數。

### 9.2 Token 與成本管理

#### 模型成本參考

| 模型 | 定位 | 用於 Agent |
|------|------|-----------|
| Claude Opus 4.6 | 最高階推理 | Sisyphus, Prometheus |
| GPT-5.4 (xhigh/high/medium) | 推理 + Agent 任務 | Oracle, Momus, Metis, Atlas 備選 |
| GPT-5.3-codex | 深度自主工作 | Hephaestus（ultrabrain/deep 類別保留） |
| Kimi K2.5 | 編排替代 | Sisyphus 備選 |
| GLM-5 | 編排備選 | Sisyphus 備選（unspecified-high default） |

#### Token 最佳化策略

| 策略 | 說明 | 效果 |
|------|------|------|
| `/init-deep` 分層上下文 | 每個目錄獨立 AGENTS.md | Agent 只讀取相關上下文 |
| Preemptive Compaction | 上下文增長時自動壓縮 | 防止 Token 超限 |
| Category-based routing | 簡單任務用小模型 | 自動節省成本 |
| Stale timeout | 背景任務 20 分鐘超時 | 防止懸掛浪費 |

### 9.3 Circuit Breaker（v3.12.0+）

防止子 Agent 進入無限迴圈的熔斷機制：

```jsonc
{
  "circuit_breaker": {
    "enabled": true,              // 啟用/停用（escape hatch）
    "max_consecutive_calls": 10   // 連續呼叫上限
  }
}
```

**v3.12.x 改進歷程**：
- v3.12.0：Smart Circuit Breaker 引入，應用於 Background Agent Manager events
- v3.12.1：Target-aware loop detection via tool signatures
- v3.12.2：Sliding Window 改為 Consecutive Call Detection

### 9.4 Agent Debug 方法

```mermaid
flowchart TD
    Issue["Agent 輸出異常"] --> Doctor["1. 執行 /doctor"]
    Doctor --> AGENTS["2. 檢查 AGENTS.md<br/>（/init-deep 重新生成）"]
    AGENTS --> Config["3. 檢查 oh-my-opencode.jsonc"]
    Config --> Model["4. 確認模型可用性"]
    Model --> Hooks["5. 檢查 disabled_hooks"]
    Hooks --> CB["6. Circuit Breaker 是否觸發"]
```

### 9.5 Session 管理工具

OMO 提供完整的 session 管理功能：

- **Session 列表**：查看所有歷史會話
- **Session 搜尋**：搜尋特定會話內容
- **Session 分析**：分析 Token 使用、模型分布
- **Session 通知**：背景 Agent 完成時通知（v3.9.0+：排隊等待閒置 session）

---

## 第 10 章：升級與版本管理（Upgrade）

### 10.1 版本歷程概覽

| 版本 | 發布時間 | 重大特性 |
|------|---------|---------|
| v3.12.3 | 2026-07 | Bug fixes, debug logging cleanup |
| v3.12.0 | 2026-07 | Smart Circuit Breaker, OpenClaw 整合（已回退）, Windows XDG_CONFIG_HOME |
| v3.11.0 | 2026-07 | **改名為 oh-my-openagent**，GPT-5.4 era，Oracle 強制驗證 |
| v3.10.0 | 2026-07 | HTTP Hook 安全（SSRF 防護），Hashline Edit opt-in |
| v3.9.0 | 2026-06 | Worktree planning, Gemini 3.1 Pro, 可靠性強化 |
| v3.8.5 | 2026-06 | Hashline 編輯精度大幅提升 |

### 10.2 升級步驟

OMO 作為 OpenCode 插件，升級方式取決於安裝方式：

```bash
# 如果使用 npm 全域安裝
npm update -g oh-my-opencode
# 或
npm update -g oh-my-openagent

# OpenCode 通常會自動檢測插件更新
# 可透過 /doctor 確認目前版本
```

### 10.3 Migration Notes（v3.11.0）

**從 oh-my-opencode 遷移到 oh-my-openagent**：

- 兩個套件名稱都受支援（雙發布機制 dual-publish）
- 配置檔同時偵測 `oh-my-opencode.json(c)` 和 `oh-my-openagent.jsonc`
- 環境變數：`OMX_*` 已更名為 `OMO_*`

**GPT-5.4 遷移**：

| Agent | 舊模型 | 新模型 |
|-------|--------|--------|
| Oracle | GPT-5.2 | GPT-5.4 high |
| Momus | GPT-5.2 | GPT-5.4 xhigh |
| Metis | GPT-5.2 | GPT-5.4 high |
| Prometheus | GPT-5.2 | GPT-5.4 high |
| Atlas | Claude Sonnet | + GPT-5.4 medium fallback |
| Multimodal Looker | GPT-5.3-codex | GPT-5.4 medium |

**ULW-Loop 注意事項**：
- Oracle 驗證變為強制 → 任務耗時略增，但完成信心度顯著提升

**OpenAI-Only 使用者**：
- Sisyphus 現在原生支援 GPT-5.4 → 不再需要退回 Hephaestus

### 10.4 版本升級策略

```mermaid
flowchart LR
    Check["檢查新版本<br/>/doctor"] 
    --> Release["閱讀 Release Notes<br/>Breaking Changes"]
    --> Backup["備份配置<br/>oh-my-opencode.jsonc"]
    --> Dev["Dev 環境升級<br/>驗證功能"]
    --> Prod["Production 升級"]
```

---

## 第 11 章：安全（SSDLC）

### 11.1 Hook Security（v3.10.0+）

OMO v3.10.0 強化了 Hook 安全，防止 SSRF 和其他攻擊：

```mermaid
flowchart TD
    Hook["Hook 執行"] --> Validate["URL Scheme 驗證"]
    Validate -->|"http: / https:"| Allow["✅ 允許執行"]
    Validate -->|"file: / data: / 其他"| Block["❌ 阻擋<br/>SSRF 防護"]
    
    Hook --> Disabled["disabled_hooks 檢查"]
    Disabled -->|"在停用清單"| Skip["⏭️ 跳過"]
    Disabled -->|"未在清單"| Execute["執行"]
```

**重要安全特性**：

| 版本 | 安全特性 |
|------|---------|
| v3.10.0 | HTTP Hook URL scheme validation（只允許 http/https） |
| v3.10.0 | `disabled_hooks` 機制擴展到 HTTP hooks |
| v3.10.0 | Deterministic message/part IDs（防止儲存碰撞） |
| v3.12.0 | Agent name normalization 防止 alias bypass |
| v3.12.0 | Forward-compatible disabled hooks |

### 11.2 Prompt Injection 防護

```jsonc
// .opencode/oh-my-opencode.jsonc
{
  // 停用危險工具
  "disabled_tools": [
    // 禁止特定工具
  ],
  
  // 停用特定 hooks
  "disabled_hooks": [
    // 根據需要停用
  ]
}
```

OMO 的 Agent 設計本身包含防護：
- **IntentGate**：分析真實使用者意圖，而非字面解釋
- **Role Boundary**：每個 Agent 有明確職責邊界
- **blocked_operations**：內建危險指令封鎖

### 11.3 Secrets 管理

```mermaid
flowchart TD
    subgraph Secure["安全做法 ✅"]
        EnvVar["環境變數"]
        OpenCodeCfg["OpenCode Provider 設定"]
        Vault["Secrets Manager"]
    end

    subgraph Insecure["不安全做法 ❌"]
        HardCode["Hard-coded in config"]
        GitCommit["提交到 Git"]
    end

    Agent["OMO Agent"] -->|"讀取"| Secure
    Agent -.->|"禁止"| Insecure
```

```bash
# .gitignore
.opencode/oh-my-opencode.json
.opencode/oh-my-opencode.jsonc
*.env
*.key
*.pem
```

### 11.4 安全掃描 CI/CD

```yaml
# .github/workflows/security.yml
name: Security Scan
on:
  pull_request:
    branches: [develop, main]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: SAST - SonarQube
        run: mvn sonar:sonar -Dsonar.qualitygate.wait=true
      - name: Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'enterprise-banking'
          format: 'HTML'
      - name: Secret Scanning
        uses: trufflesecurity/trufflehog@main
        with:
          extra_args: --only-verified
      - name: Container Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'enterprise-banking:latest'
          severity: 'CRITICAL,HIGH'
```

### 11.5 Dependabot 配置

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "maven"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
  - package-ecosystem: "npm"
    directory: "/src/frontend"
    schedule:
      interval: "weekly"
```

> **SSDLC 檢查清單**：
> - [ ] AGENTS.md 不含敏感資訊
> - [ ] API Key 通過 OpenCode Provider 設定（非 hard-code）
> - [ ] Git hooks 防止 Secrets 提交
> - [ ] `disabled_hooks` / `disabled_tools` 已配置
> - [ ] HTTP Hook 僅允許 http/https scheme
> - [ ] CI/CD 包含 SAST / DAST / SCA
> - [ ] 依賴套件定期更新

---

## 第 12 章：團隊導入策略（Enterprise Adoption）

### 12.1 導入階段

```mermaid
gantt
    title OMO 企業導入時程
    dateFormat  YYYY-MM-DD
    
    section PoC（概念驗證）
    環境搭建           :poc1, 2026-08-01, 5d
    試用功能確認       :poc2, after poc1, 5d
    結果評估           :poc3, after poc2, 3d
    
    section Pilot（試點）
    選定試點團隊       :pilot1, after poc3, 3d
    團隊培訓           :pilot2, after pilot1, 5d
    試點專案執行       :pilot3, after pilot2, 20d
    成效評估           :pilot4, after pilot3, 5d
    
    section Production（推廣）
    建立規範文件       :prod1, after pilot4, 10d
    全團隊培訓         :prod2, after prod1, 10d
    正式上線           :prod3, after prod2, 5d
    持續優化           :prod4, after prod3, 30d
```

#### Phase 1：PoC — 2 週

| 任務 | 說明 | 產出 |
|------|------|------|
| 環境搭建 | 安裝 OpenCode + OMO 插件、配置 LLM Provider | 可用的開發環境 |
| 功能驗證 | ultrawork、/start-work、/init-deep | 功能驗證報告 |
| 安全評估 | Hook Security、disabled_tools 配置 | 安全評估報告 |
| 成本估算 | 預估月 Token 成本（根據 Agent 分類） | 成本分析報告 |

#### Phase 2：Pilot — 4-6 週

| 任務 | 說明 | 產出 |
|------|------|------|
| 團隊選定 | 2-3 位資深開發者 | 試點小組 |
| 培訓 | AGENTS.md 撰寫、ultrawork 使用、Agent 系統理解 | 培訓教材 |
| 實戰 | 選一個中等複雜度功能用 OMO 開發 | 實作成果 |
| 回饋收集 | 匯集問題與改善建議 | 改善報告 |

#### Phase 3：Production — 持續

| 任務 | 說明 | 產出 |
|------|------|------|
| 規範建立 | 制定 AGENTS.md 規範、安全配置標準 | 團隊規範文件 |
| 全員培訓 | Workshop + Hands-on | 培訓記錄 |
| 知識庫 | FAQ + 最佳實務 + Skill 範本庫 | 內部 Wiki |
| 持續優化 | 定期 Review Agent 配置與成本 | 月度報告 |

### 12.2 使用 OMO 的企業

根據官方資訊，以下企業已在使用 OMO：

| 企業 | 用途 |
|------|------|
| **Indent** | Spray（網紅行銷）、vovushop（跨境電商）、vreview（AI 商業評論） |
| **Google** | 部分團隊使用 |
| **Microsoft** | 部分團隊使用 |
| **ELESTYLE** | elepay（多行動支付閘道）、OneQR（無現金 SaaS） |

### 12.3 教育訓練建議

| 階段 | 對象 | 內容 | 時間 |
|------|------|------|------|
| Level 1 | 全體工程師 | OMO 概念、ultrawork 基本使用 | 2 小時 |
| Level 2 | 資深工程師 | /init-deep、Agent 系統、Skills、配置 | 4 小時 |
| Level 3 | Tech Lead | Category routing、Background Agents、成本管理 | 4 小時 |
| Level 4 | 架構師 | Hooks 設計、Custom Agent、安全配置 | 8 小時 |
| Workshop | 全員 | Hands-on：用 ultrawork 開發完整功能 | 4 小時 |

---

## 第 13 章：最佳實務（Best Practices）

### 13.1 Context Engineering

```mermaid
graph TB
    subgraph Context["上下文分層（/init-deep）"]
        L1["Layer 1: 專案級<br/>project/AGENTS.md"]
        L2["Layer 2: 模組級<br/>src/AGENTS.md"]
        L3["Layer 3: 目錄級<br/>src/components/AGENTS.md"]
        L4["Layer 4: 對話上下文<br/>本次互動歷史"]
    end
    L1 --> L2 --> L3 --> L4
```

**原則**：
- 使用 `/init-deep` 自動生成分層 AGENTS.md
- 專案級 AGENTS.md 控制在 500-1000 行
- Agent 自動讀取相關層級——無需手動管理
- 對 Token 效率和 Agent 效能都有顯著幫助

### 13.2 任務分類策略

善用 OMO 的 Category 系統，讓正確的模型處理正確的任務：

| Category | 適用場景 | 預設模型 |
|----------|---------|---------|
| `visual-engineering` | 前端、UI/UX | 視覺類模型 |
| `deep` | 自主研究 + 長時間執行 | GPT-5.3-codex medium |
| `quick` | 單檔修改、Typo | 輕量模型 |
| `ultrabrain` | 困難邏輯、架構決策 | GPT-5.4 xhigh |
| `unspecified-high` | 一般高強度任務 | GPT-5.4 high |
| 自定義 | `business-logic` 等 | 可配置 |

### 13.3 Skills 最佳實務

- 針對特定領域建立 Skills（如 `banking-domain`、`k8s-ops`）
- Skills 可攜帶 MCP 伺服器，按需啟動，不佔用上下文
- 放在 `.opencode/skills/*/SKILL.md` 或 `~/.config/opencode/skills/*/SKILL.md`
- 使用 `/get-unpublished-changes` 和 `/review-work` Skill 進行發布前審查

### 13.4 避免 AI 亂改程式

| 策略 | 做法 |
|------|------|
| **先 /start-work** | 永遠先用 Prometheus 規劃 |
| **小步前進** | 一次只做一個功能 |
| **Git Branch** | 每個任務在獨立分支，方便 rollback |
| **Oracle 驗證** | ultrawork 強制 Oracle 驗證所有產出 |
| **Comment Checker** | 自動拒絕 AI slop 註解 |
| **人工 Review** | 所有 AI 產出必須 Code Review |

### 13.5 成本最佳化

| 方法 | 說明 |
|------|------|
| Category routing | 讓系統自動為簡單任務用小模型 |
| `/init-deep` | 精準上下文減少 Token 浪費 |
| Preemptive Compaction | 自動壓縮過長的上下文 |
| Background Agent timeout | 防止懸掛 Agent 浪費 Token |
| 模型 Fallback | 主模型不可用時自動降級 |

---

## 第 14 章：常見問題（FAQ）

### Q1：ultrawork 執行後 Agent 不停止怎麼辦？

**解決方案**：
1. 這是設計行為——ultrawork 不完成不停止
2. 如果確實陷入迴圈，Circuit Breaker（v3.12.0+）會自動觸發
3. 可手動停止會話
4. 檢查 `circuit_breaker.enabled: true` 是否已設定

### Q2：Hashline Edit 要不要啟用？

| 情況 | 建議 |
|------|------|
| 大量批次修改 | 啟用（提升精度） |
| 簡單單檔修改 | 可不啟用（v3.10.0+ 預設停用） |
| 精度要求高 | 啟用 |

```jsonc
{
  "experimental": {
    "hashline_edit": true
  }
}
```

### Q3：多模型如何選擇？

| 場景 | 推薦 | 理由 |
|------|------|------|
| 架構編排 | Claude Opus 4.6 | 最強推理 |
| 深度自主工作 | GPT-5.3-codex | 長時間編碼訓練 |
| 驗證與推理 | GPT-5.4 high | 強推理 + 成本合理 |
| 規劃 | Claude Opus 4.6 / Kimi K2.5 | 結構化思維 |
| OpenAI-only | GPT-5.4 + GPTPhus | Sisyphus 原生 GPT 支援 |
| 離線環境 | 需要自行配置本地模型 | 透過 OpenCode Provider |

### Q4：OMO 與 Claude Code 的關係？

OMO 透過 OpenCode 插件系統運行，**100% 相容 Claude Code 生態**：
- Claude Code 的 `hooks.json` → OMO 可讀取
- Claude Code 的 `CLAUDE.md` → 等同於 `AGENTS.md`
- Claude Code 的 Skills → OMO 完全支援
- Claude Code 的 MCP → OMO 內建 + 自定義
- Claude Code 的 Plugins → OMO 相容（v3.12.0+ v3 flat array format）

### Q5：如何確保 AI 生成的程式碼安全？

1. **Hook Security**：v3.10.0+ HTTP Hook URL scheme validation（SSRF 防護）
2. **Comment Checker**：自動拒絕 AI slop
3. **Oracle 強制驗證**：ultrawork 所有產出經 Oracle 驗證
4. **disabled_tools / disabled_hooks**：精細控管
5. **CI/CD 掃描**：SAST + SCA + Secret Scan
6. **人工 Review**：永遠最後一道防線

### Q6：套件名稱是 oh-my-opencode 還是 oh-my-openagent？

- v3.11.0 起改名為 **oh-my-openagent**
- 新的套件名稱：`oh-my-openagent`
- 舊的套件名稱 `oh-my-opencode` 仍然支援（雙發布）
- 配置檔偵測兩者：`oh-my-opencode.json(c)` 和 `oh-my-openagent.jsonc`

---

## 第 15 章：附錄（Appendix）

### 15.1 Slash Commands 速查表

| 指令 | 說明 |
|------|------|
| `ultrawork` / `ulw` | 啟動全自動多 Agent 執行 |
| `/ulw-loop` | 自參考迴圈，100% 完成才停止 |
| `/start-work` | Prometheus 面談式規劃 |
| `/start-work --worktree <path>` | 指定 Worktree 規劃 |
| `/init-deep` | 自動生成分層 AGENTS.md |
| `/doctor` | 診斷安裝狀態 |
| `/get-unpublished-changes` | 查看未發布的變更 |
| `/review-work` | 觸發 pre-publish review |

### 15.2 Agent 一覽表

| Agent | 主模型 | 角色 |
|-------|--------|------|
| Sisyphus | Claude Opus 4.6 | 主編排器 |
| Hephaestus | GPT-5.3-codex | 深度自主工作者 |
| Prometheus | Claude Opus 4.6 | 戰略規劃者 |
| Oracle | GPT-5.4 high | 驗證者 |
| Atlas | Claude Sonnet | 多任務編排器 |
| Metis | GPT-5.4 high | 計劃顧問 |
| Momus | GPT-5.4 xhigh | QA 審查者 |
| Librarian | — | 文件/程式碼搜尋 |
| Explore | — | 快速 Grep |
| Multimodal Looker | GPT-5.4 medium | 圖像分析 |
| Sisyphus Junior | GPT-5.4/5.3-codex | 輕量編排 |

### 15.3 Category 模型映射

| Category | 預設模型 | 用途 |
|----------|---------|------|
| `visual-engineering` | 視覺類 | 前端 / UI / 設計 |
| `deep` | GPT-5.3-codex medium | 自主研究 + 執行 |
| `quick` | 輕量模型 | 單檔修改 |
| `ultrabrain` | GPT-5.4 xhigh | 困難邏輯 / 架構 |
| `unspecified-high` | GPT-5.4 high | 一般高強度 |
| `writing` | + Kimi fallback | 文件撰寫 |

### 15.4 Hook 一覽（25+ 內建）

| Hook | 類別 | 說明 |
|------|------|------|
| `context-injector` | Context | 自動注入 AGENTS.md, README |
| `comment-checker` | Quality | 拒絕 AI slop 註解 |
| `todo-enforcer` | Behavior | 閒置 Agent 強制拉回 |
| `todo-continuation` | Session | 任務持續執行 |
| `ultrawork-model-override` | Model | ultrawork 模型切換 |
| `hashline-read-enhancer` | Tool | 讀取時加入 LINE#ID |
| `hashline-edit` | Tool | 雜湊驗證編輯 |
| `ralph-loop` | Session | 自參考完成迴圈 |
| `read-image-resizer` | Tool | 圖像尺寸最佳化（僅解碼前 32KB） |
| `todo-description-override` | Behavior | 強制原子 todo 格式 |
| `preemptive-compaction` | Token | 自動壓縮過長上下文 |
| `auto-slash-command` | Behavior | 自動 slash command |
| `gpt-permission-continuation` | Session | GPT 權限自動續航 |

### 15.5 AGENTS.md 完整範例

```markdown
# Project: Enterprise Online Banking System

## Overview
企業網路銀行系統，提供帳戶管理、轉帳、繳費等功能。
服務 500 萬用戶，日均交易量 200 萬筆。

## Tech Stack
### Backend
- Language: Java 21（Virtual Threads enabled）
- Framework: Spring Boot 3.2.x + Spring Cloud 2023
- Security: Spring Security 6 + OAuth2 + JWT
- ORM: Spring Data JPA + Hibernate 6
- DB Migration: Flyway
- Cache: Redis Cluster
- Message: Apache Kafka

### Frontend
- Framework: Vue 3.4 + TypeScript 5
- UI: Element Plus
- State: Pinia
- Build: Vite 5

### Infrastructure
- Container: Docker + Kubernetes
- CI/CD: GitHub Actions
- Monitoring: Prometheus + Grafana
- Logging: ELK Stack

## Architecture
- Clean Architecture + DDD
- Microservices（12 services）
- REST（同步）+ Kafka（異步）
- CQRS + Event Sourcing（交易相關）

## Coding Standards
- Google Java Style Guide
- No Lombok
- Constructor Injection only
- All dates: java.time.*
- Response: ResponseEntity<ApiResponse<T>>
- Logging: SLF4J + Log4j2

## Security
- OWASP Top 10
- Parameterized Query only
- CSP Header + Output Encoding
- OAuth2 + JWT + 2FA
- AES-256 + TLS 1.3

## Testing
- Unit Test Coverage ≥ 80%
- JUnit 5 + Mockito
- Performance: P99 < 500ms
```

### 15.6 配置檔完整範例

```jsonc
// .opencode/oh-my-opencode.jsonc
{
  // Agent 覆蓋
  "agents": {
    "sisyphus": {
      "model": "claude-opus-4-6"
    },
    "hephaestus": {
      "model": "gpt-5.3-codex"
    }
  },

  // Skills
  "skills": {
    "enabled": ["playwright", "git-master", "frontend-ui-ux"]
  },

  // 停用的 Hooks
  "disabled_hooks": [],

  // 停用的 Tools
  "disabled_tools": [],

  // Background Tasks
  "background_tasks": {
    "concurrency": 5,
    "stale_timeout_ms": 1200000,
    "session_wait_ms": 60000
  },

  // Circuit Breaker
  "circuit_breaker": {
    "enabled": true
  },

  // 實驗性功能
  "experimental": {
    "hashline_edit": false,
    "aggressive_truncation": false
  }
}
```

### 15.7 相關資源連結

| 資源 | 連結 |
|------|------|
| GitHub Repository | https://github.com/code-yeongyu/oh-my-openagent |
| Releases | https://github.com/code-yeongyu/oh-my-openagent/releases |
| Installation Guide | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/guide/installation.md |
| Features Documentation | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/reference/features.md |
| Configuration Documentation | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/reference/configuration.md |
| Overview Guide | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/guide/overview.md |
| Orchestration Guide | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/guide/orchestration.md |
| Ultrawork Manifesto | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/manifesto.md |
| Contributing | https://github.com/code-yeongyu/oh-my-openagent/blob/dev/CONTRIBUTING.md |
| Discord | https://discord.gg/PUwSMR9XNk |
| DeepWiki | https://deepwiki.com/code-yeongyu/oh-my-openagent |
| Sisyphus Labs | https://sisyphuslabs.ai/ |

---

## 檢查清單（Checklist）

### 新手上路 - 快速開始

- [ ] 安裝 OpenCode CLI
- [ ] 在 OpenCode 配置中加入 `oh-my-opencode` 插件
- [ ] 執行 `/doctor` 驗證安裝
- [ ] 配置 LLM Provider（API Key）
- [ ] 在專案中執行 `/init-deep` 生成 AGENTS.md
- [ ] 試用 `/start-work`（Prometheus 規劃）
- [ ] 試用 `ultrawork`（全自動執行）

### 日常開發 Checklist

- [ ] 新功能先用 `/start-work` 規劃
- [ ] `ultrawork` 在獨立 Git branch 操作
- [ ] Oracle 驗證通過後再 commit
- [ ] Comment Checker 確認無 AI slop
- [ ] 人工 Review 所有 AI 產出
- [ ] 執行測試確認品質
- [ ] PR 通過 Quality Gate 再 Merge

### 專案配置 Checklist

- [ ] `AGENTS.md` 已透過 `/init-deep` 生成或手動撰寫
- [ ] `.opencode/oh-my-opencode.jsonc` 已配置
- [ ] Skills 已建立（如需要領域特定技能）
- [ ] `disabled_hooks` / `disabled_tools` 已依需求配置
- [ ] `circuit_breaker` 已啟用
- [ ] Background Tasks `concurrency` 已設定
- [ ] CI/CD 整合已完成（Quality Gate + Security Scan）
- [ ] Git hooks 已安裝（Pre-commit Secret Scan）

### 上線前 Checklist

- [ ] 所有 AI 產出程式碼通過 Code Review
- [ ] 單元測試覆蓋率 ≥ 80%
- [ ] 整合測試通過
- [ ] SAST 掃描無 Critical / High 問題
- [ ] 依賴套件無已知漏洞
- [ ] Secret Scan 通過
- [ ] 效能測試通過（P99 < SLA 門檻）
- [ ] AGENTS.md 已同步更新
- [ ] 變更記錄已載入 CHANGELOG

---

> **文件結束**  
> 本文件為 oh-my-openagent（OMO）企業導入教學手冊。  
> 基於 GitHub Repository v3.12.3 版本資訊撰寫。  
> 如有疑問，請參考 [官方文件](https://github.com/code-yeongyu/oh-my-openagent) 或加入 [Discord 社群](https://discord.gg/PUwSMR9XNk)。  
> **最後更新**：2026-3-24 | **版本**：v2.0

