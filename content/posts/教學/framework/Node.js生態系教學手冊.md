+++
date = '2026-02-04T19:13:19+08:00'
draft = false
title = 'Node.js生態系教學手冊'
tags = ['教學', 'framework']
categories = ['教學']
+++

# Node.js 生態系教學手冊

> **版本**：2026.06  
> **適用對象**：具備基礎程式能力，準備參與 Web Application 或 Backend API 專案開發的工程師  
> **定位**：實務導向、架構導向、企業導向的內部技術文件  
> **Node.js 版本基準**：v26.1.0 LTS  
> **最後更新**：2026 年 6 月

---

## 目錄

### [第 1 章：Node.js 簡介](#第-1-章nodejs-簡介)
- [1.1 Node.js 是什麼](#11-nodejs-是什麼)
- [1.2 Runtime 架構與 V8 Engine](#12-runtime-架構與-v8-engine)
- [1.3 Event Loop 運作機制](#13-event-loop-運作機制)
- [1.4 Non-blocking I/O 模型](#14-non-blocking-io-模型)
- [1.5 Node.js 適用場景與不適用場景](#15-nodejs-適用場景與不適用場景)
- [1.6 Node.js LTS 與 Current 版本策略](#16-nodejs-lts-與-current-版本策略)

### [第 2 章：Node.js 生態系](#第-2-章nodejs-生態系)
- [2.1 npm](#21-npm)
- [2.2 yarn](#22-yarn)
- [2.3 pnpm](#23-pnpm)
- [2.4 npx 與 corepack](#24-npx-與-corepack)
- [2.5 package.json 完整解析](#25-packagejson-完整解析)
- [2.6 package-lock.json 與依賴鎖定](#26-package-lockjson-與依賴鎖定)
- [2.7 Semantic Versioning（語意化版本）](#27-semantic-versioning語意化版本)

### [第 3 章：Node.js 安裝與環境建立](#第-3-章nodejs-安裝與環境建立)
- [3.1 Windows 環境安裝](#31-windows-環境安裝)
- [3.2 Linux 環境安裝](#32-linux-環境安裝)
- [3.3 macOS 環境安裝](#33-macos-環境安裝)
- [3.4 nvm — Node Version Manager](#34-nvm--node-version-manager)
- [3.5 fnm — Fast Node Manager](#35-fnm--fast-node-manager)
- [3.6 Volta — 可靠的 JavaScript 工具管理器](#36-volta--可靠的-javascript-工具管理器)
- [3.7 企業環境設定與內部 Registry](#37-企業環境設定與內部-registry)

### [第 4 章：TypeScript 開發平台](#第-4-章typescript-開發平台)
- [4.1 為什麼企業專案必須使用 TypeScript](#41-為什麼企業專案必須使用-typescript)
- [4.2 tsconfig.json 設計原則](#42-tsconfigjson-設計原則)
- [4.3 ESM 與 CommonJS 互操作性](#43-esm-與-commonjs-互操作性)
- [4.4 ts-node 與 tsx 開發工具](#44-ts-node-與-tsx-開發工具)
- [4.5 SWC 與 esbuild 高速編譯器](#45-swc-與-esbuild-高速編譯器)
- [4.6 Node.js v26 原生 TypeScript 支援](#46-nodejs-v26-原生-typescript-支援)
- [4.7 型別設計與 Domain Model 最佳實務](#47-型別設計與-domain-model-最佳實務)

### [第 5 章：Node.js 核心 API](#第-5-章nodejs-核心-api)
- [5.1 fs（檔案系統）](#51-fs檔案系統)
- [5.2 path（路徑處理）](#52-path路徑處理)
- [5.3 os（作業系統資訊）](#53-os作業系統資訊)
- [5.4 process（程序管理）](#54-process程序管理)
- [5.5 buffer（二進位資料處理）](#55-buffer二進位資料處理)
- [5.6 stream（串流處理）](#56-stream串流處理)
- [5.7 crypto（加密與雜湊）](#57-crypto加密與雜湊)
- [5.8 http / https（HTTP 伺服器與客戶端）](#58-http--httpshttp-伺服器與客戶端)
- [5.9 events（事件發射器）](#59-events事件發射器)
- [5.10 timers（計時器）](#510-timers計時器)
- [5.11 worker_threads（工作執行緒）](#511-worker_threads工作執行緒)
- [5.12 cluster（叢集）](#512-cluster叢集)
- [5.13 child_process（子程序）](#513-child_process子程序)
- [5.14 diagnostics_channel（診斷通道）](#514-diagnostics_channel診斷通道)
- [5.15 新興 API：SQLite、FFI、Permissions](#515-新興-apisqliteffi-permissions)

### [第 6 章：非同步程式設計](#第-6-章非同步程式設計)
- [6.1 Callback 模式](#61-callback-模式)
- [6.2 Promise 與 Promise 組合器](#62-promise-與-promise-組合器)
- [6.3 async / await 最佳實務](#63-async--await-最佳實務)
- [6.4 Event Loop 深入解析](#64-event-loop-深入解析)
- [6.5 Microtask Queue 與 Macrotask Queue](#65-microtask-queue-與-macrotask-queue)
- [6.6 並行控制與流量管控](#66-並行控制與流量管控)

### [第 7 章：Express 教學](#第-7-章express-教學)
- [7.1 建立 REST API](#71-建立-rest-api)
- [7.2 Middleware 機制](#72-middleware-機制)
- [7.3 Routing 設計](#73-routing-設計)
- [7.4 Error Handling](#74-error-handling)
- [7.5 JWT 身分驗證](#75-jwt-身分驗證)
- [7.6 Request Validation](#76-request-validation)
- [7.7 File Upload](#77-file-upload)
- [7.8 Express 效能最佳化](#78-express-效能最佳化)
- [7.9 Express 安全強化](#79-express-安全強化)
- [7.10 Express 與 Graceful Shutdown](#710-express-與-graceful-shutdown)

### [第 8 章：Fastify 教學](#第-8-章fastify-教學)
- [8.1 高效能 API 建構](#81-高效能-api-建構)
- [8.2 Plugin 架構](#82-plugin-架構)
- [8.3 Schema Validation 與序列化](#83-schema-validation-與序列化)
- [8.4 效能比較與調校](#84-效能比較與調校)
- [8.5 TypeBox Schema 驗證](#85-typebox-schema-驗證)
- [8.6 Fastify Hooks 生命週期](#86-fastify-hooks-生命週期)
- [8.7 Fastify 封裝性與裝飾器](#87-fastify-封裝性與裝飾器)
- [8.8 Fastify Rate Limiting 與安全](#88-fastify-rate-limiting-與安全)
- [8.9 Fastify 錯誤處理](#89-fastify-錯誤處理)

### [第 9 章：NestJS 教學](#第-9-章nestjs-教學)
- [9.1 Module 模組設計](#91-module-模組設計)
- [9.2 Controller 控制器](#92-controller-控制器)
- [9.3 Provider 與 Service](#93-provider-與-service)
- [9.4 Dependency Injection 依賴注入](#94-dependency-injection-依賴注入)
- [9.5 Guard 守衛](#95-guard-守衛)
- [9.6 Interceptor 攔截器](#96-interceptor-攔截器)
- [9.7 Pipe 管道](#97-pipe-管道)
- [9.8 CQRS 模式](#98-cqrs-模式)
- [9.9 NestJS 微服務模式](#99-nestjs-微服務模式)
- [9.10 NestJS 排程任務](#910-nestjs-排程任務)

### [第 10 章：API 設計最佳實務](#第-10-章api-設計最佳實務)
- [10.1 RESTful API 設計原則](#101-restful-api-設計原則)
- [10.2 OpenAPI / Swagger 文件化](#102-openapi--swagger-文件化)
- [10.3 API Versioning 策略](#103-api-versioning-策略)
- [10.4 統一錯誤碼設計](#104-統一錯誤碼設計)
- [10.5 Idempotency 冪等性設計](#105-idempotency-冪等性設計)
- [10.6 Pagination 分頁設計](#106-pagination-分頁設計)
- [10.7 GraphQL 簡介與對比](#107-graphql-簡介與對比)
- [10.8 WebSocket 即時通訊 API](#108-websocket-即時通訊-api)
- [10.9 API 錯誤碼體系設計](#109-api-錯誤碼體系設計)
- [10.10 API 限流與配額設計](#1010-api-限流與配額設計)

### [第 11 章：資料庫整合](#第-11-章資料庫整合)
- [11.1 PostgreSQL 整合](#111-postgresql-整合)
- [11.2 MySQL 整合](#112-mysql-整合)
- [11.3 MongoDB 整合](#113-mongodb-整合)
- [11.4 Redis 快取整合](#114-redis-快取整合)
- [11.5 Prisma ORM](#115-prisma-orm)
- [11.6 TypeORM](#116-typeorm)
- [11.7 Transaction、Migration 與連線池](#117-transactionmigration-與連線池)
- [11.8 Prisma 進階查詢模式](#118-prisma-進階查詢模式)
- [11.9 Redis 進階模式](#119-redis-進階模式)

### [第 12 章：測試](#第-12-章測試)
- [12.1 Node.js 內建 Test Runner（node:test）](#121-nodejs-內建-test-runnernodetest)
- [12.2 Jest 測試框架](#122-jest-測試框架)
- [12.3 Vitest 測試框架](#123-vitest-測試框架)
- [12.4 Supertest 整合測試](#124-supertest-整合測試)
- [12.5 Playwright E2E 測試](#125-playwright-e2e-測試)
- [12.6 Test Pyramid 與測試策略](#126-test-pyramid-與測試策略)
- [12.7 Mock / Stub / Spy 使用時機](#127-mock--stub--spy-使用時機)
- [12.8 Coverage 工具（c8 / istanbul）](#128-coverage-工具c8--istanbul)
- [12.9 Contract Testing（契約測試）](#129-contract-testing契約測試)
- [12.10 測試資料管理](#1210-測試資料管理)
- [12.11 Snapshot Testing](#1211-snapshot-testing)

### [第 13 章：專案架構設計](#第-13-章專案架構設計)
- [13.1 Clean Architecture 應用](#131-clean-architecture-應用)
- [13.2 Hexagonal Architecture 應用](#132-hexagonal-architecture-應用)
- [13.3 Domain-Driven Design（DDD）實作](#133-domain-driven-designddd實作)
- [13.4 Monorepo 策略（Turborepo / Nx / pnpm workspace）](#134-monorepo-策略turborepo--nx--pnpm-workspace)
- [13.5 微服務架構設計](#135-微服務架構設計)
- [13.6 Error Handling 架構](#136-error-handling-架構)
- [13.7 Configuration Management](#137-configuration-management)

### [第 14 章：前端整合](#第-14-章前端整合)
- [14.1 Vue 整合模式](#141-vue-整合模式)
- [14.2 React 整合模式](#142-react-整合模式)
- [14.3 Next.js 全端框架](#143-nextjs-全端框架)
- [14.4 Nuxt.js 全端框架](#144-nuxtjs-全端框架)
- [14.5 Server-Side Rendering（SSR）架構](#145-server-side-renderingssr架構)
- [14.6 BFF（Backend for Frontend）設計模式](#146-bffbackend-for-frontend設計模式)
- [14.7 Server-Sent Events（SSE）即時推送](#147-server-sent-eventssse即時推送)
- [14.8 Micro-Frontend 整合模式](#148-micro-frontend-整合模式)
- [14.9 API 狀態管理（TanStack Query）](#149-api-狀態管理tanstack-query)

### [第 15 章：Docker 化](#第-15-章docker-化)
- [15.1 Node.js Dockerfile 撰寫](#151-nodejs-dockerfile-撰寫)
- [15.2 Multi-stage Build](#152-multi-stage-build)
- [15.3 Docker Compose 開發環境](#153-docker-compose-開發環境)
- [15.4 容器安全最佳實務](#154-容器安全最佳實務)
- [15.5 Docker Compose 完整開發環境](#155-docker-compose-完整開發環境)
- [15.6 生產環境 Docker 最佳實務](#156-生產環境-docker-最佳實務)

### [第 16 章：Kubernetes 部署](#第-16-章kubernetes-部署)
- [16.1 Deployment 設定](#161-deployment-設定)
- [16.2 Service 與 Ingress](#162-service-與-ingress)
- [16.3 ConfigMap 與 Secret](#163-configmap-與-secret)
- [16.4 HPA 自動擴縮](#164-hpa-自動擴縮)
- [16.5 Health Check 與 Readiness Probe](#165-health-check-與-readiness-probe)
- [16.6 Helm Chart 管理](#166-helm-chart-管理)
- [16.7 Namespace 與資源隔離策略](#167-namespace-與資源隔離策略)

### [第 17 章：CI/CD](#第-17-章cicd)
- [17.1 GitHub Actions 完整範例](#171-github-actions-完整範例)
- [17.2 GitLab CI 配置](#172-gitlab-ci-配置)
- [17.3 Jenkins Pipeline](#173-jenkins-pipeline)
- [17.4 Build → Test → Security Scan → Docker Build → Deploy 流程](#174-build--test--security-scan--docker-build--deploy-流程)
- [17.5 Semantic Versioning 自動化](#175-semantic-versioning-自動化)
- [17.6 Commit 規範與自動化](#176-commit-規範與自動化)

### [第 18 章：Logging 與 Monitoring](#第-18-章logging-與-monitoring)
- [18.1 Winston 日誌框架](#181-winston-日誌框架)
- [18.2 Pino 高效能日誌](#182-pino-高效能日誌)
- [18.3 OpenTelemetry 可觀測性](#183-opentelemetry-可觀測性)
- [18.4 Prometheus 指標收集](#184-prometheus-指標收集)
- [18.5 Grafana 視覺化監控](#185-grafana-視覺化監控)
- [18.6 分散式追蹤（OpenTelemetry）](#186-分散式追蹤opentelemetry)
- [18.7 ELK Stack 日誌架構](#187-elk-stack-日誌架構)
- [18.8 告警策略設計](#188-告警策略設計)

### [第 19 章：Node.js 效能調校](#第-19-章nodejs-效能調校)
- [19.1 Event Loop Lag 監控](#191-event-loop-lag-監控)
- [19.2 Memory Leak 偵測](#192-memory-leak-偵測)
- [19.3 Heap Snapshot 分析](#193-heap-snapshot-分析)
- [19.4 CPU Profile 分析](#194-cpu-profile-分析)
- [19.5 Benchmark 工具](#195-benchmark-工具)
- [19.6 效能最佳化清單](#196-效能最佳化清單)
- [19.7 V8 引擎最佳化技巧](#197-v8-引擎最佳化技巧)
- [19.8 Worker Threads 平行運算](#198-worker-threads-平行運算)
- [19.9 Stream 效能最佳化](#199-stream-效能最佳化)
- [19.10 JSON 序列化加速](#1910-json-序列化加速)

### [第 20 章：安全性（SSDLC）](#第-20-章安全性ssdlc)
- [20.1 OWASP Top 10 for Node.js](#201-owasp-top-10-for-nodejs)
- [20.2 npm 供應鏈攻擊防護](#202-npm-供應鏈攻擊防護)
- [20.3 依賴掃描與 SAST/DAST](#203-依賴掃描與-sastdast)
- [20.4 Secret 管理](#204-secret-管理)
- [20.5 JWT 安全最佳實務](#205-jwt-安全最佳實務)
- [20.6 Helmet、CORS 與 Rate Limiting](#206-helmetcors-與-rate-limiting)
- [20.7 輸入驗證與 Injection 防護](#207-輸入驗證與-injection-防護)
- [20.8 SSRF 防護](#208-ssrf-防護)
- [20.9 密碼安全與雜湊](#209-密碼安全與雜湊)
- [20.10 Content Security Policy（CSP）](#2010-content-security-policycsp)
- [20.11 安全 HTTP Headers 完整清單](#2011-安全-http-headers-完整清單)

### [第 21 章：AI 協作開發](#第-21-章ai-協作開發)
- [21.1 GitHub Copilot](#211-github-copilot)
- [21.2 Claude Code](#212-claude-code)
- [21.3 其他 AI 工具整合](#213-其他-ai-工具整合)
- [21.4 Prompt Engineering for Coding](#214-prompt-engineering-for-coding)
- [21.5 AI 輔助 Code Review](#215-ai-輔助-code-review)
- [21.6 AI 輔助測試產生](#216-ai-輔助測試產生)
- [21.7 AI 輔助文件產生](#217-ai-輔助文件產生)
- [21.8 CLAUDE.md 專案規範範例](#218-claudemd-專案規範範例)

### [第 22 章：Node.js 維運](#第-22-章nodejs-維運)
- [22.1 PM2 程序管理](#221-pm2-程序管理)
- [22.2 Cluster 模式](#222-cluster-模式)
- [22.3 部署策略](#223-部署策略)
- [22.4 Graceful Shutdown](#224-graceful-shutdown)
- [22.5 維運監控 Checklist](#225-維運監控-checklist)
- [22.6 Node.js 生產環境設定](#226-nodejs-生產環境設定)
- [22.7 日誌輪替與管理](#227-日誌輪替與管理)
- [22.8 健康檢查與自我修復](#228-健康檢查與自我修復)

### [第 23 章：企業級最佳實務](#第-23-章企業級最佳實務)
- [23.1 Coding Standard 與 Lint](#231-coding-standard-與-lint)
- [23.2 Conventional Commits](#232-conventional-commits)
- [23.3 Git Flow 與分支策略](#233-git-flow-與分支策略)
- [23.4 Release 與版本策略](#234-release-與版本策略)
- [23.5 Code Review 流程](#235-code-review-流程)
- [23.6 API 版本管理策略](#236-api-版本管理策略)
- [23.7 Feature Flag 管理](#237-feature-flag-管理)
- [23.8 國際化（i18n）](#238-國際化i18n)

### [第 24 章：完整企業級範例專案](#第-24-章完整企業級範例專案)
- [24.1 專案概覽](#241-專案概覽)
- [24.2 NestJS API 核心](#242-nestjs-api-核心)
- [24.3 認證模組](#243-認證模組)
- [24.4 Prisma Schema](#244-prisma-schema)
- [24.5 Redis 快取與 BullMQ 工作佇列](#245-redis-快取與-bullmq-工作佇列)
- [24.6 Docker Compose（完整開發環境）](#246-docker-compose完整開發環境)
- [24.7 GitHub Actions CI/CD](#247-github-actions-cicd)
- [24.8 監控與 Logging 整合](#248-監控與-logging-整合)
- [24.9 Order Module 完整實作](#249-order-module-完整實作)
- [24.10 完整測試範例](#2410-完整測試範例)

### [第 25 章：Appendix](#第-25-章appendix)
- [25.1 CLI 常用指令速查表](#251-cli-常用指令速查表)
- [25.2 Debug 技巧](#252-debug-技巧)
- [25.3 VS Code 推薦設定](#253-vs-code-推薦設定)
- [25.4 推薦套件與學習資源](#254-推薦套件與學習資源)

### [附錄：檢查清單（Checklist）](#附錄檢查清單checklist)
- [A. 新專案啟動檢查清單](#a-新專案啟動檢查清單)
- [B. Code Review 檢查清單](#b-code-review-檢查清單)
- [C. 上線前檢查清單](#c-上線前檢查清單)
- [D. 日常維運檢查清單](#d-日常維運檢查清單)
- [E. 安全性檢查清單](#e-安全性檢查清單)

---

## 第 1 章：Node.js 簡介

### 1.1 Node.js 是什麼

#### 定義

Node.js 是一個基於 **Chrome V8 引擎** 的 JavaScript 執行環境（Runtime），讓 JavaScript 能夠脫離瀏覽器在伺服器端執行。它採用 **事件驅動（Event-driven）** 與 **非阻塞 I/O（Non-blocking I/O）** 模型，特別適合建構高併發、I/O 密集型的網路應用程式。

#### 核心特性

| 特性 | 說明 |
|------|------|
| **單執行緒 + 事件迴圈** | 透過 Event Loop 處理大量併發連線，避免多執行緒上下文切換成本 |
| **非阻塞 I/O** | 所有 I/O 操作透過 libuv 非同步執行，主執行緒不會被阻塞 |
| **跨平台** | 支援 Windows、Linux、macOS，透過 libuv 抽象層實現 |
| **NPM 生態系** | 全球最大的開源套件管理生態系，超過 250 萬個套件 |
| **JavaScript 全端** | 前後端使用相同語言，降低技術棧切換成本 |
| **V8 引擎** | Google 開發的高效能 JavaScript 引擎，支援 JIT 編譯 |

#### 與其他後端平台比較

| 比較項目 | Node.js | Java / Spring Boot | Python / FastAPI | Go |
|----------|---------|-------------------|------------------|-----|
| **執行模型** | 單執行緒 + Event Loop | 多執行緒 + Thread Pool | 單執行緒 + async | Goroutine |
| **型別系統** | 動態（TypeScript 可選） | 強型別 | 動態（Type Hints） | 強型別 |
| **啟動速度** | 極快（毫秒級） | 較慢（秒級） | 快 | 極快 |
| **記憶體消耗** | 低（~30MB 起） | 高（~200MB 起） | 中（~50MB 起） | 極低（~5MB 起） |
| **適合場景** | API、即時應用、BFF | 企業核心業務 | ML、資料科學 | 高效能微服務 |
| **學習曲線** | 低 | 中高 | 低 | 中 |

---

### 1.2 Runtime 架構與 V8 Engine

#### Node.js Runtime 架構圖

```mermaid
graph TB
    subgraph "Node.js Runtime"
        subgraph "JavaScript 層"
            A[Application Code] --> B[Node.js Standard Library]
        end
        
        subgraph "Binding 層"
            B --> C[Node.js Bindings / Node-API]
        end
        
        subgraph "C/C++ 層"
            C --> D[V8 Engine]
            C --> E[libuv]
            C --> F[c-ares DNS]
            C --> G[OpenSSL]
            C --> H[zlib]
            C --> I[llhttp]
        end
        
        subgraph "作業系統"
            E --> J[epoll / kqueue / IOCP]
            D --> K[OS Memory / CPU]
        end
    end
    
    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style D fill:#FF9800,color:white
    style E fill:#FF9800,color:white
```

#### V8 Engine 運作原理

V8 是 Google 開發的高效能 JavaScript 引擎，採用 **即時編譯（JIT Compilation）** 技術：

```mermaid
flowchart LR
    A[JavaScript 原始碼] --> B[Parser]
    B --> C[AST 抽象語法樹]
    C --> D[Ignition 直譯器]
    D --> E[Bytecode 位元組碼]
    E --> F{Hot Code?}
    F -->|是| G[TurboFan 優化編譯器]
    G --> H[Optimized Machine Code]
    F -->|否| I[繼續直譯執行]
    H --> J{Deoptimize?}
    J -->|是| E
    J -->|否| K[高速執行]
```

**V8 關鍵組件**：

| 組件 | 功能 |
|------|------|
| **Ignition** | 直譯器，將 JavaScript 編譯為位元組碼，快速啟動 |
| **TurboFan** | 優化編譯器，將熱點程式碼編譯為機器碼，提升效能 |
| **Orinoco** | 垃圾回收器，採用分代式 GC（Young/Old Generation） |
| **Liftoff** | WebAssembly 基線編譯器 |

#### libuv 的角色

libuv 是 Node.js 的跨平台非同步 I/O 程式庫，負責：

- **Event Loop** 的實作
- **非同步檔案 I/O**（透過執行緒池）
- **非同步 DNS 解析**
- **非同步網路 I/O**（透過 epoll/kqueue/IOCP）
- **計時器管理**
- **子程序管理**
- **訊號處理**

```
┌─────────────────────────────────────────┐
│                  libuv                   │
├──────────┬──────────────┬───────────────┤
│  Network │  File System │   DNS/Other   │
│  (async) │  (thread pool)│  (thread pool)│
├──────────┼──────────────┼───────────────┤
│  epoll   │              │               │
│  kqueue  │  Thread Pool │  Thread Pool  │
│  IOCP    │  (4 threads) │               │
└──────────┴──────────────┴───────────────┘
```

> **⚠️ 實務注意**：libuv 預設執行緒池大小為 4。若應用程式有大量檔案 I/O 或 DNS 查詢，可透過 `UV_THREADPOOL_SIZE` 環境變數調整（最大 1024）。

---

### 1.3 Event Loop 運作機制

#### Event Loop 六個階段

```
   ┌───────────────────────────────┐
┌─▶│          timers               │  ← setTimeout, setInterval 回呼
│  └─────────────┬─────────────────┘
│  ┌─────────────┴─────────────────┐
│  │      pending callbacks        │  ← 系統層級回呼（TCP 錯誤等）
│  └─────────────┬─────────────────┘
│  ┌─────────────┴─────────────────┐
│  │        idle, prepare          │  ← 內部使用
│  └─────────────┬─────────────────┘
│  ┌─────────────┴─────────────────┐
│  │            poll               │  ← 擷取新的 I/O 事件
│  └─────────────┬─────────────────┘
│  ┌─────────────┴─────────────────┐
│  │            check              │  ← setImmediate 回呼
│  └─────────────┬─────────────────┘
│  ┌─────────────┴─────────────────┐
└──┤       close callbacks         │  ← socket.on('close') 等
   └───────────────────────────────┘
```

#### 各階段詳細說明

| 階段 | 觸發時機 | 典型回呼 |
|------|----------|----------|
| **timers** | setTimeout/setInterval 到期 | 計時器回呼函式 |
| **pending callbacks** | 上一輪延遲的 I/O 回呼 | TCP ECONNREFUSED 等 |
| **idle, prepare** | 每次 loop 前的內部準備 | 僅 Node.js 內部使用 |
| **poll** | 等待新 I/O 事件 | 檔案讀寫、網路回呼 |
| **check** | poll 階段結束後 | setImmediate 回呼 |
| **close callbacks** | 關閉事件 | socket.on('close') |

#### 執行順序範例

```javascript
// Event Loop 執行順序示範
console.log('1. 同步程式碼 - 開始');

setTimeout(() => {
  console.log('5. setTimeout (timers 階段)');
}, 0);

setImmediate(() => {
  console.log('6. setImmediate (check 階段)');
});

Promise.resolve().then(() => {
  console.log('3. Promise.then (Microtask)');
}).then(() => {
  console.log('4. Promise.then 鏈式 (Microtask)');
});

process.nextTick(() => {
  console.log('2. process.nextTick (最高優先 Microtask)');
});

console.log('1.5 同步程式碼 - 結束');

// 輸出順序：
// 1. 同步程式碼 - 開始
// 1.5 同步程式碼 - 結束
// 2. process.nextTick (最高優先 Microtask)
// 3. Promise.then (Microtask)
// 4. Promise.then 鏈式 (Microtask)
// 5. setTimeout (timers 階段)      ← 順序可能與 setImmediate 互換
// 6. setImmediate (check 階段)
```

#### Microtask vs Macrotask 優先級

```mermaid
graph TD
    A[每個 Event Loop 階段結束] --> B{有 process.nextTick?}
    B -->|是| C[執行所有 nextTick 回呼]
    C --> B
    B -->|否| D{有 Promise 微任務?}
    D -->|是| E[執行所有 Promise 回呼]
    E --> D
    D -->|否| F[進入下一個 Event Loop 階段]
```

> **⚠️ 關鍵規則**：
> 1. `process.nextTick` 優先於 Promise 微任務
> 2. 所有微任務在每個 Event Loop 階段之間清空
> 3. 不要在 `nextTick` 中遞迴呼叫，否則會餓死 Event Loop

---

### 1.4 Non-blocking I/O 模型

#### 阻塞 vs 非阻塞對比

```javascript
// ❌ 阻塞式 I/O（同步）— 絕對不要在生產環境使用
import { readFileSync } from 'node:fs';

const data = readFileSync('/path/to/large-file.txt', 'utf-8');  // 主執行緒被阻塞
console.log('檔案讀取完成');  // 必須等檔案讀完才執行

// ✅ 非阻塞式 I/O（非同步）
import { readFile } from 'node:fs/promises';

const data = await readFile('/path/to/large-file.txt', 'utf-8');  // 不阻塞主執行緒
console.log('檔案讀取完成');
```

#### I/O 效能對比

```
阻塞模型（傳統多執行緒）：
Thread 1: ████████████████░░░░░░░░  (等待 I/O)
Thread 2: ░░░░████████████████░░░░  (等待 I/O)
Thread 3: ░░░░░░░░████████████████  (等待 I/O)
→ 每個連線需要一個執行緒，資源消耗大

非阻塞模型（Node.js Event Loop）：
Main:     ██░██░██░██░██░██░██░██  (持續處理事件)
libuv:    ░██░░██░░██░░██░░██░░██  (背景 I/O)
→ 單執行緒處理所有連線，資源效率高
```

> **✅ 實務建議**：Node.js 可輕鬆處理 **10,000+ 併發連線**，但前提是不阻塞 Event Loop。

---

### 1.5 Node.js 適用場景與不適用場景

#### ✅ 適用場景

```mermaid
graph TD
    A[Node.js 適用場景] --> B[I/O 密集型應用]
    A --> C[即時應用]
    A --> D[API Gateway / BFF]
    A --> E[微服務]
    A --> F[Serverless]
    A --> G[CLI 工具]
    
    B --> B1[REST / GraphQL API]
    B --> B2[檔案上傳下載]
    C --> C1[WebSocket / Chat]
    C --> C2[即時通知推播]
    D --> D1[前端聚合層]
    E --> E1[輕量級服務]
    F --> F1[AWS Lambda / Azure Functions]
    G --> G1[開發工具 / 腳手架]
```

| 場景 | 說明 | 範例 |
|------|------|------|
| **REST API** | 高併發、低延遲的 API 服務 | 電商商品查詢 API |
| **即時通訊** | WebSocket 長連線 | 聊天室、協作編輯 |
| **BFF** | 前端聚合層，整合多個微服務 | Mobile BFF、Web BFF |
| **串流處理** | 大檔案串流、影音串流代理 | 檔案上傳、影片轉碼代理 |
| **SSR** | Server-Side Rendering | Next.js、Nuxt.js |
| **Serverless** | 函式即服務 | AWS Lambda Handler |

#### ❌ 不適用場景

| 場景 | 原因 | 替代方案 |
|------|------|----------|
| **CPU 密集型運算** | 阻塞 Event Loop | Go、Rust、Worker Threads |
| **大規模科學計算** | V8 記憶體限制（預設 ~1.5GB） | Python + NumPy、C++ |
| **複雜企業業務邏輯** | 缺乏成熟的 ORM 與 Transaction 支援 | Java + Spring Boot |
| **影像/影片處理** | CPU 密集 | FFmpeg + Go/Rust |

> **⚠️ 例外**：Node.js v26 已強化 Worker Threads，對 CPU 密集任務可透過多執行緒卸載。但架構設計仍應以 I/O 密集為主。

---

### 1.6 Node.js LTS 與 Current 版本策略

#### 版本發佈週期

```mermaid
gantt
    title Node.js 版本生命週期（2024-2028）
    dateFormat YYYY-MM
    section v22 LTS
    Active LTS    :active, 2024-10, 2026-04
    Maintenance   :2026-04, 2027-04
    section v24 LTS
    Active LTS    :active, 2025-10, 2027-04
    Maintenance   :2027-04, 2028-04
    section v26 LTS
    Current       :2026-04, 2026-10
    Active LTS    :active, 2026-10, 2028-04
    Maintenance   :2028-04, 2029-04
```

#### 版本類型

| 類型 | 說明 | 適用環境 |
|------|------|----------|
| **Current** | 最新功能版本，每 6 個月發佈 | 開發/測試環境 |
| **Active LTS** | 長期支援版本，穩定可靠 | **生產環境推薦** |
| **Maintenance LTS** | 僅修復關鍵安全漏洞 | 舊系統維護 |

#### ✅ 企業版本策略建議

1. **生產環境**：一律使用 Active LTS 版本（目前為 v26）
2. **升級節奏**：每個 LTS 版本升級一次，跳過 Current
3. **測試先行**：升級前在 CI/CD 環境完整測試
4. **版本鎖定**：使用 `.nvmrc` 或 `package.json engines` 鎖定版本

```json
// package.json — 鎖定 Node.js 版本
{
  "engines": {
    "node": ">=26.0.0 <27.0.0",
    "pnpm": ">=9.0.0"
  }
}
```

```bash
# .nvmrc — 鎖定 nvm 使用的版本
v26.1.0
```

#### 章節小練習

1. 解釋 Node.js 的 Event Loop 為何不適合 CPU 密集型任務？
2. 列出三個適合用 Node.js 建構的企業應用場景。
3. 說明 `process.nextTick` 與 `Promise.then` 的優先級差異。

#### 實務注意事項

> - 新專案務必使用最新 LTS 版本
> - 不要在生產環境使用 Current 版本
> - 建立版本升級的 SOP，包含回歸測試流程
> - 監控 Node.js 官方安全公告 (https://nodejs.org/en/blog/vulnerability)

---

## 第 2 章：Node.js 生態系

### 2.1 npm

#### 概述

npm（Node Package Manager）是 Node.js 的預設套件管理器，也是世界上最大的軟體註冊表（Registry），截至 2026 年擁有超過 **250 萬** 個套件。

#### 核心概念

```mermaid
graph TD
    A[npm 生態系] --> B[npm CLI]
    A --> C[npm Registry]
    A --> D[package.json]
    A --> E[node_modules]
    
    B --> B1[install / add]
    B --> B2[run / exec]
    B --> B3[publish]
    C --> C1[Public Registry]
    C --> C2[Private Registry]
    D --> D1[dependencies]
    D --> D2[devDependencies]
    D --> D3[scripts]
```

#### 常用指令

```bash
# 初始化專案
npm init -y

# 安裝套件
npm install express                  # 安裝到 dependencies
npm install -D typescript            # 安裝到 devDependencies
npm install -g pnpm                  # 全域安裝

# 管理依賴
npm update                           # 更新所有套件
npm outdated                         # 檢查過時套件
npm audit                            # 安全漏洞掃描
npm audit fix                        # 自動修復漏洞

# 執行腳本
npm run build                        # 執行 scripts.build
npm test                             # 執行 scripts.test（簡寫）
npm start                            # 執行 scripts.start（簡寫）

# 套件資訊
npm info express                     # 查看套件資訊
npm ls --depth=0                     # 列出已安裝的頂層套件
npm why express                      # 為何安裝此套件
```

#### npm 設定檔（.npmrc）

```ini
# .npmrc — 專案層級設定
registry=https://registry.npmjs.org/
# 企業私有 Registry
@company:registry=https://npm.company.com/
# 嚴格引擎版本檢查
engine-strict=true
# 精確版本安裝
save-exact=true
# 自動安裝 peer dependencies
auto-install-peers=true
```

---

### 2.2 yarn

#### 概述

Yarn 由 Facebook（Meta）於 2016 年推出，旨在解決早期 npm 的速度和一致性問題。目前 Yarn 4（Berry）已完全重寫。

#### Yarn 4 (Berry) 特色

| 特性 | 說明 |
|------|------|
| **Plug'n'Play (PnP)** | 移除 node_modules，使用 `.pnp.cjs` 直接映射 |
| **Zero-Installs** | 將依賴提交到 Git，CI/CD 免安裝 |
| **Workspaces** | 原生 Monorepo 支援 |
| **Constraints** | 可設定依賴一致性約束 |

```bash
# Yarn 4 基本指令
yarn init                            # 初始化
yarn add express                     # 安裝
yarn add -D typescript               # 開發依賴
yarn remove express                  # 移除
yarn up express                      # 更新
yarn dlx create-next-app             # 臨時執行（等同 npx）
```

#### ⚠️ 企業注意事項

> Yarn PnP 模式與部分套件不相容，若團隊使用，建議先做完整相容性測試。

---

### 2.3 pnpm

#### 概述

pnpm 是效能導向的套件管理器，透過**內容定址儲存（Content-Addressable Storage）** 與**硬連結（Hard Links）** 實現高效磁碟使用。

#### 核心優勢

```mermaid
graph LR
    subgraph "npm / yarn"
        A1[project-a/node_modules/lodash] 
        A2[project-b/node_modules/lodash]
        A3[project-c/node_modules/lodash]
    end
    
    subgraph "pnpm"
        B1[~/.pnpm-store/lodash@4.17.21]
        B2[project-a/node_modules/.pnpm/lodash] -->|hard link| B1
        B3[project-b/node_modules/.pnpm/lodash] -->|hard link| B1
        B4[project-c/node_modules/.pnpm/lodash] -->|hard link| B1
    end
```

| 比較 | npm | yarn | **pnpm** |
|------|-----|------|----------|
| **安裝速度** | 基準 | 快 20% | **快 50-100%** |
| **磁碟用量** | 每專案完整副本 | 每專案完整副本 | **共享硬連結** |
| **幽靈依賴** | 允許 | 允許 | **嚴格禁止** |
| **Monorepo** | Workspaces | Workspaces | **原生最佳** |

#### 常用指令

```bash
# 安裝 pnpm
npm install -g pnpm
# 或使用 Corepack
corepack enable && corepack prepare pnpm@latest --activate

# 基本操作
pnpm install                         # 安裝所有依賴
pnpm add express                     # 安裝
pnpm add -D typescript               # 開發依賴
pnpm remove express                  # 移除
pnpm update                          # 更新
pnpm store prune                     # 清理未引用的套件

# Monorepo（workspace）
pnpm add express --filter @app/api   # 指定 workspace 安裝
pnpm -r run build                    # 所有 workspace 執行 build
pnpm -r --filter @app/api run test   # 指定 workspace 執行 test
```

#### pnpm workspace 設定

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
  - 'tools/*'
```

#### ✅ 企業選型建議

> **2026 年推薦使用 pnpm**：
> 1. 安裝速度最快，節省 CI/CD 時間
> 2. 嚴格依賴管理，杜絕幽靈依賴
> 3. 原生 Monorepo 支援最佳
> 4. 磁碟空間節省 50%+

---

### 2.4 npx 與 corepack

#### npx

npx 是 npm 內建的套件執行器，用於**臨時執行**套件指令而不需全域安裝。

```bash
# 常見用法
npx create-next-app@latest my-app    # 執行腳手架
npx tsc --init                       # 初始化 tsconfig
npx eslint .                         # 執行 lint
npx prisma migrate dev               # 執行 Prisma 遷移

# 指定版本
npx -p typescript@5.7 tsc --version
```

#### corepack

Corepack 是 Node.js v16.9+ 內建的套件管理器管理工具，用於確保團隊使用一致的套件管理器版本。

```bash
# 啟用 Corepack
corepack enable

# 設定專案使用的套件管理器（寫入 package.json）
corepack use pnpm@9.15.0

# package.json 中的設定
{
  "packageManager": "pnpm@9.15.0+sha512.xxx"
}
```

> **✅ 企業建議**：所有專案都應使用 `corepack` 搭配 `packageManager` 欄位，確保團隊成員使用相同版本的套件管理器。

---

### 2.5 package.json 完整解析

#### 完整範例

```json
{
  "name": "@company/api-server",
  "version": "1.0.0",
  "description": "企業級 API 服務",
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs",
      "types": "./dist/index.d.ts"
    }
  },
  "scripts": {
    "dev": "tsx watch src/main.ts",
    "build": "tsc && tsc-alias",
    "start": "node dist/main.js",
    "test": "vitest",
    "test:cov": "vitest --coverage",
    "lint": "eslint src/ --fix",
    "format": "prettier --write 'src/**/*.ts'",
    "prepare": "husky",
    "db:migrate": "prisma migrate dev",
    "db:generate": "prisma generate"
  },
  "dependencies": {
    "@nestjs/common": "^11.0.0",
    "@nestjs/core": "^11.0.0",
    "@nestjs/platform-fastify": "^11.0.0",
    "@prisma/client": "^6.0.0",
    "ioredis": "^5.4.0",
    "pino": "^9.0.0",
    "zod": "^3.24.0"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "eslint": "^9.0.0",
    "husky": "^9.0.0",
    "lint-staged": "^15.0.0",
    "prettier": "^3.4.0",
    "prisma": "^6.0.0",
    "tsx": "^4.19.0",
    "typescript": "^5.7.0",
    "vitest": "^3.0.0"
  },
  "engines": {
    "node": ">=26.0.0",
    "pnpm": ">=9.0.0"
  },
  "packageManager": "pnpm@9.15.0",
  "license": "UNLICENSED",
  "private": true
}
```

#### 關鍵欄位說明

| 欄位 | 用途 | 建議 |
|------|------|------|
| `type` | 模組系統（`module` / `commonjs`） | 新專案用 `"module"` |
| `exports` | 條件式匯出，取代 `main` | 支援 ESM/CJS 雙模式 |
| `engines` | 限制 Node.js 版本 | 搭配 `engine-strict=true` |
| `packageManager` | 鎖定套件管理器版本 | 搭配 Corepack |
| `private` | 防止意外發佈 | 應用程式設 `true` |

---

### 2.6 package-lock.json 與依賴鎖定

#### 為什麼需要 Lock 檔案

```mermaid
graph TD
    A[沒有 Lock 檔案] --> B[npm install]
    B --> C[解析 ^3.0.0 → 3.2.1]
    B --> D[下次 npm install]
    D --> E[解析 ^3.0.0 → 3.3.0]
    E --> F[版本不一致！Bug 風險]
    
    G[有 Lock 檔案] --> H[npm ci]
    H --> I[精確安裝 3.2.1]
    H --> J[每次安裝版本相同]
    J --> K[一致且可重現]
    
    style F fill:#ffcccc
    style K fill:#ccffcc
```

#### ✅ 最佳實務

```bash
# 開發環境：使用 install（會更新 lock 檔案）
pnpm install

# CI/CD 環境：使用 frozen-lockfile（嚴格鎖定）
pnpm install --frozen-lockfile
```

| 指令 | 場景 | Lock 檔案處理 |
|------|------|--------------|
| `pnpm install` | 本地開發 | 可能更新 |
| `pnpm install --frozen-lockfile` | CI/CD | 不允許更新，不一致則失敗 |
| `npm ci` | CI/CD（npm） | 刪除 node_modules 後精確安裝 |

> **⚠️ 重要**：Lock 檔案必須提交到 Git！

---

### 2.7 Semantic Versioning（語意化版本）

#### 版本格式

```
MAJOR.MINOR.PATCH
  │      │     │
  │      │     └── Bug 修復（向下相容）
  │      └──────── 新功能（向下相容）
  └─────────────── 破壞性變更（不相容）

範例：3.2.1
  3 = MAJOR（有 Breaking Change）
  2 = MINOR（新增功能）
  1 = PATCH（Bug 修復）
```

#### 版本範圍符號

| 符號 | 範例 | 說明 | 允許安裝 |
|------|------|------|----------|
| `^` | `^3.2.1` | 允許 MINOR 和 PATCH 更新 | `3.2.1` ~ `3.x.x` |
| `~` | `~3.2.1` | 僅允許 PATCH 更新 | `3.2.1` ~ `3.2.x` |
| 精確 | `3.2.1` | 精確版本 | 僅 `3.2.1` |
| `>=` | `>=3.2.1` | 大於等於 | `3.2.1` 以上全部 |
| `*` | `*` | 任意版本 | 全部 |

#### ✅ 企業建議

```ini
# .npmrc
save-exact=true    # 安裝時精確版本（不加 ^ 或 ~）
```

> 使用精確版本 + Lock 檔案，確保所有環境完全一致。

#### 章節小練習

1. 解釋 `^3.2.1` 與 `~3.2.1` 的差異。
2. 說明 pnpm 如何節省磁碟空間。
3. 為什麼 CI/CD 應使用 `--frozen-lockfile`？

#### 實務注意事項

> - 所有專案使用 `.npmrc` 統一設定
> - Lock 檔案必須提交到版本控制
> - 定期執行 `npm audit` 或 `pnpm audit` 掃描漏洞
> - 使用 Renovate 或 Dependabot 自動更新依賴

---

## 第 3 章：Node.js 安裝與環境建立

### 3.1 Windows 環境安裝

#### 方法一：官方安裝檔

```powershell
# 1. 從官方下載 LTS 版本
# https://nodejs.org/en/download/

# 2. 執行 .msi 安裝檔，勾選以下選項：
#    ✅ Node.js runtime
#    ✅ npm package manager
#    ✅ Add to PATH
#    ✅ Automatically install necessary tools (Chocolatey)

# 3. 驗證安裝
node --version    # v26.1.0
npm --version     # 10.x.x
```

#### 方法二：使用 winget（推薦）

```powershell
# 使用 Windows Package Manager
winget install OpenJS.NodeJS.LTS

# 驗證
node --version
npm --version
```

#### 方法三：使用 Chocolatey

```powershell
# 安裝 Chocolatey（需管理員權限）
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 安裝 Node.js LTS
choco install nodejs-lts -y

# 驗證
node --version
```

---

### 3.2 Linux 環境安裝

#### Ubuntu / Debian

```bash
# 方法一：使用 NodeSource（推薦）
curl -fsSL https://deb.nodesource.com/setup_26.x | sudo -E bash -
sudo apt-get install -y nodejs

# 方法二：使用 snap
sudo snap install node --classic --channel=26

# 驗證
node --version
npm --version
```

#### CentOS / RHEL / Fedora

```bash
# 使用 NodeSource
curl -fsSL https://rpm.nodesource.com/setup_26.x | sudo bash -
sudo yum install -y nodejs

# 或 dnf（Fedora）
sudo dnf install -y nodejs
```

#### Alpine Linux（Docker 常用）

```dockerfile
# Dockerfile 中使用
FROM node:26-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
CMD ["node", "dist/main.js"]
```

---

### 3.3 macOS 環境安裝

#### 方法一：Homebrew（推薦）

```bash
# 安裝 Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安裝 Node.js LTS
brew install node@26

# 加入 PATH（若未自動加入）
echo 'export PATH="/opt/homebrew/opt/node@26/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 驗證
node --version
npm --version
```

#### 方法二：pkg 安裝檔

```bash
# 從官方下載 macOS .pkg 安裝檔
# https://nodejs.org/en/download/
# 雙擊安裝，會自動設定 PATH
```

---

### 3.4 nvm — Node Version Manager

#### 概述

nvm 是最廣泛使用的 Node.js 版本管理工具，支援在同一台機器上安裝和切換多個 Node.js 版本。

#### 安裝

```bash
# Linux / macOS
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# 重新載入 shell 設定
source ~/.bashrc   # 或 source ~/.zshrc

# Windows（使用 nvm-windows）
# 下載 https://github.com/coreybutler/nvm-windows/releases
winget install CoreyButler.NVMforWindows
```

#### 常用指令

```bash
# 安裝 Node.js 版本
nvm install 26                       # 安裝 v26 最新版
nvm install 26.1.0                   # 安裝特定版本
nvm install --lts                    # 安裝最新 LTS

# 切換版本
nvm use 26                           # 切換到 v26
nvm use --lts                        # 切換到最新 LTS

# 管理版本
nvm ls                               # 列出已安裝版本
nvm ls-remote                        # 列出所有可用版本
nvm alias default 26                 # 設定預設版本
nvm uninstall 20                     # 移除版本

# 自動切換（使用 .nvmrc）
echo "v26.1.0" > .nvmrc
nvm use                              # 自動讀取 .nvmrc
```

#### .nvmrc 配置

```bash
# .nvmrc（放在專案根目錄）
v26.1.0
```

> **⚠️ 注意**：nvm-windows 和 nvm（Linux/macOS）是不同的專案，指令略有差異。

---

### 3.5 fnm — Fast Node Manager

#### 概述

fnm（Fast Node Manager）是用 Rust 編寫的高速 Node.js 版本管理器，安裝速度和切換速度都優於 nvm。

#### 安裝

```bash
# macOS / Linux
curl -fsSL https://fnm.vercel.app/install | bash

# Windows（PowerShell）
winget install Schniz.fnm

# 或使用 Chocolatey
choco install fnm

# 設定 shell 自動切換
# Bash
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.bashrc

# Zsh
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.zshrc

# PowerShell（加入 $PROFILE）
fnm env --use-on-cd --shell power-shell | Out-String | Invoke-Expression
```

#### 常用指令

```bash
# 安裝與切換
fnm install 26                       # 安裝
fnm use 26                           # 切換
fnm default 26                       # 設定預設
fnm ls                               # 列出已安裝版本
fnm ls-remote                        # 列出可用版本

# 自動切換（.node-version 或 .nvmrc）
echo "v26.1.0" > .node-version
# 進入目錄時自動切換（需設定 --use-on-cd）
```

#### fnm vs nvm 對比

| 特性 | nvm | fnm |
|------|-----|-----|
| **安裝速度** | 慢 | 極快（Rust 編寫） |
| **切換速度** | ~200ms | ~1ms |
| **跨平台** | 不同版本 | 統一版本 |
| **Shell 支援** | Bash/Zsh | Bash/Zsh/Fish/PowerShell |
| **自動切換** | 需額外設定 | 內建 `--use-on-cd` |

> **✅ 推薦**：新團隊建議使用 fnm，效能優越且跨平台統一。

---

### 3.6 Volta — 可靠的 JavaScript 工具管理器

#### 概述

Volta 不僅管理 Node.js 版本，還能管理 npm/yarn/pnpm 的版本，並將工具版本鎖定在 `package.json` 中。

#### 安裝

```bash
# macOS / Linux
curl https://get.volta.sh | bash

# Windows
winget install Volta.Volta
```

#### 使用方式

```bash
# 安裝 Node.js
volta install node@26               # 安裝
volta pin node@26.1.0               # 鎖定到 package.json

# 安裝套件管理器
volta install pnpm@9                # 安裝 pnpm
volta pin pnpm@9.15.0               # 鎖定版本

# package.json 中的設定（自動產生）
{
  "volta": {
    "node": "26.1.0",
    "pnpm": "9.15.0"
  }
}
```

#### Volta 的獨特優勢

| 特性 | 說明 |
|------|------|
| **工具鎖定** | 版本資訊寫入 package.json，團隊自動同步 |
| **零設定切換** | 進入目錄自動切換，無需 `.nvmrc` |
| **全域工具隔離** | 每個專案的全域工具版本獨立 |
| **效能** | Rust 編寫，切換速度極快 |

---

### 3.7 企業環境設定與內部 Registry

#### 私有 npm Registry 設定

```ini
# .npmrc（專案層級，提交到 Git）
# 企業私有 Registry
@company:registry=https://npm.internal.company.com/
# 公開套件仍使用官方 Registry
registry=https://registry.npmjs.org/
# 驗證 Token（CI/CD 用環境變數）
//npm.internal.company.com/:_authToken=${NPM_TOKEN}

# 嚴格設定
engine-strict=true
save-exact=true
auto-install-peers=true
```

#### Proxy 設定（企業內網）

```ini
# .npmrc — 設定 HTTP Proxy
proxy=http://proxy.company.com:8080
https-proxy=http://proxy.company.com:8080
no-proxy=localhost,127.0.0.1,.company.com
# CA 憑證（自簽憑證環境）
cafile=/path/to/company-ca.pem
strict-ssl=true
```

#### ✅ 企業環境 Checklist

- [ ] 選定 Node.js 版本管理器（推薦 fnm 或 Volta）
- [ ] 設定 `.nvmrc` 或 `volta` 鎖定版本
- [ ] 配置 `.npmrc` 設定私有 Registry
- [ ] 設定 Proxy（若適用）
- [ ] 配置 Corepack 鎖定套件管理器版本
- [ ] 建立 `engines` 欄位限制 Node.js 版本
- [ ] 在 CI/CD 環境驗證設定

#### 章節小練習

1. 使用 fnm 安裝 Node.js v26 並設為預設。
2. 建立 `.npmrc` 設定精確版本安裝。
3. 說明 Volta 與 nvm 的主要差異。

#### 實務注意事項

> - Windows 環境推薦使用 fnm 或 Volta（避免 nvm-windows 的相容性問題）
> - 企業內網環境務必設定 Proxy 和 CA 憑證
> - 所有設定檔（`.nvmrc`、`.npmrc`）應提交到版本控制
> - 敏感資訊（Token、密碼）使用環境變數，不可寫在設定檔

---

## 第 4 章：TypeScript 開發平台

### 4.1 為什麼企業專案必須使用 TypeScript

#### TypeScript 帶來的價值

```mermaid
graph TD
    A[TypeScript 核心價值] --> B[型別安全]
    A --> C[IDE 開發體驗]
    A --> D[重構信心]
    A --> E[團隊協作]
    A --> F[文件化效果]
    
    B --> B1[編譯期攔截錯誤]
    B --> B2[消除 null/undefined 地雷]
    C --> C1[自動補全]
    C --> C2[即時錯誤提示]
    D --> D1[大規模重構不漏改]
    E --> E1[介面即契約]
    F --> F1[型別即文件]
```

#### 實際效益數據

| 指標 | JavaScript | TypeScript | 改善 |
|------|-----------|-----------|------|
| 執行時期錯誤 | 基準 | 減少 15-20% | ↓ |
| 程式碼審查時間 | 基準 | 減少 30% | ↓ |
| 重構信心指數 | 低 | 高 | ↑ |
| 新人上手時間 | 較長 | 較短 | ↓ 20% |
| Bug 回報率 | 基準 | 減少 25% | ↓ |

#### 對比範例

```javascript
// ❌ JavaScript — 隱藏的地雷
function processUser(user) {
  return user.name.toUpperCase();   // user.name 可能是 undefined → Runtime Error
}
processUser({ username: 'John' }); // 沒有任何警告！
```

```typescript
// ✅ TypeScript — 編譯期攔截
interface User {
  id: number;
  name: string;
  email: string;
}

function processUser(user: User): string {
  return user.name.toUpperCase();   // 安全：name 一定存在
}
processUser({ username: 'John' }); // ❌ 編譯錯誤：缺少 id, name, email
```

---

### 4.2 tsconfig.json 設計原則

#### 企業級 tsconfig.json

```json
{
  "compilerOptions": {
    // === 目標環境 ===
    "target": "ES2024",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2024"],

    // === 輸出設定 ===
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,

    // === 嚴格模式（全部必開）===
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,

    // === 額外檢查 ===
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": true,

    // === 模組解析 ===
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "resolveJsonModule": true,

    // === 裝飾器（NestJS 需要）===
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,

    // === 效能與其他 ===
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "incremental": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "test"]
}
```

#### 關鍵設定說明

| 設定 | 值 | 必要性 | 說明 |
|------|------|--------|------|
| `strict` | `true` | **必須** | 開啟所有嚴格檢查 |
| `noUncheckedIndexedAccess` | `true` | **強烈建議** | 陣列/物件索引存取加入 `undefined` |
| `exactOptionalPropertyTypes` | `true` | 建議 | 區分 `undefined` 與「不存在」 |
| `noImplicitOverride` | `true` | 建議 | 覆寫父類方法必須標示 `override` |
| `moduleResolution` | `NodeNext` | **必須** | Node.js ESM 相容 |

---

### 4.3 ESM 與 CommonJS 互操作性

#### 模組系統比較

| 特性 | CommonJS (CJS) | ES Modules (ESM) |
|------|---------------|------------------|
| **語法** | `require()` / `module.exports` | `import` / `export` |
| **載入方式** | 同步 | 非同步 |
| **靜態分析** | 不支援 | 支援（Tree Shaking） |
| **Top-level await** | 不支援 | 支援 |
| **Node.js 預設** | 預設（無 `"type": "module"`） | 需設定 `"type": "module"` |

#### 互操作性處理

```typescript
// ESM 中引入 CJS 模組
import express from 'express';           // ✅ default import
import { Router } from 'express';        // ✅ named import（esModuleInterop）

// 動態引入 CJS（當 named import 失敗時）
const pkg = await import('some-cjs-package');
const { feature } = pkg.default;

// 在 ESM 中使用 __dirname / __filename（CJS 專有）
import { fileURLToPath } from 'node:url';
import { dirname } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Node.js v26 也可使用 import.meta.dirname
const dir = import.meta.dirname;         // v21+ 原生支援
```

#### ✅ 遷移建議

```json
// package.json — 新專案一律使用 ESM
{
  "type": "module"
}
```

> **企業策略**：新專案使用 ESM；舊專案維持 CJS 但逐步遷移。混用時注意 `.mjs` / `.cjs` 副檔名。

---

### 4.4 ts-node 與 tsx 開發工具

#### ts-node

```bash
# 安裝
pnpm add -D ts-node

# 執行 TypeScript
npx ts-node src/main.ts

# 搭配 ESM
npx ts-node --esm src/main.ts

# tsconfig 設定
# 需要 "ts-node" 區段
{
  "ts-node": {
    "esm": true,
    "transpileOnly": true
  }
}
```

#### tsx（推薦）

tsx 是基於 esbuild 的 TypeScript 執行器，速度遠快於 ts-node。

```bash
# 安裝
pnpm add -D tsx

# 執行
npx tsx src/main.ts

# Watch 模式（開發推薦）
npx tsx watch src/main.ts

# 在 package.json 中設定
{
  "scripts": {
    "dev": "tsx watch src/main.ts",
    "start:dev": "tsx --env-file=.env src/main.ts"
  }
}
```

#### ts-node vs tsx 對比

| 特性 | ts-node | tsx |
|------|---------|-----|
| **速度** | 慢（完整型別檢查） | 極快（esbuild 轉譯） |
| **型別檢查** | 支援（預設開啟） | 不支援（僅轉譯） |
| **ESM 支援** | 需額外設定 | 原生支援 |
| **Watch 模式** | 需搭配 nodemon | 內建 |
| **設定複雜度** | 高 | 低（零設定） |

> **✅ 推薦**：開發環境使用 `tsx`（速度快），型別檢查交給 IDE 和 CI/CD 中的 `tsc --noEmit`。

---

### 4.5 SWC 與 esbuild 高速編譯器

#### esbuild

```bash
# 安裝
pnpm add -D esbuild

# 建置指令
npx esbuild src/main.ts --bundle --platform=node --target=node26 --outdir=dist

# package.json scripts
{
  "scripts": {
    "build": "esbuild src/main.ts --bundle --platform=node --target=node26 --outdir=dist --sourcemap"
  }
}
```

#### SWC

```bash
# 安裝
pnpm add -D @swc/core @swc/cli

# 建置
npx swc src -d dist

# .swcrc 設定
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "decorators": true,
      "dynamicImport": true
    },
    "transform": {
      "legacyDecorator": true,
      "decoratorMetadata": true
    },
    "target": "es2024"
  },
  "module": {
    "type": "es6"
  },
  "sourceMaps": true
}
```

#### 編譯器效能對比

| 編譯器 | 語言 | 速度（相對 tsc） | 型別檢查 | 裝飾器支援 |
|--------|------|-----------------|---------|-----------|
| **tsc** | TypeScript | 1x（基準） | ✅ | ✅ |
| **esbuild** | Go | ~100x | ❌ | ❌ |
| **SWC** | Rust | ~70x | ❌ | ✅ |

> **✅ 企業建議**：
> - 建置：使用 SWC（支援裝飾器） 或 esbuild
> - 型別檢查：在 CI/CD 中執行 `tsc --noEmit`
> - 開發：使用 tsx（基於 esbuild）

---

### 4.6 Node.js v26 原生 TypeScript 支援

#### 概述

從 Node.js v22.6.0 開始提供實驗性 TypeScript 支援，**v26 已將 Type Stripping 標記為 Stability 2（Stable）**。這意味著在 Node.js v26+ 中，無需任何旗標即可直接執行 `.ts` 檔案：

```bash
# Node.js v22-v25：需要實驗性旗標
node --experimental-strip-types src/main.ts

# Node.js v26+：直接執行（Stable 穩定功能）
node src/main.ts
node src/module.mts   # ES Module
node src/legacy.cts   # CommonJS
```

#### 工作原理

Node.js 原生 TypeScript 支援採用**型別剝離（Type Stripping）** 策略：

- **移除所有行內型別標注**，以空白字元取代（保持行號一致，無需 Source Map）
- **不執行型別檢查** — 型別檢查應在 CI/CD 中由 `tsc --noEmit` 負責
- **不讀取 `tsconfig.json`** — 不支援 `paths`、`baseUrl`、舊版語法降級等功能
- **不支援 `node_modules` 中的 TypeScript** — 防止套件作者發佈未編譯的 TypeScript

#### 支援的檔案類型與模組系統

| 副檔名 | 模組系統 | 說明 |
|---------|----------|------|
| `.ts` | 依 `package.json` 的 `"type"` 決定 | 與 `.js` 相同邏輯 |
| `.mts` | ES Modules | 對應 `.mjs`，始終為 ESM |
| `.cts` | CommonJS | 對應 `.cjs`，始終為 CJS |
| `.tsx` | **不支援** | Node.js 不支援 `.tsx` 檔案 |

> **重要**：`import` 語句中必須使用完整副檔名：`import './file.ts'`，而非 `import './file'`。

#### 支援與不支援的語法

```typescript
// ✅ 支援的語法（可直接剝離的型別標注）
const name: string = 'hello';
function greet(name: string): string { return `Hi ${name}`; }
interface User { id: number; name: string; }
type Result<T> = { data: T; error?: string };
import type { Config } from './config.ts';
import { fn, type FnParams } from './utils.ts';  // inline type import

// ❌ 不支援的語法（會產生 ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX 錯誤）
enum Status { Active, Inactive }           // Enum 需要程式碼生成
namespace App { export let x = 1; }        // 含運行時程式碼的 namespace
class User { constructor(public name: string) {} }  // 參數屬性
import Foo = require('foo');               // Import 別名

// ✅ 僅含型別的 namespace 是允許的
namespace TypeOnly {
  export type A = string;
}
```

> **Decorators（裝飾器）** 目前為 TC39 Stage 3 提案，Node.js 不提供轉換或 polyfill。
> 待 JavaScript 原生支援裝飾器後，Node.js 才會支援。

#### 型別匯入必須使用 `type` 關鍵字

由於型別剝離的特性，匯入型別時**必須**使用 `type` 關鍵字，否則會在執行期產生錯誤：

```typescript
// ✅ 正確寫法
import type { Type1, Type2 } from './module.ts';
import { fn, type FnParams } from './fn.ts';

// ❌ 錯誤寫法（會在執行期失敗）
import { Type1, Type2 } from './module.ts';   // Type1/Type2 是型別，但未標記
```

> 建議在 `tsconfig.json` 中啟用 `verbatimModuleSyntax` 以強制此行為。

#### 建議的 `tsconfig.json` 設定

Node.js 官方建議使用 TypeScript 5.8+ 搭配以下設定：

```json
{
  "compilerOptions": {
    "noEmit": true,
    "target": "esnext",
    "module": "nodenext",
    "rewriteRelativeImportExtensions": true,
    "erasableSyntaxOnly": true,
    "verbatimModuleSyntax": true
  }
}
```

| 選項 | 說明 |
|------|------|
| `erasableSyntaxOnly` | 限制只使用可剝離的語法，禁止 `enum` 等需要轉換的功能 |
| `verbatimModuleSyntax` | 強制匯入型別時使用 `type` 關鍵字 |
| `rewriteRelativeImportExtensions` | 允許 `tsc` 在編譯時處理 `.ts` 副檔名引用 |
| `noEmit` | 僅用於型別檢查，不輸出 `.js` 檔案（適合只用 `node` 執行的場景） |

#### `--eval` 與 STDIN 支援

型別剝離功能也適用於 `--eval` 和 STDIN 輸入，模組系統由 `--input-type` 決定：

```bash
# 透過 --eval 執行 TypeScript
node --input-type=module -e "const x: number = 42; console.log(x);"

# 透過 STDIN
echo "const x: number = 42; console.log(x);" | node --input-type=module
```

> **注意**：TypeScript 語法在 REPL、`--check` 和 `inspect` 模式中**不受支援**。

#### 路徑別名（Paths Aliases）

`tsconfig.json` 的 `paths` 設定不會被 Node.js 處理。替代方案是使用 `package.json` 的 [Subpath Imports](https://nodejs.org/docs/latest/api/packages.html#subpath-imports)（需以 `#` 開頭）：

```json
// package.json
{
  "imports": {
    "#utils/*": "./src/utils/*.ts",
    "#models/*": "./src/models/*.ts"
  }
}
```

```typescript
// 使用 subpath import（替代 tsconfig paths）
import { validate } from '#utils/validator.ts';
```

#### 完整 TypeScript 支援方案

對於需要完整 TypeScript 功能（包含 `tsconfig.json` 整合、`enum`、裝飾器等）的專案，建議使用第三方工具：

```bash
# 安裝 tsx（基於 esbuild，推薦）
npm install --save-dev tsx

# 使用 tsx 執行
npx tsx your-file.ts

# 或透過 node --import
node --import=tsx your-file.ts
```

#### 實務建議

| 場景 | 建議方案 |
|------|----------|
| 簡單腳本、CLI 工具 | Node.js 原生型別剝離（`node file.ts`） |
| 企業應用程式 | tsx + `tsconfig.json` 完整整合 |
| 建置產出 | SWC 或 esbuild 進行編譯 |
| 型別檢查 | CI/CD 中執行 `tsc --noEmit` |

> **企業建議**：即使 Node.js 原生支援已穩定，生產環境仍建議將 TypeScript 預編譯為 JavaScript 後部署，以確保最佳效能和可攜性。

---

### 4.7 型別設計與 Domain Model 最佳實務

#### Branded Types（品牌型別）

```typescript
// 防止不同 ID 型別混用
type UserId = string & { readonly __brand: 'UserId' };
type OrderId = string & { readonly __brand: 'OrderId' };

function createUserId(id: string): UserId {
  return id as UserId;
}

function createOrderId(id: string): OrderId {
  return id as OrderId;
}

function getOrder(orderId: OrderId) { /* ... */ }

const userId = createUserId('user-123');
const orderId = createOrderId('order-456');

// getOrder(userId);  // ❌ 編譯錯誤！型別不相容
getOrder(orderId);    // ✅ 正確
```

#### Zod 執行時期驗證

```typescript
import { z } from 'zod';

// 定義 Schema（同時作為型別和驗證器）
const UserSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1).max(100),
  email: z.string().email(),
  age: z.number().int().min(0).max(150).optional(),
  role: z.enum(['admin', 'user', 'viewer']),
  createdAt: z.string().datetime(),
});

// 從 Schema 推導 TypeScript 型別
type User = z.infer<typeof UserSchema>;

// 執行時期驗證
function parseUser(data: unknown): User {
  return UserSchema.parse(data);  // 驗證失敗拋出 ZodError
}

// 安全驗證（不拋例外）
function safeParseUser(data: unknown) {
  const result = UserSchema.safeParse(data);
  if (result.success) {
    return result.data;   // User 型別
  } else {
    console.error(result.error.issues);
    return null;
  }
}
```

#### DTO 設計模式

```typescript
// NestJS + class-validator + class-transformer
import { IsString, IsEmail, IsOptional, IsInt, Min, Max } from 'class-validator';

export class CreateUserDto {
  @IsString()
  name: string;

  @IsEmail()
  email: string;

  @IsOptional()
  @IsInt()
  @Min(0)
  @Max(150)
  age?: number;
}

// Response DTO — 控制回傳欄位
export class UserResponseDto {
  id: string;
  name: string;
  email: string;

  static fromEntity(entity: UserEntity): UserResponseDto {
    return {
      id: entity.id,
      name: entity.name,
      email: entity.email,
    };
  }
}
```

#### 常見反模式

```typescript
// ❌ 反模式：濫用 any
function processData(data: any): any { return data.value; }

// ✅ 正確：使用 unknown + 型別守衛
function processData(data: unknown): number {
  if (typeof data === 'object' && data !== null && 'value' in data) {
    return (data as { value: number }).value;
  }
  throw new Error('Invalid data');
}

// ❌ 反模式：忽略 null 檢查
function getName(user: User | null): string { return user.name; }

// ✅ 正確：使用 Optional Chaining
function getName(user: User | null): string { return user?.name ?? 'Anonymous'; }

// ❌ 反模式：Type Assertion 不驗證
const user = JSON.parse(data) as User;  // 危險！

// ✅ 正確：使用 Zod 驗證
const user = UserSchema.parse(JSON.parse(data));
```

#### 章節小練習

1. 設定一份包含嚴格模式的 `tsconfig.json`。
2. 使用 Zod 定義一個 Order Schema 並實作驗證。
3. 解釋 Branded Types 如何防止 ID 混用。

#### 實務注意事項

> - 所有專案必須開啟 `strict: true`
> - 開發環境使用 tsx，建置使用 SWC 或 esbuild
> - API 邊界使用 Zod 進行執行時期驗證
> - 禁止使用 `any`，使用 `unknown` + 型別守衛
> - 在 CI/CD 中執行 `tsc --noEmit` 確保型別正確性

---

## 第 5 章：Node.js 核心 API

### 5.1 fs（檔案系統）

#### 概述

`node:fs` 模組提供檔案系統操作的 API，支援同步、回呼和 Promise 三種風格。**企業專案一律使用 `fs/promises`**。

#### 常用操作

```typescript
import { readFile, writeFile, readdir, stat, mkdir, rm, cp, rename } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join } from 'node:path';

// 讀取檔案
const content = await readFile('config.json', 'utf-8');
const config = JSON.parse(content);

// 寫入檔案
await writeFile('output.json', JSON.stringify(data, null, 2), 'utf-8');

// 遞迴讀取目錄
const files = await readdir('./src', { recursive: true, withFileTypes: true });
for (const file of files) {
  if (file.isFile() && file.name.endsWith('.ts')) {
    console.log(`${file.parentPath}/${file.name}`);
  }
}

// 檢查檔案是否存在（少數可接受的同步 API）
if (existsSync('./config.json')) {
  // ...
}

// 建立目錄（遞迴）
await mkdir('./logs/archive', { recursive: true });

// 複製檔案 / 目錄
await cp('./src', './backup/src', { recursive: true });

// 刪除（遞迴）
await rm('./temp', { recursive: true, force: true });

// 檔案資訊
const info = await stat('./package.json');
console.log(`大小: ${info.size} bytes, 修改時間: ${info.mtime}`);
```

#### 串流式大檔案處理

```typescript
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';
import { createGzip } from 'node:zlib';

// 大檔案壓縮（串流，不佔記憶體）
await pipeline(
  createReadStream('large-file.log'),
  createGzip(),
  createWriteStream('large-file.log.gz')
);
```

#### 監聽檔案變化

```typescript
import { watch } from 'node:fs/promises';

// 監聽目錄變化（Node.js v22+ 穩定）
const watcher = watch('./config', { recursive: true });
for await (const event of watcher) {
  console.log(`[${event.eventType}] ${event.filename}`);
}
```

> **⚠️ 注意**：
> - 永遠不要在請求處理中使用 `readFileSync` 等同步方法
> - 大檔案使用 Stream，避免一次性載入到記憶體
> - `recursive` 選項在不同 OS 上行為可能有差異

---

### 5.2 path（路徑處理）

#### 常用方法

```typescript
import { join, resolve, basename, dirname, extname, relative, parse, format } from 'node:path';

// 路徑拼接（自動處理分隔符）
const filePath = join('/app', 'src', 'main.ts');       // /app/src/main.ts

// 解析為絕對路徑
const absPath = resolve('src', 'main.ts');             // /home/user/project/src/main.ts

// 路徑組成
basename('/app/src/main.ts');          // 'main.ts'
basename('/app/src/main.ts', '.ts');   // 'main'
dirname('/app/src/main.ts');           // '/app/src'
extname('/app/src/main.ts');           // '.ts'

// 相對路徑
relative('/app/src', '/app/dist/main.js');  // '../dist/main.js'

// 解析路徑
const parsed = parse('/app/src/main.ts');
// { root: '/', dir: '/app/src', base: 'main.ts', ext: '.ts', name: 'main' }

// ESM 中取得 __dirname
import { fileURLToPath } from 'node:url';
const __dirname = import.meta.dirname;                 // Node.js v21+
```

> **✅ 實務建議**：永遠使用 `path.join()` 或 `path.resolve()` 拼接路徑，不要手動拼接字串（跨平台相容）。

---

### 5.3 os（作業系統資訊）

```typescript
import { hostname, platform, arch, cpus, totalmem, freemem, tmpdir, homedir, userInfo, type as osType, release, networkInterfaces } from 'node:os';

// 系統資訊
console.log(`主機名稱: ${hostname()}`);
console.log(`平台: ${platform()}`);         // 'linux', 'darwin', 'win32'
console.log(`架構: ${arch()}`);             // 'x64', 'arm64'
console.log(`系統類型: ${osType()}`);       // 'Linux', 'Darwin', 'Windows_NT'
console.log(`核心版本: ${release()}`);

// CPU 資訊
const cpuInfo = cpus();
console.log(`CPU 核心數: ${cpuInfo.length}`);
console.log(`CPU 型號: ${cpuInfo[0].model}`);

// 記憶體資訊
const totalGB = (totalmem() / 1024 / 1024 / 1024).toFixed(2);
const freeGB = (freemem() / 1024 / 1024 / 1024).toFixed(2);
console.log(`記憶體: ${freeGB}GB / ${totalGB}GB`);

// 網路介面
const nets = networkInterfaces();
for (const [name, addrs] of Object.entries(nets)) {
  for (const addr of addrs ?? []) {
    if (addr.family === 'IPv4' && !addr.internal) {
      console.log(`${name}: ${addr.address}`);
    }
  }
}
```

#### 使用情境

- 取得 CPU 核心數來決定 Worker Threads 或 Cluster 數量
- 健康檢查端點回報系統資源使用率
- 日誌中記錄主機資訊

---

### 5.4 process（程序管理）

```typescript
// 環境變數
const port = process.env.PORT ?? '3000';
const nodeEnv = process.env.NODE_ENV ?? 'development';

// 程序資訊
console.log(`PID: ${process.pid}`);
console.log(`Node.js: ${process.version}`);
console.log(`Uptime: ${process.uptime()}s`);
console.log(`記憶體使用: ${JSON.stringify(process.memoryUsage())}`);

// 命令列參數
const args = process.argv.slice(2);   // 去除 node 和 script 路徑

// 優雅退出
process.on('SIGTERM', async () => {
  console.log('收到 SIGTERM，開始優雅關機...');
  await server.close();
  await database.disconnect();
  process.exit(0);
});

process.on('SIGINT', async () => {
  console.log('收到 SIGINT（Ctrl+C），開始優雅關機...');
  await server.close();
  process.exit(0);
});

// 未捕獲的例外處理
process.on('uncaughtException', (error) => {
  console.error('未捕獲的例外:', error);
  process.exit(1);  // 必須退出，狀態可能已損壞
});

process.on('unhandledRejection', (reason) => {
  console.error('未處理的 Promise 拒絕:', reason);
  // Node.js v26 預設會退出
});
```

> **⚠️ 重要**：`uncaughtException` 後必須退出程序，因為應用狀態可能已損壞。

---

### 5.5 buffer（二進位資料處理）

```typescript
import { Buffer } from 'node:buffer';

// 建立 Buffer
const buf1 = Buffer.from('Hello World', 'utf-8');
const buf2 = Buffer.alloc(1024);              // 初始化為 0
const buf3 = Buffer.allocUnsafe(1024);        // 未初始化（效能更好但不安全）

// 編碼轉換
const base64 = buf1.toString('base64');       // 'SGVsbG8gV29ybGQ='
const hex = buf1.toString('hex');             // '48656c6c6f20576f726c64'
const text = Buffer.from(base64, 'base64').toString('utf-8');  // 'Hello World'

// 比較
const isEqual = buf1.equals(Buffer.from('Hello World'));  // true

// 串接
const combined = Buffer.concat([buf1, Buffer.from(' !!!', 'utf-8')]);
```

#### 使用情境

- 處理檔案上傳的二進位資料
- 加密/解密操作
- Base64 編碼/解碼
- 處理網路協定的二進位封包

---

### 5.6 stream（串流處理）

#### 四種串流類型

```mermaid
graph LR
    A[Readable Stream] -->|pipe| B[Transform Stream]
    B -->|pipe| C[Writable Stream]
    D[Duplex Stream] -->|雙向| D
```

| 串流類型 | 說明 | 範例 |
|----------|------|------|
| **Readable** | 可讀取 | 檔案讀取、HTTP 請求 |
| **Writable** | 可寫入 | 檔案寫入、HTTP 回應 |
| **Duplex** | 可讀可寫 | TCP Socket |
| **Transform** | 轉換串流 | 壓縮、加密 |

#### 實務範例

```typescript
import { createReadStream, createWriteStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';
import { Transform } from 'node:stream';

// 自定義 Transform Stream — CSV 轉 JSON
const csvToJson = new Transform({
  objectMode: true,
  transform(chunk, encoding, callback) {
    const line = chunk.toString().trim();
    const [name, age, email] = line.split(',');
    this.push(JSON.stringify({ name, age: parseInt(age), email }) + '\n');
    callback();
  }
});

// 串流管道
await pipeline(
  createReadStream('data.csv'),
  csvToJson,
  createWriteStream('data.jsonl')
);

// Web Streams API（Node.js v18+ 穩定）
const response = await fetch('https://api.example.com/large-data');
const reader = response.body?.getReader();
if (reader) {
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    process.stdout.write(value);
  }
}
```

#### 背壓（Backpressure）處理

```typescript
import { Readable, Writable } from 'node:stream';

// 正確處理背壓
const readable = createReadStream('large-file.dat');
const writable = createWriteStream('output.dat');

readable.pipe(writable);

writable.on('drain', () => {
  // 寫入緩衝區已清空，可以繼續
  readable.resume();
});

// 更推薦使用 pipeline（自動處理背壓和錯誤）
await pipeline(readable, writable);
```

> **✅ 實務建議**：處理大檔案時務必使用 Stream，避免 `readFile` 將整個檔案載入記憶體。

---

### 5.7 crypto（加密與雜湊）

```typescript
import { createHash, createHmac, randomBytes, randomUUID, createCipheriv, createDecipheriv, scrypt } from 'node:crypto';
import { promisify } from 'node:util';

const scryptAsync = promisify(scrypt);

// ===== 雜湊 =====
const hash = createHash('sha256').update('password123').digest('hex');

// ===== HMAC =====
const hmac = createHmac('sha256', 'secret-key').update('message').digest('hex');

// ===== 隨機值 =====
const random = randomBytes(32).toString('hex');   // 64 字元隨機字串
const uuid = randomUUID();                         // v4 UUID

// ===== 密碼雜湊（推薦 scrypt）=====
async function hashPassword(password: string): Promise<string> {
  const salt = randomBytes(16).toString('hex');
  const derivedKey = (await scryptAsync(password, salt, 64)) as Buffer;
  return `${salt}:${derivedKey.toString('hex')}`;
}

async function verifyPassword(password: string, stored: string): Promise<boolean> {
  const [salt, hash] = stored.split(':');
  const derivedKey = (await scryptAsync(password, salt, 64)) as Buffer;
  return derivedKey.toString('hex') === hash;
}

// ===== AES-256-GCM 加密/解密 =====
function encrypt(text: string, key: Buffer): { encrypted: string; iv: string; tag: string } {
  const iv = randomBytes(16);
  const cipher = createCipheriv('aes-256-gcm', key, iv);
  let encrypted = cipher.update(text, 'utf-8', 'hex');
  encrypted += cipher.final('hex');
  const tag = cipher.getAuthTag().toString('hex');
  return { encrypted, iv: iv.toString('hex'), tag };
}

function decrypt(data: { encrypted: string; iv: string; tag: string }, key: Buffer): string {
  const decipher = createDecipheriv('aes-256-gcm', key, Buffer.from(data.iv, 'hex'));
  decipher.setAuthTag(Buffer.from(data.tag, 'hex'));
  let decrypted = decipher.update(data.encrypted, 'hex', 'utf-8');
  decrypted += decipher.final('utf-8');
  return decrypted;
}
```

> **⚠️ 安全注意**：
> - 密碼儲存使用 `scrypt` 或 `argon2`（第三方），絕不使用 MD5/SHA
> - 加密使用 AES-256-GCM（含認證），不使用 ECB 模式
> - 金鑰管理使用環境變數或 Vault，不可寫死在程式碼

---

### 5.8 http / https（HTTP 伺服器與客戶端）

#### 原生 HTTP 伺服器

```typescript
import { createServer } from 'node:http';

const server = createServer((req, res) => {
  // 路由分發
  if (req.method === 'GET' && req.url === '/api/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', uptime: process.uptime() }));
    return;
  }

  if (req.method === 'POST' && req.url === '/api/data') {
    let body = '';
    req.on('data', (chunk) => { body += chunk; });
    req.on('end', () => {
      const data = JSON.parse(body);
      res.writeHead(201, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ received: data }));
    });
    return;
  }

  res.writeHead(404);
  res.end('Not Found');
});

server.listen(3000, () => {
  console.log('Server listening on http://localhost:3000');
});
```

#### HTTP 客戶端（fetch — Node.js 內建）

```typescript
// Node.js v21+ 全域可用 fetch（基於 undici）
const response = await fetch('https://api.example.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John' }),
  signal: AbortSignal.timeout(5000),  // 5 秒超時
});

if (!response.ok) {
  throw new Error(`HTTP ${response.status}: ${response.statusText}`);
}

const data = await response.json();
```

> **✅ 實務建議**：生產環境使用 Express/Fastify/NestJS 框架，原生 http 適合了解底層原理。

---

### 5.9 events（事件發射器）

```typescript
import { EventEmitter } from 'node:events';

// 自定義事件系統
class OrderService extends EventEmitter {
  async createOrder(data: CreateOrderDto) {
    const order = await this.orderRepo.save(data);
    
    // 發射事件（解耦後續處理）
    this.emit('order:created', order);
    this.emit('order:notification', { orderId: order.id, type: 'created' });
    
    return order;
  }
}

const orderService = new OrderService();

// 註冊事件監聽器
orderService.on('order:created', async (order) => {
  await inventoryService.reserveStock(order.items);
});

orderService.on('order:notification', async (data) => {
  await notificationService.send(data);
});

// 一次性監聽
orderService.once('order:created', (order) => {
  console.log('第一筆訂單！', order.id);
});

// 錯誤處理（必須監聽 error 事件）
orderService.on('error', (err) => {
  console.error('OrderService 錯誤:', err);
});

// TypeScript 型別安全的事件
interface OrderEvents {
  'order:created': [order: Order];
  'order:notification': [data: { orderId: string; type: string }];
  'error': [error: Error];
}

class TypedOrderService extends EventEmitter<OrderEvents> {
  // emit 和 on 都有型別檢查
}
```

---

### 5.10 timers（計時器）

```typescript
import { setTimeout, setInterval, setImmediate } from 'node:timers/promises';

// Promise 版本的 setTimeout
await setTimeout(1000);   // 等待 1 秒
console.log('1 秒後執行');

// 可取消的計時器
const ac = new AbortController();
try {
  await setTimeout(5000, undefined, { signal: ac.signal });
} catch (err) {
  if (err.code === 'ABORT_ERR') {
    console.log('計時器已取消');
  }
}

// 在其他地方取消
ac.abort();

// setInterval 產生 AsyncIterator
const interval = setInterval(1000);
let count = 0;
for await (const _ of interval) {
  console.log(`第 ${++count} 次`);
  if (count >= 5) break;   // 自動清除
}

// setImmediate（在 check 階段執行）
await setImmediate();
console.log('下一個 Event Loop 迭代');
```

---

### 5.11 worker_threads（工作執行緒）

#### 概述

Worker Threads 允許在獨立的執行緒中執行 CPU 密集型任務，不阻塞主執行緒的 Event Loop。

```mermaid
graph TD
    A[Main Thread] --> B[Event Loop]
    A --> C[Worker Thread 1]
    A --> D[Worker Thread 2]
    A --> E[Worker Thread N]
    
    C --> F[CPU 密集任務]
    D --> G[CPU 密集任務]
    E --> H[CPU 密集任務]
    
    F -->|結果| A
    G -->|結果| A
    H -->|結果| A
```

#### 基本用法

```typescript
// main.ts — 主執行緒
import { Worker, isMainThread } from 'node:worker_threads';
import { cpus } from 'node:os';

function runWorker(data: unknown): Promise<unknown> {
  return new Promise((resolve, reject) => {
    const worker = new Worker(new URL('./worker.ts', import.meta.url));
    worker.postMessage(data);
    worker.on('message', resolve);
    worker.on('error', reject);
    worker.on('exit', (code) => {
      if (code !== 0) reject(new Error(`Worker exited with code ${code}`));
    });
  });
}

// 平行處理大量資料
const items = Array.from({ length: 1000 }, (_, i) => i);
const chunkSize = Math.ceil(items.length / cpus().length);
const chunks = [];
for (let i = 0; i < items.length; i += chunkSize) {
  chunks.push(items.slice(i, i + chunkSize));
}

const results = await Promise.all(chunks.map(chunk => runWorker(chunk)));
console.log('所有 Worker 完成:', results);
```

```typescript
// worker.ts — 工作執行緒
import { parentPort } from 'node:worker_threads';

parentPort?.on('message', (data: number[]) => {
  // CPU 密集型運算
  const result = data.map(n => {
    let sum = 0;
    for (let i = 0; i < 1_000_000; i++) {
      sum += Math.sqrt(n * i);
    }
    return sum;
  });
  
  parentPort?.postMessage(result);
});
```

#### Worker Thread Pool

```typescript
// 使用 Piscina（Worker Pool 套件）
import Piscina from 'piscina';

const pool = new Piscina({
  filename: new URL('./worker.ts', import.meta.url).href,
  maxThreads: 4,
  minThreads: 2,
});

const result = await pool.run({ data: 'compute this' });
```

> **✅ 使用時機**：影像處理、密碼雜湊、大量 JSON 解析、科學運算。不適合 I/O 任務。

---

### 5.12 cluster（叢集）

```typescript
import cluster from 'node:cluster';
import { cpus } from 'node:os';
import { createServer } from 'node:http';

if (cluster.isPrimary) {
  const numCPUs = cpus().length;
  console.log(`Primary ${process.pid} 啟動，建立 ${numCPUs} 個 Worker`);

  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} 已終止 (${signal || code})`);
    // 自動重啟
    cluster.fork();
  });
} else {
  createServer((req, res) => {
    res.writeHead(200);
    res.end(`Hello from Worker ${process.pid}\n`);
  }).listen(3000);

  console.log(`Worker ${process.pid} 已啟動`);
}
```

> **✅ 實務建議**：生產環境建議使用 PM2 管理 Cluster，而非手動實作。

---

### 5.13 child_process（子程序）

```typescript
import { exec, execFile, spawn } from 'node:child_process';
import { promisify } from 'node:util';

const execAsync = promisify(exec);

// exec — 執行 shell 指令（有 buffer 限制）
const { stdout, stderr } = await execAsync('git log --oneline -5');
console.log(stdout);

// spawn — 串流式執行（推薦用於大量輸出）
const child = spawn('npm', ['run', 'build'], {
  stdio: 'inherit',        // 繼承父程序的 I/O
  cwd: '/app',             // 工作目錄
  env: { ...process.env, NODE_ENV: 'production' },
});

child.on('exit', (code) => {
  console.log(`子程序結束，代碼: ${code}`);
});

// execFile — 直接執行檔案（不經過 shell，更安全）
const execFileAsync = promisify(execFile);
const { stdout: version } = await execFileAsync('node', ['--version']);
```

> **⚠️ 安全注意**：`exec` 會經過 shell，有指令注入風險。使用者輸入的參數應使用 `execFile` 或 `spawn`。

---

### 5.14 diagnostics_channel（診斷通道）

```typescript
import { channel, subscribe } from 'node:diagnostics_channel';

// 建立診斷通道
const httpChannel = channel('http.server.request');

// 發佈診斷資訊
httpChannel.publish({
  method: 'GET',
  url: '/api/users',
  duration: 45,
  statusCode: 200,
});

// 訂閱診斷資訊（用於 APM / Monitoring）
subscribe('http.server.request', (message) => {
  const { method, url, duration, statusCode } = message as any;
  console.log(`[HTTP] ${method} ${url} → ${statusCode} (${duration}ms)`);
});
```

#### 使用情境

- 應用效能監控（APM）
- 分散式追蹤（Distributed Tracing）
- 自定義指標收集

---

### 5.15 新興 API：SQLite、FFI、Permissions

#### node:sqlite（Stability 1.2 — Release Candidate）

> **穩定性狀態**：`node:sqlite` 在 Node.js v26.1.0 中為 **Stability 1.2（Release Candidate）**，
> API 已接近穩定但仍可能有小幅調整。自 v22.5.0 引入，已歷經多次迭代強化。

##### 基本用法

```typescript
import { DatabaseSync } from 'node:sqlite';

// 開啟資料庫（記憶體或檔案）
const db = new DatabaseSync(':memory:');

// 建立表格
db.exec(`
  CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
  )
`);

// 預備語句（防止 SQL Injection）
const insert = db.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
insert.run('Alice', 'alice@example.com');
insert.run('Bob', 'bob@example.com');

// 查詢單筆
const select = db.prepare('SELECT * FROM users WHERE name = ?');
const user = select.get('Alice');
console.log(user);  // { id: 1, name: 'Alice', email: 'alice@example.com', ... }

// 查詢全部
const all = db.prepare('SELECT * FROM users');
const users = all.all();

// 使用迭代器（v23.4.0+，適合大量資料）
for (const row of db.prepare('SELECT * FROM users').iterate()) {
  console.log(row.name);
}
```

##### 建構選項

```typescript
const db = new DatabaseSync('app.db', {
  readOnly: false,                       // 唯讀模式
  enableForeignKeyConstraints: true,     // 啟用外鍵約束（預設 true）
  enableDoubleQuotedStringLiterals: false, // 雙引號字串字面值（預設 false）
  allowExtension: false,                 // 允許載入擴充功能
  timeout: 5000,                         // 忙碌等待逾時（毫秒）
  readBigInts: false,                    // INTEGER 欄位以 BigInt 讀取
  returnArrays: false,                   // 查詢結果以陣列而非物件回傳
  defensive: true,                       // 啟用防禦模式，防止 SQL 腐蝕資料庫
  limits: {                              // 資源限制（v25.8.0+）
    sqlLength: 100000,                   // SQL 語句最大長度
    column: 200,                         // 最大欄位數
    variableNumber: 999,                 // 最大 SQL 變數數
  },
});
```

##### TagStore — 標記模板快取（v24.9.0+）

`createTagStore()` 建立 LRU 快取，使用 Tagged Template Literal 自動快取預備語句並安全綁定參數，兼顧效能與防止 SQL Injection：

```typescript
const db = new DatabaseSync(':memory:');
const sql = db.createTagStore();  // 預設快取 1000 條語句

db.exec('CREATE TABLE users (id INT, name TEXT)');

// 使用標記模板 — 自動參數綁定（安全）
sql.run`INSERT INTO users VALUES (1, 'Alice')`;
sql.run`INSERT INTO users VALUES (2, 'Bob')`;

// 查詢單筆
const name = 'Alice';
const user = sql.get`SELECT * FROM users WHERE name = ${name}`;
// 等同於 db.prepare('SELECT ?').get(name)，但會快取預備語句

// 查詢全部
const allUsers = sql.all`SELECT * FROM users ORDER BY id`;

// 使用迭代器
for (const row of sql.iterate`SELECT * FROM users`) {
  console.log(row);
}

// ⚠️ 注意：標記模板中的 ${value} 是參數綁定，不是字串插值
// ✅ 安全：sql.run`INSERT INTO t1 (id) VALUES (${id})`
// ❌ 危險：db.exec(`INSERT INTO t1 (id) VALUES (${id})`)  // SQL Injection 風險

// 快取管理
console.log(sql.size);      // 目前快取的語句數
console.log(sql.capacity);  // 最大快取容量
sql.clear();                 // 清除快取
```

##### 聚合函式（v24.0.0+）

```typescript
db.exec(`
  CREATE TABLE scores (student TEXT, score INTEGER);
  INSERT INTO scores VALUES ('Alice', 90), ('Bob', 85), ('Alice', 95);
`);

// 自定義聚合函式
db.aggregate('avg_score', {
  start: () => ({ sum: 0, count: 0 }),
  step: (state, value) => ({ sum: state.sum + value, count: state.count + 1 }),
  result: (state) => state.sum / state.count,
});

db.prepare('SELECT avg_score(score) as avg FROM scores').get();
// { avg: 90 }

// 支援視窗函式（提供 inverse 回呼）
db.aggregate('running_sum', {
  start: 0,
  step: (acc, value) => acc + value,
  inverse: (acc, value) => acc - value,  // 視窗滑動時移除值
  result: (acc) => acc,
});
```

##### 序列化與反序列化（v26.1.0+）

```typescript
// 將記憶體資料庫序列化為二進位
const original = new DatabaseSync(':memory:');
original.exec('CREATE TABLE t(key INTEGER PRIMARY KEY, value TEXT)');
original.exec("INSERT INTO t VALUES (1, 'hello')");

const buffer = original.serialize();  // 回傳 Uint8Array
original.close();

// 從二進位還原資料庫
const clone = new DatabaseSync(':memory:');
clone.deserialize(buffer);
console.log(clone.prepare('SELECT value FROM t').get());
// { value: 'hello' }
```

> **使用情境**：資料庫快照、傳輸、備份、測試環境初始化。

##### 非同步備份（v23.8.0+）

```typescript
import { backup, DatabaseSync } from 'node:sqlite';

const sourceDb = new DatabaseSync('production.db');

// 非同步備份（回傳 Promise）
const totalPages = await backup(sourceDb, 'backup.db', {
  rate: 100,  // 每批次傳輸 100 頁
  progress: ({ totalPages, remainingPages }) => {
    const percent = ((totalPages - remainingPages) / totalPages * 100).toFixed(1);
    console.log(`備份進度：${percent}%`);
  },
});
console.log(`備份完成，共傳輸 ${totalPages} 頁`);
```

##### 授權控制（v24.10.0+）

```typescript
import { DatabaseSync, constants } from 'node:sqlite';

const db = new DatabaseSync(':memory:');

// 設定授權回呼 — 控制 SQL 操作權限
db.setAuthorizer((actionCode, arg1, arg2, dbName, triggerOrView) => {
  // 禁止建立表格
  if (actionCode === constants.SQLITE_CREATE_TABLE) {
    return constants.SQLITE_DENY;
  }
  // 禁止刪除操作
  if (actionCode === constants.SQLITE_DELETE) {
    return constants.SQLITE_DENY;
  }
  return constants.SQLITE_OK;
});

// SELECT 正常運作
db.prepare('SELECT 1').get();

// CREATE TABLE 將拋出錯誤
try {
  db.exec('CREATE TABLE blocked (id INTEGER)');
} catch (err) {
  console.log('操作被阻止:', err.message);
}

// 清除授權器
db.setAuthorizer(null);
```

##### 執行期限制（v25.8.0+）

```typescript
const db = new DatabaseSync(':memory:');

// 讀取目前限制
console.log(db.limits.length);       // 最大字串/BLOB 長度
console.log(db.limits.sqlLength);    // 最大 SQL 語句長度

// 設定限制
db.limits.sqlLength = 100000;

// 重設為編譯時最大值
db.limits.sqlLength = Infinity;
```

##### Session 與 Changeset（v23.3.0+）

```typescript
const sourceDb = new DatabaseSync(':memory:');
const targetDb = new DatabaseSync(':memory:');

sourceDb.exec('CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT)');
targetDb.exec('CREATE TABLE data(key INTEGER PRIMARY KEY, value TEXT)');

// 建立 Session 追蹤變更
const session = sourceDb.createSession();

sourceDb.prepare('INSERT INTO data (key, value) VALUES (?, ?)').run(1, 'hello');
sourceDb.prepare('INSERT INTO data (key, value) VALUES (?, ?)').run(2, 'world');

// 取得變更集
const changeset = session.changeset();
session.close();

// 將變更套用到目標資料庫
targetDb.applyChangeset(changeset);
```

##### Symbol.dispose 支援（v23.11.0+）

```typescript
// 使用 using 語法自動關閉資料庫（需 TypeScript 5.2+）
{
  using db = new DatabaseSync(':memory:');
  db.exec('CREATE TABLE t(id INT)');
  // 離開作用域時自動呼叫 db[Symbol.dispose]() 關閉連線
}
```

> **使用情境**：設定儲存、本地快取、嵌入式應用、CLI 工具的資料持久化、
> 測試 fixture 管理、輕量級內容管理系統。

#### node:ffi（實驗性）

```typescript
// Foreign Function Interface — 呼叫原生 C 函式庫
// 需要 --experimental-ffi 旗標，且僅在支援 FFI 的建置版本中可用
// Permission Model 中需搭配 --allow-ffi 旗標
// 注意：v26 仍為實驗性，API 可能變更
```

#### Permission Model（Stability 2 — Stable）

**Node.js Permission Model 在 v26 中已標記為 Stability 2（Stable）**，提供「安全帶」機制限制 Node.js 程序對系統資源的存取。

##### 基本用法

```bash
# 以受限權限執行 Node.js（啟用 --permission 後預設限制所有資源）
node --permission app.js

# 常用權限旗標
node --permission \
  --allow-fs-read=/app/config \
  --allow-fs-write=/app/logs \
  --allow-child-process \
  --allow-worker \
  --allow-net \
  app.js

# 完整權限旗標列表
# --allow-fs-read=<path>     允許讀取指定路徑（支援萬用字元 *）
# --allow-fs-write=<path>    允許寫入指定路徑
# --allow-child-process      允許建立子程序
# --allow-worker             允許建立 Worker Threads
# --allow-net                允許網路存取
# --allow-addons             允許原生模組
# --allow-wasi               允許 WASI
# --allow-ffi                允許 FFI（Foreign Function Interface）
```

##### 設定檔支援

```json
// node.config.json — 以設定檔管理權限
{
  "permission": {
    "allow-fs-read": ["./src", "./config"],
    "allow-fs-write": ["./logs", "./tmp"],
    "allow-child-process": false,
    "allow-worker": true,
    "allow-net": true,
    "allow-addons": false,
    "allow-ffi": false
  }
}
```

```bash
# 使用設定檔啟動（自動啟用 --permission）
node --experimental-default-config-file app.js
```

##### 程式碼中檢查權限

```typescript
// 執行期權限檢查 API
import { permission } from 'node:process';

if (permission.has('fs.read', '/etc/passwd')) {
  console.log('有讀取權限');
} else {
  console.log('沒有讀取權限');
}

if (permission.has('fs.write', '/app/logs')) {
  // 安全地寫入日誌
}
```

##### 與 npx 整合

```bash
# 在 npx 中使用 Permission Model
npx --node-options="--permission" package-name

# 搭配全域套件路徑
npx --node-options="--permission --allow-fs-read=$(npm prefix -g)" package-name

# 搭配 npx 快取
npx --node-options="--permission --allow-fs-read=$(npm config get cache)" package-name
```

##### 限制與注意事項

- Permission Model **不會繼承到 Worker Thread**
- 啟用後，以下功能預設受限：原生模組、網路、子程序、Worker、Inspector、檔案系統、WASI、FFI
- Symbolic links 會被追蹤，即使目標在允許路徑之外
- `node:sqlite` 的檔案存取**不受** Permission Model 限制
- 已開啟的 file descriptor 透過 `node:fs` 可繞過 Permission Model

> **使用情境**：多租戶環境中限制不受信任的程式碼存取範圍、最小權限原則實踐、
> 沙箱化執行環境。

#### 章節小練習

1. 使用 `fs/promises` 實作遞迴讀取目錄並列出所有 `.ts` 檔案。
2. 使用 `crypto` 實作密碼雜湊與驗證。
3. 使用 Worker Threads 實作平行的質數計算。

#### 實務注意事項

> - 檔案操作一律使用 `fs/promises`，禁止同步方法
> - 大檔案使用 Stream 處理
> - CPU 密集任務使用 Worker Threads 或 Piscina
> - 路徑拼接使用 `path.join()`，不手動拼字串
> - 加密使用 AES-256-GCM，密碼雜湊使用 scrypt/argon2

---

## 第 6 章：非同步程式設計

### 6.1 Callback 模式

#### 傳統 Callback 風格

```typescript
import { readFile } from 'node:fs';

// Node.js 經典 Error-first Callback
readFile('config.json', 'utf-8', (err, data) => {
  if (err) {
    console.error('讀取失敗:', err);
    return;
  }
  console.log('內容:', data);
});
```

#### Callback Hell（回呼地獄）

```typescript
// ❌ 反模式：巢狀回呼
readFile('step1.txt', 'utf-8', (err, data1) => {
  if (err) return handleError(err);
  processData(data1, (err, result1) => {
    if (err) return handleError(err);
    readFile('step2.txt', 'utf-8', (err, data2) => {
      if (err) return handleError(err);
      processData(data2, (err, result2) => {
        if (err) return handleError(err);
        // 深層巢狀，難以維護
        console.log(result1, result2);
      });
    });
  });
});
```

> **⚠️ 2026 年已不建議使用 Callback 風格**，所有核心 API 都有 Promise 版本。了解 Callback 僅為理解歷史程式碼。

---

### 6.2 Promise 與 Promise 組合器

#### Promise 基礎

```typescript
// 建立 Promise
function fetchUser(id: string): Promise<User> {
  return new Promise((resolve, reject) => {
    database.query(`SELECT * FROM users WHERE id = $1`, [id], (err, result) => {
      if (err) reject(err);
      else resolve(result.rows[0]);
    });
  });
}

// 鏈式呼叫
fetchUser('123')
  .then(user => fetchOrders(user.id))
  .then(orders => processOrders(orders))
  .catch(err => console.error(err))
  .finally(() => console.log('完成'));
```

#### Promise 組合器

```typescript
// Promise.all — 全部成功才成功
const [users, orders, products] = await Promise.all([
  fetchUsers(),
  fetchOrders(),
  fetchProducts(),
]);

// Promise.allSettled — 等待全部完成（不管成敗）
const results = await Promise.allSettled([
  sendEmail(user1),
  sendEmail(user2),
  sendEmail(user3),
]);
results.forEach((result, i) => {
  if (result.status === 'fulfilled') {
    console.log(`Email ${i} 成功`);
  } else {
    console.error(`Email ${i} 失敗:`, result.reason);
  }
});

// Promise.race — 最先完成的結果
const fastest = await Promise.race([
  fetchFromCacheServer1(),
  fetchFromCacheServer2(),
]);

// Promise.any — 最先成功的結果（忽略失敗）
const result = await Promise.any([
  fetchFromPrimary(),
  fetchFromSecondary(),
  fetchFromTertiary(),
]);
```

#### 選擇指南

| 組合器 | 行為 | 使用場景 |
|--------|------|----------|
| `Promise.all` | 全部成功才回傳 | 平行取得多個獨立資料 |
| `Promise.allSettled` | 等待全部完成 | 批次操作，需知道每個結果 |
| `Promise.race` | 最先完成（含失敗） | 超時控制、快取競爭 |
| `Promise.any` | 最先成功 | 多來源容錯查詢 |

---

### 6.3 async / await 最佳實務

#### 基本用法

```typescript
// ✅ 正確的 async/await 用法
async function getOrderDetails(orderId: string): Promise<OrderDetails> {
  const order = await orderRepo.findById(orderId);
  if (!order) {
    throw new NotFoundException(`Order ${orderId} not found`);
  }

  const [customer, items, payment] = await Promise.all([
    customerService.findById(order.customerId),
    orderItemRepo.findByOrderId(orderId),
    paymentService.findByOrderId(orderId),
  ]);

  return { order, customer, items, payment };
}
```

#### 常見錯誤

```typescript
// ❌ 錯誤：序列化執行（效能差）
async function fetchAll() {
  const users = await fetchUsers();      // 等待完成
  const orders = await fetchOrders();    // 才開始（不需要 users 的結果）
  const products = await fetchProducts(); // 才開始
  return { users, orders, products };
}

// ✅ 正確：平行執行
async function fetchAll() {
  const [users, orders, products] = await Promise.all([
    fetchUsers(),
    fetchOrders(),
    fetchProducts(),
  ]);
  return { users, orders, products };
}

// ❌ 錯誤：忘記 await
async function saveUser(user: User) {
  userRepo.save(user);  // 沒有 await！Promise 被丟棄
  console.log('已儲存');  // 可能還沒儲存完
}

// ✅ 正確
async function saveUser(user: User) {
  await userRepo.save(user);
  console.log('已儲存');
}

// ❌ 錯誤：在迴圈中 await
for (const id of userIds) {
  const user = await fetchUser(id);  // 序列化！
  results.push(user);
}

// ✅ 正確：批次平行
const results = await Promise.all(userIds.map(id => fetchUser(id)));
```

#### 錯誤處理

```typescript
// ✅ try/catch 包覆
async function processOrder(orderId: string) {
  try {
    const order = await orderService.findById(orderId);
    await paymentService.charge(order);
    await inventoryService.deduct(order.items);
    await notificationService.send(order.customerId, 'order_confirmed');
  } catch (error) {
    if (error instanceof PaymentError) {
      await orderService.cancel(orderId, 'payment_failed');
    } else if (error instanceof InventoryError) {
      await paymentService.refund(orderId);
      await orderService.cancel(orderId, 'out_of_stock');
    } else {
      throw error;  // 未知錯誤向上拋出
    }
  }
}
```

---

### 6.4 Event Loop 深入解析

#### 完整的 Event Loop 架構

```mermaid
flowchart TD
    A[程式開始執行] --> B[執行同步程式碼]
    B --> C{Call Stack 是否為空?}
    C -->|否| B
    C -->|是| D[清空 process.nextTick Queue]
    D --> E[清空 Promise Microtask Queue]
    E --> F[timers 階段]
    F --> G[pending callbacks 階段]
    G --> H[idle/prepare 階段]
    H --> I[poll 階段]
    I --> J{有待處理事件?}
    J -->|是| K[執行 I/O 回呼]
    K --> L[清空 Microtask]
    L --> I
    J -->|否| M[check 階段 setImmediate]
    M --> N[close callbacks 階段]
    N --> O{還有待處理的工作?}
    O -->|是| D
    O -->|否| P[程式結束]
```

#### 深入範例

```typescript
import { readFile } from 'node:fs';

console.log('1. Script start');

setTimeout(() => {
  console.log('6. setTimeout 0ms');
  
  Promise.resolve().then(() => {
    console.log('7. Promise inside setTimeout');
  });
  
  process.nextTick(() => {
    console.log('7.5 nextTick inside setTimeout');  // nextTick 先於 Promise
  });
}, 0);

setImmediate(() => {
  console.log('8. setImmediate');
});

readFile(__filename, () => {
  console.log('9. I/O callback');
  
  setTimeout(() => {
    console.log('11. setTimeout inside I/O');
  }, 0);
  
  setImmediate(() => {
    console.log('10. setImmediate inside I/O');  // I/O 回呼中 setImmediate 總是先於 setTimeout
  });
});

Promise.resolve().then(() => {
  console.log('3. Promise 1');
}).then(() => {
  console.log('4. Promise 2');
});

process.nextTick(() => {
  console.log('2. nextTick');
});

console.log('1.5 Script end');

// 典型輸出（I/O 回呼的 setImmediate 在 setTimeout 之前是確定的）
```

---

### 6.5 Microtask Queue 與 Macrotask Queue

#### 優先級詳解

```
優先級（由高到低）：

1. process.nextTick()           ← 最高優先
2. Promise.then/catch/finally   ← Microtask
3. setTimeout / setInterval     ← Macrotask (timers)
4. setImmediate                 ← Macrotask (check)
5. I/O callbacks                ← Macrotask (poll)
```

#### 關鍵規則

| 規則 | 說明 |
|------|------|
| **Microtask 在 Macrotask 之間清空** | 每個 Macrotask 執行完後，清空所有 Microtask |
| **nextTick 優先於 Promise** | nextTick Queue 在 Promise Queue 之前清空 |
| **不要遞迴 nextTick** | 會餓死 Event Loop，阻止 I/O 處理 |
| **I/O 中 setImmediate 先於 setTimeout** | 在 I/O 回呼中，setImmediate 保證先執行 |

---

### 6.6 並行控制與流量管控

#### 限制並行數量

```typescript
// 使用 p-limit 控制並行數
import pLimit from 'p-limit';

const limit = pLimit(5);  // 最多 5 個同時執行

const urls = Array.from({ length: 100 }, (_, i) => `https://api.example.com/items/${i}`);

const results = await Promise.all(
  urls.map(url => limit(() => fetch(url).then(r => r.json())))
);
```

#### 手動實作並行控制

```typescript
async function parallelLimit<T>(
  tasks: (() => Promise<T>)[],
  concurrency: number
): Promise<T[]> {
  const results: T[] = [];
  const executing = new Set<Promise<void>>();

  for (const [index, task] of tasks.entries()) {
    const promise = task().then(result => {
      results[index] = result;
    });
    
    const wrapped = promise.then(() => executing.delete(wrapped));
    executing.add(wrapped);

    if (executing.size >= concurrency) {
      await Promise.race(executing);
    }
  }

  await Promise.all(executing);
  return results;
}

// 使用
const results = await parallelLimit(
  userIds.map(id => () => fetchUser(id)),
  10  // 最多 10 個同時執行
);
```

#### 重試機制

```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  options: { maxRetries?: number; delay?: number; backoff?: number } = {}
): Promise<T> {
  const { maxRetries = 3, delay = 1000, backoff = 2 } = options;
  
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === maxRetries) throw error;
      
      const waitTime = delay * Math.pow(backoff, attempt);
      console.warn(`嘗試 ${attempt + 1} 失敗，${waitTime}ms 後重試...`);
      await new Promise(resolve => globalThis.setTimeout(resolve, waitTime));
    }
  }
  
  throw new Error('Unreachable');
}

// 使用
const data = await withRetry(
  () => fetch('https://api.example.com/data').then(r => r.json()),
  { maxRetries: 3, delay: 1000, backoff: 2 }
);
```

#### 超時控制

```typescript
async function withTimeout<T>(promise: Promise<T>, ms: number): Promise<T> {
  return Promise.race([
    promise,
    new Promise<never>((_, reject) =>
      globalThis.setTimeout(() => reject(new Error(`Timeout after ${ms}ms`)), ms)
    ),
  ]);
}

// 使用 AbortSignal（推薦）
const controller = new AbortController();
const timeoutId = globalThis.setTimeout(() => controller.abort(), 5000);

try {
  const response = await fetch('https://api.example.com/data', {
    signal: controller.signal,
  });
  clearTimeout(timeoutId);
  return await response.json();
} catch (err) {
  if (err.name === 'AbortError') {
    throw new Error('Request timeout');
  }
  throw err;
}
```

#### 章節小練習

1. 寫出 `setTimeout(0)` 、`setImmediate`、`Promise.then`、`process.nextTick` 的執行順序。
2. 實作一個支援重試和超時的 HTTP 客戶端。
3. 使用 `Promise.allSettled` 實作批次發送通知，記錄成功和失敗數量。

#### 實務注意事項

> - 獨立的非同步操作使用 `Promise.all` 平行執行
> - 不要在迴圈中 `await`，改用 `Promise.all` + `map`
> - 大量平行請求使用 `p-limit` 控制並行數
> - 外部 API 呼叫必須設定超時
> - 不穩定的操作加入重試機制（指數退避）
> - 永遠不要遞迴呼叫 `process.nextTick`

---

## 第 7 章：Express 教學

> **版本說明**：Express 5 已於 2024 年 10 月正式釋出，為目前推薦版本。主要變更包括：
> - 路由路徑模式語法更新（使用 `{*splat}` 取代 `*`）
> - `req.query` 預設使用 `simple` 解析器（原為 `extended`）
> - `res.jsonp()` JSONP callback 預設名稱維持 `callback`
> - 移除已棄用的 `req.host`（改用 `req.hostname`）
> - Promise rejection 自動傳遞給 `next(err)`，不再需要手動 try/catch
> - 最低需求 Node.js 18+
>
> 以下範例均適用 Express 5。若使用 Express 4，核心概念相同，部分 API 需微調。

### 7.1 建立 REST API

#### 專案初始化

```bash
mkdir express-api && cd express-api
pnpm init
pnpm add express@5
pnpm add -D typescript @types/express @types/node tsx
npx tsc --init
```

#### 基本結構

```typescript
// src/app.ts
import express from 'express';
import { userRouter } from './routes/user.routes.js';
import { errorHandler } from './middleware/error-handler.js';

const app = express();

// 內建 Middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// 路由
app.use('/api/v1/users', userRouter);

// 健康檢查
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// 錯誤處理（必須放最後）
app.use(errorHandler);

export { app };
```

```typescript
// src/server.ts
import { app } from './app.js';

const PORT = parseInt(process.env.PORT ?? '3000', 10);

const server = app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

// 優雅關機
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});
```

---

### 7.2 Middleware 機制

#### Middleware 執行流程

```mermaid
sequenceDiagram
    participant Client
    participant Logger
    participant Auth
    participant Validator
    participant Controller
    participant ErrorHandler
    
    Client->>Logger: Request
    Logger->>Auth: next()
    Auth->>Validator: next()
    Validator->>Controller: next()
    Controller-->>Client: Response
    
    Note over Auth: 驗證失敗
    Auth-->>ErrorHandler: next(error)
    ErrorHandler-->>Client: Error Response
```

#### 常用 Middleware

```typescript
import { Request, Response, NextFunction } from 'express';

// 請求日誌
function requestLogger(req: Request, res: Response, next: NextFunction) {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.path} ${res.statusCode} ${duration}ms`);
  });
  next();
}

// 請求 ID
function requestId(req: Request, res: Response, next: NextFunction) {
  const id = req.headers['x-request-id'] as string ?? crypto.randomUUID();
  req.headers['x-request-id'] = id;
  res.setHeader('x-request-id', id);
  next();
}

// 認證
function authenticate(req: Request, res: Response, next: NextFunction) {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (!token) {
    res.status(401).json({ error: 'Unauthorized' });
    return;
  }
  try {
    const payload = verifyJwt(token);
    (req as any).user = payload;
    next();
  } catch {
    res.status(401).json({ error: 'Invalid token' });
  }
}

// 使用
app.use(requestId);
app.use(requestLogger);
app.use('/api', authenticate);
```

---

### 7.3 Routing 設計

```typescript
// src/routes/user.routes.ts
import { Router } from 'express';
import { UserController } from '../controllers/user.controller.js';
import { authenticate } from '../middleware/auth.js';
import { validate } from '../middleware/validator.js';
import { CreateUserSchema, UpdateUserSchema } from '../schemas/user.schema.js';

const router = Router();
const controller = new UserController();

router.get('/', controller.findAll);
router.get('/:id', controller.findById);
router.post('/', validate(CreateUserSchema), controller.create);
router.put('/:id', authenticate, validate(UpdateUserSchema), controller.update);
router.delete('/:id', authenticate, controller.delete);

export { router as userRouter };
```

```typescript
// src/controllers/user.controller.ts
import { Request, Response, NextFunction } from 'express';
import { UserService } from '../services/user.service.js';

export class UserController {
  private service = new UserService();

  findAll = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const { page = 1, limit = 20 } = req.query;
      const result = await this.service.findAll(Number(page), Number(limit));
      res.json(result);
    } catch (error) {
      next(error);
    }
  };

  findById = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const user = await this.service.findById(req.params.id);
      if (!user) {
        res.status(404).json({ error: 'User not found' });
        return;
      }
      res.json(user);
    } catch (error) {
      next(error);
    }
  };

  create = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const user = await this.service.create(req.body);
      res.status(201).json(user);
    } catch (error) {
      next(error);
    }
  };

  update = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const user = await this.service.update(req.params.id, req.body);
      res.json(user);
    } catch (error) {
      next(error);
    }
  };

  delete = async (req: Request, res: Response, next: NextFunction) => {
    try {
      await this.service.delete(req.params.id);
      res.status(204).end();
    } catch (error) {
      next(error);
    }
  };
}
```

---

### 7.4 Error Handling

```typescript
// src/errors/app-error.ts
export class AppError extends Error {
  constructor(
    public statusCode: number,
    public code: string,
    message: string,
    public details?: unknown
  ) {
    super(message);
    this.name = 'AppError';
  }

  static badRequest(message: string, details?: unknown) {
    return new AppError(400, 'BAD_REQUEST', message, details);
  }
  static unauthorized(message = 'Unauthorized') {
    return new AppError(401, 'UNAUTHORIZED', message);
  }
  static forbidden(message = 'Forbidden') {
    return new AppError(403, 'FORBIDDEN', message);
  }
  static notFound(message = 'Not Found') {
    return new AppError(404, 'NOT_FOUND', message);
  }
  static conflict(message: string) {
    return new AppError(409, 'CONFLICT', message);
  }
  static internal(message = 'Internal Server Error') {
    return new AppError(500, 'INTERNAL_ERROR', message);
  }
}
```

```typescript
// src/middleware/error-handler.ts
import { Request, Response, NextFunction } from 'express';
import { AppError } from '../errors/app-error.js';
import { ZodError } from 'zod';

export function errorHandler(err: Error, req: Request, res: Response, next: NextFunction) {
  // 已知的應用錯誤
  if (err instanceof AppError) {
    res.status(err.statusCode).json({
      error: {
        code: err.code,
        message: err.message,
        details: err.details,
      },
    });
    return;
  }

  // Zod 驗證錯誤
  if (err instanceof ZodError) {
    res.status(400).json({
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Request validation failed',
        details: err.errors.map(e => ({
          path: e.path.join('.'),
          message: e.message,
        })),
      },
    });
    return;
  }

  // 未知錯誤
  console.error('Unhandled error:', err);
  res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred',
    },
  });
}
```

---

### 7.5 JWT 身分驗證

```typescript
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET!;
const JWT_EXPIRES_IN = '15m';
const REFRESH_TOKEN_EXPIRES_IN = '7d';

interface TokenPayload {
  sub: string;
  email: string;
  role: string;
}

// 產生 Access Token + Refresh Token
function generateTokens(user: User) {
  const payload: TokenPayload = { sub: user.id, email: user.email, role: user.role };
  
  const accessToken = jwt.sign(payload, JWT_SECRET, { expiresIn: JWT_EXPIRES_IN });
  const refreshToken = jwt.sign({ sub: user.id }, JWT_SECRET, { expiresIn: REFRESH_TOKEN_EXPIRES_IN });
  
  return { accessToken, refreshToken };
}

// 驗證 Token
function verifyToken(token: string): TokenPayload {
  return jwt.verify(token, JWT_SECRET) as TokenPayload;
}

// Login 端點
router.post('/auth/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await userService.findByEmail(email);
  
  if (!user || !(await verifyPassword(password, user.passwordHash))) {
    throw AppError.unauthorized('Invalid credentials');
  }
  
  const tokens = generateTokens(user);
  res.json(tokens);
});

// Refresh 端點
router.post('/auth/refresh', async (req, res) => {
  const { refreshToken } = req.body;
  try {
    const payload = jwt.verify(refreshToken, JWT_SECRET) as { sub: string };
    const user = await userService.findById(payload.sub);
    if (!user) throw AppError.unauthorized();
    
    const tokens = generateTokens(user);
    res.json(tokens);
  } catch {
    throw AppError.unauthorized('Invalid refresh token');
  }
});
```

---

### 7.6 Request Validation

```typescript
// src/middleware/validator.ts
import { Request, Response, NextFunction } from 'express';
import { ZodSchema } from 'zod';

export function validate(schema: ZodSchema) {
  return (req: Request, res: Response, next: NextFunction) => {
    const result = schema.safeParse(req.body);
    if (!result.success) {
      res.status(400).json({
        error: {
          code: 'VALIDATION_ERROR',
          message: 'Request validation failed',
          details: result.error.errors,
        },
      });
      return;
    }
    req.body = result.data;  // 使用已驗證/轉換的資料
    next();
  };
}

// src/schemas/user.schema.ts
import { z } from 'zod';

export const CreateUserSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.string().email(),
  password: z.string().min(8).max(128)
    .regex(/[A-Z]/, '需包含大寫字母')
    .regex(/[a-z]/, '需包含小寫字母')
    .regex(/[0-9]/, '需包含數字'),
  role: z.enum(['admin', 'user', 'viewer']).default('user'),
});

export const UpdateUserSchema = CreateUserSchema.partial().omit({ password: true });

export type CreateUserDto = z.infer<typeof CreateUserSchema>;
export type UpdateUserDto = z.infer<typeof UpdateUserSchema>;
```

---

### 7.7 File Upload

```typescript
import multer from 'multer';
import { join } from 'node:path';

// 設定 Multer
const storage = multer.diskStorage({
  destination: './uploads',
  filename: (req, file, cb) => {
    const uniqueName = `${Date.now()}-${crypto.randomUUID()}${extname(file.originalname)}`;
    cb(null, uniqueName);
  },
});

const upload = multer({
  storage,
  limits: {
    fileSize: 10 * 1024 * 1024,  // 10MB
    files: 5,                     // 最多 5 個檔案
  },
  fileFilter: (req, file, cb) => {
    const allowed = ['image/jpeg', 'image/png', 'image/webp', 'application/pdf'];
    if (allowed.includes(file.mimetype)) {
      cb(null, true);
    } else {
      cb(new Error(`不支援的檔案類型: ${file.mimetype}`));
    }
  },
});

// 路由
router.post('/upload', authenticate, upload.single('file'), async (req, res) => {
  if (!req.file) {
    throw AppError.badRequest('No file uploaded');
  }
  res.json({
    filename: req.file.filename,
    size: req.file.size,
    mimetype: req.file.mimetype,
  });
});

// 多檔上傳
router.post('/upload/multiple', authenticate, upload.array('files', 5), async (req, res) => {
  const files = (req.files as Express.Multer.File[]).map(f => ({
    filename: f.filename,
    size: f.size,
  }));
  res.json({ files });
});
```

#### 章節小練習

1. 建立一個 Express REST API，支援 CRUD 操作。
2. 實作全域 Error Handler，處理不同類型的錯誤。
3. 使用 Zod 實作 Request Body 驗證。

#### 實務注意事項

> - 所有 Controller 方法都要使用 try/catch 或統一的 async wrapper
> - 錯誤處理 Middleware 必須有四個參數 `(err, req, res, next)`
> - 驗證必須在 Controller 之前（使用 Middleware）
> - 檔案上傳限制大小與類型
> - JWT Secret 使用環境變數，長度至少 256 bits

### 7.8 Express 效能最佳化

```typescript
// 1. 回應壓縮
import compression from 'compression';

app.use(compression({
  threshold: 1024,  // 只壓縮大於 1KB 的回應
  filter: (req, res) => {
    if (req.headers['x-no-compression']) return false;
    return compression.filter(req, res);
  },
}));

// 2. 靜態檔案快取
app.use('/static', express.static('public', {
  maxAge: '1d',
  etag: true,
  lastModified: true,
  immutable: true,  // 含 hash 的檔案設定永久快取
  setHeaders: (res, path) => {
    if (path.endsWith('.html')) {
      res.setHeader('Cache-Control', 'no-cache');
    }
  },
}));

// 3. Response Time Header
import responseTime from 'response-time';
app.use(responseTime());

// 4. 請求超時
import timeout from 'connect-timeout';
app.use(timeout('30s'));
app.use((req, res, next) => {
  if (!req.timedout) next();
});

// 5. 連線 Keep-Alive
const server = app.listen(3000, () => {
  server.keepAliveTimeout = 65_000;  // 大於 ALB 預設 60s
  server.headersTimeout = 66_000;
});
```

---

### 7.9 Express 安全強化

```typescript
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import cors from 'cors';
import hpp from 'hpp';

// 1. HTTP Security Headers
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:'],
    },
  },
  hsts: { maxAge: 31536000, includeSubDomains: true, preload: true },
}));

// 2. CORS
app.use(cors({
  origin: process.env.CORS_ORIGINS?.split(',') ?? ['http://localhost:3001'],
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Request-Id'],
  credentials: true,
  maxAge: 86400,
}));

// 3. Rate Limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  keyGenerator: (req) => req.ip ?? 'unknown',
  handler: (req, res) => {
    res.status(429).json({
      error: { code: 'RATE_LIMIT_EXCEEDED', message: 'Too many requests' },
    });
  },
});
app.use('/api', limiter);

// 登入端點更嚴格的限制
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true,
});
app.use('/api/auth/login', loginLimiter);

// 4. HTTP Parameter Pollution 防護
app.use(hpp());

// 5. Body Size 限制
app.use(express.json({ limit: '10kb' }));
app.use(express.urlencoded({ extended: true, limit: '10kb' }));

// 6. Request ID 追蹤
import { randomUUID } from 'node:crypto';
app.use((req, res, next) => {
  req.id = (req.headers['x-request-id'] as string) ?? randomUUID();
  res.setHeader('X-Request-Id', req.id);
  next();
});
```

---

### 7.10 Express 與 Graceful Shutdown

```typescript
import { createTerminus } from '@godaddy/terminus';
import http from 'node:http';

const app = express();
const server = http.createServer(app);

createTerminus(server, {
  signal: 'SIGTERM',
  healthChecks: {
    '/health/liveness': async () => 'OK',
    '/health/readiness': async () => {
      await prisma.$queryRaw`SELECT 1`;
      await redis.ping();
      return 'OK';
    },
  },
  onSignal: async () => {
    console.log('Server is shutting down...');
    // 關閉資料庫連線
    await prisma.$disconnect();
    // 關閉 Redis 連線
    await redis.quit();
    // 停止接收新的 BullMQ 任務
    await worker.close();
  },
  onShutdown: async () => {
    console.log('Cleanup finished, server is shutting down');
  },
  beforeShutdown: async () => {
    // 等待進行中的請求完成（K8s 需要）
    await new Promise(resolve => setTimeout(resolve, 5000));
  },
  timeout: 30_000,
  logger: console.error,
});

server.listen(3000, () => {
  console.log('Server listening on port 3000');
});
```

---

## 第 8 章：Fastify 教學

### 8.1 高效能 API 建構

#### 概述

Fastify 是一個高效能的 Node.js Web 框架，目前最新穩定版為 **Fastify 5**（v5.8+）。其效能比 Express 快 2-3 倍，內建 JSON Schema 驗證與序列化。Fastify 5 主要變更包括移除 `reply.res` 存取、TypeBox 套件更名為 `typebox`、改進 content-type 解析等。

#### 效能比較

| 框架 | 每秒請求數（req/s） | 延遲（ms） | 特色 |
|------|---------------------|-----------|------|
| **Fastify** | ~75,000 | 0.13 | Schema 驗證、序列化 |
| Express | ~30,000 | 0.35 | 龐大生態系 |
| Koa | ~45,000 | 0.22 | 輕量級 |
| Hono | ~80,000 | 0.12 | 多執行環境 |

#### 基本結構

```typescript
// src/app.ts
import Fastify from 'fastify';

const app = Fastify({
  logger: {
    level: 'info',
    transport: {
      target: 'pino-pretty',
      options: { colorize: true },
    },
  },
  requestTimeout: 30000,
  bodyLimit: 10 * 1024 * 1024,
});

// 路由
app.get('/api/health', async (request, reply) => {
  return { status: 'ok', uptime: process.uptime() };
});

// 啟動伺服器
const start = async () => {
  try {
    await app.listen({ port: 3000, host: '0.0.0.0' });
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
};
start();
```

---

### 8.2 Plugin 架構

```mermaid
graph TD
    A[Fastify 根實例] --> B[Plugin: Database]
    A --> C[Plugin: Auth]
    A --> D[Plugin: Routes]
    
    B --> B1[db connection]
    C --> C1[JWT verify]
    D --> D1[User Routes]
    D --> D2[Order Routes]
    
    D1 --> B
    D1 --> C
```

```typescript
// plugins/database.ts
import fp from 'fastify-plugin';
import { PrismaClient } from '@prisma/client';

export default fp(async (fastify) => {
  const prisma = new PrismaClient();
  await prisma.$connect();
  
  fastify.decorate('prisma', prisma);
  
  fastify.addHook('onClose', async () => {
    await prisma.$disconnect();
  });
});

// plugins/auth.ts
import fp from 'fastify-plugin';
import fastifyJwt from '@fastify/jwt';

export default fp(async (fastify) => {
  await fastify.register(fastifyJwt, {
    secret: process.env.JWT_SECRET!,
  });

  fastify.decorate('authenticate', async (request: any, reply: any) => {
    try {
      await request.jwtVerify();
    } catch {
      reply.code(401).send({ error: 'Unauthorized' });
    }
  });
});

// 註冊 Plugin
app.register(import('./plugins/database.js'));
app.register(import('./plugins/auth.js'));
app.register(import('./routes/user.routes.js'), { prefix: '/api/v1/users' });
```

---

### 8.3 Schema Validation 與序列化

Fastify 使用 JSON Schema 進行請求驗證和回應序列化（使用 `fast-json-stringify`，比 `JSON.stringify` 快 2-3 倍）。

```typescript
// routes/user.routes.ts
import { FastifyPluginAsync } from 'fastify';

const userRoutes: FastifyPluginAsync = async (fastify) => {
  // JSON Schema 定義
  const createUserSchema = {
    body: {
      type: 'object',
      required: ['name', 'email'],
      properties: {
        name: { type: 'string', minLength: 1, maxLength: 100 },
        email: { type: 'string', format: 'email' },
        role: { type: 'string', enum: ['admin', 'user', 'viewer'], default: 'user' },
      },
      additionalProperties: false,
    },
    response: {
      201: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          name: { type: 'string' },
          email: { type: 'string' },
          role: { type: 'string' },
          createdAt: { type: 'string' },
        },
      },
    },
  };

  fastify.post('/', { schema: createUserSchema }, async (request, reply) => {
    const body = request.body as { name: string; email: string; role: string };
    const user = await fastify.prisma.user.create({ data: body });
    reply.code(201).send(user);
  });

  // 搭配 TypeBox（TypeScript 友善的 Schema）
  // pnpm add @sinclair/typebox
  // import { Type, Static } from '@sinclair/typebox';
  // const UserSchema = Type.Object({ name: Type.String(), ... });
  // type UserType = Static<typeof UserSchema>;
};

export default userRoutes;
```

---

### 8.4 效能比較與調校

```typescript
// 效能調校建議
const app = Fastify({
  // 關閉請求 ID（若不需要追蹤）
  // disableRequestLogging: true,
  
  // 調整 JSON 解析器
  bodyLimit: 1048576,  // 1MB
  
  // 使用自定義序列化器
  serializerOpts: {
    reftypes: { mode: 'strip' },
  },
});

// 使用 Reply 快取
fastify.get('/api/static-data', async (request, reply) => {
  reply.header('Cache-Control', 'public, max-age=3600');
  return staticData;
});
```

#### 章節小練習

1. 建立一個 Fastify REST API，使用 JSON Schema 驗證。
2. 實作 Fastify Plugin 封裝資料庫連線。
3. 對比 Express 和 Fastify 的效能差異。

#### 實務注意事項

> - Fastify 內建日誌使用 Pino（高效能）
> - Schema 驗證同時提供安全性和效能（回應序列化）
> - 使用 Plugin 封裝功能，保持封裝性
> - NestJS 可搭配 Fastify 作為底層 HTTP 引擎

### 8.5 TypeBox Schema 驗證

```typescript
import { Type, Static } from '@sinclair/typebox';

// 使用 TypeBox 定義具有 TypeScript 型別推導的 Schema
const CreateUserSchema = Type.Object({
  name: Type.String({ minLength: 1, maxLength: 100 }),
  email: Type.String({ format: 'email' }),
  age: Type.Optional(Type.Integer({ minimum: 0, maximum: 150 })),
  role: Type.Union([Type.Literal('admin'), Type.Literal('user')]),
  tags: Type.Array(Type.String(), { maxItems: 10 }),
});

type CreateUserDto = Static<typeof CreateUserSchema>;

// 在 Fastify 中使用
fastify.post<{ Body: CreateUserDto }>('/api/users', {
  schema: {
    body: CreateUserSchema,
    response: {
      201: Type.Object({
        id: Type.String({ format: 'uuid' }),
        name: Type.String(),
        email: Type.String(),
        createdAt: Type.String({ format: 'date-time' }),
      }),
      400: Type.Object({
        statusCode: Type.Number(),
        error: Type.String(),
        message: Type.String(),
      }),
    },
  },
}, async (request, reply) => {
  const user = await userService.create(request.body);
  reply.status(201).send(user);
});
```

> **✅ TypeBox 優勢**：同一份定義同時產生 JSON Schema（驗證用）和 TypeScript 型別（開發用），實現「Single Source of Truth」。

---

### 8.6 Fastify Hooks 生命週期

```mermaid
graph LR
    A[onRequest] --> B[preParsing]
    B --> C[preValidation]
    C --> D[preHandler]
    D --> E[Handler]
    E --> F[preSerialization]
    F --> G[onSend]
    G --> H[onResponse]
```

```typescript
// 全域 Hook — 請求計時
fastify.addHook('onRequest', async (request) => {
  request.startTime = performance.now();
});

fastify.addHook('onResponse', async (request, reply) => {
  const duration = performance.now() - request.startTime;
  request.log.info({
    method: request.method,
    url: request.url,
    statusCode: reply.statusCode,
    durationMs: duration.toFixed(2),
  }, 'request completed');
});

// 路由級 Hook — 認證
fastify.addHook('preHandler', async (request, reply) => {
  if (request.routeOptions.config.requireAuth) {
    const token = request.headers.authorization?.replace('Bearer ', '');
    if (!token) {
      reply.status(401).send({ error: 'Unauthorized' });
      return;
    }
    request.user = await verifyToken(token);
  }
});

// onError Hook — 錯誤追蹤
fastify.addHook('onError', async (request, reply, error) => {
  request.log.error({ err: error, requestId: request.id }, 'Request error');
  // 發送到錯誤追蹤服務（Sentry 等）
});
```

---

### 8.7 Fastify 封裝性與裝飾器

```typescript
// 封裝性（Encapsulation）— Fastify 核心概念
// 每個 Plugin 有自己的封裝上下文

import fp from 'fastify-plugin';

// 使用 fp() 打破封裝（全域可用）
const dbPlugin = fp(async (fastify) => {
  const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
  
  // 裝飾器：添加到 fastify 實例
  fastify.decorate('db', pool);
  
  // 生命週期管理
  fastify.addHook('onClose', async () => {
    await pool.end();
  });
});

// 不使用 fp() 的 Plugin（限於當前上下文）
async function userRoutes(fastify: FastifyInstance) {
  // 這裡的 fastify.db 可用（因為 dbPlugin 用了 fp）
  
  // 路由級裝飾器
  fastify.decorateRequest('user', null);
  
  fastify.get('/api/users', async (request) => {
    const result = await fastify.db.query('SELECT * FROM users');
    return result.rows;
  });
  
  fastify.get('/api/users/:id', async (request) => {
    const { id } = request.params as { id: string };
    const result = await fastify.db.query('SELECT * FROM users WHERE id = $1', [id]);
    if (result.rows.length === 0) {
      throw fastify.httpErrors.notFound('User not found');
    }
    return result.rows[0];
  });
}

// 註冊
fastify.register(dbPlugin);
fastify.register(userRoutes, { prefix: '/v1' });
```

---

### 8.8 Fastify Rate Limiting 與安全

```typescript
import fastifyRateLimit from '@fastify/rate-limit';
import fastifyHelmet from '@fastify/helmet';
import fastifyCors from '@fastify/cors';

// Rate Limiting
await fastify.register(fastifyRateLimit, {
  max: 100,
  timeWindow: '1 minute',
  keyGenerator: (request) => request.ip,
  errorResponseBuilder: (request, context) => ({
    statusCode: 429,
    error: 'Too Many Requests',
    message: `Rate limit exceeded. Retry in ${context.after}`,
    retryAfter: context.after,
  }),
});

// 針對特定路由設定更嚴格的限制
fastify.post('/api/auth/login', {
  config: {
    rateLimit: { max: 5, timeWindow: '15 minutes' },
  },
}, loginHandler);

// Helmet
await fastify.register(fastifyHelmet, {
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
    },
  },
});

// CORS
await fastify.register(fastifyCors, {
  origin: process.env.CORS_ORIGINS?.split(',') ?? ['https://app.company.com'],
  credentials: true,
});
```

---

### 8.9 Fastify 錯誤處理

```typescript
import { FastifyError } from 'fastify';

// 自定義錯誤處理器
fastify.setErrorHandler((error: FastifyError, request, reply) => {
  request.log.error({ err: error }, 'Application error');

  // 驗證錯誤
  if (error.validation) {
    return reply.status(400).send({
      statusCode: 400,
      error: 'Validation Error',
      message: 'Request validation failed',
      details: error.validation.map(v => ({
        field: v.instancePath,
        message: v.message,
      })),
    });
  }

  // HTTP 錯誤
  if (error.statusCode) {
    return reply.status(error.statusCode).send({
      statusCode: error.statusCode,
      error: error.name,
      message: error.message,
    });
  }

  // 未預期錯誤
  reply.status(500).send({
    statusCode: 500,
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'production'
      ? 'An unexpected error occurred'
      : error.message,
  });
});

// 404 處理
fastify.setNotFoundHandler((request, reply) => {
  reply.status(404).send({
    statusCode: 404,
    error: 'Not Found',
    message: `Route ${request.method} ${request.url} not found`,
  });
});
```

---

## 第 9 章：NestJS 教學

### 9.1 Module 模組設計

#### 概述

NestJS 是基於 TypeScript 的企業級框架，深度借鑑 Angular 的模組化架構，內建依賴注入、裝飾器模式和開箱即用的企業功能。

```mermaid
graph TD
    A[AppModule] --> B[UserModule]
    A --> C[AuthModule]
    A --> D[OrderModule]
    A --> E[SharedModule]
    
    B --> B1[UserController]
    B --> B2[UserService]
    B --> B3[UserRepository]
    
    C --> C1[AuthController]
    C --> C2[AuthService]
    C --> C3[JwtStrategy]
    
    D --> D1[OrderController]
    D --> D2[OrderService]
    
    E --> E1[LoggerService]
    E --> E2[ConfigService]
```

```typescript
// src/user/user.module.ts
import { Module } from '@nestjs/common';
import { UserController } from './user.controller.js';
import { UserService } from './user.service.js';
import { PrismaModule } from '../prisma/prisma.module.js';

@Module({
  imports: [PrismaModule],
  controllers: [UserController],
  providers: [UserService],
  exports: [UserService],  // 供其他 Module 使用
})
export class UserModule {}
```

```typescript
// src/app.module.ts
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './user/user.module.js';
import { AuthModule } from './auth/auth.module.js';
import { OrderModule } from './order/order.module.js';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    UserModule,
    AuthModule,
    OrderModule,
  ],
})
export class AppModule {}
```

---

### 9.2 Controller 控制器

```typescript
// src/user/user.controller.ts
import { Controller, Get, Post, Put, Delete, Body, Param, Query, HttpCode, HttpStatus, ParseUUIDPipe } from '@nestjs/common';
import { UserService } from './user.service.js';
import { CreateUserDto } from './dto/create-user.dto.js';
import { UpdateUserDto } from './dto/update-user.dto.js';
import { PaginationDto } from '../common/dto/pagination.dto.js';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';

@ApiTags('Users')
@Controller('users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  @ApiOperation({ summary: '取得使用者列表' })
  findAll(@Query() pagination: PaginationDto) {
    return this.userService.findAll(pagination);
  }

  @Get(':id')
  @ApiOperation({ summary: '取得單一使用者' })
  @ApiResponse({ status: 404, description: 'User not found' })
  findById(@Param('id', ParseUUIDPipe) id: string) {
    return this.userService.findById(id);
  }

  @Post()
  @HttpCode(HttpStatus.CREATED)
  @ApiOperation({ summary: '建立使用者' })
  create(@Body() dto: CreateUserDto) {
    return this.userService.create(dto);
  }

  @Put(':id')
  update(@Param('id', ParseUUIDPipe) id: string, @Body() dto: UpdateUserDto) {
    return this.userService.update(id, dto);
  }

  @Delete(':id')
  @HttpCode(HttpStatus.NO_CONTENT)
  remove(@Param('id', ParseUUIDPipe) id: string) {
    return this.userService.remove(id);
  }
}
```

---

### 9.3 Provider 與 Service

```typescript
// src/user/user.service.ts
import { Injectable, NotFoundException, ConflictException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service.js';
import { CreateUserDto } from './dto/create-user.dto.js';
import { UpdateUserDto } from './dto/update-user.dto.js';
import { PaginationDto } from '../common/dto/pagination.dto.js';

@Injectable()
export class UserService {
  constructor(private readonly prisma: PrismaService) {}

  async findAll(pagination: PaginationDto) {
    const { page = 1, limit = 20 } = pagination;
    const skip = (page - 1) * limit;

    const [data, total] = await Promise.all([
      this.prisma.user.findMany({ skip, take: limit, orderBy: { createdAt: 'desc' } }),
      this.prisma.user.count(),
    ]);

    return {
      data,
      meta: {
        total,
        page,
        limit,
        totalPages: Math.ceil(total / limit),
      },
    };
  }

  async findById(id: string) {
    const user = await this.prisma.user.findUnique({ where: { id } });
    if (!user) {
      throw new NotFoundException(`User with ID ${id} not found`);
    }
    return user;
  }

  async create(dto: CreateUserDto) {
    const existing = await this.prisma.user.findUnique({ where: { email: dto.email } });
    if (existing) {
      throw new ConflictException(`Email ${dto.email} already exists`);
    }
    return this.prisma.user.create({ data: dto });
  }

  async update(id: string, dto: UpdateUserDto) {
    await this.findById(id);  // 確認存在
    return this.prisma.user.update({ where: { id }, data: dto });
  }

  async remove(id: string) {
    await this.findById(id);
    await this.prisma.user.delete({ where: { id } });
  }
}
```

---

### 9.4 Dependency Injection 依賴注入

```mermaid
graph TD
    A[NestJS IoC Container] -->|注入| B[UserController]
    A -->|注入| C[UserService]
    A -->|注入| D[PrismaService]
    
    B -->|依賴| C
    C -->|依賴| D
```

```typescript
// 自定義 Provider
import { Module } from '@nestjs/common';

// 值 Provider
const configProvider = {
  provide: 'APP_CONFIG',
  useValue: { apiVersion: 'v1', maxRetries: 3 },
};

// 工廠 Provider
const dbProvider = {
  provide: 'DATABASE',
  useFactory: async (config: ConfigService) => {
    const client = new PrismaClient({
      datasources: { db: { url: config.get('DATABASE_URL') } },
    });
    await client.$connect();
    return client;
  },
  inject: [ConfigService],
};

// 介面 Provider（Token）
const LOGGER_TOKEN = Symbol('LOGGER');
const loggerProvider = {
  provide: LOGGER_TOKEN,
  useClass: process.env.NODE_ENV === 'production' ? PinoLogger : ConsoleLogger,
};

@Module({
  providers: [configProvider, dbProvider, loggerProvider],
  exports: [configProvider, dbProvider, loggerProvider],
})
export class CoreModule {}
```

---

### 9.5 Guard 守衛

```typescript
// src/auth/guards/jwt-auth.guard.ts
import { Injectable, CanActivate, ExecutionContext, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class JwtAuthGuard implements CanActivate {
  constructor(private readonly jwtService: JwtService) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const token = this.extractToken(request);
    
    if (!token) {
      throw new UnauthorizedException('Missing authentication token');
    }
    
    try {
      const payload = await this.jwtService.verifyAsync(token);
      request.user = payload;
      return true;
    } catch {
      throw new UnauthorizedException('Invalid authentication token');
    }
  }

  private extractToken(request: any): string | undefined {
    return request.headers.authorization?.replace('Bearer ', '');
  }
}

// src/auth/guards/roles.guard.ts
import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private readonly reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.get<string[]>('roles', context.getHandler());
    if (!requiredRoles) return true;
    
    const request = context.switchToHttp().getRequest();
    return requiredRoles.includes(request.user?.role);
  }
}

// 使用
@UseGuards(JwtAuthGuard, RolesGuard)
@Roles('admin')
@Delete(':id')
remove(@Param('id') id: string) { /* ... */ }
```

---

### 9.6 Interceptor 攔截器

```typescript
// src/common/interceptors/transform.interceptor.ts
import { Injectable, NestInterceptor, ExecutionContext, CallHandler } from '@nestjs/common';
import { Observable, map } from 'rxjs';

// 統一回應格式
@Injectable()
export class TransformInterceptor<T> implements NestInterceptor<T, any> {
  intercept(context: ExecutionContext, next: CallHandler<T>): Observable<any> {
    return next.handle().pipe(
      map(data => ({
        success: true,
        data,
        timestamp: new Date().toISOString(),
      }))
    );
  }
}

// 日誌攔截器
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  private readonly logger = new Logger(LoggingInterceptor.name);

  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const request = context.switchToHttp().getRequest();
    const { method, url } = request;
    const now = Date.now();

    return next.handle().pipe(
      tap(() => {
        this.logger.log(`${method} ${url} - ${Date.now() - now}ms`);
      })
    );
  }
}

// 全域註冊
app.useGlobalInterceptors(new TransformInterceptor());
```

---

### 9.7 Pipe 管道

```typescript
// 內建 Pipe
import { ParseIntPipe, ParseUUIDPipe, DefaultValuePipe, ValidationPipe } from '@nestjs/common';

@Get()
findAll(
  @Query('page', new DefaultValuePipe(1), ParseIntPipe) page: number,
  @Query('limit', new DefaultValuePipe(20), ParseIntPipe) limit: number,
) { /* ... */ }

// 全域 ValidationPipe
app.useGlobalPipes(new ValidationPipe({
  whitelist: true,           // 自動移除未定義的屬性
  forbidNonWhitelisted: true, // 有未定義屬性時拋出錯誤
  transform: true,            // 自動型別轉換
  transformOptions: {
    enableImplicitConversion: true,
  },
}));

// 自定義 Pipe
@Injectable()
export class ParseDatePipe implements PipeTransform<string, Date> {
  transform(value: string): Date {
    const date = new Date(value);
    if (isNaN(date.getTime())) {
      throw new BadRequestException(`Invalid date: ${value}`);
    }
    return date;
  }
}
```

---

### 9.8 CQRS 模式

```typescript
// 安裝
// pnpm add @nestjs/cqrs

// Command（寫入操作）
export class CreateOrderCommand {
  constructor(
    public readonly userId: string,
    public readonly items: OrderItem[],
  ) {}
}

@CommandHandler(CreateOrderCommand)
export class CreateOrderHandler implements ICommandHandler<CreateOrderCommand> {
  constructor(private readonly orderRepo: OrderRepository) {}

  async execute(command: CreateOrderCommand) {
    const order = Order.create(command.userId, command.items);
    await this.orderRepo.save(order);
    return order;
  }
}

// Query（讀取操作）
export class GetOrderQuery {
  constructor(public readonly orderId: string) {}
}

@QueryHandler(GetOrderQuery)
export class GetOrderHandler implements IQueryHandler<GetOrderQuery> {
  constructor(private readonly orderRepo: OrderRepository) {}

  async execute(query: GetOrderQuery) {
    return this.orderRepo.findById(query.orderId);
  }
}

// 在 Controller 中使用
@Controller('orders')
export class OrderController {
  constructor(
    private readonly commandBus: CommandBus,
    private readonly queryBus: QueryBus,
  ) {}

  @Post()
  create(@Body() dto: CreateOrderDto, @Req() req: any) {
    return this.commandBus.execute(new CreateOrderCommand(req.user.id, dto.items));
  }

  @Get(':id')
  findById(@Param('id') id: string) {
    return this.queryBus.execute(new GetOrderQuery(id));
  }
}
```

#### 章節小練習

1. 建立一個 NestJS Module，包含 Controller、Service 和 DTO。
2. 實作 JWT Guard 和 Roles Guard。
3. 使用 Interceptor 實作統一回應格式。

#### 實務注意事項

> - NestJS 適合中大型企業專案，小型 API 可能過度工程
> - 使用 `@nestjs/platform-fastify` 替代預設的 Express 提升效能
> - 善用 Module 封裝和 DI 實現鬆耦合
> - DTO 使用 class-validator 或 Zod 進行驗證
> - CQRS 模式適合讀寫分離場景，簡單 CRUD 不需要

### 9.9 NestJS 微服務模式

```typescript
// 使用 Redis 作為 Transport Layer
// main.ts
import { MicroserviceOptions, Transport } from '@nestjs/microservices';

const app = await NestFactory.create(AppModule);

// 同時啟動 HTTP 和微服務
app.connectMicroservice<MicroserviceOptions>({
  transport: Transport.REDIS,
  options: {
    host: process.env.REDIS_HOST ?? 'localhost',
    port: 6379,
  },
});

await app.startAllMicroservices();
await app.listen(3000);

// 事件發送端
@Injectable()
export class OrderService {
  constructor(
    @Inject('ORDER_SERVICE') private readonly client: ClientProxy,
  ) {}

  async createOrder(dto: CreateOrderDto) {
    const order = await this.saveOrder(dto);

    // 發送事件（fire-and-forget）
    this.client.emit('order.created', {
      orderId: order.id,
      userId: dto.userId,
      total: order.total,
    });

    return order;
  }

  // Request-Response 模式（等待回應）
  async validateInventory(items: OrderItem[]) {
    return firstValueFrom(
      this.client.send('inventory.validate', { items })
    );
  }
}

// 事件接收端（另一個微服務）
@Controller()
export class NotificationController {
  @EventPattern('order.created')
  async handleOrderCreated(@Payload() data: OrderCreatedEvent) {
    await this.emailService.sendOrderConfirmation(data.userId, data.orderId);
    await this.pushService.notify(data.userId, 'Order placed successfully');
  }

  @MessagePattern('inventory.validate')
  async validateInventory(@Payload() data: { items: OrderItem[] }) {
    const results = await this.inventoryService.checkStock(data.items);
    return { valid: results.every(r => r.available), details: results };
  }
}

// Module 註冊
@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'ORDER_SERVICE',
        transport: Transport.REDIS,
        options: { host: 'localhost', port: 6379 },
      },
    ]),
  ],
})
export class OrderModule {}
```

---

### 9.10 NestJS 排程任務

```typescript
import { Injectable } from '@nestjs/common';
import { Cron, CronExpression, Interval, Timeout } from '@nestjs/schedule';

@Injectable()
export class TaskService {
  private readonly logger = new Logger(TaskService.name);

  // 每天凌晨 2 點清理過期 Token
  @Cron('0 2 * * *', { name: 'cleanExpiredTokens', timeZone: 'Asia/Taipei' })
  async cleanExpiredTokens() {
    const deleted = await this.prisma.refreshToken.deleteMany({
      where: { expiresAt: { lt: new Date() } },
    });
    this.logger.log(`Cleaned ${deleted.count} expired tokens`);
  }

  // 每 5 分鐘同步快取
  @Interval(5 * 60 * 1000)
  async syncCache() {
    await this.cacheService.warmUp();
  }

  // 每週一早上 9 點發送週報
  @Cron(CronExpression.EVERY_WEEK, { name: 'weeklyReport' })
  async sendWeeklyReport() {
    const report = await this.analyticsService.generateWeeklyReport();
    await this.emailService.sendReport(report);
  }

  // 應用啟動 10 秒後初始化資料
  @Timeout(10_000)
  async initializeData() {
    await this.seedService.ensureDefaultData();
    this.logger.log('Default data initialized');
  }
}

// 動態控制排程
@Injectable()
export class ScheduleManager {
  constructor(private readonly schedulerRegistry: SchedulerRegistry) {}

  // 暫停排程
  pauseJob(name: string) {
    const job = this.schedulerRegistry.getCronJob(name);
    job.stop();
  }

  // 恢復排程
  resumeJob(name: string) {
    const job = this.schedulerRegistry.getCronJob(name);
    job.start();
  }

  // 列出所有排程
  listJobs(): string[] {
    const jobs = this.schedulerRegistry.getCronJobs();
    return [...jobs.keys()];
  }
}
```

---

## 第 10 章：API 設計最佳實務

### 10.1 RESTful API 設計原則

#### URL 設計規範

| 規則 | ✅ 正確 | ❌ 錯誤 |
|------|---------|---------|
| 使用複數名詞 | `/api/users` | `/api/user` |
| 使用小寫 | `/api/order-items` | `/api/OrderItems` |
| 使用連字號 | `/api/order-items` | `/api/order_items` |
| 不要用動詞 | `POST /api/orders` | `/api/createOrder` |
| 巢狀資源 | `/api/users/123/orders` | `/api/getUserOrders?id=123` |
| 版本控制 | `/api/v1/users` | `/api/users?version=1` |

#### HTTP 方法對應

| 方法 | 操作 | 成功狀態碼 | 範例 |
|------|------|-----------|------|
| `GET` | 查詢 | `200` | `GET /api/v1/users` |
| `POST` | 建立 | `201` | `POST /api/v1/users` |
| `PUT` | 完整更新 | `200` | `PUT /api/v1/users/123` |
| `PATCH` | 部分更新 | `200` | `PATCH /api/v1/users/123` |
| `DELETE` | 刪除 | `204` | `DELETE /api/v1/users/123` |

---

### 10.2 OpenAPI / Swagger 文件化

```typescript
// NestJS + Swagger 設定
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

const config = new DocumentBuilder()
  .setTitle('Enterprise API')
  .setDescription('企業級 API 文件')
  .setVersion('1.0')
  .addBearerAuth()
  .addTag('Users', '使用者管理')
  .addTag('Orders', '訂單管理')
  .build();

const document = SwaggerModule.createDocument(app, config);
SwaggerModule.setup('api-docs', app, document);

// DTO 裝飾器
import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';

export class CreateUserDto {
  @ApiProperty({ description: '使用者名稱', example: 'John Doe' })
  name: string;

  @ApiProperty({ description: '電子郵件', example: 'john@example.com' })
  email: string;

  @ApiPropertyOptional({ description: '年齡', minimum: 0, maximum: 150 })
  age?: number;
}
```

---

### 10.3 API Versioning 策略

| 策略 | 範例 | 優點 | 缺點 |
|------|------|------|------|
| **URL 路徑** | `/api/v1/users` | 簡單直覺 | URL 膨脹 |
| **Header** | `Accept: application/vnd.api.v1+json` | URL 乾淨 | 不直覺 |
| **Query Parameter** | `/api/users?version=1` | 簡單 | 不夠 REST |

```typescript
// NestJS 版本控制
import { VersioningType } from '@nestjs/common';

app.enableVersioning({
  type: VersioningType.URI,
  defaultVersion: '1',
  prefix: 'api/v',
});

@Controller({ path: 'users', version: '2' })
export class UserV2Controller {
  // 只處理 /api/v2/users
}
```

> **✅ 企業推薦**：使用 URL 路徑版本控制（最直覺、最易於除錯）。

---

### 10.4 統一錯誤碼設計

```typescript
// 統一錯誤回應格式
interface ErrorResponse {
  error: {
    code: string;             // 機器可讀的錯誤碼
    message: string;          // 人類可讀的訊息
    details?: ErrorDetail[];  // 細節（驗證錯誤等）
    traceId?: string;         // 追蹤 ID
  };
}

// 錯誤碼設計
const ERROR_CODES = {
  // 通用錯誤 (1xxx)
  VALIDATION_ERROR: '1001',
  UNAUTHORIZED: '1002',
  FORBIDDEN: '1003',
  NOT_FOUND: '1004',
  CONFLICT: '1005',
  RATE_LIMITED: '1006',
  
  // 使用者相關 (2xxx)
  USER_NOT_FOUND: '2001',
  USER_ALREADY_EXISTS: '2002',
  USER_DISABLED: '2003',
  
  // 訂單相關 (3xxx)
  ORDER_NOT_FOUND: '3001',
  ORDER_ALREADY_PAID: '3002',
  INSUFFICIENT_STOCK: '3003',
} as const;
```

---

### 10.5 Idempotency 冪等性設計

```typescript
// 冪等性 Key Middleware
import { createHash } from 'node:crypto';

async function idempotencyMiddleware(req: Request, res: Response, next: NextFunction) {
  const idempotencyKey = req.headers['idempotency-key'] as string;
  
  if (!idempotencyKey) {
    next();
    return;
  }

  // 檢查是否已處理過
  const cached = await redis.get(`idempotency:${idempotencyKey}`);
  if (cached) {
    const result = JSON.parse(cached);
    res.status(result.statusCode).json(result.body);
    return;
  }

  // 攔截回應並快取
  const originalJson = res.json.bind(res);
  res.json = (body: any) => {
    redis.setex(
      `idempotency:${idempotencyKey}`,
      86400,  // 24 小時
      JSON.stringify({ statusCode: res.statusCode, body })
    );
    return originalJson(body);
  };

  next();
}
```

---

### 10.6 Pagination 分頁設計

#### 三種分頁策略

| 策略 | 優點 | 缺點 | 適用場景 |
|------|------|------|----------|
| **Offset-based** | 簡單、可跳頁 | 大量資料效能差 | 後台管理 |
| **Cursor-based** | 效能穩定 | 不能跳頁 | 無限滾動、API |
| **Keyset-based** | 效能最佳 | 需要排序欄位索引 | 大量資料 |

```typescript
// Cursor-based 分頁
interface CursorPaginationParams {
  cursor?: string;
  limit?: number;
  direction?: 'next' | 'prev';
}

interface CursorPaginationResult<T> {
  data: T[];
  cursor: {
    next: string | null;
    prev: string | null;
  };
  hasMore: boolean;
}

async function findWithCursor(params: CursorPaginationParams): Promise<CursorPaginationResult<User>> {
  const { cursor, limit = 20 } = params;
  
  const users = await prisma.user.findMany({
    take: limit + 1,  // 多取一筆判斷是否有下一頁
    ...(cursor ? { cursor: { id: cursor }, skip: 1 } : {}),
    orderBy: { createdAt: 'desc' },
  });

  const hasMore = users.length > limit;
  const data = hasMore ? users.slice(0, -1) : users;

  return {
    data,
    cursor: {
      next: hasMore ? data[data.length - 1].id : null,
      prev: cursor ?? null,
    },
    hasMore,
  };
}
```

---

### 10.7 GraphQL 簡介與對比

#### REST vs GraphQL

| 特性 | REST | GraphQL |
|------|------|---------|
| **資料取得** | 固定結構 | 客戶端指定欄位 |
| **Over-fetching** | 常見 | 不存在 |
| **Under-fetching** | 需多次請求 | 單次請求 |
| **快取** | HTTP 快取友善 | 需額外設定 |
| **學習曲線** | 低 | 中高 |
| **適用場景** | 通用 API | 複雜前端查詢 |

```typescript
// NestJS + GraphQL 簡單範例
import { Query, Resolver, Args } from '@nestjs/graphql';

@Resolver(() => User)
export class UserResolver {
  constructor(private readonly userService: UserService) {}

  @Query(() => [User])
  users() {
    return this.userService.findAll();
  }

  @Query(() => User)
  user(@Args('id') id: string) {
    return this.userService.findById(id);
  }
}
```

> **✅ 企業建議**：
> - 多數場景使用 REST（簡單、標準化）
> - 前端有複雜查詢需求時考慮 GraphQL
> - BFF 層可用 GraphQL 聚合多個微服務

#### 章節小練習

1. 設計一套電商 API 的 URL 結構。
2. 實作 Cursor-based 分頁。
3. 設計一套統一的錯誤碼體系。

#### 實務注意事項

> - URL 使用複數名詞、小寫、連字號
> - 回應格式統一（包含 error 格式）
> - 關鍵寫入操作實作冪等性
> - 大量資料使用 Cursor-based 分頁
> - 使用 OpenAPI 自動產生 API 文件
> - API 版本控制從第一天就規劃

### 10.8 WebSocket 即時通訊 API

```typescript
import { WebSocketServer, WebSocket } from 'ws';

// 建立 WebSocket 伺服器
const wss = new WebSocketServer({ port: 8080 });

interface Client {
  ws: WebSocket;
  userId: string;
  rooms: Set<string>;
}

const clients = new Map<string, Client>();

wss.on('connection', (ws, req) => {
  const userId = authenticateWebSocket(req);
  const client: Client = { ws, userId, rooms: new Set() };
  clients.set(userId, client);

  ws.on('message', (data) => {
    const message = JSON.parse(data.toString());
    
    switch (message.type) {
      case 'join':
        client.rooms.add(message.room);
        broadcast(message.room, { type: 'user-joined', userId });
        break;
      case 'chat':
        broadcast(message.room, {
          type: 'chat',
          userId,
          text: message.text,
          timestamp: new Date().toISOString(),
        });
        break;
      case 'leave':
        client.rooms.delete(message.room);
        broadcast(message.room, { type: 'user-left', userId });
        break;
    }
  });

  ws.on('close', () => {
    client.rooms.forEach(room => broadcast(room, { type: 'user-left', userId }));
    clients.delete(userId);
  });

  // Heartbeat
  ws.on('pong', () => { (ws as any).isAlive = true; });
});

function broadcast(room: string, data: any) {
  clients.forEach(client => {
    if (client.rooms.has(room) && client.ws.readyState === WebSocket.OPEN) {
      client.ws.send(JSON.stringify(data));
    }
  });
}

// Heartbeat 監控
setInterval(() => {
  wss.clients.forEach((ws: any) => {
    if (!ws.isAlive) return ws.terminate();
    ws.isAlive = false;
    ws.ping();
  });
}, 30000);
```

#### Socket.IO 替代方案

```typescript
import { Server } from 'socket.io';

const io = new Server(httpServer, {
  cors: { origin: 'https://app.company.com' },
  transports: ['websocket', 'polling'],
});

io.use(async (socket, next) => {
  const token = socket.handshake.auth.token;
  try {
    const user = await verifyToken(token);
    socket.data.user = user;
    next();
  } catch (err) {
    next(new Error('Authentication failed'));
  }
});

io.on('connection', (socket) => {
  const userId = socket.data.user.id;
  socket.join(`user:${userId}`);

  socket.on('chat:send', async (data) => {
    const message = await messageService.create({ ...data, userId });
    io.to(data.room).emit('chat:message', message);
  });

  socket.on('disconnect', () => {
    console.log(`User ${userId} disconnected`);
  });
});
```

| 特性 | 原生 WebSocket | Socket.IO |
|------|---------------|-----------|
| **協議** | WebSocket 標準 | WebSocket + Polling 降級 |
| **房間** | 需自行實作 | 內建 |
| **重連** | 需自行實作 | 自動 |
| **廣播** | 需自行實作 | 內建 |
| **二進位** | 支援 | 支援 |

---

### 10.9 API 錯誤碼體系設計

```typescript
// 統一錯誤碼體系
const ERROR_CODES = {
  // 認證錯誤 (1xxx)
  AUTH_TOKEN_EXPIRED: { code: 'E1001', httpStatus: 401, message: 'Token has expired' },
  AUTH_TOKEN_INVALID: { code: 'E1002', httpStatus: 401, message: 'Invalid token' },
  AUTH_INSUFFICIENT_PERMISSIONS: { code: 'E1003', httpStatus: 403, message: 'Insufficient permissions' },
  AUTH_ACCOUNT_LOCKED: { code: 'E1004', httpStatus: 403, message: 'Account is locked' },

  // 驗證錯誤 (2xxx)
  VALIDATION_FAILED: { code: 'E2001', httpStatus: 400, message: 'Validation failed' },
  VALIDATION_MISSING_FIELD: { code: 'E2002', httpStatus: 400, message: 'Required field is missing' },
  VALIDATION_INVALID_FORMAT: { code: 'E2003', httpStatus: 400, message: 'Invalid field format' },

  // 資源錯誤 (3xxx)
  RESOURCE_NOT_FOUND: { code: 'E3001', httpStatus: 404, message: 'Resource not found' },
  RESOURCE_ALREADY_EXISTS: { code: 'E3002', httpStatus: 409, message: 'Resource already exists' },
  RESOURCE_GONE: { code: 'E3003', httpStatus: 410, message: 'Resource no longer available' },

  // 業務邏輯錯誤 (4xxx)
  ORDER_INSUFFICIENT_STOCK: { code: 'E4001', httpStatus: 422, message: 'Insufficient stock' },
  ORDER_ALREADY_CANCELLED: { code: 'E4002', httpStatus: 422, message: 'Order already cancelled' },
  PAYMENT_FAILED: { code: 'E4003', httpStatus: 422, message: 'Payment processing failed' },

  // 系統錯誤 (5xxx)
  INTERNAL_ERROR: { code: 'E5001', httpStatus: 500, message: 'Internal server error' },
  SERVICE_UNAVAILABLE: { code: 'E5002', httpStatus: 503, message: 'Service temporarily unavailable' },
  RATE_LIMIT_EXCEEDED: { code: 'E5003', httpStatus: 429, message: 'Rate limit exceeded' },
} as const;

// 錯誤回應格式
interface ErrorResponse {
  error: {
    code: string;           // 'E1001'
    message: string;        // 使用者可讀訊息
    details?: unknown[];    // 驗證細節等
    traceId: string;        // 追蹤 ID
    timestamp: string;      // ISO 時間
    path: string;           // API 路徑
  };
}

// 使用範例
class AppError extends Error {
  constructor(
    public readonly errorDef: typeof ERROR_CODES[keyof typeof ERROR_CODES],
    public readonly details?: unknown[],
  ) {
    super(errorDef.message);
    this.name = 'AppError';
  }
}

throw new AppError(ERROR_CODES.ORDER_INSUFFICIENT_STOCK, [
  { productId: 'P001', requested: 10, available: 3 },
]);
```

---

### 10.10 API 限流與配額設計

```typescript
// 多層級 Rate Limiting
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

// 全域限制：每分鐘 100 次
const globalLimiter = rateLimit({
  store: new RedisStore({ sendCommand: (...args) => redis.call(...args) }),
  windowMs: 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
});

// API Key 限制：依方案不同
const apiKeyLimiter = rateLimit({
  store: new RedisStore({ sendCommand: (...args) => redis.call(...args) }),
  windowMs: 60 * 60 * 1000,  // 每小時
  max: async (req) => {
    const plan = await getPlanByApiKey(req.headers['x-api-key'] as string);
    return plan === 'enterprise' ? 10000 : plan === 'pro' ? 1000 : 100;
  },
  keyGenerator: (req) => req.headers['x-api-key'] as string,
});

// 回應中包含限流資訊
// X-RateLimit-Limit: 100
// X-RateLimit-Remaining: 95
// X-RateLimit-Reset: 1625097600
```

---

## 第 11 章：資料庫整合

### 11.1 PostgreSQL 整合

#### 使用 pg 原生驅動

```typescript
import pg from 'pg';

const pool = new pg.Pool({
  host: process.env.DB_HOST,
  port: parseInt(process.env.DB_PORT ?? '5432'),
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  max: 20,                    // 連線池大小
  idleTimeoutMillis: 30000,   // 閒置逾時
  connectionTimeoutMillis: 5000,
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: true } : false,
});

// 查詢（參數化防止 SQL Injection）
const result = await pool.query(
  'SELECT * FROM users WHERE email = $1 AND active = $2',
  [email, true]
);

// Transaction
const client = await pool.connect();
try {
  await client.query('BEGIN');
  await client.query('INSERT INTO orders (user_id, total) VALUES ($1, $2)', [userId, total]);
  await client.query('UPDATE inventory SET quantity = quantity - $1 WHERE product_id = $2', [qty, productId]);
  await client.query('COMMIT');
} catch (err) {
  await client.query('ROLLBACK');
  throw err;
} finally {
  client.release();
}
```

---

### 11.2 MySQL 整合

```typescript
import mysql from 'mysql2/promise';

const pool = mysql.createPool({
  host: process.env.MYSQL_HOST,
  port: parseInt(process.env.MYSQL_PORT ?? '3306'),
  database: process.env.MYSQL_DB,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  waitForConnections: true,
  connectionLimit: 20,
  queueLimit: 0,
});

// 查詢
const [rows] = await pool.execute('SELECT * FROM users WHERE id = ?', [userId]);

// Transaction
const conn = await pool.getConnection();
try {
  await conn.beginTransaction();
  await conn.execute('INSERT INTO orders (user_id) VALUES (?)', [userId]);
  await conn.execute('UPDATE products SET stock = stock - ? WHERE id = ?', [qty, productId]);
  await conn.commit();
} catch (err) {
  await conn.rollback();
  throw err;
} finally {
  conn.release();
}
```

---

### 11.3 MongoDB 整合

```typescript
import { MongoClient, ObjectId } from 'mongodb';

const client = new MongoClient(process.env.MONGODB_URI!, {
  maxPoolSize: 20,
  minPoolSize: 5,
  serverSelectionTimeoutMS: 5000,
});

await client.connect();
const db = client.db('myapp');
const users = db.collection<User>('users');

// CRUD
await users.insertOne({ name: 'Alice', email: 'alice@example.com', createdAt: new Date() });
const user = await users.findOne({ _id: new ObjectId(userId) });
await users.updateOne({ _id: new ObjectId(userId) }, { $set: { name: 'Bob' } });
await users.deleteOne({ _id: new ObjectId(userId) });

// 聚合查詢
const stats = await users.aggregate([
  { $group: { _id: '$role', count: { $sum: 1 } } },
  { $sort: { count: -1 } },
]).toArray();

// 索引
await users.createIndex({ email: 1 }, { unique: true });
await users.createIndex({ name: 'text' });
```

---

### 11.4 Redis 快取整合

```typescript
import Redis from 'ioredis';

const redis = new Redis({
  host: process.env.REDIS_HOST ?? 'localhost',
  port: parseInt(process.env.REDIS_PORT ?? '6379'),
  password: process.env.REDIS_PASSWORD,
  maxRetriesPerRequest: 3,
  retryStrategy: (times) => Math.min(times * 200, 5000),
});

// 基本操作
await redis.set('user:123', JSON.stringify(user), 'EX', 3600);
const cached = await redis.get('user:123');
if (cached) return JSON.parse(cached);

// Cache-aside Pattern
async function getUserWithCache(id: string): Promise<User> {
  const cacheKey = `user:${id}`;
  const cached = await redis.get(cacheKey);
  
  if (cached) {
    return JSON.parse(cached);
  }
  
  const user = await prisma.user.findUnique({ where: { id } });
  if (user) {
    await redis.setex(cacheKey, 3600, JSON.stringify(user));
  }
  return user!;
}

// 快取失效
async function invalidateUserCache(id: string) {
  await redis.del(`user:${id}`);
  await redis.del(`user-list:*`);  // 使用 pattern（注意效能）
}

// 分散式鎖
async function acquireLock(key: string, ttl = 10000): Promise<boolean> {
  const result = await redis.set(`lock:${key}`, '1', 'PX', ttl, 'NX');
  return result === 'OK';
}
```

---

### 11.5 Prisma ORM

#### Schema 定義

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(uuid())
  name      String
  email     String   @unique
  role      Role     @default(USER)
  orders    Order[]
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")

  @@map("users")
  @@index([email])
}

model Order {
  id        String      @id @default(uuid())
  userId    String      @map("user_id")
  user      User        @relation(fields: [userId], references: [id])
  items     OrderItem[]
  total     Decimal     @db.Decimal(10, 2)
  status    OrderStatus @default(PENDING)
  createdAt DateTime    @default(now()) @map("created_at")

  @@map("orders")
  @@index([userId])
}

enum Role {
  ADMIN
  USER
  VIEWER
}

enum OrderStatus {
  PENDING
  PAID
  SHIPPED
  DELIVERED
  CANCELLED
}
```

#### 使用 Prisma Client

```typescript
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

// CRUD
const user = await prisma.user.create({
  data: { name: 'Alice', email: 'alice@example.com' },
});

const users = await prisma.user.findMany({
  where: { role: 'USER' },
  include: { orders: { where: { status: 'PAID' } } },
  orderBy: { createdAt: 'desc' },
  take: 20,
  skip: 0,
});

// Transaction（互動式）
const result = await prisma.$transaction(async (tx) => {
  const order = await tx.order.create({
    data: { userId, total, items: { create: items } },
  });
  await tx.user.update({
    where: { id: userId },
    data: { orderCount: { increment: 1 } },
  });
  return order;
});
```

#### Prisma 指令

```bash
# 建立 Migration
npx prisma migrate dev --name add_user_table

# 部署 Migration（生產環境）
npx prisma migrate deploy

# 產生 Client
npx prisma generate

# 資料庫檢視工具
npx prisma studio
```

---

### 11.6 TypeORM

```typescript
import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, OneToMany } from 'typeorm';

@Entity('users')
export class UserEntity {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ length: 100 })
  name: string;

  @Column({ unique: true })
  email: string;

  @Column({ type: 'enum', enum: ['admin', 'user', 'viewer'], default: 'user' })
  role: string;

  @OneToMany(() => OrderEntity, order => order.user)
  orders: OrderEntity[];

  @CreateDateColumn({ name: 'created_at' })
  createdAt: Date;
}

// Repository 使用
const userRepo = dataSource.getRepository(UserEntity);
const users = await userRepo.find({
  where: { role: 'user' },
  relations: { orders: true },
  order: { createdAt: 'DESC' },
  take: 20,
});
```

---

### 11.7 Transaction、Migration 與連線池

#### ORM 比較

| 特性 | Prisma | TypeORM | Drizzle |
|------|--------|---------|---------|
| **設計理念** | Schema-first | Entity-first | SQL-first |
| **型別安全** | 極高（自動產生） | 高 | 極高 |
| **效能** | 中 | 中低 | 高 |
| **學習曲線** | 低 | 中 | 低 |
| **Migration** | 內建 | 內建 | 內建 |
| **Raw SQL** | 支援 | 支援 | 原生 |

#### 連線池設計

```mermaid
graph TD
    A[應用程式] --> B[Connection Pool]
    B --> C[Connection 1]
    B --> D[Connection 2]
    B --> E[Connection N]
    C --> F[(Database)]
    D --> F
    E --> F
```

> **✅ 企業建議**：
> - 新專案推薦 **Prisma**（型別安全、開發體驗好）
> - 效能敏感場景考慮 **Drizzle**（更接近 SQL）
> - 連線池大小 = CPU 核心數 × 2 + 磁碟數

#### 章節小練習

1. 使用 Prisma 建立一套包含關聯的 Schema。
2. 實作 Cache-aside Pattern（Redis + PostgreSQL）。
3. 實作互動式 Transaction（Prisma）。

#### 實務注意事項

> - 永遠使用參數化查詢，防止 SQL Injection
> - 設定適當的連線池大小
> - Redis 設定 TTL 避免記憶體爆滿
> - Migration 必須提交到版本控制
> - 生產環境使用 `prisma migrate deploy`（非 `dev`）

### 11.8 Prisma 進階查詢模式

```typescript
// 1. Cursor-based Pagination（效能優於 offset）
async function findUsers(cursor?: string, take = 20) {
  return prisma.user.findMany({
    take: take + 1,  // 多取一筆判斷是否有下一頁
    ...(cursor ? { cursor: { id: cursor }, skip: 1 } : {}),
    orderBy: { createdAt: 'desc' },
    select: {
      id: true,
      name: true,
      email: true,
      createdAt: true,
      _count: { select: { orders: true } },
    },
  });
}

// 2. Soft Delete 中間件
prisma.$use(async (params, next) => {
  // Find 查詢自動過濾已刪除記錄
  if (params.action === 'findMany' || params.action === 'findFirst') {
    if (!params.args) params.args = {};
    if (!params.args.where) params.args.where = {};
    if (params.args.where.deletedAt === undefined) {
      params.args.where.deletedAt = null;
    }
  }

  // Delete 改為 Soft Delete
  if (params.action === 'delete') {
    params.action = 'update';
    params.args.data = { deletedAt: new Date() };
  }
  if (params.action === 'deleteMany') {
    params.action = 'updateMany';
    if (!params.args.data) params.args.data = {};
    params.args.data.deletedAt = new Date();
  }

  return next(params);
});

// 3. Raw Query（複雜聚合）
const salesReport = await prisma.$queryRaw<SalesReport[]>`
  SELECT
    DATE_TRUNC('month', o."createdAt") AS month,
    COUNT(*)::int AS order_count,
    SUM(o.total)::numeric AS revenue,
    AVG(o.total)::numeric AS avg_order_value
  FROM orders o
  WHERE o.status = 'COMPLETED'
    AND o."createdAt" >= ${startDate}
  GROUP BY DATE_TRUNC('month', o."createdAt")
  ORDER BY month DESC
`;

// 4. 樂觀鎖定（Optimistic Locking）
async function updateProduct(id: string, data: UpdateProductDto, version: number) {
  const result = await prisma.product.updateMany({
    where: { id, version },
    data: { ...data, version: { increment: 1 } },
  });

  if (result.count === 0) {
    throw new ConflictException('Record was modified by another user');
  }

  return prisma.product.findUnique({ where: { id } });
}
```

---

### 11.9 Redis 進階模式

```typescript
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

// 1. 分散式鎖（Redlock）
import Redlock from 'redlock';

const redlock = new Redlock([redis], {
  retryCount: 3,
  retryDelay: 200,
  retryJitter: 200,
});

async function processPayment(orderId: string) {
  const lock = await redlock.acquire([`lock:order:${orderId}`], 10_000);
  try {
    // 確保同一訂單不會被重複處理
    const order = await getOrder(orderId);
    if (order.status !== 'PENDING') return;
    
    await chargePayment(order);
    await updateOrderStatus(orderId, 'PAID');
  } finally {
    await lock.release();
  }
}

// 2. 排行榜（Sorted Set）
async function updateLeaderboard(userId: string, score: number) {
  await redis.zadd('leaderboard:daily', score, userId);
}

async function getTopUsers(limit = 10) {
  const results = await redis.zrevrange('leaderboard:daily', 0, limit - 1, 'WITHSCORES');
  const users: { userId: string; score: number }[] = [];
  for (let i = 0; i < results.length; i += 2) {
    users.push({ userId: results[i], score: Number(results[i + 1]) });
  }
  return users;
}

// 3. Rate Limiter（Sliding Window）
async function slidingWindowRateLimit(key: string, limit: number, windowSec: number): Promise<boolean> {
  const now = Date.now();
  const windowStart = now - windowSec * 1000;

  const multi = redis.multi();
  multi.zremrangebyscore(key, 0, windowStart);   // 移除過期記錄
  multi.zadd(key, now, `${now}:${Math.random()}`);  // 新增本次請求
  multi.zcard(key);                                   // 計算視窗內數量
  multi.expire(key, windowSec);                       // 設定過期

  const results = await multi.exec();
  const count = results![2][1] as number;

  return count <= limit;
}

// 4. Pub/Sub 即時通知
const subscriber = redis.duplicate();

subscriber.subscribe('order:events', (err) => {
  if (err) throw err;
});

subscriber.on('message', (channel, message) => {
  const event = JSON.parse(message);
  switch (event.type) {
    case 'order.created':
      notifyWarehouse(event.data);
      break;
    case 'order.shipped':
      notifyCustomer(event.data);
      break;
  }
});

// 發佈事件
async function publishOrderEvent(type: string, data: unknown) {
  await redis.publish('order:events', JSON.stringify({ type, data, timestamp: Date.now() }));
}
```

---

## 第 12 章：測試

### 12.1 Node.js 內建 Test Runner（node:test）

```typescript
// tests/user.test.ts
import { describe, it, before, after, mock } from 'node:test';
import assert from 'node:assert/strict';

describe('UserService', () => {
  let service: UserService;

  before(() => {
    service = new UserService(mockPrisma);
  });

  it('should create a user', async () => {
    const user = await service.create({ name: 'Alice', email: 'alice@test.com' });
    assert.equal(user.name, 'Alice');
    assert.equal(user.email, 'alice@test.com');
  });

  it('should throw on duplicate email', async () => {
    await assert.rejects(
      () => service.create({ name: 'Bob', email: 'alice@test.com' }),
      { name: 'ConflictException' }
    );
  });

  it('should return null for non-existent user', async () => {
    const user = await service.findById('non-existent-id');
    assert.equal(user, null);
  });
});

// 執行
// node --test tests/**/*.test.ts
```

> **✅ 優勢**：零依賴、原生支援、速度極快。適合簡單專案和工具。

---

### 12.2 Jest 測試框架

```typescript
// jest.config.ts
import type { Config } from 'jest';

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  testMatch: ['**/*.spec.ts', '**/*.test.ts'],
  coverageDirectory: 'coverage',
  coverageThreshold: {
    global: { branches: 80, functions: 80, lines: 80, statements: 80 },
  },
};

export default config;
```

```typescript
// tests/user.service.spec.ts
describe('UserService', () => {
  let service: UserService;
  let mockRepo: jest.Mocked<UserRepository>;

  beforeEach(() => {
    mockRepo = {
      findById: jest.fn(),
      create: jest.fn(),
      update: jest.fn(),
      delete: jest.fn(),
    } as any;
    service = new UserService(mockRepo);
  });

  describe('findById', () => {
    it('should return user when found', async () => {
      const mockUser = { id: '1', name: 'Alice', email: 'alice@test.com' };
      mockRepo.findById.mockResolvedValue(mockUser);

      const result = await service.findById('1');

      expect(result).toEqual(mockUser);
      expect(mockRepo.findById).toHaveBeenCalledWith('1');
    });

    it('should throw NotFoundException when not found', async () => {
      mockRepo.findById.mockResolvedValue(null);

      await expect(service.findById('999')).rejects.toThrow(NotFoundException);
    });
  });
});
```

---

### 12.3 Vitest 測試框架

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['src/**/*.{test,spec}.ts', 'tests/**/*.{test,spec}.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      thresholds: { branches: 80, functions: 80, lines: 80 },
    },
  },
});
```

```typescript
// tests/user.service.spec.ts
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('UserService', () => {
  let service: UserService;
  let mockRepo: any;

  beforeEach(() => {
    mockRepo = {
      findById: vi.fn(),
      create: vi.fn(),
    };
    service = new UserService(mockRepo);
  });

  it('should create user', async () => {
    const dto = { name: 'Alice', email: 'alice@test.com' };
    mockRepo.create.mockResolvedValue({ id: '1', ...dto });

    const result = await service.create(dto);

    expect(result.id).toBe('1');
    expect(mockRepo.create).toHaveBeenCalledOnce();
  });
});
```

> **✅ 推薦 Vitest**：與 Vite 生態整合、ESM 原生支援、API 相容 Jest、速度更快。

---

### 12.4 Supertest 整合測試

```typescript
import request from 'supertest';
import { app } from '../src/app.js';

describe('User API Integration', () => {
  let authToken: string;

  beforeAll(async () => {
    // 取得測試用 Token
    const res = await request(app)
      .post('/api/v1/auth/login')
      .send({ email: 'admin@test.com', password: 'password' });
    authToken = res.body.accessToken;
  });

  describe('POST /api/v1/users', () => {
    it('should create a user', async () => {
      const res = await request(app)
        .post('/api/v1/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ name: 'Test User', email: 'test@example.com', password: 'Test1234' })
        .expect(201);

      expect(res.body).toHaveProperty('id');
      expect(res.body.name).toBe('Test User');
    });

    it('should return 400 for invalid email', async () => {
      const res = await request(app)
        .post('/api/v1/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ name: 'Test', email: 'invalid', password: 'Test1234' })
        .expect(400);

      expect(res.body.error.code).toBe('VALIDATION_ERROR');
    });

    it('should return 401 without token', async () => {
      await request(app)
        .post('/api/v1/users')
        .send({ name: 'Test', email: 'test@example.com' })
        .expect(401);
    });
  });
});
```

---

### 12.5 Playwright E2E 測試

```typescript
// e2e/user-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('User Registration Flow', () => {
  test('should register a new user', async ({ page }) => {
    await page.goto('/register');
    
    await page.fill('[name="name"]', 'Test User');
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'Test1234!');
    await page.click('button[type="submit"]');
    
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('.welcome-message')).toContainText('Welcome, Test User');
  });

  test('should show validation errors', async ({ page }) => {
    await page.goto('/register');
    await page.click('button[type="submit"]');
    
    await expect(page.locator('.error-message')).toBeVisible();
  });
});
```

---

### 12.6 Test Pyramid 與測試策略

```mermaid
graph TD
    A[E2E Tests<br/>少量 ~5%] --> B[Integration Tests<br/>中量 ~20%]
    B --> C[Unit Tests<br/>大量 ~75%]
    
    style A fill:#ff6b6b,color:white
    style B fill:#ffd93d,color:black
    style C fill:#6bcb77,color:white
```

| 測試層級 | 數量 | 速度 | 信心度 | 工具 |
|----------|------|------|--------|------|
| **Unit** | 最多 | 極快 | 低 | Vitest, Jest |
| **Integration** | 中等 | 中 | 中高 | Supertest, TestContainers |
| **E2E** | 最少 | 慢 | 最高 | Playwright, Cypress |

---

### 12.7 Mock / Stub / Spy 使用時機

| 手法 | 定義 | 使用時機 |
|------|------|----------|
| **Mock** | 完全替換依賴 | 外部 API、Email 服務 |
| **Stub** | 回傳固定值 | 資料庫查詢結果 |
| **Spy** | 監聽但不改變行為 | 確認方法是否被呼叫 |

```typescript
// Vitest 範例
import { vi } from 'vitest';

// Mock
const mockEmailService = {
  send: vi.fn().mockResolvedValue({ success: true }),
};

// Spy
const spy = vi.spyOn(userService, 'findById');
await controller.getUser('123');
expect(spy).toHaveBeenCalledWith('123');
```

---

### 12.8 Coverage 工具（c8 / istanbul）

```bash
# 使用 c8（V8 內建 Coverage）
npx c8 node --test tests/**/*.test.ts
npx c8 report --reporter=html

# Vitest 內建 Coverage
npx vitest --coverage

# 設定 Coverage 閾值
# vitest.config.ts 中設定 thresholds
```

#### 章節小練習

1. 使用 Vitest 撰寫 Service 的 Unit Test（含 Mock）。
2. 使用 Supertest 撰寫 API Integration Test。
3. 設定 Coverage 閾值達到 80%。

#### 實務注意事項

> - 新專案推薦 Vitest（快速、ESM 原生）
> - 測試覆蓋率目標：80%（不追求 100%）
> - 外部依賴（API、DB、Email）一律 Mock
> - 整合測試使用 TestContainers 建立真實環境
> - CI/CD 中必須包含測試步驟

### 12.9 Contract Testing（契約測試）

```typescript
// 使用 Pact 進行消費者驅動契約測試

// 消費者端（前端 / API 消費者）
import { PactV4, MatchersV3 } from '@pact-foundation/pact';

const { like, eachLike, string, integer } = MatchersV3;

const provider = new PactV4({
  consumer: 'frontend-app',
  provider: 'api-server',
  dir: './pacts',
});

describe('User API Contract', () => {
  it('should return user by id', async () => {
    await provider
      .addInteraction()
      .given('user with id 1 exists')
      .uponReceiving('a request for user 1')
      .withRequest('GET', '/api/v1/users/1', (builder) => {
        builder.headers({ Authorization: string('Bearer token') });
      })
      .willRespondWith(200, (builder) => {
        builder.headers({ 'Content-Type': 'application/json' });
        builder.jsonBody({
          id: string('1'),
          name: string('John'),
          email: string('john@example.com'),
          createdAt: string('2024-01-01T00:00:00Z'),
          orders: eachLike({
            id: string('order-1'),
            total: integer(100),
          }),
        });
      })
      .executeTest(async (mockserver) => {
        const client = new ApiClient(mockserver.url);
        const user = await client.getUser('1');
        
        expect(user.name).toBe('John');
        expect(user.orders).toHaveLength(1);
      });
  });
});

// 提供者端驗證
import { Verifier } from '@pact-foundation/pact';

describe('Provider Verification', () => {
  it('should fulfill consumer contracts', async () => {
    const verifier = new Verifier({
      providerBaseUrl: 'http://localhost:3000',
      pactUrls: ['./pacts/frontend-app-api-server.json'],
      stateHandlers: {
        'user with id 1 exists': async () => {
          await prisma.user.create({
            data: { id: '1', name: 'John', email: 'john@example.com' },
          });
        },
      },
    });

    await verifier.verifyProvider();
  });
});
```

---

### 12.10 測試資料管理

```typescript
// test/factories/user.factory.ts
import { faker } from '@faker-js/faker/locale/zh_TW';

interface UserOverrides {
  name?: string;
  email?: string;
  role?: 'USER' | 'ADMIN';
}

export function buildUser(overrides: UserOverrides = {}) {
  return {
    id: faker.string.uuid(),
    name: overrides.name ?? faker.person.fullName(),
    email: overrides.email ?? faker.internet.email(),
    role: overrides.role ?? 'USER',
    createdAt: faker.date.past(),
    updatedAt: new Date(),
  };
}

export function buildUsers(count: number, overrides: UserOverrides = {}) {
  return Array.from({ length: count }, () => buildUser(overrides));
}

// test/factories/order.factory.ts
export function buildOrder(overrides: Partial<Order> = {}) {
  return {
    id: faker.string.uuid(),
    userId: faker.string.uuid(),
    status: 'PENDING' as const,
    total: faker.number.int({ min: 100, max: 10000 }),
    items: [
      {
        productId: faker.string.uuid(),
        quantity: faker.number.int({ min: 1, max: 5 }),
        price: faker.number.int({ min: 50, max: 500 }),
      },
    ],
    createdAt: faker.date.past(),
    ...overrides,
  };
}

// test/helpers/db.ts — 測試資料庫管理
import { PrismaClient } from '@prisma/client';
import { execSync } from 'node:child_process';

const prisma = new PrismaClient();

export async function resetDatabase() {
  // 依照外鍵順序清除資料
  const tables = ['OrderItem', 'Order', 'Product', 'User'];
  for (const table of tables) {
    await prisma.$executeRawUnsafe(`TRUNCATE TABLE "${table}" CASCADE`);
  }
}

export async function seedTestData() {
  await prisma.user.createMany({
    data: buildUsers(5),
  });
}

// vitest.setup.ts
beforeAll(async () => {
  await resetDatabase();
  await seedTestData();
});

afterAll(async () => {
  await prisma.$disconnect();
});
```

---

### 12.11 Snapshot Testing

```typescript
// API Response Snapshot
import { describe, it, expect } from 'vitest';
import request from 'supertest';

describe('API Snapshots', () => {
  it('should match user response shape', async () => {
    const res = await request(app)
      .get('/api/v1/users/1')
      .set('Authorization', `Bearer ${token}`)
      .expect(200);

    // Inline Snapshot — 自動更新
    expect(res.body).toMatchInlineSnapshot(`
      {
        "id": "1",
        "name": "John",
        "email": "john@example.com",
        "role": "USER",
        "createdAt": Any<String>,
        "orders": Any<Array>,
      }
    `);
  });

  // 錯誤回應 Snapshot
  it('should match 404 error shape', async () => {
    const res = await request(app)
      .get('/api/v1/users/nonexistent')
      .set('Authorization', `Bearer ${token}`)
      .expect(404);

    expect(res.body).toMatchSnapshot({
      error: {
        code: 'NOT_FOUND',
        message: expect.any(String),
      },
    });
  });
});
```

---

## 第 13 章：專案架構設計

### 13.1 Clean Architecture 應用

```mermaid
graph TD
    subgraph "外層 - Framework & Drivers"
        A[Express / Fastify / NestJS]
        B[Prisma / TypeORM]
        C[Redis Client]
    end
    
    subgraph "中層 - Interface Adapters"
        D[Controllers]
        E[Repositories Implementation]
        F[Presenters / DTOs]
    end
    
    subgraph "內層 - Application Business Rules"
        G[Use Cases]
        H[Application Services]
    end
    
    subgraph "核心 - Enterprise Business Rules"
        I[Entities]
        J[Value Objects]
        K[Domain Events]
    end
    
    A --> D
    D --> G
    G --> I
    B --> E
    E --> G
```

#### 目錄結構

```
src/
├── domain/                  # 核心業務邏輯（無任何外部依賴）
│   ├── entities/
│   │   └── user.entity.ts
│   ├── value-objects/
│   │   └── email.vo.ts
│   ├── repositories/
│   │   └── user.repository.ts   # 介面定義
│   └── events/
│       └── user-created.event.ts
├── application/             # 應用邏輯
│   ├── use-cases/
│   │   ├── create-user.use-case.ts
│   │   └── get-user.use-case.ts
│   └── dto/
│       └── create-user.dto.ts
├── infrastructure/          # 外部依賴實作
│   ├── persistence/
│   │   └── prisma-user.repository.ts
│   ├── cache/
│   │   └── redis-cache.service.ts
│   └── external/
│       └── email.service.ts
└── presentation/            # 進入點
    ├── http/
    │   ├── controllers/
    │   └── middleware/
    └── main.ts
```

---

### 13.2 Hexagonal Architecture 應用

```mermaid
graph LR
    subgraph "外部"
        A[HTTP Client]
        B[CLI]
        C[Message Queue]
    end
    
    subgraph "Ports (Input)"
        D[HTTP Port]
        E[CLI Port]
        F[Event Port]
    end
    
    subgraph "Application Core"
        G[Use Cases]
        H[Domain Model]
    end
    
    subgraph "Ports (Output)"
        I[DB Port]
        J[Cache Port]
        K[Email Port]
    end
    
    subgraph "Adapters"
        L[(PostgreSQL)]
        M[(Redis)]
        N[SMTP Server]
    end
    
    A --> D --> G
    B --> E --> G
    C --> F --> G
    G --> I --> L
    G --> J --> M
    G --> K --> N
```

```typescript
// 定義 Port（介面）
interface UserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<User>;
  delete(id: string): Promise<void>;
}

// Adapter 實作
class PrismaUserRepository implements UserRepository {
  constructor(private readonly prisma: PrismaClient) {}

  async findById(id: string): Promise<User | null> {
    const data = await this.prisma.user.findUnique({ where: { id } });
    return data ? User.fromPersistence(data) : null;
  }

  async save(user: User): Promise<User> {
    const data = await this.prisma.user.upsert({
      where: { id: user.id },
      create: user.toPersistence(),
      update: user.toPersistence(),
    });
    return User.fromPersistence(data);
  }

  async delete(id: string): Promise<void> {
    await this.prisma.user.delete({ where: { id } });
  }
}
```

---

### 13.3 Domain-Driven Design（DDD）實作

```typescript
// Value Object
class Email {
  private constructor(private readonly value: string) {}

  static create(email: string): Email {
    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      throw new Error('Invalid email format');
    }
    return new Email(email.toLowerCase());
  }

  equals(other: Email): boolean {
    return this.value === other.value;
  }

  toString(): string {
    return this.value;
  }
}

// Entity
class User {
  private constructor(
    public readonly id: string,
    private _name: string,
    private _email: Email,
    private _role: UserRole,
    private _events: DomainEvent[] = [],
  ) {}

  static create(name: string, email: string): User {
    const user = new User(
      crypto.randomUUID(),
      name,
      Email.create(email),
      UserRole.USER,
    );
    user.addEvent(new UserCreatedEvent(user.id, email));
    return user;
  }

  changeName(name: string): void {
    if (name.length < 1 || name.length > 100) {
      throw new Error('Name must be 1-100 characters');
    }
    this._name = name;
  }

  private addEvent(event: DomainEvent): void {
    this._events.push(event);
  }

  pullEvents(): DomainEvent[] {
    const events = [...this._events];
    this._events = [];
    return events;
  }
}

// Aggregate Root
class Order {
  private items: OrderItem[] = [];
  
  addItem(product: Product, quantity: number): void {
    if (quantity <= 0) throw new Error('Quantity must be positive');
    if (this.status !== OrderStatus.DRAFT) throw new Error('Cannot modify non-draft order');
    
    const existing = this.items.find(i => i.productId === product.id);
    if (existing) {
      existing.updateQuantity(existing.quantity + quantity);
    } else {
      this.items.push(OrderItem.create(product, quantity));
    }
  }
}
```

---

### 13.4 Monorepo 策略（Turborepo / Nx / pnpm workspace）

#### Turborepo 範例

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"]
    },
    "lint": {},
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

```
// Monorepo 結構
monorepo/
├── apps/
│   ├── api/              # NestJS API
│   ├── web/              # Next.js 前端
│   └── admin/            # Vue 管理後台
├── packages/
│   ├── shared/           # 共用型別、工具
│   ├── database/         # Prisma Schema & Client
│   ├── config/           # 共用設定
│   └── ui/               # 共用 UI 元件
├── turbo.json
├── pnpm-workspace.yaml
└── package.json
```

---

### 13.5 微服務架構設計

```mermaid
graph TD
    A[API Gateway] --> B[User Service]
    A --> C[Order Service]
    A --> D[Payment Service]
    A --> E[Notification Service]
    
    B --> F[(User DB)]
    C --> G[(Order DB)]
    D --> H[(Payment DB)]
    
    C --> I[Message Queue]
    I --> D
    I --> E
    
    B -.->|gRPC| C
```

| 通訊方式 | 同步/非同步 | 適用場景 |
|----------|------------|----------|
| **REST** | 同步 | 標準 API 呼叫 |
| **gRPC** | 同步 | 微服務間高效能通訊 |
| **Message Queue** | 非同步 | 事件驅動、解耦 |
| **Event Sourcing** | 非同步 | 需要完整事件歷史 |

#### 章節小練習

1. 使用 Clean Architecture 設計一個 User 模組。
2. 建立 Turborepo Monorepo 結構。
3. 實作 Domain Event 發佈/訂閱機制。

#### 實務注意事項

> - 小型專案不要過度架構（KISS 原則）
> - 大型專案考慮 Hexagonal/Clean Architecture
> - Monorepo 推薦 Turborepo + pnpm workspace
> - 微服務適合大型團隊，小團隊用 Modular Monolith
> - DDD 只在複雜業務邏輯中使用

### 13.6 Error Handling 架構

```typescript
// 統一錯誤處理架構

// 1. 自定義錯誤類別階層
abstract class AppError extends Error {
  abstract readonly statusCode: number;
  abstract readonly errorCode: string;
  readonly isOperational = true;

  constructor(
    message: string,
    readonly details?: Record<string, unknown>,
  ) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }

  toJSON() {
    return {
      error: {
        code: this.errorCode,
        message: this.message,
        ...(this.details && { details: this.details }),
      },
    };
  }
}

class NotFoundError extends AppError {
  readonly statusCode = 404;
  readonly errorCode = 'NOT_FOUND';
  constructor(resource: string, id: string) {
    super(`${resource} with id '${id}' not found`, { resource, id });
  }
}

class ValidationError extends AppError {
  readonly statusCode = 400;
  readonly errorCode = 'VALIDATION_ERROR';
  constructor(errors: Array<{ field: string; message: string }>) {
    super('Validation failed', { errors });
  }
}

class ConflictError extends AppError {
  readonly statusCode = 409;
  readonly errorCode = 'CONFLICT';
}

class UnauthorizedError extends AppError {
  readonly statusCode = 401;
  readonly errorCode = 'UNAUTHORIZED';
  constructor(message = 'Authentication required') {
    super(message);
  }
}

class ForbiddenError extends AppError {
  readonly statusCode = 403;
  readonly errorCode = 'FORBIDDEN';
  constructor(message = 'Access denied') {
    super(message);
  }
}

class RateLimitError extends AppError {
  readonly statusCode = 429;
  readonly errorCode = 'RATE_LIMIT_EXCEEDED';
  constructor(retryAfter: number) {
    super('Too many requests', { retryAfter });
  }
}

// 2. 全域錯誤處理中間件（Express）
function errorHandler(err: Error, req: Request, res: Response, _next: NextFunction) {
  // 結構化日誌
  const logPayload = {
    err,
    req: {
      method: req.method,
      url: req.url,
      headers: { 'x-request-id': req.headers['x-request-id'] },
    },
  };

  if (err instanceof AppError && err.isOperational) {
    // 預期錯誤：記錄 warn 等級
    logger.warn(logPayload, err.message);
    return res.status(err.statusCode).json(err.toJSON());
  }

  // 非預期錯誤：記錄 error 等級，不洩漏內部資訊
  logger.error(logPayload, 'Unexpected error');
  return res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred',
    },
  });
}

// 3. Async Error Wrapper
function asyncHandler(fn: (req: Request, res: Response, next: NextFunction) => Promise<void>) {
  return (req: Request, res: Response, next: NextFunction) => {
    fn(req, res, next).catch(next);
  };
}

// 使用方式
app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await userService.findById(req.params.id);
  if (!user) throw new NotFoundError('User', req.params.id);
  res.json(user);
}));
```

---

### 13.7 Configuration Management

```typescript
// 型別安全的設定管理

import { z } from 'zod';
import { config as loadDotenv } from 'dotenv';

// 依環境載入 .env 檔
loadDotenv({ path: `.env.${process.env.NODE_ENV ?? 'development'}` });

// Schema 定義
const configSchema = z.object({
  app: z.object({
    name: z.string().default('api-server'),
    port: z.coerce.number().default(3000),
    env: z.enum(['development', 'production', 'test']).default('development'),
    corsOrigins: z.string().transform(s => s.split(',')),
  }),
  database: z.object({
    url: z.string().url(),
    poolMin: z.coerce.number().default(2),
    poolMax: z.coerce.number().default(10),
    logQueries: z.coerce.boolean().default(false),
  }),
  redis: z.object({
    url: z.string().url(),
    keyPrefix: z.string().default('app:'),
    ttlDefault: z.coerce.number().default(300),
  }),
  auth: z.object({
    jwtSecret: z.string().min(32),
    jwtRefreshSecret: z.string().min(32),
    accessTokenExpiresIn: z.string().default('15m'),
    refreshTokenExpiresIn: z.string().default('7d'),
    bcryptRounds: z.coerce.number().default(12),
  }),
  logging: z.object({
    level: z.enum(['fatal', 'error', 'warn', 'info', 'debug', 'trace']).default('info'),
    pretty: z.coerce.boolean().default(false),
  }),
  monitoring: z.object({
    sentryDsn: z.string().url().optional(),
    otelEndpoint: z.string().url().optional(),
  }),
});

// 從環境變數映射
function loadConfig() {
  return configSchema.parse({
    app: {
      name: process.env.APP_NAME,
      port: process.env.PORT,
      env: process.env.NODE_ENV,
      corsOrigins: process.env.CORS_ORIGINS ?? 'http://localhost:3001',
    },
    database: {
      url: process.env.DATABASE_URL,
      poolMin: process.env.DB_POOL_MIN,
      poolMax: process.env.DB_POOL_MAX,
      logQueries: process.env.DB_LOG_QUERIES,
    },
    redis: {
      url: process.env.REDIS_URL,
      keyPrefix: process.env.REDIS_KEY_PREFIX,
      ttlDefault: process.env.REDIS_TTL_DEFAULT,
    },
    auth: {
      jwtSecret: process.env.JWT_SECRET,
      jwtRefreshSecret: process.env.JWT_REFRESH_SECRET,
      accessTokenExpiresIn: process.env.ACCESS_TOKEN_EXPIRES_IN,
      refreshTokenExpiresIn: process.env.REFRESH_TOKEN_EXPIRES_IN,
      bcryptRounds: process.env.BCRYPT_ROUNDS,
    },
    logging: {
      level: process.env.LOG_LEVEL,
      pretty: process.env.LOG_PRETTY,
    },
    monitoring: {
      sentryDsn: process.env.SENTRY_DSN,
      otelEndpoint: process.env.OTEL_EXPORTER_OTLP_ENDPOINT,
    },
  });
}

export type AppConfig = z.infer<typeof configSchema>;
export const appConfig: AppConfig = loadConfig();
```

---

## 第 14 章：前端整合

### 14.1 Vue 整合模式

```typescript
// API 層（前端）
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
});

// 請求攔截器
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// 回應攔截器
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response?.status === 401) {
      router.push('/login');
    }
    return Promise.reject(error);
  }
);

// Composable
export function useUsers() {
  const users = ref<User[]>([]);
  const loading = ref(false);

  async function fetchUsers() {
    loading.value = true;
    try {
      users.value = await api.get('/api/v1/users');
    } finally {
      loading.value = false;
    }
  }

  return { users, loading, fetchUsers };
}
```

---

### 14.2 React 整合模式

```typescript
// React + TanStack Query
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function useUsers() {
  return useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/v1/users').then(r => r.json()),
    staleTime: 5 * 60 * 1000,
  });
}

function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: CreateUserDto) =>
      fetch('/api/v1/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      }).then(r => r.json()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });
}
```

---

### 14.3 Next.js 全端框架

```typescript
// app/api/users/route.ts（Next.js App Router API Route）
import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const page = parseInt(searchParams.get('page') ?? '1');
  const limit = parseInt(searchParams.get('limit') ?? '20');

  const users = await prisma.user.findMany({
    skip: (page - 1) * limit,
    take: limit,
  });

  return NextResponse.json({ data: users });
}

export async function POST(request: NextRequest) {
  const body = await request.json();
  const user = await prisma.user.create({ data: body });
  return NextResponse.json(user, { status: 201 });
}
```

```typescript
// app/users/page.tsx（Server Component）
async function UsersPage() {
  const users = await prisma.user.findMany();

  return (
    <div>
      <h1>Users</h1>
      {users.map(user => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
}
```

---

### 14.4 Nuxt.js 全端框架

```typescript
// server/api/users.get.ts（Nuxt Server API）
export default defineEventHandler(async (event) => {
  const query = getQuery(event);
  const users = await prisma.user.findMany({
    take: Number(query.limit) || 20,
  });
  return { data: users };
});

// pages/users.vue（頁面元件）
<script setup lang="ts">
const { data: users, pending } = useFetch('/api/users');
</script>

<template>
  <div>
    <h1>Users</h1>
    <div v-if="pending">Loading...</div>
    <div v-else v-for="user in users?.data" :key="user.id">
      {{ user.name }}
    </div>
  </div>
</template>
```

---

### 14.5 Server-Side Rendering（SSR）架構

```mermaid
sequenceDiagram
    participant Browser
    participant Node.js Server
    participant API Server
    participant Database
    
    Browser->>Node.js Server: GET /users
    Node.js Server->>API Server: fetch /api/users
    API Server->>Database: SELECT * FROM users
    Database-->>API Server: users data
    API Server-->>Node.js Server: JSON response
    Node.js Server->>Node.js Server: Render HTML
    Node.js Server-->>Browser: Complete HTML + Hydration JS
    Browser->>Browser: Hydration（注入互動性）
```

| 渲染模式 | 說明 | 適用場景 |
|----------|------|----------|
| **CSR** | 客戶端渲染 | SPA、後台管理 |
| **SSR** | 伺服器端渲染 | SEO 需求、首屏效能 |
| **SSG** | 靜態網站產生 | 部落格、文件站 |
| **ISR** | 增量靜態再生成 | 電商產品頁 |

---

### 14.6 BFF（Backend for Frontend）設計模式

```mermaid
graph TD
    A[Mobile App] --> B[Mobile BFF]
    C[Web App] --> D[Web BFF]
    E[Admin Panel] --> F[Admin BFF]
    
    B --> G[User Service]
    B --> H[Order Service]
    D --> G
    D --> H
    D --> I[Product Service]
    F --> G
    F --> H
    F --> I
    F --> J[Analytics Service]
```

```typescript
// Web BFF — 聚合多個微服務
app.get('/bff/dashboard', authenticate, async (req, res) => {
  const userId = req.user.id;

  const [profile, recentOrders, notifications, stats] = await Promise.all([
    userService.getProfile(userId),
    orderService.getRecent(userId, 5),
    notificationService.getUnread(userId),
    analyticsService.getUserStats(userId),
  ]);

  // 轉換為前端需要的格式
  res.json({
    user: {
      name: profile.name,
      avatar: profile.avatarUrl,
    },
    recentOrders: recentOrders.map(o => ({
      id: o.id,
      status: o.status,
      total: formatCurrency(o.total),
    })),
    unreadCount: notifications.length,
    stats: {
      totalOrders: stats.orderCount,
      totalSpent: formatCurrency(stats.totalSpent),
    },
  });
});
```

#### 章節小練習

1. 使用 Next.js 建立一個包含 API Route 和 Server Component 的頁面。
2. 實作 BFF 端點，聚合三個微服務的資料。
3. 比較 CSR、SSR、SSG 的優缺點。

#### 實務注意事項

> - 全端框架（Next.js / Nuxt.js）適合前後端在同一團隊
> - 大型系統建議使用 BFF 分離前後端關注點
> - SSR 增加伺服器負擔，需要適當的快取策略
> - API 層使用 TanStack Query（React）或 composable（Vue）管理狀態

### 14.7 Server-Sent Events（SSE）即時推送

```typescript
// SSE 伺服器端實作（Express）
app.get('/api/events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'X-Accel-Buffering': 'no',  // Nginx 禁用 buffering
  });

  // 心跳機制
  const heartbeat = setInterval(() => {
    res.write(': heartbeat\n\n');
  }, 30_000);

  // 發送事件
  const sendEvent = (event: string, data: unknown) => {
    res.write(`event: ${event}\n`);
    res.write(`data: ${JSON.stringify(data)}\n`);
    res.write(`id: ${Date.now()}\n\n`);
  };

  // 訂閱 Redis Pub/Sub 接收即時通知
  const subscriber = redis.duplicate();
  subscriber.subscribe('notifications', (message) => {
    sendEvent('notification', JSON.parse(message));
  });

  // 清理
  req.on('close', () => {
    clearInterval(heartbeat);
    subscriber.unsubscribe('notifications');
    subscriber.quit();
  });
});

// 前端 EventSource
const es = new EventSource('/api/events');

es.addEventListener('notification', (event) => {
  const data = JSON.parse(event.data);
  showToast(data.message);
});

es.onerror = () => {
  // EventSource 會自動重連
  console.warn('SSE connection error, reconnecting...');
};
```

---

### 14.8 Micro-Frontend 整合模式

```typescript
// Module Federation（Webpack 5 / Rspack）
// host-app webpack.config.ts
import { ModuleFederationPlugin } from '@module-federation/enhanced';

export default {
  plugins: [
    new ModuleFederationPlugin({
      name: 'host',
      remotes: {
        orderApp: 'orderApp@https://order.example.com/remoteEntry.js',
        userApp: 'userApp@https://user.example.com/remoteEntry.js',
      },
      shared: {
        react: { singleton: true, requiredVersion: '^19.0.0' },
        'react-dom': { singleton: true, requiredVersion: '^19.0.0' },
      },
    }),
  ],
};

// remote-app webpack.config.ts
export default {
  plugins: [
    new ModuleFederationPlugin({
      name: 'orderApp',
      filename: 'remoteEntry.js',
      exposes: {
        './OrderList': './src/components/OrderList.tsx',
        './OrderDetail': './src/components/OrderDetail.tsx',
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true },
      },
    }),
  ],
};

// Host App 動態載入 Remote Component
const OrderList = React.lazy(() => import('orderApp/OrderList'));

function App() {
  return (
    <Suspense fallback={<Skeleton />}>
      <OrderList />
    </Suspense>
  );
}
```

---

### 14.9 API 狀態管理（TanStack Query）

```typescript
// hooks/useOrders.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

// 查詢 Key 工廠模式
const orderKeys = {
  all: ['orders'] as const,
  lists: () => [...orderKeys.all, 'list'] as const,
  list: (filters: OrderFilters) => [...orderKeys.lists(), filters] as const,
  details: () => [...orderKeys.all, 'detail'] as const,
  detail: (id: string) => [...orderKeys.details(), id] as const,
};

// 查詢 Hook
export function useOrders(filters: OrderFilters) {
  return useQuery({
    queryKey: orderKeys.list(filters),
    queryFn: () => orderApi.getOrders(filters),
    staleTime: 5 * 60 * 1000,      // 5 分鐘內視為新鮮
    gcTime: 30 * 60 * 1000,         // 30 分鐘 GC
    placeholderData: keepPreviousData,  // 換頁時保留上一頁資料
  });
}

// 樂觀更新 Mutation
export function useCancelOrder() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (orderId: string) => orderApi.cancelOrder(orderId),
    onMutate: async (orderId) => {
      // 取消進行中的查詢
      await queryClient.cancelQueries({ queryKey: orderKeys.lists() });

      // 快照
      const previous = queryClient.getQueryData(orderKeys.lists());

      // 樂觀更新
      queryClient.setQueriesData({ queryKey: orderKeys.lists() }, (old: any) => ({
        ...old,
        data: old.data.map((order: any) =>
          order.id === orderId ? { ...order, status: 'CANCELLED' } : order
        ),
      }));

      return { previous };
    },
    onError: (_err, _id, context) => {
      // 回滾
      queryClient.setQueriesData({ queryKey: orderKeys.lists() }, context?.previous);
    },
    onSettled: () => {
      // 重新驗證
      queryClient.invalidateQueries({ queryKey: orderKeys.lists() });
    },
  });
}
```

---

## 第 15 章：Docker 化

### 15.1 Node.js Dockerfile 撰寫

#### 基本 Dockerfile

```dockerfile
FROM node:26-alpine

# 安全性：使用非 root 使用者
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# 先複製 package 檔案（利用 Docker 快取層）
COPY package.json pnpm-lock.yaml ./

# 安裝依賴
RUN corepack enable && corepack prepare pnpm@latest --activate
RUN pnpm install --frozen-lockfile --prod

# 複製原始碼
COPY dist/ ./dist/

# 切換到非 root 使用者
USER appuser

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

EXPOSE 3000

CMD ["node", "dist/main.js"]
```

---

### 15.2 Multi-stage Build

```dockerfile
# ===== Stage 1: Build =====
FROM node:26-alpine AS builder

WORKDIR /app

# 啟用 pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# 安裝依賴（含 devDependencies）
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

# 複製原始碼並建置
COPY tsconfig.json ./
COPY src/ ./src/
COPY prisma/ ./prisma/

RUN pnpm exec prisma generate
RUN pnpm run build

# 清除 devDependencies
RUN pnpm prune --prod

# ===== Stage 2: Production =====
FROM node:26-alpine AS production

# 安全性設定
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN apk add --no-cache dumb-init

WORKDIR /app

# 僅複製生產所需檔案
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
COPY --from=builder /app/prisma ./prisma

# 環境變數
ENV NODE_ENV=production
ENV PORT=3000

USER appuser

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

EXPOSE 3000

# 使用 dumb-init 作為 PID 1（正確處理訊號）
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "dist/main.js"]
```

#### Image 大小比較

| 基底映像 | 大小 | 適用場景 |
|----------|------|----------|
| `node:26` | ~1.1GB | 開發、偵錯 |
| `node:26-slim` | ~200MB | 一般生產 |
| `node:26-alpine` | ~130MB | **推薦生產** |
| Multi-stage + Alpine | ~80MB | 最佳化生產 |

---

### 15.3 Docker Compose 開發環境

```yaml
# docker-compose.yml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
      - "9229:9229"    # Debug port
    volumes:
      - ./src:/app/src
      - ./prisma:/app/prisma
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    command: pnpm run dev

  db:
    image: postgres:16-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
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

  adminer:
    image: adminer
    ports:
      - "8080:8080"

volumes:
  pgdata:
```

---

### 15.4 容器安全最佳實務

| 實務 | 說明 |
|------|------|
| **非 root 使用者** | 使用 `USER appuser` 切換 |
| **Alpine 基底** | 最小化攻擊面 |
| **Multi-stage Build** | 不包含建置工具 |
| **dumb-init** | 正確處理 PID 1 訊號 |
| **HEALTHCHECK** | 確保容器存活 |
| **read-only 檔案系統** | `--read-only` flag |
| **掃描漏洞** | `docker scout`, `trivy` |
| **.dockerignore** | 排除不必要檔案 |

```
# .dockerignore
node_modules
dist
.git
.env
*.md
tests
coverage
.vscode
```

#### 章節小練習

1. 撰寫 Multi-stage Dockerfile 並比較 Image 大小。
2. 建立 Docker Compose 開發環境（API + DB + Redis）。
3. 使用 Trivy 掃描 Docker Image 漏洞。

#### 實務注意事項

> - 生產環境使用 Multi-stage Build + Alpine
> - 必須使用非 root 使用者
> - 使用 `dumb-init` 或 `tini` 作為 PID 1
> - 建立 `.dockerignore` 排除不必要檔案
> - 定期掃描 Image 安全漏洞

### 15.5 Docker Compose 完整開發環境

```yaml
# docker-compose.dev.yml
version: '3.9'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: development
    container_name: api-dev
    ports:
      - '3000:3000'
      - '9229:9229'  # Node.js debugger
    volumes:
      - ./src:/app/src
      - ./prisma:/app/prisma
    environment:
      NODE_ENV: development
      DATABASE_URL: postgresql://postgres:postgres@db:5432/app_dev
      REDIS_URL: redis://redis:6379
      JWT_SECRET: dev-secret-at-least-32-characters-long
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    command: npx tsx watch src/main.ts
    networks:
      - app-network

  db:
    image: postgres:16-alpine
    container_name: postgres-dev
    ports:
      - '5432:5432'
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: app_dev
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./scripts/init-db.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 5s
      timeout: 3s
      retries: 5
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    container_name: redis-dev
    ports:
      - '6379:6379'
    volumes:
      - redis-data:/data
    healthcheck:
      test: ['CMD', 'redis-cli', 'ping']
      interval: 5s
      timeout: 3s
      retries: 5
    command: redis-server --appendonly yes --maxmemory 256mb --maxmemory-policy allkeys-lru
    networks:
      - app-network

  mailhog:
    image: mailhog/mailhog
    container_name: mailhog-dev
    ports:
      - '1025:1025'  # SMTP
      - '8025:8025'  # Web UI
    networks:
      - app-network

  minio:
    image: minio/minio
    container_name: minio-dev
    ports:
      - '9000:9000'
      - '9001:9001'  # Console
    environment:
      MINIO_ROOT_USER: minio
      MINIO_ROOT_PASSWORD: minio123
    volumes:
      - minio-data:/data
    command: server /data --console-address ":9001"
    networks:
      - app-network

volumes:
  postgres-data:
  redis-data:
  minio-data:

networks:
  app-network:
    driver: bridge
```

---

### 15.6 生產環境 Docker 最佳實務

```dockerfile
# 生產環境最佳化 Dockerfile
FROM node:26-alpine AS base

# 安裝 tini（PID 1 問題解決方案）
RUN apk add --no-cache tini

# 安全性：建立非 root 使用者
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

WORKDIR /app

# ------- 安裝依賴 -------
FROM base AS deps
COPY package.json pnpm-lock.yaml ./
RUN corepack enable pnpm && \
    pnpm install --frozen-lockfile --prod

# ------- 建置 -------
FROM base AS build
COPY package.json pnpm-lock.yaml ./
RUN corepack enable pnpm && \
    pnpm install --frozen-lockfile
COPY . .
RUN pnpm build && \
    pnpm prune --prod

# ------- 最終映像 -------
FROM base AS production

# 複製必要檔案
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY --from=build /app/package.json ./

# 安全性：移除不必要的檔案
RUN rm -rf /tmp/* /var/cache/apk/*

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# 資源限制標記（搭配 Docker Compose / K8s 使用）
LABEL maintainer="team@example.com" \
      version="1.0.0" \
      description="Production API Server"

USER appuser

EXPOSE 3000

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", "--max-old-space-size=512", "--enable-source-maps", "dist/main.js"]
```

```bash
# 掃描 Image 安全漏洞
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image --severity HIGH,CRITICAL api-server:latest

# 檢視 Image 層級大小
docker history api-server:latest --human --format "{{.Size}}\t{{.CreatedBy}}"

# 減少 Image 大小的技巧
# 1. 使用 Alpine 基底
# 2. Multi-stage Build
# 3. 合併 RUN 指令減少層數
# 4. 使用 .dockerignore
# 5. 只複製 production dependencies
```

---

## 第 16 章：Kubernetes 部署

### 16.1 Deployment 設定

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  labels:
    app: api-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-server
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: api-server
    spec:
      containers:
        - name: api
          image: registry.company.com/api-server:1.0.0
          ports:
            - containerPort: 3000
          env:
            - name: NODE_ENV
              value: "production"
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: database-url
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /health/ready
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          lifecycle:
            preStop:
              exec:
                command: ["/bin/sh", "-c", "sleep 15"]
      terminationGracePeriodSeconds: 30
```

---

### 16.2 Service 與 Ingress

```yaml
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: api-server
spec:
  selector:
    app: api-server
  ports:
    - port: 80
      targetPort: 3000
  type: ClusterIP
---
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
  annotations:
    nginx.ingress.kubernetes.io/rate-limit: "100"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
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
                name: api-server
                port:
                  number: 80
```

---

### 16.3 ConfigMap 與 Secret

```yaml
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  NODE_ENV: "production"
  LOG_LEVEL: "info"
  API_PORT: "3000"
  CORS_ORIGIN: "https://app.company.com"
---
# k8s/secret.yaml（實際應使用 Sealed Secrets 或 External Secrets）
apiVersion: v1
kind: Secret
metadata:
  name: api-secrets
type: Opaque
stringData:
  database-url: "postgresql://user:pass@db:5432/app"
  jwt-secret: "your-256-bit-secret"
  redis-url: "redis://:password@redis:6379"
```

---

### 16.4 HPA 自動擴縮

```yaml
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-server-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-server
  minReplicas: 2
  maxReplicas: 10
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
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Pods
          value: 1
          periodSeconds: 60
```

---

### 16.5 Health Check 與 Readiness Probe

```typescript
// src/health/health.controller.ts
app.get('/health', (req, res) => {
  res.json({ status: 'ok', uptime: process.uptime() });
});

app.get('/health/ready', async (req, res) => {
  try {
    // 檢查所有依賴是否就緒
    await Promise.all([
      prisma.$queryRaw`SELECT 1`,           // DB
      redis.ping(),                           // Redis
    ]);
    res.json({ status: 'ready' });
  } catch (err) {
    res.status(503).json({ status: 'not ready', error: (err as Error).message });
  }
});

app.get('/health/live', (req, res) => {
  // Liveness：程序是否存活（不檢查外部依賴）
  res.json({ status: 'alive' });
});
```

| Probe 類型 | 用途 | 失敗後果 |
|-----------|------|----------|
| **Liveness** | 程序是否存活 | 重啟 Pod |
| **Readiness** | 是否可接收流量 | 從 Service 移除 |
| **Startup** | 啟動是否完成 | 等待後才開始其他 Probe |

#### 章節小練習

1. 撰寫完整的 Kubernetes 部署設定（Deployment + Service + Ingress）。
2. 實作 Readiness Probe 檢查 DB 和 Redis 連線。
3. 設定 HPA 自動擴縮。

#### 實務注意事項

> - 設定 `preStop` hook 搭配 `terminationGracePeriodSeconds` 實現優雅關機
> - Readiness Probe 必須檢查所有關鍵依賴
> - Secret 使用 External Secrets Operator 與 Vault 整合
> - HPA 設定合理的 scaleDown 穩定視窗，避免頻繁伸縮

### 16.6 Helm Chart 管理

```yaml
# helm/api-server/Chart.yaml
apiVersion: v2
name: api-server
description: Node.js API Server Helm Chart
version: 1.0.0
appVersion: "1.0.0"

# helm/api-server/values.yaml
replicaCount: 3

image:
  repository: registry.example.com/api-server
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 3000

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: api.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: api-tls
      hosts:
        - api.example.com

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 200m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80

nodeSelector:
  role: api

tolerations: []

# 環境變數
env:
  NODE_ENV: production
  LOG_LEVEL: info

# 外部 Secret（從 Vault 取得）
externalSecrets:
  enabled: true
  secretStore: vault-backend
  data:
    - secretKey: DATABASE_URL
      remoteRef:
        key: api-server/production
        property: database_url
    - secretKey: JWT_SECRET
      remoteRef:
        key: api-server/production
        property: jwt_secret
```

```yaml
# helm/api-server/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "api-server.fullname" . }}
  labels:
    {{- include "api-server.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      {{- include "api-server.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "api-server.selectorLabels" . | nindent 8 }}
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
    spec:
      terminationGracePeriodSeconds: 30
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 3000
          envFrom:
            - configMapRef:
                name: {{ include "api-server.fullname" . }}-config
            - secretRef:
                name: {{ include "api-server.fullname" . }}-secret
          livenessProbe:
            httpGet:
              path: /health/liveness
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 15
          readinessProbe:
            httpGet:
              path: /health/readiness
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
          lifecycle:
            preStop:
              exec:
                command: ["sh", "-c", "sleep 5"]
```

---

### 16.7 Namespace 與資源隔離策略

```yaml
# 環境隔離 Namespace
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    env: production
    team: backend

---
# ResourceQuota：限制 Namespace 資源上限
apiVersion: v1
kind: ResourceQuota
metadata:
  name: production-quota
  namespace: production
spec:
  hard:
    requests.cpu: "8"
    requests.memory: 16Gi
    limits.cpu: "16"
    limits.memory: 32Gi
    pods: "50"
    services: "20"
    persistentvolumeclaims: "10"

---
# LimitRange：限制單一 Pod 資源
apiVersion: v1
kind: LimitRange
metadata:
  name: production-limits
  namespace: production
spec:
  limits:
    - type: Container
      default:
        cpu: 500m
        memory: 512Mi
      defaultRequest:
        cpu: 200m
        memory: 256Mi
      max:
        cpu: "2"
        memory: 2Gi

---
# NetworkPolicy：限制 Pod 間通訊
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-server-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api-server
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              env: production
        - podSelector:
            matchLabels:
              role: gateway
      ports:
        - protocol: TCP
          port: 3000
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: postgres
      ports:
        - protocol: TCP
          port: 5432
    - to:
        - podSelector:
            matchLabels:
              app: redis
      ports:
        - protocol: TCP
          port: 6379
```

---

## 第 17 章：CI/CD

### 17.1 GitHub Actions 完整範例

```yaml
# .github/workflows/ci.yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

permissions:
  contents: read
  packages: write

env:
  NODE_VERSION: '26'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm run lint
      - run: pnpm exec tsc --noEmit

  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: test
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
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
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm exec prisma migrate deploy
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
      - run: pnpm test -- --coverage
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
          REDIS_URL: redis://localhost:6379
      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm audit --audit-level=high
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  build-and-push:
    needs: [lint, test, security]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest

  deploy:
    needs: build-and-push
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/api-server \
            api=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

---

### 17.2 GitLab CI 配置

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - security
  - build
  - deploy

variables:
  NODE_VERSION: "26"

.node-template: &node-template
  image: node:${NODE_VERSION}-alpine
  before_script:
    - corepack enable
    - corepack prepare pnpm@latest --activate
    - pnpm install --frozen-lockfile

lint:
  <<: *node-template
  stage: lint
  script:
    - pnpm run lint
    - pnpm exec tsc --noEmit

test:
  <<: *node-template
  stage: test
  services:
    - postgres:16-alpine
    - redis:7-alpine
  variables:
    POSTGRES_DB: test
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: postgresql://test:test@postgres:5432/test
    REDIS_URL: redis://redis:6379
  script:
    - pnpm exec prisma migrate deploy
    - pnpm test -- --coverage
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - main
```

---

### 17.3 Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        NODE_VERSION = '26'
        REGISTRY = 'registry.company.com'
    }
    
    stages {
        stage('Install') {
            steps {
                sh 'corepack enable && pnpm install --frozen-lockfile'
            }
        }
        
        stage('Lint & Type Check') {
            steps {
                sh 'pnpm run lint'
                sh 'pnpm exec tsc --noEmit'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pnpm test -- --coverage'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                    publishHTML(target: [
                        reportDir: 'coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Security Scan') {
            steps {
                sh 'pnpm audit --audit-level=high'
            }
        }
        
        stage('Build & Push') {
            when { branch 'main' }
            steps {
                sh "docker build -t ${REGISTRY}/api:${BUILD_NUMBER} ."
                sh "docker push ${REGISTRY}/api:${BUILD_NUMBER}"
            }
        }
        
        stage('Deploy') {
            when { branch 'main' }
            steps {
                sh "kubectl set image deployment/api api=${REGISTRY}/api:${BUILD_NUMBER}"
            }
        }
    }
}
```

---

### 17.4 Build → Test → Security Scan → Docker Build → Deploy 流程

```mermaid
flowchart LR
    A[Push Code] --> B[Lint + Type Check]
    B --> C[Unit Test]
    C --> D[Integration Test]
    D --> E[Security Scan]
    E --> F[Docker Build]
    F --> G[Image Scan]
    G --> H[Push to Registry]
    H --> I[Deploy to Staging]
    I --> J[Smoke Test]
    J --> K{通過?}
    K -->|是| L[Deploy to Production]
    K -->|否| M[Rollback + 通知]
```

#### 章節小練習

1. 建立 GitHub Actions CI/CD Pipeline。
2. 設定自動化安全掃描。
3. 實作 Docker Image 自動建置與推送。

#### 實務注意事項

> - CI/CD 中使用 `--frozen-lockfile` 確保依賴一致
> - 安全掃描是必要步驟，不可跳過
> - 使用 GitHub Environment 保護生產部署
> - Docker Image 使用 commit SHA 作為標籤
> - 部署後執行 Smoke Test 驗證

### 17.5 Semantic Versioning 自動化

```yaml
# .github/workflows/release.yml
name: Semantic Release

on:
  push:
    branches: [main]

permissions:
  contents: write
  packages: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: 26

      - run: corepack enable pnpm && pnpm install --frozen-lockfile

      - name: Semantic Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

```javascript
// .releaserc.js
module.exports = {
  branches: ['main'],
  plugins: [
    ['@semantic-release/commit-analyzer', {
      preset: 'conventionalcommits',
      releaseRules: [
        { type: 'feat', release: 'minor' },
        { type: 'fix', release: 'patch' },
        { type: 'perf', release: 'patch' },
        { type: 'revert', release: 'patch' },
        { breaking: true, release: 'major' },
      ],
    }],
    ['@semantic-release/release-notes-generator', {
      preset: 'conventionalcommits',
      presetConfig: {
        types: [
          { type: 'feat', section: '✨ Features' },
          { type: 'fix', section: '🐛 Bug Fixes' },
          { type: 'perf', section: '⚡ Performance' },
          { type: 'docs', section: '📝 Documentation', hidden: true },
          { type: 'chore', hidden: true },
        ],
      },
    }],
    ['@semantic-release/changelog', { changelogFile: 'CHANGELOG.md' }],
    ['@semantic-release/npm'],
    ['@semantic-release/github'],
    ['@semantic-release/git', {
      assets: ['CHANGELOG.md', 'package.json'],
      message: 'chore(release): ${nextRelease.version} [skip ci]',
    }],
  ],
};
```

---

### 17.6 Commit 規範與自動化

```json
// package.json 中設定 commitlint + husky
{
  "scripts": {
    "prepare": "husky"
  },
  "commitlint": {
    "extends": ["@commitlint/config-conventional"],
    "rules": {
      "type-enum": [2, "always", [
        "feat", "fix", "docs", "style", "refactor",
        "perf", "test", "build", "ci", "chore", "revert"
      ]],
      "subject-max-length": [2, "always", 72],
      "body-max-line-length": [2, "always", 100]
    }
  }
}
```

```bash
# .husky/commit-msg
npx commitlint --edit $1

# .husky/pre-commit
npx lint-staged
```

```json
// lint-staged 設定
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,yaml,yml,md}": ["prettier --write"],
    "*.prisma": ["prisma format"]
  }
}
```

| Commit 類型 | 說明 | 版本影響 |
|------------|------|---------|
| `feat` | 新功能 | Minor |
| `fix` | 修復錯誤 | Patch |
| `perf` | 效能改善 | Patch |
| `docs` | 文件更新 | 無 |
| `refactor` | 重構 | 無 |
| `test` | 測試 | 無 |
| `chore` | 雜項 | 無 |
| `feat!` / `BREAKING CHANGE` | 破壞性變更 | Major |

---

## 第 18 章：Logging 與 Monitoring

### 18.1 Winston 日誌框架

```typescript
import winston from 'winston';

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL ?? 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'api-server',
    version: process.env.APP_VERSION ?? '1.0.0',
  },
  transports: [
    new winston.transports.Console({
      format: process.env.NODE_ENV === 'development'
        ? winston.format.combine(winston.format.colorize(), winston.format.simple())
        : winston.format.json(),
    }),
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' }),
  ],
});

// 使用
logger.info('Server started', { port: 3000 });
logger.error('Database connection failed', { error: err.message, stack: err.stack });
logger.warn('Rate limit exceeded', { ip: req.ip, path: req.path });
```

---

### 18.2 Pino 高效能日誌

```typescript
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL ?? 'info',
  transport: process.env.NODE_ENV === 'development'
    ? { target: 'pino-pretty', options: { colorize: true } }
    : undefined,
  base: {
    service: 'api-server',
    version: process.env.APP_VERSION,
  },
  serializers: {
    err: pino.stdSerializers.err,
    req: pino.stdSerializers.req,
    res: pino.stdSerializers.res,
  },
  redact: ['req.headers.authorization', 'req.headers.cookie'],
});

// Child Logger（加入 Request 上下文）
app.use((req, res, next) => {
  req.log = logger.child({ requestId: req.headers['x-request-id'] });
  next();
});
```

#### Winston vs Pino

| 特性 | Winston | Pino |
|------|---------|------|
| **效能** | 中 | **極高（5-10x 快）** |
| **JSON 格式** | 支援 | 預設 |
| **生態系** | 豐富 | 精簡 |
| **敏感資料遮蔽** | 需自行處理 | 內建 `redact` |
| **NestJS 整合** | 需額外設定 | `nestjs-pino` |

> **✅ 企業推薦**：Pino（效能最佳，結構化日誌）。

---

### 18.3 OpenTelemetry 可觀測性

```mermaid
graph TD
    A[Application] --> B[OpenTelemetry SDK]
    B --> C[Traces]
    B --> D[Metrics]
    B --> E[Logs]
    
    C --> F[Jaeger / Tempo]
    D --> G[Prometheus]
    E --> H[Loki / ELK]
    
    F --> I[Grafana Dashboard]
    G --> I
    H --> I
```

```typescript
// src/telemetry.ts
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { Resource } from '@opentelemetry/resources';
import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from '@opentelemetry/semantic-conventions';

const sdk = new NodeSDK({
  resource: new Resource({
    [ATTR_SERVICE_NAME]: 'api-server',
    [ATTR_SERVICE_VERSION]: '1.0.0',
  }),
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318/v1/traces',
  }),
  metricReader: new OTLPMetricExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318/v1/metrics',
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': { enabled: true },
      '@opentelemetry/instrumentation-express': { enabled: true },
      '@opentelemetry/instrumentation-pg': { enabled: true },
      '@opentelemetry/instrumentation-redis': { enabled: true },
    }),
  ],
});

sdk.start();

process.on('SIGTERM', () => {
  sdk.shutdown().then(() => process.exit(0));
});
```

---

### 18.4 Prometheus 指標收集

```typescript
import { collectDefaultMetrics, Registry, Counter, Histogram } from 'prom-client';

const register = new Registry();
collectDefaultMetrics({ register });

// 自定義指標
const httpRequestsTotal = new Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'path', 'status'],
  registers: [register],
});

const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration in seconds',
  labelNames: ['method', 'path', 'status'],
  buckets: [0.01, 0.05, 0.1, 0.5, 1, 5],
  registers: [register],
});

// Middleware
app.use((req, res, next) => {
  const end = httpRequestDuration.startTimer();
  res.on('finish', () => {
    const labels = { method: req.method, path: req.route?.path ?? req.path, status: res.statusCode.toString() };
    httpRequestsTotal.inc(labels);
    end(labels);
  });
  next();
});

// 指標端點
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});
```

---

### 18.5 Grafana 視覺化監控

#### 關鍵監控面板

| 面板 | 資料來源 | 重要指標 |
|------|----------|----------|
| **API 概覽** | Prometheus | 請求數、錯誤率、延遲 P50/P95/P99 |
| **Node.js Runtime** | Prometheus | Event Loop Lag、Heap Usage、GC |
| **資料庫** | Prometheus | 連線池、查詢延遲、錯誤數 |
| **Redis** | Prometheus | 命中率、記憶體使用、連線數 |
| **分散式追蹤** | Jaeger/Tempo | 請求鏈路、瓶頸分析 |
| **日誌** | Loki/ELK | 錯誤日誌、搜尋分析 |

#### 告警規則

```yaml
# prometheus/alerts.yml
groups:
  - name: api-alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "API 錯誤率超過 5%"
          
      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "API P95 延遲超過 2 秒"

      - alert: HighMemoryUsage
        expr: process_resident_memory_bytes / 1024 / 1024 > 512
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "記憶體使用超過 512MB"
```

#### 章節小練習

1. 整合 Pino + OpenTelemetry 實作結構化日誌。
2. 設定 Prometheus 指標收集（含自定義指標）。
3. 建立 Grafana 告警規則。

#### 實務注意事項

> - 生產環境使用 Pino（效能最佳）
> - 日誌必須結構化（JSON 格式）
> - 敏感資料必須遮蔽（Token、密碼、個資）
> - 使用 OpenTelemetry 實現可觀測性三大支柱（Traces + Metrics + Logs）
> - 建立告警規則，避免只看不管

### 18.6 分散式追蹤（OpenTelemetry）

```typescript
// tracing.ts — 在 main.ts 最頂端 import
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';
import { Resource } from '@opentelemetry/resources';
import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from '@opentelemetry/semantic-conventions';

const sdk = new NodeSDK({
  resource: new Resource({
    [ATTR_SERVICE_NAME]: 'api-server',
    [ATTR_SERVICE_VERSION]: '1.0.0',
    'deployment.environment': process.env.NODE_ENV ?? 'development',
  }),
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318/v1/traces',
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318/v1/metrics',
    }),
    exportIntervalMillis: 30_000,
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': {
        ignoreIncomingRequestHook: (req) => req.url === '/health',
      },
      '@opentelemetry/instrumentation-fs': { enabled: false },
    }),
  ],
});

sdk.start();
process.on('SIGTERM', () => sdk.shutdown());

// 手動建立 Span
import { trace, SpanStatusCode } from '@opentelemetry/api';

const tracer = trace.getTracer('order-service');

async function createOrder(userId: string, dto: CreateOrderDto) {
  return tracer.startActiveSpan('OrderService.createOrder', async (span) => {
    try {
      span.setAttributes({
        'user.id': userId,
        'order.items_count': dto.items.length,
      });

      const order = await processOrder(userId, dto);

      span.setAttributes({
        'order.id': order.id,
        'order.total': order.total,
      });

      span.setStatus({ code: SpanStatusCode.OK });
      return order;
    } catch (error) {
      span.setStatus({
        code: SpanStatusCode.ERROR,
        message: (error as Error).message,
      });
      span.recordException(error as Error);
      throw error;
    } finally {
      span.end();
    }
  });
}
```

---

### 18.7 ELK Stack 日誌架構

```mermaid
graph LR
    A[Node.js API] -->|Pino JSON| B[Filebeat / FluentBit]
    B -->|Ship| C[Logstash]
    C -->|Index| D[Elasticsearch]
    D -->|Visualize| E[Kibana]
    
    F[Node.js Worker] -->|Pino JSON| B
    G[Nginx Access Log] -->|File| B
```

```yaml
# filebeat.yml
filebeat.inputs:
  - type: container
    paths:
      - '/var/lib/docker/containers/*/*.log'
    processors:
      - add_docker_metadata: ~
      - decode_json_fields:
          fields: ['message']
          target: ''
          overwrite_keys: true

output.elasticsearch:
  hosts: ['elasticsearch:9200']
  indices:
    - index: 'api-logs-%{+yyyy.MM.dd}'
      when.contains:
        container.labels.app: 'api-server'
    - index: 'worker-logs-%{+yyyy.MM.dd}'
      when.contains:
        container.labels.app: 'worker'

# Kibana Index Pattern 建議
# api-logs-* → API 服務日誌
# worker-logs-* → Worker 日誌
# 建立 Dashboard：
#   - 請求量趨勢圖
#   - 錯誤率圓餅圖
#   - 回應時間 P95 折線圖
#   - Top 10 慢速端點
```

---

### 18.8 告警策略設計

```yaml
# alertmanager.yml — 分級告警策略
global:
  resolve_timeout: 5m

route:
  receiver: 'default'
  group_by: ['alertname', 'service']
  group_wait: 10s
  group_interval: 5m
  repeat_interval: 4h
  routes:
    - match:
        severity: critical
      receiver: 'pager'
      repeat_interval: 15m
    - match:
        severity: warning
      receiver: 'slack'
      repeat_interval: 1h

receivers:
  - name: 'pager'
    pagerduty_configs:
      - service_key: '<PAGERDUTY_KEY>'
  - name: 'slack'
    slack_configs:
      - api_url: '<SLACK_WEBHOOK_URL>'
        channel: '#alerts'
        title: '{{ .CommonAnnotations.summary }}'
        text: '{{ .CommonAnnotations.description }}'
  - name: 'default'
    email_configs:
      - to: 'team@example.com'
```

| 告警等級 | 回應時間 | 通知方式 | 範例 |
|---------|---------|---------|------|
| **P1 Critical** | 5 分鐘 | PagerDuty + 電話 | 服務完全中斷 |
| **P2 High** | 15 分鐘 | Slack + PagerDuty | 錯誤率 > 5% |
| **P3 Warning** | 1 小時 | Slack | 記憶體 > 80% |
| **P4 Info** | 次日 | Email | 磁碟 > 70% |

---

## 第 19 章：Node.js 效能調校

### 19.1 Event Loop Lag 監控

```typescript
import { monitorEventLoopDelay } from 'node:perf_hooks';
import { Histogram } from 'prom-client';

// 建立 Event Loop Delay 監控器
const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

// Prometheus 指標
const eventLoopLag = new Histogram({
  name: 'nodejs_event_loop_lag_seconds',
  help: 'Event loop lag in seconds',
  buckets: [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1],
});

// 定期回報
setInterval(() => {
  eventLoopLag.observe(h.mean / 1e9);  // 轉換為秒
  h.reset();
}, 10000);

// 即時檢測
function checkEventLoopHealth(): boolean {
  const lagMs = h.mean / 1e6;
  if (lagMs > 100) {
    logger.warn('Event loop lag detected', { lagMs });
    return false;
  }
  return true;
}
```

---

### 19.2 Memory Leak 偵測

```typescript
// 記憶體監控
function monitorMemory() {
  const usage = process.memoryUsage();
  const heapUsedMB = usage.heapUsed / 1024 / 1024;
  const rssMB = usage.rss / 1024 / 1024;

  logger.info('Memory usage', {
    heapUsedMB: heapUsedMB.toFixed(2),
    heapTotalMB: (usage.heapTotal / 1024 / 1024).toFixed(2),
    rssMB: rssMB.toFixed(2),
    externalMB: (usage.external / 1024 / 1024).toFixed(2),
  });

  if (heapUsedMB > 450) {
    logger.error('Memory usage critical', { heapUsedMB });
  }
}

setInterval(monitorMemory, 30000);
```

#### 常見 Memory Leak 模式

| 模式 | 原因 | 解法 |
|------|------|------|
| **全域變數累積** | 不斷往全域陣列/Map push 資料 | 使用 LRU Cache 或設定上限 |
| **事件監聽器未移除** | `emitter.on()` 不配對 `off()` | 使用 `once()` 或手動移除 |
| **閉包引用** | 閉包持有大型物件 | 減少閉包範圍 |
| **Timer 未清理** | `setInterval` 未呼叫 `clearInterval` | 在適當時機清理 |
| **Stream 未關閉** | 檔案/HTTP stream 未 end/destroy | 使用 pipeline() |

```typescript
// ❌ 錯誤：Memory Leak
const cache: Map<string, any> = new Map();
app.get('/data/:id', (req, res) => {
  cache.set(req.params.id, fetchLargeData(req.params.id)); // 無限累積
});

// ✅ 正確：使用 LRU Cache
import { LRUCache } from 'lru-cache';
const cache = new LRUCache<string, any>({ max: 1000, ttl: 1000 * 60 * 5 });
```

---

### 19.3 Heap Snapshot 分析

```bash
# 方法 1：在程式中觸發
node --inspect dist/main.js
# 在 Chrome DevTools 的 Memory Tab 中拍攝 Heap Snapshot

# 方法 2：使用 v8 模組
```

```typescript
import v8 from 'node:v8';
import fs from 'node:fs';

// 透過 API 觸發 Heap Snapshot（需管理員權限保護）
app.post('/debug/heap-snapshot', requireAdmin, (req, res) => {
  const filename = `heap-${Date.now()}.heapsnapshot`;
  const snapshotStream = v8.writeHeapSnapshot(filename);
  res.json({ file: snapshotStream });
});
```

---

### 19.4 CPU Profile 分析

```bash
# 使用 --prof 旗標
node --prof dist/main.js
# 會產生 isolate-*.log 檔案

# 處理結果
node --prof-process isolate-*.log > profile.txt

# 使用 --inspect 搭配 Chrome DevTools
node --inspect dist/main.js
# 在 Chrome DevTools → Performance Tab 錄製
```

```typescript
import { Session } from 'node:inspector/promises';

async function cpuProfile(duration = 5000): Promise<string> {
  const session = new Session();
  session.connect();

  await session.post('Profiler.enable');
  await session.post('Profiler.start');

  await new Promise(resolve => setTimeout(resolve, duration));

  const { profile } = await session.post('Profiler.stop');
  const filename = `cpu-${Date.now()}.cpuprofile`;
  fs.writeFileSync(filename, JSON.stringify(profile));

  session.disconnect();
  return filename;
}
```

---

### 19.5 Benchmark 工具

#### autocannon（HTTP 壓測）

```bash
# 安裝
npm install -g autocannon

# 基本壓測
autocannon -c 100 -d 30 http://localhost:3000/api/users

# 進階設定
autocannon \
  -c 200 \            # 200 並發連線
  -d 60 \             # 測試 60 秒
  -p 10 \             # 每連線 10 個 pipeline
  --json \            # 輸出 JSON
  --renderStatusCodes \
  http://localhost:3000/api/users
```

#### clinic.js（效能診斷套件）

```bash
# 安裝
npm install -g clinic

# Clinic Doctor — 整體健康檢查
clinic doctor -- node dist/main.js

# Clinic Flame — 火焰圖
clinic flame -- node dist/main.js

# Clinic Bubbleprof — 非同步分析
clinic bubbleprof -- node dist/main.js

# 搭配 autocannon 產生流量
clinic doctor --autocannon [ -c 100 -d 30 /api/users ] -- node dist/main.js
```

#### 0x（火焰圖工具）

```bash
npm install -g 0x
0x -- node dist/main.js
# 在另一個 terminal 執行壓測後，按 Ctrl+C 產生火焰圖
```

---

### 19.6 效能最佳化清單

| 策略 | 說明 | 影響 |
|------|------|------|
| **JSON 序列化** | 使用 `fast-json-stringify` | API 回應加速 2-5x |
| **Stream 處理** | 大檔案用 Stream 替代 Buffer | 記憶體降低 90% |
| **連線池** | DB/Redis 使用連線池 | 減少連線開銷 |
| **快取** | 熱資料用 Redis 快取 | 回應加速 10-100x |
| **Worker Threads** | CPU 密集任務移至 Worker | 不阻塞 Event Loop |
| **Cluster Mode** | 多程序利用多核 CPU | 吞吐量翻倍 |
| **壓縮** | 啟用 gzip/brotli | 頻寬降低 60-80% |
| **HTTP/2** | 多工、Header 壓縮 | 延遲降低 |

#### 章節小練習

1. 使用 `autocannon` 對 API 進行壓測，記錄基準。
2. 使用 `clinic doctor` 分析 Event Loop 健康狀態。
3. 找出並修復一個 Memory Leak 範例。

#### 實務注意事項

> - 先量測，再最佳化（避免過早最佳化）
> - Event Loop Lag > 100ms 表示有嚴重阻塞
> - 定期監控記憶體趨勢，而非單次數值
> - 壓測必須在接近生產環境的環境執行
> - 使用 `--max-old-space-size` 設定 Heap 上限

### 19.7 V8 引擎最佳化技巧

```typescript
// 1. 避免 Hidden Class 變更（Inline Cache 失效）

// ❌ 動態新增屬性 → 每次新增都改變 Hidden Class
function createUser(name: string, email: string) {
  const user: any = {};
  user.name = name;
  user.email = email;
  user.createdAt = new Date();
  return user;
}

// ✅ 固定物件形狀（Shape）
interface User {
  name: string;
  email: string;
  createdAt: Date;
}

function createUser(name: string, email: string): User {
  return { name, email, createdAt: new Date() };
}

// 2. 避免 Megamorphic Call Site

// ❌ 同一個函式收到多種不同型態的物件
function process(item: any) {
  return item.id + item.value;  // V8 無法最佳化
}
process({ id: 1, value: 'a' });
process({ id: '2', value: 'b', extra: true });

// ✅ 統一物件形狀
interface Item { id: string; value: string }
function processItem(item: Item): string {
  return item.id + item.value;
}

// 3. 善用 Buffer 替代字串操作（大型資料）
// ❌
let result = '';
for (const chunk of chunks) {
  result += chunk;  // 每次都建立新字串
}

// ✅
const buffers: Buffer[] = [];
for (const chunk of chunks) {
  buffers.push(chunk);
}
const result = Buffer.concat(buffers);
```

---

### 19.8 Worker Threads 平行運算

```typescript
import { Worker, isMainThread, parentPort, workerData } from 'node:worker_threads';
import { availableParallelism } from 'node:os';

// 主執行緒
if (isMainThread) {
  async function processInParallel<T, R>(
    items: T[],
    workerFile: string,
  ): Promise<R[]> {
    const numWorkers = Math.min(items.length, availableParallelism());
    const chunkSize = Math.ceil(items.length / numWorkers);
    
    const promises = Array.from({ length: numWorkers }, (_, i) => {
      const chunk = items.slice(i * chunkSize, (i + 1) * chunkSize);
      return new Promise<R[]>((resolve, reject) => {
        const worker = new Worker(workerFile, { workerData: chunk });
        worker.on('message', resolve);
        worker.on('error', reject);
      });
    });

    const results = await Promise.all(promises);
    return results.flat();
  }

  // 使用
  const results = await processInParallel(largeDataset, './worker.js');
}

// worker.ts（Worker 執行緒）
if (!isMainThread) {
  const data = workerData as DataItem[];
  
  const results = data.map(item => {
    // CPU 密集運算（不會阻塞主執行緒的 Event Loop）
    return heavyComputation(item);
  });
  
  parentPort!.postMessage(results);
}
```

---

### 19.9 Stream 效能最佳化

```typescript
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';
import { createGzip } from 'node:zlib';
import { Transform } from 'node:stream';

// ❌ 一次讀取整個檔案（大檔案會 OOM）
const content = await fs.readFile('large-file.csv', 'utf-8');
const lines = content.split('\n');
const processed = lines.map(processLine);
await fs.writeFile('output.csv', processed.join('\n'));

// ✅ 使用 Stream 逐行處理
const processTransform = new Transform({
  transform(chunk, encoding, callback) {
    const line = chunk.toString();
    const processed = processLine(line);
    callback(null, processed + '\n');
  },
});

await pipeline(
  createReadStream('large-file.csv'),
  processTransform,
  createGzip(),
  createWriteStream('output.csv.gz'),
);

// HTTP 回應使用 Stream
app.get('/api/export', async (req, res) => {
  res.setHeader('Content-Type', 'text/csv');
  res.setHeader('Content-Disposition', 'attachment; filename=export.csv');

  const cursor = prisma.order.findMany({
    cursor: undefined,
    take: 1000,
  });

  // 逐批查詢並串流回應
  let lastId: string | undefined;
  res.write('id,userId,total,status\n');
  
  while (true) {
    const batch = await prisma.order.findMany({
      take: 1000,
      ...(lastId ? { cursor: { id: lastId }, skip: 1 } : {}),
      orderBy: { id: 'asc' },
    });
    
    if (batch.length === 0) break;
    
    for (const order of batch) {
      res.write(`${order.id},${order.userId},${order.total},${order.status}\n`);
    }
    
    lastId = batch[batch.length - 1].id;
  }
  
  res.end();
});
```

---

### 19.10 JSON 序列化加速

```typescript
import fastJson from 'fast-json-stringify';

// 預編譯 JSON 序列化器（比 JSON.stringify 快 2-5 倍）
const stringifyUser = fastJson({
  type: 'object',
  properties: {
    id: { type: 'string' },
    name: { type: 'string' },
    email: { type: 'string' },
    role: { type: 'string' },
    createdAt: { type: 'string', format: 'date-time' },
  },
  required: ['id', 'name', 'email'],
});

const stringifyUserList = fastJson({
  type: 'object',
  properties: {
    data: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          name: { type: 'string' },
          email: { type: 'string' },
        },
      },
    },
    total: { type: 'integer' },
    cursor: { type: 'string', nullable: true },
  },
});

// 使用
app.get('/api/users', async (req, res) => {
  const users = await prisma.user.findMany({ take: 20 });
  const body = stringifyUserList({ data: users, total: users.length, cursor: null });
  res.type('application/json').send(body);
});
```

---

## 第 20 章：安全性 SSDLC

### 20.1 OWASP Top 10 for Node.js

| 排名 | 威脅 | Node.js 對策 |
|------|------|-------------|
| A01 | Broken Access Control | RBAC 中介層、最小權限原則 |
| A02 | Cryptographic Failures | 使用 `node:crypto`、HTTPS、TLS 1.3 |
| A03 | Injection | 參數化查詢、Zod 驗證、CSP |
| A04 | Insecure Design | Threat Modeling、安全架構審查 |
| A05 | Security Misconfiguration | Helmet、環境變數、最小化映像 |
| A06 | Vulnerable Components | `npm audit`、Snyk、Dependabot |
| A07 | Auth Failures | JWT 短效期 + Refresh Token、bcrypt |
| A08 | Data Integrity Failures | 簽章驗證、CI/CD 安全、SRI |
| A09 | Logging & Monitoring | 結構化日誌、告警、SIEM |
| A10 | SSRF | URL 白名單、DNS 解析檢查 |

---

### 20.2 npm 供應鏈攻擊防護

```bash
# 1. 鎖定依賴版本
pnpm install --frozen-lockfile

# 2. 安全稽核
pnpm audit --audit-level=high

# 3. 使用 Socket.dev 檢測惡意套件
npx socket scan

# 4. 設定 .npmrc 安全策略
```

```ini
# .npmrc
ignore-scripts=true           # 不自動執行 postinstall 腳本
audit-level=high
strict-ssl=true
registry=https://registry.npmjs.org/
```

```typescript
// package.json — 限制允許執行腳本的套件
{
  "pnpm": {
    "onlyBuiltDependencies": [
      "bcrypt",
      "sharp"
    ]
  }
}
```

---

### 20.3 依賴掃描與 SAST/DAST

```yaml
# GitHub Actions — 自動化安全掃描
- name: npm audit
  run: pnpm audit --audit-level=high

- name: Snyk Security Scan
  uses: snyk/actions/node@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

- name: CodeQL Analysis
  uses: github/codeql-action/analyze@v3
  with:
    languages: javascript-typescript

- name: DAST with OWASP ZAP
  uses: zaproxy/action-full-scan@v0.11.0
  with:
    target: 'https://staging.company.com'
```

| 工具類型 | 工具 | 用途 |
|----------|------|------|
| **SCA** | npm audit, Snyk, Socket.dev | 依賴漏洞掃描 |
| **SAST** | CodeQL, SonarQube, Semgrep | 原始碼靜態分析 |
| **DAST** | OWASP ZAP, Burp Suite | 動態安全測試 |
| **Secret Scan** | GitLeaks, TruffleHog | 偵測洩漏的金鑰 |

---

### 20.4 Secret 管理

```typescript
// ❌ 錯誤：硬編碼 Secret
const JWT_SECRET = 'my-super-secret-key';

// ✅ 正確：從環境變數讀取
const JWT_SECRET = process.env.JWT_SECRET;
if (!JWT_SECRET) throw new Error('JWT_SECRET is required');

// ✅ 更佳：使用 Secret Manager
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';

async function getSecret(name: string): Promise<string> {
  const client = new SecretManagerServiceClient();
  const [version] = await client.accessSecretVersion({ name });
  return version.payload?.data?.toString() ?? '';
}
```

```bash
# .gitignore — 確保 Secret 不進入版控
.env
.env.*
!.env.example
*.pem
*.key
```

---

### 20.5 JWT 安全最佳實務

```typescript
import jwt from 'jsonwebtoken';

// Token 產生
function generateTokens(userId: string) {
  const accessToken = jwt.sign(
    { sub: userId, type: 'access' },
    process.env.JWT_SECRET!,
    { expiresIn: '15m', algorithm: 'HS256' }   // 短效期
  );

  const refreshToken = jwt.sign(
    { sub: userId, type: 'refresh' },
    process.env.JWT_REFRESH_SECRET!,
    { expiresIn: '7d', algorithm: 'HS256' }
  );

  return { accessToken, refreshToken };
}

// Token 驗證
function verifyAccessToken(token: string) {
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET!, {
      algorithms: ['HS256'],     // 限定演算法
      complete: true,
    });
    return payload;
  } catch (err) {
    if (err instanceof jwt.TokenExpiredError) {
      throw new UnauthorizedException('Token expired');
    }
    throw new UnauthorizedException('Invalid token');
  }
}
```

---

### 20.6 Helmet、CORS 與 Rate Limiting

```typescript
import helmet from 'helmet';
import cors from 'cors';
import rateLimit from 'express-rate-limit';

// Helmet — 設定安全相關 HTTP Header
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:'],
    },
  },
  hsts: { maxAge: 31536000, includeSubDomains: true },
}));

// CORS — 跨域設定
app.use(cors({
  origin: process.env.CORS_ORIGINS?.split(',') ?? ['https://app.company.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
  credentials: true,
  maxAge: 86400,
}));

// Rate Limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,   // 15 分鐘
  max: 100,                     // 每個 IP 100 次
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: { code: 'RATE_LIMIT_EXCEEDED', message: 'Too many requests' } },
});
app.use('/api/', limiter);

// 登入端點更嚴格的限制
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true,
});
app.use('/api/auth/login', loginLimiter);
```

#### 章節小練習

1. 設定 Helmet + CORS + Rate Limiting。
2. 建立 GitHub Actions 安全掃描 Pipeline。
3. 實作 JWT Access + Refresh Token 流程。

#### 實務注意事項

> - 所有使用者輸入都必須驗證（Zod/Joi）
> - JWT Access Token 效期不超過 15 分鐘
> - 密碼使用 `bcrypt` 或 `argon2` 雜湊
> - 定期執行 `npm audit` 並修復漏洞
> - 生產環境必須使用 HTTPS
> - 敏感資料日誌中必須遮蔽

### 20.7 輸入驗證與 Injection 防護

```typescript
import { z } from 'zod';
import DOMPurify from 'isomorphic-dompurify';

// Zod Schema 驗證（防止 Injection）
const CreateUserSchema = z.object({
  name: z.string()
    .min(1).max(100)
    .regex(/^[\p{L}\p{N}\s\-]+$/u, 'Name contains invalid characters'),
  email: z.string().email(),
  password: z.string()
    .min(8).max(128)
    .regex(/(?=.*[a-z])/, 'Must contain lowercase letter')
    .regex(/(?=.*[A-Z])/, 'Must contain uppercase letter')
    .regex(/(?=.*\d)/, 'Must contain number')
    .regex(/(?=.*[!@#$%^&*])/, 'Must contain special character'),
  bio: z.string().max(500).optional(),
});

// XSS 防護（HTML 內容清潔）
function sanitizeHtml(input: string): string {
  return DOMPurify.sanitize(input, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p', 'br'],
    ALLOWED_ATTR: [],
  });
}

// NoSQL Injection 防護（MongoDB）
// ❌ 危險：使用者可傳入 { "$gt": "" }
app.get('/api/users', async (req, res) => {
  const filter = req.query.filter; // 未驗證
  const users = await db.collection('users').find(filter).toArray();
});

// ✅ 安全：明確指定允許的欄位和值
app.get('/api/users', async (req, res) => {
  const role = z.enum(['admin', 'user', 'viewer']).parse(req.query.role);
  const users = await db.collection('users').find({ role }).toArray();
});

// Path Traversal 防護
import path from 'node:path';

function safeFilePath(userInput: string, baseDir: string): string {
  const resolved = path.resolve(baseDir, userInput);
  if (!resolved.startsWith(path.resolve(baseDir))) {
    throw new Error('Path traversal detected');
  }
  return resolved;
}
```

---

### 20.8 SSRF 防護

```typescript
import dns from 'node:dns/promises';
import { URL } from 'node:url';
import ipaddr from 'ipaddr.js';

// SSRF 防護：驗證 URL 目標
async function safeFetch(url: string): Promise<Response> {
  const parsed = new URL(url);

  // 1. 只允許 HTTPS
  if (parsed.protocol !== 'https:') {
    throw new Error('Only HTTPS URLs are allowed');
  }

  // 2. 白名單檢查
  const allowedDomains = ['api.github.com', 'api.stripe.com'];
  if (!allowedDomains.includes(parsed.hostname)) {
    throw new Error('Domain not in whitelist');
  }

  // 3. DNS 解析後檢查是否為內網 IP
  const addresses = await dns.resolve4(parsed.hostname);
  for (const addr of addresses) {
    const ip = ipaddr.parse(addr);
    if (ip.range() !== 'unicast') {
      throw new Error('Internal IP address detected');
    }
  }

  return fetch(url, {
    signal: AbortSignal.timeout(10000),
    redirect: 'error',   // 不跟隨重定向
  });
}
```

---

### 20.9 密碼安全與雜湊

```typescript
import bcrypt from 'bcrypt';
import argon2 from 'argon2';

// bcrypt（最廣泛使用）
const SALT_ROUNDS = 12;

async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS);
}

async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return bcrypt.compare(password, hash);
}

// argon2（OWASP 推薦，更安全）
async function hashPasswordArgon2(password: string): Promise<string> {
  return argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 65536,      // 64MB
    timeCost: 3,            // 3 次迭代
    parallelism: 4,
  });
}

async function verifyPasswordArgon2(password: string, hash: string): Promise<boolean> {
  return argon2.verify(hash, password);
}
```

| 演算法 | 安全性 | 效能 | OWASP 推薦 |
|--------|--------|------|-----------|
| **MD5 / SHA-256** | ❌ 不安全 | 極快 | 不推薦 |
| **bcrypt** | ✅ 安全 | 中 | 推薦 |
| **argon2id** | ✅ 最安全 | 慢（可調） | **最推薦** |
| **scrypt** | ✅ 安全 | 慢 | 推薦 |

---

### 20.10 Content Security Policy（CSP）

```typescript
// 嚴格的 CSP 設定
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'strict-dynamic'"],
      styleSrc: ["'self'", "'unsafe-inline'"],    // CSS 通常需要 inline
      imgSrc: ["'self'", 'data:', 'https://cdn.company.com'],
      fontSrc: ["'self'", 'https://fonts.gstatic.com'],
      connectSrc: ["'self'", 'https://api.company.com'],
      mediaSrc: ["'none'"],
      objectSrc: ["'none'"],
      frameSrc: ["'none'"],
      baseUri: ["'self'"],
      formAction: ["'self'"],
      frameAncestors: ["'none'"],
      upgradeInsecureRequests: [],
    },
    reportOnly: false,
  },
}));

// CSP 違規報告
app.post('/csp-report', express.json({ type: 'application/csp-report' }), (req, res) => {
  logger.warn('CSP Violation', req.body);
  res.status(204).end();
});
```

---

### 20.11 安全 HTTP Headers 完整清單

| Header | 值 | 用途 |
|--------|-----|------|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | 強制 HTTPS |
| `Content-Security-Policy` | 見上方 | 防止 XSS |
| `X-Content-Type-Options` | `nosniff` | 防止 MIME 嗅探 |
| `X-Frame-Options` | `DENY` | 防止 Clickjacking |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 控制 Referer |
| `Permissions-Policy` | `camera=(), microphone=()` | 控制瀏覽器 API |
| `X-XSS-Protection` | `0` | 關閉舊版 XSS 篩選（依賴 CSP） |
| `Cross-Origin-Opener-Policy` | `same-origin` | 隔離跨域視窗 |
| `Cross-Origin-Resource-Policy` | `same-origin` | 控制跨域資源 |

---

## 第 21 章：AI 協作開發

### 21.1 GitHub Copilot

```typescript
// GitHub Copilot 可在 VS Code 中即時建議程式碼
// 最佳使用方式：

// 1. 寫清楚的函式簽名和註解
/** 計算訂單總金額（含稅和折扣） */
function calculateOrderTotal(
  items: OrderItem[],
  taxRate: number,
  discount?: Discount
): number {
  // Copilot 會根據簽名和註解產生實作
  const subtotal = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const discountAmount = discount ? applyDiscount(subtotal, discount) : 0;
  const taxable = subtotal - discountAmount;
  return taxable + taxable * taxRate;
}

// 2. 使用 Copilot Chat 進行對話式開發
// /explain — 解釋程式碼
// /fix — 修正錯誤
// /tests — 產生測試
// @workspace — 詢問專案相關問題
```

#### Copilot 使用技巧

| 功能 | 指令 | 說明 |
|------|------|------|
| **Code Completion** | Tab 接受 | 即時程式碼建議 |
| **Copilot Chat** | Ctrl+I | 行內對話 |
| **Explain** | `/explain` | 解釋選取的程式碼 |
| **Fix** | `/fix` | 修正錯誤 |
| **Generate Tests** | `/tests` | 產生單元測試 |
| **Workspace Q&A** | `@workspace` | 詢問整個專案 |
| **Terminal** | `@terminal` | 終端指令協助 |

---

### 21.2 Claude Code

```bash
# 安裝 Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 在專案目錄中啟動
claude

# 常用指令
claude "幫我建立 NestJS CRUD Module for User"
claude "review 這段程式碼的安全性"
claude "寫測試涵蓋所有 edge cases"
claude "重構這個函式，提高可讀性"
```

#### Claude Code 最佳實務

- **專案規範檔案**：在 `CLAUDE.md` 中定義專案規則
- **漸進式開發**：一次聚焦一個功能
- **Code Review**：讓 Claude 審查程式碼品質
- **測試產生**：描述場景讓 Claude 產生測試

---

### 21.3 其他 AI 工具整合

| 工具 | 強項 | 整合方式 |
|------|------|----------|
| **GitHub Copilot** | IDE 整合、即時建議 | VS Code 擴充 |
| **Claude Code** | 長上下文、複雜重構 | CLI / API |
| **Cursor AI** | AI-first IDE | 獨立 IDE |
| **OpenAI Codex / ChatGPT** | 通用程式協助 | API / Web |
| **Google Gemini** | 大型程式碼庫理解 | API / Web |
| **Amazon Q Developer** | AWS 整合 | VS Code 擴充 |

---

### 21.4 Prompt Engineering for Coding

````markdown
## 好的 Prompt 模板

### 產生程式碼
```
你是一位資深 Node.js 開發者。
請使用 TypeScript + NestJS 建立一個 User CRUD Module，要求：
- 使用 Prisma 作為 ORM
- 包含 Zod DTO 驗證
- 實作分頁查詢（cursor-based）
- 包含完整錯誤處理
- 遵循 Clean Architecture
```

### Code Review
```
請審查以下程式碼，檢查：
1. 安全漏洞（OWASP Top 10）
2. 效能問題
3. 錯誤處理是否完整
4. TypeScript 型別安全
5. 最佳實務符合度
```

### 測試產生
```
為以下函式撰寫 Vitest 測試案例，涵蓋：
- Happy path
- Edge cases（空陣列、null、undefined）
- Error cases（無效輸入、權限不足）
- 邊界值
```
````

---

### 21.5 AI 輔助 Code Review

```typescript
// 在 CI/CD 中整合 AI Code Review
// .github/workflows/ai-review.yml

// 範例：使用 GitHub Copilot for PRs
// 自動在 PR 中提供建議

// 人工 + AI 混合流程
// 1. 開發者提交 PR
// 2. AI 自動審查（格式、安全、最佳實務）
// 3. 人工審查（業務邏輯、架構決策）
// 4. 修正後合併
```

#### AI 協作開發原則

| 原則 | 說明 |
|------|------|
| **信任但驗證** | AI 產生的程式碼必須人工審查 |
| **漸進式採用** | 從小功能開始，逐步擴大 |
| **提供上下文** | 給 AI 足夠的專案背景 |
| **測試驗證** | AI 產生的程式碼必須通過測試 |
| **安全優先** | AI 建議的套件需驗證安全性 |

#### 章節小練習

1. 使用 Copilot Chat 產生 CRUD API 並驗證。
2. 撰寫 `CLAUDE.md` 定義專案規則。
3. 使用 AI 對現有程式碼進行安全審查。

#### 實務注意事項

> - AI 產生的程式碼必須通過 Code Review
> - 不要盲目接受 AI 建議，要理解後再採用
> - AI 工具不取代測試，產生的程式碼仍需完整測試
> - 敏感資料不要貼到公開 AI 服務
> - 在 `CLAUDE.md` 或 `.github/copilot-instructions.md` 定義規則

### 21.6 AI 輔助測試產生

```typescript
// 範例：使用 AI 產生的完整測試
// 提供 Prompt：「為 OrderService.createOrder 撰寫完整 Vitest 測試」

// AI 產生的測試（人工審查後）
describe('OrderService.createOrder', () => {
  let service: OrderService;
  let mockOrderRepo: MockProxy<OrderRepository>;
  let mockProductRepo: MockProxy<ProductRepository>;
  let mockEventBus: MockProxy<EventBus>;

  beforeEach(() => {
    mockOrderRepo = mock<OrderRepository>();
    mockProductRepo = mock<ProductRepository>();
    mockEventBus = mock<EventBus>();
    service = new OrderService(mockOrderRepo, mockProductRepo, mockEventBus);
  });

  // Happy path
  it('should create order with valid items', async () => {
    const items = [{ productId: 'P1', quantity: 2 }];
    const product = { id: 'P1', name: 'Widget', price: 100, stock: 10 };
    
    mockProductRepo.findById.calledWith('P1').mockResolvedValue(product);
    mockOrderRepo.create.mockResolvedValue({ id: 'O1', total: 200, status: 'PENDING' });

    const result = await service.createOrder('U1', items);

    expect(result.total).toBe(200);
    expect(mockEventBus.publish).toHaveBeenCalledWith(
      expect.objectContaining({ type: 'order.created' })
    );
  });

  // Edge cases
  it('should handle empty items array', async () => {
    await expect(service.createOrder('U1', [])).rejects.toThrow('Order must have items');
  });

  it('should handle quantity of zero', async () => {
    await expect(
      service.createOrder('U1', [{ productId: 'P1', quantity: 0 }])
    ).rejects.toThrow('Quantity must be positive');
  });

  // Error cases
  it('should throw when product not found', async () => {
    mockProductRepo.findById.mockResolvedValue(null);
    await expect(
      service.createOrder('U1', [{ productId: 'P999', quantity: 1 }])
    ).rejects.toThrow('Product not found');
  });

  it('should throw when insufficient stock', async () => {
    const product = { id: 'P1', name: 'Widget', price: 100, stock: 1 };
    mockProductRepo.findById.mockResolvedValue(product);
    
    await expect(
      service.createOrder('U1', [{ productId: 'P1', quantity: 10 }])
    ).rejects.toThrow('Insufficient stock');
  });

  // Concurrency
  it('should handle concurrent stock deductions', async () => {
    const product = { id: 'P1', name: 'Widget', price: 100, stock: 5 };
    mockProductRepo.findById.mockResolvedValue(product);
    mockOrderRepo.create
      .mockResolvedValueOnce({ id: 'O1', total: 300, status: 'PENDING' })
      .mockRejectedValueOnce(new Error('Insufficient stock'));

    const results = await Promise.allSettled([
      service.createOrder('U1', [{ productId: 'P1', quantity: 3 }]),
      service.createOrder('U2', [{ productId: 'P1', quantity: 3 }]),
    ]);

    const fulfilled = results.filter(r => r.status === 'fulfilled');
    expect(fulfilled.length).toBe(1);
  });
});
```

---

### 21.7 AI 輔助文件產生

```typescript
// 使用 AI 產生 API 文件的 Prompt 範例
`
分析以下 NestJS Controller，產生完整的 API 文件：
- 每個端點的描述
- 請求/回應範例
- 錯誤碼說明
- 認證需求

Controller 程式碼：
[貼上程式碼]
`

// AI 產生的 OpenAPI 註解（審查後加入程式碼）
@ApiOperation({
  summary: '建立訂單',
  description: '為指定使用者建立新訂單。需要 Bearer Token 認證。',
})
@ApiBody({
  type: CreateOrderDto,
  examples: {
    basic: {
      summary: '基本訂單',
      value: {
        items: [{ productId: 'P001', quantity: 2 }],
        shippingAddress: '台北市信義區...',
      },
    },
  },
})
@ApiResponse({ status: 201, description: '訂單建立成功', type: OrderResponseDto })
@ApiResponse({ status: 400, description: '驗證錯誤' })
@ApiResponse({ status: 422, description: '庫存不足' })
```

---

### 21.8 CLAUDE.md 專案規範範例

```markdown
# CLAUDE.md — 專案規範

## 技術堆疊
- Runtime: Node.js v26
- Language: TypeScript (strict mode)
- Framework: NestJS
- ORM: Prisma
- Database: PostgreSQL 16
- Cache: Redis 7
- Test: Vitest
- Package Manager: pnpm

## 程式碼規範
- 使用 ESM（import/export）
- 嚴格禁止 any 型別
- 所有 public API 必須有 JSDoc 註解
- 每個 Service 方法必須有對應 Unit Test
- 錯誤處理使用 AppError 類別

## 架構規範
- 遵循 Clean Architecture
- Domain 層不可依賴 Infrastructure 層
- 使用 Repository Pattern 存取資料
- 使用 DTO 進行資料傳輸

## 命名規範
- 檔案：kebab-case（user-service.ts）
- 類別：PascalCase（UserService）
- 方法/變數：camelCase（findById）
- 常數：UPPER_SNAKE_CASE（MAX_RETRY_COUNT）
- 介面：不加 I 前綴（UserRepository 而非 IUserRepository）

## 安全規範
- 所有使用者輸入必須使用 Zod 驗證
- 密碼使用 argon2id 雜湊
- JWT Access Token 有效期 15 分鐘
- 敏感資料不可寫入日誌
```

---

## 第 22 章：Node.js 維運

### 22.1 PM2 程序管理

```bash
# 安裝
npm install -g pm2

# 啟動應用程式
pm2 start dist/main.js --name api-server -i max

# 常用指令
pm2 list                # 查看所有程序
pm2 logs api-server     # 查看日誌
pm2 monit               # 即時監控
pm2 restart api-server  # 重啟
pm2 reload api-server   # 零停機重啟
pm2 stop api-server     # 停止
pm2 delete api-server   # 刪除
```

#### PM2 設定檔

```javascript
// ecosystem.config.cjs
module.exports = {
  apps: [{
    name: 'api-server',
    script: 'dist/main.js',
    instances: 'max',          // 使用所有 CPU 核心
    exec_mode: 'cluster',      // Cluster 模式
    max_memory_restart: '500M',
    env_production: {
      NODE_ENV: 'production',
      PORT: 3000,
    },
    // 日誌設定
    log_file: '/var/log/api/combined.log',
    error_file: '/var/log/api/error.log',
    out_file: '/var/log/api/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    merge_logs: true,
    // 自動重啟策略
    watch: false,
    max_restarts: 10,
    restart_delay: 5000,
    autorestart: true,
    // Graceful Shutdown
    kill_timeout: 10000,
    listen_timeout: 10000,
    shutdown_with_message: true,
  }],
};
```

---

### 22.2 Cluster 模式

```typescript
import cluster from 'node:cluster';
import { availableParallelism } from 'node:os';

const numCPUs = availableParallelism();

if (cluster.isPrimary) {
  console.log(`Primary ${process.pid} is running`);
  console.log(`Forking ${numCPUs} workers...`);

  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.warn(`Worker ${worker.process.pid} died (${signal || code}). Restarting...`);
    cluster.fork();  // 自動重啟
  });

  // 優雅關機
  process.on('SIGTERM', () => {
    for (const id in cluster.workers) {
      cluster.workers[id]?.process.kill('SIGTERM');
    }
  });
} else {
  // Worker 程序啟動 HTTP 伺服器
  const app = createApp();
  app.listen(3000, () => {
    console.log(`Worker ${process.pid} started`);
  });
}
```

---

### 22.3 部署策略

```mermaid
graph LR
    subgraph "Rolling Update"
        A1[v1] --> A2[v2]
        A3[v1] --> A4[v1]
        A5[v1] --> A6[v1]
    end
    
    subgraph "Blue-Green"
        B1[Blue v1<br/>Active] --> B2[Green v2<br/>Standby]
    end
    
    subgraph "Canary"
        C1[v1 90%] --> C2[v2 10%]
    end
```

| 策略 | 零停機 | 回滾速度 | 資源需求 | 風險 |
|------|--------|----------|----------|------|
| **Rolling** | ✅ | 慢 | 低 | 中 |
| **Blue-Green** | ✅ | **極快** | **雙倍** | 低 |
| **Canary** | ✅ | 快 | 低 | **最低** |

---

### 22.4 Graceful Shutdown

```typescript
import { createServer } from 'node:http';

const server = createServer(app);
let isShuttingDown = false;

// 啟動伺服器
server.listen(3000, () => {
  console.log('Server started on port 3000');
});

// 優雅關機處理
async function gracefulShutdown(signal: string) {
  console.log(`Received ${signal}. Starting graceful shutdown...`);
  isShuttingDown = true;

  // 1. 停止接收新連線
  server.close(async () => {
    console.log('HTTP server closed');

    try {
      // 2. 等待進行中的請求完成（最多 30 秒）
      // 3. 關閉資料庫連線
      await prisma.$disconnect();
      console.log('Database disconnected');

      // 4. 關閉 Redis 連線
      await redis.quit();
      console.log('Redis disconnected');

      // 5. 清理其他資源
      console.log('Graceful shutdown complete');
      process.exit(0);
    } catch (err) {
      console.error('Error during shutdown', err);
      process.exit(1);
    }
  });

  // 強制超時退出
  setTimeout(() => {
    console.error('Forced shutdown after timeout');
    process.exit(1);
  }, 30000);
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

// 健康檢查中介層
app.use((req, res, next) => {
  if (isShuttingDown) {
    res.status(503).json({ error: 'Server is shutting down' });
    return;
  }
  next();
});
```

---

### 22.5 維運監控 Checklist

```mermaid
graph TD
    A[維運監控] --> B[基礎設施]
    A --> C[應用程式]
    A --> D[業務指標]
    
    B --> B1[CPU / Memory / Disk]
    B --> B2[Network I/O]
    B --> B3[Container 狀態]
    
    C --> C1[Event Loop Lag]
    C --> C2[Heap Usage]
    C --> C3[Active Handles]
    C --> C4[Request Rate / Error Rate]
    
    D --> D1[註冊轉換率]
    D --> D2[API 回應時間]
    D --> D3[交易成功率]
```

#### 章節小練習

1. 使用 PM2 Cluster 模式部署應用。
2. 實作完整的 Graceful Shutdown 流程。
3. 設定 Rolling Update 部署策略。

#### 實務注意事項

> - 生產環境使用 PM2 Cluster 或 Kubernetes
> - 必須實作 Graceful Shutdown
> - Kubernetes 中使用 `preStop` hook 延遲關機
> - 監控 Event Loop Lag 和記憶體趨勢
> - 部署策略首選 Blue-Green 或 Canary

### 22.6 Node.js 生產環境設定

```typescript
// 生產環境必要設定
// 1. 環境變數管理
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().url(),
  REDIS_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  JWT_REFRESH_SECRET: z.string().min(32),
  CORS_ORIGINS: z.string(),
  LOG_LEVEL: z.enum(['fatal', 'error', 'warn', 'info', 'debug', 'trace']).default('info'),
  SENTRY_DSN: z.string().url().optional(),
});

export const env = envSchema.parse(process.env);

// 2. 未處理例外的全域捕獲
process.on('uncaughtException', (error) => {
  logger.fatal({ err: error }, 'Uncaught Exception');
  // 發送到 Sentry 等錯誤追蹤服務
  process.exit(1);  // 必須退出（狀態已不可信）
});

process.on('unhandledRejection', (reason) => {
  logger.error({ err: reason }, 'Unhandled Rejection');
  // Node.js 15+ 預設會退出，舊版需要手動處理
});

// 3. 記憶體限制
// 啟動時設定：node --max-old-space-size=512 dist/main.js

// 4. 信號處理
process.on('SIGTERM', gracefulShutdown);  // Kubernetes / Docker stop
process.on('SIGINT', gracefulShutdown);   // Ctrl+C
```

---

### 22.7 日誌輪替與管理

```typescript
// PM2 日誌輪替
// 安裝：pm2 install pm2-logrotate
// 設定：
// pm2 set pm2-logrotate:max_size 10M
// pm2 set pm2-logrotate:retain 30
// pm2 set pm2-logrotate:compress true
// pm2 set pm2-logrotate:dateFormat YYYY-MM-DD_HH-mm-ss

// Docker 日誌驅動
// docker-compose.yml
// services:
//   api:
//     logging:
//       driver: "json-file"
//       options:
//         max-size: "10m"
//         max-file: "5"

// 集中式日誌（ELK / Loki）
// Pino → Pino Transport → Loki / Elasticsearch
import pino from 'pino';

const transport = pino.transport({
  targets: [
    {
      target: 'pino-pretty',
      options: { colorize: true },
      level: 'debug',
    },
    {
      target: 'pino-loki',
      options: {
        host: process.env.LOKI_URL,
        labels: { app: 'api-server', env: process.env.NODE_ENV },
        batching: true,
        interval: 5,
      },
      level: 'info',
    },
  ],
});

const logger = pino(transport);
```

---

### 22.8 健康檢查與自我修復

```typescript
// 進階健康檢查端點
interface HealthCheck {
  name: string;
  check: () => Promise<{ status: 'up' | 'down'; responseTime: number; details?: unknown }>;
}

const healthChecks: HealthCheck[] = [
  {
    name: 'database',
    check: async () => {
      const start = performance.now();
      try {
        await prisma.$queryRaw`SELECT 1`;
        return { status: 'up', responseTime: performance.now() - start };
      } catch (err) {
        return { status: 'down', responseTime: performance.now() - start, details: (err as Error).message };
      }
    },
  },
  {
    name: 'redis',
    check: async () => {
      const start = performance.now();
      try {
        await redis.ping();
        return { status: 'up', responseTime: performance.now() - start };
      } catch (err) {
        return { status: 'down', responseTime: performance.now() - start, details: (err as Error).message };
      }
    },
  },
  {
    name: 'memory',
    check: async () => {
      const used = process.memoryUsage();
      const heapUsedMB = used.heapUsed / 1024 / 1024;
      return {
        status: heapUsedMB < 450 ? 'up' : 'down',
        responseTime: 0,
        details: { heapUsedMB: Math.round(heapUsedMB), rssMB: Math.round(used.rss / 1024 / 1024) },
      };
    },
  },
  {
    name: 'eventLoop',
    check: async () => {
      const start = performance.now();
      await new Promise(resolve => setImmediate(resolve));
      const lag = performance.now() - start;
      return {
        status: lag < 100 ? 'up' : 'down',
        responseTime: lag,
        details: { lagMs: lag.toFixed(2) },
      };
    },
  },
];

app.get('/health/detailed', async (req, res) => {
  const results = await Promise.all(
    healthChecks.map(async (hc) => ({
      name: hc.name,
      ...(await hc.check()),
    }))
  );

  const allUp = results.every(r => r.status === 'up');
  res.status(allUp ? 200 : 503).json({
    status: allUp ? 'healthy' : 'unhealthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    checks: results,
  });
});
```

---

## 第 23 章：企業級最佳實務

### 23.1 Coding Standard 與 Lint

#### ESLint 設定

```typescript
// eslint.config.mjs（ESLint Flat Config）
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintPluginPrettier from 'eslint-plugin-prettier/recommended';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  eslintPluginPrettier,
  {
    languageOptions: {
      parserOptions: {
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
    rules: {
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/explicit-function-return-type': 'warn',
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/no-misused-promises': 'error',
      '@typescript-eslint/strict-boolean-expressions': 'warn',
      'no-console': ['warn', { allow: ['warn', 'error'] }],
    },
  },
  {
    ignores: ['dist/', 'node_modules/', 'coverage/'],
  }
);
```

#### Prettier 設定

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100,
  "tabWidth": 2,
  "endOfLine": "lf",
  "arrowParens": "always"
}
```

#### EditorConfig

```ini
# .editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
indent_size = 2
indent_style = space
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false
```

#### Husky + lint-staged

```bash
# 安裝
pnpm add -D husky lint-staged
npx husky init
```

```json
// package.json
{
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{json,md,yaml}": [
      "prettier --write"
    ]
  }
}
```

```bash
# .husky/pre-commit
pnpm exec lint-staged

# .husky/commit-msg
pnpm exec commitlint --edit $1
```

---

### 23.2 Conventional Commits

```bash
# 安裝 commitlint
pnpm add -D @commitlint/cli @commitlint/config-conventional

# commitlint.config.mjs
export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [2, 'always', [
      'feat',     // 新功能
      'fix',      // Bug 修復
      'docs',     // 文件
      'style',    // 格式調整
      'refactor', // 重構
      'perf',     // 效能
      'test',     // 測試
      'build',    // 建置
      'ci',       // CI/CD
      'chore',    // 雜項
      'revert',   // 還原
    ]],
    'subject-max-length': [2, 'always', 72],
  },
};
```

#### Commit 範例

```
feat(user): add cursor-based pagination for user list

- Implement cursor-based pagination using user.id
- Add PaginatedResponse<T> generic type
- Update OpenAPI docs

Closes #123
```

---

### 23.3 Git Flow 與分支策略

```mermaid
gitGraph
    commit id: "init"
    branch develop
    checkout develop
    commit id: "feat: user module"
    branch feature/order
    checkout feature/order
    commit id: "feat: order entity"
    commit id: "feat: order service"
    checkout develop
    merge feature/order
    branch release/1.0
    checkout release/1.0
    commit id: "chore: bump version"
    checkout main
    merge release/1.0 tag: "v1.0.0"
    checkout develop
    merge release/1.0
```

| 分支 | 用途 | 命名規則 |
|------|------|----------|
| `main` | 生產版本 | — |
| `develop` | 開發整合 | — |
| `feature/*` | 新功能 | `feature/user-auth` |
| `bugfix/*` | Bug 修復 | `bugfix/login-error` |
| `release/*` | 發佈準備 | `release/1.2.0` |
| `hotfix/*` | 緊急修復 | `hotfix/security-patch` |

---

### 23.4 Release 與版本策略

#### Semantic Versioning（SemVer）

```
MAJOR.MINOR.PATCH

- MAJOR：不相容的 API 變更
- MINOR：向下相容的新功能
- PATCH：向下相容的 Bug 修復
```

#### 自動化版本與 Changelog

```json
// package.json
{
  "scripts": {
    "release": "standard-version",
    "release:major": "standard-version --release-as major",
    "release:minor": "standard-version --release-as minor",
    "release:patch": "standard-version --release-as patch"
  }
}
```

```yaml
# .versionrc.json
{
  "types": [
    { "type": "feat", "section": "✨ Features" },
    { "type": "fix", "section": "🐛 Bug Fixes" },
    { "type": "perf", "section": "⚡ Performance" },
    { "type": "docs", "section": "📚 Documentation", "hidden": true },
    { "type": "chore", "hidden": true }
  ]
}
```

---

### 23.5 Code Review 流程

#### PR Review Checklist

```markdown
## Code Review Checklist

### 功能性
- [ ] 功能符合需求規格
- [ ] Edge cases 已處理
- [ ] 錯誤處理完整

### 程式碼品質
- [ ] 遵循專案 Coding Standard
- [ ] 型別安全（無 any、無 type assertion）
- [ ] 無重複程式碼
- [ ] 命名清楚有意義

### 安全性
- [ ] 輸入驗證（Zod DTO）
- [ ] 無硬編碼 Secret
- [ ] SQL 參數化查詢
- [ ] 權限檢查

### 測試
- [ ] Unit Test 涵蓋核心邏輯
- [ ] Integration Test 涵蓋 API
- [ ] Coverage >= 80%

### 文件
- [ ] API 文件已更新
- [ ] CHANGELOG 已更新
- [ ] README 已更新（如需要）
```

#### 章節小練習

1. 設定 ESLint + Prettier + Husky + lint-staged。
2. 建立 Conventional Commits 規範。
3. 建立 Code Review Checklist。

#### 實務注意事項

> - 統一團隊的 Coding Standard（ESLint + Prettier）
> - 使用 Husky + lint-staged 在 commit 前自動檢查
> - Conventional Commits 支援自動化 Changelog
> - Code Review 是品質保障的關鍵環節
> - 版本策略使用 SemVer

### 23.6 API 版本管理策略

```typescript
// 方法 1：URL Path Versioning（最常用）
// /api/v1/users, /api/v2/users

// NestJS 實作
import { VersioningType } from '@nestjs/common';

app.enableVersioning({
  type: VersioningType.URI,
  defaultVersion: '1',
  prefix: 'api/v',
});

@Controller('users')
export class UserControllerV1 {
  @Version('1')
  @Get()
  findAll() { /* v1 邏輯 */ }
}

@Controller('users')
export class UserControllerV2 {
  @Version('2')
  @Get()
  findAll() { /* v2 邏輯，包含額外欄位 */ }
}

// 方法 2：Header Versioning
app.enableVersioning({
  type: VersioningType.HEADER,
  header: 'X-API-Version',
});

// 方法 3：Content Negotiation
// Accept: application/vnd.myapp.v2+json
```

| 策略 | 優點 | 缺點 | 適用場景 |
|------|------|------|---------|
| **URL Path** | 直觀、易快取 | URL 冗長 | 公開 API |
| **Header** | URL 乾淨 | 不易測試 | 內部 API |
| **Query** | 簡單 | 不 RESTful | 過渡期 |
| **Content-Type** | 標準化 | 複雜 | 企業級 API |

---

### 23.7 Feature Flag 管理

```typescript
// 簡易 Feature Flag 實作
interface FeatureFlag {
  name: string;
  enabled: boolean;
  rolloutPercentage?: number;  // 灰度百分比
  allowedUsers?: string[];     // 白名單
  rules?: Array<{
    attribute: string;
    operator: 'eq' | 'in' | 'gte' | 'lte';
    value: unknown;
  }>;
}

@Injectable()
export class FeatureFlagService {
  private flags = new Map<string, FeatureFlag>();

  constructor(private readonly redis: RedisService) {
    this.loadFlags();
  }

  private async loadFlags() {
    const data = await this.redis.get('feature-flags');
    if (data) {
      const flags: FeatureFlag[] = JSON.parse(data);
      flags.forEach(f => this.flags.set(f.name, f));
    }
  }

  isEnabled(flagName: string, context?: { userId?: string; attributes?: Record<string, unknown> }): boolean {
    const flag = this.flags.get(flagName);
    if (!flag) return false;
    if (!flag.enabled) return false;

    // 白名單
    if (flag.allowedUsers?.length && context?.userId) {
      if (flag.allowedUsers.includes(context.userId)) return true;
    }

    // 灰度發布
    if (flag.rolloutPercentage !== undefined && context?.userId) {
      const hash = this.hashUserId(context.userId);
      return hash % 100 < flag.rolloutPercentage;
    }

    return flag.enabled;
  }

  private hashUserId(userId: string): number {
    let hash = 0;
    for (const char of userId) {
      hash = (hash * 31 + char.charCodeAt(0)) & 0x7fffffff;
    }
    return hash;
  }
}

// Guard：基於 Feature Flag 的路由保護
@Injectable()
export class FeatureFlagGuard implements CanActivate {
  constructor(
    private readonly reflector: Reflector,
    private readonly featureFlags: FeatureFlagService,
  ) {}

  canActivate(context: ExecutionContext): boolean {
    const flag = this.reflector.get<string>('feature-flag', context.getHandler());
    if (!flag) return true;

    const request = context.switchToHttp().getRequest();
    return this.featureFlags.isEnabled(flag, { userId: request.user?.id });
  }
}

// 使用
@FeatureFlag('new-checkout-flow')
@Post('checkout/v2')
async newCheckout(@Body() dto: CheckoutDto) { /* ... */ }
```

---

### 23.8 國際化（i18n）

```typescript
// 使用 nestjs-i18n
import { I18nModule, I18nService, I18nContext } from 'nestjs-i18n';
import * as path from 'node:path';

@Module({
  imports: [
    I18nModule.forRoot({
      fallbackLanguage: 'zh-TW',
      loaderOptions: {
        path: path.join(__dirname, '/i18n/'),
        watch: true,
      },
      resolvers: [
        { use: HeaderResolver, options: ['Accept-Language'] },
        { use: QueryResolver, options: ['lang'] },
      ],
    }),
  ],
})
export class AppModule {}

// i18n/zh-TW/common.json
{
  "validation": {
    "required": "{field} 為必填欄位",
    "min_length": "{field} 長度不得少於 {min} 個字元",
    "email": "請輸入有效的 Email 地址"
  },
  "error": {
    "not_found": "找不到 {resource}",
    "unauthorized": "請先登入",
    "forbidden": "您沒有權限執行此操作"
  }
}

// i18n/en/common.json
{
  "validation": {
    "required": "{field} is required",
    "min_length": "{field} must be at least {min} characters",
    "email": "Please enter a valid email address"
  }
}

// Controller 使用
@Get(':id')
async findOne(@Param('id') id: string, @I18n() i18n: I18nContext) {
  const user = await this.userService.findById(id);
  if (!user) {
    throw new NotFoundException(
      i18n.t('common.error.not_found', { args: { resource: 'User' } })
    );
  }
  return user;
}
```

---

## 第 24 章：完整企業級範例專案

### 24.1 專案概覽

建立一個企業級「訂單管理系統」REST API，整合本手冊所有技術要點。

```
enterprise-order-api/
├── apps/
│   └── api/
│       ├── src/
│       │   ├── main.ts
│       │   ├── app.module.ts
│       │   ├── common/
│       │   │   ├── decorators/
│       │   │   ├── filters/
│       │   │   │   └── global-exception.filter.ts
│       │   │   ├── guards/
│       │   │   │   ├── jwt-auth.guard.ts
│       │   │   │   └── roles.guard.ts
│       │   │   ├── interceptors/
│       │   │   │   └── logging.interceptor.ts
│       │   │   └── pipes/
│       │   │       └── zod-validation.pipe.ts
│       │   ├── modules/
│       │   │   ├── auth/
│       │   │   │   ├── auth.module.ts
│       │   │   │   ├── auth.controller.ts
│       │   │   │   ├── auth.service.ts
│       │   │   │   └── strategies/
│       │   │   ├── user/
│       │   │   │   ├── user.module.ts
│       │   │   │   ├── user.controller.ts
│       │   │   │   ├── user.service.ts
│       │   │   │   ├── user.repository.ts
│       │   │   │   └── dto/
│       │   │   │       ├── create-user.dto.ts
│       │   │   │       └── update-user.dto.ts
│       │   │   ├── order/
│       │   │   │   ├── order.module.ts
│       │   │   │   ├── order.controller.ts
│       │   │   │   ├── order.service.ts
│       │   │   │   ├── order.repository.ts
│       │   │   │   └── dto/
│       │   │   └── product/
│       │   └── config/
│       │       ├── app.config.ts
│       │       └── database.config.ts
│       ├── test/
│       │   ├── unit/
│       │   ├── integration/
│       │   └── e2e/
│       ├── Dockerfile
│       └── tsconfig.json
├── packages/
│   ├── database/
│   │   └── prisma/
│   │       └── schema.prisma
│   └── shared/
│       └── src/
│           ├── types/
│           └── utils/
├── docker-compose.yml
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
├── .github/
│   └── workflows/
│       └── ci.yaml
├── turbo.json
├── pnpm-workspace.yaml
└── package.json
```

---

### 24.2 NestJS API 核心

```typescript
// apps/api/src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module.js';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { Logger } from 'nestjs-pino';
import helmet from 'helmet';

async function bootstrap() {
  const app = await NestFactory.create(AppModule, { bufferLogs: true });
  
  // Pino Logger
  app.useLogger(app.get(Logger));
  
  // Security
  app.use(helmet());
  app.enableCors({
    origin: process.env.CORS_ORIGINS?.split(','),
    credentials: true,
  });
  
  // Global Prefix
  app.setGlobalPrefix('api/v1');
  
  // Swagger
  const config = new DocumentBuilder()
    .setTitle('Order Management API')
    .setVersion('1.0.0')
    .addBearerAuth()
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('docs', app, document);
  
  // Graceful Shutdown
  app.enableShutdownHooks();
  
  const port = process.env.PORT ?? 3000;
  await app.listen(port);
}

bootstrap();
```

---

### 24.3 認證模組

```typescript
// modules/auth/auth.service.ts
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  constructor(
    private readonly jwtService: JwtService,
    private readonly userService: UserService,
    private readonly redis: RedisService,
  ) {}

  async login(email: string, password: string) {
    const user = await this.userService.findByEmail(email);
    if (!user) throw new UnauthorizedException('Invalid credentials');

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) throw new UnauthorizedException('Invalid credentials');

    const payload = { sub: user.id, email: user.email, role: user.role };
    const accessToken = this.jwtService.sign(payload, { expiresIn: '15m' });
    const refreshToken = this.jwtService.sign(
      { sub: user.id, type: 'refresh' },
      { expiresIn: '7d' }
    );

    // 儲存 Refresh Token 到 Redis
    await this.redis.setex(`refresh:${user.id}`, 7 * 86400, refreshToken);

    return { accessToken, refreshToken };
  }

  async refresh(refreshToken: string) {
    const payload = this.jwtService.verify(refreshToken);
    const stored = await this.redis.get(`refresh:${payload.sub}`);
    
    if (stored !== refreshToken) {
      throw new UnauthorizedException('Invalid refresh token');
    }

    const user = await this.userService.findById(payload.sub);
    if (!user) throw new UnauthorizedException('User not found');

    return this.login(user.email, user.passwordHash);
  }
}
```

---

### 24.4 Prisma Schema

```prisma
// packages/database/prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id           String   @id @default(uuid())
  email        String   @unique
  passwordHash String   @map("password_hash")
  name         String
  role         Role     @default(USER)
  orders       Order[]
  createdAt    DateTime @default(now()) @map("created_at")
  updatedAt    DateTime @updatedAt @map("updated_at")
  
  @@map("users")
}

model Product {
  id          String      @id @default(uuid())
  name        String
  description String?
  price       Decimal     @db.Decimal(10, 2)
  stock       Int         @default(0)
  orderItems  OrderItem[]
  createdAt   DateTime    @default(now()) @map("created_at")
  
  @@map("products")
}

model Order {
  id        String      @id @default(uuid())
  userId    String      @map("user_id")
  user      User        @relation(fields: [userId], references: [id])
  items     OrderItem[]
  total     Decimal     @db.Decimal(10, 2)
  status    OrderStatus @default(PENDING)
  createdAt DateTime    @default(now()) @map("created_at")
  updatedAt DateTime    @updatedAt @map("updated_at")
  
  @@map("orders")
  @@index([userId])
  @@index([status])
}

model OrderItem {
  id        String  @id @default(uuid())
  orderId   String  @map("order_id")
  order     Order   @relation(fields: [orderId], references: [id])
  productId String  @map("product_id")
  product   Product @relation(fields: [productId], references: [id])
  quantity  Int
  price     Decimal @db.Decimal(10, 2)
  
  @@map("order_items")
}

enum Role {
  ADMIN
  USER
}

enum OrderStatus {
  PENDING
  CONFIRMED
  SHIPPED
  DELIVERED
  CANCELLED
}
```

---

### 24.5 Redis 快取與 BullMQ 工作佇列

```typescript
// 快取服務
@Injectable()
export class CacheService {
  constructor(private readonly redis: RedisService) {}

  async getOrSet<T>(key: string, ttl: number, factory: () => Promise<T>): Promise<T> {
    const cached = await this.redis.get(key);
    if (cached) return JSON.parse(cached);

    const value = await factory();
    await this.redis.setex(key, ttl, JSON.stringify(value));
    return value;
  }

  async invalidate(pattern: string): Promise<void> {
    const keys = await this.redis.keys(pattern);
    if (keys.length > 0) {
      await this.redis.del(...keys);
    }
  }
}

// BullMQ 工作佇列
import { Queue, Worker } from 'bullmq';

const orderQueue = new Queue('order-processing', {
  connection: { host: 'localhost', port: 6379 },
});

// 生產者
async function processOrder(orderId: string) {
  await orderQueue.add('process', { orderId }, {
    attempts: 3,
    backoff: { type: 'exponential', delay: 1000 },
  });
}

// 消費者
const worker = new Worker('order-processing', async (job) => {
  const { orderId } = job.data;
  
  // 處理訂單邏輯
  await updateInventory(orderId);
  await sendConfirmationEmail(orderId);
  await notifyWarehouse(orderId);
}, {
  connection: { host: 'localhost', port: 6379 },
  concurrency: 5,
});
```

---

### 24.6 Docker Compose（完整開發環境）

```yaml
# docker-compose.yml
services:
  api:
    build:
      context: .
      dockerfile: apps/api/Dockerfile
      target: development
    ports:
      - "3000:3000"
      - "9229:9229"
    volumes:
      - ./apps/api/src:/app/apps/api/src
      - ./packages:/app/packages
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/orders
      - REDIS_URL=redis://redis:6379
      - JWT_SECRET=dev-secret-key-change-in-production
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    command: pnpm --filter api dev

  db:
    image: postgres:16-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: orders
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
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

  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

volumes:
  pgdata:
```

---

### 24.7 GitHub Actions CI/CD

```yaml
# .github/workflows/ci.yaml
name: CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with:
          node-version: 26
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm run lint
      - run: pnpm exec tsc --noEmit
      - run: pnpm test -- --coverage
      - run: pnpm audit --audit-level=high

  build-deploy:
    needs: quality
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/build-push-action@v5
        with:
          context: .
          file: apps/api/Dockerfile
          push: true
          tags: ghcr.io/${{ github.repository }}/api:${{ github.sha }}
      - name: Deploy
        run: kubectl set image deployment/api api=ghcr.io/${{ github.repository }}/api:${{ github.sha }}
```

---

### 24.8 監控與 Logging 整合

```typescript
// src/config/telemetry.ts
// 整合 OpenTelemetry + Pino + Prometheus
// （參考 Ch18 的完整設定）

// src/common/interceptors/logging.interceptor.ts
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  private readonly logger = new Logger(LoggingInterceptor.name);

  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const request = context.switchToHttp().getRequest();
    const { method, url } = request;
    const now = Date.now();

    return next.handle().pipe(
      tap(() => {
        const response = context.switchToHttp().getResponse();
        this.logger.log({
          method,
          url,
          statusCode: response.statusCode,
          duration: `${Date.now() - now}ms`,
        });
      }),
    );
  }
}
```

#### 章節小練習

1. 使用本章範例建立完整的企業級 API 專案。
2. 設定 Docker Compose 開發環境，一鍵啟動。
3. 建立 GitHub Actions CI/CD Pipeline。

#### 實務注意事項

> - 使用 Monorepo（Turborepo + pnpm workspace）管理多套件
> - Prisma Schema 統一在 `packages/database` 中管理
> - 認證使用 JWT Access + Refresh Token
> - 長時間任務使用 BullMQ 工作佇列
> - 開發環境使用 Docker Compose 一鍵啟動

### 24.9 Order Module 完整實作

```typescript
// modules/order/dto/create-order.dto.ts
import { z } from 'zod';

export const CreateOrderSchema = z.object({
  items: z.array(z.object({
    productId: z.string().uuid(),
    quantity: z.number().int().positive().max(100),
  })).min(1).max(50),
  shippingAddress: z.string().min(10).max(500),
  note: z.string().max(1000).optional(),
});

export type CreateOrderDto = z.infer<typeof CreateOrderSchema>;

// modules/order/order.controller.ts
@Controller('orders')
@UseGuards(JwtAuthGuard)
@ApiTags('Orders')
export class OrderController {
  constructor(private readonly orderService: OrderService) {}

  @Post()
  @ApiOperation({ summary: '建立訂單' })
  @ApiResponse({ status: 201, type: OrderResponseDto })
  async create(
    @CurrentUser() user: UserPayload,
    @Body(new ZodValidationPipe(CreateOrderSchema)) dto: CreateOrderDto,
  ) {
    return this.orderService.create(user.id, dto);
  }

  @Get()
  @ApiOperation({ summary: '查詢我的訂單' })
  async findMyOrders(
    @CurrentUser() user: UserPayload,
    @Query('cursor') cursor?: string,
    @Query('limit', new DefaultValuePipe(20), ParseIntPipe) limit?: number,
  ) {
    return this.orderService.findByUserId(user.id, { cursor, limit: limit! });
  }

  @Get(':id')
  @ApiOperation({ summary: '查詢訂單詳情' })
  async findOne(
    @CurrentUser() user: UserPayload,
    @Param('id', ParseUUIDPipe) id: string,
  ) {
    const order = await this.orderService.findById(id);
    if (order.userId !== user.id && user.role !== 'ADMIN') {
      throw new ForbiddenException('Access denied');
    }
    return order;
  }

  @Patch(':id/cancel')
  @ApiOperation({ summary: '取消訂單' })
  async cancel(
    @CurrentUser() user: UserPayload,
    @Param('id', ParseUUIDPipe) id: string,
  ) {
    return this.orderService.cancel(user.id, id);
  }
}

// modules/order/order.service.ts
@Injectable()
export class OrderService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly cacheService: CacheService,
    private readonly eventBus: EventBus,
    @InjectQueue('order-processing') private readonly orderQueue: Queue,
  ) {}

  async create(userId: string, dto: CreateOrderDto) {
    // 互動式 Transaction
    const order = await this.prisma.$transaction(async (tx) => {
      // 1. 檢查庫存
      const products = await tx.product.findMany({
        where: { id: { in: dto.items.map(i => i.productId) } },
      });

      for (const item of dto.items) {
        const product = products.find(p => p.id === item.productId);
        if (!product) throw new NotFoundException(`Product ${item.productId} not found`);
        if (product.stock < item.quantity) {
          throw new UnprocessableEntityException(`Insufficient stock for ${product.name}`);
        }
      }

      // 2. 計算總金額
      const total = dto.items.reduce((sum, item) => {
        const product = products.find(p => p.id === item.productId)!;
        return sum + Number(product.price) * item.quantity;
      }, 0);

      // 3. 建立訂單
      const order = await tx.order.create({
        data: {
          userId,
          total,
          items: {
            create: dto.items.map(item => ({
              productId: item.productId,
              quantity: item.quantity,
              price: products.find(p => p.id === item.productId)!.price,
            })),
          },
        },
        include: { items: { include: { product: true } } },
      });

      // 4. 扣減庫存
      for (const item of dto.items) {
        await tx.product.update({
          where: { id: item.productId },
          data: { stock: { decrement: item.quantity } },
        });
      }

      return order;
    });

    // 5. 非同步處理（發送確認信、通知倉庫等）
    await this.orderQueue.add('process-order', {
      orderId: order.id,
      userId,
    });

    // 6. 發佈 Domain Event
    this.eventBus.publish(new OrderCreatedEvent(order.id, userId, order.total));

    // 7. 清除快取
    await this.cacheService.invalidate(`orders:${userId}:*`);

    return order;
  }

  async findByUserId(userId: string, pagination: { cursor?: string; limit: number }) {
    return this.cacheService.getOrSet(
      `orders:${userId}:${pagination.cursor ?? 'first'}:${pagination.limit}`,
      300,
      async () => {
        const orders = await this.prisma.order.findMany({
          where: { userId },
          take: pagination.limit + 1,
          ...(pagination.cursor ? { cursor: { id: pagination.cursor }, skip: 1 } : {}),
          orderBy: { createdAt: 'desc' },
          include: { items: { include: { product: true } } },
        });

        const hasMore = orders.length > pagination.limit;
        const data = hasMore ? orders.slice(0, -1) : orders;

        return {
          data,
          cursor: hasMore ? data[data.length - 1].id : null,
          hasMore,
        };
      },
    );
  }

  async cancel(userId: string, orderId: string) {
    const order = await this.prisma.order.findUnique({
      where: { id: orderId },
      include: { items: true },
    });

    if (!order) throw new NotFoundException('Order not found');
    if (order.userId !== userId) throw new ForbiddenException('Access denied');
    if (order.status !== 'PENDING') {
      throw new UnprocessableEntityException('Only pending orders can be cancelled');
    }

    // Transaction：取消訂單 + 恢復庫存
    await this.prisma.$transaction(async (tx) => {
      await tx.order.update({
        where: { id: orderId },
        data: { status: 'CANCELLED' },
      });

      for (const item of order.items) {
        await tx.product.update({
          where: { id: item.productId },
          data: { stock: { increment: item.quantity } },
        });
      }
    });

    await this.cacheService.invalidate(`orders:${userId}:*`);
    this.eventBus.publish(new OrderCancelledEvent(orderId, userId));
  }
}
```

---

### 24.10 完整測試範例

```typescript
// test/unit/order.service.spec.ts
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { OrderService } from '../../src/modules/order/order.service.js';

describe('OrderService', () => {
  let service: OrderService;
  let mockPrisma: DeepMockProxy<PrismaClient>;
  let mockCache: MockProxy<CacheService>;
  let mockEventBus: MockProxy<EventBus>;
  let mockQueue: MockProxy<Queue>;

  beforeEach(() => {
    mockPrisma = mockDeep<PrismaClient>();
    mockCache = mock<CacheService>();
    mockEventBus = mock<EventBus>();
    mockQueue = mock<Queue>();
    service = new OrderService(mockPrisma, mockCache, mockEventBus, mockQueue);
  });

  describe('create', () => {
    const userId = 'user-1';
    const dto = {
      items: [{ productId: 'prod-1', quantity: 2 }],
      shippingAddress: '台北市信義區某路 100 號',
    };

    it('should create order and deduct stock', async () => {
      const mockProduct = { id: 'prod-1', name: 'Widget', price: 100, stock: 10 };
      const mockOrder = { id: 'order-1', userId, total: 200, status: 'PENDING', items: [] };

      mockPrisma.$transaction.mockImplementation(async (fn) => fn(mockPrisma));
      mockPrisma.product.findMany.mockResolvedValue([mockProduct]);
      mockPrisma.order.create.mockResolvedValue(mockOrder);
      mockPrisma.product.update.mockResolvedValue({ ...mockProduct, stock: 8 });
      mockQueue.add.mockResolvedValue({} as any);

      const result = await service.create(userId, dto);

      expect(result.total).toBe(200);
      expect(mockPrisma.product.update).toHaveBeenCalledWith(
        expect.objectContaining({
          data: { stock: { decrement: 2 } },
        })
      );
      expect(mockQueue.add).toHaveBeenCalledWith('process-order', expect.any(Object));
      expect(mockEventBus.publish).toHaveBeenCalled();
    });

    it('should throw when product not found', async () => {
      mockPrisma.$transaction.mockImplementation(async (fn) => fn(mockPrisma));
      mockPrisma.product.findMany.mockResolvedValue([]);

      await expect(service.create(userId, dto)).rejects.toThrow('not found');
    });

    it('should throw when insufficient stock', async () => {
      const mockProduct = { id: 'prod-1', name: 'Widget', price: 100, stock: 1 };
      mockPrisma.$transaction.mockImplementation(async (fn) => fn(mockPrisma));
      mockPrisma.product.findMany.mockResolvedValue([mockProduct]);

      await expect(service.create(userId, dto)).rejects.toThrow('Insufficient stock');
    });
  });

  describe('cancel', () => {
    it('should cancel pending order and restore stock', async () => {
      const order = {
        id: 'order-1', userId: 'user-1', status: 'PENDING',
        items: [{ productId: 'prod-1', quantity: 2, price: 100 }],
      };
      
      mockPrisma.order.findUnique.mockResolvedValue(order as any);
      mockPrisma.$transaction.mockImplementation(async (fn) => fn(mockPrisma));

      await service.cancel('user-1', 'order-1');

      expect(mockPrisma.order.update).toHaveBeenCalledWith(
        expect.objectContaining({ data: { status: 'CANCELLED' } })
      );
      expect(mockPrisma.product.update).toHaveBeenCalledWith(
        expect.objectContaining({ data: { stock: { increment: 2 } } })
      );
    });

    it('should reject cancellation of non-pending order', async () => {
      const order = { id: 'order-1', userId: 'user-1', status: 'SHIPPED', items: [] };
      mockPrisma.order.findUnique.mockResolvedValue(order as any);

      await expect(service.cancel('user-1', 'order-1')).rejects.toThrow('Only pending orders');
    });
  });
});

// test/integration/order.api.spec.ts
import request from 'supertest';

describe('Order API Integration', () => {
  let app: INestApplication;
  let authToken: string;

  beforeAll(async () => {
    const module = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = module.createNestApplication();
    app.setGlobalPrefix('api/v1');
    await app.init();

    // 取得 Token
    const res = await request(app.getHttpServer())
      .post('/api/v1/auth/login')
      .send({ email: 'test@example.com', password: 'Test1234!' });
    authToken = res.body.accessToken;
  });

  afterAll(async () => {
    await app.close();
  });

  describe('POST /api/v1/orders', () => {
    it('should create order', async () => {
      const res = await request(app.getHttpServer())
        .post('/api/v1/orders')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          items: [{ productId: 'prod-1', quantity: 1 }],
          shippingAddress: '台北市信義區某路 100 號',
        })
        .expect(201);

      expect(res.body).toHaveProperty('id');
      expect(res.body.status).toBe('PENDING');
    });

    it('should return 401 without auth', async () => {
      await request(app.getHttpServer())
        .post('/api/v1/orders')
        .send({ items: [] })
        .expect(401);
    });

    it('should return 400 for empty items', async () => {
      await request(app.getHttpServer())
        .post('/api/v1/orders')
        .set('Authorization', `Bearer ${authToken}`)
        .send({ items: [], shippingAddress: '台北市' })
        .expect(400);
    });
  });
});
```

---

## 第 25 章：附錄

### 25.1 CLI 常用指令速查表

#### Node.js / npm / pnpm

| 指令 | 說明 |
|------|------|
| `node -v` | 查看 Node.js 版本 |
| `node --run <script>` | 執行 package.json 中的腳本（Node.js 22+） |
| `pnpm init` | 初始化專案 |
| `pnpm add <pkg>` | 安裝依賴 |
| `pnpm add -D <pkg>` | 安裝開發依賴 |
| `pnpm remove <pkg>` | 移除依賴 |
| `pnpm install --frozen-lockfile` | CI 安裝（鎖定版本） |
| `pnpm update --interactive` | 互動式更新依賴 |
| `pnpm audit` | 安全稽核 |
| `pnpm exec <cmd>` | 執行本地安裝的指令 |
| `npx <cmd>` | 執行套件指令 |
| `corepack enable` | 啟用 Corepack |

#### Prisma

| 指令 | 說明 |
|------|------|
| `npx prisma init` | 初始化 Prisma |
| `npx prisma generate` | 產生 Client |
| `npx prisma migrate dev --name <name>` | 建立 Migration |
| `npx prisma migrate deploy` | 部署 Migration |
| `npx prisma studio` | 資料庫視覺化工具 |
| `npx prisma db push` | 直接同步 Schema（開發用） |

#### Docker

| 指令 | 說明 |
|------|------|
| `docker build -t <name> .` | 建置映像 |
| `docker run -p 3000:3000 <name>` | 執行容器 |
| `docker compose up -d` | 啟動所有服務 |
| `docker compose down` | 停止所有服務 |
| `docker compose logs -f <service>` | 查看服務日誌 |
| `docker scout cves <image>` | 漏洞掃描 |

#### Kubernetes

| 指令 | 說明 |
|------|------|
| `kubectl apply -f <file>` | 套用設定 |
| `kubectl get pods` | 查看 Pod 狀態 |
| `kubectl logs <pod>` | 查看 Pod 日誌 |
| `kubectl describe pod <pod>` | 查看 Pod 詳情 |
| `kubectl rollout status deployment/<name>` | 查看部署狀態 |
| `kubectl rollout undo deployment/<name>` | 回滾部署 |

---

### 25.2 Debug 技巧

#### VS Code Debug 設定

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug API",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "pnpm",
      "runtimeArgs": ["run", "dev"],
      "skipFiles": ["<node_internals>/**"],
      "env": {
        "NODE_ENV": "development"
      }
    },
    {
      "name": "Debug Tests",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "pnpm",
      "runtimeArgs": ["test"],
      "skipFiles": ["<node_internals>/**"]
    },
    {
      "name": "Attach to Process",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "restart": true
    }
  ]
}
```

#### 常用 Debug 指令

```bash
# 啟動 Inspector
node --inspect dist/main.js
node --inspect-brk dist/main.js   # 在第一行斷點

# 使用 Chrome DevTools
# 開啟 chrome://inspect

# 環境變數 Debug
NODE_DEBUG=http,net node dist/main.js
```

---

### 25.3 VS Code 推薦設定

```json
// .vscode/settings.json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "explicit"
  },
  "typescript.preferences.importModuleSpecifier": "relative",
  "typescript.tsdk": "node_modules/typescript/lib",
  "files.eol": "\n",
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

```json
// .vscode/extensions.json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "prisma.prisma",
    "ms-azuretools.vscode-docker",
    "bradlc.vscode-tailwindcss",
    "humao.rest-client",
    "github.copilot",
    "github.copilot-chat"
  ]
}
```

---

### 25.4 推薦套件與學習資源

#### 依分類推薦套件

| 分類 | 套件 | 說明 |
|------|------|------|
| **Web 框架** | Express, Fastify, NestJS | 依專案規模選擇 |
| **ORM** | Prisma, Drizzle | 型別安全 ORM |
| **驗證** | Zod, Valibot | Schema 驗證 |
| **測試** | Vitest, Playwright | 測試框架 |
| **日誌** | Pino, Winston | 結構化日誌 |
| **認證** | passport, jsonwebtoken | JWT 認證 |
| **工作佇列** | BullMQ | Redis-based Queue |
| **快取** | ioredis | Redis 客戶端 |
| **API 文件** | @nestjs/swagger | OpenAPI |
| **監控** | prom-client, @opentelemetry/* | 可觀測性 |
| **安全** | helmet, express-rate-limit | HTTP 安全 |
| **工具** | tsx, c8, autocannon | 開發工具 |

#### 學習資源

| 資源 | 類型 | 網址 |
|------|------|------|
| **Node.js 官方文件** | 文件 | https://nodejs.org/docs |
| **TypeScript Handbook** | 文件 | https://www.typescriptlang.org/docs |
| **NestJS 官方文件** | 文件 | https://docs.nestjs.com |
| **Prisma 官方文件** | 文件 | https://www.prisma.io/docs |
| **Node.js Best Practices** | GitHub | https://github.com/goldbergyoni/nodebestpractices |
| **The Node.js Event Loop** | 文章 | Node.js 官方 Blog |

---

### 附錄 A：開發環境建置 Checklist

- [ ] 安裝 Node.js v26 LTS
- [ ] 安裝 VS Code + 推薦擴充套件
- [ ] 設定 Corepack 啟用 pnpm
- [ ] 設定 Git Hooks（Husky + lint-staged）
- [ ] 設定 ESLint + Prettier
- [ ] 設定 EditorConfig
- [ ] 建立 `.env.example` 範本

### 附錄 B：專案啟動 Checklist

- [ ] 初始化 Monorepo（Turborepo + pnpm workspace）
- [ ] 建立 Prisma Schema 並執行 Migration
- [ ] 設定 Docker Compose 開發環境
- [ ] 設定 CI/CD Pipeline（GitHub Actions）
- [ ] 建立 Swagger API 文件
- [ ] 設定測試框架（Vitest）
- [ ] 設定日誌（Pino + OpenTelemetry）

### 附錄 C：上線前 Checklist

- [ ] 所有測試通過（Coverage >= 80%）
- [ ] 安全掃描通過（npm audit, Snyk, CodeQL）
- [ ] Docker Image 漏洞掃描通過
- [ ] Graceful Shutdown 實作完成
- [ ] Health Check 端點就緒
- [ ] 監控告警規則設定完成
- [ ] API 文件更新完畢
- [ ] 環境變數確認（無硬編碼 Secret）
- [ ] Rate Limiting 設定完成
- [ ] CORS 設定正確

### 附錄 D：效能調校 Checklist

- [ ] Event Loop Lag < 100ms
- [ ] Heap 記憶體無持續增長趨勢
- [ ] 連線池大小適當
- [ ] 熱資料已啟用 Redis 快取
- [ ] 大型回應啟用壓縮（gzip/brotli）
- [ ] 資料庫查詢已建立索引
- [ ] N+1 查詢問題已解決

### 附錄 E：安全性 Checklist

- [ ] HTTPS 全站啟用
- [ ] Helmet 設定完成
- [ ] CORS 白名單設定
- [ ] Rate Limiting 啟用
- [ ] 輸入驗證（Zod）
- [ ] SQL 參數化查詢
- [ ] JWT 短效期 + Refresh Token
- [ ] 密碼使用 bcrypt/argon2 雜湊
- [ ] 敏感日誌遮蔽
- [ ] Secret 管理（非硬編碼）
- [ ] 依賴定期更新並掃描

---

> **文件版本**：v2026.06
> **最後更新**：2026 年 6 月
> **適用版本**：Node.js v26.x LTS
> **授權**：內部教學使用
