+++
date = '2026-06-30T10:00:00+08:00'
draft = false
title = 'Multica 教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# Multica 教學手冊（企業級實戰版）

| 項目 | 內容 |
| --- | --- |
| **手冊版本** | v2.0（2026-10-05） |
| **產品基準** | Multica v0.6.1（2026-10-01，CLI commit `2ea01ae4e`，以 Go 1.26.8 建置） |
| **適用對象** | 資深工程師、架構師、DevOps／平台工程師、資安與技術主管 |
| **技術棧** | Go 後端（Chi + sqlc + gorilla/websocket）、Next.js 16 Web、Electron Desktop、Expo iOS、PostgreSQL 17（`pgcrypto` + `pg_trgm`）、Redis（選用）、本機 Agent Daemon |
| **授權** | Multica License（Apache License 2.0 全文，加上託管／嵌入、品牌、署名三類附加條件） |
| **文件等級** | 企業標準技術白皮書 |

本手冊使用下列標記：

| 標記 | 意義 |
| --- | --- |
| ⚠️ 注意 | 不遵守會造成資料遺失、安全風險或服務中斷的事項 |
| 💡 實務建議 | 來自官方文件或社群經驗、可直接採用的做法 |
| 📘 建議實務 | 本手冊依企業導入經驗補充的治理／流程建議，**非** Multica 官方功能或規範 |
| `v0.x.y+` | 該功能自此版本起提供（依官方 changelog） |

本手冊所有 CLI 指令與旗標均已對照 `multica 0.6.1` 的 `--help` 輸出；所有環境變數均已對照 v0.6.1 原始碼中的官方文件。驗證方法與待確認事項見[附錄 F](#附錄-f驗證紀錄)。

---

## 目錄

<!-- TOC-AUTO-BEGIN -->

- [第 1 章：Multica 概述與版本基準](#第-1-章multica-概述與版本基準)
  - [1.1 什麼是 Multica](#11-什麼是-multica)
  - [1.2 名稱由來與設計哲學](#12-名稱由來與設計哲學)
  - [1.3 核心價值主張](#13-核心價值主張)
  - [1.4 與既有工具的差異比較](#14-與既有工具的差異比較)
  - [1.5 適用場景與導入邊界](#15-適用場景與導入邊界)
  - [1.6 專案基本資訊](#16-專案基本資訊)
  - [1.7 授權模式：Multica License](#17-授權模式multica-license)
  - [1.8 v0.3.33 以來的重大變化速覽](#18-v0333-以來的重大變化速覽)
- [第 2 章：核心概念與運作原理](#第-2-章核心概念與運作原理)
  - [2.1 核心物件總覽](#21-核心物件總覽)
  - [2.2 物件關係](#22-物件關係)
  - [2.3 一次 Run 的完整路徑](#23-一次-run-的完整路徑)
  - [2.4 資料與執行邊界](#24-資料與執行邊界)
  - [2.5 四種觸發方式](#25-四種觸發方式)
  - [2.6 Run 完成 ≠ Issue 完成](#26-run-完成--issue-完成)
- [第 3 章：系統架構設計](#第-3-章系統架構設計)
  - [3.1 整體架構](#31-整體架構)
  - [3.2 技術棧](#32-技術棧)
  - [3.3 Repository 結構](#33-repository-結構)
  - [3.4 後端分層](#34-後端分層)
  - [3.5 即時通訊：兩條 WebSocket 路徑](#35-即時通訊兩條-websocket-路徑)
  - [3.6 一次執行的程式碼路徑](#36-一次執行的程式碼路徑)
  - [3.7 多 Workspace 隔離](#37-多-workspace-隔離)
  - [3.8 企業參考部署拓樸](#38-企業參考部署拓樸)
- [第 4 章：快速入門](#第-4-章快速入門)
  - [4.1 起步方式選擇](#41-起步方式選擇)
  - [4.2 五步驟完成第一次 Run](#42-五步驟完成第一次-run)
  - [4.3 官方 Tutorial 學習路徑](#43-官方-tutorial-學習路徑)
  - [4.4 起步常見問題](#44-起步常見問題)
- [第 5 章：Self-Host 安裝與部署](#第-5-章self-host-安裝與部署)
  - [5.1 部署組成與模式選擇](#51-部署組成與模式選擇)
  - [5.2 前置條件](#52-前置條件)
  - [5.3 一鍵安裝（Quick Install）](#53-一鍵安裝quick-install)
  - [5.4 Docker Compose 逐步部署](#54-docker-compose-逐步部署)
  - [5.5 連接執行電腦](#55-連接執行電腦)
  - [5.6 遠端存取與反向代理](#56-遠端存取與反向代理)
  - [5.7 Kubernetes 部署（Helm Chart）](#57-kubernetes-部署helm-chart)
  - [5.8 私有 CA 憑證](#58-私有-ca-憑證)
  - [5.9 不使用 Docker 的手動部署](#59-不使用-docker-的手動部署)
  - [5.10 停止服務與切換至 Cloud](#510-停止服務與切換至-cloud)
  - [5.11 讓 AI Agent 協助部署](#511-讓-ai-agent-協助部署)
- [第 6 章：環境變數與組態參考](#第-6-章環境變數與組態參考)
  - [6.1 正式環境最小組態](#61-正式環境最小組態)
  - [6.2 API 與資料庫](#62-api-與資料庫)
  - [6.3 公開網址與瀏覽器存取](#63-公開網址與瀏覽器存取)
  - [6.4 Email、登入與註冊](#64-email登入與註冊)
  - [6.5 附件儲存](#65-附件儲存)
  - [6.6 Redis 與速率限制](#66-redis-與速率限制)
  - [6.7 外部整合](#67-外部整合)
  - [6.8 伺服器端 LLM（輔助功能）](#68-伺服器端-llm輔助功能)
  - [6.9 前端（Web）](#69-前端web)
  - [6.10 可觀測性與分析](#610-可觀測性與分析)
  - [6.11 Daemon 端環境變數](#611-daemon-端環境變數)
  - [6.12 Daemon 設定檔與優先序](#612-daemon-設定檔與優先序)
- [第 7 章：認證、Token 與註冊管控](#第-7-章認證token-與註冊管控)
  - [7.1 登入方式總覽](#71-登入方式總覽)
  - [7.2 Email 驗證碼](#72-email-驗證碼)
  - [7.3 Google 登入](#73-google-登入)
  - [7.4 註冊限制](#74-註冊限制)
  - [7.5 企業鎖定 Workspace 建立](#75-企業鎖定-workspace-建立)
  - [7.6 Session 存活期](#76-session-存活期)
  - [7.7 Token 類型](#77-token-類型)
  - [7.8 Token 治理建議](#78-token-治理建議)
- [第 8 章：Workspace 與成員角色](#第-8-章workspace-與成員角色)
  - [8.1 Workspace 的定位](#81-workspace-的定位)
  - [8.2 建立 Workspace](#82-建立-workspace)
  - [8.3 切換、離開與刪除](#83-切換離開與刪除)
  - [8.4 角色與權限矩陣](#84-角色與權限矩陣)
  - [8.5 邀請成員](#85-邀請成員)
  - [8.6 變更角色與移除成員](#86-變更角色與移除成員)
  - [8.7 CLI 管理](#87-cli-管理)
  - [8.8 企業團隊隔離策略](#88-企業團隊隔離策略)
- [第 9 章：Issues 與 Projects](#第-9-章issues-與-projects)
  - [9.1 Issue 的組成](#91-issue-的組成)
  - [9.2 Assignee 與執行](#92-assignee-與執行)
  - [9.3 狀態與生命週期](#93-狀態與生命週期)
  - [9.4 自訂狀態](#94-自訂狀態)
  - [9.5 自訂屬性、標籤與檢視](#95-自訂屬性標籤與檢視)
  - [9.6 子 Issue、Stage 與重複標記](#96-子-issuestage-與重複標記)
  - [9.7 Metadata、時間軸與用量](#97-metadata時間軸與用量)
  - [9.8 Projects](#98-projects)
  - [9.9 Project Resources](#99-project-resources)
- [第 10 章：Agents 建立與設定](#第-10-章agents-建立與設定)
  - [10.1 Agent 的本質](#101-agent-的本質)
  - [10.2 設定項目](#102-設定項目)
  - [10.3 建立 Agent](#103-建立-agent)
  - [10.4 撰寫 Instructions](#104-撰寫-instructions)
  - [10.5 Access（誰可以執行）](#105-access誰可以執行)
  - [10.6 模型、Thinking Level 與 Service Tier](#106-模型thinking-level-與-service-tier)
  - [10.7 執行設定](#107-執行設定)
  - [10.8 MCP 設定](#108-mcp-設定)
  - [10.9 複製、封存與還原](#109-複製封存與還原)
  - [10.10 狀態顯示](#1010-狀態顯示)
  - [10.11 企業 Agent 規範](#1011-企業-agent-規範)
- [第 11 章：Skills（技能）機制](#第-11-章skills技能機制)
  - [11.1 Skill 的定位](#111-skill-的定位)
  - [11.2 建立或匯入 Skill](#112-建立或匯入-skill)
  - [11.3 從來源更新](#113-從來源更新)
  - [11.4 Skill 內容結構](#114-skill-內容結構)
  - [11.5 綁定 Agent](#115-綁定-agent)
  - [11.6 三種 Skill 來源](#116-三種-skill-來源)
  - [11.7 權限與供應鏈風險](#117-權限與供應鏈風險)
  - [11.8 企業 Skill Library 治理](#118-企業-skill-library-治理)
- [第 12 章：Squads（小隊編組）](#第-12-章squads小隊編組)
  - [12.1 Squad 的定位](#121-squad-的定位)
  - [12.2 組成要素](#122-組成要素)
  - [12.3 指派後的執行流程](#123-指派後的執行流程)
  - [12.4 Leader 每輪看到的內容](#124-leader-每輪看到的內容)
  - [12.5 Leader 重新觸發規則](#125-leader-重新觸發規則)
  - [12.6 指派與 @提及 Squad](#126-指派與-提及-squad)
  - [12.7 Access 與管理權限](#127-access-與管理權限)
  - [12.8 封存](#128-封存)
  - [12.9 CLI](#129-cli)
  - [12.10 企業編組範例](#1210-企業編組範例)
- [第 13 章：日常協作](#第-13-章日常協作)
  - [13.1 選擇觸發方式](#131-選擇觸發方式)
  - [13.2 指派 Issue](#132-指派-issue)
  - [13.3 在評論中 @提及 Agent](#133-在評論中-提及-agent)
  - [13.4 評論功能](#134-評論功能)
  - [13.5 Chat：一對一對話](#135-chat一對一對話)
  - [13.6 Inbox 與訂閱](#136-inbox-與訂閱)
  - [13.7 引導執行中的 Agent（Steer）](#137-引導執行中的-agentsteer)
  - [13.8 Issue Wakeup（事件、條件與時間喚醒）](#138-issue-wakeup事件條件與時間喚醒)
- [第 14 章：Runtime、Daemon 與 Run 執行](#第-14-章runtimedaemon-與-run-執行)
  - [14.1 Daemon 與 Runtime](#141-daemon-與-runtime)
  - [14.2 啟動與管理 Daemon](#142-啟動與管理-daemon)
  - [14.3 支援的 AI 編碼工具](#143-支援的-ai-編碼工具)
  - [14.4 安裝並驗證 AI 工具](#144-安裝並驗證-ai-工具)
  - [14.5 Run 生命週期](#145-run-生命週期)
  - [14.6 失敗原因與自動重試](#146-失敗原因與自動重試)
  - [14.7 派工與併發](#147-派工與併發)
  - [14.8 私有與公開 Runtime](#148-私有與公開-runtime)
  - [14.9 自訂 Runtime Profile](#149-自訂-runtime-profile)
  - [14.10 Task 執行環境](#1410-task-執行環境)
  - [14.11 Runtime 管理 CLI](#1411-runtime-管理-cli)
  - [14.12 離線 Runtime 排查](#1412-離線-runtime-排查)
- [第 15 章：Autopilots（自動化排程與事件觸發）](#第-15-章autopilots自動化排程與事件觸發)
  - [15.1 Autopilot 的組成](#151-autopilot-的組成)
  - [15.2 執行模式](#152-執行模式)
  - [15.3 排程觸發](#153-排程觸發)
  - [15.4 Webhook 觸發](#154-webhook-觸發)
  - [15.5 執行紀錄、重播與暫停](#155-執行紀錄重播與暫停)
  - [15.6 權限](#156-權限)
  - [15.7 CLI](#157-cli)
  - [15.8 企業應用範例](#158-企業應用範例)
- [第 16 章：通訊整合（Channels）](#第-16-章通訊整合channels)
  - [16.1 平台比較](#161-平台比較)
  - [16.2 訊息處理流程](#162-訊息處理流程)
  - [16.3 Session 隔離與帳號綁定](#163-session-隔離與帳號綁定)
  - [16.4 Slack](#164-slack)
  - [16.5 飛書／Lark](#165-飛書lark)
  - [16.6 釘釘（DingTalk，社群維護）](#166-釘釘dingtalk社群維護)
  - [16.7 企業微信（WeCom，社群維護）](#167-企業微信wecom社群維護)
  - [16.8 Telegram（社群維護）](#168-telegram社群維護)
  - [16.9 自架設定](#169-自架設定)
  - [16.10 社群維護的支援邊界](#1610-社群維護的支援邊界)
- [第 17 章：GitHub、自架 Git 與 CI/CD 整合](#第-17-章github自架-git-與-cicd-整合)
  - [17.1 整合能力範圍](#171-整合能力範圍)
  - [17.2 連接 GitHub 與功能開關](#172-連接-github-與功能開關)
  - [17.3 PR 連結與合併規則](#173-pr-連結與合併規則)
  - [17.4 多 Workspace](#174-多-workspace)
  - [17.5 自架：建立自己的 GitHub App](#175-自架建立自己的-github-app)
  - [17.6 自架 Git：Forgejo、Gitea、GitLab](#176-自架-gitforgejogiteagitlab)
  - [17.7 Agent 如何開 PR](#177-agent-如何開-pr)
  - [17.8 CI/CD 整合模式](#178-cicd-整合模式)
- [第 18 章：Desktop 與 Mobile App](#第-18-章desktop-與-mobile-app)
  - [18.1 Desktop 與 Web](#181-desktop-與-web)
  - [18.2 安裝](#182-安裝)
  - [18.3 分頁與操作](#183-分頁與操作)
  - [18.4 內建 Daemon](#184-內建-daemon)
  - [18.5 更新](#185-更新)
  - [18.6 連接自架實例：`desktop.json`](#186-連接自架實例desktopjson)
  - [18.7 Windows Defender 誤判](#187-windows-defender-誤判)
  - [18.8 iOS App（iPhone／iPad）](#188-ios-appiphoneipad)
- [第 19 章：CLI 完整參考](#第-19-章cli-完整參考)
  - [19.1 安裝與更新](#191-安裝與更新)
  - [19.2 首次連線與登入](#192-首次連線與登入)
  - [19.3 Workspace 選擇](#193-workspace-選擇)
  - [19.4 Profile 與多環境](#194-profile-與多環境)
  - [19.5 ID 與輸出格式](#195-id-與輸出格式)
  - [19.6 指令總覽](#196-指令總覽)
  - [19.7 常用工作流程範例](#197-常用工作流程範例)
  - [19.8 Agent Task 內的 CLI](#198-agent-task-內的-cli)
  - [19.9 從其他編碼 Agent 驅動 Multica](#199-從其他編碼-agent-驅動-multica)
- [第 20 章：安全模型與治理](#第-20-章安全模型與治理)
  - [20.1 安全邊界就是 Daemon 使用者](#201-安全邊界就是-daemon-使用者)
  - [20.2 建議的隔離部署](#202-建議的隔離部署)
  - [20.3 Multica 實際提供的隔離](#203-multica-實際提供的隔離)
  - [20.4 「不是邊界」的項目](#204-不是邊界的項目)
  - [20.5 機密存放位置矩陣](#205-機密存放位置矩陣)
  - [20.6 資料外流面](#206-資料外流面)
  - [20.7 網路安全](#207-網路安全)
  - [20.8 稽核與可追溯性](#208-稽核與可追溯性)
  - [20.9 SSDLC 整合](#209-ssdlc-整合)
- [第 21 章：系統維運](#第-21-章系統維運)
  - [21.1 健康檢查](#211-健康檢查)
  - [21.2 日誌](#212-日誌)
  - [21.3 Prometheus 指標](#213-prometheus-指標)
  - [21.4 用量彙總（Usage Rollup）](#214-用量彙總usage-rollup)
  - [21.5 維護作業 API](#215-維護作業-api)
  - [21.6 Go Runtime Profiling](#216-go-runtime-profiling)
  - [21.7 疑難排解](#217-疑難排解)
  - [21.8 備份與災難復原](#218-備份與災難復原)
- [第 22 章：升級、擴展與高可用](#第-22-章升級擴展與高可用)
  - [22.1 版本與發版策略](#221-版本與發版策略)
  - [22.2 CLI 與 Daemon 升級](#222-cli-與-daemon-升級)
  - [22.3 Server 升級：Docker Compose](#223-server-升級docker-compose)
  - [22.4 Server 升級：Kubernetes（Helm）](#224-server-升級kuberneteshelm)
  - [22.5 後端水平擴展](#225-後端水平擴展)
  - [22.6 執行層擴展](#226-執行層擴展)
  - [22.7 高可用參考架構](#227-高可用參考架構)
- [第 23 章：企業導入與最佳實務](#第-23-章企業導入與最佳實務)
  - [23.1 分階段導入路線圖](#231-分階段導入路線圖)
  - [23.2 角色分工（RACI）](#232-角色分工raci)
  - [23.3 Issue 撰寫原則](#233-issue-撰寫原則)
  - [23.4 Agent 使用規範](#234-agent-使用規範)
  - [23.5 常見錯誤與對策](#235-常見錯誤與對策)
  - [23.6 成效衡量指標](#236-成效衡量指標)
  - [23.7 參與 Multica 開發的本機環境](#237-參與-multica-開發的本機環境)
- [第 24 章：實戰案例——企業 Web 系統交付](#第-24-章實戰案例企業-web-系統交付)
  - [24.1 案例概要](#241-案例概要)
  - [24.2 步驟 1：環境就緒](#242-步驟-1環境就緒)
  - [24.3 步驟 2：Workspace、Repo 與 Project](#243-步驟-2workspacerepo-與-project)
  - [24.4 步驟 3：Skills 與 Agents](#244-步驟-3skills-與-agents)
  - [24.5 步驟 4：組成 Squad](#245-步驟-4組成-squad)
  - [24.6 步驟 5：建立父 Issue 與分 Stage 的子 Issue](#246-步驟-5建立父-issue-與分-stage-的子-issue)
  - [24.7 步驟 6：監控執行](#247-步驟-6監控執行)
  - [24.8 步驟 7：審查、CI 與合併](#248-步驟-7審查ci-與合併)
  - [24.9 步驟 8：日常自動化](#249-步驟-8日常自動化)
  - [24.10 案例總結](#2410-案例總結)
- [附錄 A：檢查清單](#附錄-a檢查清單)
  - [A.1 初次安裝清單](#a1-初次安裝清單)
  - [A.2 正式部署清單](#a2-正式部署清單)
  - [A.3 Agent 設定清單](#a3-agent-設定清單)
  - [A.4 升級驗收清單](#a4-升級驗收清單)
  - [A.5 安全檢查清單](#a5-安全檢查清單)
  - [A.6 日常維運清單](#a6-日常維運清單)
- [附錄 B：CLI 快速參考卡](#附錄-bcli-快速參考卡)
  - [B.1 連線與設定](#b1-連線與設定)
  - [B.2 Daemon 與 Runtime](#b2-daemon-與-runtime)
  - [B.3 Workspace、成員與 MCP](#b3-workspace成員與-mcp)
  - [B.4 Issue](#b4-issue)
  - [B.5 評論、訂閱、標籤、屬性與 Metadata](#b5-評論訂閱標籤屬性與-metadata)
  - [B.6 Run 與 Wakeup](#b6-run-與-wakeup)
  - [B.7 Project 與 Repo](#b7-project-與-repo)
  - [B.8 Agent、Skill 與 Squad](#b8-agentskill-與-squad)
  - [B.9 Autopilot](#b9-autopilot)
  - [B.10 舊版指令對照](#b10-舊版指令對照)
- [附錄 C：支援的 Agent CLI 對照](#附錄-c支援的-agent-cli-對照)
- [附錄 D：參考資源](#附錄-d參考資源)
  - [D.1 官方資源](#d1-官方資源)
  - [D.2 官方文件頁面對照](#d2-官方文件頁面對照)
  - [D.3 AI 編碼工具官方安裝文件](#d3-ai-編碼工具官方安裝文件)
  - [D.4 舊版手冊連結稽核](#d4-舊版手冊連結稽核)
- [附錄 E：版本歷程與更正紀錄](#附錄-e版本歷程與更正紀錄)
  - [E.1 v0.3.33 → v0.6.1 重大變更摘要](#e1-v0333--v061-重大變更摘要)
  - [E.2 手冊版本與章節對照](#e2-手冊版本與章節對照)
  - [E.3 更正表](#e3-更正表)
- [附錄 F：驗證紀錄](#附錄-f驗證紀錄)
  - [F.1 驗證方法](#f1-驗證方法)
  - [F.2 待確認項目](#f2-待確認項目)
- [附錄 G：術語表](#附錄-g術語表)

<!-- TOC-AUTO-END -->

---

## 第 1 章：Multica 概述與版本基準

> **本章重點：** Multica 的定位、設計哲學、核心價值、與既有工具的差異、適用邊界、v0.6.1 專案現況、Multica License 授權條件，以及 v0.3.33 以來的重大變化。

### 1.1 什麼是 Multica

Multica 是一個 **source-available、可自行部署的「人機協作工作區」**。團隊把工作指派給 AI 編碼代理（Agent）的方式，與指派給同事完全相同：Agent 領取 Issue、在 Issue 中回報進度、提出阻礙（Blocker），最後把成果交回人類審查。

它要解決的問題很具體。多數團隊已經同時在用 Claude Code、Codex、Cursor 等多個 Agent CLI，但每個 Agent 都活在自己的終端機分頁裡：

- Session 結束就遺忘一切，同樣的背景要反覆解釋；
- 工作成果散落在個人終端機與聊天紀錄，團隊看不到；
- Agent 越多，人類花在「保母式」看管上的時間越多。

Multica 的做法是把 Agent 與人類放進同一個工作區：Agent 被指派 Issue 後自行領取，在**你掌控的 Runtime**（自己的電腦或雲端主機）上執行，邊做邊留言，完成後交回審查。需求意圖、執行過程、決策與 Diff 都掛在同一個 Issue 上，因此沒有人需要重建上下文，也沒有任何東西能在未經人類同意的情況下出貨。

> **"Your next 10 hires won't be human."** —— Multica 官方標語
>
> **"Agents that show up on the board."** —— README 副標

Multica 本身**不提供模型**，也不內建 Agent。它驅動的是你已經安裝並登入的 Agent CLI（v0.6.1 共 26 種），因此「換供應商」只是一個下拉選單，而不是一次遷移。

### 1.2 名稱由來與設計哲學

**Multica** = **Mult**iplexed **I**nformation and **C**omputing **A**gent（多工資訊與計算代理）。

名稱致敬 1960 年代的 **Multics** 作業系統。Multics 首創分時共享（Time-Sharing），讓多位使用者共用一台機器，彷彿各自擁有整台機器；Unix 則是 Multics 的刻意簡化——一個使用者、一個任務。

Multica 認為同樣的轉折正在重演：數十年來軟體團隊一直是「單執行緒」的——一位工程師、一個任務、一次上下文切換。Agent 改變了這個等式。Multica 把分時共享帶回來，只是如今多工使用系統的「使用者」同時包含人類與自主 Agent。

官方 [VISION.md](https://github.com/multica-ai/multica/blob/main/VISION.md) 提出的幾個核心主張，是理解產品設計取捨的關鍵：

| 主張 | 對產品設計的影響 |
| --- | --- |
| Agent 是一等隊友 | 指派選單、活動時間軸、Run 生命週期、Runtime 基礎設施從第一天就以「Agent 也是成員」設計 |
| 人類設定方向並負最終責任 | Agent 的成果進入 `in_review`，而不是直接進 `main`；`done` 通常由人確認 |
| 審查工作本身，而非狀態表演 | Issue 直接呈現計畫、Diff、預覽、測試結果與未決問題 |
| 歷史不隨 Session 消失 | 意圖、決策、動作、產出與結果彼此串接，下一個 Agent 不必從零開始 |
| 不是失控的自主公司 | 每一次 Run 都由明確動作觸發（指派、@提及、Chat、Autopilot），Agent 不會自行開工 |

> 💡 **實務建議：** VISION.md 描述的是方向，不是功能清單。評估導入範圍時，應以 README 與官方文件列出的「已上線」功能為準。

### 1.3 核心價值主張

官方 README 把能力分成四組，本手冊章節也大致依此展開：

| 價值主張 | 主要能力 | 對應章節 |
| --- | --- | --- |
| **組建團隊（Build the team）** | 26 種 Agent CLI、Agent 即隊友、Squads、Skills、自有 Runtime | 第 10、11、12、14 章 |
| **交付工作（Hand off the work）** | 指派 Issue、Autopilots、Chat、Projects 與資源 | 第 9、13、15 章 |
| **保持掌握（Stay in the loop）** | 執行紀錄（Transcript）、引導執行中的 Agent（Steer）、用量分析、審查關卡、Inbox、重試與逾時 | 第 13、14、21 章 |
| **為我所用（Make it yours）** | Self-host、自架 Git、Workspace、角色與 Access、安全模型、通訊整合、Web／Desktop／Mobile、CLI 與 API | 第 5–8、16–20 章 |

### 1.4 與既有工具的差異比較

#### 與 AI 編碼工具（Claude Code／Codex／Copilot CLI）

Multica 不是這些工具的替代品，而是它們的**協調層**。

| 面向 | 單獨使用 Agent CLI | 透過 Multica 使用 |
| --- | --- | --- |
| 互動模式 | 人在終端機逐步對話 | 指派 Issue，Agent 自主領取並執行 |
| 上下文保存 | Session 結束即失 | Issue 描述、討論、Run 紀錄永久保存；支援 Session 續接 |
| 團隊可見性 | 僅執行者本人可見 | 全 Workspace 共享時間軸、執行紀錄與成本 |
| 多 Agent 協作 | 人工在多個終端機間複製貼上 | Squad Leader 依內容分派；Agent 間 @提及交接 |
| 方法沉澱 | 散落在個人提示詞 | Workspace Skills，可綁定多個 Agent 並集中更新 |
| 排程與事件觸發 | 自行寫 cron／腳本 | Autopilots（Cron／Webhook／手動）與 Issue Wakeup |
| 供應商綁定 | 綁定單一工具 | 26 種 CLI 可隨時切換 |

#### 與任務管理工具（Jira／Linear）

| 面向 | Jira／Linear | Multica |
| --- | --- | --- |
| 執行者 | 人類 | 人類、Agent、Squad 皆可為 Assignee |
| 指派後的行為 | 通知負責人 | 指派給 Agent 即建立 Run 並開始執行 |
| 程式碼產出 | 無 | Agent 在 Runtime 上改碼、推分支、開 PR |
| 執行環境 | 無 | Runtime 管理（本機 Daemon、自訂 Runtime Profile） |
| 自訂欄位／狀態 | 完整 | 自訂屬性（9 種型別）、自訂狀態（4 種生命週期類別）、儲存檢視 |
| 成熟度 | 成熟的企業級產品 | 仍為 0.x、平日幾乎每天發版 |

> 💡 **實務建議：** Multica 的 Issue 模型足以支撐「Agent 可執行的工作」，但若組織已有成熟的 Jira／Linear 流程，較穩健的做法是讓 Multica 專注於 Agent 執行層，正式需求管理仍保留在既有系統，並以 Webhook Autopilot 串接（見第 15 章）。

### 1.5 適用場景與導入邊界

**適合導入的情境：**

| 場景 | 說明 |
| --- | --- |
| 同時使用兩種以上 Agent CLI 的團隊 | 統一看板、統一紀錄、統一成本視角 |
| 企業內部 Web／微服務開發 | Spring Boot、Vue 等標準化專案，以 Skills 固化團隊慣例 |
| 遺留系統逐步重構 | 拆成多個子 Issue，以 Stage 分批推進 |
| 定期維運與報告 | Autopilot 產生每日站立會議摘要、依賴檢查、週報 |
| 事件驅動處理 | CI 失敗、監控告警經 Webhook 觸發 Agent 初步分析 |
| 需要資料留在內網 | Self-host 全套服務，程式碼與 Agent 憑證留在 Runtime 主機 |

**需謹慎評估或不適合的情境：**

| 情境 | 原因 |
| --- | --- |
| 一次只跑一個 Agent、一個任務 | 終端機已足夠，Multica 帶來的協調價值有限 |
| 要求穩定 API 合約與長期支援版本 | 0.x 階段、`main` 移動快速，官方未提供 LTS |
| 無法接受 Agent 以 Daemon 使用者完整權限執行 | Multica 不提供檔案系統沙箱（見第 20 章），必須自行以專用帳號／容器／VM 隔離 |
| 需要 Android 行動端或 App Store 版 iOS | 目前 iOS 需自行從原始碼建置，無 Android 用戶端 |
| 對外提供託管服務 | 需向原廠取得商業授權（見 1.7） |

#### 外部評測的疑慮與 v0.6.1 現況

2026 年 4–5 月的第三方評測（基於 v0.2.16–v0.2.27）曾提出若干疑慮。下表整理這些疑慮在 v0.6.1 的狀態，協助評估時避免引用過時資訊：

| 早期評測疑慮 | v0.6.1 現況 |
| --- | --- |
| 缺少自訂欄位、細緻權限 | 已提供自訂屬性（9 種型別）、自訂狀態、Agent Access、owner／admin／member 角色 |
| Project 無法綁定 Repo | 已提供 Project Resources（GitHub Repo、本機目錄、`ref` 指定） |
| 驗證碼端點缺乏暴力破解防護 | 已提供 `RATE_LIMIT_AUTH`／`RATE_LIMIT_AUTH_VERIFY`（需 `REDIS_URL` 才生效） |
| `custom_env` 讀取無稽核 | 列表與詳情 API 不再回傳值；僅 owner／admin 可解鎖，每次讀寫留稽核紀錄 |
| Claude Agent 無法使用 MCP（Issue #1111） | 已於 2026-04 修正；v0.4.27 起另有 Workspace MCP 函式庫 |
| Skill 匯入二進位附件失敗（Issue #1705） | **仍未解決**（2026-10-05 確認為 open），Skill 附件請以文字檔為主 |
| 僅支援 11 種 Agent | 已擴增至 26 種 CLI |

### 1.6 專案基本資訊

| 項目 | 資訊（2026-10-05 查詢） |
| --- | --- |
| GitHub | [multica-ai/multica](https://github.com/multica-ai/multica) |
| 開發商 | Index Labs (Hong Kong) Limited |
| 基準版本 | v0.6.1（2026-10-01） |
| 發版節奏 | 官方表示「多數平日都會發版」；v0.3.34 → v0.6.1 共 61 個 Release（2026-07-01 至 10-01） |
| Stars／Forks | 約 52,000／6,750 |
| 主要語言 | Go、TypeScript、MDX、PLpgSQL |
| 官網／文件 | [multica.ai](https://multica.ai)・[multica.ai/docs](https://multica.ai/docs)（英、簡中、日、韓、法） |
| 下載 | [multica.ai/download](https://multica.ai/download)（Desktop：macOS／Windows／Linux） |
| 容器映像 | `ghcr.io/multica-ai/multica-backend`、`ghcr.io/multica-ai/multica-web` |
| Helm Chart | `oci://ghcr.io/multica-ai/charts/multica`（版本號＝Git Tag 去掉 `v`） |
| CLI 套件 | GitHub Release 二進位、Homebrew `multica-ai/tap/multica`、安裝腳本 |
| CLI Skill | [multica-ai/multica-cli](https://github.com/multica-ai/multica-cli)（讓 Claude Code／Codex／Cursor 操作 Multica） |
| 社群 | [Discord](https://discord.gg/W8gYBn226t)・[X @MulticaAI](https://x.com/MulticaAI) |

### 1.7 授權模式：Multica License

v0.6.1 的授權為 **Multica License**：由 **Part I 附加條件** 與 **Part II Apache License 2.0 全文** 共同構成，兩者衝突時以 Part I 為準。舊版手冊所稱「Multica Source Available License」已不再是正式名稱。

| 條件 | 內容摘要 | 企業影響 |
| --- | --- | --- |
| **1(a) 託管或嵌入服務** | 未取得商業授權，不得以 Multica 原始碼對第三方提供託管服務，或嵌入對第三方銷售／授權的產品 | 對組織外部使用者開放的公開實例，**即使免費、無廣告**也需商業授權 |
| **1(a) 內部使用** | 單一組織內部使用（含多個 Workspace）不需商業授權 | 企業內部自架屬允許範圍 |
| **1(a) 公開原始碼** | 公開 Fork 的原始碼本身不算託管服務 | 但接收者若要營運服務仍須各自取得授權 |
| **1(b) 品牌與版權** | 未經書面豁免，不得移除或修改 Multica UI 上的 LOGO、產品名稱與版權資訊 | 不可自行「白牌化」Web／Desktop／Mobile 介面 |
| **1(c) 非介面使用署名** | 若只用後端／Daemon／CLI 打造產品，須保留 NOTICE 並在文件中聲明建構於 Multica 並附連結 | 內部平台整合時須保留署名 |
| **1(d) 授權彼此獨立** | 品牌豁免不等於商業授權，反之亦然 | 兩者需分別向原廠申請 |
| **2 貢獻條款** | 貢獻者同意原廠可調整授權、可將貢獻用於商業用途 | 企業若要回饋上游，須經法務確認 |
| **3(d) 再散布** | 再散布時必須附上完整 LICENSE 檔，只附 Apache 2.0 不符合規定 | 內部映像倉庫轉存時一併保留 |

| 使用情境 | 是否需商業授權 |
| --- | --- |
| 企業內部自架，供自家員工使用 | 否 |
| 集團內多個 Workspace | 否（同一組織） |
| 修改原始碼供內部使用 | 否（仍須保留 UI 品牌與版權） |
| 對客戶／外部合作夥伴開放的實例 | **是** |
| 以 SaaS 或託管服務形式提供 | **是** |
| 嵌入自家商業產品販售 | **是** |

> ⚠️ **注意：** 以上為技術人員的條文摘要，不構成法律意見。導入前請由法務審閱完整 [LICENSE](https://github.com/multica-ai/multica/blob/main/LICENSE) 與 [NOTICE](https://github.com/multica-ai/multica/blob/main/NOTICE)。商業授權與品牌豁免申請窗口為 <https://www.multica.ai/contact-sales>。

### 1.8 v0.3.33 以來的重大變化速覽

舊版手冊撰寫於 v0.3.33（2026-06-30）。之後三個月的 61 個 Release 帶來大幅變化，主要里程碑如下（完整清單見[附錄 E.1](#e1-v0333--v061-重大變更摘要)）：

| 版本 | 日期 | 重大變化 |
| --- | --- | --- |
| v0.3.34 | 07-01 | Slack `/issue` 斜線指令、TRAE CLI Runtime |
| v0.3.36 | 07-03 | Helm 支援外部 PostgreSQL（`postgres.external.enabled`） |
| v0.3.42 | 07-09 | Chat 獨立分頁 |
| v0.4.0 | 07-13 | 對話式建立 Agent、標籤、一個 GitHub Repo 可接多個 Workspace |
| v0.4.2 | 07-15 | 自訂 Issue 欄位、Agent Access 範圍、Grok Runtime |
| v0.4.10 | 07-24 | 自架 Git（Forgejo／Gitea／GitLab）、Project-aware Chat |
| v0.4.20 | 08-06 | 釘釘（DingTalk）Bot、每次 Run 的 Token 成本 |
| v0.4.21 | 08-07 | 企業微信（WeCom）Bot、Analytics 頁面 |
| v0.4.25 | 08-13 | Telegram Bot、本機目錄平行（worktree）模式 |
| v0.4.27 | 08-17 | Workspace MCP 伺服器函式庫、分享連結邀請 |
| v0.4.34 | 08-25 | 自訂 Issue 狀態開放所有 Workspace、評論轉子 Issue |
| v0.4.43 | 09-11 | Redis Cluster／Serverless Redis 支援 |
| v0.4.44 | 09-15 | Self-host 匿名遙測（`DO_NOT_TRACK=1` 關閉） |
| v0.5.0 | 09-18 | 法文介面、Session 滑動續期 |
| v0.5.1 | 09-21 | Issue Wakeup 規則、Project 起始分支 |
| v0.5.2 | 09-23 | Steer 執行中的 Claude Code／Codex、重複 Issue 標記 |
| v0.6.0 | 09-28 | 條件式 Wakeup v2、即時搜尋、交付物預覽、新設定頁 |
| v0.6.1 | 10-01 | 累積成本曲線、CLI `--duplicate-of` |

---

## 第 2 章：核心概念與運作原理

> **本章重點：** Multica 的十個核心物件及其關係、一次 Run 的完整路徑、Multica 與執行電腦之間的資料邊界、四種觸發方式，以及「Run 完成」與「Issue 完成」的差別。

### 2.1 核心物件總覽

| 類別 | 物件 | 定義 |
| --- | --- | --- |
| 基本物件 | **Workspace（工作區）** | 團隊協作的封閉範圍；成員、Issue、Agent、Skill、Run 紀錄都屬於某個 Workspace，彼此完全隔離 |
| | **Issue** | 一件待完成的工作，以及隨之累積的描述、討論、狀態與歷史；Assignee 可以是成員、Agent 或 Squad |
| | **Project** | 把同一目標下的多個 Issue 組織起來，追蹤進度，並可綁定 Repo 與目錄等執行資源 |
| Agent 與執行 | **Agent** | Workspace 中的 AI 協作者，是一組可重用的設定（名稱、指令、模型、Skills、Access、Runtime）；**不是常駐行程**，只在被觸發時執行 |
| | **Skill（技能）** | 可重用的能力包。Instructions 定義 Agent「是誰」，Skill 描述「某類工作怎麼做」，可綁定多個 Agent |
| | **Runtime** | 實際執行的地方：一台連上 Multica 的電腦，加上其上的一種 AI 編碼工具 |
| | **Run（執行）** | Agent 的一次具體執行紀錄。每次觸發都產生一個 Run；一個 Issue 可隨時間產生多個 Run |
| 協作與自動化 | **Squad（小隊）** | 由一個 Leader Agent 帶領的 Agent 與成員群組；指派給 Squad 時由 Leader 協調 |
| | **Chat** | 不掛在任何 Issue 上的一對一對話，每則訊息觸發一次 Run |
| | **Inbox** | 成員的通知中心；Agent 不使用 Inbox |
| | **Autopilot** | 依排程或外部事件自動觸發 Agent Run，也可手動執行 |

> 💡 **術語說明：** 官方自 v0.4.40 起在產品與文件中統一將 Agent 的每次執行稱為 **Run**；程式碼、API 與資料庫仍沿用 `task`（例如 `TaskService`、`task_id`、`multica issue cancel-task`）。本手冊以「Run」稱呼產品概念，引用 API／CLI 時保留原名。

### 2.2 物件關係

```mermaid
flowchart LR
    subgraph WS["Workspace"]
        P["Project"] --> I["Issue"]
        I -->|"指派 / @提及"| A["Agent"]
        C["Chat"] --> A
        AP["Autopilot"] --> A
        SQ["Squad"] -->|"Leader 分派"| A
        SK["Skill"] -.->|"綁定"| A
        A -->|"產生"| R["Run"]
        R -->|"結果寫回"| I
        I -->|"通知"| IN["Inbox（成員）"]
    end
    R -->|"由其領取執行"| RT["Runtime（你的電腦 + AI 工具）"]
```

關係重點：

- **Workspace** 是一切的容器，人類與 Agent 在其中協作。
- **Issue** 記錄一件工作；相關 Issue 以 **Project** 組織。
- 指派、@提及、**Chat**、**Autopilot** 觸發 Agent，產生 **Run**。
- Run 在 **Runtime** 上完成，結果寫回觸發它的地方。
- **Skill** 讓有效方法跨 Agent 重用；**Squad** 讓多個 Agent 協同工作。
- 過程中所有給人看的通知都進 **Inbox**。

### 2.3 一次 Run 的完整路徑

```mermaid
sequenceDiagram
    autonumber
    participant U as 成員
    participant S as Multica Server
    participant D as Daemon（執行電腦）
    participant T as AI 編碼工具
    U->>S: 指派 Issue 給 Agent
    S->>S: 建立 Run（queued）
    S-->>D: WebSocket 喚醒（另有輪詢備援）
    D->>S: 領取 Run（dispatched）
    S->>D: 發放綁定此 Run 的臨時 Token（mat_）
    D->>D: 準備工作目錄、注入 Skills / MCP / 環境變數
    D->>T: 啟動 AI 工具（running）
    T->>T: 讀檔、執行指令、修改程式碼
    T->>S: 透過 multica CLI 留言、更新狀態
    D->>S: 串流進度訊息與最終結果
    S-->>U: 即時更新時間軸與執行紀錄
```

1. **Issue 提供上下文**：描述、討論與 Assignee；指派給 Agent 時套用該 Agent 的指令、模型、Skills 與 Runtime。
2. **Multica 建立 Run**：進入佇列；若沒有 Runtime 在線，就在佇列中等待。
3. **Runtime 領取 Run**：在線的 Runtime 領取後呼叫 Agent 設定的 AI 編碼工具。
4. **AI 工具在本機執行**：讀取工作目錄、執行指令、產生結果。
5. **結果寫回 Issue**：進度、留言與結果出現在 Issue 時間軸與執行紀錄中。

### 2.4 資料與執行邊界

| 存放於 Multica（Cloud 或自架 Server） | 存放於執行電腦（Runtime 主機） |
| --- | --- |
| Workspace、Issue、留言與狀態 | AI 編碼工具本身及其登入憑證 |
| Agent 設定與 Skills | 程式碼目錄與本機檔案 |
| Run 狀態、紀錄與結果 | 實際的檔案變更與指令執行 |

此邊界在 Multica Cloud 與自架部署中完全相同。

> ⚠️ **注意：** 有兩類例外會存放在 Server 端：Agent 的 **`custom_env`（環境變數）** 與 **MCP 設定**。兩者以明文儲存於 Server 資料庫，於執行時下發給 Runtime。不可把「必須永遠不離開本機」的機密放進這兩處。此外，Agent 在回覆中引用的程式碼片段也會寫入 Server。

### 2.5 四種觸發方式

Agent **永遠不會自行開工**，每一次 Run 都來自明確的動作：

| 方式 | 適用情境 | 操作 |
| --- | --- | --- |
| **指派 Issue** | Agent 端到端負責這件工作 | 將 Issue 的 Assignee 設為 Agent；Issue 處於 `todo` 或之後的狀態時立即開始 |
| **在評論中 @提及** | 請 Agent 處理某個具體請求，不改變 Assignee | 在評論中 @Agent，或回覆 Agent 的評論延續對話 |
| **直接 Chat** | 不需要 Issue 的提問或快速嘗試 | 開啟 Chat 與 Agent 對話，每則訊息觸發一次 Run |
| **Autopilot** | 依排程或外部事件重複執行的工作 | 建立 Autopilot，以排程、Webhook 或手動觸發 |

四種方式共同遵守的規則：

- 只能觸發**你有權執行**的 Agent，由 Agent 的 Access 決定，與你的 Workspace 角色無關。
- 從 Issue 觸發前，輸入框下方的**觸發預覽**會明確列出這則內容會喚醒誰；以 `/note` 開頭可留言而不觸發任何 Agent。
- 處於 `backlog` 的 Issue 不觸發 Run；移到 `todo` 後，已指派的 Agent 才開始。

另有一種「延續型」觸發：**Issue Wakeup**（v0.5.1+，v0.6.0 擴充為條件式），讓 Agent 在事件、條件或時間到達時，再收到一次普通 Run。詳見第 13.8 節。

### 2.6 Run 完成 ≠ Issue 完成

執行紀錄顯示 `completed`，只代表**那一次 Run** 正常結束，不代表 Issue 的目標已達成。Issue 仍可繼續討論、補充需求或再次觸發 Agent。

| 判斷依據 | 說明 |
| --- | --- |
| Run 狀態 | 單次執行的技術結果（`completed`／`failed`／`cancelled`） |
| Issue 狀態 | 工作的業務進度，由 Agent 透過 CLI 明確寫入（`in_progress`、`in_review`）或由人類確認（`done`） |

Server **不會**因為 Run 開始或結束而自動翻轉 Issue 狀態，只有兩個系統例外（見第 9.3 節）。

---

## 第 3 章：系統架構設計

> **本章重點：** 用戶端、Go 後端、PostgreSQL、Redis 與本機 Daemon 的分工；Repository 結構與後端分層；兩條 WebSocket 路徑；一次執行的程式碼路徑；多 Workspace 隔離原則；企業參考部署拓樸。

### 3.1 整體架構

```mermaid
flowchart TB
    subgraph Clients["用戶端"]
        WEB["Web（Next.js 16）"]
        DESK["Desktop（Electron）"]
        MOB["iPhone / iPad（Expo）"]
        CLI["multica CLI / API 腳本"]
    end
    subgraph ServerSide["Multica 服務（Cloud 或自架）"]
        NEXT["Next.js 伺服器<br/>頁面 + /api /auth /uploads 代理"]
        API["Go 後端<br/>Chi + WebSocket + 排程器 + 整合 Worker"]
        PG[("PostgreSQL 17<br/>pgcrypto + pg_trgm")]
        RD[("Redis（選用）")]
        OBJ[("附件儲存<br/>本機磁碟 / S3")]
    end
    subgraph Exec["執行電腦（你的機器）"]
        DAEMON["Agent Daemon"]
        TOOLS["Claude Code / Codex / Cursor / ..."]
        REPO["工作目錄與程式碼"]
    end
    WEB --> NEXT
    NEXT --> API
    DESK -->|"HTTPS + WebSocket"| API
    MOB -->|"HTTPS + WebSocket"| API
    CLI -->|"HTTPS（PAT）"| API
    API --> PG
    API -.-> RD
    API --> OBJ
    DAEMON -->|"/api/daemon/ws + 輪詢"| API
    DAEMON -->|"啟動"| TOOLS
    TOOLS --> REPO
```

架構上最重要的設計決策是：**Server 只負責記錄與協調，執行永遠發生在你連上來的電腦**。因此 AI 工具的憑證、原始碼與檔案變更都留在執行電腦上，Server 不會代替本機工具執行指令，也不會上傳整個工作目錄。

### 3.2 技術棧

| 層 | 技術 | 說明 |
| --- | --- | --- |
| Web | Next.js 16（App Router） | 瀏覽器用戶端與 Landing Page；以 rewrites 將 `/v1`、`/api`、`/auth`、`/uploads` 代理到後端 |
| Desktop | Electron、electron-vite | 與 Web 共用 UI 套件，並自動管理本機 Daemon |
| Mobile | Expo／React Native | 獨立 iOS 用戶端（iPhone、iPad），可匯入 `@multica/core` 的型別與純函式 |
| 後端 | Go（Chi router、sqlc、gorilla/websocket） | 單一執行檔，負責 API、驗證、Run 排程、整合、CLI 與 Daemon |
| 資料庫 | PostgreSQL 17 | 必要擴充：`pgcrypto`、`pg_trgm`；選用：`pg_bigm`（CJK 搜尋品質）、`pg_cron`（相容用） |
| 快取／協調 | Redis（選用） | 跨副本即時事件、共享速率限制、通訊 Bot 連線租約、Token 快取 |
| 附件 | 本機磁碟或 S3 相容儲存 | 支援 CloudFront 簽章、Presign、Proxy 等下載模式 |
| Agent 執行 | 本機 Daemon | 偵測並驅動 26 種 Agent CLI |
| 文件站 | Next.js + Fumadocs | 五種語言 |

> ⚠️ **更正：** 舊版手冊將資料庫寫為「PostgreSQL 17 + pgvector」。依 v0.6.1 官方 `SELF_HOSTING_ADVANCED.md`，**Multica 不使用 pgvector**——沒有任何 Migration 宣告 `vector` 欄位或執行 `CREATE EXTENSION vector`。內建映像名稱 `pgvector/pgvector:pg17` 僅為歷史因素，一般 PostgreSQL 17 即可。

### 3.3 Repository 結構

| 目錄 | 職責 | 主要技術 |
| --- | --- | --- |
| `server/` | API、驗證、Run 排程、整合、CLI 與 Daemon | Go、Chi、sqlc、gorilla/websocket |
| `apps/web/` | 瀏覽器用戶端與 Landing Page | Next.js App Router |
| `apps/desktop/` | 桌面用戶端與本機行程管理 | Electron、electron-vite |
| `apps/mobile/` | 獨立 iOS 用戶端 | Expo、React Native |
| `apps/docs/` | 多語系文件站 | Next.js、Fumadocs |
| `packages/core/` | API Client、型別、Query／Mutation、平台無關業務邏輯 | TanStack Query、Zustand |
| `packages/ui/` | 無業務邏輯的基礎 UI | shadcn、Base UI |
| `packages/views/` | Web 與 Desktop 共用的業務頁面與元件 | React |
| `deploy/helm/multica/` | Kubernetes Helm Chart | Helm |

前端依賴方向固定為 `views → core + ui`，`core` 與 `ui` 彼此不依賴。伺服器資料由 TanStack Query 管理，用戶端狀態（篩選、草稿、對話框）由 Zustand 管理；WebSocket 事件只負責更新或使快取失效，不把伺服器物件複製進 Zustand。API 回應在 `packages/core/api/` 邊界以 zod schema 解析，因為已安裝的 Desktop 可能連到較新的後端。

### 3.4 後端分層

`server/cmd/` 的主要進入點：

| 進入點 | 用途 |
| --- | --- |
| `server` | 啟動 HTTP API、WebSocket、排程器與整合 Worker |
| `multica` | CLI 與本機 Daemon |
| `migrate` | 執行資料庫 Migration |
| `backfill_*` | 特定版本的資料回填工具（例如 `backfill_task_usage_hourly`） |
| `maintenance` | 維護作業 HTTP 用戶端（容器內 `/app/maintenance`） |

請求流向：

```text
router → middleware → handler → service → sqlc query → PostgreSQL
```

| 套件 | 職責 |
| --- | --- |
| `internal/middleware/` | 驗證、Workspace 與請求邊界 |
| `internal/handler/` | 解析 HTTP 輸入、產生回應 |
| `internal/service/` | 跨查詢的業務流程與交易 |
| `pkg/db/queries/` | 手寫 SQL |
| `pkg/db/generated/` | sqlc 產生碼（禁止手動修改） |
| `internal/integrations/` | GitHub、Slack、飛書、釘釘、企業微信、Telegram 等外部事件 |
| `internal/storage/` | 本機與 S3 附件 |
| `internal/realtime/`、`internal/daemonws/` | 兩條 WebSocket 路徑 |
| `internal/metrics/` | Prometheus 指標 |

PostgreSQL 是業務資料的唯一真實來源（Source of Truth）。沒有 Redis 時，單一實例會改用行程內實作。

### 3.5 即時通訊：兩條 WebSocket 路徑

| 路徑 | 端點 | 對象 | 用途 |
| --- | --- | --- | --- |
| `internal/realtime/` | `/ws` | 使用者用戶端 | 推送 Issue、留言、Inbox 等變更 |
| `internal/daemonws/` | `/api/daemon/ws` | Daemon | 喚醒 Runtime、執行 Daemon RPC |

設計原則：

- WebSocket 只用來**降低延遲**，資料庫才是最終狀態；用戶端重連後必須以查詢重新校正。
- Daemon 仍保留**輪詢路徑**（預設每 `30s` 補查；健康 WebSocket 下的安全輪詢上限 `3m`），避免單次斷線讓佇列中的 Run 永遠卡住。
- 若反向代理沒有把 `/api/daemon/ws` 導向後端，Daemon 會**靜默退回輪詢**——功能仍可用但延遲變高，後端日誌會出現該路徑重複的 `status=400`。
- 伺服器 Pod 重啟期間發布的即時事件，有 5 分鐘的有界重播視窗（v0.3.36+）。

### 3.6 一次執行的程式碼路徑

1. 使用者指派 Issue、@提及 Agent，或自動化觸發。
2. `TaskService` 建立 `queued` 的 Run，並通知對應 Runtime。
3. Daemon 透過 Daemon API 領取 Run。
4. Server 發放**綁定此 Run 與 Agent 的臨時憑證**（`mat_` 前綴，最長 24 小時，Run 結束即清除）。
5. Daemon 準備本機目錄，呼叫 `pkg/agent` 中對應的 Provider 後端。
6. AI 工具在本機執行，Daemon 上傳進度、訊息與最終狀態。
7. Server 更新 Run 與 Issue，並透過即時事件刷新用戶端。

Provider 轉接層統一了各 AI 工具在啟動、串流事件、取消與用量資料上的差異；本機目錄與 Session 則由 Daemon 管理。

### 3.7 多 Workspace 隔離

- 所有業務查詢都必須以 `workspace_id` 限定範圍；請求進入 Workspace 路由前先檢查成員資格。
- `X-Workspace-ID` 標頭只用來**選擇**目前的 Workspace，不能取代授權檢查。
- Issue 的 Assignee 是多型（成員、Agent 或 Squad），查詢、快取鍵與即時事件都必須同時保留 Workspace 與 Assignee 型別。

### 3.8 企業參考部署拓樸

📘 **建議實務：** 下圖為中大型企業內部部署的參考拓樸，組合了官方文件中的同源部署、Redis 多副本、外部 PostgreSQL 與專用 Daemon 主機建議。

```mermaid
flowchart LR
    subgraph DMZ["內網入口"]
        LB["反向代理 / Ingress<br/>TLS 終結"]
    end
    subgraph App["應用層（K8s 或 VM）"]
        FE1["multica-web x2"]
        BE1["multica-backend x2+"]
    end
    subgraph Data["資料層"]
        PGHA[("PostgreSQL 17<br/>主從 + 唯讀副本")]
        RDS[("Redis / Redis Cluster")]
        S3[("S3 相容物件儲存")]
    end
    subgraph Runners["執行層（隔離網段）"]
        R1["Daemon 主機 A<br/>專用帳號 / 容器"]
        R2["Daemon 主機 B<br/>專用帳號 / 容器"]
    end
    LB -->|"/ 與 /api"| FE1
    LB -->|"/ws、/api/daemon/ws、/health"| BE1
    FE1 --> BE1
    BE1 --> PGHA
    BE1 --> RDS
    BE1 --> S3
    R1 -->|"HTTPS / WSS"| LB
    R2 -->|"HTTPS / WSS"| LB
```

| 層 | 建議 | 依據 |
| --- | --- | --- |
| 入口 | 同源部署（單一網域），`/ws`、`/api/daemon/ws`、`/health` 直接導向後端 | 第 5.6 節；避免跨網域 Cookie 風險 |
| 後端 | 2 個以上副本，並設定 `REDIS_URL` | 多副本的即時事件、速率限制、企業微信回覆轉送都依賴 Redis |
| 資料庫 | 外部託管 PostgreSQL 17，連線池預算＝副本數 × `DATABASE_MAX_CONNS` | 第 22 章 |
| 附件 | S3 相容儲存；內網端點用 `ATTACHMENT_DOWNLOAD_MODE=proxy` | 第 6.4 節 |
| 執行層 | 獨立主機／網段，以專用 Unix 帳號或容器執行 Daemon | 第 20 章安全模型 |

---

## 第 4 章：快速入門

> **本章重點：** 三種起步方式（Cloud、Desktop、Self-host）的選擇；以五個步驟完成第一個 Agent 的第一次 Run；官方 Tutorial 的學習路徑；常見的起步問題。

### 4.1 起步方式選擇

| 方式 | 說明 | 適合 |
| --- | --- | --- |
| **Cloud** | 在 [multica.ai](https://multica.ai) 註冊，免終端機 | 個人試用、小團隊快速評估 |
| **Desktop** | 下載 [Multica Desktop](https://multica.ai/download)（macOS／Windows／Linux），登入後自動把本機註冊為 Runtime | 開發者日常使用，不想手動管理 Daemon |
| **Self-host** | 在自有基礎設施執行整套服務（第 5 章） | 企業內部、資料需留在內網 |

唯一的前置條件：**要執行 Agent 的電腦上，至少安裝並登入一種[支援的 AI 編碼工具](#143-支援的-ai-編碼工具)**（Claude Code、Codex、Cursor 等）。Multica 驅動這些工具，但不隨附它們。

### 4.2 五步驟完成第一次 Run

#### 步驟 1：登入並開啟 Workspace

在 Web 或 Desktop 登入，支援 Email 驗證碼與 Google 登入。首次登入時建立 Workspace（名稱、URL slug、Issue 前綴，見第 8 章）。

#### 步驟 2：連接一台電腦

開啟側欄底部的 **Configure → Runtimes**：

- **使用 Desktop**：Desktop 會自動把這台電腦註冊為 Runtime 並偵測已安裝的 AI 工具；剛安裝的工具按 **Refresh** 重新偵測。
- **使用 Web，或要再加一台電腦**：點右上角 **Add a computer**，在目標電腦的終端機執行對話框中的兩行指令。

macOS／Linux：

```bash
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
multica setup
```

Windows PowerShell：

```powershell
irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex
multica setup
```

`multica setup`（預設子指令為 `cloud`）會開啟瀏覽器完成登入，並讓 Daemon 在背景執行。Daemon 上線後，對話框通常在一分鐘內偵測到這台電腦。

**成功檢核：** Runtime 列表出現一台在線（online）的電腦。

#### 步驟 3：建立 Agent

開啟側欄 **Workspace → Agents**，點 **New agent**，選擇一種起點：

| 起點 | 說明 |
| --- | --- |
| **Start blank** | 自行填寫欄位；嚴格必填只有名稱，再確認 Runtime 與 AI 工具即可建立 |
| **Build with AI** | 描述你要的 Agent，Agent Builder 會提問並產生設定草稿；需要一個在線的 Runtime |

**成功檢核：** Agent 出現在列表中並顯示為在線。

#### 步驟 4：交付第一個 Issue

點側欄頂端 **New Issue**（或按 `C`），在預設的 Agent 模式下：

1. 在 **Created by** 選擇剛建立的 Agent；
2. 用一兩句話描述工作，例如「說明這個 Workspace 可以怎麼使用」；
3. 送出。Multica 建立 Issue、把 Agent 設為 Assignee，並立即開始執行。

#### 步驟 5：觀察進度與結果

開啟 Issue：右側欄的 **Execution log** 顯示 Run 狀態，Agent 的進度與回覆出現在時間軸。點 **View transcript** 可看完整的工具呼叫與輸出。

**成功檢核：** 執行紀錄狀態變為 `Completed`，時間軸出現 Agent 的回覆。

### 4.3 官方 Tutorial 學習路徑

官方 [Tutorial](https://multica.ai/docs/tutorial) 以「從空 Workspace 到一支能自我運轉的團隊」為主線，建議新進成員依序完成：

| 階段 | 內容 | 學到的能力 |
| --- | --- | --- |
| 1 | 建立 Workspace、連接電腦、建立第一個 Agent | Runtime 與 Agent 的關係 |
| 2 | 透過 Chat 建立第二個 Agent | Build with AI |
| 3 | 準備網站 Repo，發第一個 Issue 讓 Agent 建站 | 指派與執行紀錄 |
| 4 | 在 Issue 中討論、簽核，把回饋寫回 Agent 指令 | 迭代 Agent Instructions |
| 5 | 建立第三個 Agent：Reviewer，合併並結案 | 人機審查流程 |
| 6 | 組成 Squad，把第二個 Issue 交給 Squad | Leader 分派 |
| 7 | 建立 Skill | 方法重用 |
| 8 | 設定 Autopilot、邀請其他成員 | 自動化與團隊協作 |

### 4.4 起步常見問題

| 症狀 | 優先檢查 |
| --- | --- |
| 找不到 Runtime | 確認 AI 工具已安裝且能在終端機執行；Desktop 按 **Refresh**，CLI 路徑重新執行 `multica setup` |
| Runtime 顯示離線 | 保持 Desktop 開啟；CLI 路徑執行 `multica daemon status`，未執行則 `multica daemon start` |
| Issue 一直 queued | 確認 Agent 使用的 Runtime 在線；Runtime 達到併發上限時新 Run 會持續排隊 |
| Build with AI 無法使用 | 需要至少一個在線的 Runtime |

更多情境見第 21.7 節疑難排解。

---

## 第 5 章：Self-Host 安裝與部署

> **本章重點：** 自架的兩個組成部分；一鍵安裝腳本（含 Windows）；Docker Compose 逐步部署與驗證；登入驗證碼取得方式；連接執行電腦；遠端存取的三種反向代理佈局與 Cookie／CSRF 陷阱；Kubernetes Helm 部署；私有 CA；不使用 Docker 的手動部署；停止服務與切換 Cloud。

### 5.1 部署組成與模式選擇

自架 Multica 由兩個部分組成，兩者可以是同一台機器，也可以分開：

| 部分 | 執行內容 | 所在位置 |
| --- | --- | --- |
| **Multica 服務** | Web、API、PostgreSQL | 一台安裝 Docker 的機器（或 K8s 叢集） |
| **執行電腦** | Multica Daemon 與 AI 編碼工具 | 開發者實際工作的電腦或專用 Runner 主機 |

自架只取代 Multica Cloud 的部分；執行電腦的角色在 Cloud 與自架中完全相同。

| 部署模式 | 適用情境 | 章節 |
| --- | --- | --- |
| 一鍵安裝腳本 | 單機 PoC、個人或小團隊 | 5.3 |
| Docker Compose（`make selfhost`） | 單機正式環境、部門級使用 | 5.4 |
| Kubernetes Helm | 已有 K8s 平台、需要多副本 | 5.7 |
| 手動編譯（無 Docker） | 特殊環境、二次開發 | 5.9 |

### 5.2 前置條件

**Multica 服務主機：**

- Docker Engine 或 Docker Desktop，且 `docker compose`（Compose v2）可用；**不支援舊版 `docker-compose` v1**；
- Git、Make、curl、OpenSSL；
- 本機埠 `3000`（Web）與 `8080`（API）未被占用。

```bash
docker info
docker compose version
```

**執行電腦：**

- 至少一種已安裝並登入的 AI 編碼工具（見第 14.3 節）；
- Multica CLI（於 5.5 節安裝）。

### 5.3 一鍵安裝（Quick Install）

兩行指令完成 CLI 安裝、伺服器佈建與設定。

macOS／Linux：

```bash
# 1. 安裝 CLI 並佈建 self-host 伺服器
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server

# 2. 設定 CLI、登入並啟動 Daemon
multica setup self-host
```

Windows PowerShell：

```powershell
# 1. 安裝 CLI 並佈建 self-host 伺服器
$env:MULTICA_MODE="with-server"; irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex

# 2. 設定 CLI、登入並啟動 Daemon
multica setup self-host
```

安裝腳本的行為：

| 項目 | 說明 |
| --- | --- |
| 伺服器資產位置 | 預設 checkout 到 `~/.multica/server`（可用 `MULTICA_INSTALL_DIR` 覆寫） |
| 版本 | 預設取最新 Release Tag；可用 `MULTICA_SELFHOST_REF` 指定 |
| 映像 | 從 GHCR 拉取官方 `multica-backend`、`multica-web` 映像 |
| Docker 檢查 | 未安裝時提示安裝連結 |
| Windows | v0.5.2 起安裝腳本可在 PowerShell 5.1 執行 |

完成後開啟 <http://localhost:3000>。若只需要 CLI（伺服器已在別處運行），macOS／Linux 也可用 Homebrew：

```bash
brew install multica-ai/tap/multica
```

### 5.4 Docker Compose 逐步部署

#### 步驟 1：啟動服務

```bash
git clone --depth 1 https://github.com/multica-ai/multica.git
cd multica
make selfhost
```

`make selfhost` 首次執行時會：

1. 由 `.env.example` 建立 `.env`；
2. 產生隨機的 `JWT_SECRET`、PostgreSQL 密碼與 `MULTICA_VCS_SECRET_KEY`（自架 Git 整合的加密金鑰）；
3. 拉取 PostgreSQL、Multica 後端與前端映像；
4. 建立持久化 Volume 並啟動三個容器；
5. 等待後端開始回應健康檢查。

再次執行 `make selfhost` 會沿用既有 `.env` 與 Volume，**不會重新產生機密**。

| Make 目標 | 用途 |
| --- | --- |
| `make selfhost` | 拉取已發布映像並啟動（不編譯本地程式碼） |
| `make selfhost-build` | 以目前 checkout 的原始碼建置映像（使用 `multica-backend:dev`／`multica-web:dev` 標籤，不覆蓋 `:latest`） |
| `make selfhost-stop` | 停止 Compose 服務 |

> 💡 **實務建議：** 已發布映像追蹤最新 **Release Tag**，而 `git clone` 取得的是通常超前的 `main`。若要從 checkout 建置任何東西（CLI 或 `make selfhost-build`），先切到對應的 Release Tag，讓二進位與執行中的容器版本一致：
>
> ```bash
> git fetch --tags --depth 1
> git checkout $(git tag -l 'v*' --sort=-v:refname | head -1)
> ```

#### 步驟 2：確認服務就緒

```bash
docker compose -f docker-compose.selfhost.yml ps
curl -fsS http://localhost:8080/readyz
```

`postgres` 應為 `healthy`，`backend` 與 `frontend` 為 running；`/readyz` 預期回應：

```json
{"status":"ok","checks":{"db":"ok","migrations":"ok"}}
```

後端容器每次啟動都會先執行資料庫 Migration（`docker/entrypoint.sh` 呼叫 `./migrate up`），再開始服務，**不需要手動執行 Migration**。

| 健康端點 | 用途 |
| --- | --- |
| `GET /health` | 存活（Liveness）檢查：只要行程在就回 `{"status":"ok"}`，即使 Migration 失敗也一樣 |
| `GET /readyz` | 就緒（Readiness）檢查：同時檢查資料庫與已套用的 Migration |
| `GET /healthz` | `/readyz` 的別名 |

#### 步驟 3：登入並建立 Workspace

Docker 自架預設 `APP_ENV=production`，**沒有固定驗證碼**。三種登入方式：

| 方式 | 設定 | 適用 |
| --- | --- | --- |
| **正式（建議）** | 設定 Resend（`RESEND_API_KEY`）或 SMTP（`SMTP_HOST` 等），重建後端 | 正式環境 |
| **未設定 Email** | 驗證碼由伺服器產生並印在後端日誌 | 單機一次性測試 |
| **固定測試碼** | `APP_ENV=development` + `MULTICA_DEV_VERIFICATION_CODE=888888` | 本機自動化測試 |

從日誌讀取驗證碼：

```bash
docker compose -f docker-compose.selfhost.yml logs backend | grep "Verification code"
# [DEV] Verification code for you@example.com: 123456
```

> ⚠️ **注意：** 絕對不要在可公開存取的實例設定 `MULTICA_DEV_VERIFICATION_CODE`——任何知道 Email 的人都能用固定碼登入。`APP_ENV=production` 時此設定會被忽略。

#### 手動 Docker Compose（不使用 make）

```bash
git clone https://github.com/multica-ai/multica.git
cd multica
cp .env.example .env
# 必填：JWT_SECRET。Compose 缺少它會拒絕啟動；正式環境後端遇到預設值或已知佔位字串會拒絕開機
JWT_SECRET=$(openssl rand -hex 32)
# 將產生的值寫入 .env 後
docker compose -f docker-compose.selfhost.yml pull
docker compose -f docker-compose.selfhost.yml up -d
```

> ⚠️ **注意：** `docker compose restart` 只重啟既有容器，**不會重新讀取 `.env`**。修改設定後必須執行 `docker compose -f docker-compose.selfhost.yml up -d` 重建容器。

### 5.5 連接執行電腦

以下指令在**執行 AI 工具的電腦**上執行，不一定是跑 Docker 的伺服器。

> ⚠️ **注意：** Run 以執行 Daemon 之作業系統使用者的**完整權限**執行，可讀寫該使用者能存取的一切。請以專用 Unix 帳號、容器或 VM 執行 Daemon，不要用個人帳號（見第 20 章）。

安裝 CLI：

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
```

```powershell
# Windows PowerShell
irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex
```

連線：

```bash
# 服務與執行電腦為同一台
multica setup self-host

# 服務在另一台機器
multica setup self-host \
  --server-url https://api.example.com \
  --app-url https://app.example.com
```

`setup self-host` 依序：檢查 `<server-url>/health` → 開啟瀏覽器登入 → 儲存本機憑證 → 探索 Workspace → 在背景啟動 Daemon。其他旗標：

| 旗標 | 用途 |
| --- | --- |
| `--port`／`--frontend-port` | 未指定 URL 時使用的本機埠（預設 8080／3000） |
| `--callback-host` | 瀏覽器能直接連到此 CLI 時，OAuth 回呼 URL 指向的主機／IP；純 SSH 主機請依畫面上的 tunnel 提示操作 |
| `--profile <name>` | 全域旗標，以獨立 Profile 連線（例如 staging） |

確認連線：

```bash
multica daemon status
```

輸出應顯示 `Daemon: running`、`Agents` 列出本機 AI 工具、`Workspaces` 大於 0。

若偏好逐步手動設定：

```bash
multica config set server_url https://api.example.com
multica config set app_url https://app.example.com
multica login
multica daemon start
```

### 5.6 遠端存取與反向代理

Docker Compose 只把 `3000` 與 `8080` 綁定在 `127.0.0.1`。**不要改成 `0.0.0.0` 直接暴露到公網**，應以反向代理提供 HTTPS。

#### 佈局 A：雙網域（瀏覽器只走 app 網域）

`.env`：

```bash
FRONTEND_ORIGIN=https://app.example.com
MULTICA_APP_URL=https://app.example.com
MULTICA_PUBLIC_URL=https://api.example.com
```

Caddy：

```text
app.example.com {
    # 瀏覽器 WebSocket 直接交給後端
    @ws path /ws /ws/*
    handle @ws {
        reverse_proxy 127.0.0.1:8080 {
            flush_interval -1
        }
    }

    # 其餘交給前端，由前端轉發 API 與登入請求
    handle {
        reverse_proxy 127.0.0.1:3000
    }
}

api.example.com {
    reverse_proxy 127.0.0.1:8080 {
        flush_interval -1
    }
}
```

此佈局下瀏覽器流量都留在 app 網域，Cookie 不跨網域，**不需要** `COOKIE_DOMAIN`；api 網域供 CLI、Daemon、Webhook 使用（它們以 `mul_` PAT 走 `Authorization: Bearer`，不經 Cookie／CSRF）。

#### 佈局 B：單一來源（Single Origin，官方建議）

適合小型伺服器，一個網域或一個主機加一個埠：

```text
multica.example.com {
    # CLI 可達性探測：multica setup 會 GET <server-url>/health 並要求 200
    handle /health {
        reverse_proxy 127.0.0.1:8080
    }

    # 瀏覽器即時 WebSocket（Web 映像無法代理 WS Upgrade）
    handle /ws {
        reverse_proxy 127.0.0.1:8080 {
            flush_interval -1
        }
    }

    # Daemon 長連線 WebSocket：Daemon 連的是 /api/daemon/ws（不是 /ws）
    handle /api/daemon/ws {
        reverse_proxy 127.0.0.1:8080 {
            flush_interval -1
        }
    }

    # 其餘交給前端
    handle {
        reverse_proxy 127.0.0.1:3000
    }
}
```

`FRONTEND_ORIGIN` 與 `MULTICA_APP_URL` 都指向此來源，`multica setup self-host` 的 `--server-url` 與 `--app-url` 也都用它。

兩個 Caddy 細節是「即時更新失效」的常見原因：

| 細節 | 原因 |
| --- | --- |
| 用 `path /ws /ws/*`，不要用 `/ws*` | `handle /ws` 是精確比對；`/ws*` 的 `*` 沒有路徑段邊界，會誤吃 `/ws-foo` 這類合法 Workspace URL |
| `flush_interval -1` | 關閉回應緩衝，WebSocket frame 才能即時轉送；否則會出現留言延遲、只有重新整理才看得到 |

#### 佈局 C：Nginx 分離網域

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

# Backend API
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

若**瀏覽器直接呼叫 api 網域**，必須設定：

```bash
# Backend
FRONTEND_ORIGIN=https://app.example.com
CORS_ALLOWED_ORIGINS=https://app.example.com
COOKIE_DOMAIN=.example.com           # 涵蓋兩個主機的「最窄」上層網域

# Frontend（僅在以 docker-compose.selfhost.build.yml 自行建置 Web 映像時）
REMOTE_API_URL=https://api.example.com
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_WS_URL=wss://api.example.com/ws
```

> ⚠️ **注意（分離網域三大陷阱）：**
>
> 1. **缺 `COOKIE_DOMAIN` 會讓所有寫入失敗**：Web 以 HttpOnly 的 `multica_auth` Cookie 加上 JS 可讀的 `multica_csrf` Cookie 驗證，並在每個非 GET 請求送出 `X-CSRF-Token`。Cookie 預設僅限主機，app 網域讀不到 api 網域發的 Cookie，後端回 `403 {"error":"CSRF validation failed"}`——畫面能顯示，但無法新增或編輯。
> 2. **`COOKIE_DOMAIN` 要盡量窄**：它同時決定 Session JWT 的範圍，瀏覽器會把它送給該網域下**所有**主機。`agent.example.com` + `api.agent.example.com` 應設 `.agent.example.com`，不要設 `.example.com`。不可使用 IP。改值後要清除兩邊舊 Cookie 再重新登入。
> 3. **`NEXT_PUBLIC_API_URL`／`REMOTE_API_URL` 只能填 Origin，不能帶路徑**：寫成 `https://api.example.com/api` 會變成 `/api/api/...`。v0.4.10 起此變數在官方映像中生效，升級後若 UI 能載入但資料全部 404，先檢查它，並以 `up -d --force-recreate frontend` 重建前端。
>
> 若前後端沒有共同上層網域，或上層網域下有非自己管理的主機，請改用同源佈局。

#### LAN／非 localhost 存取

從區網其他機器存取（例如 `http://192.168.1.100:3000`）時：

```bash
# .env
FRONTEND_ORIGIN=http://192.168.1.100:3000
CORS_ALLOWED_ORIGINS=http://192.168.1.100:3000
```

```bash
docker compose -f docker-compose.selfhost.yml up -d
```

HTTP 請求可經 Next.js rewrites 正常運作，但 **WebSocket 不會**——rewrites 不轉送 `Upgrade` 握手。解法二選一：在前面放反向代理（建議），或以 `NEXT_PUBLIC_WS_URL=ws://<lan-ip>:8080/ws` 重新建置 Web 映像（此為建置期變數，只設在 `environment:` 無效）。

> 💡 **實務建議：** 不論哪種佈局，後端都會以白名單檢查 WebSocket 的 `Origin`，預設只允許 `localhost`。只要瀏覽器用的不是 localhost，就必須把實際來源設進 `CORS_ALLOWED_ORIGINS`（或 `FRONTEND_ORIGIN`）。否則後端日誌會出現 `websocket: request origin not allowed by Upgrader.CheckOrigin`，瀏覽器 Console 不斷顯示 `disconnected, reconnecting in 3s`。

#### 驗證遠端設定

```bash
docker compose -f docker-compose.selfhost.yml up -d
curl -fsS https://api.example.com/readyz
curl -fsS https://app.example.com/api/config | grep -o '"daemon_server_url":"[^"]*"'
```

`daemon_server_url` 是 Daemon 連 API 的網址，解析順序為 `MULTICA_DAEMON_SERVER_URL` → `MULTICA_PUBLIC_URL` → `MULTICA_APP_URL` → `FRONTEND_ORIGIN`。若印出 `localhost`，表示 `.env` 仍沿用本機預設值，請明確設定公開網址後重建容器。

> ⚠️ **注意：** `MULTICA_DAEMON_SERVER_URL` 會由未驗證的 `/api/config` 端點回傳給任何用戶端，請視為公開設定，不要放入任何憑證。

### 5.7 Kubernetes 部署（Helm Chart）

#### Chart 建立的資源

| 資源 | 說明 |
| --- | --- |
| `multica-postgres` | `pgvector/pgvector:pg17` + 10Gi PVC（可用 `postgres.external.enabled=true` 改接外部 PostgreSQL） |
| `multica-backend` | Go API／WS 伺服器；預設 5Gi `ReadWriteOnce` 上傳 PVC，設定 S3 後可用 `backend.uploads.persistence.enabled=false` 關閉 |
| `multica-frontend` | Next.js standalone 伺服器；執行期讀取 `REMOTE_API_URL` 與 `DOCS_URL`，不需重建 |
| 兩個 `Ingress` | Web 主機與後端主機各一（預設 `className: traefik`） |
| `multica-config` ConfigMap | 由 `values.yaml` 產生 |

`multica-secrets` Secret **不由 Chart 管理**，需自行以 `kubectl` 建立，避免機密進入 Git。前置條件：`kubectl`、`helm`（v3.13+ 以支援 `--take-ownership`，或 v4+）、Ingress Controller、預設 StorageClass。Chart 以 k3s + Traefik + `local-path` 撰寫，其他叢集稍作調整即可。

#### 步驟 1：主機名稱

Chart 預設 `multica.dev.lan`（Web）與 `api.multica.dev.lan`（後端）。以 `/etc/hosts` 或內部 DNS 指向 Ingress IP；**執行 Daemon 的電腦也需要相同解析**。改用其他主機名稱時，需同時覆寫 `ingress.frontend.host`、`ingress.backend.host`、`backend.config.appUrl`、`backend.config.frontendOrigin`、`backend.config.localUploadBaseUrl`、`backend.config.googleRedirectUri`。

#### 步驟 2：Namespace 與 Secret

```bash
kubectl create namespace multica

kubectl -n multica create secret generic multica-secrets \
  --from-literal=JWT_SECRET="$(openssl rand -hex 32)" \
  --from-literal=POSTGRES_PASSWORD="$(openssl rand -hex 16)" \
  --from-literal=RESEND_API_KEY="" \
  --from-literal=GOOGLE_CLIENT_SECRET="" \
  --from-literal=CLOUDFRONT_PRIVATE_KEY="" \
  --from-literal=MULTICA_DEV_VERIFICATION_CODE=""
```

#### 步驟 3：安裝 Chart

```bash
# 匯出預設值並修改
helm show values oci://ghcr.io/multica-ai/charts/multica \
  --version <chart-version> > my-values.yaml

helm install multica oci://ghcr.io/multica-ai/charts/multica \
  --version <chart-version> \
  -n multica \
  -f my-values.yaml

kubectl -n multica get pods -w
curl -H "Host: api.multica.dev.lan" http://<ingress-ip>/healthz
# {"status":"ok","checks":{"db":"ok","migrations":"ok"}}
```

已發布的 Chart 版本為 Git Tag 去掉 `v`（例如 `v0.6.1` → `0.6.1`），且預設映像 Tag 即為對應 Release。從原始碼開發時可用 `helm install multica deploy/helm/multica -n multica`。冷啟動時後端可能維持 `Running` 但未 `Ready` 數分鐘（等待 PostgreSQL 與 Migration），由 startupProbe 吸收，不會重啟。

#### 常用 values

| Key | 預設 | 說明 |
| --- | --- | --- |
| `images.backend.tag`／`images.frontend.tag` | `""`（＝Chart appVersion） | 升級時設定為目標 Release |
| `images.*.pullPolicy` | `IfNotPresent` | 追蹤浮動 Tag 時需改 `Always` |
| `postgres.external.enabled` | `false` | 改接 RDS、CNPG、Cloud SQL 等外部資料庫 |
| `backend.replicas`／`frontend.replicas` | `1` | 多副本時請一併設定 Redis |
| `backend.extraCACerts.configMap` | `""` | 私有 CA（見 5.8） |
| `backend.config.appEnv` | `production` | |
| `backend.config.allowSignup`／`disableWorkspaceCreation` | `true`／`false` | 註冊管控（第 7 章） |
| `backend.config.doNotTrack` | `""` | 設 `1` 關閉匿名遙測 |
| `backend.config.vcsIntegrationEnabled` | `true` | 自架 Git 整合開關 |
| `backend.config.maintenancePort` | `""` | 維護作業監聽埠（第 21.5 節） |
| `ingress.className` | `traefik` | 依叢集 Ingress Controller 調整 |

#### 步驟 4：登入與連接 Daemon

正式環境以 Secret 設定 Resend 金鑰後重啟後端：

```bash
kubectl -n multica patch secret multica-secrets --type=merge \
  -p '{"stringData":{"RESEND_API_KEY":"re_xxx"}}'
kubectl -n multica rollout restart deploy/multica-backend
```

未設定 Email 時，從 Pod 日誌讀取驗證碼：

```bash
kubectl -n multica logs -f deploy/multica-backend | grep "Verification code"
```

`ALLOW_SIGNUP`、`DISABLE_WORKSPACE_CREATION`、`GOOGLE_CLIENT_ID` 對應 `backend.config.allowSignup`、`disableWorkspaceCreation`、`googleClientId`；`helm upgrade` 後 ConfigMap 雜湊改變會自動滾動後端，Web 從 `/api/config` 執行期讀取，不需重建。

Daemon 在叢集外的執行電腦上連線：

```bash
multica setup self-host \
  --server-url http://api.multica.dev.lan \
  --app-url http://multica.dev.lan
```

#### 移除

```bash
# 移除工作負載，保留 PVC 與 Secret
helm -n multica uninstall multica

# 全部清除（含 PostgreSQL 資料與上傳檔）
kubectl delete namespace multica
```

升級與回滾見第 22.3 節。

### 5.8 私有 CA 憑證

後端呼叫的 HTTPS 服務（例如內部 CA 簽發的自架 Gitea／GitLab）若不被信任，連線會失敗。官方建議把 CA 加入信任庫，而非關閉驗證。後端為 Go 程式，在 Linux 上會載入系統憑證，加上 `SSL_CERT_DIR` 所列目錄中的 PEM 檔。

**Kubernetes：**

```bash
kubectl -n multica create configmap multica-extra-ca --from-file=internal-ca.crt
helm upgrade multica oci://ghcr.io/multica-ai/charts/multica \
  --version <chart-version> -n multica --reuse-values \
  --set backend.extraCACerts.configMap=multica-extra-ca
```

**Docker Compose**（`docker-compose.ca.yml` 覆寫檔）：

```yaml
services:
  backend:
    environment:
      SSL_CERT_DIR: /etc/ssl/certs:/etc/multica/ca-certs
    volumes:
      - ./ca-certs:/etc/multica/ca-certs:ro
```

```bash
docker compose -f docker-compose.selfhost.yml -f docker-compose.ca.yml up -d backend
```

| 注意事項 | 說明 |
| --- | --- |
| 只在啟動時讀取 | 新增或更換 CA 後要重啟後端；Compose 下 `up -d` 不夠（設定未變不會重建），請用 `restart backend` |
| 每次都要帶兩個檔 | 只帶 `docker-compose.selfhost.yml` 的指令（例如 `make selfhost`）會在沒有 CA 的狀態下重建後端 |
| 作用於整個後端行程 | 所有使用系統信任庫的對外 TLS 用戶端都會信任它 |
| 只解決信任問題 | 過期或主機名稱不符的憑證仍會被拒絕 |

> 💡 SMTP 使用私有 CA 時同樣以此方式處理；`SMTP_TLS_INSECURE=true` 只應在受信任內網暫時使用。

### 5.9 不使用 Docker 的手動部署

前置條件（v0.6.1）：Go 1.26.6、Node.js 22、pnpm 10.28.2、PostgreSQL 17（一般安裝即可）。

```bash
# 確認 Migration 角色可建立兩個必要擴充
psql "$DATABASE_URL" -c 'CREATE EXTENSION IF NOT EXISTS "pgcrypto";'
psql "$DATABASE_URL" -c 'CREATE EXTENSION IF NOT EXISTS pg_trgm;'

# 編譯後端
make build

# 執行 Migration（冪等）
DATABASE_URL="your-database-url" ./server/bin/migrate up

# 啟動後端
DATABASE_URL="your-database-url" PORT=8080 JWT_SECRET="your-secret" ./server/bin/server
```

```bash
# 前端
pnpm install
pnpm build
cd apps/web
REMOTE_API_URL=http://localhost:8080 pnpm start
```

> ⚠️ **注意：** 手動執行時 `LOCAL_UPLOAD_DIR` 預設 `./data/uploads` 是相對於**啟動目錄**，請改設絕對路徑；否則每次換目錄啟動，上傳檔就會寫到不同位置，既有附件也會找不到。

### 5.10 停止服務與切換至 Cloud

| 情境 | 指令 |
| --- | --- |
| 以安裝腳本安裝（macOS／Linux） | `curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh \| bash -s -- --stop` |
| 以安裝腳本安裝（Windows） | `$env:MULTICA_MODE="stop"; irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 \| iex` |
| 以 repo 手動部署 | `make selfhost-stop` |
| 停止服務但保留資料 | `docker compose -f docker-compose.selfhost.yml down` |
| 停止本機 Daemon | `multica daemon stop` |

> ⚠️ **注意：** `docker compose down` 會保留 `pgdata` 與 `backend_uploads` Volume；加上 `-v` 會刪除資料庫與附件，除非要清空實例，否則不要執行 `down -v`。

把 CLI 從自架切換到 Multica Cloud：

```bash
multica setup
```

此指令會重新設定 CLI 指向 multica.ai、重新登入並重啟 Daemon；覆寫既有設定前會先詢問。本機 Docker 服務不受影響，需另行停止。若想同時保留兩邊，改用 `--profile` 建立獨立 Profile（見第 19.4 節）。

### 5.11 讓 AI Agent 協助部署

官方提供 [`SELF_HOSTING_AI.md`](https://github.com/multica-ai/multica/blob/main/SELF_HOSTING_AI.md)，專門寫給 AI Agent 依序執行的部署步驟（安裝、等待 `✓ Multica server is running and CLI is ready!`、`multica setup self-host`、`multica daemon status` 驗證、自訂埠）。可以直接交給本機的 Claude Code 或 Codex 執行 PoC 部署。

自訂埠的正確做法：編輯 `.env` 的 `PORT` 與 `FRONTEND_PORT`（這是主機埠，容器內固定 8080／3000，不需重建），執行 `make selfhost`，再以 `multica setup self-host --port <PORT> --frontend-port <FRONTEND_PORT>` 連線。

> 💡 **實務建議：** 設定來源的優先序依進入點而不同：`make` 會 `include` `.env`，所以檔案中的值**優先於** Shell 環境變數（`PORT=9100 make selfhost` 會被忽略），但命令列賦值 `make selfhost PORT=9100` 有效；直接呼叫 Docker Compose 時則是環境變數優先於 `.env`。**修改 `.env` 是唯一在所有進入點行為一致的方法**。埠別名順序為 `BACKEND_PORT` → `API_PORT` → `SERVER_PORT` → `PORT` → `8080`。

---

## 第 6 章：環境變數與組態參考

> **本章重點：** 正式環境最小組態；API／資料庫、公開網址、Email 與登入、附件儲存、Redis 與速率限制、外部整合、伺服器端 LLM、前端、可觀測性等分組參考；Daemon 端變數、Workspace GC 與 `config.json` 鍵值；設定優先序。

Multica 在**行程啟動時**讀取環境變數；變更後必須重啟受影響的 API、Web 或 Daemon。Docker Compose 的 `docker compose restart` 不會重讀 `.env`，請以 `up -d` 重建容器。

### 6.1 正式環境最小組態

```dotenv
DATABASE_URL=postgres://user:password@postgres:5432/multica?sslmode=require
JWT_SECRET=<long-random-secret>
APP_ENV=production
FRONTEND_ORIGIN=https://multica.example.com
MULTICA_APP_URL=https://multica.example.com
MULTICA_PUBLIC_URL=https://api.multica.example.com
```

另外**必須選擇一種 Email 服務**（Resend 或 SMTP），否則驗證碼與邀請只會寫入伺服器日誌。

> ⚠️ **注意：** `APP_ENV=production` 時，`JWT_SECRET` 為空或為已知佔位字串，後端會拒絕開機（以 `openssl rand -hex 32` 產生）。正式環境不可設定 `MULTICA_DEV_VERIFICATION_CODE`。自架部署**必須**設定 `FRONTEND_ORIGIN`，否則邀請連結、Cookie 安全屬性與 WebSocket 來源檢查都可能與實際網域不符。

### 6.2 API 與資料庫

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `DATABASE_URL` | 本機 `multica` 資料庫 | PostgreSQL 連線字串 |
| `DATABASE_MAX_CONNS` | `25` | 每個 API 行程的最大連線數 |
| `DATABASE_MIN_CONNS` | `5` | 每個 API 行程維持的最小連線數（自動夾在 MAX 以下） |
| `DATABASE_SEARCH_WORK_MEM_MB` | `64` | 搜尋計畫節點的 `work_mem` 上限（MB）；`1`–`64` 降低，`0` 沿用資料庫預設 |
| `DATABASE_REPLICA_URL` | 空 | 選用唯讀副本；新連線會驗證為唯讀，但只有程式明確選用的讀取路徑才會使用 |
| `DATABASE_REPLICA_MAX_CONNS` | `10` | 每個 API 行程的副本最大連線數（與主庫預算獨立） |
| `DATABASE_REPLICA_MIN_CONNS` | `0` | 副本最小連線數 |
| `MULTICA_DATABASE_STARTUP_TIMEOUT` | `3m` | 容器層級的 Migration 與 API 啟動重試預算；`0` 表示每階段只試一次 |
| `MULTICA_DATABASE_CONNECT_TIMEOUT` | `5s` | 每次啟動連線的逾時（pgx `connect_timeout`、`PGCONNECT_TIMEOUT` 優先） |
| `PORT` | `8080` | API 監聽埠（Compose 中為主機埠） |
| `JWT_SECRET` | 正式環境必填 | 登入 JWT 與部分簽章流程的密鑰 |
| `APP_ENV` | 空 | 正式環境設為 `production` |
| `AUTH_TOKEN_TTL` | `720h`（30 天） | 瀏覽器 JWT／Cookie 存活期；滑動續期，低於 `60s` 會被拉回 `60s` |
| `LOG_LEVEL` | `info` | `debug`、`info`、`warn`、`error` |
| `MULTICA_SHUTDOWN_HOLD_DURATION` | `0` | 收到終止訊號後延遲多久才開始優雅關閉；K8s 的 `terminationGracePeriodSeconds` 必須大於此值加上實際關閉時間 |
| `MULTICA_RUNTIME_RECONNECT_GRACE` | `3h` | 離線 Runtime 可重連的寬限期，超過則其進行中的 Run 失敗；低於 `150s` 會被拉回 |
| `MAINTENANCE_PORT` | 空（停用） | 維護作業監聽埠，固定綁 `127.0.0.1`（第 21.5 節） |

### 6.3 公開網址與瀏覽器存取

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `FRONTEND_ORIGIN` | 空 | 使用者造訪的前端來源；用於 CORS、Cookie 與邀請連結 |
| `MULTICA_APP_URL` | 退回 `FRONTEND_ORIGIN` | 使用者可達的 Web 網址；CLI 登入與帳號綁定連結使用 |
| `MULTICA_PUBLIC_URL` | 空 | 公開 API 網址；用於 Webhook URL 與 Runtime 連線指示 |
| `MULTICA_DAEMON_SERVER_URL` | 依序退回 `MULTICA_PUBLIC_URL`、`MULTICA_APP_URL`／`FRONTEND_ORIGIN` | 插入 `multica setup self-host` 的伺服器網址；Daemon 走的網址與公開 Webhook 網址不同時才需設定（**公開值，不可放機密**） |
| `CORS_ALLOWED_ORIGINS` | 空（＝`FRONTEND_ORIGIN`） | 額外允許的 HTTP 來源，逗號分隔；同時影響 WebSocket 來源檢查 |
| `ALLOWED_ORIGINS` | 退回 CORS／前端來源 | WebSocket 來源白名單 |
| `COOKIE_DOMAIN` | 空 | 前後端不同主機且瀏覽器直接呼叫 API 網域時必填；單一網域保持空白（見 5.6） |

### 6.4 Email、登入與註冊

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `RESEND_API_KEY` | 空 | 設定即啟用 Resend |
| `RESEND_FROM_EMAIL` | `noreply@multica.ai` | 寄件者，須屬於已驗證網域 |
| `SMTP_HOST` | 空 | 設定即啟用 SMTP（**優先於 Resend**） |
| `SMTP_PORT` | `25` | 常見 25、587、465 |
| `SMTP_USERNAME`／`SMTP_PASSWORD` | 空 | 匿名中繼可留空 |
| `SMTP_FROM_EMAIL` | 退回 `RESEND_FROM_EMAIL` | Envelope From 與信件 From |
| `SMTP_TLS` | `starttls` | `implicit`／`smtps`／`ssl` 為隱式 TLS；465 埠自動啟用 |
| `SMTP_TLS_INSECURE` | `false` | 跳過憑證驗證，僅限受信任內網 |
| `SMTP_EHLO_NAME` | 主機名稱 | 嚴格中繼（如 Google Workspace）要求的 FQDN |
| `GOOGLE_CLIENT_ID`／`GOOGLE_CLIENT_SECRET` | 空 | Google OAuth |
| `GOOGLE_REDIRECT_URI` | `http://localhost:3000/auth/callback` | 必須與 Google Console 完全一致 |
| `ALLOW_SIGNUP` | `true` | 未設定白名單時是否允許註冊 |
| `ALLOWED_EMAILS` | 空 | 允許註冊的完整 Email，逗號分隔 |
| `ALLOWED_EMAIL_DOMAINS` | 空 | 允許註冊的網域，逗號分隔 |
| `DISABLE_WORKSPACE_CREATION` | `false` | 封鎖所有人建立 Workspace，owner／admin 亦無例外 |
| `MULTICA_DEV_VERIFICATION_CODE` | 空 | 非正式環境的固定 6 位數測試碼 |

`ALLOW_SIGNUP`、`DISABLE_WORKSPACE_CREATION`、`GOOGLE_CLIENT_ID` 由 Web 從 `/api/config` 執行期讀取，重啟後端即可，不需重建 Web。

### 6.5 附件儲存

未設定 `S3_BUCKET` 時使用本機磁碟。

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `LOCAL_UPLOAD_DIR` | `./data/uploads` | 檔案目錄，需持久化 Volume；手動執行請用絕對路徑 |
| `LOCAL_UPLOAD_BASE_URL` | 空 | 選用公開基底網址；空白時回傳相對路徑 |
| `S3_BUCKET` | 空 | 只填 Bucket 名稱，不含主機名稱 |
| `S3_REGION` | `us-west-2` | 必須與 Bucket 實際區域一致 |
| `AWS_ACCESS_KEY_ID`／`AWS_SECRET_ACCESS_KEY` | SDK 預設憑證鏈 | 靜態憑證 |
| `AWS_ENDPOINT_URL` | 空 | S3 相容端點（MinIO、R2、B2） |
| `S3_USE_PATH_STYLE` | 有自訂端點時 `true` | 需要 virtual-hosted 風格的供應商設 `false` |
| `ATTACHMENT_DOWNLOAD_MODE` | `auto` | `auto`、`cloudfront`、`presign`、`proxy`；瀏覽器無法直連的內網端點用 `proxy` |
| `ATTACHMENT_DOWNLOAD_URL_TTL` | `30m` | 簽章下載網址的有效期 |
| `CLOUDFRONT_DOMAIN`／`CLOUDFRONT_KEY_PAIR_ID`／`CLOUDFRONT_PRIVATE_KEY` | 空 | CloudFront 簽章網址 |
| `CLOUDFRONT_PRIVATE_KEY_SECRET` | 空 | 從 Secrets Manager 讀取私鑰時使用 |

私有 Bucket 且無公開 CDN 時，頭像改由 `/api/avatars/<signature>/<key>` 提供，並依 `ATTACHMENT_DOWNLOAD_MODE` 解析；系統只允許「頭像類」圖片走此路由，避免把 Issue 附件變成公開連結，無須額外設定。

### 6.6 Redis 與速率限制

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `REDIS_URL` | 空 | 所有 Redis 功能共用的連線網址：共享速率限制、即時事件、通訊 Bot WebSocket 租約、Token 快取 |
| `REDIS_CLUSTER_MODE` | `false` | 強制使用 Redis Cluster Client；需 database 0 且 `REALTIME_RELAY_MODE=sharded` |
| `REDIS_DISABLE_CLIENT_NAME` | `false` | 託管 Redis 封鎖 `CLIENT SETNAME` 時設 `true` |
| `RATE_LIMIT_AUTH` | `5` | 每 IP 每分鐘發送驗證碼或啟動 Google 登入次數 |
| `RATE_LIMIT_AUTH_VERIFY` | `20` | 每 IP 每分鐘驗證碼校驗次數 |
| `RATE_LIMIT_INVITATION_ACTOR_10M` | `10` | 每位邀請者每 10 分鐘可建立的邀請數；`0` 停用 |
| `RATE_LIMIT_INVITATION_WORKSPACE_24H` | `50` | 每個 Workspace 每 24 小時的邀請總數；`0` 停用 |
| `RATE_LIMIT_INVITATION_RECIPIENT_24H` | `6` | 同一收件 Email 跨 Workspace 每 24 小時可收到的邀請數；`0` 停用 |
| `RATE_LIMIT_TRUSTED_PROXIES` | 空 | 允許提供 `X-Forwarded-For` 的代理 CIDR |
| `MULTICA_TRUSTED_PROXIES` | 空 | 自動化 Webhook 與即時連線信任的代理 CIDR |

> ⚠️ **注意：** 驗證碼速率限制**需要 `REDIS_URL`**，未設定時啟動日誌會提示 auth rate limiting 已停用。邀請限制在無 Redis 時以行程記憶體運作，有 Redis 後跨副本共享。Redis 暫時不可用時，登入速率限制會「失敗開放」（fail open），邀請建立則回傳可重試的 `503`。反向代理後方的部署必須列出真實代理網段，不可全面信任所有來源。

### 6.7 外部整合

| 整合 | 變數 | 說明 |
| --- | --- | --- |
| GitHub | `GITHUB_APP_SLUG` | GitHub App slug |
| GitHub | `GITHUB_WEBHOOK_SECRET` | Webhook HMAC 與連線狀態簽章密鑰 |
| GitHub | `GITHUB_APP_ID`、`GITHUB_APP_PRIVATE_KEY` | PR 卡片的 CI 狀態、可合併性與「從 GitHub 挑選 Repo」所需 |
| 飛書／Lark | `MULTICA_LARK_SECRET_KEY` | Base64 編碼的 32 bytes 憑證加密金鑰 |
| Slack | `MULTICA_SLACK_SECRET_KEY` | 同上，加密 Slack Token |
| 釘釘 | `MULTICA_DINGTALK_SECRET_KEY` | 同上，加密 AppSecret |
| 企業微信 | `MULTICA_WECOM_SECRET_KEY` | 同上，加密 Bot Secret |
| 企業微信 | `MULTICA_WECOM_TRACE` | `1` 記錄所有 WeCom frame（含訊息前 120 字），僅限除錯期間 |
| Telegram | `MULTICA_TELEGRAM_SECRET_KEY` | 同上，加密 Bot Token |
| Composio | `COMPOSIO_API_KEY`、`COMPOSIO_CALLBACK_BASE_URL`、`COMPOSIO_STATE_SECRET` | 啟用 Composio 工具連線；Callback 可退回 `MULTICA_PUBLIC_URL`，State 密鑰可由 `JWT_SECRET` 衍生 |
| 自架 Git | `MULTICA_VCS_INTEGRATION_ENABLED` | Forgejo／Gitea／GitLab 整合開關（Compose 預設開啟） |
| 自架 Git | `MULTICA_VCS_SECRET_KEY` | Base64 32 bytes 加密金鑰，缺少時整合完全不可用 |
| Plugins | `MULTICA_PLUGIN_SECRET_KEY`、`MULTICA_PLUGIN_SURFACE_ORIGIN`、`MULTICA_PLUGIN_API_URL`、`MULTICA_PLUGIN_DIR` | Plugin 機密加密、專用無 Cookie 來源、Plugin Public API 基底網址、本機開發 Bundle 目錄 |
| 私有 CA | `SSL_CERT_DIR` | 例：`/etc/ssl/certs:/etc/multica/ca-certs`（見 5.8） |

所有 `*_SECRET_KEY` 都以 `openssl rand -base64 32` 產生，且**必須長期保存**：輪替或遺失後，既有憑證無法解密，對應的 Bot 或整合必須重新連線。

### 6.8 伺服器端 LLM（輔助功能）

此組變數只用於伺服器端的輔助生成（對話自動命名、Agent 回覆下方的建議追問按鈕），**與 Agent 執行 Run 所用的 AI 工具憑證無關**。

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `MULTICA_LLM_API_KEY` | 空 | OpenAI 相容 API Key |
| `MULTICA_LLM_BASE_URL` | 空 | OpenAI 相容端點 |
| `MULTICA_LLM_DEFAULT_MODEL` | `gpt-5.6-luna` | 請求未指定模型時使用 |
| `MULTICA_LLM_MAX_RETRIES` | `2` | 每次呼叫的重試上限，`0`–`5`；其他值會使啟動失敗 |
| `MULTICA_LLM_DISABLE_THINKING` | `false` | 對支援的閘道送出 `chat_template_kwargs: {"enable_thinking": false}` |

> 📘 **建議實務：** 兩個輔助功能會把聊天內容送往設定的端點（新對話的第一則訊息原文；追問功能最多送 6 則訊息，最新回覆截 3000 字、較舊訊息各截 800 字）。若資安政策不允許聊天內容離開部署環境，**將 `MULTICA_LLM_API_KEY` 與 `MULTICA_LLM_BASE_URL` 都留空**即可完全停用此層——對話仍保有由第一則訊息衍生的標題，只是不顯示追問按鈕。若要啟用，建議指向企業內部的 LLM Gateway。

### 6.9 前端（Web）

| 變數 | 類型 | 說明 |
| --- | --- | --- |
| `REMOTE_API_URL` | 執行期 | Next.js rewrites 代理 `/v1`、`/api`、`/auth`、`/uploads` 的目標，只填 Origin |
| `DOCS_URL` | 執行期 | 文件站上游 |
| `NEXT_PUBLIC_API_URL` | 建置期 | 瀏覽器直接呼叫的 API Origin；同源部署留空 |
| `NEXT_PUBLIC_WS_URL` | 建置期 | 瀏覽器 WebSocket 網址；同源部署留空 |
| `FRONTEND_PORT` | — | 前端主機埠（容器內固定 3000） |

`NEXT_PUBLIC_*` 為建置期變數，只對以 `docker-compose.selfhost.build.yml` 自行建置的映像有效。

### 6.10 可觀測性與分析

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `METRICS_ADDR` | 空（不啟動） | Prometheus 指標監聽位址，例：`127.0.0.1:9090` |
| `REALTIME_METRICS_TOKEN` | 空 | 保護 `/health/realtime` 的 Bearer Token |
| `DO_NOT_TRACK` | 空（遙測開啟） | `1`／`true` 停止第一方匿名自架遙測 |
| `ANALYTICS_DISABLED` | `false` | `true` 關閉 PostHog |
| `POSTHOG_API_KEY` | 空 | 未設定即不送；可改送到自己的 PostHog 專案 |
| `POSTHOG_HOST` | `https://us.i.posthog.com` | PostHog 主機 |

`DO_NOT_TRACK` 與 `ANALYTICS_DISABLED` 互相獨立（詳見第 20.6 節）。

### 6.11 Daemon 端環境變數

以下變數在**執行 Agent 的電腦**上讀取，不在 API 容器中。

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `MULTICA_SERVER_URL` | `ws://localhost:8080/ws` | Multica API／WebSocket 網址，也接受 `http(s)` |
| `MULTICA_APP_URL` | `http://localhost:3000` | CLI 登入流程使用的前端網址 |
| `MULTICA_WORKSPACE_ID` | 空 | 全域預設 Workspace |
| `MULTICA_DAEMON_DEVICE_NAME` | 主機名稱 | Runtime 列表顯示的裝置名稱 |
| `MULTICA_AGENT_RUNTIME_NAME` | `Local Agent` | Runtime 顯示名稱 |
| `MULTICA_DAEMON_POLL_INTERVAL` | `30s` | 沒有喚醒事件時的補查輪詢間隔 |
| `MULTICA_DAEMON_WS_CLAIM_POLL_INTERVAL` | `3m` | 健康 WebSocket 下的安全輪詢上限（實際約 `2m30s`–`2m45s`） |
| `MULTICA_DAEMON_HEARTBEAT_INTERVAL` | `15s` | 心跳間隔 |
| `MULTICA_DAEMON_MAX_CONCURRENT_TASKS` | `20` | 每個 Daemon 的併發 Run 上限 |
| `MULTICA_AGENT_TIMEOUT` | `0`（無上限） | 每次 Run 的絕對時限 |
| `MULTICA_AGENT_IDLE_WATCHDOG` | `2h` | 無輸出且無工具執行的靜默上限；`0` 完全停用 |
| `MULTICA_AGENT_TOOL_WATCHDOG` | 同 IDLE | 單一工具呼叫的靜默上限 |
| `MULTICA_OPENCODE_IDLE_WATCHDOG` | `10m` | OpenCode 專用靜默門檻 |
| `MULTICA_CODEX_SEMANTIC_INACTIVITY_TIMEOUT` | 同 IDLE | Codex 語意靜默門檻 |
| `MULTICA_CODEX_FIRST_TURN_TIMEOUT` | `0` | Codex 首輪無進度上限的明確覆寫 |
| `MULTICA_CODEX_HANDSHAKE_TIMEOUT` | `30s`（thread start/resume `60s`） | Codex app-server 啟動握手上限 |
| `MULTICA_CODEX_TURN_INTERRUPT_TIMEOUT` | `2s` | 取消後等待 Codex 確認中斷的寬限期 |
| `MULTICA_DAEMON_AUTO_UPDATE` | Cloud `true`／自架 `false` | 是否自動檢查並套用 CLI 更新 |
| `MULTICA_DAEMON_AUTO_UPDATE_INTERVAL` | `6h` | 更新檢查間隔 |
| `MULTICA_DAEMON_AUTO_RELOAD` | `true` | 磁碟上的 `multica` 二進位被替換時是否自動重啟（與自動更新獨立） |
| `MULTICA_WORKSPACES_ROOT` | `~/multica_workspaces` | Run 工作目錄的根目錄 |
| `MULTICA_AGENT_TEMP_BASE` | `/tmp`（Linux／macOS） | 每次 Run 私有暫存目錄的上層，請用短路徑（AF_UNIX socket 路徑上限 104–108 bytes） |
| `MULTICA_KEEP_ENV_AFTER_TASK` | `false` | 保留 Run 目錄以便除錯 |
| `GODEBUG=tlsmlkem=0` | — | 網路設備丟棄後量子 TLS 握手時的暫時解法（見第 21.7 節） |

> ⚠️ **注意：** 不要在啟動 Daemon 的 Shell、Compose 服務或容器 entrypoint 設定 `MULTICA_DAEMON_PORT`。Daemon 會依 Profile 自行推導健康埠並注入給 Agent Task；v0.4.22–v0.4.23 遇到此變數會誤判為受管 Task 而拒絕登入。

#### Workspace 垃圾回收（GC）

Daemon 會定期掃描 `MULTICA_WORKSPACES_ROOT` 回收磁碟：

| 變數 | 預設 | 說明 |
| --- | --- | --- |
| `MULTICA_GC_ENABLED` | `true` | 總開關 |
| `MULTICA_GC_INTERVAL` | `2h` | 掃描間隔 |
| `MULTICA_GC_TTL` | `24h` | Issue 為 `done`／`cancelled` 且閒置超過此時間，刪除整個 Task 目錄 |
| `MULTICA_GC_COMPLETED_TASK_TTL` | Cloud `14d`／自架 `0`（停用） | 即使 Issue 仍開啟，完成超過此時間的 Task 目錄也整個移除（未推送的工作會一併消失） |
| `MULTICA_GC_ORPHAN_TTL` | `72h` | 沒有 `.gc_meta.json` 的孤兒目錄 |
| `MULTICA_GC_ARTIFACT_TTL` | `12h` | 完成後只刪除可重建的產物；`0` 停用 |
| `MULTICA_GC_ARTIFACT_PATTERNS` | `node_modules,.next,.turbo` | 產物目錄名稱（僅 basename），可擴充如 `target,__pycache__` |
| `MULTICA_GC_REPO_TTL` | `720h` | `.repos/` 共享 bare clone 的閒置驅逐時間；`0` 停用 |
| `MULTICA_GC_REPO_MAINTENANCE_ENABLED` | `true` | 是否在閒置時執行 `reflog expire`／`git gc` |
| `MULTICA_GC_HERMES_MEMORY_TTL` | `2160h` | Hermes 長期記憶回收 |
| `MULTICA_GC_HERMES_SESSION_TTL` | `336h` | Hermes 對話紀錄回收 |
| `MULTICA_GC_TASK_TEMP_LEGACY_TTL` | `0` | 舊版（無鎖檔）暫存目錄的回收，預設不回收 |

以 `multica daemon disk-usage --by-workspace` 或 `--all-profiles` 檢視實際用量。

#### 各 AI 工具專屬變數

每種 AI 工具都接受 `MULTICA_<PROVIDER>_PATH`（執行檔路徑）與 `MULTICA_<PROVIDER>_MODEL`（預設模型）覆寫，例如 `MULTICA_CLAUDE_PATH`、`MULTICA_CODEX_MODEL`。例外與額外變數：

| 工具 | 變數 | 說明 |
| --- | --- | --- |
| Claude Code、Codex、CodeBuddy、Qwen Code、QwenPaw | `MULTICA_CLAUDE_ARGS`、`MULTICA_CODEX_ARGS`、`MULTICA_CODEBUDDY_ARGS`、`MULTICA_QWEN_ARGS`、`MULTICA_QWENPAW_ARGS` | 全機預設附加參數（目前僅此五種支援） |
| MiniMax Code | `MULTICA_MCODE_PATH` | 無模型變數，模型由工具自身管理 |
| QwenPaw | — | 無模型變數 |
| DeepSeek Harness | `MULTICA_DSH_PATH`、`MULTICA_DSH_MODEL`、`MULTICA_DSH_PROFILE_BUNDLE`、`MULTICA_DSH_PLUGIN_PATH` | 模型 ID 為 `provider/model` 形式；Profile Bundle 會安裝到所有 Daemon 主機，屬供應鏈決策 |
| Dim | `MULTICA_DIM_PATH`、`MULTICA_DIM_MODEL` | |
| ZeroClaw | `MULTICA_ZEROCLAW_PATH` | 無模型變數，由 Agent Profile 決定 |
| OpenClaw | `MULTICA_OPENCLAW_CLI_TIMEOUT` | 每次 `openclaw config` 呼叫的期限（預設 30s） |

完整對照表見[附錄 C](#附錄-c支援的-agent-cli-對照)。

### 6.12 Daemon 設定檔與優先序

常用 Daemon 設定可寫入 `~/.multica/config.json`（具名 Profile 為 `~/.multica/profiles/<name>/config.json`）：

```bash
multica config set poll_interval 10s
multica config set workspaces_root /data/multica_workspaces
multica config set poll_interval ""     # 清除，退回環境變數或預設值
multica config show
```

| 鍵 | 預設 | 說明 |
| --- | --- | --- |
| `server_url` | `ws://localhost:8080/ws` | API／WebSocket 網址 |
| `app_url` | 空 | 瀏覽器登入用 Web 網址 |
| `workspace_id` | 空 | 預設 Workspace |
| `device_name`／`runtime_name` | 主機名稱／`Local Agent` | 顯示名稱 |
| `workspaces_root` | Profile 相關路徑 | 相對路徑儲存時轉為絕對路徑 |
| `max_concurrent_tasks` | `20` | 非負整數 |
| `poll_interval`／`ws_claim_poll_interval`／`heartbeat_interval` | `30s`／`3m`／`15s` | |
| `agent_timeout` | 無上限 | `0s` 明確表示不限 |
| `codex_semantic_inactivity_timeout`／`codex_handshake_timeout` | 衍生／`30s` | |
| `disable_auto_update`／`auto_update_check_interval` | 依環境／`6h` | |
| `disable_auto_reload` | 依環境 | |

**優先序：命令列旗標 → 環境變數 → `config.json` → 內建預設值。** Duration 鍵只接受正值（`agent_timeout` 例外可為 `0s`）。

> ⚠️ **注意：** CLI 設定檔內含可代表你存取 Multica 的 Token，不可提交到 Repo、上傳到日誌或分享他人。

---

## 第 7 章：認證、Token 與註冊管控

> **本章重點：** Email 驗證碼（Resend／SMTP）與 Google 登入設定；註冊白名單的判斷順序與邀請例外；Session 滑動續期；四種 Token 前綴（`mul_`、`mat_`、`mcn_`、`mdt_`）的用途與管理；企業鎖定 Workspace 建立的標準程序。

### 7.1 登入方式總覽

| 方式 | 說明 | 必要設定 |
| --- | --- | --- |
| Email 驗證碼 | 預設方式；6 位數，10 分鐘有效 | Resend 或 SMTP（否則只寫入日誌） |
| Google OAuth | 疊加在 Email 之上 | `GOOGLE_CLIENT_ID`、`GOOGLE_CLIENT_SECRET`、`GOOGLE_REDIRECT_URI` |
| 個人存取 Token（PAT） | CLI、Daemon、腳本、API | 使用者於 **Settings → API Token** 建立 |

既有使用者永遠可以重新登入；註冊限制只決定**能否建立新帳號**。啟動日誌會說明目前的 Email 模式：`Resend API`、`SMTP relay` 或 `DEV mode`。

### 7.2 Email 驗證碼

#### 使用 Resend

```dotenv
RESEND_API_KEY=re_xxxxxxxxxxxxxxxx
RESEND_FROM_EMAIL=noreply@example.com
```

`RESEND_FROM_EMAIL` 必須屬於在 Resend 已驗證的網域。設定後重啟 API。

#### 使用 SMTP（企業內網建議）

```dotenv
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=multica
SMTP_PASSWORD=<password>
SMTP_FROM_EMAIL=noreply@example.com
```

| 情境 | 設定 |
| --- | --- |
| 內部匿名中繼 | `SMTP_PORT=25`，帳密留空 |
| STARTTLS | `SMTP_PORT=587`，伺服器支援時預設升級 TLS |
| 隱式 TLS | `SMTP_PORT=465`，或明確設定 `SMTP_TLS=implicit` |
| 嚴格中繼要求 EHLO | `SMTP_EHLO_NAME=mail.example.com` |
| 私有 CA | 把 CA 加入容器信任庫（第 5.8 節）；`SMTP_TLS_INSECURE=true` 僅可暫時用於受信任內網 |

兩者同時設定時 **SMTP 優先**。

#### 無 Email 服務時

伺服器仍會啟動，但驗證碼與邀請連結只寫入日誌，不寄信——只適合本機開發。

#### 固定測試驗證碼

```dotenv
APP_ENV=development
MULTICA_DEV_VERIFICATION_CODE=888888
```

驗證碼必須為 6 位數；`APP_ENV=production` 時會被忽略。

> ⚠️ **注意：** 正式環境的正確組合是 `APP_ENV=production` 且 `MULTICA_DEV_VERIFICATION_CODE` 為空。

### 7.3 Google 登入

1. 在 Google Cloud Console 建立 OAuth 2.0 Client；
2. 於 **Authorized redirect URIs** 加入前端回呼網址 `https://multica.example.com/auth/callback`；
3. 設定：

   ```dotenv
   GOOGLE_CLIENT_ID=xxxxx.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=GOCSPX-xxxxxxxxxxxxxxx
   GOOGLE_REDIRECT_URI=https://multica.example.com/auth/callback
   ```

4. 重啟 API。

Google Console 與 `GOOGLE_REDIRECT_URI` 的網址必須**完全一致**（含通訊協定、埠與結尾斜線）。設定完成後登入頁會出現 Google 按鈕，前端映像不需重建。

### 7.4 註冊限制

三個變數共同決定新帳號能否建立，判斷順序如下：

```mermaid
flowchart TD
    S["新 Email 請求註冊"] --> A{"符合 ALLOWED_EMAILS？"}
    A -->|"是"| OK["允許"]
    A -->|"否"| B{"網域符合 ALLOWED_EMAIL_DOMAINS？"}
    B -->|"是"| OK
    B -->|"否"| C{"未設任何白名單且 ALLOW_SIGNUP=true？"}
    C -->|"是"| OK
    C -->|"否"| D{"有未過期的待接受邀請？"}
    D -->|"是"| OK
    D -->|"否"| NG["拒絕"]
```

常見設定：

```dotenv
# 公司網域與受邀者
ALLOW_SIGNUP=false
ALLOWED_EMAIL_DOMAINS=company.com

# 再額外允許一位外部協作者
ALLOWED_EMAILS=partner@example.net
```

**邀請例外：** 未過期的待接受邀請，允許該 Email 建立帳號，即使 `ALLOW_SIGNUP=false` 或不在白名單中。白名單因此**不是**擋住受邀者的硬邊界。邀請在請求驗證碼與建立帳號時各檢查一次（含 Google 登入）；遺失、過期、已接受、已拒絕或已撤銷的邀請都不授予註冊權。撤銷邀請**不會**刪除已用它建立的帳號，也不會阻止其登入。

### 7.5 企業鎖定 Workspace 建立

`ALLOW_SIGNUP=false` 只限制新帳號，**不會**阻止已登入使用者透過 `POST /api/workspaces` 另建 Workspace。若平台管理者需要看得到所有 Issue／Repo／Agent，官方建議的啟動程序：

1. 以 `DISABLE_WORKSPACE_CREATION=false`（預設）啟動實例；
2. 以管理者登入並建立共用 Workspace；
3. 設定 `DISABLE_WORKSPACE_CREATION=true`（可同時設 `ALLOW_SIGNUP=false`）並重啟後端；
4. 之後使用者只能經由邀請加入；UI 隱藏「Create workspace」，直接呼叫 API 回 `403`。

> 📘 **建議實務：** 企業正式環境的建議組合為 `ALLOW_SIGNUP=false` + `ALLOWED_EMAIL_DOMAINS=<公司網域>` + `DISABLE_WORKSPACE_CREATION=true` + SMTP 內部中繼 + `REDIS_URL`（啟用驗證碼速率限制）。

### 7.6 Session 存活期

瀏覽器登入後，JWT 存放在名為 `multica_auth` 的 HttpOnly Cookie，JavaScript 無法讀取；另有 JS 可讀的 `multica_csrf` Cookie 作為 CSRF 防護。

| 特性 | 說明 |
| --- | --- |
| 預設存活期 | `AUTH_TOKEN_TTL=720h`（30 天） |
| 滑動續期 | Session 剩餘不到一半時，下一次請求會重新簽發完整存活期；持續使用的帳號不會被排程登出（v0.5.0+） |
| 單邊界限 | 只有過半後才續期，因此「保證可存活的閒置時間」是設定值的一半 |
| 下限 | `60s`，低於會被拉回並在啟動時警告 |
| 套用時機 | 對之後簽發或續期的 Session 生效 |
| 登出 | 清除目前瀏覽器的 auth 與 CSRF Cookie |

### 7.7 Token 類型

| 前綴 | 名稱 | 用途 | 由誰管理 |
| --- | --- | --- | --- |
| `mul_` | 個人存取 Token（PAT） | CLI、Daemon、腳本、API；代表你的帳號，可存取你能存取的所有 Workspace | 使用者 |
| `mat_` | Agent Run 臨時 Token | Daemon 領取 Run 時由 Server 建立，綁定使用者、Workspace、Agent 與 Run；最長 24 小時，Run 結束即清除 | Server 自動 |
| `mcn_` | Cloud Node 連線 | Multica Cloud Fleet | 原廠 |
| `mdt_` | Workspace 範圍 Daemon 驗證協定 | 內部 Server 流程 | Server 內部 |

#### 個人存取 Token（PAT）

在 **Settings → API Token** 建立，需提供名稱並選擇效期：30 天、90 天（預選）、1 年或永不過期。完整 Token **只顯示一次**，之後 Multica 只保留雜湊、前幾個字元、名稱、建立／到期／最後使用時間；遺失只能撤銷後重建。

`multica login` 透過瀏覽器完成登入後，會建立一個 90 天的 PAT 並存入目前 Profile 的設定檔。效期剩不到 7 天時會**自動續期**為 90 天；續期失敗則維持原狀，過期或撤銷後需重新 `multica login`。

無瀏覽器的機器：

```bash
multica login --token
```

此指令會在終端機提示貼上 Token，避免完整值留在 Shell 歷史。

在 API 中使用：

```bash
export MULTICA_TOKEN='mul_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

curl https://api.example.com/api/me \
  -H "Authorization: Bearer $MULTICA_TOKEN"

curl https://api.example.com/api/issues \
  -H "Authorization: Bearer $MULTICA_TOKEN" \
  -H "X-Workspace-ID: $MULTICA_WORKSPACE_ID"
```

> ⚠️ **注意：** `multica auth logout` 只刪除目前 CLI Profile 存的 PAT；Web 登出只刪除瀏覽器 Cookie——**兩者都不會撤銷 Server 上的 Token**。疑似外洩時，請立即在 **Settings → API Token** 撤銷，所有存有該 Token 的機器與腳本會同時失效。

#### Agent Run 臨時 Token（`mat_`）

Daemon 把 `mat_` 臨時 Token 注入 AI 工具（環境變數 `MULTICA_TOKEN`），而不是把使用者的 PAT 交給 Agent。因此：

- Agent 發出的請求在時間軸上記錄為 **Agent 的動作**；
- 無法用它執行只限使用者或 owner 的敏感操作；
- Agent 在 Task 內執行的 `multica` CLI 不會讀取或修改使用者的 Profile 設定檔。

> ⚠️ **注意：** `MULTICA_TOKEN` 位於 Runtime 行程的真實環境中，AI 工具啟動的子行程預設全部繼承。若某子行程不應持有此憑證，必須明確移除；不要把它寫進 Prompt、日誌、Repo 檔案或持久化設定。

### 7.8 Token 治理建議

📘 **建議實務：**

| 項目 | 建議 |
| --- | --- |
| PAT 效期 | 個人使用選 90 天；CI／自動化用途選 30–90 天並排程輪替，避免「永不過期」 |
| 存放 | 腳本從 Secret Manager 或受保護環境變數讀取，不寫死在程式碼 |
| 命名 | 名稱標示用途與主機（例如 `ci-github-actions-prod`），方便稽核與撤銷 |
| 離職流程 | 移除成員前先撤銷其 PAT；移除成員會停用其 Runtime、封存綁定的 Agent 並取消未完成 Run |
| 外洩應變 | 撤銷 Token → 檢查 Run 與時間軸中的異常動作 → 輪替該帳號可存取的下游憑證 |

---

## 第 8 章：Workspace 與成員角色

> **本章重點：** Workspace 的邊界與內容；建立時的三個欄位（名稱、URL、Issue 前綴）；Workspace Context；owner／admin／member 權限矩陣；邀請、角色變更與移除成員的連帶影響；CLI 管理；企業團隊隔離策略。

### 8.1 Workspace 的定位

Workspace 是 Multica 的**最上層邊界**。成員、Issue、Project、Agent、Skill 與 Run 紀錄都屬於某一個 Workspace，彼此完全隔離。

| 類別 | 內容 |
| --- | --- |
| 工作 | Issue、Project、留言、附件、Run 紀錄 |
| 團隊 | 成員、角色、邀請 |
| Agent | Agent 設定、Skills、Runtimes、自動化 |
| 共用設定 | Context、標籤、自訂屬性、自訂狀態、整合、MCP 函式庫 |

**Context** 會提供給 Workspace 內**每一個** Agent，適合放團隊背景、產品慣例與長期要求；一次性的需求應寫在對應 Issue 中。

### 8.2 建立 Workspace

| 欄位 | 規則 | 可否變更 |
| --- | --- | --- |
| **名稱** | 顯示給成員 | 可 |
| **Workspace URL（slug）** | `multica.ai/my-team` 中的 `my-team`；僅小寫字母、數字、連字號；不可與既有或保留位址衝突 | **建立後不可變更** |
| **Issue 前綴** | 由 slug 預填、建立前可改；大寫字母與數字，最多 10 字元。前綴 `MUL` 時編號為 `MUL-1`、`MUL-2`，在 Workspace 內獨立遞增 | 可（設定頁） |

建立者自動成為 `owner`。也可用 CLI 建立（v0.4.2+）：

```bash
multica workspace create --name "Support Team" --slug support-team --issue-prefix SUP
multica workspace switch support-team
```

`workspace create` **不會**切換目前 Profile 的預設 Workspace，需另外 `switch`。

> ⚠️ **注意：** 變更 Issue 前綴後，所有 Issue 立即改用新編號（`MUL-5` 變 `NEW-5`），但 PR、分支名稱與聊天紀錄中的舊編號**不會**更新，且 GitHub／VCS 的自動連結只比對目前前綴。

### 8.3 切換、離開與刪除

- 一個帳號可加入多個 Workspace；切換只改變目前檢視的內容，不搬移資料。
- 離開 Workspace 後需要新邀請才能回來；離開會**停用你擁有的 Runtime、封存綁定在其上的 Agent，並取消其未完成的 Run**。
- 最後一位 `owner` 不能離開，需先把其他成員升為 `owner`。
- 只有 `owner` 可以刪除 Workspace；刪除會永久移除所有工作、成員、Agent 設定與 Run 紀錄，無法復原。

### 8.4 角色與權限矩陣

每位成員只有一個角色：`owner`、`admin` 或 `member`。角色只控制 **Workspace 設定與團隊管理**；日常協作（建立 Issue、留言）對所有成員開放。

| 動作 | owner | admin | member |
| --- | :---: | :---: | :---: |
| 檢視 Workspace、日常協作 | ✓ | ✓ | ✓ |
| 變更 Workspace 設定（名稱、圖示、Context、前綴） | ✓ | ✓ | — |
| 邀請 `admin` 或 `member` | ✓ | ✓ | — |
| 變更或移除 `admin`／`member` | ✓ | ✓ | — |
| 授予、撤銷或移除 `owner` | ✓ | — | — |
| 刪除 Workspace | ✓ | — | — |
| 刪除 Project | ✓ | ✓ | — |
| 解鎖並修改 Agent 環境變數 | ✓ | ✓ | — |
| 建立／編輯自訂 Runtime Profile | ✓ | ✓ | — |
| 連接 GitHub／自架 Git／通訊 Bot | ✓ | ✓ | —（飛書 Bot 另允許 Agent 擁有者） |

> 💡 **關鍵觀念：** 角色**不**決定誰能執行 Agent。每個 Agent 有自己的 Access 範圍，`owner` 與 `admin` 也不能繞過 Access 去執行沒有授權給他們的 Agent（見第 10.5 節）。同理，私有 Runtime 只有擁有者能在其上建立 Agent，admin 也不例外。

### 8.5 邀請成員

`owner` 與 `admin` 在 **Settings → Members** 輸入 Email 並選擇角色送出邀請。

| 規則 | 說明 |
| --- | --- |
| 可授予的角色 | 只能邀請為 `admin` 或 `member`；`owner` 必須先加入再由既有 `owner` 升級 |
| 接受方式 | 受邀者以該 Email 登入即可，不需事先註冊 |
| 效期 | 7 天，過期後重寄 |
| 邀請連結 | 只出現在 Email 中，產品內無法檢視或複製；寄送失敗時撤銷後重寄 |
| 分享連結（v0.4.27+） | 另可建立讓他人直接加入 Workspace 的分享連結 |
| 註冊受限的自架實例 | 有效的待接受邀請允許該 Email 建立帳號，無須另加白名單（見 7.4） |
| 速率限制 | 每位邀請者每 10 分鐘 10 封、每 Workspace 每 24 小時 50 封、同一收件者 24 小時 6 封（可調整，見 6.6） |

CLI：

```bash
multica workspace member invite teammate@example.com
multica workspace member invite admin@example.com --role admin
multica workspace member list --output json
```

### 8.6 變更角色與移除成員

- `admin` 可在 `admin` 與 `member` 之間調整角色，並移除這兩種角色的成員；任何涉及 `owner` 的變更只能由 `owner` 執行。
- 角色變更立即生效。
- 被移除的成員立即失去 Workspace 存取權；其建立的 Issue、留言等協作紀錄保留在 Workspace 中。

> ⚠️ **注意：** 移除成員也會**停用其擁有的 Runtime、封存綁定的 Agent、取消未完成的 Run**，並清除該成員在 Agent Access 中獲得的授權；即使日後重新加入，這些授權也不會自動恢復。移除擁有共用 Runtime 的成員前，應先把其 Agent 遷移到其他 Runtime（`multica agent copy <agent-id> --runtime-id <新-runtime> --model <model>`）。

### 8.7 CLI 管理

```bash
multica workspace list                 # 列出所有 Workspace
multica workspace get                  # 目前 Workspace 詳情
multica workspace switch <slug>        # 設定目前 Profile 的預設 Workspace
multica workspace update --help        # 更新名稱、Context 等
multica workspace member list
multica workspace member invite <email> --role member
```

單一指令可用 `--workspace-id` 覆寫，或設定環境變數 `MULTICA_WORKSPACE_ID`。

> 📝 **與舊版差異：** 舊版手冊的 `multica workspace watch/unwatch` 與 `multica workspace members` 在 v0.6.1 已不存在；成員管理改為 `workspace member list/invite`。Daemon 會自動為你有權連接的所有 Workspace 註冊 Runtime，不需手動 watch。

### 8.8 企業團隊隔離策略

📘 **建議實務：**

| 策略 | 做法 | 適用 |
| --- | --- | --- |
| 依產品線分 Workspace | 每條產品線一個 Workspace，各自的 Agent、Skills、Repo | 中大型組織、團隊間資料需隔離 |
| 單一 Workspace + Projects | 一個 Workspace，以 Project 與 Project Resources 區分 | 小型組織、需要跨團隊共享 Agent |
| 環境分 Workspace | `xxx-dev` 與 `xxx-prod` 分開，Prod Workspace 的 Agent 只給少數人 Access | 有變更管理要求的維運情境 |
| 獨立 Profile | 同一台執行電腦以 `--profile` 連接不同實例（例如 staging 與正式） | 平台團隊測試新版本 |

設計時留意兩個限制：Workspace 間完全隔離，**Skills 無法跨 Workspace 共用**（需各自匯入，見第 11 章）；同一 GitHub App 安裝可接多個 Workspace，但若前綴相同造成同一編號同時命中，系統不會自動連結。

---

## 第 9 章：Issues 與 Projects

> **本章重點：** Issue 的組成與 Assignee 類型；7 個內建狀態與 4 種生命週期類別；自訂狀態、自訂屬性、標籤與儲存檢視；子 Issue 與 Stage；重複標記；Issue Metadata、時間軸與用量；Project 與進度計算；Project Resources（GitHub Repo、本機目錄的 Direct／Parallel 模式）。

### 9.1 Issue 的組成

Issue 是 Multica 組織工作的基本單位：一個功能、一個 Bug、一項調查——任何應由成員或 Agent 擁有並推進的事。

| 組成 | 用途 |
| --- | --- |
| 標題與描述 | 目標、背景、需求與驗收條件 |
| 狀態與優先序 | 工作位置與處理順序 |
| Assignee | 成員、Agent 或 Squad |
| 日期、標籤、自訂屬性 | 規劃、分類與團隊自有欄位 |
| Project 與父子關係 | 歸入更大的工作，或拆成子 Issue |
| 活動與執行紀錄 | 留言、狀態變更、Run 與 Agent 回傳的結果 |
| 交付物與附件（v0.6.0+） | 側欄集中顯示交付物版本；HTML、Markdown、CSV、JSON、YAML 可就地預覽 |
| Pull Requests | 連結的 PR、CI 狀態與可合併性（第 17 章） |

每個 Issue 有編號（如 `MUL-123`），數字在 Workspace 內遞增。任何成員都可以刪除 Issue；刪除無法復原，且會取消未完成的 Run。工作只是不再進行時，請改設 `cancelled` 保留紀錄。

### 9.2 Assignee 與執行

| Assignee | 效果 |
| --- | --- |
| 成員 | 由該成員負責後續，**不建立 Run** |
| Agent | 為該 Agent 建立 Run |
| Squad | Squad Leader 接收並決定由誰處理 |

指派給 Agent 或 Squad 時，除非 Issue 在 `backlog`，否則立即排入佇列；Runtime 離線時 Run 在佇列等待。已封存的 Agent 與 Squad 無法被指派；指派也不能繞過 Agent 的 Access（指派給 Squad 時檢查 Leader 的 Access）。詳見第 13.2 節。

### 9.3 狀態與生命週期

每個 Workspace 內建 7 個狀態，分屬 4 種生命週期類別：

| 類別 | 內建狀態 | 意義 |
| --- | --- | --- |
| `unstarted` | `backlog`、`todo` | 尚未開始（已規劃或延後） |
| `started` | `in_progress`、`in_review`、`blocked` | 進行中、待審查或暫時無法繼續 |
| `done` | `done` | 成功完成（終態） |
| `closed` | `cancelled` | 不再進行（終態，非成功完成） |

| 狀態 | 意義 |
| --- | --- |
| `backlog` | 暫不開始；指派給 Agent 的 Issue **離開 backlog 後才建立 Run** |
| `todo` | 範圍已定，等待開始 |
| `in_progress` | 進行中 |
| `in_review` | 有結果等待審查 |
| `done` | 完成 |
| `blocked` | 暫時無法繼續 |
| `cancelled` | 不再進行，保留紀錄 |

狀態之間**沒有固定流程**，成員與 Agent 都可直接變更。Agent 依其工作的實際變化**透過 CLI 明確寫入**狀態：開始處理 Issue 本身的要求 → 立即移到 `in_progress`；交付 → `in_review`；工作延續到下一輪 → 維持 `in_progress`；只是回答問題或諮詢 → 不動狀態。`done` 通常由人類確認，或由 PR 合併觸發。

```mermaid
stateDiagram-v2
    [*] --> backlog
    backlog --> todo: 排入計畫（觸發已指派的 Agent）
    todo --> in_progress: Agent 開始處理
    in_progress --> in_review: Agent 交付
    in_progress --> blocked: 遇到阻礙
    blocked --> in_progress: 阻礙排除
    in_review --> in_progress: 審查要求修改
    in_review --> done: 人類確認或 PR 全部合併
    in_progress --> todo: Run 失敗且無其他 Run／重試（系統）
    todo --> cancelled
    in_progress --> cancelled
    done --> [*]
    cancelled --> [*]
```

Server 只在兩種情況**自動**變更狀態：

1. Run 失敗、該 Issue 沒有其他 Run、也沒有觸發重試時，`in_progress` 退回 `todo`；
2. Issue 連結的**所有 PR 都已合併**時，移到 Workspace 設定的狀態（預設 `done`），除非 Workspace 選擇不變更或該 Issue 已關閉此行為（第 17.3 節）。

### 9.4 自訂狀態

Workspace `owner`／`admin` 可在 **Settings → Issue Statuses** 新增狀態（例如 `Code Review`、`QA`、`Rework`），v0.4.34 起開放所有 Workspace。

| 規則 | 說明 |
| --- | --- |
| 必屬一種類別 | `unstarted`、`started`、`done`、`closed` 之一，**建立後不可變更** |
| 只繼承生命週期語意 | **不**繼承內建 Backlog 的停車行為、In Review 的 Autopilot 完成、Blocked 的失敗、In Progress 的復原行為；需要這些行為時請用內建狀態 |
| 看板分欄 | 依個別狀態分欄，`Code Review` 與 `QA` 雖同屬 started 仍各自一欄 |
| 內建狀態鎖定 | 名稱、顏色、類別不可改，也不可封存 |
| 封存而非刪除 | 已在該狀態的 Issue 保留原狀；只是不再出現在選項中 |
| 排序與圖示 | 可拖曳排序（含內建狀態）、可設定圖示形狀（v0.4.44+） |
| API／CLI 鍵值 | 以 key 指定，例如 `multica issue status MUL-42 code_review`；改名不改 key |

> ⚠️ **注意：** 只有內建 `backlog` 會「停車」。屬於 `unstarted` 類別的**自訂狀態不會**阻止 Run——把 Agent 指派給處於該狀態的 Issue 會立即開始執行。

### 9.5 自訂屬性、標籤與檢視

**自訂屬性（Custom Properties，v0.4.2+）：** 9 種型別，建立後型別不可改。

| 型別 | 範例 |
| --- | --- |
| `text`、`number`、`date`、`url`、`checkbox` | 需求編號、估點、上線日、規格連結、是否需資安審查 |
| `select`、`multi_select` | 嚴重度、影響模組 |
| `actor`、`multi_actor` | Reviewer、相關成員（可填成員名稱、Email 或 ID） |

```bash
multica property create --name Severity --type select \
  --option "Critical:#ef4444" --option "Major:#f59e0b" --option "Minor:#6b7280"
multica property create --name Reviewer --type actor

multica issue property set MUL-42 --name Severity --value Critical
multica issue list --property "Severity=Critical" --property "Reviewer=__none__"
multica issue list --sort property:Severity
```

屬性篩選支援包含比對、數字／日期範圍與「未填值」（`__none__`），可用於篩選選單、Facet 與儲存檢視。

**標籤：** 以 `multica label create --name <名稱> --color <#hex> --resource-type issue|skill` 建立，可指定用於 Issue 或 Skill。

**儲存檢視（v0.4.22+）：** 把常用篩選存成 View，在 Issue 列表頂端切換；View 在 Workspace 內共享，排序與版面則屬個人設定。

**五種檢視：** List、Board、Table（可自訂欄位，v0.4.5+）、Gantt、Swimlane，可依狀態、Assignee、Project、屬性等篩選與排序，顯示的是同一批 Issue。

### 9.6 子 Issue、Stage 與重複標記

大型工作可拆成子 Issue：父 Issue 保留整體目標，子 Issue 獨立推進，父子狀態互不影響。

- **Stage（分批）：** 子 Issue 可指定 Stage（1、2、3…）。最早未完成 Stage 中的子 Issue 全部 `done`／`cancelled` 時，父 Issue 收到「子 Issue 已完成」通知；若父 Issue 的 Assignee 是 Agent，它會被喚醒並決定是否開始下一個 Stage。未指定 Stage 的子 Issue 視為一批。
- **評論轉子 Issue（v0.4.34+）：** 任何評論可一鍵轉為子 Issue，並帶入原討論。
- **重複標記（v0.5.2+）：** 從狀態選單標記為重複，或用 CLI（v0.6.1+）：

```bash
multica issue create --title "階段二：API 實作" --parent MUL-100 --stage 2
multica issue children MUL-100           # 依 Stage 分組列出子 Issue
multica issue status MUL-120 cancelled --duplicate-of MUL-100
```

### 9.7 Metadata、時間軸與用量

**Issue Metadata** 是 Issue 層級的鍵值對，適合給 Agent 或自動化寫入結構化狀態（例如 `waiting_for=approval`）。值預設以 JSON 解析（`true` → bool、`3` → number），可用 `--type` 強制型別。

```bash
multica issue metadata set MUL-42 --key team --value backend
multica issue metadata set MUL-42 --key ticket --value '"42"'     # 強制為字串
multica issue metadata list MUL-42
multica issue list --metadata team=backend
```

**時間軸（Timeline）**回答目前欄位無法回答的問題：何時進入 `in_review`？在目前狀態停留多久？昨天之後改了什麼？

```bash
multica issue timeline MUL-123 --action status_changed
multica issue usage MUL-123          # 彙總 Token 用量；>= 表示部分 Run 未回報用量
multica issue runs MUL-123
```

> 💡 「現在是什麼狀態」請用 `issue get`（權威快照）；`issue timeline` 用來解釋它是怎麼變成這樣的——狀態變更只寫活動紀錄、不寫留言，因此只看留言會漏掉 PR 合併造成的 `done`。

### 9.8 Projects

Project 組織需要多個 Issue 才能完成的工作——產品上線、遷移、分階段交付的功能。

| 組成 | 用途 |
| --- | --- |
| 名稱、圖示、描述 | 目標、範圍與長期要求；**描述會進入 Project 內 Agent 的執行上下文** |
| 狀態 | `planned`、`in_progress`、`paused`、`completed`、`cancelled` |
| 優先序 | `urgent`、`high`、`medium`、`low`、`none` |
| Lead | 成員或 Agent，僅標示協調者，不是權限設定、也不會自動指派或執行 |
| 起訖日期 | 計畫時程（v0.4.0+） |
| Issues 與進度 | 進度 =（`done` + `cancelled`）÷ 全部 Issue |
| Resources | GitHub Repo 或特定電腦上的本機目錄 |

一個 Issue 最多屬於一個 Project。Project 狀態與 Issue 狀態互相獨立：Issue 全部完成不會自動把 Project 設為 `completed`。任何成員可建立與編輯 Project，只有 `owner`／`admin` 可刪除；刪除 Project **不會刪除其 Issue**（會脫離並留在 Workspace）。

```bash
multica project create --title "核心系統現代化" --lead "Backend Agent" \
  --start-date 2026-10-06 --due-date 2026-12-31 \
  --repo https://github.com/example/core-api
multica project status <project-id> in_progress
multica issue create --title "實作 GET /api/v1/users/{id}" --project <project-id>
multica issue list --project <project-id>
```

### 9.9 Project Resources

Project Resources 告訴 Agent 這批工作使用哪些程式碼、在哪裡執行，不必在每個 Issue 重貼 Repo 網址或本機路徑。

| 資源 | 適用 | Run 在哪裡執行 |
| --- | --- | --- |
| **GitHub Repo**（`github_repo`） | 團隊共用、由 Runtime 管理 checkout 的程式碼；任何 Runtime 可達的 Git URL 皆可 | Runtime 管理的工作目錄（預設 worktree 模式，同一 Repo 可無限併發） |
| **本機目錄**（`local_directory`） | 既有 checkout、超大型 Repo、想直接檢視本機變更 | 特定電腦上的原始目錄 |

**資源如何進入 Run：** Agent 處理 Project 內的 Issue 時，Project 名稱、描述與資源清單會加入上下文，並寫入工作目錄的 `.multica/project/resources.json`。Workspace 的 Repo 清單（**Settings → Code**）一律包含在上下文中；Project 綁定的 Repo 則進一步指定這批工作使用的程式碼與預設 `ref`（分支、Tag 或 Commit，v0.5.1+）。

#### 本機目錄的兩種執行模式

> ⚠️ **注意：** 本機目錄是「逃生門」，不是更方便的預設值。典型情境是數十 GB、無法每次 Run 重新 clone 的遊戲專案。若目錄是可 clone 的一般 Git Repo，**請改用 `github_repo`**。新增本機目錄的 UI 只在 Desktop 提供（瀏覽器無法選取資料夾）。

| 模式 | Desktop 標示 | 行為 | 適用 |
| --- | --- | --- | --- |
| `in_place`（預設） | Direct | Agent 直接在你的目錄工作，**一次一個 Run**；後到的 Run 進入 `waiting_local_directory`；Agent 看得到並修改你目前的分支與未提交檔案，Multica 不會自動切分支、stash、commit 或 push | 非 Git 目錄、需要直接改動工作副本 |
| `worktree`（v0.4.25+） | Parallel | 每個 Run 在 Runtime 工作區內取得獨立的 Git worktree，**同一目錄可併發**，不寫入你的工作副本；成果為你 Repo 中的分支 `agent/<agent>/<issue>` | Git Repo（至少一個 commit） |

Parallel 模式的重要行為：

- Agent 從「你看到的狀態」開始，而非 `HEAD`：未提交變更與未追蹤檔案會重播進 worktree（上限 2000 檔／200 MiB，超過則 Run 失敗）；
- 成果分支以 Issue 為單位，後續評論會在同一分支繼續；Multica **永遠不會替你合併**；
- 你與 Agent 改到同一行時，Run 會在衝突的 worktree 上開始，並被要求先完成合併；
- Agent 未提交的內容會在移除 worktree 前提交到分支，不會無聲遺失；
- 隱藏 ref 存放在 `refs/multica/local-state/`，可用 `git for-each-ref refs/multica` 檢視。

路徑限制：必須是已存在、Daemon 可讀寫的絕對路徑；拒絕系統根目錄與磁碟根（`/`、`C:\`）、家目錄本身及其上層（`/Users`、`/home`、`/root`）、系統目錄（`/etc`、`/var`、`/tmp`、`/usr`、`/opt`）；符號連結會先解析再檢查。每個 Project 每台 Daemon 最多綁一個本機目錄。

> ⚠️ **自架維運注意：** worktree 模式的隔離由 Server 在儲存資源與每次領取 Run 時檢查。若在仍有 `worktree` 資源時把 **Server 回滾**到此功能之前的版本，而 Runtime 也不支援此模式，Run 會被就地執行。

#### CLI 管理資源

```bash
multica project resource list <project-id>
multica project resource add <project-id> \
  --type github_repo --url https://github.com/example/core-api --ref main

multica project resource add <project-id> \
  --type local_directory --local-path /absolute/path/to/repo \
  --daemon-id <daemon-id> --execution-mode worktree

multica project resource update <project-id> <resource-id> --execution-mode in_place
multica project resource remove <project-id> <resource-id>
```

資源變更只影響之後建立的 Run，不改寫已結束 Run 的紀錄。Runtime 也可能在目錄中寫入 AI 工具所需的指令檔與 `.multica/project/resources.json`，不希望納入版控時請加入 `.gitignore`。

---

## 第 10 章：Agents 建立與設定

> **本章重點：** Agent 的設定項目；Start blank 與 Build with AI；Instructions 撰寫；模型、Thinking Level 與 Service Tier；Access 三種範圍；併發、環境變數、自訂參數；MCP 的正確模型（Workspace MCP 函式庫 → 指派給 Agent）；複製、封存與 CLI 管理；企業 Agent 規範。

### 10.1 Agent 的本質

Agent 是 Workspace 中的協作者：可以被指派 Issue、在評論中被 @提及，或直接與它 Chat。它透過綁定的 Runtime 驅動 AI 編碼工具，並把進度與結果寫回 Workspace。

Agent **不是持續執行的行程**，而是一組可重用的身分與設定；只有在工作抵達時才產生具體的 Run。

| 概念 | 職責 |
| --- | --- |
| **Agent** | 決定「誰」做、「如何」做 |
| **Runtime** | 決定在哪台電腦、用哪個 AI 工具執行 |
| **Run** | 記錄一次執行的過程與結果 |

一個 Runtime 可承載多個 Agent；一個 Agent 會隨時間完成許多 Run。Runtime 離線時，Agent 的身分與歷史仍在，新 Run 等待 Runtime 恢復。

### 10.2 設定項目

| 設定 | 用途 |
| --- | --- |
| 名稱、頭像、描述 | 讓團隊知道它是誰、擅長什麼；**描述只供顯示，不進入執行 Prompt** |
| Instructions | 職責、工作方式、邊界與交付要求；**每次 Run 都會提供** |
| Conversation Starters | 最多 3 個範例，在新 Chat 中顯示；選取只填入輸入框，不會自動送出 |
| Skills | 可重用的方法、參考資料與支援檔案（第 11 章） |
| Runtime、模型、Thinking Level | 執行的 Runtime、AI 工具與模型；部分工具（如 Codex）另有 Service Tier |
| Access | 哪些成員可以執行它 |
| 執行設定 | 併發上限、環境變數、CLI 自訂參數、MCP、外部整合 |

切換模型或編輯 Instructions **不會**產生新 Agent，過去的 Issue、留言與 Run 紀錄都保留。

### 10.3 建立 Agent

在 Workspace 的 **Agents** 頁點 **New agent**：

| 起點 | 適用 |
| --- | --- |
| **Start blank** | 已清楚職責，想自行填寫每個欄位 |
| **Build with AI**（v0.4.0+） | 先描述目標，由 Agent Builder 提出關鍵問題並產生草稿；需要在線 Runtime；設計對話會保留供日後查閱 |

建立時**只有兩個必填**：名稱（Workspace 內唯一）與 Runtime。其他欄位都可先用預設值，日後調整。新 Agent 預設只有建立者能執行。

CLI：

```bash
multica agent create \
  --name "Frontend Reviewer" \
  --runtime-id <runtime-id> \
  --description "Reviews frontend pull requests" \
  --instructions "$(cat ./agents/frontend-reviewer.md)" \
  --model <model-id> \
  --thinking-level high \
  --max-concurrent-tasks 4 \
  --conversation-starters '[{"label":"Review a PR","prompt":"Review the most relevant open pull request."}]'
```

> 💡 `agent create`／`agent update` 的 `--instructions` 只接受字串（沒有 `-file` 版本），長指令建議存成檔案後以 Shell 讀入，如上例；`<model-id>` 請從 Web 的模型選單或 Runtime 模型清單取得。實際旗標以 `multica agent create --help` 為準。

### 10.4 撰寫 Instructions

Instructions 每次 Run 都會提供給 Agent，通常涵蓋：

- 負責與不負責的範圍；
- 工作抵達時先檢查什麼；
- 允許修改什麼；
- 如何交付結果；
- 何時應先與成員確認再繼續。

官方範例（翻譯）：

```text
你負責審查前端 Pull Request。

先閱讀 diff 與相關測試，只檢查：
- React 與 TypeScript 正確性
- 無障礙（Accessibility）
- 與既有元件模式的一致性

不要直接修改程式碼。以 Issue 留言回報發現，依嚴重度排序；
若沒有阻擋項目，明確說明此變更可以合併。
```

📘 **建議實務：企業 Instructions 範本**

```text
# 角色
你是 <系統名稱> 的後端實作 Agent，負責 Spring Boot 3 服務的功能開發與單元測試。

# 開工前
1. 讀 Issue 描述、驗收條件與所有討論；需求不清楚時，留言提問並把狀態設為 blocked。
2. 讀 Project 描述與 .multica/project/resources.json，確認目標 Repo 與分支。

# 可以做
- 在 feature 分支修改 src/main 與 src/test；執行 ./mvnw -q verify。

# 不可以做
- 不修改 CI 設定、資料庫 Migration（交由 DB Agent）、任何 secrets 檔案。
- 不直接推送 main；不自行合併 PR。

# 交付
- 開 PR，標題包含 Issue 編號（例：MUL-123 新增查詢 API）。
- 在 Issue 留言：變更摘要、測試結果、風險與待確認事項，然後把狀態設為 in_review。
```

> 💡 **實務建議：** Instructions 放「這個 Agent 長期不變的職責與邊界」；跨 Agent 重用的方法放 Skill；只屬於某件工作的需求放 Issue；整個 Workspace 都適用的背景放 Workspace Context。

### 10.5 Access（誰可以執行）

| Access | 誰可以執行（指派、@提及、Chat） |
| --- | --- |
| **Only me** | 只有 Agent 擁有者（**預設**） |
| **Entire workspace** | Workspace 所有成員 |
| **Specific people** | 擁有者與指定成員 |

| 權限 | 規則 |
| --- | --- |
| 看見 Agent | 由擁有權、Workspace 管理角色與 Access 共同決定；一般成員只看得到自己擁有或可執行的 Agent |
| 修改設定 | Agent 擁有者與 Workspace `owner`／`admin` |
| 修改 Access | **只有 Agent 擁有者**，admin 也不行 |
| 執行 | 只依 Access；`owner`／`admin` 不能憑管理角色執行未授權的 Agent |

CLI 對應旗標：`--permission-mode private|public_to`，搭配 `--public-to-workspace` 或 `--public-to-member <user-id>`（可重複）。Agent 列表可依 Access 範圍篩選與批次編輯（v0.4.2+）。

### 10.6 模型、Thinking Level 與 Service Tier

每個 Runtime 對應一種 AI 工具。選定 Runtime 後可選擇該工具支援的模型與 Thinking Level：

- 留空：使用 Runtime 或本機 CLI 的預設；
- 指定模型：之後領取的 Run 使用此覆寫；
- 部分 Runtime 自行管理模型（QwenPaw、MiniMax Code），不顯示模型選單（顯示 "Managed by runtime"）；
- 模型清單來自 Runtime 本身；Claude Code 只列出本機實際可執行的模型（v0.4.38+），可手動 Refresh；
- 切換 AI 工具後，原模型值在新工具中無效，需重新選擇。

| 旗標 | 說明 |
| --- | --- |
| `--model` | 模型識別字串，應優先使用此旗標，而非在自訂參數中傳 `--model` |
| `--thinking-level` | 例如 Claude 的 `low`、`medium`、`high`、`xhigh`、`max`；Codex 值來自 Runtime 模型目錄；不支援的 Runtime 會拒絕任何值 |
| `--service-tier` | Codex 執行速度：空白＝沿用本機設定；`default`＝明確 Standard；目錄中的 tier（如 `priority`）＝明確 Fast |

### 10.7 執行設定

| 設定 | 說明 |
| --- | --- |
| **併發上限** | Agent 同時可執行的 Run 數，預設 **6**（CLI 範圍 1–50）；超過的 Run 繼續排隊。實際併發取 Agent 上限與 Daemon 全域上限（預設 20）的較小值 |
| **環境變數**（`custom_env`） | AI 工具啟動時注入；可批次貼上編輯（v0.4.24+） |
| **自訂參數**（`custom_args`） | 以陣列逐項附加到 AI 工具的 CLI 參數，**不經 Shell 展開** |
| **MCP** | 提供 MCP 伺服器設定給支援的 AI 工具（見 10.8） |
| **Integrations** | 連接此 Agent 可使用的外部服務（例如 Composio）與通訊 Bot（第 16 章） |

設定變更**不影響執行中的 Run**，之後的 Run 使用 Runtime 領取當下所儲存的設定。

> ⚠️ **環境變數安全：** `custom_env` 以**明文**儲存於 Multica Server 資料庫，不是「只留在本機」的資料。Agent 列表與詳情 API 不再回傳任何值（只回傳數量）；只有 Workspace `owner`／`admin` 可解鎖並修改，每次讀取或變更都留稽核紀錄；執行中的 Agent 無法呼叫管理端點讀取其他 Agent 的變數。`PATH`、`HOME`、`MULTICA_*` 等關鍵變數無法在此覆寫。**不要放生產資料庫管理密碼等高價值長期憑證**，只放唯讀 API Key 或單一範圍 Token。

自訂參數同樣有洩漏風險：

> ⚠️ **自訂參數安全：** 不要把憑證放進自訂參數——它們會留在子行程的 argv 中，其他本機行程可透過 `ps` 或 `/proc` 看到。Daemon 日誌會遮蔽參數值，但無法保護作業系統的行程列表。

以 CLI 設定機密時，使用 stdin 或權限受限的檔案，避免進入 Shell 歷史與 `ps`：

```bash
# 從檔案讀入（建議權限 0600）
multica agent env set <agent-id> --custom-env-file ./secrets/reviewer-env.json

# 從 stdin 讀入
cat ./secrets/reviewer-env.json | multica agent env set <agent-id> --custom-env-stdin

# 值為 '****' 的鍵會保留既有值；'{}' 清空全部
multica agent env get <agent-id>
```

### 10.8 MCP 設定

> ⚠️ **更正：** 舊版手冊第 12 章描述「Multica 作為 MCP Provider，讓 IDE 透過 MCP 查詢 Issue、觸發任務」，在 v0.6.1 官方文件與原始碼中找不到依據。Multica 的 MCP 支援方向是**相反的**：由 Multica 管理 MCP 伺服器設定，在 Run 開始前**提供給 Agent 所用的 AI 工具**。若要讓外部 AI 工具操作 Multica，官方途徑是 CLI 與 [Multica CLI Skill](https://github.com/multica-ai/multica-cli)（第 19.6 節）。

#### 兩層模型（v0.4.27+）

```mermaid
flowchart LR
    LIB["Workspace MCP 函式庫<br/>（owner/admin 管理，唯寫）"] -->|"agent mcp add"| A1["Agent A"]
    LIB -->|"agent mcp add"| A2["Agent B"]
    A1 -->|"Run 開始前注入"| T1["Claude Code"]
    A2 -->|"Run 開始前注入"| T2["Codex"]
```

1. **Workspace MCP 函式庫：** owner／admin 定義一次 MCP 伺服器，加入函式庫時**不會指派給任何 Agent**；儲存後的設定為唯寫，`list` 只顯示名稱與傳輸方式，永不回傳內容。
2. **指派給 Agent：** 以 `agent mcp add` 把函式庫中的伺服器交給特定 Agent；`disable` 可暫停傳送而不移除指派。

```bash
# 1. 加入 Workspace 函式庫（以檔案或 stdin 傳入，避免 Token 進入 Shell 歷史）
multica workspace mcp add --server-config-file ./mcp/jira.json
multica workspace mcp list

# 2. 指派給 Agent（server id 取自 workspace mcp list）
multica agent mcp add <agent-id> <server-id>
multica agent mcp list <agent-id>
multica agent mcp disable <agent-id> <server-id>
multica agent mcp remove <agent-id> <server-id>
```

舊有的 Agent 層級 `--mcp-config`／`--mcp-config-file`／`--mcp-config-stdin`（`{"mcpServers":{...}}` 格式）仍可在 `agent create`／`agent update` 使用。MCP 伺服器可改名而不遺失連線細節與使用中的 Agent（v0.4.40+），設定頁會顯示每個 MCP 伺服器指派給幾個 Agent（v0.6.0+）。

**支援範圍：** Antigravity、GitHub Copilot CLI、DevEco Code、Pi 目前不讀取 Agent 上的 MCP 設定，建立這些 Agent 時不顯示 MCP 欄位；其他工具見[附錄 C](#附錄-c支援的-agent-cli-對照)。MCP 設定的儲存與顯示規則與環境變數相同（存放於 Server、可能含 Token）。

#### 外部工具整合（Composio）

自架部署設定 `COMPOSIO_API_KEY` 後，可在 Agent 的 **Integrations** 連接 Composio 提供的外部工具（OAuth 連線由 Multica 處理，Callback 使用 `COMPOSIO_CALLBACK_BASE_URL` 或 `MULTICA_PUBLIC_URL`）。

### 10.9 複製、封存與還原

**複製（Duplicate／`agent copy`）** 會帶走大部分工作設定（Instructions、Conversation Starters、Skills、自訂參數、頭像、併發上限、Access、模型／Thinking Level／Service Tier），但**不會複製環境變數值、MCP 設定與 `runtime_config`**，需在新 Agent 重新設定。

```bash
multica agent copy <agent-id>                                  # 同一 Runtime，名稱加 " (copy)"
multica agent copy <agent-id> --name "Reviewer-B" \
  --runtime-id <other-runtime> --model <model>                 # 換 Runtime 必須同時指定模型
multica agent copy <agent-id> --no-skills
```

**封存：** 不再使用的 Agent 可封存，封存後不出現在選單、不能被指派或 @提及，歷史保留、可還原。

> ⚠️ **注意：** 封存會取消該 Agent **所有未完成的 Run**（含排隊中與執行中），也會清除其 Chat，使 Slack 等通道不再顯示它仍在工作。

```bash
multica agent archive <agent-id>
multica agent restore <agent-id>
```

### 10.10 狀態顯示

Agent 列表並列兩種狀態：

| 狀態 | 來源 | 值 |
| --- | --- | --- |
| Availability | Runtime | online、offline、unstable |
| Workload | Runs | working、queued、idle |

「Offline」不代表 Agent 被刪除，已排隊的 Run 會等待 Runtime 恢復；只有「archived」代表不再接新工作。

```bash
multica agent list --output json
multica agent get <agent-id>
multica agent tasks <agent-id> --limit 200          # 最新一頁 Run；更多頁以 stderr 印出的 --before 游標續讀
```

### 10.11 企業 Agent 規範

📘 **建議實務：**

| 規範 | 說明 |
| --- | --- |
| 命名 | 以職責命名，例如 `be-impl-orders`、`fe-review`、`db-migration`；避免以模型命名，換模型時不必改名 |
| 單一職責 | 實作、審查、資料庫變更、文件分屬不同 Agent，Instructions 更短、行為更可預測 |
| 最小 Access | 預設 Only me；團隊共用的 Agent 才開 Entire workspace；生產相關 Agent 只開給特定人員 |
| 最小憑證 | 環境變數只放唯讀或單一範圍 Token；寫入權限透過 PR 流程由人類合併 |
| 審查必經 | Agent 交付到 `in_review`，`done` 由人類確認或 PR 合併觸發 |
| 版本化 Instructions | 把 Instructions 原文存在 Git（例如 `agents/*.md`），變更走 PR，再同步到 Multica |
| 成本控管 | 定期檢視 Analytics 與 `multica issue usage`，找出重試頻繁或高成本的 Agent |
| 定期盤點 | 每季封存閒置 Agent，檢視 Access 名單與環境變數 |

---

## 第 11 章：Skills（技能）機制

> **本章重點：** Skill 與 Agent Instructions 的分工；四種建立／匯入方式；從來源更新；`SKILL.md` 結構與支援檔案；綁定 Agent；Workspace Skill、Repo Skill 與 Runtime 本機 Skill 的差異；各 AI 工具的注入路徑；權限與供應鏈風險；企業 Skill Library 治理。

### 11.1 Skill 的定位

Skill 是 Workspace 中一套可重用的工作方法。主檔為 **`SKILL.md`**，可附帶腳本、範本與參考資料。把 Skill 加到 Agent 後，Agent 在處理相關工作時會依循其指引；同一方法不必複製到每個 Agent 的 Instructions，更新也只需維護一處。

| | Agent Instructions | Skill |
| --- | --- | --- |
| 適合放 | 此 Agent 長期的職責、邊界與交付要求 | 某類工作可重用的步驟、資料與工具 |
| 範圍 | 屬於單一 Agent，每次 Run 都提供 | 可加到多個 Agent，個別啟用或停用 |
| 範例 | 「只審查前端程式碼，絕不直接修改」 | 一份無障礙檢查清單與報告範本 |

> ⚠️ **更正：** 舊版手冊第 7 章以 `skills-lock.json` 與 YAML（`triggers`、`steps`、`checklist`）定義 Skill，這**不是** Multica 的 Skill 格式。`skills-lock.json` 是 Multica 原始碼 Repo 自身鎖定開發用 Skill 的檔案；Multica 也沒有依標籤或分支自動觸發 Skill 的機制。v0.6.1 的 Skill 是「`SKILL.md` + 支援檔案」的資料夾，由 Agent 綁定後在 Run 中使用。

### 11.2 建立或匯入 Skill

在 Workspace 的 **Skills** 頁選擇 **New skill**：

| 方式 | 適用 |
| --- | --- |
| **Create manually** | 從空白 `SKILL.md` 開始撰寫 |
| **Import from local** | 選擇包含 `SKILL.md` 的資料夾，或本機的 `.skill`／`.zip` 封存檔（v0.4.36+，可先預覽內容與名稱衝突） |
| **Import from URL** | 從 GitHub、ClawHub 或 Skills.sh 匯入已發布的 Skill |
| **Copy from a runtime** | 掃描已連接電腦上的 Skill，把選取的複製到 Workspace（當下快照，之後本機變更不會同步） |

CLI：

```bash
multica skill create --name api-conventions --description "REST API 設計慣例" \
  --content-file ./skills/api-conventions/SKILL.md
multica skill files upsert --help          # 新增或更新支援檔案
multica skill import --file ./review-helper.skill
multica skill import --url <skill-url>
multica skill list
multica skill search "review"
```

匯入遇到同名 Skill 時，預設**停止且不修改**既有內容，可依意圖選擇：

| `--on-conflict` | 行為 |
| --- | --- |
| `fail`（預設） | 停止 |
| `overwrite` | 覆寫（**只有 Skill 建立者**可用，保留原 ID 與 Agent 綁定；admin 在 App 能編輯也不能用匯入覆寫） |
| `rename` | 以新名稱另存 |
| `skip` | 略過 |

### 11.3 從來源更新

從 GitHub、ClawHub 或 Skills.sh 匯入的 Skill 會保留來源參照，可在 Skill 頁按 **Update**（或列表列選單的「Update from source」），或使用 CLI：

```bash
multica skill refresh <skill-id>
```

| 保留 | 取代 |
| --- | --- |
| Skill 身分：Agent 綁定、標籤、建立者、建立日期 | 名稱（若來源改名）、描述、`SKILL.md` 與所有支援檔案；**本地修改會被覆蓋** |

Skill 建立者與 Workspace `owner`／`admin` 可從來源更新；手動建立、從封存檔匯入或從 Runtime 複製的 Skill 沒有託管來源，只能重新匯入。列表可多選後批次 **Update**（v0.4.28+），沒有來源的會被略過。

### 11.4 Skill 內容結構

每個 Skill 都有主檔 `SKILL.md`，應寫清楚：

- 何時適用；
- 開始前檢查什麼；
- 執行步驟；
- 結果應呈現的形式；
- 何時停下來與成員確認。

支援檔案範例：

```text
SKILL.md
references/api-conventions.md
templates/review-report.md
scripts/check.sh
```

`SKILL.md` 是保留路徑，支援檔案不能使用此名稱；支援檔案會與主檔一起交給 Agent。

📘 **建議實務：企業 Code Review Skill 範例**（可直接作為 `SKILL.md` 起點）

```markdown
---
name: enterprise-code-review
description: 依公司安全與架構規範審查 Pull Request，產出分級報告。
---

# 何時使用
被要求審查 PR、或 Issue 標題含「review」時。

# 開始前
1. 確認 PR 連結與目標分支；取得 diff 與相關測試。
2. 讀取 references/secure-coding.md 與 references/architecture-rules.md。

# 步驟
1. 安全：輸入驗證、注入、敏感資料記錄、授權檢查（對照 OWASP Top 10）。
2. 架構：分層依賴方向、交易邊界、例外處理。
3. 效能：N+1 查詢、不必要的同步呼叫、大量資料分頁。
4. 測試：新增邏輯是否有對應單元測試；測試是否真的驗證行為。

# 產出
使用 templates/review-report.md，依 Blocker / Major / Minor 排序，
每項附檔案路徑與行號；沒有 Blocker 時明確寫「可合併」。

# 何時停下
發現疑似憑證外洩或需變更資料庫結構時，不繼續審查，
在 Issue 留言 @ 技術主管並把狀態設為 blocked。
```

> 💡 **實務建議：** Skill 附件目前以**文字檔**為主。從 Skills.sh 匯入含二進位支援檔（PNG、字型等）的 Skill 仍會失敗（GitHub Issue #1705，2026-10-05 仍為 open）。

### 11.5 綁定 Agent

建立或匯入 Skill 後，仍需加到特定 Agent：在 Skill 頁選擇 Agent（可一次綁多個，v0.3.35+），或從 Agent 的 **Skills** 分頁管理。

- 一個 Agent 可用多個 Skill；一個 Skill 可服務多個 Agent；
- 暫時不需要時，停用綁定而非刪除 Skill（v0.4.8+ 可逐一開關）；
- 編輯從之後的 Run 生效，不影響執行中的 Run；
- 只有能修改該 Agent 的成員可新增、移除或停用其 Skills。

```bash
multica agent skills list <agent-id>
multica agent skills add <agent-id> --skill-ids <skill-id>
multica agent skills set <agent-id> --skill-ids <id-1>,<id-2>     # 取代整份清單
multica skill label add <skill-id> <label-id>
```

### 11.6 三種 Skill 來源

| 類型 | 存放 | 管理方式 |
| --- | --- | --- |
| **Workspace Skill** | Multica | 團隊共同維護，綁定到不同 Agent |
| **Repo Skill** | 程式碼 Repo（如 `.claude/skills/`、`.agents/skills/`） | 由 Repo 管理；Multica 不會自動註冊為 Workspace Skill；是否支援取決於 AI 工具 |
| **Runtime 本機 Skill** | 已連接電腦上（Claude Code、Codex） | 出現在 Agent 的 Skills 分頁，可逐 Agent 停用 |

#### 注入路徑

Run 開始前，Multica 把綁定的 Skill 寫入各工具的原生路徑，讓工具以自身機制發現它們：

| 工具 | 注入路徑 |
| --- | --- |
| Claude Code | `.claude/skills/` |
| Codex | 每次 Run 專屬的 `$CODEX_HOME/skills/`（不寫入系統層 Codex 目錄） |
| Cursor Agent | `.cursor/skills/` |
| GitHub Copilot CLI | `.github/skills/` |
| Antigravity | `.agents/skills/` |
| OpenCode | `.opencode/skills/` |
| Hermes | 每次 Run 專屬的 `HERMES_HOME/skills/`（僅在有綁定 Skill 時隔離） |
| OpenClaw | 當次 Run 工作目錄下的 `skills/` |
| 其他 | 見[附錄 C](#附錄-c支援的-agent-cli-對照) |

Repo 中已存在的 Skill **不會被覆寫**；名稱衝突時，注入的副本改用不同目錄名稱，Run 結束後只清除 Multica 建立的檔案。

### 11.7 權限與供應鏈風險

| 動作 | 誰可以 |
| --- | --- |
| 建立、匯入 | 任何 Workspace 成員 |
| 修改、刪除 | 建立者與 Workspace `owner`／`admin` |
| 檢視、使用 | 所有成員 |

刪除為永久性，會同時從所有 Agent 移除。

> ⚠️ **注意：** 從外部來源匯入的 Skill 可能包含腳本、指令或不安全的指示。**Multica 不會替你審查、簽章或沙箱化**，匯入內容會原樣交給 Agent。來源必須可信。

### 11.8 企業 Skill Library 治理

📘 **建議實務：**

```mermaid
flowchart LR
    A["Skill 提案<br/>（Issue）"] --> B["在 Git Repo<br/>撰寫 SKILL.md"]
    B --> C["PR 審查<br/>（資安 + 領域負責人）"]
    C --> D["合併後匯入<br/>multica skill import --url"]
    D --> E["綁定試點 Agent"]
    E --> F["觀察 Run 品質"]
    F -->|"有效"| G["推廣綁定"]
    F -->|"需修正"| B
    G --> H["來源更新<br/>multica skill refresh"]
```

| 治理項目 | 建議 |
| --- | --- |
| 單一真實來源 | Skill 原文存在內部 Git Repo（例如 `platform/agent-skills`），以 URL 匯入，之後用 `skill refresh` 同步；避免在 UI 直接編輯造成漂移 |
| 審查 | 每個 Skill 變更走 PR，至少一位資安與一位領域負責人核准；特別檢查 `scripts/` |
| 分類 | 以標籤區分 `language/*`、`domain/*`、`process/*`（`multica label create --resource-type skill`） |
| 命名 | 動詞開頭、描述做什麼：`review-java-security`、`write-flyway-migration` |
| 外部 Skill | 先 Fork 到內部 Repo 審查後再匯入，不直接從公開來源匯入正式 Workspace |
| 跨 Workspace | Skill 無法跨 Workspace 共用；以同一 Git 來源分別匯入，確保一致 |
| 汰換 | 每季盤點：停用 90 天未使用的綁定；刪除前確認無 Agent 依賴 |

| 建議的起始 Skill 集 | 用途 |
| --- | --- |
| `api-conventions` | REST 命名、錯誤格式、分頁、版本規則 |
| `enterprise-code-review` | 安全／架構／效能／測試的分級審查（見 11.4） |
| `write-db-migration` | Flyway／Liquibase 命名、可回滾、不鎖大表 |
| `release-notes` | 依 PR 與 Issue 產出版本說明 |
| `incident-triage` | 告警初步分析步驟與回報格式（搭配 Webhook Autopilot） |

---

## 第 12 章：Squads（小隊編組）

> **本章重點：** Squad 解決什麼問題；組成要素；指派後的執行流程與 Leader 每輪看到的內容；Leader 重新觸發規則；指派與 @提及 Squad 的差別；Access 與管理權限；封存；CLI；企業編組範例。

### 12.1 Squad 的定位

Squad 由**一個 Leader Agent** 與任意數量的成員組成。把 Issue 指派給 Squad **不會**同時執行所有 Agent——Multica 先喚醒 Leader，由它讀上下文並決定下一步交給誰。

Squad 解決的是「這件工作該交給誰」：它不會把多個 Agent 合併成新 Agent，也不會自動提高併發量。

| 適合用 Squad | 直接指派 Agent 即可 |
| --- | --- |
| 工作需要多種能力，建立 Issue 時還不確定由誰負責 | 範圍明確，知道該由哪個 Agent 處理 |
| 例：產品交付 Squad 含前端、後端、測試 Agent，由 Leader 依內容分派 | 例：明確的前端 Bug 指派給前端 Agent |

### 12.2 組成要素

| 設定 | 作用 |
| --- | --- |
| **Leader** | 必須是 Agent；接收指派給 Squad 的工作並決定如何處理 |
| **Members** | 可以是 Agent 或人類成員；同一成員可加入多個 Squad |
| **角色描述** | 告訴 Leader 每位成員適合什麼工作；**僅為上下文**，不授予權限、也不會自動觸發成員 |
| **Squad Instructions** | 分派規則、協作規範與 Squad 層級背景；**只提供給 Leader** |

建立 Squad 需要名稱與 Leader，Leader 自動成為成員。v0.3.41 起任何成員都能建立與管理自己的 Squad（不限 admin）。

### 12.3 指派後的執行流程

```mermaid
sequenceDiagram
    autonumber
    participant H as 成員
    participant S as Multica
    participant L as Leader Agent
    participant M as 成員 Agent
    H->>S: 把非 Backlog 的 Issue 指派給 Squad
    S->>L: 為 Leader 排入 Run（不是每位成員）
    L->>L: 讀 Issue + 系統附加的協議、名冊、Squad 指令
    L->>S: 發一則委派評論（以名冊中的 mention 語法 @ 成員）
    L->>S: squad activity 記錄評估結果
    L->>S: 父 Issue 維持 in_progress，Leader 停止
    S->>M: @提及觸發成員 Agent 的 Run
    M->>S: 回報結果（評論）
    S->>L: 重新觸發 Leader 讀取更新
    L->>S: 委派下一步、升級處理、或達成目標後設為 in_review
```

1. **Leader 領取 Run**：與一般 Agent 指派相同。
2. **Leader 被簡報**：系統在 Leader 的 System Prompt 附加三段內容（見 12.4）。
3. **Leader 發一則委派評論**：使用名冊中的確切 mention markdown @ 選定成員，該 mention 會為每位被 @ 的 Agent 觸發新 Run。
4. **Leader 記錄評估**：`multica squad activity <issue-id> <outcome> --reason "..."`，寫入 Issue 活動時間軸，讓人類看到 Leader 確實評估過。
5. **派工回合讓父 Issue 維持 `in_progress`**：協調即是在處理父 Issue 的要求，派工不等於交付。
6. **Leader 停止**：Leader 不親自實作。成員回報、或子 Issue／Stage 屏障關閉時再被觸發，決定委派下一步、升級、達成整體目標後移到 `in_review`，或保持沉默。`done` 留給人類審查者或既有整合（例如帶關閉意圖的 PR 合併）。

Issue 在 **Backlog** 時不觸發 Leader。

### 12.4 Leader 每輪看到的內容

| 區塊 | 內容 | 可否編輯 |
| --- | --- | --- |
| **Squad Operating Protocol** | 硬編碼規則：讀 Issue、以 @提及委派、簡潔（不重述 Issue 內容）、每輪記錄評估、派工後停止、整體目標達成才移到 `in_review` | 否（系統管理） |
| **Squad Roster** | Leader 自己一列，加上每位未封存成員一列；每列附確切的 mention markdown（`[@Name](mention://agent/<uuid>)` 或 `[@Name](mention://member/<uuid>)`），**純文字 `@name` 不會觸發任何人** | 自動產生 |
| **Squad Instructions** | 你的自訂指引（例如「DB 工作給 Alice、前端給 Bob」、升級政策） | 是（Squad 詳情頁或 `multica squad update --instructions`） |

協議中的狀態規則**只適用於指派給此 Squad 的 Issue**。Leader 若是因為在別人的 Issue 上被 `@squad` 提及而喚醒，會被明確告知**不要**動該 Issue 的狀態。

### 12.5 Leader 重新觸發規則

| 事件 | 是否觸發 Leader |
| --- | --- |
| 非成員（人類回報者、外部 Agent）發表評論 | **是** |
| Squad 成員發表不含 @ 的進度更新 | **是**，Leader 重新評估是否需要下一步 |
| 任何人發表明確 @ 其他 Agent／成員／Squad／`@all` 的評論 | **否**，明確的 @ 就是路由訊號 |
| Leader 自己的評論 | **否**，防止迴圈 |
| 只含 Issue 交叉引用（`[MUL-123](mention://issue/...)`）的評論 | **是**，Issue 引用不算路由 |

若 Leader 在此 Issue 已有 `queued` 或 `dispatched` 的 Run，新觸發不會重複排入。例外：Agent 發表的結果中 @ 了另一個 Agent 時，Leader 仍會被喚醒以協調該串討論。

### 12.6 指派與 @提及 Squad

| 動作 | 改變 Assignee | 結果 |
| --- | --- | --- |
| 把 Issue 指派給 Squad | 是 | Squad 成為 Assignee，觸發 Leader |
| 在評論中 @ Squad | 否 | Leader 只處理該則評論，目前 Assignee 不變 |

直接 @ 特定成員則是把工作交給該成員。

### 12.7 Access 與管理權限

- 把 Agent 加入 Squad **不會**繞過其 Access；一般成員建立或管理 Squad 時，只能挑選自己有權執行的 Agent。
- 能否指派或 @ 某個 Squad，取決於你能否執行其 **Leader**；Leader 被封存或你無權執行時，該 Squad 無法被指派或 @。
- 任何成員可建立 Squad；建立者可修改與封存自己的 Squad；`owner`／`admin` 可管理所有 Squad。
- Squad 名稱不必唯一。更換 Leader 時新 Leader 自動加入；目前的 Leader 不能直接移除，需先指定其他 Leader。

### 12.8 封存

封存後 Squad 從列表、Assignee 選單與 @ 選單消失，**無法還原**。為了讓既有工作仍有負責人，目前指派給該 Squad 的 Issue 與 Autopilot 會轉給前 Leader Agent；歷史評論與活動保留。

### 12.9 CLI

```bash
multica squad create --name "Product Delivery" --leader delivery-lead \
  --description "產品交付小隊"
multica squad member add <squad-id> --member-id <agent-id> --type agent \
  --role "負責前端實作"
multica squad member add <squad-id> --member-id <member-id> --type member \
  --role "QA 驗收，處理需要人工判斷的測試"
multica squad member set-role --help
multica squad update <squad-id> --instructions "DB schema 變更一律交給 db-migration；UI 文字變更交給 fe-impl。"
multica squad list
multica squad delete <squad-id>          # 實際為封存
```

### 12.10 企業編組範例

📘 **建議實務：**

| Squad | Leader | 成員 | Squad Instructions 要點 |
| --- | --- | --- | --- |
| 功能交付 | `delivery-lead` | `be-impl`、`fe-impl`、`db-migration`、`qa-tester`、人類 Tech Lead | 先拆子 Issue 並設 Stage；Schema 變更先行；每個 Stage 完成後 @ Tech Lead 確認再進下一 Stage |
| 缺陷處理 | `triage-lead` | `be-impl`、`fe-impl`、`log-analyst` | 先由 `log-analyst` 定位；能重現才派修復；無法重現時 @ 回報者補資訊 |
| 文件與發版 | `docs-lead` | `release-notes`、`api-doc-writer` | 依合併的 PR 產出版本說明與 API 文件差異 |

> 💡 **實務建議：** Agent 之間互相 @ 時，系統會合併同一時刻的重複 Run，但**不會判斷協作何時該結束**——停止條件要寫進 Squad Instructions 與各 Agent 的 Instructions（例如「完成自己的部分後只回報結果，不再 @ 其他 Agent」）。

---

## 第 13 章：日常協作

> **本章重點：** 指派 Issue 與「先不開始」；@提及的觸發預覽、自動路由與合併規則；評論、標註、結論與 Reactions；Chat 一對一對話；Inbox 與訂閱；引導執行中的 Agent（Steer）；Issue Wakeup 事件／條件／時間喚醒。

### 13.1 選擇觸發方式

| 我想… | 使用 |
| --- | --- |
| 讓 Agent 端到端負責一件工作 | 指派 Issue（13.2） |
| 請 Agent 處理某則評論中的問題，不改變負責人 | 在評論中 @提及（13.3） |
| 問個問題、快速嘗試，不想留工作紀錄 | Chat（13.5） |
| 定期或事件驅動執行 | Autopilot（第 15 章） |
| 讓 Agent 在某個事件或時間點再回來處理 | Issue Wakeup（13.8） |
| 在 Agent 執行中途補充指示 | Steer（13.7） |

### 13.2 指派 Issue

1. 開啟 Issue，點 **Assignee**；
2. 選擇 Agent 或 Squad；
3. 在確認對話框檢視即將開始的 Agent，選 **Start**。

Agent 該知道的一切都應寫在 Issue 本身——描述、討論，或 Project 描述與 Agent Instructions。執行中 Agent 可以讀取 Issue 描述、欄位與評論；使用綁定的 Skills、MCP 與 Project 上下文；在本機工作目錄讀檔、執行指令、修改程式碼；發表評論並更新狀態。

#### 先指派、先不開始

確認對話框的 **Don't start yet** 只儲存 Assignee，這次不建立 Run，適合先確定負責人、等背景或依賴就緒再開始。對已有 Agent／Squad 負責人的 Issue，把它從 `backlog` 移出時也會出現相同對話框（目標為 `backlog` 本身或 `done`／`closed` 類別時除外）。

| 情況 | 是否建立 Run |
| --- | --- |
| 指派給 Agent，Issue 在 `todo` 或之後 | 是（除非選 Don't start yet） |
| 指派給 Agent，Issue 在內建 `backlog` | 否，移出 backlog 時才開始 |
| 指派給 Agent，Issue 在 `unstarted` 類別的**自訂**狀態 | **是**（自訂狀態不停車） |
| 指派給 Agent，Issue 已 `done`／`cancelled` | 是 |
| 改派給另一個 Agent | 為新 Assignee 建立新 Run |
| 改派給成員或移除 Assignee | 否 |

> ⚠️ **注意：** 變更 Assignee、取消指派或變更狀態，都**不會停止已開始的 Run**。要中斷請到執行紀錄停止對應的 Run（或 `multica issue cancel-task`）。

```bash
multica issue assign MUL-42 --to "Agent name"
multica issue assign MUL-42 --to-id <agent-uuid> --no-start
multica issue status MUL-42 in_progress --no-start
multica issue assign MUL-42 --unassign
```

腳本中請用 `--to-id <uuid>`，避免模糊比對到同名對象（`--to` 會比對成員、Agent 與 Squad，也接受成員 Email）。`--no-start` 也可用於 `issue update` 與 `issue status`；若同一流程同時變更指派與狀態，兩個指令都要加，否則狀態變更仍會觸發 Run。

### 13.3 在評論中 @提及 Agent

| | 指派給 Agent | 在評論中 @提及 |
| --- | --- | --- |
| 適用 | 讓 Agent 擁有整個 Issue | 讓 Agent 處理目前這則評論 |
| 改變 Assignee | 是 | 否 |
| 改變狀態 | 否 | 否 |
| 每次動作的對象 | 一個 Agent 或 Squad | 可多個 Agent 或 Squad |
| Run 的焦點 | 整個 Issue | 觸發的評論，加上同批合併的評論 |

#### 觸發預覽

在評論編輯器選了 Agent 或 Squad 後，輸入框下方會出現觸發預覽：送出後哪些 Agent 會開始工作、每個目標來自直接 @、Issue Assignee 還是 Squad Leader、目標是否無法使用或你無權執行。取消勾選只略過這一次，不必刪掉名字，也不會改變 Agent 的 Access。

#### 回覆的自動路由

不含任何 @ 的一般評論依討論上下文路由：

1. 回覆 Agent 的評論 → 交給該 Agent；
2. 在已有 Agent 參與的討論串中回覆 → 交給該討論串的 Agent；
3. 不屬於以上的頂層評論 → 交給 Issue 的 Agent Assignee；Assignee 是 Squad 時由 Leader 處理。直接回覆**人類成員**不會退回給 Assignee。

評論明確 @ 了其他對象（包含成員）時，不再套用 Assignee 退回規則。即使目標 Agent 的 Runtime 離線或忙碌，回覆仍留給它，Multica 不會逾時後改派。

#### 連續評論的合併

同一 Agent 在此 Issue 已有等待中的 Run 時，新的連續評論會併入該 Run；若 Agent 正在執行，後續評論會等待目前 Run 結束後**合併為一個後續 Run**。v0.4.42 起不同評論串各自排隊，指示不會落到別串的 Run。一則評論 @ 多個不同 Agent 時，每個 Agent 各自一個 Run。

#### 不觸發 Agent 的評論

- 以 `/note` 開頭：成員之間的筆記，不觸發任何 Agent；
- 使用 `@all`：通知所有成員，並關閉此評論對 Assignee 的自動觸發（`@all` 不包含 Agent）。

### 13.4 評論功能

| 功能 | 說明 |
| --- | --- |
| 格式 | 支援格式化、程式碼區塊、連結與附件；`html` 或 `mermaid` 程式碼區塊會就地渲染，可切換原始碼 |
| 討論串 | 回覆評論形成討論串，可巢狀但都在同一頂層討論下；每則回覆有直接連結（v0.5.1+） |
| 標註（v0.4.43+） | 在 Web／Desktop 選取評論或描述中的文字，加上註記後一起回覆；每則回覆最多 20 個標註、每段引用最多 4,000 字；草稿只存在本裝置 30 天 |
| 結論 | 可把整串標為已解決，或指定一則回覆為結論；在已解決的串中回覆會自動重開 |
| Reactions | 表情回應不觸發 Agent、不改變狀態 |
| 編輯與刪除 | 作者可編輯或刪除自己的評論；`owner`／`admin` 可編輯刪除任何人的評論；Agent 的評論在 UI 只能刪除 |
| 編輯後重算觸發 | 編輯時新增的 @ 也會建立 Run |

@ 對象的效果：

| 對象 | 效果 |
| --- | --- |
| 成員 | Inbox 收到提及通知（評論中的 @ 不會建立訂閱） |
| Agent | 為該 Agent 建立 Run（Agent 沒有 Inbox） |
| Squad | 通知 Squad 成員並觸發 Leader |
| Issue | 插入另一個 Issue 的連結，不通知、不觸發 |
| `@all` | 通知所有成員，不觸發任何 Agent |

純文字 `@name` 不會建立提及，必須從編輯器建議清單選取；輸入有效的 Issue key 會自動轉為連結（v0.3.43+）。

> ⚠️ **注意：** 刪除評論無法復原。只會刪除該則評論；若有回覆，回覆保留在討論串中。例外是串的第一則評論，會留下「This comment was deleted」佔位。內容有誤時請改用編輯。

CLI：

```bash
multica issue comment list MUL-123 --tail 20
multica issue comment add MUL-123 --content-file ./review.md
multica issue comment add MUL-123 --parent <comment-id> --content "已處理"
multica issue comment update <comment-id> --expected-revision 2 --content-file revised.md
multica issue comment resolve <comment-id>
multica issue comment delete <comment-id>
```

> 💡 **Windows 注意：** 多行或含非 ASCII 字元的內容，建議用 `--content-file`／`--description-file`，Windows 上 stdin 管線可能破壞非 ASCII 位元組。這些檔案預設必須位於目前工作目錄內，否則需加 `--allow-external-file`。

### 13.5 Chat：一對一對話

Chat 是你與**一個 Agent** 之間的一對一對話，脫離 Issue 看板：

- Agent **沒有 Issue 上下文**，不會看你的看板，也不會自行把對話轉成 Issue；
- 對話**完全私密**，Workspace 其他人（包括 admin）都看不到；
- 仍可透過 Multica CLI 在權限範圍內查詢 Workspace、Project、Issue 與 Skill；
- 可點輸入框左下 **+** → **Project context** 附加 Project，Agent 會收到該 Project 的描述、Repo 等資源（v0.4.10+）。

| 需求 | 較適合 |
| --- | --- |
| 快速提問、探索方案、私人草稿 | Chat |
| 明確的負責人、狀態、優先序與交付物 | Issue |
| 讓隊友看到背景並接續討論 | Issue |

操作重點：

- 每則訊息建立一個 Run；Agent 工作時可持續送出訊息，訊息排隊依序處理，排隊中的訊息可立即送出、編輯、移除或清空（v0.4.19+）；
- 對話會嘗試延續 AI 工具的原始 Session；Session 不存在時改用新 Session，但訊息歷史保留；
- 輸入框旁的停止鍵可中斷 Run；
- Agent 可在回覆中傳送圖片與檔案（v0.4.0+）；回覆下方可能出現一鍵追問建議（需伺服器端 LLM，見 6.8）；
- 對話可改名、置頂、封存（唯讀）、取消封存、刪除；綁定外部通道（如 Slack）的對話封存後綁定即中斷，取消封存不會恢復。

> ⚠️ **注意：** 刪除對話無法復原，並會停止其中未完成的 Run。團隊需要共同知道的結論，請寫進 Issue、Project 描述或 Skill。

### 13.6 Inbox 與訂閱

Inbox 彙整與你有關的工作活動，不是完整的活動紀錄。

**會進 Inbox 的通知：**

- Issue 指派給你或從你身上移走；
- 你訂閱的 Issue 有新評論，或 Assignee、狀態、優先序、日期變更；
- 有人在 Issue 描述或評論中 @ 你；
- 你建立的 Issue 或評論收到 Reaction；
- 你訂閱的 Issue 上 Agent Run 失敗；
- 透過 Agent 建立 Issue（quick-create）完成或失敗；
- 你訂閱的 Autopilot 建立了新 Issue，或因連續失敗被暫停。

自己的動作不會通知自己；同一 Issue 的多則通知合併為一筆。

**自動訂閱來源：** Issue 建立者、新 Assignee、任何留言者、在 Issue 描述中新被 @ 的人、Autopilot 預設的訂閱者。變更 Assignee 不會移除既有訂閱；子 Issue 狀態變更也會通知父 Issue 的訂閱者。

**處理通知：** 選取即標為已讀；右鍵可 Mark as unread／Archive；Inbox 選單可全部已讀、全部封存、封存已讀、封存已 `done`／`cancelled` 的 Issue 通知。Issue 進入把工作交回人類的狀態（`in_review`、`started` 類別的自訂狀態、`done`／`closed` 類別）時，其 Run 失敗通知會自動封存；`blocked` 例外。可依發起者、未讀、Issue 狀態與優先序篩選（v0.4.33+）；按 `E` 封存開啟中的通知。

**通知類型設定：** **Settings → Notifications** 可分別開關六組：指派、狀態變更、評論、提及、優先序與日期、Agent 活動。Reactions、quick-create 結果、Autopilot 暫停等少數類型永遠送達。

```bash
multica issue subscriber add MUL-42 --user "Alice"
multica issue subscriber list MUL-42
multica issue subscriber remove MUL-42 --user-id <uuid>
```

### 13.7 引導執行中的 Agent（Steer）

v0.5.2 起，可在 Agent **執行中**直接回覆補充指示，訊息會進入**目前這次 Run**，而不是下一次。v0.6.0 起回覆時可選擇：

| 選項 | 行為 |
| --- | --- |
| 加入目前 Run | 把新指示送入執行中的 Run |
| 排入新 Run | 等目前 Run 結束後再執行 |
| 重新開始 | 中斷並以新指示重新開始 |

系統會顯示「Agent 已收到回覆」的回執。依 v0.6.1 README，此能力目前支援 **Claude Code、Codex 與 Grok**；其他工具的回覆會依 13.3 的合併規則排入後續 Run。

### 13.8 Issue Wakeup（事件、條件與時間喚醒）

Wakeup 讓 Agent 或成員在 Issue 上儲存「事件訂閱、條件或計時器」：Agent 先結束這次 Run，等輸入到達時再收到一次**普通的 Run**。平台只比對它儲存的事實（欄位值、子 Issue 狀態、PR 狀態），業務上是否完成仍由 Agent 讀取目前狀態後判斷；沒有休眠中的行程，也沒有第二套 Run 生命週期。

| 版本 | 能力 |
| --- | --- |
| v0.5.1 | 評論到達或指定排程時喚醒；從 Issue 側欄或 Autopilot 管理 |
| v0.6.0（Wakeup v2） | 條件式喚醒（狀態改變、子 Issue 完成、PR 狀態）、到期時間、失控保護、check-in 與可見性 |

Issue 側欄集中顯示事件與時間 Wakeup，可直接開關；Issue 進入終態類別（`done`／`closed`）時所有 Wakeup 停用，重新開啟也不會自動恢復。

```bash
multica issue wakeup events                    # 可訂閱的事件類型
multica issue wakeup create MUL-42 --kind at --after 10m --instruction-file ./next.md
multica issue wakeup create MUL-42 --kind every --every 1h --max-fires 24 --instruction-file ./poll.md
multica issue wakeup create MUL-42 --kind cron --cron '0 9 * * 1-5' --timezone Asia/Taipei \
  --instruction-file ./daily.md
multica issue wakeup create MUL-42 --until-pr merged --expires-in 72h --on-timeout wake \
  --instruction-file ./after-merge.md
multica issue wakeup create MUL-42 --until-children-done --stage 1 --instruction-file ./stage2.md
multica issue wakeup create MUL-42 --until-status in_review --instruction-file ./qa.md
multica issue wakeup list MUL-42
multica issue wakeup disable --help
```

| 條件旗標 | 意義 |
| --- | --- |
| `--until-status KEY` | 此 Issue 狀態變為 KEY |
| `--until-children-done [--stage N]` | 所有子 Issue（或 N 以前的 Stage）關閉 |
| `--until-pr checks\|merged` | 連結的 PR 檢查完成或已合併 |
| `--until-issue <id> --until-issue-state done\|ended\|in_review` | 另一個 Issue 到達指定狀態 |
| `--until-assignee`、`--until-label`、`--until-property` | 指派、標籤、屬性條件 |
| `--expires-in`／`--expires-at`、`--on-timeout end\|wake` | 到期時結束，或喚醒一次處理逾時 |

> 💡 **實務建議：** Wakeup 主要由 Agent 在 Run 中自行建立（例如「等 PR 檢查跑完再回來看」）。在 Agent Instructions 中寫明何時可以建立 Wakeup、最多幾次（`--max-fires`）與到期時間，避免出現長期無人關注的週期喚醒。

---

## 第 14 章：Runtime、Daemon 與 Run 執行

> **本章重點：** Daemon 與 Runtime 的差別；啟動與管理 Daemon；26 種支援的 AI 編碼工具與最低版本；安裝驗證；Run 的 8 種狀態與逾時規則；失敗原因代碼與自動重試；併發；私有／公開 Runtime；自訂 Runtime Profile；Task 執行環境變數；Runtime 管理 CLI；離線排查。

### 14.1 Daemon 與 Runtime

| 名詞 | 定義 |
| --- | --- |
| **Daemon** | 在一台電腦上執行的 Multica 背景行程：連線 Server、偵測本機工具、領取 Run、回報結果 |
| **Runtime** | Workspace 可用的一個具體執行環境＝一台電腦 ＋ 一種 AI 工具（或一個自訂 Runtime Profile） |

例如一台電腦裝了 Claude Code 與 Codex、連接兩個 Workspace，Daemon 會在每個 Workspace 各註冊 Claude Code 與 Codex 兩個 Runtime。重啟 Daemon 只會更新既有紀錄，不會一直新增。

AI 工具本身、工具的登入憑證與本機程式碼目錄都留在執行電腦上。Server 不代替本機工具執行指令，也不自動上傳整個工作目錄；但 Agent 選擇讀取並寫進回覆的程式碼片段會存入 Server。

### 14.2 啟動與管理 Daemon

使用 Multica Desktop 時，App 會自動啟動 Daemon。Web、遠端電腦或無介面環境則先安裝 CLI（第 19.1 節）再執行：

```bash
multica daemon start
```

| 指令 | 用途 |
| --- | --- |
| `multica daemon status [--output json]` | 顯示 Daemon 與連線狀態 |
| `multica daemon logs -f`／`-n 200` | 追蹤日誌／顯示最後 N 行（會先印出實際日誌檔路徑） |
| `multica daemon restart` | 重啟並重新偵測本機工具 |
| `multica daemon stop` | 停止 |
| `multica daemon start --foreground` | 在目前終端機前景執行，便於除錯 |
| `multica daemon disk-usage [--by-workspace\|--all-profiles]` | 檢視工作目錄磁碟用量 |

`daemon start`／`restart` 常用旗標（皆有對應 `MULTICA_*` 環境變數）：

| 旗標 | 說明 |
| --- | --- |
| `--device-name`、`--runtime-name` | 顯示名稱 |
| `--workspaces-root` | 工作目錄根（優先於 `MULTICA_WORKSPACES_ROOT` 與設定檔；變更不會搬移既有目錄） |
| `--max-concurrent-tasks` | 全機併發上限 |
| `--agent-timeout` | 每次 Run 絕對時限（`0` 不限） |
| `--poll-interval`、`--heartbeat-interval`、`--ws-claim-poll-interval` | 輪詢與心跳 |
| `--no-auto-update`、`--auto-update-interval` | CLI 自動更新 |
| `--no-auto-reload` | 磁碟上的 `multica` 被替換時不自動重啟 |

> ⚠️ **注意：** Daemon 啟動時**至少要偵測到一種內建支援的 AI 工具**才會啟動；自訂 Runtime Profile 在 Daemon 啟動後才同步，不能作為空白機器的唯一啟動條件。剛安裝或剛登入的工具，需重啟 Daemon 才會被偵測（v0.4.14 起，啟動後才安裝的 CLI 也會自動出現）。

### 14.3 支援的 AI 編碼工具

v0.6.1 共支援 26 種 CLI（官方 README 計數）。下表整合官方 Providers 與安裝文件：

| 工具 | 偵測指令 | Session 續接 | Multica 管理 MCP | 最低版本／備註 |
| --- | --- | :---: | :---: | --- |
| Claude Code | `claude` | ✓ | ✓ | 2.0.0+ |
| OpenAI Codex | `codex` | ✓ | ✓ | 0.100.0+ |
| Cursor Agent | `cursor-agent` | ✓ | ✓ | |
| GitHub Copilot CLI | `copilot` | ✓ | — | 1.0.0+ |
| Antigravity | `agy` | ✓ | — | 1.1.10+ |
| OpenCode | `opencode` | ✓ | ✓ | 1.1.54+ |
| OpenClaw | `openclaw` | ✓ | ✓ | |
| Hermes | `hermes` | ✓ | ✓ | |
| Pi | `pi` | ✓ | — | Session 依賴本機檔案路徑 |
| Oh-My-Pi | `omp` | ✓ | ✓ | |
| Kimi CLI | `kimi` | ✓ | ✓ | |
| Kiro CLI | `kiro-cli` | ✓ | ✓ | |
| Grok Build | `grok` | ✓ | ✓ | 0.2.89+ |
| Qwen Code | `qwen` | ✓ | ✓ | 0.20.0+ |
| QwenPaw | `qwenpaw` | ✓ | ✓ | 模型由 QwenPaw 自身設定 |
| Qoder CLI | `qodercli` | ✓ | ✓ | |
| Qoder CN CLI | `qoderclicn` | ✓ | ✓ | |
| Trae CLI | `traecli` | ✓ | ✓ | |
| CodeBuddy | `codebuddy` | ✓ | ✓ | |
| Huawei Cloud CodeArts | `codearts` | ✓ | ✓ | 以 `codearts run` 驗證非互動路徑 |
| DevEco Code | `deveco` | ✓ | — | HarmonyOS 編碼 Agent |
| DeepSeek Harness | `dsh` | ✓ | ✓ | 需 Multica Runtime Profile 與 `DEEPSEEK_API_KEY` |
| MiniMax Code | `mcode` | — | ✓ | 0.1.2+；Node.js `>=22.19 <23` 或 `>=24 <27` |
| Reasonix | `reasonix` | ✓ | ✓ | 需先 `reasonix setup` |
| Dim | `dim` | ✓ | ✓ | |
| ZeroClaw | `zeroclaw` | 未列 | 未列 | v0.4.33+；模型由 Agent Profile 決定（官方 Providers 表未列能力欄） |

> 💡 「支援」代表 Multica 能呼叫該 CLI，**不代表** Multica 提供該工具的帳號、訂閱或模型額度。低於最低版本時，Daemon 不會註冊該 Runtime。各工具的 Skill 注入路徑與環境變數見[附錄 C](#附錄-c支援的-agent-cli-對照)。

與舊版手冊相比，支援清單有一項移除：

> ⚠️ **更正：** 舊版手冊將 Gemini 列為支援工具。v0.6.1 的 README、Providers 與安裝文件均未列出 Gemini CLI，本版移除。

### 14.4 安裝並驗證 AI 工具

**步驟 1：在終端機單獨啟動工具一次**，完成登入或模型供應商設定。工具在終端機無法完成請求，Daemon 呼叫時也會以同樣方式失敗。登入憑證由工具自行存放在本機，**Multica 永遠不會收到 Claude、Codex、Cursor 等工具的登入 Token**。

**步驟 2：確認 Daemon 找得到指令：**

```bash
# macOS / Linux / WSL
command -v claude
claude --version
```

```powershell
# Windows PowerShell
Get-Command claude
claude --version
```

終端機找得到、但 Desktop 或背景 Daemon 找不到時，通常是兩者 `PATH` 不同：重啟 App，或以 `MULTICA_<PROVIDER>_PATH` 指定絕對路徑。v0.4.26 起可辨識透過 Volta 或 Vite Plus 安裝的工具。

**步驟 3：重新偵測：**

```bash
multica daemon restart
```

Desktop 則重開 App。之後在 **Runtimes** 頁確認該工具在目標電腦下顯示為 online。

特殊工具的設定要點：

| 工具 | 要點 |
| --- | --- |
| CodeArts | `run`、`models`、`serve` 需要 `CODEARTS_CLI_AK`／`CODEARTS_CLI_SK`；以 `codearts run --model provider/model "Reply OK"` 驗證 |
| Reasonix | 先執行 `reasonix setup` 設定預設供應商與模型 |
| QwenPaw、MiniMax Code | 模型在工具自身設定，Multica 無法於執行期覆寫 |
| DeepSeek Harness | `npm install -g @deepseek-ai/dsh`，再安裝 Multica Runtime Profile（`dsh plugin --profile multica add <bundle>` 或設定 `MULTICA_DSH_PROFILE_BUNDLE`）；Bridge 尚未發布到公開 npm，需自 [multica-ai/dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) 建置 |
| Claude Code | 不可以 root 或 sudo 啟動（v0.3.40 起會顯示明確錯誤） |

### 14.5 Run 生命週期

| 狀態 | 意義 | 逾時與後果（預設） |
| --- | --- | --- |
| `deferred` | 排定稍後觸發 | 到時間進入 `queued` |
| `queued` | 等待 Runtime 領取 | 只要 Runtime 持續心跳就一直等；只有在 **Runtime 沉默超過重連寬限期，且 Run 本身也排隊這麼久** 時才失敗（`queued_expired`），不自動重試 |
| `dispatched` | 已被領取，工具啟動中 | 超過 **5 分鐘** 視為失敗 |
| `waiting_local_directory` | 目標本機目錄被其他 Run 占用（Direct 模式） | 無自身逾時，目錄釋放後繼續 |
| `running` | AI 工具執行中 | **無固定時長上限**；存活依心跳判斷（每 15 秒一次），失去心跳的 Runtime 最慢約 3 分鐘標為離線，其 Run 一併失敗 |
| `completed` | 正常結束 | — |
| `failed` | 錯誤或中斷 | 見 14.6 |
| `cancelled` | 手動停止，或隨封存／刪除取消 | — |

```mermaid
stateDiagram-v2
    [*] --> deferred: 排程觸發
    [*] --> queued: 指派 / 提及 / Chat / Autopilot
    deferred --> queued: 到達排定時間
    queued --> dispatched: Runtime 領取
    dispatched --> waiting_local_directory: 本機目錄被占用
    waiting_local_directory --> dispatched: 目錄釋放
    dispatched --> running: 工具啟動成功
    running --> completed
    running --> failed
    dispatched --> failed: 超過 5 分鐘
    queued --> failed: queued_expired
    queued --> cancelled
    running --> cancelled
    completed --> [*]
    failed --> [*]
    cancelled --> [*]
```

Server **不會**只因 Run 執行很久就強制結束；Runtime 依實際活動判斷行程是否卡住（`MULTICA_AGENT_IDLE_WATCHDOG` 預設 2 小時、`MULTICA_AGENT_TOOL_WATCHDOG`、`MULTICA_AGENT_TIMEOUT` 預設不限）。

**檢視 Run：** Issue 右側欄的 **Execution log** 列出所有 Run（進行中置頂，已結束收在 **Show past runs (N)**），每列顯示觸發來源、執行 Agent、狀態與時間；Issue 標頭會顯示「Engineer is working」等即時標籤。可在此：

- **View transcript**：Agent 訊息、工具呼叫與錯誤輸出（執行中持續串流，可切換 Newest first）；
- 停止 `deferred`、`queued`、`dispatched`、`waiting_local_directory`、`running` 的 Run；
- 重試失敗或取消的 Run。

```bash
multica issue runs MUL-123
multica issue run-messages <run-id> --issue MUL-123 --since 42     # 只取序號 42 之後的訊息
multica issue cancel-task <run-id> --issue MUL-123
multica issue rerun MUL-123        # 以目前 Assignee、全新 Session 與工作目錄重跑
```

### 14.6 失敗原因與自動重試

**平台端失敗原因：**

| 代碼 | 意義 | 處理 |
| --- | --- | --- |
| `runtime_offline` | 執行中 Runtime 離線 | 恢復 Runtime 後重試 |
| `queued_expired` | Runtime 停止心跳超過寬限期，且 Run 也排隊這麼久 | 確認 Runtime 在線後重試 |
| `runtime_recovery` | Daemon 重啟後回收中斷的 Run | 直接重試 |
| `environment_prepare_failed` | 無法準備工作目錄或本機 Runtime 設定 | 檢查磁碟空間、權限、目錄占用、工具本機設定 |
| `cancelled` | 手動停止或隨封存／刪除取消 | 無需處理 |
| `timeout` | 超過 Daemon 設定的執行時限 | 縮小範圍或調整 `agent_timeout` |
| `iteration_limit` | 達到單次 Run 的迭代上限 | 縮小 Issue 範圍 |
| `agent_blocked` | Agent 回報無法繼續 | 提供其評論所要求的資訊 |
| `api_invalid_request` | 平台 API 拒絕無效請求 | 重試；重複發生請回報 |
| `codex_semantic_inactivity` | Codex 太久沒有有意義的輸出 | 重試或調整 Codex 靜默門檻 |

**工具端失敗原因（`agent_error.*`）：**

| 代碼 | 意義 | 處理 |
| --- | --- | --- |
| `provider_auth_or_access` | 模型供應商驗證失敗（401／403） | 在該工具重新登入或檢查 API Key |
| `provider_quota_limit` | 額度或餘額用盡（402；v0.6.1 起 403 用量上限也歸此類） | 加值或換帳號 |
| `provider_capacity_or_rate_limit` | 限流或容量不足（429／529） | 稍後重試 |
| `provider_server_error` | 供應商伺服器錯誤（5xx） | 稍後重試 |
| `provider_network` | 連到供應商的網路失敗 | 自動重試；持續發生請檢查執行電腦網路 |
| `model_not_found_or_unavailable` | 模型不存在或暫不可用 | 在 Agent 設定改選可用模型 |
| `context_overflow` | 超過模型上下文視窗 | 縮小範圍或減少輸入 |
| `missing_config` | 缺少 API Key 等必要設定 | 補 Agent 環境變數或工具設定 |
| `runtime_missing_executable` | 找不到 AI 工具執行檔 | 重新安裝工具 |
| `runtime_version_unsupported` | 工具版本太舊 | 升級工具 |
| `process_failure` | 工具行程異常結束 | 檢視 Run 紀錄後重試 |
| `empty_or_unparseable_output` | 無輸出或無法解析 | 重試；重複發生請檢查工具安裝 |
| `agent_timeout` | 工具太久無回應被終止 | 重試或縮小範圍 |
| `unknown` | 未分類 | 檢視 Run 紀錄中的原始錯誤 |

**自動重試**僅涵蓋暫時性故障，且只適用於掛在 Issue 或 Chat 上的 Run（不含 Autopilot 的 run only 模式）：

| 可自動重試的原因 | 嘗試上限 |
| --- | --- |
| Runtime 離線 | 預設 2 次（首次 + 1 次重試） |
| Daemon 重啟後回收 | 預設 2 次 |
| 平台判定的執行逾時 | 預設 2 次 |
| Codex 停滯無有意義輸出 | 預設 2 次 |
| Skill Bundle 下載失敗 | 預設 2 次 |
| 工具網路中斷 | 最多 3 次（最後一次約延遲 5 秒） |

驗證、額度、設定、模型等其他原因**永不自動重試**，需先修正原因再手動重試。手動重試會呼叫**當時處理該 Run 的 Agent**（即使 Issue 已改派），盡量保留前一次寫入本機目錄的檔案；Session 仍安全且由同一 Runtime 領取時，也會延續原 Session。當 Issue 沒有其他進行中的 Run、也沒有待執行的重試時，失敗會讓 `in_progress` 的 Issue 退回 `todo`。

### 14.7 派工與併發

Runtime 註冊後維持長連線；新 Run 進入佇列時 Server 通知對應 Daemon，Daemon 也定期輪詢作為斷線備援，因此 Runtime 在線且有餘裕時，Run 通常立即開始。

| 上限 | 預設 | 調整方式 |
| --- | --- | --- |
| 每個 Daemon | 20 | `MULTICA_DAEMON_MAX_CONCURRENT_TASKS` 或 `--max-concurrent-tasks` |
| 每個 Agent | 6 | Agent 設定或 `agent update --max-concurrent-tasks` |
| 實際併發 | 兩者較小值 | |

達到上限後新 Run 持續排隊。平行 Run 會同時競爭機器資源、工具帳號額度與同一工作目錄；Run 必定綁定其 Runtime，**不會移到其他機器**。

### 14.8 私有與公開 Runtime

本機 Runtime 預設為**私有**：只有 Runtime 擁有者能在其上建立 Agent，Workspace `owner`／`admin` 也不例外——那是別人的電腦，在上面執行 Agent 會花費對方的機器資源與工具憑證。

只有 Runtime 擁有者能把它設為**公開**（admin 可以改名或刪除，但分享與否由擁有者決定）。公開後其他成員也能選用此 Runtime，但**不會分享底層 AI 工具的登入憑證**，只是讓成員的 Agent Run 路由到這台電腦。

> 📘 **建議實務：** 企業共用 Runner 主機應由平台團隊的服務帳號擁有並設為公開，AI 工具以服務帳號或團隊訂閱登入；個人筆電上的 Runtime 保持私有。

### 14.9 自訂 Runtime Profile

團隊使用內部 Wrapper、版本鎖定的執行檔，或需要為相容工具加上固定參數時，可建立自訂 Runtime Profile。它不新增通訊協定，而是選擇 Multica 已支援的協定家族，並要求指令與該家族相容。

| 規則 | 說明 |
| --- | --- |
| 誰能建立 | Workspace `owner`／`admin` |
| 共用範圍 | 整個 Workspace；每台電腦自行在 `PATH` 中解析指令，只有解析得到的電腦會註冊對應 Runtime |
| 指令欄位 | 執行檔加參數，**不是 Shell 腳本**；支援一般參數、引號與反斜線跳脫，不支援管線、重導向、`&&`、`;`、反引號、變數展開（需要時寫成 Wrapper 腳本） |
| 參數順序 | `<你的指令> <你的固定參數> <Multica 協定參數> <Agent 自訂參數>`（讓 `ccms start q36` 這類子指令式 Wrapper 可運作） |
| 衝突 | Multica 的值在後面、會生效；Agent 選的模型會覆蓋 Profile 固定的 `--model`（要全員鎖定模型就讓 Agent 模型欄位留空） |
| 協定關鍵旗標 | `-p`、`--output-format`、`--input-format`、`--permission-mode` 等會從固定參數中被丟棄 |

```bash
multica runtime profile create \
  --display-name "Claude (pinned 2.1)" \
  --command-name claude-2.1 \
  --protocol-family <family> \
  --description "版本鎖定的 Claude Code"
multica runtime profile list
multica runtime profile set-path <profile-id> --path /opt/tools/claude-2.1   # 僅限本機，不上傳
multica runtime profile unset-path <profile-id>
```

編輯 Profile 只影響之後領取的 Run；刪除前要先處理仍綁定其 Runtime 的 Agent。只刪除某台電腦上的 Runtime 實例不會刪除 Profile（執行中的 Daemon 會重新註冊）。

### 14.10 Task 執行環境

Daemon 啟動 Agent Task 時，會把 Task 上下文注入 Runtime 行程。Agent 的自訂環境變數**不能**覆蓋任何 `MULTICA_` 變數或 Task 暫存目錄變數。

| 變數 | 值 | 穩定性 |
| --- | --- | --- |
| `MULTICA_TOKEN` | Task 範圍的 `mat_` API 憑證 | **整合契約** |
| `MULTICA_TASK_ID` | 目前 Task ID | **整合契約** |
| `MULTICA_AGENT_ID` | 指派的 Agent ID | **整合契約** |
| `MULTICA_WORKSPACE_ID` | Task 所屬 Workspace | **整合契約** |
| `MULTICA_SERVER_URL` | Daemon 選用的 Server 網址 | **整合契約** |
| `MULTICA_TASK_CONFIG_ROOT` | Task 私有的 CLI 設定根 | 資訊性 |
| `MULTICA_TASK_WORKSPACES_ROOT` | Daemon 管理的 Task 工作區根 | 資訊性 |
| `MULTICA_AGENT_NAME` | Agent 顯示名稱 | 資訊性 |
| `MULTICA_DAEMON_PORT` | 本機 Daemon 健康／API 埠（供 `multica repo checkout` 等使用） | 資訊性 |
| `MULTICA_TASK_SLOT` | 全機併發池中的槽位，可用於 GPU 等依槽位分配的資源 | 資訊性 |
| `TMPDIR`（及 `TMP`、`TEMP`） | 此 Task 私有的暫存目錄 | 資訊性 |

只有標示為**整合契約**的五個變數可作為整合依據，其他可能變動。在 Task 中執行的 `multica` CLI 不會載入或修改使用者的 Profile 檔，`login`、`setup`、`workspace switch`、`daemon start/stop/restart` 等人類操作無法使用；`daemon status` 與 `daemon disk-usage` 則限縮在承載它的 Runtime 範圍內。

#### Agent 在 Task 中 checkout Repo

```bash
multica repo list
multica repo checkout <repo-url>                   # 預設遠端預設分支
multica repo checkout <repo-url> --ref release/1.2
multica repo checkout <repo-url> --fresh           # 丟棄未提交變更，從最新預設分支開新分支
```

Repo 快取（`.repos/` 共享 bare clone）以 worktree 方式提供給各 Task，同一 Session 的 Task 會持續在同一分支工作；提交使用 Task 自己的 Git 身分（v0.5.0+）。

### 14.11 Runtime 管理 CLI

```bash
multica runtime list
multica runtime rename <runtime-id> "Office Mac"
multica runtime usage <runtime-id>            # 用量與成本
multica runtime activity <runtime-id>         # 活動紀錄
multica runtime update <runtime-id> --target-version <version> --wait   # 遠端觸發該 Runtime 的 CLI 更新
multica runtime delete <runtime-id>           # 仍有綁定 Agent 時預設拒絕
multica runtime delete <runtime-id> --cascade # 解除綁定（保留 Agent 設定與歷史）並取消其進行中 Run
```

v0.4.17 起刪除 Runtime 會保留 Agent，可把它們改指向其他機器繼續使用。離線超過 7 天且沒有任何綁定 Agent（含已封存）的 Runtime 會自動清除。

### 14.12 離線 Runtime 排查

依序檢查：

1. `multica daemon status`：Daemon 是否在執行；
2. `multica daemon logs -f`：尋找登入、網路或工具偵測錯誤；
3. 在同一環境執行 `command -v <tool-command>`：Daemon 是否找得到工具；
4. Multica **Runtimes** 頁：目標電腦與對應工具是否顯示 online；
5. 安裝工具、變更路徑或更新 Profile 後執行 `multica daemon restart`。

仍無法解決時見第 21.7 節。

---

## 第 15 章：Autopilots（自動化排程與事件觸發）

> **本章重點：** Autopilot 的組成；Create issue 與 Run only 兩種執行模式；排程觸發（Cron 與時區）；Webhook 觸發、冪等、事件篩選、URL 保護與回應碼；執行紀錄與重播；自動暫停規則；權限；CLI；企業應用範例。

### 15.1 Autopilot 的組成

Autopilot 執行反覆發生的工作——每日進度摘要、定期依賴檢查、由外部系統事件啟動的 Agent。每個 Autopilot 儲存一份 **Runbook**、一個 **Assignee** 與一或多個 **Trigger**；觸發時 Multica 建立 Issue 或直接執行 Agent，並保留每一次執行紀錄。

| 欄位 | 說明 |
| --- | --- |
| 名稱 | 這個 Autopilot 負責什麼 |
| Runbook | Agent 每次執行都會讀的目標、背景、限制與步驟 |
| Assignee | Agent 或 Squad |
| Project | 選用；自動建立的 Issue 放入指定 Project |
| 執行模式 | Create issue 或 Run only |
| 訂閱者 | 自動建立 Issue 後要通知的成員 |
| Trigger | 排程或 Webhook（可多個） |

在側欄開啟 **Autopilot**，選範本或從頭建立。儲存後預設啟用；**Run now** 可隨時手動完整執行一次（v0.4.41+ Agent 也能代你啟動）。

### 15.2 執行模式

| 模式 | 行為 | 適用 |
| --- | --- | --- |
| **Create issue**（`create_issue`） | 每次觸發先建立 Issue，再指派給 Assignee；討論、狀態與 Run 紀錄都在 Issue 上 | 團隊需要審查、確認或後續追蹤的工作 |
| **Run only**（`run_only`） | 直接建立 Run，不建立 Issue；結果只在 Autopilot 執行紀錄中可見 | 不需協作紀錄的背景工作 |

- Create issue 模式與一般 Issue 共用 Run 佇列：Runtime 離線時 Issue 仍會建立，Run 等待 Runtime 上線；基礎設施失敗依第 14.6 節規則重試。
- Run only 模式要求觸發當下 Runtime 可用，否則該次顯示為 skipped，不會留下等待中的 Issue；失敗**不自動重試**（避免與下一次排程重疊）。

### 15.3 排程觸發

排程編輯器（v0.4.4+）可選擇執行時間、重複日、時間窗與時區，並預覽接下來的執行時間；一個 Autopilot 可有多個排程。需要更複雜規則時直接編輯標準 5 欄位 Cron：

```text
minute hour day month weekday
```

| Cron | 時區 | 意義 |
| --- | --- | --- |
| `0 9 * * 1-5` | `Asia/Taipei` | 平日 9:00 |
| `*/30 * * * *` | `UTC` | 每 30 分鐘 |
| `0 3 * * *` | `UTC` | 每天 3:00 |
| `0 18 * * 5` | `Asia/Taipei` | 每週五 18:00 |

Cron 沒有秒欄位，時區使用 IANA 名稱。儲存前請對照頁面上的「next runs」。個別排程可單獨編輯或暫停（v0.5.0+），不必刪除重建。

### 15.4 Webhook 觸發

新增 Webhook Trigger 後，Multica 產生唯一 URL，傳送 JSON 物件或陣列即可觸發：

```bash
curl -X POST "$MULTICA_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: build-20261005-001" \
  -d '{"event":"build.completed","eventPayload":{"status":"failed","job":"core-api"}}'
```

Payload 會存入投遞與執行紀錄並交給 Agent；Create issue 模式下也會附加到 Issue 描述。

| 限制 | 說明 |
| --- | --- |
| Body | 必須是有效的 JSON 物件或陣列，上限 256 KiB |
| 冪等 | `Idempotency-Key` 防止發送端重試造成重複執行；GitHub 投遞另以 `X-GitHub-Delivery` 去重；沒有穩定的冪等鍵時無法保證只執行一次 |
| 停用／不符 | Trigger 停用或事件不符時記錄為 ignored，不建立 Run |

#### 事件篩選

同一來源送出多種事件時，可在 Trigger 加上篩選：每列一個事件名稱加上選用的 action 清單，任一列符合即觸發；全部留空則接受所有事件。例如事件 `workflow_run`、action `completed, failed`。

事件與 action 的推斷順序：

1. Body 中的字串 `event` 欄位；
2. `X-GitHub-Event` 標頭，搭配 Body 的 `action` 組成 `github.<event>.<action>`；
3. `X-Gitlab-Event` 標頭；
4. `X-Event-Type` 標頭；
5. Body 的 `event`、`type`、`action` 欄位；
6. 皆無時記錄為 `webhook.received`。

#### 保護 Webhook URL

> ⚠️ **注意：** URL 中的 Token 就是呼叫憑證。不要把完整 URL 放進公開 Repo、Issue 或截圖。外洩時立即按 **Rotate URL**（或 `multica autopilot trigger-rotate-url`）並更新發送端，舊 URL 立即失效。

只有 Autopilot 建立者、Workspace `owner`／`admin` 與被授權的協作者可檢視完整 URL；UI 預設隱藏 Token，複製時不需顯示。`multica autopilot get` 預設把 `webhook_token`、`webhook_path`、`webhook_url` 設為 `null`，只回傳 `has_webhook_token` 與 `webhook_token_hint`；確實需要時加 `--show-secrets`（警告會印到 stderr，管線 JSON 保持有效）。Trigger 若設定了簽章密鑰，請求缺少或不符的簽章會被拒絕（401）。

#### 回應碼參考

| HTTP | 狀態 | 意義 |
| --- | --- | --- |
| 200 | `accepted` | 已接受並建立 Run，回傳投遞與 Run ID |
| 200 | `skipped` | 已接受但此次略過（例如 Run only 時 Runtime 離線），附原因 |
| 200 | `ignored` | 未建立 Run：Trigger 停用、Autopilot 暫停或封存、事件被篩掉，`reason` 說明原因 |
| 200 | `duplicate` | 冪等鍵命中既有投遞，回傳原投遞 ID，不再執行 |
| 400 | 錯誤訊息 | Body 為空、不是有效 JSON 或不是物件／陣列 |
| 401 | `rejected` | 已設定簽章密鑰，但請求缺少簽章或簽章不符 |
| 404 | 錯誤訊息 | URL 中的 Token 無效或已輪替 |
| 413 | 錯誤訊息 | Body 超過 256 KiB |
| 429 | 錯誤訊息 | 請求過多，依 `Retry-After` 稍後重試 |
| 500 | 錯誤訊息 | Multica 內部錯誤，發送端可稍後重試 |

業務層的忽略（暫停、封存、事件篩選）一律回 200 而非 4xx，避免發送端無止境重試。

### 15.5 執行紀錄、重播與暫停

- **執行紀錄**顯示觸發來源、時間、狀態、連結的 Issue 或 Run，以及失敗或略過原因；Webhook Trigger 另有獨立的**投遞紀錄**（解析出的事件、回應、去重資訊、失敗原因）。
- 處理完成的 Webhook 投遞可從詳情頁**重播**：建立新的投遞與 Run，不改寫原紀錄；簽章驗證失敗或仍在排隊的投遞不能重播，重播不參與去重。
- **自動暫停：** 系統定期檢查，若過去 7 天至少 50 次完成或失敗的 Run 中失敗率達 90%，會暫停 Autopilot 並通知建立者；修正原因後需手動恢復。
- 手動暫停會停止排程、Webhook 與 **Run now**。刪除實際上是封存：之後的觸發停止，執行與投遞紀錄保留。

### 15.6 權限

| 角色 | 權限 |
| --- | --- |
| 任何 Workspace 成員 | 建立 Autopilot |
| 建立者、`owner`／`admin` | 編輯、執行、刪除、管理 Trigger；新增協作者 |
| 協作者 | 編輯、執行、管理 Trigger，但不能再授權他人 |

能管理 Autopilot **不代表**能執行其 Agent，Agent Access 仍然適用。排程與 Webhook 觸發的 Run 以**建立該 Trigger 的人**的權限執行（v0.4.39+）；無法確認建立者的舊 Trigger 會停止而不執行。

### 15.7 CLI

```bash
# 建立（--title、--agent、--mode 為必填）
multica autopilot create \
  --title "每日站立會議摘要" \
  --agent standup-bot \
  --mode create_issue \
  --description "彙整昨日已合併的 PR、狀態變更的 Issue 與阻礙，產出摘要。" \
  --issue-title-template "每日站立摘要 {{date}}" \
  --project <project-id> \
  --subscriber "Alice" --subscriber "Bob"

# 新增排程與 Webhook Trigger
multica autopilot trigger-add <autopilot-id> --kind schedule --cron "0 9 * * 1-5" --timezone Asia/Taipei
multica autopilot trigger-add <autopilot-id> --kind webhook --label "CI failures"
multica autopilot trigger-list <autopilot-id>
multica autopilot trigger-update <autopilot-id> <trigger-id> --enabled=false   # 停用單一 Trigger
multica autopilot trigger-rotate-url <autopilot-id> <trigger-id>

# 執行與查詢
multica autopilot trigger <autopilot-id>          # 手動執行一次
multica autopilot runs <autopilot-id>
multica autopilot get <autopilot-id> --output json
multica autopilot update <autopilot-id> --status paused
multica autopilot list
multica autopilot delete <autopilot-id>           # 實際為封存
```

> 💡 `--issue-title-template` 只會內插 `{{date}}`（UTC，YYYY-MM-DD），其他 `{{...}}` 在建立時即被拒絕。

另請注意指令與舊版的差異：

> 💡 **與舊版差異：** 舊版手冊的 `multica autopilot enable/disable` 在 v0.6.1 不存在；暫停／恢復整個 Autopilot 用 `autopilot update --status paused|active`，個別 Trigger 用 `trigger-update --enabled`。

### 15.8 企業應用範例

📘 **建議實務：**

| 情境 | 模式 | Trigger | Runbook 要點 |
| --- | --- | --- | --- |
| 每日站立摘要 | Create issue | `0 9 * * 1-5` Asia/Taipei | 彙整昨日合併 PR、`blocked` Issue、待審查項目，@ 相關負責人 |
| 每週依賴與 CVE 檢查 | Create issue | `0 8 * * 1` | 執行依賴掃描，有高風險 CVE 時建立子 Issue 並設優先序 `urgent` |
| CI 失敗初步分析 | Create issue | Webhook（GitHub `workflow_run` 的 `completed`，Payload 判斷失敗） | 讀取失敗 Job 日誌，定位可能原因，附重現步驟 |
| 監控告警分流 | Create issue | Webhook（Alertmanager／Grafana） | 依告警標籤判斷服務，查最近部署與錯誤日誌，提出處置建議，不得自行重啟服務 |
| 週報 | Run only | `0 18 * * 5` | 產出本週完成項目與風險摘要，發佈到通訊頻道 |
| 夜間文件同步 | Run only | `0 2 * * *` | 依當日合併的 API 變更更新文件 Repo 並開 PR |

> 💡 **實務建議：** Webhook 發送端務必帶穩定的 `Idempotency-Key`（例如 CI 的 run ID 加嘗試次數）；Runbook 要明確寫出「不可以做的事」（例如不可重啟正式服務、不可合併 PR），並把處理結果限制在留言與 PR。

---

## 第 16 章：通訊整合（Channels）

> **本章重點：** 五種通訊平台的比較；訊息處理流程、`/issue`、`/new`、`/clear` 指令；Session 隔離與帳號綁定；Slack、飛書／Lark、釘釘、企業微信、Telegram 的連接步驟；自架所需的加密金鑰與多副本注意事項；社群維護的支援邊界。

### 16.1 平台比較

通訊整合讓團隊不必開啟 Multica，就能在聊天工具中向 Agent 提問、在群組 @ 它，或直接建立 Issue。五個平台共用相同的 Session、身分與執行機制，只是安裝方式不同。

| | 飛書／Lark | Slack | 釘釘 | 企業微信 | Telegram |
| --- | --- | --- | --- | --- | --- |
| 安裝 | Multica 產生 QR Code，以飛書掃碼授權 | 在 Slack 建立 App，貼上兩個 Token | 建立企業內部應用與 Stream 模式機器人，貼上 AppKey／AppSecret | 管理後台建立啟用長連線的智慧機器人，貼上 Bot ID 與 Secret | 以 @BotFather 建立 Bot，貼上 Token |
| 私訊 Agent | 支援 | 支援 | 支援 | 支援 | 支援 |
| 群組／頻道 | @Bot 觸發 | @Bot 觸發 | @Bot 觸發 | @Bot 觸發 | @Bot 或回覆 Bot 觸發 |
| 建立 Issue | `/issue`（原文建立） | `/issue` 斜線指令（Agent 先撰寫描述再建立） | `/issue`（原文建立） | `/issue`（原文建立） | `/issue`（原文建立） |
| 新 Chat | `/new [訊息]` | 私訊 `/new`；頻道 `@Multica /new` | `/new` | `/new` | `/new` |
| 清除上下文 | `/clear [訊息]` | 私訊 `/clear`；頻道 `@Multica /clear` | `/clear` | `/clear` | `/clear` |
| 連線方式 | 平台長連線 | Socket Mode | Stream 模式 | 平台長連線 | `getUpdates` 長輪詢 |
| 維護 | 核心團隊 | 核心團隊 | **社群維護** | **社群維護** | **社群維護** |
| 加入版本 | 早期 | 早期（`/issue` v0.3.34） | v0.4.20 | v0.4.21 | v0.4.25 |

- **每個 Bot 綁定一個 Multica Agent**；同一平台要用多個 Agent，就為每個 Agent 連一個 Bot。
- 飛書：新連線目前**只開放中國大陸版飛書**；既有的國際版 Lark 連線仍可運作與管理。
- 所有連線方式都是**由 Multica 主動對外連線**（長連線／Socket Mode／Stream／長輪詢），不需要對公網開放 Webhook 入口。

### 16.2 訊息處理流程

```mermaid
flowchart TD
    M["平台訊息"] --> B["解析 Bot 對應的 Workspace 與 Agent"]
    B --> G{"群組／頻道訊息？"}
    G -->|"是"| MEN{"明確 @Bot？"}
    MEN -->|"否"| DROP["不觸發、不進入上下文"]
    MEN -->|"是"| AUTH
    G -->|"否（私訊）"| AUTH{"帳號已綁定且仍是 Workspace 成員？"}
    AUTH -->|"否"| LINK["送出帳號綁定連結"]
    AUTH -->|"是"| CHAT["加入 Agent Chat Session，建立 Run"]
    CHAT --> REPLY["回覆送回原私訊或討論串"]
```

`/issue` 是指令而非聊天回合：結果會回傳到來源平台，但指令本身不加入 Multica Chat。

| 指令 | 行為 |
| --- | --- |
| `/new [訊息]` | 建立新的 Multica Chat，之後此外部對話的訊息都路由到新 Chat；帶訊息時作為第一回合。舊 Chat 保留可用 |
| `/clear [訊息]` | 留在目前 Chat，但開始新的「Agent 可見上下文」；完整歷史仍在 Multica，Agent 看不到邊界之前的訊息 |
| `/issue <標題>` | 建立 Issue 並指派給 Bot 背後的 Agent；第一行為標題，其餘為描述（Slack 版由 Agent 撰寫標題與內文） |

Slack 的 `/new`、`/clear` 在私訊中是原生斜線指令；頻道討論串中請用 `@Multica /new [訊息]`，因為原生斜線指令的 Payload 無法識別討論串。

### 16.3 Session 隔離與帳號綁定

| 平台 | Session 劃分 |
| --- | --- |
| 飛書／Lark | 依聊天；話題群組中每個話題各自獨立（v0.3.41+） |
| Slack | 私訊依頻道；頻道中每個討論串各自一個 Session |
| 釘釘 | 依會話；每個私訊或群組各自延續 |
| 企業微信 | 依聊天 |
| Telegram | 依聊天；論壇話題（Forum Topic）各自獨立 |

頻道中的後續訊息仍需重新 @Bot；Agent 只收到指名給它的訊息，**不會自動讀取整個頻道歷史**（Telegram 有短暫緩衝的例外，見 16.8）。

**帳號綁定：** 成員第一次傳訊給 Bot 時會收到綁定連結（一次性，約 15 分鐘有效），登入 Multica 後平台帳號即連結到其在此 Workspace 的成員身分。完成綁定後才會執行 Agent；**每則訊息都重新檢查**綁定與成員資格，離開 Workspace 後就無法再透過 Bot 存取。綁定只確認發送者身分，不會自動把聊天平台上的其他人加入 Workspace。v0.6.0 起，發送者若無權執行該 Agent，通道會拒絕該回合。

**管理連線：** Workspace `owner`／`admin` 可連接或中斷 Bot（飛書 Bot 另允許 Agent 擁有者）；一般成員可檢視已連接的整合，並使用自己有權限的 Agent。中斷後 Bot 停止接收新訊息，既有對話與 Run 紀錄保留。集中管理頁：**Settings → Messaging**。

### 16.4 Slack

前置：由 Workspace `owner`／`admin` 完成，最後需要兩個憑證——`xoxb-` 開頭的 Bot User OAuth Token，以及 `xapp-` 開頭的 App-level Token。

**步驟 1：以 Manifest 建立 Slack App。** 在 [Slack API Apps](https://api.slack.com/apps) 選 **Create New App → From a manifest**，貼上：

```yaml
display_information:
  name: Multica
features:
  app_home:
    home_tab_enabled: false
    messages_tab_enabled: true
    messages_tab_read_only_enabled: false
  bot_user:
    display_name: Multica
    always_online: true
  slash_commands:
    - command: /issue
      description: Create a Multica issue
      usage_hint: "[description]"
    - command: /new
      description: Start a new Multica chat
      usage_hint: "[message]"
    - command: /clear
      description: Clear the current Multica chat context
      usage_hint: "[message]"
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - channels:history
      - files:read
      - groups:history
      - im:history
      - mpim:history
      - chat:write
      - reactions:write
      - users:read
      - commands
settings:
  event_subscriptions:
    bot_events:
      - app_mention
      - message.im
      - message.channels
      - message.groups
      - message.mpim
  interactivity:
    is_enabled: false
  org_deploy_enabled: false
  socket_mode_enabled: true
  token_rotation_enabled: false
```

可把兩處 `Multica` 換成 Agent 名稱；**不要刪減 scopes 或 events**。Slack 斜線指令名稱是 Workspace 全域的，若 `/new`、`/clear` 已被其他 App 占用，建立時會被拒絕。

**步驟 2：取得兩個 Token。** **Install App → Install to Workspace** 後複製 `xoxb-` Token；**Basic Information → App-Level Tokens → Generate Token and Scopes**，加入 `connections:write` 後複製 `xapp-` Token。

**步驟 3：連接 Agent。** Multica **Agents** → 選擇 Agent → **Integrations** → **Connect Slack**，貼上兩個 Token。Multica 會驗證兩者來自同一 App，成功後顯示 **Connected to Slack**。

使用方式：

| 情境 | 操作 |
| --- | --- |
| 私訊 | 從側欄 **Apps** 開啟 Bot 直接傳訊 |
| 頻道 | `/invite @your-bot` 後 `@your-bot 你的需求`；每個討論串一個 Session |
| 傳檔案 | 單檔 ≤ 20 MiB、每則最多 10 個；需 `files:read`（舊 App 加 scope 後要重新安裝） |
| 建 Issue | `/issue Safari 登入成功後仍停在登入頁`（不需 @，Agent 撰寫後建立，完成時 Inbox 通知） |

| 疑難 | 檢查 |
| --- | --- |
| 連接時 Token 無效 | 前綴是否正確、是否來自同一 App |
| App 無法驗證 | Manifest 含 `users:read`，更新權限後重新安裝 |
| 沒有私訊入口 | `app_home.messages_tab_enabled` 為 `true` |
| 頻道沒回應 | Bot 已被邀請且訊息有 @Bot |
| 斜線指令不存在 | Manifest 含三個指令與 `commands` scope 並重新安裝 |
| Bot 不執行 | Agent 是否已封存、其 Runtime 是否在線 |

### 16.5 飛書／Lark

由 Agent 擁有者或 Workspace `owner`／`admin` 連接：

1. **Agents** → 選擇 Agent → **Integrations** → **Bind to Feishu**；
2. 以飛書掃描 QR Code 並確認授權（QR Code 為一次性，有效一小時）；
3. 回到 Multica，顯示 **Connected to Feishu** 即完成。要改 Bot 名稱或權限，點 **Manage in Feishu**。

| 情境 | 操作 |
| --- | --- |
| 私訊 | 直接傳訊，連續訊息留在同一 Multica 對話 |
| 群組 | 把 Bot 加入群組後 `@Bot` 描述需求 |
| 建 Issue | `/issue 修正登入後的導向` 換行接描述（單獨 `/issue` 只回覆格式說明） |
| 媒體 | 圖片、影片、檔案與語音會以附件帶入（v0.4.12+、v0.4.29+） |

> ⚠️ **最常見問題：Bot 完全不回覆。** Multica 沒有 Webhook 端點，App 必須以**長連線**推送事件。請在飛書開發者後台 **Events & Callbacks → Event Configuration** 確認訂閱方式為「長連線」而非「請求網址」、已訂閱 `im.message.receive_v1`，且帶有此設定的 App 版本已發布（需審核的租戶要已核准）。設為請求網址的 App 仍可綁定、仍顯示 Connected，但什麼都收不到。

### 16.6 釘釘（DingTalk，社群維護）

1. 在 [釘釘開放平台](https://open-dev.dingtalk.com) 建立**企業內部應用**，啟用機器人並把**訊息接收模式**設為 **Stream 模式**；
2. 預設已有「機器人發送訊息」權限（`qyapi_robot_sendmsg`）；要在 Multica 顯示 Bot 名稱，手動加入「釘釘群組基本資訊管理」（`qyapi_chat_manage`）；
3. 在**憑證與基礎資訊**頁複製 **Client ID（AppKey）** 與 **Client Secret（AppSecret）**；
4. Multica **Agents → 你的 Agent → Capabilities → Integrations → Connect DingTalk**，填入 AppKey 與 AppSecret；
5. 私訊或在群組 @Bot 觸發帳號連結，於私訊中開啟約 15 分鐘有效的連結完成綁定。

| 功能 | 說明 |
| --- | --- |
| 圖片 | PNG、JPEG、GIF、WebP、BMP；每則最多 4 張、每張 ≤ 10 MB；檔案與語音暫不支援 |
| 引用回覆 | 以釘釘引用功能選訊息後輸入，引用內容會作為上下文附加（群組仍需 @Bot） |
| 處理回饋 | 收到訊息後加上 `RogerThat` 反應，完成並成功回覆後改為 `Done`，取消則移除 |
| 群組路由 | 一個 Bot 可在不同群組服務（v0.4.25+）；管理頁顯示 Bot 已處理過訊息的群組與活動狀態，90 天無訊息的群組歸入 **Long inactive** |
| 建 Issue | `/issue <標題>` 或 `/issue <標題>` 換行接詳細描述；同則圖片會成為附件 |

### 16.7 企業微信（WeCom，社群維護）

在企業微信管理後台建立**啟用長連線的智慧機器人**，把 **Bot ID** 與 **Secret** 貼到 Agent 的 **Integrations**。v0.4.21 起提供，之後陸續支援群組 @、照片／檔案／影片（v0.4.23+）、語音轉文字（v0.4.22+）、Agent 產出檔案回傳（v0.4.24+）、依讀者語言發送通知（v0.6.0+）。

> ⚠️ **多副本注意：** 企業微信智慧機器人唯一的對外路徑，是持有該 Bot 租約的副本所維持的行程內 WebSocket 長連線。
>
> - **有 `REDIS_URL`（sharded 或 dual relay 模式）：** 其他副本產生的回覆會經 relay 轉送給持有連線的副本，支援多副本；
> - **legacy relay 模式或沒有 Redis：** 其他副本產生的回覆會被丟棄，企業微信使用者看不到，**請以單一副本執行**。
>
> 不論哪種模式，在所有副本都正在重連的空窗期產生的回覆無法送達，但會被計入 `multica_wecom_outbound_dropped_total{reason="no_live_connection"}`，可量測。若無法接受重連期間偶發遺失，單一副本仍是最保守的部署。除錯時可暫時設定 `MULTICA_WECOM_TRACE=1`（會把訊息內容與附件檔名寫入日誌，結束後務必關閉）。

### 16.8 Telegram（社群維護）

1. 開啟 [@BotFather](https://t.me/BotFather) 傳送 `/newbot`，設定顯示名稱與以 `bot` 結尾的 username，複製 HTTP API Token；
2. 預設保持 **Group Privacy** 開啟（群組中只收到指令、明確 @ 與回覆 Bot 的訊息）；
3. Multica **Agents → Integrations → Connect Telegram**，貼上 Token。Multica 會驗證 Bot、確認沒有衝突的 Webhook、加密 Token，並啟動一條受監管的 `getUpdates` 連線。

| 功能 | 說明 |
| --- | --- |
| 私訊 | 直接傳文字，不需 @ |
| 群組 | @Bot 或回覆 Bot 的訊息；未指名的群組訊息不啟動對話，但最近 10 則（每群組／話題）會暫存在記憶體，在下次指名時作為唯讀上下文附加，伺服器重啟即清空 |
| 綁定連結 | 群組中不會公開貼出，會請發送者先私訊 Bot |
| 媒體（v0.5.3+） | 照片、檔案、影片、語音、音訊以附件送給 Agent（Bot 可下載上限 20 MB）；Agent 產出的檔案回傳（照片 ≤ 10 MB 內嵌、其他 ≤ 50 MB 為檔案）；**需要伺服器設定物件儲存**，否則回覆「不支援」 |
| 指令 | `/new`、`/clear`、`/issue <標題>`；群組支援 `/issue@your_bot` 形式 |

| 疑難 | 檢查 |
| --- | --- |
| Bot 無法驗證 | 先查伺服器連線與代理（Go 會讀 `HTTPS_PROXY`、`NO_PROXY`），Telegram 明確拒絕時才換 Token |
| Webhook 衝突 | 先移除 Bot 既有 Webhook（有 Webhook 時 Telegram 不允許 `getUpdates`） |
| 409 polling conflict | 另一個 Multica 實例或行程在輪詢同一 Bot；**每個環境請用不同 Bot** |

### 16.9 自架設定

自架部署必須先為每個平台設定 32 bytes 加密金鑰，Multica 才會開放連線入口：

```dotenv
MULTICA_LARK_SECRET_KEY=<base64-encoded 32-byte key>
MULTICA_SLACK_SECRET_KEY=<base64-encoded 32-byte key>
MULTICA_DINGTALK_SECRET_KEY=<base64-encoded 32-byte key>
MULTICA_WECOM_SECRET_KEY=<base64-encoded 32-byte key>
MULTICA_TELEGRAM_SECRET_KEY=<base64-encoded 32-byte key>
```

```bash
openssl rand -base64 32
```

| 注意事項 | 說明 |
| --- | --- |
| 金鑰長期保存 | 輪替或遺失後既有 Bot 憑證無法解密，必須重新連接 |
| 綁定連結網址 | 使用 `MULTICA_APP_URL`（未設定時退回 `FRONTEND_ORIGIN`），必須是成員可到達的 Multica 位址 |
| 對外連線 | API 伺服器必須能連到各平台 API（例如 `api.telegram.org`），企業代理需放行 |
| Compose 傳遞 | 官方 `docker-compose.selfhost.yml` 已傳遞這些變數；自訂 Compose 檔時記得加入 |

### 16.10 社群維護的支援邊界

釘釘、企業微信與 Telegram 由志願者貢獻並維護：

| 承諾 | 不承諾 |
| --- | --- |
| 每個版本都隨附；核心團隊在共用層重構時維持其可編譯與測試通過；把該領域的 Issue 轉給維護者 | 核心團隊日常不使用這些平台，無法對真實平台驗證行為；需要真實平台存取的 Bug 依志願者時間處理，**沒有回應時間保證** |

若某領域壞掉且數個版本都無人修復，官方可能將其棄用。回報問題請到 [GitHub Issues](https://github.com/multica-ai/multica/issues) 並填寫 **Area** 欄位，不要直接私訊或 @ 維護者。

> 📘 **建議實務：** 對 SLA 有要求的企業流程，優先選擇核心團隊維護的 Slack 或飛書；使用社群維護平台時，在內部建立回退方案（例如通知改走 Email／Inbox），並在升級前於測試環境驗證 Bot 行為。

---

## 第 17 章：GitHub、自架 Git 與 CI/CD 整合

> **本章重點：** GitHub 整合的能力範圍與連接步驟；功能開關；PR 自動連結規則；PR 卡片；PR 合併後自動移動 Issue 的條件；多 Workspace；自架 GitHub App；Forgejo／Gitea／GitLab 整合；Agent 如何開 PR；與 CI/CD 管線的整合模式與分支策略。

### 17.1 整合能力範圍

連接 GitHub 後，Multica 會依 Issue 編號自動連結 Pull Request，並在 Issue 詳情中顯示 PR 狀態、變更規模、CI 結果與合併衝突。

> 💡 **關鍵觀念：** GitHub 整合**只讀取**安裝時授權的 Repo，**永遠不會推送 commit、留言或 status check**。Agent 開 PR 用的是 Runtime 主機自己的 Git 憑證（見 17.7）。

自架 Multica 另可同時連接自架的 Forgejo、Gitea 或 GitLab，提供相同的 PR 自動連結、合併驅動狀態變更與 CI 顯示（v0.4.10+）；Multica Cloud 不提供此入口。

### 17.2 連接 GitHub 與功能開關

由 Workspace `owner`／`admin` 完成：

1. 開啟 **Settings → Code**；
2. 在 **GitHub** 列點 **Connect GitHub**；
3. 在 GitHub 選擇帳號或組織，授權全部或部分 Repo；
4. 完成安裝後回到 Multica。

> 💡 **GitHub 連線**決定 Multica 從哪些 Repo 接收 PR 事件；**Code repositories** 設定決定 Agent 開始 Run 時可選哪些 Repo。兩者用途不同、分別設定。連接後同頁的 **Pick from GitHub** 可直接匯入 App 已授權的多個 Repo（v0.4.13+，需 `GITHUB_APP_ID` 與私鑰）。

**Settings → Code → Pull requests & issues** 的開關：

| 開關 | 效果 |
| --- | --- |
| PR sidebar | 在 Issue 詳情顯示連結的 PR |
| Co-authored-by | 在 Agent 建立的 commit 加上 `Co-authored-by: multica-agent <github@multica.ai>` |
| Auto-link PRs | 依分支名稱、標題或內文的關閉關鍵字自動連結 |
| After PRs merge, move the issue to | 所有連結 PR 合併後要移到哪個狀態（預設 `Done`），或不變更 |
| PR card → CI & mergeability | 以 GitHub API 快照把 CI 狀態與可合併性顯示在卡片上 |

GitHub 列 **⋯** 選單的 **Pause GitHub features** 可暫停上述三個功能而不中斷 GitHub App 連線。

### 17.3 PR 連結與合併規則

**自動連結：** 把 Issue 編號放在分支名稱或 PR 標題最簡單：

```text
mul-123-fix-login-redirect
MUL-123 Fix the redirect after login
```

不分大小寫、只比對目前 Workspace 的前綴；一個 PR 可連結多個 Issue。編號只出現在 PR 內文時，必須緊接在關閉關鍵字之後：

```text
Closes MUL-123
Fixes MUL-123
Resolves MUL-123
```

內文中單純提到（如 `Related to MUL-123`）**不會**連結；commit 訊息與 PR 留言也不會觸發。也可手動連結：在 Issue 的 **Pull requests** 區塊點 **+** 貼上 PR URL；從列的 **⋯** 選 **Remove from issue** 可移除，之後 Multica 不會再依標題或分支自動連結它。

**PR 卡片顯示：** Repo、編號、標題、作者；`Open`／`Draft`／`Merged`／`Closed`；增刪行數與變更檔案數；CI 狀態（全部通過含數量、部分失敗並列出失敗檢查、部分進行中；沒有設定檢查的 PR 不顯示——「沒有檢查」永遠不算通過）；可合併性（mergeable、conflicting、blocked、behind）。GitHub 暫時不可用時保留最後快照並標示 stale。

**合併後移動 Issue：** 符合以下全部條件時，Issue 移到 Workspace 選定的狀態：

1. **所有**連結的 PR 都是 `Merged`——`Open` 或 `Draft` 的 PR 會讓 Issue 繼續等待，未合併就關閉的 PR 也會，直到你把它從 Issue 移除；
2. Issue 不是 `done` 或 `cancelled`、不在 Triage、尚未處於目標狀態，且沒有對此 Issue 關閉此行為（**Pull requests → ⋯ → Keep status when PRs merge**）。

連結方式（標題、分支、`Closes`）不影響合併後的行為。檢查在 PR 事件觸及 Issue 時進行（PR 合併、連結或移除連結）；重新開啟 Issue 不會讓它移回去，變更設定也不會回溯移動先前已合併的 Issue。狀態變更以系統動作寫入時間軸並通知訂閱者。PR 列表下方會有一行說明接下來會發生什麼（例如「Moves to Done when #19 merges」）。

> 💡 **實務建議：** 當 PR 只交付 Issue 的一部分，或合併後還需要發版、驗證時，從該 Issue 的 **Pull requests** 選單設定 **Keep status when PRs merge**；或把目標狀態設為自訂的「待回歸」狀態，而不是直接 `Done`。

### 17.4 多 Workspace

同一個 GitHub App 安裝可接多個 Multica Workspace（v0.4.0+），事件分別流入各 Workspace，並以各自的 Issue 前綴比對。例如同時引用 `MUL-1` 與 `ENG-2` 的 PR 可在兩個前綴不同的 Workspace 各自連結，彼此看不到對方的 Issue。若同一編號同時命中多個 Workspace（前綴相同時可能發生），Multica **不會在任何一個 Workspace 自動連結**，請手動連結。

**中斷連線：** **Settings → Code** 的 GitHub 列 **⋯ → Disconnect** 只移除此 Workspace 與安裝的關係，不會替你在 GitHub 解除安裝 App；既有 PR 紀錄保留，新事件停止流入。要撤銷 Repo 授權，請到 GitHub 的 App 安裝頁解除安裝或調整範圍（會影響所有連結此安裝的 Workspace）。

### 17.5 自架：建立自己的 GitHub App

在 GitHub **Developer settings → GitHub Apps** 建立：

| 欄位 | 值 |
| --- | --- |
| Homepage URL | Multica 前端位址，例 `https://multica.example.com` |
| Callback URL | 留空 |
| Setup URL | `https://<api-host>/api/github/setup`，並勾選 **Redirect on update** |
| Webhook URL | `https://<api-host>/api/webhooks/github` |
| Webhook secret | 長期保存的隨機字串 |

| Repository 權限 | 等級 | 用途 |
| --- | --- | --- |
| Metadata | Read-only | 基本 |
| Contents | Read-only | **必要**：PR 快照查詢讀取 head commit、可合併性與 CI rollup |
| Pull requests | Read-only | PR 事件 |
| Checks | Read-only | CI 狀態 |
| Commit statuses | Read-only | 彙整舊式 status CI |

訂閱事件：**Pull request**；以及 **Check suite**、**Check run**、**Status**（觸發 CI 與可合併性更新）。不需要顯示 CI 可省略 Checks、Commit statuses 與對應事件，但 Contents 仍必要。

```dotenv
GITHUB_APP_SLUG=multica-acme                 # 取自 https://github.com/apps/multica-acme
GITHUB_WEBHOOK_SECRET=<建立 App 時填的 Webhook secret>
FRONTEND_ORIGIN=https://multica.example.com
GITHUB_APP_ID=<App 的數字 ID>
GITHUB_APP_PRIVATE_KEY=<完整 PEM，保留 BEGIN/END 與換行>
```

缺少 `GITHUB_APP_SLUG` 或 `GITHUB_WEBHOOK_SECRET` 時連接按鈕停用、Webhook 端點拒絕處理事件；缺少 `GITHUB_APP_ID` 與私鑰時優雅降級——PR 仍會鏡像、自動連結與合併移動，只是卡片不顯示 CI 與合併狀態。升級既有部署時先跑一般 Migration，重啟 API 後在 **Settings → Code** 完成連接。

| 疑難 | 檢查 |
| --- | --- |
| 連接按鈕停用 | `GITHUB_APP_SLUG`、`GITHUB_WEBHOOK_SECRET` 是否傳到 API 行程 |
| Webhook 回 401 | 兩端是否用同一個 **Webhook secret**（不是 OAuth Client secret），再從 GitHub **Recent Deliveries** 重送 |
| PR 未連結 | Repo 是否在授權範圍、Auto-link 是否開啟、編號是否屬於此 Workspace、是否曾被手動移除 |
| 沒有 CI 狀態 | App ID 與私鑰是否設定、Contents／Checks／Commit statuses 權限與事件；已安裝的 App 新增權限後，各安裝的擁有者須在 GitHub 核准 |

### 17.6 自架 Git：Forgejo、Gitea、GitLab

> ⚠️ **僅限自架 Multica。** 需由維運者設定 `MULTICA_VCS_INTEGRATION_ENABLED=true`（官方 Compose 已預設）與 `MULTICA_VCS_SECRET_KEY`（`openssl rand -base64 32`，`make selfhost` 首次會自動產生），否則 **Settings → Code** 不會出現此區塊。另設定 `MULTICA_PUBLIC_URL`，UI 才能顯示可直接貼上的完整 Webhook URL。

這些供應商沒有「App」模型：每個 Workspace 儲存自己的實例 URL 與 Access Token，並在 Repo 或組織註冊 Webhook；Token 與 Webhook secret 都加密儲存。可與 GitHub 任意組合並用。

**連接 Workspace：**

1. 在供應商建立對要鏡像的 Repo 有讀取權的 Token：Forgejo／Gitea 於 **Settings → Applications**；GitLab 用具 `read_api` scope 的個人／群組／專案 Access Token；
2. Multica **Settings → Code** → **Self-hosted Git** 列 → **Connect**；
3. 選擇供應商、輸入實例 URL（例 `https://gitlab.example.com`）與 Token，Multica 會先向實例驗證；
4. 複製畫面上的 **Webhook URL** 與 **Webhook secret**（**secret 只顯示一次**；重新連接同一實例會輪替 Token 與 secret）。

**註冊 Webhook：**

| 供應商 | 設定 |
| --- | --- |
| Forgejo／Gitea | Settings → Webhooks → Add Webhook：Target URL、`POST`、`application/json`、Secret（驗證 `X-Gitea-Signature` HMAC）；事件選 **Pull Request** 與 **Commit Status** |
| GitLab | Settings → Webhooks：URL、Secret token（以 `X-Gitlab-Token` 逐字比對）；觸發選 **Merge request events** 與 **Pipeline events** |

**鏡像內容：** PR／MR 的開啟、關閉、合併、草稿狀態、作者、分支與差異統計；Issue 連結規則與 GitHub 相同（跨 GitHub 與自架供應商一起判斷「全部合併」）；Forgejo／Gitea commit status 與 GitLab pipeline 彙整為 head commit 的檢查列。

若連接時出現「憑證由此伺服器不信任的 CA 簽發」，請把內部 CA 加入後端信任庫（第 5.8 節）。**Multica 沒有跳過憑證驗證的選項**，因為連接請求會帶著你的 Access Token。

### 17.7 Agent 如何開 PR

建立 PR 不需要在 Multica 設定任何供應商憑證。Agent 在 Runtime 上 checkout Repo，**使用 Runtime 主機自己的 Git 憑證**推送分支並開 PR。要讓 Agent 能操作某個供應商，請確保 Daemon 主機能向它驗證，例如：

- SSH Deploy Key（建議每個 Repo 一把、權限最小）；
- Git credential helper 中的 Token；
- 主機上已登入的 `gh`／`glab` CLI（Run 會繼承 Daemon 使用者的 `HOME`，因此這些 CLI 在 Run 內與在 Shell 中行為相同）。

> 📘 **建議實務：** Runner 主機使用**機器帳號**（例如 GitHub 的 `multica-bot`）的 Fine-grained Token，只授予目標 Repo 的 `contents:write` 與 `pull_requests:write`；以 Branch Protection 要求 PR 審查與 CI 通過，讓 Agent 無法直接推送 `main`。

### 17.8 CI/CD 整合模式

```mermaid
sequenceDiagram
    autonumber
    participant PM as 需求方
    participant MC as Multica
    participant AG as Agent（Runtime）
    participant GH as GitHub
    participant CI as CI Pipeline
    participant RV as 人類 Reviewer
    PM->>MC: 建立 Issue（MUL-123）並指派 Agent
    MC->>AG: 建立 Run
    AG->>AG: 實作與本機測試
    AG->>GH: 推送分支 mul-123-xxx 並開 PR
    AG->>MC: 留言摘要，狀態設為 in_review
    GH->>CI: 觸發 CI
    GH-->>MC: PR 與 Checks 事件（PR 卡片更新）
    CI-->>GH: 檢查結果
    RV->>GH: Code Review 並合併
    GH-->>MC: PR merged 事件
    MC->>MC: 所有連結 PR 已合併，Issue 移到 Done
```

| 模式 | 做法 |
| --- | --- |
| **PR 驅動結案** | 分支或標題帶 Issue 編號 → CI → 人類合併 → Multica 自動把 Issue 移到 `Done` |
| **CI 失敗回饋** | GitHub Actions 失敗時以 Webhook 觸發 Autopilot（Create issue 模式），由 Agent 分析失敗原因（第 15.8 節） |
| **等待 CI 再處理** | Agent 開 PR 後建立 Wakeup：`--until-pr checks`，檢查完成時再被喚醒修正失敗（第 13.8 節） |
| **PR Review Agent** | 新 commit 推送時 Review Agent 會重新執行，而非沿用舊 commit 的結論（v0.3.36+） |

範例：GitHub Actions 在 CI 失敗時呼叫 Autopilot Webhook（Webhook URL 存在 Repository Secret）：

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '21'
          cache: maven
      - run: ./mvnw -B verify

  notify-multica:
    needs: build
    if: failure()
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Multica autopilot
        env:
          MULTICA_WEBHOOK_URL: ${{ secrets.MULTICA_CI_WEBHOOK_URL }}
        run: |
          curl -fsS -X POST "$MULTICA_WEBHOOK_URL" \
            -H "Content-Type: application/json" \
            -H "Idempotency-Key: ${{ github.run_id }}-${{ github.run_attempt }}" \
            -d "{\"event\":\"ci.failed\",\"eventPayload\":{\"repo\":\"${{ github.repository }}\",\"ref\":\"${{ github.ref_name }}\",\"run_url\":\"${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}\"}}"
```

> 📘 **建議實務：分支策略。** Agent 適合「短命分支 + PR」：建議採 Trunk-Based Development，Agent 從 `main` 開分支並以 PR 合回；若團隊使用 Git Flow，請在 Project 描述或 Agent Instructions 中明確寫「從 `develop` 建立 feature 分支、PR 目標為 `develop`」，並以 Project Resource 的 `ref` 指定起始分支（v0.5.1+）。

---

## 第 18 章：Desktop 與 Mobile App

> **本章重點：** Desktop 與 Web 的差異；三平台安裝；每個 Workspace 的分頁；內建 Daemon 與專屬 Profile；自動更新；連接自架實例的 `desktop.json`；Windows Defender 誤判處理；iOS 從原始碼建置、7 天簽章限制與連接自架實例。

### 18.1 Desktop 與 Web

| | Web | Desktop |
| --- | --- | --- |
| 開啟方式 | 瀏覽器 | 安裝桌面 App（macOS／Windows／Linux） |
| Workspace 分頁 | 使用瀏覽器分頁 | 每個 Workspace 各有一組分頁 |
| Daemon | 需另外安裝並啟動 CLI | 登入後由 App 自動啟動 |
| 新增本機目錄資源 | 不支援 | 支援（第 9.9 節） |
| 更新 | 重新整理頁面 | App 內更新 |

兩者可同時登入；只要連到同一個 Multica 服務，資料完全共享。Web 適合快速查看或共用電腦。

### 18.2 安裝

從 [multica.ai/download](https://multica.ai/download) 選擇對應作業系統與 CPU 架構的安裝檔：

| 平台 | 安裝檔（v0.6.1 Release 資產） |
| --- | --- |
| macOS | `.dmg`（Apple Silicon `arm64` 與 Intel `x64`；v0.4.2 起支援 Intel） |
| Windows | `.exe`（`x64` 與 `arm64`） |
| Linux | `.AppImage`、`.deb`、`.rpm`（`x86_64`／`amd64` 與 `arm64`／`aarch64`；套件名稱 `multica-desktop`） |

安裝後以與 Web 相同的 Email 登入。登入後 Desktop 會啟動其**內建的 Multica CLI**，並偵測本機已安裝的 AI 工具。

> 💡 Desktop 內建的 CLI 只服務 App 自己管理的 Runtime。若也要在終端機使用 `multica issue` 等指令，請另外安裝 CLI（第 19.1 節）。

### 18.3 分頁與操作

- 分頁依 Workspace 儲存：在 A 開三個 Issue、切到 B 看到的是 B 的分頁，切回 A 三個分頁仍在；
- 同一資源在目前 Workspace 只開一次；分頁可排序、釘選、關閉，各自保有前進／後退歷史與捲動位置；
- 點擊或貼上此部署的 App 連結會直接在分頁開啟，不跳到瀏覽器；
- 可把任一 Issue 開在獨立視窗（v0.4.3+）；`Cmd/Ctrl+,` 在新分頁開啟設定；數字快速鍵切換分頁（v0.4.39+）；可自訂快速鍵並錄製瀏覽器通常保留的組合（v0.4.0+）；
- 登出會清除這台機器上儲存的所有分頁，下一位登入者不會看到前一個帳號留下的頁面。

### 18.4 內建 Daemon

登入後 Desktop 會為目前的 Multica 服務建立專屬 CLI Profile 並以它啟動 Daemon：

```text
~/.multica/profiles/desktop-<host>/
```

它**永遠不會讀取或覆寫**你在終端機使用的預設 Profile；若你另外手動啟動 Daemon，Multica 會顯示為不同的 Runtime。可在 Desktop 設定中檢視 Runtime 狀態與日誌；Daemon 意外停止時 Desktop 會自動拉起（v0.4.37+）。

> 💡 **macOS 權限：** Desktop 內建 CLI 以 Developer ID 簽章，macOS 隱私權限（TCC）授權在升級後仍有效；Homebrew 安裝的 CLI 沒有穩定簽章，每次升級後可能需重新授權（第 21.7 節）。

### 18.5 更新

自動更新預設開啟：App 在背景檢查並下載新版本，下載完成後可立即重啟安裝，或在下次結束時安裝；可在 **Settings → Updates** 關閉自動檢查或手動檢查。

| 規則 | 說明 |
| --- | --- |
| 更新來源 | Windows arm64 與 macOS x64（Intel）各有獨立更新來源，其他架構使用預設來源，App 自動判斷 |
| Linux | 只有 `.AppImage` 支援自動更新；`.deb`／`.rpm` 請以新套件覆蓋安裝 |
| 失敗時 | 從下載頁以對應安裝檔覆蓋安裝 |

### 18.6 連接自架實例：`desktop.json`

Desktop 預設連 Multica Cloud。要連自架實例，在家目錄的 `.multica` 目錄建立 `desktop.json`：

| 平台 | 路徑 |
| --- | --- |
| macOS | `/Users/<you>/.multica/desktop.json` |
| Linux | `/home/<you>/.multica/desktop.json` |
| Windows | `C:\Users\<you>\.multica\desktop.json` |

```json
{
  "schemaVersion": 1,
  "apiUrl": "https://api.example.com"
}
```

> ⚠️ **注意：** 這**不是** CLI 的 `~/.multica/config.json`，鍵名也不同：CLI 用 `server_url`，Desktop 用 `apiUrl`。Desktop 從不讀 CLI 設定，修改 `config.json` 不會改變 Desktop 連線的伺服器。

`apiUrl` 為後端公開位址（必填，`http` 或 `https`）。另兩個網址可省略，Desktop 會自動推導：

| 鍵 | 推導規則 | 需要明確設定的情況 |
| --- | --- | --- |
| `wsUrl` | 把 `apiUrl` 的協定換成 `ws`／`wss` 並在路徑加 `/ws` | WebSocket 獨立部署 |
| `appUrl` | 主機以 `api.` 開頭且至少三段時去掉 `api.`（`api.example.com` → `example.com`），否則同 `apiUrl` | Web 與 API 在不同網域；兩段主機（如 `api.local`） |

```json
{
  "schemaVersion": 1,
  "apiUrl": "https://api.example.com",
  "appUrl": "https://app.example.com",
  "wsUrl": "wss://ws.example.com/socket"
}
```

儲存後**重啟 Desktop**（只在啟動時讀取一次）。判斷失敗原因：

| 現象 | 原因 |
| --- | --- |
| 仍顯示 Cloud 位址、沒有錯誤 | **找不到檔案**（目錄錯誤，或檔名不是完全的 `desktop.json`） |
| 顯示設定錯誤、不退回 Cloud | 找到檔案但 JSON、版本或 URL 無效 |

刪除檔案並重啟即回到 Cloud。Desktop 只能連到瀏覽器與執行電腦都可達的位址；遠端自架實例若沒有 HTTPS 或沒有代理 WebSocket，Desktop 無法建立連線。

**Windows 建立檔案的正確方式**（避免記事本加上 `.txt`、PowerShell 重導向寫成 UTF-16 或 BOM）：

```powershell
$dir = "$env:USERPROFILE\.multica"
New-Item -ItemType Directory -Force $dir | Out-Null
$json = @'
{
  "schemaVersion": 1,
  "apiUrl": "https://api.example.com"
}
'@
[System.IO.File]::WriteAllText("$dir\desktop.json", $json)
Get-ChildItem "$env:USERPROFILE\.multica" -Filter "desktop.json*"
```

### 18.7 Windows Defender 誤判

**症狀：** Windows 安全性回報 `Trojan:Script/Wacatac.B!ml` 等威脅並隔離 Desktop 安裝目錄中的檔案，通常是內建 CLI：

```text
C:\Users\<you>\AppData\Local\Programs\@multicadesktop\resources\app.asar.unpacked\resources\bin\multica.exe
```

這是**誤判**：`!ml` 代表判定來自 Defender 的機器學習啟發式而非惡意程式簽章。Multica 的 Windows 版本尚未以 Authenticode 簽章，新發布、會啟動背景行程並開網路連線的未簽章執行檔，正是這類啟發式評分偏高的樣貌；所有 Windows 產物都由 GitHub Actions 從公開原始碼建置。

**自行驗證：**

```powershell
Get-FileHash .\multica-cli-<version>-windows-amd64.zip -Algorithm SHA256
```

與 [最新 Release](https://github.com/multica-ai/multica/releases/latest) 的 `checksums.txt` 比對。

**處理：**

1. 還原隔離檔：Windows 安全性 → 病毒與威脅防護 → 保護歷程記錄 → 選取 Multica 項目 → 還原；
2. 新增**資料夾**排除項目，兩個都要加：`%LOCALAPPDATA%\Programs\@multicadesktop` 與 `%APPDATA%\Multica`（內建 CLI 遺失時 Desktop 會下載替代品到 `%APPDATA%\Multica\bin`，只排除安裝目錄會陷入替代品也被隔離的循環）；
3. 到 [Microsoft Security Intelligence](https://www.microsoft.com/en-us/wdsi/filesubmission) 以「Software developer → Incorrectly detected as malware」回報誤判。

> ⚠️ **注意：** 只有在你從官方下載頁或 GitHub Releases 安裝、且雜湊比對相符時才加入排除項目——排除項目會關閉該資料夾內所有檔案的即時防護。企業環境應由端點防護團隊統一以雜湊或路徑白名單處理，而非讓使用者各自設定。

### 18.8 iOS App（iPhone／iPad）

Multica iOS 用戶端**尚未上架 App Store**，需在 Mac 上從公開原始碼建置 Release 版並安裝到自己的裝置；**目前沒有 Android 用戶端**。安裝後預設連 Multica Cloud，Workspace、Issue、留言與 Run 紀錄都存在伺服器，不需手動同步。v0.4.37 起原生支援 iPad 任意方向；v0.5.3 起可選簡體中文、英文或系統語言。

**前置條件：** 安裝 Xcode 的 Mac；在 **Xcode → Settings → Accounts** 登入 Apple ID；以 USB 連接的 iPhone 並在 **設定 → 隱私權與安全性** 開啟開發者模式；Node.js、pnpm、Git。

```bash
git clone https://github.com/multica-ai/multica.git
cd multica
pnpm install
pnpm ios:mobile:device:prod:release
```

此指令建置不依賴 Metro 的 Release 版並安裝到連接的 iPhone；裝置若阻擋開啟，到 **設定 → 一般 → VPN 與裝置管理** 信任開發者憑證。

| 主題 | 說明 |
| --- | --- |
| 免費簽章 7 天限制 | 以免費 Apple ID 簽章的 App 只能使用 7 天，到期後重新連接 Mac 執行同一建置指令重新簽章；Apple Developer Program 帳號簽章效期較長並可用 TestFlight |
| 簽章失敗 | 出現 `No matching provisioning profiles found` 時，`export EXPO_BUNDLE_IDENTIFIER_PROD=com.yourname.multica` 後重建 |
| 更新 | 不會自動更新：`git pull --ff-only` → `pnpm install` → 重新執行建置指令 |
| 連接自架 | 複製 `apps/mobile/.env.production.example` 為 `apps/mobile/.env.production.local`，設定 `EXPO_PUBLIC_API_URL`（必填）與 `EXPO_PUBLIC_WEB_URL` 後重建；`.local` 已被 gitignore |

```dotenv
EXPO_PUBLIC_API_URL=https://api.example.com
EXPO_PUBLIC_WEB_URL=https://app.example.com
```

> ⚠️ **注意：** 不要直接修改已提交的 `apps/mobile/.env.production`；使用 LAN 位址時不要寫 `localhost`（在 iPhone 上指的是手機本身）。兩個鍵都要設定，省略的鍵會退回 multica.ai 預設值。

企業內部發行的考量：

> 📘 **建議實務：** 企業若需要內部發行 iOS App，應以 Apple Developer Enterprise／Business 帳號統一簽章並透過 MDM 發佈，同時留意授權條件 1(b)：不得移除或修改 UI 上的 Multica 品牌與版權資訊。

此外，Web 版可「加入主畫面」以類 App 方式開啟（v0.4.27+），可作為暫時的行動端替代方案（包括 Android 使用者）。

---

## 第 19 章：CLI 完整參考

> **本章重點：** 安裝與更新 CLI；首次連線；Workspace 選擇；ID 與輸出格式；Profile 與多環境；指令分組總覽（Core／Runtime／Additional）；Agent Task 內的 CLI 行為；從 Claude Code／Codex／Cursor 驅動 Multica。

v0.6.1 CLI 共有 **21 個頂層指令，連同各層子指令共 204 個指令**（以 `--help` 遞迴列舉）。本章涵蓋常用路徑，完整速查見[附錄 B](#附錄-bcli-快速參考卡)；實際可用旗標一律以 `multica <command> --help` 為準。

### 19.1 安裝與更新

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
# 或 Homebrew
brew install multica-ai/tap/multica
```

```powershell
# Windows PowerShell
irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex
```

```bash
multica version                    # multica 0.6.1 (commit: 2ea01ae4e, built: ...)
multica version --output json
multica update                     # 更新到最新版（--download-timeout 預設 2m）
```

GitHub Release 也提供各平台 CLI 壓縮檔（`multica-cli-<version>-<os>-<arch>`）與 `checksums.txt`，離線或受控環境可自行下載驗證後部署。

> 💡 **自動更新：** 連 Cloud 的 Daemon 預設自動更新；自架預設關閉（`MULTICA_DAEMON_AUTO_UPDATE`）。v0.5.1 起自架 Multica 可指向 Gitea 或相容鏡像取得更新。企業環境建議關閉自動更新，以 `multica runtime update <runtime-id> --target-version <version>` 由平台團隊統一推送。

### 19.2 首次連線與登入

```bash
multica setup                              # 連 Multica Cloud（等同 setup cloud）
multica setup self-host \
  --server-url https://api.example.com \
  --app-url https://app.example.com        # 連自架實例
multica auth status
multica daemon status
```

`setup` 儲存伺服器位址、開啟瀏覽器完成登入、啟動 Daemon。只需重新登入、不想覆寫其他設定時用 `multica login`；無瀏覽器的機器先在 Web 建立 PAT，再用 `multica login --token`（互動提示貼上，不留在 Shell 歷史）。透過 SSH 在遠端機器安裝時，CLI 會引導較簡單的登入方式（v0.4.0+）。

### 19.3 Workspace 選擇

```bash
multica workspace list
multica workspace switch <slug>
multica issue list --workspace-id <id>     # 單一指令覆寫
export MULTICA_WORKSPACE_ID=<id>           # 環境變數覆寫
```

### 19.4 Profile 與多環境

預設設定位於 `~/.multica/config.json`。`--profile <name>` 可隔離另一組伺服器位址、Token、預設 Workspace 與 Daemon 狀態：

```bash
multica setup self-host --profile staging \
  --server-url https://api.staging.example.com \
  --app-url https://app.staging.example.com

multica issue list --profile staging
multica config show --profile staging
multica daemon status --profile staging
```

| 項目 | 預設 Profile | 具名 Profile |
| --- | --- | --- |
| 設定檔 | `~/.multica/config.json` | `~/.multica/profiles/<name>/config.json` |
| Daemon 日誌 | `~/.multica/daemon.log`、`daemon.err.log` | `~/.multica/profiles/<name>/` 下對應檔案 |
| 工作目錄 | `~/multica_workspaces` | Profile 相關路徑 |
| Desktop | — | `~/.multica/profiles/desktop-<host>/` |

### 19.5 ID 與輸出格式

| 規則 | 說明 |
| --- | --- |
| Issue ID | 使用 `MUL-123` 這類 key 或完整 UUID；**不接受**短 UUID 前綴 |
| 其他資源 | `list` 通常印出可複製的短 ID，`--full-id` 顯示完整 UUID；短 ID 有歧義時 CLI 會要求更多字元 |
| 短 Run ID | 需要搭配 `--issue` 指定所屬 Issue |
| 預設輸出 | `list` 預設 table，`get`／`create` 多數預設 JSON |
| 腳本 | 請用 `--output json`，不要解析終端機表格；`issue list --fields id,title,status` 可縮小 JSON（v0.4.41+） |
| 分頁 | `issue list --limit`（1–100，預設 50）搭配 `--offset`；JSON 輸出的 `has_more` 表示還有資料 |
| 全域旗標 | `--server-url`、`--workspace-id`、`--profile`、`--debug`（印完整錯誤，或 `MULTICA_DEBUG`） |

### 19.6 指令總覽

| 分組 | 指令 | 用途 |
| --- | --- | --- |
| Core | `issue` | 建立、更新、指派、搜尋 Issue；評論、訂閱者、標籤、屬性、Metadata、Run、Wakeup |
| | `project` | Project 與其 Resources |
| | `label`、`property` | Workspace 標籤與自訂屬性 |
| | `agent`、`skill`、`squad` | Agent、Skill、Squad |
| | `autopilot` | 自動化、Trigger 與執行紀錄 |
| | `workspace` | 建立、檢視、切換 Workspace，邀請成員，MCP 函式庫 |
| | `repo` | Workspace Repo 清單與本機 checkout |
| | `chat` | 讀取 Agent 正在處理的**外部通道**對話（主要給通訊整合中的 Agent 使用） |
| Runtime | `daemon`、`runtime` | 啟停本機 Daemon；檢視與管理 Runtime、自訂 Profile |
| Additional | `attachment` | 上傳／下載附件 |
| | `user profile` | 檢視或更新目前使用者資料 |
| | `auth`、`login`、`setup` | 登入、驗證狀態、初始化連線 |
| | `config` | 目前 Profile 的本機設定 |
| | `update`、`version` | 更新 CLI、列印版本 |

#### Core：Issue

| 子指令 | 用途 | 重點旗標 |
| --- | --- | --- |
| `list` | 列出 Issue | `--status`、`--priority`、`--assignee`／`--assignee-id`、`--project`、`--metadata k=v`、`--property "Name=Value"`、`--sort`、`--direction`、`--fields`、`--resolve-properties` |
| `get <id>` | 單一 Issue | `--resolve-properties` |
| `create` | 建立 | `--title`（必填）、`--description`／`-stdin`／`-file`、`--status`、`--priority`、`--assignee`、`--parent`、`--stage`、`--project`、`--start-date`、`--due-date`、`--attachment`、`--property` |
| `update <id>` | 更新欄位 | 同 create，另有 `--position`、`--no-start`、`--duplicate-of` |
| `assign <id>` | 指派／取消 | `--to`、`--to-id`、`--unassign`、`--no-start` |
| `status <id> <status>` | 變更狀態 | `--no-start`、`--duplicate-of` |
| `search <query>` | 搜尋 | `--limit`、`--include-closed` |
| `children <id>` | 依 Stage 分組列出子 Issue | |
| `pull-requests <id>` | 連結的 PR | |
| `timeline <id>` | 活動與評論時間序 | `--action`、`--activity-only` |
| `comment list/add/update/delete/resolve/unresolve` | 評論 | `--content`／`-stdin`／`-file`、`--parent`、`--attachment`、`--expected-revision` |
| `subscriber list/add/remove` | 訂閱者 | `--user`、`--user-id` |
| `label list/add/remove` | Issue 標籤 | |
| `metadata list/get/set/delete` | 鍵值 Metadata | `--key`、`--value`、`--type` |
| `property list/set/unset` | 自訂屬性值 | `--name`、`--value` |
| `runs <id>`、`run-messages <run-id>` | Run 紀錄與訊息 | `--since`、`--issue` |
| `usage <id>` | Token 用量 | |
| `rerun <id>`、`cancel-task <run-id>` | 重跑／取消 | `--issue` |
| `reorder <id>` | 看板內排序 | |
| `wakeup events/create/list/get/update/disable/delete/trigger/runs/checkin` | Issue Wakeup | 見第 13.8 節 |

#### Core：其他

| 指令 | 子指令 | 重點 |
| --- | --- | --- |
| `project` | `list/get/create/update/delete`、`status <id> <status>`、`resource list/add/update/remove` | `--repo`（create）、`--type`、`--url`、`--ref`、`--local-path`、`--daemon-id`、`--execution-mode` |
| `label` | `list/get/create/update/delete` | `--resource-type issue\|skill`、`--color` |
| `property` | `list/get/create/update/archive/unarchive` | `--type`（9 種）、`--option`；型別建立後不可改 |
| `agent` | `list/get/create/update/archive/restore`、`copy`、`tasks`、`avatar`、`env get/set`、`skills list/set/add`、`mcp list/add/enable/disable/remove` | 見第 10 章 |
| `skill` | `list/get/create/update/delete`、`import`、`refresh`、`search`、`files list/upsert/delete`、`label list/add/remove` | `--on-conflict fail\|overwrite\|rename\|skip` |
| `squad` | `list/get/create/update/delete`、`member list/add/set-role/remove`、`activity <issue-id> <outcome>` | `delete` 為封存 |
| `autopilot` | `list/get/create/update/delete`、`trigger`、`runs`、`trigger-add/trigger-list/trigger-update/trigger-delete/trigger-rotate-url` | `--mode create_issue\|run_only` |
| `workspace` | `list/get/create/update/switch`、`member list/invite`、`mcp list/add/update/remove` | MCP 寫入限 owner／admin |
| `repo` | `list/add/remove/checkout` | `checkout --ref`、`--fresh` |
| `chat` | `history`、`thread [id]` | `--limit`、`--before` |

#### Runtime 與 Additional

| 指令 | 子指令 | 重點 |
| --- | --- | --- |
| `daemon` | `start/stop/restart/status/logs/disk-usage` | 見第 14.2 節 |
| `runtime` | `list/usage/activity/update/rename/delete`、`profile list/create/update/delete/set-path/unset-path` | `delete --cascade`；`update --target-version --wait` |
| `auth` | `status`、`logout` | `logout` 只刪本機 Token，不撤銷 |
| `user` | `profile get/update` | |
| `login` | — | `--token` |
| `setup` | `cloud`（預設）、`self-host` | `--server-url`、`--app-url`、`--port`、`--frontend-port`、`--callback-host` |
| `attachment` | `download <id>`、`upload <path>` | `download --output-dir`；`upload --task`（給 Chat Task 內的 Agent） |
| `config` | `show`、`set <key> <value>` | 空字串清除 |
| `update`、`version` | — | `version --output json` |

### 19.7 常用工作流程範例

```bash
# 以檔案建立 Issue 並指派
multica issue create --title "升級 Spring Boot 至 3.5" \
  --description-file ./specs/upgrade.md \
  --priority high --assignee "be-impl" --project <project-id>

# 篩選我負責、進行中的 Issue（JSON，只取必要欄位）
multica issue list --assignee "me@example.com" --status in_progress \
  --output json --fields identifier,title,status

# 追蹤某個 Run 的輸出（增量）
multica issue runs MUL-123
multica issue run-messages <run-id> --issue MUL-123 --since 120

# 查詢某 Issue 在 in_review 停留多久
multica issue timeline MUL-123 --action status_changed

# 盤點：列出所有 Agent 與其 Runtime
multica agent list --output json
multica runtime list --output json
```

### 19.8 Agent Task 內的 CLI

CLI 在 Daemon 管理的 Agent Task 中執行時：

- 不載入、不修改人類的 Profile 檔；API 指令以 Daemon 注入的 Task 範圍憑證（`mat_`）驗證；
- `config show`／`config set` 使用 Task 私有狀態；
- `login`、`logout`、`setup`、`workspace switch`、本機 Runtime Profile 路徑變更、`daemon start/stop/restart`、`daemon logs` 等人類操作**不可用**；
- `auth status` 不印出 Token；
- `daemon status` 與 `daemon disk-usage` 仍可用，但限縮在承載該 Agent 的 Runtime。

這保護了 CLI 隱式的 Profile 解析，但**不是作業系統檔案邊界**：以同一系統使用者執行的行程仍可開啟已知路徑。需要更強保證時，請使用專用使用者、容器或 VM（第 20 章）。

### 19.9 從其他編碼 Agent 驅動 Multica

若大部分工作已在 Codex、Claude Code 或 Cursor 中進行，可直接在那裡操作 Multica。官方 [Multica CLI Skill](https://github.com/multica-ai/multica-cli) 教這些 Agent 安全地使用本章指令：以節省 Token 的方式讀取 Issue 與評論串、透過檔案撰寫評論，並處理 @提及、狀態變更與指派帶來的副作用。

| 特性 | 說明 |
| --- | --- |
| 權限 | 完全透過你已驗證的 CLI 執行，**本身不授予任何存取權**；權限來自你的登入、所選 Profile 與 Workspace |
| 版本需求 | CLI v0.4.26 以上 |
| 安裝 | README 說明 Claude Code Plugin Marketplace、Codex Skill 安裝器、Cursor，以及任何讀取 Markdown 指令的工具 |

> 💡 **實務建議：** 這是「讓外部 AI 工具操作 Multica」的官方途徑（取代舊版手冊中無法佐證的「MCP Provider」描述）。在本機 Claude Code 中安裝此 Skill 後，可以直接說「把這個 Bug 開成 Issue 指派給 be-impl」，由它呼叫 `multica issue create`。

---

## 第 20 章：安全模型與治理

> **本章重點：** Multica 的安全邊界是「Daemon 使用者」；三種隔離部署方式；Multica 實際提供的隔離與「不是邊界」的項目；機密存放位置矩陣；資料外流面（遙測、PostHog、伺服器端 LLM）；網路安全；稽核與可追溯性；SSDLC 整合。

### 20.1 安全邊界就是 Daemon 使用者

Agent 領取 Run 時，Daemon 會把 AI 編碼工具（Codex、Claude Code 等）啟動為子行程。理解這個行程能碰到什麼，就是整個安全模型。

預設情況下，Run 以**執行 Daemon 之作業系統使用者的完整權限**執行：能讀寫該使用者能讀寫的所有檔案、使用該使用者的憑證、不受限制地存取網路。

> ⚠️ **注意：** Multica **不提供檔案系統沙箱**。若 Daemon 以你的個人帳號執行，一次 Run 就能讀取你的 SSH 金鑰、修改 Shell 設定檔、刪除你的文件。隔離必須來自你為 Daemon 設下的邊界。

這是刻意的設計：Agent 需要安裝依賴、執行建置、使用雲端 CLI、驅動預期有正常家目錄的工具。部分檔案沙箱會以難以診斷的方式破壞這些工作（工具回報「未登入」或悄悄用錯帳號），卻仍擋不住最重要的風險——讀取憑證並經網路送出。因此 Multica 不假裝自己是邊界，而是要求你在它外面加一層。

### 20.2 建議的隔離部署

由輕到重：

| 方式 | 做法 | 取捨 |
| --- | --- | --- |
| **專用 Unix 使用者** | 建立 `multica` 使用者，只給它 Agent 需要的 Repo 與憑證，以該使用者執行 Daemon | 最輕量；你自己的帳號不受影響 |
| **容器** | 在容器中執行 Daemon，只掛載必要目錄與機密 | 隔離較好；需處理 AI 工具在容器內的登入 |
| **虛擬機** | 完整隔離 | 需要佈建與維護機器 |

不論選哪一種，**該環境中可取得的憑證都要視為 Agent 可使用的憑證**：Token 範圍盡量窄、用專用 Deploy Key 取代個人 SSH 金鑰、不要在該使用者家目錄留下無關的正式環境憑證。

📘 **建議實務：Linux 專用使用者 + systemd 範例**

```bash
# 1. 建立專用使用者（無 sudo 權限）
sudo useradd --create-home --shell /bin/bash multica-runner

# 2. 以該使用者安裝 CLI 與 AI 工具，並完成登入
sudo -iu multica-runner
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
claude        # 完成 AI 工具登入
multica setup self-host --server-url https://api.example.com --app-url https://app.example.com
multica daemon stop   # 改交由 systemd 管理
exit
```

```ini
# /etc/systemd/system/multica-daemon.service
[Unit]
Description=Multica agent daemon
After=network-online.target
Wants=network-online.target

[Service]
User=multica-runner
WorkingDirectory=/home/multica-runner
Environment=MULTICA_DAEMON_AUTO_UPDATE=false
Environment=MULTICA_WORKSPACES_ROOT=/home/multica-runner/multica_workspaces
ExecStart=/home/multica-runner/.local/bin/multica daemon start --foreground
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now multica-daemon
sudo -iu multica-runner multica daemon status
```

> 💡 `ExecStart` 的路徑請以 `sudo -iu multica-runner command -v multica` 的實際結果為準（安裝腳本與 Homebrew 的安裝位置不同）。以 `--foreground` 讓 systemd 直接管理行程生命週期。

### 20.3 Multica 實際提供的隔離

以下機制是真的，但屬於**便利性與爆炸半徑縮減**，不是對抗主動逃逸之 Run 的安全邊界：

| 機制 | 說明 |
| --- | --- |
| 每次 Run 的工作目錄 | 每個 Run 在 `~/multica_workspaces/` 下有自己的工作目錄，併發 Run 不會撞到同一個 checkout |
| 每次 Run 的 Agent 狀態 | Codex 使用 Run 專屬的 `CODEX_HOME`（設定、Session、Skills），不污染你的 `~/.codex/`；Hermes 綁定 Skill 時同理 |
| Run 範圍 API Token | 交給 Run 的 `MULTICA_TOKEN`（`mat_`）由 Server 綁定到該 Agent 與該 Run，Run 無法透過 Multica API 冒充你或其他 Agent |
| 失效關閉 | Daemon 管理的 Agent CLI 呼叫失去 Task Token 時會失效關閉，不會以 Workspace owner 身分寫入（v0.3.35+） |
| 私有 Runtime | 他人的私有 Runtime 無法透過 API 或 CLI 使用（v0.4.26+） |
| 日誌遮蔽 | Provider 指令日誌不再暴露憑證或 Prompt（v0.4.30+），更多種類的憑證從日誌中隱藏（v0.4.0、v0.4.2） |

### 20.4 「不是邊界」的項目

| 項目 | 說明 |
| --- | --- |
| **AI 工具自身的沙箱與核准設定** | Multica 無人值守執行 Agent，核准提示會自動回答；預設路徑上檔案沙箱也關閉——Codex 以 `sandbox_mode = "danger-full-access"`、Claude Code 以 `--permission-mode bypassPermissions` 執行。例外：Windows 上明確設定 Codex 原生沙箱（`windows.sandbox = "unelevated"` 或 `"elevated"`）時，Multica 會尊重並維持 `workspace-write` |
| **`HOME` 目錄結構** | Run 繼承 Daemon 使用者真實的 `HOME` 與 `XDG_*`，因此 `gh`、`aws`、`kubectl`、`gcloud`、`glab` 在 Run 內與 Shell 中行為相同——也意味著家目錄下的一切都可被存取 |

Linux 上的 Codex 過去以 `workspace-write` 沙箱搭配重導向的 `HOME` 執行，此做法已移除：它讓主機 CLI 在 Run 內無法使用，而且只限制寫入，從未阻止讀取並外流憑證。現在 Linux 與 macOS、Windows 預設一致。

確認某次 Run 的實際設定：

```bash
multica daemon logs --lines 200 | grep "codex sandbox"
```

Run 的 `CODEX_HOME` 下 `config.toml` 中 `# BEGIN multica-managed` 與 `# END multica-managed` 之間的區塊由 Daemon 每次寫入。

### 20.5 機密存放位置矩陣

| 機密 | 存放位置 | 保護方式 | 風險與建議 |
| --- | --- | --- | --- |
| AI 工具登入憑證 | 執行電腦（工具自行管理） | 作業系統權限 | Multica 不會收到；以專用使用者隔離 |
| Agent `custom_env` | **Server 資料庫（明文）** | API 不回傳值；僅 owner／admin 可解鎖；讀寫留稽核 | 只放低權限、單一範圍憑證 |
| Agent／Workspace MCP 設定 | **Server 資料庫** | 同上；Workspace MCP 函式庫為唯寫 | 同上；Token 以 `--server-config-file`／`-stdin` 傳入 |
| 個人存取 Token（`mul_`） | Server 只存雜湊；CLI 存於 `~/.multica/**/config.json` | 只顯示一次；可撤銷 | 設定檔不可提交或分享 |
| Run 臨時 Token（`mat_`） | 執行行程環境變數 | 綁定 Run，最長 24 小時 | 子行程會繼承，必要時明確移除 |
| Bot／自架 Git 憑證 | Server 資料庫（加密） | `MULTICA_*_SECRET_KEY` | 金鑰長期保存並納入 Secret 管理 |
| `JWT_SECRET`、`*_SECRET_KEY` | Server 環境變數／K8s Secret | 不進 Git（`multica-secrets` 不由 Chart 管理） | 以 Vault、Sealed Secrets、External Secrets 管理 |
| Autopilot Webhook Token | URL 中 | UI 預設隱藏；`--show-secrets` 才顯示；可輪替 | 外洩立即 Rotate URL |
| Agent 自訂參數 | 子行程 argv | 日誌遮蔽，但 `ps`／`/proc` 可見 | **不要放憑證** |

### 20.6 資料外流面

| 資料流 | 預設 | 內容 | 關閉方式 |
| --- | --- | --- | --- |
| **第一方匿名遙測**（v0.4.44+） | 開啟 | 每 UTC 日一份部署層級快照，送往固定端點 `https://telemetry.multica.ai/v1/telemetry/events`：版本；Workspace、成員、活躍 Agent、24 小時活躍 Daemon 的**分桶**數量；前 24 小時 Run 的開始／完成／失敗／取消總數。**不含**名稱、Email、IP、業務 ID、主機資訊、Repo、模型、Prompt、輸出、路徑、Token／成本、憑證、錯誤或日誌 | API 伺服器設 `DO_NOT_TRACK=1`（或 `true`）並重建後端 |
| **PostHog 產品分析** | 未設 `POSTHOG_API_KEY` 即不送 | 產品使用事件 | `ANALYTICS_DISABLED=true` |
| **伺服器端 LLM** | 未設定即停用 | 新對話第一則訊息、追問用的最近對話片段 | `MULTICA_LLM_API_KEY` 與 `MULTICA_LLM_BASE_URL` 留空 |
| **AI 工具呼叫模型** | 依工具 | Agent 讀取的程式碼與上下文 | 由 AI 工具設定與供應商合約管控（不受 Multica 設定影響） |
| **通訊平台** | 連接後 | 對話內容與 Agent 回覆 | 不連接或中斷 Bot |

遙測端點編譯在伺服器中、無法以設定改向；`DO_NOT_TRACK` 與 `ANALYTICS_DISABLED` 互相獨立。複製正式資料庫做 staging 時，請在啟動前清空副本的 `instance_telemetry_state` 資料表（或設 `DO_NOT_TRACK=true`），否則兩個部署會共用同一身分。

> 📘 **建議實務：** 受監管產業的內網部署，建議預設設定 `DO_NOT_TRACK=1`、`ANALYTICS_DISABLED=true`，伺服器端 LLM 留空或指向內部 Gateway，並以對外防火牆白名單只放行必要目的地（AI 供應商 API、Git 主機、通訊平台 API）。

### 20.7 網路安全

| 控制項 | 建議 |
| --- | --- |
| 埠暴露 | Compose 預設只綁 `127.0.0.1:3000`／`:8080`；不要改成 `0.0.0.0` 對外，改用反向代理 |
| TLS | 反向代理終結 TLS；HTTPS 頁面必須用 `wss://`；`FRONTEND_ORIGIN` 為 HTTPS 時 Session Cookie 自動加上 `Secure` |
| CORS／WebSocket 來源 | `CORS_ALLOWED_ORIGINS`／`ALLOWED_ORIGINS` 只列實際來源 |
| Cookie 範圍 | 優先同源佈局；必須分離網域時 `COOKIE_DOMAIN` 用最窄上層網域（第 5.6 節） |
| 代理信任 | `RATE_LIMIT_TRUSTED_PROXIES`、`MULTICA_TRUSTED_PROXIES` 只列真實代理 CIDR，避免偽造 `X-Forwarded-For` |
| 速率限制 | 設定 `REDIS_URL` 以啟用驗證碼速率限制 |
| 管理介面 | `METRICS_ADDR` 綁內部介面；pprof 固定在 `127.0.0.1:6060` 且不可設定；維護 API 固定 `127.0.0.1:MAINTENANCE_PORT`、**無應用層驗證**，不可加到 Service／Ingress |
| 對外連線 | Telegram、Slack 等需要對外 HTTPS；Go 會讀取 `HTTPS_PROXY`／`NO_PROXY` |
| 私有 CA | 以 `SSL_CERT_DIR` 加入信任，不要關閉驗證 |

### 20.8 稽核與可追溯性

| 能力 | 說明 |
| --- | --- |
| Agent 動作歸屬 | Agent 以 `mat_` Token 發出的請求記錄為 Agent 的動作，並標示是哪位成員觸發該 Run（v0.4.2+） |
| 時間軸 | 狀態、優先序、Assignee、標題、日期變更與 Run 完成／失敗，皆寫入 Issue 活動紀錄（`multica issue timeline`） |
| Run Transcript | 每次 Run 的工具呼叫、指令與錯誤，含時間戳與誰取消了 Task（v0.4.43+） |
| 環境變數稽核 | `custom_env` 每次解鎖讀取或變更都留稽核紀錄 |
| Squad 評估紀錄 | Leader 以 `squad activity` 記錄每輪評估 |
| 用量與成本 | Analytics 頁、`issue usage`、`runtime usage`、Agent Run 歷史 |
| 已離開成員 | 活動歷史中保留其名稱（v0.4.39+） |

> 💡 Multica 目前沒有「全 Workspace 稽核日誌匯出」的獨立功能。需要集中留存時，可定期以 CLI／API（`--output json`）匯出時間軸與 Run 紀錄到 SIEM，或在資料庫層建立唯讀副本供稽核查詢（`DATABASE_REPLICA_URL` 只提供連線，查詢需自行設計）。

### 20.9 SSDLC 整合

📘 **建議實務：**

```mermaid
flowchart LR
    REQ["需求 Issue<br/>含安全需求"] --> DEV["Agent 實作<br/>（專用 Runner）"]
    DEV --> PR["PR + 分支保護"]
    PR --> SAST["SAST / SCA / Secret Scan"]
    PR --> REV["Review Agent<br/>enterprise-code-review Skill"]
    SAST --> HUMAN["人類審查與核准"]
    REV --> HUMAN
    HUMAN --> MERGE["合併 → Issue 自動 Done"]
    MERGE --> DEPLOY["既有 CD 管線部署"]
```

| SSDLC 階段 | Multica 中的做法 |
| --- | --- |
| 需求 | Issue 範本含安全需求與驗收條件；自訂屬性「需資安審查」（checkbox） |
| 設計 | Squad Leader 拆子 Issue 時，涉及認證、加密、個資的 Stage 需 @ 資安負責人 |
| 實作 | 專用 Runner、最小憑證；Agent 不可修改 CI 設定與 secrets 檔（寫入 Instructions） |
| 驗證 | PR 必經 SAST／SCA／Secret Scanning；Review Agent 使用企業 Code Review Skill；最終由人類核准 |
| 發佈 | 部署仍由既有 CD 管線執行，Agent 不直接存取正式環境 |
| 維運 | 告警經 Webhook Autopilot 由 Agent 初步分析，處置動作由人類執行 |

安全檢查清單見[附錄 A.5](#a5-安全檢查清單)。

---

## 第 21 章：系統維運

> **本章重點：** 健康檢查端點；伺服器與 Daemon 日誌；Prometheus 指標、抓取設定與告警規則範例；用量彙總（Usage Rollup）排程；維護作業 API；Go pprof；症狀導向的疑難排解；備份與災難復原。

### 21.1 健康檢查

| 端點 | 回應 | 用途 |
| --- | --- | --- |
| `GET /health` | `{"status":"ok"}` | 存活檢查：行程有回應即 ok，**即使 Migration 失敗也是 ok** |
| `GET /readyz` | `{"status":"ok","checks":{"db":"ok","migrations":"ok"}}` | 就緒檢查：同時檢查資料庫與已套用的 Migration；**驗證升級成功請用它** |
| `GET /healthz` | 同 `/readyz` | 別名 |
| `GET /health/realtime` | 即時連線健康 | 以 `REALTIME_METRICS_TOKEN` Bearer Token 保護 |

```bash
curl -fsS http://localhost:8080/health
curl -fsS http://localhost:8080/readyz
```

Kubernetes 的 Liveness Probe 用 `/health`，Readiness／Startup Probe 用 `/readyz`；外部監控應監看 `/readyz`。

### 21.2 日誌

**伺服器端：**

```bash
docker compose -f docker-compose.selfhost.yml logs -f backend
docker compose -f docker-compose.selfhost.yml logs backend | grep "EmailService:"
kubectl -n multica logs -f deploy/multica-backend
```

`LOG_LEVEL` 可設 `debug`、`info`（預設）、`warn`、`error`。後端寫入 stderr、自身不保留日誌，保留期由 Docker logging driver 或日誌收集器決定。

**Daemon 端：**

| 元件 | 查看方式 |
| --- | --- |
| 背景 Daemon | `multica daemon logs --lines 100`（會先印出解析到的絕對路徑） |
| 即時追蹤 | `multica daemon logs --follow` |
| 預設 Profile 日誌檔 | `~/.multica/daemon.log` |
| 啟動或崩潰日誌 | `~/.multica/daemon.err.log` |
| 具名 Profile | `~/.multica/profiles/<name>/` 下對應檔案 |
| 前景觀察啟動 | `multica daemon stop && multica daemon start --foreground` |

> 💡 舊的日誌檔仍可完整閱讀，最容易誤判的就是看錯檔案。不要猜路徑，以 `multica daemon logs`（加 `--profile <name>`）印出的路徑為準。v0.3.43 起 Daemon 會自行控制日誌大小。

### 21.3 Prometheus 指標

後端可在**獨立的管理監聽埠**暴露 Prometheus 指標：

```bash
METRICS_ADDR=127.0.0.1:9090 ./server/bin/server
curl http://127.0.0.1:9090/metrics
```

`METRICS_ADDR` 預設為空，不啟動；公開 API 埠**不提供** `/metrics`。HTTP 請求指標只在啟用監聽後才開始累積。指標可能揭露內部路由、流量、相依狀態與 Runtime 健康，請綁內部介面並以私有網路、白名單、NetworkPolicy 或代理驗證保護。容器內綁 `0.0.0.0:9090` 時，只發布到受信任網路（例如 `127.0.0.1:9090:9090`）。

**主要指標（摘自 v0.6.1 原始碼 `server/internal/metrics/`）：**

| 指標 | 型別 | 標籤 | 用途 |
| --- | --- | --- | --- |
| `multica_http_requests_total` | Counter | `method`、`route`、`status` | API QPS 與錯誤率 |
| `multica_http_request_duration_seconds` | Histogram | `method`、`route`、`status` | API 延遲 |
| `multica_http_in_flight_requests` | Gauge | — | 進行中請求 |
| `multica_agent_task_enqueued_total`／`dispatched_total`／`started_total` | Counter | `source`、`runtime_mode` | Run 流量 |
| `multica_agent_task_terminal_total` | Counter | `source`、`runtime_mode`、`terminal_status` | Run 結束數 |
| `multica_agent_task_failed_total` | Counter | `source`、`runtime_mode`、`failure_reason` | 依失敗原因統計 |
| `multica_agent_task_queue_wait_seconds` | Histogram | `source`、`runtime_mode` | 排隊等待時間 |
| `multica_agent_task_run_seconds` | Histogram | `source`、`runtime_mode`、`terminal_status` | 執行時間 |
| `multica_agent_task_in_progress` | Gauge | `source`、`runtime_mode` | 此行程派出且未結束的 Run |
| `multica_llm_tokens_total`、`multica_llm_cost_usd_total` | Counter | `provider`、`model`、`token_type`… | Token 與成本 |
| `multica_runtime_offline_total` | Counter | `runtime_mode`、`provider` | Runtime 離線事件 |
| `multica_db_pool_acquired_conns`、`multica_db_pool_max_conns` | Gauge | `role` | 資料庫連線池使用率 |
| `multica_db_replica_healthy`、`multica_db_replica_replay_lag_seconds` | Gauge | — | 唯讀副本健康 |
| `multica_realtime_redis_mirror_errors_total` | Counter | — | Redis 即時事件鏡像錯誤 |
| `multica_wecom_outbound_dropped_total` | Counter | `reason` | 企業微信回覆遺失 |
| `multica_build_info` | Gauge | 版本資訊 | 部署版本 |

> 💡 指標名稱與標籤屬於實作細節，官方未承諾為穩定 API；升級後請以 `curl .../metrics` 確認再調整儀表板。

📘 **建議實務：Prometheus 抓取與告警規則**

```yaml
# prometheus.yml（片段）
scrape_configs:
  - job_name: multica-backend
    static_configs:
      - targets: ['multica-backend.internal:9090']
```

```yaml
# multica-alerts.yml
groups:
  - name: multica
    rules:
      - alert: MulticaApiHigh5xxRate
        expr: |
          sum(rate(multica_http_requests_total{status=~"5.."}[5m]))
            / clamp_min(sum(rate(multica_http_requests_total[5m])), 1) > 0.05
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Multica API 5xx 比例超過 5%"

      - alert: MulticaApiSlowP99
        expr: |
          histogram_quantile(0.99,
            sum by (le) (rate(multica_http_request_duration_seconds_bucket[5m]))) > 2
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Multica API p99 延遲超過 2 秒"

      - alert: MulticaRunFailureRateHigh
        expr: |
          sum(rate(multica_agent_task_failed_total[30m]))
            / clamp_min(sum(rate(multica_agent_task_terminal_total[30m])), 0.001) > 0.3
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "Agent Run 失敗率超過 30%"

      - alert: MulticaRunQueueWaitHigh
        expr: |
          histogram_quantile(0.9,
            sum by (le) (rate(multica_agent_task_queue_wait_seconds_bucket[15m]))) > 600
        for: 15m
        labels:
          severity: info
        annotations:
          summary: "90% Run 排隊超過 10 分鐘，檢查 Runtime 容量"

      - alert: MulticaDbPoolSaturated
        expr: |
          max by (role) (multica_db_pool_acquired_conns / multica_db_pool_max_conns) > 0.9
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "資料庫連線池使用率超過 90%"
```

建議儀表板 Panel：API QPS 與 p99、5xx 比例、Run 依 `failure_reason` 的失敗分佈、排隊時間分位數、`in_progress` Run 數、Token 成本趨勢、連線池使用率、Runtime 離線事件、`/readyz` 可用率（以 Blackbox Exporter 探測）。

### 21.4 用量彙總（Usage Rollup）

Usage 與 Runtime 儀表板讀取衍生表 `task_usage_hourly`，由 `rollup_task_usage_hourly()` 填入。自 MUL-2957 起，後端以**資料庫驅動的行程內排程器**（`sys_cron_executions`）在每個副本上執行，新安裝**無需任何操作**，也不需要 `pg_cron`、外部 cron、systemd timer 或 Kubernetes CronJob。

| 機制 | 說明 |
| --- | --- |
| 多副本安全 | 每個副本每 30 秒嘗試認領目前的 5 分鐘 UTC 計畫；唯一鍵 `(job_name, scope_kind, scope_id, plan_time)` 確保只有一個勝出 |
| 防重複寫入 | SQL 函式內部持有 advisory lock `4246`，與殘留的 `pg_cron` 或手動呼叫並存也不會重複寫入 |
| 舊版相容 | 既有的 `pg_cron` 註冊可保留；確認行程內排程穩定產生 SUCCESS 後再以 `cron.unschedule` 移除 |

```sql
-- 檢查排程狀態
SELECT plan_time, status, attempt, runner_id, error_code, error_msg, started_at, finished_at
  FROM sys_cron_executions
 WHERE job_name = 'rollup_task_usage_hourly'
 ORDER BY plan_time DESC
 LIMIT 20;
```

**回填歷史資料：**

```bash
# Docker Compose
docker compose -f docker-compose.selfhost.yml exec backend \
  ./backfill_task_usage_hourly --sleep-between-slices=2s

# Kubernetes
kubectl -n multica exec deploy/multica-backend -- \
  ./backfill_task_usage_hourly --sleep-between-slices=2s
```

| 旗標 | 說明 |
| --- | --- |
| `--sleep-between-slices` | 每個月份切片之間暫停，降低正式資料庫讀取壓力 |
| `--months-back N` | 只回填最近 N 個月，**需搭配 `--force-partial`**（更舊的資料會被永久放棄） |
| `--dry-run` | 只記錄將處理的切片，不寫入 |

### 21.5 維護作業 API

部分資料修復／回填以**維運者驅動的維護作業**執行（v0.6.x 首個處理器為 `issue_status_category` v1），不在啟動時自動執行。

| 項目 | 說明 |
| --- | --- |
| 啟用 | 設定 `MAINTENANCE_PORT`（例 `6061`）；Helm 為 `backend.config.maintenancePort`；未設定即停用 |
| 綁定 | 固定 `127.0.0.1`，不可覆寫 |
| 驗證 | **刻意沒有應用層驗證**，存取依賴容器 exec 權限與網路命名空間隔離——不可發布此埠、加入 Service／Ingress 或代理 |
| 用戶端 | 後端映像內建 `/app/maintenance`（只連 loopback、忽略代理、拒絕重導向） |
| 流程 | `create`（預設 dry-run）→ `run --max-batches 1` 金絲雀 → 觀察指標 → 有界的 `run` → 以新冪等鍵 `create --apply` → 同樣金絲雀後套用 |

```bash
docker compose -f docker-compose.selfhost.yml exec -T backend /app/maintenance status --job <JOB_UUID>
kubectl exec -n multica <backend-pod> -c backend -- /app/maintenance create --help
```

> ⚠️ **注意：** 只有在版本說明或官方文件要求執行特定維護作業時才使用，並依 `docs/maintenance-jobs.md` 選擇批次大小、延遲與 SQL 逾時，先在測試環境演練。

### 21.6 Go Runtime Profiling

後端在固定的 loopback 管理監聽 `127.0.0.1:6060` 提供所有標準 pprof 路由（不可設定、永不綁到容器或主機網卡）：

```bash
docker compose -f docker-compose.selfhost.yml exec backend \
  wget -qO /tmp/heap.pprof http://127.0.0.1:6060/debug/pprof/heap
docker compose -f docker-compose.selfhost.yml cp backend:/tmp/heap.pprof ./heap.pprof
go tool pprof ./heap.pprof
```

### 21.7 疑難排解

先判斷問題在哪一層：Multica 服務、Daemon、Runtime 或 AI 工具。

```bash
multica version
multica auth status
multica daemon status --output json
multica daemon logs --lines 100
curl -i https://api.example.com/health
curl -i https://api.example.com/readyz
```

| 症狀 | 可能原因 | 處理 |
| --- | --- | --- |
| Daemon 連不上 | 未登入或 Token 過期；連到錯誤服務；DNS／TLS／防火牆；已非 Workspace 成員；本機沒有支援的 AI 工具 | `multica login` → `multica daemon restart`；**從執行電腦**測 `/health`；`multica config show` 檢查 `server_url` |
| Issue 一直 `queued` | Runtime 離線；未偵測到 Agent 設定的工具；Agent 併發（6）或 Daemon 併發（20）已滿 | `multica daemon status --output json`、`multica agent get`、`multica issue runs` |
| `waiting_local_directory` | 同一本機目錄被另一個 Run 使用（Direct 模式） | 改用 Parallel（worktree）模式，或停止卡住的 Run；目錄鎖在 Daemon 記憶體中，`multica daemon restart` 即釋放 |
| AI 工具無法啟動 | 未登入、API Key／額度／模型權限、模型與 Thinking Level 不支援、工作目錄不可寫、自訂參數無效 | 在執行電腦終端機直接執行同一工具確認 |
| macOS 升級 CLI 後 Run 卡住 | Homebrew CLI 無穩定簽章，TCC 權限綁定舊版二進位，存取 `~/Desktop`、`~/Documents` 等受保護資料夾時等待授權視窗 | 在該 Mac 按 **Allow**；無人值守主機以 `realpath "$(command -v multica)"` 找出新路徑授予「完整磁碟取用權」；以 `--no-auto-update` 控制升級時機；或改用 Desktop 內建（已簽章）CLI |
| 即時更新失效 | WebSocket 未連上：`FRONTEND_ORIGIN` 不符、HTTPS 頁面未用 `wss://`、代理未轉送 Upgrade、登入過期 | 瀏覽器 DevTools → Network → WS 確認 `101`；Daemon 走 `/api/daemon/ws`，同樣要導到後端 |
| `multica setup` 回報伺服器無法連線 | 代理把 `/health` 送到不轉發它的舊版 Web（404），或 DNS／TLS／防火牆／5xx | 在代理中把 `/health` 明確導到後端 8080 |
| `multica login` TLS 握手逾時 | Go 預設送出含後量子金鑰的大型 ClientHello（約 1.5 KB），部分資安軟體／VPN／防火牆丟棄 | `GODEBUG=tlsmlkem=0 multica --debug login` 確認後，為執行 CLI 與 Daemon 的使用者永久設定 `GODEBUG=tlsmlkem=0`；根本解法是修正網路設備 |
| 驗證碼／邀請信未送達 | DEV mode；Resend Key 或寄件網域；SMTP 主機、埠、帳密、寄件者 | `logs backend \| grep "EmailService:"` 判斷模式與失敗階段 |
| 附件上傳／下載失敗 | 代理限制 Body 大小；上傳目錄不可寫或未掛 Volume；S3 設定不符；下載網址網域或協定錯誤 | 檢查後端日誌與回應碼；內網 S3 用 `ATTACHMENT_DOWNLOAD_MODE=proxy` |
| Usage 顯示 0 | Rollup 排程失敗或 Migration 未完成 | 比對 `task_usage` 與 `task_usage_hourly` 筆數、查 `sys_cron_executions`；手動 `SELECT rollup_task_usage_hourly();` 區分 SQL 與排程問題 |
| 升級時 `refusing to drop legacy daily rollups` | Migration 103 的自動回填未完成 | 手動執行 `backfill_task_usage_hourly` 後重啟後端，確認 `/readyz` 的 `migrations` 為 ok |
| 寫入回 `403 CSRF validation failed` | 分離網域未設 `COOKIE_DOMAIN` | 第 5.6 節 |
| 埠被占用 | 另一個 Multica checkout 或其他程式 | `lsof -nP -iTCP:8080 -sTCP:LISTEN`（macOS／Linux）、`netstat -ano \| findstr :8080`（Windows）；另一個 checkout 執行 `make stop` |

回報問題時附上錯誤訊息、相關日誌、CLI 版本與作業系統，並移除 Token、Email 等敏感資訊；可先搜尋 [GitHub Issues](https://github.com/multica-ai/multica/issues)。

### 21.8 備份與災難復原

| 資料 | 位置 | 備份方式 |
| --- | --- | --- |
| PostgreSQL | Compose Volume `multica_pgdata`（或外部資料庫） | `pg_dump`；外部資料庫用其快照／PITR |
| 本機附件 | Volume `backend_uploads` | Volume 備份或改用 S3（物件儲存版本控制） |
| `.env`／K8s Secret | 部署主機／叢集 | 納入機密管理系統；**`*_SECRET_KEY` 遺失會導致整合憑證無法解密** |
| Daemon 設定 | 執行電腦 `~/.multica/` | 可重建（重新 `setup` 即可），不必備份 |
| 工作目錄 | `~/multica_workspaces/` | 暫存性質，未推送的成果應以 Git 為準 |

官方建議的 PostgreSQL 備份寫法（Migration 只能前進，升級前務必備份）：

```bash
docker compose -f docker-compose.selfhost.yml exec -T postgres \
  pg_dump -U multica multica > multica-backup.sql && gzip multica-backup.sql
```

> ⚠️ **注意：** 不要寫成 `pg_dump ... | gzip > backup.sql.gz`。Shell 回報的是管線**最後一個**指令的結束碼，即使 dump 失敗也會得到一個有效、卻只有 20 bytes 的空壓縮檔。先導到檔案，讓 `pg_dump` 的結束碼決定 `&&` 是否繼續。若 `.env` 改過 `POSTGRES_USER`／`POSTGRES_DB`，請替換對應值。

還原（📘 建議流程）：

```bash
# 1. 停止前後端，保留資料庫
docker compose -f docker-compose.selfhost.yml stop backend frontend
# 2. 還原
gunzip -c multica-backup.sql.gz | docker compose -f docker-compose.selfhost.yml exec -T postgres \
  psql -U multica -d multica
# 3. 啟動並驗證
docker compose -f docker-compose.selfhost.yml up -d
curl -fsS http://localhost:8080/readyz
```

> 📘 **建議實務：** 正式環境建議 RPO ≤ 24 小時（每日 `pg_dump` 或資料庫 PITR）、RTO ≤ 4 小時；每季在隔離環境演練一次還原，並在演練環境設定 `DO_NOT_TRACK=true` 或清空 `instance_telemetry_state`，避免與正式環境共用遙測身分。還原到較舊的資料庫後，請使用與備份時**相同或較新**的映像版本啟動（Migration 只能前進）。

---

## 第 22 章：升級、擴展與高可用

> **本章重點：** 發版節奏與版本鎖定策略；CLI／Daemon 升級；Docker Compose 與 Helm 的伺服器升級（含兩個「看似升級、其實沒升」的陷阱）；後端多副本與 Redis；資料庫連線預算與唯讀副本；執行層擴展；高可用參考架構。

### 22.1 版本與發版策略

| 事實 | 說明 |
| --- | --- |
| 發版節奏 | 官方表示「多數平日都會發版」，`main` 移動很快；2026-07-01 至 10-01 共 61 個 Release |
| 版本號 | 仍為 `0.x`，沒有 LTS；次版本（`0.4` → `0.5` → `0.6`）也可能包含行為變更 |
| 映像標籤 | GHCR `multica-backend`／`multica-web` 提供 `latest` 與各 Release Tag（如 `v0.6.1`） |
| Helm Chart | Chart 版本＝Git Tag 去掉 `v`，預設映像 Tag 為對應 Release |
| Migration | 只能前進，在後端啟動時自動執行且冪等 |
| 用戶端相容 | Desktop 可能比 Server 新或舊；API 回應在用戶端以 zod 解析以容忍差異；v0.4.40 起本機 App 與 Server 版本不同時仍可開始 Task |

📘 **建議實務：企業版本策略**

| 環境 | 策略 |
| --- | --- |
| 開發／試點 | 追蹤 `latest`，每週更新，第一時間發現行為變化 |
| Staging | 鎖定 Release Tag，每兩週升級一次，執行驗收清單（附錄 A.4） |
| 正式 | 鎖定經 Staging 驗證的 Tag，每月或依安全修補升級；保留上一版映像與資料庫備份以便回滾 |
| 變更通知 | 訂閱 GitHub Releases 與官網 [Changelog](https://multica.ai/changelog)，留意標示 Self-host、Migration 的項目 |

### 22.2 CLI 與 Daemon 升級

```bash
multica update                                   # 偵測安裝方式並更新
brew upgrade multica                              # Homebrew 安裝時
multica runtime update <runtime-id> --target-version <version> --wait   # 遠端更新某台 Runtime
```

| 機制 | 預設 | 說明 |
| --- | --- | --- |
| 自動更新 `MULTICA_DAEMON_AUTO_UPDATE` | Cloud `true`／自架 `false` | 每 `6h` 檢查（`MULTICA_DAEMON_AUTO_UPDATE_INTERVAL`） |
| 自動重載 `MULTICA_DAEMON_AUTO_RELOAD` | `true` | 二進位被 `brew upgrade`、重新下載或本機建置替換時自動重啟 Daemon |
| 從源碼建置的 Runtime | — | 標示為本機建置，不提供不可用的更新（v0.4.18+） |
| Desktop | 自動更新開啟 | 見第 18.5 節 |

> ⚠️ **macOS 注意：** Homebrew CLI 每次升級後，存取受保護資料夾的 Run 可能卡在 TCC 授權視窗（第 21.7 節）。無人值守的 Mac Runner 建議以 `--no-auto-update` 啟動，升級時同步重新授權。

### 22.3 Server 升級：Docker Compose

```bash
cd multica
# 0. 備份（Migration 只能前進）
docker compose -f docker-compose.selfhost.yml exec -T postgres \
  pg_dump -U multica multica > multica-backup.sql && gzip multica-backup.sql
# 1. 更新 Compose 檔本身（新的環境變數、服務、健康檢查）
git pull --ff-only
# 2. 拉取映像並重建
docker compose -f docker-compose.selfhost.yml pull
docker compose -f docker-compose.selfhost.yml up -d
# 3. 驗證（用 /readyz，不要用 /health）
curl -fsS http://localhost:8080/readyz
docker compose -f docker-compose.selfhost.yml logs -f backend
```

`make selfhost` 與上述 `pull` + `up -d` 在既有安裝上結果相同（另會在 `.env` 不存在時建立，並等待 `/health`）；**不會覆寫既有 `.env`**。指定的 GHCR Tag 尚未發布時，改用 `make selfhost-build` 或 `docker compose -f docker-compose.selfhost.yml -f docker-compose.selfhost.build.yml up -d --build`。

> ⚠️ **陷阱 1：鎖定了 `MULTICA_IMAGE_TAG` 就什麼都不會升級。** 兩個映像都解析為 `${MULTICA_IMAGE_TAG:-latest}`，`.env.example` 預設 `latest`。若 `.env` 鎖定某個 Release，`pull` 只會重抓同一個 Tag——**沒有錯誤、沒有警告**，你仍在舊版。升級前先檢查：
>
> ```bash
> grep MULTICA_IMAGE_TAG .env
> # MULTICA_IMAGE_TAG=v0.4.5   ← 已鎖定：先改成目標版本或 latest
> ```
>
> 另外，`git pull` 只更新 `docker-compose.selfhost.yml`，**不是**取得新版的方法；實際版本由 `docker compose pull` 當下向 GHCR 解析 Tag 決定。

| 升級注意事項 | 說明 |
| --- | --- |
| `/health` vs `/readyz` | `/health` 在 Migration 失敗時仍回 ok；只有 `/readyz` 回 HTTP 200 且 `db`、`migrations` 皆 ok 才代表升級完成 |
| Migration 103 | `v0.3.4 → v0.3.5+` 的 fail-closed 檢查；自動回填失敗時手動執行 `backfill_task_usage_hourly` 後重啟（第 21.4 節） |
| `NEXT_PUBLIC_API_URL` | v0.4.10 起在官方映像生效；舊 `.env` 中錯誤的值（帶路徑）會在升級後突然生效，造成資料呼叫 404 |
| 中斷的升級 | v0.4.27 起被中斷的自架升級再次執行可安全續做 |
| 資料量 | `docker compose down` 保留 Volume；**不要**用 `down -v` |

### 22.4 Server 升級：Kubernetes（Helm）

```bash
# 升級到指定 Release 的 Chart（預設映像即為該 Release）
helm upgrade multica oci://ghcr.io/multica-ai/charts/multica \
  --version <chart-version> -n multica -f my-values.yaml

helm -n multica history multica
kubectl -n multica rollout status deploy/multica-backend
curl -H "Host: api.multica.dev.lan" http://<ingress-ip>/readyz

# 回滾
helm -n multica rollback multica
helm -n multica rollback multica <revision>
```

需要讓映像版本與 Chart 版本分開時，在 values 指定：

```yaml
images:
  backend:
    tag: v0.6.1
  frontend:
    tag: v0.6.1
```

> ⚠️ **陷阱 2：`rollout restart` 不是升級。** Chart 預設 `pullPolicy: IfNotPresent`，節點已有該 Tag 快取時會沿用舊映像，重啟後什麼都沒變。要追蹤浮動 Tag，先把 `images.backend.pullPolicy`／`images.frontend.pullPolicy` 設為 `Always`；可靠的做法是修改 Tag 後 `helm upgrade`，讓 Pod Spec 改變而觸發滾動更新。

回滾時也要注意資料庫：

> 💡 回滾 Helm Release 只回滾工作負載，**不會回滾資料庫 Migration**。跨越含 Migration 的版本回滾前，應準備對應時間點的資料庫備份。

### 22.5 後端水平擴展

```mermaid
flowchart LR
    LB["負載平衡 / Ingress"] --> B1["backend #1"]
    LB --> B2["backend #2"]
    LB --> B3["backend #3"]
    B1 --> R[("Redis<br/>即時事件 relay / 速率限制 / Bot 租約")]
    B2 --> R
    B3 --> R
    B1 --> P[("PostgreSQL 主庫")]
    B2 --> P
    B3 --> P
    P -.-> RP[("唯讀副本（選用）")]
```

| 項目 | 多副本需求 |
| --- | --- |
| **Redis** | 設定 `REDIS_URL`：跨副本即時事件、共享速率限制、通訊 Bot WebSocket 租約、Token 快取。沒有 Redis 時單一實例使用行程內實作 |
| Redis Cluster／Serverless | v0.4.43+ 支援；`REDIS_CLUSTER_MODE=true` 需 database 0 與 `REALTIME_RELAY_MODE=sharded`；託管 Redis 封鎖 `CLIENT SETNAME` 時設 `REDIS_DISABLE_CLIENT_NAME=true` |
| 企業微信 | 只有在 sharded／dual relay（有 Redis）時支援多副本（第 16.7 節） |
| Usage Rollup 排程 | 多副本安全，無需額外設定 |
| 優雅關閉 | `MULTICA_SHUTDOWN_HOLD_DURATION` 讓 LB 先摘除節點；`terminationGracePeriodSeconds` 必須大於 hold 加實際關閉時間 |
| 即時事件 | Pod 重啟期間的事件有 5 分鐘重播視窗 |
| Daemon 流量分流 | v0.4.33+ 可把 Daemon 流量導向另一個伺服器位址（`MULTICA_DAEMON_SERVER_URL`） |

**資料庫連線預算：**

```text
總連線數 ≈ 後端副本數 × (DATABASE_MAX_CONNS + DATABASE_REPLICA_MAX_CONNS)
         必須明顯低於 PostgreSQL max_connections
```

使用 PgBouncer、RDS Proxy、Supavisor 等連線池時可大幅提高 `DATABASE_MAX_CONNS`。`DATABASE_REPLICA_URL` 會驗證連線為唯讀，但**只有程式明確選用的讀取路徑才會使用副本**；副本失效時自動退回主庫並短暫斷路。副本讀取沒有應用層的延遲上限，請在資料庫層監控複寫延遲（`multica_db_replica_replay_lag_seconds`）。搜尋負載高時可用 `DATABASE_SEARCH_WORK_MEM_MB` 限制每個搜尋節點的記憶體。

### 22.6 執行層擴展

| 手段 | 說明 |
| --- | --- |
| 增加 Daemon 主機 | 每台主機為每個 Workspace × AI 工具註冊 Runtime；把 Agent 分散到不同 Runtime |
| 調整併發 | 主機層 `MULTICA_DAEMON_MAX_CONCURRENT_TASKS`（預設 20）、Agent 層併發（預設 6） |
| 複製 Agent 到其他 Runtime | `multica agent copy <id> --runtime-id <new> --model <model>` |
| 公開 Runtime | 由平台帳號擁有並設為公開，讓團隊 Agent 共用 Runner 主機 |
| 磁碟 | 以 `MULTICA_WORKSPACES_ROOT`、`MULTICA_AGENT_TEMP_BASE` 指向大容量磁碟；調整 GC（第 6.11 節） |
| 資源分配 | `MULTICA_TASK_SLOT` 可用於依槽位分配 GPU 等資源 |
| AI 工具額度 | 平行 Run 共享工具帳號額度，大量併發時注意 `provider_capacity_or_rate_limit` 失敗 |

> 💡 **容量估算：** 每個執行中的 Run 會啟動一個 AI 工具行程，並可能執行建置與測試。以「同時執行 Run 數 × 單一建置所需 CPU／記憶體」估算 Runner 主機規格，再以 `multica_agent_task_queue_wait_seconds` 觀察是否需要擴充。

### 22.7 高可用參考架構

📘 **建議實務：**

| 層 | 最小 HA 配置 | 說明 |
| --- | --- | --- |
| 入口 | 2 台反向代理或雲端 LB + Ingress | `/ws`、`/api/daemon/ws` 需支援長連線（`proxy_read_timeout 86400` 或 `flush_interval -1`） |
| Web | `frontend.replicas: 2` | 無狀態 |
| 後端 | `backend.replicas: 2` 以上 + Redis | 見 22.5 |
| PostgreSQL | 託管 HA（Multi-AZ）或 CloudNativePG；`postgres.external.enabled=true` | 啟用 PITR |
| Redis | 託管 HA Redis 或 Redis Cluster | 失效時登入速率限制 fail open、邀請回 503 |
| 物件儲存 | S3 相容（版本控制） | 取代單節點 `backend_uploads` PVC |
| 執行層 | 至少 2 台 Runner 主機，Agent 分散 | 單一 Runner 故障時另一台的 Agent 仍可工作（Run 不會跨機遷移） |

> ⚠️ **注意：** Run 綁定在領取它的 Runtime 上，不會自動移到其他機器。Runner 主機故障時，進行中的 Run 會在重連寬限期（`MULTICA_RUNTIME_RECONNECT_GRACE`，預設 3h）後失敗，可自動重試的原因會重試一次；高可用的關鍵是讓同一職責有多個 Agent 分散在不同 Runtime。

---

## 第 23 章：企業導入與最佳實務

> **本章重點：** 分階段導入路線圖；角色分工（RACI）；Issue 撰寫原則與範本；Agent 使用規範；常見錯誤與對策；成效衡量指標；參與 Multica 開發的本機環境。

本章內容除特別註明來自官方文件者外，皆為 📘 **建議實務**。

### 23.1 分階段導入路線圖

```mermaid
flowchart LR
    P0["Phase 0<br/>評估<br/>1–2 週"] --> P1["Phase 1<br/>試點<br/>2–4 週"]
    P1 --> P2["Phase 2<br/>單一團隊<br/>1–2 月"]
    P2 --> P3["Phase 3<br/>跨團隊推廣<br/>2–3 月"]
    P3 --> P4["Phase 4<br/>持續最佳化"]
```

| 階段 | 目標 | 主要行動 | 完成條件 |
| --- | --- | --- | --- |
| **Phase 0 評估** | 確認適用性與合規 | 法務審閱 Multica License；資安審查第 20 章安全模型；以 Cloud 或單機 PoC 跑完官方 Tutorial | 法務與資安核可、PoC 完成 5 個 Issue |
| **Phase 1 試點** | 驗證價值與流程 | 自架 Staging（Compose）；2–3 位資深工程師；1–2 個專用 Runner；建立 3 個 Agent（實作、審查、文件） | 20+ 個 Issue 完成、`in_review` 退回率可接受 |
| **Phase 2 單一團隊** | 建立標準作業 | 正式環境（同源部署 + SMTP + Redis）；Skill Library 初版；Squad；GitHub 整合與 PR 驅動結案 | 團隊 50% 以上適合的工作經由 Multica |
| **Phase 3 跨團隊** | 規模化與治理 | 依產品線分 Workspace；共用 Runner 池；Autopilot 每日摘要與 CI 失敗分析；監控與告警 | 每季盤點 Agent／Skill／Token 成本 |
| **Phase 4 最佳化** | 持續改善 | Agent 回顧會議；Skill 迭代；成本最佳化；跟進新版本功能 | 持續 |

### 23.2 角色分工（RACI）

| 活動 | 平台團隊 | Tech Lead | 開發者 | 資安 | 法務 |
| --- | :---: | :---: | :---: | :---: | :---: |
| 部署與升級 Multica 服務 | R/A | C | — | C | — |
| Runner 主機與隔離 | R/A | C | — | C | — |
| Agent 定義與 Instructions | C | A | R | C | — |
| Skill Library 審查 | C | A | R | R | — |
| Agent Access 與權限盤點 | R | A | I | C | — |
| Issue 撰寫與驗收 | — | A | R | — | — |
| PR 審查與合併 | — | A | R | C | — |
| 授權合規 | I | I | — | C | R/A |

R＝執行、A＝當責、C＝諮詢、I＝告知。

### 23.3 Issue 撰寫原則

Agent 的產出品質主要取決於 Issue 的品質。

| 原則 | 說明 | 範例 |
| --- | --- | --- |
| 具體 | 明確的輸入、輸出與限制 | ✅「實作 `POST /api/v1/users`，驗證 Email 格式，重複時回 409」 |
| 上下文充足 | 指出相關檔案、既有模式 | ✅「參考 `OrderController` 的錯誤處理方式」 |
| 可驗證 | 明確的驗收條件 | ✅「`./mvnw verify` 通過，新增邏輯皆有單元測試」 |
| 適當粒度 | 一個 Run 可完成，約 1–4 小時人工工作量 | ✅「一個 API 端點 + 測試」 |
| 結構化 | 使用固定段落 | 目標／技術要求／驗收條件／限制／參考 |
| 背景放對位置 | 長期規則放 Instructions、Skill 或 Project 描述，不在每個 Issue 重複 | ✅ Project 描述寫明技術棧與分支策略 |

**反例：**

```text
❌ 幫我寫一個使用者模組      → 太模糊
❌ 重構整個後端架構          → 太大，應拆子 Issue 並設 Stage
❌ 修個 Bug                  → 沒有重現步驟與預期行為
```

**Issue 描述範本：**

```markdown
## 目標
一句話說明要達成什麼、為什麼。

## 技術要求
- 框架／版本：Spring Boot 3.5、Java 21
- 架構：遵循既有分層（controller → service → repository）
- 介面：GET /api/v1/users/{id}，回傳 UserDTO

## 驗收條件
1. 找到時回 200 與 UserDTO（不含密碼欄位）
2. 找不到時回 404，錯誤格式符合 api-conventions Skill
3. 未授權時回 401
4. ./mvnw verify 通過

## 限制
- 不修改資料庫 Schema；不修改 CI 設定

## 參考
- src/main/java/com/example/user/User.java
- 既有範例：OrderController#getOrder
```

### 23.4 Agent 使用規範

| 規範 | 說明 |
| --- | --- |
| 人類審查必經 | Agent 產出必須經人類審查；以分支保護強制 PR 審查與 CI |
| 職責分離 | 實作、審查、資料庫變更、文件分屬不同 Agent |
| 安全邊界 | Agent 不可直接存取正式資料庫與正式環境憑證 |
| 任務粒度 | 單一 Issue 控制在一個 Run 可完成的範圍；大型工作拆子 Issue 與 Stage |
| 停止條件 | Agent 互相 @ 時，Instructions 要寫明何時停止，避免來回迴圈 |
| 成本控管 | 每週檢視 Analytics 的成本與錯誤分頁，找出高重試率的 Agent |
| 私密對話 | Chat 對話他人看不到，團隊需要的結論要寫回 Issue 或 Skill |
| 回顧 | 每個 Sprint 安排 15 分鐘「Agent 回顧」：檢視退回原因、更新 Instructions 與 Skill |

### 23.5 常見錯誤與對策

| 錯誤 | 原因 | 對策 |
| --- | --- | --- |
| Agent 產出品質低 | Issue 描述模糊、缺驗收條件 | 使用 23.3 範本；把慣例寫成 Skill |
| Run 逾時或停滯 | 任務太大；工具長時間無輸出 | 拆子 Issue；調整 Watchdog（第 6.11 節） |
| Issue 一直 queued | Runtime 離線或併發已滿 | 第 21.7 節 |
| 即時更新失效 | 代理未轉送 WebSocket；`FRONTEND_ORIGIN`／CORS 不符 | 第 5.6 節 |
| 分離網域無法寫入（403 CSRF） | 未設 `COOKIE_DOMAIN` | 改同源部署或設定最窄 `COOKIE_DOMAIN` |
| 升級後版本沒變 | 鎖定 `MULTICA_IMAGE_TAG`；Helm `IfNotPresent` | 第 22.3、22.4 節 |
| 驗證碼收不到 | DEV mode | 設定 SMTP／Resend |
| 指派了卻沒開始 | Issue 在 `backlog`；選了 Don't start yet | 移到 `todo` 或在評論中提出要求 |
| 自訂狀態下指派意外開始執行 | 自訂 `unstarted` 狀態不會停車 | 需要停車時用內建 `backlog` |
| Skill 匯入失敗 | 含二進位支援檔（Issue #1705） | Skill 附件以文字檔為主 |
| Daemon 無法啟動 | 沒有偵測到任何內建 AI 工具 | 確認 `claude`／`codex` 等在 `PATH` 且已登入 |
| 憑證外洩到日誌 | 把 Token 放在自訂參數或 Shell 指令 | 改用 `custom_env`（`--custom-env-file`）並輪替 |
| Bot 無回應 | 飛書設成請求網址；Slack 未邀請 Bot；Telegram 409 | 第 16 章各平台疑難 |

### 23.6 成效衡量指標

| 指標 | 計算方式 | 資料來源 |
| --- | --- | --- |
| Agent 交付量 | 每週由 Agent 移到 `in_review` 的 Issue 數 | `multica issue list` + `issue timeline` |
| 首次通過率 | `in_review` 後未被退回 `in_progress` 即 `done` 的比例 | Issue 時間軸 |
| 交付週期 | 指派 → `in_review` 的中位數時間 | Issue 時間軸 |
| Run 失敗率 | 失敗 Run ÷ 結束 Run，依 `failure_reason` 分類 | Analytics、`multica_agent_task_failed_total` |
| 每 Issue 成本 | Token 成本 ÷ 完成 Issue 數 | `multica issue usage`、Analytics |
| 排隊時間 | Run 排隊等待的 p90 | `multica_agent_task_queue_wait_seconds` |
| 人工介入率 | Agent 設為 `blocked` 或 @ 人類的比例 | Issue 時間軸、Squad activity |

> 💡 指標用來改善 Issue 品質、Instructions 與 Skill，而不是評比個人。初期建議只追蹤首次通過率、Run 失敗率與每 Issue 成本三項。

### 23.7 參與 Multica 開發的本機環境

以下內容摘自官方 `CONTRIBUTING.md`，適用於要修改 Multica 原始碼（例如內部客製或回饋上游）的團隊。

**前置條件：** Node.js 22、pnpm 10.28.2、Go 1.26.6、Docker。

**開發模型：** 一個共用的 PostgreSQL 容器、每個 checkout 一個資料庫；主 checkout 用 `.env`（`POSTGRES_DB=multica`），每個 Git worktree 用自己的 `.env.worktree`（資料庫名稱與前後端埠由路徑雜湊產生）。

```bash
make dev                 # 自動偵測主 checkout 或 worktree，建立 env、安裝依賴、建資料庫、跑 Migration、啟動所有服務
```

| 指令 | 用途 |
| --- | --- |
| `make db-up`／`make db-down` | 啟動／停止共用 PostgreSQL（保留 Volume） |
| `make setup`／`start`／`stop`／`check` | 目前 checkout 的設定、啟動、停止、驗證 |
| `make setup-main`／`start-main`／`stop-main`／`check-main` | 明確指定主 checkout |
| `make worktree-env` | 在 worktree 內產生 `.env.worktree`（`FORCE=1` 重新產生） |
| `make setup-worktree`／`start-worktree`／`stop-worktree`／`check-worktree` | 明確指定 worktree |
| `make test` | 執行測試 |
| `make build` | 編譯後端二進位 |
| `make migrate-up`／`migrate-down` | 資料庫 Migration |
| `make daemon` | 啟動本機 Daemon（開發用） |
| `make selfhost`／`selfhost-build`／`selfhost-stop` | 自架部署 |

```bash
# 功能分支以 worktree 開發
git worktree add ../multica-feature -b feat/my-change main
cd ../multica-feature
make dev
make check-worktree      # 推送前驗證
```

> ⚠️ **注意：** 不要把 `.env` 複製到 worktree 目錄——指令流程會優先讀 `.env`，worktree 可能因此意外連回主資料庫。提交貢獻即同意 Multica License 條件 2（貢獻依整份 Multica License 提交、可被原廠用於商業用途、原廠可調整授權），企業回饋上游前請先經法務確認。

---

## 第 24 章：實戰案例——企業 Web 系統交付

> **本章重點：** 以 Spring Boot + Vue 的「會員管理」功能為例，示範從 Workspace、Repo、Project、Agents、Skills、Squad，到分 Stage 的子 Issue、執行監控、PR 審查、CI 與 Autopilot 的完整流程。所有指令均對照 v0.6.1 CLI；ID 以 `<...>` 表示，需代入實際值。

### 24.1 案例概要

| 項目 | 內容 |
| --- | --- |
| 後端 | Spring Boot 3.5、Java 21、Flyway、PostgreSQL（Repo：`example/ent-api`） |
| 前端 | Vue 3 + TypeScript + Pinia（Repo：`example/ent-web`） |
| CI | GitHub Actions；分支保護要求 1 位審查與 CI 通過 |
| Multica | 自架（同源部署、SMTP、Redis），1 台專用 Runner（`multica-runner` 使用者，Claude Code 與 Codex） |
| 需求 | 會員查詢與編輯：新增 `member_profile` 資料表、`GET/PUT /api/v1/members/{id}`、前端個人資料頁 |

```mermaid
flowchart TB
    subgraph MC["Multica Workspace：Enterprise Web（前綴 EWEB）"]
        P["Project：會員管理<br/>Resources: ent-api, ent-web"]
        SQ["Squad：Web 交付<br/>Leader: delivery-lead"]
        A1["db-migration"]
        A2["be-impl"]
        A3["fe-impl"]
        A4["reviewer"]
        SQ --> A1
        SQ --> A2
        SQ --> A3
        SQ --> A4
    end
    subgraph RUN["Runner 主機（multica-runner）"]
        D["Daemon"] --> CC["Claude Code"]
        D --> CX["Codex"]
    end
    subgraph GH["GitHub"]
        R1["ent-api"]
        R2["ent-web"]
        CI["Actions CI"]
    end
    MC <-->|"WSS"| D
    CC -->|"push / PR"| R1
    CX -->|"push / PR"| R2
    R1 --> CI
    R2 --> CI
    GH -->|"PR / Checks 事件"| MC
```

### 24.2 步驟 1：環境就緒

依第 5 章完成自架部署，並依第 20.2 節以專用使用者啟動 Runner 上的 Daemon。確認：

```bash
curl -fsS https://multica.example.com/readyz
sudo -iu multica-runner multica daemon status
multica runtime list --output json        # 記下 Claude Code 與 Codex 兩個 Runtime 的 ID
```

Runner 主機上以機器帳號設定 GitHub 推送權限（Deploy Key 或 Fine-grained Token，第 17.7 節），並以 owner 身分在 **Settings → Code** 連接 GitHub App、開啟 Auto-link 與「PR 合併後移到 Done」。

### 24.3 步驟 2：Workspace、Repo 與 Project

```bash
multica workspace create --name "Enterprise Web" --slug enterprise-web --issue-prefix EWEB
multica workspace switch enterprise-web

multica repo add https://github.com/example/ent-api https://github.com/example/ent-web

multica project create \
  --title "會員管理" \
  --icon "👤" \
  --start-date 2026-10-06 --due-date 2026-10-31 \
  --repo https://github.com/example/ent-api \
  --repo https://github.com/example/ent-web
```

在 Web 的 Project 描述寫入所有相關 Issue 都需要的背景（此描述會進入每次 Run 的上下文）：

```markdown
## 背景
會員管理模組：後端 ent-api（Spring Boot 3.5 / Java 21），前端 ent-web（Vue 3 + TS）。

## 共通規範
- 分支：從 main 建立 eweb-<編號>-<簡述>，PR 標題以 Issue 編號開頭。
- API 錯誤格式、命名與分頁遵循 api-conventions Skill。
- Schema 變更只能由 db-migration 處理（Flyway，檔名 V<日期>__<描述>.sql）。
- 完成後在 Issue 留言：變更摘要、測試結果、風險；狀態設為 in_review。
```

### 24.4 步驟 3：Skills 與 Agents

先把公司 Skill Library（內部 Git Repo，見第 11.8 節）匯入：

```bash
multica skill import --url https://github.com/example/agent-skills/tree/main/api-conventions
multica skill import --url https://github.com/example/agent-skills/tree/main/write-db-migration
multica skill import --url https://github.com/example/agent-skills/tree/main/enterprise-code-review
multica skill list --output json
```

建立四個 Agent（Instructions 原文存在 `agents/*.md` 並納入版控）：

```bash
multica agent create --name db-migration --runtime-id <claude-runtime-id> \
  --description "Flyway schema 變更" \
  --instructions "$(cat agents/db-migration.md)" \
  --permission-mode public_to --public-to-workspace --max-concurrent-tasks 2

multica agent create --name be-impl --runtime-id <claude-runtime-id> \
  --description "Spring Boot API 實作" \
  --instructions "$(cat agents/be-impl.md)" \
  --permission-mode public_to --public-to-workspace

multica agent create --name fe-impl --runtime-id <codex-runtime-id> \
  --description "Vue 前端實作" \
  --instructions "$(cat agents/fe-impl.md)" \
  --permission-mode public_to --public-to-workspace

multica agent create --name reviewer --runtime-id <claude-runtime-id> \
  --description "PR 審查，不修改程式碼" \
  --instructions "$(cat agents/reviewer.md)" \
  --permission-mode public_to --public-to-workspace

multica agent create --name delivery-lead --runtime-id <claude-runtime-id> \
  --description "Web 交付 Squad Leader" \
  --instructions "$(cat agents/delivery-lead.md)" \
  --permission-mode public_to --public-to-workspace
```

綁定 Skills：

```bash
multica agent skills add <db-migration-id> --skill-ids <write-db-migration-id>
multica agent skills add <be-impl-id>      --skill-ids <api-conventions-id>
multica agent skills add <fe-impl-id>      --skill-ids <api-conventions-id>
multica agent skills add <reviewer-id>     --skill-ids <enterprise-code-review-id>
```

### 24.5 步驟 4：組成 Squad

```bash
multica squad create --name "Web 交付" --leader delivery-lead \
  --description "會員管理等 Web 功能的端到端交付"

multica squad member add <squad-id> --member-id <db-migration-id> --type agent --role "Flyway schema 變更"
multica squad member add <squad-id> --member-id <be-impl-id>      --type agent --role "後端 API 與單元測試"
multica squad member add <squad-id> --member-id <fe-impl-id>      --type agent --role "前端頁面與元件測試"
multica squad member add <squad-id> --member-id <reviewer-id>     --type agent --role "PR 審查"
multica squad member add <squad-id> --member-id <tech-lead-member-id> --type member --role "Tech Lead，Stage 間核准"

multica squad update <squad-id> --instructions "$(cat squads/web-delivery.md)"
```

`squads/web-delivery.md` 的重點：

```text
- 父 Issue 的子 Issue 依 Stage 推進：Stage 1 DB → Stage 2 API → Stage 3 前端。
- 某個 Stage 全部完成時，把下一個 Stage 的子 Issue 以
  multica issue status <id> todo 移出 backlog（這會觸發其 Assignee）。
- 每個子 Issue 開 PR 後，@reviewer 審查；reviewer 結論為「可合併」後 @Tech Lead。
- 全部子 Issue done 後，把父 Issue 設為 in_review。不要自己實作。
```

### 24.6 步驟 5：建立父 Issue 與分 Stage 的子 Issue

```bash
# 父 Issue：指派給 Squad
multica issue create --title "會員資料查詢與編輯" \
  --project <project-id> --priority high \
  --description-file specs/member-profile.md \
  --assignee "Web 交付" --status backlog

# Stage 1：DB（直接開始）
multica issue create --title "新增 member_profile 資料表" \
  --parent EWEB-1 --stage 1 --project <project-id> \
  --description-file specs/member-profile-db.md \
  --assignee db-migration --status todo

# Stage 2：API（先停在 backlog）
multica issue create --title "實作 GET/PUT /api/v1/members/{id}" \
  --parent EWEB-1 --stage 2 --project <project-id> \
  --description-file specs/member-profile-api.md \
  --assignee be-impl --status backlog

# Stage 3：前端（先停在 backlog）
multica issue create --title "會員個人資料頁" \
  --parent EWEB-1 --stage 3 --project <project-id> \
  --description-file specs/member-profile-web.md \
  --assignee fe-impl --status backlog

# 父 Issue 移出 backlog，喚醒 Leader
multica issue status EWEB-1 todo
```

`specs/member-profile-api.md` 依第 23.3 節範本撰寫（目標、技術要求、驗收條件、限制、參考）。由於 `--description-file` 預設只讀目前工作目錄內的檔案，請在 Repo 根目錄執行。

```mermaid
sequenceDiagram
    autonumber
    participant TL as Tech Lead
    participant L as delivery-lead
    participant DB as db-migration
    participant BE as be-impl
    participant FE as fe-impl
    participant RV as reviewer
    DB->>DB: Stage 1 實作 Flyway 並開 PR
    DB->>RV: 評論中提及 reviewer 審查
    RV-->>TL: 可合併，請 Tech Lead 核准
    TL->>TL: 合併 PR，EWEB-2 自動 Done
    L->>L: Stage 1 完成，Leader 被喚醒
    L->>BE: 把 EWEB-3 移到 todo（觸發 be-impl）
    BE->>RV: 開 PR 後請 reviewer 審查
    TL->>TL: 合併，EWEB-3 Done
    L->>FE: 把 EWEB-4 移到 todo
    FE->>RV: 開 PR 後請 reviewer 審查
    TL->>TL: 合併，EWEB-4 Done
    L->>TL: 父 Issue EWEB-1 設為 in_review
```

### 24.7 步驟 6：監控執行

```bash
multica issue children EWEB-1                      # 依 Stage 看子 Issue 進度
multica issue list --project <project-id> --output json --fields identifier,title,status,assignee_id
multica issue runs EWEB-3
multica issue run-messages <run-id> --issue EWEB-3 --since 0
multica issue timeline EWEB-1 --action status_changed
multica issue usage EWEB-1
```

需要在 Agent 執行中途補充指示時，直接在 Issue 回覆（Claude Code／Codex 支援 Steer，第 13.7 節）。

### 24.8 步驟 7：審查、CI 與合併

- 子 Issue 的 PR 標題以 `EWEB-3` 開頭，自動連結到 Issue；PR 卡片顯示 CI 與可合併性。
- reviewer 以 `enterprise-code-review` Skill 審查，結論寫在 Issue 評論；有 Blocker 時 @ be-impl 修正（同一討論串的回覆會路由回原 Agent）。
- be-impl 可建立 Wakeup 等 CI：`multica issue wakeup create EWEB-3 --until-pr checks --expires-in 2h --on-timeout wake --instruction-file ./ci-check.md`。
- Tech Lead 在 GitHub 合併後，「PR 合併後移到 Done」自動結案子 Issue，Stage 屏障喚醒 Leader 推進下一 Stage。
- CI 失敗時，第 17.8 節的 GitHub Actions 片段呼叫 Webhook Autopilot，由 Agent 分析並開 Issue。

### 24.9 步驟 8：日常自動化

```bash
multica autopilot create --title "Web 交付每日摘要" --agent delivery-lead \
  --mode create_issue --project <project-id> \
  --description "彙整昨日合併的 PR、blocked 的 Issue 與待審查項目，@ 相關負責人。" \
  --issue-title-template "Web 交付每日摘要 {{date}}" \
  --subscriber "Tech Lead"
multica autopilot trigger-add <autopilot-id> --kind schedule --cron "0 9 * * 1-5" --timezone Asia/Taipei
```

### 24.10 案例總結

| 面向 | 做法 | 效果 |
| --- | --- | --- |
| 上下文 | Project 描述 + Skills + Issue 範本 | Agent 不需在每個 Issue 重新理解慣例 |
| 順序控制 | 子 Issue Stage + `backlog` 停車 + Leader 推進 | DB → API → 前端依序進行，不會搶跑 |
| 品質 | reviewer Agent + 人類核准 + 分支保護 + CI | Agent 產出不會未經審查進入 `main` |
| 結案 | PR 合併自動移到 Done | 狀態與程式碼一致 |
| 可觀測 | 執行紀錄、時間軸、用量、每日摘要 | 進度與成本透明 |
| 安全 | 專用 Runner 使用者、機器帳號 Token、最小 Access | 爆炸半徑受控 |

**經驗教訓（📘）：**

1. **把 Stage 推進規則寫進 Squad Instructions**，並用內建 `backlog` 停車；若用 `unstarted` 類別的自訂狀態，子 Issue 一指派就會開始執行。
2. **Schema 變更獨立成 Agent 與 Stage**，避免 API 與 Migration 在同一 PR 中互相等待。
3. **Instructions 與 Skills 納入版控**，每次退回都回頭修正它們，而不是只在 Issue 中口頭糾正。
4. **先用 Codex／Claude Code 等支援 Steer 與 Session 續接的工具**承擔長任務，方便中途修正。
5. **每個 Sprint 檢視 `issue usage` 與失敗原因分佈**，高重試率通常代表 Issue 粒度過大或驗收條件不清。

---

## 附錄 A：檢查清單

### A.1 初次安裝清單

- [ ] 服務主機已安裝 Docker 與 Compose v2（`docker compose version`），埠 3000／8080 未被占用
- [ ] `make selfhost` 完成，`.env` 已產生 `JWT_SECRET`、PostgreSQL 密碼與 `MULTICA_VCS_SECRET_KEY`
- [ ] `curl -fsS http://localhost:8080/readyz` 回傳 `db` 與 `migrations` 皆為 ok
- [ ] 已取得登入驗證碼（Email 或後端日誌）並建立第一個 Workspace（slug 建立後不可改）
- [ ] 執行電腦已安裝並登入至少一種 AI 工具（`command -v claude` 等）
- [ ] 執行電腦已安裝 CLI 並完成 `multica setup self-host`
- [ ] `multica daemon status` 顯示 running、Agents 非空、Workspaces > 0
- [ ] Runtimes 頁顯示該電腦在線，已建立第一個 Agent 並完成一次 Run

### A.2 正式部署清單

- [ ] `APP_ENV=production`，`JWT_SECRET` 為 `openssl rand -hex 32` 產生的強隨機值
- [ ] 未設定 `MULTICA_DEV_VERIFICATION_CODE`
- [ ] 已設定 SMTP 或 Resend，啟動日誌顯示 `SMTP relay` 或 `Resend API`
- [ ] `FRONTEND_ORIGIN`、`MULTICA_APP_URL`、`MULTICA_PUBLIC_URL` 為正式網址；`/api/config` 的 `daemon_server_url` 不是 localhost
- [ ] 採同源部署；或分離網域時已設定最窄的 `COOKIE_DOMAIN`
- [ ] 反向代理已啟用 TLS，`/ws`、`/api/daemon/ws`、`/health` 導向後端並支援長連線
- [ ] `CORS_ALLOWED_ORIGINS`／`ALLOWED_ORIGINS` 只列實際來源
- [ ] 註冊管控：`ALLOW_SIGNUP=false`、`ALLOWED_EMAIL_DOMAINS`、建立共用 Workspace 後設 `DISABLE_WORKSPACE_CREATION=true`
- [ ] 已設定 `REDIS_URL`（驗證碼速率限制、多副本）
- [ ] `RATE_LIMIT_TRUSTED_PROXIES`、`MULTICA_TRUSTED_PROXIES` 只列真實代理 CIDR
- [ ] 附件使用持久化 Volume 或 S3；內網 S3 設 `ATTACHMENT_DOWNLOAD_MODE=proxy`
- [ ] 所有 `*_SECRET_KEY` 已納入機密管理並有備份
- [ ] `METRICS_ADDR` 綁內部介面並已接上 Prometheus；`/readyz` 已納入外部監控
- [ ] 遙測與分析政策已決定（`DO_NOT_TRACK`、`ANALYTICS_DISABLED`、`MULTICA_LLM_*`）
- [ ] 每日 PostgreSQL 備份（`pg_dump` 先寫檔再壓縮）並完成一次還原演練
- [ ] 正式環境鎖定 Release Tag（`MULTICA_IMAGE_TAG` 或 Helm `images.*.tag`）

### A.3 Agent 設定清單

- [ ] 名稱反映職責，描述說明擅長的工作
- [ ] Instructions 含職責、開工前檢查、可做／不可做、交付方式、何時停下來確認
- [ ] Instructions 原文已存入 Git 並走 PR 變更
- [ ] 選定 Runtime、模型與 Thinking Level；長任務優先選支援 Session 續接與 Steer 的工具
- [ ] Access 採最小範圍（預設 Only me）
- [ ] 併發上限符合 Runner 容量與 AI 工具額度
- [ ] `custom_env` 只含低權限、單一範圍憑證，以 `--custom-env-file` 設定
- [ ] 自訂參數不含任何憑證
- [ ] MCP 伺服器由 Workspace 函式庫管理並只指派給需要的 Agent
- [ ] 已綁定必要 Skills，未綁定來源不明的 Skill
- [ ] 以一個真實 Issue 驗證並檢視 Transcript

### A.4 升級驗收清單

- [ ] 已閱讀目標版本之間的 Changelog，特別是 Self-host 與 Migration 相關項目
- [ ] 升級前完成資料庫備份
- [ ] 確認 `MULTICA_IMAGE_TAG`／Helm `images.*.tag` 已改為目標版本（或 `pullPolicy: Always`）
- [ ] `git pull` 更新 Compose 檔後 `pull` + `up -d`；或 `helm upgrade`
- [ ] `/readyz` 回 HTTP 200 且 `db`、`migrations` 皆為 ok（不要只看 `/health`）
- [ ] 後端日誌沒有 Migration 錯誤（例如 `refusing to drop legacy daily rollups`）
- [ ] Web 可登入、可建立 Issue 與留言、即時更新正常（DevTools 看到 WS `101`）
- [ ] Runner 上的 Daemon 在線；必要時以 `multica runtime update` 或 `multica update` 升級 CLI
- [ ] 指派一個測試 Issue 完成一次 Run
- [ ] GitHub／自架 Git PR 連結與 CI 狀態正常；通訊 Bot 可回覆
- [ ] 若為 macOS Runner，處理升級後的 TCC 授權

### A.5 安全檢查清單

- [ ] Daemon 以專用使用者、容器或 VM 執行，不使用個人帳號
- [ ] Runner 使用者家目錄中沒有無關的正式環境憑證；SSH 使用專用 Deploy Key
- [ ] Git 推送使用機器帳號的最小權限 Token；`main` 有分支保護
- [ ] Compose 埠仍綁定 `127.0.0.1`，未直接暴露到公網
- [ ] 維護 API（`MAINTENANCE_PORT`）與 pprof 未暴露到任何 Service／Ingress
- [ ] Agent Access 每季盤點；離職人員的 PAT 已撤銷
- [ ] 外部 Skill 經內部審查後才匯入正式 Workspace
- [ ] Autopilot Webhook URL 未出現在 Repo、Issue 或截圖；外洩時已 Rotate
- [ ] `custom_env` 與 MCP 設定不含高價值長期憑證
- [ ] 已評估並設定遙測、PostHog 與伺服器端 LLM 的資料外流政策
- [ ] 私有 CA 以 `SSL_CERT_DIR` 信任，未關閉 TLS 驗證
- [ ] 已確認授權條件（內部使用 vs 對外提供服務）並保留 LICENSE／NOTICE

### A.6 日常維運清單

| 頻率 | 項目 |
| --- | --- |
| 每日 | 檢查 `/readyz` 告警、Run 失敗率、排隊時間；確認備份成功 |
| 每週 | 檢視 Analytics 成本與錯誤分頁；`multica daemon disk-usage --all-profiles` 檢查 Runner 磁碟；處理 Inbox 中的失敗通知 |
| 每兩週 | Staging 升級並執行 A.4 驗收 |
| 每月 | 正式環境升級；檢視 `sys_cron_executions` 與 Usage Rollup；更新 AI 工具版本 |
| 每季 | Agent／Skill／Access 盤點；還原演練；PAT 與 `*_SECRET_KEY` 管理檢查 |

---

## 附錄 B：CLI 快速參考卡

以 `multica 0.6.1` 的 `--help` 為準。全域旗標：`--server-url`、`--workspace-id`、`--profile`、`--debug`。

### B.1 連線與設定

```bash
multica setup                                   # 連 Cloud
multica setup self-host --server-url <api> --app-url <web>
multica login                                   # 瀏覽器登入
multica login --token                           # 貼上 PAT
multica auth status
multica auth logout                             # 只刪本機 Token
multica config show
multica config set <key> <value>                # 空字串清除
multica version --output json
multica update
multica user profile get
```

### B.2 Daemon 與 Runtime

```bash
multica daemon start [--foreground] [--max-concurrent-tasks N] [--no-auto-update]
multica daemon status --output json
multica daemon logs -f
multica daemon logs -n 200
multica daemon restart
multica daemon stop
multica daemon disk-usage --by-workspace
multica runtime list
multica runtime rename <runtime-id> "<name>"
multica runtime usage <runtime-id>
multica runtime activity <runtime-id>
multica runtime update <runtime-id> --target-version <version> --wait
multica runtime delete <runtime-id> --cascade
multica runtime profile list
multica runtime profile create --display-name "<name>" --command-name <cmd>
multica runtime profile set-path <profile-id> --path <abs-path>
```

### B.3 Workspace、成員與 MCP

```bash
multica workspace list
multica workspace get [<slug>]
multica workspace switch <slug>
multica workspace create --name "<name>" --slug <slug> --issue-prefix <PREFIX>
multica workspace member list
multica workspace member invite <email> --role admin
multica workspace mcp list
multica workspace mcp add --server-config-file <file.json>
multica workspace mcp remove <server-id>
```

### B.4 Issue

```bash
multica issue list --status in_progress --assignee "<name>" --output json
multica issue list --property "Severity=Critical" --sort property:Severity
multica issue get MUL-123
multica issue search "<query>" --include-closed
multica issue create --title "<title>" --description-file <file> --assignee "<agent>" --project <id>
multica issue create --title "<title>" --parent MUL-100 --stage 2
multica issue update MUL-123 --priority urgent
multica issue assign MUL-123 --to "<agent>" [--no-start]
multica issue assign MUL-123 --unassign
multica issue status MUL-123 in_review
multica issue status MUL-120 cancelled --duplicate-of MUL-100
multica issue children MUL-100
multica issue pull-requests MUL-123
multica issue timeline MUL-123 --action status_changed
multica issue reorder --help
```

### B.5 評論、訂閱、標籤、屬性與 Metadata

```bash
multica issue comment list MUL-123 --tail 20
multica issue comment add MUL-123 --content-file <file>
multica issue comment add MUL-123 --parent <comment-id> --content "<text>"
multica issue comment update <comment-id> --expected-revision <n> --content-file <file>
multica issue comment resolve <comment-id>
multica issue comment delete <comment-id>
multica issue subscriber add MUL-123 --user "<name>"
multica issue subscriber list MUL-123
multica issue label add --help
multica issue property set MUL-123 --name Severity --value Critical
multica issue property unset --help
multica issue metadata set MUL-123 --key team --value backend
multica issue metadata list MUL-123
multica label create --name "<name>" --color "#3b82f6" --resource-type issue
multica property create --name Severity --type select --option "Critical:#ef4444"
```

### B.6 Run 與 Wakeup

```bash
multica issue runs MUL-123
multica issue run-messages <run-id> --issue MUL-123 --since <seq>
multica issue usage MUL-123
multica issue cancel-task <run-id> --issue MUL-123
multica issue rerun MUL-123
multica issue wakeup events
multica issue wakeup create MUL-123 --until-pr checks --expires-in 2h --instruction-file <file>
multica issue wakeup list MUL-123
multica agent tasks <agent-id> --limit 200
```

### B.7 Project 與 Repo

```bash
multica project list
multica project create --title "<title>" --repo <git-url> --lead "<name>"
multica project status <project-id> in_progress
multica project resource list <project-id>
multica project resource add <project-id> --type github_repo --url <git-url> --ref main
multica project resource add <project-id> --type local_directory --local-path <abs> --daemon-id <id> --execution-mode worktree
multica project resource remove <project-id> <resource-id>
multica repo list
multica repo add <git-url>
multica repo checkout <git-url> --ref <ref>
```

### B.8 Agent、Skill 與 Squad

```bash
multica agent list --output json
multica agent get <agent-id>
multica agent create --name <name> --runtime-id <id> --instructions "<text>"
multica agent update <agent-id> --model <model> --thinking-level high
multica agent copy <agent-id> --runtime-id <id> --model <model>
multica agent archive <agent-id>
multica agent restore <agent-id>
multica agent env get <agent-id>
multica agent env set <agent-id> --custom-env-file <file.json>
multica agent skills add <agent-id> --skill-ids <skill-id>
multica agent mcp add <agent-id> <server-id>
multica skill list
multica skill import --url <url> --on-conflict rename
multica skill import --file <file.skill>
multica skill refresh <skill-id>
multica skill files list <skill-id>
multica squad create --name "<name>" --leader <agent>
multica squad member add <squad-id> --member-id <id> --type agent --role "<role>"
multica squad update <squad-id> --instructions "<text>"
```

### B.9 Autopilot

```bash
multica autopilot list
multica autopilot create --title "<title>" --agent <agent> --mode create_issue
multica autopilot trigger-add <autopilot-id> --kind schedule --cron "0 9 * * 1-5" --timezone Asia/Taipei
multica autopilot trigger-add <autopilot-id> --kind webhook
multica autopilot trigger-update <autopilot-id> <trigger-id> --enabled=false
multica autopilot trigger-rotate-url <autopilot-id> <trigger-id>
multica autopilot trigger <autopilot-id>
multica autopilot runs <autopilot-id>
multica autopilot update <autopilot-id> --status paused
multica autopilot get <autopilot-id> --show-secrets
```

### B.10 舊版指令對照

| 舊版手冊（v0.3.33） | v0.6.1 |
| --- | --- |
| `multica workspace members` | `multica workspace member list` |
| `multica workspace watch <id>`／`unwatch` | 已移除；Daemon 自動為可連接的 Workspace 註冊 Runtime |
| `multica autopilot enable`／`disable` | `multica autopilot update <id> --status active\|paused`；單一 Trigger 用 `trigger-update --enabled` |
| `multica --profile staging setup ...` | `multica setup self-host --profile staging ...`（`--profile` 為全域旗標，位置不限） |
| （無） | 新增 `chat`、`label`、`property`、`repo`、`squad`、`attachment`、`user`、`issue wakeup`、`issue timeline`、`workspace mcp`、`agent mcp` 等 |

---

## 附錄 C：支援的 Agent CLI 對照

依 v0.6.1 README、`providers.mdx`、`install-agent-runtime.mdx` 與 `server/internal/daemon` 原始碼整理。「—」表示不支援或不提供；「未列」表示官方文件未說明。

| 工具 | 偵測指令 | Skill 注入路徑 | Session 續接 | Multica 管理 MCP | 路徑變數 | 模型變數 | 全機預設參數 |
| --- | --- | --- | :---: | :---: | --- | --- | --- |
| Claude Code | `claude` | `.claude/skills/` | ✓ | ✓ | `MULTICA_CLAUDE_PATH` | `MULTICA_CLAUDE_MODEL` | `MULTICA_CLAUDE_ARGS` |
| OpenAI Codex | `codex` | `$CODEX_HOME/skills/`（每次 Run 專屬） | ✓ | ✓ | `MULTICA_CODEX_PATH` | `MULTICA_CODEX_MODEL` | `MULTICA_CODEX_ARGS` |
| Cursor Agent | `cursor-agent` | `.cursor/skills/` | ✓ | ✓ | `MULTICA_CURSOR_PATH` | `MULTICA_CURSOR_MODEL` | — |
| GitHub Copilot CLI | `copilot` | `.github/skills/` | ✓ | — | `MULTICA_COPILOT_PATH` | `MULTICA_COPILOT_MODEL`（依帳號權限，可能不生效） | — |
| Antigravity | `agy` | `.agents/skills/` | ✓ | — | `MULTICA_ANTIGRAVITY_PATH` | `MULTICA_ANTIGRAVITY_MODEL` | — |
| OpenCode | `opencode` | `.opencode/skills/` | ✓ | ✓ | `MULTICA_OPENCODE_PATH` | `MULTICA_OPENCODE_MODEL` | — |
| OpenClaw | `openclaw` | 工作目錄下 `skills/` | ✓ | ✓ | `MULTICA_OPENCLAW_PATH` | `MULTICA_OPENCLAW_MODEL` | — |
| Hermes | `hermes` | 每次 Run 專屬 `HERMES_HOME/skills/` | ✓ | ✓ | `MULTICA_HERMES_PATH` | `MULTICA_HERMES_MODEL` | — |
| Pi | `pi` | `.pi/skills/` | ✓ | — | `MULTICA_PI_PATH` | `MULTICA_PI_MODEL` | — |
| Oh-My-Pi | `omp` | `.omp/skills/` | ✓ | ✓ | `MULTICA_OMP_PATH` | 未列 | — |
| Kimi CLI | `kimi` | `.kimi/skills/` | ✓ | ✓ | `MULTICA_KIMI_PATH` | `MULTICA_KIMI_MODEL` | — |
| Kiro CLI | `kiro-cli` | `.kiro/skills/` | ✓ | ✓ | `MULTICA_KIRO_PATH` | `MULTICA_KIRO_MODEL` | — |
| Grok Build | `grok` | `.grok/skills/` | ✓ | ✓ | `MULTICA_GROK_PATH` | `MULTICA_GROK_MODEL` | — |
| Qwen Code | `qwen` | `.qwen/skills/` | ✓ | ✓ | `MULTICA_QWEN_PATH` | `MULTICA_QWEN_MODEL` | `MULTICA_QWEN_ARGS` |
| QwenPaw | `qwenpaw` | 每次 Run 工作區 `skills/` | ✓ | ✓ | `MULTICA_QWENPAW_PATH` | —（工具自身設定） | `MULTICA_QWENPAW_ARGS` |
| Qoder CLI | `qodercli` | `.qoder/skills/` | ✓ | ✓ | `MULTICA_QODER_PATH` | `MULTICA_QODER_MODEL` | — |
| Qoder CN CLI | `qoderclicn` | `.qoder/skills/` | ✓ | ✓ | `MULTICA_QODERCLICN_PATH` | `MULTICA_QODERCLICN_MODEL` | — |
| Trae CLI | `traecli` | `.traecli/skills/` | ✓ | ✓ | `MULTICA_TRAECLI_PATH` | `MULTICA_TRAECLI_MODEL` | — |
| CodeBuddy | `codebuddy` | `.codebuddy/skills/` | ✓ | ✓ | `MULTICA_CODEBUDDY_PATH` | `MULTICA_CODEBUDDY_MODEL` | `MULTICA_CODEBUDDY_ARGS` |
| Huawei Cloud CodeArts | `codearts` | `.codeartsdoer/skills/` | ✓ | ✓ | `MULTICA_CODEARTS_PATH` | `MULTICA_CODEARTS_MODEL` | — |
| DevEco Code | `deveco` | `.deveco/skills/` | ✓ | — | `MULTICA_DEVECO_PATH` | `MULTICA_DEVECO_MODEL` | — |
| DeepSeek Harness | `dsh` | `.dsh/skills/` | ✓ | ✓ | `MULTICA_DSH_PATH` | `MULTICA_DSH_MODEL`（`provider/model`） | — |
| MiniMax Code | `mcode` | `.minimax/skills/` | — | ✓ | `MULTICA_MCODE_PATH` | —（工具自身設定） | — |
| Reasonix | `reasonix` | `.reasonix/skills/` | ✓ | ✓ | `MULTICA_REASONIX_PATH` | `MULTICA_REASONIX_MODEL` | — |
| Dim | `dim` | — | ✓ | ✓ | `MULTICA_DIM_PATH` | `MULTICA_DIM_MODEL` | — |
| ZeroClaw | `zeroclaw` | 未列 | 未列 | 未列 | `MULTICA_ZEROCLAW_PATH` | —（Agent Profile 決定） | — |

**最低版本**（低於此版本 Daemon 不註冊該 Runtime）：Antigravity 1.1.10、Claude Code 2.0.0、Codex 0.100.0、Copilot 1.0.0、Grok 0.2.89、Qwen Code 0.20.0、MiniMax Code 0.1.2、OpenCode 1.1.54。

**Steer（執行中補充指示）：** Claude Code、Codex、Grok（v0.6.1 README）。

**其他工具專屬變數：** `MULTICA_OPENCLAW_CLI_TIMEOUT`、`MULTICA_OPENCODE_IDLE_WATCHDOG`、`MULTICA_CODEX_SEMANTIC_INACTIVITY_TIMEOUT`、`MULTICA_CODEX_FIRST_TURN_TIMEOUT`、`MULTICA_CODEX_HANDSHAKE_TIMEOUT`、`MULTICA_CODEX_TURN_INTERRUPT_TIMEOUT`、`MULTICA_DSH_PROFILE_BUNDLE`、`MULTICA_DSH_PLUGIN_PATH`（見第 6.11 節）。

---

## 附錄 D：參考資源

### D.1 官方資源

| 資源 | 連結 |
| --- | --- |
| GitHub Repository | <https://github.com/multica-ai/multica> |
| 官方網站／Multica Cloud | <https://multica.ai> |
| 官方文件（英、簡中、日、韓、法） | <https://multica.ai/docs> |
| Changelog | <https://multica.ai/changelog> |
| Desktop 下載 | <https://multica.ai/download> |
| GitHub Releases（CLI、Desktop、`checksums.txt`） | <https://github.com/multica-ai/multica/releases> |
| Self-Hosting Guide | <https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md> |
| Self-Hosting Advanced | <https://github.com/multica-ai/multica/blob/main/SELF_HOSTING_ADVANCED.md> |
| Self-Hosting for AI Agents | <https://github.com/multica-ai/multica/blob/main/SELF_HOSTING_AI.md> |
| CLI and Daemon Guide | <https://github.com/multica-ai/multica/blob/main/CLI_AND_DAEMON.md> |
| CLI Install | <https://github.com/multica-ai/multica/blob/main/CLI_INSTALL.md> |
| Contributing Guide | <https://github.com/multica-ai/multica/blob/main/CONTRIBUTING.md> |
| Vision | <https://github.com/multica-ai/multica/blob/main/VISION.md> |
| License／Notice | <https://github.com/multica-ai/multica/blob/main/LICENSE>・<https://github.com/multica-ai/multica/blob/main/NOTICE> |
| Helm Chart 原始碼 | <https://github.com/multica-ai/multica/tree/main/deploy/helm/multica> |
| Multica CLI Skill | <https://github.com/multica-ai/multica-cli> |
| DeepSeek Harness Runtime Bridge | <https://github.com/multica-ai/dsh-multica-runtime> |
| 商業授權洽詢 | <https://www.multica.ai/contact-sales> |
| Discord | <https://discord.gg/W8gYBn226t> |
| X | <https://x.com/MulticaAI> |

### D.2 官方文件頁面對照

| 本手冊章節 | 官方文件頁面 |
| --- | --- |
| 第 2 章 | [Core concepts](https://multica.ai/docs/concepts)・[How Multica works](https://multica.ai/docs/how-multica-works) |
| 第 4 章 | [Quickstart](https://multica.ai/docs/cloud-quickstart)・[Tutorial](https://multica.ai/docs/tutorial) |
| 第 5 章 | [Self-host quickstart](https://multica.ai/docs/self-host-quickstart) |
| 第 6 章 | [Environment variables](https://multica.ai/docs/environment-variables) |
| 第 7 章 | [Auth setup](https://multica.ai/docs/auth-setup)・[Auth tokens](https://multica.ai/docs/auth-tokens) |
| 第 8 章 | [Workspaces](https://multica.ai/docs/workspaces)・[Members and roles](https://multica.ai/docs/members-roles) |
| 第 9 章 | [Issues](https://multica.ai/docs/issues)・[Projects](https://multica.ai/docs/projects)・[Project resources](https://multica.ai/docs/project-resources) |
| 第 10 章 | [Agents](https://multica.ai/docs/agents)・[Create an agent](https://multica.ai/docs/agents-create) |
| 第 11 章 | [Skills](https://multica.ai/docs/skills) |
| 第 12 章 | [Squads](https://multica.ai/docs/squads) |
| 第 13 章 | [Triggering agents](https://multica.ai/docs/triggering-agents)・[Assigning issues](https://multica.ai/docs/assigning-issues)・[Comments](https://multica.ai/docs/comments)・[Mentioning agents](https://multica.ai/docs/mentioning-agents)・[Chat](https://multica.ai/docs/chat)・[Inbox](https://multica.ai/docs/inbox) |
| 第 14 章 | [Runs](https://multica.ai/docs/tasks)・[Daemon and runtimes](https://multica.ai/docs/daemon-runtimes)・[Install an agent runtime](https://multica.ai/docs/install-agent-runtime)・[Providers](https://multica.ai/docs/providers) |
| 第 15 章 | [Autopilots](https://multica.ai/docs/autopilots) |
| 第 16 章 | [Channels](https://multica.ai/docs/channels)・[Slack](https://multica.ai/docs/slack-bot-integration)・[Lark](https://multica.ai/docs/lark-bot-integration)・[DingTalk](https://multica.ai/docs/dingtalk-bot-integration)・[Telegram](https://multica.ai/docs/telegram-bot-integration)・[Community-maintained](https://multica.ai/docs/community-maintained) |
| 第 17 章 | [GitHub integration](https://multica.ai/docs/github-integration)・[Self-hosted Git](https://multica.ai/docs/vcs-integration) |
| 第 18 章 | [Desktop app](https://multica.ai/docs/desktop-app)・[Mobile app](https://multica.ai/docs/mobile-app) |
| 第 19 章 | [CLI](https://multica.ai/docs/cli) |
| 第 20 章 | [Security model](https://multica.ai/docs/security-model) |
| 第 21 章 | [Troubleshooting](https://multica.ai/docs/troubleshooting) |
| 第 23.7 節 | [Contributing](https://multica.ai/docs/developers/contributing)・[Architecture](https://multica.ai/docs/developers/architecture) |

### D.3 AI 編碼工具官方安裝文件

| 工具 | 連結 |
| --- | --- |
| Claude Code | <https://code.claude.com/docs/en/quickstart> |
| Codex CLI | <https://developers.openai.com/codex/cli/> |
| GitHub Copilot CLI | <https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli> |
| Cursor CLI | <https://docs.cursor.com/en/cli/installation> |
| Antigravity CLI | <https://antigravity.google/docs/cli-install> |
| OpenCode | <https://opencode.ai/en/docs> |
| Kiro CLI | <https://kiro.dev/docs/cli/installation/> |
| Kimi CLI | <https://github.com/MoonshotAI/kimi-cli> |
| Qwen Code | <https://github.com/QwenLM/qwen-code> |
| Grok Build | <https://docs.x.ai/build/overview> |

其他工具（CodeBuddy、CodeArts、DevEco、DeepSeek Harness、Hermes、MiniMax Code、OpenClaw、Pi、Oh-My-Pi、Qoder、QwenPaw、Reasonix、TRAE、Dim）的連結見官方 [Install an agent runtime](https://multica.ai/docs/install-agent-runtime)。

### D.4 舊版手冊連結稽核

| 舊版連結 | 狀態（2026-10-05） | 處理 |
| --- | --- | --- |
| `https://multica.ai/app`（Multica Cloud） | 官方 README 與文件改以 `https://multica.ai` 作為 Cloud 入口 | 改為 multica.ai |
| `https://docs.anthropic.com/en/docs/claude-code` | Multica 官方安裝文件改指向 Claude Code 新文件站 | 改為 `code.claude.com/docs/en/quickstart` |
| `https://github.com/openai/codex` | 有效；官方安裝文件改指向 Codex CLI 文件頁 | 改為 developers.openai.com |
| GitHub 原始碼文件（SELF_HOSTING 等） | 有效 | 保留並補 VISION、LICENSE、NOTICE |
| Discord、X | 有效 | 保留 |
| 舊版未列 | — | 新增 multica.ai/docs、changelog、download、multica-cli、contact-sales |

---

## 附錄 E：版本歷程與更正紀錄

### E.1 v0.3.33 → v0.6.1 重大變更摘要

依官方 Changelog（v0.3.34–v0.6.1，2026-07-01 至 10-01，共 61 個 Release）依主題整理：

| 主題 | 變更 | 版本 |
| --- | --- | --- |
| **Agent Runtime** | 新增 TRAE CLI、DevEco Code、Grok、Qwen Code、Reasonix、QwenPaw、Oh-My-Pi、DeepSeek Harness、MiniMax Code、ZeroClaw、Huawei Cloud CodeArts、Qoder CN 等，總數達 26 種 | v0.3.34–v0.4.37 |
| | Qoder、Trae CLI 可作為自訂 Runtime Profile 基底 | v0.3.39 |
| | 啟動後才安裝的 CLI 自動出現、不需重啟 Daemon | v0.4.14 |
| | 刪除 Runtime 保留 Agent，可改指向其他機器 | v0.4.17 |
| | Claude Code 模型探索只列出可執行的模型 | v0.4.38 |
| **Agent 設定** | 對話式建立 Agent（Build with AI）、DM 按鈕、Agent 可傳送圖片與檔案 | v0.4.0 |
| | Agent Access 範圍（列表篩選與批次編輯）、顯示每次 Run 的觸發成員 | v0.4.2 |
| | 逐 Agent 開關 Skill | v0.4.8 |
| | Codex Fast 模式、Thinking Level 與 Service Tier | v0.4.9–v0.4.13 |
| | Agent 擁有者可檢視與更新環境變數、批次貼上環境變數 | v0.4.14、v0.4.24 |
| | Workspace MCP 伺服器函式庫、MCP 改名與連線替換 | v0.4.27、v0.4.40 |
| | Conversation Starters（最多 3 個） | v0.4.35 |
| **Issue 與 Project** | 自訂 Issue 欄位（屬性）、標籤管理、Project 起訖日期 | v0.4.0–v0.4.2 |
| | 可自訂欄位的 Issue Table、儲存檢視（Saved Views） | v0.4.5、v0.4.22 |
| | 評論轉子 Issue、自訂 Issue 狀態開放所有 Workspace | v0.4.34 |
| | 屬性篩選（包含、範圍、未填值） | v0.4.36–v0.4.39 |
| | 評論／描述標註（Annotations） | v0.4.43 |
| | 狀態設定依生命週期類別分組、可拖曳排序 | v0.4.44 |
| | Issue Wakeup 規則、評論永久連結、Project 起始分支 | v0.5.1 |
| | Steer 執行中的 Claude Code／Codex、重複 Issue 標記 | v0.5.2 |
| | 條件式 Wakeup v2、即時搜尋、交付物與附件預覽、Run 時間軸 | v0.6.0 |
| | 累積成本曲線、CLI `--duplicate-of` | v0.6.1 |
| **協作** | Chat 獨立分頁、自動標題 | v0.3.42 |
| | Chat 訊息佇列、一鍵追問建議、Project-aware Chat | v0.4.10–v0.4.19 |
| | Agent Run 顯示在評論串內、各評論串獨立排隊、討論串大綱 | v0.4.42 |
| | Inbox 封存檢視、篩選、標為未讀 | v0.4.3–v0.4.35 |
| **整合** | Slack `/issue` 斜線指令 | v0.3.34 |
| | 自架 Git（Forgejo、Gitea、GitLab） | v0.4.10 |
| | PR 卡片顯示即時 CI 與可合併性；從 GitHub App 匯入多個 Repo | v0.4.12–v0.4.13 |
| | 釘釘 Bot、企業微信 Bot、Telegram Bot | v0.4.20、v0.4.21、v0.4.25 |
| | 所有通道支援 `/new`、`/clear` | v0.4.35 |
| | Telegram 媒體雙向傳送 | v0.5.3 |
| **Apps** | Desktop 自動更新、Intel Mac、Windows／Linux；Issue 獨立視窗 | v0.4.1–v0.4.3 |
| | iPad 原生支援、行動版簡體中文 | v0.4.37、v0.5.3 |
| | 法文介面與文件 | v0.5.0、v0.5.3 |
| **Self-host 與維運** | Helm 外部 PostgreSQL；即時事件 5 分鐘重播視窗 | v0.3.36 |
| | S3 path-style 定址 | v0.3.35 |
| | 指定各元件執行節點；任務工作區放到任意磁碟 | v0.4.3、v0.4.26 |
| | Daemon 流量可導向獨立伺服器、可設定排隊保留時間 | v0.4.33 |
| | 搜尋記憶體上限（`DATABASE_SEARCH_WORK_MEM_MB`） | v0.4.41 |
| | Redis Cluster 與 Serverless Redis | v0.4.43 |
| | 匿名部署遙測（`DO_NOT_TRACK=1` 關閉） | v0.4.44 |
| | Session 滑動續期（不再固定 30 天登出） | v0.5.0 |
| | 自架可指向 Gitea 或相容鏡像取得更新 | v0.5.1 |
| | 自架信任自有 CA | v0.5.3 |
| **安全** | 私有 Agent 只能由擁有者執行；Provider 指令日誌不再暴露憑證或 Prompt | v0.4.30 |
| | 他人的私有 Runtime 無法經 API／CLI 使用 | v0.4.26 |
| | Autopilot 排程與 Webhook 以 Trigger 建立者的權限執行 | v0.4.39 |
| | 通道拒絕無權執行該 Agent 的成員發起的回合 | v0.6.0 |
| **授權** | 授權明確說明：免費公開託管仍需商業授權 | v0.4.17 |

### E.2 手冊版本與章節對照

| 手冊版本 | 日期 | 產品基準 | 說明 |
| --- | --- | --- | --- |
| v0.3.33（舊版標示） | 2026-06-30 | Multica v0.3.33 | 17 章 + 附錄 A–C；手冊版本號與產品版本號混用 |
| **v2.0** | 2026-10-05 | Multica v0.6.1 | 全面重新編排為 24 章 + 附錄 A–G；手冊版本號與產品版本號分離 |

| 舊版章節 | v2.0 對應 |
| --- | --- |
| 第 1 章 概述 | 第 1 章（新增外部評測對照、授權條件細節、變更速覽） |
| 第 2 章 系統架構 | 第 3 章（新增第 2 章核心概念） |
| 第 3 章 安裝與部署 | 第 5 章（部署）、第 6 章（環境變數）、第 7 章（認證）、第 21.4 節（Rollup） |
| 第 4 章 核心運作機制 | 第 2、9、13、14 章 |
| 第 5 章 AI Agent 整合 | 第 10 章（Agent）、第 14.3–14.4 節（工具）、附錄 C |
| 第 6 章 開發流程 | 第 13、17、24 章 |
| 第 7 章 Skill 機制 | 第 11 章（改寫為 `SKILL.md` 模型） |
| 第 8 章 多工作空間 | 第 8 章、第 6.11 節（GC）、第 19.4 節（Profile） |
| 第 9 章 Squads | 第 12 章 |
| 第 10 章 Autopilots | 第 15 章 |
| 第 11 章 Projects | 第 9.8–9.9 節 |
| 第 12 章 MCP 整合 | 第 10.8 節（改寫）、第 19.9 節 |
| 第 13 章 系統維運 | 第 21 章 |
| 第 14 章 升級與擴展 | 第 22 章 |
| 第 15 章 安全設計 | 第 20 章 |
| 第 16 章 最佳實務 | 第 23 章 |
| 第 17 章 實戰案例 | 第 24 章 |
| 附錄 A／B／C | 附錄 A／B／G |
| — | **新增**：第 4 章快速入門、第 16 章通訊整合、第 18 章 Desktop／Mobile、附錄 C、D、E、F |

### E.3 更正表

| # | 舊版內容 | 問題 | v2.0 更正 | 依據 |
| --- | --- | --- | --- | --- |
| 1 | 版本 v0.3.33、101 個 Release、38,600 Stars | 過時 | v0.6.1；61 個 Release（07-01 至 10-01）；約 52,000 Stars | GitHub API、Releases |
| 2 | 授權「Multica Source Available License」，非 SaaS／轉售可自由使用 | 名稱與條件不精確 | Multica License＝Apache 2.0 + Part I；對外公開實例即使免費也需商業授權；UI 品牌不可移除；非介面使用需署名 | LICENSE、NOTICE |
| 3 | PostgreSQL 17 + pgvector，pgvector 用於 Skill 語義搜尋 | 錯誤 | 不使用 pgvector；必要擴充 `pgcrypto`、`pg_trgm`；映像名稱為歷史因素 | SELF_HOSTING_ADVANCED |
| 4 | 支援 13 種以上 Agent，含 Gemini | 過時且含錯誤 | 26 種 CLI；Gemini 不在官方清單 | README、providers |
| 5 | Skill 以 `skills-lock.json` 定義，YAML 含 `triggers`／`steps` | 虛構格式 | `SKILL.md` + 支援檔案；匯入、`skill refresh`、綁定 Agent | skills.mdx |
| 6 | 「每個解決方案自動轉化為可重用 Skill」 | 誇大 | Skill 由成員建立、匯入或從 Runtime 複製 | skills.mdx |
| 7 | Multica 作為 MCP Provider，IDE 可透過 MCP 查詢 Issue | 無依據 | MCP 是提供給 Agent 所用 AI 工具的設定；外部工具操作 Multica 用 CLI／CLI Skill | agents-create、cli.mdx |
| 8 | `multica workspace watch`／`unwatch`／`members` | 指令不存在 | `workspace member list`；Daemon 自動註冊 | CLI 0.6.1 `--help` |
| 9 | `multica autopilot enable`／`disable` | 指令不存在 | `autopilot update --status`、`trigger-update --enabled` | CLI 0.6.1 `--help` |
| 10 | 約 30 個環境變數（`REDIS_TLS_ENABLED`、`DB_POOL_*`、`COOKIE_SECURE`、`COOKIE_SAMESITE`、`S3_ENDPOINT`、`S3_FORCE_PATH_STYLE`、`S3_ACCESS_KEY_ID`、`SMTP_TLS_MODE`、`HTTP_CLIENT_TIMEOUT`、`OTEL_EXPORTER_OTLP_ENDPOINT`、`MULTICA_USAGE_ROLLUP_*`、`MULTICA_GEMINI_*`、`MULTICA_AGY_*`、`MULTICA_CURSOR_AGENT_*`、`MULTICA_KIRO_CLI_*`、多個 `MULTICA_*_ARGS`） | 原始碼中不存在 | 以官方 environment-variables 為準重寫第 6 章；`*_ARGS` 只有 5 種工具支援 | 原始碼 grep、environment-variables.mdx |
| 11 | Redis 用於 Session 與 Rate Limiting 快取 | 不完整 | 即時事件 relay、共享速率限制、通訊 Bot 租約、Token 快取；驗證碼速率限制需要 Redis | environment-variables |
| 12 | Health Check 回傳含 `"redis":"ok"` | 錯誤 | `/health` 存活；`/readyz`／`/healthz` 回 `db` 與 `migrations` | SELF_HOSTING_ADVANCED |
| 13 | `METRICS_ADDR=:9090`，「社群 Dashboard ID 待發布」 | 安全建議不足、內容空泛 | 建議綁 `127.0.0.1:9090`；列出實際指標名稱與標籤；提供告警規則範例 | 原始碼 `internal/metrics` |
| 14 | Desktop 僅 macOS；行動版 iOS | 過時 | Desktop macOS／Windows／Linux；iOS（含 iPad）需自行建置；無 Android | desktop-app、mobile-app |
| 15 | 手動部署 Node.js 20+、pnpm 10.28+、Go 1.26+ | 不精確 | Node.js 22、pnpm 10.28.2、Go 1.26.6 | SELF_HOSTING_ADVANCED |
| 16 | `multica daemon status` 輸出範例（`claude (v1.5.0)` 等） | 虛構輸出 | 改為官方描述的欄位（Daemon running、Agents、Workspaces） | self-host-quickstart |
| 17 | 術語「Magic Link」 | 不符實際 | Email 6 位數驗證碼（10 分鐘有效） | auth-setup |
| 18 | PAT 有效期 90 天 | 不完整 | 可選 30／90／365 天或永不過期；CLI 登入建立 90 天並在剩 7 天時自動續期 | auth-tokens |
| 19 | 「8.4 權限控管（RBAC）」 | 未區分角色與 Agent Access | owner／admin／member 權限矩陣 + Agent Access 三種範圍 + 私有／公開 Runtime | members-roles、agents |
| 20 | Workspace GC 參數 | 不完整 | 補齊 12 個 `MULTICA_GC_*` 與 Cloud／自架預設差異 | CLI_AND_DAEMON |
| 21 | 舊版 HA 架構與監控架構圖 | 缺乏依據 | 改為依官方多副本、Redis relay、資料庫連線預算建議的參考架構，並標示 📘 | SELF_HOSTING_ADVANCED、environment-variables |
| 22 | Issue 狀態僅列內建 | 過時 | 4 種生命週期類別、自訂狀態規則（不繼承停車行為） | issues.mdx |
| 23 | 實戰案例中的 CLI 與流程 | 部分指令不存在 | 全部改用 v0.6.1 指令；加入 Stage、Squad、Wakeup、PR 驅動結案 | CLI 0.6.1 `--help` |
| 24 | 授權允許表「提供 SaaS 禁止」 | 不完整 | 補充：嵌入商業產品、公開免費實例皆需授權；品牌豁免與商業授權分開申請 | LICENSE 1(a)–(d) |
| 25 | Usage Rollup「v0.3.20 起」 | 版本無法佐證 | 以 MUL-2957 描述，並補充多副本與 advisory lock 4246 | SELF_HOSTING |
| 26 | 參考資源 `multica.ai/app`、`docs.anthropic.com` | 過時 | 見附錄 D.4 | 官方文件 |
| 27 | 目錄缺少附錄錨點、部分舊錨點與標題不一致 | 格式 | 目錄由標題自動產生並逐一驗證錨點 | build 檢查 |

---

## 附錄 F：驗證紀錄

### F.1 驗證方法

| 項目 | 方法 | 結果 |
| --- | --- | --- |
| 產品版本基準 | `gh api repos/multica-ai/multica/releases`；下載 v0.6.1 原始碼 tarball | v0.6.1（2026-10-01），commit `2ea01ae4e` |
| 官方文件 | 逐份閱讀 v0.6.1 的 `apps/docs/content/docs/*.mdx`（50 頁英文版）與 `SELF_HOSTING*.md`、`CLI_AND_DAEMON.md`、`CONTRIBUTING.md`、`VISION.md`、`LICENSE`、`NOTICE`、`docs/*.md` | 作為各章主要依據 |
| CLI 指令與旗標 | 下載 `multica-cli-0.6.1-windows-amd64.zip`，SHA256 與 `checksums.txt` 相符（`55fef9e4…82400f`）；遞迴執行 `--help` 匯出 21 個頂層、共 204 個指令 | 手冊中所有 `multica …` 指令以腳本比對子指令路徑與旗標（411 處引用中 406 處可辨識為有效指令路徑，所用旗標全部存在；其餘 5 處為 `helm install multica deploy/...` 等參數被誤判，非錯誤） |
| 環境變數 | 比對 `environment-variables.mdx`、`SELF_HOSTING_ADVANCED.md`、`CLI_AND_DAEMON.md`、`.env.example` 與 Go 原始碼 | 手冊中所有環境變數名稱以腳本比對（手冊共引用 240 個名稱；除更正表 E.3 #10 刻意列出的 9 個舊版虛構變數外，全部存在於 v0.6.1 原始碼或官方文件） |
| Prometheus 指標 | 讀取 `server/internal/metrics/*.go` 的 Namespace／Subsystem／Name 與標籤 | 第 21.3 節表格與告警範例 |
| Helm values | 讀取 `deploy/helm/multica/values.yaml` | 第 5.7 節 |
| Changelog | 讀取 `apps/web/features/landing/i18n/en.ts` 中 v0.3.34–v0.6.1 條目，並以 WebFetch 確認官網 Changelog 最新為 v0.6.1 | 附錄 E.1、各章版本標註 |
| 外部評測 | WebSearch／WebFetch 第三方評測與 GitHub Issues（#1111 已關閉、#1705 仍開啟） | 第 1.5 節對照表 |
| Markdown 格式 | Repo 的 `check-md.ps1`、`check-toc.ps1`、`test-mermaid-syntax.ps1`；Mermaid 11 解析器逐圖驗證；Hugo 實際渲染後比對所有 `href="#…"` 與標題 id | check-md 0 筆；check-toc 263 個目錄連結、無缺漏與重複錨點；Mermaid 11.17.2 解析 17/17 通過；Hugo 渲染 314 個標題 id、587 個頁內連結，僅佈景主題的 `#top` 未解析 |

### F.2 待確認項目

| # | 項目 | 說明 | 建議驗證方式 |
| --- | --- | --- | --- |
| 1 | Agent 環境變數的檢視／修改權限 | v0.6.1 文件寫「只有 Workspace owner／admin 可解鎖修改」；v0.4.14 Changelog 寫「Agent 擁有者可檢視與更新自己 Agent 的環境變數」 | 在實際部署以一般成員（Agent 擁有者）測試 `multica agent env get` |
| 2 | ZeroClaw 能力矩陣 | README 列為 26 種之一，但 Providers 表未列 Session／MCP／Skill 欄位 | 待官方 Providers 頁補充後更新附錄 C |
| 3 | QwenPaw 模型變數 | `CLI_AND_DAEMON.md` 列出 `MULTICA_QWENPAW_MODEL`，但環境變數文件與 Daemon 原始碼皆無 | 依原始碼視為不支援，待官方文件統一 |
| 4 | 釘釘／企業微信加密金鑰 | `MULTICA_DINGTALK_SECRET_KEY`、`MULTICA_WECOM_SECRET_KEY` 出現在 Channels 文件，未列在環境變數總表 | 確認官方 Compose 檔是否傳遞 |
| 5 | 已發布 Helm Chart 版本 | 原始碼 `Chart.yaml` 為 `version: 0.1.0`、`appVersion: "latest"`，發布時改寫為 Release 版本 | 以 `helm show chart oci://ghcr.io/multica-ai/charts/multica --version 0.6.1` 確認 |
| 6 | 實機流程 | 本版未啟動完整 Server；Webhook 回應碼、Wakeup、Steer、通道整合依官方文件撰寫 | 在 Staging 依附錄 A.4 實測 |
| 7 | Multica CLI Skill | 未在 Claude Code／Codex 中實際安裝測試 | 依 multica-cli README 安裝並操作一個 Issue |
| 8 | Skill 二進位附件（Issue #1705） | 2026-10-05 仍為 open | 下次改版時重查 |
| 9 | Prometheus 指標穩定性 | 指標名稱為實作細節，官方未承諾穩定 | 每次升級後比對 `/metrics` |
| 10 | Desktop／iOS | 未實機安裝；平台與資產名稱依 v0.6.1 Release 資產清單 | 以實機驗證 `desktop.json` 與 iOS 建置 |

---

## 附錄 G：術語表

| 術語 | 英文 | 定義 |
| --- | --- | --- |
| Access | Access | Agent 的執行權限範圍：Only me、Entire workspace、Specific people；與 Workspace 角色無關 |
| Agent | Agent | Workspace 中的 AI 協作者，一組可重用的設定（名稱、指令、模型、Skills、Access、Runtime），只在被觸發時執行 |
| Agent Builder | Build with AI | 以對話方式產生 Agent 設定草稿的建立入口 |
| Autopilot | Autopilot | 依排程、Webhook 或手動觸發 Agent 的自動化，模式為 Create issue 或 Run only |
| Backlog 停車 | Backlog parking | 只有內建 `backlog` 狀態會阻止已指派的 Agent 開始執行 |
| Channel | Channel | 通訊平台整合（Slack、飛書、釘釘、企業微信、Telegram） |
| Chat | Chat | 與單一 Agent 的私密一對一對話，不掛在 Issue 上 |
| Custom Runtime Profile | Custom runtime profile | 以既有協定家族包裝自訂指令（Wrapper、版本鎖定執行檔）的 Runtime 設定 |
| Daemon | Daemon | 在執行電腦上的 Multica 背景行程：偵測 AI 工具、註冊 Runtime、領取 Run、回報結果 |
| Execution log | Execution log | Issue 側欄中列出所有 Run 的區塊 |
| GC | Garbage Collection | Daemon 定期回收 `MULTICA_WORKSPACES_ROOT` 下工作目錄與快取的機制 |
| GHCR | GitHub Container Registry | 官方映像與 Helm Chart 的發布位置 |
| Inbox | Inbox | 成員的通知中心；Agent 不使用 |
| Issue | Issue | Multica 的基本工作單位；Assignee 可為成員、Agent 或 Squad |
| Lifecycle category | Lifecycle category | Issue 狀態的四種類別：`unstarted`、`started`、`done`、`closed` |
| MCP | Model Context Protocol | 讓 AI 工具連接外部工具的協定；Multica 管理 MCP 伺服器設定並在 Run 前提供給支援的 AI 工具 |
| Metadata | Issue metadata | Issue 層級的鍵值對，供 Agent 與自動化寫入結構化狀態 |
| Multica License | Multica License | Apache License 2.0 全文加上託管／嵌入、品牌、署名等附加條件的授權 |
| PAT | Personal Access Token | `mul_` 前綴的個人存取 Token，供 CLI、Daemon、腳本與 API 使用 |
| Project | Project | 以共同目標組織多個 Issue，並可綁定 Repo 與本機目錄資源 |
| Project Resource | Project resource | Project 綁定的 GitHub Repo（`github_repo`）或本機目錄（`local_directory`） |
| Profile | CLI profile | CLI 的獨立設定集合（伺服器、Token、預設 Workspace、Daemon 狀態），以 `--profile` 切換 |
| Rollup | Usage rollup | 以 `rollup_task_usage_hourly()` 把用量彙總到 `task_usage_hourly`，由行程內排程器執行 |
| Run | Run | Agent 的一次執行紀錄；API 與資料庫中稱為 task |
| Runtime | Runtime | 一台電腦加上一種 AI 工具（或自訂 Profile）所構成的執行環境 |
| Skill | Skill | 以 `SKILL.md` 為主檔、可附支援檔案的可重用工作方法，可綁定多個 Agent |
| Squad | Squad | 由 Leader Agent 帶領的 Agent 與成員群組，Leader 負責分派 |
| Stage | Stage | 子 Issue 的批次序號；同一 Stage 全部結束時喚醒父 Issue 的 Agent Assignee |
| Steer | Steer | 在 Agent 執行中途補充指示，送入目前的 Run（Claude Code、Codex、Grok） |
| Task Token | Task token | `mat_` 前綴、綁定單一 Run 的臨時憑證，最長 24 小時 |
| Transcript | Transcript | 一次 Run 的完整訊息、工具呼叫與錯誤輸出 |
| Trigger preview | Trigger preview | 評論送出前顯示會喚醒哪些 Agent 的預覽 |
| Wakeup | Issue wakeup | 讓 Agent 在事件、條件或時間到達時再次收到 Run 的規則 |
| Workspace | Workspace | Multica 的最上層邊界，成員、Issue、Agent、Skill 與 Run 紀錄完全隔離 |
| Workspace Context | Workspace context | 提供給 Workspace 內所有 Agent 的長期背景說明 |
| Worktree 模式 | Parallel / worktree | 本機目錄資源的平行模式：每個 Run 取得獨立 Git worktree，成果為 `agent/<agent>/<issue>` 分支 |

---

**文件維護：** 本手冊 v2.0 以 Multica v0.6.1 為基準撰寫（2026-10-05）。Multica 幾乎每個平日都會發版，建議每次升級正式環境前，對照官方 Changelog 檢視第 5、6、14、16、22 章與附錄 B、C，並從附錄 F.2 的待確認項目開始下一輪改版。
