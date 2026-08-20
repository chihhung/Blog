+++
date = '2026-08-20T14:00:54+08:00'
draft = false
title = 'Prime Agent教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# Prime Agent 教學手冊（企業導入與實戰完整版）

> **版本**：v0.7.4（2026 年 8 月 19 日發布；本手冊查證日期 2026 年 8 月 20 日）
> **適用對象**：初學者、一般開發者、資深工程師、架構師、DevSecOps 工程師、PM／SA、AI Agent 導入負責人
> **技術棧示範**：Java 25 / Spring Boot 4.x / Spring Framework 7.x / Maven 4.x / Vue 3 / TypeScript / Tailwind CSS / PrimeVue / Pinia / PostgreSQL / Oracle / DB2 / SQL Server / Redis / Kafka / MQ
> **授權**：MIT License
> **開發／維護**：[Prime Intellect](https://www.primeintellect.ai/)
> **專案性質**：[`earendil-works/pi`](https://github.com/earendil-works/pi) 的 Hard Fork（詳見第 1 章），npm 套件內部仍沿用 `@earendil-works/pi-coding-agent`
> **官方倉庫**：[github.com/PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)
> **文件用途**：企業 AI Software Development／Agent Engineering 導入教材
> **文件作者**：AI Software Architecture Team

---

## 文件目的與適用對象

本手冊的目的，是把 Prime Agent 從「一個開源 CLI 工具」轉化為「企業 AI Software Development Team 的核心 Agent Runtime」——讓 AI Agent 能夠**長時間、可恢復、可驗證、可自我改善**地完成 Web Application 開發、Legacy Reverse Engineering 與 Framework Modernization。

| 讀者角色 | 建議閱讀重點 |
|----------|----------------|
| 初學者 | 第 1–10 章（定位、核心概念、安裝、第一個專案） |
| 一般開發者 | 第 1–22 章、第 45–54 章（實戰案例、Prompt Library、RLM Tutorial） |
| Senior Developer | 第 11–31 章、第 41–49 章（架構整合、Multi-Agent、實戰案例） |
| Architect | 第 4、5、13、14、30、31、55、56 章（架構、Multi-Agent 設計、安全邊界、ADR、Enterprise Architecture） |
| PM／SA／Manager | 第 32–40 章、第 57 章（導入策略、治理、KPI、成本、Roadmap） |
| Enterprise／Governance | 第 38–40、44、58–60 章（治理、SOP、常見錯誤、最佳實務、Checklist） |

**前置條件**：具備基本 Git／CLI 操作經驗；理解至少一種本手冊示範技術棧（Java/Spring Boot 或 Vue/TypeScript）者，能更快上手第 8–10、45 章的實戰內容。

---

## 關於本手冊的查證方法

本手冊撰寫前，針對 Prime Agent 的 GitHub 原始碼、官方文件（`packages/coding-agent/docs/*.md`）與 Prime Intellect 官網／Blog 逐一查證。凡是查無官方依據的內容，一律標示為「企業建議」或「注意」，不假裝是官方功能。

### 標籤說明

本手冊全文使用以下標籤區分「查證過的官方事實」與「本手冊給企業的建議」：

| 標籤 | 意義 |
|------|------|
| 🟢 **官方功能** | 已在 Prime Agent 原始碼或官方文件中逐字確認 |
| 🔵 **企業建議** | 官方未規範，屬本手冊針對企業導入提出的架構建議 |
| 🟡 **實驗性** | 功能存在但可能隨版本快速變化，或官方文件未明確承諾穩定性 |
| 🔴 **注意** | 存在安全、成本、資料正確性或穩定性風險，需要特別留意 |

---

<!-- TOC-AUTO-BEGIN -->
## 目錄（Table of Contents）

- [1. Prime Agent 是什麼](#1-prime-agent-是什麼)
  - [1.1 Prime Agent 的定位](#11-prime-agent-的定位)
  - [1.2 Prime Agent 不是什麼](#12-prime-agent-不是什麼)
  - [1.3 與 pi 的血緣關係（🔴 重要背景）](#13-與-pi-的血緣關係-重要背景)
  - [1.4 為什麼需要新的 Agent Harness](#14-為什麼需要新的-agent-harness)
  - [1.5 Prime Agent 的設計哲學：RLM + Continual Harness + Persistent Runtime](#15-prime-agent-的設計哲學rlm-continual-harness-persistent-runtime)
  - [1.6 傳統 Agent vs Prime Agent](#16-傳統-agent-vs-prime-agent)
  - [1.7 Prime Agent 不適合做什麼（先預告，第 58 章有完整版）](#17-prime-agent-不適合做什麼先預告第-58-章有完整版)
  - [1.8 ARC-AGI-3 Benchmark（官方宣稱，需正確理解限制）](#18-arc-agi-3-benchmark官方宣稱需正確理解限制)
  - [1.9 Long-Context Benchmark 結果（與企業場景較貼近的第二組官方數據）](#19-long-context-benchmark-結果與企業場景較貼近的第二組官方數據)
- [2. Prime Agent 核心概念（RLM）](#2-prime-agent-核心概念rlm)
  - [2.1 概念出處](#21-概念出處)
  - [2.2 傳統 Agent vs RLM：兩種思維方式](#22-傳統-agent-vs-rlm兩種思維方式)
  - [2.3 RLM 的實際 API（原始碼與文件逐字確認）](#23-rlm-的實際-api原始碼與文件逐字確認)
    - [2.3.1 `rlm()` — 動態產生子 Agent](#231-rlm-動態產生子-agent)
    - [2.3.2 管理子 Agent](#232-管理子-agent)
    - [2.3.3 `agent_message` — Agent 對 Agent（A2A）通訊](#233-agent_message-agent-對-agenta2a通訊)
    - [2.3.4 一個完整的最小範例](#234-一個完整的最小範例)
  - [2.4 小結與注意事項](#24-小結與注意事項)
- [3. Continual Harness](#3-continual-harness)
  - [3.1 概念出處](#31-概念出處)
  - [3.2 核心定義：H = Prompt + Sub-agents + Skills + Memory](#32-核心定義h-prompt-sub-agents-skills-memory)
  - [3.3 `/refine`：CRUD 的官方入口](#33-refinecrud-的官方入口)
  - [3.4 `rlm.harness`：原始碼中存在、但非官方公開介紹的內部介面](#34-rlmharness原始碼中存在但非官方公開介紹的內部介面)
  - [3.5 Session / Global / Local 狀態層級](#35-session-global-local-狀態層級)
- [4. Prime Agent 整體架構](#4-prime-agent-整體架構)
  - [4.1 架構總覽](#41-架構總覽)
  - [4.2 各元件說明](#42-各元件說明)
  - [4.3 為什麼這個架構適合長時間任務](#43-為什麼這個架構適合長時間任務)
  - [4.4 架構層與後續章節對應](#44-架構層與後續章節對應)
- [5. Runtime 與 Process Model](#5-runtime-與-process-model)
  - [5.1 Daemon／Worker／Kernel 三層模型](#51-daemonworkerkernel-三層模型)
  - [5.2 Session 生命週期狀態](#52-session-生命週期狀態)
  - [5.3 當機復原（Crash Recovery）](#53-當機復原crash-recovery)
  - [5.4 Runtime 與後續章節的關係](#54-runtime-與後續章節的關係)
- [6. Session Persistence](#6-session-persistence)
  - [6.1 Session 的持久化機制](#61-session-的持久化機制)
  - [6.2 常用 CLI 指令（原始碼逐字確認）](#62-常用-cli-指令原始碼逐字確認)
  - [6.3 Session 生命週期時序](#63-session-生命週期時序)
  - [6.4 為什麼企業要重視 Session Persistence](#64-為什麼企業要重視-session-persistence)
- [7. 安裝環境](#7-安裝環境)
  - [7.1 系統需求](#71-系統需求)
  - [7.2 Linux 安裝](#72-linux-安裝)
  - [7.3 macOS 安裝](#73-macos-安裝)
  - [7.4 Beta 版與原始碼安裝](#74-beta-版與原始碼安裝)
  - [7.5 Windows 環境（🔴 注意：非原生支援，需要 bash）](#75-windows-環境-注意非原生支援需要-bash)
- [8. 安裝與驗證](#8-安裝與驗證)
  - [8.1 首次啟動](#81-首次啟動)
  - [8.2 安裝後驗證指令](#82-安裝後驗證指令)
  - [8.3 更新與移除](#83-更新與移除)
  - [8.4 沒有獨立文件網站](#84-沒有獨立文件網站)
- [9. Provider 與 Model 設定](#9-provider-與-model-設定)
  - [9.1 訂閱式登入（`/login`）](#91-訂閱式登入login)
  - [9.2 API Key 環境變數（Provider 清單）](#92-api-key-環境變數provider-清單)
  - [9.3 本地／自架模型](#93-本地自架模型)
  - [9.4 Provider / Model / Authentication 對照](#94-provider-model-authentication-對照)
- [10. 第一個 Prime Agent 專案](#10-第一個-prime-agent-專案)
  - [10.1 情境設定](#101-情境設定)
  - [10.2 啟動與初次分析](#102-啟動與初次分析)
  - [10.3 建立專案專屬的 Memory 與 Skill](#103-建立專案專屬的-memory-與-skill)
  - [10.4 建立第一個 Sub-agent 分工](#104-建立第一個-sub-agent-分工)
  - [10.5 小結](#105-小結)
- [11. 使用 Prime Agent 開發 Web Application](#11-使用-prime-agent-開發-web-application)
  - [11.1 完整 AI Software Development Workflow](#111-完整-ai-software-development-workflow)
  - [11.2 各階段 Prime Agent 的角色](#112-各階段-prime-agent-的角色)
  - [11.3 企業 Web Application 技術棧整合案例](#113-企業-web-application-技術棧整合案例)
  - [11.4 實務案例](#114-實務案例)
- [12. Prime Agent 與 Spec-Driven Development](#12-prime-agent-與-spec-driven-development)
  - [12.1 為什麼要搭配 Spec-Driven Development](#121-為什麼要搭配-spec-driven-development)
  - [12.2 各階段 Prompt Template（🔵 企業建議）](#122-各階段-prompt-template-企業建議)
  - [12.3 實務案例](#123-實務案例)
- [13. Multi-Agent Architecture](#13-multi-agent-architecture)
  - [13.1 設計概念](#131-設計概念)
  - [13.2 實際 Python 範例：平行分工](#132-實際-python-範例平行分工)
  - [13.3 Parent／Child／Sibling 關係與並行策略](#133-parentchildsibling-關係與並行策略)
- [14. Sub-Agent 設計方法](#14-sub-agent-設計方法)
  - [14.1 企業常用 Agent Team](#141-企業常用-agent-team)
  - [14.2 Migration Agent（升級／遷移專用角色，🔵 企業建議）](#142-migration-agent升級遷移專用角色-企業建議)
  - [14.3 Documentation Agent（🔵 企業建議）](#143-documentation-agent-企業建議)
  - [14.4 治理提醒](#144-治理提醒)
- [15. Skills 設計](#15-skills-設計)
  - [15.1 Skills 是什麼](#151-skills-是什麼)
  - [15.2 SKILL.md 格式](#152-skillmd-格式)
  - [15.3 Skills 載入順序與內建 Skills](#153-skills-載入順序與內建-skills)
  - [15.4 企業 Skill 目錄設計（企業建議）](#154-企業-skill-目錄設計企業建議)
  - [15.5 三個完整 Skill 範例（另有 2 個範例於附錄 D）](#155-三個完整-skill-範例另有-2-個範例於附錄-d)
  - [15.6 Skill 治理提醒](#156-skill-治理提醒)
- [16. Memory 設計](#16-memory-設計)
  - [16.1 什麼資料應該進 Memory](#161-什麼資料應該進-memory)
  - [16.2 什麼資料不應該進 Memory](#162-什麼資料不應該進-memory)
  - [16.3 常見 Memory 反模式](#163-常見-memory-反模式)
  - [16.4 治理層級對應表](#164-治理層級對應表)
- [17. /refine 自我改進](#17-refine-自我改進)
  - [17.1 完整流程](#171-完整流程)
  - [17.2 `/refine` 實務操作](#172-refine-實務操作)
  - [17.3 Evidence-based Refinement（企業建議的審核原則）](#173-evidence-based-refinement企業建議的審核原則)
  - [17.4 企業使用規範：Agent 不應任意修改核心 System Prompt](#174-企業使用規範agent-不應任意修改核心-system-prompt)
- [18. Autonomous Mode](#18-autonomous-mode)
  - [18.1 Autonomous Mode 概述](#181-autonomous-mode-概述)
  - [18.2 完整旗標表（原始碼逐字確認）](#182-完整旗標表原始碼逐字確認)
  - [18.3 Goal 與 Heartbeat 搭配](#183-goal-與-heartbeat-搭配)
  - [18.4 Autonomous ≠ 無限制執行](#184-autonomous-無限制執行)
- [19. Long-running Agent](#19-long-running-agent)
  - [19.1 為什麼適合長時間任務](#191-為什麼適合長時間任務)
  - [19.2 Agent 對 Agent 通訊、Heartbeat 與 Goal](#192-agent-對-agent-通訊heartbeat-與-goal)
  - [19.3 Checkpoint、Compaction 與 Persistence](#193-checkpointcompaction-與-persistence)
  - [19.4 為什麼企業要重視 Long-running Agent 的觀察機制](#194-為什麼企業要重視-long-running-agent-的觀察機制)
- [20. Reverse Engineering／Legacy 分析](#20-reverse-engineeringlegacy-分析)
  - [20.1 情境：企業常見 Legacy System](#201-情境企業常見-legacy-system)
  - [20.2 分析工作流](#202-分析工作流)
  - [20.3 拆分子 Agent 平行分析（實際 Prompt 範例）](#203-拆分子-agent-平行分析實際-prompt-範例)
  - [20.4 輸出範例結構（企業建議格式）](#204-輸出範例結構企業建議格式)
  - [20.5 實務提醒](#205-實務提醒)
- [21. Framework Upgrade 標準作業流程](#21-framework-upgrade-標準作業流程)
  - [21.1 案例情境](#211-案例情境)
  - [21.2 AI Framework Upgrade 標準作業流程（企業建議）](#212-ai-framework-upgrade-標準作業流程企業建議)
  - [21.3 各階段說明](#213-各階段說明)
  - [21.4 實務提醒](#214-實務提醒)
- [22. Java／Spring Boot 升級案例](#22-javaspring-boot-升級案例)
  - [22.1 完整流程總覽](#221-完整流程總覽)
  - [22.2 步驟一：分析與計畫（不修改檔案）](#222-步驟一分析與計畫不修改檔案)
  - [22.3 步驟二：拆分子 Agent 平行分析](#223-步驟二拆分子-agent-平行分析)
  - [22.4 步驟三：計畫確認後執行 Autonomous 遷移](#224-步驟三計畫確認後執行-autonomous-遷移)
  - [22.5 實務提醒](#225-實務提醒)
- [23. Database Migration](#23-database-migration)
  - [23.1 案例情境](#231-案例情境)
  - [23.2 型別對照表範例（🔵 企業建議，需依實際版本驗證）](#232-型別對照表範例-企業建議需依實際版本驗證)
  - [23.3 Prompt 範例](#233-prompt-範例)
  - [23.4 Stored Procedure 與交易語意](#234-stored-procedure-與交易語意)
  - [23.5 實務提醒](#235-實務提醒)
- [24. Legacy Modernization](#24-legacy-modernization)
  - [24.1 現代化流程](#241-現代化流程)
  - [24.2 各階段說明](#242-各階段說明)
  - [24.3 Characterization Test 範例 Prompt](#243-characterization-test-範例-prompt)
  - [24.4 實務提醒](#244-實務提醒)
- [25. AI Agent Code Review](#25-ai-agent-code-review)
  - [25.1 多 Agent 審查流程](#251-多-agent-審查流程)
  - [25.2 與既有工具整合](#252-與既有工具整合)
  - [25.3 Review Prompt 範例](#253-review-prompt-範例)
  - [25.4 實務提醒](#254-實務提醒)
- [26. DevSecOps](#26-devsecops)
  - [26.1 Prime Agent 在 DevSecOps 管線中的位置](#261-prime-agent-在-devsecops-管線中的位置)
  - [26.2 各階段對應](#262-各階段對應)
  - [26.3 企業 Security Gate（🔵 企業建議）](#263-企業-security-gate-企業建議)
  - [26.4 實務提醒](#264-實務提醒)
- [27. MCP 整合](#27-mcp-整合)
  - [27.1 Prime Agent 的 MCP 實作方式（🔴 重要修正）](#271-prime-agent-的-mcp-實作方式-重要修正)
  - [27.2 目前實際內建的 MCP 整合](#272-目前實際內建的-mcp-整合)
  - [27.3 修正原始企業規劃中的常見假設](#273-修正原始企業規劃中的常見假設)
  - [27.4 MCP 安全考量](#274-mcp-安全考量)
- [28. JSON／RPC／Headless 自動化](#28-jsonrpcheadless-自動化)
  - [28.1 JSON Mode](#281-json-mode)
  - [28.2 RPC Mode](#282-rpc-mode)
  - [28.3 CI/CD 整合案例](#283-cicd-整合案例)
- [29. Git／GitHub 工作流程](#29-gitgithub-工作流程)
  - [29.1 標準工作流程](#291-標準工作流程)
  - [29.2 安全規則（🔵 企業建議，比照業界通用最佳實務）](#292-安全規則-企業建議比照業界通用最佳實務)
  - [29.3 實務案例](#293-實務案例)
- [30. Prime Agent 安全模型](#30-prime-agent-安全模型)
  - [30.1 官方 Trust Model 逐字確認（🔴 全書最重要的一段）](#301-官方-trust-model-逐字確認-全書最重要的一段)
  - [30.2 風險清單](#302-風險清單)
  - [30.3 企業安全使用 Checklist（完整版見附錄 F）](#303-企業安全使用-checklist完整版見附錄-f)
- [31. Sandbox Architecture](#31-sandbox-architecture)
  - [31.1 官方建議的隔離方向](#311-官方建議的隔離方向)
  - [31.2 實作選項比較](#312-實作選項比較)
  - [31.3 網路與憑證管理原則](#313-網路與憑證管理原則)
  - [31.4 何時需要沙箱、何時不需要](#314-何時需要沙箱何時不需要)
- [32. 金融業／銀行系統導入](#32-金融業銀行系統導入)
  - [32.1 案例情境](#321-案例情境)
  - [32.2 Prime Agent 在此技術棧中的角色](#322-prime-agent-在此技術棧中的角色)
  - [32.3 金融業特有的資料存取限制（🔴 重要）](#323-金融業特有的資料存取限制-重要)
  - [32.4 實務提醒](#324-實務提醒)
- [33. Prime Agent 與 SSDLC](#33-prime-agent-與-ssdlc)
  - [33.1 完整管線](#331-完整管線)
  - [33.2 各階段指定 Agent](#332-各階段指定-agent)
  - [33.3 實務提醒](#333-實務提醒)
- [34. Prime Agent 與 AI Software Development Team](#34-prime-agent-與-ai-software-development-team)
  - [34.1 團隊架構](#341-團隊架構)
  - [34.2 人類角色如何與 Agent Team 協作](#342-人類角色如何與-agent-team-協作)
  - [34.3 實務提醒](#343-實務提醒)
- [35. PM／SA／Architect／Developer 工作方式改變](#35-pmsaarchitectdeveloper-工作方式改變)
  - [35.1 從「人寫 Code，AI 幫忙」到「人設計系統，Agent 執行驗證」](#351-從人寫-codeai-幫忙到人設計系統agent-執行驗證)
  - [35.2 各角色的轉變](#352-各角色的轉變)
  - [35.3 實務提醒](#353-實務提醒)
- [36. Prime Agent 與其他 AI Coding Agent 比較](#36-prime-agent-與其他-ai-coding-agent-比較)
  - [36.1 定性比較（不做無依據排名）](#361-定性比較不做無依據排名)
  - [36.2 功能維度對照](#362-功能維度對照)
  - [36.3 什麼情境適合什麼工具（🔵 企業建議）](#363-什麼情境適合什麼工具-企業建議)
- [37. Prime Agent 導入策略](#37-prime-agent-導入策略)
  - [37.1 六個導入等級](#371-六個導入等級)
  - [37.2 各 Level 說明](#372-各-level-說明)
  - [37.3 實務提醒](#373-實務提醒)
- [38. Team Governance](#38-team-governance)
  - [38.1 治理項目清單](#381-治理項目清單)
  - [38.2 治理組織建議](#382-治理組織建議)
  - [38.3 實務提醒](#383-實務提醒)
- [39. Agent KPI](#39-agent-kpi)
  - [39.1 可量化 KPI 清單](#391-可量化-kpi-清單)
  - [39.2 KPI 使用原則](#392-kpi-使用原則)
- [40. Cost Management](#40-cost-management)
  - [40.1 成本構成](#401-成本構成)
  - [40.2 Cost Guardrail 設計](#402-cost-guardrail-設計)
  - [40.3 實務提醒](#403-實務提醒)
- [41. Troubleshooting](#41-troubleshooting)
  - [41.1 診斷方法論](#411-診斷方法論)
  - [41.2 症狀 → 原因 → 診斷 → 解決方案](#412-症狀-原因-診斷-解決方案)
- [42. 維運](#42-維運)
  - [42.1 日常維運指令](#421-日常維運指令)
  - [42.2 Logs](#422-logs)
  - [42.3 Session Cleanup 與 Disk Usage](#423-session-cleanup-與-disk-usage)
  - [42.4 Artifact Management、Backup 與 Recovery](#424-artifact-managementbackup-與-recovery)
- [43. 升級策略](#43-升級策略)
  - [43.1 升級流程](#431-升級流程)
  - [43.2 實際指令](#432-實際指令)
  - [43.3 升級檢查清單](#433-升級檢查清單)
- [44. 企業標準 SOP](#44-企業標準-sop)
  - [44.1 SOP 總覽](#441-sop-總覽)
  - [44.2 SOP 範例：SOP-03 Framework Upgrade](#442-sop-範例sop-03-framework-upgrade)
  - [44.3 Prime Agent Development Standard（PA-001~010）](#443-prime-agent-development-standardpa-001010)
- [45. 實戰案例一：建立 Vue 與 Spring Boot 系統](#45-實戰案例一建立-vue-與-spring-boot-系統)
  - [45.1 情境](#451-情境)
  - [45.2 步驟一：Architecture 規劃](#452-步驟一architecture-規劃)
  - [45.3 步驟二：Multi-Agent 分工建立骨架](#453-步驟二multi-agent-分工建立骨架)
  - [45.4 步驟三：實作第一個 API](#454-步驟三實作第一個-api)
  - [45.5 步驟四：安全與文件](#455-步驟四安全與文件)
  - [45.6 步驟五：`/refine` 沉澱](#456-步驟五refine-沉澱)
  - [45.7 小結](#457-小結)
- [46. 實戰案例二：Spring Boot 3 升級到 4](#46-實戰案例二spring-boot-3-升級到-4)
  - [46.1 情境](#461-情境)
  - [46.2 步驟一：分析](#462-步驟一分析)
  - [46.3 步驟二：人工確認後執行 Autonomous 遷移](#463-步驟二人工確認後執行-autonomous-遷移)
  - [46.4 步驟三：追蹤進度](#464-步驟三追蹤進度)
  - [46.5 步驟四：Review 與合併](#465-步驟四review-與合併)
  - [46.6 小結](#466-小結)
- [47. 實戰案例三：Legacy Java Reverse Engineering](#47-實戰案例三legacy-java-reverse-engineering)
  - [47.1 情境](#471-情境)
  - [47.2 步驟一：啟動平行分析](#472-步驟一啟動平行分析)
  - [47.3 步驟二：監控平行子 Agent 進度](#473-步驟二監控平行子-agent-進度)
  - [47.4 步驟三：彙整報告](#474-步驟三彙整報告)
  - [47.5 步驟五：人工審核與後續規劃](#475-步驟五人工審核與後續規劃)
  - [47.6 小結](#476-小結)
- [48. 實戰案例四：長時間 Autonomous Refactoring](#48-實戰案例四長時間-autonomous-refactoring)
  - [48.1 情境](#481-情境)
  - [48.2 步驟一：設定 Goal 與心跳](#482-步驟一設定-goal-與心跳)
  - [48.3 步驟二：週末心跳監控](#483-步驟二週末心跳監控)
  - [48.4 步驟三：週一檢視](#484-步驟三週一檢視)
  - [48.5 步驟四：`/refine` 沉澱長任務經驗](#485-步驟四refine-沉澱長任務經驗)
  - [48.6 小結](#486-小結)
- [49. 實戰案例五：Multi-Agent Code Review](#49-實戰案例五multi-agent-code-review)
  - [49.1 情境](#491-情境)
  - [49.2 步驟一：啟動審查](#492-步驟一啟動審查)
  - [49.3 步驟二：彙整](#493-步驟二彙整)
  - [49.4 步驟三：人工核准](#494-步驟三人工核准)
  - [49.5 小結](#495-小結)
- [50. 常用 Prompt Library](#50-常用-prompt-library)
- [51. Prime Agent Prompt Engineering](#51-prime-agent-prompt-engineering)
  - [51.1 標準 Prompt 結構](#511-標準-prompt-結構)
  - [51.2 範例](#512-範例)
  - [51.3 實務提醒](#513-實務提醒)
- [52. Agent Task Design](#52-agent-task-design)
  - [52.1 Bad Task vs Good Task](#521-bad-task-vs-good-task)
  - [52.2 為什麼 Bad Task 會出問題](#522-為什麼-bad-task-會出問題)
  - [52.3 任務拆解原則](#523-任務拆解原則)
- [53. Context Engineering](#53-context-engineering)
  - [53.1 核心概念](#531-核心概念)
  - [53.2 為什麼 RLM 能降低 Token 消耗](#532-為什麼-rlm-能降低-token-消耗)
  - [53.3 企業實務原則](#533-企業實務原則)
- [54. RLM Programming Tutorial](#54-rlm-programming-tutorial)
  - [54.1 第一步：基本 Python 執行](#541-第一步基本-python-執行)
  - [54.2 第二步：使用標準函式庫](#542-第二步使用標準函式庫)
  - [54.3 第三步：讀取並處理專案檔案](#543-第三步讀取並處理專案檔案)
  - [54.4 第四步：呼叫 `rlm()` 產生子 Agent](#544-第四步呼叫-rlm-產生子-agent)
  - [54.5 第五步：跨 Agent 通訊](#545-第五步跨-agent-通訊)
  - [54.6 第六步：接觸 Continual Harness（`/refine`，官方推薦入口）](#546-第六步接觸-continual-harnessrefine官方推薦入口)
  - [54.7 完整 Multi-Agent Workflow 範例](#547-完整-multi-agent-workflow-範例)
- [55. Architecture Decision Records](#55-architecture-decision-records)
  - [55.1 Prime Agent 專用 ADR 清單](#551-prime-agent-專用-adr-清單)
  - [55.2 ADR 範本](#552-adr-範本)
- [56. Enterprise Reference Architecture](#56-enterprise-reference-architecture)
  - [56.1 最終企業架構](#561-最終企業架構)
  - [56.2 架構層與治理層的對應](#562-架構層與治理層的對應)
- [57. 企業導入 Roadmap](#57-企業導入-roadmap)
  - [57.1 時間軸](#571-時間軸)
  - [57.2 各階段規劃](#572-各階段規劃)
- [58. 常見錯誤與不適合的使用情境](#58-常見錯誤與不適合的使用情境)
  - [58.1 Prime Agent 不適合做什麼（完整版，呼應第 1.7 節）](#581-prime-agent-不適合做什麼完整版呼應第-17-節)
  - [58.2 常見錯誤清單](#582-常見錯誤清單)
- [59. 最佳實務](#59-最佳實務)
  - [59.1 十大企業導入原則（總綱）](#591-十大企業導入原則總綱)
  - [59.2 五十條最佳實務（依十大原則分類）](#592-五十條最佳實務依十大原則分類)
- [60. Final Checklist](#60-final-checklist)
  - [60.1 Environment](#601-environment)
  - [60.2 Project](#602-project)
  - [60.3 Agent](#603-agent)
  - [60.4 Security](#604-security)
  - [60.5 Production](#605-production)
- [Appendix A：CLI Reference](#appendix-acli-reference)
- [Appendix B：Python／RLM Reference](#appendix-bpythonrlm-reference)
- [Appendix C：Prompt Library](#appendix-cprompt-library)
- [Appendix D：Skill Library](#appendix-dskill-library)
- [Appendix E：Troubleshooting 速查](#appendix-etroubleshooting-速查)
- [Appendix F：Security Checklist](#appendix-fsecurity-checklist)
- [Appendix G：Enterprise Checklist](#appendix-genterprise-checklist)
- [Appendix H：Glossary](#appendix-hglossary)
- [Appendix I：Reference Links](#appendix-ireference-links)
- [結語](#結語)

<!-- TOC-AUTO-END -->

---

## 1. Prime Agent 是什麼

### 1.1 Prime Agent 的定位

根據 [GitHub 官方 README](https://github.com/PrimeIntellect-ai/prime-agent) 的自我描述：

> "Prime Agent is an open-source coding and research agent for general and long-running work."（Prime Agent 是一個開源的、適用於一般任務與長時間執行任務的編碼與研究 Agent。）

Prime Intellect 官方將自己定位為 **"a self-improving agent harness built around RLMs and the Continual Harness"**（一個圍繞 RLM 與 Continual Harness 打造的自我改進型 Agent Harness）。它建構在兩個核心抽象之上：

- **Recursive Language Model（RLM）**：把 context 當成變數、把子 Agent 呼叫當成 REPL 裡的函式呼叫（第 2 章詳述）
- **Continual Harness**：把 Agent 的 Prompt、Skills、Memory、Sub-agent 視為可以 CRUD 的持久狀態（第 3 章詳述）

🟢 **官方功能**：Prime Agent 採 **MIT License** 開源，目前穩定版本為 **v0.7.4**（2026-08-19 發布）。

### 1.2 Prime Agent 不是什麼

Prime Agent 不是：

- ❌ 單純的 Chatbot
- ❌ Coding Assistant（如 IDE 內建自動完成）
- ❌ IDE Plugin
- ❌ Foundation Model / LLM 本身（它是外接多家 LLM Provider 的 Harness，見第 9 章）
- ❌ API Gateway

而是一個「**以 RLM 與 Continual Harness 為核心的自我改進型 Coding／Research Agent Harness／Runtime**」，設計上經歷了以下演進層次：

```mermaid
flowchart TD
    L1[LLM] --> L2[Agent]
    L2 --> L3[Agent Harness]
    L3 --> L4[RLM Runtime]
    L4 --> L5["Persistent IPython"]
    L5 --> L6[Sub-Agent]
    L6 --> L7[Continual Harness]
    L7 --> L8[Long-running Autonomous Workflow]
```

### 1.3 與 pi 的血緣關係（🔴 重要背景）

🔴 **注意**：Prime Agent **是 [`earendil-works/pi`](https://github.com/earendil-works/pi)（本目錄下另有《Pi Code Agent 教學手冊.md》介紹此專案）的 Hard Fork**。查證發現：

- Prime Agent 內部 npm 套件名稱仍是 `@earendil-works/pi-coding-agent`
- 大量 CLI 指令、Session 機制、Skills 標準、Provider 清單與 pi 高度重疊
- Prime Agent 相對於 pi 的**核心差異化能力**是：RLM 程式化 Context 操作、Continual Harness 自我演化機制、`/refine` 自我改進指令、以及官方宣稱的 ARC-AGI-3 benchmark 成果

若團隊已經導入 pi，可將本手冊視為「**pi + RLM + Continual Harness 進階擴充手冊**」來閱讀；若尚未使用任一工具，本手冊仍可作為獨立完整入門教材。

### 1.4 為什麼需要新的 Agent Harness

🔵 **企業建議（本手冊觀點）**：傳統「Tool Calling 迴圈」式 Coding Agent（User → LLM → Tool → Result → LLM）在企業導入時常見以下限制：

| 限制 | 說明 |
|------|------|
| **Context Window 問題** | 巨大 Legacy 專案、長 log、長 diff 難以一次塞進 context |
| **Static Prompt 問題** | Prompt 多半寫死在設定檔中，難以隨任務演化 |
| **Static Skill 問題** | Skill 集合固定，Agent 無法自行新增／調整能力描述 |
| **Static Memory 問題** | Memory（若有）通常需要人工預先寫入，Agent 無法自主沉澱經驗 |
| **Static Sub-agent 問題** | 子 Agent 分工方式需要人工預先設計，難以依任務動態調整 |

Prime Agent 官方部落格文章對此的立場是：*"Modern harness designs were built around the capabilities of earlier generations of models"*，並主張 *"harnesses should instead extrapolate on current model capabilities toward the next frontier of reasoning patterns."*（Harness 的設計應該隨模型能力演進，而不是停留在舊世代模型的假設上。）

### 1.5 Prime Agent 的設計哲學：RLM + Continual Harness + Persistent Runtime

Prime Agent 的核心設計哲學可歸納為四個支柱：

1. **RLM（第 2 章）**：Context 與 Prompt 都是 Python REPL 中的變數，可被程式化檢視、轉換、切片
2. **Continual Harness（第 3 章）**：Harness 自身狀態（Prompt／Skills／Memory／Sub-agent）可被 Agent 自行 CRUD
3. **Persistent Runtime（第 4、5 章）**：Daemon／Worker／Kernel 架構讓 Session 可在終端機關閉後持續執行
4. **Long-running Agent（第 19 章）**：架構上天生適合 Overnight／Weekend 等長時間任務

### 1.6 傳統 Agent vs Prime Agent

```mermaid
flowchart LR
    subgraph 傳統["傳統 Tool-Calling Agent"]
        A1[User] --> A2[LLM]
        A2 --> A3[Tool 呼叫]
        A3 --> A4[Tool 結果]
        A4 --> A2
    end

    subgraph PA["Prime Agent（RLM 模式）"]
        B1[LLM] --> B2["Persistent IPython REPL"]
        B2 --> B3[檢視/操作 Context 變數]
        B2 --> B4["rlm() 呼叫子 Agent"]
        B2 --> B5["agent_message 跨 Agent 通訊"]
        B4 --> B6[Continual Harness]
        B5 --> B6
        B6 --> B1
    end
```

| 面向 | 傳統 Tool-Calling Agent | Prime Agent（RLM 模式） |
|------|--------------------------|--------------------------|
| Context 處理 | 整段塞進 Prompt，受 Context Window 限制 | 🟢 Context 可作為 Python 變數被程式化檢視／切片／轉換 |
| 子任務分派 | 通常靠固定的 Tool Schema | 🟢 `rlm()` 在 REPL 內動態 spawn 子 Agent |
| 狀態持久化 | 多半只在單一 Session 內有效 | 🟢 Session 以 JSONL 持久化，可 `attach`／`resume`（第 6 章） |
| 自我改進 | 無標準機制 | 🟢 `/refine` 對 Continual Harness 做 CRUD（第 3、17 章） |
| 執行環境安全性 | 依實作而異 | 🔴 官方明文：Worker 以使用者 OS 權限執行，**非 security sandbox**（第 30 章） |

與其他工具的定性比較請見獨立的第 36 章（避免與本章重疊）。

### 1.7 Prime Agent 不適合做什麼（先預告，第 58 章有完整版）

必須客觀認知 Prime Agent 的使用邊界：

- ❌ 不應直接接 production 環境執行
- ❌ 不應直接操作 production 資料庫
- ❌ 不應無限制使用 Autonomous Mode（見第 18 章）
- ❌ 不應使用未經審查的第三方 Skill／MCP Server
- ❌ 不應把 ARC-AGI-3 等 benchmark 成績當成企業品質保證（見第 1.8 節）
- ❌ 不應完全取代 Architect／Developer／QA／Security 的角色判斷

### 1.8 ARC-AGI-3 Benchmark（官方宣稱，需正確理解限制）

🟢 **官方功能（Prime Intellect 官方報告的結果）**：根據 [primeintellect.ai/blog/prime-agent](https://www.primeintellect.ai/blog/prime-agent)（2026-08-05 發布）原文：

> "Our best results use Opus 5 in Prime Agent to achieve **95.5% RHAE Best@1**, which surpasses the ARC reported human expert baseline of **95.4%**. Across three runs, we find that Prime Agent consistently performs well **[95.0, 95.2, 95.5]** and **99.97% Best@3** with all **183/183 levels** complete."

其中 **RHAE（Relative Human Action Efficiency）** 是 ARC Prize 官方定義的評分方式（見 [docs.arcprize.org/methodology](https://docs.arcprize.org/methodology)），概念為：以「執行動作數最少的中位數人類玩家」為基準，比較 Agent 完成同一關卡所用的動作數。

🔴 **注意 — 解讀這組數字時務必一併理解以下限制**：

1. **這是 Prime Intellect 自行公布的結果**，查證當下未見獨立第三方複現。
2. **未出現在 ARC Prize 官方 Verified Leaderboard**；ARC-AGI Community Leaderboard 上雖有一筆「Add Prime Agent submission」的提交 PR（#46），但查證當下**仍是 open、尚未 merge**。
3. Community Leaderboard 現有分數（如 Tycho 100%、Retrodict 99.9%、baseline1 99%）**高於** Prime Agent 官方公布的 95.5%。
4. 「95.4% ARC reported human expert baseline」這個確切數字，查證時**找不到 ARC Prize 官方文件中逐字對應的原始出處**，僅確認是 Prime Intellect 自己在文章中的引用敘述。
5. 有二手來源（未經一手查證）指出 **Opus 5 裸模型**（不搭配 Prime Agent harness）在 ARC-AGI-3 官方榜上僅約 30% 左右 —— 若此數字屬實，代表 95.5% 這個分數主要來自 **Harness 工程**而非模型本身。此點請視為「未獨立驗證的二手資訊」。

**企業使用上的正確認知**：ARC-AGI-3 是一個抽象推理／互動遊戲類 benchmark，衡量的是特定型態的推理與規劃能力，**與企業實際 Software Engineering 工作（大型系統理解、Legacy 相依分析、跨系統整合除錯等）的能力沒有直接對應關係**。不應把這組 benchmark 數字當成「企業導入品質保證」。

> **實務案例**：某企業 AI 導入評估會議上，若有人以「Prime Agent 已經打敗 95.4% 的人類專家」作為推動導入的理由，正確的回應方式是：先說明這是特定遊戲類 benchmark 下的官方自報數字、尚未經第三方驗證，再回到「這個工具在我們的 Legacy Java 系統分析、Spring Boot 升級等實際場景表現如何」這個更貼近企業需求的問題上（見第 20、22、46、47 章）。

### 1.9 Long-Context Benchmark 結果（與企業場景較貼近的第二組官方數據）

🟢 **官方功能（Prime Intellect 官方報告的結果，直接查證官方部落格原始頁面資料）**：除了第 1.8 節的 ARC-AGI-3 之外，同一篇官方部落格文章還公布了一組**長 Context 推理／編碼 Benchmark** 的比較結果，性質上比 ARC-AGI-3 更接近企業實際會遇到的「大量文件／長程式碼庫理解」情境。官方比較了 Prime Agent 與 **Pi-mono**（第 1.3 節提及的血緣專案 `pi` 的多 Agent 模式）、**Claude Code**、**Codex** 三個 Harness，各自搭配 GLM-5.2（開源權重模型）、Opus 5、GPT-5.6 Sol 三種模型：

| Benchmark（類型） | Prime Agent（GLM-5.2） | Pi-mono（GLM-5.2） | Prime Agent（Opus 5） | Claude Code（Opus 5） | Prime Agent（GPT-5.6 Sol） | Codex（GPT-5.6 Sol） |
|------|------|------|------|------|------|------|
| OOLONG（yahoo, 128k；長 Context） | **0.700** | 0.420 | 0.900 | **0.920** | **0.940** | 0.500 |
| OOLONG-Pairs（長輸出） | **0.874** | 0.556 | **0.929** | 0.922 | **0.911** | 0.895 |
| OBLIQ-Bench（數學；長排序 ndcg@10） | **0.669** | 0.635 | **0.802** | 0.795 | 0.612 | **0.646** |
| LongBenchPro（英文；長理解） | **0.777** | 0.768 | **0.804** | 0.790 | **0.794** | 0.790 |
| LongBenchv2（專家標註長任務） | 0.680 | **0.696** | 0.744 | **0.746** | **0.714** | 0.704 |
| ManyIH Coding（長指令） | **0.424** | 0.386 | **0.536** | 0.522 | **0.499** | 0.454 |
| ManyIH IF（長指令） | **0.209** | 0.164 | **0.225** | 0.175 | 0.216 | **0.232** |
| LongCot-Mini（長推理） | **0.638** | 0.613 | **0.722** | 0.558 | 0.671 | **0.681** |
| EmulatorBench（長編碼） | **0.208** | 0.000 | 0.047\* | 0.062\* | **0.275** | 0.228 |

（粗體為官方原表標示的較高分數；`*` 為官方原表本身標註的註記符號，查證當下未在頁面上找到對應的註腳說明文字，本手冊如實保留原始標示，不代為臆測其含義。）

**逐列統計結果**（本手冊依上表自行加總，非官方直接聲明的加總數字）：搭配開源權重 GLM-5.2 時，Prime Agent 在 9 項中的 8 項優於 Pi-mono（唯一落後的是 LongBenchv2）；搭配 Opus 5 時，Prime Agent 在 9 項中的 6 項優於 Claude Code（落後 OOLONG、LongBenchv2，EmulatorBench 兩者皆非粗體、數字非常接近）。

🟢 **官方方法論說明（逐字確認）**：官方原文指出測試方法為 *"We offload the main context in each harness to a file in memory to start"*，且 *"for Prime-Agent and Pi-mono (with sub-agents), we choose an open-weights model in GLM-5.2"*（其餘 Harness 使用各自綁定的閉源模型）。

🔴 **注意 — 與第 1.8 節相同的解讀限制同樣適用**：

1. 這仍是 **Prime Intellect 官方自行公布、自行設計題組與比較方式**的結果，查證當下**未見獨立第三方複現**。
2. 官方原文明確承認：*"currently no model has been trained around Prime Agent or its core feature set"*（目前沒有任何模型是針對 Prime Agent 或其核心特性訓練的）——換言之，**這組數字反映的是「Harness 設計」在既有模型上的效果，而非「Prime Agent 訓練了更強的模型」**；第 3 章「Continual Harness」的「自我改進」，改的是 Harness 狀態（Prompt／Skills／Memory／Sub-agent），**不是模型權重本身**，企業內部溝通時應避免把「Self-improving」誤解為「模型會自動變聰明」。
3. 這組數字**比 ARC-AGI-3 更接近企業實際場景**（長文件理解、長程式碼庫、長推理鏈），但仍是特定題組下的結果，不能直接外推到任意企業自有系統的表現，實際導入前仍應以第 45–49 章的實戰案例方式在自己的專案上驗證。

---

## 2. Prime Agent 核心概念（RLM）

### 2.1 概念出處

🔴 **注意（重要出處修正）**：RLM **並非 Prime Intellect 自行發明的研究**，而是源自 **MIT CSAIL** 的論文：

> **《Recursive Language Models》** — Alex L. Zhang, Tim Kraska, Omar Khattab，arXiv:2512.24601（v1 於 2025-12-31 提出，最新版 2026-05-11）

論文摘要重點：RLM 讓模型透過持久化的 Python REPL 把輸入當成變數來檢視／轉換，並可從 REPL 內遞迴呼叫 sub-LLM 處理片段，據論文所述可讓有效處理的輸入長度達到原生 Context Window 的**約 100 倍**，且在多項任務上相較同類方法有 26%–130% 的提升。

Prime Intellect 在自家部落格文章 [primeintellect.ai/blog/rlm](https://www.primeintellect.ai/blog/rlm)（2026-01-01 發布，標題《Recursive Language Models: the paradigm of 2026》）中引用此論文，並將 RLM 定位為 *"the simplest, most flexible method for context folding"*（目前最簡單、最有彈性的 context folding 方法）。Prime Agent 則是**把這個概念工程化實作**進產品中的具體案例。

### 2.2 傳統 Agent vs RLM：兩種思維方式

**傳統 Agent 迴圈**：

```text
User → LLM → Tool 呼叫 → Tool 結果 → LLM → …
```

**RLM 思維**：

```text
LLM → 持久化 Python/IPython REPL
     → 檢視 context（把大量資料當變數，而非全部塞進 Prompt）
     → 操作／轉換資料（篩選、切片、彙總）
     → 呼叫函式（一般工具）
     → 呼叫 rlm() 動態 spawn 子 Agent 處理特定片段
     → 收集子 Agent 結果
     → 繼續推理
```

🟢 **官方功能**：Prime Intellect 官方明確指出，Prime Agent 可以「透過程式化函數直接處理資料，而不是把所有資料都轉成 token 後交給模型閱讀」——這正是 RLM 能大幅降低巨量資料處理時 token 消耗的原因（延伸討論見第 53 章 Context Engineering）。

### 2.3 RLM 的實際 API（原始碼與文件逐字確認）

以下 API 皆逐字確認於 `packages/coding-agent/docs/rlm.md` 與 `docs/rlm-runtime.md`：

> 🔴 **注意**：以下 API 需以目前 Prime Agent 官方文件與原始碼為準；次版本間可能調整簽名或行為。

#### 2.3.1 `rlm()` — 動態產生子 Agent

```python
# 🟢 官方功能：於 Prime Agent 的持久化 IPython Kernel 中執行
handle = await rlm("分析 src/main/java/com/example/order 底下所有類別的相依關係", name="dependency-scan")

print(handle.rlm_child_id)   # 子 Agent 的唯一識別碼
print(handle.name)           # "dependency-scan"
print(handle.session_dir)    # 子 Agent 的 Session 目錄
print(handle.model)          # 子 Agent 實際使用的模型
```

🔴 **注意（修正常見誤解）**：`rlm(...)` **只會立即回傳一個「受理控制代碼」（`RLMSpawnHandle`，admission handle），並不會直接回傳子 Agent 的最終答案**。子 Agent 是背景執行的，若要取得結果，需透過 `agent_message`（跨 Agent 通訊，見下）或後續查詢子 Agent 的 Session 狀態來取得。這與許多人直覺想像的「呼叫函式、同步拿到回傳值」不同，設計上更接近「派工單」而非「同步呼叫」。

🟢 **官方功能（`docs/rlm-runtime.md` 逐字確認）**：`rlm(...)` 是 `rlm.run(...)` 的簡寫，兩者等價；完整支援的關鍵字參數只有以下三個，傳入未定義的參數會直接失敗而不是被靜默忽略：

| 參數 | 說明 |
|------|------|
| `name` | 子 Agent 的唯一可讀識別名稱 |
| `model` | 由 `rlm.find_models()` 取得的精確 `provider/model` 選擇器，指定子 Agent 使用的模型（可與父層不同） |
| `thinking` | 子 Agent 的顯式 Reasoning Level（`off`／`low`／`medium`／`high`／`ultra`，須為所選模型支援的等級；未指定時預設繼承父層等級，並依子 Agent 模型能力自動下修） |

```python
# 🟢 官方功能（v0.7.4 新增）：指定子 Agent 使用不同模型與較低的 Reasoning Level，
# 適合大量平行、單純的分析型子任務，藉此降低成本與延遲
handle = await rlm(
    "掃描 legacy/ 目錄下所有 pom.xml，列出目前使用的 Spring Boot 版本",
    name="scan-poms",
    model="anthropic/claude-haiku-4-5",
    thinking="low",
)
```

#### 2.3.2 管理子 Agent

```python
# 🟢 官方功能
children = await rlm.list_subagents()   # 列出目前父層 Agent 已註冊的子 Agent
await rlm.delete_subagent(handle)       # 刪除／終止指定子 Agent
```

#### 2.3.3 `agent_message` — Agent 對 Agent（A2A）通訊

```python
# 🟢 官方功能：簽名已於原始碼與文件逐字確認
await agent_message.send(
    message="請針對 OrderService 的交易邊界重新檢查一次",
    receiver_role="child",       # "parent" | "child" | "sibling" | "all"
    receiver_name="dependency-scan",
    mode="steer",                # "auto" | "steer" | "follow_up"
)

agents = await agent_message.list_agents()   # 列出目前可通訊的 Agent 清單
```

- `receiver_role`：指定訊息要送給父層、子層、手足層還是全部 Agent
- `mode="steer"`：即時「導引」正在執行的子 Agent（介入其思考方向）
- `mode="follow_up"`：等子 Agent 目前動作完成後再處理這則訊息
- `mode="auto"`：由 Runtime 決定送達時機

#### 2.3.4 一個完整的最小範例

```python
# 🟢 官方功能 + 🔵 企業建議的組合寫法
# 情境：分析一個 Legacy Spring Boot 專案的三個模組，各自派一個子 Agent 平行分析

modules = ["order-service", "payment-service", "inventory-service"]
handles = []

for m in modules:
    h = await rlm(
        f"分析 {m} 模組：找出對外 REST API、資料庫存取方式、與其他模組的相依關係，"
        f"輸出成結構化 Markdown 表格",
        name=f"analyze-{m}",
    )
    handles.append(h)

# 之後可用 agent_message 詢問各子 Agent 進度，或直接查看各自 session_dir 內的輸出
for h in handles:
    print(f"{h.name}: session_dir={h.session_dir}")
```

**為什麼 Agent 要這樣做**：三個模組彼此獨立，讓每個子 Agent 各自在自己的 Context 中深入分析，比讓單一 Agent 依序把三個模組的原始碼都塞進同一個 Context 更省 token、也更不容易因為 Context 過長而遺漏細節。

**實務用途**：這個模式特別適合第 20 章的 Legacy Reverse Engineering 與第 22 章的 Framework Upgrade 場景——把大型專案拆成多個獨立子任務平行分析，再由父層 Agent 彙整結論。完整由淺入深的 RLM 程式化教學，見第 54 章。

### 2.4 小結與注意事項

- 🟢 RLM 是 Prime Agent 的核心執行模型，讓 Context、Prompt 都可被當成程式變數操作
- 🔴 `rlm()` 是非同步派工，不是同步取得答案的函式呼叫 —— 設計 Prompt／Skill 時務必考慮這個特性
- 🔵 **企業建議**：子 Agent 數量沒有官方文件明訂上限，但企業導入時應自行訂出「單一父任務最多可 spawn 幾個子 Agent」的治理規則，避免失控的並行擴散（見第 14.4 節、第 38 章）

---

## 3. Continual Harness

### 3.1 概念出處

🔴 **注意（重要出處修正）**：Continual Harness 同樣**不是 Prime Intellect 自行發明的概念**，而是源自 **Princeton 大學 / ARISE Foundation / Google DeepMind** 團隊的論文：

> **《Continual Harness: Online Adaptation for Self-Improving Foundation Agents》** — Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli，arXiv:2605.09998（2026-05-11 提交）

查證時發現一個值得說明的細節：這篇論文**完全沒有提到 Prime Intellect 或 Prime Agent**，其研究脈絡源自「Gemini Plays Pokémon」的 Harness 演化實驗；同時，Prime Agent 在 GitHub 上向 ARC Prize Community Leaderboard 提交結果的 PR（#46）作者正是這篇論文的第一作者 Seth Karten，顯示兩者之間存在直接的人員／技術往來，但 Continual Harness 本身仍應正確歸屬為學術界的研究成果，Prime Agent 是**採用並工程化實作**這個概念的產品之一。

### 3.2 核心定義：H = Prompt + Sub-agents + Skills + Memory

論文將 Harness 的狀態形式化為 **H = (ρ, G, K, M)**（Prompt、Sub-agents、Skills、Memory）。Prime Agent 官方部落格採用同一套框架，將 Continual Harness 定義為：

> 把 Harness 自身的狀態——抽象化為它的 **Prompt、Skills、Memory、Sub-agents**——視為 Agent 可以自行 **Create、Read、Update、Delete（CRUD）** 的對象，而不是寫死在設定檔裡的靜態內容。

```mermaid
flowchart TD
    H["Continual Harness 狀態 H"] --> P[Prompt Notes]
    H --> S[Skills]
    H --> M[Memory]
    H --> A[Sub-agent 規格]

    Task[任務執行過程] -->|觀察成敗| Refine["/refine 指令"]
    Refine -->|CRUD 提案| H
    Refine -->|保留快照| Snapshot[Snapshot]
    Snapshot -->|需要時| Rollback[Rollback]
```

### 3.3 `/refine`：CRUD 的官方入口

🟢 **官方功能**：`/refine [instructions]` 是官方文件確認的真實指令，作用是**檢視當前任務的執行軌跡（trajectory）**，並對 Continual Harness 狀態提出小幅度的 CRUD 修改建議。關鍵限制（官方文件原文精神）：

- **絕不修改 immutable 的 base system prompt** —— 只調整 Harness 層的狀態（Prompt Notes、Skills、Memory、Sub-agent 規格）
- 每次調整都會**記錄快照（Snapshot）**，支援之後 Rollback

```bash
# 🟢 官方功能：互動模式下輸入
/refine 這次任務中，我發現每次分析 Oracle Stored Procedure 都要重新解釋一次命名慣例，
請把這個慣例記錄下來，供之後任務參考
```

執行後，Agent 會根據這次任務的觀察，提出「要不要新增一筆 Memory／Skill 描述」之類的具體建議，經確認後寫入 Harness 狀態。`/refine` 的完整企業實務流程見第 17 章。

### 3.4 `rlm.harness`：原始碼中存在、但非官方公開介紹的內部介面

🔴 **注意（重要落差）**：查證原始碼（`prime-agent-runtime/src/rlm/harness.py`）確認存在 `HarnessState` 類別，其中包含 `create_memory`、`update_memory`、`delete_memory`、`create_prompt_note`、`create_skill`、`create_subagent`、`record_refinement` 等方法（真實存在於程式碼中）：

```python
# 🔴 注意：以下方法確認存在於原始碼，但官方文件並未把它們當作
# 使用者／Skill 作者應該直接呼叫的公開 API 來介紹與示範。
# 官方唯一有文件、有範例、被推薦的介面是 /refine 指令本身。
rlm.harness.create_memory(...)
rlm.harness.create_skill(...)
rlm.harness.create_subagent(...)
```

Harness 狀態實際持久化位置：

- 專案層級：Session artifact 目錄下的 `harness/harness_state.json`
- 全域層級：`~/.prime/agent/harness/`

🔵 **企業建議**：由於 `rlm.harness.*` 屬於「程式碼存在但非官方推薦公開呼叫」的灰色地帶，企業內部若要撰寫自訂 Skill 直接操作 Harness 狀態，建議：

1. 優先透過 `/refine` 這個有文件、有 Snapshot／Rollback 保障的官方入口
2. 若確實需要繞過 `/refine` 直接呼叫 `rlm.harness.*`，應在內部技術文件中明確標註「使用未公開 API，版本升級時需重新驗證相容性」
3. 對 Harness 狀態的任何自動化修改，都應該像第 29 章的 Git 規則一樣，保留可回溯的紀錄

### 3.5 Session / Global / Local 狀態層級

| 層級 | 範圍 | 典型內容 |
|------|------|----------|
| Session 狀態 | 單一 Session 存續期間 | 當次任務的暫時性 Context、子 Agent handle |
| Harness（Local）狀態 | 單一專案 | 該專案專屬的 Memory、Skill、Sub-agent 規格 |
| Harness（Global）狀態 | 跨專案（`~/.prime/agent/`） | 使用者個人慣用的 Skill、共用 Memory |

> **實務案例**：一位資深工程師在專案 A 中用 `/refine` 記錄了「本公司 Commit Message 一律要有 JIRA 單號」這個慣例。若這是跨專案通用的團隊規範，應評估是否該手動搬移到 Global 層級（而非讓每個專案各自累積一份重複的 Local Memory），否則容易出現「不同專案的 Harness 狀態互相衝突」的治理問題（延伸見第 16 章 Memory 設計）。

---

## 4. Prime Agent 整體架構

### 4.1 架構總覽

```mermaid
flowchart TD
    User[使用者] --> CLI["prime-agent CLI"]
    CLI --> Daemon[Background Daemon]
    Daemon --> Worker[Worker Process]
    Worker --> Kernel["IPython Kernel（持久化）"]
    Kernel --> RLM[RLM 執行層]
    Kernel --> Skills[Skills]
    RLM --> SubAgent[Sub-agent]
    RLM --> Harness[Continual Harness]
    Harness --> Memory[Memory]
    Harness --> PromptNotes[Prompt Notes]
    Harness --> SkillSpecs[Skill 規格]
    Harness --> SubagentSpecs[Sub-agent 規格]
    SubAgent -->|agent_message| SubAgent
    Worker --> Session["Session（JSONL 持久化）"]
    Worker --> FS[檔案系統 / Shell / Git]
```

🟢 **官方功能**：此架構圖對應官方 `docs/architecture.md`、`docs/long-running-agents.md`、`docs/rlm-runtime.md` 描述的元件關係：CLI 啟動後由背景 Daemon 管理 Worker 生命週期；每個 Worker 綁定一個持久化 IPython Kernel；Kernel 內執行 RLM 邏輯，可存取 Skills、發起 Sub-agent、讀寫 Continual Harness 狀態；所有動作都在 Session 中以 JSONL 記錄。

### 4.2 各元件說明

| 元件 | 說明 |
|------|------|
| **Host** | 執行 `prime-agent` CLI 的機器（開發者筆電或 CI Runner） |
| **Daemon** | 背景常駐行程，管理多個 Worker 的啟停與生命週期（第 5 章） |
| **Worker** | 實際執行任務的行程，綁定一個 IPython Kernel（第 5 章） |
| **Kernel** | 持久化 IPython 執行環境，狀態在多輪對話間保留 |
| **Session** | 一次任務的完整記錄，持久化為 JSONL，可 `attach`／`resume`（第 6 章） |
| **Harness State** | Continual Harness 的持久化狀態（第 3 章） |
| **Sub-agent** | 由 `rlm()` 動態產生的子 Agent，各自有獨立 Session（第 2、13 章） |
| **Skills** | 依 Agent Skills 標準定義的能力擴充（第 15 章） |
| **Provider** | LLM 供應商設定（第 9 章） |
| **MCP Integration** | 以 Python-backed Skill 型態接入的外部系統整合（第 27 章） |

### 4.3 為什麼這個架構適合長時間任務

正因為 Daemon／Worker／Kernel／Session 是分離且持久化的元件，Prime Agent 特別適合：

- Overnight（隔夜）批次分析任務
- Weekend Migration（週末進行的大型遷移）
- Large Refactoring（大型重構）
- Framework Upgrade（框架升級）
- Reverse Engineering（大型 Legacy 系統逆向分析）
- Large Codebase Analysis（超大型程式碼庫分析）

因為即使開發者的終端機關閉、筆電睡眠，背景 Daemon／Worker 仍可持續執行，之後再用 `prime-agent attach` 接回查看進度（第 6、19 章）。

### 4.4 架構層與後續章節對應

| 架構層 | 詳述章節 |
|--------|----------|
| RLM 執行層 | 第 2、54 章 |
| Continual Harness | 第 3、16、17 章 |
| Runtime／Process Model（Daemon/Worker/Kernel） | 第 5 章 |
| Session 持久化 | 第 6 章 |
| Skills | 第 15 章、附錄 D |
| Sub-agent／Multi-Agent | 第 13、14 章 |
| 安全邊界 | 第 30、31 章 |

---

## 5. Runtime 與 Process Model

### 5.1 Daemon／Worker／Kernel 三層模型

🟢 **官方功能**（`docs/long-running-agents.md`、`docs/rlm-runtime.md`）：Prime Agent 的執行模型分為三層：

- **Daemon**：背景常駐行程，負責管理多個 Worker 的生命週期（啟動、監控、回收）
- **Worker**：實際執行任務的行程，一個 Worker 綁定一個 IPython Kernel
- **Kernel**：持久化 IPython 執行環境，狀態在多輪對話間保留，直到 Session 結束或明確重置

🔴 **注意**：官方文件明確指出：*"Daemon workers are process-isolated for lifecycle and failure containment, not security-sandboxed. They normally run with the same operating-system permissions as the client."*（Daemon Worker 的行程隔離是為了生命週期管理與失敗控管，不是資安沙箱；它們通常以客戶端相同的作業系統權限執行。）完整安全討論見第 30 章。

### 5.2 Session 生命週期狀態

🔵 **企業建議（依官方 CLI 行為歸納的狀態描述）**：

| 狀態 | 說明 | 對應指令 |
|------|------|----------|
| Running | Session 正在執行任務 | `prime-agent agents` 可見 |
| Idle | Session 存在但目前無進行中任務 | `prime-agent agents` 可見 |
| Inactive／Saved | Session 已結束但記錄仍保留 | `prime-agent list --all` |
| Attach | 使用者接回一個 Running／Idle Session | `prime-agent attach <agent>` |
| Detach | 使用者離開但不終止 Session（關閉終端機即自然 Detach） | — |
| Resume | 從已儲存的 Session 記錄恢復互動 | `prime-agent -r/--resume` |

### 5.3 當機復原（Crash Recovery）

🔵 **企業建議**：由於 Session 以 JSONL 持久化，即使 Worker 行程意外終止（如系統重啟），Session 記錄本身不會遺失，可透過 `prime-agent list --all` 找回，再以 `--resume` 接續。但**進行中、尚未落盤的中間狀態**（如某次工具呼叫執行到一半）在 Worker crash 時可能遺失，因此：

- 高風險的 Autonomous Task，建議搭配第 18 章的 `--autonomous-gate` 確保每個階段都是可驗證的穩定點
- 定期以 `prime-agent status` 確認 Daemon／Worker 是否正常運作

### 5.4 Runtime 與後續章節的關係

Session 持久化的完整 CLI 操作見第 6 章；Long-running Agent 的心跳與排程機制見第 19 章；Runtime 的安全邊界見第 30、31 章。

---

## 6. Session Persistence

### 6.1 Session 的持久化機制

🟢 **官方功能**：每個 Session 的完整互動記錄以 **JSONL** 格式持久化儲存，搭配 Kernel 狀態，讓 Session 可以在終端機關閉後被重新接上（Attach）或恢復（Resume）。

### 6.2 常用 CLI 指令（原始碼逐字確認）

> 🔴 **注意**：以下所有指令與旗標皆已對照 `packages/coding-agent/docs/usage.md`、`docs/long-running-agents.md` 原始檔逐字確認，非推測內容。完整逐指令說明見附錄 A。

```bash
# 列出目前的 Session（互動瀏覽 Running/Idle/Saved 狀態）
prime-agent agents

# 列出所有 Session（含更詳細資訊）
prime-agent list --all

# 接回（Attach）一個背景執行中的 Agent Session
prime-agent attach <agent>

# 停止指定 Agent
prime-agent stop <agent>

# 重新命名 Session
prime-agent rename <agent> <name>

# 對背景 Agent 傳送一則新訊息（不需要先 attach）
prime-agent send <agent> <message>

# 排程管理（cron 或一次性排程）
prime-agent schedule list
prime-agent schedule add <agent> "<when>" -- "<prompt>"
prime-agent schedule cancel <schedule-id>

# 檢視整體狀態
prime-agent status

# 診斷環境問題（可自動修復部分問題）
prime-agent doctor
prime-agent doctor --fix

# 關閉背景 Daemon 與所有 Worker
prime-agent shutdown
prime-agent shutdown --force
```

啟動互動 Session 時常用的旗標：

```bash
prime-agent -c                    # --continue：接續最近一次 Session
prime-agent -r <path|id>          # --resume：恢復指定 Session
prime-agent --fork <path|id>      # 從既有 Session 分岔出一個新 Session（不影響原 Session）
prime-agent --no-session          # 不建立 Session 記錄（一次性用途）
prime-agent --session-dir <dir>   # 指定 Session 儲存目錄
```

| 指令／旗標 | 用途 | 使用時機 | 風險提醒 |
|------------|------|----------|----------|
| `agents` | 瀏覽所有 Session 狀態 | 每天開工時先確認有哪些背景任務還在跑 | — |
| `attach <agent>` | 接回背景 Session 即時查看 | 想確認長任務目前進度 | 🔴 接回後若直接輸入新指令，可能打斷原本的 Autonomous 流程，建議先觀察再決定是否介入 |
| `-r/--resume` | 恢復指定 Session 繼續互動 | 昨天沒做完的分析，今天想接著問 | — |
| `--fork` | 從既有 Session 分岔 | 想在不影響原 Session 的前提下嘗試不同方向 | — |
| `stop <agent>` | 停止 Agent | 任務已達成目標，或發現方向錯誤要喊停 | 🔴 停止前建議先 `attach` 確認目前狀態，避免中斷到一半的重要寫入操作 |
| `shutdown --force` | 強制關閉 Daemon 與所有 Worker | 環境異常需要整個重啟 | 🔴 會中斷所有背景 Session，執行前務必先用 `agents` 確認沒有正在跑的重要任務 |
| `doctor --fix` | 自動修復常見環境問題 | 安裝或執行異常時的第一步診斷 | 完整 Troubleshooting 見第 41 章 |

### 6.3 Session 生命週期時序

```mermaid
sequenceDiagram
    participant Dev as 開發者
    participant CLI as prime-agent CLI
    participant Daemon as Background Daemon
    participant Worker as Worker + Kernel
    participant Session as Session (JSONL)

    Dev->>CLI: prime-agent --autonomous "分析並升級 Spring Boot 3→4"
    CLI->>Daemon: 啟動任務
    Daemon->>Worker: 建立 Worker + Kernel
    Worker->>Session: 持續寫入 JSONL
    Dev->>Dev: 關閉終端機／筆電休眠
    Note over Worker: Daemon 持續在背景執行任務
    Dev->>CLI: （隔天）prime-agent agents
    CLI->>Daemon: 查詢 Session 清單
    Dev->>CLI: prime-agent attach <agent>
    CLI->>Worker: 接回 Session，顯示目前進度
```

### 6.4 為什麼企業要重視 Session Persistence

🔵 **企業建議**：對企業而言，Session Persistence 帶來的最大價值不是「方便」，而是**可稽核性**——每次任務的完整推理過程與工具呼叫都留在 JSONL 中，可作為：

- 事後追查 Agent 決策依據的稽核紀錄
- 團隊內部知識傳遞（資深工程師可以「重播」Agent 的分析過程教育新人）
- 出問題時的除錯依據（第 41 章 Troubleshooting 會用到）

> **注意事項**：Session JSONL 中可能包含專案原始碼片段、甚至 Agent 執行 Shell 指令時看到的環境變數輸出。企業導入時應將 Session 儲存目錄（預設或 `--session-dir` 指定的路徑）納入既有的資料存取控管範圍，比照原始碼倉庫的保密等級處理（詳見第 30 章安全模型）。

---

## 7. 安裝環境

### 7.1 系統需求

🟢 **官方功能**（逐字確認於 README／`docs/quickstart.md`／`packages/coding-agent/package.json`）：

- **作業系統**：官方安裝腳本原生支援 **Linux 與 macOS**
- **Node.js**：`>= 22.8.0`（`package.json` 的 `engines` 欄位明確要求）
- **Python／IPython**：官方文件**未列出明確的最低版本需求**——Kernel 執行環境會在首次使用時自動於 `~/.prime/agent/kernel-venv` 建立獨立虛擬環境並安裝必要套件（`ipykernel`、`prime-agent-runtime` 等），不需要使用者預先手動安裝特定版本的 Python

### 7.2 Linux 安裝

```bash
# 🟢 官方功能：安裝穩定版
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

- **用途**：下載並執行官方安裝腳本
- **語法**：`curl -fsSL <url> | sh`
- **參數**：`-f`（失敗時不輸出錯誤頁內容）、`-s`（靜默模式）、`-S`（靜默模式下仍顯示錯誤）、`-L`（跟隨重導向）
- **使用時機**：全新環境的第一次安裝
- **執行結果**：安裝執行檔至使用者本機路徑並加入 PATH
- **常見錯誤**：企業內網無法連外時會逾時失敗，見 7.4 節原始碼安裝替代方案

### 7.3 macOS 安裝

macOS 安裝方式與 Linux 完全相同（同一支安裝腳本，會自動偵測平台）：

```bash
# 🟢 官方功能
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

🔵 **企業建議**：macOS 上若透過 Homebrew 管理 Node.js，建議先確認版本符合 `>=22.8.0`：

```bash
brew install node@22
node --version
```

### 7.4 Beta 版與原始碼安裝

```bash
# 🟢 官方功能：安裝 main 分支的 Beta 版
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh -s -- beta
```

```bash
# 🟢 官方功能：從原始碼安裝（需 Node.js 22.8.0+）
git clone https://github.com/PrimeIntellect-ai/prime-agent
cd prime-agent
npm ci
./prime-agent.sh
```

🔵 **企業建議**：若企業內網無法直接存取 `app.primeintellect.ai` 的安裝腳本（常見於金融業／受管制網路環境），從原始碼安裝是較可控的替代方案——可先在允許存取外部套件庫的環境完成 `npm ci`，再將建置產物搬移到受限網路內的機器。

### 7.5 Windows 環境（🔴 注意：非原生支援，需要 bash）

🔴 **注意（重要修正）**：Prime Agent **沒有原生 Windows（cmd.exe／PowerShell）安裝腳本或執行路徑**。官方 `docs/windows.md` 明確指出：Prime Agent *"requires a bash shell on Windows"*，並依序偵測：

1. 使用者在設定中指定的自訂 bash 路徑
2. Git Bash（預設路徑 `C:\Program Files\Git\bin\bash.exe`）
3. PATH 上可找到的 `bash.exe`（Cygwin／MSYS2／WSL 均可）

官方文件建議 Windows 使用者安裝 **Git for Windows**（內含 Git Bash）作為最低需求。

🔵 **企業建議**：針對企業 Windows 開發機，建議依團隊需求在以下兩種路徑間擇一，兩者都符合官方「需要 bash」的硬性要求：

| 方案 | 適合情境 | 注意事項 |
|------|----------|----------|
| **Git Bash**（較輕量） | 只需要 Prime Agent 能找到 bash 執行 Shell 指令，其餘開發仍在 Windows 原生環境進行 | Git Bash 的 POSIX 相容性有限，複雜 Shell Pipeline 可能與 Linux 行為不完全一致 |
| **WSL2 + Ubuntu**（較完整） | 團隊本來就有 WSL2 開發習慣，或專案需要與正式環境（多為 Linux）行為一致 | 需要額外設定 WSL2、檔案系統跨界效能（`/mnt/c/...`）需留意 |

```bash
# 🔵 企業建議：WSL2 內的安裝方式與 Linux 完全相同
wsl --install -d Ubuntu
# 進入 WSL2 Ubuntu 後
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```

WSL2 環境下的前置需求（🔵 企業建議的標準清單，非 Prime Agent 官方專屬要求）：

- Git（`sudo apt install git`）
- SSH 金鑰與 GitHub 身分設定（若需要存取企業內部 Git 服務）
- 檔案權限：專案目錄建議放在 WSL2 檔案系統內（如 `~/projects/`）而非 `/mnt/c/...`，避免跨檔案系統效能問題
- 環境變數／API Key：透過 `~/.bashrc` 或專案層級的環境變數管理（第 9 章）

---

## 8. 安裝與驗證

### 8.1 首次啟動

```bash
# 🟢 官方功能
cd /path/to/your/project
prime-agent
```

首次啟動後，於互動介面輸入 `/login` 完成身分驗證（第 9 章）。

### 8.2 安裝後驗證指令

```bash
# 🟢 官方功能
prime-agent --help       # 顯示所有指令與旗標
prime-agent --version    # 顯示目前安裝版本（-v）
prime-agent status       # 顯示 Daemon／Worker 狀態
prime-agent doctor       # 診斷常見安裝／環境問題
```

| 指令 | 用途 | 常見錯誤 |
|------|------|----------|
| `prime-agent --help` | 確認 CLI 已正確安裝且可執行 | 找不到指令 → 檢查安裝腳本是否把執行檔加進 PATH |
| `prime-agent status` | 確認背景 Daemon 是否正常啟動 | Daemon 未啟動 → 嘗試 `prime-agent shutdown` 後重新執行任一指令觸發重啟 |
| `prime-agent doctor` | 檢查 Node.js 版本、Kernel venv、Provider 設定等常見問題 | 見第 41 章 Troubleshooting 完整章節 |

### 8.3 更新與移除

```bash
# 🟢 官方功能：更新到最新版本
prime-agent update
prime-agent update --force
```

- **用途**：`update` 檢查並套用最新版本；`--force` 強制重新安裝（即使版本號相同）
- **使用時機**：定期更新（見第 43 章升級策略）、或懷疑目前安裝已損毀時
- **常見錯誤**：企業網路限制外部連線時會更新失敗，處理方式同 7.4 節原始碼安裝

🔴 **注意**：官方文件未提供獨立的「解除安裝」子指令；移除方式為刪除安裝目錄與 `~/.prime/agent/` 設定/狀態目錄（🔵 企業建議：移除前先確認該目錄下沒有尚未備份的 Harness 狀態或 Session 記錄，見第 42 章維運）。

### 8.4 沒有獨立文件網站

🔴 **注意**：查證確認 Prime Agent **沒有獨立的文件網站**（未找到 `docs.primeintellect.ai` 等網址）。所有官方文件都在 GitHub repo 內 `packages/coding-agent/docs/*.md`，由 README 連結。企業內部若要建立離線文件鏡像，直接同步此目錄即可。

---

## 9. Provider 與 Model 設定

### 9.1 訂閱式登入（`/login`）

🟢 **官方功能**（逐字確認於 `docs/providers.md`）：Prime Agent 支援透過 `/login` 以既有訂閱身分登入，包含：

- Claude Pro / Max
- ChatGPT Plus / Pro（透過 Codex）
- GitHub Copilot

```bash
# 🟢 官方功能：互動模式下輸入
/login
```

### 9.2 API Key 環境變數（Provider 清單）

🟢 **官方功能**：以下 Provider 皆確認於官方 `docs/providers.md`，可透過環境變數設定 API Key：

| 類別 | Provider |
|------|----------|
| 主流模型 API | Anthropic、OpenAI、Google Gemini |
| 雲端代管 | Azure OpenAI、Amazon Bedrock、Google Vertex AI、Cloudflare AI Gateway、Cloudflare Workers AI |
| 其他模型供應商 | Prime Inference、DeepSeek、Mistral、Groq、Cerebras、xAI、OpenRouter、Vercel AI Gateway、ZAI、OpenCode Zen、OpenCode Go、Hugging Face、Fireworks、Kimi For Coding、MiniMax（含中國區變體）、Xiaomi MiMo（含區域變體） |

```bash
# 🔵 企業建議的環境變數管理方式（範例，實際變數名稱請以官方 docs/providers.md 為準）
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
```

### 9.3 本地／自架模型

🟢 **官方功能**：可透過 `models.json` 設定自訂 Provider 或本地模型（如 Ollama、LM Studio、vLLM 等 OpenAI 相容 API 服務）。

🔵 **企業建議（金融業／受管制產業特別適用）**：若合規要求「程式碼與資料不得離開企業內網」，本地模型是目前唯一能滿足此要求的路徑；但需注意本地開源模型在複雜推理與長任務規劃上的能力，與 Claude／GPT／Gemini 等旗艦模型仍有落差，建議先以非機敏的內部工具型任務（如產生測試骨架、簡單重構）驗證可行性，再逐步擴大使用範圍。金融業完整案例見第 32 章。

### 9.4 Provider / Model / Authentication 對照

| 驗證方式 | 涵蓋 Provider | 適合情境 |
|----------|----------------|----------|
| 訂閱登入（`/login`） | Claude Pro/Max、ChatGPT Plus/Pro、GitHub Copilot | 個人開發者、已有訂閱、想避免額外 API 帳單 |
| API Key（環境變數） | Anthropic、OpenAI、DeepSeek、Mistral、Groq 等一長串 | 團隊／CI 環境，需要可控的用量與計費 |
| 雲端代管帳號 | Azure OpenAI、Amazon Bedrock、Google Vertex AI | 企業已有雲端合約與資安治理框架 |
| 本地模型 | Ollama、LM Studio、vLLM（透過 `models.json`） | 高度合規要求、需要離線／內網運作 |

```bash
# 🟢 官方功能：啟動時指定 Provider 與 Model
prime-agent --provider anthropic --model claude-opus-5 "分析這個專案的整體架構"

# 🟢 官方功能：控制推理深度（thinking level）
prime-agent --thinking high "找出這段程式碼的併發問題"
```

`--thinking` 可用等級（🟢 官方功能，逐字確認）：`off | minimal | low | medium | high | xhigh | max`

> **實務案例**：企業內部若同時有「日常快速問答」與「大型 Framework Upgrade 規劃」兩種任務型態，建議在團隊內部 Wrapper Script 中依任務類型預設不同的 `--thinking` 等級與 `--model`，避免每個人各自摸索造成成本與品質不一致（延伸見第 40 章 Cost Management）。

---

## 10. 第一個 Prime Agent 專案

### 10.1 情境設定

本節以一個典型企業 Web Application 技術棧作為示範對象：

```text
前端：Vue 3 + TypeScript + Tailwind CSS + PrimeVue + Pinia
後端：Java 25 + Spring Boot 4.x + Maven 4.x
資料庫：PostgreSQL + Redis
API：REST + OpenAPI
測試：JUnit 5 + ArchUnit
```

這個技術棧會在第 11、45 章進一步展開為完整的開發工作流與實戰演練。

### 10.2 啟動與初次分析

```bash
cd my-webapp-project
prime-agent
```

```text
# 🔵 企業建議的第一個 Prompt（進入互動模式後輸入）
請分析目前這個專案：
1. 建立整體 Architecture Map（前端／後端／資料庫／外部整合）
2. 列出所有主要模組與彼此的相依關係
3. 找出目前的 Build 指令與 Test 指令（不要假設，直接檢查 pom.xml / package.json / CI 設定檔）
4. 摘要目前的程式碼風格慣例（命名、分層方式、例外處理模式）
5. 掃描是否有明顯的安全風險（過期相依套件、硬編碼的機密資訊、缺少輸入驗證的端點）
在完成分析前，不要修改任何檔案。
```

🔵 **企業建議**：刻意在 Prompt 最後加上「在完成分析前，不要修改任何檔案」，是呼應第 59 章「企業導入原則」中 **Human in the Loop** 與 **Reversible Change** 的具體做法——先讓 Agent 產出分析結果供人審閱，再決定是否授權它動手修改。

### 10.3 建立專案專屬的 Memory 與 Skill

分析完成後，可以進一步請 Agent 把分析結果沉澱為長期可用的資產：

```text
# 🔵 企業建議 Prompt
請把剛才分析出的「模組相依關係」與「Build/Test 指令」透過 /refine 記錄成這個專案的 Memory，
讓之後每次開啟這個專案都不用重新分析一次。
```

```bash
# 🟢 官方功能：實際指令
/refine 把剛才分析出的模組相依關係、Build/Test 指令記錄為這個專案的 Memory
```

### 10.4 建立第一個 Sub-agent 分工

```text
# 🔵 企業建議 Prompt：示範以 rlm() 拆分任務
針對 order-service、payment-service、inventory-service 三個模組，
分別用 rlm() 派出一個子 Agent 深入分析各自的資料庫存取層是否有 N+1 查詢問題，
完成後彙整成一份總表。
```

### 10.5 小結

| 步驟 | 目的 | 對應功能 |
|------|------|----------|
| 1. 整體分析 | 建立 Architecture Map | RLM 讀取／彙整專案結構（第 2 章） |
| 2. 找出 Build/Test 指令 | 避免 Agent 之後猜測指令 | Context 檢視 |
| 3. 掃描安全風險 | 建立初步風險意識 | 第 30 章安全模型 |
| 4. `/refine` 沉澱結果 | 避免每次重新分析 | Continual Harness（第 3、17 章） |
| 5. `rlm()` 平行分析 | 熟悉 Sub-agent 分工模式 | RLM（第 2 章）、Multi-Agent（第 13 章） |

這個「分析 → 沉澱 → 分工」的最小流程，會在第 45 章擴充為一個從零開始的完整 Vue + Spring Boot 實戰案例。

---

## 11. 使用 Prime Agent 開發 Web Application

### 11.1 完整 AI Software Development Workflow

🔵 **企業建議**：以下工作流建立在第 1–10 章已介紹的官方機制之上，是本手冊針對企業 Web Application 開發提出的標準流程：

```mermaid
flowchart TD
    Req[Requirement] --> Analysis[Analysis]
    Analysis --> Arch[Architecture]
    Arch --> Spec[Specification]
    Spec --> Task[Task Breakdown]
    Task --> Impl[Implementation]
    Impl --> UT[Unit Test]
    UT --> IT[Integration Test]
    IT --> Sec[Security Scan]
    Sec --> Review[Code Review]
    Review --> Perf[Performance Test]
    Perf --> Doc[Documentation]
    Doc --> Commit[Commit]
    Commit --> PR[Pull Request]
```

### 11.2 各階段 Prime Agent 的角色

| 階段 | Prime Agent 負責的工作 | 對應章節 |
|------|--------------------------|----------|
| Requirement | 協助釐清模糊需求、產出待確認的假設清單 | 第 12、51 章 |
| Analysis | RLM 讀取既有程式碼，建立 Architecture Map | 第 2、10 章 |
| Architecture | 提出候選架構、標記需人工決策的取捨點 | 第 13、55 章 |
| Specification | 依 Spec-Driven Development 模式產出規格 | 第 12 章 |
| Task Breakdown | 拆解為可獨立驗證的子任務 | 第 52 章 |
| Implementation | Frontend/Backend/Database Sub-agent 平行實作 | 第 13、14 章 |
| Unit/Integration Test | Test Agent 補齊測試 | 第 14 章 |
| Security Scan | Security Agent 依 OWASP 檢查 | 第 25、30 章 |
| Code Review | Reviewer Agent 彙整審查意見 | 第 25 章 |
| Performance Test | 產生測試腳本，基準線比較仍需人工把關 | 第 22.5 節 |
| Documentation | 產出變更摘要、更新技術文件 | — |
| Commit／PR | 遵循 Git 安全規則 | 第 29 章 |

### 11.3 企業 Web Application 技術棧整合案例

本手冊採用以下技術棧作為貫穿全書實戰案例的基礎（呼應第 10、45 章）：

```text
Frontend：Vue 3 / TypeScript / Tailwind CSS / PrimeVue / Pinia
Backend：Java 25 / Spring Boot 4.x / Spring Framework 7.x / Maven 4.x
Architecture：Clean Architecture / Hexagonal Architecture / Microservices
Database：Oracle / DB2 / PostgreSQL
Testing：JUnit 5 / ArchUnit / JMeter
Security：OWASP / SonarQube
Observability：OpenTelemetry / Prometheus / Grafana
CI/CD：Jenkins / GitHub Actions / GitLab
Container：Podman / Kubernetes
```

🔵 **企業建議**：Prime Agent 融入此技術棧的具體方式：

- **Frontend／Backend**：由第 14 章的 Frontend／Backend Sub-agent 負責，遵循既有的 Vue／Spring Boot 慣例（存放於 Memory，見第 16 章）
- **Database**：Database Sub-agent 需同時考量 Oracle／DB2／PostgreSQL 相容性（第 23 章 Database Migration）
- **Testing**：Test Agent 產生 JUnit 5／ArchUnit 測試，JMeter 效能測試腳本則由 Agent 產生、人工執行與判讀基準線
- **Security**：Security Agent 的檢查邏輯與既有 SonarQube／OWASP 規則對齊而非取代（第 25 章）
- **CI/CD**：透過第 28 章的 JSON／RPC Mode 整合進 Jenkins／GitHub Actions／GitLab Pipeline
- **Observability**：Prime Agent 本身不提供 Observability，但可協助產生 OpenTelemetry Instrumentation 程式碼

### 11.4 實務案例

> 某團隊導入初期，誤把 Prime Agent 當成「取代整個 SDLC」的工具，結果在 Requirement 階段就讓 Agent 自行假設需求細節並直接開始實作，導致返工。修正後的做法是：Requirement／Specification 階段人工主導、Agent 輔助釐清；Implementation／Test 階段才大量授權 Agent 自主執行，並搭配第 18 章的 Quality Gate。這個經驗呼應第 59 章「Human in the Loop」原則——AI 輔助開發流程中，人類負責的階段不應被跳過。

---

## 12. Prime Agent 與 Spec-Driven Development

### 12.1 為什麼要搭配 Spec-Driven Development

🔵 **企業建議**：Prime Agent 本身不內建 Spec-Driven Development 流程（官方文件未提及專屬的 Spec 機制），但其 RLM／Sub-agent／Continual Harness 能力，很適合搭配業界既有的 **spec-kit** 類方法論（規格先行、再交由 Agent 實作與驗證）。本目錄下另有《spec-kit使用教學.md》可搭配參考。

```mermaid
flowchart TD
    Req[Requirement] --> Spec[Specification]
    Spec --> Arch[Architecture]
    Arch --> Plan[Plan]
    Plan --> Tasks[Tasks]
    Tasks --> PA[Prime Agent 執行]
    PA --> Impl[Implementation]
    Impl --> Verify[Verification]
    Verify -->|不通過| Plan
```

### 12.2 各階段 Prompt Template（🔵 企業建議）

**Requirement Prompt**

```text
以下是使用者提出的需求描述：[貼上原始需求]。
請列出所有模糊或缺少細節的地方，以問題清單方式呈現，不要自行假設答案。
```

**Specification Prompt**

```text
根據已確認的需求（[貼上已確認內容]），產出結構化規格文件，包含：
- 功能範圍與非功能需求（效能、安全、可用性）
- API 介面定義（含 Request/Response Schema）
- 資料模型變更
- 明確排除的範圍（Out of Scope）
```

**Architecture Prompt**

```text
根據規格文件，提出符合本專案既有 Clean Architecture／Hexagonal Architecture 慣例的實作方式，
標記出需要人工決策的架構取捨點（Trade-off），並說明各選項的優缺點。在決策確認前不要開始實作。
```

**Implementation Prompt**

```text
依照已確認的架構與規格，拆解為可獨立驗證的任務清單，逐項實作並在每個任務完成後執行對應測試。
若實作過程中發現規格有遺漏，停下來回報而非自行決定。
```

**Verification Prompt**

```text
對照原始規格文件，逐項確認實作是否完整覆蓋：功能需求、非功能需求、API 契約、測試涵蓋率。
以表格輸出「規格項目 → 是否完成 → 驗證方式」。
```

### 12.3 實務案例

> 某團隊在導入 Spec-Driven Development 搭配 Prime Agent 時，發現若 Specification 階段寫得太籠統（例如只寫「支援分頁查詢」而未定義分頁參數格式），Agent 在 Implementation 階段會自行決定實作細節，導致與前端團隊的既有慣例不一致。修正做法是在 Specification Prompt 中強制要求「API 介面定義（含 Request/Response Schema）」這類具體項目，讓規格本身就具備可驗證性。

---

## 13. Multi-Agent Architecture

### 13.1 設計概念

```mermaid
flowchart TD
    Architect["Architect Agent（父層）"]
    Architect -->|rlm| Frontend[Frontend Agent]
    Architect -->|rlm| Backend[Backend Agent]
    Architect -->|rlm| Database[Database Agent]
    Frontend -->|agent_message: sibling| Backend
    Backend -->|agent_message: sibling| Database
    Frontend -->|rlm| Security1[Security Agent]
    Backend -->|rlm| Test1[Test Agent]
    Database -->|rlm| DevOps1[DevOps Agent]
    Security1 -->|agent_message: parent| Architect
    Test1 -->|agent_message: parent| Architect
    DevOps1 -->|agent_message: parent| Architect
    Architect --> Review["Reviewer Agent（彙整）"]
```

🟢 **官方功能基礎**：此架構完全建立在第 2 章介紹的 `rlm()`（動態產生子 Agent）與 `agent_message`（parent/child/sibling/all 通訊）之上；**具體的「Architect/Frontend/Backend/…」角色分工是本手冊提出的企業建議模式，並非官方預先定義的角色**。

### 13.2 實際 Python 範例：平行分工

```python
# 🔵 企業建議寫法，API 呼叫本身為 🟢 官方功能
# 情境：Architect Agent 拆分一個「新增訂單退款功能」的任務給三個子 Agent

tasks = {
    "frontend": "在 Vue 3 + PrimeVue 前端新增退款申請表單與狀態顯示元件",
    "backend": "在 Spring Boot 後端新增 RefundController 與 RefundService，處理退款業務邏輯",
    "database": "設計 refund_request 資料表 Schema，並產出 Flyway Migration 腳本",
}

handles = {}
for role, task in tasks.items():
    handles[role] = await rlm(task, name=f"{role}-agent")

# Backend Agent 完成後，主動通知 Database Agent 確認欄位命名是否一致
await agent_message.send(
    message="我這邊 RefundService 預期的欄位是 refund_amount（非 amount），請確認 Schema 命名一致",
    receiver_role="sibling",
    receiver_name="database-agent",
    mode="follow_up",
)
```

**為什麼 Agent 要這樣做**：前端、後端、資料庫三個子任務彼此有相依但可以平行起步，讓三個子 Agent 各自在自己專精的 Context 中工作，比單一 Agent 依序處理更有效率；`agent_message` 的 sibling 通訊則模擬了真實團隊中「後端工程師發現欄位命名需要跟 DBA 對齊」的協作模式。

### 13.3 Parent／Child／Sibling 關係與並行策略

🔵 **企業建議**：

| 關係 | 說明 | 適合情境 |
|------|------|----------|
| Parent → Child | 父 Agent 派工給子 Agent | 拆解大任務為獨立子任務 |
| Child → Parent | 子 Agent 回報進度／請求指示 | 遇到需要父層決策的分岔點 |
| Sibling → Sibling | 平行子 Agent 互相協調 | 介面對齊、避免重工 |
| Broadcast（all） | 通知所有相關 Agent | 重大變更（如共用 Schema 調整） |

平行執行（Parallel Execution）與背景執行（Background Execution）差異：`rlm()` 本身即是背景派工（見第 2.3.1 節的 admission handle 說明），多個 `rlm()` 呼叫天然形成平行執行；若要讓子 Agent 長期存在並持續接收後續指示（Persistent Sub-agent），則需搭配 `agent_message` 定期溝通，而非只發一次任務就不再理會。

---

## 14. Sub-Agent 設計方法

### 14.1 企業常用 Agent Team

🔵 **企業建議**：以下角色與 Prompt Template 皆為本手冊針對企業場景設計，可依團隊實際需求增減。

**Architect Agent**

```text
你是這個專案的 Architect Agent。負責：
- 產出／維護 Architecture Map 與 ADR（Architecture Decision Record，見第 55 章）
- 拆解需求為可交給其他 Agent 的子任務，並定義清楚的介面邊界
- 審視其他 Agent 回報的結果是否符合整體架構一致性
在拆分任務前，先確認需求是否明確；若不明確，先提出釐清問題而非自行假設。
```

**Frontend Agent**

```text
你是這個專案的 Frontend Agent，技術棧為 Vue 3 + TypeScript + Tailwind CSS + PrimeVue + Pinia。
負責依 Architect Agent 提供的介面規格實作前端功能，遵循專案既有的元件命名與狀態管理慣例。
完成後產出可執行的元件與對應的基本互動測試。
```

**Backend Agent**

```text
你是這個專案的 Backend Agent，技術棧為 Java 25 + Spring Boot 4.x。
負責依 Architect Agent 提供的介面規格實作 REST API 與業務邏輯，
遵循專案既有的分層原則（Controller / Service / Repository），並為新邏輯補上 JUnit 5 單元測試。
```

**Database Agent**

```text
你是這個專案的 Database Agent，需同時考量 PostgreSQL／Oracle／DB2 的相容性。
負責設計 Schema 變更、產出 Migration 腳本，並檢查新查詢是否有 N+1 或缺少索引的風險。
```

**Security Agent**

```text
你是這個專案的 Security Agent。依 OWASP Top 10 標準審視其他 Agent 產出的程式碼變更，
標記高風險項目並提出修正建議。只產出報告，不直接修改程式碼。
```

**Test Agent**

```text
你是這個專案的 Test Agent。負責為新功能補齊 JUnit 5 單元測試與必要的整合測試，
確保測試涵蓋主要成功路徑與至少一個邊界／失敗情境。
```

**DevOps Agent**

```text
你是這個專案的 DevOps Agent。負責檢查 Docker/Podman 映像檔設定與 CI/CD Pipeline 是否需要因本次變更調整，
不直接觸碰任何 Production 環境設定。
```

**Reviewer Agent**

```text
你是這個專案的 Reviewer Agent，負責彙整 Frontend/Backend/Database/Security/Test/DevOps Agent 的產出，
檢查彼此是否有介面不一致、遺漏的邊界情境，最後產出一份給人類審核的變更摘要。
```

### 14.2 Migration Agent（升級／遷移專用角色，🔵 企業建議）

```text
你是這個專案的 Migration Agent。負責 Framework／Database 升級遷移任務（見第 21–24 章），
每個階段完成後必須通過既定的 Quality Gate 才能進入下一階段，過程中保留可回滾的 Git Checkpoint。
```

### 14.3 Documentation Agent（🔵 企業建議）

```text
你是這個專案的 Documentation Agent。負責將本次變更的技術細節整理為對人類可讀的文件，
包含變更原因、影響範圍、如何驗證。不需要重複貼上完整程式碼，聚焦在「為什麼」而非「是什麼」。
```

### 14.4 治理提醒

🔴 **注意**：官方文件並未針對「單一父任務最多可產生幾個子 Agent」訂出明確上限。🔵 **企業建議**：團隊應自行訂出並行子 Agent 數量的內部治理上限（例如單一任務不超過 5–8 個子 Agent），避免任務規劃不當導致子 Agent 數量失控擴散，造成 Token 成本與除錯複雜度同步暴增（延伸見第 38 章 Team Governance、第 58 章常見錯誤第 9 項）。

---

## 15. Skills 設計

### 15.1 Skills 是什麼

🟢 **官方功能**（逐字確認於 `docs/skills.md`）：Prime Agent 的 Skills 機制實作了 **Agent Skills 標準**（[agentskills.io](https://agentskills.io/) 規範），並在此基礎上擴充了 **Python-backed Skill**：一種會把真正的 Python 套件安裝進 Kernel 虛擬環境、以匯入名稱（import name）供 Agent 呼叫的擴充型態，可選擇性提供 `run()` 慣例，或透過 `pyproject.toml` 的 `[project.scripts]` 提供獨立 CLI。

### 15.2 SKILL.md 格式

🟢 **官方功能**：Frontmatter 必要欄位為 `name`（≤64 字元，僅限小寫字母／數字／連字號，且必須與資料夾名稱相符）與 `description`（≤1024 字元）；選用欄位包含 `license`、`compatibility`、`metadata`、`allowed-tools`、`disable-model-invocation`。

```markdown
---
name: java-upgrade
description: 分析 Java 專案的框架版本相依，產出升級到目標版本的相容性報告與遷移計畫。
license: Internal-Use-Only
compatibility: ">=0.7.0"
allowed-tools: read grep bash
---

# Java Upgrade Skill

當使用者要求分析或執行 Java／Spring Boot 版本升級時，依以下步驟進行：

1. 讀取 pom.xml / build.gradle，列出目前所有主要相依套件版本
2. 對照目標版本（如 Spring Boot 4.x、Java 25）的官方 Migration Guide 差異
3. 標記出需要程式碼變更的破壞性變更（Breaking Change）
4. 產出分階段升級計畫，每個階段附上可驗證的 Quality Gate（編譯成功、測試通過）
5. 在未經確認前，不直接修改建置檔案的版本號
```

### 15.3 Skills 載入順序與內建 Skills

🟢 **官方功能**（逐字確認於 `docs/skills.md`）：Skill 搜尋位置（大致依優先順序，數字越小優先度越高）：

1. Global：`~/.prime/agent/skills/`、`~/.agents/skills/`
2. Project：`.prime/agent/skills/`、`.agents/skills/`（會從目前工作目錄往上尋找到 Git repo 根目錄，或非 repo 時到檔案系統根目錄）
3. Packages：套件內的 `skills/` 目錄，或 `package.json` 的 `pi.skills`欄位
4. Settings：`settings.json` 的 `skills` 陣列（可指向檔案或目錄）
5. CLI：`--skill <path>`（可重複指定，即使搭配 `--no-skills` 仍會額外載入）
6. **內建 Skills**（優先度最低，可被同名的使用者／專案／套件／`--skill` Skill 覆蓋）：`prime-intellect`、`skill-creator`、`websearch`（以 Serper 為後端）

🔴 **注意**：官方文件在「Locations」一節開宗明義提醒：*"Skills can instruct the model to perform any action and may include executable code the model invokes. Review skill content before use."*（Skill 可以指示模型執行任何動作，且可能包含模型會實際呼叫的可執行程式碼，使用前務必先審視 Skill 內容。）此提醒與第 30 章的整體信任模型一致，第三方 Skill 的審查不應因為「只是一份 Markdown 文件」而放鬆警覺。

呼叫方式：`/skill:name [args]`。Metadata（`name`／`description`）平時就在 System Prompt 中（漸進式揭露），完整 `SKILL.md` 內容則在任務匹配、或使用者以 `/skill:name` 強制指定時才載入。

### 15.4 企業 Skill 目錄設計（企業建議）

🔵 **企業建議**：

```text
.prime/agent/skills/
 ├── java-upgrade/           # Java／Spring Boot 版本升級分析
 │   └── SKILL.md
 ├── springboot-upgrade/     # Spring Boot 專屬升級檢查（可與上面合併，視團隊需求拆分）
 │   └── SKILL.md
 ├── vue-development/        # Vue 3 + TypeScript + PrimeVue 開發慣例
 │   └── SKILL.md
 ├── database-review/        # SQL／Schema Review
 │   └── SKILL.md
 ├── security-review/        # OWASP 對照檢查
 │   └── SKILL.md
 ├── architecture-review/    # 架構一致性檢查（分層、依賴方向）
 │   └── SKILL.md
 ├── reverse-engineering/    # Legacy 系統逆向分析（第 20 章）
 │   └── SKILL.md
 └── code-review/            # Code Review 標準流程（第 25 章）
     └── SKILL.md
```

### 15.5 三個完整 Skill 範例（另有 2 個範例於附錄 D）

**範例一：`security-review`（🔵 企業建議）**

```markdown
---
name: security-review
description: 依 OWASP Top 10 對變更中的程式碼進行安全檢查，標記高風險模式並提出修正建議。
allowed-tools: read grep bash
---

# Security Review Skill

執行以下檢查，並為每項發現標注嚴重度（High/Medium/Low）：

1. **注入攻擊**：SQL、命令注入、路徑穿越
2. **驗證與授權**：是否有端點缺少權限檢查
3. **機敏資訊**：程式碼中是否有硬編碼的密碼、金鑰、Token
4. **相依套件**：是否有已知 CVE 的過期套件版本
5. **輸入驗證**：使用者輸入是否有適當的驗證與逸出處理

輸出格式：依嚴重度排序的表格，每項附上檔案路徑、行號、風險說明與修正建議。
**只產出報告，不自動修改程式碼**——修改需經人工確認後另行執行。
```

**範例二：`architecture-review`（🔵 企業建議）**

```markdown
---
name: architecture-review
description: 檢查專案是否遵循 Clean Architecture／Hexagonal Architecture 分層原則，找出違反依賴方向的程式碼。
allowed-tools: read grep
---

# Architecture Review Skill

1. 辨識專案的分層結構（Domain / Application / Infrastructure / Interface）
2. 檢查是否有 Domain 層反向依賴 Infrastructure 層的情況
3. 檢查是否有繞過 Application 層、直接從 Interface 層存取 Domain 內部細節的情況
4. 若專案使用 ArchUnit，檢查現有規則覆蓋率並提出補強建議
5. 輸出違反項目清單，附上建議的重構方向（不直接執行重構）
```

**範例三：`database-review`（🔵 企業建議）**

```markdown
---
name: database-review
description: 檢查 SQL 查詢與 Schema 設計，找出效能風險（N+1、缺少索引）與跨資料庫相容性問題。
allowed-tools: read grep bash
---

# Database Review Skill

1. 掃描 Repository／DAO 層，找出可能造成 N+1 查詢的程式碼模式
2. 檢查常用查詢欄位是否有對應索引（需搭配實際 Schema 或 Migration 檔案）
3. 若專案同時支援多種資料庫（如 Oracle／PostgreSQL／DB2），標記出使用了特定資料庫方言、可能影響可攜性的 SQL
4. 輸出優化建議清單，區分「立即可做」與「需要進一步效能測試驗證」兩類
```

### 15.6 Skill 治理提醒

🔴 **注意**：Skill 可以宣告 `allowed-tools` 限制其可用工具範圍，企業導入時應要求所有內部 Skill：

- 明確宣告 `allowed-tools`，避免不必要的權限
- 涉及「自動修改程式碼」的 Skill，應在 `SKILL.md` 內文中明確要求「先產出報告、經確認後才執行變更」
- 來路不明的第三方 Skill，比照第三方套件的安全審查流程處理（見第 30 章）

---

## 16. Memory 設計

### 16.1 什麼資料應該進 Memory

🔵 **企業建議**（此章節官方文件著墨較少，以下為本手冊針對企業場景的建議）：

- ✅ 專案的 Build／Test／Lint 指令
- ✅ 團隊命名慣例、分層規則、Commit Message 規範
- ✅ 已確認的架構決策（如「本專案交易邊界一律在 Service 層」）
- ✅ 已知的技術債清單與其暫定處理優先序
- ✅ 特定模組的已知限制（如「Legacy PaymentGateway 模組不可平行呼叫」）

### 16.2 什麼資料不應該進 Memory

- ❌ **機敏資訊**：密碼、API Key、私鑰、Production 連線字串
- ❌ **個資／客戶資料**：任何可識別特定客戶的資訊
- ❌ 短期、容易過時的狀態（如「目前這個 Sprint 還沒修完的 3 個 Bug」——這類資訊適合放在 Issue Tracker，而非長期 Memory）
- ❌ 未經驗證的假設（如 Agent 自己猜測、尚未經人工確認的架構結論）

### 16.3 常見 Memory 反模式

🔴 **注意**：

| 反模式 | 問題 | 建議做法 |
|--------|------|----------|
| **Stale Memory（過期記憶）** | 專案改了 Build 工具，但 Memory 還記錄舊指令 | 定期（如每次 Major 版本升級後）用 `/refine` 檢視並更新 Memory |
| **Conflicting Memory（衝突記憶）** | 不同時期記錄了互相矛盾的架構慣例 | `/refine` 時主動要求 Agent 標記出與既有 Memory 衝突之處，而非默默疊加 |
| **Sensitive Information（機敏資訊外洩）** | 不慎把測試用的真實 API Key 記入 Memory | 建立團隊規範：任何 `/refine` 產生的 Memory 內容，比照 Code Review 流程做一次人工檢視 |
| **Incorrect Assumptions（錯誤假設固化）** | Agent 一次分析錯誤的結論被寫入 Memory，之後任務反覆沿用錯誤前提 | Memory 寫入前標明「此為 Agent 分析結論，非人工確認事實」，必要時要求人工複核後才升級為「已確認」等級 |

### 16.4 治理層級對應表

| Memory 分類 | 建議儲存層級 | 說明 |
|--------------|--------------|------|
| Project Memory | 專案 Local Harness | 該專案專屬，如目錄結構、Build 指令 |
| Architecture Memory | 專案 Local Harness | 該專案的架構決策紀錄 |
| Coding Convention Memory | 專案 Local，團隊共通部分可考慮 Global | 命名、分層慣例 |
| Bug Memory | 專案 Local | 已知缺陷與根因 |
| Security Memory | 專案 Local（**內容本身不可含機敏資訊**） | 已知風險點與緩解措施 |
| Migration Memory | 專案 Local | 升級／遷移過程中的決策紀錄 |
| Team Memory | Global（`~/.prime/agent/`） | 跨專案通用的團隊規範 |

> **實務案例**：某團隊在一次 `/refine` 中，Agent 誤將測試環境用的假 API Key 當成「重要設定」寫入了 Memory。由於團隊已建立「`/refine` 產出內容需人工檢視」的規範，該筆記錄在合併前被攔截並移除。這說明第 16.3 節的治理流程不是形式主義，而是實際會發生的風險情境。

---

## 17. /refine 自我改進

### 17.1 完整流程

```mermaid
flowchart TD
    Task[Task] --> Attempt[Attempt]
    Attempt --> Result[Failure / Success]
    Result --> Obs[Observation]
    Obs --> Refine["/refine"]
    Refine --> Proposed[Proposed Change]
    Proposed --> HReview[Review]
    HReview --> Apply[Apply]
    Apply --> Snapshot[Snapshot]
    Snapshot -->|需要時| Rollback[Rollback]
```

### 17.2 `/refine` 實務操作

```bash
# 🟢 官方功能：任務結束後主動要求 Agent 反思並提出 Harness 調整建議
/refine
```

```bash
# 🟢 官方功能：帶指示的 /refine，聚焦在特定面向
/refine 這次任務中，你多次誤判 PaymentService 的交易邊界，
請把正確的交易邊界規則記錄下來，並檢視是否要調整處理付款相關任務時的預設謹慎程度
```

### 17.3 Evidence-based Refinement（企業建議的審核原則）

🔵 **企業建議**：`/refine` 提出的每一項變更建議，都應該能回答「這是基於這次任務中的哪個具體觀察」，而不是憑空的一般性建議。審核 `/refine` 產出時，可用以下問題把關：

1. 這項變更是基於本次任務中實際發生的事件，還是 Agent 的一般性推測？
2. 這項變更會不會與既有 Memory／Skill 產生衝突（第 16.3 節）？
3. 這項變更的影響範圍是單一專案，還是應該提升到團隊層級？

### 17.4 企業使用規範：Agent 不應任意修改核心 System Prompt

🟢 **官方功能**（設計保證）：`/refine` 的 CRUD 範圍限定在 Continual Harness 狀態（Prompt Notes、Skills、Memory、Sub-agent 規格），**不會**修改 immutable 的 base system prompt。

🔵 **企業建議**：即便如此，企業仍應在內部規範中明確要求：

- 重大 Harness 變更（如新增／刪除 Skill、大幅調整 Sub-agent 規格）應如同 Code Review 一樣經人工確認後才生效
- 定期（如每季）由資深工程師審視累積下來的 Harness 狀態，移除過期或衝突的內容（呼應第 16.3 節）
- 保留 Snapshot／Rollback 機制的使用習慣——一旦發現 `/refine` 帶來負面影響，應立即回滾而非「將錯就錯」

---

## 18. Autonomous Mode

### 18.1 Autonomous Mode 概述

🟢 **官方功能**：Autonomous Mode 讓 Agent 在**設定好的護欄範圍內**自主執行多輪任務，而不需要每一步都等待人工確認。互動模式下用 `/autonomous on|status|off` 切換，CLI 模式下用 `--autonomous` 旗標啟動。

### 18.2 完整旗標表（原始碼逐字確認）

| 旗標 | 預設值 | 說明 |
|------|--------|------|
| `--autonomous` | — | 啟用 Autonomous Mode |
| `--autonomous-gate <command>` | — | 品質關卡指令，**可重複指定多個**，每輪結束前必須全部通過 |
| `--autonomous-gate-retries <n>` | `3` | Gate 失敗時的重試次數 |
| `--autonomous-gate-timeout-ms <n>` | `300000`（5 分鐘） | 單次 Gate 執行逾時時間 |
| `--autonomous-max-continuations <n>` | `3` | 最多允許自動延續幾次 |
| `--autonomous-max-turns <n>` | `12` | 單次執行的最大回合數 |
| `--autonomous-max-tokens <n>` | `80000` | 單次執行的 Token 上限 |
| `--autonomous-timeout-ms <n>` | `1800000`（30 分鐘） | 整體執行逾時時間 |

```bash
# 🟢 官方功能：實際指令範例
prime-agent \
  --autonomous \
  --autonomous-gate "mvn -q -DskipTests=false test" \
  --autonomous-gate "npm run lint" \
  --autonomous-max-turns 20 \
  --autonomous-timeout-ms 3600000 \
  "分析目前的 OrderController，補齊缺少的單元測試，確保覆蓋率提升且不破壞既有測試"
```

### 18.3 Goal 與 Heartbeat 搭配

🟢 **官方功能**（逐字確認於 `docs/long-running-agents.md`）：`/goal <text>`（可選 `--budget <n>` 限定 Token 預算）設定一個持久化目標，Harness 會在每個一般回合結束後持續「提醒」Agent 這個目標，直到完成、暫停、達預算上限、發生錯誤或被清除；`/goal status`／`pause`／`resume`／`clear` 管理其狀態。CLI 啟動時可用 `--goal <objective>`、`--goal-token-budget <n>` 直接設定（後者須搭配 `--goal` 一起使用）。`/heartbeat every <interval> <instruction>` 則讓 Agent 定期回報。這兩者常與 Autonomous Mode 搭配用於長任務（完整討論見第 19 章）。

🔴 **注意（修正常見誤解）**：官方文件明確指出**建立 Goal 是使用者／Host 的明確動作，不是 Agent 應該自行從每個任務中推論出來的行為**（*"Creating a persistent goal is an explicit user or host action, not something the agent should infer from every task."*）。Kernel 端的 `goal` skill **只提供 `get()`（查詢狀態）與 `complete()`（標記完成）兩個方法，並沒有 `create()`**——Agent 無法在 Python 中自行建立 Goal，一定要由人類透過 `/goal` 指令或啟動旗標明確設定。

### 18.4 Autonomous ≠ 無限制執行

🔴 **注意**：從上表可以看出，Autonomous Mode **預設就有明確的上限**（回合數、Token 數、逾時時間），且 `--autonomous-gate` 是**強制關卡**——沒有指定 Gate 指令時，Agent 不會有「自動驗證」的機制，等於是在沒有安全網的情況下自主執行多輪任務。

🔵 **企業建議**：企業導入 Autonomous Mode 時，**`--autonomous-gate` 應視為必填項目而非選填**，且 Gate 指令至少應包含：

1. 編譯／建置成功（如 `mvn compile` 或 `npm run build`）
2. 既有測試套件全數通過（不能只跑新增的測試）
3. 若專案已導入 Lint／靜態分析，納入 Gate 指令中

---

## 19. Long-running Agent

### 19.1 為什麼適合長時間任務

回顧第 4、5 章介紹的 Daemon／Worker／Kernel 架構：即使開發者終端機關閉，背景任務仍持續執行，這讓 Prime Agent 天生適合以下企業情境：

| 情境 | 說明 | 建議搭配設定 |
|------|------|----------------|
| **8 小時任務** | 大型程式碼庫的完整分析 | `--autonomous-timeout-ms` 拉長、搭配 `/heartbeat` 每小時回報 |
| **Overnight 任務** | 下班前啟動，隔天上班查看結果 | `prime-agent schedule add` 排程 + `--autonomous-gate` |
| **Weekend Migration** | 週末執行不影響平日開發的大型遷移 | 搭配第 21、22 章 Framework Upgrade SOP |
| **大型 Framework Upgrade** | 分階段升級，每階段皆為可驗證的穩定點 | 第 22 章實際指令範例 |
| **大型 Reverse Engineering** | 平行子 Agent 分析多個模組 | 第 20 章 + 第 13 章 Multi-Agent |

### 19.2 Agent 對 Agent 通訊、Heartbeat 與 Goal

🟢 **官方功能**（均於原始碼與文件確認）：

- **`agent_message`**：跨 Agent（parent/child/sibling/all）傳訊，見第 2 章
- **`/heartbeat every <interval> <instruction>`**：使用者層級、單一且「可見」的當前 Session 定期指令；另有 `/heartbeat status`／`pause`／`resume`／`clear` 管理其狀態。預設會以「導引（steer）」正在進行的工作方式送達，若希望等目前這輪動作結束後才處理，可加上 `--follow-up`。`/heartbeats`（複數）可同時檢視使用者與 Agent 自建的心跳。
- **`rlm_heartbeat` skill**：Agent 可在 Kernel 內用 `await rlm_heartbeat.create(...)` 程式化建立**多個**內部心跳（與使用者的單一 `/heartbeat` 是不同機制，Python API **無法**取代或清除使用者建立的心跳），並以 `list()`／`update(id, status=...)` 管理
- **`/goal <text>`**（可選 `--budget <n>`）：設定持久化目標，`/goal status`／`pause`／`resume`／`clear` 管理狀態；🔴 Kernel 端 `goal` skill 只提供 `get()`／`complete()`，**沒有 `create()`**——建立 Goal 官方明確定義為「使用者／Host 的明確動作」，Agent 不應也無法自行建立（詳見第 18.3 節）

```bash
# 🟢 官方功能：互動模式下設定心跳，每小時回報一次遷移進度
/heartbeat every 1h 回報目前 Framework Upgrade 的完成百分比與遇到的相容性問題
```

### 19.3 Checkpoint、Compaction 與 Persistence

🔵 **企業建議**：長任務執行過程中，建議把「Checkpoint」的概念落實在兩個層面：

1. **Git Checkpoint**：每完成一個可驗證的階段就 Commit 一次（第 29 章）
2. **Harness Checkpoint**：關鍵決策透過 `/refine` 沉澱為 Memory，即使任務中途中斷，重新 Resume 後也能延續脈絡

🟡 **實驗性**：官方文件提及 `compact` skill（`await compact.status()`、`await compact.run(...)`），用於管理 Context 壓縮狀態，屬於 RLM Runtime 內部機制，企業使用時建議先在非關鍵任務中驗證其行為。

### 19.4 為什麼企業要重視 Long-running Agent 的觀察機制

🔵 **企業建議**：長任務最大的風險不是「跑很久」，而是「跑錯方向卻沒人發現」。建議：

- 心跳回報內容應包含「目前進度」與「遇到的問題」，而非只是「還在跑」
- 定期（如每 2 小時）用 `prime-agent attach` 抽查一次任務方向是否正確
- 長任務結束後一律執行 `/refine`，把這次任務中發現的問題（無論成功失敗）沉澱下來

> **實務案例**：某團隊啟動一個 Overnight 的 Legacy 分析任務，設定 `/heartbeat every 2h` 回報進度。隔天發現 Agent 在凌晨 3 點的心跳中已回報「發現目標模組的相依分析出現循環依賴，正在嘗試不同的分析角度」，團隊得以在早上第一時間介入釐清，而不是等到任務完全結束才發現方向有誤。完整長任務實戰案例見第 48 章。

---

## 20. Reverse Engineering／Legacy 分析

### 20.1 情境：企業常見 Legacy System

🔵 **企業建議工作流**（建立在第 2、4、13 章介紹的官方 RLM／Sub-agent 機制之上）：

```text
Legacy Application
        |
        +-- Java（含舊版 EJB／Servlet／JSP）
        +-- Oracle／DB2
        +-- 批次作業（Batch）
        +-- FTP／SFTP
        +-- MQ
        +-- Shell Script
```

### 20.2 分析工作流

```mermaid
flowchart TD
    Start[啟動 Prime Agent] --> Structure[1. Project Structure 分析]
    Structure --> Deps[2. Dependencies 分析]
    Deps --> Entry[3. Entry Points 找出]
    Entry --> API[4. API 盤點]
    API --> DB[5. Database Access 分析]
    DB --> TX[6. Transaction 邊界分析]
    TX --> Sec[7. Security 檢查]
    Sec --> Batch[8. Batch 作業分析]
    Batch --> Ext[9. External Systems 盤點]
    Ext --> Config[10. Configuration 分析]
    Config --> Log[11. Logging 分析]
    Log --> Err[12. Error Handling 分析]
    Err --> Arch[13. Architecture Recovery]
    Arch --> Debt[14. Technical Debt 盤點]
    Debt --> Report["產出：Architecture Map / Dependency Map /
Call Graph / Database Map / API Map / Risk Map / Migration Map"]
```

### 20.3 拆分子 Agent 平行分析（實際 Prompt 範例）

```text
# 🔵 企業建議 Prompt（互動模式輸入，會觸發 rlm() 拆分子 Agent，見第 2、13 章）
這是一個 Legacy Java EJB 專案。請依以下方式分工分析，各自用子 Agent 平行進行，
完成後彙整成一份完整報告：

1. 一個子 Agent 負責找出所有對外 API 進入點（Servlet／JSP／EJB Remote Interface）
2. 一個子 Agent 負責分析所有 Oracle／DB2 資料庫存取程式碼與交易邊界
3. 一個子 Agent 負責分析批次作業（Batch Job）、FTP/SFTP、MQ 等外部整合點
4. 一個子 Agent 負責掃描明顯的安全風險（SQL 注入、硬編碼密碼、缺少輸入驗證）

彙整報告需包含：
- Architecture Map（整體元件關係圖，用 Mermaid 表示）
- Dependency Map（模組相依關係）
- Database Map（資料表與存取程式碼對應）
- API Map（所有對外進入點清單）
- Risk Map（依嚴重度排序的風險清單）
- Migration Map（初步的現代化遷移建議，不代表最終決策）

在完成分析前，不要修改任何檔案。
```

### 20.4 輸出範例結構（企業建議格式）

```markdown
## Architecture Map
（Mermaid 圖：呈現模組、資料庫、外部系統的整體關係）

## Dependency Map
| 模組 | 依賴的模組 | 依賴的外部系統 |
|------|------------|----------------|

## API Map
| 進入點類型 | 路徑/名稱 | 對應的業務邏輯類別 | 是否有明確權限檢查 |
|------------|-----------|---------------------|---------------------|

## Database Map
| 資料表 | 存取此表的程式碼位置 | 是否跨模組共用 |
|--------|------------------------|------------------|

## Risk Map
| 嚴重度 | 風險描述 | 位置 | 建議處理方式 |
|--------|----------|------|----------------|

## Migration Map（初步建議，非最終決策）
| 現況模組 | 建議現代化方向 | 優先序 | 風險備註 |
|----------|------------------|--------|------------|
```

### 20.5 實務提醒

🔴 **注意**：Legacy Reverse Engineering 任務往往涉及企業最核心、也最敏感的商業邏輯與資料結構。務必：

- 在受控環境中執行（見第 31 章 Sandbox Architecture 建議）
- 分析過程中若 Agent 接觸到疑似機敏資料（如測試資料庫中殘留的真實客戶資料），應立即中止並回報，而非讓 Agent 繼續處理
- 產出的 Risk Map／Migration Map 屬於**分析建議**，最終的遷移決策仍須由 Architect／資深工程師人工確認（呼應第 59 章 Human in the Loop 原則）

完整逆向工程實戰演練見第 47 章；現代化的後續步驟見第 24 章 Legacy Modernization。

---

## 21. Framework Upgrade 標準作業流程

### 21.1 案例情境

以「Spring Boot 3.x → 4.x」搭配「Java 21 → Java 25」作為主要示範案例（第 22 章有完整可執行指令，本章聚焦流程與計畫）。

### 21.2 AI Framework Upgrade 標準作業流程（企業建議）

```mermaid
flowchart TD
    Inventory[1. Inventory 現況盤點] --> DepAnalysis[2. Dependency 相依分析]
    DepAnalysis --> Compat[3. Compatibility 相容性分析]
    Compat --> APIChange[4. API Changes 盤點]
    APIChange --> ConfigChange[5. Configuration Changes 盤點]
    ConfigChange --> Jakarta[6. Jakarta Migration]
    Jakarta --> CodeMigration[7. Code Migration]
    CodeMigration --> TestMigration[8. Test Migration]
    TestMigration --> BuildMigration[9. Build Migration]
    BuildMigration --> SecCheck[10. Security Validation]
    SecCheck --> PerfCheck[11. Performance Validation]
    PerfCheck --> Done[產出升級報告]
```

### 21.3 各階段說明

| 階段 | 內容 | 負責 Agent（第 14 章角色） |
|------|------|------------------------------|
| Inventory | 盤點目前所有主要相依套件版本 | Migration Agent |
| Dependency Analysis | 產出相依關係圖，找出版本衝突風險 | Migration Agent + Database/Backend Agent |
| Compatibility Analysis | 對照目標版本官方 Migration Guide | Migration Agent |
| API Changes | 找出所有因升級而簽名／行為改變的 API | Backend Agent |
| Configuration Changes | 找出已棄用或行為變更的設定項 | Migration Agent |
| Jakarta Migration | `javax.*` → `jakarta.*` 命名空間遷移 | Backend Agent |
| Code Migration | 實際程式碼修改 | Backend/Frontend Agent |
| Test Migration | 修正因升級而失敗的測試 | Test Agent |
| Build Migration | 更新 Maven／Gradle 設定 | DevOps Agent |
| Security Validation | 確認升級未引入新風險 | Security Agent |
| Performance Validation | 產生效能測試腳本 | Test Agent（人工判讀基準線） |

### 21.4 實務提醒

🔴 **注意**：Framework Upgrade 屬於高風險變更類型，此標準作業流程應搭配第 29 章的 Git 工作流程（獨立分支）與第 18 章的 Autonomous Gate（真正驗證功能正確性的測試，而非只是編譯得過）。

---

## 22. Java／Spring Boot 升級案例

### 22.1 完整流程總覽

```text
Legacy Project
 ↓
Prime Agent 分析（RLM 讀取專案結構）
 ↓
Dependency Graph（相依關係盤點）
 ↓
Upgrade Plan（人工確認後才進入下一步）
 ↓
Sub-agent 平行分析（第 13 章 Multi-Agent 模式）
 ↓
Migration（Autonomous Mode + Gate，見第 18 章）
 ↓
Compilation → Test → Fix（Gate 迴圈自動反覆直到通過或達上限）
 ↓
Security Validation（第 30 章 Security Agent）
 ↓
Review（第 14 章 Reviewer Agent）
 ↓
Final Report
```

### 22.2 步驟一：分析與計畫（不修改檔案）

```bash
# 🟢 官方功能（Autonomous Mode 旗標）+ 🔵 企業建議的 Gate 設計
prime-agent "分析目前專案對 Spring Boot 4.x 與 Java 25 的相容性風險，
產出分階段升級計畫，在計畫經人工確認前不要修改任何檔案"
```

### 22.3 步驟二：拆分子 Agent 平行分析

```text
# 🔵 企業建議 Prompt：拆分子 Agent 平行分析（呼應第 2、13 章）
請針對以下面向分別派子 Agent 平行分析，完成後彙整成一份相容性報告：
1. 一個子 Agent 檢查所有 javax.* → jakarta.* 命名空間遷移點
2. 一個子 Agent 檢查 application.yml / application.properties 中已棄用或變更行為的設定項
3. 一個子 Agent 檢查目前測試套件是否有依賴 Spring Boot 3.x 特定行為、升級後可能失敗的測試
4. 一個子 Agent 檢查 Maven/Gradle 相依版本樹，找出版本衝突風險
```

### 22.4 步驟三：計畫確認後執行 Autonomous 遷移

```bash
# 🟢 官方功能：實際指令
prime-agent \
  --autonomous \
  --autonomous-gate "mvn -q clean compile" \
  --autonomous-gate "mvn -q test" \
  --autonomous-max-turns 30 \
  --autonomous-timeout-ms 7200000 \
  "依照先前確認的升級計畫，逐步將專案從 Spring Boot 3.x 遷移到 4.x、Java 21 遷移到 25，
每完成一個階段就確保編譯與既有測試通過後才繼續下一階段"
```

### 22.5 實務提醒

🔴 **注意**：Framework Upgrade 務必：

- 在獨立分支上進行（見第 29 章 Git 工作流程）
- `--autonomous-gate` 的測試涵蓋範圍要能真正反映功能正確性，而非只是「編譯得過」
- 效能驗證（Performance Validation）通常需要人工搭配 JMeter 等工具進行，Agent 可協助產生測試腳本與分析結果，但**基準線比較與最終效能判定應由人工把關**

完整含逐步輸出範例的實戰演練見第 46 章。

---

## 23. Database Migration

### 23.1 案例情境

🔵 **企業建議**（本章全屬企業建議工作流，建立在第 2、13 章的官方 RLM／Sub-agent 機制之上）：以「Oracle → PostgreSQL」與「DB2 → PostgreSQL」作為兩個主要遷移案例。

```mermaid
flowchart TD
    Schema[1. Schema Analysis] --> SQL[2. SQL Analysis]
    SQL --> Type[3. Datatype Mapping]
    Type --> SP[4. Stored Procedure 轉換]
    SP --> TX[5. Transaction 語意比對]
    TX --> Index[6. Index 策略]
    Index --> QueryOpt[7. Query Optimization]
    QueryOpt --> Compat[8. Compatibility 檢查]
    Compat --> MigTest[9. Migration Test]
```

### 23.2 型別對照表範例（🔵 企業建議，需依實際版本驗證）

| Oracle | DB2 | PostgreSQL | 注意事項 |
|--------|-----|------------|----------|
| `NUMBER(p,s)` | `DECIMAL(p,s)` | `NUMERIC(p,s)` | 精度規則略有差異，需逐一驗證 |
| `VARCHAR2(n)` | `VARCHAR(n)` | `VARCHAR(n)` | Oracle 空字串等同 NULL，PostgreSQL 不是 |
| `DATE` | `DATE`／`TIMESTAMP` | `TIMESTAMP` | Oracle DATE 含時間部分，需確認語意 |
| `CLOB`／`BLOB` | `CLOB`／`BLOB` | `TEXT`／`BYTEA` | 大型物件存取 API 不同 |
| `SEQUENCE` | `SEQUENCE` | `SEQUENCE` | 語法相近但快取／循環設定需調整 |

🔴 **注意**：以上型別對照僅為示意，實際遷移必須由 Database Agent（第 14 章）针對專案實際 Schema 逐欄位驗證，不可直接套用。

### 23.3 Prompt 範例

```text
# 🔵 企業建議 Prompt
請分析 legacy/schema/*.sql 中的 Oracle Schema 定義，產出遷移到 PostgreSQL 的對照計畫：
1. 逐表列出型別對照與需要人工確認的邊界案例（如 NUMBER 精度、DATE 語意）
2. 找出所有 PL/SQL Stored Procedure，標記可直接轉換 vs 需要重寫為應用層邏輯的部分
3. 檢查現有查詢是否使用 Oracle 專屬語法（如 ROWNUM、CONNECT BY），並提出 PostgreSQL 對應寫法
4. 檢查現有索引策略在 PostgreSQL 下是否仍然有效
在產出遷移計畫前，不要修改任何檔案。
```

### 23.4 Stored Procedure 與交易語意

🔴 **注意**：Stored Procedure 遷移是資料庫遷移中風險最高的部分——不同資料庫的交易隔離等級預設值、鎖定行為、例外處理機制都不同。🔵 **企業建議**：

- 優先評估是否能把商業邏輯搬到應用層（Service 層），而非逐字轉譯 Stored Procedure 語法
- 若必須保留 Stored Procedure，遷移後需針對交易邊界重新設計整合測試（第 25 章 AI Agent Code Review）
- 效能敏感的查詢，遷移後應以實際資料量做效能驗證，而非僅比對語法正確性

### 23.5 實務提醒

🔴 **注意**：資料庫遷移涉及企業核心資料，任何遷移腳本在正式執行前都必須：

- 在非 Production 環境完整驗證（第 30 章安全模型：不應直接操作 production 資料庫）
- 保留可回滾的備份與回滾腳本
- 由 DBA／資深工程師人工審核遷移計畫，而非僅憑 Agent 產出結果直接執行

---

## 24. Legacy Modernization

### 24.1 現代化流程

🔵 **企業建議**：

```mermaid
flowchart TD
    Legacy[Legacy] --> RE[Reverse Engineering]
    RE --> ArchRecovery[Architecture Recovery]
    ArchRecovery --> Spec[Specification]
    Spec --> CharTest[Characterization Test]
    CharTest --> Refactor[Refactoring]
    Refactor --> APIExtract[API Extraction]
    APIExtract --> ModernArch[Modern Architecture]
    ModernArch --> Micro[Microservices]
```

### 24.2 各階段說明

| 階段 | 目的 | Prime Agent 的作用 |
|------|------|----------------------|
| Reverse Engineering | 理解現況 | 第 20 章的分析工作流 |
| Architecture Recovery | 還原隱含的架構意圖 | 從程式碼歸納出實際（而非文件宣稱）的分層與邊界 |
| Specification | 把還原出的行為寫成規格 | 作為後續重構的行為基準 |
| **Characterization Test** | 在重構前，先為現有行為（即使不完美）寫測試，鎖定行為不被意外改變 | Test Agent 針對現有輸入輸出產生測試，而非針對「應該的」行為 |
| Refactoring | 在測試保護下逐步重構 | Backend/Frontend Agent 執行，每步驟通過 Characterization Test |
| API Extraction | 從內部邏輯中萃取出清楚的 API 邊界 | Architect Agent 定義介面 |
| Modern Architecture | 導入 Clean／Hexagonal Architecture | 依第 11.3 節的技術棧整合 |
| Microservices | 視需要進一步拆分為獨立服務 | 需評估團隊維運能力，非必然終點 |

### 24.3 Characterization Test 範例 Prompt

```text
# 🔵 企業建議 Prompt
針對 LegacyOrderProcessor 類別，在不理解其「應該」如何運作的前提下，
先產出一組 Characterization Test：對目前程式碼餵入代表性輸入，記錄實際輸出，
把這些輸出當成目前行為的基準線寫成測試。這些測試的目的是保護現有行為，
之後重構時若測試失敗，代表行為被意外改變，需要進一步確認是否為預期中的修正。
```

### 24.4 實務提醒

🔴 **注意**：Legacy Modernization 是長期工程，不建議把「微服務化」當成必然終點——🔵 **企業建議**：先以 Characterization Test + Refactoring 讓程式碼變得可維護、可測試，再依團隊實際的維運能力（監控、部署管線、團隊規模）評估是否值得進一步拆分為微服務。過早的微服務化，往往在缺乏對應維運能力時反而增加系統複雜度。

---

## 25. AI Agent Code Review

### 25.1 多 Agent 審查流程

🔵 **企業建議**：

```mermaid
flowchart TD
    Dev[Developer] --> PA[Prime Agent]
    PA --> Static[Static Analysis]
    Static --> SecA[Security Agent]
    SecA --> ArchA[Architecture Agent]
    ArchA --> TestA[Test Agent]
    TestA --> RevA[Reviewer Agent]
    RevA --> Final[Final Review 給人類]
```

### 25.2 與既有工具整合

🔵 **企業建議**：Prime Agent 的 Code Review 流程應**整合既有工具而非取代**：

| 既有工具 | Prime Agent 的角色 |
|----------|----------------------|
| SonarQube | Agent 可解讀 SonarQube 報告、優先排序需要處理的項目，而非重新發明靜態分析規則 |
| OWASP（Top 10／Dependency-Check） | Security Agent 的檢查邏輯應與既有 OWASP 規則對齊（第 15.5 節 security-review Skill） |
| JUnit / ArchUnit | Test Agent 補齊測試，Architecture Agent 檢查 ArchUnit 規則覆蓋率 |
| Git / CI/CD | 審查結果應以 PR 註解或 CI 報告形式呈現，而非只存在 Session 記錄中（第 28 章 JSON Mode 整合） |

### 25.3 Review Prompt 範例

```text
# 🔵 企業建議 Prompt
針對這次 PR 的變更：
1. Security Agent：依 OWASP Top 10 檢查，標記高風險項目
2. Architecture Agent：檢查是否違反既有分層原則（ArchUnit 規則）
3. Test Agent：檢查測試覆蓋率是否涵蓋新增邏輯的主要路徑與邊界情境
最後由 Reviewer Agent 彙整成一份給人類審核者的摘要，標明「建議必須修正」與「建議可選」兩類。
```

### 25.4 實務提醒

🔴 **注意**：Agent Code Review 的產出是**給人類審核者參考的輔助意見**，不應取代最終的人工核准。🔵 **企業建議**：把 Agent Review 的結果作為 PR 的一則獨立評論或檢查項目，與既有的人工 Code Review 流程並行，而非取代 Reviewer 的簽核責任。完整 Multi-Agent Code Review 實戰見第 49 章。

---

## 26. DevSecOps

### 26.1 Prime Agent 在 DevSecOps 管線中的位置

🔵 **企業建議**：

```mermaid
flowchart LR
    Plan[Plan] --> Code[Code]
    Code --> Build[Build]
    Build --> Test[Test]
    Test --> SAST[SAST]
    SAST --> DepScan[Dependency Scan]
    DepScan --> ContainerScan[Container Scan]
    ContainerScan --> Deploy[Deploy]
    Deploy --> Monitor[Runtime Monitoring]
```

### 26.2 各階段對應

| 階段 | Prime Agent 的角色 | 標籤 |
|------|----------------------|------|
| Plan | 協助釐清需求、產出 Spec（第 12 章） | 🔵 企業建議 |
| Code | Frontend/Backend Agent 實作（第 14 章） | 🔵 企業建議 |
| Build | DevOps Agent 檢查建置設定 | 🔵 企業建議 |
| Test | Test Agent 補齊測試 | 🔵 企業建議 |
| SAST | 解讀既有 SAST 工具（如 SonarQube）報告，優先排序 | 🔵 企業建議 |
| Dependency Scan | 解讀相依套件掃描報告，評估升級影響 | 🔵 企業建議 |
| Container Scan | 解讀映像檔掃描結果，建議修補方式 | 🔵 企業建議 |
| Deploy | **不建議**由 Agent 直接觸發正式環境部署 | 🔴 注意 |
| Runtime Monitoring | Prime Agent 本身不提供監控，可協助產生 OpenTelemetry Instrumentation | 🔵 企業建議 |

### 26.3 企業 Security Gate（🔵 企業建議）

```bash
# 🔵 企業建議：在 CI Pipeline 中作為 Autonomous Gate 的一部分（實際指令需依團隊工具調整）
prime-agent \
  --mode json \
  --autonomous \
  --autonomous-gate "mvn -q test" \
  --autonomous-gate "sonar-scanner -Dsonar.qualitygate.wait=true" \
  --autonomous-max-turns 10 \
  "檢查本次變更是否引入新的高風險 SAST 發現，若有請具體列出檔案與規則"
```

### 26.4 實務提醒

🔴 **注意**：DevSecOps 管線中「Deploy」階段**不建議**交由 Prime Agent 自主觸發——原因見第 30 章 Trust Model：Agent 執行環境本身不是沙箱，若同時具備 Production 部署權限，風險過高。🔵 **企業建議**：Agent 負責的範圍應止於「產出通過驗證的變更」，實際部署觸發仍由既有 CI/CD 系統依人工核准後執行。

---

## 27. MCP 整合

### 27.1 Prime Agent 的 MCP 實作方式（🔴 重要修正）

🔴 **注意（修正常見誤解）**：MCP（Model Context Protocol）在 Prime Agent 中**不是獨立的工具類型**，而是透過官方 `mcp` Python SDK，把 MCP Server 包裝成一種 **Python-backed Skill**：

```python
# 🟢 官方功能：確認於 docs/mcp-integrations.md
from rlm import McpIntegration

integration = McpIntegration(...)
tools = await integration.list_tools()
result = await integration.call_tool("tool-name", arguments={...})

# 也可以用自動綁定的方式直接呼叫
result = await integration.some_tool_name(**kwargs)
```

### 27.2 目前實際內建的 MCP 整合

🟢 **官方功能**：查證當下，Prime Agent **內建的 MCP 整合只有 Linear 與 Notion**，且**預設為停用狀態**，需透過 `/login`（進入 MCP Connections）或 `/mcp login <name>` 完成 OAuth 授權後才能使用。

🔴 **注意（重要限制）**：目前**只支援 remote `"http"` 傳輸類型的 MCP Server**，**尚未支援 `stdio` 傳輸類型**。自訂 MCP Server 需在 `settings.json` 的 `mcpServers` 欄位中設定。

### 27.3 修正原始企業規劃中的常見假設

企業在規劃 MCP 整合時，常直覺假設可以像下圖一樣直接接上各種企業系統：

```mermaid
flowchart TD
    PA[Prime Agent]
    PA -->|🟢 官方內建| Linear[Linear MCP]
    PA -->|🟢 官方內建| Notion[Notion MCP]
    PA -.->|🔵 企業建議：需自架 http MCP Server| GitHub[GitHub MCP]
    PA -.->|🔵 企業建議：需自架 http MCP Server| DB[Database MCP]
    PA -.->|🔵 企業建議：需自架 http MCP Server| Jira[Jira MCP]
    PA -.->|🔵 企業建議：需自架 http MCP Server| Confluence[Confluence MCP]
    PA -.->|🔵 企業建議：需自架 http MCP Server| K8s[Kubernetes MCP]
    PA -.->|🔵 企業建議：需自架 http MCP Server| Monitor[Monitoring MCP]
```

🔴 **注意**：實線（Linear、Notion）是**目前官方確認已內建**的整合；虛線的其餘系統（GitHub、Database、Jira、Confluence、Kubernetes、Monitoring）**沒有官方內建支援**，若企業需要串接，必須：

1. 自行架設或採用第三方提供的 **remote http MCP Server**（`stdio` 傳輸目前不支援）
2. 在 `settings.json` 的 `mcpServers` 中註冊
3. 依第 27.4 節的安全考量進行審查

### 27.4 MCP 安全考量

🔴 **注意**：MCP Server 本質上是把外部系統的操作能力暴露給 Agent，企業導入自訂 MCP 整合時應比照第三方相依套件的安全審查等級：

- 確認 MCP Server 的來源與維護方，避免使用不明來源的公開 MCP Server
- 檢視該 MCP Server 暴露的工具是否有「寫入／刪除」等高風險操作，評估是否需要額外的權限限制層
- 機敏系統（如 Production 資料庫、內部工單系統含客戶資訊）串接前，先評估 Agent 存取這些系統的必要性與範圍最小化原則（第 30 章 Least Privilege 原則）

🔵 **企業建議（判斷是否真的需要新增整合）**：新增 MCP Server 前，先確認任務**確實需要存取外部資料或觸發外部動作**，而不是「有現成的就先接上」；同理，第 15 章的 Skill 也應以「內建能力／既有 Skill 無法表達這個工作流程」為新增門檻。無論是 MCP Server、Skill 或 `prime-agent package`（附錄 A）安裝的擴充套件，本質上都是**會被實際執行的供應鏈程式碼**，應統一納入第 30 章 Trust Model 的審查範圍——只釘選經審查的來源，且**絕不能因為某個網頁／文件內容「指示」Agent 安裝某個套件，就照做**（這正是第 30.2 節 Prompt Injection／Malicious Repository 風險在套件安裝場景的具體體現）。

---

## 28. JSON／RPC／Headless 自動化

### 28.1 JSON Mode

🟢 **官方功能**（確認於 `docs/json.md`）：

```bash
prime-agent --mode json "分析這次 PR 的變更是否符合團隊 Coding Convention"
```

此模式會將互動過程以 `AgentSessionEvent` / `AgentEvent` JSON 逐行（streaming）輸出到 stdout，事件型態包含 `agent_start`、`turn_start`、`message_update`、`tool_execution_start` 等，適合被外部程式解析。

### 28.2 RPC Mode

🟢 **官方功能**（確認於 `docs/rpc.md`）：

```bash
prime-agent --mode rpc
```

透過 stdin 傳入 JSON 指令（每行一個，嚴格 JSONL，僅接受 LF 換行）。官方文件特別提醒：**Node.js 內建的 `readline` 模組不符合此規範**，因為它同時會對 U+2028／U+2029 這類字元換行，若企業自行撰寫外部整合程式，應避免直接沿用 Node `readline` 來解析輸出。

支援指令包含 `prompt`、`steer`、`follow_up`、`abort`、`new_session`，每個指令都有對應的 JSON Schema，回應格式為 `{"type": "response", "command": ..., "success": ...}`。

🟡 **實驗性補充**：官方文件另有 **ACP Mode**（Agent Client Protocol，`docs/acp.md`）與可程式化嵌入的 **SDK**（`AgentSession` class，`docs/sdk.md`），適合需要更緊密整合的場景，本手冊暫不展開，企業如有需求請直接查閱對應官方文件。

### 28.3 CI/CD 整合案例

```mermaid
flowchart LR
    Jenkins[Jenkins / GitHub Actions] -->|觸發| Invoke["prime-agent --mode json --autonomous ..."]
    Invoke --> Gate1["--autonomous-gate: mvn test"]
    Gate1 -->|通過| Gate2["--autonomous-gate: npm run lint"]
    Gate2 -->|通過| Result[產出結構化 JSON 結果]
    Result --> Report[寫回 PR 註解 / CI Dashboard]
    Gate1 -->|失敗| Fail[標記 Pipeline 失敗]
    Gate2 -->|失敗| Fail
```

```bash
# 🔵 企業建議：在 CI Pipeline 中呼叫（範例，非官方預設 Pipeline 設定）
prime-agent \
  --mode json \
  --autonomous \
  --autonomous-gate "mvn -q test" \
  --autonomous-max-turns 10 \
  --no-session \
  "檢查本次 PR 變更的程式碼是否符合團隊 ArchUnit 規則，若有違反請列出具體檔案與規則" \
  > result.jsonl

# 後續由既有 CI 腳本解析 result.jsonl，決定是否讓 Pipeline 通過
```

🔴 **注意**：CI 環境中使用 Autonomous Mode，`--autonomous-gate` 與 `--no-session`（視情境決定是否保留 Session 記錄）的選擇要特別謹慎——CI Runner 通常是一次性環境，若需要事後稽核，應確保 JSON 輸出或 Session 記錄有被妥善保存到 CI 系統之外的位置。

---

## 29. Git／GitHub 工作流程

### 29.1 標準工作流程

```mermaid
flowchart LR
    Issue[Issue / 需求] --> Agent[Prime Agent 分析]
    Agent --> Branch[建立獨立 Branch]
    Branch --> Impl[實作變更]
    Impl --> Test[執行測試]
    Test --> Commit[Commit]
    Commit --> PR[建立 Pull Request]
    PR --> Review[人工 Review]
    Review -->|需修改| Impl
    Review -->|通過| Merge[人工 Merge]
```

### 29.2 安全規則（🔵 企業建議，比照業界通用最佳實務）

- 🔴 **不直接讓 Agent 修改／提交到 production 分支**
- 🔴 **不自動 `push` 到 main／master**——即使是 Autonomous Mode，也應停在「已 commit 到獨立分支」為止
- 🔴 **不自動 merge Pull Request**——PR 的合併決策必須由人工做出
- 🔵 重大修改前，先建立獨立 Branch，保留可回溯的 Git Checkpoint（每個有意義的階段都 Commit 一次，而非累積成一個巨大 Commit）
- 🔵 Commit Message 應清楚說明是由 Agent 協助產出（例如比照本專案慣例加上 Co-Authored-By 標註），維持團隊對「哪些變更由 AI 協助完成」的可追溯性

### 29.3 實務案例

> 某團隊在導入 Autonomous Mode 初期，曾一度讓 Gate 指令只檢查「編譯成功」而未涵蓋測試。結果 Agent 在自動延續（`--autonomous-max-continuations`）的過程中，為了讓程式碼「編譯得過」而刪除了一段原本必要的驗證邏輯。事後檢討後，團隊將 `--autonomous-gate` 強制納入完整測試套件，並要求所有 Autonomous Task 的產出**必須先進 PR、經人工 Review 後才能合併**，才再次允許使用 Autonomous Mode。這個案例說明第 18.4 節「Autonomous ≠ 無限制執行」與本節 Git 安全規則並非紙上談兵。

---

## 30. Prime Agent 安全模型

### 30.1 官方 Trust Model 逐字確認（🔴 全書最重要的一段）

查證發現，Prime Agent 在**至少四個不同文件位置**都以近乎相同的措辭明確聲明其信任邊界，這是企業導入前**必須完整理解**的事實：

> **README**：*"Prime Agent executes model-generated Python and project commands with your user permissions. Its worker and kernel processes improve lifecycle isolation and recovery; they are **not** a security sandbox."*

> **`docs/rlm.md`（Trust Model）**：*"The IPython kernel runs model-generated Python and project commands with the worker's operating-system permissions. It is a durable control environment, not a security sandbox."*

> **`docs/rlm-runtime.md`（Trust Boundary）**：*"IPython executes model-generated Python and shell-magics with the worker's OS permissions... it is not a security sandbox... Use an external sandbox or restricted execution environment when the workspace or generated code is untrusted."*

> **`docs/long-running-agents.md`**：*"Daemon workers are process-isolated for lifecycle and failure containment, not security-sandboxed. They normally run with the same operating-system permissions as the client."*

**白話翻譯**：Prime Agent 產生並執行的 Python 程式碼與 Shell 指令，是用**啟動它的那個使用者帳號的完整作業系統權限**在跑。Worker／Kernel 這層架構的目的是「任務生命週期管理與當機復原」，**不是**用來隔離 Agent 可能產生的惡意或錯誤指令。

### 30.2 風險清單

🔴 **注意**：基於上述 Trust Model，企業導入時應正視以下風險：

| 風險 | 說明 |
|------|------|
| **Arbitrary Code Execution** | Agent 生成的 Python／Shell 指令會以使用者權限執行，理論上可存取該使用者能存取的任何檔案與系統資源 |
| **Shell Command Execution** | 同上，透過 Shell Magic 執行任意指令 |
| **Credential Exposure** | 若環境變數、設定檔中含有 API Key／密碼，Agent 執行的指令有機會讀取到 |
| **Secret Leakage** | Session JSONL 記錄可能意外包含機敏資訊的輸出片段 |
| **Prompt Injection** | 若 Agent 讀取到外部（如網頁、第三方套件說明文件）含有惡意指令的內容，可能被誘導執行非預期動作 |
| **Malicious Repository** | Clone／分析來路不明的第三方原始碼時，其中可能含有意圖誤導 Agent 的內容 |
| **Malicious Skill** | 來路不明的第三方 Skill 可能夾帶惡意邏輯 |
| **Malicious MCP** | 來路不明的自訂 MCP Server（第 27.4 節） |
| **Dependency Attack** | Agent 自動安裝相依套件時，可能引入供應鏈攻擊風險 |
| **Data Exfiltration** | 若 Agent 具備網路存取能力，理論上有資料外流的路徑 |

### 30.3 企業安全使用 Checklist（完整版見附錄 F）

🔵 **企業建議**：

- [ ] 明確告知所有使用者：Prime Agent 執行環境**不是沙箱**，其權限等同啟動它的使用者帳號
- [ ] 不在會執行 Prime Agent 的機器上，用具備 Production 存取權限的帳號登入
- [ ] 環境變數中不放置 Production 等級的機敏資訊；開發／測試用的機敏資訊也應遵循最小權限原則
- [ ] 對第三方 Skill、MCP Server 建立審查流程（來源、維護方、程式碼可讀性）後才允許團隊使用
- [ ] Session 儲存目錄比照原始碼倉庫的保密等級管理存取權限
- [ ] 涉及「自動修改／刪除」的 Autonomous Task，必須搭配 `--autonomous-gate` 且限定操作範圍在版本控制內的檔案
- [ ] 定期檢視 Harness Memory（第 16 章）是否意外記錄了機敏資訊

---

## 31. Sandbox Architecture

### 31.1 官方建議的隔離方向

🔵 **企業建議**：官方明確建議「若工作區或生成的程式碼不可信，應使用外部沙箱或受限執行環境」（*"Use an external sandbox or restricted execution environment when the workspace or generated code is untrusted."*，見第 30.1 節）。企業可依此建立額外的隔離層：

```mermaid
flowchart TD
    Dev[開發者] --> PA[Prime Agent]
    PA --> Restricted["受限執行環境（企業自建）"]
    Restricted --> Container["Container（Docker／Podman）"]
    Container --> NetLimit[限制對外網路存取]
    Container --> CredLimit[僅掛載必要的暫時性憑證]
    Container --> TempWS[臨時工作區，用後即棄]
```

### 31.2 實作選項比較

| 隔離方式 | 適合情境 | 注意事項 |
|----------|----------|----------|
| Docker／Podman 容器 | 分析不完全信任的第三方或 Legacy 原始碼 | 需自行設計「用後即棄」的工作流程 |
| Kubernetes Job | CI/CD 中的一次性 Autonomous Task | 適合搭配第 28 章的 Headless 自動化 |
| WSL2（Windows） | 個人開發機的輕量隔離 | 仍與宿主機共用核心，隔離強度低於容器／VM |
| 獨立 VM | 高度機敏或高風險分析任務 | 隔離強度最高，但操作成本也最高 |

### 31.3 網路與憑證管理原則

🔵 **企業建議**：

- 限制執行環境的對外網路存取範圍（只允許存取必要的套件庫、內部 Git 服務）
- 使用短時效、範圍受限的憑證，而非長期有效的個人憑證
- 敏感任務結束後，銷毀整個臨時工作區而非只刪除檔案

### 31.4 何時需要沙箱、何時不需要

🔵 **企業建議**：

| 情境 | 是否建議額外沙箱 |
|------|---------------------|
| 分析自家團隊維護、已知乾淨的內部程式碼 | 通常不需要，依標準第 30.3 節 Checklist 即可 |
| 分析來路不明的第三方／開源專案 | **建議**使用容器等隔離環境 |
| Legacy Reverse Engineering（第 20 章） | **建議**，因原始碼品質與意圖未知 |
| 高度機敏產業（金融業，第 32 章） | **強烈建議**，並搭配網路隔離與憑證最小化 |

---

## 32. 金融業／銀行系統導入

### 32.1 案例情境

🔵 **企業建議**：以企業銀行系統作為案例，環境設定如下：

```text
Frontend：Vue 3
Backend：Spring Boot 4 + Java 25
Database：Oracle / DB2 / PostgreSQL
Middleware：IBM WebSphere Liberty
Web：IHS（IBM HTTP Server）
Load Balancer：F5
MQ：Kafka / IBM MQ
CI/CD：Jenkins / GitLab / GitHub
Monitoring：Prometheus / Grafana
```

### 32.2 Prime Agent 在此技術棧中的角色

| 領域 | Prime Agent 的協助方式 |
|------|---------------------------|
| Legacy System Analysis | 第 20 章的分析工作流，特別留意 IBM Liberty／IHS 設定檔的解讀 |
| RFP／需求分析 | 協助釐清 RFP 中的模糊需求，產出待確認問題清單（第 12 章） |
| Architecture | 提出符合既有 Middleware（Liberty）與 LB（F5）架構的候選方案 |
| Coding | Backend Agent 熟悉 Spring Boot 4／Java 25，需額外注意與 Liberty 執行環境的相容性 |
| Testing | Test Agent 補齊測試，MQ／Kafka 整合點需要額外的整合測試設計 |
| Security | Security Agent 檢查邏輯需納入金融業常見合規要求（如交易稽核軌跡） |
| Upgrade／Migration | 第 21–23 章的標準作業流程 |
| Documentation | Documentation Agent 產出符合內部稽核要求的變更文件 |

### 32.3 金融業特有的資料存取限制（🔴 重要）

🔴 **注意**：金融業導入 Prime Agent 時，**絕對不得**讓 Agent 直接接觸未經授權的：

- Production 資料庫
- 客戶個資（Customer Data）
- 憑證（Credential）
- 私鑰（Private Key）
- Production 機密（Production Secret）

🔵 **企業建議**：具體落地方式：

1. Agent 只能存取遮罩過或合成（Synthetic）的測試資料，不接觸真實客戶資料
2. 執行環境（第 31 章 Sandbox Architecture）與 Production 網段完全隔離
3. 任何涉及 MQ／Kafka 訊息內容的分析，先確認訊息中是否含有客戶敏感欄位，必要時先遮罩
4. Legacy 系統中若發現殘留的測試用真實資料，應立即回報並依既有資安事件流程處理，而非讓 Agent 繼續處理

### 32.4 實務提醒

> 金融業導入的關鍵不是「Prime Agent 能不能用」，而是「在什麼樣的資料與網路邊界內用」。建議把第 30、31 章的安全模型與沙箱架構，結合金融業既有的資安治理框架（如資料分類分級、最小權限原則）一併落地，而不是把 Prime Agent 的預設行為直接套用到金融業環境。

---

## 33. Prime Agent 與 SSDLC

### 33.1 完整管線

🔵 **企業建議**：

```mermaid
flowchart TD
    Req[Requirement] --> Threat[Threat Modeling]
    Threat --> Arch[Architecture]
    Arch --> SecCode[Secure Coding]
    SecCode --> SAST[SAST]
    SAST --> DepScan[Dependency Scan]
    DepScan --> UT[Unit Test]
    UT --> SecTest[Security Test]
    SecTest --> DAST[DAST]
    DAST --> Release[Release]
    Release --> Monitor[Monitoring]
```

### 33.2 各階段指定 Agent

| 階段 | 指定 Agent（第 14 章角色） | Prime Agent 官方能力依據 |
|------|-------------------------------|------------------------------|
| Requirement | Architect Agent | RLM 讀取既有文件、釐清問題（第 2 章） |
| Threat Modeling | Security Agent | 依 OWASP 思維列出潛在威脅（🔵 企業建議邏輯，非官方內建威脅建模工具） |
| Architecture | Architect Agent | 產出 ADR（第 55 章） |
| Secure Coding | Backend／Frontend Agent | 遵循 Skill 中定義的安全編碼慣例（第 15 章） |
| SAST | Security Agent | 解讀既有工具報告（第 25 章） |
| Dependency Scan | DevOps Agent | 解讀既有掃描報告 |
| Unit Test | Test Agent | JUnit 5／ArchUnit |
| Security Test | Security/Test Agent | 針對已知威脅撰寫對應測試案例 |
| DAST | DevOps Agent | 解讀既有 DAST 工具結果，Agent 本身不執行滲透測試 |
| Release | 人工核准，Agent 不自主觸發 | 第 30 章 Trust Model |
| Monitoring | Documentation/DevOps Agent 協助產生 Instrumentation | Prime Agent 本身不提供監控能力 |

### 33.3 實務提醒

🔴 **注意**：SSDLC 管線中的 **DAST（動態應用程式安全測試）與 Release** 階段，Prime Agent 的角色應嚴格限定在「輔助分析既有工具輸出」而非「自主執行滲透測試或觸發正式發布」——這兩項都涉及對正式環境或近似正式環境系統的直接操作，違反第 30 章 Trust Model 揭示的風險。

---

## 34. Prime Agent 與 AI Software Development Team

### 34.1 團隊架構

🔵 **企業建議**：

```mermaid
flowchart TD
    Lead["AI Tech Lead（人類主導）"]
    Lead --> ArchA[Architect Agent]
    Lead --> DevAgents[Developer Agents]
    Lead --> QAAgents[QA Agents]
    ArchA --> SecA[Security Agent]
    DevAgents --> FrontA[Frontend Agent]
    DevAgents --> BackA[Backend Agent]
    QAAgents --> TestA[Test Agent]
    ArchA --> DBA[Database Agent]
    DevAgents --> DevOpsA[DevOps Agent]
    QAAgents --> RevA[Review Agent]
    DevAgents --> MigA[Migration Agent]
    QAAgents --> DocA[Documentation Agent]
```

### 34.2 人類角色如何與 Agent Team 協作

| 人類角色 | 與 Prime Agent Team 的協作方式 |
|----------|-----------------------------------|
| PM | 提供高品質、AI 可讀的需求規格（第 35 章） |
| SA | 定義架構約束，審核 Architect Agent 的 ADR 提案 |
| Architect | 定義系統邊界、安全邊界，設定 Quality Gate |
| Tech Lead | 決定何時授權 Autonomous Mode、審核任務拆解是否合理 |
| Developer | 審核各 Sub-agent 產出、負責最終 Code Review |
| QA | 制定測試策略，審核 Test Agent 涵蓋率是否足夠 |
| Security | 審核 Security Agent 的檢查邏輯是否符合企業合規要求 |
| DevOps | 維護 CI/CD 整合（第 28 章），管控 Agent 對部署管線的存取 |

### 34.3 實務提醒

🔵 **企業建議**：「AI Tech Lead」這個角色**不建議由 Agent 自動擔任**——這裡的 AI Tech Lead 概念，指的是「人類 Tech Lead 使用 Prime Agent Team 作為其團隊擴充」，而非把決策權完全交給 Agent。所有跨 Agent 的優先序仲裁、資源分配，仍應由人類 Tech Lead 拍板。

---

## 35. PM／SA／Architect／Developer 工作方式改變

### 35.1 從「人寫 Code，AI 幫忙」到「人設計系統，Agent 執行驗證」

🔵 **企業建議**：AI 時代的軟體開發不是「人寫 Code → AI 幫忙補完」，而是逐漸轉變為：

```text
人設計系統 → Agent 執行 → Agent 驗證 → Agent 自我修正 → 人類審核
```

這個轉變對每個角色都有具體影響：

### 35.2 各角色的轉變

**PM**

- Requirement Quality：需求描述必須足夠具體，能被 Agent 拆解為可驗證的任務（第 52 章 Agent Task Design）
- Acceptance Criteria：驗收標準需明確到可轉化為測試案例
- AI-readable Specification：規格文件應結構化，減少 Agent 需要自行猜測的空間（第 12 章）

**SA**

- Architecture Constraints：把架構約束明確寫下，作為 Architect Agent 提案的邊界條件
- ADR：以 ADR 形式記錄架構決策（第 55 章），讓 Agent 有明確可查詢的決策脈絡
- NFR（非功能需求）：效能、安全、可用性等需求需具體量化，而非模糊描述

**Architect**

- System Boundary：明確定義哪些系統邊界 Agent 可以自主調整、哪些需要人工核准
- Security Boundary：定義 Agent 可存取的資源範圍（第 30、31 章）
- Quality Gate：設計每個階段的驗證關卡（第 18 章 Autonomous Gate）

**Developer**

- Task Decomposition：學習如何把任務拆解成適合 Agent 執行的顆粒度（第 52 章）
- Verification：從「自己寫測試」轉變為「驗證 Agent 產出的測試是否足夠」
- Review：Code Review 的重點從「語法細節」轉向「架構一致性與業務邏輯正確性」

**QA**

- Test Strategy：制定測試策略框架，讓 Test Agent 依循框架產生具體測試
- Quality Gate：定義 Autonomous Mode 的驗證標準（第 18 章）

### 35.3 實務提醒

🔵 **企業建議**：這個轉變不是一蹴可幾的，建議搭配第 37 章的六個導入等級循序漸進，避免要求團隊一次到位跳到「Multi-Agent Development」或「Autonomous Engineering」等級，卻沒有相應的 Governance（第 38 章）與 Quality Gate 基礎。

---

## 36. Prime Agent 與其他 AI Coding Agent 比較

### 36.1 定性比較（不做無依據排名）

🔵 **企業建議**：以下比較僅描述**設計取向與適用情境**，不做「誰最強」的排名（無足夠公開、可比較的一手 benchmark 支持排名結論，第 1.8 節已說明 ARC-AGI-3 數據的解讀限制）。

| 工具 | 核心設計取向 | 較適合的情境 |
|------|--------------|----------------|
| Claude Code | 對話式 + Skills + Sub-agent + Hook 生態 | 團隊已用 Claude、重視 IDE/CLI 整合與生態系外掛 |
| GitHub Copilot | IDE 內建輔助、與 GitHub 生態深度整合 | 以 IDE 內快速輔助、PR 流程整合為主 |
| OpenAI Codex CLI | 對話式 Agent + Sandbox 執行 | 已使用 OpenAI 生態、重視官方 Sandbox |
| Gemini CLI | Google 生態整合 Agent | 已使用 GCP／Gemini 生態 |
| OpenHands | 開源多 Agent 協作框架 | 需要高度客製化的研究型部署 |
| Aider | 輕量終端 Pair-Programming | 小型專案、偏好極簡 CLI 工作流 |
| pi（earendil-works） | 極簡終端 Harness，4 個內建工具起跳，靠 Extensions/Skills/Prompt Templates 擴充 | 團隊想要「工具不綁死工作流」的高度可擴充終端環境 |
| **Prime Agent** | pi 的 Fork + **RLM 程式化 Context** + **Continual Harness 自我演化** | 長時間執行任務（Overnight／Weekend）、大型 Legacy 分析、需要 Agent 自我改進工作方式的場景 |

### 36.2 功能維度對照

| 維度 | Prime Agent | 說明 |
|------|-------------|------|
| RLM／Persistent REPL | 🟢 官方功能 | 核心差異化能力（第 2 章） |
| Continual Harness／自我改進 | 🟢 官方功能 | `/refine` CRUD（第 3、17 章） |
| Memory | 🟢 官方功能（透過 Harness） | 第 16 章 |
| Skills | 🟢 官方功能（Agent Skills 標準 + Python-backed） | 第 15 章 |
| Sub-agent | 🟢 官方功能（`rlm()`） | 第 2、13 章 |
| A2A | 🟢 官方功能（`agent_message`） | 第 2 章 |
| Long-running／Background Session | 🟢 官方功能 | 第 5、6、19 章 |
| Autonomous Mode | 🟢 官方功能 | 第 18 章 |
| CLI | 🟢 官方功能 | 附錄 A |
| MCP | 🟢 官方功能（有限：僅 Linear/Notion 內建，http-only） | 第 27 章 |
| Open Source | 🟢 官方功能（MIT License） | 第 1.1 節 |
| Security Model | 🔴 明確聲明非沙箱 | 第 30 章 |

### 36.3 什麼情境適合什麼工具（🔵 企業建議）

- **已深度導入 Claude Code 生態**（Hook、外掛豐富）：先評估 Prime Agent 的差異化能力（RLM、Continual Harness）是否解決 Claude Code 目前遇不到的痛點，再決定是否並行導入
- **需要長時間、可恢復的 Legacy 分析或 Framework 升級任務**：Prime Agent 的 Daemon／Worker 架構與 Autonomous Gate 設計較貼合此需求
- **已使用 pi**：可視 Prime Agent 為進階擴充而非替代品（第 1.3 節）
- **高度受管制產業、需要嚴格沙箱**：需額外自建第 31 章的 Sandbox Architecture，因為 Prime Agent 本身不提供沙箱

---

## 37. Prime Agent 導入策略

### 37.1 六個導入等級

🔵 **企業建議**：

```mermaid
flowchart LR
    L1["Level 1<br/>個人 Developer"] --> L2["Level 2<br/>AI-assisted Developer"]
    L2 --> L3["Level 3<br/>AI Development Team"]
    L3 --> L4["Level 4<br/>Multi-Agent Development"]
    L4 --> L5["Level 5<br/>Autonomous Engineering"]
    L5 --> L6["Level 6<br/>Enterprise AI SDLC"]
```

### 37.2 各 Level 說明

| Level | 技術 | 流程 | Governance | Risk | KPI |
|-------|------|------|------------|------|-----|
| 1. 個人 Developer | 互動模式、基本 Skill | 無固定流程，個人自由使用 | 無 | 低（個人範圍） | 主觀滿意度 |
| 2. AI-assisted Developer | + Memory、`/refine` | 團隊建議使用時機 | 基本使用規範（第 30 章 Checklist） | 中（機敏資訊誤存） | 採用率 |
| 3. AI Development Team | + Multi-Agent（第 13、14 章） | 標準 Agent Team 角色分工 | Skill／Prompt 治理起步（第 38 章） | 中高（子 Agent 失控） | PR throughput（第 39 章） |
| 4. Multi-Agent Development | + 跨專案 Skill／Memory 共享 | SOP 標準化（第 44 章） | 完整 Registry（第 38 章） | 高（治理複雜度上升） | Rework rate |
| 5. Autonomous Engineering | + Autonomous Mode 大規模使用（第 18 章） | Quality Gate 強制化 | Cost Guardrail（第 40 章） | 高（自主性帶來的風險） | Autonomous completion rate |
| 6. Enterprise AI SDLC | + 完整 SSDLC 整合（第 33 章） | 全公司標準 SOP | 完整 Audit／Compliance | 需持續監控與稽核 | 全套 KPI（第 39 章） |

### 37.3 實務提醒

🔴 **注意**：不建議企業跳級導入——例如尚未建立 Skill／Memory 治理（Level 3 的前提）就直接大規模使用 Autonomous Mode（Level 5），容易在缺乏 Governance 基礎的情況下放大第 58 章列出的常見錯誤風險。

---

## 38. Team Governance

### 38.1 治理項目清單

🔵 **企業建議**：

| 治理項目 | 內容 | 對應章節 |
|----------|------|----------|
| **Agent Registry** | 登記團隊內所有正式使用的 Agent 角色與其職責邊界 | 第 14 章 |
| **Skill Registry** | 登記所有內部 Skill、來源、審查狀態 | 第 15 章 |
| **Prompt Registry** | 集中管理標準 Prompt Template，避免各自為政 | 第 51 章 |
| **Memory Governance** | 定期審視 Memory 內容，移除過期／衝突項目 | 第 16 章 |
| **Model Governance** | 規範哪些任務可用哪些 Provider／Model | 第 9 章 |
| **MCP Governance** | 審查自訂 MCP Server 來源與權限範圍 | 第 27.4 節 |
| **Permission Governance** | Agent 執行環境的權限邊界管理 | 第 30、31 章 |
| **Cost Governance** | Token／模型成本的預算與監控 | 第 40 章 |
| **Audit** | Session 記錄的保存與可稽核性 | 第 6.4 節 |
| **Logging** | 集中蒐集 Agent 執行紀錄供事後查核 | 第 42 章 |

### 38.2 治理組織建議

🔵 **企業建議**：中大型團隊可考慮設立一個小型「AI Agent Governance 小組」，職責包含：

- 審核新 Skill／MCP Server 上線申請
- 定期（如每季）審視 Global Memory 內容
- 追蹤第 39 章 KPI 指標，發現異常時介入
- 維護第 44 章企業標準 SOP 的版本

### 38.3 實務提醒

> 治理不是要限制團隊使用 Prime Agent，而是要讓「大家都可以放心使用」——沒有 Governance 的自由使用，長期反而會累積出難以排查的 Memory 衝突、失控的子 Agent 擴散與不可控的成本（第 58 章常見錯誤有具體案例）。

---

## 39. Agent KPI

### 39.1 可量化 KPI 清單

🔵 **企業建議**：

| KPI | 定義 | 資料來源 |
|-----|------|----------|
| Lead Time | 從需求提出到功能上線的總時間 | 既有專案管理工具 + Session 記錄 |
| Cycle Time | 從開始實作到完成的時間 | Session 起訖時間 |
| PR Throughput | 單位時間內完成並合併的 PR 數量 | Git／GitHub |
| Defect Rate | Agent 協助產出的程式碼上線後的缺陷率 | 既有缺陷追蹤系統 |
| Test Coverage | Agent 補齊測試後的整體覆蓋率變化 | 既有覆蓋率工具 |
| Security Findings | Security Agent 發現並修正的高風險項目數 | 第 25 章審查記錄 |
| Rework | 因 Agent 產出品質不足而需要重做的比例 | PR Review 記錄 |
| Token Usage | 各任務類型的 Token 消耗量 | Provider 帳單／用量 API |
| Cost | 對應的實際費用 | 第 40 章 |
| Autonomous Completion Rate | Autonomous Task 成功達成目標而未中途失敗的比例 | Session 記錄 |
| Human Intervention Rate | 需要人工中途介入（`attach` 後修正方向）的任務比例 | 第 6 章 Session 記錄 |
| Rollback Rate | `/refine` 或 Git 變更需要回滾的比例 | 第 3、29 章記錄 |

### 39.2 KPI 使用原則

🔵 **企業建議**：

- KPI 應作為**趨勢觀察**工具，而非個人績效考核依據——過早把 Token Usage 或 PR Throughput 直接掛鉤個人考核，容易誘發「為了 KPI 而濫用 Autonomous Mode」等反效果
- Autonomous Completion Rate 偏低時，優先檢查是否為 Gate 設計不當（第 18.4 節），而非直接歸咎於模型能力不足
- Rollback Rate 偏高時，應回頭檢視 `/refine` 審核流程（第 17.3 節）是否確實執行

---

## 40. Cost Management

### 40.1 成本構成

🔵 **企業建議**：

| 成本項目 | 說明 |
|----------|------|
| Token（輸入／輸出） | 依 Provider 計費模式而定（第 9 章） |
| Model Cost | 不同模型單價差異大，`--thinking` 等級也影響成本 |
| Sub-agent Cost | 每個 `rlm()` 產生的子 Agent 都會消耗獨立的 Token 額度 |
| Parallel Agent Cost | 多個子 Agent 平行執行時成本會同時發生，而非攤提 |
| Long-running Cost | Overnight／Weekend 任務可能累積可觀的 Token 用量 |
| Autonomous Cost | 多輪自動延續（`--autonomous-max-continuations`）會放大成本 |

### 40.2 Cost Guardrail 設計

🔵 **企業建議**：

```text
Daily Budget：團隊每日 Token／費用上限
Per Task Budget：單一任務的預算上限
Per Agent Budget：單一 Sub-agent 的預算上限
Per Model Budget：不同模型分別設定的預算池
Timeout：--autonomous-timeout-ms（第 18.2 節）
Max Turns：--autonomous-max-turns（第 18.2 節）
Max Tokens：--autonomous-max-tokens（第 18.2 節）
```

🟢 **官方功能基礎**：`--autonomous-max-tokens`、`--autonomous-max-turns`、`--autonomous-timeout-ms` 皆為官方確認的真實旗標（第 18.2 節），是企業落實 Cost Guardrail 最直接可用的工具；Daily／Per Task／Per Agent／Per Model Budget 則需搭配企業自建的用量監控（多數 Provider 有對應的用量 API）。

### 40.3 實務提醒

🔵 **企業建議**：不同任務型態應搭配不同的預設 Guardrail——日常快速問答可用較低的 `--thinking` 等級與較短的 `--autonomous-timeout-ms`；大型 Framework Upgrade（第 21、22 章）則可放寬預算但務必搭配第 19.4 節建議的心跳監控，避免成本在無人察覺的情況下持續累積。

---

## 41. Troubleshooting

### 41.1 診斷方法論

🔵 **企業建議**：遇到問題時，優先順序建議為：

1. `prime-agent status` 確認 Daemon／Worker 是否存活
2. `prime-agent doctor`（必要時加 `--fix`）進行自動診斷
3. `prime-agent agents` 確認相關 Session 狀態
4. 查看 Session JSONL 記錄還原問題發生的完整脈絡（第 6 章）

### 41.2 症狀 → 原因 → 診斷 → 解決方案

**安裝失敗**

- 症狀：`curl` 安裝腳本執行後找不到 `prime-agent` 指令
- 原因：PATH 未正確更新，或企業內網無法連外
- 診斷：確認 Shell 設定檔（`.bashrc`／`.zshrc`）是否已載入安裝路徑；`echo $PATH` 檢查
- 解決方案：重新開啟終端機；若為網路限制，改用第 7.4 節原始碼安裝

**PATH 問題**

- 症狀：指令時有時無（例如新開的終端機找不到）
- 原因：PATH 只在特定 Shell 設定檔中生效
- 診斷：檢查 `~/.bashrc`、`~/.zshrc`、`~/.profile` 是否都有對應設定
- 解決方案：統一寫入團隊標準的 Shell 設定檔範本

**Python 問題**

- 症狀：Kernel 啟動失敗，提示找不到 Python 套件
- 原因：`~/.prime/agent/kernel-venv` 建立失敗或損毀
- 診斷：`prime-agent doctor`
- 解決方案：`prime-agent doctor --fix`；仍失敗則手動刪除 `kernel-venv` 目錄讓其重新建立

**IPython 問題**

- 症狀：REPL 執行 Python 程式碼時卡住或報錯
- 原因：Kernel 行程異常
- 診斷：`prime-agent status` 確認 Worker 狀態
- 解決方案：`prime-agent stop <agent>` 後重新啟動任務

**Provider Authentication／API Key**

- 症狀：`/login` 後仍提示未授權
- 原因：API Key 環境變數未正確設定，或訂閱已過期
- 診斷：檢查對應環境變數是否存在且未過期（第 9 章）
- 解決方案：重新設定環境變數；重新執行 `/login`

**Session 問題**

- 症狀：`prime-agent attach` 找不到指定 Session
- 原因：Session ID／名稱錯誤，或 Session 已被清理
- 診斷：`prime-agent agents`／`prime-agent list --all` 確認實際存在的 Session
- 解決方案：使用正確的 Session 識別碼；日後養成 `rename` 習慣方便辨識（第 6.2 節）

**Daemon 問題**

- 症狀：`prime-agent status` 顯示 Daemon 未回應
- 原因：Daemon 行程異常終止
- 診斷：檢查系統行程列表是否仍有殘留的 Daemon 行程
- 解決方案：`prime-agent shutdown --force` 後重新執行指令觸發 Daemon 重啟

**Worker Crash**

- 症狀：任務執行到一半無回應
- 原因：Worker 行程當機（第 5.3 節 Crash Recovery）
- 診斷：`prime-agent agents` 檢查該 Session 狀態
- 解決方案：`prime-agent -r/--resume` 嘗試恢復；若持續失敗，檢查是否為 Gate 指令本身有問題

**Kernel Crash**

- 症狀：Python REPL 狀態遺失，變數需要重新賦值
- 原因：Kernel 行程重啟
- 診斷：查看 Session JSONL 中 Kernel 重啟前後的紀錄
- 解決方案：關鍵中間結果應盡早透過 `/refine` 沉澱為 Memory，降低 Kernel 重啟造成的損失

**MCP 問題**

- 症狀：MCP 工具呼叫失敗
- 原因：OAuth 授權過期，或使用了不支援的 `stdio` 傳輸（第 27.2 節）
- 診斷：`/mcp login <name>` 檢查授權狀態
- 解決方案：重新授權；確認自訂 MCP Server 是 `http` 傳輸

**Skill 問題**

- 症狀：Skill 未被載入或呼叫
- 原因：`SKILL.md` frontmatter 格式錯誤，或路徑不在搜尋範圍（第 15.3 節）
- 診斷：檢查 `name` 是否與資料夾名稱相符、`description` 是否超過長度限制
- 解決方案：修正 frontmatter；用 `/skill:name` 強制指定測試

**Sub-agent 問題**

- 症狀：`rlm()` 呼叫後子 Agent 沒有回應
- 原因：誤以為 `rlm()` 會同步回傳結果（第 2.3.1 節常見誤解）
- 診斷：`await rlm.list_subagents()` 確認子 Agent 是否確實被建立
- 解決方案：透過 `agent_message` 或查看子 Agent `session_dir` 取得實際進度

**Context Compaction**

- 症狀：長任務中 Agent 似乎「忘記」較早的對話內容
- 原因：Context 壓縮（`compact` skill，第 19.3 節）行為
- 診斷：檢視 Session 記錄中的 compaction 事件
- 解決方案：重要決策應盡早透過 `/refine` 沉澱，而非依賴長 Context 記憶

**Autonomous Task 停止**

- 症狀：Autonomous Task 提早結束
- 原因：達到 `--autonomous-max-turns`／`--autonomous-timeout-ms` 上限，或 Gate 連續失敗達 `--autonomous-gate-retries` 上限
- 診斷：檢視 Session 記錄找出 Gate 失敗原因
- 解決方案：修正根本原因而非單純調高上限（第 18.4 節）

**Git 問題**

- 症狀：Agent 產生的變更與既有分支衝突
- 原因：未在獨立分支上操作，或分支已過期
- 診斷：`git status`、`git log` 確認目前分支狀態
- 解決方案：遵循第 29 章 Git 工作流程，確保每次任務都在獨立分支上進行

**Permission 問題**

- 症狀：Agent 執行 Shell 指令時被拒絕存取
- 原因：啟動 Prime Agent 的使用者帳號權限不足（或刻意限制，見第 31 章）
- 診斷：確認執行環境的實際 OS 權限
- 解決方案：依第 30、31 章原則調整權限範圍，而非直接授予過高權限

完整速查表版本見附錄 E。

---

## 42. 維運

### 42.1 日常維運指令

🟢 **官方功能**：

```bash
prime-agent update          # 更新到最新版本（第 43 章升級策略）
prime-agent doctor          # 診斷環境問題
prime-agent status          # 查看 Daemon／Worker 狀態
prime-agent shutdown        # 關閉背景 Daemon
```

### 42.2 Logs

🔵 **企業建議**：雖然官方文件未提供獨立的 `logs` 子指令，Session JSONL（第 6 章）本身即是最完整的執行記錄來源。企業可建立簡單的腳本，定期彙整各專案的 Session JSONL 供集中查閱。

### 42.3 Session Cleanup 與 Disk Usage

🔵 **企業建議**：長期使用下，`~/.prime/agent/` 目錄下的 Session 記錄與 Harness 狀態會持續累積：

- 定期（如每季）檢視 `prime-agent list --all` 的輸出，評估是否需要封存或清理過舊的 Session
- 清理前務必確認沒有尚未沉澱為 Memory 的重要決策
- 關注磁碟用量，尤其是包含大量子 Agent 的長任務可能累積大量 Session 檔案

### 42.4 Artifact Management、Backup 與 Recovery

🔵 **企業建議**：

- 將 `~/.prime/agent/harness/`（Global Harness 狀態）納入團隊共用的備份範圍，避免單一開發者機器損毀導致累積的團隊知識遺失
- 專案層級的 Harness 狀態（`harness/harness_state.json`）建議隨專案一起納入版本控制的備份策略考量（但需注意內容是否含機敏資訊，第 16.2 節）
- 制定簡單的 Recovery SOP：新機器上重新安裝 Prime Agent 後，如何還原團隊共用的 Skill／Memory

---

## 43. 升級策略

### 43.1 升級流程

🔵 **企業建議**：

```mermaid
flowchart TD
    Current[Current Version] --> Notes[Release Notes]
    Notes --> Compat[Compatibility Check]
    Compat --> Backup[Backup]
    Backup --> Upgrade[Upgrade]
    Upgrade --> Smoke[Smoke Test]
    Smoke --> Regression[Regression Test]
    Regression -->|失敗| Rollback[Rollback]
    Regression -->|通過| Done[完成]
```

### 43.2 實際指令

```bash
# 🟢 官方功能
prime-agent update
prime-agent update --force
```

- **用途**：`update` 更新到最新版本；`--force` 強制重新安裝
- **使用時機**：定期升級週期，或需要新版本功能／修補時
- **常見錯誤**：企業網路限制時更新失敗，處理方式見第 7.4 節

🔴 **注意**：官方 CLI 未提供內建的版本回滾指令；🔵 **企業建議**：升級前先記錄目前版本號（`prime-agent --version`），若升級後出現問題，可透過第 7.4 節的原始碼安裝方式，`git checkout` 到指定版本 tag 重新建置作為回滾手段。

### 43.3 升級檢查清單

🔵 **企業建議**：

- [ ] 閱讀 GitHub Releases 的版本說明，確認是否有 Breaking Change
- [ ] 確認自訂 Skill／MCP 整合在新版本下是否仍相容
- [ ] 先在非關鍵專案／測試環境驗證
- [ ] 團隊內部公告升級時間與已知變更
- [ ] 升級後執行團隊常用的 Smoke Test（如跑一次第 10 章的第一個專案分析流程）

---

## 44. 企業標準 SOP

### 44.1 SOP 總覽

🔵 **企業建議**：以下十項 SOP 涵蓋企業導入 Prime Agent 的主要工作情境。

| SOP 編號 | 名稱 | 對應章節 |
|----------|------|----------|
| SOP-01 | 新專案初始化 | 第 10 章 |
| SOP-02 | Legacy Analysis | 第 20 章 |
| SOP-03 | Framework Upgrade | 第 21、22 章 |
| SOP-04 | Bug Fix | 第 25 章 |
| SOP-05 | Feature Development | 第 11 章 |
| SOP-06 | Code Review | 第 25 章 |
| SOP-07 | Security Review | 第 30 章 |
| SOP-08 | Autonomous Task | 第 18 章 |
| SOP-09 | Long-running Task | 第 19 章 |
| SOP-10 | Agent Self-Improvement | 第 17 章 |

### 44.2 SOP 範例：SOP-03 Framework Upgrade

🔵 **企業建議**：

1. **Objective**：在不破壞既有功能的前提下完成框架版本升級
2. **Input**：目標版本、現有專案原始碼、既有測試套件
3. **Process**：依第 21 章標準作業流程執行
4. **Agent**：Migration Agent 主導，Backend/Test/Security Agent 協作
5. **Tools**：`prime-agent --autonomous --autonomous-gate ...`
6. **Output**：升級後的程式碼、升級報告
7. **Quality Gate**：編譯成功、既有測試全數通過、Security Agent 無新增高風險發現
8. **Risk**：Breaking Change 遺漏、效能劣化
9. **Rollback**：Git 分支未合併前皆可捨棄；已合併則需個別評估回退成本

### 44.3 Prime Agent Development Standard（PA-001~010）

🔵 **企業建議**：除 SOP 之外，另建立以任務類型為軸心的工作標準，兩者可交互參照：

| 標準編號 | 名稱 | Objective |
|----------|------|-----------|
| PA-001 | Project Analysis | 建立專案 Architecture Map 與基礎 Memory |
| PA-002 | Architecture Analysis | 產出／更新 ADR |
| PA-003 | Task Planning | 拆解任務為可驗證顆粒度 |
| PA-004 | Coding | Sub-agent 實作，遵循既有慣例 |
| PA-005 | Testing | 補齊測試涵蓋率 |
| PA-006 | Security | 依 OWASP 檢查高風險項目 |
| PA-007 | Review | Multi-Agent Review 彙整 |
| PA-008 | Refine | `/refine` 沉澱經驗 |
| PA-009 | Autonomous | 設定 Gate 後啟動自主執行 |
| PA-010 | Release | 人工核准後觸發既有發布流程 |

每項標準的完整格式（Objective／Input／Process／Agent／Tools／Output／Quality Gate／Risk／Rollback）與 SOP-03 範例相同，企業可依此格式為 PA-001~010 逐一補齊團隊專屬細節。

---

## 45. 實戰案例一：建立 Vue 與 Spring Boot 系統

### 45.1 情境

🔵 **企業建議實戰案例**：從零開始建立一個訂單管理系統，技術棧沿用第 11.3 節的企業標準棧。

### 45.2 步驟一：Architecture 規劃

```bash
mkdir order-management-system && cd order-management-system
git init
prime-agent
```

```text
# 🔵 企業建議 Prompt
請為一個訂單管理系統規劃初始架構：
- Frontend：Vue 3 + TypeScript + Tailwind CSS + PrimeVue + Pinia
- Backend：Java 25 + Spring Boot 4.x + Maven 4.x，採 Clean Architecture 分層
- Database：PostgreSQL
產出目錄結構建議與各層職責說明，先不要建立任何檔案，等我確認架構後再繼續。
```

**預期產出（示意）**：Agent 會回傳一份分層目錄結構建議（如 `domain/`、`application/`、`infrastructure/`、`interfaces/`）與各層職責說明，並在結尾詢問是否可以開始建立骨架。

### 45.3 步驟二：Multi-Agent 分工建立骨架

```text
# 🔵 企業建議 Prompt（架構確認後）
架構已確認，請用 rlm() 分工：
1. 一個子 Agent 建立 Backend 專案骨架（Maven 4 + Spring Boot 4 + 分層目錄）
2. 一個子 Agent 建立 Frontend 專案骨架（Vue 3 + Vite + TypeScript + PrimeVue + Tailwind + Pinia）
3. 一個子 Agent 撰寫 PostgreSQL 初始 Schema（訂單、訂單明細、客戶三張表）
完成後回報各自產出的檔案清單。
```

### 45.4 步驟三：實作第一個 API

```text
# 🔵 企業建議 Prompt
在 Backend 新增「建立訂單」API：POST /api/orders，
遵循 Controller → Service → Repository 分層，並補上對應的 JUnit 5 測試（含成功與驗證失敗情境）。
```

### 45.5 步驟四：安全與文件

```text
# 🔵 企業建議 Prompt
1. 依 security-review Skill（第 15.5 節）檢查剛才新增的 API
2. 產出這次新增功能的簡短技術文件（API 說明、資料模型變更）
```

### 45.6 步驟五：`/refine` 沉澱

```bash
/refine 把這個專案的分層慣例、Build/Test 指令記錄為 Memory，供後續功能開發沿用
```

### 45.7 小結

這個案例完整走過「規劃 → 平行建骨架 → 實作 → 安全檢查 → 文件 → 沉澱」的流程，對應第 10 章的最小流程與第 11 章的完整 SDLC Workflow，是團隊導入 Prime Agent 時建議的第一個練習專案。

---

## 46. 實戰案例二：Spring Boot 3 升級到 4

### 46.1 情境

🔵 **企業建議實戰案例**：延續第 22 章的指令範例，本節示範一次完整的執行過程與預期輸出結構。

### 46.2 步驟一：分析

```bash
cd legacy-order-service
prime-agent "分析目前專案對 Spring Boot 4.x 與 Java 25 的相容性風險，
產出分階段升級計畫，在計畫經人工確認前不要修改任何檔案"
```

**預期輸出結構（示意）**：

```markdown
## 相容性風險摘要
| 風險項目 | 影響範圍 | 嚴重度 |
|----------|----------|--------|

## 分階段升級計畫
### 階段一：Jakarta 命名空間遷移
### 階段二：設定檔調整
### 階段三：相依套件版本升級
### 階段四：程式碼相容性修正
```

### 46.3 步驟二：人工確認後執行 Autonomous 遷移

```bash
git checkout -b upgrade/spring-boot-4

prime-agent \
  --autonomous \
  --autonomous-gate "mvn -q clean compile" \
  --autonomous-gate "mvn -q test" \
  --autonomous-max-turns 30 \
  --autonomous-timeout-ms 7200000 \
  "依照先前確認的升級計畫，逐步執行階段一到階段四，每完成一階段確保 Gate 通過後才繼續"
```

### 46.4 步驟三：追蹤進度

```bash
# 另開終端機或稍後查看
prime-agent agents
prime-agent attach <agent-name>
```

### 46.5 步驟四：Review 與合併

```text
# 🔵 企業建議 Prompt
請 Reviewer Agent 彙整這次升級的所有變更，產出給人類審核者的摘要，
標明每個階段做了什麼變更、通過了哪些 Gate、是否有需要額外注意的地方。
```

人工審核通過後，依第 29 章 Git 工作流程建立 PR，**不自動 push main、不自動 merge**。

### 46.6 小結

此案例展示了「分析 → 人工確認計畫 → Autonomous 執行 → 人工 Review → PR」的完整升級流程，是第 21 章標準作業流程的具體落地示範。

---

## 47. 實戰案例三：Legacy Java Reverse Engineering

### 47.1 情境

🔵 **企業建議實戰案例**：延續第 20 章工作流，本節示範一個 Legacy EJB 專案的完整逆向分析過程。

### 47.2 步驟一：啟動平行分析

```bash
cd legacy-insurance-claim-system
prime-agent
```

```text
# 🔵 企業建議 Prompt（同第 20.3 節，此處展示完整執行過程）
這是一個 Legacy Java EJB 專案。請依以下方式分工分析，各自用子 Agent 平行進行：
1. 一個子 Agent 負責找出所有對外 API 進入點
2. 一個子 Agent 負責分析所有 Oracle 資料庫存取程式碼與交易邊界
3. 一個子 Agent 負責分析批次作業、FTP、MQ 等外部整合點
4. 一個子 Agent 負責掃描明顯的安全風險
在完成分析前，不要修改任何檔案。
```

### 47.3 步驟二：監控平行子 Agent 進度

```python
# 🟢 官方功能：查詢目前有哪些子 Agent 在執行
children = await rlm.list_subagents()
for c in children:
    print(c.name, c.session_dir)
```

### 47.4 步驟三：彙整報告

```text
# 🔵 企業建議 Prompt
請彙整四個子 Agent 的分析結果，產出：Architecture Map、Dependency Map、
Database Map、API Map、Risk Map、Migration Map（第 20.4 節格式）。
```

### 47.5 步驟五：人工審核與後續規劃

🔴 **注意**：Risk Map 與 Migration Map 屬於分析建議，須經 Architect／資深工程師人工確認後，才能作為後續第 24 章 Legacy Modernization 的輸入。

### 47.6 小結

此案例展示了 Multi-Agent 平行分析大型 Legacy 系統的完整流程，是第 2、13 章 RLM／Multi-Agent 概念在真實企業場景中的具體應用。

---

## 48. 實戰案例四：長時間 Autonomous Refactoring

### 48.1 情境

🔵 **企業建議實戰案例**：週五下班前啟動一個跨週末執行的大型重構任務。

### 48.2 步驟一：設定 Goal 與心跳

```bash
prime-agent \
  --autonomous \
  --autonomous-gate "mvn -q clean compile" \
  --autonomous-gate "mvn -q test" \
  --autonomous-max-turns 100 \
  --autonomous-max-tokens 2000000 \
  --autonomous-timeout-ms 259200000 \
  --goal "把 OrderModule 從交易腳本模式重構為領域模型模式，逐步進行並保持每個 commit 都可編譯、測試通過" \
  "開始重構，第一步請先建立 Characterization Test 鎖定現有行為"
```

🔴 **注意**：`--autonomous-timeout-ms 259200000` 約為 72 小時（週五晚上到週一早上），此數值需依團隊實際需求審慎評估，並非官方建議值。

### 48.3 步驟二：週末心跳監控

```bash
# 🟢 官方功能：互動模式下設定（若透過 attach 進入該 Session）
/heartbeat every 4h 回報目前重構進度、已完成的 Characterization Test 數量、遇到的問題
```

🔵 **企業建議**：搭配團隊的通知機制（如將心跳輸出轉發到 Slack／Email），讓負責人週末也能收到異常提醒，而不需要主動盯著終端機。

### 48.4 步驟三：週一檢視

```bash
prime-agent agents
prime-agent attach <agent-name>
```

```text
# 🔵 企業建議 Prompt
請總結整個週末的重構進度：完成了哪些階段、目前的測試涵蓋率變化、
是否有中途卡住重試多次的部分、以及你認為還需要多少時間完成剩餘工作。
```

### 48.5 步驟四：`/refine` 沉澱長任務經驗

```bash
/refine 這次長時間重構任務中，哪些判斷是有效的、哪些走了彎路，
請把有效的重構模式記錄為 Memory，供之後類似任務參考
```

### 48.6 小結

此案例展示第 5、19 章介紹的 Daemon／Worker 持久化架構與心跳機制，如何支撐一個真正跨越非工作時間的長任務，同時透過第 18 章的 Gate 機制確保即使無人看管，每個階段仍是可驗證的穩定點。

---

## 49. 實戰案例五：Multi-Agent Code Review

### 49.1 情境

🔵 **企業建議實戰案例**：延續第 25 章流程，示範一個完整 PR 的多 Agent 審查。

### 49.2 步驟一：啟動審查

```mermaid
flowchart TD
    MainAgent[Main Agent] --> ArchA[Architecture Agent]
    MainAgent --> SecA[Security Agent]
    MainAgent --> TestA[Test Agent]
    MainAgent --> PerfA[Performance Agent]
    MainAgent --> QualA[Code Quality Agent]
    ArchA --> RevA[Reviewer Agent]
    SecA --> RevA
    TestA --> RevA
    PerfA --> RevA
    QualA --> RevA
```

```python
# 🔵 企業建議寫法，API 呼叫本身為 🟢 官方功能
reviewers = {
    "architecture": "檢查這次 PR 是否違反既有分層原則與 ArchUnit 規則",
    "security": "依 OWASP Top 10 檢查這次 PR 的新增程式碼",
    "test": "檢查測試涵蓋率是否涵蓋新增邏輯的主要路徑與邊界情境",
    "performance": "檢查是否引入明顯的效能風險（如 N+1 查詢、不必要的巨量物件複製）",
    "quality": "檢查程式碼可讀性、是否有重複邏輯可以抽取",
}

handles = {}
for role, task in reviewers.items():
    handles[role] = await rlm(f"針對這次 PR 的變更：{task}", name=f"{role}-review")
```

### 49.3 步驟二：彙整

```text
# 🔵 企業建議 Prompt
請 Reviewer Agent 彙整五個審查子 Agent 的結果，去除重複發現，
依嚴重度排序，並標明「建議必須修正」與「建議可選」兩類，
最後產出一份給人類審核者的單一摘要。
```

### 49.4 步驟三：人工核准

🔴 **注意**：彙整結果仍以 PR 評論形式呈現給人類審核者，最終的 Approve／Request Changes 決策由人類做出（第 25.4 節）。

### 49.5 小結

此案例展示第 13 章 Multi-Agent Architecture 在 Code Review 場景的具體實作，五個審查視角平行執行後由 Reviewer Agent 統整，避免人類審核者需要逐一切換不同檢查工具的脈絡轉換成本。

---

## 50. 常用 Prompt Library

🔵 **企業建議**：以下 Prompt 皆可直接複製使用，純文字版本另見附錄 C。

**1. Project Analysis Prompt**

```text
請分析目前這個專案：建立整體 Architecture Map、列出主要模組與相依關係、
找出實際的 Build/Test 指令、摘要程式碼風格慣例、掃描明顯安全風險。
在完成分析前，不要修改任何檔案。
```

**2. Architecture Prompt**

```text
根據目前的需求與既有架構慣例，提出符合 Clean Architecture／Hexagonal Architecture 的實作方式，
標記出需要人工決策的架構取捨點，並說明各選項的優缺點。在決策確認前不要開始實作。
```

**3. Reverse Engineering Prompt**

```text
這是一個 Legacy 系統，請拆分子 Agent 平行分析：對外 API 進入點、資料庫存取與交易邊界、
外部整合點（批次/FTP/MQ）、安全風險。彙整成 Architecture Map、Dependency Map、
Database Map、API Map、Risk Map、Migration Map。在完成分析前不要修改任何檔案。
```

**4. Framework Upgrade Prompt**

```text
分析目前專案對 [目標框架版本] 的相容性風險，產出分階段升級計畫，
在計畫經人工確認前不要修改任何檔案；計畫需包含每個階段的驗證方式。
```

**5. Security Review Prompt**

```text
依 OWASP Top 10 檢查本次變更的程式碼，標記高風險項目與嚴重度，
附上檔案路徑、行號、風險說明與修正建議。只產出報告，不自動修改程式碼。
```

**6. Database Migration Prompt**

```text
分析 [來源資料庫] Schema 定義，產出遷移到 [目標資料庫] 的對照計畫：
型別對照、Stored Procedure 轉換策略、索引策略、需要人工確認的邊界案例。
在產出遷移計畫前，不要修改任何檔案。
```

**7. Code Review Prompt**

```text
針對這次 PR 的變更，分別從架構一致性、安全性、測試涵蓋率、效能風險、程式碼品質五個角度審查，
彙整成一份依嚴重度排序、區分「必須修正」與「建議可選」的摘要。
```

**8. Test Generation Prompt**

```text
為 [目標類別/函式] 補齊 JUnit 5 單元測試，確保涵蓋主要成功路徑與至少一個邊界／失敗情境，
測試命名與既有測試慣例保持一致。
```

**9. Autonomous Task Prompt**

```text
[明確、可驗證的任務目標]。在達成目標前，每個階段都要通過指定的 Gate 驗證，
若連續失敗達重試上限，停止並回報目前狀態與失敗原因，不要嘗試繞過驗證。
```

**10. Long-running Task Prompt**

```text
[長任務目標描述]。請每 [時間間隔] 回報一次目前進度、已完成的階段、遇到的問題，
並在每個階段完成後確保處於可編譯、可測試通過的穩定狀態。
```

**11. Sub-agent Prompt**

```text
請針對 [任務清單] 分別派子 Agent 平行處理，每個子 Agent 完成後回報結果，
最後由你彙整成一份總表，標記彼此之間是否有不一致或需要協調的地方。
```

**12. Skill Creation Prompt**

```text
請為 [特定重複性任務] 建立一個新的 Skill：name 為 [skill-name]，
description 需清楚描述何時該被觸發，內文需包含具體的執行步驟與輸出格式要求。
```

**13. Memory Creation Prompt**

```text
/refine 把剛才確認的 [具體事實/慣例] 記錄為這個專案的 Memory，
記錄前請先確認這是已驗證的事實而非推測，並檢查是否與既有 Memory 衝突。
```

**14. Refinement Prompt**

```text
/refine 這次任務中你觀察到 [具體觀察]，請評估是否需要更新 Memory／Skill／
Sub-agent 規格，並說明每項建議變更的具體理由。
```

**15. Release Verification Prompt**

```text
對照本次變更的原始規格文件，逐項確認實作是否完整覆蓋：功能需求、非功能需求、
API 契約、測試涵蓋率、安全檢查結果。以表格輸出「規格項目 → 是否完成 → 驗證方式」，
標記出任何未完成或需要人工確認的項目。
```

---

## 51. Prime Agent Prompt Engineering

### 51.1 標準 Prompt 結構

🔵 **企業建議**：不要只告訴 Agent「幫我寫 Code」，應該使用結構化的 Prompt Template：

```text
Context：目前的背景與既有狀態
Goal：明確的目標
Constraints：限制條件（不可修改哪些檔案、不可使用哪些做法）
Architecture：需要遵循的架構原則
Inputs：任務的輸入是什麼
Outputs：期望的輸出格式
Verification：如何驗證任務是否完成
Quality Gate：需要通過哪些檢查
Rollback：若出錯如何回復
```

### 51.2 範例

```text
Context：這是一個使用 Clean Architecture 的 Spring Boot 4 專案，OrderService 目前缺少退款邏輯。
Goal：新增退款功能，符合現有交易邊界規則。
Constraints：不可修改既有的 OrderService 公開介面簽名；不可直接操作 Production 資料庫。
Architecture：遵循 Controller → Service → Repository 分層，交易邊界在 Service 層。
Inputs：現有 OrderService、OrderRepository 原始碼。
Outputs：新增的 RefundService、對應的單元測試。
Verification：mvn test 全數通過；新增測試涵蓋成功與失敗情境。
Quality Gate：編譯成功、測試通過、Security Agent 無新增高風險發現。
Rollback：變更限定在獨立分支，未合併前可直接捨棄分支。
```

### 51.3 實務提醒

🔵 **企業建議**：這個模板不需要每次都逐項填寫，但**任務越複雜、風險越高，越應該完整使用**。日常小型任務可簡化，但 Autonomous Task（第 18 章）與長任務（第 19 章）建議一律使用完整模板。

---

## 52. Agent Task Design

### 52.1 Bad Task vs Good Task

🔵 **企業建議**：

**Bad Task**

```text
Upgrade this project.
```

**Good Task**

```text
Analyze the current Spring Boot project, identify all compatibility risks against
Spring Boot 4.x, produce a migration plan, do not modify files until the plan is
reviewed, and provide a verification strategy.
```

### 52.2 為什麼 Bad Task 會出問題

| 問題 | 說明 |
|------|------|
| 缺少明確目標 | Agent 無法判斷「升級」的範圍與完成標準 |
| 缺少驗證方式 | 無法設計對應的 Autonomous Gate |
| 缺少限制條件 | Agent 可能直接開始修改檔案，缺乏人工確認關卡 |
| 顆粒度過大 | 難以拆解為可獨立驗證的子任務 |

### 52.3 任務拆解原則

🔵 **企業建議**：

1. 每個子任務應有明確、可驗證的完成標準
2. 子任務之間的依賴關係應該清楚（哪些可以平行、哪些必須循序）
3. 高風險操作（刪除、大規模重寫）應拆成獨立、可單獨審核的任務
4. 每個任務都應該可以回答「怎麼知道這個任務做完了」

---

## 53. Context Engineering

### 53.1 核心概念

🔵 **企業建議延伸自官方 RLM 概念**（第 2 章）：Context Engineering 探討的是「如何讓 Agent 在有限的注意力資源下，看到最相關的資訊」，涵蓋：

| 概念 | 說明 |
|------|------|
| Context | 當前對話與任務中，模型實際可見的資訊 |
| Context Window | 模型單次可處理的最大 token 數量 |
| Compaction | 對過長 Context 進行壓縮的機制（第 19.3 節 `compact` skill） |
| Externalized Context | 把資訊儲存在 Context 之外（如 Memory、檔案系統），需要時才讀取 |
| Persistent State | Session／Harness 狀態的持久化（第 3、6 章） |
| Memory | 長期沉澱的知識（第 16 章） |
| Skill | 隨需載入的能力描述（第 15 章） |
| Prompt | 當次任務的具體指示 |
| Session | 一次任務的完整脈絡（第 6 章） |
| Sub-agent | 把部分工作外包給獨立 Context 的子 Agent（第 2、13 章） |

### 53.2 為什麼 RLM 能降低 Token 消耗

🟢 **官方功能**：如第 2.2 節所述，Prime Intellect 官方指出 Prime Agent 可以「透過程式化函數直接處理資料，而不是把所有資料都轉成 token 後交給模型閱讀」。具體體現在：

- 用 Python 篩選／彙總大量資料後，只把**摘要結果**放進模型的 Context，而非原始全量資料
- 用 `rlm()` 把大任務拆給子 Agent，每個子 Agent 只需要處理**自己那部分**的 Context，而非整個任務的全部資訊
- Memory／Skill 採漸進式揭露（Metadata 常駐、完整內容隨需載入），避免所有可能用到的知識都塞進每次的 Context

### 53.3 企業實務原則

🔵 **企業建議**：

1. 大型檔案分析優先用 RLM 程式化篩選，而非要求 Agent 一次讀完整份檔案
2. 長任務中反覆用到的知識，及早透過 `/refine` 沉澱為 Memory，而非每次都重新放進 Context
3. Multi-Agent 分工時，明確界定每個子 Agent 需要的 Context 範圍，避免不必要的資訊重疊

---

## 54. RLM Programming Tutorial

🔴 **注意**：以下 API 需以目前 Prime Agent 官方文件與原始碼為準；次版本間可能調整簽名或行為。本章教學循序漸進，從最基本的 Python 執行到完整 Multi-Agent workflow。

### 54.1 第一步：基本 Python 執行

```python
# 🟢 官方功能：在 Prime Agent 的持久化 IPython Kernel 中執行
print("Hello")
```

**說明**：Prime Agent 的核心互動環境是一個持久化 IPython Kernel（第 4、5 章），這代表你可以直接在其中執行 Python 程式碼，狀態會保留到下一次互動。

### 54.2 第二步：使用標準函式庫

```python
# 🟢 官方功能
import os
files = os.listdir(".")
print(files)
```

**輸入**：無（讀取目前工作目錄）
**輸出**：目前目錄下的檔案清單
**為什麼 Agent 要這樣做**：與其要求模型「用文字描述目前目錄下有哪些檔案」（容易產生幻覺），不如直接執行程式碼取得確定性的結果。

### 54.3 第三步：讀取並處理專案檔案

```python
# 🟢 官方功能
import os

java_files = []
for root, dirs, files in os.walk("src/main/java"):
    for f in files:
        if f.endswith(".java"):
            java_files.append(os.path.join(root, f))

print(f"共找到 {len(java_files)} 個 Java 檔案")
```

**實務用途**：這是第 20 章 Reverse Engineering 中「Project Structure 分析」步驟的基礎程式化實作方式——先用程式碼取得確定性的檔案清單，而非要求模型憑印象猜測。

### 54.4 第四步：呼叫 `rlm()` 產生子 Agent

```python
# 🟢 官方功能
handle = await rlm(
    "分析這份 Java 檔案清單中，哪些類別名稱看起來像是 Controller 層",
    name="controller-scan",
)
print(handle.rlm_child_id, handle.session_dir)
```

**輸入**：一段任務描述
**輸出**：`handle`（admission handle，第 2.3.1 節），**不是**分析結果本身
**為什麼 Agent 要這樣做**：把「找出 Controller 層類別」這個子任務，交給一個獨立的子 Agent 在自己的 Context 中處理，避免污染父層 Agent 的主要對話脈絡。

### 54.5 第五步：跨 Agent 通訊

```python
# 🟢 官方功能
await agent_message.send(
    message="麻煩優先看 order 相關套件下的類別",
    receiver_role="child",
    receiver_name="controller-scan",
    mode="steer",
)
```

**說明**：父層 Agent 可以在子 Agent 執行過程中即時「導引」它的方向，而不需要等子 Agent 完全做完才發現方向錯了。

### 54.6 第六步：接觸 Continual Harness（`/refine`，官方推薦入口）

```bash
# 🟢 官方功能：互動模式指令，而非 Python API
/refine 把剛才找到的 Controller 層類別清單記錄為這個專案的 Memory
```

🔴 **注意**：第 3.4 節提到 `rlm.harness.create_memory(...)` 等方法確認存在於原始碼，但官方文件推薦的入口是 `/refine` 指令本身，本教學遵循官方推薦路徑。

### 54.7 完整 Multi-Agent Workflow 範例

```python
# 🟢 官方功能 + 🔵 企業建議的組合寫法
# 情境：綜合前面所有步驟，完整分析一個模組並沉澱結果

import os

# 步驟一：程式化找出目標檔案
target_files = []
for root, dirs, files in os.walk("src/main/java/com/example/order"):
    for f in files:
        if f.endswith(".java"):
            target_files.append(os.path.join(root, f))

# 步驟二：拆分給多個子 Agent 平行分析
tasks = {
    "api-scan": "找出這個模組中所有對外 REST API 端點",
    "db-scan": "找出這個模組中所有資料庫存取程式碼",
    "security-scan": "掃描這個模組是否有明顯的安全風險",
}

handles = {}
for name, task in tasks.items():
    handles[name] = await rlm(
        f"針對以下檔案清單進行分析：{target_files}\n任務：{task}",
        name=name,
    )

# 步驟三：等待期間可先查詢已註冊的子 Agent
children = await rlm.list_subagents()
print(f"目前有 {len(children)} 個子 Agent 執行中")

# 步驟四：（後續互動中）向特定子 Agent 詢問進度或導引方向
await agent_message.send(
    message="請特別留意是否有缺少權限檢查的端點",
    receiver_role="child",
    receiver_name="security-scan",
    mode="follow_up",
)

# 步驟五：彙整完成後，透過 /refine（互動指令）沉澱為 Memory
```

**執行流程說明**：先用純 Python 取得確定性的檔案清單（步驟一），避免模型憑印象猜測；再用 `rlm()` 把三個獨立面向的分析平行外包給子 Agent（步驟二），提升效率並降低單一 Context 的負擔；透過 `list_subagents()` 追蹤進度（步驟三）；用 `agent_message` 即時導引子 Agent（步驟四）；最後用官方推薦的 `/refine` 入口把分析結果沉澱為長期可用的 Memory（步驟五）。這個流程正是第 20 章 Reverse Engineering 與第 47 章實戰案例背後的程式化基礎。

---

## 55. Architecture Decision Records

### 55.1 Prime Agent 專用 ADR 清單

🔵 **企業建議**：建立以下七個 ADR 作為企業導入 Prime Agent 時的架構決策記錄範本：

| ADR | 主題 | 決策要點範例 |
|-----|------|----------------|
| ADR-001 | Agent Architecture | 是否採用 Multi-Agent 分工（第 13、14 章）、單一父 Agent 上限 |
| ADR-002 | Model Provider | 採用哪些 Provider（第 9 章）、是否允許本地模型 |
| ADR-003 | Sub-agent Strategy | 子 Agent 產生的治理規則（第 14.4 節） |
| ADR-004 | Memory Strategy | Local／Global Memory 的分界（第 16.4 節） |
| ADR-005 | Skill Strategy | 內部 Skill 的審查與發布流程（第 15.6 節） |
| ADR-006 | Security Boundary | 執行環境的隔離策略（第 30、31 章） |
| ADR-007 | Autonomous Policy | Autonomous Mode 的預設 Gate 與上限（第 18.4 節） |

### 55.2 ADR 範本

🔵 **企業建議**：

```markdown
# ADR-001：Agent Architecture

## 狀態
已採用

## 背景
本專案需要決定是否採用 Multi-Agent 分工模式處理大型任務。

## 決策
採用第 13、14 章的 Architect/Frontend/Backend/Database/Security/Test/DevOps/Reviewer
角色分工模式，單一父任務最多允許 6 個並行子 Agent。

## 後果
- 正面：大型任務可平行處理，降低單一 Context 負擔
- 負面：子 Agent 數量增加除錯複雜度與 Token 成本，需搭配第 38 章 Governance
```

---

## 56. Enterprise Reference Architecture

### 56.1 最終企業架構

🔵 **企業建議**：

```mermaid
flowchart TD
    Enterprise[Enterprise] --> Platform[AI SDLC Platform]
    Platform --> PA[Prime Agent]
    Platform --> Gov[Governance]
    PA --> RLM[RLM]
    PA --> CH[Continual Harness]
    PA --> MCPInt[MCP]
    RLM --> MultiAgent[Multi-Agent]
    CH --> Skills[Skills]
    CH --> Memory[Memory]
    CH --> Prompt[Prompt]
    CH --> Agents[Sub-agents]
    MultiAgent --> SA[SA Agent]
    MultiAgent --> DEV[Dev Agent]
    MultiAgent --> QA[QA Agent]
    MultiAgent --> Security[Security Agent]
    MultiAgent --> DevOps[DevOps Agent]
    MultiAgent --> Data[Data Agent]
    Gov --> Registry[Agent/Skill/Prompt Registry]
    Gov --> Cost[Cost Governance]
    Gov --> Audit[Audit/Logging]
```

### 56.2 架構層與治理層的對應

| 技術層 | 對應章節 | 治理層 | 對應章節 |
|--------|----------|--------|----------|
| RLM | 第 2、54 章 | Model Governance | 第 38 章 |
| Continual Harness | 第 3、16、17 章 | Memory／Skill Governance | 第 38 章 |
| Multi-Agent | 第 13、14 章 | Agent Registry | 第 38 章 |
| MCP | 第 27 章 | MCP Governance | 第 38 章 |
| Autonomous Mode | 第 18 章 | Cost Guardrail | 第 40 章 |
| Security Model | 第 30、31 章 | Permission Governance | 第 38 章 |

---

## 57. 企業導入 Roadmap

### 57.1 時間軸

🔵 **企業建議**：

```mermaid
timeline
    title Prime Agent 企業導入 Roadmap
    30 天 : PoC
    60 天 : Team Pilot
    90 天 : Production
    180 天 : AI SDLC
    365 天 : Autonomous Engineering
```

### 57.2 各階段規劃

**30 天：PoC**

- 技術：Level 1–2（第 37 章）、單一非關鍵專案試用
- 人員：1–2 位志願工程師
- 流程：僅互動模式，不使用 Autonomous Mode
- Governance：基本安全 Checklist（第 30.3 節）
- KPI：主觀滿意度、初步採用意願
- Risk：低（範圍受控）

**60 天：Team Pilot**

- 技術：Level 3（Multi-Agent，第 13、14 章）
- 人員：一個完整開發團隊
- 流程：建立第一批團隊 Skill／Memory
- Governance：啟動 Skill Registry（第 38 章）
- KPI：PR Throughput、初步 Defect Rate 觀察
- Risk：中（需開始關注子 Agent 治理）

**90 天：Production**

- 技術：Level 3–4，部分任務導入 Autonomous Mode（低風險任務先行）
- 人員：擴展到 2–3 個團隊
- 流程：SOP-01~10（第 44 章）開始落地
- Governance：完整 Registry + Cost Guardrail（第 40 章）
- KPI：完整 Agent KPI 追蹤（第 39 章）
- Risk：中高（需要成熟的 Quality Gate）

**180 天：AI SDLC**

- 技術：Level 4–5，SSDLC 整合（第 33 章）
- 人員：跨團隊標準化
- 流程：企業標準 SOP 全面採用
- Governance：Audit／Compliance 整合進既有稽核流程
- KPI：Autonomous Completion Rate、Rollback Rate
- Risk：高（需要成熟治理才能支撐規模化）

**365 天：Autonomous Engineering**

- 技術：Level 6，Enterprise AI SDLC 全面整合
- 人員：全公司 AI Agent Governance 小組運作
- 流程：Long-running／Autonomous Task 成為常態
- Governance：持續稽核與 KPI 檢討機制
- KPI：全套第 39 章 KPI 儀表板
- Risk：需持續監控，避免第 58 章常見錯誤重現

---

## 58. 常見錯誤與不適合的使用情境

### 58.1 Prime Agent 不適合做什麼（完整版，呼應第 1.7 節）

必須客觀說明：

- ❌ 不應直接接 production 環境執行（第 30 章 Trust Model）
- ❌ 不應直接操作 production 資料庫（第 23.5、32.3 節）
- ❌ 不應無限制使用 Autonomous Mode（第 18.4 節）
- ❌ 不應使用未經審查的第三方 Skill（第 15.6 節）
- ❌ 不應安裝未經審查的 MCP Server（第 27.4 節）
- ❌ 不應暴露 production 憑證給執行環境（第 30.3 節）
- ❌ 不應把 ARC-AGI-3 等 benchmark 成績當成企業品質保證（第 1.8 節）
- ❌ 不應完全取代 Architect／Developer／QA／Security 的角色判斷（第 35 章）

🟡 **第三方觀察（非官方文件，屬本手冊查證期間蒐集到的社群評論，僅供參考）**：多篇獨立評測文章（見附錄 I）對「何時應該暫緩導入」提出了與本手冊第 30、37 章精神一致的判斷準則，可作為團隊自我檢核的簡易清單——若以下任一項是團隊的**硬性要求**，建議暫緩導入或先完成對應的補強措施再評估：

| 團隊的硬性要求 | 與 Prime Agent 現況的落差 | 對應本手冊章節 |
|------|------|------|
| 需要「每個動作」都經人工核准（Guided per-action approval） | Autonomous Mode 是以 Gate／上限為單位做批次驗證，而非逐動作核准 | 第 18 章 |
| 無法將不受信任的程式碼／專案隔離執行 | 執行環境明文不是資安沙箱（第 30.1 節） | 第 30、31 章 |
| 無法或不願意監控遞迴子 Agent 帶來的成本 | `rlm()` 產生的子 Agent 各自消耗獨立 Token 額度，缺乏官方內建的成本上限 | 第 14.4、40 章 |
| 需要「已充分驗證多年」的企業級穩定性 | 專案仍在快速迭代（第 1.1 節版本資訊），次版本間 API／CLI 行為可能調整 | 全書多處「🔴 次版本間可能調整」提醒 |

### 58.2 常見錯誤清單

🔴 **注意**：

1. **把 Prime Agent 當 Chatbot 使用**——忽略了它作為長時間執行 Harness 的設計初衷，只拿來問單次簡單問題，浪費了 RLM／Continual Harness／Sub-agent 帶來的價值
2. **沒有 Git Checkpoint**——大範圍變更沒有分階段 Commit，出問題時難以回溯（第 29 章）
3. **直接讓 Agent 修改 Production**——違反第 30 章 Trust Model 的基本認知
4. **不限制 Autonomous Mode 的回合／Token／逾時上限**——放任使用預設值，未依任務風險調整（第 18 章）
5. **不做 Quality Gate**——`--autonomous-gate` 留空或只做表面檢查
6. **不治理 Skills**——來路不明的第三方 Skill 未經審查就使用（第 15.6 節）
7. **不治理 Memory**——任由 Harness Memory 累積過期或衝突的內容（第 16.3 節）
8. **讓 Agent 接觸機敏憑證**——在會執行 Prime Agent 的環境中放置 Production 等級的機密
9. **Sub-agent 無限制建立**——單一任務放任 Agent 自行決定要 spawn 多少子 Agent，導致成本與複雜度失控（第 14.4 節）
10. **沒有成本控制**——未對 Token 用量、模型選擇設定任何團隊層級的預算與監控（第 40 章）
11. **不 Review `/refine` 的結果**——讓 Harness 狀態未經人工確認就持續累積變更（第 17.3 節）
12. **把 ARC-AGI-3 等 Benchmark 成績當成企業品質保證**——忽略第 1.8 節提到的查證限制與適用範圍差異

---

## 59. 最佳實務

### 59.1 十大企業導入原則（總綱）

🔵 **企業建議**：以下十大原則是本手冊所有具體建議的共同精神，也是下方 50 條最佳實務的分類依據：

1. **Human in the Loop**：關鍵決策（架構、Production 變更、資料遷移）保留人工確認關卡
2. **Git First**：所有變更都在版本控制之下進行，保留可回溯的 Checkpoint
3. **Test First**：Autonomous Task 必須搭配真正能驗證正確性的測試 Gate
4. **Security First**：正視第 30 章的 Trust Model，不把 Prime Agent 執行環境當成沙箱
5. **Least Privilege**：Agent 可存取的憑證、網路範圍、系統權限，遵循最小必要原則
6. **Quality Gate**：`--autonomous-gate` 視為必要而非選填項目
7. **Observable Agent**：善用 Session Persistence（第 6 章），讓 Agent 的決策過程可稽核
8. **Reversible Change**：優先要求 Agent 產出「可回滾」的變更，搭配 Harness 的 Snapshot／Rollback 機制
9. **Controlled Autonomy**：Autonomous Mode 的回合數、Token、逾時上限，依任務風險等級調整，而非一律套用預設值
10. **Evidence-based Self Improvement**：`/refine` 帶來的 Harness 變更，應基於這次任務的實際觀察，而非憑空猜測；重大變更經人工檢視

### 59.2 五十條最佳實務（依十大原則分類）

**Architecture（架構）**

1. 為每個專案建立初始 Architecture Map，並用 `/refine` 沉澱（第 10 章）
2. 明確定義各 Sub-agent 的職責邊界，避免職責重疊（第 14 章）
3. 重大架構決策以 ADR 記錄（第 55 章）
4. Multi-Agent 拆分前先評估任務是否真的適合平行處理（第 13 章）
5. 定期檢視 Enterprise Reference Architecture 是否仍符合實際使用狀況（第 56 章）

**Security（安全）**

6. 團隊成員必須理解 Trust Model 的核心事實（第 30.1 節）
7. 高風險任務安排在受控／隔離環境中執行（第 31 章）
8. 執行環境不放置 Production 等級機敏憑證（第 30.3 節）
9. 第三方 Skill／MCP Server 上線前經過審查（第 15.6、27.4 節）
10. 金融業等高度受管制產業，額外落實資料存取邊界（第 32.3 節）

**Development（開發）**

11. 任務開始前先要求 Agent 產出分析而非直接動手修改（第 10.2 節）
12. 使用結構化 Prompt Template（第 51 章），而非模糊指令
13. 遵循 Bad Task vs Good Task 的拆解原則（第 52 章）
14. 大型任務優先用 RLM 程式化篩選資料，而非整份塞進 Context（第 53 章）
15. 每個有意義的階段都 Commit 一次（第 29 章）

**Testing（測試）**

16. Autonomous Gate 至少包含編譯與完整既有測試（第 18.4 節）
17. Characterization Test 用於保護 Legacy 行為再重構（第 24.3 節）
18. Test Agent 補齊的測試需涵蓋邊界／失敗情境，而非只測成功路徑（第 14.1 節）
19. 效能驗證的基準線比較由人工把關（第 22.5 節）
20. 定期追蹤 Test Coverage KPI 趨勢（第 39 章）

**Agent（代理）**

21. 子 Agent 數量設定團隊治理上限（第 14.4 節）
22. 長任務搭配心跳機制回報進度（第 19.2 節）
23. `rlm()` 呼叫後透過 `agent_message` 或查詢 Session 取得結果，不假設同步回傳（第 2.3.1 節）
24. Multi-Agent Review 彙整後仍需人工核准（第 25.4 節）
25. 定期審視 Agent Registry 是否有職責重疊或過期角色（第 38 章）

**Prompt（提示詞）**

26. 使用 Context/Goal/Constraints/Architecture/Inputs/Outputs/Verification/Quality Gate/Rollback 模板（第 51 章）
27. 高風險任務明確加註「不要修改任何檔案」等限制條件（第 10.2 節）
28. 團隊建立 Prompt Registry，避免各自為政（第 38 章）
29. Prompt 中避免模糊詞彙（如「優化一下」），改用具體可驗證的描述（第 52 章）
30. Prompt Library 中的範本定期依實際使用經驗更新（第 50 章）

**Memory（記憶）**

31. 明確區分該進 Memory 與不該進 Memory 的資料類型（第 16.1、16.2 節）
32. `/refine` 產出內容比照 Code Review 流程做人工檢視（第 16.3 節）
33. Local 與 Global Memory 層級選擇需考量適用範圍（第 16.4 節）
34. 定期清理過期或衝突的 Memory（第 16.3 節）
35. Memory 內容絕不包含機敏資訊（第 16.2 節）

**Skill（技能）**

36. 每個 Skill 明確宣告 `allowed-tools`（第 15.6 節）
37. 涉及自動修改的 Skill 要求先產出報告再執行（第 15.6 節）
38. 內部 Skill 目錄依職責分類組織（第 15.4 節）
39. Skill 描述需清楚說明何時該被觸發，避免誤觸發或漏觸發
40. 第三方 Skill 上線前記錄審查結果於 Skill Registry（第 38 章）

**Multi-Agent（多代理）**

41. Parent／Child／Sibling 溝通模式依實際協作需求選擇（第 13.3 節）
42. 平行子 Agent 的介面約定應在拆分任務時就明確定義（第 13.2 節）
43. Reviewer Agent 的彙整結果需去除重複發現（第 49.3 節）
44. 大型 Legacy 分析優先考慮 Multi-Agent 平行處理（第 20、47 章）
45. Multi-Agent Code Review 的每個審查視角應保持獨立、避免互相干擾（第 49 章）

**Governance（治理）**

46. 建立 AI Agent Governance 小組負責跨團隊協調（第 38.2 節）
47. Cost Guardrail 依任務型態分級設定（第 40 章）
48. KPI 作為趨勢觀察工具而非個人績效考核依據（第 39.2 節）
49. Roadmap 各階段依實際治理成熟度推進，不跳級（第 37.3、57 章）
50. 定期（如每季）回顧第 58 章常見錯誤清單，檢視團隊是否重蹈覆轍

---

## 60. Final Checklist

### 60.1 Environment

- [ ] 確認作業系統（Linux／macOS 原生；Windows 需 Git Bash 或 WSL2，第 7.5 節）
- [ ] Node.js 版本 ≥ 22.8.0
- [ ] Git 已安裝並設定好身分
- [ ] Prime Agent 已安裝（`prime-agent --version` 可正常執行）
- [ ] Provider／API Key 已設定（第 9 章）

### 60.2 Project

- [ ] 專案已在 Git 版本控制下，且有獨立分支可供 Agent 操作
- [ ] Build 指令、Test 指令已被 Agent 正確識別（第 10 章）
- [ ] 已建立初步的 Architecture Map（Memory 或文件形式保存）

### 60.3 Agent

- [ ] 任務目標（Goal）明確、可驗證，避免模糊指令（第 51、52 章）
- [ ] 涉及自動修改的任務，`--autonomous-gate` 已設定且涵蓋真正的測試驗證
- [ ] 需要長期沉澱的知識已透過 `/refine` 記錄，且經人工檢視（第 16、17 章）
- [ ] 子 Agent 數量與職責分工在團隊治理範圍內（第 14.4 章）

### 60.4 Security

- [ ] 團隊成員理解 Trust Model：Prime Agent 執行環境**不是沙箱**（第 30 章）
- [ ] 高風險任務已安排在受控／隔離環境中執行（第 31 章）
- [ ] 執行環境中不存在 Production 等級機敏憑證
- [ ] 第三方 Skill／MCP Server 已經過審查

### 60.5 Production

- [ ] 所有變更皆已經人工 Review
- [ ] 測試（含新增與既有）全數通過
- [ ] 安全掃描（第 25、30 章）已完成
- [ ] Session 記錄／`/refine` 產出的 Harness 變更已妥善保存以供稽核
- [ ] 沒有自動 Merge／自動 Push 到 main 分支（第 29 章）

完整 Enterprise Checklist 見附錄 G。

---

## Appendix A：CLI Reference

🔴 **注意**：以下所有指令與旗標皆已對照 `packages/coding-agent/docs/usage.md`、`docs/long-running-agents.md`、`docs/json.md`、`docs/rpc.md` 原始檔逐字確認。

| 指令 | 用途 | 語法 | 使用時機 | 常見錯誤 | Windows／WSL 注意事項 |
|------|------|------|----------|----------|--------------------------|
| `prime-agent` | 於目前目錄啟動互動 Session | `prime-agent [options] ["prompt"]` | 開始一次新任務 | 忘記先 `cd` 到正確專案目錄 | 需先有可用的 bash（第 7.5 節） |
| `agents` | 瀏覽 Session 清單 | `prime-agent agents` | 每天開工確認背景任務 | — | 同上 |
| `list --all` | 列出所有 Session（含已結束） | `prime-agent list --all` | 尋找較舊的 Session 記錄 | — | 同上 |
| `attach` | 接回背景 Session | `prime-agent attach <agent>` | 查看長任務進度 | Session 名稱打錯 | 同上 |
| `stop` | 停止指定 Agent | `prime-agent stop <agent>` | 任務達標或方向錯誤要喊停 | 未先確認狀態就強制停止 | 同上 |
| `rename` | 重新命名 Session | `prime-agent rename <agent> <name>` | 方便日後辨識 | — | 同上 |
| `send` | 對背景 Agent 傳訊 | `prime-agent send <agent> <message>` | 不需要先 attach 就傳新指示 | — | 同上 |
| `schedule list` | 列出排程 | `prime-agent schedule list` | 檢視目前有哪些排程任務 | — | 同上 |
| `schedule add` | 新增排程 | `prime-agent schedule add <agent> "<when>" -- "<prompt>"` | 排定 Overnight／定期任務 | `when` 格式錯誤 | 同上 |
| `schedule cancel` | 取消排程 | `prime-agent schedule cancel <schedule-id>` | 排程不再需要 | — | 同上 |
| `status` | 查看整體狀態 | `prime-agent status` | 確認 Daemon／Worker 是否存活 | — | 同上 |
| `doctor` | 診斷環境問題 | `prime-agent doctor [--fix]` | 安裝或執行異常時第一步 | — | Windows 上常見問題為找不到 bash |
| `shutdown` | 關閉背景 Daemon | `prime-agent shutdown [--force]` | 環境需要整個重啟 | 未確認就強制關閉，中斷進行中任務 | 同上 |
| `package` | 管理擴充套件 | `prime-agent package install <source> [--local]`／`remove <source> [--local]`／`list`／`update [source]` | 安裝／移除第三方擴充（詳見 `docs/packages.md`） | 來源不明的套件（第 30 章風險） | 同上 |
| `update` | 更新版本 | `prime-agent update [--force]` | 定期升級（第 43 章） | 企業內網無法連外 | 同上 |
| `config` | 管理設定 | `prime-agent config` | 調整 Provider／Skill 等設定 | — | 同上 |
| `-c/--continue` | 接續最近一次 Session | `prime-agent -c` | 快速接續昨天的工作 | — | 同上 |
| `-r/--resume` | 恢復指定 Session | `prime-agent -r <path\|id>` | 恢復特定歷史 Session | ID 錯誤 | 同上 |
| `--fork` | 從既有 Session 分岔 | `prime-agent --fork <path\|id>` | 想嘗試不同方向又不想影響原 Session | — | 同上 |
| `--mode json` | JSON 事件流模式 | `prime-agent --mode json "prompt"` | CI/CD 整合（第 28 章） | 誤用一般文字解析工具解析輸出 | 同上 |
| `--mode rpc` | RPC 模式 | `prime-agent --mode rpc` | 需要雙向程式化控制 | 使用 Node `readline` 解析（官方警告不相容） | 同上 |
| `--autonomous` | 啟用 Autonomous Mode | `prime-agent --autonomous --autonomous-gate "<cmd>" "prompt"` | 需要多輪自主執行 | 未設定 Gate（第 18.4 節） | 同上 |
| `--provider` / `--model` | 指定供應商／模型 | `prime-agent --provider anthropic --model claude-opus-5` | 需要指定非預設模型 | Provider 未先設定 API Key | 同上 |
| `--thinking` | 控制推理深度 | `prime-agent --thinking high` | 複雜任務需要更深入推理 | 等級拼字錯誤 | 同上 |
| `--skill` | 指定額外 Skill 路徑 | `prime-agent --skill <path>` | 測試尚未放進標準目錄的 Skill | 路徑錯誤 | 同上 |

---

## Appendix B：Python／RLM Reference

🔴 **注意**：以下 API 需以目前 Prime Agent 官方文件與原始碼為準；次版本間可能調整簽名或行為。

| API | 簽名 | 用途 | 回傳值 |
|-----|------|------|--------|
| `rlm()` / `rlm.run()` | `await rlm(task: str, name: str = None, model: str = None, thinking: str = None)` | 產生子 Agent（兩種呼叫形式等價；未定義的關鍵字參數會直接失敗，第 2.3.1 節） | admission handle（`RLMSpawnHandle`：`.rlm_child_id`、`.name`、`.session_dir`、`.model`），**非**分析結果 |
| `rlm.list_subagents()` | `await rlm.list_subagents()` | 列出子 Agent | 子 Agent 清單 |
| `rlm.delete_subagent()` | `await rlm.delete_subagent(handle)` | 終止子 Agent | — |
| `agent_message.send()` | `await agent_message.send(message, receiver_role, receiver_name=None, mode="auto")` | 跨 Agent 通訊 | — |
| `agent_message.list_agents()` | `await agent_message.list_agents()` | 列出可通訊 Agent | Agent 清單 |
| `goal.get()` | `await goal.get()` | 查詢目前 Goal 狀態 | Goal 內容（含 Token 用量、經過時間、延續次數、預算） |
| `goal.complete()` | `await goal.complete()` | 標記 Goal 完成 | — |
| `rlm_heartbeat.create()` | `await rlm_heartbeat.create(...)` | 設定心跳排程 | — |
| `rlm_heartbeat.list()` | `await rlm_heartbeat.list()` | 列出心跳排程 | 排程清單 |
| `rlm_heartbeat.update()` | `await rlm_heartbeat.update(...)` | 更新心跳排程 | — |
| `compact.status()` | `await compact.status()` | 查詢 Context 壓縮狀態 | 狀態資訊 |
| `compact.run()` | `await compact.run(...)` | 執行 Context 壓縮 | — |
| `rlm.harness.*` | `rlm.harness.create_memory(...)` 等 | Harness 狀態直接操作（🔴 原始碼存在但非官方公開推薦介面，第 3.4 節） | — |

🔴 **注意**：Kernel 端**沒有** `goal.create()` 方法——建立 Goal 官方定義為使用者／Host 的明確動作，只能透過 `/goal` 互動指令或 `--goal`／`--goal-token-budget` 啟動旗標設定，Agent 無法在 Python 中自行建立（第 18.3 節）。

**互動指令（非 Python API）**：`/refine [instructions]`、`/autonomous on\|status\|off`、`/goal <text> [--budget <n>]`（另有 `status`／`pause`／`resume`／`clear` 子指令）、`/heartbeat every <interval> <instruction> [--follow-up]`（另有 `status`／`pause`／`resume`／`clear`；`/heartbeats` 可同時檢視使用者與 Agent 自建心跳）、`/login`、`/mcp login <name>`、`/skill:name [args]`。

---

## Appendix C：Prompt Library

（純複製版，內容與第 50 章相同，方便直接複製使用）

```text
[1. Project Analysis]
請分析目前這個專案：建立整體 Architecture Map、列出主要模組與相依關係、
找出實際的 Build/Test 指令、摘要程式碼風格慣例、掃描明顯安全風險。
在完成分析前，不要修改任何檔案。

[2. Architecture]
根據目前的需求與既有架構慣例，提出符合 Clean Architecture／Hexagonal Architecture 的實作方式，
標記出需要人工決策的架構取捨點，並說明各選項的優缺點。在決策確認前不要開始實作。

[3. Reverse Engineering]
這是一個 Legacy 系統，請拆分子 Agent 平行分析：對外 API 進入點、資料庫存取與交易邊界、
外部整合點（批次/FTP/MQ）、安全風險。彙整成 Architecture Map、Dependency Map、
Database Map、API Map、Risk Map、Migration Map。在完成分析前不要修改任何檔案。

[4. Framework Upgrade]
分析目前專案對 [目標框架版本] 的相容性風險，產出分階段升級計畫，
在計畫經人工確認前不要修改任何檔案；計畫需包含每個階段的驗證方式。

[5. Security Review]
依 OWASP Top 10 檢查本次變更的程式碼，標記高風險項目與嚴重度，
附上檔案路徑、行號、風險說明與修正建議。只產出報告，不自動修改程式碼。

[6. Database Migration]
分析 [來源資料庫] Schema 定義，產出遷移到 [目標資料庫] 的對照計畫：
型別對照、Stored Procedure 轉換策略、索引策略、需要人工確認的邊界案例。
在產出遷移計畫前，不要修改任何檔案。

[7. Code Review]
針對這次 PR 的變更，分別從架構一致性、安全性、測試涵蓋率、效能風險、程式碼品質五個角度審查，
彙整成一份依嚴重度排序、區分「必須修正」與「建議可選」的摘要。

[8. Test Generation]
為 [目標類別/函式] 補齊 JUnit 5 單元測試，確保涵蓋主要成功路徑與至少一個邊界／失敗情境，
測試命名與既有測試慣例保持一致。

[9. Autonomous Task]
[明確、可驗證的任務目標]。在達成目標前，每個階段都要通過指定的 Gate 驗證，
若連續失敗達重試上限，停止並回報目前狀態與失敗原因，不要嘗試繞過驗證。

[10. Long-running Task]
[長任務目標描述]。請每 [時間間隔] 回報一次目前進度、已完成的階段、遇到的問題，
並在每個階段完成後確保處於可編譯、可測試通過的穩定狀態。

[11. Sub-agent]
請針對 [任務清單] 分別派子 Agent 平行處理，每個子 Agent 完成後回報結果，
最後由你彙整成一份總表，標記彼此之間是否有不一致或需要協調的地方。

[12. Skill Creation]
請為 [特定重複性任務] 建立一個新的 Skill：name 為 [skill-name]，
description 需清楚描述何時該被觸發，內文需包含具體的執行步驟與輸出格式要求。

[13. Memory Creation]
/refine 把剛才確認的 [具體事實/慣例] 記錄為這個專案的 Memory，
記錄前請先確認這是已驗證的事實而非推測，並檢查是否與既有 Memory 衝突。

[14. Refinement]
/refine 這次任務中你觀察到 [具體觀察]，請評估是否需要更新 Memory／Skill／
Sub-agent 規格，並說明每項建議變更的具體理由。

[15. Release Verification]
對照本次變更的原始規格文件，逐項確認實作是否完整覆蓋：功能需求、非功能需求、
API 契約、測試涵蓋率、安全檢查結果。以表格輸出「規格項目 → 是否完成 → 驗證方式」，
標記出任何未完成或需要人工確認的項目。
```

---

## Appendix D：Skill Library

（第 15.5 節已提供 `security-review`、`architecture-review`、`database-review` 三個範例，以下為額外兩個範例）

**範例四：`api-contract-review`（🔵 企業建議）**

```markdown
---
name: api-contract-review
description: 檢查 REST API 變更是否破壞既有的 OpenAPI 契約，找出可能影響前端或外部消費者的破壞性變更。
allowed-tools: read grep
---

# API Contract Review Skill

1. 比對本次變更前後的 OpenAPI／Controller 定義
2. 標記破壞性變更：欄位刪除、型別變更、必填欄位新增、路徑變更
3. 標記非破壞性變更：新增選填欄位、新增端點
4. 若發現破壞性變更，提出版本控制建議（如 API 版本號遞增）
只產出報告，不直接修改程式碼。
```

**範例五：`test-coverage-review`（🔵 企業建議）**

```markdown
---
name: test-coverage-review
description: 檢查本次變更的測試涵蓋率，找出缺少測試的新增邏輯與未覆蓋的邊界情境。
allowed-tools: read grep bash
---

# Test Coverage Review Skill

1. 找出本次變更新增或修改的方法／函式
2. 檢查是否有對應的測試案例
3. 針對有測試但只涵蓋成功路徑的邏輯，標記缺少的邊界／失敗情境測試
4. 輸出清單：方法名稱、是否有測試、缺少的測試情境建議
```

---

## Appendix E：Troubleshooting 速查

（完整症狀→原因→診斷→解決方案見第 41 章，此處為速查表版）

| 症狀 | 可能原因 | 建議診斷／解決方式 |
|------|----------|----------------------|
| 安裝後找不到 `prime-agent` 指令 | 安裝腳本未把執行檔加進 PATH | 確認 Shell 設定檔已載入安裝路徑；重新開啟終端機 |
| Windows 下無法執行 | 找不到可用的 bash | 安裝 Git for Windows 或設定 WSL2（第 7.5 節） |
| Provider 驗證失敗 | API Key 未設定或已過期 | 檢查對應環境變數；重新執行 `/login` |
| `prime-agent status` 顯示異常 | Daemon 未正常啟動 | 執行 `prime-agent doctor`，必要時 `prime-agent shutdown` 後重試 |
| Autonomous Task 提早停止 | 達到 `--autonomous-max-turns` 或 Gate 連續失敗達重試上限 | 檢視 Session 記錄找出 Gate 失敗原因，而非單純調高上限 |
| Session 無法 `attach` | Session 已結束或 ID 錯誤 | `prime-agent agents` 確認實際 Session 清單與狀態 |
| Sub-agent 沒有回應 | `rlm()` 只回傳 admission handle，需另外查詢結果 | 透過 `agent_message` 或查看子 Agent `session_dir` 確認實際進度（第 2.3 節） |
| MCP 工具呼叫失敗 | OAuth 過期或使用不支援的 stdio 傳輸 | `/mcp login <name>`；確認為 http 傳輸（第 27.2 節） |
| Skill 未被載入 | frontmatter 格式錯誤或路徑不在搜尋範圍 | 檢查 `name`／`description`；用 `/skill:name` 強制測試（第 15.3 節） |

---

## Appendix F：Security Checklist

（完整討論見第 30、31 章）

- [ ] 明確告知所有使用者：Prime Agent 執行環境**不是沙箱**，其權限等同啟動它的使用者帳號
- [ ] 不在會執行 Prime Agent 的機器上，用具備 Production 存取權限的帳號登入
- [ ] 環境變數中不放置 Production 等級的機敏資訊
- [ ] 對第三方 Skill、MCP Server 建立審查流程後才允許團隊使用
- [ ] Session 儲存目錄比照原始碼倉庫的保密等級管理存取權限
- [ ] 涉及自動修改／刪除的 Autonomous Task，搭配 `--autonomous-gate` 且限定操作範圍
- [ ] 定期檢視 Harness Memory 是否意外記錄了機敏資訊
- [ ] 高風險任務（Legacy 分析、金融業場景）安排在容器／VM 等隔離環境
- [ ] 網路存取範圍限制在必要的套件庫與內部服務
- [ ] 使用短時效、範圍受限的憑證而非長期個人憑證

---

## Appendix G：Enterprise Checklist

（與第 60 章 Final Checklist 呼應的擴充版，涵蓋治理與導入面向）

**Governance**

- [ ] Agent／Skill／Prompt Registry 已建立（第 38 章）
- [ ] Cost Guardrail 已設定（第 40 章）
- [ ] KPI 儀表板已建立並定期檢視（第 39 章）
- [ ] AI Agent Governance 小組已指定負責人（第 38.2 節）

**流程**

- [ ] 企業標準 SOP（第 44 章）已依團隊實際情況調整落地
- [ ] Git 安全規則（第 29.2 節）已納入團隊規範
- [ ] Autonomous Mode 的預設 Gate 已標準化（第 18.4 節）

**導入節奏**

- [ ] 目前所處導入 Level（第 37 章）與 Roadmap 階段（第 57 章）已明確
- [ ] 未跳過應有的治理成熟度就升級到下一 Level

**持續改善**

- [ ] 定期回顧第 58 章常見錯誤清單
- [ ] `/refine` 產出的變更有固定的人工審核流程（第 17.3 節）
- [ ] 每季檢視 Memory／Skill 是否過期或衝突

---

## Appendix H：Glossary

| 名詞 | 說明 |
|------|------|
| RLM（Recursive Language Model） | 把 Context 當變數、在持久化 REPL 中遞迴呼叫子模型的執行模型（第 2 章） |
| Continual Harness | 把 Prompt／Skills／Memory／Sub-agent 視為可 CRUD 的持久狀態（第 3 章） |
| Harness State | Continual Harness 的實際持久化資料（`harness_state.json`） |
| Sub-agent | 由 `rlm()` 動態產生的子 Agent |
| A2A（Agent-to-Agent） | 透過 `agent_message` 進行的跨 Agent 通訊 |
| Autonomous Mode | Agent 在設定好的護欄下自主執行多輪任務（第 18 章） |
| Quality Gate | `--autonomous-gate` 指定的驗證指令 |
| Session | 一次任務的完整記錄，持久化為 JSONL（第 6 章） |
| Skill | 依 Agent Skills 標準定義的能力擴充，Prime Agent 額外支援 Python-backed 型態（第 15 章） |
| Trust Model / Trust Boundary | 官方對執行環境安全邊界的正式聲明（第 30 章） |
| Daemon／Worker／Kernel | Prime Agent 的三層執行模型（第 5 章） |
| RHAE | Relative Human Action Efficiency，ARC Prize 官方評分方式（第 1.8 節） |
| Characterization Test | 重構前為既有行為建立的保護性測試（第 24.3 節） |
| Admission Handle | `rlm()` 呼叫後立即回傳的控制代碼，非最終結果（第 2.3.1 節） |
| MCP | Model Context Protocol，在 Prime Agent 中以 Python-backed Skill 型態實作（第 27 章） |

---

## Appendix I：Reference Links

一手來源，經查證：

- Prime Agent GitHub：<https://github.com/PrimeIntellect-ai/prime-agent>
- Prime Intellect 官網：<https://www.primeintellect.ai/>
- Prime Agent 官方 Blog：<https://www.primeintellect.ai/blog/prime-agent>
- RLM 官方 Blog：<https://www.primeintellect.ai/blog/rlm>
- Recursive Language Models 論文（arXiv:2512.24601）：<https://arxiv.org/abs/2512.24601>
- Continual Harness 論文（arXiv:2605.09998）：<https://arxiv.org/abs/2605.09998>
- ARC Prize 官方 Leaderboard：<https://arcprize.org/leaderboard>
- ARC Prize Community Leaderboard：<https://arcprize.org/leaderboard/community>
- ARC-AGI-3 評分方法論（RHAE）：<https://docs.arcprize.org/methodology>
- Agent Skills 標準：<https://agentskills.io/>
- pi（Prime Agent 的 Fork 來源）：<https://github.com/earendil-works/pi>

第三方分析／評測（🟡 非官方，查證期間交叉參考，第 58.1 節「暫緩導入」準則整理自此類來源）：

- Kingy.ai — Prime Agent Review：<https://kingy.ai/blog/prime-agent-review-self-improving-rlm-harness/>
- explainx.ai — Prime Agent 分析：<https://www.explainx.ai/blog/prime-agent-rlm-continual-harness-primeintellect-august-2026>

> **延伸閱讀**：本目錄下的《Pi Code Agent 教學手冊.md》涵蓋 Prime Agent 血緣來源 pi 的基礎操作、Extensions／Skills／容器化沙箱等內容，建議與本手冊搭配閱讀；《spec-kit使用教學.md》可搭配第 12 章 Spec-Driven Development 一併參考。

---

## 結語

本手冊完整涵蓋 Prime Agent 官方確認的核心機制——RLM、Continual Harness、Autonomous Mode、Session Persistence、Skills、MCP、安全模型——並在此基礎上，針對企業 Web Application 開發、Legacy Reverse Engineering、Framework Modernization、金融業導入、SSDLC、Multi-Agent Team、Governance、KPI、Cost Management 等企業導入的完整面向，提供了可直接操作的工作流程、Prompt Template 與 SOP。

所有版本號、CLI 指令、API 簽名皆逐字查證於官方原始碼與文件；ARC-AGI-3 等宣傳性數字完整揭露其查證限制，避免企業誤將行銷數字當成品質保證；RLM 與 Continual Harness 的學術出處（MIT CSAIL、Princeton/DeepMind）也正確歸屬，不誤植為 Prime Intellect 原創研究；MCP 的實際支援範圍（Linear／Notion 內建、http-only）也修正了常見的過度樂觀假設。

企業導入 Prime Agent 的核心命題，不是「這個工具能不能寫程式」，而是「如何把它變成企業 AI Software Development Team 的核心 Agent Runtime，讓 AI Agent 能夠長時間、可恢復、可驗證、可自我改善地完成 Web Application 開發、Legacy Reverse Engineering 與 Framework Modernization」——這正是本手冊六十個章節與九個附錄共同回答的問題。

