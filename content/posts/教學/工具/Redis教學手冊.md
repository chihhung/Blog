+++
date = '2026-01-30T19:37:33+08:00'
draft = false
title = 'Redis教學手冊'
tags = ['教學', '工具', 'Redis']
categories = ['教學']
+++

# Redis教學手冊

| 項目 | 內容 |
| --- | --- |
| **文件版本** | 2.0 |
| **最後更新** | 2026 年 9 月 29 日 |
| **初版日期** | 2026 年 1 月 27 日（v1.0） |
| **適用版本** | Redis Open Source 8.10.x（最新修補版 8.10.2，2026-09-17）；向下相容說明涵蓋 7.2 / 7.4 / 8.0～8.8 |
| **適用對象** | 資深／中階後端工程師、系統架構師、SRE、DevOps、DBA、資安與稽核人員、新進同仁 |
| **文件定位** | 企業標準技術白皮書／內部標準教材 |
| **審閱週期** | 每季檢視一次；Redis 發布新 minor 版本或重大 CVE 時即時更新 |
| **Created by** | Eric Cheng |

> ⚠️ **v2.0 重大改版說明**：v1.0 以 Redis 7.2 為基準撰寫。自 2025 年 5 月起 Redis 進入 8.x 世代：Redis Stack 模組（JSON、Query Engine、Time Series、機率型資料結構）併入 Redis Open Source、授權新增 AGPLv3 選項、新增 Vector Set 與 Array 資料型態，並連續修補多個可導致遠端程式碼執行（RCE）的 CVE。本版以 **Redis 8.10.2** 為基準全面檢視每一章，修正 v1.0 約 40 處過時或錯誤內容，並新增第 14、15 章與附錄 B～E。完整更正清單請見[附錄 C：版本更新紀錄](#附錄-c版本更新紀錄)，逐項查證來源請見[附錄 D：查證紀錄](#附錄-d查證紀錄)。

<!-- TOC-AUTO-BEGIN -->

## 目錄

- [執行摘要](#執行摘要)
- [1. Redis 簡介與核心概念](#1-redis-簡介與核心概念)
  - [1.1 Redis 是什麼？適合解決什麼問題](#11-redis-是什麼適合解決什麼問題)
  - [1.2 In-Memory 設計原理](#12-in-memory-設計原理)
  - [1.3 單執行緒模型、I/O Threads 與效能優勢](#13-單執行緒模型io-threads-與效能優勢)
  - [1.4 Redis 與 RDBMS / NoSQL 的差異](#14-redis-與-rdbms--nosql-的差異)
  - [1.5 常見使用場景與反模式（Anti-pattern）](#15-常見使用場景與反模式anti-pattern)
  - [1.6 產品線、授權與生態系](#16-產品線授權與生態系)
  - [1.7 版本演進與 8.x 重點](#17-版本演進與-8x-重點)
  - [1.8 💡 本章實務建議](#18--本章實務建議)
- [2. Redis 系統架構設計](#2-redis-系統架構設計)
  - [2.1 Redis 架構總覽](#21-redis-架構總覽)
  - [2.2 Single Node 架構](#22-single-node-架構)
  - [2.3 Master / Replica（主從複寫）](#23-master--replica主從複寫)
  - [2.4 Sentinel 高可用架構](#24-sentinel-高可用架構)
  - [2.5 Redis Cluster 架構（Sharding）](#25-redis-cluster-架構sharding)
  - [2.6 架構選型建議](#26-架構選型建議)
  - [2.7 部署拓撲：多可用區、Kubernetes 與雲端託管](#27-部署拓撲多可用區kubernetes-與雲端託管)
  - [2.8 💡 本章實務建議](#28--本章實務建議)
- [3. Redis 安裝與部署](#3-redis-安裝與部署)
  - [3.1 Linux 安裝（建議版本）](#31-linux-安裝建議版本)
  - [3.2 Docker / Container 部署](#32-docker--container-部署)
  - [3.3 基本目錄結構說明](#33-基本目錄結構說明)
  - [3.4 Redis CLI 工具介紹](#34-redis-cli-工具介紹)
  - [3.5 常見安裝錯誤與排查方式](#35-常見安裝錯誤與排查方式)
  - [3.6 作業系統調校](#36-作業系統調校)
  - [3.7 Redis Insight 與圖形化工具](#37-redis-insight-與圖形化工具)
  - [3.8 💡 本章實務建議](#38--本章實務建議)
- [4. Redis 設定（redis.conf）](#4-redis-設定redisconf)
  - [4.1 基本設定說明](#41-基本設定說明)
  - [4.2 記憶體管理](#42-記憶體管理)
  - [4.3 Persistence 設定（RDB / AOF）](#43-persistence-設定rdb--aof)
  - [4.4 Replication 設定](#44-replication-設定)
  - [4.5 Cluster / Sentinel 設定重點](#45-cluster--sentinel-設定重點)
  - [4.6 資安相關設定](#46-資安相關設定)
  - [4.7 效能相關設定](#47-效能相關設定)
  - [4.8 生產環境設定範本](#48-生產環境設定範本)
  - [4.9 💡 本章實務建議](#49--本章實務建議)
- [5. Redis 資料結構與使用方式](#5-redis-資料結構與使用方式)
  - [5.1 String（字串）](#51-string字串)
  - [5.2 Hash（雜湊）](#52-hash雜湊)
  - [5.3 List（列表）](#53-list列表)
  - [5.4 Set（集合）](#54-set集合)
  - [5.5 Sorted Set（有序集合）](#55-sorted-set有序集合)
  - [5.6 進階資料結構](#56-進階資料結構)
  - [5.7 Array（陣列）](#57-array陣列)
  - [5.8 JSON（文件）](#58-json文件)
  - [5.9 機率型資料結構](#59-機率型資料結構)
  - [5.10 Time Series（時間序列）](#510-time-series時間序列)
  - [5.11 資料結構選型對照表](#511-資料結構選型對照表)
  - [5.12 💡 本章實務建議](#512--本章實務建議)
- [6. Redis 系統使用實戰](#6-redis-系統使用實戰)
  - [6.1 快取設計模式](#61-快取設計模式)
  - [6.2 TTL 與 Key 命名規範](#62-ttl-與-key-命名規範)
  - [6.3 Session 管理](#63-session-管理)
  - [6.4 Rate Limiting（速率限制）](#64-rate-limiting速率限制)
  - [6.5 分散式 Lock 與 RedLock 概念](#65-分散式-lock-與-redlock-概念)
  - [6.6 Queue / Pub-Sub / Stream 使用情境](#66-queue--pub-sub--stream-使用情境)
  - [6.7 快取穿透、擊穿與雪崩](#67-快取穿透擊穿與雪崩)
  - [6.8 Client-side Caching（客戶端快取）](#68-client-side-caching客戶端快取)
  - [6.9 交易、Lua Script 與 Functions](#69-交易lua-script-與-functions)
  - [6.10 💡 本章實務建議](#610--本章實務建議)
- [7. 應用系統如何串接 Redis](#7-應用系統如何串接-redis)
  - [7.1 系統整體架構說明](#71-系統整體架構說明)
  - [7.2 常見串接方式（Client Library）](#72-常見串接方式client-library)
  - [7.3 Java（Spring Boot + Redis）](#73-javaspring-boot--redis)
  - [7.4 Node.js / Python 串接概念](#74-nodejs--python-串接概念)
  - [7.5 Connection Pool 設計](#75-connection-pool-設計)
  - [7.6 Timeout / Retry / Fallback 設計](#76-timeout--retry--fallback-設計)
  - [7.7 Go 與 .NET 串接範例](#77-go-與-net-串接範例)
  - [7.8 RESP3 與 Client 相容性](#78-resp3-與-client-相容性)
  - [7.9 💡 本章實務建議](#79--本章實務建議)
- [8. Redis 維運與監控](#8-redis-維運與監控)
  - [8.1 常用監控指標](#81-常用監控指標)
  - [8.2 INFO 指令說明](#82-info-指令說明)
  - [8.3 慢查詢（Slow Log）](#83-慢查詢slow-log)
  - [8.4 Key 分析與 Big Key 問題](#84-key-分析與-big-key-問題)
  - [8.5 常見效能問題與處理方式](#85-常見效能問題與處理方式)
  - [8.6 Hot Key 偵測](#86-hot-key-偵測)
  - [8.7 延遲診斷](#87-延遲診斷)
  - [8.8 Prometheus + Grafana 監控](#88-prometheus--grafana-監控)
  - [8.9 備份與還原](#89-備份與還原)
  - [8.10 💡 本章實務建議](#810--本章實務建議)
- [9. Redis 系統升級與版本管理](#9-redis-系統升級與版本管理)
  - [9.1 升級前評估事項](#91-升級前評估事項)
  - [9.2 Rolling Upgrade 策略](#92-rolling-upgrade-策略)
  - [9.3 升級風險與回滾策略](#93-升級風險與回滾策略)
  - [9.4 舊資料相容性說明](#94-舊資料相容性說明)
  - [9.5 版本差異注意事項](#95-版本差異注意事項)
  - [9.6 支援週期與版本策略](#96-支援週期與版本策略)
  - [9.7 💡 本章實務建議](#97--本章實務建議)
- [10. 資安與風險控管](#10-資安與風險控管)
  - [10.1 Redis 常見資安風險](#101-redis-常見資安風險)
  - [10.2 內網 / 外網使用原則](#102-內網--外網使用原則)
  - [10.3 ACL 與權限控管](#103-acl-與權限控管)
  - [10.4 防止誤刪與資料風險](#104-防止誤刪與資料風險)
  - [10.5 實務安全建議](#105-實務安全建議)
  - [10.6 CVE 應變與修補管理](#106-cve-應變與修補管理)
  - [10.7 合規與稽核對應](#107-合規與稽核對應)
  - [10.8 💡 本章實務建議](#108--本章實務建議)
- [11. Redis Best Practices（最佳實務）](#11-redis-best-practices最佳實務)
  - [11.1 Key 設計原則](#111-key-設計原則)
  - [11.2 避免的設計地雷](#112-避免的設計地雷)
  - [11.3 高併發系統設計建議](#113-高併發系統設計建議)
  - [11.4 與資料庫搭配策略](#114-與資料庫搭配策略)
  - [11.5 團隊使用規範建議](#115-團隊使用規範建議)
  - [11.6 容量規劃與成本估算](#116-容量規劃與成本估算)
  - [11.7 服務等級目標（SLO）範例](#117-服務等級目標slo範例)
  - [11.8 💡 本章實務建議](#118--本章實務建議)
- [12. 常見問題與除錯（FAQ / Troubleshooting）](#12-常見問題與除錯faq--troubleshooting)
  - [12.1 Redis 掛掉怎麼辦](#121-redis-掛掉怎麼辦)
  - [12.2 記憶體暴增如何處理](#122-記憶體暴增如何處理)
  - [12.3 Hit Rate 過低的原因](#123-hit-rate-過低的原因)
  - [12.4 Replication 延遲處理](#124-replication-延遲處理)
  - [12.5 實務案例分享](#125-實務案例分享)
  - [12.6 Cluster 常見錯誤](#126-cluster-常見錯誤)
  - [12.7 升級後常見問題](#127-升級後常見問題)
  - [12.8 💡 本章實務建議](#128--本章實務建議)
- [13. 檢查清單（Checklist）](#13-檢查清單checklist)
  - [13.1 🔧 部署前檢查](#131--部署前檢查)
  - [13.2 📝 開發規範檢查](#132--開發規範檢查)
  - [13.3 🔍 日常維運檢查](#133--日常維運檢查)
  - [13.4 🚀 升級前檢查](#134--升級前檢查)
  - [13.5 🛡️ 資安檢查](#135--資安檢查)
  - [13.6 ✅ 上線前 Go-Live 檢查](#136--上線前-go-live-檢查)
- [14. Redis 8 Query Engine、向量搜尋與 AI 應用](#14-redis-8-query-engine向量搜尋與-ai-應用)
  - [14.1 Redis 8 內建功能概觀](#141-redis-8-內建功能概觀)
  - [14.2 Query Engine：二級索引與全文搜尋](#142-query-engine二級索引與全文搜尋)
  - [14.3 向量搜尋與混合搜尋（FT.HYBRID）](#143-向量搜尋與混合搜尋fthybrid)
  - [14.4 Vector Set](#144-vector-set)
  - [14.5 語意快取（Semantic Cache）](#145-語意快取semantic-cache)
  - [14.6 RAG 與 AI Agent 記憶架構](#146-rag-與-ai-agent-記憶架構)
  - [14.7 💡 本章實務建議](#147--本章實務建議)
- [15. 雲端託管與替代方案選型](#15-雲端託管與替代方案選型)
  - [15.1 部署模式總覽](#151-部署模式總覽)
  - [15.2 主要託管服務比較](#152-主要託管服務比較)
  - [15.3 Valkey 與相容替代方案](#153-valkey-與相容替代方案)
  - [15.4 選型決策流程](#154-選型決策流程)
  - [15.5 遷移注意事項](#155-遷移注意事項)
  - [15.6 💡 本章實務建議](#156--本章實務建議)
- [附錄 A：常用指令速查表](#附錄-a常用指令速查表)
  - [A.1 連線與認證](#a1-連線與認證)
  - [A.2 資料操作](#a2-資料操作)
  - [A.3 管理命令](#a3-管理命令)
  - [A.4 Cluster 命令](#a4-cluster-命令)
  - [A.5 Sentinel 命令](#a5-sentinel-命令)
  - [A.6 JSON／搜尋／向量命令](#a6-json搜尋向量命令)
- [附錄 B：版本新功能對照表](#附錄-b版本新功能對照表)
- [附錄 C：版本更新紀錄](#附錄-c版本更新紀錄)
  - [C.1 版本歷史](#c1-版本歷史)
  - [C.2 v1.0 → v2.0 更正清單](#c2-v10--v20-更正清單)
  - [C.3 v2.0 新增章節](#c3-v20-新增章節)
- [附錄 D：查證紀錄](#附錄-d查證紀錄)
  - [D.1 待確認事項](#d1-待確認事項)
- [附錄 E：參考資料](#附錄-e參考資料)

<!-- TOC-AUTO-END -->

## 執行摘要

Redis 是企業系統中最常見的記憶體內資料平台，承擔快取、Session、計數、排行榜、限流、分散式鎖、訊息串流，以及近年快速成長的向量搜尋與 AI 應用記憶層。本手冊以「可直接落地的企業標準」為目標，對開發、架構、維運、資安四種角色提供一致的規範。

**本版五項關鍵結論**：

| # | 結論 | 對企業的影響 | 對應章節 |
| --- | --- | --- | --- |
| 1 | 新系統一律以 **Redis 8.10.x**（或組織核准的 8.x 最新修補版）為基準；7.2 以下版本列入淘汰計畫 | 取得 I/O threads 效能提升、原子 slot 遷移、新資料型態與最新安全修補 | [1.7](#17-版本演進與-8x-重點)、[9.6](#96-支援週期與版本策略) |
| 2 | 2025-10 起的 Lua 系列 RCE（CVE-2025-49844，CVSS 10.0）影響所有啟用 Lua 的版本 | 必須完成修補；應用帳號預設禁止 `@scripting` 類命令 | [10.6](#106-cve-應變與修補管理) |
| 3 | `rename-command` 已被官方標示為不建議使用，改以 ACL 管控危險命令 | 設定範本全面改寫為 ACL 導向 | [4.6](#46-資安相關設定)、[10.3](#103-acl-與權限控管) |
| 4 | Redis 8.4 起提供 `SET ... IFEQ`、`DELEX`、`MSETEX`，8.8 提供 `INCREX` | 分散式鎖釋放、限流、批次寫入不再需要 Lua 腳本 | [6.4](#64-rate-limiting速率限制)、[6.5](#65-分散式-lock-與-redlock-概念) |
| 5 | 授權變更：7.2 以前 BSD-3；7.4～7.8 為 RSALv2/SSPLv1；8.x 為 RSALv2/SSPLv1/AGPLv3 三擇一 | 法務需確認選用授權；雲端託管與 Valkey 成為可評估的替代方案 | [1.6](#16-產品線授權與生態系)、[15](#15-雲端託管與替代方案選型) |

**閱讀路徑建議**：

| 角色 | 建議閱讀順序 |
| --- | --- |
| 新進同仁 | 1 → 3 → 5 → 6 → 13 |
| 應用開發工程師 | 1 → 5 → 6 → 7 → 11 → 13.2 |
| 系統架構師 | 1 → 2 → 11 → 14 → 15 |
| SRE／DevOps | 2 → 3 → 4 → 8 → 9 → 12 → 13 |
| 資安／稽核 | 4.6 → 10 → 13.5 → 附錄 D |

**本手冊標記慣例**：

| 標記 | 意義 |
| --- | --- |
| `> 🆕 **v2.0 新增**` | v2.0 新增的章節或段落 |
| `⚠️ **v2.0 更正**` | 修正 v1.0 錯誤或過時的內容 |
| `(8.4+)` | 該命令或參數自 Redis 8.4 起可用，以此類推 |
| ✅ / ❌ | 建議做法／不建議做法 |

---

## 1. Redis 簡介與核心概念

### 1.1 Redis 是什麼？適合解決什麼問題

**Redis（Remote Dictionary Server）** 是以記憶體為主要儲存媒介的鍵值（Key-Value）資料平台。與只能存放字串的傳統快取不同，Redis 在伺服器端直接提供多種資料結構與其原子操作，讓應用程式可以把「計數、排序、集合運算、去重、串流消費」等邏輯交給 Redis 以微秒等級完成。

從 Redis 8 開始，過去需另外安裝 Redis Stack 才能使用的 JSON、Query Engine（全文與向量搜尋）、Time Series、機率型資料結構全部內建於 Redis Open Source，因此 Redis 的定位已從「快取」擴大為「即時資料平台」。

| 使用場景 | 說明 | 主要資料結構／功能 |
| --- | --- | --- |
| **快取（Cache）** | 降低資料庫讀取壓力、縮短 API 回應時間 | String、Hash、JSON |
| **Session 管理** | 多節點應用共用登入狀態 | Hash、String |
| **計數器／排行榜** | 瀏覽數、按讚數、即時排名 | `INCR`、Sorted Set |
| **速率限制** | API 限流、防暴力破解 | `INCREX`（8.8+）、Sorted Set |
| **分散式鎖** | 跨服務的互斥控制 | `SET NX`、`DELEX`（8.4+） |
| **訊息串流** | 非同步處理、事件驅動 | Stream、Pub/Sub |
| **去重與統計** | UV、布隆過濾 | HyperLogLog、Bloom filter |
| **即時搜尋** | 商品搜尋、標籤篩選 | Query Engine（`FT.*`） |
| **AI 應用** | 語意快取、RAG 向量檢索、Agent 記憶 | Vector Set、向量索引、`FT.HYBRID` |

#### 💡 實務建議

```text
✅ 適合：讀多寫少、需要毫秒以下延遲、資料可由其他系統重建、或可接受秒級資料遺失的場景
✅ 適合：需要伺服器端原子操作的計數、排序、集合運算
❌ 不適合：資料量遠大於可負擔的記憶體、需要多表關聯查詢、需要跨 key 的強一致 ACID 交易
❌ 不適合：作為唯一且不可遺失資料的「系統記錄來源（System of Record）」
```

### 1.2 In-Memory 設計原理

Redis 將完整資料集保存在記憶體中，所有讀寫都在記憶體完成；磁碟只用於持久化（RDB 快照、AOF 日誌）與重啟後復原，不在一般讀取路徑上。

```mermaid
flowchart LR
    A[Client Request] --> B[Redis Server]
    B --> C[Memory<br/>主要資料儲存]
    B -.->|背景執行| D[Disk<br/>RDB / AOF 持久化]
    C -->|微秒級回應| B
```

**不同儲存媒介的隨機讀取延遲（數量級）**：

| 儲存媒介 | 典型延遲 | 相對記憶體 |
| --- | --- | --- |
| DRAM 記憶體 | 約 100 ns | 1× |
| NVMe SSD | 約 10～100 μs | 100～1,000× |
| SATA SSD | 約 100 μs | 約 1,000× |
| HDD | 約 5～10 ms | 約 100,000× |

> 💡 **設計含義**：Redis 的效能瓶頸通常不在 CPU 或記憶體，而在**網路往返（RTT）**與**單一命令的時間複雜度**。因此 Pipeline、批次命令與避免 O(N) 大範圍命令，比調整硬體更有效。

**記憶體效率的重要機制**：

| 機制 | 說明 |
| --- | --- |
| 緊湊編碼（listpack、intset） | 小型 Hash／List／Set／ZSet 以連續記憶體存放，大幅節省空間 |
| Compact hashes（8.10+） | 多個 schema 相同的 Hash 共用欄位名稱模板，減少重複欄位名稱的記憶體 |
| jemalloc | 預設記憶體配置器，降低碎片 |
| 主動碎片整理 | `activedefrag yes` 可在線上整理碎片（見 [4.7](#47-效能相關設定)） |

### 1.3 單執行緒模型、I/O Threads 與效能優勢

Redis 的**命令執行**由主執行緒依序處理，搭配事件迴圈（epoll／kqueue）服務大量連線；Redis 6.0 起可選擇啟用 **I/O threads** 分擔網路讀寫與協定解析，Redis 8.x 持續強化此機制。

```mermaid
flowchart TB
    subgraph IO["I/O Threads（可選，8.x 強化）"]
        T1[I/O Thread 1]
        T2[I/O Thread 2]
    end
    C1[Client 1] --> T1
    C2[Client 2] --> T1
    C3[Client 3] --> T2
    T1 --> M[Main Thread<br/>命令依序執行]
    T2 --> M
    M --> MEM[(Memory)]
    M -.->|背景| BG[Background Threads<br/>lazyfree / fsync / 關閉檔案]
```

**為什麼「命令單執行緒」仍然很快？**

1. **無鎖設計**：命令天然具原子性，不需資料結構層級的鎖。
2. **無上下文切換**：主執行緒不因搶鎖而阻塞。
3. **I/O 多工**：單一事件迴圈即可處理數萬條連線。
4. **記憶體操作**：絕大多數命令為 O(1) 或 O(log N)。

**8.x 效能相關演進**：

| 版本 | 改進 | 企業意義 |
| --- | --- | --- |
| 8.0 | I/O threads 架構重寫 | 多核心機器吞吐量顯著提升 |
| 8.4 | I/O threads 再優化（官方測試快取型負載 4 核心吞吐提升逾 30%）、命令前瞻預取（`lookahead`，預設 16） | Pipeline 與高併發場景受益 |
| 8.6 | Hash／Sorted Set 記憶體結構精簡 | 相同資料量記憶體下降 |
| 8.8 | `MGET`／`MSET`／`HGETALL` 批次預取 | 批次讀寫延遲降低 |

> ⚠️ **注意**：I/O threads 只平行化「網路 I/O」，**命令本身仍在主執行緒序列執行**。因此一個慢命令（例如對百萬元素集合執行 `SMEMBERS`）依然會阻塞所有連線。官方建議僅在 4 核心以上機器啟用，執行緒數約為「核心數減 1」。

### 1.4 Redis 與 RDBMS / NoSQL 的差異

| 特性 | Redis 8.x | RDBMS（PostgreSQL / MySQL） | 文件型 NoSQL（MongoDB） |
| --- | --- | --- | --- |
| 主要儲存 | 記憶體（磁碟僅持久化） | 磁碟＋緩衝池 | 磁碟＋快取 |
| 資料模型 | 多種資料結構、JSON、向量 | 關聯表 | 文件 |
| 查詢方式 | 命令式；Query Engine 提供索引查詢 | SQL | 查詢語言／聚合管線 |
| 交易 | `MULTI`/`EXEC`（無回滾）、Lua／Functions | 完整 ACID | 多文件交易（有限制） |
| 一致性 | 複寫為非同步；可用 `WAIT`／`WAITAOF` 提高保證 | 強一致 | 可調 |
| 延遲 | 次毫秒 | 毫秒 | 毫秒 |
| 容量成本 | 高（記憶體） | 低 | 中 |
| 典型角色 | 快取、即時計算、訊息、向量檢索 | 系統記錄來源 | 彈性結構資料 |

> 💡 **企業定位原則**：RDBMS 是「真相來源」，Redis 是「加速層與即時計算層」。即使開啟 AOF，也應假設 Redis 資料可能遺失最近 1 秒內的寫入。

### 1.5 常見使用場景與反模式（Anti-pattern）

#### ✅ 正確使用場景

```bash
# 1. 快取熱門商品（務必設定 TTL）
SET cache:product:1001 '{"name":"iPhone","price":35000}' EX 3600

# 2. Session（Hash 可部分更新欄位）
HSET session:abc123 userId 1 role admin
EXPIRE session:abc123 1800

# 3. 計數器
INCR stat:page:views:homepage

# 4. 排行榜
ZADD rank:game:season1 1000 "player1" 950 "player2"

# 5. 限流（8.8+，單一原子命令）
INCREX ratelimit:api:user:1001 BYINT 1 UBOUND 100 EX 60 ENX
```

#### ❌ 反模式（Anti-pattern）

| 反模式 | 問題 | 建議 |
| --- | --- | --- |
| 把 Redis 當唯一主資料庫 | 記憶體有限、非同步複寫可能遺失資料 | 以 RDBMS 為真相來源，Redis 作加速層 |
| 儲存大型物件（> 1 MB） | 阻塞主執行緒、網路頻寬暴增、複寫延遲 | 拆分、壓縮或改存物件儲存，Redis 只存索引 |
| 使用 `KEYS *` | O(N) 全表掃描，阻塞整個服務 | 使用 `SCAN` 系列；以 ACL 禁止 `KEYS` |
| 快取不設 TTL | 記憶體持續增長直到觸發淘汰或 OOM | 所有快取 key 必須有 TTL |
| Key 命名無規範 | 難以盤點、ACL 無法以前綴授權 | 採用 `{業務}:{模組}:{實體}:{識別碼}` |
| 在 Redis 執行長時間 Lua 腳本 | 腳本執行期間阻塞所有連線 | 腳本控制在毫秒內；優先改用 8.x 原生原子命令 |
| 對外網開放 6379 | 遭未授權存取、挖礦、資料勒索 | 僅內網存取＋ACL＋TLS（見 [10.2](#102-內網--外網使用原則)） |

### 1.6 產品線、授權與生態系

> 🆕 **v2.0 新增**

**Redis 產品線**：

| 產品 | 型態 | 主要差異 | 適用情境 |
| --- | --- | --- | --- |
| **Redis Open Source**（原 Community Edition） | 自建軟體 | 8.x 起內建 JSON、Query Engine、Time Series、機率型結構、Vector Set | 自建機房、Kubernetes、成本敏感 |
| **Redis Software**（原 Redis Enterprise） | 商業自建軟體 | 多租戶叢集管理、Active-Active（CRDT）跨區雙寫、Redis Flex（RAM＋SSD 分層）、官方支援 | 金融級 SLA、跨資料中心 |
| **Redis Cloud** | 全託管服務 | 在 AWS／GCP／Azure 上由 Redis 公司代管 | 不想自行維運 |

**授權沿革**（依 Redis 官方授權頁面）：

| 版本 | 授權 | 企業注意事項 |
| --- | --- | --- |
| 7.2.x 及以前 | BSD-3-Clause | 最寬鬆；可自由商用與再散布 |
| 7.4.x～7.8.x | RSALv2 或 SSPLv1（二擇一） | 均非 OSI 認可開源授權；禁止以此提供競爭性託管服務 |
| 8.0 及以後 | RSALv2、SSPLv1 或 **AGPLv3**（三擇一） | AGPLv3 為 OSI 認可開源授權，但具「網路使用即需公開修改原始碼」的傳染性條款 |

> 💡 **法務建議**：企業內部自用 Redis（未修改原始碼、未對外提供 Redis 託管服務）通常不受上述授權限制影響，但仍應由法務確認選用的授權並留存紀錄。若組織政策禁止 AGPL／SSPL 類授權，可評估 7.2 BSD 版本（需自行承擔 EOL 風險）、雲端託管服務，或 [Valkey](#153-valkey-與相容替代方案)。

**生態系關係**：

```mermaid
flowchart LR
    R72[Redis 7.2<br/>BSD-3] --> R74[Redis 7.4<br/>RSALv2/SSPLv1]
    R74 --> R8[Redis 8.x<br/>+AGPLv3]
    R72 -->|2024 分叉| VK[Valkey<br/>BSD-3<br/>Linux Foundation]
    VK --> VK9[Valkey 9.x]
    R8 --> RC[Redis Cloud]
    R8 --> RS[Redis Software]
    VK9 --> CLOUD[AWS ElastiCache／MemoryDB<br/>GCP Memorystore for Valkey]
```

### 1.7 版本演進與 8.x 重點

> 🆕 **v2.0 新增**

| 版本 | GA 時間 | 重點功能 |
| --- | --- | --- |
| 6.0 | 2020-04 | ACL、TLS、RESP3、I/O threads、Client-side caching |
| 6.2 | 2021-02 | `GETDEL`／`GETEX`、`ZRANGE` 統一語法、`LMOVE` |
| 7.0 | 2022-04 | Functions、Multi-part AOF、Sharded Pub/Sub、ACL selectors |
| 7.2 | 2023-08 | 最後一個 BSD 授權版本 |
| 7.4 | 2024-07 | Hash field expiration（`HEXPIRE` 等） |
| **8.0** | 2025-05 | Redis Stack 併入、Vector Set、`HGETEX`／`HSETEX`／`HGETDEL`、AGPLv3 |
| **8.2** | 2025-08 | `XDELEX`／`XACKDEL`、`BITOP` 新運算子、`CLUSTER SLOT-STATS`、SVS-VAMANA 向量索引 |
| **8.4** | 2025-11 | `SET IFEQ`／`DELEX`／`DIGEST`、`MSETEX`、`XREADGROUP CLAIM`、原子 slot 遷移、`FT.HYBRID` |
| **8.6** | 2026-02 | `XADD IDMP` 冪等寫入、`HOTKEYS`、`*-lrm` 淘汰策略、TLS 憑證自動認證 |
| **8.8** | 2026-05 | Array 資料型態、`INCREX`、`XNACK`、Hash 欄位層級通知 |
| **8.10** | 2026-07 | Compact hashes、`HIMPORT`、`LMOVEM`、`SUNIONCARD`／`SDIFFCARD`、`BACKUP` 線上備份 |

> 完整對照表請見[附錄 B：版本新功能對照表](#附錄-b版本新功能對照表)。

### 1.8 💡 本章實務建議

- 以「Redis 是加速層與即時計算層，而非唯一真相來源」作為架構審查的第一條檢查點。
- 新專案直接採用 Redis 8.10.x；需要 JSON、搜尋、向量或時序功能時，不必再另外部署 Redis Stack。
- 在架構文件中記錄所選的授權（RSALv2／SSPLv1／AGPLv3）與版本，作為稽核證據。
- 評估效能時優先檢查「網路往返次數」與「命令時間複雜度」，而非直接加大硬體。

---

## 2. Redis 系統架構設計

### 2.1 Redis 架構總覽

Redis Open Source 提供四種部署型態，依「可用性」與「擴充性」需求逐步演進：

```mermaid
flowchart LR
    A[Single Node] -->|需要資料備援| B[Primary-Replica]
    B -->|需要自動故障轉移| C[Sentinel]
    B -->|資料量或寫入量超過單機| D[Cluster]
```

| 型態 | 可用性 | 寫入擴充 | 讀取擴充 | 故障轉移 | 多 key 操作限制 |
| --- | --- | --- | --- | --- | --- |
| Single Node | 低 | 否 | 否 | 無 | 無 |
| Primary-Replica | 中 | 否 | 是 | 手動 | 無 |
| Sentinel | 高 | 否 | 是 | 自動 | 無 |
| Cluster | 高 | 是 | 是 | 自動 | 需同一 hash slot |

> ⚠️ **v2.0 更正**：官方文件已改用 **primary／replica** 稱呼（`replicaof`、`replica-*` 參數）；舊稱 master／slave 僅保留於部分相容命令與 `INFO` 欄位（如 `master_link_status`）。本手冊敘述採新稱呼，命令與欄位名稱維持原樣。

### 2.2 Single Node 架構

**適用場景**：開發測試環境、可接受短暫停機與資料可重建的快取。

```text
┌─────────────────────────────────┐
│          Application            │
└─────────────┬───────────────────┘
              │ TCP 6379 / TLS
              ▼
┌─────────────────────────────────┐
│        Redis Server             │
│   ┌─────────────────────────┐   │
│   │      Memory Data        │   │
│   └─────────────────────────┘   │
│   ┌─────────────────────────┐   │
│   │  RDB / AOF (Disk)       │   │
│   └─────────────────────────┘   │
└─────────────────────────────────┘
```

| 優點 | 缺點 |
| --- | --- |
| 架構簡單、易維運 | 單點故障 |
| 成本最低 | 容量受單機記憶體限制 |
| 無複寫延遲問題 | 重啟期間服務中斷，大資料集載入需數分鐘 |

### 2.3 Master / Replica（主從複寫）

**適用場景**：需要讀取擴充與資料熱備援，但可接受人工切換。

```mermaid
flowchart TB
    A[Application] -->|Write| M[Primary]
    A -->|Read| R1[Replica 1]
    A -->|Read| R2[Replica 2]
    M -->|非同步複寫| R1
    M -->|非同步複寫| R2
```

**Replica 端設定範例**：

```bash
# redis.conf（Replica）
replicaof 192.168.1.100 6379
masteruser repl_user              # 以 ACL 使用者進行複寫認證（建議）
masterauth your_replication_password
replica-read-only yes
```

**複寫機制重點**：

| 項目 | 說明 |
| --- | --- |
| 預設模式 | 非同步複寫；Primary 不等待 Replica 確認即回應客戶端 |
| 部分重同步（PSYNC） | 短暫斷線後依 replication backlog 補齊差異，避免全量同步 |
| 全量同步 | backlog 不足或 replication ID 不符時觸發；Primary 會 fork 產生 RDB |
| 無碟複寫 | `repl-diskless-sync yes`（預設）直接經 socket 傳送 RDB |
| 同步寫入保證 | `WAIT numreplicas timeout` 等待指定數量 Replica 確認；`WAITAOF` 等待 AOF fsync |

> ⚠️ **注意**：`WAIT` 只能降低資料遺失機率，**不會讓 Redis 變成強一致系統**；故障轉移時仍可能選到尚未收到最新寫入的 Replica。

### 2.4 Sentinel 高可用架構

**適用場景**：資料量可放入單機、需要自動故障轉移的生產環境。

```mermaid
flowchart TB
    subgraph Sentinels["Sentinel 仲裁群（奇數，跨主機／可用區）"]
        S1[Sentinel 1]
        S2[Sentinel 2]
        S3[Sentinel 3]
    end
    S1 -.->|監控| M[Primary]
    S2 -.->|監控| M
    S3 -.->|監控| M
    M -->|複寫| R1[Replica 1]
    M -->|複寫| R2[Replica 2]
    APP[Application] -->|1. 詢問目前 Primary| S1
    APP -->|2. 連線| M
```

**Sentinel 設定範例**：

```bash
# sentinel.conf
sentinel monitor mymaster 192.168.1.100 6379 2
sentinel auth-user mymaster sentinel_user
sentinel auth-pass mymaster your_password
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1
sentinel resolve-hostnames yes      # 使用主機名稱（Kubernetes／DNS 環境）
sentinel announce-hostnames yes
```

**故障轉移流程**：

1. 單一 Sentinel 在 `down-after-milliseconds` 內無法取得回應 → 標記**主觀下線（SDOWN）**。
2. 達到 `quorum`（上例為 2）個 Sentinel 同意 → 標記**客觀下線（ODOWN）**。
3. Sentinel 之間選出領導者（需多數 Sentinel 同意）。
4. 領導者挑選最合適的 Replica（優先權、複寫 offset、run ID）升為新 Primary。
5. 其他 Replica 改為複寫新 Primary；客戶端透過 Sentinel 取得新位址。

**Sentinel 部署建議**：

- 至少 **3 個**、且為奇數，分散在不同主機或可用區。
- `quorum` 通常設為 Sentinel 數量的過半數。
- `down-after-milliseconds` 不宜過短（網路抖動會誤判），生產環境常見 5～30 秒。
- 客戶端必須使用支援 Sentinel 的連線方式，**不可**寫死 Primary IP。

### 2.5 Redis Cluster 架構（Sharding）

**適用場景**：資料量或寫入吞吐超過單機、需要水平擴充。

```mermaid
flowchart TB
    APP[Cluster-aware Client<br/>快取 slot 對應表] --> M1
    APP --> M2
    APP --> M3
    subgraph S1["Shard 1：slot 0-5460"]
        M1[Primary 1] --> R1[Replica 1]
    end
    subgraph S2["Shard 2：slot 5461-10922"]
        M2[Primary 2] --> R2[Replica 2]
    end
    subgraph S3["Shard 3：slot 10923-16383"]
        M3[Primary 3] --> R3[Replica 3]
    end
```

**Cluster 核心特性**：

| 特性 | 說明 |
| --- | --- |
| Hash Slot | 固定 16,384 個 slot；`slot = CRC16(key) mod 16384` |
| 最小規模 | 至少 3 個 Primary；生產環境建議每個 Primary 至少 1 個 Replica（共 6 節點） |
| 重新導向 | 客戶端存取錯誤節點時收到 `MOVED`（永久）或 `ASK`（遷移中）回應 |
| 多 key 命令 | 所有 key 必須落在同一 slot，否則回傳 `CROSSSLOT`；可用 hash tag `{...}` 強制同 slot |
| 資料庫編號 | 只支援 db 0（`SELECT` 其他編號會失敗） |
| Pub/Sub | 一般 Pub/Sub 會廣播至所有節點；大量訊息建議改用 Sharded Pub/Sub（`SPUBLISH`，7.0+） |

**Hash Slot 與 Hash Tag**：

```bash
CLUSTER KEYSLOT user:1001
# (integer) 某個 0～16383 的值

# 使用 hash tag：只有大括號內的字串參與 slot 計算
CLUSTER KEYSLOT {user:1001}:profile
CLUSTER KEYSLOT {user:1001}:orders
# 兩者結果相同 → 可在同一個 MULTI／Lua／MSET 中操作
```

> 🆕 **v2.0 新增：原子 slot 遷移（8.4+）**
>
> 傳統 reshard 以 `MIGRATE` 逐 key 搬移，遷移中的 key 會產生 `ASK` 重新導向，大 key 可能造成延遲尖峰。Redis 8.4 新增 `CLUSTER MIGRATION` 命令，以「整批 slot 原子切換」方式遷移；Redis 8.10 起 `redis-cli --cluster reshard` 與 `rebalance` 預設改用此伺服器端原子遷移。
>
> 另外，8.2 起可用 `CLUSTER SLOT-STATS` 查詢每個 slot 的 key 數、CPU 時間與網路 I/O，協助找出熱點 slot；8.6 新增 `cluster-slot-stats-enabled` 參數，用於控制要收集哪些 slot 統計項目。

### 2.6 架構選型建議

| 情境 | 建議架構 | 理由 |
| --- | --- | --- |
| 開發／測試環境 | Single Node（Docker） | 簡單、成本低 |
| 小型生產系統（< 25 GB、寫入 < 5 萬 ops/s） | Primary + 2 Replica + 3 Sentinel | 自動故障轉移、架構單純 |
| 讀取量大、資料可放入單機 | Sentinel + 多 Replica（讀寫分離） | 讀取水平擴充 |
| 大型系統（資料量或寫入量超過單機） | Redis Cluster（每 shard 1～2 Replica） | 寫入與容量水平擴充 |
| 跨資料中心雙活 | Redis Software／Redis Cloud Active-Active | Open Source 沒有內建多主跨區同步 |
| 跨資料中心災備（單向） | 主站 Cluster + 異地冷備（RDB／BACKUP 異地保存）或託管服務的跨區複寫 | 以 RPO／RTO 決定 |

> ⚠️ **v2.0 更正**：v1.0 將「跨機房部署」寫為「Cluster + 異地複寫」。Redis Open Source **沒有**內建跨叢集複寫或多主寫入；跨區雙活需使用 Redis Software／Redis Cloud 的 Active-Active（CRDT），或由應用層雙寫並自行處理衝突。

**💡 單機容量經驗值**：單一 Redis 節點的資料集建議控制在 **25 GB 以內**，以縮短 fork、全量同步與重啟載入時間；超過時優先考慮 Cluster 分片。此為業界經驗值，實際上限依硬體與 RTO 要求評估。

#### 💡 決策流程圖

```mermaid
flowchart TD
    A[開始選型] --> B{資料量或寫入量<br/>超過單機?}
    B -->|是| C[Redis Cluster]
    B -->|否| D{可接受停機?}
    D -->|是| E[Single Node]
    D -->|否| F{需要自動故障轉移?}
    F -->|否| G[Primary-Replica]
    F -->|是| H[Sentinel]
    C --> I{需要跨區雙活?}
    H --> I
    I -->|是| J[Redis Software／Cloud<br/>Active-Active]
    I -->|否| K[完成]
```

### 2.7 部署拓撲：多可用區、Kubernetes 與雲端託管

> 🆕 **v2.0 新增**

**多可用區（Multi-AZ）拓撲原則**：

| 原則 | 說明 |
| --- | --- |
| Primary 與其 Replica 分散在不同 AZ | 單一 AZ 故障時仍有完整資料副本 |
| Sentinel 分散在至少 3 個 AZ | 避免單一 AZ 故障導致無法形成多數決 |
| Cluster 每個 shard 的 Primary 平均分散 | 避免單一 AZ 故障同時失去多個 Primary |
| 跨 AZ 延遲納入 SLO | 跨 AZ 往返通常增加約 0.5～2 ms |

**Kubernetes 部署考量**：

| 項目 | 建議 |
| --- | --- |
| 工作負載型態 | 使用 StatefulSet（穩定網路識別與 PVC）；生產環境優先評估 Operator（如 Redis Enterprise Operator 或社群 Operator） |
| 儲存 | 使用低延遲 PV（SSD）；純快取可關閉持久化以省去 PV |
| 資源 | 設定 memory `requests` = `limits`，並讓 `maxmemory` 約為 limit 的 70～80%，保留 fork 與緩衝空間 |
| 反親和性 | Primary 與 Replica 以 `podAntiAffinity` 分散節點／AZ |
| 主機名稱 | Sentinel 啟用 `resolve-hostnames`／`announce-hostnames`；Cluster 設定 `cluster-announce-hostname` |
| PodDisruptionBudget | 確保維護期間不會同時驅逐同一 shard 的多個副本 |
| 探針 | liveness 使用 `redis-cli PING`；readiness 可加上複寫狀態或載入完成檢查（`loading:0`） |

**託管服務**：若組織不具備 Redis 維運能力，優先評估雲端託管服務，詳見[第 15 章](#15-雲端託管與替代方案選型)。

### 2.8 💡 本章實務建議

- 生產環境最低配置為 **Primary + 2 Replica + 3 Sentinel**，或 **3 shard × (1 Primary + 1 Replica)** 的 Cluster。
- 設計 Cluster key 時就規劃好 hash tag，避免上線後才遇到 `CROSSSLOT`。
- 不要依賴 `WAIT` 取得強一致；需要強一致的資料留在 RDBMS。
- Sentinel、Cluster 都要求客戶端「拓撲感知」，選用與設定 client 時一併驗證故障轉移行為（見 [7.6](#76-timeout--retry--fallback-設計)）。

---

## 3. Redis 安裝與部署

### 3.1 Linux 安裝（建議版本）

⚠️ **v2.0 更正**：建議版本由 v1.0 的「Redis 7.2.x」更新為 **Redis 8.10.x**（2026-09-17 最新修補版為 8.10.2）。若組織因授權或相容性須留在舊版，至少升級到該分支最新的安全修補版（例如 8.2.10、7.4.11、7.2.16）。

**官方測試過的作業系統（Redis 8.10）**：

| 發行版 | 版本 |
| --- | --- |
| Ubuntu | 22.04、24.04、26.04 |
| Debian | 12（Bookworm）、13（Trixie） |
| Rocky Linux／AlmaLinux | 8.10、9.7、10.1 |
| Alpine | 3.23 |
| macOS | 14、15、26（Intel 與 Apple Silicon） |

> Windows 沒有原生 Redis Open Source；請使用 Docker Desktop（Linux 容器）或 WSL2。

#### 方式一：官方套件庫（建議）

**Ubuntu／Debian（APT）**：

```bash
sudo apt-get install -y lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" \
  | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install -y redis

# 啟動並設為開機自動啟動
sudo systemctl enable --now redis-server
redis-cli INFO server | grep redis_version
```

**Rocky Linux／AlmaLinux（RPM）**：

```bash
# /etc/yum.repos.d/redis.repo（Rocky/Alma 9 使用 rockylinux9，8 使用 rockylinux8）
sudo tee /etc/yum.repos.d/redis.repo <<'EOF'
[Redis]
name=Redis
baseurl=http://packages.redis.io/rpm/rockylinux9
enabled=1
gpgcheck=1
EOF

curl -fsSL https://packages.redis.io/gpg > /tmp/redis.key
sudo rpm --import /tmp/redis.key
sudo yum install -y redis
sudo systemctl enable --now redis
```

> 💡 **版本鎖定**：生產環境請用 `apt-mark hold redis`（APT）或 `dnf versionlock`（RPM）鎖定版本，避免例行 `apt upgrade` 在非維護時段升級 Redis。

#### 方式二：從原始碼編譯

適用於需要自訂編譯選項（例如 TLS、特定 CPU 最佳化）或離線環境。

```bash
# 1. 安裝相依套件（Debian/Ubuntu）
sudo apt-get install -y build-essential pkg-config libssl-dev tcl

# 2. 下載指定版本原始碼（避免 redis-stable 在不同時間取得不同版本）
REDIS_VERSION=8.10.2
wget https://github.com/redis/redis/archive/refs/tags/${REDIS_VERSION}.tar.gz -O redis-${REDIS_VERSION}.tar.gz
sha256sum redis-${REDIS_VERSION}.tar.gz   # 與官方發布之雜湊比對
tar xzf redis-${REDIS_VERSION}.tar.gz
cd redis-${REDIS_VERSION}

# 3. 編譯（啟用 TLS）
make BUILD_TLS=yes -j"$(nproc)"
make test            # 可選：執行測試（耗時）

# 4. 安裝
sudo make install PREFIX=/opt/redis

# 5. 驗證
/opt/redis/bin/redis-server --version
```

> ⚠️ 自行編譯的 8.x 預設只包含核心功能；若需要 JSON、Query Engine、Time Series 等內建模組，需依官方「Build from source」文件加上對應建置參數，或直接使用官方套件／Docker 映像。

### 3.2 Docker / Container 部署

#### 單節點部署

```bash
# 使用明確版本標籤（不要使用 latest）
docker pull redis:8.10.2

docker run -d \
  --name redis \
  -p 127.0.0.1:6379:6379 \
  -v /data/redis:/data \
  -v /etc/redis/redis.conf:/usr/local/etc/redis/redis.conf:ro \
  -v /etc/redis/users.acl:/usr/local/etc/redis/users.acl:ro \
  --restart unless-stopped \
  redis:8.10.2 redis-server /usr/local/etc/redis/redis.conf
```

> 💡 `-p 127.0.0.1:6379:6379` 只綁定本機介面，避免 Docker 自動開放 iptables 規則讓外部網路可直接連線。

#### Docker Compose 範例

⚠️ **v2.0 更正**：Docker Compose v2 已不使用最上層的 `version:` 欄位（保留時只會出現警告），範例已移除。

```yaml
# compose.yaml
services:
  redis:
    image: redis:8.10.2
    container_name: redis
    ports:
      - "127.0.0.1:6379:6379"
    volumes:
      - redis-data:/data
      - ./redis.conf:/usr/local/etc/redis/redis.conf:ro
      - ./users.acl:/usr/local/etc/redis/users.acl:ro
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    restart: unless-stopped
    healthcheck:
      # 使用 REDISCLI_AUTH 環境變數避免密碼出現在程序清單
      test: ["CMD-SHELL", "REDISCLI_AUTH=$$REDIS_HEALTH_PASSWORD redis-cli --user healthcheck PING | grep PONG"]
      interval: 10s
      timeout: 5s
      retries: 3
    environment:
      REDIS_HEALTH_PASSWORD: ${REDIS_HEALTH_PASSWORD}
    ulimits:
      nofile:
        soft: 65535
        hard: 65535

volumes:
  redis-data:
```

#### Docker Compose - Sentinel 架構

```yaml
# compose-sentinel.yaml（示範用；生產環境請分散到不同主機）
services:
  redis-primary:
    image: redis:8.10.2
    command: ["redis-server", "--requirepass", "${REDIS_PASSWORD}", "--masterauth", "${REDIS_PASSWORD}"]
    volumes:
      - primary-data:/data

  redis-replica-1:
    image: redis:8.10.2
    command: ["redis-server", "--replicaof", "redis-primary", "6379",
              "--masterauth", "${REDIS_PASSWORD}", "--requirepass", "${REDIS_PASSWORD}"]
    depends_on: [redis-primary]

  redis-replica-2:
    image: redis:8.10.2
    command: ["redis-server", "--replicaof", "redis-primary", "6379",
              "--masterauth", "${REDIS_PASSWORD}", "--requirepass", "${REDIS_PASSWORD}"]
    depends_on: [redis-primary]

  sentinel-1: &sentinel
    image: redis:8.10.2
    command: ["redis-sentinel", "/etc/redis/sentinel.conf"]
    # Sentinel 會改寫設定檔，因此每個 Sentinel 需各自一份可寫入的副本
    volumes:
      - ./sentinel-1.conf:/etc/redis/sentinel.conf
    depends_on: [redis-primary, redis-replica-1, redis-replica-2]

  sentinel-2:
    <<: *sentinel
    volumes:
      - ./sentinel-2.conf:/etc/redis/sentinel.conf

  sentinel-3:
    <<: *sentinel
    volumes:
      - ./sentinel-3.conf:/etc/redis/sentinel.conf

volumes:
  primary-data:
```

```bash
# sentinel-N.conf（三份內容相同、檔案各自獨立）
sentinel resolve-hostnames yes
sentinel announce-hostnames yes
sentinel monitor mymaster redis-primary 6379 2
sentinel auth-pass mymaster ${REDIS_PASSWORD}
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1
```

> ⚠️ **v2.0 更正**：v1.0 的 Sentinel 範例只有 1 個 Sentinel，無法達到 quorum 2，故障轉移不會發生。Sentinel 至少需要 3 個，且每個 Sentinel 必須有自己的可寫入設定檔。`sentinel.conf` 不會展開環境變數，實際部署時請以範本工具（envsubst、Helm）替換密碼。

### 3.3 基本目錄結構說明

⚠️ **v2.0 更正**：Redis 7.0 起 AOF 改為多部分（Multi-part AOF），不再是單一 `appendonly.aof` 檔案，而是一個目錄（預設 `appendonlydir/`）。

```text
/etc/redis/
├── redis.conf              # 主要設定檔
├── sentinel.conf           # Sentinel 設定檔（Sentinel 會自行改寫）
├── users.acl               # ACL 使用者定義（aclfile）
└── tls/                    # TLS 憑證與私鑰（權限 600）

/var/lib/redis/              # dir 參數指定的工作目錄
├── dump.rdb                # RDB 快照
├── appendonlydir/          # Multi-part AOF 目錄（appenddirname）
│   ├── appendonly.aof.1.base.rdb    # BASE：重寫時產生的基底（RDB 格式）
│   ├── appendonly.aof.1.incr.aof    # INCR：之後的增量寫入
│   └── appendonly.aof.manifest      # 清單：記錄目前有效的檔案組合
├── backupdir/              # BACKUP 命令輸出目錄（8.10+，backupdirname）
└── nodes.conf              # Cluster 節點設定（Cluster 自動維護，勿手動修改）

/var/log/redis/
└── redis-server.log        # 日誌

/run/redis/
└── redis-server.pid        # PID 檔
```

### 3.4 Redis CLI 工具介紹

#### 基本連線

```bash
# 本地連線
redis-cli

# 遠端連線
redis-cli -h 192.168.1.100 -p 6379

# 以 ACL 使用者登入（密碼透過環境變數，避免出現在 shell 歷史與程序清單）
export REDISCLI_AUTH='your_password'
redis-cli -h 192.168.1.100 --user app_user

# 或使用互動式輸入密碼
redis-cli -h 192.168.1.100 --user app_user --askpass

# URI 形式（TLS 使用 rediss://）
redis-cli -u rediss://app_user@redis.example.com:6380/0 --cacert ca.crt

# 使用 RESP3
redis-cli -3

# Cluster 模式（自動跟隨 MOVED/ASK）
redis-cli -c -h 192.168.1.101
```

> ⚠️ **v2.0 更正**：v1.0 範例使用 `-a your_password`，密碼會留在 shell 歷史與 `ps` 輸出中。官方建議改用 `REDISCLI_AUTH` 環境變數或 `--askpass`。

#### 常用命令

```bash
127.0.0.1:6379> PING
PONG

127.0.0.1:6379> INFO server           # 版本、執行時間、設定檔路徑
127.0.0.1:6379> INFO memory           # 記憶體使用
127.0.0.1:6379> INFO keysizes         # key 大小分布（8.x）

# 非阻塞掃描 key（生產環境不可使用 KEYS）
127.0.0.1:6379> SCAN 0 MATCH "user:*" COUNT 100

127.0.0.1:6379> SLOWLOG GET 10        # 慢查詢
127.0.0.1:6379> LATENCY DOCTOR        # 延遲診斷報告
127.0.0.1:6379> CLIENT LIST           # 目前連線
127.0.0.1:6379> MEMORY USAGE user:1001

# MONITOR 會輸出所有命令並顯著降低吞吐量，生產環境僅限短時間診斷
127.0.0.1:6379> MONITOR
```

#### 常用命令列模式

| 模式 | 用途 |
| --- | --- |
| `redis-cli --stat` | 每秒滾動顯示 key 數、記憶體、連線、請求數 |
| `redis-cli --bigkeys` | 找出元素數量最多的 key（依型別） |
| `redis-cli --memkeys` | 找出記憶體占用最大的 key |
| `redis-cli --keystats` | 合併 bigkeys 與 memkeys，並輸出分布統計 |
| `redis-cli --hotkeys` | 以 LFU 資訊找熱點 key（需 `maxmemory-policy` 為 `*-lfu`） |
| `redis-cli --latency` / `--latency-history` | 持續量測 PING 延遲；8.10 起可加 `--latency-percentiles 50,99,99.9` |
| `redis-cli --intrinsic-latency 30` | 在 Redis 主機上量測系統本身的排程延遲基線 |
| `redis-cli --rdb /backup/dump.rdb` | 從遠端節點取得一份 RDB 備份 |
| `redis-cli --cluster check host:port` | 檢查 Cluster slot 分配與節點狀態 |

### 3.5 常見安裝錯誤與排查方式

| 錯誤訊息 | 可能原因 | 解決方式 |
| --- | --- | --- |
| `Could not connect to Redis` | 服務未啟動、`bind` 未包含該介面、防火牆阻擋 | 檢查服務狀態、`bind` 設定與防火牆 |
| `DENIED Redis is running in protected mode` | 未設定認證且未明確綁定介面 | 設定 ACL／密碼並明確 `bind`，**不要**關閉 protected-mode 了事 |
| `NOAUTH Authentication required` | 未認證 | 以 `AUTH user pass` 或 `--user` 認證 |
| `WRONGPASS invalid username-password pair or user is disabled` | 帳密錯誤或使用者停用 | 檢查 ACL 設定 |
| `OOM command not allowed when used memory > 'maxmemory'` | 記憶體達上限且策略為 `noeviction` | 調整 `maxmemory`／淘汰策略、清理資料或擴容 |
| `MISCONF Redis is configured to save RDB snapshots, but it's currently unable to persist to disk` | RDB 寫入失敗（磁碟滿、權限、fork 失敗） | 檢查磁碟空間、目錄權限、`vm.overcommit_memory` |
| `Can't open the log file` | 日誌目錄權限 | `chown redis:redis /var/log/redis` |
| `WARNING overcommit_memory is set to 0!` | 核心參數未調整 | 設定 `vm.overcommit_memory = 1`（見 [3.6](#36-作業系統調校)） |

#### 排查步驟

```bash
# 1. 檢查服務狀態
sudo systemctl status redis-server

# 2. 查看日誌（或 journalctl）
sudo tail -f /var/log/redis/redis-server.log
sudo journalctl -u redis-server -n 200 --no-pager

# 3. 檢查 Port 監聽（netstat 已被多數發行版淘汰）
sudo ss -tlnp | grep 6379

# 4. 測試連線
redis-cli -h 127.0.0.1 PING

# 5. 驗證設定檔：以前景模式啟動，錯誤會直接輸出到終端機
sudo -u redis redis-server /etc/redis/redis.conf --daemonize no
```

> ⚠️ **v2.0 更正**：v1.0 以 `redis-server ... --test-memory 256` 「檢查設定檔語法」並不正確；`--test-memory` 是記憶體硬體測試工具。Redis 沒有獨立的設定語法檢查指令，建議在測試環境以前景模式啟動驗證。

### 3.6 作業系統調校

> 🆕 **v2.0 新增**

| 項目 | 建議值 | 原因 |
| --- | --- | --- |
| `vm.overcommit_memory` | `1` | 避免 `BGSAVE`／AOF 重寫 fork 時因記憶體估算失敗 |
| Transparent Huge Pages | `never`（或 `madvise`） | THP 會放大 fork 後 copy-on-write 成本並造成延遲尖峰 |
| `net.core.somaxconn` | ≥ `tcp-backlog`（預設 511） | 避免高併發連線被核心截斷 |
| 檔案描述子上限 | ≥ `maxclients` + 32 | 每個連線占用一個 fd |
| Swap | 關閉或 `vm.swappiness=1` | Redis 被換出到 swap 會造成嚴重延遲 |
| 時鐘同步 | 啟用 chrony／NTP | TTL、Sentinel 判斷與稽核日誌需要正確時間 |

```bash
# /etc/sysctl.d/99-redis.conf
vm.overcommit_memory = 1
net.core.somaxconn = 1024
vm.swappiness = 1

sudo sysctl --system

# 關閉 THP（需寫入開機腳本或 systemd unit 使其永久生效）
echo never | sudo tee /sys/kernel/mm/transparent_hugepage/enabled

# systemd 服務的檔案描述子上限
sudo systemctl edit redis-server
# [Service]
# LimitNOFILE=65535
```

### 3.7 Redis Insight 與圖形化工具

> 🆕 **v2.0 新增**

| 工具 | 用途 | 注意事項 |
| --- | --- | --- |
| **Redis Insight** | 官方免費 GUI：瀏覽資料、執行命令、分析記憶體、Profiler、慢查詢、JSON／搜尋／向量資料視覺化 | 生產環境連線請使用唯讀 ACL 帳號；Profiler 底層使用 `MONITOR`，僅短時間使用 |
| `redis-cli` | 標準命令列工具 | 用於腳本化維運 |
| Prometheus + Grafana | 長期監控與告警 | 見 [8.8](#88-prometheus--grafana-監控) |

### 3.8 💡 本章實務建議

- 使用官方套件庫或官方 Docker 映像，並**鎖定明確版本號**；禁止在生產環境使用 `latest` 標籤。
- 安裝後第一件事：設定 ACL、`bind`、`protected-mode`，並完成 [3.6](#36-作業系統調校) 的核心調校。
- CLI 認證一律使用 `REDISCLI_AUTH` 或 `--askpass`，不要把密碼寫在命令列參數。
- Sentinel 至少 3 個節點，且各自擁有可寫入的設定檔。

---

## 4. Redis 設定（redis.conf）

> 設定可透過三種方式生效：`redis.conf` 檔案、啟動參數（`redis-server --port 6380`）、執行期 `CONFIG SET`。以 `CONFIG SET` 修改後，務必執行 `CONFIG REWRITE` 寫回設定檔，否則重啟後遺失。部分參數（如 `appenddirname`、`backupdirname`、`io-threads`）只能在啟動時設定。

### 4.1 基本設定說明

```bash
# 綁定介面：只列出需要服務的內網 IP 與 loopback
bind 127.0.0.1 -::1 192.168.1.100

# 保護模式：未設定認證且綁定所有介面時，只接受本機連線
protected-mode yes

# 監聽 Port（純 TLS 部署時設為 0，見 4.6）
port 6379

# 連線佇列長度（需搭配 net.core.somaxconn）
tcp-backlog 511

# 閒置連線逾時（秒），0 表示不逾時；建議由連線池管理
timeout 0

# TCP keepalive（秒），用於偵測斷線的客戶端
tcp-keepalive 300

# 使用 systemd 管理時不需 daemonize，交由 supervised 處理
daemonize no
supervised systemd

pidfile /run/redis/redis-server.pid

# 日誌等級：debug、verbose、notice、warning、nothing
loglevel notice
logfile /var/log/redis/redis-server.log

# 資料庫數量（Cluster 模式只能使用 db 0）
databases 16

# 工作目錄（RDB、AOF 目錄、BACKUP 目錄的根目錄）
dir /var/lib/redis
```

### 4.2 記憶體管理

```bash
# 最大記憶體：建議為可用實體記憶體的 60～75%
# 需保留：fork 時 copy-on-write、複寫緩衝、客戶端輸出緩衝、碎片
maxmemory 12gb

# 淘汰策略（預設 noeviction）
maxmemory-policy allkeys-lru

# LRU/LFU 取樣數，越大越精準但耗 CPU
maxmemory-samples 5
```

**淘汰策略說明**：

| 策略 | 淘汰範圍 | 演算法 | 適用場景 |
| --- | --- | --- | --- |
| `noeviction`（預設） | 不淘汰，寫入回傳 OOM 錯誤 | — | 不可遺失資料（如佇列、鎖） |
| `allkeys-lru` | 所有 key | 最久未**存取** | **純快取首選** |
| `allkeys-lfu` | 所有 key | 最少**存取次數** | 有明顯熱點的快取 |
| `allkeys-lrm` 🆕（8.6+） | 所有 key | 最久未**修改** | 讀多但需保留近期寫入的資料 |
| `volatile-lru` | 有 TTL 的 key | 最久未存取 | 快取與持久資料混放 |
| `volatile-lfu` | 有 TTL 的 key | 最少存取次數 | 同上，熱點明顯 |
| `volatile-lrm` 🆕（8.6+） | 有 TTL 的 key | 最久未修改 | 同上 |
| `volatile-ttl` | 有 TTL 的 key | TTL 最短者優先 | TTL 反映價值的場景 |
| `allkeys-random` | 所有 key | 隨機 | 存取均勻 |
| `volatile-random` | 有 TTL 的 key | 隨機 | 特殊場景 |

> 💡 **選擇原則**：「純快取」選 `allkeys-lru` 或 `allkeys-lfu`；「快取＋不可遺失資料混放」應**拆成不同實例**，而不是依賴 `volatile-*`，因為不可遺失資料在記憶體不足時仍會讓寫入失敗。

**其他記憶體相關設定**：

```bash
# 背景釋放大型物件，避免 DEL 大 key 阻塞主執行緒
lazyfree-lazy-eviction yes
lazyfree-lazy-expire yes
lazyfree-lazy-server-del yes
lazyfree-lazy-user-del yes      # 讓 DEL 行為等同 UNLINK
replica-lazy-flush yes

# 客戶端輸出緩衝限制（防止慢消費者撐爆記憶體）
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit replica 512mb 128mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
```

### 4.3 Persistence 設定（RDB / AOF）

#### RDB（快照）設定

⚠️ **v2.0 更正**：Redis 7.0 起預設儲存條件已改為 `3600 1 300 100 60 10000`，v1.0 列出的 `900 1 / 300 10 / 60 10000` 為舊版預設值。

```bash
# 儲存條件（任一條件滿足即觸發 BGSAVE）
save 3600 1 300 100 60 10000
#   3600 秒內至少 1 次修改
#   300 秒內至少 100 次修改
#   60 秒內至少 10000 次修改

# 純快取且不需重啟保留資料時可停用
# save ""

dbfilename dump.rdb
rdbcompression yes
rdbchecksum yes

# RDB 寫入失敗時拒絕寫入（避免在無法持久化時繼續接受資料）
stop-writes-on-bgsave-error yes
```

#### AOF（追加日誌）設定

```bash
appendonly yes

# 7.0+：AOF 以目錄形式保存 BASE、INCR 與 manifest
appenddirname "appendonlydir"
appendfilename "appendonly.aof"   # 目錄內檔案的名稱前綴

# 同步策略
# always   : 每批寫入都 fsync（最安全，最慢）
# everysec : 每秒 fsync（預設、建議；最多遺失約 1 秒資料）
# no       : 交由作業系統（最快，最不安全）
appendfsync everysec

# AOF 重寫期間暫停 fsync，可降低延遲但故障時可能遺失更多資料
no-appendfsync-on-rewrite no

# 自動重寫觸發條件
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

# BASE 檔使用 RDB 格式（預設 yes，建議保留）
aof-use-rdb-preamble yes

# 尾端被截斷時仍載入（預設 yes）
aof-load-truncated yes

# 8.4+：啟動時自動修復尾端損壞的最大位元組數（預設 0 = 不自動修復）
# aof-load-corrupt-tail-max-size 0
```

#### 💡 持久化策略建議

| 資料性質 | 建議策略 | RPO（可能遺失） |
| --- | --- | --- |
| 純快取、可從 DB 重建 | 關閉持久化，或僅 RDB 以加速重啟 | 全部／數分鐘 |
| Session、計數器 | RDB + AOF `everysec` | 約 1 秒 |
| 佇列、Stream、鎖狀態 | RDB + AOF `everysec`，並搭配 Replica 與 `WAITAOF` | 約 1 秒（`WAITAOF` 可再降低） |
| 金融級不可遺失 | 不應以 Redis 為唯一儲存；寫入 RDBMS 後再同步 | — |

```mermaid
flowchart TD
    A[選擇持久化策略] --> B{資料可由其他系統重建?}
    B -->|是| C{需要快速重啟?}
    C -->|否| D[關閉持久化]
    C -->|是| E[僅 RDB]
    B -->|否| F[RDB + AOF everysec]
    F --> G{需要更低 RPO?}
    G -->|是| H[加上 Replica + WAITAOF<br/>或改存 RDBMS]
    G -->|否| I[完成]
```

### 4.4 Replication 設定

**Primary 端**：

```bash
# 以 ACL 建立專用的複寫帳號（見 10.3）
# user repl_user on >ReplPass!2026 +psync +replconf +ping

# 至少 N 個 Replica 延遲 < M 秒時才接受寫入（降低腦裂時的資料遺失）
min-replicas-to-write 1
min-replicas-max-lag 10

# 無碟複寫（預設 yes）
repl-diskless-sync yes
repl-diskless-sync-delay 5

# 複寫積壓緩衝區：越大越能避免斷線後全量同步
# 經驗公式：寫入量(MB/s) × 可容忍斷線秒數 × 2
repl-backlog-size 256mb
repl-backlog-ttl 3600
```

**Replica 端**：

```bash
replicaof 192.168.1.100 6379
masteruser repl_user
masterauth ReplPass!2026

replica-read-only yes

# 與 Primary 斷線時仍回應讀取（可能是舊資料）；要求嚴格可設 no
replica-serve-stale-data yes

repl-timeout 60

# Sentinel 選主優先權：數字越小越優先，0 表示永不升為 Primary
replica-priority 100

# 全量同步時的無碟載入策略：disabled／on-empty-db／swapdb／flushdb（8.6+）
repl-diskless-load disabled
```

### 4.5 Cluster / Sentinel 設定重點

#### Cluster 設定

```bash
cluster-enabled yes

# 節點狀態檔（Redis 自動維護，不要手動編輯）
cluster-config-file nodes-6379.conf

# 節點失聯多久視為故障（毫秒）
cluster-node-timeout 15000

# Replica 與 Primary 失聯超過 (node-timeout × factor) 時，不參與故障轉移（避免用太舊的資料升主）
cluster-replica-validity-factor 10

# Primary 至少保留幾個 Replica 後，多餘的 Replica 才會自動遷移到孤兒 Primary
cluster-migration-barrier 1

# 部分 slot 無人負責時是否停止整個叢集服務
cluster-require-full-coverage yes

# 叢集故障時是否允許讀取（在 require-full-coverage no 時有意義）
cluster-allow-reads-when-down no

# 容器／NAT 環境需宣告對外位址
# cluster-announce-hostname redis-0.redis.svc.cluster.local
# cluster-preferred-endpoint-type hostname
```

> ⚠️ **v2.0 更正**：v1.0 將 `cluster-replica-validity-factor` 解釋為「至少需要多少 Replica 才允許 Master 失敗」並不正確；該描述屬於 `cluster-migration-barrier`。`cluster-replica-validity-factor` 用於判斷 Replica 的資料是否「新到足以升主」。

#### Sentinel 設定

```bash
sentinel monitor mymaster 192.168.1.100 6379 2
sentinel auth-user mymaster sentinel_user
sentinel auth-pass mymaster your_password

# 主觀下線判定時間（毫秒）
sentinel down-after-milliseconds mymaster 5000

# 故障轉移逾時
sentinel failover-timeout mymaster 60000

# 故障轉移後同時重新同步新 Primary 的 Replica 數量
sentinel parallel-syncs mymaster 1

# Sentinel 本身也應啟用認證
requirepass sentinel_admin_password
# 或使用 Sentinel ACL（6.2+）
# user sentinel_admin on >SentinelPass!2026 allcommands
```

### 4.6 資安相關設定

```bash
# 1. 網路：只綁定必要介面
bind 127.0.0.1 -::1 192.168.1.100
protected-mode yes

# 2. 認證：以 ACL 檔案管理使用者（不要只依賴 requirepass）
aclfile /etc/redis/users.acl

# 3. 高風險功能預設關閉（以下皆為預設值，列出以示明確）
enable-debug-command no
enable-protected-configs no
enable-module-command no

# 4. 危險命令：以 ACL 限制，不再使用 rename-command
#   （見 10.3 與 10.4）

# 5. TLS（見 10.5）
# port 0
# tls-port 6379
```

⚠️ **v2.0 更正**：v1.0 以 `rename-command` 停用或改名危險命令。Redis 官方安全文件已將此方法標示為**已不建議使用（deprecated），未來可能移除**，`redis.conf` 內也註明「盡量避免使用，改以 ACL 自 default 使用者移除命令」。此外，改名後的命令名稱會寫入 AOF 並傳給 Replica，若各節點設定不一致會造成複寫或載入失敗。

#### ACL 設定範例

```bash
# /etc/redis/users.acl
# 關閉 default 使用者（或至少設定強密碼並限縮權限）
user default off

# 管理員：完整權限，只允許維運人員使用
user admin on >Adm!n-Very-Long-Pass-2026 ~* &* +@all

# 應用程式：只能存取自己的前綴，禁止危險、管理與腳本類命令
user app_order on >App0rder-Pass-2026 ~order:* ~cache:order:* &order:* +@all -@dangerous -@admin -@scripting

# 唯讀帳號（報表、Redis Insight 檢視）
user readonly on >Read0nly-Pass-2026 ~* &* +@read +@connection -@dangerous

# 監控帳號（Prometheus exporter）
user monitor on >M0nitor-Pass-2026 +client|list +info +ping +config|get +latency +slowlog|get +cluster|info +cluster|nodes
```

```bash
# 載入與驗證
ACL LOAD
ACL LIST
ACL DRYRUN app_order SET order:1001 x      # 預期 OK
ACL DRYRUN app_order FLUSHALL              # 預期錯誤
```

### 4.7 效能相關設定

> 🆕 **v2.0 新增**

```bash
# I/O threads：4 核心以上機器才建議啟用，數量約為核心數 - 1（上限依官方建議）
io-threads 4

# 8.4+：命令前瞻預取深度（預設 16），通常不需調整
# lookahead 16

# 主動碎片整理（jemalloc 才支援）
activedefrag yes
active-defrag-ignore-bytes 100mb
active-defrag-threshold-lower 10
active-defrag-threshold-upper 100
active-defrag-cycle-min 1
active-defrag-cycle-max 25

# 慢查詢記錄
slowlog-log-slower-than 10000    # 微秒（10 ms）
slowlog-max-len 1024
# 8.8+：避免慢查詢紀錄保存過長參數
# slowlog-entry-max-argc 32
# slowlog-entry-max-string-len 128

# 延遲監控：記錄超過門檻（毫秒）的事件，供 LATENCY 命令分析
latency-monitor-threshold 100

# 小型集合的緊湊編碼門檻（預設值通常已合適）
hash-max-listpack-entries 128
hash-max-listpack-value 64
zset-max-listpack-entries 128
zset-max-listpack-value 64
set-max-intset-entries 512
```

> ⚠️ `io-threads` 為啟動期參數；啟用後請以實際負載壓測（`redis-benchmark --threads`、`memtier_benchmark`）驗證，不要只依直覺調高。

### 4.8 生產環境設定範本

> 🆕 **v2.0 新增**：以下為「快取＋Session」用途、8 核心 / 16 GB 主機的起始範本，請依實際情境調整。

```bash
# ===== 網路 =====
bind 127.0.0.1 -::1 10.0.1.10
protected-mode yes
port 0
tls-port 6379
tcp-backlog 1024
tcp-keepalive 300
timeout 0
maxclients 10000

# ===== TLS =====
tls-cert-file /etc/redis/tls/redis.crt
tls-key-file /etc/redis/tls/redis.key
tls-ca-cert-file /etc/redis/tls/ca.crt
tls-auth-clients optional
tls-replication yes
tls-protocols "TLSv1.2 TLSv1.3"

# ===== 認證 =====
aclfile /etc/redis/users.acl

# ===== 程序 =====
daemonize no
supervised systemd
loglevel notice
logfile /var/log/redis/redis-server.log
dir /var/lib/redis

# ===== 記憶體 =====
maxmemory 10gb
maxmemory-policy allkeys-lfu
lazyfree-lazy-eviction yes
lazyfree-lazy-expire yes
lazyfree-lazy-server-del yes
lazyfree-lazy-user-del yes
activedefrag yes

# ===== 持久化 =====
save 3600 1 300 100 60 10000
appendonly yes
appendfsync everysec
aof-use-rdb-preamble yes

# ===== 效能與診斷 =====
io-threads 4
slowlog-log-slower-than 10000
slowlog-max-len 1024
latency-monitor-threshold 100
```

### 4.9 💡 本章實務建議

- 所有設定檔納入版本控制（Git），並以 Ansible／Helm 等工具部署，禁止手動修改後遺忘 `CONFIG REWRITE`。
- 危險命令一律以 ACL 管控；`rename-command` 僅保留於無法升級的舊版本。
- `maxmemory` 不可省略；未設定時 Redis 會用到系統記憶體耗盡並被 OOM Killer 終止。
- 快取與不可遺失資料分屬不同實例，各自設定淘汰與持久化策略。

---

## 5. Redis 資料結構與使用方式

> 本章每個資料結構依「說明 → 使用情境 → 常用指令 → 實務範例 → 不建議的使用方式」編排。標示 `(x.y+)` 的命令需該版本以上才能使用；企業內若同時存在多個 Redis 版本，請以最舊版本為準選用命令。

### 5.1 String（字串）

**說明**：最基本的型別，可儲存文字、數字或任意二進位資料，單一值上限 512 MB（實務上應遠小於此）。數值字串可直接進行原子加減。

#### 使用情境

- 快取（序列化後的物件）
- 計數器、ID 產生器
- 分散式鎖
- 限流計數

#### 常用指令

```bash
# 設定值
SET key value
SET key value EX 3600                 # 秒
SET key value PX 3600000              # 毫秒
SET key value EXAT 1790000000         # 指定到期的 Unix 時間（6.2+）
SET key value NX                      # 只在 key 不存在時設定
SET key value XX                      # 只在 key 存在時設定
SET key value KEEPTTL                 # 覆寫值但保留原 TTL（6.0+）
SET key newvalue GET                  # 設定並回傳舊值（取代 GETSET）

# 條件式寫入（8.4+）：比較目前值後才寫入，取代「GET 比對後 SET」的 Lua 腳本
SET key newvalue IFEQ oldvalue        # 目前值等於 oldvalue 才寫入
SET key newvalue IFNE oldvalue        # 目前值不等於 oldvalue 才寫入（key 不存在也會建立）
DIGEST key                            # 取得值的 XXH3 雜湊（十六進位字串）
SET key newvalue IFDEQ <digest>       # 以雜湊比對，適合大型值

# 取得值
GET key
GETEX key EX 60                       # 取得並重設 TTL（6.2+）
GETDEL key                            # 取得並刪除（6.2+）
MGET key1 key2 key3

# 批次設定
MSET key1 v1 key2 v2
MSETEX 2 key1 v1 key2 v2 EX 300       # 批次設定並共用 TTL（8.4+）
MSETEX 2 key1 v1 key2 v2 NX EX 300    # 全部不存在才寫入

# 條件式刪除（8.4+）
DELEX key IFEQ expected_value         # 值相符才刪除，回傳 1／0

# 數值操作
INCR counter
INCRBY counter 10
INCRBYFLOAT counter 1.5
DECR counter
DECRBY counter 10

# 進階遞增（8.8+）：遞增＋上下限＋TTL 一次完成，回傳 [新值, 實際增量]
INCREX counter BYINT 1 UBOUND 100 EX 60 ENX

# 字串操作
APPEND key " appended"
STRLEN key
GETRANGE key 0 4
```

⚠️ **v2.0 更正**：`SETNX`、`SETEX`、`PSETEX`、`GETSET` 皆可由 `SET` 的選項取代，官方說明未來版本可能將其棄用；新程式請統一使用 `SET key value NX EX n` 等寫法。

#### 實務範例

```bash
# 快取使用者資料（務必設定 TTL）
SET cache:user:1001 '{"id":1001,"name":"John"}' EX 3600

# 頁面瀏覽計數
INCR stat:page:views:homepage

# 分散式鎖：取得（token 必須為不可猜測的隨機值）
SET lock:order:123 "c1f7e2a9-..." NX EX 30
# 釋放（8.4+，原子比對並刪除）
DELEX lock:order:123 IFEQ "c1f7e2a9-..."

# 樂觀更新：只有在他人未修改的情況下才寫入
GET config:feature:x                  # 讀到 "v1"
SET config:feature:x "v2" IFEQ "v1"   # 若回傳 nil 表示已被他人改動
```

#### ❌ 不建議的使用方式

- 儲存超過 100 KB 的單一值（網路與複寫成本高）；超過 1 MB 應視為 Big Key。
- 把結構化物件整包存成 JSON 字串，卻頻繁只更新其中一個欄位（改用 Hash 或 JSON 型別）。
- 使用 `GET` + 應用程式比對 + `SET` 實作「比較後寫入」（非原子，改用 `IFEQ`）。

---

### 5.2 Hash（雜湊）

**說明**：欄位—值（field-value）的集合，適合表示物件，可單獨讀寫欄位。7.4 起支援**欄位層級 TTL**；8.10 起多個相同欄位結構的 Hash 可共用欄位名稱模板（Compact hashes）以節省記憶體。

#### 使用情境

- 使用者資料、商品資訊（部分欄位更新）
- Session（不同欄位不同存活時間）
- 設定項目、功能開關

#### 常用指令

```bash
# 設定與讀取
HSET user:1001 name "John" email "john@example.com" age 30
HGET user:1001 name
HMGET user:1001 name email
HGETALL user:1001                     # 欄位多時請改用 HSCAN
HDEL user:1001 age
HEXISTS user:1001 name
HLEN user:1001
HINCRBY user:1001 login_count 1
HINCRBYFLOAT user:1001 balance 10.5
HSCAN user:1001 0 MATCH "pref:*" COUNT 100

# 欄位層級過期（7.4+）
HEXPIRE session:abc 600 FIELDS 1 csrf_token     # 單一欄位 600 秒後過期
HPEXPIRE session:abc 500 FIELDS 1 otp           # 毫秒
HTTL session:abc FIELDS 2 csrf_token otp        # 查詢剩餘秒數（-1 無 TTL、-2 欄位不存在）
HPERSIST session:abc FIELDS 1 csrf_token        # 移除欄位 TTL

# 讀寫同時處理 TTL（8.0+）
HSETEX session:abc EX 900 FIELDS 2 user_id 1001 role admin   # 設定欄位並給 TTL
HSETEX session:abc FNX EX 60 FIELDS 1 otp 123456              # 欄位都不存在才設定
HGETEX session:abc EX 900 FIELDS 1 user_id                    # 讀取並延長欄位 TTL（滑動過期）
HGETDEL session:abc FIELDS 1 otp                              # 讀取並刪除欄位（一次性 OTP）

# 批次匯入相同結構的 Hash（8.10+）
HIMPORT PREPARE u name email age
HIMPORT SET user:2001 u alice a@example.com 30
HIMPORT SET user:2002 u bob b@example.com 25
```

⚠️ **v2.0 更正**：`HMSET` 自 Redis 4.0 起已由可接受多組欄位的 `HSET` 取代，v1.0 附錄仍列出 `HMSET`，本版已移除。

#### 實務範例

```bash
# 購物車：每個品項獨立過期，不必整個購物車一起過期
HSET cart:user:1001 sku:A 2 sku:B 1
HEXPIRE cart:user:1001 86400 FIELDS 2 sku:A sku:B

# 一次性驗證碼（讀取即刪除，避免重放）
HSETEX auth:otp:1001 EX 300 FIELDS 1 code 482913
HGETDEL auth:otp:1001 FIELDS 1 code
```

> 💡 **欄位過期與 Keyspace notification**：8.8 起支援 Hash 欄位層級的鍵空間通知（subkey notification），可訂閱欄位過期事件；啟用前請評估事件量。

#### ❌ 不建議的使用方式

- 單一 Hash 欄位數過多（> 5,000）或總大小 > 1 MB，`HGETALL` 會成為慢命令。
- 需要巢狀結構或依欄位值查詢時硬用 Hash（改用 [JSON](#58-json文件) + Query Engine）。
- 大量欄位各自設定 TTL 而不評估記憶體（每個有 TTL 的欄位都有額外記錄成本）。

---

### 5.3 List（列表）

**說明**：依插入順序排列的字串序列，頭尾操作為 O(1)，依索引存取為 O(N)。

#### 使用情境

- 簡易工作佇列
- 最新動態（固定長度 Timeline）
- 可靠佇列（搭配 `LMOVE` 實作「處理中」清單）

#### 常用指令

```bash
LPUSH mylist a b                       # 從左加入
RPUSH mylist c d                       # 從右加入
LPOP mylist 2                          # 從左取出 2 個（6.2+ 支援 count）
RPOP mylist
BLPOP mylist 10                        # 阻塞取出，最多等 10 秒
LMPOP 2 list1 list2 LEFT COUNT 10      # 從多個 list 中第一個非空者取出（7.0+）

LRANGE mylist 0 -1
LLEN mylist
LTRIM mylist 0 99                      # 只保留前 100 個

LMOVE source dest LEFT RIGHT           # 原子搬移一個元素（6.2+）
BLMOVE source dest LEFT RIGHT 5        # 阻塞版本
LMOVEM source dest LEFT RIGHT COUNT 10 BULK   # 一次搬移最多 10 個（8.10+）
LMOVEM source dest LEFT RIGHT EXACTLY 3 BULK  # 剛好 3 個才搬移，否則不動作
```

⚠️ **v2.0 更正**：`RPOPLPUSH`／`BRPOPLPUSH` 自 6.2 起由 `LMOVE`／`BLMOVE` 取代。

#### 實務範例

```bash
# 可靠佇列：取出時同時放入 processing，處理完成才移除
BLMOVE queue:orders queue:orders:processing RIGHT LEFT 30
# ...業務處理成功後
LREM queue:orders:processing 1 '{"orderId":1001}'

# 最新 100 則動態
LPUSH timeline:user:1001 '{"type":"post","id":88}'
LTRIM timeline:user:1001 0 99
```

#### ❌ 不建議的使用方式

- 以 `LINDEX`／`LSET` 做大量隨機存取（O(N)）；需要索引存取請用 [Array](#57-array陣列)。
- 不限制長度的 List。
- 需要確認、重試、消費者群組的訊息佇列（改用 Stream）。

---

### 5.4 Set（集合）

**說明**：無序、不重複的字串集合，支援交集、聯集、差集運算。

#### 使用情境

- 標籤系統、權限集合
- 共同好友、共同興趣
- 去重（精確）
- 抽獎

#### 常用指令

```bash
SADD myset m1 m2 m3
SREM myset m1
SISMEMBER myset m1
SMISMEMBER myset m1 m2                 # 一次檢查多個（6.2+）
SCARD myset
SRANDMEMBER myset 3                    # 隨機取 3 個（不移除）
SPOP myset 1                           # 隨機取出 1 個（移除）
SSCAN myset 0 MATCH "m*" COUNT 100

SINTER s1 s2
SINTERCARD 2 s1 s2 LIMIT 1000          # 只回傳交集數量（7.0+）
SUNION s1 s2
SUNIONCARD 2 s1 s2                     # 只回傳聯集數量（8.10+）
SUNIONCARD 2 s1 s2 APPROX              # 以 HyperLogLog 近似計算（誤差約 0.81%）
SDIFF s1 s2
SDIFFCARD 2 s1 s2 LIMIT 1000           # 只回傳差集數量，達上限即停止計算（8.10+）
```

#### 實務範例

```bash
# 共同好友
SADD user:1001:friends user:1002 user:1003 user:1004
SADD user:1002:friends user:1001 user:1003 user:1005
SINTER user:1001:friends user:1002:friends       # user:1003

# 抽獎：使用 SPOP 避免同一人重複中獎
SADD lottery:2026q4 user:1001 user:1002 user:1003
SPOP lottery:2026q4 3
```

⚠️ **v2.0 更正**：v1.0 抽獎範例使用 `SRANDMEMBER`，該命令不會移除成員，多次抽獎可能重複中獎；需要「抽出即移除」時應使用 `SPOP`。

#### ❌ 不建議的使用方式

- 成員數很大（> 10,000）時使用 `SMEMBERS`（改用 `SSCAN`）。
- 只需要數量卻先取出完整集合再計數（改用 `SCARD`、`SINTERCARD`、`SUNIONCARD`）。
- 需要排序（改用 Sorted Set）。

---

### 5.5 Sorted Set（有序集合）

**說明**：每個成員附帶一個浮點數分數（score），依分數排序；排名、範圍查詢為 O(log N + M)。

#### 使用情境

- 排行榜
- 延遲佇列（分數 = 執行時間）
- 滑動視窗限流
- 時間序索引

#### 常用指令

```bash
ZADD rank 1000 "p1" 950 "p2"
ZADD rank GT 1200 "p1"                 # 只在新分數較高時更新（6.2+）
ZINCRBY rank 50 "p1"
ZSCORE rank "p1"
ZMSCORE rank "p1" "p2"                 # 6.2+
ZRANK rank "p1" WITHSCORE              # 7.2+ 可同時回傳分數
ZREVRANK rank "p1"

# 6.2+ 統一的 ZRANGE 語法（取代 ZREVRANGE、ZRANGEBYSCORE、ZRANGEBYLEX）
ZRANGE rank 0 9 REV WITHSCORES                     # 前 10 名（高到低）
ZRANGE rank 900 1000 BYSCORE WITHSCORES            # 分數範圍
ZRANGE rank (1000 -inf BYSCORE REV LIMIT 0 10      # 分數 < 1000，由高到低取 10 筆
ZRANGESTORE top10 rank 0 9 REV                     # 結果存成新 key

ZCOUNT rank 900 1000
ZREM rank "p1"
ZREMRANGEBYRANK rank 0 -11                         # 只保留前 10 名（低分在前時）
ZPOPMIN delayq 10                                  # 取出分數最低的 10 個
BZPOPMIN delayq 5                                  # 阻塞版本

# 集合運算
ZUNIONSTORE out 2 z1 z2 WEIGHTS 1 2
ZINTER 2 z1 z2 WITHSCORES
ZUNION 2 z1 z2 AGGREGATE COUNT WITHSCORES          # 計算成員出現在幾個集合（8.8+）
```

⚠️ **v2.0 更正**：`ZREVRANGE`、`ZRANGEBYSCORE`、`ZREVRANGEBYSCORE`、`ZRANGEBYLEX` 自 6.2 起官方標示為可由 `ZRANGE` 的 `REV`／`BYSCORE`／`BYLEX` 選項取代，新程式請使用統一語法。

#### 實務範例

```bash
# 排行榜 Top 10
ZADD rank:game:s1 1000 "player1" 950 "player2" 900 "player3"
ZRANGE rank:game:s1 0 9 REV WITHSCORES

# 延遲佇列：分數為預計執行的 Unix 時間
ZADD delayq:email 1790000000 '{"task":"send","to":"a@example.com"}'
# 取出已到期任務（應以 Lua 或 ZPOPMIN + 檢查分數確保不重複處理）
ZRANGE delayq:email -inf 1790000000 BYSCORE LIMIT 0 100
```

#### ❌ 不建議的使用方式

- 分數需要超過 2^53 的整數精度（double 精度限制）。
- 大型集合一次取全部（`ZRANGE key 0 -1`）。
- 用多個 client 同時「讀出到期任務再刪除」而不保證原子性（會重複消費）。

---

### 5.6 進階資料結構

#### Bitmap（點陣圖）

以 String 的位元操作實作，適合大量布林狀態（簽到、在線、特徵旗標）。1 億個位元約占 12 MB。

```bash
SETBIT user:1001:signin:202609 0 1     # 9/1 簽到
SETBIT user:1001:signin:202609 1 1
GETBIT user:1001:signin:202609 1
BITCOUNT user:1001:signin:202609       # 本月簽到天數
BITPOS user:1001:signin:202609 0       # 第一個未簽到的日子

BITOP AND out bm1 bm2                  # 交集
BITOP OR out bm1 bm2                   # 聯集
# 8.2+ 新運算子
BITOP DIFF out X Y1 Y2                 # 在 X 中、但不在任何 Y 中
BITOP DIFF1 out X Y1 Y2                # 在任一 Y 中、但不在 X 中
BITOP ANDOR out X Y1 Y2                # 在 X 中、且在至少一個 Y 中
BITOP ONE out K1 K2 K3                 # 只出現在剛好一個 key 中

BITFIELD stats INCRBY u32 0 1          # 在同一 key 中管理多個固定寬度整數
```

#### HyperLogLog

以約 12 KB 固定記憶體估算不重複元素個數，標準誤差約 0.81%。

```bash
PFADD uv:20260929 user1 user2 user3
PFCOUNT uv:20260929
PFMERGE uv:202609 uv:20260901 uv:20260902
```

#### Geospatial（地理位置）

```bash
GEOADD stores 121.5654 25.0330 "taipei101"
GEOSEARCH stores FROMLONLAT 121.56 25.03 BYRADIUS 2 km ASC COUNT 10 WITHDIST
GEODIST stores taipei101 store2 km
```

> ⚠️ `GEORADIUS`／`GEORADIUSBYMEMBER` 自 6.2 起由 `GEOSEARCH`／`GEOSEARCHSTORE` 取代。

#### Stream（Redis 5.0+）

Stream 是具持久性的追加式日誌，支援消費者群組、確認（ACK）、未確認清單（PEL）與重新認領，是 Redis 內建最完整的訊息佇列機制。

```bash
# 寫入
XADD orders * orderId 1001 status pending
XADD orders MAXLEN ~ 100000 * orderId 1002 status pending    # 近似修剪，控制長度

# 冪等寫入（8.6+）：同一 producer-id + 冪等 ID 重送時不會產生重複訊息
XADD orders IDMP order-svc req-7f3a * orderId 1003 status pending
XADD orders IDMPAUTO order-svc * orderId 1004 status pending  # 由 Redis 依內容自動產生冪等 ID
XCFGSET orders IDMP-DURATION 300 IDMP-MAXSIZE 1000            # 冪等 ID 保留時間與數量

# 消費者群組
XGROUP CREATE orders g-billing $ MKSTREAM
XREADGROUP GROUP g-billing c1 COUNT 10 BLOCK 5000 STREAMS orders >
XACK orders g-billing 1790000000000-0

# 同時認領閒置超過 60 秒的待處理訊息與讀取新訊息（8.4+）
XREADGROUP GROUP g-billing c1 COUNT 10 BLOCK 5000 CLAIM 60000 STREAMS orders >

# 主動退回處理失敗的訊息，讓其他消費者立即接手（8.8+）
XNACK orders g-billing FAIL IDS 1 1790000000000-0

# 確認並刪除（8.2+），避免已處理訊息持續占用記憶體
XACKDEL orders g-billing ACKED IDS 1 1790000000000-0

# 觀察
XPENDING orders g-billing
XINFO GROUPS orders
XLEN orders
```

**Stream 修剪與刪除策略（8.2+）**：

| 選項 | 行為 |
| --- | --- |
| `KEEPREF`（預設） | 刪除 Stream 條目，但保留消費者群組 PEL 中的參照 |
| `DELREF` | 刪除條目並一併移除所有群組 PEL 中的參照 |
| `ACKED` | 只刪除已被**所有**消費者群組確認的條目 |

> 💡 多個消費者群組共用一個 Stream 時，修剪應使用 `ACKED`（例如 `XTRIM orders MAXLEN ~ 100000 ACKED`），避免刪掉尚未被某個群組處理的訊息。

### 5.7 Array（陣列）

> 🆕 **v2.0 新增**（Redis 8.8+）

**說明**：以數字索引定址的字串集合，讀寫任意索引皆為 O(1)。內部以 4,096 個槽位為一組按需配置，稀疏索引（例如只寫入 0 與 1,000,000）幾乎不浪費記憶體。Array 補足了 List「索引存取為 O(N)」的缺點。

```bash
ARSET events:1 0 "login" "click" "purchase"   # 從索引 0 起連續寫入
ARGET events:1 1                              # "click"
ARMSET metrics 0 "10" 5 "20" 100 "30"         # 不連續索引批次寫入
ARMGET metrics 0 5 100 999                    # 999 未設定 → nil
ARLEN metrics                                 # 最大索引 + 1（101）
ARCOUNT metrics                               # 實際元素數（3）
ARGETRANGE metrics 0 10                       # 範圍讀取（單次上限 100 萬筆）

ARINSERT log "event1"                         # 依內部游標循序附加
ARRING readings 3 "v0"                        # 環狀緩衝：長度 3，自動覆寫最舊資料
ARLASTITEMS readings 3                        # 取最後 3 筆

AROP scores 0 2 SUM                           # 範圍聚合：SUM、MAX…
ARGREP log - + MATCH "error" NOCASE           # 搜尋元素
ARDEL scores 1
ARDELRANGE scores 0 2
```

| 需求 | 建議型別 |
| --- | --- |
| 依數字位置隨機讀寫、稀疏資料、環狀緩衝 | **Array** |
| 頭尾推入／取出、阻塞佇列 | List |
| 依欄位名稱存取 | Hash |
| 需要消費者群組與 ACK 的事件流 | Stream |

> ⚠️ Array 為 8.8 新型別，部分 client（例如 Lettuce）與託管服務的支援可能落後；採用前先確認 client 版本與雲端服務是否支援。

### 5.8 JSON（文件）

> 🆕 **v2.0 新增**（Redis 8.0 起內建，過去需 RedisJSON 模組）

**說明**：原生 JSON 文件型別，可用 JSONPath 讀寫局部欄位，並可由 Query Engine 建立索引查詢。8.4 起同質陣列（例如向量）記憶體大幅縮減；8.10 擴充 JSONPath 運算子與函式。

```bash
JSON.SET product:1001 $ '{"name":"Laptop","price":35000,"tags":["pc","work"],"stock":{"tw":12}}'
JSON.GET product:1001 $.name
JSON.GET product:1001 '$.stock.tw'
JSON.NUMINCRBY product:1001 $.stock.tw -1
JSON.ARRAPPEND product:1001 $.tags '"sale"'
JSON.SET product:1001 $.price 33000 XX      # 欄位存在才更新
JSON.DEL product:1001 $.tags[0]
JSON.MGET product:1001 product:1002 $.price
```

| 比較 | String（序列化 JSON） | Hash | JSON 型別 |
| --- | --- | --- | --- |
| 局部更新 | 需整包讀寫 | 只支援一層欄位 | 任意深度 JSONPath |
| 巢狀結構 | 可（但不可局部操作） | 否 | 是 |
| 建立搜尋索引 | 否 | 是 | 是 |
| 記憶體 | 最省 | 小物件最省 | 略高 |

### 5.9 機率型資料結構

> 🆕 **v2.0 新增**（Redis 8.0 起內建，過去需 RedisBloom 模組）

以極小記憶體換取「可接受的誤差」，適合超大量資料的存在判斷、頻率統計與分位數估計。

| 結構 | 回答的問題 | 典型用途 | 範例命令 |
| --- | --- | --- | --- |
| Bloom filter | 「一定不存在」或「可能存在」 | 快取穿透防護、帳號是否已註冊 | `BF.RESERVE`、`BF.ADD`、`BF.EXISTS` |
| Cuckoo filter | 同上，且支援刪除 | 需要移除元素的存在判斷 | `CF.ADD`、`CF.EXISTS`、`CF.DEL` |
| Top-K | 前 K 名熱門元素 | 熱門商品、熱門搜尋字 | `TOPK.RESERVE`、`TOPK.ADD`、`TOPK.LIST` |
| Count-Min Sketch | 元素出現次數（近似） | 事件頻率統計 | `CMS.INITBYPROB`、`CMS.INCRBY`、`CMS.QUERY` |
| t-digest | 分位數（P50／P99） | 延遲分布、金額分布 | `TDIGEST.CREATE`、`TDIGEST.ADD`、`TDIGEST.QUANTILE` |
| HyperLogLog | 不重複個數 | UV 統計 | `PFADD`、`PFCOUNT` |

```bash
# 快取穿透防護：誤判率 0.1%、預估 1,000 萬筆
BF.RESERVE bf:product:ids 0.001 10000000
BF.MADD bf:product:ids 1001 1002 1003
BF.EXISTS bf:product:ids 9999999      # 0 → 一定不存在，可直接回應不查 DB

# 熱門搜尋字 Top 10
TOPK.RESERVE topk:search 10
TOPK.ADD topk:search "iphone" "laptop" "iphone"
TOPK.LIST topk:search

# 延遲 P99
TDIGEST.CREATE lat:api:checkout
TDIGEST.ADD lat:api:checkout 12.5 8.1 230.4
TDIGEST.QUANTILE lat:api:checkout 0.5 0.99
```

### 5.10 Time Series（時間序列）

> 🆕 **v2.0 新增**（Redis 8.0 起內建，過去需 RedisTimeSeries 模組）

```bash
# 建立：保留 7 天、附標籤便於多序列查詢
TS.CREATE ts:cpu:host1 RETENTION 604800000 LABELS metric cpu host host1

# 寫入（* 代表伺服器時間）
TS.ADD ts:cpu:host1 * 37.5

# 範圍查詢與降採樣：每分鐘平均
TS.RANGE ts:cpu:host1 - + AGGREGATION avg 60000

# 自動降採樣規則：寫入原始序列時同步產生 1 小時平均
TS.CREATE ts:cpu:host1:1h LABELS metric cpu host host1 res 1h
TS.CREATERULE ts:cpu:host1 ts:cpu:host1:1h AGGREGATION avg 3600000

# 依標籤跨序列查詢
TS.MRANGE - + FILTER metric=cpu AGGREGATION max 60000
```

> 💡 8.6 起支援 NaN 值與 `COUNTNAN`／`COUNTALL` 聚合；8.8 起單一查詢可指定多個聚合器；8.10 新增 `TS.NRANGE`（依時間戳合併多序列）、`TS.READ`（可阻塞讀取）與 `TS.QUERYLABELS`。大量長期指標仍建議使用 Prometheus／專用時序資料庫，Redis Time Series 適合「即時、短保留期」的指標。

### 5.11 資料結構選型對照表

> 🆕 **v2.0 新增**

| 需求 | 首選 | 次選 | 避免 |
| --- | --- | --- | --- |
| 快取整個物件 | String | JSON | — |
| 快取物件且常局部更新 | Hash | JSON | String |
| 巢狀文件＋條件查詢 | JSON + Query Engine | — | String |
| 計數器／限流 | String（`INCR`／`INCREX`） | Hash 欄位 | Sorted Set（除非需要滑動視窗） |
| 排行榜 | Sorted Set | — | List |
| 工作佇列（簡易） | List | — | Pub/Sub |
| 可靠訊息佇列 | Stream | List + `LMOVE` | Pub/Sub |
| 即時廣播（可遺失） | Pub/Sub | Stream | — |
| 精確去重 | Set | — | — |
| 大量近似去重／存在判斷 | HyperLogLog／Bloom filter | Set | — |
| 索引定址、環狀緩衝 | Array（8.8+） | List | — |
| 地理位置 | Geo | — | — |
| 向量相似度搜尋 | Vector Set／向量索引（見 [第 14 章](#14-redis-8-query-engine向量搜尋與-ai-應用)） | — | 自行計算距離 |

### 5.12 💡 本章實務建議

- 依 [5.11](#511-資料結構選型對照表) 選型，並在設計審查時記錄「為何選擇此資料結構」。
- 新程式優先使用 8.x 原生原子命令（`SET IFEQ`、`DELEX`、`MSETEX`、`INCREX`、`HGETEX`），減少 Lua 腳本數量與維護成本。
- 集合型資料一律規劃上限（長度、欄位數、成員數），並以 `--keystats` 定期檢查。
- 導入 8.8／8.10 新型別或新命令前，確認所有環境（含 DR 與託管服務）與 client 版本均支援。

---

## 6. Redis 系統使用實戰

### 6.1 快取設計模式

| 模式 | 讀取 | 寫入 | 一致性 | 複雜度 | 適用 |
| --- | --- | --- | --- | --- | --- |
| **Cache-Aside（旁路快取）** | 應用先查快取，未命中查 DB 後回填 | 先寫 DB，再**刪除**快取 | 最終一致 | 低 | **預設首選** |
| Read-Through | 由快取層代為載入 | — | 最終一致 | 中 | 有快取框架／中介層時 |
| Write-Through | — | 由快取層同步寫入 DB 與快取 | 較高 | 中 | 寫後立即讀 |
| Write-Behind（Write-Back） | — | 先寫快取，非同步批次寫 DB | 低（可能遺失） | 高 | 高頻寫入、可容忍遺失的統計類資料 |
| Refresh-Ahead | 快到期前背景刷新 | — | 最終一致 | 中 | 熱點資料、避免擊穿 |

#### Cache-Aside（旁路快取）- 最常用

```mermaid
sequenceDiagram
    participant App as 應用程式
    participant R as Redis
    participant DB as 資料庫
    App->>R: GET cache:user:1001
    alt 命中
        R-->>App: 資料
    else 未命中
        R-->>App: nil
        App->>DB: SELECT ...
        DB-->>App: 資料
        App->>R: SET cache:user:1001 ... EX 3600
    end
```

```java
// Java 範例（Spring Boot）
public User getUser(long userId) {
    String key = "cache:user:" + userId;

    // 1. 查詢快取
    String cached = stringRedisTemplate.opsForValue().get(key);
    if (cached != null) {
        return NULL_MARKER.equals(cached) ? null : jsonMapper.readValue(cached, User.class);
    }

    // 2. 查詢資料庫
    User user = userRepository.findById(userId).orElse(null);

    // 3. 回填快取（查無資料時寫入短 TTL 的空值標記，防止穿透）
    if (user != null) {
        stringRedisTemplate.opsForValue().set(key, jsonMapper.writeValueAsString(user),
                jitter(Duration.ofHours(1)));
    } else {
        stringRedisTemplate.opsForValue().set(key, NULL_MARKER, Duration.ofMinutes(5));
    }
    return user;
}
```

**寫入順序為何是「先更新 DB、再刪除快取」？**

| 做法 | 並發風險 |
| --- | --- |
| 先刪快取、再更新 DB | 刪除後、DB 更新前，另一請求讀到舊 DB 資料並回填，快取長時間保留舊值 |
| 先更新 DB、再**更新**快取 | 兩個並發寫入可能以相反順序更新快取，造成快取與 DB 不一致 |
| **先更新 DB、再刪除快取**（建議） | 仍有極小視窗，但機率最低；可再搭配「延遲雙刪」或 CDC 事件刪除補強 |

#### Write Through（寫入穿透）

```mermaid
flowchart LR
    A[應用程式] -->|寫入| B[快取層]
    B -->|同步寫入| C[(資料庫)]
    B -->|同步寫入| D[(Redis)]
```

#### Write Back（延遲寫入）

```mermaid
flowchart LR
    A[應用程式] -->|寫入| B[(Redis)]
    B -->|Stream／佇列| C[背景 Worker]
    C -->|批次寫入| D[(資料庫)]
```

> ⚠️ Write-Behind 在 Redis 故障時會遺失尚未落地的資料，只適合按讚數、瀏覽數等可容忍誤差的資料；交易、帳務資料禁止使用。

### 6.2 TTL 與 Key 命名規範

#### Key 命名規範

```text
格式：{業務}:{模組}:{實體}:{識別碼}[:{子項}]

範例：
- cache:user:profile:1001         # 使用者資料快取
- order:detail:ORD202609001       # 訂單詳情
- cache:product:list:page:1       # 商品列表第 1 頁
- session:web:9f2c...             # Session
- lock:order:create:1001          # 分散式鎖
- ratelimit:api:login:1.2.3.4     # 限流計數
- {user:1001}:cart                # Cluster：以 hash tag 讓同使用者資料落在同一 slot
```

| 規則 | 說明 |
| --- | --- |
| 全小寫、以冒號分隔 | 與 Redis Insight 樹狀檢視及 ACL 前綴授權相容 |
| 第一段為業務或用途前綴 | 便於 ACL `~order:*` 授權與 `SCAN MATCH` 盤點 |
| 識別碼放最後 | 同類 key 前綴相同，方便分析 |
| 長度 ≤ 100 bytes | key 本身也占記憶體；百萬級 key 時差異顯著 |
| 不含個資明文 | 例如以使用者 ID 取代 email、身分證字號 |

#### TTL 設定建議

| 資料類型 | 建議 TTL | 說明 |
| --- | --- | --- |
| Session | 30 分鐘（滑動延長） | 依資安政策；可用 `GETEX`／`HGETEX` 延長 |
| 使用者資料快取 | 1～24 小時 | 依更新頻率 |
| 商品列表／搜尋結果 | 5～30 分鐘 | 熱門資料可較短 |
| 設定快取 | 1～7 天，並於變更時主動刪除 | 變動不頻繁 |
| 驗證碼／OTP | 1～5 分鐘 | 讀取後即刪除（`GETDEL`／`HGETDEL`） |
| 限流計數 | 等於視窗長度 | `INCREX ... EX n ENX` |
| 空值標記（防穿透） | 1～5 分鐘 | 避免長時間遮蔽真實資料 |

```bash
SET key value EX 3600              # 寫入時設定
EXPIRE key 3600                    # 對既有 key 設定
EXPIRE key 3600 NX                 # 只在尚無 TTL 時設定（7.0+）
EXPIRE key 3600 GT                 # 只在新 TTL 較長時設定（7.0+）
EXPIREAT key 1790000000            # 指定 Unix 時間
TTL key                            # 剩餘秒數（-1 無 TTL，-2 不存在）
PTTL key                           # 剩餘毫秒
EXPIRETIME key                     # 到期的 Unix 時間（7.0+）
PERSIST key                        # 移除 TTL
```

> 💡 **TTL 加入隨機抖動（jitter）**：大量 key 若以相同 TTL 同時寫入，會在同一時間到期而造成快取雪崩。建議 `TTL = 基準值 × (1 + random(0, 0.1))`。

### 6.3 Session 管理

#### Spring Session + Redis 範例

⚠️ **v2.0 更正**：Spring Boot 3.0 起 Redis 連線屬性由 `spring.redis.*` 改為 **`spring.data.redis.*`**，且 `spring.session.store-type` 已移除（Spring Boot 依 classpath 自動選擇 Session 儲存）。以下為 Spring Boot 4.x 寫法。

```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.session</groupId>
    <artifactId>spring-session-data-redis</artifactId>
</dependency>
```

```yaml
# application.yml（Spring Boot 4.x）
spring:
  data:
    redis:
      host: redis.internal
      port: 6379
      username: app_session
      password: ${REDIS_PASSWORD}
      ssl:
        enabled: true
  session:
    timeout: 30m
    redis:
      namespace: session:web          # Session key 前綴，便於 ACL 授權
      flush-mode: on-save
      repository-type: default        # 需要依使用者查 Session 時改為 indexed
```

```java
// 需要自訂時才加上註解；一般情況交由 Spring Boot 自動設定即可
@Configuration
@EnableRedisHttpSession(maxInactiveIntervalInSeconds = 1800, redisNamespace = "session:web")
public class SessionConfig {
}
```

**Session 安全要點**：

- Session ID 需為高熵隨機值，登入成功後重新產生（防 Session Fixation）。
- Session 內容避免存放敏感個資明文；必要時加密。
- 登出時主動刪除 Session key，不要只依賴 TTL。

### 6.4 Rate Limiting（速率限制）

#### 方法一：固定視窗計數器（8.8+ 使用 `INCREX`）

```bash
# 每個使用者每 60 秒最多 100 次
# 回傳 [目前計數, 實際增量]；實際增量為 0 表示已達上限
INCREX ratelimit:api:user:1001 BYINT 1 UBOUND 100 EX 60 ENX
```

- `UBOUND 100`：超過上限時不遞增，並回傳增量 0。
- `EX 60 ENX`：只有在 key 尚無 TTL（新視窗）時才設定 60 秒過期，後續請求不會延長視窗。
- 單一原子命令，不需 Lua。

```python
new_val, applied = r.execute_command(
    "INCREX", f"ratelimit:api:user:{user_id}",
    "BYINT", 1, "UBOUND", 100, "EX", 60, "ENX",
)
if applied == 0:
    raise TooManyRequests()
```

#### 方法二：固定視窗計數器（相容 8.8 以前版本，使用 Lua）

```lua
-- KEYS[1] = 限流 key；ARGV[1] = 上限；ARGV[2] = 視窗秒數
local current = redis.call('INCR', KEYS[1])
if current == 1 then
    redis.call('EXPIRE', KEYS[1], ARGV[2])
end
if current > tonumber(ARGV[1]) then
    return 0
end
return 1
```

#### 方法三：滑動視窗（Sorted Set + Lua，精確但較耗記憶體）

⚠️ **v2.0 更正**：v1.0 的 Java 範例以多個獨立命令（移除、計數、新增、設定 TTL）實作，並發時多個請求可能同時通過檢查。以下改為單一 Lua 腳本確保原子性。

```lua
-- KEYS[1] = 限流 key
-- ARGV[1] = 現在時間(ms)；ARGV[2] = 視窗(ms)；ARGV[3] = 上限；ARGV[4] = 請求唯一 ID
local now    = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
redis.call('ZREMRANGEBYSCORE', KEYS[1], 0, now - window)
if redis.call('ZCARD', KEYS[1]) >= tonumber(ARGV[3]) then
    return 0
end
redis.call('ZADD', KEYS[1], now, ARGV[4])
redis.call('PEXPIRE', KEYS[1], window)
return 1
```

| 演算法 | 精確度 | 記憶體 | 突發容忍 | 建議用途 |
| --- | --- | --- | --- | --- |
| 固定視窗（`INCREX`） | 視窗邊界可能 2 倍突發 | 極低 | 低 | 一般 API 限流 |
| 滑動視窗（Sorted Set） | 精確 | 與請求數成正比 | 無 | 登入、付款等敏感端點 |
| Token Bucket（Lua） | 高 | 低 | 可設定 | 需要允許短暫突發 |

> 💡 在 Cluster 中，限流 key 應以使用者或 API 為單位分散，避免所有請求集中到同一 key 形成熱點。

### 6.5 分散式 Lock 與 RedLock 概念

#### 單節點分散式鎖

```bash
# 取得鎖：token 為每次請求產生的隨機值（UUID）
SET lock:resource:123 "7d2f...token" NX PX 30000

# 釋放鎖（8.4+）：值相符才刪除，原子操作，不需 Lua
DELEX lock:resource:123 IFEQ "7d2f...token"

# 延長鎖（8.4+）：仍持有鎖時才延長
SET lock:resource:123 "7d2f...token" IFEQ "7d2f...token" PX 30000
```

**相容 8.4 以前版本的釋放腳本**：

```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
    return redis.call("DEL", KEYS[1])
else
    return 0
end
```

#### Spring 實作範例

```java
@Service
public class DistributedLockService {

    private final StringRedisTemplate redis;

    // 8.4 以前版本相容用
    private static final RedisScript<Long> UNLOCK_SCRIPT = RedisScript.of(
        "if redis.call('GET', KEYS[1]) == ARGV[1] then " +
        "  return redis.call('DEL', KEYS[1]) else return 0 end", Long.class);

    public DistributedLockService(StringRedisTemplate redis) {
        this.redis = redis;
    }

    public Optional<String> tryLock(String key, Duration ttl) {
        String token = UUID.randomUUID().toString();
        Boolean ok = redis.opsForValue().setIfAbsent(key, token, ttl);
        return Boolean.TRUE.equals(ok) ? Optional.of(token) : Optional.empty();
    }

    public boolean unlock(String key, String token) {
        // Redis 8.4+：可改用原生命令 DELEX key IFEQ token
        // （若 client 尚未提供 API，可透過 connection.execute("DELEX", ...) 呼叫）
        Long result = redis.execute(UNLOCK_SCRIPT, List.of(key), token);
        return Long.valueOf(1).equals(result);
    }
}
```

> 💡 生產環境建議直接使用成熟函式庫（例如 Redisson 的 `RLock`，具備看門狗自動續期、可重入、公平鎖），避免自行處理續期與重入邏輯。

#### ⚠️ RedLock 注意事項

RedLock 演算法在 N 個（通常 5 個）**彼此獨立**的 Redis 主節點上取得多數鎖，以容忍部分節點故障。但它仍存在以下限制：

- 依賴各節點時鐘大致同步，時鐘跳躍可能讓鎖提前失效。
- 持鎖程序若發生長時間 GC 停頓或網路延遲，鎖可能已過期而程序仍以為自己持有。
- 單純的 Redis 鎖**無法提供 fencing token**，無法阻止「過期持鎖者」的延遲寫入。

**企業使用準則**：

| 場景 | 建議 |
| --- | --- |
| 效率型鎖（避免重複計算，偶爾重複可接受） | 單節點 Redis 鎖即可 |
| 正確性型鎖（重複執行會造成資料錯誤、重複扣款） | 以資料庫唯一約束、樂觀鎖版本號或具 fencing token 的協調服務（ZooKeeper、etcd）為最終防線 |
| 長時間任務 | 使用看門狗續期，並設計冪等處理 |

### 6.6 Queue / Pub-Sub / Stream 使用情境

| 機制 | 持久性 | 消費模型 | ACK／重試 | 回放歷史 | 適用 |
| --- | --- | --- | --- | --- | --- |
| List（`LPUSH`/`BLMOVE`） | 有（隨持久化） | 競爭消費 | 需自行實作 | 否 | 簡單工作佇列 |
| Pub/Sub | **無**；離線即遺失 | 廣播 | 無 | 否 | 即時通知、快取失效廣播 |
| Sharded Pub/Sub（7.0+） | 無 | 廣播（Cluster 內依 slot 分片） | 無 | 否 | Cluster 內大量頻道 |
| Keyspace notifications | 無 | 廣播 | 無 | 否 | 監聽 key 過期／變更（非可靠） |
| **Stream** | 有 | 消費者群組 + 廣播 | 有（PEL、`XACK`、`XNACK`、`CLAIM`） | 是 | **可靠訊息佇列** |

#### 簡易佇列（List）

```bash
RPUSH queue:tasks '{"taskId":1,"type":"email"}'
BLMOVE queue:tasks queue:tasks:processing LEFT RIGHT 30   # 取出同時放入處理中清單
```

#### Pub/Sub

```bash
SUBSCRIBE channel:notifications
PUBLISH channel:notifications '{"type":"alert","message":"System update"}'

# Cluster 環境建議使用 Sharded Pub/Sub
SSUBSCRIBE channel:{tenant1}:events
SPUBLISH channel:{tenant1}:events '{"type":"refresh"}'
```

> ⚠️ **注意**：Pub/Sub 不保存訊息，訂閱者離線或斷線期間的訊息會遺失；也不應用於需要「每筆都要被處理」的業務事件。

#### Stream（推薦用於訊息佇列）

```mermaid
flowchart LR
    P1[Producer<br/>XADD IDMP] --> S[(Stream<br/>orders)]
    S --> G1[Group: billing]
    S --> G2[Group: shipping]
    G1 --> C1[Consumer b-1]
    G1 --> C2[Consumer b-2]
    G2 --> C3[Consumer s-1]
    C1 -.->|XACK／XNACK| S
```

```bash
# 建立群組（$ 表示只消費建立之後的新訊息；0 表示從頭消費）
XGROUP CREATE orders g-billing $ MKSTREAM

# 生產者：以業務請求 ID 做冪等寫入（8.6+），網路重送不會重複
XADD orders IDMP order-api req-20260929-0001 MAXLEN ~ 1000000 * orderId 1001 status pending

# 消費者：一次讀取閒置 60 秒以上的待處理訊息 + 新訊息（8.4+）
XREADGROUP GROUP g-billing b-1 COUNT 50 BLOCK 5000 CLAIM 60000 STREAMS orders >

# 成功：確認並（若所有群組皆已確認）刪除
XACKDEL orders g-billing ACKED IDS 1 1790000000000-0

# 暫時性失敗：退回讓其他消費者立即重試（8.8+）
XNACK orders g-billing FAIL IDS 1 1790000000000-0

# 毒訊息：標記為永久失敗，交由死信流程處理
XNACK orders g-billing FATAL IDS 1 1790000000000-0

# 監控
XPENDING orders g-billing - + 10
XINFO GROUPS orders
```

**Stream 消費者設計要點**：

1. **冪等處理**：Stream 提供「至少一次」投遞，消費端必須以業務 ID 去重。
2. **死信佇列**：以 `XPENDING` 的投遞次數判斷，超過門檻者搬到 `orders:dlq`。
3. **長度控制**：`XADD ... MAXLEN ~ N` 或定期 `XTRIM ... ACKED`。
4. **優雅關閉**：消費者下線前以 `XNACK ... SILENT` 退回手上未處理的訊息。

### 6.7 快取穿透、擊穿與雪崩

> 🆕 **v2.0 新增**

| 問題 | 成因 | 症狀 | 對策 |
| --- | --- | --- | --- |
| **快取穿透**（Penetration） | 查詢不存在的資料，每次都打到 DB（常見於惡意掃描） | DB 查詢量異常、命中率下降 | 空值標記（短 TTL）、Bloom filter 前置判斷、參數驗證 |
| **快取擊穿**（Breakdown） | 單一熱點 key 到期瞬間，大量請求同時回源 | DB 瞬間尖峰 | 互斥重建（single-flight 鎖）、邏輯過期＋背景刷新、熱點永不過期 |
| **快取雪崩**（Avalanche） | 大量 key 同時到期，或 Redis 整體故障 | DB 全面過載 | TTL 抖動、多層快取、熔斷與降級、Redis 高可用 |

**擊穿防護：互斥重建（Single-flight）**

```java
public Product getProduct(long id) {
    String key = "cache:product:" + id;
    String cached = redis.opsForValue().get(key);
    if (cached != null) return decode(cached);

    String lockKey = "lock:rebuild:" + key;
    String token = UUID.randomUUID().toString();
    if (Boolean.TRUE.equals(redis.opsForValue().setIfAbsent(lockKey, token, Duration.ofSeconds(10)))) {
        try {
            // 取得鎖後再檢查一次，避免重複回源
            cached = redis.opsForValue().get(key);
            if (cached != null) return decode(cached);
            Product p = productRepository.findById(id).orElse(null);
            redis.opsForValue().set(key, encode(p), jitter(Duration.ofMinutes(30)));
            return p;
        } finally {
            unlock(lockKey, token);   // 值相符才刪除（見 6.5）
        }
    }
    // 未取得鎖：短暫等待後重試讀快取，或回傳降級資料
    sleepQuietly(50);
    return getProductFromCacheOrFallback(key);
}
```

**穿透防護：Bloom filter 前置**

```mermaid
flowchart LR
    Q[查詢 product:9999999] --> B{BF.EXISTS}
    B -->|0 一定不存在| R1[直接回應 404]
    B -->|1 可能存在| C{Redis 快取}
    C -->|命中| R2[回應]
    C -->|未命中| D[(DB)]
```

### 6.8 Client-side Caching（客戶端快取）

> 🆕 **v2.0 新增**

Redis 6.0 起支援伺服器輔助的客戶端快取：client 在本地記憶體保存讀過的值，Redis 追蹤該 client 讀過的 key，當 key 被修改時主動推送**失效通知**（invalidation）。這可把熱點讀取延遲從網路往返降到本地記憶體存取。

| 模式 | 說明 | 記憶體成本 |
| --- | --- | --- |
| 預設模式 | 伺服器記住每個 client 讀過的 key | 伺服器端記憶體隨追蹤 key 數成長 |
| 廣播模式（`BCAST`） | client 訂閱 key 前綴，該前綴任何變更都通知 | 伺服器端幾乎無成本，通知量較大 |
| `OPTIN`／`OPTOUT` | 僅追蹤明確標記的讀取 | 可精準控制 |

```bash
# RESP3 連線直接在同一連線接收失效推播
HELLO 3
CLIENT TRACKING ON BCAST PREFIX cache:config:
GET cache:config:feature-x
# 其他 client 修改該 key 後，本連線會收到 invalidate 推播
```

> 💡 主流 client 已內建此功能（例如 redis-py、node-redis、Jedis 的 client-side caching 設定），實務上應透過 client 設定啟用，而不是手動處理推播。適合「讀取極頻繁、變更少」的設定、權限、功能開關資料。

### 6.9 交易、Lua Script 與 Functions

> 🆕 **v2.0 新增**

| 機制 | 原子性 | 條件邏輯 | 回滾 | 建議用途 |
| --- | --- | --- | --- | --- |
| Pipeline | 否（僅批次傳送） | 否 | 否 | 減少網路往返 |
| `MULTI`/`EXEC` | 是（批次內不被插入其他命令） | 否（可搭配 `WATCH` 樂觀鎖） | **否**，失敗命令不會回滾先前命令 | 多個寫入需一起生效 |
| Lua（`EVAL`/`EVALSHA`） | 是 | 是 | 否 | 複雜條件邏輯 |
| Functions（7.0+，`FUNCTION LOAD`/`FCALL`） | 是 | 是 | 否 | 需要版本管理、隨持久化與複寫保存的伺服器端邏輯 |
| 8.x 原生條件命令（`IFEQ`、`DELEX`、`INCREX`） | 是 | 有限 | — | **優先使用**，取代簡單 Lua |

```bash
# WATCH 樂觀鎖：被監看的 key 在 EXEC 前被修改時，交易不執行（回傳 nil）
WATCH account:1001:balance
GET account:1001:balance
MULTI
DECRBY account:1001:balance 100
INCRBY account:1002:balance 100
EXEC
```

```lua
#!lua name=inventory
-- Functions 範例：以函式庫形式載入，名稱與版本可管理
redis.register_function('reserve', function(keys, args)
    local stock = tonumber(redis.call('GET', keys[1]) or '0')
    local qty = tonumber(args[1])
    if stock < qty then
        return 0
    end
    redis.call('DECRBY', keys[1], qty)
    return 1
end)
```

```bash
# 載入與呼叫
cat inventory.lua | redis-cli -x FUNCTION LOAD REPLACE
FCALL reserve 1 stock:sku:A 2
```

**Lua／Functions 使用規範**：

- 腳本執行期間會阻塞 Redis，單次執行應控制在 **數毫秒以內**；`busy-reply-threshold`（預設 5 秒）後才可中斷。
- 腳本中存取的所有 key 必須以 `KEYS` 傳入（Cluster 需在同一 slot）。
- 不可在腳本中組合來自使用者輸入的腳本內容。
- 2025 年 10 月起多個 Lua 相關 CVE（見 [10.6](#106-cve-應變與修補管理)）顯示腳本引擎是高風險面：應用帳號若不需要腳本，應以 ACL `-@scripting` 禁止。

### 6.10 💡 本章實務建議

- Cache-Aside 為預設模式；寫入時「先更新 DB、再刪除快取」，所有快取 TTL 加入抖動。
- 限流、鎖釋放、比較後寫入等場景，8.4／8.8 以上版本優先使用原生命令取代 Lua。
- 業務事件使用 Stream，並以冪等寫入（`IDMP`）＋冪等消費＋死信佇列構成完整可靠性設計。
- 正確性要求高的互斥控制，不可只依賴 Redis 鎖，需有資料庫層的最終防線。

---

## 7. 應用系統如何串接 Redis

### 7.1 系統整體架構說明

```mermaid
flowchart TB
    subgraph AppLayer["Application Layer"]
        A1[Service 1<br/>L1 本地快取]
        A2[Service 2<br/>L1 本地快取]
    end

    subgraph CacheLayer["Cache Layer（跨 AZ）"]
        subgraph SentinelGroup["Sentinel"]
            S1[Sentinel 1]
            S2[Sentinel 2]
            S3[Sentinel 3]
        end
        M[Redis Primary]
        R1[Replica 1]
        R2[Replica 2]
    end

    subgraph DataLayer["Database Layer"]
        DB[(RDBMS<br/>真相來源)]
    end

    A1 -->|1. 查詢 Primary 位址| S1
    A1 -->|2. 讀寫| M
    A2 -->|讀取（可接受延遲資料）| R1
    M --> R1
    M --> R2
    A1 --> DB
    A2 --> DB
```

**串接設計原則**：

| 原則 | 說明 |
| --- | --- |
| 使用拓撲感知 client | Sentinel／Cluster 模式由 client 自動追蹤 Primary 與 slot 分配 |
| 共用長連線 | 使用連線池或多工連線（Lettuce、node-redis），禁止每次請求建立新連線 |
| 明確逾時 | 連線逾時、命令逾時都要設定，不可使用無限等待 |
| 可降級 | Redis 不可用時，快取讀取應降級為直接查 DB（並限流保護 DB） |
| 可觀測 | 記錄命令延遲、錯誤率、連線池使用率 |

### 7.2 常見串接方式（Client Library）

⚠️ **v2.0 更正**：Redis 官方目前推薦 **node-redis** 作為 Node.js 新專案首選；ioredis 仍受支援，但官方說明其缺少部分新功能與效能最佳化，並提供遷移指南。

| 語言 | 官方推薦 Client | 其他選項 | 特點 |
| --- | --- | --- | --- |
| Java | **Lettuce**（非同步、反應式、Spring Boot 預設）、**Jedis**（同步、API 簡單、功能最完整） | Redisson（分散式物件、鎖）、Redis OM Spring | Lettuce 尚未涵蓋全部新型別（如 Time Series、機率型結構） |
| Node.js | **node-redis** | ioredis（既有專案可續用） | node-redis 5.x 預設使用 RESP3 |
| Python | **redis-py** | RedisVL（向量／AI）、Redis OM Python | 支援 sync／asyncio |
| Go | **go-redis**（v9） | — | 支援 Cluster、Sentinel、OpenTelemetry |
| .NET | **StackExchange.Redis** | NRedisStack（JSON、搜尋、Time Series） | 多工單一連線 |
| PHP | Predis | phpredis（C 擴充，效能較佳） | — |

### 7.3 Java（Spring Boot + Redis）

> 以下以 **Spring Boot 4.x / Spring Data Redis 4.x** 為基準。Spring Data Redis 4.0 起 JSON 序列化改以 Jackson 3 為主，`GenericJackson2JsonRedisSerializer`、`Jackson2JsonRedisSerializer` 等 Jackson 2 類別已標示為 deprecated（預計移除）。

#### Maven 依賴

```xml
<dependencies>
    <!-- Spring Data Redis（預設使用 Lettuce） -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
    </dependency>

    <!-- Lettuce 使用連線池時需要（多數情境使用預設的共用連線即可，不必開啟連線池） -->
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-pool2</artifactId>
    </dependency>

    <!-- 若使用 @Cacheable -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-cache</artifactId>
    </dependency>
</dependencies>
```

#### 設定檔

⚠️ **v2.0 更正**：Spring Boot 3.0 起屬性前綴由 `spring.redis` 改為 **`spring.data.redis`**，v1.0 的設定在 Spring Boot 3／4 不會生效。

```yaml
# application.yml — 單節點
spring:
  data:
    redis:
      host: redis.internal
      port: 6379
      username: app_order
      password: ${REDIS_PASSWORD}
      database: 0
      client-name: order-service         # 方便以 CLIENT LIST 追查來源
      timeout: 2s                        # 命令逾時
      connect-timeout: 2s
      ssl:
        enabled: true
        bundle: redis-tls                # 以 spring.ssl.bundle 管理憑證
      lettuce:
        shutdown-timeout: 100ms
        pool:
          enabled: false                 # Lettuce 預設以單一多工連線即可
```

```yaml
# Sentinel
spring:
  data:
    redis:
      username: app_order
      password: ${REDIS_PASSWORD}
      sentinel:
        master: mymaster
        nodes:
          - sentinel-1.internal:26379
          - sentinel-2.internal:26379
          - sentinel-3.internal:26379
        username: sentinel_user          # Sentinel 本身的認證（若有啟用）
        password: ${SENTINEL_PASSWORD}
```

```yaml
# Cluster
spring:
  data:
    redis:
      username: app_order
      password: ${REDIS_PASSWORD}
      cluster:
        nodes:
          - redis-0.internal:6379
          - redis-1.internal:6379
          - redis-2.internal:6379
        max-redirects: 3
      lettuce:
        cluster:
          refresh:
            adaptive: true               # 收到 MOVED/ASK 或連線中斷時自動刷新拓撲
            period: 30s                  # 週期性刷新
```

#### Redis 設定類別

⚠️ **v2.0 更正**：v1.0 範例對 `ObjectMapper` 啟用 `activateDefaultTyping(LaissezFaireSubTypeValidator...)`，這會允許反序列化任意類別，是已知的 Jackson 反序列化攻擊面。本版改為「每種型別使用有型別的序列化器」，泛型快取則使用 Spring Data Redis 4 的 `GenericJacksonJsonRedisSerializer`。

```java
@Configuration
public class RedisConfig {

    /** 字串型操作：最常用、最安全 */
    @Bean
    public StringRedisTemplate stringRedisTemplate(RedisConnectionFactory factory) {
        return new StringRedisTemplate(factory);
    }

    /** 有型別的 Template：只會反序列化成 User，不接受任意類別 */
    @Bean
    public RedisTemplate<String, User> userRedisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<String, User> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        template.setKeySerializer(RedisSerializer.string());
        template.setValueSerializer(new JacksonJsonRedisSerializer<>(User.class));
        template.setHashKeySerializer(RedisSerializer.string());
        template.setHashValueSerializer(RedisSerializer.string());
        template.afterPropertiesSet();
        return template;
    }

    /** Lettuce 進階設定：透過 Customizer 加入，保留 Spring Boot 自動設定 */
    @Bean
    public LettuceClientConfigurationBuilderCustomizer lettuceCustomizer() {
        return builder -> builder.clientOptions(ClientOptions.builder()
                // 斷線時立即拒絕命令，而不是無限期暫存在記憶體中
                .disconnectedBehavior(ClientOptions.DisconnectedBehavior.REJECT_COMMANDS)
                .autoReconnect(true)
                .socketOptions(SocketOptions.builder()
                        .connectTimeout(Duration.ofSeconds(2))
                        .keepAlive(true)
                        .build())
                .timeoutOptions(TimeoutOptions.enabled(Duration.ofSeconds(2)))
                .build());
    }
}
```

⚠️ **v2.0 更正**：v1.0 在 7.6 直接宣告 `LettuceClientConfiguration` Bean，Spring Boot 的自動設定並不會採用該 Bean（逾時等設定因此不生效）；自訂 Lettuce 選項應使用 `LettuceClientConfigurationBuilderCustomizer`，才能與 `spring.data.redis.*` 屬性合併。

> 💡 Cluster 模式請改用 `ClusterClientOptions`，並搭配 `ClusterTopologyRefreshOptions` 啟用自適應拓撲刷新；使用 Spring Boot 屬性 `spring.data.redis.lettuce.cluster.refresh.*` 即可達成大部分需求。

#### 使用範例

```java
@Service
public class UserCacheService {

    private static final String KEY_PREFIX = "cache:user:";
    private static final Duration DEFAULT_TTL = Duration.ofHours(1);

    private final RedisTemplate<String, User> userRedis;
    private final StringRedisTemplate redis;

    public UserCacheService(RedisTemplate<String, User> userRedis, StringRedisTemplate redis) {
        this.userRedis = userRedis;
        this.redis = redis;
    }

    public void save(User user) {
        userRedis.opsForValue().set(KEY_PREFIX + user.getId(), user, jitter(DEFAULT_TTL));
    }

    public Optional<User> find(long userId) {
        return Optional.ofNullable(userRedis.opsForValue().get(KEY_PREFIX + userId));
    }

    public void evict(long userId) {
        // UNLINK：在背景釋放記憶體，避免大 key 阻塞
        userRedis.unlink(KEY_PREFIX + userId);
    }

    /** 批次讀取：一次 MGET，避免 N 次網路往返 */
    public List<User> findAll(List<Long> ids) {
        List<String> keys = ids.stream().map(id -> KEY_PREFIX + id).toList();
        List<User> results = userRedis.opsForValue().multiGet(keys);
        return results == null ? List.of() : results.stream().filter(Objects::nonNull).toList();
    }

    /** Hash：部分欄位更新 */
    public void updateLoginInfo(long userId, String ip) {
        String key = "user:login:" + userId;
        redis.opsForHash().putAll(key, Map.of(
                "lastIp", ip,
                "lastLoginAt", Instant.now().toString()));
        redis.expire(key, Duration.ofDays(30));
    }

    private static Duration jitter(Duration base) {
        long extra = (long) (base.toMillis() * ThreadLocalRandom.current().nextDouble(0.1));
        return base.plusMillis(extra);
    }
}
```

#### 快取註解方式

```java
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public RedisCacheManager cacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration defaults = RedisCacheConfiguration.defaultCacheConfig()
                .entryTtl(Duration.ofHours(1))
                .prefixCacheNameWith("cache:")          // 所有快取 key 以 cache: 開頭，便於 ACL 授權
                .serializeKeysWith(RedisSerializationContext.SerializationPair
                        .fromSerializer(RedisSerializer.string()))
                .serializeValuesWith(RedisSerializationContext.SerializationPair
                        .fromSerializer(GenericJacksonJsonRedisSerializer.builder().build()))
                .disableCachingNullValues();

        return RedisCacheManager.builder(factory)
                .cacheDefaults(defaults)
                // 不同快取不同 TTL
                .withCacheConfiguration("products", defaults.entryTtl(Duration.ofMinutes(10)))
                .withCacheConfiguration("config", defaults.entryTtl(Duration.ofDays(1)))
                .build();
    }
}

@Service
public class ProductService {

    private final ProductRepository productRepository;

    public ProductService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    // sync = true：同一 JVM 內對同一 key 的並發未命中只回源一次（降低擊穿）
    @Cacheable(cacheNames = "products", key = "#id", sync = true)
    public Product getProduct(Long id) {
        return productRepository.findById(id).orElse(null);
    }

    @CacheEvict(cacheNames = "products", key = "#product.id")
    public Product updateProduct(Product product) {
        return productRepository.save(product);   // 先更新 DB，方法成功後再刪除快取
    }

    @CacheEvict(cacheNames = "products", key = "#id")
    public void deleteProduct(Long id) {
        productRepository.deleteById(id);
    }
}
```

> ⚠️ **v2.0 更正**：v1.0 在更新時使用 `@CachePut`（寫入快取），在並發更新下可能以舊值覆蓋新值；與 [6.1](#61-快取設計模式) 的原則一致，更新時建議使用 `@CacheEvict` 刪除快取。另外，應避免使用 `allEntries = true`：`RedisCacheWriter` 預設的批次策略會以 `KEYS` 列出整個快取命名空間再刪除，大量 key 時會阻塞 Redis；確有需要時請將批次策略改為 `BatchStrategies.scan(1000)`。

### 7.4 Node.js / Python 串接概念

#### Node.js（node-redis，官方推薦）

```javascript
import { createClient, createSentinel, createCluster } from 'redis';

// 單節點
const client = createClient({
  url: 'rediss://app_order@redis.internal:6379',
  password: process.env.REDIS_PASSWORD,
  socket: {
    connectTimeout: 2000,
    reconnectStrategy: (retries) => Math.min(retries * 100, 3000), // 退避重連
  },
});
client.on('error', (err) => console.error('Redis Client Error', err));
await client.connect();

await client.set('cache:user:1001', JSON.stringify({ id: 1001 }), { EX: 3600 });
const value = await client.get('cache:user:1001');

// Sentinel
const sentinel = await createSentinel({
  name: 'mymaster',
  sentinelRootNodes: [
    { host: 'sentinel-1.internal', port: 26379 },
    { host: 'sentinel-2.internal', port: 26379 },
    { host: 'sentinel-3.internal', port: 26379 },
  ],
}).connect();

// Cluster
const cluster = await createCluster({
  rootNodes: [
    { url: 'redis://redis-0.internal:6379' },
    { url: 'redis://redis-1.internal:6379' },
  ],
  defaults: { username: 'app_order', password: process.env.REDIS_PASSWORD },
}).connect();
```

⚠️ **v2.0 更正**：v1.0 的 ioredis 範例在同一範圍內三次宣告 `const redis`，無法執行；且 `retryDelayOnFailover` 並非目前 ioredis 版本的有效選項。既有 ioredis 專案可參考官方「Migrate from ioredis」指南評估遷移。

#### Python（redis-py）

```python
import redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry
from redis.sentinel import Sentinel
from redis.cluster import RedisCluster

retry = Retry(ExponentialBackoff(cap=1.0, base=0.05), retries=3)

# 單節點（連線池由 Redis 物件內部管理，請在應用程式中共用同一個實例）
r = redis.Redis(
    host="redis.internal", port=6379,
    username="app_order", password=os.environ["REDIS_PASSWORD"],
    ssl=True, ssl_ca_certs="/etc/ssl/redis-ca.crt",
    socket_connect_timeout=2, socket_timeout=2,
    retry=retry, decode_responses=True,
    health_check_interval=30,
)
r.set("cache:user:1001", '{"id":1001}', ex=3600)

# Sentinel
sentinel = Sentinel(
    [("sentinel-1.internal", 26379), ("sentinel-2.internal", 26379), ("sentinel-3.internal", 26379)],
    socket_timeout=0.5,
    sentinel_kwargs={"username": "sentinel_user", "password": os.environ["SENTINEL_PASSWORD"]},
)
primary = sentinel.master_for("mymaster", username="app_order", password=os.environ["REDIS_PASSWORD"])
replica = sentinel.slave_for("mymaster", username="app_order", password=os.environ["REDIS_PASSWORD"])

# Cluster
rc = RedisCluster(
    host="redis-0.internal", port=6379,
    username="app_order", password=os.environ["REDIS_PASSWORD"],
    retry=retry,
)
```

> 💡 `master_for`／`slave_for` 為 redis-py Sentinel API 的既有方法名稱；敘述上本手冊一律稱 Primary／Replica。

### 7.5 Connection Pool 設計

```mermaid
flowchart LR
    subgraph App["Application"]
        T1[Thread 1]
        T2[Thread 2]
        T3[Thread 3]
    end
    subgraph Pool["Connection Pool"]
        C1[Conn 1]
        C2[Conn 2]
    end
    T1 -->|借用| C1
    T2 -->|借用| C2
    T3 -->|等待 max-wait| Pool
    C1 -->|歸還| Pool
```

**不同 client 的連線模型**：

| Client | 模型 | 是否需要連線池 |
| --- | --- | --- |
| Lettuce | 單一 TCP 連線多工（Netty），執行緒安全 | 一般**不需要**；僅在使用阻塞命令（`BLPOP`、`XREAD BLOCK`）或交易（`MULTI`）時需要獨立連線 |
| Jedis | 一個連線同時只能服務一個執行緒 | **需要**（`JedisPooled`／`JedisPool`） |
| node-redis | 單一連線多工；阻塞命令需額外連線（`isolationPool`） | 一般不需要 |
| redis-py | 內建連線池 | 共用同一個 `Redis` 物件即可 |
| StackExchange.Redis | 單一 `ConnectionMultiplexer` 多工 | 應用程式全域共用一個 multiplexer |

**連線池參數建議（Jedis／需要連線池時）**：

| 參數 | 建議值 | 說明 |
| --- | --- | --- |
| max-total（max-active） | 依「峰值併發 × 平均命令時間」估算，常見 16～64 | 過大會造成伺服器連線數暴增 |
| max-idle | 等於 max-total | 避免頻繁建立與關閉連線 |
| min-idle | 4～8 | 預熱連線，降低冷啟動延遲 |
| max-wait | 200～1000 ms | 取不到連線時快速失敗，而非無限等待 |
| test-while-idle | true | 背景偵測失效連線 |
| test-on-borrow | false | 每次借用都 PING 會增加延遲 |

> 💡 **連線數預算**：`應用實例數 × 每實例最大連線數` 必須小於 Redis `maxclients`（預設 10000）並保留維運餘裕。Kubernetes 自動擴展時尤其容易超過上限。

### 7.6 Timeout / Retry / Fallback 設計

**逾時與重試建議值**：

| 參數 | 建議 | 說明 |
| --- | --- | --- |
| 連線逾時 | 1～2 秒 | 失敗應快速回報 |
| 命令逾時 | 快取讀取 100～500 ms；一般 1～2 秒 | 快取讀取逾時應短於回源 DB 的時間 |
| 重試次數 | 讀取 1～2 次；寫入非冪等命令**不重試** | `INCR` 重試可能重複遞增 |
| 重試退避 | 指數退避 + 隨機抖動 | 避免重試風暴 |
| 熔斷 | 錯誤率 > 50%（10 秒視窗）開啟，30 秒後半開 | 保護 Redis 與應用執行緒 |

```mermaid
flowchart TD
    A[讀取請求] --> B{熔斷器開啟?}
    B -->|是| F[直接回源 DB<br/>DB 端限流保護]
    B -->|否| C[Redis GET<br/>逾時 300ms]
    C -->|命中| D[回應]
    C -->|未命中| F
    C -->|逾時／錯誤| E[記錄錯誤率] --> F
    F --> G[非同步回填快取<br/>失敗僅記錄]
    G --> D
```

#### 使用 Resilience4j

⚠️ **v2.0 更正**：v1.0 範例使用 Vavr 的 `Try`，但未說明需要額外相依套件，且自行撰寫的 for 迴圈重試會讓每次錯誤延長回應時間。以下改用 Resilience4j 原生 API。

```java
@Service
public class ResilientUserService {

    private final RedisTemplate<String, User> userRedis;
    private final UserRepository userRepository;
    private final CircuitBreaker circuitBreaker;

    public ResilientUserService(RedisTemplate<String, User> userRedis,
                                UserRepository userRepository,
                                CircuitBreakerRegistry registry) {
        this.userRedis = userRedis;
        this.userRepository = userRepository;
        this.circuitBreaker = registry.circuitBreaker("redis");
    }

    public User getUser(long userId) {
        String key = "cache:user:" + userId;
        User cached = null;
        try {
            cached = circuitBreaker.executeSupplier(() -> userRedis.opsForValue().get(key));
        } catch (CallNotPermittedException | RedisConnectionFailureException | QueryTimeoutException e) {
            log.warn("Redis 不可用，降級為直接查詢資料庫: {}", e.getMessage());
        }
        if (cached != null) {
            return cached;
        }

        User user = userRepository.findById(userId).orElse(null);
        if (user != null && circuitBreaker.getState() == CircuitBreaker.State.CLOSED) {
            try {
                userRedis.opsForValue().set(key, user, Duration.ofHours(1));
            } catch (RuntimeException e) {
                log.warn("回填快取失敗，不影響回應", e);
            }
        }
        return user;
    }
}
```

```yaml
# application.yml
resilience4j:
  circuitbreaker:
    instances:
      redis:
        sliding-window-type: TIME_BASED
        sliding-window-size: 10
        failure-rate-threshold: 50
        slow-call-duration-threshold: 500ms
        slow-call-rate-threshold: 50
        wait-duration-in-open-state: 30s
        permitted-number-of-calls-in-half-open-state: 5
```

> ⚠️ **降級時保護 DB**：Redis 故障時所有流量回到 DB，可能造成連鎖故障。回源路徑必須搭配 DB 連線池上限、限流或部分功能降級（例如暫停非核心排行榜）。

### 7.7 Go 與 .NET 串接範例

> 🆕 **v2.0 新增**

**Go（go-redis v9）**：

```go
import (
    "context"
    "crypto/tls"
    "os"
    "time"

    "github.com/redis/go-redis/v9"
)

func newClient() *redis.Client {
    return redis.NewClient(&redis.Options{
        Addr:         "redis.internal:6379",
        Username:     "app_order",
        Password:     os.Getenv("REDIS_PASSWORD"),
        TLSConfig:    &tls.Config{MinVersion: tls.VersionTLS12},
        DialTimeout:  2 * time.Second,
        ReadTimeout:  500 * time.Millisecond,
        WriteTimeout: 500 * time.Millisecond,
        PoolSize:     32,
        MinIdleConns: 4,
    })
}

// Sentinel：redis.NewFailoverClient(&redis.FailoverOptions{MasterName: "mymaster", SentinelAddrs: [...]})
// Cluster ：redis.NewClusterClient(&redis.ClusterOptions{Addrs: [...]})

func example(ctx context.Context, rdb *redis.Client) error {
    return rdb.Set(ctx, "cache:user:1001", `{"id":1001}`, time.Hour).Err()
}
```

**.NET（StackExchange.Redis）**：

```csharp
// 應用程式全域共用一個 ConnectionMultiplexer（例如以 DI 註冊為 Singleton）
var options = ConfigurationOptions.Parse("redis.internal:6379");
options.User = "app_order";
options.Password = Environment.GetEnvironmentVariable("REDIS_PASSWORD");
options.Ssl = true;
options.ConnectTimeout = 2000;
options.SyncTimeout = 1000;
options.AbortOnConnectFail = false;   // 啟動時 Redis 暫不可用也不會直接失敗

var mux = await ConnectionMultiplexer.ConnectAsync(options);
IDatabase db = mux.GetDatabase();
await db.StringSetAsync("cache:user:1001", "{\"id\":1001}", TimeSpan.FromHours(1));
```

### 7.8 RESP3 與 Client 相容性

> 🆕 **v2.0 新增**

RESP3 是 Redis 6.0 引入的新版通訊協定，支援 Map、Set、Double、Push 等原生型別，是 client-side caching 推播與多數新功能的基礎。2026 年起主流 client 已陸續把預設協定改為 RESP3（例如 node-redis 5.x；redis-py 7.x 亦改以 RESP3 連線並保留舊回應格式相容）。

| 檢查項目 | 說明 |
| --- | --- |
| 回應型別變化 | 同一命令在 RESP2／RESP3 下回傳結構不同（例如 `HGETALL` 在 RESP3 為 Map）；升級 client 後需回歸測試 |
| 代理與中介軟體 | 舊版 Proxy（如 Twemproxy）可能不支援 `HELLO 3` |
| 可強制指定 | 多數 client 可設定 `protocol=2` 回到 RESP2 以漸進遷移 |
| 新命令支援 | 8.x 新命令（`INCREX`、`XNACK`、`AR*`）需較新 client；舊 client 可用「送出原始命令」API（如 `execute_command`、`sendCommand`） |

### 7.9 💡 本章實務建議

- Java 新專案使用 Spring Boot 4 + Lettuce；屬性一律使用 `spring.data.redis.*`，進階設定透過 `LettuceClientConfigurationBuilderCustomizer`。
- 值的序列化優先使用「有型別」序列化器；禁止對不受信任資料啟用 Jackson 任意型別反序列化。
- Node.js 新專案使用 node-redis；既有 ioredis 專案依需求評估遷移。
- 每個服務都要有明確的逾時、熔斷與降級路徑，並在壓測中實際演練 Redis 故障。
- 升級 client 大版本時，特別驗證 RESP3 預設協定造成的回應格式差異。

---

## 8. Redis 維運與監控

### 8.1 常用監控指標

| 類別 | 指標（`INFO` 欄位） | 說明 | 建議告警門檻 |
| --- | --- | --- | --- |
| **可用性** | 探測 `PING` | 服務是否回應 | 連續 3 次失敗 → P1 |
| **記憶體** | `used_memory` / `maxmemory` | 使用率 | > 80% 警告、> 90% 嚴重 |
| | `mem_fragmentation_ratio` | RSS ÷ used_memory | > 1.5 持續 30 分鐘；< 1.0 表示發生 swap |
| | `evicted_keys`（每秒增量） | 因記憶體不足被淘汰的 key | 非純快取實例 > 0 即告警 |
| **效能** | `instantaneous_ops_per_sec` | 目前 QPS | 偏離基線 ± 50% |
| | 命令延遲（`INFO latencystats`、`LATENCY LATEST`） | P50／P99 延遲 | P99 > 10 ms |
| | `slowlog` 新增筆數 | 慢查詢 | 每分鐘 > 10 筆 |
| **命中率** | `keyspace_hits / (hits + misses)` | 快取命中率 | < 80%（依業務基線調整） |
| **連線** | `connected_clients` | 連線數 | > `maxclients` × 80% |
| | `blocked_clients` | 阻塞命令中的連線 | 非預期增加 |
| | `rejected_connections`（增量） | 因達上限被拒 | > 0 |
| **複寫** | `master_link_status`（Replica） | 與 Primary 連線 | `down` |
| | `master_repl_offset` − Replica offset | 複寫落後位元組數 | 持續增加 |
| | `sync_full`（增量） | 全量同步次數 | > 0 需調查 backlog 大小 |
| **持久化** | `rdb_last_bgsave_status` | RDB 狀態 | `err` |
| | `aof_last_write_status`、`aof_last_bgrewrite_status` | AOF 狀態 | `err` |
| | `latest_fork_usec` | 最近一次 fork 耗時 | > 500 ms（大資料集需評估） |
| **安全** | `acl_access_denied_auth`（增量） | 認證失敗 | 短時間大量 → 可能暴力破解 |
| | `total_error_replies`（增量） | 錯誤回應數 | 偏離基線 |

⚠️ **v2.0 更正**：v1.0 以 `master_last_io_seconds_ago` 代表「複寫延遲」並不精確；該欄位表示距離上次收到 Primary 資料的秒數，在寫入很少時也會增加。複寫落後應以 **Primary 的 `master_repl_offset` 與各 Replica 回報的 `offset` 差值**衡量（`INFO replication` 中 `slaveN:...offset=...,lag=...`）。

### 8.2 INFO 指令說明

```bash
INFO                  # 預設區塊
INFO everything       # 全部區塊（含 commandstats、latencystats）
INFO server           # 版本、執行時間、設定檔
INFO clients          # 連線數、阻塞連線、輸入/輸出緩衝
INFO memory           # 記憶體、碎片率、淘汰
INFO persistence      # RDB/AOF 狀態
INFO stats            # 命令數、命中率、淘汰、錯誤
INFO replication      # 角色、Replica 狀態、offset
INFO cpu              # CPU 時間
INFO commandstats     # 每個命令的呼叫次數與平均耗時
INFO latencystats     # 每個命令的延遲百分位數（7.0+）
INFO errorstats       # 各類錯誤統計（6.2+）
INFO keysizes         # 各資料型別的 key 大小分布（8.x）
INFO cluster
INFO keyspace         # 各 db 的 key 數、有 TTL 的 key 數
```

**重要指標解讀**：

```bash
# 記憶體
used_memory_human:6.20G
used_memory_rss_human:6.95G
used_memory_peak_human:7.10G
used_memory_peak_time:1790000000       # 8.2+：峰值發生時間
maxmemory_human:10.00G
maxmemory_policy:allkeys-lfu
mem_fragmentation_ratio:1.12           # 1.0～1.5 正常
allocator_frag_ratio:1.03

# 效能
instantaneous_ops_per_sec:48213
total_commands_processed:9876543210

# 命中率
keyspace_hits:4500000
keyspace_misses:500000
# 命中率 = 4500000 / (4500000 + 500000) = 90%

# 複寫（Primary 端）
role:master
connected_slaves:2
slave0:ip=10.0.1.11,port=6379,state=online,offset=123456789,lag=0
slave1:ip=10.0.2.11,port=6379,state=online,offset=123450000,lag=1
master_repl_offset:123456789           # 與 slave1 相差 6789 bytes

# 複寫（Replica 端，8.2+ 新增欄位）
master_link_status:up
master_link_up_since_seconds:86400
master_total_sync_attempts:1
```

### 8.3 慢查詢（Slow Log）

```bash
# 門檻（微秒）；10000 = 10 ms。延遲敏感系統可設 1000～5000
CONFIG SET slowlog-log-slower-than 10000
CONFIG SET slowlog-max-len 1024

SLOWLOG GET 10
# 每筆包含：ID、Unix 時間、耗時（微秒）、命令與參數、客戶端位址、客戶端名稱
# 8.10+ 另回傳命令的原始參數總數（紀錄可能被 slowlog-entry-max-argc 截斷）

SLOWLOG LEN
SLOWLOG RESET
```

> 💡 SLOWLOG 只記錄**命令執行時間**，不含網路傳輸與排隊等待。若 SLOWLOG 乾淨但應用端延遲高，應檢查網路、連線池等待、客戶端 GC 或 Redis 主執行緒被 fork／AOF fsync 阻塞（見 [8.7](#87-延遲診斷)）。

### 8.4 Key 分析與 Big Key 問題

#### 找出 Big Key

```bash
# 依元素數量（O(N) 型別的長度）找最大 key
redis-cli --bigkeys -i 0.01

# 依記憶體用量找最大 key
redis-cli --memkeys -i 0.01

# 合併兩者並輸出分布統計、Top N（建議）
redis-cli --keystats --top 20 -i 0.01

# 單一 key 記憶體
MEMORY USAGE cache:user:1001 SAMPLES 0

# 伺服器端 key 大小分布（不需掃描）
INFO keysizes
```

> 💡 `-i 0.01` 讓每 100 次 `SCAN` 休息 10 ms，降低掃描對線上服務的影響；以上工具皆以 `SCAN` 實作，可在 Replica 上執行以完全避開 Primary。

**Big Key 判斷基準（企業建議值）**：

| 型別 | 警告 | 嚴重 |
| --- | --- | --- |
| String | > 100 KB | > 1 MB |
| Hash／Set／ZSet／List | > 5,000 元素或 > 1 MB | > 50,000 元素或 > 10 MB |
| Stream | > 100 萬筆且未修剪 | 持續增長無修剪 |

#### Big Key 處理方式

```mermaid
flowchart TD
    A[發現 Big Key] --> B{型別?}
    B -->|String| C[拆分／壓縮<br/>或移至物件儲存]
    B -->|Hash| D[依欄位雜湊分片<br/>user:1001:0..N]
    B -->|List| E[分段或改用 Stream／Array]
    B -->|Set/ZSet| F[依成員雜湊分片<br/>或縮小範圍]
    B -->|Stream| G[XADD MAXLEN／XTRIM ACKED]
    C --> H[刪除舊 key：UNLINK<br/>或 HSCAN＋HDEL 漸進刪除]
    D --> H
    E --> H
    F --> H
```

```bash
# 刪除大 key：使用 UNLINK（背景釋放），不要用 DEL
UNLINK big:hash:1

# 大 Hash 分片：以欄位雜湊決定分片
# 原本：user:1001:prefs（10 萬欄位）
# 改為：user:1001:prefs:{0..15}，分片 = CRC32(field) % 16
```

### 8.5 常見效能問題與處理方式

| 問題 | 症狀 | 原因 | 解決方式 |
| --- | --- | --- | --- |
| **命令阻塞** | 延遲突然升高、所有客戶端受影響 | `KEYS`、`HGETALL`／`SMEMBERS`／`LRANGE 0 -1` 大 key、長 Lua | `SCAN` 系列、限制範圍、ACL 禁用 `KEYS` |
| **Big Key** | 單一操作延遲高、網路尖峰 | 單一 key 過大 | 拆分、`UNLINK` |
| **Hot Key** | 單一節點 CPU 高、Cluster 負載不均 | 少數 key 被大量存取 | `HOTKEYS` 找出後以本地快取或副本分散（見 [8.6](#86-hot-key-偵測)） |
| **記憶體碎片** | `used_memory_rss` 遠大於 `used_memory` | 頻繁刪改不同大小的值 | 啟用 `activedefrag`；低峰期滾動重啟 |
| **fork 延遲** | 週期性延遲尖峰 | RDB／AOF 重寫 fork、THP | 關閉 THP、調整 `save`、在 Replica 做持久化 |
| **AOF fsync 阻塞** | 日誌出現 `Asynchronous AOF fsync is taking too long` | 磁碟 I/O 慢 | 使用 SSD、檢查同機其他 I/O |
| **連線數過多** | `rejected_connections` 增加 | 連線池過大、連線洩漏、自動擴展 | 修正連線池、設定 `timeout`、提高 `maxclients` |
| **網路往返過多** | QPS 上不去但 CPU 不高 | 大量單一小請求 | Pipeline、`MGET`／`MSET`／`MSETEX` |
| **Swap** | 延遲數十毫秒以上、`mem_fragmentation_ratio < 1` | 記憶體不足被換出 | 關閉 swap、降低 `maxmemory` |

⚠️ **v2.0 更正**：v1.0 建議以 `MEMORY PURGE` 處理碎片。`MEMORY PURGE` 只要求 jemalloc 釋放已歸還的閒置分頁，效果有限；持續性碎片應啟用 `activedefrag`（見 [4.7](#47-效能相關設定)）。

#### Pipeline 優化範例

```java
// 批次寫入 1,000 筆：一次網路往返取代 1,000 次
public void batchSet(Map<String, String> data, Duration ttl) {
    stringRedisTemplate.executePipelined((RedisCallback<Object>) connection -> {
        StringRedisConnection conn = (StringRedisConnection) connection;
        data.forEach((key, value) -> conn.set(key, value, Expiration.from(ttl),
                RedisStringCommands.SetOption.upsert()));
        return null;
    });
}
```

> 💡 單一 Pipeline 建議 100～1,000 個命令；過大會占用大量客戶端與伺服器端緩衝。若所有 key 需共用 TTL，8.4+ 可直接使用單一 `MSETEX`。

### 8.6 Hot Key 偵測

> 🆕 **v2.0 新增**

| 方法 | 版本 | 優點 | 限制 |
| --- | --- | --- | --- |
| `HOTKEYS` 命令 | 8.6+ | 伺服器端以機率型結構統計 CPU 與網路占比，準確且成本低 | 需 admin 權限 |
| `redis-cli --hotkeys` | 4.0+ | 簡單 | 需要 `maxmemory-policy` 為 `*-lfu` |
| `CLUSTER SLOT-STATS` | 8.2+ | 找出熱點 slot | 粒度為 slot 而非 key |
| `MONITOR` 抽樣 | 全部 | 可看到完整命令 | 嚴重影響效能，僅限極短時間 |

```bash
# 啟動追蹤：同時以 CPU 與網路計算，取前 10 名，持續 60 秒，取樣率 1/10
HOTKEYS START METRICS 2 CPU NET COUNT 10 DURATION 60 SAMPLE 10

# 取得結果
HOTKEYS GET

# 提前停止與釋放資源
HOTKEYS STOP
HOTKEYS RESET
```

**Hot Key 處理策略**：

| 策略 | 說明 |
| --- | --- |
| 應用端本地快取（L1） | 對熱點 key 以 Caffeine 等快取 1～10 秒 |
| Client-side caching | 由 Redis 推送失效通知，本地快取可維持一致（見 [6.8](#68-client-side-caching客戶端快取)） |
| 讀取分散到 Replica | 可接受短暫舊資料時 |
| Key 複製分片 | 寫入時同步寫 `hot:{n}` 多份，讀取隨機挑一份（寫入需全部更新） |

### 8.7 延遲診斷

> 🆕 **v2.0 新增**

```bash
# 1. 建立基線：在 Redis 主機本機測量系統固有延遲（不連線 Redis）
redis-cli --intrinsic-latency 30

# 2. 從應用主機量測 PING 延遲與百分位數（8.10+ 支援 --latency-percentiles）
redis-cli -h redis.internal --latency-history -i 5 --latency-percentiles 50,99,99.9

# 3. 啟用延遲監控並查看報告
CONFIG SET latency-monitor-threshold 100
LATENCY LATEST              # 各事件最近一次與最大延遲
LATENCY HISTORY fork        # 特定事件歷史
LATENCY DOCTOR              # 以文字說明可能原因與建議

# 4. 各命令延遲分布
INFO latencystats
```

| 常見延遲來源 | 判斷方式 |
| --- | --- |
| 慢命令 | `SLOWLOG GET`、`INFO commandstats` |
| fork（RDB／AOF 重寫、全量同步） | `latest_fork_usec`、`LATENCY HISTORY fork` |
| AOF fsync | `LATENCY HISTORY aof-fsync-always`、日誌警告 |
| 大量 key 同時過期 | `LATENCY HISTORY expire-cycle` |
| 淘汰 | `LATENCY HISTORY eviction-cycle` |
| 虛擬化／鄰居干擾 | `--intrinsic-latency` 結果偏高 |
| 網路 | 應用端與 Redis 端延遲差異大 |

### 8.8 Prometheus + Grafana 監控

> 🆕 **v2.0 新增**

**架構**：

```mermaid
flowchart LR
    R1[(Redis 節點)] --> E[redis_exporter<br/>oliver006/redis_exporter]
    R2[(Redis 節點)] --> E
    E -->|/metrics| P[Prometheus]
    P --> G[Grafana Dashboard]
    P --> AM[Alertmanager] --> N[通報：Email／Teams／PagerDuty]
```

```yaml
# redis_exporter（Docker Compose 片段）
services:
  redis-exporter:
    image: oliver006/redis_exporter:latest    # 生產環境請鎖定版本
    environment:
      REDIS_ADDR: "rediss://redis.internal:6379"
      REDIS_USER: "monitor"
      REDIS_PASSWORD: "${REDIS_MONITOR_PASSWORD}"
    ports:
      - "9121:9121"
```

```yaml
# Prometheus 告警規則範例
groups:
  - name: redis
    rules:
      - alert: RedisDown
        expr: redis_up == 0
        for: 1m
        labels: { severity: critical }
      - alert: RedisMemoryHigh
        expr: redis_memory_used_bytes / redis_memory_max_bytes > 0.9
        for: 5m
        labels: { severity: critical }
      - alert: RedisEvictions
        expr: rate(redis_evicted_keys_total[5m]) > 0
        for: 10m
        labels: { severity: warning }
      - alert: RedisReplicationBroken
        expr: redis_master_link_up == 0
        for: 1m
        labels: { severity: critical }
      - alert: RedisRejectedConnections
        expr: increase(redis_rejected_connections_total[5m]) > 0
        labels: { severity: warning }
      - alert: RedisLowHitRate
        expr: |
          rate(redis_keyspace_hits_total[10m])
          / (rate(redis_keyspace_hits_total[10m]) + rate(redis_keyspace_misses_total[10m])) < 0.8
        for: 30m
        labels: { severity: warning }
```

> 💡 監控帳號使用最小權限 ACL（見 [4.6](#46-資安相關設定) 的 `monitor` 使用者範例），並確認 exporter 需要的命令都已授權。指標名稱以實際使用的 exporter 版本為準。

### 8.9 備份與還原

> 🆕 **v2.0 新增**

⚠️ **v2.0 更正**：v1.0 的排程範例「`redis-cli BGSAVE && cp dump.rdb ...`」有時序問題：`BGSAVE` 為非同步，命令回傳時新快照尚未完成，`cp` 複製到的是**上一份**快照。RDB 檔案在產生過程中使用暫存檔名、完成後才以原子方式改名，因此**任何時間直接複製 `dump.rdb` 都是安全的**；若要確保取得最新快照，需等待 `LASTSAVE` 時間改變。

**備份方式比較**：

| 方式 | 適用版本 | 內容 | 說明 |
| --- | --- | --- | --- |
| 複製 `dump.rdb` | 全部 | 最近一次快照 | 最簡單；可每小時複製一份並保留 48 小時 |
| `redis-cli --rdb <file>` | 全部 | 當下快照 | 從遠端節點（建議 Replica）取得，適合集中備份 |
| 複製 AOF 目錄 | 7.0+ | 快照 + 增量 | 需先暫停自動重寫（`auto-aof-rewrite-percentage 0`），確認無重寫進行中再複製 |
| **`BACKUP` 命令** | **8.10+** | BASE + INCR + manifest | 不需停止寫入或管理重寫；Cluster 可錯開各節點 fork 時間 |

**RDB 定時備份腳本（可用於 8.10 以前版本）**：

```bash
#!/usr/bin/env bash
set -euo pipefail
export REDISCLI_AUTH="$(cat /etc/redis/backup.pass)"
BACKUP_DIR=/backup/redis/$(hostname)
mkdir -p "$BACKUP_DIR"

before=$(redis-cli --user backup LASTSAVE)
redis-cli --user backup BGSAVE >/dev/null
# 等待新快照完成（最多 10 分鐘）
for _ in $(seq 1 600); do
  sleep 1
  [ "$(redis-cli --user backup LASTSAVE)" != "$before" ] && break
done
[ "$(redis-cli --user backup INFO persistence | grep -c 'rdb_last_bgsave_status:ok')" -eq 1 ]

cp /var/lib/redis/dump.rdb "$BACKUP_DIR/dump-$(date +%Y%m%d%H%M).rdb"
sha256sum "$BACKUP_DIR"/dump-*.rdb | tail -1 >> "$BACKUP_DIR/checksums.txt"

# 保留 48 小時的每小時備份；每日備份另行搬移並保留 30 天
find "$BACKUP_DIR" -name 'dump-*.rdb' -mmin +2880 -delete
```

**`BACKUP` 線上備份流程（8.10+）**：

```bash
BACKUP START          # 開啟備份視窗並產生 BASE 快照（不論是否啟用 AOF）
BACKUP LIST           # 取得已固定的檔案絕對路徑，可先開始複製 BASE
BACKUP SEAL           # 凍結備份：產生 INCR 硬連結與 manifest
BACKUP LIST           # 此時包含 BASE、INCR、manifest
# ... 將檔案複製到備份儲存 ...
BACKUP CLEANUP        # 釋放檔案
BACKUP STATUS         # 任何時候查看狀態；BACKUP ABORT 可取消尚未 seal 的備份
```

```bash
# redis.conf：備份輸出目錄（啟動期參數，位於 dir 之下）
backupdirname backupdir
backup-sealed-ttl 0          # 0 = sealed 備份不會自動清除

# 還原：啟動時預先載入指定備份（只在啟動時生效）
preload-file aof:/restore/appendonly.aof.manifest
# 或載入單一 RDB
# preload-file rdb:/restore/dump.rdb
```

**備份與災難復原原則**：

| 原則 | 說明 |
| --- | --- |
| 3-2-1 | 至少 3 份、2 種媒介、1 份異地 |
| 在 Replica 備份 | 避免 Primary fork 影響線上延遲 |
| 加密與存取控制 | 備份檔含完整資料，需加密（例如 `gpg`、物件儲存伺服器端加密）並限制存取 |
| 定期還原演練 | 每季至少一次，驗證 RTO／RPO 與資料筆數 |
| 監控備份作業 | 備份失敗需告警，不可只依賴排程存在 |

### 8.10 💡 本章實務建議

- 建立 Prometheus + Grafana 監控與告警，至少涵蓋 [8.1](#81-常用監控指標) 的可用性、記憶體、複寫、持久化指標。
- 每週以 `--keystats` 盤點 Big Key，每月以 `HOTKEYS` 盤點熱點，結果納入容量規劃。
- 延遲問題依「SLOWLOG → LATENCY DOCTOR → intrinsic latency → 網路」順序排查。
- 8.10 以上優先使用 `BACKUP` 命令；所有備份都要加密、異地保存並定期還原演練。

---

## 9. Redis 系統升級與版本管理

### 9.1 升級前評估事項

**檢查清單**：

- [ ] 確認目前版本（`INFO server` 的 `redis_version`）與目標版本，並閱讀**中間每一個 minor 版本**的 Release Notes
- [ ] 確認授權變更是否需要法務核准（7.2 → 7.4／8.x 授權不同，見 [1.6](#16-產品線授權與生態系)）
- [ ] 確認所有應用的 client library 版本支援目標版本（特別是 RESP3 預設協定與新命令）
- [ ] 比對設定檔：已移除或更名的參數、預設值變更
- [ ] 檢查 ACL 規則在新版命令分類下的實際權限（8.0 起模組命令納入既有 ACL 類別）
- [ ] 評估資料格式相容性：新版 RDB 無法被舊版讀取
- [ ] 準備回滾計畫與**升級前**的完整備份
- [ ] 在與生產相同版本、相同資料量的測試環境完成演練與壓測
- [ ] 安排維護視窗並通知相關團隊

**版本差異重點**：

| 版本 | 重要變更 | 升級注意 |
| --- | --- | --- |
| 6.0 | ACL、TLS、RESP3、I/O threads | `slave-*` 參數改名為 `replica-*`（舊名仍相容） |
| 6.2 | `GETDEL`／`GETEX`、`ZRANGE` 統一語法、`LMOVE` | 多個舊命令標示可被取代 |
| 7.0 | Functions、Multi-part AOF、Sharded Pub/Sub、ACL selectors、`save` 預設值變更 | AOF 目錄結構改變；`DEBUG`／`MODULE`／保護性設定預設停用 |
| 7.2 | 最後的 BSD 授權版本 | — |
| 7.4 | Hash 欄位 TTL | 授權改為 RSALv2／SSPLv1 |
| 8.0 | Redis Stack 模組內建、Vector Set、新 ACL 類別對應 | 授權新增 AGPLv3；檢查 ACL |
| 8.2 | Stream 刪除策略、`BITOP` 新運算子、`CLUSTER SLOT-STATS` | — |
| 8.4 | `SET IFEQ`、`DELEX`、`MSETEX`、原子 slot 遷移、`FT.HYBRID` | Query Engine 預設計分器改為 BM25STD |
| 8.6 | `XADD IDMP`、`HOTKEYS`、`*-lrm`、TLS 憑證自動認證 | — |
| 8.8 | Array、`INCREX`、`XNACK` | — |
| 8.10 | Compact hashes、`BACKUP`、`LMOVEM` | reshard／rebalance 改用原子 slot 遷移 |

### 9.2 Rolling Upgrade 策略

**核心原則**：**先升級 Replica，再透過故障轉移讓已升級的 Replica 成為 Primary，最後升級舊 Primary**。Redis 支援「舊版 Primary → 新版 Replica」的複寫，**不支援**「新版 Primary → 舊版 Replica」。

#### Sentinel 架構升級流程

```mermaid
flowchart TB
    A[開始：備份 RDB/AOF 與設定] --> B[升級 Replica 1]
    B --> C[驗證：版本、master_link_status:up、offset 追上]
    C --> D[升級 Replica 2 並驗證]
    D --> E[SENTINEL FAILOVER<br/>讓已升級 Replica 成為 Primary]
    E --> F[確認應用已連到新 Primary]
    F --> G[升級舊 Primary（現為 Replica）]
    G --> H[逐一升級 Sentinel]
    H --> I[觀察 24 小時後才啟用新版功能]
```

```bash
# ===== 1. 逐一升級 Replica =====
redis-cli -h replica-1 INFO replication | grep -E 'role|master_link_status'
sudo systemctl stop redis-server
sudo cp -a /etc/redis/redis.conf /backup/redis.conf.$(date +%F)

# 解除版本鎖定 → 安裝指定版本 → 重新鎖定
sudo apt-mark unhold redis
sudo apt-get install -y redis=<目標套件版本>
sudo apt-mark hold redis

sudo systemctl start redis-server
redis-cli -h replica-1 INFO server | grep redis_version

# ===== 2. 確認複寫正常且追上 =====
redis-cli -h replica-1 INFO replication | grep -E 'master_link_status|slave_repl_offset'
redis-cli -h primary INFO replication | grep master_repl_offset

# ===== 3. 手動故障轉移 =====
redis-cli -p 26379 SENTINEL FAILOVER mymaster
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# ===== 4. 升級舊 Primary（此時為 Replica）：重複步驟 1～2 =====

# ===== 5. 逐一升級 Sentinel（一次一個，確認其餘 Sentinel 仍達 quorum）=====
redis-cli -p 26379 SENTINEL CKQUORUM mymaster
```

#### Cluster 架構升級流程

⚠️ **v2.0 更正**：v1.0 寫「對每個 Replica 先執行 `CLUSTER FAILOVER` 再升級」順序錯誤。正確做法是先升級 Replica，再在**已升級的 Replica 上**執行 `CLUSTER FAILOVER` 讓它接手，最後升級原 Primary。

```bash
# 對每個 shard 重複以下步驟（一次只處理一個 shard）

# 1. 升級該 shard 的 Replica 並確認同步
redis-cli -h replica-a INFO replication | grep master_link_status

# 2. 在已升級的 Replica 上執行手動故障轉移（安全、不遺失資料）
redis-cli -h replica-a CLUSTER FAILOVER

# 3. 確認角色互換後，升級原 Primary（現為 Replica）
redis-cli -h replica-a ROLE
redis-cli -h old-primary ROLE

# 4. 全部完成後驗證叢集
redis-cli --cluster check redis-0.internal:6379
redis-cli -h redis-0.internal CLUSTER INFO | grep -E 'cluster_state|cluster_slots_ok'
```

> 💡 叢集升級過程中會短暫存在混合版本；**在全部節點完成升級前，不要使用新版本才有的命令或資料型別**，否則舊版節點接手時會失敗或無法載入資料。

### 9.3 升級風險與回滾策略

**風險評估**：

| 風險 | 機率 | 影響 | 緩解措施 |
| --- | --- | --- | --- |
| 設定參數不相容 | 中 | 服務無法啟動 | 測試環境先以相同設定啟動 |
| Client 不相容（RESP3、新回應格式） | 中 | 應用錯誤 | 先升級 client 並回歸測試 |
| ACL 權限範圍改變 | 中 | 權限過大或功能失效 | 升級後以 `ACL DRYRUN` 驗證關鍵帳號 |
| 效能退化 | 低 | 延遲增加 | 升級前後壓測比對 |
| 資料無法回滾 | 高（一旦新版寫入） | 無法降級 | 保留升級前備份、分階段升級 |

⚠️ **v2.0 更正**：v1.0 的回滾步驟「降級套件後直接以原資料目錄啟動」在跨大版本時通常會失敗：**新版產生的 RDB／AOF 無法被舊版讀取**。可行的回滾方式如下：

| 情境 | 回滾方式 | 代價 |
| --- | --- | --- |
| 只升級了 Replica，尚未 failover | 將該 Replica 降版並清空資料，重新從舊版 Primary 全量同步 | 無資料遺失 |
| 已 failover、新版 Primary 已接受寫入 | 以**升級前的備份**還原到舊版節點 | 遺失升級後寫入的資料 |
| 純快取實例 | 直接降版並以空資料集啟動，由應用回填 | 短暫命中率下降 |

```bash
# 以升級前備份回滾（會遺失升級後的寫入）
sudo systemctl stop redis-server
sudo apt-get install -y --allow-downgrades redis=<舊版套件版本>
sudo cp /backup/redis.conf.<date> /etc/redis/redis.conf
sudo rm -rf /var/lib/redis/appendonlydir /var/lib/redis/dump.rdb
sudo cp /backup/dump-before-upgrade.rdb /var/lib/redis/dump.rdb
sudo chown redis:redis /var/lib/redis/dump.rdb
# 若 appendonly yes：先以 appendonly no 啟動載入 RDB，再以 CONFIG SET appendonly yes 產生新的 AOF
sudo systemctl start redis-server
redis-cli INFO server | grep redis_version
redis-cli DBSIZE
```

### 9.4 舊資料相容性說明

**RDB 相容性**：

- 新版可以讀取舊版產生的 RDB（向後相容）。
- 舊版**不保證**能讀取新版 RDB；使用了新型別（如 Vector Set、Array、Hash 欄位 TTL）的資料集更不可能被舊版載入。

**AOF 相容性**：

- 7.0 起為 Multi-part AOF（目錄 + manifest）；7.0 以前版本無法讀取。
- 從 7.0 以前升級時，Redis 會自動把舊的單一 AOF 轉為新格式。

**模組資料**：

- 過去使用 Redis Stack（RedisJSON、RediSearch 等模組）的資料，升級到 8.x 後由內建功能載入；升級前請確認模組版本與 8.x 內建版本的相容性，並在測試環境以實際 RDB 驗證載入。

```bash
# 升級前：取得一致的備份
redis-cli --user backup BGSAVE
# 等待 LASTSAVE 變更後複製（見 8.9）

# 升級後：驗證資料完整性
redis-cli INFO keyspace          # 比對 keys、expires 數量
redis-cli DBSIZE
redis-cli --keystats --top 20    # 比對大小分布
```

### 9.5 版本差異注意事項

#### Redis 7.x → 8.x 升級注意事項

> 🆕 **v2.0 新增**

| 項目 | 說明 | 建議行動 |
| --- | --- | --- |
| **授權** | 8.x 為 RSALv2／SSPLv1／AGPLv3 三擇一 | 法務確認並記錄 |
| **模組內建** | JSON、Query Engine、Time Series、機率型結構成為內建 | 移除自行載入的舊模組 `loadmodule` 設定，避免衝突 |
| **ACL 類別** | 8.0 起 Query Engine、JSON、Time Series、機率型結構命令納入既有 ACL 類別（如 `@read`、`@write`） | 原本 `+@read` 的帳號，升級後也可執行 `JSON.GET`、`FT.SEARCH` 等；以 `ACL DRYRUN` 檢查 |
| **新資料型別** | Vector Set、Array（8.8）、Compact hash 編碼（8.10） | 全部節點與 DR 環境升級完成前不要使用 |
| **Client** | 需使用支援 8.x 的 client；多數 client 新版預設 RESP3 | 先升級 client 並回歸測試 |
| **Query Engine 預設計分** | 8.4 起預設文字計分器為 BM25STD | 搜尋排序結果可能改變，需驗證 |
| **Cluster 維運** | 8.10 起 `redis-cli --cluster reshard／rebalance` 使用原子 slot 遷移 | 更新維運手冊 |
| **安全修補** | 2025-10 起多個 Lua、`RESTORE` 相關 RCE | 升級到該分支最新修補版 |

#### Redis 6.x → 7.x 注意事項（保留）

1. **AOF 格式變更**：改為 Multi-part AOF（`appenddirname`），備份腳本需改為複製整個目錄。
2. **預設值變更**：`save` 預設改為 `3600 1 300 100 60 10000`；`enable-debug-command`、`enable-module-command`、`enable-protected-configs` 預設為 `no`。
3. **新功能**：Functions（可取代部分 Lua 腳本）、ACL selectors、Sharded Pub/Sub。
4. **設定更名**：`slave-*` → `replica-*`（6.0 開始，舊名仍相容）。

### 9.6 支援週期與版本策略

> 🆕 **v2.0 新增**

**Redis Open Source 各分支狀態（2026-09-29 彙整）**：

| 分支 | GA | 最新修補版 | 狀態 | 安全支援結束（參考） |
| --- | --- | --- | --- | --- |
| 8.10 | 2026-07 | 8.10.2（2026-09-17） | **現行主線** | 進行中 |
| 8.8 | 2026-05 | 8.8.3（2026-09-17） | 僅安全修補 | 進行中 |
| 8.6 | 2026-02 | 8.6.7（2026-09-17） | 僅安全修補 | 進行中 |
| 8.4 | 2025-11 | 8.4.7（2026-09-17） | 僅安全修補 | 進行中 |
| 8.2 | 2025-08 | 8.2.10（2026-09-17） | 僅安全修補 | 2030-09-01 |
| 8.0 | 2025-05 | 8.0.6 | 僅安全修補 | **2026-12-01** |
| 7.4 | 2024-07 | 7.4.11 | 僅安全修補 | 2029-12-01 |
| 7.2 | 2023-08 | 7.2.16 | 僅安全修補 | 2029-12-01 |
| 6.2 | 2021-02 | 6.2.24 | 僅安全修補 | 2027-04-01 |
| 7.0 及更早（除 6.2） | — | — | **已終止** | 已結束 |

> ⚠️ 「安全支援結束」欄位彙整自 endoflife.date，Redis 官方對 Open Source 各分支的支援承諾請以官方公告為準（見[附錄 D.1](#d1-待確認事項)）。**8.0 的安全支援將於 2026-12-01 結束**，仍在 8.0 的系統應盡速規劃升級。

**企業版本策略建議**：

| 策略 | 說明 |
| --- | --- |
| N 或 N-1 | 生產環境維持在現行主線或前一個 minor 版本 |
| 修補版 30 天內套用 | `SECURITY` 等級的修補版應在 30 天內（CVSS ≥ 9 時 7 天內）完成 |
| 每年至少一次 minor 升級 | 避免與主線差距過大，造成一次性大跨度升級 |
| 環境一致 | 開發、測試、生產、DR 使用相同版本 |
| 版本清冊 | 以 CMDB 記錄每個實例的版本、授權與負責人 |

### 9.7 💡 本章實務建議

- 升級一律「先 Replica、後 Primary」，並以手動故障轉移切換；禁止直接停機升級 Primary。
- 升級前完成備份並確認回滾方式；理解跨版本升級後**資料無法原地降級**。
- 升級後立即以 `ACL DRYRUN` 驗證關鍵帳號權限，特別是 7.x → 8.x。
- 建立版本清冊與修補 SLA，並追蹤 [9.6](#96-支援週期與版本策略) 的支援期限。

---

## 10. 資安與風險控管

### 10.1 Redis 常見資安風險

Redis 官方安全模型的前提是：**Redis 應只被受信任環境中的受信任客戶端存取**。一旦暴露或權限過大，單一命令即可清空資料或危及主機。

```mermaid
flowchart TB
    subgraph Vectors["常見攻擊向量"]
        A[未授權存取] --> A1[無密碼／弱密碼]
        A --> A2[6379 暴露於公網或過大內網區段]
        B[權限濫用] --> B1[應用帳號可執行 CONFIG／FLUSHALL]
        B --> B2[可執行 Lua 腳本 → 觸發引擎漏洞]
        B --> B3[可執行 RESTORE → 載入惡意序列化資料]
        C[資料外洩] --> C1[傳輸未加密]
        C --> C2[備份檔未加密]
        C --> C3[Key 名稱或值含個資]
        D[服務中斷] --> D1[記憶體耗盡]
        D --> D2[KEYS／大 key 阻塞]
    end
```

**歷史案例**：

| 案例 | 說明 |
| --- | --- |
| 未授權存取寫入 SSH 金鑰 | 攻擊者對無密碼且暴露的 Redis 執行 `CONFIG SET dir /root/.ssh` 與 `CONFIG SET dbfilename authorized_keys`，再以 `SAVE` 寫入公鑰取得主機權限；此類攻擊促使 Redis 3.2 引入 protected mode |
| 挖礦／勒索 | 大量暴露於公網的 Redis 被植入排程任務或清空資料後留下勒索訊息 |
| CVE-2015-4335 | Redis 2.8.21／3.0.2 以前版本，攻擊者可透過 `EVAL` 執行任意 Lua 位元組碼 |
| CVE-2025-49844（RediShell） | Lua 垃圾回收相關 use-after-free，已認證使用者可藉惡意 Lua 腳本達成遠端程式碼執行，CVSS 10.0（見 [10.6](#106-cve-應變與修補管理)） |

⚠️ **v2.0 更正**：v1.0 將 CVE-2015-4335 描述為「未授權存取漏洞：可寫入 SSH 公鑰」並不正確。CVE-2015-4335 是 **Lua 沙箱／位元組碼執行**漏洞；寫入 SSH 公鑰屬於「未授權存取 + `CONFIG` 濫用」的攻擊手法，並非單一 CVE。

### 10.2 內網 / 外網使用原則

**原則**：

1. ❌ **永遠不要**將 Redis 直接暴露在公網。
2. ✅ 只放在資料區（Data Zone），僅允許應用伺服器所在網段連線。
3. ✅ 維運人員透過堡壘機／VPN 存取，並留存稽核紀錄。
4. ✅ 雲端環境使用 Security Group／NSG 與私有端點（Private Link／PSC）。
5. ✅ 以非 root 的專用 `redis` 帳號執行服務。

**網路架構建議**：

```mermaid
flowchart LR
    subgraph Internet["Public Network"]
        U[User]
    end
    subgraph DMZ["DMZ"]
        LB[Load Balancer / WAF]
    end
    subgraph AppZone["Application Zone"]
        APP[Application Server]
    end
    subgraph DataZone["Data Zone"]
        REDIS[(Redis)]
        DB[(Database)]
    end
    subgraph MgmtZone["Management Zone"]
        BASTION[堡壘機]
    end
    U --> LB --> APP
    APP -->|TLS 6379| REDIS
    APP --> DB
    BASTION -->|TLS + 稽核| REDIS
```

**防火牆設定範例**：

```bash
# nftables／iptables：僅允許應用網段與堡壘機
iptables -A INPUT -p tcp --dport 6379 -s 10.0.10.0/24 -j ACCEPT   # 應用網段
iptables -A INPUT -p tcp --dport 6379 -s 10.0.99.5/32 -j ACCEPT   # 堡壘機
iptables -A INPUT -p tcp --dport 6379 -j DROP

# Cluster 另需開放節點間 bus port（預設為資料 port + 10000，即 16379），且只允許叢集節點之間互連
iptables -A INPUT -p tcp --dport 16379 -s 10.0.1.0/28 -j ACCEPT
iptables -A INPUT -p tcp --dport 16379 -j DROP
```

```bash
# redis.conf
bind 127.0.0.1 -::1 10.0.1.10
protected-mode yes
```

### 10.3 ACL 與權限控管

**ACL 規則語法速查**：

| 規則 | 意義 |
| --- | --- |
| `on` / `off` | 啟用／停用使用者 |
| `>password` / `#<sha256>` | 新增密碼（明文／SHA-256 雜湊）；設定檔建議使用雜湊 |
| `~pattern` | 允許存取的 key 模式（讀寫） |
| `%R~pattern` / `%W~pattern` | 只讀／只寫的 key 模式（7.0+） |
| `&pattern` | 允許的 Pub/Sub 頻道（7.0 起預設 `resetchannels`，需明確授權） |
| `+@category` / `-@category` | 允許／禁止一類命令（`ACL CAT` 可列出所有類別） |
| `+command` / `-command` / `+command\|sub` | 允許／禁止單一命令或子命令 |
| `(...)` | Selector：附加一組獨立的權限規則（7.0+） |
| `reset` | 重設為無權限狀態 |

**企業角色範本**：

```bash
# /etc/redis/users.acl

# 停用預設使用者
user default off

# 1. 管理員（僅維運人員，透過堡壘機使用）
user admin on #<sha256-of-password> ~* &* +@all

# 2. 應用程式：限定前綴；禁止危險、管理、腳本類命令
user app_order on #<sha256> ~order:* ~cache:order:* ~{order}:* &order:* +@all -@dangerous -@admin -@scripting

# 3. 需要執行已審核 Functions 的應用：只開放 FCALL，不開放 EVAL／FUNCTION LOAD
user app_inventory on #<sha256> ~stock:* +@read +@write +@connection +fcall +fcall_ro -@dangerous

# 4. 讀寫分離：一般 key 唯讀、特定前綴可寫（7.0+ 讀寫權限分離）
user app_report on #<sha256> %R~* %W~report:* +@read +@write +@connection -@dangerous

# 5. 唯讀帳號（Redis Insight 檢視、稽核）
user readonly on #<sha256> ~* &* +@read +@connection -@dangerous

# 6. 複寫帳號（Replica 使用 masteruser）
user repl_user on #<sha256> +psync +replconf +ping

# 7. 監控帳號（exporter）
user monitor on #<sha256> +client|list +info +ping +config|get +latency +slowlog|get +cluster|info +cluster|nodes

# 8. 備份帳號
user backup on #<sha256> +bgsave +lastsave +info +ping
```

```bash
# 產生高強度密碼與雜湊
ACL GENPASS                                   # 產生 64 個十六進位字元的隨機密碼
echo -n 'the-password' | sha256sum            # 設定檔中以 #<hash> 保存

# 載入、檢視、測試
ACL LOAD
ACL LIST
ACL GETUSER app_order
ACL DRYRUN app_order SET order:1001 x         # OK
ACL DRYRUN app_order FLUSHALL                 # 權限不足
ACL DRYRUN app_order EVAL "return 1" 0        # 權限不足

# 稽核：拒絕紀錄（認證失敗、命令或 key 權限不足）
ACL LOG 20
ACL LOG RESET
```

> 💡 **8.0 ACL 注意**：8.0 起 JSON、Query Engine、Time Series、機率型結構的命令被納入 `@read`、`@write` 等既有類別。若只想讓應用使用核心資料結構，需額外以 `-@search`、`-@json`、`-@timeseries` 等類別排除（可用 `ACL CAT` 確認實際類別名稱）。

### 10.4 防止誤刪與資料風險

**危險命令防護（以 ACL 為主）**：

| 命令／類別 | 風險 | 建議 |
| --- | --- | --- |
| `FLUSHALL`、`FLUSHDB` | 清空資料 | 應用帳號禁止（`-@dangerous` 已涵蓋） |
| `KEYS` | 阻塞服務 | 應用帳號禁止 |
| `CONFIG`、`DEBUG`、`MODULE`、`SHUTDOWN` | 變更設定、當機、載入模組 | 僅 admin；`DEBUG`／`MODULE` 另以 `enable-*-command no` 關閉 |
| `EVAL`、`EVALSHA`、`SCRIPT`、`FUNCTION` | 腳本引擎漏洞面 | 應用帳號預設禁止（`-@scripting`）；需要時只開放 `FCALL` 已審核函式 |
| `RESTORE`、`MIGRATE` | 載入序列化資料（近年多個 RCE 經由惡意 `RESTORE` 資料觸發） | 僅限維運帳號 |
| `MONITOR` | 洩漏所有命令內容（含資料） | 僅限 admin，且短時間使用 |
| `CLIENT KILL`、`CLIENT PAUSE` | 中斷服務 | 僅限 admin |

⚠️ **v2.0 更正**：v1.0 以 `rename-command` 停用或改名危險命令。此方法已被官方標示為**不建議使用**，且改名後的命令名稱會寫入 AOF 與複寫流，各節點設定不一致時會造成載入或複寫失敗。請改用上述 ACL 規則。

**操作安全規範**：

```bash
# ❌ 危險操作
KEYS *
FLUSHALL
DEL big:key                     # 大 key 同步刪除阻塞主執行緒

# ✅ 安全替代
SCAN 0 MATCH "cache:*" COUNT 1000
UNLINK big:key                  # 背景釋放
# 大量刪除：以 SCAN 分批 + UNLINK，並控制速率（見 12.2）
```

**誤刪後的救援**：

| 情境 | 救援方式 |
| --- | --- |
| 已開啟 AOF 且尚未重寫 | 立即停止自動重寫與服務、備份 AOF 目錄，從最後的 INCR 檔移除 `FLUSHALL` 等誤操作命令後重啟 |
| 只有 RDB | 從最近的備份還原（遺失備份後的寫入） |
| 有 Replica 且尚未同步誤操作 | 機率極低（複寫幾乎即時），不可依賴 |

### 10.5 實務安全建議

**安全設定基線**：

```bash
# ===== 1. 網路 =====
bind 127.0.0.1 -::1 10.0.1.10
protected-mode yes
port 0                              # 關閉明文連線埠
tls-port 6379

# ===== 2. 認證與授權 =====
aclfile /etc/redis/users.acl
acllog-max-len 256

# ===== 3. 高風險功能 =====
enable-debug-command no
enable-module-command no
enable-protected-configs no

# ===== 4. 資源限制 =====
maxclients 10000
maxmemory 10gb
maxmemory-policy allkeys-lfu

# ===== 5. 日誌 =====
loglevel notice
logfile /var/log/redis/redis-server.log

# ===== 6. TLS =====
tls-cert-file /etc/redis/tls/redis.crt
tls-key-file /etc/redis/tls/redis.key
tls-ca-cert-file /etc/redis/tls/ca.crt
tls-auth-clients yes                # 要求客戶端憑證（mTLS）；可設 optional
tls-replication yes                 # 複寫連線使用 TLS
tls-cluster yes                     # Cluster bus 使用 TLS
tls-protocols "TLSv1.2 TLSv1.3"
tls-prefer-server-ciphers yes
```

⚠️ **v2.0 更正**：v1.0 範例同時保留 `port 6379` 與 `tls-port 6380`，等於明文連線仍然開放，TLS 形同虛設。若要求全面加密，應設定 `port 0` 關閉明文埠。

**TLS 設定（加密傳輸）**：

```bash
# 測試用自簽 CA 與伺服器憑證（生產環境請使用企業 PKI）
openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes -sha256 -key ca.key -days 3650 -subj "/CN=Redis-CA" -out ca.crt

openssl genrsa -out redis.key 2048
openssl req -new -sha256 -key redis.key -subj "/CN=redis.internal" -out redis.csr
# 加入 SAN，讓客戶端能以主機名稱驗證
printf "subjectAltName=DNS:redis.internal,IP:10.0.1.10\n" > san.ext
openssl x509 -req -sha256 -in redis.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -days 365 -extfile san.ext -out redis.crt

chmod 600 redis.key
chown redis:redis redis.key redis.crt ca.crt

# 以 TLS 連線（mTLS 時需提供客戶端憑證）
redis-cli --tls --cacert ca.crt --cert client.crt --key client.key -h redis.internal -p 6379
```

> 🆕 **憑證式自動認證（8.6+）**：設定 `tls-auth-clients-user CN` 後，客戶端完成 mTLS 交握時，Redis 會以客戶端憑證的 Common Name 對應同名 ACL 使用者自動登入，無需在應用程式保存 Redis 密碼（預設 `off`）。8.10 另支援節點間（server-to-server）的憑證式認證。導入前請確認憑證簽發流程能保證 CN 唯一且不可偽造；2026-08 修補版曾修正「CN 內含 NUL 字元可冒用其他使用者」的弱點，務必使用最新修補版。

### 10.6 CVE 應變與修補管理

> 🆕 **v2.0 新增**

**近期重大 CVE 時間軸（摘要）**：

| 公告時間 | CVE／問題 | 類型 | 前提條件 | 已修補版本（各分支首個修補版） |
| --- | --- | --- | --- | --- |
| 2025-07 | CVE-2025-32023 | HyperLogLog 越界寫入 | 已認證 | 8.2.0 及各分支同期修補版 |
| 2025-10-03 | **CVE-2025-49844**（RediShell，CVSS 10.0） | Lua use-after-free → RCE | 已認證且可執行 Lua | 6.2.20、7.2.11、7.4.6、8.0.4、8.2.2 |
| 2025-10-03 | CVE-2025-46817／46818／46819 | Lua 整數溢位 RCE／以他人身分執行／越界讀取 | 已認證且可執行 Lua | 同上 |
| 2025-11 | CVE-2025-62507 | `XACKDEL` 堆疊溢位 → 可能 RCE | 已認證 | 8.2.3 |
| 2026-05 | CVE-2026-23479、23631、25243、25588、25589 | 解除阻塞流程 UAF、Lua UAF、惡意 `RESTORE` 資料 → RCE | 已認證 | 8.2.6、8.4.3、8.6.3、8.8.0 |
| 2026-08 | CVE-2026-62356 等 | CMSketch RDB 載入堆積越界寫入、惡意 RDB `SLOT_INFO` 記憶體破壞、TLS 憑證 CN 認證繞過、ACL key 權限繞過 | 已認證或可提供 RDB／憑證 | 8.2.9、8.4.6、8.6.6、8.8.2、8.10.1 |
| 2026-09-17 | 交易中的 ACL 繞過、Cluster bus 認證強化 | 權限繞過 | 已認證 | 8.2.10、8.4.7、8.6.7、8.8.3、8.10.2 |

> 各 CVE 的完整影響版本與修補版本請以 [Redis GitHub Security Advisories](https://github.com/redis/redis/security/advisories) 與各版 Release Notes 為準。

**關鍵觀察**：幾乎所有近期重大漏洞都需要「已認證」才能利用，因此**最小權限 ACL 是最有效的縱深防禦**：應用帳號若無法執行 `EVAL`、`RESTORE`，即使尚未修補也能大幅降低風險。

**CVE 應變流程**：

```mermaid
flowchart TD
    A[訂閱來源：GitHub Advisories、Release Notes、CERT] --> B[影響評估：版本清冊比對]
    B --> C{CVSS ≥ 9 或可遠端利用?}
    C -->|是| D[7 天內修補<br/>修補前先以 ACL 暫時禁用相關命令]
    C -->|否| E[30 天內隨例行修補]
    D --> F[依 9.2 滾動升級]
    E --> F
    F --> G[驗證版本與功能]
    G --> H[更新版本清冊與稽核紀錄]
```

**暫時性緩解（無法立即修補時）**：

```bash
# 以 ACL 禁止所有非管理帳號執行 Lua 與 RESTORE
ACL SETUSER app_order -@scripting -restore -restore-asking
ACL SAVE
# 確認
ACL DRYRUN app_order EVAL "return 1" 0
```

### 10.7 合規與稽核對應

> 🆕 **v2.0 新增**

| 控制目標 | Redis 對應措施 | 可提供的稽核證據 |
| --- | --- | --- |
| 存取控制（最小權限） | ACL 角色範本、停用 default 使用者 | `ACL LIST` 輸出、ACL 檔版本紀錄 |
| 身分鑑別 | 每個應用獨立帳號、強密碼或 mTLS | ACL 設定、密碼輪替紀錄 |
| 傳輸加密 | TLS 1.2+、`port 0` | `CONFIG GET tls-*`、`CONFIG GET port` |
| 靜態資料保護 | 磁碟加密（LUKS／雲端磁碟加密）、備份加密 | 主機與備份加密設定 |
| 日誌與監控 | 認證失敗告警、`ACL LOG`、堡壘機操作紀錄 | 告警紀錄、ACL LOG 匯出 |
| 弱點管理 | 版本清冊、修補 SLA | 修補紀錄、版本清冊 |
| 備份與復原 | 加密異地備份、還原演練 | 備份報表、演練紀錄 |
| 個人資料保護 | Key 不含個資明文、敏感值加密或雜湊、TTL 控制保存期限 | 資料盤點與 Key 命名規範 |

> 💡 Redis 本身不提供「逐筆命令」的完整稽核日誌（`MONITOR` 不適合常態使用）。若法規要求記錄資料存取，應在應用層或堡壘機記錄操作，Redis 端以 ACL LOG 記錄拒絕事件。

### 10.8 💡 本章實務建議

- 每個應用使用獨立 ACL 帳號與 key 前綴，預設禁止 `@dangerous`、`@admin`、`@scripting`。
- 生產環境啟用 TLS 並關閉明文埠；複寫與 Cluster bus 一併加密。
- 建立 CVE 應變流程：7 天（重大）／30 天（一般）修補 SLA，修補前以 ACL 暫時緩解。
- 備份檔視同正式資料，必須加密、限制存取並定期演練還原。

---

## 11. Redis Best Practices（最佳實務）

### 11.1 Key 設計原則

**命名規範**：

```text
格式：{業務}:{模組}:{實體}:{識別碼}

✅ cache:user:profile:1001
✅ order:detail:ORD202609001
✅ cache:product:list:cat:electronics:page:1
✅ session:web:9f2c1a...
✅ lock:order:create:1001
✅ {tenant42}:cart:1001              # Cluster：同租戶資料落在同一 slot

❌ user_profile_1001                  # 無層級，無法以前綴授權或盤點
❌ UserProfile:1001                   # 大小寫混用，容易打錯
❌ 1001                               # 無語意
❌ cache:product:list:category:electronics:brand:apple:page:1:sort:price:order:asc  # 過長，改為雜湊
❌ user:alice@example.com             # key 含個資
```

**Key 設計要點**：

| 要點 | 說明 |
| --- | --- |
| 長度 | 建議 ≤ 100 bytes；查詢條件組合過長時，以 `cache:search:{sha1(條件)}` 取代 |
| 前綴對應 ACL | 每個服務擁有自己的前綴，ACL 以 `~prefix:*` 授權 |
| Cluster hash tag | 需要多 key 原子操作的資料使用相同 `{tag}`；但避免單一 tag 承載過多資料形成熱點 |
| 版本化 | 資料結構變更時使用 `cache:v2:user:1001`，舊版本 key 自然過期，避免新舊程式互相讀取錯誤格式 |
| 個資保護 | 以內部 ID 或雜湊取代 email、電話、身分證字號 |

### 11.2 避免的設計地雷

| 地雷 | 問題 | 解決方式 |
| --- | --- | --- |
| 使用 `KEYS *` | O(N) 阻塞 | 使用 `SCAN`；ACL 禁止 `KEYS` |
| Big Key（> 1 MB 或 > 5,000 元素） | 阻塞、複寫延遲、記憶體不均 | 拆分（見 [8.4](#84-key-分析與-big-key-問題)） |
| 無 TTL 快取 | 記憶體無限增長 | 所有快取設定 TTL，並加入抖動 |
| Hot Key | 單點瓶頸、Cluster 負載不均 | L1 本地快取、client-side caching、複製分片 |
| 以 Redis 為唯一資料來源 | 故障時資料遺失 | RDBMS 為真相來源 |
| 在 Cluster 使用跨 slot 多 key 命令 | `CROSSSLOT` 錯誤 | 設計 hash tag 或改為多次單 key 命令 |
| 在單一實例混放快取與不可遺失資料 | 淘汰策略衝突 | 依用途拆分實例 |
| 大量使用 `SELECT` 多 db 隔離租戶 | Cluster 不支援、ACL 無法依 db 授權 | 以 key 前綴 + ACL 隔離，或拆實例 |
| 在 Lua 中執行長迴圈 | 阻塞整個實例 | 限制腳本工作量；優先使用 8.x 原生命令 |
| 以 Pub/Sub 傳遞業務事件 | 離線即遺失 | 使用 Stream |

**Hot Key 處理**：

```java
// 方案 1：本地快取（Caffeine，取代已不建議的 Guava Cache）
private final LoadingCache<String, String> localCache = Caffeine.newBuilder()
        .maximumSize(10_000)
        .expireAfterWrite(Duration.ofSeconds(5))      // 短 TTL，容忍秒級不一致
        .refreshAfterWrite(Duration.ofSeconds(3))     // 背景刷新，避免同時過期
        .build(key -> stringRedisTemplate.opsForValue().get(key));

// 方案 2：複製分片（讀多寫少的熱點）
private static final int REPLICAS = 8;

public void setHot(String key, String value, Duration ttl) {
    // 寫入時必須更新全部副本，否則會讀到舊值
    stringRedisTemplate.executePipelined((RedisCallback<Object>) conn -> {
        StringRedisConnection c = (StringRedisConnection) conn;
        for (int i = 0; i < REPLICAS; i++) {
            c.set(key + ":r" + i, value, Expiration.from(ttl), RedisStringCommands.SetOption.upsert());
        }
        return null;
    });
}

public String getHot(String key) {
    int shard = ThreadLocalRandom.current().nextInt(REPLICAS);
    return stringRedisTemplate.opsForValue().get(key + ":r" + shard);
}
```

⚠️ **v2.0 更正**：v1.0 的 Key 分散範例只示範隨機讀取某個分片，未說明寫入時必須同步更新所有分片，否則會讀到不一致的資料。

### 11.3 高併發系統設計建議

```mermaid
flowchart TB
    A[Client] --> B[L1 本地快取<br/>Caffeine / client-side caching]
    B -->|未命中| C[L2 Redis Cluster]
    C -->|未命中| D[(L3 Database)]
    E[Write Request] --> D
    D -->|CDC／Outbox 事件| F[Stream / MQ]
    F --> G[Cache Invalidator]
    G -->|UNLINK| C
    G -->|廣播失效| B
```

**設計原則**：

1. **多層快取**

    ```text
    L1：本地快取（奈秒～微秒級，容量小，秒級 TTL）
    L2：Redis（次毫秒級，容量中）
    L3：資料庫（毫秒級，真相來源）
    ```

2. **讀寫分離（需評估一致性）**：Lettuce 可設定 `ReadFrom.REPLICA_PREFERRED` 讓讀取優先走 Replica，但讀取可能拿到毫秒～秒級的舊資料，只適用於可容忍延遲的查詢。

    ```java
    @Bean
    public LettuceClientConfigurationBuilderCustomizer readFromReplica() {
        return builder -> builder.readFrom(ReadFrom.REPLICA_PREFERRED);
    }
    ```

3. **以事件驅動快取失效**：DB 交易提交後才發送失效事件（Transactional Outbox 或 CDC），避免交易回滾卻已刪除快取。

    ```java
    @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
    public void onUserUpdated(UserUpdatedEvent event) {
        stringRedisTemplate.unlink("cache:user:" + event.userId());
    }
    ```

4. **批次與 Pipeline**：`MGET`／`MSETEX`／Pipeline 減少往返；單批控制在 100～1,000 個命令。

5. **避免同步放大**：一個 API 請求觸發數十次 Redis 呼叫時，應改為批次或重新設計資料結構。

### 11.4 與資料庫搭配策略

**快取一致性策略**：

```mermaid
flowchart TB
    A[更新請求] --> B[更新資料庫<br/>交易提交]
    B --> C[刪除快取 UNLINK]
    C --> D{刪除失敗?}
    D -->|是| E[寫入重試佇列<br/>或依 CDC 事件補刪]
    D -->|否| F[下次讀取時回填]
```

| 一致性需求 | 建議策略 |
| --- | --- |
| 秒級最終一致即可 | Cache-Aside + TTL + 更新後刪除 |
| 需要更快收斂 | 加上 CDC（如 Debezium）驅動的快取失效 |
| 必須讀到最新資料 | 該查詢直接讀 DB，不經快取 |

```java
@Service
public class UserService {

    private final UserRepository userRepository;
    private final StringRedisTemplate redis;
    private final ApplicationEventPublisher events;

    public UserService(UserRepository userRepository, StringRedisTemplate redis,
                       ApplicationEventPublisher events) {
        this.userRepository = userRepository;
        this.redis = redis;
        this.events = events;
    }

    @Transactional
    public User updateUser(User user) {
        User updated = userRepository.save(user);
        // 交易提交後才刪快取（見 11.3 的 AFTER_COMMIT 監聽器）
        events.publishEvent(new UserUpdatedEvent(user.getId()));
        return updated;
    }
}
```

⚠️ **v2.0 更正**：v1.0 在 `@Transactional` 方法內直接刪除快取；若交易稍後回滾，快取已被刪除雖然無害，但若在交易提交**前**就有其他請求讀取 DB 舊值並回填，快取會保留舊資料。改為交易提交後刪除可縮小不一致視窗。

**快取雪崩防護**：

```java
// TTL 加上 0～10% 隨機抖動，避免同時過期
public void setWithJitter(String key, String value, Duration baseTtl) {
    long extra = (long) (baseTtl.toMillis() * ThreadLocalRandom.current().nextDouble(0.1));
    redis.opsForValue().set(key, value, baseTtl.plusMillis(extra));
}
```

### 11.5 團隊使用規範建議

**Redis 使用規範文件範本**：

```markdown
# Redis 使用規範 v2.0

## 1. Key 命名
- 格式：{業務}:{模組}:{實體}:{識別碼}，全小寫、冒號分隔
- 長度 ≤ 100 bytes；不得包含個資明文
- 每個服務使用專屬前綴，並申請對應 ACL 帳號

## 2. TTL
- 所有快取 key 必須設定 TTL，並加入 0～10% 抖動
- Session：30 分鐘（滑動）；使用者資料：1～24 小時；列表／搜尋：5～30 分鐘；設定：1～7 天

## 3. 資料大小
- String ≤ 100 KB；集合型元素數 ≤ 5,000；單一元素 ≤ 10 KB
- Stream 必須有 MAXLEN 或定期 XTRIM

## 4. 禁止事項
- 禁止 KEYS、FLUSHALL、FLUSHDB、MONITOR（應用程式中）
- 禁止在應用程式中使用 EVAL；伺服器端邏輯以已審核的 Functions 發布
- 禁止儲存密碼、金鑰、完整卡號等敏感資料
- 禁止以 Pub/Sub 傳遞必須送達的業務事件

## 5. 效能
- 單一命令伺服器端執行時間 < 1 ms（慢查詢門檻 10 ms）
- Pipeline 單批 100～1,000 個命令
- 共用 client 實例；禁止每次請求建立連線

## 6. 可靠性
- 所有 Redis 呼叫必須設定逾時，並具備降級路徑
- 分散式鎖必須使用隨機 token 並以原子方式釋放

## 7. 監控告警
- 記憶體使用率 > 80% 警告、> 90% 嚴重
- 命中率低於服務基線 20% 告警
- P99 延遲 > 10 ms 告警；複寫中斷立即告警

## 8. 變更管理
- 新增資料結構、ACL、Functions 需經架構審查
- 使用 8.x 新命令前，確認所有環境版本與 client 支援
```

### 11.6 容量規劃與成本估算

> 🆕 **v2.0 新增**

**記憶體估算步驟**：

1. 以代表性資料在測試環境寫入 10 萬筆，使用 `INFO memory` 的 `used_memory` 差值算出**每筆平均占用**（含 key、值、內部結構與 TTL 成本）。
2. 乘上預估筆數與成長率。
3. 加上複寫緩衝、客戶端緩衝與碎片餘裕。

```text
資料記憶體 = 每筆平均占用 × 預估筆數 × (1 + 年成長率)
maxmemory  ≥ 資料記憶體 × 1.2（碎片與緩衝餘裕）
主機記憶體 ≥ maxmemory ÷ 0.7（保留 fork copy-on-write、作業系統與其他程序）

範例：每筆 1.2 KB × 2,000 萬筆 × 1.3 = 31.2 GB
      maxmemory ≥ 37.4 GB → 超過單機建議值（約 25 GB）
      → 規劃 Cluster 3 shard，每 shard maxmemory 約 13 GB、主機 20 GB
```

**吞吐量估算**：

| 項目 | 經驗值（依硬體與命令而異，需壓測確認） |
| --- | --- |
| 單執行緒簡單命令（GET／SET，小值） | 每秒約 10 萬級 ops |
| 啟用 I/O threads（多核心） | 可再提升數倍 |
| Pipeline | 每秒可達百萬級 ops |

```bash
# 以 redis-benchmark 建立基線（請在獨立測試環境執行）
redis-benchmark -h redis.internal --tls --user bench -a "$PASS" \
  -t get,set -n 1000000 -c 100 -P 16 -d 512 --threads 4 -q
```

**成本最佳化**：

| 手段 | 效果 |
| --- | --- |
| 選用正確資料結構（小型 Hash 取代多個 String） | 減少 key 與指標開銷 |
| Compact hashes（8.10+）、`HIMPORT` | 大量同結構 Hash 顯著省記憶體 |
| 值壓縮（應用端 LZ4／Zstd） | 大型 JSON 可省 50% 以上 |
| 合理 TTL 與淘汰策略 | 只保留熱資料 |
| 分層儲存（Redis Software／Cloud 的 Flex） | 冷資料放 SSD |

### 11.7 服務等級目標（SLO）範例

> 🆕 **v2.0 新增**

| SLI | SLO 範例 | 量測方式 |
| --- | --- | --- |
| 可用性 | 月可用性 ≥ 99.95%（生產快取層） | 探測成功率 |
| 延遲 | 應用端量測 P99 ≤ 5 ms、P99.9 ≤ 20 ms | client 端指標（Micrometer 等） |
| 快取命中率 | ≥ 90%（依服務基線） | `keyspace_hits` 比例或應用端統計 |
| 故障轉移時間 | Sentinel／Cluster 故障轉移 ≤ 30 秒 | 演練實測 |
| RPO | 持久化實例 ≤ 1 秒 | AOF `everysec` |
| RTO | 單節點故障 ≤ 1 分鐘；整體重建 ≤ 1 小時 | 還原演練 |

### 11.8 💡 本章實務建議

- 以 [11.5](#115-團隊使用規範建議) 的規範範本建立團隊標準，並納入程式碼審查檢查項目。
- 容量規劃以實測的「每筆平均占用」計算，不要只用值的大小估算。
- 為 Redis 定義 SLO，並以故障演練驗證故障轉移時間與降級路徑。
- 熱點與大 key 是最常見的效能問題來源，設計階段就要預防。

---

## 12. 常見問題與除錯（FAQ / Troubleshooting）

### 12.1 Redis 掛掉怎麼辦

**診斷步驟**：

```bash
# 1. 服務狀態與最近日誌
sudo systemctl status redis-server
sudo journalctl -u redis-server -n 300 --no-pager
sudo tail -300 /var/log/redis/redis-server.log

# 2. 系統資源
free -h                               # 記憶體
df -h /var/lib/redis                  # 磁碟空間
dmesg -T | grep -iE 'oom|killed'      # 是否被 OOM Killer 終止

# 3. 連線埠
sudo ss -tlnp | grep 6379

# 4. 若為 Sentinel／Cluster，確認是否已自動故障轉移
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
redis-cli -c -h redis-0 CLUSTER INFO | grep cluster_state
```

**常見原因與解決**：

| 原因 | 日誌特徵 | 解決方式 |
| --- | --- | --- |
| OOM Killer | `dmesg` 出現 `Out of memory: Killed process ... (redis-server)` | 設定 `maxmemory`、保留 fork 餘裕、調整 `vm.overcommit_memory=1` |
| RDB 儲存失敗 | `Can't save in background: fork: Cannot allocate memory` | `vm.overcommit_memory=1`、確認磁碟空間與權限 |
| AOF 尾端截斷 | `Bad file format reading the append only file` 或 `short read` | 預設 `aof-load-truncated yes` 會自動略過；否則用 `redis-check-aof` 修復 |
| AOF 中段損壞 | 啟動中止並提示使用 `redis-check-aof` | 先備份，再以 `redis-check-aof` 分析（見下方） |
| 設定錯誤 | `FATAL CONFIG FILE ERROR` | 依提示行號修正設定檔 |
| 模組載入失敗（7.x 升 8.x） | `Module ... failed to load` | 移除舊的 `loadmodule`（8.x 已內建） |
| 磁碟滿 | `No space left on device` | 清理空間；確認 AOF 重寫未堆積 |

**緊急恢復**：

```bash
# 從 RDB 備份恢復
sudo systemctl stop redis-server
sudo cp /backup/dump-YYYYmmddHHMM.rdb /var/lib/redis/dump.rdb
sudo chown redis:redis /var/lib/redis/dump.rdb
# 若同時啟用 AOF，Redis 會優先載入 AOF；要以 RDB 還原需先移開 appendonlydir 並暫時 appendonly no
sudo systemctl start redis-server

# 修復 Multi-part AOF（7.0+）：以 manifest 檔為參數
sudo cp -a /var/lib/redis/appendonlydir /backup/appendonlydir.$(date +%s)
redis-check-aof /var/lib/redis/appendonlydir/appendonly.aof.manifest          # 先分析
redis-check-aof --fix /var/lib/redis/appendonlydir/appendonly.aof.manifest    # 確認後才修復
```

⚠️ **v2.0 更正**：v1.0 使用 `redis-check-aof --fix /var/lib/redis/appendonly.aof`，這是 7.0 以前單一 AOF 檔的路徑。7.0 起應指定 `appendonlydir` 內的 manifest 檔；修復前務必先備份，因為 `--fix` 會截斷損壞點之後的所有資料。

### 12.2 記憶體暴增如何處理

**診斷**：

```bash
redis-cli INFO memory | grep -E 'used_memory_human|used_memory_rss_human|mem_fragmentation_ratio|used_memory_dataset|mem_clients_normal|mem_replication_backlog'
redis-cli MEMORY STATS                # 記憶體組成明細
redis-cli MEMORY DOCTOR               # 文字化診斷建議
redis-cli INFO keyspace               # 各 db key 數與有 TTL 的 key 數
redis-cli --keystats --top 20 -i 0.01 # 找出大 key 與分布
redis-cli CLIENT LIST                 # 檢查 omem（輸出緩衝）異常大的連線
```

**處理方式**：

```mermaid
flowchart TD
    A[記憶體暴增] --> B{資料集成長?<br/>used_memory_dataset}
    B -->|是| C{Big Key?}
    C -->|是| D[拆分或 UNLINK]
    C -->|否| E{無 TTL 的 key 增加?<br/>keys 與 expires 差距}
    E -->|是| F[修正程式補上 TTL<br/>分批清理]
    E -->|否| G[容量不足：擴容或分片]
    B -->|否| H{客戶端緩衝大?<br/>mem_clients_normal}
    H -->|是| I[找出慢消費者<br/>Pub/Sub、MONITOR、大量 MGET]
    H -->|否| J{碎片率 > 1.5?}
    J -->|是| K[啟用 activedefrag<br/>或低峰期滾動重啟]
    J -->|否| L[檢查複寫 backlog 與 Lua 腳本快取]
```

**分批清理特定前綴的 key（安全做法）**：

```bash
# 以 SCAN 分批、UNLINK 背景刪除，並限速；先在 Replica 或測試環境確認範圍
redis-cli --scan --pattern 'cache:tmp:*' --count 1000 -i 0.01 \
  | xargs -r -n 500 redis-cli UNLINK
```

⚠️ **v2.0 更正**：v1.0 將 `redis-cli --scan --pattern "cache:*" | xargs -L 100 redis-cli DEL` 標示為「清理過期 Key」，但該指令會刪除**所有**符合前綴的 key（不論是否過期），且 `DEL` 大 key 會阻塞。過期 key 由 Redis 自動回收，無需手動清理；需要刪除特定資料時請使用上述 `UNLINK` 分批作法並確認範圍。

```bash
# 調整淘汰策略與上限（記得 CONFIG REWRITE）
redis-cli CONFIG SET maxmemory-policy allkeys-lfu
redis-cli CONFIG SET maxmemory 12gb
redis-cli CONFIG REWRITE
```

### 12.3 Hit Rate 過低的原因

**診斷**：

```bash
redis-cli INFO stats | grep -E 'keyspace_hits|keyspace_misses|evicted_keys|expired_keys'
# 命中率 = hits / (hits + misses)
```

**常見原因與解決**：

| 原因 | 檢查方式 | 解決方式 |
| --- | --- | --- |
| TTL 過短 | 抽查 `TTL`；`expired_keys` 增加很快 | 依更新頻率延長 TTL，搭配主動失效 |
| 記憶體不足被淘汰 | `evicted_keys` 持續增加 | 擴容、改用 LFU、縮小值大小 |
| 快取未回填 | 程式碼審查；未命中後 key 仍不存在 | 確保 Cache-Aside 正確實作 |
| 快取穿透 | 大量查詢不存在的 ID | 空值標記、Bloom filter（見 [6.7](#67-快取穿透擊穿與雪崩)） |
| Key 生成不一致 | 同一資料產生不同 key（大小寫、參數順序） | 統一 key 產生函式並正規化參數 |
| 資料更新頻繁 | 寫入後立即刪除，快取常態為空 | 評估是否適合快取，或改為寫入時更新 |
| 冷啟動 | 重啟或擴容後命中率驟降 | 預熱熱門資料、分批重啟 |
| 共用 `keyspace_hits` 統計 | 多個應用共用實例，指標被其他服務稀釋 | 以應用端指標計算各自命中率 |

### 12.4 Replication 延遲處理

**監控複寫狀態**：

```bash
# Primary 端
redis-cli INFO replication
# role:master
# connected_slaves:2
# slave0:ip=10.0.1.11,port=6379,state=online,offset=123456789,lag=0
# slave1:ip=10.0.2.11,port=6379,state=online,offset=123450000,lag=1
# master_repl_offset:123456789

# Replica 端
redis-cli INFO replication
# role:slave
# master_link_status:up
# master_last_io_seconds_ago:0
# master_sync_in_progress:0
# slave_repl_offset:123450000
```

**延遲原因與解決**：

| 原因 | 症狀 | 解決方式 |
| --- | --- | --- |
| 網路頻寬或延遲 | offset 差距持續增加 | 檢查網路、Replica 與 Primary 放在低延遲網段 |
| 大 key 寫入 | 寫入尖峰時延遲 | 避免 Big Key |
| Replica 讀取負載過高 | lag 隨讀取量波動 | 減少 Replica 讀流量或增加 Replica |
| `repl-backlog-size` 不足 | 斷線後頻繁全量同步（`sync_full` 增加） | 加大 backlog（見 [4.4](#44-replication-設定)） |
| 輸出緩衝上限過小 | 日誌出現 `scheduled to be closed ASAP for overcoming of output buffer limits` | 調高 `client-output-buffer-limit replica` |
| 全量同步耗時 | `master_sync_in_progress:1` 長時間 | 使用無碟複寫、縮小資料集 |

```bash
redis-cli CONFIG SET repl-backlog-size 512mb
redis-cli CONFIG SET client-output-buffer-limit "replica 1gb 256mb 60"
redis-cli CONFIG REWRITE
```

### 12.5 實務案例分享

#### 案例 1：生產環境 Redis 突然變慢

**現象**：API P99 延遲從 50 ms 上升到 500 ms。

**診斷過程**：

```bash
# 1. 慢查詢
redis-cli SLOWLOG GET 10
# 發現大量 KEYS order:* 命令

# 2. 追查來源（client-name 設定得好，這一步會很快）
redis-cli CLIENT LIST | grep -i keys

# 3. 確認原因：排程程式以 KEYS 盤點訂單 key
```

**解決**：

- 立即停止該排程；改為 `SCAN` 分批並於 Replica 執行。
- 以 ACL 從所有應用帳號移除 `KEYS`：`ACL SETUSER app_batch -keys`。
- 將「禁止 KEYS」納入程式碼審查與團隊規範。

⚠️ **v2.0 更正**：v1.0 建議設定 `rename-command KEYS ""`；本版改以 ACL 管控（見 [10.4](#104-防止誤刪與資料風險)）。

---

#### 案例 2：快取雪崩導致資料庫過載

**現象**：資料庫 CPU 100%，大量逾時。

**原因**：批次作業在同一時間寫入大量快取並設定相同 TTL，1 小時後同時到期。

**解決**：

```java
// TTL 加上隨機抖動
public void setCache(String key, String value) {
    Duration base = Duration.ofHours(1);
    long extraSeconds = ThreadLocalRandom.current().nextLong(0, 600);   // 0～10 分鐘
    redis.opsForValue().set(key, value, base.plusSeconds(extraSeconds));
}

// 熱點資料提前背景刷新（Refresh-Ahead）
@Scheduled(fixedRate = 60_000)
public void refreshHotCache() {
    for (String key : hotKeys()) {
        Long ttl = redis.getExpire(key);
        if (ttl != null && ttl < 120) {
            reloadFromDatabase(key);
        }
    }
}
```

另於應用端加上 DB 連線池上限與熔斷，避免 Redis 或快取失效時拖垮 DB（見 [7.6](#76-timeout--retry--fallback-設計)）。

---

#### 案例 3：記憶體碎片導致 OOM

**現象**：`used_memory` 只有 6 GB，但 `used_memory_rss` 達到 12 GB，主機觸發 OOM Killer。

**診斷**：

```bash
redis-cli INFO memory | grep -E 'mem_fragmentation_ratio|allocator_frag_ratio'
# mem_fragmentation_ratio:2.0
redis-cli MEMORY DOCTOR
```

**解決**：

```bash
# 方案 1：啟用主動碎片整理（建議，線上生效）
redis-cli CONFIG SET activedefrag yes
redis-cli CONFIG REWRITE

# 方案 2：低峰期透過 failover 滾動重啟（Sentinel／Cluster 環境）

# 根本原因：值大小差異大且頻繁覆寫 → 調整資料設計，並確保 maxmemory 留有足夠餘裕
```

---

#### 案例 4：Sentinel 故障轉移後應用仍連舊 Primary

> 🆕 **v2.0 新增**

**現象**：故障轉移完成，但部分服務持續收到 `READONLY You can't write against a read only replica.`。

**原因**：應用以固定 IP 連線 Primary（未使用 Sentinel 模式），舊 Primary 恢復後成為 Replica。

**解決**：改用 client 的 Sentinel 連線模式；Lettuce 另可啟用 `DisconnectedBehavior.REJECT_COMMANDS` 讓錯誤快速浮現；並將故障轉移列入季度演練。

### 12.6 Cluster 常見錯誤

> 🆕 **v2.0 新增**

| 錯誤 | 意義 | 處理 |
| --- | --- | --- |
| `MOVED 3999 10.0.1.12:6379` | key 所屬 slot 在其他節點 | 使用 cluster-aware client（或 `redis-cli -c`）；client 需能刷新拓撲 |
| `ASK 3999 10.0.1.12:6379` | slot 正在遷移中 | 由 client 自動處理；8.4+ 原子 slot 遷移可大幅減少此情況 |
| `CROSSSLOT Keys in request don't hash to the same slot` | 多 key 命令跨 slot | 使用 hash tag `{...}`，或拆成單 key 命令 |
| `CLUSTERDOWN The cluster is down` | 有 slot 無人負責 | `redis-cli --cluster check` 找出缺失 slot；檢查節點與故障轉移 |
| `TRYAGAIN` | 遷移中的多 key 操作暫時無法執行 | 稍後重試 |
| 節點頻繁 `PFAIL`／`FAIL` | 節點逾時 | 檢查網路、`cluster-node-timeout`、大 key 或長命令造成的阻塞 |

```bash
redis-cli --cluster check redis-0.internal:6379
redis-cli --cluster fix redis-0.internal:6379        # 修復 slot 分配（先評估影響）
redis-cli -h redis-0.internal CLUSTER SHARDS         # 7.0+ 叢集拓撲（取代 CLUSTER SLOTS）
redis-cli -h redis-0.internal CLUSTER SLOT-STATS SLOTSRANGE 0 16383   # 8.2+ 每個 slot 的使用統計
```

### 12.7 升級後常見問題

> 🆕 **v2.0 新增**

| 症狀 | 可能原因 | 處理 |
| --- | --- | --- |
| 應用解析回應失敗（型別錯誤） | client 升級後預設改用 RESP3 | 回歸測試；必要時暫時指定 RESP2 |
| 啟動失敗：模組重複載入 | 8.x 已內建 JSON／Search 等功能，舊 `loadmodule` 仍存在 | 移除舊的 `loadmodule` 設定 |
| 帳號權限突然變大或變小 | 8.0 起模組命令納入既有 ACL 類別 | `ACL DRYRUN` 檢查並調整規則 |
| 搜尋排序改變 | 8.4 起預設文字計分器改為 BM25STD | 明確指定 `SCORER` 或接受新排序 |
| 舊 Replica 無法同步新 Primary | 新版 Primary → 舊版 Replica 不支援 | 依 [9.2](#92-rolling-upgrade-策略) 順序升級 |
| `ERR unknown command` | 使用了新命令但部分節點仍為舊版 | 全部升級後再啟用新功能 |

### 12.8 💡 本章實務建議

- 將本章表格整理成值班手冊（Runbook），並附上各環境的實際主機、帳號與告警連結。
- 所有「修復」類操作（`redis-check-aof --fix`、`--cluster fix`）執行前都要先備份。
- 每季進行一次故障演練：Primary 停機、Sentinel 故障轉移、Cluster 節點失效、從備份還原。
- 應用程式設定 `client-name`，可大幅縮短追查問題來源的時間。

---

## 13. 檢查清單（Checklist）

⚠️ **v2.0 更正**：本章子標題加上編號（13.1～13.6），修正 v1.0 目錄中「🛡️ 資安檢查」連結含不可見字元（U+FE0F）導致無法跳轉的問題。

### 13.1 🔧 部署前檢查

- [ ] 使用 Redis 8.10.x（或組織核准的分支最新修補版），並以套件鎖定版本
- [ ] 完成作業系統調校：`vm.overcommit_memory=1`、關閉 THP、`somaxconn`、檔案描述子上限、關閉 swap
- [ ] `bind` 只包含必要介面，`protected-mode yes`
- [ ] 以 `aclfile` 建立 ACL，停用 `default` 使用者，每個應用獨立帳號
- [ ] 啟用 TLS，`port 0` 關閉明文埠；複寫與 Cluster bus 同步加密
- [ ] 設定 `maxmemory` 與符合用途的淘汰策略
- [ ] 依資料性質設定持久化（RDB／AOF）
- [ ] 高可用：Sentinel ≥ 3 或 Cluster 每 shard ≥ 1 Replica，並跨可用區
- [ ] 防火牆只允許應用網段與堡壘機
- [ ] 監控（exporter + 告警）與備份排程上線
- [ ] 設定檔納入版本控制

### 13.2 📝 開發規範檢查

- [ ] Key 命名符合 `{業務}:{模組}:{實體}:{識別碼}`，不含個資
- [ ] 所有快取 key 設定 TTL，並加入抖動
- [ ] 無 Big Key（String ≤ 100 KB、集合 ≤ 5,000 元素）
- [ ] 不使用 `KEYS`、`FLUSHALL`；以 `SCAN`、`UNLINK` 取代
- [ ] 批次操作使用 `MGET`／`MSETEX`／Pipeline
- [ ] Cache-Aside：先更新 DB、再刪除快取（交易提交後）
- [ ] 快取穿透、擊穿、雪崩三項防護皆已實作
- [ ] 分散式鎖使用隨機 token，以 `DELEX IFEQ`（8.4+）或 Lua 原子釋放
- [ ] 所有 Redis 呼叫設定逾時、熔斷與降級路徑
- [ ] 值序列化使用有型別的序列化器，未啟用任意型別反序列化
- [ ] Cluster 環境的多 key 操作使用 hash tag
- [ ] 業務事件使用 Stream，消費端冪等並有死信處理

### 13.3 🔍 日常維運檢查

- [ ] 記憶體使用率 < 80%，碎片率 1.0～1.5
- [ ] 快取命中率符合服務基線
- [ ] 無持續的慢查詢（> 10 ms）
- [ ] 複寫連線正常、offset 差距穩定
- [ ] `evicted_keys`、`rejected_connections` 無異常增加
- [ ] RDB／AOF 狀態為 ok，備份作業成功且已異地保存
- [ ] 每週 `--keystats` 盤點大 key；每月 `HOTKEYS` 盤點熱點
- [ ] `ACL LOG` 無異常的認證失敗

### 13.4 🚀 升級前檢查

- [ ] 閱讀目前版本至目標版本之間所有 Release Notes
- [ ] 法務確認授權（跨 7.2 → 7.4／8.x 時）
- [ ] 所有 client 已升級並完成 RESP3 回歸測試
- [ ] 設定檔差異比對完成；移除 8.x 已內建模組的 `loadmodule`
- [ ] 完成升級前備份並確認回滾方式
- [ ] 測試環境已演練滾動升級與故障轉移
- [ ] 升級後以 `ACL DRYRUN` 驗證關鍵帳號
- [ ] 全部節點完成前不使用新命令與新型別
- [ ] 安排維護視窗並通知相關團隊

### 13.5 🛡️ 資安檢查

- [ ] 6379／16379 未對外開放
- [ ] 無 `default` 使用者可用的無密碼存取
- [ ] 應用帳號禁止 `@dangerous`、`@admin`、`@scripting`（或僅開放已審核的 `FCALL`）
- [ ] `RESTORE`、`MIGRATE`、`MONITOR`、`CONFIG` 僅限維運帳號
- [ ] 版本為該分支最新安全修補版，並符合修補 SLA
- [ ] TLS 啟用且憑證未過期（納入憑證到期監控）
- [ ] 以非 root 帳號執行 Redis
- [ ] 備份檔已加密並限制存取
- [ ] 日誌與 Key 不含敏感資料

### 13.6 ✅ 上線前 Go-Live 檢查

> 🆕 **v2.0 新增**

- [ ] 壓測達到預估峰值 2 倍且 P99 延遲符合 SLO
- [ ] 故障演練完成：Primary 停機、網路中斷、Redis 全部不可用時應用可降級
- [ ] 監控儀表板與告警已驗證（實際觸發過一次告警）
- [ ] Runbook 已交接給值班團隊
- [ ] 容量規劃文件已核准，並設定擴容觸發門檻
- [ ] 資料分類與保存期限（TTL）已經資料治理或個資窗口確認

---

## 14. Redis 8 Query Engine、向量搜尋與 AI 應用

> 🆕 **v2.0 新增章節**

### 14.1 Redis 8 內建功能概觀

Redis 8 將過去 Redis Stack 的模組全部整合進 Redis Open Source，安裝一個 Redis 即可同時提供快取、文件、搜尋、時序與向量能力。

```mermaid
flowchart TB
    subgraph R8["Redis Open Source 8.x"]
        CORE[核心資料結構<br/>String／Hash／List／Set／ZSet／Stream／Array]
        JSON[JSON 文件]
        QE[Query Engine<br/>全文／數值／標籤／地理／向量索引]
        TS[Time Series]
        PROB[機率型結構<br/>Bloom／Cuckoo／Top-K／CMS／t-digest]
        VS[Vector Set]
    end
    CORE --> QE
    JSON --> QE
    APP[應用程式／AI Agent] --> R8
```

| 能力 | 典型企業用途 | 章節 |
| --- | --- | --- |
| Query Engine | 商品搜尋、後台多條件篩選、即時報表 | [14.2](#142-query-engine二級索引與全文搜尋) |
| 向量索引 + `FT.HYBRID` | RAG 檢索、語意搜尋、推薦 | [14.3](#143-向量搜尋與混合搜尋fthybrid) |
| Vector Set | 輕量級相似度搜尋、少量向量 | [14.4](#144-vector-set) |
| 語意快取 | 降低 LLM 呼叫成本與延遲 | [14.5](#145-語意快取semantic-cache) |
| Agent 記憶 | 對話短期記憶、長期記憶檢索 | [14.6](#146-rag-與-ai-agent-記憶架構) |

### 14.2 Query Engine：二級索引與全文搜尋

Query Engine 會為 Hash 或 JSON 建立**二級索引**，寫入資料時自動同步更新索引，查詢時不需要掃描 key。

```bash
# 1. 以 JSON 文件建立索引：前綴為 product: 的 key 都會被索引
FT.CREATE idx:product ON JSON PREFIX 1 product: SCHEMA
  $.name        AS name     TEXT WEIGHT 2.0
  $.description AS desc     TEXT
  $.brand       AS brand    TAG
  $.category    AS category TAG
  $.price       AS price    NUMERIC SORTABLE
  $.location    AS location GEO

# 2. 寫入資料（索引自動更新）
JSON.SET product:1001 $ '{"name":"輕薄筆電 14 吋","description":"適合商務出差","brand":"acme","category":"laptop","price":35000,"location":"121.56,25.03"}'

# 3. 查詢：全文 + 標籤 + 數值範圍 + 排序 + 分頁
FT.SEARCH idx:product "@name:筆電 @category:{laptop} @price:[20000 40000]"
  SORTBY price ASC LIMIT 0 10 RETURN 2 name price

# 4. 聚合：各分類的商品數與平均價格
FT.AGGREGATE idx:product "*"
  GROUPBY 1 @category
  REDUCE COUNT 0 AS cnt
  REDUCE AVG 1 @price AS avg_price
  SORTBY 2 @cnt DESC

# 5. 索引維運
FT.INFO idx:product
FT._LIST
FT.ALIASADD product idx:product      # 以別名切換索引（重建索引時零停機）
FT.ALIASLIST                         # 列出所有別名（8.10+）
FT.DROPINDEX idx:product             # 只刪索引，不刪資料
```

**欄位型別**：

| 型別 | 用途 | 查詢語法範例 |
| --- | --- | --- |
| `TEXT` | 全文檢索（分詞、詞幹、權重） | `@name:筆電` |
| `TAG` | 精確比對（分類、狀態、ID） | `@category:{laptop\|tablet}` |
| `NUMERIC` | 數值範圍 | `@price:[100 (500]` |
| `GEO`／`GEOSHAPE` | 地理位置與形狀 | `@location:[121.56 25.03 5 km]` |
| `VECTOR` | 向量相似度 | 見 14.3 |

> ⚠️ **中文全文檢索**：Query Engine 內建的中文分詞支援有限，需以 `LANGUAGE chinese` 設定並實測效果；對中文搜尋品質要求高的場景，可在應用端先分詞後以 `TAG` 或空白分隔的 `TEXT` 寫入，或評估專用搜尋引擎（Elasticsearch／OpenSearch）。

**Query Engine 設計要點**：

| 要點 | 說明 |
| --- | --- |
| 索引記憶體 | 索引本身占用記憶體，需納入容量規劃（`FT.INFO` 查看） |
| Cluster | 查詢由協調者分送到所有 shard 再合併；大量 shard 時延遲增加 |
| 逾時策略 | `search-on-timeout`（8.10 支援 `FAIL`、`RETURN`、`RETURN_STRICT`）決定逾時時回傳部分結果或失敗 |
| 重建索引 | 使用別名：建立新索引 → 背景索引完成 → `FT.ALIASUPDATE` 切換 |
| 權限 | 8.0 起 `FT.*` 命令納入既有 ACL 類別，需確認應用帳號權限 |

### 14.3 向量搜尋與混合搜尋（FT.HYBRID）

**建立向量索引**：

```bash
FT.CREATE idx:doc ON HASH PREFIX 1 doc: SCHEMA
  title      TEXT
  content    TEXT
  dept       TAG
  updated_at NUMERIC SORTABLE
  embedding  VECTOR HNSW 6 TYPE FLOAT32 DIM 1024 DISTANCE_METRIC COSINE
```

| 向量索引演算法 | 特性 | 適用 |
| --- | --- | --- |
| `FLAT` | 暴力搜尋，100% 準確 | 向量數 < 10 萬 |
| `HNSW` | 近似最近鄰，速度快、記憶體較高 | 通用首選 |
| `SVS-VAMANA`（8.2+） | 圖索引＋向量壓縮，記憶體效率高 | 大量向量、記憶體成本敏感 |

**純向量 KNN 查詢**：

```bash
# 找出與查詢向量最相近的 5 筆，且限定部門
FT.SEARCH idx:doc "(@dept:{legal})=>[KNN 5 @embedding $vec AS score]"
  PARAMS 2 vec <float32-binary-blob>
  SORTBY score RETURN 3 title dept score
  DIALECT 2
```

**混合搜尋（8.4+）**：`FT.HYBRID` 在單一命令中同時執行全文檢索與向量相似度，並以 RRF（Reciprocal Rank Fusion）或線性加權融合排序，是 RAG 檢索的推薦做法。

```bash
FT.HYBRID idx:doc
  SEARCH "@content:(請假 規定)"
  VSIM @embedding $vec
    KNN 2 K 20
    FILTER "@dept:{hr}"
  COMBINE RRF 4 WINDOW 40 CONSTANT 60
  LOAD 3 @title @content @updated_at
  LIMIT 0 5
  PARAMS 2 vec <float32-binary-blob>
```

| 參數 | 說明 |
| --- | --- |
| `SEARCH` | 文字查詢，語法同 `FT.SEARCH`；預設計分器 BM25STD |
| `VSIM ... KNN 2 K 20` | 向量 KNN，取 20 個候選（`2` 為後續參數個數） |
| `FILTER` | 向量搜尋的前置過濾 |
| `COMBINE RRF` | 以排名融合兩路結果；`WINDOW` 預設 20、`CONSTANT` 預設 60 |
| `COMBINE LINEAR ... ALPHA a BETA b` | 以加權分數融合 |
| `LOAD` | 回傳欄位（預設只回傳 key 與分數） |

> 💡 向量需以 client 轉為 little-endian 的 FLOAT32 二進位（例如 Python `np.array(v, dtype=np.float32).tobytes()`）。Python 專案可直接使用官方 **RedisVL** 函式庫處理索引定義、向量編碼與查詢組裝。

### 14.4 Vector Set

Vector Set 是 Redis 8.0 新增的原生資料型別（由 Redis 原作者 antirez 設計），概念類似 Sorted Set：每個元素對應一個向量而非分數，支援相似度查詢與屬性過濾。它**不需要建立索引**，適合輕量、少量或每個使用者／租戶一組向量的場景。

```bash
# 新增元素（VALUES 形式可避免位元組序問題）
VADD movies VALUES 3 0.12 0.88 0.35 "movie:1001"
VADD movies VALUES 3 0.10 0.80 0.40 "movie:1002" SETATTR '{"year":1999,"genre":"scifi"}'

# 以量化降低記憶體：Q8（預設）、BIN（二元）、NOQUANT（不量化）
VADD movies:bin VALUES 3 0.2 0.1 0.9 "movie:2001" BIN

# 相似度查詢
VSIM movies ELE "movie:1001" WITHSCORES COUNT 5              # 與某元素相似
VSIM movies VALUES 3 0.1 0.9 0.3 COUNT 5                     # 與某向量相似
VSIM movies VALUES 3 0.1 0.9 0.3 COUNT 5 FILTER '.year > 1990 and .genre == "scifi"'

# 其他
VCARD movies          # 元素數
VDIM movies           # 維度
VEMB movies movie:1001
VGETATTR movies movie:1002
VREM movies movie:1001
VRANGE movies - + 10  # 依字典序列出元素（8.4+）
```

| 比較 | Vector Set | Query Engine 向量索引 |
| --- | --- | --- |
| 需要建立索引 | 否 | 是（`FT.CREATE`） |
| 與全文／數值條件結合 | 簡單屬性過濾 | 完整查詢語言＋`FT.HYBRID` |
| 資料模型 | 一個 key 一組向量 | 跨大量 Hash／JSON 文件 |
| Cluster 分散 | 單一 key 位於單一 shard | 跨 shard 查詢 |
| 適用 | 每使用者／每租戶的小型向量集合、推薦 | 企業知識庫、大規模 RAG |

### 14.5 語意快取（Semantic Cache）

傳統快取以「完全相同的 key」命中；語意快取以**問題的語意相似度**命中，當使用者以不同措辭問相同問題時，直接回傳先前的 LLM 回答。

```mermaid
sequenceDiagram
    participant U as 使用者
    participant App as 應用程式
    participant E as Embedding 模型
    participant R as Redis 向量索引
    participant L as LLM
    U->>App: 「公司特休怎麼算？」
    App->>E: 產生問題向量
    E-->>App: vector
    App->>R: KNN 查詢（距離門檻 0.1）
    alt 命中
        R-->>App: 既有回答
    else 未命中
        App->>L: 呼叫 LLM
        L-->>App: 回答
        App->>R: 儲存（問題向量＋回答＋TTL）
    end
    App-->>U: 回答
```

```python
# RedisVL（Python）語意快取範例；匯入路徑依 RedisVL 版本可能不同
from redisvl.extensions.cache.llm import SemanticCache

cache = SemanticCache(
    name="llmcache:hr",
    redis_url="rediss://app_ai:***@redis.internal:6379",
    distance_threshold=0.1,     # 越小越嚴格
    ttl=86400,
)

if hits := cache.check(prompt=question):
    answer = hits[0]["response"]
else:
    answer = call_llm(question)
    cache.store(prompt=question, response=answer)
```

**語意快取治理要點**：

| 風險 | 對策 |
| --- | --- |
| 回答含個人或權限相關資訊被他人命中 | 以使用者／角色／租戶作為過濾條件或分區；個人化回答不快取 |
| 門檻過寬造成錯誤命中 | 以真實問題集調校 `distance_threshold` 並監控誤命中率 |
| 知識更新後回答過時 | 設定 TTL；知識庫更新時依標籤清除相關快取 |
| 提示注入內容被快取 | 只快取通過內容安全檢查的回答 |

> 💡 Redis Cloud 另提供託管的語意快取服務（LangCache），不想自行維運向量索引時可評估。

### 14.6 RAG 與 AI Agent 記憶架構

```mermaid
flowchart LR
    subgraph Ingest["資料匯入"]
        DOC[文件／知識庫] --> CH[切塊 Chunking]
        CH --> EMB[Embedding]
        EMB --> IDX[(Redis<br/>JSON + 向量索引)]
    end
    subgraph Query["查詢"]
        Q[使用者問題] --> SC{語意快取}
        SC -->|命中| ANS[回答]
        SC -->|未命中| HY[FT.HYBRID<br/>全文 + 向量 + 權限過濾]
        HY --> IDX
        HY --> LLM[LLM 產生回答]
        LLM --> ANS
    end
    subgraph Memory["Agent 記憶"]
        STM[短期記憶<br/>Hash／JSON + TTL]
        LTM[長期記憶<br/>向量索引]
    end
    LLM <--> STM
    LLM <--> LTM
```

| 元件 | Redis 實作 | 說明 |
| --- | --- | --- |
| 文件切塊儲存 | JSON（內容、來源、權限標籤、向量） | 以 `doc:{id}:chunk:{n}` 命名 |
| 檢索 | `FT.HYBRID` + `FILTER` 權限標籤 | 同時利用關鍵字與語意，並落實資料權限 |
| 對話短期記憶 | Hash／JSON／Stream + TTL | 保存最近 N 輪對話，會話結束後過期 |
| 長期記憶 | 向量索引 | 將重要事實摘要後向量化，跨會話召回 |
| 語意快取 | 向量索引 | 降低重複問題的 LLM 成本 |
| 工具呼叫結果快取 | String／JSON + TTL | 避免 Agent 重複呼叫外部 API |
| 限流與配額 | `INCREX` | 控制每位使用者的 LLM 呼叫次數 |

**AI 應用的資安重點**：

- 檢索時一定要以使用者權限過濾（例如 `@acl_groups:{hr|all}`），避免 RAG 洩漏未授權文件。
- 向量與原文同樣屬於敏感資料，需套用相同的加密、保存期限與刪除流程。
- Agent 使用的 Redis 帳號遵循最小權限，禁止 `@dangerous`、`@scripting`。

### 14.7 💡 本章實務建議

- 已有 Redis 8 的團隊，中小規模的搜尋與 RAG 需求可先以 Query Engine 實作，減少額外元件。
- 搜尋品質（特別是中文）與向量召回率需要以實際資料評估，建立離線評測集後再上線。
- 向量索引記憶體占用大，導入前依「向量數 × 維度 × 4 bytes × 索引倍數」估算並壓測。
- 語意快取與 Agent 記憶必須設計權限隔離與 TTL，並納入個資盤點。

---

## 15. 雲端託管與替代方案選型

> 🆕 **v2.0 新增章節**

### 15.1 部署模式總覽

| 模式 | 維運責任 | 優點 | 缺點 |
| --- | --- | --- | --- |
| 自建（VM／實體機） | 全部自行負責 | 成本透明、完全掌控版本與設定 | 需具備 HA、備份、修補、監控能力 |
| 自建（Kubernetes + Operator） | 平台團隊負責 | 與既有平台整合、自動化程度高 | Operator 與儲存需成熟維運 |
| 雲端託管（CSP 服務） | 雲端業者負責基礎設施 | 自動故障轉移、備份、修補 | 版本與功能受限於業者；多為 Valkey 或特定 Redis 版本 |
| Redis Cloud／Redis Software | Redis 公司或自行（Software） | 完整 Redis 8 功能、Active-Active、官方支援 | 授權與訂閱成本 |

### 15.2 主要託管服務比較

> 下表為 2026-09 的彙整，各服務支援版本與功能變動頻繁，採購前請以業者官方文件確認。

| 服務 | 引擎 | 重點特性 | 企業注意事項 |
| --- | --- | --- | --- |
| **Redis Cloud** | Redis 8.x | 完整 Redis 8 功能（搜尋、向量、JSON）、Active-Active、多雲 | 功能最完整；費用依規格與區域 |
| **Amazon ElastiCache** | Valkey（含 9.0、9.1）、Redis OSS（舊版） | Serverless 與節點式、多 AZ、全球資料存放區 | 主推 Valkey；Redis 8 專有功能（Vector Set、Array、新命令）不適用 |
| **Amazon MemoryDB** | Valkey／Redis OSS 相容 | 以多 AZ 交易日誌提供持久性，可作主要資料庫 | 寫入延遲高於 ElastiCache |
| **Azure Managed Redis** | Redis（以 Redis Enterprise 為基礎） | Redis 8 功能、Active geo-replication | Azure Cache for Redis（Basic／Standard／Premium）將於 **2028-09-30** 退役，**2026-10-01** 起既有客戶無法新建；Enterprise 層級於 2027-03-31 退役，需規劃遷移 |
| **Google Memorystore** | Memorystore for Valkey（7.2、8.0、9.0、9.1）、Memorystore for Redis Cluster、Memorystore for Redis | 全託管、Cluster 模式 | 新專案主推 Memorystore for Valkey |

**託管服務評估項目**：

| 類別 | 檢查項目 |
| --- | --- |
| 相容性 | 支援的引擎與版本、是否支援所需命令與資料型別（JSON、搜尋、向量、Stream 新命令） |
| 可用性 | SLA、多 AZ、故障轉移時間、維護視窗 |
| 資料保護 | 備份頻率與保留、跨區複寫、加密（傳輸與靜態）、客戶自管金鑰 |
| 網路 | 私有端點、VPC 對等、是否可完全關閉公網 |
| 身分 | ACL、IAM 整合、憑證輪替 |
| 維運 | 監控指標、慢查詢存取、版本升級方式與通知期 |
| 成本 | 計價模式（節點、Serverless、資料傳輸）、保留執行個體折扣 |
| 法遵 | 資料所在地、稽核報告（SOC 2、ISO 27001） |

### 15.3 Valkey 與相容替代方案

**Valkey**：2024 年 Redis 改變授權後，由 Linux Foundation 主導、自 Redis 7.2.4 分叉的開源專案，維持 BSD-3-Clause 授權。

| 項目 | Valkey 9.x（2026-09 最新 9.1.2） | Redis Open Source 8.10 |
| --- | --- | --- |
| 授權 | BSD-3-Clause | RSALv2／SSPLv1／AGPLv3 |
| 治理 | Linux Foundation 社群 | Redis 公司 |
| 核心命令 | 與 Redis 7.2 相容，之後各自演進 | — |
| Hash 欄位 TTL | 有（9.0） | 有（7.4） |
| 原子 slot 遷移 | 有（9.0） | 有（8.4） |
| Cluster 多資料庫 | 有（9.0） | 無（僅 db 0） |
| JSON／搜尋／Bloom | 以獨立模組提供（valkey-json、valkey-search、valkey-bloom） | 內建 |
| Vector Set、Array、`INCREX`、`XNACK` 等 8.x 新功能 | 無 | 有 |
| 雲端支援 | AWS、GCP 主推 | Redis Cloud、Azure Managed Redis |

**其他相容方案**：

| 方案 | 特性 | 注意 |
| --- | --- | --- |
| Dragonfly | 多執行緒架構、單機高吞吐、Redis／Memcached 協定相容 | 授權為 BSL；部分命令與 Cluster 行為不同 |
| KeyDB | 多執行緒 Redis 分支 | 社群活躍度需評估 |
| Garnet（Microsoft） | 以 .NET 實作、RESP 相容 | 功能覆蓋度需驗證 |

> ⚠️ **相容性陷阱**：Redis 7.4 以後與 Valkey 各自演進，**RDB 檔案格式與新命令不保證互通**。跨產品遷移應以邏輯遷移工具或以相容版本作為中繼，並完整回歸測試。

### 15.4 選型決策流程

```mermaid
flowchart TD
    A[開始] --> B{需要 Redis 8 專有功能?<br/>Vector Set、Array、內建搜尋/JSON、新命令}
    B -->|是| C{希望自行維運?}
    C -->|是| D[Redis Open Source 8.x<br/>或 Redis Software]
    C -->|否| E[Redis Cloud<br/>或 Azure Managed Redis]
    B -->|否| F{授權政策禁止<br/>AGPL／SSPL／RSAL?}
    F -->|是| G{希望自行維運?}
    G -->|是| H[Valkey 自建]
    G -->|否| I[ElastiCache／Memorystore for Valkey]
    F -->|否| J{具備 Redis 維運能力?}
    J -->|是| D
    J -->|否| K[依雲端平台選擇託管服務]
```

### 15.5 遷移注意事項

| 遷移路徑 | 建議方法 | 注意 |
| --- | --- | --- |
| 自建 Redis → 同引擎託管 | 業者提供的線上遷移工具、以 Replica 同步後切換 | 確認 ACL、TLS、參數差異 |
| Redis → Valkey | 以 Redis 7.2 相容格式或邏輯遷移（例如 RIOT 等工具）；應用端雙寫過渡 | 不可使用 8.x 專有命令與型別 |
| Valkey／舊版 → Redis 8 | 新版可讀取舊版 RDB；以 Replica 同步或 RDB 匯入 | 升級 client、檢查 ACL 類別變化 |
| Azure Cache for Redis → Azure Managed Redis | 依 Microsoft 遷移指南 | 注意 2026-10-01 起的新建限制與 2028-09-30 退役日 |
| 純快取 | 最簡單：切換連線後由應用回填 | 預熱熱點資料，避免冷啟動擊穿 DB |

**遷移步驟通則**：

1. 盤點：版本、資料量、使用的命令與資料型別（`INFO commandstats`）、ACL、client 版本。
2. 相容性測試：在目標環境執行完整回歸與壓測。
3. 資料同步：選擇離線（RDB）或線上（複寫、雙寫、工具）方式。
4. 切換：以設定中心或 DNS 切換連線，保留回切能力。
5. 觀察：比對命中率、延遲、錯誤率至少一個完整業務週期。

### 15.6 💡 本章實務建議

- 選型先確認「是否需要 Redis 8 專有功能」與「組織授權政策」，這兩點通常直接決定方向。
- 使用 Azure Cache for Redis 的團隊，應立即依退役時程規劃遷移至 Azure Managed Redis。
- 應用程式只使用「目標平台都支援」的命令子集，可大幅降低未來更換引擎的成本。
- 任何引擎遷移都需完整回歸測試，不要假設「Redis 相容」代表行為完全一致。

---

## 附錄 A：常用指令速查表

### A.1 連線與認證

```bash
redis-cli -h host -p 6379 --user app_user --askpass       # 互動輸入密碼
REDISCLI_AUTH=*** redis-cli -h host --user app_user       # 以環境變數提供密碼
redis-cli -u rediss://user@host:6380/0 --cacert ca.crt    # TLS
redis-cli -c -h host                                      # Cluster 模式
AUTH username password
HELLO 3 AUTH username password                            # 切換 RESP3 並認證
CLIENT SETNAME order-service
```

### A.2 資料操作

```bash
# String
SET key value [NX|XX|IFEQ v|IFNE v] [GET] [EX s|PX ms|EXAT t|KEEPTTL]
GET key | GETEX key EX s | GETDEL key
MGET k1 k2 | MSET k1 v1 k2 v2 | MSETEX 2 k1 v1 k2 v2 EX 300
DELEX key IFEQ value                  # 8.4+
INCR key | INCRBY key n | INCREX key BYINT 1 UBOUND 100 EX 60 ENX   # 8.8+

# Hash
HSET key f1 v1 f2 v2 | HGET key f | HMGET key f1 f2 | HGETALL key | HDEL key f
HEXPIRE key 60 FIELDS 1 f | HTTL key FIELDS 1 f       # 7.4+
HSETEX key EX 60 FIELDS 1 f v | HGETEX key EX 60 FIELDS 1 f | HGETDEL key FIELDS 1 f   # 8.0+

# List
LPUSH/RPUSH key v | LPOP/RPOP key [count] | BLPOP key timeout
LRANGE key 0 -1 | LTRIM key 0 99
LMOVE src dst LEFT RIGHT | LMOVEM src dst LEFT RIGHT COUNT 10 BULK   # 8.10+

# Set
SADD key m | SREM key m | SISMEMBER key m | SCARD key | SSCAN key 0
SINTER k1 k2 | SINTERCARD 2 k1 k2 | SUNIONCARD 2 k1 k2 | SDIFFCARD 2 k1 k2   # 後兩者 8.10+

# Sorted Set
ZADD key score m | ZINCRBY key n m | ZSCORE key m | ZRANK key m
ZRANGE key 0 9 REV WITHSCORES | ZRANGE key min max BYSCORE LIMIT 0 10
ZPOPMIN key n | ZREM key m

# Stream
XADD key [IDMP pid iid] [MAXLEN ~ n] * f v
XGROUP CREATE key grp $ MKSTREAM
XREADGROUP GROUP grp c COUNT 10 BLOCK 5000 [CLAIM ms] STREAMS key >
XACK key grp id | XACKDEL key grp ACKED IDS 1 id | XNACK key grp FAIL IDS 1 id
XPENDING key grp | XINFO GROUPS key | XTRIM key MAXLEN ~ n ACKED

# 其他
UNLINK key | EXPIRE key s | TTL key | PERSIST key | TYPE key | OBJECT ENCODING key
```

### A.3 管理命令

```bash
INFO [section] | INFO everything | INFO keysizes
DBSIZE
SCAN cursor [MATCH pattern] [COUNT n] [TYPE type]     # 取代 KEYS
MEMORY USAGE key | MEMORY STATS | MEMORY DOCTOR
SLOWLOG GET [n] | SLOWLOG RESET
LATENCY LATEST | LATENCY DOCTOR
CLIENT LIST | CLIENT KILL ID id | CLIENT NO-EVICT on
CONFIG GET param | CONFIG SET param value | CONFIG REWRITE
BGSAVE | LASTSAVE | BGREWRITEAOF
BACKUP START | BACKUP LIST | BACKUP SEAL | BACKUP CLEANUP | BACKUP STATUS   # 8.10+
HOTKEYS START METRICS 2 CPU NET COUNT 10 DURATION 60 | HOTKEYS GET        # 8.6+
ACL LIST | ACL GETUSER u | ACL DRYRUN u cmd args | ACL LOG | ACL LOAD | ACL SAVE
FUNCTION LIST | FUNCTION LOAD [REPLACE] code | FCALL fn numkeys key...
```

### A.4 Cluster 命令

```bash
CLUSTER INFO
CLUSTER NODES
CLUSTER SHARDS                       # 7.0+，取代 CLUSTER SLOTS
CLUSTER KEYSLOT key
CLUSTER FAILOVER                     # 在 Replica 上執行
CLUSTER SLOT-STATS SLOTSRANGE 0 100  # 8.2+
redis-cli --cluster create h1:6379 h2:6379 h3:6379 h4:6379 h5:6379 h6:6379 --cluster-replicas 1
redis-cli --cluster check h1:6379
redis-cli --cluster reshard h1:6379  # 8.10+ 使用原子 slot 遷移
redis-cli --cluster rebalance h1:6379
```

### A.5 Sentinel 命令

```bash
SENTINEL masters
SENTINEL master mymaster
SENTINEL replicas mymaster           # 取代舊的 SENTINEL slaves
SENTINEL sentinels mymaster
SENTINEL get-master-addr-by-name mymaster
SENTINEL failover mymaster
SENTINEL ckquorum mymaster
SENTINEL reset mymaster
```

### A.6 JSON／搜尋／向量命令

```bash
JSON.SET key $ '{...}' | JSON.GET key $.path | JSON.NUMINCRBY key $.n 1 | JSON.DEL key $.path
FT.CREATE idx ON JSON PREFIX 1 p: SCHEMA $.f AS f TEXT ...
FT.SEARCH idx "@f:word" LIMIT 0 10 | FT.AGGREGATE idx "*" GROUPBY 1 @c REDUCE COUNT 0 AS n
FT.HYBRID idx SEARCH "q" VSIM @vec $v KNN 2 K 10 PARAMS 2 v <blob>     # 8.4+
FT.INFO idx | FT.ALIASADD a idx | FT.DROPINDEX idx
VADD key VALUES 3 0.1 0.2 0.3 elem | VSIM key ELE elem COUNT 5 WITHSCORES   # 8.0+
BF.RESERVE key 0.001 1000000 | BF.ADD key item | BF.EXISTS key item
TS.CREATE key RETENTION ms LABELS k v | TS.ADD key * value | TS.RANGE key - + AGGREGATION avg 60000
```

---

## 附錄 B：版本新功能對照表

| 類別 | 功能 | 版本 |
| --- | --- | --- |
| **String** | `GETDEL`、`GETEX`、`SET ... EXAT/PXAT/GET` | 6.2 |
| | `SET IFEQ/IFNE/IFDEQ/IFDNE`、`DELEX`、`DIGEST`、`MSETEX` | 8.4 |
| | `INCREX`（上下限＋TTL 遞增） | 8.8 |
| **Hash** | 欄位 TTL：`HEXPIRE`、`HPEXPIRE`、`HTTL`、`HPERSIST` 等 | 7.4 |
| | `HGETEX`、`HSETEX`、`HGETDEL` | 8.0 |
| | Hash 欄位層級鍵空間通知 | 8.8 |
| | Compact hashes、`HIMPORT` | 8.10 |
| **List** | `LMOVE`、`BLMOVE` | 6.2 |
| | `LMPOP`、`BLMPOP` | 7.0 |
| | `LMOVEM`、`BLMOVEM` | 8.10 |
| **Set** | `SMISMEMBER` | 6.2 |
| | `SINTERCARD` | 7.0 |
| | `SUNIONCARD`、`SDIFFCARD` | 8.10 |
| **Sorted Set** | `ZRANGE` 統一語法（`BYSCORE`、`REV`、`LIMIT`）、`ZRANGESTORE` | 6.2 |
| | `ZRANK ... WITHSCORE` | 7.2 |
| | `ZUNION`／`ZINTER` 系列 `COUNT` 聚合 | 8.8 |
| **Bitmap** | `BITOP DIFF/DIFF1/ANDOR/ONE` | 8.2 |
| **Stream** | 消費者群組 | 5.0 |
| | `XDELEX`、`XACKDEL`、`KEEPREF/DELREF/ACKED` 修剪策略 | 8.2 |
| | `XREADGROUP ... CLAIM` | 8.4 |
| | `XADD IDMP/IDMPAUTO`（冪等寫入）、`XCFGSET` | 8.6 |
| | `XNACK` | 8.8 |
| | `XREAD`／`XREADGROUP` 的 `MAXCOUNT`、`MAXSIZE` | 8.10 |
| **新型別** | JSON、Time Series、機率型結構、Query Engine 內建 | 8.0 |
| | Vector Set | 8.0 |
| | Array | 8.8 |
| **搜尋／向量** | SVS-VAMANA 向量索引 | 8.2 |
| | `FT.HYBRID`、預設計分器 BM25STD、搜尋 I/O threads | 8.4 |
| | `FT.ALIASLIST`、JSONPath 擴充、`search-on-timeout RETURN_STRICT` | 8.10 |
| **Cluster** | Sharded Pub/Sub、`CLUSTER SHARDS` | 7.0 |
| | `CLUSTER SLOT-STATS` | 8.2 |
| | `CLUSTER MIGRATION`（原子 slot 遷移） | 8.4 |
| | `redis-cli --cluster reshard/rebalance` 使用原子遷移 | 8.10 |
| **維運** | Multi-part AOF、Functions、ACL selectors | 7.0 |
| | `aof-load-corrupt-tail-max-size`、`lookahead` | 8.4 |
| | `HOTKEYS`、`key-memory-histograms`、`*-lrm` 淘汰策略 | 8.6 |
| | `slowlog-entry-max-argc`、`slowlog-entry-max-string-len` | 8.8 |
| | `BACKUP` 命令族、`preload-file`、`redis-cli --latency-percentiles` | 8.10 |
| **安全** | ACL、TLS | 6.0 |
| | TLS 憑證自動認證（`tls-auth-clients-user`） | 8.6 |
| | 節點間 TLS 憑證認證 | 8.10 |

---

## 附錄 C：版本更新紀錄

### C.1 版本歷史

| 版本 | 日期 | 說明 |
| --- | --- | --- |
| 1.0 | 2026-01-27 | 初版，以 Redis 7.2 為基準，13 章＋附錄 |
| 2.0 | 2026-09-29 | 以 Redis 8.10.2 為基準全面改版：逐章查證更新、修正 v1.0 錯誤、新增第 14～15 章與附錄 B～E、修正目錄連結與 Markdown 格式 |

### C.2 v1.0 → v2.0 更正清單

| # | 章節 | v1.0 內容 | v2.0 更正 |
| --- | --- | --- | --- |
| 1 | 標頭 | 「最後更新」重複兩次、適用 Redis 7.x、行尾空白換行 | 改為文件資訊表格；適用 Redis 8.10.x |
| 2 | 2 | 以 master／slave 稱呼 | 敘述改用 primary／replica（命令與欄位名稱不變） |
| 3 | 2.6 | 跨機房部署建議「Cluster + 異地複寫」 | Open Source 無內建跨叢集複寫；雙活需 Redis Software／Cloud Active-Active |
| 4 | 3.1 | 建議版本 Redis 7.2.x | 建議 Redis 8.10.x；列出各分支最新修補版 |
| 5 | 3.1 | 下載 `redis-stable` 未鎖定版本 | 指定版本並驗證雜湊；增加 RPM 安裝方式 |
| 6 | 3.2 | Compose 使用 `version: '3.8'` | Compose v2 已不需要，移除 |
| 7 | 3.2 | `-p 6379:6379` 綁定所有介面 | 改為 `127.0.0.1:6379:6379` |
| 8 | 3.2 | Sentinel 範例只有 1 個 Sentinel（無法達 quorum 2） | 3 個 Sentinel，且各自擁有可寫設定檔 |
| 9 | 3.3 | AOF 為單一 `appendonly.aof` 檔 | 7.0+ 為 `appendonlydir/`（BASE、INCR、manifest） |
| 10 | 3.4 | `redis-cli -a password` | 改用 `REDISCLI_AUTH` 或 `--askpass` |
| 11 | 3.5 | 使用 `netstat` | 改用 `ss` |
| 12 | 3.5 | `--test-memory` 用於「檢查設定檔語法」 | `--test-memory` 為記憶體測試；改以前景模式啟動驗證 |
| 13 | 4.1 | `daemonize yes` | systemd 管理時使用 `daemonize no` + `supervised systemd` |
| 14 | 4.2 | 淘汰策略缺少 8.6 新增項目 | 新增 `allkeys-lrm`、`volatile-lrm` |
| 15 | 4.3 | `save 900 1 / 300 10 / 60 10000` | 7.0+ 預設 `3600 1 300 100 60 10000` |
| 16 | 4.5 | `cluster-replica-validity-factor` 解釋錯誤 | 更正為「Replica 資料新舊判斷」；另說明 `cluster-migration-barrier` |
| 17 | 4.6、10.4、10.5 | 以 `rename-command` 停用危險命令 | 官方標示不建議使用；改以 ACL 管控 |
| 18 | 5.1 | 列出 `SETNX`、`SETEX` 為一般用法 | 建議統一使用 `SET` 選項 |
| 19 | 5.2、附錄 | 使用 `HMSET` | `HSET` 已支援多欄位，移除 `HMSET` |
| 20 | 5.4 | 抽獎使用 `SRANDMEMBER` | 會重複中獎；改用 `SPOP` |
| 21 | 5.5 | 使用 `ZREVRANGE`、`ZRANGEBYSCORE` | 改用 6.2+ 統一的 `ZRANGE` 語法 |
| 22 | 6.3 | `spring.redis.*`、`spring.session.store-type` | Spring Boot 3+ 為 `spring.data.redis.*`；`store-type` 已移除 |
| 23 | 6.4 | 滑動視窗以多個獨立命令實作 | 非原子，改為單一 Lua；8.8+ 可用 `INCREX` |
| 24 | 7.2 | Node.js 推薦 ioredis | 官方推薦 node-redis |
| 25 | 7.3 | `spring.redis.*` 屬性 | 改為 `spring.data.redis.*` |
| 26 | 7.3 | `activateDefaultTyping(LaissezFaireSubTypeValidator)` | 反序列化攻擊風險；改用有型別序列化器與 Jackson 3 序列化器 |
| 27 | 7.3 | 更新時使用 `@CachePut`；使用 `allEntries = true` | 改用 `@CacheEvict`；說明 `allEntries` 預設以 `KEYS` 清除的風險 |
| 28 | 7.4 | ioredis 範例重複宣告 `const redis`、使用無效選項 | 改為 node-redis 可執行範例 |
| 29 | 7.6 | 宣告 `LettuceClientConfiguration` Bean | 不會被 Spring Boot 採用；改用 Customizer |
| 30 | 7.6 | 使用 Vavr `Try` 與手寫重試迴圈 | 改用 Resilience4j 原生 API 與熔斷設定 |
| 31 | 8.1 | 以 `master_last_io_seconds_ago` 代表複寫延遲 | 改以 offset 差值衡量 |
| 32 | 8.5 | 以 `MEMORY PURGE` 處理碎片 | 改以 `activedefrag` 為主 |
| 33 | 9.2 | Cluster 升級「對每個 Replica 先 `CLUSTER FAILOVER`」 | 順序更正：先升級 Replica，再在其上 failover |
| 34 | 9.3 | 降級套件後直接以原資料啟動 | 新版資料無法被舊版讀取；改以升級前備份回滾 |
| 35 | 10.1 | CVE-2015-4335 描述為未授權存取寫入 SSH 金鑰 | 更正為 Lua 位元組碼執行漏洞 |
| 36 | 10.4 | 備份排程 `BGSAVE && cp` | `BGSAVE` 為非同步；改為等待 `LASTSAVE` 或直接複製（見 8.9） |
| 37 | 10.5 | 同時開放 `port 6379` 與 `tls-port 6380` | 明文埠仍開放；改為 `port 0` |
| 38 | 11.2 | Hot Key 使用 Guava Cache；分片範例未處理寫入 | 改用 Caffeine；補上寫入需更新所有分片 |
| 39 | 11.4 | 交易方法內刪除快取 | 改為交易提交後（AFTER_COMMIT）刪除 |
| 40 | 12.1 | `redis-check-aof --fix appendonly.aof` | 7.0+ 需指定 manifest 檔，並先備份 |
| 41 | 12.2 | 將「刪除所有 cache:* key」標示為清理過期 key | 過期 key 自動回收；改為 `UNLINK` 分批並確認範圍 |
| 42 | 12.5 | 設定 `rename-command KEYS ""` | 改以 ACL 移除 `KEYS` |
| 43 | 13 | 資安檢查錨點含 U+FE0F，目錄連結失效；檢查清單建議 7.x | 子標題加上編號並重建目錄；更新為 8.x |
| 44 | 參考資源 | 連結為舊版網址（`/documentation`、`/docs/manual/patterns/`） | 更新為 `redis.io/docs/latest/` 下的現行網址 |
| 45 | 全文 | 4 處程式碼區塊未標語言、多處清單與程式碼區塊前缺空行 | 全部補上語言標籤與空行 |

### C.3 v2.0 新增章節

| 章節 | 內容 |
| --- | --- |
| 執行摘要 | 五項關鍵結論、角色閱讀路徑 |
| 1.6、1.7 | 產品線、授權與生態系；版本演進 |
| 2.7 | 多可用區、Kubernetes 部署拓撲 |
| 3.6、3.7 | 作業系統調校；Redis Insight |
| 4.7、4.8 | 效能相關設定；生產環境設定範本 |
| 5.7～5.11 | Array、JSON、機率型結構、Time Series、資料結構選型表 |
| 6.7～6.9 | 快取穿透／擊穿／雪崩；Client-side caching；交易、Lua 與 Functions |
| 7.7、7.8 | Go 與 .NET 範例；RESP3 相容性 |
| 8.6～8.9 | Hot Key 偵測；延遲診斷；Prometheus + Grafana；備份與還原（含 `BACKUP`） |
| 9.5、9.6 | 7.x → 8.x 升級注意事項；支援週期與版本策略 |
| 10.6、10.7 | CVE 應變與修補管理；合規與稽核對應 |
| 11.6、11.7 | 容量規劃與成本；SLO 範例 |
| 12.5～12.7 | 案例 4；Cluster 常見錯誤；升級後常見問題 |
| 13.6 | 上線前 Go-Live 檢查 |
| 14 | Redis 8 Query Engine、向量搜尋與 AI 應用 |
| 15 | 雲端託管與替代方案選型 |
| 附錄 B、C、D、E | 版本對照、更新紀錄、查證紀錄、參考資料 |
| 各章 | 章末「💡 本章實務建議」 |

---

## 附錄 D：查證紀錄

所有項目查證日期均為 **2026-09-29**。

| # | 查證事實 | 本文位置 | 來源 |
| --- | --- | --- | --- |
| 1 | Redis Open Source 最新版為 8.10.2（2026-09-17），8.8.3／8.6.7／8.4.7／8.2.10 同日發布 | 標頭、3.1、9.6 | GitHub redis/redis Releases |
| 2 | 8.0（2025-05）～8.10（2026-07）各 minor 版本 GA 時間 | 1.7、9.6 | Redis Open Source release notes 索引頁 |
| 3 | 8.10 新增 Compact hashes、`HIMPORT`、`LMOVEM`、`SUNIONCARD`、`SDIFFCARD`、`BACKUP`、`MAXCOUNT`／`MAXSIZE`、節點間 TLS 憑證認證 | 1.7、5、8.9、附錄 B | Redis 8.10 release notes |
| 4 | 8.8 新增 Array、`INCREX`、`XNACK`、Hash 子鍵通知、`slowlog-entry-max-*` | 5、6、附錄 B | Redis 8.8 release notes |
| 5 | 8.6 新增 `XADD IDMP`、`HOTKEYS`、`*-lrm`、`tls-auth-clients-user`、`cluster-slot-stats-enabled` | 4、5、8、10 | Redis 8.6 release notes |
| 6 | 8.4 新增 `SET IF*`、`DELEX`、`DIGEST`、`MSETEX`、`XREADGROUP CLAIM`、`CLUSTER MIGRATION`、`FT.HYBRID`、`lookahead` | 2、5、6、14 | Redis 8.4 release notes |
| 7 | 8.2 新增 `XDELEX`、`XACKDEL`、`BITOP` 新運算子、`CLUSTER SLOT-STATS`、SVS-VAMANA | 5、8、14 | Redis 8.2 release notes |
| 8 | `SET` 完整語法與 `IFEQ` 等條件；`SETNX`／`SETEX` 可能於未來棄用 | 5.1 | redis.io 命令文件：SET |
| 9 | `DELEX`、`MSETEX`、`INCREX`、`HSETEX`、`HGETEX` 語法與版本 | 5、6 | redis.io 命令文件 |
| 10 | `XADD` IDMP 語法與 `XCFGSET IDMP-DURATION／IDMP-MAXSIZE` | 5.6、6.6 | redis.io 命令文件：XADD |
| 11 | `XREADGROUP` 的 `CLAIM`（8.4）、`MAXCOUNT`／`MAXSIZE`（8.10） | 5.6、6.6 | redis.io 命令文件：XREADGROUP |
| 12 | `XNACK` 語法與 `SILENT`／`FAIL`／`FATAL` 模式 | 5.6、6.6 | redis.io 命令文件：XNACK |
| 13 | `HOTKEYS START` 語法與 CPU／NET 指標 | 8.6 | redis.io 命令文件：HOTKEYS、HOTKEYS START |
| 14 | Array 命令（`ARSET`、`ARGET`、`ARRING` 等）與 `ARGETRANGE` 單次 100 萬筆上限 | 5.7 | redis.io：Redis arrays |
| 15 | Vector Set 命令、`VADD` 預設 Q8 量化、`VRANGE` 語法 | 14.4 | redis.io：Vector sets、VADD、VRANGE |
| 16 | `FT.HYBRID` 語法、RRF 預設 WINDOW 20／CONSTANT 60、預設計分器 BM25STD | 14.3 | redis.io 命令文件：FT.HYBRID |
| 17 | `LMOVEM`、`SUNIONCARD`、`SDIFFCARD`、`HIMPORT` 語法 | 5 | redis.io 命令文件 |
| 18 | 授權：7.2 以前 BSD-3；7.4～7.8 RSALv2／SSPLv1；8.x 三授權含 AGPLv3 | 1.6、9.5 | redis.io/legal/licenses |
| 19 | `rename-command` 已標示為 deprecated，建議改用 ACL | 4.6、10.4 | redis.io：Redis security；redis.conf 註解 |
| 20 | redis.conf 預設值：`save 3600 1 300 100 60 10000`、`appenddirname`、`maxmemory-policy` 選項含 lrm、`tls-auth-clients-user` 預設 off | 4 | redis/redis 8.10 分支 redis.conf |
| 21 | Multi-part AOF、AOF 備份流程、`BACKUP` 命令族、`backupdirname`、`preload-file` | 3.3、8.9 | redis.io：Redis persistence |
| 22 | redis-cli `--keystats`、`--hotkeys`、`--latency-percentiles`、`REDISCLI_AUTH` | 3.4、8 | redis.io：Redis CLI |
| 23 | 官方 APT／RPM 安裝指令與 8.10 測試過的作業系統 | 3.1 | redis.io：Install Redis Open Source；8.10 release notes |
| 24 | 官方推薦 node-redis，ioredis 缺少部分新功能 | 7.2 | redis.io：Connect with Redis client API libraries |
| 25 | Spring Data Redis 4.0 以 Jackson 3 為主，`GenericJackson2JsonRedisSerializer` 已 deprecated；`GenericJacksonJsonRedisSerializer.builder()` | 7.3 | Spring Data Redis 4.x API 文件 |
| 26 | Spring Boot 4.1 的 `spring.data.redis.*` 與 `spring.session.redis.*` 屬性 | 6.3、7.3 | Spring Boot 4.1.1 Application Properties |
| 27 | CVE-2025-49844（CVSS 10.0）修補版本 6.2.20、7.2.11、7.4.6、8.0.4、8.2.2 | 10.6 | Redis 安全公告、Wiz、各版 release notes |
| 28 | 2026 年 5 月、8 月、9 月的安全修補內容 | 10.6 | Redis 8.2～8.10 release notes |
| 29 | 各分支最新修補版與支援期限 | 9.6 | endoflife.date/redis（第三方彙整） |
| 30 | Valkey 9.0（2025-10）、9.1（2026-05）、最新 9.1.2（2026-09-01） | 1.6、15.3 | valkey.io、endoflife.date/valkey |
| 31 | Azure Cache for Redis 2028-09-30 退役、2026-10-01 起限制新建；Enterprise 2027-03-31 退役 | 15.2 | Microsoft Learn：Retirement FAQ、Azure Updates |
| 32 | ElastiCache 支援 Valkey 9.0／9.1；Memorystore for Valkey 支援 7.2／8.0／9.0／9.1 | 15.2 | AWS What's New、Google Cloud 文件 |

### D.1 待確認事項

以下項目在本版撰寫時無法取得足夠明確的官方來源，引用前請再次確認：

| # | 項目 | 目前處理方式 |
| --- | --- | --- |
| 1 | Redis Open Source 各分支的官方支援期限政策 | 9.6 採 endoflife.date 彙整並標示「參考」 |
| 2 | Lettuce、Jedis、node-redis、redis-py 最新確切版本號，以及 redis-py 7.x 預設 RESP3 的細節 | 7.8 僅描述趨勢，未寫死版本號 |
| 3 | Redis 7.4+／8.x 與 Valkey 之間 RDB 格式互通的具體版本界線 | 15.3 以「不保證互通」描述 |
| 4 | 自行編譯 8.x 時啟用內建模組的建置參數 | 3.1 僅提示需參考官方 Build from source 文件 |
| 5 | 8.x 模組命令對應的 ACL 類別完整名稱（如 `@search`、`@json`） | 10.3 建議以 `ACL CAT` 實際確認 |
| 6 | 8.10 節點間 TLS 憑證認證的設定參數名稱 | 10.5 僅描述功能 |
| 7 | 8.8 Hash 欄位層級通知的啟用參數與事件名稱 | 5.2 僅描述功能 |
| 8 | redis_exporter 最新版本與各指標名稱 | 8.8 提醒以實際版本為準 |
| 9 | Query Engine 中文分詞（`LANGUAGE chinese`）的實際效果 | 14.2 建議實測 |
| 10 | Redis LangCache 的服務範圍與區域 | 14.5 僅提及可評估 |

---

## 附錄 E：參考資料

**Redis 官方**：

- [Redis 官方文件](https://redis.io/docs/latest/)
- [Redis Commands](https://redis.io/docs/latest/commands/)
- [Redis 使用模式（Patterns）](https://redis.io/docs/latest/develop/clients/patterns/)
- [Distributed Locks with Redis](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)
- [Redis Open Source Release Notes](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/)
- [Install Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/)
- [Redis Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [Redis Security](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Redis CLI](https://redis.io/docs/latest/develop/tools/cli/)
- [Redis Client Libraries](https://redis.io/docs/latest/develop/clients/)
- [Redis Arrays](https://redis.io/docs/latest/develop/data-types/arrays/)
- [Redis Vector Sets](https://redis.io/docs/latest/develop/data-types/vector-sets/)
- [FT.HYBRID](https://redis.io/docs/latest/commands/ft.hybrid/)
- [Redis Licenses](https://redis.io/legal/licenses/)
- [Security Advisory: CVE-2025-49844](https://redis.io/blog/security-advisory-cve-2025-49844/)
- [redis/redis GitHub Releases](https://github.com/redis/redis/releases)
- [redis/redis Security Advisories](https://github.com/redis/redis/security/advisories)

**生態系與雲端**：

- [Spring Data Redis Reference](https://docs.spring.io/spring-data/redis/reference/)
- [Valkey](https://valkey.io/)
- [Azure Cache for Redis Retirement FAQ](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq)
- [Amazon ElastiCache：Valkey 9.1 支援公告](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-elasticache-valkey-9-1/)
- [Memorystore for Valkey Overview](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)
- [oliver006/redis_exporter](https://github.com/oliver006/redis_exporter)
- [endoflife.date：Redis](https://endoflife.date/redis)
