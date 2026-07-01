+++
date = '2026-04-21T14:30:24+08:00'
draft = false
title = 'GSD Pi 教學手冊（原 GSD-2）'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# GSD Pi 教學手冊（Enterprise Edition）

> **版本**：v1.3.0（open-gsd/gsd-pi 基線） ｜ **最後更新**：2026-07-01
> **適用對象**：資深後端 / 前端 / 架構師 / DevOps 工程師
> **授權**：MIT License
> **官方網站**：[www.opengsd.net](https://www.opengsd.net/) ｜ **Web 配置器**：[pi.opengsd.net](https://pi.opengsd.net/)

> ⚠️ **重要公告**：GSD-2 專案已於 2026 年 5 月遷移至新的組織與倉庫。原 `gsd-build/gsd-2`（v3.0.0 最終版，7.7k Stars，已封存）不再是活躍開發地點，所有後續開發、Issues、Releases 皆在 [`open-gsd/gsd-pi`](https://github.com/open-gsd/gsd-pi) 進行。npm 套件名稱也從 `gsd-pi` 更名為 `@opengsd/gsd-pi`。本文件已依據最新版本 **v1.3.0**（2026-06-21）全面更新。

---

## 目錄

- [1. 總覽（Overview）](#1-總覽overview)
  - [1.1 GSD Pi 是什麼](#11-gsd-pi-是什麼)
  - [1.2 與傳統開發模式差異](#12-與傳統開發模式差異)
  - [1.3 適用場景](#13-適用場景)
  - [1.4 版本演進與生態系](#14-版本演進與生態系)
  - [1.5 從 GSD-2 遷移至 GSD Pi](#15-從-gsd-2-遷移至-gsd-pi)
- [2. 核心概念（Core Concepts）](#2-核心概念core-concepts)
  - [2.1 Meta Prompting](#21-meta-prompting)
  - [2.2 Context Engineering](#22-context-engineering)
  - [2.3 Spec-Driven Development](#23-spec-driven-development)
  - [2.4 Agent Workflow](#24-agent-workflow)
  - [2.5 Knowledge Graph（KNOWLEDGE.md）](#25-knowledge-graphknowledgemd)
  - [2.6 Reactive Task Execution](#26-reactive-task-execution)
  - [2.7 Context Pressure Monitor](#27-context-pressure-monitor)
  - [2.8 Planning Depth — 深度探索模式](#28-planning-depth--深度探索模式)
  - [2.9 Per-Phase Thinking Level — 分階段思考深度](#29-per-phase-thinking-level--分階段思考深度)
- [3. 系統架構設計（Architecture）](#3-系統架構設計architecture)
  - [3.1 GSD Pi 內部架構](#31-gsd-pi-內部架構)
  - [3.2 GSD Pi + 微服務架構整合](#32-gsd-pi--微服務架構整合)
  - [3.3 與 Spring Boot 架構整合方式](#33-與-spring-boot-架構整合方式)
  - [3.4 與前端（Vue）協作方式](#34-與前端vue協作方式)
  - [3.5 與 CI/CD 整合方式](#35-與-cicd-整合方式)
  - [3.6 與 SSDLC 整合方式](#36-與-ssdlc-整合方式)
  - [3.7 MCP Server 架構](#37-mcp-server-架構)
  - [3.8 Cloud MCP Gateway 架構](#38-cloud-mcp-gateway-架構)
- [4. 安裝與環境建置（Installation）](#4-安裝與環境建置installation)
  - [4.1 系統需求](#41-系統需求)
  - [4.2 安裝步驟](#42-安裝步驟)
  - [4.3 從舊版遷移安裝](#43-從舊版遷移安裝)
  - [4.4 首次啟動與設定](#44-首次啟動與設定)
  - [4.5 MCP Server 啟動](#45-mcp-server-啟動)
  - [4.6 VS Code 擴充設定](#46-vs-code-擴充設定)
  - [4.7 與 Claude Code / Copilot 整合](#47-與-claude-code--copilot-整合)
  - [4.8 Docker Sandbox 部署](#48-docker-sandbox-部署)
  - [4.9 Web 介面啟動](#49-web-介面啟動)
  - [4.10 常見安裝問題與排除](#410-常見安裝問題與排除)
- [5. 專案初始化（Project Setup）](#5-專案初始化project-setup)
  - [5.1 專案目錄結構](#51-專案目錄結構)
  - [5.2 GSD 標準檔案說明](#52-gsd-標準檔案說明)
  - [5.3 初始化流程](#53-初始化流程)
- [6. Spec-Driven 開發流程](#6-spec-driven-開發流程)
  - [6.1 整體流程概覽](#61-整體流程概覽)
  - [6.2 步驟 1：撰寫規格（Spec）](#62-步驟-1撰寫規格spec)
  - [6.3 步驟 2：拆解任務（Tasks）](#63-步驟-2拆解任務tasks)
  - [6.4 步驟 3：指派 AI Agent](#64-步驟-3指派-ai-agent)
  - [6.5 步驟 4：產生程式碼](#65-步驟-4產生程式碼)
  - [6.6 步驟 5：測試與驗證](#66-步驟-5測試與驗證)
  - [6.7 步驟 6：回饋到 KNOWLEDGE.md](#67-步驟-6回饋到-knowledgemd)
- [7. AI Agent 協作模式](#7-ai-agent-協作模式)
  - [7.1 多 Agent 協作架構](#71-多-agent-協作架構)
  - [7.2 Claude Code 使用方式](#72-claude-code-使用方式)
  - [7.3 Copilot 使用方式](#73-copilot-使用方式)
  - [7.4 Agent 任務切分策略](#74-agent-任務切分策略)
  - [7.5 雙終端機工作流](#75-雙終端機工作流)
  - [7.6 Quick Mode — 快速任務](#76-quick-mode--快速任務)
  - [7.7 Session 可觀察性命令](#77-session-可觀察性命令)
  - [7.8 Telegram 遠端控制](#78-telegram-遠端控制)
  - [7.9 Web 介面管理](#79-web-介面管理)
  - [7.10 思緒捕捉（Capture）與工作流視覺化](#710-思緒捕捉capture與工作流視覺化)
  - [7.11 Visual Briefs — 視覺化簡報產出](#711-visual-briefs--視覺化簡報產出)
  - [7.12 自訂工作流插件（Custom Workflows）](#712-自訂工作流插件custom-workflows)
- [8. 知識圖譜與學習系統](#8-知識圖譜與學習系統)
  - [8.1 KNOWLEDGE.md 設計方式](#81-knowledgemd-設計方式)
  - [8.2 記憶架構（v2.77 ADR-013）](#82-記憶架構v277-adr-013)
  - [8.3 Knowledge Graph 建立](#83-knowledge-graph-建立)
  - [8.4 如何提升 AI 理解能力](#84-如何提升-ai-理解能力)
- [9. 技能管理（Skill Management）](#9-技能管理skill-management)
  - [9.1 技能系統概述](#91-技能系統概述)
  - [9.2 技能發現與 Skill Rules](#92-技能發現與-skill-rules)
  - [9.3 技能評估方式](#93-技能評估方式)
  - [9.4 Agent 健康度監控](#94-agent-健康度監控)
  - [9.5 擴充套件管理（Extensions）](#95-擴充套件管理extensions)
- [10. 實戰範例](#10-實戰範例)
- [11. SSDLC 整合（安全開發）](#11-ssdlc-整合安全開發)
- [12. 系統維護（Maintenance）](#12-系統維護maintenance)
  - [12.1 如何更新 Spec](#121-如何更新-spec)
  - [12.2 如何修復 Bug](#122-如何修復-bug)
  - [12.3 Forensics — 失敗調查](#123-forensics--失敗調查)
  - [12.4 如何讓 AI 持續學習](#124-如何讓-ai-持續學習)
  - [12.5 Provider Error Recovery](#125-provider-error-recovery)
  - [12.6 Failure Recovery](#126-failure-recovery)
  - [12.7 Pipeline Architecture](#127-pipeline-architecture)
  - [12.8 清理與歸檔](#128-清理與歸檔)
  - [12.9 Token Telemetry 與成本追蹤](#129-token-telemetry-與成本追蹤)
  - [12.10 Unit Closeout 模組](#1210-unit-closeout-模組)
- [13. 系統升級（Upgrade）](#13-系統升級upgrade)
  - [13.1 從 gsd-build/gsd-2 遷移到 open-gsd/gsd-pi](#131-從-gsd-buildgsd-2-遷移到-open-gsdgsd-pi)
- [14. 最佳實務（Best Practices）](#14-最佳實務best-practices)
  - [14.1 Prompt 設計原則](#141-prompt-設計原則)
  - [14.2 Context 控制技巧](#142-context-控制技巧)
  - [14.3 避免 Hallucination](#143-避免-hallucination)
  - [14.4 大型專案管理技巧](#144-大型專案管理技巧)
  - [14.5 成本控制](#145-成本控制)
  - [14.6 Hooks 系統](#146-hooks-系統)
  - [14.7 Reactive Task Execution 實務](#147-reactive-task-execution-實務)
  - [14.8 企業指引範本](#148-企業指引範本)
  - [14.9 Per-Model MCP 過濾與 URL 安全](#149-per-model-mcp-過濾與-url-安全)
- [15. 常見問題（FAQ）](#15-常見問題faq)
  - [15.1 AI 不照 Spec 怎麼辦？](#151-ai-不照-spec-怎麼辦)
  - [15.2 程式碼品質不佳？](#152-程式碼品質不佳)
  - [15.3 Context 過大怎麼辦？](#153-context-過大怎麼辦)
  - [15.4 Auto Mode 卡住怎麼辦？](#154-auto-mode-卡住怎麼辦)
  - [15.5 如何恢復崩潰的 Session？](#155-如何恢復崩潰的-session)
  - [15.6 團隊成員 Milestone ID 衝突？](#156-團隊成員-milestone-id-衝突)
  - [15.7 如何在企業防火牆環境使用？](#157-如何在企業防火牆環境使用)
  - [15.8 如何使用本地 LLM（Ollama）？](#158-如何使用本地-llmollama)
- [16. 團隊導入建議（Enterprise Adoption）](#16-團隊導入建議enterprise-adoption)
  - [16.1 導入策略（分階段）](#161-導入策略分階段)
  - [16.2 教育訓練方式](#162-教育訓練方式)
  - [16.3 Governance（治理）](#163-governance治理)
- [17. 檢查清單（Checklist）](#17-檢查清單checklist)
  - [17.1 環境建置 Checklist](#171-環境建置-checklist)
  - [17.2 專案初始化 Checklist](#172-專案初始化-checklist)
  - [17.3 日常開發 Checklist](#173-日常開發-checklist)
  - [17.4 安全 Checklist](#174-安全-checklist)
  - [17.5 團隊協作 Checklist](#175-團隊協作-checklist)
  - [17.6 GSD Pi 命令速查表](#176-gsd-pi-命令速查表)
- [附錄 A：GSD Pi 內建擴充套件一覽](#附錄-agsd-pi-內建擴充套件一覽)
- [附錄 B：相關資源](#附錄-b相關資源)
- [附錄 C：MCP Server 設定指南](#附錄-cmcp-server-設定指南)
  - [C.1 概述](#c1-概述)
  - [C.2 連線外部 MCP Server](#c2-連線外部-mcp-server)
  - [C.3 驗證 MCP 連線](#c3-驗證-mcp-連線)
  - [C.4 匯入其他工具的 MCP 設定](#c4-匯入其他工具的-mcp-設定)
  - [C.5 Cloud MCP Gateway](#c5-cloud-mcp-gateway)
  - [C.6 企業注意事項](#c6-企業注意事項)
- [附錄 D：進階設定參考](#附錄-d進階設定參考)
  - [D.1 Dynamic Model Routing](#d1-dynamic-model-routing)
  - [D.2 Notifications](#d2-notifications)
  - [D.3 Context Management](#d3-context-management)
  - [D.4 Git 進階設定](#d4-git-進階設定)
  - [D.5 GitHub Sync](#d5-github-sync)
  - [D.6 Forensics 和除錯](#d6-forensics-和除錯)
  - [D.7 Parallel Orchestration](#d7-parallel-orchestration)
  - [D.8 Custom Model Definitions](#d8-custom-model-definitions)
  - [D.9 其他設定](#d9-其他設定)
- [附錄 E：環境變數一覽](#附錄-e環境變數一覽)

---

## 1. 總覽（Overview）

### 1.1 GSD Pi 是什麼

GSD Pi（前稱 GSD-2，Get Stuff Done，採用 [Pi SDK](https://github.com/badlogic/pi-mono)）是一套 **Meta-Prompting、Context Engineering 與 Spec-Driven Development** 系統，專為 AI Agent 長時間自主開發而設計。它不是提示框架（Prompt Framework），而是一個獨立的 **TypeScript CLI 應用程式**，能夠真正控制 Agent 的 Context Window、Session 生命週期與 Git 策略。

2026 年 5 月，專案從 `gsd-build/gsd-2` 遷移至 [`open-gsd/gsd-pi`](https://github.com/open-gsd/gsd-pi)，以全新 v1.0.0 為基線重新出發。npm 套件名稱同步更名為 `@opengsd/gsd-pi`，舊有的 `gsd-pi` 不再維護。

核心能力：

| 能力 | 說明 |
|------|------|
| **Context Engineering** | 每個任務（Task）使用全新的 200K Token Context Window，自動預載相關檔案 |
| **Auto Mode** | 狀態機驅動，自動研究 → 規劃 → 執行 → 驗證 → 提交 → 下一輪 |
| **Crash Recovery** | Lock 檔 + Session Forensics，中斷後自動恢復 |
| **Cost Tracking** | 逐任務追蹤 Token 用量與費用，Dashboard 即時呈現 |
| **Git Isolation** | Worktree / Branch 隔離，Milestone 完成後 Squash Merge |
| **MCP Server** | 支援 Model Context Protocol，可與 Claude Desktop / VS Code Copilot 整合 |
| **Knowledge Graph** | LEARNINGS.md / KNOWLEDGE.md 轉化為知識圖譜供 AI 持續學習 |
| **Reactive Execution** | 基於依賴圖譜的平行任務執行（預設啟用），同一 Slice 內無衝突任務同時運行 |
| **Web Interface** | 瀏覽器介面，視覺化專案管理與即時進度追蹤 |
| **Telegram Remote** | 透過 Telegram / Slack / Discord 遠端控制 Auto Mode |
| **Hooks System** | Pre-dispatch / Post-unit / Layer 0 Shell Hooks，支援自訂自動化流程 |
| **GitHub Sync** | 自動同步 Milestone 到 GitHub Issues、PR 與 Milestones |
| **Cloud MCP Gateway** | 內建雲端 MCP Gateway Runtime，管理遠端 MCP 伺服器生命週期 |
| **Visual Briefs** | `/gsd brief` 產生 Mermaid 視覺化簡報，自動剖析專案結構 |
| **Custom Workflows** | 統一的工作流插件系統，支援安裝 / 管理自訂範本 |
| **Per-Model MCP 過濾** | 每個模型可獨立指定允許使用的 MCP 工具子集 |
| **Extensions 管理** | `/gsd extensions` 安裝、移除、更新擴充套件 |
| **Planning Depth** | `planning_depth: deep` 啟用分階段專案探索，深度分析後再規劃 |
| **Per-Phase Thinking** | 每個階段（planning / execution / completion）可獨立設定 `thinking_level`，平衡推理深度與成本（v1.2.0） |
| **Planner Handoff** | 規劃與執行明確分離，Planner Agent 完成後移交給 Worker Agent（v1.2.0） |
| **Unit Closeout** | 互動式工作項目收尾模組，確保每個 Task 的產出完整且記錄清晰（v1.3.0） |
| **Claude Fable 5** | 支援 Claude Fable 5（Opus-tier 思考能力），可指定為 planning 模型（v1.3.0） |
| **MiniMax M3** | 支援 MiniMax M3 模型，擴展多元 Provider 選擇（v1.2.0） |
| **Tool Surface Readiness** | SDK 初始化時驗證所有工具介面就緒，避免分派至無回應工具（v1.3.0） |
| **Session Observability** | `/gsd usage` 查看 Session 用量、`/gsd context` 查看 Context 狀態（v1.1.0） |

### 1.2 與傳統開發模式差異

| 面向 | 傳統開發 | GSD-1（Prompt Framework） | GSD Pi（v1.3.0） |
|------|----------|--------------------------|-------------------|
| 執行方式 | 人工編碼 | Claude Code Slash Commands | 獨立 CLI（Pi SDK） |
| Context 管理 | N/A | 希望 LLM 不要塞滿 | 每任務全新 Session，程式化注入 |
| 自動模式 | 無 | LLM 自我迴圈 | 狀態機讀取 `.gsd/` 檔案 |
| 崩潰恢復 | 無 | 無 | Lock 檔 + Session Forensics |
| Git 策略 | 人工 | LLM 寫 Git 指令 | Worktree 隔離、逐次提交、Squash Merge |
| 成本追蹤 | 無 | 無 | 逐單元 Token / 成本帳本 + Telemetry |
| 卡住偵測 | 無 | 無 | 滑動窗口偵測 + 診斷重試 |
| 驗證 | 人工 | 人工 | 自動驗證指令 + Auto-fix 重試 |
| 報告 | 無 | 無 | 自包含 HTML 報告（含指標與依賴圖） |
| 平行執行 | 無 | 無 | 多 Worker 平行 Milestone 編排（預設啟用） |
| Web 介面 | N/A | 無 | 瀏覽器專案管理 + 即時進度 |
| 遠端控制 | N/A | 無 | Telegram / Slack / Discord 控制 |
| Hooks 系統 | N/A | 無 | Pre-dispatch + Post-unit + Layer 0 Shell |
| GitHub 同步 | 人工 | 無 | 自動同步 Issues / PR / Milestones |
| 視覺化簡報 | N/A | 無 | Visual Briefs — Mermaid 架構圖自動產出 |
| 擴充管理 | N/A | 無 | `/gsd extensions` 統一管理擴充套件 |

### 1.3 適用場景

- **企業級大型系統開發**：微服務、前後端分離、多資料庫
- **AI Agent 長時間自主任務**：一個指令、離開、回來看成品
- **複雜重構與遷移**：大規模程式碼搬遷、框架升級
- **DevSecOps 自動化**：CI/CD 整合 Headless 模式
- **多人團隊協作**：Unique Milestone ID、共享 `.gsd/` Artifacts

> **💡 實務建議**：GSD Pi 最適合「一個 Milestone 可拆為 4-10 個 Slice、每個 Slice 1-7 個 Task」的中大型任務。小型單次修改建議使用 `/gsd quick`。

### 1.4 版本演進與生態系

GSD 專案歷經兩大階段。原始倉庫 `gsd-build/gsd-2` 累積發佈 **116 個版本**（至 v3.0.0），2026 年 5 月遷移至 `open-gsd/gsd-pi`，以 v1.0.0 為新基線重新出發。目前新倉庫已獲得 **389 Stars**、**98 位 Contributors**，TypeScript 佔比 94.2%。

**版本演進里程碑**：

| 階段 | 版本 | 重點特性 |
|------|------|----------|
| **舊倉庫** | v2.26 | Verification Enforcement、Crash Recovery、HTML Reports |
| | v2.28 | Failure Recovery（原子寫入、OAuth 超時）、Headless Auto-restart |
| | v2.38 | Reactive Task Execution（平行任務圖譜）|
| | v2.39 | Stuck Detection、RUNTIME.md、GitHub Sync、Skill Activation |
| | v2.40 | Pipeline Architecture、Post-Mortem Forensics |
| | v2.59 | Context Management（Observation Masking、Compaction）|
| | v2.77 | Context Mode、Memory Architecture ADR-013、Hook Stack 升級 |
| | v3.0.0 | 最終版本，整合至 open-gsd/gsd-pi |
| **新倉庫** | v1.0.0 | 新基線：Cloud MCP Gateway、gsd-browser、Per-Model MCP 過濾、Custom Workflows 插件、Visual Briefs、Extensions 管理、`planning_depth: deep`、Workspace multi-repo、Custom Model Definitions（models.json）、Ollama 支援、Community Provider Extensions、Token Telemetry、In-session update、cmux 整合 |
| | v1.0.2 | Bug fixes：修復 worktree checkout 問題、改進 headless recover、修正 theme config 讀取 |
| | v1.1.0 | Claude Opus 4.8 支援、`/gsd usage` 和 `/gsd context` 可觀察性命令、ADR-010 seam 修復、Cloud MCP Gateway 本地 Runtime 能力 |
| | v1.1.1 | npm 發佈 tarball 同步修補（穩定性修正） |
| | v1.2.0 | Per-phase thinking level 設定、Planner Handoff（規劃與執行明確分離）、Managed gsd-browser 引擎、MiniMax M3 模型支援、TUI 工具軌道即時顯示 |
| | v1.3.0 | Claude Fable 5 支援（Opus-tier 思考）、Unit Closeout 互動式收尾模組、Tool Surface Readiness Gate（SDK 初始化驗證）、Shell 工具改善（uncapped bash、可中斷等待、優雅終止）、PATH gsd-browser 路徑修復 |

**生態系**：

| 元件 | 說明 |
|------|------|
| [`@opengsd/gsd-pi`](https://www.npmjs.com/package/@opengsd/gsd-pi) (npm) | 核心 CLI 套件（Scoped Package） |
| [pi.opengsd.net](https://pi.opengsd.net/) | Web 配置器 — 線上互動式設定產生 |
| [www.opengsd.net](https://www.opengsd.net/) | 官方文件網站 |
| VS Code Extension | FluxLabs 發佈，Chat Participant + Sidebar Dashboard |
| Docker Sandbox | 隔離容器執行環境 |
| Web Interface | 瀏覽器專案管理介面（`gsd --web`） |
| Cloud MCP Gateway | 雲端 MCP 伺服器生命週期管理 |
| gsd-browser | 內建瀏覽器 MCP Server（Playwright） |
| Custom Workflows | 統一工作流插件系統 |
| Community Providers | 社群擴充（如 `pi-dashscope`） |
| [Discord](https://discord.gg/8NnkKuepmQ) | 社群支援頻道 |

### 1.5 從 GSD-2 遷移至 GSD Pi

若您仍在使用舊版 `gsd-pi`（來自 `gsd-build/gsd-2`），請依以下步驟遷移：

```bash
# 1. 解除安裝舊版
npm uninstall -g gsd-pi

# 2. 安裝新版（Scoped Package）
npm install -g @opengsd/gsd-pi@latest

# 3. 驗證版本
gsd --version
# 應顯示 v1.0.x

# 4. 執行健康檢查
gsd
/gsd doctor
```

**注意事項**：
- 所有 `.gsd/` 目錄結構和 `PREFERENCES.md` 格式向下相容
- `reactive_execution` 設定格式已從布林值改為物件（詳見 §2.6）
- 舊版 `gsd-build/gsd-2` 已存檔，不再接受 Issues 或 PR

---

## 2. 核心概念（Core Concepts）

### 2.1 Meta Prompting

Meta Prompting 指的是「產生 Prompt 的 Prompt」。GSD Pi 不是讓開發者手寫每一步的指令，而是透過 **Spec → Roadmap → Slice Plan → Task Plan** 的層級結構，自動為每個任務生成精準的 Dispatch Prompt。

```
開發者撰寫 Spec（高階需求）
       ↓
GSD 自動拆解為 Milestone / Slice / Task
       ↓
每個 Task 的 Dispatch Prompt 自動包含：
  - Task Plan + Must-haves
  - 前置 Task Summary
  - 相關檔案（預載入）
  - 架構決策（DECISIONS.md）
  - 知識庫（KNOWLEDGE.md）
```

### 2.2 Context Engineering

Context Engineering 是 GSD Pi 的核心差異化能力。每次 Dispatch 時，系統會自動建構最適合的 Context：

```mermaid
graph LR
    A[STATE.md] --> D[Dispatch Prompt]
    B[ROADMAP.md] --> D
    C[Slice Plan] --> D
    E[Task Plan] --> D
    F[Prior Summaries] --> D
    G[DECISIONS.md] --> D
    H[KNOWLEDGE.md] --> D
    I[RUNTIME.md] --> D
    D --> J[LLM 執行]
```

**Context Mode**：自動拉取最相關的專案 Artifacts、先前 Session 狀態、Milestone/Slice 信號與執行 Metadata，減少手動組裝 Prompt 的需要。新專案預設啟用。

### 2.3 Spec-Driven Development

規格驅動開發（Spec-Driven Development）的核心原則：

1. **先寫規格，再寫程式碼**：所有開發工作都從 Spec 開始
2. **機械式可驗證**：每個 Task 都有 Must-haves（Truths、Artifacts、Key Links）
3. **自動拆解**：GSD 將 Spec 自動拆為可執行的 Task 層級結構

```
Milestone  →  一個可交付版本（4-10 slices）
  Slice    →  一個可展示的垂直功能（1-7 tasks）
    Task   →  一個 Context Window 大小的工作單元
```

**鐵律**：一個 Task 必須能在一個 Context Window 內完成。如果不能，就拆成兩個 Task。

### 2.4 Agent Workflow

GSD Pi 的工作流程是一個自動推進的狀態機：

```mermaid
graph TD
    A[Plan<br/>整合研究 + 拆解任務] --> B[Execute<br/>逐 Task 執行]
    B --> C[Complete<br/>摘要 + UAT + 提交]
    C --> D[Reassess Roadmap<br/>重新評估計畫]
    D --> E{所有 Slice 完成?}
    E -->|否| A
    E -->|是| F[Validate Milestone<br/>對照成功標準]
    F --> G[Complete Milestone]
```

### 2.5 Knowledge Graph（KNOWLEDGE.md）

GSD Pi 使用 `KNOWLEDGE.md` 作為跨 Session 的知識庫：

- **自動學習**：每個 Task 完成後，提取的教訓自動寫入
- **結構化記憶**：`structured_fields` 支援型別化 Metadata
- **持久化**：所有記憶讀寫透過 `memories` 表格作為唯一事實來源
- **跨 Agent 共享**：所有 Agent、工具與 UI 表面共享同一記憶狀態
- **知識條目管理**：透過 `/gsd knowledge <type> <desc>` 快速新增 rule / pattern / lesson

> **💡 實務建議**：在企業環境中，建議將 `KNOWLEDGE.md` 和 `DECISIONS.md` 納入版本控制，確保團隊知識不會因為人員異動而流失。

### 2.6 Reactive Task Execution

Reactive Task Execution 是 GSD Pi 的平行任務執行機制。系統會從任務計畫中的 IO 註解衍生出依賴圖譜，並自動將無衝突的任務平行分發。**GSD Pi v1.0 預設啟用此功能**。

```mermaid
graph TD
    subgraph "Slice S01 依賴圖譜"
        T1[T01: Domain Entity] --> T2[T02: Repository 介面]
        T1 --> T3[T03: Value Objects]
        T2 --> T4[T04: JPA 實作]
        T3 --> T4
        T4 --> T5[T05: Controller]
    end

    subgraph "平行批次"
        B1[Batch 1] -.-> T1
        B2[Batch 2] -.-> T2
        B2 -.-> T3
        B3[Batch 3] -.-> T4
        B4[Batch 4] -.-> T5
    end
```

**設定方式**：

```yaml
# .gsd/PREFERENCES.md — 新格式（物件）
reactive_execution:
  enabled: true               # 預設啟用
  max_parallel: 3             # 最大平行數
  isolation_mode: worktree    # worktree | branch
  subagent_model: ""          # 可指定 Subagent 使用的模型
```

> **⚠️ 向下相容**：舊格式 `reactive_execution: true`（布林值）仍可使用，系統會自動轉換為物件格式。

**核心特性**：

- **純函數圖譜衍生**：確定性的依賴解析，無副作用
- **衝突偵測**：自動識別共享檔案讀寫衝突
- **死鎖防護**：內建循環依賴偵測
- **驗證傳遞**：平行批次間驗證結果自動傳遞，避免重複驗證

> **⚠️ 注意**：Reactive Execution 適合檔案分離度高的專案。若多個 Task 頻繁修改相同檔案，建議維持循序執行。

### 2.7 Context Pressure Monitor

Context Pressure Monitor 監控 Context Window 使用率，防止 Session 在任務中途因 Context 耗盡而無產出：

```
Context 使用率:
  0% ─────── 70% ───── 80% ───── 100%
       正常    │  包裝信號  │  暫停點   │  硬限制
               │           │           │
            自動發送      可選暫停     強制中斷
           包裝提示      檢查點
```

**運作機制**：

1. **70% 閾值**：發送包裝信號（Wrap-up Signal），引導 LLM 完成持久化產出（提交、撰寫摘要）
2. **80% 閾值**（可設定）：觸發 `context_pause_threshold` 暫停，進行檢查點

```yaml
# .gsd/PREFERENCES.md
context_pause_threshold: 80    # 設為 0 停用（預設）
```

### 2.8 Planning Depth — 深度探索模式

GSD Pi 新增 `planning_depth: deep` 設定，啟用分階段的專案探索流程。在規劃前先進行多輪遞迴式的程式碼庫分析，確保 AI 對大型或陌生專案建立足夠的上下文理解：

```yaml
# .gsd/PREFERENCES.md
planning_depth: deep    # normal（預設）| deep
```

**Deep 模式運作流程**：

1. **Phase 1 — Codebase Discovery**：掃描目錄結構、建置設定、依賴關係
2. **Phase 2 — Architecture Analysis**：識別模組邊界、API 端點、資料模型
3. **Phase 3 — Risk Assessment**：評估複雜度、耦合度、潛在風險
4. **Phase 4 — Plan Generation**：基於前三階段的理解產出精準計畫

> **💡 實務建議**：對初次接手的大型專案（>50K LOC）建議啟用 `deep` 模式。雖然規劃時間較長，但後續執行的 Task 品質與準確度顯著提升。

### 2.9 Per-Phase Thinking Level — 分階段思考深度

GSD Pi v1.2.0 新增 Per-Phase Thinking Level 設定，允許針對不同執行階段獨立配置 LLM 的思考深度（reasoning effort），在推理品質與 Token 成本之間精準取得平衡。

**設定方式**：

```yaml
# .gsd/PREFERENCES.md
phases:
  planning:
    thinking_level: high       # 規劃階段：深度推理，確保架構正確
  execution:
    thinking_level: medium     # 執行階段：平衡品質與成本
  completion:
    thinking_level: low        # 完成階段：快速產出摘要與提交
```

**Thinking Level 對應說明**：

| Level | 說明 | 適用階段 | Token 消耗 |
| ----- | ---- | -------- | ---------- |
| `high` | 完整延伸思考（Extended Thinking） | Planning、架構設計 | 高 |
| `medium` | 標準推理 | Execution、一般開發 | 中 |
| `low` | 快速回應，無延伸思考 | Completion、文件產生 | 低 |

**核心優勢**：

- **成本優化**：Completion 階段通常只需產生摘要和提交訊息，降至 `low` 可節省 30–50% Token
- **品質保障**：Planning 階段最重要，設定 `high` 確保架構決策正確
- **靈活配置**：支援與 `claude-fable-5`（v1.3.0）、`claude-opus-4-8`（v1.1.0）等高能力模型搭配使用

> **💡 實務建議**：企業環境中建議 planning 搭配 `claude-fable-5` + `thinking_level: high`，execution 使用 `claude-sonnet-4-6` + `thinking_level: medium`，completion 使用任何快速模型 + `thinking_level: low`。此組合在品質與成本之間達到最佳平衡。

---

## 3. 系統架構設計（Architecture）

### 3.1 GSD Pi 內部架構

GSD Pi 是一個 TypeScript 應用程式，嵌入 Pi Coding Agent SDK：

```
gsd (CLI binary)
  └─ loader.ts          設定 PI_PACKAGE_DIR、GSD 環境變數，動態載入 cli.ts
      └─ cli.ts         連接 SDK 管理器、載入擴充套件、啟動 InteractiveMode
          ├─ headless.ts       Headless 編排器（CI/cron/腳本）
          ├─ onboarding.ts     首次執行設定精靈
          ├─ wizard.ts         環境填充（auth.json 認證）
          ├─ app-paths.ts      ~/.gsd/agent/、~/.gsd/sessions/、auth.json
          ├─ resource-loader.ts 同步內建擴充套件 + Agent
          └─ src/resources/
              ├─ extensions/gsd/    核心 GSD 擴充（auto、state、commands…）
              ├─ extensions/...     21 個支援擴充
              ├─ agents/            scout、researcher、worker、javascript-pro、typescript-pro
              └─ GSD-WORKFLOW.md    手動引導協議
```

關鍵設計決策：

- **狀態儲存在磁碟**：`.gsd/` 是唯一事實來源，Auto Mode 讀寫並基於內容推進
- **每次啟動同步**：`npm update -g` 後立即生效，內建擴充每次啟動都同步到 `~/.gsd/agent/`
- **雙檔載入模式**：`loader.ts` 零 SDK 匯入設定環境變數，再動態載入 `cli.ts`

### 3.2 GSD Pi + 微服務架構整合

```mermaid
graph TB
    subgraph "開發者工作站"
        DEV[開發者] --> GSD[GSD Pi CLI]
        GSD --> VSCODE[VS Code Extension]
        GSD --> TERM2[Terminal 2 — 導引]
    end

    subgraph "GSD Pi Core"
        GSD --> AUTO[Auto Mode 狀態機]
        AUTO --> DISPATCH[Dispatch Engine]
        DISPATCH --> LLM[LLM Provider<br/>Anthropic / OpenAI / OpenRouter]
    end

    subgraph "專案結構 .gsd/"
        DISPATCH --> STATE[STATE.md]
        DISPATCH --> ROADMAP[M001-ROADMAP.md]
        DISPATCH --> KNOWLEDGE[KNOWLEDGE.md]
        DISPATCH --> DECISIONS[DECISIONS.md]
    end

    subgraph "企業微服務架構"
        direction TB
        FE[Vue 3 + TypeScript<br/>Tailwind CSS] --> API[Spring Boot 3.5<br/>RESTful API]
        API --> SVC1[Service A]
        API --> SVC2[Service B]
        SVC1 --> DB1[(Oracle / PostgreSQL)]
        SVC2 --> DB2[(DB2 / SQL Server)]
        SVC1 --> CACHE[(Redis)]
        SVC1 --> MQ[Kafka / RabbitMQ]
    end

    subgraph "CI/CD Pipeline"
        GH_ACTIONS[GitHub Actions] --> BUILD[Build & Test]
        BUILD --> SCAN[SAST / DAST / SonarQube]
        SCAN --> DEPLOY[Deploy to Container]
        DEPLOY --> PODMAN[Podman]
    end

    GSD -->|生成程式碼| FE
    GSD -->|生成程式碼| API
    GSD -->|Headless Mode| GH_ACTIONS
```

### 3.3 與 Spring Boot 架構整合方式

GSD Pi 透過 Spec-Driven 方式與 Spring Boot Clean Architecture 整合：

```yaml
# .gsd/PREFERENCES.md 中的驗證指令
verification_commands:
  - mvn compile
  - mvn test
  - mvn checkstyle:check
```

GSD 在 Task 執行完畢後自動執行上述指令，失敗時自動修復重試。

**整合流程**：

1. 在 `AGENTS.md` 中定義 Spring Boot 開發規範（Clean Architecture 層級、命名慣例）
2. GSD 規劃 Slice 時會參考 `AGENTS.md` 中的架構規範
3. 每個 Task 產生的程式碼自動通過 `mvn compile` + `mvn test` 驗證
4. ArchUnit 測試確保架構合規性

### 3.4 與前端（Vue）協作方式

```yaml
# 前端專案 .gsd/PREFERENCES.md
verification_commands:
  - npm run lint
  - npm run type-check
  - npm run test:unit
```

GSD 可同時管理前後端：

- **方案 A — 單一 Repo**：前後端在同一 Milestone，不同 Slice 處理
- **方案 B — 多 Repo**：各自獨立 GSD 實例，API Spec（OpenAPI）作為契約

### 3.5 與 CI/CD 整合方式

使用 GSD Headless Mode 整合 GitHub Actions：

```yaml
# .github/workflows/gsd-auto.yml
name: GSD Auto Build
on:
  workflow_dispatch:
    inputs:
      milestone:
        description: 'Milestone context file'
        required: true

jobs:
  gsd-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '24'

      - name: Install GSD Pi
        run: npm install -g @opengsd/gsd-pi@latest

      - name: Run GSD Headless
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          gsd headless new-milestone \
            --context ${{ inputs.milestone }} \
            --auto \
            --timeout 600000
```

Headless Mode 退出碼：

| 退出碼 | 意義 |
|--------|------|
| `0` | 完成 |
| `1` | 錯誤 / 超時 |
| `2` | 被阻擋（需人工介入） |

### 3.6 與 SSDLC 整合方式

```mermaid
graph LR
    subgraph "SSDLC Pipeline"
        REQ[需求分析] --> DESIGN[安全設計]
        DESIGN --> DEV[安全開發]
        DEV --> TEST[安全測試]
        TEST --> DEPLOY[安全部署]
        DEPLOY --> OPS[安全維運]
    end

    subgraph "GSD Pi 介入點"
        G1[AGENTS.md<br/>安全編碼規範] --> DEV
        G2[verification_commands<br/>SAST / Lint] --> TEST
        G3[Headless Mode<br/>CI/CD 整合] --> DEPLOY
        G4[KNOWLEDGE.md<br/>安全知識庫] --> OPS
    end
```

> **💡 實務建議**：在企業環境中，建議將 SonarQube 掃描加入 `verification_commands`，確保每個 Task 產出的程式碼都通過安全檢查。

### 3.7 MCP Server 架構

GSD Pi 支援 Model Context Protocol（MCP），可連接外部 MCP Server 擴展功能：

```mermaid
graph TB
    subgraph "GSD Pi MCP 架構"
        GSD[GSD Pi CLI] --> MCP_CLIENT[MCP Client<br/>內建擴充]
        MCP_CLIENT --> STDIO[stdio Transport<br/>本地程序]
        MCP_CLIENT --> HTTP[HTTP Transport<br/>遠端服務]
    end

    subgraph "外部 MCP Servers"
        STDIO --> LOCAL_SVR[本地工具<br/>自訂腳本]
        HTTP --> INTERNAL[內部 API<br/>企業服務]
        HTTP --> SELF_HOSTED[自架服務<br/>文件系統]
    end

    subgraph "GSD 作為 MCP Server"
        GSD_SVR[gsd-mcp-server] --> CLAUDE[Claude Desktop]
        GSD_SVR --> VSCODE[VS Code Copilot]
        GSD_SVR --> OTHER[其他 MCP Client]
    end
```

**設定檔位置**：

| 路徑 | 用途 |
|------|------|
| `.mcp.json` | 團隊共享的 MCP 設定（納入版本控制） |
| `.gsd/mcp.json` | 本地專用的 MCP 設定（不共享） |

**支援的傳輸協議**：

| 協議 | 參數 | 適用場景 |
|------|------|----------|
| `stdio` | `command` + `args`、`env`、`cwd` | 啟動本地 MCP Server 程序 |
| `http` | `url` | 連接已執行的遠端 MCP Server |

**設定範例**：

```json
{
  "mcpServers": {
    "internal-docs": {
      "type": "stdio",
      "command": "/usr/bin/python3",
      "args": ["/opt/mcp/doc-server.py"],
      "env": {
        "API_URL": "http://internal-docs.company.com"
      }
    },
    "code-review": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

**驗證步驟**：

```bash
# 在 GSD Session 中
mcp_servers                                    # 確認設定檔被載入
mcp_discover(server="internal-docs")           # 確認 Server 啟動並回應
mcp_call(server="internal-docs", tool="search", args={...})  # 測試工具調用
```

> **💡 實務建議**：企業環境中，建議使用 `.mcp.json` 存放團隊共享的內部文件 Server 設定，使用 `.gsd/mcp.json` 存放個人本地開發服務。GSD 會自動合併兩個設定檔。

### 3.8 Cloud MCP Gateway 架構

GSD Pi v1.0 新增 Cloud MCP Gateway Runtime，可管理雲端 MCP 伺服器的完整生命週期（啟動、監控、自動恢復、關閉）。這讓團隊可以集中管理 MCP 資源，避免每位開發者各自啟動本地程序：

```mermaid
graph TB
    subgraph "GSD Pi Cloud MCP Gateway"
        GATEWAY[Cloud Gateway Runtime] --> LIFECYCLE[Server Lifecycle Manager]
        LIFECYCLE --> HEALTH[Health Monitor]
        LIFECYCLE --> AUTO_RECOVER[Auto Recovery]
    end

    subgraph "託管的 MCP Servers"
        LIFECYCLE --> S1[Documentation Server]
        LIFECYCLE --> S2[Code Review Server]
        LIFECYCLE --> S3[Database Server]
    end

    subgraph "消費端"
        GSD1[GSD Pi Instance 1] --> GATEWAY
        GSD2[GSD Pi Instance 2] --> GATEWAY
        CI[CI/CD Pipeline] --> GATEWAY
    end
```

**設定方式**（透過 `.gsd/PREFERENCES.md`）：

```yaml
cloud_mcp:
  enabled: true
  gateway_url: "https://mcp-gateway.company.com"
  auto_recovery: true
  health_check_interval: 30   # 秒
```

> **💡 實務建議**：Cloud MCP Gateway 特別適合多人團隊共享 Database MCP Server、內部文件 Server 等需要持久連線的服務。

---

## 4. 安裝與環境建置（Installation）

### 4.1 系統需求

| 項目 | 需求 |
|------|------|
| **Node.js** | ≥ 22.0.0（推薦 24 LTS） |
| **Git** | 任意版本（未安裝時自動初始化） |
| **LLM Provider** | 20+ 支援的供應商任選其一 |
| **作業系統** | Windows / macOS / Linux |

選配：

| 項目 | 用途 |
|------|------|
| Brave Search API Key | 網路研究 |
| Tavily API Key | 網路研究（替代方案） |
| Google Gemini API Key | Gemini Search 研究 |
| Context7 API Key | 函式庫 / 框架文件查詢 |
| Jina API Key | 頁面內容擷取 |

### 4.2 安裝步驟

#### 快速安裝（推薦 — 互動式引導）

```bash
# 使用 npx 直接執行（免全域安裝，自動引導設定）
npx @opengsd/gsd-pi@latest
```

此方式會自動下載最新版本、執行首次設定精靈（選擇 LLM Provider、設定 API Key）。

#### 全域安裝

```bash
# 全域安裝
npm install -g @opengsd/gsd-pi@latest

# 驗證安裝
gsd --version    # 應顯示 v1.0.x
```

#### Windows

```powershell
# 1. 安裝 Node.js 24 LTS（若尚未安裝）
winget install OpenJS.NodeJS.LTS

# 2. 驗證 Node.js 版本
node --version   # 應為 v24.x.x

# 3. 全域安裝 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 4. 驗證安裝
gsd --version    # 應顯示 v1.0.x
```

#### macOS

```bash
# 1. 安裝 Node.js 24 LTS
brew install node@24
brew link --overwrite node@24

# 2. 全域安裝 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 3. 驗證安裝
gsd --version
```

> ⚠️ **macOS 注意**：若透過 Homebrew 安裝 Node.js，可能會安裝到開發版本而非 LTS。請確認使用 `node@24`。

#### Linux（Ubuntu / Debian）

```bash
# 1. 安裝 Node.js 24 LTS
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. 全域安裝 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 3. 驗證安裝
gsd --version
```

#### Linux（Fedora / RHEL / CentOS）

```bash
# 1. 安裝 Node.js 24 LTS
curl -fsSL https://rpm.nodesource.com/setup_24.x | sudo bash -
sudo dnf install -y nodejs git

# 2. 全域安裝 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 3. 驗證安裝
gsd --version
```

#### Linux（Arch Linux）

```bash
# 1. 安裝 Node.js 與 Git
sudo pacman -S nodejs npm git

# 2. 全域安裝 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 3. 驗證安裝
gsd --version
```

#### 使用 nvm（任何 Linux 發行版）

```bash
# 1. 安裝 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
source ~/.bashrc   # 或 ~/.zshrc

# 2. 安裝 Node.js 24 LTS
nvm install 24
nvm use 24

# 3. 全域安裝 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 4. 驗證安裝
gsd --version
```

> **💡 Linux 注意**：若 `npm install -g` 出現權限錯誤，**不要使用 `sudo npm`**。改用以下方式修正 npm 全域目錄：
>
> ```bash
> mkdir -p ~/.npm-global
> npm config set prefix '~/.npm-global'
> echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
> source ~/.bashrc
> npm install -g @opengsd/gsd-pi
> ```

### 4.3 從舊版遷移安裝

若您先前安裝的是舊版 `gsd-pi`（來自 `gsd-build/gsd-2`），請先移除再重新安裝：

```bash
# 移除舊版
npm uninstall -g gsd-pi

# 安裝新版（Scoped Package）
npm install -g @opengsd/gsd-pi@latest

# 驗證
gsd --version   # 應顯示 v1.0.x
```

> **ℹ️ 提示**：既有的 `.gsd/` 目錄、`PREFERENCES.md`、`AGENTS.md` 等專案設定檔完全向下相容，無需修改。

### 4.4 首次啟動與設定

```bash
# 進入專案目錄
cd /path/to/your-project

# 啟動 GSD（首次會進入設定精靈）
gsd
```

首次執行時，GSD 會啟動設定精靈：

1. **選擇 LLM Provider**：從 20+ 供應商中選擇（Anthropic、OpenAI、Google、OpenRouter、GitHub Copilot 等）
2. **認證方式**：
   - **OAuth**：Claude Max / GitHub Copilot 訂閱者可直接 OAuth 認證
   - **API Key**：貼上 API Key（**企業環境推薦此方式**）
3. **工具 API Key**（選填）：Brave Search、Context7、Jina、Slack、Discord
4. 每一步都可按 Enter 跳過

```bash
# 重新執行設定精靈
gsd config
```

> ⚠️ **安全警告**：OAuth Token 用於第三方工具可能違反供應商服務條款。**企業環境強烈建議使用 API Key** 而非 OAuth。

### 4.5 MCP Server 啟動

GSD Pi 可作為 MCP Server 運行，供 Claude Desktop 或 VS Code Copilot 等外部 AI 用戶端使用：

```bash
# 檢查 MCP 狀態
gsd
/gsd mcp
```

### 4.6 VS Code 擴充設定

GSD Pi 提供官方 VS Code 擴充套件（由 FluxLabs 發佈）：

1. 在 VS Code 擴充市場搜尋 `GSD` 或 `FluxLabs GSD`
2. 安裝後可使用：
   - **側邊欄儀表板**：即時查看 Milestone / Slice / Task 進度
   - **Chat Participant**：在 VS Code Chat 中直接與 GSD 互動
   - **RPC 整合**：與終端機 GSD 實例同步

### 4.7 與 Claude Code / Copilot 整合

#### Claude Code 整合

```bash
# 使用 Claude Code CLI 作為 Provider
gsd
/login
# 選擇 "Claude Code CLI" provider
```

GSD 內建 `Claude Code CLI` 擴充套件，可直接使用 Claude Code 作為外部 Provider。

#### GitHub Copilot 整合

```bash
# 使用 GitHub Copilot 作為 Provider
gsd
/login
# 選擇 "GitHub Copilot" provider
# 依照 OAuth 流程完成認證
```

### 4.8 Docker Sandbox 部署

GSD Pi 提供官方 Docker Sandbox 範本，可在隔離容器中執行 Auto Mode，無需在主機安裝 Node.js：

**前置需求**：Docker Desktop 4.58+

```bash
# 1. Clone GSD Pi 倉庫
git clone https://github.com/open-gsd/gsd-pi.git
cd gsd-pi/docker

# 2. 建立 Sandbox
docker sandbox create --template . --name gsd-sandbox

# 3. 進入 Sandbox
docker sandbox exec -it gsd-sandbox bash

# 4. 設定 API Key 並執行
export ANTHROPIC_API_KEY="sk-ant-..."
gsd auto "implement the feature described in issue #42"
```

**企業用途**：

- **CI/CD 隔離**：在 Docker 中執行 GSD Headless Mode，避免污染建置環境
- **安全沙箱**：限制 AI Agent 的檔案系統和網路存取範圍
- **可重現環境**：團隊成員使用相同的容器映像，確保一致性

> **💡 實務建議**：企業環境中，建議基於官方 Dockerfile 建立自訂映像，預裝團隊需要的工具（Maven、Gradle 等），並透過環境變數注入 API Key。

### 4.9 Web 介面啟動

GSD Pi 提供瀏覽器介面，適合視覺化專案管理和即時進度追蹤：

```bash
# 啟動 Web 介面
gsd --web
```

Web 介面功能：

| 功能 | 說明 |
|------|------|
| **專案儀表板** | 視覺化 Milestone / Slice / Task 進度 |
| **即時進度** | 自動更新執行狀態和成本 |
| **CLI 入門完成度** | 顯示 CLI Onboarding 完成記錄 |
| **設定管理** | 透過瀏覽器管理偏好設定 |

### 4.10 常見安裝問題與排除

| 問題 | 解決方案 |
|------|----------|
| `npm ERR! EACCES` | 使用 `sudo npm install -g @opengsd/gsd-pi` 或設定 npm prefix |
| Node.js 版本過低 | 升級至 22.0.0 以上，推薦 24 LTS |
| Windows 執行權限 | 以管理員身份執行 PowerShell |
| API Key 無效 | 執行 `gsd config` 重新設定 |
| Provider 連線失敗 | 檢查防火牆 / Proxy 設定 |
| `command not found: gsd` | 將 npm 全域 bin 加入 PATH（參見各平台注意事項） |
| `gsd` 執行 `git svn dcommit` | oh-my-zsh 衝突 — 在 `~/.zshrc` 加入 `unalias gsd 2>/dev/null`，或改用 `gsd-cli` |
| macOS Apple Silicon 找不到 `gsd` | `echo 'export PATH="$(npm prefix -g)/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| Windows 找不到 `gsd` | 重啟終端機（Windows 需要新終端才能載入 PATH） |
| WSL2 環境 | 安裝 WSL 後，在 WSL 內按 Linux 指引操作 |

```bash
# 執行健康檢查
gsd
/gsd doctor
```

`/gsd doctor` 會執行完整的運行時健康檢查，問題會顯示在 Widget、Visualizer 和報告中。

> **💡 實務建議**：企業環境中若有 Proxy，需設定 `HTTP_PROXY` / `HTTPS_PROXY` 環境變數。建議將 GSD 安裝指令加入團隊的開發環境初始化腳本。對於企業內網環境，可使用 `GSD_FETCH_ALLOWED_URLS` 環境變數允許內部 URL 存取（參見附錄 D）。

---

## 5. 專案初始化（Project Setup）

### 5.1 專案目錄結構

GSD Pi 使用 `.gsd/` 目錄管理所有工作狀態。以下為一個完整的企業專案目錄結構範例：

```
my-enterprise-app/
├── .gsd/                              # GSD 工作目錄（自動產生）
│   ├── PREFERENCES.md                 # 專案級偏好設定
│   ├── PROJECT.md                     # 專案描述（活文件）
│   ├── DECISIONS.md                   # 架構決策記錄（Append-only）
│   ├── KNOWLEDGE.md                   # 跨 Session 知識庫
│   ├── RUNTIME.md                     # 執行環境資訊（API、環境變數、服務）
│   ├── STATE.md                       # 狀態儀表板（自動產生）
│   ├── milestones/
│   │   └── M001-abc123/
│   │       ├── M001-ROADMAP.md        # Milestone 計畫（Slice 清單）
│   │       ├── M001-CONTEXT.md        # 使用者決策
│   │       ├── M001-RESEARCH.md       # 程式碼庫與生態系研究
│   │       ├── slices/
│   │       │   └── S01/
│   │       │       ├── S01-PLAN.md    # Slice 任務拆解
│   │       │       ├── S01-UAT.md     # 人工測試腳本
│   │       │       └── tasks/
│   │       │           ├── T01-PLAN.md    # 任務計畫
│   │       │           ├── T01-SUMMARY.md # 任務摘要
│   │       │           ├── T02-PLAN.md
│   │       │           └── T02-SUMMARY.md
│   │       └── reports/               # HTML 報告
│   ├── metrics.json                   # Token / 成本追蹤
│   ├── auto.lock                      # 崩潰偵測哨兵
│   └── gsd.db                         # SQLite 狀態資料庫
├── AGENTS.md                          # Agent 行為指引（專案級）
├── src/
│   ├── main/java/...                  # Spring Boot 後端
│   └── test/java/...                  # 測試
├── frontend/                          # Vue 前端
├── pom.xml                            # Maven 設定
└── .github/
    └── workflows/                     # CI/CD 設定
```

### 5.2 GSD 標準檔案說明

#### PROJECT.md — 專案活文件

```markdown
# 企業客戶管理平台

## 概述
一個基於 Spring Boot 3.5 + Vue 3 的客戶關係管理系統，
支援多租戶架構、角色權限管理與報表分析。

## 技術棧
- Backend: Java 21, Spring Boot 3.5.x, Clean Architecture
- Frontend: Vue 3.x, TypeScript, Tailwind CSS
- Database: PostgreSQL 16
- Cache: Redis 7
- MQ: Kafka 3.x

## 目前狀態
Milestone M001 — 基礎架構與使用者模組
```

#### REQUIREMENTS.md — 需求契約

`REQUIREMENTS.md` 是專案需求的正式契約文件，由討論流程自動產生或手動撰寫：

```markdown
# 需求規格

## 功能需求
### FR-001: 使用者註冊
- 支援 Email + 密碼註冊
- Email 必須唯一
- 密碼強度驗證（≥ 8 字元、含大小寫和數字）

### FR-002: 使用者登入
- JWT Token 認證
- Token 過期時間 30 分鐘
- 支援 Refresh Token

## 非功能需求
### NFR-001: 效能
- API 回應時間 < 200ms（P95）
- 支援 1,000 併發使用者

### NFR-002: 安全
- OWASP Top 10 防護
- 傳輸層 TLS 1.2+
```

#### DECISIONS.md — 架構決策記錄

```markdown
# 架構決策記錄

## D001: 採用 Clean Architecture
- **日期**: 2026-04-21
- **決策**: 使用 Clean Architecture 分層（Domain → Use Case → Interface → Infrastructure）
- **原因**: 確保業務邏輯與框架解耦，便於測試與維護
- **影響**: 需要額外的介面定義，但長期降低耦合度

## D002: 使用 PostgreSQL 作為主資料庫
- **日期**: 2026-04-21
- **決策**: 開發階段使用 PostgreSQL，正式環境可切換至 Oracle
- **原因**: PostgreSQL 開源免費，語法與 Oracle 相近
```

#### KNOWLEDGE.md — 跨 Session 知識庫

```markdown
# 專案知識庫

## 編碼規範
- Controller 命名：`XxxController`，放在 `adapter.in.web` 套件
- Service 命名：`XxxService`（介面）+ `XxxServiceImpl`（實作）
- Repository 命名：`XxxRepository`，放在 `adapter.out.persistence` 套件

## 已知問題
- Redis 連線池在高併發時需設定 maxTotal >= 50
- Kafka Consumer 需設定 max.poll.records=500 避免 Rebalance

## 最佳做法
- 所有 REST API 回傳統一 ApiResponse 包裝
- 例外處理統一使用 @ControllerAdvice
```

#### RUNTIME.md — 執行環境資訊

```markdown
# 執行環境

## API 端點
- 本地: http://localhost:8080
- SIT: https://sit-api.example.com
- UAT: https://uat-api.example.com

## 環境變數
- SPRING_PROFILES_ACTIVE: dev / sit / uat / prod
- DB_HOST: localhost (dev)
- REDIS_HOST: localhost (dev)

## 服務依賴
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- Kafka: localhost:9092
```

#### AGENTS.md — Agent 行為指引

```markdown
# Agent 指引

## 程式碼風格
- 使用 Java 21 特性（Records、Pattern Matching、Sealed Classes）
- 遵循 Clean Architecture：Domain 不依賴任何框架
- 每個 public method 必須有 JavaDoc
- 使用 Log4j2 記錄日誌

## 測試要求
- 每個 Service 必須有對應的 JUnit 5 測試
- 測試覆蓋率 > 80%
- 使用 Mockito 模擬外部依賴

## 安全規範
- 不得在程式碼中硬編碼密碼或 API Key
- SQL 查詢必須使用參數化查詢
- 所有 API 端點必須有權限檢查
```

### 5.3 初始化流程

```bash
# 1. 進入專案目錄
cd /path/to/my-enterprise-app

# 2. 確保 Git 已初始化
git init  # 如果尚未初始化

# 3. 建立 AGENTS.md（專案級 Agent 指引）
# 手動撰寫或參考上方範例

# 4. 啟動 GSD
gsd

# 5. GSD 自動偵測到沒有 .gsd/ 目錄，進入討論流程
# → 描述你的專案願景、限制條件與偏好
# → GSD 建立 PROJECT.md 和初始 Milestone

# 6. 設定專案偏好
/gsd prefs
```

**專案偏好設定範例**（`.gsd/PREFERENCES.md`）：

```yaml
---
version: 1
models:
  research: claude-sonnet-4-6
  planning:
    model: claude-opus-4-7
    fallbacks:
      - openrouter/deepseek/deepseek-r1
  execution: claude-sonnet-4-6
  completion: claude-sonnet-4-6
skill_discovery: suggest
auto_supervisor:
  soft_timeout_minutes: 20
  idle_timeout_minutes: 10
  hard_timeout_minutes: 30
budget_ceiling: 100.00
unique_milestone_ids: true
git:
  isolation: worktree
verification_commands:
  - mvn compile
  - mvn test
  - mvn checkstyle:check
verification_auto_fix: true
verification_max_retries: 2
auto_report: true
---
```

> **💡 實務建議**：團隊協作時務必啟用 `unique_milestone_ids: true`，避免多人同時開發時 Milestone ID 衝突。建議將 `.gsd/PREFERENCES.md` 納入 Git 版本控制。

---

## 6. Spec-Driven 開發流程

### 6.1 整體流程概覽

```mermaid
graph TD
    A[1. 撰寫規格 Spec] --> B[2. GSD 討論與研究]
    B --> C[3. 產生 Roadmap<br/>拆解 Slice]
    C --> D[4. 規劃 Slice<br/>拆解 Task]
    D --> E[5. 執行 Task<br/>AI 產生程式碼]
    E --> F[6. 驗證<br/>Lint / Test / Security]
    F --> G{驗證通過?}
    G -->|否| H[Auto-fix 重試]
    H --> F
    G -->|是| I[7. 提交 + 摘要]
    I --> J[8. 重新評估 Roadmap]
    J --> K{所有 Slice 完成?}
    K -->|否| D
    K -->|是| L[9. 驗證 Milestone]
    L --> M[10. 回饋到 KNOWLEDGE.md]
```

### 6.2 步驟 1：撰寫規格（Spec）

Spec 是整個流程的起點。可以透過多種方式提供：

**方式 A：互動式討論**

```bash
gsd
# GSD 偵測到新專案，自動進入討論流程
# 描述需求，GSD 會引導你細化 Spec
```

**方式 B：提供 Spec 檔案**

```bash
gsd headless new-milestone --context spec.md --auto
```

**Spec 撰寫範例**：

```markdown
# 使用者管理模組

## 功能需求
1. 使用者註冊（Email + 密碼）
2. 使用者登入（JWT Token）
3. 使用者資料 CRUD
4. 角色權限管理（RBAC）

## 非功能需求
- API 回應時間 < 200ms
- 支援 1000 併發使用者
- 密碼使用 BCrypt 加密
- JWT Token 過期時間 30 分鐘

## 技術限制
- 必須使用 Clean Architecture
- 必須有 80% 以上測試覆蓋率
- 必須通過 OWASP Top 10 安全檢查
```

### 6.3 步驟 2：拆解任務（Tasks）

GSD 自動將 Spec 拆解為層級結構：

```
Milestone M001: 使用者管理模組
├── Slice S01: 領域模型與基礎架構
│   ├── Task T01: 定義 User Domain Entity 與 Value Objects
│   ├── Task T02: 實作 UserRepository 介面與 JPA 實作
│   └── Task T03: 設定 PostgreSQL 連線與 Flyway Migration
├── Slice S02: 認證與授權
│   ├── Task T01: 實作 RegisterUseCase
│   ├── Task T02: 實作 LoginUseCase（JWT 產生）
│   └── Task T03: 實作 JWT Filter 與 Security Config
├── Slice S03: REST API 端點
│   ├── Task T01: UserController CRUD 端點
│   ├── Task T02: AuthController（Register / Login）
│   └── Task T03: Swagger 文件配置
└── Slice S04: 測試與文件
    ├── Task T01: 單元測試（Service 層）
    ├── Task T02: 整合測試（Controller + Repository）
    └── Task T03: API 文件與 UAT 腳本
```

每個 Task Plan 包含 **Must-haves**：

```markdown
# T01-PLAN: 定義 User Domain Entity

## Must-haves

### Truths（可觀察行為）
- [ ] User Entity 包含 id, email, password, name, role 欄位
- [ ] Email 格式驗證通過 Value Object 實作
- [ ] Password 使用 BCrypt 加密

### Artifacts（必須存在的檔案）
- [ ] src/main/java/com/example/domain/model/User.java
- [ ] src/main/java/com/example/domain/model/Email.java
- [ ] src/main/java/com/example/domain/model/Role.java

### Key Links（匯入與連接）
- [ ] User.java 使用 Email Value Object
- [ ] User.java 使用 Role Enum
```

### 6.4 步驟 3：指派 AI Agent

GSD Pi 內建五個專業 Subagent：

| Agent | 用途 |
|-------|------|
| **Scout** | 快速程式碼偵察，回傳壓縮的 Context 供後續處理 |
| **Researcher** | 網路研究，搜尋並綜合最新資訊 |
| **Worker** | 通用執行，在隔離的 Context Window 中工作 |
| **JavaScript Pro** | JavaScript 專業執行與除錯 |
| **TypeScript Pro** | TypeScript 專業執行與除錯 |

Agent 分配策略：

- **Research Phase**：使用 Researcher + Scout
- **Planning Phase**：使用主模型（建議 Opus）
- **Execution Phase**：使用主模型（建議 Sonnet）
- **Completion Phase**：使用快速模型

### 6.5 步驟 4：產生程式碼

GSD Auto Mode 自動執行：

```bash
# Terminal 1 — 自動執行
gsd
/gsd auto

# Terminal 2 — 同步導引（選用）
gsd
/gsd discuss    # 討論架構決策
/gsd status     # 查看進度
/gsd steer      # 修改計畫
```

每個 Task 的執行流程：

1. **建立全新 Session**：200K Token Context Window
2. **注入 Context**：Task Plan + Slice Plan + Prior Summaries + DECISIONS.md + KNOWLEDGE.md
3. **LLM 執行**：產生程式碼
4. **驗證**：執行 `verification_commands`
5. **Auto-fix**：驗證失敗時自動修復（最多重試 2 次）
6. **提交**：有意義的 Commit Message（從 Task Summary 產生）

### 6.6 步驟 5：測試與驗證

GSD 的驗證階梯（Verification Ladder）：

```
靜態檢查（Lint / Compile）
       ↓
指令執行（Unit Test / Integration Test）
       ↓
行為測試（E2E / UAT）
       ↓
人工審查（僅當 Agent 無法自行驗證時）
```

```yaml
# .gsd/PREFERENCES.md
verification_commands:
  - mvn compile                    # 編譯檢查
  - mvn test                      # 單元測試
  - mvn checkstyle:check          # 程式碼風格
  - mvn spotbugs:check            # 靜態分析
verification_auto_fix: true        # 失敗時自動修復
verification_max_retries: 2        # 最多重試 2 次
```

### 6.7 步驟 6：回饋到 KNOWLEDGE.md

每個 Task 完成後，GSD 自動提取教訓並寫入 `KNOWLEDGE.md`：

```markdown
## 新增知識 — 2026-04-21

### Spring Boot 3.5 + JWT 整合
- Spring Security 6.x 不再使用 `WebSecurityConfigurerAdapter`
- 改用 `SecurityFilterChain` Bean 配置
- JWT Filter 必須在 `UsernamePasswordAuthenticationFilter` 之前註冊

### PostgreSQL UUID 主鍵
- 使用 `@GeneratedValue(strategy = GenerationType.UUID)` 而非自定義 Generator
- JPA 3.x 原生支援 UUID 策略
```

> **💡 實務建議**：定期審查 `KNOWLEDGE.md` 的內容，移除過時的知識，補充團隊共識。這是提升 AI 輸出品質最有效的方式。

---

## 7. AI Agent 協作模式

### 7.1 多 Agent 協作架構

```mermaid
graph TB
    subgraph "GSD Pi Agent 協作"
        DISPATCH[Dispatch Engine] --> SCOUT[Scout Agent<br/>程式碼偵察]
        DISPATCH --> RESEARCHER[Researcher Agent<br/>網路研究]
        DISPATCH --> WORKER[Worker Agent<br/>通用執行]
        DISPATCH --> JS_PRO[JavaScript Pro<br/>JS 專業]
        DISPATCH --> TS_PRO[TypeScript Pro<br/>TS 專業]
    end

    subgraph "典型 Agent 協作流程"
        R1[1. Researcher<br/>研究最新技術] --> R2[2. Scout<br/>偵察現有程式碼]
        R2 --> R3[3. Planner<br/>主模型規劃任務]
        R3 --> R4[4. Worker<br/>執行開發任務]
        R4 --> R5[5. 驗證<br/>自動測試]
        R5 --> R6[6. Reviewer<br/>程式碼審查]
    end
```

### 7.2 Claude Code 使用方式

GSD Pi 內建 `Claude Code CLI` 擴充套件：

```bash
# 登入 Claude Code 作為 Provider
gsd
/login
# 選擇 Claude Code CLI

# 設定模型（建議）
/gsd prefs
# models:
#   planning: claude-opus-4-7
#   execution: claude-sonnet-4-6
```

**Claude Code 在 GSD 中的角色**：

- 作為 **LLM Provider**，提供推理能力
- GSD 控制 Context Window 管理、Session 生命週期
- Claude Code 的原生能力（File Editing、Shell Execution）由 GSD 編排

### 7.3 Copilot 使用方式

```bash
# 登入 GitHub Copilot 作為 Provider
gsd
/login
# 選擇 GitHub Copilot
# 完成 OAuth 認證流程
```

**VS Code 整合**：

- 安裝 GSD VS Code Extension
- Chat 中輸入 `@gsd` 與 GSD 互動
- 側邊欄顯示即時進度

### 7.4 Agent 任務切分策略

**原則**：一個 Task = 一個 Context Window

```
❌ 不好的拆分：
  Task: 實作整個使用者模組（太大）

✅ 好的拆分：
  Task T01: 定義 User Domain Entity 與 Value Objects
  Task T02: 實作 UserRepository 介面
  Task T03: 實作 JPA UserRepositoryImpl
  Task T04: 實作 RegisterUseCase
  Task T05: 實作 UserController
```

**拆分依據**：

1. **功能垂直切分**：每個 Slice 是一個可展示的完整功能
2. **技術水平切分**：Domain → Infrastructure → Application → Interface
3. **複雜度控制**：每個 Task 的程式碼變更不超過 500 行
4. **依賴順序**：後置 Task 可依賴前置 Task 的成果

### 7.5 雙終端機工作流

這是 GSD Pi 推薦的日常工作模式：

**Terminal 1 — 自動執行（放著跑）**：

```bash
gsd
/gsd auto
# 自動研究 → 規劃 → 執行 → 驗證 → 提交 → 下一輪
```

**Terminal 2 — 導引與監控**：

```bash
gsd
/gsd discuss    # 討論架構決策（決策自動被 Auto Mode 拾取）
/gsd status     # 查看進度儀表板
/gsd steer      # 修改計畫文件（Hard-steer）
/gsd queue      # 排隊下一個 Milestone
```

兩個終端讀寫相同的 `.gsd/` 檔案。Terminal 2 的決策在下一個 Phase 邊界自動被拾取。

**Planner Handoff（v1.2.0）**：

GSD Pi v1.2.0 引入 Planner Handoff 機制，將規劃與執行明確分離。規劃階段由高能力模型（如 `claude-fable-5` 或 `claude-opus-4-8`）完成後，系統自動生成詳細的移交文件，再由執行模型（如 `claude-sonnet-4-6`）接手實作：

```text
Planner Agent（高能力模型）
  → 分析需求、設計架構、拆解任務
  → 產生 Handoff Document（含技術決策、檔案清單、依賴關係）
      ↓
Worker Agent（執行模型）
  → 讀取 Handoff Document
  → 逐 Task 實作，無需重新理解架構
```

此機制的優勢：

- **品質提升**：規劃用最強模型，不受預算影響執行品質
- **成本降低**：執行用標準模型，規劃成本均攤至整個 Milestone
- **上下文清晰**：Worker Agent 起始 Context 乾淨，不含規劃過程的冗餘資訊

### 7.6 Quick Mode — 快速任務

對於小型修改，不需要完整的 Milestone 流程：

```bash
gsd
/gsd quick
# 直接描述任務，GSD 以完整保證執行，但跳過規劃開銷
```

### 7.7 Session 可觀察性命令

GSD Pi v1.1.0 新增兩個可觀察性（Observability）命令，讓開發者在 Auto Mode 執行期間即時掌握資源用量與 Context 狀態：

#### `/gsd usage` — Session 用量查詢

```bash
gsd
/gsd usage
```

輸出範例：

```text
Session Usage:
  Input tokens:    128,432
  Output tokens:    24,891
  Cache read:       89,034
  Cache write:       8,200
  Total cost:        $0.87 USD

Per-phase breakdown:
  Planning:    45,200 tokens  ($0.32)
  Execution:   92,400 tokens  ($0.48)
  Completion:  15,723 tokens  ($0.07)
```

#### `/gsd context` — Context 狀態查詢

```bash
gsd
/gsd context
```

輸出範例：

```text
Context State:
  Window size:     200,000 tokens
  Used:            142,310 tokens (71.2%)
  Available:        57,690 tokens
  Pressure level:  moderate
  Next threshold:  80% (wrap-up signal)

Loaded artifacts:
  - ROADMAP.md        (12,400 tokens)
  - Slice S02 Plan    ( 3,200 tokens)
  - KNOWLEDGE.md      ( 8,900 tokens)
  - Prior summaries   ( 5,600 tokens)
```

> **💡 實務建議**：在長時間 Auto Mode 執行中，定期執行 `/gsd usage` 監控成本，搭配 `budget_ceiling` 設定避免超支。Context 壓力超過 70% 時可執行 `/gsd context` 評估是否需要手動壓縮知識庫。

### 7.8 Telegram 遠端控制

GSD Pi 支援透過 Telegram 遠端控制 Auto Mode，適合在 Headless / CI 模式下遠端監控和操作：

**設定方式**：

```yaml
# .gsd/PREFERENCES.md
remote_questions:
  channel: telegram
  channel_id: "your-chat-id"
  timeout_minutes: 15
  poll_interval_seconds: 10

notifications:
  enabled: true
  on_complete: true
  on_error: true
  on_budget: true
  on_milestone: true
  on_attention: true
```

**Telegram 命令**：

| 命令 | 說明 |
|------|------|
| `/pause` | 暫停 Auto Mode（當前單元完成後暫停） |
| `/resume` | 清除暫停指令，繼續 Auto Mode |
| `/status` | 顯示當前 Milestone、活動單元和 Session 成本 |
| `/progress` | Roadmap 總覽（已完成 / 未完成 Milestone） |
| `/budget` | Token 使用量和當前 Session 成本 |
| `/log [n]` | 最近 n 筆活動日誌（預設 5 筆） |

GSD 在 Auto Mode 活動期間每 ~5 秒輪詢 Telegram 命令。

**其他遠端頻道**：

除了 Telegram，也支援 Slack 和 Discord 作為遠端問答與通知頻道：

```yaml
# Slack 設定
remote_questions:
  channel: slack
  channel_id: "C1234567890"

# Discord 設定
remote_questions:
  channel: discord
  channel_id: "123456789012345678"
```

啟用 `notifications.enabled: true` 時，里程碑完成、阻擋、預算警報等通知也會自動發送到遠端頻道。

### 7.9 Web 介面管理

GSD Pi 提供瀏覽器介面，可視覺化管理專案：

```bash
# 啟動 Web 介面
gsd --web
```

Web 介面適合以下場景：

- **專案經理**：無需使用 CLI 即可查看進度和成本
- **團隊協作**：共享 URL 讓團隊成員即時查看狀態
- **報告產出**：直接從瀏覽器匯出 HTML 報告

### 7.10 思緒捕捉（Capture）與工作流視覺化

#### `/gsd capture` — 即時思緒捕捉

在 Auto Mode 執行期間，隨時記錄想法，系統會在任務間自動分類處理：

```bash
gsd
/gsd capture "add rate limiting to API endpoints"
```

Capture 特性：

- **Fire-and-forget**：不中斷當前執行
- **自動分類**：Capture 在任務間自動被分類處理（Triage）
- **Dashboard 整合**：待處理的 Capture 數量顯示在儀表板

#### `/gsd visualize` — 工作流視覺化

開啟互動式工作流視覺化器：

```bash
gsd
/gsd visualize
```

視覺化器包含：

| 標籤頁 | 內容 |
|--------|------|
| **Progress** | Milestone / Slice / Task 進度樹 |
| **Dependencies** | Slice 依賴關係圖 |
| **Metrics** | 成本、Token、執行時間統計 |
| **Timeline** | 執行時間線 |
| **Discussion Status** | 討論狀態與決策追蹤 |

```yaml
# 自動在 Milestone 完成後顯示視覺化器
# .gsd/PREFERENCES.md
auto_visualize: true
```

> **💡 實務建議**：建議團隊建立 `AGENTS.md` 範本，統一定義程式碼風格、架構規範與安全要求。這確保不同 Agent 和不同 Session 產出一致的程式碼。搭配 Telegram 遠端控制，可在離開工位後持續監控 AI 開發進度。

### 7.11 Visual Briefs — 視覺化簡報產出

GSD Pi v1.0 新增 `/gsd brief` 命令，自動分析專案結構並產生 Mermaid 視覺化簡報：

```bash
gsd
/gsd brief
# 自動掃描專案結構，產出包含以下內容的視覺化摘要：
# - 模組依賴圖
# - API 端點清單
# - 資料模型關係圖
# - 技術棧概覽
```

**產出範例**（自動產生的 Mermaid 圖表）：

```mermaid
graph TD
    subgraph "後端模組"
        AUTH[Auth Module] --> USER[User Module]
        ORDER[Order Module] --> USER
        ORDER --> PRODUCT[Product Module]
    end
    subgraph "資料層"
        USER --> DB[(PostgreSQL)]
        ORDER --> DB
        PRODUCT --> DB
        AUTH --> CACHE[(Redis)]
    end
```

**適用場景**：
- **新人入職**：快速理解專案全貌
- **架構審查**：自動產出最新架構圖供會議使用
- **文件同步**：讓文件與程式碼保持一致

### 7.12 自訂工作流插件（Custom Workflows）

GSD Pi 提供統一的工作流插件系統，可安裝、管理與執行自訂工作流範本：

```bash
# 查看可用的工作流範本
/gsd workflow list

# 啟動內建工作流
/gsd start bugfix        # Bug 修復流程
/gsd start release       # 發佈流程
/gsd start refactor      # 重構流程

# 安裝自訂工作流
/gsd workflow install my-custom-workflow.md

# 移除工作流
/gsd workflow uninstall my-custom-workflow
```

**自訂工作流範本格式**：

```markdown
---
name: security-audit
description: 執行安全稽核工作流
triggers:
  - /gsd start security-audit
phases:
  - name: scan
    prompt: "掃描所有依賴的已知弱點（CVE）"
  - name: review
    prompt: "審查 OWASP Top 10 合規性"
  - name: report
    prompt: "產出安全稽核報告"
---
```

---

## 8. 知識圖譜與學習系統

### 8.1 KNOWLEDGE.md 設計方式

`KNOWLEDGE.md` 是 GSD Pi 的長期記憶系統，跨 Session 保持學習成果：

```markdown
# 專案知識庫

## 架構知識
### Clean Architecture 層級映射
- `domain/model/` → Domain Entities & Value Objects
- `domain/port/` → Input/Output Ports（Use Case 介面）
- `application/service/` → Use Case 實作
- `adapter/in/web/` → REST Controllers
- `adapter/out/persistence/` → JPA Repositories

### Spring Boot 3.5 重要變更
- Security Config 使用 Lambda DSL
- `@SpringBootTest` 預設使用 `MOCK` 環境
- Hibernate 6.x 的 `@Type` 改用 `@JdbcTypeCode`

## 技術陷阱
### PostgreSQL
- JSONB 欄位查詢需使用 `@Query(nativeQuery = true)`
- Sequence 命名需與 Entity 的 `@SequenceGenerator` 一致

### Redis
- Spring Data Redis 的 `@Cacheable` 預設序列化為 JDK 格式
- 建議改用 `Jackson2JsonRedisSerializer`

## 團隊共識
- API 統一使用 `/api/v1/` 前綴
- 所有日期時間使用 ISO 8601 格式
- 錯誤碼格式：`MODULE-XXXX`（例：`USER-0001`）
```

### 8.2 記憶架構（v2.77 ADR-013）

GSD Pi 的記憶系統架構（源自 ADR-013）：

```mermaid
graph TB
    subgraph "記憶來源"
        T1[Task Summary] --> MEM[Memories 表格<br/>唯一事實來源]
        T2[Extract Learnings] --> MEM
        T3[Decisions Register] --> MEM
        T4[手動輸入] --> MEM
    end

    subgraph "記憶存取"
        MEM --> A1[Agent Dispatch]
        MEM --> A2[MCP Tools]
        MEM --> A3[UI 表面]
        MEM --> A4[知識檔案]
    end

    subgraph "結構化欄位"
        MEM --> SF[structured_fields<br/>型別化 Metadata]
        SF --> F1[category: architecture]
        SF --> F2[confidence: high]
        SF --> F3[source: task-execution]
    end
```

關鍵改進：

- **Memories 表格為唯一事實來源**：所有記憶讀寫統一路徑，不再有同步漂移
- **結構化欄位**：`structured_fields` 支援型別化 Metadata，提升檢索精度
- **雙寫遷移完成**：舊格式無縫轉換，保留歷史資料

### 8.3 Knowledge Graph 建立

GSD Pi 將 `KNOWLEDGE.md` 解析為知識圖譜：

```
知識節點類型：
├── 架構決策（Architecture Decision）
├── 技術知識（Technical Knowledge）
├── 已知問題（Known Issue）
├── 最佳做法（Best Practice）
├── 團隊共識（Team Convention）
└── 錯誤教訓（Lesson Learned）
```

**建立知識圖譜的最佳做法**：

1. **分類清楚**：使用二級標題區分知識類別
2. **具體可操作**：每條知識必須包含「什麼」和「為什麼」
3. **定期修剪**：移除過時知識，避免誤導 AI
4. **版本控制**：`KNOWLEDGE.md` 納入 Git，追蹤知識演進

### 8.4 如何提升 AI 理解能力

**策略 1：豐富 AGENTS.md**

```markdown
# AGENTS.md

## 領域術語
- **租戶（Tenant）**: 使用系統的企業客戶
- **經辦人（Handler）**: 處理案件的行員
- **核決（Approval）**: 主管審核通過

## 業務規則
- 金額 > 100萬需雙簽核
- 跨行轉帳 T+1 到帳
```

**策略 2：善用 DECISIONS.md**

```bash
gsd
/gsd discuss
# 討論架構問題，GSD 自動記錄到 DECISIONS.md
# Auto Mode 會在後續 Task 中參考這些決策
```

**策略 3：Slice Discussion（v2.77）**

```yaml
# .gsd/PREFERENCES.md
phases:
  require_slice_discussion: true  # 每個 Slice 前暫停，等待人工討論
```

啟用後，Auto Mode 在每個 Slice 開始前暫停，讓開發者審查計畫並提供額外指引。

**策略 4：Skill Discovery**

```yaml
# .gsd/PREFERENCES.md
skill_discovery: auto    # auto / suggest / off
always_use_skills:       # 始終載入的技能
  - java-spring-boot
  - clean-architecture
```

GSD 自動偵測並安裝相關技能（Skills），為特定領域提供專業指引。

**策略 5：Custom Instructions**

在偏好設定中加入持久性指令，附加到每個 Session：

```yaml
# .gsd/PREFERENCES.md
custom_instructions:
  - "Always use TypeScript strict mode"
  - "Prefer functional patterns over classes"
  - "所有 API 回傳必須包含 correlation-id"
```

對於專案特定的知識（模式、陷阱、教訓），建議使用 `.gsd/KNOWLEDGE.md`，透過 `/gsd knowledge rule|pattern|lesson <描述>` 新增條目。

**策略 6：Knowledge CLI 命令**

```bash
# 快速新增知識條目
/gsd knowledge rule "所有 REST API 必須使用統一回應包裝"
/gsd knowledge pattern "Redis 連線池使用 Lettuce 而非 Jedis"
/gsd knowledge lesson "Flyway Migration 命名必須使用 V{timestamp} 格式"
```

> **💡 實務建議**：知識庫的品質直接決定 AI 產出的品質。建議每週安排 30 分鐘的「知識審查」時間，團隊共同維護 `KNOWLEDGE.md`。

---

## 9. 技能管理（Skill Management）

### 9.1 技能系統概述

GSD Pi 的技能系統（Skills）提供領域專業指引，讓 AI Agent 在特定任務中獲得更精準的知識：

```mermaid
graph LR
    A[任務開始] --> B{Skill Discovery}
    B -->|auto| C[自動偵測 + 安裝]
    B -->|suggest| D[建議 + 等待確認]
    B -->|off| E[不啟用]
    C --> F[載入相關 Skills]
    D --> F
    F --> G[注入 Task Dispatch]
    G --> H[AI 執行<br/>含專業知識]
```

### 9.2 技能發現模式

```yaml
# .gsd/PREFERENCES.md
skill_discovery: auto       # auto / suggest / off

# 始終載入的技能
always_use_skills:
  - java-spring-boot
  - clean-architecture
  - security-best-practices

# 情境式技能規則
skill_rules:
  - when: "*.java"
    use: java-spring-boot
  - when: "*.vue"
    use: vue-typescript
  - when: "*.sql"
    use: database-design
```

| 模式 | 說明 |
|------|------|
| `auto` | 自動偵測、安裝並應用相關技能 |
| `suggest` | 偵測後建議，等待開發者確認 |
| `off` | 不啟用技能發現 |

### 9.3 技能評估方式

GSD Pi 追蹤每個技能的使用情況：

- **使用頻率**：技能被載入和應用的次數
- **任務成功率**：使用該技能的任務成功完成比例
- **技能新鮮度**：`skill_staleness_days`（預設 60 天），超過未使用的技能會被降低優先級

```yaml
# 設定技能過期天數
skill_staleness_days: 60    # 60 天未使用的技能降低優先級
                            # 設為 0 停用此功能
```

### 9.4 Agent 健康度監控

使用 `/gsd doctor` 執行全面健康檢查：

```bash
gsd
/gsd doctor
```

健康檢查涵蓋：

| 檢查項目 | 說明 |
|----------|------|
| **Provider 連線** | API Key 有效性、Provider 可用性 |
| **Node.js 版本** | 確認 ≥ 22.0.0 |
| **Git 狀態** | Repository 初始化、分支狀態 |
| **Schema 版本** | 資料庫遷移一致性 |
| **技能狀態** | 已安裝技能清單、過期技能 |
| **擴充套件** | 24 個內建擴充的載入狀態 |

#### Real-Time Health Visibility（v2.40）

Doctor 健康問題現在即時顯示在三個位置：

| 顯示位置 | 說明 |
|----------|------|
| **Dashboard Widget** | 健康指標 + 問題數量 + 嚴重等級 |
| **Workflow Visualizer** | 狀態面板中顯示問題 |
| **HTML Reports** | 報告生成時包含所有問題 |

問題分類等級：

| 等級 | 說明 | Auto Mode 影響 |
|------|------|----------------|
| `error` | 嚴重問題 | 阻擋 Auto Mode |
| `warning` | 非阻擋性問題 | 記錄警告，繼續執行 |
| `info` | 建議性資訊 | 僅供參考 |

Auto Mode 在 Dispatch 時檢查健康狀態，遇到 `error` 等級問題會自動暫停。

```bash
# 查看日誌
/gsd logs
# 瀏覽 Activity、Debug、Metrics 日誌
```

#### Tool Surface Readiness Gate（v1.3.0）

GSD Pi v1.3.0 在 SDK 初始化階段新增 **Tool Surface Readiness Gate**，在任何任務分派之前驗證所有必要的工具介面（MCP Server、Shell、瀏覽器等）均已就緒並可回應：

```text
GSD Pi 啟動
  → SDK 初始化
  → Tool Surface Readiness Check
      ✓ Shell 工具：就緒
      ✓ MCP Servers：全部就緒（3/3）
      ✓ gsd-browser：就緒
      ⚠ Voice Tool：未連線（非必要，忽略）
  → 所有必要工具就緒，開始分派任務
```

**優勢**：

- **提前失敗**：初始化時即偵測工具問題，避免任務執行中途因工具不可用而中斷
- **精準診斷**：明確顯示哪個工具未就緒，縮短排錯時間
- **非必要工具容錯**：選配工具（如語音輸入）未就緒時只記錄警告，不阻擋執行

### 9.5 擴充套件管理（Extensions）

GSD Pi v1.0 新增統一的擴充套件管理系統，可安裝、更新和移除第三方擴充：

```bash
# 查看已安裝擴充
/gsd extensions list

# 安裝擴充
/gsd extensions install <extension-name>

# 更新擴充
/gsd extensions update <extension-name>

# 移除擴充
/gsd extensions uninstall <extension-name>
```

**內建擴充套件數量**：GSD Pi 隨附 24 個以上的內建擴充，涵蓋瀏覽器工具、搜尋引擎、GitHub 整合、語音輸入等（詳見附錄 A）。

**社群擴充範例**：

| 擴充名稱 | 功能 |
|----------|------|
| `pi-dashscope` | 阿里雲通義千問（DashScope）Provider |
| `gsd-browser` | 內建 Playwright 瀏覽器 MCP Server |

> **💡 實務建議**：建議在專案初始化時，透過 `always_use_skills` 鎖定核心技能（如 `java-spring-boot`、`clean-architecture`），確保 AI 始終遵循團隊的技術棧規範。搭配 `/gsd extensions` 管理擴充，可快速擴展 GSD Pi 的功能邊界。

---

## 10. 實戰範例

### 10.1 目標

使用 GSD Pi 完整流程建立一個「Spring Boot REST API + Vue UI」的客戶管理系統。

### 10.2 Step 1：撰寫 Spec

建立 `spec.md` 檔案：

```markdown
# 客戶管理系統 — Spec

## 系統目標
建立一個客戶關係管理（CRM）系統，支援客戶 CRUD、搜尋與分頁。

## 後端需求
- Spring Boot 3.5.x + Java 21
- Clean Architecture（Domain → Application → Infrastructure → Interface）
- PostgreSQL 資料庫
- RESTful API + Swagger UI
- JWT 認證
- 分頁與排序支援

## 前端需求
- Vue 3 + TypeScript + Tailwind CSS
- 客戶列表（分頁、搜尋）
- 客戶詳情頁
- 新增/編輯客戶表單
- 登入頁面

## API 端點
- POST /api/v1/auth/login
- POST /api/v1/auth/register
- GET /api/v1/customers?page=0&size=20&search=keyword
- GET /api/v1/customers/{id}
- POST /api/v1/customers
- PUT /api/v1/customers/{id}
- DELETE /api/v1/customers/{id}

## 資料模型
### Customer
- id: UUID
- name: String (required, max 100)
- email: String (required, unique)
- phone: String (optional)
- address: String (optional)
- status: ACTIVE / INACTIVE
- createdAt: Timestamp
- updatedAt: Timestamp

## 安全要求
- 密碼 BCrypt 加密
- SQL Injection 防護（參數化查詢）
- XSS 防護（輸入驗證）
- JWT Token 30 分鐘過期
```

### 10.3 Step 2：初始化 GSD 專案

```bash
# 建立專案目錄
mkdir crm-system && cd crm-system
git init

# 建立 AGENTS.md
cat > AGENTS.md << 'EOF'
# Agent 指引

## 後端規範
- Java 21，使用 Records、Sealed Classes
- Clean Architecture 四層：domain / application / adapter.in / adapter.out
- 每個 public method 必須有 JavaDoc
- 使用 Log4j2
- 測試覆蓋率 > 80%

## 前端規範
- Vue 3 Composition API + TypeScript
- 元件命名使用 PascalCase
- 使用 Pinia 狀態管理
- 使用 Axios HTTP Client

## 安全規範
- 不得硬編碼敏感資訊
- 所有 API 必須有權限檢查
- 輸入驗證使用 Bean Validation
EOF

# 啟動 GSD
gsd

# 登入 Provider
/login
# 選擇 Anthropic，貼上 API Key

# 開始新 Milestone（提供 Spec）
```

### 10.4 Step 3：GSD 自動規劃

GSD 讀取 Spec 後，自動產生 Roadmap：

```
Milestone M001-crm001: 客戶管理系統 MVP

├── Slice S01: 專案骨架與領域模型（風險：低）
│   ├── T01: Spring Boot 專案初始化 + Maven 依賴
│   ├── T02: Clean Architecture 套件結構
│   ├── T03: Customer Domain Entity + Value Objects
│   └── T04: 資料庫 Migration（Flyway）
│
├── Slice S02: 後端 CRUD API（風險：中）
│   ├── T01: CustomerRepository 介面 + JPA 實作
│   ├── T02: CRUD Use Cases（Create / Read / Update / Delete）
│   ├── T03: CustomerController + Swagger
│   └── T04: 分頁與搜尋實作
│
├── Slice S03: 認證與授權（風險：高）
│   ├── T01: User Entity + Repository
│   ├── T02: JWT 工具類
│   ├── T03: Spring Security Config
│   └── T04: AuthController（Login / Register）
│
├── Slice S04: Vue 前端（風險：中）
│   ├── T01: Vue 專案初始化 + Router + Pinia
│   ├── T02: 登入頁 + Auth Store
│   ├── T03: 客戶列表頁（分頁 + 搜尋）
│   └── T04: 客戶詳情與表單頁
│
└── Slice S05: 測試與整合（風險：低）
    ├── T01: 後端單元測試
    ├── T02: 後端整合測試
    └── T03: API 文件完善 + UAT 腳本
```

### 10.5 Step 4：執行 Auto Mode

```bash
# Terminal 1 — 開始自動執行
/gsd auto

# GSD 開始自動工作：
# → Research: 偵察專案結構，研究 Spring Boot 3.5 最新 API
# → Plan S01: 拆解第一個 Slice 的 Tasks
# → Execute T01: 初始化 Spring Boot 專案
# → Verify: mvn compile ✓
# → Execute T02: 建立套件結構
# → Verify: mvn compile ✓
# → ...（持續推進）
```

```bash
# Terminal 2 — 監控進度
/gsd status

# 輸出範例：
# ┌─────────────────────────────────────────┐
# │ M001-crm001: 客戶管理系統 MVP          │
# │ Progress: ████████░░ 40%               │
# │ Current: S02/T03 - CustomerController   │
# │ Cost: $2.34 / Budget: $100.00          │
# │ Elapsed: 1h 23m                         │
# └─────────────────────────────────────────┘
```

### 10.6 Step 5：查看產出

GSD 自動產生的程式碼範例：

**Domain Layer — Customer.java**：

```java
package com.example.crm.domain.model;

import java.time.Instant;
import java.util.UUID;

/**
 * 客戶領域實體。
 * 
 * <p>代表系統中的一個客戶，包含基本資訊與狀態管理。
 * 遵循 DDD 原則，業務邏輯封裝在實體內部。</p>
 */
public class Customer {

    private final UUID id;
    private String name;
    private Email email;
    private String phone;
    private String address;
    private CustomerStatus status;
    private final Instant createdAt;
    private Instant updatedAt;

    /**
     * 建立新客戶。
     *
     * @param name  客戶名稱（必填）
     * @param email 客戶信箱（必填，唯一）
     * @return 新建的客戶實體
     */
    public static Customer create(String name, Email email) {
        return new Customer(
            UUID.randomUUID(),
            name,
            email,
            null,
            null,
            CustomerStatus.ACTIVE,
            Instant.now(),
            Instant.now()
        );
    }

    /**
     * 停用此客戶。
     */
    public void deactivate() {
        this.status = CustomerStatus.INACTIVE;
        this.updatedAt = Instant.now();
    }

    // Constructor, getters...
}
```

**Application Layer — CreateCustomerUseCase.java**：

```java
package com.example.crm.application.service;

import com.example.crm.domain.model.Customer;
import com.example.crm.domain.model.Email;
import com.example.crm.domain.port.out.CustomerRepository;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * 建立客戶使用案例。
 */
public class CreateCustomerUseCase {

    private static final Logger log = LogManager.getLogger(CreateCustomerUseCase.class);
    private final CustomerRepository customerRepository;

    public CreateCustomerUseCase(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    /**
     * 執行建立客戶。
     *
     * @param command 建立客戶命令
     * @return 新建的客戶
     * @throws EmailAlreadyExistsException 當信箱已存在時
     */
    public Customer execute(CreateCustomerCommand command) {
        log.info("建立客戶: {}", command.name());

        Email email = Email.of(command.email());

        if (customerRepository.existsByEmail(email)) {
            throw new EmailAlreadyExistsException(email.value());
        }

        Customer customer = Customer.create(command.name(), email);
        return customerRepository.save(customer);
    }

    public record CreateCustomerCommand(String name, String email) {}
}
```

### 10.7 Step 6：查看 Learning

Task 完成後，`KNOWLEDGE.md` 自動更新：

```markdown
## 2026-04-21 新增

### Spring Boot 3.5 + Clean Architecture
- `@Repository` 註解放在 Adapter 層的 JPA 實作上，不放在 Port 介面
- Use Case 不應直接依賴 Spring 註解，保持領域純淨
- DTO ↔ Entity 轉換使用 Mapper 類，不在 Controller 直接操作 Entity

### Vue 3 + Pinia
- `defineStore` 建議使用 Setup Store 語法（Composition API 風格）
- Axios interceptor 統一處理 401 → 導向登入頁
```

### 10.8 Step 7：查看報告

Milestone 完成後，自動產生 HTML 報告：

```bash
# 手動產生報告
/gsd export --html

# 報告位置：.gsd/reports/
# 包含：專案摘要、進度樹、Slice 依賴圖、成本/Token 指標、執行時間線
```

> **💡 實務建議**：將 GSD 產生的 HTML 報告分享給專案經理和技術主管，提供 AI 開發的透明度與可追蹤性。

---

## 11. SSDLC 整合（安全開發）

### 11.1 安全開發生命週期整合概覽

```mermaid
graph TB
    subgraph "SSDLC + GSD Pi"
        direction TB
        A[需求階段<br/>Security Requirements] --> B[設計階段<br/>Threat Modeling]
        B --> C[開發階段<br/>Secure Coding]
        C --> D[測試階段<br/>Security Testing]
        D --> E[部署階段<br/>Secure Deployment]
        E --> F[維運階段<br/>Security Monitoring]
    end

    subgraph "GSD Pi 安全工具"
        G1[AGENTS.md<br/>安全編碼規範] --> C
        G2[verification_commands<br/>SAST + Lint] --> D
        G3[KNOWLEDGE.md<br/>安全知識庫] --> C
        G4[Headless Mode<br/>CI/CD 整合] --> E
        G5[Dependency Scan<br/>SCA] --> D
    end
```

### 11.2 Secure Prompt — 安全提示設計

在 `AGENTS.md` 中定義安全編碼規範：

```markdown
# AGENTS.md — 安全規範

## 必須遵守
- 所有 SQL 使用參數化查詢（PreparedStatement 或 JPA）
- 密碼使用 BCrypt（cost factor ≥ 12）加密
- 不得在日誌中輸出敏感資訊（密碼、API Key、Token）
- 所有 API 輸入必須驗證（使用 Bean Validation @Valid）
- CORS 設定必須明確指定允許的 Origin（禁止 *）
- JWT Token 必須設定過期時間（≤ 30 分鐘）
- 檔案上傳必須驗證副檔名和 MIME Type

## 禁止事項
- 禁止使用 eval() 或動態程式碼執行
- 禁止在前端儲存敏感資料（localStorage 存 JWT 除外）
- 禁止使用 MD5 / SHA-1 作為密碼雜湊
- 禁止關閉 CSRF 保護（除非 API-only 應用）
- 禁止在程式碼中硬編碼任何認證資訊
```

### 11.3 Code Scan（SAST）整合

```yaml
# .gsd/PREFERENCES.md
verification_commands:
  - mvn compile
  - mvn test
  - mvn checkstyle:check
  - mvn spotbugs:check           # 靜態分析（含安全規則）
  - mvn org.owasp:dependency-check-maven:check  # 依賴漏洞掃描
```

**SpotBugs 安全規則設定**（`pom.xml`）：

```xml
<plugin>
    <groupId>com.github.spotbugs</groupId>
    <artifactId>spotbugs-maven-plugin</artifactId>
    <version>4.8.6.6</version>
    <configuration>
        <plugins>
            <plugin>
                <groupId>com.h3xstream.findsecbugs</groupId>
                <artifactId>findsecbugs-plugin</artifactId>
                <version>1.13.0</version>
            </plugin>
        </plugins>
    </configuration>
</plugin>
```

### 11.4 Dependency Scan（SCA）

使用 OWASP Dependency Check：

```xml
<!-- pom.xml -->
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>10.0.4</version>
    <configuration>
        <failBuildOnCVSS>7</failBuildOnCVSS>
        <suppressionFiles>
            <suppressionFile>dependency-check-suppressions.xml</suppressionFile>
        </suppressionFiles>
    </configuration>
</plugin>
```

GSD 的 `verification_commands` 自動執行此掃描。若發現 CVSS ≥ 7 的漏洞，Task 驗證會失敗，觸發 Auto-fix。

### 11.5 API Security

在 `AGENTS.md` 加入 API 安全規範：

```markdown
## API 安全規範
- 所有 API 端點必須有認證（除了 /api/v1/auth/**）
- 使用 @PreAuthorize 進行方法級權限控制
- Rate Limiting：每個 IP 每分鐘最多 60 次請求
- 回應不得洩漏技術細節（關閉 Spring Boot 預設錯誤頁面）
- 所有 API 回應必須設定安全標頭：
  - X-Content-Type-Options: nosniff
  - X-Frame-Options: DENY
  - X-XSS-Protection: 1; mode=block
  - Strict-Transport-Security: max-age=31536000
```

### 11.6 DevSecOps 整合

將 GSD Headless Mode 與安全掃描整合到 CI/CD：

```yaml
# .github/workflows/security-scan.yml
name: Security Scan
on: [push, pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: SAST Scan (SpotBugs + FindSecBugs)
        run: mvn spotbugs:check

  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Dependency Check
        run: mvn org.owasp:dependency-check-maven:check

  sonarqube:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: SonarQube Scan
        run: |
          mvn sonar:sonar \
            -Dsonar.host.url=${{ secrets.SONAR_HOST }} \
            -Dsonar.token=${{ secrets.SONAR_TOKEN }}
```

### 11.7 KNOWLEDGE.md 安全知識庫

```markdown
# 安全知識庫

## OWASP Top 10 防護
### A01: Broken Access Control
- 使用 Spring Security Method Security（@PreAuthorize）
- 資源存取必須驗證 ownership

### A02: Cryptographic Failures
- 使用 BCrypt（cost ≥ 12）
- 傳輸層必須使用 TLS 1.2+
- 敏感資料加密存儲

### A03: Injection
- JPA 參數化查詢（永不拼接 SQL）
- Input Validation（@Valid + Custom Validator）

### A07: Security Misconfiguration
- 關閉 Spring Boot Actuator 的敏感端點
- 正式環境禁止開啟 debug 模式
```

> **💡 實務建議**：建議將安全掃描結果納入 GSD 的 `KNOWLEDGE.md`，讓 AI 在後續開發中自動避免已知的安全陷阱。每次安全稽核的發現都應更新知識庫。

---

## 12. 系統維護（Maintenance）

### 12.1 如何更新 Spec

當需求變更時，使用 GSD 的導引功能更新計畫：

```bash
# 方式 1：互動式討論
gsd
/gsd discuss
# 描述需求變更，GSD 自動更新 DECISIONS.md
# 變更在下一個 Phase 邊界被 Auto Mode 拾取

# 方式 2：Hard-steer（直接修改計畫）
/gsd steer
# 直接編輯 Roadmap 或 Slice Plan 文件

# 方式 3：重新思考
/gsd rethink
# 啟動對話式專案重組
```

### 12.2 如何修復 Bug

**快速修復**（不需要完整 Milestone）：

```bash
gsd
/gsd quick
# 描述 Bug 和期望行為
# GSD 以完整保證執行，但跳過規劃開銷
```

**複雜修復**（需要計畫）：

```bash
gsd
/gsd start bugfix
# 使用內建的 bugfix 工作流範本
# 自動建立修復分支、執行修復、驗證、合併
```

### 12.3 Forensics — 失敗調查

當 Auto Mode 失敗時，使用 Forensics 工具調查：

```bash
gsd
/gsd forensics
# 完整存取 GSD 除錯器
# 檢視 dispatch 決策、狀態轉換、計時數據
```

```bash
# 查看日誌
/gsd logs
# 瀏覽三種日誌：
# - Activity Log: 使用者活動
# - Debug Log: 除錯資訊
# - Metrics Log: 效能指標
```

### 12.4 如何讓 AI 持續學習

**策略 1：定期維護 KNOWLEDGE.md**

```bash
# 審查知識庫
cat .gsd/KNOWLEDGE.md

# 移除過時知識
# 補充新的最佳做法
# 更新技術限制
```

**策略 2：善用 Task Summary 回饋**

每個 Task 完成後會產生 `T01-SUMMARY.md`，包含 YAML frontmatter + 敘述：

```yaml
---
status: completed
duration_minutes: 8
tokens_used: 45000
cost_usd: 0.18
model: claude-sonnet-4-6
---

## 完成摘要
成功實作 CustomerController CRUD 端點。

## 教訓
- Spring Boot 3.5 的 `@RequestBody` 預設使用 Jackson 的 `@JsonNaming(SnakeCaseStrategy)`
- 分頁使用 `Pageable` 時，需在 Repository 方法上明確指定 Sort

## 待改善
- 缺少 Swagger 文件的詳細範例
```

**策略 3：Slice Discussion 人工指引**

```yaml
# .gsd/PREFERENCES.md
phases:
  require_slice_discussion: true
```

每個 Slice 開始前暫停，開發者可以：

- 審查計畫
- 提供額外背景
- 修正方向

**策略 4：使用 `/gsd discuss` 持續對話**

```bash
# 在 Auto Mode 執行期間，另一個終端討論
gsd
/gsd discuss
# 討論內容自動寫入 DECISIONS.md
# Auto Mode 在下一個 Phase 邊界拾取
```

### 12.5 Provider Error Recovery

GSD Pi 自動分類 Provider 錯誤並據此決定恢復策略：

| 錯誤類型 | 觸發條件 | 恢復行為 |
|----------|----------|----------|
| **Rate Limit** | 429、"too many requests" | 依據 `retry-after` 標頭或 60 秒後自動恢復 |
| **Server Error** | 500、502、503、"overloaded"、"api_error" | 30 秒後自動恢復 |
| **Permanent** | "unauthorized"、"invalid key"、"billing" | 無限期暫停，需人工處理 |

暫態錯誤不需人工介入 — Session 短暫暫停後自動繼續。模型回退鏈會在切換模型之前先重試暫態網路錯誤。

### 12.6 Failure Recovery

Auto Mode 的可靠性機制：

| 機制 | 說明 |
|------|------|
| **原子檔案寫入** | 防止崩潰時檔案損壞 |
| **OAuth 擷取超時** | 30 秒超時防止無限等待 |
| **RPC 子程序退出偵測** | 偵測並報告 RPC 子程序意外退出 |
| **Blob 垃圾回收** | 防止磁碟空間無限增長 |
| **Headless Auto-restart** | 崩潰時自動重啟（指數退避：5s → 10s → 30s，預設 3 次） |

```bash
# Headless Mode 配合自動重啟
gsd headless auto --max-restarts 5
```

### 12.7 Pipeline Architecture

Auto Mode 的迴圈結構為線性 Phase Pipeline（非遞迴分派）：

```mermaid
graph LR
    A[Pre-Dispatch<br/>驗證狀態<br/>檢查守衛<br/>解析模型] --> B[Dispatch<br/>執行單元<br/>注入 Prompt]
    B --> C[Post-Unit<br/>結束單元<br/>更新快取<br/>清理]
    C --> D[Verification<br/>驗證閘門<br/>Lint / Test]
    D --> E[Stuck Detection<br/>滑動窗口<br/>模式分析]
    E --> A
```

線性流程的優勢：

- **除錯容易**：每個 Phase 有明確的進入和退出條件
- **記憶體效率**：無遞迴呼叫堆疊
- **錯誤恢復**：每個 Phase 獨立恢復，不影響整體流程

### 12.8 清理與歸檔

```bash
# 歸檔已完成 Milestone 的 Phase 目錄
/gsd cleanup

# 查看 Milestone 報告
/gsd export --html
```

> **💡 實務建議**：建議每個 Sprint 結束時執行 `/gsd cleanup`，歸檔已完成的 Milestone。同時審查 `KNOWLEDGE.md`，確保知識庫保持最新。

### 12.9 Token Telemetry 與成本追蹤

GSD Pi v1.0 新增 Token Telemetry 功能，透過環境變數 `PI_TOKEN_TELEMETRY` 啟用詳細的 Token 使用量追蹤：

```bash
# 啟用 Token Telemetry
export PI_TOKEN_TELEMETRY=true
gsd
```

啟用後，系統會記錄每次 API 呼叫的：

| 指標 | 說明 |
|------|------|
| **Input Tokens** | 傳送給模型的 Token 數量 |
| **Output Tokens** | 模型回應的 Token 數量 |
| **Cache Read/Write** | 快取讀取和寫入的 Token 數量 |
| **Cost (USD)** | 基於各 Provider 定價計算的費用 |
| **Model** | 使用的模型名稱 |
| **Phase** | 所屬的工作階段（research / plan / execute / verify） |

```bash
# 查看成本報告
/gsd status
# Dashboard 顯示逐單元的 Token 使用量與成本
```

> **💡 實務建議**：企業環境中建議啟用 Token Telemetry，搭配 `budget_ceiling` 設定預算上限。定期匯出成本數據（`/gsd export --html`）作為專案成本分析的依據。

### 12.10 Unit Closeout 模組（v1.3.0）

GSD Pi v1.3.0 引入 **Unit Closeout 模組**，提供互動式工作項目收尾流程（Interactive Closeout Adapter）。每個 Task 完成後，系統主動引導開發者確認產出的完整性，並自動補全摘要、教訓萃取與 Git 提交：

**Closeout 流程**：

```text
Task 執行完成
  ↓
Unit Closeout 模組啟動
  ├─ 驗證 Must-haves 全部勾選
  ├─ 確認 Artifacts 全部存在
  ├─ 產生 Task Summary（T0x-SUMMARY.md）
  ├─ 萃取教訓 → 寫入 KNOWLEDGE.md
  └─ 建立 Git Commit（含結構化訊息）
  ↓
下一個 Task 分派
```

**啟用方式**（v1.3.0 預設啟用）：

```yaml
# .gsd/PREFERENCES.md
unit_closeout:
  enabled: true
  interactive: true        # 互動確認模式（Auto Mode 可設為 false）
  extract_learnings: true  # 自動萃取教訓到 KNOWLEDGE.md
  require_summary: true    # 強制產生 SUMMARY.md
```

**Headless / CI 環境**：

在 Headless Mode 中，`interactive: false` 時系統自動完成所有 Closeout 步驟，無需人工介入：

```bash
gsd headless auto --unit-closeout
```

**企業價值**：

| 面向 | 說明 |
| ---- | ---- |
| **可追蹤性** | 每個 Task 均有完整的 Summary + 教訓記錄 |
| **知識累積** | 自動萃取教訓，KNOWLEDGE.md 持續成長 |
| **審計合規** | Git History 包含結構化、有意義的提交訊息 |
| **品質門檻** | Must-haves 未完成時阻擋進入下一個 Task |

> **💡 實務建議**：企業環境中建議啟用 `require_summary: true`，確保每個 Task 均有書面記錄。搭配 `/gsd extract-learnings` 命令可手動觸發教訓萃取，適用於補充舊版 Session 的知識記錄。

---

## 13. 系統升級（Upgrade）

### 13.1 GSD Pi 升級與遷移策略

**從 GSD-2 遷移到 GSD Pi**：

```bash
# 步驟 1：移除舊版 GSD-2
npm uninstall -g gsd-pi

# 步驟 2：安裝新版 GSD Pi
npm install -g @opengsd/gsd-pi@latest

# 步驟 3：驗證安裝
gsd --version
# 應顯示 v1.0.x
```

**已安裝 GSD Pi 的更新**：

```bash
# 更新 GSD Pi 到最新版本
npm update -g @opengsd/gsd-pi

# 或指定版本
npm install -g @opengsd/gsd-pi@1.0.2

# 在 GSD 內部更新（Session 內即時更新）
gsd update

# 驗證版本
gsd --version
```

**升級注意事項**：

| 面向 | 說明 |
|------|------|
| **自動同步** | `npm update -g` 後立即生效，內建擴充每次啟動同步到 `~/.gsd/agent/` |
| **Schema 遷移** | 升級時自動套用 Schema 版本遷移 |
| **向下相容** | `.gsd/` 檔案格式保持向下相容，舊專案可直接使用新版本 |
| **套件範圍變更** | npm 套件從無範圍的 `gsd-pi` 改為 `@opengsd/gsd-pi` |

### 13.2 版本升級路徑

```mermaid
graph LR
    V1[GSD v1<br/>.planning/] -->|/gsd migrate| V2[GSD-2 v2.x<br/>.gsd/]
    V2 -->|npm uninstall + install| V3[GSD Pi v1.x<br/>@opengsd/gsd-pi]
```

**從 GSD-2 v2.x 遷移**：

`.gsd/` 目錄結構保持相容，只需更換安裝套件即可。`PREFERENCES.md`、`KNOWLEDGE.md`、`AGENTS.md` 等檔案不需修改。

**從 v1 遷移**：

```bash
# 在專案目錄中
gsd
/gsd migrate

# 或指定路徑
/gsd migrate ~/projects/my-old-project
```

遷移工具功能：

- 解析舊 `PROJECT.md`、`ROADMAP.md`、`REQUIREMENTS.md`、Phase 目錄
- 映射 Phases → Slices、Plans → Tasks
- 保留完成狀態（`[x]` 標記不變）
- 合併研究檔案到新結構
- 寫入前顯示預覽
- 可選的 Agent 驅動品質審查

### 13.3 Prompt 相容性

GSD Pi 的 Prompt 由系統自動管理，開發者不需要手動維護 Prompt 版本。但自定義的 `AGENTS.md` 需要注意：

```markdown
# AGENTS.md 版本管理建議

## 版本紀錄
- 2026-04-01: 初始版本，Java 21 + Spring Boot 3.5
- 2026-04-15: 新增 PostgreSQL JSONB 規範
- 2026-04-21: 更新 Security Config 為 Lambda DSL
```

### 13.4 知識庫遷移

升級時知識庫的處理策略：

1. **KNOWLEDGE.md**：自動保留，無需手動遷移
2. **DECISIONS.md**：Append-only 格式，天然向下相容
3. **Memories 表格**：v2.77 自動從舊路徑遷移到新的統一表格
4. **PREFERENCES.md**：新增的設定項使用預設值，既有設定不受影響

```yaml
# 檢查是否有 deprecated 的設定
# 舊：agent-instructions.md（已廢棄）
# 新：AGENTS.md 或 CLAUDE.md
```

> ⚠️ **注意**：`~/.gsd/agent-instructions.md` 和 `.gsd/agent-instructions.md` 格式已廢棄，不再被載入。請將內容遷移至 `AGENTS.md` 或 `CLAUDE.md`。

> **💡 實務建議**：建議在升級前先執行 `/gsd doctor` 確認系統健康，升級後再次執行確認一切正常。將升級時間安排在 Sprint 之間，避免影響進行中的 Milestone。

---

## 14. 最佳實務（Best Practices）

### 14.1 Prompt 設計原則

| 原則 | 說明 | 範例 |
|------|------|------|
| **具體明確** | 避免模糊描述 | ✅ "使用 BCrypt cost=12 加密" ❌ "加密密碼" |
| **結構化** | 使用 Markdown 格式 | 使用標題、清單、程式碼區塊 |
| **可驗證** | 定義 Must-haves | "檔案 X 必須存在，方法 Y 必須通過測試" |
| **有界限** | 明確範圍 | "只修改 UserService，不動 Controller" |
| **含上下文** | 提供背景 | "因為 PostgreSQL 不支援，所以改用..." |

### 14.2 Context 控制技巧

**技巧 1：善用 Token Profile**

```yaml
# .gsd/PREFERENCES.md
token_profile: balanced    # budget / balanced / quality

# budget:   省 40-60%，跳過研究/重評估，最少 Context
# balanced: 省 10-20%，跳過 Slice 研究，標準 Context
# quality:  不省，全 Phase 全 Context
```

**技巧 2：Complexity-based Routing**

GSD 自動將任務分為 simple / standard / complex，路由到適合的模型：

```
simple（文件任務）→ 快速模型（如 Haiku）
standard（一般開發）→ 標準模型（如 Sonnet）
complex（架構設計）→ 強力模型（如 Opus）
```

**技巧 3：Budget Pressure**

```yaml
budget_ceiling: 100.00    # USD 上限
```

接近上限時自動降級模型：

- 50% 使用量 → 開始漸進降級
- 75% 使用量 → 更多工作交給便宜模型
- 90% 使用量 → 全部使用最便宜模型

**技巧 4：Per-Phase Model 選擇**

```yaml
models:
  research: openrouter/deepseek/deepseek-r1    # 便宜但夠用
  planning:
    model: claude-fable-5                       # Fable 5 — Opus-tier 思考（v1.3.0）
    fallbacks:
      - claude-opus-4-8                         # Opus 4.8（v1.1.0）
      - openrouter/z-ai/glm-5                  # 社群 Fallback
  execution: claude-sonnet-4-6                  # 平衡的執行模型
  completion: claude-sonnet-4-6                 # 快速完成
```

**技巧 5：Per-Phase Thinking Level（v1.2.0）** — 搭配模型選擇，獨立控制各階段的推理深度，精準優化成本：

```yaml
# .gsd/PREFERENCES.md
phases:
  planning:
    thinking_level: high       # 規劃：完整延伸思考，確保架構正確
  execution:
    thinking_level: medium     # 執行：標準推理，平衡品質與速度
  completion:
    thinking_level: low        # 完成：快速產出摘要，節省 Token
```

此設定可節省 Completion 階段 30–50% Token，同時確保 Planning 階段品質最高。

### 14.3 避免 Hallucination

| 策略 | 做法 |
|------|------|
| **驗證指令** | 設定 `verification_commands` 確保程式碼可編譯、測試通過 |
| **Must-haves** | 每個 Task 定義機械式可驗證的 Truths 和 Artifacts |
| **KNOWLEDGE.md** | 提供正確的技術知識，減少 AI 猜測 |
| **AGENTS.md** | 明確規範禁止事項 |
| **Fresh Context** | 每個 Task 全新 Session，避免累積混淆 |
| **Skill Discovery** | 載入領域專業技能，提供準確知識 |

### 14.4 大型專案管理技巧

**技巧 1：平行 Milestone 執行**

```bash
# 多個 Worker 同時執行不同 Milestone
# 使用 .gsd/parallel/ 協調

# Terminal 1
gsd --worktree
/gsd auto  # Milestone A

# Terminal 2
gsd --worktree
/gsd auto  # Milestone B
```

**技巧 2：Git Worktree 隔離**

```yaml
# .gsd/PREFERENCES.md
git:
  isolation: worktree    # none / worktree / branch
```

每個 Milestone 在獨立的 Worktree 中工作：

- 不會有分支切換衝突
- Milestone 完成後 Squash Merge
- Git Bisect 可追溯個別 Milestone

**技巧 3：排隊 Milestone**

```bash
gsd
/gsd queue
# 在 Auto Mode 運行期間，安全地排隊下一個 Milestone
```

**技巧 4：Workflow Templates**

```bash
# 使用內建工作流範本
/gsd start bugfix      # Bug 修復流程
/gsd start release     # 發佈流程

# 查看可用範本
/gsd workflow list

# 安裝自訂範本
/gsd workflow install my-workflow.md
```

### 14.5 成本控制

```bash
# 查看成本報告
/gsd status

# Dashboard 顯示：
# - 每單元 Token 使用量與成本
# - 按 Phase / Slice / Model 分類
# - 成本預測（基於已完成工作）
# - 預算使用率
```

```yaml
# .gsd/PREFERENCES.md
budget_ceiling: 50.00              # USD 上限
token_profile: balanced             # Token 優化策略
budget_enforcement: pause           # warn | pause | halt
auto_supervisor:
  hard_timeout_minutes: 30          # 單任務最長時間
show_token_cost: true               # 即時顯示 Token 成本
service_tier: default               # default | flex（低優先低價）
```

**預算強制模式**：

| 模式 | 行為 | 適用場景 |
|------|------|----------|
| `warn` | 超出預算時顯示警告，繼續執行 | 開發探索階段 |
| `pause` | 暫停並等待人工確認 | 互動開發（預設） |
| `halt` | 立即終止 Session | CI/CD 管線 |

**Fast 模式**：

```bash
gsd
/gsd fast          # 切換 service_tier: flex（較低價格但可能較慢）
```

> **💡 實務建議**：開始使用 GSD Pi 時，建議先用 `token_profile: quality` 並設定較低的 `budget_ceiling`（如 $10），觀察 AI 行為。熟悉後再調整為 `balanced` 並提高預算。

### 14.6 Hooks 系統

Hooks 系統提供生命週期擴充點，在 Auto Mode 關鍵階段注入自訂行為。

#### Post-Unit Hooks（單元後鉤子）

每個單元完成後自動觸發。典型用途：自動生成 Changelog、更新文件、檢查一致性。

```yaml
# .gsd/PREFERENCES.md
post_unit_hooks:
  - name: "generate-changelog"
    after: "code"              # code | test | doc | any
    prompt: "根據最近修改生成 CHANGELOG.md 更新條目"
    model: "claude-sonnet-4-6"
    max_cycles: 3
    artifact: "changelog.md"
    retry_on: "no changes"
    agent: "worker"
    enabled: true
  
  - name: "api-doc-sync"
    after: "code"
    prompt: "確保 OpenAPI spec 與實作一致"
    model: "claude-sonnet-4-6"
    max_cycles: 2
    agent: "worker"
    enabled: true
```

**Post-Unit Hook 參數**：

| 參數 | 類型 | 說明 |
|------|------|------|
| `name` | string | Hook 唯一標識名稱 |
| `after` | string | 觸發時機：`code`、`test`、`doc`、`any` |
| `prompt` | string | 傳遞給 Agent 的指令 |
| `model` | string | 使用的模型（可覆蓋全域設定） |
| `max_cycles` | number | 最大執行回合數 |
| `artifact` | string | 產出檔案路徑 |
| `retry_on` | string | 失敗關鍵字，符合時自動重試 |
| `agent` | string | 執行 Hook 的 Agent |
| `enabled` | boolean | 是否啟用 |

#### Pre-Dispatch Hooks（分派前鉤子）

在分派單元之前觸發，可修改、跳過或替換即將執行的單元。

```yaml
# .gsd/PREFERENCES.md
pre_dispatch_hooks:
  - name: "security-gate"
    condition: "unit.type == 'code'"
    action: modify              # modify | skip | replace
    prompt: "在單元指令前加入安全掃描要求"
    enabled: true

  - name: "skip-docs-on-hotfix"
    condition: "branch.startsWith('hotfix/') && unit.type == 'doc'"
    action: skip
    enabled: true
```

**Pre-Dispatch Hook 動作**：

| 動作 | 說明 |
|------|------|
| `modify` | 修改單元的 Prompt 或參數 |
| `skip` | 跳過該單元 |
| `replace` | 用替代指令取代原始單元 |

#### Layer 0 Shell Hooks（v2.77）

v2.77 新增 Layer 0 shell hooks，在每個單元之前或之後執行 shell 命令：

```yaml
# .gsd/PREFERENCES.md
hooks:
  pre_unit:
    - command: "npm run lint:fix"
      on_fail: warn            # warn | abort
  post_unit:
    - command: "npm test"
      on_fail: abort
```

### 14.7 Reactive Task Execution 實務

Reactive Execution 在 Slice 內建立任務依賴圖，實現安全的平行執行：

```yaml
# .gsd/PREFERENCES.md（v1.0 新格式，舊版布林值仍向下相容）
reactive_execution:
  enabled: true
  max_parallel: 3            # 最大平行任務數
  isolation_mode: worktree   # worktree | branch
  subagent_model: ""         # 留空時使用主模型
```

> **⚠ 遷移提示**：舊版 `reactive_execution: true`（布林值）格式仍可使用，GSD Pi 會自動轉換為等效物件設定。

**企業應用範例**：

```
Slice: "新增使用者管理 API"
├─ Task A: 建立 Entity 類別         ← 無依賴，立即執行
├─ Task B: 建立 Repository 介面      ← 依賴 A
├─ Task C: 建立 Service 層           ← 依賴 B
├─ Task D: 建立 Controller           ← 依賴 C
├─ Task E: 建立資料庫 Migration      ← 依賴 A，與 B/C/D 平行
└─ Task F: 建立整合測試              ← 依賴 C + D
```

衝突偵測機制：若 Task E 和 Task B 同時修改同一檔案，系統自動序列化執行。

> **💡 提示**：Reactive Execution 自 GSD Pi v1.0 起已預設啟用，並在生產環境中廣泛驗證。對於頻繁修改相同檔案的 Task，系統會自動序列化執行，無需手動關閉此功能。

### 14.8 企業指引範本

```yaml
# .gsd/PREFERENCES.md（企業範本）
provider: anthropic
model: claude-sonnet-4-6
planning_model: claude-opus-4-7
auto_mode:
  iterations: 10
  cost_limit: 3.00
  budget_enforcement: pause
git:
  isolation: worktree
  auto_push: true
  push_branches: auto
  snapshots: true
  auto_pr: true
  pr_target_branch: develop
  merge_strategy: squash
skill_discovery: suggest
custom_instructions:
  - "所有 API 端點必須包含 OpenAPI 註解"
  - "程式碼必須符合 SonarQube Quality Gate"
  - "日誌必須使用結構化格式（JSON）"
  - "資料庫操作必須在 Transaction 內完成"
context_management:
  observation_masking: true
  compaction_threshold: 30000
notifications:
  enabled: true
  on_complete: true
  on_error: true
  on_budget: true
remote_questions:
  channel: telegram
  channel_id: "your-chat-id"
```

### 14.9 Per-Model MCP 過濾與 URL 安全

GSD Pi v1.0 新增按模型過濾 MCP Server 的能力，可控制不同模型存取不同的工具集：

```yaml
# .gsd/PREFERENCES.md
mcp_model_filter:
  claude-sonnet-4-6:
    allow:
      - browser
      - github
    deny: []
  gpt-4o:
    allow:
      - browser
    deny:
      - github
```

**URL 安全防護（SSRF Protection）**：

GSD Pi 內建 `fetchBlockedUrls` 清單，防止 MCP Server 存取內部網路或敏感 URL：

```yaml
# 內建封鎖規則（不可覆寫）
fetchBlockedUrls:
  - "169.254.*"         # AWS Metadata（SSRF 防護）
  - "10.*"              # 私有網段
  - "192.168.*"         # 私有網段
  - "127.0.0.1"         # Localhost
```

> **💡 實務建議**：企業環境中，建議明確設定 `mcp_model_filter`，依據模型能力和信任等級分配工具存取權限。搭配 URL 封鎖規則，可有效防止 Server-Side Request Forgery（SSRF）攻擊。

---

## 15. 常見問題（FAQ）

### 15.1 AI 不照 Spec 怎麼辦？

**原因分析**：

1. **Spec 不夠具體**：模糊的需求導致 AI 自行解讀
2. **AGENTS.md 缺失**：沒有明確的編碼規範
3. **Context 不足**：相關知識未載入

**解決方案**：

```bash
# 1. 豐富 AGENTS.md
# 加入具體的技術規範和禁止事項

# 2. 使用 /gsd steer 修正計畫
/gsd steer
# 直接修改 Slice Plan 或 Task Plan

# 3. 使用 /gsd discuss 提供額外指引
/gsd discuss
# 討論具體期望，決策記錄到 DECISIONS.md

# 4. 啟用 Slice Discussion
# .gsd/PREFERENCES.md
# phases:
#   require_slice_discussion: true
```

### 15.2 產生的 Code 不可用？

**檢查清單**：

1. **驗證指令是否設定正確？**
   ```yaml
   verification_commands:
     - mvn compile
     - mvn test
   ```
2. **Auto-fix 是否啟用？**
   ```yaml
   verification_auto_fix: true
   verification_max_retries: 2
   ```
3. **KNOWLEDGE.md 是否包含正確的技術知識？**
4. **模型選擇是否適當？**（弱模型可能產出低品質程式碼）

### 15.3 Context 過大怎麼辦？

**症狀**：Token 使用量高、成本快速增長、Task 執行緩慢

**解決方案**：

```yaml
# 1. 使用 Token 優化
token_profile: budget    # 省 40-60%

# 2. 使用 Complexity Routing
# 簡單任務自動用便宜模型

# 3. 拆分 Task
# 確保每個 Task 在一個 Context Window 內完成

# 4. 減少 Context 注入
# 精簡 KNOWLEDGE.md，只保留相關知識
```

### 15.4 Auto Mode 卡住怎麼辦？

```bash
# 1. 按 Escape 暫停
# 檢查當前狀態

# 2. 查看 Forensics
/gsd forensics

# 3. 手動推進
/gsd next
# 以 Step Mode 手動推進一步

# 4. 檢查健康度
/gsd doctor
```

GSD 內建卡住偵測：

- 滑動窗口偵測重複的 Dispatch 模式
- 偵測到後自動重試一次（含深度診斷）
- 再次失敗則暫停並報告

### 15.5 如何恢復崩潰的 Session？

```bash
# GSD 自動恢復
gsd
/gsd auto
# 讀取 auto.lock，合成恢復簡報，從中斷點繼續

# 恢復特定 Session
gsd sessions
# 互動式 Session 選擇器

# 恢復最近的 Session
gsd --continue
# 或
gsd -c
```

### 15.6 團隊成員 Milestone ID 衝突？

```yaml
# .gsd/PREFERENCES.md
unique_milestone_ids: true
# Milestone 名稱會附加 6 字元隨機字串
# 例如：M001-ush8s3（而非 M001）
```

### 15.7 如何在企業防火牆環境使用？

```bash
# 設定 Proxy
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# 使用 API Key（避免 OAuth）
gsd config
# 選擇 API Key 認證方式
```

> **💡 實務建議**：建立團隊 FAQ 文件，收集常見問題和解決方案。將解決方案同步更新到 `KNOWLEDGE.md`，讓 AI 也能從中學習。

### 15.8 如何使用本地 LLM（Ollama）？

GSD Pi v1.0 新增 Ollama 支援，可在完全離線的環境下運行：

```bash
# 步驟 1：安裝並啟動 Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama serve

# 步驟 2：下載模型
ollama pull qwen2.5-coder:32b

# 步驟 3：設定 GSD Pi 使用 Ollama
gsd config
# Provider: ollama
# Model: qwen2.5-coder:32b
```

```yaml
# .gsd/PREFERENCES.md
provider: ollama
model: qwen2.5-coder:32b
planning_model: qwen2.5-coder:32b
```

**Ollama 注意事項**：

| 面向 | 說明 |
|------|------|
| **硬體需求** | 32B 模型建議 24GB+ VRAM（RTX 4090 或 A100） |
| **效能** | 本地推論速度視 GPU 而定，通常慢於雲端 API |
| **功能限制** | 較小模型可能在複雜規劃任務中表現不佳 |
| **離線優勢** | 完全不需要網路，資料不離開本機 |
| **自訂模型** | 可透過 `models.json` 定義自訂模型（見附錄 D.8） |

---

## 16. 團隊導入建議（Enterprise Adoption）

### 16.1 導入策略（分階段）

```mermaid
graph LR
    P1[Phase 1<br/>試點<br/>2-4 週] --> P2[Phase 2<br/>擴展<br/>4-8 週]
    P2 --> P3[Phase 3<br/>全面導入<br/>8-12 週]
    P3 --> P4[Phase 4<br/>持續優化<br/>持續]
```

#### Phase 1：試點（2-4 週）

| 項目 | 內容 |
|------|------|
| **目標** | 驗證 GSD Pi 在團隊中的可行性 |
| **範圍** | 1-2 位資深工程師，1 個非關鍵專案 |
| **工作** | 安裝環境、建立 AGENTS.md、完成一個 Milestone |
| **產出** | 試點報告（成本、品質、效率評估） |

#### Phase 2：擴展（4-8 週）

| 項目 | 內容 |
|------|------|
| **目標** | 建立團隊標準與最佳做法 |
| **範圍** | 3-5 位工程師，2-3 個專案 |
| **工作** | 標準化 AGENTS.md 範本、建立 KNOWLEDGE.md 共享機制 |
| **產出** | 團隊操作手冊、標準 AGENTS.md 範本 |

#### Phase 3：全面導入（8-12 週）

| 項目 | 內容 |
|------|------|
| **目標** | 全團隊導入 GSD Pi |
| **範圍** | 所有專案團隊 |
| **工作** | CI/CD 整合、Headless Mode 設定、成本預算管理 |
| **產出** | 完整的 DevSecOps 流程、成本報告機制 |

#### Phase 4：持續優化（持續）

| 項目 | 內容 |
|------|------|
| **目標** | 持續提升 AI 協作效率 |
| **範圍** | 全組織 |
| **工作** | 知識庫維護、技能管理、版本升級 |
| **產出** | 月度效能報告、知識庫更新 |

### 16.2 教育訓練方式

**課程規劃**：

| 階段 | 主題 | 時數 | 對象 |
|------|------|------|------|
| Level 1 | GSD Pi 基礎操作 | 2h | 所有工程師 |
| Level 2 | Spec-Driven 開發 | 4h | 開發工程師 |
| Level 3 | Context Engineering | 3h | 資深工程師 |
| Level 4 | CI/CD 整合 & 管理 | 2h | DevOps / 主管 |

**Level 1 課程大綱**：

1. GSD Pi 概念與安裝（30 min）
2. 首次啟動與 Provider 設定（15 min）
3. Step Mode 操作實戰（30 min）
4. Auto Mode 操作實戰（30 min）
5. Q&A（15 min）

**Level 2 課程大綱**：

1. Spec 撰寫技巧（60 min）
2. AGENTS.md 設計（30 min）
3. 驗證指令設定（30 min）
4. 實作練習：完成一個 Milestone（120 min）

### 16.3 Governance（治理）

#### 成本治理

```yaml
# 組織級預算控制
# 每個專案 .gsd/PREFERENCES.md
budget_ceiling: 50.00        # 每 Milestone 預算上限
token_profile: balanced       # Token 優化策略
```

建議建立成本報告機制：

```bash
# 每週產出成本報告
/gsd status > weekly-cost-report.md

# 使用 Headless Query 自動收集
gsd headless query
# 回傳 JSON：phase、next dispatch、成本
```

#### 安全治理

| 項目 | 規範 |
|------|------|
| **API Key 管理** | 使用組織級密鑰管理（Vault / GitHub Secrets） |
| **程式碼審查** | GSD 產出的程式碼仍需人工 Code Review |
| **知識庫審查** | 定期審查 KNOWLEDGE.md 中的安全相關知識 |
| **模型選擇** | 統一使用組織核准的 LLM Provider |
| **資料保護** | 確保敏感資料不會被送入 LLM（在 AGENTS.md 中明確禁止） |

#### 品質治理

```yaml
# 強制驗證（不可跳過）
verification_commands:
  - mvn compile
  - mvn test
  - mvn checkstyle:check
  - mvn spotbugs:check
verification_auto_fix: true
verification_max_retries: 2
```

#### Git 治理

```yaml
# 團隊 Git 設定
git:
  isolation: worktree          # Worktree 隔離
  manage_gitignore: true       # GSD 管理 .gitignore

unique_milestone_ids: true     # 避免 Milestone ID 衝突
```

建議的 `.gitignore` 設定（團隊協作）：

```gitignore
# ── GSD: Runtime / Ephemeral（每人每 Session）──
.gsd/auto.lock
.gsd/completed-units*.json
.gsd/state-manifest.json
.gsd/STATE.md
.gsd/metrics.json
.gsd/activity/
.gsd/runtime/
.gsd/worktrees/
.gsd/parallel/
.gsd/gsd.db*
.gsd/journal/
.gsd/doctor-history.jsonl
.gsd/event-log.jsonl
.gsd/reports/
.gsd/milestones/**/continue.md
.gsd/milestones/**/*-CONTINUE.md

# ── GSD: 納入版控的檔案 ──
# .gsd/PREFERENCES.md    → 團隊共享設定
# .gsd/PROJECT.md         → 專案描述
# .gsd/DECISIONS.md       → 架構決策
# .gsd/KNOWLEDGE.md       → 知識庫
# .gsd/RUNTIME.md         → 執行環境
# .gsd/milestones/        → Milestone 計畫與成果
```

> **💡 實務建議**：導入初期，建議指定一位「GSD Champion」負責推動、收集回饋和解決問題。定期舉辦「GSD 分享會」，讓團隊成員交流使用心得。

---

## 17. 檢查清單（Checklist）

### 17.1 環境建置 Checklist

- [ ] Node.js ≥ 22.0.0 已安裝（推薦 24 LTS）
- [ ] `npm install -g @opengsd/gsd-pi@latest` 已執行
- [ ] `gsd --version` 顯示正確版本
- [ ] Git 已安裝並初始化
- [ ] LLM Provider 已設定（`gsd config` 或 `/login`）
- [ ] API Key 已設定（企業環境建議使用 API Key 而非 OAuth）
- [ ] `/gsd doctor` 健康檢查通過
- [ ] VS Code GSD 擴充已安裝（選用）

### 17.2 專案初始化 Checklist

- [ ] `AGENTS.md` 已撰寫（含程式碼風格、安全規範、測試要求）
- [ ] `.gsd/PREFERENCES.md` 已設定
  - [ ] `models` 已選擇適合的模型
  - [ ] `budget_ceiling` 已設定
  - [ ] `verification_commands` 已配置
  - [ ] `unique_milestone_ids: true`（團隊協作）
  - [ ] `git.isolation: worktree`（建議）
- [ ] `.gitignore` 已設定 GSD 相關規則
- [ ] Spec 已撰寫（含功能需求、非功能需求、技術限制）

### 17.3 日常開發 Checklist

- [ ] Terminal 1 執行 `/gsd auto`
- [ ] Terminal 2 可用 `/gsd discuss` / `/gsd status`
- [ ] 驗證指令通過率 > 90%
- [ ] `KNOWLEDGE.md` 定期更新
- [ ] 成本在預算內
- [ ] Git 提交訊息有意義

### 17.4 安全 Checklist

- [ ] `AGENTS.md` 包含安全編碼規範
- [ ] `verification_commands` 包含安全掃描（SpotBugs / Dependency Check）
- [ ] API Key 使用密鑰管理（不硬編碼）
- [ ] GSD 產出的程式碼已通過人工 Code Review
- [ ] 敏感資料不會被送入 LLM（在 AGENTS.md 中明確禁止）
- [ ] OWASP Top 10 防護知識已納入 `KNOWLEDGE.md`

### 17.5 團隊協作 Checklist

- [ ] `unique_milestone_ids: true` 已啟用
- [ ] `.gsd/PREFERENCES.md` 已納入版本控制
- [ ] `AGENTS.md` 範本已建立並共享
- [ ] `KNOWLEDGE.md` 維護責任已指派
- [ ] 成本報告機制已建立
- [ ] 新成員入職培訓材料已準備

### 17.6 GSD Pi 命令速查表

| 命令 | 說明 |
|------|------|
| `gsd` | 啟動 GSD 互動式 Session |
| `gsd config` | 重新執行設定精靈 |
| `gsd update` | 更新 GSD 到最新版本 |
| `gsd --continue` (`-c`) | 恢復最近的 Session |
| `gsd --worktree` (`-w`) | 啟動 Worktree 隔離 Session |
| `gsd --web` | 啟動 Web 管理介面 |
| `gsd --debug` | 啟用除錯日誌 |
| `gsd sessions` | 互動式 Session 選擇器 |
| `gsd headless [cmd]` | 無 TUI 執行（CI/cron） |
| `gsd headless auto` | Headless 自動模式（含 `--max-restarts`） |
| `gsd headless query` | 即時 JSON 快照（無 LLM） |
| `/gsd` | Step Mode — 逐步執行 |
| `/gsd auto` | Auto Mode — 自主執行 |
| `/gsd quick` | 快速任務（跳過規劃） |
| `/gsd stop` | 停止 Auto Mode |
| `/gsd steer` | 修改計畫文件 |
| `/gsd discuss` | 架構討論（可併行 Auto） |
| `/gsd rethink` | 專案重組 |
| `/gsd status` | 進度儀表板 |
| `/gsd queue` | 排隊下一個 Milestone |
| `/gsd capture "..."` | 思緒捕捉（fire-and-forget） |
| `/gsd visualize` | 工作流視覺化器 |
| `/gsd fast` | 切換 Fast Mode（`service_tier: flex`） |
| `/gsd prefs` | 設定偏好 |
| `/gsd prefs project` | 專案級偏好設定 |
| `/gsd prefs global` | 全域偏好設定 |
| `/gsd prefs status` | 顯示當前偏好（含來源） |
| `/gsd prefs wizard` | 互動式偏好精靈 |
| `/gsd prefs import-claude` | 匯入 Claude Code 設定 |
| `/gsd doctor` | 健康檢查 |
| `/gsd usage` | 查看 Session Token 用量與費用（v1.1.0） |
| `/gsd context` | 查看 Context 使用狀態與載入的 Artifacts（v1.1.0） |
| `/gsd forensics` | 失敗調查 |
| `/gsd logs` | 日誌瀏覽 |
| `/gsd export --html` | 產生 HTML 報告 |
| `/gsd cleanup` | 歸檔已完成 Milestone |
| `/gsd migrate` | v1 → v2 遷移 |
| `/gsd help` | 指令參考 |
| `/gsd mode` | 切換 Solo / Team 模式 |
| `/gsd workflow` | 工作流插件管理 |
| `/gsd start <template>` | 啟動工作流範本 |
| `/gsd keys` | API Key 管理 |
| `/gsd mcp` | MCP Server 狀態 |
| `/gsd brief` | 產出 Visual Briefs（Mermaid 視覺化摘要） |
| `/gsd ship` | 發佈流程（版本、Changelog、Tag） |
| `/gsd scan` | 程式碼掃描（安全、品質） |
| `/gsd codebase` | 程式碼庫分析 |
| `/gsd debug` | 除錯模式 |
| `/gsd language` | 切換語言 |
| `/gsd recover` | Session 恢復（Headless 增強） |
| `/gsd extensions` | 擴充套件管理（install / uninstall / update） |
| `/gsd eval-review` | 評估審查 |
| `/gsd extract-learnings` | 從 Session 中擷取學習心得 |
| `/gsd backlog` | Backlog 管理 |
| `/gsd knowledge <type> <desc>` | 新增知識條目（rule / pattern / lesson） |
| `/worktree` (`/wt`) | Git Worktree 管理 |
| `Ctrl+Alt+G` | Dashboard 覆疊 |
| `Escape` | 暫停 Auto Mode |

---

## 附錄 A：GSD Pi 內建擴充套件一覽

| 擴充套件 | 功能 |
|----------|------|
| GSD | 核心工作流引擎、Auto Mode、命令、Dashboard |
| Browser Tools | Playwright 瀏覽器（含表單智慧、語義操作、PDF 匯出） |
| Search the Web | Brave Search / Tavily / Jina 頁面擷取 |
| Google Search | Gemini 網路搜尋 + AI 綜合回答 |
| Context7 | 最新函式庫 / 框架文件 |
| Background Shell | 長執行程序管理 + 就緒偵測 |
| Async Jobs | 背景 Bash 指令 + 工作追蹤 |
| Subagent | 隔離 Context Window 的委派任務 |
| GitHub | GitHub Issues / PR 全套管理 |
| Mac Tools | macOS Accessibility API 自動化 |
| MCP Client | MCP Server 原生整合 |
| Voice | 即時語音轉文字（macOS / Linux） |
| Slash Commands | 自訂命令建立 |
| Ask User Questions | 結構化使用者輸入 |
| Secure Env Collect | 遮罩式密鑰收集 |
| Remote Questions | 路由決策到 Slack / Discord |
| Universal Config | 匯入其他 AI 工具的 MCP 設定 |
| AWS Auth | Bedrock 認證自動刷新 |
| Ollama | 本地 LLM（Ollama）整合 |
| Claude Code CLI | Claude Code CLI 外部 Provider |
| cmux | Claude 多工器整合 |
| GitHub Sync | 自動同步 Milestone 到 GitHub Issues / PR |
| LSP | Language Server Protocol 整合 |
| TTSR | 工具觸發系統規則 |

---

## 附錄 B：相關資源

| 資源 | 連結 |
|------|------|
| **官方網站** | https://www.opengsd.net |
| **Web 配置器** | https://pi.opengsd.net |
| GitHub Repository（新） | https://github.com/open-gsd/gsd-pi |
| GitHub Repository（舊，已封存） | https://github.com/gsd-build/gsd-2 |
| npm Package | https://www.npmjs.com/package/@opengsd/gsd-pi |
| Getting Started Guide | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/getting-started.md |
| Auto Mode Guide | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/auto-mode.md |
| Configuration Guide | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/configuration.md |
| Token Optimization | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/token-optimization.md |
| Cost Management | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/cost-management.md |
| Git Strategy | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/git-strategy.md |
| Skills Guide | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/skills.md |
| Docker Sandbox | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/docker.md |
| Web Interface | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/web-interface.md |
| Remote Questions | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/remote-questions.md |
| Dynamic Model Routing | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/dynamic-routing.md |
| Parallel Orchestration | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/parallel.md |
| Visualizer | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/visualizer.md |
| Captures & Triage | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/captures.md |
| Troubleshooting | https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/troubleshooting.md |
| Architecture | https://github.com/open-gsd/gsd-pi/blob/main/docs/dev/architecture.md |
| Discord Community | https://discord.gg/8NnkKuepmQ |
| Changelog | https://github.com/open-gsd/gsd-pi/blob/main/CHANGELOG.md |
| License | MIT License |

---

## 附錄 C：MCP Server 設定指南

### C.1 概述

GSD Pi 既是 MCP Client（連線到外部工具），也可作為 MCP Server（暴露自身功能供其他工具呼叫）。

### C.2 連線外部 MCP Server

**設定檔位置**：

| 層級 | 檔案路徑 | 說明 |
|------|----------|------|
| 專案級 | `.mcp.json`（專案根目錄） | 納入版控，團隊共用 |
| GSD 專用 | `.gsd/mcp.json` | 不納入版控，個人設定 |
| 全域 | `~/.gsd/mcp.json` | 所有專案共用 |

**stdio 傳輸（推薦）**：

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/mydb"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**HTTP 傳輸（StreamableHTTP）**：

```json
{
  "mcpServers": {
    "remote-api": {
      "url": "https://mcp.example.com/sse",
      "headers": {
        "Authorization": "Bearer ${API_TOKEN}"
      }
    }
  }
}
```

### C.3 驗證 MCP 連線

```bash
gsd
/gsd mcp
# 顯示所有已連線的 MCP Server 及可用工具

# 或在 Doctor 中檢查
/gsd doctor
# MCP 區段會顯示連線狀態
```

### C.4 匯入其他工具的 MCP 設定

GSD Pi 的 Universal Config 擴充可自動匯入 Claude Code、Cursor 等工具的 MCP 設定：

```bash
gsd
/gsd prefs import-claude
# 自動偵測並匯入 claude_desktop_config.json 中的 MCP 設定
```

### C.5 Cloud MCP Gateway

GSD Pi v1.0 新增 Cloud MCP Gateway，可透過雲端閘道集中管理 MCP Server，無需在每台開發機上安裝所有 MCP Server：

```json
{
  "mcpServers": {
    "cloud-gateway": {
      "type": "streamable-http",
      "url": "https://mcp-gateway.company.com/sse",
      "headers": {
        "Authorization": "Bearer ${MCP_GATEWAY_TOKEN}"
      }
    }
  }
}
```

**優勢**：
- **集中管理**：統一管理所有 MCP Server 的版本和設定
- **存取控制**：透過 Gateway 層實施 RBAC 和稽核日誌
- **減少本地安裝**：開發者只需連線到 Gateway，無需安裝各個 MCP Server

### C.6 企業注意事項

- **安全性**：MCP Server 可能存取外部系統，確保僅連線到受信任的 Server
- **環境變數**：使用 `${VAR_NAME}` 語法引用環境變數，避免在設定檔中硬編碼敏感資訊
- **網路限制**：若企業防火牆限制外部連線，建議使用 stdio 傳輸（本地 subprocess）

---

## 附錄 D：進階設定參考

本附錄列出 `.gsd/PREFERENCES.md` 中所有進階設定選項。

### D.1 Dynamic Model Routing

根據任務複雜度自動選擇模型：

```yaml
dynamic_routing:
  enabled: true
  rules:
    - condition: "task.complexity == 'low'"
      model: "claude-haiku-4"
    - condition: "task.complexity == 'medium'"
      model: "claude-sonnet-4-6"
    - condition: "task.complexity == 'high'"
      model: "claude-opus-4-7"
    - condition: "task.type == 'test'"
      model: "claude-sonnet-4-6"
```

### D.2 Notifications

```yaml
notifications:
  enabled: true
  on_complete: true      # Milestone 完成時通知
  on_error: true         # 錯誤發生時通知
  on_budget: true        # 接近預算上限時通知
  on_milestone: true     # 里程碑狀態變更時通知
  on_attention: true     # 需要人工注意時通知
```

### D.3 Context Management

```yaml
context_management:
  observation_masking: true     # 遮蔽冗長工具觀察結果
  compaction_threshold: 30000   # Token 超過此閾值時觸發壓縮

context_pause_threshold: 0.8    # Context 壓力 80% 時暫停
```

### D.4 Git 進階設定

```yaml
git:
  isolation: worktree          # none | worktree | branch
  auto_push: true              # 單元完成後自動 push
  push_branches: auto          # auto | always | never
  snapshots: true              # 每個單元完成後建立快照
  pre_merge_check: true        # Merge 前執行驗證指令
  commit_type: conventional    # conventional | descriptive | minimal
  main_branch: main            # 主分支名稱
  merge_strategy: squash       # squash | merge | rebase
  commit_docs: true            # 在 commit message 中附加文件
  auto_pr: true                # Milestone 完成後自動建立 PR
  pr_target_branch: develop    # PR 目標分支
  worktree_post_create: ""     # Worktree 建立後執行的命令
  manage_gitignore: true       # GSD 自動管理 .gitignore
```

### D.5 GitHub Sync

自動將 Milestone 進度同步到 GitHub Issues 和 Pull Request：

```yaml
github:
  sync: true                   # 啟用 GitHub 同步
  auto_issue: true             # 自動建立 Issue
  auto_pr: true                # 自動建立 PR
  labels:
    - "gsd-auto"
    - "ai-generated"
```

### D.6 Forensics 和除錯

```yaml
forensics_dedup: true          # 去重重複的 Forensics 記錄
show_token_cost: true          # 即時顯示每個 API 呼叫的成本
auto_visualize: true           # Milestone 完成後自動開啟視覺化器
```

### D.7 Parallel Orchestration

```yaml
parallel:
  max_concurrent: 3            # 最大同時執行的任務數
  strategy: dependency-aware   # dependency-aware | sequential
  conflict_resolution: serialize  # serialize | abort
```

### D.8 自訂模型定義（Custom Model Definitions）

GSD Pi v1.0 新增 `models.json` 設定檔，可定義自訂模型，特別適用於 Ollama 或企業私有 LLM：

```json
// ~/.gsd/models.json
{
  "models": [
    {
      "id": "qwen2.5-coder:32b",
      "provider": "ollama",
      "displayName": "Qwen 2.5 Coder 32B",
      "contextWindow": 32768,
      "maxOutputTokens": 8192,
      "capabilities": ["code", "chat"],
      "costPer1kInput": 0,
      "costPer1kOutput": 0
    },
    {
      "id": "deepseek-coder-v2",
      "provider": "ollama",
      "displayName": "DeepSeek Coder V2",
      "contextWindow": 128000,
      "maxOutputTokens": 8192,
      "capabilities": ["code", "chat"],
      "costPer1kInput": 0,
      "costPer1kOutput": 0
    }
  ]
}
```

定義後即可在 `PREFERENCES.md` 中使用自訂模型 ID。

### D.9 其他設定

```yaml
service_tier: default          # default | flex（低優先低價）
unique_milestone_ids: true     # Milestone ID 附加隨機後綴
auto_supervisor:
  hard_timeout_minutes: 30     # 單任務最長執行時間
skill_discovery: suggest       # auto | suggest | off
always_use_skills:             # 始終載入的技能
  - java-spring-boot
fetchAllowedUrls:              # 允許存取的 URL Pattern
  - "https://docs.company.com/*"
  - "https://api.company.com/*"
```

---

## 附錄 E：環境變數一覽

| 環境變數 | 說明 | 預設值 |
|----------|------|--------|
| `GSD_HOME` | GSD 全域資料目錄 | `~/.gsd` |
| `GSD_PROJECT_ID` | 專案唯一識別碼 | 自動產生 |
| `GSD_STATE_DIR` | 狀態資料目錄 | `.gsd/` |
| `GSD_CODING_AGENT_DIR` | Agent 工作目錄 | 自動設定 |
| `GSD_RTK_DISABLED` | 停用 RTK（Runtime Toolkit） | `false` |
| `GSD_ALLOWED_COMMAND_PREFIXES` | 允許執行的命令前綴（安全限制） | 無限制 |
| `GSD_FETCH_ALLOWED_URLS` | 允許 Fetch 的 URL Pattern | 全部允許 |
| `PI_TOKEN_TELEMETRY` | 啟用 Token Telemetry 詳細追蹤 | `false` |
| `HTTP_PROXY` | HTTP Proxy 設定 | 無 |
| `HTTPS_PROXY` | HTTPS Proxy 設定 | 無 |
| `NO_PROXY` | 不使用 Proxy 的域名 | 無 |
| `ANTHROPIC_API_KEY` | Anthropic API Key | 無 |
| `OPENAI_API_KEY` | OpenAI API Key | 無 |
| `GOOGLE_API_KEY` | Google API Key | 無 |

---

> **文件維護說明**：本教學手冊基於 GSD Pi v1.0.2（原 GSD-2）撰寫。專案已從 `gsd-build/gsd-2` 遷移至 `open-gsd/gsd-pi`。GSD Pi 更新頻繁，建議定期對照[官方 Changelog](https://github.com/open-gsd/gsd-pi/blob/main/CHANGELOG.md) 更新內容。執行 `npm update -g @opengsd/gsd-pi` 可隨時升級到最新版本。

