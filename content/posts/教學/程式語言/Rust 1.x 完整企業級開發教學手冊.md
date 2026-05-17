+++
date = '2026-05-17T21:57:02+08:00'
draft = false
title = 'Rust 1.x 完整企業級開發教學手冊'
tags = ['教學', '程式語言']
categories = ['教學']
+++

# Rust 1.x 完整企業級開發教學手冊

> **版本**: 2.0  
> **最後更新**: 2026 年 5 月 17 日
> **適用對象**: 新手工程師、中階工程師、資深工程師、架構師、技術主管、DevOps 團隊  
> **技術層級**: 初階 → 進階 → 架構師級  
> **Rust 版本**: 1.95.0 穩定版（Edition 2024）  
> **授權**: 內部教育訓練使用  
> **參考來源**: [rust-lang.org](https://www.rust-lang.org/)、[The Rust Book](https://doc.rust-lang.org/book/)、[crates.io](https://crates.io/)、[docs.rs](https://docs.rs/)、[rustup.rs](https://rustup.rs/)

---

## 目錄

1. [Rust 介紹](#1-rust-介紹)
   - [1.1 Rust 歷史與發展](#11-rust-歷史與發展)
   - [1.2 Rust 設計理念](#12-rust-設計理念)
   - [1.3 Rust 與 C/C++ 差異](#13-rust-與-cc-差異)
   - [1.4 Rust 與 Java/Golang 差異](#14-rust-與-javagolang-差異)
   - [1.5 Rust 適合的應用場景](#15-rust-適合的應用場景)
   - [1.6 Rust 不適合的場景](#16-rust-不適合的場景)
   - [1.7 Rust 生態系介紹](#17-rust-生態系介紹)
   - [1.8 Cargo 介紹](#18-cargo-介紹)
   - [1.9 Crates.io 介紹](#19-cratesio-介紹)
   - [1.10 docs.rs 介紹](#110-docsrs-介紹)
2. [Rust 核心特色](#2-rust-核心特色)
   - [2.1 Ownership（所有權）](#21-ownership所有權)
   - [2.2 Borrowing（借用）](#22-borrowing借用)
   - [2.3 Lifetime（生命週期）](#23-lifetime生命週期)
   - [2.4 Move Semantics](#24-move-semantics)
   - [2.5 Zero-Cost Abstraction](#25-zero-cost-abstraction)
   - [2.6 Pattern Matching](#26-pattern-matching)
   - [2.7 Traits](#27-traits)
   - [2.8 Generics](#28-generics)
   - [2.9 Async/Await](#29-asyncawait)
   - [2.10 Memory Safety](#210-memory-safety)
   - [2.11 Concurrency Safety](#211-concurrency-safety)
3. [開發環境安裝](#3-開發環境安裝)
   - [3.1 Windows 環境安裝](#31-windows-環境安裝)
   - [3.2 Linux 環境安裝](#32-linux-環境安裝)
   - [3.3 macOS 環境安裝](#33-macos-環境安裝)
   - [3.4 VSCode 設定](#34-vscode-設定)
   - [3.5 IntelliJ Rust 設定](#35-intellij-rust-設定)
   - [3.6 Toolchain 管理](#36-toolchain-管理)
   - [3.7 nightly / stable / beta 差異](#37-nightly--stable--beta-差異)
4. [Cargo 完整教學](#4-cargo-完整教學)
   - [4.1 專案建立與初始化](#41-專案建立與初始化)
   - [4.2 建置與執行](#42-建置與執行)
   - [4.3 測試與文件](#43-測試與文件)
   - [4.4 程式碼品質工具](#44-程式碼品質工具)
   - [4.5 安全性稽核](#45-安全性稽核)
   - [4.6 發佈與套件管理](#46-發佈與套件管理)
   - [4.7 Workspace 管理](#47-workspace-管理)
   - [4.8 相依性管理與語意版本](#48-相依性管理與語意版本)
5. [Rust 基礎語法](#5-rust-基礎語法)
   - [5.1 變數與可變性](#51-變數與可變性)
   - [5.2 資料型別](#52-資料型別)
   - [5.3 函式](#53-函式)
   - [5.4 控制流程](#54-控制流程)
   - [5.5 迴圈](#55-迴圈)
   - [5.6 結構體（Struct）](#56-結構體struct)
   - [5.7 列舉（Enum）](#57-列舉enum)
   - [5.8 模組系統](#58-模組系統)
   - [5.9 錯誤處理（Result / Option）](#59-錯誤處理result--option)
   - [5.10 集合（Collections）](#510-集合collections)
   - [5.11 迭代器（Iterators）](#511-迭代器iterators)
   - [5.12 閉包（Closures）](#512-閉包closures)
6. [Rust 進階教學](#6-rust-進階教學)
   - [6.1 Traits 深入](#61-traits-深入)
   - [6.2 Lifetimes 深入](#62-lifetimes-深入)
   - [6.3 Smart Pointers](#63-smart-pointers)
   - [6.4 Rc / Arc](#64-rc--arc)
   - [6.5 Mutex / RwLock](#65-mutex--rwlock)
   - [6.6 Channels（通道）](#66-channels通道)
   - [6.7 Async Runtime 與 Tokio](#67-async-runtime-與-tokio)
   - [6.8 Pin / Unpin](#68-pin--unpin)
   - [6.9 Unsafe Rust](#69-unsafe-rust)
   - [6.10 Macros（巨集）](#610-macros巨集)
   - [6.11 Procedural Macros](#611-procedural-macros)
7. [Rust Web 開發](#7-rust-web-開發)
   - [7.1 Web Framework 比較](#71-web-framework-比較)
   - [7.2 Axum 概觀](#72-axum-概觀)
   - [7.3 Actix Web 概觀](#73-actix-web-概觀)
   - [7.4 Rocket 概觀](#74-rocket-概觀)
   - [7.5 Warp 概觀](#75-warp-概觀)
   - [7.6 Framework 選型建議](#76-framework-選型建議)
8. [使用 Axum 建立 RESTful API](#8-使用-axum-建立-restful-api)
   - [8.1 專案架構（Clean Architecture）](#81-專案架構clean-architecture)
   - [8.2 DTO 與資料驗證](#82-dto-與資料驗證)
   - [8.3 Service Layer](#83-service-layer)
   - [8.4 Repository Pattern](#84-repository-pattern)
   - [8.5 Middleware](#85-middleware)
   - [8.6 JWT 認證與授權](#86-jwt-認證與授權)
   - [8.7 OpenAPI / Swagger](#87-openapi--swagger)
   - [8.8 完整 API 範例](#88-完整-api-範例)
   - [8.9 Docker 化](#89-docker-化)
9. [資料庫整合](#9-資料庫整合)
   - [9.1 SQLx（推薦）](#91-sqlx推薦)
   - [9.2 Diesel](#92-diesel)
   - [9.3 SeaORM](#93-seaorm)
   - [9.4 ORM 比較表](#94-orm-比較表)
   - [9.5 Redis 快取](#95-redis-快取)
   - [9.6 PostgreSQL 整合實務](#96-postgresql-整合實務)
   - [9.7 MySQL 整合實務](#97-mysql-整合實務)
   - [9.8 SQLite 整合實務](#98-sqlite-整合實務)
10. [非同步程式設計與高併發](#10-非同步程式設計與高併發)
    - [10.1 Tokio Runtime 詳解](#101-tokio-runtime-詳解)
    - [10.2 任務產生與管理](#102-任務產生與管理)
    - [10.3 並行模式](#103-並行模式)
    - [10.4 Stream 處理](#104-stream-處理)
    - [10.5 限流與背壓](#105-限流與背壓)
    - [10.6 Graceful Shutdown](#106-graceful-shutdown)
    - [10.7 Actor Model](#107-actor-model)
    - [10.8 高併發架構設計](#108-高併發架構設計)
11. [WebAssembly（WASM）](#11-webassemblywasm)
    - [11.1 WASM 概念](#111-wasm-概念)
    - [11.2 wasm-pack 建置](#112-wasm-pack-建置)
    - [11.3 在前端使用 WASM](#113-在前端使用-wasm)
    - [11.4 WASM 使用場景](#114-wasm-使用場景)
    - [11.5 Rust + React 整合範例](#115-rust--react-整合範例)
    - [11.6 WASM 效能優化](#116-wasm-效能優化)
12. [系統架構設計](#12-系統架構設計)
    - [12.1 Clean Architecture](#121-clean-architecture)
    - [12.2 Hexagonal Architecture（六角架構）](#122-hexagonal-architecture六角架構)
    - [12.3 微服務架構](#123-微服務架構)
    - [12.4 事件驅動架構](#124-事件驅動架構)
    - [12.5 CQRS（命令與查詢責任分離）](#125-cqrs命令與查詢責任分離)
    - [12.6 架構比較](#126-架構比較)
    - [12.7 模組拆分策略](#127-模組拆分策略)
13. [Docker 與 Kubernetes](#13-docker-與-kubernetes)
    - [13.1 Dockerfile 最佳實務](#131-dockerfile-最佳實務)
    - [13.2 Docker Compose 企業配置](#132-docker-compose-企業配置)
    - [13.3 Kubernetes 部署](#133-kubernetes-部署)
    - [13.4 Helm Chart 結構](#134-helm-chart-結構)
    - [13.5 Service / Ingress / ConfigMap / Secret](#135-service--ingress--configmap--secret)
    - [13.6 HPA 自動擴展](#136-hpa-自動擴展)
14. [測試策略](#14-測試策略)
    - [14.1 單元測試](#141-單元測試)
    - [14.2 整合測試](#142-整合測試)
    - [14.3 屬性測試（Property-Based Testing）](#143-屬性測試property-based-testing)
    - [14.4 效能測試](#144-效能測試)
    - [14.5 測試金字塔](#145-測試金字塔)
    - [14.6 Mock Test（mockall）](#146-mock-testmockall)
    - [14.7 Benchmark（criterion）](#147-benchmarkcriterion)
15. [DevSecOps 與 SSDLC](#15-devsecops-與-ssdlc)
    - [15.1 GitHub Actions CI/CD](#151-github-actions-cicd)
    - [15.2 SSDLC 安全開發生命週期](#152-ssdlc-安全開發生命週期)
    - [15.3 供應鏈安全](#153-供應鏈安全)
    - [15.4 模糊測試（Fuzzing）](#154-模糊測試fuzzing)
    - [15.5 SBOM 與 Dependency Scan](#155-sbom-與-dependency-scan)
    - [15.6 Secret Scan 與 Container Scan](#156-secret-scan-與-container-scan)
16. [可觀測性（Observability）](#16-可觀測性observability)
    - [16.1 日誌（Logging）](#161-日誌logging)
    - [16.2 指標（Metrics）](#162-指標metrics)
    - [16.3 分散式追蹤（Distributed Tracing）](#163-分散式追蹤distributed-tracing)
    - [16.4 可觀測性架構](#164-可觀測性架構)
    - [16.5 健康檢查端點](#165-健康檢查端點)
17. [效能調校](#17-效能調校)
    - [17.1 Profile 工具](#171-profile-工具)
    - [17.2 編譯最佳化](#172-編譯最佳化)
    - [17.3 常見效能最佳化技巧](#173-常見效能最佳化技巧)
    - [17.4 Async 效能調校](#174-async-效能調校)
    - [17.5 效能檢查清單](#175-效能檢查清單)
    - [17.6 Lock Contention 分析](#176-lock-contention-分析)
18. [團隊建立與治理](#18-團隊建立與治理)
    - [18.1 Rust 團隊組建策略](#181-rust-團隊組建策略)
    - [18.2 程式碼規範](#182-程式碼規範)
    - [18.3 Code Review 檢查清單](#183-code-review-檢查清單)
    - [18.4 技術債管理](#184-技術債管理)
    - [18.5 開發流程（Git Flow / Trunk Based）](#185-開發流程git-flow--trunk-based)
    - [18.6 文件治理](#186-文件治理)
    - [18.7 AI 使用規範](#187-ai-使用規範)
19. [AI 協作開發](#19-ai-協作開發)
    - [19.1 GitHub Copilot 與 Rust](#191-github-copilot-與-rust)
    - [19.2 AI 輔助的工作流程](#192-ai-輔助的工作流程)
    - [19.3 Prompt 撰寫技巧](#193-prompt-撰寫技巧)
    - [19.4 AI Pair Programming](#194-ai-pair-programming)
    - [19.5 AI Review 與 Test Generation](#195-ai-review-與-test-generation)
    - [19.6 Team Prompt Library](#196-team-prompt-library)
20. [企業級最佳實務](#20-企業級最佳實務)
    - [20.1 專案結構最佳實務](#201-專案結構最佳實務)
    - [20.2 設定管理](#202-設定管理)
    - [20.3 版本管理策略](#203-版本管理策略)
    - [20.4 錯誤處理最佳實務](#204-錯誤處理最佳實務)
    - [20.5 API Versioning](#205-api-versioning)
    - [20.6 Security Best Practices](#206-security-best-practices)
    - [20.7 Scalability 與 High Availability](#207-scalability-與-high-availability)
21. [Rust 生態系推薦](#21-rust-生態系推薦)
    - [21.1 依類別推薦 Crate](#211-依類別推薦-crate)
    - [21.2 Crate 評估準則](#212-crate-評估準則)
    - [21.3 CLI 與 DevOps 類別](#213-cli-與-devops-類別)
    - [21.4 AI 與 WASM 類別](#214-ai-與-wasm-類別)
22. [完整企業級專案實戰](#22-完整企業級專案實戰)
    - [22.1 專案架構](#221-專案架構)
    - [22.2 Cargo.toml](#222-cargotoml)
    - [22.3 main.rs 入口](#223-mainrs-入口)
    - [22.4 領域模型](#224-領域模型)
    - [22.5 Repository 層](#225-repository-層)
    - [22.6 Service 層（含 Redis 快取）](#226-service-層含-redis-快取)
    - [22.7 API Handler](#227-api-handler)
    - [22.8 JWT 認證中介層](#228-jwt-認證中介層)
    - [22.9 路由組裝](#229-路由組裝)
    - [22.10 資料庫遷移](#2210-資料庫遷移)
    - [22.11 Docker 化部署](#2211-docker-化部署)
23. [常見問題與解答（FAQ）](#23-常見問題與解答faq)
    - [23.1 編譯相關](#231-編譯相關)
    - [23.2 Async 相關](#232-async-相關)
    - [23.3 專案實務](#233-專案實務)
    - [23.4 Async Deadlock](#234-async-deadlock)
    - [23.5 Memory Leak 排查](#235-memory-leak-排查)
    - [23.6 Cargo 問題](#236-cargo-問題)
24. [學習路線圖](#24-學習路線圖)
    - [24.1 各階段推薦資源](#241-各階段推薦資源)
    - [24.2 初學者路線（0-3 個月）](#242-初學者路線0-3-個月)
    - [24.3 中階路線（3-6 個月）](#243-中階路線3-6-個月)
    - [24.4 高階與架構師路線（6-12 個月）](#244-高階與架構師路線6-12-個月)
25. [結論](#25-結論)
    - [25.1 Rust 在企業中的價值](#251-rust-在企業中的價值)
    - [25.2 導入建議](#252-導入建議)
    - [25.3 技術選型建議](#253-技術選型建議)
26. [附錄：新進成員檢查清單](#26-附錄新進成員檢查清單)
    - [26.1 環境建置（第 1 天）](#261-環境建置第-1-天)
    - [26.2 開發規範熟悉（第 1-2 週）](#262-開發規範熟悉第-1-2-週)
    - [26.3 進階能力（第 3-4 週）](#263-進階能力第-3-4-週)
    - [26.4 獨立作業（第 5-8 週）](#264-獨立作業第-5-8-週)
27. [版本歷史](#27-版本歷史)

---

## Rust 學習路徑總覽

```mermaid
graph LR
    A[🟢 新手入門] --> B[🔵 基礎語法]
    B --> C[🟡 核心特色]
    C --> D[🟠 進階開發]
    D --> E[🔴 企業實戰]

    A --- A1[安裝環境]
    A --- A2[Cargo 基礎]

    B --- B1[變數/函式/流程控制]
    B --- B2[Struct/Enum/Module]
    B --- B3[錯誤處理/集合]

    C --- C1[Ownership/Borrowing]
    C --- C2[Lifetime]
    C --- C3[Traits/Generics]

    D --- D1[Async/Tokio]
    D --- D2[Web API/Axum]
    D --- D3[資料庫整合]

    E --- E1[架構設計]
    E --- E2[Docker/K8s]
    E --- E3[DevSecOps/CI-CD]
    E --- E4[Observability]
```

---

## 1. Rust 介紹

### 1.1 Rust 歷史與發展

Rust 是一門注重**安全性**、**效能**與**並發性**的現代系統級程式語言。

**發展歷程：**

| 年份 | 里程碑 |
|------|--------|
| 2006 | Graydon Hoare 在 Mozilla 以個人專案開始開發 Rust |
| 2009 | Mozilla 正式贊助 Rust 開發 |
| 2010 | Rust 首次公開發表（v0.1） |
| 2012 | 引入 Ownership 與 Borrowing 機制 |
| 2015 | **Rust 1.0 穩定版**正式發布，承諾向後相容 |
| 2018 | Rust 2018 Edition 發布，引入 `async/await` 語法 |
| 2021 | Rust 2021 Edition 發布，Rust Foundation 成立 |
| 2024 | Rust 2024 Edition 發布（Rust 1.85 起支援），語言持續演進 |
| 2025 | Rust 1.95.0（最新穩定版），被 Linux Kernel、Android、Windows 核心採用 |

**重要事件：**

- 🏆 Stack Overflow 連續多年「最受開發者喜愛的程式語言」第一名
- 🐧 Linux Kernel 6.1+ 正式支援 Rust 作為第二開發語言
- 🤖 Google Android 團隊大量使用 Rust 開發底層元件
- 🪟 Microsoft 使用 Rust 重寫 Windows 核心元件
- ☁️ AWS、Cloudflare、Discord、Dropbox 等企業在生產環境使用 Rust

### 1.2 Rust 設計理念

Rust 的核心設計哲學可歸納為三大支柱：

```mermaid
graph TD
    R[Rust 設計理念] --> S[Safety<br/>安全性]
    R --> P[Performance<br/>效能]
    R --> C[Concurrency<br/>並發性]

    S --> S1[編譯期記憶體安全]
    S --> S2[無 Null / 無 GC]
    S --> S3[型別安全]

    P --> P1[零成本抽象]
    P --> P2[無執行期開銷]
    P --> P3[極致最佳化]

    C --> C1[無資料競爭]
    C --> C2[Send / Sync Traits]
    C --> C3[Async/Await]
```

**核心原則：**

1. **記憶體安全不犧牲效能**：透過 Ownership 系統在編譯期保證記憶體安全，無需 GC
2. **零成本抽象（Zero-Cost Abstraction）**：高階抽象的效能等同於手寫底層程式碼
3. **錯誤在編譯期捕獲**：嚴格的型別系統與 Borrow Checker 將大多數錯誤提前至編譯階段
4. **顯式優於隱式**：所有的記憶體操作、錯誤處理均需明確表達
5. **實用主義**：提供 `unsafe` 逃生出口，兼顧安全與彈性

### 1.3 Rust 與 C/C++ 差異

| 比較項目 | Rust | C | C++ |
|---------|------|---|-----|
| 記憶體安全 | ✅ 編譯期保證（Ownership） | ❌ 手動管理，易產生 UB | ❌ 手動管理 + RAII |
| Null Safety | ✅ 無 null（使用 `Option<T>`） | ❌ Null Pointer | ❌ Null Pointer |
| Data Race | ✅ 編譯期防止 | ❌ 需手動同步 | ❌ 需手動同步 |
| 垃圾回收 | ❌ 無 GC（零開銷） | ❌ 無 GC | ❌ 無 GC |
| 套件管理 | ✅ Cargo（內建） | ❌ 無標準工具 | ❌ CMake / Conan 等 |
| 建置系統 | ✅ Cargo（統一） | ❌ Make / CMake | ❌ CMake / Meson |
| 錯誤處理 | `Result<T, E>` / `Option<T>` | errno / return code | Exception |
| 學習曲線 | 中等偏高 | 中等 | 高 |
| 編譯速度 | 較慢（特別是大型專案） | 快 | 慢 |
| 執行效能 | 極高（媲美 C） | 極高 | 極高 |

**⚠️ 關鍵差異：Rust 透過 Ownership 系統在編譯期消除了 C/C++ 中常見的記憶體安全漏洞（Use-After-Free、Buffer Overflow、Double Free）。**

### 1.4 Rust 與 Java/Golang 差異

| 比較項目 | Rust | Java | Go |
|---------|------|------|----|
| 執行模型 | 編譯為原生機器碼 | JVM 位元碼 | 編譯為原生機器碼 |
| GC 機制 | ❌ 無 GC | ✅ JVM GC | ✅ GC（三色標記） |
| 記憶體開銷 | 極低 | 較高（JVM） | 中等 |
| 啟動速度 | 極快 | 慢（JVM Cold Start） | 快 |
| 並發模型 | async/await + 多執行緒 | Thread + Virtual Thread | Goroutine |
| 型別系統 | 強型別 + ADT | 強型別 + OOP | 強型別 + 結構化 |
| Null 處理 | `Option<T>` | `null`（NullPointerException） | 零值（zero value） |
| 錯誤處理 | `Result<T, E>` | try-catch Exception | error 回傳值 |
| 泛型 | ✅ 單態化（Monomorphization） | ✅ 型別擦除 | ✅（Go 1.18+） |
| 學習曲線 | 高 | 中 | 低 |
| 生態成熟度 | 快速成長 | 極成熟 | 成熟 |
| 適合場景 | 系統級 / 高效能 | 企業應用 / 微服務 | 雲原生 / 微服務 |

### 1.5 Rust 適合的應用場景

| 場景 | 說明 | 代表專案 |
|------|------|---------|
| ⚡ 高效能網路服務 | 低延遲、高吞吐量的 API 服務 | Cloudflare Workers、Discord |
| 🐧 作業系統 / 核心開發 | Linux Kernel Module、驅動程式 | Linux Kernel、Redox OS |
| 🌐 WebAssembly | 前端高效能計算模組 | Figma、Photoshop Web |
| 🔐 安全敏感系統 | 密碼學、區塊鏈、安全工具 | Solana、Firecracker |
| 🎮 遊戲引擎 | 高效能遊戲邏輯與渲染 | Bevy Engine |
| 📦 CLI 工具 | 快速啟動的命令列工具 | ripgrep、fd、bat、exa |
| 🗄️ 資料庫引擎 | 高效能儲存引擎 | TiKV、SurrealDB |
| 📡 嵌入式系統 | 低資源消耗的嵌入式裝置 | Embassy Framework |
| 🤖 AI / ML 基礎設施 | 推論引擎、資料處理管線 | Candle、Burn |

### 1.6 Rust 不適合的場景

| 場景 | 原因 | 替代建議 |
|------|------|---------|
| 快速原型開發 | 編譯器嚴格，開發速度較慢 | Python、Go、TypeScript |
| 簡單腳本 | 過度工程化 | Bash、Python |
| 既有 Java/C# 企業系統擴展 | 團隊學習成本高 | 繼續使用既有語言 |
| 資料科學 / 機器學習（高階） | 生態不如 Python 成熟 | Python + PyTorch |
| GUI 桌面應用 | GUI 生態仍在發展中 | Electron、Qt、Flutter |
| 需要大量反射的應用 | Rust 不支援執行期反射 | Java、C# |

### 1.7 Rust 生態系介紹

```mermaid
graph TD
    ECO[Rust 生態系統] --> LANG[語言核心]
    ECO --> TOOLS[工具鏈]
    ECO --> COMMUNITY[社群資源]

    LANG --> LANG1[rustc 編譯器]
    LANG --> LANG2[Standard Library]
    LANG --> LANG3[Editions 2015/2018/2021/2024]

    TOOLS --> TOOLS1[Cargo 套件管理]
    TOOLS --> TOOLS2[rustup 工具鏈管理]
    TOOLS --> TOOLS3[rustfmt 格式化]
    TOOLS --> TOOLS4[clippy 靜態分析]
    TOOLS --> TOOLS5[rust-analyzer LSP]

    COMMUNITY --> COM1[crates.io 套件中心]
    COMMUNITY --> COM2[docs.rs 文件中心]
    COMMUNITY --> COM3[The Rust Book]
    COMMUNITY --> COM4[Rust Playground]
    COMMUNITY --> COM5[This Week in Rust]
```

**核心元件：**

- **rustc**：Rust 編譯器，基於 LLVM 後端，產出高效能原生機器碼
- **Standard Library（std）**：提供核心資料結構、I/O、多執行緒、網路等基礎功能
- **Editions**：每三年發布一次新版本（2015 → 2018 → 2021 → 2024），保持向後相容

### 1.8 Cargo 介紹

Cargo 是 Rust 的**官方建置系統與套件管理器**，整合了從專案建立到發佈的完整開發生命週期。

**核心功能：**

```bash
# 建立新專案
cargo new my-project

# 建置專案
cargo build --release

# 執行專案
cargo run

# 執行測試
cargo test

# 格式化程式碼
cargo fmt

# 靜態分析
cargo clippy

# 安全稽核
cargo audit

# 產生文件
cargo doc --open
```

**Cargo.toml 範例：**

```toml
[package]
name = "enterprise-api"
version = "1.0.0"
edition = "2024"
authors = ["開發團隊 <team@company.com>"]
description = "企業級 REST API 服務"
license = "MIT"
rust-version = "1.95"

[dependencies]
axum = "0.8"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
sqlx = { version = "0.8", features = ["runtime-tokio", "postgres"] }
tracing = "0.1"

[dev-dependencies]
criterion = { version = "0.5", features = ["html_reports"] }
mockall = "0.13"

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
strip = true
```

### 1.9 Crates.io 介紹

[Crates.io](https://crates.io/) 是 Rust 的**官方套件註冊中心**，類似於 npm（Node.js）、Maven Central（Java）或 PyPI（Python）。

**關鍵特色：**

- 📦 超過 **26.8 萬+** 已發佈的套件（crates），累計下載次數超過 **3,060 億次**
- 🔒 每個版本一旦發佈即不可變更（immutable publishing）
- 📊 下載統計、版本歷史、相依性分析
- 🔍 全文搜尋與分類瀏覽
- 🛡️ 與 `cargo audit` 整合的安全漏洞資料庫（RustSec Advisory）

**常用 crate 速查：**

| 分類 | Crate | 用途 |
|------|-------|------|
| Web 框架 | `axum` | 高效能 Web 框架（Tokio 生態） |
| 序列化 | `serde` | 通用序列化 / 反序列化框架 |
| 非同步 | `tokio` | 非同步執行時期 |
| 資料庫 | `sqlx` | 編譯期檢查的 SQL 工具 |
| 日誌 | `tracing` | 結構化日誌與追蹤 |
| CLI | `clap` | 命令列參數解析 |
| HTTP 客戶端 | `reqwest` | 非同步 HTTP 客戶端 |
| 測試 | `mockall` | Mock 框架 |

### 1.10 docs.rs 介紹

[docs.rs](https://docs.rs/) 是 Rust 的**自動化文件託管平台**，自動為 crates.io 上所有已發佈的 crate 產生 API 文件。

**特色：**

- 📖 自動從 `///` 和 `//!` 註解產生結構化文件
- 🔗 跨 crate 的型別連結
- 🏷️ Feature flag 切換文件檢視
- 📱 響應式設計，支援行動裝置瀏覽
- 🌙 暗色 / 亮色主題

**撰寫文件範例：**

```rust
/// 使用者帳戶管理服務
///
/// 提供使用者的 CRUD 操作，包含驗證與授權邏輯。
///
/// # 範例
///
/// ```rust
/// use enterprise_api::UserService;
///
/// let service = UserService::new(pool);
/// let user = service.find_by_id(1).await?;
/// println!("使用者名稱: {}", user.name);
/// ```
///
/// # 錯誤
///
/// 當使用者不存在時，回傳 [`AppError::NotFound`]。
pub struct UserService {
    pool: PgPool,
}
```

> 💡 **實務建議**：在企業專案中，強制要求所有 `pub` 型別與函式都必須附帶 `///` 文件註解，並在 CI 中加入 `#![deny(missing_docs)]` 檢查。

---

## 2. Rust 核心特色

Rust 最獨特且最重要的特色是其**所有權系統（Ownership System）**，這是理解整個語言的基石。

### 2.1 Ownership（所有權）

#### 所有權規則

Rust 中每一個值都有一個**所有者（Owner）**，且同一時間只能有一個所有者。

```
Rust 所有權三大規則：
1. 每個值都有一個所有者（owner）
2. 同一時間只能有一個所有者
3. 當所有者離開作用域，值會被自動釋放（drop）
```

```mermaid
graph LR
    subgraph "Stack（堆疊）"
        S1["s1: ptr → | len: 5 | cap: 5"]
    end
    subgraph "Heap（堆積）"
        H1["h | e | l | l | o"]
    end
    S1 --> H1

    style S1 fill:#4CAF50,color:white
    style H1 fill:#2196F3,color:white
```

#### 基本範例

```rust
fn main() {
    // 規則 1：每個值都有一個所有者
    let s1 = String::from("hello"); // s1 是 "hello" 的所有者

    // 規則 2：同一時間只能有一個所有者（所有權轉移）
    let s2 = s1; // 所有權從 s1 轉移到 s2
    // println!("{}", s1); // ❌ 編譯錯誤！s1 已經失效

    println!("{}", s2); // ✅ s2 是有效的所有者

    // 規則 3：離開作用域時自動釋放
    {
        let s3 = String::from("world");
        println!("{}", s3); // ✅ s3 在作用域內有效
    } // s3 在此被自動 drop

    // println!("{}", s3); // ❌ s3 已不存在
}
```

#### 所有權轉移（Move）圖解

```mermaid
sequenceDiagram
    participant S as Stack
    participant H as Heap

    Note over S,H: let s1 = String::from("hello")
    S->>H: s1 擁有 heap 資料
    Note over S: s1: {ptr, len:5, cap:5}

    Note over S,H: let s2 = s1 （Move）
    S->>S: s1 的資料複製到 s2
    S--xH: s1 失效 ❌
    Note over S: s2: {ptr, len:5, cap:5}
    Note over S: s1: 已失效

    Note over S,H: } 離開作用域
    S->>H: s2 的 drop() 被呼叫
    Note over H: heap 記憶體被釋放
```

#### ⚠️ 常見錯誤：Use After Move

```rust
fn main() {
    let name = String::from("Rust");
    let greeting = format!("Hello, {}!", name); // name 仍有效（format! 使用借用）

    let moved_name = name; // 所有權轉移
    // println!("{}", name); // ❌ 編譯錯誤 E0382
    // error[E0382]: borrow of moved value: `name`
    //   --> src/main.rs:5:24
    //   |
    // 2 |     let name = String::from("Rust");
    //   |         ---- move occurs because `name` has type `String`
    // 4 |     let moved_name = name;
    //   |                      ---- value moved here
    // 5 |     println!("{}", name);
    //   |                    ^^^^ value borrowed here after move

    println!("{}", moved_name); // ✅
}
```

#### 函式與所有權

```rust
fn main() {
    let s = String::from("hello");

    // 所有權轉移進函式
    takes_ownership(s);
    // println!("{}", s); // ❌ s 已被移動

    let x = 5;
    makes_copy(x); // i32 實作了 Copy trait，所以是複製
    println!("{}", x); // ✅ x 仍有效

    // 函式回傳值轉移所有權
    let s2 = gives_ownership();
    println!("{}", s2); // ✅
}

fn takes_ownership(some_string: String) {
    println!("{}", some_string);
} // some_string 在此被 drop

fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
}

fn gives_ownership() -> String {
    String::from("hello") // 所有權轉移給呼叫者
}
```

### 2.2 Borrowing（借用）

借用讓你在不取得所有權的情況下存取資料，分為**不可變借用（`&T`）**與**可變借用（`&mut T`）**。

#### 借用規則

```
借用規則：
1. 同一時間可以有多個不可變借用（&T）
2. 同一時間只能有一個可變借用（&mut T）
3. 不可變借用與可變借用不能同時存在
```

```mermaid
graph TD
    V["值 (Value)"] --> IMM["不可變借用 &T"]
    V --> MUT["可變借用 &mut T"]

    IMM --> IMM1["&T ✅"]
    IMM --> IMM2["&T ✅"]
    IMM --> IMM3["&T ✅"]
    IMM -.- NOTE1["可以同時存在多個"]

    MUT --> MUT1["&mut T ✅"]
    MUT -.- NOTE2["同一時間只能有一個"]

    IMM -.->|"❌ 不可同時"| MUT

    style IMM fill:#4CAF50,color:white
    style MUT fill:#FF9800,color:white
```

#### 借用範例

```rust
fn main() {
    let s = String::from("hello");

    // 不可變借用：可以同時多個
    let r1 = &s;
    let r2 = &s;
    println!("{} and {}", r1, r2); // ✅ 多個不可變借用

    // 可變借用：同一時間只能一個
    let mut s = String::from("hello");
    let r3 = &mut s;
    r3.push_str(", world");
    println!("{}", r3); // ✅

    // ❌ 不可變 + 可變借用不能同時存在
    // let r4 = &s;
    // let r5 = &mut s;
    // println!("{}, {}", r4, r5); // 編譯錯誤 E0502
}

/// 使用借用避免所有權轉移
fn calculate_length(s: &String) -> usize {
    s.len()
} // s 離開作用域，但因為沒有所有權，不會 drop

fn change(s: &mut String) {
    s.push_str(", world");
}
```

#### ⚠️ 常見錯誤：同時存在不可變與可變借用

```rust
fn main() {
    let mut s = String::from("hello");

    let r1 = &s;     // ✅ 不可變借用
    let r2 = &s;     // ✅ 另一個不可變借用
    // let r3 = &mut s; // ❌ 編譯錯誤！
    // error[E0502]: cannot borrow `s` as mutable because it is also
    //               borrowed as immutable

    println!("{} and {}", r1, r2);
    // r1 和 r2 在此之後不再使用（NLL: Non-Lexical Lifetimes）

    let r3 = &mut s;  // ✅ 因為 r1, r2 已不再使用
    r3.push_str(", world");
    println!("{}", r3);
}
```

### 2.3 Lifetime（生命週期）

生命週期是 Rust 用來確保**引用始終有效**的機制。大多數時候編譯器可以自動推斷（Lifetime Elision），但有時需要明確標註。

#### 生命週期基本概念

```mermaid
graph TD
    subgraph "作用域"
        A["'a: 外層作用域 ─────────────────"] --- B["'b: 內層作用域 ──────"]
    end

    C["r: &'a T ── 引用的生命週期不能超過 'a"]
    D["x: T ───── 值的生命週期為 'a"]

    style A fill:#4CAF50,color:white
    style B fill:#FF9800,color:white
```

#### 生命週期標註範例

```rust
// 返回兩個字串切片中較長的那個
// 需要標註生命週期，因為編譯器無法確定回傳值的生命週期
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let string1 = String::from("long string");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
        println!("最長的字串: {}", result); // ✅ 在 string2 的作用域內
    }
    // println!("{}", result); // ❌ string2 已離開作用域
}
```

#### 結構體中的生命週期

```rust
/// 包含引用的結構體必須標註生命週期
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    /// 回傳引用的方法，生命週期會自動推斷（Elision Rule #3）
    fn level(&self) -> i32 {
        3
    }

    /// 回傳自身引用，需要與 self 相同的生命週期
    fn announce_and_return(&self, announcement: &str) -> &'a str {
        println!("注意: {}", announcement);
        self.part
    }
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("找不到 '.'");
    let excerpt = Excerpt {
        part: first_sentence,
    };
    println!("摘錄: {}", excerpt.part);
}
```

#### Lifetime Elision Rules（生命週期省略規則）

編譯器會自動套用以下三條規則來推斷生命週期：

| 規則 | 說明 | 範例 |
|------|------|------|
| 規則 1 | 每個引用參數獲得獨立的生命週期 | `fn foo(x: &str, y: &str)` → `fn foo<'a, 'b>(x: &'a str, y: &'b str)` |
| 規則 2 | 若只有一個引用參數，輸出生命週期 = 輸入生命週期 | `fn foo(x: &str) -> &str` → `fn foo<'a>(x: &'a str) -> &'a str` |
| 規則 3 | 若方法有 `&self`，輸出生命週期 = `self` 的生命週期 | `fn foo(&self, x: &str) -> &str` → `&self` 的生命週期 |

### 2.4 Move Semantics

Move 是 Rust 預設的值傳遞方式（對於未實作 `Copy` trait 的型別）。

```rust
fn main() {
    // ======== Move 語意（預設）========
    let v1 = vec![1, 2, 3];
    let v2 = v1; // Move：v1 的所有權轉移到 v2
    // println!("{:?}", v1); // ❌ v1 已失效

    // ======== Copy 語意（基本型別）========
    let x = 42;
    let y = x; // Copy：x 被複製（i32 實作了 Copy）
    println!("x = {}, y = {}", x, y); // ✅ 兩者都有效

    // ======== Clone（顯式深拷貝）========
    let s1 = String::from("hello");
    let s2 = s1.clone(); // 明確的深拷貝
    println!("s1 = {}, s2 = {}", s1, s2); // ✅ 兩者都有效
}
```

**實作 Copy 的型別：**

| 型別 | 實作 Copy |
|------|----------|
| 整數（`i32`, `u64` 等） | ✅ |
| 浮點數（`f32`, `f64`） | ✅ |
| 布林（`bool`） | ✅ |
| 字元（`char`） | ✅ |
| 固定大小 Tuple（成員皆為 Copy） | ✅ |
| 固定大小 Array（元素為 Copy） | ✅ |
| `String` | ❌（堆積配置） |
| `Vec<T>` | ❌（堆積配置） |
| `Box<T>` | ❌（堆積配置） |

### 2.5 Zero-Cost Abstraction

零成本抽象意味著你使用的高階抽象不會帶來額外的執行期開銷。

```rust
// ======== 迭代器鏈（編譯後等同手寫迴圈）========
fn sum_of_squares_even(numbers: &[i32]) -> i32 {
    numbers
        .iter()
        .filter(|&&x| x % 2 == 0)    // 過濾偶數
        .map(|&x| x * x)              // 計算平方
        .sum()                         // 加總
}
// 編譯器會將上述程式碼最佳化為單一迴圈，效能等同於：
fn sum_of_squares_even_manual(numbers: &[i32]) -> i32 {
    let mut sum = 0;
    for &x in numbers {
        if x % 2 == 0 {
            sum += x * x;
        }
    }
    sum
}

// ======== Trait Object vs 泛型（靜態分派）========
// 靜態分派（零成本）—— 編譯期確定呼叫目標
fn print_area<T: Shape>(shape: &T) {
    println!("面積: {}", shape.area());
}

// 動態分派（有成本）—— 執行期透過 vtable 查詢
fn print_area_dyn(shape: &dyn Shape) {
    println!("面積: {}", shape.area());
}

trait Shape {
    fn area(&self) -> f64;
}
```

### 2.6 Pattern Matching

Rust 的模式匹配是**窮舉式（exhaustive）**的，編譯器確保所有可能的情況都被處理。

```rust
// ======== 基本 match 表達式 ========
enum Direction {
    North,
    South,
    East,
    West,
}

fn describe_direction(dir: Direction) -> &'static str {
    match dir {
        Direction::North => "向北",
        Direction::South => "向南",
        Direction::East  => "向東",
        Direction::West  => "向西",
        // 必須窮舉所有變體，否則編譯錯誤
    }
}

// ======== 帶值的 Enum 匹配 ========
enum Message {
    Quit,
    Echo(String),
    Move { x: i32, y: i32 },
    Color(u8, u8, u8),
}

fn process_message(msg: Message) {
    match msg {
        Message::Quit => println!("退出"),
        Message::Echo(text) => println!("回聲: {}", text),
        Message::Move { x, y } => println!("移動到 ({}, {})", x, y),
        Message::Color(r, g, b) => println!("顏色: ({}, {}, {})", r, g, b),
    }
}

// ======== if let 語法糖 ========
fn main() {
    let some_value: Option<i32> = Some(42);

    // 只關心一種情況時使用 if let
    if let Some(value) = some_value {
        println!("值為: {}", value);
    }

    // match guard（匹配守衛）
    let num = 4;
    match num {
        n if n < 0 => println!("負數"),
        0 => println!("零"),
        n if n % 2 == 0 => println!("正偶數: {}", n),
        n => println!("正奇數: {}", n),
    }

    // 解構 Tuple
    let point = (3, -5);
    match point {
        (0, 0) => println!("原點"),
        (x, 0) => println!("x 軸上, x={}", x),
        (0, y) => println!("y 軸上, y={}", y),
        (x, y) => println!("座標 ({}, {})", x, y),
    }
}
```

### 2.7 Traits

Trait 定義了一組行為（方法簽名），類似於 Java 的 Interface 或 Haskell 的 Type Class。

```rust
/// 定義 Summary trait
trait Summary {
    /// 必須實作的方法
    fn summarize(&self) -> String;

    /// 有預設實作的方法
    fn preview(&self) -> String {
        format!("（閱讀更多 {}...）", self.summarize())
    }
}

/// 新聞文章
struct NewsArticle {
    title: String,
    author: String,
    content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {}", self.title, self.author)
    }
}

/// 推文
struct Tweet {
    username: String,
    content: String,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }

    fn preview(&self) -> String {
        format!("@{} 的推文", self.username)
    }
}

// Trait Bound 語法
fn notify(item: &impl Summary) {
    println!("快訊！{}", item.summarize());
}

// 等同於泛型語法
fn notify_generic<T: Summary>(item: &T) {
    println!("快訊！{}", item.summarize());
}

// 多重 Trait Bound
fn notify_display(item: &(impl Summary + std::fmt::Display)) {
    println!("{}", item);
}

// where 子句（複雜的 Trait Bound）
fn some_function<T, U>(t: &T, u: &U) -> String
where
    T: Summary + Clone,
    U: std::fmt::Display + std::fmt::Debug,
{
    format!("{} - {:?}", t.summarize(), u)
}

fn main() {
    let article = NewsArticle {
        title: String::from("Rust 2024 Edition 發布"),
        author: String::from("Rust Team"),
        content: String::from("..."),
    };
    notify(&article);
    println!("{}", article.preview());
}
```

### 2.8 Generics

```rust
// ======== 泛型函式 ========
fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// ======== 泛型結構體 ========
#[derive(Debug)]
struct Point<T> {
    x: T,
    y: T,
}

impl<T: std::fmt::Display> Point<T> {
    fn display(&self) {
        println!("Point({}, {})", self.x, self.y);
    }
}

// 不同型別的 Point
#[derive(Debug)]
struct MixedPoint<T, U> {
    x: T,
    y: U,
}

impl<T, U> MixedPoint<T, U> {
    fn mixup<V, W>(self, other: MixedPoint<V, W>) -> MixedPoint<T, W> {
        MixedPoint {
            x: self.x,
            y: other.y,
        }
    }
}

// ======== 泛型列舉 ========
// 標準庫的 Result 和 Option 就是泛型列舉
enum MyResult<T, E> {
    Ok(T),
    Err(E),
}

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    println!("最大值: {}", largest(&numbers));

    let chars = vec!['y', 'm', 'a', 'q'];
    println!("最大字元: {}", largest(&chars));

    let int_point = Point { x: 5, y: 10 };
    let float_point = Point { x: 1.0, y: 4.0 };
    int_point.display();
    float_point.display();

    let p1 = MixedPoint { x: 5, y: 10.4 };
    let p2 = MixedPoint { x: "Hello", y: 'c' };
    let p3 = p1.mixup(p2);
    println!("p3: ({}, {})", p3.x, p3.y); // p3: (5, c)
}
```

> 💡 **效能提示**：Rust 的泛型使用**單態化（Monomorphization）**策略，在編譯期為每個具體型別產生專門的程式碼，因此泛型不會有任何執行期開銷。

### 2.9 Async/Await

Rust 的非同步程式設計基於**零成本 Future**與 **async/await** 語法。

```rust
use tokio::time::{sleep, Duration};

// async fn 回傳一個 Future
async fn fetch_data(url: &str) -> Result<String, reqwest::Error> {
    let response = reqwest::get(url).await?;
    let body = response.text().await?;
    Ok(body)
}

// 並行執行多個非同步任務
async fn fetch_all() {
    let (result1, result2) = tokio::join!(
        fetch_data("https://api.example.com/users"),
        fetch_data("https://api.example.com/orders"),
    );

    match (result1, result2) {
        (Ok(users), Ok(orders)) => {
            println!("使用者: {} bytes", users.len());
            println!("訂單: {} bytes", orders.len());
        }
        _ => eprintln!("部分請求失敗"),
    }
}

// Tokio 非同步主函式
#[tokio::main]
async fn main() {
    // 產生非同步任務
    let handle = tokio::spawn(async {
        sleep(Duration::from_secs(1)).await;
        println!("任務完成！");
        42
    });

    let result = handle.await.unwrap();
    println!("結果: {}", result);
}
```

```mermaid
sequenceDiagram
    participant M as Main Thread
    participant R as Tokio Runtime
    participant T1 as Task 1
    participant T2 as Task 2

    M->>R: tokio::spawn(task1)
    M->>R: tokio::spawn(task2)
    R->>T1: 執行至 .await
    T1-->>R: 讓出控制權（Yield）
    R->>T2: 切換到 task2
    T2-->>R: 讓出控制權（Yield）
    R->>T1: task1 就緒，恢復執行
    T1->>R: 完成
    R->>T2: task2 就緒，恢復執行
    T2->>R: 完成
    R->>M: 所有任務完成
```

### 2.10 Memory Safety

Rust 在**編譯期**就消除了以下常見的記憶體安全問題：

| 問題類型 | C/C++ 表現 | Rust 的保護機制 |
|---------|-----------|---------------|
| Use-After-Free | 存取已釋放的記憶體 → 未定義行為 | Ownership 系統禁止 |
| Double Free | 多次釋放同一記憶體 → 程式崩潰 | 單一所有者規則 |
| Buffer Overflow | 超出陣列邊界 → 安全漏洞 | 執行期邊界檢查 |
| Null Pointer Deref | 存取 null 指標 → Segfault | 無 null（使用 `Option<T>`） |
| Dangling Pointer | 引用已失效的指標 | 生命週期檢查 |
| Data Race | 多執行緒同時讀寫 → 未定義行為 | Send/Sync Trait 約束 |

```rust
fn main() {
    // ======== Null Safety ========
    // Rust 沒有 null，使用 Option<T>
    let value: Option<i32> = Some(42);
    match value {
        Some(v) => println!("值: {}", v),
        None => println!("沒有值"),
    }

    // 安全的解包方式
    let safe_value = value.unwrap_or(0);        // 提供預設值
    let mapped = value.map(|v| v * 2);          // 轉換
    let chained = value.and_then(|v| {          // 鏈式操作
        if v > 0 { Some(v) } else { None }
    });

    // ======== 邊界檢查 ========
    let v = vec![1, 2, 3];
    // v[10]; // ❌ 執行期 panic: index out of bounds
    let safe = v.get(10); // ✅ 回傳 Option<&i32>，超出邊界回傳 None
}
```

### 2.11 Concurrency Safety

Rust 透過 **`Send`** 和 **`Sync`** 兩個 marker trait 在編譯期保證並發安全。

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Arc：原子引用計數（跨執行緒共享）
    // Mutex：互斥鎖（保護共享資料）
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("計數器: {}", *counter.lock().unwrap()); // 10
}
```

**Send 與 Sync Trait：**

| Trait | 意義 | 範例 |
|-------|------|------|
| `Send` | 型別的值可以安全地在執行緒之間**傳送** | 大多數型別都是 `Send` |
| `Sync` | 型別的引用可以安全地在執行緒之間**共享** | `&T` 是 `Sync` 若 `T` 是 `Sync` |
| `!Send` | 不能跨執行緒傳送 | `Rc<T>`（非原子引用計數） |
| `!Sync` | 不能跨執行緒共享 | `Cell<T>`、`RefCell<T>` |

```rust
use std::rc::Rc;
use std::sync::Arc;

fn main() {
    // Rc 不是 Send，不能跨執行緒
    let rc = Rc::new(42);
    // thread::spawn(move || {
    //     println!("{}", rc); // ❌ 編譯錯誤：Rc<i32> 不是 Send
    // });

    // Arc 是 Send + Sync，可以安全跨執行緒
    let arc = Arc::new(42);
    let arc_clone = Arc::clone(&arc);
    thread::spawn(move || {
        println!("{}", arc_clone); // ✅
    });
}
```

> ⚠️ **企業實務注意**：在多執行緒程式碼中，優先使用 `Arc<Mutex<T>>` 或 `Arc<RwLock<T>>` 來保護共享狀態。對於高效能場景，考慮使用 `crossbeam` 或 `parking_lot` 提供的無鎖或更高效能的同步原語。

---

---

## 3. 開發環境安裝

### 3.1 Windows 環境安裝

#### 方式一：使用 rustup-init.exe（推薦）

```powershell
# 1. 下載並執行 rustup-init
# 前往 https://rustup.rs/ 下載 rustup-init.exe
# 或使用 winget
winget install Rustlang.Rustup

# 2. 安裝完成後驗證
rustc --version
cargo --version
rustup --version
```

#### MSVC Toolchain（推薦用於 Windows）

```powershell
# 安裝 Visual Studio Build Tools（必要）
# 前往 https://visualstudio.microsoft.com/visual-cpp-build-tools/
# 勾選「使用 C++ 的桌面開發」工作負載

# 設定預設 toolchain 為 MSVC
rustup default stable-x86_64-pc-windows-msvc

# 驗證
rustup show
```

#### GNU Toolchain（替代方案）

```powershell
# 安裝 MSYS2（https://www.msys2.org/）
# 在 MSYS2 中安裝 MinGW-w64
pacman -S mingw-w64-x86_64-gcc

# 設定 GNU toolchain
rustup default stable-x86_64-pc-windows-gnu
```

**⚠️ 企業建議**：Windows 環境優先使用 **MSVC Toolchain**，與 Visual Studio Build Tools 整合度最佳。

### 3.2 Linux 環境安裝

#### Ubuntu / Debian

```bash
# 安裝系統依賴
sudo apt update
sudo apt install -y build-essential curl pkg-config libssl-dev

# 使用 rustup 安裝 Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 載入環境變數
source "$HOME/.cargo/env"

# 驗證安裝
rustc --version
cargo --version
```

#### RHEL / Rocky Linux / CentOS

```bash
# 安裝系統依賴
sudo dnf groupinstall "Development Tools"
sudo dnf install -y openssl-devel curl

# 安裝 Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# 驗證
rustc --version
```

#### PATH 設定

```bash
# rustup 預設安裝到 ~/.cargo/bin
# 確保以下路徑在 PATH 中

# Bash（~/.bashrc 或 ~/.bash_profile）
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Zsh（~/.zshrc）
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Fish（~/.config/fish/config.fish）
set -gx PATH "$HOME/.cargo/bin" $PATH
```

### 3.3 macOS 環境安裝

#### Apple Silicon（M1/M2/M3/M4）

```bash
# 安裝 Xcode Command Line Tools
xcode-select --install

# 安裝 Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# 預設 target 為 aarch64-apple-darwin
rustup show
# Default host: aarch64-apple-darwin
```

#### Intel Mac

```bash
# 安裝方式相同
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# 預設 target 為 x86_64-apple-darwin
rustup show
```

#### 跨平台編譯（Cross Compilation）

```bash
# Apple Silicon 上編譯 Intel 版本
rustup target add x86_64-apple-darwin
cargo build --target x86_64-apple-darwin

# 編譯 Linux 版本（需要 cross-compilation 工具鏈）
rustup target add x86_64-unknown-linux-gnu
# 建議使用 cross 工具
cargo install cross
cross build --target x86_64-unknown-linux-gnu
```

### 3.4 VSCode 設定

**必裝擴充套件：**

| 擴充套件 | 說明 |
|---------|------|
| `rust-analyzer` | 官方 LSP 伺服器（必裝） |
| `CodeLLDB` | LLDB 除錯器 |
| `Even Better TOML` | TOML 語法高亮 |
| `Error Lens` | 行內錯誤提示 |
| `crates` | Cargo.toml 相依版本提示 |

**VSCode settings.json 建議設定：**

```json
{
    // rust-analyzer 設定
    "rust-analyzer.check.command": "clippy",
    "rust-analyzer.cargo.features": "all",
    "rust-analyzer.inlayHints.typeHints.enable": true,
    "rust-analyzer.inlayHints.parameterHints.enable": true,
    "rust-analyzer.lens.enable": true,
    "rust-analyzer.lens.run.enable": true,
    "rust-analyzer.lens.debug.enable": true,

    // 儲存時自動格式化
    "[rust]": {
        "editor.defaultFormatter": "rust-lang.rust-analyzer",
        "editor.formatOnSave": true,
        "editor.rulers": [100]
    },

    // 除錯設定
    "lldb.displayFormat": "auto",
    "lldb.showDisassembly": "never"
}
```

**launch.json 除錯設定：**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug executable",
            "cargo": {
                "args": ["build", "--bin=my-app", "--package=my-app"],
                "filter": {
                    "name": "my-app",
                    "kind": "bin"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests",
            "cargo": {
                "args": ["test", "--no-run", "--bin=my-app", "--package=my-app"],
                "filter": {
                    "name": "my-app",
                    "kind": "bin"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

### 3.5 IntelliJ Rust 設定

```
安裝步驟：
1. 安裝 IntelliJ IDEA（Community 或 Ultimate）
2. 前往 File → Settings → Plugins
3. 搜尋並安裝 "Rust" 外掛
4. 重啟 IDE
5. 設定 Toolchain：File → Settings → Languages & Frameworks → Rust
   - Toolchain location: ~/.cargo/bin（自動偵測）
   - Standard library: 自動下載
```

### 3.6 Toolchain 管理

```bash
# 查看已安裝的 toolchain
rustup show

# 更新所有 toolchain
rustup update

# 安裝特定版本
rustup install 1.95.0
rustup install nightly

# 設定全域預設
rustup default stable

# 設定專案級 toolchain（建立 rust-toolchain.toml）
cat > rust-toolchain.toml << 'EOF'
[toolchain]
channel = "stable"
components = ["rustfmt", "clippy", "rust-analyzer"]
targets = ["x86_64-unknown-linux-gnu", "x86_64-pc-windows-msvc"]
EOF

# 安裝元件
rustup component add rustfmt clippy rust-src rust-analyzer

# 安裝交叉編譯目標
rustup target add x86_64-unknown-linux-musl  # 靜態連結的 Linux
rustup target add wasm32-unknown-unknown       # WebAssembly
rustup target add aarch64-unknown-linux-gnu    # ARM64 Linux
```

### 3.7 nightly / stable / beta 差異

| 通道 | 發布頻率 | 穩定性 | 適用場景 |
|------|---------|--------|---------|
| **stable** | 每 6 週 | ✅ 最穩定 | 生產環境（推薦） |
| **beta** | 每 6 週（下一版 stable 候選） | ⚡ 較穩定 | 提前測試相容性 |
| **nightly** | 每天 | ⚠️ 可能不穩定 | 實驗性功能、部分 crate 需要 |

```bash
# 僅在特定專案使用 nightly
cd my-nightly-project
rustup override set nightly

# 或使用 rust-toolchain.toml（推薦）
# [toolchain]
# channel = "nightly-2026-05-01"

# 暫時使用 nightly 執行
cargo +nightly build
cargo +nightly fmt -- --check
```

> ⚠️ **企業規範**：生產環境專案**必須使用 stable 通道**。需要 nightly 功能的 crate 應在評估後謹慎引入，並在 `rust-toolchain.toml` 中固定 nightly 日期版本。

---

## 4. Cargo 完整教學

### 4.1 專案建立與初始化

```bash
# 建立新的 binary 專案（包含 main.rs）
cargo new my-app
# 建立的目錄結構：
# my-app/
# ├── Cargo.toml
# └── src/
#     └── main.rs

# 建立新的 library 專案（包含 lib.rs）
cargo new my-lib --lib
# my-lib/
# ├── Cargo.toml
# └── src/
#     └── lib.rs

# 在既有目錄中初始化
mkdir existing-project && cd existing-project
cargo init          # binary
cargo init --lib    # library

# 指定版本與名稱
cargo new my-app --edition 2024 --name custom-name
```

**企業級專案 Cargo.toml 範本：**

```toml
[package]
name = "enterprise-service"
version = "0.1.0"
edition = "2024"
authors = ["Backend Team <backend@company.com>"]
description = "企業級後端服務"
license = "MIT OR Apache-2.0"
repository = "https://github.com/company/enterprise-service"
readme = "README.md"
rust-version = "1.95"
keywords = ["api", "enterprise", "rest"]
categories = ["web-programming::http-server"]

[dependencies]
# Web 框架
axum = { version = "0.8", features = ["macros"] }
tower = "0.5"
tower-http = { version = "0.6", features = ["cors", "trace", "compression-gzip"] }

# 非同步執行時期
tokio = { version = "1", features = ["full"] }

# 序列化
serde = { version = "1", features = ["derive"] }
serde_json = "1"

# 資料庫
sqlx = { version = "0.8", features = [
    "runtime-tokio",
    "tls-rustls",
    "postgres",
    "uuid",
    "chrono",
    "migrate"
] }

# 日誌與追蹤
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter", "json"] }

# 安全
jsonwebtoken = "9"
argon2 = "0.5"

# 工具
uuid = { version = "1", features = ["v4", "serde"] }
chrono = { version = "0.4", features = ["serde"] }
dotenvy = "0.15"
thiserror = "2"
anyhow = "1"

[dev-dependencies]
criterion = { version = "0.5", features = ["html_reports"] }
mockall = "0.13"
tokio-test = "0.4"
wiremock = "0.6"
fake = { version = "3", features = ["derive"] }

[[bench]]
name = "api_benchmark"
harness = false

[profile.dev]
opt-level = 0
debug = true

[profile.release]
opt-level = 3
lto = "fat"
codegen-units = 1
strip = true
panic = "abort"

[profile.test]
opt-level = 1
```

### 4.2 建置與執行

```bash
# 開發模式建置（快速編譯，未最佳化）
cargo build

# 釋出模式建置（最佳化，較慢編譯）
cargo build --release

# 執行
cargo run
cargo run --release
cargo run -- --port 8080  # 傳遞參數給程式

# 檢查（只做型別檢查，不產生二進位）
cargo check

# 清理建置產物
cargo clean

# 指定 target
cargo build --target x86_64-unknown-linux-musl

# 查看編譯時間分析
cargo build --timings
```

**建置產物目錄：**

```
target/
├── debug/              # dev profile 產物
│   └── my-app          # 執行檔
├── release/            # release profile 產物
│   └── my-app          # 最佳化後的執行檔
└── .cargo-lock         # lock 檔
```

### 4.3 測試與文件

```bash
# 執行所有測試
cargo test

# 執行特定測試
cargo test test_name
cargo test module_name::

# 顯示 stdout 輸出
cargo test -- --show-output

# 執行忽略的測試
cargo test -- --ignored

# 只執行 doc tests
cargo test --doc

# 執行整合測試
cargo test --test integration_test

# 測試覆蓋率（需安裝 cargo-tarpaulin）
cargo install cargo-tarpaulin
cargo tarpaulin --out html

# 產生文件
cargo doc --open                    # 產生並開啟文件
cargo doc --no-deps                 # 不包含依賴的文件
cargo doc --document-private-items  # 包含私有項目
```

### 4.4 程式碼品質工具

```bash
# ======== rustfmt：程式碼格式化 ========
cargo fmt              # 格式化所有檔案
cargo fmt -- --check   # 檢查格式（CI 用）

# rustfmt.toml 設定檔
cat > rustfmt.toml << 'EOF'
max_width = 100
tab_spaces = 4
edition = "2024"
imports_granularity = "Module"
group_imports = "StdExternalCrate"
reorder_imports = true
use_field_init_shorthand = true
EOF

# ======== clippy：靜態分析 ========
cargo clippy                              # 執行 clippy
cargo clippy -- -W clippy::all            # 啟用所有警告
cargo clippy -- -D warnings               # 將警告視為錯誤（CI 用）
cargo clippy --fix                        # 自動修正

# clippy 設定（Cargo.toml 或 clippy.toml）
# [lints.clippy]
# pedantic = "warn"
# unwrap_used = "deny"
# expect_used = "warn"
```

### 4.5 安全性稽核

```bash
# 安裝 cargo-audit
cargo install cargo-audit

# 掃描已知漏洞
cargo audit

# 產生 JSON 報告
cargo audit --json > audit-report.json

# 安裝 cargo-deny（更全面的檢查）
cargo install cargo-deny

# 初始化設定
cargo deny init

# 執行完整檢查
cargo deny check              # 檢查所有規則
cargo deny check licenses     # 檢查授權
cargo deny check bans         # 檢查禁用的 crate
cargo deny check advisories   # 檢查安全公告
cargo deny check sources      # 檢查來源
```

**deny.toml 企業級設定範例：**

```toml
[advisories]
vulnerability = "deny"
unmaintained = "warn"
yanked = "deny"

[licenses]
allow = ["MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"]
deny = ["GPL-3.0"]
copyleft = "deny"
unlicensed = "deny"

[bans]
multiple-versions = "warn"
wildcards = "deny"

[[bans.deny]]
name = "openssl"         # 禁用 openssl，改用 rustls
wrappers = ["openssl-sys"]
```

### 4.6 發佈與套件管理

```bash
# 登入 crates.io（需要 API Token）
cargo login

# 打包（不發佈，用於檢查）
cargo package

# 發佈到 crates.io
cargo publish

# 發佈到私有 Registry
cargo publish --registry my-private-registry

# 使用私有 Registry（.cargo/config.toml）
cat > .cargo/config.toml << 'EOF'
[registries.company]
index = "https://registry.company.com/index"

[registry]
default = "company"
EOF
```

### 4.7 Workspace 管理

Workspace 允許在一個倉庫中管理多個相關的 crate。

```toml
# 根目錄 Cargo.toml（Workspace 定義）
[workspace]
resolver = "2"
members = [
    "crates/api",
    "crates/core",
    "crates/domain",
    "crates/infrastructure",
    "crates/shared",
]

# 統一管理依賴版本
[workspace.dependencies]
serde = { version = "1", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
sqlx = { version = "0.8", features = ["runtime-tokio", "postgres"] }
tracing = "0.1"
thiserror = "2"
uuid = { version = "1", features = ["v4", "serde"] }

[workspace.package]
edition = "2024"
authors = ["Backend Team <backend@company.com>"]
license = "MIT"
rust-version = "1.95"
```

```toml
# crates/api/Cargo.toml（成員 crate）
[package]
name = "api"
version = "0.1.0"
edition.workspace = true
authors.workspace = true
license.workspace = true

[dependencies]
serde.workspace = true       # 使用 workspace 定義的版本
tokio.workspace = true
core = { path = "../core" }  # 引用同 workspace 的 crate
domain = { path = "../domain" }
```

**Workspace 目錄結構：**

```
enterprise-service/
├── Cargo.toml              # workspace 定義
├── Cargo.lock              # 統一的 lock 檔
├── crates/
│   ├── api/                # HTTP API 層
│   │   ├── Cargo.toml
│   │   └── src/
│   ├── core/               # 核心業務邏輯
│   │   ├── Cargo.toml
│   │   └── src/
│   ├── domain/             # 領域模型
│   │   ├── Cargo.toml
│   │   └── src/
│   ├── infrastructure/     # 基礎設施（DB、快取）
│   │   ├── Cargo.toml
│   │   └── src/
│   └── shared/             # 共享工具
│       ├── Cargo.toml
│       └── src/
├── tests/                  # 整合測試
├── benches/                # 效能測試
└── docs/                   # 文件
```

```bash
# Workspace 操作指令
cargo build -p api                    # 只建置 api crate
cargo test -p core                    # 只測試 core crate
cargo test --workspace                # 測試所有 crate
cargo clippy --workspace              # 檢查所有 crate
cargo fmt --all                       # 格式化所有 crate
```

### 4.8 相依性管理與語意版本

```mermaid
graph LR
    SV["語意版本 X.Y.Z"] --> MAJOR["X（主版本）<br/>不相容的 API 變更"]
    SV --> MINOR["Y（次版本）<br/>向後相容的功能新增"]
    SV --> PATCH["Z（修補版本）<br/>向後相容的錯誤修正"]
```

**版本指定語法：**

| 語法 | 範圍 | 說明 |
|------|------|------|
| `"1.2.3"` | `>=1.2.3, <2.0.0` | 預設（Caret） |
| `"~1.2.3"` | `>=1.2.3, <1.3.0` | Tilde（只允許 patch 更新） |
| `"1.2.*"` | `>=1.2.0, <1.3.0` | 萬用字元 |
| `">=1.2, <1.5"` | 指定範圍 | 精確範圍 |
| `"=1.2.3"` | 僅 `1.2.3` | 精確版本 |

```bash
# 更新依賴（在 Cargo.toml 允許的範圍內）
cargo update

# 更新特定 crate
cargo update -p serde

# 查看可用更新（需安裝 cargo-outdated）
cargo install cargo-outdated
cargo outdated

# 查看依賴樹
cargo tree
cargo tree -d              # 只顯示重複的依賴
cargo tree -e features     # 顯示啟用的 features
cargo tree -i sqlx         # 反向查詢（誰依賴 sqlx）
```

> 💡 **企業實務**：務必將 `Cargo.lock` 加入版本控制（binary crate），確保所有開發者和 CI/CD 使用完全相同的依賴版本。Library crate 不需要 commit `Cargo.lock`。

---

## 5. Rust 基礎語法

### 5.1 變數與可變性

```rust
fn main() {
    // ======== 不可變變數（預設）========
    let x = 5;
    // x = 6; // ❌ 編譯錯誤：cannot assign twice to immutable variable

    // ======== 可變變數 ========
    let mut y = 5;
    println!("y = {}", y);
    y = 6; // ✅
    println!("y = {}", y);

    // ======== 遮蔽（Shadowing）========
    let z = 5;
    let z = z + 1;        // 新的 z，遮蔽了前一個
    let z = z * 2;
    println!("z = {}", z); // 12

    // Shadowing 可以改變型別
    let spaces = "   ";          // &str
    let spaces = spaces.len();   // usize（不同型別）
    println!("spaces = {}", spaces);

    // ======== 常數 ========
    const MAX_CONNECTIONS: u32 = 10_000;
    const API_TIMEOUT_SECS: u64 = 30;
    println!("最大連線數: {}", MAX_CONNECTIONS);

    // ======== 型別推斷 ========
    let guess: u32 = "42".parse().expect("Not a number");
    let inferred = 42_i64; // 型別後綴
    let big_number = 1_000_000; // 數值分隔符
    let hex = 0xff;
    let octal = 0o77;
    let binary = 0b1111_0000;
    let byte = b'A'; // u8
}
```

### 5.2 資料型別

```rust
fn main() {
    // ======== 純量型別（Scalar Types）========

    // 整數
    let i8_val: i8 = -128;         // -128 ~ 127
    let u8_val: u8 = 255;          // 0 ~ 255
    let i16_val: i16 = -32_768;
    let i32_val: i32 = 2_147_483_647;
    let i64_val: i64 = 9_223_372_036_854_775_807;
    let i128_val: i128 = 170_141_183_460_469_231_731_687_303_715_884_105_727;
    let isize_val: isize = 42; // 平台相關（32 或 64 位元）
    let usize_val: usize = 42;

    // 浮點數
    let f32_val: f32 = 3.14;
    let f64_val: f64 = 2.718_281_828_459_045; // 預設型別

    // 布林
    let is_active: bool = true;

    // 字元（Unicode，4 bytes）
    let ch: char = '中';
    let emoji: char = '🦀';

    // ======== 複合型別（Compound Types）========

    // Tuple（固定長度，不同型別）
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;           // 解構
    let first = tup.0;             // 索引存取
    let unit: () = ();             // Unit Tuple

    // Array（固定長度，相同型別）
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    let first = arr[0];
    let zeros = [0; 5];            // [0, 0, 0, 0, 0]

    // Slice（動態長度的參考）
    let slice: &[i32] = &arr[1..3]; // [2, 3]

    // String 與 &str
    let s1: String = String::from("hello");   // 堆積配置，可變
    let s2: &str = "hello";                   // 字串切片，不可變
    let s3: String = format!("{} world", s1); // 格式化
}
```

**型別大小速查表：**

| 型別 | 大小（bytes） | 範圍 |
|------|-------------|------|
| `i8` / `u8` | 1 | -128~127 / 0~255 |
| `i16` / `u16` | 2 | -32768~32767 / 0~65535 |
| `i32` / `u32` | 4 | ±21 億 / 0~42 億 |
| `i64` / `u64` | 8 | ±9.2×10¹⁸ |
| `i128` / `u128` | 16 | ±1.7×10³⁸ |
| `isize` / `usize` | 4 或 8 | 取決於平台 |
| `f32` | 4 | ~6-7 位有效數字 |
| `f64` | 8 | ~15-17 位有效數字 |
| `bool` | 1 | true / false |
| `char` | 4 | Unicode 碼位 |

### 5.3 函式

```rust
/// 基本函式
fn add(a: i32, b: i32) -> i32 {
    a + b // 最後一個表達式為回傳值（不加分號）
}

/// 使用 return 提前回傳
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        return Err("除以零".to_string());
    }
    Ok(a / b)
}

/// 多回傳值（使用 Tuple）
fn swap(a: i32, b: i32) -> (i32, i32) {
    (b, a)
}

/// 泛型函式
fn first<T>(list: &[T]) -> Option<&T> {
    list.first()
}

/// 接受閉包的函式
fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(x)
}

/// 方法（定義在 impl 區塊中）
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    /// 關聯函式（類似靜態方法）
    fn new(width: f64, height: f64) -> Self {
        Self { width, height }
    }

    /// 方法（接受 &self）
    fn area(&self) -> f64 {
        self.width * self.height
    }

    /// 可變方法（接受 &mut self）
    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }

    /// 消耗自身的方法（接受 self）
    fn into_square(self) -> Rectangle {
        let side = (self.width + self.height) / 2.0;
        Rectangle::new(side, side)
    }
}

fn main() {
    println!("{}", add(3, 5));
    println!("{:?}", divide(10.0, 3.0));
    println!("{:?}", swap(1, 2));

    let mut rect = Rectangle::new(10.0, 20.0);
    println!("面積: {}", rect.area());
    rect.scale(2.0);
    println!("縮放後面積: {}", rect.area());
}
```

### 5.4 控制流程

```rust
fn main() {
    let number = 7;

    // ======== if / else if / else ========
    if number < 5 {
        println!("小於 5");
    } else if number < 10 {
        println!("介於 5 和 10 之間");
    } else {
        println!("大於等於 10");
    }

    // if 作為表達式
    let condition = true;
    let value = if condition { 5 } else { 6 };

    // ======== match ========
    let grade = 85;
    let level = match grade {
        90..=100 => "優秀",
        80..=89  => "良好",
        70..=79  => "中等",
        60..=69  => "及格",
        _        => "不及格",
    };
    println!("等級: {}", level);

    // ======== if let ========
    let config_value: Option<u32> = Some(3);
    if let Some(val) = config_value {
        println!("設定值: {}", val);
    }

    // ======== let else（Rust 1.65+）========
    let Some(count) = config_value else {
        println!("沒有設定值");
        return;
    };
    println!("計數: {}", count);
}
```

### 5.5 迴圈

```rust
fn main() {
    // ======== loop（無限迴圈）========
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2; // loop 可以回傳值
        }
    };
    println!("result = {}", result); // 20

    // 標記迴圈（用於巢狀迴圈）
    'outer: for i in 0..5 {
        for j in 0..5 {
            if i + j > 5 {
                break 'outer; // 跳出外層迴圈
            }
            println!("({}, {})", i, j);
        }
    }

    // ======== while ========
    let mut n = 3;
    while n != 0 {
        println!("{}!", n);
        n -= 1;
    }
    println!("發射！");

    // ======== while let ========
    let mut stack = vec![1, 2, 3];
    while let Some(top) = stack.pop() {
        println!("{}", top);
    }

    // ======== for ========
    // Range
    for i in 0..5 {
        print!("{} ", i); // 0 1 2 3 4
    }
    println!();

    for i in 0..=5 {
        print!("{} ", i); // 0 1 2 3 4 5（包含結尾）
    }
    println!();

    // 迭代集合
    let names = vec!["Alice", "Bob", "Charlie"];
    for name in &names {
        println!("Hello, {}!", name);
    }

    // 帶索引的迭代
    for (i, name) in names.iter().enumerate() {
        println!("{}: {}", i, name);
    }
}
```

### 5.6 結構體（Struct）

```rust
// ======== 一般結構體 ========
#[derive(Debug, Clone)]
struct User {
    id: u64,
    username: String,
    email: String,
    active: bool,
}

impl User {
    /// 建構函式
    fn new(id: u64, username: String, email: String) -> Self {
        Self {
            id,
            username,
            email,
            active: true, // 預設值
        }
    }

    /// 建造者模式（Builder Pattern）
    fn with_active(mut self, active: bool) -> Self {
        self.active = active;
        self
    }

    fn display_info(&self) {
        println!("使用者 {}: {} <{}>", self.id, self.username, self.email);
    }
}

// ======== Tuple Struct ========
struct Color(u8, u8, u8);
struct Point(f64, f64, f64);

// ======== Unit Struct ========
struct Marker;

// ======== 結構體更新語法 ========
fn main() {
    let user1 = User::new(1, "alice".into(), "alice@example.com".into());

    // 使用 ..user1 複製其餘欄位
    let user2 = User {
        id: 2,
        username: "bob".into(),
        ..user1.clone()
    };

    user1.display_info();
    user2.display_info();

    // Tuple struct
    let red = Color(255, 0, 0);
    println!("Red: ({}, {}, {})", red.0, red.1, red.2);

    // 解構
    let User { username, email, .. } = &user1;
    println!("{} - {}", username, email);
}
```

### 5.7 列舉（Enum）

```rust
/// 簡單列舉
#[derive(Debug)]
enum HttpStatus {
    Ok = 200,
    NotFound = 404,
    InternalServerError = 500,
}

/// 帶資料的列舉（Algebraic Data Type）
#[derive(Debug)]
enum ApiResponse {
    Success { data: String, status: u16 },
    Error { message: String, code: u16 },
    Loading,
    Redirect(String), // Tuple 變體
}

impl ApiResponse {
    fn is_success(&self) -> bool {
        matches!(self, ApiResponse::Success { .. })
    }

    fn status_code(&self) -> u16 {
        match self {
            ApiResponse::Success { status, .. } => *status,
            ApiResponse::Error { code, .. } => *code,
            ApiResponse::Loading => 0,
            ApiResponse::Redirect(_) => 302,
        }
    }
}

/// 使用 Option<T> 表示可能不存在的值
fn find_user(id: u64) -> Option<String> {
    match id {
        1 => Some("Alice".to_string()),
        2 => Some("Bob".to_string()),
        _ => None,
    }
}

/// 使用 Result<T, E> 表示可能失敗的操作
fn parse_config(input: &str) -> Result<u32, String> {
    input.parse::<u32>().map_err(|e| format!("解析失敗: {}", e))
}

fn main() {
    let response = ApiResponse::Success {
        data: "OK".into(),
        status: 200,
    };
    println!("{:?}, code: {}", response, response.status_code());

    // Option 的常用方法
    let user = find_user(1);
    let name = user.unwrap_or("未知".to_string());
    let mapped = find_user(2).map(|n| n.to_uppercase());
    println!("{}, {:?}", name, mapped);

    // Result 的處理
    match parse_config("42") {
        Ok(val) => println!("設定值: {}", val),
        Err(e) => eprintln!("錯誤: {}", e),
    }
}
```

### 5.8 模組系統

```rust
// ======== 模組宣告（同一檔案）========
mod authentication {
    /// 模組內的公開結構體
    pub struct Credentials {
        pub username: String,
        password: String, // 私有欄位
    }

    impl Credentials {
        pub fn new(username: String, password: String) -> Self {
            Self { username, password }
        }

        pub fn validate(&self) -> bool {
            !self.username.is_empty() && self.password.len() >= 8
        }
    }

    /// 子模組
    pub mod jwt {
        pub fn generate_token(username: &str) -> String {
            format!("token_for_{}", username)
        }
    }
}

// ======== 使用模組 ========
use authentication::Credentials;
use authentication::jwt;

fn main() {
    let creds = Credentials::new("admin".into(), "secure_password".into());
    if creds.validate() {
        let token = jwt::generate_token(&creds.username);
        println!("Token: {}", token);
    }
}
```

**多檔案模組結構：**

```
src/
├── main.rs
├── lib.rs          # crate root
├── config.rs       # mod config
├── routes/
│   ├── mod.rs      # mod routes（聲明子模組）
│   ├── users.rs    # routes::users
│   └── health.rs   # routes::health
├── services/
│   ├── mod.rs
│   └── user_service.rs
└── models/
    ├── mod.rs
    └── user.rs
```

```rust
// src/lib.rs
pub mod config;
pub mod routes;
pub mod services;
pub mod models;

// src/routes/mod.rs
pub mod users;
pub mod health;

// src/routes/users.rs
use crate::services::user_service::UserService;

pub async fn get_users() {
    // ...
}
```

### 5.9 錯誤處理（Result / Option）

```rust
use std::fs;
use std::io;
use std::num::ParseIntError;

// ======== 自定義錯誤型別（使用 thiserror）========
#[derive(Debug, thiserror::Error)]
enum AppError {
    #[error("資料庫錯誤: {0}")]
    Database(#[from] sqlx::Error),

    #[error("找不到資源: {0}")]
    NotFound(String),

    #[error("驗證失敗: {0}")]
    Validation(String),

    #[error("未授權")]
    Unauthorized,

    #[error("IO 錯誤: {0}")]
    Io(#[from] io::Error),

    #[error("解析錯誤: {0}")]
    Parse(#[from] ParseIntError),
}

// ======== ? 運算子（錯誤傳播）========
fn read_and_parse(path: &str) -> Result<u32, AppError> {
    let content = fs::read_to_string(path)?;  // io::Error → AppError::Io
    let number: u32 = content.trim().parse()?; // ParseIntError → AppError::Parse
    Ok(number)
}

// ======== 多種錯誤處理方式 ========
fn main() {
    // 方式 1：match
    match read_and_parse("config.txt") {
        Ok(value) => println!("值: {}", value),
        Err(AppError::NotFound(msg)) => eprintln!("未找到: {}", msg),
        Err(e) => eprintln!("其他錯誤: {}", e),
    }

    // 方式 2：unwrap_or / unwrap_or_else
    let value = read_and_parse("config.txt").unwrap_or(0);

    // 方式 3：if let
    if let Ok(value) = read_and_parse("config.txt") {
        println!("值: {}", value);
    }

    // 方式 4：map / and_then 鏈式操作
    let result = read_and_parse("config.txt")
        .map(|v| v * 2)
        .unwrap_or_default();

    // 方式 5：使用 anyhow（適合應用程式）
    // fn main() -> anyhow::Result<()> {
    //     let value = read_and_parse("config.txt")
    //         .context("讀取設定檔失敗")?;
    //     Ok(())
    // }
}
```

> ⚠️ **企業規範**：
> - **Library crate**：使用 `thiserror` 定義結構化的錯誤型別
> - **Application（binary crate）**：使用 `anyhow` 簡化錯誤處理
> - **禁止在生產程式碼中使用 `unwrap()` 和 `expect()`**（CI 中用 clippy 強制）

### 5.10 集合（Collections）

```rust
use std::collections::HashMap;

fn main() {
    // ======== Vec<T>（動態陣列）========
    let mut numbers: Vec<i32> = Vec::new();
    numbers.push(1);
    numbers.push(2);
    numbers.push(3);

    // 使用巨集初始化
    let mut fruits = vec!["apple", "banana", "cherry"];
    fruits.push("date");

    // 存取元素
    let first = &numbers[0];           // 可能 panic
    let second = numbers.get(1);       // 回傳 Option<&i32>

    // 迭代
    for num in &numbers {
        print!("{} ", num);
    }
    println!();

    // 可變迭代
    for num in &mut numbers {
        *num *= 2;
    }

    // 函式式操作
    let doubled: Vec<i32> = numbers.iter().map(|&x| x * 2).collect();
    let evens: Vec<&i32> = numbers.iter().filter(|&&x| x % 2 == 0).collect();

    // ======== HashMap<K, V>（雜湊表）========
    let mut scores: HashMap<String, i32> = HashMap::new();
    scores.insert("Alice".to_string(), 95);
    scores.insert("Bob".to_string(), 87);

    // 取值
    let alice_score = scores.get("Alice"); // Option<&i32>

    // entry API（不存在時插入）
    scores.entry("Charlie".to_string()).or_insert(0);

    // 更新計數器模式
    let text = "hello world hello rust";
    let mut word_count: HashMap<&str, i32> = HashMap::new();
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);
        *count += 1;
    }
    println!("{:?}", word_count);

    // 迭代
    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }

    // ======== 其他集合 ========
    // HashSet：不重複集合
    use std::collections::HashSet;
    let mut set: HashSet<i32> = HashSet::new();
    set.insert(1);
    set.insert(2);
    set.insert(1); // 重複，不會插入
    println!("集合大小: {}", set.len()); // 2

    // BTreeMap：有序的 Map
    use std::collections::BTreeMap;
    let mut ordered: BTreeMap<&str, i32> = BTreeMap::new();
    ordered.insert("c", 3);
    ordered.insert("a", 1);
    ordered.insert("b", 2);
    // 迭代時按 key 排序
    for (k, v) in &ordered {
        println!("{}: {}", k, v); // a:1, b:2, c:3
    }

    // VecDeque：雙端佇列
    use std::collections::VecDeque;
    let mut deque: VecDeque<i32> = VecDeque::new();
    deque.push_back(1);
    deque.push_front(0);
    println!("{:?}", deque); // [0, 1]
}
```

### 5.11 迭代器（Iterators）

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // ======== 基本迭代器方法 ========

    // map：轉換
    let squared: Vec<i32> = numbers.iter().map(|&x| x * x).collect();

    // filter：過濾
    let evens: Vec<&i32> = numbers.iter().filter(|&&x| x % 2 == 0).collect();

    // filter_map：過濾 + 轉換
    let parsed: Vec<i32> = vec!["1", "two", "3", "four", "5"]
        .iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    // fold：摺疊（reduce）
    let sum: i32 = numbers.iter().fold(0, |acc, &x| acc + x);

    // 簡化版 sum
    let total: i32 = numbers.iter().sum();

    // ======== 進階迭代器方法 ========

    // chain：串接兩個迭代器
    let a = vec![1, 2, 3];
    let b = vec![4, 5, 6];
    let combined: Vec<&i32> = a.iter().chain(b.iter()).collect();

    // zip：配對
    let names = vec!["Alice", "Bob", "Charlie"];
    let scores = vec![95, 87, 92];
    let paired: Vec<(&&str, &i32)> = names.iter().zip(scores.iter()).collect();

    // enumerate：帶索引
    for (i, &num) in numbers.iter().enumerate() {
        if i >= 3 { break; }
        println!("[{}] = {}", i, num);
    }

    // take / skip
    let first_three: Vec<&i32> = numbers.iter().take(3).collect();
    let skip_five: Vec<&i32> = numbers.iter().skip(5).collect();

    // any / all
    let has_even = numbers.iter().any(|&x| x % 2 == 0);     // true
    let all_positive = numbers.iter().all(|&x| x > 0);       // true

    // find
    let first_even = numbers.iter().find(|&&x| x % 2 == 0);  // Some(&2)

    // flatten
    let nested = vec![vec![1, 2], vec![3, 4], vec![5]];
    let flat: Vec<&i32> = nested.iter().flatten().collect();

    // ======== 自定義迭代器 ========
    println!("{:?}", squared);
    println!("sum = {}", sum);
}

/// 自定義迭代器：費波那契數列
struct Fibonacci {
    a: u64,
    b: u64,
}

impl Fibonacci {
    fn new() -> Self {
        Self { a: 0, b: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let result = self.a;
        let new_b = self.a + self.b;
        self.a = self.b;
        self.b = new_b;
        Some(result)
    }
}

// 使用自定義迭代器
fn fibonacci_example() {
    let fib_10: Vec<u64> = Fibonacci::new().take(10).collect();
    println!("前 10 個費波那契數: {:?}", fib_10);
    // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
}
```

### 5.12 閉包（Closures）

```rust
fn main() {
    // ======== 閉包語法 ========
    let add = |a: i32, b: i32| -> i32 { a + b };
    let add_short = |a, b| a + b; // 型別可推斷

    println!("{}", add(3, 5));

    // ======== 捕獲環境變數 ========

    // 不可變借用（Fn）
    let name = String::from("Rust");
    let greet = || println!("Hello, {}!", name); // 借用 name
    greet();
    println!("{}", name); // ✅ name 仍可用

    // 可變借用（FnMut）
    let mut count = 0;
    let mut increment = || {
        count += 1; // 可變借用 count
        println!("count = {}", count);
    };
    increment();
    increment();

    // 取得所有權（FnOnce）
    let name = String::from("Rust");
    let consume = move || {
        println!("Consumed: {}", name); // 取得 name 的所有權
    };
    consume();
    // println!("{}", name); // ❌ name 已被移動

    // ======== 閉包作為參數 ========
    let numbers = vec![1, 2, 3, 4, 5];

    // 使用閉包做為 filter 的條件
    let threshold = 3;
    let filtered: Vec<&i32> = numbers
        .iter()
        .filter(|&&x| x > threshold)
        .collect();
    println!("大於 {}: {:?}", threshold, filtered);

    // ======== 閉包作為回傳值 ========
    let multiplier = make_multiplier(3);
    println!("5 * 3 = {}", multiplier(5));
}

/// 回傳閉包（使用 impl Fn）
fn make_multiplier(factor: i32) -> impl Fn(i32) -> i32 {
    move |x| x * factor
}

/// 接受不同閉包 Trait 的函式
fn apply_fn<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 { f(x) }
fn apply_fn_mut<F: FnMut()>(mut f: F) { f(); }
fn apply_fn_once<F: FnOnce() -> String>(f: F) -> String { f() }
```

**閉包 Trait 比較：**

| Trait | 捕獲方式 | 可呼叫次數 | 適用場景 |
|-------|---------|-----------|---------|
| `Fn` | 不可變借用 `&T` | 多次 | 唯讀存取 |
| `FnMut` | 可變借用 `&mut T` | 多次 | 需要修改狀態 |
| `FnOnce` | 取得所有權 `T` | 一次 | 消耗捕獲的值 |

> 💡 **實務建議**：函式參數中接受閉包時，盡量使用最寬鬆的 Trait Bound：`FnOnce` > `FnMut` > `Fn`。這樣呼叫者有最大的彈性。

---

## 6. Rust 進階教學

### 6.1 Traits 深入

```rust
// ======== Trait 定義與預設實作 ========
trait Repository<T> {
    fn find_by_id(&self, id: u64) -> Option<T>;
    fn find_all(&self) -> Vec<T>;
    fn save(&mut self, entity: T) -> Result<(), String>;
    fn delete(&mut self, id: u64) -> Result<(), String>;

    /// 預設實作
    fn count(&self) -> usize {
        self.find_all().len()
    }
}

// ======== Trait 繼承 ========
trait Auditable {
    fn created_at(&self) -> chrono::NaiveDateTime;
    fn updated_at(&self) -> chrono::NaiveDateTime;
}

trait AuditableRepository<T: Auditable>: Repository<T> {
    fn find_modified_after(&self, since: chrono::NaiveDateTime) -> Vec<T>;
}

// ======== Associated Types（關聯型別）========
trait Iterator {
    type Item;  // 關聯型別（每個實作只有一個具體型別）
    fn next(&mut self) -> Option<Self::Item>;
}

// 對比泛型 Trait：同一型別可實作多次
trait From<T> {
    fn from(value: T) -> Self;
}

// ======== Supertraits ========
use std::fmt;

trait Printable: fmt::Display + fmt::Debug {
    fn print(&self) {
        println!("{}", self); // 使用 Display
    }

    fn debug_print(&self) {
        println!("{:?}", self); // 使用 Debug
    }
}

// ======== Trait Object（動態分派）========
fn log_all(items: &[&dyn fmt::Display]) {
    for item in items {
        println!("{}", item);
    }
}

// ======== Blanket Implementation ========
// 為所有實作 Display 的型別自動實作 ToString
// （標準庫已有此實作）
// impl<T: fmt::Display> ToString for T { ... }
```

### 6.2 Lifetimes 深入

```rust
// ======== 多重生命週期 ========
fn first_word<'a>(s: &'a str) -> &'a str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    s
}

// ======== 不同生命週期參數 ========
fn longest_with_announcement<'a, 'b>(
    x: &'a str,
    y: &'a str,
    ann: &'b str,
) -> &'a str {
    println!("公告: {}", ann);
    if x.len() > y.len() { x } else { y }
}

// ======== 'static 生命週期 ========
// 存活整個程式執行期間
fn get_static_str() -> &'static str {
    "我是 static 字串"
}

// Trait bound 中的 'static
fn spawn_task<F>(f: F)
where
    F: FnOnce() + Send + 'static, // 必須 'static 才能送到其他執行緒
{
    std::thread::spawn(f);
}

// ======== 結構體中的生命週期 ========
#[derive(Debug)]
struct Config<'a> {
    name: &'a str,
    database_url: &'a str,
}

impl<'a> Config<'a> {
    fn new(name: &'a str, database_url: &'a str) -> Self {
        Self { name, database_url }
    }

    fn display(&self) -> String {
        format!("Config[{}]: {}", self.name, self.database_url)
    }
}

// ======== Higher-Rank Trait Bounds（HRTB）========
fn apply_to_str<F>(f: F) -> String
where
    F: for<'a> Fn(&'a str) -> &'a str, // 對所有生命週期 'a 都有效
{
    let s = String::from("hello world");
    f(&s).to_string()
}
```

### 6.3 Smart Pointers

```mermaid
graph TD
    SP["Smart Pointers"] --> BOX["Box&lt;T&gt;<br/>堆積配置"]
    SP --> RC["Rc&lt;T&gt;<br/>引用計數（單執行緒）"]
    SP --> ARC["Arc&lt;T&gt;<br/>原子引用計數（多執行緒）"]
    SP --> REF["RefCell&lt;T&gt;<br/>內部可變性"]
    SP --> COW["Cow&lt;T&gt;<br/>Copy-on-Write"]

    BOX --> B1["單一所有者"]
    BOX --> B2["固定大小"]

    RC --> R1["多所有者"]
    RC --> R2["!Send"]

    ARC --> A1["多所有者"]
    ARC --> A2["Send + Sync"]

    REF --> RF1["執行期借用檢查"]
    REF --> RF2["搭配 Rc 使用"]
```

```rust
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    // ======== Box<T>：堆積配置 ========
    let boxed = Box::new(42);
    println!("Box: {}", boxed);

    // 用於遞迴型別
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }
    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
    println!("{:?}", list);

    // ======== Rc<T>：引用計數（單執行緒）========
    let shared = Rc::new(String::from("共享資料"));
    let clone1 = Rc::clone(&shared); // 增加引用計數
    let clone2 = Rc::clone(&shared);
    println!("引用計數: {}", Rc::strong_count(&shared)); // 3
    println!("{}, {}, {}", shared, clone1, clone2);

    // ======== RefCell<T>：內部可變性 ========
    let data = RefCell::new(vec![1, 2, 3]);
    data.borrow_mut().push(4); // 執行期可變借用
    println!("{:?}", data.borrow()); // 執行期不可變借用

    // ======== Rc<RefCell<T>>：共享 + 可變 ========
    let shared_data = Rc::new(RefCell::new(0));
    let clone_a = Rc::clone(&shared_data);
    let clone_b = Rc::clone(&shared_data);

    *clone_a.borrow_mut() += 10;
    *clone_b.borrow_mut() += 20;
    println!("共享值: {}", shared_data.borrow()); // 30

    // ======== Cow<T>：Copy-on-Write ========
    use std::borrow::Cow;

    fn process_name(name: &str) -> Cow<str> {
        if name.contains(' ') {
            Cow::Owned(name.replace(' ', "_")) // 需要修改時才分配
        } else {
            Cow::Borrowed(name) // 不需要修改就借用
        }
    }

    println!("{}", process_name("Alice"));       // 借用
    println!("{}", process_name("Bob Smith"));    // 擁有
}
```

### 6.4 Rc / Arc

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    // ======== Arc<T>：原子引用計數（跨執行緒）========
    let config = Arc::new(AppConfig {
        database_url: "postgres://localhost/mydb".to_string(),
        max_connections: 20,
    });

    let mut handles = vec![];

    for i in 0..5 {
        let config = Arc::clone(&config);
        let handle = thread::spawn(move || {
            println!(
                "執行緒 {}: 連線到 {}，最大連線數 {}",
                i, config.database_url, config.max_connections
            );
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}

struct AppConfig {
    database_url: String,
    max_connections: u32,
}
```

### 6.5 Mutex / RwLock

```rust
use std::sync::{Arc, Mutex, RwLock};
use std::thread;

fn main() {
    // ======== Mutex<T>：互斥鎖 ========
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            // lock() 回傳 MutexGuard，離開作用域自動解鎖
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("計數器: {}", *counter.lock().unwrap()); // 10

    // ======== RwLock<T>：讀寫鎖 ========
    let cache = Arc::new(RwLock::new(std::collections::HashMap::<String, String>::new()));

    // 多個讀取者可以同時存取
    {
        let read_guard = cache.read().unwrap();
        println!("快取大小: {}", read_guard.len());
    }

    // 寫入時會獨佔
    {
        let mut write_guard = cache.write().unwrap();
        write_guard.insert("key".to_string(), "value".to_string());
    }
}
```

> ⚠️ **效能提示**：高併發場景中，考慮使用 `parking_lot` crate 取代標準庫的 `Mutex`/`RwLock`，它提供更好的效能且不需要 `unwrap()`（不會 poison）。

### 6.6 Channels（通道）

```rust
use std::sync::mpsc; // multi-producer, single-consumer
use std::thread;
use std::time::Duration;

fn main() {
    // ======== mpsc Channel ========
    let (tx, rx) = mpsc::channel();

    // 多個發送者
    for i in 0..5 {
        let tx = tx.clone();
        thread::spawn(move || {
            let msg = format!("訊息 {} 來自執行緒 {:?}", i, thread::current().id());
            tx.send(msg).unwrap();
        });
    }
    drop(tx); // 釋放原始發送者

    // 接收所有訊息
    for received in rx {
        println!("收到: {}", received);
    }

    // ======== Bounded Channel（有限容量）========
    let (tx, rx) = mpsc::sync_channel(3); // 容量 3

    thread::spawn(move || {
        for i in 0..10 {
            println!("發送 {}", i);
            tx.send(i).unwrap(); // 容量滿時會阻塞
        }
    });

    for received in rx {
        println!("  收到 {}", received);
        thread::sleep(Duration::from_millis(100));
    }
}

// ======== 使用 tokio 的非同步 Channel ========
// tokio::sync::mpsc  - 多生產者單消費者
// tokio::sync::broadcast - 廣播（多消費者）
// tokio::sync::watch  - 監看（最新值）
// tokio::sync::oneshot - 一次性（單發單收）
```

### 6.7 Async Runtime 與 Tokio

```rust
use tokio::sync::mpsc;
use tokio::time::{sleep, Duration};

// Tokio 主函式
#[tokio::main]
async fn main() {
    // ======== 產生非同步任務 ========
    let handle = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        "任務結果"
    });
    let result = handle.await.unwrap();
    println!("{}", result);

    // ======== 並行執行（tokio::join!）========
    let (a, b, c) = tokio::join!(
        async_task("A", 100),
        async_task("B", 200),
        async_task("C", 50),
    );
    println!("結果: {}, {}, {}", a, b, c);

    // ======== 競爭執行（tokio::select!）========
    tokio::select! {
        val = async_task("fast", 50) => println!("fast 完成: {}", val),
        val = async_task("slow", 500) => println!("slow 完成: {}", val),
    }
    // 只有最快完成的會被處理，另一個被取消

    // ======== 非同步 Channel ========
    let (tx, mut rx) = mpsc::channel(32);

    tokio::spawn(async move {
        for i in 0..5 {
            tx.send(format!("msg-{}", i)).await.unwrap();
            sleep(Duration::from_millis(50)).await;
        }
    });

    while let Some(msg) = rx.recv().await {
        println!("收到: {}", msg);
    }
}

async fn async_task(name: &str, delay_ms: u64) -> String {
    sleep(Duration::from_millis(delay_ms)).await;
    format!("{} 完成", name)
}
```

**Tokio Runtime 架構：**

```mermaid
graph TD
    RT["Tokio Runtime"] --> EXEC["Task Executor<br/>（工作竊取排程器）"]
    RT --> REACTOR["I/O Reactor<br/>（epoll/kqueue/IOCP）"]
    RT --> TIMER["Timer Driver<br/>（計時器驅動）"]

    EXEC --> W1["Worker Thread 1"]
    EXEC --> W2["Worker Thread 2"]
    EXEC --> WN["Worker Thread N"]

    W1 --> T1["Task"]
    W1 --> T2["Task"]
    W2 --> T3["Task"]
    WN --> TN["Task"]

    REACTOR --> IO1["TCP Socket"]
    REACTOR --> IO2["UDP Socket"]
    REACTOR --> IO3["File I/O"]

    style RT fill:#4CAF50,color:white
    style EXEC fill:#2196F3,color:white
    style REACTOR fill:#FF9800,color:white
```

### 6.8 Pin / Unpin

```rust
use std::pin::Pin;
use std::future::Future;

// Pin 確保值不會在記憶體中移動，對於自引用結構（如 async fn 產生的 Future）至關重要

// 大多數型別自動實作 Unpin（可以安全移動）
// async fn 產生的 Future 是 !Unpin（不能安全移動）

// 在實務中，你通常只在以下情況需要 Pin：
// 1. 實作自定義的 Future
// 2. 使用 tokio::pin! 巨集

async fn example() {
    let future = async { 42 };

    // 使用 tokio::pin! 將 future 釘在 stack 上
    tokio::pin!(future);

    // 現在可以多次 poll
    let result = (&mut future).await;
    println!("結果: {}", result);
}

// 在函式簽名中使用 Pin
fn process_future(future: Pin<&mut dyn Future<Output = i32>>) {
    // ...
}
```

### 6.9 Unsafe Rust

```rust
/// Unsafe Rust 允許以下操作：
/// 1. 解引用裸指標
/// 2. 呼叫 unsafe 函式
/// 3. 存取或修改 static mut 變數
/// 4. 實作 unsafe trait
/// 5. 存取 union 的欄位

fn main() {
    // ======== 解引用裸指標 ========
    let mut num = 5;
    let r1 = &num as *const i32;    // 不可變裸指標
    let r2 = &mut num as *mut i32;  // 可變裸指標

    unsafe {
        println!("r1: {}", *r1);
        *r2 = 10;
        println!("r2: {}", *r2);
    }

    // ======== 呼叫 unsafe 函式 ========
    unsafe {
        dangerous();
    }

    // ======== 安全封裝 unsafe 程式碼 ========
    let mut v = vec![1, 2, 3, 4, 5, 6];
    let (left, right) = split_at_mut(&mut v, 3);
    println!("左: {:?}", left);
    println!("右: {:?}", right);
}

unsafe fn dangerous() {
    // 這是一個 unsafe 函式
    println!("This is unsafe!");
}

/// 安全封裝 unsafe 操作的範例
/// 這是標準庫 split_at_mut 的簡化版
fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = values.len();
    let ptr = values.as_mut_ptr();

    assert!(mid <= len);

    unsafe {
        (
            std::slice::from_raw_parts_mut(ptr, mid),
            std::slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

> ⚠️ **企業規範**：
> - `unsafe` 區塊必須附帶 `// SAFETY:` 註解說明為何是安全的
> - 所有 `unsafe` 程式碼都必須經過嚴格的 Code Review
> - 優先使用安全的替代方案，只在確實必要時使用 `unsafe`
> - 在 CI 中使用 Miri（`cargo +nightly miri test`）檢測未定義行為

### 6.10 Macros（巨集）

```rust
// ======== 宣告式巨集（Declarative Macros）========

/// 自定義 vec! 巨集的簡化版
macro_rules! my_vec {
    // 空向量
    () => {
        Vec::new()
    };
    // 帶初始值
    ( $( $x:expr ),+ $(,)? ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )+
            temp_vec
        }
    };
}

/// HashMap 快速建立巨集
macro_rules! hashmap {
    ( $( $key:expr => $value:expr ),* $(,)? ) => {
        {
            let mut map = std::collections::HashMap::new();
            $(
                map.insert($key, $value);
            )*
            map
        }
    };
}

/// 自動實作 Builder Pattern
macro_rules! builder {
    ($name:ident { $( $field:ident : $ty:ty ),* $(,)? }) => {
        #[derive(Debug, Default)]
        struct $name {
            $( $field: Option<$ty>, )*
        }

        impl $name {
            fn new() -> Self {
                Self::default()
            }

            $(
                fn $field(mut self, value: $ty) -> Self {
                    self.$field = Some(value);
                    self
                }
            )*
        }
    };
}

fn main() {
    let v = my_vec![1, 2, 3];
    println!("{:?}", v);

    let scores = hashmap! {
        "Alice" => 95,
        "Bob" => 87,
    };
    println!("{:?}", scores);

    builder!(ServerConfig {
        host: String,
        port: u16,
        workers: usize,
    });

    let config = ServerConfig::new()
        .host("0.0.0.0".to_string())
        .port(8080)
        .workers(4);
    println!("{:?}", config);
}
```

### 6.11 Procedural Macros

```rust
// Procedural Macros 定義在獨立的 crate 中（proc-macro = true）

// ======== Derive Macro 使用範例 ========
// 使用 serde 的 derive macro
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
struct User {
    id: u64,
    #[serde(rename = "userName")]
    username: String,
    email: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    phone: Option<String>,
    #[serde(default)]
    active: bool,
}

// ======== Attribute Macro 使用範例 ========
// 使用 tokio 的 attribute macro
#[tokio::main]
async fn main() {
    let user = User {
        id: 1,
        username: "alice".to_string(),
        email: "alice@example.com".to_string(),
        phone: None,
        active: true,
    };

    // 序列化為 JSON
    let json = serde_json::to_string_pretty(&user).unwrap();
    println!("{}", json);

    // 從 JSON 反序列化
    let parsed: User = serde_json::from_str(&json).unwrap();
    println!("{:?}", parsed);
}

// ======== 自定義 Derive Macro（概念）========
// 需要建立獨立的 proc-macro crate
//
// Cargo.toml:
// [lib]
// proc-macro = true
//
// [dependencies]
// syn = "2"
// quote = "1"
// proc-macro2 = "1"
//
// use proc_macro::TokenStream;
// use quote::quote;
// use syn::{parse_macro_input, DeriveInput};
//
// #[proc_macro_derive(MyTrait)]
// pub fn my_trait_derive(input: TokenStream) -> TokenStream {
//     let input = parse_macro_input!(input as DeriveInput);
//     let name = input.ident;
//
//     let expanded = quote! {
//         impl MyTrait for #name {
//             fn hello(&self) {
//                 println!("Hello from {}!", stringify!(#name));
//             }
//         }
//     };
//
//     TokenStream::from(expanded)
// }
```

---

## 7. Rust Web 開發

### 7.1 Web Framework 比較

| 特性 | Axum | Actix Web | Rocket | Warp |
|------|------|-----------|--------|------|
| **維護者** | Tokio 團隊 | 社群 | Sergio Benitez | Sean McArthur |
| **效能** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **學習曲線** | 中等 | 中等偏高 | 低 | 高 |
| **生態整合** | Tokio / Tower 生態 | 自有生態 | 獨立生態 | Hyper 生態 |
| **型別安全** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Middleware** | Tower Service/Layer | Actix Middleware | Fairings | Filter 組合 |
| **WebSocket** | ✅ | ✅ | ✅ | ✅ |
| **HTTP/2** | ✅ | ✅ | ✅ | ✅ |
| **Async** | ✅ Tokio | ✅ Actix Runtime | ✅ Tokio | ✅ Tokio |
| **社群活躍度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **適合場景** | 企業 API / 微服務 | 高效能服務 | 快速開發 | 組合式 API |

### 7.2 Axum 概觀

Axum 是由 **Tokio 團隊**開發的 Web 框架，完全基於 Tower 生態系統。

```rust
use axum::{
    routing::{get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};
use tokio::net::TcpListener;

#[derive(Serialize)]
struct HealthResponse {
    status: String,
    version: String,
}

async fn health_check() -> Json<HealthResponse> {
    Json(HealthResponse {
        status: "healthy".to_string(),
        version: env!("CARGO_PKG_VERSION").to_string(),
    })
}

#[derive(Deserialize)]
struct CreateUser {
    username: String,
    email: String,
}

#[derive(Serialize)]
struct UserResponse {
    id: u64,
    username: String,
    email: String,
}

async fn create_user(Json(payload): Json<CreateUser>) -> Json<UserResponse> {
    Json(UserResponse {
        id: 1,
        username: payload.username,
        email: payload.email,
    })
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/health", get(health_check))
        .route("/users", post(create_user));

    let listener = TcpListener::bind("0.0.0.0:3000").await.unwrap();
    println!("伺服器啟動於 http://0.0.0.0:3000");
    axum::serve(listener, app).await.unwrap();
}
```

### 7.3 Actix Web 概觀

```rust
use actix_web::{web, App, HttpServer, HttpResponse, Responder};
use serde::Serialize;

#[derive(Serialize)]
struct Health {
    status: String,
}

async fn health() -> impl Responder {
    HttpResponse::Ok().json(Health {
        status: "ok".to_string(),
    })
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/health", web::get().to(health))
    })
    .bind("0.0.0.0:8080")?
    .run()
    .await
}
```

### 7.4 Rocket 概觀

```rust
#[macro_use] extern crate rocket;
use rocket::serde::json::Json;
use serde::Serialize;

#[derive(Serialize)]
struct Health {
    status: String,
}

#[get("/health")]
fn health() -> Json<Health> {
    Json(Health {
        status: "ok".to_string(),
    })
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![health])
}
```

### 7.5 Warp 概觀

```rust
use warp::Filter;
use serde::Serialize;

#[derive(Serialize)]
struct Health {
    status: String,
}

#[tokio::main]
async fn main() {
    let health = warp::path("health")
        .and(warp::get())
        .map(|| {
            warp::reply::json(&Health {
                status: "ok".to_string(),
            })
        });

    warp::serve(health)
        .run(([0, 0, 0, 0], 3000))
        .await;
}
```

### 7.6 Framework 選型建議

```mermaid
graph TD
    START["選擇 Web Framework"] --> Q1{"需要 Tokio<br/>生態整合？"}
    Q1 -->|是| Q2{"團隊熟悉度？"}
    Q1 -->|否| ACTIX["Actix Web"]

    Q2 -->|有經驗| AXUM["✅ Axum（推薦）"]
    Q2 -->|新手| Q3{"專案規模？"}

    Q3 -->|小型/原型| ROCKET["Rocket"]
    Q3 -->|中大型| AXUM

    ACTIX --> NOTE1["高效能場景<br/>獨立執行時期"]
    AXUM --> NOTE2["企業級首選<br/>Tower 生態整合"]
    ROCKET --> NOTE3["快速開發<br/>學習曲線低"]
```

> 💡 **企業推薦**：**Axum** 是目前企業級 Rust Web 開發的首選，原因：
> 1. 由 Tokio 團隊維護，長期支援有保障
> 2. 完整的 Tower 中介層生態（限流、追蹤、CORS、壓縮等）
> 3. 型別安全的路由與 Extractor 設計
> 4. 與 Tokio 生態（sqlx、tonic、reqwest）無縫整合

---

## 8. 使用 Axum 建立 RESTful API

### 8.1 專案架構（Clean Architecture）

```
enterprise-api/
├── Cargo.toml
├── .env
├── migrations/              # SQLx 資料庫遷移
│   └── 001_create_users.sql
├── src/
│   ├── main.rs              # 應用入口
│   ├── lib.rs               # Library root
│   ├── config.rs            # 設定管理
│   ├── error.rs             # 統一錯誤處理
│   ├── state.rs             # 應用狀態
│   ├── api/                 # API 層（Controller）
│   │   ├── mod.rs
│   │   ├── routes.rs        # 路由定義
│   │   ├── users.rs         # 使用者 API
│   │   ├── auth.rs          # 認證 API
│   │   └── health.rs        # 健康檢查
│   ├── domain/              # 領域層（Entity）
│   │   ├── mod.rs
│   │   └── user.rs
│   ├── dto/                 # 資料傳輸物件
│   │   ├── mod.rs
│   │   └── user_dto.rs
│   ├── service/             # 服務層（Use Case）
│   │   ├── mod.rs
│   │   └── user_service.rs
│   ├── repository/          # 資料存取層
│   │   ├── mod.rs
│   │   └── user_repo.rs
│   └── middleware/          # 中介層
│       ├── mod.rs
│       ├── auth.rs
│       ├── logging.rs
│       └── cors.rs
├── tests/                   # 整合測試
│   └── api_tests.rs
└── Dockerfile
```

```mermaid
graph TD
    subgraph "Clean Architecture"
        API["API Layer<br/>（Controllers / Handlers）"]
        DTO["DTO Layer<br/>（Request / Response）"]
        SVC["Service Layer<br/>（Business Logic）"]
        REPO["Repository Layer<br/>（Data Access）"]
        DOM["Domain Layer<br/>（Entities / Value Objects）"]

        API --> DTO
        API --> SVC
        SVC --> REPO
        SVC --> DOM
        REPO --> DOM
    end

    subgraph "外部依賴"
        DB[(PostgreSQL)]
        CACHE[(Redis)]
        EXT[外部 API]
    end

    REPO --> DB
    REPO --> CACHE
    SVC --> EXT
```

### 8.2 DTO 與資料驗證

```rust
// src/dto/user_dto.rs
use serde::{Deserialize, Serialize};
use validator::Validate;

/// 建立使用者請求
#[derive(Debug, Deserialize, Validate)]
pub struct CreateUserRequest {
    #[validate(length(min = 3, max = 50, message = "使用者名稱長度必須在 3-50 之間"))]
    pub username: String,

    #[validate(email(message = "無效的電子郵件格式"))]
    pub email: String,

    #[validate(length(min = 8, message = "密碼長度至少 8 個字元"))]
    pub password: String,
}

/// 更新使用者請求
#[derive(Debug, Deserialize, Validate)]
pub struct UpdateUserRequest {
    #[validate(length(min = 3, max = 50))]
    pub username: Option<String>,

    #[validate(email)]
    pub email: Option<String>,
}

/// 使用者回應
#[derive(Debug, Serialize)]
pub struct UserResponse {
    pub id: uuid::Uuid,
    pub username: String,
    pub email: String,
    pub active: bool,
    pub created_at: chrono::NaiveDateTime,
}

/// 分頁查詢參數
#[derive(Debug, Deserialize)]
pub struct PaginationParams {
    #[serde(default = "default_page")]
    pub page: u32,
    #[serde(default = "default_per_page")]
    pub per_page: u32,
}

fn default_page() -> u32 { 1 }
fn default_per_page() -> u32 { 20 }

/// 分頁回應
#[derive(Debug, Serialize)]
pub struct PaginatedResponse<T: Serialize> {
    pub data: Vec<T>,
    pub total: u64,
    pub page: u32,
    pub per_page: u32,
    pub total_pages: u32,
}

impl<T: Serialize> PaginatedResponse<T> {
    pub fn new(data: Vec<T>, total: u64, page: u32, per_page: u32) -> Self {
        let total_pages = ((total as f64) / (per_page as f64)).ceil() as u32;
        Self { data, total, page, per_page, total_pages }
    }
}
```

### 8.3 Service Layer

```rust
// src/service/user_service.rs
use crate::domain::user::User;
use crate::dto::user_dto::*;
use crate::error::AppError;
use crate::repository::user_repo::UserRepository;
use uuid::Uuid;

pub struct UserService {
    repo: UserRepository,
}

impl UserService {
    pub fn new(repo: UserRepository) -> Self {
        Self { repo }
    }

    /// 建立新使用者
    pub async fn create_user(&self, req: CreateUserRequest) -> Result<UserResponse, AppError> {
        // 檢查使用者名稱是否已存在
        if self.repo.find_by_username(&req.username).await?.is_some() {
            return Err(AppError::Conflict("使用者名稱已存在".to_string()));
        }

        // 雜湊密碼
        let password_hash = hash_password(&req.password)?;

        // 建立使用者
        let user = User::new(req.username, req.email, password_hash);
        let created = self.repo.create(&user).await?;

        Ok(created.into())
    }

    /// 取得使用者
    pub async fn get_user(&self, id: Uuid) -> Result<UserResponse, AppError> {
        let user = self.repo
            .find_by_id(id)
            .await?
            .ok_or_else(|| AppError::NotFound(format!("使用者 {} 不存在", id)))?;

        Ok(user.into())
    }

    /// 取得使用者列表（分頁）
    pub async fn list_users(&self, params: PaginationParams) -> Result<PaginatedResponse<UserResponse>, AppError> {
        let offset = ((params.page - 1) * params.per_page) as i64;
        let limit = params.per_page as i64;

        let (users, total) = self.repo.find_all(offset, limit).await?;
        let responses: Vec<UserResponse> = users.into_iter().map(Into::into).collect();

        Ok(PaginatedResponse::new(responses, total as u64, params.page, params.per_page))
    }
}

fn hash_password(password: &str) -> Result<String, AppError> {
    use argon2::{Argon2, PasswordHasher};
    use argon2::password_hash::SaltString;
    use argon2::password_hash::rand_core::OsRng;

    let salt = SaltString::generate(&mut OsRng);
    let argon2 = Argon2::default();
    let hash = argon2
        .hash_password(password.as_bytes(), &salt)
        .map_err(|e| AppError::Internal(format!("密碼雜湊失敗: {}", e)))?
        .to_string();
    Ok(hash)
}
```

### 8.4 Repository Pattern

```rust
// src/repository/user_repo.rs
use crate::domain::user::User;
use crate::error::AppError;
use sqlx::PgPool;
use uuid::Uuid;

#[derive(Clone)]
pub struct UserRepository {
    pool: PgPool,
}

impl UserRepository {
    pub fn new(pool: PgPool) -> Self {
        Self { pool }
    }

    pub async fn create(&self, user: &User) -> Result<User, AppError> {
        let created = sqlx::query_as!(
            User,
            r#"
            INSERT INTO users (id, username, email, password_hash, active, created_at, updated_at)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
            RETURNING *
            "#,
            user.id,
            user.username,
            user.email,
            user.password_hash,
            user.active,
            user.created_at,
            user.updated_at,
        )
        .fetch_one(&self.pool)
        .await?;

        Ok(created)
    }

    pub async fn find_by_id(&self, id: Uuid) -> Result<Option<User>, AppError> {
        let user = sqlx::query_as!(User, "SELECT * FROM users WHERE id = $1", id)
            .fetch_optional(&self.pool)
            .await?;
        Ok(user)
    }

    pub async fn find_by_username(&self, username: &str) -> Result<Option<User>, AppError> {
        let user = sqlx::query_as!(User, "SELECT * FROM users WHERE username = $1", username)
            .fetch_optional(&self.pool)
            .await?;
        Ok(user)
    }

    pub async fn find_all(&self, offset: i64, limit: i64) -> Result<(Vec<User>, i64), AppError> {
        let users = sqlx::query_as!(
            User,
            "SELECT * FROM users ORDER BY created_at DESC LIMIT $1 OFFSET $2",
            limit,
            offset,
        )
        .fetch_all(&self.pool)
        .await?;

        let count = sqlx::query_scalar!("SELECT COUNT(*) FROM users")
            .fetch_one(&self.pool)
            .await?
            .unwrap_or(0);

        Ok((users, count))
    }

    pub async fn delete(&self, id: Uuid) -> Result<bool, AppError> {
        let result = sqlx::query!("DELETE FROM users WHERE id = $1", id)
            .execute(&self.pool)
            .await?;
        Ok(result.rows_affected() > 0)
    }
}
```

### 8.5 Middleware

```rust
// src/middleware/logging.rs
use axum::{extract::Request, middleware::Next, response::Response};
use std::time::Instant;
use tracing::info;

/// 請求日誌中介層
pub async fn logging_middleware(req: Request, next: Next) -> Response {
    let method = req.method().clone();
    let uri = req.uri().clone();
    let start = Instant::now();

    let response = next.run(req).await;

    let duration = start.elapsed();
    let status = response.status();

    info!(
        method = %method,
        uri = %uri,
        status = %status,
        duration_ms = %duration.as_millis(),
        "HTTP 請求"
    );

    response
}

// src/middleware/cors.rs
use tower_http::cors::{Any, CorsLayer};
use http::Method;

pub fn cors_layer() -> CorsLayer {
    CorsLayer::new()
        .allow_origin(Any)
        .allow_methods([Method::GET, Method::POST, Method::PUT, Method::DELETE])
        .allow_headers(Any)
        .max_age(std::time::Duration::from_secs(3600))
}
```

### 8.6 JWT 認證與授權

```rust
// src/middleware/auth.rs
use axum::{
    extract::Request,
    http::{header, StatusCode},
    middleware::Next,
    response::Response,
};
use jsonwebtoken::{decode, encode, DecodingKey, EncodingKey, Header, Validation};
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Claims {
    pub sub: String,       // 使用者 ID
    pub role: String,      // 角色
    pub exp: usize,        // 過期時間（Unix timestamp）
    pub iat: usize,        // 簽發時間
}

impl Claims {
    pub fn new(user_id: &str, role: &str, duration_hours: i64) -> Self {
        let now = chrono::Utc::now();
        Self {
            sub: user_id.to_string(),
            role: role.to_string(),
            iat: now.timestamp() as usize,
            exp: (now + chrono::Duration::hours(duration_hours)).timestamp() as usize,
        }
    }
}

/// 產生 JWT Token
pub fn generate_token(user_id: &str, role: &str, secret: &str) -> Result<String, jsonwebtoken::errors::Error> {
    let claims = Claims::new(user_id, role, 24); // 24 小時有效
    encode(
        &Header::default(),
        &claims,
        &EncodingKey::from_secret(secret.as_ref()),
    )
}

/// 驗證 JWT Token
pub fn verify_token(token: &str, secret: &str) -> Result<Claims, jsonwebtoken::errors::Error> {
    let token_data = decode::<Claims>(
        token,
        &DecodingKey::from_secret(secret.as_ref()),
        &Validation::default(),
    )?;
    Ok(token_data.claims)
}

/// JWT 認證中介層
pub async fn auth_middleware(mut req: Request, next: Next) -> Result<Response, StatusCode> {
    let auth_header = req
        .headers()
        .get(header::AUTHORIZATION)
        .and_then(|h| h.to_str().ok())
        .ok_or(StatusCode::UNAUTHORIZED)?;

    let token = auth_header
        .strip_prefix("Bearer ")
        .ok_or(StatusCode::UNAUTHORIZED)?;

    let secret = std::env::var("JWT_SECRET").unwrap_or_else(|_| "default-secret".to_string());

    let claims = verify_token(token, &secret).map_err(|_| StatusCode::UNAUTHORIZED)?;

    // 將 claims 注入請求擴展
    req.extensions_mut().insert(claims);

    Ok(next.run(req).await)
}
```

### 8.7 OpenAPI / Swagger

```rust
// 使用 utoipa 產生 OpenAPI 文件
use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

#[derive(OpenApi)]
#[openapi(
    paths(
        api::health::health_check,
        api::users::create_user,
        api::users::get_user,
        api::users::list_users,
    ),
    components(
        schemas(
            dto::user_dto::CreateUserRequest,
            dto::user_dto::UserResponse,
            dto::user_dto::PaginatedResponse<dto::user_dto::UserResponse>,
        )
    ),
    tags(
        (name = "health", description = "健康檢查"),
        (name = "users", description = "使用者管理"),
    ),
    info(
        title = "企業級 API",
        version = "1.0.0",
        description = "Rust + Axum 企業級 REST API"
    )
)]
struct ApiDoc;

// 在 Router 中掛載 Swagger UI
fn create_router() -> Router {
    Router::new()
        // ... 其他路由
        .merge(SwaggerUi::new("/swagger-ui").url("/api-docs/openapi.json", ApiDoc::openapi()))
}
```

### 8.8 完整 API 範例

```rust
// src/api/users.rs
use axum::{
    extract::{Path, Query, State},
    http::StatusCode,
    Json,
};
use uuid::Uuid;
use validator::Validate;

use crate::dto::user_dto::*;
use crate::error::AppError;
use crate::state::AppState;

/// 建立使用者
#[utoipa::path(
    post,
    path = "/api/v1/users",
    request_body = CreateUserRequest,
    responses(
        (status = 201, description = "使用者建立成功", body = UserResponse),
        (status = 400, description = "驗證失敗"),
        (status = 409, description = "使用者名稱已存在"),
    ),
    tag = "users"
)]
pub async fn create_user(
    State(state): State<AppState>,
    Json(payload): Json<CreateUserRequest>,
) -> Result<(StatusCode, Json<UserResponse>), AppError> {
    // 驗證輸入
    payload.validate().map_err(|e| AppError::Validation(e.to_string()))?;

    let user = state.user_service.create_user(payload).await?;
    Ok((StatusCode::CREATED, Json(user)))
}

/// 取得使用者
#[utoipa::path(
    get,
    path = "/api/v1/users/{id}",
    params(("id" = Uuid, Path, description = "使用者 ID")),
    responses(
        (status = 200, description = "成功", body = UserResponse),
        (status = 404, description = "使用者不存在"),
    ),
    tag = "users"
)]
pub async fn get_user(
    State(state): State<AppState>,
    Path(id): Path<Uuid>,
) -> Result<Json<UserResponse>, AppError> {
    let user = state.user_service.get_user(id).await?;
    Ok(Json(user))
}

/// 取得使用者列表
pub async fn list_users(
    State(state): State<AppState>,
    Query(params): Query<PaginationParams>,
) -> Result<Json<PaginatedResponse<UserResponse>>, AppError> {
    let result = state.user_service.list_users(params).await?;
    Ok(Json(result))
}

// src/api/routes.rs
use axum::{middleware, routing::{get, post, put, delete}, Router};
use crate::state::AppState;
use crate::middleware::auth::auth_middleware;

pub fn create_router(state: AppState) -> Router {
    let public_routes = Router::new()
        .route("/health", get(super::health::health_check))
        .route("/api/v1/auth/login", post(super::auth::login))
        .route("/api/v1/auth/register", post(super::auth::register));

    let protected_routes = Router::new()
        .route("/api/v1/users", get(super::users::list_users))
        .route("/api/v1/users/:id", get(super::users::get_user))
        .route("/api/v1/users/:id", put(super::users::update_user))
        .route("/api/v1/users/:id", delete(super::users::delete_user))
        .layer(middleware::from_fn(auth_middleware));

    Router::new()
        .merge(public_routes)
        .merge(protected_routes)
        .with_state(state)
}
```

### 8.9 Docker 化

```dockerfile
# ======== Multi-stage Dockerfile ========
# Stage 1: 建置
FROM rust:1.95-bookworm AS builder

WORKDIR /app

# 利用 Docker cache：先複製依賴檔案
COPY Cargo.toml Cargo.lock ./
RUN mkdir src && echo "fn main() {}" > src/main.rs
RUN cargo build --release && rm -rf src

# 複製完整原始碼並建置
COPY . .
RUN touch src/main.rs  # 強制重新編譯 main
RUN cargo build --release

# Stage 2: 執行（最小化 image）
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 建立非 root 使用者
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# 從 builder 複製執行檔
COPY --from=builder /app/target/release/enterprise-api .
COPY --from=builder /app/migrations ./migrations

# 設定權限
RUN chown -R appuser:appuser /app
USER appuser

# 暴露埠號
EXPOSE 3000

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# 執行
ENTRYPOINT ["./enterprise-api"]
```

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/enterprise
      - REDIS_URL=redis://cache:6379
      - JWT_SECRET=${JWT_SECRET}
      - RUST_LOG=info
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: enterprise
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data

volumes:
  pgdata:
  redisdata:
```

---

## 9. 資料庫整合

### 9.1 SQLx（推薦）

SQLx 是 Rust 生態中最受歡迎的 async 資料庫驅動程式，特色是**編譯期 SQL 驗證**。

```toml
# Cargo.toml
[dependencies]
sqlx = { version = "0.8", features = [
    "runtime-tokio",
    "tls-rustls",
    "postgres",
    "uuid",
    "chrono",
    "migrate",
] }
```

```rust
use sqlx::postgres::PgPoolOptions;
use sqlx::PgPool;

/// 建立資料庫連線池
pub async fn create_pool(database_url: &str) -> Result<PgPool, sqlx::Error> {
    PgPoolOptions::new()
        .max_connections(20)
        .min_connections(5)
        .acquire_timeout(std::time::Duration::from_secs(5))
        .idle_timeout(std::time::Duration::from_secs(600))
        .max_lifetime(std::time::Duration::from_secs(1800))
        .connect(database_url)
        .await
}

// ======== 編譯期驗證的查詢（query_as!）========
#[derive(Debug, sqlx::FromRow)]
pub struct User {
    pub id: uuid::Uuid,
    pub username: String,
    pub email: String,
    pub password_hash: String,
    pub active: bool,
    pub created_at: chrono::NaiveDateTime,
    pub updated_at: chrono::NaiveDateTime,
}

impl User {
    /// 根據 ID 查詢（編譯期驗證 SQL）
    pub async fn find_by_id(pool: &PgPool, id: uuid::Uuid) -> Result<Option<User>, sqlx::Error> {
        sqlx::query_as!(User, "SELECT * FROM users WHERE id = $1", id)
            .fetch_optional(pool)
            .await
    }

    /// 建立使用者
    pub async fn create(pool: &PgPool, username: &str, email: &str, password_hash: &str) -> Result<User, sqlx::Error> {
        sqlx::query_as!(
            User,
            r#"
            INSERT INTO users (id, username, email, password_hash, active, created_at, updated_at)
            VALUES ($1, $2, $3, $4, true, NOW(), NOW())
            RETURNING *
            "#,
            uuid::Uuid::new_v4(),
            username,
            email,
            password_hash,
        )
        .fetch_one(pool)
        .await
    }

    /// 分頁查詢
    pub async fn find_all(pool: &PgPool, offset: i64, limit: i64) -> Result<Vec<User>, sqlx::Error> {
        sqlx::query_as!(
            User,
            "SELECT * FROM users ORDER BY created_at DESC LIMIT $1 OFFSET $2",
            limit,
            offset,
        )
        .fetch_all(pool)
        .await
    }
}
```

#### SQLx 遷移管理

```bash
# 安裝 sqlx-cli
cargo install sqlx-cli --no-default-features --features postgres

# 建立遷移目錄
sqlx migrate add create_users_table

# 遷移檔案範例：migrations/20260501000001_create_users_table.sql
```

```sql
-- migrations/20260501000001_create_users_table.sql
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);

-- 自動更新 updated_at
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();
```

```bash
# 執行遷移
sqlx migrate run --database-url postgres://user:pass@localhost/mydb

# 回滾
sqlx migrate revert

# 在程式中自動遷移
```

```rust
// 程式啟動時自動遷移
sqlx::migrate!("./migrations")
    .run(&pool)
    .await
    .expect("資料庫遷移失敗");
```

#### 交易處理

```rust
use sqlx::PgPool;

pub async fn transfer_funds(
    pool: &PgPool,
    from_id: uuid::Uuid,
    to_id: uuid::Uuid,
    amount: f64,
) -> Result<(), sqlx::Error> {
    let mut tx = pool.begin().await?;

    // 扣款
    sqlx::query!(
        "UPDATE accounts SET balance = balance - $1 WHERE id = $2 AND balance >= $1",
        amount,
        from_id,
    )
    .execute(&mut *tx)
    .await?;

    // 入款
    sqlx::query!(
        "UPDATE accounts SET balance = balance + $1 WHERE id = $2",
        amount,
        to_id,
    )
    .execute(&mut *tx)
    .await?;

    // 記錄交易
    sqlx::query!(
        "INSERT INTO transactions (from_id, to_id, amount) VALUES ($1, $2, $3)",
        from_id,
        to_id,
        amount,
    )
    .execute(&mut *tx)
    .await?;

    // 提交交易
    tx.commit().await?;
    Ok(())
}
```

### 9.2 Diesel

Diesel 是 Rust 的 ORM 框架，特色是**完全型別安全的查詢 DSL**。

```toml
# Cargo.toml
[dependencies]
diesel = { version = "2", features = ["postgres", "uuid", "chrono"] }
diesel-async = { version = "0.5", features = ["postgres", "deadpool"] }
```

```rust
// schema.rs（由 diesel_cli 自動產生）
diesel::table! {
    users (id) {
        id -> Uuid,
        username -> Varchar,
        email -> Varchar,
        password_hash -> Varchar,
        active -> Bool,
        created_at -> Timestamp,
        updated_at -> Timestamp,
    }
}

// models.rs
use diesel::prelude::*;
use uuid::Uuid;
use chrono::NaiveDateTime;

#[derive(Queryable, Selectable, Debug)]
#[diesel(table_name = crate::schema::users)]
pub struct User {
    pub id: Uuid,
    pub username: String,
    pub email: String,
    pub password_hash: String,
    pub active: bool,
    pub created_at: NaiveDateTime,
    pub updated_at: NaiveDateTime,
}

#[derive(Insertable)]
#[diesel(table_name = crate::schema::users)]
pub struct NewUser<'a> {
    pub username: &'a str,
    pub email: &'a str,
    pub password_hash: &'a str,
}

// 查詢範例
use diesel::prelude::*;
use crate::schema::users::dsl::*;

fn find_active_users(conn: &mut PgConnection) -> QueryResult<Vec<User>> {
    users
        .filter(active.eq(true))
        .order(created_at.desc())
        .limit(10)
        .select(User::as_select())
        .load(conn)
}
```

### 9.3 SeaORM

SeaORM 是一個 async 的 ORM 框架，靈感來自 ActiveRecord。

```toml
# Cargo.toml
[dependencies]
sea-orm = { version = "1", features = [
    "sqlx-postgres",
    "runtime-tokio-rustls",
    "macros"
] }
```

```rust
use sea_orm::entity::prelude::*;

// Entity 定義
#[derive(Clone, Debug, PartialEq, DeriveEntityModel)]
#[sea_orm(table_name = "users")]
pub struct Model {
    #[sea_orm(primary_key)]
    pub id: Uuid,
    pub username: String,
    pub email: String,
    pub password_hash: String,
    pub active: bool,
    pub created_at: DateTimeUtc,
    pub updated_at: DateTimeUtc,
}

#[derive(Copy, Clone, Debug, EnumIter, DeriveRelation)]
pub enum Relation {}

impl ActiveModelBehavior for ActiveModel {}

// 查詢範例
async fn find_users(db: &DatabaseConnection) -> Result<Vec<Model>, DbErr> {
    Entity::find()
        .filter(Column::Active.eq(true))
        .order_by_desc(Column::CreatedAt)
        .limit(10)
        .all(db)
        .await
}
```

### 9.4 ORM 比較表

| 特性 | SQLx | Diesel | SeaORM |
|------|------|--------|--------|
| **類型** | 驅動程式 / 輕量 SQL | 完整 ORM | 完整 ORM |
| **Async** | ✅ 原生 | ⚠️ 需 diesel-async | ✅ 原生 |
| **SQL 驗證** | 編譯期（需要 DB） | 編譯期（不需 DB） | 執行期 |
| **學習曲線** | 低 | 中高 | 中 |
| **效能** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **遷移** | ✅ sqlx-cli | ✅ diesel_cli | ✅ sea-orm-cli |
| **Raw SQL** | ✅ 原生 | ⚠️ `sql_query` | ⚠️ 有限 |
| **多資料庫** | PG/MySQL/SQLite | PG/MySQL/SQLite | PG/MySQL/SQLite |
| **適合場景** | 效能敏感 / 複雜 SQL | 型別安全優先 | 快速開發 / 類 ORM |

> 💡 **企業推薦**：中大型專案推薦 **SQLx**，因為它提供最佳效能、編譯期 SQL 驗證、最大的靈活性，以及與 Tokio 生態的完美整合。

### 9.5 Redis 快取

```rust
use bb8_redis::{bb8, RedisConnectionManager};
use redis::AsyncCommands;
use serde::{de::DeserializeOwned, Serialize};

pub type RedisPool = bb8::Pool<RedisConnectionManager>;

/// 建立 Redis 連線池
pub async fn create_redis_pool(redis_url: &str) -> Result<RedisPool, Box<dyn std::error::Error>> {
    let manager = RedisConnectionManager::new(redis_url)?;
    let pool = bb8::Pool::builder()
        .max_size(20)
        .min_idle(Some(5))
        .build(manager)
        .await?;
    Ok(pool)
}

/// 通用的快取服務
pub struct CacheService {
    pool: RedisPool,
    default_ttl: u64,
}

impl CacheService {
    pub fn new(pool: RedisPool, default_ttl: u64) -> Self {
        Self { pool, default_ttl }
    }

    /// 取得快取
    pub async fn get<T: DeserializeOwned>(&self, key: &str) -> Result<Option<T>, anyhow::Error> {
        let mut conn = self.pool.get().await?;
        let value: Option<String> = conn.get(key).await?;
        match value {
            Some(v) => Ok(Some(serde_json::from_str(&v)?)),
            None => Ok(None),
        }
    }

    /// 設定快取
    pub async fn set<T: Serialize>(&self, key: &str, value: &T, ttl: Option<u64>) -> Result<(), anyhow::Error> {
        let mut conn = self.pool.get().await?;
        let serialized = serde_json::to_string(value)?;
        let ttl = ttl.unwrap_or(self.default_ttl);
        conn.set_ex(key, serialized, ttl).await?;
        Ok(())
    }

    /// 刪除快取
    pub async fn delete(&self, key: &str) -> Result<(), anyhow::Error> {
        let mut conn = self.pool.get().await?;
        conn.del(key).await?;
        Ok(())
    }

    /// Cache-Aside Pattern
    pub async fn get_or_set<T, F, Fut>(
        &self,
        key: &str,
        ttl: Option<u64>,
        fetch: F,
    ) -> Result<T, anyhow::Error>
    where
        T: Serialize + DeserializeOwned,
        F: FnOnce() -> Fut,
        Fut: std::future::Future<Output = Result<T, anyhow::Error>>,
    {
        // 先查快取
        if let Some(cached) = self.get::<T>(key).await? {
            return Ok(cached);
        }

        // 快取未命中，從資料來源取得
        let value = fetch().await?;

        // 存入快取
        self.set(key, &value, ttl).await?;

        Ok(value)
    }
}
```

### 9.6 PostgreSQL 整合實務

PostgreSQL 是企業級 Rust 專案最常搭配的關聯式資料庫。以下展示透過 SQLx 進行 PostgreSQL 專屬功能整合：

```toml
# Cargo.toml
[dependencies]
sqlx = { version = "0.8", features = [
    "runtime-tokio",
    "postgres",
    "chrono",
    "uuid",
    "json",        # 支援 JSONB 欄位
    "ipnetwork",   # 支援 INET / CIDR 型別
] }
tokio = { version = "1", features = ["full"] }
```

```rust
use sqlx::postgres::{PgPoolOptions, PgRow};
use sqlx::{FromRow, Row};

/// PostgreSQL 專屬功能示範
#[derive(Debug, FromRow)]
struct AuditLog {
    id: i64,
    user_id: uuid::Uuid,
    action: String,
    payload: serde_json::Value, // JSONB 欄位
    created_at: chrono::DateTime<chrono::Utc>,
}

/// 建立連線池（PostgreSQL 建議參數）
async fn create_pg_pool(url: &str) -> sqlx::PgPool {
    PgPoolOptions::new()
        .max_connections(20)
        .min_connections(5)
        .acquire_timeout(std::time::Duration::from_secs(3))
        .idle_timeout(std::time::Duration::from_secs(600))
        .max_lifetime(std::time::Duration::from_secs(1800))
        .connect(url)
        .await
        .expect("無法連線至 PostgreSQL")
}

/// 使用 JSONB 查詢
async fn query_audit_by_action(pool: &sqlx::PgPool, action: &str) -> Vec<AuditLog> {
    sqlx::query_as::<_, AuditLog>(
        "SELECT id, user_id, action, payload, created_at
         FROM audit_logs
         WHERE payload->>'action' = $1
         ORDER BY created_at DESC"
    )
    .bind(action)
    .fetch_all(pool)
    .await
    .unwrap_or_default()
}

/// 使用 LISTEN/NOTIFY 做即時通知
async fn listen_notifications(pool: &sqlx::PgPool) {
    let mut listener = sqlx::postgres::PgListener::connect_with(pool).await.unwrap();
    listener.listen("order_created").await.unwrap();

    loop {
        let notification = listener.recv().await.unwrap();
        println!("收到通知 channel={}, payload={}", notification.channel(), notification.payload());
    }
}
```

### 9.7 MySQL 整合實務

```toml
# Cargo.toml
[dependencies]
sqlx = { version = "0.8", features = ["runtime-tokio", "mysql", "chrono"] }
```

```rust
use sqlx::mysql::MySqlPoolOptions;

/// MySQL 連線池建立
async fn create_mysql_pool(url: &str) -> sqlx::MySqlPool {
    MySqlPoolOptions::new()
        .max_connections(10)
        .connect(url) // mysql://user:pass@host:3306/dbname
        .await
        .expect("無法連線至 MySQL")
}

/// MySQL 查詢範例（使用 LAST_INSERT_ID）
async fn insert_and_get_id(pool: &sqlx::MySqlPool, name: &str) -> u64 {
    let result = sqlx::query("INSERT INTO products (name) VALUES (?)")
        .bind(name)
        .execute(pool)
        .await
        .unwrap();
    result.last_insert_id()
}
```

> ⚠️ **注意**：MySQL 使用 `?` 作為佔位符（PostgreSQL 使用 `$1`）。SQLx 會根據 feature flag 自動切換。

### 9.8 SQLite 整合實務

```toml
# Cargo.toml
[dependencies]
sqlx = { version = "0.8", features = ["runtime-tokio", "sqlite", "chrono"] }
```

```rust
use sqlx::sqlite::SqlitePoolOptions;

/// SQLite 適合嵌入式場景、測試環境、CLI 工具
async fn create_sqlite_pool(path: &str) -> sqlx::SqlitePool {
    SqlitePoolOptions::new()
        .max_connections(5)
        .connect(&format!("sqlite:{}", path))
        .await
        .expect("無法開啟 SQLite 資料庫")
}

/// 使用 SQLite 做整合測試的慣例模式
#[cfg(test)]
async fn setup_test_db() -> sqlx::SqlitePool {
    let pool = SqlitePoolOptions::new()
        .connect("sqlite::memory:") // 記憶體內資料庫
        .await
        .unwrap();
    sqlx::migrate!("./migrations").run(&pool).await.unwrap();
    pool
}
```

---

## 10. 非同步程式設計與高併發

### 10.1 Tokio Runtime 詳解

```rust
use tokio::runtime::Builder;

fn main() {
    // ======== 多執行緒 Runtime（預設）========
    let rt = Builder::new_multi_thread()
        .worker_threads(4)           // Worker 執行緒數量
        .thread_name("my-worker")    // 執行緒名稱
        .thread_stack_size(3 * 1024 * 1024) // 堆疊大小
        .enable_all()                // 啟用所有功能（IO + Time）
        .build()
        .unwrap();

    rt.block_on(async {
        println!("在多執行緒 runtime 中執行");
    });

    // ======== 單執行緒 Runtime ========
    let rt = Builder::new_current_thread()
        .enable_all()
        .build()
        .unwrap();

    rt.block_on(async {
        println!("在單執行緒 runtime 中執行");
    });
}

// 使用 #[tokio::main] 巨集等同於：
// fn main() {
//     tokio::runtime::Builder::new_multi_thread()
//         .enable_all()
//         .build()
//         .unwrap()
//         .block_on(async { ... })
// }
```

### 10.2 任務產生與管理

```rust
use tokio::task;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    // ======== tokio::spawn：產生非同步任務 ========
    let handle = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        42
    });
    let result = handle.await.unwrap();
    println!("結果: {}", result);

    // ======== 多個並行任務 ========
    let mut handles = Vec::new();
    for i in 0..10 {
        handles.push(tokio::spawn(async move {
            sleep(Duration::from_millis(100)).await;
            i * 2
        }));
    }

    let mut results = Vec::new();
    for handle in handles {
        results.push(handle.await.unwrap());
    }
    println!("結果: {:?}", results);

    // ======== JoinSet：管理一組任務 ========
    let mut set = task::JoinSet::new();
    for i in 0..5 {
        set.spawn(async move {
            sleep(Duration::from_millis(i * 50)).await;
            format!("任務 {} 完成", i)
        });
    }

    while let Some(result) = set.join_next().await {
        println!("{}", result.unwrap());
    }

    // ======== spawn_blocking：在阻塞執行緒池中執行 ========
    let result = task::spawn_blocking(|| {
        // CPU 密集或阻塞操作
        let mut sum = 0u64;
        for i in 0..1_000_000 {
            sum += i;
        }
        sum
    }).await.unwrap();
    println!("阻塞計算結果: {}", result);
}
```

### 10.3 並行模式

```mermaid
graph LR
    subgraph "join! — 等待所有任務"
        J1["Task A"] --> JR["全部完成<br/>回傳 (A, B, C)"]
        J2["Task B"] --> JR
        J3["Task C"] --> JR
    end

    subgraph "select! — 競爭執行"
        S1["Task A ✅（最快）"] --> SR["回傳最快的結果<br/>取消其餘"]
        S2["Task B ❌"] --> SR
        S3["Task C ❌"] --> SR
    end
```

```rust
use tokio::time::{sleep, timeout, Duration};

#[tokio::main]
async fn main() {
    // ======== tokio::join!：等待所有任務 ========
    let (user, orders, notifications) = tokio::join!(
        fetch_user(1),
        fetch_orders(1),
        fetch_notifications(1),
    );
    println!("使用者: {:?}, 訂單: {:?}, 通知: {:?}", user, orders, notifications);

    // ======== tokio::try_join!：任一失敗即中止 ========
    let result = tokio::try_join!(
        async { Ok::<_, String>("a".to_string()) },
        async { Ok::<_, String>("b".to_string()) },
    );
    match result {
        Ok((a, b)) => println!("{}, {}", a, b),
        Err(e) => eprintln!("錯誤: {}", e),
    }

    // ======== tokio::select!：競爭執行 ========
    tokio::select! {
        result = fetch_from_primary() => {
            println!("主要來源: {:?}", result);
        }
        result = fetch_from_secondary() => {
            println!("備用來源: {:?}", result);
        }
    }

    // ======== timeout：超時控制 ========
    match timeout(Duration::from_secs(5), slow_operation()).await {
        Ok(result) => println!("結果: {:?}", result),
        Err(_) => eprintln!("操作超時！"),
    }
}

async fn fetch_user(id: u64) -> String { format!("User-{}", id) }
async fn fetch_orders(user_id: u64) -> Vec<String> { vec![] }
async fn fetch_notifications(user_id: u64) -> Vec<String> { vec![] }
async fn fetch_from_primary() -> String { sleep(Duration::from_millis(100)).await; "primary".into() }
async fn fetch_from_secondary() -> String { sleep(Duration::from_millis(200)).await; "secondary".into() }
async fn slow_operation() -> String { sleep(Duration::from_secs(10)).await; "done".into() }
```

### 10.4 Stream 處理

```rust
use futures::stream::{self, StreamExt};
use tokio::sync::mpsc;

#[tokio::main]
async fn main() {
    // ======== 基本 Stream ========
    let stream = stream::iter(vec![1, 2, 3, 4, 5]);

    // map + collect
    let doubled: Vec<i32> = stream
        .map(|x| x * 2)
        .collect()
        .await;
    println!("{:?}", doubled);

    // ======== 並行 Stream 處理 ========
    let results: Vec<String> = stream::iter(0..10)
        .map(|i| async move {
            tokio::time::sleep(tokio::time::Duration::from_millis(100)).await;
            format!("結果-{}", i)
        })
        .buffer_unordered(5) // 最多 5 個並行
        .collect()
        .await;
    println!("{:?}", results);

    // ======== 從 Channel 建立 Stream ========
    let (tx, mut rx) = mpsc::channel::<i32>(100);

    tokio::spawn(async move {
        for i in 0..10 {
            tx.send(i).await.unwrap();
        }
    });

    while let Some(value) = rx.recv().await {
        println!("收到: {}", value);
    }
}
```

### 10.5 限流（Rate Limiting）與背壓（Backpressure）

```rust
use std::sync::Arc;
use tokio::sync::Semaphore;
use tokio::time::{sleep, Duration};

/// 使用 Semaphore 實作限流
async fn rate_limited_fetch(urls: Vec<String>, max_concurrent: usize) -> Vec<String> {
    let semaphore = Arc::new(Semaphore::new(max_concurrent));
    let mut handles = Vec::new();

    for url in urls {
        let permit = semaphore.clone().acquire_owned().await.unwrap();
        handles.push(tokio::spawn(async move {
            let result = fetch_url(&url).await;
            drop(permit); // 釋放 permit，允許下一個請求
            result
        }));
    }

    let mut results = Vec::new();
    for handle in handles {
        results.push(handle.await.unwrap());
    }
    results
}

async fn fetch_url(url: &str) -> String {
    sleep(Duration::from_millis(100)).await;
    format!("Response from {}", url)
}

/// Tower 限流中介層
use tower::ServiceBuilder;
use tower::limit::RateLimitLayer;

fn create_rate_limited_router() -> axum::Router {
    axum::Router::new()
        .route("/api/data", axum::routing::get(handler))
        .layer(
            ServiceBuilder::new()
                .layer(RateLimitLayer::new(100, Duration::from_secs(1))) // 每秒 100 請求
        )
}

async fn handler() -> &'static str { "OK" }
```

### 10.6 Graceful Shutdown

```rust
use tokio::signal;
use tokio::sync::broadcast;

#[tokio::main]
async fn main() {
    // 建立 shutdown 通知 channel
    let (shutdown_tx, _) = broadcast::channel::<()>(1);

    // 啟動伺服器
    let server_shutdown = shutdown_tx.subscribe();
    let server_handle = tokio::spawn(run_server(server_shutdown));

    // 啟動背景工作
    let worker_shutdown = shutdown_tx.subscribe();
    let worker_handle = tokio::spawn(run_background_worker(worker_shutdown));

    // 等待 shutdown 訊號
    shutdown_signal().await;
    println!("收到 shutdown 訊號，開始優雅關閉...");

    // 通知所有元件
    let _ = shutdown_tx.send(());

    // 等待所有元件關閉
    let _ = tokio::join!(server_handle, worker_handle);
    println!("所有元件已關閉");
}

async fn shutdown_signal() {
    let ctrl_c = async {
        signal::ctrl_c().await.expect("無法安裝 Ctrl+C handler");
    };

    #[cfg(unix)]
    let terminate = async {
        signal::unix::signal(signal::unix::SignalKind::terminate())
            .expect("無法安裝 SIGTERM handler")
            .recv()
            .await;
    };

    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();

    tokio::select! {
        _ = ctrl_c => {},
        _ = terminate => {},
    }
}

async fn run_server(mut shutdown: broadcast::Receiver<()>) {
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    let app = axum::Router::new();

    axum::serve(listener, app)
        .with_graceful_shutdown(async move {
            let _ = shutdown.recv().await;
        })
        .await
        .unwrap();

    println!("伺服器已關閉");
}

async fn run_background_worker(mut shutdown: broadcast::Receiver<()>) {
    loop {
        tokio::select! {
            _ = shutdown.recv() => {
                println!("背景工作收到 shutdown 訊號");
                break;
            }
            _ = tokio::time::sleep(tokio::time::Duration::from_secs(5)) => {
                println!("背景工作執行中...");
            }
        }
    }
    println!("背景工作已關閉");
}
```

### 10.7 Actor Model

Actor Model 是一種適合高併發的架構模式，每個 Actor 擁有獨立狀態，透過訊息傳遞溝通。

```rust
use tokio::sync::mpsc;

/// Actor 訊息定義
enum UserActorMessage {
    GetBalance { user_id: u64, reply: tokio::sync::oneshot::Sender<f64> },
    UpdateBalance { user_id: u64, amount: f64 },
}

/// User Actor：管理使用者餘額
struct UserActor {
    receiver: mpsc::Receiver<UserActorMessage>,
    balances: std::collections::HashMap<u64, f64>,
}

impl UserActor {
    fn new(receiver: mpsc::Receiver<UserActorMessage>) -> Self {
        Self { receiver, balances: std::collections::HashMap::new() }
    }

    async fn run(mut self) {
        while let Some(msg) = self.receiver.recv().await {
            match msg {
                UserActorMessage::GetBalance { user_id, reply } => {
                    let balance = self.balances.get(&user_id).copied().unwrap_or(0.0);
                    let _ = reply.send(balance);
                }
                UserActorMessage::UpdateBalance { user_id, amount } => {
                    *self.balances.entry(user_id).or_insert(0.0) += amount;
                }
            }
        }
    }
}

/// Actor Handle：對外提供類型安全的 API
#[derive(Clone)]
struct UserActorHandle {
    sender: mpsc::Sender<UserActorMessage>,
}

impl UserActorHandle {
    fn new() -> Self {
        let (sender, receiver) = mpsc::channel(256);
        let actor = UserActor::new(receiver);
        tokio::spawn(actor.run());
        Self { sender }
    }

    async fn get_balance(&self, user_id: u64) -> f64 {
        let (reply, rx) = tokio::sync::oneshot::channel();
        let _ = self.sender.send(UserActorMessage::GetBalance { user_id, reply }).await;
        rx.await.unwrap_or(0.0)
    }

    async fn update_balance(&self, user_id: u64, amount: f64) {
        let _ = self.sender.send(UserActorMessage::UpdateBalance { user_id, amount }).await;
    }
}
```

> 💡 **企業實務**：在生產環境中，可使用 `actix`（Actor 框架）或自行以 `mpsc` channel 實作輕量 Actor。Actor Model 特別適合管理共享狀態、連線池代理、工作排程器等場景。

### 10.8 高併發架構設計

```mermaid
graph TD
    LB[Load Balancer<br/>Nginx / HAProxy] --> S1[Rust Service 1]
    LB --> S2[Rust Service 2]
    LB --> S3[Rust Service N]

    S1 --> POOL[Connection Pool<br/>bb8 / deadpool]
    S2 --> POOL
    S3 --> POOL

    POOL --> DB[(PostgreSQL<br/>Read Replica)]
    POOL --> CACHE[(Redis Cluster)]

    S1 --> MQ[Message Queue<br/>NATS / Kafka]
    MQ --> WORKER[Background Workers]
```

**高併發設計要點：**

| 策略 | 說明 | Rust 工具 |
|------|------|----------|
| **連線池** | 重用資料庫 / Redis 連線 | `sqlx::PgPool`、`bb8`、`deadpool` |
| **非同步 I/O** | 避免阻塞執行緒 | `tokio`、`async/await` |
| **背壓控制** | 限制同時處理的請求數 | `tower::limit`、`Semaphore` |
| **批次處理** | 合併多個小請求 | `tokio::sync::mpsc` + buffer |
| **快取策略** | 減少資料庫查詢 | Redis + `moka`（本地快取） |
| **水平擴展** | 無狀態服務 + K8s HPA | Kubernetes + Prometheus |

---

## 11. WebAssembly（WASM）

### 11.1 WASM 概念

```mermaid
graph LR
    RUST["Rust 原始碼<br/>(.rs)"] --> COMPILER["wasm-pack<br/>（編譯器）"]
    COMPILER --> WASM[".wasm 模組"]
    COMPILER --> JS["JS 綁定<br/>（.js）"]
    COMPILER --> TS["TypeScript 定義<br/>（.d.ts）"]

    WASM --> BROWSER["瀏覽器"]
    WASM --> NODE["Node.js"]
    WASM --> EDGE["Edge Computing<br/>（Cloudflare Workers）"]

    JS --> BROWSER
    JS --> NODE
```

### 11.2 wasm-pack 建置

```bash
# 安裝 wasm-pack
curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
# 或
cargo install wasm-pack

# 安裝 wasm32 target
rustup target add wasm32-unknown-unknown

# 建立 wasm 專案
cargo new --lib my-wasm-lib
```

```toml
# Cargo.toml
[package]
name = "my-wasm-lib"
version = "0.1.0"
edition = "2024"

[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
wasm-bindgen = "0.2"
js-sys = "0.3"
web-sys = { version = "0.3", features = ["console", "Document", "Element", "HtmlElement", "Window"] }
serde = { version = "1", features = ["derive"] }
serde-wasm-bindgen = "0.6"
```

```rust
// src/lib.rs
use wasm_bindgen::prelude::*;

// 從 JS 匯入函式
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);
}

/// 匯出給 JS 呼叫的函式
#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    let greeting = format!("Hello, {}! 來自 Rust WASM", name);
    log(&greeting);
    greeting
}

/// 匯出結構體
#[wasm_bindgen]
pub struct Calculator {
    history: Vec<f64>,
}

#[wasm_bindgen]
impl Calculator {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Calculator {
        Calculator { history: Vec::new() }
    }

    pub fn add(&mut self, a: f64, b: f64) -> f64 {
        let result = a + b;
        self.history.push(result);
        result
    }

    pub fn multiply(&mut self, a: f64, b: f64) -> f64 {
        let result = a * b;
        self.history.push(result);
        result
    }

    pub fn get_history(&self) -> Vec<f64> {
        self.history.clone()
    }
}

/// 高效能運算範例：費波那契數列
#[wasm_bindgen]
pub fn fibonacci(n: u32) -> u64 {
    if n <= 1 {
        return n as u64;
    }
    let mut a: u64 = 0;
    let mut b: u64 = 1;
    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    b
}
```

```bash
# 建置（產生 npm 套件）
wasm-pack build --target web      # 瀏覽器直接使用
wasm-pack build --target bundler  # 搭配 Webpack/Vite
wasm-pack build --target nodejs   # Node.js
```

### 11.3 在前端使用 WASM

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Rust WASM Demo</title>
</head>
<body>
    <h1>Rust WASM 範例</h1>
    <div id="output"></div>

    <script type="module">
        import init, { greet, Calculator, fibonacci } from './pkg/my_wasm_lib.js';

        async function main() {
            await init();

            // 呼叫 Rust 函式
            const greeting = greet("World");
            document.getElementById('output').textContent = greeting;

            // 使用 Rust 結構體
            const calc = new Calculator();
            console.log('1 + 2 =', calc.add(1, 2));
            console.log('3 * 4 =', calc.multiply(3, 4));

            // 效能比較
            console.time('WASM Fibonacci');
            const result = fibonacci(40);
            console.timeEnd('WASM Fibonacci');
            console.log('fibonacci(40) =', result);
        }

        main();
    </script>
</body>
</html>
```

### 11.4 WASM 使用場景

| 場景 | 說明 | 適合度 |
|------|------|--------|
| **影像/音訊處理** | 濾鏡、轉碼、編輯 | ⭐⭐⭐⭐⭐ |
| **遊戲引擎** | 物理模擬、渲染邏輯 | ⭐⭐⭐⭐⭐ |
| **加密/雜湊** | 客戶端加密運算 | ⭐⭐⭐⭐⭐ |
| **資料處理** | CSV/JSON 大量處理 | ⭐⭐⭐⭐ |
| **科學計算** | 矩陣運算、模擬 | ⭐⭐⭐⭐⭐ |
| **Edge Computing** | Cloudflare Workers | ⭐⭐⭐⭐ |
| **一般 DOM 操作** | 簡單 UI 互動 | ⭐⭐（不建議） |
| **簡單 CRUD** | 表單驗證等 | ⭐（不建議） |

> 💡 **實務建議**：WASM 適合 **CPU 密集型** 操作。對於一般的 DOM 操作和 AJAX 請求，JavaScript 仍然是更好的選擇。將效能關鍵路徑用 Rust/WASM 實作，其餘保留 JavaScript。

### 11.5 Rust + React 整合範例

```bash
# 建立 React + Rust WASM 專案
npx create-react-app my-app
cd my-app
mkdir wasm-lib && cd wasm-lib
cargo init --lib
# 在 wasm-lib/Cargo.toml 加入 wasm-bindgen 依賴
wasm-pack build --target bundler
cd .. && npm install ./wasm-lib/pkg
```

```jsx
// src/App.jsx — React 元件中使用 Rust WASM
import React, { useState, useEffect } from 'react';

function App() {
    const [wasm, setWasm] = useState(null);
    const [result, setResult] = useState('');

    useEffect(() => {
        // 動態載入 WASM 模組
        import('my-wasm-lib').then(module => {
            setWasm(module);
        });
    }, []);

    const handleCompute = () => {
        if (wasm) {
            const start = performance.now();
            const fib = wasm.fibonacci(45);
            const elapsed = (performance.now() - start).toFixed(2);
            setResult(`fibonacci(45) = ${fib}（耗時 ${elapsed}ms）`);
        }
    };

    return (
        <div>
            <h1>React + Rust WASM</h1>
            <button onClick={handleCompute}>計算 Fibonacci</button>
            <p>{result}</p>
        </div>
    );
}

export default App;
```

> 💡 **最佳實務**：將 WASM 模組以 `lazy import` 方式載入，避免阻塞首次頁面渲染。僅在需要高效能計算時載入 WASM。

### 11.6 WASM 效能優化

| 優化策略 | 說明 | 工具/方法 |
|---------|------|----------|
| **wasm-opt** | LLVM 後端最佳化 WASM 二進位 | `wasm-opt -O3 input.wasm -o output.wasm` |
| **縮小體積** | 移除 debug 資訊 | `wasm-pack build --release` |
| **Lazy Loading** | 按需載入 WASM 模組 | 動態 `import()` |
| **SharedArrayBuffer** | 多執行緒 WASM | `wasm-bindgen-rayon` |
| **SIMD** | 向量化運算加速 | `std::arch::wasm32` intrinsics |
| **避免頻繁跨界** | 減少 JS ↔ WASM 呼叫次數 | 批次操作、傳遞 typed arrays |
| **記憶體管理** | 預分配記憶體 | `wee_alloc`（極小配置器） |

```toml
# Cargo.toml — WASM 體積最佳化
[profile.release]
opt-level = "s"          # 最佳化體積（"z" 更小但更慢）
lto = true
codegen-units = 1
strip = true

[dependencies]
wee_alloc = "0.4"        # 極小的記憶體配置器（約 1KB）
```

```rust
// 使用 wee_alloc 減少 WASM 體積
#[cfg(target_arch = "wasm32")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;
```

---

## 12. 系統架構設計

### 12.1 Clean Architecture

```mermaid
graph TD
    subgraph "外層（框架與驅動程式）"
        WEB["Web Framework<br/>（Axum）"]
        DB["Database<br/>（PostgreSQL）"]
        CACHE["Cache<br/>（Redis）"]
        MQ["Message Queue<br/>（RabbitMQ）"]
    end

    subgraph "介面適配層（Interface Adapters）"
        CTRL["Controllers<br/>（API Handlers）"]
        REPO_IMPL["Repository Impl"]
        PRES["Presenters<br/>（DTO 轉換）"]
    end

    subgraph "應用層（Use Cases）"
        UC["Use Cases<br/>（Service Layer）"]
    end

    subgraph "核心層（Entities）"
        ENT["Domain Entities"]
        VO["Value Objects"]
        REPO_TRAIT["Repository Traits"]
    end

    WEB --> CTRL
    CTRL --> UC
    UC --> ENT
    UC --> REPO_TRAIT
    REPO_IMPL --> REPO_TRAIT
    REPO_IMPL --> DB
    REPO_IMPL --> CACHE

    style ENT fill:#4CAF50,color:white
    style VO fill:#4CAF50,color:white
    style REPO_TRAIT fill:#4CAF50,color:white
    style UC fill:#2196F3,color:white
    style CTRL fill:#FF9800,color:white
    style PRES fill:#FF9800,color:white
    style REPO_IMPL fill:#FF9800,color:white
```

```rust
// ======== Domain Layer（核心層）========

// domain/user.rs
#[derive(Debug, Clone)]
pub struct User {
    pub id: uuid::Uuid,
    pub username: Username,
    pub email: Email,
    pub password_hash: String,
    pub role: Role,
    pub active: bool,
}

// Value Object：使用者名稱
#[derive(Debug, Clone)]
pub struct Username(String);

impl Username {
    pub fn new(value: &str) -> Result<Self, DomainError> {
        if value.len() < 3 || value.len() > 50 {
            return Err(DomainError::InvalidUsername);
        }
        Ok(Self(value.to_string()))
    }

    pub fn as_str(&self) -> &str {
        &self.0
    }
}

// Value Object：電子郵件
#[derive(Debug, Clone)]
pub struct Email(String);

impl Email {
    pub fn new(value: &str) -> Result<Self, DomainError> {
        if !value.contains('@') {
            return Err(DomainError::InvalidEmail);
        }
        Ok(Self(value.to_lowercase()))
    }
}

// Repository Trait（核心層定義介面）
#[async_trait::async_trait]
pub trait UserRepository: Send + Sync {
    async fn find_by_id(&self, id: uuid::Uuid) -> Result<Option<User>, DomainError>;
    async fn find_by_username(&self, username: &str) -> Result<Option<User>, DomainError>;
    async fn save(&self, user: &User) -> Result<User, DomainError>;
    async fn delete(&self, id: uuid::Uuid) -> Result<bool, DomainError>;
}

// ======== Application Layer（應用層）========

// service/user_service.rs
pub struct UserService<R: UserRepository> {
    repo: R,
}

impl<R: UserRepository> UserService<R> {
    pub fn new(repo: R) -> Self {
        Self { repo }
    }

    pub async fn create_user(&self, cmd: CreateUserCommand) -> Result<User, AppError> {
        let username = Username::new(&cmd.username)?;
        let email = Email::new(&cmd.email)?;

        if self.repo.find_by_username(username.as_str()).await?.is_some() {
            return Err(AppError::Conflict("使用者名稱已存在".into()));
        }

        let user = User {
            id: uuid::Uuid::new_v4(),
            username,
            email,
            password_hash: hash_password(&cmd.password)?,
            role: Role::User,
            active: true,
        };

        self.repo.save(&user).await.map_err(Into::into)
    }
}
```

### 12.2 Hexagonal Architecture（六角架構）

```mermaid
graph LR
    subgraph "外部世界"
        HTTP["HTTP Client"]
        CLI["CLI"]
        GRPC["gRPC Client"]
    end

    subgraph "入站適配器（Driving）"
        REST["REST API Adapter"]
        CMD["CLI Adapter"]
        GRPC_IN["gRPC Adapter"]
    end

    subgraph "入站埠"
        IP["Port: UseCase Trait"]
    end

    subgraph "核心領域"
        DOMAIN["Domain Logic"]
    end

    subgraph "出站埠"
        OP["Port: Repository Trait"]
    end

    subgraph "出站適配器（Driven）"
        PG["PostgreSQL Adapter"]
        REDIS["Redis Adapter"]
        KAFKA["Kafka Adapter"]
    end

    HTTP --> REST --> IP --> DOMAIN --> OP --> PG
    CLI --> CMD --> IP
    GRPC --> GRPC_IN --> IP
    OP --> REDIS
    OP --> KAFKA

    style DOMAIN fill:#4CAF50,color:white
    style IP fill:#2196F3,color:white
    style OP fill:#2196F3,color:white
```

```rust
// 六角架構的 Rust 實作

// ======== Port（入站）========
#[async_trait::async_trait]
pub trait CreateOrderUseCase: Send + Sync {
    async fn execute(&self, cmd: CreateOrderCommand) -> Result<Order, AppError>;
}

// ======== Port（出站）========
#[async_trait::async_trait]
pub trait OrderRepository: Send + Sync {
    async fn save(&self, order: &Order) -> Result<Order, RepositoryError>;
    async fn find_by_id(&self, id: uuid::Uuid) -> Result<Option<Order>, RepositoryError>;
}

#[async_trait::async_trait]
pub trait EventPublisher: Send + Sync {
    async fn publish(&self, event: DomainEvent) -> Result<(), PublishError>;
}

// ======== 核心領域 ========
pub struct OrderService {
    order_repo: Arc<dyn OrderRepository>,
    event_publisher: Arc<dyn EventPublisher>,
}

#[async_trait::async_trait]
impl CreateOrderUseCase for OrderService {
    async fn execute(&self, cmd: CreateOrderCommand) -> Result<Order, AppError> {
        let order = Order::new(cmd.customer_id, cmd.items)?;
        let saved = self.order_repo.save(&order).await?;
        self.event_publisher.publish(DomainEvent::OrderCreated(saved.id)).await?;
        Ok(saved)
    }
}

// ======== 出站適配器 ========
pub struct PgOrderRepository {
    pool: sqlx::PgPool,
}

#[async_trait::async_trait]
impl OrderRepository for PgOrderRepository {
    async fn save(&self, order: &Order) -> Result<Order, RepositoryError> {
        // PostgreSQL 實作
        todo!()
    }

    async fn find_by_id(&self, id: uuid::Uuid) -> Result<Option<Order>, RepositoryError> {
        todo!()
    }
}
```

### 12.3 微服務架構

```mermaid
graph TD
    GW["API Gateway<br/>（Envoy / Traefik）"] --> US["User Service<br/>（Rust / Axum）"]
    GW --> OS["Order Service<br/>（Rust / Axum）"]
    GW --> PS["Payment Service<br/>（Rust / Axum）"]
    GW --> NS["Notification Service<br/>（Rust / Axum）"]

    US --> DB1[(PostgreSQL)]
    OS --> DB2[(PostgreSQL)]
    PS --> DB3[(PostgreSQL)]

    US --> MQ["Message Broker<br/>（RabbitMQ / Kafka）"]
    OS --> MQ
    PS --> MQ
    NS --> MQ

    US --> CACHE["Redis"]
    OS --> CACHE

    subgraph "可觀測性"
        TRACE["Jaeger<br/>（分散式追蹤）"]
        METRICS["Prometheus<br/>（指標收集）"]
        LOGS["Loki<br/>（日誌聚合）"]
    end

    US --> TRACE
    OS --> TRACE
    PS --> TRACE
```

### 12.4 事件驅動架構

```rust
use serde::{Deserialize, Serialize};
use chrono::{DateTime, Utc};

/// 領域事件
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum DomainEvent {
    UserCreated {
        user_id: uuid::Uuid,
        username: String,
        timestamp: DateTime<Utc>,
    },
    OrderPlaced {
        order_id: uuid::Uuid,
        user_id: uuid::Uuid,
        total: f64,
        timestamp: DateTime<Utc>,
    },
    PaymentCompleted {
        payment_id: uuid::Uuid,
        order_id: uuid::Uuid,
        amount: f64,
        timestamp: DateTime<Utc>,
    },
}

/// 事件處理器 Trait
#[async_trait::async_trait]
pub trait EventHandler: Send + Sync {
    async fn handle(&self, event: &DomainEvent) -> Result<(), anyhow::Error>;
}

/// 事件匯流排
pub struct EventBus {
    handlers: Vec<Box<dyn EventHandler>>,
}

impl EventBus {
    pub fn new() -> Self {
        Self { handlers: Vec::new() }
    }

    pub fn register(&mut self, handler: Box<dyn EventHandler>) {
        self.handlers.push(handler);
    }

    pub async fn publish(&self, event: &DomainEvent) -> Result<(), anyhow::Error> {
        for handler in &self.handlers {
            handler.handle(event).await?;
        }
        Ok(())
    }
}

/// 事件處理器範例：發送通知
pub struct NotificationHandler;

#[async_trait::async_trait]
impl EventHandler for NotificationHandler {
    async fn handle(&self, event: &DomainEvent) -> Result<(), anyhow::Error> {
        match event {
            DomainEvent::OrderPlaced { order_id, user_id, .. } => {
                tracing::info!("訂單 {} 已建立，通知使用者 {}", order_id, user_id);
                // 發送通知邏輯...
            }
            _ => {}
        }
        Ok(())
    }
}
```

### 12.5 CQRS（命令與查詢責任分離）

```rust
// ======== Command（寫入端）========
#[derive(Debug)]
pub struct CreateOrderCommand {
    pub customer_id: uuid::Uuid,
    pub items: Vec<OrderItem>,
}

#[async_trait::async_trait]
pub trait CommandHandler<C> {
    type Output;
    async fn handle(&self, command: C) -> Result<Self::Output, AppError>;
}

pub struct CreateOrderHandler {
    repo: Arc<dyn OrderRepository>,
    event_bus: Arc<EventBus>,
}

#[async_trait::async_trait]
impl CommandHandler<CreateOrderCommand> for CreateOrderHandler {
    type Output = uuid::Uuid;

    async fn handle(&self, cmd: CreateOrderCommand) -> Result<Self::Output, AppError> {
        let order = Order::new(cmd.customer_id, cmd.items)?;
        let saved = self.repo.save(&order).await?;
        self.event_bus.publish(&DomainEvent::OrderPlaced {
            order_id: saved.id,
            user_id: cmd.customer_id,
            total: saved.total,
            timestamp: chrono::Utc::now(),
        }).await?;
        Ok(saved.id)
    }
}

// ======== Query（讀取端）========
#[derive(Debug)]
pub struct GetOrderQuery {
    pub order_id: uuid::Uuid,
}

#[async_trait::async_trait]
pub trait QueryHandler<Q> {
    type Output;
    async fn handle(&self, query: Q) -> Result<Self::Output, AppError>;
}

pub struct GetOrderHandler {
    read_repo: Arc<dyn OrderReadRepository>, // 可以是不同的資料來源（如 ReadReplica）
}

#[async_trait::async_trait]
impl QueryHandler<GetOrderQuery> for GetOrderHandler {
    type Output = OrderDto;

    async fn handle(&self, query: GetOrderQuery) -> Result<Self::Output, AppError> {
        self.read_repo
            .find_by_id(query.order_id)
            .await?
            .ok_or_else(|| AppError::NotFound("訂單不存在".into()))
    }
}
```

### 12.6 架構比較

| 架構 | 複雜度 | 適用規模 | 優點 | 缺點 |
|------|--------|---------|------|------|
| **Clean Architecture** | 中 | 中～大型 | 依賴反轉、可測試 | 較多分層 |
| **Hexagonal** | 中高 | 中～大型 | 埠/適配器清晰分離 | 抽象較多 |
| **微服務** | 高 | 大型/分散式 | 獨立部署、可擴展 | 維運複雜 |
| **事件驅動** | 高 | 中～大型 | 鬆耦合、非同步 | 最終一致性挑戰 |
| **CQRS** | 高 | 大型 | 讀寫分離最佳化 | 同步複雜度增加 |
| **Monolith** | 低 | 小～中型 | 簡單、易部署 | 擴展性有限 |

> 💡 **選型建議**：
> - 新專案/小團隊 → **Clean Architecture**（Monolith）
> - 中型團隊/需要彈性 → **Hexagonal + 模組化 Monolith**
> - 大型團隊/高擴展需求 → **微服務 + 事件驅動**

### 12.7 模組拆分策略

在 Rust 中，使用 Cargo Workspace 進行模組拆分是企業級專案的標準做法：

```
enterprise-app/
├── Cargo.toml            # workspace 根
├── crates/
│   ├── domain/           # 領域模型（零外部依賴）
│   │   └── src/lib.rs
│   ├── application/      # 應用服務（依賴 domain）
│   │   └── src/lib.rs
│   ├── infrastructure/   # 基礎設施（DB、Redis、MQ）
│   │   └── src/lib.rs
│   ├── api/              # HTTP API 層
│   │   └── src/lib.rs
│   └── shared/           # 共用工具（錯誤型別、常數）
│       └── src/lib.rs
└── src/main.rs           # 入口
```

**拆分原則：**

| 原則 | 說明 |
|------|------|
| **依賴方向** | 外層依賴內層：`api → application → domain`，反向禁止 |
| **單一職責** | 每個 crate 只負責一個關注點 |
| **介面隔離** | 跨 crate 邊界使用 trait 定義介面 |
| **編譯效率** | 修改 `api` crate 時，`domain` 不需要重新編譯 |
| **獨立測試** | 每個 crate 可獨立執行 `cargo test -p <crate>` |

```toml
# Cargo.toml（workspace 根）
[workspace]
members = ["crates/*"]
resolver = "2"

[workspace.dependencies]
serde = { version = "1", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
uuid = { version = "1", features = ["v4", "serde"] }

# crates/domain/Cargo.toml
[package]
name = "domain"
version.workspace = true

[dependencies]
serde.workspace = true
uuid.workspace = true
# domain 層不依賴任何基礎設施 crate
```

---

## 13. Docker 與 Kubernetes

### 13.1 Dockerfile 最佳實務

```dockerfile
# ======== 最佳化的多階段建置 ========

# Stage 1: 使用 chef 快取依賴編譯
FROM rust:1.95-bookworm AS chef
RUN cargo install cargo-chef
WORKDIR /app

# Stage 2: 準備依賴清單
FROM chef AS planner
COPY . .
RUN cargo chef prepare --recipe-path recipe.json

# Stage 3: 建置依賴（利用 Docker layer cache）
FROM chef AS builder
COPY --from=planner /app/recipe.json recipe.json
RUN cargo chef cook --release --recipe-path recipe.json

# 建置應用
COPY . .
RUN cargo build --release

# Stage 4: 執行環境
FROM debian:bookworm-slim AS runtime

# 安裝最小必要套件
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 安全性：非 root 使用者
RUN groupadd -r app && useradd -r -g app -d /app -s /sbin/nologin app

WORKDIR /app

COPY --from=builder /app/target/release/enterprise-api .
COPY --from=builder /app/migrations ./migrations
COPY --from=builder /app/config ./config

RUN chown -R app:app /app
USER app

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

ENTRYPOINT ["./enterprise-api"]
```

**使用靜態連結（Musl）的極小 Image：**

```dockerfile
FROM rust:1.95-bookworm AS builder
RUN rustup target add x86_64-unknown-linux-musl
RUN apt-get update && apt-get install -y musl-tools

WORKDIR /app
COPY . .
RUN cargo build --release --target x86_64-unknown-linux-musl

# 使用 scratch（零依賴 image）
FROM scratch
COPY --from=builder /app/target/x86_64-unknown-linux-musl/release/enterprise-api /
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
EXPOSE 3000
ENTRYPOINT ["/enterprise-api"]
# 最終 image 大小可以小於 10MB
```

### 13.2 Docker Compose 企業配置

```yaml
# docker-compose.yml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgres://postgres:${DB_PASSWORD}@db:5432/enterprise
      REDIS_URL: redis://cache:6379
      JWT_SECRET: ${JWT_SECRET}
      RUST_LOG: info,sqlx=warn
      APP_ENV: production
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_healthy
      migrate:
        condition: service_completed_successfully
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 128M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
    networks:
      - backend

  migrate:
    build:
      context: .
      target: builder
    command: ["sqlx", "migrate", "run"]
    environment:
      DATABASE_URL: postgres://postgres:${DB_PASSWORD}@db:5432/enterprise
    depends_on:
      db:
        condition: service_healthy
    networks:
      - backend

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: enterprise
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - backend

  cache:
    image: redis:7-alpine
    command: redis-server --appendonly yes --maxmemory 256mb --maxmemory-policy allkeys-lru
    volumes:
      - redisdata:/data
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 3
    networks:
      - backend

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./config/prometheus.yml:/etc/prometheus/prometheus.yml
      - promdata:/prometheus
    ports:
      - "9090:9090"
    networks:
      - backend

  grafana:
    image: grafana/grafana:latest
    environment:
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_PASSWORD:-admin}
    volumes:
      - grafanadata:/var/lib/grafana
    ports:
      - "3001:3000"
    depends_on:
      - prometheus
    networks:
      - backend

volumes:
  pgdata:
  redisdata:
  promdata:
  grafanadata:

networks:
  backend:
    driver: bridge
```

### 13.3 Kubernetes 部署

```yaml
# k8s/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: enterprise
  labels:
    app: enterprise-api
---
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
  namespace: enterprise
data:
  RUST_LOG: "info,sqlx=warn"
  APP_ENV: "production"
---
# k8s/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: api-secrets
  namespace: enterprise
type: Opaque
data:
  DATABASE_URL: cG9zdGdyZXM6Ly91c2VyOnBhc3NAcGctc2VydmljZTo1NDMyL2VudGVycHJpc2U=
  JWT_SECRET: c3VwZXItc2VjcmV0LWtleQ==
  REDIS_URL: cmVkaXM6Ly9yZWRpcy1zZXJ2aWNlOjYzNzk=
---
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: enterprise-api
  namespace: enterprise
  labels:
    app: enterprise-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: enterprise-api
  template:
    metadata:
      labels:
        app: enterprise-api
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "3000"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: enterprise-api
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
      containers:
        - name: api
          image: ghcr.io/company/enterprise-api:latest
          ports:
            - containerPort: 3000
              name: http
          envFrom:
            - configMapRef:
                name: api-config
            - secretRef:
                name: api-secrets
          resources:
            requests:
              cpu: 250m
              memory: 128Mi
            limits:
              cpu: "1"
              memory: 512Mi
          readinessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 15
            periodSeconds: 20
          startupProbe:
            httpGet:
              path: /health
              port: 3000
            failureThreshold: 30
            periodSeconds: 10
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: kubernetes.io/hostname
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app: enterprise-api
---
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: enterprise-api
  namespace: enterprise
spec:
  selector:
    app: enterprise-api
  ports:
    - port: 80
      targetPort: 3000
      protocol: TCP
  type: ClusterIP
---
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: enterprise-api
  namespace: enterprise
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: enterprise-api
  minReplicas: 3
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 30
      policies:
        - type: Pods
          value: 2
          periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Pods
          value: 1
          periodSeconds: 60
---
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: enterprise-api
  namespace: enterprise
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/rate-limit: "100"
    nginx.ingress.kubernetes.io/rate-limit-window: "1m"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - api.company.com
      secretName: api-tls
  rules:
    - host: api.company.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: enterprise-api
                port:
                  number: 80
```

### 13.4 Helm Chart 結構

```
helm/enterprise-api/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-staging.yaml
├── values-prod.yaml
├── templates/
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── configmap.yaml
│   └── secret.yaml
```

```yaml
# values.yaml
replicaCount: 3

image:
  repository: ghcr.io/company/enterprise-api
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80
  targetPort: 3000

resources:
  requests:
    cpu: 250m
    memory: 128Mi
  limits:
    cpu: "1"
    memory: 512Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 20
  targetCPUUtilization: 70

ingress:
  enabled: true
  host: api.company.com
  tls: true
```

```bash
# Helm 操作
helm install enterprise-api ./helm/enterprise-api -f values-prod.yaml
helm upgrade enterprise-api ./helm/enterprise-api -f values-prod.yaml
helm rollback enterprise-api 1
```

### 13.5 Service / Ingress / ConfigMap / Secret

> 上述 13.3 節中已展示 Service、Ingress 與 HPA 的完整 YAML 範例。以下補充 ConfigMap 與 Secret 的最佳實務。

```yaml
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: enterprise-api-config
  namespace: enterprise
data:
  APP__SERVER__HOST: "0.0.0.0"
  APP__SERVER__PORT: "3000"
  APP__LOGGING__LEVEL: "info"
  APP__LOGGING__FORMAT: "json"
  RUST_BACKTRACE: "1"
---
# k8s/secret.yaml（生產環境建議使用 External Secrets Operator）
apiVersion: v1
kind: Secret
metadata:
  name: enterprise-api-secret
  namespace: enterprise
type: Opaque
stringData:
  APP__DATABASE__URL: "postgresql://user:pass@db:5432/enterprise"
  APP__AUTH__JWT_SECRET: "change-me-in-production"
```

> ⚠️ **安全注意**：生產環境中**禁止**將密鑰直接寫入 Secret YAML。應使用 **External Secrets Operator**、**HashiCorp Vault** 或雲端 Secret Manager 動態注入。

### 13.6 HPA 自動擴展

> HPA 完整範例已在 13.3 節中展示。以下為自訂指標擴展的進階模式：

```yaml
# 基於 Prometheus 自訂指標的 HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: enterprise-api-custom
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: enterprise-api
  minReplicas: 3
  maxReplicas: 30
  metrics:
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second  # 自訂 Prometheus 指標
        target:
          type: AverageValue
          averageValue: "1000"           # 每個 Pod 平均 1000 RPS
```

---

## 14. 測試策略

### 14.1 單元測試

```rust
// src/service/user_service.rs

#[cfg(test)]
mod tests {
    use super::*;
    use mockall::predicate::*;
    use mockall::mock;

    // 使用 mockall 產生 Mock
    mock! {
        pub UserRepo {}

        #[async_trait::async_trait]
        impl UserRepository for UserRepo {
            async fn find_by_id(&self, id: uuid::Uuid) -> Result<Option<User>, DomainError>;
            async fn find_by_username(&self, username: &str) -> Result<Option<User>, DomainError>;
            async fn save(&self, user: &User) -> Result<User, DomainError>;
            async fn delete(&self, id: uuid::Uuid) -> Result<bool, DomainError>;
        }
    }

    fn create_test_user() -> User {
        User {
            id: uuid::Uuid::new_v4(),
            username: Username::new("testuser").unwrap(),
            email: Email::new("test@example.com").unwrap(),
            password_hash: "hashed".to_string(),
            role: Role::User,
            active: true,
        }
    }

    #[tokio::test]
    async fn test_create_user_success() {
        let mut mock_repo = MockUserRepo::new();

        // 設定期望
        mock_repo
            .expect_find_by_username()
            .with(eq("newuser"))
            .times(1)
            .returning(|_| Ok(None)); // 使用者不存在

        mock_repo
            .expect_save()
            .times(1)
            .returning(|user| Ok(user.clone()));

        let service = UserService::new(mock_repo);
        let cmd = CreateUserCommand {
            username: "newuser".to_string(),
            email: "new@example.com".to_string(),
            password: "secure_password_123".to_string(),
        };

        let result = service.create_user(cmd).await;
        assert!(result.is_ok());

        let user = result.unwrap();
        assert_eq!(user.username.as_str(), "newuser");
    }

    #[tokio::test]
    async fn test_create_user_duplicate_username() {
        let mut mock_repo = MockUserRepo::new();

        mock_repo
            .expect_find_by_username()
            .with(eq("existing"))
            .times(1)
            .returning(|_| Ok(Some(create_test_user()))); // 使用者已存在

        let service = UserService::new(mock_repo);
        let cmd = CreateUserCommand {
            username: "existing".to_string(),
            email: "dup@example.com".to_string(),
            password: "password123".to_string(),
        };

        let result = service.create_user(cmd).await;
        assert!(matches!(result, Err(AppError::Conflict(_))));
    }
}
```

### 14.2 整合測試

```rust
// tests/api_tests.rs
use axum::body::Body;
use axum::http::{Request, StatusCode};
use tower::ServiceExt; // for `oneshot`
use serde_json::json;

// 測試工具
async fn setup_test_app() -> axum::Router {
    // 使用測試用資料庫
    let database_url = std::env::var("TEST_DATABASE_URL")
        .unwrap_or("postgres://postgres:postgres@localhost:5432/test_db".to_string());

    let pool = sqlx::PgPool::connect(&database_url).await.unwrap();

    // 執行遷移
    sqlx::migrate!("./migrations").run(&pool).await.unwrap();

    // 建立應用狀態與路由
    let state = AppState::new(pool).await;
    create_router(state)
}

#[tokio::test]
async fn test_health_check() {
    let app = setup_test_app().await;

    let response = app
        .oneshot(
            Request::builder()
                .uri("/health")
                .body(Body::empty())
                .unwrap()
        )
        .await
        .unwrap();

    assert_eq!(response.status(), StatusCode::OK);
}

#[tokio::test]
async fn test_create_user_api() {
    let app = setup_test_app().await;

    let body = json!({
        "username": "testuser",
        "email": "test@example.com",
        "password": "secure_password_123"
    });

    let response = app
        .oneshot(
            Request::builder()
                .method("POST")
                .uri("/api/v1/users")
                .header("Content-Type", "application/json")
                .body(Body::from(serde_json::to_string(&body).unwrap()))
                .unwrap()
        )
        .await
        .unwrap();

    assert_eq!(response.status(), StatusCode::CREATED);

    let body = axum::body::to_bytes(response.into_body(), usize::MAX).await.unwrap();
    let user: serde_json::Value = serde_json::from_slice(&body).unwrap();
    assert_eq!(user["username"], "testuser");
}

#[tokio::test]
async fn test_unauthorized_access() {
    let app = setup_test_app().await;

    let response = app
        .oneshot(
            Request::builder()
                .uri("/api/v1/users")
                .body(Body::empty())
                .unwrap()
        )
        .await
        .unwrap();

    assert_eq!(response.status(), StatusCode::UNAUTHORIZED);
}
```

### 14.3 屬性測試（Property-Based Testing）

```rust
use proptest::prelude::*;

// 使用 proptest 做屬性測試
proptest! {
    #[test]
    fn test_username_validation(s in "[a-zA-Z0-9]{3,50}") {
        // 3-50 個英數字元都應該是合法的使用者名稱
        let result = Username::new(&s);
        prop_assert!(result.is_ok());
    }

    #[test]
    fn test_username_too_short(s in "[a-zA-Z0-9]{0,2}") {
        // 少於 3 個字元應該驗證失敗
        let result = Username::new(&s);
        prop_assert!(result.is_err());
    }

    #[test]
    fn test_email_must_contain_at(s in "[a-zA-Z0-9]+") {
        // 不含 @ 的字串不應該是合法 email
        if !s.contains('@') {
            let result = Email::new(&s);
            prop_assert!(result.is_err());
        }
    }
}
```

### 14.4 效能測試

```rust
// benches/api_benchmark.rs
use criterion::{black_box, criterion_group, criterion_main, Criterion, BenchmarkId};

fn fibonacci(n: u64) -> u64 {
    match n {
        0 | 1 => n,
        _ => {
            let mut a = 0u64;
            let mut b = 1u64;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

fn benchmark_fibonacci(c: &mut Criterion) {
    let mut group = c.benchmark_group("fibonacci");

    for size in [10, 20, 30, 40, 50].iter() {
        group.bench_with_input(
            BenchmarkId::from_parameter(size),
            size,
            |b, &size| {
                b.iter(|| fibonacci(black_box(size)));
            },
        );
    }

    group.finish();
}

fn benchmark_serialization(c: &mut Criterion) {
    let user = UserResponse {
        id: uuid::Uuid::new_v4(),
        username: "benchmark_user".to_string(),
        email: "bench@example.com".to_string(),
        active: true,
        created_at: chrono::Utc::now().naive_utc(),
    };

    c.bench_function("serialize_user", |b| {
        b.iter(|| serde_json::to_string(black_box(&user)).unwrap())
    });

    let json = serde_json::to_string(&user).unwrap();
    c.bench_function("deserialize_user", |b| {
        b.iter(|| serde_json::from_str::<UserResponse>(black_box(&json)).unwrap())
    });
}

criterion_group!(benches, benchmark_fibonacci, benchmark_serialization);
criterion_main!(benches);
```

```bash
# 執行效能測試
cargo bench

# 執行特定 benchmark
cargo bench -- fibonacci

# 產生 HTML 報告
# 報告位於 target/criterion/
```

### 14.5 測試金字塔

```mermaid
graph TB
    subgraph "測試金字塔"
        E2E["E2E 測試<br/>（少量）<br/>完整流程驗證"]
        INT["整合測試<br/>（適量）<br/>API + 資料庫"]
        UNIT["單元測試<br/>（大量）<br/>業務邏輯"]
    end

    E2E --> |"慢、高成本"| INT
    INT --> |"中速、中等成本"| UNIT

    style E2E fill:#f44336,color:white
    style INT fill:#FF9800,color:white
    style UNIT fill:#4CAF50,color:white
```

| 測試類型 | 涵蓋範圍 | 速度 | 數量 | 工具 |
|---------|---------|------|------|------|
| **單元測試** | 函式/方法邏輯 | 快 | 多 | `#[test]`, mockall |
| **整合測試** | API + DB | 中 | 適量 | testcontainers, sqlx |
| **屬性測試** | 邊界條件 | 中 | 適量 | proptest |
| **效能測試** | 效能基準線 | 慢 | 少 | criterion |
| **E2E 測試** | 完整流程 | 慢 | 少 | reqwest, testcontainers |

> ⚠️ **企業規範**：
> - 所有 PR 必須通過單元測試與整合測試
> - 程式碼覆蓋率目標：核心邏輯 ≥ 80%
> - 效能測試在每次 Release 前執行，與基準線比較
> - 使用 `cargo-tarpaulin` 產生覆蓋率報告

### 14.6 Mock Test（mockall）

```rust
use mockall::predicate::*;
use mockall::mock;

/// 定義 Repository trait
#[async_trait::async_trait]
pub trait OrderRepository: Send + Sync {
    async fn find_by_id(&self, id: uuid::Uuid) -> Result<Option<Order>, AppError>;
    async fn save(&self, order: &Order) -> Result<(), AppError>;
}

// mockall 自動產生 MockOrderRepository
mock! {
    pub OrderRepo {}
    #[async_trait::async_trait]
    impl OrderRepository for OrderRepo {
        async fn find_by_id(&self, id: uuid::Uuid) -> Result<Option<Order>, AppError>;
        async fn save(&self, order: &Order) -> Result<(), AppError>;
    }
}

#[tokio::test]
async fn test_create_order_with_mock() {
    let mut mock_repo = MockOrderRepo::new();

    // 設定 mock 預期行為
    mock_repo
        .expect_save()
        .times(1)                   // 預期呼叫一次
        .returning(|_| Ok(()));     // 回傳成功

    let service = OrderService::new(Arc::new(mock_repo));
    let result = service.create_order(CreateOrderRequest {
        customer_id: uuid::Uuid::new_v4(),
        items: vec![],
    }).await;

    assert!(result.is_ok());
}

#[tokio::test]
async fn test_get_order_not_found() {
    let mut mock_repo = MockOrderRepo::new();

    mock_repo
        .expect_find_by_id()
        .with(eq(uuid::Uuid::nil()))  // 預期特定參數
        .times(1)
        .returning(|_| Ok(None));     // 模擬查無資料

    let service = OrderService::new(Arc::new(mock_repo));
    let result = service.get_order(uuid::Uuid::nil()).await;

    assert!(matches!(result, Err(AppError::NotFound(_))));
}
```

### 14.7 Benchmark（criterion）

> 效能測試範例已在 14.4 節中展示。以下為 `Cargo.toml` 設定與進階用法：

```toml
# Cargo.toml
[[bench]]
name = "api_benchmark"
harness = false       # 使用 criterion 取代內建測試框架

[dev-dependencies]
criterion = { version = "0.5", features = ["html_reports", "async_tokio"] }
```

```rust
// 非同步 benchmark 範例
use criterion::{criterion_group, criterion_main, Criterion};

fn bench_async_db_query(c: &mut Criterion) {
    let rt = tokio::runtime::Runtime::new().unwrap();
    let pool = rt.block_on(setup_test_pool());

    c.bench_function("db_find_user_by_id", |b| {
        b.to_async(&rt).iter(|| async {
            let _ = sqlx::query_as::<_, User>("SELECT * FROM users WHERE id = $1")
                .bind(uuid::Uuid::new_v4())
                .fetch_optional(&pool)
                .await;
        });
    });
}

criterion_group!(benches, bench_async_db_query);
criterion_main!(benches);
```

---

## 15. DevSecOps 與 SSDLC

### 15.1 GitHub Actions CI/CD

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  CARGO_TERM_COLOR: always
  RUST_BACKTRACE: 1

jobs:
  check:
    name: Check & Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: dtolnay/rust-toolchain@stable
        with:
          components: rustfmt, clippy

      - uses: Swatinem/rust-cache@v2

      - name: 檢查格式
        run: cargo fmt --all -- --check

      - name: Clippy 靜態分析
        run: cargo clippy --all-targets --all-features -- -D warnings

      - name: 編譯檢查
        run: cargo check --all-targets

  test:
    name: Test
    runs-on: ubuntu-latest
    needs: check

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: Swatinem/rust-cache@v2

      - name: 執行遷移
        env:
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
        run: |
          cargo install sqlx-cli --no-default-features --features postgres
          sqlx migrate run

      - name: 執行測試
        env:
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
        run: cargo test --all-features --workspace -- --test-threads=1

      - name: 測試覆蓋率
        env:
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
        run: |
          cargo install cargo-tarpaulin
          cargo tarpaulin --out xml --output-dir coverage/
        continue-on-error: true

      - name: 上傳覆蓋率報告
        uses: codecov/codecov-action@v4
        with:
          files: coverage/cobertura.xml
          fail_ci_if_error: false

  security:
    name: Security Audit
    runs-on: ubuntu-latest
    needs: check
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: Swatinem/rust-cache@v2

      - name: 安全稽核
        run: |
          cargo install cargo-audit
          cargo audit

      - name: 授權檢查
        run: |
          cargo install cargo-deny
          cargo deny check licenses
          cargo deny check advisories

  build:
    name: Build & Push Image
    runs-on: ubuntu-latest
    needs: [test, security]
    if: github.ref == 'refs/heads/main'

    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: 登入 GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: 建置並推送 Image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: 設定 kubectl
        uses: azure/setup-kubectl@v4

      - name: 部署到 Kubernetes
        run: |
          kubectl set image deployment/enterprise-api \
            api=ghcr.io/${{ github.repository }}:${{ github.sha }} \
            -n enterprise

      - name: 等待部署完成
        run: |
          kubectl rollout status deployment/enterprise-api \
            -n enterprise \
            --timeout=300s
```

### 15.2 SSDLC 安全開發生命週期

```mermaid
graph LR
    PLAN["規劃<br/>威脅建模"] --> DEV["開發<br/>安全編碼"]
    DEV --> BUILD["建置<br/>SAST / SCA"]
    BUILD --> TEST["測試<br/>DAST / Pen Test"]
    TEST --> DEPLOY["部署<br/>映像掃描"]
    DEPLOY --> MONITOR["監控<br/>Runtime 保護"]
    MONITOR --> PLAN

    style PLAN fill:#4CAF50,color:white
    style DEV fill:#2196F3,color:white
    style BUILD fill:#FF9800,color:white
    style TEST fill:#f44336,color:white
    style DEPLOY fill:#9C27B0,color:white
    style MONITOR fill:#607D8B,color:white
```

**Rust 安全工具鏈：**

| 階段 | 工具 | 用途 |
|------|------|------|
| 開發 | `clippy` | 靜態分析，捕捉常見錯誤 |
| 開發 | `rustfmt` | 統一程式碼風格 |
| 建置 | `cargo-audit` | 檢查已知 CVE |
| 建置 | `cargo-deny` | 授權合規、依賴管理 |
| 建置 | `cargo-geiger` | 偵測 unsafe 程式碼比例 |
| 測試 | `cargo-fuzz` | 模糊測試 |
| 測試 | `miri` | 偵測未定義行為 |
| 部署 | `trivy` | 容器映像漏洞掃描 |
| 監控 | `tracing` | 執行時期追蹤 |

### 15.3 供應鏈安全

```bash
# cargo-geiger：偵測 unsafe 程式碼
cargo install cargo-geiger
cargo geiger

# cargo-crev：社群信任驗證
cargo install cargo-crev
cargo crev trust --level medium <crate-author>
cargo crev verify

# cargo-vet：供應鏈審計
cargo install cargo-vet
cargo vet init
cargo vet
```

```toml
# deny.toml 企業級安全設定
[advisories]
vulnerability = "deny"
unmaintained = "warn"
yanked = "deny"
notice = "warn"

[licenses]
allow = [
    "MIT",
    "Apache-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "ISC",
    "Unicode-3.0",
]
copyleft = "deny"
unlicensed = "deny"

[bans]
multiple-versions = "warn"
wildcards = "deny"
highlight = "all"

# 禁用的 crate
[[bans.deny]]
name = "openssl"
wrappers = ["openssl-sys"]

[sources]
unknown-registry = "deny"
unknown-git = "deny"
allow-registry = ["https://github.com/rust-lang/crates.io-index"]
```

### 15.4 模糊測試（Fuzzing）

```rust
// fuzz/fuzz_targets/fuzz_parser.rs
#![no_main]
use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    if let Ok(s) = std::str::from_utf8(data) {
        // 對解析器進行模糊測試
        let _ = parse_config(s);
    }
});

fn parse_config(input: &str) -> Result<Config, ParseError> {
    // 被測試的解析函式
    todo!()
}
```

```bash
# 安裝 cargo-fuzz
cargo install cargo-fuzz

# 建立 fuzz target
cargo fuzz init
cargo fuzz add fuzz_parser

# 執行模糊測試
cargo +nightly fuzz run fuzz_parser -- -max_len=1024 -jobs=4

# 查看 crash 報告
ls fuzz/artifacts/fuzz_parser/
```

### 15.5 SBOM 與 Dependency Scan

SBOM（Software Bill of Materials）是企業供應鏈安全的關鍵環節，記錄所有直接與間接依賴。

```bash
# 使用 cargo-cyclonedx 產生 SBOM（CycloneDX 格式）
cargo install cargo-cyclonedx
cargo cyclonedx --format json --output-file sbom.json

# 使用 cargo-audit 掃描已知漏洞
cargo install cargo-audit
cargo audit                        # 檢查 Cargo.lock 中的 CVE
cargo audit --json > audit.json    # 輸出 JSON 報告

# 使用 cargo-deny 做全面依賴檢查
cargo deny check advisories        # 安全公告
cargo deny check licenses          # 授權合規
cargo deny check bans              # 禁用 crate
cargo deny check sources           # 來源可信度
```

```yaml
# GitHub Actions 整合 SBOM
- name: 產生 SBOM
  run: |
    cargo install cargo-cyclonedx
    cargo cyclonedx --format json

- name: 上傳 SBOM 到 Dependency Graph
  uses: advanced-security/spdx-dependency-submission-action@v0.0.1
```

### 15.6 Secret Scan 與 Container Scan

```yaml
# GitHub Actions — Secret 掃描 + Container 掃描
- name: Secret 掃描（TruffleHog）
  uses: trufflesecurity/trufflehog@main
  with:
    extra_args: --only-verified

- name: Container 映像掃描（Trivy）
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ghcr.io/${{ github.repository }}:${{ github.sha }}
    format: sarif
    output: trivy-results.sarif
    severity: CRITICAL,HIGH

- name: 上傳掃描結果
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: trivy-results.sarif
```

> ⚠️ **企業規範**：
> - CI 管線中 `cargo audit` 發現 **CRITICAL** 等級漏洞時必須阻擋合併
> - 所有生產映像必須通過 Trivy 掃描且無 **HIGH** 以上漏洞
> - 每次 Release 必須附帶 SBOM 檔案

---

## 16. 可觀測性（Observability）

### 16.1 日誌（Logging）

```rust
use tracing::{debug, error, info, instrument, warn};
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt, EnvFilter};

/// 初始化日誌系統
pub fn init_tracing() {
    let env_filter = EnvFilter::try_from_default_env()
        .unwrap_or_else(|_| EnvFilter::new("info,sqlx=warn,tower_http=debug"));

    let fmt_layer = tracing_subscriber::fmt::layer()
        .json()                          // JSON 格式（適合日誌聚合系統）
        .with_target(true)               // 包含模組路徑
        .with_thread_ids(true)           // 包含執行緒 ID
        .with_file(true)                 // 包含檔案名稱
        .with_line_number(true);         // 包含行號

    tracing_subscriber::registry()
        .with(env_filter)
        .with(fmt_layer)
        .init();
}

/// 使用 #[instrument] 自動記錄函式呼叫
#[instrument(skip(pool, password), fields(user.id))]
pub async fn create_user(
    pool: &sqlx::PgPool,
    username: &str,
    email: &str,
    password: &str,
) -> Result<User, AppError> {
    info!(username, email, "建立新使用者");

    let user = User::new(username, email, password)?;

    match save_user(pool, &user).await {
        Ok(saved) => {
            info!(user.id = %saved.id, "使用者建立成功");
            Ok(saved)
        }
        Err(e) => {
            error!(error = %e, "使用者建立失敗");
            Err(e.into())
        }
    }
}

/// 結構化日誌範例
fn log_examples() {
    // 基本日誌
    info!("伺服器啟動");
    warn!(port = 3000, "使用預設埠");
    error!(code = 500, "內部錯誤");

    // Span（跨度）
    let span = tracing::info_span!("process_request", request_id = "abc-123");
    let _guard = span.enter();
    info!("處理請求中...");
    // span 自動結束

    // 動態欄位
    debug!(
        user_id = 42,
        action = "login",
        ip = "192.168.1.1",
        "使用者登入"
    );
}
```

### 16.2 指標（Metrics）

```rust
use axum::{extract::MatchedPath, http::Request, middleware::Next, response::Response};
use metrics::{counter, gauge, histogram};
use metrics_exporter_prometheus::PrometheusBuilder;

/// 初始化 Prometheus Metrics
pub fn init_metrics() -> metrics_exporter_prometheus::PrometheusHandle {
    PrometheusBuilder::new()
        .install_recorder()
        .expect("無法初始化 Prometheus")
}

/// HTTP 請求指標中介層
pub async fn metrics_middleware(
    matched_path: Option<MatchedPath>,
    req: Request<axum::body::Body>,
    next: Next,
) -> Response {
    let start = std::time::Instant::now();
    let method = req.method().to_string();
    let path = matched_path
        .map(|p| p.as_str().to_string())
        .unwrap_or_else(|| "unknown".to_string());

    // 增加請求計數
    counter!("http_requests_total", "method" => method.clone(), "path" => path.clone()).increment(1);

    // 更新活躍連線數
    gauge!("http_active_connections").increment(1.0);

    let response = next.run(req).await;

    gauge!("http_active_connections").decrement(1.0);

    let duration = start.elapsed().as_secs_f64();
    let status = response.status().as_u16().to_string();

    // 記錄回應時間直方圖
    histogram!(
        "http_request_duration_seconds",
        "method" => method,
        "path" => path,
        "status" => status
    ).record(duration);

    response
}

/// 暴露 Prometheus 指標端點
pub async fn metrics_handler(
    metrics_handle: axum::extract::State<metrics_exporter_prometheus::PrometheusHandle>,
) -> String {
    metrics_handle.render()
}
```

### 16.3 分散式追蹤（Distributed Tracing）

```rust
use opentelemetry::trace::TracerProvider;
use opentelemetry_otlp::WithExportConfig;
use tracing_subscriber::layer::SubscriberExt;

/// 初始化 OpenTelemetry 追蹤
pub fn init_otel_tracing(service_name: &str, otel_endpoint: &str) {
    let exporter = opentelemetry_otlp::SpanExporter::builder()
        .with_tonic()
        .with_endpoint(otel_endpoint)
        .build()
        .expect("無法建立 OTLP exporter");

    let provider = opentelemetry_sdk::trace::SdkTracerProvider::builder()
        .with_batch_exporter(exporter)
        .with_resource(
            opentelemetry_sdk::Resource::builder()
                .with_service_name(service_name.to_string())
                .build(),
        )
        .build();

    let tracer = provider.tracer("api");

    let telemetry_layer = tracing_opentelemetry::layer().with_tracer(tracer);

    let subscriber = tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::new("info"))
        .with(tracing_subscriber::fmt::layer().json())
        .with(telemetry_layer);

    tracing::subscriber::set_global_default(subscriber)
        .expect("無法設定全域 subscriber");
}
```

### 16.4 可觀測性架構

```mermaid
graph TD
    subgraph "應用服務"
        S1["Service A"] --> |Traces| OTEL["OpenTelemetry Collector"]
        S2["Service B"] --> |Traces| OTEL
        S1 --> |Metrics| PROM["Prometheus"]
        S2 --> |Metrics| PROM
        S1 --> |Logs| LOKI["Loki"]
        S2 --> |Logs| LOKI
    end

    OTEL --> JAEGER["Jaeger / Tempo"]
    PROM --> GRAFANA["Grafana"]
    LOKI --> GRAFANA
    JAEGER --> GRAFANA

    subgraph "告警"
        GRAFANA --> ALERT["AlertManager"]
        ALERT --> SLACK["Slack"]
        ALERT --> PD["PagerDuty"]
        ALERT --> EMAIL["Email"]
    end

    style GRAFANA fill:#FF9800,color:white
    style PROM fill:#E65100,color:white
    style JAEGER fill:#2196F3,color:white
```

### 16.5 健康檢查端點

```rust
use axum::Json;
use serde::Serialize;
use sqlx::PgPool;

#[derive(Serialize)]
pub struct HealthResponse {
    pub status: String,
    pub version: String,
    pub checks: HealthChecks,
}

#[derive(Serialize)]
pub struct HealthChecks {
    pub database: ComponentHealth,
    pub redis: ComponentHealth,
}

#[derive(Serialize)]
pub struct ComponentHealth {
    pub status: String,
    pub latency_ms: u64,
}

pub async fn health_check(
    pool: axum::extract::State<PgPool>,
    redis: axum::extract::State<RedisPool>,
) -> Json<HealthResponse> {
    let db_health = check_database(&pool).await;
    let redis_health = check_redis(&redis).await;

    let overall_status = if db_health.status == "healthy" && redis_health.status == "healthy" {
        "healthy"
    } else {
        "degraded"
    };

    Json(HealthResponse {
        status: overall_status.to_string(),
        version: env!("CARGO_PKG_VERSION").to_string(),
        checks: HealthChecks {
            database: db_health,
            redis: redis_health,
        },
    })
}

async fn check_database(pool: &PgPool) -> ComponentHealth {
    let start = std::time::Instant::now();
    match sqlx::query("SELECT 1").execute(pool).await {
        Ok(_) => ComponentHealth {
            status: "healthy".to_string(),
            latency_ms: start.elapsed().as_millis() as u64,
        },
        Err(_) => ComponentHealth {
            status: "unhealthy".to_string(),
            latency_ms: start.elapsed().as_millis() as u64,
        },
    }
}
```

---

## 17. 效能調校

### 17.1 Profile 工具

```bash
# ======== perf（Linux）========
# 編譯含有 debug 符號的 release 版本
cargo build --release
# 或在 Cargo.toml 中設定
# [profile.release]
# debug = true

perf record -g ./target/release/my-app
perf report

# ======== flamegraph ========
cargo install flamegraph
cargo flamegraph --root          # 產生火焰圖
# 輸出：flamegraph.svg

# ======== cargo-instruments（macOS）========
cargo install cargo-instruments
cargo instruments -t time        # CPU Time Profile
cargo instruments -t alloc       # 記憶體分配

# ======== tokio-console（非同步 profiling）========
cargo install tokio-console
# 在程式中啟用 console-subscriber
# 然後執行 tokio-console 連線
```

### 17.2 編譯最佳化

```toml
# Cargo.toml

[profile.release]
opt-level = 3           # 最高最佳化等級
lto = "fat"             # Link-Time Optimization（跨 crate 最佳化）
codegen-units = 1        # 單一 codegen unit（更好的最佳化，更慢的編譯）
strip = true            # 移除 debug 符號（縮小二進位大小）
panic = "abort"         # panic 時直接 abort（縮小二進位）
target-cpu = "native"   # 針對本機 CPU 最佳化

[profile.dev]
opt-level = 0
debug = true

[profile.dev.package."*"]
opt-level = 2           # 依賴套件在 dev 模式也做最佳化（加速執行）

[profile.test]
opt-level = 1           # 測試模式做些許最佳化

# 建置速度最佳化
[profile.dev]
incremental = true      # 增量編譯

# 使用 mold linker（Linux，大幅加速連結）
# .cargo/config.toml
# [target.x86_64-unknown-linux-gnu]
# linker = "clang"
# rustflags = ["-C", "link-arg=-fuse-ld=mold"]
```

### 17.3 常見效能最佳化技巧

```rust
// ======== 1. 避免不必要的分配 ========

// ❌ 不好：每次都分配新 String
fn bad_greeting(name: &str) -> String {
    format!("Hello, {}!", name)
}

// ✅ 好：使用 Cow 避免不必要的分配
use std::borrow::Cow;
fn good_greeting(name: &str) -> Cow<str> {
    if name.is_empty() {
        Cow::Borrowed("Hello, World!")
    } else {
        Cow::Owned(format!("Hello, {}!", name))
    }
}

// ======== 2. 預先分配容量 ========

// ❌ 不好：多次重新分配
fn bad_collect(n: usize) -> Vec<i32> {
    let mut v = Vec::new();
    for i in 0..n {
        v.push(i as i32);
    }
    v
}

// ✅ 好：預先分配
fn good_collect(n: usize) -> Vec<i32> {
    let mut v = Vec::with_capacity(n);
    for i in 0..n {
        v.push(i as i32);
    }
    v
}

// ======== 3. 使用 &str 而非 String 作為參數 ========

// ❌ 不好：強制呼叫者分配
fn bad_search(haystack: &str, needle: String) -> bool {
    haystack.contains(&needle)
}

// ✅ 好：接受引用
fn good_search(haystack: &str, needle: &str) -> bool {
    haystack.contains(needle)
}

// ======== 4. 使用 SmallVec 避免小集合的堆積分配 ========
use smallvec::SmallVec;

fn process_tags(tags: SmallVec<[String; 4]>) {
    // 4 個以內的元素存在 stack 上
    for tag in &tags {
        println!("{}", tag);
    }
}

// ======== 5. 使用 bytes::Bytes 處理大量二進位資料 ========
use bytes::Bytes;

fn process_data(data: Bytes) {
    // Bytes 是引用計數的，clone 是 O(1)
    let copy = data.clone(); // 零拷貝
    let slice = data.slice(0..100); // 零拷貝切片
}

// ======== 6. 使用 rayon 做資料平行化 ========
use rayon::prelude::*;

fn parallel_process(data: &[i32]) -> Vec<i32> {
    data.par_iter()    // 平行迭代器
        .map(|&x| expensive_computation(x))
        .collect()
}

fn expensive_computation(x: i32) -> i32 {
    // CPU 密集計算
    x * x + x
}
```

### 17.4 Async 效能調校

```rust
// ======== 避免在 async 中做阻塞操作 ========

// ❌ 不好：在 async context 中阻塞
async fn bad_read_file(path: &str) -> String {
    std::fs::read_to_string(path).unwrap() // 阻塞！
}

// ✅ 好：使用 tokio 的非同步版本
async fn good_read_file(path: &str) -> tokio::io::Result<String> {
    tokio::fs::read_to_string(path).await
}

// ✅ 好：使用 spawn_blocking 處理阻塞操作
async fn blocking_operation() -> String {
    tokio::task::spawn_blocking(|| {
        // 阻塞操作在專用執行緒池中執行
        std::thread::sleep(std::time::Duration::from_secs(1));
        "done".to_string()
    })
    .await
    .unwrap()
}

// ======== 連線池最佳化 ========
use sqlx::postgres::PgPoolOptions;

async fn create_optimized_pool(url: &str) -> sqlx::PgPool {
    PgPoolOptions::new()
        .max_connections(20)       // 最大連線數
        .min_connections(5)        // 最小保持連線
        .acquire_timeout(std::time::Duration::from_secs(3))  // 取得連線超時
        .idle_timeout(std::time::Duration::from_secs(600))   // 閒置連線超時
        .max_lifetime(std::time::Duration::from_secs(1800))  // 連線最大生命週期
        .connect(url)
        .await
        .expect("無法連線到資料庫")
}
```

### 17.5 效能檢查清單

| 項目 | 檢查重點 | 工具 |
|------|---------|------|
| **編譯設定** | release profile 最佳化等級 | Cargo.toml |
| **記憶體分配** | 減少不必要的堆積分配 | `cargo flamegraph` |
| **序列化** | 選擇高效的序列化格式 | `criterion` bench |
| **資料庫** | 連線池設定、查詢最佳化 | `sqlx` + `EXPLAIN ANALYZE` |
| **Async** | 避免阻塞 async runtime | `tokio-console` |
| **快取** | 熱點資料快取策略 | Redis metrics |
| **連結器** | 使用 mold/lld 加速連結 | `.cargo/config.toml` |
| **二進位大小** | strip + LTO + panic=abort | `cargo bloat` |

### 17.6 Lock Contention 分析

在高併發場景中，鎖競爭是效能瓶頸的常見來源。

```rust
// ======== 避免鎖競爭的策略 ========

// ❌ 粗粒度鎖：整個 HashMap 一把鎖
use std::sync::{Arc, RwLock};
let cache: Arc<RwLock<HashMap<String, String>>> = Arc::new(RwLock::new(HashMap::new()));

// ✅ 使用 DashMap（無鎖分段式 HashMap）
use dashmap::DashMap;
let cache: Arc<DashMap<String, String>> = Arc::new(DashMap::new());
cache.insert("key".into(), "value".into());
let val = cache.get("key");

// ✅ 使用 tokio::sync::RwLock（async 友善，不阻塞 runtime）
use tokio::sync::RwLock;
let cache: Arc<RwLock<HashMap<String, String>>> = Arc::new(RwLock::new(HashMap::new()));
{
    let read = cache.read().await;  // 多個讀者可同時持有
}
{
    let mut write = cache.write().await;  // 寫者獨佔
    write.insert("key".into(), "value".into());
}

// ✅ 使用 Atomic 型別避免鎖（計數器場景）
use std::sync::atomic::{AtomicU64, Ordering};
let counter = AtomicU64::new(0);
counter.fetch_add(1, Ordering::Relaxed);
```

**鎖競爭診斷工具：**

| 工具 | 用途 | 平台 |
|------|------|------|
| `tokio-console` | 觀察 async task 的鎖等待 | 跨平台 |
| `perf lock` | Linux 核心層級鎖分析 | Linux |
| `cargo-instruments` | Time Profiler 分析鎖等待 | macOS |
| `parking_lot` | 替代 `std::sync::Mutex`，效能更佳 | 跨平台 |

---

## 18. 團隊建立與治理

### 18.1 Rust 團隊組建策略

```mermaid
graph TD
    subgraph "Phase 1：種子團隊（1-3 個月）"
        SEED["2-3 位有經驗的<br/>Rust 工程師"]
        SEED --> INFRA["建立基礎設施<br/>CI/CD、模板、規範"]
        SEED --> PROTO["完成 PoC /<br/>第一個微服務"]
    end

    subgraph "Phase 2：擴展團隊（3-6 個月）"
        GROW["招募/培訓<br/>新成員"]
        GROW --> MENTOR["配對程式設計<br/>Code Review"]
        GROW --> DOC["完善內部文件<br/>最佳實務指南"]
    end

    subgraph "Phase 3：成熟團隊（6-12 個月）"
        MATURE["全團隊具備<br/>Rust 開發能力"]
        MATURE --> SCALE["擴展到<br/>更多服務"]
        MATURE --> SHARE["向組織分享<br/>經驗與成果"]
    end

    INFRA --> GROW
    PROTO --> GROW
    MENTOR --> MATURE
    DOC --> MATURE
```

### 18.2 程式碼規範

```toml
# rustfmt.toml — 團隊統一格式設定
max_width = 100
tab_spaces = 4
edition = "2024"
imports_granularity = "Module"
group_imports = "StdExternalCrate"
reorder_imports = true
use_field_init_shorthand = true
newline_style = "Unix"
```

```toml
# Cargo.toml — Clippy lint 設定
[lints.rust]
unsafe_code = "forbid"

[lints.clippy]
# 錯誤級
unwrap_used = "deny"
expect_used = "warn"
panic = "deny"
todo = "warn"

# 警告級
pedantic = { level = "warn", priority = -1 }
module_name_repetitions = "allow"
must_use_candidate = "allow"
missing_errors_doc = "allow"

# 效能
needless_collect = "warn"
unnecessary_lazy_evaluations = "warn"
```

### 18.3 Code Review 檢查清單

| 類別 | 檢查項目 |
|------|---------|
| **安全性** | 無 `unwrap()` / `expect()` 在生產路徑 |
| **安全性** | 無 `unsafe` 或已附帶 `SAFETY` 註解 |
| **安全性** | 敏感資料不記錄到日誌 |
| **效能** | 避免不必要的 `clone()` |
| **效能** | 使用 `&str` 而非 `String` 作為參數 |
| **效能** | 大型集合預先分配容量 |
| **錯誤處理** | 使用結構化錯誤型別 |
| **錯誤處理** | 錯誤訊息對使用者/開發者有意義 |
| **測試** | 新功能有對應的測試 |
| **測試** | 邊界條件有測試覆蓋 |
| **文件** | 公開 API 有 doc comment |
| **風格** | 通過 `cargo fmt` 和 `cargo clippy` |

### 18.4 技術債管理

```rust
// 使用 TODO / FIXME / HACK 標記技術債
// 團隊約定格式：

// TODO(author, #issue): 待實作的功能
// FIXME(author, #issue): 已知問題待修復
// HACK(author, #issue): 暫時的解決方案
// PERF(author): 效能待最佳化

// 範例：
// TODO(alice, #234): 實作分頁快取失效策略
// FIXME(bob, #567): 高併發下可能有 race condition
// HACK(carol, #890): 暫時使用硬編碼的超時值，等待設定中心上線
```

```bash
# 追蹤技術債的指令
grep -rn "TODO\|FIXME\|HACK" src/
cargo clippy --all-targets 2>&1 | grep "warning" | wc -l
```

### 18.5 開發流程

```mermaid
graph LR
    TICKET["Issue / Ticket"] --> BRANCH["Feature Branch"]
    BRANCH --> DEV["開發 + 單元測試"]
    DEV --> PR["Pull Request"]
    PR --> REVIEW["Code Review<br/>（至少 2 人）"]
    REVIEW --> CI["CI 管線通過"]
    CI --> MERGE["合併到 main"]
    MERGE --> RELEASE["Release / 部署"]
```

**分支策略（Trunk-based Development）：**

| 分支 | 命名慣例 | 用途 | 壽命 |
|------|---------|------|------|
| `main` | — | 可部署的主線 | 永久 |
| `feature/*` | `feature/add-order-api` | 新功能 | < 3 天 |
| `bugfix/*` | `bugfix/fix-auth-token` | 修復 | < 1 天 |
| `hotfix/*` | `hotfix/cve-2025-xxxx` | 緊急修補 | < 2 小時 |
| `release/*` | `release/v1.2.0` | 版本凍結 | 1-2 天 |

**Code Review 檢查清單：**

- [ ] 程式碼通過 `cargo clippy` 且零警告
- [ ] 新增程式碼有對應的單元測試
- [ ] `unsafe` 區塊附有安全性說明註解
- [ ] 錯誤處理使用 `thiserror` / `anyhow` 正確分層
- [ ] 公開 API 有 `/// doc comment`
- [ ] 效能敏感路徑已用 `criterion` 驗證

### 18.6 文件治理

| 文件類型 | 工具 | 維護頻率 |
|---------|------|---------|
| API 文件 | `utoipa` + Swagger UI | 每次 API 變更 |
| 程式碼文件 | `cargo doc` + `docs.rs` | 每次合併 |
| 架構文件 | Markdown + Mermaid | 每季更新 |
| ADR（Architecture Decision Record） | Markdown | 每次重大決策 |
| CHANGELOG | `git-cliff` | 每次 Release |
| README | Markdown | 每次重大變更 |

```bash
# 使用 git-cliff 自動產生 CHANGELOG
cargo install git-cliff
git cliff -o CHANGELOG.md

# 設定 git-cliff.toml
[changelog]
header = "# Changelog\n"
body = """
{% for group, commits in commits | group_by(attribute="group") %}
## {{ group | upper_first }}
{% for commit in commits %}
- {{ commit.message | upper_first }} ({{ commit.id | truncate(length=7, end="") }})
{% endfor %}
{% endfor %}
"""
trim = true
```

### 18.7 AI 使用規範

| 分類 | 規範 | 說明 |
|------|------|------|
| **允許** | Copilot 補完樣板程式碼 | struct、impl、derive、測試骨架 |
| **允許** | AI 輔助撰寫文件 | doc comment、README |
| **需審查** | AI 生成的業務邏輯 | 必須通過 Code Review |
| **禁止** | AI 生成的 `unsafe` 直接合併 | 必須資深工程師審查 |
| **禁止** | 將公司程式碼貼入公開 AI 工具 | 資安合規要求 |
| **禁止** | 完全依賴 AI 處理密碼學 | 必須使用經審計的 crate |

---

## 19. AI 協作開發

### 19.1 GitHub Copilot 與 Rust

**Copilot 對 Rust 的輔助效果：**

| 場景 | 效果 | 建議 |
|------|------|------|
| **樣板程式碼** | ⭐⭐⭐⭐⭐ | struct、impl、derive 自動補完 |
| **測試程式碼** | ⭐⭐⭐⭐ | 給予函式簽名即可生成測試 |
| **錯誤處理** | ⭐⭐⭐⭐ | thiserror/anyhow 模式自動推薦 |
| **Trait 實作** | ⭐⭐⭐⭐ | 根據 trait 定義自動實作 |
| **複雜生命週期** | ⭐⭐⭐ | 簡單情況可以，複雜需人工 |
| **unsafe 程式碼** | ⭐⭐ | **必須人工審查** |
| **效能最佳化** | ⭐⭐⭐ | 基本建議可用，深度最佳化需人工 |

### 19.2 AI 輔助的工作流程

```
1. 設計階段
   └─ 使用 AI 討論架構決策
   └─ 產生領域模型草案

2. 開發階段
   └─ Copilot 輔助編寫樣板程式碼
   └─ AI 生成的程式碼必須通過 Code Review
   └─ 所有 AI 生成的 unsafe 程式碼必須人工審查

3. 測試階段
   └─ AI 輔助生成測試案例
   └─ 人工補充邊界條件測試

4. 文件階段
   └─ AI 輔助撰寫 doc comment
   └─ 人工審查準確性
```

### 19.3 Prompt 撰寫技巧

```
// 好的 Prompt 範例（Rust 特定）

// 1. 明確指定回傳型別和錯誤處理
/// 從資料庫查詢使用者，支援分頁
/// 使用 sqlx query_as! 巨集
/// 回傳 Result<(Vec<User>, i64), AppError>

// 2. 指定 trait bounds
/// 實作 Repository trait for PostgreSQL
/// 使用 async_trait
/// 所有方法回傳 Result<T, RepositoryError>

// 3. 指定效能要求
/// 實作 LRU Cache，使用 Arc<RwLock<HashMap>>
/// 支援 TTL 過期機制
/// 執行緒安全
```

> ⚠️ **企業規範**：
> - AI 生成的程式碼**必須**通過完整的 CI 管線（測試、lint、安全掃描）
> - AI 生成的 `unsafe` 程式碼**禁止**直接合併，必須由資深工程師審查
> - 不得將公司敏感程式碼貼入公開的 AI 工具

### 19.4 AI Pair Programming

AI 配對程式設計的最佳實務模式：

```
┌──────────────────────────────────────────┐
│           AI Pair Programming 工作流程     │
├──────────────────────────────────────────┤
│                                          │
│  工程師：定義需求 + 設計 API 簽名          │
│  ↓                                       │
│  AI：生成實作骨架 + 樣板程式碼              │
│  ↓                                       │
│  工程師：審查邏輯 + 調整實作               │
│  ↓                                       │
│  AI：生成對應的測試案例                    │
│  ↓                                       │
│  工程師：補充邊界測試 + 驗證正確性          │
│  ↓                                       │
│  AI：生成 doc comment + 錯誤處理           │
│  ↓                                       │
│  工程師：最終 Review + 合併               │
│                                          │
└──────────────────────────────────────────┘
```

**適用場景與效益：**

| 場景 | AI 貢獻度 | 注意事項 |
|------|----------|---------|
| CRUD API | 高（70%） | 結構化程式碼 AI 很擅長 |
| 資料轉換 | 高（60%） | serde 相關程式碼 |
| 錯誤處理 | 中（50%） | 需確認錯誤型別正確 |
| 複雜演算法 | 低（20%） | AI 可提供起點，但需人工驗證 |
| 系統架構設計 | 低（10%） | AI 可做腦力激盪，決策由人做 |

### 19.5 AI Review 與 Test Generation

```bash
# 使用 Copilot CLI 做 Code Review
gh copilot suggest "review this Rust function for potential issues"

# 使用 AI 批量生成測試
# 在 VS Code 中選取函式 → Copilot → Generate Tests
```

**AI 測試生成策略：**

1. **正向路徑測試**：AI 生成基本功能測試（可直接使用）
2. **邊界條件測試**：AI 生成後需人工驗證覆蓋範圍
3. **錯誤路徑測試**：提供錯誤型別讓 AI 生成
4. **屬性測試**：給 AI 示範 `proptest` 模式讓其推廣

### 19.6 Team Prompt Library

建立團隊共用的 Prompt 範本，確保一致性：

```markdown
# Team Prompt Library（存放於 .github/prompts/）

## rust-api-endpoint.prompt.md
---
mode: agent
description: "生成 Axum API endpoint"
---
請根據以下規格生成 Axum API endpoint：
- 使用 `axum::extract` 解析參數
- 回傳型別為 `Result<Json<T>, AppError>`
- 加上 `#[instrument]` 追蹤
- 生成對應的 handler test

## rust-repository.prompt.md
---
mode: agent
description: "生成 Repository trait + impl"
---
請生成 Repository 層程式碼：
- 定義 `#[async_trait]` trait
- 使用 `sqlx` 實作 PostgreSQL 版本
- 所有方法回傳 `Result<T, RepositoryError>`
- 生成 mockall mock 供測試使用
```

---

## 20. 企業級最佳實務

### 20.1 專案結構最佳實務

```
enterprise-service/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── cd.yml
│   │   └── security.yml
│   └── CODEOWNERS
├── .cargo/
│   └── config.toml
├── Cargo.toml              # workspace 定義
├── Cargo.lock
├── rust-toolchain.toml      # 固定 Rust 版本
├── rustfmt.toml             # 格式設定
├── clippy.toml              # Clippy 設定
├── deny.toml                # cargo-deny 設定
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── README.md
├── CHANGELOG.md
├── crates/
│   ├── api/                 # HTTP API
│   ├── core/                # 業務邏輯
│   ├── domain/              # 領域模型
│   ├── infrastructure/      # 基礎設施
│   └── shared/              # 共用工具
├── migrations/              # 資料庫遷移
├── config/                  # 組態檔
├── helm/                    # Kubernetes Helm Chart
├── tests/                   # 整合測試
├── benches/                 # 效能測試
└── docs/                    # 文件
```

### 20.2 設定管理

```rust
use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct AppConfig {
    pub server: ServerConfig,
    pub database: DatabaseConfig,
    pub redis: RedisConfig,
    pub auth: AuthConfig,
    pub logging: LoggingConfig,
}

#[derive(Debug, Deserialize)]
pub struct ServerConfig {
    pub host: String,
    pub port: u16,
    pub workers: usize,
}

#[derive(Debug, Deserialize)]
pub struct DatabaseConfig {
    pub url: String,
    pub max_connections: u32,
    pub min_connections: u32,
}

#[derive(Debug, Deserialize)]
pub struct RedisConfig {
    pub url: String,
    pub default_ttl: u64,
}

#[derive(Debug, Deserialize)]
pub struct AuthConfig {
    pub jwt_secret: String,
    pub token_expiry_hours: i64,
}

#[derive(Debug, Deserialize)]
pub struct LoggingConfig {
    pub level: String,
    pub format: String, // "json" or "pretty"
}

impl AppConfig {
    /// 從環境變數載入設定
    pub fn from_env() -> Result<Self, config::ConfigError> {
        let config = config::Config::builder()
            .set_default("server.host", "0.0.0.0")?
            .set_default("server.port", 3000)?
            .set_default("server.workers", num_cpus::get())?
            .set_default("database.max_connections", 20)?
            .set_default("database.min_connections", 5)?
            .set_default("redis.default_ttl", 3600)?
            .set_default("auth.token_expiry_hours", 24)?
            .set_default("logging.level", "info")?
            .set_default("logging.format", "json")?
            .add_source(config::File::with_name("config/default").required(false))
            .add_source(config::File::with_name("config/local").required(false))
            .add_source(config::Environment::with_prefix("APP").separator("__"))
            .build()?;

        config.try_deserialize()
    }
}
```

### 20.3 版本管理策略

```toml
# rust-toolchain.toml
[toolchain]
channel = "1.95.0"
components = ["rustfmt", "clippy", "rust-analyzer"]
targets = ["x86_64-unknown-linux-gnu"]
```

```
版本發佈策略：
1. 使用語意版本（SemVer）：MAJOR.MINOR.PATCH
2. 每次 Release 更新 CHANGELOG.md
3. 使用 Git Tag 標記版本
4. Cargo.lock 必須提交到版本控制

分支策略：
main        ← 生產環境
develop     ← 開發環境
feature/*   ← 功能開發
hotfix/*    ← 緊急修復
release/*   ← 版本準備
```

### 20.4 錯誤處理最佳實務

```rust
// 統一的錯誤回應格式
use axum::{http::StatusCode, Json};
use serde::Serialize;

#[derive(Serialize)]
pub struct ErrorResponse {
    pub error: ErrorDetail,
}

#[derive(Serialize)]
pub struct ErrorDetail {
    pub code: String,
    pub message: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub details: Option<Vec<String>>,
}

#[derive(Debug, thiserror::Error)]
pub enum AppError {
    #[error("找不到資源: {0}")]
    NotFound(String),

    #[error("驗證失敗: {0}")]
    Validation(String),

    #[error("衝突: {0}")]
    Conflict(String),

    #[error("未授權")]
    Unauthorized,

    #[error("禁止存取")]
    Forbidden,

    #[error("內部錯誤: {0}")]
    Internal(String),
}

impl axum::response::IntoResponse for AppError {
    fn into_response(self) -> axum::response::Response {
        let (status, code, message) = match &self {
            AppError::NotFound(msg) => (StatusCode::NOT_FOUND, "NOT_FOUND", msg.clone()),
            AppError::Validation(msg) => (StatusCode::BAD_REQUEST, "VALIDATION_ERROR", msg.clone()),
            AppError::Conflict(msg) => (StatusCode::CONFLICT, "CONFLICT", msg.clone()),
            AppError::Unauthorized => (StatusCode::UNAUTHORIZED, "UNAUTHORIZED", "未授權".to_string()),
            AppError::Forbidden => (StatusCode::FORBIDDEN, "FORBIDDEN", "禁止存取".to_string()),
            AppError::Internal(msg) => {
                tracing::error!(error = %msg, "內部錯誤");
                (StatusCode::INTERNAL_SERVER_ERROR, "INTERNAL_ERROR", "伺服器錯誤".to_string())
            }
        };

        let body = Json(ErrorResponse {
            error: ErrorDetail {
                code: code.to_string(),
                message,
                details: None,
            },
        });

        (status, body).into_response()
    }
}
```

### 20.5 API Versioning

```rust
use axum::{Router, extract::Path};

/// API 版本管理策略：URL Path 版本控制
pub fn versioned_router() -> Router {
    Router::new()
        .nest("/api/v1", v1_routes())
        .nest("/api/v2", v2_routes())
}

fn v1_routes() -> Router {
    Router::new()
        .route("/users", axum::routing::get(v1::list_users))
        .route("/users/{id}", axum::routing::get(v1::get_user))
}

fn v2_routes() -> Router {
    Router::new()
        .route("/users", axum::routing::get(v2::list_users))  // 新的分頁格式
        .route("/users/{id}", axum::routing::get(v2::get_user))
}

// 版本遷移策略
// 1. v1 保持向後相容，設定 Deprecation header
// 2. v2 引入新功能，在 CHANGELOG 中標註破壞性變更
// 3. v1 在 2 個 major release 後移除
```

**API 版本管理策略比較：**

| 策略 | 範例 | 優點 | 缺點 |
|------|------|------|------|
| URL Path | `/api/v1/users` | 直觀、易於路由 | URL 膨脹 |
| Header | `Accept: application/vnd.api.v1+json` | URL 乾淨 | 不易測試 |
| Query Param | `/api/users?version=1` | 簡單 | 容易被忽略 |
| **建議** | **URL Path** | 企業環境最常用 | — |

### 20.6 Security Best Practices

```rust
// ======== 安全最佳實務 ========

// 1. 密碼雜湊：使用 argon2
use argon2::{Argon2, PasswordHasher, PasswordVerifier, password_hash::SaltString};
use rand_core::OsRng;

pub fn hash_password(password: &str) -> Result<String, AppError> {
    let salt = SaltString::generate(&mut OsRng);
    let argon2 = Argon2::default();
    let hash = argon2.hash_password(password.as_bytes(), &salt)
        .map_err(|e| AppError::Internal(e.to_string()))?;
    Ok(hash.to_string())
}

// 2. JWT 驗證
use jsonwebtoken::{decode, DecodingKey, Validation, Algorithm};

pub fn verify_jwt(token: &str, secret: &str) -> Result<Claims, AppError> {
    let validation = Validation::new(Algorithm::HS256);
    let data = decode::<Claims>(token, &DecodingKey::from_secret(secret.as_bytes()), &validation)
        .map_err(|_| AppError::Unauthorized)?;
    Ok(data.claims)
}

// 3. Rate Limiting（使用 tower-governor）
use tower_governor::{GovernorConfigBuilder, GovernorLayer};

let governor_conf = GovernorConfigBuilder::default()
    .per_second(10)           // 每秒 10 個請求
    .burst_size(30)           // 允許瞬間 burst 30 個
    .finish()
    .unwrap();

let app = Router::new()
    .route("/api/login", axum::routing::post(login))
    .layer(GovernorLayer { config: governor_conf });

// 4. 輸入驗證（使用 validator）
use validator::Validate;

#[derive(Validate)]
pub struct CreateUserRequest {
    #[validate(length(min = 3, max = 50))]
    pub username: String,
    #[validate(email)]
    pub email: String,
    #[validate(length(min = 12))]  // 最少 12 字元
    pub password: String,
}
```

### 20.7 Scalability 與 High Availability

```
                      ┌─────────────┐
                      │   CDN / WAF  │
                      └──────┬──────┘
                             │
                      ┌──────▼──────┐
                      │ Load Balancer│
                      └──┬───┬───┬──┘
                         │   │   │
                    ┌────▼┐ ┌▼──┐┌▼────┐
                    │Pod 1│ │P 2││Pod 3 │  ← HPA 自動擴展
                    └──┬──┘ └─┬─┘└──┬──┘
                       │      │     │
              ┌────────▼──────▼─────▼───────┐
              │       Connection Pool        │
              └─────┬──────────────┬────────┘
                    │              │
            ┌───────▼──────┐  ┌───▼──────┐
            │ PostgreSQL   │  │  Redis    │
            │ (Primary)    │  │ (Cluster) │
            └──────┬───────┘  └──────────┘
                   │
            ┌──────▼───────┐
            │ PostgreSQL   │
            │ (Read Replica)│
            └──────────────┘
```

**高可用設計要點：**

| 項目 | 策略 | Rust 實作 |
|------|------|----------|
| 無狀態服務 | Session 存 Redis | `bb8-redis` + `tower-sessions` |
| 健康檢查 | `/health` + `/ready` | Axum route + DB ping |
| 優雅關機 | 處理 `SIGTERM` | `tokio::signal` + `shutdown_signal` |
| 重試機制 | 指數退避重試 | `backon` crate |
| 熔斷器 | Circuit Breaker | 自訂中介層 |
| 讀寫分離 | Primary / Replica | 多個 `sqlx::Pool` |

---

## 21. Rust 生態系推薦

### 21.1 依類別推薦 Crate

**Web 開發：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `axum` | Web 框架 | ⭐⭐⭐⭐⭐ |
| `tower` | 中介層抽象 | ⭐⭐⭐⭐⭐ |
| `tower-http` | HTTP 中介層 | ⭐⭐⭐⭐⭐ |
| `reqwest` | HTTP 客戶端 | ⭐⭐⭐⭐⭐ |
| `utoipa` | OpenAPI 文件 | ⭐⭐⭐⭐ |

**序列化：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `serde` | 序列化框架 | ⭐⭐⭐⭐⭐ |
| `serde_json` | JSON | ⭐⭐⭐⭐⭐ |
| `toml` | TOML 設定 | ⭐⭐⭐⭐⭐ |
| `csv` | CSV 處理 | ⭐⭐⭐⭐ |

**資料庫：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `sqlx` | SQL 驅動 | ⭐⭐⭐⭐⭐ |
| `sea-orm` | ORM | ⭐⭐⭐⭐ |
| `redis` | Redis 客戶端 | ⭐⭐⭐⭐⭐ |
| `bb8` | 連線池 | ⭐⭐⭐⭐ |

**非同步：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `tokio` | 非同步 Runtime | ⭐⭐⭐⭐⭐ |
| `futures` | Future 工具 | ⭐⭐⭐⭐⭐ |
| `async-trait` | 非同步 Trait | ⭐⭐⭐⭐⭐ |

**安全與認證：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `jsonwebtoken` | JWT | ⭐⭐⭐⭐⭐ |
| `argon2` | 密碼雜湊 | ⭐⭐⭐⭐⭐ |
| `rustls` | TLS | ⭐⭐⭐⭐⭐ |

**工具與錯誤處理：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `thiserror` | 錯誤型別定義 | ⭐⭐⭐⭐⭐ |
| `anyhow` | 簡化錯誤處理 | ⭐⭐⭐⭐⭐ |
| `tracing` | 日誌/追蹤 | ⭐⭐⭐⭐⭐ |
| `chrono` | 日期時間 | ⭐⭐⭐⭐⭐ |
| `uuid` | UUID 生成 | ⭐⭐⭐⭐⭐ |
| `dotenvy` | 環境變數 | ⭐⭐⭐⭐ |
| `config` | 設定管理 | ⭐⭐⭐⭐ |
| `clap` | CLI 參數解析 | ⭐⭐⭐⭐⭐ |

**測試：**

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `mockall` | Mock 框架 | ⭐⭐⭐⭐⭐ |
| `criterion` | 效能測試 | ⭐⭐⭐⭐⭐ |
| `proptest` | 屬性測試 | ⭐⭐⭐⭐ |
| `fake` | 假資料生成 | ⭐⭐⭐⭐ |
| `wiremock` | HTTP Mock | ⭐⭐⭐⭐ |
| `testcontainers` | 容器化測試 | ⭐⭐⭐⭐ |

### 21.2 Crate 評估準則

```
選擇 Crate 的檢查清單：
□ crates.io 下載量 > 10 萬
□ 最近 3 個月有更新
□ GitHub stars > 500
□ 有活躍的 issue 處理
□ 文件完整（docs.rs）
□ 授權合規（MIT/Apache-2.0）
□ 沒有已知 CVE（cargo audit）
□ 依賴數量合理
□ 支援最新 stable Rust
```

### 21.3 CLI 與 DevOps 類別

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `clap` | CLI 參數解析 | ⭐⭐⭐⭐⭐ |
| `indicatif` | 進度條 / Spinner | ⭐⭐⭐⭐ |
| `dialoguer` | 互動式 CLI 提示 | ⭐⭐⭐⭐ |
| `colored` | 終端機彩色輸出 | ⭐⭐⭐⭐ |
| `skim` | 模糊搜尋（fzf 替代） | ⭐⭐⭐⭐ |
| `bollard` | Docker API 客戶端 | ⭐⭐⭐⭐ |
| `kube` | Kubernetes 客戶端 | ⭐⭐⭐⭐⭐ |
| `tonic` | gRPC 框架 | ⭐⭐⭐⭐⭐ |
| `prost` | Protocol Buffers | ⭐⭐⭐⭐⭐ |

### 21.4 AI 與 WASM 類別

| Crate | 用途 | 推薦度 |
|-------|------|--------|
| `candle` | 機器學習推論（Hugging Face） | ⭐⭐⭐⭐ |
| `burn` | 深度學習框架 | ⭐⭐⭐⭐ |
| `ort` | ONNX Runtime 綁定 | ⭐⭐⭐⭐ |
| `tiktoken-rs` | OpenAI tokenizer | ⭐⭐⭐⭐ |
| `wasm-bindgen` | Rust ↔ JavaScript 互操作 | ⭐⭐⭐⭐⭐ |
| `wasm-pack` | WASM 打包工具 | ⭐⭐⭐⭐⭐ |
| `leptos` | WASM 全端框架 | ⭐⭐⭐⭐ |
| `yew` | WASM 前端框架 | ⭐⭐⭐⭐ |
| `wasmtime` | WASM 執行環境（嵌入式） | ⭐⭐⭐⭐⭐ |

---

## 22. 完整企業級專案實戰

> 💡 本章展示一個完整的企業級 REST API 專案，整合 Axum + PostgreSQL + Redis + JWT 認證 + Docker + Kubernetes。

### 22.1 專案架構

```
enterprise-api/
├── Cargo.toml
├── Cargo.lock
├── rust-toolchain.toml
├── rustfmt.toml
├── deny.toml
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── config/
│   └── default.toml
├── migrations/
│   ├── 001_create_users.sql
│   └── 002_create_orders.sql
├── src/
│   ├── main.rs
│   ├── lib.rs
│   ├── config.rs
│   ├── error.rs
│   ├── domain/
│   │   ├── mod.rs
│   │   ├── user.rs
│   │   └── order.rs
│   ├── api/
│   │   ├── mod.rs
│   │   ├── router.rs
│   │   ├── auth.rs
│   │   ├── user_handler.rs
│   │   └── order_handler.rs
│   ├── service/
│   │   ├── mod.rs
│   │   ├── user_service.rs
│   │   └── order_service.rs
│   ├── repository/
│   │   ├── mod.rs
│   │   ├── user_repo.rs
│   │   └── order_repo.rs
│   └── middleware/
│       ├── mod.rs
│       ├── auth.rs
│       ├── logging.rs
│       └── metrics.rs
├── tests/
│   ├── common/mod.rs
│   └── api_tests.rs
└── helm/
    └── enterprise-api/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
```

### 22.2 Cargo.toml

```toml
[package]
name = "enterprise-api"
version = "1.0.0"
edition = "2024"
rust-version = "1.95"

[dependencies]
# Web 框架
axum = { version = "0.8", features = ["macros"] }
tower = "0.5"
tower-http = { version = "0.6", features = ["cors", "trace", "compression-gzip"] }
tokio = { version = "1", features = ["full"] }

# 序列化
serde = { version = "1", features = ["derive"] }
serde_json = "1"

# 資料庫
sqlx = { version = "0.8", features = ["runtime-tokio", "postgres", "chrono", "uuid"] }
redis = { version = "0.27", features = ["tokio-comp"] }

# 認證
jsonwebtoken = "9"
argon2 = "0.5"

# 設定
config = "0.14"
dotenvy = "0.15"

# 日誌與可觀測性
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["json", "env-filter"] }
metrics = "0.24"
metrics-exporter-prometheus = "0.16"

# 工具
chrono = { version = "0.4", features = ["serde"] }
uuid = { version = "1", features = ["v4", "serde"] }
thiserror = "2"
anyhow = "1"
validator = { version = "0.19", features = ["derive"] }
num_cpus = "1"

[dev-dependencies]
mockall = "0.13"
tower = { version = "0.5", features = ["util"] }
http-body-util = "0.1"
fake = { version = "3", features = ["derive", "chrono", "uuid"] }
```

### 22.3 main.rs 入口

```rust
// src/main.rs
use enterprise_api::{api::router::create_router, config::AppConfig};
use tracing::info;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // 載入 .env
    dotenvy::dotenv().ok();

    // 初始化日誌
    tracing_subscriber::fmt()
        .json()
        .with_env_filter(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| tracing_subscriber::EnvFilter::new("info")),
        )
        .init();

    // 載入設定
    let config = AppConfig::from_env()?;
    info!("設定載入完成，啟動伺服器於 {}:{}", config.server.host, config.server.port);

    // 建立資料庫連線池
    let db_pool = sqlx::postgres::PgPoolOptions::new()
        .max_connections(config.database.max_connections)
        .min_connections(config.database.min_connections)
        .connect(&config.database.url)
        .await?;

    // 執行資料庫遷移
    sqlx::migrate!("./migrations").run(&db_pool).await?;
    info!("資料庫遷移完成");

    // 建立 Redis 連線
    let redis_client = redis::Client::open(config.redis.url.as_str())?;

    // 建立 Prometheus metrics handle
    let metrics_handle = metrics_exporter_prometheus::PrometheusBuilder::new()
        .install_recorder()
        .expect("無法初始化 Prometheus");

    // 建立路由
    let app = create_router(db_pool, redis_client, metrics_handle, &config);

    // 啟動伺服器
    let addr = format!("{}:{}", config.server.host, config.server.port);
    let listener = tokio::net::TcpListener::bind(&addr).await?;
    info!("伺服器啟動於 {}", addr);

    // Graceful shutdown
    axum::serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await?;

    info!("伺服器已關閉");
    Ok(())
}

async fn shutdown_signal() {
    let ctrl_c = async {
        tokio::signal::ctrl_c()
            .await
            .expect("無法安裝 Ctrl+C handler");
    };

    #[cfg(unix)]
    let terminate = async {
        tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
            .expect("無法安裝 signal handler")
            .recv()
            .await;
    };

    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();

    tokio::select! {
        _ = ctrl_c => info!("收到 Ctrl+C 信號"),
        _ = terminate => info!("收到 SIGTERM 信號"),
    }
}
```

### 22.4 領域模型

```rust
// src/domain/user.rs
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use uuid::Uuid;
use validator::Validate;

/// 使用者領域模型
#[derive(Debug, Clone, Serialize, Deserialize, sqlx::FromRow)]
pub struct User {
    pub id: Uuid,
    pub username: String,
    pub email: String,
    #[serde(skip_serializing)]
    pub password_hash: String,
    pub role: UserRole,
    pub is_active: bool,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, sqlx::Type)]
#[sqlx(type_name = "user_role", rename_all = "lowercase")]
pub enum UserRole {
    Admin,
    User,
    Viewer,
}

/// 建立使用者的請求 DTO
#[derive(Debug, Deserialize, Validate)]
pub struct CreateUserRequest {
    #[validate(length(min = 3, max = 50, message = "使用者名稱長度需介於 3-50"))]
    pub username: String,

    #[validate(email(message = "Email 格式不正確"))]
    pub email: String,

    #[validate(length(min = 8, message = "密碼長度至少 8 位"))]
    pub password: String,
}

/// 使用者回應 DTO
#[derive(Debug, Serialize)]
pub struct UserResponse {
    pub id: Uuid,
    pub username: String,
    pub email: String,
    pub role: UserRole,
    pub created_at: DateTime<Utc>,
}

impl From<User> for UserResponse {
    fn from(user: User) -> Self {
        Self {
            id: user.id,
            username: user.username,
            email: user.email,
            role: user.role,
            created_at: user.created_at,
        }
    }
}
```

### 22.5 Repository 層

```rust
// src/repository/user_repo.rs
use crate::domain::user::{CreateUserRequest, User};
use crate::error::AppError;
use sqlx::PgPool;
use uuid::Uuid;

/// 使用者 Repository
pub struct UserRepository {
    pool: PgPool,
}

impl UserRepository {
    pub fn new(pool: PgPool) -> Self {
        Self { pool }
    }

    /// 依 ID 查詢使用者
    pub async fn find_by_id(&self, id: Uuid) -> Result<Option<User>, AppError> {
        let user = sqlx::query_as::<_, User>(
            "SELECT id, username, email, password_hash, role, is_active, created_at, updated_at
             FROM users WHERE id = $1 AND is_active = true"
        )
        .bind(id)
        .fetch_optional(&self.pool)
        .await?;

        Ok(user)
    }

    /// 依 Email 查詢使用者
    pub async fn find_by_email(&self, email: &str) -> Result<Option<User>, AppError> {
        let user = sqlx::query_as::<_, User>(
            "SELECT id, username, email, password_hash, role, is_active, created_at, updated_at
             FROM users WHERE email = $1"
        )
        .bind(email)
        .fetch_optional(&self.pool)
        .await?;

        Ok(user)
    }

    /// 建立使用者
    pub async fn create(&self, req: &CreateUserRequest, password_hash: &str) -> Result<User, AppError> {
        let user = sqlx::query_as::<_, User>(
            "INSERT INTO users (id, username, email, password_hash, role, is_active, created_at, updated_at)
             VALUES ($1, $2, $3, $4, 'user', true, NOW(), NOW())
             RETURNING *"
        )
        .bind(Uuid::new_v4())
        .bind(&req.username)
        .bind(&req.email)
        .bind(password_hash)
        .fetch_one(&self.pool)
        .await?;

        Ok(user)
    }

    /// 分頁查詢
    pub async fn find_all(&self, page: i64, per_page: i64) -> Result<(Vec<User>, i64), AppError> {
        let offset = (page - 1) * per_page;

        let users = sqlx::query_as::<_, User>(
            "SELECT * FROM users WHERE is_active = true
             ORDER BY created_at DESC LIMIT $1 OFFSET $2"
        )
        .bind(per_page)
        .bind(offset)
        .fetch_all(&self.pool)
        .await?;

        let total: (i64,) = sqlx::query_as("SELECT COUNT(*) FROM users WHERE is_active = true")
            .fetch_one(&self.pool)
            .await?;

        Ok((users, total.0))
    }
}
```

### 22.6 Service 層（含 Redis 快取）

```rust
// src/service/user_service.rs
use crate::domain::user::{CreateUserRequest, User, UserResponse};
use crate::error::AppError;
use crate::repository::user_repo::UserRepository;
use argon2::{password_hash::SaltString, Argon2, PasswordHash, PasswordHasher, PasswordVerifier};
use rand_core::OsRng;
use redis::AsyncCommands;
use tracing::{info, instrument};
use uuid::Uuid;

pub struct UserService {
    repo: UserRepository,
    redis: redis::Client,
}

impl UserService {
    pub fn new(repo: UserRepository, redis: redis::Client) -> Self {
        Self { repo, redis }
    }

    /// 取得使用者（快取優先）
    #[instrument(skip(self))]
    pub async fn get_user(&self, id: Uuid) -> Result<UserResponse, AppError> {
        let cache_key = format!("user:{}", id);

        // 嘗試從 Redis 快取讀取
        let mut conn = self.redis.get_multiplexed_async_connection().await?;
        if let Ok(cached) = conn.get::<_, String>(&cache_key).await {
            if let Ok(user) = serde_json::from_str::<UserResponse>(&cached) {
                info!("快取命中：{}", cache_key);
                return Ok(user);
            }
        }

        // 快取未命中，從資料庫讀取
        let user = self.repo.find_by_id(id).await?
            .ok_or_else(|| AppError::NotFound(format!("使用者 {} 不存在", id)))?;

        let response = UserResponse::from(user);

        // 寫入快取（TTL 1 小時）
        let json = serde_json::to_string(&response)?;
        let _: () = conn.set_ex(&cache_key, &json, 3600).await?;

        Ok(response)
    }

    /// 建立使用者
    #[instrument(skip(self, req), fields(username = %req.username))]
    pub async fn create_user(&self, req: CreateUserRequest) -> Result<UserResponse, AppError> {
        // 檢查 Email 是否已存在
        if self.repo.find_by_email(&req.email).await?.is_some() {
            return Err(AppError::Conflict(format!("Email {} 已被使用", req.email)));
        }

        // 雜湊密碼
        let salt = SaltString::generate(&mut OsRng);
        let password_hash = Argon2::default()
            .hash_password(req.password.as_bytes(), &salt)
            .map_err(|e| AppError::Internal(format!("密碼雜湊失敗: {}", e)))?
            .to_string();

        let user = self.repo.create(&req, &password_hash).await?;
        info!(user_id = %user.id, "使用者建立成功");

        Ok(UserResponse::from(user))
    }

    /// 驗證密碼
    pub fn verify_password(password: &str, hash: &str) -> Result<bool, AppError> {
        let parsed_hash = PasswordHash::new(hash)
            .map_err(|e| AppError::Internal(format!("密碼雜湊解析失敗: {}", e)))?;

        Ok(Argon2::default().verify_password(password.as_bytes(), &parsed_hash).is_ok())
    }
}
```

### 22.7 API Handler

```rust
// src/api/user_handler.rs
use crate::domain::user::{CreateUserRequest, UserResponse};
use crate::error::AppError;
use crate::service::user_service::UserService;
use axum::{extract::Path, extract::State, Json};
use std::sync::Arc;
use uuid::Uuid;
use validator::Validate;

/// 取得使用者
pub async fn get_user(
    State(service): State<Arc<UserService>>,
    Path(id): Path<Uuid>,
) -> Result<Json<UserResponse>, AppError> {
    let user = service.get_user(id).await?;
    Ok(Json(user))
}

/// 建立使用者
pub async fn create_user(
    State(service): State<Arc<UserService>>,
    Json(req): Json<CreateUserRequest>,
) -> Result<(axum::http::StatusCode, Json<UserResponse>), AppError> {
    // 驗證請求
    req.validate()
        .map_err(|e| AppError::Validation(e.to_string()))?;

    let user = service.create_user(req).await?;
    Ok((axum::http::StatusCode::CREATED, Json(user)))
}
```

### 22.8 JWT 認證中介層

```rust
// src/middleware/auth.rs
use axum::{extract::Request, http::header, middleware::Next, response::Response};
use jsonwebtoken::{decode, encode, DecodingKey, EncodingKey, Header, Validation};
use serde::{Deserialize, Serialize};
use uuid::Uuid;
use crate::error::AppError;

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Claims {
    pub sub: Uuid,       // 使用者 ID
    pub role: String,    // 使用者角色
    pub exp: i64,        // 過期時間
    pub iat: i64,        // 簽發時間
}

impl Claims {
    pub fn new(user_id: Uuid, role: &str, expiry_hours: i64) -> Self {
        let now = chrono::Utc::now();
        Self {
            sub: user_id,
            role: role.to_string(),
            iat: now.timestamp(),
            exp: (now + chrono::Duration::hours(expiry_hours)).timestamp(),
        }
    }
}

/// 產生 JWT Token
pub fn create_token(claims: &Claims, secret: &str) -> Result<String, AppError> {
    encode(
        &Header::default(),
        claims,
        &EncodingKey::from_secret(secret.as_bytes()),
    )
    .map_err(|e| AppError::Internal(format!("Token 產生失敗: {}", e)))
}

/// 認證中介層
pub async fn auth_middleware(
    mut req: Request,
    next: Next,
) -> Result<Response, AppError> {
    let token = req
        .headers()
        .get(header::AUTHORIZATION)
        .and_then(|v| v.to_str().ok())
        .and_then(|v| v.strip_prefix("Bearer "))
        .ok_or(AppError::Unauthorized)?;

    let jwt_secret = std::env::var("APP__AUTH__JWT_SECRET")
        .unwrap_or_else(|_| "default-secret-change-me".to_string());

    let token_data = decode::<Claims>(
        token,
        &DecodingKey::from_secret(jwt_secret.as_bytes()),
        &Validation::default(),
    )
    .map_err(|_| AppError::Unauthorized)?;

    // 將 Claims 存入請求 Extension
    req.extensions_mut().insert(token_data.claims);

    Ok(next.run(req).await)
}
```

### 22.9 路由組裝

```rust
// src/api/router.rs
use crate::api::{auth, user_handler};
use crate::middleware::auth::auth_middleware;
use crate::repository::user_repo::UserRepository;
use crate::service::user_service::UserService;
use crate::config::AppConfig;
use axum::{
    middleware,
    routing::{get, post},
    Router,
};
use sqlx::PgPool;
use std::sync::Arc;
use tower_http::{
    compression::CompressionLayer,
    cors::{Any, CorsLayer},
    trace::TraceLayer,
};

pub fn create_router(
    pool: PgPool,
    redis: redis::Client,
    metrics_handle: metrics_exporter_prometheus::PrometheusHandle,
    _config: &AppConfig,
) -> Router {
    // 建立 Service
    let user_repo = UserRepository::new(pool.clone());
    let user_service = Arc::new(UserService::new(user_repo, redis.clone()));

    // 公開路由（不需認證）
    let public_routes = Router::new()
        .route("/api/v1/auth/login", post(auth::login))
        .route("/api/v1/auth/register", post(user_handler::create_user))
        .route("/health", get(health_handler))
        .route("/metrics", get(move || async move { metrics_handle.render() }));

    // 需認證路由
    let protected_routes = Router::new()
        .route("/api/v1/users/{id}", get(user_handler::get_user))
        .layer(middleware::from_fn(auth_middleware));

    Router::new()
        .merge(public_routes)
        .merge(protected_routes)
        .with_state(user_service)
        .layer(TraceLayer::new_for_http())
        .layer(CompressionLayer::new())
        .layer(
            CorsLayer::new()
                .allow_origin(Any)
                .allow_methods(Any)
                .allow_headers(Any),
        )
}

async fn health_handler() -> &'static str {
    "OK"
}
```

### 22.10 資料庫遷移

```sql
-- migrations/001_create_users.sql
CREATE TYPE user_role AS ENUM ('admin', 'user', 'viewer');

CREATE TABLE IF NOT EXISTS users (
    id          UUID PRIMARY KEY,
    username    VARCHAR(50) NOT NULL UNIQUE,
    email       VARCHAR(255) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role        user_role NOT NULL DEFAULT 'user',
    is_active   BOOLEAN NOT NULL DEFAULT true,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
```

### 22.11 Docker 化部署

```dockerfile
# Dockerfile
FROM rust:1.95-bookworm AS chef
RUN cargo install cargo-chef
WORKDIR /app

FROM chef AS planner
COPY . .
RUN cargo chef prepare --recipe-path recipe.json

FROM chef AS builder
COPY --from=planner /app/recipe.json recipe.json
RUN cargo chef cook --release --recipe-path recipe.json
COPY . .
RUN cargo build --release

FROM debian:bookworm-slim AS runtime
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/target/release/enterprise-api /usr/local/bin/
COPY --from=builder /app/migrations /app/migrations
COPY --from=builder /app/config /app/config
WORKDIR /app
EXPOSE 3000
ENTRYPOINT ["enterprise-api"]
```

```yaml
# docker-compose.yml
services:
  api:
    build: .
    ports:
      - "3000:3000"
    env_file: .env
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: enterprise
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

---

## 23. 常見問題與解答（FAQ）

### 23.1 編譯相關

**Q1：`cannot move out of borrowed content` 是什麼意思？**

這表示你嘗試從一個引用中移出值的所有權。解法：

```rust
// ❌ 錯誤
fn get_name(user: &User) -> String {
    user.name // 嘗試移出引用中的值
}

// ✅ 正確：clone 或回傳引用
fn get_name(user: &User) -> &str {
    &user.name
}
```

**Q2：`lifetime may not live long enough` 怎麼修？**

通常需要明確標注生命週期：

```rust
// ❌ 錯誤
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() { x } else { y }
}

// ✅ 正確
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

**Q3：`the trait bound X is not satisfied` 如何處理？**

檢查是否有遺漏的 derive 或 trait 實作：

```rust
// 確認加上必要的 derive
#[derive(Debug, Clone, Serialize, Deserialize)]
struct MyStruct { /* ... */ }

// 或手動實作 trait
impl std::fmt::Display for MyStruct {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "MyStruct")
    }
}
```

### 23.2 Async 相關

**Q4：`future cannot be sent between threads safely` 怎麼辦？**

確認你的 Future 中使用的型別都是 `Send`：

```rust
// ❌ 使用了非 Send 型別（如 Rc、Cell）
use std::rc::Rc;
let data = Rc::new(42);
tokio::spawn(async move {
    println!("{}", data); // Rc 不是 Send
});

// ✅ 改用 Arc
use std::sync::Arc;
let data = Arc::new(42);
tokio::spawn(async move {
    println!("{}", data);
});
```

**Q5：什麼時候該用 `tokio::spawn` vs `tokio::spawn_blocking`？**

```
tokio::spawn         → 非同步任務（I/O bound）
tokio::spawn_blocking → 阻塞任務（CPU bound、同步 I/O）
```

### 23.3 專案實務

**Q6：該用 `String` 還是 `&str`？**

```
函式參數      → &str（接受引用，更彈性）
結構體欄位    → String（擁有所有權）
回傳值        → String（呼叫者擁有所有權）
臨時比對/搜尋 → &str（零分配）
```

**Q7：如何選擇錯誤處理策略？**

```
程式庫（library）  → thiserror（定義具體錯誤型別）
應用程式（binary） → anyhow（便利的錯誤串接）
```

**Q8：何時使用 `clone()`？**

```
✅ 跨越執行緒邊界（Arc::clone）
✅ 資料量小且不頻繁
✅ 避免複雜的生命週期標注
❌ 在迴圈中對大資料 clone
❌ 懶惰地 clone 所有東西
```

### 23.4 Async Deadlock

**Q9：我的 async 程式卡住了，怎麼排查？**

常見原因與解法：

```rust
// ❌ 在 async 中使用 std::sync::Mutex（會阻塞整個 runtime thread）
use std::sync::Mutex;
let data = Mutex::new(vec![]);
// 在 .await 期間持有 std::sync::MutexGuard → 可能導致死鎖

// ✅ 使用 tokio::sync::Mutex
use tokio::sync::Mutex;
let data = Mutex::new(vec![]);
let mut guard = data.lock().await;

// ❌ block_on 嵌套（在 async 中再次 block_on 會死鎖）
// tokio::runtime::Runtime::new().unwrap().block_on(async { ... })

// ✅ 使用 tokio::spawn 或直接 .await
tokio::spawn(async { /* ... */ });
```

**排查步驟：**

1. 啟用 `tokio-console`：觀察哪些 task 處於等待狀態
2. 檢查是否在 `.await` 期間持有 `std::sync` 鎖
3. 檢查是否有 `block_on` 嵌套
4. 確認沒有在 async context 中呼叫同步阻塞 I/O

### 23.5 Memory Leak 排查

**Q10：Rust 不是記憶體安全的嗎？為什麼會有 Memory Leak？**

Rust 保證不會有 use-after-free 和 dangling pointer，但 **memory leak 不違反記憶體安全**。

常見原因：

```rust
// 1. 循環引用（Rc<T> 互相引用）
use std::rc::Rc;
use std::cell::RefCell;
// 解法：使用 Weak<T> 打破循環

// 2. 忘記 drop 長期存活的資源
// 解法：明確呼叫 drop() 或限制 scope

// 3. unbounded channel 不斷堆積
// 解法：使用 bounded channel（tokio::sync::mpsc::channel(capacity)）

// 4. 快取無 eviction 策略
// 解法：使用 LRU cache 或設定 TTL
```

**排查工具：**

```bash
# 使用 Valgrind（Linux）
valgrind --tool=massif ./target/release/my_app

# 使用 heaptrack（Linux）
heaptrack ./target/release/my_app

# 使用 DHAT（透過 dhat crate）
# 在 Cargo.toml 加入 dhat = "0.3"
```

### 23.6 Cargo 問題

**Q11：`cargo build` 很慢怎麼辦？**

```bash
# 1. 使用 sccache 快取編譯結果
cargo install sccache
export RUSTC_WRAPPER=sccache

# 2. 使用更快的連結器
# .cargo/config.toml
[target.x86_64-unknown-linux-gnu]
linker = "clang"
rustflags = ["-C", "link-arg=-fuse-ld=mold"]

# 3. 減少 codegen-units（只在 release）
# dev profile 保持多個 codegen-units 加速

# 4. 使用 cargo-nextest 加速測試
cargo install cargo-nextest
cargo nextest run  # 平行化測試執行
```

**Q12：依賴衝突（duplicate versions）怎麼處理？**

```bash
# 查看重複依賴
cargo tree -d

# 在 Cargo.toml 使用 [patch] 統一版本
[patch.crates-io]
some-crate = { git = "https://github.com/user/some-crate", branch = "fix" }
```

---

## 24. 學習路線圖

```mermaid
graph TD
    START["🚀 開始學習 Rust"] --> BASIC["📘 基礎語法<br/>變數、型別、函式<br/>控制流程、Pattern Matching<br/>預計：2-3 週"]
    BASIC --> OWN["🔑 所有權系統<br/>Ownership、Borrowing<br/>Lifetimes、Move Semantics<br/>預計：2-3 週"]
    OWN --> ADV["⚙️ 進階特性<br/>Traits、Generics<br/>Smart Pointers<br/>Error Handling<br/>預計：3-4 週"]

    ADV --> PATH{選擇方向}

    PATH --> WEB["🌐 Web 後端<br/>Axum / Actix-web<br/>SQLx / SeaORM<br/>JWT 認證<br/>預計：4-6 週"]
    PATH --> SYS["🖥️ 系統程式<br/>Async / Tokio<br/>網路程式設計<br/>FFI / unsafe<br/>預計：4-6 週"]
    PATH --> WASM["🔮 WebAssembly<br/>wasm-pack<br/>前端整合<br/>預計：2-3 週"]

    WEB --> ENT["🏢 企業實戰<br/>Clean Architecture<br/>Docker / K8s<br/>CI/CD / DevSecOps<br/>可觀測性<br/>預計：4-8 週"]
    SYS --> ENT
    WASM --> ENT

    ENT --> MASTER["🏆 精通<br/>效能調校<br/>巨集開發<br/>開源貢獻<br/>持續精進"]

    style START fill:#4CAF50,color:white
    style BASIC fill:#2196F3,color:white
    style OWN fill:#FF9800,color:white
    style ADV fill:#9C27B0,color:white
    style WEB fill:#00BCD4,color:white
    style SYS fill:#607D8B,color:white
    style WASM fill:#795548,color:white
    style ENT fill:#f44336,color:white
    style MASTER fill:#FFD700,color:black
```

### 24.1 各階段推薦資源

| 階段 | 資源 | 類型 |
|------|------|------|
| **入門** | [The Rust Programming Language](https://doc.rust-lang.org/book/) | 官方書籍 |
| **入門** | [Rustlings](https://github.com/rust-lang/rustlings) | 練習題 |
| **入門** | [Rust by Example](https://doc.rust-lang.org/rust-by-example/) | 範例學習 |
| **進階** | [Programming Rust, 2nd Ed.](https://www.oreilly.com/library/view/programming-rust-2nd/9781492052586/) | 書籍 |
| **進階** | [Rust for Rustaceans](https://rust-for-rustaceans.com/) | 書籍 |
| **非同步** | [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/) | 官方文件 |
| **Web** | [Axum 官方範例](https://github.com/tokio-rs/axum/tree/main/examples) | 範例 |
| **實戰** | [Zero To Production In Rust](https://www.zero2prod.com/) | 書籍 |

### 24.2 初學者路線（0-3 個月）

| 週次 | 學習目標 | 實作練習 | 參考章節 |
|------|---------|---------|---------|
| 1-2 | 環境建置、基本語法 | Hello World、猜數字遊戲 | Ch1-2 |
| 3-4 | 所有權、借用、生命週期 | 實作字串處理工具 | Ch3 |
| 5-6 | Struct、Enum、Pattern Matching | 實作命令列計算機 | Ch4 |
| 7-8 | Trait、泛型、錯誤處理 | 實作簡易 JSON parser | Ch5 |
| 9-10 | 集合、迭代器、閉包 | 實作文字統計工具 | Ch6 |
| 11-12 | 模組系統、Cargo | 將以上練習整合為 Cargo 專案 | Ch7 |

### 24.3 中階路線（3-6 個月）

| 週次 | 學習目標 | 實作練習 | 參考章節 |
|------|---------|---------|---------|
| 13-14 | 非同步程式設計（Tokio） | 實作並發 HTTP 下載器 | Ch10 |
| 15-16 | Web 框架（Axum） | 實作 REST API（CRUD） | Ch8 |
| 17-18 | 資料庫整合（SQLx） | 加入 PostgreSQL 持久化 | Ch9 |
| 19-20 | 認證授權（JWT） | 為 API 加入登入機制 | Ch8 |
| 21-22 | 測試策略 | 為專案撰寫完整測試 | Ch14 |
| 23-24 | Docker 容器化 | 為專案撰寫 Dockerfile | Ch13 |

### 24.4 高階與架構師路線（6-12 個月）

| 週次 | 學習目標 | 實作練習 | 參考章節 |
|------|---------|---------|---------|
| 25-28 | Clean Architecture | 重構為分層架構 | Ch12 |
| 29-32 | CI/CD + DevSecOps | 建置完整 GitHub Actions | Ch15 |
| 33-36 | 可觀測性 | 整合 tracing + Prometheus | Ch16 |
| 37-40 | Kubernetes 部署 | Helm Chart + HPA | Ch13 |
| 41-44 | 效能調校 | Flamegraph + Benchmark | Ch17 |
| 45-48 | 巨集與 FFI | 撰寫 proc macro + C FFI | Ch5 進階 |

---

## 25. 結論

### 25.1 Rust 在企業中的價值

```
✅ 記憶體安全 → 減少 70% 以上的安全漏洞（微軟、Google 實證）
✅ 高效能 → 與 C/C++ 同級的執行效能，無 GC 暫停
✅ 可靠性 → 編譯器驅動的正確性保證，大幅降低線上問題
✅ 現代工具鏈 → Cargo、rustfmt、clippy 提供一流的開發體驗
✅ 活躍生態 → crates.io 超過 26.8 萬個套件，涵蓋各主要領域
✅ 人才吸引力 → 連續多年 Stack Overflow 最受喜愛的語言
```

### 25.2 導入建議

```
1. 從邊緣服務開始 → 選擇一個低風險的微服務作為試點
2. 建立種子團隊 → 2-3 位有經驗的工程師引領
3. 投資培訓 → 系統性的培訓計劃，配對程式設計
4. 建立規範 → 程式碼風格、CI/CD、Code Review 流程
5. 量化成效 → 追蹤效能、安全性、開發效率指標
6. 逐步擴展 → 成功後推廣到更多服務
```

### 25.3 技術選型建議

| 應用場景 | 推薦使用 Rust | 替代方案 | 說明 |
|---------|:------------:|---------|------|
| 高效能微服務 | ✅ | Go | Rust 效能更高，但學習曲線較陡 |
| CLI 工具 | ✅ | Go, Python | Rust 產出單一靜態二進位 |
| 系統程式 | ✅ | C, C++ | Rust 記憶體安全優勢明顯 |
| WebAssembly | ✅ | C++, AssemblyScript | Rust WASM 生態最成熟 |
| 嵌入式系統 | ✅ | C | 無 std 支援良好 |
| 快速原型 | ❌ | Python, TypeScript | Rust 編譯時間較長 |
| 資料科學 | ❌ | Python | Python 生態遠超 Rust |
| 前端 UI | ⚠️ | TypeScript | Leptos/Yew 尚在成長中 |
| 大量 CRUD 應用 | ⚠️ | Java, C# | 框架成熟度差距 |

> ⭐ **Rust 不只是一個程式語言，它是對軟體品質的承諾。**
> 在正確性、效能和安全性上，Rust 為企業提供了前所未有的保障。

---

## 26. 附錄：新進成員檢查清單

### 26.1 環境建置（第 1 天）

- [ ] 安裝 Rust（`rustup`）
- [ ] 安裝 VS Code + rust-analyzer 擴充套件
- [ ] 設定 Git 並 clone 專案
- [ ] 執行 `cargo build`，確認編譯成功
- [ ] 執行 `cargo test`，確認測試通過
- [ ] 安裝 Docker Desktop
- [ ] 使用 `docker compose up` 啟動本地環境

### 26.2 開發規範熟悉（第 1-2 週）

- [ ] 閱讀本手冊第 1-5 章（基礎語法）
- [ ] 完成 Rustlings 練習
- [ ] 閱讀團隊 `rustfmt.toml` 和 Clippy 設定
- [ ] 理解專案目錄結構和模組劃分
- [ ] 閱讀 `CONTRIBUTING.md`
- [ ] 提交第一個 PR（修復小 bug 或改善文件）
- [ ] 參加第一次 Code Review

### 26.3 進階能力（第 3-4 週）

- [ ] 閱讀本手冊第 6-10 章（進階特性）
- [ ] 理解專案的錯誤處理策略
- [ ] 瞭解 CI/CD 管線和部署流程
- [ ] 完成一個小型功能開發（含測試）
- [ ] 學習使用 `cargo clippy` 和 `cargo audit`

### 26.4 獨立作業（第 5-8 週）

- [ ] 閱讀本手冊第 12-17 章（架構與運維）
- [ ] 獨立完成一個中型功能開發
- [ ] 擔任 Code Reviewer
- [ ] 理解可觀測性工具（日誌、指標、追蹤）
- [ ] 排查並修復一個線上問題

---

## 27. 版本歷史

| 版本 | 日期 | 更新內容 |
|------|------|---------|
| 1.0.0 | 2025-05-17 | 初版發佈，涵蓋 25 章完整教學 |
| 2.0.0 | 2026-05-17 | 全面更新至 Rust 1.95.0；同步 crates.io 最新統計（26.8 萬+ crates）；補齊目錄與內容一致性；新增缺漏章節內容；修正 Markdown 格式；整體品質提升至企業技術白皮書等級 |

---

> 📝 **文件維護說明**：本手冊應隨 Rust 版本更新和團隊實務演進而定期維護。建議每季度檢視一次，確保內容與最新穩定版 Rust 和生態系保持同步。

