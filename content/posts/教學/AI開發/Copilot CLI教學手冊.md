+++
date = '2026-05-29T10:00:00+08:00'
lastmod = '2026-10-14T18:00:00+08:00'
draft = false
title = 'Copilot CLI教學手冊'
tags = ['教學', 'AI開發', 'copilot-cli']
categories = ['教學']
+++

# GitHub Copilot CLI 教學手冊

> **文件版本**：v2.0（2026-10-14，全面重新編排）
> **對應產品版本**：GitHub Copilot CLI **v1.0.97**（2026-10-13 發佈的最新穩定版），旗標與設定鍵以本機 v1.0.97 的 `copilot --help`、`copilot help config|environment|commands|permissions|sandbox` 輸出逐一核對
> **文件等級**：企業標準技術白皮書（Enterprise Technical Whitepaper）
> **適用對象**：資深工程師、DevOps／平台工程師、架構師、資安與治理人員
> **技術情境**：企業級 Web 應用（Java 21／Spring Boot 3.5、Vue 3、微服務、GitHub Enterprise Cloud）
> **適用方案**：Copilot Free／Student／Pro／Pro+／Max／Business／Enterprise（全面採用 **AI Credits** 用量計費，詳見第 17 章）
> **查證紀錄**：所有更正、已執行的驗證與尚待確認的項目，集中記錄於[附錄 H](#附錄-h查證紀錄)

## 如何使用本手冊

本手冊的目標不是「列出所有功能」，而是**讓讀者學會正確使用 Copilot CLI，並有能力審查 AI 產出的結果**。因此每一章都遵循相同結構：

| 區塊 | 內容 | 讀者要做的事 |
|------|------|------|
| 本章目標 | 讀完後應具備的能力 | 讀完後自我檢核 |
| 概念與原理 | 功能是什麼、為什麼這樣設計、限制在哪裡 | 理解，而不是背指令 |
| 操作範例 | 可直接複製的指令、設定檔與腳本（皆已在本機驗證，見附錄 H.3） | 動手做一次 |
| ❌／✅ 對照 | 常見的錯誤寫法與正確寫法 | 用來審查 AI 或同事的產出 |
| 本章審查與驗證清單 | AI 產出項目、錯誤示範、正確做法、人工如何驗證 | 落地成團隊的 Review Checklist |

> 💡 **給審查者的提示**：本手冊中的設定檔（hooks、MCP、custom agent、skill、settings）都可以用[第 21 章](#第-21-章ai-產出驗證方法論)提供的 `check_config.py` 檢查；所有 `copilot` 旗標與 slash 指令都可以用 `check_flags.py` 對照本機版本確認是否存在。

## 全書架構

| 部 | 章節 | 主題 |
|----|------|------|
| 第一部：認識與導入 | [第 1 章](#第-1-章copilot-cli-概述與定位)～[第 3 章](#第-3-章安裝驗證與初始設定) | 產品定位、企業導入模型、安裝與身分驗證 |
| 第二部：核心操作 | [第 4 章](#第-4-章互動介面與操作模式)～[第 8 章](#第-8-章github-整合) | 操作模式、Context 工程、自訂指引與代理、Session、GitHub 整合 |
| 第三部：擴充 | [第 9 章](#第-9-章mcp-伺服器)～[第 12 章](#第-12-章lspacpsdk自訂模型與可觀測性) | MCP、Skills／Plugins、Hooks、LSP／ACP／SDK／BYOK／OpenTelemetry |
| 第四部：安全與治理 | [第 13 章](#第-13-章權限模型)～[第 15 章](#第-15-章企業治理與稽核) | 權限模型、Sandbox、受管設定與稽核 |
| 第五部：自動化與維運 | [第 16 章](#第-16-章程式化介面headless-與-cicd)～[第 18 章](#第-18-章升級發佈頻道與版本管理) | 程式化執行與 CI/CD、計費與成本、升級策略 |
| 第六部：實戰與方法論 | [第 19 章](#第-19-章實戰案例)～[第 21 章](#第-21-章ai-產出驗證方法論) | 實戰案例、最佳實務、AI 產出驗證方法論 |
| 附錄 | [附錄 A](#附錄-a指令與-slash-指令速查)～[附錄 H](#附錄-h查證紀錄) | 速查表、設定鍵、範本、版本里程碑、檢查清單、查證紀錄 |

## 版本與時效聲明

Copilot CLI 幾乎每週發佈一版（2026-08-14 的 v1.0.80 到 2026-10-13 的 v1.0.97，兩個月內就發佈了 17 個版本）。模型清單、預覽功能與預設值變動得最快，本手冊對這幾類資訊一律標註查證日期。導入時請以下列指令確認你手上的版本：

```bash
copilot --version            # 版本號
copilot help config          # 目前版本支援的全部設定鍵
copilot help environment     # 目前版本支援的全部環境變數
copilot help commands        # 目前版本的 slash 指令
```

## 目錄

> 目錄為三層結構（章 → 節 → 小節），每一項都連到 Hugo 實際產生的錨點；各章最後一節固定為「本章審查與驗證清單」。

<!-- TOC-AUTO-BEGIN -->

- [第 1 章：Copilot CLI 概述與定位](#第-1-章copilot-cli-概述與定位)
  - [1.1 什麼是 GitHub Copilot CLI](#11-什麼是-github-copilot-cli)
    - [1.1.1 發展歷程重點](#111-發展歷程重點)
    - [1.1.2 核心能力一覽](#112-核心能力一覽)
  - [1.2 「代理」與「指令產生器」的根本差異](#12-代理與指令產生器的根本差異)
  - [1.3 與其他 Copilot 介面的分工](#13-與其他-copilot-介面的分工)
    - [1.3.1 與同類 Agentic CLI 的比較](#131-與同類-agentic-cli-的比較)
  - [1.4 適用與不適用場景](#14-適用與不適用場景)
    - [1.4.1 適合的場景](#141-適合的場景)
    - [1.4.2 不適合或需要額外控制的場景](#142-不適合或需要額外控制的場景)
  - [1.5 本章審查與驗證清單](#15-本章審查與驗證清單)
- [第 2 章：企業架構與治理模型](#第-2-章企業架構與治理模型)
  - [2.1 Copilot CLI 在企業架構中的位置](#21-copilot-cli-在企業架構中的位置)
    - [2.1.1 會影響 Copilot CLI 的企業控制](#211-會影響-copilot-cli-的企業控制)
  - [2.2 設定的六層覆寫順序](#22-設定的六層覆寫順序)
    - [2.2.1 控制要放在哪一層](#221-控制要放在哪一層)
  - [2.3 角色與責任（RACI）](#23-角色與責任raci)
  - [2.4 導入路線圖](#24-導入路線圖)
  - [2.5 本章審查與驗證清單](#25-本章審查與驗證清單)
- [第 3 章：安裝、驗證與初始設定](#第-3-章安裝驗證與初始設定)
  - [3.1 系統需求](#31-系統需求)
  - [3.2 安裝方式](#32-安裝方式)
    - [3.2.1 各方式的操作範例](#321-各方式的操作範例)
    - [3.2.2 驗證安裝](#322-驗證安裝)
  - [3.3 身分驗證](#33-身分驗證)
    - [3.3.1 五種驗證來源與優先順序](#331-五種驗證來源與優先順序)
    - [3.3.2 支援的 Token 類型](#332-支援的-token-類型)
    - [3.3.3 互動式登入](#333-互動式登入)
    - [3.3.4 以 PAT 非互動式驗證](#334-以-pat-非互動式驗證)
    - [3.3.5 多帳號、登出與撤銷](#335-多帳號登出與撤銷)
    - [3.3.6 不需要 GitHub 驗證的情境](#336-不需要-github-驗證的情境)
  - [3.4 企業網路設定](#34-企業網路設定)
    - [3.4.1 Proxy](#341-proxy)
    - [3.4.2 GitHub Enterprise Cloud 資料落地區域與 GHES](#342-github-enterprise-cloud-資料落地區域與-ghes)
    - [3.4.3 設定與快取目錄](#343-設定與快取目錄)
  - [3.5 首次啟動與初始設定](#35-首次啟動與初始設定)
    - [3.5.1 首次啟動流程](#351-首次啟動流程)
    - [3.5.2 建議的初始設定](#352-建議的初始設定)
  - [3.6 常見安裝與驗證問題](#36-常見安裝與驗證問題)
  - [3.7 本章審查與驗證清單](#37-本章審查與驗證清單)
- [第 4 章：互動介面與操作模式](#第-4-章互動介面與操作模式)
  - [4.1 介面組成](#41-介面組成)
    - [4.1.1 輸入語法](#411-輸入語法)
    - [4.1.2 最常用的快捷鍵](#412-最常用的快捷鍵)
  - [4.2 權限核准對話框](#42-權限核准對話框)
  - [4.3 三種操作模式](#43-三種操作模式)
    - [4.3.1 Plan 模式](#431-plan-模式)
    - [4.3.2 Autopilot 模式](#432-autopilot-模式)
    - [4.3.3 Autopilot、`--allow-all` 與 `--no-ask-user` 的差異](#433-autopilot--allow-all-與---no-ask-user-的差異)
  - [4.4 `/fleet`：平行子代理](#44-fleet平行子代理)
  - [4.5 `/delegate`：交給 Copilot cloud agent](#45-delegate交給-copilot-cloud-agent)
  - [4.6 引導、取消與回溯](#46-引導取消與回溯)
    - [4.6.1 在執行中引導代理](#461-在執行中引導代理)
    - [4.6.2 取消](#462-取消)
    - [4.6.3 回溯（rewind）](#463-回溯rewind)
  - [4.7 其他常用互動功能](#47-其他常用互動功能)
  - [4.8 本章審查與驗證清單](#48-本章審查與驗證清單)
- [第 5 章：Context 工程](#第-5-章context-工程)
  - [5.1 Context window 的組成](#51-context-window-的組成)
  - [5.2 自動壓縮（Compaction）與檢查點](#52-自動壓縮compaction與檢查點)
  - [5.3 精準提供 context](#53-精準提供-context)
    - [5.3.1 `@` 引用檔案](#531--引用檔案)
    - [5.3.2 `#` 引用 GitHub 資源](#532--引用-github-資源)
    - [5.3.3 圖片與附件](#533-圖片與附件)
  - [5.4 多 Repo 與目錄存取](#54-多-repo-與目錄存取)
  - [5.5 Copilot Memory](#55-copilot-memory)
  - [5.6 讓 context 保持健康的習慣](#56-讓-context-保持健康的習慣)
  - [5.7 本章審查與驗證清單](#57-本章審查與驗證清單)
- [第 6 章：Custom Instructions 與 Custom Agents](#第-6-章custom-instructions-與-custom-agents)
  - [6.1 指引來源與合併規則](#61-指引來源與合併規則)
  - [6.2 撰寫 Repo 全域指引](#62-撰寫-repo-全域指引)
    - [6.2.1 用 `/init` 產生初稿](#621-用-init-產生初稿)
    - [6.2.2 範例：企業 Java 專案的指引](#622-範例企業-java-專案的指引)
    - [6.2.3 ❌／✅ 對照](#623--對照)
  - [6.3 路徑專屬指引](#63-路徑專屬指引)
  - [6.4 Custom Agents](#64-custom-agents)
    - [6.4.1 存放位置與優先順序](#641-存放位置與優先順序)
    - [6.4.2 frontmatter 欄位](#642-frontmatter-欄位)
    - [6.4.3 範例：資安審查代理](#643-範例資安審查代理)
    - [6.4.4 建立與使用](#644-建立與使用)
    - [6.4.5 哪些代理會讀取 Repo 指引](#645-哪些代理會讀取-repo-指引)
    - [6.4.6 Sidekick 代理](#646-sidekick-代理)
  - [6.5 內建子代理](#65-內建子代理)
  - [6.6 本章審查與驗證清單](#66-本章審查與驗證清單)
- [第 7 章：Session 管理](#第-7-章session-管理)
  - [7.1 Session 是什麼](#71-session-是什麼)
  - [7.2 啟動、恢復與命名](#72-啟動恢復與命名)
  - [7.3 多 Session 並行](#73-多-session-並行)
  - [7.4 Worktree 與 Fork：隔離並行工作](#74-worktree-與-fork隔離並行工作)
  - [7.5 分享與匯出](#75-分享與匯出)
  - [7.6 Session 同步與遠端控制](#76-session-同步與遠端控制)
  - [7.7 Chronicle：Session 歷史的分析工具](#77-chroniclesession-歷史的分析工具)
  - [7.8 本章審查與驗證清單](#78-本章審查與驗證清單)
- [第 8 章：GitHub 整合](#第-8-章github-整合)
  - [8.1 以自然語言操作 GitHub](#81-以自然語言操作-github)
  - [8.2 `/pr`：PR 生命週期](#82-prpr-生命週期)
  - [8.3 內建 GitHub MCP 伺服器](#83-內建-github-mcp-伺服器)
  - [8.4 Issue、PR 與 Gist 瀏覽分頁](#84-issuepr-與-gist-瀏覽分頁)
  - [8.5 程式審查：`/review` 與 `/security-review`](#85-程式審查review-與-security-review)
  - [8.6 在 Actions 中使用](#86-在-actions-中使用)
  - [8.7 本章審查與驗證清單](#87-本章審查與驗證清單)
- [第 9 章：MCP 伺服器](#第-9-章mcp-伺服器)
  - [9.1 MCP 在 Copilot CLI 中的角色](#91-mcp-在-copilot-cli-中的角色)
  - [9.2 設定檔位置與載入優先順序](#92-設定檔位置與載入優先順序)
    - [9.2.1 信任模型](#921-信任模型)
  - [9.3 新增 MCP 伺服器](#93-新增-mcp-伺服器)
    - [9.3.1 互動式](#931-互動式)
    - [9.3.2 非互動式：`copilot mcp`](#932-非互動式copilot-mcp)
    - [9.3.3 設定檔格式與範例](#933-設定檔格式與範例)
    - [9.3.4 從 `.vscode/mcp.json` 遷移](#934-從-vscodemcpjson-遷移)
  - [9.4 管理與疑難排解](#94-管理與疑難排解)
  - [9.5 企業管控](#95-企業管控)
  - [9.6 本章審查與驗證清單](#96-本章審查與驗證清單)
- [第 10 章：Skills、Plugins、Marketplace 與 Extensions](#第-10-章skillspluginsmarketplace-與-extensions)
  - [10.1 四種擴充機制的比較](#101-四種擴充機制的比較)
  - [10.2 Skills](#102-skills)
    - [10.2.1 存放位置與優先順序](#1021-存放位置與優先順序)
    - [10.2.2 `SKILL.md` frontmatter](#1022-skillmd-frontmatter)
    - [10.2.3 範例：資料庫遷移 skill](#1023-範例資料庫遷移-skill)
    - [10.2.4 管理指令](#1024-管理指令)
  - [10.3 Plugins](#103-plugins)
    - [10.3.1 安裝與管理](#1031-安裝與管理)
    - [10.3.2 兩種 plugin 格式](#1032-兩種-plugin-格式)
    - [10.3.3 建立企業內部 marketplace](#1033-建立企業內部-marketplace)
    - [10.3.4 企業管控](#1034-企業管控)
  - [10.4 Extensions（實驗性）](#104-extensions實驗性)
  - [10.5 本章審查與驗證清單](#105-本章審查與驗證清單)
- [第 11 章：Hooks](#第-11-章hooks)
  - [11.1 Hooks 是什麼、適合做什麼](#111-hooks-是什麼適合做什麼)
  - [11.2 載入來源與順序](#112-載入來源與順序)
  - [11.3 設定格式](#113-設定格式)
    - [11.3.1 Command hook](#1131-command-hook)
    - [11.3.2 HTTP hook 與 Prompt hook](#1132-http-hook-與-prompt-hook)
  - [11.4 事件總覽](#114-事件總覽)
  - [11.5 `preToolUse`：攔截政策](#115-pretooluse攔截政策)
    - [11.5.1 輸入與輸出](#1151-輸入與輸出)
    - [11.5.2 失敗語意：最容易出錯的地方](#1152-失敗語意最容易出錯的地方)
    - [11.5.3 範例：Repo 層級的安全政策](#1153-範例repo-層級的安全政策)
    - [11.5.4 範例：只記錄中繼資料的稽核](#1154-範例只記錄中繼資料的稽核)
    - [11.5.5 測試 hook](#1155-測試-hook)
  - [11.6 其他事件的決策控制](#116-其他事件的決策控制)
    - [11.6.1 `permissionRequest`](#1161-permissionrequest)
    - [11.6.2 `agentStop`／`subagentStop`](#1162-agentstopsubagentstop)
    - [11.6.3 `postToolUse`](#1163-posttooluse)
    - [11.6.4 進度訊息](#1164-進度訊息)
  - [11.7 Sandbox 中的 hooks](#117-sandbox-中的-hooks)
  - [11.8 停用 hooks](#118-停用-hooks)
  - [11.9 v1 手冊的錯誤寫法對照](#119-v1-手冊的錯誤寫法對照)
  - [11.10 本章審查與驗證清單](#1110-本章審查與驗證清單)
- [第 12 章：LSP、ACP、SDK、自訂模型與可觀測性](#第-12-章lspacpsdk自訂模型與可觀測性)
  - [12.1 LSP 語言伺服器](#121-lsp-語言伺服器)
  - [12.2 ACP（Agent Client Protocol）](#122-acpagent-client-protocol)
  - [12.3 Copilot SDK](#123-copilot-sdk)
  - [12.4 自訂模型供應商（BYOK）](#124-自訂模型供應商byok)
    - [12.4.1 支援的供應商與需求](#1241-支援的供應商與需求)
    - [12.4.2 設定範例](#1242-設定範例)
    - [12.4.3 BYOK 的治理要點](#1243-byok-的治理要點)
  - [12.5 OpenTelemetry 可觀測性](#125-opentelemetry-可觀測性)
    - [12.5.1 啟用條件](#1251-啟用條件)
    - [12.5.2 匯出的資料](#1252-匯出的資料)
    - [12.5.3 內容擷取](#1253-內容擷取)
  - [12.6 本章審查與驗證清單](#126-本章審查與驗證清單)
- [第 13 章：權限模型](#第-13-章權限模型)
  - [13.1 三類權限與預設行為](#131-三類權限與預設行為)
  - [13.2 兩層工具控制](#132-兩層工具控制)
  - [13.3 權限規則語法](#133-權限規則語法)
    - [13.3.1 比對行為對照](#1331-比對行為對照)
    - [13.3.2 情境範例](#1332-情境範例)
    - [13.3.3 ❌／✅ 對照](#1333--對照)
  - [13.4 已儲存的核准](#134-已儲存的核准)
  - [13.5 核准模式](#135-核准模式)
  - [13.6 YOLO（allow-all）的風險矩陣](#136-yoloallow-all的風險矩陣)
  - [13.7 其他保護機制](#137-其他保護機制)
  - [13.8 本章審查與驗證清單](#138-本章審查與驗證清單)
- [第 14 章：Sandbox 與執行隔離](#第-14-章sandbox-與執行隔離)
  - [14.1 為什麼需要 Sandbox](#141-為什麼需要-sandbox)
  - [14.2 本機 Sandbox](#142-本機-sandbox)
    - [14.2.1 啟用](#1421-啟用)
    - [14.2.2 支援的作業系統](#1422-支援的作業系統)
    - [14.2.3 保護範圍與限制](#1423-保護範圍與限制)
  - [14.3 設定](#143-設定)
    - [14.3.1 主要設定鍵](#1431-主要設定鍵)
    - [14.3.2 範例：開發者的使用者設定](#1432-範例開發者的使用者設定)
    - [14.3.3 憑證遮蔽](#1433-憑證遮蔽)
  - [14.4 Bypass（跳出 Sandbox）](#144-bypass跳出-sandbox)
  - [14.5 企業強制 Sandbox](#145-企業強制-sandbox)
  - [14.6 雲端 Sandbox](#146-雲端-sandbox)
  - [14.7 本章審查與驗證清單](#147-本章審查與驗證清單)
- [第 15 章：企業治理與稽核](#第-15-章企業治理與稽核)
  - [15.1 受管設定的來源](#151-受管設定的來源)
  - [15.2 受管設定支援的鍵](#152-受管設定支援的鍵)
    - [15.2.1 範例：企業基線](#1521-範例企業基線)
  - [15.3 受管權限規則](#153-受管權限規則)
    - [15.3.1 網域邊界 `limitTo`](#1531-網域邊界-limitto)
  - [15.4 MCP 伺服器管控](#154-mcp-伺服器管控)
  - [15.5 Policy hooks 與內容排除](#155-policy-hooks-與內容排除)
  - [15.6 已知風險與業界研究](#156-已知風險與業界研究)
  - [15.7 稽核證據鏈](#157-稽核證據鏈)
  - [15.8 治理成熟度檢核](#158-治理成熟度檢核)
  - [15.9 本章審查與驗證清單](#159-本章審查與驗證清單)
- [第 16 章：程式化介面、Headless 與 CI/CD](#第-16-章程式化介面headless-與-cicd)
  - [16.1 程式化模式基礎](#161-程式化模式基礎)
  - [16.2 程式化模式的信任差異](#162-程式化模式的信任差異)
  - [16.3 常用腳本模式](#163-常用腳本模式)
    - [16.3.1 解析 JSONL 輸出](#1631-解析-jsonl-輸出)
  - [16.4 GitHub Actions](#164-github-actions)
    - [16.4.1 兩種驗證方式](#1641-兩種驗證方式)
    - [16.4.2 範例：PR 變更摘要（`GITHUB_TOKEN`）](#1642-範例pr-變更摘要github_token)
    - [16.4.3 範例：排程報告（PAT）](#1643-範例排程報告pat)
    - [16.4.4 官方推薦：GitHub Agentic Workflows](#1644-官方推薦github-agentic-workflows)
  - [16.5 動態 workflow：`copilot workflow run`](#165-動態-workflowcopilot-workflow-run)
  - [16.6 本機 CI 前置檢查腳本範例](#166-本機-ci-前置檢查腳本範例)
  - [16.7 本章審查與驗證清單](#167-本章審查與驗證清單)
- [第 17 章：計費與成本管理](#第-17-章計費與成本管理)
  - [17.1 AI Credits 的計算方式](#171-ai-credits-的計算方式)
  - [17.2 方案與內含額度](#172-方案與內含額度)
  - [17.3 超額與預算](#173-超額與預算)
  - [17.4 在 CLI 中觀察與限制用量](#174-在-cli-中觀察與限制用量)
    - [17.4.1 Session 上限（公開預覽）](#1741-session-上限公開預覽)
  - [17.5 節省成本的做法](#175-節省成本的做法)
  - [17.6 本章審查與驗證清單](#176-本章審查與驗證清單)
- [第 18 章：升級、發佈頻道與版本管理](#第-18-章升級發佈頻道與版本管理)
  - [18.1 更新方式](#181-更新方式)
  - [18.2 自動更新的控制](#182-自動更新的控制)
  - [18.3 企業版本管理策略](#183-企業版本管理策略)
  - [18.4 升級回歸驗證清單](#184-升級回歸驗證清單)
  - [18.5 v1.0.80 之後值得注意的變更](#185-v1080-之後值得注意的變更)
  - [18.6 本章審查與驗證清單](#186-本章審查與驗證清單)
- [第 19 章：實戰案例](#第-19-章實戰案例)
  - [19.1 案例一：新增客戶管理 API（Plan → 實作）](#191-案例一新增客戶管理-apiplan--實作)
    - [19.1.1 情境與提示](#1911-情境與提示)
    - [19.1.2 審查計畫](#1912-審查計畫)
    - [19.1.3 AI 產出與審查發現](#1913-ai-產出與審查發現)
    - [19.1.4 驗證](#1914-驗證)
  - [19.2 案例二：修 Bug 並補回歸測試](#192-案例二修-bug-並補回歸測試)
    - [19.2.1 情境與提示](#1921-情境與提示)
    - [19.2.2 AI 產出與審查發現](#1922-ai-產出與審查發現)
    - [19.2.3 驗證](#1923-驗證)
  - [19.3 案例三：建立 PR 與描述](#193-案例三建立-pr-與描述)
    - [19.3.1 情境與提示](#1931-情境與提示)
    - [19.3.2 審查發現](#1932-審查發現)
  - [19.4 案例四：Spring Batch 每日報表](#194-案例四spring-batch-每日報表)
    - [19.4.1 情境與提示](#1941-情境與提示)
    - [19.4.2 AI 產出與審查發現](#1942-ai-產出與審查發現)
    - [19.4.3 驗證](#1943-驗證)
  - [19.5 案例的共同審查模式](#195-案例的共同審查模式)
  - [19.6 本章審查與驗證清單](#196-本章審查與驗證清單)
- [第 20 章：最佳實務](#第-20-章最佳實務)
  - [20.1 標準工作流程](#201-標準工作流程)
  - [20.2 撰寫提示](#202-撰寫提示)
    - [20.2.1 提示結構範本](#2021-提示結構範本)
    - [20.2.2 品質等級對照](#2022-品質等級對照)
    - [20.2.3 提示的黃金法則](#2023-提示的黃金法則)
  - [20.3 人機協作：依風險決定介入密度](#203-人機協作依風險決定介入密度)
  - [20.4 團隊規範建議](#204-團隊規範建議)
  - [20.5 成效指標](#205-成效指標)
  - [20.6 常見反模式](#206-常見反模式)
  - [20.7 本章審查與驗證清單](#207-本章審查與驗證清單)
- [第 21 章：AI 產出驗證方法論](#第-21-章ai-產出驗證方法論)
  - [21.1 核心原則](#211-核心原則)
  - [21.2 審查五問](#212-審查五問)
  - [21.3 依產出類型的審查方法](#213-依產出類型的審查方法)
    - [21.3.1 計畫（Plan 模式）](#2131-計畫plan-模式)
    - [21.3.2 程式碼 diff](#2132-程式碼-diff)
    - [21.3.3 測試](#2133-測試)
    - [21.3.4 Shell 指令（核准對話框中）](#2134-shell-指令核准對話框中)
    - [21.3.5 Copilot 設定檔](#2135-copilot-設定檔)
  - [21.4 離線檢查工具](#214-離線檢查工具)
    - [21.4.1 `check_config.py`：設定檔檢查器](#2141-check_configpy設定檔檢查器)
    - [21.4.2 `check_flags.py`：旗標與指令檢查器](#2142-check_flagspy旗標與指令檢查器)
    - [21.4.3 正反範例測試](#2143-正反範例測試)
    - [21.4.4 放進 CI](#2144-放進-ci)
  - [21.5 驗證的極限](#215-驗證的極限)
  - [21.6 本章審查與驗證清單](#216-本章審查與驗證清單)
- [附錄 A：指令與 slash 指令速查](#附錄-a指令與-slash-指令速查)
  - [A.1 子指令（在 shell 執行）](#a1-子指令在-shell-執行)
  - [A.2 Slash 指令](#a2-slash-指令)
    - [A.2.1 代理與模式](#a21-代理與模式)
    - [A.2.2 Session](#a22-session)
    - [A.2.3 權限與環境](#a23-權限與環境)
    - [A.2.4 擴充](#a24-擴充)
    - [A.2.5 GitHub 與程式碼](#a25-github-與程式碼)
    - [A.2.6 介面與其他](#a26-介面與其他)
  - [A.3 快捷鍵](#a3-快捷鍵)
  - [A.4 輸入前綴](#a4-輸入前綴)
- [附錄 B：命令列選項](#附錄-b命令列選項)
  - [B.1 執行模式與 Session](#b1-執行模式與-session)
  - [B.2 模型](#b2-模型)
  - [B.3 權限](#b3-權限)
  - [B.4 擴充](#b4-擴充)
  - [B.5 輸出、日誌與其他](#b5-輸出日誌與其他)
- [附錄 C：環境變數](#附錄-c環境變數)
  - [C.1 驗證與主機](#c1-驗證與主機)
  - [C.2 設定與行為](#c2-設定與行為)
  - [C.3 程式化模式的信任開關](#c3-程式化模式的信任開關)
  - [C.4 網路](#c4-網路)
  - [C.5 自訂模型（BYOK）](#c5-自訂模型byok)
  - [C.6 OpenTelemetry](#c6-opentelemetry)
- [附錄 D：設定檔與設定鍵](#附錄-d設定檔與設定鍵)
  - [D.1 `~/.copilot` 目錄結構](#d1-copilot-目錄結構)
  - [D.2 Repo 層級檔案](#d2-repo-層級檔案)
  - [D.3 使用者設定鍵（`~/.copilot/settings.json`）](#d3-使用者設定鍵copilotsettingsjson)
  - [D.4 Repo 設定鍵（`.github/copilot/settings.json`）](#d4-repo-設定鍵githubcopilotsettingsjson)
  - [D.5 Repo 模型白名單（`.github/allowed_models.txt`）](#d5-repo-模型白名單githuballowed_modelstxt)
  - [D.6 受管設定](#d6-受管設定)
- [附錄 E：Prompt 範本](#附錄-eprompt-範本)
  - [E.1 新增 API（Plan 模式）](#e1-新增-apiplan-模式)
  - [E.2 修 Bug](#e2-修-bug)
  - [E.3 程式審查](#e3-程式審查)
  - [E.4 建立 PR](#e4-建立-pr)
  - [E.5 CI/CD 設定](#e5-cicd-設定)
  - [E.6 資料庫遷移](#e6-資料庫遷移)
  - [E.7 陌生程式庫導覽](#e7-陌生程式庫導覽)
  - [E.8 大規模機械式修改（Autopilot）](#e8-大規模機械式修改autopilot)
- [附錄 F：版本里程碑與已移除項目](#附錄-f版本里程碑與已移除項目)
  - [F.1 版本里程碑](#f1-版本里程碑)
  - [F.2 已移除、改名與行為變更](#f2-已移除改名與行為變更)
- [附錄 G：檢查清單](#附錄-g檢查清單)
  - [G.1 開發者入門](#g1-開發者入門)
  - [G.2 Repo 設定](#g2-repo-設定)
  - [G.3 安全](#g3-安全)
  - [G.4 每日使用](#g4-每日使用)
  - [G.5 企業管理者](#g5-企業管理者)
  - [G.6 版本升級](#g6-版本升級)
- [附錄 H：查證紀錄](#附錄-h查證紀錄)
  - [H.1 查證基準與參考來源](#h1-查證基準與參考來源)
  - [H.2 v1 → v2 更正清單](#h2-v1--v2-更正清單)
  - [H.3 已執行的驗證](#h3-已執行的驗證)
  - [H.4 尚待確認的項目](#h4-尚待確認的項目)
  - [H.5 Hugo 與目錄比對結果](#h5-hugo-與目錄比對結果)

<!-- TOC-AUTO-END -->

---

## 第 1 章：Copilot CLI 概述與定位

> **本章目標**
>
> - 說清楚 Copilot CLI 是什麼、不是什麼，以及它和 IDE Copilot、Copilot cloud agent 的分工。
> - 理解「代理（agent）」與「指令產生器」的差異，以及這個差異帶來的風險。
> - 能依任務特性判斷該用 CLI、IDE 還是 cloud agent。

### 1.1 什麼是 GitHub Copilot CLI

GitHub Copilot CLI（指令為 `copilot`）是在終端機中執行的 **AI 程式開發代理**。它與 GitHub Copilot cloud agent 使用同一套代理執行框架（agentic harness），可以讀寫檔案、執行 shell 指令、搜尋程式碼、操作 GitHub 上的 Issue／PR，並在你核准的範圍內**自主完成多步驟任務**。

它有兩種介面：

| 介面 | 啟動方式 | 適用情境 |
|------|----------|----------|
| 互動式（interactive） | `copilot` | 與代理對話、逐步核准、需要人工判斷的開發工作 |
| 程式化（programmatic） | `copilot -p "提示"` 或 `echo "提示" \| copilot` | 腳本、CI/CD、排程任務；執行完即結束 |

> ⚠️ **與舊產品區分**：早期的 GitHub CLI 擴充套件 `gh copilot`（只會建議或解釋 shell 指令）已退役。本手冊談的是獨立的 `copilot` 指令，它是完整的代理，**會實際執行指令並修改檔案**。

#### 1.1.1 發展歷程重點

| 時間 | 事件 |
|------|------|
| 2025-09 | 公開預覽（v0.0.3xx），首次提供 `/model` 切換模型 |
| 2026-02-25 | 正式 GA（v0.0.418） |
| 2026-03-06 | 主版號升為 1.0 |
| 2026-06 | 計費全面改為 AI Credits；Copilot SDK 六種語言 GA |
| 2026-09～10 | 指令列解析改為 Rust 文法（v1.0.85）、設定改存 `settings.json`（v1.0.93）、本機 Sandbox 開放所有使用者（v1.0.93）、`copilot config` 子指令（v1.0.92） |

完整里程碑見[附錄 F](#附錄-f版本里程碑與已移除項目)。

#### 1.1.2 核心能力一覽

| 能力 | 說明 | 詳見 |
|------|------|------|
| 代理式執行 | 規劃、讀寫檔案、執行指令、修正錯誤，直到任務完成 | 第 4 章 |
| 三種操作模式 | 標準（逐步核准）、Plan（先規劃再動手）、Autopilot（自主完成） | 第 4 章 |
| 平行子代理 | `/fleet` 把任務拆成多個子代理同時執行 | 第 4 章 |
| 委派到雲端 | `/delegate`（或 `&` 前綴）交給 Copilot cloud agent，開草稿 PR | 第 4、8 章 |
| Context 工程 | `@檔案`、`#Issue`、`/add-dir`、自動壓縮、Copilot Memory | 第 5 章 |
| 自訂指引與代理 | `copilot-instructions.md`、`AGENTS.md`、`.agent.md`、內建子代理 | 第 6 章 |
| 擴充 | MCP 伺服器、Skills、Plugins、Hooks、LSP、Extensions | 第 9～12 章 |
| 安全控制 | 工具／路徑／網址權限、核准模式、本機與雲端 Sandbox、受管設定 | 第 13～15 章 |
| 自動化 | `-p`、JSONL 輸出、GitHub Actions、動態 workflow | 第 16 章 |
| 可觀測性 | OpenTelemetry traces 與 metrics | 第 12 章 |

### 1.2 「代理」與「指令產生器」的根本差異

理解這一點，是正確使用與治理 Copilot CLI 的前提。

```mermaid
flowchart LR
    subgraph G1["指令產生器（舊式 gh copilot）"]
        A1[使用者提問] --> B1[AI 建議一條指令]
        B1 --> C1[使用者自行判斷並執行]
    end
    subgraph G2["代理（Copilot CLI）"]
        A2[使用者交付任務] --> B2[代理規劃步驟]
        B2 --> C2[呼叫工具：讀檔、改檔、執行指令]
        C2 --> D2{需要核准?}
        D2 -- 是 --> E2[使用者核准或拒絕]
        D2 -- 否：已預先授權 --> F2[直接執行]
        E2 --> F2
        F2 --> G2b[觀察結果並決定下一步]
        G2b --> B2
    end
```

代理會根據**觀察到的結果**決定下一步，這帶來三個直接後果：

1. **權限就是風險邊界**：一旦你允許某個工具「本 Session 不再詢問」，代理之後可以用任何方式使用它。官方文件明確舉例：核准一次 `rm ./this-file.txt` 並選擇「本 Session 不再詢問」，代理之後就能不經詢問執行 `rm -rf ./*`。
2. **輸入來源都可能是攻擊面**：README、程式註解、Issue 內容、MCP 伺服器回應都會進入代理的 context，可能藏有提示注入（prompt injection）。詳見第 15 章。
3. **產出必須被驗證**：代理會「宣稱完成」，但宣稱不等於正確。第 21 章提供系統化的驗證方法。

### 1.3 與其他 Copilot 介面的分工

| 面向 | IDE Copilot（VS Code 等） | Copilot CLI | Copilot cloud agent |
|------|------|------|------|
| 執行位置 | 本機編輯器 | 本機終端機（或雲端 Sandbox） | GitHub 代管的雲端環境 |
| 互動方式 | 補全、Chat、Agent Mode | 對話＋代理執行 | 指派 Issue 或 `/delegate`，非同步完成 |
| 產出 | 編輯器中的變更 | 本機檔案變更、commit、PR | 草稿 PR |
| 適合 | 邊寫邊改、精細編輯 | 跨檔案任務、終端機工作流、自動化腳本 | 可以背景執行、不必盯著的工作 |
| 權限控制 | 編輯器設定 | 旗標、`settings.json`、受管設定、Sandbox | Repo 的 cloud agent 設定與防火牆 |

三者可以接力使用：在 CLI 用 `/plan` 規劃 → 用 `/ide` 連到 VS Code 檢視 diff → 把旁支工作 `/delegate` 給 cloud agent。

#### 1.3.1 與同類 Agentic CLI 的比較

| 面向 | Copilot CLI | Claude Code | OpenAI Codex CLI | Gemini CLI |
|------|------|------|------|------|
| 模型 | 多家（Anthropic、OpenAI、Google、xAI、Moonshot 等）＋ BYOK | 以 Anthropic 為主 | 以 OpenAI 為主 | 以 Google 為主 |
| GitHub 整合 | 內建 GitHub MCP、`/pr`、`/delegate` | 需透過 MCP 或 `gh` | 需透過 MCP 或 `gh` | 需透過 MCP 或 `gh` |
| 企業治理 | 沿用 Copilot 授權、組織政策、MDM 受管設定 | 自有受管設定 | 自有設定 | 依 Google 雲端治理 |
| 跨工具相容 | 讀取 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.claude/skills`、`.claude/rules`、`.claude/settings.json` 部分鍵 | — | 讀取 `AGENTS.md` | 讀取 `GEMINI.md` |

> 📝 Copilot CLI 刻意相容其他工具的設定檔（例如 `.claude/skills/` 與 `CLAUDE.md`），讓團隊可以共用同一套指引。但要注意：**同一份指引會被多個工具讀取**，內容必須避免只對某一個工具有效的指令。

### 1.4 適用與不適用場景

#### 1.4.1 適合的場景

| 場景 | 範例提示 | 建議模式 |
|------|------|------|
| 理解陌生程式庫 | `這個專案的認證流程怎麼運作？列出相關檔案。` | 標準 |
| 跨檔案的功能實作 | `/plan 新增訂單取消 API，含 service、controller 與測試` | Plan → 標準或 Autopilot |
| 修 Bug | `重現 #482 的錯誤，找出根因並補回歸測試` | 標準 |
| Git 與 PR 操作 | `把這個分支 rebase 到 main 並解決 package.json 的衝突` | 標準 |
| 大量但規則明確的修改 | `把所有 class component 改成 function component，逐一跑測試` | Autopilot＋`/fleet` |
| CI/CD 自動化 | `copilot -p "摘要本次 PR 變更" -s` | 程式化 |
| 旁支工作 | `/delegate 更新 README 中過時的安裝說明` | cloud agent |

#### 1.4.2 不適合或需要額外控制的場景

| 場景 | 原因 | 替代做法 |
|------|------|------|
| 在家目錄或含機敏資料的目錄啟動 | 代理可讀取工作目錄下所有檔案 | 只在專案目錄啟動；機敏路徑設定 Sandbox `deniedPaths` |
| 需求模糊的開放式探索搭配 Autopilot | 代理會「盡力完成」，可能產出大量無用變更 | 先用 Plan 模式釐清，再切換 Autopilot |
| 直接操作正式環境 | 指令可能不可逆 | 只在開發環境使用；正式環境變更走 CI/CD 與人工核准 |
| 處理不受信任的 Repo 或 PR | 提示注入風險高 | 啟用 Sandbox、不使用 `--allow-all`、不信任該資料夾 |

### 1.5 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 導入評估文件中的產品描述 | 把 `gh copilot` 與 `copilot` 當成同一產品 | 明確區分已退役的 `gh copilot` 與代理式 `copilot` | 執行 `copilot --version`，確認是 GitHub Copilot CLI 1.0.x |
| 工具選型建議 | 「CLI 可以完全取代 IDE」 | 說明 CLI、IDE、cloud agent 的分工與接力方式 | 對照 1.3 節表格，檢查建議是否說明執行位置與權限差異 |
| 使用情境規劃 | 對模糊需求直接建議 Autopilot＋`--allow-all` | 模糊需求先 Plan，再依風險選擇核准模式 | 檢查每個情境是否標註模式與權限設定 |
| 風險描述 | 只寫「AI 可能出錯」 | 具體指出權限邊界、提示注入、未經驗證的完成宣稱三類風險 | 對照 1.2 節三個後果，逐項確認有對應控制措施 |

---

## 第 2 章：企業架構與治理模型

> **本章目標**
>
> - 說明 Copilot CLI 在企業 SDLC 中的位置，以及哪些企業控制會影響它。
> - 理解設定的六層覆寫順序，知道每一種控制該放在哪一層。
> - 能規劃「試點 → 擴大 → 全面」的導入路線，並定義各角色的責任。

### 2.1 Copilot CLI 在企業架構中的位置

```mermaid
flowchart TB
    subgraph ORG["GitHub Enterprise／Organization"]
        P1[Copilot 授權與 CLI 政策]
        P2[模型啟用政策]
        P3[MCP Registry 與 Allowlist]
        P4[Content Exclusion]
        P5[伺服器端受管設定]
    end
    subgraph DEV["開發者工作站"]
        MDM[MDM 受管設定／Policy Hooks]
        CLI[Copilot CLI]
        SB[本機 Sandbox（MXC）]
        REPO[Repo：指引、agents、skills、hooks、MCP 設定]
    end
    subgraph CLOUD["GitHub 雲端"]
        CCA[Copilot cloud agent]
        CSB[雲端 Sandbox]
        API[Copilot 模型路由]
    end
    subgraph CI["CI/CD"]
        GHA[GitHub Actions：copilot -p]
    end
    ORG --> CLI
    MDM --> CLI
    REPO --> CLI
    CLI --> SB
    CLI --> API
    CLI -->|"/delegate"| CCA
    CLI -->|"--cloud"| CSB
    GHA --> API
```

#### 2.1.1 會影響 Copilot CLI 的企業控制

依官方〈Administering Copilot CLI for your enterprise〉文件整理：

| 控制 | 對 CLI 的影響 | 設定位置 |
|------|------|------|
| Copilot CLI 啟用政策 | 關閉後該組織授權的使用者無法使用 CLI | Enterprise／Organization → Copilot → Features & clients |
| 模型啟用 | `/model` 只會列出企業已啟用的模型；企業自備金鑰的模型會出現在清單底部 | Enterprise 模型政策 |
| Custom agents | 組織或企業層級的 custom agent 可在 CLI 中使用 | `.github-private` Repo 的 `agents/` |
| Content exclusion | 被排除的檔案不會作為 context | Enterprise／Organization／Repo 設定 |
| MCP 政策 | Registry URL 會成為探索來源，Allowlist 限制可執行的伺服器 | MCP 政策設定 |
| Cloud agent 啟用 | **CLI 與 cloud agent 兩個政策都開啟**，`/delegate` 才能使用 | Copilot 政策 |
| 稽核日誌 | 影響 CLI 的政策變更會記錄在企業稽核日誌 | Enterprise audit log |
| 座位指派 | 必須有 Copilot 授權才能使用 | 授權管理 |
| **不適用**的控制 | IDE 專屬的政策（某個編輯器或擴充套件的設定）不影響 CLI | — |

> ⚠️ **注意**：使用者在本機以環境變數設定的 BYOK 模型**不受企業模型政策控制**（官方文件明載）。如果組織需要禁止 BYOK，必須透過受管設定的 `forceLoginOrgs`（會拒絕 BYOK／API key 驗證）或端點管理工具處理，詳見第 15 章。

### 2.2 設定的六層覆寫順序

Copilot CLI 的設定依下列順序套用，**後面的覆寫前面的**：

| 順序 | 層級 | 位置 | 誰管理 |
|------|------|------|------|
| 1 | 內建預設值 | 程式內建 | GitHub |
| 2 | MDM／伺服器受管設定 | macOS plist、Windows 登錄檔或 `managed-settings.json`；伺服器端政策 | 企業 IT |
| 3 | 使用者設定 | `~/.copilot/settings.json` | 開發者 |
| 4 | Repo 設定 | `.github/copilot/settings.json`（commit 進 Repo） | 技術負責人 |
| 5 | 本機設定 | `.github/copilot/settings.local.json`（加入 `.gitignore`） | 開發者 |
| 6 | 環境變數 → 指令列旗標 | `COPILOT_*`、`--model` 等 | 執行者 |

但有三個重要的例外，治理設計時必須記住：

1. **`permissions.disableBypassPermissionsMode`**：MDM 設為 `"disable"` 時永遠生效，帳號切換也無法覆寫。
2. **`sandbox` 受管設定是「下限」**：受管值設定的是使用者不能放寬的底線，使用者自己的值若更寬鬆，以受管值為準。
3. **Repo 設定只接受白名單內的鍵**（`model`、`effortLevel`、`deniedUrls`、`hooks` 等 14 個），其他鍵一律靜默忽略；而且 `deniedUrls`、`disabledMcpServers` 等清單採「聯集、只能加不能減」，`respectGitignore` 只能收緊。完整清單見[附錄 D](#附錄-d設定檔與設定鍵)。

```mermaid
flowchart LR
    A[內建預設] --> B[MDM／伺服器受管設定]
    B --> C[使用者 settings.json]
    C --> D[Repo settings.json]
    D --> E[settings.local.json]
    E --> F[環境變數]
    F --> G[指令列旗標]
    B -. 受管 sandbox 為下限、disableBypassPermissionsMode 不可覆寫 .-> G
```

#### 2.2.1 控制要放在哪一層

| 想達成的效果 | 正確的層級 | 錯誤的做法 |
|------|------|------|
| 全公司禁止 `--allow-all`／`--yolo` | MDM 受管設定 `permissions.disableBypassPermissionsMode: "disable"` | 寫在 Repo 的 `copilot-instructions.md` 請 AI「不要用」 |
| 某個 Repo 固定使用某個模型 | Repo 設定 `model` | 每位開發者自己改使用者設定 |
| 某個 Repo 禁止連到特定網站 | Repo 設定 `deniedUrls` | 只在 README 提醒 |
| 強制所有人啟用 Sandbox | 受管設定 `sandbox.enabled: true` | Repo 設定 `sandbox`（Repo 層級不支援，會被忽略） |
| 攔截危險指令 | Repo 的 `.github/hooks/*.json` 或 Policy Hooks | 只靠提示詞 |

> ✅ **原則**：**能用設定強制的，不要用提示詞要求**。提示詞（custom instructions）是「建議」，模型可能不遵守；設定、hooks 與 Sandbox 是「強制」。

### 2.3 角色與責任（RACI）

| 工作項目 | 平台／DevEx 團隊 | 資安團隊 | 技術負責人 | 開發者 |
|------|------|------|------|------|
| 啟用 CLI 政策、指派座位 | R | C | I | I |
| MDM 受管設定（權限、Sandbox、MCP allowlist） | R | A | C | I |
| Policy Hooks（機器層級） | R | A | I | I |
| Repo 指引、agents、skills | C | C | A | R |
| Repo hooks 與 MCP 設定 | C | A | R | C |
| 每日使用與產出審查 | I | I | C | R |
| 成本與用量監控 | R | I | C | I |

R＝負責執行、A＝最終負責、C＝諮詢、I＝告知。

### 2.4 導入路線圖

```mermaid
flowchart LR
    S1["階段 1：試點<br/>2～4 週<br/>5～10 位資深工程師"] --> S2["階段 2：擴大<br/>1～2 個月<br/>單一事業部"]
    S2 --> S3["階段 3：全面<br/>依組織規模<br/>全公司"]
```

| 階段 | 目標 | 必要交付 | 進入下一階段的條件 |
|------|------|------|------|
| 1 試點 | 驗證價值與風險 | 受管設定草案、Repo 指引範本、hook 政策、用量基準 | 無資安事件；用量與成本在預算內；試點者回饋可行 |
| 2 擴大 | 建立標準與教育訓練 | 本手冊的內部版、Review Checklist（各章 N.x 節）、內部 plugin marketplace | 標準指引覆蓋 80% 以上的 Repo；Hook 稽核日誌可查 |
| 3 全面 | 規模化與持續改善 | 預算與 cost center、季度版本升級流程（第 18 章）、生產力指標 | 定期檢討，持續調整 |

### 2.5 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 治理設計文件 | 用 Repo 設定強制 Sandbox | 用 MDM／伺服器受管設定的 `sandbox`（作為下限） | 對照附錄 D 的 Repo 可覆寫鍵清單；用 `check_config.py repo-settings` 檢查 |
| 「禁止 YOLO」的實作 | 在 `copilot-instructions.md` 寫「不要使用 --yolo」 | 受管設定 `permissions.disableBypassPermissionsMode` | 在測試機套用後執行 `copilot --yolo`，確認出現政策警告 |
| BYOK 管控說明 | 「企業模型政策會限制所有模型」 | 註明本機 BYOK 不受企業模型政策控制，需 `forceLoginOrgs` 等措施 | 對照 2.1.1 節的注意事項與官方 admin 文件 |
| `/delegate` 可用性說明 | 只開啟 CLI 政策 | CLI 與 cloud agent 政策都要開啟 | 在測試帳號執行 `/delegate`，確認能建立草稿 PR |
| 導入計畫 | 直接全公司上線 | 分階段，每階段有明確的進入條件 | 檢查計畫是否包含 2.4 節的交付項目與條件 |

---

## 第 3 章：安裝、驗證與初始設定

> **本章目標**
>
> - 依作業系統與企業限制選擇正確的安裝方式，並能驗證安裝結果。
> - 理解五種驗證來源的優先順序，避免「用錯 Token」的常見事故。
> - 完成企業網路（Proxy、憑證、資料落地區域）下的初始設定。

### 3.1 系統需求

| 項目 | 需求 |
|------|------|
| 作業系統 | Linux、macOS、Windows（PowerShell 或 WSL） |
| Windows Shell | **PowerShell 6 以上**（建議 PowerShell 7）；CLI 會優先使用 `pwsh`，找不到才退回 `powershell.exe` |
| npm 安裝 | **Node.js 22 以上** |
| 訂閱 | 有效的 Copilot 授權；組織授權者需組織／企業**已啟用 Copilot CLI 政策** |
| 本機 Sandbox（選用） | macOS 15 以上；Linux 需 bubblewrap 0.5.0+ 等套件；Windows 需支援 Sandbox 的 Windows 11 版本（第 14 章） |

### 3.2 安裝方式

| 方式 | 平台 | 指令 | 更新方式 |
|------|------|------|------|
| npm | 全平台 | `npm install -g @github/copilot` | `npm install -g @github/copilot`（npm 安裝只會**提示**有新版，不會自動安裝） |
| WinGet | Windows | `winget install GitHub.Copilot` | `copilot update` 或 `winget upgrade` |
| Homebrew | macOS、Linux | `brew install --cask copilot-cli` | `copilot update` 或 `brew upgrade` |
| 安裝腳本 | macOS、Linux | `curl -fsSL https://gh.io/copilot-install \| bash` | `copilot update` |
| 直接下載 | 全平台 | 從 [github/copilot-cli Releases](https://github.com/github/copilot-cli/releases/) 下載對應平台執行檔 | 手動替換或 `copilot update` |

預發佈版：npm 用 `@github/copilot@prerelease`、WinGet 用 `GitHub.Copilot.Prerelease`、Homebrew 用 `copilot-cli@prerelease`。

#### 3.2.1 各方式的操作範例

```bash
# npm（全平台）
npm install -g @github/copilot

# 若 ~/.npmrc 設了 ignore-scripts=true，必須暫時解除，否則安裝不完整
npm_config_ignore_scripts=false npm install -g @github/copilot

# 安裝腳本：指定版本與安裝目錄（企業鎖版常用）
curl -fsSL https://gh.io/copilot-install | VERSION="v1.0.97" PREFIX="$HOME/.local" bash
```

```powershell
# Windows
winget install GitHub.Copilot
```

> ⚠️ **企業鎖版建議**：CI 與受管工作站請固定版本（npm 用 `@github/copilot@1.0.97`、安裝腳本用 `VERSION=`），並關閉自動更新（第 18 章），避免不同機器執行不同版本而產生難以重現的行為差異。

#### 3.2.2 驗證安裝

```bash
copilot --version     # 預期輸出：GitHub Copilot CLI 1.0.97.
copilot --help        # 能列出 Commands 與 Options 即表示可正常執行
```

### 3.3 身分驗證

#### 3.3.1 五種驗證來源與優先順序

CLI 每次執行時依下列順序尋找憑證，**找到第一個就使用**：

| 優先序 | 來源 | 典型用途 |
|------|------|------|
| 1 | `COPILOT_GITHUB_TOKEN` 環境變數 | CI/CD、只給 Copilot 用的 Token |
| 2 | `GH_TOKEN` 環境變數 | 與 GitHub CLI 共用 |
| 3 | `GITHUB_TOKEN` 環境變數 | GitHub Actions 內建 Token |
| 4 | 系統鑰匙圈中的 OAuth Token（`copilot login`／`/login` 產生） | 互動式使用 |
| 5 | GitHub CLI 的 Token（`gh auth token`） | 已登入 `gh` 時的備援 |

> ⚠️ **最常見的事故**：開發者為了其他工具在 shell 設定檔中匯出了 `GH_TOKEN`，結果 Copilot CLI **靜默改用**這個 Token，而不是 `copilot login` 登入的帳號。症狀是「明明登入了公司帳號，卻顯示沒有授權」或用錯帳號計費。排查方式是執行 `/user` 查看目前帳號與驗證來源（v1.0.96 起 `/user list` 會顯示每個帳號的驗證來源）。
>
> 例外：在 GitHub Codespaces 中自動注入的 `GITHUB_TOKEN` 不會優先於 `/login` 帳號；但你**明確匯出**的 `GITHUB_TOKEN` 仍會優先。

#### 3.3.2 支援的 Token 類型

| Token 類型 | 前綴 | 是否支援 | 說明 |
|------|------|------|------|
| OAuth Token（瀏覽器或裝置碼流程） | `gho_` | ✅ | `copilot login` 的預設方式 |
| Fine-grained PAT | `github_pat_` | ✅ | 必須由**個人帳號**擁有，並具備 **Copilot Requests** 帳號權限 |
| GitHub App user-to-server | `ghu_` | ✅ | 透過環境變數 |
| Classic PAT | `ghp_` | ❌ | **不支援** |

#### 3.3.3 互動式登入

```bash
copilot login                    # 本機桌面預設開啟瀏覽器（web flow）
copilot login --device-code      # SSH、Codespaces、容器、CI 等無瀏覽器環境
copilot login --host https://acme.ghe.com   # GitHub Enterprise Cloud 資料落地區域（*.ghe.com）
```

在互動式介面中則輸入 `/login`，依序選擇帳號類型（GitHub.com 或 `*.ghe.com`）與登入方式。組織若啟用 SAML SSO，授權頁面上需要對各組織按 **Authorize**。

登入後 Token 存放在系統鑰匙圈（服務名稱 `copilot-cli`）：macOS Keychain、Windows Credential Manager、Linux libsecret。若沒有可用的鑰匙圈（例如沒有安裝 libsecret 的無頭 Linux），CLI 會詢問是否以明文存入 `~/.copilot/config.json`；設定 `storeTokenPlaintext: true` 則不再詢問。

> ✅ **企業建議**：伺服器環境優先安裝 libsecret，或改用環境變數注入短效 Token；不要讓長效 Token 以明文留在共用主機上。

#### 3.3.4 以 PAT 非互動式驗證

1. 前往 <https://github.com/settings/personal-access-tokens/new>。
2. **Resource owner 選個人帳號**（不要選組織；Copilot Requests 權限只出現在個人擁有的 fine-grained PAT）。
3. 在 **Permissions → Account** 加入 **Copilot Requests**。
4. 產生 Token 後以環境變數提供，或從標準輸入讀入：

```bash
# 方式 A：環境變數（CI 推薦，搭配 Secret 管理）
export COPILOT_GITHUB_TOKEN="github_pat_xxx"

# 方式 B：從標準輸入讀入並存入鑰匙圈
copilot login --with-token < token.txt
```

GitHub Actions 中更推薦使用內建的 `GITHUB_TOKEN`（需 `copilot-requests: write` 權限，不必發 PAT），詳見第 16 章。

#### 3.3.5 多帳號、登出與撤銷

| 動作 | 指令 |
|------|------|
| 查看目前帳號 | `/user` 或 `/user show` |
| 列出所有帳號 | `/user list` |
| 切換帳號 | `/user switch` |
| 登出（只刪除本機 Token） | `/logout` |
| 撤銷授權 | GitHub → Settings → Applications → Authorized OAuth Apps → Revoke |

#### 3.3.6 不需要 GitHub 驗證的情境

使用自備模型（BYOK，設定 `COPILOT_PROVIDER_BASE_URL`）時可以不登入 GitHub，但 `/delegate`、內建 GitHub MCP 伺服器與 GitHub 程式碼搜尋都無法使用。設定 `COPILOT_OFFLINE=true` 會完全不連 GitHub（不驗證、不送遙測、不自動更新），只連到 BYOK 端點；**只有在 BYOK 端點本身也在隔離網路內時，才是真正的離線**。詳見第 12 章。

### 3.4 企業網路設定

#### 3.4.1 Proxy

| 設定 | 說明 |
|------|------|
| `HTTP_PROXY`／`HTTPS_PROXY`（大小寫皆可） | 優先於設定檔 |
| `NO_PROXY` | 不經 Proxy 的主機清單，例如 `localhost,127.0.0.1,.corp.example.com` |
| `proxyUrl`（settings.json） | 未設定環境變數時使用，例如 `http://proxy.corp.example:3128`；變更後需重新啟動 |
| `proxyKerberosServicePrincipal` 或 `COPILOT_PROXY_KERBEROS_SPN` | Kerberos／Negotiate Proxy 的 SPN（預設為 `HTTP/<proxy-host>`） |

```bash
# 用 copilot config 寫入使用者設定（不必手動編輯 JSON）
copilot config proxyUrl http://proxy.corp.example:3128
copilot config proxyUrl            # 讀回確認
```

v1.0.83 起支援 HTTPS Proxy 的 mTLS 用戶端憑證；v1.0.97 修正了 TLS 攔截型 Proxy 未送出 `close_notify` 時串流回應無法完成的問題。若公司 Proxy 會攔截 TLS，請**至少使用 v1.0.97**。

#### 3.4.2 GitHub Enterprise Cloud 資料落地區域與 GHES

| 變數 | 用途 |
|------|------|
| `GH_HOST` | GitHub CLI 與 Copilot CLI 共用的主機名稱，例如 `acme.ghe.com` |
| `COPILOT_GH_HOST` | 只給 Copilot CLI 用，優先於 `GH_HOST`。常見於 `GH_HOST` 指向 GHES，而 Copilot 需要對 github.com 或 `*.ghe.com` 驗證的情境 |

#### 3.4.3 設定與快取目錄

| 項目 | 預設位置 | 覆寫方式 |
|------|------|------|
| 設定與狀態 | `~/.copilot`（Windows：`%USERPROFILE%\.copilot`） | `COPILOT_HOME`（`--config-dir` 已棄用） |
| 快取（marketplace、更新套件） | macOS `~/Library/Caches/copilot`；Linux `$XDG_CACHE_HOME/copilot`；Windows `%LOCALAPPDATA%/copilot` | `COPILOT_CACHE_HOME` |

`COPILOT_HOME` 會取代**整個** `~/.copilot` 路徑；改了之後原有的設定、Session 與已安裝的 plugins 都不會被找到，需要自行搬移。完整目錄結構見[附錄 D](#附錄-d設定檔與設定鍵)。

### 3.5 首次啟動與初始設定

#### 3.5.1 首次啟動流程

```bash
cd ~/src/order-service     # 一定要在專案目錄啟動，不要在家目錄
copilot
```

1. **信任資料夾**：CLI 會詢問是否信任目前目錄（僅本次 Session，或本次與未來）。**信任後才會載入該 Repo 的 MCP 伺服器、hooks、skills 與 plugins**，所以不受信任的 Repo 請只選「本次」或直接拒絕。
2. **登入**：尚未登入時輸入 `/login`。
3. **專案指引**：若沒有 `.github/copilot-instructions.md`，CLI 會提示執行 `/init` 產生（第 6 章）。不想看到提示可用 `/init suppress`。

#### 3.5.2 建議的初始設定

```bash
copilot config theme github
copilot config autoUpdatesChannel stable
copilot config footer.showQuota on
copilot config footer.showAiUsed on
copilot config allowedUrls docs.github.com      # 清單型設定：附加一筆
copilot config --list                           # 列出全部設定
copilot config --repo --list --json             # 列出 Repo 設定（JSON）
```

在互動式介面中也可以用 `/settings`（或 `/config`）開啟設定畫面，或 `/settings KEY VALUE` 單行設定。按 <kbd>Ctrl</kbd>+<kbd>E</kbd> 可直接以編輯器開啟 `settings.json`，清單與巢狀結構的設定只能這樣修改。

| 建議設定 | 指令 | 理由 |
|------|------|------|
| 多行輸入 | `/terminal-setup` | 讓 <kbd>Shift</kbd>+<kbd>Enter</kbd> 換行（VS Code、Windows Terminal 等） |
| Shell 補全 | `source <(copilot completion bash)`（另支援 zsh、fish） | 補全子指令、旗標與 `copilot config` 的設定鍵 |
| 顯示用量 | `/statusline` 加入 `quota` 與 `ai-used` | 隨時掌握 AI Credits 消耗 |
| 共同作者標記 | `includeCoAuthoredBy`（預設 `true`） | commit 會加上 `Co-authored-by`，方便稽核 AI 參與的變更 |

### 3.6 常見安裝與驗證問題

| 症狀 | 可能原因 | 處理方式 |
|------|------|------|
| `copilot: command not found` | npm 全域 bin 不在 PATH | `npm prefix -g` 找出目錄並加入 PATH |
| 啟動後顯示沒有 Copilot 存取權 | 組織未啟用 CLI 政策，或未指派座位 | 請管理者檢查企業／組織政策；企業政策為「讓組織決定」時，至少要有一個授權組織啟用 CLI |
| 登入的帳號正確卻仍失敗 | 環境中的 `GH_TOKEN`／`GITHUB_TOKEN` 優先被使用 | `/user` 確認驗證來源；`unset GH_TOKEN` 後重試 |
| 使用 `ghp_` Token 失敗 | Classic PAT 不支援 | 改用 fine-grained PAT＋Copilot Requests 權限 |
| `401 Bad credentials` | Token 過期或被撤銷 | 重新 `copilot login`（v1.0.82 起會顯示具體失敗原因） |
| 企業網路下回應卡住 | TLS 攔截型 Proxy | 升級到 v1.0.97 以上；確認 `HTTPS_PROXY` 與 `NO_PROXY` |
| `settings.json` 設定沒生效 | JSON 格式錯誤或鍵名打錯 | 開 `/settings` 的 **Problems** 分頁查看錯誤；用 `check_config.py user-settings` 檢查 |
| 舊的設定寫在 `config.json` 失效 | v1.0.93 起使用者設定只讀 `settings.json` | 把設定搬到 `~/.copilot/settings.json` |

### 3.7 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 安裝說明 | `brew install copilot-cli` 未註明官方文件使用 `--cask` | `brew install --cask copilot-cli` | 對照官方安裝文件；在乾淨環境實際安裝一次 |
| CI 驗證設定 | 使用 classic PAT（`ghp_`） | fine-grained PAT＋Copilot Requests，或 Actions 內建 `GITHUB_TOKEN` | 檢查 Token 前綴；在 CI 跑一次 `copilot -p "hello" -s` |
| 驗證優先序說明 | 「`GITHUB_TOKEN` 優先於 `COPILOT_GITHUB_TOKEN`」 | `COPILOT_GITHUB_TOKEN` → `GH_TOKEN` → `GITHUB_TOKEN` → 鑰匙圈 → `gh` | `copilot help environment` 中的說明 |
| 使用者設定檔 | 把設定寫進 `~/.copilot/config.json` | 寫入 `~/.copilot/settings.json`，或用 `copilot config` | `copilot config --list` 讀回；`check_config.py user-settings` |
| Proxy 設定 | 同時設定 `proxyUrl` 與 `HTTPS_PROXY`，卻以為 `proxyUrl` 生效 | 了解環境變數優先，擇一設定 | `copilot config proxyUrl` 與 `env \| grep -i proxy` 比對 |
| 首次啟動指引 | 建議在家目錄啟動以便存取所有專案 | 在專案目錄啟動；多 Repo 用 `/add-dir` | 檢查文件中的 `cd` 路徑 |

---

## 第 4 章：互動介面與操作模式

> **本章目標**
>
> - 熟悉互動介面的輸入語法、快捷鍵與核准對話框，知道每個選項的影響範圍。
> - 能依任務選擇標準、Plan、Autopilot 模式，以及 `/fleet`、`/delegate`。
> - 學會在代理執行中途引導、取消與回溯，而不是等它做完再重來。

### 4.1 介面組成

| 區域 | 內容 |
|------|------|
| Timeline（對話時間軸） | 你的提示、代理的回應、工具呼叫與結果、權限決策（v1.0.96 起會標示是你、Assisted Permissions、政策或無人值守備援做的決定） |
| 輸入框 | 輸入提示、slash 指令或 shell 指令 |
| Footer（狀態列） | 模型、目錄、分支、Context 用量、AI Credits 配額、Sandbox 與 YOLO 狀態，可用 `/statusline` 調整 |
| Sessions 側欄 | 在空白輸入框按 <kbd>←</kbd> 開啟；可在多個 Session 之間切換 |
| 首頁分頁列 | Session、Agents、Issues、Pull requests、Gists，可用 `tabs` 設定隱藏或排序 |

#### 4.1.1 輸入語法

| 輸入 | 作用 | 範例 |
|------|------|------|
| `@檔案` | 把檔案內容加入 context | `解釋 @src/main/java/com/acme/order/OrderService.java` |
| `#編號` | 把 GitHub Issue 或 PR 加入 context | `依照 #482 的描述修正錯誤` |
| `! 指令` | 直接在本機 shell 執行，**不經過代理、不消耗 AI Credits** | `! git status` |
| `!`（單獨） | 進入 shell 模式，可連續執行多個指令；<kbd>Esc</kbd> 離開 | — |
| `$`（單獨＋Enter） | 把終端機交給真正的互動式 shell（`$SHELL`／`%COMSPEC%`），結束 shell 後回到 CLI | — |
| `?`（空白輸入框） | 開啟快速說明 | — |
| `/指令` | slash 指令 | `/model`、`/plan` |
| `&提示` | 等同 `/delegate`，交給 cloud agent | `& 補齊 README 的安裝章節` |

#### 4.1.2 最常用的快捷鍵

| 快捷鍵 | 作用 |
|------|------|
| <kbd>Shift</kbd>+<kbd>Tab</kbd> | 在標準、Plan、Autopilot 三種模式間切換 |
| <kbd>Esc</kbd> | 取消目前操作；執行中按兩下中斷；閒置時按兩下開啟回溯（rewind）選單 |
| <kbd>Ctrl</kbd>+<kbd>C</kbd> | 立即取消並清除排隊的提示；連按兩下離開 |
| <kbd>Ctrl</kbd>+<kbd>Q</kbd> 或 <kbd>Ctrl</kbd>+<kbd>Enter</kbd> | 代理忙碌時把訊息排入佇列 |
| <kbd>↑</kbd>（空白輸入框） | 取回最近排隊或引導中的提示來修改 |
| <kbd>Ctrl</kbd>+<kbd>X</kbd> 接 <kbd>/</kbd> | 已經打了一半提示時，插入 slash 指令（例如中途換模型） |
| <kbd>Ctrl</kbd>+<kbd>X</kbd> 接 <kbd>b</kbd> | 把執行中的任務或 shell 指令移到背景 |
| <kbd>Ctrl</kbd>+<kbd>G</kbd> | 用外部編輯器（`$EDITOR`）撰寫提示 |
| <kbd>Ctrl</kbd>+<kbd>R</kbd> | 反向搜尋指令歷史 |
| <kbd>Ctrl</kbd>+<kbd>O</kbd>／<kbd>Ctrl</kbd>+<kbd>E</kbd> | 空白輸入框時展開最近／全部的 timeline 項目 |
| <kbd>Ctrl</kbd>+<kbd>T</kbd> | 顯示或隱藏推理過程 |
| <kbd>Ctrl</kbd>+<kbd>V</kbd>／<kbd>Alt</kbd>+<kbd>V</kbd> | 貼上剪貼簿內容／圖片作為附件 |

完整快捷鍵見[附錄 A](#附錄-a指令與-slash-指令速查)。

### 4.2 權限核准對話框

代理第一次要使用可能修改或執行檔案的工具（例如 `touch`、`chmod`、`node`、`sed`）時，會跳出核准對話框：

```text
1. Yes
2. Yes, and approve TOOL for the rest of the running session
3. No, and tell Copilot what to do differently (Esc)
```

| 選項 | 範圍 | 風險 |
|------|------|------|
| 1. Yes | 只允許這一次 | 最低 |
| 2. 本 Session 不再詢問 | 目前執行中的 Session，代理可用**任何方式**使用該工具 | 核准 `rm ./a.txt` 等於也核准了 `rm -rf ./*` |
| 3. No，並給回饋 | 拒絕，並以文字告訴代理改用什麼方法 | 代理會調整做法，而不是停止 |

在完整對話框中還有持久化選項：**Once**（一次）、**This location**（存到磁碟，同一個 Git 根目錄或目錄下次不再詢問）、**Always**（寫入設定檔）。也可以用單鍵回應：<kbd>y</kbd> 允許一次、<kbd>n</kbd> 拒絕一次、<kbd>!</kbd> 本 Session 允許所有同類請求、<kbd>#</kbd> 本 Session 拒絕所有同類請求、<kbd>?</kbd> 查看詳細資訊。

> ✅ **原則**：對**唯讀**或**範圍明確**的指令（`git status`、`./mvnw test`）可以選「本 Session 不再詢問」；對 `rm`、`git push`、`curl`、套件安裝等指令，一律逐次核准。`/permissions reset` 只清除本 Session 記憶體中的核准；`/reset-allowed-tools` 還會一併清除目前位置存在 `permissions-config.json` 的「This location」核准。

### 4.3 三種操作模式

```mermaid
stateDiagram-v2
    [*] --> 標準模式
    標準模式 --> Plan模式: Shift+Tab
    Plan模式 --> Autopilot模式: Shift+Tab
    Autopilot模式 --> 標準模式: Shift+Tab
    Plan模式 --> 標準模式: 核准計畫後實作
    Plan模式 --> Autopilot模式: 核准計畫並以 Autopilot 執行
```

| 模式 | 行為 | 適合 | 啟動方式 |
|------|------|------|------|
| 標準（interactive） | 每個需要核准的動作都會詢問；遇到決策點會問你 | 大多數開發工作 | 預設 |
| Plan | 先分析、提問釐清，產生結構化計畫，**核准前不修改專案檔案** | 多檔案變更、重構、新功能 | <kbd>Shift</kbd>+<kbd>Tab</kbd>、`/plan 提示`、`--plan` |
| Autopilot | 自主連續執行直到任務完成、遇到問題、按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 或達到延續上限 | 規格明確、可驗證的大型任務 | <kbd>Shift</kbd>+<kbd>Tab</kbd>、`/autopilot`、`--autopilot` |

#### 4.3.1 Plan 模式

```text
/plan 新增「取消訂單」功能：
- API：POST /api/v1/orders/{id}/cancel
- 只有狀態為 CREATED 或 PAID 的訂單可以取消；PAID 需觸發退款事件
- 需要 service 單元測試與 controller 的 @WebMvcTest
- 不要修改既有的 Flyway 遷移檔
```

Plan 模式的運作：

1. 代理分析需求與程式碼，**主動提出釐清問題**。
2. 產生含核取方塊的實作計畫，存成 Session 資料夾中的 `plan.md`（可用 `/session plan` 查看，<kbd>Ctrl</kbd>+<kbd>Y</kbd> 以編輯器開啟）。
3. 等你核准。核准選項包含「實作」、「Accept plan and continue in Autopilot execution mode」，以及再加上 `/fleet` 的平行執行選項。

> ⚠️ **Plan 模式的保護是「安全網」，不是「保證」**。官方文件說明：Plan 模式會**直接封鎖**修改工作區檔案的編輯、patch 與 shell 指令（不是靠模型自律），子任務也繼承同樣限制；但為了不妨礙研究，**效果無法事先判斷的 shell 指令與 MCP 工具呼叫**仍可能被放行。因此在 Plan 模式下仍要看清楚核准對話框。

為 Plan 模式指定不同的模型：`/model plan`（或 `/config model` 的 plan 選項），例如用推理力較強的模型規劃、較便宜的模型實作。

#### 4.3.2 Autopilot 模式

進入 Autopilot 時，若尚未授予全部權限，CLI 會詢問：

```text
1. Enable all permissions (recommended)
2. Use Manual Approval for this session
3. Cancel (Esc)
```

選 2 時，任何需要核准的工具請求都會被**自動拒絕**（沒有人可以回答），任務可能因此無法完成。

| 控制 | 說明 |
|------|------|
| `--max-autopilot-continues N` | 自動延續訊息的上限；本機 v1.0.97 `--help` 顯示預設為 5 |
| `/autopilot 目標`（別名 `/goal`） | 明確設定目標；可用 `--max-ai-credits` 限制本次花費 |
| `stayInAutopilot`（預設 `true`） | 任務完成後是否停留在 Autopilot；設為 `false` 則自動回到標準模式 |
| `defaultMode` | 新互動 Session 的起始模式（`interactive`、`plan`、`autopilot`） |
| preToolUse hook 回傳 `ask` | Autopilot 下會被視為拒絕（v1.0.97），代理會知道無法詢問使用者 |

**Plan-then-autopilot**：`copilot --plan --mode autopilot` 會從 Plan 模式開始，計畫完成後**不等人工核准**就自動進入 Autopilot。這等於把「審查計畫」這個關卡拿掉，只建議用在已有其他控制（Sandbox、受限權限、CI 測試）的情境。

> ✅ **Autopilot 使用守則**
>
> 1. 先用 Plan 模式產生並**人工審查**計畫，再切換 Autopilot。
> 2. 給予全部權限前先啟用本機 Sandbox（第 14 章），或在雲端 Sandbox 執行。
> 3. 設定延續上限與 AI Credits 上限，避免失控。
> 4. 任務要有**可自動驗證的完成條件**（例如「`./mvnw verify` 全部通過」）。

#### 4.3.3 Autopilot、`--allow-all` 與 `--no-ask-user` 的差異

| 選項 | 會自動核准工具嗎 | 會自動延續下一步嗎 | 會問你釐清問題嗎 |
|------|------|------|------|
| `--allow-all`／`--yolo` | ✅ | ❌（仍是正常對話流程） | ✅ |
| `--no-ask-user` | ❌ | ❌ | ❌（代理自行決定） |
| Autopilot＋全部權限 | ✅ | ✅ | 盡量不問 |

### 4.4 `/fleet`：平行子代理

`/fleet` 讓主代理把任務拆成**彼此獨立**的子任務，交給多個子代理平行執行；每個子代理有自己的 context window。

```text
/fleet 為 order、payment、inventory 三個模組分別補齊 service 層單元測試，
每個模組獨立完成，使用 @test-writer 代理，完成後各自執行 ./mvnw -pl <模組> test
```

| 要點 | 說明 |
|------|------|
| 適合 | 可拆成互不相依的子任務（多模組測試、多檔案重構） |
| 不適合 | 本質上有先後順序的任務；拆開反而沒有效益 |
| 子代理模型 | 預設使用低成本模型；可在提示中指定模型或 `@自訂代理` |
| 成本 | 每個子代理獨立呼叫模型，**總 AI Credits 通常比單一代理高** |
| 同時執行上限 | 依方案：Free／Education 2、Pro／Pro+ 4、Max 8、Business 16、Enterprise 32 |
| 指令列 | `copilot --fleet -p "..."`（不支援 ACP 模式） |

用 `/tasks` 檢視與管理子代理和背景 shell：<kbd>Enter</kbd> 可「傳送」進子代理的畫面直接引導它，<kbd>X</kbd> 終止、<kbd>B</kbd> 移到背景。

### 4.5 `/delegate`：交給 Copilot cloud agent

```text
/delegate 補齊 API 整合測試並修正失敗的邊界案例
```

或在提示前加 `&`。CLI 會先詢問是否把未 stage 的變更 commit 成新分支上的檢查點，接著 cloud agent 會開草稿 PR、在背景工作，完成後請你審查。

| 比較 | Autopilot | `/delegate` |
|------|------|------|
| 執行位置 | 本機 | GitHub 雲端 |
| 關機後 | 停止 | 繼續執行 |
| 產出 | 本機檔案變更 | 草稿 PR |
| 前提 | — | 已登入 GitHub；組織同時開啟 CLI 與 cloud agent 政策 |
| 指定目標分支 | — | `/delegate --base 分支` |

適合 `/delegate` 的工作：文件更新、獨立模組的重構、不必即時盯著的旁支任務。核心功能開發與除錯建議留在本機。

### 4.6 引導、取消與回溯

#### 4.6.1 在執行中引導代理

- 代理工作時直接輸入訊息並送出，就能**引導（steer）**目前的方向；連續送出的引導訊息會合併成一則。
- 想讓訊息排在目前回合之後才處理，用 <kbd>Ctrl</kbd>+<kbd>Q</kbd> 排入佇列。
- 拒絕某個權限請求時可附上文字回饋，代理會改變做法而不是停下來。

#### 4.6.2 取消

| 情況 | <kbd>Esc</kbd> | <kbd>Ctrl</kbd>+<kbd>C</kbd> |
|------|------|------|
| 代理執行中 | 第一下顯示提醒，半秒內再按一下才中斷 | 立即中斷，並清除排隊的提示 |
| 權限對話框開啟中 | 按一下即拒絕該請求 | 中斷 |
| 閒置且輸入框為空 | 按兩下開啟回溯選單 | 連按兩下離開 CLI |

#### 4.6.3 回溯（rewind）

閒置時按兩下 <kbd>Esc</kbd>，或輸入 `/rewind`（別名 `/undo`），選擇要回到哪一個提示之前：

| 選項 | 效果 |
|------|------|
| Conversation only | 只回溯對話，檔案不變 |
| Conversation + files | 同時把**代理在那之後改過的檔案**還原；你自己後來改過的檔案會被略過，不會被覆蓋 |

無法還原的情況：單一檔案超過 10 MB、單一回合修改超過 500 個檔案、在檔案追蹤功能啟用前建立的 Session、遠端 Session 或仍在執行中的 Session。

> ⚠️ 回溯不能取代 Git。重要的變更請先 commit，或在 `/worktree` 中進行（第 7 章）；回溯只是「快速撤銷最近幾步」的工具。

### 4.7 其他常用互動功能

| 指令 | 用途 | 注意事項 |
|------|------|------|
| `/ask 問題`（別名 `/btw`） | 問一個旁支問題，**不加入對話歷史** | 適合查語法，不污染主任務 context |
| `/research 主題` | 由 research 子代理使用 GitHub 搜尋與網路來源做深入研究 | 會產生研究報告，可用 `/share research` 匯出 |
| `/rubber-duck 提示` | 由**不同模型**的 rubber-duck 子代理批評目前的計畫、程式或測試 | 只審查、不改檔；可在 `/subagents` 開啟主動呼叫 |
| `/review 提示` | 由 code-review 子代理審查變更 | 只回報真正的問題（bug、安全、競態），不談風格 |
| `/security-review` | 針對本機已變更的程式碼做安全審查 | 不是完整的 Repo 安全稽核（第 8 章） |
| `/diff` | 檢視目前目錄的變更，可逐行留言並一次送給代理 | 工作區乾淨時自動切到分支 diff |
| `/refine 文字` | 把口語化、雜亂的提示改寫成清楚的提示 | 也可在輸入中途用 <kbd>Ctrl</kbd>+<kbd>X</kbd> 接 `/refine` |
| `/every`、`/after` | 在目前 Session 排程重複或延遲執行的提示 | 實驗性功能 |
| `/vim` | 輸入框的 Vim 模式（v1.0.85 起開放所有人） | 設定鍵 `editorMode` |
| `/voice` | 語音聽寫（透過 Foundry Local 在本機轉錄） | <kbd>Ctrl</kbd>+<kbd>Space</kbd> 切換 |

### 4.8 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 操作手冊中的核准建議 | 「遇到權限詢問一律選 2 以節省時間」 | 唯讀與範圍明確的指令才選 2；破壞性指令逐次核准 | 檢查文件是否區分指令風險等級 |
| Autopilot 執行計畫 | 直接 `copilot --plan --mode autopilot --yolo` 處理模糊需求 | 先 Plan 並人工審查，再 Autopilot；搭配 Sandbox 與上限 | 確認有延續上限、AI Credits 上限與可自動驗證的完成條件 |
| `/fleet` 任務拆分 | 把有先後順序的遷移步驟交給 `/fleet` | 只把互不相依的子任務平行化 | 畫出子任務相依圖，確認沒有相依邊 |
| 回溯操作說明 | 「rewind 可以還原所有變更，不用 commit」 | 說明 10 MB／500 檔／手動修改不覆蓋等限制，重要變更仍要 commit | 在測試 Repo 修改大檔後實際回溯一次 |
| `/delegate` 說明 | 「delegate 會在本機背景執行」 | 在 GitHub 雲端執行並開草稿 PR | 執行後確認 GitHub 上出現草稿 PR 與 agent session 連結 |
| 快捷鍵與指令 | 寫出不存在的指令（例如舊版手冊的 new-worktree） | 以 `copilot help commands` 為準 | `check_flags.py` 檢查文件中所有 slash 指令 |

---

## 第 5 章：Context 工程

> **本章目標**
>
> - 理解 context window 由哪些內容組成，以及自動壓縮會失去什麼。
> - 學會用 `@`、`#`、`/add-dir`、圖片附件精準提供 context，而不是讓代理盲目搜尋。
> - 知道 Copilot Memory 會記住什麼、保存多久、誰看得到。

### 5.1 Context window 的組成

模型每次回應時能看到的全部資訊稱為 context window，以 token 計算，大小依模型而定。它包含：

| 組成 | 說明 | 可控性 |
|------|------|------|
| 系統提示 | CLI 內建的行為指示 | 不可控 |
| Custom instructions | 你的 `copilot-instructions.md`、`AGENTS.md` 等 | 可控：寫精簡 |
| 系統工具定義 | 內建工具的 schema | 部分可控：`--available-tools` |
| MCP 工具定義 | 每個 MCP 伺服器的工具 schema | 可控：只啟用需要的伺服器與工具 |
| 對話歷史 | 你的提示、代理的回應 | 可控：`/new`、`/compact` |
| 工具呼叫與結果 | 讀檔、指令輸出、搜尋結果；**通常是最大宗** | 可控：精準引用檔案 |

用 `/context` 查看各部分的 token 數與百分比。單一工具輸出超過 20 KiB 時會被存成暫存檔，模型只收到路徑與預覽（門檻可用 `COPILOT_LARGE_OUTPUT_THRESHOLD_BYTES` 調整）。

> 💡 **Tool search（延遲載入工具）**：工具數量很多時，CLI 會只先提供工具名稱，需要時再載入完整定義，以節省 context。這個行為由模型與功能決定，可用設定 `toolSearch: false` 關閉。

### 5.2 自動壓縮（Compaction）與檢查點

| 時機 | 行為 |
|------|------|
| 約 80% 容量 | 背景開始壓縮，保留約 20% 緩衝讓工具呼叫繼續執行 |
| 約 95% 容量且壓縮尚未完成 | 等待壓縮完成才繼續 |
| 手動 | `/compact`，可加上重點提示，例如 `/compact 保留訂單取消 API 的設計決策` |

壓縮會把對話送給模型產生結構化摘要（目標、已完成事項、關鍵技術細節、重要檔案、下一步），再以摘要取代舊歷史；**原始使用者指示、計畫與待辦清單會保留**。每次壓縮都會建立檢查點：

```text
/session checkpoints        # 列出所有檢查點
/session checkpoints 2      # 查看第 2 個檢查點的摘要內容
```

> ⚠️ **壓縮會遺失細節**：每一則訊息的原文、指令的完整輸出、早期的小決定都可能不在摘要中。重要的決定要寫進檔案（例如 `plan.md` 或 ADR），不要只存在對話裡。發現代理「忘記」先前的決定時，先查最新的檢查點。

### 5.3 精準提供 context

#### 5.3.1 `@` 引用檔案

```text
@src/main/java/com/acme/order/OrderService.java 的 cancel() 為什麼在並發時會重複退款？
參考 @src/test/java/com/acme/order/OrderServiceTest.java 的既有測試寫法，補一個並發測試。
```

| ❌ 模糊 | ✅ 精準 |
|------|------|
| `訂單取消有 bug，幫我修` | `@OrderService.java 的 cancel() 在兩個請求同時進來時會呼叫兩次 refund()，請找出原因並以樂觀鎖修正` |
| `看一下設定` | `比較 @application.yml 與 @application-prod.yml 的資料庫連線池設定差異` |

`@` 選單預設排除 `.gitignore` 中的檔案；需要引用被忽略的目錄時，設定 `respectGitignore: false`。

#### 5.3.2 `#` 引用 GitHub 資源

```text
依照 #482 的重現步驟找出根因，修正後在 PR 描述中引用 #482
```

輸入 `#` 會出現自動完成選單。也可以直接貼上完整網址，例如 `https://github.com/acme/order-service/issues/482`。

#### 5.3.3 圖片與附件

| 方式 | 說明 |
|------|------|
| 拖放圖片到輸入框 | 支援 PNG、JPEG、WebP、GIF；BMP、TIFF 會被標示為不支援的格式 |
| <kbd>Ctrl</kbd>+<kbd>V</kbd>／<kbd>Alt</kbd>+<kbd>V</kbd> | 貼上剪貼簿內容／圖片 |
| `@mockup.png` | 以檔案路徑引用 |
| `--attachment 路徑` | 程式化模式附加檔案（圖片或文件），可重複使用 |

```text
依照 @docs/design/order-list.png 實作 web/src/views/OrderList.vue，
間距與欄位順序要完全一致，完成後列出與設計稿不同的地方
```

使用圖片前要確認所選模型支援視覺輸入，且組織政策允許。

### 5.4 多 Repo 與目錄存取

預設只能存取**啟動目錄及其子目錄**與系統暫存目錄。要跨 Repo 工作有兩種方式：

| 方式 | 指令 | 適合 |
|------|------|------|
| 從父目錄啟動 | `cd ~/src && copilot` | 多個相關 Repo 放在同一層（微服務） |
| 動態加入目錄 | `/add-dir /home/me/src/shared-lib` 或啟動時 `--add-dir` | 以一個 Repo 為主，偶爾需要另一個 |

```text
/add-dir /home/me/src/api-gateway
/add-dir /home/me/src/auth-service
/list-dirs
我要修改使用者認證 API，變更涉及 api-gateway 的路由、auth-service 的核心邏輯。
先畫出目前兩邊的呼叫流程，不要修改任何檔案。
```

> ⚠️ **`/add-dir` 是信任決定**：加入的目錄除了可以存取檔案，其 `.github/skills` 與 `.github/agents` 也會被當成**受信任的設定**載入。不要加入來源不明的目錄。啟用 Sandbox 時，`/add-dir` 也會授予 Sandbox 對該目錄的存取權（v1.0.96）。

### 5.5 Copilot Memory

Copilot Memory 讓代理跨 Session 記住事實，目前為公開預覽，CLI、cloud agent、code review 共用。

| 類型 | 內容 | 誰看得到 | 管理 |
|------|------|------|------|
| Repo 層級事實 | 程式慣例、架構決策、建置指令，**附有指向程式碼的引用** | 該 Repo 所有啟用 Memory 的使用者 | Repo 擁有者可檢視與刪除 |
| 使用者層級偏好 | 個人的工作偏好，可能引用你說過的話 | 只有本人；Business／Enterprise 管理者可匯出或刪除 | 本人可檢視與刪除 |

| 規則 | 說明 |
|------|------|
| 建立條件 | Repo 事實只會因**有寫入權限**且啟用 Memory 的使用者的操作而建立 |
| 使用前驗證 | 使用 Repo 事實前會比對目前分支的程式碼引用，**驗證通過才使用** |
| 保存期限 | 28 天未使用自動刪除；成功驗證並使用時重新計時 |
| 啟用 | 個人方案預設開啟；組織方案需管理者先開啟政策 |
| CLI 控制 | `/memory on\|off` 或設定 `memory`；程式化模式預設關閉，需 `--enable-memory` |
| 權限 | 只有主代理能寫入或投票；子代理只能讀取 |
| 匯入 | `copilot memories import 檔案.jsonl`（可加 `--dry-run` 驗證） |

> ✅ **Memory 與 custom instructions 的分工**：團隊必須遵守的規則寫在 `copilot-instructions.md`（commit 進 Repo、可審查、可版本控制）；Memory 適合代理自行學到的細節。**不要依賴 Memory 傳遞強制規範**，因為它會過期，而且內容不經過 Code Review。

### 5.6 讓 context 保持健康的習慣

| 習慣 | 做法 |
|------|------|
| 一個 Session 一個主題 | 不相關的任務用 `/new` 開新對話 |
| 旁支問題不進主線 | 用 `/ask` |
| 進入新階段前主動壓縮 | `/compact 保留：API 設計、測試策略；捨棄：除錯過程` |
| 精簡 MCP 工具 | 只啟用需要的伺服器與工具（第 9 章），用 `/context` 觀察 MCP 工具佔用 |
| 大量輸出先過濾 | 要求代理「只輸出失敗的測試名稱與錯誤訊息」 |
| 決策寫進檔案 | 重要決定寫進 `plan.md`、ADR 或 PR 描述 |

### 5.7 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 提示詞 | 不給檔案路徑，讓代理全專案搜尋 | 用 `@檔案` 與 `#Issue` 指定範圍 | 檢查提示是否包含具體檔案、函式或 Issue 編號 |
| 跨 Repo 作業 | 在家目錄啟動以存取所有 Repo | 在父目錄啟動或用 `/add-dir` 加入特定 Repo | `/list-dirs` 確認只授權必要目錄 |
| 長 Session 的成果 | 重要設計決策只存在對話中 | 寫入 `plan.md`／ADR | 壓縮後查看 `/session checkpoints`，確認決策仍在 |
| 團隊規範的落地 | 依賴 Copilot Memory 記住規範 | 寫進 `copilot-instructions.md` 並 commit | 檢查規範是否在版本控制中 |
| MCP 設定 | 啟用所有 MCP 伺服器的全部工具 | 只啟用需要的工具 | `/context` 查看 MCP Tools 佔用比例 |

---

## 第 6 章：Custom Instructions 與 Custom Agents

> **本章目標**
>
> - 知道 CLI 會從哪些位置讀取指引、如何合併，以及哪些寫法不會生效。
> - 能寫出精簡、可執行、可驗證的 Repo 指引與路徑專屬指引。
> - 能設計 custom agent（`.agent.md`），並理解內建子代理的分工與限制。

### 6.1 指引來源與合併規則

| 位置 | 範圍 | 備註 |
|------|------|------|
| `~/.copilot/copilot-instructions.md` | 個人，所有 Repo | `COPILOT_HOME` 會改變此路徑 |
| `~/.copilot/instructions/**/*.instructions.md` | 個人，模組化 | — |
| `.github/copilot-instructions.md` | Repo 全域 | 最主要的團隊指引 |
| `.github/instructions/**/*.instructions.md` | 路徑專屬 | 以 `applyTo` 指定適用檔案 |
| `AGENTS.md` | 代理指引 | 與其他代理工具共用的開放格式 |
| `CLAUDE.md`、`.claude/CLAUDE.md` | 代理指引 | 與 Claude Code 共用 |
| `GEMINI.md` | 代理指引 | 與 Gemini CLI 共用 |
| `.claude/rules/**/*.md` | 路徑專屬 | 以 `paths`（或 `applyTo`）指定，v1.0.89 起支援 |
| `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` 指定的目錄 | 額外來源 | 逗號分隔，可放 `AGENTS.md` 與 `*.instructions.md` |

Repo 與代理指引會在**標準位置**被找到：Repo 根目錄、目前工作目錄、兩者之間的目錄，以及代理正在處理的檔案路徑上的目錄（`.github/instructions/` 不搜尋中間目錄）。

**合併規則**（容易誤解的重點）：

1. 所有適用的檔案會**合併**使用，**沒有一般性的優先順序**；完全相同的內容會去重。因此不同檔案之間**不能互相矛盾**。
2. 路徑專屬指引只在 `applyTo` 符合代理正在處理的檔案時才載入。
3. 指引檔變更**不會套用到執行中的 Session**；要離開後 `copilot --continue` 恢復，或 `/new` 開新對話。

查看與控制目前載入的指引：

```bash
copilot instruction list          # 在 shell 列出這個目錄會載入的指引來源
copilot instruction list --json
```

在互動式介面中用 `/instructions` 檢視並逐一開關；用 `/env` 一次查看已載入的指引、MCP、skills、agents、hooks、plugins 與 LSP。完全不載入指引用 `--no-custom-instructions`。

### 6.2 撰寫 Repo 全域指引

#### 6.2.1 用 `/init` 產生初稿

```bash
copilot init        # 在 shell 執行；或在互動式介面輸入 /init
```

`/init` 會用一組**唯讀工具**分析程式庫，產生 `.github/copilot-instructions.md`，內容包含建置與測試指令、架構、慣例與技術棧。檔案已存在時，它會提出修改建議讓你逐項接受或拒絕。**產生的內容一定要人工審查**：AI 推論出的「慣例」可能只是程式庫中的歷史包袱。

#### 6.2.2 範例：企業 Java 專案的指引

```markdown
# 訂單管理系統：Copilot 專案指引

## 技術棧

- Java 21、Spring Boot 3.5、Spring Data JPA、PostgreSQL 17、Flyway
- 前端：Vue 3 + TypeScript（位於 `web/`，有自己的指引檔）

## 建置與測試（變更後一律執行）

- 編譯與單元測試：`./mvnw -q verify`
- 只跑單一測試類別：`./mvnw -q -Dtest=ClassName test`
- 靜態檢查：`./mvnw -q spotless:check`

## 架構規則

- 分層：`controller` → `service` → `repository`；controller 不得直接注入 repository。
- 對外 API 一律使用 DTO（Java `record`），不得回傳 JPA Entity。
- 例外統一由 `GlobalExceptionHandler` 轉成 RFC 9457 Problem Details。

## 程式碼慣例

- 建構子注入（`@RequiredArgsConstructor`），禁止欄位注入。
- JPA Entity 不使用 Lombok `@Data`（會產生不安全的 `equals/hashCode`）。
- 日誌使用 SLF4J 參數化訊息，禁止記錄個資與 Token。

## 交付規則

- Commit 訊息遵循 Conventional Commits，例如 `feat(order): add cancel API`。
- 不得修改 `src/main/resources/db/migration/` 中已存在的檔案。

詳細的 API 規範見 @docs/api-guidelines.md
```

這份範例的設計重點：

| 原則 | 範例中的做法 |
|------|------|
| 指令可直接執行 | 寫出完整指令 `./mvnw -q verify`，而不是「記得跑測試」 |
| 規則可被驗證 | 「controller 不得直接注入 repository」可以用 ArchUnit 或 grep 驗證 |
| 說明理由 | 「不使用 `@Data`（會產生不安全的 `equals/hashCode`）」，模型更容易遵守 |
| 精簡 | 約 30 行；細節用 `@docs/api-guidelines.md` 引用，而不是全部塞進來 |

#### 6.2.3 ❌／✅ 對照

| ❌ 不會生效或效果差 | ✅ 有效寫法 | 原因 |
|------|------|------|
| `請寫出高品質的程式碼` | `新增的 public 方法都要有對應的單元測試，執行 ./mvnw -q verify 必須通過` | 抽象要求無法執行，也無法驗證 |
| `絕對不可以 git push --force` | 用 hook 或 `--deny-tool='shell(git push)'` 強制 | 指引是建議，模型可能不遵守；安全規則要用設定強制 |
| `@~/company/rules.md` | `@docs/rules.md`（Repo 內的相對路徑） | 絕對路徑與 `~/` 開頭的引用不會被載入 |
| 在 `*.instructions.md` 中寫 `@other.md` | 把內容直接寫進檔案 | `*.instructions.md` 與 `GEMINI.md` **不展開** `@` 引用 |
| 300 行的指引包含整份程式規範 | 30～80 行核心規則＋路徑專屬指引 | 過長會稀釋效果，也佔用每一次請求的 context |
| `CLAUDE.md` 寫「用 Bash 工具」，`AGENTS.md` 寫「用 PowerShell」 | 統一寫法，或只維護一份並讓另一份引用 | 兩份會被同時載入，互相矛盾 |

### 6.3 路徑專屬指引

```markdown
---
applyTo: "src/main/java/**/controller/**/*.java"
---

# Controller 層規則

- 類別加 `@RestController` 與 `@RequestMapping("/api/v{n}/...")`，版本號放在路徑中。
- 請求物件加 `@Valid`，驗證失敗交由 `GlobalExceptionHandler` 處理，不在 controller 內 try/catch。
- 建立資源回傳 `201 Created` 並附 `Location` 標頭；刪除回傳 `204 No Content`。
- 分頁參數使用 `Pageable`，並以 `@PageableDefault(size = 20)` 限制預設筆數，最大 100 筆。
- 每個公開端點都要有對應的 `@WebMvcTest` 測試，至少涵蓋成功、驗證失敗、找不到資源三種情境。
```

| frontmatter 欄位 | 說明 |
|------|------|
| `applyTo` | 必填。glob 模式，多個以逗號分隔，例如 `"**/*.ts,**/*.tsx"` |
| `excludeAgent` | 選填。`"code-review"` 或 `"cloud-agent"`，讓該代理不讀取此檔 |

glob 速查：`*.py` 只符合目前目錄；`**/*.py` 遞迴符合；`src/*.py` 不含子目錄；`src/**/*.py` 含子目錄。

### 6.4 Custom Agents

Custom agent 是以 Markdown＋YAML frontmatter 定義的「專門化代理」。主代理會依 `description` 判斷是否把子任務交給它，**以子代理（subagent）執行，擁有獨立的 context window**，避免主對話被細節塞滿。

#### 6.4.1 存放位置與優先順序

| 優先序 | 範圍 | 位置 |
|------|------|------|
| 1（最高） | 使用者 | `~/.copilot/agents/` |
| 2 | 專案 | `.github/agents/`（從目前目錄往上到 Git 根目錄，越深越優先） |
| 3 | 專案 | `.claude/agents/`（同上） |
| 4 | 加入的目錄 | `--add-dir`／`/add-dir` 目錄下的 `.github/agents/` |
| 5 | Plugin | `<plugin>/agents/` |
| 6（最低） | 遠端 | 組織或企業的 agents（`.github` 或 `.github-private` Repo 的 `agents/`） |

**代理 ID** 由檔案相對於 `agents` 目錄的路徑決定：去掉 `.agent.md` 或 `.md`，子目錄分隔符號換成 `--`。例如 `agents/security/reviewer.agent.md` 的 ID 是 `security--reviewer`。ID 相同時優先序高者勝出；`name` 欄位**不影響**去重。

#### 6.4.2 frontmatter 欄位

| 欄位 | 必填 | 說明 |
|------|------|------|
| `description` | ✅ | 代理的用途與使用時機；主代理依此決定是否委派 |
| `name` | | 顯示名稱，也可用於 `--agent "名稱"` |
| `tools` | | 可用工具陣列，預設 `["*"]`；只要包含 `*` 就代表全部工具 |
| `model` | | 指定模型；未設定則繼承主代理。Session 模型為 Auto 時，子代理一律使用 Auto 解析出的模型 |
| `models` | | 依序嘗試的模型清單，使用第一個方案可用的模型；優先於 `model` |
| `modelPolicy` | | `"preferred"`（預設，可被 `/subagents` 覆寫）或 `"required"`（鎖定，不可覆寫） |
| `reasoningEffort` | | 預設推理強度，例如 `"high"` |
| `infer` | | 是否允許主代理自動委派，預設 `true` |
| `include-custom-instructions` | | 以子代理執行時是否讀取 Repo 指引，預設 `false` |
| `mcp-servers` | | 此代理專用的 MCP 伺服器，格式同 `mcp-config.json` |
| `hooks` | | 只在選用此代理時執行的 hooks（v1.0.97，見第 11 章） |

#### 6.4.3 範例：資安審查代理

```markdown
---
name: security-reviewer
description: 審查 Java / Spring Boot 變更中的安全弱點（注入、授權繞過、密鑰外洩、不安全反序列化）。當使用者要求 security review、資安檢查或提到 seccheck 時使用。
tools: ["view", "grep", "glob", "bash"]
model: claude-opus-5.5
reasoningEffort: high
include-custom-instructions: true
---

你是資深應用程式安全工程師，只負責審查，不修改任何檔案。

## 審查範圍

1. 以 `git diff origin/main...HEAD` 取得本分支變更，只審查變更到的檔案。
2. 依下列類別檢查：SQL/命令注入、授權檢查缺漏（`@PreAuthorize`）、敏感資料寫入日誌、
   硬編碼密鑰、不安全的反序列化、SSRF。

## 輸出格式

每個發現使用以下欄位，沒有把握（信心低於 80%）的項目不要列出：

| 欄位 | 說明 |
|------|------|
| 位置 | `檔案:行號` |
| 類別 | 上述類別之一 |
| 嚴重度 | Critical / High / Medium |
| 證據 | 引用實際程式碼 |
| 修正建議 | 具體到可直接套用 |

若沒有發現，明確回覆「未發現高信心弱點」，並列出你檢查過的檔案。
```

設計重點：

- `description` 同時寫出**能力**與**觸發條件**（「security review、資安檢查、seccheck」），主代理才能正確推論何時使用。
- `tools` 只給唯讀與 `bash`（用來執行 `git diff`），不給 `edit`／`create`，確保它「只審查不修改」。
- 要求**信心門檻**與**固定輸出格式**，產出才能被比對與追蹤。
- `include-custom-instructions: true` 讓它以子代理執行時也遵守 Repo 規範。

#### 6.4.4 建立與使用

建立：在互動式介面輸入 `/agent` → **Create new agent** → 選擇 Project（`.github/agents/`）或 User（`~/.copilot/agents/`）→ 由 Copilot 依描述產生，或手動填寫。建立後**重新啟動 CLI** 才會載入。

| 使用方式 | 範例 |
|------|------|
| slash 指令 | `/agent` 選擇代理後輸入提示 |
| 明確指示 | `用 security-reviewer 代理審查 src/main/java/com/acme/payment` |
| 推論 | `幫我做這個分支的 seccheck`（符合 description 中的觸發詞） |
| 程式化 | `copilot --agent security-reviewer -p "審查本分支的變更" -s` |
| 在 `/fleet` 中指定 | `... 使用 @security-reviewer 檢查付款模組 ...` |

#### 6.4.5 哪些代理會讀取 Repo 指引

| 代理 | 是否讀取 `copilot-instructions.md`／`AGENTS.md`／`CLAUDE.md` |
|------|------|
| Session 代理（預設，或以 `--agent` 選定的 custom agent） | ✅ |
| 內建 `general-purpose` 子代理 | ✅ |
| 內建 `explore`、`task`、`code-review` 子代理 | ❌ |
| 以子代理身分執行的 custom agent | 只有設定 `include-custom-instructions: true` 時 |

`--no-custom-instructions` 永遠優先：使用它時，即使代理設定了 `include-custom-instructions: true` 也不會讀取。

#### 6.4.6 Sidekick 代理

在代理定義加入 `sidekick:` 區塊，它就會在背景依事件自動執行（例如 `session.context_changed` 切換目錄或分支時、`user.message` 每則訊息時），把整理好的 context 放進 Session 收件匣。適合「切換分支時自動摘要最近變更」這類輔助工作。`behavior: restart` 每次觸發重新開始；`persistent` 維持同一個長時間執行的迴圈。

### 6.5 內建子代理

| 代理 | 預設模型（2026-10 文件快照） | 用途 | 會修改檔案嗎 |
|------|------|------|------|
| `explore` | gpt-5.4-mini | 快速探索程式庫，回答限 300 字內，可平行執行 | ❌ |
| `task` | gpt-5.6-luna（退回 gpt-5.4-mini、claude-haiku-4.5） | 執行測試、建置、lint；成功只回摘要，失敗回完整輸出 | 依權限 |
| `general-purpose` | claude-sonnet-4.6 | 需要獨立 context 的完整任務 | 依權限 |
| `code-review` | claude-sonnet-4.6 | 高訊噪比的程式審查，不談風格 | ❌ |
| `research` | claude-haiku-4.5 | 搜尋 GitHub 與網路，附引用的研究報告（`/research`） | ❌ |
| `rubber-duck` | 與主 Session **不同家族**的模型 | 對計畫、程式、測試提出建設性批評（`/rubber-duck`） | ❌ |
| `security-review` | claude-sonnet-4.6 | 11 類安全弱點，只回報可利用性信心超過 80% 的發現（`/security-review`） | ❌ |

> ⚠️ 預設模型會隨版本調整，表中是官方 command reference 在查證日的內容。要控制子代理的模型、推理強度與 context tier，用 `/subagents`（設定寫入 `subagents.agents.<名稱>`），值設為 `"inherit"` 代表沿用主 Session。

子代理的限制：

| 限制 | 預設 | 上限 | 說明 |
|------|------|------|------|
| 巢狀深度 | 6 | 256 | 只有用量計費使用者能用 `subagents.maxDepth` 調整 |
| 同時執行數 | 依方案（2～32） | 32 | 只有用量計費使用者能用 `subagents.maxConcurrency` 調整 |

> 📝 官方 command reference 的環境變數表另列 `COPILOT_SUBAGENT_MAX_DEPTH` 預設 4、`COPILOT_SUBAGENT_MAX_CONCURRENT` 預設 32，與設定鍵表（深度預設 6）不一致；本手冊以設定鍵表為準，已列入附錄 H.4 待確認。

### 6.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| `copilot-instructions.md` | 抽象口號、沒有可執行指令 | 列出建置／測試指令、可驗證的架構規則與理由 | 逐條問：「這條規則能用指令或工具驗證嗎？」 |
| 路徑專屬指引 | 缺少 `applyTo` | frontmatter 寫 `applyTo` glob | `python check_config.py instructions <檔案>` |
| 指引中的檔案引用 | `@~/rules.md`、`@/etc/x` | Repo 內相對路徑 | `check_config.py instructions` 會標出不會載入的引用 |
| 多份指引 | `AGENTS.md` 與 `CLAUDE.md` 內容矛盾 | 只維護一份或內容一致 | `copilot instruction list` 列出全部來源後逐一比對 |
| `.agent.md` | 缺 `description`、`tools` 寫成字串 | 必填 `description`，`tools` 為陣列 | `python check_config.py agent <檔案>` |
| 審查類代理 | 給予 `edit`、`create` 工具 | 只給唯讀工具 | 檢查 `tools` 陣列不含寫入工具 |
| 子代理設計 | 以為子代理會自動遵守 Repo 規範 | 需要時設定 `include-custom-instructions: true` | 對照 6.4.5 節表格 |
| 指引更新後的測試 | 修改後在同一個 Session 繼續測 | `/new` 或重新啟動後再測 | `/instructions` 確認新內容已載入 |

---

## 第 7 章：Session 管理

> **本章目標**
>
> - 理解 Session 包含哪些資料、存在哪裡、可以如何恢復、分享與刪除。
> - 能用 worktree 與 fork 隔離並行的工作，避免多個任務互相污染。
> - 知道 Session 同步、分享與遠端控制涉及的資料外流風險。

### 7.1 Session 是什麼

每次啟動 Copilot CLI，都會建立或恢復一個 Session，內容包括：你的提示、代理的回應、送給模型的 context、工具活動（讀過的檔案、執行過的指令），以及 Session 狀態（工作目錄、檔案權限、已核准的工具、目前模式）。

本機儲存位置：

```text
~/.copilot/session-state/{session-id}/
├── events.jsonl      # 完整事件紀錄
├── workspace.yaml    # 中繼資料
├── plan.md           # Plan 模式產生的計畫（若有）
├── checkpoints/      # 每次壓縮的摘要
└── files/            # Session 期間產生的暫存成品
```

另外，`~/.copilot/session-store.db`（SQLite）存放跨 Session 的索引；刪除後可用 `/chronicle reindex` 重建。

> ⚠️ `events.jsonl` 會記錄指令與輸出，**可能含有密鑰或個資**。共用電腦、備份與日誌收集政策都要把 `~/.copilot/session-state/` 視為機敏資料。

### 7.2 啟動、恢復與命名

```bash
copilot --name "order-cancel-api"     # 以名稱建立新 Session，方便日後尋找
copilot --continue                    # 恢復目前目錄最近的 Session（找不到則用全域最近的）
copilot --resume                      # 開啟選擇器
copilot --resume="order-cancel-api"   # 依名稱恢復（完全符合、不分大小寫）
copilot --resume=0cb916d              # 依 ID 前綴（7 個以上十六進位字元）恢復
copilot --session-id=0cb916db-26aa-40f2-86b5-1ba81b225fd2   # 精確指定 ID；不存在且為合法 UUID 時建立新 Session
```

互動式介面中的對應指令：

| 指令 | 用途 |
|------|------|
| `/resume`（別名 `/continue`） | 切換到其他 Session（本機或雲端歷史、任務 ID、名稱） |
| `/rename [名稱]` | 重新命名；省略名稱會依對話自動產生 |
| `/new [提示]`（別名 `/clear`、`/reset`） | 開始新對話 |
| `/session info` | Session ID、時長、工作目錄、**日誌檔路徑** |
| `/session files`／`/session plan` | 暫存成品／目前計畫 |
| `/session checkpoints [n]` | 壓縮檢查點 |
| `/session delete [ID]`／`cleanup`／`prune`／`delete-all` | 刪除與清理 |
| `/exit` | 結束並保存 Session，之後可恢復 |
| `/restart` | 重新啟動 CLI，並恢復目前程序中所有存活的 Session |

選擇器中按 <kbd>s</kbd> 切換排序（相關性 → 建立時間 → 名稱 → 最後使用），<kbd>Tab</kbd> 切換本機與遠端分頁，<kbd>x</kbd> 刪除。

**命名規範建議**：`<類型>-<模組>-<主題>`，例如 `feat-order-cancel`、`bug-482-double-refund`、`spike-kafka-retry`。名稱會用於 `--resume` 與搜尋，好名字等於好索引。

### 7.3 多 Session 並行

一個 CLI 程序可以同時執行多個 Session；切換走的 Session 會**繼續在背景執行**。

| 介面 | 開啟方式 | 用途 |
|------|------|------|
| Sessions 側欄 | 空白輸入框按 <kbd>←</kbd> | 快速切換最近的本機 Session；<kbd>n</kbd> 新建、<kbd>x</kbd> <kbd>x</kbd> 關閉、<kbd>s</kbd> 排序 |
| Sessions 分頁 | <kbd>Tab</kbd> 或 `/session` | 完整歷史、搜尋（<kbd>/</kbd>）、本機／遠端篩選（<kbd>a</kbd>） |
| Session 選擇器 | `/resume` | 指令式切換 |

側欄狀態符號：脈動圓點代表執行中、實心圓點代表閒置、`!` 代表等待權限核准、`?` 代表代理在提問、空心圓 `○` 代表未執行的可恢復 Session。

> ⚠️ 在側欄或 Sessions 分頁對**本機** Session 按兩次 <kbd>x</kbd> 會**永久刪除**該 Session 的歷史，無法恢復；伺服器端的 Session 則只是關閉。只想停止而保留，請用 `/exit`。

### 7.4 Worktree 與 Fork：隔離並行工作

多個 Session 在**同一個工作目錄**同時改檔，會互相覆蓋。正確做法是讓每條工作線使用自己的 Git worktree。

| 指令 | 作用 | 未 commit 的變更 |
|------|------|------|
| `copilot -w [名稱]`（`--worktree`） | 建立或重用 worktree，並在其中啟動 Session | 留在原處 |
| `/worktree [分支或任務描述]` | 從設定的基準建立 worktree 並切換過去 | **留在原處** |
| `/move [分支或任務描述]` | 建立 worktree 並切換過去 | **一併帶過去** |
| `/new worktree [提示]` | 在新 worktree 開始空白對話，目前對話不變 | 留在原處 |
| `/fork [名稱]`（別名 `/branch`） | 把目前 Session 複製成新 Session（保留 context）；可在代理執行中使用 | — |
| `/fork worktree` | 複製目前 Session 到從 `HEAD` 分出的新 worktree | — |

相關設定：

| 設定鍵 | 說明 |
|------|------|
| `worktreeBaseRef` | `"head"`（預設，從目前 checkout 分出）或 `"defaultBranch"`（從遠端預設分支分出）；`/fork worktree` 一律從 `HEAD` |
| `worktreePathTemplate` | worktree 位置，例如 `~/src/worktrees/{repo}/{branch}`；支援 `{repoPath}`、`{repo}`、`{branch}`、`{branchSlug}`；未設定時為 `<repo>.worktrees/` |

```text
# 情境：主線在做功能，臨時要修一個 bug
/worktree bug-482-double-refund
重現 #482 並修正，補上回歸測試，完成後 commit 到這個分支
```

> ✅ linked worktree 會解析到主 Repo 根目錄，因此**共用同一組「This location」權限核准**（`permissions-config.json`）。

### 7.5 分享與匯出

| 方式 | 指令 | 資料去向 |
|------|------|------|
| Markdown 檔 | `/share file [路徑]`；程式化用 `--share=路徑` | 本機 |
| HTML 檔 | `/share html` | 本機 |
| 秘密 Gist | `/share gist`；程式化用 `--share-gist` | GitHub（Enterprise Managed Users 與 `*.ghe.com` 不可用） |
| 分享連結 | `/share` 或 `/share link`（`/share off` 停止） | GitHub（需登入並啟用 Session 同步） |
| 研究報告 | `/share research` | 依目標而定 |
| 複製最後回應 | `/copy` | 剪貼簿 |

> ⚠️ 分享前先檢查內容：Session 紀錄可能含有內部程式碼、內部網址、錯誤訊息中的連線字串。企業環境建議禁止 `--share-gist`，並在 CI 只輸出到本機再由流程控管上傳。

### 7.6 Session 同步與遠端控制

| 設定或旗標 | 作用 |
|------|------|
| `remote: "off"` 或 `--no-remote` | 不同步 Session、停用遠端控制，資料只留在本機 |
| `remoteExport: false` 或 `--no-remote-export` | 不匯出 Session 到 GitHub（也會停用遠端控制） |
| `--remote` 或 `/remote on` | 允許從 GitHub 網頁與 GitHub Mobile 遠端操控目前 Session |
| `--remote-export` | 只匯出供檢視（唯讀），不允許遠端操控 |
| `--connect[=ID]` | 直接連到遠端 Session |
| 受管設定 `remoteControl.mode` | `enabled`、`disabled` 或 `requireSSO`（第 15 章） |

遠端控制適合「在手機上核准一個長時間任務的權限請求」這類情境；但它代表**別的裝置可以驅動你本機的代理**，企業應以受管設定限制為 `requireSSO` 或 `disabled`。

### 7.7 Chronicle：Session 歷史的分析工具

`/chronicle` 會分析你的 Session 歷史：

| 子指令 | 用途 |
|------|------|
| `standup` | 依最近的 Session 產生站立會議摘要 |
| `tips` | 依你的使用習慣給建議 |
| `improve` | 建議如何改善指引或工作流程 |
| `reindex` | 重建 `session-store.db` 索引（也會同步到帳號） |
| `skills create`／`review`／`status` | 依觀察到的使用模式草擬 Repo skill 提案、審查、追蹤狀態 |

> ✅ `chronicle skills create` 產生的 skill 是**草稿**，必須經過與一般程式碼相同的 PR 審查，再 commit 進 `.github/skills/`。

### 7.8 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 並行工作安排 | 兩個 Session 在同一目錄同時改檔 | 每條工作線用 `/worktree` 或 `-w` | `git worktree list` 確認各 Session 的目錄不同 |
| 未 commit 變更的處理 | 用 `/worktree` 卻以為變更會帶過去 | 要帶走變更用 `/move` | 切換後 `git status` 比對兩邊 |
| Session 清理 | 在側欄按 x x 以為只是暫停 | 暫停用 `/exit`；刪除前確認不再需要 | 刪除前 `/session info` 記下 ID，刪除後 `--resume=ID` 應找不到 |
| 分享紀錄 | 直接 `--share-gist` 公開 CI 紀錄 | 輸出到本機檔案，審查後再分享 | 檢查產出檔是否含內部網址、Token、個資 |
| 機敏資料保護 | 把 `~/.copilot` 整包納入一般備份 | `session-state/` 依機敏資料政策處理 | 盤點備份範圍與存取權限 |
| 遠端控制 | 全公司預設 `--remote` | 受管設定 `remoteControl.mode: requireSSO` 或 `disabled` | `check_config.py managed-settings` |

---

## 第 8 章：GitHub 整合

> **本章目標**
>
> - 用 `/pr` 管理 PR 的完整生命週期，並知道哪些子指令會 commit 與 push。
> - 了解內建 GitHub MCP 伺服器的預設工具範圍，以及如何擴大或收斂。
> - 能把 `/review`、`/security-review` 納入團隊的審查流程，同時清楚它們的限制。

### 8.1 以自然語言操作 GitHub

Copilot CLI 內建 GitHub MCP 伺服器，以你登入的帳號存取 GitHub。常見的提示：

| 目的 | 提示範例 |
|------|------|
| 查我的工作 | `列出我在 acme/order-service 被指派、還沒關閉的 Issue` |
| 從 Issue 開工 | `我被指派了 https://github.com/acme/order-service/issues/482，開一個合適名稱的分支開始處理` |
| 建立 Issue | `在 acme/order-service 開一個 improvement issue：OrderExporter.java 開啟檔案後沒有關閉` |
| 審查他人的 PR | `檢查 https://github.com/acme/order-service/pull/57 的變更，只回報嚴重問題` |
| 查 Actions | `列出這個 Repo 中會對 PR 留言的 workflow` |

> ⚠️ 由代理建立的 PR 與 Issue，**作者是你本人**。代理用你的權限操作，因此「合併我所有開啟中的 PR」這類提示會真的執行。對寫入操作要逐次核准，不要對 GitHub MCP 工具使用「本 Session 不再詢問」。

### 8.2 `/pr`：PR 生命週期

所有 `/pr` 子指令都以**目前分支**對應的 PR 為對象。

| 子指令 | 作用 | 需要既有 PR | 可能 commit 與 push |
|------|------|------|------|
| `/pr`、`/pr view` | 顯示 PR 狀態 | ✅ | ❌ |
| `/pr view web` | 用瀏覽器開啟 PR | ✅ | ❌ |
| `/pr create [指示]` | 推送 commit 並建立或更新 PR；**會遵循 Repo 的 PR 範本** | ❌ | ✅ |
| `/pr fix feedback` | 處理 review 留言，在討論串回覆並標記已解決；需要你判斷的討論串只回覆不解決 | ✅ | ✅ |
| `/pr fix conflicts` | 同步基準分支並解決衝突 | ✅ | ✅ |
| `/pr fix ci` | 診斷並修正失敗的 CI | ✅ | ✅ |
| `/pr fix`、`/pr fix all` | 依序執行上述三個階段 | ✅ | ✅ |
| `/pr auto` | 必要時建立 PR，然後反覆修正直到所有檢查通過 | ❌ | ✅ |
| `/pr automerge`（別名 `agentmerge`） | 同 `/pr auto`，通過後**自動合併** | ❌ | ✅ |

```text
/pr create 標題加上「[ORDER]」前綴，描述中列出資料庫遷移與部署注意事項
```

衝突解決策略由 `mergeStrategy` 設定（`"rebase"` 或 `"merge"`），可放在使用者設定或 Repo 設定；未設定時每次都會詢問。

> ⚠️ **`/pr automerge` 的治理**：它會在檢查通過後直接合併。企業應以分支保護規則（必要的人工 review、必要的狀態檢查）確保「綠燈」不等於「可以合併」。代理只能在保護規則允許的範圍內合併。
>
> ⚠️ **`/pr fix ci` 的風險**：代理可能以「讓測試通過」為目標而**修改或刪除測試**。審查時必須特別檢查測試檔的 diff（第 21 章）。

### 8.3 內建 GitHub MCP 伺服器

| 項目 | 說明 |
|------|------|
| 伺服器名稱 | `github-mcp-server`（使用權限規則時以此名稱指定） |
| 預設工具範圍 | CLI 預設子集：檔案內容與程式碼搜尋、Issue、PR、commit、workflow run 與日誌、label |
| 驗證 | 使用 CLI 登入的帳號 |
| 列表 | `copilot mcp list` 會列出 Builtin 來源的伺服器 |

調整工具範圍的旗標：

```bash
copilot --add-github-mcp-toolset=actions         # 加入某個 toolset（可重複；all 代表全部）
copilot --add-github-mcp-tool=create_issue       # 加入單一工具（可重複；* 代表全部）
copilot --enable-all-github-mcp-tools            # 啟用全部工具（會覆寫上面兩個旗標）
copilot --disable-builtin-mcps                   # 停用全部內建 MCP 伺服器
copilot --disable-mcp-server=github-mcp-server   # 只停用 GitHub MCP
```

> ✅ **最小權限**：日常開發用預設子集即可。需要寫入類工具時，以 `--add-github-mcp-tool` 逐一加入，並搭配權限規則，例如 `--deny-tool='github-mcp-server(merge_pull_request)'`。

### 8.4 Issue、PR 與 Gist 瀏覽分頁

首頁分頁列提供 **Issues**、**Pull requests**、**Gists** 分頁，可以直接瀏覽並把項目帶進對話。用設定 `tabs.hide`、`tabs.sort` 調整顯示。

### 8.5 程式審查：`/review` 與 `/security-review`

| 指令 | 審查範圍 | 回報內容 | 不會做的事 |
|------|------|------|------|
| `/review [提示]` | 已 stage／未 stage 的變更與分支 diff | bug、安全弱點、競態、記憶體洩漏、邏輯錯誤 | 不評論風格與排版、不修改檔案 |
| `/security-review [提示]` | **本機目前的變更** | 依優先順序排列的弱點與修正建議；只回報可利用性信心超過 80% 的發現 | 不是完整的 Repo 安全稽核、不修改檔案 |

```text
/review 與 main 比較本分支的變更，重點看並發與交易邊界的錯誤
/security-review 優先列出 High 以上的發現，並給我可以直接套用的修正
```

程式化執行：

```bash
copilot -p '/review the changes on this branch compared to main. Focus on bugs and security issues.' \
  -s --allow-tool='shell(git:*)'
```

> ✅ **交叉審查的技巧**：讓**不同模型**審查同一份變更可以降低共同盲點。例如由 Claude 模型實作、在 `/review` 的提示中指定改用 GPT Codex 模型審查；或使用 `/rubber-duck`，它本身就會使用與主 Session 不同家族的模型。

> ⚠️ AI 審查是**第一道篩選**，不能取代人工審查與 SAST／SCA 工具。它的信心門檻設計會**漏報**低信心的問題；沒有發現不代表沒有問題。

### 8.6 在 Actions 中使用

在 GitHub Actions 中執行 `copilot -p` 的完整範例、驗證方式與安全注意事項見第 16 章；GitHub 官方對大多數自動化情境更推薦 **GitHub Agentic Workflows**（`gh-aw`），它預設使用 `GITHUB_TOKEN` 並內建自動化防護。

### 8.7 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| `/pr fix ci` 的修正 | 修改斷言或刪除失敗的測試讓 CI 變綠 | 修正被測程式；若要改測試需說明理由 | `git diff origin/main -- '*Test*.java'` 逐行檢查測試變更 |
| `/pr create` 的描述 | 自行編造測試結果與覆蓋率 | 只寫實際執行過的結果，並遵循 PR 範本 | 對照 CI 結果與 PR 範本的必填段落 |
| `/pr automerge` 的使用 | 在沒有分支保護的 Repo 使用 | 先設定必要 review 與狀態檢查 | 檢查 Repo 的 branch protection／rulesets |
| GitHub MCP 權限 | `--enable-all-github-mcp-tools` 搭配本 Session 不再詢問 | 預設子集＋逐一加入需要的工具 | `copilot mcp get github-mcp-server` 檢查工具清單 |
| AI 審查結果的使用 | 「`/security-review` 沒有發現，所以安全」 | AI 審查＋人工審查＋SAST／SCA | 檢查 PR 是否同時有人工 review 與掃描結果 |
| 代理建立的 Issue／PR | 未確認內容就送出 | 寫入動作逐次核准，送出前檢視內容 | 檢查 GitHub 上的作者、標題與內容 |

---

## 第 9 章：MCP 伺服器

> **本章目標**
>
> - 正確設定使用者層級、Repo 層級與單次 Session 的 MCP 伺服器，並理解載入優先順序。
> - 知道 Repo 層級 MCP 何時會（或不會）被載入，以及背後的信任模型。
> - 能審查一份 MCP 設定是否安全：版本固定、密鑰不外露、工具最小化。

### 9.1 MCP 在 Copilot CLI 中的角色

Model Context Protocol（MCP）讓代理透過標準介面使用外部工具與資料（瀏覽器自動化、內部文件、資料庫、工單系統）。CLI 支援兩種伺服器：

| 類型 | `type` 值 | 說明 |
|------|------|------|
| 本機 | `local` 或 `stdio`（預設 `local`） | 啟動本機程序，以 stdin／stdout 溝通。`stdio` 是標準名稱，與 VS Code、cloud agent 相容 |
| 遠端 | `http`（Streamable HTTP；`streamable-http` 為別名） | 連到遠端端點 |
| 遠端（舊） | `sse` | 舊式 HTTP＋SSE，MCP 規格已棄用，僅為相容保留 |

**所有 MCP 工具呼叫都需要明確核准**，即使是對外部服務的唯讀操作也一樣。

### 9.2 設定檔位置與載入優先順序

| 優先序 | 來源 | 位置 | 條件 |
|------|------|------|------|
| 1（最高） | 單次 Session | `--additional-mcp-config=JSON` 或 `@檔案` | 只影響本次執行 |
| 2 | Plugin | 已安裝 plugin 內的設定 | — |
| 3 | 工作區 | `.mcp.json` 與 `.github/mcp.json`，從目前目錄往上到 Git 根目錄 | **資料夾必須已受信任** |
| 4（最低） | 使用者 | `~/.copilot/mcp-config.json` | — |

- 同一目錄同時有 `.mcp.json` 與 `.github/mcp.json` 時，`.mcp.json` 優先；名稱衝突時，離目前目錄越近的定義優先。
- **`.vscode/mcp.json` 不會被讀取**（它的頂層鍵是 `servers`，CLI 不支援）。
- 工作區設定檔中某一筆設定無效時，只會略過那一筆並顯示警告；整個檔案 JSON 格式錯誤則整檔略過。

> 📝 **v1 手冊更正**：舊版寫「v1.0.22 起 `.mcp.json` 是唯一讀取的工作區 MCP 設定檔」，目前版本另外支援 `.github/mcp.json`，官方建議**要 commit 共用的設定放 `.github/mcp.json`**，個人或單次 checkout 的設定放 `.mcp.json`。

#### 9.2.1 信任模型

| 來源 | 信任等級 | 是否需要審查 |
|------|------|------|
| 內建 | 高 | 否 |
| Repo（`.github/mcp.json`）、工作區（`.mcp.json`） | 中 | 建議 |
| 使用者設定 | 使用者自訂 | 使用者自行負責 |
| 遠端伺服器 | 低 | 一律 |

工作區 MCP 只在**確認資料夾信任之後**載入，在不受信任的目錄會被靜默略過。程式化模式（`-p`）無法顯示信任提示，因此：目錄已受信任才會載入；否則略過，除非設定 `GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP=true`。

> ⚠️ **TrustFall 類風險**：一旦信任資料夾，該 Repo 的 `.mcp.json` 定義的本機伺服器就會**自動啟動並執行程式**。這是所有代理式 CLI 的共通風險（Adversa AI 於 2026 年揭露的研究，第 15 章）。Clone 不受信任的 Repo 後，**先檢查 `.mcp.json`、`.github/mcp.json`、`.github/hooks/`，再決定是否信任**。

### 9.3 新增 MCP 伺服器

#### 9.3.1 互動式

```text
/mcp add          # 開啟表單：名稱、類型、指令或 URL、環境變數、工具清單；Ctrl+S 儲存，立即生效
/mcp search playwright   # 從 GitHub MCP Registry（或組織設定的 Registry）搜尋並安裝；實驗性功能
```

#### 9.3.2 非互動式：`copilot mcp`

```bash
# 本機伺服器：指令放在 -- 之後
copilot mcp add context7 -- npx -y @upstash/context7-mcp@1.0.20

# 本機伺服器＋環境變數
copilot mcp add github-local --env GITHUB_PERSONAL_ACCESS_TOKEN="$GH_PAT" \
  -- docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server

# 遠端伺服器
copilot mcp add --transport http --header "Authorization: Bearer $DOCS_TOKEN" \
  --tools "search_docs,get_page" internal-docs https://mcp.docs.example.com/mcp

copilot mcp list                 # 依來源（User、Workspace、Plugin、Builtin）列出
copilot mcp get internal-docs    # 詳細設定（密鑰預設遮蔽；--show-secrets 顯示）
copilot mcp disable internal-docs
copilot mcp enable internal-docs
copilot mcp remove internal-docs # 只能移除使用者設定中的伺服器
```

> ⚠️ `copilot mcp add --env KEY=值` 會把值**寫進** `~/.copilot/mcp-config.json`。上例使用 `"$GH_PAT"` 只是讓 shell 展開，結果仍是明文寫入。要避免明文，請在設定檔中使用 `${VAR}` 參照（9.3.3 節），讓 CLI 在執行時從環境變數展開。

#### 9.3.3 設定檔格式與範例

Repo 層級共用設定 `.github/mcp.json`：

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@0.0.41"],
      "env": {},
      "tools": ["browser_navigate", "browser_snapshot", "browser_take_screenshot"]
    },
    "internal-docs": {
      "type": "http",
      "url": "https://mcp.docs.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${INTERNAL_DOCS_TOKEN}"
      },
      "tools": ["*"]
    }
  }
}
```

重點：

- `@playwright/mcp@0.0.41` **固定版本**，避免供應鏈變更在不知不覺中進入開發環境；企業 allowlist 也依指令與參數比對。
- `tools` 明確列出需要的工具，而不是 `["*"]`，降低 context 佔用與誤用。
- 密鑰以 `${INTERNAL_DOCS_TOKEN}` 參照環境變數，**不寫入檔案**（`env` 與 `headers` 支援 `$VAR`、`${VAR}`、`${VAR:-預設值}`）。
- Repo 層級檔案可用 `mcpServers` 物件，也可用「每個鍵就是伺服器名稱」的簡寫格式。

常用欄位：

| 欄位 | 適用 | 說明 |
|------|------|------|
| `command`、`args` | 本機 | 啟動指令與參數 |
| `url`、`headers` | 遠端 | 端點與 HTTP 標頭 |
| `tools` | 全部 | `["*"]` 或工具名稱陣列 |
| `env`、`cwd` | 本機 | 環境變數與工作目錄 |
| `timeout` | 全部 | 毫秒，預設 30000 |
| `oauthClientId`、`oauthScopes`、`oauthPublicClient`、`oauthGrantType` | 遠端 | OAuth 設定；`client_credentials` 適合 CI（無瀏覽器） |
| `deferTools` | 全部 | `"never"` 讓工具在 tool search 啟用時仍一直可見 |
| `filterMapping` | 全部 | 工具輸出處理：`none`、`markdown`、`hidden_characters`（預設，移除隱藏字元） |

#### 9.3.4 從 `.vscode/mcp.json` 遷移

```bash
jq '{mcpServers: .servers}' .vscode/mcp.json > .github/mcp.json
python check_config.py mcp .github/mcp.json     # 遷移後檢查
```

### 9.4 管理與疑難排解

| 動作 | 互動式 | 非互動式 |
|------|------|------|
| 開啟管理介面 | `/mcp`（plugins 儀表板的 MCP 分頁） | — |
| 列出 | `/mcp list` | `copilot mcp list [--json]` |
| 詳細資訊與工具 | `/mcp show 名稱` | `copilot mcp get 名稱` |
| 編輯／刪除 | `/mcp edit 名稱`、`/mcp delete 名稱` | 編輯設定檔／`copilot mcp remove` |
| 停用／啟用（持久化） | `/mcp disable｜enable 名稱` | `copilot mcp disable｜enable 名稱` |
| 本次 Session 暫時啟用 | — | `--enable-mcp-server 名稱`（不寫入設定） |
| 本次 Session 停用 | — | `--disable-mcp-server 名稱` |
| 重新 OAuth 登入 | `/mcp auth 名稱` | — |
| 重新載入 | `/mcp reload` | — |

v1.0.93 起，MCP 設定變更會在回合之間套用，不必重新啟動 Session。

| 症狀 | 原因與處理 |
|------|------|
| Repo 的伺服器沒出現 | 資料夾未受信任；或用了 `.vscode/mcp.json`；或程式化模式未設定 `GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP` |
| 伺服器啟動逾時 | 加大 `timeout`；`slowConnectionThresholdMs` 只影響警告時機 |
| 初始化卡住 | 本機伺服器把日誌寫到 stdout；**診斷訊息必須寫到 stderr** |
| 顯示 `needs-auth` | Token 過期或需要另一個帳號：`/mcp auth 名稱` |
| 被企業封鎖 | 訊息為 `blocked by your enterprise`：請管理者把伺服器加入 allowlist |

### 9.5 企業管控

| 機制 | 說明 | 詳見 |
|------|------|------|
| MCP Registry URL | 組織設定的 Registry 成為 `/mcp search` 的來源 | 第 15 章 |
| 企業 MCP allowlist | 依伺服器的指令、參數與遠端 URL 計算指紋送到企業端點評估；**端點無法連線時 fail-closed**，非預設伺服器一律封鎖 | 第 15 章 |
| 受管設定 `allowedMcpServers`／`deniedMcpServers` | 依 `serverUrl`、`serverCommand`、`serverName` 比對；deny 永遠優先；空的 allowlist 代表全部禁止 | 第 15 章 |
| Sandbox `sandboxMcpServers` | 讓本機 MCP 伺服器也在 Sandbox 中執行（遠端伺服器不受 Sandbox 影響） | 第 14 章 |

> 📝 **文件不一致**：官方〈About Copilot CLI〉頁面仍寫「CLI 目前不支援 *MCP servers in Copilot* 與 *MCP Registry URL* 兩個組織政策」，但〈Adding MCP servers〉與〈Administering Copilot CLI〉頁面已說明 Registry URL 與 allowlist 政策會套用到 CLI。導入時請以實際測試為準，已列入附錄 H.4。

### 9.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| Repo MCP 設定檔 | 放在 `.vscode/mcp.json` 或使用 `servers` 鍵 | `.github/mcp.json`，使用 `mcpServers` | `python check_config.py mcp .github/mcp.json` |
| 套件版本 | `npx -y some-mcp@latest` | 固定版本號 | 檢查 `args` 中的版本；checker 會對 `@latest` 發出警告 |
| 密鑰 | `headers` 中直接寫 Token | `${ENV_VAR}` 參照 | checker 掃描常見 Token 前綴；`git log -p` 確認沒有歷史洩漏 |
| 遠端端點 | `http://` 非本機端點 | `https://` | checker 會標出非 HTTPS 的遠端端點 |
| 工具範圍 | 一律 `["*"]` | 列出需要的工具 | `copilot mcp get 名稱` 比對實際需要 |
| 本機伺服器實作 | 把日誌印到 stdout | 日誌寫 stderr | 手動執行伺服器，確認 stdout 只有 JSON-RPC |
| CI 中使用工作區 MCP | 直接在未受信任的 Runner 上 `-p` 並設定 `GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP=true` | 只在受控 Repo 啟用，並審查設定檔 | 檢查 workflow 是否在 fork PR 上執行 |

---

## 第 10 章：Skills、Plugins、Marketplace 與 Extensions

> **本章目標**
>
> - 分辨 skill、custom agent、plugin、extension 各自解決什麼問題。
> - 能撰寫可被正確觸發、附帶驗證步驟的 `SKILL.md`。
> - 能建立與發佈企業內部的 plugin 與 marketplace，並在受管設定中限制來源。

### 10.1 四種擴充機制的比較

| 機制 | 本質 | 何時載入 | 典型用途 | 是否執行程式碼 |
|------|------|------|------|------|
| Skill | 一個資料夾：`SKILL.md` 指示＋腳本與資源 | 相關任務時由代理載入，或以 `/skill名稱` 呼叫 | 「怎麼做某件專門的事」：DB 遷移、發版流程 | 只有在指示中要求執行腳本時 |
| Custom agent | `.agent.md` 定義的專門化代理 | 以子代理執行，有獨立 context | 「由誰來做」：資安審查、測試撰寫 | 透過工具 |
| Plugin | 可安裝的套件，打包 agents、skills、hooks、MCP、LSP | 安裝並啟用後 | 團隊／企業共用的一整套設定 | 視內容（hooks、MCP 會執行程式） |
| Extension | Node.js 模組，新增工具與 slash 指令 | Session 啟動時（實驗性） | 內建工具做不到的客製能力 | ✅ 以你的權限執行 |

官方的比較原則：custom instructions 適合「永遠適用」的規則；skill 適合「特定任務才需要」的詳細步驟；custom agent 適合需要獨立 context 與工具限制的工作；hooks 適合必須確定執行的檢查。

### 10.2 Skills

#### 10.2.1 存放位置與優先順序

名稱重複時，先找到的勝出：

| 位置 | 範圍 |
|------|------|
| `.github/skills/`、`.agents/skills/`、`.claude/skills/` | 專案 |
| 上層目錄的 `.github/skills/` | Monorepo 繼承 |
| `~/.copilot/skills/`、`~/.agents/skills/` | 個人 |
| Plugin 目錄 | Plugin |
| `COPILOT_SKILLS_DIRS`、設定 `skillDirectories` | 自訂 |
| `--add-dir` 目錄下的 `.github/skills/` | 加入的目錄（等同專案信任） |
| CLI 內建 | 最低優先，可被任何來源覆寫 |
| 組織／企業遠端 skills | 依需求取得內容 |

兩個 plugin 提供同名 skill 時會並存，以 `/plugin名稱/skill名稱` 區分。`ignoredSkillsLocations` 可排除特定目錄。

#### 10.2.2 `SKILL.md` frontmatter

| 欄位 | 必填 | 說明 |
|------|------|------|
| `name` | ✅ | 以英數字開頭，可含英數字、`-`、`_`、`.`、`:`、空白，最多 64 字元；冒號用於命名空間，例如 `my-plugin:search`。官方建議小寫加連字號並與目錄同名 |
| `description` | ✅ | 做什麼、何時使用，最多 1024 字元；**代理依此決定是否載入** |
| `argument-hint` | | 在選單中顯示的參數提示 |
| `allowed-tools` | | 啟用該 skill 時自動核准的工具；`"*"` 代表全部 |
| `user-invocable` | | 能否用 `/名稱` 呼叫，預設 `true` |
| `disable-model-invocation` | | 禁止代理自動載入，預設 `false` |
| `license` | | 授權說明 |

#### 10.2.3 範例：資料庫遷移 skill

````markdown
---
name: db-migration
description: 建立或審查 Flyway 資料庫遷移腳本。當使用者要求新增資料表、修改欄位、建立索引或撰寫 migration 時使用。
argument-hint: "[變更描述]"
---

# 資料庫遷移（Flyway）

## 命名規則

- 檔名：`src/main/resources/db/migration/V{yyyyMMddHHmm}__{snake_case_描述}.sql`
- 一個檔案只做一件事；**禁止**修改已合併到 main 的遷移檔。

## 撰寫規則

1. 新增 NOT NULL 欄位時，必須同時給 `DEFAULT` 或分兩步（先可為 NULL → 回填 → 再加限制）。
2. 大表（> 100 萬筆）建立索引一律用 `CREATE INDEX CONCURRENTLY`（PostgreSQL），且該檔案不得包含其他語句。
3. 每個破壞性變更（DROP / RENAME）都要附上回復腳本 `U{同版本}__*.sql`。

## 完成前必做的驗證

```bash
./mvnw -q flyway:validate
./mvnw -q -Dtest='*MigrationIT' verify
```

兩個指令都成功才可回報完成，並在回覆中貼出指令輸出的最後 20 行。
````

設計重點：

- `description` 寫出觸發情境（「新增資料表、修改欄位、建立索引、migration」）。
- 規則具體且有理由（大表索引用 `CONCURRENTLY`）。
- **以「完成前必做的驗證」結尾**，並要求貼出指令輸出，讓人工可以檢查代理是否真的跑過。
- 刻意**不設定** `allowed-tools`：Flyway 指令會連線資料庫，應該讓使用者逐次核准。

> ⚠️ **`allowed-tools` 的風險**：官方警告，只有在審查過 skill 與它引用的所有腳本、而且完全信任來源時，才可以預先核准 `shell` 或 `bash`。預先核准等於拿掉執行終端機指令前的確認步驟。

#### 10.2.4 管理指令

```bash
copilot skill list [--json]                       # 依來源列出（欄位：name、description、source、path、enabled）
copilot skill add ./db-migration/SKILL.md         # 複製到 ~/.copilot/skills/<name>/
copilot skill add --project ./db-migration/SKILL.md   # 複製到專案的 .github/skills/
copilot skill add ~/team-skills                   # 註冊整個目錄（不複製）
copilot skill disable db-migration
copilot skill enable db-migration
copilot skill remove db-migration
```

互動式介面：`/skills`（plugins 儀表板的 Skills 分頁）、`/skills list`、`/skills info 名稱`、`/skills reload`；呼叫 skill 則輸入 `/db-migration 新增 orders.cancel_reason 欄位`。

`.claude/commands/*.md` 也會被當成簡化版 skill（指令名稱取自檔名），同名時優先序低於 skill。

### 10.3 Plugins

#### 10.3.1 安裝與管理

```bash
copilot plugin marketplace list                    # 已註冊的 marketplace（內建 awesome-copilot）
copilot plugin marketplace browse awesome-copilot  # 瀏覽
copilot plugin install arch@awesome-copilot        # 從 marketplace 安裝
copilot plugin install acme-corp/copilot-java-kit  # 從 GitHub Repo 安裝
copilot plugin install acme-corp/monorepo:plugins/java-kit   # 從 Repo 子目錄安裝
copilot plugin install ./my-plugin                 # 從本機目錄安裝（開發測試用）
copilot plugin list [--json]
copilot plugin update --all
copilot plugin disable arch@awesome-copilot
copilot plugin uninstall arch@awesome-copilot
```

互動式介面輸入 `/plugin` 開啟儀表板（Installed、Online、Marketplace 三個檢視），有新版時會標示並提供 Update。`--plugin-dir 路徑` 可在單次執行時載入本機 plugin，不必安裝。

> ⚠️ 安裝後 plugin 會被快取，**修改本機 plugin 後要重新 `copilot plugin install ./my-plugin`** 才會生效（directory 來源的 marketplace 例外，會即時從目錄載入）。

#### 10.3.2 兩種 plugin 格式

| 格式 | 判斷方式 | 特性 |
|------|------|------|
| Agent Plugins 1.0 | `plugin.json` 宣告 `$schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` | 可跨相容用戶端攜帶 skills 與 MCP；`skills/` 與根目錄 `mcp.json` 位置固定；Copilot 專屬元件放在 `com.github.copilot/` |
| 舊版 Copilot 格式 | 沒有上述 `$schema` | 可在 `plugin.json` 自訂元件路徑（`agents`、`skills`、`hooks`、`mcpServers`、`lspServers`） |

Agent Plugins 1.0 範例：

```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "acme-java-toolkit",
  "description": "ACME 公司 Java 團隊共用的 skills 與 MCP 設定",
  "version": "1.0.0",
  "author": { "name": "ACME Platform Team", "email": "platform@acme.example.com" },
  "license": "MIT",
  "keywords": ["java", "spring-boot", "flyway"]
}
```

Agent Plugins 1.0 只允許 `$schema`、`name`、`version`、`description`、`author`、`homepage`、`repository`、`license`、`keywords`、`extensions` 這些頂層欄位，其他欄位會被回報並忽略。Plugin 內的本機 MCP 伺服器可使用 `${PLUGIN_ROOT}`（plugin 目錄）與 `${PLUGIN_DATA}`（plugin 資料目錄）。

#### 10.3.3 建立企業內部 marketplace

在 Repo 的 `.github/plugin/marketplace.json`（也支援 `.claude-plugin/`）建立索引：

```json
{
  "name": "acme-copilot-plugins",
  "owner": { "name": "ACME Platform Team", "email": "platform@acme.example.com" },
  "metadata": { "description": "ACME 內部核准的 Copilot CLI plugins", "version": "2026.10.0" },
  "plugins": [
    {
      "name": "acme-java-toolkit",
      "description": "Java 團隊共用的 skills 與 MCP 設定",
      "version": "1.0.0",
      "source": "./plugins/acme-java-toolkit"
    }
  ]
}
```

```bash
copilot plugin marketplace add acme-corp/copilot-plugins     # 開發者註冊
copilot plugin install acme-java-toolkit@acme-copilot-plugins
```

也可以在 Repo 設定 `.github/copilot/settings.json` 用 `extraKnownMarketplaces` 與 `enabledPlugins` **宣告式**地讓成員自動安裝；只在 Repo 中啟用的 plugin 只對該 Repo 生效，離開 Repo 即停用。

#### 10.3.4 企業管控

| 受管設定 | 效果 |
|------|------|
| `strictKnownMarketplaces` | 只允許清單中的 marketplace；**空陣列會連內建 marketplace 一起封鎖** |
| `extraKnownMarketplaces` | 加入受信任的 marketplace（逐項鎖定，使用者無法改指向） |
| `enabledPlugins` | 強制啟用或停用特定 plugin（逐項鎖定） |

### 10.4 Extensions（實驗性）

Extension 是一個 Node.js 模組（子目錄中的 `extension.mjs`、`extension.cjs` 或 `extension.js`），以獨立程序執行並連回 Session，可以新增代理可呼叫的**工具**與你使用的**slash 指令**。

| 位置 | 範圍 |
|------|------|
| `.github/extensions/名稱/` | 專案 |
| `~/.copilot/extensions/名稱/` | 個人 |
| 已安裝的 plugin | Plugin |

啟用需要實驗性模式（`--experimental` 或 `/experimental on`）。`/extensions mode` 有三種模式：

| 模式 | 說明 |
|------|------|
| Load & Augment（預設） | 執行 extensions，且代理可以列出、檢查、建立、重新載入 extensions |
| Load Only | 執行既有的 extensions，但代理**不能**建立或修改 extension 程式碼 |
| Disabled | 完全停用，持續到切換回其他模式 |

程式化模式預設不載入專案 extensions，需設定 `GITHUB_COPILOT_PROMPT_MODE_EXTENSIONS=true`。

> ⚠️ Extension 以**你的權限**在本機執行程式碼。企業環境建議使用 **Load Only**，避免代理在工作過程中順手產生並載入新的可執行程式碼；Repo 中的 `.github/extensions/` 必須與一般程式碼一樣經過 Code Review。

### 10.5 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| `SKILL.md` | 缺 `description`、`name` 含 `/` 或特殊字元 | 必填欄位齊全，名稱與目錄一致 | `python check_config.py skill <路徑>/SKILL.md` |
| Skill 內容 | 只有原則、沒有驗證步驟 | 以「完成前必做的驗證」結尾並要求貼出輸出 | 檢查是否有可執行的驗證指令 |
| Skill 的 `allowed-tools` | 未審查腳本就預先核准 `shell` | 審查腳本後才核准，或不設定 | 逐一閱讀 skill 目錄內的腳本 |
| `plugin.json` | Agent Plugins 1.0 格式卻加入 `agents` 等自訂欄位 | 1.0 只用允許的頂層欄位；需要自訂路徑改用舊格式 | `python check_config.py plugin plugin.json` |
| `marketplace.json` | `source` 使用絕對路徑或 `..` | Repo 內相對路徑 | `python check_config.py marketplace marketplace.json` |
| 企業 plugin 治理 | 讓開發者自由加入任意 marketplace | 受管設定 `strictKnownMarketplaces` | 在測試機嘗試加入未核准的 marketplace，應被拒絕 |
| Extension 模式 | 企業預設 Load & Augment | Load Only，並審查 `.github/extensions/` | `/extensions mode` 確認目前模式 |

---

## 第 11 章：Hooks

> **本章目標**
>
> - 知道 hooks 從哪些來源載入、以什麼順序合併，以及在 Sandbox 中如何執行。
> - 正確實作 `preToolUse` 政策：讀 stdin、輸出單一 JSON 決策，並理解 fail-closed 與 fail-open 的差異。
> - 能用模擬輸入測試 hook，而不是「上線後看看會不會擋」。

### 11.1 Hooks 是什麼、適合做什麼

Hooks 是在代理生命週期的特定時間點執行的外部指令（或 HTTP 呼叫），用來做**必須確定發生**的事：攔截危險指令、稽核記錄、注入 context、通知。與 custom instructions 最大的差別是：**hooks 是程式強制執行的，指引只是給模型的建議**。

| 適合 | 不適合 |
|------|------|
| 攔截 `git push --force`、`curl \| sh` 等高風險指令 | 需要複雜推理的判斷（交給代理或人工審查） |
| 記錄每次工具使用的中繼資料 | 長時間執行的工作（逾時會被終止） |
| Session 開始時注入當日公告或分支資訊 | 取代 Sandbox（hook 只看得到指令文字，看不到指令實際做了什麼） |
| 代理結束時發送通知 | — |

### 11.2 載入來源與順序

CLI 依序載入下列來源並**全部合併執行**（同一事件在多個來源都有定義時，全部都會跑）：

| 順序 | 來源 | 位置 | 備註 |
|------|------|------|------|
| 1 | Policy hooks（機器層級） | Linux／macOS：`/etc/github-copilot/policy.d/*.json`；Windows：`C:\ProgramData\GitHub\Copilot\policy.d\*.json` 或登錄檔 `HKLM\Software\Policies\GitHub\Copilot` | 需系統管理權限安裝；**不受 `disableAllHooks` 影響、不需資料夾信任、一律在 Sandbox 外執行**；POSIX 上檔案必須屬於 root 且不可被群組或其他人寫入 |
| 2 | 使用者 hook 檔 | `~/.copilot/hooks/*.json` | — |
| 3 | Repo hook 檔 | `.github/hooks/*.json` | 需資料夾信任 |
| 4 | Repo 設定內嵌 | `.github/copilot/settings.json`、`settings.local.json` 的 `hooks` 欄位；也讀 `.claude/settings.json` | — |
| 5 | 使用者設定內嵌 | `~/.copilot/settings.json` 的 `hooks` 欄位（**不再讀 `config.json`**） | — |
| 6 | Plugin | plugin 內的 `hooks.json` 或 `hooks/hooks.json` | — |
| 7 | Agent 範圍 | custom agent frontmatter 的 `hooks`，只在選用該代理時執行（v1.0.97） | 遠端或組織代管的代理不執行 |

程式化模式（`-p`）只有在資料夾已受信任、或設定 `COPILOT_ALLOW_ALL`、或 `GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS=true` 時才載入 Repo hooks。Hook 設定在 **CLI 啟動時**載入，修改後要重新啟動。

### 11.3 設定格式

所有 hook 檔都是 `{"version": 1, "hooks": {事件名稱: [項目, ...]}}`。**缺少 `version: 1` 或 JSON 結構錯誤會讓整個檔案被拒絕**；單一項目格式錯誤則只略過那一項（`settings.json` 內嵌的 hooks 例外：任何一項錯誤會讓整個 `hooks` 欄位失效）。

#### 11.3.1 Command hook

| 欄位 | 說明 |
|------|------|
| `type` | `"command"`（可省略） |
| `bash` | Linux／macOS 執行的指令 |
| `powershell` | Windows 執行的指令（需 PowerShell 7） |
| `command` | 跨平台備援；`bash`／`powershell` 缺少時使用 |
| `exec`＋`args` | 不經 shell 直接執行程式（不可與上面三個並用；沒有管線與萬用字元展開） |
| `cwd` | 工作目錄，相對於 Repo 根目錄；**未指定時為專案根目錄**（v1.0.88 修正） |
| `env` | 環境變數 |
| `timeoutSec`（別名 `timeout`） | 逾時秒數，預設 30 |
| `matcher` | 正規表示式，以 `^(?:模式)$` 完整比對（只有部分事件支援） |

#### 11.3.2 HTTP hook 與 Prompt hook

| 類型 | 說明 |
|------|------|
| `http` | 以 JSON `POST` 送出輸入；只允許 `https://`（`COPILOT_HOOK_ALLOW_LOCALHOST=1` 時允許本機 http）；`preToolUse` 與 `permissionRequest` **必須** https；網路錯誤、逾時、非 2xx 一律 **fail-open** |
| `prompt` | 只支援 `sessionStart`，自動送出一段文字或 slash 指令；只在**新的互動式 Session** 觸發，恢復 Session 與 `-p` 模式都不會觸發 |

### 11.4 事件總覽

| 事件 | 觸發時機 | 能否影響行為 | `matcher` 比對對象 |
|------|------|------|------|
| `sessionStart` | 新建或恢復 Session | 可注入 `additionalContext` | — |
| `sessionEnd` | Session 結束（`/clear` 也會觸發，`reason: "user_exit"`） | 否 | — |
| `userPromptSubmitted` | 使用者送出提示 | `modifiedPrompt` 只對 SDK 程式化 hook 有效 | — |
| `userPromptTransformed` | 提示轉成模型輸入之前 | 可改寫模型看到的內容 | — |
| `preToolUse` | 每次工具執行前 | **可允許、拒絕、詢問或修改參數** | `toolName` |
| `postToolUse` | 工具成功後 | 可改寫結果或附加 context | `toolName` |
| `postToolUseFailure` | 工具失敗後 | exit 2 時可提供修復指引 | — |
| `permissionRequest` | 權限服務執行**之前** | 可直接允許或拒絕（適合 `-p` 模式） | `toolName` |
| `agentStop` | 主代理結束一個回合 | `decision: "block"` 可強制繼續 | — |
| `subagentStart`／`subagentStop` | 子代理啟動／完成 | 可附加 context／阻擋或改寫回傳內容 | `agentName`（start） |
| `errorOccurred` | 發生錯誤 | 否 | — |
| `preCompact` | 壓縮之前 | 否（通知） | `trigger`（`manual`／`auto`） |
| `notification` | 系統通知（背景 shell 完成、權限請求等），非同步、不阻塞 | 可注入 context | `notification_type` |

**事件名稱的大小寫決定輸入格式**：camelCase（`preToolUse`）收到 camelCase 欄位（`toolName`、`toolArgs`）；PascalCase（`PreToolUse`）收到與 VS Code 相容的 snake_case 欄位（`tool_name`、`tool_input`），而且使用 **Claude 的 matcher 語意與工具名稱**（`Bash`、`Edit`、`Write`、`Read`）。從 Claude Code 搬過來的 hook 用 PascalCase 名稱即可沿用。

工具名稱（camelCase 事件）：`bash`、`powershell`、`view`、`create`、`edit`、`glob`、`grep`、`web_fetch`、`task`、`ask_user`；MCP 工具以 `伺服器名稱-工具名稱` 表示。

### 11.5 `preToolUse`：攔截政策

#### 11.5.1 輸入與輸出

輸入（stdin）：

```json
{
  "sessionId": "0cb916db-26aa-40f2-86b5-1ba81b225fd2",
  "timestamp": 1760000000000,
  "cwd": "/home/dev/order-service",
  "toolName": "bash",
  "toolArgs": "{\"command\":\"git push --force origin main\"}"
}
```

官方教學說明 `toolArgs` 是 **JSON 字串**，必須再解析一次；參考文件的型別標為 `unknown`。本手冊的腳本兩種情況都處理。

輸出（stdout，**只能有一個 JSON 物件**）：

| 欄位 | 值 | 說明 |
|------|------|------|
| `permissionDecision` | `"allow"`、`"deny"`、`"ask"` | 不輸出任何東西 = 交回正常的核准流程 |
| `permissionDecisionReason` | 字串 | 拒絕時必填，會讓代理知道原因 |
| `modifiedArgs` | 物件 | 以修改後的參數取代原參數 |

`"ask"` 在 Autopilot 與 cloud agent 中會被當成拒絕（沒有人可以回答）。

#### 11.5.2 失敗語意：最容易出錯的地方

| 情況 | Command hook | HTTP hook |
|------|------|------|
| exit 0＋決策 JSON | 依 JSON 決策 | — |
| exit 0、沒有輸出 | 交回正常核准流程 | — |
| **exit 2** | **拒絕**（即使 stdout 寫了 allow） | — |
| 其他非 0（含腳本崩潰） | **拒絕**（fail-closed） | — |
| **逾時** | **放行到正常核准流程**（fail-open），連管理者部署的 policy hooks 也一樣 | fail-open |
| 網路錯誤、非 2xx | — | fail-open |
| 輸出兩個 JSON 物件 | 合併成無效 JSON，被當成**沒有輸出** | — |

三個實務推論：

1. **腳本必須快**：慢到逾時等於沒擋。不要在 `preToolUse` 中呼叫遠端服務。
2. **有 bug 的腳本會擋住所有指令**：任何未預期的非 0 結束都會拒絕工具呼叫，所以上線前一定要測試。
3. **安全邊界不能只靠 hook**：它只能比對指令文字，`bash -c "$(echo ...)"` 這類混淆可以繞過字串比對。Hook 是「攔截明顯錯誤」的護欄，真正的邊界是 Sandbox 與受管權限規則（第 13、14 章）。

#### 11.5.3 範例：Repo 層級的安全政策

設定檔 `.github/hooks/copilot-policy.json`：

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "command",
        "bash": "echo '本 Repo 受 Copilot CLI 安全政策約束：危險指令會被 preToolUse 攔截並記錄。' >&2",
        "powershell": "[Console]::Error.WriteLine('本 Repo 受 Copilot CLI 安全政策約束：危險指令會被 preToolUse 攔截並記錄。')",
        "timeoutSec": 5
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "matcher": "bash|powershell",
        "bash": "./scripts/pre-tool-policy.sh",
        "powershell": "./scripts/pre-tool-policy.ps1",
        "cwd": ".github/hooks",
        "timeoutSec": 10
      }
    ],
    "postToolUse": [
      {
        "type": "command",
        "bash": "./scripts/post-tool-audit.sh",
        "powershell": "./scripts/post-tool-audit.ps1",
        "cwd": ".github/hooks",
        "timeoutSec": 10
      }
    ]
  }
}
```

Bash 版政策 `.github/hooks/scripts/pre-tool-policy.sh`：

```bash
#!/usr/bin/env bash
# preToolUse 政策：從 stdin 讀取 JSON，必要時輸出 deny 決策。
# 注意：本腳本任何「非 0 結束」都會讓工具呼叫被拒絕（fail-closed），
#       但「逾時」會放行（fail-open），所以規則必須輕量、快速。
set -uo pipefail

INPUT="$(cat)"
TOOL_NAME="$(printf '%s' "$INPUT" | jq -r '.toolName // empty')"

# 只檢查 shell 類工具；其他工具不輸出任何東西 = 交回預設權限流程
case "$TOOL_NAME" in
  bash|powershell) ;;
  *) exit 0 ;;
esac

# toolArgs 可能是 JSON 字串，也可能已是物件，兩種都處理
COMMAND="$(printf '%s' "$INPUT" | jq -r '
  (.toolArgs | if type == "string" then (fromjson? // {}) else . end)
  | .command // empty')"

deny() {
  jq -cn --arg r "$1" '{permissionDecision: "deny", permissionDecisionReason: $r}'
  exit 0
}

# 規則 1：強制推送
if printf '%s' "$COMMAND" | grep -Eq 'git[[:space:]]+push([[:space:]].*)?[[:space:]](--force|-f)([[:space:]]|$)'; then
  deny "政策禁止 git push --force，請改用 --force-with-lease 並由人工執行。"
fi
# 規則 2：刪除根目錄、家目錄或整個工作目錄
if printf '%s' "$COMMAND" | grep -Eq 'rm[[:space:]]+-[a-zA-Z]*r[a-zA-Z]*f?[[:space:]]+(/|~|\.|\*)([[:space:]]|$)'; then
  deny "政策禁止遞迴刪除 /、~、. 或 *。"
fi
# 規則 3：下載後直接執行
if printf '%s' "$COMMAND" | grep -Eq '(curl|wget|iwr|Invoke-WebRequest)[^|]*\|[[:space:]]*(ba|z)?sh|\|[[:space:]]*iex'; then
  deny "政策禁止下載後直接執行（curl | sh、iwr | iex）。"
fi
# 規則 4：讀取或外傳密鑰檔
if printf '%s' "$COMMAND" | grep -Eq '(^|[[:space:]/])(\.env|id_rsa|id_ed25519|\.npmrc)([[:space:]]|$)'; then
  deny "政策禁止由代理直接存取密鑰檔（.env、SSH 私鑰、.npmrc）。"
fi

# 未命中任何規則：不輸出 = 交回 CLI 的正常核准流程（不是自動放行）
exit 0
```

PowerShell 版 `.github/hooks/scripts/pre-tool-policy.ps1`（Windows 使用者需要）：

```powershell
#!/usr/bin/env pwsh
# preToolUse 政策（Windows / PowerShell 7+ 版），規則與 pre-tool-policy.sh 相同。
$ErrorActionPreference = 'Stop'

$inputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json
if ($inputJson.toolName -notin @('bash', 'powershell')) { exit 0 }

$toolArgs = $inputJson.toolArgs
if ($toolArgs -is [string]) {
    try { $toolArgs = $toolArgs | ConvertFrom-Json } catch { $toolArgs = $null }
}
$command = if ($toolArgs -and $toolArgs.command) { [string]$toolArgs.command } else { '' }

function Deny([string]$reason) {
    @{ permissionDecision = 'deny'; permissionDecisionReason = $reason } |
        ConvertTo-Json -Compress
    exit 0
}

if ($command -match 'git\s+push(\s.*)?\s(--force|-f)(\s|$)') {
    Deny '政策禁止 git push --force，請改用 --force-with-lease 並由人工執行。'
}
if ($command -match 'rm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+(/|~|\.|\*)(\s|$)' -or
    $command -match 'Remove-Item\s.*-Recurse.*\s(/|~|\.|\*|C:\\)(\s|$)') {
    Deny '政策禁止遞迴刪除 /、~、. 或 *。'
}
if ($command -match '(curl|wget|iwr|Invoke-WebRequest)[^|]*\|\s*((ba|z)?sh|iex|Invoke-Expression)') {
    Deny '政策禁止下載後直接執行（curl | sh、iwr | iex）。'
}
if ($command -match '(^|[\s/\\])(\.env|id_rsa|id_ed25519|\.npmrc)(\s|$)') {
    Deny '政策禁止由代理直接存取密鑰檔（.env、SSH 私鑰、.npmrc）。'
}
exit 0
```

#### 11.5.4 範例：只記錄中繼資料的稽核

```bash
#!/usr/bin/env bash
# postToolUse 稽核：只記錄中繼資料（時間、Session、工具名稱、結果類型），
# 不記錄完整參數與輸出，避免把密鑰寫進日誌。
set -uo pipefail

LOG_DIR="${COPILOT_AUDIT_DIR:-logs}"
mkdir -p "$LOG_DIR"

jq -c '{
  ts: (.timestamp // 0),
  session: (.sessionId // ""),
  tool: (.toolName // ""),
  result: (.toolResult.resultType // "unknown"),
  cwd: (.cwd // "")
}' >> "$LOG_DIR/copilot-audit.jsonl"

# 不輸出任何 JSON = 保留原本的工具結果
exit 0
```

PowerShell 版：

```powershell
#!/usr/bin/env pwsh
# postToolUse 稽核（PowerShell 版）：只記錄中繼資料。
$ErrorActionPreference = 'Stop'
$logDir = if ($env:COPILOT_AUDIT_DIR) { $env:COPILOT_AUDIT_DIR } else { 'logs' }
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$in = [Console]::In.ReadToEnd() | ConvertFrom-Json
$record = [ordered]@{
    ts      = if ($in.timestamp) { $in.timestamp } else { 0 }
    session = [string]$in.sessionId
    tool    = [string]$in.toolName
    result  = if ($in.toolResult.resultType) { $in.toolResult.resultType } else { 'unknown' }
    cwd     = [string]$in.cwd
}
($record | ConvertTo-Json -Compress) | Add-Content -Path (Join-Path $logDir 'copilot-audit.jsonl') -Encoding utf8
exit 0
```

> ⚠️ 官方教學特別提醒：工具參數可能含有 Token、密碼等憑證，**記錄前要遮蔽**，或只記錄工具名稱、時間、決策等中繼資料，並送到有存取控制與保存政策的集中式日誌系統。範例刻意不記錄 `toolArgs` 與工具輸出。稽核日誌目錄要加入 `.gitignore`。

#### 11.5.5 測試 hook

不要等上線才知道 hook 有沒有效。下列腳本以模擬的 stdin 驅動 Bash 與 PowerShell 兩個版本，確認「該放行的放行、該擋的擋」：

```bash
#!/usr/bin/env bash
# 以模擬的 preToolUse / postToolUse 輸入驅動 hook 腳本，驗證決策是否符合預期。
# 用法：bash test_hooks.sh <hooks 目錄>（預設 repo/.github/hooks）
set -u
HOOKS="${1:-$(dirname "$0")/repo/.github/hooks}"
pass=0; fail=0

# 參數：說明、預期(deny|none)、執行器(bash|pwsh)、輸入 JSON
check() {
  local desc="$1" expect="$2" runner="$3" input="$4" out got
  if [ "$runner" = pwsh ]; then
    out="$(printf '%s' "$input" | pwsh -NoProfile -File "$HOOKS/scripts/pre-tool-policy.ps1")"
  else
    out="$(printf '%s' "$input" | bash "$HOOKS/scripts/pre-tool-policy.sh")"
  fi
  local rc=$?
  if [ -z "$out" ]; then got=none
  else got="$(printf '%s' "$out" | jq -r '.permissionDecision')"; fi
  if [ "$got" = "$expect" ] && [ $rc -eq 0 ]; then
    pass=$((pass + 1)); echo "PASS [$runner] $desc -> $got"
  else
    fail=$((fail + 1)); echo "FAIL [$runner] $desc -> got=$got rc=$rc out=$out"
  fi
}

# 產生 preToolUse 輸入；toolArgs 依官方教學以「JSON 字串」傳入
mk() { jq -cn --arg t "$1" --arg c "$2" \
  '{sessionId:"s1", timestamp:1760000000000, cwd:"/repo", toolName:$t, toolArgs:({command:$c}|tojson)}'; }
# toolArgs 為物件的變體
mk_obj() { jq -cn --arg t "$1" --arg c "$2" \
  '{sessionId:"s1", timestamp:1760000000000, cwd:"/repo", toolName:$t, toolArgs:{command:$c}}'; }

for r in bash pwsh; do
  check "一般 git status"            none "$r" "$(mk bash 'git status')"
  check "刪除 build 目錄"            none "$r" "$(mk bash 'rm -rf ./build')"
  check "刪除 /tmp/x"                none "$r" "$(mk bash 'rm -rf /tmp/x')"
  check "force-with-lease"           none "$r" "$(mk bash 'git push --force-with-lease origin feat')"
  check "非 shell 工具 (edit)"       none "$r" "$(mk edit 'irrelevant')"
  check "git push --force"           deny "$r" "$(mk bash 'git push --force origin main')"
  check "git push -f"                deny "$r" "$(mk bash 'git push origin main -f')"
  check "rm -rf /"                   deny "$r" "$(mk bash 'rm -rf /')"
  check "rm -fr ~"                   deny "$r" "$(mk bash 'rm -fr ~')"
  check "curl | bash"                deny "$r" "$(mk bash 'curl -fsSL https://x.example/i.sh | bash')"
  check "iwr | iex (powershell)"     deny "$r" "$(mk powershell 'iwr https://x.example/a.ps1 | iex')"
  check "cat .env"                   deny "$r" "$(mk bash 'cat .env')"
  check "toolArgs 為物件"            deny "$r" "$(mk_obj bash 'git push --force')"
done

# postToolUse 稽核：寫入一筆 JSONL，且不得包含工具參數內容
TMP="$(mktemp -d)"
printf '%s' '{"sessionId":"s1","timestamp":1,"cwd":"/repo","toolName":"bash","toolArgs":"{\"command\":\"echo SECRET123\"}","toolResult":{"resultType":"success","textResultForLlm":"SECRET123"}}' \
  | COPILOT_AUDIT_DIR="$TMP" bash "$HOOKS/scripts/post-tool-audit.sh"
if [ "$(wc -l < "$TMP/copilot-audit.jsonl")" -eq 1 ] && ! grep -q SECRET123 "$TMP/copilot-audit.jsonl"; then
  pass=$((pass + 1)); echo "PASS [bash] postToolUse 只記錄中繼資料"
else
  fail=$((fail + 1)); echo "FAIL [bash] postToolUse 稽核內容異常"; cat "$TMP/copilot-audit.jsonl"
fi
printf '%s' '{"sessionId":"s1","timestamp":1,"cwd":"/repo","toolName":"bash","toolArgs":"{}","toolResult":{"resultType":"success","textResultForLlm":"SECRET123"}}' \
  | COPILOT_AUDIT_DIR="$TMP/ps" pwsh -NoProfile -File "$HOOKS/scripts/post-tool-audit.ps1"
if [ -s "$TMP/ps/copilot-audit.jsonl" ] && ! grep -q SECRET123 "$TMP/ps/copilot-audit.jsonl"; then
  pass=$((pass + 1)); echo "PASS [pwsh] postToolUse 只記錄中繼資料"
else
  fail=$((fail + 1)); echo "FAIL [pwsh] postToolUse 稽核內容異常"
fi
rm -rf "$TMP"

echo "結果：PASS=$pass FAIL=$fail"
[ "$fail" -eq 0 ]
```

本手冊在 Windows 11（Git Bash＋jq 1.8.1、PowerShell 7）實際執行的結果為 `PASS=28 FAIL=0`（附錄 H.3）。

手動測試單一案例：

```bash
echo '{"toolName":"bash","toolArgs":"{\"command\":\"rm -rf /\"}"}' \
  | bash .github/hooks/scripts/pre-tool-policy.sh
# 預期輸出：{"permissionDecision":"deny","permissionDecisionReason":"政策禁止遞迴刪除 /、~、. 或 *。"}
```

### 11.6 其他事件的決策控制

#### 11.6.1 `permissionRequest`

在權限服務（規則、Session 核准、自動允許／拒絕、詢問使用者）之前執行，回傳 `{"behavior": "allow"}` 或 `{"behavior": "deny", "message": "原因", "interrupt": true}` 會直接短路正常流程；回傳空值則照常處理。command hook 以 exit 2 代表拒絕。**例外**：要求跳出 Sandbox 的請求（`requestSandboxBypass: true`），hook 的 allow **不會**預先核准，使用者一定要互動確認；只有 deny 會生效。

#### 11.6.2 `agentStop`／`subagentStop`

回傳 `{"decision": "block", "reason": "請先執行 ./mvnw verify 並修正所有失敗"}` 會強制代理再做一個回合，`reason` 就是下一回合的提示。連續 8 次 block 後 CLI 會強制結束回合以防無限迴圈；輸入中的 `stop_hook_active` 為 `true` 代表本回合已經是被強制延續的，hook 應據此自我節制。`subagentStop` 另可用 `modifiedResponse` 改寫回傳給主代理的內容（例如遮蔽敏感資訊）。

#### 11.6.3 `postToolUse`

回傳 `{"additionalContext": "提醒：此檔案屬於公開 API，修改需更新 CHANGELOG"}` 會附加在工具結果後面讓模型看到；`modifiedResult` 可取代結果。多個 hook 的 `additionalContext` 以兩個換行串接，上限 10 KB。

#### 11.6.4 進度訊息

hook 執行中可以先輸出 `{"type": "progress", "message": "檢查政策中..."}`（每則獨立一行），再輸出最後的決策 JSON；加上 `"temporary": true` 則是會被取代的暫時狀態列。進度訊息只用於顯示，不影響決策。

### 11.7 Sandbox 中的 hooks

啟用 Sandbox 時，Repo、使用者與 plugin 的 command hooks **在 Sandbox 內執行**，權限與代理的 shell 指令相同；`cwd` 與 `env` 不能擴大存取範圍（例如在 `env` 設定 `TMPDIR` 不會因此獲得該目錄的權限）。需要更多存取時，在使用者設定的 `sandbox.userPolicy` 加入路徑。Policy hooks 則一律在 Sandbox 外執行，因此**不應該執行工作區中的腳本**。

### 11.8 停用 hooks

| 位置 | 效果 |
|------|------|
| 單一 hook 檔內 `"disableAllHooks": true` | 只略過該檔案 |
| Repo `settings.json` 的 `disableAllHooks` | 該 Repo 的所有 hooks（Repo、使用者、plugin、內嵌）都略過；**policy hooks 不受影響** |
| 使用者設定 `disableAllHooks` | 停用 Repo 與使用者層級的 hooks |
| 受管設定 `allowManagedHooksOnly` | 只允許受管的 hooks；v1.0.85 起也封鎖 extension 註冊的 `preToolUse`／`postToolUse` 回呼 |

> ⚠️ 開發者可以在 `settings.local.json` 設定 `disableAllHooks` 關掉 Repo 的安全 hooks。**必須確保執行的控制要用 policy hooks 或受管設定部署**，不能只靠 Repo hooks。

### 11.9 v1 手冊的錯誤寫法對照

| v1 手冊寫法 | 問題 | 正確寫法 |
|------|------|------|
| 缺少 `"version": 1` | 整個檔案被拒絕載入 | 加上 `"version": 1` |
| `"matcher": "shell"` | shell 工具名稱是 `bash`／`powershell` | `"matcher": "bash\|powershell"` |
| `"permission": "deny"` | 不存在的欄位 | 由腳本輸出 `permissionDecision` |
| 從環境變數 `TOOL_INPUT`、`TOOL_NAME`、`FILE_PATH` 讀取 | 輸入是 **stdin 的 JSON**，沒有這些環境變數 | `INPUT="$(cat)"` 後用 `jq` 解析 |
| 以 `sys.exit(1)` 表示拒絕 | 會拒絕，但代理只收到「hook 出錯」，不知道原因 | exit 0 並輸出含 `permissionDecisionReason` 的 deny JSON |
| JSON 範例第一行寫 `// .github/hooks/hooks.json` | JSON 不允許註解，檔案無法解析 | 檔名寫在內文說明 |

### 11.10 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| Hook 設定檔 | 缺 `version`、未知欄位、事件名稱拼錯 | 依 11.3 節格式 | `python check_config.py hooks .github/hooks/*.json` |
| 跨平台 | 只有 `bash` | 同時提供 `bash` 與 `powershell` | checker 會警告只有 bash 的項目 |
| `preToolUse` 腳本 | 從環境變數讀輸入、輸出多個 JSON | 讀 stdin、只輸出一個決策 JSON | 用 11.5.5 節的測試腳本跑正反案例 |
| 腳本健壯性 | `set -e` 下任何小錯都非 0 結束，導致所有指令被拒 | 明確處理錯誤，只在命中規則時輸出 deny | 送入格式錯誤的 JSON，確認行為符合預期 |
| 逾時設定 | `timeoutSec: 120` 並呼叫遠端 API | 本機快速比對，逾時短 | checker 會警告 `preToolUse` 逾時過長；量測腳本執行時間 |
| 稽核內容 | 記錄完整 `toolArgs` 與輸出 | 只記錄中繼資料或先遮蔽 | 送入含假 Token 的輸入，確認日誌中沒有該字串 |
| 強制性控制 | 只用 Repo hooks 實作公司政策 | 用 policy hooks 或受管設定 | 在 `settings.local.json` 設 `disableAllHooks: true`，確認政策仍生效 |

---

## 第 12 章：LSP、ACP、SDK、自訂模型與可觀測性

> **本章目標**
>
> - 為專案設定 LSP，讓代理取得型別、定義與診斷資訊。
> - 理解 ACP 與 Copilot SDK 的用途差異，知道何時把 CLI 當成元件整合。
> - 安全地設定 BYOK（自備模型），並以 OpenTelemetry 觀測代理行為與成本。

### 12.1 LSP 語言伺服器

LSP 讓代理可以使用「跳到定義、查型別、取得診斷」等程式碼智慧，減少盲目搜尋。**CLI 不內建語言伺服器**，需要自行安裝。

| 層級 | 位置 |
|------|------|
| 使用者 | `~/.copilot/lsp-config.json` |
| Repo | `.github/lsp.json` |
| Plugin | `lsp-config/servers.json` 或 `plugin.json` 的 `lspServers` |

```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileExtensions": { ".ts": "typescript", ".tsx": "typescriptreact" }
    },
    "java": {
      "command": "jdtls",
      "fileExtensions": { ".java": "java" },
      "rootUri": "."
    }
  }
}
```

| 欄位 | 必填 | 說明 |
|------|------|------|
| `command`／`bash`／`powershell` | 擇一 | 啟動指令；跨平台時用 `bash` 與 `powershell` |
| `args` | | 參數（只用於 `command`） |
| `fileExtensions` | ✅ | 副檔名對應 language ID，例如 `{".ts": "typescript"}` |
| `rootUri` | | 相對於 Git 根目錄的專案根，預設 `.` |
| `env`、`cwd`、`initializationOptions` | | 環境變數、工作目錄、初始化選項 |

```bash
npm install -g typescript-language-server typescript   # 先安裝語言伺服器
copilot lsp list [--json]                              # 列出設定的語言伺服器與負責的副檔名
```

互動式介面用 `/lsp`（`show`、`test`、`reload`、`logs`）啟動、測試與查看日誌。啟用 Sandbox 時，語言伺服器預設也在 Sandbox 中執行（`sandboxLspServers`）。

### 12.2 ACP（Agent Client Protocol）

ACP 是編輯器與代理之間的開放協定，讓任何支援 ACP 的工具把 Copilot CLI 當成代理後端使用（公開預覽）。

```bash
copilot --acp                       # 預設 stdio 模式（由用戶端啟動子程序）
copilot --acp --stdio               # 明確指定 stdio
copilot --acp --port 3000           # TCP 模式，可接受多個連線
copilot --acp --port 3000 --effort=max --available-tools="bash,view"   # 對所有 Session 生效的設定
```

| 面向 | stdio | TCP |
|------|------|------|
| 連線方式 | 用戶端以子程序啟動，透過標準輸入輸出交換 NDJSON | 連到 TCP 埠 |
| 用戶端數 | 一個 | 多個 |
| 生命週期 | 父程序結束即停止 | 獨立運作 |
| 適合 | IDE 整合（推薦） | 跨程序或容器、長時間運作的服務 |

ACP 的 `session/new` 只能設定工作目錄與 MCP 伺服器；工具過濾、推理強度要在**啟動伺服器時**以旗標設定。企業受管設定也會套用到 ACP Session（v1.0.88 起）。

> ⚠️ TCP 模式會開啟網路監聽埠。只在本機或受控網路使用，不要對外暴露。

### 12.3 Copilot SDK

Copilot SDK（[github/copilot-sdk](https://github.com/github/copilot-sdk)）把與 CLI 相同的代理執行環境開放給應用程式整合，Repo 中提供 Node.js、Python、Go、.NET、Java、Rust 的實作。

| 部署方式 | 說明 |
|------|------|
| Bundled CLI（預設） | Node.js 與 .NET SDK 內含 CLI；Python 以 `python -m copilot download-runtime` 下載。SDK 以子程序啟動並管理版本 |
| Local CLI | 使用機器上已安裝的 `copilot` |

TypeScript 最小範例（取自官方文件）：

```typescript
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();
const session = await client.createSession({ model: "gpt-5.4" });
const response = await session.sendAndWait({ prompt: "Hello!" });
console.log(response?.data.content);
await client.stop();
```

| 選擇 | 情境 |
|------|------|
| `copilot -p` | 腳本、CI 的一次性任務 |
| ACP | 讓既有編輯器或工具接上 Copilot |
| SDK | 在自己的應用程式中嵌入代理能力，需要細緻控制 Session、權限回呼與事件 |

> ⚠️ SDK 範例中常見的 `PermissionHandler.approve_all` 會核准所有工具請求，只適合 Sandbox 或拋棄式環境；正式應用要實作自己的權限回呼。

### 12.4 自訂模型供應商（BYOK）

#### 12.4.1 支援的供應商與需求

| `COPILOT_PROVIDER_TYPE` | 相容服務 |
|------|------|
| `openai`（預設） | OpenAI、Ollama、vLLM、Foundry Local 等 OpenAI 相容端點 |
| `azure` | Azure OpenAI（可用主機 URL 或含 `/api/projects/<專案>` 的完整專案 URL） |
| `anthropic` | Anthropic |

模型必須支援 **tool calling** 與 **streaming**，建議 context window 至少 128k tokens。

#### 12.4.2 設定範例

```bash
# 本機 Ollama（不需要 API key）
export COPILOT_PROVIDER_BASE_URL=http://localhost:11434/v1
export COPILOT_MODEL=qwen3-coder:30b
copilot

# Azure OpenAI：部署名稱與基礎模型不同時，用 MODEL_ID 告訴 CLI 模型能力
export COPILOT_PROVIDER_TYPE=azure
export COPILOT_PROVIDER_BASE_URL=https://acme-ai.openai.azure.com
export COPILOT_PROVIDER_MODEL_ID=gpt-5.4
export COPILOT_PROVIDER_WIRE_MODEL=acme-gpt54-prod
export COPILOT_MODEL=acme-gpt54-prod
# 每次請求前取得新的短效金鑰，不把金鑰留在環境變數
export COPILOT_PROVIDER_API_KEY_COMMAND='az keyvault secret show --vault-name acme-kv --name aoai-key --query value -o tsv'
copilot
```

| 變數 | 說明 |
|------|------|
| `COPILOT_PROVIDER_API_KEY` | API key（`openai` 以 `Authorization` 送出、`azure` 以 `api-key`、`anthropic` 以 `x-api-key`） |
| `COPILOT_PROVIDER_API_KEY_COMMAND` | 每次請求執行一次、輸出新金鑰；優先於 `API_KEY` |
| `COPILOT_PROVIDER_BEARER_TOKEN` | Bearer token，優先於 `API_KEY` |
| `COPILOT_PROVIDER_WIRE_API` | `completions`（預設）或 `responses`（GPT-5 系列使用） |
| `COPILOT_PROVIDER_TRANSPORT` | `http`（預設）或 `websockets` |
| `COPILOT_PROVIDER_HEADERS` | 只送給供應商的自訂標頭（例如閘道金鑰），以換行分隔 |
| `COPILOT_PROVIDER_MAX_PROMPT_TOKENS`／`MAX_OUTPUT_TOKENS` | 手動指定 token 上限 |
| `COPILOT_PROVIDERS_CONFIG` | 供應商與模型註冊檔，預設 `~/.copilot/providers.json`；有內容時優先於 `COPILOT_PROVIDER_*` |

#### 12.4.3 BYOK 的治理要點

| 要點 | 說明 |
|------|------|
| 不受企業模型政策控制 | 使用者本機設定的 BYOK 模型不經企業模型啟用政策；`.github/allowed_models.txt` 也**不能**過濾 BYOK 模型 |
| 程式碼送往何處 | 提示與程式碼 context 會送到你設定的端點；端點的資料保存政策需另行審查 |
| 成本 | 不經 AI Credits 計費，CLI 會隱藏成本估算（仍顯示 token 數） |
| 子代理 | 內建子代理（`/review`、explore、`/fleet`）會沿用 BYOK 設定 |
| `/delegate` | 仍需要 GitHub 登入，工作會交給 GitHub 雲端，不是你的供應商 |
| 封鎖 BYOK | 受管設定 `forceLoginOrgs` 會拒絕 BYOK／API key 驗證 |
| 離線 | `COPILOT_OFFLINE=true` 不連 GitHub；只有端點也在隔離網路內時才是真正離線 |

企業也可以由管理者在企業層級提供自訂模型金鑰，這類模型會出現在 `/model` 清單底部，並受企業政策管理，比個人 BYOK 更適合正式導入。

### 12.5 OpenTelemetry 可觀測性

#### 12.5.1 啟用條件

預設關閉。下列任一條件成立即啟用：`COPILOT_OTEL_ENABLED=true`、設定 `OTEL_EXPORTER_OTLP_ENDPOINT`、設定 `COPILOT_OTEL_FILE_EXPORTER_PATH`；企業也可用受管設定 `telemetry` 推送設定。

```bash
# 輸出到本機 JSON Lines 檔（離線或 CI 稽核）
COPILOT_OTEL_FILE_EXPORTER_PATH=/tmp/copilot-otel.jsonl copilot

# 企業 Collector（私有 CA＋mTLS）
OTEL_EXPORTER_OTLP_ENDPOINT=https://otel-collector.corp.example:4318 \
OTEL_EXPORTER_OTLP_CERTIFICATE=/etc/otel/ca.pem \
OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE=/etc/otel/client.pem \
OTEL_EXPORTER_OTLP_CLIENT_KEY=/etc/otel/client.key \
OTEL_RESOURCE_ATTRIBUTES="team=order,env=dev" \
copilot
```

> ⚠️ **靜默失敗陷阱**：使用 otlp-http 匯出器但端點是 `http://`（包括預設的 `http://localhost:4318`）時，CLI 會**停用匯出而不是以明文傳送**，而且只在程序日誌（`~/.copilot/logs`）留下警告，畫面上不會顯示。`--log-level error` 或 `none` 時連警告都沒有。驗證時請檢查 Collector 端是否真的收到資料。另外 `NODE_EXTRA_CA_CERTS` 對 OTLP 匯出器無效，要用 `OTEL_EXPORTER_OTLP_CERTIFICATE`；協定只支援 `http/json`（預設）與 `http/protobuf`，`grpc` 會退回預設。

#### 12.5.2 匯出的資料

Traces 依 OTel GenAI 語意慣例：

```text
invoke_agent                    代理協調（包含所有 LLM 呼叫與工具執行）
  plan                          Plan 模式的任務拆解
    chat <model>
    execute_tool <tool>
  chat <model>                  單次 LLM API 呼叫
  execute_tool <tool>           單次工具呼叫
```

常用指標：

| 指標 | 用途 |
|------|------|
| `gen_ai.client.inference.usage.input_tokens`／`output_tokens` | token 用量（成本分析） |
| `gen_ai.client.inference.usage.cache_read.input_tokens` | 快取命中（成本優化） |
| `gen_ai.client.operation.duration` | LLM 呼叫延遲 |
| `github.copilot.tool.call.count`／`duration` | 工具使用次數與延遲 |
| `github.copilot.code.lines_added`／`lines_removed` | 代理修改的行數 |
| `github.copilot.agent.turn.count` | 每次呼叫的 LLM 來回次數 |
| `github.copilot.sandbox.*` | Sandbox 狀態轉換與啟動延遲（不是完整稽核日誌） |

#### 12.5.3 內容擷取

預設**只擷取中繼資料**。設定 `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true` 會擷取完整提示、回應、系統指示、工具參數與結果，以及 Sandbox 的路徑規則與被拒的資源。這些資料可能包含程式碼與機敏資訊，**只能在受信任、有存取控制的環境啟用**；企業可用受管設定 `telemetry.lockCaptureContent` 鎖定。

Hooks 輸入也會帶有 `traceparent`（v1.0.81），可以讓 hook 產生與代理同一條 trace 的 span。

### 12.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| `.github/lsp.json` | 缺 `fileExtensions` 或副檔名沒有 `.` | 依 12.1 節欄位 | `python check_config.py lsp .github/lsp.json`；`copilot lsp list` |
| ACP 部署 | TCP 模式綁定對外介面 | stdio 或只在本機的 TCP | `netstat`／`ss` 確認監聽位址 |
| SDK 整合 | 正式應用使用 `approve_all` | 實作權限回呼並記錄決策 | 程式碼審查權限處理路徑 |
| BYOK 設定 | API key 寫在 shell 設定檔或 Repo | `API_KEY_COMMAND` 從金鑰庫取得 | `grep -r COPILOT_PROVIDER_API_KEY` 檢查是否外洩 |
| BYOK 治理說明 | 「allowed_models.txt 可以限制 BYOK」 | 說明 BYOK 不受此檔與企業模型政策限制 | 對照官方 config-dir reference |
| OTel 設定 | 對 `http://` Collector 設定後以為有資料 | 使用 `https://`，並在 Collector 端確認收到資料 | 檢查 `~/.copilot/logs` 警告與 Collector 指標 |
| 內容擷取 | 在共用 Collector 開啟 `CAPTURE_MESSAGE_CONTENT` | 預設關閉，必要時限定環境並鎖定 | 檢查受管設定 `telemetry` 與 Collector 存取權限 |

---

## 第 13 章：權限模型

> **本章目標**
>
> - 理解工具、路徑、網址三類權限，以及「可見工具」與「核准規則」兩層控制。
> - 能寫出正確的 `--allow-tool`／`--deny-tool` 規則，並預測它會比對到哪些指令。
> - 能依情境選擇核准模式（manual、assisted、allow-all），並了解 YOLO 的實際風險。

### 13.1 三類權限與預設行為

| 類別 | 預設行為 | 相關選項 |
|------|------|------|
| 工具 | 唯讀操作（搜尋、讀檔、唯讀 shell 指令）自動允許；修改系統的操作需核准 | `--allow-tool`、`--deny-tool`、`--allow-all-tools`、`--available-tools`、`--excluded-tools` |
| 路徑 | 只能存取工作目錄、其子目錄與系統暫存目錄 | `--add-dir`、`--allow-all-paths`、`--disallow-temp-dir` |
| 網址 | 每個網址都需要核准；協定有區別（核准 `https://` 不代表允許 `http://`） | `--allow-url`、`--deny-url`、`--allow-all-urls` |

`--allow-all`（別名 `--yolo`）等於同時使用 `--allow-all-tools --allow-all-paths --allow-all-urls`。

> ⚠️ **路徑與網址偵測是啟發式的**。官方文件明載：shell 指令中的路徑是靠斷詞猜測；只展開 `HOME`、`TMPDIR`、`PWD` 等少數變數，自訂變數如 `$MY_PROJECT_DIR` 不會展開；建立中的檔案不解析 symlink；檔案內容、設定檔或環境變數中的網址、拆開的字串都偵測不到。**權限規則不是安全邊界**，真正的隔離要靠 Sandbox（第 14 章）。

### 13.2 兩層工具控制

```mermaid
flowchart LR
    A[模型想使用工具] --> B{在可見工具集內?<br/>--available-tools / --excluded-tools}
    B -- 否 --> X[模型根本看不到此工具]
    B -- 是 --> C{符合 deny 規則?}
    C -- 是 --> D[拒絕]
    C -- 否 --> E{符合 allow 規則<br/>或已儲存的核准?}
    E -- 是 --> F[直接執行]
    E -- 否 --> G[詢問使用者<br/>程式化模式則自動拒絕]
```

| 層次 | 選項 | 效果 |
|------|------|------|
| 可見工具 | `--available-tools` | 只讓模型看到列出的工具（同時使用時 `--excluded-tools` 會被忽略） |
| | `--excluded-tools` | 讓模型看不到列出的工具 |
| 核准規則 | `--deny-tool` | 一律拒絕，**優先於任何 allow，包括 `--allow-all` 與已儲存的核准** |
| | `--allow-tool` | 不詢問直接允許 |

可見工具名稱：`bash`／`powershell`（以及 `list_`、`read_`、`stop_`、`write_` 前綴的 shell 管理工具）、`view`、`create`、`edit`、`apply_patch`、`glob`、`grep`（或 `rg`）、`web_fetch`、`task`、`list_agents`、`read_agent`、`write_agent`、`ask_user`、`skill`。

### 13.3 權限規則語法

格式為 `種類(參數)`，參數可省略（代表該種類全部）。多個規則可重複使用旗標，或以逗號分隔放在同一個加引號的字串中。

| 種類 | 範例 | 比對方式 |
|------|------|------|
| `shell` | `shell`、`shell(npm test)`、`shell(git:*)` | 預設**完全比對**指令名稱；`git`、`gh` 以第一層子指令比對（`git push`）；`:*` 比對字首後接空白 |
| `write` | `write`、`write(.env)`、`write(/repo/.env)` | 非 shell 的寫入工具；相對路徑以**結尾路徑片段**比對（`write(.env)` 符合任何目錄下的 `.env`）；不支援 glob |
| `read` | `read`、`read(.env)` | 讀取檔案或目錄 |
| `url` | `url(github.com)`、`url(https://*.github.com)`、`url(http://localhost:3000)` | 未寫協定時預設 `https://`；萬用字元只能在主機名稱開頭或路徑結尾 |
| `memory` | `memory` | 寫入 Copilot Memory |
| MCP 伺服器名稱 | `github-mcp-server(create_issue)`、`MyMCP` | 指定伺服器的工具，省略工具名稱代表全部 |

#### 13.3.1 比對行為對照

| 規則 | 會比對到 | 不會比對到 |
|------|------|------|
| `shell(git:*)` | `git status`、`git push origin main` | `gitea serve` |
| `shell(git push)` | `git push`、`git push --force origin main` | `git status` |
| `shell(npm test)` | `npm test` | `npm test -- --watch`？（依完全比對原則不會；需要時用 `shell(npm test:*)`） |
| `shell(npm run:*)` | `npm run build`、`npm run lint` | `npm install` |
| `write(.env)` | `/repo/.env`、`/repo/config/.env` | `/repo/.env.example` |

> 💡 規則有疑問時，先在拋棄式 Repo 用**互動模式**實測：不加 allow 規則，觀察核准對話框顯示的指令識別碼，再據此寫規則。

#### 13.3.2 情境範例

```bash
# 開發：可以改檔與跑 git，但不能 push、不能刪檔
copilot --allow-tool='write' --allow-tool='shell(git:*)' \
        --deny-tool='shell(git push)' --deny-tool='shell(rm)'

# 唯讀分析：模型只看得到探索與讀取工具
copilot --available-tools='view,grep,glob' -p "說明 order 模組的分層架構" -s

# 受限但可提交：能探索、修改、commit，但無法上網、無法開子代理、無法 push
copilot --available-tools='bash,edit,view,grep,glob' \
        --allow-tool='shell(git:*)' --deny-tool='shell(git push)'

# 允許 MCP 伺服器的全部工具，但禁止其中一個
copilot --allow-tool='github-mcp-server' --deny-tool='github-mcp-server(merge_pull_request)'

# 只允許特定網站
copilot --allow-url=github.com --allow-url=repo.maven.apache.org --deny-url=pastebin.com
```

#### 13.3.3 ❌／✅ 對照

| ❌ | ✅ | 說明 |
|------|------|------|
| `--allow-tool='shell(git*)'` | `--allow-tool='shell(git:*)'` | 單獨的 `*` 沒有特殊意義，字首比對必須用 `:*` |
| `--allow-tool='write(src/**/*.java)'` | `--allow-tool='write'` 搭配 Sandbox 路徑限制 | `write` 規則目前不支援 glob |
| `--allow-all-tools --allow-tool='shell(rm)'` 以為可以限制 | `--allow-all-tools --deny-tool='shell(rm)'` | allow 不能縮小範圍，要用 deny |
| `alias copilot='copilot --yolo'` | 不要用 alias 永久套用 allow-all | 官方明確警告不要這樣做 |
| `--deny-tool='shell(git push --force)'` | `--deny-tool='shell(git push)'`＋hook 檢查 `--force` | `git` 以第一層子指令比對，旗標層級要靠 hook |

### 13.4 已儲存的核准

| 核准方式 | 儲存位置 | 範圍 |
|------|------|------|
| 對話框選「本 Session」 | 記憶體 | 目前執行中的 Session |
| 對話框選「This location」 | `~/.copilot/permissions-config.json` | 該 Git 根目錄（linked worktree 共用主 Repo）或目錄 |
| 永久核准網址 | `settings.json` 的 `allowedUrls` | 所有 Session |
| 指令列旗標 | 不儲存 | 本次執行 |

`permissions-config.json` 只支援允許，不支援 deny、ask、URL 規則；`shell` 的 `commandIdentifiers` 為字面比對，只有結尾的 `:*` 有字首比對效果。範例：

```json
{
  "locations": {
    "/home/dev/src/order-service": {
      "tool_approvals": [
        { "kind": "commands", "commandIdentifiers": ["git status", "git diff", "./mvnw:*"] },
        { "kind": "mcp", "serverName": "github-mcp-server", "toolName": "search_code" }
      ],
      "allowed_directories": ["/home/dev/src/shared-docs"]
    }
  }
}
```

| 清除方式 | 效果 |
|------|------|
| `/permissions reset` | 只清除本 Session 記憶體中的核准 |
| `/reset-allowed-tools` | 清除本 Session 的核准，**也清除目前位置**在 `permissions-config.json` 的核准，回到啟動旗標定義的狀態 |
| `/list-dirs` | 列出允許的目錄與精確路徑核准 |

### 13.5 核准模式

```text
/permissions show            # 目前模式
/permissions default         # manual：寫入與指令逐次詢問，唯讀自動允許
/permissions assisted        # assisted：由安全判斷模型自動核准它認為安全的請求
/permissions allow-all       # 全部自動核准（等同 /allow-all、/yolo）
```

| 模式 | 設定值（`defaultPermissionMode`） | 行為 | 適合 |
|------|------|------|------|
| Manual（預設） | `"manual"` | 寫入與指令詢問、唯讀自動允許 | 一般開發 |
| Assisted | `"assisted"` | **機率性**的 LLM 審查，判斷安全就自動核准，否則詢問；需要實驗性模式或 `enabledFeatureFlags.AUTO_APPROVAL`；`--assisted-approval` 旗標或 `COPILOT_ASSISTED_APPROVAL` | 降低重複詢問，但**不是安全邊界** |
| Allow-all | `"allow-all"` | 全部自動核准；政策禁用 bypass 時會被忽略 | 只在 Sandbox 或拋棄式環境 |

v1.0.96 起 timeline 會標示每個權限決策是由你、Assisted Permissions、政策或無人值守備援做出的，方便事後追查。

> ⚠️ 官方對 Assisted 模式的描述是「機率性的 LLM 審查……不是硬性的安全邊界，要可強制執行的限制請使用受管規則、Sandbox、最小權限憑證與對外連線控制」。

### 13.6 YOLO（allow-all）的風險矩陣

| 風險 | 情境 | 嚴重度 | 緩解 |
|------|------|------|------|
| 刪除或覆寫檔案 | 代理誤判清理範圍 | 高 | Sandbox 限制可寫路徑；先 commit；用 worktree |
| 推送或改寫歷史 | `git push --force`、`git reset --hard` | 高 | `--deny-tool='shell(git push)'`；分支保護 |
| 資料外流 | 提示注入誘導 `curl` 上傳檔案 | 高 | Sandbox 網路規則、受管 `limitTo`、`--deny-url` |
| 讀取密鑰 | 讀 `.env`、`~/.ssh`、雲端憑證 | 高 | Sandbox `deniedPaths`、受管 `Read(...)` deny 規則、`--secret-env-vars` |
| 安裝惡意套件 | 依賴幻覺（套件名稱被搶注） | 中 | 鎖定 registry、審查新增依賴 |
| 失控成本 | Autopilot＋`/fleet` 長時間執行 | 中 | `--max-ai-credits`、延續上限 |

企業應以受管設定禁止或限制 allow-all：

| `permissions.disableBypassPermissionsMode` | 效果 |
|------|------|
| `"disable"` | 啟動時壓制所有 allow-all 旗標（`--allow-all-tools`、`--allow-all-paths`、`--allow-all-urls`、`--allow-all`、`--yolo`），會顯示政策警告 |
| `"allow-auto-only"` | 禁止完全 allow-all，但允許 Assisted 模式 |
| 其他無法辨識的值 | 記錄錯誤並視為 `"disable"`（fail-closed） |

設定來源的持久性：使用者設定（機器層級，所有帳號）→ 伺服器受管設定（切換帳號會清除）→ MDM（裝置層級，帳號切換無法覆寫）。

### 13.7 其他保護機制

| 機制 | 說明 |
|------|------|
| 指令安全分析 | 執行前分析 `rm -rf`、`sudo`、`chmod 777`、以 `curl` 傳送敏感路徑、讀取 `.env`／SSH 金鑰等模式，高風險指令會額外警告 |
| 環境變數黑名單 | 禁止行內設定可被濫用的變數：`LD_*`、`DYLD_*`、`GIT_CONFIG_*`、`GIT_EXTERNAL_DIFF`、`GIT_PROXY_COMMAND`、`PATH`、`BASH_ENV`、`ENV`、`PAGER`、`GIT_SSH_COMMAND`、`GIT_ASKPASS`、`EDITOR` 等 |
| `web_fetch` SSRF 防護 | 只允許 http／https；封鎖 loopback、RFC 1918 私有網段與雲端中繼資料端點（如 169.254.169.254）；重新導向逐跳重新驗證，跨來源需核准。開發時要連本機文件伺服器可設 `COPILOT_WEB_FETCH_ALLOW_LOCALHOST=1` |
| UNC 路徑封鎖 | 封鎖網路路徑，避免透過 SMB 洩漏憑證 |
| `--secret-env-vars` | 從 shell 與 MCP 環境中移除指定變數的值，並在輸出中遮蔽；`GITHUB_TOKEN` 與 `COPILOT_GITHUB_TOKEN` 預設遮蔽 |
| 歷史漏洞 | CVE-2026-29783：v0.0.422 以前的唯讀指令判斷可被 bash 參數展開繞過，v0.0.423 修正。**保持升級**是權限模型有效的前提 |

### 13.8 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 權限規則 | `shell(git*)`、`write(src/**)` | `shell(git:*)`；`write` 搭配 Sandbox | `check_flags.py` 確認旗標存在；在拋棄式 Repo 互動測試規則 |
| 限制範圍的寫法 | 用 allow 規則縮小 allow-all | 用 deny 規則 | 檢查規則中是否有「allow-all＋allow」組合 |
| CI 權限 | `--allow-all` | 最小 `--allow-tool` 組合＋`--deny-tool` | 列出任務實際需要的工具，比對旗標 |
| 核准模式 | 以 Assisted 作為安全控制 | Assisted 只用來減少詢問；強制控制用受管規則與 Sandbox | 對照 13.5 節官方說明 |
| 禁用 YOLO | 只在文件中規定 | 受管設定 `disableBypassPermissionsMode` | 在測試機執行 `copilot --yolo`，確認被壓制並顯示警告 |
| 已儲存核准的清理 | 以為 `/permissions reset` 會清除「This location」 | 用 `/reset-allowed-tools` 或編輯 `permissions-config.json` | 清除後重新執行，確認再次詢問 |

---

## 第 14 章：Sandbox 與執行隔離

> **本章目標**
>
> - 理解本機 Sandbox（MXC）的保護範圍與**保護不到**的地方。
> - 能設定檔案系統、網路、憑證遮蔽與 bypass 政策，並用 `/sandbox policy` 驗證。
> - 知道何時改用雲端 Sandbox 或容器／VM。

### 14.1 為什麼需要 Sandbox

沒有 Sandbox 時，代理執行的 shell 指令擁有**與你的帳號完全相同的權限**：可以讀寫刪除你能存取的任何檔案、連到你的機器能連的任何網路、使用你環境中的所有憑證。權限規則（第 13 章）只是在執行前「看指令文字」做判斷；Sandbox 則是讓作業系統在**執行時**強制限制。

| 方案 | 隔離強度 | 成本 | 適合 |
|------|------|------|------|
| 無 Sandbox | 無 | — | 只在完全信任的 Repo、逐次核准時 |
| 本機 Sandbox（MXC） | 輕量的 OS 層級程序與檔案系統隔離 | 免費 | 日常開發，特別是使用 Autopilot 或 allow-all 時 |
| 雲端 Sandbox | 完全隔離的拋棄式 Linux 環境 | 依用量計費 | 不受信任的程式碼、需要平行大量任務、跨裝置接續 |
| 容器／VM | 依設定 | 自行維運 | 已有標準化開發環境的組織 |

### 14.2 本機 Sandbox

#### 14.2.1 啟用

```text
/sandbox enable        # 開啟（寫入 sandbox.enabled）
/sandbox status        # 是否啟用、是否只對本 Session 啟用
/sandbox policy        # 檢視實際生效的路徑、拒絕清單、網路狀態
/sandbox policy npm install    # 不執行指令，預覽該指令會獲得哪些開發工具存取
/sandbox               # 開啟設定對話框（Filesystem、Network、Credentials 分頁）
/sandbox disable       # 關閉
```

```bash
copilot --sandbox -p "執行測試並修正失敗" --allow-tool='shell(./mvnw:*)' --allow-tool=write   # 只對本次啟用
copilot init --sandbox
```

> 📝 `--sandbox`／`--no-sandbox` 在 v1.0.97 的 `copilot --help` 中沒有列出，但官方 command reference 有記載，本機實測也被接受（附錄 H.3）。

啟用時的預設政策：檔案系統限於工作目錄、PATH 目錄、暫存目錄與使用者設定檔目錄；允許對外連線；git 與 `gh` 透過遮蔽代理驗證；允許單一指令的 bypass。

#### 14.2.2 支援的作業系統

| 作業系統 | 後端 | 需求 |
|------|------|------|
| macOS | Seatbelt（`sandbox-exec`） | 建議 macOS 15 以上 |
| Linux | bubblewrap | `bwrap` 0.5.0+；允許對外連線時另需 `slirp4netns`、util-linux 2.35+ 的 `unshare`／`nsenter`、`iptables`／`ip6tables` 及其 restore 程式、`/dev/net/tun` 存取（建議 nf_tables 後端） |
| Windows | ProcessContainer＋BaseContainer | 支援 Sandbox 的近期 Windows 11 版本；拒絕路徑、localhost、Proxy 等功能依版本而定 |

主機不支援時：使用者的啟用偏好會在本 Session 被關閉並顯示通知（設定值不變）。若受管設定要求 Sandbox 且 `failIfUnavailable: true`，則**無法執行任何 shell 指令**，需由管理者部署前置條件。

#### 14.2.3 保護範圍與限制

| 項目 | 是否受 Sandbox 保護 |
|------|------|
| Shell 指令 | ✅ |
| 檔案搜尋工具 | ✅ |
| 本機 MCP、LSP 伺服器 | ✅（預設；`sandboxMcpServers`、`sandboxLspServers`） |
| Repo、使用者、plugin 的 command hooks | ✅（第 11 章） |
| **CLI 內建的檔案編輯工具** | ⚠️ 在 CLI 程序內執行，**OS Sandbox 看不到**；只是「盡力」套用相同政策 |
| 遠端（HTTP／SSE）MCP 伺服器 | ❌ 永遠不在 Sandbox 中 |
| Policy hooks | ❌ 一律在主機執行 |
| 背景（detached）指令 | ❌ 無法包裝；允許 bypass 時會先詢問，核准後**不在 Sandbox 中**執行 |
| 你環境中的其他憑證 | ⚠️ Sandbox 會繼承 shell 環境（除了固定黑名單），例如 `AWS_ACCESS_KEY_ID` 仍看得到，除非設定遮蔽 |

> ⚠️ 官方定位：本機 Sandbox 屬於隔離強度光譜中**較輕量**的一端（程序與檔案系統層級），不是 hypervisor 或容器等級的隔離。處理不受信任的程式碼請使用雲端 Sandbox 或 VM。

### 14.3 設定

設定存在使用者 `settings.json` 的 `sandbox` 鍵（**Repo 設定不能覆寫 Sandbox**），可在 `/sandbox` 對話框按 <kbd>Ctrl</kbd>+<kbd>E</kbd> 直接編輯。

#### 14.3.1 主要設定鍵

| 鍵 | 預設 | 說明 |
|------|------|------|
| `enabled` | `false` | 是否啟用 |
| `addCurrentWorkingDirectory` | 啟用時開啟 | 授予工作目錄讀寫權限 |
| `allowDevToolAccess` | `true` | 自動授予建置需要的開發工具位置：快取與工具鏈（讀取，含 `~/.npmrc`、`~/.m2/settings.xml` 等 registry 設定）、共用建置快取（讀寫）。依指令與工作目錄中的建置檔（`pom.xml`、`package.json`…）**逐指令**授予；`~/.ssh` 等憑證儲存永遠排除 |
| `allowBypass` | `true` | 允許單一指令要求跳出 Sandbox（會顯示核准提示） |
| `auth.git`／`auth.gh` | `true` | 透過遮蔽代理讓 git／`gh` 驗證，子程序拿不到真實憑證（舊鍵 `gitAuth`／`ghAuth` 已失效且不會自動遷移） |
| `credentials.envVars` | — | 其他要遮蔽的環境變數與允許注入的主機 |
| `sandboxMcpServers`／`sandboxLspServers` | 啟用 | 本機 MCP／LSP 伺服器也在 Sandbox 中執行 |
| `userPolicy.filesystem.readwritePaths`／`readonlyPaths`／`deniedPaths` | — | 額外的讀寫、唯讀、拒絕路徑 |
| `userPolicy.network.allowOutbound` | 允許 | 是否允許對外連線 |
| `userPolicy.network.allowLocalNetwork` | `false` | 是否允許區域網路（Windows 使用本機代理、Proxy 或主機規則時必須開啟） |
| `userPolicy.network.allowedHosts`／`blockedHosts` | — | 主機白名單／黑名單；`*.example.com` 符合子網域；blocked 優先 |
| `userPolicy.network.proxy` | — | 上游 HTTP(S) Proxy（`url`、`username`、`password`；密碼存在 OS 憑證庫） |
| `userPolicy.seatbelt.keychainAccess` | `false` | macOS：是否可存取系統鑰匙圈（只能在 settings.json 設定） |

#### 14.3.2 範例：開發者的使用者設定

```json
{
  "model": "auto",
  "autoTier": "balance",
  "theme": "github",
  "autoUpdatesChannel": "stable",
  "askUser": true,
  "defaultMode": "interactive",
  "defaultPermissionMode": "manual",
  "allowedUrls": ["github.com", "docs.github.com", "*.maven.apache.org"],
  "deniedUrls": ["pastebin.com"],
  "footer": {
    "showQuota": true,
    "showAiUsed": true,
    "showSandbox": true
  },
  "sandbox": {
    "enabled": true,
    "allowBypass": true,
    "auth": { "git": true, "gh": true },
    "userPolicy": {
      "filesystem": { "deniedPaths": ["~/.aws", "~/.kube"] },
      "network": { "allowLocalNetwork": false }
    }
  },
  "worktreeBaseRef": "defaultBranch"
}
```

這份設定的意圖：以 Auto 模型與 Manual 核准為預設；啟用 Sandbox 並拒絕存取 `~/.aws`、`~/.kube`；禁止區域網路（避免代理連到內部服務）；新 worktree 從遠端預設分支建立。

> ⚠️ `deniedPaths` 中不存在的路徑與其上層目錄會在啟動前被**建立為目錄**，而且不會自動移除（即使名稱是 `.env`）。Windows 不支援拒絕路徑時，指令會直接失敗而不是以較弱的限制執行。

#### 14.3.3 憑證遮蔽

```json
{
  "sandbox": {
    "enabled": true,
    "credentials": {
      "envVars": {
        "ARTIFACTORY_TOKEN": { "injectHosts": ["artifactory.corp.example.com"] }
      }
    }
  }
}
```

運作方式：啟動 Sandbox 子程序前，CLI 把指定變數換成每次啟動隨機產生的假值；本機代理驗證目的地的 TLS 憑證後，**只在送往核准主機的 HTTPS 標頭中**換回真實值。限制：純 HTTP、網址與請求本體不會替換；會對值做編碼或簽章、要求 HTTP/2、釘選憑證或使用用戶端憑證的工具可能無法運作；檔案中的密鑰不受保護；核准的 bypass 會跳過遮蔽。

HTTPS 攔截需要信任代理的 CA。CLI 會透過 `SSL_CERT_FILE`、`NODE_EXTRA_CA_CERTS`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`、`GIT_SSL_CAINFO` 提供憑證包，多數工具不需要額外設定；需要時可安裝到 OS 信任：

```bash
copilot sandbox ca status     # 0=已信任 1=讀取失敗 3=未信任 4=平台不支援 5=需先 rotate
copilot sandbox ca create     # 以執行 Copilot 的使用者身分建立（不要用系統管理員）
copilot sandbox ca trust      # 加入 OS 信任（Windows 需系統管理員核准，寫入本機電腦根憑證存放區）
copilot sandbox ca rotate     # 新增憑證注入主機後需 rotate
copilot sandbox ca remove
```

> ⚠️ CA 私鑰存在 Copilot 設定目錄中，**任何你執行的程式都讀得到**，要像密碼一樣保護 `~/.copilot`。Windows 上安裝的是整台電腦信任的根憑證。

### 14.4 Bypass（跳出 Sandbox）

| 情況 | 行為 |
|------|------|
| 同步指令被檔案或網路政策擋住，且 `allowBypass` 為 `true` | 提示是否在 Sandbox 外重新執行；選項包含「Yes, and disable the sandbox for the rest of this session」 |
| Windows 支援拒絕擷取的版本 | 先以「記錄不阻擋」重跑（網路政策仍有效），仍被擋才提供完整 bypass，只詢問一次 |
| `permissionRequest` hook 回傳 allow | **不會**預先核准 bypass，一定要使用者互動確認 |
| 受管設定 `allowBypass: false` | 不提供 bypass、`/sandbox disable` 被拒絕 |

> ✅ Autopilot＋Sandbox 時，任何需要跳出 Sandbox 的步驟都會被拒絕，這是預期行為：代理會在 Sandbox 能做到的範圍內完成工作。

### 14.5 企業強制 Sandbox

受管設定（MDM、`managed-settings.json` 或伺服器端）的 `sandbox` 值是**下限**：

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowBypass": false,
    "sandboxMcpServers": true
  }
}
```

| 受管設定 | 效果 |
|------|------|
| `enabled: true` | 使用者的 `--no-sandbox` 與 `sandbox.enabled: false` 無效；CLI 會顯示是政策強制 |
| `allowBypass: true`（只設 `enabled` 時的預設） | 使用者仍可 `/sandbox disable` 關閉**本 Session**（不會保存） |
| `allowBypass: false` | Sandbox 強制，無法關閉 |
| `failIfUnavailable: true` | 無法建立 Sandbox 時封鎖模型與工具執行，而不是退回無 Sandbox |
| `learningMode: "allow"` | 只能透過 Windows 原生 MDM（Intune、登錄檔）設定：記錄存取但允許，用來觀察團隊實際需要哪些路徑 |
| 受管政策無法讀取 | fail-closed，以最嚴格層級強制 Sandbox |

### 14.6 雲端 Sandbox

```bash
copilot --cloud --experimental     # 在 GitHub 代管的隔離 Linux 環境啟動互動式 Session
```

| 特性 | 說明 |
|------|------|
| 狀態 | 公開預覽、實驗性功能 |
| 基礎 | Azure Container Apps Sandboxes，GitHub 提供身分、政策與計費 |
| 限制 | 只支援互動式；**不能**與 `-p` 或 `-i` 並用；每次都要加 `--cloud` |
| 治理 | 政策沿用 Copilot cloud agent 的設定（例如防火牆規則）；組織方案預設**停用**，需管理者開啟 |
| 計費 | 依用量計費 |
| 好處 | 不影響本機、可跨裝置接續、可平行執行多個任務 |

開始對話前，也可以在空白輸入框按 <kbd>Ctrl</kbd>+<kbd>E</kbd> 選擇在本機或雲端環境執行。

### 14.7 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| Sandbox 設定位置 | 寫在 `.github/copilot/settings.json` | 使用者設定或受管設定 | `check_config.py repo-settings` 會標出 Repo 中的 `sandbox` |
| 舊設定鍵 | `sandbox.gitAuth`、`allowDevToolCaches` | `sandbox.auth.git`、`allowDevToolAccess` | `check_config.py user-settings` 會指出改名的鍵 |
| 保護範圍說明 | 「啟用 Sandbox 後所有檔案操作都受 OS 保護」 | 說明內建檔案工具、遠端 MCP、背景指令、policy hooks 的例外 | 對照 14.2.3 節表格 |
| 憑證保護 | 只啟用 Sandbox 就以為雲端憑證安全 | `credentials.envVars` 遮蔽或 `deniedPaths` 封鎖憑證目錄 | 在 Sandbox 中執行 `env \| grep AWS`、`cat ~/.aws/credentials`，確認被遮蔽或拒絕 |
| 實際生效政策 | 只看設定檔 | 以 `/sandbox policy` 確認 | 在 Session 中執行 `/sandbox policy` 並截圖存證 |
| 企業強制 | 只設 `enabled: true` 卻以為無法關閉 | 需要時同時設 `allowBypass: false` | 測試機上執行 `/sandbox disable`，確認被拒絕 |
| 雲端 Sandbox 用於 CI | `copilot --cloud -p ...` | 雲端 Sandbox 只支援互動式；CI 用 Actions Runner | `check_flags.py`；實際執行會被拒絕 |

---

## 第 15 章：企業治理與稽核

> **本章目標**
>
> - 能用 MDM／伺服器受管設定建立公司層級的 Copilot CLI 政策基線。
> - 理解受管權限規則、網域邊界 `limitTo` 與 MCP allow／deny 的合併語意。
> - 建立可稽核的證據鏈，並掌握目前已知的風險與業界研究。

### 15.1 受管設定的來源

| 平台 | 類型 | 位置 |
|------|------|------|
| macOS | MDM plist | `com.github.copilot` |
| macOS | 檔案 | `/Library/Application Support/GitHubCopilot/managed-settings.json` |
| Windows | MDM 登錄檔 | `HKLM\SOFTWARE\Policies\GitHubCopilot` |
| Windows | 檔案 | `%ProgramFiles%\GitHubCopilot\managed-settings.json` |
| Linux | 檔案 | `/etc/github-copilot/managed-settings.json` |
| 伺服器 | 組織／企業推送 | 登入後取得 |

規則：

- POSIX 上的檔案若是 symlink、不屬於 root 或其他人可寫，會被拒絕。
- MDM 與伺服器設定**逐鍵合併**：MDM 有設定的鍵以 MDM 為準，其餘由伺服器補上。
- 受管設定套用到所有執行模式：互動式、`-p`、`--acp`、`--ahp-host`、`--server`（v1.0.88 起），無法透過換一種啟動方式繞過。
- 長時間執行的 Session **每小時重新取得並套用**受管設定。
- 帳號登出會清除該帳號快取的受管設定；`forceRemoteSettingsRefresh: true` 時啟動必須取得最新政策，失敗則以「政策未確定」的嚴格模式運作（封鎖非預設 MCP、禁止 bypass、禁止受政策管制的 plugin 安裝）。

### 15.2 受管設定支援的鍵

| 鍵 | 用途 |
|------|------|
| `model`（＋`effortLevel`、`contextTier`） | 預設模型（可被 `--model` 或恢復的 Session 覆寫） |
| `autoTier` | Auto 路由層級；字串為強制鎖定，`{"overridable": "balance"}` 為可覆寫的預設 |
| `permissions` | `disableBypassPermissionsMode`、`deny`／`ask`／`allow` 規則、`limitTo` 網域邊界 |
| `allowedMcpServers`／`deniedMcpServers` | MCP 伺服器白名單／黑名單 |
| `enabledPlugins`、`extraKnownMarketplaces`、`strictKnownMarketplaces` | Plugin 與 marketplace 管控 |
| `forceLoginOrgs` | 只允許屬於指定組織的帳號登入；個人帳號、其他企業帳號與 BYOK／API key 驗證會被拒絕 |
| `forceRemoteSettingsRefresh` | 強制啟動時取得最新伺服器政策 |
| `remoteControl` | `mode`：`enabled`、`disabled`、`requireSSO`（需搭配 `githubDotComOrganizations`） |
| `sandbox` | Sandbox 下限（第 14 章） |
| `shellShortcut` | 強制開啟或關閉 `$` 互動式 shell 捷徑 |
| `telemetry` | OpenTelemetry 基線：`enabled`、`endpoint`、`protocol`、`headers`、`resourceAttributes`、`captureContent`、`lockCaptureContent`、`serviceName` |
| `policyHelper` | 註冊提供最低優先層受管設定的執行檔；**目前會驗證但尚未實際執行**（未來版本提供） |

#### 15.2.1 範例：企業基線

```json
{
  "model": "auto",
  "autoTier": { "overridable": "balance" },
  "forceLoginOrgs": ["acme-corp"],
  "permissions": {
    "disableBypassPermissionsMode": "allow-auto-only",
    "deny": [
      "Shell(git push --force *)",
      "Shell(rm -rf /*)",
      "Read(~/.ssh/**)",
      "Domain(*.pastebin.com)"
    ],
    "ask": ["Shell(git push *)", "Shell(npm publish *)"],
    "limitTo": ["github.com", "*.github.com", "*.githubusercontent.com", "registry.npmjs.org", "repo.maven.apache.org"]
  },
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.docs.example.com/*" },
    { "serverCommand": ["npx", "-y", "@playwright/mcp@0.0.41"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" }
  ],
  "sandbox": {
    "enabled": true,
    "allowBypass": true,
    "sandboxMcpServers": true
  },
  "remoteControl": {
    "mode": "requireSSO",
    "githubDotComOrganizations": ["acme-corp"]
  }
}
```

這份基線的意圖：

| 設定 | 意圖 |
|------|------|
| `autoTier: {"overridable": "balance"}` | 預設平衡成本與能力，但允許團隊調整 |
| `forceLoginOrgs` | 只能用公司組織帳號，同時封鎖個人 BYOK |
| `disableBypassPermissionsMode: "allow-auto-only"` | 禁止 YOLO，但允許 Assisted 模式減少詢問 |
| `deny` 規則 | 強制禁止 force push、刪除根目錄、讀 SSH 金鑰、連 pastebin |
| `ask` 規則 | `git push`、`npm publish` 一律詢問 |
| `limitTo` | 代理的網路請求只能到 GitHub、npm 與 Maven Central |
| MCP allow／deny | 只允許核准的兩個 MCP 伺服器 |
| `sandbox` | 強制 Sandbox，但允許單一指令 bypass（由使用者確認） |
| `remoteControl: requireSSO` | 遠端控制需要組織 SSO |

### 15.3 受管權限規則

| 規則家族 | 比對對象 | 寫法 |
|------|------|------|
| `Bash(...)`、`Shell(...)` | shell 指令 | `git push *` 比對字首，否則完全比對 |
| `PowerShell(...)` | PowerShell 指令 | 同上 |
| `Read(...)` | 讀取路徑 | 支援 glob；`/` 為工作區根目錄、`~/` 為家目錄、`./` 為目前目錄 |
| `Edit(...)`、`Write(...)` | 寫入路徑 | 同 `Read`；**也涵蓋 shell 的輸出重新導向**（`>`、`>>`、`&>` 等）與 `sed -i` |
| `Domain(...)` | 網址主機 | 同網址規則 |

合併語意（多個受管來源時）：

1. **deny 永遠優先**，其次 ask，最後 allow。
2. deny 與 ask 跨來源**聯集**；allow 跨來源**交集**（每個有宣告 allow 的來源都必須允許）。
3. 只要設定了 deny／ask／allow 任一個，不符合任何規則的操作**預設為 ask**。

#### 15.3.1 網域邊界 `limitTo`

`limitTo` 是**封閉世界**的網域白名單：清單外的網路請求一律拒絕、不詢問，使用者規則、已儲存的核准與 allow-all 都無法放寬。shell 指令中偵測到的網址也必須符合。注意事項：

- 只接受 `Domain` 形式的項目；空清單代表禁止所有網域；無效的清單會被當成空清單（並回報設定錯誤）。
- deny 仍優先於 `limitTo`；ask 與 allow 只在邊界內進一步細分。
- `limitTo` 不限制 shell、讀、寫操作本身，只限制網路目的地；而網址偵測是啟發式的，**要可靠的網路隔離仍需 Sandbox 網路規則或防火牆**。

### 15.4 MCP 伺服器管控

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.docs.example.com/*" },
    { "serverCommand": ["npx", "-y", "@playwright/mcp@0.0.41"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" }
  ]
}
```

| 規則 | 說明 |
|------|------|
| 每筆只能用一種比對 | `serverUrl`（遠端，支援 `*`）、`serverCommand`（本機，指令與參數完全依序比對）、`serverName` |
| 首方伺服器 | 內建 GitHub MCP 等首方伺服器永遠豁免 |
| 未設定 allowlist | 允許所有非預設伺服器；**空陣列 = 全部禁止** |
| deny 優先 | 符合 deny 就封鎖，即使也符合 allow |
| 比對來源 | 遠端伺服器必須由 `serverUrl` 比對（沒有任何 `serverUrl` 項目時才看 `serverName`）；本機伺服器同理看 `serverCommand` |
| 啟動時序 | v1.0.83 起，非預設伺服器會等受管設定取得後才啟動，避免競態 |

這與組織層級的**企業 MCP allowlist**（依指紋向企業端點評估，fail-closed）是兩套獨立機制，可以並用。

### 15.5 Policy hooks 與內容排除

| 機制 | 說明 |
|------|------|
| Policy hooks | 管理者部署在 `policy.d/` 的 hooks，不受 `disableAllHooks` 影響、不需資料夾信任，適合強制稽核與攔截（第 11 章） |
| `allowManagedHooksOnly` | 只允許受管 hooks，連 extension 註冊的工具回呼也一併封鎖 |
| Content exclusion | 企業、組織、Repo 層級設定的內容排除會套用到 CLI，被排除的檔案不會作為 context |

> 📝 **v1 手冊更正**：舊版引用第三方分析稱「Content Exclusions 不涵蓋 Copilot CLI」。目前官方〈About Copilot CLI〉與〈Administering Copilot CLI〉文件都明載 Business／Enterprise 的內容排除政策**會套用到 CLI**。但內容排除只影響「作為 context」，不等於代理無法用 shell 指令讀取該檔案；機敏檔案仍應以 Sandbox `deniedPaths` 或受管 `Read(...)` deny 規則保護，並實測確認。

### 15.6 已知風險與業界研究

| 風險 | 說明 | 狀態與對策 |
|------|------|------|
| 唯讀指令判斷繞過（CVE-2026-29783） | v0.0.422 以前，shell 工具的「唯讀指令」分類可被 bash 參數展開繞過，搭配提示注入（README、程式註解、Issue、MCP 回應）可執行任意程式；CVSS v4 7.5 | v0.0.423 修正。**維持升級**，並以 Sandbox 作為第二道防線 |
| 透過 README 的提示注入下載並執行惡意程式 | PromptArmor 研究展示：clone 的 Repo 中藏在 README 的注入，可在首次查詢後下載並執行外部程式；GitHub 當時回應為已知問題 | 不受信任的 Repo 不使用 allow-all、啟用 Sandbox 與網路限制 |
| 資料夾信任後自動啟動 MCP（TrustFall 類） | Adversa AI 指出多個代理式 CLI 在使用者接受資料夾信任後，會自動啟動 Repo 定義的 MCP 伺服器 | 信任前檢查 `.mcp.json`、`.github/mcp.json`、`.github/hooks/`；受管 MCP allowlist |
| 密鑰外洩 | 代理可能讀取 `.env` 或在輸出中帶出憑證；Adversa AI 另報告在 Autopilot 下依模型而異的密鑰洩漏風險 | `deniedPaths`、受管 `Read` deny、憑證遮蔽、`--secret-env-vars`、提交前密鑰掃描 |
| 依賴幻覺 | 代理建議安裝不存在或被搶注的套件 | 內部 registry、審查新增依賴、SCA 掃描 |
| 自動化中的提示注入 | Fork 送來的 PR 內容進入 CI 中的代理 | 不在 fork PR 上執行、最小權限、優先使用 GitHub Agentic Workflows |

> 📝 上表研究的發佈日期與修補狀態以各原始報告為準（見附錄 H.1）；業界研究會持續更新，資安團隊應定期追蹤，而不是把這張表當成一次性清單。

### 15.7 稽核證據鏈

| 證據 | 來源 | 保存建議 |
|------|------|------|
| 政策變更 | Enterprise audit log（影響 CLI 的政策變更） | 依公司稽核政策 |
| 工具使用中繼資料 | `postToolUse` policy hook 寫入集中式日誌 | 只存中繼資料，遮蔽參數 |
| 權限決策 | Timeline 標示決策來源（v1.0.96）；`events.jsonl` | Session 資料視為機敏資料 |
| 模型用量與成本 | `/usage`、`--usage-output-file`、帳單與用量儀表板 | 依 cost center 彙整 |
| 遙測 | OpenTelemetry traces／metrics | 預設不擷取內容 |
| 程式變更歸屬 | commit 的 `Co-authored-by` trailer（`includeCoAuthoredBy`）、PR 作者 | 保留在 Git 歷史 |
| CI 執行紀錄 | Actions log、`--output-format json` 的 JSONL、`--share` 匯出 | 以 artifact 保存，設定保留天數 |

### 15.8 治理成熟度檢核

| 等級 | 特徵 |
|------|------|
| L1 放任 | 個人自行安裝與設定，沒有政策 |
| L2 規範 | 有使用規範與 Repo 指引，但沒有強制機制 |
| L3 強制 | 受管設定禁止 YOLO、強制 Sandbox、MCP allowlist；Repo 有安全 hooks |
| L4 可稽核 | Policy hooks＋集中式日誌、OTel、用量與成本報表、季度政策檢討 |
| L5 持續改善 | 依稽核數據調整政策（例如 Sandbox learningMode 收集需求），版本升級有回歸測試 |

### 15.9 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| `managed-settings.json` | 使用不支援的鍵、規則格式錯誤 | 依 15.2 節鍵名，規則用 `Shell(...)` 等家族 | `python check_config.py managed-settings managed-settings.json` |
| MCP 管控 | 一筆同時寫 `serverUrl` 與 `serverName` | 每筆只用一種比對 | checker 會檢查；測試機上啟動未核准伺服器應被封鎖 |
| `limitTo` | 寫成 `https://github.com/` | 只寫網域，例如 `github.com`、`*.github.com` | checker 會標出含協定或路徑的項目 |
| Linux 部署 | 檔案權限 664 或用 symlink | root 擁有、不可被其他人寫入、實體檔案 | `stat /etc/github-copilot/managed-settings.json` |
| 內容排除說明 | 「設定內容排除就代表代理讀不到檔案」 | 內容排除只影響 context；另以 Sandbox／Read deny 保護 | 在測試 Repo 讓代理 `cat` 被排除的檔案，觀察結果 |
| 風險評估 | 引用無法查證的統計數字 | 引用可查證的 CVE 與原始研究，註明日期 | 逐一開啟附錄 H.1 的來源連結 |

---

## 第 16 章：程式化介面、Headless 與 CI/CD

> **本章目標**
>
> - 正確使用 `-p` 程式化模式：最小權限、穩定輸出、可重現。
> - 在 GitHub Actions 中以 `GITHUB_TOKEN` 或 PAT 安全地執行 Copilot CLI。
> - 知道程式化模式與互動模式在信任、MCP、hooks、Memory 上的差異。

### 16.1 程式化模式基礎

```bash
copilot -p "說明 src/main/java/com/acme/order/OrderService.java 的責任" -s
echo "列出這個 Repo 的建置指令" | copilot -s        # 也可以用管線送入（有 -p 時會忽略管線內容）
```

| 選項 | 用途 |
|------|------|
| `-p`／`--prompt` | 執行一次後結束；結束摘要會附 `copilot --resume=<ID>` 提示 |
| `-s`／`--silent` | 只輸出代理的回應，不含統計資訊，方便擷取 |
| `--output-format json` | 輸出 JSONL（每行一個 JSON 事件），方便程式解析；密鑰會被安全遮蔽（v1.0.97） |
| `--no-ask-user` | 不讓代理提問（沒有人可以回答） |
| `--model` | 固定模型，讓不同環境行為一致 |
| `--allow-tool`／`--deny-tool`／`--available-tools` | 最小權限；**程式化模式無法顯示核准對話框，未預先允許的動作會被自動拒絕** |
| `--max-ai-credits N` | 成本上限（最少 30） |
| `--attachment 路徑` | 附加圖片或文件（只限程式化模式） |
| `--share=路徑`／`--share-gist` | 結束後匯出紀錄 |
| `--usage-output-file 路徑` | 寫出最終用量統計 JSON（含每個代理的用量） |
| `--autopilot`＋`--max-autopilot-continues N` | 程式化 Autopilot |
| `--fleet` | 平行子代理 |
| `--enable-memory` | 程式化模式預設**關閉** Memory |

`-p` 預設最多等待背景代理或 shell 600 秒才結束（`COPILOT_TASK_WAIT_TIMEOUT_SECONDS`）。

### 16.2 程式化模式的信任差異

程式化模式無法顯示資料夾信任提示，因此：

| 項目 | 資料夾已受信任 | 未受信任（預設） | 強制載入的環境變數 |
|------|------|------|------|
| 工作區 MCP（`.mcp.json` 等） | 載入 | 略過 | `GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP=true` |
| Repo hooks | 載入 | 略過 | `GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS=true` 或 `COPILOT_ALLOW_ALL` |
| 專案 extensions | 載入 | 略過 | `GITHUB_COPILOT_PROMPT_MODE_EXTENSIONS=true` |

> ⚠️ `COPILOT_ALLOW_ALL` 只有設為**精確的 `true`** 時才會同時信任工作目錄（載入該目錄的 skills、plugins、MCP 與 hooks，包括會執行 shell 的 hooks）；`1`、`yes`、`on`、`y` 只自動核准工具，不信任目錄（v1.0.85 起）。在 CI 中設定這個變數前，要確認 Repo 內容是受信任的。

### 16.3 常用腳本模式

```bash
# 產生 commit 訊息（只允許 git 指令）
copilot -p '依照 Conventional Commits，為已 stage 的變更寫 commit 訊息，只輸出訊息本身' -s \
  --allow-tool='shell(git:*)'

# 擷取到變數
node_version=$(copilot -p '這個專案要求的 Node.js 版本？只回答版本號，不要其他文字。' -s)
echo "需要 Node.js $node_version"

# 審查分支（使用 /review 子代理）
copilot -p '/review 與 main 比較本分支的變更，只回報 bug 與安全問題' -s --allow-tool='shell(git:*)'

# 限制花費並保存紀錄
copilot -p '稽核 package.json 的依賴並整理成表格' -s \
  --allow-tool='shell(npm audit:*)' --max-ai-credits 100 --share=./audit-session.md
```

> ⚠️ **不要用自然語言的輸出做為 CI 的通過條件**。例如「回答 YES 或 NO」再用 `grep` 判斷，模型可能回答「No errors found, YES」。CI 的通過與否要由**確定性工具**（測試、lint、編譯）決定；代理的輸出只作為報告或建議。

#### 16.3.1 解析 JSONL 輸出

```bash
copilot -p "摘要最近 10 個 commit" -s --allow-tool='shell(git log:*)' \
  --output-format json > events.jsonl
jq -r '.type' events.jsonl | sort | uniq -c     # 先盤點事件類型，再依需要擷取
```

事件結構可能隨版本變動，解析程式應容忍未知欄位，並在升級 CLI 時回歸測試（第 18 章）。

### 16.4 GitHub Actions

#### 16.4.1 兩種驗證方式

| 方式 | 計費對象 | 前提 | 建議 |
|------|------|------|------|
| `GITHUB_TOKEN` | 個人 Repo：Repo 擁有者的座位；組織 Repo：**直接計入組織** | workflow 要有 `copilot-requests: write` 權限；組織需開啟「Allow use of Copilot CLI billed to the organization」政策（啟用 CLI 的組織預設開啟） | **組織 Repo 推薦**：短效、範圍受限，不必保存長效憑證 |
| PAT（`COPILOT_GITHUB_TOKEN`） | 發行 PAT 的使用者座位 | fine-grained PAT＋Copilot Requests 權限，存成 Actions secret | 政策未開啟、或要計入特定服務帳號時 |

以 `GITHUB_TOKEN` 計入組織時，使用者層級的預算不適用，要用 **cost center 預算**控制花費。

#### 16.4.2 範例：PR 變更摘要（`GITHUB_TOKEN`）

```yaml
name: Copilot PR summary

on:
  pull_request:
    types: [opened, synchronize]

# 最小權限：只讀程式碼、可發 Copilot 請求、可寫 PR 留言
permissions:
  contents: read
  copilot-requests: write
  pull-requests: write

concurrency:
  group: copilot-summary-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  summarize:
    # 不在 fork 送來的 PR 上執行，降低提示注入風險
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v7
        with:
          node-version: 22

      - name: Install Copilot CLI (pinned)
        run: npm install -g @github/copilot@1.0.97

      - name: Summarize changes
        env:
          GITHUB_TOKEN: ${{ github.token }}
          COPILOT_AUTO_UPDATE: "false"
          BASE_REF: ${{ github.event.pull_request.base.ref }}
        run: |
          copilot -p "用繁體中文摘要 origin/${BASE_REF}...HEAD 的變更：列出修改的模組、可能的風險與需要人工特別審查的檔案。只輸出 Markdown。" \
            --model claude-sonnet-5.5 \
            --allow-tool='shell(git diff:*)' --allow-tool='shell(git log:*)' \
            --deny-tool='shell(git push)' \
            --no-ask-user --max-ai-credits 200 -s > summary.md

      - name: Post summary as PR comment
        env:
          GH_TOKEN: ${{ github.token }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: gh pr comment "$PR_NUMBER" --body-file summary.md
```

| 設計 | 目的 |
|------|------|
| `permissions` 最小化並明確列出 `copilot-requests: write` | 沒有這個權限無法發出 Copilot 請求 |
| `if: ...head.repo.full_name == github.repository` | 不在 fork PR 上執行，降低提示注入風險 |
| `npm install -g @github/copilot@1.0.97`＋`COPILOT_AUTO_UPDATE=false` | 固定版本、可重現（CI 中自動更新預設關閉，這裡明確宣告） |
| 只允許 `git diff`、`git log`，並 deny `git push` | 最小權限 |
| `--no-ask-user`、`--max-ai-credits 200`、`timeout-minutes` | 不會卡住、不會失控 |
| 以 `gh pr comment` 張貼 | 代理只產生文字，寫入 GitHub 由確定性的步驟完成 |

#### 16.4.3 範例：排程報告（PAT）

```yaml
name: Copilot nightly report

on:
  workflow_dispatch:
  schedule:
    - cron: "30 17 * * 1-5"   # 週一到週五 UTC 17:30（台北 01:30）

permissions:
  contents: read

jobs:
  report:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v7
        with:
          node-version: 22

      - run: npm install -g @github/copilot@1.0.97

      - name: Generate report (PAT billed to a service account seat)
        env:
          COPILOT_GITHUB_TOKEN: ${{ secrets.COPILOT_PAT }}
          COPILOT_AUTO_UPDATE: "false"
        run: |
          copilot -p "整理過去 24 小時 main 分支的 commit，依模組分類，寫入 report.md" \
            --allow-tool='shell(git log:*)' --allow-tool='write(report.md)' \
            --no-ask-user --output-format json --usage-output-file usage.json > events.jsonl
          cat report.md >> "$GITHUB_STEP_SUMMARY"

      - uses: actions/upload-artifact@v5
        with:
          name: copilot-run-${{ github.run_id }}
          path: |
            report.md
            events.jsonl
            usage.json
          retention-days: 30
```

`--output-format json` 與 `--usage-output-file` 的輸出以 artifact 保存，作為稽核證據。

> 📝 actionlint 1.7.12（2026-10 最新版）尚未認得 `copilot-requests` 權限範圍，會誤報「unknown permission scope」；以 `actionlint -ignore 'unknown permission scope "copilot-requests"'` 排除即可（附錄 H.3）。

#### 16.4.4 官方推薦：GitHub Agentic Workflows

GitHub 官方對大多數自動化情境更推薦 [GitHub Agentic Workflows](https://github.com/github/gh-aw)（`gh-aw`），而不是在 `run` 步驟直接呼叫 `copilot`：它預設使用 `GITHUB_TOKEN`，並內建適合自動化的防護。直接呼叫 CLI 會讓它取得 workflow 環境的廣泛存取權，**fork 送來的 PR 觸發的 workflow 風險特別高**。

### 16.5 動態 workflow：`copilot workflow run`

已註冊的動態 workflow 可以不經主代理直接執行：

```bash
copilot workflow run release-notes --args '{"tag":"v2.3.0"}' --silent --output-format json
copilot workflow run release-notes --args @input.json --result-file result.json
```

| 結束碼 | 意義 |
|------|------|
| 0 | 完成，且要求的結果檔已成功寫入 |
| 1 | 未完成（暫停、達到上限、取消、失敗）或一般指令錯誤 |
| 2 | 找不到 workflow，或參數無法讀取、解析或驗證 |
| 130 | 被 SIGINT／SIGTERM 中斷 |

`workflow run` 不顯示核准提示，也不支援 `-p`、`-i`、`--agent`、`--fleet`、`--autopilot`、`--resume`。**先檢查結束碼再讀結果檔**：失敗時舊的結果檔可能還在。互動式介面可用 `/workflows` 觀察執行狀況（需要 token 計費方案）。

### 16.6 本機 CI 前置檢查腳本範例

把「AI 審查」放進開發者推送前的流程，但通過與否仍由確定性工具決定：

```bash
#!/usr/bin/env bash
# scripts/pre-push-review.sh：推送前先跑測試，再請 Copilot 產生審查報告（報告僅供參考）
set -euo pipefail

./mvnw -q verify                      # 確定性的關卡：失敗就停止

base="${1:-origin/main}"
report="target/copilot-review-$(date +%Y%m%d-%H%M%S).md"
mkdir -p target

copilot -p "/review 比較 ${base}...HEAD 的變更，只回報 bug、安全問題與遺漏的測試，以 Markdown 表格輸出" \
  -s --allow-tool='shell(git:*)' --deny-tool='shell(git push)' \
  --no-ask-user --max-ai-credits 150 > "$report"

echo "審查報告：$report（請人工閱讀後再推送）"
```

### 16.7 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| Workflow 權限 | 缺 `copilot-requests: write`，或給 `contents: write` 等過多權限 | 最小權限並明確列出 `copilot-requests: write` | actionlint（排除已知誤報）；人工檢查 `permissions` |
| 觸發條件 | `pull_request_target` 或 fork PR 也執行 | 排除 fork PR；優先考慮 gh-aw | 檢查 `on:` 與 `if:` |
| CLI 版本 | `npm install -g @github/copilot`（未固定） | 固定版本並關閉自動更新 | 檢查安裝步驟 |
| 工具權限 | `--allow-all` 或 `--yolo` | 任務所需的最小 `--allow-tool` | `check_flags.py`；列出任務實際需要的指令 |
| 通過條件 | 以模型回答 YES／NO 決定 CI 成敗 | 由測試、lint、編譯決定 | 檢查失敗條件是否來自確定性工具 |
| 憑證 | Classic PAT、PAT 寫在 workflow 中 | `GITHUB_TOKEN` 或 secret 中的 fine-grained PAT | 檢查 `env:` 來源 |
| `COPILOT_ALLOW_ALL` | 在處理外部貢獻的 workflow 設成 `true` | 只在受信任內容上使用，並了解它會信任目錄 | 對照 16.2 節 |
| 稽核證據 | 只看 Actions log | 保存 JSONL、用量 JSON 與報告為 artifact | 檢查 `upload-artifact` 與保留天數 |

---

## 第 17 章：計費與成本管理

> **本章目標**
>
> - 理解 AI Credits 的計算方式，能估算一次任務大約花多少。
> - 知道各方案的內含額度、超額處理與預算控制。
> - 能用 Session 上限、模型選擇與 context 管理控制成本。

> 📝 本章價格與額度為 **2026-10-14 查證**的官方文件內容，GitHub 會調整模型價格與內含額度，導入時請以[官方定價頁](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)為準。

### 17.1 AI Credits 的計算方式

自 2026-06 起，Copilot 全面採用用量計費：每次互動消耗的 token（輸入、輸出、快取）依模型單價計算，再換算成 AI Credits。

```text
費用（美元）= 輸入 token × 輸入單價 + 快取輸入 token × 快取單價 + 快取寫入 token × 寫入單價 + 輸出 token × 輸出單價
AI Credits  = 費用 ÷ 0.01        （1 AI Credit = US$0.01）
```

**估算範例**：一個中型修 Bug 任務，累計送出 20 萬輸入 token、產生 2 萬輸出 token：

| 模型 | 輸入（每百萬） | 輸出（每百萬） | 估算費用 | AI Credits |
|------|------|------|------|------|
| Claude Haiku 5.5（≤100K 層級） | $0.10 | $0.50 | 0.2×0.10＋0.02×0.50＝$0.03 | 約 3 |
| Claude Sonnet 5.5 | $2.00 | $10.00 | 0.2×2＋0.02×10＝$0.60 | 約 60 |
| GPT-5.4（≤272K 層級） | $2.50 | $15.00 | 0.2×2.5＋0.02×15＝$0.80 | 約 80 |
| Claude Opus 5.5 | $4.00 | $20.00 | 0.2×4＋0.02×20＝$1.20 | 約 120 |
| GPT-6 Astra（≤272K 層級） | $10.00 | $50.00 | 0.2×10＋0.02×50＝$3.00 | 約 300 |

（未計入快取折扣；代理的多輪工具呼叫會讓累計輸入 token 遠大於單次提示，實際數字以 `/usage` 為準。）

三個關鍵觀察：

1. **同一任務在不同模型間可差 100 倍**，模型選擇是最大的成本槓桿。
2. **長 context 層級更貴**：GPT-5.4 超過 272K 輸入時單價加倍；Haiku 5.5 超過 100K 時輸入單價變 5 倍。選擇 1M context 或更高推理強度都會增加消耗，官方建議預設用一般 context 與推理強度，複雜任務才提高。
3. **快取輸入便宜很多**（通常約為輸入單價的 1/10 到 1/20），保持同一 Session 連續工作比反覆開新 Session 重新載入 context 划算。

### 17.2 方案與內含額度

| 方案 | 月費 | 內含 AI Credits | 備註 |
|------|------|------|------|
| Copilot Free／Student | 免費 | 有額度 | 只能透過 Auto 模型選擇使用模型 |
| Copilot Pro | US$10 | 1,500（基本 1,000＋彈性 500） | — |
| Copilot Pro+ | US$39 | 7,000（基本 3,900＋彈性 3,100） | — |
| Copilot Max | US$100 | 20,000（基本 10,000＋彈性 10,000） | — |
| Copilot Business | 依授權 | 每人每月 1,900，**在計費實體層級合併成共用池** | 超額預設允許 |
| Copilot Enterprise | 依授權 | 每人每月 3,900，共用池 | 超額預設允許 |

| 規則 | 說明 |
|------|------|
| 重置 | 每月 1 日 00:00:00 UTC，與訂閱日期無關；未用完不遞延 |
| 先用哪個 | 個人方案先用基本額度，再用彈性額度 |
| Auto 折扣 | 付費方案使用 Auto 模型選擇時，模型費用享 10% 折扣（Chat、CLI、Copilot app、cloud agent） |
| 不計費的功能 | 程式碼補全與 next edit suggestions 不計入 AI Credits |
| 舊計費平台 | 仍在舊平台的帳戶會看到「premium requests」而非 AI Credits |
| 最低 CLI 版本 | 要正確顯示用量計費資訊，CLI 至少需 v1.0.48 |

### 17.3 超額與預算

**個人方案**用完額度時：升級方案（只付差額）、設定額外用量預算（以美元設定、以 AI Credits 扣抵）、或等下個月重置。

**組織與企業**：

| 控制 | 說明 |
|------|------|
| AI credits paid usage 政策 | 超額用量**預設啟用**；要禁止超額必須由管理者明確關閉 |
| 使用者層級預算 | 限制個人可從共用池與超額中使用的量；設為 $0 立即封鎖 |
| Cost center 預算 | 限制一組使用者在共用池用完後的超額費用 |
| 組織層級預算 | 限制計入該組織座位的超額費用 |
| 企業支出上限 | 限制整個企業的超額費用 |
| 無自動降級 | 預算用完會直接封鎖，**不會自動改用較便宜的模型** |

以 Actions 的 `GITHUB_TOKEN` 計入組織的用量不歸屬個人，使用者預算不適用，要用 cost center 管理（第 16 章）。

### 17.4 在 CLI 中觀察與限制用量

| 工具 | 內容 |
|------|------|
| Footer | 持續顯示剩餘 AI Credits 額度 |
| `/statusline` | 加入 `quota`（相對方案上限）與 `ai-used`（本 Session 已用） |
| `/model` | 顯示各模型的每 token 單價（舊平台顯示倍率） |
| `/context` | context 中各部分的 token 佔用；實驗性模式可細分到 skills、子代理、MCP、plugins |
| `/usage` | 本 Session 的 AI Credits、token 明細（輸入、輸出、快取）與各模型用量 |
| `/exit` | 離開時的用量摘要 |
| `--usage-output-file` | 程式化模式輸出用量 JSON |

#### 17.4.1 Session 上限（公開預覽）

```text
/limits                              # 互動式設定
/limits set max-ai-credits 300       # 設定上限（最少 30）
/limits unset                        # 移除
```

```bash
copilot -p "重構 OrderMapper 並補測試" --max-ai-credits 200 --allow-tool=write --allow-tool='shell(./mvnw:*)'
```

| 特性 | 說明 |
|------|------|
| 軟上限 | 用量要等模型回應後才知道，單次呼叫可能超過上限，之後的呼叫才會被擋 |
| 範圍 | 互動式：整個 Session（`/clear`、`/new` 會重置已用量但保留上限）；程式化：整次執行 |
| 子代理 | 與主 Session 共用同一個上限 |
| 隱藏工作 | 壓縮等不可見的模型呼叫也會計入 |
| 提示 | 約 50%、75%、90% 時顯示；只剩最後一次呼叫時會提示工具將被停用 |
| Autopilot | `/autopilot 目標 --max-ai-credits N` 可為單一目標設定上限 |

> 📝 官方 command reference 對 `--max-ai-credits` 的描述（「每個回應」、每則訊息重置）與 `copilot help limits` 及〈Setting a session limit〉頁面（整個 Session 累計）不一致；本手冊以本機 v1.0.97 的 `copilot help limits` 為準，已列入附錄 H.4。

### 17.5 節省成本的做法

| 做法 | 效果 | 範例 |
|------|------|------|
| 依任務選模型 | 最大的槓桿 | 探索與簡單問答用 Haiku 或 Auto；複雜重構才用 Opus |
| 使用 Auto | 10% 折扣，並依任務自動選擇 | `copilot --model auto` |
| Plan 用強模型、實作用一般模型 | 推理集中在規劃 | `/model plan` 設定規劃模型 |
| 精準 context | 減少輸入 token | `@檔案` 取代全專案搜尋；精簡 MCP 工具 |
| 旁支問題用 `/ask` | 不污染主 context | `/ask Java record 可以有 static 方法嗎` |
| 不需要 AI 的指令用 `!` | 不消耗 AI Credits | `! ./mvnw test` |
| 小心 `/fleet` | 子代理各自呼叫模型 | 只在真正可平行的任務使用 |
| 設定上限 | 防止失控 | `--max-ai-credits`、延續上限 |
| 被限速時切到 Auto | 減少中斷 | 設定 `continueOnAutoMode: true` |

### 17.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 成本說明 | 仍用「每個提示扣一次 premium request」 | AI Credits 依 token 與模型計價 | 對照官方 billing 文件與 `/usage` |
| 方案額度 | 寫死舊數字、未註明查證日期 | 註明查證日期並附官方連結 | 開啟官方定價頁比對 |
| 成本估算 | 只看單次提示 | 以多輪累計 token 估算，並以 `/usage` 實測校正 | 試點期間收集 `--usage-output-file` 數據 |
| 組織預算 | 以為超額預設關閉 | 超額預設啟用，需明確設定預算或關閉政策 | 檢查企業 AI Controls 設定 |
| Session 上限 | 以為是硬上限 | 軟上限，可能小幅超過 | 設定 30 credits 執行長任務，觀察實際用量 |
| CI 成本歸屬 | `GITHUB_TOKEN` 卻設定使用者預算控管 | 使用 cost center | 檢查帳單中的歸屬 |

---

## 第 18 章：升級、發佈頻道與版本管理

> **本章目標**
>
> - 理解自動更新在不同安裝方式下的實際行為。
> - 建立企業的版本鎖定、分批升級與回歸驗證流程。
> - 掌握 v1.0.80 之後的破壞性變更，避免升級後設定失效。

### 18.1 更新方式

| 安裝方式 | 自動更新行為 | 手動更新 |
|------|------|------|
| 獨立執行檔（WinGet、Homebrew、安裝腳本、直接下載） | 背景下載新版，**下次啟動時套用**；`/restart` 可在目前程序套用 | `copilot update` |
| npm | **只提示**有新版，不會自動安裝 | `npm install -g @github/copilot` |
| CI 環境 | 偵測到 `CI`、`BUILD_NUMBER`、`RUN_ID`、`SYSTEM_COLLECTIONURI` 時**預設關閉** | 固定版本安裝 |

```bash
copilot version                # 顯示版本並檢查更新（會連網）
copilot update                 # 更新到目前頻道最新版
copilot update stable          # 指定穩定頻道
copilot update prerelease      # 指定預發佈頻道
```

互動式介面：`/version`、`/update`（別名 `/upgrade`）、`/changelog`（別名 `/release-notes`），例如 `/changelog summarize since 1.0.80` 讓 AI 摘要多個版本的變更。團隊帳號可用 `/downgrade 版本` 下載並重新啟動到指定版本。

### 18.2 自動更新的控制

| 控制 | 說明 |
|------|------|
| `autoUpdate`（預設 `true`） | 是否自動下載新版；同時控制 session 開始時更新首方 plugins。**設為 `false` 只停止之後的下載，已下載的版本仍會套用** |
| `COPILOT_AUTO_UPDATE=false` 或 `--no-auto-update` | 停止下載，**而且**啟動時忽略快取中較新的版本，執行安裝檔內建的版本 |
| `autoUpdatesChannel` | `"stable"`（預設）或 `"prerelease"` |
| `--prefer-version 版本` | 指定使用快取中的特定版本（help 未列出的進階選項） |
| 受管設定要求新版 | v1.0.94 起，受管設定要求更新的 CLI 版本時會顯示更新指引，但不會阻擋一般提示 |

> 📝 **v1 手冊更正**：舊版提到 v1.0.29 新增「Nightly 發佈頻道」。v1.0.97 的 `copilot update --help` 只列出 `stable` 與 `prerelease` 兩個頻道。

### 18.3 企業版本管理策略

```mermaid
flowchart LR
    R0["Ring 0：平台團隊<br/>prerelease 或新 stable 當天"] --> R1["Ring 1：試點團隊<br/>穩定版發佈後 3～5 天"]
    R1 --> R2["Ring 2：全公司<br/>通過回歸驗證後"]
    R2 --> CI["CI 鎖定版本<br/>同步更新"]
```

| 項目 | 建議 |
|------|------|
| 鎖定版本 | 受管工作站與 CI 固定版本；以 `COPILOT_AUTO_UPDATE=false` 確保執行鎖定版本 |
| 升級節奏 | 每 2～4 週一次，或有安全修正時立即升級（例如 CVE-2026-29783 這類修正） |
| 變更審查 | 用 `/changelog since <目前版本>` 或閱讀 [changelog.md](https://github.com/github/copilot-cli/blob/main/changelog.md)，特別找 `Remove`、`Replace`、`renamed`、`no longer` 等字眼 |
| 回歸驗證 | 見 18.4 節 |
| 回退 | 安裝腳本 `VERSION=` 或 npm 指定版本；團隊帳號可 `/downgrade` |

### 18.4 升級回歸驗證清單

升級前在 Ring 0 執行：

```bash
copilot --version
# 1. 重新擷取 help，與舊版比對新增與消失的旗標、設定鍵、環境變數
copilot --help > help-new.txt && diff help-old.txt help-new.txt
copilot help config > config-new.txt && diff config-old.txt config-new.txt
copilot help environment > env-new.txt && diff env-old.txt env-new.txt
copilot completion bash > completion-new.bash    # 更新 check_flags.py 的旗標清單
# 2. 以新版清單檢查團隊文件與腳本中的旗標
python check_flags.py docs/copilot-guide.md --probe
# 3. 檢查所有 Copilot 設定檔
python check_config.py hooks .github/hooks/*.json
python check_config.py repo-settings .github/copilot/settings.json
# 4. 重跑 hook 測試
bash test_hooks.sh .github/hooks
# 5. 在拋棄式 Repo 跑一次 CI workflow（真正的 -p 執行）
```

### 18.5 v1.0.80 之後值得注意的變更

| 版本 | 變更 | 影響 |
|------|------|------|
| v1.0.81 | `/plugins` 移除，資源改到 `/plugin`、`/mcp`、`/skills`；hooks 與 LSP 的個別啟停暫時無法使用 | 舊文件中的 `/plugins` 失效 |
| v1.0.81 | 新增 `defaultMode`、`defaultPermissionMode`、`copilot app`、`copilot login --with-token` | 可用設定控制啟動模式與核准行為 |
| v1.0.83 | Linux Sandbox 需要 slirp4netns、nsenter、iptables 等；macOS／Linux Sandbox 預設封鎖本機服務 | 綁定本機埠的測試在 Sandbox 中失敗，需開啟 Allow local network |
| v1.0.85 | 指令列解析改為 Rust 文法，錯誤與 help 文字改變；`--max-autopilot-continues` 不再接受科學記號 | 解析 CLI 錯誤訊息的腳本要更新 |
| v1.0.85 | `copilot plugins install --skill`、`--kind`、`--scope`、`--mcp` 移除，改用 `copilot skill`、`copilot mcp`；`copilot plugins list --json` 改為扁平陣列 | 自動化腳本需要修改 |
| v1.0.85 | `COPILOT_ALLOW_ALL` 的值解析修正：`false`、`0` 等值會**關閉**自動核准 | 先前誤設的環境可能行為改變 |
| v1.0.87 | 空的 `strictKnownMarketplaces` 會封鎖內建 marketplace | 受管設定需檢查 |
| v1.0.88 | 未指定 `cwd` 的 hook 改回在專案根目錄執行；受管設定套用到 ACP、AHP、server 模式 | 依賴舊行為的 hook 需確認 |
| v1.0.89 | 支援 `.claude/rules` 作為指引；PR 建立會遵循 PR 範本 | 跨工具的規則檔會被讀取 |
| v1.0.91 | `/sandbox ca install` 改為 `create`＋`trust`；新增 `copilot sandbox ca` | 更新安裝文件 |
| v1.0.92 | 新增 `copilot config`；Sandbox 中的 shell 不再取得環境中的 `GITHUB_TOKEN`（除非明確設定） | 依賴該 Token 的 Sandbox 指令需調整 |
| v1.0.93 | **使用者設定只讀 `~/.copilot/settings.json`**，`config.json` 中的使用者設定被忽略；本機 Sandbox 開放所有使用者；新增受管 `permissions.limitTo` | 未搬移的設定會靜默失效 |
| v1.0.97 | custom agent 範圍的 hooks；Autopilot 中 preToolUse 的 `ask` 視為拒絕；TLS 攔截 Proxy 的串流修正 | 企業 Proxy 環境建議升級 |

完整的版本里程碑與已移除項目見[附錄 F](#附錄-f版本里程碑與已移除項目)。

### 18.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 自動更新說明 | 「`autoUpdate: false` 就不會再換版本」 | 已下載的版本仍會套用；要完全鎖定用 `COPILOT_AUTO_UPDATE=false` | 對照 `copilot help config` 與 `help environment` |
| npm 安裝的更新 | 以為 npm 安裝會自動更新 | npm 只提示，需手動更新 | 檢查升級 SOP |
| 發佈頻道 | 提到 nightly 頻道 | 只有 stable 與 prerelease | `copilot update --help` |
| 升級流程 | 直接全公司升級 | 分 Ring 並執行回歸驗證 | 檢查是否有 18.4 節的驗證紀錄 |
| 升級後的設定 | 沿用 `config.json` 中的設定 | 搬到 `settings.json` | `copilot config --list` 確認設定生效 |
| 自動化腳本 | 使用 `copilot plugins install --skill` | `copilot skill add` | `check_flags.py`；`copilot plugin --help` |

---

## 第 19 章：實戰案例

> **本章目標**
>
> - 透過四個企業常見情境，練習「提示 → AI 產出 → 審查 → 修正 → 驗證」的完整循環。
> - 學會在 AI 產出中找出看起來合理、實際有問題的程式碼。
> - 建立每類任務的驗證指令組合。

> 📝 本章的 Java 程式碼是**示意用的 AI 產出片段**，用來練習審查；它們沒有附完整專案，因此未經編譯（附錄 H.4）。可執行驗證的範例（hooks、設定檔、workflow）見第 11、16 章。

### 19.1 案例一：新增客戶管理 API（Plan → 實作）

#### 19.1.1 情境與提示

訂單系統要新增客戶管理模組（CRUD、分頁、驗證、測試）。使用 Plan 模式：

```text
/plan 在 order-service 新增客戶管理模組：
1. Customer：id、name、email（唯一）、phone、createdAt、updatedAt
2. API：GET /api/v1/customers（分頁）、GET /{id}、POST、PUT /{id}、DELETE /{id}
3. 遵守 .github/copilot-instructions.md 的分層與 DTO 規則
4. Flyway 遷移檔、service 單元測試、@WebMvcTest、@DataJpaTest
完成條件：./mvnw -q verify 全部通過
```

#### 19.1.2 審查計畫

代理產生的計畫若出現下列問題，要在核准前要求修改：

| 計畫中的問題 | 為什麼有問題 | 要求修改為 |
|------|------|------|
| 「修改 V1__init.sql 加入 customers 表」 | 違反「不得修改既有遷移檔」 | 新增 `V202610141200__create_customers.sql` |
| 沒有提到 email 唯一性的錯誤處理 | 重複 email 會變成 500 | 回 409 Problem Details |
| 測試只有成功路徑 | 驗證失敗、找不到資源未涵蓋 | 每個端點至少三種情境 |

#### 19.1.3 AI 產出與審查發現

```java
@Entity
@Table(name = "customers")
@Data                                   // ← 審查點 1
public class Customer {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(nullable = false, unique = true)
    private String email;
    // ...
}

@GetMapping
public Page<Customer> list(@RequestParam int page, @RequestParam int size) {   // ← 審查點 2、3
    return repository.findAll(PageRequest.of(page, size));                     // ← 審查點 4
}
```

| # | 發現 | 風險 | 正確做法 |
|------|------|------|------|
| 1 | JPA Entity 使用 `@Data` | `equals/hashCode` 涵蓋可變欄位與延遲載入關聯，放進 Set 後行為錯誤，`toString` 可能觸發 N+1 | 只用 `@Getter`／`@Setter`，`equals/hashCode` 以 id 實作或不覆寫 |
| 2 | 直接回傳 Entity | 洩漏內部欄位、API 與資料模型耦合；違反 Repo 指引 | 回傳 `record CustomerResponse(...)` |
| 3 | `size` 無上限 | `size=1000000` 造成記憶體與資料庫壓力 | `@PageableDefault(size = 20)` 並限制最大 100 |
| 4 | controller 直接注入 repository | 違反分層規則 | 經由 `CustomerService` |

#### 19.1.4 驗證

```bash
./mvnw -q verify                                          # 完成條件
git diff --name-only origin/main | grep 'db/migration'   # 只能有新增的遷移檔
git diff --diff-filter=M --name-only origin/main -- src/main/resources/db/migration   # 應該沒有輸出
grep -rn "@Data" src/main/java/**/domain/ || true         # Entity 不應出現 @Data
```

### 19.2 案例二：修 Bug 並補回歸測試

#### 19.2.1 情境與提示

正式環境回報：批次匯入客戶時偶發 `DataIntegrityViolationException`。

```text
#511 的錯誤：批次匯入客戶時偶發 DataIntegrityViolationException。
相關檔案 @src/main/java/com/acme/customer/CustomerImportService.java
請：1. 先寫一個能重現問題的失敗測試 2. 說明根因 3. 修正 4. 確認測試通過
不要修改既有測試的斷言。
```

#### 19.2.2 AI 產出與審查發現

```java
@Test
void shouldRollbackAllWhenCriticalErrorOccurs() {
    doThrow(new RuntimeException("DB connection lost"))
        .when(customerRepository).saveAll(anyList());
    assertThrows(ImportException.class, () -> service.batchImport(createBatch(1000)));
    assertThat(customerRepository.count()).isEqualTo(0);   // ← 審查點
}
```

| # | 發現 | 說明 |
|------|------|------|
| 1 | 對 mock 驗證「沒有寫入資料」 | `customerRepository` 是 mock，`count()` 永遠回傳預設值 0，這個斷言**永遠通過**，沒有驗證任何交易行為 |
| 2 | 測試沒有重現原始問題 | 原始問題是同一批次中的重複 email，測試卻模擬連線中斷 |
| 3 | 修正方式是「先查詢 email 是否存在再寫入」 | 存在競態：兩個批次同時匯入相同 email 仍會衝突；應依賴資料庫唯一限制並處理例外，或使用 upsert |

正確的回歸測試要用真實資料庫（例如 Testcontainers）並重現「同批次重複 email」：

```java
@Test
void batchWithDuplicateEmailsImportsFirstAndReportsSecond() {
    var result = service.batchImport(List.of(
        new CustomerImport("Alice", "alice@example.com"),
        new CustomerImport("Alice 2", "alice@example.com")));

    assertThat(result.successCount()).isEqualTo(1);
    assertThat(result.failures()).singleElement()
        .extracting(ImportFailure::reason).asString().contains("duplicate email");
    assertThat(customerRepository.count()).isEqualTo(1);   // 真實資料庫，斷言有意義
}
```

#### 19.2.3 驗證

```bash
git stash && ./mvnw -q -Dtest=CustomerImportServiceIT test; git stash pop   # 修正前測試必須失敗
./mvnw -q -Dtest=CustomerImportServiceIT test                               # 修正後必須通過
git diff origin/main -- 'src/test/**' | grep -E '^-\s*assert' || echo "沒有刪除既有斷言"
```

> ✅ **「先失敗再通過」是驗證修 Bug 最可靠的方法**：如果修正前測試就會通過，這個測試沒有重現問題。

### 19.3 案例三：建立 PR 與描述

#### 19.3.1 情境與提示

```text
/pr create 目標分支 develop；標題用 Conventional Commits；
描述依照 PR 範本，列出：變更摘要、修改的檔案、實際執行過的測試指令與結果、部署注意事項。
不要寫沒有執行過的測試結果。
```

#### 19.3.2 審查發現

| AI 產出的描述 | 問題 | 驗證方式 |
|------|------|------|
| 「單元測試 23/23 ✅、整合測試 8/8 ✅、覆蓋率 87%」 | 代理沒有執行整合測試與覆蓋率報告，數字是編造的 | 對照 Session timeline 中實際執行的指令；看 CI 結果 |
| 「需設定 `JWT_SECRET`」但變更中沒有讀取此變數 | 部署注意事項與程式碼不一致 | `git diff origin/develop \| grep JWT_SECRET` |
| 缺少 PR 範本中的「回滾方式」 | 未遵循範本 | 對照 `.github/pull_request_template.md` |

> ✅ PR 描述中的每一個「事實」（測試數字、設定變數、遷移檔名）都要能在 diff 或 CI 中找到對應證據。

### 19.4 案例四：Spring Batch 每日報表

#### 19.4.1 情境與提示

```text
建立 Spring Batch Job：DailyTransactionReportJob
- 讀取當日交易、依銀行代碼統計、輸出 CSV 到 /reports/、寄送摘要 Email
- 可重新啟動（restartable）、依銀行代碼分割平行處理、失敗重試 3 次
- 每日 02:00 執行
環境：Spring Boot 3.5、Spring Batch 5
```

#### 19.4.2 AI 產出與審查發現

```java
@Configuration
@EnableBatchProcessing                                   // ← 審查點 1
public class DailyTransactionReportJobConfig {
    @Bean
    public Job dailyTransactionReportJob(JobRepository repo, Step partitionStep) {
        return new JobBuilder("dailyTransactionReportJob", repo)
            .incrementer(new RunIdIncrementer())         // ← 審查點 2
            .start(partitionStep).build();
    }
    @Bean
    public Step partitionStep(JobRepository repo, Step processStep, Partitioner partitioner) {
        return new StepBuilder("partitionStep", repo)
            .partitioner("processStep", partitioner).step(processStep)
            .gridSize(10)
            .taskExecutor(new SimpleAsyncTaskExecutor())  // ← 審查點 3
            .build();
    }
}
```

| # | 發現 | 說明 | 正確做法 |
|------|------|------|------|
| 1 | Spring Boot 3 中加上 `@EnableBatchProcessing` | 會讓 Boot 的 Batch 自動設定退讓（包括啟動時自動執行 Job 等行為） | Boot 3 一般不需要此註解，除非刻意自行設定 |
| 2 | `RunIdIncrementer` 搭配「可重新啟動」需求 | 每次都產生新的 JobInstance，失敗後再執行不會從中斷處續跑，與 restartable 需求矛盾 | 以業務日期作為識別參數（例如 `businessDate`），重跑同一天即續跑 |
| 3 | `SimpleAsyncTaskExecutor` | 每個分割建立新執行緒、沒有上限 | 使用有界的 `ThreadPoolTaskExecutor` |
| 4 | 未見 `@Scheduled` 與重疊執行保護 | 前一次未完成時可能重複啟動 | 排程加上分散式鎖（例如 ShedLock），或交由外部排程器 |

#### 19.4.3 驗證

```bash
./mvnw -q -Dtest=DailyTransactionReportJobIT test     # 以 JobLauncherTestUtils 驗證完整流程
# 重新啟動測試：讓第 2 個分割失敗，重跑同一個 businessDate，確認只重做失敗的分割
```

### 19.5 案例的共同審查模式

| 模式 | 在本章出現的例子 | 審查方法 |
|------|------|------|
| 看起來對但斷言無效 | 對 mock 驗證 `count()` | 問：「把被測程式改壞，這個測試會失敗嗎？」 |
| 違反團隊規範 | `@Data`、回傳 Entity、修改遷移檔 | 以 `copilot-instructions.md` 逐條比對；能自動化的寫成 ArchUnit 或 lint |
| 與需求矛盾 | `RunIdIncrementer` vs. 可重新啟動 | 把需求逐條對應到程式碼位置 |
| 編造的事實 | PR 中的測試數字 | 要求證據：指令輸出、CI 連結 |
| 隱性資源風險 | 無上限分頁、無上限執行緒 | 檢查所有使用者輸入與並行設定的上限 |

### 19.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 實作計畫 | 修改既有遷移檔、測試只有成功路徑 | 新增遷移檔、每端點三種情境 | 核准計畫前逐條對照指引 |
| 回歸測試 | 修正前就會通過的測試 | 先失敗再通過 | `git stash` 後執行測試確認失敗 |
| 測試斷言 | 對 mock 斷言資料狀態 | 真實資料庫或驗證互動 | 刻意改壞程式，確認測試失敗（或使用 mutation testing） |
| PR 描述 | 未執行的測試結果 | 只寫有證據的事實 | 比對 timeline 與 CI |
| 框架用法 | Boot 3 加 `@EnableBatchProcessing`、無界執行緒 | 依框架版本的建議做法 | 查閱框架官方文件；壓力或重啟測試 |

---

## 第 20 章：最佳實務

> **本章目標**
>
> - 採用「探索 → 規劃 → 審查 → 實作 → 驗證 → 提交」的標準工作流程。
> - 寫出結構化、可驗證的提示。
> - 依任務風險決定人工介入的密度，並建立團隊規範與成效指標。

### 20.1 標準工作流程

官方最佳實務建議的流程，加上每一步的產出與檢查點：

```mermaid
flowchart LR
    E[探索 Explore] --> P[規劃 Plan]
    P --> R[審查 Review]
    R -- 需修改 --> P
    R -- 核准 --> I[實作 Implement]
    I --> V[驗證 Verify]
    V -- 失敗 --> I
    V -- 通過 --> C[提交 Commit]
```

| 步驟 | 提示範例 | 產出 | 人工檢查點 |
|------|------|------|------|
| 探索 | `閱讀認證相關的檔案，說明目前流程，先不要寫程式` | 理解摘要、相關檔案清單 | 代理找到的檔案是否完整 |
| 規劃 | `/plan 實作密碼重設流程` | `plan.md` | 範圍、步驟、測試策略、不能碰的東西 |
| 審查 | 直接在計畫上提出修改；必要時 `/rubber-duck 檢查這個計畫` | 修訂後的計畫 | **核准是最重要的人工關卡** |
| 實作 | `依照計畫實作`，或切換 Autopilot | 程式碼變更 | 核准對話框中的指令 |
| 驗證 | `執行 ./mvnw verify，修正所有失敗` | 測試結果 | 用確定性工具確認，而不是相信代理的「已完成」 |
| 提交 | `以 Conventional Commits 格式 commit` 或 `/pr create` | commit／PR | diff 審查（第 21 章） |

### 20.2 撰寫提示

#### 20.2.1 提示結構範本

```text
[目標]     要達成什麼（一句話）
[背景]     @相關檔案、#Issue、既有限制
[需求]     1. … 2. … 3. …
[限制]     不能做什麼（不修改遷移檔、不新增依賴…）
[完成條件] 可以用指令驗證的條件（./mvnw -q verify 通過、新增 3 個測試）
[輸出]     希望的回報格式（變更檔案清單＋驗證指令輸出）
```

#### 20.2.2 品質等級對照

| 等級 | 範例 | 問題 |
|------|------|------|
| ❌ 差 | `修一下訂單的 bug` | 沒有範圍、沒有重現方式、沒有完成條件 |
| ⚠️ 普通 | `修正 OrderService 取消訂單時重複退款的問題` | 有範圍，但沒有驗證方式 |
| ✅ 好 | `@OrderService.java 的 cancel() 在並發請求下會重複呼叫 refund()（#482）。先寫一個重現的並發測試，再以樂觀鎖修正，不要改 RefundClient。完成條件：新測試在修正前失敗、修正後通過，./mvnw -q verify 全綠。回報修改的檔案與測試輸出。` | 範圍、重現、限制、完成條件、輸出格式都有 |

#### 20.2.3 提示的黃金法則

1. **給範圍**：`@檔案`、`#Issue`、模組名稱。
2. **給完成條件**：能用指令驗證，而不是「做好一點」。
3. **給限制**：明確說不能做什麼。
4. **要證據**：要求貼出指令輸出，而不是只說「已完成」。
5. **一次一件事**：大任務先 Plan，拆成可驗證的步驟。
6. **口語化的想法先整理**：用 `/refine` 把語音或零散的想法改寫成結構化提示。

### 20.3 人機協作：依風險決定介入密度

| 任務風險 | 例子 | 模式 | 權限 | 人工介入 |
|------|------|------|------|------|
| 低 | 解釋程式、產生文件草稿 | 標準 | 預設（唯讀自動） | 看結果 |
| 中 | 新增功能、補測試 | Plan → 標準 | 寫入與建置指令可「本 Session」允許 | 審查計畫＋審查 diff |
| 中高 | 跨模組重構 | Plan → Autopilot＋Sandbox | 受限 allow＋deny push | 審查計畫、階段性檢查、完整 diff 審查 |
| 高 | 資料庫遷移、安全相關、正式環境設定 | 標準 | 逐次核准 | 每一步都看，並由第二人審查 |
| 不適合 | 直接操作正式環境 | — | — | 走 CI/CD 與變更管理 |

**何時必須停下來由人判斷**：代理要刪除或覆寫大量檔案、要修改 CI／部署設定、要改測試斷言才能讓測試通過、要新增或升級依賴、要存取 Repo 以外的路徑或網站、同一個錯誤修了三次還沒好。

### 20.4 團隊規範建議

| 項目 | 建議 |
|------|------|
| Repo 標配 | `.github/copilot-instructions.md`、`.github/hooks/`（安全政策）、`.github/copilot/settings.json`（模型與 deniedUrls） |
| 共用擴充 | 內部 plugin marketplace 發佈團隊 skills 與 agents |
| 何時用 Plan | 多檔案、重構、新功能 |
| 何時用 `/delegate` | 旁支任務、文件、獨立模組 |
| AI 參與的標示 | 保留 `Co-authored-by` trailer；PR 範本加入「AI 協助範圍」欄位 |
| Code Review | AI 產出與人寫的程式碼適用相同標準，並使用第 21 章的審查清單 |
| 知識累積 | 反覆出現的指示寫進 instructions 或 skill，而不是每次在提示中重寫 |

### 20.5 成效指標

| 指標 | 量測方式 | 注意 |
|------|------|------|
| Issue 到 PR 的時間 | GitHub 資料 | 與導入前基準比較 |
| PR 合併前的修改輪數 | PR review 資料 | 輪數上升可能代表 AI 產出品質不足 |
| Review 回饋數量與類型 | Review 留言分類 | 重複出現的問題應寫進指引 |
| 測試覆蓋率與缺陷逃逸率 | CI 與事件紀錄 | 速度提升不能以品質下降為代價 |
| AI Credits 成本 | `/usage`、帳單、OTel | 換算每個合併 PR 的成本 |
| 開發者回饋 | 定期問卷 | 搭配客觀數據解讀 |

### 20.6 常見反模式

| 反模式 | 後果 | 改善 |
|------|------|------|
| 每次都 `--yolo` | 一次誤判就造成損失 | 預設 Manual；Autopilot 搭配 Sandbox |
| 一個 Session 做所有事 | context 混雜、品質下降、成本上升 | 一個主題一個 Session，`/new` 切換 |
| 跳過計畫審查 | 方向錯誤時浪費大量 AI Credits 與時間 | 核准前逐條審查計畫 |
| 相信「已完成」 | 未驗證的程式碼進入主線 | 確定性工具驗證＋diff 審查 |
| 把規範寫在提示裡 | 每次重寫、容易遺漏 | 寫進 instructions、skill 或 hooks |
| 讓代理修 CI 而不看測試 diff | 測試被弱化 | 必看測試檔的變更 |

### 20.7 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 提示 | 沒有完成條件 | 包含可用指令驗證的完成條件 | 檢查提示是否符合 20.2.1 節範本 |
| 工作流程 | 直接要求實作複雜功能 | 先探索與規劃，審查後再實作 | Session 中是否有 `plan.md` 與審查紀錄 |
| 完成回報 | 「全部完成，測試通過」沒有證據 | 附上指令與輸出 | 自己重跑一次驗證指令 |
| 介入密度 | 高風險任務使用 Autopilot | 依 20.3 節表格選擇模式 | 對照任務風險分類 |
| 團隊規範 | 只有口頭約定 | 寫進 Repo 設定、hooks、PR 範本 | 檢查 Repo 是否有標配檔案 |

---

## 第 21 章：AI 產出驗證方法論

> **本章目標**
>
> - 建立一套可重複的方法，審查 AI 產出的計畫、程式碼、測試、指令與設定檔。
> - 學會用確定性工具取代「感覺沒問題」。
> - 取得並使用本手冊的離線檢查工具（`check_config.py`、`check_flags.py`）。

### 21.1 核心原則

| 原則 | 說明 |
|------|------|
| 宣稱不等於證據 | 代理說「測試通過」不算數；要看到指令與輸出，或自己重跑 |
| 確定性工具優先 | 編譯器、測試、lint、schema 驗證、靜態分析的結果，比任何模型（包括另一個 AI 審查者）都可靠 |
| 審查要有清單 | 依產出類型使用固定清單，避免只看「看起來對不對」 |
| 反向驗證 | 刻意弄壞程式或設定，確認測試或檢查器會失敗 |
| 範圍控制 | 檢查變更是否**只**涵蓋任務範圍，沒有順手改到其他東西 |

### 21.2 審查五問

每一份 AI 產出都先問這五個問題：

1. **範圍**：改動是否只限於任務需要的檔案？（`git diff --stat`）
2. **需求**：每一條需求能對應到哪一段程式碼或設定？
3. **證據**：完成條件是否有可重現的指令輸出？
4. **反向**：把被測程式改壞，測試會失敗嗎？把設定改錯，檢查器會抓到嗎？
5. **副作用**：有沒有新增依賴、修改 CI、放寬權限、刪除測試、寫入密鑰？

### 21.3 依產出類型的審查方法

#### 21.3.1 計畫（Plan 模式）

| 檢查項目 | 方法 |
|------|------|
| 是否誤解需求 | 逐條對照需求；代理提出的釐清問題是否都已回答 |
| 範圍外的變更 | 計畫中是否出現「順便重構」 |
| 違反限制 | 對照 `copilot-instructions.md` 與提示中的限制 |
| 測試策略 | 是否涵蓋失敗路徑與邊界 |
| 第二意見 | `/rubber-duck 檢查這份計畫的風險與遺漏` |

#### 21.3.2 程式碼 diff

```bash
git diff --stat origin/main...HEAD                  # 範圍：改了哪些檔案、多少行
git diff origin/main...HEAD -- '*Test*' '*IT*'      # 必看：測試檔的變更
git diff origin/main...HEAD -- pom.xml package.json build.gradle   # 依賴變更
git diff origin/main...HEAD -- .github/             # CI、hooks、Copilot 設定的變更
git log --format='%h %s%n%b' origin/main..HEAD | grep -i 'co-authored-by'   # AI 參與的 commit
```

| 風險訊號 | 意義 |
|------|------|
| 刪除或修改斷言 | 可能為了讓測試通過而弱化測試 |
| 新增 `@Disabled`、`skip`、`\|\| true` | 隱藏失敗 |
| 捕捉例外後什麼都不做 | 隱藏錯誤 |
| 新增依賴 | 需確認套件存在、維護狀態、授權與漏洞（防範依賴幻覺） |
| 修改 `.github/` 下的檔案 | 可能改變 CI、hooks 或 Copilot 權限 |
| 硬編碼 URL、Token、路徑 | 環境耦合或密鑰外洩 |

#### 21.3.3 測試

| 檢查 | 方法 |
|------|------|
| 修正前會失敗 | `git stash` 修正後重跑新測試 |
| 斷言有意義 | 不對 mock 斷言資料狀態；不只斷言「不為 null」 |
| 突變測試 | 以 PIT（Java）、Stryker（JS/TS）等工具量測測試是否能抓到程式變動 |
| 測試沒有被弱化 | 21.3.2 節的測試檔 diff |

#### 21.3.4 Shell 指令（核准對話框中）

| 看到 | 動作 |
|------|------|
| `rm -rf`、`git reset --hard`、`git push --force`、`git clean -fdx` | 拒絕，除非完全理解範圍 |
| `curl … \| sh`、下載並執行 | 拒絕 |
| 讀取 `.env`、`~/.ssh`、雲端憑證 | 拒絕並查明原因（可能是提示注入） |
| 連到不認識的網域 | 拒絕並檢查 context 中是否有可疑內容 |
| `sudo`、修改系統設定 | 拒絕 |
| 安裝套件 | 確認套件名稱拼字與來源 |

#### 21.3.5 Copilot 設定檔

使用 21.4 節的 `check_config.py`；它對照 v1.0.97 官方文件與 `copilot help config` 檢查 hooks、MCP、custom agent、skill、instructions、三種 settings、模型白名單、plugin、marketplace、LSP 共 12 種設定檔。

### 21.4 離線檢查工具

工具不需要呼叫模型、不消耗 AI Credits，可放進 pre-commit 或 CI。

#### 21.4.1 `check_config.py`：設定檔檢查器

用法：`python check_config.py <種類> <檔案>...`，結束碼 0 表示沒有錯誤。需要 Python 3.10 以上與 PyYAML（用於解析 frontmatter）。設定鍵清單 `user-keys.txt` 由 `copilot help config` 與官方 config-dir reference 擷取產生（共 99 個鍵）。

```python
#!/usr/bin/env python3
"""Copilot CLI 設定檔離線檢查器（對照 v1.0.97 官方文件與 `copilot help config`）。

用法：python check_config.py <種類> <檔案>...
種類：hooks | mcp | agent | skill | instructions | user-settings | repo-settings |
      managed-settings | models | plugin | marketplace | lsp
結束碼：0 = 沒有錯誤；1 = 至少一個錯誤（警告不影響結束碼）。
"""
import fnmatch
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

HOOK_EVENTS = {
    "sessionStart", "sessionEnd", "userPromptSubmitted", "userPromptTransformed",
    "preToolUse", "postToolUse", "postToolUseFailure", "agentStop", "subagentStart",
    "subagentStop", "errorOccurred", "preCompact", "permissionRequest", "notification",
    # VS Code / Claude 相容的 PascalCase 名稱
    "SessionStart", "SessionEnd", "UserPromptSubmit", "PreToolUse", "PostToolUse",
    "PostToolUseFailure", "Stop", "SubagentStop", "ErrorOccurred", "PreCompact",
    "PermissionRequest", "Notification",
}
MATCHER_EVENTS = {"preToolUse", "postToolUse", "permissionRequest", "notification",
                  "preCompact", "subagentStart", "PreToolUse", "PostToolUse",
                  "PermissionRequest", "Notification", "PreCompact"}
CMD_FIELDS = {"type", "bash", "powershell", "command", "exec", "args", "cwd", "env",
              "timeoutSec", "timeout", "matcher"}
HTTP_FIELDS = {"type", "url", "headers", "allowedEnvVars", "timeoutSec", "timeout", "matcher"}
SECRET_RE = re.compile(r"(ghp_|gho_|ghu_|github_pat_|sk-[A-Za-z0-9]{8}|xox[bp]-)[A-Za-z0-9_\-]{8,}")

AGENT_KEYS = {"name", "description", "tools", "model", "models", "modelPolicy",
              "reasoningEffort", "infer", "mcp-servers", "include-custom-instructions",
              "hooks", "sidekick", "target", "argument-hint", "handoffs"}
SKILL_KEYS = {"name", "description", "argument-hint", "allowed-tools", "user-invocable",
              "disable-model-invocation", "license", "metadata", "compatibility"}
REPO_KEYS = {"companyAnnouncements", "contextTier", "deniedUrls", "disableAllHooks",
             "disabledMcpServers", "disabledSkills", "effortLevel", "enabledPlugins",
             "extraKnownMarketplaces", "hooks", "includeCoAuthoredBy", "mergeStrategy",
             "model", "respectGitignore", "$schema"}
MANAGED_KEYS = {"allowedMcpServers", "autoTier", "deniedMcpServers", "enabledPlugins",
                "extraKnownMarketplaces", "forceLoginOrgs", "forceRemoteSettingsRefresh",
                "model", "effortLevel", "contextTier", "permissions", "policyHelper",
                "remoteControl", "sandbox", "shellShortcut", "strictKnownMarketplaces",
                "telemetry"}
SANDBOX_KEYS = {"enabled", "addCurrentWorkingDirectory", "allowDevToolAccess", "allowBypass",
                "auth", "credentials", "sandboxMcpServers", "sandboxLspServers", "userPolicy",
                "failIfUnavailable", "learningMode"}
MANAGED_ONLY_SANDBOX = {"failIfUnavailable", "learningMode"}
PERM_RULE_RE = re.compile(r"^(Bash|Shell|PowerShell|Read|Edit|Write|Domain)\((.+)\)$")


class Report:
    def __init__(self, path):
        self.path, self.errors, self.warnings = path, [], []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def load_json(path, rep):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001
        rep.err(f"JSON 無法解析：{e}")
        return None


def frontmatter(path, rep):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        rep.err("缺少 YAML frontmatter（檔案開頭必須是 --- ... ---）")
        return None, text
    try:
        import yaml
        data = yaml.safe_load(m.group(1)) or {}
    except Exception as e:  # noqa: BLE001
        rep.err(f"frontmatter YAML 無法解析：{e}")
        return None, m.group(2)
    if not isinstance(data, dict):
        rep.err("frontmatter 必須是 key: value 物件")
        return None, m.group(2)
    return data, m.group(2)


def scan_secrets(obj, rep, where=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            scan_secrets(v, rep, f"{where}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            scan_secrets(v, rep, f"{where}[{i}]")
    elif isinstance(obj, str) and SECRET_RE.search(obj):
        rep.err(f"{where} 疑似硬編碼密鑰，請改用 ${{ENV_VAR}} 參照")


# ---------- hooks ----------
def check_hooks(path, rep):
    d = load_json(path, rep)
    if d is None:
        return
    if d.get("version") != 1:
        rep.err('缺少 "version": 1（整個檔案會被拒絕載入）')
    hooks = d.get("hooks")
    if not isinstance(hooks, dict):
        rep.err('"hooks" 必須是以事件名稱為 key 的物件')
        return
    for ev, entries in hooks.items():
        if ev not in HOOK_EVENTS:
            rep.err(f"未知的事件名稱：{ev}")
        if not isinstance(entries, list):
            rep.err(f"{ev} 的值必須是陣列")
            continue
        for i, e in enumerate(entries):
            tag = f"{ev}[{i}]"
            t = e.get("type", "command")
            if t == "command":
                if "exec" in e and any(k in e for k in ("bash", "powershell", "command")):
                    rep.err(f"{tag} 不可同時使用 exec 與 bash/powershell/command")
                if not any(k in e for k in ("bash", "powershell", "command", "exec")):
                    rep.err(f"{tag} 需要 bash、powershell、command 或 exec 其中之一")
                if "bash" in e and "powershell" not in e and "command" not in e:
                    rep.warn(f"{tag} 只有 bash，Windows 使用者不會執行此 hook")
                unknown = set(e) - CMD_FIELDS
            elif t == "http":
                url = e.get("url", "")
                if not url:
                    rep.err(f"{tag} http hook 缺少 url")
                elif ev in ("preToolUse", "permissionRequest", "PreToolUse",
                            "PermissionRequest") and not url.startswith("https://"):
                    rep.err(f"{tag} {ev} 的 http hook 必須使用 https://")
                unknown = set(e) - HTTP_FIELDS
            elif t == "prompt":
                if ev not in ("sessionStart", "SessionStart"):
                    rep.err(f"{tag} prompt hook 只支援 sessionStart")
                unknown = set(e) - {"type", "prompt"}
            else:
                rep.err(f"{tag} 未知的 type：{t}")
                unknown = set()
            for k in sorted(unknown):
                rep.err(f"{tag} 未知欄位：{k}")
            if "matcher" in e:
                if ev not in MATCHER_EVENTS:
                    rep.warn(f"{tag} {ev} 不支援 matcher，會被忽略")
                try:
                    re.compile(e["matcher"])
                except re.error:
                    rep.err(f"{tag} matcher 不是合法的正規表示式（該 hook 會被略過）")
            to = e.get("timeoutSec", e.get("timeout"))
            if ev in ("preToolUse", "PreToolUse") and isinstance(to, (int, float)) and to > 30:
                rep.warn(f"{tag} preToolUse 逾時一律放行（fail-open），timeoutSec={to} 過長")
    scan_secrets(d, rep)


# ---------- MCP ----------
def check_mcp(path, rep):
    d = load_json(path, rep)
    if d is None:
        return
    if "servers" in d and "mcpServers" not in d:
        rep.err('頂層使用 "servers"（VS Code 格式），Copilot CLI 不會讀取；請改為 "mcpServers"')
        return
    servers = d.get("mcpServers", d)
    if not isinstance(servers, dict) or not servers:
        rep.err("找不到任何 MCP server 定義")
        return
    for name, s in servers.items():
        if not isinstance(s, dict):
            rep.err(f"{name} 必須是物件")
            continue
        if any(ord(c) < 32 or c == "}" for c in name):
            rep.err(f"{name} 名稱含控制字元或 }}")
        t = s.get("type", "local")
        if t in ("local", "stdio"):
            if not s.get("command"):
                rep.err(f"{name}（{t}）缺少 command")
            if "url" in s:
                rep.warn(f"{name}（{t}）的 url 不會被使用")
            args = " ".join(map(str, s.get("args", [])))
            if re.search(r"@latest\b", args):
                rep.warn(f"{name} 使用 @latest，建議固定版本以利稽核與重現")
        elif t in ("http", "sse", "streamable-http"):
            url = s.get("url", "")
            if not url:
                rep.err(f"{name}（{t}）缺少 url")
            elif not url.startswith("https://") and not re.match(r"^http://(localhost|127\.|\[::1\])", url):
                rep.err(f"{name} 遠端 server 應使用 https://（目前：{url}）")
            if t == "sse":
                rep.warn(f"{name} 使用已棄用的 SSE transport，建議改為 http（Streamable HTTP）")
        else:
            rep.err(f"{name} 未知的 type：{t}（允許 local、stdio、http、sse）")
        if "tools" not in s:
            rep.warn(f"{name} 未設定 tools；command reference 列為必填，建議明確列出需要的工具")
        tools = s.get("tools", ["*"])
        if not isinstance(tools, list):
            rep.err(f"{name} tools 必須是陣列")
    scan_secrets(d, rep)


# ---------- custom agent ----------
def check_agent(path, rep):
    base = os.path.basename(path)
    if not (base.endswith(".agent.md") or base.endswith(".md")):
        rep.err("檔名必須以 .agent.md 或 .md 結尾")
    fm, body = frontmatter(path, rep)
    if fm is None:
        return
    if not fm.get("description"):
        rep.err("缺少必填欄位 description（主代理依此決定何時委派）")
    for k in sorted(set(fm) - AGENT_KEYS):
        rep.err(f"未知的 frontmatter 欄位：{k}")
    tools = fm.get("tools")
    if tools is not None and not isinstance(tools, list):
        rep.err('tools 必須是陣列，例如 ["view", "grep"]')
    if "infer" in fm and not isinstance(fm["infer"], bool):
        rep.err("infer 必須是布林值 true/false")
    if "include-custom-instructions" in fm and not isinstance(fm["include-custom-instructions"], bool):
        rep.err("include-custom-instructions 必須是布林值")
    if fm.get("modelPolicy") not in (None, "preferred", "required"):
        rep.err('modelPolicy 只能是 "preferred" 或 "required"')
    if isinstance(tools, list) and "*" in tools and len(tools) > 1:
        rep.warn("tools 含 * 代表全部工具，其他項目沒有限制效果")
    if len(body.strip()) < 40:
        rep.warn("提示內容過短，代理行為難以預期")


# ---------- skill ----------
def check_skill(path, rep):
    if os.path.basename(path) != "SKILL.md":
        rep.err("檔名必須是 SKILL.md")
    fm, body = frontmatter(path, rep)
    if fm is None:
        return
    name = fm.get("name")
    if not name:
        rep.err("缺少必填欄位 name")
    elif not re.match(r"^[A-Za-z0-9][A-Za-z0-9 _.:\-]{0,63}$", str(name)):
        rep.err(f"name 不合法：{name}（須以英數字開頭，只含英數字、-_.: 與空白，最多 64 字元）")
    desc = fm.get("description")
    if not desc:
        rep.err("缺少必填欄位 description")
    elif len(str(desc)) > 1024:
        rep.err("description 超過 1024 字元")
    for k in sorted(set(fm) - SKILL_KEYS):
        rep.warn(f"非標準欄位：{k}")
    dirname = os.path.basename(os.path.dirname(os.path.abspath(path)))
    if name and dirname != str(name):
        rep.warn(f"目錄名稱 {dirname} 與 name {name} 不一致，維護時容易混淆")
    if not body.strip():
        rep.err("SKILL.md 沒有內容")


# ---------- instructions ----------
def check_instructions(path, rep):
    base = os.path.basename(path)
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    if base.endswith(".instructions.md"):
        fm, body = frontmatter(path, rep)
        if fm is not None:
            if not fm.get("applyTo"):
                rep.err("路徑專屬指引缺少 applyTo（不會套用到任何檔案）")
            ex = fm.get("excludeAgent")
            if ex not in (None, "code-review", "cloud-agent"):
                rep.err('excludeAgent 只能是 "code-review" 或 "cloud-agent"')
        text = body
    for m in re.finditer(r"^@(\S+)", text, re.M):
        ref = m.group(1)
        if ref.startswith(("/", "~")) or re.match(r"^[A-Za-z]:[\\/]", ref):
            rep.err(f"@{ref}：絕對路徑或 ~/ 開頭的引用不會被載入")
        elif base.endswith(".instructions.md") or base == "GEMINI.md":
            rep.warn(f"@{ref}：{base} 不展開 @ 檔案引用")
    lines = [ln for ln in text.split("\n") if ln.strip()]
    if len(lines) > 200:
        rep.warn(f"指引有 {len(lines)} 行，過長會稀釋效果；建議拆成路徑專屬指引")


# ---------- settings ----------
def user_keys():
    keys = set()
    for ln in open(os.path.join(HERE, "user-keys.txt"), encoding="utf-8"):
        ln = ln.strip()
        if ln:
            keys.add(re.split(r"[.\[]", ln)[0])
    return keys | {"$schema"}


def check_sandbox(sb, rep, managed):
    if not isinstance(sb, dict):
        rep.err("sandbox 必須是物件")
        return
    for k in sb:
        if k not in SANDBOX_KEYS:
            hint = ""
            if k in ("gitAuth", "ghAuth"):
                hint = "（已改名為 auth.git / auth.gh，舊鍵會被忽略）"
            if k == "allowDevToolCaches":
                hint = "（已改名為 allowDevToolAccess）"
            rep.err(f"sandbox.{k} 不是有效的鍵{hint}")
        elif k in MANAGED_ONLY_SANDBOX and not managed:
            rep.err(f"sandbox.{k} 只能由管理者在受管設定中設定")


def check_settings(path, rep, scope):
    d = load_json(path, rep)
    if d is None or not isinstance(d, dict):
        return
    if scope == "user":
        allowed = user_keys()
    elif scope == "repo":
        allowed = REPO_KEYS
    else:
        allowed = MANAGED_KEYS
    for k in d:
        if k not in allowed:
            if scope == "repo" and k in user_keys():
                rep.err(f"{k} 是使用者層級設定，放在 Repo 設定中會被靜默忽略")
            else:
                rep.err(f"未知的設定鍵：{k}")
    if "sandbox" in d:
        if scope == "repo":
            pass  # 已在上面回報
        else:
            check_sandbox(d["sandbox"], rep, scope == "managed")
    perms = d.get("permissions")
    if isinstance(perms, dict):
        mode = perms.get("disableBypassPermissionsMode")
        if mode not in (None, "disable", "allow-auto-only"):
            rep.err(f'disableBypassPermissionsMode 無效值 {mode}（會被強制視為 "disable"）')
        if scope == "managed":
            for fam in ("deny", "ask", "allow"):
                for rule in perms.get(fam, []):
                    if not PERM_RULE_RE.match(rule):
                        rep.err(f"permissions.{fam} 規則格式錯誤：{rule}")
            for dom in perms.get("limitTo", []):
                if dom.startswith(("http://", "https://")) or "/" in dom:
                    rep.err(f"limitTo 只接受網域，不可含協定或路徑：{dom}")
        elif any(k in perms for k in ("deny", "ask", "allow", "limitTo")):
            rep.warn("permissions 規則陣列只在受管設定（MDM／伺服器）中生效")
    for urlkey in ("allowedUrls",):
        if "*" in d.get(urlkey, []):
            rep.err(f"{urlkey} 含 *，等同放行所有網址")
    if scope == "managed":
        for lst in ("allowedMcpServers", "deniedMcpServers"):
            for i, e in enumerate(d.get(lst, [])):
                keys = set(e) & {"serverUrl", "serverCommand", "serverName"}
                if len(keys) != 1:
                    rep.err(f"{lst}[{i}] 必須剛好使用 serverUrl、serverCommand、serverName 其中之一")
                if lst == "allowedMcpServers" and "serverName" in e and not re.match(r"^[A-Za-z0-9_-]+$", e["serverName"]):
                    rep.err(f"{lst}[{i}] allowlist 的 serverName 只能含 [A-Za-z0-9_-]")
        rc = d.get("remoteControl")
        if isinstance(rc, dict) and rc.get("mode") == "requireSSO" and not rc.get("githubDotComOrganizations"):
            rep.err("remoteControl.mode=requireSSO 時必須設定 githubDotComOrganizations")
    scan_secrets(d, rep)


# ---------- allowed_models.txt ----------
def check_models(path, rep):
    fallbacks, globs = [], []
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        ln = raw.strip()
        if not ln or ln.startswith("#"):
            continue
        if ln.startswith("fallback:"):
            fallbacks.append((n, ln.split(":", 1)[1].strip()))
        elif ln.startswith("!"):
            rep.err(f"第 {n} 行：不支援否定規則 {ln}")
        else:
            globs.append(ln)
    if len(fallbacks) != 1:
        rep.err(f"fallback: 必須剛好出現一次（目前 {len(fallbacks)} 次）")
    for n, fb in fallbacks:
        if any(c in fb for c in "*?[]"):
            rep.err(f"第 {n} 行：fallback 必須是完整模型 ID，不能是 glob")
        elif globs and not any(fnmatch.fnmatchcase(fb, g) for g in globs):
            rep.err(f"第 {n} 行：fallback 模型 {fb} 不符合任何允許規則")


# ---------- plugin / marketplace / lsp ----------
AP_TOP = {"$schema", "name", "version", "description", "author", "homepage",
          "repository", "license", "keywords", "extensions"}


def check_plugin(path, rep):
    d = load_json(path, rep)
    if d is None:
        return
    if not d.get("name"):
        rep.err("缺少 name")
    elif not re.match(r"^[a-z0-9][a-z0-9.\-]{0,63}$", d["name"]):
        rep.err(f"name 建議使用 kebab-case（目前：{d['name']}）")
    if "agent-plugins.org" in str(d.get("$schema", "")):
        for k in sorted(set(d) - AP_TOP):
            rep.err(f"Agent Plugins 1.0 不允許頂層欄位 {k}（會被忽略）")
    if not d.get("version"):
        rep.warn("缺少 version，使用者難以判斷是否需要更新")


def check_marketplace(path, rep):
    d = load_json(path, rep)
    if d is None:
        return
    for k in ("name", "owner", "plugins"):
        if k not in d:
            rep.err(f"缺少必填欄位 {k}")
    if not isinstance(d.get("owner", {}), dict) or not d.get("owner", {}).get("name"):
        rep.err("owner 必須是含 name 的物件")
    for i, p in enumerate(d.get("plugins", [])):
        for k in ("name", "source"):
            if not p.get(k):
                rep.err(f"plugins[{i}] 缺少 {k}")
        src = p.get("source")
        if isinstance(src, str) and (src.startswith("/") or ".." in src):
            rep.err(f"plugins[{i}].source 必須是 Repo 內的相對路徑：{src}")


def check_lsp(path, rep):
    d = load_json(path, rep)
    if d is None:
        return
    servers = d.get("lspServers")
    if not isinstance(servers, dict) or not servers:
        rep.err('缺少 "lspServers" 物件')
        return
    for name, s in servers.items():
        if not any(k in s for k in ("command", "bash", "powershell")):
            rep.err(f"{name} 需要 command、bash 或 powershell 其中之一")
        fe = s.get("fileExtensions")
        if not isinstance(fe, dict) or not fe:
            rep.err(f"{name} 缺少 fileExtensions（副檔名 → language ID）")
        else:
            for ext in fe:
                if not ext.startswith("."):
                    rep.err(f"{name} 副檔名必須以 . 開頭：{ext}")


KINDS = {
    "hooks": check_hooks, "mcp": check_mcp, "agent": check_agent, "skill": check_skill,
    "instructions": check_instructions,
    "user-settings": lambda p, r: check_settings(p, r, "user"),
    "repo-settings": lambda p, r: check_settings(p, r, "repo"),
    "managed-settings": lambda p, r: check_settings(p, r, "managed"),
    "models": check_models, "plugin": check_plugin, "marketplace": check_marketplace,
    "lsp": check_lsp,
}


def main(argv):
    if len(argv) < 3 or argv[1] not in KINDS:
        print(__doc__)
        return 2
    total_err = 0
    for path in argv[2:]:
        rep = Report(path)
        KINDS[argv[1]](path, rep)
        status = "OK" if not rep.errors else "FAIL"
        print(f"[{status}] {argv[1]} {path}")
        for e in rep.errors:
            print(f"    錯誤：{e}")
        for w in rep.warnings:
            print(f"    警告：{w}")
        total_err += len(rep.errors)
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

#### 21.4.2 `check_flags.py`：旗標與指令檢查器

掃描 Markdown 文件中程式碼區塊裡的 `copilot` 指令與 slash 指令，對照本機版本的清單。清單產生方式：

```bash
copilot completion bash | grep -oE -- '--[a-z][a-z0-9-]+' | sort -u > flags.txt    # 含 help 未列出的隱藏旗標
copilot --help | sed -n '/^Commands:/,/^Options:/p' | awk '/^  [a-z]+ /{print $1}' > subcommands.txt
copilot help commands | grep -oE '^    /[a-z][a-z-]*' | tr -d ' ' > slash-commands.txt
```

`--probe` 選項會對清單外的旗標實際執行 `copilot <旗標> --help`：v1.0.97 對未知旗標回傳 `error: unexpected argument`，因此可以離線判斷旗標是否存在。

```python
#!/usr/bin/env python3
"""檢查 Markdown 文件中出現的 Copilot CLI 旗標、子指令與 slash 指令是否真實存在。

對照來源（同目錄）：
  flags.txt          由 `copilot completion bash` 擷取的全部旗標（含 help 未列出的隱藏旗標）
  subcommands.txt    `copilot --help` 的 Commands 區段
  slash-commands.txt `copilot help commands` + 官方 command reference 的 slash 指令
  slash-extra.txt    文件中自行定義的 skill 名稱（skill 會成為 /名稱 指令）
  slash-removed.txt  已移除的舊指令：只允許出現在含「移除／失效／不存在／舊版」字樣的行
用法：python check_flags.py <file.md> [--probe]
  --probe：對不在清單中的旗標實際執行 `copilot <flag> --help` 確認（需本機已安裝 copilot）
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return {ln.strip() for ln in f if ln.strip()}


FLAGS, SUBS = load("flags.txt"), load("subcommands.txt")
SLASH = load("slash-commands.txt") | load("slash-extra.txt")
REMOVED = load("slash-removed.txt")
REMOVED_CTX = re.compile(r"移除|失效|不存在|舊版|removed")


def slash_ok(cmd, line):
    return cmd in SLASH or (cmd in REMOVED and REMOVED_CTX.search(line) is not None)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
# 文件中刻意示範的錯誤寫法（❌ 範例）可用行尾註解 `# check-flags: ignore` 排除
IGNORE_MARK = "check-flags: ignore"


def code_blocks(lines):
    fence, lang, start = None, "", 0
    for i, ln in enumerate(lines):
        m = FENCE.match(ln)
        if fence is None and m:
            fence, lang, start = m.group(1), m.group(2).strip(), i + 1
        elif fence is not None and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2).strip():
            yield lang, start, lines[start:i]
            fence = None


def logical_lines(block, base):
    """合併以反斜線或反引號結尾的續行，回傳 (行號, 內容)。"""
    buf, first = "", None
    for k, ln in enumerate(block):
        if first is None:
            first = base + k + 1
        s = ln.rstrip()
        if s.endswith("\\") or s.endswith("`"):
            buf += s[:-1] + " "
            continue
        yield first, buf + s
        buf, first = "", None
    if buf:
        yield first, buf


def probe(flag):
    for args in ([flag, "--help"], [flag, "x", "--help"]):
        try:
            r = subprocess.run(["copilot", *args], capture_output=True, text=True, timeout=30,
                               shell=(os.name == "nt"))
        except Exception:  # noqa: BLE001
            return None
        if "unexpected argument" not in (r.stdout + r.stderr):
            return True
    return False


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path, do_probe = sys.argv[1], "--probe" in sys.argv
    lines = open(path, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    problems, n_flag, n_sub, n_slash = [], 0, 0, 0
    for lang, base, block in code_blocks(lines):
        for ln_no, text in logical_lines(block, base):
            if IGNORE_MARK in text:
                continue
            # slash 指令：行首（可帶 > 或 $ 提示字元）
            m = re.match(r"^\s*(?:>\s*|\$\s*)?(/[a-z][a-z-]*)(?=\s|$)", text)
            if m and lang not in ("json", "yaml", "yml", "python", "java", "typescript", "toml", "ini"):
                n_slash += 1
                if not slash_ok(m.group(1), text):
                    problems.append(f"L{ln_no} 未知的 slash 指令 {m.group(1)}：{text.strip()[:80]}")
            # copilot 指令：可能在行首、$ 之後、管線或 && 之後、YAML run: 之後
            for cm in re.finditer(r"(?:^|[\s;&|(]|run:\s*)copilot((?:\s+(?!\||&&|;|>)\S+)*)", text):
                args = cm.group(1).split()
                if args and not args[0].startswith("-") and not args[0].startswith(("'", '"')):
                    word = args[0]
                    if re.match(r"^[a-z]+$", word):
                        n_sub += 1
                        if word not in SUBS:
                            problems.append(f"L{ln_no} 未知的子指令 copilot {word}")
                for a in args:
                    fm = re.match(r"^(--[a-z][a-z0-9-]*)", a)
                    if not fm:
                        continue
                    flag = fm.group(1)
                    n_flag += 1
                    if flag in FLAGS:
                        continue
                    ok = probe(flag) if do_probe else None
                    if ok is not True:
                        problems.append(f"L{ln_no} 未知的旗標 {flag}" + ("（實測不接受）" if ok is False else ""))
    # 內文中的 `/command` 行內程式碼
    in_code = False
    for i, ln in enumerate(lines, 1):
        if FENCE.match(ln):
            in_code = not in_code
            continue
        if in_code or IGNORE_MARK in ln:
            continue
        for m in re.finditer(r"`(/[a-z][a-z-]+)(?:[\s`])", ln):
            cmd = m.group(1)
            if "/" in cmd[1:]:
                continue
            n_slash += 1
            if not slash_ok(cmd, ln):
                problems.append(f"L{i} 內文未知的 slash 指令 {cmd}")
    print(f"檢查：旗標 {n_flag} 次、子指令 {n_sub} 次、slash 指令 {n_slash} 次")
    print(f"問題：{len(problems)}")
    for p in problems:
        print("  ", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
```

#### 21.4.3 正反範例測試

檢查器本身也需要被驗證：正向範例必須通過、反向範例必須被抓到。

```bash
#!/usr/bin/env bash
# 正向範例必須全部通過；反向範例必須全部被抓到（每一筆都要 FAIL）。
cd "$(dirname "$0")" || exit 2
PY="python -X utf8 checkers/check_config.py"
R=examples/repo/.github
ok=0; bad=0

pos() { if $PY "$@"; then ok=$((ok+1)); else bad=$((bad+1)); echo "!! 正向範例未通過：$*"; fi; }
neg() { if $PY "$@" >/tmp/neg.out 2>&1; then bad=$((bad+1)); echo "!! 反向範例未被抓到：$*"; cat /tmp/neg.out
        else ok=$((ok+1)); echo "[預期失敗] $*"; sed -n '2,6p' /tmp/neg.out; fi; }

echo "== 正向範例 =="
pos hooks "$R/hooks/copilot-policy.json"
pos mcp "$R/mcp.json"
pos agent "$R/agents/security-reviewer.agent.md"
pos skill "$R/skills/db-migration/SKILL.md"
pos instructions "$R/copilot-instructions.md" "$R/instructions/controller.instructions.md"
pos repo-settings "$R/copilot/settings.json"
pos user-settings examples/user-settings.json
pos managed-settings examples/managed-settings.json
pos models "$R/allowed_models.txt"
pos plugin examples/plugin/plugin.json
pos marketplace examples/plugin/marketplace.json
pos lsp "$R/lsp.json"

echo "== 反向範例 =="
neg hooks neg/v1-handbook-hooks.json
neg mcp neg/vscode-mcp.json
neg mcp neg/bad-mcp.json
neg agent neg/bad.agent.md
neg skill neg/bad-skill/SKILL.md
neg instructions neg/bad.instructions.md
neg repo-settings neg/bad-repo-settings.json
neg models neg/bad_allowed_models.txt

echo "總計：符合預期 $ok，不符合 $bad"
[ "$bad" -eq 0 ]
```

本手冊的執行結果：正向 12 項全部通過、反向 8 項全部被抓到（`符合預期 20，不符合 0`）。反向範例中的 `v1-handbook-hooks.json` 就是舊版手冊中的 hook 設定，被檢查器抓出缺少 `version` 與不存在的 `permission` 欄位。

#### 21.4.4 放進 CI

```yaml
name: Copilot config lint
on:
  pull_request:
    paths: [".github/**", "AGENTS.md", "CLAUDE.md"]
permissions:
  contents: read
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install pyyaml
      - name: Check Copilot configuration files
        run: |
          python tools/check_config.py hooks .github/hooks/*.json
          python tools/check_config.py repo-settings .github/copilot/settings.json
          python tools/check_config.py instructions .github/copilot-instructions.md .github/instructions/*.instructions.md
          for f in .github/agents/*.agent.md; do python tools/check_config.py agent "$f"; done
          for f in .github/skills/*/SKILL.md; do python tools/check_config.py skill "$f"; done
          if [ -f .github/mcp.json ]; then python tools/check_config.py mcp .github/mcp.json; fi
```

### 21.5 驗證的極限

| 工具 | 抓得到 | 抓不到 |
|------|------|------|
| `check_config.py` | 格式、未知鍵、改名的鍵、明顯的密鑰、不安全的端點 | 設定的語意是否符合你的意圖；未來版本新增的鍵（需更新清單） |
| `check_flags.py` | 不存在的旗標、子指令、slash 指令 | 旗標組合是否合理；旗標值是否正確 |
| Hook 測試 | 規則對指定輸入的決策 | 混淆過的指令；規則沒想到的危險指令 |
| AI 審查（`/review`） | 常見 bug 與弱點 | 低信心問題（刻意不回報）；業務邏輯錯誤 |
| 人工審查 | 意圖、架構、業務邏輯 | 疲勞與疏忽（所以需要清單與工具輔助） |

沒有任何一層足夠，**分層組合**才是可靠的驗證：確定性工具 → AI 審查 → 人工審查 → Sandbox 與權限作為執行期防線。

### 21.6 本章審查與驗證清單

| AI 產出項目 | ❌ 錯誤示範 | ✅ 正確做法 | 人工如何驗證 |
|------|------|------|------|
| 任何程式碼變更 | 只看代理的總結 | 審查五問＋diff 審查 | 依 21.2 與 21.3.2 節逐項檢查 |
| 測試 | 修正前就會通過 | 先失敗再通過，必要時突變測試 | `git stash` 重跑；PIT／Stryker 報告 |
| 設定檔 | 憑感覺判斷 | `check_config.py` | CI 中自動執行 |
| 文件中的指令 | 抄自舊文件或 AI 推測 | 對照本機版本 | `check_flags.py --probe` |
| 檢查器本身 | 只測正向案例 | 正反範例都要測 | `run_checks.sh` 結果為「不符合 0」 |

---

## 附錄 A：指令與 slash 指令速查

> 依 v1.0.97 的 `copilot --help`、`copilot help commands` 與官方 command reference 整理。部分指令需要實驗性模式（標示為「實驗」）。

### A.1 子指令（在 shell 執行）

| 子指令 | 用途 | 常用範例 |
|------|------|------|
| `copilot login` | OAuth 或 Token 登入 | `copilot login --device-code`、`--host https://acme.ghe.com`、`--with-token` |
| `copilot init` | 產生 `.github/copilot-instructions.md` | `copilot init --sandbox` |
| `copilot config` | 讀寫設定 | `copilot config --list --json`、`copilot config --repo model claude-sonnet-5.5`、`copilot config --rm theme` |
| `copilot update` | 更新 | `copilot update stable` |
| `copilot version` | 版本與更新檢查 | — |
| `copilot mcp` | MCP 伺服器 | `list`、`get`、`add`、`remove`、`enable`、`disable` |
| `copilot plugin` | Plugin 與 marketplace | `install`、`uninstall`、`update --all`、`list --json`、`enable`、`disable`、`marketplace add\|remove\|list\|browse\|update` |
| `copilot skill` | Skills | `list --json`、`add [--project]`、`remove`、`enable`、`disable` |
| `copilot instruction list` | 列出會載入的指引來源 | `--json` |
| `copilot lsp list` | 列出語言伺服器 | `--json` |
| `copilot sandbox ca` | Sandbox 代理 CA | `status`、`create`、`trust`、`rotate`、`remove` |
| `copilot workflow run` | 執行已註冊的動態 workflow | `--args @input.json --result-file out.json` |
| `copilot sessions import` | 匯入語意化 Session JSONL | `--dry-run` |
| `copilot memories import` | 匯入 Memory JSONL | `--dry-run`、`--on-conflict skip` |
| `copilot completion` | Shell 補全腳本 | `bash`、`zsh`、`fish` |
| `copilot app` | 在目前目錄開啟 GitHub Copilot app | — |
| `copilot help 主題` | 說明主題 | `config`、`commands`、`environment`、`permissions`、`logging`、`billing`、`limits`、`monitoring`、`providers`、`sandbox` |

### A.2 Slash 指令

#### A.2.1 代理與模式

| 指令 | 用途 |
|------|------|
| `/plan [提示]` | 先建立實作計畫 |
| `/autopilot [目標]`（`/goal`） | 進入或重新聚焦 Autopilot，可加 `--max-ai-credits` |
| `/fleet [提示]` | 平行子代理 |
| `/delegate [提示]` | 交給 Copilot cloud agent 開草稿 PR；`--base` 指定目標分支 |
| `/agent [名稱]` | 瀏覽與選擇 custom agent |
| `/subagents`（`/agents`） | 設定子代理的模型與開關 |
| `/tasks` | 管理子代理與背景 shell |
| `/model [MODEL\|auto 層級]`（`/models`） | 選擇模型；`--global`、`--repo`、`--local` 決定寫入位置；`plan` 設定 Plan 模式模型 |
| `/research 主題` | 深度研究 |
| `/rubber-duck [提示]` | 不同模型的第二意見 |
| `/review [提示]` | 程式審查子代理 |
| `/security-review [提示]` | 本機變更的安全審查 |
| `/ask 問題`（`/btw`） | 不進入歷史的旁支問題 |
| `/refine 文字` | 改寫雜亂的提示 |

#### A.2.2 Session

| 指令 | 用途 |
|------|------|
| `/new [提示]`（`/clear`、`/reset`） | 新對話；`/new worktree` 在新 worktree 開始 |
| `/resume [ID]`（`/continue`） | 切換 Session |
| `/rename [名稱]` | 重新命名 |
| `/session [info\|checkpoints [n]\|files\|plan\|rename\|cleanup\|prune\|delete [ID]\|delete-all]`（`/sessions`） | Session 資訊與管理 |
| `/fork [名稱]`（`/branch`） | 複製 Session；`/fork worktree` 到新 worktree |
| `/worktree [分支\|任務]` | 建立 worktree 並切換（未 commit 的變更留在原處） |
| `/move [分支\|任務]` | 建立 worktree 並把未 commit 的變更帶過去 |
| `/rewind`（`/undo`） | 回溯對話與檔案 |
| `/compact [重點]` | 手動壓縮 |
| `/context` | context 用量 |
| `/usage` | 用量與 AI Credits |
| `/share [link\|off\|file\|html\|gist\|research]`（`/export`） | 分享或匯出 |
| `/copy` | 複製最後回應 |
| `/remote [on\|off]` | 遠端控制 |
| `/search [查詢]`（`/find`） | 搜尋 timeline（實驗） |
| `/chronicle <standup\|tips\|improve\|reindex\|skills ...>` | Session 歷史分析 |
| `/exit [print]`（`/quit`） | 離開 |
| `/restart` | 重新啟動並恢復存活的 Session |

#### A.2.3 權限與環境

| 指令 | 用途 |
|------|------|
| `/permissions [default\|assisted\|allow-all\|show\|reset]` | 核准模式 |
| `/allow-all [off\|auto\|show]`（`/yolo`） | 全部允許（`/permissions allow-all` 的別名） |
| `/reset-allowed-tools` | 清除本 Session 與目前位置的核准 |
| `/add-dir 路徑` | 加入可存取的目錄（並信任其 skills／agents） |
| `/list-dirs` | 列出允許的目錄 |
| `/cwd [路徑]`（`/cd`） | 切換或顯示工作目錄 |
| `/sandbox [config\|status\|policy [指令]\|enable\|disable]`、`/sandbox ca ...` | Sandbox |
| `/limits`、`/limits set max-ai-credits N`、`/limits unset` | Session 上限 |
| `/env` | 已載入的指引、MCP、skills、agents、hooks、plugins、LSP、extensions |
| `/instructions` | 檢視與開關指引檔 |

#### A.2.4 擴充

| 指令 | 用途 |
|------|------|
| `/mcp [config\|list\|show\|add\|edit\|delete\|disable\|enable\|auth\|reload\|search] [名稱]` | MCP 管理 |
| `/plugin`、`/plugin install\|update\|uninstall\|list\|marketplace ...` | Plugin 管理 |
| `/skills [list\|info\|add\|remove\|reload]` | Skill 管理 |
| `/lsp [show\|test\|reload\|logs\|help]` | LSP 管理 |
| `/extensions [manage\|mode]`（`/extension`） | Extension 管理（實驗） |
| `/init [suppress]` | 產生專案指引／隱藏提示 |

#### A.2.5 GitHub 與程式碼

| 指令 | 用途 |
|------|------|
| `/pr [view [web]\|create\|fix [feedback\|conflicts\|ci\|all]\|auto\|automerge]` | PR 生命週期 |
| `/diff` | 檢視變更並逐行留言 |
| `/ide` | 連線到 IDE 工作區 |

#### A.2.6 介面與其他

| 指令 | 用途 |
|------|------|
| `/settings [--repo\|--local] [show KEY\|KEY\|KEY VALUE]`（`/config`） | 設定 |
| `/theme`、`/statusline`（`/footer`）、`/vim`、`/voice`、`/terminal-setup` | 介面 |
| `/login`、`/logout`、`/user [show\|list\|switch]` | 帳號 |
| `/memory [on\|off]` | Memory 狀態與開關 |
| `/experimental [on\|off\|show]` | 實驗性功能 |
| `/every`、`/after` | 排程提示（實驗） |
| `/keep-alive`（`/caffeinate`） | 防止系統休眠 |
| `/computer` | Computer Use 開關（macOS、Windows 本機 Session） |
| `/changelog`（`/release-notes`）、`/version`、`/update`（`/upgrade`）、`/downgrade 版本` | 版本 |
| `/diagnose [提示]`、`/collect-debug-logs`、`/feedback`（`/bug`） | 疑難排解與回饋 |
| `/workflows` | 觀察動態 workflow 執行 |
| `/app` | 在 GitHub Copilot app 開啟目前 Session |
| `/help` | 說明 |

### A.3 快捷鍵

| 類別 | 快捷鍵 | 作用 |
|------|------|------|
| 全域 | <kbd>Shift</kbd>+<kbd>Tab</kbd> | 切換標準、Plan、Autopilot |
| 全域 | <kbd>Esc</kbd> | 取消；執行中按兩下中斷；閒置按兩下回溯 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>C</kbd> | 立即取消並清除佇列；連按兩下離開 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>D</kbd> | 關閉 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>Q</kbd>、<kbd>Ctrl</kbd>+<kbd>Enter</kbd> | 排入佇列 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>G</kbd>、<kbd>Ctrl</kbd>+<kbd>X</kbd> <kbd>e</kbd> | 外部編輯器撰寫提示 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>X</kbd> <kbd>/</kbd> | 輸入中途插入 slash 指令 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>X</kbd> <kbd>b</kbd> | 移到背景 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>X</kbd> <kbd>g</kbd>／<kbd>h</kbd>／<kbd>o</kbd>／<kbd>v</kbd>／<kbd>x</kbd> | Autopilot 面板／隱藏側欄／開啟最近連結／語音／關閉 Session |
| 全域 | <kbd>Ctrl</kbd>+<kbd>Space</kbd> | 語音聽寫 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>R</kbd> | 反向搜尋歷史 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>L</kbd> | 清除畫面 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>V</kbd>、<kbd>Alt</kbd>+<kbd>V</kbd> | 貼上為附件、貼上圖片 |
| 全域 | <kbd>Shift</kbd>+<kbd>Enter</kbd>（或 <kbd>Alt</kbd>／<kbd>Option</kbd>+<kbd>Enter</kbd>） | 換行 |
| 全域 | <kbd>Ctrl</kbd>+<kbd>Z</kbd> | 暫停到背景（Unix） |
| Timeline | <kbd>Ctrl</kbd>+<kbd>F</kbd>、<kbd>Ctrl</kbd>+<kbd>O</kbd>、<kbd>Ctrl</kbd>+<kbd>E</kbd>、<kbd>Ctrl</kbd>+<kbd>T</kbd> | 搜尋、展開最近、展開全部、推理內容 |
| 輸入 | <kbd>Ctrl</kbd>+<kbd>A</kbd>／<kbd>E</kbd>／<kbd>K</kbd>／<kbd>U</kbd>／<kbd>W</kbd> | 行首、行尾、刪到行尾、刪到行首、刪前一個字 |
| 輸入 | <kbd>↑</kbd>／<kbd>↓</kbd>、<kbd>Ctrl</kbd>+<kbd>P</kbd> | 歷史（空白輸入框的 ↑ 取回排隊提示）、不取回佇列的歷史瀏覽 |
| 輸入 | <kbd>Tab</kbd>、<kbd>Ctrl</kbd>+<kbd>Y</kbd> | 接受行內補全 |
| 核准 | <kbd>y</kbd>／<kbd>n</kbd>／<kbd>!</kbd>／<kbd>#</kbd>／<kbd>?</kbd> | 允許一次／拒絕一次／本 Session 全允許／本 Session 全拒絕／詳細資訊 |
| 側欄 | <kbd>←</kbd>／<kbd>→</kbd>、<kbd>n</kbd>、<kbd>x</kbd> <kbd>x</kbd>、<kbd>s</kbd> | 開關與焦點、新 Session、關閉、排序 |
| Diff | <kbd>c</kbd>、<kbd>s</kbd>、<kbd>b</kbd>、<kbd>w</kbd>、<kbd>Enter</kbd> | 留言、留言摘要、切換未 stage／分支 diff、隱藏空白變更、送出留言 |
| Tasks | <kbd>a</kbd>、<kbd>f</kbd>、<kbd>X</kbd>、<kbd>R</kbd>、<kbd>B</kbd> | 全部層級、顯示已完成、終止、移除、移到背景 |

### A.4 輸入前綴

| 前綴 | 作用 |
|------|------|
| `@` | 引用檔案 |
| `#` | 引用 Issue／PR |
| `!` | 直接執行 shell 指令（單獨輸入進入 shell 模式） |
| `$` | 單獨輸入並 Enter：交出終端機給互動式 shell |
| `&` | 等同 `/delegate` |
| `?` | 空白輸入框時開啟快速說明 |

---

## 附錄 B：命令列選項

> 來源：v1.0.97 `copilot --help`。標示「help 未列出」者出自官方 command reference 或 completion 腳本，並以 `copilot <旗標> --help` 確認本機接受（附錄 H.3）。

### B.1 執行模式與 Session

| 選項 | 說明 |
|------|------|
| `-p`、`--prompt <文字>` | 程式化執行後結束 |
| `-i`、`--interactive <提示>` | 啟動互動模式並自動執行提示 |
| `-s`、`--silent` | 只輸出代理回應 |
| `--mode <interactive\|plan\|autopilot>` | 起始模式 |
| `--plan` | 從 Plan 模式開始（與 `--mode autopilot` 合用為 plan-then-autopilot） |
| `--autopilot` | 從 Autopilot 開始 |
| `--max-autopilot-continues <N>` | Autopilot 延續上限（v1.0.97 help 顯示預設 5） |
| `--fleet` | 平行子代理（需搭配 `-i`、`-p` 或管線） |
| `--agent <代理>` | 指定 custom agent |
| `-r`、`--resume [<值>]` | 恢復 Session（ID、ID 前綴、任務 ID、名稱） |
| `--continue` | 恢復最近的 Session |
| `-n`、`--name <名稱>` | 新 Session 的名稱 |
| `--session-id <ID>` | 精確指定 Session 或任務 ID |
| `--connect [<ID>]` | 直接連到遠端 Session |
| `-w`、`--worktree [<名稱>]` | 在 worktree 中啟動（help 未列出） |
| `--cloud` | 在雲端 Sandbox 啟動（實驗；help 未列出） |
| `-C <目錄>` | 先切換工作目錄 |
| `--acp` | 以 ACP 伺服器啟動（另有 `--stdio`、`--port`） |
| `--experimental`、`--no-experimental` | 實驗性功能 |

### B.2 模型

| 選項 | 說明 |
|------|------|
| `--model <模型>` | 模型；`auto` 由 Copilot 選擇 |
| `--reasoning-effort <none\|minimal\|low\|medium\|high\|xhigh\|max>` | 推理強度（別名 `--effort`，help 未列出） |
| `--context <default\|long_context>` | context 層級 |
| `--auto-tier <層級>` | Auto 路由層級 |

### B.3 權限

| 選項 | 說明 |
|------|------|
| `--allow-tool [<工具>...]`、`--deny-tool [<工具>...]` | 允許／拒絕（deny 優先） |
| `--available-tools [<工具>...]`、`--excluded-tools [<工具>...]` | 模型可見的工具 |
| `--allow-all-tools` | 全部工具（環境變數 `COPILOT_ALLOW_ALL`） |
| `--allow-all-paths` | 停用路徑檢查 |
| `--allow-all-urls` | 全部網址 |
| `--allow-all`、`--yolo` | 以上三者 |
| `--allow-url [<網址>...]`、`--deny-url [<網址>...]` | 網址允許／拒絕 |
| `--add-dir <目錄>` | 加入可存取目錄（並信任其 skills／agents） |
| `--disallow-temp-dir` | 禁止自動存取系統暫存目錄 |
| `--assisted-approval` | Assisted 核准（需實驗性模式或 `AUTO_APPROVAL` 旗標） |
| `--no-ask-user` | 停用 `ask_user` 工具 |
| `--secret-env-vars [<變數>...]` | 從 shell／MCP 環境移除並遮蔽 |
| `--sandbox`、`--no-sandbox` | 本次啟用／停用本機 Sandbox（help 未列出；受管下限會覆寫 `--no-sandbox`） |
| `--max-ai-credits <N>` | AI Credits 上限（最少 30） |

### B.4 擴充

| 選項 | 說明 |
|------|------|
| `--additional-mcp-config <json\|@檔案>` | 本次額外的 MCP 伺服器 |
| `--disable-mcp-server <名稱>`、`--enable-mcp-server <名稱>` | 本次停用／暫時啟用 |
| `--disable-builtin-mcps` | 停用內建 MCP 伺服器 |
| `--enable-all-github-mcp-tools`、`--add-github-mcp-toolset <toolset>`、`--add-github-mcp-tool <工具>` | GitHub MCP 工具範圍 |
| `--mcp-github-auth <server=origin>` | 只把 GitHub 憑證送給指定的額外 MCP 伺服器與來源 |
| `--allow-all-mcp-server-instructions` | 載入所有 MCP 伺服器的初始化指示 |
| `--plugin-dir <目錄>` | 載入本機 plugin |
| `--extension-sdk-path <目錄>` | 覆寫 extension 使用的 SDK |
| `--no-custom-instructions` | 不載入指引檔 |
| `--enable-memory` | 程式化模式啟用 Memory |
| `--dynamic-retrieval <類別=on\|off>` | embeddings 動態檢索（目前類別：skills） |

### B.5 輸出、日誌與其他

| 選項 | 說明 |
|------|------|
| `--output-format <text\|json>` | json 為 JSONL |
| `--stream <on\|off>` | 串流輸出 |
| `--share [<路徑>]`、`--share-gist` | 程式化結束後匯出 |
| `--attachment <路徑>` | 附加檔案（程式化模式） |
| `--usage-output-file <檔案>` | 用量統計 JSON |
| `--log-dir <目錄>`、`--log-level <等級>` | 日誌 |
| `--remote`、`--no-remote`、`--remote-export`、`--no-remote-export` | 遠端控制與匯出 |
| `--no-auto-update` | 停止自動更新並使用安裝檔內建版本 |
| `--banner`、`--screen-reader`、`--plain-diff`、`--no-color`、`--mouse`／`--no-mouse`、`--bash-env`／`--no-bash-env` | 介面 |
| `--no-eager-powershell-resolution` | Windows 停用背景 PowerShell 解析 |
| `-v`、`--version`、`-h`、`--help` | 版本、說明 |

---

## 附錄 C：環境變數

> 來源：v1.0.97 `copilot help environment`、`copilot help providers`、`copilot help monitoring` 與官方 command reference。

### C.1 驗證與主機

| 變數 | 說明 |
|------|------|
| `COPILOT_GITHUB_TOKEN`、`GH_TOKEN`、`GITHUB_TOKEN` | 驗證 Token，依此順序優先，且優先於已存的登入 |
| `GH_HOST` | GitHub CLI 與 Copilot CLI 共用的主機名稱（`*.ghe.com`） |
| `COPILOT_GH_HOST` | 只給 Copilot CLI 的主機名稱，優先於 `GH_HOST` |
| `COPILOT_OFFLINE` | `true`：不連 GitHub，只連 BYOK 端點 |

### C.2 設定與行為

| 變數 | 說明 |
|------|------|
| `COPILOT_HOME` | 設定與狀態目錄（預設 `~/.copilot`） |
| `COPILOT_CACHE_HOME` | 快取目錄 |
| `COPILOT_MODEL` | 模型 |
| `COPILOT_AUTO_TIER` | Auto 路由層級（`efficiency`、`balance`、`intelligence`） |
| `COPILOT_ALLOW_ALL` | 自動核准工具；**只有精確的 `true` 會同時信任工作目錄** |
| `COPILOT_ASSISTED_APPROVAL` | Assisted 核准 |
| `COPILOT_PLAN_THEN_AUTOPILOT` | 等同 `--plan --mode autopilot` |
| `COPILOT_AUTO_UPDATE` | `false` 停止自動更新並使用內建版本；CI 中預設關閉 |
| `COPILOT_CLI_VERSION` | 覆寫更新比較用的版本號 |
| `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` | 額外的指引目錄（逗號分隔） |
| `COPILOT_SKILLS_DIRS` | 額外的 skill 目錄 |
| `COPILOT_EDITOR`、`VISUAL`、`EDITOR` | 編輯器（依此優先序） |
| `COPILOT_LARGE_OUTPUT_THRESHOLD_BYTES` | 工具輸出直接給模型的上限（預設 20480） |
| `COPILOT_TASK_WAIT_TIMEOUT_SECONDS` | `-p` 等待背景工作的秒數（預設 600） |
| `COPILOT_SUBAGENT_MAX_CONCURRENT`、`COPILOT_SUBAGENT_MAX_DEPTH` | 子代理上限（與設定鍵預設值的不一致見附錄 H.4） |
| `COPILOT_MCP_TOOL_CACHE` | `false` 停用 MCP 工具快照快取 |
| `COPILOT_ENABLE_INTERRUPTED_SESSION_RESTORE` | `1` 啟用中斷 Session 的恢復提示 |
| `COPILOT_ENABLE_HTTP2` | 啟用 HTTP/2 |
| `COPILOT_WEB_FETCH_ALLOW_LOCALHOST` | `1` 允許 `web_fetch` 連本機 |
| `COPILOT_HOOK_ALLOW_LOCALHOST` | `1` 允許 HTTP hook 使用本機 http |
| `COPILOT_MULTIPLEXER` | 覆寫終端多工器偵測（`tmux`、`herdr`、`none`） |
| `PLUGINS_DASHBOARD` | `false` 停用 plugins 儀表板與 `copilot plugin` 指令 |
| `PLAIN_DIFF`、`NO_COLOR` | 介面 |
| `USE_BUILTIN_RIPGREP`、`USE_TGREP`、`TGREP_FILE_COUNT_THRESHOLD`、`USE_TGREP_WARM_START` | 搜尋引擎（大型 Repo 自動使用 tgrep 索引） |

### C.3 程式化模式的信任開關

| 變數 | 說明 |
|------|------|
| `GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP` | `true`：`-p` 載入工作區 MCP |
| `GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS` | `true`：`-p` 載入 Repo hooks |
| `GITHUB_COPILOT_PROMPT_MODE_EXTENSIONS` | `true`：`-p` 載入專案 extensions |

### C.4 網路

| 變數 | 說明 |
|------|------|
| `HTTP_PROXY`、`HTTPS_PROXY`、`NO_PROXY`（大小寫皆可） | Proxy，優先於 `proxyUrl` 設定 |
| `COPILOT_PROXY_KERBEROS_SPN` | Kerberos Proxy 的 SPN |

### C.5 自訂模型（BYOK）

| 變數 | 說明 |
|------|------|
| `COPILOT_PROVIDER_BASE_URL` | 端點（設定後啟用 BYOK） |
| `COPILOT_PROVIDER_TYPE` | `openai`、`azure`、`anthropic` |
| `COPILOT_PROVIDER_API_KEY`、`COPILOT_PROVIDER_API_KEY_COMMAND`、`COPILOT_PROVIDER_BEARER_TOKEN` | 憑證 |
| `COPILOT_PROVIDER_WIRE_API`、`COPILOT_PROVIDER_TRANSPORT` | API 格式、傳輸方式 |
| `COPILOT_PROVIDER_AZURE_API_VERSION` | Azure API 版本 |
| `COPILOT_PROVIDER_MODEL_ID`、`COPILOT_PROVIDER_WIRE_MODEL` | 模型識別、送給供應商的模型名稱 |
| `COPILOT_PROVIDER_MAX_PROMPT_TOKENS`、`COPILOT_PROVIDER_MAX_OUTPUT_TOKENS` | token 上限 |
| `COPILOT_PROVIDER_HEADERS` | 只送給供應商的標頭 |
| `COPILOT_PROVIDERS_CONFIG` | 供應商與模型註冊檔 |

### C.6 OpenTelemetry

| 變數 | 說明 |
|------|------|
| `COPILOT_OTEL_ENABLED` | 啟用 |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP 端點（設定即啟用） |
| `COPILOT_OTEL_EXPORTER_TYPE` | `otlp-http`（預設）或 `file` |
| `COPILOT_OTEL_FILE_EXPORTER_PATH` | JSONL 檔路徑（設定即啟用） |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/json`（預設）或 `http/protobuf` |
| `OTEL_EXPORTER_OTLP_HEADERS` | 匯出器驗證標頭 |
| `OTEL_EXPORTER_OTLP_CERTIFICATE`、`OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE`、`OTEL_EXPORTER_OTLP_CLIENT_KEY` | 私有 CA 與 mTLS |
| `OTEL_SERVICE_NAME`、`OTEL_RESOURCE_ATTRIBUTES`、`COPILOT_OTEL_SOURCE_NAME` | 資源屬性 |
| `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT` | 擷取完整內容（預設 `false`） |
| `OTEL_LOG_LEVEL` | OTel 診斷日誌等級 |

---

## 附錄 D：設定檔與設定鍵

### D.1 `~/.copilot` 目錄結構

| 路徑 | 類型 | 說明 | 可否刪除 |
|------|------|------|------|
| `settings.json` | 使用者編輯 | 個人設定（支援 JSONC 註解） | 小心：會重置所有偏好 |
| `copilot-instructions.md`、`instructions/` | 使用者編輯 | 個人指引 | 不建議（先備份） |
| `mcp-config.json` | 使用者編輯 | 使用者層級 MCP | 不建議 |
| `lsp-config.json` | 使用者編輯 | 使用者層級 LSP | 不建議 |
| `providers.json` | 使用者編輯 | BYOK 供應商與模型註冊 | 不建議 |
| `agents/`、`skills/`、`hooks/`、`extensions/` | 使用者編輯 | 個人代理、skills、hooks、extensions | 不建議 |
| `config.json` | 自動管理 | 驗證、已安裝 plugins、受信任資料夾等內部狀態；**不再讀取使用者設定** | 小心：需重新登入 |
| `permissions-config.json` | 自動管理 | 各位置的已儲存核准 | 小心：所有核准重置 |
| `session-state/` | 自動管理 | Session 歷史 | 小心：無法再恢復 |
| `session-store.db` | 自動管理 | 跨 Session 索引（可 `/chronicle reindex` 重建） | 小心 |
| `command-history-state/` | 自動管理 | 指令歷史 | 小心 |
| `logs/` | 自動管理 | `process-{timestamp}-{pid}.log` | 可以 |
| `installed-plugins/`、`plugin-data/` | 自動管理 | Plugin 檔案與資料 | 用 `copilot plugin uninstall`；`plugin-data/` 可刪 |
| `ide/`、`mcp-oauth-config/`、`mcp-secrets/` | 自動管理 | IDE 狀態、MCP OAuth 與密鑰的備援儲存 | 小心：可能需重新驗證 |

### D.2 Repo 層級檔案

| 路徑 | 用途 | 章節 |
|------|------|------|
| `.github/copilot-instructions.md` | Repo 全域指引 | 第 6 章 |
| `.github/instructions/**/*.instructions.md` | 路徑專屬指引 | 第 6 章 |
| `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.claude/rules/**/*.md` | 跨工具指引 | 第 6 章 |
| `.github/agents/*.agent.md`、`.claude/agents/` | Custom agents | 第 6 章 |
| `.github/skills/*/SKILL.md`、`.agents/skills/`、`.claude/skills/` | Skills | 第 10 章 |
| `.github/hooks/*.json` | Hooks | 第 11 章 |
| `.github/mcp.json`、`.mcp.json` | MCP 伺服器 | 第 9 章 |
| `.github/lsp.json` | LSP | 第 12 章 |
| `.github/extensions/*/extension.mjs` | Extensions | 第 10 章 |
| `.github/copilot/settings.json` | Repo 設定（commit） | D.4 |
| `.github/copilot/settings.local.json` | 個人覆寫（加入 `.gitignore`） | D.4 |
| `.github/allowed_models.txt` | Repo 模型白名單 | D.5 |
| `.github/plugin/marketplace.json` | Plugin marketplace 索引 | 第 10 章 |

### D.3 使用者設定鍵（`~/.copilot/settings.json`）

常用鍵（完整清單以 `copilot help config` 為準，本手冊擷取 99 個鍵供 `check_config.py` 使用）：

| 類別 | 鍵 | 預設 | 說明 |
|------|------|------|------|
| 模型 | `model` | 依方案 | 預設模型；`auto` 由 Copilot 選擇 |
| | `autoTier` | 未設定 | `efficiency`、`balance`、`intelligence` |
| | `effortLevel` | `"medium"` | 推理強度 |
| | `contextTier` | — | `default` 或 `long_context` |
| | `continueOnAutoMode` | `false` | 被限速時自動切到 Auto |
| | `subagents.agents`、`subagents.disabledSubagents`、`subagents.maxConcurrency`、`subagents.maxDepth` | — | 子代理設定 |
| 模式與權限 | `defaultMode` | `"interactive"` | 新 Session 的起始模式 |
| | `defaultPermissionMode` | `"manual"` | `manual`、`assisted`、`allow-all` |
| | `stayInAutopilot` | `true` | 任務完成後停留在 Autopilot |
| | `askUser` | `true` | 允許代理提問 |
| | `allowedUrls`、`deniedUrls` | `[]` | 網址允許／拒絕 |
| | `permissions.disableBypassPermissionsMode` | — | `disable` 或 `allow-auto-only` |
| Sandbox | `sandbox.*` | 見第 14 章 | 只能在使用者或受管設定中設定 |
| 擴充 | `enabledPlugins`、`extraKnownMarketplaces` | `{}` | 宣告式 plugin 安裝 |
| | `disabledMcpServers`、`enabledMcpServers`、`disabledSkills` | `[]` | 停用／啟用 |
| | `skillDirectories`、`ignoredSkillsLocations` | `[]` | Skill 搜尋路徑 |
| | `hooks`、`disableAllHooks` | — | 內嵌 hooks、停用所有 hooks |
| | `customAgents.defaultLocalOnly` | `false` | 只用本機 custom agents |
| | `toolSearch`、`dynamicRetrieval` | 依功能 | 延遲載入工具、embeddings 檢索 |
| 更新 | `autoUpdate` | `true` | 自動下載新版與更新首方 plugins |
| | `autoUpdatesChannel` | `"stable"` | `stable` 或 `prerelease` |
| Git | `includeCoAuthoredBy` | `true` | commit 加上 `Co-authored-by` |
| | `mergeStrategy` | — | `/pr fix conflicts` 用 `rebase` 或 `merge` |
| | `worktreeBaseRef`、`worktreePathTemplate` | `"head"`、未設定 | worktree 基準與位置 |
| 網路 | `proxyUrl`、`proxyKerberosServicePrincipal` | — | Proxy |
| 隱私與同步 | `memory` | `true` | Copilot Memory |
| | `remote`、`remoteExport` | `"on"`、`true` | Session 同步與遠端控制 |
| | `storeTokenPlaintext` | `false` | 無鑰匙圈時允許明文存放 Token |
| 介面 | `theme`、`banner`、`bannerStyle`、`footer.*`、`statusLine`、`tabs.*`、`editorMode`、`transcriptView`、`renderMarkdown`、`mouse`、`notifications`、`beep` 等 | — | 介面偏好 |
| Windows | `powershellFlags`、`taskbarPresence` | `["-NoProfile","-NoLogo"]`、`true` | PowerShell 參數、工作列狀態 |

### D.4 Repo 設定鍵（`.github/copilot/settings.json`）

**只有下列 14 個鍵有效**，其他鍵（包括合法的使用者鍵）會被**靜默忽略**：

| 鍵 | 合併方式 |
|------|------|
| `companyAnnouncements` | 取代：Repo 優先 |
| `contextTier` | 取代：Repo 優先（需資料夾受信任） |
| `deniedUrls` | 聯集：Repo 只能新增，不能移除 |
| `disableAllHooks` | Repo 優先 |
| `disabledMcpServers` | 聯集 |
| `disabledSkills` | 聯集 |
| `effortLevel` | 取代：Repo 優先（需資料夾受信任） |
| `enabledPlugins` | 合併：同鍵以 Repo 為準 |
| `extraKnownMarketplaces` | 合併：同鍵以 Repo 為準（Repo 層級的 `autoUpdate: true` 目前被忽略） |
| `hooks` | 合併：同鍵以 Repo 為準 |
| `includeCoAuthoredBy` | 取代：Repo 優先 |
| `mergeStrategy` | 取代：Repo 優先 |
| `model` | 取代：Repo 優先（需資料夾受信任） |
| `respectGitignore` | 只能收緊：Repo 可以啟用，不能停用 |

範例：

```json
{
  "companyAnnouncements": [
    "提醒：AI 產出的程式碼必須經過人工 Code Review 才能合併。"
  ],
  "model": "claude-sonnet-5.5",
  "effortLevel": "medium",
  "includeCoAuthoredBy": true,
  "deniedUrls": ["pastebin.com", "*.ngrok.io"],
  "disabledMcpServers": ["playwright"],
  "respectGitignore": true,
  "mergeStrategy": "rebase"
}
```

`.github/copilot/settings.local.json` 使用相同的結構並優先於 Repo 設定。CLI 也會讀取 `.claude/settings.json`、`.claude/settings.local.json` 中的跨工具子集（`companyAnnouncements`、`disableAllHooks`、`enabledPlugins`、`extraKnownMarketplaces`、`hooks`）。

### D.5 Repo 模型白名單（`.github/allowed_models.txt`）

```text
# 本 Repo 允許的內建模型（BYOK 模型不受此檔限制）
fallback: claude-sonnet-5.5
claude-sonnet-5.5
claude-opus-5.5
claude-haiku-*
gpt-5.4
gpt-6-*
```

| 規則 | 說明 |
|------|------|
| `模型 ID` 或 glob | 允許符合的內建模型；沒有檔案時等於 `*` |
| `fallback: 模型 ID` | **必須剛好一次**；必須是完整 ID（不能是 glob），而且本身要符合某條允許規則 |
| `#` | 註解 |
| 不支援 | 否定規則（`!pattern`） |
| 不影響 | BYOK 模型 |

CLI 在 `/cd` 時重新評估，檔案無效時會在執行前報錯。檢查：`python check_config.py models .github/allowed_models.txt`。

### D.6 受管設定

受管設定的位置、支援的鍵與範例見[第 15 章](#第-15-章企業治理與稽核)；檢查：`python check_config.py managed-settings managed-settings.json`。

---

## 附錄 E：Prompt 範本

> 每個範本都遵循第 20 章的結構：目標、背景、需求、限制、完成條件、輸出。`<...>` 為需要替換的內容。

### E.1 新增 API（Plan 模式）

```text
/plan 在 <模組> 新增 <資源> API：
背景：@<既有的類似 controller>、遵守 .github/copilot-instructions.md
需求：
1. 端點：<方法 路徑>…
2. 驗證規則：<欄位與規則>
3. 錯誤：<情境> 回 <狀態碼> Problem Details
限制：不修改既有 Flyway 遷移檔；不新增依賴；不改公開 API 的既有欄位
完成條件：每個端點有成功、驗證失敗、找不到資源三種 @WebMvcTest；./mvnw -q verify 通過
輸出：計畫中列出要新增與修改的檔案
```

### E.2 修 Bug

```text
#<Issue 編號>：<症狀>
相關檔案：@<檔案>
請依序：
1. 寫一個能重現問題的失敗測試，執行並貼出失敗輸出
2. 說明根因（指出檔案與行號）
3. 修正，不修改既有測試的斷言
4. 重跑測試並貼出通過的輸出
限制：只修改與根因相關的檔案
```

### E.3 程式審查

```text
/review 比較 origin/main...HEAD 的變更。
重點：並發與交易邊界、輸入驗證、錯誤處理、遺漏的測試。
每個發現列出：檔案:行號、問題、為什麼是問題、建議修正。
不要評論命名與排版。沒有把握的不要列。
```

### E.4 建立 PR

```text
/pr create 目標分支 <分支>；標題使用 Conventional Commits；
描述依照 PR 範本，包含：變更摘要、修改的檔案、實際執行過的驗證指令與結果、部署與回滾注意事項。
沒有執行過的測試不要寫結果。
```

### E.5 CI/CD 設定

```text
為這個 Repo 建立 GitHub Actions workflow：PR 時執行 ./mvnw -q verify 與 spotless:check。
限制：permissions 只給 contents: read；不使用 pull_request_target；actions 版本以大版本標籤固定；
加上 concurrency 取消同一 PR 的舊執行；timeout-minutes 15。
完成後執行 actionlint 並貼出結果。
```

### E.6 資料庫遷移

```text
/db-migration 在 orders 表新增 cancel_reason（varchar 200，可為 NULL）與 cancelled_at（timestamptz）。
同時為 (status, cancelled_at) 建立索引；orders 約 2,000 萬筆。
依 skill 規則完成，並貼出 flyway:validate 與遷移整合測試的輸出。
```

### E.7 陌生程式庫導覽

```text
我剛加入這個專案。請在不修改任何檔案的前提下：
1. 用 5 句話說明系統做什麼、主要模組
2. 畫出一個請求從 controller 到資料庫的流程（列出實際檔案）
3. 列出建置、測試、本機啟動的指令（從專案檔中找證據，不要猜）
4. 指出你認為最需要注意的 3 個技術債，附檔案位置
```

### E.8 大規模機械式修改（Autopilot）

```text
目標：把 src/main/java 下所有使用 java.util.Date 的地方改為 java.time。
步驟：先執行 grep 產生清單寫入 migration-checklist.md，逐一修改並勾選，
每完成一個套件執行 ./mvnw -q -pl <模組> test。
限制：不修改公開 API 簽章（若必須修改，記錄在 checklist 並跳過）；不修改測試斷言的預期值。
完成條件：checklist 全部勾選或註明跳過原因；./mvnw -q verify 通過。
```

---

## 附錄 F：版本里程碑與已移除項目

> 本附錄每一列都以 [changelog.md](https://github.com/github/copilot-cli/blob/main/changelog.md) 的版本標題日期與條目逐一核對（2026-10-14）。v1 手冊的里程碑表有多處日期誤差一天以上（例如 v1.0.15 實為 2026-04-01、v1.0.22 實為 04-09、v1.0.35 實為 04-23），已全部以 changelog 為準重建。

### F.1 版本里程碑

| 版本 | 日期 | 重點 |
|------|------|------|
| v0.0.329 | 2025-09-29 | 支援 Claude Sonnet 4.5；新增 `/model` |
| v0.0.353 | 2025-10-28 | Custom agents；`/delegate` |
| v0.0.374 | 2026-01-02 | 自動壓縮與 `/compact`；內建子代理；`web_fetch` |
| v0.0.387 | 2026-01-20 | Plan 模式；`ask_user` 工具 |
| v0.0.400 | 2026-01-30 | MCP 伺服器指示；`/theme` |
| v0.0.411 | 2026-02-17 | Claude Sonnet 4.6 |
| **v0.0.418** | **2026-02-25** | **正式 GA** |
| v0.0.423 | 2026-03-06 | 修正 CVE-2026-29783（唯讀指令判斷可被 bash 參數展開繞過） |
| **v1.0.2** | **2026-03-06** | 主版號升為 1.0；hook 支援跨平台 `command` 欄位與 `timeout` 別名 |
| v1.0.3 | 2026-03-09 | Extensions（實驗）；`/restart` |
| v1.0.25 | 2026-04-13 | 從 MCP Registry 安裝；`/env` |
| v1.0.49 | 2026-05-18 | `postToolUse` 的 `additionalContext` 會注入給模型；支援 Alpine Linux |
| v1.0.55 | 2026-05-28 | Free／Student 用量計費限 Auto 模型；Claude Opus 4.8 |
| v1.0.58 | 2026-06-02 | Rubber Duck 預設啟用；`/every`、`/after`（實驗） |
| v1.0.66 | 2026-06-30 | Claude Opus 4.8 Fast，棄用 Opus 4.6 Fast |
| v1.0.70 | 2026-07-09 | GPT-5.6 |
| v1.0.75 | 2026-07-24 | Claude Opus 5 |
| v1.0.79 | 2026-08-10 | 企業 `allow-auto-only` 政策；`--plan --mode autopilot`；Sessions 分頁與側欄 |
| v1.0.80 | 2026-08-14 | 模型設定更新（v1 手冊的基準版本） |
| v1.0.81 | 2026-08-27 | Plugins 儀表板開放所有人；移除 `/plugins`；MCP 2026-07-28 規格；hooks 取得 `traceparent`；`defaultMode`、`defaultPermissionMode`、`copilot app`、`login --with-token` |
| v1.0.82 | 2026-08-29 | 顯示具體的驗證失敗原因 |
| v1.0.83 | 2026-09-04 | Windows 11 工作列狀態；MCP OAuth CIMD；agent `models` 清單與 `model-policy`；Claude Fable 5.1；`forceLoginOrgs`；HTTPS Proxy mTLS |
| v1.0.85 | 2026-09-16 | Vim 模式開放所有人；`/config` 側欄；指令列改為 Rust 文法；`copilot instruction list`、`copilot lsp list`；`copilot plugin\|mcp\|skill enable/disable`；GPT-6 Astra |
| v1.0.86 | 2026-09-17 | Custom agent `include-custom-instructions` |
| v1.0.87 | 2026-09-21 | 受管 Auto 層級預設；`worktreePathTemplate`；MCP `slowConnectionThresholdMs` |
| v1.0.88 | 2026-09-22 | OSC 777 終端通知；受管設定套用到 ACP／AHP／server 模式；hooks 預設在專案根目錄執行 |
| v1.0.89 | 2026-09-28 | `.claude/rules` 指引；PR 遵循範本；Claude Opus 5.5、GPT-6 Sol／Luna；移除 Auto 的 Fast 層級 |
| v1.0.90 | 2026-09-30 | GPT-6.1 Sol；`--mcp-github-auth`；Session 範圍的唯讀目錄核准 |
| v1.0.91 | 2026-10-01 | `copilot sandbox ca` |
| v1.0.92 | 2026-10-05 | `copilot config` 子指令；開始前以 <kbd>Ctrl</kbd>+<kbd>E</kbd> 選擇本機或雲端；Sandbox shell 不再取得環境中的 `GITHUB_TOKEN` |
| v1.0.93 | 2026-10-07 | 受管 `permissions.limitTo`；**本機 Sandbox 開放所有使用者**；MCP 設定變更免重啟；**使用者設定只讀 `settings.json`** |
| v1.0.94 | 2026-10-08 | Claude Haiku 5.5；受管政策可停用 Assisted Permissions |
| v1.0.95 | 2026-10-09 | macOS 原生 Entra broker 驗證；`copilot config` 支援 Sandbox 憑證注入主機 |
| v1.0.96 | 2026-10-12 | Sandbox 設定會提示可能的環境密鑰；`/add-dir` 授予 Sandbox 存取；timeline 標示權限決策來源 |
| **v1.0.97** | **2026-10-13** | **本手冊基準**：agent 範圍 hooks；Autopilot 中 `ask` 視為拒絕；TLS 攔截 Proxy 串流修正；`--output-format json` 安全遮蔽密鑰；inline 圖片預設開啟 |

### F.2 已移除、改名與行為變更

| 項目 | 版本 | 替代或說明 |
|------|------|------|
| `--disable-parallel-tools-execution`、`parallel_tool_execution` | v0.0.418 | 已移除 |
| `--binary-version` | v1.0.3 新增，v1.0.97 已不在 completion 文法中 | 使用 `copilot --version` |
| `/plugins`（已移除） | v1.0.81 | 改用 `/plugin`、`/mcp`、`/skills`、`/subagents`、`/instructions` |
| `PLUGINS_DASHBOARD` 的退出選項與舊 skills 選擇器 | v1.0.81 | 儀表板固定開啟（command reference 仍列出此變數，可停用儀表板與 `copilot plugin` 指令） |
| Auto 的 `fast` 層級 | v1.0.89 | 退回 `balance` |
| `copilot plugins install --skill [--scope project]` | v1.0.85 | `copilot skill add [--project]` |
| `copilot plugins` 的 `--kind`、`--scope`、`--mcp`、`--skill` | v1.0.85 | `copilot mcp`、`copilot skill` |
| `copilot plugins list --kind instruction\|lsp` | v1.0.85 | `copilot instruction list`、`copilot lsp list` |
| `copilot plugins list --json` 的 `{plugins, errors}` 結構 | v1.0.85 | 改為扁平陣列 |
| `/sandbox ca install` | v1.0.91 | `create`＋`trust` |
| `~/.copilot/config.json` 中的使用者設定 | v1.0.93 | 搬到 `~/.copilot/settings.json` |
| `sandbox.gitAuth`、`sandbox.ghAuth` | — | `sandbox.auth.git`、`sandbox.auth.gh`（舊鍵被忽略、無自動遷移） |
| `allowDevToolCaches` | — | `allowDevToolAccess` |
| `--config-dir` | 已棄用 | `COPILOT_HOME` |
| `colorMode` | 已棄用別名 | `theme` |
| `/worktree new` | 已棄用 | `/new worktree` |
| `--enable-reasoning-summaries` | 已棄用（接受但忽略） | <kbd>Ctrl</kbd>+<kbd>T</kbd> 切換推理顯示 |
| `.vscode/mcp.json` | 不讀取 | `.github/mcp.json` 或 `.mcp.json` |
| Premium Requests 計費 | 2026-06 | AI Credits（舊計費平台帳戶仍顯示 premium requests） |

---

## 附錄 G：檢查清單

### G.1 開發者入門

- [ ] 確認有 Copilot 授權，組織已啟用 Copilot CLI 政策
- [ ] 安裝並確認版本：`copilot --version`（第 3 章）
- [ ] 確認環境中沒有不打算使用的 `GH_TOKEN`／`GITHUB_TOKEN`，登入後以 `/user` 確認帳號與驗證來源
- [ ] 只在專案目錄啟動，不受信任的 Repo 不選擇永久信任
- [ ] 執行 `/terminal-setup` 與 `copilot completion`
- [ ] 以 `/statusline` 顯示 `quota` 與 `ai-used`
- [ ] 練習 <kbd>Shift</kbd>+<kbd>Tab</kbd> 三種模式、<kbd>Esc</kbd> 取消與回溯（第 4 章）
- [ ] 讀過第 21 章的審查五問

### G.2 Repo 設定

- [ ] `.github/copilot-instructions.md`：建置／測試指令、可驗證的架構規則（第 6 章）
- [ ] 必要時的路徑專屬指引 `.github/instructions/*.instructions.md`（含 `applyTo`）
- [ ] `.github/hooks/` 安全政策＋Bash 與 PowerShell 兩版腳本，並通過 hook 測試（第 11 章）
- [ ] `.github/copilot/settings.json`：`model`、`deniedUrls`、`mergeStrategy` 等（只用 14 個 Repo 鍵）
- [ ] `.github/mcp.json`：固定版本、`${ENV}` 參照密鑰、最小工具（第 9 章）
- [ ] 需要時的 `.github/agents/`、`.github/skills/`、`.github/lsp.json`
- [ ] `.gitignore` 加入 `.github/copilot/settings.local.json` 與 hook 稽核日誌目錄
- [ ] CI 執行 `check_config.py`（第 21 章）
- [ ] 分支保護：必要的人工 review 與狀態檢查

### G.3 安全

- [ ] 受管設定 `permissions.disableBypassPermissionsMode`（`disable` 或 `allow-auto-only`）
- [ ] 受管設定 `sandbox`（至少 `enabled: true`），確認目標作業系統支援
- [ ] `deniedPaths` 或受管 `Read(...)` deny 保護 `~/.ssh`、`~/.aws`、`~/.kube`、`.env`
- [ ] 受管 MCP allowlist 或企業 MCP allowlist
- [ ] `strictKnownMarketplaces` 限制 plugin 來源
- [ ] `remoteControl.mode` 設為 `requireSSO` 或 `disabled`
- [ ] Policy hooks 進行集中稽核（只記錄中繼資料）
- [ ] 不受信任的 Repo：先檢查 `.mcp.json`、`.github/mcp.json`、`.github/hooks/`、`.github/extensions/` 再信任
- [ ] CI：不在 fork PR 上執行、最小權限、固定版本、不使用 `--allow-all`
- [ ] 維持在含安全修正的版本

### G.4 每日使用

- [ ] 一個 Session 一個主題，名稱有意義
- [ ] 複雜任務先 Plan，**審查計畫後**才實作
- [ ] 用 `@`、`#` 給精準 context
- [ ] 核准對話框中仔細看指令，破壞性指令逐次核准
- [ ] 要求代理貼出驗證指令的輸出，並自己重跑
- [ ] `/diff` 與 `git diff` 審查變更，特別是測試、依賴與 `.github/` 的變更
- [ ] 留意 `/usage` 與 `/context`
- [ ] 重要決策寫進檔案，不只留在對話中

### G.5 企業管理者

- [ ] 企業／組織的 Copilot CLI 政策與 cloud agent 政策（`/delegate` 需要兩者）
- [ ] 模型啟用政策與企業自訂模型
- [ ] 部署 MDM／檔案受管設定，Linux 檔案權限正確（root 擁有、不可他人寫入）
- [ ] 預算：使用者、cost center、組織、企業支出上限；決定是否允許超額
- [ ] Actions 計入組織的政策（`GITHUB_TOKEN`）與 cost center
- [ ] 稽核：audit log、集中式 hook 日誌、OTel
- [ ] 內部 plugin marketplace 與標準 Repo 範本
- [ ] 版本管理：分 Ring 升級與回歸驗證（第 18 章）

### G.6 版本升級

- [ ] 閱讀 changelog（`/changelog since <目前版本>`），標出 Remove／Replace／renamed
- [ ] 重新擷取 `copilot --help`、`help config`、`help environment` 並與舊版比對
- [ ] 更新 `check_flags.py` 的清單並重跑
- [ ] 重跑 `check_config.py` 與 hook 測試
- [ ] 在拋棄式 Repo 執行一次 CI workflow
- [ ] 更新團隊文件中的版本號與變更

---

## 附錄 H：查證紀錄

> 本附錄記錄 v2.0 的查證基準、參考來源、相對 v1 的更正、實際執行的驗證與尚待確認的項目。下次更新時請從 H.4 開始。

### H.1 查證基準與參考來源

| 項目 | 內容 |
|------|------|
| 查證日期 | 2026-10-14 |
| 產品版本 | Copilot CLI v1.0.97（2026-10-13，最新穩定版；當日另有 v1.0.98 預發佈版） |
| 本機環境 | Windows 11 Pro、Copilot CLI 1.0.97、Git Bash、PowerShell 7、Python 3.12、jq 1.8.1、actionlint 1.7.12、Hugo |
| 本機 help 擷取 | `copilot --help`、`help config／environment／commands／permissions／logging／billing／limits／monitoring／providers／sandbox`、全部子指令的 `--help`、`copilot completion bash` |

主要來源：

| 來源 | 用途 |
|------|------|
| [github.com/features/copilot/cli](https://github.com/features/copilot/cli) | 產品定位與方案涵蓋範圍 |
| [github/copilot-cli](https://github.com/github/copilot-cli) README 與 [changelog.md](https://github.com/github/copilot-cli/blob/main/changelog.md) | 安裝方式、v0.0.329～v1.0.97 變更 |
| docs.github.com Copilot CLI 文件（concepts、how-tos、reference 共 76 頁，以 `/api/article/body` 取得原始 Markdown） | 全書事實依據 |
| [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) | 旗標、slash 指令、快捷鍵、權限樣式、環境變數、內建代理 |
| [CLI configuration directory](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference) | `~/.copilot` 結構、設定鍵、受管設定 |
| [Hooks reference](https://docs.github.com/en/copilot/reference/hooks-configuration) 與 [hooks 教學](https://docs.github.com/en/copilot/tutorials/copilot-cli-hooks) | 第 11 章 |
| [Plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) | 第 10 章 |
| [Programmatic reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference)、[Actions 自動化](https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions) | 第 16 章 |
| [About cloud and local sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes) | 第 14 章 |
| [Models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)、個人與組織的用量計費頁 | 第 17 章 |
| [CVE-2026-29783（Tenable）](https://www.tenable.com/cve/CVE-2026-29783) | 第 13、15 章 |
| [PromptArmor：Copilot CLI downloads and executes malware](https://www.promptarmor.com/resources/github-copilot-cli-downloads-and-executes-malware) | 第 15 章 |
| [The Register：Adversa AI 研究報導](https://www.theregister.com/a/5301206) | 第 15 章 |

### H.2 v1 → v2 更正清單

| # | v1 內容 | v2 更正 | 依據 |
|------|------|------|------|
| 1 | 基準 v1.0.80（2026-08-14） | v1.0.97（2026-10-13） | changelog、本機 `--version` |
| 2 | Hook 設定沒有 `"version": 1` | 必須有，否則整檔被拒 | hooks reference；`check_config.py` 反向範例 |
| 3 | Hook `"matcher": "shell"`、`"permission": "deny"` | 工具名稱為 `bash`／`powershell`；沒有 `permission` 欄位，由腳本輸出 `permissionDecision` | hooks reference |
| 4 | Hook 從環境變數 `TOOL_INPUT`、`TOOL_NAME`、`FILE_PATH` 讀取 | 輸入是 stdin 的 JSON | hooks reference、教學腳本 |
| 5 | JSON 範例首行有 `//` 註解 | JSON 不允許註解 | JSON 規格 |
| 6 | 「v1.0.22 起 `.mcp.json` 是唯一工作區 MCP 設定檔」 | 另支援 `.github/mcp.json`（官方建議共用設定放此） | Adding MCP servers、command reference |
| 7 | 引用第三方：「Content Exclusions 不涵蓋 CLI」 | 官方明載內容排除會套用到 CLI（但不等於 shell 讀不到檔案） | About Copilot CLI、Administering Copilot CLI |
| 8 | `--binary-version` | v1.0.97 不存在，用 `--version` | completion 文法、`check_flags.py --probe` |
| 9 | GitHub MCP `--read-only` 旗標 | v1.0.97 不存在 | completion 文法 |
| 10 | `/new-worktree` | 不存在；用 `/new worktree` | `copilot help commands` |
| 11 | `/plugins`（含精細啟停） | v1.0.81 移除 | changelog |
| 12 | 「v1.0.29 新增 Nightly 發佈頻道」 | 只有 stable 與 prerelease | `copilot update --help`；changelog 1.0.29 無此條目 |
| 13 | 使用者設定 `~/.copilot/config.json` | v1.0.93 起只讀 `settings.json` | changelog、config-dir reference |
| 14 | Plugin 預設 marketplace 有多個 | v1.0.97 內建一個：`awesome-copilot` | `copilot plugin --help` |
| 15 | 版本里程碑多處日期誤差（如 v1.0.15 寫 03-28，實為 04-01） | 依 changelog 重建 | changelog |
| 16 | 自動壓縮「達到 95% 時」 | 約 80% 開始背景壓縮，約 95% 等待完成 | Managing context 文件 |
| 17 | Homebrew `brew install copilot-cli` | 官方文件為 `brew install --cask copilot-cli` | Installing Copilot CLI |
| 18 | 驗證優先序只列 `GH_TOKEN`、`GITHUB_TOKEN` | `COPILOT_GITHUB_TOKEN` → `GH_TOKEN` → `GITHUB_TOKEN` → 鑰匙圈 → `gh` | Authenticating 文件、`help environment` |
| 19 | 方案表無 Max；Business／Enterprise 額度未明 | Pro 1,500、Pro+ 7,000、Max 20,000；Business 1,900／人、Enterprise 3,900／人（共用池） | 用量計費文件 |
| 20 | 案例程式碼直接當作範例 | 改為審查練習並指出問題（`@Data` Entity、對 mock 斷言、Boot 3 的 `@EnableBatchProcessing`、`RunIdIncrementer` 與可重啟矛盾、無界執行緒） | 第 19 章 |
| 21 | 引用 Gartner、Maxim AI、Checkmarx、GitGuardian 統計等無法重新查證的說法 | 移除；只保留可查證的 CVE 與原始研究 | 第 15 章 |
| 22 | `/permissions reset` 與 `/reset-allowed-tools` 視為相同 | 後者另清除目前位置的已儲存核准 | Allowing tools 文件 |
| 23 | 多重 H1、目錄只到第二層、案例與檢查清單未收錄於目錄 | 單一 H1、三層目錄（## → ### → ####）、TOC 自動產生 | 本次重編 |

### H.3 已執行的驗證

| 驗證 | 方法 | 結果 |
|------|------|------|
| Hook 腳本（Bash＋PowerShell） | `test_hooks.sh`：13 組 preToolUse 輸入 × 2 版本＋2 組 postToolUse | PASS=28 FAIL=0 |
| 設定檔檢查器 | `run_checks.sh`：12 個正向範例、8 個反向範例 | 符合預期 20，不符合 0 |
| GitHub Actions workflow | actionlint 1.7.12 | 只有 `copilot-requests` 權限範圍的已知誤報，排除後 0 錯誤 |
| 隱藏旗標 | `copilot <旗標> --help`：`--sandbox`、`--no-sandbox`、`--cloud`、`--effort`、`--worktree`、`--config-dir`、`--prefer-version` 等皆接受；`--bogus-flag` 回 `unexpected argument` | 符合預期 |
| 手冊旗標與指令 | `check_flags.py`（對 v2 全文） | 旗標 91 次、子指令 65 次、slash 指令 447 次，0 個問題 |
| v1 手冊旗標與指令 | `check_flags.py`（對 v1 全文） | 13 個問題（見 H.2 #8～#11） |
| 程式碼區塊 | `extract_blocks.py`：JSON 解析、YAML 解析、`bash -n` | bash 44、json 13、yaml 3、powershell 3 個區塊全部通過（java 4、python 2、typescript 1、markdown 4、text 34 個區塊未執行） |
| Mermaid 圖表 | mermaid-cli 11.17.0（與網站載入的 mermaid@11 同大版本）逐一渲染 | 8 張全部渲染成功，沒有 Syntax error |
| 目錄與錨點 | 見 H.5 | — |

### H.4 尚待確認的項目

| # | 項目 | 原因 |
|------|------|------|
| 1 | 實際執行 `copilot -p`（含 `--output-format json` 的事件結構、`-p` 的結束碼） | 本次依使用者決定只做離線驗證，不消耗 AI Credits |
| 2 | `--max-autopilot-continues` 預設值 | 本機 help 顯示 5；command reference 寫「預設無限制」 |
| 3 | `--max-ai-credits` 的計算範圍 | command reference 寫「每個回應」；`help limits` 與 session limit 頁面寫「整個 Session 累計」 |
| 4 | 子代理深度預設 | 設定鍵表為 6；環境變數表 `COPILOT_SUBAGENT_MAX_DEPTH` 為 4 |
| 5 | 內建 MCP 伺服器清單 | 本機 help 列 `github-mcp-server`、`githubiq`；command reference 另列 `playwright`、`fetch`、`time` |
| 6 | 組織 MCP 政策對 CLI 的適用性 | About 頁寫不支援「MCP servers in Copilot」與「Registry URL」；其他頁面寫 Registry URL 與 allowlist 會套用 |
| 7 | 本機 Sandbox 實際行為（Windows BaseContainer、Linux bubblewrap） | 需要在各作業系統實測 |
| 8 | 雲端 Sandbox、`/delegate`、遠端控制、ACP 用戶端整合 | 需要帳號與政策設定 |
| 9 | 第 19 章 Java 片段 | 示意用，未建立專案編譯 |
| 10 | `strictKnownMarketplaces` 的項目格式 | 文件只寫「marketplace spec 陣列」，未提供範例 |
| 11 | 權限規則邊界（例如 `shell(npm test)` 是否符合帶參數的指令） | 依文件「完全比對」原則推論，需互動實測 |
| 12 | v1.0.98 之後的變更 | 本手冊截至 v1.0.97 |

### H.5 Hugo 與目錄比對結果

| 項目 | 結果 |
|------|------|
| 建置 | `hugo -d <scratchpad 絕對路徑> --quiet` 成功 |
| 頁內連結 | 688 個 `href="#..."`（336 個不重複），**無法解析 0 個** |
| 目錄 | 330 項（`##`～`####`），與 Hugo 產生的標題 id 比對**不符 0 項** |
| 標題 | 單一 H1；渲染後 h2～h4 共 334 個（目錄 330 項＋前言 3 節＋「目錄」本身） |
| `check-toc.ps1` | [A] TOC 連結找不到標題：無；[B] 有編號標題未收錄：無；[C] 重複錨點：無（v1 有 4 組重複錨點） |
| `check-md.ps1` | 其他格式問題 0 筆（v1 為 8 筆）；1 筆 MD040 為 4 個反引號巢狀區塊內層 fence 的已知誤報 |
| `test-mermaid-syntax.ps1` | 8 張圖表皆可辨識；「timeline」警告是內文出現 Timeline 一詞造成的已知誤報 |
| 檔案格式 | UTF-8 無 BOM、CRLF（5,977 行皆為 CRLF） |
