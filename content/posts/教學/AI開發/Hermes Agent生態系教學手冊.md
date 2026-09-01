+++
date = '2026-06-30T10:00:00+08:00'
draft = false
title = 'Hermes Agent生態系教學手冊'
tags = ['教學', 'AI開發','指引']
categories = ['教學']
+++

# Hermes Agent 生態系教學手冊（Enterprise Edition）

> **版本**：v0.21.0（Git tag `v2026.8.31`，2026 年 8 月 31 日 — **The Pantheon Release**；本文涵蓋 The Judgment / The Quicksilver / The Herald / The Pantheon 四大版本 + 中間全部穩定化補丁）  
> **適用對象**：資深工程師 / 架構師 / DevOps 團隊 / 技術採購與風險評估決策者  
> **軟體授權**：MIT License（Hermes Agent 本體完全開源、免費、可自架；下述訂閱方案僅為選用的 Nous Portal 代管服務，非軟體授權費）  
> **官方網站**：[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)  
> **GitHub**：[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)  
> **官方文件**：[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)  
> **Desktop 下載**：[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)（macOS Apple Silicon / Windows 10-11 / Linux；**macOS Intel 已不支援**）  
> **Skills Hub**：[agentskills.io](https://agentskills.io/) / [skills.sh](https://skills.sh/)  
> **LLM 友善文件**：[llms.txt](https://hermes-agent.nousresearch.com/docs/llms.txt) / [llms-full.txt](https://hermes-agent.nousresearch.com/docs/llms-full.txt)  
> **最後更新**：2026 年 9 月 1 日  
> **資料來源聲明**：本文所有版本資訊、功能敘述均逐條核對 **GitHub Releases API**（版本號、日期、統計數字之權威來源）、**GitHub REST API**（倉庫即時數據）、官方文件站全站目錄（以 `llms.txt` 逐頁比對覆蓋率）與 NVD／GitHub Advisory 資料庫；價格類數字凡標示「二手來源」者，代表官方定價頁在查證當下回應 HTTP 429，未能以一手頁面直接核實，建議上線前至 [portal.nousresearch.com/manage-subscription](https://portal.nousresearch.com/manage-subscription) 覆核。

---

<!-- TOC-AUTO-BEGIN -->

## 📑 目錄

> 目錄採三層結構：**章**（第一層）→ **節**（`x.y`，第二層）→ 第三層僅保留兩處「索引型」清單——**1.4.x 核心設計理念**（共 41 項功能總覽）與 **9.7.x 風險評估**，其餘小節請於各節內文瀏覽。

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
    - [1.4.14 PyPI 套件安裝（v0.14.0 起，v0.20.0 已停用）](#1414-pypi-套件安裝v0140-起v0200-已停用)
    - [1.4.15 /handoff 即時 Session 轉移（v0.14.0+）](#1415-handoff-即時-session-轉移v0140)
    - [1.4.16 Promptware 防禦（v0.15.0+）](#1416-promptware-防禦v0150)
    - [1.4.17 Bitwarden Secrets Manager（v0.15.0+）](#1417-bitwarden-secrets-managerv0150)
    - [1.4.18 Skill Bundles（v0.15.0+）](#1418-skill-bundlesv0150)
    - [1.4.19 Hermes Desktop App（v0.16.0+）](#1419-hermes-desktop-appv0160)
    - [1.4.20 Background Subagents（v0.17.0+）](#1420-background-subagentsv0170)
    - [1.4.21 Image Editing（v0.17.0+）](#1421-image-editingv0170)
    - [1.4.22 Automation Blueprints（v0.17.0+）](#1422-automation-blueprintsv0170)
    - [1.4.23 Memory Atomic Batch Operations（v0.17.0+）](#1423-memory-atomic-batch-operationsv0170)
    - [1.4.24 Mixture-of-Agents（MoA）一級模型化（v0.18.0+）](#1424-mixture-of-agentsmoa一級模型化v0180)
    - [1.4.25 自我學習強化：/learn 與 /journey（v0.18.0+）](#1425-自我學習強化learn-與-journeyv0180)
    - [1.4.26 /goal 完成契約（Completion Contracts）（v0.18.0+）](#1426-goal-完成契約completion-contractsv0180)
    - [1.4.27 訂閱管理與密碼管理器整合（v0.19.0+）](#1427-訂閱管理與密碼管理器整合v0190)
    - [1.4.28 智慧審批預設化與配送保證（v0.19.0+）](#1428-智慧審批預設化與配送保證v0190)
    - [1.4.29 A2A（Agent-to-Agent）協定 v1.0（v0.20.0+）](#1429-a2aagent-to-agent協定-v10v0200)
    - [1.4.30 即時對話式語音（v0.20.0+）](#1430-即時對話式語音v0200)
    - [1.4.31 簽章式 Outbound Webhook（v0.20.0+）](#1431-簽章式-outbound-webhookv0200)
    - [1.4.32 Desktop 平台化：Artifacts 與 Plugin SDK（v0.20.0+）](#1432-desktop-平台化artifacts-與-plugin-sdkv0200)
    - [1.4.33 CLI 強化指令與中途導引（v0.20.0+）](#1433-cli-強化指令與中途導引v0200)
    - [1.4.34 Bot Mode — Profile 具名化與群組協作（v0.21.0+）](#1434-bot-mode--profile-具名化與群組協作v0210)
    - [1.4.35 hermes peer — 跨 Gateway Agent 直訊（v0.21.0+）](#1435-hermes-peer--跨-gateway-agent-直訊v0210)
    - [1.4.36 Cron 記憶化與 continuity 連續性（v0.21.0+）](#1436-cron-記憶化與-continuity-連續性v0210)
    - [1.4.37 Live Subagent Orchestration（v0.21.0+）](#1437-live-subagent-orchestrationv0210)
    - [1.4.38 MCP Command Center 與 hermes:// Deep Link（v0.21.0+）](#1438-mcp-command-center-與-hermes-deep-linkv0210)
    - [1.4.39 Agent 驅動的應用內瀏覽器（v0.21.0+）](#1439-agent-驅動的應用內瀏覽器v0210)
    - [1.4.40 CLI Power Wave（v0.21.0+）](#1440-cli-power-wavev0210)
    - [1.4.41 model_overrides — 免等改版的模型參數覆寫（v0.21.0+）](#1441-model_overrides--免等改版的模型參數覆寫v0210)
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
  - [3.11 Recurring Loops（/loop）與 Session Heartbeats](#311-recurring-loopsloop與-session-heartbeats)
- [第四章：安裝與環境建置](#第四章安裝與環境建置)
  - [4.1 系統需求](#41-系統需求)
  - [4.2 快速安裝（Linux / macOS / WSL2）](#42-快速安裝linux--macos--wsl2)
  - [4.3 Native Windows 安裝](#43-native-windows-安裝)
  - [4.4 Docker / Podman 部署](#44-docker--podman-部署)
  - [4.5 Nix Flake 安裝](#45-nix-flake-安裝)
  - [4.6 設定 API Key](#46-設定-api-key)
  - [4.7 設定檔說明](#47-設定檔說明)
  - [4.8 Managed Scope（組織層級設定釘選）](#48-managed-scope組織層級設定釘選)
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
  - [6.10 Batch Processing 與 Trajectory Format](#610-batch-processing-與-trajectory-format)
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
  - [9.2 成本控制](#92-成本控制)
  - [9.3 效能優化](#93-效能優化)
  - [9.4 Logging / Monitoring](#94-logging--monitoring)
  - [9.5 錯誤處理與重試機制](#95-錯誤處理與重試機制)
  - [9.6 Tips & Best Practices](#96-tips--best-practices)
  - [9.7 風險評估與治理考量（企業導入前必讀）](#97-風險評估與治理考量企業導入前必讀)
    - [9.7.1 資安揭露制度現況](#971-資安揭露制度現況)
    - [9.7.2 貢獻者規模與專案永續性（Bus Factor）](#972-貢獻者規模與專案永續性bus-factor)
    - [9.7.3 與其他 Coding Agent 的能力定位比較](#973-與其他-coding-agent-的能力定位比較)
    - [9.7.4 Nous Portal 訂閱定價與總持有成本（TCO）](#974-nous-portal-訂閱定價與總持有成本tco)
    - [9.7.5 生態系鎖定風險](#975-生態系鎖定風險)
    - [9.7.6 企業導入前風險檢查清單](#976-企業導入前風險檢查清單)
  - [9.8 Egress 憑證注入代理（iron-proxy）— 沙箱零信任外連](#98-egress-憑證注入代理iron-proxy-沙箱零信任外連)
- [第十章：部署與維運（DevOps）](#第十章部署與維運devops)
  - [10.1 Docker 部署](#101-docker-部署)
  - [10.2 Kubernetes 部署](#102-kubernetes-部署)
  - [10.3 CI/CD 流程](#103-cicd-流程)
  - [10.4 滾動升級](#104-滾動升級)
  - [10.5 災難復原（DR）](#105-災難復原dr)
- [第十一章：升級與版本管理](#第十一章升級與版本管理)
  - [11.1 升級策略](#111-升級策略)
  - [11.2 相容性管理](#112-相容性管理)
  - [11.3 Migration 設計](#113-migration-設計)
- [第十二章：實戰案例](#第十二章實戰案例)
  - [12.1 AI Coding Agent](#121-ai-coding-agent)
  - [12.2 智慧客服 Agent](#122-智慧客服-agent)
  - [12.3 銀行流程自動化 Agent](#123-銀行流程自動化-agent)
  - [12.4 多媒體創作 Agent](#124-多媒體創作-agent)
- [第十三章：常見問題（FAQ）](#第十三章常見問題faq)
  - [Q1：Agent 無法學習 / 不建立 Skill？](#q1agent-無法學習--不建立-skill)
  - [Q2：Memory 佔用過多空間？](#q2memory-佔用過多空間)
  - [Q3：Token 成本過高？](#q3token-成本過高)
  - [Q4：模型切換失敗？](#q4模型切換失敗)
  - [Q5：Gateway 連線不穩定？](#q5gateway-連線不穩定)
  - [Q6：Windows 環境怎麼用？](#q6windows-環境怎麼用)
  - [Q7：如何與 VS Code 整合？](#q7如何與-vs-code-整合)
  - [Q8：MCP 伺服器連線失敗？](#q8mcp-伺服器連線失敗)
  - [Q9：Voice Mode 無法使用？](#q9voice-mode-無法使用)
  - [Q10：如何查看 Agent 的完整執行日誌？](#q10如何查看-agent-的完整執行日誌)
  - [Q11：如何在多個專案間切換？](#q11如何在多個專案間切換)
  - [Q12：Autonomous Curator 會刪除重要技能嗎？（v0.12.0）](#q12autonomous-curator-會刪除重要技能嗎v0120)
  - [Q13：hermes -z 和普通模式有何不同？（v0.12.0）](#q13hermes--z-和普通模式有何不同v0120)
  - [Q14：如何使用 Background Sessions？（v0.12.0）](#q14如何使用-background-sessionsv0120)
  - [Q15：如何配置 Prompt Cache？（v0.12.0）](#q15如何配置-prompt-cachev0120)
  - [Q16：Multi-agent Kanban 如何設定？（v0.13.0）](#q16multi-agent-kanban-如何設定v0130)
  - [Q17：如何啟用 i18n（多語系）介面？（v0.13.0）](#q17如何啟用-i18n多語系介面v0130)
  - [Q18：video_analyze 工具怎麼用？（v0.13.0）](#q18video_analyze-工具怎麼用v0130)
  - [Q19：原本用 brew／pip 安裝，現在升級失敗怎麼辦？（v0.20.0）](#q19原本用-brew-install-hermes-agent-或-pip-install-hermes-agent-安裝現在升級失敗怎麼辦v0200)
  - [Q20：升級後危險指令不再每次都問我，是不是有安全問題？（v0.19.0）](#q20升級後危險指令不再每次都問我是不是有安全問題v0190)
  - [Q21：什麼時候該用 A2A、Kanban 或 delegate_task？（v0.20.0）](#q21什麼時候該用-a2a什麼時候該用-kanban-或-delegate_taskv0200)
  - [Q22：官方說「Hermes 完全免費」，為什麼還有月費方案？](#q22官方說hermes-完全免費為什麼還有月費方案)
  - [Q23：升級 v0.21.0 後多出一堆「bot」，這是什麼？怎麼關掉？（v0.21.0）](#q23升級-v0210-後多出一堆bot這是什麼有風險嗎怎麼關掉v0210)
  - [Q24：hermes egress（iron-proxy）和 hermes proxy 有什麼不同？](#q24hermes-egressiron-proxy和-hermes-proxy-有什麼不同)
  - [Q25：/loop、/goal、Cron 該用哪個？](#q25loopgoalcron-三個看起來都是重複執行該用哪個)
  - [Q26：v0.21.0 把委派併發預設值調高了，成本會失控嗎？](#q26v0210-把委派併發預設值調高了成本會失控嗎)
  - [Q27：Managed Scope 可以當作正式的權限控管邊界嗎？](#q27managed-scope-可以當作正式的權限控管邊界嗎)
  - [Q28：Tool Search 值得開嗎？什麼情況下反而變慢？](#q28tool-search-值得開嗎什麼情況下反而變慢)
- [第十四章：Hermes Desktop App（v0.16.0+，v0.20.0 起成為完整平台）](#第十四章hermes-desktop-appv0160v0200-起成為完整平台)
  - [14.1 架構概覽](#141-架構概覽)
  - [14.2 安裝方式](#142-安裝方式)
  - [14.3 核心功能](#143-核心功能)
  - [14.4 解除安裝](#144-解除安裝)
  - [14.5 企業部署建議](#145-企業部署建議)
- [第十五章：Bot Mode 與多 Agent 群組協作（v0.21.0）](#第十五章bot-mode-與多-agent-群組協作v0210)
  - [15.1 概念定位：bot 即 profile](#151-概念定位bot-即-profile)
  - [15.2 建立與設定 Bot](#152-建立與設定-bot)
  - [15.3 群組聊天機制](#153-群組聊天機制)
  - [15.4 hermes peer — 跨 Gateway Agent 直訊](#154-hermes-peer--跨-gateway-agent-直訊)
  - [15.5 五種多 Agent 機制選型對照](#155-五種多-agent-機制選型對照)
  - [15.6 企業治理與關閉方式](#156-企業治理與關閉方式)
  - [15.7 CLI 對應指令](#157-cli-對應指令)
- [附錄 A：檢查清單（Checklist）](#附錄-a檢查清單checklist)
  - [A.1 安裝檢查清單](#a1-安裝檢查清單)
  - [A.2 API Key 設定檢查清單](#a2-api-key-設定檢查清單)
  - [A.3 安全檢查清單](#a3-安全檢查清單)
  - [A.4 生產部署檢查清單](#a4-生產部署檢查清單)
  - [A.5 團隊導入檢查清單](#a5-團隊導入檢查清單)
  - [A.6 升級檢查清單](#a6-升級檢查清單)
- [附錄 B：指令速查表](#附錄-b指令速查表)
  - [B.1 CLI 指令（依功能分類）](#b1-cli-指令依功能分類)
  - [B.2 對話中斜線指令](#b2-對話中斜線指令)
- [附錄 C：環境變數參考](#附錄-c環境變數參考)
  - [C.1 模型 Provider 金鑰](#c1-模型-provider-金鑰)
  - [C.2 訊息平台 Token](#c2-訊息平台-token)
  - [C.3 工具與整合](#c3-工具與整合)
  - [C.4 系統與行為控制](#c4-系統與行為控制)
- [附錄 D：Provider 完整清單](#附錄-dprovider-完整清單)
  - [D.1 雲端推理 Provider](#d1-雲端推理-provider)
  - [D.2 自架／本地推理後端](#d2-自架本地推理後端)
  - [D.3 第三方 OpenAI 相容端點（經官方文件證實可用）](#d3-第三方-openai-相容端點經官方文件證實可用)
- [參考資源](#參考資源)
<!-- TOC-AUTO-END -->

---

## 第一章：Hermes Agent 概述

### 1.1 技術背景與發展

Hermes Agent 是由 **Nous Research** 開發的開源自我改進 AI Agent。Nous Research 是知名的 AI 研究實驗室，以訓練 Hermes、Nomos、Psyche 等開源模型聞名。

**發展歷程**：

| 版本 | 日期 | 重要里程碑 |
| ------ | ------ | ------------ |
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
| v0.16.0 | 2026.06.05 | **The Surface Release**：**Hermes Desktop App**（原生 Electron 桌面應用：macOS/Linux/Windows、一鍵安裝、應用內自動更新、拖放檔案、剪貼簿圖片貼入、Cmd+K 命令面板、狀態列模型選擇器、多 Profile 併行 Session、遠端 Gateway 連線 via OAuth/密碼認證）、**Dashboard 全面管理面板**（Channels 設定、MCP 目錄管理、Credential 管理、Webhook、記憶設定、Gateway 控制、System 檢查更新 + Debug Share）、**Quick Setup via Nous Portal**（`hermes portal` 一鍵快速設定）、**Fuzzy Model Picker**（Desktop/Web/TUI/CLI 統一模糊搜尋、每小時目錄刷新）、**`/undo [N]`**（撤回最近 N 輪對話 + 訊息預填）、**NVIDIA/skills 信任 Tap**（與 OpenAI/Anthropic/HuggingFace 並列預設信任來源）、**精簡預設 Skill Set**（移除冗餘技能、重型 Skills 移至 optional、`environments:` 相關性閘門）、**簡體中文 Desktop 翻譯**（完整 GUI i18n）、**選擇預設介面**（`cli` 或 `tui`，`--cli` 覆寫）、**CVE-2026-48710 Starlette 修正**、**SSRF off-loop 強化**、874 commits / 542 PR / 170 貢獻者 |
| v0.17.0 | 2026.06.19 | **The Reach Release**：**iMessage via Photon Spectrum**（無需 Mac relay，`hermes photon login` 裝置碼認證，第 24 平台）、**Raft Agent Network**（第 25 平台：外部 agent network gateway channel bridge，隱私合約設計）、**Background/Async Subagents**（`delegate_task(background=true)` 背景子代理，完成後結果自動回注對話）、**Image-to-image Editing**（`image_generate` 支援圖像編輯/變換，所有圖片 Provider 通用）、**Automation Blueprints**（自然語言排程模板：Dashboard 表單 / CLI slash command / Messenger 對話 / Docs 目錄統一呈現，無需 cron 語法）、**Cursor grok-composer-2.5-fast**（xAI Grok 訂閱直接使用 Cursor Composer 模型，200k context）、**Full Profile Builder**（Dashboard 中建置完整 Profile：選模型、選 Skills、附加 MCP servers、全機器跨 Profile 管理 + 全域切換器）、**Skills Hub Browser 重做**（Connected Hubs、Featured section、安全掃描、完整預覽後安裝）、**Memory 原子批次操作**（`operations` 陣列：add/replace/remove 單次呼叫原子執行，character budget 自動管理）、**Secure Dashboard Login**（401 OAuth gate 強化、WebSocket auth token、`public_url` override 警告）、**WhatsApp Business Cloud API**（官方 Meta 第一方 API，無需 bridge）、**Telegram Bot API 10.1 Rich Text**（原生 rich message 格式化）、**Curator Cost Optimization**（預設 deterministic inactivity sweep 免費，LLM consolidation 改為 opt-in `curator.consolidate: true`）、**Desktop 深化**（可重綁快捷鍵、OS 原生通知、Subagent watch-windows、Composer model selector、RTL/bidi 自動偵測、VS Code 主題安裝、per-thread drafts）、~1,475 commits / ~800 PR / 245 貢獻者 |
| v0.18.0 | 2026.07.01 | **The Judgment Release**：**P0/P1 議題全數清零**（3 P0 + 493 P1，計 496 議題／196 PR 一次性清空，官方宣示此後持續維持零 P0/P1）、**Mixture-of-Agents（MoA）一級模型化**（具名 MoA 預設可在任何模型選擇器直接選用，如同挑選 Claude/GPT/Grok；各參考模型獨立展示完整推理區塊，聚合器最終答案即時串流；`/moa` 為一次性語法糖）、**`/goal` 完成契約（Completion Contracts）**（使用者定義「完成」的可驗證標準，標準目標迴圈依實證判定完成度而非模型自稱、`pre_verify` 自訂檢查掛鉤）、**`/learn`**（將任意目錄／URL／剛示範的操作萃取為可重用 Skill，依專案 `CONTRIBUTING.md` 標準撰寫）、**`/journey`**（CLI／TUI 學習時間軸，Desktop 版提供可互動記憶圖）、**Google Vertex AI** 原生 Provider（Service Account JSON／ADC 自動換發短期 OAuth2 Token，免靜態金鑰）、**Gateway Scale-to-zero + Drain 協調**（代管 Gateway 閒置自動休眠，重啟／遷移前協調排空進行中對話避免中斷）、`/prompt` 開啟 `$EDITOR` 撰寫長篇提示、移除 `google-gemini-cli`／`google-antigravity` OAuth Provider、~1,720 commits / 998 PR / 2,215 files / 381 貢獻者 |
| v0.18.1 | 2026.07.07 | 基礎設施穩定化補丁（非精選版本，官方政策：僅供 Docker image／代管服務／全新安裝有穩定版本可依附，完整分類說明隨下個 Minor 版本補齊）：~667 commits，Windows 安裝程式／更新程式自我修復、Dashboard 與 Gateway 一般性修正、WhatsApp Dashboard 配對流程 |
| v0.18.2 | 2026.07.08 | 同日追加修正：WhatsApp Baileys 依賴由釘選 git commit 改為使用已發布之 npm `7.0.0-rc13` 版本，修正 Docker image 建置可靠性 |
| v0.19.0 | 2026.07.20 | **The Quicksilver Release**：**首個 Token 回應時間全平台縮短約 80%**（冷啟動「Initializing agent...」4.3s → 0.9s，透過延遲 Discord 能力偵測快取、略過非 Ollama Provider 探測等手法）、推理模型預設即時串流顯示思考過程、**Desktop 應用約 20 項效能優化**（串流 Markdown 解析器 CPU 降 14 倍、Review Pane Diff 虛擬化、大型逐字稿快速切換 Session）、**`/subscription` 與 `/topup`**（終端機內完整訂閱管理：查看方案與剩餘額度、升降級預覽與排程變更）、**密碼管理器整合**（可插拔 `SecretSource` 介面，支援 Bitwarden 與 1Password `op://` 參照、多金鑰庫並行、明確優先序，整併 11 個社群 PR 為單一介面）、**智慧審批預設啟用**（LLM 獨立審查每個被標記指令是否放行，取代逐次詢問使用者；搭配自訂拒絕規則與 `/deny <原因>`）、**背景子代理即時逐字稿**（`tail -f` 可追蹤每個子代理的即時工具呼叫）、**配送保證台帳**（Gateway 於回應產生與平台送達確認之間當機時，不再靜默遺失回應，於 `state.db` 記錄並於重啟後補送，修復橫跨 Telegram/Discord/Slack 的 P1 級靜默遺失風險）、**Profile-based Gateway 路由**（單一共用 Bot Token 依 Guild／頻道／討論串路由至不同 Profile，各自獨立設定／技能／記憶／秘密）、新增 **Fireworks AI**（躍升 Provider 選擇器第二順位）、DeepInfra、Upstage Solar Provider，新增 GPT-5.6 系列、grok-4.5（GA）、`claude-fable-5`／`claude-sonnet-5`，新增 `max`／`ultra` 推理強度層級、**`hermes sessions export`**（Markdown／Quarto／HTML／Hugging Face 格式，支援 `--redact`）、~2,245 commits / 1,065 PR / 450+ 貢獻者（官方稱「史上最大貢獻者窗口」） |
| v0.19.1 | 2026.07.30 | 基礎設施穩定化補丁：~2,789 commits，Gateway／語音子系統／Desktop／安裝程式全面修正波，新增 Buzz（Nostr 協定）平台雛型、FLUX3 影片生成、Telegram 媒體可靠性與語音模式回歸修正 |
| v0.20.0 | 2026.08.03 | **The Herald Release**：**A2A（Agent-to-Agent）v1.0 協定**（收斂長年擱置的 issue #514；純外掛實作於 `plugins/platforms/a2a/`，零核心程式碼異動；出站 `a2a_discover/a2a_call/a2a_list/a2a_history/a2a_orchestrate` 工具集；入站服務 `/.well-known/agent-card.json` Agent Card、JSON-RPC 1.0 + SSE 串流、按 Peer 分別的 Bearer Token、SSRF 防護 + HMAC 簽章推播、防提示注入過濾、反迴圈輪次上限；已通過官方 `a2a-sdk` E2E 測試套件）、**即時對話式語音**（逐句串流播放、使用者可隨時「Barge-in」插話中斷、裝置端喚醒詞偵測音檔不外流、WhatsApp／Feishu／DingTalk／LINE／QQ／Photon／微信語音全平台支援）、**簽章式 Outbound Webhook**（HMAC-SHA256、GitHub 風格 `X-Hermes-Signature-256` 標頭、fire-and-forget 佇列不阻塞工具呼叫、notify-only 設計不可回注上下文）、**具憑證研究引註**（`grounded-citations` Skill：逐句比對原文出處避免幻覺引用，並提供事實查核模式）、**Desktop 正式成為「平台」**：**Artifacts**（大型 HTML／SVG／程式碼區塊自動升級為版本化卡片，`<iframe sandbox="allow-scripts">` 沙箱執行）+ **Plugin SDK**（Kanban 作為首個參考外掛，`ctx.rest`／`ctx.storage`／`ctx.i18n`／`ctx.onDispose` 等擴充點）+ 全域快捷鍵速記視窗 + RFC 8252 原生桌面登入，**CLI 強化指令**（`!command` 免佔用模型輪次直接執行 Shell、`/init` 掃描專案生成 AGENTS.md、`/diff`、`/context`、`/focus`）、**中途導引（Mid-turn Redirect）**（執行中可即時輸入修正方向）、工具自我修復波（截斷輸出可回讀、`patch` 冪等偵測、工具呼叫迭代上限由 90 提升至 500）、壓縮機制大改（per-turn 微壓縮、Ghost-skill 防護避免被剪除技能悄悄重現）、**Node.js 26 成為必要條件**、**Homebrew／PyPI／pip wheel 安裝管道正式停用**（僅保留 Shell Installer／Docker／Nix 三種官方安裝管道）、Vercel AI Gateway 與 Vercel Sandbox 回歸（現代化重寫）、~3,650 commits / 1,400 PR / 647 貢獻者 |
| v0.20.1 | 2026.08.13 | 基礎設施穩定化補丁：1,444 commits / 656 PR，涵蓋 2,172 個檔案，橫跨 Desktop 應用、Gateway 平台、安裝程式、工具系統與 Provider 目錄的廣泛穩定化修正 |
| v0.20.2 | 2026.08.16 | 補丁（~397 PR）：**多 Gateway Connections 註冊表**（單一 Desktop 管理多個 Hermes 實例）、MCP 伺服器健康檢查、Windows 更新探測、Cron 強化、**LiteLLM Claude on OpenAI wire 的 Prompt Caching** |
| v0.20.3 | 2026.08.17 | 補丁（~125 PR）：**MCP 2.x 遷移**（⚠️ 升級破壞性變更，見 11.1.14）、**Bot Mode 以 bundled plugin 形式內建**、CommandCode 新 Provider、Python runtime 強化、Cron 排程器 EMFILE 耗盡自動復原 |
| v0.20.4 | 2026.08.18 | 補丁（~74 PR）：Desktop glass／translucency 介面、側邊欄改為 `SESSIONS｜BOTS` 分頁、Bot Mode 群組聊天修正、**Skill 安裝前安全掃描**、Kanban 原生系統通知 |
| v0.20.5 | 2026.08.21 | 補丁（~323 PR）：**Bot Mode 群組房間（Group Rooms）**、可摺疊摘要、**keyless web tier**（免金鑰網頁層）、CLI 打磨浪潮、**Cron 取得持久記憶與 per-job 推理強度控制** |
| v0.20.6 | 2026.08.27 | 補丁（~525 PR）：**同意閘門式 Profile 瀏覽**（consent-gated profile browsing）、**遠端 MCP 目錄擴充至 50+ 伺服器**、工具結果 TTL 快取、**持久化事故確認台帳**（durable incident acknowledgments）、多項新模型 |
| v0.21.0 | 2026.08.31 | **The Pantheon Release**（**目前最新版本**，自 v0.20.0 起累計 ~5,800 commits / 2,475 PR / 5,680 檔案 / 869,000 插入 / 135,000 刪除 / ~2,100 議題關閉 / 760+ 貢獻者，為本專案史上最大規模 Minor 發布）：**Bot Mode 內建化且預設開啟**（每個 Profile 成為具名 Agent，含依名稱決定的頭像、共享名冊、Discord 風格群組聊天，最多 6 bot 同室、3 輪序列回應）、**`hermes peer` 跨 Profile／跨 Gateway Agent 直訊**（對話持久且可稽核，落於各 Agent 的正規 Bot Chat）、**Cron 記憶化與連續性**（排程任務如同一般 Agent 載入持久記憶、`continuity=true` 跨執行帶入輸出、per-job 持久 notepad、monitor 模式無變更時以雜湊抑制跳過 LLM 呼叫）、**Live Subagent Orchestration**（`delegate_task` 支援執行中列出／中途導引／提前停止並保留部分結果，加上 JSON Schema 結構化輸出驗證與逐次委派成本追蹤；預設值提高至 250 iterations／10 並行子代理）、**MCP Command Center**（伺服器與目錄整併為單一 Desktop 頁面、拖放匯入、背景健康檢查、fleet 成本／用量疊層、`hermes://` deep link 一鍵安裝）、**CLI Power Wave**（`Ctrl+P` 模糊命令面板、`/model` 互動篩選、`/status` 顯示推理模式／待審批／context 用量、狀態列即時 cache-hit%／延遲／tokens-per-sec、全域緊急停止、Terminal Pets）、**Agent 驅動的應用內瀏覽器**（導航／點擊／讀取，可彈出至系統瀏覽器）、**6 個新 Provider**（Meta Model API〔Muse Spark〕／CommandCode〔GOAT・Pro・Max〕／Actual Computer／Tencent TokenPlan／Nebius Token Factory／Ramp Router）與 `model_overrides` 免改版覆寫、**安全強化波**（`AGENTS.md`／skills／memory 寫入一律需審批以阻擋提示注入改寫常規指令、終端錯誤與 `.env` 讀取與 checkpoints 與 ACP log 的秘密外洩清掃、Windows 破壞性指令納入審批、Blender MCP 目錄項目因上游遭入侵而下架、Plugin 安裝納入 Tier-1 安全掃描、macOS TCC 身分跨更新存續）；**已回退不出貨**：Model Council（`/council`）、DCP context engine、WS-only Gateway Server |

**核心數據**（截至 2026.09.01，逐條核對 GitHub REST API 一手資料）：

- GitHub Stars：**239,282**
- Forks：**48,843**
- Open Issues：**38,350**（含 Issue 與 PR）
- Watchers（訂閱者）：**933**
- 最近推送（`pushed_at`）：**2026-09-01**（開發活躍度極高，主分支 `main`）
- 主要語言：**Python** 為主，TypeScript 次之（Desktop／Dashboard），另有 JavaScript／Shell／PowerShell／Nix 等
- 倉庫主題標籤：`ai`、`ai-agents`、`anthropic`、`chatgpt`、`claude`、`claude-code`、`codex`、`hermes`、`llm`、`nous-research`、`openai`
- 授權：**MIT License**（可商用，Hermes Agent 軟體本體完全免費）
- 專案建立日：2025-07-22；累計 Releases：**31 個**（GitHub Releases API 記錄自 v0.2.0 起算，v0.21.0 為最新）

> ⚠️ **貢獻者人數存在口徑差異，企業評估時建議留意**：Hermes 官方各版本 Release Notes 慣例宣稱「370～760+ 貢獻者」（v0.21.0 宣稱 760+），但透過 GitHub `/contributors` API 直接查證僅得數百個具名帳號——官方數字額外納入了 commit co-author 掛名與未直接合併之社群 PR 貢獻，兩者衡量口徑不同，非造假亦非錯誤，但代表專案核心可長期維運人力的真實規模，需另行評估。事實上 v0.21.0 官方自行揭露的核心團隊 PR 分布高度集中：`@teknium1` 一人即約 1,340 個 merged PR，其次 `@kshitijk4poor` 374 個、`@OutThisLife` 209 個，其餘核心成員多為兩位數——**Bus Factor 風險並未因總貢獻者數上升而改善**（詳見 9.7 節風險評估）。

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
| ------ | --------------------- | -------------- |
| 記憶 | 僅單次對話 | 跨對話長期記憶（FTS5 + Vector DB）+ Session Key 隔離 |
| 學習 | 不會學習 | 內建 Learning Loop，自動封裝技能 + Autonomous Curator |
| 工具使用 | 有限（Plugins/GPTs） | 70+ 內建工具 + MCP 擴展（SSE Transport + OAuth 轉發） |
| 執行環境 | 雲端沙箱 | 本地 / Docker / SSH / Modal / Daytona / Singularity（6 種後端） |
| 多平台 | Web UI 為主 | CLI + TUI + Desktop App + 30+ 通訊平台／連接器（Telegram/Discord/Slack/Matrix/WhatsApp（Baileys＋官方 Cloud API 雙軌）/Signal/Email/SMS/DingTalk/Feishu/WeCom/微信/iMessage（BlueBubbles＋Photon 雙軌）/Mattermost/Home Assistant/QQBot/元寶/Microsoft Teams/Google Chat/LINE/SimpleX Chat/ntfy/Raft/Buzz（Nostr）/A2A/Webhook/API Server 等，另有實驗性 Hermes Relay 連接器框架） |
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
| ------ | ------------------- | ---------------------- | ------------------ |
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
- **全面管理面板**（v0.16.0）：Dashboard 升級為完整管理面板：
  - **Channels 設定**：圖形化管理所有通訊平台連線
  - **MCP 目錄管理**：瀏覽、安裝、設定 MCP 伺服器
  - **Credential 管理**：集中管理所有 API Key 與 OAuth 憑證
  - **Webhook 管理**：設定與監控 Webhook 端點
  - **記憶設定**：配置 Memory Provider、容量、自動壓縮策略
  - **Gateway 控制**：啟停 Gateway、查看連線狀態、Debug Share
  - **System 頁面**：檢查更新 + Debug Share 匯出
- **Fuzzy Model Picker**（v0.16.0）：所有介面統一模糊搜尋模型，每小時自動刷新目錄
- **Quick Setup**（v0.16.0）：`hermes portal` 透過 Nous Portal 引導快速設定
- **Full Profile Builder**（v0.17.0）：在 Dashboard 中建置完整 Profile（模型 + Skills + MCP servers + 全域切換器）
- **Automation Blueprints 管理**（v0.17.0）：視覺化管理排程模板
- **Secure Login**（v0.17.0）：401 OAuth gate 強化 + WebSocket auth token

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

#### 1.4.14 PyPI 套件安裝（v0.14.0 起，**v0.20.0 已停用**）

v0.14.0 曾正式發佈 PyPI 套件供 `pip` 直接安裝：

```bash
# ⚠️ 以下管道已於 v0.20.0 停用，僅作歷史記錄，請改用 4.2 節的 Shell Installer / Docker / Nix
pip install hermes-agent
uv tool install hermes-agent
```

> **v0.20.0 變更**：官方基於安裝可靠性考量，正式停用 Homebrew 與 PyPI／pip wheel 兩種管道（詳見 4.2.3 節），僅保留 Shell Installer、Docker、Nix 三種官方支援的安裝方式。

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
- **供應鏈審計子指令**：以 OSV.dev 掃描所有相依套件漏洞（v0.15.0 導入時名為 `hermes audit`，**現行指令為 `hermes security audit`**）

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

#### 1.4.19 Hermes Desktop App（v0.16.0+）

v0.16.0（The Surface Release）推出原生 Electron 桌面應用，提供完整圖形化操作介面：

| 特性 | 說明 |
| ------ | ------ |
| 跨平台安裝 | macOS（DMG/Brew）、Linux（AppImage/deb）、Windows（NSIS installer） |
| 應用內自動更新 | 偵測新版本後自動下載並安裝，無需手動介入 |
| 拖放檔案 & 剪貼簿圖片 | 直接拖入檔案或 Cmd/Ctrl+V 貼入螢幕截圖 |
| 命令面板 | `Cmd+K` / `Ctrl+K` 快速執行 slash commands、切換模型與 Profile |
| 狀態列模型選擇器 | 即時切換 LLM 模型，支援 Fuzzy 搜尋 |
| 多 Profile 併行 Session | 同時開啟多個 Profile 對話視窗 |
| 遠端 Gateway 連線 | 透過 OAuth 或密碼認證連至遠端 Gateway 實例 |
| OS 原生通知 | 子代理完成、Kanban 任務完成時推送系統通知 |

> **企業場景**：非技術人員（PM、QA）可透過 Desktop App 直接與 Agent 互動，無需接觸命令列。

#### 1.4.20 Background Subagents（v0.17.0+）

v0.17.0 允許以背景模式啟動子代理，不阻塞主對話流程：

```python
# 語法範例
delegate_task(
    task="分析所有 PR 的安全風險",
    background=True  # 背景執行，完成後結果自動回注對話
)
```

- **非阻塞**：主 Agent 可繼續處理其他工作
- **結果回注**：背景子代理完成後自動將結果注入當前對話上下文
- **進度追蹤**：Desktop App 提供 Subagent watch-windows 即時觀察進度
- **搭配 Kanban**：背景 Subagent 可作為 Kanban Worker 處理佇列任務

#### 1.4.21 Image Editing（v0.17.0+）

`image_generate` 工具擴展支援圖像到圖像編輯：

- **編輯模式**：提供參考圖 + 文字指令，產生修改後版本
- **通用後端**：所有圖片 Provider（Krea、FAL、DALL-E 等）均可使用
- **適用場景**：UI mockup 修改、圖片風格轉換、局部區域重繪

#### 1.4.22 Automation Blueprints（v0.17.0+）

自然語言排程模板，取代傳統 cron 語法：

```yaml
# 範例：每日早上 9 點檢查安全漏洞
name: daily-security-scan
schedule: "每天早上 9 點"
task: "掃描所有專案的已知漏洞，彙整報告到 Slack #security 頻道"
profile: security-ops
```

- **多入口統一**：Dashboard 表單 / CLI slash command / Messenger 對話 / Docs 目錄
- **自然語言排程**：「每週一早上」、「每隔 4 小時」等描述自動轉換
- **條件觸發**：可搭配 webhook 事件或檔案變更作為觸發條件
- **Dashboard 管理**：視覺化管理所有 Blueprint、執行歷史與結果

#### 1.4.23 Memory Atomic Batch Operations（v0.17.0+）

`memory` 工具支援原子批次操作，一次呼叫完成多項記憶異動：

```json
{
  "operations": [
    {"action": "add", "key": "user_preference_theme", "value": "dark"},
    {"action": "replace", "key": "project_status", "value": "phase-2"},
    {"action": "remove", "key": "deprecated_config"}
  ]
}
```

- **原子性**：全部操作成功或全部回滾，避免部分寫入導致不一致
- **Character Budget 自動管理**：接近容量上限時自動壓縮或建議移除舊記憶
- **效能提升**：減少多次往返呼叫，單次 tool call 即完成批次異動

> **實務案例**：某金融團隊將 Hermes Agent 部署在內部 VPS，使用 Anthropic Claude 作為主模型處理程式碼審查，搭配免費的 MiMo v2 Pro（Nous Portal）進行摘要與壓縮，Token 成本降低 60%。

#### 1.4.24 Mixture-of-Agents（MoA）一級模型化（v0.18.0+）

v0.18.0 起，MoA 不再是實驗性功能，而是與 Claude／GPT／Grok 同等地位、可在任何模型選擇器中直接挑選的「一級模型」：

- **具名預設**：在 CLI／TUI／Desktop／Gateway 的模型選擇器中，MoA 預設與一般模型並列顯示
- **可視化推理**：每個參考模型的完整推理過程各自成一個標示區塊呈現，聚合器（Aggregator）的最終答案即時串流輸出，不再等待整體完成才顯示
- **可靠性強化**：參考／聚合模型皆走各自真實 Provider 路徑；Context Window 依聚合器實際能力解析（不再套用 256K 預設值）
- **`/moa`**：一次性語法糖，套用預設組合執行單一提示後即還原；持久切換仍透過模型選擇器

```bash
# 查看與設定 MoA 組合
hermes moa list
hermes moa configure
```

#### 1.4.25 自我學習強化：`/learn` 與 `/journey`（v0.18.0+）

v0.18.0 大幅強化 Learning Loop 的可操作性：

- **`/learn <對象>`**：對任意目錄、URL，或剛剛示範完成的操作流程執行，Agent 會依專案 `CONTRIBUTING.md` 定義的標準，萃取並撰寫成可重用 Skill
- **`/journey`**：CLI／TUI 顯示已累積記憶與技能的學習時間軸，可直接編輯或刪除；Desktop 版另提供可拖拽探索的放射狀記憶圖（Memory Graph）
- **推論後自我改進效率提升**：判斷是否儲存記憶／技能的推論改走輔助模型並僅摘要上下文，不再重播整段對話，降低成本

#### 1.4.26 `/goal` 完成契約（Completion Contracts）（v0.18.0+）

`/goal` 的「完成」判定機制由模型自我宣稱，改為可驗證的具體契約：

- **契約結構**：Outcome／Verification／Constraints／Boundaries／Stop_when 等欄位明確定義完成標準
- **證據台帳**：每個 Profile 範疇的標準專案檢查（如測試、Lint）留下可查證紀錄，並可透過 `pre_verify` 掛鉤加入自訂檢查
- **`verify-on-stop` 預設關閉**：僅文件類編輯自動略過驗證，訊息類介面則直接停用此機制
- **`/goal wait <pid>`**：可讓持久目標迴圈暫停等待背景程序完成後再繼續

#### 1.4.27 訂閱管理與密碼管理器整合（v0.19.0+）

v0.19.0「The Quicksilver Release」新增終端機內完整訂閱與憑證管理能力：

- **`/subscription` / `/topup`**：直接在 TUI／CLI 查看目前方案與剩餘額度、預覽升降級費用（如「Pay $46.30 並立即升級」）與生效時間，Desktop 版同步提供對應的帳務設定分頁
- **可插拔 `SecretSource` 介面**：新增 **Bitwarden** 與 **1Password**（`op://` 參照）密鑰來源，可同時啟用多個金鑰庫並定義明確優先序與衝突警告；官方將此定位為整併 11 個相互競爭的社群 PR 而成的統一介面，為未來更多金鑰庫供應商保留擴充點

```yaml
# config.yaml — 多密鑰來源設定範例
secrets:
  sources:
    - type: bitwarden
      priority: 1
    - type: 1password
      priority: 2
      vault: "op://Engineering/hermes"
```

#### 1.4.28 智慧審批預設化與配送保證（v0.19.0+）

- **智慧審批（Smart Approvals）成為預設**：Agent 欲執行被標記指令時，改由獨立 LLM 審查者依情境判斷是否放行，而非每次都詢問使用者；每個判定僅涵蓋精確比對到的該次指令。可搭配使用者自訂的拒絕規則（即使 YOLO 模式下仍會阻擋）與 `/deny <原因>` 讓 Agent 得知拒絕理由並自我修正
- **配送保證台帳（Delivery-obligation Ledger）**：修正一項跨 Telegram／Discord／Slack 等全平台的 P1 級靜默遺失風險——過去若 Gateway 在「產生回應」與「確認平台送達」之間當機，該回應會被靜默遺失；現在所有最終回應會先記錄於 `state.db` 持久台帳，Gateway 重啟後自動補送
- **背景子代理即時逐字稿**：`delegate_task` 背景派工現可產出可 `tail -f` 追蹤的即時逐字稿，記錄每個子代理的工具呼叫、結果與回覆；背景派工結果亦透過具擁有權檢查的台帳持久化，即使 Gateway 重啟也不遺失
- **Profile-based Gateway 路由**：單一共用 Bot Token 的 Gateway，現可依 Guild／頻道／討論串路由至不同 Profile，各自套用獨立設定、技能、記憶與秘密

#### 1.4.29 A2A（Agent-to-Agent）協定 v1.0（v0.20.0+）

v0.20.0「The Herald Release」為 Hermes 補上長年缺口——與其他 Agent 互通的標準協定（對應 GitHub 上擱置多年的 issue #514）：

- **純外掛實作**：整個實作位於 `plugins/platforms/a2a/`，**零核心程式碼異動**，包含 `adapter.py`、`protocol.py`、`security.py` 等模組
- **出站方向**：新增（預設關閉的）`a2a` Toolset，提供 `a2a_discover`／`a2a_call`／`a2a_list`／`a2a_history`／`a2a_orchestrate` 工具，讓 Hermes 可探索並呼叫任何符合 A2A 規範的其他 Agent
- **入站方向**：於標準路徑 `/.well-known/agent-card.json` 發布 Agent Card（同時保留舊版 `agent.json` 路徑相容）、JSON-RPC 1.0（PascalCase 方法名 + 舊版別名相容）、SSE 串流、推播通知 CRUD、租戶隔離；入站任務直接路由進即時 Gateway Session
- **安全預設**：僅限 localhost 免 Token 存取、按 Peer 各自的 Bearer Token、入站內容提示注入過濾、出站憑證遮蔽、SSRF 防護 + HMAC 簽章推播回呼、稽核日誌、防迴圈輪次上限
- **協定版本**：明確對齊 **A2A v1.0.1**（Linux Foundation，2026 年 5 月），已通過官方 `a2a-sdk` 端對端測試套件（Agent Card 解析、`SendMessage`、串流）

> **企業應用建議**：A2A 適合「與外部組織的 Agent 互通」場景（例如供應鏈夥伴、合作單位各自的 Agent 系統對接），與內部委派任務優先使用 6.2 節 Subagent 委派或 6.3 節 Multi-agent Kanban 的定位不同，三者互補而非互斥。

#### 1.4.30 即時對話式語音（v0.20.0+）

語音模式由「錄音→轉錄→回覆→播放」的輪替式互動，升級為真正的即時對話：

- **逐句串流播放 + Barge-in 插話**：Hermes 隨回應串流逐句朗讀，使用者可隨時開口打斷，Agent 會停止播放、聆聽並得知自己被中途打斷
- **裝置端喚醒詞**：開放詞彙的自訂喚醒短語（如「Hey Hermes」），偵測完全在裝置端執行、語音不外流；多 Profile 可各自綁定不同喚醒詞
- **語音全平台覆蓋**：WhatsApp、飛書、釘釘、LINE、QQ、Photon（iMessage）、微信等平台送出的語音訊息均可自動轉錄與回覆，並依平台特性自動選擇編碼與字幕呈現方式

#### 1.4.31 簽章式 Outbound Webhook（v0.20.0+）

Hermes 現可將 Session 活動、輪次完成、工具事件等生命週期事件，以簽章方式主動推送到任意 HTTP 端點：

```yaml
# config.yaml
hooks:
  outbound:
    - url: "https://internal.example.com/hermes-events"
      events: ["on_session_end", "subagent_stop", "post_tool_call"]
      secret_env: "HERMES_WEBHOOK_SECRET"
```

- **HMAC-SHA256 簽章**：以 GitHub 風格的 `X-Hermes-Signature-256: sha256=<hex>` 標頭驗證真偽
- **Fire-and-forget 佇列**：單一背景執行緒 + 有界佇列，故障中的接收端不會拖垮工具呼叫；連線錯誤／5xx 有限重試，4xx 不重試
- **Notify-only 設計**：回呼恆為單向通知，不會、也不能將任何內容回注 Agent 上下文（與 Inbound Shell Hooks 明確區隔）

#### 1.4.32 Desktop 平台化：Artifacts 與 Plugin SDK（v0.20.0+）

v0.20.0 起，Hermes Desktop 從「圖形化用戶端」升級為「可擴充的平台」：

- **Artifacts**：大型 HTML 全文件、SVG（≥2,000 字元）或程式碼區塊（≥48 行／3,000 字元）會自動從對話串抽離，成為右側欄的版本化卡片，支援版本切換、原始碼／預覽切換、下載與瀏覽器開啟；HTML 於 `<iframe sandbox="allow-scripts">` 沙箱中執行（不可同源存取、不可跳出導覽），SVG 則經 DOMPurify 淨化
- **Plugin SDK**：Kanban 功能已重寫為此 SDK 的首個參考外掛（預設關閉），對外暴露 `ctx.rest`／`ctx.socket`（外掛專屬 REST/WebSocket）、`ctx.storage`（外掛範疇持久化）、`ctx.i18n`（外掛自帶語系包）、`ctx.onDispose`（停用時保證清理）等擴充點，第三方可據此開發原生等級的 Desktop 擴充功能
- **全域快捷鍵速記視窗**：可在作業系統任何位置以全域熱鍵喚出，將靈感直接記錄進任一 Session
- **RFC 8252 原生桌面登入**：改用系統瀏覽器 + PKCE 完成 OAuth，不再透過內嵌 WebView 儲存 Cookie

#### 1.4.33 CLI 強化指令與中途導引（v0.20.0+）

```bash
!ls -la              # 免佔用模型輪次，直接執行 Shell 指令
/init                 # 掃描專案，自動產生／更新 AGENTS.md
/diff                 # 顯示 staged / all / session 變更
/context              # 檢視目前上下文視窗的組成明細
/focus                # 精簡輸出檢視，隱藏內容可隨時復原
```

- **中途導引（Mid-turn Redirect）**：Agent 執行中若方向偏離，使用者可直接輸入修正內容，進行中的工作會被保留、原始提示不遺失，Agent 據此course-correct
- **`hermes import-agent`**：一鍵將既有 Claude Code 或 Codex CLI 設定遷移至 Hermes
- **工具呼叫迭代上限提升**：單一任務可用的工具呼叫輪次上限由 90 提升至 500，移除長時間自主執行的人為限制

#### 1.4.34 Bot Mode — Profile 具名化與群組協作（v0.21.0+）

v0.21.0 將既有的 Profile 系統升級為「具名 Agent 名冊」：每個 Profile 成為一個有名字、有頭像、有專屬模型／記憶／技能的 **bot**，並可在 Discord 風格的群組房間中彼此協作。

- **內建且預設開啟**：以 bundled plugin 形式隨 Desktop 出貨（v0.20.3 導入、v0.21.0 正式預設啟用），無須額外安裝
- **bot 即 profile**：底層仍是 `~/.hermes/profiles/<name>/`，既有 Profile 資產完全沿用，非新的平行概念
- **群組房間**：最多 6 個 bot 同室，以最多 3 輪序列回應收斂討論，各 bot 依相關性自行決定是否發言
- **企業提醒**：預設開啟代表**未主動關閉即為啟用狀態**，導入前應納入治理決策（關閉方式與完整說明見 [第十五章](#第十五章bot-mode-與多-agent-群組協作v0210)）

#### 1.4.35 `hermes peer` — 跨 Gateway Agent 直訊（v0.21.0+）

讓不同機器、不同 Gateway 上的 Hermes Agent 直接互傳訊息並移交工作成果，且**不需要 Desktop 介入**。

```bash
# 註冊對端 Gateway
hermes peer add research-box --url https://gw.internal:8080 --key "$API_SERVER_KEY"

# 送出一則訊息（可從檔案讀入）
hermes peer dm research-box < findings.md

# 交付長時間任務並輪詢狀態
hermes peer run research-box
hermes peer status
```

與 A2A v1.0（[1.4.29](#1429-a2aagent-to-agent協定-v10v0200)）的差異：`hermes peer` 是 **Hermes 對 Hermes** 的第一方通道，對話持久落在各 Agent 的正規 Bot Chat 中可回溯稽核；A2A 則是**跨廠商**的標準化協定。選型對照見 [15.5 節](#155-五種多-agent-機制選型對照)。

#### 1.4.36 Cron 記憶化與 `continuity` 連續性（v0.21.0+）

過去排程任務是「無記憶的一次性執行」，v0.21.0 起排程任務與一般 Agent 對齊：

- **載入並更新持久記憶**：排程執行的所見所學會回寫記憶，不再每次從零開始
- **`continuity=true`**：將上一次執行的輸出帶入下一次執行，形成跨日的連續工作
- **per-job 持久 notepad**：每個排程任務擁有自己的耐久筆記本
- **monitor 模式雜湊抑制**：偵測到來源無變化時直接跳過 LLM 呼叫，**顯著降低長期監控類任務的 Token 成本**
- **失敗簽章確認（acked failure signatures）**：同一個失敗不會反覆告警轟炸

#### 1.4.37 Live Subagent Orchestration（v0.21.0+）

子代理從「送出後只能等」變成「可即時操控」：

- 列出目前執行中的所有子代理
- 對進行中的子代理**中途導引**修正方向
- **提前停止並保留部分結果**（而非整份丟棄）
- `delegate_task` 支援 **JSON Schema 結構化輸出驗證**，與**逐次委派的成本追蹤**
- ⚠️ **預設值提高**：迭代上限 250、並行子代理 10 個——效能提升的同時**成本上限也同步放大**，企業應主動設限（見 [11.1.15](#11115-v0210-升級特別注意事項目前最新-minor-版本)）

#### 1.4.38 MCP Command Center 與 `hermes://` Deep Link（v0.21.0+）

分散在多處的 MCP 伺服器與目錄整併為單一 Desktop 管理頁面：

- **拖放匯入**設定、**背景健康檢查**自動偵測失效伺服器
- **Fleet 成本／用量疊層**：跨所有 MCP 伺服器的用量與花費一覽
- **`hermes://` deep link**：從網頁或文件一鍵觸發明確的伺服器安裝流程（安裝仍需使用者確認）
- v0.20.6 另將遠端 MCP 目錄擴充至 **50+ 伺服器**

#### 1.4.39 Agent 驅動的應用內瀏覽器（v0.21.0+）

Desktop 內建瀏覽器不再只是檢視器，而是 Agent 可直接操作的工具面——Agent 自行導航、點擊、讀取頁面內容；使用者可將頁面彈出至系統瀏覽器，並具備完整的連結右鍵選單。與既有的 `browser` 工具集（Playwright／CDP，見 [3.5.1](#351-內建-toolsets)）互補：前者供人機共視的互動式操作，後者供無頭自動化。

#### 1.4.40 CLI Power Wave（v0.21.0+）

```bash
# Ctrl+P 開啟模糊命令面板（等同 /palette）
/palette

/model                # 互動式篩選模型選擇器
/status               # 推理模式、待審批項目、context 用量一覽
```

- **狀態列即時指標**：cache-hit %、延遲、tokens／sec，各欄位可獨立開關
- **全域緊急停止**：一鍵中止所有進行中的工作
- **`hermes approval-check`**：以 dry-run 方式測試審批規則會給出什麼判決，不必真的執行危險指令
- **Terminal Pets（Petdex）**：`/pet`／`/hatch` 陪伴型終端寵物（趣味功能，企業環境可停用）
- **Ctrl+C 中斷修正**：移除 Kitty keyboard protocol，修正部分終端機無法中斷的問題

#### 1.4.41 `model_overrides` — 免等改版的模型參數覆寫（v0.21.0+）

上游 Provider 調整了 context window 或定價，但 Hermes 尚未發版更新目錄時，不必再等待：

```yaml
# ~/.hermes/config.yaml
model_overrides:
  "openrouter/some-vendor/new-model":
    context_window: 400000
    input_price_per_1m: 1.25
    output_price_per_1m: 5.00
    supports_vision: true
```

同時 v0.21.0 起，**以 pip 安裝的第三方模型 Provider 可透過 Python entry points 被自動探索**，無須改動 Hermes 本體程式碼。

> ⚠️ **變更管控提醒**：`model_overrides` 直接影響成本估算與 context 管理決策，屬於「繞過官方目錄」的機制，企業應將其納入設定檔的版本控管與審核流程（見 [9.7.6](#976-企業導入前風險檢查清單)）。

---

## 第二章：整體系統架構

### 2.1 架構設計概述

Hermes Agent 採用分層架構設計，從前端展示層到底層資料層，每一層都具備可替換和可擴展的特性。以下是企業級部署時的完整架構設計。

### 2.2 分層架構圖

```mermaid
graph TB
    subgraph "Presentation Layer（展示層）"
        CLI[Terminal CLI<br/>TUI 界面（Ink 重寫）]
        DESK[Hermes Desktop App<br/>Electron 原生桌面]
        TG[Telegram Bot]
        DC[Discord Bot]
        SK[Slack Bot]
        WA[WhatsApp / WhatsApp Business Cloud API]
        SG[Signal]
        MX[Matrix]
        MT[Mattermost]
        FS_P[Feishu / DingTalk / WeCom]
        WX[WeChat]
        IM[iMessage via Photon Spectrum]
        QQ[QQBot]
        YB[Yuanbao]
        TM[Microsoft Teams]
        GC[Google Chat]
        LN[LINE]
        SX[SimpleX Chat]
        NT[ntfy]
        RF[Raft Agent Network]
        BZ[Buzz<br/>Nostr 協定]
        A2AP[A2A Connector<br/>Agent-to-Agent v1.0]
        EM[Email / SMS]
        HA[Home Assistant]
        WEB[Web API<br/>REST/SSE]
        DASH[Web Dashboard<br/>React SPA 全面管理面板]
    end

    subgraph "API Gateway Layer（閘道層）"
        GW[Hermes Gateway<br/>消息路由 / 認證 / 限流 / Scale-to-zero]
        ACP[ACP Adapter<br/>VS Code / JetBrains / Zed]
    end

    subgraph "Agent Layer（代理層）"
        CORE[Agent Core<br/>Planning / Execution / Loop]
        SUB[Subagent Pool<br/>平行委派 + 背景派工]
        SKILL[Skill Engine<br/>技能載入 / /learn 自動建立]
        MOA[MoA Router<br/>Mixture-of-Agents 聚合]
        PLUG[Plugin System<br/>Honcho / Hindsight / RetainDB / ByteRover 等]
    end

    subgraph "Memory Layer（記憶層）"
        STM[Short-term Memory<br/>Context Window]
        LTM[Long-term Memory<br/>MEMORY.md / USER.md]
        FTS[FTS5 Session Search<br/>跨對話搜尋 + Trigram CJK]
        VDB[(External Memory Providers<br/>9 種可插拔：mem0/Supermemory/<br/>Hindsight/OpenViking 等)]
        UDB[(User Model<br/>Honcho Dialectic)]
    end

    subgraph "Tool Layer（工具層）"
        TERM[Terminal Backends<br/>Local/Docker/SSH/Modal/Daytona/Singularity/Vercel]
        BROW[Browser Engine<br/>Playwright / Camofox]
        FILE[File Tools<br/>讀寫/搜尋/壓縮]
        WEB_TOOL[Web Tools<br/>搜尋/擷取/Vision]
        MCP_T[MCP Servers<br/>外部工具擴展]
        CRON[Cron Scheduler<br/>排程自動化 + Blueprints]
        HOOK[Outbound Webhooks<br/>HMAC 簽章事件推送]
    end

    subgraph "Data Layer（資料層）"
        SQLITE[(SQLite<br/>Sessions / Config)]
        KANBAN[(kanban.db<br/>多 Agent 看板)]
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
    TM --> GW
    GC --> GW
    LN --> GW
    SX --> GW
    NT --> GW
    RF --> GW
    BZ --> GW
    A2AP --> GW
    EM --> GW
    HA --> GW
    WEB --> GW
    DASH --> GW
    ACP --> CORE

    GW --> CORE
    CORE --> SUB
    CORE --> SKILL
    CORE --> MOA
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
    CORE --> HOOK

    STM --> SQLITE
    SUB --> KANBAN
    LTM --> FS_D
    SKILL --> FS_D
    CORE --> EXT
```

### 2.3 各層級說明

#### 2.3.1 Presentation Layer（展示層）

| 組件 | 說明 | 連線方式 |
| ------ | ------ | ---------- |
| Terminal CLI / TUI | 完整 TUI（v0.11.0 Ink 重寫），支援多行編輯、斜線指令自動完成、串流工具輸出、OSC-52 剪貼簿、**LaTeX 渲染**（v0.12.0）、冷啟動提升 57% | 本地 stdin/stdout |
| Web Dashboard | React SPA 本地管理介面，設定/Session/Skills/Gateway 管理、Plugin 擴展 Tab | HTTP（localhost） |
| Telegram Bot | 群組/私訊/Forum Topic、語音轉文字、Emoji 審批按鈕、Webhook Mode | Telegram Bot API |
| Discord Bot | 原生 Slash Commands、頻道控制、Interactive Model Picker、Voice Channel | Discord Gateway |
| Slack Bot | Thread 自動回覆、mrkdwn 格式、互動審批按鈕、Multi-Workspace OAuth | Slack Events API |
| WhatsApp | 透過 WhatsApp Business API 對接 | Webhook |
| Signal | 全 MEDIA 標籤交付（圖片/語音/影片） | signal-cli |
| Matrix | Tier 1 支援：Reactions、Read Receipts、E2EE、Room Management、CJK 輸入 | Matrix Client |
| Mattermost | 檔案附件交付、訊息串接 | Mattermost API |
| Feishu（飛書） | 互動卡片審批按鈕、ACL 控制、自動重連 | Feishu Open API |
| DingTalk（釘釘） | 企業機器人整合 | DingTalk API |
| WeCom（企業微信） | 企業應用整合、Callback Mode | WeCom API |
| WeChat（微信） | Native WeChat via iLink Bot API、Streaming Cursor、Media Upload | WeChat API |
| iMessage via Photon Spectrum | 無需 Mac relay，`hermes photon login` 裝置碼認證（v0.17.0 第 24 平台） | Photon Spectrum API |
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
| **Raft Agent Network** | 外部 agent network gateway channel bridge，隱私合約設計（v0.17.0 第 25 平台） | Raft Protocol |
| **WhatsApp Business Cloud API** | Meta 官方第一方 API，無需 bridge（v0.17.0），與既有 Baileys 橋接版本雙軌並存 | Meta Cloud API |
| **Buzz** | Block 旗下 Nostr 協定人機協作訊息平台，原生 WebSocket + NIP-42 認證（v0.20.0 新增） | Nostr Protocol |
| **A2A（Agent-to-Agent）** | 對外發布 Agent Card 供其他 A2A 相容 Agent 探索與呼叫，純外掛實作零核心異動（v0.20.0，見 1.4.29 節） | JSON-RPC 1.0 + SSE |
| **Hermes Relay**（實驗性） | 非獨立平台，而是前置 Discord/Telegram/Slack/WhatsApp 等多個外部連接器的能力協商框架 | 依連接器而定 |

> **平台總數說明**：官方文件現列出 **30+ 個訊息平台／連接器**（含 API Server 與 Webhook）；各平台支援的能力矩陣（工具／語音／圖片／檔案／討論串／已讀回條／串流）不盡相同，完整逐平台對照請見官方 `/docs/user-guide/messaging/` 各子頁面。

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
- **Scale-to-zero + Drain 協調**（v0.18.0）：代管 Gateway 閒置自動休眠，重啟／遷移前協調排空進行中對話
- **Profile-based 路由**（v0.19.0）：單一共用 Bot Token 依 Guild／頻道／討論串路由至不同 Profile
- **配送保證台帳**（v0.19.0）：回應產生與平台送達確認之間 Gateway 當機不再靜默遺失訊息，重啟後自動補送
- **智慧審批預設化**（v0.19.0）：獨立 LLM 審查者取代逐次詢問，成為危險指令的預設判斷機制

#### 2.3.3 Agent Layer（代理層）

| 組件 | 職責 |
| ------ | ------ |
| Agent Core | 核心循環：接收 → 規劃 → 工具呼叫 → 評估 → 回應 |
| Subagent Pool | 隔離子代理，支援平行工作流與背景派工（Live 逐字稿） |
| Skill Engine | 載入已有技能、複雜任務後自動建立新技能、`/learn` 手動萃取（v0.18.0） |
| MoA Router | Mixture-of-Agents 聚合：多參考模型併行推理 + 聚合器即時串流合成（v0.18.0，一級模型化） |
| Plugin System | 擴展記憶 / CLI / API Hook / Desktop SDK，如 Honcho、Hindsight、ByteRover、Kanban Desktop Plugin |

#### 2.3.4 Memory Layer（記憶層）

| 類型 | 實作 | 用途 |
| ------ | ------ | ------ |
| Short-term | Context Window（2,200 字元 MEMORY.md／1,375 字元 USER.md 上限） | 當次對話上下文管理，支援 `/compress` 壓縮；「凍結快照」模式：本次對話寫入，下次對話才生效 |
| Long-term（內建） | MEMORY.md / USER.md | 持久化知識、使用者偏好，免外部依賴 |
| Session Search | FTS5（免 LLM，~20ms） | 跨對話搜尋，v0.15.0 重建後較舊版快 4,500 倍 |
| 外部記憶 Provider（單選插件，9 種） | Honcho／Mem0／Supermemory／Hindsight／OpenViking／Holographic／RetainDB／ByteRover／Memori | 語義搜尋、知識圖譜、多容器記憶等進階場景，詳見 3.3 節 |
| User Model | Honcho Dialectic | 辯證式使用者理解與信任分數 |

#### 2.3.5 Tool Layer（工具層）

Hermes 內建 **70+ 工具，分屬約 28 個 Toolset**（v0.14.0 起 debloating 浪潮將部分重型後端改為 lazy install；工具依 `tools/registry.py` 自我註冊，涵蓋 Schema、分派、可用性與錯誤包裝），分為以下類別：

| 類別 | 工具 | 說明 |
| ------ | ------ | ------ |
| Terminal | execute_command, execute_code | 7 種後端：Local, Docker, SSH, Modal, Daytona, Singularity, Vercel Sandbox（v0.15.0 移除，v0.20.0 現代化重新引入） |
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
| A2A | a2a_discover, a2a_call, a2a_list, a2a_history, a2a_orchestrate | 呼叫外部 A2A 相容 Agent，預設關閉的獨立 Toolset（v0.20.0） |
| Webhook | 出站事件訂閱設定（非傳統 tool call） | HMAC 簽章、notify-only、不可回注上下文（v0.20.0） |

#### 2.3.6 Data Layer（資料層）

| 儲存 | 技術 | 存放內容 |
| ------ | ------ | ---------- |
| SQLite | 內建 | Session 歷史、設定、Cron 排程、配送保證台帳 |
| kanban.db | 獨立 SQLite（每看板一個） | Multi-agent Kanban 任務、Worker 心跳、稽核軌跡 |
| File System | `~/.hermes/` | Skills、Memories、SOUL.md、Logs |
| External APIs | HTTP/gRPC | LLM Provider（40+ 種，OpenAI / Anthropic / OpenRouter 等） |

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

> **注意事項**：Hermes Agent 已正式支援 Windows（v0.16.0+）。企業部署可使用 Desktop App / Linux VM / WSL2 / Docker 容器。

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
| ---------- | ------ |
| **Class-first Rubric** | 基於分類評分標準評估 Skill 品質，取代簡單的數值評分 |
| **Active-update Bias** | 偏好主動更新現有 Skill 而非建立新 Skill，減少重複 |
| **Fork Inheritance** | Fork 的 Skill 自動繼承父 Skill 的執行統計資料 |
| **Scoped Toolset** | 自我改進過程僅可存取 memory + skills 工具，不可執行系統指令 |
| **Autonomous Curator** | 配合 3.7 節 Curator 自動維護技能庫品質 |

**範例 — Skill 自動建立流程**：

```text
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

```text
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
| ------ | ------ |
| `/skills` | 列出所有可用技能 |
| `/<skill-name>` | 執行特定技能，支援堆疊（如 `/github-pr-workflow /test-driven-development`） |
| `/learn <對象>`（v0.18.0） | 將目錄／URL／剛示範的操作萃取為可重用 Skill，依 `CONTRIBUTING.md` 標準撰寫 |
| `hermes skills browse\|search\|install\|inspect\|list` | 瀏覽、搜尋、安裝、檢視、列出技能 |
| `hermes skills check\|update\|uninstall` | 檢查更新、更新、解除安裝 |
| `hermes skills opt-out\|opt-in` | 停用／啟用特定技能來源 |
| `hermes skills tap add owner/repo` | 新增自訂 GitHub Tap 作為技能來源 |
| `hermes bundles list\|show\|create\|delete` | 管理 Skill Bundle（一個 Slash Command 載入多個技能） |
| `hermes curator status\|run\|pause\|resume\|pin\|unpin` | 技能庫維護（見 3.7 節） |
| 自動建立 | Agent 複雜任務完成後自動封裝 |

技能採**漸進式揭露（Progressive Disclosure）**三層架構以節省 Token：Level 0 `skills_list()`（僅中繼資料，約 3k tokens）→ Level 1 `skill_view(name)`（完整內容）→ Level 2 `skill_view(name, path)`（特定參考檔案）。

#### 3.2.4 Skills Hub 生態系

Hermes 支援 [agentskills.io](https://agentskills.io/) 開放標準，技能可在社群間分享與下載，每個技能都有版本控制、使用統計和評分。技能發現來源已從單一 Hub 擴展為多來源生態系：

| 來源 | 說明 |
| ------ | ------ |
| 官方內建 | `official/security/1password` 等隨版本附帶的官方技能 |
| **skills.sh**（Vercel） | 公開技能目錄 |
| `/.well-known/skills/index.json` | 標準化端點，任何網域皆可託管自己的技能索引 |
| **ClawHub / LobeHub / browse.sh** | 社群技能託管平台 |
| 自訂 GitHub Tap | `hermes skills tap add owner/repo`，預設讀取 `skills/` 子目錄 |
| 直接 SKILL.md URL | 單一技能檔案直接安裝 |

**v0.17.0 Skills Hub Browser 重做**（v0.20.0 起支援 Connected Hubs 多來源並存）：
- **Connected Hubs**：可連接多個 Hub 來源（官方 + 企業內部 + 第三方）
- **Featured Section**：精選推薦技能展示區
- **安全掃描**：安裝前自動掃描技能是否含資料外洩／提示注入／破壞性操作模式（`--force` 可覆寫非危險性發現）
- **完整預覽**：安裝前可預覽技能完整內容（描述 / 程式碼 / 依賴 / 評分）

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

外部記憶為**單選式插件**（每個 Profile 僅能啟用一種），與內建 MEMORY.md／USER.md 並存互補。官方文件目前列出 **9 種**：

| Provider | 儲存位置 | 費用模式 | 特點 | 工具數 |
| ---------- | ------ | ------ | ------ | ------ |
| 內建 | 本地檔案 | 免費 | MEMORY.md + USER.md，零依賴，2,200／1,375 字元上限 | - |
| Honcho | 雲端或自架 | 自架免費／雲端付費 | 辯證式使用者建模、跨 Session Context 注入、信任分數 | 5 |
| Mem0 | 雲端／自架 Docker／內嵌 OSS | 自架免費、雲端付費 | 伺服器端 LLM 事實萃取、語義搜尋、去重 | 4 |
| Supermemory | 雲端或自架 | 自架免費、雲端付費 | 多容器隔離、`search_mode` 混合搜尋、Session 結束自動彙整 | 4 |
| Hindsight | 雲端或本地嵌入式 PostgreSQL | 本地免費、雲端付費 | 知識圖譜、實體解析、獨有 `hindsight_reflect` 跨記憶合成 | 3 |
| OpenViking | 自架（位元組跳動 Volcengine） | 免費（AGPL-3.0） | 檔案系統式階層結構、分層檢索、自動萃取 6 大類別 | 6 |
| Holographic | 本地 SQLite | 免費 | FTS5 全文檢索、信任評分、HRR 全像縮減表示組合式查詢 | fact_store（9 動作）+ feedback |
| RetainDB | 雲端 | **$20／月** | 混合搜尋（Vector + BM25 + 重排序）、7 種記憶類型、差量壓縮 | 10 |
| ByteRover | 本地預設／可選雲端同步 | 本地免費、雲端付費 | 階層知識樹、分層檢索、**SOC 2 Type II 認證** | 3 |
| Memori | Memori Cloud | 付費 | 結構化長期記憶、背景擷取已完成輪次、工具感知上下文 | 5 |

> **選型建議**：個人／小型團隊優先使用內建方案（零依賴、零成本）；需要跨 Session 使用者建模選 Honcho；企業多租戶場景優先 Supermemory 或 RetainDB；重視資料主權可完全自架的選 OpenViking（AGPL-3.0）或 Holographic（純本地 SQLite，無任何外部依賴）；已通過 SOC 2 稽核要求的環境可考慮 ByteRover。

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

#### 3.3.3 Memory Atomic Batch Operations（v0.17.0+）

v0.17.0 引入的 `memory` 工具原子批次操作，允許在單次 tool call 中完成多項記憶異動：

```python
# Agent 內部 tool call 格式
memory(operations=[
    {"action": "add", "key": "new_learning", "value": "React 19 uses compiler..."},
    {"action": "replace", "key": "project_phase", "value": "production"},
    {"action": "remove", "key": "outdated_note_xyz"}
])
```

**核心保證**：
- **原子性**：所有操作要麼全部成功，要麼全部回滾
- **Character Budget**：自動追蹤記憶總容量，接近上限時建議壓縮或移除
- **衝突解決**：同一 key 的多次操作按陣列順序執行

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
| --------- | --------- | ---------- |
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
| `image` | image_generate（含 v0.17.0 image-to-image editing mode） | 停用 |
| `automation` | blueprint_create, blueprint_list, blueprint_run（v0.17.0 Automation Blueprints） | v0.17.0 啟用 |

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
- **Sampling 支援**：MCP 伺服器可透過 `sampling/createMessage` 向 Hermes 請求 LLM 推論，並可依伺服器設定模型覆寫、Token 上限、速率限制與工具迴圈深度
- **HTTP Transport 免子行程**：除 stdio 本地子行程外，亦支援直連遠端 HTTP 端點的 MCP 伺服器，免本地啟動子行程

```yaml
# 兩種 MCP 連線方式並存範例
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
  linear:
    url: "https://mcp.linear.app/mcp"
    auth: oauth
```

#### 3.5.3 Terminal Backends

| 後端 | 連線方式 | 適用場景 | 危險指令審批 |
| ------ | ---------- | ---------- | ------ |
| Local | 本地 Shell | 開發環境 | 生效 |
| Docker | Docker API（硬化容器：capability 全數移除後選擇性復原、`no-new-privileges`、程序數上限 256） | 隔離執行 | 生效 |
| SSH | SSH 連線 | 遠端伺服器 | 生效 |
| Daytona | Daytona API | Serverless（閒置休眠） | **不生效**（沙箱本身即為安全邊界） |
| Modal | Modal API | GPU 計算 / Serverless | **不生效** |
| Singularity | Container | HPC 環境 | **不生效** |
| Vercel Sandbox | Vercel API | Serverless | **不生效** |

> **版本沿革**：v0.15.0 曾移除 Vercel Sandbox 後端（與 Vercel AI Gateway 一併下架），**v0.20.0 現代化重寫後重新引入**。企業若在 v0.15.0～v0.19.x 期間已遷移至 Docker／Daytona／Modal，可自行評估是否切回，非必要變更。
>
> ⚠️ **安全提醒**：雲端後端（Daytona／Modal／Vercel Sandbox／Singularity）**略過危險指令審批檢查**，官方文件明確說明其安全模型改為「沙箱本身即邊界」——選用這些後端前，務必確認沙箱之網路存取、憑證掛載範圍已依 9.1 節原則收斂。

**瀏覽器後端**（v0.8.0 更新）：

| 後端 | 說明 | 適用場景 |
| ------ | ------ | ---------- |
| Playwright | 本地 Chromium 瀏覽器 | 一般網頁操作 |
| Camofox | 反偵測 Firefox 瀏覽器 | 需要反偵測的場景 |
| Browser Use | 託管瀏覽器服務（取代 Browserbase） | 雲端瀏覽、免本地安裝 |
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

#### 3.5.4 Tool Search（延遲式工具 Schema 載入）

**解決什麼問題**：當一個 Session 掛載了大量 MCP 伺服器與 Plugin 工具時，光是這些工具的 JSON Schema 就可能吃掉可觀比例的 context window——而且是**每一輪都要重新付費**。Tool Search 讓這些 Schema 改為「用到才載入」。

**運作方式**：模型平常只看到三個橋接工具，而非全部工具的完整定義。

| 橋接工具 | 作用 |
| ---------- | ------ |
| `tool_search(query)` | 以自然語言查詢找出相關工具 |
| `tool_describe(name)` | 載入指定工具的完整 Schema |
| `tool_call(name, args)` | 實際呼叫該工具 |

為維持可發現性，Hermes 仍會嵌入一份「技能風格」的精簡清單（僅工具名稱與一行描述），讓模型知道有哪些能力存在。

```yaml
# ~/.hermes/config.yaml
tool_search:
  enabled: auto            # auto = 偵測到有可延遲載入的工具時自動啟用
  threshold_pct: 5         # 清單預算佔 context 的百分比上限
  search_default_limit: 5  # 每次查詢預設回傳結果數
  max_search_limit: 25     # 每次查詢的硬上限
  listing: auto            # 空間足夠時嵌入工具清單
  listing_max_tokens: 4000 # 嵌入清單的 Token 上限
```

**企業考量與取捨**：

- ✅ 掛載 10 個以上 MCP 伺服器時，context 節省效果顯著
- ⚠️ 首次存取某工具需**多一次 round trip**（先 search／describe 再 call），互動延遲略增
- ⚠️ 延遲載入的 Schema **無法受益於 System Prompt 快取**，若某幾個工具其實每輪都會用到，反而可能更貴
- ⚠️ 效果取決於模型組織查詢字串的能力，較小的模型可能找不到正確工具
- **建議**：工具數量少（< 10）或工具使用高度集中時維持關閉；工具生態龐大且使用分散時再開啟

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
/model xai:grok-composer-2.5-fast   # v0.17.0: Cursor Composer 模型, 200k context
/model vertex:gemini-2.5-pro        # v0.18.0: Google Vertex AI，Service Account／ADC 自動換發 Token
/model fireworks:llama-4-maverick   # v0.19.0: Fireworks AI，Provider 選擇器第二順位

# 查看當前模型
/model

# 切換 Provider（v0.16.0+ Fuzzy Model Picker：所有介面統一模糊搜尋）
hermes model   # 互動式選擇

# Mixture-of-Agents（v0.18.0 起與一般模型並列於選擇器）
hermes moa list          # 列出可用的 MoA 預設組合
hermes moa configure      # 設定參考模型 + 聚合器
/moa                      # 一次性套用預設 MoA 組合執行單一提示
```

> **推理強度分級**（v0.19.0 新增 `max`／`ultra`）：`/model --effort low|medium|high|max|ultra` 可依任務複雜度調整推理深度，`max`／`ultra` 主要對應 GPT-5.6／Codex 頂層模型；MoA 亦支援每個參考模型槽位各自設定不同推理強度（例如顧問模型深度思考、聚合器保持快速）。

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
| ------ | ------ |
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
    consolidate: false      # v0.17.0: LLM consolidation 改為 opt-in（預設 deterministic sweep 免費）
```

#### 3.7.5 v0.17.0 成本優化（Curator Cost Optimization）

v0.17.0 大幅降低 Curator 運行成本：
- **預設 Deterministic Sweep 免費**：不活躍技能的判定改為純演算法（基於使用頻率 + 最後呼叫時間），無需 LLM 呼叫
- **LLM Consolidation 改為 Opt-in**：需要 AI 判斷的合併/精煉操作改為 `curator.consolidate: true` 才啟用
- **影響**：絕大多數用戶的 Curator 運行零 Token 成本

> **企業建議**：大型團隊建議將 Curator 間隔設為 3-5 天，並監控 `REPORT.md` 確保重要技能不被意外修剪。可透過 `pinned` 標記保護關鍵技能。對於需要智慧合併的場景，設定 `consolidate: true` 並指定低成本模型。

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
| ------ | ------ |
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
| ------ | ---------- | ------ |
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
| ---------- | ------------ |
| 孤立 Shadow Repos 無法清理 | 單一儲存（Single-store）架構 |
| 磁碟空間無限膨脹 | 真正的修剪（Real pruning）+ 磁碟護欄（Disk guardrails） |
| 跨 Session 狀態遺失 | 完整的 Session 恢復機制 |

**企業建議**：升級到 v0.13.0 後，建議執行一次完整的 Checkpoint 清理以釋放舊版孤立資源。

### 3.11 Recurring Loops（`/loop`）與 Session Heartbeats

Hermes 提供三種「讓 Agent 持續工作」的機制，三者**觸發來源與作用範圍完全不同**，是實務上最常混淆的一組概念。

#### 3.11.1 三者選型對照

| 面向 | `/loop`（Recurring Loops） | `/goal`（Persistent Goals） | Cron（排程任務） |
| ------ | ------ | ------ | ------ |
| 觸發來源 | **計時器**（固定或自我調速） | **判定器**（依完成契約實證判定） | **外部排程**（cron 運算式／Blueprint） |
| 作用範圍 | 當前 Session 內 | 當前 Session 內 | **獨立於任何 Session**，無人值守 |
| 終止條件 | 次數用盡／`--until` 條件成立／手動停止 | 完成契約被判定達成 | 排程被刪除或停用 |
| 典型場景 | 輪詢 CI／部署狀態、反覆跑測試直到通過 | 單一有明確驗收標準的目標 | 每日簡報、長期監控、定期維運 |
| 相關章節 | 本節 | [3.8](#38-persistent-goals-與-ralph-loop)、[1.4.26](#1426-goal-完成契約completion-contractsv0180) | [6.6](#66-workflow-orchestration)、[6.6.5](#665-cron-記憶化與連續性v0210) |

一句話區分：**`/loop` 是時間驅動、`/goal` 是判定驅動、Cron 是排程驅動且脫離 Session**。

#### 3.11.2 `/loop` 語法與設定

```text
/loop [interval] <prompt> [--times N] [--until <condition>]
```

每一次觸發都是一次**完整的 Agent 輪次**——會重新讀取當前狀態後回報，而非重播舊結果。省略 `interval` 時 Agent 自行決定節奏（self-paced）。另有狀態查詢、暫停、恢復、停止等子操作。

```yaml
# ~/.hermes/config.yaml
loops:
  min_interval_seconds: 30      # 固定間隔的下限，避免過於頻繁
  self_paced_floor_seconds: 60  # 自我調速模式的起始節奏
  max_ticks: 100                # 總次數上限，防止無限消耗 Token
```

> ⚠️ **成本護欄**：`max_ticks` 是防止失控的最後一道防線，企業環境**不建議調高**。輪詢外部狀態時，間隔應貼合該狀態實際的變化速度——監控一個需時 8 分鐘的 CI 流程，一次 480 秒的檢查遠優於八次 60 秒的檢查。

#### 3.11.3 Session Heartbeats

`/heartbeat every <interval> <prompt>`（簡寫 `/hb`）為**閒置時的週期性提示**：與 `/loop` 不同，它只在 Session 處於閒置狀態時觸發，適合「有空就順手檢查一下」類型的背景關注，而不會與使用者正在進行的工作競爭。

---

## 第四章：安裝與環境建置

### 4.1 系統需求

| 需求項目 | 最低要求 | 建議配置 |
| ---------- | ---------- | ---------- |
| 作業系統 | Linux / macOS（Apple Silicon）/ WSL2 / Windows 10-11 / Android (Termux) | Ubuntu 22.04+ LTS / macOS 14+（Apple Silicon）/ Windows 11 |
| Python | 3.11+（安裝程式透過 `uv` 自動處理，免手動安裝） | 3.11 |
| Node.js | **26+（v0.20.0 起為硬性必要條件）** | 26 LTS |
| 記憶體 | 2 GB | 4 GB+ |
| 磁碟空間 | 500 MB | 2 GB+（含依賴與快取） |
| 網路 | 可連接 LLM API | 穩定連線 |
| Git | 2.30+（必要，安裝程式不會自動安裝） | 最新版 |
| LLM Context Window | **最低 64,000 tokens**（低於此門檻的模型會在啟動時被拒絕） | 128K+ |

> ⚠️ **macOS 僅支援 Apple Silicon**：官方文件明確將 **macOS Intel/x86** 列為「不支援、且拒絕相關 PR」的組合，企業若仍有 Intel Mac 機隊，需改用 Docker 或雲端/Linux VM 部署。
>
> 🪟 **Windows 支援**（v0.16.0+ 正式支援）：Hermes Agent 已完整支援 **Native Windows**（x86_64／aarch64），可透過 Desktop App（NSIS installer）或 PowerShell 安裝腳本直接安裝。少數功能在 Windows 上仍不可用，生產環境仍可選擇 [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) 以獲得最佳相容性。
>
> 📱 **Android 支援**（v0.12.0+，Tier 2 盡力支援）：Hermes 可在 Android 的 [Termux](https://termux.dev/) 環境中運行，安裝方式與 Linux 相同，手機端有部分功能不可用。

#### 4.1.1 平台支援層級（Platform Support Tiers）

官方文件明確將支援平台分為三個層級，企業選型前應對照確認。**層級同時決定了官方認可的安裝管道**——不在對應管道之列者，即使技術上可行也不受支援：

| 層級 | 平台（OS／架構） | 官方安裝管道 | 說明 |
| ------ | ------ | ------ | ------ |
| **Tier 1（完整支援）**<br>官方承諾「絕不破壞安裝與更新」 | macOS（僅 Apple Silicon） | Hermes Desktop、`install.sh` | — |
| | Windows 10／11（x86_64、aarch64） | Hermes Desktop、`install.ps1` | 見 4.3 節注意事項 |
| | Linux／WSL2（x86_64、aarch64） | `install.sh` | 以 Ubuntu + WSL2 為測試基準 |
| | Docker 容器（x86_64、aarch64） | `docker pull` | 容器**不支援 `hermes update`**，升級須重新拉取映像 |
| **Tier 2（盡力支援）**<br>官方明示可能於改版時中斷 | Android／Termux（aarch64） | `install.sh` | 手機端部分功能不可用 |
| | Nix（macOS／Linux／NixOS） | `install.sh` | 官方坦承因 Node.js 套件生態問題「時常故障（breaks often）」 |
| **明確不支援**<br>相關 PR 將被拒絕 | AUR、**macOS Intel（x86）**、PyPI（`pip install`／`uv tool install`）、Homebrew | — | PyPI 與 Homebrew 已於 v0.20.0 正式終止，見 4.2.3 節 |

#### 4.1.2 安裝目錄結構

| 安裝方式 | 程式碼路徑 | 執行檔路徑 | 資料路徑（`$HERMES_HOME`） |
| ------ | ------ | ------ | ------ |
| 一般使用者（免 sudo） | `~/.hermes/hermes-agent/` | `~/.local/bin/hermes` | `~/.hermes/` |
| Root／sudo 安裝 | `/usr/local/lib/hermes-agent/` | `/usr/local/bin/hermes` | `/root/.hermes/` |

> 安裝程式會自動處理 Python 3.11（透過 `uv`）、Node.js 26、`ripgrep`、`ffmpeg` 等依賴；Git 需自行預先安裝。非互動式／服務帳號環境下瀏覽器依賴需另行執行 `sudo npx playwright install-deps chromium`，或於安裝時加上 `--skip-browser` 略過。

### 4.2 快速安裝（Linux / macOS / WSL2）

#### 4.2.1 一鍵安裝

```bash
# 一鍵安裝（處理所有依賴：Python、Node.js、套件、hermes 指令）
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

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

#### 4.2.3 已停用安裝管道（Homebrew／PyPI／pip）

> ⚠️ **v0.20.0 起正式停用**：Homebrew（`brew install hermes-agent`）與 PyPI／pip wheel（`pip install hermes-agent`，原為 v0.14.0 新增）兩種安裝管道已於官方文件明確列為「**不支援，相關 PR 將被拒絕**」。企業若仍在維護內部套件庫參照舊安裝方式，須改用官方目前唯三支援的管道：
>
> 1. **Shell Installer**（`curl ... | bash` / `irm ... | iex`，見 4.2.1／4.3.2）
> 2. **Docker**（見 4.4 節，注意 Docker 容器**不支援 `hermes update`**，須改為重新拉取映像）
> 3. **Nix Flake**（見 4.5 節，官方標示為 Tier 2「盡力支援」，非 NixOS 環境常見套件相容性問題）
>
> 既有透過 Homebrew／pip 安裝的環境不會自動遷移，建議規劃一次性改用上述三種管道之一重新安裝。

### 4.3 Native Windows 安裝

v0.16.0 起 Windows 已為正式支援平台，提供兩種安裝方式：Desktop App 與 PowerShell CLI。

#### 4.3.1 Desktop App 安裝（推薦）

1. 前往 [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/) 下載 Windows 安裝程式（NSIS installer）
2. 執行安裝程式，依指引完成安裝
3. 應用內自動更新，無需手動升級

#### 4.3.2 PowerShell CLI 安裝

```powershell
# 以系統管理員身份開啟 PowerShell
# 一鍵安裝（處理所有依賴）
irm https://hermes-agent.nousresearch.com/install.ps1 | iex

# 驗證安裝
hermes --version
```

#### 4.3.3 注意事項

| 項目 | 說明 |
| ------ | ------ |
| **狀態** | 正式支援（v0.16.0+ GA） |
| **Desktop App** | Electron 原生應用，內建自動更新 |
| **CLI** | 完整 CLI/TUI 功能，包含 MinGit |
| **路徑轉換** | ACP Adapter 已支援 Windows cwd → WSL 路徑自動轉換 |
| **WSL 互通** | 可保留 WSL interop PATH 在 systemd units 中 |

> **企業建議**：Windows 開發者可直接使用 Desktop App 獲得最佳體驗。對於需要完整 Linux 工具鏈的 CI/CD 環境，仍建議採用 WSL2。

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
>
> 💡 **Dashboard in Docker**（v0.13.0）：在 Docker 中啟動 Dashboard，只需加入 `-e HERMES_DASHBOARD=1` 環境變數，Dashboard 會以 Side-process 方式啟動。

#### 4.4.2 自建 Docker Image

```dockerfile
# Dockerfile（專案根目錄已提供；自 v0.20.0 起 Node.js 26 為硬性必要條件）
FROM python:3.11-slim

WORKDIR /app

# 安裝系統依賴（Debian/Ubuntu 預設 apt 套件庫的 nodejs 版本通常過舊，
# 需改用 NodeSource 官方腳本安裝 Node.js 26，否則 hermes 將無法啟動）
RUN apt-get update && apt-get install -y curl git gnupg ripgrep ffmpeg \
    && curl -fsSL https://deb.nodesource.com/setup_26.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# 複製應用程式
COPY . .

# 安裝 Python 依賴（此處為原始碼可編輯安裝，非透過已停用的 PyPI 發行版安裝）
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

#### 4.6.1 初始設定精靈

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

#### 4.6.2 環境變數設定

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

#### 4.6.3 Nous Portal 登入（免費模型）

```bash
# OAuth 登入（瀏覽器會自動開啟）
hermes auth login nous

# 登入後可使用免費模型（如 MiMo v2 Pro）
# 無需 API Key，適合預算有限的團隊
```

### 4.7 設定檔說明

#### 4.7.1 主設定檔

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

#### 4.7.2 設定檔驗證

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

### 4.8 Managed Scope（組織層級設定釘選）

**解決什麼問題**：在多人共用的機器或整批部署的機隊上，IT 管理者需要「釘住」某些基準設定，讓一般使用者無法覆寫——例如強制走內部 Provider、強制開啟秘密遮蔽。Managed Scope 就是官方對此需求的機制。

#### 4.8.1 檔案位置與權限模型

設定放在系統層級目錄（可用環境變數 `HERMES_MANAGED_DIR` 改指他處）：

| 檔案 | 用途 | 建議權限 |
| ------ | ------ | ------ |
| `/etc/hermes/config.yaml` | 釘選設定值 | root 擁有，`0644` |
| `/etc/hermes/.env` | 釘選環境變數 | root 擁有，`0644` |
| `/etc/hermes/`（目錄） | — | root 擁有，`0755` |

**執行機制就是檔案系統權限本身**：檔案所有人為 root、全員可讀但僅管理者可寫。Hermes 沒有另外實作一套權限引擎。

```yaml
# /etc/hermes/config.yaml — 只釘住需要強制的鍵
model:
  provider: nous
security:
  redact_secrets: true
```

#### 4.8.2 優先序（逐鍵覆寫，非整段覆寫）

```text
/etc/hermes/（Managed）  >  ~/.hermes/（使用者）  >  使用者 .env  >  Shell 環境變數
```

關鍵在於**優先序僅套用於被明確釘選的那些鍵**，其餘設定完全由使用者掌控。官方原文的例子最清楚：釘住 `model.default` **並不會**凍結其餘的 `model.*` 設定。

#### 4.8.3 v1 版本的限制：不可作為權限控管邊界

這是本節企業導入時**最重要的一段**，官方文件亦誠實揭露：

| 限制 | 意涵 |
| ------ | ------ |
| 僅依賴檔案系統權限 | 沒有加密簽章、沒有完整性驗證；具備 root 或該檔寫入權者即可繞過 |
| Managed `.env` 為**全域可讀**（`0644`） | **絕對不可放置敏感 Secret**——同機器上任何使用者都讀得到。敏感憑證請改用 Bitwarden Secrets Manager 或 1Password（見 [1.4.17](#1417-bitwarden-secrets-managerv0150)、[1.4.27](#1427-訂閱管理與密碼管理器整合v0190)） |
| Agent 可在自身子行程覆寫被釘選的環境變數 | 被釘選的值**擋得住設定檔層級的變更，擋不住執行期的子行程環境** |

> ⚠️ **結論**：Managed Scope 應定位為「**組織預設值的散佈機制**」（讓新機器開箱即有正確基準設定），**而非資安控管邊界**。若合規要求真正的強制不可繞過，需搭配 OS 層級的 MDM／端點管控、以及 [9.8 節](#98-egress-憑證注入代理iron-proxy-沙箱零信任外連) 的 egress 代理等外部機制共同構成。

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
| ------ | ------ |
| `/new` 或 `/reset` | 開啟新對話（保留記憶）；v0.13.0 支援 `/new [session-name]` 指定名稱 |
| `/model [provider:model]` | 切換模型（v0.13.0 TUI 與 `hermes model` 一致化 + 內建認證） |
| `/compress` | 壓縮當前上下文（v0.13.0 狀態列顯示壓縮次數） |
| `/usage` | 查看 Token 使用量 |
| `/insights [--days N]` | 查看使用洞察 |
| `/skills` | 列出可用技能 |
| `/personality [name]` | 設定人格 |
| `/retry` | 重試上一輪 |
| `/undo` | 撤銷上一輪 |
| `/busy [steer\|queue\|interrupt]` | 設定忙碗模式（v0.12.0） |
| `/btw` | 導引中插任務（v0.12.0） |
| `/reload-skills` | 重新載入技能庫（v0.12.0） |
| `/reload` | 熱重載 `.env` 設定（v0.12.0） |
| `/reload-mcp` | 重建 MCP cached agents（v0.12.0） |
| `/background` | 將任務移至背景執行（v0.12.0） |
| `/mouse` | 互動式滑鼠操作（v0.12.0） |
| `/fast` | 切換 Fast Mode（Priority Processing） |
| `/steer` | 中途導引 Agent 行為（v0.11.0） |
| **`/goal`** | **設定跨回合持久目標（Ralph Loop）（v0.13.0）** |
| **`/kanban`** | **管理 Multi-agent Kanban 看板（v0.13.0）** |
| **`/queue`** | **ACP：對進行中的 Agent 排隊後續指令（v0.13.0）** |
| **`/learn <對象>`** | **將目錄／URL／剛示範的操作萃取為可重用 Skill（v0.18.0）** |
| **`/journey`** | **檢視記憶與技能學習時間軸（v0.18.0）** |
| **`/subscription` / `/topup`** | **查看 Nous Portal 訂閱方案、剩餘額度、升降級（v0.19.0）** |
| **`/deny <原因>`** | **拒絕待審指令並告知理由，讓 Agent 自我修正（v0.19.0）** |
| **`!<shell 指令>`** | **免佔用模型輪次，直接執行 Shell 指令（v0.20.0）** |
| **`/init`** | **掃描專案，自動產生／更新 AGENTS.md（v0.20.0）** |
| **`/diff`** | **顯示 staged／all／session 變更（v0.20.0）** |
| **`/context`** | **檢視目前上下文視窗的組成明細（v0.20.0）** |
| **`/focus`** | **精簡輸出檢視，隱藏內容可復原（v0.20.0）** |

> **中途導引（Mid-turn Redirect，v0.20.0）**：Agent 執行中若發現方向偏離，可直接在 TUI 中輸入修正內容，無需等待當前輪次結束——進行中的工作會被保留，原始提示不遺失，Agent 據此修正方向，是 v0.11.0 `/steer` 的自然延伸（差異在於 `/steer` 需明確指令觸發，Mid-turn Redirect 可直接以自然語言插話）。

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

```text
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

#### 6.2.1b Background Subagents（v0.17.0+）

v0.17.0 新增背景子代理模式，允許非阻塞委派：

```python
# 同步委派（既有行為，等待完成）
delegate_task(task="分析 API 安全性")

# 背景委派（v0.17.0 新增，不阻塞主對話）
delegate_task(
    task="掃描所有 1,200 個 REST endpoint 的安全合規性",
    background=True
)
# 主 Agent 可繼續回應使用者
# 背景子代理完成後，結果自動注入對話上下文
```

**適用場景**：
- 耗時任務（大規模程式碼掃描、全倉庫搜尋）
- 平行探索（同時研究多個技術方案）
- Kanban Worker 角色（背景處理佇列任務）

**Desktop App 整合**：背景子代理在 Desktop App 中顯示為 Subagent Watch-windows，可即時觀察進度。

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

#### 6.2.1c Live Subagent Orchestration（v0.21.0+）

v0.17.0 讓子代理可以「非同步跑」，v0.19.0 讓它「可以看」（即時逐字稿），v0.21.0 則讓它**「可以改」**——委派不再是送出後只能等待的黑箱。

**四項新增能力**：

| 能力 | 說明 |
| ------ | ------ |
| 列出執行中子代理 | 隨時查詢目前有哪些 child 在跑、各自進度為何 |
| **中途導引（course-correct）** | 對進行中的子代理注入修正指示，不必砍掉重練 |
| **提前停止並保留部分結果** | 判斷方向已足夠或已偏離時中止，**已完成的部分成果仍會回收**而非整份丟棄 |
| 逐次委派成本追蹤 | 每一次 `delegate_task` 的 Token 與費用獨立記帳，可歸因到具體子任務 |

**結構化輸出與品質閘門**：

```python
# v0.21.0：委派時直接指定 JSON Schema，回傳值不符即判定失敗
delegate_task(
    task="盤點所有對外 REST endpoint 的認證方式",
    schema={
        "type": "object",
        "properties": {
            "endpoints": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "path":   {"type": "string"},
                        "method": {"type": "string"},
                        "auth":   {"type": "string", "enum": ["jwt", "apikey", "none"]}
                    },
                    "required": ["path", "method", "auth"]
                }
            }
        },
        "required": ["endpoints"]
    }
)
```

其餘配套：**批次品質預檢**（spawn 之前先驗證批次任務的合理性，避免一次噴出一堆廢工）、**截斷標記**（被上限截斷的 child 會明確標示，不會讓不完整結果被誤當作完整結果）。

> ⚠️ **成本警告 — v0.21.0 提高了預設值**：迭代上限由既有值提升至 **250**，並行子代理數提升至 **10**。這使長時間自主任務更容易一次跑完，但**成本上限也同步放大一個量級**。企業環境務必在 `config.yaml` 中依實際預算調降，或搭配 9.2 節的成本控制設定與 `/usage`／`hermes insights` 監控。

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
# Kanban CLI 指令（每個看板為獨立 SQLite：~/.hermes/kanban/boards/<slug>/kanban.db）
hermes kanban init                    # 初始化預設看板
hermes kanban boards create <slug>    # 建立多專案看板（各自獨立資料庫，不可跨看板連結）
hermes kanban list                    # 列出所有任務
hermes kanban create "重構 API"        # 建立新任務
hermes kanban assign task-1 backend   # 指派任務到 Profile
hermes kanban show task-1             # 查看任務詳情
hermes kanban link task-1 task-2      # 建立任務相依關係
hermes kanban complete task-1         # 標記任務完成
hermes kanban dispatch                # 手動觸發一次派工迴圈

# 對話中斜線指令（與 CLI 對應同一份資料）
/kanban                        # 查看當前看板狀態

# Agent 內部工具（kanban_* toolset，供 Worker 自身呼叫）
# kanban_show / kanban_complete / kanban_block / kanban_heartbeat /
# kanban_comment / kanban_create / kanban_link / kanban_request_review
# Orchestrator 專用：kanban_list / kanban_unblock
```

**任務生命週期**：`triage → todo → ready → running → review｜blocked → done → archived`。**Dispatcher** 為長駐迴圈（預設 60 秒輪詢一次，`kanban.dispatch_in_gateway: true` 時內建於 Gateway 執行），負責回收逾時／當機的認領、於父任務完成後自動將子任務由 `todo` 推進至 `ready`、原子性認領 `ready` 任務並以獨立 OS 行程派生對應 Profile 的 Worker，連續失敗達 `max_retries` 後自動標記阻擋。

**工作區類型**（`workspace` 欄位）：`scratch`（暫存，預設，任務結束即清除）、`worktree`（獨立 Git worktree，保留）、`dir:<絕對路徑>`（共用目錄，保留）。

**多租戶支援**：`hermes kanban dispatch --tenant business-a --workspace dir:~/tenants/business-a/`，Worker 取得 `$HERMES_TENANT` 環境變數，記憶寫入自動依租戶命名空間隔離。

**與 `delegate_task` 的定位差異**：`delegate_task` 為阻塞式 RPC、匿名子代理、不可恢復、壓縮後稽核紀錄即遺失，僅支援階層式委派；Kanban 則是持久化佇列、具名且持久記憶的 Profile、可恢復（阻擋→解除阻擋、當機自動回收）、完整 SQLite 稽核軌跡，支援對等（Peer）協作而非僅階層委派。企業選型時應依「一次性平行子任務」選 `delegate_task`（見 6.2 節），「跨會話、需人工可視、需審計軌跡」的協作場景選 Kanban。

#### 6.3.3 可靠性保障機制

| 機制 | 說明 |
| ------ | ------ |
| **心跳監測** | Worker 定期發送心跳，超時則標記為失聯 |
| **殭屍偵測** | 自動偵測 Darwin 和 Linux 環境中的殭屍 Worker |
| **工作回收** | 失聯 Worker 的任務自動回收並重新指派 |
| **幻覺閘門** | 防止 Worker 聲稱完成了未建立的任務卡 |
| **重試預算** | 每任務可設定 `max_retries`，超過則標記失敗 |
| **統一失敗計數器** | 跨 spawn / timeout / crash 統一計算失敗次數 |
| **任務所有權驗證** | 對破壞性工具呼叫強制驗證 Worker 任務所有權 |
| **Auto-block** | 未完成退出的 Worker 自動被阻擋 |

> **企業建議**：Multi-agent Kanban 特別適合大型跨團隊專案，建議搭配 Profile 機制為不同角色（前端/後端/QA/DevOps）配置專屬的 SOUL.md 和技能集。

#### 6.3.4 Worker Lanes 與 v0.21.0 強化

**Worker Lanes（工作通道）** 讓同一個看板上的 Worker 依「通道」分流——例如將 `backend`、`frontend`、`qa` 各自視為獨立的處理通道，任務卡依標籤進入對應通道，避免所有 Worker 競爭同一個佇列而互相踩線。官方另有專頁說明（`/docs/user-guide/features/kanban-worker-lanes`）與逐步教學（`/docs/user-guide/features/kanban-tutorial`）。

v0.21.0 針對長時間多 Agent 運行的實際故障模式，補上四項強化：

| 強化項 | 解決的實際問題 |
| ------ | ------ |
| **碰撞熱點標記（collision-hotspot flagging）** | 標示出反覆被多個 Worker 同時搶改的檔案／任務，讓人類可及早介入重新切分工作 |
| **腦裂決策歸屬契約（split-brain decision-ownership contract）** | 當兩個 Worker 對同一件事做出矛盾判斷時，明確定義由誰的決策為準，不再靜默地互相覆寫 |
| **記憶感知派工閘門（memory-aware dispatch guard）** | 派工前檢查 Worker 的記憶狀態，避免將任務丟給記憶尚未就緒的 Worker |
| **notify／wake 投遞模式** | 區分「僅通知」與「喚醒處理」兩種投遞語意，Worker 不會被每一則通知都喚醒 |

另外 v0.20.4 起，Kanban 事件可直接觸發 **Desktop 原生系統通知**；v0.21.0 修正了「Cron 任務會誤繼承 Kanban Worker 的派工者身分」以及「快取的 DB 路徑遺失 schema 時 Kanban 不會重建」兩個資料層問題——長期運行的看板建議升級。

### 6.4 長期記憶設計（Vector DB）

#### 6.4.1 使用 Supermemory（推薦企業使用）

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

#### 6.4.2 使用 mem0

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

#### 6.4.3 記憶架構設計（企業級）

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

#### 6.6.1 使用 Cron 建立自動化流程

```bash
> 建立以下自動化流程：
>
> 1. 每天 08:00 - 檢查 GitHub 上的新 Issue，摘要傳到 Slack
> 2. 每天 18:00 - 執行程式碼品質掃描，結果傳到 Telegram
> 3. 每週一 09:00 - 生成週報（本週 commits / issues / PRs 摘要）
```

#### 6.6.2 Automation Blueprints（v0.17.0+）

v0.17.0 新增自然語言排程模板，取代傳統 cron 語法。Blueprints 可透過四種入口管理：

| 入口 | 說明 |
| ------ | ------ |
| Dashboard 表單 | 視覺化建立與管理 Blueprint |
| CLI slash command | `/blueprint create "每天早上 9 點掃描漏洞"` |
| Messenger 對話 | 直接在聊天中說「幫我每週一產生週報」 |
| Docs 目錄 | `~/.hermes/blueprints/*.yaml` 檔案化管理 |

```yaml
# ~/.hermes/blueprints/weekly-report.yaml
name: weekly-report
schedule: "每週一早上 9 點"
task: |
  彙整本週的 Git commits、PR 合併數、Issue 解決數，
  生成 Markdown 週報傳送到 Slack #engineering 頻道
profile: devops
channel: slack
conditions:
  - type: day_of_week
    value: monday
```

> **與 Cron 的關係**：Automation Blueprints 底層仍使用 Cron 引擎，但提供自然語言介面。既有 `cron_add` 指令完全相容，Blueprints 為更高層的抽象。

#### 6.6.3 使用 Context Files 定義工作流

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

#### 6.6.4 Profile-based 多團隊工作流

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

#### 6.6.5 Cron 記憶化與連續性（v0.21.0+）

在 v0.21.0 之前，排程任務是**無記憶的一次性執行**：每次醒來都像第一次上工，既無法累積上下文，也無法把上一輪的結論帶到下一輪。v0.21.0（部分能力於 v0.20.5 先行導入）讓 Cron 與一般 Agent 的能力對齊。

| 新能力 | 說明 | 企業價值 |
| ------ | ------ | ------ |
| **持久記憶載入／更新** | 排程任務如同一般 Agent 讀取並回寫持久記憶 | 監控類任務能記住「上次已經回報過什麼」 |
| **`continuity=true`** | 將上一次執行的輸出帶入下一次執行 | 形成跨日的連續工作，如逐日推進的重構專案 |
| **per-job 持久 notepad** | 每個排程任務擁有自己的耐久筆記本 | 與全域記憶隔離，避免排程雜訊污染主記憶 |
| **Monitor 模式雜湊抑制** | 偵測來源無變化時**直接跳過 LLM 呼叫** | **成本大幅下降**——長期監控多半是「沒事發生」 |
| **失敗簽章確認** | 同一個失敗簽章不會反覆推播告警 | 避免告警疲勞 |
| **派工前設定驗證** | 排程觸發前先驗證設定合法性 | 設定錯誤不會等到半夜才炸 |
| **per-job 推理強度釘選** | 每個任務各自指定 reasoning effort | 簡單巡檢用低強度，複雜分析用高強度 |
| **「Trigger now」立即執行** | 手動立刻觸發且不破壞排程狀態 | 便於測試與驗收 |

```yaml
# ~/.hermes/config.yaml — Cron 進階設定（v0.21.0）
cron:
  jobs:
    - name: daily-security-scan
      schedule: "0 9 * * *"
      prompt: "掃描主分支的新增相依套件是否有已知 CVE，僅在有新發現時回報"
      workdir: /srv/app
      continuity: true          # 帶入上一次執行的輸出
      monitor: true             # 無變化時跳過 LLM 呼叫
      reasoning_effort: medium  # 此任務專用的推理強度
      notify: slack:#sec-alerts
```

> 💡 **成本實務**：`monitor: true` 是本次更新中對 TCO 影響最大的單一設定。一個每 15 分鐘執行、但九成時間「無事發生」的監控任務，開啟後可省下約九成的 LLM 呼叫費用。
>
> ⚠️ **v0.21.0 修正**：先前版本存在「Cron 任務誤繼承 Kanban Worker 派工者身分」的缺陷，同時使用 Cron 與 Kanban 的環境建議升級。

### 6.7 SOUL.md 與 Personality 系統

SOUL.md 是 Hermes Agent 的人格定義檔案，決定 Agent 的說話風格、行為準則和限制條件。每個 Profile 可以有獨立的 SOUL.md。

#### 6.7.1 SOUL.md 結構

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

#### 6.7.2 Personality 切換

```bash
# 設定人格
/personality professional    # 專業模式
/personality friendly        # 友善模式
/personality concise         # 精簡模式

# 自訂人格（寫入 SOUL.md）
> 請調整你的人格為：專業但友善的金融科技顧問
```

#### 6.7.3 多 Profile SOUL.md 管理

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

#### 6.8.1 支援的 Context Files

| 檔案 | 位置 | 用途 |
| ------ | ------ | ------ |
| `AGENTS.md` | 專案根目錄 | 專案上下文、規範、技術棧說明 |
| `SOUL.md` | `~/.hermes/` 或 Profile 目錄 | Agent 人格定義 |
| `MEMORY.md` | `~/.hermes/memories/` | 持久化知識與經驗 |
| `USER.md` | `~/.hermes/memories/` | 使用者偏好記錄 |
| `.hermesignore` | 專案根目錄 | 排除 Agent 不應讀取的檔案 |

#### 6.8.2 AGENTS.md 最佳實踐

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

#### 6.8.3 .hermesignore 範例

```gitignore
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
| -------- | ------ | ------ |
| `plugins/platform-teams` | 平台 | Microsoft Teams 整合（第 19 平台） |
| `plugins/platform-yuanbao` | 平台 | 騰訊元寶整合（第 18 平台） |
| `plugins/model-lmstudio` | 模型 | LM Studio first-class Provider |
| `plugins/model-azure-foundry` | 模型 | Azure AI Foundry Provider |
| `plugins/model-tencent` | 模型 | Tencent Tokenhub Provider |
| `plugins/tool-spotify` | 工具 | Spotify 原生整合（7 工具 + PKCE OAuth） |
| `plugins/tool-google-meet` | 工具 | Google Meet 加入/轉錄/發言 |
| `plugins/tool-comfyui` | 工具 | ComfyUI v5 圖像生成（預設內建） |
| `plugins/tool-touchdesigner` | 工具 | TouchDesigner-MCP（預設內建） |
| `plugins/observability-langfuse` | 可觀測性 | Langfuse tracing + metrics |
| `plugins/hermes-achievements` | 擴展 | 成就系統 gamification |
| **`plugins/platform-google-chat`** | **平台** | **Google Chat 整合（v0.13.0 第 20 平台）+ 通用 Platform-Plugin Hooks** |
| **`plugins/model-providers/*`** | **模型** | **ProviderProfile ABC — Provider 可插拔化（v0.13.0）** |

#### 6.9.2.1 v0.13.0 Plugin 新功能

| 功能 | 說明 |
| ------ | ------ |
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

#### 6.9.5 自訂 Plugin 開發（官方標準結構）

Plugin 目錄需包含清單檔 `plugin.yaml` 與進入點 `__init__.py`：

```text
~/.hermes/plugins/my-custom-tool/
├── plugin.yaml       # 清單：name / version / description / capabilities / requires_env
├── __init__.py        # register(ctx) 進入點
├── schemas.py          # 工具參數 Schema（選用）
└── tools.py             # 工具實作（選用）
```

```yaml
# plugin.yaml
name: my-custom-tool
version: "1.0.0"
description: "封裝內部 JIRA API 為 Agent 工具"
capabilities: []          # 如需覆寫工具行為填 tools.override，需存取 LLM 填 llm.model_override
requires_env: ["JIRA_API_TOKEN"]
```

```python
# __init__.py
def register(ctx):
    ctx.register_tool(
        name="jira_create_ticket",
        toolset="jira",
        schema={"title": "string", "description": "string"},
        handler=create_ticket_handler,
    )
    ctx.register_hook("post_tool_call", on_tool_result)
    ctx.register_command("jira-status", jira_status_handler, description="查詢 JIRA 專案狀態")
```

**`PluginContext`（`ctx`）核心 API**：`register_tool`（新增工具）、`register_hook`（掛接 26 種生命週期事件之一，如 `pre_tool_call`／`transform_llm_output`／`on_session_end`）、`register_command`（新增 `/name` 斜線指令）、`register_cli_command`（新增 `hermes <plugin> <subcommand>`）、`register_skill`（隨 Plugin 附帶 Skill）、`inject_message`（插入訊息至對話）、`call_mcp`（呼叫已設定的 MCP 伺服器）。

**探索來源**：官方內建（`<repo>/plugins/`）、使用者（`~/.hermes/plugins/`）、專案層級（`.hermes/plugins/`，需 `HERMES_ENABLE_PROJECT_PLUGINS=true` 明確開啟）、pip entry points（`hermes_agent.plugins`）、Nix module。

> ⚠️ **安全模型（官方原文）**：「Plugin 以 in-process Python 執行——capabilities 是同意層（consent layer），不是沙箱（sandbox）」。一般 Plugin **預設全部停用**，需在 `config.yaml` 的 `plugins.enabled` 明確列出才會載入；安裝與每次更新新增權限時皆會提示使用者同意。企業導入任何第三方 Plugin 前，應視同引入可完整存取 Agent Process 的程式碼進行審查，而非僅信任其描述文字。

```yaml
# config.yaml — Plugin 啟用控制
plugins:
  enabled: [my-custom-tool, disk-cleanup]
  disabled: [noisy-plugin]
```

**Plugin Packs**（`hermes plugins pack install ./hermes-pack.yaml`）：以 `hermes-pack.yaml` 將多個 Plugin 釘選至精確 commit SHA 一次性分享安裝，安裝時僅需確認一次所有權限；秘密憑證不會隨 Pack 一併打包。

> **企業建議**：善用 Plugin 系統將內部系統（JIRA、Confluence、內部 API）封裝為 Plugin，讓 Agent 能直接操作企業工具鏈；跨團隊分享時優先使用 Plugin Pack 釘選版本，避免非預期的自動更新引入未經審查的行為變更。Desktop 端的對應能力另見 1.4.32 節「Desktop Plugin SDK」。

### 6.10 Batch Processing 與 Trajectory Format

#### 6.10.1 Batch Processing（批次軌跡生成）

Hermes 原生支援**批次執行大量任務並記錄完整執行軌跡（trajectory）**——同一份提示模板套用到成百上千筆輸入，每一筆的完整推理過程、工具呼叫序列與最終結果都被結構化保存。官方文件將此列於自動化章節（`/docs/user-guide/features/batch-processing`）。

**企業實務用途**（與模型訓練無關的那些）：

- **大規模程式碼庫改造**：對 800 個微服務各跑一次相同的相依套件升級檢查，產出可比對的結構化報表
- **迴歸驗證**：改動 Skill 或 SOUL.md 後，以同一批基準任務重跑，比對前後軌跡差異，量化「改動有沒有讓 Agent 變笨」
- **稽核證據**：軌跡是完整的執行證據鏈，可作為自動化決策的可追溯紀錄

#### 6.10.2 Trajectory Format（軌跡格式）

軌跡格式在官方開發者指南中有正式規格（`/docs/developer-guide/trajectory-format`），其設計目的之一即為**產出可直接用於模型訓練的資料集**——這與 Nous Research 作為模型訓練實驗室的本業直接相關。

> ⚠️ **資料治理提醒（與 [9.7.3](#973-與其他-coding-agent-的能力定位比較) 交叉參照）**：軌跡包含 Agent 看過的檔案內容、工具輸出與完整推理過程，屬於**高敏感度資料**。獨立評測曾指出「軌跡資料回流用於官方模型訓練」的策略誘因值得留意。
>
> 需要澄清的是：**自架的 Hermes 不會自動把軌跡上傳給 Nous Research**——軌跡預設存放於本機。真正需要控管的是三件事：(1) 是否使用了會保留資料的 Provider 資料層級（v0.21.0 已在各模型選擇器統一顯示 data-training-tier 警示）；(2) `hermes sessions export` 匯出時是否使用 `--redact`；(3) 團隊是否有人手動將軌跡分享至外部。企業應將軌跡納入既有的敏感資料分類與保存政策，而非視為單純的日誌。

---

## 第七章：Voice Mode（語音模式）

### 7.1 語音模式概述

Hermes Agent v0.3.0+ 支援語音互動能力，v0.20.0「The Herald Release」起由「錄音→轉錄→回覆→播放」的輪替式互動，升級為**真正的即時對話式語音**，可在 CLI、Desktop、Telegram、Discord 及 WhatsApp／飛書／釘釘／LINE／QQ／Photon／微信等訊息平台進行語音互動。語音模式整合 STT（語音轉文字）和 TTS（文字轉語音）雙向轉換，適用於免手動操作場景。

**v0.20.0 即時對話式語音三大能力**：
- **逐句串流播放 + Barge-in 插話**：Hermes 隨回應串流逐句朗讀，使用者可隨時開口打斷正在播放的語音，Agent 會立即停止播放、轉為聆聽，並得知自己是被中途打斷（而非誤判為新的獨立提問）
- **裝置端喚醒詞**：開放詞彙的自訂喚醒短語（如「Hey Hermes」），偵測完全在裝置端執行，語音資料不外流；多 Profile 可各自綁定不同喚醒詞，實現「一裝置多身分」語音路由
- **語音全平台覆蓋**：前述訊息平台送出的語音訊息均可自動轉錄與回覆，並依平台特性自動選擇音訊編碼（如 Opus）與字幕呈現方式

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

| Provider | 說明 | 延遲 | 費用 | 特點 |
| ---------- | ------ | ------ | ------ | ------ |
| **faster-whisper**（本地） | 本地執行，tiny/base/small/medium/large-v3 多種模型尺寸 | 依模型與硬體而定 | 免費 | 免 API Key，base 模型約 150MB，完全離線 |
| **Groq**（`whisper-large-v3-turbo`） | 雲端高速推論 | ~0.5s | 有免費額度 | 官方文件列為預設 Fallback 優先順位第二 |
| OpenAI（`gpt-transcribe`） | 官方雲端 STT | 略高 | $0.0045／分鐘 | 官方文件標註「品質最佳」 |
| Mistral（Voxtral Transcribe） | Mistral AI STT | 中等 | 依方案 | 多語言 |
| xAI | xAI 語音轉文字 | 中等 | 依方案 | 與 xAI 生態系整合 |

> **Fallback 優先序**（官方預設）：本地 faster-whisper → Groq → OpenAI，依序嘗試直到成功，兼顧成本與可用性。

#### 7.2.2 TTS（文字轉語音）提供者

| Provider | 說明 | 延遲 | 費用 | 特點 |
| ---------- | ------ | ------ | ------ | ------ |
| **Edge TTS** | 微軟 Edge 引擎 | ~1s | 免費 | 免 API Key，官方預設之一 |
| ElevenLabs | 高品質語音合成 | ~2s | 付費 | 語音克隆、高擬真度 |
| OpenAI TTS | 官方雲端 TTS | ~1.5s | 付費 | 6 種語音 |
| **NeuTTS** | 本地開源 TTS | 依硬體而定（CPU/GPU） | 免費 | 完全離線，需 `espeak-ng` |
| MiniMax（Speech 2.8） | MiniMax TTS | 中等 | 依方案 | v0.8.0 新增 |
| **xAI Custom Voices** | xAI 語音克隆 TTS | 中等 | 依方案 | 支援語音克隆（voice cloning），v0.13.0 新增，v0.15.0 起 `auto_speech_tags` 自然語調 |

> 系統依賴：語音模式需要 PortAudio、ffmpeg；Discord 語音頻道另需 Opus codec；NeuTTS 需 `espeak-ng`。安裝擴充套件：`uv pip install -e ".[voice]"`（CLI 語音）、`".[messaging]"`（Discord/Telegram 語音）、`".[tts-premium]"`（付費 TTS）。

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

  # v0.20.0: 裝置端喚醒詞與對話式語音行為
  record_key: "ctrl+b"           # CLI 錄音快捷鍵
  silence_threshold: 200          # 靜音判定音量閾值
  silence_duration: 3.0           # 靜音多久後自動結束錄音（秒）
  stop_phrases: ["stop", "停止"]  # 語音／文字說出即結束語音對話
  wake_word: "hey hermes"         # 裝置端喚醒詞，偵測不外流
```

**CLI 語音互動實際操作方式**：`Ctrl+B` 按下開始錄音，停頓 3 秒自動結束（採兩階段偵測：0.3 秒確認開始說話 + 3.0 秒判定結束），兩聲提示音確認錄音起訖，之後持續循環直到再次按 `Ctrl+B` 或說出／輸入「stop」結束；回覆採**逐句串流播放**並支援 **Barge-in**（說話即可打斷正在播放的語音）。

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

```text
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
| ------ | ---------- | ------ |
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
| -------- | ---------- | ------ |
| POST | `/api/agent/chat` | 對話（同步回應） |
| POST | `/api/agent/stream` | 對話（SSE 串流） |
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
| ------ | ------ |
| 開發環境 | `.env` 檔案（加入 `.gitignore`） |
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
| ------ | ------ | ---------- |
| `always` | 所有指令都需審批 | 高安全環境（銀行核心系統） |
| `smart` | 智慧判斷，危險指令要求審批 | 一般企業（推薦） |
| `never` | 不審批（白名單仍生效） | 信任環境 |
| `yolo` | 完全不審批（`--yolo` flag） | 僅限開發測試 |

#### 9.1.3 MCP 安全

- **OAuth 2.1 PKCE**（v0.5.0+）：所有 MCP 伺服器連線支援標準 OAuth 認證
- **OSV 掃描**：自動檢測 MCP 套件是否有已知漏洞
- **工具過濾**：可限制 MCP 伺服器暴露給 Agent 的工具
- **OAuth TOCTOU 關閉**（v0.13.0）：MCP OAuth 憑證儲存的時間競爭窗口已修正
- **SSE Transport OAuth 轉發**（v0.13.0）：SSE 連線自動轉發 OAuth 認證

#### 9.1.4 安全強化歷程（v0.5.0 — v0.21.0 持續強化）

| 防護項目 | 實作 |
| ---------- | ------ |
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
| **`hermes security audit`** | OSV.dev 供應鏈審計子指令，掃描所有依賴漏洞（v0.15.0 導入，原名 `hermes audit`） |
| **mTLS for MCP** | MCP 伺服器支援雙向 TLS 認證（v0.15.0） |
| **xAI `base_url` 洩漏防護** | 防止 xAI base_url 透過工具呼叫洩漏（v0.15.0） |
| **Docker `--insecure` 顯式 opt-in** | 不安全 Docker 連線改為顯式環境變數啟用（v0.15.1） |
| **CVE-2026-48710（Starlette）** | 修補上游 Starlette 漏洞（v0.16.0） |
| **SSRF off-loop 強化** | 非主迴圈路徑的 SSRF 防護補強（v0.16.0） |
| **Secure Dashboard Login** | 401 OAuth 閘門強化、WebSocket 認證 Token、`public_url` 覆寫警告（v0.17.0） |
| **P0／P1 議題清零** | 3 項 P0 + 493 項 P1 一次性清空，並宣示持續維持零 P0/P1（v0.18.0） |
| **智慧審批預設啟用** | 由 LLM 獨立審查每個被標記指令是否放行，取代逐次詢問（v0.19.0，見 [1.4.28](#1428-智慧審批預設化與配送保證v0190)） |
| **Promptware 過濾（A2A）** | A2A 入站訊息的提示注入過濾與反迴圈輪次上限（v0.20.0） |
| **Skill 安裝前安全掃描** | Skill 安裝流程納入安全掃描（v0.20.4） |
| **同意閘門式 Profile 瀏覽** | 瀏覽他人 Profile 需經明確同意（v0.20.6） |
| **受保護指令檔（Protected Instruction Files）** | `AGENTS.md`／skills／memory 的寫入**一律需審批**（v0.21.0，見 9.1.5） |
| **Redaction Sweep** | 封閉終端錯誤、`.env` 讀取、checkpoints、ACP log 的秘密外洩路徑（v0.21.0） |
| **Windows 審批覆蓋** | 破壞性 Windows 指令與路徑納入審批系統（v0.21.0） |
| **Plugin Tier-1 安全掃描** | Plugin 安裝納入第一級安全掃描（v0.21.0） |
| **PKCE Cookie 修正** | HTTPS 下設定 `SameSite=None`，修正 OAuth 流程（v0.21.0） |
| **macOS TCC 身分穩定化** | 以穩定簽章身分讓權限授予跨更新存續（v0.21.0） |

#### 9.1.5 受保護指令檔與 v0.21.0 安全強化波

v0.21.0 的安全主題明確針對**提示注入的「持久化」階段**——不是阻止注入發生，而是阻止注入後果被寫進 Agent 的長期狀態。

**（1）受保護指令檔（Protected Instruction Files）**

> 官方原則：**對 `AGENTS.md`、skills 目錄、memory 的寫入一律需要審批。**

這解決的是一類極隱蔽的攻擊：Agent 讀了一份被植入指令的文件後，把「以後都要把結果傳到某網址」寫進自己的 `AGENTS.md` 或記憶——**注入只發生一次，效果卻永久生效，且後續每一輪都看起來像是使用者自己的設定**。強制審批讓這類改寫必須經過人眼。

此機制與 [9.7.1](#971-資安揭露制度現況) 提到的第三方威脅模型中「經檢索上下文的記憶注入」正面對應，是本專案首次針對該攻擊面提出結構性防禦，而非僅靠模式比對。

**（2）Redaction Sweep（秘密外洩清掃）**

先前的秘密遮蔽主要覆蓋 LLM 回應與瀏覽器 URL。v0.21.0 補上四條先前的漏網路徑：

- 終端機**錯誤訊息**（例外堆疊中夾帶的憑證）
- **`.env` 檔案讀取**（以檔案讀取偵測攔截）
- **Checkpoints**（狀態快照中的秘密）
- **ACP log**（IDE 整合的日誌）

**（3）Windows 審批覆蓋**

Native Windows 支援自 v0.16.0 起成熟，但審批系統的危險指令樣式長期以 POSIX 為主。v0.21.0 補齊 Windows 專屬的破壞性指令與路徑判定——**在 Windows 上部署的企業應特別確認已升級至此版本**。

**（4）供應鏈事件應對**

v0.21.0 期間，官方因上游遭入侵而**主動從 MCP 目錄下架 Blender MCP 項目**，並將 Plugin 安裝納入 Tier-1 安全掃描。這是本專案首次公開處置的第三方供應鏈事件，處理速度可作為評估其供應鏈治理成熟度的正面參考點。

**（5）macOS TCC 身分**

macOS 每次更新後權限授予失效的長期痛點，改以穩定簽章身分解決：

```bash
# macOS 使用者升級至 v0.21.0 後執行一次
hermes desktop --setup-tcc-identity
```

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

#### 9.3.5 非同步處理

```bash
# 背景任務 + 自動通知（v0.8.0 新增 notify_on_complete）
> 在背景執行完整測試套件，完成後通知我

# Agent 使用 execute_command 的 background + notify_on_complete
# 測試完成後自動通知到 CLI / Telegram / Discord
```

#### 9.3.6 Subagent 平行化

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
| ---------- | ------ |
| Request Rate | 每分鐘請求數（by model / profile） |
| Token Usage | 每小時 Token 消耗（by provider） |
| Error Rate | 錯誤率（by error type） |
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

```text
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
| ---------- | ---------- |
| API 暫時不可用 | 指數退避重試（最多 4 次） |
| Token 餘額不足（402） | 自動切換 Fallback Provider |
| 速率限制（429） | 指數退避 + Jitter |
| 模型不支援工具呼叫 | 顯示警告，建議切換模型 |
| Context 溢出 | 自動 Compaction |
| 工具執行失敗 | 重試或改用替代工具 |
| 網路中斷 | 自動重連（Gateway 支援） |

> **實務案例**：某金融企業使用 Hermes Agent 做 24/7 自動化監控。透過 Cron 排程每小時檢查系統健康度，搭配 Telegram 通知。Provider Failover 確保即使某個 API 當機，Agent 仍可用備援模型持續運作，系統可用性達 99.9%。

### 9.6 Tips & Best Practices

以下是根據官方文檔和社群經驗整理的最佳實踐清單：

#### 9.6.1 開發效率

| 技巧 | 說明 |
| ------ | ------ |
| 使用 AGENTS.md | 在專案根目錄放置 AGENTS.md，Agent 會自動載入專案規範 |
| 善用 Skill 封裝 | 複雜的重複任務封裝為 Skill，一次定義多次使用 |
| 使用 `/compress` | 長對話時定期壓縮上下文，節省 Token 並維持效能 |
| 善用 Subagent | 複雜任務使用 `delegate_task` 平行處理，減少總等待時間 |
| Context Files | 建立完整的 AGENTS.md + SOUL.md，確保輸出品質一致 |
| Programmatic Tool Calling | 使用 `execute_code` 批次操作，將多步驟壓縮為單次推理 |

#### 9.6.2 成本優化

| 技巧 | 節省幅度 | 說明 |
| ------ | ---------- | ------ |
| 免費輔助模型 | ~60% | 使用 Nous Portal mimo-v2-pro 處理壓縮/摘要 |
| 自動壓縮 | ~30% | 設定 `context.auto_compress: true` |
| 模型分級 | ~50% | 簡單任務用小模型，複雜任務用大模型 |
| `/insights` 監控 | - | 定期查看 Token 使用趨勢，識別浪費 |

#### 9.6.3 安全運作

| 技巧 | 說明 |
| ------ | ------ |
| `command_approval: smart` | 不要使用 `yolo` 模式在生產環境 |
| 白名單機制 | 明確列出允許的指令，縮小攻擊面 |
| Gateway `allowed_users` | 限制可與 Agent 對話的使用者 |
| API Key 輪換 | 每 90 天輪換，使用 Vault 管理 |
| MCP OAuth | 啟用 OAuth 2.1 PKCE 認證所有 MCP 連線 |
| 日誌審計 | 啟用集中式日誌，定期審計 Agent 行為 |

#### 9.6.4 維運穩定

| 技巧 | 說明 |
| ------ | ------ |
| Provider Failover | 至少配置 2 個 Provider |
| `hermes doctor` | 升級後必執行，驗證環境完整性 |
| 備份 `~/.hermes/` | 每日備份 Skills、Memories、Config |
| Health Check | Docker / K8s 配置 `hermes doctor --quick` |
| Profile 隔離 | 不同團隊使用不同 Profile，避免互相干擾 |

### 9.7 風險評估與治理考量（企業導入前必讀）

多數技術文件僅羅列功能，本節依「企業技術白皮書」慣例，補上功能清單之外、採購與風險評估決策者需要的資訊。以下內容逐條核對 NVD、GitHub Advisory Database 與獨立第三方評測，並非官方行銷素材。

#### 9.7.1 資安揭露制度現況

- **Nous Research 未自行發布任何 GitHub Security Advisory（GHSA）**：截至查證當下，官方倉庫的 Security Advisories 頁面顯示「There aren't any published security advisories」。目前可查得的多個 CVE（如 CVE-2026-9368 `execute_code` 沙箱繞過、CVE-2026-53869 WebSocket 端點缺少驗證、CVE-2026-11461 Session 解析授權繞過等）**均由第三方 CNA（主要為 VulDB）指派**，而非官方協調揭露流程；多筆 NVD 紀錄明確註記「vendor was contacted... but did not respond」。
- 這與「原廠自行營運揭露／修補流程」是本質不同的資安治理姿態，企業評估時應納入採購風險考量，而非預設等同於有正式資安回應 SLA 的商用產品。
- 另有 **CVE-2026-7396**（WeChat 平台轉接器路徑穿越，影響程度低）由第三方揭露。截至 2026-09-01 覆查，官方 Security Advisories 頁面仍顯示「There aren't any published security advisories」，此姿態未隨版本推進而改變。
- 正向對照：Hermes 官方版本紀錄中**可查證的主動安全清理行動**相對積極——v0.13.0「The Tenacity Release」8 項 P0 安全修正、v0.16.0 修補 CVE-2026-48710（Starlette 上游漏洞）、v0.18.0 一次性清空全部 3 項 P0 與 493 項 P1 議題並公開宣示「持續維持零 P0/P1」、v0.21.0 的受保護指令檔與 Redaction Sweep（見 [9.1.5](#915-受保護指令檔與-v0210-安全強化波)），以及首次公開處置第三方供應鏈事件（Blender MCP 下架）。換言之：**專案回應已知內部議題積極，但對外部研究者的協調揭露回應機制尚未成熟**，兩者需分開評估。

**第三方企業威脅模型（獨立觀點，非官方素材）**

一份針對「企業工作站部署」的獨立威脅模型分析歸納出四大攻擊面，其價值在於指出**架構性風險的量級遠大於已揭露 CVE 的數量**——換言之，用「CVE 很少」來論證安全性是誤導的：

| 攻擊面 | 核心風險 | Hermes 官方對應現況 |
| ------ | ------ | ------ |
| **技能市集供應鏈** | Skill 本質上是 Agent 會安裝並執行的任意程式碼，惡意 Skill 可執行 Shell 指令、外洩 API Key、破壞檔案 | v0.20.4 起安裝前安全掃描、v0.17.0 Skills Hub 安全掃描、v0.21.0 Plugin Tier-1 掃描；**但掃描非沙箱**，企業仍須自行審查 |
| **經檢索上下文的記憶注入**（最具 Hermes 特異性） | 攻擊者在 Agent 會摘要的文件中植入指令，污染持久 SQLite 記憶；日後每次檢索都靜默執行——**繞過所有只監控「使用者輸入」的傳統提示注入防禦** | v0.15.0 Promptware 防禦（記憶載入時掃描）、**v0.21.0 受保護指令檔（memory 寫入需審批）為目前最有效的結構性對策** |
| **多 Provider 憑證曝險** | Agent 同時持有多家 LLM 的有效 API Key，經日誌、除錯產物、錯誤訊息意外外洩 | v0.13.0 Secret Redaction 預設開啟、v0.15.0 Bitwarden、v0.19.0 密碼管理器整合、**v0.21.0 Redaction Sweep**、[9.8 節 iron-proxy](#98-egress-憑證注入代理iron-proxy-沙箱零信任外連)（真實金鑰不進沙箱） |
| **MCP 信任邊界** | 連接的 MCP 伺服器預設認證與能力範圍限縮不足 | v0.15.0 mTLS、v0.13.0 OAuth 轉發、v0.21.0 MCP Command Center 健康檢查；**能力範圍限縮仍主要仰賴使用者自行設定** |

> **企業關鍵結論**：上述攻擊多半運作於**提示層與資料層**，而非行程層——**標準端點偵測（EDR）完全看不到**。持久記憶是架構層面的固有風險，無法單靠打補丁消除。企業若在工作站大規模部署，應規劃：Skill 安裝的 manifest 審查與能力白名單、記憶內容的加密與版本追蹤、所有工具呼叫與輸出的完整日誌並串接 SIEM，以及在檢索到的記憶進入工具執行前做指令樣式偵測。

#### 9.7.2 貢獻者規模與專案永續性（Bus Factor）

- 見 1.1 節「核心數據」已揭露的官方數字（370–450+／版本）與 GitHub API 一手數字（396 具名帳號）之口徑差異。
- 一份獨立技術評測（見文末參考資源）另指出「核心維護者僅約 30 人、對應近 1,800 個開放 Issue」，评估者將此列為維運債／單點失效風險；此數字與官方口徑差異更大，可能僅計入具倉庫寫入權限的核心成員，本文無法完全調解此落差，企業評估時建議自行以 `git shortlog` 或倉庫 Insights 交叉核對後再下判斷。
- **建議**：導入前確認團隊自身是否具備 Python／TypeScript 內部維運能力，不宜完全依賴上游修補節奏（尤其是 patch 版本如 v0.18.1/v0.18.2 官方明確聲明「非精選版本、不列完整清單」，代表細節修正需自行追蹤 commit 而非僅讀 Release Notes）。

#### 9.7.3 與其他 Coding Agent 的能力定位比較

| 面向 | Hermes Agent | Claude Code／Codex CLI |
| ------ | ------ | ------ |
| 多平台訊息整合 | 強項（30+ 平台原生支援，同類產品中最完整） | 較弱（多聚焦 IDE／終端機） |
| 持久記憶／自我學習 | 強項（Learning Loop + 9 種可插拔記憶後端） | 多需外部插件或手動維護 CLAUDE.md |
| 程式碼導覽深度（LSP／AST 感知） | **早期評測所稱「缺乏原生 LSP／AST 整合」已不成立**：v0.14.0 起提供原生 LSP 語義診斷（`hermes lsp`，write_file／patch 後由真實 Language Server 分析），v0.21.0 另新增 ast-grep codemods 技能。惟大型程式碼庫的整體導覽體驗仍略遜 | 強項，原生深度整合、生態更成熟 |
| 測試套件穩定性 | 官方 AGENTS.md 明確警告「不建議直接執行 pytest」，反映環境耦合的脆弱性；v0.21.0 已導入 macOS／Windows 真實 OS CI 車道改善此問題 | 相對成熟 |
| 多 Agent 協作機制 | **強項**：同時提供 delegate_task、Kanban、Bot Mode 群組、`hermes peer`、A2A v1.0 五種層次（見 [15.5](#155-五種多-agent-機制選型對照)） | 較單一，多以子代理委派為主 |
| 授權與可自架性 | MIT，可完全自架、零強制雲端依賴 | 依產品而異，多數依賴官方雲端服務 |
| 資料流向 | 獨立評測認為「軌跡資料回流用於官方模型訓練」的策略誘因值得留意；實務上自架版軌跡預設留在本機，需控管的是 Provider 資料層級與匯出行為（見 [6.10.2](#6102-trajectory-format軌跡格式)） | 依各家隱私條款而異 |
| 發版節奏 | **極快**（約每 2–4 週一個 Minor，中間密集 patch），功能領先但版本追蹤成本高 | 相對穩定可預期 |

> **企業建議**：Hermes Agent 的差異化優勢在於「多平台入口 + 持久記憶 + 自我學習」的**通用型助理與跨平台自動化場景**；若核心需求是**深度軟體工程／大型程式碼庫導覽**，建議將 Claude Code、Codex CLI 等納入並列評估，而非視為互斥的單選題——兩者也可透過 6.9 節 Plugin 系統或 `hermes import-agent`／`hermes claw migrate` 併存或漸進遷移。

#### 9.7.4 Nous Portal 訂閱定價與總持有成本（TCO）

Hermes Agent 軟體本體 **完全免費、MIT 授權、可無限自架**，訂閱制僅存在於選用的代管服務 **Nous Portal**：

| 方案 | 月費（二手來源，未經一手頁面核實） | 每月使用額度 | 簽約／升級／續約 Bonus |
| ------ | ------ | ------ | ------ |
| Free | $0 | — | — |
| Plus | ~$20／月 | ~$22 | +$2 |
| Super | ~$100／月 | ~$110 | +$10 |
| Ultra | ~$200／月 | ~$220 | +$20 |

付費方案共通內容：**300+ 前沿模型單一帳單**（Anthropic Claude、OpenAI GPT、Google Gemini、DeepSeek 等）＋ **Nous Tool Gateway 五項代管工具**：

| 代管工具 | 底層服務 | 備註 |
| ------ | ------ | ------ |
| 網頁搜尋與擷取 | Firecrawl | — |
| 圖片生成 | 9 種模型（含 FLUX 2、GPT Image、Ideogram V3） | — |
| 文字轉語音（TTS） | OpenAI TTS | — |
| 瀏覽器自動化 | Browser Use | — |
| **雲端終端沙箱** | Modal | **選購加購項目**，非方案內含 |

**認證機制**：Hermes 在本機儲存 Portal 的 refresh token，**每次推論呼叫即時簽發短效 JWT**，而非長期存放 API Key——這對「工作站遭入侵時的憑證曝險面」是正面設計，值得在資安評估中列為加分項。Ultra 方案另享全方案中最高的速率限制。

> ⚠️ **查證狀態未變**：上表金額於本次（2026-09-01）覆查時，官方定價頁 `portal.nousresearch.com/manage-subscription` **仍回應 HTTP 429**。數字係由多個獨立第三方來源交叉比對取得一致結果，**正式採購前務必至官方頁面或以 `/subscription` 指令於終端機內覆核**（v0.19.0 起支援）。
>
> **完整 TCO 除訂閱費／API 費用外，企業還應納入**：(1) 自架基礎設施成本（VPS／K8s／GPU，見第十章）；(2) 內部整合與客製 Skill／Plugin 開發人力；(3) 因無官方 SLA（Hermes Cloud 目前仍為 Preview 階段，無正式運行時間承諾）而需自建的監控與備援機制；(4) **版本快速迭代（約每 2–4 週一個 Minor，中間另有密集 patch；光是 2026 年 8 月即發布 v0.20.1 至 v0.21.0 共 7 個版本）帶來的持續追蹤與回歸驗證人力**；(5) v0.21.0 提高委派預設併發後，若未主動設限而放大的推論支出。**開源 ≠ 零成本**，僅代表授權費為零。

#### 9.7.5 生態系鎖定風險

Hermes 標榜「Model Agnostic、無廠商鎖定」，但企業仍應留意生態系層面的實質轉換成本：

- **技能／記憶資產鎖定**：透過 `/learn` 累積的 Skill 庫、MEMORY.md／USER.md 及各記憶 Provider 內的知識圖譜，格式與 Hermes 的 Skill／記憶架構綁定，遷移至其他 Agent 框架需重新萃取
- **社群外掛供應鏈**：`awesome-hermes-agent` 等社群目錄雖標註 production／beta／experimental 成熟度，但明確聲明僅為「發現輔助工具，非安全背書」，導入任何第三方 Skill／Plugin 前應自行審查其權限範圍、可觸發者與可讀取憑證
- **企業級功能仍在早期階段**：團隊帳單、存取控制的 Hermes Cloud 目前仍為 Preview，尚無正式 SLA、SOC 2／DPA 等採購文件；坊間確有第三方顧問公司提供 CMMC／HIPAA／SOC 2 就緒的代管部署服務，但屬於第三方加值服務，非 Nous Research 官方保證

#### 9.7.6 企業導入前風險檢查清單

- [ ] 已確認團隊內部具備 Python／TypeScript 除錯能力，可不完全依賴上游支援節奏
- [ ] 已將「Nous Research 目前未自行發布 GHSA」納入資安治理評估，並規劃內部依 NVD／第三方情資的定期掃描（`hermes security audit` 為必要但非充分條件）
- [ ] 已針對核心工作負載（程式碼工程 vs. 跨平台助理／自動化）確認 Hermes 的能力定位是否匹配，而非僅因「開源、免費」而選型
- [ ] 已將 Nous Portal 訂閱費用（如採用）以外的整合、監控、備援人力成本納入 TCO 試算，並以官方一手定價頁完成最終覆核
- [ ] 已對將導入的任何社群 Skill／Plugin 完成權限與資料流向審查，而非僅依賴其成熟度標籤
- [ ] 若合規要求需要正式 SLA／DPA／SOC 2 報告，已確認 Hermes Cloud（Preview 階段）或替代自架方案能否滿足，而非預設存在
- [ ] **（v0.21.0）** 若有 Docker 沙箱工作負載，已評估是否啟用 [9.8 節 iron-proxy 憑證注入代理](#98-egress-憑證注入代理iron-proxy-沙箱零信任外連)，並確認其「僅支援 Docker backend、簽章式認證 Provider 會繞過」的限制不影響實際防護目標
- [ ] **（v0.21.0）** 已確認 [Managed Scope](#48-managed-scope組織層級設定釘選) **未被誤當作權限控管邊界**，敏感 Secret 未放入全域可讀的 `/etc/hermes/.env`
- [ ] **（v0.21.0）** 已就 **Bot Mode 預設開啟**做出明確治理決策（採用或關閉），而非因未察覺而預設啟用；並評估多 bot 並行的成本與稽核影響
- [ ] **（v0.21.0）** 已將 `model_overrides` 這類「繞過官方目錄」的覆寫機制納入設定檔版本控管與變更審核流程
- [ ] **（v0.21.0）** 已依實際預算調降 `delegate_task` 提高後的預設值（250 iterations／10 並行），並建立 `/usage`／`hermes insights` 的定期成本檢視機制
- [ ] 已針對「持久記憶為架構性攻擊面、EDR 無法偵測」規劃記憶內容審查、工具呼叫全量日誌與 SIEM 串接

### 9.8 Egress 憑證注入代理（iron-proxy）— 沙箱零信任外連

這是 Hermes 目前**最接近「零信任」設計的企業級安全能力**，對於在 Docker 沙箱中執行不可信任工作負載的組織尤其關鍵。

#### 9.8.1 名稱釐清：與 `hermes proxy` 完全不同

兩者名稱相近但方向與用途完全相反，實務上極易混淆：

| — | `hermes proxy`（[1.4.13](#1413-hermes-proxy--openai-相容本地代理v0140)） | `hermes egress`（iron-proxy，本節） |
| ------ | ------ | ------ |
| 方向 | **入站**：接受第三方工具的請求 | **出站**：攔截沙箱對外的請求 |
| 目的 | OpenAI 相容聚合器，讓 Aider／Cline／Cursor 共用 Hermes 的訂閱 | **防止被提示注入的 Agent 從沙箱外洩真實 API 憑證** |
| 位置 | 位於第三方工具與 Hermes 之間 | 位於**沙箱與上游 Provider 之間** |

#### 9.8.2 解決什麼問題

傳統做法是把 `OPENROUTER_API_KEY` 之類的真實金鑰直接放進 Docker 沙箱的環境變數。一旦 Agent 被提示注入攻擊，沙箱內的金鑰即可被完整讀出並外送——**金鑰本身就在攻擊者手中**。

iron-proxy 的核心主張：**真實憑證永遠不進入沙箱**。沙箱拿到的只是不透明的代理權杖（proxy token），對代理邊界之外毫無用處。

#### 9.8.3 架構與運作原理

三個組成元件：

| 元件 | 位置 | 說明 |
| ------ | ------ | ------ |
| Host 端 daemon | `~/.hermes/bin/iron-proxy`，預設監聽 port 9090 | 以子行程形式由 Hermes 管理 |
| 憑證基礎設施 | `~/.hermes/proxy/ca.crt`（公開）、`ca.key`（敏感，`0o600`） | 自簽 CA |
| 設定與對應表 | `proxy.yaml`（允許清單）、`mappings.json`（代理權杖 ↔ 上游憑證對應） | — |

**請求生命週期**：

1. 沙箱啟動時掛載唯讀的 CA 憑證，環境變數指向代理，並注入**代理權杖**而非真實金鑰
2. Provider SDK 照常發出 HTTPS 請求，權杖落在標準位置：`Authorization`（Bearer）、`x-api-key`（Anthropic）、`api-key`（Azure OpenAI）、`?key=`（Google）
3. daemon 以動態簽發的 leaf 憑證進行 TLS 終止，**先驗證目的地主機名是否在允許清單內**
4. 將該標頭／查詢參數中的權杖**替換為 daemon 自身環境中的真實憑證**，重新加密後轉發上游

daemon 與 Hermes 同一使用者身分執行於 host 上，真實憑證始終留在 host 的行程記憶體中，於傳輸途中即時換入。

#### 9.8.4 完整設定鍵參考

```yaml
# ~/.hermes/config.yaml
proxy:
  enabled: false            # 總開關，預設關閉
  tunnel_port: 9090         # daemon 監聽埠
  auto_install: true        # 首次使用時自動下載 iron-proxy
  credential_source: env    # env（讀 host 行程環境）或 bitwarden（每次重啟重抓）
  enforce_on_docker: true   # 預設 true：代理已啟用但未運行時，Docker 沙箱拒絕啟動
  allow_env_fallback: false # 預設 false：Bitwarden 模式設定錯誤時 fail-loud，不靜默退回
  extra_allowed_hosts:      # 內建允許清單之外的額外上游（支援 *.example.com 萬用字元）
    - "*.internal.corp"
  # upstream_deny_cidrs: 預設已封鎖 loopback、link-local（含 169.254.169.254 雲端 metadata）、
  #                      RFC1918 私有網段、IPv6 ULA、CGNAT、benchmark 網段
```

**雙層防護**：

- **主機名允許清單（預設拒絕）**：內建涵蓋 OpenRouter、OpenAI、Anthropic、Google、xAI、Mistral、Groq、Together、DeepSeek、Nous。不在清單者，請求**尚未離開 host 就先收到 HTTP 403**
- **網路層 SSRF 拒絕清單**：不論主機名是否過關，一律封鎖上表 CIDR——**雲端 metadata endpoint 的攔截尤其重要**，這是容器逃逸後最常見的橫向移動途徑

#### 9.8.5 部署與輪替操作

```bash
# 1. 安裝（下載並以 SHA-256 驗證二進位檔）
hermes egress install

# 2. 設定精靈（產生 CA 與代理權杖）
hermes egress setup

# 3. 啟動 daemon
hermes egress start

# 查看狀態（對話中亦可用 /egress）
hermes egress status
```

| 輪替情境 | 操作 |
| ------ | ------ |
| **上游憑證輪替（Bitwarden 模式）** | 於 Bitwarden Web UI 改金鑰 → host 上 `hermes egress stop && hermes egress start` → 執行中的沙箱即取得新值，**完全不需碰 `.env` 檔案** |
| 上游憑證輪替（env 模式） | 憑證於代理啟動時自 host 環境讀取，改完環境變數後重啟 daemon |
| **代理權杖輪替** | `hermes egress setup --rotate-tokens`：簽發新權杖並使舊權杖失效。⚠️ 持有舊權杖的執行中沙箱會開始收到 401，需重啟；舊 mappings 會以時間戳備份供回復 |

**日誌**：在釘選的 v0.39 二進位版本中，daemon 事件與逐請求紀錄皆以行分隔 JSON 寫入 `~/.hermes/proxy/iron-proxy.log`；官方規劃未來拆分為獨立的 daemon 與稽核串流，`audit.log` 已預先建立為占位檔。**企業串接 SIEM 時應注意此格式未來會變動**。

#### 9.8.6 已知限制（採購決策前必讀）

| 限制 | 影響與因應 |
| ------ | ------ |
| **僅接上 Docker backend** | Modal、Daytona、SSH、Singularity 後端**不會收到代理設定**，這些環境仍以真實憑證直連。若主力沙箱不是 Docker，本機制對你**無效** |
| **簽章式認證完全繞過** | AWS SigV4、GCP service-account OAuth 的認證無法以標頭替換攔截，會直接繞過代理。使用 Bedrock／Vertex AI 的企業需另行設計防護 |
| **CA 無輪替機制** | 10 年期自簽憑證，官方未提供內建輪替流程 |
| **不保護 host 本身** | host 一旦淪陷，其行程環境中的真實憑證同樣曝露。iron-proxy 縮小的是**沙箱**的爆炸半徑，不是 host 的 |
| `enforce_on_docker: false` 的取捨 | 設為 false 時沙箱會退回以真實憑證直連——僅適用於遷移或測試期間，**等同放棄隔離保證** |

> **企業建議**：iron-proxy 是目前 Hermes 生態中唯一能實質達成「憑證不落地於執行環境」的機制，對於執行不可信程式碼（如處理外部提交的 PR、分析未知倉庫）的場景**強烈建議啟用**，並維持 `enforce_on_docker: true` 的預設值。但**不應誇大其覆蓋範圍**——請先確認你的沙箱後端與 Provider 認證方式落在其保護範圍內，再將其納入合規論述。

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

# 安裝 Node.js（v0.20.0 起 26 為硬性必要條件，低於此版本 hermes 將無法啟動）
RUN curl -fsSL https://deb.nodesource.com/setup_26.x | bash - \
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
>
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
| ---------- | ------ | ------ | ------ |
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
| ------ | ---------- | ---------- | ------ |
| 開發環境 | 24h | 1h | 每日備份 |
| 測試環境 | 24h | 2h | 每日備份 |
| 生產環境 | 1h | 30min | 多副本 + 即時備份 |
| 金融環境 | 0（零丟失） | 15min | 主從 + 即時同步 |

> **實務案例**：某銀行團隊在 Kubernetes 上部署 Hermes Agent，使用 `ReadWriteMany` PVC 共享 Skills 和 Memories。每日凌晨透過 CronJob 備份到 S3，搭配 Rolling Update 策略實現零停機升級。RTO 目標 15 分鐘，RPO 目標 1 小時。

---

## 第十一章：升級與版本管理

### 11.1 升級策略

#### 11.1.1 版本號規則

Hermes Agent 使用語義化版本（附日期標籤）：

```text
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
| ------ | ------ |
| Skills 同步 | 升級後 bundled skills 會自動同步到所有 Profiles |
| Gateway 保護 | `hermes update` 不再 kill 正在運行的 gateway service |
| Config 驗證 | 啟動時會自動驗證 config.yaml 結構 |
| OpenClaw 移轉 | 如果從 OpenClaw 升級，使用 `hermes claw migrate` |

#### 11.1.5 v0.12.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| Node.js | 建議升級至 v22 LTS，影響 TUI 冷啟動效能 |
| Secret Redaction | 預設已關閉，避免 patch 損壞，如需請手動啟用 |
| Pluggable Providers | 所有 Provider 已移至 `plugins/model-*` 架構 |
| Curator 預設啟用 | 自動技能維護預設開啟，可透過 `auxiliary.curator.enabled: false` 關閉 |
| Remote Model Catalog | OpenRouter / Nous Portal 模型目錄改為遠端拉取 |

#### 11.1.6 v0.13.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| Secret Redaction | **預設翻轉為開啟**，如遇 patch 損壞可透過 `security.redaction: false` 關閉 |
| Checkpoints v2 | 新的 Checkpoint 格式，舊 Checkpoint 不會自動遷移，需要手動清除後重建 |
| `hermes update --yes` | 升級指令新增 `-y / --yes` 旗標，跳過確認直接升級（適合 CI） |
| ProviderProfile ABC | 自訂 Provider 需改寫為繼承 `ProviderProfile` ABC 介面 |
| Docker Root 拒絕 | Gateway 現拒絕以 root 身份運行，必須使用非 root 使用者 |
| Windows 正式支援 | 原生 Windows 支援已為 GA（v0.16.0+），可透過 Desktop App 或 CLI 安裝 |
| `display.language` | 新增 i18n 設定項，支援 `zh`、`ja`、`de`、`es`、`fr`、`uk`、`tr` |
| Kanban | 多 Agent Kanban 預設停用，需手動設定 `kanban.enabled: true` |

#### 11.1.7 v0.14.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
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
| ------ | ------ |
| **The Big Refactor** | `run_agent.py` 重構為 14 個 `agent/*` 模組，自訂 monkey-patch 可能需要更新路徑 |
| **移除 Vercel AI Gateway** | 如有使用 Vercel AI Gateway Provider，請遷移至其他 Provider |
| **移除 Vercel Sandbox** | Terminal Backend 移除 Vercel Sandbox，請遷移至 Docker/Daytona/Modal |
| Kanban Swarm | 新增 `hermes kanban swarm` Swarm v1 拓撲 |
| `session_search` 重建 | 不再使用 LLM，免費且快 4,500 倍 |
| Promptware 防禦 | 預設啟用，可能影響含特殊格式的 Skill/Memory 檔案 |
| Bitwarden Secrets | 新增 `secrets.backend: bitwarden` 設定選項 |
| ntfy | 新增第 23 平台 |
| s6-overlay Docker | Docker 容器監督改用 s6-overlay |
| `hermes audit` | 新增 OSV.dev 供應鏈審計指令（後續已更名為 `hermes security audit`） |
| `hermes send` | 新增腳本輸出推送至任何平台 |
| mTLS for MCP | MCP 伺服器支援雙向 TLS |
| OpenAI API 獨立 Provider | OpenAI API 現為獨立 Provider（不再與 Codex 共用） |
| FAL → Plugin | FAL 圖片生成移至 Plugin 架構 |

#### 11.1.9 v0.16.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| **Hermes Desktop App** | 新增原生桌面應用（macOS/Linux/Windows），可從官網下載安裝 |
| **Dashboard 全面升級** | Dashboard 升級為完整管理面板（Channels/MCP/Credentials/Webhooks/Memory/Gateway） |
| **Quick Setup** | `hermes portal` 一鍵快速設定（透過 Nous Portal 引導） |
| **Fuzzy Model Picker** | 所有介面統一模糊搜尋模型，取代舊有選擇器 |
| **`/undo [N]`** | 新增撤回對話指令，可能影響自訂 slash command |
| **精簡預設 Skill Set** | 重型 Skills 移至 optional，`environments:` 閘門可能影響已安裝技能可見性 |
| **選擇預設介面** | 新增 `interface: cli` 或 `interface: tui` 設定，影響 `hermes` 啟動行為 |
| **NVIDIA/skills Tap** | 新增為預設信任來源，與 OpenAI/Anthropic/HuggingFace 並列 |
| **CVE-2026-48710** | Starlette SSRF 修正，如有自訂 middleware 需確認相容性 |
| Windows GA | Windows 正式支援，不再標記為 Early Beta |

#### 11.1.10 v0.17.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| **iMessage via Photon** | 替代 BlueBubbles，無需 macOS relay。若原使用 BlueBubbles 需遷移設定 |
| **Background Subagents** | 新增 `delegate_task(background=true)`，不影響既有同步行為 |
| **Image Editing** | `image_generate` 新增 edit mode 參數，既有呼叫不受影響 |
| **Automation Blueprints** | 新增自然語言排程，與既有 `cron_add` 並存（非取代） |
| **Memory Atomic Batch** | `memory` 工具新增 `operations` 參數，單一操作呼叫仍相容 |
| **Curator 成本變更** | 預設 sweep 免費（不再呼叫 LLM），需 `consolidate: true` 才啟用 AI 合併 |
| **Secure Dashboard Login** | 401 OAuth gate 強化，自訂 Dashboard 整合需確認 auth 流程 |
| **WhatsApp Business Cloud API** | 新增官方 Meta API adapter，與既有 WhatsApp（Baileys）並存 |
| **Telegram Bot API 10.1** | Rich text 格式化升級，自訂 Telegram Plugin 需確認相容性 |
| **Skills Hub Connected Hubs** | 多 Hub 來源支援，既有安裝的 Skills 不受影響 |
| **grok-composer-2.5-fast** | 新增 Cursor Composer 模型（200k context），需 xAI 訂閱 |

#### 11.1.11 v0.18.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| **P0/P1 清零** | 大量長期存在的 Bug／安全問題於此版本一次修復，升級後建議重新執行完整回歸測試 |
| **`verify-on-stop` 預設關閉** | `/goal` 完成驗證改為選擇性；如需強制驗證需自行於 `goals` 設定中開啟 |
| **移除 `google-gemini-cli` / `google-antigravity`** | 改用新增的 `vertex` Provider（Google Vertex AI），舊 OAuth 設定需重新設定 |
| **Google Vertex AI 新增** | 建議改用 Service Account／ADC，不再需要管理靜態 API Key |

#### 11.1.12 v0.19.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| **智慧審批預設啟用** | 危險指令審批機制由「逐次詢問」變為「LLM 獨立審查」，行為模式改變，正式環境升級前建議先於測試環境驗證審查準確度 |
| **密碼管理器整合** | 新增 `secrets.sources` 設定區塊，原本平面式 `.env` 仍完全相容，屬於新增能力非破壞性變更 |
| **Profile-based Gateway 路由** | 多 Profile 共用同一 Bot Token 的部署方式需重新規劃路由規則 |
| **配送保證台帳** | Gateway 重啟後可能補送先前「疑似遺失」的回應，訊息平台整合方需留意去重邏輯 |

#### 11.1.13 v0.20.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| **Node.js 26 成為硬性必要條件** | 升級前務必先確認 CI/CD 與部署環境的 Node.js 版本，低於 26 將無法啟動 |
| **Homebrew／PyPI／pip 安裝管道停用** | 見 4.2.3 節，須改用 Shell Installer／Docker／Nix 三者之一 |
| **工具呼叫迭代上限 90 → 500** | 長時間自主執行任務的實際執行時間可能顯著拉長，需重新評估逾時與成本預算設定 |
| **壓縮機制大改** | per-turn 微壓縮取代單次大壓縮，Token 消耗曲線變得更平滑但總量計算方式改變，`/usage` 歷史對照基準需重新校準 |
| **A2A Toolset 預設關閉** | 需自行於 `toolsets.enabled` 加入 `a2a` 才會啟用，不會意外對外暴露 |
| **Vercel AI Gateway／Vercel Sandbox 回歸** | 若企業已完全遷移離開 Vercel 生態系，此變更不影響現況，純屬新增選項 |

#### 11.1.14 v0.20.1 – v0.20.6 補丁串升級注意事項

2026 年 8 月中下旬，官方在 v0.20.0 與 v0.21.0 之間密集發布 6 個 patch 版本（8/13、8/16、8/17、8/18、8/21、8/27），合計約 1,900 個 PR。**其中並非全是修正，數個實質新功能是在 patch 中悄悄導入的**——這打破了「patch 只修 bug」的一般預期，是本專案版本治理上企業需特別留意之處。

| 版本 | 需注意的實質變更 |
| ------ | ------ |
| v0.20.1 | 廣泛穩定化（1,444 commits / 656 PR / 2,172 檔案），無破壞性變更 |
| v0.20.2 | **多 Gateway Connections 註冊表**（單一 Desktop 可管理多個 Hermes 實例，多實例部署者建議檢視連線設定）；LiteLLM Claude on OpenAI wire 新增 Prompt Caching（成本曲線改變） |
| **v0.20.3** | ⚠️ **MCP 2.x 遷移**——本補丁串中**唯一具破壞性風險的變更**。自訂 MCP 伺服器或 Client 整合須驗證相容性。同時 **Bot Mode 以 bundled plugin 形式內建**（此時尚未預設開啟）；新增 CommandCode Provider |
| v0.20.4 | Desktop 側邊欄改為 `SESSIONS｜BOTS` 分頁（UI 習慣改變）；**Skill 安裝前安全掃描**（正面，但掃描可能擋下先前可安裝的 Skill）；Kanban 原生系統通知 |
| v0.20.5 | **Bot Mode 群組房間**；keyless web tier；**Cron 取得持久記憶與 per-job 推理強度**（既有排程任務行為改變，見 [6.6.5](#665-cron-記憶化與連續性v0210)） |
| v0.20.6 | **同意閘門式 Profile 瀏覽**（既有跨 Profile 存取流程需重新授權）；遠端 MCP 目錄擴至 50+ 伺服器；工具結果 TTL 快取；持久化事故確認台帳 |

> **企業實務建議**：若組織政策為「只升 Minor、跳過 patch」，本次應直接由 v0.20.0／v0.20.1 升至 v0.21.0，並將上表 v0.20.3 的 MCP 2.x 遷移與 v0.20.5 的 Cron 行為改變**一併納入驗收測試範圍**——這兩項變更會隨 v0.21.0 一起生效，容易被誤認為 v0.21.0 的新問題。

#### 11.1.15 v0.21.0 升級特別注意事項（**目前最新 Minor 版本**）

| 項目 | 說明 |
| ------ | ------ |
| ⚠️ **Bot Mode 預設開啟** | 這是本版**最需要主動決策**的項目：Bot Mode 為 bundled 且預設啟用，等同每個 Profile 自動成為具名 Agent 並可參與群組協作。企業若不需要，應於 **Settings → Plugins → Bots** 明確關閉（不影響底層 profiles 與資料）。詳見 [第十五章](#第十五章bot-mode-與多-agent-群組協作v0210) |
| ⚠️ **委派預設值大幅提高** | `delegate_task` 迭代上限提升至 **250**、並行子代理提升至 **10**。**成本上限同步放大一個量級**，升級前務必依預算調降並建立監控 |
| **MCP 2.x 遷移** | 於 v0.20.3 導入，跳過 patch 直升者於此版首次遭遇，自訂 MCP 整合須驗證 |
| **受保護指令檔生效** | `AGENTS.md`／skills／memory 的寫入改為一律需審批。**自動化流程若原本仰賴 Agent 自行寫入這些檔案，將開始卡在審批**，需改為 `/yolo`、調整審批規則或改由外部流程寫入 |
| **Windows 審批覆蓋擴大** | 先前可直接執行的部分 Windows 指令現在會觸發審批，Windows 上的無人值守自動化需重新驗證 |
| **macOS TCC 身分** | 升級後執行一次 `hermes desktop --setup-tcc-identity`，讓權限授予於日後更新中存續 |
| **Electron 回退至 40.10.2** | Desktop 底層版本**回退**（非升級），若有自製 Desktop Plugin 依賴較新 Electron API 需確認 |
| **已回退、不隨此版出貨的功能** | Model Council（`/council`）、DCP context engine、WS-only Gateway Server（FastAPI 仍在桌面啟動路徑上，但 seq-stamped 事件重放有出貨）、TCC interpreter anchor 移除。**若曾依早期 nightly 或社群討論規劃導入這些功能，需重新評估** |
| **6 個新 Provider** | Meta Model API（Muse Spark）／CommandCode／Actual Computer／Tencent TokenPlan／Nebius Token Factory／Ramp Router，屬新增選項，不影響既有設定 |
| **`model_overrides`** | 新增免改版覆寫機制，屬新增能力；但應納入設定變更審核（見 [1.4.41](#1441-model_overrides--免等改版的模型參數覆寫v0210)） |
| **真實 OS CI 車道** | 官方 CI 新增 macOS／Windows 真實主機測試，這對「Windows 上的行為與 Linux 不一致」類問題是結構性改善，Windows 使用者建議升級 |

> **Patch 版本（v0.18.1／v0.18.2／v0.19.1／v0.20.1–v0.20.6）升級提醒**：官方明確聲明部分 patch 版本**非精選版本**，Release Notes 不列逐項清單，僅作為「有一個可依附的穩定 tag」之用，完整內容會併入下一個 Minor 版本說明。企業如需掌握 patch 版本間的實際變更，建議直接比對 `git log <上一版>...<新版>` 或 GitHub Compare 頁面，而非僅信任 Release Notes 摘要。**v0.20.x 補丁串已證明 patch 中可能夾帶具破壞性的實質變更（MCP 2.x），此提醒的重要性高於一般專案。**

### 11.2 相容性管理

#### 11.2.1 版本相容性矩陣

| Hermes 版本 | Python | Node.js | LLM Provider API | MCP |
| ------------- | -------- | --------- | ------------------- | ----- |
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
| **v0.16.x** | **3.11+** | **22 LTS** | **OpenAI v1 + Responses** | **1.0 + OAuth 2.1 + SSE + mTLS** |
| **v0.17.x** | **3.11+** | **22 LTS** | **OpenAI v1 + Responses** | **1.0 + OAuth 2.1 + SSE + mTLS** |
| **v0.18.x** | **3.11+** | **22 LTS** | **OpenAI v1 + Responses + Vertex OAuth2** | **1.0 + OAuth 2.1 + SSE + mTLS** |
| **v0.19.x** | **3.11+** | **22 LTS** | **同上** | **同上，新增 Sampling** |
| **v0.20.0 – v0.20.2** | **3.11+** | **26（硬性必要）** | **同上 + A2A JSON-RPC 1.0/SSE** | **1.x + OAuth 2.1 + SSE + mTLS** |
| **v0.20.3 – v0.20.6** | **3.11+** | **26（硬性必要）** | **同上** | ⚠️ **2.x（遷移，見 11.1.14）** |
| **v0.21.x（最新）** | **3.11+** | **26（硬性必要）** | **同上，另加 6 個新 Provider 與 pip entry-point 可插拔 Provider** | **2.x + OAuth 2.1 + SSE + mTLS** |

> `hermes-agent-self-evolution` 等衍生研究專案要求 **Python 3.11–3.13**，與主專案的 3.11+ 相容，但不建議在同一虛擬環境混用生產與研究工具鏈。
>
> ⚠️ **MCP 版本斷點在 v0.20.3**：這是本矩陣中最容易被忽略的相容性邊界——它落在一個 patch 版本上，而非 Minor 版本邊界。自建 MCP 伺服器的企業應以此為升級驗證的分界點。

#### 11.2.2 Provider 相容性

| Provider | 支援版本 | 備註 |
| ---------- | ---------- | ------ |
| Anthropic | Claude 3+ | Thinking block signature 管理 |
| OpenAI | GPT-4+ | 自動修正工具呼叫參數類型 |
| OpenRouter | 全部 | 200+ 模型，aggregator-aware routing |
| Google AI Studio | Gemini 2+ | v0.8.0 新增原生支援，models.dev 自動偵測 |
| Nous Portal | 全部 | 免費 mimo-v2-pro 可用 |
| Ollama | 全部 | 本地模型，支援 Cloud auth |
| z.ai/GLM | 全部 | 端點自動偵測與快取 |
| MiniMax | 全部 | context length 修正、MiniMax TTS Speech 2.8 |
| xAI (Grok) | 全部 | prompt caching 支援、SuperGrok OAuth（v0.14.0）、1M context window |
| Qwen Cloud（原 Alibaba Cloud） | 全部 | OAuth Provider 支援、Portal request |
| Kimi/Moonshot | 全部 | OpenAI 相容端點 |
| **NovitaAI** | **全部** | **v0.14.0 新增 Provider** |
| **OpenAI API** | **全部** | **v0.15.0 獨立 Provider**（不再與 Codex 共用） |
| **Google Vertex AI** | **全部** | **v0.18.0 新增**，Service Account／ADC 自動換發短期 Token，免靜態金鑰 |
| **Fireworks AI** | **全部** | **v0.19.0 新增**，Provider 選擇器第二順位，附成本估算 |
| **DeepInfra / Upstage Solar** | **全部** | **v0.19.0 新增**（Upstage Solar 為社群貢獻整併） |
| **GitHub Copilot** | **全部** | 現為獨立 Provider（`copilot`／`copilot-acp`），可用既有 GitHub Copilot 訂閱存取 GPT-5.x／Claude／Gemini |
| **AWS Bedrock** | **全部** | 標準 AWS 憑證鏈（boto3），免 API Key |
| **Actual Computer** | **全部** | 自有硬體作為私有推論叢集，本地迴路免金鑰 |

> **提醒**：`alibaba` Provider 已更名 Qwen Cloud 的品牌識別，但設定鍵仍為 `alibaba` / `alibaba-coding-plan`，屬品牌更名非技術性變更。

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
| ------ | ------ | ------ |
| SOUL.md | `~/.openclaw/SOUL.md` | `~/.hermes/SOUL.md` |
| Memories | MEMORY.md + USER.md | `~/.hermes/memories/` |
| Skills | 使用者技能 | `~/.hermes/skills/openclaw-imports/` |
| 指令白名單 | approval patterns | `~/.hermes/config.yaml` |
| 訊息設定 | platform configs | `~/.hermes/config.yaml` |
| API Keys | Telegram / OpenRouter / OpenAI 等 | `~/.hermes/.env` |
| TTS 資源 | workspace audio | `~/.hermes/assets/` |
| AGENTS.md | workspace 指令 | 專案目錄 |

#### 11.3.2 從 Claude Code／Codex CLI 移轉（v0.20.0+）

v0.20.0 新增 `hermes import-agent`，可將既有 Claude Code 或 OpenAI Codex CLI 設定一鍵匯入：

```bash
# 預覽將匯入的內容（不執行）
hermes import-agent claude-code --dry-run
hermes import-agent codex --dry-run

# 正式匯入，若有既有設定衝突可加 --overwrite
hermes import-agent claude-code --overwrite
```

> 此功能定位為「輔助團隊漸進式評估／併行使用 Hermes」，而非強迫二選一遷移——見 9.7.3 節，兩者在程式碼工程深度（LSP／AST 整合）與跨平台通訊廣度上各有優勢，企業可視工作負載併存。

#### 11.3.3 版本間 Migration

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

#### 12.1 場景描述

團隊需要一個 AI Coding Agent 來輔助日常開發工作，包括程式碼撰寫、審查、測試和文件產出。

#### 12.1 架構設計

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

#### 12.1 設定檔

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

#### 12.1 使用範例

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

#### 12.2 場景描述

為銀行建立智慧客服系統，Agent 能理解客戶問題、查詢知識庫、處理常見業務。

#### 12.2 架構設計

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

#### 12.2 SOUL.md 設定

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

#### 12.2 客服知識庫 Skill

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

#### 12.3 場景描述

自動化銀行內部 IT 作業流程，包括定時報表、系統監控、變更管理。

#### 12.3 架構設計

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

#### 12.3 Cron 排程設定

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

#### 12.3 自動化報表範例輸出

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

#### 12.4 場景描述

結合 v0.12.0 新增的 ComfyUI v5、Spotify 整合和 TouchDesigner-MCP，建立多媒體內容創作 Agent。

#### 12.4 架構設計

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

#### 12.4 設定檔

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

#### 12.4 使用範例

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
| ------ | ------ | ------ |
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
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 方式 2：Native Windows（v0.16.0+ 正式支援）
irm https://hermes-agent.nousresearch.com/install.ps1 | iex
# 或安裝 Desktop App（官網下載 NSIS installer）
# 企業環境可選擇 WSL2 以獲得完整 Linux 工具鏈
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

### Q19：原本用 `brew install hermes-agent` 或 `pip install hermes-agent` 安裝，現在升級失敗怎麼辦？（v0.20.0）

這兩個管道已於 v0.20.0 正式停用（官方明確標示「PR 將被拒絕」），不會再收到任何更新。**解法**：改用官方目前支援的三種管道之一重新安裝——Shell Installer（`curl ... | bash`）、Docker，或 Nix Flake（詳見 4.2.3 節）。既有的 `~/.hermes/` 資料目錄（Skills、Memories、設定）不受影響，可直接沿用。

### Q20：升級後危險指令不再每次都問我，是不是有安全問題？（v0.19.0）

這是 v0.19.0 引入的**智慧審批（Smart Approvals）預設化**：一個獨立的 LLM 審查者會依情境自動判斷是否放行，取代逐次詢問。並非安全性降低，而是判斷者從「使用者」變成「LLM」。若企業合規要求所有危險指令都必須由人工確認，可將 `security.command_approval` 設回 `always`（見 9.1.2 節）。

### Q21：什麼時候該用 A2A，什麼時候該用 Kanban 或 delegate_task？（v0.20.0）

三者定位不同：**A2A**（1.4.29 節）用於與**組織外部、非 Hermes 架構**的其他 Agent 互通（如合作夥伴自建的 Agent 系統）；**Multi-agent Kanban**（6.3 節）用於**組織內部、需要持久記憶與稽核軌跡**的多 Agent 協作；**`delegate_task`**（6.2 節）用於**單次、階層式、不需要持久化**的平行子任務。三者可並存，非互斥選擇。

> 📌 **v0.21.0 更新**：現已增為**五種**機制（另加 Bot Mode 群組與 `hermes peer`），完整的四維度選型對照表與決策樹請見 [15.5 節](#155-五種多-agent-機制選型對照)。

### Q22：官方說「Hermes 完全免費」，為什麼還有月費方案？

兩者不衝突。**Hermes Agent 軟體本體**（本文所述的 Agent、Gateway、Skills、Memory 等所有核心功能）100% 免費、MIT 授權、可無限自架，這點官方 FAQ 明確保證「無訂閱、無席次費、無功能鎖付費牆」。月費方案（Free／Plus／Super／Ultra）屬於**選用的 Nous Portal 代管服務**——付費本質是購買「300+ 模型與 Web Search／圖片生成等 Tool Gateway 的隨插即用額度」，用戶仍可完全略過 Nous Portal，改用自己的 Anthropic／OpenAI／OpenRouter 等 API Key 或本地 Ollama 模型，此時成本為零（詳見 9.7.4 節 TCO 分析）。

### Q23：升級 v0.21.0 後多出一堆「bot」，這是什麼？有風險嗎？怎麼關掉？（v0.21.0）

那是 **Bot Mode**——你既有的每個 Profile 自動成為一個具名 Agent（含名稱與頭像），並可參與群組聊天。它是 bundled plugin 且**預設開啟**。

**風險層面需分開看**：

- ✅ **不會**改變既有 Profile 的資料、Skills 或記憶
- ⚠️ **會**放大成本：群組房間最多 6 bot × 3 輪 = 單次討論最多 18 次模型呼叫
- ⚠️ **會**新增一條協作路徑（`agent.bot_mode_protocol` 預設 `true`），若同時設定了 `hermes peer`，需確認 `API_SERVER_KEY` 強度與網路暴露面

**關閉方式**：`Desktop → Settings → Plugins → Bots`，或於 `config.yaml` 設 `agent.bot_mode_protocol: false`。關閉不影響底層 profiles 與資料。完整說明見 [第十五章](#第十五章bot-mode-與多-agent-群組協作v0210)。

### Q24：`hermes egress`（iron-proxy）和 `hermes proxy` 有什麼不同？

**方向完全相反，別搞混**：

- **`hermes proxy`**（1.4.13 節）是**入站**的 OpenAI 相容聚合器——讓 Aider、Cline、Cursor 等第三方工具共用你的 Hermes 訂閱
- **`hermes egress`**（9.8 節）是**出站**的憑證注入代理——讓 Docker 沙箱中的 Agent **拿不到真實 API 金鑰**，只拿到代理權杖，真實憑證由 host 端 daemon 在傳輸途中換入

若你的目標是「防止被提示注入的 Agent 外洩金鑰」，要的是 `hermes egress`。但務必先確認其限制：**僅支援 Docker backend**，且 AWS SigV4／GCP service-account OAuth 這類簽章式認證會完全繞過它。

### Q25：`/loop`、`/goal`、Cron 三個看起來都是「重複執行」，該用哪個？

一句話：**`/loop` 是時間驅動、`/goal` 是判定驅動、Cron 是排程驅動且脫離 Session**。

- 想「每 5 分鐘看一次 CI 跑完了沒」→ `/loop`
- 想「一直改到測試全過為止」→ `/goal`（搭配完成契約）
- 想「每天早上 9 點產出安全報告，不管我有沒有開著終端機」→ Cron

完整四維度對照表見 [3.11.1 節](#3111-三者選型對照)。另提醒：`/loop` 的 `max_ticks`（預設 100）是防止 Token 失控的最後防線，企業環境不建議調高。

### Q26：v0.21.0 把委派併發預設值調高了，成本會失控嗎？

會，如果不管它的話。預設值由既有值提高到 **250 iterations／10 個並行子代理**——**成本上限放大約一個量級**。

建議的三道防線：

1. **降低預設值**：依實際預算在 `config.yaml` 中調回合理範圍
2. **啟用成本監控**：v0.21.0 起 `delegate_task` 支援逐次委派的成本追蹤，搭配 `/usage`、`hermes insights` 定期檢視
3. **搭配免費／低價輔助模型**：見 9.2.2 節的成本控制設定

另外別忽略反方向的好消息：v0.21.0 的 Cron **monitor 模式雜湊抑制**（[6.6.5](#665-cron-記憶化與連續性v0210)）在無變化時直接跳過 LLM 呼叫，對長期監控類任務是顯著的成本下降。

### Q27：Managed Scope 可以當作正式的權限控管邊界嗎？

**不行。** 這點官方文件自己就寫得很清楚，企業評估時千萬別誤判：

- 它的執行機制**就只是檔案系統權限**（root 擁有的 `/etc/hermes/`），沒有簽章、沒有完整性驗證
- Managed `.env` 是**全域可讀**（`0644`），**絕對不能放敏感 Secret**——同機器上任何使用者都讀得到
- Agent 仍可在自己的子行程中覆寫被釘選的環境變數

正確定位是「**組織預設值的散佈機制**」——讓新機器開箱即有正確基準設定。若需要真正不可繞過的強制，須搭配 OS 層級 MDM／端點管控，以及 [9.8 節 iron-proxy](#98-egress-憑證注入代理iron-proxy-沙箱零信任外連) 等外部機制。詳見 [4.8.3 節](#483-v1-版本的限制不可作為權限控管邊界)。

### Q28：Tool Search 值得開嗎？什麼情況下反而變慢？

**值得開的情況**：掛了 10 個以上 MCP 伺服器或大量 Plugin 工具，且工具使用分散——此時工具 Schema 佔用的 context 相當可觀，而且是**每一輪都要重複付費**。

**反而變慢／變貴的情況**：

- 工具數量少（< 10），省下的 context 不值得多一次 round trip
- 工具使用**高度集中**（每輪都在用同幾個）——延遲載入的 Schema **無法受益於 System Prompt 快取**，反而比直接放在系統提示中更貴
- 使用較小的模型——Tool Search 依賴模型自行組織查詢字串找出正確工具，小模型可能找不到

設定與完整取捨分析見 [3.5.4 節](#354-tool-search延遲式工具-schema-載入)。

---

## 第十四章：Hermes Desktop App（v0.16.0+，v0.20.0 起成為完整平台）

v0.16.0（The Surface Release）推出的 **Hermes Desktop App** 是 Hermes Agent 的原生桌面圖形介面，基於 Electron 建構。官方定位為「與 CLI／Gateway 完全相同的 Agent——相同設定、相同 API Key、相同 Session、相同 Skills、相同記憶」，並非另一套獨立產品。v0.18.0～v0.20.0 三個版本大幅擴充其能力，v0.20.0「The Herald Release」更使其正式從「圖形化用戶端」升級為「可擴充的平台」（見 1.4.32 節）。

### 14.1 架構概覽

```mermaid
graph TB
    subgraph "Hermes Desktop App"
        ELEC[Electron Shell]
        RENDER[React Renderer<br/>主對話視窗]
        CMD[Command Palette<br/>Cmd+K / Ctrl+K]
        MODEL[Model Selector<br/>Fuzzy Picker]
        PROFILE[Profile Manager<br/>多 Session 併行]
        NOTIFY[OS Notifications<br/>原生通知]
        ART[Artifacts<br/>版本化卡片沙箱預覽]
        SDK[Plugin SDK<br/>Kanban 為首個參考外掛]
        PROJ[Projects<br/>Project → Repo → Lane]
        MGRAPH[Memory Graph<br/>放射狀時間軸]
        QE[Quick Entry<br/>全域熱鍵速記]
        HUD[HUD Mode<br/>無邊框浮動視窗]
    end
    
    subgraph "Backend Connection"
        LOCAL[本地 Agent Process]
        REMOTE[遠端 Gateway<br/>OAuth / 密碼認證]
        CLOUD[Hermes Cloud<br/>Preview 階段]
        SSH_B[SSH 遠端後端<br/>v0.20.0]
    end
    
    ELEC --> RENDER
    RENDER --> CMD
    RENDER --> MODEL
    RENDER --> PROFILE
    RENDER --> NOTIFY
    RENDER --> ART
    RENDER --> SDK
    RENDER --> PROJ
    RENDER --> MGRAPH
    RENDER --> QE
    RENDER --> HUD
    RENDER --> LOCAL
    RENDER --> REMOTE
    RENDER --> CLOUD
    RENDER --> SSH_B
```

### 14.2 安裝方式

| 平台 | 安裝方式 | 說明 |
| ------ | ---------- | ------ |
| macOS | 官網下載安裝程式或 `curl` 腳本 | **僅支援 Apple Silicon，macOS 12+**（Intel 不支援，見 4.1.1 節平台層級表） |
| Linux | 官網下載安裝程式或 `curl` 腳本 | 支援 X11 / Wayland |
| Windows | NSIS installer（官網下載） | Windows 10/11 64-bit |
| 已安裝 CLI 者 | `hermes desktop` 或 `hermes gui` | 免另外下載，直接由既有 CLI 安裝喚出桌面應用 |

> ⚠️ Homebrew 安裝（`brew install --cask hermes-desktop`）已隨 v0.20.0 一併停用，見 4.2.3 節。應用內具**自動更新**機制，無需手動重新下載安裝程式。

### 14.3 核心功能

#### 14.3.1 命令面板（Command Palette）

`Cmd+K`（macOS）或 `Ctrl+K`（Windows/Linux）開啟：
- 執行 Slash Commands（`/goal`、`/fast`、`/undo`、`/learn`、`/subscription` 等）
- 切換模型（Fuzzy 搜尋，每小時自動刷新目錄）
- 切換 Profile
- 安裝 Skills
- 管理 MCP Servers
- 執行 Plugin 貢獻的自訂指令（v0.20.0 Plugin SDK）

#### 14.3.2 多 Profile 併行 Session

- 同時開啟多個 Profile 對話視窗（多分頁／多視窗）
- 每個 Session 獨立模型、記憶、工具集
- **跨 Profile `@session` 連結**：可在不同 Profile 的對話間互相參照
- **每 Profile 匯出／匯入**：`.tar.gz` 封裝單一 Profile 的完整狀態，便於團隊間交接或備份
- 視窗間可拖放檔案傳遞上下文

#### 14.3.3 拖放與剪貼簿

- **拖放檔案**：直接將檔案拖入對話視窗作為上下文
- **剪貼簿圖片**：`Cmd/Ctrl+V` 貼入螢幕截圖，自動送入 Vision 分析
- **多檔案附加**：一次拖入多個檔案
- **右側預覽面板**：附件與生成內容獨立面板呈現，不佔用主對話串版面

#### 14.3.4 遠端連線（本地 / 遠端 Gateway / Hermes Cloud / SSH）

```yaml
# Desktop App 設定（Settings → Connections）
remote_gateway:
  url: "https://hermes-gateway.company.internal"
  auth: oauth2        # 信任網路／Tailscale 可用 password，公開網路建議 oauth2
  auto_reconnect: true
```

Desktop App 的「Connections」登錄可管理四種後端連線模式：
- **本地執行環境**：Agent Process 直接在本機運行
- **遠端 Gateway**：透過使用者名稱／密碼（信任網路、Tailscale 等場景）或 OAuth（公開網路、Nous Portal）連至團隊共享 Gateway，自動重連、Session 狀態本地與遠端同步
- **Hermes Cloud**（**目前為 Preview 階段，無正式 SLA**）：Nous Portal 內的代管執行個體
- **SSH 遠端後端**（v0.20.0 新增）：直接透過 SSH 連至遠端機器上運行的 `hermes serve`

> 登入採 **RFC 8252 原生桌面登入**（v0.20.0）：改用系統瀏覽器 + PKCE 完成 OAuth，不再透過內嵌 WebView 儲存 Cookie，降低憑證外洩風險。

#### 14.3.5 開發工具整合

- **內建終端機**：側邊欄提供具持久狀態的真實終端機
- **Git 整合**：分支切換、Diff 檢視、暫存／提交、AI 產生的 Commit 訊息建議面板
- **Git Worktree 管理**：圖形化管理多個並行的 Git worktree
- **檔案瀏覽器**：專案檔案樹狀瀏覽

#### 14.3.6 Artifacts（v0.20.0）

大型 HTML 全文件、SVG（≥2,000 字元）或程式碼區塊（≥48 行／3,000 字元）自動從對話串抽離為右側欄的**版本化卡片**：
- 版本切換（`‹ v2 of 3 ›`）、原始碼／預覽切換、下載、瀏覽器開啟
- HTML 於 `<iframe sandbox="allow-scripts">` 沙箱執行（不可同源存取、不可跳出導覽、不可彈窗），SVG 經 DOMPurify 淨化
- 一般散文、終端機輸出、Markdown／Mermaid 區塊與小型程式碼片段**不會**觸發自動升級

#### 14.3.7 Plugin SDK（v0.20.0）

見 1.4.32 節技術細節；Kanban 功能已完全重寫為此 SDK 的首個參考外掛（預設關閉），第三方可透過 `ctx.rest`／`ctx.storage`／`ctx.i18n`／`ctx.onDispose` 等擴充點開發原生等級的 Desktop 擴充功能，包含自訂頁面、狀態列項目、命令面板指令與可重綁快捷鍵。

#### 14.3.8 Projects（v0.18.0）

`project → repo → lane` 三層模型：側邊欄以「專案」組織多個程式碼庫，每個專案下可見多條並行的「工作道（lane）」，搭配 Coding Rail 與 Review Pane，用於同時管理多個並行的開發任務。

#### 14.3.9 Memory Graph（v0.18.0）

可互動、可拖拽探索的放射狀時間軸，視覺化呈現已累積的記憶與技能學習歷程，與 CLI／TUI 的 `/journey` 指令呈現同一份資料的不同檢視方式。

#### 14.3.10 Quick Entry 與 HUD Mode（v0.20.0 / v0.17.0+）

- **Quick Entry**：全域快捷鍵（`Ctrl/Cmd+Shift+Space`）可在作業系統任何位置喚出速記視窗，將靈感直接記錄進任一 Session，無需切換到 Hermes 主視窗
- **HUD Mode**：`Ctrl/Cmd+Shift+H` 切換為無邊框、置頂的浮動疊加視窗，適合搭配其他應用程式同時使用

#### 14.3.11 Bot Mode 桌面體驗（v0.21.0）

v0.21.0 讓 Desktop 從「單一對話視窗」轉變為「多 Agent 工作台」：

- **歸屬式 Agent 間訊息卡**：群組聊天中每則訊息明確標示發話 bot，並附送出端的投遞通知，可清楚追溯是誰對誰說了什麼
- **Paint-first hydration**：先繪製介面再載入資料，切換群組房間時不再空白閃爍
- **可編輯群組名稱與圖片**：群組如同 Discord 頻道般可自訂識別
- **Routines 面板**：bot 的排程任務（Cron／Blueprint）集中呈現，任務名稱以 `[bot:<name>] …` 標示
- **側邊欄 `SESSIONS｜BOTS` 分頁**（v0.20.4）：一般對話與 bot 名冊分流

完整概念與 CLI 對應見 [第十五章](#第十五章bot-mode-與多-agent-群組協作v0210)。

#### 14.3.12 應用內瀏覽器與 MCP Command Center（v0.21.0）

- **Agent 驅動的應用內瀏覽器**：Agent 可自行導航、點擊、讀取頁面；使用者可將頁面彈出至系統瀏覽器，並具備完整的連結右鍵選單。與無頭的 `browser` 工具集互補——這一個是**人機共視**的
- **MCP Command Center**：MCP 伺服器與目錄整併為單一頁面，支援拖放匯入設定、背景健康檢查、跨所有伺服器的 fleet 成本／用量疊層，以及 `hermes://` deep link 一鍵安裝流程

#### 14.3.13 更新與診斷體驗（v0.21.0）

- **Detached update hand-off**：各作業系統統一改用單一 shim 視窗接手更新流程，**修正 Windows 長期卡在「Updating」畫面的問題**
- **Send Diagnostics**：錯誤卡片可直接上傳已去識別化的除錯包，並附支援交接資訊
- **Seq-stamped 事件重放**：WebSocket 斷線重連時以序號比對補齊事件，不再遺漏訊息

#### 14.3.14 其他體驗優化（v0.21.0）

- HUD 貼齊游標位置（`⌘⇧G`）
- 免聚焦即可貼上內容至輸入框
- 每輪回應顯示耗時徽章
- macOS 半透明效果改善可讀性
- **Linux 啟動器項目與 keychain 自動偵測**（Linux 桌面整合度提升）
- 側邊欄直接呈現 cron／blueprint recipes
- Desktop 巨型檔案拆解為原子模組（維護性改善，對使用者無直接可見變化）

#### 14.3.15 累積功能一覽（依版本）

| 功能 | 版本 | 說明 |
| ------ | ------ | ------ |
| 可重綁快捷鍵 | v0.17.0 | 自訂所有鍵盤快捷鍵 |
| Subagent Watch-windows | v0.17.0 | 即時觀察背景子代理進度 |
| RTL/Bidi 自動偵測 | v0.17.0 | 支援阿拉伯語、希伯來語等右到左文字 |
| VS Code 主題安裝 | v0.17.0 | 匯入 VS Code 色彩主題 |
| Per-thread Drafts | v0.17.0 | 每個對話串獨立草稿暫存 |
| Projects | v0.18.0 | project → repo → lane 三層專案管理模型 |
| Memory Graph | v0.18.0 | 可互動記憶／技能學習時間軸 |
| ~20 項效能優化 | v0.19.0 | 串流 Markdown 解析器 CPU 降 14 倍、Diff 虛擬化、大型逐字稿快速切換 |
| 訂閱管理分頁 | v0.19.0 | 對應 CLI `/subscription`／`/topup` 的圖形化介面 |
| Artifacts | v0.20.0 | 版本化卡片、沙箱預覽 |
| Plugin SDK | v0.20.0 | Kanban 為首個參考外掛 |
| Quick Entry | v0.20.0 | 全域熱鍵速記視窗 |
| SSH 遠端後端 | v0.20.0 | 直連遠端 `hermes serve` |
| RFC 8252 原生登入 | v0.20.0 | 系統瀏覽器 + PKCE，免內嵌 WebView |
| 多 Gateway Connections 註冊表 | v0.20.2 | 單一 Desktop 管理多個 Hermes 實例 |
| Glass／Translucency 介面 | v0.20.4 | 半透明視覺層 |
| `SESSIONS｜BOTS` 分頁側邊欄 | v0.20.4 | 對話與 bot 名冊分流 |
| **Bot Mode（預設開啟）** | **v0.21.0** | **具名 Agent 名冊、群組聊天、Routines 面板** |
| **應用內瀏覽器（Agent 可操作）** | **v0.21.0** | **導航／點擊／讀取，可彈出至系統瀏覽器** |
| **MCP Command Center** | **v0.21.0** | **拖放匯入、健康檢查、fleet 成本疊層、`hermes://` deep link** |
| Detached update hand-off | v0.21.0 | 修正 Windows 卡在「Updating」 |
| Send Diagnostics | v0.21.0 | 上傳去識別化除錯包 |
| Seq-stamped 事件重放 | v0.21.0 | WebSocket 重連無損補齊 |
| Linux 啟動器與 keychain 偵測 | v0.21.0 | Linux 桌面整合度提升 |

### 14.4 解除安裝

Settings → About → Danger Zone 提供三種層級：僅移除 GUI、移除 GUI + Agent、完整移除（含 `~/.hermes/` 資料）。CLI 對應指令：`hermes uninstall [--full] [--gui] [--dry-run]`。

### 14.5 企業部署建議

| 場景 | 建議配置 |
| ------ | ---------- |
| 開發團隊 | 本地安裝 + 連至共享 Gateway，善用 Projects 管理多程式碼庫 |
| 非技術用戶（PM/QA） | 僅安裝 Desktop App，連至團隊 Gateway |
| 遠端工作 | Desktop App + VPN／Tailscale 或 OAuth 認證 |
| CI/CD 整合 | 伺服器端使用 CLI，開發者使用 Desktop App |
| 需要遠端終端機存取但不信任裝置本機環境 | v0.20.0 SSH 遠端後端，Agent 實際執行於受控伺服器 |

> **企業建議**：Desktop App 適合作為團隊的統一入口點，搭配集中式 Gateway 可確保所有對話紀錄、技能和記憶由組織統一管理，同時降低個人裝置的設定負擔。若考慮採用 Hermes Cloud 作為代管後端，須留意其目前仍為 **Preview 階段、無正式 SLA**（見 9.7.5 節），正式生產環境建議優先採用自架 Gateway。

---

## 第十五章：Bot Mode 與多 Agent 群組協作（v0.21.0）

Bot Mode 是 v0.21.0「The Pantheon Release」的旗艦主題，也是 Hermes 自 Multi-agent Kanban 以來對多 Agent 協作最大幅度的一次重新定位。本章完整說明其概念、操作、與既有四種多 Agent 機制的選型關係，以及企業導入的治理考量。

### 15.1 概念定位：bot 即 profile

Bot Mode **不是一個平行的新概念**——它是把既有的 Profile 系統「人格化、可視化」的一層封裝。

| 面向 | 說明 |
| ------ | ------ |
| 底層儲存 | 仍是 `~/.hermes/profiles/<name>/`，與 [6.6.4 節](#664-profile-based-多團隊工作流) 的 Profile 完全同一份資產 |
| 一個 bot 擁有 | 專屬模型、記憶、Skills、工具集、SOUL.md 人格、頭像、名稱 |
| 既有 Profile | **自動成為 bot**，無需遷移或轉換 |
| 交付形式 | 隨 Desktop 以 bundled plugin 出貨（v0.20.3 內建、v0.21.0 預設開啟） |

換言之：**先前你為前端／後端／QA 建立的 Profile，升級後就直接是三個可以在同一個房間裡討論的具名 Agent。**

### 15.2 建立與設定 Bot

建立 bot 時可選擇的設定面向：

| 設定項 | 說明 |
| ------ | ------ |
| **從既有 Profile 複製（clone）** | 以既有設定為基礎快速衍生，不必從零配置 |
| **釘選模型** | 為此 bot 固定使用特定模型（例如安全審查 bot 固定用高推理強度模型） |
| **自訂 SOUL.md** | 定義該 bot 的人格與行為準則（見 [6.7 節](#67-soulmd-與-personality-系統)） |
| **選擇性啟用 Skills／Tools** | **最小權限原則的實踐點**——文件整理 bot 不需要 `execute_command` |

**頭像機制**（五種選擇）：

1. **依名稱決定的 blob face**（deterministic）——同名永遠產生同一張臉，團隊成員間視覺一致
2. 幾何圖形配色
3. 上傳圖片
4. AI 生成肖像
5. Pixel pet（與 Petdex 連動）

> 💡 **實務建議**：deterministic blob face 對企業最實用——不必人工指派頭像，同一個 bot 名稱在所有團隊成員的桌面上長得一模一樣，口頭溝通時「那個紫色的」就能對得上。

### 15.3 群組聊天機制

多個 bot 與人類共處一室協作，機制設計上刻意避免「所有 bot 同時搶話」的災難：

| 機制 | 規則 |
| ------ | ------ |
| **成員上限** | 單一群組最多 **6 個 bot** |
| **回應模式** | **序列回應**，最多 **3 輪** |
| **發言決策** | 每個 bot 依議題相關性**自行決定是否發言**，不強制每個都回 |
| **人類升級決策** | 使用者可 **@自己** 以將決策權收回人類手上 |
| **持久性** | 房間跨「連線至同一 Gateway 的多台桌面」持久存在；Gateway 斷線時本地仍可存續 |

**適用場景**：需要多個專業視角同時檢視同一問題的討論——例如把「架構師 bot」「資安 bot」「DBA bot」拉進同一個房間評估一份設計文件，各自從專業角度提出意見，再由人類收斂。

**不適用場景**：需要嚴格工作分派與進度追蹤的長期專案——那是 Kanban（[6.3 節](#63-multi-agent-kanban-實戰)）的領域。

### 15.4 `hermes peer` — 跨 Gateway Agent 直訊

當協作對象不在同一台機器上時，`hermes peer` 提供 **Hermes 對 Hermes 的第一方通道**，且**不需要 Desktop 介入**。

```bash
# 註冊對端 Gateway（需對方的 API_SERVER_KEY）
hermes peer add research-box \
  --url https://gw.research.internal:8080 \
  --key "$RESEARCH_API_SERVER_KEY"

# 送出一則訊息（支援標準輸入）
hermes peer dm research-box < findings.md

# 交付長時間任務，之後輪詢狀態
hermes peer run research-box
hermes peer status
```

**設計重點**：對話**不是短暫的 RPC**，而是持久落在雙方各自的正規 Bot Chat 中——**可回溯、可稽核**，這是它與一般 API 呼叫最大的差異。

#### 15.4.1 安全前提

| 項目 | 要求 |
| ------ | ------ |
| **`API_SERVER_KEY` 強度** | 這是 peer 註冊的唯一憑證，**必須足夠強**。弱金鑰等同對外開放 Agent 執行權 |
| **憑證存放位置** | 位於 `~/.hermes/.env`，須確保檔案權限為 `0600`（v0.13.0 起預設如此） |
| **網路可達性** | 跨 Gateway 需雙方直接可達。**不建議直接暴露於公網**——官方建議以 Tailscale 或 VPN 進行 NAT 穿透，將通道限縮在私有網路內 |
| **`agent.bot_mode_protocol`** | 預設 `true`，會將 bot 間通訊協定注入正規 Bot Chat。若不使用 peer 功能可關閉 |

### 15.5 五種多 Agent 機制選型對照

Hermes 目前提供五種讓多個 Agent 協作的機制，這是實務上最容易選錯的一組決策。以四個維度區分：

| 機制 | 跨組織？ | 持久看板／稽核軌跡 | 人類在迴圈 | 協定標準化 | 最適場景 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| **`delegate_task`**（[6.2](#62-多-agent-協作設計)） | ❌ 同一實例內 | ❌ 壓縮後即遺失 | ❌ 通常無人值守 | 內部機制 | 一次性平行子任務（掃描、平行探索） |
| **Multi-agent Kanban**（[6.3](#63-multi-agent-kanban-實戰)） | ❌ 同一實例／多 Profile | ✅ **完整 SQLite 稽核軌跡** | ✅ 看板可視、可介入 | 內部機制 | **跨會話的長期專案**，需工作分派與進度追蹤 |
| **Bot Mode 群組**（本章） | ❌ 同一 Gateway | ⚠️ 對話持久，非結構化任務追蹤 | ✅ **人類同room、可 @ 升級** | 內部機制 | **多專業視角的即時討論與決策** |
| **`hermes peer`**（[15.4](#154-hermes-peer--跨-gateway-agent-直訊)） | ⚠️ 跨機器，但仍限 Hermes | ✅ 落於各自 Bot Chat | ⚠️ 可事後檢視 | Hermes 專有 | **跨機器／跨團隊的 Hermes 實例互通** |
| **A2A v1.0**（[1.4.29](#1429-a2aagent-to-agent協定-v10v0200)） | ✅ **跨廠商** | ⚠️ 依實作 | ⚠️ 依實作 | ✅ **開放標準協定** | **與非 Hermes 的第三方 Agent 互通** |

**選型決策樹**：

```text
需要與「非 Hermes」的 Agent 互通？
├─ 是 → A2A v1.0（1.4.29）
└─ 否 → 協作對象在同一台機器上嗎？
        ├─ 否 → hermes peer（15.4）
        └─ 是 → 需要工作分派與進度追蹤嗎？
                ├─ 是 → Multi-agent Kanban（6.3）
                └─ 否 → 需要人類即時參與討論嗎？
                        ├─ 是 → Bot Mode 群組（15.3）
                        └─ 否 → delegate_task（6.2）
```

### 15.6 企業治理與關閉方式

**Bot Mode 預設開啟**是本版最需要主動決策的變更。若組織評估後不採用，關閉方式如下：

```text
Desktop → Settings → Plugins → Bots → 關閉
```

> ✅ 關閉 Bot Mode **不會影響底層 profiles 與其資料**——Profile 系統、既有 Skills 與記憶完全不受影響，僅是不再以「具名 bot 名冊 + 群組」的形式呈現。

```yaml
# ~/.hermes/config.yaml — CLI／Gateway 側的協定開關
agent:
  bot_mode_protocol: true   # 預設 true；設為 false 則不注入 bot 間通訊協定
```

**治理考量清單**：

| 考量 | 說明 |
| ------ | ------ |
| **成本放大** | 一個群組房間中最多 6 個 bot × 3 輪 = **單次討論最多 18 次模型呼叫**。應為群組指派較經濟的模型，或限制成員數 |
| **稽核歸屬** | 群組對話中每則訊息有明確的 bot 歸屬，但**跨 bot 的決策責任鏈**需組織自行定義——「三個 bot 都同意」不構成人類的審核 |
| **最小權限** | 善用「選擇性啟用 Skills／Tools」為每個 bot 配置最小必要權限，避免每個 bot 都是全能管理員 |
| **peer 對外暴露** | 若未使用 `hermes peer`，建議不設定 peer 且確保 `API_SERVER_KEY` 未對外可達 |
| **與 Managed Scope 的關係** | 可透過 [4.8 節](#48-managed-scope組織層級設定釘選) 在 `/etc/hermes/config.yaml` 中釘選 `agent.bot_mode_protocol: false` 作為組織預設值——但請記得那**不是強制邊界** |

### 15.7 CLI 對應指令

Bot Mode 的每一項操作在終端機都有對應指令，無 Desktop 環境（如伺服器）同樣可用：

| 操作 | CLI 指令 |
| ------ | ------ |
| 與特定 bot 對話 | `hermes -p <bot> chat` |
| 建立／列出 bot（即 Profile） | `hermes profile create` ／ `hermes profile list` |
| 檢視 bot 的排程任務（Routines） | `hermes cron list`（顯示為 `[bot:<name>] …`） |
| 註冊對端 Gateway | `hermes peer add <name> --url <gateway> --key <API_KEY>` |
| 跨 Gateway 送訊息 | `hermes peer dm <target>` |
| 跨 Gateway 交付任務 | `hermes peer run <target>` |
| 查詢 peer 狀態 | `hermes peer status` |
| 匯出／匯入 bot 設定 | `/export [profile]` ／ `/import <archive.tar.gz>` |

---

## 附錄 A：檢查清單（Checklist）

### A.1 安裝檢查清單

- [ ] 確認作業系統落在 [Tier 1／Tier 2 支援層級](#411-平台支援層級platform-support-tiers)內（**macOS Intel 不支援**）
- [ ] 確認 Python 3.11+ 已安裝
- [ ] 確認 **Node.js 26+** 已安裝（**v0.20.0 起為硬性必要條件**，低於此版本無法啟動）
- [ ] 確認 Git 2.30+ 已安裝（安裝程式不會自動安裝）
- [ ] 確認未使用已停用的安裝管道（Homebrew／PyPI／pip／AUR）
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
- [ ] **（v0.21.0）** Docker 沙箱工作負載已評估啟用 [iron-proxy 憑證注入代理](#98-egress-憑證注入代理iron-proxy-沙箱零信任外連)，並維持 `enforce_on_docker: true`
- [ ] **（v0.21.0）** 已確認 iron-proxy 的限制不影響防護目標（僅 Docker backend；AWS SigV4／GCP OAuth 會繞過）
- [ ] **（v0.21.0）** 若使用 [Managed Scope](#48-managed-scope組織層級設定釘選)，已確認 `/etc/hermes/.env`（全域可讀）**未存放敏感 Secret**
- [ ] **（v0.21.0）** 已對 **Bot Mode 預設開啟**做出明確採用或關閉的決策
- [ ] **（v0.21.0）** 若使用 `hermes peer`，`API_SERVER_KEY` 強度足夠且通道限縮於 VPN／Tailscale 私網
- [ ] **（v0.21.0）** 受保護指令檔審批已納入既有自動化流程的相容性測試
- [ ] `model_overrides` 等免改版覆寫設定已納入版本控管與變更審核

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

> 本附錄依官方 `/docs/reference/cli-commands` 全面重整，依功能分類；篇幅所限僅列最常用旗標，完整旗標請執行 `hermes <指令> --help`。

### B.1 CLI 指令（依功能分類）

**全域旗標**：`hermes [--profile/-p <name>] [--resume/-r <session>] [--continue/-c] [--worktree/-w] [--yolo] [--tui|--cli] [--safe-mode] <指令>`

| 分類 | 指令 | 說明 |
| ------ | ------ | ------ |
| 對話 | `hermes` / `hermes chat` | 啟動互動式 CLI（`-q` 單次提問／`-m` 指定模型／`-t` 指定 Toolset／`--image` 附圖） |
| 對話 | `hermes -z "<task>"` | Non-interactive 單次模式（v0.12.0），可加 `--usage-file` 輸出用量報告 |
| 模型 | `hermes model` | 互動式 Fuzzy 選擇模型與 Provider |
| 模型 | `hermes moa list\|configure\|delete` | 管理 Mixture-of-Agents 預設組合（v0.18.0） |
| 模型 | `hermes fallback list\|add\|remove\|clear` | 管理 Fallback Provider 鏈 |
| 工具 | `hermes tools [--summary]` | 列出所有工具集與狀態 |
| 訊息平台 | `hermes send --to <target> "msg"` | 主動推送訊息至任一平台（v0.15.0） |
| 訊息平台 | `hermes gateway run\|start\|stop\|restart\|status\|list\|setup\|enroll` | Gateway 生命週期管理 |
| 訊息平台 | `hermes whatsapp` / `hermes whatsapp-cloud` | WhatsApp（Baileys／官方 Cloud API 雙軌）配對設定 |
| 訊息平台 | `hermes slack manifest [--write]` | 產生 Slack App Manifest |
| 設定 | `hermes setup [model\|--portal\|--quick\|--non-interactive\|--reset]` | 執行設定精靈 |
| 設定 | `hermes config show\|edit\|get\|set\|unset\|path\|check\|migrate` | 設定檔管理 |
| 設定 | `hermes auth list\|add\|remove\|status\|logout` | Provider 認證管理 |
| 技能 | `hermes skills browse\|search\|install\|inspect\|list\|check\|update\|uninstall` | 技能管理（見 3.2.3 節） |
| 技能 | `hermes bundles list\|show\|create\|delete` | Skill Bundle 管理 |
| 技能 | `hermes curator status\|run\|pause\|resume\|pin\|unpin` | 技能庫維護（v0.12.0 起，v0.13.0 擴充） |
| 技能 | `hermes plugins install\|search\|update\|remove\|enable\|disable\|list\|doctor` | Plugin 管理 |
| 憑證 | `hermes secrets bitwarden setup\|status\|token\|sync\|disable` | Bitwarden Secrets Manager（v0.15.0） |
| 憑證 | `hermes proxy start\|status\|providers` | `hermes proxy` 本地代理（v0.14.0） |
| 開發整合 | `hermes acp` | Agent Client Protocol（VS Code／Zed／JetBrains） |
| 開發整合 | `hermes mcp catalog\|install\|serve\|add\|remove\|list\|test` | MCP 伺服器管理 |
| 開發整合 | `hermes computer-use install\|status` | 桌面自動化後端安裝 |
| 開發整合 | `hermes lsp status\|list\|install\|install-all\|restart` | LSP 語言伺服器管理 |
| Session／專案 | `hermes sessions list\|browse\|export\|delete\|prune\|archive\|rename\|optimize` | Session 管理（`export` 支援 Markdown／Quarto／HTML／Hugging Face，v0.19.0） |
| Session／專案 | `hermes project create\|list\|show\|add-folder\|remove-folder\|rename\|bind-board` | Desktop Projects 對應之 CLI 操作（v0.18.0） |
| Kanban | `hermes kanban init\|boards\|create\|list\|show\|assign\|link\|complete\|dispatch` | Multi-agent Kanban（見 6.3.2 節） |
| 自動化 | `hermes cron list\|create\|edit\|pause\|resume\|run\|remove\|tick` | 排程任務管理 |
| 自動化 | `hermes webhook subscribe\|list\|remove\|test` | 入站 Webhook 管理 |
| 自動化 | `hermes hooks list\|test\|revoke\|doctor` | 出站 Webhook／Shell Hooks 管理（v0.20.0） |
| 診斷 | `hermes status [--all\|--deep]` | 查看 Agent 整體狀態 |
| 診斷 | `hermes doctor [--fix]` | 診斷環境問題並可自動修復 |
| 診斷 | `hermes logs [agent\|errors\|gateway\|gui\|desktop] [-f]` | 查看日誌 |
| 診斷 | `hermes security audit [--json] [--fail-on critical]` | OSV.dev 供應鏈安全稽核 |
| 診斷 | `hermes insights [--days N] [--source]` | 使用洞察報告 |
| 資料 | `hermes backup [-o] [--quick] [--label]` | 備份 `~/.hermes/` |
| 資料 | `hermes checkpoints status\|prune\|clear` | Checkpoint 管理 |
| 資料 | `hermes import <zip>` | 匯入備份 |
| 遷移 | `hermes claw migrate [--dry-run] [--preset full\|user-data]` | 從 OpenClaw 移轉（見 11.3.1 節） |
| 遷移 | `hermes import-agent claude-code\|codex [--dry-run] [--overwrite]` | 從 Claude Code／Codex CLI 匯入（v0.20.0，見 11.3.2 節） |
| 記憶 | `hermes memory setup\|status\|off` | 外部記憶 Provider 設定 |
| 記憶 | `hermes journey` / `hermes learning` / `hermes memory-graph` | 學習時間軸／記憶圖檢視 |
| 審批 | `hermes approvals` / `hermes approvals suggest` | 危險指令審批策略管理（`suggest` 為 v0.20.0 新增，依歷史提出白名單建議） |
| 審批 | `hermes pairing list\|approve\|revoke\|clear-pending` | DM Pairing 配對管理 |
| 系統 | `hermes egress install\|setup\|start\|stop\|status` | 出站憑證注入代理 iron-proxy（見 9.8 節）；`setup --rotate-tokens` 輪替代理權杖 |
| **多 Agent** | **`hermes peer add\|dm\|run\|status`** | **跨 Gateway Agent 直訊（v0.21.0，見 15.4 節）** |
| 審批 | `hermes approval-check` | 以 dry-run 測試審批規則的判決結果，不實際執行指令（v0.21.0） |
| 憑證 | `hermes secrets` | 外部秘密來源管理（Bitwarden／1Password `op://`／Command Helper，v0.19.0 起可插拔） |
| 模型 | `hermes migrate <provider>` | 針對已退役模型自動改寫設定（如 `hermes migrate xai`） |
| 設定 | `hermes portal` | Nous Portal OAuth 認證與 Tool Gateway 狀態（`hermes setup --portal` 為一鍵快速設定） |
| 診斷 | `hermes prompt-size` | 顯示 System Prompt 各組成的位元組佔比，用於排查 context 膨脹 |
| 診斷 | `hermes dump` | 產出可複製貼上的設定摘要，供技術支援使用 |
| 診斷 | `hermes debug` | 上傳已遮蔽的日誌與系統資訊並取得分享連結 |
| 介面 | `hermes desktop --setup-tcc-identity` | macOS 專用：以穩定簽章身分固定 TCC 權限，使授權跨更新存續（v0.21.0） |
| 介面 | `hermes pets` | 瀏覽與管理 Petdex 終端寵物（趣味功能） |
| 訊息平台 | `hermes photon login` | Photon Spectrum iMessage 裝置碼認證（v0.17.0，免 Mac relay） |
| 介面 | `hermes dashboard [--port 9119] [--stop] [--status]` | Web Dashboard 管理 |
| 介面 | `hermes gui` / `hermes desktop` | 啟動 Desktop App |
| 介面 | `hermes serve [--host] [--port]` | 啟動供 Desktop／遠端連線的 Agent 伺服器 |
| Profile | `hermes profile list\|use\|create\|delete\|show\|rename\|export\|import\|install\|update` | Profile 完整管理 |
| 維護 | `hermes version` / `hermes update [--check] [--backup] [--gateway]` | 版本檢視與升級 |
| 維護 | `hermes completion bash\|zsh\|fish` | Shell 自動完成腳本 |
| 維護 | `hermes uninstall [--full] [--gui] [--dry-run]` | 解除安裝（見 14.4 節） |

### B.2 對話中斜線指令

| 指令 | 說明 |
| ------ | ------ |
| `/new` 或 `/reset` | 開啟新對話（保留記憶） |
| `/model [provider:model]` | 切換模型 |
| `/compress` | 壓縮當前上下文 |
| `/usage` | 查看 Token 使用量 |
| `/insights [--days N]` | 查看使用洞察 |
| `/skills` | 列出可用技能 |
| `/<skill-name>` | 執行特定技能，支援堆疊 |
| `/personality [name]` | 設定人格 |
| `/retry` | 重試上一輪 |
| `/undo [N]` | 撤銷最近 N 輪對話（v0.16.0） |
| `/voice on/off` | 開關語音模式 |
| `/approve` | 批准待審指令 |
| `/deny [<原因>]` | 拒絕待審指令，v0.19.0 起可附理由讓 Agent 自我修正 |
| `/stop` | 中斷當前操作 |
| `/platforms` | 查看連線平台狀態 |
| `/status` | 查看 Agent 狀態 |
| `/busy [steer\|queue\|interrupt]` | 忙碗模式（v0.12.0） |
| `/btw` | 中插任務導引（v0.12.0） |
| `/background` | 移至背景執行（v0.12.0） |
| `/reload` | 熱重載 `.env`（v0.12.0） |
| `/reload-skills` | 重新載入技能庫（v0.12.0） |
| `/reload-mcp` | 重建 MCP cached agents（v0.12.0） |
| `/mouse` | 互動式滑鼠操作（v0.12.0） |
| `/fast` | 切換 Fast Mode |
| `/steer` | 中途導引 Agent 行為（v0.11.0） |
| `/goal` / `/goal draft\|show\|pause\|resume\|clear` / `/subgoal` | 持久化目標管理（Ralph Loop）（v0.13.0，v0.18.0 起支援完成契約） |
| `/kanban` | 顯示 Multi-agent Kanban 看板（v0.13.0） |
| `/queue` | 查看任務佇列（v0.13.0） |
| `/learn <對象>` | 萃取目錄／URL／操作為可重用 Skill（v0.18.0） |
| `/journey` | 檢視學習時間軸（v0.18.0） |
| `/subscription` / `/topup` | Nous Portal 訂閱管理（v0.19.0） |
| `/prompt` | 開啟 `$EDITOR` 撰寫長篇提示（v0.18.0） |
| `!<shell 指令>` | 免佔用模型輪次直接執行 Shell（v0.20.0） |
| `/init` | 掃描專案產生／更新 AGENTS.md（v0.20.0） |
| `/diff` | 顯示變更（v0.20.0） |
| `/context` | 檢視上下文視窗組成（v0.20.0） |
| `/focus` | 精簡輸出檢視（v0.20.0） |
| `/palette`（或 `Ctrl+P`） | 開啟模糊命令面板（v0.21.0） |
| `/loop [interval] <prompt> [--times N] [--until <cond>]` | 於當前 Session 內週期性重跑提示（見 3.11 節） |
| `/heartbeat every <interval> <prompt>`（`/hb`） | 閒置時的週期性提示 |
| `/egress [status]` | 檢視 Docker egress 代理狀態（見 9.8 節） |
| `/review [instructions]` | 派出獨立審查子代理檢視當前工作 |
| `/refine [focus]` | 執行記憶／技能改進檢視 |
| `/plan [task]` | 產出 Markdown 實作計畫 |
| `/suggestions [accept\|dismiss N\|catalog\|clear]`（`/suggest`） | 檢視自動化建議 |
| `/blueprint [name] [slot=value ...]`（`/bp`） | 以模板建立自動化（見 6.6.2 節） |
| `/snapshot`（`/snap`） | 建立／還原狀態快照 |
| `/rollback` | 列出或還原檔案系統 Checkpoint |
| `/branch [name]`（`/fork`） | 由當前 Session 分岔出新路徑 |
| `/worktree [new [name]\|list]` | 管理 Git worktree（CLI only） |
| `/handoff <platform>` | 即時轉移 Session 至其他平台／模型（v0.14.0，CLI only） |
| `/sessions` / `/switch` | 瀏覽並恢復先前 Session |
| `/resume [name]` | 回到指定名稱的 Session |
| `/title` / `/save` / `/history` / `/clear` | Session 命名／保存／歷史／清畫面 |
| `/agents` / `/tasks` | 顯示執行中的子代理與任務（v0.21.0 起可中途導引，見 6.2.1c） |
| `/bg <prompt>` | 於獨立背景 Session 執行提示 |
| `/tools [list\|disable\|enable]` / `/toolsets` | 工具與工具集管理 |
| `/browser [connect\|disconnect\|status]` | 管理 Chromium CDP 連線 |
| `/memory [pending\|approve\|reject\|approval]` | **檢視並審批記憶寫入（v0.21.0 受保護指令檔的操作入口）** |
| `/bundles` / `/plugins` / `/curator` | Skill Bundle／Plugin／Curator 管理 |
| `/config` / `/profile` / `/version` / `/whoami` | 設定、Profile、版本、權限層級檢視 |
| `/reasoning [level\|show\|hide\|full\|clamp] [--global]` | 推理強度與思考過程顯示控制 |
| `/approvals [manual\|smart\|off]` / `/yolo` | 審批模式切換（`/yolo` 略過所有危險指令確認） |
| `/verbose` / `/statusbar`（`/sb`） / `/footer` / `/timestamps` / `/battery` | 顯示層開關 |
| `/skin` / `/indicator [kaomoji\|emoji\|unicode\|ascii]` / `/redraw` | 主題、忙碌指示樣式、強制重繪（CLI only） |
| `/wake [on\|off\|status]` | 喚醒詞監聽開關（CLI only） |
| `/codex-runtime [auto\|codex_app_server\|on\|off]` | Codex App-Server Runtime 切換 |
| `/paste` / `/image <path>` / `/copy [number]` | 剪貼簿圖片、附加圖檔、複製回應（CLI only） |
| `/export [profile] [-o out.tar.gz]` / `/import <archive.tar.gz>` | Profile 打包匯出／匯入（CLI only） |
| `/pet [list\|<slug>]` / `/hatch <description>` | Petdex 終端寵物（趣味功能） |
| `/topic [off\|help\|session-id]` | 多 Session DM 模式（僅 Telegram） |
| `/platform <list\|pause\|resume> [name]` / `/sethome` / `/restart` | Gateway 平台操作（僅訊息平台） |
| `/debug` | 上傳除錯報告並取得分享連結 |
| `/update` | 升級 Hermes 至最新版本 |
| `/help` / `/quit`（`/exit`） | 說明與離開 |

---

## 附錄 C：環境變數參考

### C.1 模型 Provider 金鑰

| 環境變數 | 說明 | 必要性 |
| ---------- | ------ | -------- |
| `ANTHROPIC_API_KEY` | Anthropic API 金鑰（或改用 `hermes auth login anthropic` OAuth，Claude Max 訂閱可用） | 至少一個 Provider |
| `OPENAI_API_KEY` | OpenAI API 金鑰 | 至少一個 Provider |
| `OPENROUTER_API_KEY` | OpenRouter API 金鑰 | 至少一個 Provider |
| `GOOGLE_API_KEY` / `GEMINI_API_KEY` | Google AI Studio（Gemini）API 金鑰 | 選用 |
| `XAI_API_KEY` | xAI (Grok) API 金鑰（或 `hermes auth login xai` OAuth，需 SuperGrok／X Premium+） | 選用 |
| `NVIDIA_API_KEY` | NVIDIA NIM（build.nvidia.com）API 金鑰 | 選用 |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | AWS Bedrock 認證（標準 boto3 憑證鏈） | 選用 |
| `HF_TOKEN` | Hugging Face Inference API Token | 選用 |
| `GMI_API_KEY` | GMI Cloud API 金鑰 | 選用 |
| `DEEPSEEK_API_KEY` | DeepSeek API 金鑰 | 選用 |
| `DASHSCOPE_API_KEY` | Qwen Cloud（原 Alibaba Cloud）API 金鑰 | 選用 |
| `MISTRAL_API_KEY` | Mistral AI API 金鑰（Voxtral STT） | 選用 |
| `KIMI_API_KEY` / `KIMI_CN_API_KEY` | Moonshot 國際版／中國版 API 金鑰 | 選用 |
| `ARCEEAI_API_KEY` | Arcee AI（Trinity 系列）API 金鑰 | 選用 |
| `MINIMAX_API_KEY` / `MINIMAX_CN_API_KEY` | MiniMax 國際版／中國版 API 金鑰 | 選用 |
| `COPILOT_GITHUB_TOKEN` / `GH_TOKEN` | GitHub Copilot 訂閱認證（獨立 Provider） | 選用 |
| **`FIREWORKS_API_KEY`** | **Fireworks AI API 金鑰（v0.19.0 新增，Provider 選擇器第二順位）** | 選用 |
| **`NOVITA_API_KEY`** | NovitaAI API 金鑰（v0.14.0） | 選用 |
| **Vertex AI** | 無需靜態金鑰，改以 Service Account JSON 或 Application Default Credentials 自動換發（v0.18.0） | 選用 |
| `AI_GATEWAY_API_KEY` | Vercel AI Gateway API 金鑰（v0.15.0 曾移除，**v0.20.0 現代化重新引入**） | 選用 |
| `LM_STUDIO_URL` / `LM_API_KEY` | LM Studio 本地端點 | 選用 |
| `AZURE_AI_FOUNDRY_KEY` / `AZURE_AI_FOUNDRY_ENDPOINT` | Azure AI Foundry（Microsoft Entra ID auth，v0.15.0） | 選用 |
| `TENCENT_TOKENHUB_KEY` | 騰訊 Tokenhub API 金鑰 | 選用 |
| `KILOCODE_API_KEY` | Kilocode API 金鑰 | 選用 |
| `XIAOMI_API_KEY` | 小米 MiMo API 金鑰 | 選用 |
| `STEPFUN_API_KEY` | StepFun API 金鑰 | 選用 |
| `OLLAMA_API_KEY` | Ollama Cloud API 金鑰（本地 Ollama 免金鑰） | 選用 |
| `ACTUAL_API_KEY` | Actual Computer 私有推論叢集金鑰（本地迴路可免） | 選用 |

### C.2 訊息平台 Token

| 環境變數 | 說明 | 必要性 |
| ---------- | ------ | -------- |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token | Gateway 需要 |
| `DISCORD_BOT_TOKEN` | Discord Bot Token | Gateway 需要 |
| `DISCORD_ALLOWED_ROLES` | Discord Guild 角色白名單（v0.13.0 安全修正） | 選用 |
| `SLACK_BOT_TOKEN` | Slack Bot Token | Gateway 需要 |
| `GOOGLE_CHAT_WEBHOOK` | Google Chat Webhook URL | Gateway 需要 |
| `LINE_CHANNEL_ACCESS_TOKEN` | LINE Messaging API Token | Gateway 需要 |
| `SIMPLEX_CHAT_PORT` | SimpleX Chat 連接埠 | Gateway 需要 |
| `NTFY_TOPIC` | ntfy 推播主題 URL | Gateway 需要 |
| **`BUZZ_RELAY_URL`** | **Buzz（Nostr）中繼站設定（v0.20.0 新增，實際變數名稱以官方文件為準）** | Gateway 需要 |

### C.3 工具與整合

| 環境變數 | 說明 | 必要性 |
| ---------- | ------ | -------- |
| `GITHUB_TOKEN` | GitHub Token（MCP／各類 Git 整合用） | MCP 需要 |
| `DATABASE_URL` | PostgreSQL 連線字串（MCP 用） | MCP 需要 |
| `ELEVENLABS_API_KEY` | ElevenLabs TTS API 金鑰 | Voice 需要 |
| `MEM0_API_KEY` | Mem0 Cloud API 金鑰 | Mem0 記憶需要 |
| `SPOTIFY_CLIENT_ID` / `SPOTIFY_CLIENT_SECRET` | Spotify PKCE OAuth | Spotify 需要 |
| `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | Langfuse 可觀測性 | 選用 |
| `GOOGLE_MEET_CREDENTIALS` | Google Meet 憑證 | Meet 需要 |
| **`BWS_ACCESS_TOKEN`** | **Bitwarden Secrets Manager Machine Account Token（v0.15.0，v0.19.0 起與 1Password 並列可插拔 `SecretSource`）** | 選用 |
| **`OP_SERVICE_ACCOUNT_TOKEN`** | **1Password Service Account Token（`op://` 參照解析用，v0.19.0 新增）** | 選用 |
| **`HERMES_WEBHOOK_SECRET`** | **Outbound Webhook HMAC 簽章密鑰（v0.20.0，見 1.4.31 節）** | Webhook 需要 |

### C.4 系統與行為控制

| 環境變數 | 說明 | 必要性 |
| ---------- | ------ | -------- |
| `HERMES_HOME` | 自訂 Hermes 主目錄（預設 `~/.hermes`） | 選用 |
| `HERMES_PORTAL_BASE_URL` | 自訂 Nous Portal URL | 選用 |
| `HERMES_DASHBOARD` | 設為 `1` 啟動 Dashboard Side-process | 選用 |
| `HERMES_YOLO_MODE` | 等同 `--yolo` flag，跳過審批（硬性封鎖清單仍生效） | 選用，生產環境不建議 |
| `HERMES_WRITE_SAFE_ROOT` | 限制 `write_file`／`patch` 僅能寫入指定路徑前綴 | 建議生產環境設定 |
| `HERMES_ENABLE_PROJECT_PLUGINS` | 設為 `true` 才允許載入 `.hermes/plugins/` 專案層級 Plugin | 選用 |
| `HERMES_TENANT` | Kanban 多租戶模式的租戶識別 | 多租戶場景需要 |
| `HERMES_KANBAN_TASK` / `HERMES_KANBAN_BOARD` | Kanban Dispatcher 派生 Worker 時自動注入，無需手動設定 | 系統內部使用 |
| `HERMES_STREAM_READ_TIMEOUT` / `HERMES_API_TIMEOUT` | 串流／API 逾時設定（秒） | 選用 |
| **`HERMES_MANAGED_DIR`** | 覆寫 Managed Scope 的系統層設定目錄（預設 `/etc/hermes/`，見 [4.8 節](#48-managed-scope組織層級設定釘選)） | 機隊部署選用 |
| **`API_SERVER_KEY`** | API Server 與 `hermes peer` 註冊的認證金鑰。**強度不足等同對外開放 Agent 執行權**（見 [15.4.1 節](#1541-安全前提)） | 使用 API Server／peer 時必要 |

**Egress 憑證注入代理（iron-proxy）相關**：主要以 `config.yaml` 的 `proxy:` 區塊設定（見 [9.8.4 節](#984-完整設定鍵參考)）。沙箱側由 Hermes 自動注入代理位址、唯讀 CA 憑證掛載點與**代理權杖（非真實金鑰）**，一般情況下不需手動設定環境變數。

---

## 附錄 D：Provider 完整清單

截至 v0.20.1，Hermes Agent 官方文件（`/docs/integrations/providers`）列出 **40+ 雲端／自架 Provider**，均可透過 `/model <provider-id>:<model>` 語法直接指定，第三方亦可依 `ProviderProfile` ABC 開發自訂 Provider Plugin 掛載（`plugins/model-providers/`）。以下依官方 Provider ID 整理：

### D.1 雲端推理 Provider

| Provider ID | 名稱 | 認證方式 | 說明 |
| ------ | ------ | ------ | ------ |
| `nous` | Nous Portal | OAuth | 統一閘道，300+ 模型 + Tool Gateway |
| `openai-codex` | OpenAI Codex | OAuth 裝置碼 | ChatGPT 訂閱、Codex 系列模型 |
| `copilot` | GitHub Copilot | OAuth 或 `COPILOT_GITHUB_TOKEN` | 透過 Copilot API 存取 GPT-5.x／Claude／Gemini |
| `copilot-acp` | GitHub Copilot（本地 CLI） | 本地 Session | 派生本地 Copilot 子行程 |
| `anthropic`（別名 `claude`／`claude-code`） | Anthropic | OAuth（Claude Max）或 API Key | Thinking block signature 管理 |
| `openrouter` | OpenRouter | `OPENROUTER_API_KEY` | 200+ 模型聚合，aggregator-aware routing |
| `fireworks`（別名 `fireworks-ai`／`fw`） | Fireworks AI | `FIREWORKS_API_KEY` | **v0.19.0 新增**，選擇器第二順位，附成本估算 |
| `novita` | NovitaAI | `NOVITA_API_KEY` | 200+ 模型、Model API、Agent Sandbox、GPU Cloud（v0.14.0） |
| `ai-gateway` | Vercel AI Gateway | `AI_GATEWAY_API_KEY` | v0.15.0 移除，**v0.20.0 現代化重新引入** |
| `zai` | z.ai / GLM | `GLM_API_KEY` | 自動偵測全球／中國／Coding Plan 端點 |
| `kimi-coding` / `kimi-coding-cn` | Moonshot（國際／中國） | `KIMI_API_KEY` / `KIMI_CN_API_KEY` | 各自獨立端點與計費 |
| `arcee`（別名 `arcee-ai`） | Arcee AI | `ARCEEAI_API_KEY` | Trinity 系列企業微調模型 |
| `gmi` | GMI Cloud | `GMI_API_KEY` | GMI 雲端推理 |
| `actual`（別名 `actual-computer`） | Actual Computer | `ACTUAL_API_KEY` 或本地迴路免金鑰 | 自有硬體作為私有推論叢集 |
| `minimax` / `minimax-cn` | MiniMax（國際／中國） | `MINIMAX_API_KEY` / `MINIMAX_CN_API_KEY` | 獨立 SKU |
| `minimax-oauth` | MiniMax OAuth | 瀏覽器 PKCE | Anthropic Messages 相容端點 |
| `xai` | xAI（Grok） | `XAI_API_KEY` | Responses API，Grok 4 自動啟用推理 |
| `xai-oauth` | xAI OAuth | 瀏覽器 OAuth | 需 SuperGrok／X Premium+ 訂閱 |
| `alibaba` | Qwen Cloud（原 Alibaba Cloud） | `DASHSCOPE_API_KEY` | 品牌更名，設定鍵沿用 `alibaba` |
| `alibaba-coding-plan` | Qwen Coding Plan | 獨立端點 | 獨立計費 SKU |
| `qwen-oauth` | Qwen Portal | 瀏覽器 PKCE | 消費級 Qwen Portal |
| `kilocode` | Kilocode | `KILOCODE_API_KEY` | — |
| `xiaomi`（別名 `mimo`） | 小米 MiMo | `XIAOMI_API_KEY` | — |
| `tencent-tokenhub`（別名 `tencent`） | 騰訊 Tokenhub | `TOKENHUB_API_KEY` | Hy3 Preview 模型 |
| `opencode-zen` / `opencode-go` | OpenCode | `OPENCODE_ZEN_API_KEY` / `OPENCODE_GO_API_KEY` | — |
| `deepseek` | DeepSeek | `DEEPSEEK_API_KEY` | DeepSeek v3／v4 系列 |
| `huggingface`（別名 `hf`） | Hugging Face | `HF_TOKEN` | 20+ 開源模型，統一 OpenAI 相容端點 |
| `gemini` | Google AI Studio | `GOOGLE_API_KEY` / `GEMINI_API_KEY` | Gemini 系列 |
| `vertex` | Google Vertex AI | Service Account／ADC | **v0.18.0 新增**，自動換發短期 Token，免靜態金鑰 |
| `openai-api` | OpenAI API | `OPENAI_API_KEY` | v0.15.0 起獨立 Provider（不與 Codex 共用） |
| `azure-foundry` | Azure AI Foundry | OAuth2（Microsoft Entra ID） | v0.12.0 新增，v0.15.0 支援 Entra ID |
| `bedrock` | AWS Bedrock | 標準 AWS 憑證鏈（boto3） | Converse API（Native），免 API Key |
| `nvidia` | NVIDIA NIM | `NVIDIA_API_KEY` | build.nvidia.com 託管模型 |
| `ollama-cloud` | Ollama Cloud | `OLLAMA_API_KEY` | 雲端版 Ollama |
| `stepfun` | StepFun | `STEPFUN_API_KEY` | 階段規劃推理 |
| `lmstudio` | LM Studio | 選用 `LM_API_KEY` | 本地桌面 GUI 應用 |
| `custom` | 任意 OpenAI 相容端點 | 依端點而定 | 通用相容層 |
| **`meta`（Meta Model API）** | Meta Model API | 依官方設定 | **v0.21.0 新增**，提供 Muse Spark 系列；經 Responses API 路由以支援快取 |
| **`commandcode`** | CommandCode | 依官方設定 | **v0.20.3 新增**，GOAT／Pro／Max 三個 SKU |
| **`tencent-tokenplan`** | 騰訊 TokenPlan | 依官方設定 | **v0.21.0 新增**，與既有 `tencent-tokenhub` 為不同 SKU |
| **`nebius`** | Nebius Token Factory | 依官方設定 | **v0.21.0 新增** |
| **`ramp`（Ramp Router）** | Ramp Router | 依官方設定 | **v0.21.0 新增**，路由型 Provider |

#### D.1.1 v0.21.0 新增模型

| 模型 | 所屬 | 備註 |
| ------ | ------ | ------ |
| `qwen3.8-max` / `qwen3.8-flash` | Qwen | — |
| Gemini 3.7 Flash | Google | — |
| GLM-5.3-Flash | z.ai／GLM | 於多個目錄同時上架 |
| MiniMax M3 + Inkling | MiniMax | **含免費 SKU** |
| Nemotron 3.5 Lightning | NVIDIA | — |
| Meta Muse Spark 1.2 | Meta Model API | — |

#### D.1.2 `model_overrides` — 免改版覆寫與可插拔 Provider（v0.21.0）

上游調整了 context window 或定價、而 Hermes 目錄尚未跟上時，不必等待官方發版：

```yaml
# ~/.hermes/config.yaml
model_overrides:
  "openrouter/some-vendor/new-model":
    context_window: 400000
    input_price_per_1m: 1.25
    output_price_per_1m: 5.00
    supports_vision: true
```

同時 v0.21.0 起，**以 pip 安裝的第三方模型 Provider 可透過 Python entry points 被自動探索**，無須修改 Hermes 本體。另有兩項與模型目錄相關的校正值得注意：Codex GPT 的 context 預設值已核實為 **272K**（並提供明確的 `-900k` 變體），以及**資料訓練層級（data-training-tier）警示已於所有模型選擇器介面統一顯示**——這對有資料落地要求的企業是實用的選型輔助。

> ⚠️ **變更管控**：`model_overrides` 直接影響成本估算與 context 管理決策，屬「繞過官方目錄」的機制，應納入設定檔版本控管與審核流程。

### D.2 自架／本地推理後端

| 後端 | 端點慣例 | 特點 |
| ------ | ------ | ------ |
| Ollama | `localhost:11434/v1` | 最普及的本地模型執行環境 |
| vLLM | `:8000/v1` | 高輸送量推論伺服器 |
| SGLang | `:30000/v1` | RadixAttention KV-cache 重用 |
| llama.cpp / llama-server | `:8080/v1` | 極輕量、CPU 可執行 |
| LiteLLM Proxy | `:4000/v1` | 統一代理 100+ Provider |
| **ClawRouter** | `:8402/v1` | 以 **USDC 加密貨幣**付費，依查詢複雜度自動選模型 |

### D.3 第三方 OpenAI 相容端點（經官方文件證實可用）

Together AI、Groq、Cerebras、Mistral AI、LocalAI、Jan、Perplexity——均可透過 `custom` Provider ID 或各自專屬設定連接。

> **架構說明**：v0.12.0 將所有 Provider 重構為 Pluggable 架構，v0.13.0 引入 `ProviderProfile` ABC 介面，v0.15.0 一度移除 Vercel AI Gateway 與 Vercel Sandbox（v0.20.0 現代化重新引入）。第三方可自行開發 Provider Plugin 並掛載至 Hermes，無需修改核心程式碼。

---

## 參考資源

| 資源 | 連結 |
| ------ | ------ |
| 官方文件首頁 | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/) |
| 快速入門 | [/docs/getting-started/quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) |
| 安裝指南 | [/docs/getting-started/installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation) |
| 平台支援層級 | [/docs/getting-started/platform-support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support) |
| GitHub | [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| GitHub Releases（版本紀錄權威來源） | [github.com/NousResearch/hermes-agent/releases](https://github.com/NousResearch/hermes-agent/releases) |
| Skills Hub | [agentskills.io](https://agentskills.io/) |
| skills.sh（社群技能目錄） | [skills.sh](https://skills.sh/) |
| Discord 社群 | [discord.gg/NousResearch](https://discord.gg/NousResearch) |
| Nous Portal | [portal.nousresearch.com](https://portal.nousresearch.com/) |
| Nous Portal 訂閱管理（定價一手來源） | [portal.nousresearch.com/manage-subscription](https://portal.nousresearch.com/manage-subscription) |
| OpenRouter | [openrouter.ai](https://openrouter.ai/) |
| Issue Tracker | [GitHub Issues](https://github.com/NousResearch/hermes-agent/issues) |
| 討論區 | [GitHub Discussions](https://github.com/NousResearch/hermes-agent/discussions) |
| Voice Mode 指南 | [/docs/guides/use-voice-mode-with-hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes) |
| MCP 使用指南 | [/docs/guides/use-mcp-with-hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes) |
| CLI 指令完整參考 | [/docs/reference/cli-commands](https://hermes-agent.nousresearch.com/docs/reference/cli-commands) |
| 官方 FAQ | [/docs/reference/faq](https://hermes-agent.nousresearch.com/docs/reference/faq) |
| 斜線指令完整參考 | [/docs/reference/slash-commands](https://hermes-agent.nousresearch.com/docs/reference/slash-commands) |
| 模型目錄 | [/docs/reference/model-catalog](https://hermes-agent.nousresearch.com/docs/reference/model-catalog) |
| 環境變數參考 | [/docs/reference/environment-variables](https://hermes-agent.nousresearch.com/docs/reference/environment-variables) |
| 開發者架構文件 | [/docs/developer-guide/architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture) |
| Desktop Plugin SDK 文件 | [/docs/developer-guide/desktop-plugin-sdk](https://hermes-agent.nousresearch.com/docs/developer-guide/desktop-plugin-sdk) |
| 軌跡格式規格（見 6.10.2 節） | [/docs/developer-guide/trajectory-format](https://hermes-agent.nousresearch.com/docs/developer-guide/trajectory-format) |
| 貢獻指南 | [/docs/developer-guide/contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing) |
| **Bot Mode（見第十五章）** | [/docs/user-guide/bot-mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode) |
| **Egress 憑證注入代理 iron-proxy（見 9.8 節）** | [/docs/user-guide/egress/iron-proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy) |
| **Managed Scope（見 4.8 節）** | [/docs/user-guide/managed-scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope) |
| **Tool Search（見 3.5.4 節）** | [/docs/user-guide/features/tool-search](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-search) |
| **Recurring Loops（見 3.11 節）** | [/docs/user-guide/features/loops](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops) |
| Kanban 逐步教學 | [/docs/user-guide/features/kanban-tutorial](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial) |
| Kanban Worker Lanes（見 6.3.4 節） | [/docs/user-guide/features/kanban-worker-lanes](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-worker-lanes) |
| 批次處理（見 6.10.1 節） | [/docs/user-guide/features/batch-processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing) |
| LSP 語義診斷（見 9.7.3 節校正） | [/docs/user-guide/features/lsp](https://hermes-agent.nousresearch.com/docs/user-guide/features/lsp) |
| 秘密來源：Bitwarden／1Password／Command Helper | [/docs/user-guide/secrets](https://hermes-agent.nousresearch.com/docs/user-guide/secrets) |
| 在工作機上安全運行 Hermes | [/docs/guides/secure-hermes-on-a-work-machine](https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine) |
| 疑難排解：「我的 Agent 變笨了」 | [/docs/guides/troubleshooting-agent-quality](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality) |
| 用戶故事與使用案例 | [/docs/user-stories](https://hermes-agent.nousresearch.com/docs/user-stories) |
| 社群生態系目錄（非官方，見 9.7.5 節使用提醒） | [github.com/0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) |
| 第三方企業威脅模型（**非官方觀點**，見 9.7.1 節） | [repello.ai/blog/hermes-agent-security](https://repello.ai/blog/hermes-agent-security) |

---

> **文件版本**：v8.0.0  
> **基於 Hermes Agent**：v0.21.0（Git tag `v2026.8.31`，The Pantheon Release；涵蓋 The Judgment／The Quicksilver／The Herald／The Pantheon 四大版本 + 中間全部穩定化補丁）  
> **建立日期**：2026 年 4 月 9 日  
> **最後更新**：2026 年 9 月 1 日  
> **維護者**：技術架構團隊  
> **本次更新重點**：
>
> 1. **版本基準升至 v0.21.0**：補齊 v0.20.2 – v0.20.6 六個補丁版本與 v0.21.0「The Pantheon Release」的完整發展歷程，GitHub 統計數字依 REST API 一手覆核（Stars 239,282／Forks 48,843／Open Issues 38,350／Releases 31）
> 2. **新增第十五章「Bot Mode 與多 Agent 群組協作」**：涵蓋 bot 即 profile 的定位、群組聊天機制、`hermes peer` 跨 Gateway 直訊，以及**五種多 Agent 機制的四維度選型對照表與決策樹**
> 3. **新增 9.8 節「Egress 憑證注入代理（iron-proxy）」**：本次篇幅最大的新增，完整記錄架構、`proxy:` 設定鍵、雙層允許清單與 SSRF 防護、輪替流程，以及六項已知限制
> 4. **新增 4.8 節「Managed Scope」**：組織層級設定釘選，並明確揭露其 v1 版本**不可作為權限控管邊界**
> 5. **新增 3.5.4 Tool Search、3.11 Recurring Loops（含 `/loop` vs `/goal` vs Cron 對照）、6.2.1c Live Subagent Orchestration、6.3.4 Kanban Worker Lanes、6.6.5 Cron 記憶化、6.10 Batch Processing 與 Trajectory Format、9.1.5 受保護指令檔**
> 6. **既有內容失準校正**：修正 9.7.3「缺乏原生 LSP／AST 整合」的過時判斷；`hermes audit` 更名為 `hermes security audit`；平台支援層級依官方 Tier 表補上安裝管道；定價章節補上 bonus credits 與 Tool Gateway 五項工具明細
> 7. **企業風險章節強化**：9.7.1 新增 CVE-2026-7396 與第三方威脅模型的四大攻擊面對照；9.7.6 檢查清單新增 6 項 v0.21.0 相關項目
> 8. **第十一章新增 11.1.14／11.1.15**：完整記錄 v0.20.x 補丁串（含 v0.20.3 的 MCP 2.x 破壞性遷移）與 v0.21.0 升級注意事項，含已回退功能清單
> 9. **附錄全面重建**：附錄 B 依官方參考文件補齊 `hermes peer`／`egress`／`approval-check` 等 CLI 與 40+ 斜線指令；附錄 C 新增 `HERMES_MANAGED_DIR`／`API_SERVER_KEY`；附錄 D 新增 6 個 Provider、6 個模型與 `model_overrides` 機制
> 10. **目錄與格式**：加入 `TOC-AUTO` 標記使目錄可機器驗證、統一目錄深度規則、修正 §4.6／§4.7 子節編號錯誤與尾隨空白等 Markdown 問題
