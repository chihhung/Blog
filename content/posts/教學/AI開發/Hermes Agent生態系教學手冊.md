+++
date = '2026-05-31T10:00:00+08:00'
draft = false
title = 'Hermes Agent生態系教學手冊'
tags = ['教學', 'AI開發','指引']
categories = ['教學']
+++

# Hermes Agent 生態系教學手冊（Enterprise Edition）

> **版本**：v0.15.2（v2026.5.29 — 涵蓋 The Foundation Release + The Velocity Release）  
> **適用對象**：資深工程師 / 架構師 / DevOps 團隊  
> **授權**：MIT License  
> **官方網站**：[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)  
> **GitHub**：[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)  
> **官方文件**：[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)  
> **Skills Hub**：[agentskills.io](https://agentskills.io/)  
> **LLM 友善文件**：[llms.txt](https://hermes-agent.nousresearch.com/docs/assets/files/llms-bcf65f79b33e57e6c0cce5b9627945d4.txt) / [llms-full.txt](https://hermes-agent.nousresearch.com/docs/assets/files/llms-full-5976b0eaaf4d9bbfcc2463097a4f7e13.txt)  
> **最後更新**：2026 年 6 月 1 日

---

## 📑 目錄

- [第一章：Hermes Agent 概述](#第一章hermes-agent-概述)
  - [1.1 技術背景與發展](#11-技術背景與發展)
  - [1.2 與傳統 AI 的差異](#12-與傳統-ai-的差異)
  - [1.3 Agent vs Workflow vs RPA 比較](#13-agent-vs-workflow-vs-rpa-比較)
  - [1.4 核心設計理念](#14-核心設計理念)
    - [1.4.1 Learning Loop（學習迴圈）](#141-learning-loop學習迴圈)
    - [1.4.2 Skill System（技能系統）](#142-skill-system技能系統)
    - [1.4.3 Persistent Memory（持久記憶）](#143-persistent-memory持久記憶)
    - [1.4.4 Model Agnostic（模型無關）](#144-model-agnostic模型無關)
    - [1.4.5 Voice Mode（語音模式）](#145-voice-mode語音模式)
    - [1.4.6 Web Dashboard（v0.9.0+）](#146-web-dashboardv090)
    - [1.4.7 Transport 架構（v0.11.0+）](#147-transport-架構v0110)
    - [1.4.8 Autonomous Curator（v0.12.0+）](#148-autonomous-curatorv0120)
    - [1.4.9 Multi-agent Kanban（v0.13.0+）](#149-multi-agent-kanbanv0130)
    - [1.4.10 Persistent Goals（v0.13.0+）](#1410-persistent-goalsv0130)
    - [1.4.11 Post-write Delta Lint（v0.13.0+）](#1411-post-write-delta-lintv0130)
    - [1.4.12 i18n 多語言支援（v0.13.0+）](#1412-i18n-多語言支援v0130)
    - [1.4.13 hermes proxy — OpenAI 相容本地代理（v0.14.0+）](#1413-hermes-proxy--openai-相容本地代理v0140)
    - [1.4.14 PyPI 套件安裝（v0.14.0+）](#1414-pypi-套件安裝v0140)
    - [1.4.15 /handoff 即時 Session 轉移（v0.14.0+）](#1415-handoff-即時-session-轉移v0140)
    - [1.4.16 Promptware 防禦（v0.15.0+）](#1416-promptware-防禦v0150)
    - [1.4.17 Bitwarden Secrets Manager（v0.15.0+）](#1417-bitwarden-secrets-managerv0150)
    - [1.4.18 Skill Bundles（v0.15.0+）](#1418-skill-bundlesv0150)
- [第二章：整體系統架構](#第二章整體系統架構)
  - [2.1 架構設計概述](#21-架構設計概述)
  - [2.2 分層架構圖](#22-分層架構圖)
  - [2.3 各層級說明](#23-各層級說明)
  - [2.4 多 Agent 協作架構](#24-多-agent-協作架構)
  - [2.5 高可用與擴展性設計](#25-高可用與擴展性設計)
- [第三章：Hermes Agent 核心機制解析](#第三章hermes-agent-核心機制解析)
  - [3.1 Learning Loop（學習迴圈）](#31-learning-loop學習迴圈)
  - [3.2 Skill System（技能系統）](#32-skill-system技能系統)
  - [3.3 Memory System（記憶系統）](#33-memory-system記憶系統)
  - [3.4 Planning / Execution Flow](#34-planning--execution-flow)
  - [3.5 Tool Calling 機制](#35-tool-calling-機制)
  - [3.6 Model Routing（多模型切換）](#36-model-routing多模型切換)
  - [3.7 Autonomous Curator（自動技能維護）](#37-autonomous-curator自動技能維護)
  - [3.8 Persistent Goals 與 Ralph Loop](#38-persistent-goals-與-ralph-loop)
  - [3.9 Post-write Delta Lint（自動語法檢查）](#39-post-write-delta-lint自動語法檢查)
  - [3.10 Checkpoints v2（狀態持久化）](#310-checkpoints-v2狀態持久化)
- [第四章：安裝與環境建置](#第四章安裝與環境建置)
  - [4.1 系統需求](#41-系統需求)
  - [4.2 快速安裝（Linux / macOS / WSL2）](#42-快速安裝linux--macos--wsl2)
  - [4.3 Native Windows 安裝（Early Beta）](#43-native-windows-安裝early-beta)
  - [4.4 Docker / Podman 部署](#44-docker--podman-部署)
  - [4.5 Nix Flake 安裝](#45-nix-flake-安裝)
  - [4.6 設定 API Key](#46-設定-api-key)
  - [4.7 設定檔說明](#47-設定檔說明)
- [第五章：快速開始（Quick Start）](#第五章快速開始quick-start)
  - [5.1 第一次對話](#51-第一次對話)
  - [5.2 建立 AI Coding Agent](#52-建立-ai-coding-agent)
  - [5.3 設定 Memory](#53-設定-memory)
  - [5.4 設定 Tools](#54-設定-tools)
  - [5.5 執行任務範例](#55-執行任務範例)
- [第六章：進階開發（企業級）](#第六章進階開發企業級)
  - [6.1 自訂 Skill（技能封裝）](#61-自訂-skill技能封裝)
  - [6.2 多 Agent 協作設計](#62-多-agent-協作設計)
  - [6.3 Multi-agent Kanban 實戰](#63-multi-agent-kanban-實戰)
  - [6.4 長期記憶設計（Vector DB）](#64-長期記憶設計vector-db)
  - [6.5 任務拆解（Task Decomposition）](#65-任務拆解task-decomposition)
  - [6.6 Workflow Orchestration](#66-workflow-orchestration)
  - [6.7 SOUL.md 與 Personality 系統](#67-soulmd-與-personality-系統)
  - [6.8 Context Files（專案上下文檔案）](#68-context-files專案上下文檔案)
  - [6.9 Plugin 系統（v0.12.0+ / v0.13.0 擴充）](#69-plugin-系統v0120--v0130-擴充)
- [第七章：Voice Mode（語音模式）](#第七章voice-mode語音模式)
  - [7.1 語音模式概述](#71-語音模式概述)
  - [7.2 支援的 STT / TTS 提供者](#72-支援的-stt--tts-提供者)
  - [7.3 CLI 語音互動](#73-cli-語音互動)
  - [7.4 Telegram / Discord 語音互動](#74-telegram--discord-語音互動)
  - [7.5 Discord Voice Channel 即時語音](#75-discord-voice-channel-即時語音)
  - [7.6 企業語音整合建議](#76-企業語音整合建議)
- [第八章：Web Application 整合](#第八章web-application-整合)
  - [8.1 整合架構設計](#81-整合架構設計)
  - [8.2 FastAPI 後端整合](#82-fastapi-後端整合)
  - [8.3 Spring Boot 後端整合](#83-spring-boot-後端整合)
  - [8.4 前端整合（Vue / React）](#84-前端整合vue--react)
  - [8.5 Agent-as-a-Service API 設計](#85-agent-as-a-service-api-設計)
- [第九章：企業級最佳實踐](#第九章企業級最佳實踐)
  - [9.1 安全性設計](#91-安全性設計)
  - [9.1.4 安全強化（v0.5.0 — v0.13.0 持續強化）](#914-安全強化v050--v0130-持續強化)
  - [9.2 成本控制](#92-成本控制)
  - [9.3 效能優化](#93-效能優化)
  - [9.4 Logging / Monitoring](#94-logging--monitoring)
  - [9.5 錯誤處理與重試機制](#95-錯誤處理與重試機制)
  - [9.6 Tips & Best Practices](#96-tips--best-practices)
- [第十章：部署與維運（DevOps）](#第十章部署與維運devops)
  - [10.1 Docker 部署](#101-docker-部署)
  - [10.2 Kubernetes 部署](#102-kubernetes-部署)
  - [10.3 CI/CD 流程](#103-cicd-流程)
  - [10.4 滾動升級](#104-滾動升級)
  - [10.5 災難復原（DR）](#105-災難復原dr)
- [第十一章：升級與版本管理](#第十一章升級與版本管理)
  - [11.1 升級策略](#111-升級策略)
  - [11.1.6 v0.13.0 升級特別注意事項](#1116-v0130-升級特別注意事項)
  - [11.2 相容性管理](#112-相容性管理)
  - [11.3 Migration 設計](#113-migration-設計)
- [第十二章：實戰案例](#第十二章實戰案例)
  - [12.1 AI Coding Agent](#121-ai-coding-agent)
  - [12.2 智慧客服 Agent](#122-智慧客服-agent)
  - [12.3 銀行流程自動化 Agent](#123-銀行流程自動化-agent)
  - [12.4 多媒體創作 Agent](#124-多媒體創作-agent)
- [第十三章：常見問題（FAQ）](#第十三章常見問題faq)
- [附錄 A：檢查清單（Checklist）](#附錄-a檢查清單checklist)
- [附錄 B：指令速查表](#附錄-b指令速查表)
- [附錄 C：環境變數參考](#附錄-c環境變數參考)
- [附錄 D：Provider 完整清單](#附錄-dprovider-完整清單)

---

## 第一章：Hermes Agent 概述

### 1.1 技術背景與發展

Hermes Agent 是由 **Nous Research** 開發的開源自我改進 AI Agent。Nous Research 是知名的 AI 研究實驗室，以訓練 Hermes、Nomos、Psyche 等開源模型聞名。

**發展歷程**：

| 版本 | 日期 | 重要里程碑 |
|------|------|------------|
| v0.1.0 | 2026.02 | 初始開源發佈，核心 Agent Loop 與 Learning Loop |
| v0.2.0 | 2026.03.12 | 多平台 Gateway（Telegram/Discord/Slack/WhatsApp/Signal/Email/Home Assistant）、MCP Client、Skills 生態系、CLI 皮膚引擎、3,289 測試 |
| v0.3.0 | 2026.03.17 | 統一串流架構、Plugin 系統、Native Anthropic Provider、Voice Mode、ACP IDE 整合、Smart Approvals |
| v0.4.0 | 2026.03.23 | OpenAI-compatible API Server、6 新通訊平台（Signal/DingTalk/SMS/Mattermost/Matrix/Webhook）、MCP OAuth 2.1、@ 上下文參考、Gateway Prompt Caching |
| v0.5.0 | 2026.03.28 | Hugging Face Provider、Nix Flake、供應鏈安全強化（移除 litellm）、Plugin Lifecycle Hooks、Telegram Private Chat Topics |
| v0.6.0 | 2026.03.30 | Profiles 多實例隔離、MCP Server Mode、Docker 容器、Fallback Provider Chain、Feishu/WeCom 平台 |
| v0.7.0 | 2026.04.03 | Pluggable Memory Provider、Credential Pool 輪替、Camofox 反偵測瀏覽器、Inline Diff Preview、Secret Exfiltration Blocking |
| v0.8.0 | 2026.04.08 | 背景任務自動通知、Live Model Switching、Google AI Studio（Gemini）、Smart Inactivity Timeout、MCP OAuth 2.1 PKCE、209 PRs |
| v0.9.0 | 2026.04.13 | **Web Dashboard**、Fast Mode（`/fast`）、iMessage（BlueBubbles）、WeChat/WeCom Callback、Termux/Android 支援、`hermes backup/import`、16 平台、487 commits |
| v0.10.0 | 2026.04.16 | **Nous Tool Gateway**（付費訂閱用戶自動取得 Web Search/Image Gen/TTS/Browser 工具，零額外 API Key） |
| v0.11.0 | 2026.04.23 | **Ink TUI 全面重寫**、Transport ABC 架構、Native AWS Bedrock、5 新推理路徑（NVIDIA NIM/Arcee AI/Step Plan/Gemini CLI OAuth/Vercel AI Gateway）、GPT-5.5 via Codex OAuth、QQBot（第 17 平台）、Plugin 大幅擴展、`/steer` 中途導引、Shell Hooks、Orchestrator 子代理、1,556 commits |
| v0.12.0 | 2026.04.30 | **Autonomous Curator**（自動技能維護 Agent）、Self-improvement Loop 大幅升級（rubric-based）、5 新 Provider（LM Studio / GMI Cloud / Azure AI Foundry / MiniMax OAuth / Tencent Tokenhub）、Pluggable Gateway Platforms、Microsoft Teams（第 19 平台）、Tencent 元宝（第 18 平台）、Spotify 原生整合（7 工具 + PKCE OAuth）、Google Meet Plugin、ComfyUI v5 內建、Piper 本地 TTS、`hermes -z` 單次模式、Models Dashboard Tab、Remote Model Catalog、Cold-start 效能提升 ~57%、Langfuse 可觀測性 Plugin、1,096 commits |
| v0.13.0 | 2026.05.07 | **Multi-agent Kanban**（持久多 Agent 協作看板：心跳 / 回收 / 殭屍偵測 / 重試預算 / 幻覺閘門）、**`/goal`**（跨回合持久目標 — Ralph Loop）、**`video_analyze`** 原生影片理解工具、**xAI Custom Voices** 語音克隆 TTS、**Google Chat**（第 20 平台）+ 通用平台 Plugin Hooks、**Sessions 自動恢復**（Gateway 重啟後對話復原）、**8 項 P0 安全修正**（Secret Redaction 預設開啟、Discord 角色白名單 Guild 隔離 CVSS 8.1、WhatsApp 預設拒絕陌生人、TOCTOU 修正）、**Checkpoints v2**（狀態持久化重寫 + 真正修剪 + 磁碟護欄）、**Post-write Delta Lint**（write_file + patch 後自動 lint：Python/JSON/YAML/TOML）、**`no_agent` Cron 模式**（純腳本看門狗）、**Platform Allowlists**（`allowed_channels/chats/rooms` 全平台）、**ProviderProfile ABC**（Provider 可插拔化）、**API Server `X-Hermes-Session-Key`**（記憶 Session 隔離）、**MCP SSE Transport + OAuth 轉發**、**Curator 新子指令**（`archive` / `prune` / `list-archived` / 同步 `run`）、**ACP `/steer` + `/queue`**（VS Code/Zed/JetBrains）、**Dashboard 升級**（Plugins 頁 / Profiles 頁 / 可排序分析表 / 反向代理 `X-Forwarded-Prefix` / `default-large` 18px 主題）、**SearXNG 原生搜尋後端** + 分離式 Web 工具（搜尋/擷取/瀏覽各自選擇後端）、**OpenRouter Response Caching**、**`[[as_document]]` Skill 媒體路由指令**、**`transform_llm_output` Plugin Hook**、**7 語言 i18n**（中/日/德/西/法/烏/土）、**Native Windows 早期測試版**（PowerShell 安裝腳本）、**6 新 Optional Skills**（Shopify / here.now / shop-app / Anthropic 金融服務 / kanban-video-orchestrator / searxng-search）、新模型（DeepSeek v4 Pro / Grok 4.3 / Owl Alpha / tencent hy3-preview / Arcee Trinity Large Thinking）、**100 新 CLI 啟動提示**、864 commits / 588 PR / 295 貢獻者 |
| v0.14.0 | 2026.05.16 | **The Foundation Release**：**xAI Grok via SuperGrok OAuth**（grok-4.3 升至 1M context window）、**`hermes proxy`**（OpenAI 相容本地代理，一個訂閱所有工具可用：Codex/Aider/Cline/Continue）、**`x_search`** 第一級 X (Twitter) 搜尋工具、**Microsoft Teams 端到端整合**（Graph auth + webhook + pipeline + outbound）、**去臃腫化浪潮**（lazy install 大幅減少安裝體積）、**`pip install hermes-agent`**（PyPI 正式套件）、**跨 Session 1 小時 Claude Prompt Cache**、**180 倍 `browser_console` 效能提升**（持久 CDP 連線）、**冷啟動效能浪潮**（啟動快 ~19 秒）、**LINE + SimpleX Chat**（第 21、22 平台）、**`/handoff`** 即時 Session 轉移（跨模型/Profile 零掉落）、**`clarify` 原生按鈕 UI**（Telegram/Discord）、**Discord 頻道歷史回填**、**`vision_analyze` 原生像素傳遞**（Vision 模型直接看圖）、**Per-turn 檔案變更驗證 Footer**、**LSP 語義診斷**（write_file/patch 後真實語言伺服器分析）、**統一 `video_generate` 可插拔後端**、**`computer_use` cua-driver 後端**（非 Anthropic 模型也可驅動桌面）、**可點擊 OSC8 URL**、**Zed ACP Registry**（`uvx` 一鍵安裝）、**OpenRouter Pareto Code Router**（`min_coding_score`）、**NovitaAI 新 Provider**、**Codex app-server Runtime**、**`huggingface/skills` 預設信任 Tap**、**9 新 Optional Skills**（Hyperliquid/Yahoo Finance/api-testing/EVM/darwinian-evolver/osint/pinggy-tunnel/watchers/Notion）、**`/subgoal`** 目標追加、**Alibaba Cloud → Qwen Cloud 更名**、**Native Windows Beta**（PowerShell installer + MinGit）、**16 語系 i18n**、**Brave Search + DDGS 免費搜尋**、**Sudo brute-force 阻擋**、**Plugin `ctx.llm` + `tool_override`**、808 commits / 633 PR / 215 貢獻者 |
| v0.15.0 | 2026.05.28 | **The Velocity Release**：**The Big Refactor** — `run_agent.py` 16,083 → 3,821 行（-76%），拆分為 14 個 `agent/*` 模組、**Kanban 成熟化浪潮**（104 PR：Swarm v1 拓撲、`hermes kanban swarm`、自動分解、per-task model override、排程任務、worktree-per-task、worker visibility endpoints、拖放刪除）、**冷啟動效能持續優化**（47% fewer per-turn function calls、`hermes --version` 快 63%、Termux 2.9s → 0.8s）、**`session_search` 重建**（無 LLM、免費、4,500 倍快速）、**Promptware 防禦**（Brainworm-class 攻擊阻擋：threat patterns + 記憶掃描 + tool-result delimiters）、**Bitwarden Secrets Manager**（一個 bootstrap token 取代所有 API Key）、**ntfy**（第 23 平台：自託管推播通知、零帳號）、**Skill Bundles**（`/<name>` 一次載入多個 Skills）、**TUI Session Orchestrator**（多活躍 Session 切換）、**Krea 2 Medium + Large 圖片生成**、**FAL 移至 Plugin 架構**、**Nous 核准 MCP 目錄**（互動式 picker + 一鍵安裝）、**OpenHands 協作技能**（delegate 至 OpenHands CLI）、**深度 xAI 整合**（Web Search plugin、`hermes proxy` xAI 上游、May 15 模型退役偵測 + `hermes migrate xai`、`auto_speech_tags` 自然 TTS、`base_url` 洩漏防護）、**s6-overlay Docker 容器監督**（systemd/launchd/Windows/s6 後端 + per-profile gateway 監督）、**Session Control API**（`/api/sessions/*` REST + SSE）、**mTLS MCP 支援**、**OpenAI API 作為獨立 Provider**、**Microsoft Entra ID auth for Azure Foundry**、**OpenRouter sticky routing**（`session_id`）、**移除 Vercel AI Gateway 與 Vercel Sandbox**、**3 新 Skills**（code-wiki / openhands / web-pentest）、**Plugin 新 Hooks**（`register_tts_provider` / `register_transcription_provider` / `register_auxiliary_task`）、**bundled `security-guidance` plugin**、**`hermes audit`** OSV.dev 供應鏈審計、**`hermes send`** 腳本輸出推送任何平台、1,302 commits / 747 PR / 321 貢獻者 |
| v0.15.1 | 2026.05.29 | **Hotfix**：Dashboard 401 reload loop 修正（loopback 模式）、Docker `--insecure` 改為顯式 env opt-in、MCP bare command Docker 相容、Skills Hub 完整目錄（858 → 19,932 entries）、Kanban worker SIGTERM 修正、`/yolo` mid-session bypass、gateway probe stepdown safety、web URL redaction passthrough、21 PR / 9 貢獻者 |
| v0.15.2 | 2026.05.29 | 追加修正（v0.15.1 同日發佈） |

**核心數據**（截至 2026.06.01）：

- GitHub Stars：**174,000+**
- Contributors：**1,282+**
- Forks：**29,600+**
- 主要語言：**Python 89.1%**、TypeScript 8.1%
- 授權：**MIT License**（可商用）
- 累計 Releases：**16 個**（v0.1.0 — v0.15.2）

### 1.2 與傳統 AI 的差異

```mermaid
graph LR
    subgraph "傳統 AI（ChatGPT 等）"
        A[使用者輸入] --> B[單次推理]
        B --> C[回應輸出]
        C --> D[無學習/無記憶]
    end
    
    subgraph "Hermes Agent"
        E[使用者輸入] --> F[規劃 Planning]
        F --> G[執行 Execution]
        G --> H[學習 Learning]
        H --> I[技能累積 Skill]
        I --> J[長期記憶 Memory]
        J --> F
    end
```

| 特性 | 傳統 AI（ChatGPT） | Hermes Agent |
|------|---------------------|--------------|
| 記憶 | 僅單次對話 | 跨對話長期記憶（FTS5 + Vector DB）+ Session Key 隔離 |
| 學習 | 不會學習 | 內建 Learning Loop，自動封裝技能 + Autonomous Curator |
| 工具使用 | 有限（Plugins/GPTs） | 70+ 內建工具 + MCP 擴展（SSE Transport + OAuth 轉發） |
| 執行環境 | 雲端沙箱 | 本地 / Docker / SSH / Modal / Daytona / Singularity（6 種後端） |
| 多平台 | Web UI 為主 | CLI + TUI + 23+ 通訊平台（Telegram/Discord/Slack/Matrix/WhatsApp/Signal/Email/SMS/DingTalk/Feishu/WeCom/WeChat/BlueBubbles/Mattermost/Home Assistant/QQBot/Yuanbao/Microsoft Teams/Google Chat/LINE/SimpleX Chat/ntfy/Webhook 等） |
| 語音 | 有限 | Voice Mode（STT + TTS）支援 CLI / Telegram / Discord / Discord VC + xAI 語音克隆 |
| 模型綁定 | 固定 | 任意 OpenAI-compatible（200+ 模型）+ Provider 可插拔 ABC |
| 多 Agent | 無原生支援 | Multi-agent Kanban 持久協作看板（心跳 / 回收 / 殭屍偵測） |
| 持久目標 | 僅單輪指令 | `/goal` 跨回合持久目標（Ralph Loop） |
| 國際化 | 僅介面語言 | 16 語系 i18n（中/日/德/西/法/烏/土/韓/義/葡 等） |
| 授權 | 閉源 | MIT（可商用） |
| 成本 | 按月訂閱 | 自控（用多少付多少 Token） |
| Windows 支援 | 原生 | Native Windows Beta（PowerShell installer + MinGit）+ WSL2 完整支援 |
| Promptware 防禦 | 無 | Brainworm-class 攻擊阻擋（threat patterns + memory scan + tool-result delimiters） |
| 秘密管理 | 手動設定 | Bitwarden Secrets Manager（一個 bootstrap token 取代所有 API Key） |
| Session 轉移 | 不支援 | `/handoff` 即時 Session 轉移（跨模型/Profile 零掉落） |

### 1.3 Agent vs Workflow vs RPA 比較

| 維度 | AI Agent（Hermes） | Workflow（Airflow 等） | RPA（UiPath 等） |
|------|-------------------|----------------------|------------------|
| 決策能力 | 自主決策 + 學習 | 人工定義流程 | 人工錄製腳本 |
| 適應性 | 高（動態調整） | 低（靜態 DAG） | 低（固定腳本） |
| 學習能力 | 從經驗中學習 | 無 | 無 |
| 處理非結構化任務 | 擅長 | 不擅長 | 不擅長 |
| 開發效率 | 自然語言描述任務 | 需要寫 DAG 程式 | 需要錄製/寫腳本 |
| 成本 | Token 為主 | 伺服器資源 | License + 伺服器 |
| 最佳用途 | 複雜、多步驟、需要判斷的任務 | 固定批次流程 | 重複性 UI 操作 |

### 1.4 核心設計理念

Hermes Agent 的核心設計理念可歸納為四大支柱：

#### 1.4.1 Learning Loop（學習迴圈）

Agent 在完成複雜任務時，會自動分析過程、提取經驗，並封裝為可重用的 Skill。下次遇到類似問題時，Agent 會自動調用已學會的技能，效率逐步提升。

#### 1.4.2 Skill System（技能系統）

- 技能以 Markdown 格式存儲，可讀可編輯
- 支援社群共享（[agentskills.io](https://agentskills.io/)）
- 技能在使用過程中自我改進
- 與 Claude Code Skill 標準兼容

#### 1.4.3 Persistent Memory（持久記憶）

- 短期記憶：當前對話上下文
- 長期記憶：跨對話持久記憶（MEMORY.md / USER.md）
- 使用者建模：透過 Honcho 辯證式使用者理解
- 多種記憶後端：內建、mem0、Supermemory、Honcho、Hindsight 等

#### 1.4.4 Model Agnostic（模型無關）

- 支援 OpenAI（含 GPT-5.5 via Codex OAuth、**OpenAI API 獨立 Provider**）、Anthropic、Google AI Studio（Gemini）、OpenRouter（200+ 模型）
- Nous Portal、z.ai/GLM、Kimi/Moonshot、MiniMax、Qwen Cloud（原 Alibaba Cloud 更名）、xAI（Grok — **SuperGrok OAuth**、grok-4.3 1M context window）、Ollama
- NVIDIA NIM（Nemotron）、Arcee AI、Hugging Face、GMI Cloud、Xiaomi MiMo、DeepSeek
- AWS Bedrock（Native Converse API）、**NovitaAI**（v0.14.0）
- **`hermes proxy`**（v0.14.0）：OpenAI 相容本地代理，一個訂閱讓所有 Agent 工具（Codex/Aider/Cline/Continue）可用
- 任何 OpenAI-compatible API 端點
- 即時切換模型 `/model` 指令，無需修改程式碼
- xAI (Grok) 支援 Prompt Caching、**跨 Session 1 小時 Claude Prompt Cache**（v0.14.0）
- Fast Mode（`/fast`）：OpenAI Priority Processing + Anthropic Fast Tier
- **v0.14.0 新增**：OpenRouter Pareto Code Router（`min_coding_score`）、Codex app-server Runtime
- **v0.15.0 新增**：Microsoft Entra ID auth for Azure Foundry、OpenRouter sticky routing（`session_id`）
- **v0.13.0 Provider 可插拔化**：`ProviderProfile` ABC + `plugins/model-providers/`，第三方 Provider 無需修改核心程式碼即可接入
- **Nous OAuth 跨 Profile 持久化**：共享 Token Store，一次登入所有 Profile 共享 Session
- **Nous Portal 一鍵設定**（v0.15.0）：`hermes setup --portal` 快速引導
- **OpenRouter Response Caching**：顯式快取控制
- **Brave Search + DDGS 免費搜尋**（v0.14.0）：免費 Web Search 後端

> **注意**：v0.15.0 起 **移除 Vercel AI Gateway 與 Vercel Sandbox** — 如有使用請遷移至其他 Provider/Terminal Backend。

#### 1.4.5 Voice Mode（語音模式）

v0.3.0 起新增完整語音互動能力：
- **CLI Voice Mode**：在終端中即時語音對話
- **Telegram / Discord**：語音備忘錄自動轉文字
- **Discord Voice Channel**：即時語音通話
- 支援多種 STT/TTS 提供者：OpenAI TTS/Whisper、ElevenLabs、MiniMax Speech 2.8、Voxtral Transcribe（Mistral AI）
- **Piper TTS**（v0.12.0）：完全離線本地 TTS
- **xAI Custom Voices**（v0.13.0）：語音克隆（voice cloning）TTS 提供者
- **xAI `auto_speech_tags` 自然 TTS**（v0.15.0）：更自然的語音合成
- **Plugin TTS/Transcription Hooks**（v0.15.0）：`register_tts_provider` / `register_transcription_provider` 讓 Plugin 可註冊自訂語音後端

#### 1.4.6 Web Dashboard（v0.9.0+）

v0.9.0 新增本地 Web Dashboard，可透過瀏覽器管理 Hermes Agent：
- **設定管理**：圖形化設定 Provider、Model、Tools
- **Session 瀏覽**：查看與搜尋所有對話歷史
- **Skills 管理**：瀏覽、安裝、啟用/停用技能
- **Gateway 監控**：管理訊息平台連線狀態
- **Plugin 擴展**（v0.11.0）：第三方 Plugin 可新增自訂 Tab、Widget
- **Models Tab**（v0.12.0）：豐富的每模型分析、從瀏覽器切換主模型 / 輔助模型
- **Dashboard Chat Tab**（v0.12.0）：xterm.js + JSON-RPC sidecar，可在瀏覽器中直接使用 CLI
- **Plugins 頁面**（v0.13.0）：管理、啟用/停用、查看認證狀態
- **Profiles 管理頁面**（v0.13.0）：多 Profile 統一管理
- **可排序分析表格**（v0.13.0）：互動式欄位排序
- **`default-large` 主題**（v0.13.0）：18px 基礎字體大小
- **反向代理支援**（v0.13.0）：透過 `X-Forwarded-Prefix` 支援 URL 前綴部署
- **Docker 啟動**（v0.13.0）：`HERMES_DASHBOARD=1` 環境變數可在 Docker 中啟動 Dashboard 為 Side-process
- **i18n 支援**：英文 + 中文 + 土耳其文介面、行動裝置響應式設計
- **TUI Session Orchestrator**（v0.15.0）：多活躍 Session 在同一視窗切換管理
- **Session Control API**（v0.15.0）：`/api/sessions/*` REST + SSE 端點，程式化控制 Session 生命週期

#### 1.4.7 Transport 架構（v0.11.0+）

v0.11.0 引入可插拔的 Transport 抽象層，將格式轉換與 HTTP 傳輸從 Agent Core 解耦：
- **AnthropicTransport**：Anthropic Messages API
- **ChatCompletionsTransport**：OpenAI-compatible 預設路徑
- **ResponsesApiTransport**：OpenAI Responses API + Codex
- **BedrockTransport**：AWS Bedrock Converse API

#### 1.4.8 Autonomous Curator（v0.12.0+）

v0.12.0 新增自動化技能維護 Agent，可自主管理技能庫：
- **背景執行**：透過 Gateway 的 Cron Ticker 運行，預設每 7 天執行一次
- **技能評分**：自動評估每個 Skill 的品質與使用頻率
- **合併與清理**：合併重複技能、清理長期未使用的技能
- **報告產出**：每次執行產生 `logs/curator/run.json` + `REPORT.md`
- **安全防護**：bundled / hub skills 受防護不會被修改，pinned skills 也不會被 curator 變更
- **狀態查詢**：`hermes curator status` 依使用頻率排名技能（most-used / least-used）
- **統一設定**：透過 `auxiliary.curator` 配置，可從 Dashboard 管理
- **新子指令**（v0.13.0）：`hermes curator archive`（歸檔）、`hermes curator prune`（修剪）、`hermes curator list-archived`（列出已歸檔）
- **同步執行**（v0.13.0）：手動 `hermes curator run` 現為同步模式，即時回傳結果無需輪詢

#### 1.4.9 Multi-agent Kanban（v0.13.0+）

v0.13.0 引入持久化多 Agent 協作看板系統，v0.15.0 經歷 104 PR 成熟化浪潮，是企業級多 Agent 協作的核心架構：
- **持久看板**：durable multi-profile collaboration board，支援多專案看板（一次安裝，多個 Kanban）
- **Worker 生命週期管理**：心跳監測（heartbeat）、工作回收（reclaim）、殭屍偵測（zombie detection）、自動阻擋未完成退出的 Worker
- **可靠性保障**：每任務 `max_retries` 覆寫、統一的失敗計數器（spawn/timeout/crash）
- **幻覺閘門**：hallucination gate + recovery UX，防止 Worker 聲稱完成了未建立的任務卡
- **Swarm v1 拓撲**（v0.15.0）：`hermes kanban swarm` 指令，Orchestrator 自動分解目標為子任務
- **Per-task Model Override**（v0.15.0）：每個任務可指定不同模型
- **排程任務**（v0.15.0）：支援 scheduled task 排程執行
- **Worktree-per-task**（v0.15.0）：每個任務使用獨立 Git worktree，避免衝突
- **Worker Visibility Endpoints**（v0.15.0）：即時查看 Worker 狀態
- **Dashboard 整合**：Kanban Dashboard 含工作區種類/路徑輸入、每平台 Home-channel 通知切換、任務拖放→執行
- **跨 Profile 共享**：看板、工作區、Worker 日誌可跨 Profile 分享
- **通用診斷引擎**：任務痛苦信號（distress signals）的通用診斷機制
- **Worker 任務所有權**：對破壞性工具呼叫強制驗證 Worker 任務所有權

```yaml
# config.yaml — Kanban 設定範例
kanban:
  enabled: true
  multi_project: true
  max_retries: 3
  heartbeat_interval: 30  # 秒
  zombie_timeout: 300     # 秒
  hallucination_gate: true
```

#### 1.4.10 Persistent Goals（v0.13.0+）

v0.13.0 引入 `/goal` 指令，讓 Agent 鎖定目標並跨回合追蹤完成度（Ralph Loop）：
- **跨回合持久**：目標不會因對話分頁或 Session 邊界而遺失
- **目標 Turn Budget**：可設定目標允許的最大回合數
- **Ralph Loop**：以 Agent-as-action-item 概念將學習迴圈提升為一級原語（first-class primitive）

```bash
# 使用 /goal 設定持久目標
> /goal 重構所有 API endpoints 為 RESTful 風格，並撰寫完整測試

# Agent 會持續追蹤進度，跨回合記錄
# 即使中途切換話題，/goal 會在每次對話開始時提醒目標進度
```

#### 1.4.11 Post-write Delta Lint（v0.13.0+）

v0.13.0 為 `write_file` 和 `patch` 工具新增自動語法檢查，v0.14.0 升級為完整 LSP 語義診斷：
- **支援語言**：Python、JSON、YAML、TOML（v0.13.0 基礎），**v0.14.0 起支援任何安裝了 Language Server 的語言**（LSP 語義診斷）
- **增量檢查**：僅檢查變更的部分（delta），效能影響極小
- **即時回饋**：語法錯誤立即顯示在工具輸出中，Agent 可自動修正

#### 1.4.12 i18n 多語言支援（v0.13.0+）

v0.13.0 起引入 i18n，v0.14.0 擴展至 **16 語系**：
- **支援語言**：中文（zh）、日文（ja）、德文（de）、西班牙文（es）、法文（fr）、烏克蘭文（uk）、土耳其文（tr）、韓文（ko）、義大利文（it）、葡萄牙文（pt）等共 16 語系
- **設定方式**：`display.language` 配置項
- **文件站**：Docs 站新增中文簡體（zh-Hans）語言環境

#### 1.4.13 `hermes proxy` — OpenAI 相容本地代理（v0.14.0+）

v0.14.0 新增 `hermes proxy` 子指令，讓 Hermes 充當 OpenAI-compatible 本地代理伺服器：
- **一個訂閱，所有工具可用**：透過 OAuth Provider（xAI SuperGrok、Codex 等）的授權，讓第三方 Agent 工具（Aider、Cline、Continue、Cursor）直接使用 Hermes 的 API Key
- **零成本跨工具整合**：無需為每個工具分別設定 API Key
- **安全隔離**：Proxy 在本地執行，API Key 不離開本機

```bash
# 啟動 hermes proxy
hermes proxy --port 4141

# 其他工具指向本地 proxy
export OPENAI_API_BASE=http://localhost:4141/v1
aider --model grok-4.3  # 使用 Hermes 的 xAI 授權
```

#### 1.4.14 PyPI 套件安裝（v0.14.0+）

v0.14.0 正式發佈 PyPI 套件，可透過 `pip` 直接安裝：

```bash
pip install hermes-agent
# 或使用 uv
uv tool install hermes-agent
```

#### 1.4.15 `/handoff` 即時 Session 轉移（v0.14.0+）

v0.14.0 新增 `/handoff` 指令，支援在不同模型或 Profile 之間即時轉移對話，不丟失上下文：
- **跨模型轉移**：從 Claude 切換到 GPT-5.5 時保留完整對話歷史
- **跨 Profile 轉移**：將任務從個人 Profile 無縫交接至團隊 Profile
- **零掉落保證**：Session 狀態完整遷移，不漏失任何資訊

```bash
# 將當前 session 轉移到新 Profile
> /handoff team-ops
# 或轉移到不同模型
> /handoff --model gpt-5.5
```

#### 1.4.16 Promptware 防禦（v0.15.0+）

v0.15.0 引入針對 Brainworm-class 攻擊的 Promptware 防禦機制：
- **Threat Patterns**：內建惡意 Prompt 模式偵測
- **記憶掃描**：載入長期記憶時自動掃描是否被注入惡意內容
- **Tool-result Delimiters**：工具結果使用加密分隔符，防止 Prompt Injection
- **bundled `security-guidance` Plugin**：預設啟用的安全指引 Plugin
- **`hermes audit`**：OSV.dev 供應鏈審計子指令

#### 1.4.17 Bitwarden Secrets Manager（v0.15.0+）

v0.15.0 整合 Bitwarden Secrets Manager，大幅簡化多 API Key 管理：
- **單一 Bootstrap Token**：一個 Bitwarden Machine Account token 取代所有散落的 API Key
- **集中式管理**：所有 Provider 的 API Key 統一在 Bitwarden 管理
- **自動同步**：啟動時自動從 Bitwarden 拉取最新密鑰

```yaml
# config.yaml — Bitwarden Secrets Manager 設定
secrets:
  backend: bitwarden
  bitwarden:
    machine_account_token: ${BWS_ACCESS_TOKEN}
```

#### 1.4.18 Skill Bundles（v0.15.0+）

v0.15.0 引入 Skill Bundles，一個指令載入多個相關技能：
- **語法**：`/<bundle-name>` 即可載入預定義的技能組合
- **自訂 Bundle**：可在 `skills/bundles/` 定義自己的 Bundle
- **預設 Bundles**：`/fullstack`、`/devops`、`/security` 等

> **實務案例**：某金融團隊將 Hermes Agent 部署在內部 VPS，使用 Anthropic Claude 作為主模型處理程式碼審查，搭配免費的 MiMo v2 Pro（Nous Portal）進行摘要與壓縮，Token 成本降低 60%。

---

## 第二章：整體系統架構

### 2.1 架構設計概述

Hermes Agent 採用分層架構設計，從前端展示層到底層資料層，每一層都具備可替換和可擴展的特性。以下是企業級部署時的完整架構設計。

### 2.2 分層架構圖

```mermaid
graph TB
    subgraph "Presentation Layer（展示層）"
        CLI[Terminal CLI<br/>TUI 界面（Ink 重寫）]
        TG[Telegram Bot]
        DC[Discord Bot]
        SK[Slack Bot]
        WA[WhatsApp]
        SG[Signal]
        MX[Matrix]
        MT[Mattermost]
        FS_P[Feishu / DingTalk / WeCom]
        WX[WeChat / iMessage]
        QQ[QQBot]
        YB[Yuanbao / Teams]
        GC[Google Chat]
        LN[LINE]
        SX[SimpleX Chat]
        NT[ntfy]
        EM[Email / SMS]
        HA[Home Assistant]
        WEB[Web API<br/>REST/SSE]
        DASH[Web Dashboard<br/>React SPA]
    end

    subgraph "API Gateway Layer（閘道層）"
        GW[Hermes Gateway<br/>消息路由 / 認證 / 限流]
        ACP[ACP Adapter<br/>VS Code / JetBrains / Zed]
    end

    subgraph "Agent Layer（代理層）"
        CORE[Agent Core<br/>Planning / Execution / Loop]
        SUB[Subagent Pool<br/>平行委派]
        SKILL[Skill Engine<br/>技能載入 / 自動建立]
        PLUG[Plugin System<br/>Honcho / Hindsight / RetainDB]
    end

    subgraph "Memory Layer（記憶層）"
        STM[Short-term Memory<br/>Context Window]
        LTM[Long-term Memory<br/>MEMORY.md / USER.md]
        FTS[FTS5 Session Search<br/>跨對話搜尋 + Trigram CJK]
        VDB[(Vector DB<br/>mem0 / Supermemory)]
        UDB[(User Model<br/>Honcho Dialectic)]
    end

    subgraph "Tool Layer（工具層）"
        TERM[Terminal Backends<br/>Local/Docker/SSH/Modal/Daytona/Singularity]
        BROW[Browser Engine<br/>Playwright / Camofox]
        FILE[File Tools<br/>讀寫/搜尋/壓縮]
        WEB_TOOL[Web Tools<br/>搜尋/擷取/Vision]
        MCP_T[MCP Servers<br/>外部工具擴展]
        CRON[Cron Scheduler<br/>排程自動化]
    end

    subgraph "Data Layer（資料層）"
        SQLITE[(SQLite<br/>Sessions / Config)]
        FS_D[(File System<br/>Skills / Memories)]
        EXT[(External APIs<br/>LLM Providers)]
    end

    CLI --> GW
    TG --> GW
    DC --> GW
    SK --> GW
    WA --> GW
    SG --> GW
    MX --> GW
    MT --> GW
    FS_P --> GW
    WX --> GW
    QQ --> GW
    YB --> GW
    GC --> GW
    LN --> GW
    SX --> GW
    NT --> GW
    EM --> GW
    HA --> GW
    WEB --> GW
    DASH --> GW
    ACP --> CORE

    GW --> CORE
    CORE --> SUB
    CORE --> SKILL
    CORE --> PLUG

    CORE --> STM
    CORE --> LTM
    CORE --> FTS
    PLUG --> VDB
    PLUG --> UDB

    CORE --> TERM
    CORE --> BROW
    CORE --> FILE
    CORE --> WEB_TOOL
    CORE --> MCP_T
    CORE --> CRON

    STM --> SQLITE
    LTM --> FS_D
    SKILL --> FS_D
    CORE --> EXT
```

### 2.3 各層級說明

#### 2.3.1 Presentation Layer（展示層）

| 組件 | 說明 | 連線方式 |
|------|------|----------|
| Terminal CLI / TUI | 完整 TUI（v0.11.0 Ink 重寫），支援多行編輯、斜線指令自動完成、串流工具輸出、OSC-52 剪貼簿、**LaTeX 渲染**（v0.12.0）、冷啟動提升 57% | 本地 stdin/stdout |
| Web Dashboard | React SPA 本地管理介面，設定/Session/Skills/Gateway 管理、Plugin 擴展 Tab | HTTP（localhost） |
| Telegram Bot | 群組/私訊/Forum Topic、語音轉文字、Emoji 審批按鈕、Webhook Mode | Telegram Bot API |
| Discord Bot | 原生 Slash Commands、頻道控制、Interactive Model Picker、Voice Channel | Discord Gateway |
| Slack Bot | Thread 自動回覆、mrkdwn 格式、互動審批按鈕、Multi-Workspace OAuth | Slack Events API |
| WhatsApp | 透過 WhatsApp Business API 對接 | Webhook |
| Signal | 全 MEDIA 標籤交付（圖片/語音/影片）| signal-cli |
| Matrix | Tier 1 支援：Reactions、Read Receipts、E2EE、Room Management、CJK 輸入 | Matrix Client |
| Mattermost | 檔案附件交付、訊息串接 | Mattermost API |
| Feishu（飛書）| 互動卡片審批按鈕、ACL 控制、自動重連 | Feishu Open API |
| DingTalk（釘釘）| 企業機器人整合 | DingTalk API |
| WeCom（企業微信）| 企業應用整合、Callback Mode | WeCom API |
| WeChat（微信）| Native WeChat via iLink Bot API、Streaming Cursor、Media Upload | WeChat API |
| BlueBubbles（iMessage）| macOS 原生 iMessage 整合、Auto-Webhook | BlueBubbles API |
| QQBot | QQ 官方 API v2、QR 掃碼設定、Streaming Cursor、DM/Group 管控 | QQ Official API |
| Email | 電子郵件收發整合 | SMTP/IMAP |
| SMS | 簡訊通知交付 | Twilio / SMS API |
| Home Assistant | 智慧家庭整合、語音助理 | Home Assistant API |
| Webhook | 通用 Webhook 接收/推送、Direct-Delivery Mode（v0.11.0） | HTTP Webhook |
| Web API | REST + SSE 串流，可做自訂前端 | HTTP/SSE |
| **Tencent 元寶** | 騰訊元寶平台整合（v0.12.0 第 18 平台） | Pluggable Gateway |
| **Microsoft Teams** | Teams 對話整合（v0.12.0 第 19 平台）、Sidebar + Threading + 群聊回退 | Pluggable Gateway |
| **Google Chat** | Google Chat 整合（v0.13.0 第 20 平台）+ 通用 `env_enablement_fn` / `cron_deliver_env_var` Platform-Plugin Hooks | Pluggable Gateway |
| **LINE** | LINE Messaging API 整合（v0.14.0 第 21 平台） | Pluggable Gateway |
| **SimpleX Chat** | SimpleX Chat 去中心化訊息整合（v0.14.0 第 22 平台） | Pluggable Gateway |
| **ntfy** | 自託管推播通知平台（v0.15.0 第 23 平台）、零帳號、ntfy.sh 或自建 | Pluggable Gateway |

#### 2.3.2 API Gateway Layer（閘道層）

Gateway 是 Hermes 的消息路由核心，負責：
- **認證與授權**：DM Pairing、allowed_users 白名單
- **限流與超時**：基於活動的智慧超時（非掛鐘計時）
- **訊息去重**：防止重複投遞
- **多平台路由**：統一介面分發到各平台
- **審批機制**：危險指令需透過 `/approve` 或平台原生按鈕確認
- **Platform Allowlists**（v0.13.0）：`allowed_channels` / `allowed_chats` / `allowed_rooms` 跨 Slack / Telegram / Mattermost / Matrix / DingTalk
- **Session 自動恢復**（v0.13.0）：Gateway 重啟後自動恢復中斷的對話
- **通用 Platform-Plugin Hooks**（v0.13.0）：`env_enablement_fn` + `cron_deliver_env_var`，IRC 與 Teams 已遷移至此機制
- **s6-overlay Docker 容器監督**（v0.15.0）：systemd/launchd/Windows/s6 後端 + per-profile gateway 監督
- **Session Control API**（v0.15.0）：`/api/sessions/*` REST + SSE 端點

#### 2.3.3 Agent Layer（代理層）

| 組件 | 職責 |
|------|------|
| Agent Core | 核心循環：接收 → 規劃 → 工具呼叫 → 評估 → 回應 |
| Subagent Pool | 隔離子代理，支援平行工作流 |
| Skill Engine | 載入已有技能、複雜任務後自動建立新技能 |
| Plugin System | 擴展記憶 / CLI / API Hook，如 Honcho、Hindsight |

#### 2.3.4 Memory Layer（記憶層）

| 類型 | 實作 | 用途 |
|------|------|------|
| Short-term | Context Window | 當次對話上下文管理，支援 `/compress` 壓縮 |
| Long-term | MEMORY.md / USER.md | 持久化知識、使用者偏好 |
| Session Search | FTS5 + LLM Summarization | 跨對話搜尋與摘要 |
| Vector DB | mem0 / Supermemory | 語義搜尋、多容器記憶 |
| User Model | Honcho Dialectic | 辯證式使用者理解與信任分數 |

#### 2.3.5 Tool Layer（工具層）

Hermes 內建 **60+ 工具**（v0.14.0 起 debloating 浪潮將部分重型後端改為 lazy install），分為以下類別：

| 類別 | 工具 | 說明 |
|------|------|------|
| Terminal | execute_command, execute_code | 6 種後端：Local, Docker, SSH, Modal, Daytona, Singularity（v0.15.0 移除 Vercel Sandbox） |
| Browser | browser_open, browser_navigate, browser_console | Playwright / Camofox 反偵測 / Browser Use 託管 / Firecrawl 雲端 / **Lightpanda**（v0.12.0）/ **180 倍 `browser_console` 效能提升**（v0.14.0 持久 CDP 連線） |
| File | read_file, write_file, search_files | 檔案讀寫、搜尋、.zip 文件支援、**Per-turn 檔案變更驗證 Footer**（v0.14.0）、**LSP 語義診斷**（v0.14.0） |
| Web | web_search, web_extract, **x_search** | 網頁搜尋與內容擷取、Vision 圖像分析、**SearXNG** 搜尋後端（v0.12.0）、**Brave Search + DDGS**（v0.14.0）、**`x_search` X (Twitter) 搜尋**（v0.14.0） |
| MCP | 任意 MCP 伺服器 | OAuth 2.1 PKCE 認證，OSV 惡意軟體掃描、**Nous 核准 MCP 目錄**（v0.15.0）、**mTLS 支援**（v0.15.0） |
| Cron | cron_add, cron_list, cron_remove | 自然語言排程，多平台投遞，Per-job `workdir`（v0.12.0） |
| Delegation | delegate_task | 委派子代理執行平行任務 |
| Voice | voice_transcribe, voice_synthesize | STT/TTS 語音轉文字與文字轉語音 |
| Vision | vision_analyze | **原生像素傳遞**（v0.14.0：Vision 模型直接看圖，不經壓縮） |
| Video | video_analyze, **video_generate** | 影片理解（v0.13.0）+ **統一 video_generate 可插拔後端**（v0.14.0） |
| Desktop | **computer_use** | **cua-driver 後端**（v0.14.0：非 Anthropic 模型也可驅動桌面自動化） |
| Session | **session_search** | **v0.15.0 重建**：無 LLM、免費、4,500 倍快速（~20ms vs ~90s） |

#### 2.3.6 Data Layer（資料層）

| 儲存 | 技術 | 存放內容 |
|------|------|----------|
| SQLite | 內建 | Session 歷史、設定、Cron 排程 |
| File System | `~/.hermes/` | Skills、Memories、SOUL.md、Logs |
| External APIs | HTTP/gRPC | LLM Provider（OpenAI / Anthropic / OpenRouter 等） |

### 2.4 多 Agent 協作架構

```mermaid
sequenceDiagram
    participant User as 使用者
    participant Main as Main Agent
    participant Sub1 as Subagent-1（Research）
    participant Sub2 as Subagent-2（Coding）
    participant Sub3 as Subagent-3（Testing）
    participant Tools as Tool Layer

    User->>Main: 複雜任務請求
    Main->>Main: 規劃（Task Decomposition）
    
    par 平行委派
        Main->>Sub1: 研究任務
        Sub1->>Tools: web_search / web_extract
        Sub1-->>Main: 研究結果
    and
        Main->>Sub2: 程式開發
        Sub2->>Tools: write_file / execute_code
        Sub2-->>Main: 程式碼
    end
    
    Main->>Sub3: 測試驗證
    Sub3->>Tools: execute_command（pytest）
    Sub3-->>Main: 測試結果
    
    Main->>Main: 整合、學習、技能封裝
    Main-->>User: 完成回報
```

**關鍵特性**：

- **隔離性**：每個 Subagent 有獨立的 Context Window，不污染主 Agent
- **零上下文成本**：子代理執行結果以摘要形式回傳，不消耗主 Agent 的上下文
- **Credential 共享**：子代理共享主 Agent 的 Credential Pool
- **Workspace 路徑提示**：自動傳遞工作目錄給子代理

### 2.5 高可用與擴展性設計

```mermaid
graph TB
    subgraph "高可用架構"
        LB[Load Balancer<br/>Nginx / HAProxy]
        
        subgraph "Agent Cluster"
            A1[Hermes Instance 1<br/>Profile: default]
            A2[Hermes Instance 2<br/>Profile: team-dev]
            A3[Hermes Instance 3<br/>Profile: team-ops]
        end
        
        subgraph "Shared Storage"
            NFS[(NFS / S3<br/>Skills + Memories)]
            DB[(PostgreSQL<br/>Sessions)]
            REDIS[(Redis<br/>Cache + Queue)]
        end
        
        subgraph "Model Providers"
            NP[Nous Portal<br/>免費模型]
            OR[OpenRouter<br/>200+ 模型]
            OA[OpenAI<br/>GPT-5.5]
            AN[Anthropic<br/>Claude]
            GG[Google AI Studio<br/>Gemini]
            QW[Qwen / xAI<br/>Grok]
            NV[NVIDIA NIM<br/>Nemotron]
            BK[AWS Bedrock]
            LOCAL[Ollama<br/>本地模型]
        end
    end

    LB --> A1
    LB --> A2
    LB --> A3
    
    A1 --> NFS
    A2 --> NFS
    A3 --> NFS
    A1 --> DB
    A2 --> DB
    A3 --> DB
    A1 --> REDIS
    
    A1 --> NP
    A1 --> OR
    A2 --> OA
    A3 --> AN
    A3 --> LOCAL
```

**企業級設計要點**：

1. **多 Profile 隔離**：使用 `hermes --profile team-dev` 啟動獨立實例，Memory 和 Skill 完全隔離
2. **Model Failover**：Credential Pool 支援多個 Provider，主 Provider 失敗自動切換
3. **Serverless 選項**：Daytona / Modal 後端，閒置時自動休眠，幾乎零成本
4. **Gateway 集中化**：單一 Gateway 程序管理所有通訊平台連線

> **注意事項**：Hermes Agent 目前不支援 Native Windows，企業部署請使用 Linux VM / WSL2 / Docker 容器。

---

## 第三章：Hermes Agent 核心機制解析

### 3.1 Learning Loop（學習迴圈）

Learning Loop 是 Hermes 最核心的差異化設計，使其成為唯一具備「自我改進」能力的開源 Agent。

```mermaid
graph TD
    A[接收任務] --> B[分析 & 規劃]
    B --> C[執行任務<br/>呼叫工具鏈]
    C --> D{任務複雜度高?}
    D -->|是| E[自動回顧過程]
    E --> F[提取經驗模式]
    F --> G[封裝為 Skill]
    G --> H[存入技能庫]
    D -->|否| I[完成回應]
    H --> I
    I --> J[週期性 Nudge<br/>提醒持久化知識]
    J --> K[更新 Memory]
    K --> A
    
    style E fill:#e1f5fe
    style F fill:#e1f5fe
    style G fill:#e1f5fe
    style H fill:#e1f5fe
```

**學習迴圈的三個觸發時機**：

1. **任務完成後**：Agent 自動評估任務複雜度，對高複雜度任務進行回顧與封裝
2. **週期性 Nudge**：Agent 主動提醒自己持久化重要知識到 MEMORY.md
3. **使用技能時**：如果現有 Skill 在執行過程中發現改進點，會自動更新 Skill 內容

#### 3.1.1 Self-improvement Loop 升級（v0.12.0）

v0.12.0 對 Learning Loop 進行大幅升級：

| 改進項目 | 說明 |
|----------|------|
| **Class-first Rubric** | 基於分類評分標準評估 Skill 品質，取代簡單的數值評分 |
| **Active-update Bias** | 偏好主動更新現有 Skill 而非建立新 Skill，減少重複 |
| **Fork Inheritance** | Fork 的 Skill 自動繼承父 Skill 的執行統計資料 |
| **Scoped Toolset** | 自我改進過程僅可存取 memory + skills 工具，不可執行系統指令 |
| **Autonomous Curator** | 配合 3.7 節 Curator 自動維護技能庫品質 |

**範例 — Skill 自動建立流程**：

```
使用者：幫我分析這個 Spring Boot 專案的安全漏洞

Agent 執行過程：
1. 讀取 pom.xml（了解依賴）
2. 搜尋已知 CVE
3. 掃描程式碼（SQL Injection / XSS 等）
4. 生成報告

Agent 自動回顧：
→ 這個任務涉及多步驟安全分析
→ 封裝為 Skill: "spring-security-audit"
→ 下次呼叫 /spring-security-audit 即可直接使用
```

### 3.2 Skill System（技能系統）

#### 3.2.1 技能結構

每個 Skill 是一個目錄，包含一個 Markdown 指令檔：

```
~/.hermes/skills/
├── bundled/                    # 官方內建技能
│   ├── claude-code/
│   │   └── skill.md
│   ├── popular-web-designs/
│   │   └── skill.md
│   ├── gitnexus-explorer/
│   │   └── skill.md
│   ├── humanizer/              # v0.12.0: 去除 AI 文風
│   │   └── skill.md
│   └── spotify/                # v0.12.0: Spotify 整合技能
│       └── skill.md
├── user/                       # 使用者自建技能
│   ├── spring-security-audit/
│   │   └── skill.md
│   └── bank-api-generator/
│       └── skill.md
└── community/                  # 社群下載技能
    └── research-paper-writing/
        └── skill.md
```

#### 3.2.2 Skill 範例

```markdown
# spring-security-audit

## Description
掃描 Spring Boot 專案的常見安全漏洞，包括依賴 CVE、程式碼注入風險、認證配置問題。

## Steps
1. 讀取 pom.xml 或 build.gradle，列出所有依賴版本
2. 使用 web_search 查詢各依賴的已知 CVE
3. 掃描 src/ 目錄中的以下模式：
   - SQL String Concatenation（SQL Injection 風險）
   - @CrossOrigin 無限制（CORS 風險）
   - 硬編碼密碼或 API Key
4. 檢查 Spring Security 配置（SecurityFilterChain）
5. 生成安全報告（表格格式 + 嚴重度 + 修復建議）

## Config
- scan_depth: 3  # 掃描目錄深度
- severity_threshold: medium  # 最低報告嚴重度
```

#### 3.2.3 技能管理指令

| 指令 | 說明 |
|------|------|
| `/skills` | 列出所有可用技能 |
| `/<skill-name>` | 執行特定技能 |
| `/skills install <url>` | 從 Skills Hub 安裝技能 |
| `/skills create` | 手動建立新技能 |
| 自動建立 | Agent 複雜任務完成後自動封裝 |

#### 3.2.4 Skills Hub（agentskills.io）

Hermes 支援 [agentskills.io](https://agentskills.io/) 開放標準，技能可在社群間分享與下載。每個技能都有版本控制、使用統計和評分。

### 3.3 Memory System（記憶系統）

Hermes 的記憶系統分為多層，從短期到長期，提供完整的知識持久化方案。

```mermaid
graph LR
    subgraph "Short-term（短期記憶）"
        CTX[Context Window<br/>當前對話上下文]
        COMP[Context Compaction<br/>Token 預算壓縮]
    end
    
    subgraph "Mid-term（中期記憶）"
        SESS[Session Search<br/>FTS5 全文搜尋]
        SUM[LLM Summarization<br/>跨對話摘要]
    end
    
    subgraph "Long-term（長期記憶）"
        MEM[MEMORY.md<br/>核心知識]
        USER[USER.md<br/>使用者偏好]
        SOUL[SOUL.md<br/>Agent 人格]
    end
    
    subgraph "Plugin Memory（插件記憶）"
        M0[mem0<br/>語義記憶]
        SM[Supermemory<br/>多容器記憶]
        HC[Honcho<br/>辯證式建模]
        HS[Hindsight<br/>事後分析]
    end
    
    CTX --> COMP
    COMP --> SESS
    SESS --> SUM
    SUM --> MEM
    MEM --> USER
    
    CTX --> M0
    CTX --> SM
    CTX --> HC
    CTX --> HS
```

#### 3.3.1 記憶提供者比較

| Provider | 類型 | 適用場景 | 特點 |
|----------|------|----------|------|
| 內建 | 檔案 | 個人 / 小團隊 | MEMORY.md + USER.md，零依賴 |
| mem0 | Vector | 語義搜尋場景 | API v2 相容、Secret 遮蔽 |
| Supermemory | Vector | 多租戶 / 企業 | 多容器支援、search_mode、identity template |
| Honcho | 辯證式 | 個人化 Agent | 信任分數、Holographic Prompt |
| Hindsight | 事後分析 | 學習增強 | 事後回顧 + 記憶整理 |
| RetainDB | 完整 DB | 大規模部署 | 寫入佇列、檔案工具整合 |
| OpenViking | API | 多租戶伺服器 | tenant-scoping headers |
| ByteRover | 同步 | 即時查詢 | LLM 呼叫前同步查詢 |

#### 3.3.2 記憶設定範例

```yaml
# ~/.hermes/config.yaml
memory:
  provider: supermemory  # 或 mem0, honcho, builtin
  auto_save: true
  nudge_interval: 5      # 每 5 輪對話提醒一次持久化
  
  supermemory:
    containers:
      - name: project-knowledge
        description: "專案技術知識"
      - name: user-preferences  
        description: "使用者偏好與習慣"
    search_mode: hybrid    # keyword + semantic
```

### 3.4 Planning / Execution Flow

Hermes Agent 的核心執行流程如下：

```mermaid
stateDiagram-v2
    [*] --> Receive: 接收使用者訊息
    Receive --> Prefetch: Memory Prefetch
    Prefetch --> Plan: 規劃步驟
    Plan --> ToolCall: 呼叫工具
    ToolCall --> Execute: 執行工具
    Execute --> Evaluate: 評估結果
    
    Evaluate --> ToolCall: 需要更多工具
    Evaluate --> Respond: 完成
    
    Respond --> Learn: 學習（自動）
    Learn --> Nudge: 記憶 Nudge
    Nudge --> [*]
    
    Execute --> Approve: 需要審批
    Approve --> Execute: 使用者同意
    Approve --> Reject: 使用者拒絕
    Reject --> Plan: 重新規劃
```

**關鍵機制說明**：

1. **Memory Prefetch**：在 LLM 呼叫前，同步查詢記憶插件，注入相關上下文
2. **Tool Call Coercion**：自動轉換工具呼叫參數類型（修正模型傳入字串而非數字的問題）
3. **Oversized Result Handling**：過大的工具結果自動存檔，避免破壞性截斷
4. **Approval Gate**：危險指令（如 `rm -rf`、`git push --force`）需使用者確認
5. **Context Compaction**：上下文接近 Token 上限時，自動壓縮保留重要資訊

### 3.5 Tool Calling 機制

#### 3.5.1 內建 Toolsets

Hermes 將工具組織為 **Toolsets**（工具集），可個別啟用或停用：

```bash
hermes tools                    # 列出所有工具集與狀態
hermes tools enable browser     # 啟用瀏覽器工具集
hermes tools disable delegation # 停用委派工具集
```

| Toolset | 包含工具 | 預設狀態 |
|---------|---------|----------|
| `core` | execute_command, read_file, write_file, search_files, patch | 啟用 |
| `browser` | browser_open, browser_navigate, browser_console, browser_screenshot | 停用 |
| `web` | web_search, web_extract | 啟用 |
| `delegation` | delegate_task | 啟用 |
| `mcp` | 外部 MCP 伺服器工具 | 依設定 |
| `cron` | cron_add, cron_list, cron_remove, cron_status | 啟用 |
| `code` | execute_code | 啟用 |
| `voice` | voice_transcribe, voice_synthesize | 停用 |
| `spotify` | spotify_play, spotify_pause, spotify_search 等 | v0.12.0 停用 |
| `kanban` | kanban_create, kanban_assign, kanban_status 等 | v0.13.0 啟用 |
| `video` | **video_analyze**（原生影片理解，Gemini + 相容多模態模型） | v0.13.0 停用 |

#### 3.5.2 MCP（Model Context Protocol）擴展

```yaml
# ~/.hermes/config.yaml
mcp:
  servers:
    - name: github
      command: npx
      args: ["@modelcontextprotocol/server-github"]
      env:
        GITHUB_TOKEN: "${GITHUB_TOKEN}"
    - name: postgres
      command: npx
      args: ["@modelcontextprotocol/server-postgres"]
      env:
        DATABASE_URL: "${DATABASE_URL}"
```

**安全特性**：
- OAuth 2.1 PKCE 認證（v0.8.0 新增）
- OSV 惡意軟體掃描（自動檢測 MCP 套件漏洞）
- 工具過濾（可限制 MCP 伺服器暴露的工具）
- **SSE Transport**（v0.13.0）：支援 Server-Sent Events 傳輸協定 + OAuth 轉發
- **Stale-pipe 重試**（v0.13.0）：過期管道自動以 Session-expired 重試
- **圖片結果交付**（v0.13.0）：MCP 工具的圖片結果以 MEDIA 標籤呈現（不再被丟棄）
- **長連線 Keepalive**（v0.13.0）：`_wait_for_lifecycle_event` 定期心跳，防止連線超時
- **TOCTOU 修正**（v0.13.0）：MCP OAuth 憑證儲存的時間競爭視窗已關閉
- **mTLS 支援**（v0.15.0）：MCP 伺服器支援雙向 TLS 認證
- **Nous 核准 MCP 目錄**（v0.15.0）：`hermes mcp` 互動式 picker，一鍵安裝核准的 MCP 伺服器

#### 3.5.3 Terminal Backends

| 後端 | 連線方式 | 適用場景 |
|------|----------|----------|
| Local | 本地 Shell | 開發環境 |
| Docker | Docker API | 隔離執行 |
| SSH | SSH 連線 | 遠端伺服器 |
| Daytona | Daytona API | Serverless（閒置休眠） |
| Modal | Modal API | GPU 計算 / Serverless |
| Singularity | Container | HPC 環境 |

> **注意**：v0.15.0 起移除 Vercel Sandbox 後端。原使用 Vercel Sandbox 的使用者請遷移至 Docker、Daytona 或 Modal。

**瀏覽器後端**（v0.8.0 更新）：

| 後端 | 說明 | 適用場景 |
|------|------|----------|
| Playwright | 本地 Chromium 瀏覽器 | 一般網頁操作 |
| Camofox | 反偵測 Firefox 瀏覽器 | 需要反偵測的場景 |
| Browser Use | 託管瀏覽器服務（取代 Browserbase）| 雲端瀏覽、免本地安裝 |
| Firecrawl | 雲端網頁擷取服務 | 大規模網頁爬取 |

```yaml
# ~/.hermes/config.yaml
terminal:
  backend: docker
  docker:
    image: "python:3.11-slim"
    docker_env:
      PYTHONPATH: "/workspace"
    volumes:
      - "./project:/workspace"
```

### 3.6 Model Routing（多模型切換）

Hermes 的 `/model` 指令支援即時切換模型與 Provider（v0.5.0 引入，v0.8.0 大幅強化）：

```bash
# CLI 切換
/model anthropic:claude-sonnet-4-20250514
/model openrouter:deepseek/deepseek-r1
/model nous:hermes-3-405b
/model google:gemini-2.5-pro
/model qwen:qwen-max
/model xai:grok-3

# 查看當前模型
/model

# 切換 Provider
hermes model   # 互動式選擇
```

#### 3.6.1 Credential Pool 與 Failover

```yaml
# ~/.hermes/config.yaml
providers:
  primary: anthropic
  fallback:
    - openrouter
    - nous
  
  anthropic:
    api_key: "${ANTHROPIC_API_KEY}"
    model: claude-sonnet-4-20250514
  
  openrouter:
    api_key: "${OPENROUTER_API_KEY}"
    model: anthropic/claude-sonnet-4-20250514
  
  nous:
    # OAuth 自動管理
    model: hermes-3-405b

# 輔助模型（壓縮 / Vision / 摘要）
auxiliary:
  provider: nous
  model: mimo-v2-pro  # 免費模型
```

#### 3.6.2 Model Routing 策略

```mermaid
graph TD
    REQ[推理請求] --> PRI{Primary Provider<br/>可用?}
    PRI -->|是| CALL1[呼叫 Primary]
    PRI -->|否| FB1{Fallback 1<br/>可用?}
    FB1 -->|是| CALL2[呼叫 Fallback 1]
    FB1 -->|否| FB2{Fallback 2<br/>可用?}
    FB2 -->|是| CALL3[呼叫 Fallback 2]
    FB2 -->|否| ERR[錯誤：無可用 Provider]
    
    CALL1 --> RES{回應成功?}
    CALL2 --> RES
    CALL3 --> RES
    
    RES -->|是| OK[返回結果]
    RES -->|402 付費失敗| RETRY[切換下一個 Provider]
    RES -->|429 限流| BACKOFF[指數退避 + Jitter 重試]
    RES -->|500 伺服器錯誤| RETRY
    
    RETRY --> FB1
    BACKOFF --> REQ
```

**關鍵特性**：
- **Aggregator-aware Resolution**：透過 OpenRouter / Nous Portal 路由時，自動解析最佳模型
- **Payment Fallback**：402 錯誤（餘額不足）自動切換下一個 Provider
- **Jittered Retry Backoff**：避免多實例同時重試造成的 thundering herd
- **Stale OAuth Recovery**：過期 OAuth Token 自動刷新（v0.8.0 修正）

> **最佳實踐**：企業部署建議配置至少 2 個 Provider（Primary + Fallback），並使用免費的 Nous Portal mimo-v2-pro 作為輔助模型。這樣即使主 Provider 當機，Agent 仍可用 Fallback 持續運作。

---

### 3.7 Autonomous Curator（自動技能維護）

v0.12.0 引入的 **Autonomous Curator** 是一個背景運行的自動化 Agent，負責維護技能庫品質，確保 Skills 保持最新、精簡且高品質。

#### 3.7.1 運作原理

```mermaid
graph TD
    CRON["Cron Ticker<br/>(每 7 天觸發)"] --> SCAN["掃描所有 Skills"]
    SCAN --> GRADE["評分每個 Skill<br/>(品質 + 使用頻率)"]
    GRADE --> DECIDE{決策}
    DECIDE -->|低品質| PRUNE["修剪: 刪除或合併"]
    DECIDE -->|重複| MERGE["合併重複 Skill"]
    DECIDE -->|高品質| KEEP["保留"]
    DECIDE -->|可改善| REFINE["精煉: 改善內容"]
    
    PRUNE --> REPORT["產出報告"]
    MERGE --> REPORT
    KEEP --> REPORT
    REFINE --> REPORT
    
    REPORT --> LOG["logs/curator/run.json"]
    REPORT --> MD["logs/curator/REPORT.md"]
```

#### 3.7.2 核心特性

| 特性 | 說明 |
|------|------|
| **Class-first 評分** | 基於 Rubric 的分類評估，非簡單數值打分 |
| **Active-update 偏向** | 偏好更新而非刪除，盡量保留學習成果 |
| **Fork 繼承** | Fork 的 Skill 繼承父 Skill 的運行時資料 |
| **Scoped Toolset** | Curator 僅可存取 memory + skills 工具，不可執行系統指令 |
| **安全邊界** | Bundled / Hub / Pinned Skills 受保護不被修改 |

#### 3.7.3 CLI 操作

```bash
# 手動觸發 Curator
hermes curator

# 查看 Curator 狀態（依使用頻率排名）
hermes curator status

# 查看最近一次 Curator 報告
cat logs/curator/REPORT.md
```

#### 3.7.4 設定檔

```yaml
# ~/.hermes/config.yaml
auxiliary:
  curator:
    enabled: true           # 啟用 / 停用
    interval_days: 7        # 執行間隔（天）
    min_quality_score: 0.3  # 品質閾值
    max_skills: 500         # 技能庫上限
    protect_pinned: true    # 保護 pinned skills
```

> **企業建議**：大型團隊建議將 Curator 間隔設為 3-5 天，並監控 `REPORT.md` 確保重要技能不被意外修剪。可透過 `pinned` 標記保護關鍵技能。

### 3.8 Persistent Goals 與 Ralph Loop

v0.13.0 引入的 `/goal` 指令，是 Agent 自主性的重要里程碑。Agent 不再僅回應單次對話，而是能鎖定長期目標並跨回合追蹤進度。

#### 3.8.1 運作原理

```mermaid
graph TD
    USER["使用者設定 /goal"] --> LOCK["Agent 鎖定目標"]
    LOCK --> PLAN["制定執行計畫"]
    PLAN --> EXEC["執行步驟"]
    EXEC --> EVAL{"已完成?"}
    EVAL -->|否| TRACK["追蹤進度<br/>(跨回合持久)"]
    TRACK --> REMIND["新對話開始時<br/>提醒目標進度"]
    REMIND --> EXEC
    EVAL -->|是| COMPLETE["標記目標完成"]
    
    RESTART["Session 中斷 /<br/>Gateway 重啟"] -.->|自動恢復| TRACK
```

#### 3.8.2 核心特性

| 特性 | 說明 |
|------|------|
| **跨回合持久** | 目標不因對話分頁、Session 邊界、Gateway 重啟而遺失 |
| **Turn Budget** | 可設定目標允許的最大回合數，防止 Agent 無限循環 |
| **Ralph Loop** | 將 learning loop 提升為一級原語（first-class primitive） |
| **進度追蹤** | 每次對話開始時自動提醒目標狀態與剩餘步驟 |

#### 3.8.3 使用範例

```bash
# 設定一個跨回合持久目標
> /goal 將整個後端 API 從 REST 遷移到 GraphQL，包括 schema 設計、resolver 實作、測試覆蓋

# Agent 會自動拆解為多個子任務，持續追蹤
# 即使切換話題或重啟 Gateway，目標仍然有效

# 查看當前目標狀態
> /goal status

# 清除目標
> /goal clear
```

### 3.9 Post-write Delta Lint（自動語法檢查）

v0.13.0 為 `write_file` 和 `patch` 工具新增即時增量語法檢查機制。Agent 寫入檔案時自動驗證語法正確性，錯誤在當下浮出而非向下游傳遞。

#### 3.9.1 支援格式

| 格式 | 檢查範圍 | 說明 |
|------|----------|------|
| **Python** | AST 語法驗證 | 透過內建 linter 檢查語法樹 |
| **JSON** | 結構驗證 | 確保有效 JSON 格式 |
| **YAML** | 結構驗證 | 確保有效 YAML 格式 |
| **TOML** | 結構驗證 | 確保有效 TOML 格式 |

#### 3.9.2 運作方式

- **增量檢查（Delta）**：僅檢查寫入變更的部分，不影響效能
- **即時回饋**：語法錯誤立即顯示在工具輸出中
- **自動修正**：Agent 可根據 lint 結果自動修正錯誤
- **In-proc 執行**：linter 在 Agent Process 內執行，無需外部工具

### 3.10 Checkpoints v2（狀態持久化）

v0.13.0 完全重寫狀態持久化系統，解決舊版 Checkpoint 機制的三大痛點：

| 舊版問題 | v2 解決方案 |
|----------|------------|
| 孤立 Shadow Repos 無法清理 | 單一儲存（Single-store）架構 |
| 磁碟空間無限膨脹 | 真正的修剪（Real pruning）+ 磁碟護欄（Disk guardrails） |
| 跨 Session 狀態遺失 | 完整的 Session 恢復機制 |

**企業建議**：升級到 v0.13.0 後，建議執行一次完整的 Checkpoint 清理以釋放舊版孤立資源。

---

## 第四章：安裝與環境建置

### 4.1 系統需求

| 需求項目 | 最低要求 | 建議配置 |
|----------|----------|----------|
| 作業系統 | Linux / macOS / WSL2 / Windows（Early Beta）/ Android (Termux) | Ubuntu 22.04 LTS / macOS 14+ |
| Python | 3.11+ | 3.11（官方測試版本）|
| Node.js | 18+ | 22 LTS |
| 記憶體 | 2 GB | 4 GB+ |
| 磁碟空間 | 500 MB | 2 GB+（含依賴與快取）|
| 網路 | 可連接 LLM API | 穩定連線 |
| Git | 2.30+ | 最新版 |

> 🪟 **Windows 支援**（v0.13.0+）：Hermes Agent 現提供 **Native Windows 早期測試版**（Early Beta），可透過 PowerShell 安裝腳本直接安裝。仍建議穩定生產環境使用 [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)。

> 📱 **Android 支援**（v0.12.0+）：Hermes 可在 Android 的 [Termux](https://termux.dev/) 環境中運行，安裝方式與 Linux 相同。

### 4.2 快速安裝（Linux / macOS / WSL2）

#### 4.2.1 一鍵安裝

```bash
# 一鍵安裝（處理所有依賴：Python、Node.js、套件、hermes 指令）
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# 重新載入 Shell 環境
source ~/.bashrc    # Bash 使用者
source ~/.zshrc     # Zsh 使用者

# 驗證安裝
hermes --version
```

#### 4.2.2 手動安裝（從原始碼）

```bash
# 1. Clone 專案
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# 2. 安裝 uv（Python 套件管理器）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. 建立虛擬環境
uv venv venv --python 3.11
source venv/bin/activate

# 4. 安裝所有依賴
uv pip install -e ".[all]"

# 5. 驗證
python cli.py --version
```

#### 4.2.3 Homebrew 安裝（macOS）

```bash
# v0.6.0+ 支援 Homebrew
brew install hermes-agent

# 升級
brew upgrade hermes-agent
```

### 4.3 Native Windows 安裝（Early Beta）

v0.13.0 開始提供 Native Windows 早期測試版支援，無需 WSL2 即可直接在 Windows 上運行。

#### 4.3.1 PowerShell 一鍵安裝

```powershell
# 以系統管理員身份開啟 PowerShell
# 一鍵安裝（處理所有依賴）
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex

# 驗證安裝
hermes --version
```

#### 4.3.2 注意事項

| 項目 | 說明 |
|------|------|
| **狀態** | Early Beta — 部分功能可能不穩定 |
| **建議** | 生產環境仍建議使用 WSL2 或 Linux |
| **Runtime Lock** | v0.13.0 修正了 Windows runtime-lock offset 問題 |
| **路徑轉換** | ACP Adapter 已支援 Windows cwd → WSL 路徑自動轉換 |
| **WSL 互通** | 可保留 WSL interop PATH 在 systemd units 中 |

> **企業建議**：Windows 開發者建議採用 WSL2 + 完整 Linux 安裝路徑。Native Windows 適合快速原型驗證與個人開發場景。詳細的 WSL2 安裝指南（檔案系統、網路、服務、常見陷阱）已在 v0.13.0 文件大幅擴充。

### 4.4 Docker / Podman 部署

#### 4.4.1 使用官方 Docker Image

```bash
# 拉取映像
docker pull ghcr.io/nousresearch/hermes-agent:latest

# 啟動（互動模式）
docker run -it \
  --name hermes \
  -v ~/.hermes:/root/.hermes \
  -e ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}" \
  ghcr.io/nousresearch/hermes-agent:latest

# 啟動（Gateway 模式，背景執行）
docker run -d \
  --name hermes-gateway \
  --restart unless-stopped \
  -v ~/.hermes:/root/.hermes \
  -e ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}" \
  -e TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN}" \
  ghcr.io/nousresearch/hermes-agent:latest \
  hermes gateway start
```

> ⚠️ **v0.13.0 安全變更**：官方 Docker Image 現**拒絕以 root 身份運行 Gateway**。請確保使用 `hermes` 使用者或指定 `--user` 參數。

> 💡 **Dashboard in Docker**（v0.13.0）：在 Docker 中啟動 Dashboard，只需加入 `-e HERMES_DASHBOARD=1` 環境變數，Dashboard 會以 Side-process 方式啟動。

#### 4.4.2 自建 Docker Image

```dockerfile
# Dockerfile（專案根目錄已提供）
FROM python:3.11-slim

WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    git curl nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# 複製應用程式
COPY . .

# 安裝 Python 依賴
RUN pip install -e ".[all]"

# 安裝 Playwright（瀏覽器工具）
RUN playwright install chromium

ENTRYPOINT ["hermes"]
```

#### 4.4.3 Docker Compose（企業部署）

```yaml
# docker-compose.yml
version: '3.8'

services:
  hermes-agent:
    build: .
    container_name: hermes-agent
    restart: unless-stopped
    volumes:
      - hermes-data:/root/.hermes
      - ./projects:/workspace
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
    ports:
      - "8080:8080"  # API Server
    networks:
      - hermes-net
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2.0'

  hermes-gateway:
    build: .
    container_name: hermes-gateway
    restart: unless-stopped
    command: hermes gateway start
    volumes:
      - hermes-data:/root/.hermes
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}
      - SLACK_BOT_TOKEN=${SLACK_BOT_TOKEN}
    networks:
      - hermes-net

volumes:
  hermes-data:

networks:
  hermes-net:
    driver: bridge
```

### 4.5 Nix Flake 安裝

```bash
# Nix Flake 安裝（v0.5.0+ 支援）
nix profile install github:NousResearch/hermes-agent

# 或在 NixOS 配置中
{
  inputs.hermes-agent.url = "github:NousResearch/hermes-agent";
  
  # 加入系統套件
  environment.systemPackages = [ inputs.hermes-agent.packages.${system}.default ];
}
```

### 4.6 設定 API Key

#### 4.5.1 初始設定精靈

```bash
# 執行完整設定精靈（推薦首次使用）
hermes setup

# 精靈將引導完成：
# 1. 選擇 LLM Provider
# 2. 輸入 API Key
# 3. 選擇模型
# 4. 設定工具
# 5. 設定記憶系統
# 6. （可選）設定訊息平台
```

#### 4.5.2 環境變數設定

建立 `.env` 檔案：

```bash
# ~/.hermes/.env
# === 主要 Provider（至少需要一個）===

# Anthropic（推薦）
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# OpenAI
OPENAI_API_KEY=sk-xxxxxxxxxxxxx

# OpenRouter（200+ 模型）
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxx

# Nous Portal（免費模型可用）
# 使用 OAuth 登入：hermes auth login nous

# Google AI Studio（Gemini）
GOOGLE_AI_API_KEY=AIzaSyxxxxxxxxxxxx

# Qwen（通義千問）— OAuth 登入
# 使用 OAuth 登入：hermes auth login qwen

# xAI（Grok）
XAI_API_KEY=xai-xxxxxxxxxxxxx

# === 訊息平台 ===
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghIJKLmnoPQRSTuvwxyz
DISCORD_BOT_TOKEN=your-discord-bot-token
SLACK_BOT_TOKEN=xoxb-your-slack-token

# === MCP 伺服器 ===
GITHUB_TOKEN=ghp_xxxxxxxxxxxxx
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
```

#### 4.5.3 Nous Portal 登入（免費模型）

```bash
# OAuth 登入（瀏覽器會自動開啟）
hermes auth login nous

# 登入後可使用免費模型（如 MiMo v2 Pro）
# 無需 API Key，適合預算有限的團隊
```

### 4.7 設定檔說明

#### 4.6.1 主設定檔

```yaml
# ~/.hermes/config.yaml

# === 模型設定 ===
model:
  provider: anthropic
  model: claude-sonnet-4-20250514
  reasoning_effort: medium   # low / medium / high

# === 輔助模型（壓縮/Vision/摘要）===
auxiliary:
  provider: nous
  model: mimo-v2-pro         # 免費

# === 記憶設定 ===
memory:
  provider: builtin           # builtin / mem0 / supermemory / honcho
  auto_save: true
  nudge_interval: 5

# === 安全設定 ===
security:
  command_approval: smart      # always / smart / never / yolo
  allowed_commands:
    - "git status"
    - "git diff"
    - "npm test"
    - "mvn test"
    - "python -m pytest"

# === 終端後端 ===
terminal:
  backend: local               # local / docker / ssh / daytona / modal
  
# === 工具集 ===
toolsets:
  enabled:
    - core
    - web
    - delegation
    - cron
    - code
  disabled:
    - browser

# === MCP ===
mcp:
  servers: []

# === Gateway ===
gateway:
  platforms:
    telegram:
      enabled: true
      allowed_users: ["your_telegram_id"]
    discord:
      enabled: false
    slack:
      enabled: false

# === 日誌 ===
logging:
  level: INFO                  # DEBUG / INFO / WARNING / ERROR
  file: ~/.hermes/logs/agent.log
```

#### 4.6.2 設定檔驗證

v0.8.0 起新增**結構驗證**功能，啟動時會自動檢查 YAML 格式：

```bash
# 手動驗證設定
hermes doctor

# 診斷內容：
# ✅ Config YAML syntax valid
# ✅ Provider credentials found
# ✅ Model accessible
# ✅ Memory provider configured
# ✅ No WAL corruption detected
# ⚠️ Browser toolset disabled (optional)
```

> **實務案例**：某銀行團隊在 WSL2 上安裝 Hermes Agent，使用 Anthropic Claude 作為主 Provider，Nous Portal 免費模型作為輔助，Docker 後端做終端隔離。安裝過程約 5 分鐘，設定精靈引導完成所有配置。

---

## 第五章：快速開始（Quick Start）

### 5.1 第一次對話

```bash
# 啟動 Hermes（互動式 CLI）
hermes

# 進入 TUI 界面後，直接輸入問題：
> 你好！請自我介紹一下你的能力

# Agent 會回應其工具、記憶、技能能力
# 使用 Ctrl+C 暫停當前操作
# 使用 /new 開啟新對話
# 使用 /exit 或 Ctrl+D 離開
```

**常用 CLI 指令**：

| 指令 | 功能 |
|------|------|
| `/new` 或 `/reset` | 開啟新對話（保留記憶）；v0.13.0 支援 `/new [session-name]` 指定名稱 |
| `/model [provider:model]` | 切換模型（v0.13.0 TUI 與 `hermes model` 一致化 + 內建認證） |
| `/compress` | 壓縮當前上下文（v0.13.0 狀態列顯示壓縮次數） |
| `/usage` | 查看 Token 使用量 |
| `/insights [--days N]` | 查看使用洞察 |
| `/skills` | 列出可用技能 |
| `/personality [name]` | 設定人格 |
| `/retry` | 重試上一輪 |
| `/undo` | 撤銷上一輪 |
| `/busy [steer\|queue\|interrupt]` | 設定忙碗模式（v0.12.0）|
| `/btw` | 導引中插任務（v0.12.0）|
| `/reload-skills` | 重新載入技能庫（v0.12.0）|
| `/reload` | 熱重載 `.env` 設定（v0.12.0）|
| `/reload-mcp` | 重建 MCP cached agents（v0.12.0）|
| `/background` | 將任務移至背景執行（v0.12.0）|
| `/mouse` | 互動式滑鼠操作（v0.12.0）|
| `/fast` | 切換 Fast Mode（Priority Processing）|
| `/steer` | 中途導引 Agent 行為（v0.11.0）|
| **`/goal`** | **設定跨回合持久目標（Ralph Loop）（v0.13.0）** |
| **`/kanban`** | **管理 Multi-agent Kanban 看板（v0.13.0）** |
| **`/queue`** | **ACP：對進行中的 Agent 排隊後續指令（v0.13.0）** |

#### 5.1.1 Non-interactive 單次模式（v0.12.0+）

```bash
# 使用 -z 旗標執行單次任務（不進入互動式 TUI）
hermes -z "列出當前目錄下所有 Python 檔案"

# 指定模型與 Provider
hermes -z --model anthropic:claude-sonnet-4-20250514 "審查 main.py 的安全性"
hermes -z --provider openrouter "產生項目摘要"

# 適合 CI/CD 或腳本自動化使用
```

#### 5.1.2 Background Sessions（v0.12.0+）

```bash
# 將當前任務移至背景運行
/background

# 允許平行執行多個任務，主線程可繼續對話
# 背景任務完成後會自動通知
```

#### 5.1.3 Quick Commands（v0.12.0+）

```bash
# 自訂快速指令（直接執行 Shell，不經過 LLM）
# ~/.hermes/config.yaml
quick_commands:
  test: "mvn test"
  lint: "npm run lint"
  deploy: "./scripts/deploy.sh"

# 在 TUI 中使用
/test    # 直接執行 mvn test
/lint    # 直接執行 npm run lint
```

#### 5.1.4 Opt-in 自動恢復上次對話（v0.12.0+）

```yaml
# config.yaml
session:
  auto_resume: true    # 啟動時自動復原上次對話記錄
```

### 5.2 建立 AI Coding Agent

以下範例展示如何使用 Hermes 作為 Coding Agent 開發一個 REST API：

```bash
# 啟動 Hermes 並指定工作目錄
cd /path/to/your/project
hermes

# 開始互動
> 請幫我建立一個 Spring Boot REST API 專案，包含：
> 1. 使用者 CRUD API（/api/users）
> 2. JWT 認證
> 3. PostgreSQL 資料庫
> 4. Swagger 文件
> 5. 完整的單元測試
```

**Agent 執行流程**：

```
Agent 會自動：
1. [execute_command] 使用 Spring Initializr 建立專案骨架
2. [write_file] 建立 Entity、Repository、Service、Controller
3. [write_file] 建立 Security 配置（JWT Filter）
4. [write_file] 建立 application.yml（DB 連線）
5. [write_file] 建立 Swagger 配置
6. [write_file] 建立 JUnit 測試
7. [execute_command] 執行 mvn test 驗證
8. [自動學習] 封裝為 "spring-boot-rest-api" Skill
```

### 5.3 設定 Memory

```bash
# 設定 Memory Provider
hermes setup  # 在 Memory 區段選擇 provider

# 或直接編輯 config.yaml
hermes config set memory.provider supermemory
hermes config set memory.auto_save true
```

**記憶持久化範例**：

```bash
# 告訴 Agent 你的偏好
> 我使用 Java 21，偏好 Clean Architecture，測試框架用 JUnit 5 + Mockito

# Agent 會自動記錄到 MEMORY.md：
# - User prefers Java 21
# - Uses Clean Architecture
# - Testing: JUnit 5 + Mockito

# 下次對話時，Agent 會自動載入這些偏好
```

### 5.4 設定 Tools

```bash
# 查看所有工具集
hermes tools

# 啟用瀏覽器工具（如需要網頁操作）
hermes tools enable browser

# 設定 MCP 伺服器（擴展工具能力）
hermes config set mcp.servers '[{"name":"github","command":"npx","args":["@modelcontextprotocol/server-github"]}]'
```

### 5.5 執行任務範例

#### 範例 1：程式碼審查

```bash
> 請審查 src/main/java/com/example/UserService.java，
> 檢查安全性、效能和程式碼品質問題

# Agent 會：
# 1. 讀取檔案
# 2. 分析 SQL Injection / XSS 風險
# 3. 檢查效能瓶頸（N+1 Query 等）
# 4. 檢查 Code Style
# 5. 產出報告 + 修改建議
```

#### 範例 2：自動化部署腳本

```bash
> 幫我寫一個 GitHub Actions CI/CD pipeline，需求：
> - Java 21 + Maven
> - 執行 unit test 和 integration test
> - 建構 Docker image
> - 推送到 GitHub Container Registry
> - 部署到 Kubernetes

# Agent 會產出完整的 .github/workflows/deploy.yml
```

#### 範例 3：使用 Cron 排程

```bash
> 每天早上 9 點幫我：
> 1. 執行 git pull 更新專案
> 2. 執行 mvn test
> 3. 將測試結果傳到 Telegram

# Agent 會使用 cron_add 建立排程任務
# 結果自動透過 Gateway 投遞到指定平台
```

#### Per-job `workdir` 與 `context_from` 鏈式排程（v0.12.0+）

```yaml
# config.yaml — Cron 進階設定
cron:
  jobs:
    daily-test:
      schedule: "0 8 * * *"
      task: "執行完整測試套件並產出報告"
      workdir: "/home/dev/my-project"       # v0.12.0: 指定工作目錄
      deliver_to: telegram
    
    weekly-report:
      schedule: "0 9 * * 1"
      task: "根據上次測試結果產出週報"
      context_from: "daily-test"             # v0.12.0: 從前一任務繼承上下文
      deliver_to: slack
```

> **注意事項**：Quick Start 階段建議使用 `command_approval: smart`（預設），Agent 在執行危險指令前會要求確認。熟悉後可考慮調整為 `never`（自動批准所有安全指令）。

---

## 第六章：進階開發（企業級）

### 6.1 自訂 Skill（技能封裝）

#### 6.1.1 手動建立 Skill

建立目錄結構：

```bash
mkdir -p ~/.hermes/skills/user/bank-api-security-check
```

建立 `skill.md`：

```markdown
# bank-api-security-check

## Description
銀行 API 安全性檢查技能。依據 OWASP Top 10 和金融法規要求，
對 RESTful API 進行全面安全掃描。

## Triggers
- 使用者提到「安全檢查」、「弱掃」、「安全掃描」

## Steps
1. **掃描 API Controller**
   - 讀取所有 @RestController 類別
   - 檢查是否有 @PreAuthorize 或 @Secured 註解
   - 確認 CSRF 保護狀態

2. **檢查認證機制**
   - 確認 JWT 配置（Token 過期時間、簽發者驗證）
   - 檢查 OAuth2 Scope 設定
   - 確認 CORS 配置是否過於寬鬆

3. **掃描注入風險**
   - SQL Injection：搜尋字串拼接 SQL
   - XSS：檢查輸入是否有 sanitize
   - Command Injection：檢查 Runtime.exec() 使用
   - SSRF：檢查外部 URL 呼叫是否有白名單

4. **檢查敏感資料處理**
   - 確認密碼使用 BCrypt/Argon2 加密
   - 確認 PII 資料是否有遮蔽（Masking）
   - 確認日誌中不包含敏感資訊

5. **產出報告**
   - 格式：Markdown 表格
   - 欄位：風險項目 / 嚴重度 / 檔案位置 / 修復建議
   - 依嚴重度排序（Critical > High > Medium > Low）

## Config
- severity_threshold: medium
- include_owasp_references: true
- output_format: markdown
```

#### 6.1.2 Skill Config 介面（v0.8.0 新增）

Skills 可以宣告必要的 config.yaml 設定，在安裝時會自動提示使用者：

```markdown
# skill.md 中加入 Config Block

## Config
- api_scan_depth: 5
  description: "API 掃描深度（目錄層級）"
  required: true
- custom_rules_path: null
  description: "自訂規則檔案路徑"
  required: false
```

#### 6.1.3 從 Skills Hub 安裝

```bash
# 瀏覽社群技能
/skills

# 安裝特定技能
/skills install popular-web-designs
/skills install gitnexus-explorer
/skills install research-paper-writing

# 自動同步到所有 Profiles
hermes update  # 會自動將 bundled skills 同步到所有 profile
```

### 6.2 多 Agent 協作設計

#### 6.2.1 Subagent 委派機制

```mermaid
graph TD
    USER[使用者] --> MAIN[Main Agent<br/>任務分解 & 整合]
    
    MAIN --> |"delegate_task<br/>(credential sharing)"| SA1[Subagent: Researcher<br/>負責技術調研]
    MAIN --> |"delegate_task<br/>(workspace hints)"| SA2[Subagent: Developer<br/>負責程式碼開發]
    MAIN --> |"delegate_task"| SA3[Subagent: Reviewer<br/>負責程式碼審查]
    
    SA1 --> |"web_search<br/>web_extract"| WEB[Web Tools]
    SA2 --> |"write_file<br/>execute_code"| CODE[Code Tools]
    SA3 --> |"read_file<br/>execute_command"| TEST[Test Tools]
    
    SA1 -.-> |摘要回傳| MAIN
    SA2 -.-> |程式碼回傳| MAIN
    SA3 -.-> |審查報告| MAIN
    
    MAIN --> |最終結果| USER
```

**使用方式**：

```bash
> 請用以下分工完成這個功能：
> 1. 先研究 Spring Boot 3 的 Virtual Threads 最佳實踐
> 2. 根據研究結果開發 API
> 3. 對開發結果進行安全審查
> 
> 使用 subagent 平行處理第 1 和第 2 步

# Agent 會自動使用 delegate_task 工具委派子代理
```

#### 6.2.2 Programmatic Tool Calling（execute_code）

v0.8.0 的 `execute_code` 支援透過 RPC 呼叫工具，將多步驟流水線壓縮為單次推理：

```python
# Agent 可以生成並執行這樣的腳本
import json

# 透過 RPC 呼叫多個工具
results = []
files = tool_call("search_files", {"pattern": "*.java", "path": "src/"})
for f in files:
    content = tool_call("read_file", {"path": f})
    if "SQL" in content and "PreparedStatement" not in content:
        results.append({"file": f, "risk": "SQL Injection"})

# 一次性回傳結果，零額外上下文成本
print(json.dumps(results))
```

### 6.3 Multi-agent Kanban 實戰

v0.13.0 引入的 Multi-agent Kanban 是企業級多 Agent 協作的核心架構，遠超基本的 Subagent 委派。

#### 6.3.1 架構概述

```mermaid
graph TD
    USER[使用者 / Orchestrator] --> BOARD["Kanban Board<br/>(持久化看板)"]
    
    BOARD --> TASK1["Task 1: 後端 API"]
    BOARD --> TASK2["Task 2: 前端 UI"]
    BOARD --> TASK3["Task 3: 測試"]
    
    subgraph "Worker Pool"
        W1["Worker Agent 1<br/>(Profile: backend-dev)"]
        W2["Worker Agent 2<br/>(Profile: frontend-dev)"]
        W3["Worker Agent 3<br/>(Profile: qa-tester)"]
    end
    
    TASK1 -->|"自動指派"| W1
    TASK2 -->|"自動指派"| W2
    TASK3 -->|"自動指派"| W3
    
    W1 -.->|"心跳 / 進度"| BOARD
    W2 -.->|"心跳 / 進度"| BOARD
    W3 -.->|"心跳 / 進度"| BOARD
    
    subgraph "可靠性機制"
        HB["💓 心跳監測"]
        ZD["🧟 殭屍偵測"]
        RC["♻️ 工作回收"]
        HG["🛡️ 幻覺閘門"]
        RB["🔄 重試預算"]
    end
    
    BOARD --> HB
    BOARD --> ZD
    BOARD --> RC
    BOARD --> HG
    BOARD --> RB
```

#### 6.3.2 設定與使用

```yaml
# config.yaml — Multi-agent Kanban 完整設定
kanban:
  enabled: true
  multi_project: true         # 支援多專案看板
  max_retries: 3              # 每任務最大重試次數
  heartbeat_interval: 30      # Worker 心跳間隔（秒）
  zombie_timeout: 300         # 殭屍 Worker 判定超時（秒）
  hallucination_gate: true    # 啟用幻覺閘門
  
  # 跨 Profile 共享設定
  sharing:
    board: true               # 共享看板
    workspaces: true           # 共享工作區
    worker_logs: true          # 共享 Worker 日誌
```

```bash
# Kanban 操作指令
/kanban                        # 查看當前看板狀態
/kanban create "重構 API"       # 建立新任務
/kanban assign task-1 backend  # 指派任務到 Profile
/kanban status                 # 查看所有任務進度

# Worker 生命週期管理
hermes kanban workers          # 列出所有 Worker 狀態
hermes kanban diagnostics      # 執行任務診斷引擎
```

#### 6.3.3 可靠性保障機制

| 機制 | 說明 |
|------|------|
| **心跳監測** | Worker 定期發送心跳，超時則標記為失聯 |
| **殭屍偵測** | 自動偵測 Darwin 和 Linux 環境中的殭屍 Worker |
| **工作回收** | 失聯 Worker 的任務自動回收並重新指派 |
| **幻覺閘門** | 防止 Worker 聲稱完成了未建立的任務卡 |
| **重試預算** | 每任務可設定 `max_retries`，超過則標記失敗 |
| **統一失敗計數器** | 跨 spawn / timeout / crash 統一計算失敗次數 |
| **任務所有權驗證** | 對破壞性工具呼叫強制驗證 Worker 任務所有權 |
| **Auto-block** | 未完成退出的 Worker 自動被阻擋 |

> **企業建議**：Multi-agent Kanban 特別適合大型跨團隊專案，建議搭配 Profile 機制為不同角色（前端/後端/QA/DevOps）配置專屬的 SOUL.md 和技能集。

### 6.4 長期記憶設計（Vector DB）

#### 6.3.1 使用 Supermemory（推薦企業使用）

```yaml
# ~/.hermes/config.yaml
memory:
  provider: supermemory
  
  supermemory:
    # 多容器設計
    containers:
      - name: technical-knowledge
        description: "技術知識庫（架構/設計模式/最佳實踐）"
      - name: project-context
        description: "專案上下文（需求/決策/變更記錄）"
      - name: team-preferences
        description: "團隊偏好（程式風格/工具設定/流程）"
    
    search_mode: hybrid     # keyword + semantic
    identity_template: "enterprise-developer"
```

#### 6.3.2 使用 mem0

```yaml
# ~/.hermes/config.yaml
memory:
  provider: mem0
  
  mem0:
    api_key: "${MEM0_API_KEY}"     # Cloud 版
    # 或使用 mem0.json 進行本地配置
    prefetch_context: true          # LLM 呼叫前預取
    secret_redaction: true          # 自動遮蔽敏感資訊
```

#### 6.3.3 記憶架構設計（企業級）

```mermaid
graph TB
    subgraph "記憶分層策略"
        L1[L1: 對話快取<br/>Context Window<br/>TTL: 單次對話]
        L2[L2: 對話搜尋<br/>FTS5 Session Search<br/>TTL: 永久]
        L3[L3: 知識庫<br/>Vector DB<br/>TTL: 永久]
        L4[L4: 使用者建模<br/>Honcho Dialectic<br/>TTL: 永久]
    end
    
    L1 -->|壓縮與摘要| L2
    L2 -->|語義索引| L3
    L3 -->|行為分析| L4
    
    L4 -->|人格化回應| L1
    L3 -->|RAG 擷取| L1
    L2 -->|歷史查詢| L1
```

### 6.5 任務拆解（Task Decomposition）

Hermes Agent 自動進行任務拆解，但你可以透過 Prompt 引導更精確的分解：

```bash
> 我要重構整個訂單系統，請先分析後提出分階段執行計畫：
> 
> 系統現況：
> - Monolithic Spring Boot 2.7
> - 16 個 REST API
> - PostgreSQL 資料庫
> - 無單元測試
> 
> 目標：
> - 升級到 Spring Boot 3.2
> - 導入 Clean Architecture
> - 補齊單元測試（>80% 覆蓋率）
> - 保持向後相容

# Agent 會產出分階段計畫：
# Phase 1: 架構分析 & 依賴盤點
# Phase 2: Spring Boot 3.2 升級
# Phase 3: Clean Architecture 重構
# Phase 4: 測試補齊
# Phase 5: 效能測試 & 上線
```

### 6.6 Workflow Orchestration

#### 6.5.1 使用 Cron 建立自動化流程

```bash
> 建立以下自動化流程：
> 
> 1. 每天 08:00 - 檢查 GitHub 上的新 Issue，摘要傳到 Slack
> 2. 每天 18:00 - 執行程式碼品質掃描，結果傳到 Telegram
> 3. 每週一 09:00 - 生成週報（本週 commits / issues / PRs 摘要）
```

#### 6.5.2 使用 Context Files 定義工作流

在專案根目錄建立 `AGENTS.md`：

```markdown
# AGENTS.md - 專案上下文

## 專案說明
這是一個銀行核心系統的 REST API，使用 Spring Boot 3.2 + Java 21。

## 開發規範
- 所有 API 必須有輸入驗證
- 所有 Service 必須有 JUnit 測試
- 所有 Repository 方法必須使用 Parameterized Query
- 程式碼風格遵循 Google Java Style

## 部署流程
1. 通過 CI（mvn verify）
2. SonarQube 掃描通過
3. Docker build & push
4. K8s rolling update

## 安全要求
- 所有 API 需 JWT 認證
- 敏感資料需加密存儲
- 日誌不得包含 PII
```

Agent 在每次對話中都會載入此檔案，確保輸出符合專案規範。

#### 6.5.3 Profile-based 多團隊工作流

```bash
# 建立不同團隊的 Profile
hermes --profile team-backend     # 後端團隊
hermes --profile team-frontend    # 前端團隊
hermes --profile team-devops      # DevOps 團隊

# 每個 Profile 有獨立的：
# - Skills（技能）
# - Memory（記憶）
# - Config（設定）
# - SOUL.md（人格）
```

> **注意事項**：多 Agent 協作時，注意 Token 成本。建議使用 `/usage` 定期查看消耗。子代理回傳的結果會以摘要形式進入主 Agent 的上下文，有效控制成本。

### 6.7 SOUL.md 與 Personality 系統

SOUL.md 是 Hermes Agent 的人格定義檔案，決定 Agent 的說話風格、行為準則和限制條件。每個 Profile 可以有獨立的 SOUL.md。

#### 6.6.1 SOUL.md 結構

```markdown
# SOUL.md
你是「Hermes」，一個專業的 AI 開發助理。

## 性格特質
- 精確、專業、注重細節
- 主動提供替代方案
- 遇到不確定的問題時，會明確告知並提供最佳猜測

## 專業領域
- Java / Spring Boot 開發
- DevOps / CI/CD 流程
- 系統架構設計

## 語言偏好
- 使用繁體中文回應
- 程式碼註解使用英文
- 專有名詞保留原文

## 限制
- 不得修改生產環境設定
- 不得刪除 Git 分支
- 敏感資訊必須遮蔽

## 輸出格式
- 程式碼使用 Markdown Code Block
- 表格使用 Markdown 表格
- 重要警告使用 ⚠️ 標記
```

#### 6.6.2 Personality 切換

```bash
# 設定人格
/personality professional    # 專業模式
/personality friendly        # 友善模式
/personality concise         # 精簡模式

# 自訂人格（寫入 SOUL.md）
> 請調整你的人格為：專業但友善的金融科技顧問
```

#### 6.6.3 多 Profile SOUL.md 管理

```bash
# 每個 Profile 有獨立 SOUL.md
~/.hermes/profiles/
├── default/
│   └── SOUL.md          # 預設人格
├── team-backend/
│   └── SOUL.md          # 後端團隊：專注 Java / Spring Boot
├── team-devops/
│   └── SOUL.md          # DevOps：專注部署 / 監控
└── customer-service/
    └── SOUL.md          # 客服：親切有禮、遵守合規
```

> **企業建議**：為不同團隊或場景建立專屬 Profile + SOUL.md，確保 Agent 在各場景中表現一致。金融客服場景務必在 SOUL.md 中明確列出合規限制。

### 6.8 Context Files（專案上下文檔案）

Context Files 是放在專案目錄中的特殊檔案，Agent 會在每次對話啟動時自動載入，確保輸出始終符合專案規範。

#### 6.7.1 支援的 Context Files

| 檔案 | 位置 | 用途 |
|------|------|------|
| `AGENTS.md` | 專案根目錄 | 專案上下文、規範、技術棧說明 |
| `SOUL.md` | `~/.hermes/` 或 Profile 目錄 | Agent 人格定義 |
| `MEMORY.md` | `~/.hermes/memories/` | 持久化知識與經驗 |
| `USER.md` | `~/.hermes/memories/` | 使用者偏好記錄 |
| `.hermesignore` | 專案根目錄 | 排除 Agent 不應讀取的檔案 |

#### 6.7.2 AGENTS.md 最佳實踐

```markdown
# AGENTS.md

## 專案概述
[簡短描述專案目標和技術棧]

## 技術規範
[列出程式語言版本、框架、套件管理器等]

## 程式碼風格
[定義 coding standard、命名慣例、註解要求]

## 安全要求
[列出安全合規要求、禁止的操作]

## Git 工作流
[定義分支策略、commit 格式、PR 規範]

## 測試要求
[定義測試框架、覆蓋率目標]

## 部署流程
[定義 CI/CD 流程、環境配置]
```

#### 6.7.3 .hermesignore 範例

```
# .hermesignore — 排除 Agent 不應讀取的檔案
*.env
**/secrets/**
**/node_modules/**
**/.git/**
**/target/**
**/build/**
*.log
credentials.yaml
```

> **實務案例**：某團隊在 AGENTS.md 中詳細定義了 Spring Boot 開發規範，Agent 在生成程式碼時自動遵循 Google Java Style、自動加入 JavaDoc、自動使用 Parameterized Query，大幅減少 Code Review 的修改量。

### 6.9 Plugin 系統（v0.12.0+ / v0.13.0 擴充）

v0.12.0 將 Gateway 重構為 **Pluggable Gateway**，第三方 Plugin 可以擴展平台、工具、Dashboard 元件等，形成完整的生態系統。

#### 6.9.1 Plugin 架構

```mermaid
graph TB
    subgraph "Plugin Host（Gateway）"
        REGISTRY["Plugin Registry"]
        LIFECYCLE["Lifecycle Manager<br/>install → init → start → stop"]
    end
    
    subgraph "Plugin 類型"
        PLAT["platform-*<br/>通訊平台"]
        MODEL["model-*<br/>模型 Provider"]
        TOOL["tool-*<br/>工具擴展"]
        DASH["dashboard-*<br/>Dashboard Widget"]
        OBS["observability-*<br/>可觀測性"]
    end
    
    REGISTRY --> PLAT
    REGISTRY --> MODEL
    REGISTRY --> TOOL
    REGISTRY --> DASH
    REGISTRY --> OBS
```

#### 6.9.2 內建 Plugin 清單（v0.12.0 + v0.13.0）

| Plugin | 類型 | 說明 |
|--------|------|------|
| `plugins/platform-teams` | 平台 | Microsoft Teams 整合（第 19 平台）|
| `plugins/platform-yuanbao` | 平台 | 騰訊元寶整合（第 18 平台）|
| `plugins/model-lmstudio` | 模型 | LM Studio first-class Provider |
| `plugins/model-azure-foundry` | 模型 | Azure AI Foundry Provider |
| `plugins/model-tencent` | 模型 | Tencent Tokenhub Provider |
| `plugins/tool-spotify` | 工具 | Spotify 原生整合（7 工具 + PKCE OAuth）|
| `plugins/tool-google-meet` | 工具 | Google Meet 加入/轉錄/發言 |
| `plugins/tool-comfyui` | 工具 | ComfyUI v5 圖像生成（預設內建）|
| `plugins/tool-touchdesigner` | 工具 | TouchDesigner-MCP（預設內建）|
| `plugins/observability-langfuse` | 可觀測性 | Langfuse tracing + metrics |
| `plugins/hermes-achievements` | 擴展 | 成就系統 gamification |
| **`plugins/platform-google-chat`** | **平台** | **Google Chat 整合（v0.13.0 第 20 平台）+ 通用 Platform-Plugin Hooks** |
| **`plugins/model-providers/*`** | **模型** | **ProviderProfile ABC — Provider 可插拔化（v0.13.0）** |

#### 6.9.2.1 v0.13.0 Plugin 新功能

| 功能 | 說明 |
|------|------|
| **`transform_llm_output` Hook** | 新生命週期掛鉤：在 LLM 輸出到達對話前進行 reshape / filter。適用於上下文窗口壓縮器和內容過濾器 |
| **`env_enablement_fn` Hook** | 平台 Plugin 可定義環境變數啟用函式（IRC、Teams 已遷移） |
| **`cron_deliver_env_var` Hook** | Cron 交付環境變數掛鉤 |
| **ProviderProfile ABC** | `plugins/model-providers/` 目錄下的第三方 Provider 可插拔，無需修改核心程式碼 |
| **Dashboard Plugins 頁面** | 圖形化管理 Plugin：啟用/停用、查看認證狀態 |
| **SRI 完整性** | Dashboard Plugin 腳本採用 Subresource Integrity 驗證 |

```python
# plugins/my-output-filter/__init__.py — 使用 transform_llm_output hook
from hermes.plugins import PluginBase, hook

class OutputFilterPlugin(PluginBase):
    name = "my-output-filter"
    version = "1.0.0"
    
    @hook("transform_llm_output")
    async def filter_output(self, output: str) -> str:
        """在 LLM 輸出送入對話前進行過濾/變形"""
        # 例如：移除敏感資訊、壓縮上下文
        return output.replace("INTERNAL_SECRET", "[REDACTED]")
```

#### 6.9.3 Spotify 整合範例

```bash
# 安裝 Spotify Plugin（v0.12.0 預設已內建）
hermes plugins enable spotify

# 首次使用會啟動 PKCE OAuth 流程
# 瀏覽器自動開啟 Spotify 授權頁面

# 之後可直接對 Agent 下達音樂指令：
> 播放一些適合寫程式的 Lo-fi 音樂
> 暫停播放
> 建立一個名為「Coding Vibes」的播放清單
```

**提供的 7 個工具**：
- `spotify_play` — 播放音樂/播放清單
- `spotify_pause` — 暫停播放
- `spotify_next` / `spotify_prev` — 上/下一首
- `spotify_search` — 搜尋音樂
- `spotify_create_playlist` — 建立播放清單
- `spotify_current` — 查看當前播放

#### 6.9.4 Google Meet 整合

```yaml
# config.yaml
plugins:
  google_meet:
    enabled: true
    credentials: "${GOOGLE_MEET_CREDENTIALS}"  # OAuth 或 Service Account
```

功能：加入會議、即時轉錄、語音發言、會後自動產出會議摘要與行動項目。

#### 6.9.5 自訂 Plugin 開發

```python
# plugins/my-custom-tool/__init__.py
from hermes.plugins import PluginBase, tool

class MyCustomPlugin(PluginBase):
    name = "my-custom-tool"
    version = "1.0.0"
    
    @tool(description="執行自訂業務邏輯")
    async def my_action(self, param: str) -> str:
        # 實作你的工具邏輯
        return f"執行完成: {param}"
```

> **企業建議**：善用 Plugin 系統將內部系統（JIRA、Confluence、內部 API）封裝為 Plugin，讓 Agent 能直接操作企業工具鏈。

---

## 第七章：Voice Mode（語音模式）

### 7.1 語音模式概述

Hermes Agent v0.3.0+ 支援完整的語音互動能力，可在 CLI、Telegram、Discord 等平台進行即時語音對話。語音模式整合 STT（語音轉文字）和 TTS（文字轉語音）雙向轉換，適用於免手動操作場景。

```mermaid
graph LR
    subgraph "語音輸入"
        MIC[麥克風 / 語音備忘錄]
        STT[STT 引擎<br/>Whisper / Voxtral / Deepgram]
    end
    
    subgraph "Agent 處理"
        AGENT[Hermes Agent<br/>理解 → 規劃 → 執行]
    end
    
    subgraph "語音輸出"
        TTS[TTS 引擎<br/>OpenAI TTS / ElevenLabs / MiniMax / Piper]
        SPK[喇叭 / 語音訊息]
    end
    
    MIC --> STT
    STT --> AGENT
    AGENT --> TTS
    TTS --> SPK
```

### 7.2 支援的 STT / TTS 提供者

#### 7.2.1 STT（語音轉文字）提供者

| Provider | 說明 | 語言支援 | 特點 |
|----------|------|----------|------|
| OpenAI Whisper | OpenAI 官方 STT | 99+ 語言 | 高準確率、即時串流 |
| Voxtral Transcribe | Mistral AI 最新 STT | 多語言 | v0.8.0+ 新增、高效能 |
| Deepgram | 企業級 STT | 30+ 語言 | 低延遲、即時串流 |
| 本地 Whisper | 自託管 Whisper 模型 | 99+ 語言 | 離線可用、隱私保護 |

#### 7.2.2 TTS（文字轉語音）提供者

| Provider | 說明 | 語音選擇 | 特點 |
|----------|------|----------|------|
| OpenAI TTS | OpenAI 官方 TTS | 6 種語音 | 自然流暢 |
| ElevenLabs | 高品質語音合成 | 自訂語音 | 語音克隆、高擬真度 |
| MiniMax Speech 2.8 | MiniMax TTS | 預設語音 | v0.8.0 新增 |
| **Piper TTS** | 本地開源 TTS | 多種語音模型 | **v0.12.0 新增**，完全離線、零成本、低延遲 |
| **xAI Custom Voices** | xAI 語音克隆 TTS | **自訂克隆語音** | **v0.13.0 新增**，支援語音克隆（voice cloning）|

### 7.3 CLI 語音互動

```bash
# 啟用語音模式
hermes --voice

# 或在對話中切換
/voice on     # 開啟語音
/voice off    # 關閉語音

# 設定 STT/TTS Provider
hermes config set voice.stt_provider openai
hermes config set voice.tts_provider elevenlabs
```

```yaml
# ~/.hermes/config.yaml
voice:
  enabled: false                # 預設關閉
  stt_provider: openai          # openai / voxtral / deepgram / local
  tts_provider: openai          # openai / elevenlabs / minimax / piper / xai
  
  openai:
    stt_model: whisper-1
    tts_model: tts-1
    tts_voice: alloy             # alloy / echo / fable / onyx / nova / shimmer
  
  elevenlabs:
    api_key: "${ELEVENLABS_API_KEY}"
    voice_id: "your-voice-id"
  
  # xAI Custom Voices（v0.13.0 新增）
  xai:
    api_key: "${XAI_API_KEY}"
    voice_id: "your-cloned-voice-id"  # 語音克隆 ID
  
  voxtral:
    api_key: "${MISTRAL_API_KEY}"   # Mistral AI API Key
  
  # v0.12.0: Piper 本地 TTS
  piper:
    model: "zh_CN-huayan-medium"  # 本地模型名稱
    speaker_id: 0                 # 說話者 ID
    # 模型存放於 ~/.hermes/tts/piper/models/
    # 首次使用自動下載
```

#### 7.3.1 Pluggable TTS Provider Registry（v0.12.0+）

v0.12.0 將 TTS 架構重構為可插拔式註冊表，允許第三方 Plugin 新增 TTS 引擎：

```yaml
# 自訂 TTS Provider
tts:
  providers:
    my_custom_tts:
      plugin: "plugins/tts-my-engine"
      endpoint: "http://localhost:5500/api/tts"
      voice: "default"
```

### 7.4 Telegram / Discord 語音互動

Telegram 和 Discord 支援語音備忘錄自動轉錄：

```
使用者：[傳送語音備忘錄]
Agent：
  1. 自動用 STT 轉錄語音為文字
  2. 處理轉錄後的文字指令
  3. 以文字或語音回應（依設定）
```

**Telegram 設定**：

```yaml
# config.yaml
gateway:
  platforms:
    telegram:
      enabled: true
      voice_transcription: true    # 自動轉錄語音備忘錄
      voice_response: false        # 是否以語音回應
```

### 7.5 Discord Voice Channel 即時語音

Hermes 支援加入 Discord Voice Channel 進行即時語音對話：

```bash
# Discord Voice Channel 設定
gateway:
  platforms:
    discord:
      enabled: true
      voice_channel:
        enabled: true
        auto_join: false          # 是否自動加入語音頻道
        wake_word: "hermes"       # 喚醒詞
```

**使用流程**：
1. 在 Discord 邀請 Hermes Bot 加入語音頻道
2. Bot 監聽語音並使用 STT 轉錄
3. 偵測到喚醒詞或被 @mention 時開始處理
4. 使用 TTS 語音回應

### 7.6 企業語音整合建議

| 場景 | 建議配置 | 說明 |
|------|----------|------|
| 開發團隊 | CLI Voice + Whisper | 邊 coding 邊語音下指令 |
| 客服系統 | Telegram Voice + ElevenLabs | 自然語音客服回應 |
| 會議記錄 | Discord VC + Voxtral | 即時會議記錄與摘要 |
| 離線環境 | Local Whisper + Local TTS | 無需網路的語音互動 |

> **安全提醒**：語音資料可能包含敏感資訊。企業環境建議使用本地 Whisper 模型或確保語音資料傳輸加密（TLS）。不要在語音中傳輸密碼、API Key 等敏感資訊。

---

## 第八章：Web Application 整合

### 8.1 整合架構設計

```mermaid
graph TB
    subgraph "Frontend（前端層）"
        VUE[Vue 3 / React<br/>Chat UI + Dashboard]
    end
    
    subgraph "Backend（後端層）"
        API[Spring Boot / FastAPI<br/>業務邏輯 API]
        AGENT_SVC[Agent Service<br/>Hermes 封裝層]
    end
    
    subgraph "Hermes Agent Layer"
        HERMES[Hermes Agent<br/>CLI / API Mode]
        GW[Hermes Gateway<br/>多平台消息]
        MCP_SRV[MCP Server<br/>暴露業務工具]
    end
    
    subgraph "Data Layer"
        BIZ_DB[(Business DB<br/>PostgreSQL)]
        AGENT_DB[(Agent DB<br/>SQLite / Vector)]
        CACHE[(Redis<br/>Cache + Queue)]
    end
    
    VUE -->|REST/WebSocket| API
    VUE -->|SSE Stream| AGENT_SVC
    API --> BIZ_DB
    API --> CACHE
    
    AGENT_SVC -->|HTTP API / CLI| HERMES
    HERMES --> GW
    HERMES -->|MCP Protocol| MCP_SRV
    MCP_SRV --> BIZ_DB
    
    HERMES --> AGENT_DB
```

### 8.2 FastAPI 後端整合

#### 8.2.1 Agent-as-a-Service API

```python
# agent_service.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import subprocess
import asyncio
import json

app = FastAPI(title="Hermes Agent Service", version="1.0.0")

class AgentRequest(BaseModel):
    """Agent 請求模型"""
    message: str
    session_id: str | None = None
    profile: str = "default"
    model: str | None = None

class AgentResponse(BaseModel):
    """Agent 回應模型"""
    response: str
    session_id: str
    tokens_used: int
    tools_called: list[str]

@app.post("/api/agent/chat", response_model=AgentResponse)
async def chat(request: AgentRequest):
    """
    與 Hermes Agent 進行對話
    
    - **message**: 使用者訊息
    - **session_id**: 對話 Session ID（可選，用於延續對話）
    - **profile**: Agent Profile（預設 default）
    - **model**: 指定模型（可選）
    """
    cmd = ["hermes", "chat", "--message", request.message]
    
    if request.session_id:
        cmd.extend(["--session", request.session_id])
    if request.profile != "default":
        cmd.extend(["--profile", request.profile])
    if request.model:
        cmd.extend(["--model", request.model])
    
    try:
        result = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=stderr.decode())
        
        output = json.loads(stdout.decode())
        return AgentResponse(
            response=output["response"],
            session_id=output["session_id"],
            tokens_used=output.get("tokens_used", 0),
            tools_called=output.get("tools_called", [])
        )
    except json.JSONDecodeError:
        return AgentResponse(
            response=stdout.decode(),
            session_id=request.session_id or "new",
            tokens_used=0,
            tools_called=[]
        )

@app.post("/api/agent/stream")
async def stream_chat(request: AgentRequest):
    """SSE 串流模式 - 即時回傳 Agent 回應"""
    async def generate():
        cmd = ["hermes", "chat", "--message", request.message, "--stream"]
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        async for line in process.stdout:
            text = line.decode().strip()
            if text:
                yield f"data: {json.dumps({'content': text})}\n\n"
        
        yield f"data: {json.dumps({'done': True})}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")

@app.get("/api/agent/skills")
async def list_skills():
    """列出所有可用技能"""
    result = subprocess.run(
        ["hermes", "skills", "--json"],
        capture_output=True, text=True
    )
    return json.loads(result.stdout)

@app.post("/api/agent/skill/{skill_name}")
async def execute_skill(skill_name: str, request: AgentRequest):
    """執行指定技能"""
    message = f"/{skill_name} {request.message}"
    request.message = message
    return await chat(request)
```

#### 8.2.2 啟動 Agent Service

```bash
# 安裝依賴
pip install fastapi uvicorn pydantic

# 啟動服務
uvicorn agent_service:app --host 0.0.0.0 --port 8000 --reload

# API 文件：http://localhost:8000/docs
```

### 8.3 Spring Boot 後端整合

#### 8.3.1 Agent Client 封裝

```java
/**
 * Hermes Agent 客戶端
 * 透過 HTTP 呼叫 Agent Service 或直接呼叫 CLI
 */
@Service
@Slf4j
public class HermesAgentClient {

    private final WebClient webClient;
    
    @Value("${hermes.agent.url:http://localhost:8000}")
    private String agentUrl;

    public HermesAgentClient(WebClient.Builder builder) {
        this.webClient = builder.baseUrl(agentUrl).build();
    }

    /**
     * 與 Agent 對話
     * @param message 使用者訊息
     * @param sessionId Session ID（可選）
     * @return Agent 回應
     */
    public Mono<AgentResponse> chat(String message, String sessionId) {
        AgentRequest request = new AgentRequest();
        request.setMessage(message);
        request.setSessionId(sessionId);
        
        return webClient.post()
            .uri("/api/agent/chat")
            .bodyValue(request)
            .retrieve()
            .bodyToMono(AgentResponse.class)
            .doOnError(e -> log.error("Agent 呼叫失敗", e))
            .onErrorResume(e -> Mono.just(
                AgentResponse.error("Agent 暫時無法回應，請稍後再試")
            ));
    }

    /**
     * SSE 串流對話
     */
    public Flux<String> streamChat(String message) {
        AgentRequest request = new AgentRequest();
        request.setMessage(message);
        
        return webClient.post()
            .uri("/api/agent/stream")
            .bodyValue(request)
            .retrieve()
            .bodyToFlux(String.class);
    }

    /**
     * 執行指定技能
     */
    public Mono<AgentResponse> executeSkill(String skillName, String message) {
        AgentRequest request = new AgentRequest();
        request.setMessage(message);
        
        return webClient.post()
            .uri("/api/agent/skill/{skill}", skillName)
            .bodyValue(request)
            .retrieve()
            .bodyToMono(AgentResponse.class);
    }
}
```

#### 8.3.2 REST Controller

```java
/**
 * 智能助手 API Controller
 */
@RestController
@RequestMapping("/api/assistant")
@RequiredArgsConstructor
public class AssistantController {

    private final HermesAgentClient agentClient;

    @PostMapping("/chat")
    public Mono<ResponseEntity<AgentResponse>> chat(
            @RequestBody @Valid ChatRequest request) {
        return agentClient.chat(request.getMessage(), request.getSessionId())
            .map(ResponseEntity::ok);
    }

    @PostMapping("/stream")
    public Flux<ServerSentEvent<String>> streamChat(
            @RequestBody @Valid ChatRequest request) {
        return agentClient.streamChat(request.getMessage())
            .map(content -> ServerSentEvent.<String>builder()
                .data(content)
                .build());
    }

    @PostMapping("/code-review")
    public Mono<ResponseEntity<AgentResponse>> codeReview(
            @RequestBody @Valid CodeReviewRequest request) {
        String prompt = String.format(
            "請審查以下程式碼的安全性和品質：\n```java\n%s\n```",
            request.getCode()
        );
        return agentClient.executeSkill("code-review", prompt)
            .map(ResponseEntity::ok);
    }
}
```

### 8.4 前端整合（Vue / React）

#### 8.4.1 Vue 3 Chat 組件

```vue
<template>
  <div class="agent-chat">
    <div class="messages" ref="messagesRef">
      <div v-for="msg in messages" :key="msg.id"
           :class="['message', msg.role]">
        <div class="content" v-html="renderMarkdown(msg.content)"></div>
        <div class="meta">
          <span v-if="msg.tokens">{{ msg.tokens }} tokens</span>
          <span v-if="msg.tools?.length">
            工具：{{ msg.tools.join(', ') }}
          </span>
        </div>
      </div>
      <div v-if="isStreaming" class="message assistant streaming">
        <div class="content">{{ streamContent }}</div>
        <span class="typing-indicator">▋</span>
      </div>
    </div>
    
    <div class="input-area">
      <textarea v-model="input" 
                @keydown.enter.ctrl="sendMessage"
                placeholder="輸入訊息（Ctrl+Enter 發送）"
                rows="3"></textarea>
      <button @click="sendMessage" :disabled="isStreaming">
        {{ isStreaming ? '回應中...' : '發送' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { marked } from 'marked'

const messages = ref([])
const input = ref('')
const isStreaming = ref(false)
const streamContent = ref('')
const sessionId = ref(null)
const messagesRef = ref(null)

const AGENT_API = '/api/agent'

async function sendMessage() {
  if (!input.value.trim() || isStreaming.value) return
  
  const userMsg = input.value.trim()
  input.value = ''
  
  messages.value.push({
    id: Date.now(),
    role: 'user',
    content: userMsg
  })
  
  isStreaming.value = true
  streamContent.value = ''
  
  try {
    const response = await fetch(`${AGENT_API}/stream`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: userMsg,
        session_id: sessionId.value
      })
    })
    
    const reader = response.body.getReader()
    const decoder = new TextDecoder()
    
    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      
      const text = decoder.decode(value)
      const lines = text.split('\n')
      
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = JSON.parse(line.slice(6))
          if (data.done) break
          streamContent.value += data.content
        }
      }
      
      await nextTick()
      scrollToBottom()
    }
    
    messages.value.push({
      id: Date.now(),
      role: 'assistant',
      content: streamContent.value
    })
  } catch (error) {
    messages.value.push({
      id: Date.now(),
      role: 'error',
      content: `錯誤：${error.message}`
    })
  } finally {
    isStreaming.value = false
    streamContent.value = ''
  }
}

function renderMarkdown(text) {
  return marked.parse(text || '')
}

function scrollToBottom() {
  if (messagesRef.value) {
    messagesRef.value.scrollTop = messagesRef.value.scrollHeight
  }
}
</script>
```

### 8.5 Agent-as-a-Service API 設計

#### 8.5.1 API 規格

| Method | Endpoint | 說明 |
|--------|----------|------|
| POST | `/api/agent/chat` | 對話（同步回應）|
| POST | `/api/agent/stream` | 對話（SSE 串流）|
| GET | `/api/agent/skills` | 列出技能 |
| POST | `/api/agent/skill/{name}` | 執行技能 |
| GET | `/api/agent/sessions` | 列出對話歷史 |
| GET | `/api/agent/sessions/{id}` | 取得對話詳情 |
| DELETE | `/api/agent/sessions/{id}` | 刪除對話 |
| GET | `/api/agent/usage` | Token 使用統計 |
| POST | `/api/agent/memory/search` | 搜尋記憶 |

#### 8.5.2 整合架構圖

```mermaid
graph LR
    subgraph "Client Apps"
        WEB_APP[Web Application<br/>Vue / React]
        MOBILE[Mobile App<br/>React Native]
        BOT[Chat Bot<br/>Telegram / Discord]
    end
    
    subgraph "API Gateway"
        NGINX[Nginx / Kong<br/>Rate Limit + Auth]
    end
    
    subgraph "Agent Service Cluster"
        SVC1[Agent Service 1<br/>Profile: general]
        SVC2[Agent Service 2<br/>Profile: code-review]
        SVC3[Agent Service 3<br/>Profile: security]
    end
    
    subgraph "Hermes Instances"
        H1[Hermes Agent<br/>General]
        H2[Hermes Agent<br/>Code Expert]
        H3[Hermes Agent<br/>Security Expert]
    end
    
    WEB_APP --> NGINX
    MOBILE --> NGINX
    BOT --> NGINX
    
    NGINX --> SVC1
    NGINX --> SVC2
    NGINX --> SVC3
    
    SVC1 --> H1
    SVC2 --> H2
    SVC3 --> H3
```

> **最佳實踐**：企業 Web 整合建議使用 Agent Service 中間層（FastAPI/Spring Boot），而非直接暴露 Hermes CLI。這樣可以：（1）統一認證與授權（2）加入請求限流（3）整合業務邏輯（4）多實例負載平衡。

---

## 第九章：企業級最佳實踐

### 9.1 安全性設計

#### 9.1.1 API Key 管理

| 層級 | 做法 |
|------|------|
| 開發環境 | `.env` 檔案（加入 `.gitignore`）|
| CI/CD | GitHub Secrets / Vault |
| 生產環境 | HashiCorp Vault / AWS Secrets Manager / **Bitwarden Secrets Manager**（v0.15.0） |
| 旋轉策略 | 每 90 天輪換 API Key |

> **v0.15.0 推薦**：使用 Bitwarden Secrets Manager，一個 bootstrap token 取代所有散落的 API Key（詳見 1.4.17 節）。

```bash
# 不要這樣做 ❌
export ANTHROPIC_API_KEY=sk-ant-real-key-here

# 應該這樣做 ✅
# .env 檔案（不入版控）
ANTHROPIC_API_KEY=${vault:secret/hermes/anthropic-key}
```

#### 9.1.2 指令審批（Command Approval）

```yaml
# ~/.hermes/config.yaml
security:
  command_approval: smart      # 推薦企業使用

  # 永久白名單（無需審批）
  allowed_commands:
    - "git status"
    - "git diff"
    - "git log"
    - "mvn test"
    - "mvn verify"
    - "npm test"
    - "python -m pytest"
    - "ls"
    - "cat"
    - "grep"
  
  # 永久黑名單（永遠需要審批）
  # rm -rf, git push --force, DROP TABLE 等自動觸發
```

**審批模式比較**：

| 模式 | 說明 | 適用環境 |
|------|------|----------|
| `always` | 所有指令都需審批 | 高安全環境（銀行核心系統）|
| `smart` | 智慧判斷，危險指令要求審批 | 一般企業（推薦）|
| `never` | 不審批（白名單仍生效）| 信任環境 |
| `yolo` | 完全不審批（`--yolo` flag）| 僅限開發測試 |

#### 9.1.3 MCP 安全

- **OAuth 2.1 PKCE**（v0.5.0+）：所有 MCP 伺服器連線支援標準 OAuth 認證
- **OSV 掃描**：自動檢測 MCP 套件是否有已知漏洞
- **工具過濾**：可限制 MCP 伺服器暴露給 Agent 的工具
- **OAuth TOCTOU 關閉**（v0.13.0）：MCP OAuth 憑證儲存的時間競爭窗口已修正
- **SSE Transport OAuth 轉發**（v0.13.0）：SSE 連線自動轉發 OAuth 認證

#### 9.1.4 安全強化（v0.5.0 — v0.13.0 持續強化）

| 防護項目 | 實作 |
|----------|------|
| SSRF 防護 | 合併 SSRF 保護，阻擋內網存取 |
| Timing Attack | 計時攻擊緩解 |
| Tar Traversal | tar 解壓路徑穿越防護 |
| Credential Leakage | 憑證洩露防護 |
| Cross-session Isolation | 跨 Session 隔離 |
| Cron Path Traversal | Cron 路徑穿越防護 |
| Workdir Sanitization | 所有終端後端的工作目錄清理 |
| Secret Exfiltration Blocking | 瀏覽器 URL 與 LLM 回應掃描機密模式（v0.7.0+） |
| Shell Injection | Sandbox 寫入的 Shell 注入中和化（v0.9.0+） |
| Git Argument Injection | Git 參數注入防護（v0.9.0+） |
| **Hardline Blocklist** | 不可恢復指令永久封鎖清單（v0.12.0） |
| **Secret Redaction 預設關閉** | 避免 patch 損壞，需手動啟用（v0.12.0） |
| **Secret Redaction 預設開啟** | **v0.13.0 翻轉預設：Redaction 現為預設開啟**，確保機密不外洩 |
| **Discord 角色白名單 Guild 隔離** | 修正 CVSS 8.1 跨 Guild DM 繞過漏洞，`DISCORD_ALLOWED_ROLES` 現限定原始 Guild（v0.13.0） |
| **WhatsApp 拒絕陌生人** | 預設拒絕未知聯絡人訊息，不在自聊中回應（v0.13.0） |
| **MCP OAuth TOCTOU** | 關閉 MCP OAuth 憑證儲存的時間競爭窗口（v0.13.0） |
| **auth.json TOCTOU** | 關閉 CLI 憑證寫入的時間競爭窗口（v0.13.0） |
| **Browser SSRF Floor** | 強制雲端元資料 SSRF 底線保護（v0.13.0） |
| **Cron Prompt Injection** | 掃描已組裝的提示（含 Skill 內容）檢測 Prompt Injection（v0.13.0） |
| **`hermes debug share` 遮蔽** | 上傳時自動遮蔽日誌內容中的機密（v0.13.0） |
| **檔案權限** | `.env` / `auth.json` / `state.db` 還原為 0600 權限（v0.13.0） |
| **Dashboard SRI** | Dashboard Plugin 腳本採用 Subresource Integrity 完整性驗證（v0.13.0） |
| **Meet Server** | Node 伺服器綁定 localhost，Token 檔案限制 owner read（v0.13.0） |
| **Sensitive-write 擴展** | 敏感寫入目標擴展覆蓋 Shell RC 和憑證檔案（v0.13.0） |
| **YOLO Mode 強化** | 強化 YOLO 模式環境變數解析，防止引號布林值繞過（v0.13.0） |
| **OSV-Scanner CI** | CI 加入 OSV-Scanner + Dependabot（僅 GitHub Actions）（v0.13.0） |
| **Sudo Brute-force 阻擋** | 阻擋 sudo 暴力破解嘗試（v0.14.0） |
| **Plugin `ctx.llm` + `tool_override`** | 插件可覆寫工具行為與存取 LLM（v0.14.0，需信任 Plugin） |
| **Promptware 防禦** | Brainworm-class 攻擊阻擋：threat patterns + 記憶載入時掃描 + tool-result delimiters（v0.15.0） |
| **bundled `security-guidance` Plugin** | 預設啟用的安全指引 Plugin，提供安全最佳實踐提示（v0.15.0） |
| **`hermes audit`** | OSV.dev 供應鏈審計子指令，掃描所有依賴漏洞（v0.15.0） |
| **mTLS for MCP** | MCP 伺服器支援雙向 TLS 認證（v0.15.0） |
| **xAI `base_url` 洩漏防護** | 防止 xAI base_url 透過工具呼叫洩漏（v0.15.0） |
| **Docker `--insecure` 顯式 opt-in** | 不安全 Docker 連線改為顯式環境變數啟用（v0.15.1） |

### 9.2 成本控制

#### 9.2.1 Token 成本策略

```mermaid
graph TD
    A[使用者請求] --> B{任務複雜度}
    B -->|簡單| C[免費模型<br/>MiMo v2 Pro / Nous Portal]
    B -->|中等| D[中階模型<br/>Claude Haiku / GPT-4o-mini]
    B -->|複雜| E[高階模型<br/>Claude Sonnet / GPT-4o]
    B -->|極複雜| F[最強模型<br/>o1 / Claude Opus]
    
    C --> G[成本: ~$0]
    D --> H[成本: ~$0.001/次]
    E --> I[成本: ~$0.01/次]
    F --> J[成本: ~$0.1/次]
```

#### 9.2.2 成本控制設定

```yaml
# config.yaml
model:
  provider: anthropic
  model: claude-sonnet-4-20250514

# 使用免費模型做輔助任務
auxiliary:
  provider: nous
  model: mimo-v2-pro     # 免費！

# Context 壓縮策略
context:
  auto_compress: true
  compress_threshold: 0.8  # 上下文使用 80% 時觸發壓縮
```

#### 9.2.3 成本監控

```bash
# 查看使用量
/usage

# 查看 N 天內的使用洞察
/insights --days 7

# 範例輸出：
# 過去 7 天：
# - 總 Token：125,430
# - 估計成本：$2.35
# - 對話數：45
# - 技能使用：12 次
# - 最常用工具：execute_command(38%), write_file(25%)
```

### 9.3 效能優化

#### 9.3.1 Context Compaction（上下文壓縮）

```bash
# 手動壓縮
/compress

# 自動壓縮（config.yaml）
context:
  auto_compress: true
  compress_threshold: 0.8
```

**Token 預算尾部保護**（v0.8.0 新增）：壓縮時優先保留最近的工具結果和使用者訊息。

#### 9.3.2 Cold-start 效能優化（v0.12.0 — v0.15.0 持續優化）

各版本冷啟動效能提升：

```bash
# v0.11.0: ~2.1s 冷啟動
# v0.12.0: ~0.9s 冷啟動（-57%）
# v0.14.0: 再快 ~19 秒（Cold-start 效能浪潮）
# v0.15.0: 47% fewer per-turn function calls
#          `hermes --version` 快 63%
#          Termux: 2.9s → 0.8s
hermes  # 幾乎即時啟動
```

**v0.15.0 The Big Refactor 效能影響**：
- `run_agent.py` 從 16,083 行重構為 3,821 行（-76%），拆分為 14 個 `agent/*` 模組
- 每回合函數呼叫減少 47%
- `session_search` 重建：無 LLM、免費、4,500 倍快速（~20ms vs ~90s）

#### 9.3.3 Configurable Prompt Cache TTL（v0.12.0）

```yaml
# config.yaml
prompt_caching:
  cache_ttl: 300          # 預設 5 分鐘（秒）
  # cache_ttl: 3600       # 可設為 1 小時（opt-in）
  # 減少重複 System Prompt 的 Token 消耗
```

#### 9.3.4 Programmatic Tool Calling

使用 `execute_code` 將多步驟操作壓縮為單次推理呼叫：

```bash
# 傳統方式（多次推理，高 Token 消耗）
Agent → read_file(a.java) → read_file(b.java) → read_file(c.java) → 分析
# 4 次推理 = 4x Token 成本

# Programmatic 方式（單次推理，低 Token 消耗）
Agent → execute_code("讀取所有 .java 並分析") → 結果
# 1 次推理 + 本地執行 = 1x Token 成本
```

#### 9.3.3 非同步處理

```bash
# 背景任務 + 自動通知（v0.8.0 新增 notify_on_complete）
> 在背景執行完整測試套件，完成後通知我

# Agent 使用 execute_command 的 background + notify_on_complete
# 測試完成後自動通知到 CLI / Telegram / Discord
```

#### 9.3.4 Subagent 平行化

```bash
# 委派子代理平行處理，減少總等待時間
> 請同時做以下三件事：
> 1. 搜尋最新的 Spring Boot 安全修補
> 2. 掃描 src/ 中的程式碼品質問題
> 3. 檢查 Docker Compose 配置是否正確

# 三個 subagent 平行執行
# 總時間 ≈ max(task1, task2, task3) 而非 sum(task1+task2+task3)
```

### 9.4 Logging / Monitoring

#### 9.4.1 集中式日誌（v0.8.0）

```bash
# Hermes 自動寫入日誌
~/.hermes/logs/agent.log    # INFO+ 級別
~/.hermes/logs/errors.log   # WARNING+ 級別

# 即時查看日誌
hermes logs                  # tail -f agent.log
hermes logs --errors         # 只看錯誤
hermes logs --filter "tool"  # 過濾特定關鍵字
```

#### 9.4.2 與 ELK Stack 整合

```yaml
# filebeat.yml
filebeat.inputs:
  - type: log
    paths:
      - /root/.hermes/logs/agent.log
    json.keys_under_root: true
    fields:
      service: hermes-agent
      environment: production

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
  index: "hermes-agent-%{+yyyy.MM.dd}"
```

#### 9.4.3 與 Prometheus 整合

```python
# 自訂 Prometheus metrics exporter
from prometheus_client import Counter, Histogram, start_http_server

agent_requests = Counter(
    'hermes_agent_requests_total',
    'Total agent requests',
    ['status', 'model']
)

token_usage = Histogram(
    'hermes_agent_tokens_used',
    'Tokens used per request',
    buckets=[100, 500, 1000, 5000, 10000, 50000]
)

tool_calls = Counter(
    'hermes_agent_tool_calls_total',
    'Total tool calls',
    ['tool_name']
)

# 啟動 metrics endpoint
start_http_server(9090)
```

#### 9.4.4 Grafana Dashboard 建議指標

| 指標面板 | 內容 |
|----------|------|
| Request Rate | 每分鐘請求數（by model / profile）|
| Token Usage | 每小時 Token 消耗（by provider）|
| Error Rate | 錯誤率（by error type）|
| Tool Usage | 工具使用排行 |
| Latency | P50 / P95 / P99 回應時間 |
| Cost | 每日 / 每週 / 每月成本趨勢 |
| Active Sessions | 活躍對話數 |
| Skill Usage | 技能使用頻率 |

#### 9.4.5 Langfuse 可觀測性 Plugin（v0.12.0）

v0.12.0 內建 Langfuse observability plugin，提供端到端的 LLM 操作追蹤：

```yaml
# config.yaml
plugins:
  langfuse:
    enabled: true
    public_key: "${LANGFUSE_PUBLIC_KEY}"
    secret_key: "${LANGFUSE_SECRET_KEY}"
    host: "https://cloud.langfuse.com"  # 或自託管
```

**Langfuse 提供**：
- **Trace 追蹤**：每次 Agent 對話的完整呼叫鏈（Prompt → Tools → Response）
- **成本分析**：按模型、使用者、時間段的 Token 成本明細
- **品質評估**：LLM 回應品質的自動與人工評分
- **A/B 測試**：不同 Prompt / Model 的效果比較

### 9.5 錯誤處理與重試機制

#### 9.5.1 Jittered Retry Backoff（v0.8.0）

Hermes v0.8.0 內建指數退避 + 隨機抖動的重試機制：

```
重試間隔 = min(base_delay * 2^attempt + random_jitter, max_delay)

第 1 次重試: ~1s + jitter
第 2 次重試: ~2s + jitter
第 3 次重試: ~4s + jitter
第 4 次重試: ~8s + jitter
最大間隔: 30s
```

#### 9.5.2 Provider Failover

```yaml
# 自動 failover 配置
providers:
  primary: anthropic
  fallback:
    - openrouter
    - nous
  
  # 402 付費失敗 → 切換下一個
  # 429 限流 → 指數退避
  # 500 伺服器錯誤 → 切換下一個
  # OAuth 過期 → 自動刷新
```

#### 9.5.3 企業級錯誤處理建議

| 錯誤場景 | 處理策略 |
|----------|----------|
| API 暫時不可用 | 指數退避重試（最多 4 次）|
| Token 餘額不足（402）| 自動切換 Fallback Provider |
| 速率限制（429）| 指數退避 + Jitter |
| 模型不支援工具呼叫 | 顯示警告，建議切換模型 |
| Context 溢出 | 自動 Compaction |
| 工具執行失敗 | 重試或改用替代工具 |
| 網路中斷 | 自動重連（Gateway 支援）|

> **實務案例**：某金融企業使用 Hermes Agent 做 24/7 自動化監控。透過 Cron 排程每小時檢查系統健康度，搭配 Telegram 通知。Provider Failover 確保即使某個 API 當機，Agent 仍可用備援模型持續運作，系統可用性達 99.9%。

### 9.6 Tips & Best Practices

以下是根據官方文檔和社群經驗整理的最佳實踐清單：

#### 9.6.1 開發效率

| 技巧 | 說明 |
|------|------|
| 使用 AGENTS.md | 在專案根目錄放置 AGENTS.md，Agent 會自動載入專案規範 |
| 善用 Skill 封裝 | 複雜的重複任務封裝為 Skill，一次定義多次使用 |
| 使用 `/compress` | 長對話時定期壓縮上下文，節省 Token 並維持效能 |
| 善用 Subagent | 複雜任務使用 `delegate_task` 平行處理，減少總等待時間 |
| Context Files | 建立完整的 AGENTS.md + SOUL.md，確保輸出品質一致 |
| Programmatic Tool Calling | 使用 `execute_code` 批次操作，將多步驟壓縮為單次推理 |

#### 9.6.2 成本優化

| 技巧 | 節省幅度 | 說明 |
|------|----------|------|
| 免費輔助模型 | ~60% | 使用 Nous Portal mimo-v2-pro 處理壓縮/摘要 |
| 自動壓縮 | ~30% | 設定 `context.auto_compress: true` |
| 模型分級 | ~50% | 簡單任務用小模型，複雜任務用大模型 |
| `/insights` 監控 | - | 定期查看 Token 使用趨勢，識別浪費 |

#### 9.6.3 安全運作

| 技巧 | 說明 |
|------|------|
| `command_approval: smart` | 不要使用 `yolo` 模式在生產環境 |
| 白名單機制 | 明確列出允許的指令，縮小攻擊面 |
| Gateway `allowed_users` | 限制可與 Agent 對話的使用者 |
| API Key 輪換 | 每 90 天輪換，使用 Vault 管理 |
| MCP OAuth | 啟用 OAuth 2.1 PKCE 認證所有 MCP 連線 |
| 日誌審計 | 啟用集中式日誌，定期審計 Agent 行為 |

#### 9.6.4 維運穩定

| 技巧 | 說明 |
|------|------|
| Provider Failover | 至少配置 2 個 Provider |
| `hermes doctor` | 升級後必執行，驗證環境完整性 |
| 備份 `~/.hermes/` | 每日備份 Skills、Memories、Config |
| Health Check | Docker / K8s 配置 `hermes doctor --quick` |
| Profile 隔離 | 不同團隊使用不同 Profile，避免互相干擾 |

---

## 第十章：部署與維運（DevOps）

### 10.1 Docker 部署

#### 10.1.1 生產級 Docker 配置

```dockerfile
# Dockerfile.production
FROM python:3.11-slim AS builder

WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# 安裝 uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# 複製依賴檔案
COPY pyproject.toml uv.lock ./

# 安裝依賴
RUN /root/.cargo/bin/uv pip install --system -e ".[all]"

# --- Production Stage ---
FROM python:3.11-slim

WORKDIR /app

# 複製已安裝的套件
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/bin/node /usr/bin/node

# 複製應用程式
COPY . .

# 非 root 使用者
RUN useradd -m hermes && \
    mkdir -p /home/hermes/.hermes && \
    chown -R hermes:hermes /home/hermes

USER hermes

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD hermes doctor --quick || exit 1

ENTRYPOINT ["hermes"]
```

> ⚠️ **v0.13.0 安全強制**：官方 Docker Image 現**拒絕以 root 身份運行 Gateway**。上述 `USER hermes` 為必要配置。Runtime `node_modules` 目錄會自動 chown 為 `hermes` 使用者。

> 💡 **Docker Dashboard**（v0.13.0）：加入 `HERMES_DASHBOARD=1` 環境變數，Dashboard 會以 Side-process 啟動。加入 `-p 3000:3000` 暴露 Dashboard 連接埠。

#### 10.1.2 Docker Compose 生產部署

```yaml
# docker-compose.production.yml
version: '3.8'

services:
  hermes-agent:
    build:
      context: .
      dockerfile: Dockerfile.production
    container_name: hermes-agent
    restart: unless-stopped
    volumes:
      - hermes-data:/home/hermes/.hermes
      - ./workspace:/workspace
    env_file:
      - .env.production
    ports:
      - "127.0.0.1:8080:8080"
    networks:
      - hermes-net
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2.0'
        reservations:
          memory: 1G
          cpus: '0.5'
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
        max-file: "3"
    healthcheck:
      test: ["CMD", "hermes", "doctor", "--quick"]
      interval: 60s
      timeout: 10s
      retries: 3

  hermes-gateway:
    build:
      context: .
      dockerfile: Dockerfile.production
    container_name: hermes-gateway
    restart: unless-stopped
    command: ["gateway", "start"]
    volumes:
      - hermes-data:/home/hermes/.hermes
    env_file:
      - .env.production
    networks:
      - hermes-net
    depends_on:
      hermes-agent:
        condition: service_healthy

volumes:
  hermes-data:
    driver: local

networks:
  hermes-net:
    driver: bridge
```

### 10.2 Kubernetes 部署

#### 10.2.1 K8s Deployment

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hermes-agent
  labels:
    app: hermes-agent
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hermes-agent
  template:
    metadata:
      labels:
        app: hermes-agent
    spec:
      containers:
        - name: hermes-agent
          image: ghcr.io/your-org/hermes-agent:v0.11.0
          resources:
            requests:
              memory: "1Gi"
              cpu: "500m"
            limits:
              memory: "4Gi"
              cpu: "2000m"
          envFrom:
            - secretRef:
                name: hermes-secrets
          volumeMounts:
            - name: hermes-data
              mountPath: /home/hermes/.hermes
            - name: workspace
              mountPath: /workspace
          livenessProbe:
            exec:
              command: ["hermes", "doctor", "--quick"]
            initialDelaySeconds: 30
            periodSeconds: 60
          readinessProbe:
            exec:
              command: ["hermes", "doctor", "--quick"]
            initialDelaySeconds: 10
            periodSeconds: 30
      volumes:
        - name: hermes-data
          persistentVolumeClaim:
            claimName: hermes-data-pvc
        - name: workspace
          persistentVolumeClaim:
            claimName: workspace-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: hermes-agent-svc
spec:
  selector:
    app: hermes-agent
  ports:
    - port: 8080
      targetPort: 8080
  type: ClusterIP

---
apiVersion: v1
kind: Secret
metadata:
  name: hermes-secrets
type: Opaque
stringData:
  ANTHROPIC_API_KEY: "sk-ant-xxxxx"
  OPENROUTER_API_KEY: "sk-or-xxxxx"
  TELEGRAM_BOT_TOKEN: "12345:ABCdef"
```

#### 10.2.2 PersistentVolumeClaim

```yaml
# k8s/pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: hermes-data-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
```

### 10.3 CI/CD 流程

#### 10.3.1 GitHub Actions Pipeline

```yaml
# .github/workflows/hermes-deploy.yml
name: Hermes Agent Deploy

on:
  push:
    branches: [main]
    paths:
      - 'hermes/**'
      - 'Dockerfile*'
      - 'docker-compose*.yml'

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}/hermes-agent

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -e ".[all,dev]"
      
      - name: Run tests
        run: |
          python -m pytest tests/ -q
      
      - name: Security scan
        run: |
          pip install safety
          safety check

  build-image:
    needs: build-and-test
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          file: Dockerfile.production
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}

  deploy:
    needs: build-image
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Kubernetes
        uses: azure/k8s-deploy@v4
        with:
          manifests: k8s/
          images: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

### 10.4 滾動升級

#### 10.4.1 Kubernetes Rolling Update 策略

```yaml
# k8s/deployment.yaml 的 spec.strategy
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0      # 升級期間不停機
      maxSurge: 1             # 最多多 1 個 Pod
```

#### 10.4.2 Hermes 內建升級

```bash
# 使用內建升級指令
hermes update

# 注意事項（v0.8.0 修正）：
# - 升級不會 kill 正在運行的 gateway service
# - 升級後 bundled skills 會自動同步到所有 profiles
# - 升級後建議執行 hermes doctor 驗證
```

### 10.5 災難復原（DR）

#### 10.5.1 備份策略

| 備份項目 | 路徑 | 頻率 | 方式 |
|----------|------|------|------|
| 設定檔 | `~/.hermes/config.yaml` | 每次修改 | Git 版控 |
| Skills | `~/.hermes/skills/` | 每日 | rsync / S3 |
| Memories | `~/.hermes/memories/` | 每日 | rsync / S3 |
| Sessions DB | `~/.hermes/sessions.db` | 每日 | SQLite backup |
| SOUL.md | `~/.hermes/SOUL.md` | 每次修改 | Git 版控 |
| .env | `~/.hermes/.env` | 每次修改 | Vault |

#### 10.5.2 備份腳本

```bash
#!/bin/bash
# backup-hermes.sh

BACKUP_DIR="/backup/hermes/$(date +%Y%m%d)"
HERMES_HOME="$HOME/.hermes"

mkdir -p "$BACKUP_DIR"

# 備份設定
cp "$HERMES_HOME/config.yaml" "$BACKUP_DIR/"
cp "$HERMES_HOME/SOUL.md" "$BACKUP_DIR/" 2>/dev/null

# 備份 Skills
tar czf "$BACKUP_DIR/skills.tar.gz" -C "$HERMES_HOME" skills/

# 備份 Memories
tar czf "$BACKUP_DIR/memories.tar.gz" -C "$HERMES_HOME" memories/ 2>/dev/null

# 備份 Session DB（SQLite）
sqlite3 "$HERMES_HOME/sessions.db" ".backup '$BACKUP_DIR/sessions.db'"

# 上傳到 S3（可選）
# aws s3 sync "$BACKUP_DIR" "s3://your-bucket/hermes-backup/$(date +%Y%m%d)/"

echo "Backup completed: $BACKUP_DIR"
```

#### 10.5.3 RTO / RPO 建議

| 場景 | RPO 建議 | RTO 建議 | 策略 |
|------|----------|----------|------|
| 開發環境 | 24h | 1h | 每日備份 |
| 測試環境 | 24h | 2h | 每日備份 |
| 生產環境 | 1h | 30min | 多副本 + 即時備份 |
| 金融環境 | 0（零丟失）| 15min | 主從 + 即時同步 |

> **實務案例**：某銀行團隊在 Kubernetes 上部署 Hermes Agent，使用 `ReadWriteMany` PVC 共享 Skills 和 Memories。每日凌晨透過 CronJob 備份到 S3，搭配 Rolling Update 策略實現零停機升級。RTO 目標 15 分鐘，RPO 目標 1 小時。

---

## 第十一章：升級與版本管理

### 11.1 升級策略

#### 11.1.1 版本號規則

Hermes Agent 使用語義化版本（附日期標籤）：

```
v0.8.0 (v2026.4.8)
│ │ │    │    │ │
│ │ │    │    │ └── 日（Day）
│ │ │    │    └──── 月（Month）
│ │ │    └───────── 年（Year）
│ │ └────────────── Patch（修復版本）
│ └──────────────── Minor（功能版本）
└────────────────── Major（大版本）
```

#### 11.1.2 升級流程

```mermaid
graph TD
    A[查看新版本] --> B[閱讀 Release Notes]
    B --> C{是否有破壞性變更?}
    C -->|是| D[在測試環境驗證]
    C -->|否| E[直接升級]
    D --> F{測試通過?}
    F -->|是| E
    F -->|否| G[回報問題 / 等待修復]
    E --> H[執行升級]
    H --> I[hermes update]
    I --> J[hermes doctor]
    J --> K{診斷通過?}
    K -->|是| L[完成升級]
    K -->|否| M[檢查錯誤日誌]
    M --> N[hermes logs --errors]
    N --> O{可修復?}
    O -->|是| P[修復後重試]
    O -->|否| Q[回滾到前版]
```

#### 11.1.3 升級指令

```bash
# 方式 1：使用內建升級指令（推薦）
hermes update

# 方式 1a：免確認升級（v0.13.0，適合 CI/CD）
hermes update --yes     # 或 -y

# 方式 1b：升級前預檢（v0.12.0）
hermes update --check   # 預覽可升級版本與破壞性變更

# 方式 2：手動升級（pip）
pip install --upgrade hermes-agent

# 方式 3：從原始碼升級
cd ~/hermes-agent
git pull origin main
uv pip install -e ".[all]"

# 方式 4：Docker 映像升級
docker pull ghcr.io/nousresearch/hermes-agent:latest
docker-compose up -d --force-recreate

# 升級後驗證
hermes --version
hermes doctor
```

#### 11.1.4 升級注意事項（v0.8.0 特告）

| 項目 | 說明 |
|------|------|
| Skills 同步 | 升級後 bundled skills 會自動同步到所有 Profiles |
| Gateway 保護 | `hermes update` 不再 kill 正在運行的 gateway service |
| Config 驗證 | 啟動時會自動驗證 config.yaml 結構 |
| OpenClaw 移轉 | 如果從 OpenClaw 升級，使用 `hermes claw migrate` |

#### 11.1.5 v0.12.0 升級特別注意事項

| 項目 | 說明 |
|------|------|
| Node.js | 建議升級至 v22 LTS，影響 TUI 冷啟動效能 |
| Secret Redaction | 預設已關閉，避免 patch 損壞，如需請手動啟用 |
| Pluggable Providers | 所有 Provider 已移至 `plugins/model-*` 架構 |
| Curator 預設啟用 | 自動技能維護預設開啟，可透過 `auxiliary.curator.enabled: false` 關閉 |
| Remote Model Catalog | OpenRouter / Nous Portal 模型目錄改為遠端拉取 |

#### 11.1.6 v0.13.0 升級特別注意事項

| 項目 | 說明 |
|------|------|
| Secret Redaction | **預設翻轉為開啟**，如遇 patch 損壞可透過 `security.redaction: false` 關閉 |
| Checkpoints v2 | 新的 Checkpoint 格式，舊 Checkpoint 不會自動遷移，需要手動清除後重建 |
| `hermes update --yes` | 升級指令新增 `-y / --yes` 旗標，跳過確認直接升級（適合 CI） |
| ProviderProfile ABC | 自訂 Provider 需改寫為繼承 `ProviderProfile` ABC 介面 |
| Docker Root 拒絕 | Gateway 現拒絕以 root 身份運行，必須使用非 root 使用者 |
| Windows Early Beta | 原生 Windows 支援為早期測試階段，WSL 仍為企業推薦方案 |
| `display.language` | 新增 i18n 設定項，支援 `zh`、`ja`、`de`、`es`、`fr`、`uk`、`tr` |
| Kanban | 多 Agent Kanban 預設停用，需手動設定 `kanban.enabled: true` |

#### 11.1.7 v0.14.0 升級特別注意事項

| 項目 | 說明 |
|------|------|
| Debloating 浪潮 | 部分重型後端改為 lazy install，工具數從 68+ 降至 60+，首次使用時按需安裝 |
| PyPI 安裝 | 新增 `pip install hermes-agent` 安裝方式 |
| `hermes proxy` | 新增 OpenAI 相容本地代理子指令 |
| Alibaba Cloud → Qwen Cloud | Provider 更名，舊設定名稱仍相容但建議更新 |
| i18n 擴展 | 從 7 語系擴展至 16 語系 |
| Native Windows Beta | PowerShell installer + MinGit 原生 Windows 安裝，不再需要 WSL（測試階段） |
| LINE / SimpleX Chat | 新增第 21、22 平台，需設定對應 API Key |
| `/handoff` | 新增 Session 轉移指令 |
| `/subgoal` | 新增目標追加指令 |
| Brave Search / DDGS | 新增免費 Web Search 後端選項 |

#### 11.1.8 v0.15.0 升級特別注意事項

| 項目 | 說明 |
|------|------|
| **The Big Refactor** | `run_agent.py` 重構為 14 個 `agent/*` 模組，自訂 monkey-patch 可能需要更新路徑 |
| **移除 Vercel AI Gateway** | 如有使用 Vercel AI Gateway Provider，請遷移至其他 Provider |
| **移除 Vercel Sandbox** | Terminal Backend 移除 Vercel Sandbox，請遷移至 Docker/Daytona/Modal |
| Kanban Swarm | 新增 `hermes kanban swarm` Swarm v1 拓撲 |
| `session_search` 重建 | 不再使用 LLM，免費且快 4,500 倍 |
| Promptware 防禦 | 預設啟用，可能影響含特殊格式的 Skill/Memory 檔案 |
| Bitwarden Secrets | 新增 `secrets.backend: bitwarden` 設定選項 |
| ntfy | 新增第 23 平台 |
| s6-overlay Docker | Docker 容器監督改用 s6-overlay |
| `hermes audit` | 新增 OSV.dev 供應鏈審計指令 |
| `hermes send` | 新增腳本輸出推送至任何平台 |
| mTLS for MCP | MCP 伺服器支援雙向 TLS |
| OpenAI API 獨立 Provider | OpenAI API 現為獨立 Provider（不再與 Codex 共用） |
| FAL → Plugin | FAL 圖片生成移至 Plugin 架構 |

### 11.2 相容性管理

#### 11.2.1 版本相容性矩陣

| Hermes 版本 | Python | Node.js | LLM Provider API | MCP |
|-------------|--------|---------|-------------------|-----|
| v0.5.x | 3.11+ | 18+ | OpenAI v1 | 1.0 |
| v0.6.x | 3.11+ | 18+ | OpenAI v1 | 1.0 |
| v0.7.x | 3.11+ | 18+ | OpenAI v1 | 1.0 + OAuth |
| v0.8.x | 3.11+ | 18+ | OpenAI v1 | 1.0 + OAuth 2.1 |
| v0.9.x – v0.10.x | 3.11+ | 18+ | OpenAI v1 | 1.0 + OAuth 2.1 |
| v0.11.x | 3.11+ | 20+ | OpenAI v1 + Responses | 1.0 + OAuth 2.1 |
| v0.12.x | 3.11+ | 22 LTS | OpenAI v1 + Responses | 1.0 + OAuth 2.1 |
| **v0.13.x** | **3.11+** | **22 LTS** | **OpenAI v1 + Responses** | **1.0 + OAuth 2.1 + SSE** |
| **v0.14.x** | **3.11+** | **22 LTS** | **OpenAI v1 + Responses** | **1.0 + OAuth 2.1 + SSE** |
| **v0.15.x** | **3.11+** | **22 LTS** | **OpenAI v1 + Responses** | **1.0 + OAuth 2.1 + SSE + mTLS** |

#### 11.2.2 Provider 相容性

| Provider | 支援版本 | 備註 |
|----------|----------|------|
| Anthropic | Claude 3+ | Thinking block signature 管理 |
| OpenAI | GPT-4+ | 自動修正工具呼叫參數類型 |
| OpenRouter | 全部 | 200+ 模型，aggregator-aware routing |
| Google AI Studio | Gemini 2+ | v0.8.0 新增原生支援，models.dev 自動偵測 |
| Nous Portal | 全部 | 免費 mimo-v2-pro 可用 |
| Ollama | 全部 | 本地模型，支援 Cloud auth |
| z.ai/GLM | 全部 | 端點自動偵測與快取 |
| MiniMax | 全部 | context length 修正、MiniMax TTS Speech 2.8 |
| xAI (Grok) | 全部 | prompt caching 支援、SuperGrok OAuth（v0.14.0）、1M context window |
| Qwen Cloud（原 Alibaba Cloud）| 全部 | OAuth Provider 支援、Portal request |
| Kimi/Moonshot | 全部 | OpenAI 相容端點 |
| **NovitaAI** | **全部** | **v0.14.0 新增 Provider** |
| **OpenAI API** | **全部** | **v0.15.0 獨立 Provider**（不再與 Codex 共用） |

### 11.3 Migration 設計

#### 11.3.1 從 OpenClaw 移轉

如果你之前使用 OpenClaw（Hermes 的前身），可以自動移轉：

```bash
# 互動式移轉（推薦）
hermes claw migrate

# 預覽移轉內容（不執行）
hermes claw migrate --dry-run

# 僅移轉使用者資料（不含 Secrets）
hermes claw migrate --preset user-data

# 覆寫已存在的衝突
hermes claw migrate --overwrite

# 移轉 workspace 指令
hermes claw migrate --workspace-target
```

**移轉內容清單**：

| 項目 | 來源 | 目標 |
|------|------|------|
| SOUL.md | `~/.openclaw/SOUL.md` | `~/.hermes/SOUL.md` |
| Memories | MEMORY.md + USER.md | `~/.hermes/memories/` |
| Skills | 使用者技能 | `~/.hermes/skills/openclaw-imports/` |
| 指令白名單 | approval patterns | `~/.hermes/config.yaml` |
| 訊息設定 | platform configs | `~/.hermes/config.yaml` |
| API Keys | Telegram / OpenRouter / OpenAI 等 | `~/.hermes/.env` |
| TTS 資源 | workspace audio | `~/.hermes/assets/` |
| AGENTS.md | workspace 指令 | 專案目錄 |

#### 11.3.2 版本間 Migration

```bash
# Config migration 由 hermes doctor 自動偵測
hermes doctor

# 如果有 config 結構變更，會自動建議修改
# 例如：
# ⚠️ Config migration needed:
#   - memory_mode → recall_mode (Honcho)
#   - reasoning_effort 統一到 config.yaml
```

> **注意事項**：大版本升級（如 v0.x → v1.x）前，務必先閱讀 Release Notes 的 Breaking Changes 區塊，並在測試環境驗證後再升級生產環境。

---

## 第十二章：實戰案例

### 12.1 AI Coding Agent

#### 場景描述

團隊需要一個 AI Coding Agent 來輔助日常開發工作，包括程式碼撰寫、審查、測試和文件產出。

#### 架構設計

```mermaid
graph LR
    DEV[開發人員] -->|CLI 或 VS Code| HERMES[Hermes Agent<br/>Profile: coding]
    
    HERMES --> |read/write| CODE[專案程式碼<br/>Git Repository]
    HERMES --> |execute| BUILD[建構工具<br/>Maven / Gradle / npm]
    HERMES --> |execute| TEST[測試框架<br/>JUnit / pytest]
    HERMES --> |search| WEB[技術文件<br/>Web Search]
    HERMES --> |MCP| GH[GitHub MCP<br/>PR / Issues]
    
    HERMES --> |記憶| MEM[專案知識庫<br/>架構 / 規範 / 決策]
```

#### 設定檔

```yaml
# AGENTS.md（放在專案根目錄）
# AI Coding Agent 上下文

## 技術棧
- Java 21 / Spring Boot 3.2
- Maven
- JUnit 5 + Mockito
- PostgreSQL 16
- Clean Architecture

## 程式碼規範
- Google Java Style
- 每個 public 方法必須有 JavaDoc
- 測試覆蓋率 > 80%
- 不得使用 System.out.println

## Git 工作流
- feature/* → develop → main
- Conventional Commits
- PR 需要 2 人 review
```

```yaml
# config.yaml
model:
  provider: anthropic
  model: claude-sonnet-4-20250514

security:
  command_approval: smart
  allowed_commands:
    - "mvn *"
    - "git status"
    - "git diff"
    - "git log"

toolsets:
  enabled: [core, web, delegation, code]

mcp:
  servers:
    - name: github
      command: npx
      args: ["@modelcontextprotocol/server-github"]
```

#### 使用範例

```bash
# 1. 開發新功能
> 幫我開發使用者 CRUD API，遵循 AGENTS.md 中的規範

# 2. 程式碼審查
> 請審查 git diff 中的變更，檢查安全性和效能

# 3. 測試補齊
> 幫 UserService 補齊單元測試，目標覆蓋率 90%

# 4. 自動化 PR
> 幫我建立 PR，標題遵循 Conventional Commits

# 5. 排程（每日定時）
> 每天早上 9 點執行 mvn verify，結果傳到 Slack
```

### 12.2 智慧客服 Agent

#### 場景描述

為銀行建立智慧客服系統，Agent 能理解客戶問題、查詢知識庫、處理常見業務。

#### 架構設計

```mermaid
graph TB
    subgraph "客戶端"
        TG[Telegram]
        LINE[LINE]
        WEB[Web Chat]
    end
    
    subgraph "Hermes Gateway"
        GW[消息路由<br/>認證 / 限流]
    end
    
    subgraph "Agent Layer"
        CS[客服 Agent<br/>Profile: customer-service]
        KB[知識庫 Skill<br/>FAQ / 產品 / 流程]
        ESC[升級 Skill<br/>轉接真人客服]
    end
    
    subgraph "Backend"
        API[銀行 API<br/>帳戶查詢 / 交易記錄]
        CRM[CRM 系統<br/>客戶資料]
    end
    
    TG --> GW
    LINE --> GW
    WEB --> GW
    
    GW --> CS
    CS --> KB
    CS --> ESC
    CS -->|MCP| API
    CS -->|MCP| CRM
```

#### SOUL.md 設定

```markdown
# SOUL.md
你是「小安」，XX 銀行的智慧客服助理。

## 性格特質
- 親切有禮、專業可靠
- 說話簡潔明瞭
- 遇到無法處理的問題，主動告知並轉接真人客服

## 限制
- 不能提供投資建議
- 不能洩漏其他客戶的資料
- 不能修改客戶帳戶（只能查詢）
- 敏感資訊必須遮蔽（帳號僅顯示末 4 碼）

## 語言
- 使用繁體中文
- 稱呼客戶為「您」
```

#### 客服知識庫 Skill

```markdown
# bank-customer-service

## Description
銀行客服知識庫，處理客戶常見問題。

## FAQ Categories
1. **帳戶查詢**：餘額、交易記錄、對帳單
2. **信用卡**：帳單、繳費、掛失、額度
3. **匯款**：國內匯款、國際匯款、轉帳限額
4. **貸款**：房貸、信貸、車貸進度查詢
5. **其他**：營業時間、ATM 據點、網銀問題

## Escalation Rules
- 客戶連續 3 次表示不滿意 → 轉接真人
- 涉及交易爭議 → 轉接真人
- 涉及帳戶異常 → 轉接真人 + 通知風控
```

### 12.3 銀行流程自動化 Agent

#### 場景描述

自動化銀行內部 IT 作業流程，包括定時報表、系統監控、變更管理。

#### 架構設計

```mermaid
graph TB
    subgraph "排程系統"
        CRON[Hermes Cron<br/>排程管理]
    end
    
    subgraph "自動化任務"
        RPT[報表 Agent<br/>每日/週/月報表]
        MON[監控 Agent<br/>系統健康檢查]
        CHG[變更 Agent<br/>部署前檢查]
    end
    
    subgraph "工具"
        DB[(Database<br/>報表查詢)]
        GIT[Git Repository<br/>程式碼掃描]
        JIRA[Jira / Issue<br/>工單管理]
        DOCKER[Docker/K8s<br/>部署狀態]
    end
    
    subgraph "通知"
        TG_N[Telegram<br/>即時通知]
        MAIL[Email<br/>報表分發]
        SK_N[Slack<br/>團隊通知]
    end
    
    CRON --> RPT
    CRON --> MON
    CRON --> CHG
    
    RPT -->|MCP| DB
    MON --> DOCKER
    CHG --> GIT
    CHG --> JIRA
    
    RPT --> TG_N
    RPT --> MAIL
    MON --> TG_N
    CHG --> SK_N
```

#### Cron 排程設定

```bash
# 1. 每日報表（每天 08:00）
> 每天早上 8 點：
> - 查詢 PostgreSQL 取得昨日交易統計
> - 產生摘要報表（表格格式）
> - 傳送到 Telegram 群組和 Email

# 2. 系統監控（每小時）
> 每小時：
> - 檢查所有 K8s Pod 狀態
> - 檢查 DB connection pool
> - 檢查 API 回應時間
> - 如有異常，立即通知 Telegram

# 3. 部署前檢查（觸發式）
> 當收到 "部署檢查 [環境]" 訊息時：
> - 執行 mvn verify
> - 執行安全掃描（/bank-api-security-check）
> - 檢查 Jira 是否有未關閉的相關 Bug
> - 產出部署檢查報告
```

#### 自動化報表範例輸出

```markdown
# XX銀行系統日報 - 2026/04/09

## 交易統計
| 類型 | 筆數 | 金額（萬元）|
|------|------|------------|
| 轉帳 | 12,345 | 45,678 |
| 匯款 | 1,234 | 23,456 |
| 刷卡 | 34,567 | 12,345 |

## 系統健康度
- API 可用率：99.97%
- 平均回應時間：45ms（P99: 200ms）
- 錯誤率：0.03%
- DB Connection Pool：65/100

## 安全事件
- ⚠️ 偵測到 3 次異常登入嘗試（已鎖定）
- ✅ CVE 掃描：無新漏洞

## 待處理項目
- JIRA-1234：修復對帳差異問題（High，已指派）
- JIRA-1235：優化查詢效能（Medium，待指派）
```

> **實務案例**：某銀行導入 Hermes Agent 自動化流程後，IT 團隊每日例行作業時間從 2 小時縮短至 15 分鐘。報表產出從人工製作改為自動化，錯誤率從 5% 降至 0.1%。系統異常平均偵測時間從 30 分鐘縮短至 5 分鐘。

### 12.4 多媒體創作 Agent

#### 場景描述

結合 v0.12.0 新增的 ComfyUI v5、Spotify 整合和 TouchDesigner-MCP，建立多媒體內容創作 Agent。

#### 架構設計

```mermaid
graph LR
    USER[創作者] -->|描述需求| AGENT[Hermes Agent<br/>Profile: creative]
    
    AGENT -->|圖像生成| COMFY[ComfyUI v5<br/>Stable Diffusion]
    AGENT -->|音樂控制| SPOTIFY[Spotify Plugin<br/>PKCE OAuth]
    AGENT -->|視覺效果| TD[TouchDesigner-MCP<br/>即時互動視覺]
    AGENT -->|影片腳本| WRITE[寫作 Skill<br/>文案 / 分鏡]
    
    COMFY --> OUTPUT[創作成果]
    SPOTIFY --> OUTPUT
    TD --> OUTPUT
    WRITE --> OUTPUT
```

#### 設定檔

```yaml
# config.yaml
model:
  provider: anthropic
  model: claude-sonnet-4-20250514

plugins:
  spotify:
    enabled: true
  comfyui:
    enabled: true
    endpoint: "http://localhost:8188"   # 本地 ComfyUI 伺服器
  touchdesigner:
    enabled: true

toolsets:
  enabled: [core, web, code, browser]
```

#### 使用範例

```bash
# 1. 生成行銷素材
> 幫我用 ComfyUI 生成一張企業年度報告的封面圖，
> 風格：科技感、藍色調、包含數據視覺化元素

# 2. 音樂配合
> 搜尋一首適合產品發布會的背景音樂，加到播放清單

# 3. 互動視覺
> 用 TouchDesigner 設計一個即時數據看板的原型
```

> **實務案例**：某行銷團隊使用 Hermes Creative Agent 將素材製作時間從 3 天縮短至 2 小時，搭配 ComfyUI 自動生成的圖像與 Spotify 配樂，單月產出效率提升 10 倍。

---

## 第十三章：常見問題（FAQ）

### Q1：Agent 無法學習 / 不建立 Skill？

**可能原因**：
1. 任務複雜度不夠高，Agent 判定不需要封裝
2. Memory provider 未正確設定

**解決方法**：
```bash
# 確認記憶設定
hermes config get memory.provider

# 手動觸發技能建立
> 請將剛才的操作流程封裝為一個技能

# 查看已有技能
/skills
```

### Q2：Memory 佔用過多空間？

**解決方法**：
```bash
# 查看記憶大小
du -sh ~/.hermes/memories/

# 壓縮 Session 資料庫
sqlite3 ~/.hermes/sessions.db "VACUUM;"

# 清理舊 Session
> 幫我清理 30 天前的 session 資料

# 如果使用 Vector DB，定期清理低相關性記憶
# mem0 / Supermemory 都有自動清理機制
```

### Q3：Token 成本過高？

**優化策略**：

| 策略 | 效果 | 做法 |
|------|------|------|
| 使用免費輔助模型 | 節省 ~60% | `auxiliary.model: mimo-v2-pro` |
| 自動 Context 壓縮 | 節省 ~30% | `context.auto_compress: true` |
| Programmatic Tool Calling | 節省 ~50% | 用 execute_code 批次工具呼叫 |
| 選擇較小模型 | 節省 ~70% | 簡單任務用 Haiku / 4o-mini |
| Subagent 委派 | 節省上下文 | 複雜任務分拆到子代理 |

### Q4：模型切換失敗？

**常見問題與解法**：

```bash
# 錯誤：Stale OAuth credentials
hermes auth login nous   # 重新登入

# 錯誤：Model not found
/model                   # 查看可用模型清單

# 錯誤：402 Payment Required
# → 自動切換到 fallback provider
# → 或充值 API 額度

# 錯誤：Non-agentic model warning
# → 切換到支援 tool-use 的模型（如 Claude Sonnet / GPT-4o）

# 診斷工具
hermes doctor
```

### Q5：Gateway 連線不穩定？

**排查步驟**：

```bash
# 1. 檢查 gateway 狀態
hermes gateway status

# 2. 查看日誌
hermes logs --filter "gateway"

# 3. 重啟 gateway
hermes gateway restart

# 4. 診斷
hermes doctor

# 5. 常見修復
# Telegram：檢查 BOT_TOKEN 是否正確
# Discord：確認 Bot 權限（不需要 members intent）
# Slack：確認 Event Subscription URL
```

### Q6：Windows 環境怎麼用？

```bash
# 方式 1：WSL2（企業推薦）
wsl --install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# 方式 2：Native Windows Early Beta（v0.13.0 新增）
irm https://hermes-agent.nousresearch.com/install.ps1 | iex
# 注意：Native Windows 為早期測試版，
# 不支援 Gateway / Voice / Docker 工具
# 企業生產環境仍建議使用 WSL2
```

### Q7：如何與 VS Code 整合？

```bash
# Hermes 支援 ACP（Agent Communication Protocol）
# 可與 VS Code / JetBrains / Zed 整合

# 在 VS Code 中使用 Hermes 作為 AI Agent：
# 1. 安裝 Hermes VS Code 擴展
# 2. 設定 ACP adapter
# 3. 即可在 IDE 中直接呼叫 Hermes

# 或者直接在 VS Code Terminal 中使用 hermes CLI
```

### Q8：MCP 伺服器連線失敗？

```bash
# 1. 確認 MCP 伺服器可用
npx @modelcontextprotocol/server-github --version

# 2. 確認環境變數已設定
echo $GITHUB_TOKEN

# 3. 檢查 OAuth 認證（v0.8.0）
# MCP OAuth 2.1 PKCE 需要瀏覽器互動

# 4. 檢查 OSV 掃描結果
# 如果套件有已知漏洞，Hermes 會阻擋安裝
```

### Q9：Voice Mode 無法使用？

**排查步驟**：

```bash
# 1. 確認已啟用語音工具集
hermes tools enable voice

# 2. 確認 STT/TTS Provider 設定
hermes config get voice.stt_provider
hermes config get voice.tts_provider

# 3. 確認 API Key 已配置
# OpenAI Whisper → 需要 OPENAI_API_KEY
# Voxtral → 需要 MISTRAL_API_KEY
# ElevenLabs → 需要 ELEVENLABS_API_KEY

# 4. 確認麥克風權限（CLI Voice Mode）
# macOS: 系統偏好設定 → 隱私權 → 麥克風
# Linux: 確認 PulseAudio / PipeWire 正常

# 5. 診斷
hermes doctor
```

### Q10：如何查看 Agent 的完整執行日誌？

```bash
# 即時查看日誌
hermes logs

# 只看錯誤
hermes logs --errors

# 過濾特定關鍵字
hermes logs --filter "tool_call"
hermes logs --filter "memory"

# 日誌位置
~/.hermes/logs/agent.log     # INFO+ 級別
~/.hermes/logs/errors.log    # WARNING+ 級別
```

### Q11：如何在多個專案間切換？

```bash
# 方式 1：使用不同 Profile
hermes --profile project-a
hermes --profile project-b

# 方式 2：在不同工作目錄啟動（會自動載入當前目錄的 AGENTS.md）
cd /path/to/project-a && hermes
cd /path/to/project-b && hermes

# 方式 3：使用 /new 重置對話但保留記憶
/new
```

### Q12：Autonomous Curator 會刪除重要技能嗎？（v0.12.0）

**Curator 的安全邊界**：
- Bundled Skills（內建技能）：**永遠不會**被修改或刪除
- Hub Skills（社群安裝的技能）：受保護，不會被修改
- Pinned Skills：使用者手動標記的技能受保護
- 使用者自建技能：低品質或長期未使用的「可能」被修剪

```bash
# 保護重要技能
hermes skills pin my-important-skill

# 關閉 Curator
hermes config set auxiliary.curator.enabled false

# 檢查 Curator 最近的操作報告
cat ~/.hermes/logs/curator/REPORT.md
```

### Q13：`hermes -z` 和普通模式有何不同？（v0.12.0）

```bash
# -z 模式（非互動式，適合腳本與 CI/CD）
hermes -z "列出所有待修 bug"
# → 直接執行一次任務後退出，不進入 TUI
# → 不會記錄 session history
# → 可用 --model / --provider 指定模型

# 普通模式（互動式 TUI）
hermes
# → 進入持久對話，支援多輪互動
# → 記錄 session history
# → 支援所有 slash 指令
```

### Q14：如何使用 Background Sessions？（v0.12.0）

```bash
# 在對話中，將耗時任務移至背景
> 幫我對整個 src/ 目錄做安全掃描
/background    # 將此任務移至背景

# 繼續在主對話中工作
> 幫我修改 README.md

# 背景任務完成後會自動通知
# [Background] 安全掃描完成，發現 2 個中風險問題
```

### Q15：如何配置 Prompt Cache？（v0.12.0）

```yaml
# config.yaml
prompt_caching:
  cache_ttl: 300         # 預設 5 分鐘
  # cache_ttl: 3600      # 高頻使用場景可設為 1 小時
  # 適用於 System Prompt 不常變更的場景
  # 可有效降低重複 Token 消耗
```

### Q16：Multi-agent Kanban 如何設定？（v0.13.0）

```yaml
# config.yaml
kanban:
  enabled: true
  max_concurrent: 4      # 同時運行的子代理數量
  auto_spawn: true        # 自動依任務生成子代理
```

```bash
# 使用 /kanban 查看看板狀態
/kanban

# 使用 /goal 設定持久化目標（Ralph Loop）
/goal 完成 API 重構並通過所有測試
```

### Q17：如何啟用 i18n（多語系）介面？（v0.13.0）

```yaml
# config.yaml
display:
  language: zh    # 繁體中文
  # 支援: zh, ja, de, es, fr, uk, tr
```

### Q18：video_analyze 工具怎麼用？（v0.13.0）

```bash
# 在對話中直接分析影片
> 請分析這段影片的內容：/path/to/video.mp4

# 支援格式：MP4、WebM 等常見格式
# 需要 LLM Provider 支援 Vision（如 Claude Sonnet、GPT-4o）
```

---

## 附錄 A：檢查清單（Checklist）

### A.1 安裝檢查清單

- [ ] 確認作業系統為 Linux / macOS / WSL2
- [ ] 確認 Python 3.11+ 已安裝
- [ ] 確認 Node.js 22 LTS 已安裝（v0.12.0+ 建議）
- [ ] 確認 Git 已安裝
- [ ] 執行 `curl -fsSL ... | bash` 安裝 Hermes
- [ ] 執行 `source ~/.bashrc` 重新載入 Shell
- [ ] 執行 `hermes --version` 確認安裝成功
- [ ] 執行 `hermes setup` 完成初始設定
- [ ] 執行 `hermes doctor` 確認無問題

### A.2 API Key 設定檢查清單

- [ ] 至少設定一個 LLM Provider（Anthropic / OpenAI / OpenRouter）
- [ ] 設定輔助模型（建議 Nous Portal 免費 mimo-v2-pro）
- [ ] API Key 存放在 `.env` 檔案（不入版控）
- [ ] `.env` 已加入 `.gitignore`
- [ ] 生產環境 API Key 透過 Vault 或 Secret Manager 管理

### A.3 安全檢查清單

- [ ] `command_approval` 設定為 `smart` 或 `always`
- [ ] `allowed_commands` 白名單已配置
- [ ] 生產環境未使用 `--yolo` flag
- [ ] MCP 伺服器有 OAuth 認證
- [ ] API Key 定期輪換（建議 90 天）
- [ ] 日誌中無敏感資訊洩漏
- [ ] Gateway `allowed_users` 白名單已設定

### A.4 生產部署檢查清單

- [ ] Docker 映像使用多階段建構
- [ ] 容器以非 root 使用者執行
- [ ] Health Check 已配置
- [ ] 資源限制已設定（memory / cpu）
- [ ] 日誌已導向集中式日誌系統
- [ ] 備份策略已制定並執行
- [ ] Provider Failover 已配置（至少 2 個 Provider）
- [ ] 監控告警已設定（Token 使用量 / 錯誤率 / 回應時間）

### A.5 團隊導入檢查清單

- [ ] 建立專案 AGENTS.md（專案上下文）
- [ ] 建立團隊 SOUL.md（Agent 人格定義）
- [ ] 建立團隊 Profile（`hermes --profile team-xxx`）
- [ ] 建立常用 Skills（如程式碼審查、安全掃描）
- [ ] 建立 Cron 排程（如每日報表、系統監控）
- [ ] 建立使用規範（哪些任務適合 / 不適合交給 Agent）
- [ ] 團隊成員完成基礎訓練
- [ ] 設定 Token 預算上限

### A.6 升級檢查清單

- [ ] 閱讀 Release Notes（特別是 Breaking Changes）
- [ ] 在測試環境驗證
- [ ] 備份 `~/.hermes/` 目錄
- [ ] 執行 `hermes update`
- [ ] 執行 `hermes doctor` 驗證
- [ ] 確認所有 Skills 正常載入
- [ ] 確認 Gateway 連線正常
- [ ] 確認 Memory Provider 正常
- [ ] 更新 Docker 映像版本（如使用容器部署）

---

## 附錄 B：指令速查表

### B.1 CLI 指令

| 指令 | 說明 |
|------|------|
| `hermes` | 啟動互動式 CLI |
| `hermes model` | 互動式選擇模型與 Provider |
| `hermes tools` | 列出所有工具集與狀態 |
| `hermes tools enable <name>` | 啟用工具集 |
| `hermes tools disable <name>` | 停用工具集 |
| `hermes config set <key> <value>` | 設定單項配置 |
| `hermes config get <key>` | 查看單項配置 |
| `hermes setup` | 執行完整設定精靈 |
| `hermes gateway start` | 啟動訊息平台閘道 |
| `hermes gateway stop` | 停止閘道 |
| `hermes gateway status` | 查看閘道狀態 |
| `hermes gateway setup` | 設定閘道平台 |
| `hermes auth login <provider>` | OAuth 登入 Provider |
| `hermes auth remove <provider>` | 移除 Provider 憑證 |
| `hermes claw migrate` | 從 OpenClaw 移轉 |
| `hermes update` | 升級到最新版本 |
| `hermes doctor` | 診斷環境問題 |
| `hermes logs` | 查看 Agent 日誌 |
| `hermes logs --errors` | 只查看錯誤日誌 |
| `hermes --profile <name>` | 使用指定 Profile 啟動 |
| `hermes --voice` | 啟用語音模式 |
| `hermes --version` | 顯示版本資訊 |
| `hermes -z "<task>"` | Non-interactive 單次模式（v0.12.0）|
| `hermes -z --model <m>` | 單次模式指定模型（v0.12.0）|
| `hermes curator` | 手動觸發 Curator（v0.12.0）|
| `hermes curator status` | 查看 Curator 技能排名（v0.12.0）|
| `hermes curator archive` | 歸檔低品質技能（v0.13.0）|
| `hermes curator prune` | 清理已歸檔技能（v0.13.0）|
| `hermes curator list-archived` | 列出已歸檔技能（v0.13.0）|
| `hermes update --check` | 升級預檢（v0.12.0）|
| `hermes update --yes` | 免確認升級（v0.13.0）|
| `hermes fallback` | 管理 Fallback Provider（v0.12.0）|
| `hermes plugins list` | 列出已安裝 Plugin（v0.12.0）|
| `hermes plugins enable <name>` | 啟用 Plugin（v0.12.0）|
| `hermes gateway list` | 列出所有已設定平台（v0.13.0）|
| `hermes kanban` | 查看 Kanban 看板狀態（v0.13.0）|

### B.2 對話中斜線指令

| 指令 | 說明 |
|------|------|
| `/new` 或 `/reset` | 開啟新對話（保留記憶）|
| `/model [provider:model]` | 切換模型 |
| `/compress` | 壓縮當前上下文 |
| `/usage` | 查看 Token 使用量 |
| `/insights [--days N]` | 查看使用洞察 |
| `/skills` | 列出可用技能 |
| `/<skill-name>` | 執行特定技能 |
| `/personality [name]` | 設定人格 |
| `/retry` | 重試上一輪 |
| `/undo` | 撤銷上一輪 |
| `/voice on/off` | 開關語音模式 |
| `/approve` | 批准待審指令 |
| `/deny` | 拒絕待審指令 |
| `/stop` | 中斷當前操作 |
| `/platforms` | 查看連線平台狀態 |
| `/status` | 查看 Agent 狀態 |
| `/busy [steer\|queue\|interrupt]` | 忙碗模式（v0.12.0）|
| `/btw` | 中插任務導引（v0.12.0）|
| `/background` | 移至背景執行（v0.12.0）|
| `/reload` | 熱重載 `.env`（v0.12.0）|
| `/reload-skills` | 重新載入技能庫（v0.12.0）|
| `/reload-mcp` | 重建 MCP cached agents（v0.12.0）|
| `/mouse` | 互動式滑鼠操作（v0.12.0）|
| `/fast` | 切換 Fast Mode |
| `/steer` | 中途導引 Agent 行為（v0.11.0）|
| `/goal` | 設定持久化目標（Ralph Loop）（v0.13.0）|
| `/kanban` | 顯示 Multi-agent Kanban 看板（v0.13.0）|
| `/queue` | 查看任務佇列（v0.13.0）|

---

## 附錄 C：環境變數參考

| 環境變數 | 說明 | 必要性 |
|----------|------|--------|
| `ANTHROPIC_API_KEY` | Anthropic API 金鑰 | 至少一個 Provider |
| `OPENAI_API_KEY` | OpenAI API 金鑰 | 至少一個 Provider |
| `OPENROUTER_API_KEY` | OpenRouter API 金鑰 | 至少一個 Provider |
| `GOOGLE_AI_API_KEY` | Google AI Studio API 金鑰 | 選用 |
| `XAI_API_KEY` | xAI (Grok) API 金鑰 | 選用 |
| `NVIDIA_API_KEY` | NVIDIA NIM API 金鑰 | 選用 |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | AWS Bedrock 認證 | 選用 |
| `HF_TOKEN` | Hugging Face Inference API Token | 選用 |
| `GMI_API_KEY` | GMI Cloud API 金鑰 | 選用 |
| `DEEPSEEK_API_KEY` | DeepSeek API 金鑰 | 選用 |
| `DASHSCOPE_API_KEY` | Alibaba Cloud / Qwen API 金鑰 | 選用 |
| `MISTRAL_API_KEY` | Mistral AI API 金鑰（Voxtral STT） | 選用 |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token | Gateway 需要 |
| `DISCORD_BOT_TOKEN` | Discord Bot Token | Gateway 需要 |
| `SLACK_BOT_TOKEN` | Slack Bot Token | Gateway 需要 |
| `GITHUB_TOKEN` | GitHub Token（MCP / Copilot 用）| MCP 需要 |
| `DATABASE_URL` | PostgreSQL 連線字串（MCP 用）| MCP 需要 |
| `ELEVENLABS_API_KEY` | ElevenLabs TTS API 金鑰 | Voice 需要 |
| `MEM0_API_KEY` | mem0 Cloud API 金鑰 | mem0 記憶需要 |
| `HERMES_PORTAL_BASE_URL` | 自訂 Nous Portal URL | 選用 |
| `HERMES_HOME` | 自訂 Hermes 主目錄（預設 `~/.hermes`）| 選用 |
| `AI_GATEWAY_API_KEY` | Vercel AI Gateway API 金鑰（**v0.15.0 已移除**） | 已棄用 |
| `LM_STUDIO_URL` | LM Studio 本地端點（v0.12.0）| 選用 |
| `AZURE_AI_FOUNDRY_KEY` | Azure AI Foundry API 金鑰（v0.12.0）| 選用 |
| `AZURE_AI_FOUNDRY_ENDPOINT` | Azure AI Foundry 端點（v0.12.0）| 選用 |
| `TENCENT_TOKENHUB_KEY` | 騰訊 Tokenhub API 金鑰（v0.12.0）| 選用 |
| `MINIMAX_API_KEY` | MiniMax API 金鑰（v0.12.0 PKCE）| 選用 |
| `SPOTIFY_CLIENT_ID` | Spotify Client ID（v0.12.0）| Spotify 需要 |
| `SPOTIFY_CLIENT_SECRET` | Spotify Client Secret（v0.12.0）| Spotify 需要 |
| `LANGFUSE_PUBLIC_KEY` | Langfuse Public Key（v0.12.0）| 可觀測性選用 |
| `LANGFUSE_SECRET_KEY` | Langfuse Secret Key（v0.12.0）| 可觀測性選用 |
| `GOOGLE_MEET_CREDENTIALS` | Google Meet 憑證（v0.12.0）| Meet 需要 |
| `HERMES_DASHBOARD` | 設為 `1` 啟動 Dashboard Side-process（v0.13.0）| 選用 |
| `DISCORD_ALLOWED_ROLES` | Discord Guild 角色白名單（v0.13.0 安全修正）| 選用 |
| `XAI_API_KEY` | xAI Custom Voices TTS API 金鑰（v0.13.0）| Voice 需要 |
| `GOOGLE_CHAT_WEBHOOK` | Google Chat Webhook URL（v0.13.0）| Gateway 需要 |
| `NOVITA_API_KEY` | NovitaAI API 金鑰（v0.14.0）| 選用 |
| `LINE_CHANNEL_ACCESS_TOKEN` | LINE Messaging API Token（v0.14.0）| Gateway 需要 |
| `SIMPLEX_CHAT_PORT` | SimpleX Chat 連接埠（v0.14.0）| Gateway 需要 |
| `BWS_ACCESS_TOKEN` | Bitwarden Secrets Manager Machine Account Token（v0.15.0）| Bitwarden 需要 |
| `NTFY_TOPIC` | ntfy 推播主題 URL（v0.15.0）| Gateway 需要 |

---

## 附錄 D：Provider 完整清單

截至 v0.15.2，Hermes Agent 支援 **35+ 可插拔式 Provider**，均透過 `ProviderProfile` ABC + `plugins/model-*` 架構載入：

| # | Provider | 說明 | 版本 |
|---|----------|------|------|
| 1 | OpenAI | GPT-4o / GPT-5.5 / o1 / o3 | v0.1.0+ |
| 2 | Anthropic | Claude Sonnet / Opus / Haiku | v0.1.0+ |
| 3 | OpenRouter | 200+ 模型聚合 | v0.1.0+ |
| 4 | Nous Portal | Hermes 3 / MiMo v2 Pro（免費） | v0.3.0+ |
| 5 | Google AI Studio | Gemini 2.5 Pro / Flash | v0.4.0+ |
| 6 | Ollama | 本地模型 | v0.4.0+ |
| 7 | z.ai / GLM | 智譜模型 | v0.5.0+ |
| 8 | Kimi / Moonshot | Kimi 系列 | v0.5.0+ |
| 9 | MiniMax | MiniMax 模型 + TTS | v0.5.0+ |
| 10 | Qwen Cloud（原 Alibaba Cloud） | Qwen 系列 | v0.5.0+（v0.14.0 更名） |
| 11 | xAI | Grok 3 / Grok 4.3 / SuperGrok OAuth | v0.6.0+ |
| 12 | DeepSeek | DeepSeek v3 / v4 | v0.6.0+ |
| 13 | Hugging Face | Inference API | v0.7.0+ |
| 14 | ~~GitHub Copilot~~ | ~~Codex OAuth~~ | ~~v0.8.0+~~（已棄用） |
| 15 | Xiaomi MiMo | MiMo 模型 | v0.9.0+ |
| 16 | AWS Bedrock | Converse API（Native） | v0.11.0+ |
| 17 | NVIDIA NIM | Nemotron 系列 | v0.11.0+ |
| 18 | Arcee AI | 企業微調模型 | v0.11.0+ |
| 19 | GMI Cloud | GMI 雲端推理 | v0.11.0+ |
| 20 | Step Plan | 階段規劃推理 | v0.11.0+ |
| 21 | Gemini CLI OAuth | Google CLI OAuth 流程 | v0.11.0+ |
| 22 | ~~Vercel AI Gateway~~ | ~~Vercel 網關~~ | ~~v0.11.0+~~（**v0.15.0 移除**） |
| 23 | **LM Studio** | 本地 first-class Provider | **v0.12.0** |
| 24 | **Azure AI Foundry** | Azure 雲端推理 | **v0.12.0** |
| 25 | **GMI Cloud** | GMI 雲端推理（升級） | **v0.12.0** |
| 26 | **MiniMax OAuth** | PKCE OAuth 流程 | **v0.12.0** |
| 27 | **Tencent Tokenhub** | 騰訊雲模型 | **v0.12.0** |
| 28 | **xAI Custom Voices** | 語音克隆 TTS Provider | **v0.13.0** |
| 29 | **SearXNG** | 原生搜尋引擎 Provider | **v0.13.0** |
| 30 | **NovitaAI** | NovitaAI 推理 Provider | **v0.14.0** |
| 31 | **Brave Search** | 免費 Web Search | **v0.14.0** |
| 32 | **DDGS** | DuckDuckGo 免費搜尋 | **v0.14.0** |
| 33 | **OpenAI API** | OpenAI API 獨立 Provider（不再與 Codex 共用） | **v0.15.0** |
| 34 | **Krea** | Krea 2 Medium / Large 圖片生成 | **v0.15.0** |
| 35+ | OpenAI-compatible | 任何相容 API 端點 | 全版本 |

**v0.13.0 — v0.15.0 新增模型與功能**：

| 模型 | Provider | 說明 |
|------|----------|------|
| DeepSeek v4 Pro | DeepSeek | 最新代推理模型（v0.13.0） |
| Grok 4.3 | xAI | 升級版 Grok，1M context window（v0.14.0 SuperGrok OAuth） |
| Owl Alpha | OpenRouter | 免費模型（v0.13.0） |
| hy3-preview | Tencent | 預覽版模型（v0.13.0） |
| Arcee Trinity Large Thinking | Arcee AI | 支援溫度 + 壓縮覆寫（v0.13.0） |

> **說明**：v0.12.0 將所有 Provider 重構為 Pluggable 架構，v0.13.0 引入 `ProviderProfile` ABC 介面，v0.15.0 移除 Vercel AI Gateway 與 Vercel Sandbox，新增 OpenAI API 獨立 Provider、Microsoft Entra ID auth。第三方可自行開發 Provider Plugin 並載入 Hermes。

---

## 參考資源

| 資源 | 連結 |
|------|------|
| 官方文件 | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/) |
| GitHub | [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| Skills Hub | [agentskills.io](https://agentskills.io/) |
| Discord 社群 | [discord.gg/NousResearch](https://discord.gg/NousResearch) |
| Nous Portal | [portal.nousresearch.com](https://portal.nousresearch.com/) |
| OpenRouter | [openrouter.ai](https://openrouter.ai/) |
| Issue Tracker | [GitHub Issues](https://github.com/NousResearch/hermes-agent/issues) |
| 討論區 | [GitHub Discussions](https://github.com/NousResearch/hermes-agent/discussions) |
| Voice Mode 指南 | [Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/voice) |
| MCP 使用指南 | [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/mcp) |
| WSL2 網路指南 | [WSL2 Networking Guide](https://hermes-agent.nousresearch.com/docs/guides/wsl2-networking) |

---

> **文件版本**：v5.0.0  
> **基於 Hermes Agent**：v0.15.2 (v2026.5.29，涵蓋 The Foundation Release + The Velocity Release)  
> **建立日期**：2026 年 4 月 9 日  
> **最後更新**：2026 年 6 月 1 日  
> **維護者**：技術架構團隊

