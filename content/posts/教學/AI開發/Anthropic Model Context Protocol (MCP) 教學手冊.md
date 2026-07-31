+++
date = '2026-01-09T18:11:38+08:00'
lastmod = '2026-07-31T10:00:00+08:00'
draft = false
title = 'Anthropic Model Context Protocol (MCP) 教學手冊'
tags = ['教學', 'AI開發', 'MCP']
categories = ['教學']
+++

> **文件版本**：2.0
> **對應規範**：MCP Specification `2026-07-28`（正式版，2026-07-28 發布）
> **前一規範**：`2025-11-25`（相容性內容仍保留於本文）
> **最後更新**：2026 年 7 月 31 日
> **文件等級**：企業標準技術白皮書
> **適用對象**：資深軟體開發工程師、系統架構師、平台工程與資安治理人員
> **Created by**：Eric Cheng

# Anthropic Model Context Protocol (MCP) 教學手冊

> **重大提醒**：`2026-07-28` 是 MCP 自發布以來最大幅度的改版，**包含破壞性變更（Breaking Changes）**。
> 核心協議由「有狀態、雙向」轉為「無狀態、請求／回應」。`initialize` 交握、`Mcp-Session-Id`
> 與 SSE 續傳機制均已移除；Roots、Sampling、Logging 進入棄用（Deprecated）狀態。
> 詳見 [版本更新摘要](#版本更新摘要2026-07-28-規範重點) 與 [第十一章](#第十一章2026-07-28-遷移指南)。

## 目錄

- [版本更新摘要：2026-07-28 規範重點](#版本更新摘要2026-07-28-規範重點)
  - [0.1 一頁式變更總覽](#01-一頁式變更總覽)
  - [0.2 破壞性變更清單](#02-破壞性變更清單)
  - [0.3 棄用功能與生命週期政策](#03-棄用功能與生命週期政策)
  - [0.4 本手冊改版說明](#04-本手冊改版說明)
- [第一章：MCP 概述與核心概念](#第一章mcp-概述與核心概念)
  - [1.1 什麼是 MCP？](#11-什麼是-mcp)
  - [1.2 為什麼需要 MCP？](#12-為什麼需要-mcp)
  - [1.3 MCP 架構概覽](#13-mcp-架構概覽)
  - [1.4 協議演進史與版本治理](#14-協議演進史與版本治理)
- [第二章：MCP 技術架構深度解析](#第二章mcp-技術架構深度解析)
  - [2.1 分層架構](#21-分層架構)
  - [2.2 資料層協議（Data Layer Protocol）](#22-資料層協議data-layer-protocol)
  - [2.3 MCP 核心原語（Primitives）](#23-mcp-核心原語primitives)
  - [2.4 通知機制與訂閱串流（Notifications & Subscriptions）](#24-通知機制與訂閱串流notifications--subscriptions)
  - [2.5 多輪往返請求（Multi Round-Trip Requests, MRTR）](#25-多輪往返請求multi-round-trip-requests-mrtr)
- [第三章：傳輸層深度解析](#第三章傳輸層深度解析)
  - [3.1 STDIO Transport](#31-stdio-transport)
  - [3.2 Streamable HTTP Transport](#32-streamable-http-transport)
  - [3.3 標頭路由、快取與可觀測性](#33-標頭路由快取與可觀測性)
  - [3.4 傳輸層相容性策略](#34-傳輸層相容性策略)
- [第四章：實戰開發指南](#第四章實戰開發指南)
  - [4.1 開發環境設置](#41-開發環境設置)
  - [4.2 開發 MCP Server](#42-開發-mcp-server)
  - [4.3 開發 MCP Client](#43-開發-mcp-client)
  - [4.4 整合到 AI 應用](#44-整合到-ai-應用)
- [第五章：完整實戰範例](#第五章完整實戰範例)
  - [5.1 範例一：檔案系統 MCP Server](#51-範例一檔案系統-mcp-server)
  - [5.2 範例二：資料庫查詢 MCP Server](#52-範例二資料庫查詢-mcp-server)
  - [5.3 範例三：API 整合 MCP Server](#53-範例三api-整合-mcp-server)
- [第六章：最佳實踐與設計模式](#第六章最佳實踐與設計模式)
  - [6.1 MCP Server 設計原則](#61-mcp-server-設計原則)
  - [6.2 效能優化](#62-效能優化)
  - [6.3 安全性考量](#63-安全性考量)
  - [6.4 測試策略](#64-測試策略)
- [第七章：進階主題](#第七章進階主題)
  - [7.1 Tasks 擴充（io.modelcontextprotocol/tasks）](#71-tasks-擴充iomodelcontextprotocoltasks)
  - [7.2 自訂傳輸層](#72-自訂傳輸層)
  - [7.3 多語言 SDK 比較](#73-多語言-sdk-比較)
  - [7.4 偵錯與監控](#74-偵錯與監控)
- [第八章：疑難排解](#第八章疑難排解)
  - [8.1 常見錯誤與解決方案](#81-常見錯誤與解決方案)
  - [8.2 除錯技巧](#82-除錯技巧)
  - [8.3 錯誤訊息參考](#83-錯誤訊息參考)
- [第九章：實際案例研究](#第九章實際案例研究)
  - [9.1 案例一：企業知識庫 MCP Server](#91-案例一企業知識庫-mcp-server)
  - [9.2 案例二：DevOps 整合 MCP Server](#92-案例二devops-整合-mcp-server)
- [第十章：資源與參考](#第十章資源與參考)
  - [10.1 官方資源](#101-官方資源)
  - [10.2 社群資源](#102-社群資源)
  - [10.3 開發環境建議](#103-開發環境建議)
  - [10.4 版本相容性](#104-版本相容性)
  - [10.5 快速參考](#105-快速參考)
- [第十一章：2026-07-28 遷移指南](#第十一章2026-07-28-遷移指南)
  - [11.1 遷移總體策略](#111-遷移總體策略)
  - [11.2 Server 端遷移步驟](#112-server-端遷移步驟)
  - [11.3 Client 端遷移步驟](#113-client-端遷移步驟)
  - [11.4 從 Session 到顯式握柄（Explicit Handle）](#114-從-session-到顯式握柄explicit-handle)
  - [11.5 雙時代（Dual-era）相容部署](#115-雙時代dual-era相容部署)
- [第十二章：擴充框架與官方擴充](#第十二章擴充框架與官方擴充)
  - [12.1 擴充框架（Extensions Framework）](#121-擴充框架extensions-framework)
  - [12.2 MCP Apps：伺服器渲染互動介面](#122-mcp-apps伺服器渲染互動介面)
  - [12.3 Tasks 擴充深入解析](#123-tasks-擴充深入解析)
  - [12.4 企業託管授權（EMA）與 OAuth 擴充](#124-企業託管授權ema與-oauth-擴充)
  - [12.5 自建第三方擴充](#125-自建第三方擴充)
- [第十三章：企業級部署與治理](#第十三章企業級部署與治理)
  - [13.1 無狀態水平擴展架構](#131-無狀態水平擴展架構)
  - [13.2 API 閘道、WAF 與速率限制](#132-api-閘道waf-與速率限制)
  - [13.3 授權硬化與身分治理](#133-授權硬化與身分治理)
  - [13.4 可觀測性與 OpenTelemetry](#134-可觀測性與-opentelemetry)
  - [13.5 一致性驗證與 SDK 分級](#135-一致性驗證與-sdk-分級)
- [附錄：檢查清單（Checklist）](#附錄檢查清單checklist)
  - [A. Server 開發檢查清單](#a-server-開發檢查清單)
  - [B. 部署檢查清單](#b-部署檢查清單)
  - [C. 程式碼審查檢查清單](#c-程式碼審查檢查清單)
  - [D. 故障排除檢查清單](#d-故障排除檢查清單)
  - [E. 2026-07-28 遷移檢查清單](#e-2026-07-28-遷移檢查清單)
- [結語](#結語)
- [參考文獻與延伸閱讀](#參考文獻與延伸閱讀)
  - [官方規範（2026-07-28）](#官方規範2026-07-28)
  - [治理與流程](#治理與流程)
  - [官方擴充](#官方擴充)
  - [官方部落格](#官方部落格)
  - [社群分析](#社群分析)
  - [相關標準](#相關標準)
  - [主要 SEP 索引](#主要-sep-索引)

---

## 版本更新摘要：2026-07-28 規範重點

### 0.1 一頁式變更總覽

`2026-07-28` 由六份以上的 SEP（Specification Enhancement Proposal）共同構成，將 MCP 從
「為單機 stdio 情境設計的有狀態雙向協議」重塑為「可在通用 HTTP 基礎設施上水平擴展的無狀態
請求／回應協議」。以下為與前一版 `2025-11-25` 的對照總覽。

| 面向 | `2025-11-25`（舊） | `2026-07-28`（新） | 依據 |
|------|------------------|------------------|------|
| **連線模型** | 必須先 `initialize` / `notifications/initialized` 交握 | 無交握。每個請求自我描述（self-contained） | SEP-2575 |
| **工作階段** | `Mcp-Session-Id` 標頭綁定實例 | 協議層 Session 完全移除 | SEP-2567 |
| **能力協商** | 交握時一次性交換 | 每請求以 `_meta` 攜帶；另有 `server/discover` 供前置查詢 | SEP-2575 |
| **負載平衡** | 需 Sticky Session 或共享狀態儲存 | 標準 Round-Robin 即可 | SEP-2567 |
| **伺服器發起請求** | Server 於 SSE 串流直接送出 JSON-RPC Request | 改為 MRTR：回傳 `InputRequiredResult`，由 Client 重試 | SEP-2322 |
| **回應型別** | 無 `resultType` | 所有 Result 必含 `resultType`（`complete` / `input_required`） | SEP-2322 |
| **變更通知** | HTTP GET 長連線 + `resources/subscribe` | 單一 `subscriptions/listen` 串流，逐類型 opt-in | SEP-2575 |
| **HTTP 標頭** | 僅 `MCP-Protocol-Version` | 強制 `Mcp-Method`、`Mcp-Name`；新增 `x-mcp-header` 參數鏡射 | SEP-2243 |
| **快取語意** | 無 | List／Read 結果必帶 `ttlMs`、`cacheScope` | SEP-2549 |
| **SSE 續傳** | `Last-Event-ID` 可續傳重送 | 移除；串流中斷即重發新請求 | SEP-2575 |
| **Tasks** | 核心實驗性功能（`tasks/result` 阻塞式） | 移出核心，成為官方擴充 `io.modelcontextprotocol/tasks`，改為輪詢 | SEP-2663 |
| **Tools Schema** | 受限的 JSON Schema 子集 | 完整 JSON Schema 2020-12（`oneOf`／`$ref`／條件式） | SEP-2106 |
| **追蹤傳播** | 未規範 | `_meta` 中的 `traceparent` / `tracestate` / `baggage` 正式納入 | SEP-414 |
| **授權** | 基本 OAuth 2.1 | RFC 9207 `iss` 驗證、`application_type`、憑證綁定 issuer | SEP-2468 / 837 / 2352 |
| **用戶端註冊** | DCR 為主 | CIMD（Client ID Metadata Documents）為主，DCR 棄用 | PR #2858 |
| **擴充機制** | 有概念但無流程 | 正式框架：反向 DNS 識別碼、`ext-*` 倉庫、Extensions Track | SEP-2133 |
| **功能移除流程** | 無正式政策 | 生命週期政策：Active → Deprecated → Removed，最短 12 個月窗口 | SEP-2596 |

```mermaid
graph TB
    subgraph OLD["2025-11-25：有狀態拓撲"]
        C1[MCP Client] -->|Sticky Route| LB1[Load Balancer]
        LB1 --> S1[Server #1]
        LB1 -.被綁定.-> S2[Server #2]
        S1 --> Store[(共享 Session Store)]
        S2 --> Store
    end
```

```mermaid
graph TB
    subgraph NEW["2026-07-28：無狀態拓撲"]
        C2[MCP Client] -->|Round-Robin| LB2[Load Balancer]
        LB2 --> N1[Server #1]
        LB2 --> N2[Server #2]
        LB2 --> N3[Server #3]
    end
```

### 0.2 破壞性變更清單

以下項目在 `2026-07-28` 中**已移除或語意改變**，升級時必須處理：

| # | 變更項目 | 影響對象 | 必要動作 |
|---|----------|----------|----------|
| 1 | 移除 `initialize` / `notifications/initialized` | Client 與 Server | 改以每請求 `_meta` 攜帶版本與能力 |
| 2 | 移除 `Mcp-Session-Id` 標頭與協議層 Session | Server、閘道 | 改用顯式握柄（handle）承載跨呼叫狀態 |
| 3 | 移除 HTTP GET 串流端點 | Server | 改實作 `subscriptions/listen` |
| 4 | 移除 `resources/subscribe` / `resources/unsubscribe` | 兩端 | 併入 `subscriptions/listen` 的 `resourceSubscriptions` |
| 5 | 移除 `ping`、`logging/setLevel`、`notifications/roots/list_changed` | 兩端 | 日誌層級改以 `_meta` 的 `io.modelcontextprotocol/logLevel` 逐請求指定 |
| 6 | 移除 SSE `Last-Event-ID` 續傳與訊息重送 | Client | 串流中斷須以**新的 request id** 重發請求 |
| 7 | Server 不得於串流上發送獨立 JSON-RPC Request | Server | 全面改用 MRTR `InputRequiredResult` |
| 8 | 所有 Result 必須含 `resultType` | 兩端 | 舊版回應缺欄位時，Client **MUST** 視為 `complete` |
| 9 | 強制 `Mcp-Method` / `Mcp-Name` 標頭 | Client | 未帶或與 Body 不符 → `400` + `-32020` `HeaderMismatch` |
| 10 | 資源不存在錯誤碼 `-32002` → `-32602` | Client | 比對字面值 `-32002` 的程式須更新（仍應相容舊版） |
| 11 | 錯誤碼重新編號 | 兩端 | `HeaderMismatch` `-32020`、`MissingRequiredClientCapability` `-32021`、`UnsupportedProtocolVersion` `-32022` |
| 12 | Tasks 由核心移至擴充，`tasks/result`、`tasks/list` 移除 | 已採用實驗性 Tasks 者 | 改用 `tasks/get` 輪詢 + `tasks/update` |
| 13 | 移除 `notifications/elicitation/complete` 與 `elicitationId` | Server | 以 `requestState` 自行編碼關聯識別碼 |

> **⚠️ 治理提醒**：`2026-07-28` 是規範方明確承認的「一次性乾淨切割」。官方同時導入生命週期政策與擴充框架，
> 目的即是讓**未來版本不再需要如此規模的破壞性變更**。

### 0.3 棄用功能與生命週期政策

SEP-2596 導入正式的功能生命週期政策：任何功能自標記 **Deprecated** 起，
**至少維持 12 個月可用**，並登記於官方「棄用功能登錄表」（Deprecated Features Registry）後，
才可能於後續版本 **Removed**。以 `2026-07-28` 為基準，最早移除日為 **2027-07-28**。

| 棄用功能 | 棄用理由 | 官方建議遷移路徑 |
|----------|----------|------------------|
| **Roots** | 與檔案系統假設耦合，無法泛化至遠端／雲端環境 | 以工具參數、Resource URI 或伺服器組態傳遞路徑 |
| **Sampling** | 形成 Server 反向呼叫 Client LLM 的依賴，信任邊界複雜 | Server 端直接串接 LLM 供應商 API |
| **Logging**（`notifications/message`） | 與既有可觀測性基礎設施重疊 | stdio 走 `stderr`；結構化觀測改用 OpenTelemetry |
| **HTTP+SSE Transport**（2024-11-05） | 已被 Streamable HTTP 取代 | 遷移至 Streamable HTTP |
| **Dynamic Client Registration (DCR)** | 與企業預先配置授權方向衝突 | 改用 Client ID Metadata Documents（CIMD） |
| **`includeContext` 的 `thisServer` / `allServers`** | 隨 Sampling 一併退場 | 省略該欄位或使用 `"none"` |

> **📌 實務判讀**：棄用**不等於**停止運作。以上功能在 `2026-07-28` 與其後至少一年的版本中
> 仍完全可用。但**新專案不應採用**，既有專案應排入技術債清償計畫。

### 0.4 本手冊改版說明

本次改版（v1.0 → v2.0）的內容調整原則：

1. **以 `2026-07-28` 為主敘事**：所有協議層說明、範例 JSON、HTTP 交換皆以新版為準。
2. **保留相容性說明**：凡涉及舊版行為處，以「相容性說明」區塊標註，供維運既有系統者參照。
3. **新增三個章節**：第十一章（遷移指南）、第十二章（擴充框架）、第十三章（企業級部署與治理）。
4. **程式碼範例定位**：第四～九章的實作範例以「業務邏輯與工程實踐」為主要價值，
   協議層細節請以第二、三、十一章為權威依據；各範例已標註 SDK 版本適用性。

---

## 第一章：MCP 概述與核心概念

### 1.1 什麼是 MCP？

#### 1.1.1 MCP 的定義與核心價值

**Model Context Protocol（MCP）** 是由 Anthropic 開發的一個開放標準協議，旨在為 AI 應用程式提供一個統一的方式來連接各種資料來源、工具和服務。

> **核心價值**：MCP 就像是 AI 世界的「USB-C」—— 一個標準化的介面，讓任何 AI 應用程式都能輕鬆連接到任何相容的資料來源或工具。

```text
┌─────────────────────────────────────────────────────────────────┐
│                        MCP 核心價值                              │
├─────────────────────────────────────────────────────────────────┤
│  ✓ 標準化：統一的協議規範，降低整合成本                           │
│  ✓ 可重用：一次開發，多處使用                                    │
│  ✓ 安全性：內建安全機制，保護敏感資料                             │
│  ✓ 擴展性：模組化設計，易於擴展功能                               │
└─────────────────────────────────────────────────────────────────┘
```

#### 1.1.2 USB-C 類比解釋

想像在 USB-C 出現之前，每個設備都有自己專屬的連接線：

```mermaid
graph LR
    subgraph "沒有 MCP 之前"
        A1[AI 應用 1] --> |專用 API| D1[資料庫]
        A1 --> |專用連接器| F1[檔案系統]
        A2[AI 應用 2] --> |另一套 API| D1
        A2 --> |另一套連接器| F1
    end
```

```mermaid
graph LR
    subgraph "有 MCP 之後"
        A1[AI 應用 1] --> |MCP| M[MCP Server]
        A2[AI 應用 2] --> |MCP| M
        M --> D1[資料庫]
        M --> F1[檔案系統]
        M --> E1[外部 API]
    end
```

#### 1.1.3 MCP 在 AI 應用生態系統中的定位

| 層級 | 說明 | 範例 |
|------|------|------|
| **應用層** | AI 應用程式（MCP Host） | Claude Desktop、VS Code、自訂 AI 應用 |
| **協議層** | MCP 協議 | 標準化的通訊規範 |
| **服務層** | MCP Server | 資料庫連接器、檔案系統服務、API 整合 |
| **資料層** | 底層資源 | 資料庫、檔案、外部服務 |

---

### 1.2 為什麼需要 MCP？

#### 1.2.1 解決的核心問題

**問題一：N × M 整合問題**

沒有 MCP 時，如果有 N 個 AI 應用和 M 個資料來源，需要開發 N × M 個整合。

```text
傳統方式：N × M = 大量重複工作
┌─────────┐     ┌─────────┐
│ AI App 1│────→│ 資料源 1 │
│         │────→│ 資料源 2 │
│         │────→│ 資料源 3 │
└─────────┘     └─────────┘
┌─────────┐     ┌─────────┐
│ AI App 2│────→│ 資料源 1 │ （重複開發）
│         │────→│ 資料源 2 │
│         │────→│ 資料源 3 │
└─────────┘     └─────────┘

MCP 方式：N + M = 大幅減少工作量
┌─────────┐          ┌─────────┐
│ AI App 1│──┐   ┌──→│ 資料源 1 │
│         │  │   │   └─────────┘
└─────────┘  │   │   ┌─────────┐
┌─────────┐  ├──MCP──→│ 資料源 2 │
│ AI App 2│  │   │   └─────────┘
│         │──┘   │   ┌─────────┐
└─────────┘      └──→│ 資料源 3 │
                     └─────────┘
```

**問題二：安全性與權限管理分散**

每個整合都需要獨立處理認證授權，MCP 提供統一的安全框架。

**問題三：維護成本高昂**

API 變更時需要更新多處程式碼，MCP 的抽象層降低了這種耦合。

#### 1.2.2 對不同角色的價值

| 角色 | MCP 帶來的價值 |
|------|----------------|
| **開發者** | • 減少重複開發工作<br>• 標準化的開發模式<br>• 豐富的現成 Server 可用 |
| **AI 應用** | • 快速獲取外部資料<br>• 動態發現可用工具<br>• 統一的錯誤處理 |
| **終端用戶** | • 更強大的 AI 能力<br>• 更好的整合體驗<br>• 資料安全有保障 |
| **企業** | • 降低整合成本<br>• 統一的安全管理<br>• 更好的可維護性 |

#### 1.2.3 實際應用場景範例

```text
場景 1：企業知識庫整合
┌────────────────────────────────────────────────────────┐
│ Claude Desktop                                          │
│    ↓ MCP                                               │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│ │ Confluence   │  │ SharePoint   │  │ 內部 Wiki    │   │
│ │ MCP Server   │  │ MCP Server   │  │ MCP Server   │   │
│ └──────────────┘  └──────────────┘  └──────────────┘   │
└────────────────────────────────────────────────────────┘

場景 2：開發者工具鏈整合
┌────────────────────────────────────────────────────────┐
│ VS Code + Claude                                        │
│    ↓ MCP                                               │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│ │   GitHub     │  │    Jira      │  │  Database    │   │
│ │ MCP Server   │  │ MCP Server   │  │ MCP Server   │   │
│ └──────────────┘  └──────────────┘  └──────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

### 1.3 MCP 架構概覽

#### 1.3.1 Client-Server 架構說明

MCP 採用經典的 Client-Server 架構，但有其獨特的角色定義：

```mermaid
graph TB
    subgraph "MCP 架構"
        Host[MCP Host<br/>如 Claude Desktop]
        Client[MCP Client<br/>協議客戶端]
        Server[MCP Server<br/>功能提供者]
        Resource[(資源<br/>資料庫/檔案/API)]
        
        Host --> |包含| Client
        Client <--> |MCP Protocol| Server
        Server --> |存取| Resource
    end
```

#### 1.3.2 MCP Host、Client、Server 的角色與關係

| 角色 | 說明 | 職責 | 範例 |
|------|------|------|------|
| **Host** | 宿主應用程式 | • 提供使用者介面<br>• 管理 Client 生命週期<br>• 處理使用者授權 | Claude Desktop、VS Code、自訂應用 |
| **Client** | 協議客戶端 | • 與 Server 建立連接<br>• 發送請求<br>• 處理回應 | 通常內嵌於 Host |
| **Server** | 功能提供者 | • 暴露 Tools/Resources/Prompts<br>• 處理客戶端請求<br>• 存取底層資源 | 檔案系統 Server、資料庫 Server |

**關係圖解**：

```text
┌─────────────────────────────────────────────────────────────────┐
│                         MCP Host                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                      MCP Client                          │    │
│  │  • 連接管理                                              │    │
│  │  • 請求/回應處理                                         │    │
│  │  • 能力協商                                              │    │
│  └─────────────────────────────────────────────────────────┘    │
│              ↑                    ↑                    ↑         │
│              │ MCP Protocol       │                    │         │
│              ↓                    ↓                    ↓         │
│     ┌────────────┐      ┌────────────┐      ┌────────────┐      │
│     │ Server A   │      │ Server B   │      │ Server C   │      │
│     │ (檔案系統) │      │ (資料庫)   │      │ (GitHub)   │      │
│     └────────────┘      └────────────┘      └────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

#### 1.3.3 本地伺服器 vs 遠端伺服器的差異

| 特性 | 本地伺服器（Local Server） | 遠端伺服器（Remote Server） |
|------|---------------------------|----------------------------|
| **部署位置** | 與 Host 同一機器 | 獨立部署的伺服器 |
| **傳輸方式** | STDIO（標準輸入/輸出） | Streamable HTTP |
| **啟動方式** | Host 直接啟動進程 | 獨立運行，透過網路連接 |
| **適用場景** | 個人工具、本地資源存取 | 團隊共享、雲端服務 |
| **安全考量** | 由環境變數取得憑證，繼承本地權限 | 需 OAuth 2.1 / OIDC 認證授權 |
| **效能** | 低延遲、高效能 | 網路延遲、需考慮可用性 |
| **水平擴展**（`2026-07-28`） | 不適用 | 標準 Round-Robin，無需 Sticky Session |

> **📌 `2026-07-28` 重要澄清**：規範明訂「一條開啟的連線（含 stdio 進程）**不等於**一個對話或工作階段」。
> 用戶端可在同一條傳輸上交錯送出彼此無關的請求；伺服器**不得**以連線或進程身分推測對話連續性。
> 這對本地與遠端伺服器同時適用。

**選擇建議**：

```text
┌─────────────────────────────────────────────────────────────────┐
│                    選擇本地 vs 遠端伺服器                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  選擇本地伺服器當：                                               │
│  ✓ 存取本地檔案系統                                              │
│  ✓ 需要低延遲回應                                                │
│  ✓ 個人使用場景                                                  │
│  ✓ 開發測試階段                                                  │
│                                                                  │
│  選擇遠端伺服器當：                                               │
│  ✓ 多人共享服務                                                  │
│  ✓ 需要集中管理                                                  │
│  ✓ 整合雲端服務                                                  │
│  ✓ 生產環境部署                                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

> **💡 實務建議**：開發階段建議使用本地伺服器進行快速迭代，確認功能後再部署為遠端伺服器供團隊使用。

---

### 1.4 協議演進史與版本治理

#### 1.4.1 版本時間軸

MCP 的協議版本採用「發布日期」作為版本識別碼（`YYYY-MM-DD`），而非語意化版本號。

| 版本 | 發布日期 | 里程碑意義 |
|------|----------|-----------|
| `2024-11-05` | 2024-11-05 | 初始公開版本。定義 JSON-RPC 基礎、Tools/Resources/Prompts、stdio 與 HTTP+SSE 傳輸 |
| `2025-03-26` | 2025-03-26 | 導入 Streamable HTTP 取代 HTTP+SSE；強化 OAuth 授權框架 |
| `2025-06-18` | 2025-06-18 | 導入 `MCP-Protocol-Version` 標頭；Elicitation 初版；結構化工具輸出 |
| `2025-11-25` | 2025-11-25 | 一週年版本。實驗性 Tasks、URL 模式 Elicitation、擴充概念雛形 |
| **`2026-07-28`** | **2026-07-28** | **無狀態核心、MRTR、擴充框架正式化、授權硬化、生命週期政策** |

```mermaid
timeline
    title MCP 協議演進
    2024-11-05 : 初始版本 : stdio + HTTP&#43;SSE
    2025-03-26 : Streamable HTTP : OAuth 框架
    2025-06-18 : 協議版本標頭 : Elicitation
    2025-11-25 : 實驗性 Tasks : 一週年
    2026-07-28 : 無狀態核心 : MRTR : 擴充框架
```

#### 1.4.2 SEP 流程（Specification Enhancement Proposal）

MCP 的規範變更透過 SEP 流程進行治理，類似 Python 的 PEP 或 Java 的 JEP：

| 階段 | 說明 |
|------|------|
| **Proposal** | 於規範倉庫 `seps/` 目錄以 Markdown 提出 PR，編號取自 PR 編號 |
| **Sponsorship** | 需取得核心維護者（Core Maintainer）擔任 Sponsor |
| **Draft / Review** | 於對應 Working Group 討論，狀態以 PR 標籤管理 |
| **Final** | **必須**先有對應情境進入 [Conformance Suite](https://github.com/modelcontextprotocol/conformance)（SEP-2484）才可定案 |

SEP 分為兩條軌道：

- **Standards Track**：變更核心規範本體。
- **Extensions Track**（SEP-2133 新增）：定義官方擴充，可獨立於核心規範版本演進。

#### 1.4.3 功能生命週期政策（SEP-2596）

```mermaid
stateDiagram-v2
    [*] --> Active: 功能納入規範
    Active --> Deprecated: 標記棄用並登錄 Registry
    Deprecated --> Removed: 至少 12 個月後，經獨立 SEP 核准
    Deprecated --> Active: 撤回棄用決議
    Removed --> [*]
```

| 狀態 | 定義 | 實作者義務 |
|------|------|-----------|
| **Active** | 功能為規範正式組成部分 | 依規範實作 |
| **Deprecated** | 仍完全可用，但不建議新採用 | 既有實作維持相容；新專案避免採用 |
| **Removed** | 自規範移除 | 可停止支援 |

> **企業採用建議**：將「棄用功能登錄表」納入年度技術債盤點流程。
> 12 個月的最短窗口足以規劃遷移，但不足以應付未追蹤的大型系統。

#### 1.4.4 SDK 分級制度（SDK Tier System）

官方導入 SDK 分級，並以 Conformance Suite 評分：

| 分級 | 定義 | 目前成員 |
|------|------|----------|
| **Tier 1** | 官方維護，需於規範發布窗口內完成支援 | TypeScript、Python、Go、C# |
| **Tier 2 以下** | 官方或社群維護，支援時程不受規範窗口約束 | Rust（`2026-07-28` beta）、Java、Kotlin、Swift、Ruby、PHP 等 |

> **選型建議**：企業導入若需在規範發布後短期內跟進，應優先選擇 Tier 1 SDK。
> 非 Tier 1 SDK 應於架構決策紀錄（ADR）中明列版本落後風險與緩解方案。

---

## 第二章：MCP 技術架構深度解析

### 2.1 分層架構

MCP 採用清晰的分層架構設計，將關注點分離：

```mermaid
graph TB
    subgraph "MCP 分層架構"
        App[應用層<br/>AI 應用程式]
        Data[資料層<br/>JSON-RPC 2.0 訊息]
        Transport[傳輸層<br/>STDIO / HTTP]
        Physical[實體層<br/>進程 / 網路]
        
        App --> Data
        Data --> Transport
        Transport --> Physical
    end
```

#### 2.1.1 資料層（Data Layer）詳解

資料層負責定義訊息格式和協議語義：

| 元素 | 說明 | `2026-07-28` 實作方式 |
|------|------|---------------------|
| **訊息格式** | JSON-RPC 2.0 | 請求、回應（含 `resultType`）、通知 |
| **請求中繼資料** | 取代連線生命週期 | 每請求的 `params._meta` 攜帶版本、身分、能力 |
| **能力採協** | 功能探索 | `server/discover` RPC（可選前置查詢） |
| **原語定義** | 核心抽象 | Tools、Resources、Prompts |
| **互動模式** | 訊息交換型態 | Request/Response、MRTR、Subscribe & Notify |

#### 2.1.2 傳輸層（Transport Layer）詳解

傳輸層負責訊息的實際傳遞：

| 傳輸方式 | 協議 | 狀態 | 特點 |
|----------|------|------|------|
| **STDIO** | 標準輸入/輸出 | Active | 本地進程通訊、低延遲 |
| **Streamable HTTP** | HTTP POST（+ 每請求 SSE 串流） | Active | 遠端通訊、可水平擴展 |
| **HTTP + SSE**（2024-11-05） | HTTP POST + 獨立 SSE 端點 | **Deprecated** | 僅向後相容，不得新採用 |

#### 2.1.3 層與層之間的互動關係

```text
┌─────────────────────────────────────────────────────────────────┐
│                        資料層 ←→ 傳輸層 互動                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. 序列化                                                       │
│     資料層物件 ──JSON.stringify──→ 傳輸層字串                     │
│                                                                  │
│  2. 傳輸                                                         │
│     傳輸層字串 ──STDIO/HTTP──→ 對端                               │
│                                                                  │
│  3. 反序列化                                                     │
│     傳輸層字串 ──JSON.parse──→ 資料層物件                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

### 2.2 資料層協議（Data Layer Protocol）

#### 2.2.1 JSON-RPC 2.0 基礎與 `resultType`

MCP 使用 JSON-RPC 2.0 作為訊息協議，包含三種訊息類型：

**請求（Request）**：

`2026-07-28` 起，每個請求都是自我描述（self-contained）的：協議版本、用戶端身分與能力
一律透過 `params._meta` 攜帶，不再依賴任何先前的交握。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "read_file",
    "arguments": {
      "path": "/path/to/file.txt"
    },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientInfo": {
        "name": "MyApp",
        "version": "1.0.0"
      },
      "io.modelcontextprotocol/clientCapabilities": {
        "elicitation": {}
      }
    }
  }
}
```

**回應（Response）**：

所有 Result **必須**包含 `resultType` 欄位，用以支援多型結果。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "complete",
    "content": [
      {
        "type": "text",
        "text": "檔案內容..."
      }
    ],
    "_meta": {
      "io.modelcontextprotocol/serverInfo": {
        "name": "FileSystemServer",
        "version": "2.0.0"
      }
    }
  }
}
```

| `resultType` | 意義 | 定義來源 |
|--------------|------|----------|
| `complete` | 請求已完成，`result` 為最終內容 | 核心協議 |
| `input_required` | 請求未完成，需要額外輸入（見 [2.5 MRTR](#25-多輪往返請求multi-round-trip-requests-mrtr)） | 核心協議 |
| `task` | 伺服器改以非同步任務處理（見 [12.3](#123-tasks-擴充深入解析)） | Tasks 擴充 |

> **相容性規則**：舊版伺服器的回應不含 `resultType`，用戶端 **MUST** 將其視為 `complete`。
> 用戶端無法辨識的 `resultType` 值 **MUST** 視為無效。

**通知（Notification）**：
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed",
  "params": {
    "_meta": {
      "io.modelcontextprotocol/subscriptionId": 1
    }
  }
}
```

**JSON-RPC 錯誤碼分區政策**（`2026-07-28` 新增）：

JSON-RPC 2.0 保留 `-32000` 至 `-32099` 供實作自訂，MCP 進一步分區：

| 區間 | 用途 | 規則 |
|------|------|------|
| `-32700`、`-32600`～`-32603` | JSON-RPC 標準錯誤 | 依 JSON-RPC 2.0 |
| `-32000`～`-32019` | **Legacy**：既有 SDK 已配置 | 新實作**不應**使用；除 `-32002` 外不得假設語意 |
| `-32020`～`-32099` | **保留給 MCP 規範** | 僅規範可定義；實作不得自行配置 |
| 其餘整數空間 | 應用層自訂錯誤 | 建議配置於 `-32768`～`-32000` 之外 |

MCP 目前定義的錯誤碼：

| 錯誤碼 | 名稱 | 觸發情境 |
|--------|------|----------|
| `-32020` | `HeaderMismatch` | HTTP 標頭與 Body 值不符，或缺少必要標頭 |
| `-32021` | `MissingRequiredClientCapability` | 處理請求所需能力未在 `clientCapabilities` 宣告 |
| `-32022` | `UnsupportedProtocolVersion` | 伺服器不支援請求宣告的協議版本 |

已保留不再重用的舊碼：`-32002`（資源不存在，已改用 `-32602`）、`-32042`（URL Elicitation，`2025-11-25` 專用）。

#### 2.2.2 無狀態核心與 `_meta` 請求中繼資料

MCP 在 `2026-07-28` 成為**無狀態協議（Stateless Protocol）**：處理一個請求所需的全部資訊，
都必須包含在該請求本身。伺服器獨立處理每個請求，**不得**從先前請求推論任何狀態，
即使兩者來自同一條連線或串流。

**規範明確要求**：

- 伺服器 **MUST NOT** 依賴同一連線上的先前請求來建立上下文（能力、協議版本、用戶端身分）。
- 伺服器 **SHOULD** 準備好處理來自多個任務、執行緒或對話的交錯請求。
- 伺服器 **SHOULD NOT** 要求用戶端重用同一連線或進程來執行相關操作。
- 需跨請求延續的狀態 **MUST** 由顯式識別碼承載，並由用戶端在每次請求中傳入。

```mermaid
stateDiagram-v2
    [*] --> Ready: 連線建立（無交握）
    Ready --> Processing: 收到自我描述請求
    Processing --> Ready: 回傳 complete
    Processing --> Ready: 回傳 input_required（MRTR）
    Processing --> Ready: 回傳 task handle（Tasks 擴充）
    Ready --> [*]: 連線關閉（不影響應用狀態）
```

**與舊版的對照**：

```text
【2025-11-25：有交握】                    【2026-07-28：無交握】
Client                Server              Client                Server
   │─── initialize ──────→│                  │                     │
   │←── initialize result ─│                  │─ tools/call ───────→│
   │─── initialized ──────→│                  │   (含 _meta)         │
   │   === 就緒 ===        │                  │←── result ──────────│
   │─── tools/call ───────→│                  │  （單一往返即完成）    │
   │   (Mcp-Session-Id)    │                  │
```

**`_meta` 逐請求協議欄位**：

| 鍵名 | 型別 | 必要 | 說明 |
|------|------|------|------|
| `io.modelcontextprotocol/protocolVersion` | `string` | **是** | 本請求使用的協議版本，例如 `"2026-07-28"` |
| `io.modelcontextprotocol/clientCapabilities` | `ClientCapabilities` | **是** | 與本請求相關的用戶端能力 |
| `io.modelcontextprotocol/clientInfo` | `Implementation` | 否（**SHOULD** 提供） | 用戶端名稱與版本 |
| `io.modelcontextprotocol/logLevel` | `LoggingLevel` | 否 | 本請求要求伺服器輸出的最低日誌層級 |
| `progressToken` | `string \| number` | 否 | 訂閱進度通知 |
| `traceparent` / `tracestate` / `baggage` | `string` | 否 | W3C Trace Context 傳播 |

**回應端 `_meta` 欄位**：

| 鍵名 | 型別 | 說明 |
|------|------|------|
| `io.modelcontextprotocol/serverInfo` | `Implementation` | 伺服器名稱與版本，**SHOULD** 於每個 Result 提供 |
| `io.modelcontextprotocol/subscriptionId` | `number` | 訂閱串流上的通知**必須**攜帶，供用戶端解多工 |

**錯誤處理規則**：

- 缺少任一必要欄位 → 伺服器 **MUST** 回傳 `-32602`（Invalid params）；HTTP 狀態 **MUST** 為 `400`。
- 伺服器 **MUST NOT** 依賴用戶端未宣告的能力；若處理請求需要未宣告能力，
  **MUST** 回傳 `-32021` `MissingRequiredClientCapabilityError`，並於 `data.requiredCapabilities` 列出缺項。

> **⚠️ 安全提醒**：`clientInfo` 與 `serverInfo` 為自我宣告且**未經協議驗證**，
> 僅供顯示、日誌與除錯使用。實作 **SHOULD NOT** 依其改變行為，
> 更 **SHOULD NOT** 作為安全決策依據。

**`_meta` 鍵名命名規則**：

- 前綴為以點分隔的標籤序列 + 斜線，建議採反向 DNS（例如 `com.example/`）。
- 第二個標籤為 `modelcontextprotocol` 或 `mcp` 的前綴**保留給 MCP 官方**
  （`io.modelcontextprotocol/`、`dev.mcp/`、`com.mcp.tools/` 皆保留；`com.example.mcp/` 不保留）。
- 名稱部分須以英數字開頭與結尾，中間可含 `-`、`_`、`.`。

#### 2.2.3 能力協商與 `server/discover`

在無交握模型下，能力宣告拆分為兩個方向：

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    opt 前置探索（可選）
        C->>S: server/discover
        S-->>C: supportedVersions + capabilities + serverInfo<br/>（含 ttlMs / cacheScope）
    end

    C->>S: tools/call（_meta 攜帶 clientCapabilities）
    alt 版本與能力相符
        S-->>C: Result（resultType: complete）
    else 版本不支援
        S-->>C: -32022 UnsupportedProtocolVersion（附 supported 清單）
    else 缺少必要用戶端能力
        S-->>C: -32021 MissingRequiredClientCapability
    end
```

**`server/discover`**：伺服器 **MUST** 實作此 RPC。用戶端 **MAY**（非必要）於任何請求前呼叫，
以取得支援版本、能力與身分；在 stdio 上亦可作為「新舊時代偵測探針」。

```json
// Client → Server
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "server/discover",
  "params": {
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {}
    }
  }
}

// Server → Client
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "complete",
    "supportedVersions": ["2026-07-28", "2025-11-25"],
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": { "listChanged": true },
      "prompts": { "listChanged": true },
      "extensions": {
        "io.modelcontextprotocol/tasks": {}
      }
    },
    "_meta": {
      "io.modelcontextprotocol/serverInfo": {
        "name": "FileSystemServer",
        "version": "2.0.0"
      }
    },
    "ttlMs": 3600000,
    "cacheScope": "public"
  }
}
```

**Client 能力**（於每個請求的 `_meta` 中宣告）：

| 能力 | 說明 | 狀態 |
|------|------|------|
| `elicitation` | 可向使用者索取結構化輸入 | Active |
| `extensions` | 支援的擴充識別碼對應設定物件 | Active（SEP-2133） |
| `sampling` | 可代 Server 執行 LLM 補全 | **Deprecated** |
| `roots` | 可提供工作區根目錄清單 | **Deprecated** |

**Server 能力**（於 `server/discover` 回應中宣告）：

| 能力 | 說明 | 狀態 |
|------|------|------|
| `tools` | 提供可呼叫的工具 | Active |
| `resources` | 提供可讀取的資源 | Active |
| `prompts` | 提供可用的提示模板 | Active |
| `completions` | 提供參數自動補全 | Active |
| `extensions` | 支援的擴充識別碼對應設定物件 | Active |
| `logging` | 協議層日誌訊息 | **Deprecated** |

#### 2.2.4 版本協商與相容性矩陣

`2026-07-28` **沒有版本協商交握**。每個請求宣告自身版本，伺服器逐請求接受或拒絕。

```mermaid
sequenceDiagram
    participant Client
    participant Server
    Client->>Server: request（_meta.protocolVersion）
    alt 支援該版本
        Server-->>Client: result
    else 不支援
        Server-->>Client: UnsupportedProtocolVersionError（-32022）
        Note over Client,Server: Client 自 supported 清單挑選共同版本後重試
    end
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32022,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2026-07-28", "2025-11-25"],
      "requested": "1900-01-01"
    }
  }
}
```

**時代（Era）術語**：

| 術語 | 定義 |
|------|------|
| **Modern** | 以逐請求中繼資料傳遞版本／身分／能力的版本（`2026-07-28` 及之後） |
| **Legacy** | 以 `initialize` 交握建立 Session 的版本（`2025-11-25` 及之前） |
| **Dual-era** | 同時支援 Modern 與 Legacy 的實作 |

**相容性矩陣**：

| Client | Server | 結果 |
|--------|--------|------|
| Modern | Modern | ✅ 正常。`server/discover` 為可選；版本不符以 `-32022` 表面化後重試 |
| Modern | Legacy | ❌ 失敗。stdio 上 **SHOULD** 先送 `server/discover` 以確定性地失敗並回報可行錯誤 |
| Dual-era | Modern | ✅ 正常。維持 Modern 模式 |
| Dual-era | Legacy | ✅ 正常。回退至 `initialize`（必要時再退至 HTTP+SSE） |
| Legacy | Modern | ❌ 失敗。Legacy 用戶端**沒有向前相容機制** |
| Legacy | Dual-era | ✅ 正常。伺服器以協商出的 Legacy 版本服務 |
| Legacy | Legacy | ✅ 依 Legacy 版本運作（不在本版規範範圍） |

> **實作要點**：時代判定是**伺服器層級**屬性而非單一請求屬性。
> 用戶端 **SHOULD** 於伺服器進程（stdio）或來源（HTTP origin）的生命週期內快取判定結果，
> 並 **MAY** 跨重啟持久化；若快取假設後續失效則重新探測。
>
> 僅支援 Modern 的伺服器 **SHOULD** 在回應 `initialize` 的錯誤訊息中，
> 明列自身支援的協議版本——這往往是 Legacy 用戶端唯一能呈現給使用者的診斷資訊。

**擴充協商**：

擴充以 `extensions` 欄位協商，為「擴充識別碼 → 設定物件」的對應表：

```json
{
  "capabilities": {
    "tools": {},
    "extensions": {
      "io.modelcontextprotocol/tasks": {},
      "io.modelcontextprotocol/ui": {
        "mimeTypes": ["text/html;profile=mcp-app"]
      }
    }
  }
}
```

若一方支援而另一方不支援，支援方 **MUST** 退回核心協議行為，或以適當錯誤拒絕請求。
擴充規格 **SHOULD** 明文記載預期的降級（fallback）行為。

---

### 2.3 MCP 核心原語（Primitives）

MCP 定義了多種原語（Primitives），作為 Client 與 Server 之間互動的基本單位。
`2026-07-28` 對原語清單做了重要調整：

```mermaid
graph TB
    subgraph SERVER["Server 端原語（Active）"]
        Tools[Tools<br/>可執行函數]
        Resources[Resources<br/>資料來源]
        Prompts[Prompts<br/>模板]
    end

    subgraph CLIENT["Client 端原語"]
        Elicitation[Elicitation<br/>用戶互動<br/>Active，經 MRTR 傳遞]
        Sampling[Sampling<br/>LLM 請求<br/>Deprecated]
        Roots[Roots<br/>工作區根目錄<br/>Deprecated]
        Logging[Logging<br/>協議層日誌<br/>Deprecated]
    end

    subgraph EXT["官方擴充"]
        Tasks[Tasks<br/>長時間任務<br/>io.modelcontextprotocol/tasks]
        Apps[MCP Apps<br/>伺服器渲染 UI<br/>io.modelcontextprotocol/ui]
    end
```

| 原語 | 歸屬 | `2025-11-25` 狀態 | `2026-07-28` 狀態 |
|------|------|------------------|------------------|
| Tools | Server | Active | Active（Schema 升級至 JSON Schema 2020-12） |
| Resources | Server | Active | Active（新增 `ttlMs` / `cacheScope`） |
| Prompts | Server | Active | Active（新增 `ttlMs` / `cacheScope`） |
| Elicitation | Client | Active（Server 主動送出） | Active（**改由 MRTR 傳遞**） |
| Sampling | Client | Active | **Deprecated** |
| Roots | Client | Active | **Deprecated** |
| Logging | Server → Client | Active | **Deprecated**（`logging/setLevel` 已移除） |
| Tasks | 通用 | 實驗性核心功能 | **移出核心，成為官方擴充** |

#### 2.3.1 Server 端原語：Tools

**Tools** 是 Server 暴露給 Client 的可執行函數，允許 AI 執行特定操作。

**Tool 定義結構**：

```json
{
  "name": "read_file",
  "description": "讀取指定路徑的檔案內容",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "檔案的完整路徑"
      }
    },
    "required": ["path"]
  }
}
```

**列出工具（tools/list）**：

```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "read_file",
        "description": "讀取檔案內容",
        "inputSchema": { ... }
      },
      {
        "name": "write_file",
        "description": "寫入檔案內容",
        "inputSchema": { ... }
      }
    ]
  }
}
```

**呼叫工具（tools/call）**：

```json
// Request
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "read_file",
    "arguments": {
      "path": "/home/user/document.txt"
    }
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "這是檔案的內容..."
      }
    ],
    "isError": false
  }
}
```

#### 2.3.2 Server 端原語：Resources

**Resources** 代表 Server 可以提供的資料來源，可以是檔案、資料庫記錄、API 回應等。

**Resource 定義結構**：

```json
{
  "uri": "file:///path/to/document.txt",
  "name": "document.txt",
  "description": "專案說明文件",
  "mimeType": "text/plain"
}
```

**列出資源（resources/list）**：

```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list"
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": "file:///docs/readme.md",
        "name": "README",
        "mimeType": "text/markdown"
      },
      {
        "uri": "db://users/schema",
        "name": "Users Schema",
        "mimeType": "application/json"
      }
    ]
  }
}
```

**讀取資源（resources/read）**：

```json
// Request
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///docs/readme.md"
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///docs/readme.md",
        "mimeType": "text/markdown",
        "text": "# README\n\n這是專案說明..."
      }
    ]
  }
}
```

#### 2.3.3 Server 端原語：Prompts

**Prompts** 是預定義的可重用模板，可以包含動態參數。

**Prompt 定義結構**：

```json
{
  "name": "code_review",
  "description": "程式碼審查模板",
  "arguments": [
    {
      "name": "language",
      "description": "程式語言",
      "required": true
    },
    {
      "name": "code",
      "description": "要審查的程式碼",
      "required": true
    }
  ]
}
```

**取得提示（prompts/get）**：

```json
// Request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "language": "Python",
      "code": "def hello(): print('Hello')"
    }
  }
}

// Response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "description": "Python 程式碼審查",
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "請審查以下 Python 程式碼：\n\ndef hello(): print('Hello')\n\n請提供改進建議。"
        }
      }
    ]
  }
}
```

#### 2.3.4 Client 端原語：Sampling（已棄用）

> **⚠️ 棄用公告（SEP-2577）**：Sampling 自 `2026-07-28` 起標記為 **Deprecated**。
> 棄用理由是它造成「Server 反向呼叫 Client 的 LLM」的逆向依賴，使信任邊界複雜化、
> 難以在安全面推理。**官方建議遷移路徑：Server 端直接串接 LLM 供應商 API。**
> 最早移除日不早於 2027-07-28。

**Sampling** 允許 Server 請求 Client 進行 LLM 完成操作。在 `2026-07-28` 中，
它**不再以獨立 JSON-RPC Request 送出**，而是包裝在 MRTR 的 `inputRequests` 內：

```json
// Server → Client：InputRequiredResult 內嵌 sampling 請求
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "input_required",
    "inputRequests": {
      "summarize": {
        "method": "sampling/createMessage",
        "params": {
          "messages": [
            {
              "role": "user",
              "content": { "type": "text", "text": "請摘要以下內容..." }
            }
          ],
          "systemPrompt": "You are a helpful assistant.",
          "maxTokens": 500
        }
      }
    },
    "requestState": "<AEAD 保護的不透明字串>"
  }
}

// Client → Server：重試原請求並附上 inputResponses
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "summarize_doc",
    "arguments": { "docId": "D-1024" },
    "inputResponses": {
      "summarize": {
        "role": "assistant",
        "content": { "type": "text", "text": "這是摘要內容..." },
        "model": "claude-3-sonnet",
        "stopReason": "endTurn"
      }
    },
    "requestState": "<原樣回傳>",
    "_meta": { "io.modelcontextprotocol/protocolVersion": "2026-07-28",
               "io.modelcontextprotocol/clientCapabilities": { "sampling": {} } }
  }
}
```

**遷移建議（Server 端直接串接 LLM）**：

| 考量點 | Sampling 模式 | 直接串接模式 |
|--------|--------------|-------------|
| 模型選擇 | 由 Client 決定 | 由 Server 決定，可用專屬微調模型 |
| 成本歸屬 | 使用者的模型額度 | Server 營運方的額度 |
| 信任邊界 | Server 可影響 Client 的 LLM 呼叫 | 邊界清晰 |
| 相依 | 需 Client 宣告 `sampling` 能力 | 無協議相依 |
| 憑證管理 | 無需管理 LLM 金鑰 | **需要**安全的金鑰管理 |

> **架構決策提示**：直接串接會將 LLM 成本與金鑰管理責任移至 Server 端。
> 導入前應確認：金鑰儲存於 Vault／KMS、有分租戶額度控管、有 Token 用量可觀測性。

#### 2.3.5 Client 端原語：Elicitation

**Elicitation** 允許 Server 請求使用者輸入或確認，是 `2026-07-28` 中**唯一保持 Active** 的
Server-to-Client 互動原語。

**關鍵變更（SEP-2260 / SEP-2322）**：

1. Server 發起的請求 **只能** 在伺服器正在處理某個用戶端請求時發出——
   舊版是「建議」，新版是**強制要求**。使用者不會被突如其來的提示打斷，
   每個 Elicitation 都可回溯到使用者（或其代理）啟動的動作。
2. 傳遞方式改為 MRTR：不再需要維持一條開啟的 SSE 串流。
3. 移除 `notifications/elicitation/complete` 與 URL 模式的 `elicitationId`；
   需跨重試關聯者，由 Server 自行編碼於 `requestState`。

```json
// Server → Client：InputRequiredResult
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "input_required",
    "inputRequests": {
      "confirm_delete": {
        "method": "elicitation/create",
        "params": {
          "mode": "form",
          "message": "是否確認刪除這 3 個檔案？",
          "requestedSchema": {
            "type": "object",
            "properties": {
              "confirm": { "type": "boolean", "description": "確認刪除" }
            },
            "required": ["confirm"]
          }
        }
      }
    },
    "requestState": "eyJzdGVwIjoxLCJmaWxlcyI6WyJhIiwiYiIsImMiXX0="
  }
}
```

用戶端收集答案後，以**新的 JSON-RPC id** 重試原請求，並附上 `inputResponses` 與原樣的 `requestState`。

#### 2.3.6 Server 端原語：Logging（已棄用）

> **⚠️ 棄用公告（SEP-2577）**：協議層 Logging 自 `2026-07-28` 起標記為 **Deprecated**，
> 理由是與既有且更成熟的可觀測性基礎設施重疊。
> **建議遷移路徑：stdio 傳輸寫入 `stderr`；結構化觀測改用 OpenTelemetry。**

**`2026-07-28` 的行為變更**：

- `logging/setLevel` 方法**已移除**。
- 日誌層級改為**逐請求**指定：於 `_meta` 放入 `io.modelcontextprotocol/logLevel`。
- 伺服器 **MUST NOT** 對未包含該欄位的請求發送 `notifications/message`。
- `notifications/message` 屬「請求範圍通知」，只在該請求自身的回應串流上傳遞，
  **不會**出現在 `subscriptions/listen` 串流。

```json
// Client：於請求中指定日誌層級
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "read_file",
    "arguments": { "path": "/data/a.txt" },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {},
      "io.modelcontextprotocol/logLevel": "debug"
    }
  }
}

// Server → Client：於該請求的回應串流上發送
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "info",
    "logger": "FileSystem",
    "data": "檔案讀取成功: /data/a.txt"
  }
}
```

日誌級別（沿用 RFC 5424 syslog 嚴重度）：

| 級別 | 說明 | 建議用途 |
|------|------|----------|
| `debug` | 除錯資訊 | 開發期詳細追蹤 |
| `info` | 一般資訊 | 正常操作記錄 |
| `notice` | 重要通知 | 值得注意但非異常 |
| `warning` | 警告訊息 | 潛在問題 |
| `error` | 錯誤訊息 | 操作失敗 |
| `critical` | 嚴重錯誤 | 元件失效 |
| `alert` | 需要立即處理 | 須人工介入 |
| `emergency` | 系統不可用 | 全面失效 |

#### 2.3.7 Client 端原語：Roots（已棄用）

> **⚠️ 棄用公告（SEP-2577）**：Roots 自 `2026-07-28` 起標記為 **Deprecated**。
> 棄用理由是它讓 Client 與 Server 圍繞「本機檔案系統」假設緊密耦合，
> 無法泛化至遠端或雲端環境。
> **建議遷移路徑：以工具參數、Resource URI 或伺服器組態傳遞目錄／檔案路徑。**

同時，`notifications/roots/list_changed` 通知**已移除**；`roots/list` 若仍使用，
必須改由 MRTR 的 `inputRequests` 傳遞。

**遷移範例（以工具參數取代 Roots）**：

```json
{
  "name": "search_code",
  "description": "在指定的專案目錄中搜尋程式碼",
  "inputSchema": {
    "type": "object",
    "properties": {
      "workspacePath": {
        "type": "string",
        "description": "專案根目錄的絕對路徑（由呼叫端明確提供）"
      },
      "pattern": { "type": "string" }
    },
    "required": ["workspacePath", "pattern"]
  }
}
```

> **安全提醒**：將路徑改為工具參數後，**路徑白名單與正規化（path canonicalization）
> 的責任完全落在 Server**。務必防範路徑穿越（`../`）、符號連結逃逸與 UNC 路徑攻擊。
> 詳見 [6.3.2 輸入驗證](#632-輸入驗證)。

#### 2.3.8 官方擴充：Tasks

> **狀態變更（SEP-2663）**：Tasks 在 `2025-11-25` 是核心的實驗性功能；
> 生產環境使用經驗顯示需要重新設計，因此 `2026-07-28` 將其**移出核心規範**，
> 成為官方擴充 `io.modelcontextprotocol/tasks`。
> **既有採用 `2025-11-25` 實驗性 Tasks API 的實作必須遷移。**

**主要設計變更**：

| 項目 | `2025-11-25`（核心實驗性） | `2026-07-28`（官方擴充） |
|------|--------------------------|------------------------|
| 取得結果 | `tasks/result`（阻塞式） | `tasks/get`（輪詢式） |
| 中途輸入 | 無標準機制 | `tasks/update` 提交 `inputResponses` |
| 列出任務 | `tasks/list` | **已移除**（無 Session 即無法安全界定範圍） |
| 建立方式 | 用戶端逐請求 opt-in | **伺服器主導**：Client 宣告擴充，Server 決定何時轉為 Task |
| 結果型別 | 一般 Result 附 `taskId` | `CreateTaskResult`（`resultType: "task"`） |

```json
// Server → Client：以任務握柄回應 tools/call
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "task",
    "taskId": "task-8f21c",
    "status": "working",
    "ttlMs": 86400000,
    "pollIntervalMs": 2000
  }
}

// Client → Server：輪詢
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tasks/get",
  "params": {
    "taskId": "task-8f21c",
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {
        "extensions": { "io.modelcontextprotocol/tasks": {} }
      }
    }
  }
}
```

任務狀態機與完整實作指引請見 [12.3 Tasks 擴充深入解析](#123-tasks-擴充深入解析)。

---

### 2.4 通知機制與訂閱串流（Notifications & Subscriptions）

`2026-07-28` 將通知明確劃分為兩類，這是理解新版通知模型的關鍵：

| 類別 | 範例 | 傳遞管道 |
|------|------|----------|
| **請求範圍通知**（Request-scoped） | `notifications/progress`、`notifications/message` | **只在該請求自身的回應串流上** |
| **變更通知**（Change notifications） | `notifications/tools/list_changed`、`notifications/resources/updated` | **只在 `subscriptions/listen` 串流上** |

#### 2.4.1 `subscriptions/listen`：統一的長效通知串流

`subscriptions/listen` 取代了舊版的 HTTP GET 串流端點與
`resources/subscribe` / `resources/unsubscribe` 方法。它本身是一個
**長效的請求／回應**：回應即是一條持續開啟、只傳送用戶端明確訂閱之通知類型的串流。

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    C->>S: POST subscriptions/listen（notifications 篩選器）
    S-->>C: SSE: notifications/subscriptions/acknowledged
    Note over C,S: 串流保持開啟
    S-->>C: SSE: notifications/tools/list_changed
    S-->>C: SSE: notifications/resources/updated
    Note over C,S: 直到任一方關閉串流
```

**開啟訂閱**：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "subscriptions/listen",
  "params": {
    "notifications": {
      "toolsListChanged": true,
      "resourceSubscriptions": ["file:///project/config.json"]
    },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {}
    }
  }
}
```

**通知篩選器欄位**：

| 欄位 | 型別 | 說明 |
|------|------|------|
| `toolsListChanged` | `boolean` | 接收 `notifications/tools/list_changed` |
| `promptsListChanged` | `boolean` | 接收 `notifications/prompts/list_changed` |
| `resourcesListChanged` | `boolean` | 接收 `notifications/resources/list_changed` |
| `resourceSubscriptions` | `string[]` | 對這些 Resource URI 接收 `notifications/resources/updated` |

所有欄位皆為可選；省略即等同於不訂閱該類型。伺服器 **MUST NOT** 發送用戶端未明確要求的通知類型。

**確認（Acknowledgment）**：

伺服器 **MUST** 以 `notifications/subscriptions/acknowledged` 作為該訂閱的第一則訊息，
並於 `_meta.io.modelcontextprotocol/subscriptionId` 帶入訂閱 ID（即 `subscriptions/listen`
請求的 JSON-RPC id）。確認訊息中的 `notifications` 欄位反映**伺服器實際同意承接的子集**——
不支援的類型會被省略。用戶端 **SHOULD** 比對請求與確認內容，並優雅處理未被支援的類型。

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/subscriptions/acknowledged",
  "params": {
    "_meta": { "io.modelcontextprotocol/subscriptionId": 1 },
    "notifications": {
      "toolsListChanged": true,
      "resourceSubscriptions": ["file:///project/config.json"]
    }
  }
}
```

**多重併發訂閱**：用戶端 **MAY** 同時持有多個訂閱。所有串流訊息都攜帶
`io.modelcontextprotocol/subscriptionId`，在 stdio（所有訊息共用單一通道）上
用戶端 **MUST** 依此欄位解多工。

**優雅關閉（Graceful Closure）**：

伺服器主動結束訂閱（例如關機）時，**SHOULD** 先以空 Result 回應原本的
`subscriptions/listen` 請求，再關閉串流：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "complete",
    "_meta": { "io.modelcontextprotocol/subscriptionId": 1 }
  }
}
```

收到此回應代表訂閱正常結束；若串流未附此回應即中斷，代表非預期斷線，
用戶端 **MAY** 據以觸發重連。在 **stdio** 上，連線中斷後重建時用戶端 **MUST**
重新送出 `subscriptions/listen`——伺服器不跨重連保留任何訂閱狀態。

**保活（Keep-alive）**：對長效串流（尤其是 `subscriptions/listen`），伺服器建議
定期發出 SSE 註解行（以冒號開頭，例如 `:\r\n`），避免中介設備或用戶端閒置逾時關閉連線。

#### 2.4.2 主要通知類型

| 通知類型 | 方向 | 管道 | 狀態 |
|----------|------|------|------|
| `notifications/progress` | S→C | 請求回應串流 | Active |
| `notifications/message` | S→C | 請求回應串流 | **Deprecated**（隨 Logging） |
| `notifications/tools/list_changed` | S→C | `subscriptions/listen` | Active |
| `notifications/resources/list_changed` | S→C | `subscriptions/listen` | Active |
| `notifications/resources/updated` | S→C | `subscriptions/listen` | Active |
| `notifications/prompts/list_changed` | S→C | `subscriptions/listen` | Active |
| `notifications/subscriptions/acknowledged` | S→C | `subscriptions/listen` | Active |
| `notifications/tasks` | S→C | `subscriptions/listen` | Tasks 擴充 |
| `notifications/cancelled` | C→S | **僅 stdio** | Active |
| `notifications/initialized` | C→S | — | **已移除** |
| `notifications/roots/list_changed` | C→S | — | **已移除** |
| `notifications/elicitation/complete` | S→C | — | **已移除** |

> **傳輸差異**：在 Streamable HTTP 上，**關閉 SSE 回應串流本身就是取消訊號**，
> 不預期也不需要 `notifications/cancelled` 訊息。該通知僅用於 stdio。

#### 2.4.3 進度通知範例

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "operation-123",
    "progress": 50,
    "total": 100,
    "message": "處理中... 50%"
  }
}
```

進度通知需由用戶端在原請求的 `_meta.progressToken` 中主動開啟；
伺服器僅能在該請求自身的回應串流上回送，且**必須**與發起請求相關。

> **💡 實務建議**：
> - 善用 `ttlMs` / `cacheScope` 降低對變更通知的依賴，減少長效串流數量。
> - 避免過於頻繁的通知；高頻事件應在 Server 端聚合後再送出。
> - 訂閱串流是有成本的資源：企業部署應對每連線／每租戶的併發訂閱數設上限。

---

### 2.5 多輪往返請求（Multi Round-Trip Requests, MRTR）

MRTR（SEP-2322）是 `2026-07-28` 為了在**無狀態協議下仍能支援伺服器索取輸入**
所引入的模式，取代了先前「伺服器主動送出 `roots/list`、`sampling/createMessage`、
`elicitation/create` 請求」的做法。

> **這是破壞性變更**：伺服器 **MUST** 以 MRTR 傳遞所有 Server-to-Client 請求；
> 舊的伺服器主動請求模式**不再受支援**。

#### 2.5.1 高階流程

```mermaid
sequenceDiagram
    participant U as User
    participant C as Client
    participant S as Server

    C->>S: tools/call (id: 1)
    note over S: 需要更多資訊
    S-->>C: InputRequiredResult (id: 1)<br/>inputRequests + requestState
    note over C,S: 原請求就此終止

    C->>U: 向使用者索取輸入
    U-->>C: 提供回覆

    note over C: 以「新的 id」重試原請求<br/>附上 inputResponses 與 requestState
    C->>S: tools/call (id: 2)
    note over S: 由 requestState 重建上下文<br/>完成執行
    S-->>C: Result (id: 2, resultType: complete)
```

關鍵在於：**每一步的請求都完全獨立**。處理重試的伺服器實例不需要任何
重試請求本身以外的資訊——這正是可在 Round-Robin 負載平衡下運作的原因。

#### 2.5.2 核心型別

**`InputRequests`**：伺服器指派的字串識別碼 → 請求物件的對應表。
值必須是 `ElicitRequest`、`CreateMessageRequest` 或 `ListRootsRequest` 之一。

```json
{
  "github_login": {
    "method": "elicitation/create",
    "params": {
      "mode": "form",
      "message": "Please provide your GitHub username",
      "requestedSchema": {
        "type": "object",
        "properties": { "name": { "type": "string" } },
        "required": ["name"]
      }
    }
  },
  "capital_of_france": {
    "method": "sampling/createMessage",
    "params": {
      "messages": [
        { "role": "user", "content": { "type": "text", "text": "What is the capital of France?" } }
      ],
      "systemPrompt": "You are a helpful assistant.",
      "maxTokens": 100
    }
  }
}
```

**`InputResponses`**：鍵對應 `InputRequests`，值為用戶端對每個請求的結果。

```json
{
  "github_login": {
    "action": "accept",
    "content": { "name": "octocat" }
  },
  "capital_of_france": {
    "role": "assistant",
    "content": { "type": "text", "text": "The capital of France is Paris." },
    "model": "claude-3-sonnet-20240307",
    "stopReason": "endTurn"
  }
}
```

**`InputRequiredResult`**：

| 欄位 | 必要 | 說明 |
|------|------|------|
| `resultType` | 是 | 固定為 `"input_required"` |
| `inputRequests` | 可選 | 用戶端必須履行的伺服器請求對應表 |
| `requestState` | 可選 | **不透明字串**，僅對伺服器有意義。用戶端 **MUST NOT** 檢視、解析、修改或做任何假設 |

伺服器 **MUST** 在每個 `InputRequiredResult` 中至少包含 `inputRequests` 或 `requestState` 之一。

#### 2.5.3 適用的請求類型

| 用戶端請求 | 支援 `InputRequiredResult` |
|------------|---------------------------|
| `tools/call` | ✅ |
| `resources/read` | ✅ |
| `prompts/get` | ✅ |
| 其他所有請求 | ❌ 伺服器 **MUST NOT** 回傳 |

#### 2.5.4 實作規則摘要

**伺服器端（Server Requirements）**：

1. **MAY** 對任何支援的請求回傳 `InputRequiredResult`。
2. `inputRequests` 的鍵由伺服器指派，**MUST** 在該請求範圍內唯一。
3. `requestState` 格式自由（Base64 JSON、加密 JWT、序列化二進位皆可）。
4. **MUST** 將用戶端傳回的 `requestState` 視為**攻擊者可控輸入**。
   若其影響授權、資源存取或商業邏輯，**MUST** 以 HMAC 或 AEAD 保護完整性，
   並拒絕驗證失敗的狀態。僅當竄改最壞只會導致請求失敗時，才可省略完整性保護。
5. 為防重放攻擊，**SHOULD** 在完整性保護的 `requestState` 內含：
   - 經認證的主體（principal），拒絕由不同主體提出的狀態；
   - 短期有效期（TTL），逾期即拒；
   - 原始請求的識別（方法名 + 關鍵參數摘要），不符即拒。
6. **MUST NOT** 送出用戶端未宣告支援的 `inputRequests` 類型。
7. **MUST NOT** 假設用戶端一定會履行或重試；**MAY** 對同一請求多次回傳
   `InputRequiredResult` 以反覆索取資訊。

**用戶端（Client Requirements）**：

1. 收到含 `inputRequests` 的結果時，**MUST** 先取得所需輸入再重試原請求；
   若不含 `inputRequests`，**MAY** 立即重試。
2. 若含 `requestState`，重試時 **MUST** 原樣回傳；若不含，重試時 **MUST NOT** 自行加上。
3. 重試的 JSON-RPC `id` **MUST** 與原請求不同——它們是獨立的請求。
4. `inputRequests` 與 `requestState` **MUST** 只作用於該原請求的重試，
   不得用於任何平行進行的其他請求。

#### 2.5.5 錯誤處理

- 伺服器 **SHOULD** 驗證 `InputResponses` 結構與內容可正確解析。
- 協議層錯誤（JSON 格式錯誤、Schema 不符、內部錯誤）**SHOULD** 回傳 JSON-RPC 錯誤回應。
- 對於無法辨識或不需要的額外參數，伺服器 **SHOULD** 忽略。
- 若用戶端未提供全部所需資訊，且缺漏部分為完成請求所必需，
  伺服器 **SHOULD** 回傳新的 `InputRequiredResult` 再次索取，而非回傳錯誤。

> **⚠️ 安全考量（重點）**：`requestState` 會經過用戶端。惡意或被入侵的用戶端可能嘗試竄改，
> 藉以改變伺服器行為、繞過授權檢查或破壞伺服器邏輯。
> 上述第 4、5 點的完整性保護與重放防護是**強制性的安全控制，不可省略**。
> 需要「僅能使用一次」語意者（例如一次性兌換），**MUST** 於伺服器端額外強制該不變式。

---

## 第三章：傳輸層深度解析

### 3.1 STDIO Transport

#### 3.1.1 適用場景：本地進程通訊

STDIO Transport 透過標準輸入/輸出進行通訊，適用於：

- ✅ 本地工具整合
- ✅ 開發測試環境
- ✅ 單一使用者場景
- ✅ 需要存取本地資源
- ❌ 不適合多使用者共享
- ❌ 不適合遠端存取

```mermaid
graph LR
    Host[MCP Host] -->|stdout| Server[MCP Server]
    Server -->|stdin| Host
    
    subgraph "同一台機器"
        Host
        Server
    end
```

#### 3.1.2 配置方式與範例

**Claude Desktop 配置（claude_desktop_config.json）**：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": ["/path/to/filesystem-server/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "database": {
      "command": "python",
      "args": ["-m", "database_server"],
      "env": {
        "DB_CONNECTION": "postgresql://localhost/mydb"
      }
    }
  }
}
```

**配置說明**：

| 欄位 | 說明 | 範例 |
|------|------|------|
| `command` | 執行命令 | `node`、`python`、`npx` |
| `args` | 命令參數 | 腳本路徑、模組名稱 |
| `env` | 環境變數 | 資料庫連線字串等 |

#### 3.1.3 效能特性與限制

| 特性 | 說明 |
|------|------|
| **延遲** | 極低（毫秒級） |
| **吞吐量** | 受限於 pipe buffer size |
| **穩定性** | 依賴進程管理 |
| **除錯** | 需要額外日誌機制（`2026-07-28` 建議寫入 `stderr`） |

**限制**：
- 無法跨機器通訊
- 進程重啟會中斷連接
- 除錯較為困難

**`2026-07-28` 對 stdio 的重點規則**：

| 項目 | 規則 |
|------|------|
| 交握 | **無** `initialize`／`initialized`。連線建立即可送出請求 |
| 進程 ≠ 對話 | 單一 stdio 進程 **MUST NOT** 被視為單一對話或工作階段 |
| 時代偵測 | 用戶端 **SHOULD** 以 `server/discover` 作為探針（見 [3.4.2](#342-stdio-上的時代偵測)） |
| 取消 | `notifications/cancelled` **僅**適用於 stdio |
| 訂閱 | 斷線重連後，用戶端 **MUST** 重新送出 `subscriptions/listen` |
| 解多工 | 所有訊息共用單一通道，用戶端 **MUST** 依 `subscriptionId` 區分訂閱串流 |
| 日誌 | 伺服器 **MUST NOT** 將非 MCP 訊息寫入 `stdout`；診斷輸出一律走 `stderr` |

---

### 3.2 Streamable HTTP Transport

#### 3.2.1 適用場景：遠端伺服器通訊

HTTP Transport 適用於需要遠端存取的場景：

- ✅ 團隊共享服務
- ✅ 雲端部署
- ✅ 需要認證授權
- ✅ 負載均衡
- ❌ 延遲較高
- ❌ 需要網路連接

```mermaid
graph LR
    subgraph "用戶端"
        Client[MCP Client]
    end
    
    subgraph "伺服器端"
        Server[MCP Server]
        DB[(資料庫)]
        API[外部 API]
    end
    
    Client -->|HTTP POST| Server
    Server -->|SSE| Client
    Server --> DB
    Server --> API
```

#### 3.2.2 HTTP POST 與 Server-Sent Events

> **⚠️ `2026-07-28` 破壞性變更**：Streamable HTTP 大幅簡化。
> **只保留 POST**；GET 與 DELETE 皆回傳 `405 Method Not Allowed`；
> `Mcp-Session-Id` 與 `Last-Event-ID` 標頭一律忽略；**不再支援串流可恢復性（resumability）**。

**端點與方法**：

| 方法 | `2025-11-25` | `2026-07-28` |
|------|-------------|-------------|
| `POST /mcp` | 送出請求／通知／回應 | **僅**送出單一請求或通知 |
| `GET /mcp` | 開啟伺服器推送 SSE 串流 | `405 Method Not Allowed`（改用 `subscriptions/listen`） |
| `DELETE /mcp` | 終止 Session | `405 Method Not Allowed`（已無 Session 概念） |

**請求規則**：

- 用戶端 **MUST** 在 `Accept` 標頭同時列出 `application/json` 與 `text/event-stream`。
- Body **MUST** 為**單一** JSON-RPC 請求或通知（不可為批次、不可為回應）。
- 若為通知且伺服器接受，**MUST** 回傳 `202 Accepted` 且無 Body。

**回應規則**：

- 伺服器回傳 `Content-Type: application/json`（單一 JSON 物件）
  或 `Content-Type: text/event-stream`（SSE 串流）。
- SSE 串流的範圍**限於該請求**。串流上 **MAY** 先送出
  `notifications/progress` 與 `notifications/message`，最終回應 **SHOULD** 終止該串流。
- 伺服器 **MUST NOT** 在任何串流上送出獨立的 JSON-RPC 請求
  （Server-to-Client 請求一律走 MRTR）。

**HTTP POST 範例**（自我描述請求 + `2026-07-28` 必要標頭）：

```http
POST /mcp HTTP/1.1
Host: mcp-server.example.com
Content-Type: application/json
Accept: application/json, text/event-stream
Authorization: Bearer <token>
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: execute_sql
Mcp-Param-Region: us-west1

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "execute_sql",
    "arguments": { "region": "us-west1", "query": "SELECT 1" },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {},
      "io.modelcontextprotocol/clientInfo": { "name": "my-app", "version": "1.0" }
    }
  }
}
```

**SSE 回應範例**：

```http
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache
X-Accel-Buffering: no

event: message
data: {"jsonrpc":"2.0","method":"notifications/progress","params":{"progressToken":"t1","progress":50,"total":100}}

event: message
data: {"jsonrpc":"2.0","id":1,"result":{"resultType":"complete","content":[{"type":"text","text":"OK"}]}}
```

- 伺服器 **SHOULD** 於 SSE 回應加上 `X-Accel-Buffering: no`，
  避免反向代理（Nginx 等）緩衝造成串流延遲。
- 長效串流 **SHOULD** 定期送出 SSE 註解行（`:\r\n`）作為保活。

**取消（Cancellation）**：

在 Streamable HTTP 上，**關閉 SSE 回應串流即為取消訊號**。
用戶端不需（也不應）送出 `notifications/cancelled`——該通知僅適用於 stdio。

```mermaid
sequenceDiagram
    participant C as Client
    participant LB as Load Balancer
    participant S1 as Server Pod A
    participant S2 as Server Pod B

    C->>LB: POST /mcp（tools/list，自我描述）
    LB->>S1: 轉發
    S1-->>C: 200 application/json

    C->>LB: POST /mcp（tools/call，自我描述）
    LB->>S2: 轉發（不同 Pod 也可）
    S2-->>C: 200 text/event-stream
    Note over C,S2: 無 Sticky Session 需求
```

#### 3.2.3 認證與授權機制

`2026-07-28` 的授權基線為 **OAuth 2.1 + OIDC**，並在此版本進行多項硬化。

**授權伺服器（AS）身分驗證（SEP-2468）**：

授權伺服器 **SHOULD** 依 RFC 9207 在授權回應中回傳 `iss` 參數；
用戶端在兌換授權碼**之前**，**MUST** 將收到的 `iss` 與先前記錄的發行者比對，不符即中止。
此措施用以緩解 **AS Mix-up 攻擊**——MCP「單一用戶端對多個伺服器」的常見模式，
正是這類攻擊的高風險場景。未來版本將要求「缺少 `iss` 的回應一律拒絕」。

**用戶端註冊優先順序（PR #2858）**：

動態用戶端註冊（DCR，RFC 7591）已**正式標記為棄用**，
改以 **CIMD（Client ID Metadata Documents）** 為標準做法。

```mermaid
graph TD
    A[需要與 AS 建立用戶端身分] --> B{有預先註冊的憑證？}
    B -->|有| C[使用預先註冊憑證]
    B -->|無| D{AS metadata 宣告<br/>client_id_metadata_document_supported？}
    D -->|是| E[使用 CIMD：client_id 為 HTTPS URL]
    D -->|否| F{AS metadata 有<br/>registration_endpoint？}
    F -->|有| G[回退使用 DCR（已棄用）]
    F -->|無| H[提示使用者手動提供憑證]
```

**CIMD 要點**：

| 項目 | 規則 |
|------|------|
| `client_id` 形式 | 具路徑元件的 HTTPS URL，例如 `https://example.com/client.json` |
| 文件必要欄位 | 至少含 `client_id`、`client_name`、`redirect_uris` |
| 一致性 | 文件內的 `client_id` **必須**與文件 URL 完全相同 |
| AS 宣告 | AS metadata 的 `client_id_metadata_document_supported: true` |
| AS 行為 | **SHOULD** 抓取並依 HTTP 快取標頭快取；**MUST** 驗證 redirect URI 與文件結構 |
| 用戶端驗證 | **MAY** 使用 `private_key_jwt` |
| 可攜性 | 同一 CIMD `client_id` 可跨多個 AS 使用，無需重複註冊 |

**DCR 使用注意（SEP-837 / SEP-2352）**：

- 註冊時 **MUST** 明確指定 `application_type`。
  省略時 OIDC 預設為 `"web"`，會導致 localhost 重導向 URI 被拒。
  桌面／行動／CLI／localhost 網頁應用一律使用 `"native"`；遠端瀏覽器應用使用 `"web"`。
- 用戶端 **MUST** 處理註冊失敗，**MAY** 以調整後的值重試。
- 註冊所得憑證**綁定於發出它的 AS**：**MUST** 以 `issuer` 為鍵持久化，
  **MUST NOT** 跨 AS 重用；偵測到 AS 變更（透過受保護資源中繼資料）時 **MUST** 重新註冊。

**分階段授權（Step-up Authorization）**：

伺服器可在流程中途以 `WWW-Authenticate` 標頭要求追加範圍（scope），
用戶端累積既有範圍後重新取得 Token（SEP-2350），無需重跑整段授權。

```mermaid
sequenceDiagram
    participant U as 使用者
    participant C as MCP Client
    participant A as 授權伺服器（AS）
    participant S as MCP Server

    C->>S: 未帶 Token 的請求
    S-->>C: 401 + WWW-Authenticate（resource_metadata）
    C->>S: 取得受保護資源中繼資料
    C->>A: 取得 AS metadata
    Note over C,A: 依 CIMD → DCR 順序建立用戶端身分
    C->>A: 授權請求（PKCE + resource 指示）
    U->>A: 登入並同意
    A-->>C: 授權碼 + iss
    Note over C: MUST 驗證 iss 與記錄一致
    C->>A: 兌換 Token
    A-->>C: Access Token（受眾限定）
    C->>S: 請求 + Bearer Token
    S-->>C: 200 Result
```

**Bearer Token 與 API Key**：

```http
POST /mcp HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

> **企業提醒**：純 API Key（如 `X-API-Key`）不在規範的授權模型內，
> 缺乏受眾限定（audience restriction）與範圍控制。
> 僅建議用於封閉內網或機器對機器情境，且應搭配 `ext-auth` 的
> **OAuth Client Credentials** 擴充逐步汰換。

#### 3.2.4 安全性最佳實踐

**規範層級的強制要求**：

| 要求 | 層級 | 說明 |
|------|------|------|
| 驗證 `Origin` 標頭 | **MUST** | 防範 DNS Rebinding；不符者回傳 `403 Forbidden` |
| 本機執行時綁定 `127.0.0.1` | **SHOULD** | 避免綁定 `0.0.0.0` 對外曝露 |
| 對所有連線實施認證 | **SHOULD** | 見 3.2.3 |
| 標頭與 Body 一致性驗證 | **MUST** | 不符回傳 `400` + `-32020` |
| 一律使用 HTTPS | **MUST**（遠端） | 授權規範前提 |

```text
┌─────────────────────────────────────────────────────────────────┐
│              Streamable HTTP 安全清單（2026-07-28）               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✓ 一律使用 HTTPS（遠端部署）                                     │
│  ✓ MUST 驗證 Origin 標頭，不符回 403                              │
│  ✓ MUST 驗證 MCP-Protocol-Version 標頭與 _meta 值一致             │
│  ✓ MUST 驗證 Mcp-Method / Mcp-Name 與 Body 一致                   │
│  ✓ 本機服務綁定 127.0.0.1，勿綁 0.0.0.0                           │
│  ✓ 以 OAuth 2.1 + OIDC 取代靜態 API Key                           │
│  ✓ 驗證授權回應的 iss 參數（RFC 9207）                            │
│  ✓ 以 issuer 為鍵儲存用戶端憑證，不跨 AS 重用                      │
│  ✓ requestState 以 HMAC/AEAD 保護完整性並設 TTL                   │
│  ✓ 對 tools/call 實施速率限制與併發訂閱數上限                      │
│  ✓ 驗證輸入參數，限制 JSON Schema 深度與驗證時間                   │
│  ✓ 使用 CORS 限制來源                                             │
│  ✓ 記錄存取日誌並定期輪換憑證                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**CORS 配置範例**：

```javascript
// Express.js 範例（2026-07-28：僅需允許 POST）
app.use(cors({
  origin: ['https://claude.ai', 'https://your-app.com'],
  methods: ['POST'],
  allowedHeaders: [
    'Content-Type',
    'Authorization',
    'MCP-Protocol-Version',
    'Mcp-Method',
    'Mcp-Name'
  ],
  credentials: true
}));
```

> **⚠️ 安全警告**：
> - 永遠不要在程式碼中硬編碼認證憑證
> - 使用環境變數或安全的密鑰管理服務（Vault、KMS、Key Vault）
> - 定期審計存取日誌
> - `clientInfo` / `serverInfo` 為未驗證的自我宣告，**不得**作為安全決策依據

---

### 3.3 標頭路由、快取與可觀測性

#### 3.3.1 必要 HTTP 標頭（SEP-2243）

`2026-07-28` 將關鍵路由資訊提升至 HTTP 標頭，讓 API 閘道、WAF 與快取層
**無需解析 JSON Body** 即可做出路由與策略決策。

| 標頭 | 必要性 | 值 |
|------|--------|-----|
| `MCP-Protocol-Version` | **MUST** | 必須與 `_meta.io.modelcontextprotocol/protocolVersion` 相同 |
| `Mcp-Method` | **MUST** | 必須與 JSON-RPC `method` 欄位相同 |
| `Mcp-Name` | 條件式 **MUST** | 對 `tools/call`、`resources/read`、`prompts/get`：必須等於 `params.name` 或 `params.uri` |
| `Mcp-Param-{Name}` | 條件式 | 由工具 Schema 的 `x-mcp-header` 註記產生 |

#### 3.3.2 `x-mcp-header`：將工具參數提升為標頭

工具可在 `inputSchema` 的屬性上加註 `x-mcp-header`，指示用戶端將該參數值
鏡射到 HTTP 標頭 `Mcp-Param-{Name}`：

```json
{
  "name": "execute_sql",
  "inputSchema": {
    "type": "object",
    "properties": {
      "region": {
        "type": "string",
        "x-mcp-header": "Region"
      },
      "query": { "type": "string" }
    },
    "required": ["region", "query"]
  }
}
```

**約束條件**（用戶端 **MUST** 支援，違反者 **MUST** 從 `tools/list` 結果排除該工具並 **SHOULD** 記錄警告）：

| 約束 | 說明 |
|------|------|
| 非空字串 | 必須符合 RFC 9110 的 token 語法 |
| 無 CR/LF | 防止標頭注入 |
| 大小寫不敏感唯一 | 同一工具內不得重複 |
| 型別限制 | 僅允許 `integer`、`string`、`boolean`；**不允許 `number`** |
| 整數範圍 | 必須落在 JavaScript 安全整數範圍內 |
| 靜態可達 | 僅能經由 `properties` 鏈到達；不得位於 `items`、`oneOf`/`anyOf`/`allOf`/`not`、`if`/`then`/`else`、`$ref` 之內 |

#### 3.3.3 標頭值編碼

含非 ASCII 字元、控制字元或前後空白的值，**MUST** 以下列哨符格式編碼：

```text
=?base64?{Base64EncodedValue}?=
```

哨符標記為小寫且大小寫敏感。此規則同時適用於 `Mcp-Name` 與 `Mcp-Param-*`。
值本身若恰好符合哨符樣式，也**必須**編碼以避免歧義。

```http
Mcp-Name: =?base64?5rqW5YKZ5aCx5ZGK?=
Mcp-Param-Region: us-west1
```

#### 3.3.4 伺服器端驗證與 `-32020`

伺服器 **MUST** 驗證標頭與 Body 的一致性。任一不符、缺漏或格式錯誤時：

- HTTP 狀態 **MUST** 為 `400 Bad Request`
- JSON-RPC 錯誤碼 **MUST** 為 `-32020`（`HeaderMismatch`）
- 整數值比對 **SHOULD** 採數值比較而非字串比較
- 中介設備（閘道／代理）**MUST** 回傳 HTTP 錯誤，但不必回傳 JSON-RPC 錯誤物件

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32020,
    "message": "Header mismatch: Mcp-Name does not match params.name"
  }
}
```

#### 3.3.5 快取控制：`ttlMs` 與 `cacheScope`（SEP-2549）

在無狀態架構下，`listChanged` 通知不足以支撐效率，因此 `2026-07-28` 引入
`CacheableResult` 介面。以下方法的結果**必須**包含這兩個欄位：

`tools/list`、`prompts/list`、`resources/list`、`resources/templates/list`、`resources/read`

| 欄位 | 型別 | 說明 |
|------|------|------|
| `ttlMs` | `number` | 新鮮度提示（毫秒）。`0` 表示不可快取 |
| `cacheScope` | `"public"` \| `"private"` | `public` 可跨使用者共用；`private` 僅限單一使用者 |

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "complete",
    "tools": [ /* ... */ ],
    "ttlMs": 3600000,
    "cacheScope": "public"
  }
}
```

> **效能提示**：規範建議伺服器以**確定性順序**回傳 `tools/list` 的工具清單。
> 順序穩定不僅讓用戶端能安全快取，也能大幅提升 LLM 的 Prompt Cache 命中率，
> 直接反映在延遲與 Token 成本上。

#### 3.3.6 分散式追蹤（SEP-414）

`_meta` 保留三個**不需前綴**的鍵（規範明訂的例外）：

| 鍵 | 標準 |
|----|------|
| `traceparent` | W3C Trace Context |
| `tracestate` | W3C Trace Context |
| `baggage` | W3C Baggage |

```json
{
  "params": {
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {},
      "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
      "tracestate": "vendor=abc123"
    }
  }
}
```

如此可建立橫跨「主機應用 → Client SDK → MCP Server → 下游服務」的**單一 Span 樹**。
對應的語意慣例請見 [OpenTelemetry gen-ai/mcp semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/)。

---

### 3.4 傳輸層相容性策略

#### 3.4.1 HTTP 上的時代偵測

```mermaid
graph TD
    A[送出 Modern 請求] --> B{HTTP 狀態}
    B -->|2xx| C[Modern 伺服器]
    B -->|400| D{Body 是否為可辨識的<br/>Modern JSON-RPC 錯誤？}
    D -->|是| E[Modern 伺服器<br/>依 supported 清單重試]
    D -->|否／空 Body| F[回退：送出 initialize]
    F --> G{成功？}
    G -->|是| H[Legacy 伺服器]
    G -->|否| I[再回退至 HTTP&#43;SSE 探測]
```

**判定準則**：`400 Bad Request` 且 Body 為可辨識的 Modern JSON-RPC 錯誤
（例如 `-32022`）⇒ 對方是 Modern 伺服器，僅是版本不合，應挑選共同版本重試。
若 Body 為空或無法辨識 ⇒ 極可能是 Legacy 伺服器對未知請求的通用拒絕，
此時回退至 `initialize`。

#### 3.4.2 stdio 上的時代偵測

stdio 沒有 HTTP 狀態碼可用，因此用戶端 **SHOULD** 以 `server/discover` 作為探針：

- 成功回應 ⇒ Modern 伺服器，取用其 `supportedVersions`。
- 回傳非 Modern 錯誤或逾時 ⇒ 視為 Legacy，回退至 `initialize`。

Modern 用戶端對 Legacy stdio 伺服器**沒有可行的通訊路徑**；
先送 `server/discover` 的價值在於**確定性地快速失敗**，而非在真正的業務請求上發生語意不明的逾時。

#### 3.4.3 快取與再探測

時代判定是**伺服器層級**的屬性：

| 傳輸 | 快取範圍 | 建議 |
|------|----------|------|
| stdio | 伺服器進程生命週期 | 進程結束即失效 |
| HTTP | 來源（origin） | **MAY** 跨用戶端重啟持久化 |

若基於快取的假設後續失敗，用戶端 **SHOULD** 重新探測。

#### 3.4.4 伺服器端的雙時代支援建議

| 情境 | 建議做法 |
|------|----------|
| 僅支援 Modern | 對 `initialize` 回傳的錯誤訊息中 **SHOULD** 明列支援的協議版本——這常是 Legacy 用戶端唯一能顯示給使用者的診斷資訊 |
| 雙時代 | 依請求是否含 `_meta.protocolVersion` 分流至 Modern／Legacy 處理路徑 |
| 支援 `2025-06-18` 之前的用戶端 | **MAY** 將缺少 `MCP-Protocol-Version` 標頭的請求視為 `2025-03-26` |

完整的遷移執行步驟請見 [第十一章：2026-07-28 遷移指南](#第十一章2026-07-28-遷移指南)。

---

## 第四章：實戰開發指南

### 4.1 開發環境設置

#### 4.1.1 SDK 選擇與安裝

自 `2026-07-28` 起，MCP 導入 **SDK 分級制度**。Tier 1 SDK 由核心維護者直接維護，
承諾在規範發布後的既定窗口內跟進；Tier 2 為社群維護，跟進時程不保證。

**Tier 1（官方維護）**：

| SDK | 語言／執行環境 | 套件名稱 | `2026-07-28` 狀態 |
|-----|---------------|----------|------------------|
| **TypeScript SDK** | Node.js 18+ | `@modelcontextprotocol/sdk` | GA |
| **Python SDK** | Python 3.10+ | `mcp` | GA |
| **Go SDK** | Go 1.21+ | `github.com/modelcontextprotocol/go-sdk` | GA |
| **C# SDK** | .NET 8+ | `ModelContextProtocol` | GA |

**Tier 2（社群維護）**：

| SDK | 語言 | `2026-07-28` 狀態 |
|-----|------|------------------|
| Rust SDK | Rust | Beta |
| Java SDK | Java 17+ | 社群維護，跟進時程視社群進度 |
| Kotlin / Swift / Ruby / PHP 等 | 各語言 | 依社群進度 |

> **選型建議**：企業專案若對協議版本跟進速度有要求，**應優先選用 Tier 1 SDK**。
> 採用 Tier 2 SDK 時，應在架構決策紀錄（ADR）中明列版本落後風險與緩解方案，
> 並以官方 [Conformance Suite](https://github.com/modelcontextprotocol/conformance) 驗證實際符規程度。
>
> 本手冊的程式範例以 Java 撰寫以維持一致性，實作 API 名稱請以所選 SDK 的實際版本為準。

**Python SDK 安裝**：

```bash
# 使用 pip 安裝
pip install mcp

# 或使用 uv（推薦）
uv add mcp

# 安裝開發工具
pip install mcp[cli]
```

**TypeScript SDK 安裝**：

```bash
# 使用 npm
npm install @modelcontextprotocol/sdk

# 或使用 pnpm
pnpm add @modelcontextprotocol/sdk

# 安裝 CLI 工具
npm install -g @modelcontextprotocol/inspector
```

#### 4.1.2 開發工具介紹（MCP Inspector）

**MCP Inspector** 是官方提供的除錯工具，可用於測試 MCP Server：

```bash
# 啟動 Inspector
npx @modelcontextprotocol/inspector

# 連接到本地 Server
npx @modelcontextprotocol/inspector node /path/to/server.js
```

**Inspector 功能**：

```text
┌─────────────────────────────────────────────────────────────────┐
│                    MCP Inspector 功能                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📋 工具列表    檢視 Server 提供的所有工具                        │
│  📁 資源瀏覽    瀏覽可用資源並讀取內容                            │
│  💬 提示測試    測試 Prompts 並查看結果                          │
│  🔧 互動測試    手動呼叫工具並檢視回應                            │
│  📊 日誌監控    即時查看 Server 日誌                             │
│  🔍 協議檢查    檢視原始 JSON-RPC 訊息                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.1.3 專案結構建議

**Python 專案結構**：

```text
my-mcp-server/
├── pyproject.toml          # 專案配置
├── README.md               # 說明文件
├── src/
│   └── my_mcp_server/
│       ├── __init__.py
│       ├── __main__.py     # 入口點
│       ├── server.py       # Server 主程式
│       ├── tools/          # 工具定義
│       │   ├── __init__.py
│       │   ├── file_tools.py
│       │   └── db_tools.py
│       ├── resources/      # 資源處理
│       │   ├── __init__.py
│       │   └── handlers.py
│       └── utils/          # 工具函數
│           ├── __init__.py
│           └── helpers.py
├── tests/                  # 測試檔案
│   ├── test_tools.py
│   └── test_resources.py
└── config/                 # 配置檔案
    └── settings.yaml
```

**TypeScript 專案結構**：

```text
my-mcp-server/
├── package.json
├── tsconfig.json
├── README.md
├── src/
│   ├── index.ts           # 入口點
│   ├── server.ts          # Server 主程式
│   ├── tools/
│   │   ├── index.ts
│   │   ├── fileTools.ts
│   │   └── dbTools.ts
│   ├── resources/
│   │   ├── index.ts
│   │   └── handlers.ts
│   └── utils/
│       ├── index.ts
│       └── helpers.ts
├── tests/
│   ├── tools.test.ts
│   └── resources.test.ts
└── dist/                  # 編譯輸出
```

---

### 4.2 開發 MCP Server

#### 4.2.1 基礎範例：最簡單的 MCP Server

**Python 版本**：

```python
#!/usr/bin/env python3
"""
最簡單的 MCP Server 範例
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# 建立 Server 實例
server = Server("simple-server")

# 定義工具列表
@server.list_tools()
async def list_tools() -> list[Tool]:
    """回傳可用工具列表"""
    return [
        Tool(
            name="hello",
            description="回傳問候訊息",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "要問候的名字"
                    }
                },
                "required": ["name"]
            }
        )
    ]

# 實作工具處理
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """處理工具呼叫"""
    if name == "hello":
        user_name = arguments.get("name", "World")
        return [TextContent(type="text", text=f"Hello, {user_name}!")]
    
    raise ValueError(f"Unknown tool: {name}")

# 主程式入口
async def main():
    """啟動 Server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

**TypeScript 版本**：

```typescript
#!/usr/bin/env node
/**
 * 最簡單的 MCP Server 範例
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// 建立 Server 實例
const server = new Server(
  {
    name: "simple-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 處理工具列表請求
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "hello",
        description: "回傳問候訊息",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "要問候的名字",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

// 處理工具呼叫請求
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "hello") {
    const userName = (args as { name: string }).name || "World";
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${userName}!`,
        },
      ],
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

// 啟動 Server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Simple MCP Server running on stdio");
}

main().catch(console.error);
```

#### 4.2.2 註冊與能力揭露流程

> **⚠️ `2026-07-28` 變更**：交握流程已移除。伺服器不再處理 `initialize`，
> 改為實作 `server/discover`（**MUST**），並由每個請求的 `_meta` 自帶協議版本與用戶端能力。
> 詳見 [2.2.3 能力協商與 server/discover](#223-能力協商與-serverdiscover)。

**`2026-07-28` 流程**：

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    Note over S: Server 啟動
    S->>S: 載入設定
    S->>S: 註冊 Handlers（含 server/discover）

    Note over C: 首次接觸（可選，結果可快取）
    C->>S: server/discover
    S-->>C: supportedVersions / capabilities / extensions<br/>+ ttlMs + cacheScope

    Note over C,S: 之後每個請求皆自我描述
    C->>S: tools/call（_meta 含 protocolVersion + clientCapabilities）
    S-->>C: resultType: complete
```

**`2025-11-25` 舊流程（僅供對照，已移除）**：

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    C->>S: initialize
    S->>S: 驗證版本
    S->>S: 設定能力
    S-->>C: initialize response
    C->>S: notifications/initialized

    Note over C,S: 建立 Session 後才可處理請求
```

**能力宣告配置**：

```java
// Java - 宣告 Server 能力（2026-07-28）
import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.spec.ServerCapabilities;

public class MyMcpServer {
    public static void main(String[] args) {
        // 注意：resources 的 subscribe 旗標已移除，
        // 訂閱改由 subscriptions/listen 統一處理
        ServerCapabilities capabilities = ServerCapabilities.builder()
            .tools(ServerCapabilities.ToolCapabilities.builder()
                .listChanged(true)
                .build())
            .resources(ServerCapabilities.ResourceCapabilities.builder()
                .listChanged(true)
                .build())
            .build();

        McpServerOptions options = McpServerOptions.builder()
            .serverName("my-server")
            .serverVersion("1.0.0")
            .capabilities(capabilities)
            .build();

        McpServer server = new McpServer(options);

        // MUST：實作 server/discover
        server.setDiscoverHandler(request ->
            DiscoverResult.builder()
                .resultType("complete")
                .supportedVersions(List.of("2026-07-28"))
                .capabilities(capabilities)
                .ttlMs(3_600_000L)      // 建議快取一小時
                .cacheScope("public")   // 結果不因使用者而異
                .build());
    }
}
```

> **常見誤解**：`server/discover` **不是**新版的 `initialize`。
> 它沒有副作用、不建立任何狀態，用戶端可以完全不呼叫它就直接送出請求，
> 也可以把結果快取後長期重用。

#### 4.2.3 進階範例：實作 Tools（資料庫查詢）

```java
/**
 * 資料庫查詢工具範例
 * DatabaseMcpServer.java
 */
package com.example.mcp;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.sql.*;
import java.util.*;
import java.util.concurrent.CompletableFuture;

public class DatabaseMcpServer {
    
    private final McpServer server;
    private final HikariDataSource dataSource;
    
    public DatabaseMcpServer() {
        // 初始化資料庫連接池
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
        config.setUsername("user");
        config.setPassword("password");
        config.setMinimumIdle(5);
        config.setMaximumPoolSize(20);
        this.dataSource = new HikariDataSource(config);
        
        // 建立 MCP Server
        McpServerOptions options = McpServerOptions.builder()
            .serverName("database-server")
            .serverVersion("1.0.0")
            .capabilities(ServerCapabilities.builder()
                .tools(ServerCapabilities.ToolCapabilities.builder()
                    .listChanged(true)
                    .build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        
        // 註冊工具
        registerTools();
    }
    
    private void registerTools() {
        // 註冊查詢工具
        server.addTool(Tool.builder()
            .name("query_database")
            .description("執行 SQL 查詢（僅支援 SELECT）")
            .inputSchema(Map.of(
                "type", "object",
                "properties", Map.of(
                    "query", Map.of(
                        "type", "string",
                        "description", "SQL SELECT 查詢語句"
                    ),
                    "limit", Map.of(
                        "type", "integer",
                        "description", "結果筆數限制",
                        "default", 100
                    )
                ),
                "required", List.of("query")
            ))
            .build());
        
        // 註冊列表資料表工具
        server.addTool(Tool.builder()
            .name("list_tables")
            .description("列出資料庫中的所有資料表")
            .inputSchema(Map.of(
                "type", "object",
                "properties", Map.of()
            ))
            .build());
        
        // 註冊描述資料表工具
        server.addTool(Tool.builder()
            .name("describe_table")
            .description("取得資料表的 schema 資訊")
            .inputSchema(Map.of(
                "type", "object",
                "properties", Map.of(
                    "table_name", Map.of(
                        "type", "string",
                        "description", "資料表名稱"
                    )
                ),
                "required", List.of("table_name")
            ))
            .build());
        
        // 設定工具處理器
        server.setToolHandler(this::handleToolCall);
    }
    
    private CompletableFuture<CallToolResult> handleToolCall(CallToolRequest request) {
        return CompletableFuture.supplyAsync(() -> {
            String toolName = request.getParams().getName();
            Map<String, Object> arguments = request.getParams().getArguments();
            
            try {
                return switch (toolName) {
                    case "query_database" -> handleQuery(arguments);
                    case "list_tables" -> handleListTables();
                    case "describe_table" -> handleDescribeTable(arguments);
                    default -> CallToolResult.error("Unknown tool: " + toolName);
                };
            } catch (Exception e) {
                return CallToolResult.error("錯誤：" + e.getMessage());
            }
        });
    }
    
    private CallToolResult handleQuery(Map<String, Object> arguments) throws SQLException {
        String query = (String) arguments.get("query");
        int limit = (int) arguments.getOrDefault("limit", 100);
        
        // 安全檢查：僅允許 SELECT
        if (!query.trim().toUpperCase().startsWith("SELECT")) {
            return CallToolResult.text("錯誤：僅支援 SELECT 查詢");
        }
        
        // 加入 LIMIT 限制
        if (!query.toUpperCase().contains("LIMIT")) {
            query = query + " LIMIT " + limit;
        }
        
        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {
            
            ResultSetMetaData metaData = rs.getMetaData();
            int columnCount = metaData.getColumnCount();
            
            // 建立表頭
            StringBuilder result = new StringBuilder();
            result.append("| ");
            for (int i = 1; i <= columnCount; i++) {
                result.append(metaData.getColumnName(i)).append(" | ");
            }
            result.append("\n| ");
            for (int i = 1; i <= columnCount; i++) {
                result.append("--- | ");
            }
            result.append("\n");
            
            // 建立資料列
            int rowCount = 0;
            while (rs.next()) {
                result.append("| ");
                for (int i = 1; i <= columnCount; i++) {
                    result.append(rs.getString(i)).append(" | ");
                }
                result.append("\n");
                rowCount++;
            }
            
            if (rowCount == 0) {
                return CallToolResult.text("查詢無結果");
            }
            
            return CallToolResult.text(result.toString());
        }
    }
    
    private CallToolResult handleListTables() throws SQLException {
        String query = """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
            """;
        
        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {
            
            List<String> tables = new ArrayList<>();
            while (rs.next()) {
                tables.add(rs.getString("table_name"));
            }
            
            StringBuilder result = new StringBuilder("資料表列表：\n");
            for (String table : tables) {
                result.append("- ").append(table).append("\n");
            }
            
            return CallToolResult.text(result.toString());
        }
    }
    
    private CallToolResult handleDescribeTable(Map<String, Object> arguments) throws SQLException {
        String tableName = (String) arguments.get("table_name");
        
        String query = """
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_name = ?
            ORDER BY ordinal_position
            """;
        
        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {
            
            stmt.setString(1, tableName);
            
            try (ResultSet rs = stmt.executeQuery()) {
                StringBuilder result = new StringBuilder();
                result.append("資料表 ").append(tableName).append(" 結構：\n\n");
                result.append("| 欄位名稱 | 資料型別 | 可為空 | 預設值 |\n");
                result.append("| --- | --- | --- | --- |\n");
                
                boolean hasRows = false;
                while (rs.next()) {
                    hasRows = true;
                    result.append("| ")
                        .append(rs.getString("column_name")).append(" | ")
                        .append(rs.getString("data_type")).append(" | ")
                        .append(rs.getString("is_nullable")).append(" | ")
                        .append(rs.getString("column_default") != null ? 
                                rs.getString("column_default") : "-")
                        .append(" |\n");
                }
                
                if (!hasRows) {
                    return CallToolResult.text("資料表 " + tableName + " 不存在");
                }
                
                return CallToolResult.text(result.toString());
            }
        }
    }
    
    public void start() throws Exception {
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
        System.err.println("Database MCP Server running on stdio");
    }
    
    public void shutdown() {
        dataSource.close();
    }
    
    public static void main(String[] args) throws Exception {
        DatabaseMcpServer server = new DatabaseMcpServer();
        Runtime.getRuntime().addShutdownHook(new Thread(server::shutdown));
        server.start();
    }
}
```

#### 4.2.4 進階範例：實作 Resources（檔案系統）

```java
/**
 * 檔案系統資源範例
 * FilesystemMcpServer.java
 */
package com.example.mcp;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import java.io.*;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.*;
import java.util.concurrent.CompletableFuture;

public class FilesystemMcpServer {
    
    private final McpServer server;
    private final Path allowedRoot;
    
    public FilesystemMcpServer(String rootPath) {
        this.allowedRoot = Paths.get(rootPath).toAbsolutePath().normalize();
        
        // 建立 MCP Server
        McpServerOptions options = McpServerOptions.builder()
            .serverName("filesystem-server")
            .serverVersion("1.0.0")
            .capabilities(ServerCapabilities.builder()
                .resources(ServerCapabilities.ResourceCapabilities.builder()
                    .listChanged(true)
                    .subscribe(true)
                    .build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        
        // 註冊資源處理器
        registerHandlers();
    }
    
    /**
     * 檢查路徑是否在允許範圍內
     */
    private boolean isSafePath(Path path) {
        try {
            Path resolved = path.toAbsolutePath().normalize();
            return resolved.startsWith(allowedRoot);
        } catch (Exception e) {
            return false;
        }
    }
    
    /**
     * 猜測 MIME 類型
     */
    private String guessMimeType(Path path) {
        try {
            String contentType = Files.probeContentType(path);
            return contentType != null ? contentType : "application/octet-stream";
        } catch (IOException e) {
            return "application/octet-stream";
        }
    }
    
    private void registerHandlers() {
        // 註冊資源列表處理器
        server.setResourceListHandler(request -> CompletableFuture.supplyAsync(() -> {
            List<Resource> resources = new ArrayList<>();
            
            try {
                Files.walkFileTree(allowedRoot, new SimpleFileVisitor<Path>() {
                    @Override
                    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                        Path relativePath = allowedRoot.relativize(file);
                        String mimeType = guessMimeType(file);
                        
                        resources.add(Resource.builder()
                            .uri("file:///" + relativePath.toString().replace("\\", "/"))
                            .name(file.getFileName().toString())
                            .description("檔案：" + relativePath)
                            .mimeType(mimeType)
                            .build());
                        
                        return FileVisitResult.CONTINUE;
                    }
                });
            } catch (IOException e) {
                System.err.println("掃描目錄錯誤：" + e.getMessage());
            }
            
            return ListResourcesResult.builder()
                .resources(resources)
                .build();
        }));
        
        // 註冊資源讀取處理器
        server.setResourceReadHandler(request -> CompletableFuture.supplyAsync(() -> {
            String uri = request.getParams().getUri();
            
            // 解析 URI
            String relativePath;
            if (uri.startsWith("file:///")) {
                relativePath = uri.substring(8);
            } else {
                throw new IllegalArgumentException("不支援的 URI 格式：" + uri);
            }
            
            Path filePath = allowedRoot.resolve(relativePath);
            
            // 安全檢查
            if (!isSafePath(filePath)) {
                throw new SecurityException("存取被拒絕：路徑不在允許範圍內");
            }
            
            if (!Files.exists(filePath)) {
                throw new IllegalArgumentException("檔案不存在：" + relativePath);
            }
            
            try {
                String mimeType = guessMimeType(filePath);
                
                if (mimeType.startsWith("text/") || mimeType.equals("application/json")) {
                    // 文字檔案
                    String content = Files.readString(filePath);
                    return ReadResourceResult.builder()
                        .contents(List.of(
                            ResourceContent.text(uri, mimeType, content)
                        ))
                        .build();
                } else {
                    // 二進位檔案
                    byte[] bytes = Files.readAllBytes(filePath);
                    String base64Content = Base64.getEncoder().encodeToString(bytes);
                    return ReadResourceResult.builder()
                        .contents(List.of(
                            ResourceContent.blob(uri, mimeType, base64Content)
                        ))
                        .build();
                }
            } catch (IOException e) {
                throw new RuntimeException("讀取檔案錯誤：" + e.getMessage());
            }
        }));
        
        // 註冊資源訂閱處理器
        server.setResourceSubscribeHandler(request -> CompletableFuture.supplyAsync(() -> {
            String uri = request.getParams().getUri();
            // 實作檔案監控邏輯（可使用 WatchService）
            System.err.println("訂閱資源：" + uri);
            return SubscribeResult.builder().build();
        }));
    }
    
    public void start() throws Exception {
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
        System.err.println("Filesystem MCP Server running on stdio");
        System.err.println("Allowed root: " + allowedRoot);
    }
    
    public static void main(String[] args) throws Exception {
        String rootPath = args.length > 0 ? args[0] : System.getProperty("user.home") + "/documents";
        FilesystemMcpServer server = new FilesystemMcpServer(rootPath);
        server.start();
    }
}
```

#### 4.2.5 進階範例：實作 Prompts（互動模板）

```java
/**
 * 提示模板範例
 * PromptsMcpServer.java
 */
package com.example.mcp;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class PromptsMcpServer {
    
    private final McpServer server;
    private final Map<String, PromptDefinition> prompts = new HashMap<>();
    
    // 內部類別：提示定義
    private record PromptDefinition(
        String description,
        List<PromptArgument> arguments
    ) {}
    
    public PromptsMcpServer() {
        // 初始化提示模板
        initializePrompts();
        
        // 建立 MCP Server
        McpServerOptions options = McpServerOptions.builder()
            .serverName("prompts-server")
            .serverVersion("1.0.0")
            .capabilities(ServerCapabilities.builder()
                .prompts(ServerCapabilities.PromptCapabilities.builder()
                    .listChanged(true)
                    .build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        
        // 註冊處理器
        registerHandlers();
    }
    
    private void initializePrompts() {
        // 程式碼審查模板
        prompts.put("code_review", new PromptDefinition(
            "程式碼審查模板",
            List.of(
                PromptArgument.builder()
                    .name("language")
                    .description("程式語言")
                    .required(true)
                    .build(),
                PromptArgument.builder()
                    .name("code")
                    .description("要審查的程式碼")
                    .required(true)
                    .build(),
                PromptArgument.builder()
                    .name("focus")
                    .description("審查重點（security/performance/style）")
                    .required(false)
                    .build()
            )
        ));
        
        // 程式碼解說模板
        prompts.put("explain_code", new PromptDefinition(
            "程式碼解說模板",
            List.of(
                PromptArgument.builder()
                    .name("code")
                    .description("要解說的程式碼")
                    .required(true)
                    .build(),
                PromptArgument.builder()
                    .name("level")
                    .description("解說程度（beginner/intermediate/advanced）")
                    .required(false)
                    .build()
            )
        ));
        
        // 測試案例生成模板
        prompts.put("generate_tests", new PromptDefinition(
            "測試案例生成模板",
            List.of(
                PromptArgument.builder()
                    .name("code")
                    .description("要測試的程式碼")
                    .required(true)
                    .build(),
                PromptArgument.builder()
                    .name("framework")
                    .description("測試框架（junit/testng/mockito）")
                    .required(false)
                    .build()
            )
        ));
    }
    
    private void registerHandlers() {
        // 列出提示模板
        server.setPromptListHandler(request -> CompletableFuture.supplyAsync(() -> {
            List<Prompt> promptList = new ArrayList<>();
            
            prompts.forEach((name, definition) -> {
                promptList.add(Prompt.builder()
                    .name(name)
                    .description(definition.description())
                    .arguments(definition.arguments())
                    .build());
            });
            
            return ListPromptsResult.builder()
                .prompts(promptList)
                .build();
        }));
        
        // 取得提示內容
        server.setPromptGetHandler(request -> CompletableFuture.supplyAsync(() -> {
            String name = request.getParams().getName();
            Map<String, String> arguments = request.getParams().getArguments();
            
            List<PromptMessage> messages = switch (name) {
                case "code_review" -> generateCodeReviewPrompt(arguments);
                case "explain_code" -> generateExplainCodePrompt(arguments);
                case "generate_tests" -> generateTestsPrompt(arguments);
                default -> throw new IllegalArgumentException("Unknown prompt: " + name);
            };
            
            return GetPromptResult.builder()
                .messages(messages)
                .build();
        }));
    }
    
    private List<PromptMessage> generateCodeReviewPrompt(Map<String, String> args) {
        String language = args.getOrDefault("language", "");
        String code = args.getOrDefault("code", "");
        String focus = args.getOrDefault("focus", "general");
        
        Map<String, String> focusInstructions = Map.of(
            "security", "請特別關注安全性問題，包括：輸入驗證、SQL 注入、XSS、認證授權等。",
            "performance", "請特別關注效能問題，包括：演算法複雜度、記憶體使用、資料庫查詢效率等。",
            "style", "請特別關注程式碼風格，包括：命名規範、程式碼結構、可讀性、註解等。",
            "general", "請全面審查程式碼，包括：正確性、安全性、效能、可維護性等面向。"
        );
        
        String promptText = String.format("""
            請審查以下 %s 程式碼：
            
            ```%s
            %s
            ```
            
            %s
            
            請提供：
            1. 發現的問題（按嚴重程度排序）
            2. 改進建議
            3. 整體評分（1-10）
            4. 修改後的程式碼範例（如適用）
            """, 
            language, 
            language.toLowerCase(), 
            code,
            focusInstructions.getOrDefault(focus, focusInstructions.get("general"))
        );
        
        return List.of(
            PromptMessage.builder()
                .role(Role.USER)
                .content(TextContent.builder()
                    .type("text")
                    .text(promptText)
                    .build())
                .build()
        );
    }
    
    private List<PromptMessage> generateExplainCodePrompt(Map<String, String> args) {
        String code = args.getOrDefault("code", "");
        String level = args.getOrDefault("level", "intermediate");
        
        Map<String, String> levelInstructions = Map.of(
            "beginner", "請用簡單易懂的語言解說，避免使用專業術語，多用比喻說明。",
            "intermediate", "請詳細解說程式碼的運作原理，可以使用常見的技術術語。",
            "advanced", "請深入分析程式碼的設計模式、效能考量、潛在問題等進階面向。"
        );
        
        String promptText = String.format("""
            請解說以下程式碼：
            
            ```
            %s
            ```
            
            %s
            
            請包含：
            1. 程式碼的整體功能說明
            2. 逐行或逐段解說
            3. 使用的程式技巧或設計模式
            4. 可能的使用情境
            """,
            code,
            levelInstructions.getOrDefault(level, levelInstructions.get("intermediate"))
        );
        
        return List.of(
            PromptMessage.builder()
                .role(Role.USER)
                .content(TextContent.builder()
                    .type("text")
                    .text(promptText)
                    .build())
                .build()
        );
    }
    
    private List<PromptMessage> generateTestsPrompt(Map<String, String> args) {
        String code = args.getOrDefault("code", "");
        String framework = args.getOrDefault("framework", "junit");
        
        String promptText = String.format("""
            請為以下程式碼生成測試案例：
            
            ```
            %s
            ```
            
            使用 %s 測試框架。
            
            請包含：
            1. 正常情況測試（Happy Path）
            2. 邊界條件測試
            3. 錯誤處理測試
            4. 效能測試（如適用）
            
            請提供完整可執行的測試程式碼。
            """,
            code,
            framework
        );
        
        return List.of(
            PromptMessage.builder()
                .role(Role.USER)
                .content(TextContent.builder()
                    .type("text")
                    .text(promptText)
                    .build())
                .build()
        );
    }
    
    public void start() throws Exception {
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
        System.err.println("Prompts MCP Server running on stdio");
    }
    
    public static void main(String[] args) throws Exception {
        PromptsMcpServer server = new PromptsMcpServer();
        server.start();
    }
}
```

#### 4.2.6 動態工具列表管理與發送通知

> **⚠️ `2026-07-28` 變更**：`notifications/tools/list_changed` 本身仍存在，但**投遞路徑改變**。
> 由於已無 Session，通知**只能**送往用戶端以 `subscriptions/listen` 開啟的訂閱串流，
> 且 **MUST** 在 `_meta` 攜帶 `io.modelcontextprotocol/subscriptionId`。
> 伺服器不能像下方範例那樣「向所有已連線用戶端廣播」——必須改為對每個有效訂閱逐一投遞。
> 詳見 [2.4 通知機制與訂閱串流](#24-通知機制與訂閱串流notifications--subscriptions)。
>
> 此外，工具清單變更後 **SHOULD** 一併調整 `tools/list` 回應的 `ttlMs`，
> 避免用戶端仍在使用過期的快取。

**`2026-07-28` 的投遞方式**：

```java
/**
 * 對所有有效訂閱投遞工具列表變更通知
 */
private void broadcastToolsListChanged() {
    subscriptionRegistry.forEachMatching("toolsListChanged", (subscriptionId, stream) ->
        stream.send(Notification.of("notifications/tools/list_changed", Map.of(
            "_meta", Map.of("io.modelcontextprotocol/subscriptionId", subscriptionId)
        ))));
}
```

**下方範例保留舊版廣播寫法，僅供理解動態工具管理的邏輯骨架**：

```java
/**
 * 動態工具管理範例
 * DynamicToolsMcpServer.java
 */
package com.example.mcp;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ConcurrentHashMap;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class DynamicToolsMcpServer {
    
    private final McpServer server;
    private final Map<String, Tool> registeredTools = new ConcurrentHashMap<>();
    
    public DynamicToolsMcpServer() {
        // 建立 MCP Server
        McpServerOptions options = McpServerOptions.builder()
            .serverName("dynamic-tools-server")
            .serverVersion("1.0.0")
            .capabilities(ServerCapabilities.builder()
                .tools(ServerCapabilities.ToolCapabilities.builder()
                    .listChanged(true)
                    .build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        
        // 初始化內建工具
        initBuiltinTools();
        
        // 註冊處理器
        registerHandlers();
    }
    
    /**
     * 註冊新工具並通知 Client
     */
    public void registerTool(Tool tool) {
        registeredTools.put(tool.getName(), tool);
        // 發送工具列表變更通知
        server.sendNotification("notifications/tools/list_changed", Map.of());
        System.err.println("已註冊工具：" + tool.getName());
    }
    
    /**
     * 取消註冊工具並通知 Client
     */
    public void unregisterTool(String name) {
        if (registeredTools.remove(name) != null) {
            server.sendNotification("notifications/tools/list_changed", Map.of());
            System.err.println("已移除工具：" + name);
        }
    }
    
    private void initBuiltinTools() {
        // 註冊管理工具
        registerTool(Tool.builder()
            .name("register_calculator")
            .description("註冊計算機工具")
            .inputSchema(Map.of(
                "type", "object",
                "properties", Map.of()
            ))
            .build());
        
        registerTool(Tool.builder()
            .name("list_registered_tools")
            .description("列出所有已註冊的工具")
            .inputSchema(Map.of(
                "type", "object",
                "properties", Map.of()
            ))
            .build());
    }
    
    private void registerHandlers() {
        // 工具列表處理器
        server.setToolListHandler(request -> CompletableFuture.supplyAsync(() -> 
            ListToolsResult.builder()
                .tools(new ArrayList<>(registeredTools.values()))
                .build()
        ));
        
        // 工具呼叫處理器
        server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
            String toolName = request.getParams().getName();
            Map<String, Object> arguments = request.getParams().getArguments();
            
            return switch (toolName) {
                case "register_calculator" -> handleRegisterCalculator();
                case "calculate" -> handleCalculate(arguments);
                case "list_registered_tools" -> handleListTools();
                default -> CallToolResult.error("Unknown tool: " + toolName);
            };
        }));
    }
    
    private CallToolResult handleRegisterCalculator() {
        // 動態註冊計算機工具
        Tool calculatorTool = Tool.builder()
            .name("calculate")
            .description("執行數學計算")
            .inputSchema(Map.of(
                "type", "object",
                "properties", Map.of(
                    "expression", Map.of(
                        "type", "string",
                        "description", "數學表達式（例如：2+3*4）"
                    )
                ),
                "required", List.of("expression")
            ))
            .build();
        
        registerTool(calculatorTool);
        
        return CallToolResult.text("Calculator tool registered successfully");
    }
    
    private CallToolResult handleCalculate(Map<String, Object> arguments) {
        String expression = (String) arguments.get("expression");
        
        if (expression == null || expression.isEmpty()) {
            return CallToolResult.error("表達式不能為空");
        }
        
        // 安全檢查：僅允許基本運算符和數字
        if (!expression.matches("[0-9+\\-*/().\\s]+")) {
            return CallToolResult.error("不允許的字元，僅支援數字和基本運算符");
        }
        
        try {
            // 使用 JavaScript 引擎計算表達式
            ScriptEngineManager manager = new ScriptEngineManager();
            ScriptEngine engine = manager.getEngineByName("JavaScript");
            
            if (engine == null) {
                // 如果沒有 JavaScript 引擎，使用簡單的計算方式
                double result = evaluateSimpleExpression(expression);
                return CallToolResult.text("結果：" + result);
            }
            
            Object result = engine.eval(expression);
            return CallToolResult.text("結果：" + result);
            
        } catch (Exception e) {
            return CallToolResult.error("計算錯誤：" + e.getMessage());
        }
    }
    
    private double evaluateSimpleExpression(String expression) {
        // 簡單的表達式計算（僅支援加減乘除）
        expression = expression.replaceAll("\\s+", "");
        
        // 這是一個簡化的實作，生產環境應使用更完善的表達式解析器
        javax.script.ScriptEngineManager mgr = new javax.script.ScriptEngineManager();
        javax.script.ScriptEngine eng = mgr.getEngineByName("nashorn");
        
        if (eng != null) {
            try {
                return ((Number) eng.eval(expression)).doubleValue();
            } catch (Exception e) {
                throw new RuntimeException("無法計算表達式：" + expression);
            }
        }
        
        // 簡單的加法計算作為後備
        try {
            return Double.parseDouble(expression);
        } catch (NumberFormatException e) {
            throw new RuntimeException("無法計算表達式：" + expression);
        }
    }
    
    private CallToolResult handleListTools() {
        StringBuilder result = new StringBuilder("已註冊的工具：\n");
        
        for (Tool tool : registeredTools.values()) {
            result.append("- ").append(tool.getName())
                  .append(": ").append(tool.getDescription())
                  .append("\n");
        }
        
        return CallToolResult.text(result.toString());
    }
    
    public void start() throws Exception {
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
        System.err.println("Dynamic Tools MCP Server running on stdio");
    }
    
    public static void main(String[] args) throws Exception {
        DynamicToolsMcpServer server = new DynamicToolsMcpServer();
        server.start();
    }
}
```

---

### 4.3 開發 MCP Client

#### 4.3.1 基礎範例：連接到 MCP Server

> **⚠️ `2026-07-28` 變更**：下方範例中的 `client.initialize()` 屬於舊版流程。
> 新版用戶端**不需要**（也不能）呼叫 `initialize`，而是在**每個請求**的 `_meta`
> 帶上 `protocolVersion` 與 `clientCapabilities`。SDK 通常已封裝此行為，
> 若需自行控制請參考 [11.3.1 步驟一：建構自我描述請求](#113-client-端遷移步驟)。

**Java Client**：

```java
/**
 * MCP Client 基礎範例
 * McpClientExample.java
 */
package com.example.mcp.client;

import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.McpClientOptions;
import io.modelcontextprotocol.client.transport.StdioClientTransport;
import io.modelcontextprotocol.spec.*;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class McpClientExample {
    
    public static void main(String[] args) throws Exception {
        // 設定 Server 連接參數
        StdioClientTransport transport = new StdioClientTransport(
            "java",                           // 命令
            List.of("-jar", "my-mcp-server.jar")  // 參數
        );
        
        // 建立 Client
        McpClientOptions options = McpClientOptions.builder()
            .clientInfo(ClientInfo.builder()
                .name("example-client")
                .version("1.0.0")
                .build())
            .build();
        
        try (McpClient client = new McpClient(options)) {
            // 連接到 Server
            client.connect(transport);
            
            // 初始化連接
            InitializeResult initResult = client.initialize().get();
            System.out.println("已連接到 Server：" + initResult.getServerInfo().getName());
            
            // 列出可用工具
            ListToolsResult toolsResult = client.listTools().get();
            System.out.println("\n可用工具：");
            for (Tool tool : toolsResult.getTools()) {
                System.out.println("  - " + tool.getName() + ": " + tool.getDescription());
            }
            
            // 呼叫工具
            CallToolResult result = client.callTool(
                "hello",
                Map.of("name", "MCP User")
            ).get();
            
            System.out.println("\n工具回應：" + result.getContent().get(0).getText());
        }
    }
}
```

**TypeScript Client**：

```typescript
/**
 * MCP Client 基礎範例
 */

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

async function main() {
  // 建立 Client
  const client = new Client(
    {
      name: "example-client",
      version: "1.0.0",
    },
    {
      capabilities: {},
    }
  );

  // 建立 Transport
  const transport = new StdioClientTransport({
    command: "node",
    args: ["./server.js"],
  });

  // 連接到 Server
  await client.connect(transport);

  // 列出可用工具
  const tools = await client.listTools();
  console.log("可用工具：");
  for (const tool of tools.tools) {
    console.log(`  - ${tool.name}: ${tool.description}`);
  }

  // 呼叫工具
  const result = await client.callTool({
    name: "hello",
    arguments: { name: "MCP User" },
  });

  console.log("\n工具回應：", result.content[0]);

  // 關閉連接
  await client.close();
}

main().catch(console.error);
```

#### 4.3.2 能力發現與版本協商

**`2026-07-28` 做法**：以 `server/discover` 取得伺服器能力，並將結果依 `ttlMs` 快取。

```java
/**
 * 能力發現範例（2026-07-28）
 * DiscoverExample.java
 */
package com.example.mcp.client;

import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.spec.*;

import java.util.List;
import java.util.Map;

public class DiscoverExample {

    private static final String PROTOCOL_VERSION = "2026-07-28";

    public static void main(String[] args) throws Exception {
        try (McpClient client = McpClient.stdio("java", List.of("-jar", "my-mcp-server.jar"))) {

            // server/discover 無副作用，不建立任何狀態
            DiscoverResult discover = client.discover(clientMeta()).get();

            System.out.println("支援的協議版本：" + discover.getSupportedVersions());
            if (!discover.getSupportedVersions().contains(PROTOCOL_VERSION)) {
                throw new IllegalStateException("無共同支援的協議版本");
            }

            ServerCapabilities caps = discover.getCapabilities();
            if (caps.getTools() != null)     System.out.println("  ✓ Tools");
            if (caps.getResources() != null) System.out.println("  ✓ Resources");
            if (caps.getPrompts() != null)   System.out.println("  ✓ Prompts");

            // 擴充能力（2026-07-28 新增）
            caps.getExtensions().forEach((id, cfg) ->
                System.out.println("  ✓ 擴充：" + id));

            // 依伺服器提示快取，避免每次連線都重新探詢
            capabilityCache.put(serverKey, discover, discover.getTtlMs());
        }
    }

    /** 每個請求都必須攜帶的協議中繼資料 */
    private static Map<String, Object> clientMeta() {
        return Map.of("_meta", Map.of(
            "io.modelcontextprotocol/protocolVersion", PROTOCOL_VERSION,
            "io.modelcontextprotocol/clientCapabilities", Map.of(
                "elicitation", Map.of(),
                "extensions", Map.of("io.modelcontextprotocol/tasks", Map.of())
            ),
            "io.modelcontextprotocol/clientInfo", Map.of(
                "name", "capability-client", "version", "1.0.0")
        ));
    }
}
```

**注意事項**：

| 項目 | 說明 |
|------|------|
| `logging` 能力 | 已棄用，伺服器不應再宣告 |
| `resources.subscribe` | 已移除，改由 `subscriptions/listen` 統一處理 |
| `sampling` / `roots` | 已棄用的**用戶端**能力，新用戶端不應宣告 |
| `extensions` | 新增；鍵為擴充識別碼，空物件表示「支援但無額外設定」 |
| 快取 | 依 `ttlMs` 與 `cacheScope` 快取；`private` 表示結果因使用者而異 |

**`2025-11-25` 舊做法（僅供對照）**：

```java
/**
 * 能力協商範例（已過時）
 * CapabilityNegotiationExample.java
 */
package com.example.mcp.client;

import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.McpClientOptions;
import io.modelcontextprotocol.client.transport.StdioClientTransport;
import io.modelcontextprotocol.spec.*;

import java.util.List;

public class CapabilityNegotiationExample {
    
    public static void main(String[] args) throws Exception {
        StdioClientTransport transport = new StdioClientTransport(
            "java",
            List.of("-jar", "my-mcp-server.jar")
        );
        
        McpClientOptions options = McpClientOptions.builder()
            .clientInfo(ClientInfo.builder()
                .name("capability-client")
                .version("1.0.0")
                .build())
            .build();
        
        try (McpClient client = new McpClient(options)) {
            client.connect(transport);
            
            // 初始化並取得 Server 能力
            InitializeResult initResult = client.initialize().get();
            
            System.out.println("Server 資訊：");
            System.out.println("  名稱：" + initResult.getServerInfo().getName());
            System.out.println("  版本：" + initResult.getServerInfo().getVersion());
            System.out.println("  協議版本：" + initResult.getProtocolVersion());
            
            System.out.println("\nServer 能力：");
            ServerCapabilities caps = initResult.getCapabilities();
            
            if (caps.getTools() != null) {
                System.out.println("  ✓ Tools 支援");
                if (Boolean.TRUE.equals(caps.getTools().getListChanged())) {
                    System.out.println("    - 支援工具列表變更通知");
                }
            }
            
            if (caps.getResources() != null) {
                System.out.println("  ✓ Resources 支援");
                if (Boolean.TRUE.equals(caps.getResources().getSubscribe())) {
                    System.out.println("    - 支援資源訂閱");
                }
                if (Boolean.TRUE.equals(caps.getResources().getListChanged())) {
                    System.out.println("    - 支援資源列表變更通知");
                }
            }
            
            if (caps.getPrompts() != null) {
                System.out.println("  ✓ Prompts 支援");
                if (Boolean.TRUE.equals(caps.getPrompts().getListChanged())) {
                    System.out.println("    - 支援提示列表變更通知");
                }
            }
            
            if (caps.getLogging() != null) {
                System.out.println("  ✓ Logging 支援");
            }
        }
    }
}
```

#### 4.3.3 進階範例：處理通知與錯誤

> **⚠️ `2026-07-28` 補充**：新版用戶端除了下方的重試與通知處理外，還**必須**額外具備兩項能力：
>
> 1. **MRTR 迴圈** —— 收到 `resultType: "input_required"` 時，補上 `inputResponses`
>    與原樣的 `requestState`，以**新的 JSON-RPC id** 重送原請求；並設定輪數上限防止無限迴圈。
>    參見 [11.3.2 步驟二：實作 MRTR 重試迴圈](#113-client-端遷移步驟)。
> 2. **訂閱串流** —— 通知只會出現在 `subscriptions/listen` 開啟的串流上，
>    需依 `subscriptionId` 解多工。參見 [2.4.1 subscriptions/listen](#24-通知機制與訂閱串流notifications--subscriptions)。
>
> 錯誤重試方面，`-32020`（HeaderMismatch）、`-32021`（MissingRequiredClientCapability）
> 與 `-32022`（UnsupportedProtocolVersion）皆屬**用戶端實作缺陷**，
> **不應重試**，應直接修正請求後再送出。

```java
/**
 * 進階 Client 範例：通知處理與錯誤重試
 * McpClientWrapper.java
 */
package com.example.mcp.client;

import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.McpClientOptions;
import io.modelcontextprotocol.client.transport.StdioClientTransport;
import io.modelcontextprotocol.spec.*;

import java.util.*;
import java.util.concurrent.*;
import java.util.function.Consumer;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * 封裝 MCP Client 的進階功能
 */
public class McpClientWrapper implements AutoCloseable {
    
    private static final Logger logger = Logger.getLogger(McpClientWrapper.class.getName());
    
    private final String serverCommand;
    private final List<String> serverArgs;
    private McpClient client;
    private final Map<String, Consumer<Map<String, Object>>> notificationHandlers;
    private final int retryCount;
    private final long retryDelayMs;
    
    public McpClientWrapper(String serverCommand, List<String> serverArgs) {
        this.serverCommand = serverCommand;
        this.serverArgs = serverArgs;
        this.notificationHandlers = new ConcurrentHashMap<>();
        this.retryCount = 3;
        this.retryDelayMs = 1000L;
    }
    
    /**
     * 註冊通知處理器
     */
    public void onNotification(String method, Consumer<Map<String, Object>> handler) {
        notificationHandlers.put(method, handler);
    }
    
    /**
     * 處理接收到的通知
     */
    private void handleNotification(String method, Map<String, Object> params) {
        Consumer<Map<String, Object>> handler = notificationHandlers.get(method);
        if (handler != null) {
            handler.accept(params);
        } else {
            logger.fine("未處理的通知：" + method);
        }
    }
    
    /**
     * 帶重試機制的工具呼叫
     */
    public CompletableFuture<CallToolResult> callToolWithRetry(String name, Map<String, Object> arguments) {
        return CompletableFuture.supplyAsync(() -> {
            Exception lastError = null;
            
            for (int attempt = 0; attempt < retryCount; attempt++) {
                try {
                    return client.callTool(name, arguments).get();
                } catch (Exception e) {
                    lastError = e;
                    logger.warning(String.format("工具呼叫失敗 (嘗試 %d/%d): %s", 
                        attempt + 1, retryCount, e.getMessage()));
                    
                    if (attempt < retryCount - 1) {
                        try {
                            Thread.sleep(retryDelayMs * (attempt + 1));
                        } catch (InterruptedException ie) {
                            Thread.currentThread().interrupt();
                            throw new CompletionException(ie);
                        }
                    }
                }
            }
            
            throw new CompletionException(lastError);
        });
    }
    
    /**
     * 連接到 Server
     */
    public void connect() throws Exception {
        StdioClientTransport transport = new StdioClientTransport(serverCommand, serverArgs);
        
        McpClientOptions options = McpClientOptions.builder()
            .clientInfo(ClientInfo.builder()
                .name("advanced-client")
                .version("1.0.0")
                .build())
            .notificationHandler(this::handleNotification)
            .build();
        
        client = new McpClient(options);
        client.connect(transport);
        client.initialize().get();
    }
    
    /**
     * 取得 Session
     */
    public McpClient getClient() {
        return client;
    }
    
    @Override
    public void close() throws Exception {
        if (client != null) {
            client.close();
        }
    }
    
    // 使用範例
    public static void main(String[] args) throws Exception {
        McpClientWrapper wrapper = new McpClientWrapper(
            "java", 
            List.of("-jar", "my-mcp-server.jar")
        );
        
        // 註冊通知處理器
        wrapper.onNotification("notifications/tools/list_changed", params -> {
            logger.info("工具列表已變更，重新載入...");
            try {
                ListToolsResult tools = wrapper.getClient().listTools().get();
                logger.info("新工具列表：" + tools.getTools().stream()
                    .map(Tool::getName)
                    .toList());
            } catch (Exception e) {
                logger.severe("重新載入工具列表失敗：" + e.getMessage());
            }
        });
        
        wrapper.onNotification("notifications/message", params -> {
            String level = (String) params.getOrDefault("level", "info");
            String message = (String) params.getOrDefault("data", "");
            logger.log(Level.parse(level.toUpperCase()), "Server: " + message);
        });
        
        try {
            wrapper.connect();
            
            // 列出工具
            ListToolsResult tools = wrapper.getClient().listTools().get();
            System.out.println("可用工具數量：" + tools.getTools().size());
            
            // 使用重試機制呼叫工具
            try {
                CallToolResult result = wrapper.callToolWithRetry(
                    "hello",
                    Map.of("name", "World")
                ).get();
                System.out.println("結果：" + result.getContent().get(0).getText());
            } catch (Exception e) {
                System.out.println("工具呼叫失敗：" + e.getMessage());
            }
        } finally {
            wrapper.close();
        }
    }
}
```

#### 4.3.4 多伺服器管理

> **📌 `2026-07-28` 補充**：多伺服器管理器在新版下需額外維護兩項狀態：
>
> | 狀態 | 用途 | 建議實作 |
> |------|------|----------|
> | **世代偵測快取** | 記錄每個伺服器是 `2025-11-25` 還是 `2026-07-28` | 以 origin 為 key，首次連線時探測並快取 |
> | **能力快取** | 存放 `server/discover` 結果與 `ttlMs` | 到期後重新探詢，不依賴連線存活 |
>
> 由於已無 Session，管理器**不再需要維持長連線**；
> 連線中斷後只需重送請求，無需重新交握。只有訂閱串流（`subscriptions/listen`）
> 需要斷線重連邏輯。混合環境的完整策略參見
> [11.5 雙時代（Dual-era）相容部署](#115-雙時代dual-era相容部署)。

```java
/**
 * 多 MCP Server 管理範例
 * MultiServerClient.java
 */
package com.example.mcp.client;

import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.McpClientOptions;
import io.modelcontextprotocol.client.transport.StdioClientTransport;
import io.modelcontextprotocol.spec.*;

import java.util.*;
import java.util.concurrent.*;

/**
 * Server 配置
 */
record ServerConfig(
    String name,
    String command,
    List<String> args,
    String description
) {}

/**
 * 管理多個 MCP Server 連接
 */
public class MultiServerClient implements AutoCloseable {
    
    private final Map<String, McpClient> servers = new ConcurrentHashMap<>();
    private final Map<String, List<String>> serverTools = new ConcurrentHashMap<>();
    
    /**
     * 添加並連接到 Server
     */
    public void addServer(ServerConfig config) throws Exception {
        StdioClientTransport transport = new StdioClientTransport(
            config.command(), 
            config.args()
        );
        
        McpClientOptions options = McpClientOptions.builder()
            .clientInfo(ClientInfo.builder()
                .name("multi-server-client")
                .version("1.0.0")
                .build())
            .build();
        
        McpClient client = new McpClient(options);
        client.connect(transport);
        client.initialize().get();
        
        servers.put(config.name(), client);
        
        // 快取工具列表
        ListToolsResult tools = client.listTools().get();
        List<String> toolNames = tools.getTools().stream()
            .map(Tool::getName)
            .toList();
        serverTools.put(config.name(), toolNames);
        
        System.out.println("已連接到 " + config.name() + "，可用工具：" + toolNames);
    }
    
    /**
     * 根據工具名稱找到對應的 Server
     */
    public Optional<String> findServerForTool(String toolName) {
        for (Map.Entry<String, List<String>> entry : serverTools.entrySet()) {
            if (entry.getValue().contains(toolName)) {
                return Optional.of(entry.getKey());
            }
        }
        return Optional.empty();
    }
    
    /**
     * 智能路由工具呼叫
     */
    public CompletableFuture<CallToolResult> callTool(String toolName, Map<String, Object> arguments) {
        String serverName = findServerForTool(toolName)
            .orElseThrow(() -> new IllegalArgumentException("找不到提供 " + toolName + " 的 Server"));
        
        McpClient client = servers.get(serverName);
        return client.callTool(toolName, arguments);
    }
    
    /**
     * 列出所有 Server 的工具
     */
    public Map<String, List<Map<String, String>>> listAllTools() throws Exception {
        Map<String, List<Map<String, String>>> allTools = new LinkedHashMap<>();
        
        for (Map.Entry<String, McpClient> entry : servers.entrySet()) {
            ListToolsResult tools = entry.getValue().listTools().get();
            List<Map<String, String>> toolInfoList = tools.getTools().stream()
                .map(t -> Map.of(
                    "name", t.getName(),
                    "description", t.getDescription() != null ? t.getDescription() : ""
                ))
                .toList();
            allTools.put(entry.getKey(), toolInfoList);
        }
        
        return allTools;
    }
    
    @Override
    public void close() throws Exception {
        for (McpClient client : servers.values()) {
            try {
                client.close();
            } catch (Exception e) {
                // 記錄錯誤但繼續關閉其他連接
            }
        }
        servers.clear();
        serverTools.clear();
    }
    
    // 使用範例
    public static void main(String[] args) throws Exception {
        MultiServerClient client = new MultiServerClient();
        
        // 配置多個 Server
        List<ServerConfig> serverConfigs = List.of(
            new ServerConfig(
                "filesystem",
                "java",
                List.of("-jar", "filesystem-server.jar"),
                "檔案系統操作"
            ),
            new ServerConfig(
                "database",
                "java",
                List.of("-jar", "database-server.jar"),
                "資料庫查詢"
            ),
            new ServerConfig(
                "github",
                "node",
                List.of("./github-server.js"),
                "GitHub 整合"
            )
        );
        
        try {
            // 連接所有 Server
            for (ServerConfig config : serverConfigs) {
                try {
                    client.addServer(config);
                } catch (Exception e) {
                    System.out.println("無法連接到 " + config.name() + ": " + e.getMessage());
                }
            }
            
            // 列出所有工具
            Map<String, List<Map<String, String>>> allTools = client.listAllTools();
            System.out.println("\n所有可用工具：");
            for (Map.Entry<String, List<Map<String, String>>> entry : allTools.entrySet()) {
                System.out.println("\n" + entry.getKey() + ":");
                for (Map<String, String> tool : entry.getValue()) {
                    System.out.println("  - " + tool.get("name") + ": " + tool.get("description"));
                }
            }
            
            // 智能路由呼叫
            CallToolResult result = client.callTool(
                "read_file", 
                Map.of("path", "/etc/hosts")
            ).get();
            String content = result.getContent().get(0).getText();
            System.out.println("\n讀取檔案結果：" + content.substring(0, Math.min(100, content.length())) + "...");
            
        } finally {
            client.close();
        }
    }
}
```

---

### 4.4 整合到 AI 應用

> **📌 主要用戶端對 `2026-07-28` 的支援狀態**
>
> 規範發布與產品實作之間存在時差。佈建前 **應實際驗證**目標用戶端的實際支援版本，
> 不可僅依據文件描述。實務上建議伺服器**同時支援兩個版本**（雙時代部署），
> 直到目標用戶端完成升級。完整策略參見
> [11.5 雙時代（Dual-era）相容部署](#115-雙時代dual-era相容部署)。
>
> 下方的客戶端設定檔格式（`mcpServers` 區塊、`command` / `args` / `env`）
> 屬於**用戶端自定的啟動設定**，**不屬於 MCP 規範**，
> 因此不受 `2026-07-28` 的協議變更影響，可繼續沿用。

#### 4.4.1 Claude Desktop 整合範例

**配置檔案位置**：
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**配置範例**：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/user/Documents"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    },
    "custom-server": {
      "command": "python",
      "args": ["-m", "my_custom_server"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

#### 4.4.2 Claude Code 整合範例

VS Code 設定（`settings.json`）：

```json
{
  "claude.mcpServers": {
    "workspace-tools": {
      "command": "node",
      "args": ["${workspaceFolder}/.mcp/server.js"],
      "env": {}
    },
    "docker": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-docker"],
      "env": {}
    }
  }
}
```

#### 4.4.3 自訂 AI 應用整合流程

```mermaid
graph TB
    subgraph "整合流程"
        A[1. 初始化 MCP Client] --> B[2. 連接 MCP Server]
        B --> C[3. 探索可用工具]
        C --> D[4. 建立工具描述]
        D --> E[5. 傳送給 LLM]
        E --> F{LLM 決定使用工具?}
        F -->|是| G[6. 執行工具呼叫]
        G --> H[7. 取得結果]
        H --> I[8. 回傳給 LLM]
        I --> E
        F -->|否| J[9. 輸出最終回應]
    end
```

**整合程式碼範例**：

```java
/**
 * 自訂 AI 應用整合 MCP 範例
 * McpEnabledAssistant.java
 */
package com.example.mcp.assistant;

import com.anthropic.client.AnthropicClient;
import com.anthropic.models.*;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.McpClientOptions;
import io.modelcontextprotocol.client.transport.StdioClientTransport;
import io.modelcontextprotocol.spec.*;

import java.util.*;
import java.util.stream.Collectors;

/**
 * 整合 MCP 的 AI 助理
 */
public class McpEnabledAssistant implements AutoCloseable {
    
    private final AnthropicClient anthropic;
    private McpClient mcpClient;
    private List<Map<String, Object>> availableTools;
    
    public McpEnabledAssistant(String anthropicApiKey) {
        this.anthropic = AnthropicClient.builder()
            .apiKey(anthropicApiKey)
            .build();
        this.availableTools = new ArrayList<>();
    }
    
    /**
     * 連接 MCP Server
     */
    public void connectMcp(String command, List<String> args) throws Exception {
        StdioClientTransport transport = new StdioClientTransport(command, args);
        
        McpClientOptions options = McpClientOptions.builder()
            .clientInfo(ClientInfo.builder()
                .name("ai-assistant")
                .version("1.0.0")
                .build())
            .build();
        
        mcpClient = new McpClient(options);
        mcpClient.connect(transport);
        mcpClient.initialize().get();
        
        // 取得並轉換工具格式
        ListToolsResult toolsResponse = mcpClient.listTools().get();
        availableTools = convertToolsForClaude(toolsResponse.getTools());
    }
    
    /**
     * 將 MCP 工具格式轉換為 Claude API 格式
     */
    private List<Map<String, Object>> convertToolsForClaude(List<Tool> mcpTools) {
        return mcpTools.stream()
            .map(tool -> Map.<String, Object>of(
                "name", tool.getName(),
                "description", tool.getDescription() != null ? tool.getDescription() : "",
                "input_schema", tool.getInputSchema()
            ))
            .collect(Collectors.toList());
    }
    
    /**
     * 與助理對話
     */
    public String chat(String userMessage) throws Exception {
        List<Map<String, Object>> messages = new ArrayList<>();
        messages.add(Map.of("role", "user", "content", userMessage));
        
        while (true) {
            // 呼叫 Claude API
            MessageCreateParams params = MessageCreateParams.builder()
                .model("claude-sonnet-4-20250514")
                .maxTokens(4096)
                .tools(availableTools)
                .messages(messages)
                .build();
            
            Message response = anthropic.messages().create(params);
            
            // 檢查是否需要使用工具
            if ("tool_use".equals(response.getStopReason())) {
                // 處理工具呼叫
                List<Map<String, Object>> toolResults = new ArrayList<>();
                
                for (ContentBlock content : response.getContent()) {
                    if (content instanceof ToolUseBlock toolUse) {
                        String toolName = toolUse.getName();
                        Map<String, Object> toolInput = toolUse.getInput();
                        String toolUseId = toolUse.getId();
                        
                        // 透過 MCP 執行工具
                        String toolResult;
                        boolean isError;
                        
                        try {
                            CallToolResult result = mcpClient.callTool(toolName, toolInput).get();
                            toolResult = result.getContent().get(0).getText();
                            isError = false;
                        } catch (Exception e) {
                            toolResult = "工具執行錯誤：" + e.getMessage();
                            isError = true;
                        }
                        
                        toolResults.add(Map.of(
                            "type", "tool_result",
                            "tool_use_id", toolUseId,
                            "content", toolResult,
                            "is_error", isError
                        ));
                    }
                }
                
                // 將結果加入對話
                messages.add(Map.of("role", "assistant", "content", response.getContent()));
                messages.add(Map.of("role", "user", "content", toolResults));
            } else {
                // 沒有工具呼叫，回傳最終回應
                StringBuilder finalResponse = new StringBuilder();
                for (ContentBlock content : response.getContent()) {
                    if (content instanceof TextBlock textBlock) {
                        finalResponse.append(textBlock.getText());
                    }
                }
                return finalResponse.toString();
            }
        }
    }
    
    @Override
    public void close() throws Exception {
        if (mcpClient != null) {
            mcpClient.close();
        }
    }
    
    // 使用範例
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("ANTHROPIC_API_KEY");
        
        try (McpEnabledAssistant assistant = new McpEnabledAssistant(apiKey)) {
            // 連接 MCP Server
            assistant.connectMcp("java", List.of("-jar", "filesystem-server.jar"));
            
            // 對話
            String response = assistant.chat(
                "請幫我讀取 /tmp/test.txt 的內容，並摘要其中的重點"
            );
            System.out.println("助理回應：" + response);
        }
    }
}
```

> **💡 實務建議**：
> - 在生產環境中，確保正確處理 API Key 和敏感資訊
> - 實作適當的錯誤處理和重試機制
> - 考慮使用連接池管理多個 MCP Server 連接

---

## 第五章：完整實戰範例

本章提供三個完整的端到端範例，包含可直接執行的程式碼。

> **📌 `2026-07-28` 適用性說明**
>
> 本章範例的**業務邏輯、安全控制與工具設計**在 `2026-07-28` 下完全適用，
> 但涉及協議層的部分需依下表調整。範例以 stdio 傳輸為主，
> 因此受影響的面向相對有限。
>
> | 範例中的寫法 | `2026-07-28` 調整 |
> |-------------|------------------|
> | `initialize` 交握 | 移除；改實作 `server/discover` |
> | 回傳 `CallToolResult` | 加上 `resultType: "complete"` |
> | 清單類結果 | 加上 `ttlMs` 與 `cacheScope`，並採確定性排序 |
> | 資源不存在錯誤 `-32002` | 改用 `-32602` |
> | 廣播 `notifications/*/list_changed` | 改由 `subscriptions/listen` 串流逐訂閱投遞 |
> | 需要使用者確認的操作 | 改用 MRTR（`resultType: "input_required"`） |
> | 依賴連線狀態的暫存 | 改為顯式握柄（參見 [11.4 從 Session 到顯式握柄](#114-從-session-到顯式握柄explicit-handle)） |

### 5.1 範例一：檔案系統 MCP Server

#### 5.1.1 功能說明

提供安全的檔案系統操作功能：
- 讀取檔案內容
- 寫入檔案
- 列出目錄
- 搜尋檔案
- 取得檔案資訊

#### 5.1.2 完整程式碼

**專案結構**：

```text
filesystem-mcp-server/
├── pom.xml
├── README.md
└── src/
    └── main/
        └── java/
            └── com/
                └── example/
                    └── mcp/
                        └── filesystem/
                            └── FilesystemMcpServer.java
```

**pom.xml**：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example.mcp</groupId>
    <artifactId>filesystem-mcp-server</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <name>Filesystem MCP Server</name>
    <description>MCP Server for filesystem operations</description>
    
    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>io.modelcontextprotocol</groupId>
            <artifactId>mcp-server</artifactId>
            <version>1.0.0</version>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.example.mcp.filesystem.FilesystemMcpServer</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.5.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

**src/main/java/com/example/mcp/filesystem/FilesystemMcpServer.java**：
```java
package com.example.mcp.filesystem;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * 檔案系統 MCP Server
 * 提供安全的檔案讀寫、搜尋功能
 */
public class FilesystemMcpServer {
    
    private final McpServer server;
    
    // 配置：允許存取的目錄（可透過環境變數設定）
    private final List<String> allowedDirectories;
    
    // 最大檔案大小限制（10MB）
    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024;
    
    // 禁止的檔案類型
    private static final Set<String> FORBIDDEN_EXTENSIONS = Set.of(
        ".exe", ".dll", ".so", ".dylib", ".bin"
    );
    
    public FilesystemMcpServer() {
        // 從環境變數讀取允許的目錄
        String allowedDirs = System.getenv().getOrDefault("MCP_ALLOWED_DIRS", "/tmp,/home");
        this.allowedDirectories = Arrays.stream(allowedDirs.split(","))
            .map(String::trim)
            .filter(s -> !s.isEmpty())
            .collect(Collectors.toList());
        
        // 建立 Server
        McpServerOptions options = McpServerOptions.builder()
            .serverInfo(ServerInfo.builder()
                .name("filesystem-server")
                .version("1.0.0")
                .build())
            .capabilities(ServerCapabilities.builder()
                .tools(ToolsCapability.builder().listChanged(true).build())
                .resources(ResourcesCapability.builder().subscribe(true).listChanged(true).build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        setupHandlers();
    }
    
    private boolean isPathAllowed(Path path) {
        try {
            Path resolved = path.toAbsolutePath().normalize();
            return allowedDirectories.stream()
                .anyMatch(dir -> resolved.startsWith(dir));
        } catch (Exception e) {
            return false;
        }
    }
    
    private boolean isSafeFilename(String filename) {
        // 檢查路徑遍歷攻擊
        if (filename.contains("..") || filename.startsWith("/")) {
            return false;
        }
        
        // 檢查禁止的副檔名
        String ext = filename.contains(".") 
            ? filename.substring(filename.lastIndexOf(".")).toLowerCase() 
            : "";
        return !FORBIDDEN_EXTENSIONS.contains(ext);
    }
    
    private void setupHandlers() {
        // 工具列表處理器
        server.setToolListHandler(request -> CompletableFuture.supplyAsync(() -> 
            ListToolsResult.builder()
                .tools(List.of(
                    Tool.builder()
                        .name("read_file")
                        .description("讀取指定檔案的內容。支援文字檔案。")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "path", Map.of(
                                    "type", "string",
                                    "description", "檔案的完整路徑"
                                ),
                                "encoding", Map.of(
                                    "type", "string",
                                    "description", "檔案編碼（預設 utf-8）",
                                    "default", "utf-8"
                                )
                            ),
                            "required", List.of("path")
                        ))
                        .build(),
                    Tool.builder()
                        .name("write_file")
                        .description("寫入內容到指定檔案。如果檔案不存在會建立。")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "path", Map.of("type", "string", "description", "檔案的完整路徑"),
                                "content", Map.of("type", "string", "description", "要寫入的內容"),
                                "mode", Map.of(
                                    "type", "string",
                                    "enum", List.of("overwrite", "append"),
                                    "description", "寫入模式：overwrite（覆蓋）或 append（附加）",
                                    "default", "overwrite"
                                )
                            ),
                            "required", List.of("path", "content")
                        ))
                        .build(),
                    Tool.builder()
                        .name("list_directory")
                        .description("列出目錄中的檔案和子目錄")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "path", Map.of("type", "string", "description", "目錄路徑"),
                                "recursive", Map.of("type", "boolean", "description", "是否遞迴列出子目錄", "default", false),
                                "pattern", Map.of("type", "string", "description", "檔案名稱過濾模式（如 *.txt）")
                            ),
                            "required", List.of("path")
                        ))
                        .build(),
                    Tool.builder()
                        .name("search_files")
                        .description("在指定目錄中搜尋包含特定內容的檔案")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "directory", Map.of("type", "string", "description", "搜尋的起始目錄"),
                                "query", Map.of("type", "string", "description", "要搜尋的文字內容"),
                                "file_pattern", Map.of("type", "string", "description", "檔案名稱過濾模式", "default", "*"),
                                "max_results", Map.of("type", "integer", "description", "最大結果數量", "default", 20)
                            ),
                            "required", List.of("directory", "query")
                        ))
                        .build(),
                    Tool.builder()
                        .name("get_file_info")
                        .description("取得檔案的詳細資訊（大小、修改時間等）")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "path", Map.of("type", "string", "description", "檔案路徑")
                            ),
                            "required", List.of("path")
                        ))
                        .build(),
                    Tool.builder()
                        .name("create_directory")
                        .description("建立新目錄（包含父目錄）")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "path", Map.of("type", "string", "description", "目錄路徑")
                            ),
                            "required", List.of("path")
                        ))
                        .build(),
                    Tool.builder()
                        .name("delete_file")
                        .description("刪除指定檔案")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "path", Map.of("type", "string", "description", "檔案路徑"),
                                "confirm", Map.of("type", "boolean", "description", "確認刪除", "default", false)
                            ),
                            "required", List.of("path", "confirm")
                        ))
                        .build()
                ))
                .build()
        ));
        
        // 工具呼叫處理器
        server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
            String name = request.getParams().getName();
            Map<String, Object> args = request.getParams().getArguments();
            
            try {
                return switch (name) {
                    case "read_file" -> handleReadFile(args);
                    case "write_file" -> handleWriteFile(args);
                    case "list_directory" -> handleListDirectory(args);
                    case "search_files" -> handleSearchFiles(args);
                    case "get_file_info" -> handleGetFileInfo(args);
                    case "create_directory" -> handleCreateDirectory(args);
                    case "delete_file" -> handleDeleteFile(args);
                    default -> CallToolResult.error("未知的工具：" + name);
                };
            } catch (Exception e) {
                return CallToolResult.error("錯誤：" + e.getMessage());
            }
        }));
        
        // 資源列表處理器
        server.setResourceListHandler(request -> CompletableFuture.supplyAsync(() -> {
            List<Resource> resources = allowedDirectories.stream()
                .map(dir -> {
                    Path path = Path.of(dir);
                    if (Files.exists(path) && Files.isDirectory(path)) {
                        return Resource.builder()
                            .uri("file://" + path.toAbsolutePath())
                            .name("目錄：" + path)
                            .description("允許存取的目錄：" + path)
                            .mimeType("inode/directory")
                            .build();
                    }
                    return null;
                })
                .filter(Objects::nonNull)
                .collect(Collectors.toList());
            
            return ListResourcesResult.builder().resources(resources).build();
        }));
    }
    
    private CallToolResult handleReadFile(Map<String, Object> args) throws IOException {
        Path path = Path.of((String) args.get("path"));
        String encoding = (String) args.getOrDefault("encoding", "utf-8");
        
        if (!isPathAllowed(path)) {
            return CallToolResult.error("錯誤：存取被拒絕，路徑不在允許範圍內");
        }
        
        if (!Files.exists(path)) {
            return CallToolResult.error("錯誤：檔案不存在 - " + path);
        }
        
        if (!Files.isRegularFile(path)) {
            return CallToolResult.error("錯誤：指定路徑不是檔案");
        }
        
        if (Files.size(path) > MAX_FILE_SIZE) {
            return CallToolResult.error("錯誤：檔案過大（超過 " + (MAX_FILE_SIZE / 1024 / 1024) + "MB）");
        }
        
        try {
            String content = Files.readString(path, java.nio.charset.Charset.forName(encoding));
            return CallToolResult.text(content);
        } catch (java.nio.charset.MalformedInputException e) {
            return CallToolResult.error("錯誤：無法以指定編碼讀取檔案，可能是二進位檔案");
        }
    }
    
    private CallToolResult handleWriteFile(Map<String, Object> args) throws IOException {
        Path path = Path.of((String) args.get("path"));
        String content = (String) args.get("content");
        String mode = (String) args.getOrDefault("mode", "overwrite");
        
        if (!isPathAllowed(path)) {
            return CallToolResult.error("錯誤：存取被拒絕，路徑不在允許範圍內");
        }
        
        if (!isSafeFilename(path.getFileName().toString())) {
            return CallToolResult.error("錯誤：不安全的檔案名稱");
        }
        
        // 確保父目錄存在
        Files.createDirectories(path.getParent());
        
        if ("append".equals(mode)) {
            Files.writeString(path, content, StandardCharsets.UTF_8, 
                StandardOpenOption.CREATE, StandardOpenOption.APPEND);
            return CallToolResult.text("成功：已附加檔案 - " + path);
        } else {
            Files.writeString(path, content, StandardCharsets.UTF_8);
            return CallToolResult.text("成功：已覆寫檔案 - " + path);
        }
    }
    
    private CallToolResult handleListDirectory(Map<String, Object> args) throws IOException {
        Path path = Path.of((String) args.get("path"));
        boolean recursive = Boolean.TRUE.equals(args.get("recursive"));
        String pattern = (String) args.getOrDefault("pattern", "*");
        
        if (!isPathAllowed(path)) {
            return CallToolResult.error("錯誤：存取被拒絕");
        }
        
        if (!Files.exists(path)) {
            return CallToolResult.error("錯誤：目錄不存在 - " + path);
        }
        
        if (!Files.isDirectory(path)) {
            return CallToolResult.error("錯誤：指定路徑不是目錄");
        }
        
        PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:" + pattern);
        List<String> results = new ArrayList<>();
        
        try (Stream<Path> stream = recursive ? Files.walk(path) : Files.list(path)) {
            stream.filter(p -> matcher.matches(p.getFileName()))
                .sorted()
                .limit(100)
                .forEach(p -> {
                    String icon = Files.isDirectory(p) ? "📁" : "📄";
                    Path relPath = path.relativize(p);
                    String size = "";
                    if (Files.isRegularFile(p)) {
                        try {
                            size = " (" + Files.size(p) + " bytes)";
                        } catch (IOException ignored) {}
                    }
                    results.add(icon + " " + relPath + size);
                });
        }
        
        if (results.isEmpty()) {
            return CallToolResult.text("目錄為空或無符合條件的項目");
        }
        
        String header = "目錄列表：" + path + "\n" + "=".repeat(50) + "\n";
        return CallToolResult.text(header + String.join("\n", results));
    }
    
    private CallToolResult handleSearchFiles(Map<String, Object> args) throws IOException {
        Path directory = Path.of((String) args.get("directory"));
        String query = (String) args.get("query");
        String filePattern = (String) args.getOrDefault("file_pattern", "*");
        int maxResults = ((Number) args.getOrDefault("max_results", 20)).intValue();
        
        if (!isPathAllowed(directory)) {
            return CallToolResult.error("錯誤：存取被拒絕");
        }
        
        if (!Files.exists(directory) || !Files.isDirectory(directory)) {
            return CallToolResult.error("錯誤：目錄不存在");
        }
        
        PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:" + filePattern);
        List<Map<String, Object>> results = new ArrayList<>();
        String queryLower = query.toLowerCase();
        
        try (Stream<Path> stream = Files.walk(directory)) {
            stream.filter(Files::isRegularFile)
                .filter(p -> matcher.matches(p.getFileName()))
                .filter(p -> {
                    try {
                        return Files.size(p) <= MAX_FILE_SIZE;
                    } catch (IOException e) {
                        return false;
                    }
                })
                .forEach(filePath -> {
                    if (results.size() >= maxResults) return;
                    
                    try {
                        String content = Files.readString(filePath, StandardCharsets.UTF_8);
                        if (content.toLowerCase().contains(queryLower)) {
                            String[] lines = content.split("\n");
                            List<String> matchingLines = new ArrayList<>();
                            
                            for (int i = 0; i < lines.length && matchingLines.size() < 5; i++) {
                                if (lines[i].toLowerCase().contains(queryLower)) {
                                    String line = lines[i].length() > 100 
                                        ? lines[i].substring(0, 100) 
                                        : lines[i];
                                    matchingLines.add("  Line " + (i + 1) + ": " + line);
                                }
                            }
                            
                            results.add(Map.of(
                                "path", filePath.toString(),
                                "matches", matchingLines
                            ));
                        }
                    } catch (IOException ignored) {}
                });
        }
        
        if (results.isEmpty()) {
            return CallToolResult.text("找不到包含 '" + query + "' 的檔案");
        }
        
        StringBuilder output = new StringBuilder();
        output.append("搜尋結果：找到 ").append(results.size()).append(" 個檔案包含 '").append(query).append("'\n");
        output.append("=".repeat(50)).append("\n\n");
        
        for (Map<String, Object> result : results) {
            output.append("📄 ").append(result.get("path")).append("\n");
            @SuppressWarnings("unchecked")
            List<String> matches = (List<String>) result.get("matches");
            for (String match : matches) {
                output.append(match).append("\n");
            }
            output.append("\n");
        }
        
        return CallToolResult.text(output.toString());
    }
    
    private CallToolResult handleGetFileInfo(Map<String, Object> args) throws IOException {
        Path path = Path.of((String) args.get("path"));
        
        if (!isPathAllowed(path)) {
            return CallToolResult.error("錯誤：存取被拒絕");
        }
        
        if (!Files.exists(path)) {
            return CallToolResult.error("錯誤：路徑不存在 - " + path);
        }
        
        BasicFileAttributes attrs = Files.readAttributes(path, BasicFileAttributes.class);
        String mimeType = Files.probeContentType(path);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
            .withZone(ZoneId.systemDefault());
        
        String info = String.format("""
            檔案資訊：%s
            %s
            類型：%s
            大小：%,d bytes
            MIME 類型：%s
            建立時間：%s
            修改時間：%s
            存取時間：%s
            """,
            path,
            "=".repeat(50),
            Files.isDirectory(path) ? "目錄" : "檔案",
            attrs.size(),
            mimeType != null ? mimeType : "未知",
            formatter.format(attrs.creationTime().toInstant()),
            formatter.format(attrs.lastModifiedTime().toInstant()),
            formatter.format(attrs.lastAccessTime().toInstant())
        );
        
        return CallToolResult.text(info);
    }
    
    private CallToolResult handleCreateDirectory(Map<String, Object> args) throws IOException {
        Path path = Path.of((String) args.get("path"));
        
        if (!isPathAllowed(path)) {
            return CallToolResult.error("錯誤：存取被拒絕");
        }
        
        Files.createDirectories(path);
        return CallToolResult.text("成功：已建立目錄 - " + path);
    }
    
    private CallToolResult handleDeleteFile(Map<String, Object> args) throws IOException {
        Path path = Path.of((String) args.get("path"));
        boolean confirm = Boolean.TRUE.equals(args.get("confirm"));
        
        if (!confirm) {
            return CallToolResult.error("錯誤：請設定 confirm=true 以確認刪除");
        }
        
        if (!isPathAllowed(path)) {
            return CallToolResult.error("錯誤：存取被拒絕");
        }
        
        if (!Files.exists(path)) {
            return CallToolResult.error("錯誤：檔案不存在");
        }
        
        if (Files.isDirectory(path)) {
            return CallToolResult.error("錯誤：不支援刪除目錄");
        }
        
        Files.delete(path);
        return CallToolResult.text("成功：已刪除檔案 - " + path);
    }
    
    public void start() throws Exception {
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
        System.err.println("Filesystem MCP Server 啟動中...");
        System.err.println("允許的目錄：" + allowedDirectories);
    }
    
    public static void main(String[] args) throws Exception {
        FilesystemMcpServer server = new FilesystemMcpServer();
        server.start();
    }
}
```

#### 5.1.3 測試與除錯步驟

**1. 建置專案**：
```bash
cd filesystem-mcp-server
mvn clean package
```

**2. 使用 MCP Inspector 測試**：
```bash
npx @modelcontextprotocol/inspector java -jar target/filesystem-mcp-server-1.0.0.jar
```

**3. 測試指令**：
```json
// 列出工具
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}

// 讀取檔案
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "read_file",
    "arguments": {"path": "/tmp/test.txt"}
  }
}

// 列出目錄
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "list_directory",
    "arguments": {"path": "/tmp", "pattern": "*.txt"}
  }
}
```

---

### 5.2 範例二：資料庫查詢 MCP Server

#### 5.2.1 功能說明

提供安全的 PostgreSQL 資料庫操作：
- 列出資料表
- 查看 Schema
- 執行 SELECT 查詢
- 安全的參數化查詢

#### 5.2.2 完整程式碼

**pom.xml**（資料庫 Server）：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example.mcp</groupId>
    <artifactId>database-mcp-server</artifactId>
    <version>1.0.0</version>
    
    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>io.modelcontextprotocol</groupId>
            <artifactId>mcp-server</artifactId>
            <version>1.0.0</version>
        </dependency>
        <dependency>
            <groupId>com.zaxxer</groupId>
            <artifactId>HikariCP</artifactId>
            <version>5.1.0</version>
        </dependency>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>42.7.1</version>
        </dependency>
    </dependencies>
</project>
```

**DatabaseMcpServer.java**：
```java
package com.example.mcp.database;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.sql.*;
import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.regex.*;

/**
 * 資料庫查詢 MCP Server
 * 提供安全的 PostgreSQL 資料庫查詢功能
 */
public class DatabaseMcpServer {
    
    private final McpServer server;
    private final HikariDataSource dataSource;
    
    // 配置
    private static final int MAX_QUERY_ROWS = Integer.parseInt(
        System.getenv().getOrDefault("MAX_QUERY_ROWS", "100")
    );
    private static final int QUERY_TIMEOUT = Integer.parseInt(
        System.getenv().getOrDefault("QUERY_TIMEOUT", "30")
    );
    
    // SQL 安全檢查
    private static final Set<String> DANGEROUS_KEYWORDS = Set.of(
        "DROP", "DELETE", "TRUNCATE", "UPDATE", "INSERT",
        "ALTER", "CREATE", "GRANT", "REVOKE", "EXECUTE"
    );
    
    public DatabaseMcpServer() {
        // 初始化連接池
        String databaseUrl = System.getenv().getOrDefault(
            "DATABASE_URL", 
            "jdbc:postgresql://localhost/postgres"
        );
        
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl(databaseUrl);
        config.setMinimumIdle(2);
        config.setMaximumPoolSize(10);
        config.setConnectionTimeout(QUERY_TIMEOUT * 1000L);
        
        this.dataSource = new HikariDataSource(config);
        
        // 建立 Server
        McpServerOptions options = McpServerOptions.builder()
            .serverInfo(ServerInfo.builder()
                .name("database-server")
                .version("1.0.0")
                .build())
            .capabilities(ServerCapabilities.builder()
                .tools(ToolsCapability.builder().build())
                .resources(ResourcesCapability.builder().build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        setupHandlers();
    }
    
    private record SafeQueryResult(boolean safe, String errorMessage) {}
    
    private SafeQueryResult isSafeQuery(String query) {
        // 移除註解
        String cleanQuery = query.replaceAll("--.*$", "");
        cleanQuery = cleanQuery.replaceAll("/\\*.*?\\*/", "");
        String upperQuery = cleanQuery.toUpperCase().trim();
        
        // 必須以 SELECT 開頭
        if (!upperQuery.startsWith("SELECT")) {
            return new SafeQueryResult(false, "僅支援 SELECT 查詢");
        }
        
        // 檢查危險關鍵字
        for (String keyword : DANGEROUS_KEYWORDS) {
            Pattern pattern = Pattern.compile("\\b" + keyword + "\\b");
            if (pattern.matcher(upperQuery).find()) {
                return new SafeQueryResult(false, "查詢包含不允許的關鍵字：" + keyword);
            }
        }
        
        // 檢查多語句
        String queryWithoutTrailing = cleanQuery.replaceAll(";\\s*$", "");
        if (queryWithoutTrailing.contains(";")) {
            return new SafeQueryResult(false, "不支援多語句查詢");
        }
        
        return new SafeQueryResult(true, "");
    }
    
    private void setupHandlers() {
        // 工具列表處理器
        server.setToolListHandler(request -> CompletableFuture.supplyAsync(() ->
            ListToolsResult.builder()
                .tools(List.of(
                    Tool.builder()
                        .name("list_tables")
                        .description("列出資料庫中的所有資料表")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "schema", Map.of(
                                    "type", "string",
                                    "description", "Schema 名稱（預設 public）",
                                    "default", "public"
                                )
                            )
                        ))
                        .build(),
                    Tool.builder()
                        .name("describe_table")
                        .description("取得資料表的結構資訊（欄位、型別、限制）")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "table_name", Map.of("type", "string", "description", "資料表名稱"),
                                "schema", Map.of("type", "string", "description", "Schema 名稱", "default", "public")
                            ),
                            "required", List.of("table_name")
                        ))
                        .build(),
                    Tool.builder()
                        .name("query")
                        .description("執行 SQL SELECT 查詢（僅支援讀取操作）")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "sql", Map.of("type", "string", "description", "SQL SELECT 查詢語句"),
                                "limit", Map.of("type", "integer", "description", "結果筆數限制", "default", 50)
                            ),
                            "required", List.of("sql")
                        ))
                        .build(),
                    Tool.builder()
                        .name("get_table_sample")
                        .description("取得資料表的範例資料")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "table_name", Map.of("type", "string", "description", "資料表名稱"),
                                "limit", Map.of("type", "integer", "description", "範例筆數", "default", 5)
                            ),
                            "required", List.of("table_name")
                        ))
                        .build(),
                    Tool.builder()
                        .name("get_table_stats")
                        .description("取得資料表的統計資訊")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "table_name", Map.of("type", "string", "description", "資料表名稱")
                            ),
                            "required", List.of("table_name")
                        ))
                        .build()
                ))
                .build()
        ));
        
        // 工具呼叫處理器
        server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
            String name = request.getParams().getName();
            Map<String, Object> args = request.getParams().getArguments();
            
            try {
                return switch (name) {
                    case "list_tables" -> handleListTables(args);
                    case "describe_table" -> handleDescribeTable(args);
                    case "query" -> handleQuery(args);
                    case "get_table_sample" -> handleTableSample(args);
                    case "get_table_stats" -> handleTableStats(args);
                    default -> CallToolResult.error("未知的工具：" + name);
                };
            } catch (SQLException e) {
                return CallToolResult.error("資料庫錯誤：" + e.getMessage());
            } catch (Exception e) {
                return CallToolResult.error("錯誤：" + e.getMessage());
            }
        }));
    }
    
    private CallToolResult handleListTables(Map<String, Object> args) throws SQLException {
        String schema = (String) args.getOrDefault("schema", "public");
        
        String query = """
            SELECT 
                table_name,
                table_type,
                (SELECT count(*) FROM information_schema.columns c 
                 WHERE c.table_name = t.table_name 
                 AND c.table_schema = t.table_schema) as column_count
            FROM information_schema.tables t
            WHERE table_schema = ?
            ORDER BY table_name
            """;
        
        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, schema);
            ResultSet rs = stmt.executeQuery();
            
            StringBuilder output = new StringBuilder();
            output.append("資料表列表（Schema: ").append(schema).append("）\n");
            output.append("=".repeat(50)).append("\n\n");
            output.append("| 資料表名稱 | 類型 | 欄位數 |\n");
            output.append("| --- | --- | --- |\n");
            
            boolean hasResults = false;
            while (rs.next()) {
                hasResults = true;
                output.append("| ").append(rs.getString("table_name"))
                      .append(" | ").append(rs.getString("table_type"))
                      .append(" | ").append(rs.getInt("column_count"))
                      .append(" |\n");
            }
            
            if (!hasResults) {
                return CallToolResult.text("Schema '" + schema + "' 中沒有資料表");
            }
            
            return CallToolResult.text(output.toString());
        }
    }
    
    private CallToolResult handleDescribeTable(Map<String, Object> args) throws SQLException {
        String tableName = (String) args.get("table_name");
        String schema = (String) args.getOrDefault("schema", "public");
        
        // 驗證資料表名稱（防止 SQL 注入）
        if (!tableName.matches("^[a-zA-Z_][a-zA-Z0-9_]*$")) {
            return CallToolResult.error("錯誤：無效的資料表名稱");
        }
        
        String columnQuery = """
            SELECT 
                column_name,
                data_type,
                character_maximum_length,
                is_nullable,
                column_default
            FROM information_schema.columns
            WHERE table_schema = ? AND table_name = ?
            ORDER BY ordinal_position
            """;
        
        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(columnQuery)) {
            stmt.setString(1, schema);
            stmt.setString(2, tableName);
            ResultSet rs = stmt.executeQuery();
            
            StringBuilder output = new StringBuilder();
            output.append("資料表結構：").append(schema).append(".").append(tableName).append("\n");
            output.append("=".repeat(60)).append("\n\n");
            output.append("| 欄位名稱 | 資料型別 | 可為空 | 預設值 |\n");
            output.append("| --- | --- | --- | --- |\n");
            
            boolean hasResults = false;
            while (rs.next()) {
                hasResults = true;
                String dataType = rs.getString("data_type");
                Integer maxLen = rs.getObject("character_maximum_length", Integer.class);
                if (maxLen != null) {
                    dataType += "(" + maxLen + ")";
                }
                
                output.append("| ").append(rs.getString("column_name"))
                      .append(" | ").append(dataType)
                      .append(" | ").append(rs.getString("is_nullable"))
                      .append(" | ").append(rs.getString("column_default") != null ? rs.getString("column_default") : "-")
                      .append(" |\n");
            }
            
            if (!hasResults) {
                return CallToolResult.error("資料表 '" + tableName + "' 不存在");
            }
            
            return CallToolResult.text(output.toString());
        }
    }
    
    private CallToolResult handleQuery(Map<String, Object> args) throws SQLException {
        String sql = (String) args.get("sql");
        int limit = Math.min(((Number) args.getOrDefault("limit", 50)).intValue(), MAX_QUERY_ROWS);
        
        // 安全檢查
        SafeQueryResult safeResult = isSafeQuery(sql);
        if (!safeResult.safe()) {
            return CallToolResult.error("查詢被拒絕：" + safeResult.errorMessage());
        }
        
        // 添加 LIMIT（如果沒有）
        if (!sql.toUpperCase().contains("LIMIT")) {
            sql = sql.replaceAll(";\\s*$", "") + " LIMIT " + limit;
        }
        
        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.setQueryTimeout(QUERY_TIMEOUT);
            ResultSet rs = stmt.executeQuery(sql);
            ResultSetMetaData metaData = rs.getMetaData();
            int columnCount = metaData.getColumnCount();
            
            // 取得欄位名稱
            List<String> columns = new ArrayList<>();
            for (int i = 1; i <= columnCount; i++) {
                columns.add(metaData.getColumnName(i));
            }
            
            // 建立輸出
            StringBuilder output = new StringBuilder();
            List<List<String>> rows = new ArrayList<>();
            
            while (rs.next()) {
                List<String> row = new ArrayList<>();
                for (int i = 1; i <= columnCount; i++) {
                    Object value = rs.getObject(i);
                    String strValue = value != null ? value.toString() : "NULL";
                    if (strValue.length() > 50) {
                        strValue = strValue.substring(0, 50) + "...";
                    }
                    row.add(strValue);
                }
                rows.add(row);
            }
            
            if (rows.isEmpty()) {
                return CallToolResult.text("查詢無結果");
            }
            
            output.append("查詢結果（共 ").append(rows.size()).append(" 筆）\n");
            output.append("=".repeat(50)).append("\n\n");
            output.append("| ").append(String.join(" | ", columns)).append(" |\n");
            output.append("| ").append(String.join(" | ", Collections.nCopies(columns.size(), "---"))).append(" |\n");
            
            for (List<String> row : rows) {
                output.append("| ").append(String.join(" | ", row)).append(" |\n");
            }
            
            return CallToolResult.text(output.toString());
        }
    }
    
    private CallToolResult handleTableSample(Map<String, Object> args) throws SQLException {
        String tableName = (String) args.get("table_name");
        int limit = Math.min(((Number) args.getOrDefault("limit", 5)).intValue(), 20);
        
        if (!tableName.matches("^[a-zA-Z_][a-zA-Z0-9_]*$")) {
            return CallToolResult.error("錯誤：無效的資料表名稱");
        }
        
        return handleQuery(Map.of(
            "sql", "SELECT * FROM " + tableName,
            "limit", limit
        ));
    }
    
    private CallToolResult handleTableStats(Map<String, Object> args) throws SQLException {
        String tableName = (String) args.get("table_name");
        
        if (!tableName.matches("^[a-zA-Z_][a-zA-Z0-9_]*$")) {
            return CallToolResult.error("錯誤：無效的資料表名稱");
        }
        
        try (Connection conn = dataSource.getConnection()) {
            // 取得行數
            long rowCount;
            try (Statement stmt = conn.createStatement()) {
                ResultSet rs = stmt.executeQuery("SELECT count(*) FROM " + tableName);
                rs.next();
                rowCount = rs.getLong(1);
            }
            
            // 取得表大小
            String sizeQuery = """
                SELECT 
                    pg_size_pretty(pg_total_relation_size(?)) as total_size,
                    pg_size_pretty(pg_relation_size(?)) as table_size,
                    pg_size_pretty(pg_indexes_size(?)) as index_size
                """;
            
            try (PreparedStatement stmt = conn.prepareStatement(sizeQuery)) {
                stmt.setString(1, tableName);
                stmt.setString(2, tableName);
                stmt.setString(3, tableName);
                ResultSet rs = stmt.executeQuery();
                rs.next();
                
                StringBuilder output = new StringBuilder();
                output.append("資料表統計：").append(tableName).append("\n");
                output.append("=".repeat(40)).append("\n\n");
                output.append("總筆數：").append(String.format("%,d", rowCount)).append("\n");
                output.append("總大小：").append(rs.getString("total_size")).append("\n");
                output.append("資料大小：").append(rs.getString("table_size")).append("\n");
                output.append("索引大小：").append(rs.getString("index_size")).append("\n");
                
                return CallToolResult.text(output.toString());
            }
        }
    }
    
    public void start() throws Exception {
        System.err.println("Database MCP Server 啟動中...");
        System.err.println("資料庫連接池已初始化");
        
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
    }
    
    public void close() {
        if (dataSource != null) {
            dataSource.close();
        }
    }
    
    public static void main(String[] args) throws Exception {
        DatabaseMcpServer server = new DatabaseMcpServer();
        Runtime.getRuntime().addShutdownHook(new Thread(server::close));
        server.start();
    }
}
```

#### 5.2.3 安全性考量

> **📌 `2026-07-28` 補充**：下列清單屬於**資料庫存取層**的控制，在新版仍完全適用。
> 但因為授權不再綁定於 Session，**每一次 `tools/call` 都必須重新審查呼叫者身分與權限**，
> 不可將「已驗證」狀態快取於連線層。另建議搭配
> [13.3 授權硬化與身分治理](#133-授權硬化與身分治理) 的權杖驗證與審計機制一併實作。

```text
┌─────────────────────────────────────────────────────────────────┐
│                    資料庫 Server 安全清單                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✓ 僅允許 SELECT 查詢                                            │
│  ✓ 禁止危險關鍵字（DROP、DELETE、UPDATE 等）                       │
│  ✓ 禁止多語句查詢                                                │
│  ✓ 查詢結果數量限制                                              │
│  ✓ 查詢超時設定                                                  │
│  ✓ 資料表名稱驗證                                                │
│  ✓ 使用連接池管理                                                │
│  ✓ 敏感資訊不輸出到日誌                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.3 範例三：API 整合 MCP Server

#### 5.3.1 功能說明

整合 GitHub API 提供：
- 搜尋儲存庫
- 取得儲存庫資訊
- 列出 Issues
- 讀取檔案內容

#### 5.3.2 完整程式碼

**pom.xml**（GitHub Server）：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example.mcp</groupId>
    <artifactId>github-mcp-server</artifactId>
    <version>1.0.0</version>
    
    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>io.modelcontextprotocol</groupId>
            <artifactId>mcp-server</artifactId>
            <version>1.0.0</version>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>
        <dependency>
            <groupId>com.squareup.okhttp3</groupId>
            <artifactId>okhttp</artifactId>
            <version>4.12.0</version>
        </dependency>
    </dependencies>
</project>
```

**GitHubMcpServer.java**：
```java
package com.example.mcp.github;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerOptions;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.*;

import com.google.gson.*;
import okhttp3.*;

import java.io.IOException;
import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.concurrent.*;

/**
 * GitHub API 整合 MCP Server
 */
public class GitHubMcpServer {
    
    private final McpServer server;
    private final OkHttpClient httpClient;
    private final Gson gson;
    
    // GitHub API 配置
    private static final String GITHUB_API_BASE = "https://api.github.com";
    private static final String GITHUB_TOKEN = System.getenv("GITHUB_TOKEN");
    
    // 速率限制追蹤
    private volatile int rateLimitRemaining = 60;
    private volatile Instant rateLimitReset = null;
    
    public GitHubMcpServer() {
        this.httpClient = new OkHttpClient.Builder()
            .connectTimeout(30, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .build();
        this.gson = new GsonBuilder().create();
        
        // 建立 Server
        McpServerOptions options = McpServerOptions.builder()
            .serverInfo(ServerInfo.builder()
                .name("github-server")
                .version("1.0.0")
                .build())
            .capabilities(ServerCapabilities.builder()
                .tools(ToolsCapability.builder().build())
                .build())
            .build();
        
        this.server = new McpServer(options);
        setupHandlers();
    }
    
    /**
     * GitHub API 錯誤
     */
    public static class GitHubAPIException extends Exception {
        private final int status;
        
        public GitHubAPIException(int status, String message) {
            super("GitHub API Error (" + status + "): " + message);
            this.status = status;
        }
        
        public int getStatus() { return status; }
    }
    
    /**
     * 發送 GitHub API 請求
     */
    private JsonObject githubRequest(String method, String endpoint, Map<String, String> params) 
            throws IOException, GitHubAPIException {
        
        HttpUrl.Builder urlBuilder = HttpUrl.parse(GITHUB_API_BASE + endpoint).newBuilder();
        if (params != null) {
            params.forEach(urlBuilder::addQueryParameter);
        }
        
        Request.Builder requestBuilder = new Request.Builder()
            .url(urlBuilder.build())
            .header("Accept", "application/vnd.github.v3+json")
            .header("User-Agent", "MCP-GitHub-Server/1.0");
        
        if (GITHUB_TOKEN != null && !GITHUB_TOKEN.isEmpty()) {
            requestBuilder.header("Authorization", "token " + GITHUB_TOKEN);
        }
        
        if ("GET".equals(method)) {
            requestBuilder.get();
        }
        
        try (Response response = httpClient.newCall(requestBuilder.build()).execute()) {
            // 更新速率限制
            String remaining = response.header("X-RateLimit-Remaining");
            String reset = response.header("X-RateLimit-Reset");
            if (remaining != null) {
                rateLimitRemaining = Integer.parseInt(remaining);
            }
            if (reset != null) {
                rateLimitReset = Instant.ofEpochSecond(Long.parseLong(reset));
            }
            
            if (response.code() == 401) {
                throw new GitHubAPIException(401, "認證失敗，請檢查 GITHUB_TOKEN");
            } else if (response.code() == 403) {
                throw new GitHubAPIException(403, "存取被拒絕或已達速率限制（剩餘：" + rateLimitRemaining + "）");
            } else if (response.code() == 404) {
                throw new GitHubAPIException(404, "找不到資源");
            } else if (response.code() >= 400) {
                throw new GitHubAPIException(response.code(), response.body().string());
            }
            
            String body = response.body().string();
            return JsonParser.parseString(body).getAsJsonObject();
        }
    }
    
    private JsonArray githubRequestArray(String method, String endpoint, Map<String, String> params) 
            throws IOException, GitHubAPIException {
        
        HttpUrl.Builder urlBuilder = HttpUrl.parse(GITHUB_API_BASE + endpoint).newBuilder();
        if (params != null) {
            params.forEach(urlBuilder::addQueryParameter);
        }
        
        Request.Builder requestBuilder = new Request.Builder()
            .url(urlBuilder.build())
            .header("Accept", "application/vnd.github.v3+json")
            .header("User-Agent", "MCP-GitHub-Server/1.0");
        
        if (GITHUB_TOKEN != null && !GITHUB_TOKEN.isEmpty()) {
            requestBuilder.header("Authorization", "token " + GITHUB_TOKEN);
        }
        
        try (Response response = httpClient.newCall(requestBuilder.build()).execute()) {
            if (response.code() >= 400) {
                throw new GitHubAPIException(response.code(), response.body().string());
            }
            return JsonParser.parseString(response.body().string()).getAsJsonArray();
        }
    }
    
    private void setupHandlers() {
        // 工具列表處理器
        server.setToolListHandler(request -> CompletableFuture.supplyAsync(() ->
            ListToolsResult.builder()
                .tools(List.of(
                    Tool.builder()
                        .name("search_repositories")
                        .description("搜尋 GitHub 儲存庫")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "query", Map.of("type", "string", "description", "搜尋關鍵字"),
                                "language", Map.of("type", "string", "description", "程式語言過濾"),
                                "sort", Map.of("type", "string", "enum", List.of("stars", "forks", "updated"), "default", "stars"),
                                "limit", Map.of("type", "integer", "description", "結果數量", "default", 10)
                            ),
                            "required", List.of("query")
                        ))
                        .build(),
                    Tool.builder()
                        .name("get_repository")
                        .description("取得儲存庫詳細資訊")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "owner", Map.of("type", "string", "description", "擁有者名稱"),
                                "repo", Map.of("type", "string", "description", "儲存庫名稱")
                            ),
                            "required", List.of("owner", "repo")
                        ))
                        .build(),
                    Tool.builder()
                        .name("list_issues")
                        .description("列出儲存庫的 Issues")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "owner", Map.of("type", "string", "description", "擁有者名稱"),
                                "repo", Map.of("type", "string", "description", "儲存庫名稱"),
                                "state", Map.of("type", "string", "enum", List.of("open", "closed", "all"), "default", "open"),
                                "limit", Map.of("type", "integer", "default", 10)
                            ),
                            "required", List.of("owner", "repo")
                        ))
                        .build(),
                    Tool.builder()
                        .name("get_file_content")
                        .description("取得儲存庫中的檔案內容")
                        .inputSchema(Map.of(
                            "type", "object",
                            "properties", Map.of(
                                "owner", Map.of("type", "string"),
                                "repo", Map.of("type", "string"),
                                "path", Map.of("type", "string", "description", "檔案路徑"),
                                "ref", Map.of("type", "string", "description", "分支或 commit", "default", "main")
                            ),
                            "required", List.of("owner", "repo", "path")
                        ))
                        .build(),
                    Tool.builder()
                        .name("get_rate_limit")
                        .description("取得 GitHub API 速率限制狀態")
                        .inputSchema(Map.of("type", "object", "properties", Map.of()))
                        .build()
                ))
                .build()
        ));
        
        // 工具呼叫處理器
        server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
            String name = request.getParams().getName();
            Map<String, Object> args = request.getParams().getArguments();
            
            try {
                return switch (name) {
                    case "search_repositories" -> handleSearchRepos(args);
                    case "get_repository" -> handleGetRepo(args);
                    case "list_issues" -> handleListIssues(args);
                    case "get_file_content" -> handleGetFile(args);
                    case "get_rate_limit" -> handleRateLimit();
                    default -> CallToolResult.error("未知的工具：" + name);
                };
            } catch (GitHubAPIException e) {
                return CallToolResult.error("GitHub API 錯誤：" + e.getMessage());
            } catch (Exception e) {
                return CallToolResult.error("錯誤：" + e.getMessage());
            }
        }));
    }
    
    private CallToolResult handleSearchRepos(Map<String, Object> args) throws Exception {
        String query = (String) args.get("query");
        String language = (String) args.get("language");
        String sort = (String) args.getOrDefault("sort", "stars");
        int limit = Math.min(((Number) args.getOrDefault("limit", 10)).intValue(), 30);
        
        String searchQuery = query;
        if (language != null && !language.isEmpty()) {
            searchQuery += " language:" + language;
        }
        
        JsonObject data = githubRequest("GET", "/search/repositories", Map.of(
            "q", searchQuery,
            "sort", sort,
            "per_page", String.valueOf(limit)
        ));
        
        JsonArray repos = data.getAsJsonArray("items");
        
        if (repos == null || repos.isEmpty()) {
            return CallToolResult.text("找不到符合條件的儲存庫");
        }
        
        StringBuilder output = new StringBuilder();
        output.append("搜尋結果：'").append(query).append("'\n");
        output.append("=".repeat(50)).append("\n\n");
        
        for (JsonElement item : repos) {
            JsonObject repo = item.getAsJsonObject();
            output.append("### ").append(repo.get("full_name").getAsString()).append("\n");
            output.append("⭐ ").append(String.format("%,d", repo.get("stargazers_count").getAsInt())).append(" | ");
            output.append("🍴 ").append(String.format("%,d", repo.get("forks_count").getAsInt())).append(" | ");
            output.append("📝 ").append(repo.get("language").isJsonNull() ? "N/A" : repo.get("language").getAsString()).append("\n");
            output.append(repo.get("description").isJsonNull() ? "無描述" : repo.get("description").getAsString()).append("\n");
            output.append("🔗 ").append(repo.get("html_url").getAsString()).append("\n\n");
        }
        
        return CallToolResult.text(output.toString());
    }
    
    private CallToolResult handleGetRepo(Map<String, Object> args) throws Exception {
        String owner = (String) args.get("owner");
        String repo = (String) args.get("repo");
        
        JsonObject data = githubRequest("GET", "/repos/" + owner + "/" + repo, null);
        
        StringBuilder output = new StringBuilder();
        output.append("# ").append(data.get("full_name").getAsString()).append("\n\n");
        output.append("**描述**：").append(data.get("description").isJsonNull() ? "無描述" : data.get("description").getAsString()).append("\n\n");
        output.append("## 統計\n");
        output.append("- ⭐ Stars：").append(String.format("%,d", data.get("stargazers_count").getAsInt())).append("\n");
        output.append("- 🍴 Forks：").append(String.format("%,d", data.get("forks_count").getAsInt())).append("\n");
        output.append("- 👁 Watchers：").append(String.format("%,d", data.get("watchers_count").getAsInt())).append("\n");
        output.append("- 📝 Open Issues：").append(String.format("%,d", data.get("open_issues_count").getAsInt())).append("\n\n");
        output.append("## 資訊\n");
        output.append("- 程式語言：").append(data.get("language").isJsonNull() ? "N/A" : data.get("language").getAsString()).append("\n");
        output.append("- 預設分支：").append(data.get("default_branch").getAsString()).append("\n");
        output.append("- 建立時間：").append(data.get("created_at").getAsString().substring(0, 10)).append("\n");
        output.append("- 最後更新：").append(data.get("updated_at").getAsString().substring(0, 10)).append("\n");
        
        JsonElement license = data.get("license");
        output.append("- 授權：").append(license.isJsonNull() ? "N/A" : license.getAsJsonObject().get("name").getAsString()).append("\n\n");
        output.append("🔗 **連結**：").append(data.get("html_url").getAsString()).append("\n");
        
        return CallToolResult.text(output.toString());
    }
    
    private CallToolResult handleListIssues(Map<String, Object> args) throws Exception {
        String owner = (String) args.get("owner");
        String repo = (String) args.get("repo");
        String state = (String) args.getOrDefault("state", "open");
        int limit = Math.min(((Number) args.getOrDefault("limit", 10)).intValue(), 30);
        
        JsonArray data = githubRequestArray("GET", "/repos/" + owner + "/" + repo + "/issues", 
            Map.of("state", state, "per_page", String.valueOf(limit)));
        
        if (data.isEmpty()) {
            return CallToolResult.text("沒有 " + state + " 狀態的 Issues");
        }
        
        StringBuilder output = new StringBuilder();
        output.append("Issues (").append(state).append(") - ").append(owner).append("/").append(repo).append("\n");
        output.append("=".repeat(50)).append("\n\n");
        
        for (JsonElement item : data) {
            JsonObject issue = item.getAsJsonObject();
            
            // 排除 Pull Requests
            if (issue.has("pull_request")) continue;
            
            JsonArray labels = issue.getAsJsonArray("labels");
            String labelStr = labels.isEmpty() ? "無標籤" : 
                labels.asList().stream()
                    .map(l -> l.getAsJsonObject().get("name").getAsString())
                    .reduce((a, b) -> a + ", " + b)
                    .orElse("無標籤");
            
            output.append("### #").append(issue.get("number").getAsInt())
                  .append(" ").append(issue.get("title").getAsString()).append("\n");
            output.append("狀態：").append(issue.get("state").getAsString())
                  .append(" | 標籤：").append(labelStr).append("\n");
            output.append("作者：").append(issue.getAsJsonObject("user").get("login").getAsString())
                  .append(" | 建立於：").append(issue.get("created_at").getAsString().substring(0, 10)).append("\n");
            output.append("🔗 ").append(issue.get("html_url").getAsString()).append("\n\n");
        }
        
        return CallToolResult.text(output.toString());
    }
    
    private CallToolResult handleGetFile(Map<String, Object> args) throws Exception {
        String owner = (String) args.get("owner");
        String repo = (String) args.get("repo");
        String path = (String) args.get("path");
        String ref = (String) args.getOrDefault("ref", "main");
        
        JsonObject data = githubRequest("GET", 
            "/repos/" + owner + "/" + repo + "/contents/" + path,
            Map.of("ref", ref));
        
        if (!"file".equals(data.get("type").getAsString())) {
            return CallToolResult.error("指定路徑不是檔案");
        }
        
        int size = data.get("size").getAsInt();
        if (size > 1024 * 1024) {
            return CallToolResult.error("檔案過大，無法顯示");
        }
        
        String content = new String(Base64.getDecoder().decode(
            data.get("content").getAsString().replaceAll("\\s", "")));
        
        StringBuilder output = new StringBuilder();
        output.append("檔案：").append(path).append(" (ref: ").append(ref).append(")\n");
        output.append("=".repeat(50)).append("\n\n");
        output.append("```\n").append(content).append("\n```");
        
        return CallToolResult.text(output.toString());
    }
    
    private CallToolResult handleRateLimit() throws Exception {
        JsonObject data = githubRequest("GET", "/rate_limit", null);
        
        JsonObject core = data.getAsJsonObject("resources").getAsJsonObject("core");
        JsonObject search = data.getAsJsonObject("resources").getAsJsonObject("search");
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
            .withZone(ZoneId.systemDefault());
        Instant resetTime = Instant.ofEpochSecond(core.get("reset").getAsLong());
        
        StringBuilder output = new StringBuilder();
        output.append("GitHub API 速率限制狀態\n");
        output.append("=".repeat(40)).append("\n\n");
        output.append("## Core API\n");
        output.append("- 剩餘：").append(core.get("remaining").getAsInt())
              .append("/").append(core.get("limit").getAsInt()).append("\n");
        output.append("- 重置時間：").append(formatter.format(resetTime)).append("\n\n");
        output.append("## Search API\n");
        output.append("- 剩餘：").append(search.get("remaining").getAsInt())
              .append("/").append(search.get("limit").getAsInt()).append("\n");
        
        return CallToolResult.text(output.toString());
    }
    
    public void start() throws Exception {
        System.err.println("GitHub MCP Server 啟動中...");
        
        if (GITHUB_TOKEN == null || GITHUB_TOKEN.isEmpty()) {
            System.err.println("警告：未設定 GITHUB_TOKEN，將使用較低的速率限制");
        }
        
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport);
    }
    
    public static void main(String[] args) throws Exception {
        GitHubMcpServer server = new GitHubMcpServer();
        server.start();
    }
}
```

#### 5.3.3 錯誤處理與重試機制

```java
/**
 * 增強版 API 請求處理（含重試機制）
 * RetryableGitHubClient.java
 */
package com.example.mcp.github;

import java.util.concurrent.*;
import java.util.function.Supplier;

public class RetryableGitHubClient {
    
    private final int maxRetries;
    private final double backoffFactor;
    
    public RetryableGitHubClient(int maxRetries, double backoffFactor) {
        this.maxRetries = maxRetries;
        this.backoffFactor = backoffFactor;
    }
    
    /**
     * 帶重試機制的請求執行
     */
    public <T> T executeWithRetry(Supplier<T> action) throws Exception {
        Exception lastException = null;
        
        for (int attempt = 0; attempt < maxRetries; attempt++) {
            try {
                return action.get();
            } catch (GitHubMcpServer.GitHubAPIException e) {
                // 不重試的錯誤
                if (e.getStatus() == 401 || e.getStatus() == 403 || e.getStatus() == 404) {
                    throw e;
                }
                lastException = e;
            } catch (Exception e) {
                lastException = e;
            }
            
            // 計算等待時間（指數退避）
            long waitTime = (long) (backoffFactor * Math.pow(2, attempt) * 1000);
            try {
                Thread.sleep(waitTime);
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
                throw new RuntimeException("重試被中斷", ie);
            }
        }
        
        throw new RuntimeException("重試次數已達上限", lastException);
    }
    
    /**
     * 非同步版本
     */
    public <T> CompletableFuture<T> executeWithRetryAsync(Supplier<T> action) {
        return CompletableFuture.supplyAsync(() -> {
            try {
                return executeWithRetry(action);
            } catch (Exception e) {
                throw new CompletionException(e);
            }
        });
    }
}
```

---

*（第五章完結，繼續第六章）*

---

## 第六章：最佳實踐與設計模式

### 6.1 MCP Server 設計原則

> **📌 `2026-07-28` 新增設計原則：無狀態優先**
>
> 由於 Session 已移除，「跨請求狀態」不再由協議層保證，設計上必須遵守：
>
> - **不得**假設同一用戶端的連續請求會落在同一個伺服器實例
> - 需要跨請求延續的狀態，**MUST** 以**顯式握柄**（如 `cursor`、`taskId`、
>   自訂的 `contextId`）回傳給用戶端，由用戶端在下次請求時帶回
> - 握柄必須**可驗證且不可偽造**（建議簽章或以伺服器端儲存映射），
>   不可直接把內部主鍵或檔案路徑外露
> - 握柄應設有效期並在過期時回傳明確錯誤，避免無限期有效
>
> 完整設計指引參見
> [11.4 從 Session 到顯式握柄（Explicit Handle）](#114-從-session-到顯式握柄explicit-handle)。

#### 6.1.1 單一職責原則

每個 MCP Server 應該專注於一個領域或功能集：

```text
✅ 好的設計：
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Filesystem      │  │ Database        │  │ GitHub          │
│ Server          │  │ Server          │  │ Server          │
│                 │  │                 │  │                 │
│ - read_file     │  │ - query         │  │ - search_repos  │
│ - write_file    │  │ - list_tables   │  │ - get_issues    │
│ - list_dir      │  │ - describe      │  │ - get_commits   │
└─────────────────┘  └─────────────────┘  └─────────────────┘

❌ 不好的設計：
┌───────────────────────────────────────────────────────────┐
│                   Everything Server                        │
│                                                            │
│ - read_file, write_file, query_db, search_github,         │
│   send_email, parse_json, encrypt_data, ...               │
└───────────────────────────────────────────────────────────┘
```

#### 6.1.2 工具命名規範

| 規範 | 說明 | 好的範例 | 不好的範例 |
|------|------|---------|-----------|
| **動詞開頭** | 明確表達動作 | `read_file`, `create_user` | `file`, `user` |
| **snake_case** | 使用底線分隔 | `list_directory` | `listDirectory` |
| **具體描述** | 避免模糊名稱 | `search_by_name` | `search` |
| **一致性** | 同類工具統一前綴 | `db_query`, `db_insert` | `query`, `insert_record` |

**命名模板**：

```text
{action}_{target}[_{qualifier}]

範例：
- read_file          # 動作 + 目標
- search_users_by_name  # 動作 + 目標 + 限定詞
- list_active_orders   # 動作 + 修飾詞 + 目標
```

#### 6.1.3 參數設計與驗證

**好的參數設計**：

```java
Tool.builder()
    .name("search_records")
    .description("搜尋資料庫記錄")
    .inputSchema(Map.of(
        "type", "object",
        "properties", Map.of(
            // 必填參數放前面
            "table", Map.of(
                "type", "string",
                "description", "資料表名稱",
                "pattern", "^[a-zA-Z_][a-zA-Z0-9_]*$"  // 正則驗證
            ),
            "query", Map.of(
                "type", "string",
                "description", "搜尋關鍵字",
                "minLength", 1,
                "maxLength", 100
            ),
            // 選填參數有預設值
            "limit", Map.of(
                "type", "integer",
                "description", "結果數量限制（1-100）",
                "default", 20,
                "minimum", 1,
                "maximum", 100
            ),
            "offset", Map.of(
                "type", "integer",
                "description", "跳過的記錄數",
                "default", 0,
                "minimum", 0
            ),
            "sort_by", Map.of(
                "type", "string",
                "description", "排序欄位",
                "enum", List.of("created_at", "updated_at", "name")
            ),
            "sort_order", Map.of(
                "type", "string",
                "description", "排序方向",
                "enum", List.of("asc", "desc"),
                "default", "desc"
            )
        ),
        "required", List.of("table", "query"),
        "additionalProperties", false  // 禁止額外參數
    ))
    .build()
```

**參數驗證實作**：

```java
import com.networknt.schema.*;
import com.fasterxml.jackson.databind.*;

/**
 * 工具參數驗證器
 */
public class ArgumentValidator {
    
    private final JsonSchemaFactory schemaFactory;
    private final ObjectMapper objectMapper;
    
    public ArgumentValidator() {
        this.schemaFactory = JsonSchemaFactory.getInstance(SpecVersion.VersionFlag.V7);
        this.objectMapper = new ObjectMapper();
    }
    
    /**
     * 驗證工具參數
     */
    public ValidationResult validate(Map<String, Object> schema, Map<String, Object> arguments) {
        try {
            JsonSchema jsonSchema = schemaFactory.getSchema(
                objectMapper.writeValueAsString(schema)
            );
            
            JsonNode argumentsNode = objectMapper.valueToTree(arguments);
            Set<ValidationMessage> errors = jsonSchema.validate(argumentsNode);
            
            if (errors.isEmpty()) {
                return new ValidationResult(true, "");
            } else {
                String errorMsg = errors.stream()
                    .map(ValidationMessage::getMessage)
                    .reduce((a, b) -> a + "; " + b)
                    .orElse("驗證失敗");
                return new ValidationResult(false, errorMsg);
            }
        } catch (Exception e) {
            return new ValidationResult(false, "Schema 處理錯誤：" + e.getMessage());
        }
    }
    
    public record ValidationResult(boolean isValid, String error) {}
}

// 在工具處理器中使用
server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
    String name = request.getParams().getName();
    Map<String, Object> arguments = request.getParams().getArguments();
    
    // 取得工具定義
    Tool tool = findToolByName(name);
    if (tool == null) {
        return CallToolResult.error("未知工具：" + name);
    }
    
    // 驗證參數
    ArgumentValidator validator = new ArgumentValidator();
    var result = validator.validate(tool.getInputSchema(), arguments);
    if (!result.isValid()) {
        return CallToolResult.error("參數驗證失敗：" + result.error());
    }
    
    // 處理工具呼叫...
    return handleToolCall(name, arguments);
}));
```

#### 6.1.4 錯誤處理標準

> **⚠️ `2026-07-28` 需注意**：下方範例使用**字串型**錯誤代碼封裝在工具結果內，
> 這種做法仍然適用且推薦（工具執行失敗 ≠ 協議層錯誤）。
> 但若要回傳 **JSON-RPC 層級**的錯誤碼，**MUST** 遵守新的分區政策：
>
> | 區間 | 可否自訂 |
> |------|----------|
> | `-32000` ～ `-32019` | **否**（Legacy 保留） |
> | `-32020` ～ `-32099` | **否**（MCP 規範專用） |
> | `-32768` ～ `-32000` 之外 | **是**（應用層自訂） |
>
> 詳見 [8.3.1 JSON-RPC 錯誤碼與 MCP 分區政策](#83-錯誤訊息參考)。
>
> **實務建議**：優先將業務錯誤以 `CallToolResult` 的 `isError` 搭配
> 可讀訊息回傳，讓模型能自行重試或調整參數；
> JSON-RPC 錯誤碼僅保留給真正的**協議層**問題。

```java
/**
 * 標準化錯誤處理模式
 */
package com.example.mcp.error;

import io.modelcontextprotocol.spec.CallToolResult;
import java.util.*;
import java.util.function.Supplier;

/**
 * 錯誤代碼枚舉
 */
public enum ErrorCode {
    VALIDATION_ERROR("VALIDATION_ERROR"),
    NOT_FOUND("NOT_FOUND"),
    PERMISSION_DENIED("PERMISSION_DENIED"),
    RATE_LIMITED("RATE_LIMITED"),
    TIMEOUT("TIMEOUT"),
    INTERNAL_ERROR("INTERNAL_ERROR");
    
    private final String value;
    
    ErrorCode(String value) {
        this.value = value;
    }
    
    public String getValue() { return value; }
}

/**
 * 工具錯誤結構
 */
public record ToolError(
    ErrorCode code,
    String message,
    Map<String, Object> details
) {
    public ToolError(ErrorCode code, String message) {
        this(code, message, null);
    }
    
    /**
     * 轉換為 CallToolResult
     */
    public CallToolResult toCallToolResult() {
        StringBuilder errorText = new StringBuilder();
        errorText.append("❌ 錯誤 [").append(code.getValue()).append("]\n");
        errorText.append("訊息：").append(message).append("\n");
        if (details != null && !details.isEmpty()) {
            errorText.append("詳細資訊：").append(details).append("\n");
        }
        return CallToolResult.error(errorText.toString());
    }
}

/**
 * 錯誤處理工具類
 */
public class ToolErrorHandler {
    
    /**
     * 包裝工具執行，統一處理錯誤
     */
    public static CallToolResult handleToolExecution(Supplier<CallToolResult> action) {
        try {
            return action.get();
        } catch (java.nio.file.NoSuchFileException e) {
            return new ToolError(ErrorCode.NOT_FOUND, e.getMessage()).toCallToolResult();
        } catch (java.nio.file.AccessDeniedException e) {
            return new ToolError(ErrorCode.PERMISSION_DENIED, e.getMessage()).toCallToolResult();
        } catch (java.util.concurrent.TimeoutException e) {
            return new ToolError(ErrorCode.TIMEOUT, "操作超時").toCallToolResult();
        } catch (Exception e) {
            return new ToolError(
                ErrorCode.INTERNAL_ERROR,
                "內部錯誤",
                Map.of("exception", e.getMessage())
            ).toCallToolResult();
        }
    }
}

// 使用範例
server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> 
    ToolErrorHandler.handleToolExecution(() -> {
        String name = request.getParams().getName();
        return switch (name) {
            case "read_file" -> handleReadFile(request.getParams().getArguments());
            case "write_file" -> handleWriteFile(request.getParams().getArguments());
            default -> CallToolResult.error("未知工具：" + name);
        };
    })
));
```

---

### 6.2 效能優化

#### 6.2.1 連接池管理

```java
/**
 * 連接池管理最佳實踐
 */
package com.example.mcp.pool;

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.time.Duration;

/**
 * 通用連接池管理器（抽象類）
 */
public abstract class ConnectionPool<T> implements AutoCloseable {
    
    private final int minSize;
    private final int maxSize;
    private final Duration timeout;
    
    private final BlockingQueue<T> pool;
    private final AtomicInteger currentSize;
    private final Object lock = new Object();
    private volatile boolean closed = false;
    
    protected ConnectionPool(int minSize, int maxSize, Duration timeout) {
        this.minSize = minSize;
        this.maxSize = maxSize;
        this.timeout = timeout;
        this.pool = new LinkedBlockingQueue<>(maxSize);
        this.currentSize = new AtomicInteger(0);
    }
    
    /**
     * 初始化連接池
     */
    public void initialize() throws Exception {
        for (int i = 0; i < minSize; i++) {
            T conn = createConnection();
            pool.put(conn);
            currentSize.incrementAndGet();
        }
    }
    
    /**
     * 建立新連接（子類實作）
     */
    protected abstract T createConnection() throws Exception;
    
    /**
     * 驗證連接是否有效（子類實作）
     */
    protected abstract boolean validateConnection(T conn);
    
    /**
     * 關閉連接（子類實作）
     */
    protected abstract void closeConnection(T conn);
    
    /**
     * 取得連接（try-with-resources 友好）
     */
    public PooledConnection<T> acquire() throws Exception {
        if (closed) {
            throw new IllegalStateException("連接池已關閉");
        }
        
        T conn = null;
        
        // 嘗試從池中取得連接
        conn = pool.poll(timeout.toMillis(), TimeUnit.MILLISECONDS);
        
        if (conn == null) {
            // 如果沒有可用連接，嘗試建立新的
            synchronized (lock) {
                if (currentSize.get() < maxSize) {
                    conn = createConnection();
                    currentSize.incrementAndGet();
                } else {
                    throw new TimeoutException("連接池已滿，無法取得連接");
                }
            }
        }
        
        // 驗證連接
        if (!validateConnection(conn)) {
            closeConnection(conn);
            currentSize.decrementAndGet();
            conn = createConnection();
            currentSize.incrementAndGet();
        }
        
        final T finalConn = conn;
        return new PooledConnection<>(finalConn, this::release);
    }
    
    /**
     * 歸還連接
     */
    private void release(T conn) {
        if (!closed && conn != null) {
            pool.offer(conn);
        }
    }
    
    @Override
    public void close() {
        closed = true;
        T conn;
        while ((conn = pool.poll()) != null) {
            closeConnection(conn);
            currentSize.decrementAndGet();
        }
    }
    
    /**
     * 可關閉的連接包裝器
     */
    public static class PooledConnection<T> implements AutoCloseable {
        private final T connection;
        private final java.util.function.Consumer<T> releaser;
        private boolean released = false;
        
        PooledConnection(T connection, java.util.function.Consumer<T> releaser) {
            this.connection = connection;
            this.releaser = releaser;
        }
        
        public T get() { return connection; }
        
        @Override
        public void close() {
            if (!released) {
                released = true;
                releaser.accept(connection);
            }
        }
    }
}

/**
 * PostgreSQL 連接池實作（使用 HikariCP 更佳）
 */
public class PostgresPool extends ConnectionPool<java.sql.Connection> {
    
    private final String jdbcUrl;
    private final String username;
    private final String password;
    
    public PostgresPool(String jdbcUrl, String username, String password,
                        int minSize, int maxSize, Duration timeout) {
        super(minSize, maxSize, timeout);
        this.jdbcUrl = jdbcUrl;
        this.username = username;
        this.password = password;
    }
    
    @Override
    protected java.sql.Connection createConnection() throws Exception {
        return java.sql.DriverManager.getConnection(jdbcUrl, username, password);
    }
    
    @Override
    protected boolean validateConnection(java.sql.Connection conn) {
        try {
            return conn.isValid(5);
        } catch (Exception e) {
            return false;
        }
    }
    
    @Override
    protected void closeConnection(java.sql.Connection conn) {
        try {
            conn.close();
        } catch (Exception ignored) {}
    }
}
```

#### 6.2.2 快取策略

> **📌 `2026-07-28` 新增：協議層快取提示**
>
> 除了伺服器**內部**的快取（下方範例），新規範還允許伺服器透過 `ttlMs` 與 `cacheScope`
> 告知**用戶端**可快取多久（SEP-2549）。這在無狀態架構下尤其重要——
> 由於沒有 Session，用戶端依賴快取來避免重複探詢。
>
> | 層級 | 位置 | 控制方式 |
> |------|------|----------|
> | 用戶端快取 | Client | 伺服器回傳的 `ttlMs` / `cacheScope` |
> | 閘道快取 | API Gateway | 依 `Mcp-Method` 快取 `server/discover`、`tools/list` |
> | 伺服器內部快取 | Server | 下方範例的應用層快取 |
>
> **適用方法**：`server/discover`、`tools/list`、`prompts/list`、`resources/list`、
> `resources/templates/list`、`resources/read`。
>
> **重要前提**：可快取的回應 **SHOULD** 採確定性排序，
> 否則中介快取將因順序隨機而失效。`cacheScope` 若因使用者而異，
> **MUST** 設為 `"private"`，避免共用快取導致資料外洩。

```java
/**
 * 快取策略實作
 */
package com.example.mcp.cache;

import java.security.MessageDigest;
import java.time.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.Supplier;

/**
 * 快取項目
 */
record CacheEntry<V>(V value, Instant expiresAt) {
    boolean isExpired() {
        return Instant.now().isAfter(expiresAt);
    }
}

/**
 * 非同步快取
 */
public class AsyncCache<V> {
    
    private final Duration defaultTtl;
    private final int maxSize;
    private final ConcurrentHashMap<String, CacheEntry<V>> cache;
    private final ScheduledExecutorService cleanupExecutor;
    
    public AsyncCache(Duration defaultTtl, int maxSize) {
        this.defaultTtl = defaultTtl;
        this.maxSize = maxSize;
        this.cache = new ConcurrentHashMap<>();
        
        // 定期清理過期項目
        this.cleanupExecutor = Executors.newSingleThreadScheduledExecutor();
        cleanupExecutor.scheduleAtFixedRate(
            this::cleanup, 
            1, 1, TimeUnit.MINUTES
        );
    }
    
    /**
     * 生成快取鍵
     */
    public String makeKey(Object... parts) {
        try {
            String keyData = Arrays.toString(parts);
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] digest = md.digest(keyData.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (Exception e) {
            return Arrays.toString(parts).hashCode() + "";
        }
    }
    
    /**
     * 取得快取值
     */
    public CompletableFuture<Optional<V>> get(String key) {
        return CompletableFuture.supplyAsync(() -> {
            CacheEntry<V> entry = cache.get(key);
            if (entry != null && !entry.isExpired()) {
                return Optional.of(entry.value());
            } else if (entry != null) {
                cache.remove(key);
            }
            return Optional.empty();
        });
    }
    
    /**
     * 設定快取值
     */
    public CompletableFuture<Void> set(String key, V value, Duration ttl) {
        return CompletableFuture.runAsync(() -> {
            // 清理過期項目（如果接近上限）
            if (cache.size() >= maxSize) {
                cleanup();
            }
            
            Instant expiresAt = Instant.now().plus(ttl != null ? ttl : defaultTtl);
            cache.put(key, new CacheEntry<>(value, expiresAt));
        });
    }
    
    public CompletableFuture<Void> set(String key, V value) {
        return set(key, value, null);
    }
    
    /**
     * 清理過期快取
     */
    private void cleanup() {
        Instant now = Instant.now();
        cache.entrySet().removeIf(entry -> entry.getValue().isExpired());
    }
    
    /**
     * 關閉快取
     */
    public void close() {
        cleanupExecutor.shutdown();
        cache.clear();
    }
}

/**
 * 帶快取的函數包裝器
 */
public class CachedFunction<T> {
    
    private final AsyncCache<T> cache;
    private final Duration ttl;
    
    public CachedFunction(AsyncCache<T> cache, Duration ttl) {
        this.cache = cache;
        this.ttl = ttl;
    }
    
    /**
     * 帶快取執行函數
     */
    public CompletableFuture<T> execute(
        Supplier<CompletableFuture<T>> function,
        Object... keyParts
    ) {
        String key = cache.makeKey(keyParts);
        
        return cache.get(key).thenCompose(cached -> {
            if (cached.isPresent()) {
                return CompletableFuture.completedFuture(cached.get());
            }
            
            return function.get().thenCompose(result -> 
                cache.set(key, result, ttl).thenApply(v -> result)
            );
        });
    }
}

// 使用範例
public class GitHubService {
    
    private final AsyncCache<Map<String, Object>> cache = 
        new AsyncCache<>(Duration.ofMinutes(5), 1000);
    private final CachedFunction<Map<String, Object>> cachedFunction = 
        new CachedFunction<>(cache, Duration.ofMinutes(1));
    
    /**
     * 取得儲存庫資訊（帶快取）
     */
    public CompletableFuture<Map<String, Object>> getRepositoryInfo(String owner, String repo) {
        return cachedFunction.execute(
            () -> githubRequest("GET", "/repos/" + owner + "/" + repo),
            "getRepositoryInfo", owner, repo
        );
    }
}
```

#### 6.2.3 批次處理

```java
/**
 * 批次處理模式
 */
package com.example.mcp.batch;

import java.util.*;
import java.util.concurrent.*;
import java.util.function.Function;
import java.util.stream.*;

public class BatchProcessor {
    
    /**
     * 批次處理項目
     *
     * @param items 要處理的項目列表
     * @param processor 處理函數
     * @param batchSize 批次大小
     * @param delayBetweenBatches 批次間延遲
     * @return 處理結果列表
     */
    public static <T, R> CompletableFuture<List<R>> batchProcess(
        List<T> items,
        Function<T, CompletableFuture<R>> processor,
        int batchSize,
        Duration delayBetweenBatches
    ) {
        if (items.isEmpty()) {
            return CompletableFuture.completedFuture(Collections.emptyList());
        }
        
        List<List<T>> batches = partition(items, batchSize);
        List<R> results = new CopyOnWriteArrayList<>();
        
        return processBatchesSequentially(batches, processor, delayBetweenBatches, results)
            .thenApply(v -> new ArrayList<>(results));
    }
    
    /**
     * 分割列表為批次
     */
    private static <T> List<List<T>> partition(List<T> list, int size) {
        List<List<T>> partitions = new ArrayList<>();
        for (int i = 0; i < list.size(); i += size) {
            partitions.add(list.subList(i, Math.min(i + size, list.size())));
        }
        return partitions;
    }
    
    /**
     * 順序處理批次
     */
    private static <T, R> CompletableFuture<Void> processBatchesSequentially(
        List<List<T>> batches,
        Function<T, CompletableFuture<R>> processor,
        Duration delay,
        List<R> results
    ) {
        CompletableFuture<Void> future = CompletableFuture.completedFuture(null);
        
        for (int i = 0; i < batches.size(); i++) {
            final List<T> batch = batches.get(i);
            final boolean isLastBatch = (i == batches.size() - 1);
            
            future = future.thenCompose(v -> {
                // 並行處理批次內的項目
                List<CompletableFuture<R>> futures = batch.stream()
                    .map(item -> processor.apply(item)
                        .exceptionally(e -> null))  // 處理單項錯誤
                    .collect(Collectors.toList());
                
                return CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                    .thenRun(() -> {
                        futures.forEach(f -> {
                            try {
                                R result = f.get();
                                if (result != null) results.add(result);
                            } catch (Exception ignored) {}
                        });
                    });
            });
            
            // 批次間延遲（最後一批不延遲）
            if (!isLastBatch) {
                future = future.thenCompose(v -> 
                    CompletableFuture.runAsync(() -> {
                        try {
                            Thread.sleep(delay.toMillis());
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                    })
                );
            }
        }
        
        return future;
    }
}

// 使用範例
public class FileProcessor {
    
    /**
     * 批次處理檔案
     */
    public CompletableFuture<List<FileInfo>> processFiles(List<String> filePaths) {
        return BatchProcessor.batchProcess(
            filePaths,
            this::readAndAnalyze,
            10,                          // 批次大小
            Duration.ofMillis(100)       // 批次間延遲
        );
    }
    
    private CompletableFuture<FileInfo> readAndAnalyze(String path) {
        return CompletableFuture.supplyAsync(() -> {
            try {
                String content = java.nio.file.Files.readString(java.nio.file.Path.of(path));
                return new FileInfo(
                    path,
                    content.length(),
                    content.lines().count()
                );
            } catch (Exception e) {
                return null;
            }
        });
    }
    
    public record FileInfo(String path, long size, long lines) {}
}
```

---

### 6.3 安全性考量

#### 6.3.1 認證與授權

> **⚠️ `2026-07-28` 重大變更**：授權模型已大幅硬化，下方 JWT 範例僅示範
> **應用層**的權限判定骨架，實際的 **MCP 授權流程**必須改依新規範：
>
> | 項目 | `2025-11-25` | `2026-07-28` |
> |------|-------------|-------------|
> | 動態用戶端註冊（DCR） | 建議支援 | **移除**，改用預先註冊或 EMA |
> | 憑證繫結 | 未強制 | Resource Indicator（RFC 8707）**MUST** |
> | 企業託管授權 | 無 | **EMA 擴充**（`io.modelcontextprotocol/ema`） |
> | 權杖生命週期 | 依 Session | 與 Session 解耦，**每次請求獨立驗證** |
> | 缺少必要能力 | 泛用錯誤 | `-32021` MissingRequiredClientCapability |
>
> 由於已無 Session，**每一次請求都必須獨立完成認證與授權**，
> 不可將授權結果快取於連線層。詳見
> [13.3 授權硬化與身分治理](#133-授權硬化與身分治理) 與
> [12.4 企業託管授權（EMA）與 OAuth 擴充](#124-企業託管授權ema與-oauth-擴充)。

```java
/**
 * 認證授權模式
 */
package com.example.mcp.security;

import io.jsonwebtoken.*;
import io.jsonwebtoken.security.Keys;

import java.nio.charset.StandardCharsets;
import java.security.Key;
import java.time.*;
import java.util.*;

/**
 * 認證錯誤
 */
public class AuthError extends Exception {
    public AuthError(String message) {
        super(message);
    }
}

/**
 * JWT Token 管理器
 */
public class TokenManager {
    
    private final Key secretKey;
    private final Duration tokenExpiry;
    
    public TokenManager(String secret, Duration tokenExpiry) {
        this.secretKey = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
        this.tokenExpiry = tokenExpiry;
    }
    
    public TokenManager() {
        this(
            System.getenv().getOrDefault("MCP_SECRET_KEY", "change-me-in-production-with-at-least-32-chars"),
            Duration.ofHours(24)
        );
    }
    
    /**
     * 生成 JWT Token
     */
    public String generateToken(String userId, List<String> permissions) {
        Instant now = Instant.now();
        
        return Jwts.builder()
            .setSubject(userId)
            .claim("permissions", permissions)
            .setIssuedAt(Date.from(now))
            .setExpiration(Date.from(now.plus(tokenExpiry)))
            .signWith(secretKey, SignatureAlgorithm.HS256)
            .compact();
    }
    
    /**
     * 驗證 JWT Token
     */
    public TokenPayload verifyToken(String token) throws AuthError {
        try {
            Claims claims = Jwts.parserBuilder()
                .setSigningKey(secretKey)
                .build()
                .parseClaimsJws(token)
                .getBody();
            
            @SuppressWarnings("unchecked")
            List<String> permissions = claims.get("permissions", List.class);
            
            return new TokenPayload(
                claims.getSubject(),
                permissions != null ? permissions : List.of(),
                claims.getIssuedAt().toInstant(),
                claims.getExpiration().toInstant()
            );
        } catch (ExpiredJwtException e) {
            throw new AuthError("Token 已過期");
        } catch (JwtException e) {
            throw new AuthError("無效的 Token");
        }
    }
    
    public record TokenPayload(
        String userId,
        List<String> permissions,
        Instant issuedAt,
        Instant expiresAt
    ) {}
}

/**
 * 權限檢查器
 */
public class PermissionChecker {
    
    private final TokenManager tokenManager;
    
    // 工具層級權限對應
    private static final Map<String, List<String>> TOOL_PERMISSIONS = Map.of(
        "read_file", List.of("file:read"),
        "write_file", List.of("file:write"),
        "delete_file", List.of("file:delete"),
        "query", List.of("db:read"),
        "execute", List.of("db:write")
    );
    
    public PermissionChecker(TokenManager tokenManager) {
        this.tokenManager = tokenManager;
    }
    
    /**
     * 檢查工具權限
     */
    public void checkToolPermission(String toolName, String token) throws AuthError {
        if (token == null || token.isEmpty()) {
            throw new AuthError("需要認證");
        }
        
        TokenManager.TokenPayload payload = tokenManager.verifyToken(token);
        List<String> requiredPermissions = TOOL_PERMISSIONS.getOrDefault(toolName, List.of());
        
        for (String perm : requiredPermissions) {
            if (!payload.permissions().contains(perm)) {
                throw new AuthError("缺少權限：" + perm);
            }
        }
    }
}

// 在工具處理器中使用
server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
    String name = request.getParams().getName();
    String authToken = getAuthTokenFromContext();  // 從 context 取得
    
    try {
        permissionChecker.checkToolPermission(name, authToken);
    } catch (AuthError e) {
        return CallToolResult.error("權限不足：" + e.getMessage());
    }
    
    // 執行工具...
    return handleToolCall(name, request.getParams().getArguments());
}));
```

#### 6.3.2 輸入驗證

```java
/**
 * 輸入驗證模式
 */
package com.example.mcp.security;

import java.nio.file.Path;
import java.util.List;
import java.util.regex.*;

/**
 * 輸入驗證器
 */
public class InputValidator {
    
    /**
     * 清理字串
     */
    public static String sanitizeString(String value, int maxLength) {
        if (value == null) return "";
        
        // 截斷長度
        String result = value.length() > maxLength ? value.substring(0, maxLength) : value;
        
        // HTML 編碼
        return result
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\"", "&quot;")
            .replace("'", "&#x27;");
    }
    
    public static String sanitizeString(String value) {
        return sanitizeString(value, 1000);
    }
    
    /**
     * 驗證路徑安全性
     */
    public static ValidationResult validatePath(String pathStr, List<String> allowedRoots) {
        try {
            Path resolved = Path.of(pathStr).toAbsolutePath().normalize();
            
            // 檢查路徑遍歷
            for (String root : allowedRoots) {
                Path rootPath = Path.of(root).toAbsolutePath().normalize();
                if (resolved.startsWith(rootPath)) {
                    return new ValidationResult(true, resolved.toString());
                }
            }
            
            return new ValidationResult(false, "路徑不在允許範圍內");
        } catch (Exception e) {
            return new ValidationResult(false, "無效的路徑：" + e.getMessage());
        }
    }
    
    /**
     * 驗證 SQL 安全性
     */
    public static ValidationResult validateSql(String query) {
        if (query == null || query.isBlank()) {
            return new ValidationResult(false, "查詢不能為空");
        }
        
        // 移除註解
        String cleanQuery = query
            .replaceAll("--.*$", "")
            .replaceAll("/\\*.*?\\*/", "");
        String upperQuery = cleanQuery.toUpperCase().trim();
        
        // 僅允許 SELECT
        if (!upperQuery.startsWith("SELECT")) {
            return new ValidationResult(false, "僅允許 SELECT 查詢");
        }
        
        // 檢查危險關鍵字
        List<String> dangerous = List.of("DROP", "DELETE", "TRUNCATE", "UPDATE", "INSERT", "ALTER");
        for (String kw : dangerous) {
            Pattern pattern = Pattern.compile("\\b" + kw + "\\b", Pattern.CASE_INSENSITIVE);
            if (pattern.matcher(upperQuery).find()) {
                return new ValidationResult(false, "不允許的關鍵字：" + kw);
            }
        }
        
        return new ValidationResult(true, "");
    }
    
    /**
     * 驗證識別符（表名、欄位名）
     */
    public static ValidationResult validateIdentifier(String name, int maxLength) {
        if (name == null || name.isEmpty()) {
            return new ValidationResult(false, "識別符不能為空");
        }
        
        if (name.length() > maxLength) {
            return new ValidationResult(false, "識別符過長（最大 " + maxLength + "）");
        }
        
        if (!name.matches("^[a-zA-Z_][a-zA-Z0-9_]*$")) {
            return new ValidationResult(false, "識別符包含非法字元");
        }
        
        return new ValidationResult(true, "");
    }
    
    public static ValidationResult validateIdentifier(String name) {
        return validateIdentifier(name, 63);
    }
    
    public record ValidationResult(boolean isValid, String message) {}
}
```

#### 6.3.3 敏感資料處理

```java
/**
 * 敏感資料處理
 */
package com.example.mcp.security;

import java.util.*;
import java.util.logging.*;
import java.util.regex.*;

/**
 * 敏感資料處理器
 */
public class SensitiveDataHandler {
    
    // 敏感欄位模式
    private static final List<String> SENSITIVE_PATTERNS = List.of(
        "password", "secret", "token", "api_key", "apikey",
        "authorization", "credential", "private_key"
    );
    
    private static final Pattern SENSITIVE_REGEX = Pattern.compile(
        String.join("|", SENSITIVE_PATTERNS),
        Pattern.CASE_INSENSITIVE
    );
    
    /**
     * 遮罩敏感值
     */
    public static String maskSensitiveValue(String value, int visibleChars) {
        if (value == null) return null;
        if (value.length() <= visibleChars) {
            return "*".repeat(value.length());
        }
        return value.substring(0, visibleChars) + "*".repeat(value.length() - visibleChars);
    }
    
    public static String maskSensitiveValue(String value) {
        return maskSensitiveValue(value, 4);
    }
    
    /**
     * 清理資料以供日誌記錄
     */
    @SuppressWarnings("unchecked")
    public static Object sanitizeForLogging(Object data, int depth) {
        if (depth > 10) {
            return "<max depth reached>";
        }
        
        if (data instanceof Map) {
            Map<String, Object> result = new LinkedHashMap<>();
            Map<String, Object> map = (Map<String, Object>) data;
            
            for (Map.Entry<String, Object> entry : map.entrySet()) {
                String key = entry.getKey();
                Object value = entry.getValue();
                
                if (SENSITIVE_REGEX.matcher(key).find()) {
                    result.put(key, maskSensitiveValue(String.valueOf(value)));
                } else {
                    result.put(key, sanitizeForLogging(value, depth + 1));
                }
            }
            return result;
        } else if (data instanceof List) {
            List<Object> result = new ArrayList<>();
            for (Object item : (List<?>) data) {
                result.add(sanitizeForLogging(item, depth + 1));
            }
            return result;
        } else if (data instanceof String) {
            String str = (String) data;
            // 檢查是否像 Token
            if (str.length() > 20 && str.matches("^[A-Za-z0-9_\\-]+$")) {
                return maskSensitiveValue(str);
            }
            return str;
        }
        
        return data;
    }
    
    public static Object sanitizeForLogging(Object data) {
        return sanitizeForLogging(data, 0);
    }
}

/**
 * 安全日誌類別
 */
public class SecureLogger {
    
    private final Logger logger;
    
    public SecureLogger(String name) {
        this.logger = Logger.getLogger(name);
    }
    
    public void info(String message, Object data) {
        if (data != null) {
            data = SensitiveDataHandler.sanitizeForLogging(data);
        }
        logger.info(data != null ? message + " " + data : message);
    }
    
    public void info(String message) {
        info(message, null);
    }
    
    public void error(String message, Object data) {
        if (data != null) {
            data = SensitiveDataHandler.sanitizeForLogging(data);
        }
        logger.severe(data != null ? message + " " + data : message);
    }
    
    public void error(String message) {
        error(message, null);
    }
}
```

#### 6.3.4 速率限制

```java
/**
 * 速率限制實作
 */
package com.example.mcp.security;

import java.time.*;
import java.util.*;
import java.util.concurrent.*;

/**
 * 滑動窗口速率限制器
 */
public class RateLimiter {
    
    private final int maxRequests;
    private final Duration windowDuration;
    private final ConcurrentHashMap<String, Deque<Instant>> requests;
    
    public RateLimiter(int maxRequests, Duration windowDuration) {
        this.maxRequests = maxRequests;
        this.windowDuration = windowDuration;
        this.requests = new ConcurrentHashMap<>();
    }
    
    public RateLimiter() {
        this(100, Duration.ofMinutes(1));
    }
    
    /**
     * 檢查請求是否允許
     */
    public synchronized RateLimitResult isAllowed(String key) {
        Instant now = Instant.now();
        Instant windowStart = now.minus(windowDuration);
        
        // 取得或建立請求佇列
        Deque<Instant> keyRequests = requests.computeIfAbsent(key, k -> new ConcurrentLinkedDeque<>());
        
        // 清理過期記錄
        while (!keyRequests.isEmpty() && keyRequests.peekFirst().isBefore(windowStart)) {
            keyRequests.pollFirst();
        }
        
        int currentCount = keyRequests.size();
        int remaining = Math.max(0, maxRequests - currentCount);
        Instant resetAt = now.plus(windowDuration);
        
        RateLimitInfo info = new RateLimitInfo(maxRequests, remaining, resetAt);
        
        if (currentCount >= maxRequests) {
            return new RateLimitResult(false, info);
        }
        
        keyRequests.addLast(now);
        return new RateLimitResult(true, new RateLimitInfo(maxRequests, remaining - 1, resetAt));
    }
    
    public record RateLimitInfo(int limit, int remaining, Instant resetAt) {}
    public record RateLimitResult(boolean allowed, RateLimitInfo info) {}
}

// 在工具處理器中使用
public class RateLimitedToolHandler {
    
    private final RateLimiter rateLimiter = new RateLimiter(100, Duration.ofMinutes(1));
    
    public CompletableFuture<CallToolResult> handleToolCall(
        String toolName,
        Map<String, Object> arguments,
        String rateLimitKey
    ) {
        return CompletableFuture.supplyAsync(() -> {
            // 檢查速率限制
            RateLimiter.RateLimitResult result = rateLimiter.isAllowed(rateLimitKey);
            
            if (!result.allowed()) {
                return CallToolResult.error(String.format(
                    "速率限制：請稍後再試%n剩餘配額：%d/%d",
                    result.info().remaining(),
                    result.info().limit()
                ));
            }
            
            // 執行工具...
            return executeToolInternal(toolName, arguments);
        });
    }
    
    private CallToolResult executeToolInternal(String name, Map<String, Object> args) {
        // 實際工具執行邏輯
        return CallToolResult.text("執行結果");
    }
}
```

---

### 6.4 測試策略

> **📌 `2026-07-28` 新增測試面向**
>
> 除了傳統的單元、整合與 Mock 測試，無狀態架構帶來四項**必需新增**的測試項目：
>
> | 測試面向 | 驗證重點 |
> |----------|----------|
> | **無狀態性** | 連續兩次請求分別送到不同實例，結果 **MUST** 一致 |
> | **自描述請求** | 缺少 `_meta` 必要欄位時回 `-32602`；標頭與 Body 不符時回 `-32020` |
> | **快取確定性** | 相同輸入下 `tools/list` 回傳順序 **MUST** 相同，否則中介快取失效 |
> | **MRTR 循環** | `input_required` → 補送 `inputResponses` → `complete` 的完整路徑，並驗證輪數上限 |
>
> 此外，符規性應以官方
> [Conformance Suite](https://github.com/modelcontextprotocol/conformance)
> 作為 CI 闘門，而非僅依賴自寫測試。參見
> [13.5 一致性驗證與 SDK 分級](#135-一致性驗證與-sdk-分級)。

#### 6.4.1 單元測試

```java
/**
 * MCP Server 單元測試範例
 */
package com.example.mcp.test;

import org.junit.jupiter.api.*;
import org.junit.jupiter.api.io.TempDir;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.nio.file.*;
import java.util.*;
import java.util.concurrent.*;

/**
 * 工具測試
 */
class ToolsTest {
    
    @Test
    void testListTools() throws Exception {
        // 取得工具列表
        List<Tool> tools = server.listTools().get();
        
        assertFalse(tools.isEmpty());
        assertTrue(tools.stream().allMatch(t -> t.getName() != null));
        assertTrue(tools.stream().allMatch(t -> t.getDescription() != null));
        assertTrue(tools.stream().allMatch(t -> t.getInputSchema() != null));
    }
    
    @Test
    void testReadFileSuccess(@TempDir Path tempDir) throws Exception {
        // 建立測試檔案
        Path testFile = tempDir.resolve("test.txt");
        Files.writeString(testFile, "Hello, World!");
        
        // 模擬允許的路徑
        List<String> originalAllowed = ALLOWED_DIRECTORIES;
        try {
            ALLOWED_DIRECTORIES = List.of(tempDir.toString());
            
            CallToolResult result = handleReadFile(Map.of("path", testFile.toString())).get();
            
            assertTrue(result.isSuccess());
            assertEquals("Hello, World!", result.getText());
        } finally {
            ALLOWED_DIRECTORIES = originalAllowed;
        }
    }
    
    @Test
    void testReadFileNotFound() throws Exception {
        CallToolResult result = handleReadFile(Map.of("path", "/nonexistent/file.txt")).get();
        
        assertTrue(result.isError());
        assertTrue(result.getText().contains("不存在") || result.getText().contains("錯誤"));
    }
    
    @Test
    void testReadFilePermissionDenied(@TempDir Path tempDir) throws Exception {
        // 設定不允許的路徑
        List<String> originalAllowed = ALLOWED_DIRECTORIES;
        try {
            ALLOWED_DIRECTORIES = List.of("/other/path");
            
            Path testFile = tempDir.resolve("test.txt");
            Files.writeString(testFile, "content");
            
            CallToolResult result = handleReadFile(Map.of("path", testFile.toString())).get();
            
            assertTrue(result.isError());
            assertTrue(result.getText().contains("拒絕") || result.getText().contains("錯誤"));
        } finally {
            ALLOWED_DIRECTORIES = originalAllowed;
        }
    }
    
    @Test
    void testQueryValidation() {
        // 有效查詢
        var validResult = InputValidator.validateSql("SELECT * FROM users WHERE id = 1");
        assertTrue(validResult.isValid());
        
        // 無效查詢 - DROP
        var dropResult = InputValidator.validateSql("DROP TABLE users");
        assertFalse(dropResult.isValid());
        assertTrue(dropResult.message().contains("DROP") || dropResult.message().contains("SELECT"));
        
        // 無效查詢 - 多語句
        var multiResult = InputValidator.validateSql("SELECT 1; DELETE FROM users");
        assertFalse(multiResult.isValid());
    }
}

/**
 * 輸入驗證測試
 */
class InputValidationTest {
    
    @Test
    void testValidatePathSafe() {
        var result = InputValidator.validatePath(
            "/home/user/documents/file.txt",
            List.of("/home/user")
        );
        assertTrue(result.isValid());
    }
    
    @Test
    void testValidatePathTraversal() {
        // 測試路徑遍歷攻擊
        var result = InputValidator.validatePath(
            "/home/user/../../../etc/passwd",
            List.of("/home/user")
        );
        assertFalse(result.isValid());
    }
    
    @Test
    void testValidateIdentifierValid() {
        // 測試有效識別符
        var result = InputValidator.validateIdentifier("user_table");
        assertTrue(result.isValid());
    }
    
    @Test
    void testValidateIdentifierInvalid() {
        // 測試無效識別符
        var result = InputValidator.validateIdentifier("user; DROP TABLE--");
        assertFalse(result.isValid());
    }
}
```

#### 6.4.2 整合測試

```java
/**
 * MCP Server 整合測試
 */
package com.example.mcp.test;

import io.modelcontextprotocol.client.*;
import io.modelcontextprotocol.client.transport.StdioClientTransport;
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.*;
import java.util.concurrent.*;

class IntegrationTest {
    
    private McpClient client;
    
    @BeforeEach
    void setUp() throws Exception {
        // 建立 MCP Client
        ProcessBuilder pb = new ProcessBuilder(
            "java", "-jar", "target/my-mcp-server-1.0.0.jar"
        );
        pb.environment().put("MCP_ALLOWED_DIRS", "/tmp");
        
        Process process = pb.start();
        StdioClientTransport transport = new StdioClientTransport(
            process.getInputStream(),
            process.getOutputStream()
        );
        
        client = new McpClient(McpClientOptions.builder()
            .clientInfo(ClientInfo.builder()
                .name("test-client")
                .version("1.0.0")
                .build())
            .build());
        
        client.connect(transport).get(10, TimeUnit.SECONDS);
    }
    
    @AfterEach
    void tearDown() {
        if (client != null) {
            client.close();
        }
    }
    
    @Test
    void testFullWorkflow() throws Exception {
        // 測試完整工作流程
        
        // 1. 列出工具
        ListToolsResult toolsResult = client.listTools().get(5, TimeUnit.SECONDS);
        assertFalse(toolsResult.getTools().isEmpty());
        
        // 2. 寫入檔案
        CallToolResult writeResult = client.callTool(
            "write_file",
            Map.of(
                "path", "/tmp/test_integration.txt",
                "content", "Integration test content"
            )
        ).get(5, TimeUnit.SECONDS);
        assertTrue(writeResult.getText().contains("成功"));
        
        // 3. 讀取檔案
        CallToolResult readResult = client.callTool(
            "read_file",
            Map.of("path", "/tmp/test_integration.txt")
        ).get(5, TimeUnit.SECONDS);
        assertTrue(readResult.getText().contains("Integration test content"));
        
        // 4. 刪除檔案
        CallToolResult deleteResult = client.callTool(
            "delete_file",
            Map.of(
                "path", "/tmp/test_integration.txt",
                "confirm", true
            )
        ).get(5, TimeUnit.SECONDS);
        assertTrue(deleteResult.getText().contains("成功"));
    }
}
```

#### 6.4.3 使用 MCP Inspector 進行測試

```bash
# 啟動 Inspector 並連接到 Server
npx @modelcontextprotocol/inspector java -jar target/my-mcp-server-1.0.0.jar

# Inspector 會開啟 Web UI，可以：
# 1. 查看所有可用工具
# 2. 手動執行工具並查看結果
# 3. 檢視原始 JSON-RPC 訊息
# 4. 監控 Server 日誌
```

> **📌 搭配 Conformance Suite**：Inspector 適合**人工探索**，
> 但無法證明符規。企業專案應將官方符規測試集納入 CI：
>
> ```bash
> # 對本地 Server 執行官方符規測試（實際指令請依官方倉庫說明為準）
> npx @modelcontextprotocol/conformance --target http://localhost:8080/mcp \
>   --protocol-version 2026-07-28
> ```
>
> 建議將符規測試設為**合併前必過闘門**，並將報告保留作為發布證據。

#### 6.4.4 模擬與 Mock

```java
/**
 * Mock 測試範例
 */
package com.example.mcp.test;

import org.junit.jupiter.api.*;
import org.mockito.*;
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.*;
import java.util.concurrent.*;

class MockTest {
    
    @Mock
    private GitHubApiClient mockGitHubClient;
    
    @Mock
    private DatabaseConnectionPool mockDbPool;
    
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }
    
    @Test
    void testGitHubApiWithMock() throws Exception {
        // 模擬 GitHub API 回應
        Map<String, Object> mockResponse = Map.of(
            "full_name", "test/repo",
            "description", "Test repository",
            "stargazers_count", 100
        );
        
        when(mockGitHubClient.request(eq("GET"), eq("/repos/test/repo"), any()))
            .thenReturn(CompletableFuture.completedFuture(mockResponse));
        
        // 執行測試
        GitHubMcpServer server = new GitHubMcpServer(mockGitHubClient);
        CallToolResult result = server.handleGetRepo(Map.of(
            "owner", "test",
            "repo", "repo"
        ));
        
        assertTrue(result.getText().contains("test/repo"));
        assertTrue(result.getText().contains("100"));
        
        verify(mockGitHubClient).request(eq("GET"), eq("/repos/test/repo"), any());
    }
    
    @Test
    void testDatabaseWithMock() throws Exception {
        // 模擬資料庫查詢結果
        List<Map<String, Object>> mockRows = List.of(
            Map.of("id", 1, "name", "Alice"),
            Map.of("id", 2, "name", "Bob")
        );
        
        Connection mockConn = mock(Connection.class);
        PreparedStatement mockStmt = mock(PreparedStatement.class);
        ResultSet mockRs = mock(ResultSet.class);
        
        when(mockDbPool.getConnection()).thenReturn(mockConn);
        when(mockConn.prepareStatement(anyString())).thenReturn(mockStmt);
        when(mockStmt.executeQuery()).thenReturn(mockRs);
        
        // 模擬 ResultSet 迭代
        when(mockRs.next()).thenReturn(true, true, false);
        when(mockRs.getObject("id")).thenReturn(1, 2);
        when(mockRs.getObject("name")).thenReturn("Alice", "Bob");
        
        // 執行測試
        DatabaseMcpServer server = new DatabaseMcpServer(mockDbPool);
        CallToolResult result = server.handleQuery(Map.of(
            "sql", "SELECT * FROM users",
            "limit", 10
        ));
        
        assertTrue(result.getText().contains("Alice"));
        assertTrue(result.getText().contains("Bob"));
    }
    
    @Test
    void testRateLimiterMock() {
        // 測試速率限制器
        RateLimiter rateLimiter = new RateLimiter(2, Duration.ofSeconds(1));
        
        // 前兩次應該允許
        assertTrue(rateLimiter.isAllowed("test-key").allowed());
        assertTrue(rateLimiter.isAllowed("test-key").allowed());
        
        // 第三次應該被限制
        assertFalse(rateLimiter.isAllowed("test-key").allowed());
    }
}
```

---

## 第七章：進階主題

### 7.1 Tasks 擴充（io.modelcontextprotocol/tasks）

#### 7.1.1 Tasks 概述

> **⚠️ 版本狀態變更**：Tasks 在 `2025-11-25` 屬於**核心規範中的實驗性功能**；
> 自 `2026-07-28` 起已**移出核心**，成為官方擴充 `io.modelcontextprotocol/tasks`（SEP-2663）。
> 本節說明其設計原理與實作骨架；擴充協商細節與新版方法規格請見
> [12.3 Tasks 擴充深入解析](#123-tasks-擴充深入解析)。

Tasks 用於處理長時間運行的操作，將「執行」與「取得結果」解耦：

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server

    Note over C,S: Client 於 _meta 宣告支援 tasks 擴充
    C->>S: tools/call（長時間操作）
    Note over S: 伺服器主導：決定轉為 Task
    S-->>C: CreateTaskResult（resultType: task）<br/>taskId / status / ttlMs / pollIntervalMs

    loop 輪詢（間隔 pollIntervalMs）
        C->>S: tasks/get (taskId)
        S-->>C: status: working / input_required / completed / failed / cancelled
    end

    alt 需要中途輸入
        C->>S: tasks/update（inputResponses）
        S-->>C: status: working
    end

    C->>S: tasks/get (taskId)
    S-->>C: status: completed + result
```

**`2026-07-28` 與舊版的關鍵差異**：

| 項目 | `2025-11-25`（實驗性） | `2026-07-28`（擴充） |
|------|----------------------|--------------------|
| 取結果 | `tasks/result` | **已移除**，改用 `tasks/get` |
| 列任務 | `tasks/list` | **已移除**（無 Session 無法安全界定範圍） |
| 決策者 | 用戶端逐請求 opt-in | **伺服器主導** |
| 狀態集 | `pending`/`running`/... | `working`/`input_required`/`completed`/`failed`/`cancelled` |
| 推播 | 無標準機制 | `notifications/tasks`（經 `subscriptions/listen` 訂閱） |

> **遷移提醒**：既有採用 `2025-11-25` 實驗性 Tasks API 的實作**必須遷移**。
> 下方 Java 範例展示的是任務儲存與生命週期管理的通用骨架，
> 對外方法名稱請依 `2026-07-28` 擴充規格調整。

#### 7.1.2 實作範例

```java
/**
 * Tasks 實作範例
 */
package com.example.mcp.tasks;

import java.time.*;
import java.util.*;
import java.util.concurrent.*;

/**
 * 任務狀態枚舉
 */
public enum TaskStatus {
    PENDING("pending"),
    RUNNING("running"),
    COMPLETED("completed"),
    FAILED("failed"),
    CANCELLED("cancelled");
    
    private final String value;
    
    TaskStatus(String value) {
        this.value = value;
    }
    
    public String getValue() { return value; }
}

/**
 * 任務實體
 */
public class Task {
    private final String id;
    private final String name;
    private volatile TaskStatus status;
    private volatile double progress;
    private volatile Object result;
    private volatile String error;
    private final Instant createdAt;
    private volatile Instant completedAt;
    
    public Task(String id, String name) {
        this.id = id;
        this.name = name;
        this.status = TaskStatus.PENDING;
        this.progress = 0.0;
        this.createdAt = Instant.now();
    }
    
    // Getters and setters
    public String getId() { return id; }
    public String getName() { return name; }
    public TaskStatus getStatus() { return status; }
    public void setStatus(TaskStatus status) { this.status = status; }
    public double getProgress() { return progress; }
    public void setProgress(double progress) { this.progress = progress; }
    public Object getResult() { return result; }
    public void setResult(Object result) { this.result = result; }
    public String getError() { return error; }
    public void setError(String error) { this.error = error; }
    public Instant getCreatedAt() { return createdAt; }
    public Instant getCompletedAt() { return completedAt; }
    public void setCompletedAt(Instant completedAt) { this.completedAt = completedAt; }
}

/**
 * 任務管理器
 */
public class TaskManager {
    
    private final ConcurrentHashMap<String, Task> tasks = new ConcurrentHashMap<>();
    private final ConcurrentHashMap<String, CompletableFuture<?>> runningTasks = new ConcurrentHashMap<>();
    private final ExecutorService executor = Executors.newCachedThreadPool();
    
    /**
     * 建立新任務
     */
    public Task createTask(String name) {
        String taskId = UUID.randomUUID().toString();
        Task task = new Task(taskId, name);
        tasks.put(taskId, task);
        return task;
    }
    
    /**
     * 執行任務
     */
    public <T> CompletableFuture<T> runTask(
        String taskId,
        Callable<T> callable,
        java.util.function.Consumer<Double> progressCallback
    ) {
        Task task = tasks.get(taskId);
        if (task == null) {
            throw new IllegalArgumentException("任務不存在：" + taskId);
        }
        
        task.setStatus(TaskStatus.RUNNING);
        
        CompletableFuture<T> future = CompletableFuture.supplyAsync(() -> {
            try {
                T result = callable.call();
                task.setResult(result);
                task.setStatus(TaskStatus.COMPLETED);
                return result;
            } catch (CancellationException e) {
                task.setStatus(TaskStatus.CANCELLED);
                throw e;
            } catch (Exception e) {
                task.setError(e.getMessage());
                task.setStatus(TaskStatus.FAILED);
                throw new CompletionException(e);
            } finally {
                task.setCompletedAt(Instant.now());
            }
        }, executor);
        
        runningTasks.put(taskId, future);
        return future;
    }
    
    /**
     * 取得任務狀態
     */
    public Optional<Task> getTask(String taskId) {
        return Optional.ofNullable(tasks.get(taskId));
    }
    
    /**
     * 取消任務
     */
    public boolean cancelTask(String taskId) {
        CompletableFuture<?> future = runningTasks.get(taskId);
        if (future != null) {
            return future.cancel(true);
        }
        return false;
    }
    
    /**
     * 更新進度
     */
    public void updateProgress(String taskId, double progress) {
        Task task = tasks.get(taskId);
        if (task != null) {
            task.setProgress(progress);
        }
    }
    
    /**
     * 關閉管理器
     */
    public void shutdown() {
        executor.shutdown();
    }
}

// 在 MCP Server 中使用任務管理器
public class TaskEnabledMcpServer {
    
    private final McpServer server;
    private final TaskManager taskManager = new TaskManager();
    
    public TaskEnabledMcpServer() {
        // 初始化 server...
        this.server = createServer();
        setupHandlers();
    }
    
    private void setupHandlers() {
        server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
            String name = request.getParams().getName();
            Map<String, Object> args = request.getParams().getArguments();
            
            if ("long_running_analysis".equals(name)) {
                // 建立任務
                Task task = taskManager.createTask("analysis");
                
                // 背景執行
                taskManager.runTask(task.getId(), () -> {
                    int totalSteps = 10;
                    for (int i = 0; i < totalSteps; i++) {
                        Thread.sleep(1000);  // 模擬工作
                        taskManager.updateProgress(task.getId(), (i + 1.0) / totalSteps);
                    }
                    return Map.of("result", "Analysis completed", "items_processed", 100);
                }, null);
                
                return CallToolResult.text("任務已啟動，任務 ID：" + task.getId());
                
            } else if ("get_task_status".equals(name)) {
                String taskId = (String) args.get("task_id");
                Optional<Task> taskOpt = taskManager.getTask(taskId);
                
                if (taskOpt.isEmpty()) {
                    return CallToolResult.text("任務不存在");
                }
                
                Task task = taskOpt.get();
                StringBuilder output = new StringBuilder();
                output.append("任務狀態：").append(task.getId()).append("\n");
                output.append("狀態：").append(task.getStatus().getValue()).append("\n");
                output.append("進度：").append(String.format("%.1f%%", task.getProgress() * 100)).append("\n");
                
                if (task.getStatus() == TaskStatus.COMPLETED) {
                    output.append("結果：").append(task.getResult()).append("\n");
                } else if (task.getStatus() == TaskStatus.FAILED) {
                    output.append("錯誤：").append(task.getError()).append("\n");
                }
                
                return CallToolResult.text(output.toString());
            }
            
            return CallToolResult.error("未知工具：" + name);
        }));
    }
}
```

---

### 7.2 自訂傳輸層

#### 7.2.1 何時需要自訂傳輸層

- WebSocket 通訊
- 自訂加密通道
- 特殊網路環境
- 效能優化需求

#### 7.2.2 實作指南

```java
/**
 * 自訂傳輸層範例：WebSocket Transport
 */
package com.example.mcp.transport;

import com.google.gson.*;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

import java.net.URI;
import java.util.*;
import java.util.concurrent.*;

/**
 * WebSocket 傳輸層
 */
public class WebSocketTransport extends WebSocketClient {
    
    private final BlockingQueue<Map<String, Object>> messageQueue;
    private final Gson gson;
    
    public WebSocketTransport(URI serverUri) {
        super(serverUri);
        this.messageQueue = new LinkedBlockingQueue<>();
        this.gson = new Gson();
    }
    
    @Override
    public void onOpen(ServerHandshake handshake) {
        System.out.println("WebSocket 連接已建立");
    }
    
    @Override
    public void onMessage(String message) {
        try {
            @SuppressWarnings("unchecked")
            Map<String, Object> data = gson.fromJson(message, Map.class);
            messageQueue.put(data);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    @Override
    public void onClose(int code, String reason, boolean remote) {
        System.out.println("WebSocket 連接已關閉：" + reason);
    }
    
    @Override
    public void onError(Exception ex) {
        ex.printStackTrace();
    }
    
    /**
     * 發送訊息
     */
    public void sendMessage(Map<String, Object> message) {
        send(gson.toJson(message));
    }
    
    /**
     * 接收訊息
     */
    public Map<String, Object> receiveMessage() throws InterruptedException {
        return messageQueue.take();
    }
    
    /**
     * 接收訊息（帶超時）
     */
    public Map<String, Object> receiveMessage(long timeout, TimeUnit unit) throws InterruptedException {
        return messageQueue.poll(timeout, unit);
    }
}

/**
 * 使用 WebSocket 的 MCP Client
 */
public class WebSocketMcpClient implements AutoCloseable {
    
    private final WebSocketTransport transport;
    private final AtomicInteger requestId;
    private final ConcurrentHashMap<Integer, CompletableFuture<Map<String, Object>>> pendingRequests;
    private final ExecutorService executor;
    
    public WebSocketMcpClient(String uri) throws Exception {
        this.transport = new WebSocketTransport(new URI(uri));
        this.requestId = new AtomicInteger(0);
        this.pendingRequests = new ConcurrentHashMap<>();
        this.executor = Executors.newSingleThreadExecutor();
    }
    
    /**
     * 連接到伺服器
     */
    public CompletableFuture<Void> connect() {
        return CompletableFuture.runAsync(() -> {
            try {
                transport.connectBlocking();
                startResponseHandler();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new CompletionException(e);
            }
        });
    }
    
    /**
     * 啟動回應處理器
     */
    private void startResponseHandler() {
        executor.submit(() -> {
            while (!Thread.currentThread().isInterrupted()) {
                try {
                    Map<String, Object> message = transport.receiveMessage();
                    handleMessage(message);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
    }
    
    /**
     * 處理訊息
     */
    @SuppressWarnings("unchecked")
    private void handleMessage(Map<String, Object> message) {
        if (message.containsKey("id")) {
            // 這是對請求的回應
            int id = ((Number) message.get("id")).intValue();
            CompletableFuture<Map<String, Object>> future = pendingRequests.remove(id);
            if (future != null) {
                future.complete(message);
            }
        } else {
            // 這是通知
            handleNotification(message);
        }
    }
    
    /**
     * 處理通知
     */
    private void handleNotification(Map<String, Object> notification) {
        System.out.println("收到通知：" + notification);
    }
    
    /**
     * 發送請求
     */
    public CompletableFuture<Map<String, Object>> request(String method, Map<String, Object> params) {
        int id = requestId.incrementAndGet();
        
        Map<String, Object> message = new LinkedHashMap<>();
        message.put("jsonrpc", "2.0");
        message.put("id", id);
        message.put("method", method);
        if (params != null) {
            message.put("params", params);
        }
        
        CompletableFuture<Map<String, Object>> future = new CompletableFuture<>();
        pendingRequests.put(id, future);
        
        transport.sendMessage(message);
        
        return future.thenApply(response -> {
            if (response.containsKey("error")) {
                @SuppressWarnings("unchecked")
                Map<String, Object> error = (Map<String, Object>) response.get("error");
                throw new CompletionException(new RuntimeException((String) error.get("message")));
            }
            return response.get("result");
        }).thenApply(result -> {
            @SuppressWarnings("unchecked")
            Map<String, Object> resultMap = (Map<String, Object>) result;
            return resultMap;
        });
    }
    
    @Override
    public void close() {
        executor.shutdown();
        transport.close();
    }
}
```

---

### 7.3 多語言 SDK 比較

| 特性 | Java SDK | Python SDK | TypeScript SDK |
|------|---------|-----------|----------------|
| **成熟度** | 穩定 | 穩定 | 穩定 |
| **非同步支援** | CompletableFuture | asyncio | Promise/async-await |
| **型別系統** | 強型別 | 選用（typing） | 內建 |
| **套件管理** | Maven/Gradle | pip/uv | npm/pnpm |
| **適用場景** | 企業應用、微服務 | 資料處理、ML | Web 應用、前端整合 |

**Java 特點**：
```java
// Handler 註冊風格
server.setToolListHandler(request -> CompletableFuture.supplyAsync(() -> {
    return ListToolsResult.builder()
        .tools(List.of(...))
        .build();
}));

server.setToolHandler(request -> CompletableFuture.supplyAsync(() -> {
    return handleToolCall(request.getParams().getName(), request.getParams().getArguments());
}));
```

**Python 特點**：
```python
# 裝飾器風格的 Handler 註冊
@server.list_tools()
async def list_tools():
    ...

@server.call_tool()
async def call_tool(name, arguments):
    ...
```

**TypeScript 特點**：
```typescript
// Schema 驗證風格
server.setRequestHandler(ListToolsRequestSchema, async () => {
  ...
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  ...
});
```

---

### 7.4 偵錯與監控

#### 7.4.1 日誌記錄最佳實踐

```java
/**
 * 日誌記錄最佳實踐
 */
package com.example.mcp.logging;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.PrintStream;
import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.logging.*;

/**
 * 結構化日誌格式器
 */
public class StructuredFormatter extends Formatter {
    
    private final Gson gson = new GsonBuilder().create();
    
    @Override
    public String format(LogRecord record) {
        Map<String, Object> logData = new LinkedHashMap<>();
        logData.put("timestamp", Instant.now().toString());
        logData.put("level", record.getLevel().getName());
        logData.put("logger", record.getLoggerName());
        logData.put("message", record.getMessage());
        
        // 添加額外資訊（透過 MDC 或參數傳遞）
        Object[] params = record.getParameters();
        if (params != null && params.length > 0) {
            if (params[0] instanceof Map) {
                @SuppressWarnings("unchecked")
                Map<String, Object> extra = (Map<String, Object>) params[0];
                logData.putAll(extra);
            }
        }
        
        return gson.toJson(logData) + System.lineSeparator();
    }
}

/**
 * MCP Server 日誌工具
 */
public class McpLogger {
    
    private static final Logger logger;
    
    static {
        // MCP Server 日誌應該輸出到 stderr
        logger = Logger.getLogger("mcp_server");
        logger.setUseParentHandlers(false);
        
        StreamHandler handler = new StreamHandler(System.err, new StructuredFormatter()) {
            @Override
            public synchronized void publish(LogRecord record) {
                super.publish(record);
                flush();
            }
        };
        handler.setLevel(Level.INFO);
        logger.addHandler(handler);
        logger.setLevel(Level.INFO);
    }
    
    public static Logger getLogger() {
        return logger;
    }
    
    /**
     * 記錄工具呼叫
     */
    public static void logToolCall(String toolName, double durationMs, boolean success) {
        Map<String, Object> extra = new LinkedHashMap<>();
        extra.put("tool_name", toolName);
        extra.put("duration_ms", durationMs);
        
        if (success) {
            logger.log(Level.INFO, "工具呼叫成功", new Object[]{extra});
        } else {
            logger.log(Level.SEVERE, "工具呼叫失敗", new Object[]{extra});
        }
    }
}
```

#### 7.4.2 效能監控

```java
/**
 * 效能監控
 */
package com.example.mcp.monitoring;

import java.time.Instant;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.function.Supplier;
import java.util.stream.Collectors;

/**
 * 指標點
 */
record MetricPoint(long timestamp, double value) {}

/**
 * 指標收集器
 */
public class Metrics {
    
    private final int retentionSeconds;
    private final ConcurrentMap<String, AtomicLong> counters;
    private final ConcurrentMap<String, CopyOnWriteArrayList<MetricPoint>> timings;
    private final ConcurrentMap<String, AtomicReference<Double>> gauges;
    private final ScheduledExecutorService cleaner;
    
    public Metrics(int retentionSeconds) {
        this.retentionSeconds = retentionSeconds;
        this.counters = new ConcurrentHashMap<>();
        this.timings = new ConcurrentHashMap<>();
        this.gauges = new ConcurrentHashMap<>();
        
        // 定期清理舊資料
        this.cleaner = Executors.newSingleThreadScheduledExecutor();
        this.cleaner.scheduleAtFixedRate(
            this::cleanupOldData, 
            60, 60, TimeUnit.SECONDS
        );
    }
    
    public Metrics() {
        this(3600);  // 預設保留 1 小時
    }
    
    /**
     * 增加計數器
     */
    public void increment(String name, long value) {
        counters.computeIfAbsent(name, k -> new AtomicLong(0)).addAndGet(value);
    }
    
    public void increment(String name) {
        increment(name, 1);
    }
    
    /**
     * 記錄時間
     */
    public void timing(String name, double durationMs) {
        timings.computeIfAbsent(name, k -> new CopyOnWriteArrayList<>())
            .add(new MetricPoint(System.currentTimeMillis(), durationMs));
    }
    
    /**
     * 設定量規
     */
    public void gauge(String name, double value) {
        gauges.computeIfAbsent(name, k -> new AtomicReference<>(0.0)).set(value);
    }
    
    /**
     * 清理舊資料
     */
    private void cleanupOldData() {
        long cutoff = System.currentTimeMillis() - (retentionSeconds * 1000L);
        
        timings.forEach((name, points) -> {
            points.removeIf(p -> p.timestamp() < cutoff);
        });
    }
    
    /**
     * 取得統計資訊
     */
    public Map<String, Object> getStats(String name) {
        List<MetricPoint> points = timings.getOrDefault(name, new CopyOnWriteArrayList<>());
        
        if (points.isEmpty()) {
            return Map.of("count", 0);
        }
        
        List<Double> values = points.stream()
            .map(MetricPoint::value)
            .sorted()
            .collect(Collectors.toList());
        
        Map<String, Object> stats = new LinkedHashMap<>();
        stats.put("count", values.size());
        stats.put("min", values.get(0));
        stats.put("max", values.get(values.size() - 1));
        stats.put("avg", values.stream().mapToDouble(d -> d).average().orElse(0));
        
        if (values.size() >= 20) {
            int p95Index = (int) (values.size() * 0.95);
            stats.put("p95", values.get(p95Index));
        }
        
        return stats;
    }
    
    public void shutdown() {
        cleaner.shutdown();
    }
}

// 全域指標收集器
class MetricsHolder {
    static final Metrics INSTANCE = new Metrics();
}

/**
 * 時間測量包裝器
 */
public class MeasuredExecutor {
    
    private final String metricName;
    private final Metrics metrics;
    
    public MeasuredExecutor(String metricName, Metrics metrics) {
        this.metricName = metricName;
        this.metrics = metrics;
    }
    
    public MeasuredExecutor(String metricName) {
        this(metricName, MetricsHolder.INSTANCE);
    }
    
    /**
     * 測量並執行
     */
    public <T> CompletableFuture<T> measureAsync(Supplier<CompletableFuture<T>> task) {
        long start = System.nanoTime();
        
        return task.get()
            .whenComplete((result, error) -> {
                double durationMs = (System.nanoTime() - start) / 1_000_000.0;
                metrics.timing(metricName + "_duration", durationMs);
                
                if (error != null) {
                    metrics.increment(metricName + "_error");
                } else {
                    metrics.increment(metricName + "_success");
                }
            });
    }
    
    /**
     * 測量同步操作
     */
    public <T> T measure(Supplier<T> task) {
        long start = System.nanoTime();
        
        try {
            T result = task.get();
            metrics.increment(metricName + "_success");
            return result;
        } catch (Exception e) {
            metrics.increment(metricName + "_error");
            throw e;
        } finally {
            double durationMs = (System.nanoTime() - start) / 1_000_000.0;
            metrics.timing(metricName + "_duration", durationMs);
        }
    }
}

// 使用範例
class ToolHandler {
    private final MeasuredExecutor readFileMetrics = new MeasuredExecutor("tool_read_file");
    
    public CompletableFuture<String> handleReadFile(Map<String, Object> args) {
        return readFileMetrics.measureAsync(() -> 
            CompletableFuture.supplyAsync(() -> {
                // 實際處理邏輯
                return "file content";
            })
        );
    }
}
```

---

*（第七章完結，繼續第八章）*

---

## 第八章：疑難排解

### 8.1 常見錯誤與解決方案

#### 8.1.1 連接問題

| 錯誤訊息 | 可能原因 | 解決方案 |
|---------|---------|---------|
| `Connection refused` | Server 未啟動 | 確認 Server 正在運行 |
| `Timeout waiting for response` | Server 處理過慢 | 增加超時時間或優化 Server |
| `Protocol version mismatch` | 版本不相容 | 更新 SDK 到相容版本 |
| `Transport error` | STDIO 管道問題 | 檢查 stdout/stderr 使用 |

**STDIO 連接問題診斷**：

```java
/**
 * STDIO 連接診斷工具
 */
package com.example.mcp.diagnostic;

import java.io.*;
import java.util.logging.*;

public class StdioDiagnostic {
    
    // 確保日誌輸出到 stderr，不干擾 STDIO 通訊
    private static final Logger logger;
    
    static {
        logger = Logger.getLogger(StdioDiagnostic.class.getName());
        logger.setUseParentHandlers(false);
        
        ConsoleHandler handler = new ConsoleHandler() {
            @Override
            protected void setOutputStream(OutputStream out) throws SecurityException {
                super.setOutputStream(System.err);  // 重要！
            }
        };
        handler.setFormatter(new SimpleFormatter());
        logger.addHandler(handler);
        logger.setLevel(Level.ALL);
    }
    
    public static void diagnoseStdio() {
        // 1. 檢查 stdin 是否可讀
        logger.info("檢查 stdin...");
        if (System.console() != null) {
            logger.warning("stdin 是終端機，可能不適合 STDIO 傳輸");
        }
        
        // 2. 檢查 stdout 是否可寫
        logger.info("檢查 stdout...");
        
        // 3. 測試寫入
        try {
            String testMessage = "{\"test\": \"message\"}\n";
            System.out.write(testMessage.getBytes());
            System.out.flush();
            logger.info("stdout 寫入測試成功");
        } catch (IOException e) {
            logger.severe("stdout 寫入失敗：" + e.getMessage());
        }
        
        // 4. 檢查環境變數
        logger.info("JAVA_HOME: " + System.getenv("JAVA_HOME"));
        String path = System.getenv("PATH");
        logger.info("PATH: " + (path != null ? path.substring(0, Math.min(100, path.length())) + "..." : "not set"));
    }
    
    public static void main(String[] args) {
        diagnoseStdio();
    }
}
```

#### 8.1.2 工具執行錯誤

**錯誤模式與處理**：

```java
/**
 * 錯誤模式分析
 */
package com.example.mcp.error;

import io.modelcontextprotocol.server.*;
import io.modelcontextprotocol.spec.McpSchema.*;

import java.util.*;
import java.util.concurrent.*;
import java.util.function.Function;

/**
 * 工具錯誤處理
 */
public class ToolErrorHandling {
    
    /**
     * 1. 參數錯誤處理
     */
    public static CallToolResult validateAndCallTool(
            String name, 
            Map<String, Object> arguments,
            Function<Map<String, Object>, CallToolResult> toolHandler) {
        
        try {
            // 驗證參數
            if ("read_file".equals(name)) {
                Object path = arguments.get("path");
                
                if (path == null) {
                    return CallToolResult.error(
                        "錯誤：缺少必要參數 'path'\n" +
                        "請使用：read_file(path='/path/to/file')"
                    );
                }
                
                // 類型檢查
                if (!(path instanceof String)) {
                    return CallToolResult.error(
                        String.format("錯誤：參數 'path' 類型錯誤%n預期：String，收到：%s",
                            path.getClass().getSimpleName())
                    );
                }
            }
            
            // 呼叫工具
            return toolHandler.apply(arguments);
            
        } catch (IllegalArgumentException e) {
            return CallToolResult.error("參數錯誤：" + e.getMessage());
        } catch (ClassCastException e) {
            return CallToolResult.error("類型錯誤：" + e.getMessage());
        }
    }
    
    /**
     * 2. 資源錯誤
     */
    public static class ResourceException extends RuntimeException {
        private final String resourceType;
        
        public ResourceException(String message, String resourceType) {
            super(message);
            this.resourceType = resourceType;
        }
        
        public String getResourceType() { return resourceType; }
    }
    
    /**
     * 資源錯誤處理包裝器
     */
    public static CallToolResult handleResourceErrors(
            java.util.function.Supplier<CallToolResult> operation) {
        
        try {
            return operation.get();
            
        } catch (java.nio.file.NoSuchFileException e) {
            return CallToolResult.error(
                String.format("❌ 檔案未找到：%s%n請確認路徑是否正確", e.getFile())
            );
        } catch (java.nio.file.AccessDeniedException e) {
            return CallToolResult.error(
                String.format("❌ 權限被拒絕：%s%n請檢查檔案權限或允許的目錄設定", e.getFile())
            );
        } catch (java.net.ConnectException e) {
            return CallToolResult.error(
                String.format("❌ 連接錯誤：%s%n請檢查網路連接或服務狀態", e.getMessage())
            );
        }
    }
}
```

#### 8.1.3 記憶體與效能問題

```java
/**
 * 效能問題診斷
 */
package com.example.mcp.diagnostic;

import java.lang.management.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.Supplier;
import java.util.logging.*;

/**
 * 記憶體監控工具
 */
public class MemoryMonitor {
    
    private static final Logger logger = Logger.getLogger(MemoryMonitor.class.getName());
    private static final MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();
    
    /**
     * 取得記憶體快照
     */
    public static void memorySnapshot() {
        MemoryUsage heapUsage = memoryBean.getHeapMemoryUsage();
        MemoryUsage nonHeapUsage = memoryBean.getNonHeapMemoryUsage();
        
        System.err.println("記憶體使用狀況：");
        System.err.printf("  Heap: 使用 %d MB / 最大 %d MB%n",
            heapUsage.getUsed() / (1024 * 1024),
            heapUsage.getMax() / (1024 * 1024));
        System.err.printf("  Non-Heap: 使用 %d MB%n",
            nonHeapUsage.getUsed() / (1024 * 1024));
        
        // 執行緒資訊
        ThreadMXBean threadBean = ManagementFactory.getThreadMXBean();
        System.err.printf("  執行緒數：%d%n", threadBean.getThreadCount());
    }
}

/**
 * 慢操作偵測
 */
public class SlowOperationDetector {
    
    private static final Logger logger = Logger.getLogger(SlowOperationDetector.class.getName());
    private final double thresholdSeconds;
    
    public SlowOperationDetector(double thresholdSeconds) {
        this.thresholdSeconds = thresholdSeconds;
    }
    
    public SlowOperationDetector() {
        this(5.0);
    }
    
    /**
     * 偵測慢操作
     */
    public <T> CompletableFuture<T> detectSlow(
            String operationName, 
            Supplier<CompletableFuture<T>> operation) {
        
        long start = System.nanoTime();
        
        return operation.get()
            .whenComplete((result, error) -> {
                double duration = (System.nanoTime() - start) / 1_000_000_000.0;
                if (duration > thresholdSeconds) {
                    logger.warning(String.format(
                        "慢操作偵測：%s 耗時 %.2f 秒",
                        operationName, duration));
                }
            });
    }
    
    /**
     * 同步版本
     */
    public <T> T detectSlowSync(String operationName, Supplier<T> operation) {
        long start = System.nanoTime();
        
        try {
            return operation.get();
        } finally {
            double duration = (System.nanoTime() - start) / 1_000_000_000.0;
            if (duration > thresholdSeconds) {
                logger.warning(String.format(
                    "慢操作偵測：%s 耗時 %.2f 秒",
                    operationName, duration));
            }
        }
    }
}

/**
 * 連接池監控
 */
public class PoolMonitor<T> {
    
    private final int maxSize;
    private final java.util.concurrent.BlockingQueue<T> pool;
    private final java.util.concurrent.atomic.AtomicInteger inUse;
    
    public PoolMonitor(BlockingQueue<T> pool, int maxSize) {
        this.pool = pool;
        this.maxSize = maxSize;
        this.inUse = new java.util.concurrent.atomic.AtomicInteger(0);
    }
    
    public Map<String, Object> getStats() {
        int available = pool.size();
        int used = inUse.get();
        
        Map<String, Object> stats = new LinkedHashMap<>();
        stats.put("available", available);
        stats.put("in_use", used);
        stats.put("max_size", maxSize);
        return stats;
    }
    
    public record HealthCheckResult(boolean healthy, String message) {}
    
    public HealthCheckResult checkHealth() {
        Map<String, Object> stats = getStats();
        
        int used = (int) stats.get("in_use");
        double usageRatio = (double) used / maxSize;
        
        if (usageRatio > 0.9) {
            return new HealthCheckResult(false, "連接池使用率過高 (>90%)");
        }
        
        if ((int) stats.get("available") == 0) {
            return new HealthCheckResult(false, "沒有可用連接");
        }
        
        return new HealthCheckResult(true, "正常");
    }
}
```

---

### 8.2 除錯技巧

#### 8.2.1 MCP Inspector 使用

```bash
# 基本使用
npx @modelcontextprotocol/inspector python -m my_server

# 帶環境變數
npx @modelcontextprotocol/inspector \
    -e MCP_ALLOWED_DIRS=/path/to/allowed \
    -e DEBUG=true \
    python -m my_server

# 連接到 HTTP Server
npx @modelcontextprotocol/inspector --url http://localhost:8080/mcp
```

**Inspector 功能**：

1. **工具檢視**：查看所有可用工具及其 Schema
2. **手動執行**：直接呼叫工具並查看結果
3. **訊息監控**：檢視原始 JSON-RPC 訊息
4. **日誌查看**：即時查看 Server 日誌

#### 8.2.2 日誌分析

```java
/**
 * 日誌分析工具
 */
package com.example.mcp.diagnostic;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;

public class LogAnalyzer {
    
    private final Gson gson = new Gson();
    
    public record LogStats(
        int totalRequests,
        int errors,
        Map<String, Integer> toolCalls,
        List<Double> durations,
        Map<String, Integer> errorTypes
    ) {
        public double getErrorRate() {
            return totalRequests > 0 ? (double) errors / totalRequests * 100 : 0;
        }
        
        public Double getAverageDuration() {
            return durations.isEmpty() ? null : 
                durations.stream().mapToDouble(d -> d).average().orElse(0);
        }
    }
    
    /**
     * 分析 MCP Server 日誌
     */
    public LogStats analyzeLogs(String logFile) throws IOException {
        int totalRequests = 0;
        int errors = 0;
        Map<String, Integer> toolCalls = new HashMap<>();
        List<Double> durations = new ArrayList<>();
        Map<String, Integer> errorTypes = new HashMap<>();
        
        try (BufferedReader reader = Files.newBufferedReader(Path.of(logFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                try {
                    Map<String, Object> entry = gson.fromJson(
                        line, 
                        new TypeToken<Map<String, Object>>(){}.getType()
                    );
                    
                    totalRequests++;
                    
                    if ("ERROR".equals(entry.get("level"))) {
                        errors++;
                        String errorType = (String) entry.getOrDefault("error_type", "unknown");
                        errorTypes.merge(errorType, 1, Integer::sum);
                    }
                    
                    if (entry.containsKey("tool_name")) {
                        String toolName = (String) entry.get("tool_name");
                        toolCalls.merge(toolName, 1, Integer::sum);
                    }
                    
                    if (entry.containsKey("duration_ms")) {
                        durations.add(((Number) entry.get("duration_ms")).doubleValue());
                    }
                    
                } catch (Exception e) {
                    // 跳過無法解析的行
                }
            }
        }
        
        return new LogStats(totalRequests, errors, toolCalls, durations, errorTypes);
    }
    
    /**
     * 列印分析報告
     */
    public void printReport(LogStats stats) {
        System.out.println("=".repeat(50));
        System.out.println("MCP Server 日誌分析報告");
        System.out.println("=".repeat(50));
        System.out.printf("總請求數：%d%n", stats.totalRequests());
        System.out.printf("錯誤數：%d%n", stats.errors());
        System.out.printf("錯誤率：%.2f%%%n", stats.getErrorRate());
        
        Double avgDuration = stats.getAverageDuration();
        System.out.printf("平均回應時間：%s ms%n", 
            avgDuration != null ? String.format("%.2f", avgDuration) : "N/A");
        
        System.out.println("\n工具呼叫統計：");
        stats.toolCalls().entrySet().stream()
            .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
            .forEach(e -> System.out.printf("  %s: %d%n", e.getKey(), e.getValue()));
        
        System.out.println("\n錯誤類型分布：");
        stats.errorTypes().forEach((type, count) -> 
            System.out.printf("  %s: %d%n", type, count));
    }
    
    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.err.println("用法：java LogAnalyzer <log-file>");
            System.exit(1);
        }
        
        LogAnalyzer analyzer = new LogAnalyzer();
        LogStats stats = analyzer.analyzeLogs(args[0]);
        analyzer.printReport(stats);
    }
}
```

#### 8.2.3 網路除錯

```java
/**
 * 網路除錯工具
 */
package com.example.mcp.diagnostic;

import okhttp3.*;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class NetworkDebugger {
    
    private final OkHttpClient client;
    
    public NetworkDebugger() {
        this.client = new OkHttpClient.Builder()
            .connectTimeout(5, TimeUnit.SECONDS)
            .readTimeout(5, TimeUnit.SECONDS)
            .build();
    }
    
    /**
     * 除錯 HTTP 連接
     */
    public void debugHttpConnection(String url) {
        System.out.println("測試連接：" + url);
        
        try {
            // 1. 基本連接測試
            Request request = new Request.Builder()
                .url(url)
                .get()
                .build();
            
            try (Response response = client.newCall(request).execute()) {
                System.out.println("✅ 連接成功");
                System.out.println("   狀態碼：" + response.code());
                System.out.println("   Headers：");
                response.headers().forEach(pair -> 
                    System.out.println("     " + pair.getFirst() + ": " + pair.getSecond()));
            }
            
            // 2. SSE 端點測試
            String sseUrl = url.contains("/mcp") ? 
                url.replace("/mcp", "/sse") : url + "/sse";
            
            try {
                Request sseRequest = new Request.Builder()
                    .url(sseUrl)
                    .get()
                    .build();
                
                try (Response sseResponse = client.newCall(sseRequest).execute()) {
                    System.out.println("✅ SSE 端點可用");
                    System.out.println("   Content-Type：" + 
                        sseResponse.header("Content-Type"));
                }
            } catch (Exception e) {
                System.out.println("⚠️ SSE 端點無法連接");
            }
            
        } catch (java.net.ConnectException e) {
            System.out.println("❌ 連接錯誤：" + e.getMessage());
        } catch (java.net.SocketTimeoutException e) {
            System.out.println("❌ 連接超時");
        } catch (Exception e) {
            System.out.println("❌ 未知錯誤：" + e.getMessage());
        }
    }
    
    /**
     * 追蹤 HTTP 請求
     */
    public void traceRequest(String method, String url, RequestBody body) throws IOException {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("請求：" + method + " " + url);
        
        long start = System.currentTimeMillis();
        
        Request.Builder requestBuilder = new Request.Builder().url(url);
        
        switch (method.toUpperCase()) {
            case "GET" -> requestBuilder.get();
            case "POST" -> requestBuilder.post(body != null ? body : RequestBody.create("", null));
            case "PUT" -> requestBuilder.put(body != null ? body : RequestBody.create("", null));
            case "DELETE" -> requestBuilder.delete(body);
            default -> throw new IllegalArgumentException("不支援的方法：" + method);
        }
        
        try (Response response = client.newCall(requestBuilder.build()).execute()) {
            long duration = System.currentTimeMillis() - start;
            
            System.out.println("\n回應：");
            System.out.println("  狀態：" + response.code());
            System.out.println("  耗時：" + duration + " ms");
            System.out.println("  Headers：");
            response.headers().forEach(pair -> 
                System.out.println("    " + pair.getFirst() + ": " + pair.getSecond()));
            
            ResponseBody responseBody = response.body();
            if (responseBody != null) {
                String bodyStr = responseBody.string();
                System.out.println("  Body：" + 
                    (bodyStr.length() > 500 ? bodyStr.substring(0, 500) + "..." : bodyStr));
            }
        }
    }
    
    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("用法：java NetworkDebugger <url>");
            System.exit(1);
        }
        
        NetworkDebugger debugger = new NetworkDebugger();
        debugger.debugHttpConnection(args[0]);
    }
}
```

---

### 8.3 錯誤訊息參考

#### 8.3.1 JSON-RPC 錯誤碼與 MCP 分區政策

**JSON-RPC 2.0 標準錯誤**：

| 錯誤碼 | 名稱 | 說明 | 解決方案 |
|-------|------|------|---------|
| -32700 | Parse error | JSON 解析錯誤 | 檢查 JSON 格式 |
| -32600 | Invalid Request | 無效的請求物件 | 檢查 `jsonrpc`、`method` 欄位 |
| -32601 | Method not found | 方法不存在 | 確認方法名稱正確；注意 `2026-07-28` 已移除多個方法 |
| -32602 | Invalid params | 參數錯誤 | 檢查參數格式、類型與必要的 `_meta` 欄位 |
| -32603 | Internal error | 內部錯誤 | 檢查 Server 日誌 |

**MCP 錯誤碼分區（`2026-07-28` 新增）**：

| 區間 | 用途 | 規則 |
|------|------|------|
| `-32000` ～ `-32019` | Legacy：既有 SDK 已配置 | **新實作 MUST NOT 於此區間配置新碼**；除 `-32002` 外不得假設語意 |
| `-32020` ～ `-32099` | 保留給 MCP 規範 | 僅規範可定義 |
| `-32768` ～ `-32000` 之外 | 應用層自訂 | 新的非規範錯誤碼 **SHOULD** 配置於此 |

**MCP 規範定義的錯誤碼**：

| 錯誤碼 | 名稱 | 觸發情境 | HTTP 狀態 |
|--------|------|----------|-----------|
| `-32020` | `HeaderMismatch` | HTTP 標頭與 Body 不符，或缺少必要標頭 | `400` |
| `-32021` | `MissingRequiredClientCapability` | 缺少處理請求所需的用戶端能力宣告 | `400` |
| `-32022` | `UnsupportedProtocolVersion` | 伺服器不支援請求宣告的協議版本 | `400` |

**已保留、不得再發出的錯誤碼**：

| 錯誤碼 | 原用途 | `2026-07-28` 處置 |
|--------|--------|------------------|
| `-32002` | 資源不存在 | **改用 `-32602`**（Invalid Params）。用戶端 **SHOULD** 仍接受舊版伺服器發出的 `-32002` |
| `-32042` | URL Elicitation 需求（`2025-11-25` 專用） | 隨該功能移除而保留，**MUST NOT** 再發出 |

**錯誤回應範例**：

```json
// 缺少必要的 _meta 欄位
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Missing required _meta field: io.modelcontextprotocol/protocolVersion"
  }
}

// 缺少必要的用戶端能力
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32021,
    "message": "Missing required client capability",
    "data": { "requiredCapabilities": ["elicitation"] }
  }
}

// 不支援的協議版本
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32022,
    "message": "Unsupported protocol version",
    "data": { "supported": ["2026-07-28", "2025-11-25"], "requested": "1900-01-01" }
  }
}
```

> **⚠️ 遷移警示**：下方 Java 範例保留自 `2025-11-25` 版本，
> 其中在 `-32000`～`-32019` 區間自訂錯誤碼的做法**已不符合 `2026-07-28` 規範**。
> 新專案請改為：使用上表的規範錯誤碼，或將自訂錯誤碼配置於 `-32768`～`-32000` 之外。
> 特別注意 `session_expired`（`-32020`）與規範的 `HeaderMismatch` 衝突，**必須重新配置**。

#### 8.3.2 MCP 特定錯誤

```java
/**
 * MCP 錯誤處理參考
 */
package com.example.mcp.error;

import java.util.*;

/**
 * MCP 錯誤定義
 */
public class McpErrors {
    
    public record ErrorDefinition(
        int code,
        String message,
        String solution
    ) {}
    
    // 資源相關錯誤
    public static final Map<String, ErrorDefinition> RESOURCE_ERRORS = Map.of(
        "resource_not_found", new ErrorDefinition(
            -32001,
            "找不到指定的資源",
            "確認資源 URI 正確且資源存在"
        ),
        "resource_access_denied", new ErrorDefinition(
            -32002,
            "資源存取被拒絕",
            "檢查權限設定和允許的路徑"
        ),
        "resource_read_error", new ErrorDefinition(
            -32003,
            "資源讀取錯誤",
            "檢查檔案是否可讀取、編碼是否正確"
        )
    );
    
    // 工具相關錯誤
    public static final Map<String, ErrorDefinition> TOOL_ERRORS = Map.of(
        "tool_not_found", new ErrorDefinition(
            -32010,
            "找不到指定的工具",
            "使用 tools/list 確認可用工具"
        ),
        "tool_execution_error", new ErrorDefinition(
            -32011,
            "工具執行錯誤",
            "檢查參數和 Server 日誌"
        ),
        "tool_timeout", new ErrorDefinition(
            -32012,
            "工具執行超時",
            "增加超時時間或優化操作"
        )
    );
    
    // 連接相關錯誤
    public static final Map<String, ErrorDefinition> CONNECTION_ERRORS = Map.of(
        "session_expired", new ErrorDefinition(
            -32020,
            "Session 已過期",
            "重新初始化連接"
        ),
        "rate_limited", new ErrorDefinition(
            -32021,
            "請求過於頻繁",
            "減少請求頻率或等待配額重置"
        )
    );
    
    /**
     * 根據錯誤碼取得錯誤定義
     */
    public static Optional<ErrorDefinition> getByCode(int code) {
        return java.util.stream.Stream.of(RESOURCE_ERRORS, TOOL_ERRORS, CONNECTION_ERRORS)
            .flatMap(map -> map.values().stream())
            .filter(e -> e.code() == code)
            .findFirst();
    }
    
    /**
     * 根據名稱取得錯誤定義
     */
    public static Optional<ErrorDefinition> getByName(String name) {
        return java.util.stream.Stream.of(RESOURCE_ERRORS, TOOL_ERRORS, CONNECTION_ERRORS)
            .filter(map -> map.containsKey(name))
            .map(map -> map.get(name))
            .findFirst();
    }
}
```

---

---

## 第九章：實際案例研究

> **📌 `2026-07-28` 適用性說明**
>
> 本章案例的**需求分析、架構分層與工具切分邏輯**不受協議改版影響，
> 但若要以 `2026-07-28` 重新實作，架構上有三項重要差異：
>
> 1. **無狀態水平擴展**：因為 Session 已移除，伺服器可直接置於無黏滞的負載均衡器後，
>    不再需要 sticky session 或共用 Session 存放區。參見
>    [13.1 無狀態水平擴展架構](#131-無狀態水平擴展架構)。
> 2. **長時作業改用 Tasks 擴充**：案例中的非同步作業（建置、部署、批次索引）
>    應採官方 `io.modelcontextprotocol/tasks` 而非自行輪詢。參見
>    [12.3 Tasks 擴充深入解析](#123-tasks-擴充深入解析)。
> 3. **人工確認改用 MRTR**：需要使用者授權的高風險操作（如正式環境部署）
>    應回傳 `resultType: "input_required"` 而非自定的確認協定。參見
>    [2.5 多輪往返請求（Multi-Round-Trip Requests, MRTR）](#25-多輪往返請求multi-round-trip-requests-mrtr)。

### 9.1 案例一：企業知識庫 MCP Server

#### 9.1.1 需求背景

- **場景**：企業內部有大量文件、Wiki、FAQ 資料
- **目標**：讓 AI 助手能搜尋和引用內部知識
- **挑戰**：資料分散、權限控制、即時更新

#### 9.1.2 架構設計

```mermaid
graph TB
    subgraph "AI 層"
        Claude[Claude/AI 助手]
    end
    
    subgraph "MCP 層"
        KBServer[Knowledge Base<br/>MCP Server]
    end
    
    subgraph "資料層"
        ES[(Elasticsearch)]
        Wiki[(Confluence)]
        SharePoint[(SharePoint)]
    end
    
    subgraph "認證層"
        LDAP[LDAP/AD]
        OAuth[OAuth 2.0]
    end
    
    Claude --> KBServer
    KBServer --> ES
    KBServer --> Wiki
    KBServer --> SharePoint
    KBServer --> LDAP
    KBServer --> OAuth
```

#### 9.1.3 核心實作

```java
/**
 * 企業知識庫 MCP Server
 */
package com.example.mcp.kb;

import co.elastic.clients.elasticsearch.ElasticsearchAsyncClient;
import co.elastic.clients.elasticsearch._types.query_dsl.*;
import co.elastic.clients.elasticsearch.core.*;
import co.elastic.clients.elasticsearch.core.search.*;
import co.elastic.clients.json.jackson.JacksonJsonpMapper;
import co.elastic.clients.transport.rest_client.RestClientTransport;
import io.modelcontextprotocol.server.*;
import io.modelcontextprotocol.spec.McpSchema.*;
import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;

import java.util.*;
import java.util.concurrent.*;

public class KnowledgeBaseMcpServer {
    
    // 配置
    private static final String ES_HOST = "elasticsearch";
    private static final int ES_PORT = 9200;
    private static final String WIKI_URL = "http://confluence.internal";
    
    private final McpServer server;
    private final ElasticsearchAsyncClient esClient;
    
    public KnowledgeBaseMcpServer() {
        this.server = McpServer.builder()
            .name("knowledge-base")
            .version("1.0.0")
            .build();
        
        // 初始化 Elasticsearch 客戶端
        RestClient restClient = RestClient.builder(
            new HttpHost(ES_HOST, ES_PORT)
        ).build();
        
        this.esClient = new ElasticsearchAsyncClient(
            new RestClientTransport(restClient, new JacksonJsonpMapper())
        );
        
        setupHandlers();
    }
    
    private void setupHandlers() {
        // 工具列表
        server.setToolListHandler(request -> CompletableFuture.supplyAsync(() -> {
            List<Tool> tools = List.of(
                Tool.builder()
                    .name("search_knowledge")
                    .description("搜尋企業知識庫，包含文件、Wiki、FAQ")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "query", Map.of(
                                "type", "string",
                                "description", "搜尋關鍵字或問題"
                            ),
                            "sources", Map.of(
                                "type", "array",
                                "items", Map.of(
                                    "type", "string",
                                    "enum", List.of("documents", "wiki", "faq", "all")
                                ),
                                "default", List.of("all"),
                                "description", "搜尋來源"
                            ),
                            "department", Map.of(
                                "type", "string",
                                "description", "限制特定部門的文件"
                            ),
                            "date_from", Map.of(
                                "type", "string",
                                "format", "date",
                                "description", "起始日期過濾"
                            ),
                            "max_results", Map.of(
                                "type", "integer",
                                "default", 10,
                                "maximum", 50
                            )
                        ),
                        "required", List.of("query")
                    ))
                    .build(),
                    
                Tool.builder()
                    .name("get_document")
                    .description("取得特定文件的完整內容")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "doc_id", Map.of(
                                "type", "string",
                                "description", "文件 ID"
                            ),
                            "include_metadata", Map.of(
                                "type", "boolean",
                                "default", true
                            )
                        ),
                        "required", List.of("doc_id")
                    ))
                    .build(),
                    
                Tool.builder()
                    .name("ask_faq")
                    .description("從 FAQ 中找尋最相關的問答")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "question", Map.of(
                                "type", "string",
                                "description", "用戶問題"
                            ),
                            "category", Map.of(
                                "type", "string",
                                "enum", List.of("hr", "it", "finance", "general")
                            )
                        ),
                        "required", List.of("question")
                    ))
                    .build()
            );
            
            return ListToolsResult.builder().tools(tools).build();
        }));
        
        // 工具呼叫處理
        server.setToolHandler(request -> {
            String name = request.getParams().getName();
            Map<String, Object> args = request.getParams().getArguments();
            
            return switch (name) {
                case "search_knowledge" -> searchKnowledge(args);
                case "get_document" -> getDocument(args);
                case "ask_faq" -> askFaq(args);
                default -> CompletableFuture.completedFuture(
                    CallToolResult.error("未知工具：" + name)
                );
            };
        });
    }
    
    /**
     * 搜尋知識庫
     */
    private CompletableFuture<CallToolResult> searchKnowledge(Map<String, Object> args) {
        String query = (String) args.get("query");
        @SuppressWarnings("unchecked")
        List<String> sources = (List<String>) args.getOrDefault("sources", List.of("all"));
        String department = (String) args.get("department");
        String dateFrom = (String) args.get("date_from");
        int maxResults = ((Number) args.getOrDefault("max_results", 10)).intValue();
        
        // 構建查詢
        List<Query> mustQueries = new ArrayList<>();
        mustQueries.add(MultiMatchQuery.of(mm -> mm
            .query(query)
            .fields("title^3", "content", "tags^2")
            .type(TextQueryType.BestFields)
            .fuzziness("AUTO")
        )._toQuery());
        
        List<Query> filterQueries = new ArrayList<>();
        
        if (!sources.contains("all")) {
            filterQueries.add(TermsQuery.of(t -> t
                .field("source")
                .terms(TermsQueryField.of(tf -> tf
                    .value(sources.stream().map(FieldValue::of).toList())
                ))
            )._toQuery());
        }
        
        if (department != null) {
            filterQueries.add(TermQuery.of(t -> t
                .field("department")
                .value(department)
            )._toQuery());
        }
        
        if (dateFrom != null) {
            filterQueries.add(RangeQuery.of(r -> r
                .field("updated_at")
                .gte(co.elastic.clients.json.JsonData.of(dateFrom))
            )._toQuery());
        }
        
        BoolQuery boolQuery = BoolQuery.of(b -> b
            .must(mustQueries)
            .filter(filterQueries)
        );
        
        return esClient.search(s -> s
            .index("knowledge_base")
            .query(boolQuery._toQuery())
            .size(maxResults)
            .highlight(h -> h
                .fields("content", hf -> hf.fragmentSize(200))
            ),
            Map.class
        ).thenApply(response -> {
            List<Hit<Map>> hits = response.hits().hits();
            
            if (hits.isEmpty()) {
                return CallToolResult.text("未找到與「" + query + "」相關的內容");
            }
            
            StringBuilder output = new StringBuilder();
            output.append("## 搜尋結果：「").append(query).append("」\n\n");
            output.append("找到 ").append(response.hits().total().value())
                  .append(" 筆相關文件\n\n");
            
            int i = 1;
            for (Hit<Map> hit : hits) {
                @SuppressWarnings("unchecked")
                Map<String, Object> source = hit.source();
                
                output.append("### ").append(i++).append(". ")
                      .append(source.get("title")).append("\n");
                output.append("- **來源**：").append(source.get("source")).append("\n");
                output.append("- **部門**：")
                      .append(source.getOrDefault("department", "N/A")).append("\n");
                output.append("- **更新日期**：").append(source.get("updated_at")).append("\n");
                output.append("- **文件 ID**：`").append(hit.id()).append("`\n");
                
                Map<String, List<String>> highlight = hit.highlight();
                if (highlight != null && highlight.containsKey("content")) {
                    output.append("- **摘要**：...")
                          .append(highlight.get("content").get(0)).append("...\n");
                }
                
                output.append("\n");
            }
            
            return CallToolResult.text(output.toString());
        }).exceptionally(e -> CallToolResult.error("搜尋失敗：" + e.getMessage()));
    }
    
    /**
     * 取得文件內容
     */
    private CompletableFuture<CallToolResult> getDocument(Map<String, Object> args) {
        String docId = (String) args.get("doc_id");
        boolean includeMetadata = (Boolean) args.getOrDefault("include_metadata", true);
        
        return esClient.get(g -> g
            .index("knowledge_base")
            .id(docId),
            Map.class
        ).thenApply(response -> {
            if (!response.found()) {
                return CallToolResult.text("無法取得文件 " + docId + "：文件不存在");
            }
            
            @SuppressWarnings("unchecked")
            Map<String, Object> source = response.source();
            
            StringBuilder output = new StringBuilder();
            output.append("# ").append(source.get("title")).append("\n\n");
            
            if (includeMetadata) {
                output.append("## 文件資訊\n");
                output.append("- **作者**：")
                      .append(source.getOrDefault("author", "N/A")).append("\n");
                output.append("- **建立日期**：")
                      .append(source.getOrDefault("created_at", "N/A")).append("\n");
                output.append("- **更新日期**：")
                      .append(source.getOrDefault("updated_at", "N/A")).append("\n");
                
                @SuppressWarnings("unchecked")
                List<String> tags = (List<String>) source.getOrDefault("tags", List.of());
                output.append("- **標籤**：").append(String.join(", ", tags)).append("\n\n");
            }
            
            output.append("## 內容\n\n");
            output.append(source.getOrDefault("content", "（無內容）"));
            
            return CallToolResult.text(output.toString());
        }).exceptionally(e -> CallToolResult.error("無法取得文件 " + docId + "：" + e.getMessage()));
    }
    
    /**
     * FAQ 問答
     */
    private CompletableFuture<CallToolResult> askFaq(Map<String, Object> args) {
        String question = (String) args.get("question");
        String category = (String) args.get("category");
        
        List<Query> mustQueries = List.of(
            MultiMatchQuery.of(mm -> mm
                .query(question)
                .fields("question^2", "answer")
                .type(TextQueryType.BestFields)
            )._toQuery()
        );
        
        List<Query> filterQueries = new ArrayList<>();
        filterQueries.add(TermQuery.of(t -> t.field("type").value("faq"))._toQuery());
        
        if (category != null) {
            filterQueries.add(TermQuery.of(t -> t
                .field("category")
                .value(category)
            )._toQuery());
        }
        
        return esClient.search(s -> s
            .index("knowledge_base")
            .query(q -> q.bool(b -> b
                .must(mustQueries)
                .filter(filterQueries)
            ))
            .size(5),
            Map.class
        ).thenApply(response -> {
            List<Hit<Map>> hits = response.hits().hits();
            
            if (hits.isEmpty()) {
                return CallToolResult.text("FAQ 中沒有找到與「" + question + "」相關的問答");
            }
            
            // 取最相關的答案
            Hit<Map> bestHit = hits.get(0);
            @SuppressWarnings("unchecked")
            Map<String, Object> bestMatch = bestHit.source();
            double score = bestHit.score();
            
            StringBuilder output = new StringBuilder();
            output.append("## FAQ 回答\n\n");
            output.append("**問題**：").append(bestMatch.get("question")).append("\n\n");
            output.append("**答案**：").append(bestMatch.get("answer")).append("\n\n");
            output.append("**分類**：")
                  .append(bestMatch.getOrDefault("category", "general")).append("\n");
            output.append("**相關度**：").append(String.format("%.2f", score)).append("\n\n");
            
            if (hits.size() > 1) {
                output.append("### 其他相關問題\n");
                for (int i = 1; i < Math.min(4, hits.size()); i++) {
                    @SuppressWarnings("unchecked")
                    Map<String, Object> otherSource = hits.get(i).source();
                    output.append("- ").append(otherSource.get("question")).append("\n");
                }
            }
            
            return CallToolResult.text(output.toString());
        }).exceptionally(e -> CallToolResult.error("FAQ 查詢失敗：" + e.getMessage()));
    }
}
```

---

### 9.2 案例二：DevOps 整合 MCP Server

#### 9.2.1 需求背景

- **場景**：開發團隊需要 AI 協助管理 CI/CD、監控、部署
- **目標**：透過對話式介面操作 DevOps 工具鏈
- **整合工具**：Jenkins、Kubernetes、Prometheus、GitLab

#### 9.2.2 架構設計

```mermaid
graph LR
    subgraph "AI 助手"
        Claude[Claude]
    end
    
    subgraph "DevOps MCP"
        DevServer[DevOps Server]
        
        subgraph "工具集"
            CI[CI/CD 工具]
            K8s[K8s 工具]
            Monitor[監控工具]
        end
    end
    
    subgraph "基礎設施"
        Jenkins[Jenkins]
        Kubernetes[Kubernetes]
        Prometheus[Prometheus]
        GitLab[GitLab]
    end
    
    Claude --> DevServer
    DevServer --> CI
    DevServer --> K8s
    DevServer --> Monitor
    
    CI --> Jenkins
    CI --> GitLab
    K8s --> Kubernetes
    Monitor --> Prometheus
```

#### 9.2.3 核心工具

```java
/**
 * DevOps MCP Server
 */
package com.example.mcp.devops;

import io.kubernetes.client.openapi.*;
import io.kubernetes.client.openapi.apis.*;
import io.kubernetes.client.openapi.models.*;
import io.kubernetes.client.util.Config;
import io.modelcontextprotocol.server.*;
import io.modelcontextprotocol.spec.McpSchema.*;
import okhttp3.*;

import java.io.IOException;
import java.time.*;
import java.util.*;
import java.util.concurrent.*;

public class DevOpsMcpServer {
    
    // 配置
    private static final String JENKINS_URL = "http://jenkins.internal";
    private static final String PROMETHEUS_URL = "http://prometheus.internal:9090";
    
    private final McpServer server;
    private final CoreV1Api k8sCoreApi;
    private final AppsV1Api k8sAppsApi;
    private final OkHttpClient httpClient;
    
    public DevOpsMcpServer() throws IOException {
        this.server = McpServer.builder()
            .name("devops")
            .version("1.0.0")
            .build();
        
        // 載入 K8s 配置
        ApiClient k8sClient;
        try {
            k8sClient = Config.fromCluster();
        } catch (Exception e) {
            k8sClient = Config.defaultClient();
        }
        Configuration.setDefaultApiClient(k8sClient);
        
        this.k8sCoreApi = new CoreV1Api();
        this.k8sAppsApi = new AppsV1Api();
        this.httpClient = new OkHttpClient();
        
        setupHandlers();
    }
    
    private void setupHandlers() {
        // 工具列表
        server.setToolListHandler(request -> CompletableFuture.supplyAsync(() -> {
            List<Tool> tools = List.of(
                // CI/CD 工具
                Tool.builder()
                    .name("trigger_pipeline")
                    .description("觸發 CI/CD Pipeline")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "project", Map.of("type", "string", "description", "專案名稱"),
                            "branch", Map.of("type", "string", "default", "main"),
                            "parameters", Map.of("type", "object", "description", "Pipeline 參數")
                        ),
                        "required", List.of("project")
                    ))
                    .build(),
                    
                Tool.builder()
                    .name("get_pipeline_status")
                    .description("取得 Pipeline 執行狀態")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "project", Map.of("type", "string"),
                            "build_number", Map.of("type", "integer")
                        ),
                        "required", List.of("project")
                    ))
                    .build(),
                    
                // Kubernetes 工具
                Tool.builder()
                    .name("list_pods")
                    .description("列出 Kubernetes Pods")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "namespace", Map.of("type", "string", "default", "default"),
                            "label_selector", Map.of("type", "string"),
                            "status", Map.of(
                                "type", "string",
                                "enum", List.of("all", "running", "pending", "failed")
                            )
                        )
                    ))
                    .build(),
                    
                Tool.builder()
                    .name("scale_deployment")
                    .description("調整 Deployment 副本數")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "name", Map.of("type", "string", "description", "Deployment 名稱"),
                            "namespace", Map.of("type", "string", "default", "default"),
                            "replicas", Map.of("type", "integer", "minimum", 0, "maximum", 50)
                        ),
                        "required", List.of("name", "replicas")
                    ))
                    .build(),
                    
                Tool.builder()
                    .name("get_pod_logs")
                    .description("取得 Pod 日誌")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "pod_name", Map.of("type", "string"),
                            "namespace", Map.of("type", "string", "default", "default"),
                            "container", Map.of("type", "string"),
                            "tail_lines", Map.of("type", "integer", "default", 100)
                        ),
                        "required", List.of("pod_name")
                    ))
                    .build(),
                    
                // 監控工具
                Tool.builder()
                    .name("query_metrics")
                    .description("查詢 Prometheus 指標")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "query", Map.of("type", "string", "description", "PromQL 查詢"),
                            "time_range", Map.of(
                                "type", "string",
                                "enum", List.of("5m", "15m", "1h", "6h", "24h"),
                                "default", "15m"
                            )
                        ),
                        "required", List.of("query")
                    ))
                    .build(),
                    
                Tool.builder()
                    .name("get_service_health")
                    .description("取得服務健康狀態摘要")
                    .inputSchema(Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "service", Map.of("type", "string"),
                            "namespace", Map.of("type", "string", "default", "default")
                        ),
                        "required", List.of("service")
                    ))
                    .build()
            );
            
            return ListToolsResult.builder().tools(tools).build();
        }));
        
        // 工具呼叫處理
        server.setToolHandler(request -> {
            String name = request.getParams().getName();
            Map<String, Object> args = request.getParams().getArguments();
            
            return switch (name) {
                case "trigger_pipeline" -> triggerPipeline(args);
                case "get_pipeline_status" -> getPipelineStatus(args);
                case "list_pods" -> listPods(args);
                case "scale_deployment" -> scaleDeployment(args);
                case "get_pod_logs" -> getPodLogs(args);
                case "query_metrics" -> queryMetrics(args);
                case "get_service_health" -> getServiceHealth(args);
                default -> CompletableFuture.completedFuture(
                    CallToolResult.error("未知工具：" + name)
                );
            };
        });
    }
    
    // ===== 工具實作 =====
    
    /**
     * 觸發 Pipeline
     */
    private CompletableFuture<CallToolResult> triggerPipeline(Map<String, Object> args) {
        return CompletableFuture.supplyAsync(() -> {
            String project = (String) args.get("project");
            String branch = (String) args.getOrDefault("branch", "main");
            @SuppressWarnings("unchecked")
            Map<String, String> parameters = (Map<String, String>) args.getOrDefault("parameters", Map.of());
            
            HttpUrl.Builder urlBuilder = HttpUrl.parse(JENKINS_URL + "/job/" + project + "/buildWithParameters")
                .newBuilder()
                .addQueryParameter("BRANCH", branch);
            
            parameters.forEach(urlBuilder::addQueryParameter);
            
            Request request = new Request.Builder()
                .url(urlBuilder.build())
                .post(RequestBody.create("", null))
                .build();
            
            try (Response response = httpClient.newCall(request).execute()) {
                if (response.code() == 201) {
                    String location = response.header("Location", "");
                    return CallToolResult.text(String.format(
                        "✅ Pipeline 已觸發%n專案：%s%n分支：%s%n追蹤：%s",
                        project, branch, location
                    ));
                } else {
                    return CallToolResult.error("❌ 觸發失敗：" + response.code());
                }
            } catch (IOException e) {
                return CallToolResult.error("❌ 觸發失敗：" + e.getMessage());
            }
        });
    }
    
    /**
     * 取得 Pipeline 狀態
     */
    private CompletableFuture<CallToolResult> getPipelineStatus(Map<String, Object> args) {
        // 實作類似，省略詳細程式碼
        return CompletableFuture.completedFuture(CallToolResult.text("Pipeline 狀態查詢"));
    }
    
    /**
     * 列出 Pods
     */
    private CompletableFuture<CallToolResult> listPods(Map<String, Object> args) {
        return CompletableFuture.supplyAsync(() -> {
            String namespace = (String) args.getOrDefault("namespace", "default");
            String labelSelector = (String) args.get("label_selector");
            String statusFilter = (String) args.getOrDefault("status", "all");
            
            try {
                V1PodList podList = k8sCoreApi.listNamespacedPod(
                    namespace, null, null, null, null,
                    labelSelector, null, null, null, null, null
                );
                
                StringBuilder output = new StringBuilder();
                output.append("## Pods in ").append(namespace).append("\n\n");
                output.append("| Name | Status | Restarts | Age |\n");
                output.append("|------|--------|----------|-----|\n");
                
                for (V1Pod pod : podList.getItems()) {
                    String status = pod.getStatus().getPhase();
                    
                    // 過濾狀態
                    if (!"all".equals(statusFilter)) {
                        if ("running".equals(statusFilter) && !"Running".equals(status)) continue;
                        if ("pending".equals(statusFilter) && !"Pending".equals(status)) continue;
                        if ("failed".equals(statusFilter) && 
                            !"Failed".equals(status) && !"Error".equals(status)) continue;
                    }
                    
                    // 計算重啟次數
                    int restarts = 0;
                    if (pod.getStatus().getContainerStatuses() != null) {
                        restarts = pod.getStatus().getContainerStatuses().stream()
                            .mapToInt(V1ContainerStatus::getRestartCount)
                            .sum();
                    }
                    
                    // 計算年齡
                    OffsetDateTime creationTime = pod.getMetadata().getCreationTimestamp();
                    Duration age = Duration.between(creationTime.toInstant(), Instant.now());
                    String ageStr = age.toDays() > 0 ? 
                        age.toDays() + "d" : age.toHours() + "h";
                    
                    output.append(String.format("| %s | %s | %d | %s |%n",
                        pod.getMetadata().getName(), status, restarts, ageStr));
                }
                
                return CallToolResult.text(output.toString());
                
            } catch (ApiException e) {
                return CallToolResult.error("❌ 列出 Pods 失敗：" + e.getMessage());
            }
        });
    }
    
    /**
     * 調整 Deployment 副本
     */
    private CompletableFuture<CallToolResult> scaleDeployment(Map<String, Object> args) {
        return CompletableFuture.supplyAsync(() -> {
            String name = (String) args.get("name");
            String namespace = (String) args.getOrDefault("namespace", "default");
            int replicas = ((Number) args.get("replicas")).intValue();
            
            try {
                // 取得當前狀態
                V1Deployment deployment = k8sAppsApi.readNamespacedDeployment(
                    name, namespace, null
                );
                int current = deployment.getSpec().getReplicas();
                
                // 更新副本數
                deployment.getSpec().setReplicas(replicas);
                k8sAppsApi.replaceNamespacedDeployment(name, namespace, deployment, null, null, null, null);
                
                return CallToolResult.text(String.format(
                    "✅ Deployment %s 已調整%n副本數：%d → %d",
                    name, current, replicas
                ));
                
            } catch (ApiException e) {
                return CallToolResult.error("❌ 調整失敗：" + e.getMessage());
            }
        });
    }
    
    /**
     * 取得 Pod 日誌
     */
    private CompletableFuture<CallToolResult> getPodLogs(Map<String, Object> args) {
        return CompletableFuture.supplyAsync(() -> {
            String podName = (String) args.get("pod_name");
            String namespace = (String) args.getOrDefault("namespace", "default");
            String container = (String) args.get("container");
            int tailLines = ((Number) args.getOrDefault("tail_lines", 100)).intValue();
            
            try {
                String logs = k8sCoreApi.readNamespacedPodLog(
                    podName, namespace, container, null, null, null, null,
                    null, null, tailLines, null
                );
                
                return CallToolResult.text("## Pod 日誌：" + podName + "\n\n```\n" + logs + "\n```");
                
            } catch (ApiException e) {
                return CallToolResult.error("❌ 取得日誌失敗：" + e.getMessage());
            }
        });
    }
    
    /**
     * 查詢 Prometheus 指標
     */
    private CompletableFuture<CallToolResult> queryMetrics(Map<String, Object> args) {
        return CompletableFuture.supplyAsync(() -> {
            String query = (String) args.get("query");
            String timeRange = (String) args.getOrDefault("time_range", "15m");
            
            HttpUrl url = HttpUrl.parse(PROMETHEUS_URL + "/api/v1/query_range")
                .newBuilder()
                .addQueryParameter("query", query)
                .addQueryParameter("start", "now()-" + timeRange)
                .addQueryParameter("end", "now()")
                .addQueryParameter("step", "60s")
                .build();
            
            Request request = new Request.Builder().url(url).get().build();
            
            try (Response response = httpClient.newCall(request).execute()) {
                // 解析 Prometheus 回應並格式化輸出
                String body = response.body().string();
                
                StringBuilder output = new StringBuilder();
                output.append("## 指標查詢結果\n\n");
                output.append("查詢：`").append(query).append("`\n");
                output.append("時間範圍：").append(timeRange).append("\n\n");
                output.append("回應：").append(body.substring(0, Math.min(500, body.length())));
                
                return CallToolResult.text(output.toString());
                
            } catch (IOException e) {
                return CallToolResult.error("查詢失敗：" + e.getMessage());
            }
        });
    }
    
    /**
     * 取得服務健康狀態
     */
    private CompletableFuture<CallToolResult> getServiceHealth(Map<String, Object> args) {
        return CompletableFuture.supplyAsync(() -> {
            String service = (String) args.get("service");
            String namespace = (String) args.getOrDefault("namespace", "default");
            
            StringBuilder output = new StringBuilder();
            output.append("## 服務健康狀態：").append(service).append("\n\n");
            
            try {
                // 1. 檢查 Pods 狀態
                V1PodList pods = k8sCoreApi.listNamespacedPod(
                    namespace, null, null, null, null,
                    "app=" + service, null, null, null, null, null
                );
                
                long running = pods.getItems().stream()
                    .filter(p -> "Running".equals(p.getStatus().getPhase()))
                    .count();
                int total = pods.getItems().size();
                
                output.append("### Pods\n");
                output.append("- 運行中：").append(running).append("/").append(total).append("\n");
                output.append("- 狀態：").append(running == total ? "✅ 健康" : "⚠️ 異常").append("\n\n");
                
                // 2. 查詢錯誤率（透過 Prometheus）
                String errorQuery = String.format(
                    "sum(rate(http_requests_total{service=\"%s\",status=~\"5..\"}[5m]))",
                    service
                );
                
                HttpUrl url = HttpUrl.parse(PROMETHEUS_URL + "/api/v1/query")
                    .newBuilder()
                    .addQueryParameter("query", errorQuery)
                    .build();
                
                Request request = new Request.Builder().url(url).get().build();
                
                try (Response response = httpClient.newCall(request).execute()) {
                    if (response.isSuccessful()) {
                        output.append("### 錯誤率\n");
                        output.append("- 查詢已執行（詳見 Prometheus）\n\n");
                    }
                } catch (Exception e) {
                    // 忽略 Prometheus 錯誤
                }
                
                return CallToolResult.text(output.toString());
                
            } catch (ApiException e) {
                return CallToolResult.error("❌ 取得健康狀態失敗：" + e.getMessage());
            }
        });
    }
}
```

---

*（第九章完結，繼續第十章）*

---

## 第十章：資源與參考

### 10.1 官方資源

#### 10.1.1 核心文件

| 資源 | URL | 說明 |
|------|-----|------|
| **MCP 規格書** | [spec.modelcontextprotocol.io](https://spec.modelcontextprotocol.io) | 完整協議規格 |
| **官方文件** | [modelcontextprotocol.io/docs](https://modelcontextprotocol.io/docs) | 入門教學與指南 |
| **GitHub 組織** | [github.com/modelcontextprotocol](https://github.com/modelcontextprotocol) | 所有官方專案 |
| **Anthropic MCP 介紹** | [anthropic.com/news/model-context-protocol](https://anthropic.com/news/model-context-protocol) | 官方公告與說明 |

#### 10.1.2 SDK 與工具

| 專案 | 語言 | 說明 |
|------|------|------|
| **mcp** | Python | 官方 Python SDK |
| **@modelcontextprotocol/sdk** | TypeScript | 官方 TypeScript SDK |
| **mcp-inspector** | TypeScript | 互動式除錯工具 |
| **mcp-cli** | TypeScript | 命令列測試工具 |

**安裝指令**：

```bash
# Python SDK
pip install mcp
# 或使用 uv
uv add mcp

# TypeScript SDK
npm install @modelcontextprotocol/sdk

# Inspector
npx @modelcontextprotocol/inspector <server-command>
```

#### 10.1.3 官方範例 Server

| Server | 功能 | 來源 |
|--------|------|------|
| **filesystem** | 檔案系統操作 | 官方範例 |
| **memory** | 知識圖譜記憶 | 官方範例 |
| **puppeteer** | 瀏覽器自動化 | 官方範例 |
| **brave-search** | 網路搜尋 | 官方範例 |
| **github** | GitHub 整合 | 官方範例 |
| **gitlab** | GitLab 整合 | 官方範例 |
| **google-maps** | Google Maps API | 官方範例 |
| **slack** | Slack 整合 | 官方範例 |
| **postgres** | PostgreSQL 資料庫 | 官方範例 |
| **sqlite** | SQLite 資料庫 | 官方範例 |

---

### 10.2 社群資源

#### 10.2.1 第三方 Server 集合

| 資源 | 說明 |
|------|------|
| **Awesome MCP Servers** | 社群維護的 MCP Server 列表 |
| **MCP Hub** | MCP Server 集中倉庫 |

#### 10.2.2 學習資源

| 類型 | 資源 |
|------|------|
| **教學文章** | - Anthropic 官方 Blog<br>- Dev.to MCP 標籤<br>- Medium MCP 文章 |
| **影片教學** | - YouTube MCP 系列<br>- Anthropic 官方直播 |
| **社群討論** | - Discord: MCP Community<br>- Reddit: r/mcp |

---

### 10.3 開發環境建議

#### 10.3.1 VS Code 擴充套件

| 擴充套件 | 用途 |
|----------|------|
| **Python** | Python 開發支援 |
| **Pylance** | Python 型別檢查 |
| **Ruff** | Python Linter |
| **REST Client** | HTTP 請求測試 |
| **YAML** | YAML 格式支援 |
| **JSON Schema Store** | JSON Schema 驗證 |

#### 10.3.2 推薦專案結構

```text
my-mcp-server/
├── src/
│   └── main/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           └── mcp/
│       │               ├── McpServerApp.java       # Server 主程式
│       │               ├── tools/                  # 工具實作
│       │               │   ├── FileTools.java
│       │               │   └── ApiTools.java
│       │               ├── resources/              # 資源實作
│       │               │   └── DataResources.java
│       │               └── util/                   # 工具函數
│       │                   ├── ValidationUtils.java
│       │                   └── CacheUtils.java
│       └── resources/
│           └── log4j2.xml
├── src/
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   └── mcp/
│                       ├── tools/
│                       │   └── FileToolsTest.java
│                       └── resources/
│                           └── DataResourcesTest.java
├── pom.xml
├── README.md
└── .env.example
```

#### 10.3.3 pom.xml 範本

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-mcp-server</artifactId>
    <version>0.1.0</version>
    <packaging>jar</packaging>

    <name>My MCP Server</name>
    <description>My MCP Server Implementation</description>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- MCP SDK -->
        <dependency>
            <groupId>io.modelcontextprotocol</groupId>
            <artifactId>mcp-sdk</artifactId>
            <version>1.1.0</version>
        </dependency>

        <!-- JSON 處理 -->
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>

        <!-- HTTP 客戶端 -->
        <dependency>
            <groupId>com.squareup.okhttp3</groupId>
            <artifactId>okhttp</artifactId>
            <version>4.12.0</version>
        </dependency>

        <!-- 日誌 -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.22.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j2-impl</artifactId>
            <version>2.22.1</version>
        </dependency>

        <!-- 測試 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.8.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.12.1</version>
                <configuration>
                    <source>${java.version}</source>
                    <target>${java.version}</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.example.mcp.McpServerApp</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.5.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.example.mcp.McpServerApp</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

---

### 10.4 版本相容性

#### 10.4.1 MCP 協議版本

| 版本 | 日期 | 時代 | 重大變更 |
|------|------|------|---------|
| **2026-07-28** | 2026-07 | Modern | 無狀態核心、移除 `initialize`／Session、MRTR、`server/discover`、`subscriptions/listen`、擴充框架、JSON Schema 2020-12、標頭路由、快取提示、授權硬化 |
| **2025-11-25** | 2025-11 | Legacy | 實驗性 Tasks、URL 模式 Elicitation、Icons |
| **2025-06-18** | 2025-06 | Legacy | `MCP-Protocol-Version` 標頭、Elicitation 初版、結構化工具輸出 |
| **2025-03-26** | 2025-03 | Legacy | Streamable HTTP 取代 HTTP+SSE、OAuth 授權框架 |
| **2024-11-05** | 2024-11 | Legacy | 初始穩定版本 |

**時代相容性速查**：

| Client 時代 | Server 時代 | 結果 |
|------------|------------|------|
| Modern | Modern | ✅ |
| Modern | Legacy | ❌ 無相容路徑 |
| Dual-era | Modern / Legacy | ✅ |
| Legacy | Modern | ❌ 無向前相容 |
| Legacy | Dual-era | ✅ |

#### 10.4.2 SDK 版本對照

**Tier 1 SDK**（官方維護，需於規範發布窗口內完成支援）：

| SDK | 語言 | `2026-07-28` 支援 |
|-----|------|------------------|
| `@modelcontextprotocol/sdk` | TypeScript | ✅ GA |
| `mcp` | Python | ✅ GA |
| `mcp-go` | Go | ✅ GA |
| `ModelContextProtocol` | C# | ✅ GA |

**Tier 2 及社群 SDK**：

| SDK | 語言 | 狀態 |
|-----|------|------|
| `rmcp` | Rust | Beta |
| `io.modelcontextprotocol.sdk` | Java | 依社群進度跟進 |
| Kotlin / Swift / Ruby / PHP 等 | 多語言 | 依各專案進度 |

> **選型提醒**：非 Tier 1 SDK 不受規範發布窗口約束，可能出現數個月的版本落差。
> 若專案需在規範發布後短期內跟進，應優先選擇 Tier 1 SDK，
> 或在架構決策紀錄（ADR）中明列版本落後風險與緩解方案。

#### 10.4.3 Client 支援狀態

| Client | 支援功能 | 備註 |
|--------|---------|------|
| **Claude Desktop** | Tools, Resources, Prompts, Elicitation | 依版本跟進 `2026-07-28` |
| **Claude Code** | Tools, Resources, Prompts | CLI／IDE 整合 |
| **VS Code / GitHub Copilot** | Tools, Resources, Prompts | 內建 MCP 用戶端 |
| **自訂 Client** | 依實作而定 | 建議使用 Tier 1 SDK |

> **驗證方式**：實際支援程度應以
> [官方 Conformance Suite](https://github.com/modelcontextprotocol/conformance) 的測試結果為準，
> 而非僅依產品說明頁面。

---

### 10.5 快速參考

#### 10.5.1 JSON-RPC 方法列表

**`2026-07-28` 核心方法**：

| 方法 | 方向 | 說明 |
|------|------|------|
| `server/discover` | C→S | 探索伺服器支援的版本與能力（Server **MUST** 實作） |
| `tools/list` | C→S | 列出工具（回應含 `ttlMs` / `cacheScope`） |
| `tools/call` | C→S | 呼叫工具（支援 MRTR） |
| `resources/list` | C→S | 列出資源 |
| `resources/read` | C→S | 讀取資源（支援 MRTR） |
| `resources/templates/list` | C→S | 列出資源範本 |
| `prompts/list` | C→S | 列出提示詞 |
| `prompts/get` | C→S | 取得提示詞（支援 MRTR） |
| `completion/complete` | C→S | 參數自動補全 |
| `subscriptions/listen` | C→S | 開啟長效通知訂閱串流 |

**MRTR 內嵌請求**（不再作為獨立 JSON-RPC 請求送出）：

| 方法 | 承載於 | 狀態 |
|------|--------|------|
| `elicitation/create` | `InputRequests` | Active |
| `sampling/createMessage` | `InputRequests` | Deprecated |
| `roots/list` | `InputRequests` | Deprecated |

**Tasks 擴充方法**（`io.modelcontextprotocol/tasks`）：

| 方法 | 方向 | 說明 |
|------|------|------|
| `tasks/get` | C→S | 查詢任務狀態與結果 |
| `tasks/update` | C→S | 提交任務所需的 `inputResponses` |
| `tasks/cancel` | C→S | 請求取消任務（協作式） |

**通知**：

| 方法 | 方向 | 管道 |
|------|------|------|
| `notifications/progress` | S→C | 請求回應串流 |
| `notifications/message` | S→C | 請求回應串流（Deprecated） |
| `notifications/subscriptions/acknowledged` | S→C | `subscriptions/listen` |
| `notifications/tools/list_changed` | S→C | `subscriptions/listen` |
| `notifications/resources/list_changed` | S→C | `subscriptions/listen` |
| `notifications/resources/updated` | S→C | `subscriptions/listen` |
| `notifications/prompts/list_changed` | S→C | `subscriptions/listen` |
| `notifications/tasks` | S→C | `subscriptions/listen`（Tasks 擴充） |
| `notifications/cancelled` | C→S | **僅 stdio** |

**已移除的方法／通知**（`2026-07-28`）：

| 名稱 | 取代方案 |
|------|----------|
| `initialize` | `_meta` 逐請求中繼資料 |
| `notifications/initialized` | 無（不再需要） |
| `ping` | 傳輸層機制（SSE 保活註解、TCP keep-alive） |
| `logging/setLevel` | `_meta.io.modelcontextprotocol/logLevel` |
| `resources/subscribe` / `resources/unsubscribe` | `subscriptions/listen` 的 `resourceSubscriptions` |
| `notifications/roots/list_changed` | 無（Roots 已棄用） |
| `notifications/elicitation/complete` | 無（改由 `requestState` 關聯） |
| `tasks/result` | `tasks/get` |
| `tasks/list` | 無（無 Session 無法安全界定範圍） |

#### 10.5.2 常用程式碼片段

**快速建立 Server**：

```java
package com.example.mcp;

import io.modelcontextprotocol.server.*;
import io.modelcontextprotocol.server.transport.*;
import io.modelcontextprotocol.spec.McpSchema.*;

import java.util.*;
import java.util.concurrent.*;

public class McpServerApp {
    
    public static void main(String[] args) {
        McpServer server = McpServer.builder()
            .name("my-server")
            .version("1.0.0")
            .build();
        
        // 工具列表
        server.setToolListHandler(request -> 
            CompletableFuture.completedFuture(
                ListToolsResult.builder()
                    .tools(List.of(/* 工具定義 */))
                    .build()
            )
        );
        
        // 工具呼叫
        server.setToolHandler(request -> 
            CompletableFuture.supplyAsync(() -> {
                String name = request.getParams().getName();
                Map<String, Object> args = request.getParams().getArguments();
                // 處理工具呼叫
                return CallToolResult.text("結果");
            })
        );
        
        // 使用 STDIO 傳輸啟動
        StdioServerTransport transport = new StdioServerTransport();
        server.connect(transport).join();
    }
}
```

**Claude Desktop 配置**：

```json
{
  "mcpServers": {
    "my-server": {
      "command": "java",
      "args": ["-jar", "/path/to/my-mcp-server.jar"],
      "env": {
        "MY_VAR": "value"
      }
    }
  }
}
```

---

## 第十一章：2026-07-28 遷移指南

### 11.1 遷移總體策略

`2026-07-28` 是 MCP 自公開以來變動幅度最大的版本。本節提供的是**可執行的遷移路線**，
而非僅是變更清單。

#### 11.1.1 遷移決策樹

```mermaid
graph TD
    A[現有 MCP 實作] --> B{是 Server 還是 Client？}
    B -->|Server| C{是否需要服務既有 Legacy 用戶端？}
    C -->|需要| D[實作雙時代 Dual-era]
    C -->|不需要| E[直接遷移為 Modern-only]
    B -->|Client| F{目標伺服器生態是否已全面升級？}
    F -->|是| G[直接遷移為 Modern-only]
    F -->|否| H[實作雙時代含回退偵測]
    D --> I[以 Conformance Suite 驗證]
    E --> I
    G --> I
    H --> I
```

#### 11.1.2 遷移階段規劃

| 階段 | 目標 | 主要產出 |
|------|------|----------|
| **P0 盤點** | 掌握受影響範圍 | 功能相依矩陣、棄用功能使用清單 |
| **P1 相依升級** | 升級 SDK 至支援 `2026-07-28` 的版本 | 相依版本鎖定、建置通過 |
| **P2 核心改造** | 移除 Session 假設、導入 `_meta` | 無狀態伺服器、`server/discover` |
| **P3 互動改造** | 導入 MRTR、`subscriptions/listen` | Elicitation 流程重寫 |
| **P4 棄用汰換** | 移除 Sampling／Roots／Logging 相依 | 直接 LLM 串接、參數化路徑、OTel |
| **P5 部署改造** | 移除 Sticky Session、加入標頭路由 | 無狀態擴展、閘道策略 |
| **P6 驗證** | Conformance + 端對端測試 | 符規報告、回歸測試報告 |

#### 11.1.3 風險評估

| 風險 | 影響 | 緩解措施 |
|------|------|----------|
| 隱式依賴連線狀態 | 水平擴展後間歇性失敗 | 以 Round-Robin 測試環境驗證；刻意讓每個請求打到不同實例 |
| `requestState` 未加保護 | 授權繞過、狀態竄改 | 強制 HMAC/AEAD + TTL + principal 綁定 |
| Legacy 用戶端未通知即斷開 | 生產中斷 | 先部署雙時代，觀察 Legacy 流量降至零再移除 |
| 非 Tier 1 SDK 未跟上 | 專案受阻 | 評估暫時自行實作傳輸層，或改用 Tier 1 SDK |
| Tasks 實驗性 API 相依 | 編譯／執行失敗 | 依 12.3 重寫為擴充 API |

---

### 11.2 Server 端遷移步驟

#### 11.2.1 步驟一：移除交握與 Session

```diff
- // 舊：處理 initialize
- server.setInitializeHandler(request -> {
-     var clientCaps = request.getParams().getCapabilities();
-     sessionStore.put(sessionId, new Session(clientCaps));
-     return InitializeResult.builder()
-         .protocolVersion("2025-11-25")
-         .capabilities(serverCapabilities)
-         .build();
- });
-
+ // 新：實作 server/discover（MUST）
+ server.setDiscoverHandler(request ->
+     DiscoverResult.builder()
+         .resultType("complete")
+         .supportedVersions(List.of("2026-07-28"))
+         .capabilities(serverCapabilities)
+         .ttlMs(3_600_000L)
+         .cacheScope("public")
+         .build());
```

**必須移除的狀態假設**：

- 以 `Mcp-Session-Id` 或連線物件為鍵的任何快取／上下文。
- 「第一個請求一定是 `initialize`」的前提。
- 「同一連線上的請求屬於同一對話」的前提。

#### 11.2.2 步驟二：從 `_meta` 讀取請求上下文

```java
/**
 * 2026-07-28：逐請求解析協議中繼資料
 */
public final class RequestContext {

    private static final String NS = "io.modelcontextprotocol/";

    public static RequestContext from(Map<String, Object> params) {
        @SuppressWarnings("unchecked")
        Map<String, Object> meta = (Map<String, Object>) params.get("_meta");

        if (meta == null) {
            throw new InvalidParamsException("Missing _meta");
        }

        String version = (String) meta.get(NS + "protocolVersion");
        if (version == null) {
            // MUST 回傳 -32602，HTTP 400
            throw new InvalidParamsException(
                "Missing required _meta field: " + NS + "protocolVersion");
        }
        if (!SUPPORTED_VERSIONS.contains(version)) {
            // MUST 回傳 -32022
            throw new UnsupportedProtocolVersionException(SUPPORTED_VERSIONS, version);
        }

        @SuppressWarnings("unchecked")
        Map<String, Object> caps = (Map<String, Object>) meta.get(NS + "clientCapabilities");
        if (caps == null) {
            throw new InvalidParamsException(
                "Missing required _meta field: " + NS + "clientCapabilities");
        }

        return new RequestContext(
            version,
            ClientCapabilities.fromMap(caps),
            Implementation.fromMap(meta.get(NS + "clientInfo")),   // 可選
            (String) meta.get(NS + "logLevel"),                     // 可選
            (String) meta.get("traceparent")                        // 可選
        );
    }

    /** 需要某能力但用戶端未宣告時使用 */
    public void requireCapability(String name) {
        if (!clientCapabilities.has(name)) {
            throw new MissingRequiredClientCapabilityException(List.of(name));
        }
    }
}
```

> **安全提醒**：`clientInfo` 為未驗證的自我宣告值。
> **MUST NOT** 用於授權判斷、功能開關或速率限制分組。

#### 11.2.3 步驟三：將 Server-to-Client 請求改為 MRTR

```diff
- // 舊：伺服器主動送出 elicitation/create
- var answer = server.request("elicitation/create", Map.of(
-         "message", "確認刪除？",
-         "requestedSchema", schema))
-     .get();
- if (Boolean.TRUE.equals(answer.get("confirm"))) {
-     performDelete();
- }

+ // 新：回傳 InputRequiredResult，等待用戶端以新請求重試
+ var responses = params.get("inputResponses");
+ if (responses == null) {
+     return InputRequiredResult.builder()
+         .inputRequests(Map.of("confirm_delete", ElicitRequest.builder()
+             .mode("form")
+             .message("確認刪除？")
+             .requestedSchema(schema)
+             .build()))
+         .requestState(stateCodec.seal(new PendingDelete(targetPath), principal))
+         .build();
+ }
+ // 重試路徑：驗證並解封 requestState
+ PendingDelete pending = stateCodec.unseal(
+     (String) params.get("requestState"), principal);   // 驗證失敗即拋錯
+ if (isAccepted(responses, "confirm_delete")) {
+     performDelete(pending.targetPath());
+ }
```

**`requestState` 保護實作要點**：

```java
/**
 * requestState 封裝：AEAD 加密 + 綁定 principal + TTL + 原請求識別
 */
public record SealedState(
    String principal,      // 經認證的主體
    String requestFingerprint, // method + 關鍵參數摘要
    Instant expiresAt,     // 短期 TTL
    byte[] payload
) {}

public String seal(Object state, String principal, String fingerprint) {
    var sealed = new SealedState(
        principal,
        fingerprint,
        Instant.now().plus(Duration.ofMinutes(5)),
        serialize(state)
    );
    return Base64.getUrlEncoder().withoutPadding()
        .encodeToString(aead.encrypt(serialize(sealed)));
}

public <T> T unseal(String token, String principal, String fingerprint, Class<T> type) {
    SealedState sealed = deserialize(aead.decrypt(Base64.getUrlDecoder().decode(token)));
    // MUST：完整性已由 AEAD 保證，接著檢查重放防護三要素
    if (!sealed.principal().equals(principal)) throw new SecurityException("principal mismatch");
    if (!sealed.requestFingerprint().equals(fingerprint)) throw new SecurityException("request mismatch");
    if (Instant.now().isAfter(sealed.expiresAt())) throw new SecurityException("state expired");
    return deserialize(sealed.payload(), type);
}
```

> **⚠️ 一次性語意**：若某個 `requestState` 只能被兌換一次（例如扣款、發放額度），
> **MUST** 在伺服器端額外維護已兌換識別碼的紀錄。
> AEAD 只能保證未被竄改，**不能**防止用戶端重複提交同一份合法狀態。

#### 11.2.4 步驟四：改寫通知與訂閱

```diff
- // 舊：resources/subscribe + GET SSE 串流
- server.setResourceSubscribeHandler(req -> {
-     subscriptions.add(sessionId, req.getParams().getUri());
-     return EmptyResult.INSTANCE;
- });

+ // 新：subscriptions/listen 長效請求
+ server.setSubscriptionsListenHandler((req, stream) -> {
+     var filter = req.getParams().getNotifications();
+     long subscriptionId = req.getId();
+
+     // MUST：第一則訊息為 acknowledged，回報實際承接的子集
+     stream.send(Notification.of("notifications/subscriptions/acknowledged",
+         Map.of("_meta", Map.of("io.modelcontextprotocol/subscriptionId", subscriptionId),
+                "notifications", honoredSubset(filter))));
+
+     registry.register(subscriptionId, filter, stream);
+ });
```

**檢查點**：

- 所有推送至訂閱串流的通知 **MUST** 攜帶 `io.modelcontextprotocol/subscriptionId`。
- `notifications/progress`、`notifications/message` **MUST NOT** 出現在訂閱串流。
- 伺服器主動關閉前 **SHOULD** 先回傳空的 `complete` 結果。

#### 11.2.5 步驟五：加入快取提示與確定性排序

```java
return ListToolsResult.builder()
    .resultType("complete")
    .tools(tools.stream()
        .sorted(Comparator.comparing(Tool::getName))   // 確定性順序
        .toList())
    .ttlMs(3_600_000L)
    .cacheScope("public")     // 若清單因使用者而異，改用 "private"
    .build();
```

#### 11.2.6 步驟六：HTTP 層調整

| 項目 | 動作 |
|------|------|
| `GET /mcp` | 改回傳 `405 Method Not Allowed` |
| `DELETE /mcp` | 改回傳 `405 Method Not Allowed` |
| `Mcp-Session-Id` | 停止產生與驗證 |
| `Last-Event-ID` | 停止處理（不再支援 resumability） |
| 標頭驗證 | 新增 `MCP-Protocol-Version` / `Mcp-Method` / `Mcp-Name` 一致性檢查，不符回 `400` + `-32020` |
| SSE 回應 | 加上 `X-Accel-Buffering: no`；長效串流加保活註解 |
| 取消 | 以「串流關閉」判定取消，移除對 `notifications/cancelled` 的 HTTP 處理 |

---

### 11.3 Client 端遷移步驟

#### 11.3.1 步驟一：建構自我描述請求

```java
/**
 * 每個請求都注入協議中繼資料
 */
public Map<String, Object> withProtocolMeta(Map<String, Object> params) {
    var meta = new LinkedHashMap<String, Object>();
    meta.put("io.modelcontextprotocol/protocolVersion", "2026-07-28");
    meta.put("io.modelcontextprotocol/clientCapabilities", Map.of(
        "elicitation", Map.of(),
        "extensions", Map.of(
            "io.modelcontextprotocol/tasks", Map.of()
        )
    ));
    meta.put("io.modelcontextprotocol/clientInfo", Map.of(
        "name", "my-app", "version", "1.0.0"
    ));
    // 分散式追蹤
    currentSpan().ifPresent(s -> meta.put("traceparent", s.traceparent()));

    var merged = new LinkedHashMap<>(params);
    merged.put("_meta", meta);
    return merged;
}
```

#### 11.3.2 步驟二：實作 MRTR 重試迴圈

```java
/**
 * MRTR 迴圈：以「新的 JSON-RPC id」重試原請求
 */
public CallToolResult callToolWithMrtr(String name, Map<String, Object> arguments) {
    Map<String, Object> params = new LinkedHashMap<>();
    params.put("name", name);
    params.put("arguments", arguments);

    for (int round = 0; round < MAX_ROUNDS; round++) {
        var result = transport.request("tools/call", withProtocolMeta(params));

        // 舊版伺服器無 resultType，視為 complete
        String type = result.getString("resultType", "complete");

        switch (type) {
            case "complete" -> { return CallToolResult.from(result); }
            case "input_required" -> {
                var inputRequests = result.getMap("inputRequests");   // 可能不存在
                if (inputRequests != null) {
                    params.put("inputResponses", fulfil(inputRequests));
                }
                // MUST：原樣回傳；若原本沒有就不要自行加上
                if (result.has("requestState")) {
                    params.put("requestState", result.getString("requestState"));
                }
                // 迴圈下一輪會產生新的 JSON-RPC id
            }
            case "task" -> { return pollTask(result.getString("taskId")); }
            default -> throw new ProtocolException("Unrecognized resultType: " + type);
        }
    }
    throw new ProtocolException("MRTR 迴圈超過上限");
}
```

> **實作提醒**：`MAX_ROUNDS` 是必要的防護。規範允許伺服器對同一請求
> **多次**回傳 `InputRequiredResult`，缺乏上限會讓惡意或有缺陷的伺服器造成無限迴圈。

#### 11.3.3 步驟三：改用 `subscriptions/listen`

```diff
- // 舊：GET /mcp 開啟 SSE + resources/subscribe
- eventSource = httpClient.openSse("GET", baseUrl + "/mcp");
- client.request("resources/subscribe", Map.of("uri", uri));

+ // 新：單一長效 POST 請求
+ var stream = client.openStream("subscriptions/listen", withProtocolMeta(Map.of(
+     "notifications", Map.of(
+         "toolsListChanged", true,
+         "resourceSubscriptions", List.of(uri)))));
+
+ var ack = stream.awaitFirst();   // MUST 為 notifications/subscriptions/acknowledged
+ long subscriptionId = ack.meta().getLong("io.modelcontextprotocol/subscriptionId");
+ // SHOULD：比對請求與確認內容，優雅處理伺服器未承接的類型
+ warnIfUnsupported(requested, ack.get("notifications"));
```

#### 11.3.4 步驟四：處理標頭鏡射

用戶端 **MUST** 支援 `x-mcp-header`。實作重點：

```java
/**
 * 依工具 Schema 的 x-mcp-header 註記產生 Mcp-Param-* 標頭
 */
Map<String, String> buildParamHeaders(Tool tool, Map<String, Object> args) {
    var headers = new LinkedHashMap<String, String>();
    for (var e : staticallyReachableProperties(tool.inputSchema()).entrySet()) {
        String headerName = e.getValue().getString("x-mcp-header");
        if (headerName == null) continue;
        Object value = args.get(e.getKey());
        if (value == null) continue;
        headers.put("Mcp-Param-" + headerName, encodeHeaderValue(String.valueOf(value)));
    }
    return headers;
}

/** 非 ASCII／控制字元／前後空白 → =?base64?...?= */
String encodeHeaderValue(String raw) {
    if (needsEncoding(raw)) {
        return "=?base64?" + Base64.getEncoder().encodeToString(
            raw.getBytes(StandardCharsets.UTF_8)) + "?=";
    }
    return raw;
}
```

驗證失敗的工具定義 **MUST** 從 `tools/list` 結果中排除，並 **SHOULD** 記錄警告。

#### 11.3.5 步驟五：時代偵測與回退

```java
/**
 * HTTP：Modern → Legacy 回退偵測
 */
Era detectEra(String origin) {
    return eraCache.computeIfAbsent(origin, o -> {
        var resp = postModern(o, buildDiscoverRequest());
        if (resp.status() / 100 == 2) return Era.MODERN;

        if (resp.status() == 400 && isRecognizedModernError(resp.body())) {
            return Era.MODERN;   // 只是版本不合，挑共同版本重試
        }
        // 空 Body 或無法辨識 → 視為 Legacy
        return tryInitialize(o) ? Era.LEGACY : Era.UNKNOWN;
    });
}
```

stdio 情境改以 `server/discover` 作為探針；失敗或逾時即視為 Legacy。

---

### 11.4 從 Session 到顯式握柄（Explicit Handle）

#### 11.4.1 問題本質

舊版的隱式 Session 讓伺服器可以「記住」上一次呼叫的結果。無狀態化後，
這類需求必須改由**顯式握柄**承載——由伺服器鑄造識別碼、放進工具結果，
再由模型當作一般參數傳回。

```mermaid
sequenceDiagram
    participant M as LLM / Agent
    participant C as Client
    participant S as Server（多實例）

    M->>C: 建立購物車
    C->>S: tools/call create_basket
    S-->>C: { basketId: "bk_7f3a" }
    Note over M: 模型「看得見」這個握柄

    M->>C: 加入商品（basketId=bk_7f3a）
    C->>S: tools/call add_item（不同實例也可）
    S-->>C: { basketId: "bk_7f3a", itemCount: 1 }
```

#### 11.4.2 設計對照

| 面向 | 隱式 Session | 顯式握柄 |
|------|-------------|----------|
| 模型可見性 | 不可見 | **可見**，可推理、可組合 |
| 多實例部署 | 需 Sticky Session | 天然支援 Round-Robin |
| 併發操作 | 難以同時操作多個上下文 | 可同時持有多個握柄 |
| 交接與稽核 | 難以在對話間傳遞 | 可直接交接、可記錄 |
| 失效處理 | 連線中斷即遺失 | 由伺服器 TTL 控制，可續用 |

#### 11.4.3 握柄設計準則

| 準則 | 說明 |
|------|------|
| **可辨識前綴** | `bk_`、`wf_`、`br_` 等前綴讓模型與人類都能辨識用途 |
| **不可猜測** | 使用密碼學隨機值，長度足以抵抗列舉 |
| **授權綁定** | 伺服器端 **MUST** 驗證呼叫者有權存取該握柄，不可僅憑握柄本身授權 |
| **明確 TTL** | 於工具描述與結果中標示有效期 |
| **顯式生命週期工具** | 提供 `close_*` / `release_*` 工具讓代理主動釋放資源 |
| **清楚的錯誤** | 握柄過期或無效時回傳可讀訊息，指引模型重新建立 |

```json
{
  "name": "add_item_to_basket",
  "description": "將商品加入既有購物車。basketId 由 create_basket 取得，有效期 30 分鐘。",
  "inputSchema": {
    "type": "object",
    "properties": {
      "basketId": {
        "type": "string",
        "description": "購物車握柄，格式 bk_xxxxxxxx",
        "pattern": "^bk_[A-Za-z0-9]{8,}$"
      },
      "sku": { "type": "string" },
      "quantity": { "type": "integer", "minimum": 1 }
    },
    "required": ["basketId", "sku", "quantity"]
  }
}
```

> **⚠️ 安全要求**：握柄**不是**憑證。伺服器 **MUST** 以請求的授權主體
> 交叉驗證握柄擁有權，否則將形成不安全的直接物件參考（IDOR，OWASP A01）。

#### 11.4.4 常見遷移對照

| 舊模式 | 新模式 |
|--------|--------|
| Session 內的瀏覽器實例 | `browser_id` 握柄 + 顯式 `close_browser` 工具 |
| Session 內的資料庫交易 | `transaction_id` 握柄 + `commit` / `rollback` 工具 |
| Session 內的多步驟精靈 | `workflow_id` 握柄 + `resultType: input_required`（MRTR） |
| Session 內的分頁游標 | 於結果回傳 `nextCursor`，由用戶端傳回 |
| Session 內的使用者偏好 | 由授權 Token 的主體推導，或以工具參數明確傳入 |

---

### 11.5 雙時代（Dual-era）相容部署

#### 11.5.1 伺服器端分流

```java
/**
 * 依請求特徵分流至 Modern / Legacy 處理管線
 */
public Response route(HttpRequest http) {
    JsonObject body = parse(http.body());

    boolean isModern = body.path("params").path("_meta")
        .has("io.modelcontextprotocol/protocolVersion");

    if (isModern) {
        return modernPipeline.handle(http, body);
    }
    if ("initialize".equals(body.getString("method"))) {
        return legacyPipeline.handle(http, body);
    }
    // Legacy 的後續請求依 Mcp-Session-Id 判定
    if (http.header("Mcp-Session-Id") != null) {
        return legacyPipeline.handle(http, body);
    }
    return badRequest(-32602, "Missing protocol metadata");
}
```

#### 11.5.2 部署拓樸

```mermaid
graph TB
    Client1[Modern Client] --> GW[API Gateway]
    Client2[Legacy Client] --> GW

    GW -->|有 _meta.protocolVersion| MP[Modern Pool<br/>無狀態 / Round-Robin]
    GW -->|initialize 或 Mcp-Session-Id| LP[Legacy Pool<br/>Sticky Session]

    MP --> BE[(共用後端服務)]
    LP --> BE

    MP -.時代流量指標.-> OBS[可觀測性平台]
    LP -.時代流量指標.-> OBS
```

**設計要點**：Legacy 與 Modern 應以**獨立資源池**部署。
Legacy 池仍需 Sticky Session 與較高記憶體配額；Modern 池則可積極自動擴縮。
兩池共用同一後端服務層，確保業務邏輯單一來源。

#### 11.5.3 汰除計畫

| 里程碑 | 動作 | 判準 |
|--------|------|------|
| M1 | 部署雙時代，開始蒐集時代流量指標 | Modern 路徑通過 Conformance |
| M2 | 對 Legacy 請求回傳棄用警示（日誌／文件公告） | Legacy 流量開始下降 |
| M3 | 公告 Legacy 支援終止日（建議 ≥ 90 天前置） | 主要用戶端已升級 |
| M4 | Legacy 池縮容至最小 | Legacy 流量 < 1% |
| M5 | 移除 Legacy 管線與相關程式碼 | Legacy 流量歸零逾 30 天 |

> **官方時程參考**：`2026-07-28` 標記的棄用功能，最早移除日不早於 **2027-07-28**。
> 企業可據此規劃內部汰除窗口，但**不應假設**上游一定會延後移除。

---

## 第十二章：擴充框架與官方擴充

### 12.1 擴充框架（Extensions Framework）

#### 12.1.1 設計動機

`2026-07-28` 之前，任何新功能都必須進入核心規範，導致核心不斷膨脹、
發布節奏被最慢的功能拖住。擴充框架（SEP-2133）將「協議核心」與「可選能力」正式分離。

```mermaid
graph TB
    subgraph CORE["核心規範（Standards Track）"]
        A[JSON-RPC 訊息模型]
        B[Tools / Resources / Prompts]
        C[MRTR / Subscriptions]
        D[傳輸層 / 授權]
    end

    subgraph EXT["擴充（Extensions Track）"]
        E[io.modelcontextprotocol/tasks]
        F[io.modelcontextprotocol/ui]
        G[ext-auth 系列]
        H[com.example/my-extension]
    end

    CORE -->|穩定基礎| EXT
    EXT -->|協商後啟用| CORE
```

#### 12.1.2 識別碼規範

擴充識別碼格式為 `{vendor-prefix}/{extension-name}`，前綴採**反向 DNS**：

| 前綴 | 歸屬 |
|------|------|
| `io.modelcontextprotocol/` | MCP 官方擴充 |
| `com.example/` | 擁有 `example.com` 網域的組織 |

> **命名規則**：第三方**必須**使用自己實際擁有的網域反轉形式，
> 避免與官方或其他組織的擴充命名衝突。

#### 12.1.3 協商機制

擴充透過 `capabilities.extensions` 對應表協商——鍵為識別碼，值為設定物件；
空物件 `{}` 表示「支援但無額外設定」。

```json
// Client → Server：於每個請求的 _meta 中
{
  "_meta": {
    "io.modelcontextprotocol/protocolVersion": "2026-07-28",
    "io.modelcontextprotocol/clientCapabilities": {
      "extensions": {
        "io.modelcontextprotocol/ui": {
          "mimeTypes": ["text/html;profile=mcp-app"]
        }
      }
    }
  }
}

// Server → Client：於 server/discover 結果中
{
  "resultType": "complete",
  "supportedVersions": ["2026-07-28"],
  "capabilities": {
    "tools": {},
    "extensions": {
      "io.modelcontextprotocol/ui": {}
    }
  },
  "ttlMs": 3600000,
  "cacheScope": "public"
}
```

#### 12.1.4 治理原則

| 原則 | 說明 |
|------|------|
| **預設關閉** | 擴充一律預設停用，需開發者明確啟用 |
| **獨立版本** | 擴充存放於 `ext-*` 儲存庫，有專屬維護者，版本獨立於核心規範 |
| **實驗軌道** | 早期擴充置於 `experimental-ext-*`，須綁定 Working／Interest Group |
| **優雅降級** | 支援方 **MUST** 退回核心行為或回傳適當錯誤 |
| **破壞性變更** | 優先以設定物件內的能力旗標／版本欄位處理；不得已才改用新識別碼（如 `.../my-extension-v2`） |

#### 12.1.5 擴充生命週期

```mermaid
graph LR
    A[Propose<br/>提出 SEP<br/>Extensions Track] --> B[Implement<br/>至少一個官方 SDK<br/>參考實作]
    B --> C[Review<br/>核心維護者審查]
    C --> D[Publish<br/>發布至 ext-* 儲存庫]
    D --> E[Adopt<br/>生態採用]
```

> **重點**：Extensions Track 的 SEP **必須先有可運作的參考實作**才進入審查。
> 這與 Standards Track「先定規範再實作」的順序相反，目的是確保擴充設計經過實務驗證。

---

### 12.2 MCP Apps：伺服器渲染互動介面

#### 12.2.1 概述

MCP Apps（SEP-1865，識別碼 `io.modelcontextprotocol/ui`）讓 MCP 伺服器
能夠提供**互動式使用者介面**，直接嵌入在對話中呈現，而非只能回傳文字或結構化資料。

```mermaid
sequenceDiagram
    participant U as 使用者
    participant H as Host（沙箱 iframe）
    participant C as Client
    participant S as Server

    Note over C,S: 協商 io.modelcontextprotocol/ui
    S-->>C: tools/list（工具的 _meta.ui.resourceUri 指向 ui:// 資源）
    C->>S: resources/read（ui://...）
    S-->>C: HTML / JS 範本

    U->>C: 觸發工具
    C->>H: 於沙箱 iframe 渲染範本
    H->>C: postMessage（JSON-RPC）
    Note over C: 與直接工具呼叫走相同的<br/>稽核與同意路徑
    C->>S: tools/call
    S-->>C: 結果
    C->>H: 更新 UI
```

#### 12.2.2 運作機制

| 環節 | 說明 |
|------|------|
| **範本註冊** | 伺服器將工具透過 `_meta.ui.resourceUri` 連結到 `ui://` 資源 |
| **預先宣告** | 範本事先宣告，讓 Host 可預先抓取、快取與安全審查 |
| **沙箱渲染** | Host 在**沙箱 iframe** 中渲染 HTML／JS，無法存取宿主頁面或 Cookie |
| **雙向通訊** | 透過 `postMessage` 承載 JSON-RPC，UI 可回頭呼叫工具 |
| **同一稽核路徑** | UI 發起的每個動作都走與直接工具呼叫**相同**的稽核與使用者同意流程 |

#### 12.2.3 價值主張

| 效益 | 說明 |
|------|------|
| **脈絡保存** | 使用者無須離開對話切換到外部應用 |
| **一次建置、處處執行** | 同一份介面可在任何支援此擴充的 Host 中運作 |
| **優雅降級** | 不支援的 Host 自動退回文字或結構化資料呈現 |

#### 12.2.4 適用情境

| 情境 | 說明 |
|------|------|
| 資料儀表板 | 互動式圖表與篩選器，取代大量文字表格 |
| 多步驟設定表單 | 一次收集完整參數，減少來回問答 |
| 文件審閱 | 以標註、差異比對呈現變更 |
| 即時監控元件 | 持續更新的狀態面板 |

> **⚠️ 安全考量**：沙箱 iframe 是必要但非充分的防護。
> 企業導入時應額外要求：範本來源可審查、CSP（Content Security Policy）明確限制、
> UI 觸發的工具呼叫比照一般工具呼叫進行速率限制與授權檢查。

---

### 12.3 Tasks 擴充深入解析

#### 12.3.1 定位與貢獻來源

Tasks 擴充（SEP-2663，識別碼 `io.modelcontextprotocol/tasks`）由 **AWS 貢獻**，
用於處理「執行時間遠超單次請求合理等待時間」的操作。
其設計已在 Amazon Bedrock AgentCore 上實際驗證。

#### 12.3.2 伺服器主導模型

這是與 `2025-11-25` 實驗性版本最根本的差異：

```mermaid
graph TD
    A[Client 於 _meta 宣告支援 tasks 擴充] --> B[Client 送出一般 tools/call]
    B --> C{Server 判斷執行時間}
    C -->|短| D[直接回傳 resultType: complete]
    C -->|長| E[MUST 先確認 Client 已宣告支援]
    E --> F[持久化建立任務]
    F --> G[回傳 CreateTaskResult<br/>resultType: task]
```

用戶端**不需要**、也**不能**逐請求標記「這個要用任務」。
它只需宣告支援一次，之後由伺服器依實際情況決定。

> **強制檢查**：伺服器 **MUST** 在回傳任務前確認用戶端已宣告支援此擴充。
> 對未宣告的用戶端回傳 `resultType: "task"` 會導致其無法辨識而視為無效結果。

#### 12.3.3 任務狀態機

```mermaid
stateDiagram-v2
    [*] --> working: CreateTaskResult
    working --> input_required: 需要額外輸入
    input_required --> working: tasks/update（inputResponses）
    working --> completed: 成功
    working --> failed: 錯誤
    working --> cancelled: tasks/cancel
    input_required --> cancelled: tasks/cancel
    completed --> [*]
    failed --> [*]
    cancelled --> [*]
```

| 狀態 | 終端 | 附帶欄位 |
|------|------|----------|
| `working` | 否 | `pollIntervalMs` |
| `input_required` | 否 | `inputRequests` |
| `completed` | **是** | `result` |
| `failed` | **是** | `error` |
| `cancelled` | **是** | — |

終端狀態**不可變**：一旦進入 `completed` / `failed` / `cancelled`，狀態與內容即固定。

#### 12.3.4 方法一覽

| 方法 | 用途 | 備註 |
|------|------|------|
| `tasks/get` | 查詢狀態與結果 | 預設互動模式；依 `pollIntervalMs` 輪詢 |
| `tasks/update` | 提交 `inputResponses` | 用於 `input_required` 狀態 |
| `tasks/cancel` | 請求取消 | **協作式**：伺服器盡力而為，非保證立即停止 |

**已移除**：`tasks/result`（合併入 `tasks/get`）、`tasks/list`
（無 Session 時無法安全界定「這個用戶端的任務」範圍，列出他人任務將構成資訊洩漏）。

#### 12.3.5 建立與輪詢

```json
// 1) Server 回傳任務握柄
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "task",
    "taskId": "task-8f21c",
    "status": "working",
    "ttlMs": 86400000,
    "pollIntervalMs": 2000
  }
}

// 2) Client 輪詢
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tasks/get",
  "params": {
    "taskId": "task-8f21c",
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {
        "extensions": { "io.modelcontextprotocol/tasks": {} }
      }
    }
  }
}

// 3) 完成
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "resultType": "complete",
    "taskId": "task-8f21c",
    "status": "completed",
    "result": {
      "content": [{ "type": "text", "text": "分析完成，處理 10,482 筆資料。" }]
    }
  }
}
```

#### 12.3.6 中途輸入

任務進入 `input_required` 時會攜帶 `inputRequests`，用戶端以 `tasks/update` 回覆：

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tasks/update",
  "params": {
    "taskId": "task-8f21c",
    "inputResponses": {
      "approve_budget": { "action": "accept", "content": { "approved": true } }
    },
    "_meta": { "io.modelcontextprotocol/protocolVersion": "2026-07-28",
               "io.modelcontextprotocol/clientCapabilities": {
                 "elicitation": {},
                 "extensions": { "io.modelcontextprotocol/tasks": {} } } }
  }
}
```

#### 12.3.7 推播通知

輪詢是**預設**模式，但用戶端可透過 `subscriptions/listen` 訂閱 `notifications/tasks`
以降低延遲與請求量。該通知**攜帶完整任務狀態**，用戶端無須再額外呼叫 `tasks/get`。

#### 12.3.8 持久性要求

| 要求 | 說明 |
|------|------|
| 建立即持久化 | 伺服器 **MUST** 在回傳 `CreateTaskResult` 前完成任務的持久化建立 |
| 跨連線存活 | `taskId` **MUST** 在連線中斷、伺服器重啟後仍可用 |
| 用戶端持久化 | 用戶端 **SHOULD** 持久化 `taskId`，以便重啟後續接 |
| TTL | `ttlMs` 定義任務記錄的保留期限 |

> **企業提醒**：任務持久化通常意味著引入外部儲存（資料庫、Redis、DynamoDB 等）。
> 在無狀態伺服器架構下，這是**唯一**被規範認可的跨請求狀態存放方式，
> 且必須以 `taskId` 為顯式鍵，而非以連線或進程為鍵。

---

### 12.4 企業託管授權（EMA）與 OAuth 擴充

#### 12.4.1 Enterprise-Managed Authorization

EMA 位於 `ext-auth` 儲存庫，解決企業導入 MCP 時最常見的摩擦：
**每個使用者、對每個 MCP 伺服器，都要各自跑一次 OAuth 同意流程**。

```mermaid
sequenceDiagram
    participant Admin as IT 管理員
    participant IdP as 企業 IdP
    participant U as 使用者
    participant H as MCP Host
    participant S as MCP Server

    Admin->>IdP: 集中佈建可存取的 MCP 伺服器清單
    U->>IdP: 單一登入
    IdP-->>H: 身分 + 已授權的伺服器清單
    Note over H,S: 使用者無須逐一同意
    H->>S: 已授權的請求
```

| 效益 | 說明 |
|------|------|
| **集中治理** | IT 管理員在 IdP 決定誰能存取哪些 MCP 伺服器 |
| **零額外同意** | 使用者登入後自動連上已佈建的伺服器 |
| **可稽核** | 存取決策集中於身分平台，符合企業合規要求 |
| **可撤銷** | 於 IdP 撤銷即全域生效 |

#### 12.4.2 OAuth Client Credentials 擴充

同樣位於 `ext-auth`，用於**機器對機器（M2M）**情境：自動化流程、
排程作業、後端服務彼此呼叫等沒有互動式使用者的場景。

| 對比 | Authorization Code + PKCE | Client Credentials |
|------|--------------------------|-------------------|
| 適用 | 有互動使用者 | 無互動使用者（M2M） |
| 主體 | 使用者 | 服務身分 |
| 使用者同意 | 需要 | 不適用 |
| 憑證 | Access／Refresh Token | Client ID + Secret 或 `private_key_jwt` |

> **安全提醒**：Client Credentials 沒有使用者上下文，
> 因此**所有授權判斷都落在服務身分的權限範圍**。
> 應嚴格套用最小權限原則，並為每個自動化流程配置獨立的服務身分，避免共用。

#### 12.4.3 授權硬化摘要（`2026-07-28`）

| SEP | 主題 | 要求 |
|-----|------|------|
| SEP-2468 | AS Mix-up 防護 | AS **SHOULD** 回傳 `iss`（RFC 9207）；Client **MUST** 於兌換前驗證 |
| SEP-837 | DCR `application_type` | Client **MUST** 明確指定；原生應用用 `"native"` |
| SEP-2352 | 憑證綁定 | **MUST** 以 `issuer` 為鍵持久化；**MUST NOT** 跨 AS 重用 |
| SEP-2207 | Refresh Token | 明確記載向 OIDC 型 AS 請求 Refresh Token 的做法 |
| SEP-2350 | 範圍累積 | 分階段授權時累積既有 scope，避免權限降級 |
| SEP-2351 | 探索路徑 | 釐清 `.well-known` 後綴的組合規則 |
| PR #2858 | CIMD | 正式取代 DCR，DCR 標記為棄用 |

---

### 12.5 自建第三方擴充

#### 12.5.1 何時該建立擴充

```mermaid
graph TD
    A[有新需求] --> B{能以既有 Tools/Resources/Prompts 表達？}
    B -->|能| C[直接以工具設計解決<br/>不需擴充]
    B -->|不能| D{需要新的 JSON-RPC 方法<br/>或新的協議語意？}
    D -->|不需要| E[以 _meta 自訂欄位承載<br/>使用自有前綴]
    D -->|需要| F{是否為通用需求？}
    F -->|是| G[提出 SEP<br/>走 Extensions Track]
    F -->|否| H[建立組織內部擴充<br/>com.yourdomain/...]
```

> **實務建議**：絕大多數需求應該用**工具設計**解決，而非建立擴充。
> 擴充帶來的協商複雜度、降級處理與長期維護成本相當可觀。

#### 12.5.2 內部擴充實作範例

```java
/**
 * 自建擴充：com.example/audit-context
 * 用途：在每個請求中攜帶企業稽核所需的上下文
 */
public final class AuditContextExtension {

    public static final String ID = "com.example/audit-context";

    /** Client：宣告支援並提供設定 */
    public static Map<String, Object> clientCapability() {
        return Map.of(ID, Map.of(
            "version", 1,
            "fields", List.of("costCenter", "ticketId")
        ));
    }

    /** Server：檢查是否已協商 */
    public static boolean isNegotiated(ClientCapabilities caps) {
        return caps.extensions().containsKey(ID);
    }

    /** Server：優雅降級——未協商時退回核心行為 */
    public static AuditContext extract(Map<String, Object> meta, ClientCapabilities caps) {
        if (!isNegotiated(caps)) {
            return AuditContext.unavailable();   // 不得因此讓請求失敗
        }
        @SuppressWarnings("unchecked")
        var ctx = (Map<String, Object>) meta.get(ID + "/context");
        return AuditContext.of(ctx);
    }
}
```

#### 12.5.3 設計檢查清單

- [ ] 識別碼使用組織實際擁有的網域反轉形式
- [ ] 設定物件內預留 `version` 或能力旗標，避免未來被迫換識別碼
- [ ] 明確定義**未協商時的降級行為**（退回核心行為或回傳適當錯誤）
- [ ] `_meta` 自訂鍵使用自有前綴，避開保留前綴規則
- [ ] 撰寫規格文件，說明方法、欄位、錯誤碼與安全考量
- [ ] 自訂錯誤碼配置於 `-32768`～`-32000` **之外**
- [ ] 提供至少一份參考實作與符規測試

---

## 第十三章：企業級部署與治理

### 13.1 無狀態水平擴展架構

#### 13.1.1 架構轉變

無狀態核心帶來的最直接效益，是 MCP 伺服器終於能以**一般 Web 服務**的方式部署。

```mermaid
graph TB
    subgraph OLD["2025-11-25：Sticky Session"]
        C1[Client] -->|Mcp-Session-Id| LB1[LB<br/>Session Affinity]
        LB1 --> P1[Pod A<br/>持有 Session 狀態]
        LB1 -.無法路由.-> P2[Pod B]
        P1 -.Pod 重啟即失效.-> X[對話中斷]
    end
```

```mermaid
graph TB
    subgraph NEW["2026-07-28：無狀態"]
        C2[Client] --> LB2[LB<br/>Round-Robin]
        LB2 --> Q1[Pod A]
        LB2 --> Q2[Pod B]
        LB2 --> Q3[Pod C]
        Q1 --> ST[(共用狀態儲存<br/>顯式握柄 / Task)]
        Q2 --> ST
        Q3 --> ST
    end
```

#### 13.1.2 Kubernetes 部署建議

| 面向 | 舊模式 | `2026-07-28` |
|------|--------|-------------|
| Service `sessionAffinity` | `ClientIP` | `None` |
| 工作負載型別 | 常需 StatefulSet | **Deployment** |
| 自動擴縮 | 受 Session 綁定限制 | HPA 依 CPU／RPS 自由擴縮 |
| 滾動更新 | 需長 `terminationGracePeriod` 等 Session 結束 | 僅需等待進行中的請求／串流結束 |
| Readiness 探針 | 常需自訂 | 一般 HTTP 探針即可 |

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mcp-server
spec:
  sessionAffinity: None          # 2026-07-28：不再需要 Sticky Session
  ports:
    - port: 443
      targetPort: 8080
  selector:
    app: mcp-server
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-server
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: server
          image: registry.example.com/mcp-server:2.0.0
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
          # SSE 串流可能長時間開啟，需給予足夠的優雅關閉時間
          lifecycle:
            preStop:
              exec:
                command: ["sh", "-c", "sleep 15"]
      terminationGracePeriodSeconds: 60
```

> **仍需注意**：無狀態指的是**協議層**無狀態。長效的 `subscriptions/listen`
> 串流仍會佔用連線與記憶體，滾動更新時必須妥善處理——
> 伺服器 **SHOULD** 在關閉前對訂閱回傳空的 `complete` 結果，讓用戶端得知需重連。

#### 13.1.3 容量規劃要素

| 指標 | 說明 | 建議上限來源 |
|------|------|-------------|
| 每 Pod 併發 SSE 串流數 | 主要記憶體與檔案描述符壓力來源 | 壓力測試實測 |
| 每租戶併發訂閱數 | 防止單一租戶耗盡資源 | 業務需求 + 公平性政策 |
| 請求 P95／P99 延遲 | 決定 HPA 觸發門檻 | SLO |
| MRTR 往返輪數分布 | 反映互動設計品質 | 觀測後優化 |
| Task 佇列深度 | 決定背景工作者數量 | 業務尖峰 |

---

### 13.2 API 閘道、WAF 與速率限制

#### 13.2.1 標頭路由帶來的能力

`2026-07-28` 將 `Mcp-Method`、`Mcp-Name` 與 `Mcp-Param-*` 提升至 HTTP 標頭，
使中介設備**無須解析 JSON Body** 即可套用策略——這是企業治理的關鍵前提。

```mermaid
graph LR
    C[Client] --> WAF[WAF<br/>依 Mcp-Method 套規則]
    WAF --> GW[API Gateway<br/>依 Mcp-Name 路由與限流]
    GW --> R1[讀取類工具池]
    GW --> R2[寫入類工具池<br/>更嚴格限流]
    GW --> R3[高成本工具池<br/>獨立配額]
```

#### 13.2.2 策略範例

**依方法分級限流**：

| `Mcp-Method` | 建議策略 |
|--------------|----------|
| `tools/list`、`prompts/list`、`resources/list` | 寬鬆；優先由 `ttlMs` 快取吸收 |
| `resources/read` | 中等；依 `Mcp-Name`（URI）細分 |
| `tools/call` | **嚴格**；依 `Mcp-Name`（工具名）分別配額 |
| `subscriptions/listen` | 依併發數限制而非速率限制 |
| `server/discover` | 寬鬆；可於閘道層直接快取回應 |

**Nginx 範例**：

```nginx
map $http_mcp_method $mcp_zone {
    default            "general";
    "tools/call"       "toolcall";
    "subscriptions/listen" "listen";
}

limit_req_zone $binary_remote_addr$http_mcp_name zone=toolcall:10m rate=10r/s;
limit_conn_zone $binary_remote_addr zone=listenconn:10m;

server {
    location /mcp {
        # 僅允許 POST（2026-07-28）
        limit_except POST { deny all; }

        limit_req zone=toolcall burst=20 nodelay;
        limit_conn listenconn 5;

        proxy_pass http://mcp_upstream;
        proxy_buffering off;              # SSE 必要設定
        proxy_read_timeout 3600s;
        proxy_set_header X-Accel-Buffering no;
    }
}
```

#### 13.2.3 閘道層的驗證責任

| 檢查 | 動作 |
|------|------|
| 缺少 `MCP-Protocol-Version` | 回傳 `400` |
| `Mcp-Method` 不在允許清單 | 回傳 `403` |
| `Mcp-Name` 指向已停用工具 | 回傳 `403` |
| Body 大小超過上限 | 回傳 `413` |
| `Origin` 不在白名單 | 回傳 `403` |

> **規範說明**：中介設備 **MUST** 在標頭驗證失敗時回傳 HTTP 錯誤，
> 但**不必**回傳 JSON-RPC 錯誤物件。伺服器本身則必須同時回傳 `400` 與 `-32020`。
>
> **⚠️ 重要**：閘道的標頭檢查是**縱深防禦**，不是唯一防線。
> 伺服器 **MUST** 自行再驗證一次標頭與 Body 的一致性，
> 因為攻擊者可能繞過閘道直接觸達後端。

---

### 13.3 授權硬化與身分治理

#### 13.3.1 分層授權模型

```mermaid
graph TB
    A[使用者身分<br/>企業 IdP / OIDC] --> B[Access Token<br/>受眾限定 + scope]
    B --> C[MCP Server 授權檢查]
    C --> D[工具層授權<br/>誰能呼叫哪個工具]
    C --> E[資料層授權<br/>能存取哪些資料列]
    C --> F[握柄授權<br/>握柄擁有權驗證]
```

#### 13.3.2 必要控制項

| 控制項 | 層級 | 說明 |
|--------|------|------|
| Token 受眾限定 | **MUST** | 為特定 MCP 伺服器簽發，防止 Token 轉用 |
| `iss` 驗證 | **MUST** | 兌換授權碼前驗證（RFC 9207） |
| 憑證按 issuer 分區 | **MUST** | 不跨 AS 重用用戶端憑證 |
| 握柄擁有權驗證 | **MUST** | 防止 IDOR |
| `requestState` 完整性 | **MUST** | HMAC/AEAD + principal + TTL |
| 最小 scope | **SHOULD** | 搭配分階段授權逐步提升 |
| Token 短效 + Refresh | **SHOULD** | 縮小外洩影響窗口 |
| 工具層 RBAC | **SHOULD** | 依角色控制可見與可呼叫的工具 |

#### 13.3.3 CIMD 導入建議

| 情境 | 建議 |
|------|------|
| 企業自建 MCP 用戶端 | 於企業網域託管 CIMD 文件，跨所有內部 AS 重用同一 `client_id` |
| 使用第三方用戶端 | 確認其支援 CIMD；不支援者評估 DCR 的維運成本 |
| 既有 DCR 部署 | 保留 DCR 作為回退，但規劃遷移至 CIMD；注意 DCR 已標記棄用 |

```json
// https://example.com/mcp-client.json
{
  "client_id": "https://example.com/mcp-client.json",
  "client_name": "Example Corp MCP Client",
  "client_uri": "https://example.com",
  "redirect_uris": ["https://example.com/oauth/callback"],
  "application_type": "native",
  "token_endpoint_auth_method": "private_key_jwt",
  "jwks_uri": "https://example.com/.well-known/jwks.json"
}
```

> **驗證要點**：文件內的 `client_id` **必須**與文件 URL 完全相同，
> 否則授權伺服器將拒絕。此設計可防止攻擊者託管冒名的中繼資料文件。

#### 13.3.4 JSON Schema 安全（SEP-2106）

升級至 JSON Schema 2020-12 帶來表達力，也帶來新的攻擊面：

| 風險 | 控制 |
|------|------|
| 網路 `$ref` 解析 | 實作 **MUST NOT** 自動解析網路 `$ref`；選用模式 **MUST** 預設關閉 |
| SSRF | 啟用時 **SHOULD** 強制主機白名單，拒絕 loopback／link-local／私有位址 |
| 資源耗盡 | **SHOULD** 限制 Schema 深度、子 Schema 數量與驗證時間預算 |
| 未解析的外部 `$ref` | **SHOULD** 拒絕該 Schema，而非以未驗證方式放行 |
| 稽核 | 啟用網路解析時 **SHOULD** 記錄所有被解析的 URI |

---

### 13.4 可觀測性與 OpenTelemetry

#### 13.4.1 追蹤上下文傳播

```mermaid
graph LR
    A[Host 應用] -->|traceparent| B[Client SDK]
    B -->|_meta.traceparent| C[MCP Server]
    C -->|傳播| D[下游 API / DB]
    A -.同一 Trace.-> E[(OTel Collector)]
    B -.-> E
    C -.-> E
    D -.-> E
```

`_meta` 保留 `traceparent`、`tracestate`、`baggage` 三個**免前綴**鍵，
使整條鏈路可組成單一 Span 樹。這是規範中極少數不遵守反向 DNS 前綴規則的例外，
目的正是為了與既有 W3C 標準無縫接軌。

#### 13.4.2 建議指標

| 指標 | 型別 | 用途 |
|------|------|------|
| `mcp.server.request.duration` | Histogram | 依 `Mcp-Method`、`Mcp-Name` 分維 |
| `mcp.server.request.errors` | Counter | 依錯誤碼分維（`-32020`／`-32021`／`-32022`） |
| `mcp.server.mrtr.rounds` | Histogram | MRTR 往返輪數，反映互動設計品質 |
| `mcp.server.subscriptions.active` | Gauge | 併發訂閱串流數 |
| `mcp.server.tasks.queue_depth` | Gauge | Tasks 佇列深度 |
| `mcp.server.era` | Counter | Modern／Legacy 流量比，驅動汰除決策 |
| `mcp.client.cache.hit_ratio` | Gauge | `ttlMs` 快取效益 |

#### 13.4.3 日誌策略

協議層 Logging 已棄用，企業應改採：

| 傳輸 | 診斷輸出位置 |
|------|-------------|
| stdio | `stderr`（**MUST NOT** 汙染 `stdout`） |
| Streamable HTTP | 標準應用日誌管線 + OTel Logs |

> **重要**：`_meta.io.modelcontextprotocol/logLevel` 只影響**協議層**的
> `notifications/message`。伺服器自身的營運日誌不應受用戶端指定的層級影響，
> 否則將形成由外部控制的日誌抑制風險。

#### 13.4.4 稽核要求

| 事件 | 必記欄位 |
|------|----------|
| 工具呼叫 | 主體、工具名、參數摘要（去敏）、結果狀態、trace id |
| 授權失敗 | 主體、目標資源、失敗原因、來源 IP |
| `requestState` 驗證失敗 | 主體、原請求指紋、失敗類型（**高優先告警**） |
| 握柄存取拒絕 | 主體、握柄 ID、擁有者（**高優先告警**） |
| 擴充協商 | 擴充識別碼、設定摘要 |

---

### 13.5 一致性驗證與 SDK 分級

#### 13.5.1 Conformance Suite

官方符規測試套件位於
[modelcontextprotocol/conformance](https://github.com/modelcontextprotocol/conformance)。
自 SEP-2484 起，**任何 SEP 必須先有對應的符規情境才能定案**——
這代表符規套件與規範是同步演進的，而非事後補寫。

| 用途 | 說明 |
|------|------|
| SDK 評級 | Tier 分級的客觀依據 |
| 自建實作驗證 | 企業自行實作傳輸層或用戶端時的驗收標準 |
| 供應商評估 | 導入第三方 MCP 伺服器時的技術盡職調查依據 |
| 回歸測試 | 納入 CI 管線，防止升級時破壞相容性 |

#### 13.5.2 建議的 CI 整合

```yaml
# 範例：於 CI 管線納入符規驗證
name: MCP Conformance
on: [push, pull_request]
jobs:
  conformance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 啟動待測 MCP Server
        run: ./gradlew bootRun &
      - name: 執行符規測試
        run: |
          npx @modelcontextprotocol/conformance \
            --url http://localhost:8080/mcp \
            --protocol-version 2026-07-28 \
            --report conformance-report.json
      - name: 上傳報告
        uses: actions/upload-artifact@v4
        with:
          name: conformance-report
          path: conformance-report.json
```

#### 13.5.3 SDK 選型治理

```mermaid
graph TD
    A[選擇 MCP SDK] --> B{是否為 Tier 1？}
    B -->|是| C[可假設規範窗口內跟進]
    B -->|否| D{規範發布後多久必須支援？}
    D -->|3 個月內| E[高風險<br/>評估自行補實作或改用 Tier 1]
    D -->|6 個月以上| F[可接受<br/>但需列入 ADR 風險項]
    C --> G[納入 CI 符規測試]
    E --> G
    F --> G
```

| 治理項目 | 建議 |
|----------|------|
| SDK 版本鎖定 | 明確鎖定次要版本，避免非預期的協議行為變動 |
| 規範版本宣告 | 於服務中繼資料與文件明列支援的協議版本 |
| 升級節奏 | 規範發布後 90 天內完成評估，180 天內完成升級 |
| 棄用追蹤 | 將棄用功能清單納入年度技術債盤點 |
| 符規報告 | 每次發布保留符規報告作為稽核證據 |

#### 13.5.4 生態現況參考

| 面向 | 現況 |
|------|------|
| SDK 下載量 | Tier 1 SDK 合計約每月數億次下載；TypeScript 與 Python SDK 累計均已突破十億次 |
| Tier 1 就緒度 | TypeScript、Python、Go、C# 於 `2026-07-28` 發布時即為 GA |
| Rust | Beta 階段 |
| 主要生態夥伴 | Anthropic、AWS、Cloudflare、Microsoft、Google Cloud、OpenAI、Figma、Netlify、Supabase、PostHog、Prefect、Honeycomb 等 |
| 里程碑追蹤 | [modelcontextprotocol milestone/6](https://github.com/modelcontextprotocol/modelcontextprotocol/milestone/6) |

---

## 附錄：檢查清單（Checklist）

### A. Server 開發檢查清單

#### A.1 基本功能

- [ ] Server 可以成功啟動
- [ ] 可以透過 STDIO 連接
- [ ] `server/discover` 正確回傳支援版本與 Server 能力（`2026-07-28` **MUST**）
- [ ] 每個請求都獨立解析 `_meta`，不依賴先前請求
- [ ] `tools/list` 回傳所有工具定義，且順序具確定性
- [ ] 所有工具有完整的 `inputSchema`（JSON Schema 2020-12）
- [ ] 工具描述清楚明確
- [ ] `tools/call` 正確處理所有工具，並回傳正確的 `resultType`

#### A.2 資源與提示詞（如適用）

- [ ] `resources/list` 回傳資源清單
- [ ] `resources/read` 正確讀取資源
- [ ] 資源 URI 格式正確
- [ ] `prompts/list` 回傳提示詞清單
- [ ] `prompts/get` 正確回傳提示詞內容

#### A.3 錯誤處理

- [ ] 處理無效參數並回傳有意義的錯誤
- [ ] 處理資源不存在的情況
- [ ] 處理權限被拒絕的情況
- [ ] 處理網路錯誤和超時
- [ ] 不會因為單一工具錯誤而崩潰

#### A.4 安全性

- [ ] 實作輸入驗證
- [ ] 路徑操作防止目錄遍歷
- [ ] SQL 操作使用參數化查詢
- [ ] 敏感資訊不會記錄在日誌
- [ ] API 金鑰從環境變數讀取
- [ ] 實作適當的認證機制（如適用）
- [ ] 實作速率限制（如適用）

#### A.5 效能

- [ ] 長時間操作有超時設定
- [ ] 資源重用（連接池等）
- [ ] 適當的快取策略
- [ ] 批次處理大量資料

---

### B. 部署檢查清單

#### B.1 環境準備

- [ ] Python 3.10+ 或 Node.js 18+ 已安裝
- [ ] 所有依賴套件已安裝
- [ ] 環境變數已正確設定
- [ ] 必要的認證資訊已配置
- [ ] 日誌目錄存在且可寫入

#### B.2 配置驗證

- [ ] Claude Desktop/Client 配置正確
- [ ] Server 路徑指向正確
- [ ] 環境變數傳遞正確
- [ ] 允許的目錄/資源已配置

#### B.3 連接測試

- [ ] 使用 MCP Inspector 測試連接
- [ ] 所有工具可以手動呼叫
- [ ] 資源可以正確讀取
- [ ] 錯誤情況有適當回應

#### B.4 監控設定

- [ ] 日誌輸出到 stderr
- [ ] 日誌等級可配置
- [ ] 效能指標收集（如適用）
- [ ] 錯誤追蹤設定（如適用）

---

### C. 程式碼審查檢查清單

#### C.1 程式碼品質

- [ ] 遵循 PEP 8 / ESLint 規範
- [ ] 函數有適當的型別標註
- [ ] 有完整的 docstring / JSDoc
- [ ] 沒有硬編碼的敏感資訊
- [ ] 沒有未使用的程式碼
- [ ] 異常處理適當

#### C.2 測試涵蓋

- [ ] 每個工具有單元測試
- [ ] 錯誤情況有測試
- [ ] 整合測試通過
- [ ] 測試涵蓋率 > 80%

#### C.3 文件完整

- [ ] README 說明如何安裝和使用
- [ ] 有 API 文件或工具說明
- [ ] 有配置範例
- [ ] 有常見問題說明

---

### D. 故障排除檢查清單

#### D.1 Server 無法啟動

- [ ] 檢查 Python/Node.js 版本
- [ ] 檢查依賴套件是否安裝
- [ ] 檢查環境變數是否設定
- [ ] 檢查程式碼是否有語法錯誤
- [ ] 查看 stderr 輸出

#### D.2 Client 無法連接

- [ ] 確認 Server 正在運行
- [ ] 檢查 Client 配置路徑
- [ ] 確認使用正確的傳輸方式
- [ ] 檢查防火牆設定（HTTP 模式）
- [ ] 使用 Inspector 測試

#### D.3 工具執行失敗

- [ ] 檢查參數格式是否正確
- [ ] 確認資源/檔案存在
- [ ] 檢查權限設定
- [ ] 查看 Server 日誌
- [ ] 使用 Inspector 手動測試

#### D.4 效能問題

- [ ] 檢查是否有 N+1 查詢
- [ ] 確認連接池正常運作
- [ ] 檢查快取是否生效
- [ ] 監控記憶體使用
- [ ] 檢查是否有資源洩漏

---

### E. 2026-07-28 遷移檢查清單

#### E.1 盤點階段

- [ ] 列出所有使用 `initialize` / `notifications/initialized` 的程式路徑
- [ ] 列出所有依賴 `Mcp-Session-Id` 或連線狀態的邏輯
- [ ] 列出所有使用 Sampling 的功能點
- [ ] 列出所有使用 Roots 的功能點
- [ ] 列出所有使用 `logging/setLevel` 的功能點
- [ ] 列出所有使用 `resources/subscribe` / `resources/unsubscribe` 的功能點
- [ ] 列出所有使用實驗性 Tasks API（`tasks/result`、`tasks/list`）的功能點
- [ ] 列出所有使用 `ping` 的功能點
- [ ] 確認目前 SDK 是否支援 `2026-07-28`；不支援則評估替代方案
- [ ] 確認是否需要服務 Legacy 用戶端（決定是否採雙時代）

#### E.2 Server 端改造

- [ ] 實作 `server/discover`（**MUST**）
- [ ] 移除 `initialize` / `notifications/initialized` 處理器
- [ ] 移除 Session 儲存與 `Mcp-Session-Id` 產生／驗證
- [ ] 從 `params._meta` 解析 `protocolVersion`（缺少→ `-32602` + HTTP `400`）
- [ ] 從 `params._meta` 解析 `clientCapabilities`（缺少→ `-32602` + HTTP `400`）
- [ ] 需要未宣告能力時回傳 `-32021` 並附 `data.requiredCapabilities`
- [ ] 不支援的版本回傳 `-32022` 並附 `data.supported`
- [ ] 每個 Result 加上 `resultType`
- [ ] 每個 Result 的 `_meta` 加上 `serverInfo`
- [ ] 將所有 Server-to-Client 請求改為 `InputRequiredResult`（MRTR）
- [ ] `requestState` 以 HMAC/AEAD 保護完整性
- [ ] `requestState` 內含 principal、TTL、原請求指紋（防重放）
- [ ] 一次性語意另行以伺服器端紀錄強制
- [ ] 實作 `subscriptions/listen`，第一則訊息為 `acknowledged`
- [ ] 訂閱串流上所有通知攜帶 `subscriptionId`
- [ ] `notifications/progress` / `message` 僅在請求回應串流上發送
- [ ] 關閉訂閱前回傳空的 `complete` 結果
- [ ] `tools/list` / `prompts/list` / `resources/list` / `resources/templates/list` / `resources/read` 加上 `ttlMs` 與 `cacheScope`
- [ ] `tools/list` 採確定性排序
- [ ] `GET /mcp`、`DELETE /mcp` 回傳 `405`
- [ ] 忽略 `Mcp-Session-Id` 與 `Last-Event-ID`
- [ ] 驗證 `MCP-Protocol-Version` / `Mcp-Method` / `Mcp-Name` 與 Body 一致（不符→ `400` + `-32020`）
- [ ] 驗證 `Origin` 標頭（不符→ `403`）
- [ ] SSE 回應加上 `X-Accel-Buffering: no`
- [ ] 長效串流加上 SSE 保活註解
- [ ] 以串流關閉判定取消，移除 HTTP 上的 `notifications/cancelled` 處理
- [ ] 移除 `-32000`～`-32019` 區間的自訂錯誤碼
- [ ] 資源不存在改回傳 `-32602`（不再用 `-32002`）
- [ ] 升級 `inputSchema` 至 JSON Schema 2020-12，並限制深度／驗證時間
- [ ] **MUST NOT** 自動解析網路 `$ref`

#### E.3 Client 端改造

- [ ] 每個請求注入完整的 `_meta` 協議欄位
- [ ] 實作 MRTR 重試迴圈（新 JSON-RPC id、原樣回傳 `requestState`、設輪數上限）
- [ ] 缺少 `resultType` 時視為 `complete`
- [ ] 無法辨識的 `resultType` 視為無效
- [ ] 改用 `subscriptions/listen` 取代 GET SSE 與 `resources/subscribe`
- [ ] 比對訂閱請求與 `acknowledged` 內容，處理未承接的類型
- [ ] 依 `subscriptionId` 解多工（stdio 必要）
- [ ] 支援 `x-mcp-header`，產生 `Mcp-Param-*` 標頭
- [ ] 實作 `=?base64?...?=` 標頭值編碼
- [ ] 排除違反 `x-mcp-header` 約束的工具定義並記錄警告
- [ ] 實作時代偵測與快取（HTTP 依 origin、stdio 依進程）
- [ ] `Accept` 標頭同時包含 `application/json` 與 `text/event-stream`
- [ ] DCR 時明確指定 `application_type`
- [ ] 驗證授權回應的 `iss`（RFC 9207）
- [ ] 用戶端憑證以 `issuer` 為鍵儲存，不跨 AS 重用
- [ ] 評估改用 CIMD 取代 DCR

#### E.4 棄用功能汰換

- [ ] Sampling → Server 端直接串接 LLM API（含金鑰管理與額度控管）
- [ ] Roots → 工具參數／Resource URI／伺服器組態（並補強路徑白名單與正規化）
- [ ] Logging → stdio 寫 `stderr`；結構化觀測改用 OpenTelemetry
- [ ] HTTP+SSE 傳輸 → Streamable HTTP
- [ ] DCR → CIMD
- [ ] 實驗性 Tasks → `io.modelcontextprotocol/tasks` 擴充

#### E.5 部署與治理

- [ ] Service `sessionAffinity` 改為 `None`
- [ ] 工作負載由 StatefulSet 改為 Deployment（如適用）
- [ ] 設定 HPA 與合理的 `terminationGracePeriodSeconds`
- [ ] 閘道層依 `Mcp-Method` / `Mcp-Name` 套用限流與存取策略
- [ ] 伺服器端**再次**驗證標頭（不倚賴閘道）
- [ ] 限制每租戶併發訂閱數
- [ ] 傳播 `traceparent` / `tracestate` / `baggage`
- [ ] 建立 Modern／Legacy 流量指標，驅動汰除決策
- [ ] 稽核 `requestState` 驗證失敗與握柄存取拒絕（高優先告警）

#### E.6 驗證

- [ ] 通過官方 Conformance Suite（`--protocol-version 2026-07-28`）
- [ ] 於 Round-Robin 測試環境驗證，刻意讓相關請求落在不同實例
- [ ] MRTR 端對端測試（含伺服器多次索取輸入的情境）
- [ ] 訂閱串流重連測試（stdio 需重送 `subscriptions/listen`）
- [ ] 標頭竄改測試（驗證回傳 `400` + `-32020`）
- [ ] `requestState` 竄改與重放測試
- [ ] 握柄跨主體存取測試（驗證 IDOR 防護）
- [ ] 雙時代部署下的 Legacy 用戶端回歸測試
- [ ] 將符規測試納入 CI 管線

---

## 結語

Model Context Protocol (MCP) 代表了 AI 應用整合的新典範。透過標準化的協議，開發者可以輕鬆地讓 AI 助手與各種資料來源和工具進行互動，同時保持安全性和可控性。

`2026-07-28` 是 MCP 走向**生產級基礎設施**的分水嶺。無狀態核心讓 MCP 伺服器
得以用一般 Web 服務的方式部署與擴展；MRTR 在不犧牲互動能力的前提下維持了無狀態性；
擴充框架讓核心保持精簡，同時容納快速演進的能力；授權硬化與生命週期政策，
則回應了企業導入時最關心的治理需求。

本教學手冊涵蓋了 MCP 的核心概念、技術架構、實作指南、最佳實踐、遷移路徑以及實際案例。希望這份資源能幫助您：

1. **理解 MCP 的價值** — 認識到為何需要標準化的 AI 整合協議
2. **掌握技術細節** — 深入了解傳輸層、JSON-RPC、核心原語與無狀態模型
3. **快速上手開發** — 透過範例程式碼建立自己的 MCP Server
4. **遵循最佳實踐** — 建立安全、高效、可維護的解決方案
5. **順利完成遷移** — 依循第十一章的步驟由 `2025-11-25` 升級至 `2026-07-28`
6. **達成企業級治理** — 以第十三章的架構與控制項支撐正式生產環境

隨著 MCP 生態系統的持續發展，我們期待看到更多創新的應用場景。歡迎加入 MCP 社群，一起推動 AI 工具整合的未來！

---

## 參考文獻與延伸閱讀

### 官方規範（2026-07-28）

| 主題 | 連結 |
|------|------|
| 規範首頁 | <https://modelcontextprotocol.io/specification/2026-07-28> |
| 變更紀錄 | <https://modelcontextprotocol.io/specification/2026-07-28/changelog> |
| 基礎協議 | <https://modelcontextprotocol.io/specification/2026-07-28/basic/index> |
| 版本管理與相容性 | <https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning> |
| MRTR 模式 | <https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr> |
| 訂閱模式 | <https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions> |
| Streamable HTTP 傳輸 | <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> |
| 用戶端註冊（CIMD／DCR） | <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration> |
| 棄用功能登錄 | <https://modelcontextprotocol.io/specification/2026-07-28/deprecated> |

### 治理與流程

| 主題 | 連結 |
|------|------|
| 功能生命週期政策 | <https://modelcontextprotocol.io/community/feature-lifecycle> |
| 擴充框架總覽 | <https://modelcontextprotocol.io/docs/extensions/overview> |
| Conformance Suite | <https://github.com/modelcontextprotocol/conformance> |
| `2026-07-28` 里程碑追蹤 | <https://github.com/modelcontextprotocol/modelcontextprotocol/milestone/6> |

### 官方擴充

| 擴充 | 連結 |
|------|------|
| Tasks | <https://modelcontextprotocol.io/extensions/tasks/overview> |
| MCP Apps | <https://modelcontextprotocol.io/extensions/apps/overview> |
| 企業託管授權（EMA） | <https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization> |

### 官方部落格

| 文章 | 連結 |
|------|------|
| `2026-07-28` 正式發布 | <https://blog.modelcontextprotocol.io/posts/2026-07-28/> |
| `2026-07-28` Release Candidate | <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/> |
| MCP 傳輸層的未來 | <https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/> |

### 社群分析

| 文章 | 連結 |
|------|------|
| MCP 2026-07-28：變更與遷移指南 | <https://aaif.io/blog/mcp-2026-07-28-whats-changing-and-how-to-migrate> |

### 相關標準

| 標準 | 說明 | 連結 |
|------|------|------|
| JSON-RPC 2.0 | 訊息協議基礎 | <https://www.jsonrpc.org/specification> |
| JSON Schema 2020-12 | 工具 Schema 方言 | <https://json-schema.org/specification-links#2020-12> |
| RFC 9110 | HTTP 語意（token 語法） | <https://www.rfc-editor.org/rfc/rfc9110> |
| RFC 9207 | OAuth 2.0 授權伺服器發行者識別 | <https://www.rfc-editor.org/rfc/rfc9207> |
| RFC 7591 | OAuth 2.0 動態用戶端註冊（已棄用於 MCP） | <https://www.rfc-editor.org/rfc/rfc7591> |
| RFC 5424 | Syslog 嚴重度層級 | <https://www.rfc-editor.org/rfc/rfc5424> |
| W3C Trace Context | `traceparent` / `tracestate` | <https://www.w3.org/TR/trace-context/> |
| W3C Baggage | `baggage` | <https://www.w3.org/TR/baggage/> |
| OpenTelemetry gen-ai/mcp | MCP 語意慣例 | <https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/> |
| OWASP Top 10 | 應用安全風險 | <https://owasp.org/www-project-top-ten/> |

### 主要 SEP 索引

| SEP | 主題 |
|-----|------|
| SEP-2575 / SEP-2567 | 無狀態核心與逐請求中繼資料 |
| SEP-2322 | 多輪往返請求（MRTR） |
| SEP-2260 | Server-initiated 請求的時機限制 |
| SEP-2243 | HTTP 標頭路由與 `x-mcp-header` |
| SEP-2549 | 快取提示（`ttlMs` / `cacheScope`） |
| SEP-2106 | JSON Schema 2020-12 |
| SEP-2133 | 擴充框架 |
| SEP-2663 | Tasks 擴充 |
| SEP-1865 | MCP Apps |
| SEP-2577 | Sampling / Roots / Logging 棄用 |
| SEP-2596 | 功能生命週期政策 |
| SEP-2484 | SEP 定案需具備符規情境 |
| SEP-414 | 分散式追蹤上下文 |
| SEP-2468 | 授權伺服器發行者驗證 |
| SEP-837 | DCR `application_type` |
| SEP-2352 | 用戶端憑證與 AS 綁定 |
| SEP-2350 | 分階段授權的範圍累積 |
| SEP-2351 | `.well-known` 探索路徑釐清 |
| SEP-2207 | OIDC 型 AS 的 Refresh Token |

---

| 項目 | 內容 |
|------|------|
| 文件版本 | 2.0 |
| 最後更新 | 2026-07-31 |
| 對應協議版本 | 2026-07-28 |
| 文件等級 | 企業標準技術白皮書 |

---

*（教學手冊完結）*

