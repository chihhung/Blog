+++
date = '2026-06-30T10:00:00+08:00'
draft = false
title = 'Hermes Agent生態系教學手冊'
tags = ['教學', 'AI開發','指引']
categories = ['教學']
lastmod = '2026-11-08T20:00:00+08:00'
+++

# Hermes Agent 生態系教學手冊（Enterprise Edition）

> **版本**：基於 Hermes Agent **v0.23.0**（Git tag `v0.23.0`，2026 年 11 月 5 日 — **The Hearth Release**；涵蓋 v0.22.0 The Threshold 與 v0.21.1–v0.22.7 全部補丁）；文件版本 v9.0.0
> **適用對象**：資深工程師 / 架構師 / DevOps 團隊 / 技術採購與風險評估決策者
> **軟體授權**：MIT License（Hermes Agent 本體完全開源、免費、可自架；下述訂閱方案僅為選用的 Nous Portal 代管服務，非軟體授權費）
> **官方網站**：[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)
> **GitHub**：[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
> **官方文件**：[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)
> **Desktop 下載**：[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)（macOS 13+ Apple Silicon 簽章 DMG／Windows 11 22H2+ MSIX 或 Microsoft Store；官方不提供 Linux 與 Intel macOS 桌面套件）
> **Skills Hub**：[agentskills.io](https://agentskills.io/) / [skills.sh](https://skills.sh/)
> **LLM 友善文件**：[llms.txt](https://hermes-agent.nousresearch.com/docs/llms.txt) / [llms-full.txt](https://hermes-agent.nousresearch.com/docs/llms-full.txt)
> **最後更新**：2026 年 11 月 8 日
> **資料來源聲明**：本文所有版本資訊、功能敘述均逐條核對 **GitHub Releases API**（v0.21.0 起 18 份 release notes）、**GitHub REST API**（倉庫即時數據）、**v0.23.0 tag 的原始碼與 `website/docs/`（435 頁）**、GitHub Advisory 資料庫；指令、設定鍵與環境變數另以**實際安裝的 v0.23.0** 驗證（真實 argparse 指令樹、`hermes config set` 使用的設定鍵驗證器、官方環境變數參考），方法與結果見[附錄 E](#附錄-e驗證紀錄v900)；價格類數字凡標示「二手來源」者，代表官方定價頁在查證當下回應 HTTP 429，未能以一手頁面直接核實，建議上線前至 [portal.nousresearch.com/manage-subscription](https://portal.nousresearch.com/manage-subscription) 覆核。

---

<!-- TOC-AUTO-BEGIN -->

## 📑 目錄

> 目錄採三層結構：**章**（第一層）→ **節**（`x.y`，第二層）→ 第三層僅保留兩處「索引型」清單——**1.4.x 核心設計理念**（功能總覽）與 **9.7.x 風險評估**，其餘小節請於各節內文瀏覽。所有連結皆依 Hugo 實際產生的錨點建立，並以輸出頁面逐一比對。

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
    - [1.4.13 `hermes proxy` — OpenAI 相容本地代理（v0.14.0+）](#1413-hermes-proxy--openai-相容本地代理v0140)
    - [1.4.14 PyPI 套件安裝（v0.14.0 起，**v0.20.0 已停用**）](#1414-pypi-套件安裝v0140-起v0200-已停用)
    - [1.4.15 `/handoff` 即時 Session 轉移（v0.14.0+）](#1415-handoff-即時-session-轉移v0140)
    - [1.4.16 Promptware 防禦（v0.15.0+）](#1416-promptware-防禦v0150)
    - [1.4.17 Bitwarden Secrets Manager（v0.15.0+）](#1417-bitwarden-secrets-managerv0150)
    - [1.4.18 Skill Bundles（v0.15.0+）](#1418-skill-bundlesv0150)
    - [1.4.19 Hermes Desktop App（v0.16.0+）](#1419-hermes-desktop-appv0160)
    - [1.4.20 Background Subagents（v0.17.0+）](#1420-background-subagentsv0170)
    - [1.4.21 Image Editing（v0.17.0+）](#1421-image-editingv0170)
    - [1.4.22 Automation Blueprints（v0.17.0+）](#1422-automation-blueprintsv0170)
    - [1.4.23 Memory Atomic Batch Operations（v0.17.0+）](#1423-memory-atomic-batch-operationsv0170)
    - [1.4.24 Mixture-of-Agents（MoA）一級模型化（v0.18.0+）](#1424-mixture-of-agentsmoa一級模型化v0180)
    - [1.4.25 自我學習強化：`/learn` 與 `/journey`（v0.18.0+）](#1425-自我學習強化learn-與-journeyv0180)
    - [1.4.26 `/goal` 完成契約（Completion Contracts）（v0.18.0+）](#1426-goal-完成契約completion-contractsv0180)
    - [1.4.27 訂閱管理與密碼管理器整合（v0.19.0+）](#1427-訂閱管理與密碼管理器整合v0190)
    - [1.4.28 智慧審批預設化與配送保證（v0.19.0+）](#1428-智慧審批預設化與配送保證v0190)
    - [1.4.29 A2A（Agent-to-Agent）協定 v1.0（v0.20.0+）](#1429-a2aagent-to-agent協定-v10v0200)
    - [1.4.30 即時對話式語音（v0.20.0+）](#1430-即時對話式語音v0200)
    - [1.4.31 簽章式 Outbound Webhook（v0.20.0+）](#1431-簽章式-outbound-webhookv0200)
    - [1.4.32 Desktop 平台化：Artifacts 與 Plugin SDK（v0.20.0+）](#1432-desktop-平台化artifacts-與-plugin-sdkv0200)
    - [1.4.33 CLI 強化指令與中途導引（v0.20.0+）](#1433-cli-強化指令與中途導引v0200)
    - [1.4.34 Bot Mode — Profile 具名化與群組協作（v0.21.0+）](#1434-bot-mode--profile-具名化與群組協作v0210)
    - [1.4.35 `hermes peer` — 跨 Gateway Agent 直訊（v0.21.0+）](#1435-hermes-peer--跨-gateway-agent-直訊v0210)
    - [1.4.36 Cron 記憶化與 `continuity` 連續性（v0.21.0+）](#1436-cron-記憶化與-continuity-連續性v0210)
    - [1.4.37 Live Subagent Orchestration（v0.21.0+）](#1437-live-subagent-orchestrationv0210)
    - [1.4.38 MCP Command Center 與 `hermes://` Deep Link（v0.21.0+）](#1438-mcp-command-center-與-hermes-deep-linkv0210)
    - [1.4.39 Agent 驅動的應用內瀏覽器（v0.21.0+）](#1439-agent-驅動的應用內瀏覽器v0210)
    - [1.4.40 CLI Power Wave（v0.21.0+）](#1440-cli-power-wavev0210)
    - [1.4.41 `model_overrides` — 免等改版的模型參數覆寫（v0.21.0+）](#1441-model_overrides--免等改版的模型參數覆寫v0210)
    - [1.4.42 穩定發行通道與統一套件管理器 PM（v0.21.7／v0.22.0+）](#1442-穩定發行通道與統一套件管理器-pmv0217v0220)
    - [1.4.43 首次啟動引導、免費方案與 Connectors（v0.22.0+）](#1443-首次啟動引導免費方案與-connectorsv0220)
    - [1.4.44 一鍵 Local Models（v0.22.0+）](#1444-一鍵-local-modelsv0220)
    - [1.4.45 單一 Gateway 擁有所有對話（v0.22.0／v0.23.0）](#1445-單一-gateway-擁有所有對話v0220v0230)
    - [1.4.46 Plugin Catalog 與自動更新（v0.22.0／v0.23.0）](#1446-plugin-catalog-與自動更新v0220v0230)
    - [1.4.47 Webapp：瀏覽器中的 Desktop 工作區（v0.23.0）](#1447-webapp瀏覽器中的-desktop-工作區v0230)
    - [1.4.48 對話回溯 `/rewind` 與終端機圖片（v0.23.0）](#1448-對話回溯-rewind-與終端機圖片v0230)
    - [1.4.49 Group Chats 自主運作與 Bot Screen（v0.22.0／v0.23.0）](#1449-group-chats-自主運作與-bot-screenv0220v0230)
    - [1.4.50 付費工具標價與花費上限（v0.23.0）](#1450-付費工具標價與花費上限v0230)
    - [1.4.51 可插拔委派策略與子代理即時操控（v0.22.0／v0.23.0）](#1451-可插拔委派策略與子代理即時操控v0220v0230)
    - [1.4.52 精簡技能集與 Cron 控制（v0.23.0）](#1452-精簡技能集與-cron-控制v0230)
  - [1.5 本章審查與驗證清單](#15-本章審查與驗證清單)
- [第二章：整體系統架構](#第二章整體系統架構)
  - [2.1 架構設計概述](#21-架構設計概述)
  - [2.2 分層架構圖](#22-分層架構圖)
  - [2.3 各層級說明](#23-各層級說明)
  - [2.4 多 Agent 協作架構](#24-多-agent-協作架構)
  - [2.5 高可用與擴展性設計](#25-高可用與擴展性設計)
  - [2.6 本章審查與驗證清單](#26-本章審查與驗證清單)
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
  - [3.11 Recurring Loops（`/loop`）與 Session Heartbeats](#311-recurring-loopsloop與-session-heartbeats)
  - [3.12 本章審查與驗證清單](#312-本章審查與驗證清單)
- [第四章：安裝與環境建置](#第四章安裝與環境建置)
  - [4.1 系統需求](#41-系統需求)
  - [4.2 快速安裝（Linux / macOS / WSL2）](#42-快速安裝linux--macos--wsl2)
  - [4.3 Native Windows 安裝](#43-native-windows-安裝)
  - [4.4 Docker / Podman 部署](#44-docker--podman-部署)
  - [4.5 Nix 安裝（Tier 2）](#45-nix-安裝tier-2)
  - [4.6 設定 API Key](#46-設定-api-key)
  - [4.7 設定檔說明](#47-設定檔說明)
  - [4.8 Managed Scope（組織層級設定釘選）](#48-managed-scope組織層級設定釘選)
  - [4.9 本章審查與驗證清單](#49-本章審查與驗證清單)
- [第五章：快速開始（Quick Start）](#第五章快速開始quick-start)
  - [5.1 第一次對話](#51-第一次對話)
  - [5.2 建立 AI Coding Agent](#52-建立-ai-coding-agent)
  - [5.3 設定 Memory](#53-設定-memory)
  - [5.4 設定 Tools](#54-設定-tools)
  - [5.5 執行任務範例](#55-執行任務範例)
  - [5.6 本章審查與驗證清單](#56-本章審查與驗證清單)
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
  - [6.11 本章審查與驗證清單](#611-本章審查與驗證清單)
- [第七章：Voice Mode（語音模式）](#第七章voice-mode語音模式)
  - [7.1 語音模式概述](#71-語音模式概述)
  - [7.2 支援的 STT / TTS 提供者](#72-支援的-stt--tts-提供者)
  - [7.3 CLI 語音互動](#73-cli-語音互動)
  - [7.4 Telegram / Discord 語音互動](#74-telegram--discord-語音互動)
  - [7.5 Discord Voice Channel 即時語音](#75-discord-voice-channel-即時語音)
  - [7.6 企業語音整合建議](#76-企業語音整合建議)
  - [7.7 本章審查與驗證清單](#77-本章審查與驗證清單)
- [第八章：Web Application 整合](#第八章web-application-整合)
  - [8.1 整合架構設計](#81-整合架構設計)
  - [8.2 FastAPI 後端整合](#82-fastapi-後端整合)
  - [8.3 Spring Boot 後端整合](#83-spring-boot-後端整合)
  - [8.4 前端整合（Vue / React）](#84-前端整合vue--react)
  - [8.5 Agent-as-a-Service API 設計](#85-agent-as-a-service-api-設計)
  - [8.6 本章審查與驗證清單](#86-本章審查與驗證清單)
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
  - [9.9 v0.22／v0.23 新增的安全與治理議題](#99-v022v023-新增的安全與治理議題)
  - [9.10 本章審查與驗證清單](#910-本章審查與驗證清單)
- [第十章：部署與維運（DevOps）](#第十章部署與維運devops)
  - [10.1 Docker 部署](#101-docker-部署)
  - [10.2 Kubernetes 部署](#102-kubernetes-部署)
  - [10.3 CI/CD 流程](#103-cicd-流程)
  - [10.4 升級與回退](#104-升級與回退)
  - [10.5 災難復原（DR）](#105-災難復原dr)
  - [10.6 本章審查與驗證清單](#106-本章審查與驗證清單)
- [第十一章：升級與版本管理](#第十一章升級與版本管理)
  - [11.1 升級策略](#111-升級策略)
  - [11.2 相容性管理](#112-相容性管理)
  - [11.3 Migration 設計](#113-migration-設計)
  - [11.4 本章審查與驗證清單](#114-本章審查與驗證清單)
- [第十二章：實戰案例](#第十二章實戰案例)
  - [12.1 AI Coding Agent](#121-ai-coding-agent)
  - [12.2 智慧客服 Agent](#122-智慧客服-agent)
  - [12.3 銀行流程自動化 Agent](#123-銀行流程自動化-agent)
  - [12.4 多媒體創作 Agent](#124-多媒體創作-agent)
  - [12.5 本章審查與驗證清單](#125-本章審查與驗證清單)
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
  - [Q13：`hermes -z` 和普通模式有何不同？（v0.12.0）](#q13hermes--z-和普通模式有何不同v0120)
  - [Q14：如何使用 Background Sessions？（v0.12.0）](#q14如何使用-background-sessionsv0120)
  - [Q15：如何配置 Prompt Cache？（v0.12.0）](#q15如何配置-prompt-cachev0120)
  - [Q16：Multi-agent Kanban 如何設定？（v0.13.0）](#q16multi-agent-kanban-如何設定v0130)
  - [Q17：如何啟用 i18n（多語系）介面？（v0.13.0）](#q17如何啟用-i18n多語系介面v0130)
  - [Q18：video_analyze 工具怎麼用？（v0.13.0）](#q18video_analyze-工具怎麼用v0130)
  - [Q19：原本用 `brew install hermes-agent` 或 `pip install hermes-agent` 安裝，現在升級失敗怎麼辦？（v0.20.0）](#q19原本用-brew-install-hermes-agent-或-pip-install-hermes-agent-安裝現在升級失敗怎麼辦v0200)
  - [Q20：升級後危險指令不再每次都問我，是不是有安全問題？（v0.19.0）](#q20升級後危險指令不再每次都問我是不是有安全問題v0190)
  - [Q21：什麼時候該用 A2A，什麼時候該用 Kanban 或 delegate_task？（v0.20.0）](#q21什麼時候該用-a2a什麼時候該用-kanban-或-delegate_taskv0200)
  - [Q22：官方說「Hermes 完全免費」，為什麼還有月費方案？](#q22官方說hermes-完全免費為什麼還有月費方案)
  - [Q23：升級 v0.21.0 後多出一堆「bot」，這是什麼？有風險嗎？怎麼關掉？（v0.21.0）](#q23升級-v0210-後多出一堆bot這是什麼有風險嗎怎麼關掉v0210)
  - [Q24：`hermes egress`（iron-proxy）和 `hermes proxy` 有什麼不同？](#q24hermes-egressiron-proxy和-hermes-proxy-有什麼不同)
  - [Q25：`/loop`、`/goal`、Cron 三個看起來都是「重複執行」，該用哪個？](#q25loopgoalcron-三個看起來都是重複執行該用哪個)
  - [Q26：v0.21.0 把委派併發預設值調高了，成本會失控嗎？](#q26v0210-把委派併發預設值調高了成本會失控嗎)
  - [Q27：Managed Scope 可以當作正式的權限控管邊界嗎？](#q27managed-scope-可以當作正式的權限控管邊界嗎)
  - [Q28：Tool Search 值得開嗎？什麼情況下反而變慢？](#q28tool-search-值得開嗎什麼情況下反而變慢)
  - [Q29：升級到 v0.23.0 後，原本的瀏覽器自動化技能失效了？（v0.23.0）](#q29升級到-v0230-後原本的瀏覽器自動化技能失效了v0230)
  - [Q30：Claude Desktop／IDE 把 Hermes 當成 MCP Server，升級後連不上？（v0.23.0）](#q30claude-desktopide-把-hermes-當成-mcp-server升級後連不上v0230)
  - [Q31：為什麼 `hermes -p coder gateway start` 被拒絕（exit 78）？（v0.22.0）](#q31為什麼-hermes--p-coder-gateway-start-被拒絕exit-78v0220)
  - [Q32：升級後可以退回 v0.21.x 嗎？（v0.23.0）](#q32升級後可以退回-v021x-嗎v0230)
  - [Q33：舊對話在 Webapp 中是唯讀的？（v0.23.0）](#q33舊對話在-webapp-中是唯讀的v0230)
  - [Q34：舊 Session 會不會被自動刪除？（v0.22.0／v0.23.0）](#q34舊-session-會不會被自動刪除v0220v0230)
  - [Q35：外部記憶（Honcho／Mem0／Supermemory）升級後不見了？（v0.22.0）](#q35外部記憶honchomem0supermemory升級後不見了v0220)
  - [Q36：Local Models 要怎麼在無 GPU 的伺服器上用？（v0.22.0）](#q36local-models-要怎麼在無-gpu-的伺服器上用v0220)
  - [Q37：付費 MCP 工具在 Cron 中一直被拒絕？（v0.23.0）](#q37付費-mcp-工具在-cron-中一直被拒絕v0230)
  - [本章審查與驗證清單](#本章審查與驗證清單)
- [第十四章：Hermes Desktop App（v0.16.0+，v0.20.0 起成為完整平台）](#第十四章hermes-desktop-appv0160v0200-起成為完整平台)
  - [14.1 架構概覽](#141-架構概覽)
  - [14.2 安裝方式](#142-安裝方式)
  - [14.3 核心功能](#143-核心功能)
  - [14.4 解除安裝](#144-解除安裝)
  - [14.5 企業部署建議](#145-企業部署建議)
  - [14.6 Webapp（v0.23.0）](#146-webappv0230)
  - [14.7 多 Gateway 連線與 Bot Screen（v0.22.0／v0.23.0）](#147-多-gateway-連線與-bot-screenv0220v0230)
  - [14.8 本章審查與驗證清單](#148-本章審查與驗證清單)
- [第十五章：Bot Mode 與多 Agent 群組協作（v0.21.0）](#第十五章bot-mode-與多-agent-群組協作v0210)
  - [15.1 概念定位：bot 即 profile](#151-概念定位bot-即-profile)
  - [15.2 建立與設定 Bot](#152-建立與設定-bot)
  - [15.3 群組聊天機制](#153-群組聊天機制)
  - [15.4 `hermes peer` — 跨 Gateway Agent 直訊](#154-hermes-peer--跨-gateway-agent-直訊)
  - [15.5 五種多 Agent 機制選型對照](#155-五種多-agent-機制選型對照)
  - [15.6 企業治理與關閉方式](#156-企業治理與關閉方式)
  - [15.7 CLI 對應指令](#157-cli-對應指令)
  - [15.8 本章審查與驗證清單](#158-本章審查與驗證清單)
- [附錄 A：檢查清單（Checklist）](#附錄-a檢查清單checklist)
  - [A.1 安裝檢查清單](#a1-安裝檢查清單)
  - [A.2 API Key 設定檢查清單](#a2-api-key-設定檢查清單)
  - [A.3 安全檢查清單](#a3-安全檢查清單)
  - [A.4 生產部署檢查清單](#a4-生產部署檢查清單)
  - [A.5 團隊導入檢查清單](#a5-團隊導入檢查清單)
  - [A.6 升級檢查清單](#a6-升級檢查清單)
  - [A.7 v0.22／v0.23 新增檢查項目](#a7-v022v023-新增檢查項目)
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
- [附錄 E：驗證紀錄（v9.0.0）](#附錄-e驗證紀錄v900)
  - [E.1 版本基準與權威來源](#e1-版本基準與權威來源)
  - [E.2 原稿更正清單](#e2-原稿更正清單)
  - [E.3 實測方法與結果](#e3-實測方法與結果)
  - [E.4 待確認事項](#e4-待確認事項)
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
| v0.9.0 | 2026.04.13 | **Web Dashboard**、Fast Mode（`/fast`）、iMessage（BlueBubbles）、WeChat/WeCom Callback、Termux/Android 支援、`hermes backup`／`hermes import`、16 平台、487 commits |
| v0.10.0 | 2026.04.16 | **Nous Tool Gateway**（付費訂閱用戶自動取得 Web Search/Image Gen/TTS/Browser 工具，零額外 API Key） |
| v0.11.0 | 2026.04.23 | **Ink TUI 全面重寫**、Transport ABC 架構、Native AWS Bedrock、5 新推理路徑（NVIDIA NIM/Arcee AI/Step Plan/Gemini CLI OAuth/Vercel AI Gateway）、GPT-5.5 via Codex OAuth、QQBot（第 17 平台）、Plugin 大幅擴展、`/steer` 中途導引、Shell Hooks、Orchestrator 子代理、1,556 commits |
| v0.12.0 | 2026.04.30 | **Autonomous Curator**（自動技能維護 Agent）、Self-improvement Loop 大幅升級（rubric-based）、5 新 Provider（LM Studio / GMI Cloud / Azure AI Foundry / MiniMax OAuth / Tencent Tokenhub）、Pluggable Gateway Platforms、Microsoft Teams（第 19 平台）、Tencent 元宝（第 18 平台）、Spotify 原生整合（7 工具 + PKCE OAuth）、Google Meet Plugin、ComfyUI v5 內建、Piper 本地 TTS、`hermes -z` 單次模式、Models Dashboard Tab、Remote Model Catalog、Cold-start 效能提升 ~57%、Langfuse 可觀測性 Plugin、1,096 commits |
| v0.13.0 | 2026.05.07 | **Multi-agent Kanban**（持久多 Agent 協作看板：心跳 / 回收 / 殭屍偵測 / 重試預算 / 幻覺閘門）、**`/goal`**（跨回合持久目標 — Ralph Loop）、**`video_analyze`** 原生影片理解工具、**xAI Custom Voices** 語音克隆 TTS、**Google Chat**（第 20 平台）+ 通用平台 Plugin Hooks、**Sessions 自動恢復**（Gateway 重啟後對話復原）、**8 項 P0 安全修正**（Secret Redaction 預設開啟、Discord 角色白名單 Guild 隔離 CVSS 8.1、WhatsApp 預設拒絕陌生人、TOCTOU 修正）、**Checkpoints v2**（狀態持久化重寫 + 真正修剪 + 磁碟護欄）、**Post-write Delta Lint**（write_file + patch 後自動 lint：Python/JSON/YAML/TOML）、**`no_agent` Cron 模式**（純腳本看門狗）、**Platform Allowlists**（`allowed_channels/chats/rooms` 全平台）、**ProviderProfile ABC**（Provider 可插拔化）、**API Server `X-Hermes-Session-Key`**（記憶 Session 隔離）、**MCP SSE Transport + OAuth 轉發**、**Curator 新子指令**（`archive` / `prune` / `list-archived` / 同步 `run`）、**ACP `/steer` + `/queue`**（VS Code/Zed/JetBrains）、**Dashboard 升級**（Plugins 頁 / Profiles 頁 / 可排序分析表 / 反向代理 `X-Forwarded-Prefix` / `default-large` 18px 主題）、**SearXNG 原生搜尋後端** + 分離式 Web 工具（搜尋/擷取/瀏覽各自選擇後端）、**OpenRouter Response Caching**、**`[[as_document]]` Skill 媒體路由指令**、**`transform_llm_output` Plugin Hook**、**7 語言 i18n**（中/日/德/西/法/烏/土）、**Native Windows 早期測試版**（PowerShell 安裝腳本）、**6 新 Optional Skills**（Shopify / here.now / shop-app / Anthropic 金融服務 / kanban-video-orchestrator / searxng-search）、新模型（DeepSeek v4 Pro / Grok 4.3 / Owl Alpha / tencent hy3-preview / Arcee Trinity Large Thinking）、**100 新 CLI 啟動提示**、864 commits / 588 PR / 295 貢獻者 |
| v0.14.0 | 2026.05.16 | **The Foundation Release**：**xAI Grok via SuperGrok OAuth**（grok-4.3 升至 1M context window）、**`hermes proxy`**（OpenAI 相容本地代理，一個訂閱所有工具可用：Codex/Aider/Cline/Continue）、**`x_search`** 第一級 X (Twitter) 搜尋工具、**Microsoft Teams 端到端整合**（Graph auth + webhook + pipeline + outbound）、**去臃腫化浪潮**（lazy install 大幅減少安裝體積）、**`pip install hermes-agent`**（PyPI 正式套件）、**跨 Session 1 小時 Claude Prompt Cache**、**180 倍 `browser_console` 效能提升**（持久 CDP 連線）、**冷啟動效能浪潮**（啟動快 ~19 秒）、**LINE + SimpleX Chat**（第 21、22 平台）、**`/handoff`** 即時 Session 轉移（跨模型/Profile 零掉落）、**`clarify` 原生按鈕 UI**（Telegram/Discord）、**Discord 頻道歷史回填**、**`vision_analyze` 原生像素傳遞**（Vision 模型直接看圖）、**Per-turn 檔案變更驗證 Footer**、**LSP 語義診斷**（write_file/patch 後真實語言伺服器分析）、**統一 `video_generate` 可插拔後端**、**`computer_use` cua-driver 後端**（非 Anthropic 模型也可驅動桌面）、**可點擊 OSC8 URL**、**Zed ACP Registry**（`uvx` 一鍵安裝）、**OpenRouter Pareto Code Router**（`min_coding_score`）、**NovitaAI 新 Provider**、**Codex app-server Runtime**、**`huggingface/skills` 預設信任 Tap**、**9 新 Optional Skills**（Hyperliquid/Yahoo Finance/api-testing/EVM/darwinian-evolver/osint/pinggy-tunnel/watchers/Notion）、**`/subgoal`** 目標追加、**Alibaba Cloud → Qwen Cloud 更名**、**Native Windows Beta**（PowerShell installer + MinGit）、**16 語系 i18n**、**Brave Search + DDGS 免費搜尋**、**Sudo brute-force 阻擋**、**Plugin `ctx.llm` + `tool_override`**、808 commits / 633 PR / 215 貢獻者 |
| v0.15.0 | 2026.05.28 | **The Velocity Release**：**The Big Refactor** — `run_agent.py` 16,083 → 3,821 行（-76%），拆分為 14 個 `agent/*` 模組、**Kanban 成熟化浪潮**（104 PR：Swarm v1 拓撲、`hermes kanban swarm`、自動分解、per-task model override、排程任務、worktree-per-task、worker visibility endpoints、拖放刪除）、**冷啟動效能持續優化**（47% fewer per-turn function calls、`hermes --version` 快 63%、Termux 2.9s → 0.8s）、**`session_search` 重建**（無 LLM、免費、4,500 倍快速）、**Promptware 防禦**（Brainworm-class 攻擊阻擋：threat patterns + 記憶掃描 + tool-result delimiters）、**Bitwarden Secrets Manager**（一個 bootstrap token 取代所有 API Key）、**ntfy**（第 23 平台：自託管推播通知、零帳號）、**Skill Bundles**（`/<name>` 一次載入多個 Skills）、**TUI Session Orchestrator**（多活躍 Session 切換）、**Krea 2 Medium + Large 圖片生成**、**FAL 移至 Plugin 架構**、**Nous 核准 MCP 目錄**（互動式 picker + 一鍵安裝）、**OpenHands 協作技能**（delegate 至 OpenHands CLI）、**深度 xAI 整合**（Web Search plugin、`hermes proxy` xAI 上游、May 15 模型退役偵測 + `hermes migrate xai`、`auto_speech_tags` 自然 TTS、`base_url` 洩漏防護）、**s6-overlay Docker 容器監督**（systemd/launchd/Windows/s6 後端 + per-profile gateway 監督）、**Session Control API**（`/api/sessions/*` REST + SSE）、**mTLS MCP 支援**、**OpenAI API 作為獨立 Provider**、**Microsoft Entra ID auth for Azure Foundry**、**OpenRouter sticky routing**（`session_id`）、**移除 Vercel AI Gateway 與 Vercel Sandbox**、**3 新 Skills**（code-wiki / openhands / web-pentest）、**Plugin 新 Hooks**（`register_tts_provider` / `register_transcription_provider` / `register_auxiliary_task`）、**bundled `security-guidance` plugin**、**`hermes audit`**（現為 `hermes security audit`）OSV.dev 供應鏈審計、**`hermes send`** 腳本輸出推送任何平台、1,302 commits / 747 PR / 321 貢獻者 |
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
| v0.21.0 | 2026.08.31 | **The Pantheon Release**（自 v0.20.0 起累計 ~5,800 commits / 2,475 PR / 5,680 檔案 / 869,000 插入 / 135,000 刪除 / ~2,100 議題關閉 / 760+ 貢獻者，為本專案史上最大規模 Minor 發布）：**Bot Mode 內建化且預設開啟**（每個 Profile 成為具名 Agent，含依名稱決定的頭像、共享名冊、Discord 風格群組聊天，最多 6 bot 同室、3 輪序列回應）、**`hermes peer` 跨 Profile／跨 Gateway Agent 直訊**（對話持久且可稽核，落於各 Agent 的正規 Bot Chat）、**Cron 記憶化與連續性**（排程任務如同一般 Agent 載入持久記憶、`continuity=true` 跨執行帶入輸出、per-job 持久 notepad、monitor 模式無變更時以雜湊抑制跳過 LLM 呼叫）、**Live Subagent Orchestration**（`delegate_task` 支援執行中列出／中途導引／提前停止並保留部分結果，加上 JSON Schema 結構化輸出驗證與逐次委派成本追蹤；預設值提高至 250 iterations／10 並行子代理）、**MCP Command Center**（伺服器與目錄整併為單一 Desktop 頁面、拖放匯入、背景健康檢查、fleet 成本／用量疊層、`hermes://` deep link 一鍵安裝）、**CLI Power Wave**（`Ctrl+P` 模糊命令面板、`/model` 互動篩選、`/status` 顯示推理模式／待審批／context 用量、狀態列即時 cache-hit%／延遲／tokens-per-sec、全域緊急停止、Terminal Pets）、**Agent 驅動的應用內瀏覽器**（導航／點擊／讀取，可彈出至系統瀏覽器）、**6 個新 Provider**（Meta Model API〔Muse Spark〕／CommandCode〔GOAT・Pro・Max〕／Actual Computer／Tencent TokenPlan／Nebius Token Factory／Ramp Router）與 `model_overrides` 免改版覆寫、**安全強化波**（`AGENTS.md`／skills／memory 寫入一律需審批以阻擋提示注入改寫常規指令、終端錯誤與 `.env` 讀取與 checkpoints 與 ACP log 的秘密外洩清掃、Windows 破壞性指令納入審批、Blender MCP 目錄項目因上游遭入侵而下架、Plugin 安裝納入 Tier-1 安全掃描、macOS TCC 身分跨更新存續）；**已回退不出貨**：Model Council（`/council`）、DCP context engine、WS-only Gateway Server |
| v0.21.1–v0.21.5 | 2026.09.07–09.24 | 日期式 tag（`v2026.9.7`／`v2026.9.11`／`v2026.9.14`／`v2026.9.21`／`v2026.9.24`）的累積補丁，供 Docker 映像與 Hermes Cloud 依附；v0.21.2 為「state.db Patch Release」（消除第二寫入者、WAL 卡死、FTS 索引損壞不再中斷對話），v0.21.3 修正遠端 Dashboard Session 過期與 `state.db` 寫入 handle 外洩；完整分類說明延至 v0.22.0 |
| v0.21.6 | 2026.10.08 | **首個由新「穩定發行管線」產出的版本**：tag 改為 SemVer（`vX.Y.Z`），每次發行只出 tag + GitHub Release + 經測試的 Docker 映像 |
| v0.21.7 | 2026.10.12 | **原始碼安裝改追蹤已發布 Release**（不再逐 commit 追 `main`）、Desktop 新增「Update channel」切換、推理內容（thinking）在 `--resume` 後可重播 |
| v0.22.0 | 2026.10.13 | **The Threshold Release**（自 v0.21.0 起約 24,200 commits／6,080 PR／2,520 貢獻者）：首次啟動對話式引導（Onboarding）+ Nous 免費方案、**Connectors**（經 Nous Tool Gateway 在 Linear／Notion 等託管應用內操作）、**一鍵 Local Models**（自動安裝 llama.cpp 並依硬體挑選模型）、**穩定發行通道**（`hermes update --set-channel`）、**簽章 Desktop 套件 + Microsoft Store + 統一套件管理器（PM）**、**Plugin Catalog（600 個人工審核外掛）**、Claude 5.5／GPT-6／Gemini 4 模型波、瀏覽器以密碼管理器登入網站、**Bot Screen**（接手 bot 的桌面處理登入／2FA／CAPTCHA）、**每台機器單一 Gateway／單一 Desktop 後端服務所有 Profile**、子代理即時檢視與導引、16 語系全面翻譯、程式碼瘦身 34%（約 1.06M → 698K 行）。⚠️ 破壞性：Python 3.14、Windows Desktop 僅 MSIX、記憶 Provider 改為 catalog 外掛、移除 `hermes sync` 與 tirith（見 [11.1.16](#11116-v0210--v0230-升級特別注意事項目前最新版本)） |
| v0.22.1–v0.22.7 | 2026.10.14–11.03 | 穩定化補丁：Microsoft Store 修正、Nemotron 3.5 預設參數、Gateway 重開機後 PID 誤判修正（v0.22.2）、筆電上長時間 Local Model 回合不中斷、無依賴 Plugin 略過同意步驟（v0.22.4）；v0.22.3／.5／.6／.7 為累積 rollup（合計約 1,650 PR） |
| v0.23.0 | 2026.11.05 | **The Hearth Release**（**本手冊基準版本**；自 v0.22.0 起約 10,080 commits／1,950 PR／666 貢獻者）：**Webapp**（由自己的 Gateway 在瀏覽器提供完整 Desktop 工作區，預設關閉）、**單一 Gateway 擁有所有對話**（CLI／TUI／Desktop／ACP／Bot／Cron 都改為用戶端）、終端機內直接顯示圖片、**`/rewind`** 回溯並分岔對話、Desktop 同時連線多台機器、**Group Chats 自主運作**（lead bot／自動路由、房間筆記、Cron 發文、防 bot 互相觸發迴圈）、**Plugin 自動更新** + Catalog 擴充至 1,050+（新增 Verified 層級）、**付費 MCP 工具標價與每對話花費上限**、可插拔委派（`advanced-delegation` 外掛 + `/delegation`）、內建技能 58 → 44 + **`hermes curator lock`**、停止執行中的 Cron。⚠️ 破壞性：舊 `browser_*` 工具全數移除（只剩 `browser_exec`）、`hermes mcp serve` → `hermes mcp-serve`、Desktop 需 macOS 13+／64 位元 Windows |

**核心數據**（截至 2026.11.08，逐條核對 GitHub REST API 一手資料；括號內為 2026.09.01 舊值，便於觀察趨勢）：

- GitHub Stars：**261,617**（239,282）
- Forks：**58,096**（48,843）
- Open Issues：**53,675**（38,350；含 Issue 與 PR）
- Watchers（訂閱者）：**995**（933）
- 最近推送（`pushed_at`）：**2026-11-08**（開發活躍度極高，主分支 `main`；但一般安裝自 v0.21.7 起只追蹤已發布的 `vX.Y.Z` Release）
- 主要語言：**Python** 為主，TypeScript 次之（Desktop／Dashboard），另有 JavaScript／Shell／PowerShell／Nix 等
- 倉庫主題標籤：`ai`、`ai-agents`、`anthropic`、`chatgpt`、`claude`、`claude-code`、`codex`、`hermes`、`llm`、`nous-research`、`openai`
- 授權：**MIT License**（可商用，Hermes Agent 軟體本體完全免費）
- 專案建立日：2025-07-22；累計 Releases：**47 個**（GitHub Releases API 記錄自 v0.2.0 起算，v0.23.0 為最新）
- 程式規模：v0.22.0 官方宣稱「零行為變更」的全面簡化，原始碼由約 1.06M 行降至 698K 行（−34%），`gateway/run.py` 由 34,847 行降至 5,512 行

> ⚠️ **貢獻者人數存在口徑差異，企業評估時建議留意**：Hermes 官方各版本 Release Notes 慣例宣稱「370～760+ 貢獻者」（v0.21.0 宣稱 760+；v0.22.0 更宣稱自 v0.21.0 起約 2,520 人，v0.23.0 為 666 人），但透過 GitHub `/contributors` API 直接查證僅得數百個具名帳號——官方數字額外納入了 commit co-author 掛名與未直接合併之社群 PR 貢獻，兩者衡量口徑不同，非造假亦非錯誤，但代表專案核心可長期維運人力的真實規模，需另行評估。事實上 v0.21.0 官方自行揭露的核心團隊 PR 分布高度集中：`@teknium1` 一人即約 1,340 個 merged PR，其次 `@kshitijk4poor` 374 個、`@OutThisLife` 209 個，其餘核心成員多為兩位數——**Bus Factor 風險並未因總貢獻者數上升而改善**（詳見 9.7 節風險評估）。

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
| 記憶 | 僅單次對話 | 跨對話長期記憶（內建 `MEMORY.md`／`USER.md` + SQLite FTS5 Session 搜尋；外部記憶 Provider 自 v0.22.0 起改由 Plugin Catalog 安裝，ByteRover／RetainDB 仍內建）+ Session Key 隔離 |
| 學習 | 不會學習 | 內建 Learning Loop，自動封裝技能 + Autonomous Curator |
| 工具使用 | 有限（Plugins/GPTs） | 70+ 內建工具（約 19 個罕用工具改由 Tool Search 延遲載入）+ MCP 擴展（含工具標價與每對話花費上限）+ 1,050+ 人工審核 Catalog 外掛 |
| 執行環境 | 雲端沙箱 | 6 種內建終端後端：`local`／`docker`／`ssh`／`modal`／`daytona`／`vercel_sandbox`；Singularity 自 v0.23.0 起移為外掛，另有 bubblewrap 沙箱外掛 |
| 多平台 | Web UI 為主 | CLI + TUI + Desktop App + Webapp（v0.23.0，瀏覽器版 Desktop 工作區）+ 30+ 通訊平台／連接器（Telegram/Discord/Slack/Matrix/WhatsApp（Baileys＋官方 Cloud API 雙軌）/Signal/Email/SMS/DingTalk/Feishu/WeCom/微信/iMessage（BlueBubbles＋Photon 雙軌）/Mattermost/Home Assistant/QQBot/元寶/Microsoft Teams/Google Chat/LINE/SimpleX Chat/ntfy/Raft/Buzz（Nostr）/A2A/Webhook/API Server 等，另有實驗性 Hermes Relay 連接器框架） |
| 語音 | 有限 | Voice Mode（STT + TTS）支援 CLI / Telegram / Discord / Discord VC + xAI 語音克隆 |
| 模型綁定 | 固定 | 任意 OpenAI-compatible（200+ 模型）+ Provider 可插拔 ABC |
| 多 Agent | 無原生支援 | 子代理委派（可即時檢視／導引）、Multi-agent Kanban 持久協作看板、Bot Mode Group Chats、`hermes peer`、A2A v1.0 |
| 持久目標 | 僅單輪指令 | `/goal` 跨回合持久目標（Ralph Loop） |
| 國際化 | 僅介面語言 | 16 語系 i18n（中/日/德/西/法/烏/土/韓/義/葡 等） |
| 授權 | 閉源 | MIT（可商用） |
| 成本 | 按月訂閱 | 自控（用多少付多少 Token；或以一鍵 Local Models 完全離線、零 API 費用） |
| Windows 支援 | 原生 | Native Windows 為 Tier 1 平台（`install.ps1`；Desktop 為簽章 MSIX，需 Windows 11 22H2+，另上架 Microsoft Store）+ WSL2 完整支援 |
| Promptware 防禦 | 無 | Brainworm-class 攻擊阻擋（threat patterns + memory scan + tool-result delimiters） |
| 秘密管理 | 手動設定 | 可插拔秘密來源：Bitwarden Secrets Manager／1Password（`hermes secrets`）+ 加密瀏覽器憑證庫（`hermes vault`，金鑰可存 OS keychain） |
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
- **統一設定**：透過頂層 `curator:` 區塊配置（`interval_hours`、`stale_after_days`、`archive_after_days`、`consolidate` 等；⚠️ 舊版文件寫的 `auxiliary.curator` 並非有效鍵），可從 Dashboard 管理
- **鎖定技能**（v0.23.0）：`hermes curator lock <skill>` 讓 Agent 不能再透過任何工具改寫手工維護的技能，即使在 YOLO 模式下也一樣；`unlock` 解除
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
# ~/.hermes/config.yaml — Kanban 調度設定（鍵名以 v0.23.0 DEFAULT_CONFIG 為準）
kanban:
  dispatch_in_gateway: true        # 由 Gateway 內建調度器派工
  dispatch_interval_seconds: 60    # 調度週期（秒）
  failure_limit: 2                 # 連續失敗幾次後停止自動重派
  max_in_progress: 4               # 全看板同時進行中的任務上限（null = 不限）
  auto_decompose: true             # 允許 Orchestrator 自動拆解大型任務
```

> 💡 **審查要點**：重試次數是**每個任務**的屬性（`hermes kanban create --max-retries 3`），不是全域設定；舊版文件中的 `kanban.enabled`、`multi_project`、`heartbeat_interval`、`zombie_timeout`、`hallucination_gate` 都不是有效設定鍵（`hermes config set` 會提示「not a recognized config key」）。

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
# 啟動 hermes proxy（v0.23.0 為子指令 start；`hermes proxy providers` 列出可用上游）
hermes proxy start --port 4141

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

```bash
# 互動式設定（寫入 config.yaml 並驗證 token）
hermes secrets bitwarden setup --project-id <專案UUID>
hermes secrets bitwarden status
```

```yaml
# ~/.hermes/config.yaml — Bitwarden Secrets Manager 設定
secrets:
  bitwarden:
    enabled: true
    access_token_env: BWS_ACCESS_TOKEN   # 存放 Machine Account token 的環境變數「名稱」，不是 token 本身
    project_id: "00000000-0000-0000-0000-000000000000"
    cache_ttl_seconds: 300
```

#### 1.4.18 Skill Bundles（v0.15.0+）

v0.15.0 引入 Skill Bundles，一個指令載入多個相關技能：

- **語法**：`/<bundle-name>` 即可一次載入 Bundle 內列出的所有技能，斜線指令後的文字會作為使用者指示附上
- **建立方式**：`hermes bundles create backend-dev --skill github --skill test-driven-development -d "後端功能開發"`；以 `hermes bundles list`／`show` 檢視
- **沒有預設 Bundle**：Bundle 一律由使用者或團隊自行建立（舊版文件列出的 `/fullstack`、`/devops`、`/security` 並不存在）

#### 1.4.19 Hermes Desktop App（v0.16.0+）

v0.16.0（The Surface Release）推出原生 Electron 桌面應用，提供完整圖形化操作介面：

| 特性 | 說明 |
| ------ | ------ |
| 跨平台安裝 | v0.23.0：macOS 13+ Apple Silicon（簽章 + 公證 DMG）、Windows 10/11 64 位元（簽章 MSIX，需 Windows 11 22H2+；或 Microsoft Store）；官方發行流程已停止產出 Linux 桌面套件（Linux 可在 CLI 安裝後執行 `hermes desktop` 自行建置）；NSIS／MSI 安裝程式自 v0.22.0 起停用 |
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

```text
# 在 CLI／TUI／任何訊息平台輸入（Hermes 會逐一詢問所需欄位，確認後才建立排程）
/blueprint morning-brief
# 進階：直接帶入欄位值
/blueprint morning-brief time=08:00
```

> 💡 Blueprint 不是使用者自寫的 YAML 檔，而是官方（或外掛）提供的**參數化範本**；建立後即為一般的 Cron 工作，以 `hermes cron list` 檢視、`hermes cron edit` 修改。外掛提供的 Blueprint 以 `外掛名:範本名` 命名，無法覆蓋內建範本。

- **多入口統一**：Dashboard 表單 / CLI slash command / Messenger 對話 / Docs 目錄
- **自然語言排程**：「每週一早上」、「每隔 4 小時」等描述自動轉換
- **條件觸發**：可搭配 webhook 事件或檔案變更作為觸發條件
- **Dashboard 管理**：視覺化管理所有 Blueprint、執行歷史與結果

#### 1.4.23 Memory Atomic Batch Operations（v0.17.0+）

`memory` 工具支援原子批次操作，一次呼叫完成多項記憶異動：

```json
{
  "target": "user",
  "operations": [
    {"action": "add", "content": "偏好深色主題與繁體中文回覆"},
    {"action": "patch", "old_text": "phase-1", "content": "phase-2"},
    {"action": "remove", "old_text": "舊的部署主機名稱"}
  ]
}
```

> ⚠️ 動作只有 `add`／`patch`／`remove`，以 `content`／`old_text` 比對內容，沒有 `key`／`value`；`target` 必填（`memory` 或 `user`）。完整說明見 [3.3.3](#333-memory-atomic-batch-operationsv0170)。

- **以最終結果檢查容量**：字元上限只檢查整批套用後的結果，因此可以在同一批次中先刪減再新增
- **超限時回傳現有條目**：工具會回傳 `current_entries`，讓 Agent 以一個批次整理後重試
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
# ~/.hermes/config.yaml — 多密鑰來源設定範例
secrets:
  sources: [onepassword, bitwarden]     # 可選：同類型來源的先後順序（先者優先）
  onepassword:
    enabled: true
    service_account_token_env: OP_SERVICE_ACCOUNT_TOKEN
    env:                                # 明確映射（mapped）來源永遠優先於整包注入的 bulk 來源
      ANTHROPIC_API_KEY: "op://Engineering/Anthropic/credential"
  bitwarden:
    enabled: true
    project_id: "00000000-0000-0000-0000-000000000000"
```

> 💡 **優先序（官方規則）**：① `.env`／Shell 既有值預設勝出，除非該來源設 `override_existing: true`（Bitwarden 預設為 true）；② 有 `env:` 映射的來源勝過整包注入的來源；③ 同類型時依 `secrets.sources` 順序先者勝出，後到的宣告會在啟動時警告而非靜默覆蓋。

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
- **`hermes import-agent`**：一鍵將既有 Claude Code 或 Codex CLI 設定遷移至 Hermes（v0.23.0 起此指令由官方 `agent-importers` 外掛提供；核心另有 `hermes migrate <openclaw|claude-code|codex|cursor|grok-bot|openbot>`，缺外掛時會自動安裝）
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

# 交付長時間任務（回傳 run_id），之後以 run_id 輪詢狀態
hermes peer run research-box "整理本週 CVE 影響評估" --json
hermes peer status research-box <run_id>
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
- ⚠️ **預設值提高**：迭代上限 250、並行子代理 10 個——效能提升的同時**成本上限也同步放大**，企業應主動設限（見 [11.1.15](#11115-v0210-升級特別注意事項)）

#### 1.4.38 MCP Command Center 與 `hermes://` Deep Link（v0.21.0+）

分散在多處的 MCP 伺服器與目錄整併為單一 Desktop 管理頁面：

- **拖放匯入**設定、**背景健康檢查**自動偵測失效伺服器
- **Fleet 成本／用量疊層**：跨所有 MCP 伺服器的用量與花費一覽
- **`hermes://` deep link**：從網頁或文件一鍵觸發明確的伺服器安裝流程（安裝仍需使用者確認）
- v0.20.6 另將遠端 MCP 目錄擴充至 **50+ 伺服器**

#### 1.4.39 Agent 驅動的應用內瀏覽器（v0.21.0+）

Desktop 內建瀏覽器不再只是檢視器，而是 Agent 可直接操作的工具面——Agent 自行導航、點擊、讀取頁面內容；使用者可將頁面彈出至系統瀏覽器，並具備完整的連結右鍵選單。與 `browser` 工具集（v0.23.0 起只剩單一 `browser_exec` 工具，以 CDP 驅動 Chromium，見 [3.5.1](#351-內建-toolsets)）互補：前者供人機共視的互動式操作，後者供無頭自動化。

#### 1.4.40 CLI Power Wave（v0.21.0+）

```bash
# Ctrl+P 開啟模糊命令面板（等同 /palette）
/palette

/model                # 互動式篩選模型選擇器
/status               # 推理模式、待審批項目、context 用量一覽
```

- **狀態列即時指標**：cache-hit %、延遲、tokens／sec，各欄位可獨立開關
- **全域緊急停止**：一鍵中止所有進行中的工作
- **審批規則試算**：以 dry-run 方式測試審批規則會給出什麼判決，不必真的執行危險指令（v0.21.0 時名為 `hermes approval-check`，v0.23.0 為 `hermes approvals test "<指令>"`；`hermes approvals suggest` 可依歷史紀錄建議允許清單）
- **Terminal Pets（Petdex）**：`/pet`／`/hatch` 陪伴型終端寵物（趣味功能，企業環境可停用）
- **Ctrl+C 中斷修正**：移除 Kitty keyboard protocol，修正部分終端機無法中斷的問題

#### 1.4.41 `model_overrides` — 免等改版的模型參數覆寫（v0.21.0+）

上游 Provider 調整了 context window 或定價，但 Hermes 尚未發版更新目錄時，不必再等待：

```yaml
# ~/.hermes/config.yaml — 結構為 model_overrides.<provider>.<model id>
model_overrides:
  openrouter:
    some-vendor/new-model:
      context_window: 400000      # 正整數
      supports_vision: true
      supports_tools: true
      supports_reasoning: false
      model_family: claude        # 可選
    _default:                     # 可選：此 provider 下未列出模型的預設值
      context_window: 128000
```

> ⚠️ **更正**：`model_overrides` 只能覆寫**能力宣告**（三個 `supports_*` 布林值、`context_window`、`model_family`），**不能覆寫價格**；省略的欄位維持「未知」而非 `false`。查表優先序為：使用者 `model_overrides` → Provider 外掛宣告 → 官方目錄 → `_default`。

同時 v0.21.0 起，**以 pip 安裝的第三方模型 Provider 可透過 Python entry points 被自動探索**，無須改動 Hermes 本體程式碼。

> ⚠️ **變更管控提醒**：`model_overrides` 直接影響成本估算與 context 管理決策，屬於「繞過官方目錄」的機制，企業應將其納入設定檔的版本控管與審核流程（見 [9.7.6](#976-企業導入前風險檢查清單)）。

#### 1.4.42 穩定發行通道與統一套件管理器 PM（v0.21.7／v0.22.0+）

自 v0.21.6 起，官方以新的「穩定發行管線」產出 SemVer 版本：每個 `vX.Y.Z` 在發布前都要通過原始碼 CI、Docker、Nix、簽章 Desktop 建置，以及各作業系統的安裝與升級測試。對企業而言，最大的改變是**原始碼安裝預設只在已發布的 Release 之間移動**，不再逐 commit 追蹤 `main`。

```bash
hermes update --check                  # 只預覽，不做任何變更
hermes update                          # 依目前通道（預設 stable）升級到最新 Release
hermes update --set-channel main       # 改為追每一個 main commit（不建議用於正式環境）
hermes update --set-channel stable     # 改回只追 Release
hermes update --channel main           # 僅此次對 main 執行，不保存選擇
```

- **PM（Package Manager）**：安裝腳本只負責 clone 原始碼並取得經校驗的 `uv`，其餘依賴（釘選版的 Python 3.14、Node.js、npm、ripgrep、FFmpeg、Chromium、`cua-driver`）都交給 PM 依 `pm/lock.json` 安裝。PM 不會採用系統上任意版本的 Node.js。
- **通道設定位置**：寫在 `config.yaml` 的 `update.installs` 下，每個安裝各自記錄。

> ✅ **如何驗證**：執行 `hermes update --check`，輸出應顯示目前通道與最新 Release；執行 `hermes --version`，版本號應為 `vX.Y.Z` 格式。若顯示 `vunknown`，代表不是透過官方 git checkout 安裝（例如直接解壓 tarball），`hermes update` 將無法正常判斷版本。

#### 1.4.43 首次啟動引導、免費方案與 Connectors（v0.22.0+）

- **對話式 Onboarding**：在從未使用過 Hermes 的電腦上開啟 Desktop，會以簡短的設定對話取代設定畫面：一次一張卡片，詢問名字、主題色、版面、要連接的應用與外掛，最後推薦最多四個起手任務。這段引導使用免費試用模型執行。
- **Connectors**：Agent 可以透過 Nous Tool Gateway 直接在 Linear、Notion、Gmail 等託管應用內操作。第一次使用時在瀏覽器登入一次，同一回合內即可使用該應用的工具；不需要先有 Nous 帳號，Hermes 會建立只限 Connectors 的免費身分。
- **同一應用多個帳號**：可連接多個帳號（例如 Gmail `home` 與 `work`）。帳號名稱為 1–32 個小寫英數字或 `-`。**沒有預設帳號**：有兩個以上具名帳號時，每個工具呼叫都必須帶 `connector_alias`。Agent 永遠不會自行移除帳號。

```bash
hermes connectors list                 # 列出可用的 Connector 與已連接帳號
hermes connectors connect linear       # 在瀏覽器完成授權
hermes connectors accounts gmail       # 檢視某應用的所有帳號
hermes connectors rename gmail old-name --to work
```

> ⚠️ **企業治理**：Connectors 讓 Agent 以**使用者本人的身分**在 SaaS 內讀寫資料，資料流會經過 Nous 的託管基礎設施。導入前應確認資料分級與委外處理規範，必要時以 `hermes tools` 關閉相關工具集（見 [9.7 節](#97-風險評估與治理考量企業導入前必讀)）。

#### 1.4.44 一鍵 Local Models（v0.22.0+）

Hermes 可以完全在本機執行開源模型：不需要帳號、不需要 API Key，模型下載後也不需要網路。它會自動安裝並維護 llama.cpp（依硬體選擇 CPU／CUDA／Metal／Vulkan／ROCm 引擎），依 GPU 與記憶體為目錄中的每個模型評分，再挑選能放得下的最高品質版本。

```bash
hermes model        # 選「Local models」：列出依本機規格標價的目錄（★ 為推薦），安裝引擎、下載模型並設為預設
```

```yaml
# ~/.hermes/config.yaml — 無頭／CLI 環境的本機推理設定
local_runtime:
  enabled: true          # 隨 Hermes 啟動受管理的 llama-server
  backend: auto          # auto | cuda | metal | vulkan | hip | cpu
  detect_ports: [8081]   # 額外探測自行啟動的 llama-server（預設只探測 :8080）
model:
  provider: llamacpp
```

> ✅ **如何驗證**：執行 `hermes doctor`，並在對話中以 `/model` 確認目前模型列在「Local」群組；拔除網路後再送出一則訊息，應仍能正常回應。

#### 1.4.45 單一 Gateway 擁有所有對話（v0.22.0／v0.23.0）

- **v0.22.0**：每台機器只執行**一個**訊息 Gateway 與**一個** Desktop 後端，服務所有 Profile，不再一個 Profile 一個行程。各 Profile 仍保有自己的憑證、允許清單、Cron 與 Session；新建 Profile 不需重啟就能上線。`hermes update` 會在不衝突時自動把舊的 per-profile Gateway 併入。
- **v0.23.0**：過去 CLI、TUI、Desktop、編輯器（ACP）、訊息 bot 與 Cron 可能各自對同一個對話執行一份 Agent，導致訊息重複寫入或遺失。現在每台機器的 Gateway **擁有所有 Session**，其他介面一律以用戶端身分連上：在任何地方開啟的對話都是同一個對話、同一個佇列。

> ⚠️ **升級後不可回退**：新版 Gateway 一旦寫入 `state.db`，舊版本就無法再使用該資料庫。若要回退，只能還原升級前的快照或完整備份（詳見 [11.1.16](#11116-v0210--v0230-升級特別注意事項目前最新版本)）。

#### 1.4.46 Plugin Catalog 與自動更新（v0.22.0／v0.23.0）

Plugin Catalog 是**人工審核**的外掛目錄：v0.22.0 推出時有 600 項，v0.23.0 擴充至 1,050+ 項，並新增 **Verified** 層級，標示由該廠商自行開發的外掛（層級為 Official／Verified／Community）。

- 每個項目都釘選**經審核的 commit SHA**；作者推送新程式碼**不會**改變 Catalog 安裝的內容。
- 審核時會執行與安裝程式相同的安全掃描：判定為 `dangerous` 的項目不會收錄。
- 被下架的外掛列在 `removed.yaml` 中：無法安裝；已安裝的停止更新、無法啟用，載入時也會被拒絕。
- **安裝 ≠ 啟用**：安裝只是把檔案放到磁碟，仍需 `enable` 才會載入。

```bash
hermes plugins search memory               # 搜尋 Catalog
hermes plugins install honcho              # 安裝前會顯示宣告的工具／hooks／所需環境變數
hermes plugins enable honcho
hermes plugins update                      # v0.23.0：一次更新全部；會破壞設定的更新會被擱置
hermes plugins auto-update on              # 選擇性開啟自動更新（Catalog 與 git 外掛）
```

> ⚠️ Catalog 審核是**單一時間點**的人工審閱，不是安全稽核；Desktop 外掛（`desktop/plugin.js`）在 App 內**無沙箱**執行，權限等同 App 本身。企業應另建允許清單（見 6.9 節）。

#### 1.4.47 Webapp：瀏覽器中的 Desktop 工作區（v0.23.0）

Gateway 可以把完整的 Desktop 工作區（對話、Group Chats、外掛、設定、檔案樹、Git 檢視、終端機）提供給一般瀏覽器使用。**預設關閉**；它與 Web Dashboard 是兩回事。

```bash
hermes config set webapp.enabled true
hermes gateway restart
hermes webapp                 # 建置前端（必要時）、啟動 Gateway，並開啟一次性登入連結（60 秒內有效）
hermes webapp --status        # 檢查 Gateway 是否正在提供 Webapp，以及無法提供的原因
```

> ⚠️ **資安等級**：登入 Webapp 的使用者**可以用執行 Hermes 的 OS 帳號執行任意指令**。若要從其他機器存取，必須把 `webapp.host` 設為非 loopback 位址並啟用 Dashboard 登入閘門（區網／VPN 用帳密，對外網路用 OAuth/OIDC）；官方建議優先使用 SSH tunnel、Tailscale 或其他 VPN。詳見 [14.6 節](#146-webappv0230)。

#### 1.4.48 對話回溯 `/rewind` 與終端機圖片（v0.23.0）

- **`/rewind`**（或在空白輸入框連按兩次 `Esc`）：選擇較早的一則提示後，按 `Enter` 編輯並重送（重送時會移除該提示之後的所有內容），按 `f` 則從該點分岔出新 Session。原 Session 保持不變。
- **終端機圖片**：貼上的圖片或工具截圖會直接畫在對話中。kitty、Ghostty（CLI 與 TUI）以及 iTerm2、WezTerm、Konsole（CLI）顯示真實像素，其他終端機以色塊近似；VS Code 終端機在開啟圖片支援後可顯示完整解析度。
- **TUI 可在回合進行中執行 `/new`**：舊回合會在背景繼續完成。

#### 1.4.49 Group Chats 自主運作與 Bot Screen（v0.22.0／v0.23.0）

- **Bot Screen**（v0.22.0）：在 Linux Gateway 上執行的 bot 可以擁有自己的桌面，並由 Hermes Desktop 即時串流畫面。遇到登入、2FA 或 CAPTCHA 時，使用者可以接手畫面完成該步驟，再交還控制權。
- **Group Chats**（v0.23.0）：
  - 房間可以指定 lead bot 或啟用自動路由，替沒有點名任何人的訊息決定由誰回答。
  - Cron 工作可以把結果發到房間中；房間可保存「目的」與共享筆記。
  - bot 之間**不會再無止境地互相觸發**。
  - 每個 bot 會即時顯示自己正在做什麼，例如「scout · terminal · 7s」。

詳見 [第十五章](#第十五章bot-mode-與多-agent-群組協作v0210)。

#### 1.4.50 付費工具標價與花費上限（v0.23.0）

付費的 MCP 工具（例如 3D、影像生成）可以宣告每次呼叫的成本。審批提示會顯示該次呼叫的價格與本對話的累計花費；即將超過上限時一定會先詢問，**即使在 YOLO 模式或 `trust: full` 的伺服器也一樣**。在無人可回答的情境（Cron、`hermes chat -q`）中，超限呼叫會直接被拒絕。

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  renders:
    command: "render-mcp"
    trust: untrusted
    tool_costs:
      create_image: 20                                   # 每次約 20 點
      animate: {credits: [5, 20], note: "per animation"}  # 區間計價
    spend_limit: 100       # 每個對話的上限；0 或省略 = 不限
    cost_unit: credits
```

> ✅ **如何驗證**：在對話中連續呼叫 `create_image` 六次，第六次（累計 120 > 100）時，審批提示應只提供「Allow Once／Deny」兩個選項。若 `tool_costs` 格式錯誤，該伺服器會在啟動時被略過並記錄錯誤，不會靜默忽略預算設定。

#### 1.4.51 可插拔委派策略與子代理即時操控（v0.22.0／v0.23.0）

- **即時檢視**（v0.22.0）：執行中的子代理會常駐顯示在輸入框上方（CLI 按 `F6`、TUI 按 `Ctrl+T`、Desktop 側欄），包含任務、經過時間與即時逐字稿，並提供 Steer 與 Stop。`/stop` 可以停止背景子代理，並取回其部分成果。
- **委派策略**（v0.23.0）：`delegation.backend` 決定任務如何變成子代理。預設為 `default`；安裝官方 `advanced-delegation` 外掛後可改用 `model_map`（具名模型選單）或 `profile_routes`（每個子代理以某個 Profile 的身分執行），並以 `/delegation` 切換。

```yaml
# ~/.hermes/config.yaml（需先 hermes plugins install advanced-delegation）
delegation:
  backend: model_map
  backends:
    model_map:
      options:
        - name: fast
          description: "簡單查詢、格式轉換"
          provider: openrouter
          model: anthropic/claude-haiku-5.5
        - name: deep
          description: "架構分析、跨檔重構"
          provider: anthropic
          model: claude-opus-5-5
```

> ⚠️ **憑證共享**：把某個 Profile 列入 `profile_routes`，代表本 Profile 的子代理可以使用該 Profile 的憑證、`SOUL.md` 與終端政策。若所選後端不存在或無法執行，`delegate_task` 會**明確回報錯誤**，不會靜默改走預設路徑。

#### 1.4.52 精簡技能集與 Cron 控制（v0.23.0）

- **內建技能 58 → 44**：Word、PowerPoint、Excel 合併為單一 `microsoft-office` 技能。舊副本會留在磁碟上，直到手動移除。
- **`hermes curator lock <skill>`**：禁止 Agent 改寫該技能（即使在 YOLO 模式下）。
- **停止執行中的 Cron**：`hermes cron cancel <job>` 只停止**目前這一次**執行，`remove` 才會刪除整個工作。可用 `--grace-minutes` 設定每個工作在 Hermes 關機期間錯過的排程該如何補跑（`0` 表示不補跑）。

```bash
hermes curator lock release-checklist
hermes cron cancel nightly-triage
hermes cron edit market-open --grace-minutes 0
```

### 1.5 本章審查與驗證清單

本章是功能與版本總覽。審查 AI 依本章產出的「功能導入評估」或「版本差異說明」時，請逐項核對：

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 版本基準正確 | `gh api repos/NousResearch/hermes-agent/releases/latest --jq .tag_name` | 與文件宣稱的基準版本一致（本手冊為 `v0.23.0`） |
| 2 | 實際安裝版本 | `hermes --version` | 顯示 `vX.Y.Z`；若為 `vunknown`，代表非官方 git checkout 安裝 |
| 3 | 指令確實存在 | `hermes <指令> --help` | 不出現「is not a `hermes` command」；本章提到的 `hermes approval-check`、`hermes claw migrate` 等舊指令應改為 `hermes approvals test`、`hermes migrate openclaw` |
| 4 | 設定鍵有效 | `hermes config set <key> <value>` 後看是否出現 unknown-key 提示；或使用本手冊附錄 E 的 `check_doc.py` | 無「not a recognized config key」提示 |
| 5 | 外掛提供的功能已安裝 | `hermes plugins list` | `advanced-delegation`、`agent-importers`、記憶 Provider 等外掛已安裝**且已啟用** |
| 6 | 破壞性變更已涵蓋 | 對照 [11.1.16](#11116-v0210--v0230-升級特別注意事項目前最新版本) 的清單 | 提及瀏覽器工具時使用 `browser_exec`；提及 MCP Server 模式時使用 `hermes mcp-serve` |
| 7 | 數據附帶查證日期 | 檢查 Stars／貢獻者等數字旁是否有日期與來源 | 有日期與來源；官方宣稱的貢獻者人數與 API 實測口徑不同時，應加以註明 |

---

## 第二章：整體系統架構

### 2.1 架構設計概述

Hermes Agent 採用分層架構：從使用者介面一路往下到資料層，每一層都可以替換或擴充。v0.22.0 與 v0.23.0 對架構做了兩項根本調整，企業部署設計必須以此為前提：

1. **每台主機只有一個 Gateway**（v0.22.0）：單一 Gateway 行程同時服務該主機上的所有 Profile。各 Profile 的憑證、允許清單、Cron 與 Session 仍彼此隔離，但不再各自擁有一個 Gateway 行程。
2. **Gateway 擁有所有對話**（v0.23.0）：CLI、TUI、Desktop、Webapp、編輯器（ACP）、訊息 bot、API Server 與 Cron 全部改為 Gateway 的**用戶端**。Agent 的執行、審批等待、工具呼叫與 Session 儲存都集中在 Gateway 內，同一個對話在任何介面看到的都是同一份歷史、同一個佇列。

### 2.2 分層架構圖

以下為 v0.23.0 的邏輯架構。實線表示同步呼叫，虛線表示選用或外掛提供的元件。

```mermaid
graph TB
    subgraph CLIENTS["用戶端層（全部連到同一個 Gateway）"]
        CLI["CLI／TUI<br/>hermes、hermes --tui"]
        DESK["Hermes Desktop<br/>Electron，可同時連多台主機"]
        WEBAPP["Webapp<br/>瀏覽器版 Desktop 工作區（預設關閉）"]
        ACPC["ACP 編輯器<br/>VS Code／JetBrains／Zed"]
        MSG["訊息平台 Adapter<br/>Telegram／Slack／Teams／Discord 等 30+"]
        API["API Server<br/>OpenAI 相容 REST／SSE"]
        DASH["Web Dashboard<br/>管理介面"]
    end

    subgraph GWL["Gateway 層（每台主機一個，擁有所有 Session）"]
        GW["Gateway<br/>認證／路由／審批等待／配送台帳"]
        MUX["Profile 多工<br/>default、team-dev、team-ops…"]
        CRON["Cron 排程器<br/>Blueprints、/loop"]
    end

    subgraph AGL["Agent 層"]
        CORE["Agent Loop<br/>Prompt 建構／Provider 解析／工具分派"]
        SUB["子代理<br/>delegate_task，可即時導引"]
        SKILL["技能引擎<br/>44 內建 + Curator"]
        PLUG["Plugin 系統<br/>hooks／middleware／Provider／Desktop SDK"]
    end

    subgraph TL["工具層"]
        TERM["終端後端<br/>local／docker／ssh／modal／daytona／vercel_sandbox"]
        BROW["browser_exec<br/>CDP 驅動 Chromium"]
        FILES["檔案工具<br/>read_file／write_file／patch"]
        MCP["MCP Servers<br/>trust／tool_costs／spend_limit"]
        TGW["Nous Tool Gateway<br/>Connectors、雲端瀏覽器"]
        LOCALRT["Local Runtime<br/>受管理的 llama.cpp"]
    end

    subgraph DL["資料層（皆在 HERMES_HOME 之下）"]
        STATE[("state.db<br/>SQLite WAL：Session、配送台帳")]
        KB[("kanban.db<br/>每看板一個")]
        FSD[("檔案<br/>skills／MEMORY.md／USER.md／SOUL.md／logs")]
    end

    EXT["LLM Provider<br/>Anthropic／OpenAI／OpenRouter／Nous Portal 等"]
    MEMP["外部記憶 Provider<br/>Catalog 外掛：Honcho、Mem0 等"]

    CLI --> GW
    DESK --> GW
    WEBAPP --> GW
    ACPC --> GW
    MSG --> GW
    API --> GW
    DASH --> GW
    GW --> MUX
    CRON --> GW
    MUX --> CORE
    CORE --> SUB
    CORE --> SKILL
    CORE --> PLUG
    CORE --> TERM
    CORE --> BROW
    CORE --> FILES
    CORE --> MCP
    CORE -.-> TGW
    CORE --> EXT
    CORE -.-> LOCALRT
    PLUG -.-> MEMP
    GW --> STATE
    SUB --> KB
    SKILL --> FSD
    CORE --> FSD
```

> 💡 **讀圖重點**：v0.21.0 以前的架構圖常把 CLI 畫成「直接執行 Agent」，ACP 直接連到 Agent Core。v0.23.0 起這兩條路徑都改為經過 Gateway。審查 AI 產出的架構文件時，**若出現多個行程各自寫同一個 `state.db`，即為過時設計**。

### 2.3 各層級說明

#### 2.3.1 Presentation Layer（展示層）

| 組件 | 說明 | 連線方式 |
| ------ | ------ | ---------- |
| Terminal CLI / TUI | 完整 TUI（v0.11.0 Ink 重寫），支援多行編輯、斜線指令自動完成、串流工具輸出、OSC-52 剪貼簿、LaTeX 渲染、**v0.23.0 終端機內圖片顯示與 `/rewind`**；`hermes --native` 讓終端機自行處理捲動與搜尋 | 本機 Gateway 用戶端 |
| Hermes Desktop | Electron 原生桌面；v0.23.0 起可同時保持多個 Gateway（本機、SSH、遠端）連線，切換即時 | Gateway 用戶端（本機或遠端） |
| **Webapp**（v0.23.0） | 由 Gateway 直接在瀏覽器提供完整 Desktop 工作區，**預設關閉**；非 loopback 存取必須啟用登入閘門 | HTTP(S)，預設 `127.0.0.1:9120` |
| Web Dashboard | React SPA 管理介面：設定、Session、Skills、Gateway 管理、Plugin 擴充 Tab | HTTP（localhost 或經登入閘門） |
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
| iMessage via Photon Spectrum | 無需 Mac relay；以內建 Photon 平台外掛提供，`hermes photon setup --phone +886…` 設定、`hermes photon status` 檢查（v0.17.0 第 24 平台） | Photon Spectrum API |
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

Gateway 是 Hermes 的訊息路由與 Session 擁有者，負責：

- **Session 所有權**（v0.23.0）：每台主機一個 Gateway，擁有該主機上**所有** Session 的執行、審批等待與儲存；其他介面只是附加上來的檢視者。所有檢視者都關閉後，執行與待審批項目仍會在 Gateway 內繼續存在。
- **Profile 多工**（v0.22.0，`gateway.multiplex_profiles: true`）：單一 Gateway 服務所有 Profile。以 HTTP 進來的平台（Webhook、API Server）透過 `/p/<profile>/` URL 前綴區分 Profile。具名 Profile 預設**不能**自行啟動 Gateway（`hermes -p coder gateway start` 會以 exit 78 拒絕）。
- **認證與授權**：DM Pairing、`allowed_users` 白名單；`gateway.allow_all_users` 預設為 `false`。
- **Platform Allowlists**（v0.13.0）：`allowed_channels`／`allowed_chats`／`allowed_rooms`，適用於 Slack、Telegram、Mattermost、Matrix、DingTalk。
- **配送保證台帳**（v0.19.0，`gateway.delivery_ledger: true`）：Gateway 若在「產生回應」與「平台確認送達」之間當機，重啟後會自動補送。
- **Bot 迴圈防護**（`gateway.bot_loop_guard`）：預設在 300 秒內超過 20 個事件或 4 次轉發即冷卻 600 秒，防止 bot 之間互相觸發。
- **Scale-to-zero + Drain 協調**（v0.18.0）：代管 Gateway 閒置時自動休眠；重啟或遷移前會先排空進行中的對話。
- **Profile-based 路由**（v0.19.0，`gateway.profile_routes`）：單一共用 Bot Token 可依 Guild／頻道／討論串路由到不同 Profile。
- **智慧審批**（v0.19.0）：由獨立的 LLM 審查者判斷被標記的指令，成為危險指令的預設判斷機制。
- **看門狗**：`gateway.loop_watchdog` 與 `startup_watchdog` 偵測事件迴圈卡住或啟動逾時；`restart_loop_guard` 與 `respawn_storm` 防止反覆崩潰重啟。

#### 2.3.3 Agent Layer（代理層）

| 組件 | 職責 |
| ------ | ------ |
| Agent Loop | 核心循環：組合 System Prompt → 解析 Provider（`chat_completions`／`codex_responses`／`anthropic_messages` 三種 API 模式）→ 工具分派 → 評估 → 回應 |
| 子代理 | 隔離的子代理，支援平行與背景派工；v0.22.0 起可在 CLI（`F6`）／TUI（`Ctrl+T`）／Desktop 即時檢視、導引（Steer）與停止 |
| 委派策略 | `delegation.backend`：`default`，或由 `advanced-delegation` 外掛提供的 `model_map`／`profile_routes`（v0.23.0） |
| 技能引擎 | 載入技能、在複雜任務後自動建立新技能、以 `/learn` 手動萃取；由 Curator 定期維護（v0.23.0 新增 `lock`） |
| MoA | Mixture-of-Agents：多個參考模型平行推理，聚合器即時串流合成（v0.18.0 起為一級模型） |
| Plugin 系統 | 透過 hooks、middleware、Provider Profile、Desktop SDK slot 等公開介面擴充；Catalog 規則禁止外掛在執行期覆寫 Hermes 核心 |

#### 2.3.4 Memory Layer（記憶層）

| 類型 | 實作 | 用途 |
| ------ | ------ | ------ |
| 內建持久記憶 | `MEMORY.md`（`memory.memory_char_limit`，預設 2,200 字元）／`USER.md`（`memory.user_char_limit`，預設 1,375 字元） | 持久化知識與使用者偏好，不依賴外部服務。採「凍結快照」：本次對話寫入的內容，下次對話才會載入 System Prompt |
| Context Window | 模型的上下文視窗 | 當次對話；可用 `/compress` 手動壓縮，也有自動壓縮 |
| Session Search | SQLite FTS5（無 LLM，約 20ms；`sessions.cjk_fts: true` 支援中日韓） | 跨對話搜尋；v0.15.0 重建後速度大幅提升 |
| 外部記憶 Provider | **v0.22.0 起由 Plugin Catalog 安裝**：Honcho、Supermemory、Hindsight、Mem0、OpenViking、Holographic 等；ByteRover、RetainDB 仍為內建 | 語義搜尋、知識圖譜等進階場景；同時只能啟用一個（`memory.provider`），詳見 3.3 節 |
| 寫入審批 | `memory.write_approval`（預設 `false`） | v0.21.0 起，`AGENTS.md`、技能與記憶的寫入一律需要審批；可另外對記憶寫入加開審批 |

#### 2.3.5 Tool Layer（工具層）

Hermes 內建 **70+ 工具**，依 `tools/registry.py` 自我註冊。v0.22.0 起約 19 個罕用工具改由 **Tool Search** 延遲載入（Agent 需要時才搜尋並載入），每次呼叫送出的工具 Schema 因此大約減半。下表列出 v0.23.0 的**真實工具名稱**，可用 `hermes tools` 或官方 Tools Reference 核對：

| 類別（Toolset） | 主要工具 | 說明 |
| ------ | ------ | ------ |
| `terminal` | `terminal`、`process_manage`、`read_terminal`、`close_terminal` | 6 種內建後端：`local`／`docker`／`ssh`／`modal`／`daytona`／`vercel_sandbox`；Singularity 與 bubblewrap 沙箱為外掛 |
| `code_execution` | `execute_code` | 在沙箱中執行 Python 腳本，可透過 RPC 一次呼叫多個工具 |
| `file` | `read_file`、`write_file`、`patch`、`search_files` | 寫入後 Delta Lint 與 LSP 語義診斷；v0.23.0 開啟 LSP 時 `patch`／`write_file` 可在毫秒內回應 |
| `browser` | `browser_exec`、`browser_cdp`、`browser_dialog`、`browser_vault` | **v0.23.0 只剩 `browser_exec`** 一個主要驅動工具（browser-harness／CDP）；舊的 `browser_navigate`／`browser_click` 等 10 個工具已移除，Camofox 改為外掛 |
| `web` | `web_search`、`web_extract` | SearXNG、Brave、DDGS、Firecrawl 或 Nous Tool Gateway 等後端 |
| `x_search` | `x_search` | X（Twitter）搜尋 |
| `connections` | `manage_connections` | Connectors（v0.22.0）帳號管理 |
| `cronjob` | `cronjob_manage` | 排程管理（舊名 `cronjob`，仍相容） |
| `delegation` | `delegate_task` | 委派子代理；可指定 JSON Schema 驗證輸出 |
| `todo` | `todo_list` | 任務清單（舊名 `todo`，仍相容） |
| `memory`／`session_search`／`skills` | `memory`、`session_search`、`skill_manage`、`skill_view`、`skills_list` | 記憶、跨對話搜尋、技能管理 |
| `vision`／`image_gen`／`video`／`video_gen` | `vision_analyze`、`image_generate`、`video_analyze`、`video_generate` | 多模態 |
| `tts` | `text_to_speech` | 預設 Provider 為 `edge` |
| `computer_use` | `computer_use` | 以 `cua-driver` 驅動桌面 |
| `kanban` | `kanban_show`、`kanban_complete`、`kanban_block`… | 看板 Worker 用工具 |
| `clarify` | `clarify` | 向使用者提問（Telegram／Discord 有原生按鈕） |
| MCP | 動態註冊 | `mcp_servers.<name>`；可宣告 `trust`、`tool_costs`、`spend_limit` |

> ⚠️ **審查重點**：AI 產生的技能、提示或 `toolsets` 清單若仍出現 `browser_navigate`、`execute_command`、`cron_add`、`voice_synthesize` 等名稱，在 v0.23.0 中**不存在或已移除**，必須改成上表的名稱。

#### 2.3.6 Data Layer（資料層）

| 儲存 | 技術 | 存放內容 |
| ------ | ------ | ---------- |
| `state.db` | SQLite，預設 WAL（`database.journal_mode: wal`）；**單一寫入者**由 Gateway 擔任 | Session 歷史、訊息、配送台帳、Gateway 執行期紀錄 |
| `kanban/boards/<slug>/kanban.db` | 獨立 SQLite（每個看板一個） | 看板任務、Worker 心跳、稽核軌跡 |
| `cron/` | 檔案 | 排程定義、執行紀錄、per-job notepad |
| 檔案系統 | `HERMES_HOME`（預設 `~/.hermes/`；Windows 為 `%LOCALAPPDATA%\hermes`；Docker 為 `/opt/data`） | `config.yaml`、`.env`、Skills、`MEMORY.md`／`USER.md`、`SOUL.md`、logs、`profiles/<name>/` |
| 外部 API | HTTPS | LLM Provider、Tool Gateway、MCP 遠端伺服器 |

> ⚠️ **檔案系統要求**：WAL 依賴同一主機上的共享記憶體（`state.db-shm`）。若資料目錄位於 NFS、SMB 或 FUSE 等網路檔案系統，必須明確設定 `database.journal_mode: delete`。Docker Desktop／Podman on macOS 的 virtiofs 與 Windows 的 9p 掛載會被自動偵測；但**已存在的 WAL 資料庫不會被線上降級**，必須離線轉換（見 10.1 節）。

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
        Sub2->>Tools: write_file / patch / terminal
        Sub2-->>Main: 程式碼
    end

    Main->>Sub3: 測試驗證
    Sub3->>Tools: terminal（pytest）
    Sub3-->>Main: 測試結果

    Main->>Main: 整合、學習、技能封裝
    Main-->>User: 完成回報
```

**關鍵特性**：

- **隔離性**：每個子代理都有獨立的 Context Window，不會污染主 Agent。
- **摘要回傳**：子代理的結果以摘要回傳（`delegation.max_summary_chars`，預設 24,000 字元），不會把整段過程塞進主 Agent 的上下文。
- **並行與深度上限**：`delegation.max_concurrent_children` 預設 10，`max_spawn_depth` 預設 1（子代理不能再生子代理），`max_iterations` 預設 250。
- **Credential 共享**：預設共享主 Agent 的 Credential Pool；使用 `profile_routes` 時改用目標 Profile 的憑證。
- **可觀測**：每個委派都會寫入即時逐字稿 `<HERMES_HOME>/cache/delegation/live/<delegation_id>/task-<n>.log`，可用 `tail -f` 追蹤。

### 2.5 高可用與擴展性設計

v0.23.0 的擴展單位是「**主機**」，而不是「行程」。每台主機有一個 Gateway，擁有該主機 `HERMES_HOME` 中的 `state.db`。因此正確的擴展方式是**依團隊或用途分片到多台主機**，而**不是**在共享資料庫前放負載平衡器、同時跑多個副本。

```mermaid
graph TB
    subgraph EDGE["入口層"]
        RP["反向代理／零信任存取<br/>TLS + SSO（Dashboard／Webapp 登入閘門）"]
        CHAT["訊息平台<br/>每個 Bot Token 只綁定一台主機"]
    end

    subgraph HOSTA["主機 A：研發團隊"]
        GWA["Gateway A<br/>Profiles：team-dev、team-qa"]
        DBA[("本機磁碟 state.db<br/>WAL")]
        GWA --> DBA
    end

    subgraph HOSTB["主機 B：維運團隊"]
        GWB["Gateway B<br/>Profiles：team-ops、oncall"]
        DBB[("本機磁碟 state.db<br/>WAL")]
        GWB --> DBB
    end

    subgraph SHARED["共用服務（無狀態或外部）"]
        LLM["LLM Provider／內部 Model Gateway<br/>以 fallback_providers 實現 failover"]
        BAK[("備份儲存<br/>hermes backup → S3／NAS")]
        SECR["秘密管理<br/>Bitwarden／1Password"]
    end

    RP --> GWA
    RP --> GWB
    CHAT --> GWA
    CHAT --> GWB
    GWA --> LLM
    GWB --> LLM
    GWA -.-> BAK
    GWB -.-> BAK
    GWA -.-> SECR
    GWB -.-> SECR
    GWA <-.->|"hermes peer／A2A"| GWB
```

**企業級設計要點**：

1. **一台主機、一個 Gateway、一個狀態擁有者**：K8s 上請用 `replicas: 1` 搭配 `strategy: Recreate`（見 10.2 節），**不要**使用 RollingUpdate 或 HPA 讓兩個 Pod 同時開啟同一個 `state.db`。
2. **以分片取代副本**：依團隊、資料分級或地域把 Profile 分配到不同主機。主機之間以 `hermes peer`（Hermes 對 Hermes）或 A2A（跨廠商）協作。
3. **Model Failover**：可靠性應放在模型層：`fallback_providers` 加上 Credential Pool，主 Provider 失敗時自動切換（見 9.5 節）。
4. **快速復原優於熱備援**：定期執行 `hermes backup` 並異地保存，搭配 `hermes import` 還原，以 RTO／RPO 目標設計備份頻率（見 10.5 節）。
5. **Serverless 終端後端**：Daytona／Modal 後端閒置時自動休眠，適合突發性的重型運算。

> ❌ **反例（請勿採用）**：以 Nginx 負載平衡分流到三個 Hermes 實例，並共享 NFS 上的 `state.db` 或 PostgreSQL。Hermes 沒有 PostgreSQL 儲存後端；多行程同時寫入網路檔案系統上的 SQLite 會造成鎖定錯誤，甚至資料毀損。

### 2.6 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 每台主機只有一個 Gateway | `hermes gateway status`；`hermes -p <profile> gateway start` | 只有一個 Gateway 行程；具名 Profile 自行啟動會以 exit 78 被拒絕（除非刻意設定 `gateway.standalone: true`） |
| 2 | Profile 多工已啟用 | `hermes config get gateway.multiplex_profiles` | `true` |
| 3 | `state.db` 位於本機磁碟 | `hermes config path` 找出 `HERMES_HOME`，再以 `df -T <路徑>`（Linux）檢查檔案系統類型 | ext4／xfs／apfs／NTFS 等本機檔案系統；若為 nfs／cifs，`database.journal_mode` 必須為 `delete` |
| 4 | 資料庫健康 | `hermes doctor` | 沒有 WAL／journal mode 相關錯誤 |
| 5 | 工具名稱為現行名稱 | `hermes tools`；搜尋技能與提示中的 `browser_navigate`、`execute_command` 等舊名 | 只出現 2.3.5 表列的名稱 |
| 6 | 架構文件沒有多副本共享狀態 | 人工審查 AI 產出的部署圖 | 沒有「LB → 多個 Hermes → 共享 DB」的設計；K8s 為 `replicas: 1` + `Recreate` |
| 7 | 委派上限已評估 | `hermes config get delegation.max_concurrent_children` | 依成本政策調整（預設 10）；正式環境建議明確寫入設定，而不是依賴預設值 |

---

## 第三章：Hermes Agent 核心機制解析

### 3.1 Learning Loop（學習迴圈）

Learning Loop 是 Hermes 官方定位的核心差異化設計：Agent 會把完成任務的經驗封裝成可重用的技能，並在後續使用中持續修正。（「唯一具備自我改進能力」屬行銷說法，企業評估時應以實測為準。）

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

每個 Skill 是一個目錄，其中**必須**有一個 `SKILL.md`（大寫檔名，含 YAML frontmatter），並可附帶參考文件與輔助腳本。所有技能（內建、Hub 安裝、Agent 自建）都存放在同一個目錄 `~/.hermes/skills/`，以**分類子目錄**組織，而不是以來源區分：

```text
~/.hermes/skills/                  # 唯一的技能來源目錄（每個 Profile 各自一份）
├── software-development/          # 分類目錄
│   ├── test-driven-development/   # 內建技能（安裝或 hermes update 時播種）
│   │   └── SKILL.md
│   └── spring-security-audit/     # Agent 自建或使用者撰寫
│       ├── SKILL.md               # 主要指示（必要）
│       ├── references/            # 補充文件
│       ├── templates/             # 輸出範本
│       └── scripts/               # 技能可呼叫的輔助腳本
├── .hub/                          # Skills Hub 狀態
│   ├── lock.json                  # 來源 URL、內容雜湊、掃描結果
│   ├── quarantine/                # 安裝前隔離區
│   └── audit.log
└── .bundled_manifest              # 記錄已播種的內建技能
```

> 💡 **審查重點**：從 URL 或 GitHub 安裝的技能，只會複製 `SKILL.md` 與它**明確引用**的 `references/`、`templates/`、`scripts/`、`assets/`、`examples/` 檔案；Hermes 會先在隔離區掃描整包內容，並把來源、雜湊、掃描器版本與結果記錄在 `.hub/lock.json`。稽核時可直接檢查這個檔案。

#### 3.2.2 Skill 範例

```markdown
---
name: spring-security-audit
description: 掃描 Spring Boot 專案的依賴 CVE、注入風險與認證設定，產出分級報告
version: 1.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [security, java, spring]
    category: software-development
    requires_toolsets: [terminal, web]
    config:
      - key: spring_audit.severity_threshold
        description: 報告的最低嚴重度
        default: "medium"
        prompt: "最低回報嚴重度（low/medium/high）"
---

# Spring Security Audit

## When to Use
使用者要求檢查 Spring Boot／Spring Security 專案的安全性，或在 PR 合併前做安全審查時。

## Procedure
1. 讀取 `pom.xml` 或 `build.gradle`，列出所有依賴與版本。
2. 用 `web_search` 查詢各依賴的已知 CVE（優先 NVD、GitHub Advisory）。
3. 用 `search_files` 掃描 `src/`：SQL 字串串接、`@CrossOrigin` 未限制來源、硬編碼的密碼或 API Key。
4. 檢查 `SecurityFilterChain` 設定（CSRF、CORS、授權規則）。
5. 依 `spring_audit.severity_threshold` 過濾後，輸出「發現／嚴重度／檔案:行號／修正建議」表格。

## Pitfalls
- 不要把測試目錄中的假憑證當成真實洩漏；先確認路徑是否在 `src/test/`。
- CVE 版本範圍要逐一比對，不能只比對套件名稱。

## Verification
- 報告中每一項都附有檔案路徑與行號，可以人工點開核對。
- 執行 `mvn -q dependency:tree` 的結果與報告列出的依賴版本一致。
```

> ✅ **如何驗證技能格式**：`hermes skills inspect spring-security-audit` 可以顯示解析後的中繼資料；frontmatter 格式錯誤時，技能不會出現在 `hermes skills list` 中。技能宣告的 `config` 會存在 `config.yaml` 的 `skills.config` 下，`hermes config migrate` 會詢問尚未設定的值。

#### 3.2.3 技能管理指令

| 指令 | 說明 |
| ------ | ------ |
| `/skills` | 列出所有可用技能 |
| `/<skill-name>` | 執行特定技能，支援堆疊（如 `/github /test-driven-development`，兩者皆為 v0.23.0 內建技能） |
| `/learn <對象>`（v0.18.0） | 將目錄／URL／剛示範的操作萃取為可重用 Skill，依 `CONTRIBUTING.md` 標準撰寫 |
| `hermes skills browse\|search\|install\|inspect\|list` | 瀏覽、搜尋、安裝、檢視、列出技能 |
| `hermes skills check\|update\|uninstall` | 檢查更新、更新、解除安裝 |
| `hermes skills opt-out\|opt-in` | 停止／恢復在此 Profile 播種內建技能（寫入 `.no-bundled-skills` 標記；`opt-out --remove` 只刪除未修改過的內建技能） |
| `hermes skills tap add owner/repo` | 新增自訂 GitHub Tap 作為技能來源 |
| `hermes bundles list\|show\|create\|delete` | 管理 Skill Bundle（一個 Slash Command 載入多個技能） |
| `hermes curator status\|run\|pause\|resume\|pin\|unpin\|lock\|unlock` | 技能庫維護（見 3.7 節；`lock` 為 v0.23.0 新增，禁止 Agent 改寫） |
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

外部記憶為**單選式外掛**（每個 Profile 只能啟用一種，設定於 `memory.provider`），與內建 `MEMORY.md`／`USER.md` 並存互補。**v0.22.0 起，多數 Provider 已移出 Hermes 核心，改由各維護者透過 Plugin Catalog 發布**；`hermes update` 會自動替已設定這些 Provider 的 Profile 安裝對應外掛，名稱、設定與資料目錄都不變。

| Provider | 安裝方式（v0.23.0） | 儲存位置 | 費用模式 | 特點 | 工具數 |
| ---------- | ------ | ------ | ------ | ------ | ------ |
| 內建 | 無需安裝 | 本地檔案 | 免費 | `MEMORY.md` + `USER.md`，零依賴，2,200／1,375 字元上限 | - |
| Honcho | `hermes plugins install honcho`（Plastic Labs 維護） | 雲端或自架 | 自架免費／雲端付費 | 辯證式使用者建模、Session 範圍上下文注入 | 5 |
| Mem0 | `hermes plugins install mem0` | 雲端／自架 | 自架免費、雲端付費 | 伺服器端 LLM 事實萃取、去重 | 4 |
| Supermemory | `hermes plugins install supermemory` | 雲端或自架 | 自架免費、雲端付費 | 多容器隔離、Session 圖譜匯入 | 4 |
| Hindsight | `hermes plugins install hindsight` | 雲端或本地 | 本地免費、雲端付費 | 知識圖譜、`reflect` 跨記憶合成 | 3 |
| OpenViking | `hermes plugins install openviking` + 自架伺服器 | 自架 | 免費（AGPL-3.0） | 檔案系統式階層、分層載入 | 6 |
| Holographic | `hermes plugins install holographic` | 本地 SQLite | 免費 | HRR 代數、信任評分 | 2 |
| RetainDB | 內建（相依 `requests`） | 雲端 | $20／月 | Vector + BM25 + 重排序、差量壓縮 | 10 |
| ByteRover | 內建（需 `brv` CLI） | 本地預設／可選雲端 | 本地免費、雲端付費 | 壓縮前萃取、階層知識樹 | 3 |
| Memori | 外部套件 `hermes-memori` | Memori Cloud | 免費／付費 | 工具感知記憶、結構化回想 | 5 |

> ⚠️ **待確認事項**：官方 Memory Providers 文件一方面說 RetainDB 與 ByteRover「仍隨 Hermes 內建」，另一方面又說它們「於 2026-10-15 移出核心，獨立倉庫目前無人維護」。v0.23.0 原始碼的 `plugins/memory/` 中**仍包含**這兩者。企業若選用，應把「上游無人維護」列為風險（見附錄 E.4）。

> **選型建議**：個人／小型團隊優先使用內建方案（零依賴、零成本）；需要跨 Session 使用者建模選 Honcho；企業多租戶場景優先 Supermemory 或 RetainDB；重視資料主權可完全自架的選 OpenViking（AGPL-3.0）或 Holographic（純本地 SQLite，無任何外部依賴）；已通過 SOC 2 稽核要求的環境可考慮 ByteRover。

#### 3.3.2 記憶設定範例

```bash
# 建議做法：用互動式精靈選擇並設定 Provider（會提示安裝 Catalog 外掛）
hermes plugins install supermemory
hermes memory setup
hermes memory status        # 確認目前啟用的 Provider
```

```yaml
# ~/.hermes/config.yaml — 記憶相關設定（鍵名以 v0.23.0 DEFAULT_CONFIG 為準）
memory:
  memory_enabled: true        # false 會移除 memory 工具
  user_profile_enabled: true
  memory_char_limit: 2200
  user_char_limit: 1375
  nudge_interval: 10          # 每 10 輪提醒一次持久化
  write_approval: true        # 企業建議：非互動介面的記憶寫入需人工核准
  provider: supermemory       # 外部 Provider（需先安裝外掛）；空字串 = 僅用內建
```

> 💡 **Provider 專屬設定放在哪裡？** 外部 Provider 的金鑰與參數**不是**寫在 `memory.<provider>` 子鍵下：Honcho、Mem0、Hindsight、Supermemory 把設定存在 `$HERMES_HOME/` 中各自的設定檔，OpenViking 讀取各 Profile 的 `.env`。舊版文件中的 `memory.auto_save`、`memory.supermemory.containers` 都不是有效設定鍵；請以 `hermes memory setup` 產生設定。

#### 3.3.3 Memory Atomic Batch Operations（v0.17.0+）

v0.17.0 引入的 `memory` 工具批次操作，允許在單次工具呼叫中完成多項記憶異動。動作只有三種：`add`（新增）、`patch`（以 `old_text` 找到片段並以 `content` 取代）、`remove`（以 `old_text` 子字串比對刪除）；沒有 `read` 動作，因為記憶內容會在 Session 開始時自動注入 System Prompt。

```json
{
  "target": "memory",
  "operations": [
    {"action": "add", "content": "專案使用 Java 25 + Spring Boot 4.1，測試用 JUnit 6"},
    {"action": "patch", "old_text": "phase-1", "content": "phase-2（2026-11 上線）"},
    {"action": "remove", "old_text": "已淘汰的 Redis 叢集位址"}
  ]
}
```

**核心規則**：

- **`target` 必填**：`"memory"`（Agent 筆記）或 `"user"`（使用者側寫）。一個批次只能針對一個 target；若某個操作內的 target 與頂層不同，會在寫入前直接回錯。
- **容量檢查看最終結果**：字元上限只檢查整批套用後的結果。新增內容會超限時，工具會回傳 `current_entries` 並要求 Agent 以**一個**批次先刪減再新增。
- **寫入審批**：`memory.write_approval: true` 時，非互動介面的寫入會被暫存，需以 `/memory pending`、`/memory approve all` 核准。

> ⚠️ **更正**：舊版文件使用的 `{"action": "add", "key": ..., "value": ...}` 格式**不存在**；記憶項目沒有 key，是以內容子字串比對。

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
hermes tools                         # 互動式啟用／停用工具集
hermes tools list                    # 列出所有工具集與狀態
hermes tools enable browser          # 啟用瀏覽器工具集
hermes tools disable delegation      # 停用委派工具集
hermes tools list --platform telegram   # 檢視特定平台的工具集設定
```

下表為 v0.23.0 的核心 Toolset 與真實工具名稱（完整清單見官方 Toolsets Reference）：

| Toolset | 包含工具 | 備註 |
| --------- | --------- | ---------- |
| `terminal` | `terminal`、`process_manage`、`read_terminal`、`close_terminal` | `process` 已更名為 `process_manage`（舊名仍相容） |
| `file` | `read_file`、`write_file`、`patch`、`search_files` | 寫入後自動 Lint／LSP 診斷 |
| `code_execution` | `execute_code` | 以 Python 腳本批次呼叫工具 |
| `web` | `web_search`、`web_extract` | |
| `browser` | `browser_exec`、`browser_cdp`、`browser_dialog`、`browser_vault` | **v0.23.0 移除舊的 10 個 `browser_*` 工具** |
| `delegation` | `delegate_task` | |
| `cronjob` | `cronjob_manage` | 舊名 `cronjob` 仍相容 |
| `todo` | `todo_list` | 舊名 `todo` 仍相容 |
| `memory`／`session_search`／`skills` | `memory`、`session_search`、`skill_manage`、`skill_view`、`skills_list` | |
| `connections` | `manage_connections` | Connectors 與本機 MCP 目錄 |
| `kanban` | `kanban_show`、`kanban_complete`、`kanban_block`、`kanban_heartbeat` 等 | 供看板 Worker 使用 |
| `vision`／`image_gen` | `vision_analyze`、`image_generate` | |
| `video`／`video_gen` | `video_analyze`、`video_generate` | |
| `tts` | `text_to_speech` | 語音輸入（STT）由語音模式處理，不是工具 |
| `computer_use` | `computer_use` | |
| `clarify` | `clarify` | |
| 組合型 | `coding`、`debugging` 等 | 由多個 Toolset 組成的套組，例如 `coding` = file + terminal + web + skills + browser + … |

> ⚠️ **更正**：舊版文件中的 `core`、`cron`、`code`、`voice`、`automation` 等 Toolset 名稱，以及 `execute_command`、`browser_navigate`、`cron_add`、`voice_synthesize`、`blueprint_create` 等工具名稱，在 v0.23.0 中都不存在。Automation Blueprints 是以 `/blueprint` 斜線指令操作，不是工具。

#### 3.5.2 MCP（Model Context Protocol）擴展

```yaml
# ~/.hermes/config.yaml — MCP 伺服器定義在頂層 mcp_servers（以伺服器名稱為鍵的 map）
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
    trust: untrusted            # 具寫入能力的呼叫都要審批
  postgres:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-postgres", "postgresql://readonly@db:5432/app"]
```

> ⚠️ **更正**：舊版文件使用的 `mcp: servers: [- name: …]` 清單格式**不是**有效設定（`mcp` 區塊只放全域選項）。伺服器一律寫在 `mcp_servers.<名稱>` 下；也可以用 `hermes mcp add` 或 `hermes mcp install <目錄名稱>` 產生。

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
| Singularity | Container（**v0.23.0 起移為外掛**，曾使用者升級時自動安裝） | HPC 環境 | **不生效** |
| Vercel Sandbox | Vercel API | Serverless | **不生效** |

> **版本沿革**：v0.15.0 曾移除 Vercel Sandbox 後端（與 Vercel AI Gateway 一併下架），**v0.20.0 現代化重寫後重新引入**。企業若在 v0.15.0～v0.19.x 期間已遷移至 Docker／Daytona／Modal，可自行評估是否切回，非必要變更。
>
> ⚠️ **安全提醒**：雲端後端（Daytona／Modal／Vercel Sandbox／Singularity）**略過危險指令審批檢查**，官方文件明確說明其安全模型改為「沙箱本身即邊界」——選用這些後端前，務必確認沙箱之網路存取、憑證掛載範圍已依 9.1 節原則收斂。

**瀏覽器來源**（v0.23.0）：工具一律是 `browser_exec`，「瀏覽器從哪裡來」則是另一個選擇：

| 來源 | 說明 | 適用場景 |
| ------ | ------ | ---------- |
| 本機 Chromium（預設） | Hermes 啟動自己封裝的 Chromium（Chrome for Testing），headless，每個 Session 一個 | 一般網頁操作，免 API Key |
| 雲端瀏覽器 | Nous 訂閱、Browserbase、Browser Use、Firecrawl 或瀏覽器 Provider 外掛 | 免本機安裝、需要雲端 IP |
| Lightpanda | 輕量 headless 引擎（`browser.engine: lightpanda`） | 小型機器上的文字型瀏覽 |
| 自己的瀏覽器 | `/browser connect` 附加到執行中的 Chrome／Brave／Edge | 需要人機共視 |
| 真實設定檔 | 日常瀏覽器設定檔的受管理副本（含登入狀態，需明確開啟） | 需要既有登入的工作 |
| Camofox | 反偵測 Firefox，**v0.23.0 起為外掛**（曾使用者自動安裝） | 需要反偵測的場景 |

```yaml
# ~/.hermes/config.yaml — Docker 終端後端（v0.23.0 為扁平鍵 terminal.docker_*）
terminal:
  backend: docker
  docker_image: "python:3.13-slim"
  docker_env:
    PYTHONPATH: "/workspace"
  docker_volumes:
    - "./project:/workspace"
  docker_network: "none"          # 企業建議：預設無網路，需要時再開
browser:
  allow_private_urls: false       # 禁止瀏覽內網位址（SSRF 防護）
```

> ⚠️ **更正**：舊版文件的 `terminal.docker.image`／`terminal.docker.volumes` 巢狀格式不是有效設定鍵；正確為 `terminal.docker_image`、`terminal.docker_volumes`、`terminal.docker_env`。

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
# ~/.hermes/config.yaml — Tool Search 位於 tools.tool_search 之下
tools:
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

```text
# 對話中切換（格式為 /model [provider:]model）
/model anthropic:claude-sonnet-5-5
/model openrouter:deepseek/deepseek-v4-pro
/model nous:nvidia/nemotron-3-ultra:free   # Nous Portal 免費層
/model vertex:gemini-4-argon
/model xai:grok-4.5
/model claude-opus-5-5 --reasoning high   # v0.22.0：選模型時一併指定推理強度
/model custom:local:qwen                   # 具名自訂 Provider
/model @preset/my-team                     # OpenRouter 帳號預設組合

/model                                     # 開啟模型選擇器（可加星號、顯示訂閱剩餘額度）
/reasoning xhigh                           # 單獨調整推理強度：none/minimal/low/medium/high/xhigh/max/ultra
/moa                                       # 一次性套用預設 MoA 組合執行單一提示
```

```bash
hermes model              # 互動式選擇 Provider 與模型（含 Local models）
hermes moa list           # 列出可用的 MoA 預設組合
hermes moa configure      # 設定參考模型 + 聚合器
```

> **推理強度**（v0.19.0 新增 `max`／`ultra`）：以 `/reasoning <level>` 調整，加上 `--global` 會寫回設定檔；`max`／`ultra` 主要對應頂層推理模型。MoA 的每個參考模型槽位可以各自設定不同推理強度。模型名稱會隨 Provider 目錄更新，**實際可用名稱請以 `/model` 選擇器或 `hermes model` 列出的為準**。

#### 3.6.1 Credential Pool 與 Failover

```yaml
# ~/.hermes/config.yaml — 主模型 + 依序備援 + 輔助任務模型
model:
  provider: anthropic
  default: claude-sonnet-5-5

fallback_providers:              # 依序嘗試；每一項都必須同時有 provider 與 model
  - provider: openrouter
    model: anthropic/claude-sonnet-5.5
  - provider: nous
    model: nvidia/nemotron-3-ultra:free

fallback:
  min_switch_reset_seconds: 120  # 主 Provider 若在 120 秒內恢復就不切換（0 = 一律切換）

auxiliary:                       # 輔助任務各自設定，沒有全域的 auxiliary.provider
  compression:
    provider: nous
    model: nvidia/nemotron-3-ultra:free   # 免費層，適合摘要／壓縮
  vision:
    provider: openrouter
    model: google/gemini-3-flash
```

```bash
hermes fallback add          # 互動式新增備援 Provider
hermes fallback list
hermes auth add openrouter --api-key "$OPENROUTER_API_KEY"   # 加入 Credential Pool
hermes auth list
```

> ⚠️ **更正**：舊版文件的 `providers.primary`／`providers.fallback` 結構與頂層 `auxiliary.provider`／`auxiliary.model` 都不是有效設定。`providers:` 用來定義**自訂端點**（如 `providers.llamacpp.base_url`），備援要用 `fallback_providers`，輔助模型要用 `auxiliary.<任務>`（`compression`、`vision`、`title_generation`、`curator` 等 20 餘種）。
>
> **觸發條件**：429 限流與 500／502／503 錯誤會在重試用盡後切換；401／403 認證失敗則**立即**切換。若限流回應帶有重設時間，主 Provider 會被暫停到該時間為止；否則採 60 秒到 4 小時的指數退避。

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

> **最佳實踐**：企業部署建議設定至少 2 個 Provider（`model` + `fallback_providers`），並為壓縮、摘要等輔助任務指定低成本模型（例如 Nous Portal 免費層的 `nvidia/nemotron-3-ultra:free`）。這樣即使主 Provider 當機，Agent 仍可用備援持續運作。⚠️ 免費層模型可能有資料使用條款差異，涉及機敏資料前請先確認。

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
hermes curator run --dry-run          # 預覽本次會做的變更，不寫入
hermes curator run                    # 手動執行（同步）
hermes curator status                 # 狀態與排程
hermes curator usage --sort activity   # 依使用頻率列出技能（activity|recent|name）
hermes curator lock release-checklist # v0.23.0：禁止 Agent 改寫此技能
hermes curator rollback --list        # 列出可回復的備份
ls ~/.hermes/logs/curator/            # 每次執行一個時間戳目錄，內含 run.json 與 REPORT.md
```

#### 3.7.4 設定檔

```yaml
# ~/.hermes/config.yaml — Curator 設定在頂層 curator（鍵名以 v0.23.0 DEFAULT_CONFIG 為準）
curator:
  enabled: true
  interval_hours: 168        # 執行間隔（預設 7 天）
  min_idle_hours: 2          # 使用者閒置多久後才執行
  stale_after_days: 14       # 多久未使用視為不活躍
  archive_after_days: 30     # 不活躍多久後歸檔
  consolidate: false         # v0.17.0：LLM 合併／精煉改為選用
  backup:
    enabled: true            # 每次變更前備份，可 hermes curator rollback
    keep: 2
auxiliary:
  curator:                   # 若開啟 consolidate，可在此指定低成本模型
    provider: openrouter
    model: google/gemini-3-flash
```

> ⚠️ **更正**：舊版文件的 `auxiliary.curator.enabled`／`interval_days`／`min_quality_score`／`max_skills`／`protect_pinned` 都不是有效設定。`auxiliary.curator` 只用來指定 Curator 使用的**模型**；行為設定在頂層 `curator:`。

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

### 3.12 本章審查與驗證清單

審查 AI 依本章產出的技能、設定或架構說明時，請逐項核對：

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 技能檔案格式 | `hermes skills inspect <name>`；`hermes skills list` | 技能會出現在清單中；`SKILL.md` 有 `name`／`description` frontmatter |
| 2 | 技能沒有危險內容 | `hermes skills audit`；檢查 `~/.hermes/skills/.hub/lock.json` 的 findings | 沒有 `dangerous` 判定；外部來源都有雜湊與來源 URL |
| 3 | 記憶 Provider 已安裝且啟用 | `hermes plugins list`、`hermes memory status` | `memory.provider` 指名的外掛為 enabled；status 顯示同一個 Provider |
| 4 | 工具與 Toolset 名稱為現行名稱 | `hermes tools list`；在技能與提示中搜尋 `browser_navigate`、`execute_command`、`cron_add` | 只出現 3.5.1 表列名稱 |
| 5 | MCP 設定位置正確 | `hermes mcp list`；`hermes config get mcp_servers` | 伺服器位於 `mcp_servers.<名稱>`，不是 `mcp.servers` |
| 6 | 備援設定可運作 | `hermes fallback list`；暫時把主 Provider 金鑰改為無效值，送出一則訊息 | 回覆來自 `fallback_providers` 的第一項；恢復金鑰後回到主 Provider |
| 7 | Curator 不會改寫關鍵技能 | `hermes curator run --dry-run`；對關鍵技能執行 `hermes curator lock <name>` | dry-run 清單不含被鎖定的技能；`~/.hermes/logs/curator/<時間戳>/REPORT.md` 可供稽核 |
| 8 | 所有 YAML 範例都是有效設定鍵 | 對每個鍵執行 `hermes config set <key> <value>`，或使用附錄 E 的 `check_doc.py` | 沒有「not a recognized config key」提示 |

---

## 第四章：安裝與環境建置

### 4.1 系統需求

| 需求項目 | 最低要求 | 建議配置 |
| ---------- | ---------- | ---------- |
| 作業系統 | Linux／WSL2（x86_64、aarch64）、macOS（Apple Silicon）、Windows 10／11（x86_64、aarch64）、Android（Termux aarch64，Tier 2） | Ubuntu LTS 最新版／macOS 14+（Apple Silicon）／Windows 11 22H2+ |
| Python | **3.14**（由 PM 自動提供並釘選版本，免手動安裝；`pyproject.toml` 的 `>=3.11,<3.15` 範圍只是讓舊環境能執行升級程式，**不代表**支援以 3.11–3.13 執行） | 交給 PM 管理 |
| Node.js | 由 PM 依 `pm/lock.json` 提供釘選版本，**不採用系統上的 Node.js** | 交給 PM 管理 |
| Git、curl、tar、SHA-256 工具 | POSIX 安裝腳本必要；Windows 缺 Git 時會自動取得釘選版的 Git for Windows | 最新版 |
| glibc Linux 額外套件 | `libatomic1`（apt／zypper）／`libatomic`（dnf／yum／apk）／`gcc-libs`（pacman）；安裝程式與 `hermes update` 會嘗試自動安裝 | — |
| 記憶體 | 1 GB（不使用瀏覽器工具） | 2–4 GB（啟用瀏覽器工具至少 2 GB；Local Models 依模型而定） |
| 磁碟空間 | 500 MB（資料目錄） | 2 GB+（隨 Session 與技能成長；Local Models 另計） |
| 網路 | 可連接 LLM API（Local Models 下載後可完全離線） | 穩定連線 |
| LLM Context Window | **最低 64,000 tokens**（低於此門檻的模型會在啟動時被拒絕） | 128K+ |
| Desktop App | macOS 13+（Apple Silicon）、Windows 10／11 64 位元（MSIX 需 Windows 11 22H2+） | — |

> ⚠️ **macOS 僅支援 Apple Silicon**：官方不建置、也不測試 Intel macOS 的 Desktop 套件，也拒絕相關 PR。Intel Mac 只能安裝 CLI 後執行 `hermes desktop` 自行建置，或改用 Docker、雲端或 Linux VM。
>
> 🪟 **Windows**：為 Tier 1 平台。`install.ps1` **不需要系統管理員權限**，會安裝到 `%LOCALAPPDATA%\hermes\` 並加入使用者 PATH；Desktop 為簽章 MSIX（App Installer 或 Microsoft Store）。少數功能在原生 Windows 上仍不可用，需要完整 Linux 工具鏈時可選擇 WSL2。
>
> 📱 **Android**：只支援 aarch64 的 Termux，**透過官方簽章 APT 套件庫安裝**（`pkg install hermes-agent`），不是 `install.sh`。此套件預設不隨每次 Release 建置，可能落後最新版本。

#### 4.1.1 平台支援層級（Platform Support Tiers）

官方把支援平台分為三個層級。**層級同時決定了官方認可的安裝管道**：不在對應管道之列者，即使技術上可行也不受支援。

| 層級 | 平台（OS／架構） | 官方安裝管道 | 說明 |
| ------ | ------ | ------ | ------ |
| **Tier 1（完整支援）**<br>官方承諾盡力不破壞安裝與更新 | macOS（僅 Apple Silicon） | Hermes Desktop（簽章 + 公證）、`install.sh` | — |
| | Windows 10／11（x86_64、aarch64） | `install.ps1`、MSIX Desktop（需 Windows 11 22H2+）、Microsoft Store | 見 4.3 節 |
| | Linux／WSL2（x86_64、aarch64） | `install.sh` | 以最新 Ubuntu 與 WSL2 為測試基準；**官方發行流程已停用 Linux 桌面套件** |
| | Docker 容器（x86_64、aarch64） | `docker pull nousresearch/hermes-agent` | 容器內**不支援 `hermes update`**，升級須重新拉取映像 |
| **Tier 2（盡力支援）**<br>官方明示可能於改版時中斷 | Nix（macOS／Linux／NixOS） | Nix flake 與 NixOS module | 「不再是明確支援的安裝路徑」；由 Nix 自行負責執行環境與更新 |
| | Android／Termux（aarch64） | 簽章 APT 套件庫 | 預發行套件；只有以 `--with termux` 發行的版本才會更新 |
| **明確不支援**<br>相關 PR 將被拒絕 | AUR、Intel macOS 的 Desktop 套件、非 aarch64 的 Termux、PyPI（`pip install`／`uv tool install`）、Homebrew | — | PyPI 與 Homebrew 已於 v0.20.0 終止，見 4.2.3 節 |

#### 4.1.2 安裝目錄結構

| 安裝方式 | 程式碼路徑 | CLI 進入點 | 預設資料路徑（`HERMES_HOME`） |
| ------ | ------ | ------ | ------ |
| POSIX 安裝腳本 | `~/.hermes/hermes-agent/` | `~/.local/bin/hermes` | `~/.hermes/` |
| Windows 安裝腳本 | `%LOCALAPPDATA%\hermes\hermes-agent\` | `%LOCALAPPDATA%\hermes\bin\` | `%LOCALAPPDATA%\hermes\` |
| Desktop 套件 | App 套件內 | 套件內啟動器；Windows 執行別名 | 平台預設資料目錄 |
| Docker | `/opt/hermes/`（root 擁有、執行期唯讀） | 映像 entrypoint 與 `hermes` shim | 掛載的 `/opt/data/` |
| Termux APT | `$PREFIX/lib/hermes-agent/` | `$PREFIX/bin/` 下的符號連結 | `~/.hermes/` |

- `HERMES_HOME` 決定使用者資料的位置。POSIX 腳本的 `--dir` 可獨立指定原始碼位置；Windows 則提供 `-HermesHome` 與 `-InstallDir`。
- **以 root 執行 POSIX 腳本不會改用 FHS 路徑**（例如 `/usr/local`），而是使用 root 的家目錄，除非明確指定原始碼路徑。服務帳號安裝請參考官方「Non-Sudo / System Service User Installs」。
- **不要刪除資料目錄來「修復」安裝**：程式與資料的生命週期是分開的。

### 4.2 快速安裝（Linux / macOS / WSL2）

#### 4.2.1 一鍵安裝

```bash
# 一鍵安裝：clone 原始碼、取得經校驗的 uv，再由 PM 安裝釘選版 Python／Node.js／ripgrep／FFmpeg／Chromium
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 重新載入 Shell 環境
source ~/.bashrc    # Bash 使用者（Zsh 使用者改為 source ~/.zshrc）

# 驗證安裝
hermes --version
hermes doctor
```

常用安裝選項（以 `bash -s --` 傳遞）：

```bash
# 無人值守安裝（CI／映像建置）：略過需要互動的步驟
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --non-interactive

# 不安裝瀏覽器與 computer-use 工具（伺服器環境常用）；之後可用 hermes pm install chromium 補裝
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --skip-browser --skip-computer-use

# 追蹤 main 而非最新穩定版（不建議用於正式環境）
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --channel main
```

> 💡 **安裝紀錄**：在終端機上執行時，每個步驟只顯示一行狀態，git、uv 與建置的完整輸出寫入資料目錄下的 `logs/install.log`；失敗時會印出最後幾行與日誌路徑。在 CI 中（設有 `CI` 或 `GITHUB_ACTIONS`）、輸出被導向，或使用 `--verbose`／`HERMES_INSTALL_VERBOSE=1` 時，則改為完整串流輸出。

#### 4.2.2 開發者安裝（從原始碼）

官方**不支援**建置 wheel 或 sdist（執行 `pip install .` 會直接拋出 `RuntimeError: Building wheels or sdists for hermes-agent is not supported`），開發時必須使用 editable install：

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
git checkout v0.23.0          # 正式評估請釘選 Release tag
source ./activate             # 官方開發環境腳本（PowerShell：. .\activate.ps1）
hermes --version              # 應顯示 v0.23.0
```

> ⚠️ **實測紀錄（本手冊驗證環境）**：從 GitHub tarball（沒有 `.git`）以 `uv pip install -e` 安裝時，`hermes --version` 顯示 `vunknown`，因為版本號取自 git tag。此外，`uv pip install -r` 會因 `pillow` 版本衝突而失敗，因為上游依賴 `uv.lock` 中的 override，必須改用 `uv export --frozen` 搭配 `--no-deps` 安裝。詳見附錄 E.3。

#### 4.2.3 已停用安裝管道（Homebrew／PyPI／pip）

> ⚠️ **v0.20.0 起正式停用**：Homebrew（`brew install hermes-agent`）與 PyPI／pip wheel（`pip install hermes-agent`，原為 v0.14.0 新增）兩種安裝管道，官方文件已明確列為「**不支援，相關 PR 將被拒絕**」。企業若仍在維護參照舊安裝方式的內部套件庫，須改用官方目前支援的管道：
>
> 1. **安裝腳本**（`install.sh`／`install.ps1`，見 4.2.1、4.3.2）
> 2. **Desktop 套件**（macOS DMG、Windows MSIX／Microsoft Store）
> 3. **Docker**（見 4.4 節；容器內**不支援 `hermes update`**，須改為重新拉取映像）
> 4. **Nix**（見 4.5 節；Tier 2 盡力支援）
> 5. **Termux APT**（Android aarch64）
>
> 既有透過 Homebrew／pip 安裝的環境不會自動遷移，請規劃一次性改用上述管道重新安裝，再以 `hermes import` 還原備份。

### 4.3 Native Windows 安裝

Windows 為 Tier 1 平台，提供 Desktop 套件與 PowerShell CLI 兩種方式。

#### 4.3.1 Desktop App 安裝

1. 前往 [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/) 下載 Windows 的 `.appinstaller`，以 Windows App Installer 開啟。它會安裝簽章的 MSIX bundle，並記錄更新來源；也可以改從 Microsoft Store 安裝（兩者的更新所有權不同）。
2. 系統需求：Windows 11 22H2 或更新版本、64 位元（x64／ARM64）。**v0.22.0 起 NSIS／MSI 安裝程式已停用**。
3. 更新方式：MSIX 透過 Desktop 的 Update 控制與 App Installer；Store 版由 Microsoft Store 更新。

#### 4.3.2 PowerShell CLI 安裝

```powershell
# 一般使用者權限即可（不需要系統管理員）
iex (irm https://hermes-agent.nousresearch.com/install.ps1)

# 帶選項安裝（例如無人值守 + 追蹤 main）
& ([scriptblock]::Create((irm https://hermes-agent.nousresearch.com/install.ps1))) -NonInteractive -Channel main

# 驗證（請開啟新的終端機，讓使用者 PATH 生效）
hermes --version
```

#### 4.3.3 注意事項

| 項目 | 說明 |
| ------ | ------ |
| **安裝位置** | `%LOCALAPPDATA%\hermes\`（程式碼、資料、`bin\`），自動加入使用者 PATH |
| **背景服務** | `hermes gateway install` 在 Windows 上使用「排程工作」，並以啟動資料夾作為備援，**不需要管理員權限** |
| **Desktop** | 簽章 MSIX，需 Windows 11 22H2+；macOS 13+ 與 64 位元 Windows 為 Electron 44 的最低需求（v0.23.0） |
| **路徑轉換** | ACP Adapter 支援 Windows cwd → WSL 路徑自動轉換 |
| **WSL2** | 需要完整 Linux 工具鏈（例如 Docker 終端後端）時建議使用 |

> **企業建議**：一般開發者使用 MSIX Desktop 即可；CI／CD 與需要 Linux 工具鏈的情境使用 WSL2 或 Docker。企業可透過 Intune 等工具散佈 MSIX 套件。

### 4.4 Docker / Podman 部署

官方映像發布在 Docker Hub 的 **`nousresearch/hermes-agent`**（amd64 與 arm64）。所有使用者資料（設定、API Key、Session、技能、記憶）都存放在掛載到容器內 **`/opt/data`** 的單一目錄；映像本身是無狀態的。

| 映像標籤 | 意義 |
| --- | --- |
| `latest`／`stable` | 通過穩定發行閘門的映像 |
| `main` | 由 main 分支建置的開發版映像（不建議正式環境使用） |
| `X.Y.Z` | 指定版本的穩定映像；需要完全固定時請使用 digest |

#### 4.4.1 使用官方 Docker Image

```bash
# 1) 第一次：建立資料目錄並執行設定精靈（會把 API Key 寫入 ~/.hermes/.env）
mkdir -p ~/.hermes
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent:0.23.0 setup

# 2) 以背景 Gateway 模式執行（容器內由 s6-overlay 監督，崩潰會自動重啟）
docker run -d \
  --name hermes \
  --restart unless-stopped \
  --memory=4g --cpus=2 \
  -v ~/.hermes:/opt/data \
  -p 127.0.0.1:8642:8642 \
  nousresearch/hermes-agent:0.23.0 gateway run

# 3) 互動式 CLI（附加到同一個容器）
docker exec -it hermes hermes
```

> ⚠️ **實務注意**：
>
> - 埠號 `8642` 是 Gateway 的 OpenAI 相容 API Server 與健康檢查端點；若只使用聊天平台可以不對外開放。上例綁定在 `127.0.0.1`，避免直接暴露到外部網路。
> - `docker exec` 會自動降權為 `hermes` 使用者；`/opt/hermes` 安裝樹在執行期為 root 擁有且唯讀，Agent 無法修改核心程式碼。
> - 部分 VPS 的瀏覽器式主控台會把 `:`、`@` 等字元傳錯，請改用 SSH 貼上指令。
> - **Dashboard in Docker**：加上 `-e HERMES_DASHBOARD=1` 並開放 `9119` 埠，Dashboard 會以附屬行程啟動。

#### 4.4.2 自建衍生映像（Derived Image）

官方建議**以官方映像為基底**加裝工具，而不是從 `python:*-slim` 自行組裝。後者需要自行處理 PM、釘選版 Node.js、s6-overlay 與權限模型，容易與官方行為不一致。

```dockerfile
# Dockerfile — 在官方映像上加裝企業內部工具
FROM nousresearch/hermes-agent:0.23.0

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends jq postgresql-client \
    && rm -rf /var/lib/apt/lists/*
# 保留 root entrypoint；s6 會在執行期自動降權為 hermes 使用者
```

```bash
docker build -t corp/hermes:0.23.0-1 .
docker run -d --name hermes --restart unless-stopped \
  -v ~/.hermes:/opt/data -p 127.0.0.1:8642:8642 \
  corp/hermes:0.23.0-1 gateway run
```

> 💡 每次上游發布新版時，都要重新建置衍生映像。單純安裝 npm 或 Python 工具時，可在容器內改用 `npx`／`uvx`，不必建置新映像。

#### 4.4.3 Docker Compose（企業部署）

v0.22.0 起官方建議**一個容器、多個 Profile**（由容器內的 s6 為每個 Profile 監督 Gateway 槽位），而不是一個 Profile 一個容器；這樣只有一份映像與快取，備份也只需處理一個目錄。

```yaml
# docker-compose.yml
services:
  hermes:
    image: nousresearch/hermes-agent:0.23.0
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "127.0.0.1:8642:8642"   # Gateway API Server
      - "127.0.0.1:9119:9119"   # Dashboard（需 HERMES_DASHBOARD=1）
    volumes:
      - hermes-data:/opt/data   # 具名 volume：位於 Docker VM 的原生檔案系統，WAL 可正常運作
    environment:
      - HERMES_DASHBOARD=1
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: "2.0"

volumes:
  hermes-data:
```

```bash
docker compose up -d
docker compose logs -f
docker exec hermes hermes profile create team-ops   # 新增 Profile（s6 自動註冊其 Gateway 槽位）
```

> ⚠️ **`state.db` 檔案系統要求**：在 macOS（Docker Desktop／Podman／OrbStack 的 virtiofs）或 Windows Docker Desktop（9p／drvfs）上以 bind mount 掛載 `~/.hermes` 時，SQLite 的 WAL 模式無法跨 VM 邊界正確共享記憶體。新建的資料庫會自動改用 `DELETE` journal mode，但**既有的 WAL 資料庫不會被線上降級**，必須停止所有行程後離線轉換。正式環境請優先使用上例的**具名 volume**。

### 4.5 Nix 安裝（Tier 2）

> ⚠️ Nix 自 v0.22.0 起「**不再是明確支援的安裝路徑**」（盡力支援）：執行環境與更新由 Nix 負責，`hermes update` 不適用。

```bash
# 直接執行（不安裝）
nix run github:NousResearch/hermes-agent -- setup
nix run github:NousResearch/hermes-agent -- --tui

# 安裝到使用者 profile（之後 hermes、hermes-agent、hermes-acp 皆在 PATH 上）
nix profile install github:NousResearch/hermes-agent

# Desktop（Nix 建置）
nix run github:NousResearch/hermes-agent#desktop
```

```nix
# /etc/nixos/flake.nix — 在 NixOS 系統 flake 中加入套件
{
  inputs.hermes-agent.url = "github:NousResearch/hermes-agent/v0.23.0";

  outputs = { self, nixpkgs, hermes-agent, ... }: {
    nixosConfigurations.myhost = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        ({ pkgs, ... }: {
          environment.systemPackages = [ hermes-agent.packages.x86_64-linux.default ];
        })
      ];
    };
  };
}
```

官方另提供宣告式 NixOS module 與 container mode，細節請參考官方 Nix & NixOS Setup 文件。

### 4.6 設定 API Key

#### 4.6.1 初始設定精靈

```bash
hermes setup              # 完整設定精靈（Provider → API Key → 模型 → 工具 → 記憶 → 訊息平台）
hermes setup --portal     # 最快路徑：登入 Nous Portal、設為 Provider 並開啟 Tool Gateway
hermes setup --quick      # 精簡流程
hermes setup --non-interactive   # 無人值守（搭配預先準備好的 .env／config.yaml）
```

v0.22.0 起，在新電腦首次開啟 Desktop 時會改為**對話式 Onboarding**，以免費試用模型引導完成設定。`hermes setup` 也會偵測 `~/.openclaw`、`~/.claude`、`~/.codex`、`~/.cursor` 等既有 Agent 設定，並詢問是否匯入。

#### 4.6.2 環境變數設定

`~/.hermes/.env`（Windows 為 `%LOCALAPPDATA%\hermes\.env`；Docker 為 `/opt/data/.env`）存放憑證。**不要**把金鑰寫進 `config.yaml`：

```bash
# ~/.hermes/.env
# === LLM Provider（至少一個；也可完全使用 OAuth 或 Local Models）===
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
OPENAI_API_KEY=sk-xxxxxxxxxxxxx
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxx
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxx        # Google AI Studio（亦接受 GOOGLE_API_KEY）
XAI_API_KEY=xai-xxxxxxxxxxxxx

# === 訊息平台 ===
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghIJKLmnoPQRSTuvwxyz
TELEGRAM_ALLOWED_USERS=123456789         # 逗號分隔；未設定時陌生人無法使用
DISCORD_BOT_TOKEN=your-discord-bot-token
SLACK_BOT_TOKEN=xoxb-your-slack-token
SLACK_APP_TOKEN=xapp-your-socket-mode-token

# === API Server（Gateway 的 OpenAI 相容端點）===
API_SERVER_KEY=change-me-to-a-long-random-string

# === MCP 伺服器使用的憑證（由 mcp_servers.<name>.env 以 ${VAR} 引用）===
GITHUB_TOKEN=ghp_xxxxxxxxxxxxx
```

> 🔐 **企業建議**：正式環境改用 Bitwarden／1Password 秘密來源（`hermes secrets bitwarden setup`），`.env` 只保留 bootstrap token。`.env` 檔案權限應為 `0600`。

#### 4.6.3 Nous Portal 登入

```bash
hermes setup --portal                 # 一步完成：登入 + 設為 Provider + 開啟 Tool Gateway
hermes portal                         # 等同 hermes auth add nous --type oauth（登入並選擇 Nous 模型）
hermes auth add nous --type oauth --no-browser   # SSH／無瀏覽器環境：顯示裝置碼
hermes portal status                  # 檢查訂閱與 Tool Gateway 狀態
```

> 💡 Nous Portal 提供免費層模型（例如 `nvidia/nemotron-3-ultra:free`），適合評估與輔助任務；付費訂閱另含 Tool Gateway（網路搜尋、影像生成、TTS、雲端瀏覽器）。⚠️ 舊版文件中的 `hermes auth login nous` 指令**不存在**。

### 4.7 設定檔說明

#### 4.7.1 主設定檔

以下是可直接使用的企業基準設定。所有鍵都已用 v0.23.0 官方驗證器（`hermes config set` 使用的 `_validate_config_key`）逐一檢查：

```yaml
# ~/.hermes/config.yaml — v0.23.0 企業基準設定

# === 模型 ===
model:
  provider: anthropic
  default: claude-sonnet-5-5
fallback_providers:
  - provider: openrouter
    model: anthropic/claude-sonnet-5.5

# === 輔助任務模型（壓縮／Vision 等，各自設定）===
auxiliary:
  compression:
    provider: openrouter
    model: google/gemini-3-flash

# === 記憶 ===
memory:
  memory_enabled: true
  write_approval: true         # 非互動介面的記憶寫入需人工核准
  nudge_interval: 10

# === 審批與安全 ===
approvals:
  mode: smart                  # smart（預設）／manual／off（等同 --yolo，正式環境禁用）
  cron_mode: deny              # 無人值守的 Cron 遇到危險指令一律拒絕
  unattended_mode: deny        # Webhook／API Server 等無人可回答的介面
command_allowlist:             # 永久允許的指令（精確文字、glob 或規則名稱）
  - "git status"
  - "git diff *"
  - "mvn test"
security:
  redact_secrets: true
  allow_private_urls: false    # 禁止 Agent 存取內網位址（SSRF 防護）
  allow_lazy_installs: false   # 禁止執行期自動安裝外掛／依賴（企業管控）

# === 終端後端 ===
terminal:
  backend: docker              # local／docker／ssh／modal／daytona／vercel_sandbox
  docker_image: "python:3.13-slim"
  docker_network: "none"

# === 工具集（依平台；hermes-cli 為 CLI 預設組合）===
toolsets: [hermes-cli]
agent:
  disabled_toolsets: [computer_use]

# === Session 保存（稽核需求請明確設定）===
sessions:
  auto_prune: false            # v0.23.0 預設即為 false；需要自動清理時設 true
  retention_days: 365

# === 日誌 ===
logging:
  level: INFO                  # DEBUG／INFO／WARNING／ERROR
  max_size_mb: 5
  backup_count: 3
```

> ⚠️ **更正**：舊版文件範例中的 `model.model`、`auxiliary.provider`、`memory.auto_save`、`security.command_approval`、`security.allowed_commands`、`toolsets.enabled`、`mcp.servers`、`gateway.platforms.*`、`logging.file` 都**不是**有效設定鍵。訊息平台的憑證與允許清單主要寫在 `.env`（例如 `TELEGRAM_ALLOWED_USERS`），平台行為設定則放在頂層的 `telegram:`、`slack:` 等區塊。

#### 4.7.2 設定檔驗證

```bash
hermes config check        # 檢查設定版本是否需要遷移、列出必要／選用的環境變數
hermes config migrate      # 執行設定遷移（升級後建議執行）
hermes config get approvals.mode
hermes config set approvals.mode manual   # 未知鍵會提示「not a recognized config key」並給出建議
hermes doctor              # 全面診斷：Provider 憑證、state.db、外掛、Gateway
```

> ⚠️ **實測發現**：`hermes config check` **不會**檢查未知鍵，它檢查的是設定版本（例如「Config version: 0 → 52」）與環境變數。要驗證設定鍵，請以 `hermes config set <key> <value>` 逐一寫入並觀察提示，或使用附錄 E 的 `check_doc.py`（它呼叫與 `config set` 相同的驗證函式）。

> **實務案例**：某銀行團隊在 WSL2 上以 `install.sh --non-interactive` 安裝，再以版本控管的 `config.yaml`（上例）與 Bitwarden 秘密來源完成設定，主 Provider 為 Anthropic，Docker 終端後端搭配 `docker_network: none` 做隔離。

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

### 4.9 本章審查與驗證清單

審查 AI 產出的安裝手冊、映像定義或基準設定時，請逐項核對：

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 安裝管道受官方支援 | 對照 4.1.1 表 | 沒有 `pip install hermes-agent`、`brew install`、ghcr 映像等已停用或不存在的管道 |
| 2 | 版本已釘選 | 檢查 Dockerfile／compose 的映像標籤、安裝腳本參數 | 正式環境使用 `X.Y.Z` 標籤或 digest，而不是 `main`；原始碼安裝的通道為 `stable` |
| 3 | 安裝成功 | `hermes --version`、`hermes doctor` | 版本為 `v0.23.0`；doctor 沒有錯誤 |
| 4 | Docker 掛載路徑正確 | `docker inspect hermes --format '{{json .Mounts}}'` | 資料掛載到 `/opt/data`（不是 `/root/.hermes`） |
| 5 | `state.db` journal mode 合適 | `docker exec hermes python3 -c "import sqlite3;print(sqlite3.connect('/opt/data/state.db').execute('PRAGMA journal_mode').fetchone())"` | 具名 volume 或本機磁碟為 `wal`；跨 VM bind mount 或網路檔案系統為 `delete` |
| 6 | API Server 沒有直接對外暴露 | `docker port hermes`、`ss -ltnp` | `8642`／`9119` 只綁定 `127.0.0.1`，或位於有認證的反向代理之後 |
| 7 | 設定鍵全部有效 | 對 4.7.1 的每個鍵執行 `hermes config get <key>`；或執行附錄 E 的 `check_doc.py` | 沒有未知鍵提示 |
| 8 | 憑證不在 `config.yaml` 中 | `grep -nE 'sk-|xox[bp]-|ghp_' ~/.hermes/config.yaml` | 沒有任何結果；`.env` 權限為 `0600` |
| 9 | 環境變數名稱正確 | 對照官方 Environment Variables 參考（或附錄 C） | 例如使用 `GEMINI_API_KEY`／`GOOGLE_API_KEY`，而不是不存在的 `GOOGLE_AI_API_KEY` |

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
# 使用 /quit（別名 /exit）或 Ctrl+D 離開
# v0.22.0：Ctrl+C 在輸入框有草稿時會先清除草稿，而不是中斷整個回合
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
| `/busy [steer\|queue\|interrupt]` | 設定 Agent 忙碌時新訊息的處理方式（v0.12.0） |
| `/btw` | 導引中插任務（v0.12.0） |
| `/reload-skills` | 重新載入技能庫（v0.12.0） |
| `/reload` | 熱重載 `.env` 設定（v0.12.0） |
| `/reload-mcp` | 重建 MCP cached agents（v0.12.0） |
| `/bg <prompt>` | 在獨立的背景 Session 執行一個提示（v0.12.0） |
| `/fast` | 切換 Fast Mode（Priority Processing） |
| `/steer` | 中途導引 Agent 行為（v0.11.0） |
| **`/goal`** | **設定跨回合持久目標（Ralph Loop）（v0.13.0）** |
| **`/kanban`** | **管理 Multi-agent Kanban 看板（v0.13.0）** |
| **`/queue`**（別名 `/q`） | **排入下一回合的提示；v0.22.0 起可 `list`／`edit N`／`rm N`／`move A B`／`clear`** |
| **`/learn <對象>`** | **將目錄／URL／剛示範的操作萃取為可重用 Skill（v0.18.0）** |
| **`/journey`** | **檢視記憶與技能學習時間軸（v0.18.0）** |
| **`/subscription` / `/topup`** | **查看 Nous Portal 訂閱方案、剩餘額度、升降級（v0.19.0）** |
| **`/deny <原因>`** | **拒絕待審指令並告知理由，讓 Agent 自我修正（v0.19.0）** |
| **`!<shell 指令>`** | **免佔用模型輪次，直接執行 Shell 指令（v0.20.0）** |
| **`/init`** | **掃描專案，自動產生／更新 AGENTS.md（v0.20.0）** |
| **`/diff`** | **顯示 staged／all／session 變更（v0.20.0）** |
| **`/context`** | **檢視目前上下文視窗的組成明細（v0.20.0）** |
| **`/focus`** | **精簡輸出檢視，隱藏內容可復原（v0.20.0）** |
| **`/rewind`** | **回溯到較早的提示後編輯重送，或按 `f` 分岔新 Session（v0.23.0；TUI 可在空白輸入框連按兩次 `Esc`）** |
| **`/stop`** | **停止目前回合；v0.22.0 起也能停止背景子代理並取回部分成果** |
| **`/autoprune [on\|off\|later]`** | **設定是否自動清理舊 Session（v0.23.0 預設關閉）** |

> **中途導引（Mid-turn Redirect，v0.20.0）**：Agent 執行中若發現方向偏離，可直接在 TUI 中輸入修正內容，無需等待當前輪次結束——進行中的工作會被保留，原始提示不遺失，Agent 據此修正方向，是 v0.11.0 `/steer` 的自然延伸（差異在於 `/steer` 需明確指令觸發，Mid-turn Redirect 可直接以自然語言插話）。

#### 5.1.1 Non-interactive 單次模式（v0.12.0+）

```bash
# 使用 -z（--oneshot）執行單次任務，不進入互動式介面
hermes -z "列出當前目錄下所有 Python 檔案"

# 指定模型與 Provider：--model／--provider 必須放在 -z 之前（-z 會吃掉緊接的下一個參數當作提示）
hermes --model anthropic/claude-sonnet-5.5 --provider openrouter -z "審查 main.py 的安全性"

# 另一種寫法：chat 子指令搭配 -q
hermes chat -q "產生項目摘要"
```

> ⚠️ ❌ **實測更正（反例）**：`hermes -z --model X "提示"` 會以 exit 2 失敗（`argument -z/--oneshot: expected one argument`）；直接寫 `hermes "提示"` 也會失敗（`is not a hermes command`）。在無人值守的 `-z`／`chat -q` 情境中，危險指令依 `approvals.single_query_mode`（預設 `deny`）處理，**不會**停下來等待人工核准。

#### 5.1.2 Background Sessions（v0.12.0+）

```text
# 把一個提示丟到獨立的背景 Session 執行，主對話可繼續
/bg 掃描 src/ 的依賴漏洞並整理成報告

# 背景任務完成後會自動通知；CLI 按 F6、TUI 按 Ctrl+T 可即時檢視子代理與背景工作
```

#### 5.1.3 Quick Commands（v0.12.0+）

```yaml
# ~/.hermes/config.yaml — Quick Commands：不經 LLM、不耗 Token，直接在主機執行
quick_commands:
  unittest:
    type: exec
    command: mvn -q test
  lint:
    type: exec
    command: npm run lint
  gwrestart:
    type: alias          # alias 型：轉成另一個斜線指令
    target: /restart
```

```text
# 在 CLI 或任何訊息平台輸入
/unittest
/lint
```

> 💡 **規則**：`type` 只能是 `exec` 或 `alias`；`exec` 指令有 **30 秒逾時**；Quick Commands 優先於同名技能；**純字串寫法（例如 `test: "mvn test"`）無效**，只會顯示錯誤。由於 `exec` 直接在主機上執行，請只放無破壞性的指令，並把 `config.yaml` 納入變更審查。

#### 5.1.4 Opt-in 自動恢復上次對話（v0.12.0+）

```bash
hermes -c                    # 繼續「這個終端機」上一次的 Session（依 tty／tmux pane 等辨識）
hermes --resume my-feature   # 繼續指定名稱的 Session
hermes sessions list         # 列出可繼續的 Session
```

> ⚠️ **更正**：v0.23.0 沒有 `session.auto_resume` 設定鍵。`session.terminal_continue`（預設 `true`）控制的是 `hermes -c` 是否以終端機為單位辨識要繼續的 Session。

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
1. [terminal] 使用 Spring Initializr 建立專案骨架
2. [write_file] 建立 Entity、Repository、Service、Controller
3. [write_file] 建立 Security 配置（JWT Filter）
4. [write_file] 建立 application.yml（DB 連線）
5. [write_file] 建立 Swagger 配置
6. [write_file] 建立 JUnit 測試
7. [terminal] 執行 mvn test 驗證
8. [自動學習] 封裝為 "spring-boot-rest-api" Skill
```

### 5.3 設定 Memory

```bash
# 設定 Memory Provider
hermes setup  # 在 Memory 區段選擇 provider

# 或直接編輯 config.yaml
hermes plugins install supermemory      # v0.22.0 起外部記憶 Provider 需先安裝外掛
hermes config set memory.provider supermemory
hermes config set memory.write_approval true
```

**記憶持久化範例**：

```bash
# 告訴 Agent 你的偏好
> 我使用 Java 21，偏好 Clean Architecture，測試框架用 JUnit 5 + Mockito

# Agent 會以 memory 工具寫入 USER.md（target: user）：
# - 使用 Java 21，偏好 Clean Architecture；測試用 JUnit 5 + Mockito

# 注意：記憶是「凍結快照」，本次寫入的內容要到下一個 Session 才會載入
```

### 5.4 設定 Tools

```bash
# 查看所有工具集
hermes tools

# 啟用瀏覽器工具（如需要網頁操作）
hermes tools enable browser

# 設定 MCP 伺服器（擴展工具能力）
hermes mcp catalog                       # 瀏覽 Nous 核准的 MCP 目錄
hermes mcp install github                # 從目錄安裝
hermes mcp list
hermes mcp test github                   # 測試連線與列出工具
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

# Agent 會使用 cronjob_manage 工具建立排程任務
# 結果自動透過 Gateway 投遞到指定平台；也可直接用 CLI 建立（見下方）
```

#### Per-job `workdir` 與跨執行連續性（v0.12.0／v0.21.0）

Cron 工作**不是**寫在 `config.yaml` 中，而是以 CLI（或 `cronjob_manage` 工具、Dashboard）建立，儲存在 `~/.hermes/cron/`：

```bash
# 每天 08:00 在指定目錄跑測試，結果送到 Telegram
hermes cron create "0 8 * * *" "執行完整測試套件並產出報告" \
  --name daily-test --workdir /home/dev/my-project --deliver telegram

# 每週一 09:00 產出週報；--continuity 會把上一次執行的輸出帶入下一次
hermes cron create "0 9 * * 1" "根據上週的測試結果產出週報" \
  --name weekly-report --continuity --deliver slack --timezone Asia/Taipei

hermes cron list
hermes cron run daily-test        # 下一個排程週期額外觸發一次（不影響原排程）
hermes cron cancel daily-test     # v0.23.0：停止目前這一次執行
```

> ⚠️ **更正**：舊版文件的 `cron.jobs.<name>.schedule/task/deliver_to/context_from` 都不是有效設定；`context_from` 不存在，跨執行延續請用 `--continuity`。

> **注意事項**：Quick Start 階段請維持 `approvals.mode: smart`（預設）：由輔助 LLM 判斷風險，低風險指令自動核准，真正危險的指令自動拒絕，不確定時才詢問你。需要每次都人工確認時改為 `manual`。`off` 等同 `--yolo`，**只應在可拋棄的容器或 CI 中使用**。

### 5.6 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 單次模式指令可執行 | `hermes --model <m> -z "hello"` | 正常回覆；`-z` 不在 `--model` 之前 |
| 2 | 斜線指令存在 | 在 CLI 輸入 `/help` 或 `/commands` | 文件中提到的指令都在清單中（`/bg`、`/quit`、`/rewind` 等）；沒有 ❌ `/background`、`/mouse` 等不存在的指令 |
| 3 | Quick Commands 格式正確 | 在 CLI 輸入 `/unittest` | 直接顯示指令輸出，不耗用 Token；純字串格式會顯示錯誤 |
| 4 | 記憶已寫入 | `/new` 開新 Session 後詢問偏好；或檢查 `~/.hermes/memories/USER.md` | 偏好出現在新 Session 中 |
| 5 | Cron 工作已建立 | `hermes cron list`、`hermes cron status` | 工作與排程正確；不在 `config.yaml` 的 `cron.jobs` 下 |
| 6 | MCP 伺服器可用 | `hermes mcp test <name>` | 列出該伺服器的工具 |
| 7 | 審批模式符合政策 | `hermes config get approvals.mode` | `smart` 或 `manual`；正式環境不是 `off` |

---

## 第六章：進階開發（企業級）

### 6.1 自訂 Skill（技能封裝）

#### 6.1.1 手動建立 Skill

技能放在 `~/.hermes/skills/<分類>/<技能名稱>/SKILL.md`。檔名必須是大寫的 `SKILL.md`，開頭是 YAML frontmatter：

```bash
mkdir -p ~/.hermes/skills/security/bank-api-security-check/references
```

```markdown
---
name: bank-api-security-check
description: 依 OWASP API Top 10 與金融業規範檢查 Spring Boot REST API，產出分級報告
version: 1.0.0
metadata:
  hermes:
    tags: [security, owasp, banking]
    category: security
    requires_toolsets: [file, terminal]
    config:
      - key: bank_api_audit.severity_threshold
        description: 報告的最低嚴重度
        default: "medium"
        prompt: "最低回報嚴重度（low/medium/high/critical）"
---

# Bank API Security Check

## When to Use
使用者提到「安全檢查」、「弱掃」、「API 安全審查」，或 PR 變更了 `@RestController`、`SecurityFilterChain`。

## Procedure
1. **掃描 API Controller**：以 `search_files` 找出所有 `@RestController`，確認每個端點都有 `@PreAuthorize` 或 `@Secured`。
2. **檢查認證機制**：JWT 過期時間與簽發者驗證、OAuth2 Scope、CORS 是否允許 `*`。
3. **掃描注入風險**：SQL 字串串接、未淨化的輸入、`Runtime.exec()`、未設白名單的外部 URL 呼叫（SSRF）。
4. **檢查敏感資料**：密碼雜湊演算法（BCrypt／Argon2）、PII 遮蔽、日誌是否含個資。
5. **產出報告**：依 `bank_api_audit.severity_threshold` 過濾，輸出 Markdown 表格（風險／嚴重度／檔案:行號／修復建議），依 Critical > High > Medium > Low 排序。

## Pitfalls
- 測試目錄（`src/test/`）中的假憑證不算洩漏。
- 不要只看註解存在與否；`permitAll()` 設定也會讓註解失效，需一併檢查 `SecurityFilterChain`。

## Verification
- 每項發現都附檔案路徑與行號，可人工開啟核對。
- 報告中「Critical」項目的數量與 `references/checklist.md` 的檢查項一一對應。
```

> ✅ **如何驗證**：
>
> 1. `hermes skills list | grep bank-api-security-check`：確認技能已被載入（frontmatter 錯誤時不會出現）。
> 2. `hermes skills inspect bank-api-security-check`：檢視解析後的中繼資料與 config 宣告。
> 3. `hermes config migrate`：會詢問尚未設定的 `bank_api_audit.severity_threshold`，值存於 `skills.config` 下。
> 4. 對一個刻意放入 SQL 字串串接的測試專案執行 `/bank-api-security-check`，報告必須抓到該行。

#### 6.1.2 Skill Config 介面（v0.8.0 新增）

技能可以在 frontmatter 的 `metadata.hermes.config` 宣告**非機密**設定（路徑、偏好等）。值儲存在 `config.yaml` 的 `skills.config` 下，技能載入時會自動注入上下文；機密值請改用 `requires_env` 類的環境變數，不要放進技能 config。

> ⚠️ **實測發現（v0.23.0）**：`hermes config set skills.config.bank_api_audit.severity_threshold high` 會成功寫入，但同時顯示「not a recognized config key … Hermes may not read it」的警告，這與官方文件「技能設定存放於 `skills.config`」的說明不一致。建議以 `hermes config migrate` 的互動提示寫入技能設定，並在導入時實際驗證技能是否讀到該值（見附錄 E.4）。

```yaml
# ~/.hermes/config.yaml — 技能 config 的實際儲存位置
skills:
  config:
    bank_api_audit:
      severity_threshold: high
```

#### 6.1.3 從 Skills Hub 安裝

```bash
hermes skills browse                               # 瀏覽 Hub（官方優先）
hermes skills search kubernetes                    # 搜尋所有來源
hermes skills inspect openai/skills/k8s            # 安裝前預覽
hermes skills install openai/skills/k8s            # 安裝（含安全掃描）
hermes skills install official/security/1password  # 官方 optional 技能
hermes skills check                                # 檢查已安裝 Hub 技能的上游更新
hermes skills audit                                # 重新掃描所有 Hub 技能
```

> ⚠️ **v0.22.0 變更**：`hermes sync`（Skill Sync）已移除。內建技能會在安裝與 `hermes update` 時播種到每個 Profile；若某個 Profile 不需要內建技能，請執行 `hermes skills opt-out`。

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
    SA3 --> |"read_file<br/>terminal"| TEST[Test Tools]
    
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
# ~/.hermes/config.yaml — Multi-agent Kanban 調度設定（鍵名以 v0.23.0 DEFAULT_CONFIG 為準）
kanban:
  dispatch_in_gateway: true          # 由 Gateway 內建調度器派工
  dispatch_interval_seconds: 60      # 調度週期
  failure_limit: 2                   # 連續失敗幾次後停止自動重派
  max_in_progress: 6                 # 全看板同時進行中的上限
  max_in_progress_per_profile: 2     # 每個 Profile（Worker 身分）的上限
  dispatch_profiles: [team-backend, team-frontend, team-qa]   # 允許被派工的 Profile
  orchestrator_profile: team-lead    # 負責拆解與協調的 Profile
  auto_decompose: true
  dispatch_stale_timeout_seconds: 14400   # 認領多久未更新視為逾時並回收
  done_sub_retention_days: 30
```

> ⚠️ **更正**：舊版範例的 `kanban.enabled`、`multi_project`、`max_retries`、`heartbeat_interval`、`zombie_timeout`、`hallucination_gate`、`sharing.*` 都不是有效設定鍵。重試次數是**任務層級**的屬性（`hermes kanban create --max-retries N`）；多看板是以 `hermes kanban boards create` 建立，不需要開關。

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
hermes kanban dispatch --dry-run      # 預覽派工結果
hermes kanban dispatch                # 手動觸發一次派工迴圈
hermes kanban diag --severity warning # 診斷卡住、逾時的任務

# 對話中斜線指令（與 CLI 對應同一份資料）
/kanban                        # 查看當前看板狀態

# Agent 內部工具（kanban_* toolset，供 Worker 自身呼叫）
# kanban_show / kanban_complete / kanban_block / kanban_heartbeat /
# kanban_comment / kanban_create / kanban_link / kanban_request_review
# Orchestrator 專用：kanban_list / kanban_unblock
```

**任務生命週期**：`triage → todo → ready → running → review｜blocked → done → archived`。**Dispatcher** 為長駐迴圈（預設 60 秒輪詢一次，`kanban.dispatch_in_gateway: true` 時內建於 Gateway 執行），負責回收逾時／當機的認領、於父任務完成後自動將子任務由 `todo` 推進至 `ready`、原子性認領 `ready` 任務並以獨立 OS 行程派生對應 Profile 的 Worker，連續失敗達 `max_retries` 後自動標記阻擋。

**工作區類型**（`workspace` 欄位）：`scratch`（暫存，預設，任務結束即清除）、`worktree`（獨立 Git worktree，保留）、`dir:<絕對路徑>`（共用目錄，保留）。

**多租戶支援**：租戶與工作區是**任務**的屬性，在建立任務時指定，例如 `hermes kanban create "月結報表" --tenant business-a --workspace dir:/srv/tenants/business-a`；之後以 `hermes kanban list --tenant business-a` 篩選。Worker 會取得 `$HERMES_TENANT` 環境變數，記憶寫入依租戶命名空間隔離。（舊版文件把 `--tenant`／`--workspace` 寫在 `kanban dispatch` 上，實測為 `unrecognized arguments`。）

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

#### 6.4.1 使用 Supermemory

v0.22.0 起，Supermemory 由其維護者透過 Plugin Catalog 發布。容器、搜尋模式等進階參數在外掛自己的設定中，**不是** `config.yaml` 的 `memory.supermemory.*`。

```bash
hermes plugins install supermemory     # 從 Catalog 安裝（同時安裝 SDK）
hermes plugins enable supermemory
hermes memory setup                    # 選擇 supermemory，依提示輸入 API Key 或自架位址
hermes memory status                   # 確認啟用中的 Provider
```

```bash
# ~/.hermes/.env — 手動設定時
SUPERMEMORY_API_KEY=sm_xxxxxxxxxxxx
```

提供的工具：`supermemory_store`、`supermemory_search`、`supermemory_forget`、`supermemory_profile`。自架時可執行 `npx supermemory local`。

#### 6.4.2 使用 Mem0

```bash
hermes plugins install mem0
hermes memory setup            # 選擇 mem0 → Platform／Open Source（自架）／Self-hosted server
```

```bash
# ~/.hermes/.env — Platform 模式
MEM0_API_KEY=m0-xxxxxxxxxxxx
MEM0_TELEMETRY=false           # mem0ai SDK 預設會送出匿名 PostHog 使用統計；企業環境建議關閉
```

提供的工具：`mem0_search`、`mem0_add`、`mem0_update`、`mem0_delete`。

> 🔐 **資料治理**：Hermes 交給外部 Provider 的所有內容（對話輪次、含工具輸出的逐字稿、查詢、委派結果等）都會先經過與其他出站資料相同的秘密遮蔽。但遮蔽不等於去識別化：涉及個資時，請優先選擇可自架的 Provider，並把 Provider 列入資料流盤點。

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

v0.17.0 新增的 Automation Blueprints 是**參數化的現成自動化範本**：選一個範本、填幾個欄位，Hermes 就會建立一個 Cron 工作，不需要寫 cron 語法。每一個入口都會在建立前請你確認，不會靜默排程。

| 入口 | 操作方式 |
| ------ | ------ |
| Dashboard／Desktop | Cron 頁面 → **Blueprints** 分頁 → 填表 → *Schedule it* |
| CLI／TUI／訊息平台 | `/blueprint <名稱>`，Hermes 逐一詢問所需欄位；也可直接帶值：`/blueprint morning-brief time=08:00` |
| Desktop 文件頁 | 點 **Send to App**，指令會預先填入輸入框 |
| 外掛 | 外掛可以提供自己的 Blueprint，名稱為 `外掛名:範本名`（例如 `/blueprint teamtools:standup`），不會覆蓋內建範本 |

```text
/blueprint morning-brief
/blueprint morning-brief time=08:00
/cron                     # 管理建立出來的工作
```

> **與 Cron 的關係**：Blueprint 只是「產生 Cron 工作的精靈」，建立後就是一般的 Cron 工作（`hermes cron list` 可見），停用提供它的外掛也不會刪除已建立的工作。⚠️ **更正**：舊版文件的 `~/.hermes/blueprints/*.yaml` 檔案格式與 `/blueprint create "…"` 語法都不存在。

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
# 建立不同團隊的 Profile（只需一次）
hermes profile create team-backend
hermes profile create team-frontend
hermes profile create team-devops

# 以指定 Profile 啟動（-p 等同 --profile）
hermes -p team-backend
hermes -p team-frontend
hermes profile list

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

```bash
# Cron 工作以 CLI 建立（儲存於 ~/.hermes/cron/），不是寫在 config.yaml
hermes cron create "0 9 * * *" "掃描主分支的新增相依套件是否有已知 CVE，僅在有新發現時回報" \
  --name daily-security-scan \
  --workdir /srv/app \
  --continuity \
  --monitor-script deps_snapshot.sh \
  --reasoning-effort medium \
  --deliver slack \
  --failure-deliver telegram

hermes cron list                          # 確認工作已建立與下次執行時間
hermes cron status                        # 排程器整體狀態（不接受工作名稱參數）
hermes cron notepad daily-security-scan   # 檢視此工作的持久筆記
hermes cron runs daily-security-scan      # 執行紀錄
```

- `--continuity`：每次執行都會把**上一次的輸出**注入提示，讓 Agent 可以去重並接續。
- `--monitor-script <~/.hermes/scripts/ 下的腳本>`（或 `--monitor-url <URL>`）：每次觸發先執行這個便宜的來源檢查；**輸出位元組雜湊不變就完全跳過 Agent 執行**，有變化才把差異注入提示。
- `--deliver`：`origin`、`local`、平台名稱（送到該平台的 Home channel）、`platform:chat_id`，或 `bot-chat[:profile]`。

> ⚠️ **更正**：舊版範例的 `cron.jobs: [...]`（含 `monitor: true`、`notify:`）不是有效設定。Monitor 模式需要提供 `--monitor-script` 或 `--monitor-url` 作為變化偵測來源。

> 💡 **成本實務**：Monitor 模式（`--monitor-script`／`--monitor-url`）是對 TCO 影響最大的單一設定。一個每 15 分鐘執行、但九成時間「無事發生」的監控任務，開啟後可省下約九成的 LLM 呼叫費用。
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

#### 6.9.2 內建 Plugin 與 Catalog 外掛（v0.23.0）

v0.22.0 起，許多原本內建的整合改由各維護者透過 **Plugin Catalog** 發布（見 1.4.46）。下表依 v0.23.0 原始碼的 `plugins/` 目錄整理：

| 類別 | 內建於 v0.23.0（`plugins/`） | 已移到 Catalog（需 `hermes plugins install`） |
| -------- | ------ | ------ |
| 訊息平台 | `platforms/`：telegram、discord、slack、teams、google_chat、line、matrix、mattermost、signal、whatsapp、whatsapp_cloud、photon、a2a、ntfy、raft、buzz 等 | Home Assistant |
| 模型 Provider | `model-providers/`：anthropic、openrouter、nous、bedrock、vertex、azure-foundry、lmstudio、ollama-cloud、xai 等 40+ | — |
| 記憶 | `memory/`：byterover、retaindb | honcho、mem0、supermemory、hindsight、openviking、holographic |
| 瀏覽器來源 | `browser/`：browserbase、browser_use、firecrawl | camofox |
| 網路搜尋 | `web/`：brave_free、ddgs、exa、firecrawl、searxng、tavily、perplexity 等 | — |
| 影像／影片生成 | `image_gen/`（fal、krea、openai、xai 等）、`video_gen/` | Meshy（3D）、ElevenLabs Music／SFX |
| 其他 | `google_meet`、`teams_pipeline`、`kanban`、`delegation`、`security-guidance`、`disk-cleanup`、`hermes-achievements` | Spotify、Langfuse、`mcp-serve`、`agent-importers`、`advanced-delegation`、Singularity、bubblewrap 沙箱、REA、X Chat |

> 💡 **自動遷移**：升級時，已設定某個整合的 Profile 會由 `hermes update`（或 Desktop 首次啟動）自動安裝對應的 Catalog 外掛；若 `security.allow_lazy_installs: false`、離線或被拒絕，警告訊息會附上確切的 `hermes plugins install <name>` 指令。

#### 6.9.2.1 Plugin Hooks（v0.23.0 共 46 種）

`hermes_cli.plugins.VALID_HOOKS` 在 v0.23.0 共有 **46** 個事件，可分為：

| 類型 | 代表事件 | 行為 |
| ------ | ------ | ------ |
| Observer（觀察） | `post_tool_call`、`post_llm_call`、`on_session_start`、`on_session_end`、`subagent_stop`、`on_kanban_task_updated` | 回傳值被忽略 |
| Transform（轉換） | `transform_llm_output`、`transform_tool_result`、`transform_terminal_output`、`transform_api_error_classification` | 採用第一個有效的字串回傳值 |
| Directive／Control（控制） | `pre_tool_call`、`pre_llm_call`、`pre_gateway_dispatch`、`pre_approval_request`、`pre_verify` | 可依文件定義的回傳格式改變流程（例如阻擋工具呼叫） |

```python
# ~/.hermes/plugins/output-redactor/__init__.py — transform_llm_output 範例（官方 register(ctx) 介面）
import re

_PATTERN = re.compile(r"INTERNAL-[A-Z0-9]{8}")


def register(ctx):
    def redact(text, **kwargs):
        del kwargs
        if not isinstance(text, str):
            return None          # 不處理就回傳 None，交給下一個 transform
        return _PATTERN.sub("[REDACTED]", text)

    ctx.register_hook("transform_llm_output", redact)
```

> ⚠️ **更正**：舊版範例使用的 `from hermes.plugins import PluginBase, hook` 與類別裝飾器寫法**不是** Hermes 的外掛 API；官方介面是模組層級的 `register(ctx)` 函式。

#### 6.9.3 Spotify 整合（v0.22.0 起為 Catalog 外掛）

```bash
hermes plugins install spotify
hermes plugins enable spotify
# 首次使用時會啟動 PKCE OAuth 流程，瀏覽器自動開啟 Spotify 授權頁面
```

#### 6.9.4 Google Meet 整合（內建外掛）

Google Meet 是 v0.23.0 仍內建的外掛（`plugins/google_meet`），會註冊 `hermes meet` CLI 子指令：加入會議、即時轉錄、語音發言、會後產出摘要與行動項目。啟用方式與一般外掛相同：

```bash
hermes plugins enable google_meet
hermes meet --help
```

#### 6.9.5 自訂 Plugin 開發（官方標準結構）

Plugin 目錄需包含清單檔 `plugin.yaml` 與進入點 `__init__.py`：

```text
~/.hermes/plugins/my-custom-tool/
├── plugin.yaml       # 清單：name / version / description / provides_tools / provides_hooks / requires_env / capabilities
├── __init__.py        # register(ctx) 進入點
├── schemas.py          # 工具參數 Schema（選用）
└── tools.py             # 工具實作（選用）
```

```yaml
# plugin.yaml
name: my-custom-tool
version: "1.0.0"
description: "封裝內部 JIRA API 為 Agent 工具"
provides_tools:
  - jira_create_ticket      # 必須與 register() 實際註冊的工具一致，否則 hermes plugins validate 失敗
provides_hooks:
  - post_tool_call
requires_env:
  - name: JIRA_API_TOKEN
    description: "JIRA 個人存取權杖"
    secret: true
capabilities: []            # 需覆寫內建工具填 tools.override；需指定 ctx.llm 的模型填 llm.model_override
```

```python
# __init__.py
import json


def create_ticket_handler(params, **kwargs):
    del kwargs
    # 實際呼叫 JIRA REST API（略）；回傳 JSON 字串
    return json.dumps({"success": True, "key": "OPS-123", "title": params["title"]})


def on_tool_result(tool_name, args, result, **kwargs):
    del args, result, kwargs
    print(f"[my-custom-tool] tool called: {tool_name}")


def jira_status_handler(*args, **kwargs):
    return "JIRA OK"


def register(ctx):
    ctx.register_tool(
        name="jira_create_ticket",
        toolset="jira",
        schema={
            "name": "jira_create_ticket",
            "description": "在 JIRA 建立工單",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "工單標題"},
                    "description": {"type": "string", "description": "工單內容"},
                },
                "required": ["title"],
            },
        },
        handler=create_ticket_handler,
    )
    ctx.register_hook("post_tool_call", on_tool_result)
    ctx.register_command("jira-status", jira_status_handler, description="查詢 JIRA 專案狀態")
```

**`PluginContext`（`ctx`）核心 API**：`register_tool`（新增工具；`schema` 為完整的 OpenAI function 格式，模型看到的描述放在 `schema["description"]`）、`register_hook`（掛接 46 種生命週期事件之一，如 `pre_tool_call`／`transform_llm_output`／`on_session_end`）、`register_command`（新增 `/name` 斜線指令）、`register_cli_command`（新增 `hermes <plugin> <subcommand>`）、`register_skill`（隨 Plugin 附帶 Skill）、`inject_message`（插入訊息至對話）、`call_mcp`（呼叫已設定的 MCP 伺服器）。

**探索來源**：官方內建（`<repo>/plugins/`）、使用者（`~/.hermes/plugins/` 或 `hermes plugins install`）、pip entry points（`hermes_agent.plugins`）、Nix module。⚠️ **v0.23.0 變更**：所有 Session 都在單一 Gateway 中執行，Gateway 只在啟動時探索一次外掛，**不會**從你啟動 Session 的資料夾載入專案層級外掛（`./.hermes/plugins/`），`HERMES_ENABLE_PROJECT_PLUGINS=true` 對 Session 已無作用。

> ⚠️ **安全模型（官方原文）**：「Plugin 以 in-process Python 執行——capabilities 是同意層（consent layer），不是沙箱（sandbox）」。一般 Plugin **預設全部停用**，需在 `config.yaml` 的 `plugins.enabled` 明確列出才會載入；安裝與每次更新新增權限時皆會提示使用者同意。企業導入任何第三方 Plugin 前，應視同引入可完整存取 Agent Process 的程式碼進行審查，而非僅信任其描述文字。

```yaml
# ~/.hermes/config.yaml — Plugin 啟用控制與行程隔離
plugins:
  enabled: [my-custom-tool, disk-cleanup]
  disabled: [noisy-plugin]
  isolation: host            # 預設 in_process；host = 第三方外掛在每個 Profile 獨立的 Python 行程中執行
```

> 🔐 **`plugins.isolation: host`（企業建議開啟）**：第三方 Python 外掛不再匯入 Hermes 主行程，因此無法從記憶體讀取其他 Profile 的資料，也無法修補 Hermes 內部；`plugins.host.launcher` 可以再包一層沙箱啟動器。內建外掛仍在主行程中執行。

```bash
hermes plugins validate ./my-custom-tool    # 宣告的工具是否與註冊一致、安全掃描結果
hermes plugins capabilities my-custom-tool  # 檢視外掛要求的特權
hermes plugins doctor
```

**Plugin Packs**（`hermes plugins pack show ./hermes-pack.yaml` 先預覽，再 `hermes plugins pack install ./hermes-pack.yaml`；`hermes plugins pack export` 可匯出目前安裝狀態）：以 `hermes-pack.yaml` 將多個 Plugin 釘選至精確 commit SHA 一次性分享安裝，安裝時僅需確認一次所有權限；秘密憑證不會隨 Pack 一併打包。

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

### 6.11 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 技能可被載入 | `hermes skills list`、`hermes skills inspect <name>` | 技能出現在清單；frontmatter 欄位正確解析 |
| 2 | 技能行為符合預期 | 用含已知缺陷的測試專案執行 `/<skill>` | 報告抓到植入的缺陷，且附檔案:行號 |
| 3 | Kanban 設定有效 | `hermes config get kanban.dispatch_interval_seconds`；`hermes kanban dispatch --dry-run` | 回傳設定值；dry-run 列出將被派工的任務 |
| 4 | 多租戶隔離 | `hermes kanban list --tenant business-a` | 只列出該租戶的任務 |
| 5 | 記憶 Provider 為已安裝的外掛 | `hermes plugins list`、`hermes memory status` | Provider 外掛為 enabled，status 顯示同一個 Provider |
| 6 | Cron 工作設定正確 | `hermes cron status <job>`、`hermes cron doctor` | 有 `--continuity`／monitor 來源；沒有 `config.yaml` 的 `cron.jobs` |
| 7 | 外掛宣告與實作一致 | `hermes plugins validate <path>` | declared tools 檢查通過；安全掃描沒有 `dangerous` |
| 8 | 第三方外掛行程隔離 | `hermes config get plugins.isolation` | 企業環境為 `host` |
| 9 | 外掛程式碼使用官方 API | 人工審查 `__init__.py` | 使用模組層級 `register(ctx)`，沒有 `PluginBase`／`@hook` 之類不存在的 API |

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
| KittenTTS | 本地輕量 TTS | 低 | 免費 | ⚠️ **v0.22.0 起在 Python 3.14 執行環境中無法使用** |
| Piper | 本地 TTS | 低 | 免費 | `tts.piper.voice` 指定語音 |
| Gemini／Mistral（Voxtral）／DeepInfra | 雲端 TTS | 中等 | 依方案 | `tts.provider` 可選 `gemini`、`mistral`、`deepinfra` |
| MiniMax（Speech 2.8） | MiniMax TTS | 中等 | 依方案 | v0.8.0 新增 |
| **xAI Custom Voices** | xAI 語音克隆 TTS | 中等 | 依方案 | 支援語音克隆（voice cloning），v0.13.0 新增，v0.15.0 起 `auto_speech_tags` 自然語調 |

> 系統依賴：語音模式需要 PortAudio；Discord 語音頻道另需 Opus codec；NeuTTS 需 `espeak-ng`。v0.22.0 起 FFmpeg 與本機 Faster-Whisper 由 PM 準備（支援的平台上不需要 STT API Key）。官方安裝腳本選用 `all` extra，一般不必再手動安裝語音擴充套件。v0.23.0 另新增官方外掛 **ElevenLabs Music／Sound Effects**（`hermes plugins install` 安裝）。

### 7.3 CLI 語音互動

```text
# 在 CLI／TUI 對話中切換（沒有 --voice 啟動旗標）
/voice on       # 開啟語音模式
/voice off      # 關閉
/voice tts      # 切換語音輸出
/voice status   # 目前狀態
```

```bash
# 以設定指令選擇 Provider
hermes config set stt.provider local        # local（免費、離線）| groq | openai | mistral | xai | elevenlabs | deepinfra
hermes config set tts.provider edge         # edge（免費）| elevenlabs | openai | neutts | minimax | mistral | gemini | xai | kittentts | piper
```

```yaml
# ~/.hermes/config.yaml — 語音相關設定分成 stt／tts／voice／wake_word 四個區塊
stt:
  enabled: true
  provider: local              # 本機 Faster-Whisper，免 API Key
  language: "zh"               # 全域語言提示；"" = 自動偵測
  local:
    model: base                # tiny | base | small | medium | large-v3 | turbo

tts:
  provider: elevenlabs
  elevenlabs:
    voice_id: "pNInz6obpgDQGcFmaJgB"
    model_id: "eleven_multilingual_v2"
  openai:
    model: "gpt-4o-mini-tts"
    voice: "alloy"
  xai:                         # xAI Custom Voices（v0.13.0）
    voice_id: "eve"
    auto_speech_tags: true     # v0.15.0：自然語調標記

voice:                         # CLI 互動行為
  record_key: "ctrl+b"
  silence_threshold: 200
  silence_duration: 3.0
  stop_phrases: ["stop", "停止"]
  barge_in: true
  auto_tts: false

wake_word:                     # v0.20.0：裝置端喚醒詞（偵測不外流）
  enabled: true
  phrase: "hey hermes"
  sensitivity: 0.6
```

```bash
# ~/.hermes/.env — 語音 Provider 的金鑰一律放在 .env，不寫進 config.yaml
ELEVENLABS_API_KEY=sk_xxxxxxxxxxxx
GROQ_API_KEY=gsk_xxxxxxxxxxxx
```

> ⚠️ **更正**：舊版範例的 `hermes --voice`（實測為 `unrecognized arguments`）、`voice.enabled`、`voice.stt_provider`、`voice.tts_provider`、`voice.openai.*`、`voice.voxtral`、`voice.piper`、`voice.wake_word` 都不是有效設定。STT 設定在 `stt:`，TTS 設定在 `tts:`，喚醒詞在頂層 `wake_word:`，金鑰放在 `.env`。

**CLI 語音互動實際操作方式**：`Ctrl+B` 按下開始錄音，停頓 3 秒自動結束（採兩階段偵測：0.3 秒確認開始說話 + 3.0 秒判定結束），兩聲提示音確認錄音起訖，之後持續循環直到再次按 `Ctrl+B` 或說出／輸入「stop」結束；回覆採**逐句串流播放**並支援 **Barge-in**（說話即可打斷正在播放的語音）。

#### 7.3.1 Pluggable TTS Provider Registry（v0.12.0+）

v0.12.0 將 TTS 架構重構為可插拔式註冊表，允許第三方 Plugin 新增 TTS 引擎：

自訂 TTS 引擎以**外掛**的形式註冊（`ctx.register_tts_provider(...)`），而不是在 `config.yaml` 中宣告端點。安裝並啟用外掛後，即可把 `tts.provider` 設為該外掛註冊的名稱：

```bash
hermes plugins install <tts-plugin>
hermes plugins enable <tts-plugin>
hermes config set tts.provider <外掛註冊的名稱>
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

**Telegram／Discord 的語音回覆模式**以對話中的斜線指令切換，設定會在 Gateway 重啟後保留：

```text
/voice          # 切換開／關
/voice on       # 只有使用者傳語音時才以語音回覆（voice_only）
/voice tts      # 所有訊息都以語音回覆（all）
/voice off      # 只回文字（預設）
/voice status   # 顯示目前設定
```

> 💡 語音備忘錄的自動轉錄由 `stt.enabled` 控制（預設 `true`）。設為 `false` 時 Gateway 仍會快取音檔，並把路徑交給 Agent，方便接自訂的處理流程（說話者分離、歸檔等）。

### 7.5 Discord Voice Channel 即時語音

Hermes 支援加入 Discord Voice Channel 進行即時語音對話：

```text
# 在 Discord 文字頻道中輸入（你必須已經在某個語音頻道內）
/voice join      # Bot 加入你目前所在的語音頻道（/voice channel 為別名）
/voice leave     # Bot 離開語音頻道
```

```bash
# ~/.hermes/.env — 伺服器頻道預設需要 @mention；可針對特定頻道免 mention
DISCORD_REQUIRE_MENTION=true
DISCORD_FREE_RESPONSE_CHANNELS=123456789012345678
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
| 離線環境 | `stt.provider: local` + `tts.provider: neutts` 或 `piper` | 無需網路的語音互動（避免 KittenTTS：Python 3.14 不支援） |

> **安全提醒**：語音資料可能包含敏感資訊。企業環境建議使用本地 Whisper 模型或確保語音資料傳輸加密（TLS）。不要在語音中傳輸密碼、API Key 等敏感資訊。

### 7.7 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 語音設定鍵有效 | `hermes config get stt.provider`、`hermes config get tts.provider` | 回傳設定值；沒有 `voice.stt_provider` 之類的鍵 |
| 2 | 金鑰不在 config.yaml | `grep -n 'api_key' ~/.hermes/config.yaml` | 語音 Provider 的金鑰都在 `.env` |
| 3 | CLI 語音可用 | 在 CLI 執行 `/voice on`，按 `Ctrl+B` 說一句話 | 出現兩聲提示音，轉錄文字顯示在輸入框 |
| 4 | 離線語音可用 | 斷網後以 `stt.provider: local` 錄音 | 仍能轉錄（首次需先下載模型） |
| 5 | 訊息平台語音模式 | 在 Telegram 輸入 `/voice status` | 顯示 `off`／`voice_only`／`all` 之一 |
| 6 | 不使用已失效的 Provider | 檢查 `tts.provider` | 在 Python 3.14 執行環境中不是 `kittentts` |

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
        AGENT_SVC[Agent Facade<br/>FastAPI / Spring Boot]
    end
    
    subgraph "Hermes Agent Layer"
        GW[Hermes Gateway<br/>API Server :8642（OpenAI 相容）]
        HERMES[Agent Loop<br/>由 Gateway 擁有 Session]
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
    
    AGENT_SVC -->|Bearer API_SERVER_KEY<br/>X-Hermes-Session-Key| GW
    GW --> HERMES
    HERMES -->|MCP Protocol| MCP_SRV
    MCP_SRV --> BIZ_DB
    
    HERMES --> AGENT_DB
```

### 8.2 FastAPI 後端整合

> ⚠️ **v0.23.0 整合原則**：**不要用子行程呼叫 `hermes` CLI 來包裝成服務**。舊版範例使用的 `hermes chat --message`、`--session`、`--stream`、`hermes skills --json` 等旗標都不存在；而且 v0.23.0 起所有 Session 都由 Gateway 擁有，正確做法是呼叫 Gateway 內建的 **OpenAI 相容 API Server**。

#### 8.2.1 啟用 Hermes API Server

```bash
# ~/.hermes/.env
API_SERVER_ENABLED=true
API_SERVER_KEY=change-me-to-a-long-random-string
```

```bash
hermes gateway restart
curl -s http://127.0.0.1:8642/health
curl -s http://127.0.0.1:8642/v1/chat/completions \
  -H "Authorization: Bearer $API_SERVER_KEY" -H "Content-Type: application/json" \
  -d '{"model": "hermes-agent", "messages": [{"role": "user", "content": "Hello"}]}'
```

| 重點 | 說明 |
| --- | --- |
| 端點 | `POST /v1/chat/completions`（無狀態，對話內容放在 `messages`）、`POST /v1/responses`、`POST /v1/runs`（可串流事件、可 stop／approval／clarify）、`GET /v1/models`、`GET /health` |
| 認證 | `Authorization: Bearer <API_SERVER_KEY>` |
| 延續對話 | 加上 `X-Hermes-Session-Key: <你的鍵>`（同一個鍵 = 同一段對話）；或以 `X-Hermes-Session-Id` 指定既有 Session |
| 結束狀態 | `finish_reason` 為 `stop`（成功）、`length`（迭代預算用盡，但內容仍是可用的總結）、`cancelled`、`error` |
| 無人值守審批 | API Server 屬於無人可回答的介面，危險指令依 `approvals.unattended_mode`（預設 `deny`）處理 |
| 多 Profile | 單一 Gateway 服務多個 Profile 時，以 `/p/<profile>/` URL 前綴指定 Profile |

#### 8.2.2 FastAPI Facade（已實測）

以下 Facade 保留 `/api/agent/chat`、`/api/agent/stream` 兩個業務端點，後端轉送到 Hermes API Server，並以上游 API Gateway 注入的 `X-User-Id` 為每位使用者隔離 session key：

```python
# agent_service.py — 企業內部的 Agent Facade：把前端請求轉送到 Hermes Gateway 的 OpenAI 相容 API Server
# 依賴：pip install fastapi uvicorn httpx pydantic
import json
import os
from collections.abc import AsyncIterator

import httpx
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

HERMES_URL = os.environ.get("HERMES_API_URL", "http://127.0.0.1:8642")
HERMES_KEY = os.environ["HERMES_API_KEY"]  # 與 Gateway 的 API_SERVER_KEY 相同；缺少時啟動即失敗
TIMEOUT = httpx.Timeout(connect=5.0, read=600.0, write=30.0, pool=5.0)

app = FastAPI(title="Hermes Agent Facade", version="2.0.0")


class AgentRequest(BaseModel):
    message: str = Field(min_length=1, max_length=20_000)
    session_key: str | None = Field(default=None, max_length=128)  # 同一個值 = 同一段對話
    skill: str | None = Field(default=None, pattern=r"^[a-z0-9][a-z0-9-]{0,63}$")


class AgentResponse(BaseModel):
    response: str
    finish_reason: str
    total_tokens: int


def _headers(session_key: str | None) -> dict[str, str]:
    headers = {"Authorization": f"Bearer {HERMES_KEY}", "Content-Type": "application/json"}
    if session_key:
        headers["X-Hermes-Session-Key"] = session_key
    return headers


def _payload(req: AgentRequest, stream: bool) -> dict:
    text = f"/{req.skill} {req.message}" if req.skill else req.message
    return {"model": "hermes-agent", "messages": [{"role": "user", "content": text}], "stream": stream}


@app.post("/api/agent/chat", response_model=AgentResponse)
async def chat(req: AgentRequest, x_user_id: str = Header(...)) -> AgentResponse:
    """同步對話。X-User-Id 由上游 API Gateway 注入，用來組出每位使用者自己的 session key。"""
    session_key = f"{x_user_id}:{req.session_key}" if req.session_key else None
    async with httpx.AsyncClient(base_url=HERMES_URL, timeout=TIMEOUT) as client:
        r = await client.post("/v1/chat/completions", headers=_headers(session_key), json=_payload(req, False))
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail=f"hermes returned {r.status_code}")
    body = r.json()
    choice = body["choices"][0]
    if choice.get("finish_reason") in ("error", "cancelled"):
        raise HTTPException(status_code=502, detail=f"agent run {choice['finish_reason']}")
    return AgentResponse(
        response=choice["message"]["content"],
        finish_reason=choice["finish_reason"],  # "length" = 迭代預算用盡但仍有可用的總結
        total_tokens=body.get("usage", {}).get("total_tokens", 0),
    )


@app.post("/api/agent/stream")
async def stream_chat(req: AgentRequest, x_user_id: str = Header(...)) -> StreamingResponse:
    """SSE 串流：逐段轉送 Hermes 的 chat.completion.chunk，前端收到 {"content": ...} 與 {"done": true}。"""
    session_key = f"{x_user_id}:{req.session_key}" if req.session_key else None

    async def generate() -> AsyncIterator[str]:
        async with httpx.AsyncClient(base_url=HERMES_URL, timeout=TIMEOUT) as client:
            async with client.stream(
                "POST", "/v1/chat/completions", headers=_headers(session_key), json=_payload(req, True)
            ) as r:
                if r.status_code != 200:
                    yield f"data: {json.dumps({'error': r.status_code})}\n\n"
                    return
                async for line in r.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    data = line[len("data: "):]
                    if data == "[DONE]":
                        break
                    delta = json.loads(data)["choices"][0].get("delta", {}).get("content")
                    if delta:
                        yield f"data: {json.dumps({'content': delta}, ensure_ascii=False)}\n\n"
        yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


@app.get("/api/agent/health")
async def health() -> dict:
    async with httpx.AsyncClient(base_url=HERMES_URL, timeout=5.0) as client:
        r = await client.get("/health")
    return {"hermes": r.status_code == 200}
```

#### 8.2.3 啟動與驗證

```bash
pip install fastapi uvicorn httpx pydantic
export HERMES_API_KEY="$API_SERVER_KEY"
uvicorn agent_service:app --host 127.0.0.1 --port 8000

curl -s -X POST http://127.0.0.1:8000/api/agent/chat \
  -H "Content-Type: application/json" -H "X-User-Id: u001" \
  -d '{"message": "列出 src/ 的 TODO", "session_key": "repo-a"}'
```

> ✅ **本手冊的實測方式**：以一個模擬 Hermes API Server（實作 `/v1/chat/completions` 一般與 SSE 兩種回應），對上述 Facade 執行 9 項端對端測試，全部通過：轉送成功、session key 依使用者隔離（`u7:s1`）、Bearer 轉送、技能前綴、非法技能名稱回 422、缺少 `X-User-Id` 回 422、SSE 內容組合正確、結束標記、上游 401 轉為 502。測試程式見附錄 E.3。

### 8.3 Spring Boot 後端整合

#### 8.3.1 Agent Client 封裝

```java
package com.example.assistant.hermes;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

/**
 * Hermes Gateway API Server 客戶端（Spring Boot 3.2+ / 4.x 的 RestClient）。
 * 設定值以建構子注入，避免「@Value 欄位在建構子執行時尚未注入」的常見錯誤。
 */
@Service
public class HermesAgentClient {

    private final RestClient restClient;

    public HermesAgentClient(RestClient.Builder builder,
                             @Value("${hermes.api.url:http://127.0.0.1:8642}") String baseUrl,
                             @Value("${hermes.api.key}") String apiKey) {
        this.restClient = builder
                .baseUrl(baseUrl)
                .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
                .build();
    }

    /** 與 Agent 對話；sessionKey 相同即延續同一段對話（null = 無狀態）。 */
    public ChatResult chat(String message, String sessionKey) {
        Map<String, Object> body = Map.of(
                "model", "hermes-agent",
                "messages", List.of(Map.of("role", "user", "content", message)),
                "stream", false);

        RestClient.RequestBodySpec spec = restClient.post()
                .uri("/v1/chat/completions")
                .contentType(MediaType.APPLICATION_JSON);
        if (sessionKey != null && !sessionKey.isBlank()) {
            spec = spec.header("X-Hermes-Session-Key", sessionKey);
        }
        ChatCompletion completion = spec.body(body).retrieve().body(ChatCompletion.class);
        if (completion == null || completion.choices() == null || completion.choices().isEmpty()) {
            throw new HermesException("empty response from Hermes");
        }
        Choice choice = completion.choices().get(0);
        if ("error".equals(choice.finishReason()) || "cancelled".equals(choice.finishReason())) {
            throw new HermesException("agent run " + choice.finishReason());
        }
        int tokens = completion.usage() == null ? 0 : completion.usage().totalTokens();
        return new ChatResult(choice.message().content(), choice.finishReason(), tokens);
    }

    /** 以技能執行：在訊息前加上 /<skill-name>（例如內建的 requesting-code-review）。 */
    public ChatResult runSkill(String skillName, String message, String sessionKey) {
        if (!skillName.matches("[a-z0-9][a-z0-9-]{0,63}")) {
            throw new IllegalArgumentException("invalid skill name");
        }
        return chat("/" + skillName + " " + message, sessionKey);
    }

    public record ChatResult(String content, String finishReason, int totalTokens) { }

    record ChatCompletion(List<Choice> choices, Usage usage) { }

    record Choice(Message message,
                  @com.fasterxml.jackson.annotation.JsonProperty("finish_reason") String finishReason) { }

    record Message(String role, String content) { }

    record Usage(@com.fasterxml.jackson.annotation.JsonProperty("total_tokens") int totalTokens) { }

    public static class HermesException extends RuntimeException {
        public HermesException(String msg) {
            super(msg);
        }
    }
}
```

```yaml
# application.yml
hermes:
  api:
    url: http://127.0.0.1:8642
    key: ${HERMES_API_KEY}     # 由環境變數或秘密管理系統注入
```

> ⚠️ **更正**：舊版範例在建構子中使用 `@Value` 欄位（`builder.baseUrl(agentUrl)`），但欄位注入發生在建構子**之後**，因此 `agentUrl` 會是 `null`。上例改用建構子參數注入。另外內建技能中沒有 `code-review`，應使用 `requesting-code-review`。✅ 本段 Java 以 `JavacTask.parse()`（JDK 21）通過語法驗證。

#### 8.3.2 REST Controller

```java
@RestController
@RequestMapping("/api/assistant")
public class AssistantController {

    private final HermesAgentClient agentClient;

    public AssistantController(HermesAgentClient agentClient) {
        this.agentClient = agentClient;
    }

    @PostMapping("/chat")
    public HermesAgentClient.ChatResult chat(@RequestBody @Valid ChatRequest request,
                                             @RequestHeader("X-User-Id") String userId) {
        String sessionKey = request.sessionKey() == null ? null : userId + ":" + request.sessionKey();
        return agentClient.chat(request.message(), sessionKey);
    }

    @PostMapping("/code-review")
    public HermesAgentClient.ChatResult codeReview(@RequestBody @Valid CodeReviewRequest request,
                                                   @RequestHeader("X-User-Id") String userId) {
        String prompt = "請審查以下程式碼的安全性和品質：\n```java\n" + request.code() + "\n```";
        return agentClient.runSkill("requesting-code-review", prompt, userId + ":review");
    }

    public record ChatRequest(@NotBlank @Size(max = 20000) String message, String sessionKey) { }

    public record CodeReviewRequest(@NotBlank @Size(max = 200000) String code) { }
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
        session_key: sessionId.value
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

#### 8.5.1 API 規格（Facade 端點 → Hermes API 對照）

| Method | Facade 端點 | 轉送到 Hermes | 說明 |
| -------- | ---------- | ------ | ------ |
| POST | `/api/agent/chat` | `POST /v1/chat/completions` | 對話（同步回應） |
| POST | `/api/agent/stream` | `POST /v1/chat/completions`（`stream: true`） | 對話（SSE 串流） |
| POST | `/api/agent/runs` | `POST /v1/runs` | 長時間任務；回傳 `run_id` |
| GET | `/api/agent/runs/{id}/events` | `GET /v1/runs/{run_id}/events` | 任務事件串流 |
| POST | `/api/agent/runs/{id}/stop` | `POST /v1/runs/{run_id}/stop` | 停止任務 |
| POST | `/api/agent/runs/{id}/approval` | `POST /v1/runs/{run_id}/approval` | 由人工回覆審批 |
| GET／POST | `/api/agent/jobs` | `GET／POST /api/jobs` | 背景排程工作 |
| GET | `/api/agent/models` | `GET /v1/models` | 可用模型 |
| GET | `/api/agent/health` | `GET /health` | 健康檢查 |

> 💡 技能清單、Session 管理與用量統計屬於管理功能，建議由 Dashboard（或 `hermes sessions`／`hermes insights` CLI）提供，**不要**對一般業務使用者開放。

#### 8.5.2 整合架構圖

```mermaid
graph LR
    subgraph CA["Client Apps"]
        WEB_APP["Web Application<br/>Vue / React"]
        MOBILE["Mobile App"]
    end

    subgraph APIGW["API Gateway"]
        NGINX["Kong / Nginx<br/>SSO + Rate Limit + X-User-Id 注入"]
    end

    subgraph FAC["Agent Facade"]
        SVC["FastAPI / Spring Boot<br/>業務規則、輸入驗證、稽核日誌"]
    end

    subgraph HOST["Hermes 主機（單一 Gateway）"]
        GW["API Server :8642"]
        P1["Profile: general"]
        P2["Profile: code-review"]
        P3["Profile: security"]
    end

    WEB_APP --> NGINX
    MOBILE --> NGINX
    NGINX --> SVC
    SVC -->|"/v1/..."| GW
    SVC -->|"/p/code-review/v1/..."| GW
    SVC -->|"/p/security/v1/..."| GW
    GW --> P1
    GW --> P2
    GW --> P3
```

> **最佳實踐**：企業 Web 整合請使用 Facade 中間層（FastAPI／Spring Boot），**不要**把 Hermes API Server 直接暴露給終端使用者，也不要以子行程呼叫 CLI。Facade 負責：（1）統一 SSO 與授權，並把使用者身分轉成 session key；（2）請求限流與輸入長度限制；（3）業務規則與稽核日誌；（4）只開放業務需要的端點。API Server 本身只綁定 `127.0.0.1` 或內部網段，並使用長且隨機的 `API_SERVER_KEY`。

### 8.6 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 沒有以子行程包裝 CLI | 在程式碼中搜尋 `subprocess`、`ProcessBuilder` 與 `hermes chat` | 沒有結果；一律呼叫 API Server |
| 2 | API Server 已啟用且有認證 | `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8642/v1/models` 不帶 Token | 回傳 401 |
| 3 | Session 依使用者隔離 | 以兩個不同的 `X-User-Id` 送出相同 `session_key` | 兩者的對話歷史互不可見 |
| 4 | 結束狀態有處理 | 檢查程式碼對 `finish_reason` 的判斷 | `error`／`cancelled` 視為失敗；`length` 視為不完整但可用 |
| 5 | 串流解析正確 | 執行附錄 E.3 的 `test_facade.py` | 9/9 PASS |
| 6 | 金鑰不在程式碼中 | `grep -rn 'API_SERVER_KEY\|Bearer ' src/` | 只有從環境變數讀取 |
| 7 | Java 設定注入正確 | 人工審查 | 以建構子參數注入 `@Value`，沒有在建構子中使用尚未注入的欄位 |

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
# ❌ 不要這樣做：金鑰寫在 shell 歷史、腳本或版控中
export ANTHROPIC_API_KEY=sk-ant-real-key-here

# ✅ 應該這樣做：由秘密來源在啟動時注入，.env 只保留 bootstrap token
hermes secrets bitwarden setup --project-id 00000000-0000-0000-0000-000000000000
hermes secrets bitwarden status
chmod 600 ~/.hermes/.env
```

> ⚠️ **更正**：Hermes 的 `.env` **不支援** `${vault:...}` 這類間接引用語法。要從 Vault 類系統取值，請使用官方的秘密來源（Bitwarden、1Password，或以外掛實作的 `SecretSource`），或由部署平台（K8s Secret、systemd `LoadCredential`）在啟動前注入環境變數。

#### 9.1.2 指令審批（Command Approval）

```yaml
# ~/.hermes/config.yaml — 危險指令審批（v0.23.0 鍵名）
approvals:
  mode: smart                # smart（預設，推薦）／manual／off
  cron_mode: deny            # 無人值守的 Cron：危險指令一律拒絕
  single_query_mode: deny    # hermes -z／chat -q
  unattended_mode: deny      # Webhook／API Server 等無人可回答的介面
  deny:                      # 自訂拒絕規則：即使 YOLO 模式也會阻擋
    - "git push --force*"
    - "kubectl delete *"
command_allowlist:           # 永久允許：精確文字、glob 或危險規則名稱
  - "git status"
  - "git diff *"
  - "git log *"
  - "mvn test"
  - "mvn verify"
  - "npm test"
  - "python -m pytest *"
```

**審批模式比較**：

| 模式 | 說明 | 適用環境 |
| ------ | ------ | ---------- |
| `manual` | 危險指令一律詢問使用者 | 高安全環境（銀行核心系統） |
| `smart`（預設） | 由輔助 LLM 評估風險：低風險自動核准、真正危險的自動拒絕、不確定才詢問 | 一般企業（推薦） |
| `off` | 關閉所有審批，等同 `--yolo` | **僅限可拋棄的容器或 CI** |

```bash
# 審批規則試算（不實際執行）
hermes approvals test "rm -rf ./build"
hermes approvals test "git push --force origin main" --json
hermes approvals suggest --days 30        # 依歷史紀錄建議可加入允許清單的指令
```

> ⚠️ **更正**：舊版文件的 `security.command_approval`（`always`／`smart`／`never`／`yolo`）與 `security.allowed_commands` 都不是有效設定鍵；正確為 `approvals.mode`（`smart`／`manual`／`off`）與頂層 `command_allowlist`。

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
# ~/.hermes/config.yaml — 成本控制
model:
  provider: anthropic
  default: claude-sonnet-5-5

auxiliary:                    # 輔助任務改用低成本模型（各任務分開設定）
  compression:
    provider: nous
    model: nvidia/nemotron-3-ultra:free
  title_generation:
    provider: nous
    model: nvidia/nemotron-3-ultra:free

compression:
  enabled: true
  threshold: 0.5              # 上下文使用 50% 時觸發壓縮（預設）
  target_ratio: 0.2           # 壓縮後目標比例
  protect_last_n: 20          # 保留最近 20 則訊息不壓縮

delegation:
  max_concurrent_children: 4  # 收斂並行子代理（預設 10）
  max_iterations: 120         # 收斂子代理迭代上限（預設 250）
```

> ⚠️ **更正**：舊版範例的 `context.auto_compress`／`context.compress_threshold` 不是有效設定；壓縮設定在頂層 `compression:`（`context:` 區塊用於選擇 context engine）。

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
# - 最常用工具：terminal(38%), write_file(25%)
```

### 9.3 效能優化

#### 9.3.1 Context Compaction（上下文壓縮）

```text
/compress            # 手動壓縮目前上下文
```

```yaml
# ~/.hermes/config.yaml — 自動壓縮
compression:
  enabled: true
  threshold: 0.5
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

# Agent 使用 terminal 工具的 background + notify_on_complete
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
hermes logs                         # 預設顯示 agent.log 最後幾行
hermes logs -f                      # 持續追蹤（tail -f）
hermes logs errors -n 200           # 檢視 errors.log 最後 200 行
hermes logs gateway --since 1h      # Gateway 日誌，最近 1 小時
hermes logs --level WARNING --session <session_id>
hermes logs -f | grep tool_call     # 關鍵字過濾請搭配 grep（沒有 --filter 旗標）
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
| Health Check | Docker／K8s 探測 Gateway API Server 的 `GET /health`（例如 `curl -fsS http://127.0.0.1:8642/health`）；深入診斷用 `GET /health/detailed` 或 `hermes doctor`（沒有 `--quick` 旗標） |
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

> **企業建議**：Hermes Agent 的差異化優勢在於「多平台入口 + 持久記憶 + 自我學習」的**通用型助理與跨平台自動化場景**；若核心需求是**深度軟體工程／大型程式碼庫導覽**，建議將 Claude Code、Codex CLI 等納入並列評估，而非視為互斥的單選題——兩者也可透過 6.9 節 Plugin 系統或 `hermes import-agent`／`hermes migrate openclaw` 併存或漸進遷移。

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

### 9.9 v0.22／v0.23 新增的安全與治理議題

#### 9.9.1 已知公開弱點（GitHub Advisory Database）

Nous Research **至今仍未在官方倉庫發布任何 Repository Security Advisory**（2026-11-08 以 `gh api repos/NousResearch/hermes-agent/security-advisories` 查證，結果為空）。但 GitHub Advisory Database 已收錄 10 筆 `hermes-agent`（pip 生態系）公告：

| GHSA | CVE | 嚴重度 | 影響範圍 | 首個修補版本 | 摘要 |
| --- | --- | --- | --- | --- | --- |
| GHSA-4pqm-j46f-795x | CVE-2026-53869 | High | < 0.16.0 | 0.16.0 | WebSocket 端點 DNS rebinding，可繞過 Host／Origin 驗證 |
| GHSA-99f9-j8r3-p853 | CVE-2026-53870 | Medium | < 0.16.0 | 0.16.0 | `response_store.db`、`webhook_subscriptions.json` 以 0644 建立（全員可讀） |
| GHSA-pmqc-57g8-c22c | CVE-2026-10224 | Medium | <= 0.19.0 | **未列出** | 資源耗用失控 |
| GHSA-xq8w-9jvx-gm3v | CVE-2026-10221 | Medium | <= 0.19.0 | **未列出** | Injection |
| GHSA-mv8x-fg99-32mf | CVE-2026-10222 | Low | < 0.18.0 | 0.18.0 | Injection |
| GHSA-33qv-c5qm-799v | CVE-2026-10223 | Low | < 0.15.0 | 0.15.0 | Injection |
| GHSA-cv5c-mh6j-wvp9 | CVE-2026-9369 | Low | < 0.15.0 | 0.15.0 | Incorrect Comparison |
| GHSA-pgp4-xr4j-h5cg | CVE-2026-9366 | Medium | < 0.15.0 | 0.15.0 | Injection |
| GHSA-238w-f66p-w349 | CVE-2026-9353 | Medium | < 0.15.0 | 0.15.0 | Injection |
| GHSA-wm96-9gfh-vvgq | CVE-2026-9368 | Medium | < 0.11.0 | 0.11.0 | Sandbox issue |

> ⚠️ **判讀方式**：v0.23.0 不在上述任何一筆的宣告影響範圍內；但 CVE-2026-10224 與 CVE-2026-10221 沒有列出修補版本，**無法從公告本身確認修補狀態**（列入附錄 E.4）。另外，這些公告的 pip 版本號與 Hermes 的 Release 版本號是同一套 SemVer，但官方已停止發行 PyPI 套件，請以 Release tag 對照。企業應把以下查詢納入每月的弱點情資作業：
>
> ```bash
> gh api "advisories?ecosystem=pip&affects=hermes-agent&per_page=50" \
>   --jq '.[] | [.ghsa_id, .cve_id, .severity, .published_at[0:10]] | @tsv'
> hermes security audit --json --fail-on high     # 依賴、MCP、外掛的供應鏈稽核
> ```

#### 9.9.2 tirith 移除後的掃描替代方案（v0.22.0）

v0.22.0 移除了內建的 tirith 掃描器。下列機制仍在，應改為企業的標準檢查點：

| 掃描對象 | 指令／機制 | 何時執行 |
| --- | --- | --- |
| 依賴、MCP、外掛供應鏈 | `hermes security audit --fail-on high` | CI 與每次升級後 |
| Hub 技能 | 安裝時自動隔離掃描；`hermes skills audit` 重新掃描 | 每週 |
| 外掛 | `hermes plugins validate <path>`（含 `security scan`）；Catalog 收錄時已掃描 | 導入新外掛前 |
| 寫入保護 | `security.protected_instruction_files: true`（預設），`AGENTS.md`／技能／記憶寫入需審批 | 持續 |

#### 9.9.3 外掛與 Catalog 的信任邊界

- **Catalog 審核是單一時間點的人工審閱**，不是安全稽核；只代表「被釘選的那個 commit 有人看過」。
- **Desktop 外掛無沙箱**：`desktop/plugin.js` 在 App 內與 App 本身同權限執行。
- **Python 外掛預設在主行程執行**：企業應設定 `plugins.isolation: host`，讓第三方外掛在每個 Profile 獨立的行程中執行（見 6.9 節）。
- **自動更新要審慎**：`hermes plugins auto-update` 會套用 Catalog 中經審核的新 pin，但等於把變更時程交給上游；受管環境建議關閉自動更新，改走內部變更流程。
- **禁止執行期自動安裝**：`security.allow_lazy_installs: false` 可阻止 Hermes 在執行中自動安裝外掛或依賴（代價是升級時遷移出核心的 Provider 不會被自動補裝，需手動安裝）。

#### 9.9.4 Webapp 與遠端存取

- Webapp 預設關閉；開啟後，**登入者即等同主機上執行 Hermes 的 OS 使用者**，可執行任意指令。
- 非 loopback 存取必須啟用 Dashboard 登入閘門；對外網路請使用 OAuth/OIDC 並強制 HTTPS（`webapp.public_url`）。
- 優先使用 SSH tunnel、Tailscale 或企業 VPN；`hermes webapp --sign-out` 可一次登出所有瀏覽器。

#### 9.9.5 Connectors、密碼管理器與付費工具

| 功能 | 風險 | 建議控制 |
| --- | --- | --- |
| Connectors（v0.22.0） | Agent 以使用者身分讀寫 SaaS 資料，資料流經 Nous 託管基礎設施 | 依資料分級決定是否允許；不需要時以 `tools.connectors.enabled: false` 關閉 |
| 瀏覽器憑證庫／密碼管理器（v0.22.0／v0.23.0） | 自動登入網站 | 只使用 Verified 的密碼管理器外掛；`hermes vault key migrate --to keychain` 把金鑰移到 OS keychain；卡片與地址填寫需使用者確認 |
| 付費 MCP 工具（v0.23.0） | 意外高額花費 | 對每個付費伺服器宣告 `tool_costs` 與 `spend_limit`；Cron 與 `chat -q` 超限時會直接拒絕 |
| Local Models（v0.22.0） | 模型檔來源與授權 | 機敏資料可改用本機推理，資料不出機器；模型下載來源需納入軟體資產管理 |

#### 9.9.6 Session 保存與稽核

v0.22.0 的 release notes 寫「`sessions.auto_prune` 預設開啟」，但 **v0.23.0 的原始碼與文件都是預設關閉**，改為在磁碟空間不足時詢問一次（`/autoprune on|off|later`）。有稽核保存義務的組織，應明確寫入設定，而不是依賴預設值：

```yaml
# ~/.hermes/config.yaml
sessions:
  auto_prune: false          # 由組織的保存政策決定；需清理時以 hermes sessions archive／export 先保存
  retention_days: 365
```

```bash
hermes sessions export --format md --redact --older-than 90d --dry-run   # 先預覽
hermes sessions archive --older-than 180d --yes
```

### 9.10 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 審批設定有效 | `hermes config get approvals.mode`、`hermes approvals test "rm -rf /"` | 模式為 `smart` 或 `manual`；試算結果為拒絕或需審批 |
| 2 | 無人值守介面不會自動放行 | `hermes config get approvals.cron_mode`、`unattended_mode` | 皆為 `deny` |
| 3 | 秘密沒有落地 | `grep -rnE 'sk-|xox[bp]-|ghp_' ~/.hermes/*.yaml`；`ls -l ~/.hermes/.env` | 沒有結果；`.env` 為 `-rw-------` |
| 4 | 供應鏈稽核通過 | `hermes security audit --fail-on high` | exit 0 |
| 5 | 外掛隔離 | `hermes config get plugins.isolation` | `host` |
| 6 | Webapp 未裸露 | `hermes webapp --status`；外部主機 `curl http://<host>:9120` | 未啟用，或需要登入；沒有明文 HTTP 對外 |
| 7 | 弱點情資已更新 | 執行 9.9.1 的 `gh api` 查詢 | 沒有影響目前版本的新公告；若有，已建立處置工單 |
| 8 | Session 保存符合政策 | `hermes config get sessions.auto_prune`、`retention_days` | 與組織保存政策一致，且明確寫在設定檔中 |
| 9 | 成本上限已設定 | `hermes config get delegation.max_concurrent_children`；檢查付費 MCP 的 `spend_limit` | 有明確上限 |

---

## 第十章：部署與維運（DevOps）

> **本章前提（v0.23.0）**：每台主機（或每個 Pod）只能有**一個** Gateway 擁有 `state.db`。官方映像是 Docker Hub 的 `nousresearch/hermes-agent`，資料掛載在 `/opt/data`，Gateway 以 `gateway run` 啟動，並在容器內由 s6-overlay 監督。下列範例都依此設計，並已通過 YAML 結構驗證（見 10.6 節與附錄 E.3）。

### 10.1 Docker 部署

#### 10.1.1 生產級衍生映像

官方建議以官方映像為基底加裝工具，而不是從 `python:*-slim` 自行組裝。自行組裝必須重現 PM、釘選版 Node.js、s6-overlay 與權限模型，很容易與官方行為不一致。

```dockerfile
# Dockerfile.production — 以官方映像為基底（版本請與 Release tag 一致）
FROM nousresearch/hermes-agent:0.23.0

USER root
# 只加裝企業必要的工具；套件清單納入軟體資產管理
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates jq \
    && rm -rf /var/lib/apt/lists/*

# 企業內部 CA（若有 TLS 攔截的出口代理）
COPY corp-root-ca.crt /usr/local/share/ca-certificates/corp-root-ca.crt
RUN update-ca-certificates

# 健康檢查：Gateway 的 API Server 必須啟用（API_SERVER_ENABLED=true）
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python3 -c "import sys,urllib.request; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8642/health', timeout=5).status == 200 else 1)"

# 保留官方 root entrypoint；s6 會在執行期自動降權為 hermes 使用者
```

> ⚠️ **更正**：舊版範例的 `HEALTHCHECK CMD hermes doctor --quick` 中，`--quick` 旗標不存在；以 `python:3.11-slim` 自建並手動安裝 Node.js 26 的做法，也與 v0.22.0 起「Python 3.14 + PM 管理 Node.js」的官方執行環境不一致。

#### 10.1.2 Docker Compose 生產部署

```yaml
# docker-compose.production.yml
services:
  hermes:
    image: corp/hermes:0.23.0-1          # 由 Dockerfile.production 建置的衍生映像
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "127.0.0.1:8642:8642"            # API Server：只綁 loopback，對外經反向代理
    volumes:
      - hermes-data:/opt/data            # 具名 volume（原生檔案系統，WAL 可正常運作）
    env_file:
      - ./secrets/hermes.env             # 權限 0600；僅含 bootstrap token 與 API_SERVER_KEY
    environment:
      - API_SERVER_ENABLED=true
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: "2.0"
    logging:
      driver: json-file
      options:
        max-size: "20m"
        max-file: "5"

volumes:
  hermes-data:
```

```bash
docker compose -f docker-compose.production.yml up -d
docker compose -f docker-compose.production.yml ps          # STATUS 應顯示 (healthy)
docker exec hermes hermes doctor
docker exec hermes hermes profile create team-ops           # 新增 Profile：同一容器、同一 Gateway
```

> 💡 **一個容器、多個 Profile**：v0.22.0 起官方建議以單一容器服務多個 Profile（s6 會為每個 Profile 監督 Gateway 槽位），而不是每個 Profile 一個容器；這樣只有一份映像與快取、一個備份目錄。只有在需要 OS 層級隔離（不同 UNIX 使用者、不同資料分級）時才拆成多個容器，而且每個容器要使用**自己的** volume。

### 10.2 Kubernetes 部署

#### 10.2.1 K8s Deployment（單一狀態擁有者）

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hermes
  namespace: ai-agents
  labels:
    app: hermes
spec:
  replicas: 1                     # Gateway 是 state.db 的唯一擁有者，不可多副本
  strategy:
    type: Recreate                # 先停舊 Pod 再起新 Pod，避免兩個 Pod 同時開啟同一個 state.db
  selector:
    matchLabels:
      app: hermes
  template:
    metadata:
      labels:
        app: hermes
    spec:
      terminationGracePeriodSeconds: 120   # 讓 Gateway 有時間排空進行中的對話
      securityContext:
        fsGroup: 10000
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: hermes
          image: registry.corp.example/hermes:0.23.0-1
          imagePullPolicy: IfNotPresent
          args: ["gateway", "run"]
          ports:
            - name: api
              containerPort: 8642
          env:
            - name: API_SERVER_ENABLED
              value: "true"
          envFrom:
            - secretRef:
                name: hermes-secrets        # API_SERVER_KEY、BWS_ACCESS_TOKEN 等
          resources:
            requests:
              cpu: "500m"
              memory: 2Gi
            limits:
              cpu: "2"
              memory: 4Gi
          startupProbe:
            httpGet:
              path: /health
              port: api
            periodSeconds: 10
            failureThreshold: 30
          livenessProbe:
            httpGet:
              path: /health
              port: api
            periodSeconds: 30
            timeoutSeconds: 5
          readinessProbe:
            httpGet:
              path: /health
              port: api
            periodSeconds: 10
          volumeMounts:
            - name: data
              mountPath: /opt/data
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: hermes-data
---
apiVersion: v1
kind: Service
metadata:
  name: hermes
  namespace: ai-agents
spec:
  type: ClusterIP
  selector:
    app: hermes
  ports:
    - name: api
      port: 8642
      targetPort: api
---
apiVersion: v1
kind: Secret
metadata:
  name: hermes-secrets
  namespace: ai-agents
type: Opaque
stringData:
  API_SERVER_KEY: "replace-with-a-long-random-string"   # 正式環境請改用 External Secrets／Sealed Secrets
```

> ⚠️ **更正**：舊版範例使用 `replicas: 2`、`RollingUpdate`（`maxSurge: 1`），並以 `ReadWriteMany` PVC 讓多個 Pod 共用資料。在 v0.23.0 中，這會讓兩個 Gateway 同時寫入同一個 `state.db`，造成鎖定錯誤甚至資料毀損；健康檢查用的 `hermes doctor --quick` 旗標也不存在。需要水平擴展時，請依團隊**分成多個 Deployment**，各自有自己的 PVC（見 2.5 節）。

#### 10.2.2 PersistentVolumeClaim

```yaml
# k8s/pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: hermes-data
  namespace: ai-agents
spec:
  accessModes:
    - ReadWriteOnce               # 單一節點讀寫；不要用 RWX 共享 state.db
  storageClassName: standard-ssd  # 區塊儲存（非 NFS）
  resources:
    requests:
      storage: 20Gi
```

> ⚠️ 若叢集只能提供 NFS 類儲存，請在 `config.yaml` 設定 `database.journal_mode: delete`，並在建立 Pod **之前**就寫好（既有的 WAL 資料庫不會被線上降級，需停機後離線轉換）。

### 10.3 CI/CD 流程

#### 10.3.1 GitHub Actions Pipeline

企業的 Pipeline 不需要建置 Hermes 本身；它的工作是**跟隨官方 Release 重建衍生映像，並在部署前完成稽核**。

```yaml
# .github/workflows/hermes-image.yml
name: Hermes image

on:
  workflow_dispatch:
    inputs:
      hermes_version:
        description: "官方 Release 版本（例如 0.23.0）"
        required: true
  pull_request:
    paths: ["deploy/hermes/**"]

permissions:
  contents: read

jobs:
  build-scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    env:
      HERMES_VERSION: ${{ inputs.hermes_version || '0.23.0' }}
      IMAGE: ghcr.io/${{ github.repository_owner }}/hermes
    steps:
      - uses: actions/checkout@v4

      - name: Build derived image
        run: |
          sed -i "s|^FROM nousresearch/hermes-agent:.*|FROM nousresearch/hermes-agent:${HERMES_VERSION}|" deploy/hermes/Dockerfile.production
          docker build -f deploy/hermes/Dockerfile.production -t "$IMAGE:${HERMES_VERSION}-${GITHUB_RUN_NUMBER}" deploy/hermes

      - name: Smoke test
        run: |
          docker run --rm "$IMAGE:${HERMES_VERSION}-${GITHUB_RUN_NUMBER}" --version | tee version.txt
          grep -q "v${HERMES_VERSION}" version.txt

      - name: Supply-chain audit (fails on high)
        run: |
          docker run --rm "$IMAGE:${HERMES_VERSION}-${GITHUB_RUN_NUMBER}" security audit --fail-on high

      - name: Validate committed config keys
        run: |
          docker run --rm -v "$PWD/deploy/hermes/config:/opt/data" \
            "$IMAGE:${HERMES_VERSION}-${GITHUB_RUN_NUMBER}" config check

      - name: Push
        if: github.event_name == 'workflow_dispatch'
        run: |
          echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u "${{ github.actor }}" --password-stdin
          docker push "$IMAGE:${HERMES_VERSION}-${GITHUB_RUN_NUMBER}"
```

> 💡 **審查重點**：舊版 Pipeline 在 CI 中執行 `pip install -e ".[all,dev]"` 與 `safety check`，把 Hermes 當成自家應用程式建置，這與官方「不支援建置 wheel／sdist」的立場不符，也不會產生可部署的官方執行環境。另外，`config check` 只檢查設定版本與環境變數，**不檢查未知鍵**；設定鍵的正確性請在 PR 階段以附錄 E 的 `check_doc.py` 或 `hermes config set` 驗證。

### 10.4 升級與回退

#### 10.4.1 Kubernetes 升級策略

```yaml
# k8s/deployment.yaml 的 spec.strategy
spec:
  strategy:
    type: Recreate     # 不可使用 RollingUpdate：新舊 Pod 不可同時開啟 state.db
```

升級流程：

1. 執行 `kubectl exec deploy/hermes -- hermes backup -o /opt/data/backups/pre-0.23.0.zip`，建立完整備份。
2. 修改 Deployment 的映像標籤後 `kubectl apply`。Recreate 會先停止舊 Pod（`terminationGracePeriodSeconds` 讓 Gateway 排空對話），再啟動新 Pod。
3. 容器啟動時會先執行非互動式的設定 schema 遷移，並在 `config.yaml`／`.env` 旁寫入帶時間戳的備份；需要先人工檢查時，可設定 `HERMES_SKIP_CONFIG_MIGRATION=1`。
4. 驗證：`kubectl exec deploy/hermes -- hermes doctor`，並確認 `/health` 為 200。

#### 10.4.2 非容器環境的內建升級

```bash
hermes update --check          # 只預覽
hermes update --plan           # 檢視整個 Profile 群的升級計畫
hermes update --backup         # 升級前先做完整備份（建議）
hermes update                  # 依 stable 通道升到最新 Release
hermes doctor                  # 升級後驗證
```

> ⚠️ **回退限制（v0.23.0）**：新版 Gateway 一旦寫入 `state.db`，舊版本就**不能**再使用該資料庫。`hermes update` 會拒絕切回早於 Gateway 執行期的版本；正在執行的 Gateway 若被切回舊版，約 30 秒內會自行停止。要回退，必須先 `hermes gateway stop`，切回舊版後，再還原升級前的快照（`/snapshot restore <id>`）或完整備份（`hermes import <backup.zip>`）；升級後新增的對話不在還原範圍內。

### 10.5 災難復原（DR）

#### 10.5.1 備份策略

| 層級 | 方法 | 內容 | 頻率建議 |
| --- | --- | --- | --- |
| 完整備份 | `hermes backup` | 資料根目錄下的設定、**憑證（`.env`、`auth.json`）**、記憶、技能、Session、所有 Profile | 每日 + 每次升級前 |
| 快速快照 | `hermes backup --quick --label <名稱>` | 關鍵狀態檔（config、`state.db`、`.env`、auth、cron） | 每小時或重大變更前 |
| 單一 Profile | `hermes profile export <name>` | 單一 Profile 的 `SOUL.md`、記憶、Session、技能（**不含**憑證） | 移轉或分享時 |
| 儲存層快照 | PVC VolumeSnapshot／磁碟快照 | 整個 `/opt/data` | 依儲存平台政策 |

> 🔐 **完整備份含有憑證**，必須加密後才能離開主機，並限制存取權限。完整備份**不包含**：原始碼與依賴環境、下載的模型與執行期、建置快取、checkpoints、瀏覽器設定檔、SQLite 附屬檔與 PID 檔。備份完成時若有檔案複製失敗會列出清單，**請檢查清單後再刪除來源**。

#### 10.5.2 備份腳本

```bash
#!/usr/bin/env bash
# backup-hermes.sh — 每日完整備份 + 加密 + 異地保存（以 cron 或 K8s CronJob 執行）
set -euo pipefail

BACKUP_DIR="/var/backups/hermes"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT="$BACKUP_DIR/hermes-backup-$STAMP.zip"
RECIPIENT="age1examplepublickeyreplacewithyourown0000000000000000000000"

mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

# 1) 官方完整備份（--keep 只保留本機最新 N 份）
hermes backup --output "$OUT" --keep 3

# 2) 加密（完整備份含 .env 與 auth.json）
age --encrypt --recipient "$RECIPIENT" --output "$OUT.age" "$OUT"
shred -u "$OUT"

# 3) 異地保存（物件儲存應啟用版本控制與 Object Lock）
aws s3 cp "$OUT.age" "s3://corp-hermes-backup/$(hostname)/" --only-show-errors

echo "backup ok: $OUT.age"
```

```bash
# 還原演練（在隔離主機上）
age --decrypt --identity ~/.config/age/hermes.key --output restore.zip hermes-backup-20261108-020000.zip.age
hermes import restore.zip
hermes doctor
hermes sessions list --limit 5
```

> ⚠️ **更正**：舊版腳本以 `sqlite3 "$HERMES_HOME/sessions.db" ".backup ..."` 備份 Session，但 v0.23.0 的資料庫是 `state.db`；而且逐檔複製會漏掉 `auth.json`、各 Profile 與 cron 狀態。請改用 `hermes backup`。

#### 10.5.3 RTO / RPO 建議

| 情境 | RPO | RTO | 作法 |
| --- | --- | --- | --- |
| 單一 Pod／容器故障 | 0（同一個 volume） | < 5 分鐘 | s6／K8s 自動重啟；Recreate 重新掛載同一個 PVC |
| 節點或磁碟故障 | 最近一次快照或備份 | < 1 小時 | 從 VolumeSnapshot 或 `hermes import` 還原到新節點 |
| 誤操作（刪除技能、錯誤升級） | 最近一次快速快照 | < 30 分鐘 | `/snapshot restore <id>`；技能可用 `hermes curator rollback` |
| 機房級災難 | 24 小時（每日異地備份） | < 4 小時 | 異地主機解密 `hermes import`，重新綁定訊息平台 Token |

> **實務案例**：某銀行團隊在 Kubernetes 上依「研發」「維運」分成兩個 Deployment，各自使用 RWO 的 SSD PVC；每日 02:00 由 CronJob 以 `kubectl exec` 執行 `hermes backup`，並以 age 加密後上傳到啟用 Object Lock 的 S3。每季在隔離環境做一次還原演練，量測實際 RTO。

### 10.6 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 單一狀態擁有者 | `kubectl get deploy hermes -o jsonpath='{.spec.replicas} {.spec.strategy.type}'` | `1 Recreate` |
| 2 | PVC 存取模式 | `kubectl get pvc hermes-data -o jsonpath='{.spec.accessModes}'` | `["ReadWriteOnce"]`，且非 NFS 儲存類別 |
| 3 | 健康檢查正確 | `kubectl describe pod -l app=hermes` | Probe 為 `http-get :api/health`；沒有 `doctor --quick` |
| 4 | API Server 未對外裸露 | `kubectl get svc hermes`；`docker port hermes` | Service 為 ClusterIP；Docker 只綁 `127.0.0.1` |
| 5 | 映像版本已釘選 | 檢查 Deployment／compose 的 image | 使用 `X.Y.Z` 或 digest，與 Release tag 一致 |
| 6 | 備份可還原 | 在隔離環境執行 10.5.2 的還原演練 | `hermes doctor` 通過，Session 數量與來源相符 |
| 7 | 備份已加密 | 檢查備份儲存位置 | 只有 `.age`（或同等加密格式）檔案 |
| 8 | YAML 結構有效 | 以 `kubectl apply --dry-run=server -f k8s/` 或附錄 E.3 的 `validate_k8s.py` | 沒有錯誤；斷言 `replicas == 1`、`strategy == Recreate`、`accessModes == [ReadWriteOnce]` 成立 |

---

## 第十一章：升級與版本管理

### 11.1 升級策略

#### 11.1.1 版本號規則

Hermes Agent 的版本號與 Git tag 規則在 v0.21.6 改變過一次，查證或撰寫升級文件時要分清楚：

| 期間 | 版本號 | Git tag 範例 | 說明 |
| --- | --- | --- | --- |
| v0.21.5（2026-09-24）以前 | 語義化版本 | `v2026.8.31`（日期式） | GitHub Release 名稱寫成「Hermes Agent v0.21.0 (v2026.8.31)」 |
| v0.21.6（2026-10-08）起 | 語義化版本 | `v0.21.6`、`v0.22.0`、`v0.23.0` | 由新的穩定發行管線產出；原始碼安裝預設只在這些 tag 之間移動 |

```bash
# 查詢最新穩定版與本機版本
gh api repos/NousResearch/hermes-agent/releases/latest --jq '.tag_name + "  " + .published_at'
hermes --version
hermes update --check
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
    M --> N[hermes logs errors]
    N --> O{可修復?}
    O -->|是| P[修復後重試]
    O -->|否| Q[回滾到前版]
```

#### 11.1.3 升級指令

```bash
# 方式 1：原始碼安裝（install.sh／install.ps1）— 內建升級指令（推薦）
hermes update --check          # 預覽，不做任何變更
hermes update --backup         # 升級前先做完整備份
hermes update                  # 依通道（預設 stable）升到最新 Release
hermes update --yes            # 免確認（CI／自動化），等同 -y

# 方式 2：Desktop 套件
#   macOS：App 內 Update 控制（electron-updater）
#   Windows：MSIX 由 App Installer 更新；Microsoft Store 版由 Store 更新

# 方式 3：Docker（容器內不支援 hermes update）
docker pull nousresearch/hermes-agent:0.23.0
docker compose up -d           # 以新映像重建容器；資料 volume 保留

# 方式 4：Nix
nix profile upgrade --all      # 或更新 flake input 後重新建置

# 升級後驗證
hermes --version
hermes config migrate
hermes doctor
```

> ⚠️ **已不適用的方式**：`pip install --upgrade hermes-agent`（PyPI 已於 v0.20.0 停止支援）、在原始碼目錄 `git pull origin main` 後 `uv pip install -e ".[all]"`（會繞過 PM 與穩定通道，且 v0.22.0 起 Python 版本由 PM 管理）、`ghcr.io/nousresearch/hermes-agent`（官方映像在 Docker Hub 的 `nousresearch/hermes-agent`）。

#### 11.1.4 升級注意事項（v0.8.0 特告）

| 項目 | 說明 |
| ------ | ------ |
| Skills 同步 | 升級後 bundled skills 會自動同步到所有 Profiles |
| Gateway 保護 | `hermes update` 不再 kill 正在運行的 gateway service |
| Config 驗證 | 啟動時會自動驗證 config.yaml 結構 |
| OpenClaw 移轉 | 當時使用 `hermes claw migrate`；v0.23.0 已改為 `hermes migrate openclaw`／`hermes import-agent openclaw`（見 11.3.1） |

#### 11.1.5 v0.12.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| Node.js | 建議升級至 v22 LTS，影響 TUI 冷啟動效能 |
| Secret Redaction | 預設已關閉，避免 patch 損壞，如需請手動啟用 |
| Pluggable Providers | 所有 Provider 已移至 `plugins/model-*` 架構 |
| Curator 預設啟用 | 自動技能維護預設開啟（v0.23.0 的關閉方式為 `curator.enabled: false`；當時文件寫的 `auxiliary.curator.enabled` 不是有效鍵） |
| Remote Model Catalog | OpenRouter / Nous Portal 模型目錄改為遠端拉取 |

#### 11.1.6 v0.13.0 升級特別注意事項

| 項目 | 說明 |
| ------ | ------ |
| Secret Redaction | **預設翻轉為開啟**（v0.23.0 鍵名為 `security.redact_secrets`，預設 `true`） |
| Checkpoints v2 | 新的 Checkpoint 格式，舊 Checkpoint 不會自動遷移，需要手動清除後重建 |
| `hermes update --yes` | 升級指令新增 `-y / --yes` 旗標，跳過確認直接升級（適合 CI） |
| ProviderProfile ABC | 自訂 Provider 需改寫為繼承 `ProviderProfile` ABC 介面 |
| Docker Root 拒絕 | Gateway 現拒絕以 root 身份運行，必須使用非 root 使用者 |
| Windows 正式支援 | 原生 Windows 支援已為 GA（v0.16.0+），可透過 Desktop App 或 CLI 安裝 |
| `display.language` | 新增 i18n 設定項，支援 `zh`、`ja`、`de`、`es`、`fr`、`uk`、`tr` |
| Kanban | 當時預設停用；v0.23.0 沒有 `kanban.enabled` 開關，以 `hermes kanban init` 初始化看板、以 `kanban.dispatch_in_gateway` 控制調度 |

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
| Bitwarden Secrets | 新增 Bitwarden 秘密來源（v0.23.0 設定為 `secrets.bitwarden.enabled: true`，或執行 `hermes secrets bitwarden setup`） |
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

#### 11.1.15 v0.21.0 升級特別注意事項

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

#### 11.1.16 v0.21.0 → v0.23.0 升級特別注意事項（目前最新版本）

從 v0.21.x 升到 v0.23.0 要跨越兩個 Minor 版本與十多個補丁，下表是**必須處理**的破壞性變更。建議依「檢查方式」欄位逐項確認，並把結果附在變更單中。

| # | 版本 | 變更 | 影響 | 處理方式 | 檢查方式 |
| --- | --- | --- | --- | --- | --- |
| 1 | v0.22.0 | 受管安裝的執行環境改為 **Python 3.14** | KittenTTS 無法使用；自建映像若沿用 3.11 會與官方不一致 | 交給 PM 管理；Docker 改用官方映像為基底 | `hermes doctor`、`hermes --version` |
| 2 | v0.22.0 | **Windows Desktop 僅支援 MSIX**（Windows 11 22H2+），NSIS／MSI 停用；macOS App 僅 Apple Silicon | 舊安裝程式無法再更新 | 改以 `.appinstaller` 或 Microsoft Store 重新安裝 | 「設定 → 應用程式」中的套件類型 |
| 3 | v0.22.0 | **每台機器單一 Gateway**；`hermes update` 會把 per-profile Gateway 合併 | 具名 Profile 不能再自行啟動 Gateway（exit 78）；以 HTTP 進來的平台改用 `/p/<profile>/` 前綴 | 執行 `hermes gateway migrate --multiplex`；更新 Webhook URL | `hermes gateway status`；以 `hermes -p <name> gateway start` 測試，應被拒絕 |
| 4 | v0.22.0 | `session_reset` idle／daily 模式退役 | 對話不再定時重置；設定仍存在會記錄警告 | 移除 `session_reset` 設定，改由使用者 `/new`／`/reset` | `hermes logs --level WARNING` 不再出現相關警告 |
| 5 | v0.22.0 → v0.23.0 | `sessions.auto_prune`：release notes 寫預設開啟，**v0.23.0 實際預設關閉**，磁碟不足時詢問一次 | 保存政策可能與預期不同 | 在 `config.yaml` 明確設定 `sessions.auto_prune` 與 `retention_days` | `hermes config get sessions.auto_prune` |
| 6 | v0.22.0 | 記憶 Provider（Honcho、Supermemory、Hindsight、Mem0、OpenViking、Holographic）與 Home Assistant、Spotify、Langfuse **移到 Catalog 外掛** | 升級時自動安裝；`security.allow_lazy_installs: false` 或離線時不會自動安裝 | 預先 `hermes plugins install <name>` | `hermes plugins list`、`hermes memory status` |
| 7 | v0.22.0 | 移除外掛相容匯入層、**移除 `hermes sync`**、**移除 tirith 掃描器** | 自製外掛若使用舊匯入路徑會載入失敗；依賴 tirith 的流程失效 | 外掛改用 `register(ctx)` 公開 API；改用 `hermes security audit`／`hermes skills audit`（見 9.9.2） | `hermes plugins doctor` |
| 8 | v0.22.0 | 工具更名：`todo` → `todo_list`、`cronjob` → `cronjob_manage`、`process` → `process_manage` | 舊名仍可用，但新的技能與文件應改用新名 | 更新自訂技能與 toolset 清單 | 在技能目錄 `grep -rn '"todo"\|cronjob\b'` |
| 9 | v0.23.0 | **舊的 10 個 `browser_*` 工具與 agent-browser 全數移除**，只剩 `browser_exec`；Camofox 改為外掛 | 提示、技能、`toolsets` 清單中的舊工具名稱失效 | 改寫為 `browser_exec`；有用 Camofox 的環境會自動安裝外掛 | `grep -rn 'browser_navigate\|browser_click' ~/.hermes/skills` 無結果 |
| 10 | v0.23.0 | **`hermes mcp serve` 改為 `hermes mcp-serve`**（移到外掛） | 以 Hermes 作為 MCP Server 的用戶端設定**不會被自動改寫** | 更新 Claude Desktop／IDE 等 MCP 用戶端的啟動指令；`hermes plugins install mcp-serve` | 用戶端能列出 Hermes 的工具 |
| 11 | v0.23.0 | Desktop 需 macOS 13+、64 位元 Windows（Electron 44） | 舊作業系統上的 Desktop 無法啟動 | 升級作業系統或改用 CLI／Webapp | — |
| 12 | v0.23.0 | Word／PowerPoint／Excel 技能合併為 `microsoft-office` | 舊副本留在磁碟上，可能重複觸發 | 確認無自訂修改後刪除舊技能目錄 | `hermes skills list \| grep -i office` |
| 13 | v0.23.0 | **Gateway 擁有所有 Session**；`cron.bot_chat_delivery_timeout_seconds` 退役（設定遷移 v51） | 升級切換瞬間進行中的輸入標記為 `unknown`，**不會重播** | 升級前排空工作；升級後以 `/discard <admission_id>` 或 `hermes sessions discard <session> --yes` 確認 | `hermes sessions list`；Webapp 中舊對話需 `hermes sessions adopt` |
| 14 | v0.23.0 | **升級後不可回退**：新版 Gateway 寫過 `state.db` 後，舊版本無法使用 | 回退只能還原升級前備份 | 升級前一定執行 `hermes update --backup` 或 `hermes backup` | 備份檔存在且可在隔離環境 `hermes import` |
| 15 | v0.23.0 | Webapp 預設關閉 | 無影響；開啟前需完成資安審查 | 見 9.9.4 | `hermes webapp --status` |

**建議升級順序**：

```bash
# 0) 升級前
hermes --version                         # 記錄目前版本
hermes update --check                    # 確認目標版本
hermes backup -o ~/pre-0.23.0.zip        # 完整備份（含憑證，請加密保存）
hermes plugins list > ~/plugins-before.txt

# 1) 升級
hermes update --backup

# 2) 升級後
hermes config migrate
hermes doctor
hermes plugins list                      # 確認記憶 Provider 等外掛已自動安裝並啟用
hermes gateway status                    # 只有一個 Gateway
hermes sessions adopt --dry-run          # 檢視哪些舊對話需要被 Gateway 接管
```

> 💡 **一次跨多版的注意事項**：中間的 v0.21.6／v0.21.7 改變了更新通道（改追穩定 Release）。若你的安裝在 v0.21.7 以前一直追蹤 `main`，而本機 checkout 比最新 Release 還新，`hermes update` 會**停在原地**，等到有更新的 Release 才移動；這不是錯誤。

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

如果你之前使用 OpenClaw（或舊名 Clawdbot／Moltbot，與 Hermes 是不同的專案），可以用官方 `agent-importers` 外掛匯入設定。全新安裝時 `hermes setup` 偵測到 `~/.openclaw` 會主動詢問；既有安裝可執行：

```bash
hermes migrate openclaw --dry-run                 # 核心指令；缺少外掛時會自動安裝
hermes plugins install agent-importers            # 或手動安裝外掛（每個 Profile 一次）
hermes import-agent openclaw --dry-run            # 只預覽，不寫入
hermes import-agent openclaw                      # 先顯示計畫，確認後才寫入
hermes import-agent openclaw --preset full --migrate-secrets --yes   # 含 API Key 與 Bot Token（無人值守）
```

> ⚠️ **更正**：舊版文件的 `hermes claw migrate` 指令在 v0.23.0 中不存在（實測為「is not a hermes command」）；`--workspace-target` 選項也不存在。另外 OpenClaw 不是「Hermes 的前身」，而是另一個 Agent 專案。

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

v0.20.0 新增 `hermes import-agent`，可將既有 Claude Code 或 OpenAI Codex CLI 設定一鍵匯入。v0.23.0 起此指令由官方 `agent-importers` 外掛提供（另支援 Cursor、Grok Bot、OpenBot），核心的 `hermes migrate <agent>` 會在缺少外掛時自動安裝：

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
# 設定遷移：升級後執行（Docker 映像會在啟動時自動執行非互動式遷移）
hermes config check          # 顯示目前設定版本（例如 0 → 52）與缺少的環境變數
hermes config migrate        # 執行遷移；會先在 config.yaml 旁寫入備份
hermes doctor

# 如果有 config 結構變更，會自動建議修改
# 例如：
# ⚠️ Config migration needed:
#   - memory_mode → recall_mode (Honcho)
#   - reasoning_effort 統一到 config.yaml
```

> **注意事項**：大版本升級（如 v0.x → v1.x）前，務必先閱讀 Release Notes 的 Breaking Changes 區塊，並在測試環境驗證後再升級生產環境。

### 11.4 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 升級計畫涵蓋所有破壞性變更 | 對照 11.1.16 的 15 項 | 每一項都有處理方式與驗證結果 |
| 2 | 升級前有可還原的備份 | 在隔離環境 `hermes import <backup.zip>` | 成功還原；`hermes doctor` 通過 |
| 3 | 升級指令為官方支援的方式 | 審查升級腳本 | 沒有 `pip install --upgrade hermes-agent`、`git pull origin main`、ghcr 映像 |
| 4 | 升級後設定已遷移 | `hermes config check` | 設定版本為最新，沒有「update available」 |
| 5 | 外掛化的整合已就位 | `hermes plugins list`、`hermes memory status` | 記憶 Provider、Camofox、mcp-serve 等外掛已安裝且啟用 |
| 6 | 舊工具名稱已清除 | 在技能、提示、`toolsets` 中搜尋 `browser_navigate`、`hermes mcp serve`、`hermes sync` | 沒有結果 |
| 7 | MCP 用戶端已更新 | 用戶端設定中的啟動指令 | 為 `hermes mcp-serve` |
| 8 | 移轉指令正確 | 執行 `hermes migrate openclaw --dry-run` | 顯示預覽計畫；不是「is not a hermes command」 |

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
# ~/.hermes/config.yaml — AI Coding Agent（v0.23.0 鍵名）
model:
  provider: anthropic
  default: claude-sonnet-5-5

approvals:
  mode: smart
command_allowlist:
  - "mvn *"
  - "git status"
  - "git diff *"
  - "git log *"

toolsets: [coding]               # 組合型 Toolset：file + terminal + web + skills + browser + todo + memory …

mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
    trust: untrusted
```

```bash
# 建議搭配的內建技能（v0.23.0 皆為內建，無需安裝）
hermes skills list | grep -E 'github|test-driven-development|requesting-code-review|systematic-debugging'
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

結合 ComfyUI（optional skill）、Spotify（v0.22.0 起為 Catalog 外掛）、TouchDesigner-MCP（第三方 MCP 伺服器）與 v0.23.0 新增的 Meshy 3D 外掛，建立多媒體內容創作 Agent。

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

```bash
# v0.23.0 的安裝方式：ComfyUI 為 optional skill、Spotify 為 Catalog 外掛
hermes skills install official/creative/comfyui
hermes plugins install spotify && hermes plugins enable spotify
hermes plugins install meshy                # v0.23.0 新增：文字／圖片轉 3D（付費工具，請設定花費上限）
```

```yaml
# ~/.hermes/config.yaml — 多媒體創作 Agent
model:
  provider: anthropic
  default: claude-sonnet-5-5

toolsets: [hermes-cli]

mcp_servers:
  touchdesigner:                     # 第三方 TouchDesigner MCP 伺服器（自行審查來源）
    url: "http://127.0.0.1:9981/mcp"
    trust: untrusted
  renders:                           # 任何付費生成類 MCP 都應宣告成本與上限
    command: "render-mcp"
    tool_costs:
      create_image: 20
    spend_limit: 200
    cost_unit: credits
```

> ⚠️ **更正**：舊版範例把 ComfyUI、Spotify、TouchDesigner 寫成 `plugins.<name>.enabled`，並使用 `toolsets.enabled` 與 `model.model`；這些都不是 v0.23.0 的有效寫法。外掛的啟用清單是 `plugins.enabled: [...]`（或 `hermes plugins enable`），不是每個外掛一個子區塊。

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

### 12.5 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 案例設定可直接載入 | 將範例 `config.yaml` 放入測試 Profile 後執行 `hermes -p <test> doctor` | 沒有設定錯誤 |
| 2 | 技能與外掛已安裝 | `hermes skills list`、`hermes plugins list` | 案例使用的技能（例如 `comfyui`）與外掛（例如 `spotify`）都在清單中 |
| 3 | 排程任務以 CLI 建立 | `hermes cron list` | 案例中的每日／每小時工作都存在，且投遞目標正確 |
| 4 | 客服案例有升級（escalation）機制 | 以超出 FAQ 範圍的問題測試 | Agent 依技能中的 Escalation Rules 轉人工，而不是自行編造答案 |
| 5 | 付費工具有上限 | 檢查 `mcp_servers.*.spend_limit` | 所有生成類 MCP 都有 `tool_costs` 與 `spend_limit` |
| 6 | 案例數據有出處 | 檢查「實務案例」中的效益數字 | 標明為示意或附上可查證來源 |

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
hermes auth refresh nous           # 重新整理 OAuth Token
hermes auth add nous --type oauth  # 仍失敗時重新登入（等同 hermes portal）

# 錯誤：Model not found
/model                   # 查看可用模型清單

# 錯誤：402 Payment Required
# → 自動切換到 fallback provider
# → 或充值 API 額度

# 錯誤：Non-agentic model warning
# → 切換到支援 tool-use 的模型（以 /model 選擇器中有工具標記的模型為準）

# 診斷工具
hermes doctor
```

### Q5：Gateway 連線不穩定？

**排查步驟**：

```bash
# 1. 檢查 gateway 狀態
hermes gateway status

# 2. 查看 Gateway 日誌（最近 1 小時）
hermes logs gateway --since 1h

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
hermes logs errors

# 依等級或 Session 過濾；關鍵字請搭配 grep（沒有 --filter 旗標）
hermes logs --level WARNING
hermes logs --session <session_id>
hermes logs -n 500 | grep tool_call

# 日誌位置
~/.hermes/logs/agent.log     # INFO+ 級別
~/.hermes/logs/errors.log    # WARNING+ 級別
```

### Q11：如何在多個專案間切換？

```bash
# 方式 1：使用不同 Profile（先 hermes profile create project-a）
hermes -p project-a
hermes -p project-b

# 方式 2：在不同工作目錄啟動（會自動載入當前目錄的 AGENTS.md）
cd /path/to/project-a && hermes
cd /path/to/project-b && hermes

# 方式 3：使用 /new 重置對話但保留記憶
/new
```

### Q12：Autonomous Curator 會刪除重要技能嗎？（v0.12.0）

**Curator 的安全邊界**：

- Bundled Skills（內建技能）：預設不會被修剪（除非設定 `curator.prune_builtins: true`）
- Hub Skills（社群安裝的技能）：受保護，不會被修改
- Pinned Skills：`hermes curator pin` 標記的技能受保護
- **Locked Skills**（v0.23.0）：`hermes curator lock` 鎖定後，Agent 透過任何工具都不能改寫，即使在 YOLO 模式下
- Agent 自建技能：長期未使用者會先**歸檔**（`archive_after_days`，預設 30 天），可用 `hermes curator restore` 還原；每次變更前都有備份（`hermes curator rollback`）

```bash
# 保護重要技能
hermes curator pin my-important-skill
hermes curator lock my-important-skill     # v0.23.0：連內容都不允許 Agent 改寫

# 關閉 Curator
hermes config set curator.enabled false

# 檢查 Curator 最近的操作報告（每次執行一個時間戳目錄）
ls -t ~/.hermes/logs/curator/ | head -1
hermes curator rollback --list
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
# 在對話中，把耗時任務丟到獨立的背景 Session
/bg 對整個 src/ 目錄做安全掃描並整理報告

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
# ~/.hermes/config.yaml — v0.23.0 沒有 kanban.enabled 開關
kanban:
  dispatch_in_gateway: true     # 由 Gateway 內建調度器派工
  max_in_progress: 4            # 同時進行中的任務上限
  auto_decompose: true          # 允許自動拆解大型任務
```

```bash
hermes kanban init                       # 初始化預設看板
hermes kanban create "API 重構" --assignee team-backend --max-retries 3
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

### Q29：升級到 v0.23.0 後，原本的瀏覽器自動化技能失效了？（v0.23.0）

舊的 10 個 `browser_*` 工具（`browser_navigate`、`browser_click` 等）已全數移除，只剩 `browser_exec`：它以「執行預先匯入輔助函式的 Python」方式完成導航、點擊、輸入與截圖。請把技能、提示與 `toolsets` 清單中的舊工具名稱改掉；有使用 Camofox 的環境會自動安裝 `camofox` 外掛。

```bash
grep -rln 'browser_navigate\|browser_click\|browser_open' ~/.hermes/skills   # 找出需要改寫的技能
```

### Q30：Claude Desktop／IDE 把 Hermes 當成 MCP Server，升級後連不上？（v0.23.0）

`hermes mcp serve` 已改為 `hermes mcp-serve`（移到外掛），而且**不會自動改寫**用戶端設定。請先 `hermes plugins install mcp-serve`，再把 MCP 用戶端設定中的啟動指令改成 `hermes mcp-serve`。

### Q31：為什麼 `hermes -p coder gateway start` 被拒絕（exit 78）？（v0.22.0）

v0.22.0 起每台機器只有一個 Gateway 服務所有 Profile。請從預設 Profile 啟動 Gateway（`hermes gateway start`），它會同時服務 `coder`；舊的 per-profile 部署可以用 `hermes gateway migrate --multiplex` 合併。真的需要獨立 Gateway（例如不同 UNIX 使用者）時才使用 `--force`，或暫時設定 `gateway.standalone: true`（官方標示為過渡用，日後會移除）。

### Q32：升級後可以退回 v0.21.x 嗎？（v0.23.0）

不能直接退回。新版 Gateway 寫入 `state.db` 後，舊版本無法使用該資料庫；`hermes update` 會拒絕切回舊版，強行切換時正在執行的 Gateway 也會在約 30 秒內停止。要回退只能還原升級前的備份（`hermes import <backup.zip>`）或快照（`/snapshot restore <id>`），升級後產生的新對話不會包含在內。**升級前務必 `hermes update --backup`**。

### Q33：舊對話在 Webapp 中是唯讀的？（v0.23.0）

在 Gateway 接管 Session 之前建立的對話，需要先被「接管（adopt）」才能從瀏覽器繼續：在主機上執行一次 `hermes sessions adopt`（其他 Profile 用 `hermes -p <profile> sessions adopt`），或在原生 Desktop／TUI／CLI 中開啟一次該對話。

### Q34：舊 Session 會不會被自動刪除？（v0.22.0／v0.23.0）

v0.22.0 的 release notes 寫「`sessions.auto_prune` 預設開啟」，但 v0.23.0 實際上**預設關閉**；只有在 `config.yaml` 沒有這個鍵、且 `state.db` 所在磁碟空間不足時，才會詢問一次。可用 `/autoprune on|off|later` 回答，或直接在設定中寫明 `sessions.auto_prune` 與 `retention_days`。刪除的歷史會釋放 `state.db` 內部空間，要把空間還給磁碟請執行 `hermes sessions optimize`。

### Q35：外部記憶（Honcho／Mem0／Supermemory）升級後不見了？（v0.22.0）

這些 Provider 已移到 Plugin Catalog。`hermes update` 通常會自動安裝；若設定了 `security.allow_lazy_installs: false`、處於離線環境或拒絕了安裝，警告訊息中會附上確切的指令，例如 `hermes plugins install honcho`。安裝後以 `hermes memory status` 確認。

### Q36：Local Models 要怎麼在無 GPU 的伺服器上用？（v0.22.0）

`hermes model` → **Local models** 會依硬體挑選可執行的模型；沒有 GPU 時使用 CPU 引擎（`local_runtime.backend: cpu`），請選擇小型量化模型並預期較慢的速度。也可以自行啟動 `llama-server`，再以 `local_runtime.detect_ports` 或 `providers.llamacpp.base_url` 指向它。

### Q37：付費 MCP 工具在 Cron 中一直被拒絕？（v0.23.0）

宣告了 `spend_limit` 的 MCP 伺服器，若某次呼叫會讓累計花費超過上限，一定要有人核准；Cron 與 `hermes chat -q` 等無人可回答的情境會**直接拒絕**。請調整該伺服器的 `spend_limit`（每次 Cron 執行各自計算總額），或把該工作改為互動式執行。

### 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | FAQ 中的指令都能執行 | 以 `hermes <cmd> --help` 或附錄 E 的 `check_doc.py` 驗證 | 沒有 `auth login`、`logs --filter`、`skills pin`、`/background` 等不存在的用法 |
| 2 | 版本標註正確 | 對照第一章版本時間線 | 每題標註的版本與 release notes 一致 |
| 3 | 升級類問題與第十一章一致 | 對照 11.1.16 | 內容與處理方式一致 |

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
| macOS | 官網下載簽章 + 公證的 DMG（複製 `Hermes.app` 到「應用程式」） | **僅支援 Apple Silicon；v0.23.0 起需 macOS 13+**（Electron 44） |
| Windows | 官網下載 `.appinstaller`（以 App Installer 安裝簽章 MSIX），或 Microsoft Store | Windows 11 22H2+、64 位元（x64／ARM64）；**NSIS／MSI 自 v0.22.0 起停用** |
| Linux | 官方發行流程**未提供** Linux 桌面套件；以 `install.sh` 安裝 CLI 後執行 `hermes desktop` 自行建置 | 支援 X11／Wayland；Local Models 在 Linux Desktop 上預設開啟 |
| 已安裝 CLI 者 | `hermes desktop` 或 `hermes gui` | 免另外下載，直接由既有 CLI 安裝喚出桌面應用 |

> ⚠️ Homebrew 安裝（`brew install --cask hermes-desktop`）已隨 v0.20.0 一併停用，見 4.2.3 節。v0.22.0 起 Desktop 是**自帶 Python 與 Node.js 的封閉簽章套件**，首次啟動不需要建置任何東西，並會自行更新；`Hermes-Setup` 引導安裝程式則不同，它會下載原始碼並建置 Desktop。

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
| 非技術用戶（PM/QA） | 僅安裝 Desktop App，連至團隊 Gateway；可開啟 v0.22.0 的 **Simple** 模式，介面簡化為單純的聊天 |
| 遠端工作 | Desktop App + VPN／Tailscale 或 OAuth 認證；無法安裝 App 的裝置可改用 Webapp（14.6） |
| CI/CD 整合 | 伺服器端使用 CLI，開發者使用 Desktop App |
| 需要遠端終端機存取但不信任裝置本機環境 | v0.20.0 SSH 遠端後端，Agent 實際執行於受控伺服器 |

> **企業建議**：Desktop App 適合作為團隊的統一入口點，搭配集中式 Gateway 可確保所有對話紀錄、技能和記憶由組織統一管理，同時降低個人裝置的設定負擔。若考慮採用 Hermes Cloud 作為代管後端，須留意其目前仍為 **Preview 階段、無正式 SLA**（見 9.7.5 節），正式生產環境建議優先採用自架 Gateway。

### 14.6 Webapp（v0.23.0）

Webapp 是由 Gateway 直接提供給一般瀏覽器使用的 **Desktop 工作區**（Session、Profile、Capabilities、Messaging、Artifacts、排程、主機檔案樹、Git 檢視、預覽與終端機）。它**不是** Web Dashboard，而且**預設關閉**。

```bash
hermes config set webapp.enabled true
hermes gateway restart
hermes webapp                # 必要時建置前端、啟動 Gateway，並開啟一次性登入連結
hermes -p work webapp        # 開啟指定 Profile
hermes webapp --status       # 是否正在提供服務；不能提供時說明原因
hermes webapp --sign-out     # 登出所有瀏覽器分頁
```

```yaml
# ~/.hermes/config.yaml — 預設值
webapp:
  enabled: false
  host: 127.0.0.1         # 改為 0.0.0.0 時，Gateway 會強制要求 Dashboard 登入閘門
  port: 9120
  public_url: ""          # 位於同機反向代理或 tunnel 之後時，填入對外的 HTTPS 位址
```

**登入機制**：`hermes webapp` 產生的連結只能使用一次，而且必須在 60 秒內開啟。登入狀態保存在該分頁中，重新整理頁面或 Gateway 重啟都不會登出；但新分頁或直接輸入網址會看到登入說明，需要重新執行 `hermes webapp` 取得連結。

**限制與規格**：

| 項目 | 規格 |
| --- | --- |
| 上傳檔案 | 每個檔案 16 MiB |
| 終端機 | 中斷連線的 Shell 保留 15 分鐘；每台主機最多 16 個終端機；重連時回放最多 1 MiB 輸出 |
| 非 HTTPS 的遠端位址 | 瀏覽器會停用 Bot Screen 檢視、麥克風（聽寫、即時語音、遠端喚醒詞）、剪貼簿讀取與系統通知 |
| 僅限原生 App 的功能 | 全域快捷鍵、置頂浮動視窗、OS 視窗檢視、外部終端機、更新程式 |

> ⚠️ **資安等級**：登入 Webapp 的使用者可以**用執行 Hermes 的 OS 帳號執行任意指令**、使用 Agent 工具、存取主機檔案與 Git，並取得該帳號的環境變數與憑證。**沒有登入提供者時不要對外開放**；優先使用 SSH tunnel、Tailscale 或企業 VPN；遠端存取必須使用 HTTPS（`webapp.public_url`）。

> ✅ **如何驗證**：在另一台機器上以 `curl -s -o /dev/null -w '%{http_code}' http://<host>:9120/` 測試。`webapp.host` 為 `127.0.0.1` 時應無法連線；改為 `0.0.0.0` 後，未登入的請求只能看到登入頁，不能取得工作區資料。

### 14.7 多 Gateway 連線與 Bot Screen（v0.22.0／v0.23.0）

- **同時連線多台機器**（v0.23.0）：Desktop 會讓所有 Gateway（本機、SSH、遠端）保持連線，切換即時；終端機分頁在開啟它的主機上執行；Group Chat 可以混用不同機器上的 bot。遠端 Gateway 在 **Settings → Gateways** 中新增。
- **Bot Screen**（v0.22.0）：在 Linux Gateway 上執行的 bot 可以擁有自己的桌面，由 Desktop 即時串流。遇到登入、2FA 或 CAPTCHA 時，使用者可以接手畫面、完成步驟後再交還控制權。使用 Docker、SSH 或 Singularity 後端時，bot 的畫面與 computer-use 都在該後端內執行。
- **介面模式**（v0.22.0）：新增 **Simple** 模式，把 App 變成單純的聊天介面，適合非技術使用者。

### 14.8 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | 安裝套件為官方簽章套件 | macOS：`codesign -dv /Applications/Hermes.app`；Windows：`Get-AppxPackage *Hermes*` | 簽章有效；Windows 為 MSIX 套件 |
| 2 | 作業系統符合需求 | 檢查 OS 版本 | macOS 13+（Apple Silicon）、Windows 11 22H2+ 64 位元 |
| 3 | Desktop 連到正確的 Gateway | Settings → Gateways | 只連到核准的 Gateway；遠端連線使用 OAuth 或密碼認證 |
| 4 | Webapp 狀態符合政策 | `hermes webapp --status`；`hermes config get webapp.host` | 預設關閉；若開啟，`host` 為 loopback 或已有登入閘門與 HTTPS |
| 5 | 移除時資料處理正確 | `hermes uninstall --dry-run` | 預覽清單符合預期（`--full` 才會刪除資料目錄） |

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

#### 15.3.1 v0.23.0：Group Chats 自主運作

v0.23.0 讓 Gateway 擁有的群組房間可以在無人介入下運作，並補上防失控機制：

| 能力 | 說明 | 企業意涵 |
| --- | --- | --- |
| **誰回答沒有點名的訊息** | Room settings 可選 **Everyone**（預設）、**Lead**（由指定的 lead bot 轉交）或 **Pick who answers automatically**（以一次不帶工具的模型呼叫，依房間目的、筆記與成員角色挑選） | 以 Lead 或自動路由減少「每個 bot 都回答」的 Token 浪費 |
| **房間目的與共享筆記** | 房間可保存 purpose 與 notes，作為自動路由與成員回覆的依據 | 把房間的職責寫清楚，等於替群組寫 SOP |
| **Cron 可以發文到房間** | 排程工作的結果可直接送進房間，由成員接手處理 | 例行巡檢 → 房間 → 對應 bot 處理 |
| **防止無止境互相觸發** | bot 回覆「發訊息給它的 bot」時自動變成 notify-only；`gateway.bot_loop_guard.max_hops`（預設 4）限制每次交換的 bot 對 bot 訊息數 | 防止兩個 bot 互相觸發而燒掉預算 |
| **硬上限與暫停** | 每次送出最多 10 則訊息、3 輪；達上限時房間顯示「Paused after N messages」，可按 **Continue**（同一討論最多 5 次） | 失控時自動暫停，而不是持續花費 |
| **即時狀態** | 每個 bot 顯示目前正在做什麼（例如「scout · terminal · 7s」）；外掛可透過 `on_room_member_activity` hook 觀察 | 可接入監控與稽核 |
| **跨機器房間** | 新建 Group Chat 時可選擇不同連線上的 bot；全部在同一連線上的房間由該 Gateway 擁有，關閉 Desktop 也會繼續運作 | 跨團隊協作不必集中到同一台主機 |

```yaml
# ~/.hermes/config.yaml — bot 對 bot 迴圈防護（預設值）
gateway:
  bot_loop_guard:
    enabled: true
    max_events: 20
    window_seconds: 300
    cooldown_seconds: 600
    max_hops: 4                       # 每次交換最多幾則 bot 對 bot 訊息
    bot_replies_expect_reply: false   # true = bot 回覆 bot 的訊息可以再被回覆（不建議）
```

### 15.4 `hermes peer` — 跨 Gateway Agent 直訊

當協作對象不在同一台機器上時，`hermes peer` 提供 **Hermes 對 Hermes 的第一方通道**，且**不需要 Desktop 介入**。

```bash
# 註冊對端 Gateway（需對方的 API_SERVER_KEY）
hermes peer add research-box \
  --url https://gw.research.internal:8080 \
  --key "$RESEARCH_API_SERVER_KEY"

# 送出一則訊息（支援標準輸入）
hermes peer dm research-box < findings.md

# 交付長時間任務（回傳 run_id），之後以 run_id 輪詢狀態
hermes peer run research-box "彙整本週 CVE 影響評估" --json
hermes peer status research-box <run_id>
hermes peer stop research-box <run_id>      # 必要時中止
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

### 15.8 本章審查與驗證清單

| # | 檢查項目 | 驗證方式 | 預期結果 |
| --- | --- | --- | --- |
| 1 | Bot Mode 狀態符合治理決策 | Desktop：Capabilities → Plugins → Bots | 已依政策開啟或關閉 |
| 2 | 迴圈防護未被關閉 | `hermes config get gateway.bot_loop_guard.enabled`、`max_hops` | `true`；`max_hops` 未調高 |
| 3 | peer 只連到核准的 Gateway | `hermes peer list` | 只有核准的對端；URL 為 HTTPS 內部位址 |
| 4 | peer 金鑰夠強且未外洩 | 檢查 `API_SERVER_KEY` 長度與存放位置 | 32 字元以上隨機字串；只存在 `.env`（`0600`）或秘密管理系統 |
| 5 | 群組房間有明確目的 | 檢查 Room settings 的 purpose／notes | 每個房間都寫明職責與成員角色 |
| 6 | peer 任務可追蹤 | `hermes peer status <target> <run_id> --json` | 可查到任務狀態；對話紀錄落在雙方的 Bot Chat 中 |

---

## 附錄 A：檢查清單（Checklist）

### A.1 安裝檢查清單

- [ ] 確認作業系統落在 [Tier 1／Tier 2 支援層級](#411-平台支援層級platform-support-tiers)內（**macOS Intel 不支援**）
- [ ] 確認執行環境為 **Python 3.14**（由 PM 提供；`hermes doctor` 會顯示），不要自行以 3.11–3.13 執行
- [ ] 確認 Node.js、ripgrep、FFmpeg、Chromium 由 PM 安裝（v0.22.0 起不採用系統 Node.js；glibc Linux 需有 `libatomic1`）
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

- [ ] `approvals.mode` 設定為 `smart` 或 `manual`（`off` 僅限可拋棄環境）；`approvals.cron_mode`／`unattended_mode` 為 `deny`
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
- [ ] 以 `hermes backup`（或 `hermes update --backup`）建立完整備份，並加密保存（備份含憑證）
- [ ] 執行 `hermes update`
- [ ] 執行 `hermes doctor` 驗證
- [ ] 確認所有 Skills 正常載入
- [ ] 確認 Gateway 連線正常
- [ ] 確認 Memory Provider 正常
- [ ] 更新 Docker 映像版本（`nousresearch/hermes-agent:X.Y.Z`）；容器內不執行 `hermes update`
- [ ] 逐項完成 [11.1.16](#11116-v0210--v0230-升級特別注意事項目前最新版本) 的破壞性變更清單
- [ ] 確認升級後**不可回退**的影響已被接受（新版 Gateway 寫入 `state.db` 後只能以備份還原）

### A.7 v0.22／v0.23 新增檢查項目

- [ ] 每台主機只有一個 Gateway；K8s 為 `replicas: 1` + `Recreate`，PVC 為 RWO（見 2.5、10.2 節）
- [ ] `state.db` 位於本機檔案系統；位於 NFS／SMB 時 `database.journal_mode: delete`
- [ ] 第三方外掛已設定 `plugins.isolation: host`；外掛自動更新符合變更管理政策
- [ ] 記憶 Provider 等已外掛化的整合已安裝並啟用（`hermes plugins list`、`hermes memory status`）
- [ ] 技能、提示與 toolset 清單中沒有 `browser_*` 舊工具與 `hermes mcp serve`、`hermes sync`
- [ ] Webapp 預設關閉；若開啟，已啟用登入閘門與 HTTPS（見 14.6 節）
- [ ] Connectors 的使用已依資料分級核准，不需要時已關閉
- [ ] 付費 MCP 工具都有 `tool_costs` 與 `spend_limit`
- [ ] `sessions.auto_prune`／`retention_days` 已依保存政策明確設定
- [ ] 已執行 9.9.1 的弱點情資查詢與 `hermes security audit --fail-on high`
- [ ] 手冊範例與內部設定已用附錄 E.3 的檢查工具驗證

---

## 附錄 B：指令速查表

> 本附錄依 v0.23.0 的**實際 argparse 指令樹**（共 507 條指令路徑，以 `hermes_cli.main._build_cli_parser()` 匯出）與官方 `/docs/reference/cli-commands` 重整，依功能分類。表中每個子指令與旗標都經過白名單比對；篇幅所限僅列最常用旗標，完整旗標請執行 `hermes <指令> --help`。標示「外掛」者需先安裝對應外掛。

### B.1 CLI 指令（依功能分類）

**全域旗標**：`hermes [-p/--profile <name>] [-m/--model <m>] [--provider <p>] [--reasoning <level>] [-r/--resume <session>] [-c/--continue] [-w/--worktree] [--yolo] [--tui|--cli|--native] [--safe-mode] <指令>`；單次模式為 `hermes [--model <m>] -z "<prompt>"`（`-z` 必須放在 `--model` 之後）

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
| 開發整合 | `hermes mcp catalog\|install\|add\|remove\|list\|test\|login\|reauth` | MCP 伺服器管理 |
| 開發整合 | `hermes mcp-serve`（外掛 `mcp-serve`） | 以 Hermes 作為 MCP Server（v0.23.0 由 `hermes mcp serve` 更名） |
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
| 遷移 | `hermes migrate openclaw\|claude-code\|codex\|cursor\|grok-bot\|openbot [--dry-run] [--overwrite] [--yes]` | 從其他 Agent 匯入（缺 `agent-importers` 外掛時自動安裝；見 11.3 節） |
| 遷移 | `hermes import-agent <agent> [--dry-run]`（外掛 `agent-importers`） | 同上，外掛提供的完整選項（例如 `--preset full --migrate-secrets`） |
| 記憶 | `hermes memory setup\|status\|off` | 外部記憶 Provider 設定 |
| 記憶 | `hermes journey` / `hermes learning` / `hermes memory-graph` | 學習時間軸／記憶圖檢視 |
| 審批 | `hermes approvals` / `hermes approvals suggest` | 危險指令審批策略管理（`suggest` 為 v0.20.0 新增，依歷史提出白名單建議） |
| 審批 | `hermes pairing list\|approve\|revoke\|clear-pending` | DM Pairing 配對管理 |
| 系統 | `hermes egress install\|setup\|start\|stop\|status` | 出站憑證注入代理 iron-proxy（見 9.8 節）；`setup --rotate-tokens` 輪替代理權杖 |
| **多 Agent** | **`hermes peer add\|list\|dm\|run\|status\|stop\|remove`** | **跨 Gateway Agent 直訊（v0.21.0，見 15.4 節；`status`／`stop` 需帶 `<target> <run_id>`）** |
| **v0.22／v0.23** | `hermes webapp [--status] [--sign-out] [--no-open]` | 在瀏覽器開啟 Desktop 工作區（v0.23.0，預設關閉，見 14.6 節） |
| **v0.22／v0.23** | `hermes connectors list\|connect\|accounts\|rename\|disconnect` | 管理 Connectors 帳號（v0.22.0；`rename <app> <name> --to <新名稱>`） |
| **v0.22／v0.23** | `hermes vault add\|list\|rm\|sources\|key` | 瀏覽器憑證庫；`hermes vault key migrate --to keychain` 把金鑰移到 OS keychain（v0.23.0） |
| **v0.22／v0.23** | `hermes plugins update\|auto-update\|check-updates\|validate\|capabilities\|pack` | 外掛更新、自動更新（v0.23.0）、驗證與 Plugin Pack |
| **v0.22／v0.23** | `hermes curator lock\|unlock\|rollback\|usage` | 鎖定技能（v0.23.0）、回復、使用統計 |
| **v0.22／v0.23** | `hermes cron cancel\|runs\|notepad\|doctor\|incidents` | 停止執行中的工作（v0.23.0）與執行紀錄 |
| **v0.22／v0.23** | `hermes sessions adopt\|discard\|pin\|unpin\|optimize-storage` | 讓 Gateway 接管舊對話、確認中斷的輸入（v0.23.0） |
| **v0.22／v0.23** | `hermes gateway migrate [--multiplex]` | 把 per-profile Gateway 合併為單一 Gateway（v0.22.0） |
| **v0.22／v0.23** | `hermes pm install chromium\|cua-driver` | PM 補裝受管工具（v0.22.0；`pm` 在 argparse 之前分派） |
| **v0.22／v0.23** | `hermes pause [--reason <文字>]` / `hermes resume` | 全域緊急停止：暫停所有排程觸發 |
| 審批 | `hermes approvals test "<指令>" [--json]` | 以 dry-run 測試審批規則的判決結果，不實際執行指令（v0.21.0 時名為 `approval-check`） |
| 憑證 | `hermes secrets` | 外部秘密來源管理（Bitwarden／1Password `op://`／Command Helper，v0.19.0 起可插拔） |
| 模型 | `hermes migrate <provider>` | 針對已退役模型自動改寫設定（如 `hermes migrate xai`） |
| 設定 | `hermes portal` | Nous Portal OAuth 認證與 Tool Gateway 狀態（`hermes setup --portal` 為一鍵快速設定） |
| 診斷 | `hermes prompt-size` | 顯示 System Prompt 各組成的位元組佔比，用於排查 context 膨脹 |
| 診斷 | `hermes dump` | 產出可複製貼上的設定摘要，供技術支援使用 |
| 診斷 | `hermes debug` | 上傳已遮蔽的日誌與系統資訊並取得分享連結 |
| 介面 | `hermes desktop --setup-tcc-identity` | macOS 專用：以穩定簽章身分固定 TCC 權限，使授權跨更新存續（v0.21.0） |
| 介面 | `hermes pets` | 瀏覽與管理 Petdex 終端寵物（趣味功能） |
| 訊息平台 | `hermes photon setup\|status\|install-sidecar`（內建平台外掛） | Photon Spectrum iMessage 設定（v0.17.0，免 Mac relay） |
| 介面 | `hermes dashboard [--port 9119] [--stop] [--status]` | Web Dashboard 管理 |
| 介面 | `hermes gui` / `hermes desktop` | 啟動 Desktop App |
| 介面 | `hermes serve [--host] [--port]` | 啟動供 Desktop／遠端連線的 Agent 伺服器 |
| Profile | `hermes profile list\|use\|create\|delete\|show\|rename\|export\|import\|install\|update` | Profile 完整管理 |
| 維護 | `hermes --version` / `hermes update [--check] [--plan] [--backup] [--set-channel stable\|main]` | 版本檢視與升級（v0.21.7 起預設只追穩定 Release） |
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
| `/platforms` | 查看連線平台狀態 |
| `/status` | 查看 Agent 狀態 |
| `/busy [steer\|queue\|interrupt\|status]` | Agent 忙碌時新訊息的處理方式（v0.12.0） |
| `/btw` | 中插任務導引（v0.12.0） |
| `/reload` | 熱重載 `.env`（v0.12.0） |
| `/reload-skills` | 重新載入技能庫（v0.12.0） |
| `/reload-mcp` | 重建 MCP cached agents（v0.12.0） |
| `/fast` | 切換 Fast Mode |
| `/steer` | 中途導引 Agent 行為（v0.11.0） |
| `/goal` / `/goal draft\|show\|pause\|resume\|clear` / `/subgoal` | 持久化目標管理（Ralph Loop）（v0.13.0，v0.18.0 起支援完成契約） |
| `/kanban` | 顯示 Multi-agent Kanban 看板（v0.13.0） |
| `/queue`（`/q`） `[<prompt>\|list\|edit N <prompt>\|rm N\|move A B\|clear]` | 排入下一回合的提示；v0.22.0 起可編輯（v0.13.0） |
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
| `/rewind` | 回溯到較早的提示：編輯重送，或按 `f` 分岔新 Session（v0.23.0；TUI 空白輸入框按兩次 `Esc`） |
| `/autoprune [on\|off\|later]` | 自動清理舊 Session 的開關（v0.23.0 預設關閉） |
| `/delegation [default\|model_map\|profile_routes]`（外掛 `advanced-delegation`） | 切換委派策略（v0.23.0） |
| `/connectors`（TUI） | 管理 Connectors 帳號（v0.22.0） |
| `/stop` | 停止目前回合；v0.22.0 起也會停止背景子代理並取回部分成果 |
| `/help` / `/commands` / `/quit`（`/exit`） | 說明、列出所有指令與離開 |

> ✅ **如何驗證本附錄**：`python -X utf8 check_synopsis.py <手冊.md> cli.json`（附錄 E.3）會把每個 `a\|b\|c` 多選展開，逐一比對 v0.23.0 的指令白名單；斜線指令則以 `COMMAND_REGISTRY`（105 個）加上內建／optional 技能名稱比對。

---

## 附錄 C：環境變數參考

### C.1 模型 Provider 金鑰

| 環境變數 | 說明 | 必要性 |
| ---------- | ------ | -------- |
| `ANTHROPIC_API_KEY` | Anthropic API 金鑰（或改用 `hermes auth add anthropic` 以 OAuth 登入，Claude Max 訂閱可用） | 至少一個 Provider |
| `OPENAI_API_KEY` | OpenAI API 金鑰 | 至少一個 Provider |
| `OPENROUTER_API_KEY` | OpenRouter API 金鑰 | 至少一個 Provider |
| `GOOGLE_API_KEY` / `GEMINI_API_KEY` | Google AI Studio（Gemini）API 金鑰 | 選用 |
| `XAI_API_KEY` | xAI (Grok) API 金鑰（或 `hermes auth add xai` 以 OAuth 登入，需 SuperGrok／X Premium+） | 選用 |
| `NVIDIA_API_KEY` | NVIDIA NIM（build.nvidia.com）API 金鑰 | 選用 |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | AWS Bedrock 認證（AWS SDK 標準變數，亦可用 IAM Role／`AWS_PROFILE`） | 選用 |
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
| `LM_BASE_URL` / `LM_API_KEY` | LM Studio 本地端點 | 選用 |
| `AZURE_FOUNDRY_API_KEY` / `AZURE_FOUNDRY_BASE_URL` | Azure AI Foundry（亦支援 Microsoft Entra ID auth，v0.15.0） | 選用 |
| `TOKENHUB_API_KEY` / `TOKENHUB_BASE_URL` | 騰訊 Tokenhub API 金鑰與端點 | 選用 |
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
| `GOOGLE_CHAT_PROJECT_ID` / `GOOGLE_CHAT_SUBSCRIPTION_NAME` / `GOOGLE_CHAT_SERVICE_ACCOUNT_JSON` | Google Chat（Pub/Sub 訂閱 + Service Account；另有 `GOOGLE_CHAT_ALLOWED_USERS`） | Gateway 需要 |
| `LINE_CHANNEL_ACCESS_TOKEN` | LINE Messaging API Token | Gateway 需要 |
| `SIMPLEX_WS_URL` / `SIMPLEX_ALLOWED_USERS` | SimpleX Chat CLI 的 WebSocket 位址與允許清單 | Gateway 需要 |
| `NTFY_TOPIC` | ntfy 推播主題 URL | Gateway 需要 |
| **`BUZZ_RELAY_URL`** | **Buzz（Nostr）中繼站設定（v0.20.0 新增，實際變數名稱以官方文件為準）** | Gateway 需要 |

### C.3 工具與整合

| 環境變數 | 說明 | 必要性 |
| ---------- | ------ | -------- |
| `GITHUB_TOKEN` | GitHub Token（MCP／各類 Git 整合用） | MCP 需要 |
| （自訂名稱，例如 `DATABASE_URL`） | MCP 伺服器所需的憑證：名稱由你自己決定，再在 `mcp_servers.<name>.env` 中以 `${VAR}` 引用；不是 Hermes 本身讀取的變數 | 依 MCP 伺服器 |
| `ELEVENLABS_API_KEY` | ElevenLabs TTS API 金鑰 | Voice 需要 |
| `MEM0_API_KEY` | Mem0 Cloud API 金鑰 | Mem0 記憶需要 |
| `SPOTIFY_CLIENT_ID` | Spotify PKCE OAuth（v0.22.0 起由 Catalog 外掛 `spotify` 讀取） | Spotify 需要 |
| `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | Langfuse 可觀測性（v0.22.0 起為 Catalog 外掛 `langfuse`） | 選用 |
| **`BWS_ACCESS_TOKEN`** | **Bitwarden Secrets Manager Machine Account Token（v0.15.0，v0.19.0 起與 1Password 並列可插拔 `SecretSource`）** | 選用 |
| **`OP_SERVICE_ACCOUNT_TOKEN`** | **1Password Service Account Token（`op://` 參照解析用，v0.19.0 新增）** | 選用 |
| **（自訂名稱，例如 `HERMES_OUTBOUND_WEBHOOK_SECRET`）** | **Outbound Webhook HMAC 簽章密鑰：變數名稱由 `hooks.outbound[].secret_env` 指定（v0.20.0，見 1.4.31 節）** | Webhook 需要 |

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

> ✅ **如何驗證本附錄**：表中每個變數名稱都已比對 v0.23.0 官方 Environment Variables 參考（683 個）與原始碼中的 `HERMES_*` 常數（261 個）；不在兩者之中的只有 AWS SDK 標準變數與標示「自訂名稱」的範例。舊版本附錄中的 `GOOGLE_AI_API_KEY`、`LM_STUDIO_URL`、`AZURE_AI_FOUNDRY_KEY`、`TENCENT_TOKENHUB_KEY`、`GOOGLE_CHAT_WEBHOOK`、`SIMPLEX_CHAT_PORT`、`GOOGLE_MEET_CREDENTIALS` 都不存在，已更正或移除。

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

#### D.1.2 v0.22.0／v0.23.0 新增模型

| 模型 | 所屬 | 備註 |
| ------ | ------ | ------ |
| Claude Fable 5.1、Opus 5.5（`claude-opus-5-5`）、Sonnet 5.5、Haiku 5.5 | Anthropic | v0.22.0「Claude 5.5 模型波」；可經 Nous Portal、OpenRouter（如 `anthropic/claude-sonnet-5.5`）或原生 Provider 使用 |
| GPT-6 Astra／Sol／Luna、GPT-6.1 Sol | OpenAI | v0.22.0；Codex 路徑另有 `gpt-6-astra-900k` 等變體 |
| Gemini 4 Argon（`gemini-4-argon`） | Google | v0.22.0；可經 Vertex 或 OpenRouter |
| Nemotron 3.5（Super 預設參數）、Nemotron 3 Ultra 免費層（`nvidia/nemotron-3-ultra:free`） | NVIDIA | v0.22.2；免費層經 Nous Portal |

> 💡 v0.22.0 起，凡 Provider 能讀取的先前推理內容（reasoning）會在 resume、分支與壓縮後**預設重播**；模型選擇器可加星號、顯示訂閱剩餘額度與限流解除時間，並可在選模型時一併指定推理強度（`/model <id> --reasoning high`）。實際可用的模型 ID 以 `/model` 選擇器或 `hermes model` 的清單為準。

#### D.1.3 `model_overrides` — 免改版覆寫與可插拔 Provider（v0.21.0）

上游調整了 context window 或能力、而 Hermes 目錄尚未跟上時，不必等待官方發版（**只能覆寫能力宣告，不能覆寫價格**）：

```yaml
# ~/.hermes/config.yaml — 結構為 model_overrides.<provider>.<model id>
model_overrides:
  openrouter:
    some-vendor/new-model:
      context_window: 400000
      supports_vision: true
      supports_tools: true
      supports_reasoning: true
  bedrock:
    _default:
      context_window: 200000      # 此 Provider 下未列出模型的預設值
```

> ⚠️ **更正與 checker 盲點**：舊版範例的扁平鍵 `"openrouter/some-vendor/new-model"` 與 `input_price_per_1m`／`output_price_per_1m` 都不在原始碼（`agent/models_dev.py`）讀取的欄位中。官方驗證器對 `model_overrides` 底下的鍵**不做深層檢查**，所以 `hermes config set` 不會警告，必須以本表的欄位人工審查。

同時 v0.21.0 起，**以 pip 安裝的第三方模型 Provider 可透過 Python entry points 被自動探索**，無須修改 Hermes 本體。另有兩項與模型目錄相關的校正值得注意：Codex GPT 的 context 預設值已核實為 **272K**（並提供明確的 `-900k` 變體），以及**資料訓練層級（data-training-tier）警示已於所有模型選擇器介面統一顯示**——這對有資料落地要求的企業是實用的選型輔助。

> ⚠️ **變更管控**：`model_overrides` 直接影響成本估算與 context 管理決策，屬「繞過官方目錄」的機制，應納入設定檔版本控管與審核流程。

### D.2 自架／本地推理後端

| 後端 | 端點慣例 | 特點 |
| ------ | ------ | ------ |
| Ollama | `localhost:11434/v1` | 最普及的本地模型執行環境 |
| vLLM | `:8000/v1` | 高輸送量推論伺服器 |
| SGLang | `:30000/v1` | RadixAttention KV-cache 重用 |
| llama.cpp / llama-server | `:8080/v1` | 極輕量、CPU 可執行 |
| **Hermes 受管 Local Models**（v0.22.0） | 自動（`model.provider: llamacpp`） | Hermes 自動安裝並維護 llama.cpp 引擎、依硬體挑選模型；`local_runtime.backend: auto\|cuda\|metal\|vulkan\|hip\|cpu`（見 1.4.44） |
| LiteLLM Proxy | `:4000/v1` | 統一代理 100+ Provider |
| **ClawRouter** | `:8402/v1` | 以 **USDC 加密貨幣**付費，依查詢複雜度自動選模型 |

### D.3 第三方 OpenAI 相容端點（經官方文件證實可用）

Together AI、Groq、Cerebras、Mistral AI、LocalAI、Jan、Perplexity——均可透過 `custom` Provider ID 或各自專屬設定連接。

> **架構說明**：v0.12.0 將所有 Provider 重構為 Pluggable 架構，v0.13.0 引入 `ProviderProfile` ABC 介面，v0.15.0 一度移除 Vercel AI Gateway 與 Vercel Sandbox（v0.20.0 現代化重新引入）。第三方可自行開發 Provider Plugin 並掛載至 Hermes，無需修改核心程式碼。

---

## 附錄 E：驗證紀錄（v9.0.0）

本附錄記錄本版手冊**如何**被驗證：用了哪些權威來源、執行了哪些檢查、原稿發現了什麼、修正後的結果，以及還無法確認的事項。目的是讓審查者可以**重複執行同樣的檢查**，而不必相信本文的說法。

### E.1 版本基準與權威來源

| 項目 | 值 | 取得方式 |
| --- | --- | --- |
| 基準版本 | **v0.23.0 The Hearth**（2026-11-05） | `gh api repos/NousResearch/hermes-agent/releases/latest` |
| 涵蓋範圍 | v0.21.1–v0.21.7、v0.22.0–v0.22.7、v0.23.0（共 18 份 release notes） | `gh api repos/NousResearch/hermes-agent/releases/tags/<tag>` |
| 原始碼 | v0.23.0 tag 的 tarball（約 90 MB） | `gh api repos/NousResearch/hermes-agent/tarball/v0.23.0` |
| 官方文件 | 同一 tag 的 `website/docs/`（435 頁） | 與原始碼同一版本，避免線上文件已更新到 `main` 的落差 |
| 執行環境 | Python 3.14.10、uv 0.13.7、Windows 11 | `uv python install 3.14`（隔離的 venv，不影響使用者的 `~/.hermes`） |
| 倉庫數據 | Stars 261,617、Forks 58,096、Releases 47 | `gh api repos/NousResearch/hermes-agent`（2026-11-08） |
| 公開弱點 | 10 筆 GHSA（全域資料庫）；官方倉庫 0 筆 | `gh api "advisories?ecosystem=pip&affects=hermes-agent"` |
| Plugin Catalog | 1,051 個 YAML（含 `removed.yaml`）；Community 1,018、Official 21、Verified 9 | 計數 `plugin-catalog/*.yaml` 的 `tier:` |
| 內建／optional 技能 | 44／142 | 計數 `skills/**/SKILL.md`、`optional-skills/**/SKILL.md` |

**白名單（由實際安裝的 v0.23.0 匯出）**：

| 白名單 | 數量 | 來源 |
| --- | --- | --- |
| CLI 指令路徑（含每條路徑的旗標與帶值旗標） | 507 | `hermes_cli.main._build_cli_parser()` 遞迴走訪 argparse 樹 |
| 斜線指令（含別名） | 105 | `hermes_cli.commands.COMMAND_REGISTRY`；另加 TUI 專用的 `/connectors`、`/switch` 與外掛提供的 `/delegation` |
| 設定鍵 | 1,133 條路徑（102 個頂層鍵） | `hermes_cli.config_defaults.DEFAULT_CONFIG`；**實際判斷呼叫 `hermes_cli.config._validate_config_key`**（與 `hermes config set` 相同） |
| 環境變數 | 683（官方參考）＋ 261（原始碼中的 `HERMES_*` 常數） | `reference/environment-variables.md` 表格 |
| 外掛 CLI 指令 | `meet`、`photon`、`teams-pipeline`（內建外掛）、`pm`（argparse 之前分派）、`mcp-serve`、`import-agent`（Catalog） | `ctx.register_cli_command` 搜尋 |

### E.2 原稿更正清單

下表依類別列出代表性更正（完整逐行清單由 E.3 的工具重新產生）。「來源」欄的 [CLI] 表示真實 argparse 實測，[CFG] 表示官方設定鍵驗證器，[D] 表示 v0.23.0 tag 的官方文件，[S] 表示原始碼，[R] 表示 release notes。

| # | 類別 | 原稿寫法 | v0.23.0 正確寫法 | 來源 | 章節 |
| --- | --- | --- | --- | --- | --- |
| 1 | CLI | ❌ `hermes -z --model X "提示"` | `hermes --model X -z "提示"`（`-z` 會吃掉下一個參數） | [CLI] exit 2 | 5.1.1 |
| 2 | CLI | ❌ `hermes "列出…"`（裸提示） | `hermes -z "…"` 或 `hermes chat -q "…"` | [CLI] exit 2 | 5.1.1 |
| 3 | CLI | ❌ `hermes auth login nous` | `hermes auth add nous --type oauth`／`hermes portal`／`hermes auth refresh` | [CLI] | 4.6.3、13 |
| 4 | CLI | ❌ `hermes claw migrate [--workspace-target]` | `hermes migrate openclaw`／`hermes import-agent openclaw` | [CLI][D] | 11.3.1 |
| 5 | CLI | ❌ `hermes approval-check` | `hermes approvals test "<指令>"` | [CLI] | 1.4.40、B |
| 6 | CLI | ❌ `hermes logs --errors`／`--filter` | `hermes logs errors`、`--level`、`--session`、`--since`；關鍵字用 `grep` | [CLI] | 9.4、13 |
| 7 | CLI | ❌ `hermes doctor --quick`（健康檢查） | `GET /health`（API Server） | [CLI][D] | 9、10 |
| 8 | CLI | ❌ `hermes skills pin` | `hermes curator pin`／`hermes curator lock` | [CLI] | 13 |
| 9 | CLI | ❌ `hermes proxy --port 4141` | `hermes proxy start --port 4141` | [CLI] | 1.4.13 |
| 10 | CLI | ❌ `hermes peer status` | `hermes peer status <target> <run_id>` | [CLI] | 1.4.35、15.4 |
| 11 | CLI | ❌ `hermes --voice` | 對話中 `/voice on` | [CLI] | 7.3 |
| 12 | CLI | ❌ `hermes kanban dispatch --tenant … --workspace …` | `hermes kanban create "…" --tenant … --workspace …` | [CLI] | 6.3.2 |
| 13 | CLI | ❌ `hermes connectors rename gmail old work` | `hermes connectors rename gmail old --to work` | [CLI] | 1.4.43 |
| 14 | CLI | ❌ `hermes photon login`、`hermes version` | `hermes photon setup`、`hermes --version` | [S][CLI] | B |
| 15 | CLI | ❌ `hermes mcp serve` | `hermes mcp-serve`（外掛） | [R:v0.23.0] | 11.1.16、B |
| 16 | 斜線 | ❌ `/background`、`/mouse`、`/fullstack`、`/devops`、`/security` | `/bg <prompt>`；`/mouse` 不存在；Bundle 須自行 `hermes bundles create` | [S] | 1.4.18、5、B |
| 17 | 設定 | ❌ `mcp: servers: [- name: …]` | 頂層 `mcp_servers.<name>` | [CFG][D] | 3.5.2、4.7、12 |
| 18 | 設定 | ❌ `security.command_approval`、`security.allowed_commands` | `approvals.mode`（smart／manual／off）、頂層 `command_allowlist` | [CFG][D] | 4.7、9.1.2、12 |
| 19 | 設定 | ❌ `auxiliary.provider`／`auxiliary.model` | `auxiliary.<任務>.provider/model`（例如 `auxiliary.compression`） | [CFG] | 3.6.1、4.7、9.2 |
| 20 | 設定 | ❌ `auxiliary.curator.enabled/interval_days/...` | 頂層 `curator.enabled/interval_hours/...` | [CFG] | 1.4.8、3.7.4 |
| 21 | 設定 | ❌ `kanban.enabled/max_retries/heartbeat_interval/...` | `kanban.dispatch_in_gateway/dispatch_interval_seconds/failure_limit/...`；重試為任務屬性 | [CFG][CLI] | 1.4.9、6.3.2、13 |
| 22 | 設定 | ❌ `memory.auto_save`、`memory.supermemory.*`、`memory.mem0.*` | `memory.write_approval` 等；Provider 設定由外掛管理 | [CFG][D] | 3.3.2、6.4 |
| 23 | 設定 | ❌ `voice.stt_provider/tts_provider/openai/...` | `stt.*`、`tts.*`、`voice.*`、`wake_word.*` | [CFG][D] | 7.3 |
| 24 | 設定 | ❌ `tool_search.*`（頂層） | `tools.tool_search.*` | [CFG] | 3.5.4 |
| 25 | 設定 | ❌ `terminal.docker.image/volumes` | `terminal.docker_image`、`terminal.docker_volumes` | [CFG] | 3.5.3 |
| 26 | 設定 | ❌ `context.auto_compress/compress_threshold` | `compression.enabled/threshold/target_ratio` | [CFG] | 9.2、9.3 |
| 27 | 設定 | ❌ `cron.jobs.<name>.schedule/task/context_from` | 以 `hermes cron create … --continuity --monitor-script …` 建立 | [CFG][CLI] | 5.5、6.6.5 |
| 28 | 設定 | ❌ `providers.primary/fallback` | `model.provider/default` + `fallback_providers: [{provider, model}]` | [CFG][D] | 3.6.1 |
| 29 | 設定 | ❌ `model_overrides."openrouter/x"` + 價格欄位 | `model_overrides.<provider>.<model>`；只有 `supports_*`、`context_window`、`model_family` | [S:agent/models_dev.py] | 1.4.41、D.1.3 |
| 30 | 設定 | ❌ `secrets.backend: bitwarden`、`secrets.sources: [{type, priority}]` | `secrets.bitwarden.enabled` 等；`secrets.sources: [名稱, …]` | [CFG][D] | 1.4.17、1.4.27 |
| 31 | 設定 | ❌ `session.auto_resume` | `hermes -c`／`--resume`（無此鍵） | [CFG] | 5.1.4 |
| 32 | 設定 | ❌ `quick_commands: {test: "mvn test"}` | `quick_commands.<name>: {type: exec, command: …}` | [D] | 5.1.3 |
| 33 | 環境變數 | ❌ `GOOGLE_AI_API_KEY` | `GEMINI_API_KEY`／`GOOGLE_API_KEY` | [D] | 4.6.2 |
| 34 | 環境變數 | ❌ `LM_STUDIO_URL`、`AZURE_AI_FOUNDRY_KEY`、`TENCENT_TOKENHUB_KEY`、`GOOGLE_CHAT_WEBHOOK`、`SIMPLEX_CHAT_PORT`、`GOOGLE_MEET_CREDENTIALS` | `LM_BASE_URL`、`AZURE_FOUNDRY_API_KEY`、`TOKENHUB_API_KEY`、`GOOGLE_CHAT_*`、`SIMPLEX_WS_URL`；最後一項移除 | [D][S] | C |
| 35 | 工具名稱 | ❌ `execute_command`、`browser_navigate`、`cron_add`、`voice_synthesize`、`blueprint_create` | `terminal`、`browser_exec`、`cronjob_manage`、`text_to_speech`；Blueprint 為斜線指令 | [D:tools-reference] | 2.3.5、3.5.1 |
| 36 | 工具格式 | ❌ `memory` 工具 `{"action","key","value"}` | `{"target", "operations":[{"action","content"/"old_text"}]}` | [D] | 1.4.23、3.3.3 |
| 37 | 技能格式 | ❌ `skill.md` + `## Description` | `SKILL.md` + YAML frontmatter；`~/.hermes/skills/<分類>/<名稱>/` | [D] | 3.2、6.1 |
| 38 | 外掛 API | ❌ `from hermes.plugins import PluginBase, hook` | 模組層級 `register(ctx)`；`plugin.yaml` 的 `provides_tools`／`provides_hooks` | [D] | 6.9 |
| 39 | 外掛 | ❌ 「Hook 共 26 種」；專案層級外掛以 `HERMES_ENABLE_PROJECT_PLUGINS` 開啟 | 46 種；v0.23.0 Gateway 不再載入專案層級外掛 | [S][D] | 6.9 |
| 40 | 安裝 | ❌ `ghcr.io/nousresearch/hermes-agent`、掛載 `/root/.hermes` | `nousresearch/hermes-agent`、掛載 `/opt/data`、`gateway run` | [D:docker] | 4.4、10.1 |
| 41 | 安裝 | ❌ `python:3.11-slim` + 手動 Node.js 26 自建映像 | `FROM nousresearch/hermes-agent:X.Y.Z` 衍生映像 | [D] | 4.4.2、10.1.1 |
| 42 | 安裝 | ❌ Windows NSIS installer、需系統管理員 | MSIX／Microsoft Store；`install.ps1` 不需要管理員 | [D] | 4.3、14.2 |
| 43 | 安裝 | ❌ root 安裝使用 `/usr/local/lib/hermes-agent/` | root 執行不會改用 FHS 路徑，使用 root 家目錄 | [D] | 4.1.2 |
| 44 | 部署 | ❌ K8s `replicas: 2` + RollingUpdate + RWX PVC | `replicas: 1` + `Recreate` + RWO；依團隊分片 | [D][R] | 2.5、10.2 |
| 45 | 部署 | ❌ 備份 `sessions.db`（sqlite3 `.backup`） | `hermes backup`（`state.db`、含憑證，需加密） | [CLI][D] | 10.5 |
| 46 | 架構 | ❌ 「LB → 多 Hermes → 共享 PostgreSQL／Redis／NFS」 | 無 PostgreSQL 後端；單一 Gateway 擁有 `state.db`（SQLite WAL） | [CFG][D] | 2.5 |
| 47 | 整合 | ❌ FastAPI 以子行程呼叫 `hermes chat --message/--session/--stream`、`hermes skills --json` | 呼叫 Gateway API Server `/v1/chat/completions` + `X-Hermes-Session-Key` | [CLI][D] | 8.2 |
| 48 | 整合 | ❌ Spring Boot 在建構子使用 `@Value` 欄位 | 建構子參數注入；技能名稱 `requesting-code-review` | 程式語意 | 8.3 |
| 49 | 事實 | ❌ 「OpenClaw 是 Hermes 的前身」 | 兩者是不同專案 | [D] | 11.3.1 |
| 50 | 事實 | ❌ `sessions.auto_prune` 預設開啟（依 v0.22.0 release notes） | v0.23.0 預設關閉，磁碟不足時詢問 | [S][D] | 9.9.6、11.1.16 |

### E.3 實測方法與結果

#### E.3.1 檢查工具

| 工具 | 作用 | 負面測試（證明它真的會抓錯） |
| --- | --- | --- |
| `dump_help.py` | 走訪 v0.23.0 的 argparse 樹，輸出 `cli.json`（507 條路徑、旗標、帶值旗標） | — |
| `dump_registry.py` | 匯出斜線指令登錄表與 `DEFAULT_CONFIG` 設定鍵 | — |
| `check_doc.py` | 對手冊做 7 類檢查：CLI 白名單、**真實 argparse 解析**（PARSE）、斜線指令、設定鍵（呼叫官方驗證器）、`.env` 變數名稱、inline 指令、歷史敘述辨識（INFO） | 原稿：175 項發現 |
| `check_synopsis.py` | 展開附錄 B 的 `a\|b\|c` 多選寫法，逐一比對白名單 | 原稿：17 項發現 |
| `validate_k8s.py` | 解析部署 YAML，斷言 `replicas == 1`、`Recreate`、`/health` probe、`/opt/data`、RWO、loopback 埠號；`bash -n` 檢查腳本 | 內建反例：6 項違規；原稿第十章：9 項 |
| `test_facade.py` | 以模擬 Hermes API Server 端對端測試第八章的 FastAPI Facade | 上游 401 → 502 等 9 項 |
| `JavaParse.java` | 以 `JavacTask.parse()`（JDK 21）做 Java 語法檢查 | 含 `int x = ;` 的檔案回報 1 項錯誤、exit 1 |

核心方法很簡單：**不要相信文件，直接把每一行指令交給真正的 parser**。以下是 `try_parse.py` 的完整內容，可以用來驗證任何一份文件中的 `hermes` 指令：

```python
"""Parse argv lists (one per line, shlex) with the real hermes parser; print OK/EXIT."""
import shlex, sys, io, contextlib
from hermes_cli.main import _build_cli_parser
p = _build_cli_parser()[0]
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    argv = shlex.split(line)[1:]
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            p.parse_args(argv)
        print("OK  ", line)
    except SystemExit as e:
        print(f"EXIT{e.code}", line, "|", err.getvalue().strip().splitlines()[-1:] )
```

設定鍵則直接呼叫 `hermes config set` 使用的同一個函式：

```python
from hermes_cli.config import _validate_config_key
print(_validate_config_key("kanban.enabled"))        # (False, None)  → 不是有效鍵
print(_validate_config_key("approvals.mode"))        # (True, None)
print(_validate_config_key("tool_search.enabled"))   # (False, 'x_search.enabled') → 實際應為 tools.tool_search.enabled
```

#### E.3.2 結果

| 檢查 | 原稿（v8.0.0） | 本版（v9.0.0） |
| --- | --- | --- |
| `check_doc.py --inline`（20 個章節檔逐一執行） | 175 項發現（CFG 100、CLI 19、PARSE 20、ENV 2、SLASH 4、CLI-inline 12、PARSE-inline 10、SLASH-inline 8） | **0**（組裝後的完整文件；另有 INFO 36 項，皆為明確標示「舊名／已移除／改為」的歷史敘述） |
| `check_synopsis.py`（附錄 B） | 17 | **0** |
| `validate_k8s.py`（第十章） | 9 | **0**（yaml 5、Deployment 1、PVC 1、compose 1、bash 1） |
| `test_facade.py`（第八章 FastAPI） | 原稿程式碼使用不存在的 CLI 旗標，無法運作 | **9/9 PASS** |
| Java 語法（`HermesAgentClient.java`） | 有 `@Value` 建構子注入時序錯誤（語法正確但執行期為 `null`） | **0 diagnostics** |
| Python 語法（`agent_service.py`） | — | `py_compile` 通過 |

#### E.3.3 安裝過程中的實測發現

| 發現 | 影響 | 處理 |
| --- | --- | --- |
| 本機 uv 0.8.17 讀不懂 v0.23.0 的 `uv.lock`（`invalid type: boolean false, expected a timestamp string`） | 舊版 uv 無法照官方 lock 安裝 | 改用 uv 0.13.7（官方安裝腳本本來就會下載校驗過的 uv pin） |
| `uv pip install -r` 因 `pillow` 版本衝突失敗（`browser-harness` 要 12.3.0、主套件要 13.0.0） | 上游依賴 `uv.lock` 的 override 才能解析 | `uv export --frozen` 後以 `--no-deps` 安裝 |
| `pip install .` 拋出 `RuntimeError: Building wheels or sdists for hermes-agent is not supported` | 官方刻意禁止 wheel／sdist | 改用 editable install（4.2.2） |
| 從 tarball 安裝時 `hermes --version` 顯示 `vunknown (2026.9.24)` | 版本取自 git tag | 正式評估請用 git checkout 或官方安裝腳本 |
| `hermes config check` 不會報告未知鍵 | 不能用它驗證設定檔內容 | 以 `hermes config set`（會提示 unknown key）或 `check_doc.py` 驗證 |
| `hermes config set skills.config.<x>` 會成功寫入，但同時警告「not a recognized config key」 | 與官方文件「技能設定存於 `skills.config`」不一致 | 列入 E.4；checker 以 INFO 回報 |
| `model_overrides` 底下的任意鍵都會通過驗證器 | 錯誤的欄位（例如價格）不會被提示 | 人工比對 `agent/models_dev.py` 讀取的欄位（D.1.3） |

#### E.3.4 重新執行方式

```bash
# 1) 取得原始碼並建立隔離環境（不影響 ~/.hermes）
gh api repos/NousResearch/hermes-agent/tarball/v0.23.0 > v0.23.0.tgz
mkdir tree && tar -xzf v0.23.0.tgz -C tree --strip-components=1
uv python install 3.14 && uv venv --python 3.14 .venv
uv export --project tree --frozen --no-hashes --no-emit-project -o req.txt
uv pip install --python .venv/bin/python --no-deps -r req.txt
uv pip install --python .venv/bin/python --no-deps -e tree
uv pip install --python .venv/bin/python pyyaml

# 2) 匯出白名單後檢查文件（HERMES_HOME 指向暫存目錄）
export HERMES_HOME="$PWD/home"
.venv/bin/python -X utf8 dump_help.py cli.json
.venv/bin/python -X utf8 dump_registry.py .
.venv/bin/python -X utf8 check_doc.py "Hermes Agent生態系教學手冊.md" . --inline
```

### E.4 待確認事項

| # | 事項 | 現況 | 建議 |
| --- | --- | --- | --- |
| 1 | CVE-2026-10224、CVE-2026-10221（影響 `<= 0.19.0`）沒有列出修補版本 | v0.23.0 不在宣告的影響範圍內，但無法從公告確認修補狀態 | 每月以 9.9.1 的查詢追蹤；必要時向上游詢問 |
| 2 | 官方仍未在倉庫發布 Repository Security Advisory | `security-advisories` API 結果為空 | 弱點情資以 GitHub Advisory Database／NVD 為準 |
| 3 | `skills.config.*` 被 `hermes config set` 判為未知鍵，與文件說明不一致 | 值仍會寫入；技能是否讀取未以實際對話驗證 | 導入時以實際技能驗證，或以 `hermes config migrate` 寫入 |
| 4 | RetainDB／ByteRover：文件同時說「仍內建」與「2026-10-15 移出核心、上游無人維護」 | v0.23.0 原始碼中仍內建 | 選用時把「上游無人維護」列入風險 |
| 5 | 開發者架構文件寫「Terminal 7 backends」，使用者設定文件寫「6 種」 | 本手冊採使用者設定文件與 `terminal.backend` 選項（6 種 + 外掛） | 以 `hermes config` 實際可用值為準 |
| 6 | Nous Portal 定價與方案 | 未在本版重新查證 | 上線前至 portal.nousresearch.com/manage-subscription 覆核 |
| 7 | Desktop、Webapp、Local Models、Connectors 的 GUI 行為 | 依官方文件與 release notes 撰寫，未在本機實際操作 | 導入評估時依各章清單實機驗證 |
| 8 | 模型 ID（`claude-sonnet-5-5`、`gemini-4-argon` 等） | 已確認出現在 v0.23.0 原始碼，但可用性取決於 Provider 目錄 | 以 `/model` 選擇器列出的 ID 為準 |

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
| **v0.23.0 Release Notes（The Hearth）** | [releases/tag/v0.23.0](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0) |
| **v0.22.0 Release Notes（The Threshold）** | [releases/tag/v0.22.0](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0) |
| **更新與通道（含回退限制）** | [/docs/getting-started/updating](https://hermes-agent.nousresearch.com/docs/getting-started/updating) |
| **Webapp 與 Desktop（見 14.6 節）** | [/docs/user-guide/desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) |
| **Local Models（見 1.4.44 節）** | [/docs/user-guide/local-models](https://hermes-agent.nousresearch.com/docs/user-guide/local-models) |
| **Plugin Catalog 與信任模型（見 1.4.46、6.9 節）** | [/docs/user-guide/features/plugin-catalog](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugin-catalog) |
| **Nous Tool Gateway 與 Connectors（見 1.4.43 節）** | [/docs/user-guide/features/tool-gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway) |
| **Multi-profile Gateways（見 2.3.2 節）** | [/docs/user-guide/multi-profile-gateways](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways) |
| **Docker（見 4.4、10.1 節）** | [/docs/user-guide/docker](https://hermes-agent.nousresearch.com/docs/user-guide/docker) |
| **API Server（見 8.2 節）** | [/docs/user-guide/features/api-server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server) |
| **委派策略（見 1.4.51 節）** | [/docs/user-guide/features/delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) |
| **MCP 工具成本與花費上限（見 1.4.50 節）** | [/docs/user-guide/features/mcp](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) |
| **從其他 Agent 匯入（見 11.3 節）** | [/docs/user-guide/import-from-other-agents](https://hermes-agent.nousresearch.com/docs/user-guide/import-from-other-agents) |
| **GitHub Advisory Database：hermes-agent（見 9.9.1 節）** | [github.com/advisories?query=hermes-agent](https://github.com/advisories?query=hermes-agent) |
| 社群生態系目錄（非官方，見 9.7.5 節使用提醒） | [github.com/0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) |
| 第三方企業威脅模型（**非官方觀點**，見 9.7.1 節） | [repello.ai/blog/hermes-agent-security](https://repello.ai/blog/hermes-agent-security) |

---

> **文件版本**：v9.0.0
> **基於 Hermes Agent**：v0.23.0（Git tag `v0.23.0`，The Hearth Release，2026-11-05；涵蓋 v0.21.1–v0.22.7 補丁與 v0.22.0 The Threshold）
> **建立日期**：2026 年 4 月 9 日
> **最後更新**：2026 年 11 月 8 日
> **維護者**：技術架構團隊
> **本次更新重點**：
>
> 1. **版本基準升至 v0.23.0**：補齊 v0.21.1–v0.21.7、v0.22.0–v0.22.7 與 v0.23.0 的發展歷程；GitHub 統計依 REST API 覆核（Stars 261,617／Forks 58,096／Releases 47）
> 2. **以實際安裝的 v0.23.0 驗證全文**：指令以真實 argparse 樹（507 條路徑）逐行解析、設定鍵以官方驗證器逐鍵檢查、環境變數以官方參考比對；原稿自動檢查共 **201 項發現**（`check_doc.py` 175、`check_synopsis.py` 17、`validate_k8s.py` 9），連同人工審查發現的問題已全部更正，修正後三項檢查皆為 0（詳見附錄 E.2、E.3）
> 3. **架構重寫**：第二章依「單一 Gateway 擁有所有 Session」重繪架構與高可用設計；第十章 K8s 改為 `replicas: 1` + `Recreate` + RWO PVC，備份改用 `hermes backup` 並加密
> 4. **新增內容**：1.4.42–1.4.52（穩定通道、Connectors、Local Models、Plugin Catalog、Webapp、`/rewind`、Group Chats、付費工具上限、可插拔委派、`curator lock`）、9.9（公開弱點、tirith 替代方案、外掛信任邊界、Webapp、Session 保存）、11.1.16（15 項破壞性變更對照）、14.6–14.7（Webapp、多 Gateway）、15.3.1（Group Chats 自主運作）、FAQ Q29–Q37、附錄 A.7
> 5. **Web 整合重寫**：第八章改為呼叫 Gateway 的 OpenAI 相容 API Server；FastAPI Facade 以模擬伺服器實測 9/9 通過，Java 以 `JavacTask.parse()` 通過語法驗證
> 6. **每章新增「本章審查與驗證清單」**：每一項都附可執行的驗證指令與預期結果
> 7. **新增附錄 E「驗證紀錄」**：版本基準、更正清單、實測方法與結果、待確認事項，以及可重複執行的檢查工具
> 8. **目錄與格式**：目錄依 Hugo 實際產生的錨點重建，並以 Hugo 輸出頁面逐一比對所有內部連結
