+++
date = '2026-02-04T19:13:19+08:00'
draft = false
title = 'Node.js生態系教學手冊'
tags = ['教學', 'framework']
categories = ['教學']
+++

# Node.js 生態系教學手冊

> **版本**：2026.02  
> **適用對象**：具備基礎程式能力，準備參與 Web Application 或 Backend API 專案開發的工程師  
> **定位**：實務導向、架構導向、企業導向的內部技術文件

---

## 目錄

### [第 1 章：Node.js 與生態系總覽](#第-1-章nodejs-與生態系總覽)
- [1.1 Node.js 是什麼？適合解決什麼問題？](#11-nodejs-是什麼適合解決什麼問題)
- [1.2 與 Java / Spring Boot、Python / FastAPI 的差異](#12-與-java--spring-bootpython--fastapi-的差異)
- [1.3 Node.js 在企業系統中的常見使用場景](#13-nodejs-在企業系統中的常見使用場景)
- [1.4 單體、微服務、Serverless 架構定位](#14-單體微服務serverless-架構定位)

### [第 2 章：Node.js 核心基礎](#第-2-章nodejs-核心基礎)
- [2.1 Node.js 執行模型（Event Loop、Non-blocking I/O）](#21-nodejs-執行模型event-loopnon-blocking-io)
- [2.2 CommonJS vs ES Modules](#22-commonjs-vs-es-modules)
- [2.3 NPM、Yarn、PNPM 生態比較](#23-npmyarnpnpm-生態比較)
- [2.4 專案目錄結構最佳實務](#24-專案目錄結構最佳實務)

### [第 3 章：TypeScript 在 Node.js 的標準用法](#第-3-章typescript-在-nodejs-的標準用法)
- [3.1 為什麼企業專案一定要用 TypeScript](#31-為什麼企業專案一定要用-typescript)
- [3.2 tsconfig 設計原則](#32-tsconfig-設計原則)
- [3.3 型別設計與 Domain Model](#33-型別設計與-domain-model)
- [3.4 常見反模式與避坑指南](#34-常見反模式與避坑指南)

### [第 4 章：Web Framework 生態系](#第-4-章web-framework-生態系)
- [4.1 Express（歷史定位與限制）](#41-express歷史定位與限制)
- [4.2 Fastify（高效能）](#42-fastify高效能)
- [4.3 NestJS（企業級主流）](#43-nestjs企業級主流)
- [4.4 Framework 選型建議與比較表](#44-framework-選型建議與比較表)

### [第 5 章：RESTful API 與 Backend 架構設計](#第-5-章restful-api-與-backend-架構設計)
- [5.1 Controller / Service / Repository 分層](#51-controller--service--repository-分層)
- [5.2 DTO、Validation、Error Handling 設計](#52-dtovalidationerror-handling-設計)
- [5.3 OpenAPI / Swagger 文件化](#53-openapi--swagger-文件化)
- [5.4 Clean Architecture / Hexagonal Architecture 應用](#54-clean-architecture--hexagonal-architecture-應用)

### [第 6 章：非同步處理與背景任務](#第-6-章非同步處理與背景任務)
- [6.1 async / await 正確使用方式](#61-async--await-正確使用方式)
- [6.2 Queue（BullMQ / RabbitMQ / Kafka）](#62-queuebullmq--rabbitmq--kafka)
- [6.3 排程任務（cron）](#63-排程任務cron)
- [6.4 長時間任務設計原則](#64-長時間任務設計原則)

### [第 7 章：資料庫與 ORM / Query Builder](#第-7-章資料庫與-orm--query-builder)
- [7.1 PostgreSQL / MySQL / MongoDB 使用場景](#71-postgresql--mysql--mongodb-使用場景)
- [7.2 Prisma / TypeORM / Sequelize 比較](#72-prisma--typeorm--sequelize-比較)
- [7.3 Transaction、Migration、效能調校](#73-transactionmigration效能調校)
- [7.4 連線池與資源管理](#74-連線池與資源管理)

### [第 8 章：快取與效能優化](#第-8-章快取與效能優化)
- [8.1 Redis 使用場景](#81-redis-使用場景)
- [8.2 HTTP Cache / CDN](#82-http-cache--cdn)
- [8.3 Rate Limit](#83-rate-limit)
- [8.4 Memory Leak 與效能監控](#84-memory-leak-與效能監控)

### [第 9 章：安全性設計](#第-9-章安全性設計)
- [9.1 身分驗證（JWT / OAuth2 / OIDC）](#91-身分驗證jwt--oauth2--oidc)
- [9.2 API Security Best Practices](#92-api-security-best-practices)
- [9.3 資料驗證與 Injection 防護](#93-資料驗證與-injection-防護)
- [9.4 Secrets 管理與環境變數設計](#94-secrets-管理與環境變數設計)

### [第 10 章：測試策略](#第-10-章測試策略)
- [10.1 單元測試（Jest / Vitest）](#101-單元測試jest--vitest)
- [10.2 整合測試（Supertest）](#102-整合測試supertest)
- [10.3 Test Pyramid](#103-test-pyramid)
- [10.4 Mock / Stub 使用時機](#104-mock--stub-使用時機)

### [第 11 章：Logging、Monitoring 與 Observability](#第-11-章loggingmonitoring-與-observability)
- [11.1 Logging 設計原則（Winston / Pino）](#111-logging-設計原則winston--pino)
- [11.2 Metrics 與 Tracing（OpenTelemetry）](#112-metrics-與-tracingopentelemetry)
- [11.3 錯誤追蹤（如 Sentry）](#113-錯誤追蹤如-sentry)
- [11.4 生產環境可觀測性設計](#114-生產環境可觀測性設計)

### [第 12 章：DevOps 與部署](#第-12-章devops-與部署)
- [12.1 Node.js Build 與 Release 流程](#121-nodejs-build-與-release-流程)
- [12.2 Docker 化最佳實務](#122-docker-化最佳實務)
- [12.3 CI/CD Pipeline 設計](#123-cicd-pipeline-設計)
- [12.4 Kubernetes / Cloud Run / Serverless 部署模式](#124-kubernetes--cloud-run--serverless-部署模式)

### [第 13 章：專案範本與團隊開發規範](#第-13-章專案範本與團隊開發規範)
- [13.1 企業級 Node.js 專案範本建議](#131-企業級-nodejs-專案範本建議)
- [13.2 Coding Style 與 Lint 規範](#132-coding-style-與-lint-規範)
- [13.3 Git Flow / Branch Strategy](#133-git-flow--branch-strategy)
- [13.4 Code Review 重點清單](#134-code-review-重點清單)

### [第 14 章：常見地雷與反模式](#第-14-章常見地雷與反模式)
- [14.1 阻塞 Event Loop 的錯誤寫法](#141-阻塞-event-loop-的錯誤寫法)
- [14.2 Promise 使用錯誤](#142-promise-使用錯誤)
- [14.3 TypeScript 濫用 any](#143-typescript-濫用-any)
- [14.4 設計不良的 API 與資料模型](#144-設計不良的-api-與資料模型)

### [第 15 章：總結與最佳實務建議](#第-15-章總結與最佳實務建議)
- [15.1 Node.js 在企業長期維運的關鍵成功因素](#151-nodejs-在企業長期維運的關鍵成功因素)
- [15.2 技術選型決策建議](#152-技術選型決策建議)
- [15.3 學習路線與進階主題建議](#153-學習路線與進階主題建議)

### [附錄：檢查清單（Checklist）](#附錄檢查清單checklist)
- [A. 新專案啟動檢查清單](#a-新專案啟動檢查清單)
- [B. Code Review 檢查清單](#b-code-review-檢查清單)
- [C. 上線前檢查清單](#c-上線前檢查清單)
- [D. 日常維運檢查清單](#d-日常維運檢查清單)

---

## 第 1 章：Node.js 與生態系總覽

### 1.1 Node.js 是什麼？適合解決什麼問題？

#### 定義

Node.js 是一個基於 **Chrome V8 引擎** 的 JavaScript 執行環境，讓 JavaScript 能夠在伺服器端執行。它採用 **事件驅動（Event-driven）** 與 **非阻塞 I/O（Non-blocking I/O）** 模型，特別適合處理高併發、I/O 密集型的應用場景。

#### 核心特性

| 特性 | 說明 |
|------|------|
| **單執行緒 + 事件迴圈** | 透過 Event Loop 處理大量併發連線 |
| **非阻塞 I/O** | I/O 操作不會阻塞主執行緒 |
| **跨平台** | 支援 Windows、Linux、macOS |
| **NPM 生態系** | 全球最大的套件管理生態系 |
| **JavaScript 全端** | 前後端使用相同語言，降低學習成本 |

#### 適合的應用場景

```mermaid
graph TD
    A[Node.js 適合場景] --> B[I/O 密集型應用]
    A --> C[即時應用]
    A --> D[API Gateway / BFF]
    A --> E[微服務架構]
    A --> F[Serverless Functions]
    
    B --> B1[REST API]
    B --> B2[GraphQL Server]
    C --> C1[WebSocket / Chat]
    C --> C2[即時通知系統]
    D --> D1[Backend for Frontend]
    E --> E1[輕量級服務]
    F --> F1[AWS Lambda / Azure Functions]
```

#### ⚠️ 不適合的場景

- **CPU 密集型運算**（如：影像處理、大量數學運算）
- **需要多執行緒平行計算的場景**（可考慮 Worker Threads，但仍有限制）
- **傳統企業系統需要強型別與複雜 ORM**（Java/Spring 可能更適合）

---

### 1.2 與 Java / Spring Boot、Python / FastAPI 的差異

| 比較項目 | Node.js | Java / Spring Boot | Python / FastAPI |
|----------|---------|-------------------|------------------|
| **執行模型** | 單執行緒 + Event Loop | 多執行緒 + Thread Pool | 單執行緒 + async/await |
| **型別系統** | 動態型別（TypeScript 可選） | 強型別 | 動態型別（Type Hints 可選） |
| **啟動速度** | 極快（毫秒級） | 較慢（秒級） | 快 |
| **記憶體消耗** | 低 | 高 | 中 |
| **生態系成熟度** | NPM 套件極多但品質參差 | Maven 套件穩定成熟 | PyPI 套件豐富 |
| **適合場景** | API、即時應用、BFF | 企業級應用、複雜業務邏輯 | 資料科學、ML、快速原型 |
| **學習曲線** | 低（熟悉 JS 即可） | 中高 | 低 |

#### 企業選型建議

```mermaid
flowchart TD
    A[專案需求評估] --> B{是否需要高併發 I/O?}
    B -->|是| C{團隊熟悉 JavaScript?}
    B -->|否| D{是否有複雜業務邏輯?}
    
    C -->|是| E[選擇 Node.js]
    C -->|否| F[評估學習成本]
    
    D -->|是| G[選擇 Java/Spring Boot]
    D -->|否| H{是否涉及 ML/資料處理?}
    
    H -->|是| I[選擇 Python]
    H -->|否| J[依團隊技能選擇]
```

---

### 1.3 Node.js 在企業系統中的常見使用場景

#### 1. API Gateway / BFF（Backend for Frontend）

```
┌─────────────┐     ┌─────────────────┐     ┌──────────────┐
│   Web App   │────▶│                 │────▶│ User Service │
├─────────────┤     │   Node.js BFF   │     ├──────────────┤
│  Mobile App │────▶│  (聚合 + 轉換)   │────▶│Order Service │
├─────────────┤     │                 │     ├──────────────┤
│   Partner   │────▶│                 │────▶│Payment Service│
└─────────────┘     └─────────────────┘     └──────────────┘
```

**實務案例**：
- 前端需要的資料來自多個微服務
- Node.js BFF 負責聚合、轉換、快取
- 減少前端直接呼叫多個 API 的複雜度

#### 2. 即時通訊系統

```javascript
// WebSocket 即時通訊範例
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    // 廣播給所有連線的客戶端
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });
});
```

#### 3. 微服務中的輕量級服務

適合用 Node.js 實作的微服務：
- 通知服務（Email、SMS、Push）
- 檔案上傳處理
- 排程任務調度器
- 資料轉換 / ETL 輕量處理

---

### 1.4 單體、微服務、Serverless 架構定位

#### 架構演進路線

```mermaid
graph LR
    A[單體架構 Monolith] --> B[模組化單體]
    B --> C[微服務架構]
    C --> D[Serverless]
    
    style A fill:#ffcccc
    style B fill:#ffffcc
    style C fill:#ccffcc
    style D fill:#ccccff
```

#### Node.js 在不同架構的定位

| 架構類型 | Node.js 定位 | 推薦框架 |
|----------|-------------|----------|
| **單體架構** | 快速原型、中小型專案 | Express、Fastify |
| **模組化單體** | 內部模組化，外部單一部署 | NestJS |
| **微服務** | 輕量級服務、BFF、API Gateway | NestJS、Fastify |
| **Serverless** | 函數即服務（FaaS） | 原生 JS/TS、Serverless Framework |

#### ✅ 實務建議

> **新專案起步建議**：
> 1. 除非確定需要微服務，否則從「模組化單體」開始
> 2. 使用 NestJS 的模組化設計，未來可輕鬆拆分
> 3. 避免過早優化，先求正確再求效能

---

## 第 2 章：Node.js 核心基礎

### 2.1 Node.js 執行模型（Event Loop、Non-blocking I/O）

#### Event Loop 運作機制

Event Loop 是 Node.js 的核心，負責協調非同步操作的執行順序。

```mermaid
graph TD
    A[Call Stack] --> B{Stack 是否為空?}
    B -->|否| A
    B -->|是| C[檢查 Microtask Queue]
    C --> D{有 Microtask?}
    D -->|是| E[執行所有 Microtask]
    E --> C
    D -->|否| F[檢查 Macrotask Queue]
    F --> G{有 Macrotask?}
    G -->|是| H[執行一個 Macrotask]
    H --> C
    G -->|否| I[等待新任務]
    I --> B
```

#### Event Loop 六個階段

```
   ┌───────────────────────────┐
┌─▶│         timers            │  ← setTimeout, setInterval
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │     pending callbacks     │  ← 系統操作回呼
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │       idle, prepare       │  ← 內部使用
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │          poll             │  ← I/O 回呼
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │          check            │  ← setImmediate
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
└──┤     close callbacks       │  ← socket.on('close')
   └───────────────────────────┘
```

#### 執行順序範例

```javascript
console.log('1. 同步程式碼');

setTimeout(() => {
  console.log('4. setTimeout (Macrotask)');
}, 0);

Promise.resolve().then(() => {
  console.log('3. Promise (Microtask)');
});

console.log('2. 同步程式碼結束');

// 輸出順序：
// 1. 同步程式碼
// 2. 同步程式碼結束
// 3. Promise (Microtask)
// 4. setTimeout (Macrotask)
```

#### ⚠️ 注意事項

> **絕對不要阻塞 Event Loop！**
> - 避免同步的大量運算
> - 避免同步的檔案操作（使用 `fs.promises`）
> - 大量迴圈運算考慮使用 Worker Threads

---

### 2.2 CommonJS vs ES Modules

#### 比較表

| 特性 | CommonJS (CJS) | ES Modules (ESM) |
|------|---------------|------------------|
| **語法** | `require()` / `module.exports` | `import` / `export` |
| **載入方式** | 同步 | 非同步 |
| **靜態分析** | 不支援 | 支援（Tree Shaking） |
| **Top-level await** | 不支援 | 支援 |
| **檔案副檔名** | `.js` / `.cjs` | `.mjs` 或 `"type": "module"` |
| **Node.js 支援** | 原生支援 | v12+ 原生支援 |

#### CommonJS 範例

```javascript
// utils.cjs
const helper = require('./helper');

function greet(name) {
  return `Hello, ${name}!`;
}

module.exports = { greet };

// main.cjs
const { greet } = require('./utils');
console.log(greet('World'));
```

#### ES Modules 範例

```javascript
// utils.mjs
import { helper } from './helper.mjs';

export function greet(name) {
  return `Hello, ${name}!`;
}

export default class Utils {
  // ...
}

// main.mjs
import Utils, { greet } from './utils.mjs';
console.log(greet('World'));
```

#### ✅ 企業專案建議

```json
// package.json
{
  "name": "enterprise-project",
  "type": "module",  // 👈 使用 ES Modules 作為預設
  "engines": {
    "node": ">=22.0.0"
  }
}
```

> **2026 年建議**：新專案一律使用 ES Modules
> - 更好的靜態分析與 Tree Shaking
> - 支援 Top-level await
> - 與瀏覽器端 JavaScript 一致

---

### 2.3 NPM、Yarn、PNPM 生態比較

#### 套件管理器比較

| 特性 | NPM | Yarn | PNPM |
|------|-----|------|------|
| **速度** | 中 | 快 | 最快 |
| **磁碟空間** | 高（重複安裝） | 高 | 低（硬連結共享） |
| **Monorepo 支援** | Workspaces | Workspaces | 原生支援最佳 |
| **Lock 檔案** | `package-lock.json` | `yarn.lock` | `pnpm-lock.yaml` |
| **嚴格性** | 寬鬆 | 中 | 嚴格（防止幽靈依賴） |
| **企業採用率** | 最高 | 高 | 成長中 |

#### 常用指令對照

| 操作 | NPM | Yarn | PNPM |
|------|-----|------|------|
| 安裝所有依賴 | `npm install` | `yarn` | `pnpm install` |
| 新增依賴 | `npm install pkg` | `yarn add pkg` | `pnpm add pkg` |
| 新增開發依賴 | `npm install -D pkg` | `yarn add -D pkg` | `pnpm add -D pkg` |
| 移除依賴 | `npm uninstall pkg` | `yarn remove pkg` | `pnpm remove pkg` |
| 執行腳本 | `npm run script` | `yarn script` | `pnpm script` |
| 更新依賴 | `npm update` | `yarn upgrade` | `pnpm update` |

#### ✅ 企業選型建議

```bash
# 2026 年建議：使用 PNPM
# 原因：
# 1. 最快的安裝速度
# 2. 節省磁碟空間（尤其在 CI/CD）
# 3. 嚴格的依賴管理，避免幽靈依賴問題
# 4. 優秀的 Monorepo 支援

# 安裝 PNPM
npm install -g pnpm

# 或使用 Corepack（Node.js 內建）
corepack enable
corepack prepare pnpm@latest --activate
```

---

### 2.4 專案目錄結構最佳實務

#### 推薦的企業級專案結構

```
project-root/
├── src/                          # 原始碼
│   ├── main.ts                   # 應用程式進入點
│   ├── app.module.ts             # 根模組（NestJS）
│   ├── config/                   # 設定相關
│   │   ├── index.ts
│   │   ├── database.config.ts
│   │   └── app.config.ts
│   ├── common/                   # 共用工具
│   │   ├── decorators/
│   │   ├── filters/
│   │   ├── guards/
│   │   ├── interceptors/
│   │   ├── pipes/
│   │   └── utils/
│   ├── modules/                  # 功能模組
│   │   ├── user/
│   │   │   ├── user.module.ts
│   │   │   ├── user.controller.ts
│   │   │   ├── user.service.ts
│   │   │   ├── user.repository.ts
│   │   │   ├── dto/
│   │   │   │   ├── create-user.dto.ts
│   │   │   │   └── update-user.dto.ts
│   │   │   ├── entities/
│   │   │   │   └── user.entity.ts
│   │   │   └── interfaces/
│   │   │       └── user.interface.ts
│   │   └── order/
│   │       └── ...
│   └── infrastructure/           # 基礎設施層
│       ├── database/
│       ├── cache/
│       ├── messaging/
│       └── external-services/
├── test/                         # 測試
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/                      # 腳本工具
├── docs/                         # 文件
├── .github/                      # GitHub 相關
│   └── workflows/
├── docker/                       # Docker 相關
│   ├── Dockerfile
│   └── docker-compose.yml
├── .env.example                  # 環境變數範本
├── .eslintrc.js                  # ESLint 設定
├── .prettierrc                   # Prettier 設定
├── tsconfig.json                 # TypeScript 設定
├── package.json
├── pnpm-lock.yaml
└── README.md
```

#### 目錄命名原則

| 目錄 | 用途 | 命名規則 |
|------|------|----------|
| `src/` | 所有原始碼 | 固定名稱 |
| `modules/` | 業務功能模組 | 以業務領域命名（user、order） |
| `common/` | 跨模組共用 | 以技術功能命名（guards、pipes） |
| `config/` | 設定檔 | 以設定類型命名（database、app） |
| `infrastructure/` | 外部依賴封裝 | 以技術命名（database、cache） |

---

## 第 3 章：TypeScript 在 Node.js 的標準用法

### 3.1 為什麼企業專案一定要用 TypeScript

#### TypeScript 帶來的價值

```mermaid
graph TD
    A[TypeScript] --> B[型別安全]
    A --> C[更好的 IDE 支援]
    A --> D[重構信心]
    A --> E[文件化效果]
    A --> F[錯誤提早發現]
    
    B --> B1[減少執行時期錯誤]
    C --> C1[自動補全 + 跳轉定義]
    D --> D1[大規模重構不怕漏改]
    E --> E1[型別即文件]
    F --> F1[編譯期攔截問題]
```

#### 實際效益數據

| 指標 | JavaScript | TypeScript | 改善幅度 |
|------|------------|------------|----------|
| 執行時期錯誤 | 基準 | 減少 15-20% | ↓ 15-20% |
| 程式碼審查時間 | 基準 | 減少 30% | ↓ 30% |
| 重構信心指數 | 低 | 高 | ↑ 顯著 |
| 新人上手時間 | 較長 | 較短 | ↓ 20% |

#### ❌ 不使用 TypeScript 的代價

```javascript
// JavaScript - 隱藏的地雷
function processUser(user) {
  // user 是什麼結構？有哪些屬性？
  // 沒有型別，只能靠猜測或查文件
  return user.name.toUpperCase();  // user.name 可能是 undefined
}

// 呼叫時傳錯參數，不會有任何警告
processUser({ username: 'John' });  // Runtime Error!
```

```typescript
// TypeScript - 明確的契約
interface User {
  id: number;
  name: string;
  email: string;
}

function processUser(user: User): string {
  return user.name.toUpperCase();  // 安全，因為 name 一定存在
}

// 編譯期就會報錯
processUser({ username: 'John' });  // ❌ Compile Error!
```

---

### 3.2 tsconfig 設計原則

#### 企業級推薦 tsconfig.json

```json
{
  "compilerOptions": {
    // 目標環境
    "target": "ES2023",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2023"],

    // 輸出設定
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,

    // 嚴格模式（必開）
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,

    // 額外檢查
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // 模組解析
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "resolveJsonModule": true,

    // 實驗性功能
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,

    // 其他
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "incremental": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "test"]
}
```

#### 關鍵設定說明

| 設定 | 建議值 | 說明 |
|------|--------|------|
| `strict` | `true` | 開啟所有嚴格檢查 |
| `noImplicitAny` | `true` | 禁止隱式 any |
| `strictNullChecks` | `true` | 嚴格 null 檢查 |
| `noUncheckedIndexedAccess` | `true` | 陣列/物件索引存取加入 undefined 可能性 |
| `noImplicitOverride` | `true` | 覆寫父類方法必須明確標示 |

---

### 3.3 型別設計與 Domain Model

#### 善用 TypeScript 型別系統

```typescript
// 1. 使用 type 定義 Union Types
type OrderStatus = 'pending' | 'confirmed' | 'shipped' | 'delivered' | 'cancelled';

// 2. 使用 interface 定義物件結構
interface Order {
  id: string;
  status: OrderStatus;
  items: OrderItem[];
  totalAmount: number;
  createdAt: Date;
  updatedAt: Date;
}

interface OrderItem {
  productId: string;
  productName: string;
  quantity: number;
  unitPrice: number;
}

// 3. 使用 Branded Types 增加型別安全
type UserId = string & { readonly brand: unique symbol };
type OrderId = string & { readonly brand: unique symbol };

function createUserId(id: string): UserId {
  return id as UserId;
}

function createOrderId(id: string): OrderId {
  return id as OrderId;
}

// 這樣就不能把 UserId 傳給需要 OrderId 的地方
function getOrder(orderId: OrderId): Order {
  // ...
}

const userId = createUserId('user-123');
const orderId = createOrderId('order-456');

// getOrder(userId);  // ❌ 編譯錯誤！
getOrder(orderId);    // ✅ 正確
```

#### DTO 設計最佳實務

```typescript
// create-order.dto.ts
import { IsString, IsNumber, IsArray, ValidateNested, Min } from 'class-validator';
import { Type } from 'class-transformer';

export class CreateOrderItemDto {
  @IsString()
  productId: string;

  @IsNumber()
  @Min(1)
  quantity: number;
}

export class CreateOrderDto {
  @IsString()
  customerId: string;

  @IsArray()
  @ValidateNested({ each: true })
  @Type(() => CreateOrderItemDto)
  items: CreateOrderItemDto[];
}

// response.dto.ts
export class OrderResponseDto {
  id: string;
  status: OrderStatus;
  totalAmount: number;
  createdAt: string;  // ISO 8601 格式

  static fromEntity(order: Order): OrderResponseDto {
    return {
      id: order.id,
      status: order.status,
      totalAmount: order.totalAmount,
      createdAt: order.createdAt.toISOString(),
    };
  }
}
```

---

### 3.4 常見反模式與避坑指南

#### ❌ 反模式 1：濫用 any

```typescript
// ❌ 錯誤示範
function processData(data: any): any {
  return data.result.items.map((item: any) => item.value);
}

// ✅ 正確做法
interface ApiResponse<T> {
  result: {
    items: T[];
  };
}

interface DataItem {
  value: number;
}

function processData(data: ApiResponse<DataItem>): number[] {
  return data.result.items.map(item => item.value);
}
```

#### ❌ 反模式 2：忽略 null/undefined 檢查

```typescript
// ❌ 錯誤示範
function getUserName(user: User | null): string {
  return user.name;  // 可能是 null！
}

// ✅ 正確做法（使用 Optional Chaining 與 Nullish Coalescing）
function getUserName(user: User | null): string {
  return user?.name ?? 'Anonymous';
}

// ✅ 或使用 Guard
function getUserName(user: User | null): string {
  if (!user) {
    throw new Error('User is required');
  }
  return user.name;
}
```

#### ❌ 反模式 3：Type Assertion 濫用

```typescript
// ❌ 錯誤示範
const data = JSON.parse(response) as User;  // 危險！沒有驗證

// ✅ 正確做法：使用 Zod 進行執行時期驗證
import { z } from 'zod';

const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
});

type User = z.infer<typeof UserSchema>;

function parseUser(data: unknown): User {
  return UserSchema.parse(data);  // 執行時期驗證
}
```

---

## 第 4 章：Web Framework 生態系

### 4.1 Express（歷史定位與限制）

#### Express 簡介

Express 是 Node.js 最老牌、最普及的 Web Framework，以極簡主義著稱。

```javascript
// 最簡單的 Express 應用
import express from 'express';

const app = express();

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello World!' });
});

app.listen(3000);
```

#### Express 的優點

- ✅ 學習曲線低，文件豐富
- ✅ 中介軟體生態系龐大
- ✅ 社群活躍，問題容易找到解答
- ✅ 適合快速原型開發

#### Express 的限制

| 限制 | 說明 | 影響 |
|------|------|------|
| **無原生 TypeScript 支援** | 需要額外設定 @types | 型別支援不完整 |
| **無內建架構指引** | 自由度高但缺乏規範 | 大型專案難以維護 |
| **效能較低** | 相比 Fastify 慢約 2x | 高併發場景受限 |
| **Callback-based** | 早期設計，async/await 支援後加 | 錯誤處理需額外處理 |
| **無依賴注入** | 需自行實作或使用第三方 | 測試不易 |

#### ⚠️ 企業專案建議

> Express 適合：
> - 小型專案或 PoC
> - 團隊只熟悉 Express
> - 簡單的 API Gateway
>
> 不建議用於：
> - 新的大型企業專案
> - 需要長期維護的系統

---

### 4.2 Fastify（高效能）

#### Fastify 簡介

Fastify 是以效能為核心設計的現代 Web Framework，號稱是最快的 Node.js Framework 之一。

```typescript
// Fastify 基本範例
import Fastify from 'fastify';

const fastify = Fastify({ logger: true });

// 使用 JSON Schema 進行驗證
fastify.route({
  method: 'POST',
  url: '/api/users',
  schema: {
    body: {
      type: 'object',
      required: ['name', 'email'],
      properties: {
        name: { type: 'string' },
        email: { type: 'string', format: 'email' }
      }
    },
    response: {
      201: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          name: { type: 'string' }
        }
      }
    }
  },
  handler: async (request, reply) => {
    const { name, email } = request.body;
    const user = await createUser(name, email);
    reply.code(201).send(user);
  }
});

fastify.listen({ port: 3000 });
```

#### Fastify 的優勢

| 優勢 | 說明 |
|------|------|
| **極致效能** | 比 Express 快約 2x，接近原生 http 效能 |
| **Schema-based 驗證** | 內建 JSON Schema 驗證與序列化 |
| **TypeScript 友善** | 原生支援，型別定義完整 |
| **插件系統** | 強大的封裝與模組化機制 |
| **自動文件生成** | 基於 Schema 自動產生 OpenAPI 文件 |

#### 何時選擇 Fastify

適合用於：
- 高效能 API 服務
- 需要 Schema 驗證的 API
- 微服務架構中的服務
- 追求效能的 Gateway/Proxy

---

### 4.3 NestJS（企業級主流）

#### NestJS 簡介

NestJS 是一個漸進式的 Node.js Framework，採用 Angular 風格的架構，支援 TypeScript、依賴注入、模組化設計。

```mermaid
graph TD
    A[NestJS 核心概念] --> B[Modules]
    A --> C[Controllers]
    A --> D[Providers/Services]
    A --> E[Dependency Injection]
    A --> F[Decorators]
    
    B --> B1[功能模組化]
    C --> C1[處理 HTTP 請求]
    D --> D1[業務邏輯封裝]
    E --> E1[自動注入依賴]
    F --> F1[宣告式程式設計]
```

#### NestJS 基本範例

```typescript
// user.module.ts
import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';
import { UserRepository } from './user.repository';

@Module({
  controllers: [UserController],
  providers: [UserService, UserRepository],
  exports: [UserService],
})
export class UserModule {}

// user.controller.ts
import { Controller, Get, Post, Body, Param, HttpCode, HttpStatus } from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';
import { UserResponseDto } from './dto/user-response.dto';

@Controller('api/users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  @HttpCode(HttpStatus.CREATED)
  async create(@Body() createUserDto: CreateUserDto): Promise<UserResponseDto> {
    return this.userService.create(createUserDto);
  }

  @Get(':id')
  async findOne(@Param('id') id: string): Promise<UserResponseDto> {
    return this.userService.findOne(id);
  }
}

// user.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';
import { UserRepository } from './user.repository';
import { CreateUserDto } from './dto/create-user.dto';
import { User } from './entities/user.entity';

@Injectable()
export class UserService {
  constructor(private readonly userRepository: UserRepository) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    return this.userRepository.create(createUserDto);
  }

  async findOne(id: string): Promise<User> {
    const user = await this.userRepository.findById(id);
    if (!user) {
      throw new NotFoundException(`User with ID ${id} not found`);
    }
    return user;
  }
}
```

#### NestJS 核心優勢

| 優勢 | 說明 | 企業價值 |
|------|------|----------|
| **依賴注入** | 內建 IoC Container | 鬆耦合、易測試 |
| **模組化設計** | 清晰的邊界與職責 | 易於團隊分工 |
| **TypeScript 原生** | 完整型別支援 | 開發體驗佳 |
| **豐富的生態** | ORM、驗證、快取、排程等 | 減少自行整合成本 |
| **微服務支援** | 內建多種傳輸層 | 擴展彈性高 |
| **文件完善** | 官方文件詳盡 | 學習資源豐富 |

---

### 4.4 Framework 選型建議與比較表

#### 完整比較表

| 比較項目 | Express | Fastify | NestJS |
|----------|---------|---------|--------|
| **效能** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **學習曲線** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **TypeScript 支援** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **架構指引** | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **依賴注入** | 無內建 | 無內建 | ⭐⭐⭐⭐⭐ |
| **測試友善** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **微服務支援** | 需自行整合 | 插件支援 | ⭐⭐⭐⭐⭐ |
| **生態系成熟度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **企業採用率** | 高（但多為舊專案） | 成長中 | 高（新專案主流） |

#### 選型決策流程

```mermaid
flowchart TD
    A[新專案選型] --> B{專案規模?}
    
    B -->|小型/PoC| C{團隊經驗?}
    B -->|中大型| D{效能優先?}
    
    C -->|熟悉 Express| E[Express]
    C -->|願意學習| F[Fastify]
    
    D -->|是，API Gateway/高併發| G[Fastify]
    D -->|否，一般業務系統| H[NestJS]
    
    style E fill:#ffcccc
    style F fill:#ccffcc
    style G fill:#ccffcc
    style H fill:#ccccff
```

#### ✅ 2026 年企業專案建議

> **首選 NestJS**：
> - 新的中大型專案
> - 需要長期維護的系統
> - 團隊協作開發
>
> **選擇 Fastify**：
> - API Gateway / Proxy
> - 對效能有極致要求
> - 微服務中的輕量級服務
>
> **保守選擇 Express**：
> - 只能用在舊系統維護
> - 極簡的內部工具

---

## 第 5 章：RESTful API 與 Backend 架構設計

### 5.1 Controller / Service / Repository 分層

#### 三層架構概念

```mermaid
graph TD
    subgraph "表現層 Presentation"
        A[Controller]
    end
    
    subgraph "業務層 Business"
        B[Service]
    end
    
    subgraph "資料層 Data"
        C[Repository]
    end
    
    subgraph "外部"
        D[(Database)]
        E[External API]
    end
    
    A --> B
    B --> C
    C --> D
    B --> E
    
    A -.-|"HTTP Request/Response<br/>DTO 驗證"| A
    B -.-|"業務邏輯<br/>Transaction"| B
    C -.-|"資料存取<br/>Query"| C
```

#### 各層職責定義

| 層級 | 職責 | 不該做的事 |
|------|------|-----------|
| **Controller** | 接收請求、參數驗證、回應格式化 | 不該有業務邏輯 |
| **Service** | 業務邏輯、Transaction 管理 | 不該直接存取 DB |
| **Repository** | 資料存取、Query 封裝 | 不該有業務邏輯 |

#### 完整範例

```typescript
// === Controller 層 ===
// order.controller.ts
import {
  Controller, Post, Get, Param, Body,
  HttpCode, HttpStatus, UseGuards
} from '@nestjs/common';
import { OrderService } from './order.service';
import { CreateOrderDto } from './dto/create-order.dto';
import { OrderResponseDto } from './dto/order-response.dto';
import { JwtAuthGuard } from '../auth/guards/jwt-auth.guard';
import { CurrentUser } from '../auth/decorators/current-user.decorator';
import { User } from '../user/entities/user.entity';

@Controller('api/orders')
@UseGuards(JwtAuthGuard)
export class OrderController {
  constructor(private readonly orderService: OrderService) {}

  @Post()
  @HttpCode(HttpStatus.CREATED)
  async create(
    @CurrentUser() user: User,
    @Body() createOrderDto: CreateOrderDto,
  ): Promise<OrderResponseDto> {
    const order = await this.orderService.createOrder(user.id, createOrderDto);
    return OrderResponseDto.fromEntity(order);
  }

  @Get(':id')
  async findOne(
    @CurrentUser() user: User,
    @Param('id') id: string,
  ): Promise<OrderResponseDto> {
    const order = await this.orderService.findOrderById(id, user.id);
    return OrderResponseDto.fromEntity(order);
  }
}

// === Service 層 ===
// order.service.ts
import { Injectable, NotFoundException, BadRequestException } from '@nestjs/common';
import { OrderRepository } from './order.repository';
import { ProductService } from '../product/product.service';
import { CreateOrderDto } from './dto/create-order.dto';
import { Order, OrderStatus } from './entities/order.entity';
import { DataSource } from 'typeorm';

@Injectable()
export class OrderService {
  constructor(
    private readonly orderRepository: OrderRepository,
    private readonly productService: ProductService,
    private readonly dataSource: DataSource,
  ) {}

  async createOrder(userId: string, dto: CreateOrderDto): Promise<Order> {
    // 使用 Transaction 確保資料一致性
    return this.dataSource.transaction(async (manager) => {
      // 1. 驗證商品庫存
      for (const item of dto.items) {
        const product = await this.productService.findById(item.productId);
        if (product.stock < item.quantity) {
          throw new BadRequestException(
            `Product ${product.name} has insufficient stock`,
          );
        }
      }

      // 2. 計算總金額
      let totalAmount = 0;
      const orderItems = [];
      for (const item of dto.items) {
        const product = await this.productService.findById(item.productId);
        totalAmount += product.price * item.quantity;
        orderItems.push({
          productId: item.productId,
          quantity: item.quantity,
          unitPrice: product.price,
        });
      }

      // 3. 建立訂單
      const order = await this.orderRepository.createWithManager(manager, {
        userId,
        items: orderItems,
        totalAmount,
        status: OrderStatus.PENDING,
      });

      // 4. 扣除庫存
      for (const item of dto.items) {
        await this.productService.decreaseStockWithManager(
          manager,
          item.productId,
          item.quantity,
        );
      }

      return order;
    });
  }

  async findOrderById(id: string, userId: string): Promise<Order> {
    const order = await this.orderRepository.findByIdAndUserId(id, userId);
    if (!order) {
      throw new NotFoundException(`Order ${id} not found`);
    }
    return order;
  }
}

// === Repository 層 ===
// order.repository.ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository, EntityManager } from 'typeorm';
import { Order } from './entities/order.entity';

@Injectable()
export class OrderRepository {
  constructor(
    @InjectRepository(Order)
    private readonly repository: Repository<Order>,
  ) {}

  async findByIdAndUserId(id: string, userId: string): Promise<Order | null> {
    return this.repository.findOne({
      where: { id, userId },
      relations: ['items', 'items.product'],
    });
  }

  async createWithManager(
    manager: EntityManager,
    data: Partial<Order>,
  ): Promise<Order> {
    const order = manager.create(Order, data);
    return manager.save(order);
  }

  async findByUserId(userId: string): Promise<Order[]> {
    return this.repository.find({
      where: { userId },
      order: { createdAt: 'DESC' },
    });
  }
}
```

---

### 5.2 DTO、Validation、Error Handling 設計

#### DTO（Data Transfer Object）設計原則

```typescript
// dto/create-order.dto.ts
import {
  IsString, IsArray, ValidateNested,
  IsNumber, Min, ArrayMinSize
} from 'class-validator';
import { Type } from 'class-transformer';
import { ApiProperty } from '@nestjs/swagger';

export class CreateOrderItemDto {
  @ApiProperty({ example: 'prod-123', description: '商品 ID' })
  @IsString()
  productId: string;

  @ApiProperty({ example: 2, description: '數量', minimum: 1 })
  @IsNumber()
  @Min(1)
  quantity: number;
}

export class CreateOrderDto {
  @ApiProperty({ type: [CreateOrderItemDto], description: '訂單項目' })
  @IsArray()
  @ArrayMinSize(1)
  @ValidateNested({ each: true })
  @Type(() => CreateOrderItemDto)
  items: CreateOrderItemDto[];

  @ApiProperty({ example: '請盡快出貨', required: false })
  @IsString()
  @IsOptional()
  note?: string;
}

// dto/order-response.dto.ts
import { ApiProperty } from '@nestjs/swagger';
import { Order } from '../entities/order.entity';

export class OrderItemResponseDto {
  @ApiProperty()
  productId: string;

  @ApiProperty()
  productName: string;

  @ApiProperty()
  quantity: number;

  @ApiProperty()
  unitPrice: number;
}

export class OrderResponseDto {
  @ApiProperty()
  id: string;

  @ApiProperty()
  status: string;

  @ApiProperty({ type: [OrderItemResponseDto] })
  items: OrderItemResponseDto[];

  @ApiProperty()
  totalAmount: number;

  @ApiProperty()
  createdAt: string;

  static fromEntity(order: Order): OrderResponseDto {
    return {
      id: order.id,
      status: order.status,
      items: order.items.map(item => ({
        productId: item.productId,
        productName: item.product?.name ?? '',
        quantity: item.quantity,
        unitPrice: item.unitPrice,
      })),
      totalAmount: order.totalAmount,
      createdAt: order.createdAt.toISOString(),
    };
  }
}
```

#### 統一錯誤處理

```typescript
// common/filters/http-exception.filter.ts
import {
  ExceptionFilter, Catch, ArgumentsHost,
  HttpException, HttpStatus, Logger
} from '@nestjs/common';
import { Request, Response } from 'express';

interface ErrorResponse {
  statusCode: number;
  message: string;
  error: string;
  timestamp: string;
  path: string;
  requestId?: string;
}

@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
  private readonly logger = new Logger(GlobalExceptionFilter.name);

  catch(exception: unknown, host: ArgumentsHost): void {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();

    let statusCode = HttpStatus.INTERNAL_SERVER_ERROR;
    let message = 'Internal server error';
    let error = 'Internal Server Error';

    if (exception instanceof HttpException) {
      statusCode = exception.getStatus();
      const exceptionResponse = exception.getResponse();
      
      if (typeof exceptionResponse === 'string') {
        message = exceptionResponse;
      } else if (typeof exceptionResponse === 'object') {
        message = (exceptionResponse as any).message || message;
        error = (exceptionResponse as any).error || error;
      }
    } else if (exception instanceof Error) {
      message = exception.message;
      // 記錄完整錯誤堆疊（僅在 log，不回傳給客戶端）
      this.logger.error(
        `Unhandled exception: ${message}`,
        exception.stack,
      );
    }

    const errorResponse: ErrorResponse = {
      statusCode,
      message,
      error,
      timestamp: new Date().toISOString(),
      path: request.url,
      requestId: request.headers['x-request-id'] as string,
    };

    response.status(statusCode).json(errorResponse);
  }
}

// 在 main.ts 中註冊
// app.useGlobalFilters(new GlobalExceptionFilter());
```

---

### 5.3 OpenAPI / Swagger 文件化

#### NestJS Swagger 設定

```typescript
// main.ts
import { NestFactory } from '@nestjs/core';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Swagger 設定
  const config = new DocumentBuilder()
    .setTitle('Order Service API')
    .setDescription('訂單服務 API 文件')
    .setVersion('1.0.0')
    .addBearerAuth(
      {
        type: 'http',
        scheme: 'bearer',
        bearerFormat: 'JWT',
      },
      'JWT-auth',
    )
    .addTag('orders', '訂單相關 API')
    .addTag('users', '使用者相關 API')
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api-docs', app, document);

  await app.listen(3000);
}
bootstrap();
```

#### Controller 加上 Swagger 裝飾器

```typescript
import {
  ApiTags, ApiOperation, ApiResponse,
  ApiBearerAuth, ApiParam, ApiBody
} from '@nestjs/swagger';

@ApiTags('orders')
@ApiBearerAuth('JWT-auth')
@Controller('api/orders')
@UseGuards(JwtAuthGuard)
export class OrderController {
  @Post()
  @ApiOperation({ summary: '建立訂單', description: '建立新的訂單' })
  @ApiBody({ type: CreateOrderDto })
  @ApiResponse({
    status: 201,
    description: '訂單建立成功',
    type: OrderResponseDto,
  })
  @ApiResponse({ status: 400, description: '請求參數錯誤' })
  @ApiResponse({ status: 401, description: '未授權' })
  async create(
    @CurrentUser() user: User,
    @Body() createOrderDto: CreateOrderDto,
  ): Promise<OrderResponseDto> {
    // ...
  }

  @Get(':id')
  @ApiOperation({ summary: '取得訂單', description: '根據 ID 取得訂單詳情' })
  @ApiParam({ name: 'id', description: '訂單 ID' })
  @ApiResponse({
    status: 200,
    description: '成功取得訂單',
    type: OrderResponseDto,
  })
  @ApiResponse({ status: 404, description: '訂單不存在' })
  async findOne(
    @CurrentUser() user: User,
    @Param('id') id: string,
  ): Promise<OrderResponseDto> {
    // ...
  }
}
```

---

### 5.4 Clean Architecture / Hexagonal Architecture 應用

#### Clean Architecture 概念

```mermaid
graph TD
    subgraph "外層 - 框架與驅動"
        A[Web Framework<br/>NestJS]
        B[Database<br/>PostgreSQL]
        C[External Services<br/>Payment Gateway]
    end
    
    subgraph "介面轉接層 Adapters"
        D[Controllers]
        E[Repositories Impl]
        F[External Service Adapters]
    end
    
    subgraph "應用層 Application"
        G[Use Cases]
        H[Application Services]
    end
    
    subgraph "核心層 Domain"
        I[Entities]
        J[Domain Services]
        K[Repository Interfaces]
    end
    
    A --> D
    D --> G
    G --> I
    G --> K
    E --> K
    B --> E
    C --> F
    F --> G
```

#### Hexagonal Architecture 實作範例

```typescript
// === Domain Layer（核心，不依賴任何外部） ===

// domain/entities/order.entity.ts
export class Order {
  constructor(
    public readonly id: string,
    public readonly userId: string,
    public items: OrderItem[],
    public status: OrderStatus,
    public totalAmount: number,
    public readonly createdAt: Date,
  ) {}

  // Domain Logic
  confirm(): void {
    if (this.status !== OrderStatus.PENDING) {
      throw new DomainError('Only pending orders can be confirmed');
    }
    this.status = OrderStatus.CONFIRMED;
  }

  cancel(): void {
    if (this.status === OrderStatus.SHIPPED) {
      throw new DomainError('Shipped orders cannot be cancelled');
    }
    this.status = OrderStatus.CANCELLED;
  }

  calculateTotal(): number {
    return this.items.reduce(
      (sum, item) => sum + item.unitPrice * item.quantity,
      0,
    );
  }
}

// domain/ports/order.repository.port.ts（介面）
export interface OrderRepositoryPort {
  findById(id: string): Promise<Order | null>;
  findByUserId(userId: string): Promise<Order[]>;
  save(order: Order): Promise<Order>;
}

// domain/ports/payment.service.port.ts（介面）
export interface PaymentServicePort {
  processPayment(orderId: string, amount: number): Promise<PaymentResult>;
}

// === Application Layer（Use Cases） ===

// application/use-cases/create-order.use-case.ts
import { Inject, Injectable } from '@nestjs/common';
import { OrderRepositoryPort } from '../../domain/ports/order.repository.port';
import { Order } from '../../domain/entities/order.entity';

@Injectable()
export class CreateOrderUseCase {
  constructor(
    @Inject('OrderRepositoryPort')
    private readonly orderRepository: OrderRepositoryPort,
  ) {}

  async execute(input: CreateOrderInput): Promise<Order> {
    // 業務邏輯
    const order = new Order(
      generateId(),
      input.userId,
      input.items,
      OrderStatus.PENDING,
      0,
      new Date(),
    );
    
    order.totalAmount = order.calculateTotal();
    
    return this.orderRepository.save(order);
  }
}

// === Infrastructure Layer（實作） ===

// infrastructure/repositories/order.repository.ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { OrderRepositoryPort } from '../../domain/ports/order.repository.port';
import { Order } from '../../domain/entities/order.entity';
import { OrderEntity } from '../persistence/entities/order.entity';

@Injectable()
export class OrderRepository implements OrderRepositoryPort {
  constructor(
    @InjectRepository(OrderEntity)
    private readonly repository: Repository<OrderEntity>,
  ) {}

  async findById(id: string): Promise<Order | null> {
    const entity = await this.repository.findOne({ where: { id } });
    return entity ? this.toDomain(entity) : null;
  }

  async save(order: Order): Promise<Order> {
    const entity = this.toEntity(order);
    const saved = await this.repository.save(entity);
    return this.toDomain(saved);
  }

  private toDomain(entity: OrderEntity): Order {
    return new Order(
      entity.id,
      entity.userId,
      entity.items.map(/* ... */),
      entity.status,
      entity.totalAmount,
      entity.createdAt,
    );
  }

  private toEntity(domain: Order): OrderEntity {
    // ...
  }
}
```

#### ✅ 架構選擇建議

| 專案規模 | 建議架構 | 原因 |
|----------|----------|------|
| 小型 / PoC | 傳統三層 | 簡單、快速 |
| 中型 | 模組化三層 | 平衡複雜度與彈性 |
| 大型 / 核心系統 | Clean / Hexagonal | 長期維護、測試、替換彈性 |

---

> 📌 **本章重點回顧**：
> 1. 三層架構（Controller/Service/Repository）是基礎，確保職責分離
> 2. DTO 搭配 class-validator 做驗證，回應用專屬 ResponseDto
> 3. 統一錯誤處理，不要讓錯誤訊息洩漏敏感資訊
> 4. OpenAPI/Swagger 文件化是 API 開發必備
> 5. 大型專案考慮 Clean Architecture 提升可測試性與彈性

---

## 第 6 章：非同步處理與背景任務

### 6.1 async / await 正確使用方式

#### 基本原則

```typescript
// ✅ 正確：使用 async/await
async function fetchUserData(userId: string): Promise<UserData> {
  const user = await userRepository.findById(userId);
  const orders = await orderRepository.findByUserId(userId);
  return { user, orders };
}

// ✅ 更佳：平行執行不相依的操作
async function fetchUserData(userId: string): Promise<UserData> {
  const [user, orders] = await Promise.all([
    userRepository.findById(userId),
    orderRepository.findByUserId(userId),
  ]);
  return { user, orders };
}
```

#### 常見錯誤與修正

```typescript
// ❌ 錯誤 1：忘記 await
async function saveUser(user: User): Promise<void> {
  userRepository.save(user);  // 沒有 await，不會等待完成
}

// ✅ 正確
async function saveUser(user: User): Promise<void> {
  await userRepository.save(user);
}

// ❌ 錯誤 2：在迴圈中逐一 await（效能差）
async function processUsers(userIds: string[]): Promise<User[]> {
  const users: User[] = [];
  for (const id of userIds) {
    const user = await userRepository.findById(id);  // 序列執行
    users.push(user);
  }
  return users;
}

// ✅ 正確：使用 Promise.all 平行處理
async function processUsers(userIds: string[]): Promise<User[]> {
  return Promise.all(
    userIds.map(id => userRepository.findById(id))
  );
}

// ✅ 更佳：控制併發數量避免過載
import pLimit from 'p-limit';

async function processUsers(userIds: string[]): Promise<User[]> {
  const limit = pLimit(10);  // 最多同時 10 個
  return Promise.all(
    userIds.map(id => limit(() => userRepository.findById(id)))
  );
}
```

#### 錯誤處理最佳實務

```typescript
// ✅ 使用 try-catch 處理錯誤
async function createOrder(dto: CreateOrderDto): Promise<Order> {
  try {
    const order = await orderService.create(dto);
    await emailService.sendConfirmation(order);
    return order;
  } catch (error) {
    if (error instanceof InsufficientStockError) {
      throw new BadRequestException('庫存不足');
    }
    if (error instanceof PaymentFailedError) {
      throw new PaymentRequiredException('付款失敗');
    }
    throw error;  // 未知錯誤向上拋
  }
}

// ✅ Promise.allSettled 處理部分失敗
async function sendNotifications(userIds: string[]): Promise<NotificationResult> {
  const results = await Promise.allSettled(
    userIds.map(id => notificationService.send(id))
  );

  const succeeded = results.filter(r => r.status === 'fulfilled').length;
  const failed = results.filter(r => r.status === 'rejected').length;

  return { succeeded, failed, total: userIds.length };
}
```

---

### 6.2 Queue（BullMQ / RabbitMQ / Kafka）

#### 訊息佇列使用場景

```mermaid
graph LR
    A[API Request] --> B[Web Server]
    B --> C{需要即時回應?}
    C -->|是| D[同步處理]
    C -->|否| E[放入 Queue]
    E --> F[Background Worker]
    F --> G[Email Service]
    F --> H[報表生成]
    F --> I[資料同步]
```

#### BullMQ 範例（推薦用於 Node.js）

```typescript
// queue/email.queue.ts
import { Queue, Worker, Job } from 'bullmq';
import { Injectable, OnModuleInit, OnModuleDestroy } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

interface EmailJobData {
  to: string;
  subject: string;
  template: string;
  context: Record<string, unknown>;
}

@Injectable()
export class EmailQueue implements OnModuleInit, OnModuleDestroy {
  private queue: Queue<EmailJobData>;
  private worker: Worker<EmailJobData>;

  constructor(
    private readonly configService: ConfigService,
    private readonly emailService: EmailService,
  ) {}

  async onModuleInit() {
    const redisConfig = {
      host: this.configService.get('REDIS_HOST'),
      port: this.configService.get('REDIS_PORT'),
    };

    // 建立 Queue
    this.queue = new Queue<EmailJobData>('email', {
      connection: redisConfig,
      defaultJobOptions: {
        attempts: 3,
        backoff: {
          type: 'exponential',
          delay: 1000,
        },
        removeOnComplete: 1000,
        removeOnFail: 5000,
      },
    });

    // 建立 Worker
    this.worker = new Worker<EmailJobData>(
      'email',
      async (job: Job<EmailJobData>) => {
        await this.processEmail(job);
      },
      {
        connection: redisConfig,
        concurrency: 5,  // 同時處理 5 個任務
      },
    );

    this.worker.on('completed', (job) => {
      console.log(`Email job ${job.id} completed`);
    });

    this.worker.on('failed', (job, err) => {
      console.error(`Email job ${job?.id} failed:`, err);
    });
  }

  async onModuleDestroy() {
    await this.queue.close();
    await this.worker.close();
  }

  // 新增任務到 Queue
  async addEmailJob(data: EmailJobData): Promise<void> {
    await this.queue.add('send-email', data, {
      priority: data.template === 'password-reset' ? 1 : 10,
    });
  }

  // 處理任務
  private async processEmail(job: Job<EmailJobData>): Promise<void> {
    const { to, subject, template, context } = job.data;
    await this.emailService.send(to, subject, template, context);
  }
}

// 使用方式
@Injectable()
export class UserService {
  constructor(private readonly emailQueue: EmailQueue) {}

  async registerUser(dto: RegisterDto): Promise<User> {
    const user = await this.userRepository.create(dto);
    
    // 非同步發送歡迎信（不阻塞回應）
    await this.emailQueue.addEmailJob({
      to: user.email,
      subject: '歡迎加入！',
      template: 'welcome',
      context: { userName: user.name },
    });

    return user;
  }
}
```

#### 訊息佇列選型

| 特性 | BullMQ | RabbitMQ | Kafka |
|------|--------|----------|-------|
| **適用場景** | 任務佇列、延遲任務 | 企業級訊息傳遞 | 大量事件串流 |
| **吞吐量** | 中 | 中高 | 極高 |
| **訊息保證** | At-least-once | At-most/least/exactly | At-least-once |
| **學習曲線** | 低 | 中 | 高 |
| **依賴** | Redis | Erlang Runtime | Zookeeper/KRaft |
| **Node.js 整合** | 原生優秀 | 良好 | 良好 |

---

### 6.3 排程任務（cron）

#### NestJS Schedule 模組

```typescript
// schedule/tasks.service.ts
import { Injectable, Logger } from '@nestjs/common';
import { Cron, CronExpression, Interval, Timeout } from '@nestjs/schedule';

@Injectable()
export class TasksService {
  private readonly logger = new Logger(TasksService.name);

  // 每天凌晨 2 點執行
  @Cron('0 2 * * *')
  async handleDailyReport() {
    this.logger.log('Generating daily report...');
    await this.reportService.generateDailyReport();
  }

  // 使用預設常數
  @Cron(CronExpression.EVERY_HOUR)
  async handleHourlyCacheCleanup() {
    this.logger.log('Cleaning up expired cache...');
    await this.cacheService.cleanupExpired();
  }

  // 每 30 秒執行（毫秒）
  @Interval(30000)
  async handleHealthCheck() {
    await this.healthService.checkExternalServices();
  }

  // 應用啟動後 5 秒執行一次
  @Timeout(5000)
  async handleStartup() {
    this.logger.log('Running startup tasks...');
    await this.initializationService.warmupCache();
  }
}

// app.module.ts
import { ScheduleModule } from '@nestjs/schedule';

@Module({
  imports: [
    ScheduleModule.forRoot(),
    // ...
  ],
})
export class AppModule {}
```

#### Cron 表達式速查

```
┌───────────── 秒 (0 - 59)（可選）
│ ┌───────────── 分 (0 - 59)
│ │ ┌───────────── 時 (0 - 23)
│ │ │ ┌───────────── 日 (1 - 31)
│ │ │ │ ┌───────────── 月 (1 - 12)
│ │ │ │ │ ┌───────────── 週幾 (0 - 7)（0 和 7 都是週日）
│ │ │ │ │ │
* * * * * *
```

| 表達式 | 說明 |
|--------|------|
| `0 0 * * *` | 每天午夜 |
| `0 */2 * * *` | 每 2 小時 |
| `0 9-17 * * 1-5` | 週一到週五 9-17 點每小時 |
| `0 0 1 * *` | 每月 1 號午夜 |
| `*/10 * * * * *` | 每 10 秒（含秒欄位）|

---

### 6.4 長時間任務設計原則

#### 設計考量

```mermaid
graph TD
    A[長時間任務] --> B{執行時間?}
    B -->|< 30秒| C[同步執行]
    B -->|30秒-5分鐘| D[背景任務 + 輪詢]
    B -->|> 5分鐘| E[任務佇列 + 進度追蹤]
    
    D --> D1[回傳 taskId]
    D --> D2[提供查詢 API]
    
    E --> E1[分段處理]
    E --> E2[斷點續傳]
    E --> E3[進度通知]
```

#### 任務進度追蹤範例

```typescript
// task/task.entity.ts
export enum TaskStatus {
  PENDING = 'pending',
  RUNNING = 'running',
  COMPLETED = 'completed',
  FAILED = 'failed',
}

export interface Task {
  id: string;
  type: string;
  status: TaskStatus;
  progress: number;  // 0-100
  result?: unknown;
  error?: string;
  createdAt: Date;
  updatedAt: Date;
}

// task/task.service.ts
@Injectable()
export class TaskService {
  constructor(
    private readonly taskRepository: TaskRepository,
    private readonly exportQueue: ExportQueue,
  ) {}

  // 建立長時間任務
  async createExportTask(userId: string, params: ExportParams): Promise<Task> {
    const task = await this.taskRepository.create({
      type: 'export',
      status: TaskStatus.PENDING,
      progress: 0,
      metadata: { userId, params },
    });

    // 放入佇列處理
    await this.exportQueue.add(task.id, { taskId: task.id, ...params });

    return task;
  }

  // 更新進度
  async updateProgress(taskId: string, progress: number): Promise<void> {
    await this.taskRepository.update(taskId, {
      progress,
      status: TaskStatus.RUNNING,
    });
  }

  // 查詢任務狀態
  async getTaskStatus(taskId: string): Promise<Task> {
    return this.taskRepository.findById(taskId);
  }
}

// task/export.worker.ts
@Injectable()
export class ExportWorker {
  async process(job: Job): Promise<void> {
    const { taskId, params } = job.data;
    
    try {
      const totalRecords = await this.countRecords(params);
      const batchSize = 1000;
      const batches = Math.ceil(totalRecords / batchSize);
      
      for (let i = 0; i < batches; i++) {
        // 處理一批資料
        await this.processBatch(params, i * batchSize, batchSize);
        
        // 更新進度
        const progress = Math.round(((i + 1) / batches) * 100);
        await this.taskService.updateProgress(taskId, progress);
      }

      // 完成
      await this.taskRepository.update(taskId, {
        status: TaskStatus.COMPLETED,
        progress: 100,
        result: { downloadUrl: '/exports/...' },
      });
    } catch (error) {
      await this.taskRepository.update(taskId, {
        status: TaskStatus.FAILED,
        error: error.message,
      });
      throw error;
    }
  }
}
```

---

## 第 7 章：資料庫與 ORM / Query Builder

### 7.1 PostgreSQL / MySQL / MongoDB 使用場景

#### 資料庫選型指引

```mermaid
graph TD
    A[資料類型評估] --> B{結構化程度?}
    B -->|高度結構化| C{需要 ACID?}
    B -->|半結構化/多變| D[MongoDB]
    
    C -->|是| E{規模/功能需求?}
    C -->|可接受最終一致| D
    
    E -->|企業級/進階功能| F[PostgreSQL]
    E -->|簡單/快速| G[MySQL]
```

| 資料庫 | 適用場景 | 優勢 | 限制 |
|--------|----------|------|------|
| **PostgreSQL** | 複雜查詢、地理資訊、JSONB | 功能豐富、擴展性強 | 學習曲線較陡 |
| **MySQL** | 一般 CRUD、讀取為主 | 簡單、效能好、廣泛支援 | 功能較少 |
| **MongoDB** | 文件型資料、快速迭代 | Schema 彈性、水平擴展 | 不適合複雜關聯 |

---

### 7.2 Prisma / TypeORM / Sequelize 比較

#### ORM 比較表

| 特性 | Prisma | TypeORM | Sequelize |
|------|--------|---------|-----------|
| **TypeScript 支援** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **學習曲線** | 低 | 中 | 中 |
| **型別安全** | 自動生成，極佳 | 需手動維護 | 較弱 |
| **Migration** | 內建優秀 | 內建 | 內建 |
| **Query Builder** | 有限 | 強大 | 強大 |
| **Raw SQL 支援** | 支援 | 支援 | 支援 |
| **關聯處理** | 宣告式，直觀 | Decorator 式 | 設定式 |
| **效能** | 良好 | 良好 | 良好 |
| **社群活躍度** | 高（快速成長） | 高 | 中 |

#### Prisma 範例（推薦）

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
  email     String   @unique
  name      String
  orders    Order[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([email])
}

model Order {
  id          String      @id @default(uuid())
  userId      String
  user        User        @relation(fields: [userId], references: [id])
  items       OrderItem[]
  totalAmount Decimal     @db.Decimal(10, 2)
  status      OrderStatus @default(PENDING)
  createdAt   DateTime    @default(now())
  updatedAt   DateTime    @updatedAt

  @@index([userId])
  @@index([status])
}

model OrderItem {
  id        String  @id @default(uuid())
  orderId   String
  order     Order   @relation(fields: [orderId], references: [id])
  productId String
  quantity  Int
  unitPrice Decimal @db.Decimal(10, 2)
}

enum OrderStatus {
  PENDING
  CONFIRMED
  SHIPPED
  DELIVERED
  CANCELLED
}
```

```typescript
// user.repository.ts
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { User, Prisma } from '@prisma/client';

@Injectable()
export class UserRepository {
  constructor(private readonly prisma: PrismaService) {}

  async findById(id: string): Promise<User | null> {
    return this.prisma.user.findUnique({
      where: { id },
    });
  }

  async findByIdWithOrders(id: string) {
    return this.prisma.user.findUnique({
      where: { id },
      include: {
        orders: {
          include: { items: true },
          orderBy: { createdAt: 'desc' },
          take: 10,
        },
      },
    });
  }

  async create(data: Prisma.UserCreateInput): Promise<User> {
    return this.prisma.user.create({ data });
  }

  async findMany(params: {
    skip?: number;
    take?: number;
    where?: Prisma.UserWhereInput;
    orderBy?: Prisma.UserOrderByWithRelationInput;
  }) {
    const { skip, take, where, orderBy } = params;
    return this.prisma.user.findMany({
      skip,
      take,
      where,
      orderBy,
    });
  }
}
```

#### TypeORM 範例

```typescript
// entities/user.entity.ts
import {
  Entity, PrimaryGeneratedColumn, Column,
  CreateDateColumn, UpdateDateColumn, OneToMany, Index
} from 'typeorm';
import { Order } from './order.entity';

@Entity('users')
export class User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Index()
  @Column({ unique: true })
  email: string;

  @Column()
  name: string;

  @OneToMany(() => Order, order => order.user)
  orders: Order[];

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;
}

// user.repository.ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from './entities/user.entity';

@Injectable()
export class UserRepository {
  constructor(
    @InjectRepository(User)
    private readonly repository: Repository<User>,
  ) {}

  async findByIdWithOrders(id: string): Promise<User | null> {
    return this.repository.findOne({
      where: { id },
      relations: ['orders', 'orders.items'],
    });
  }

  // 使用 QueryBuilder 進行複雜查詢
  async findUsersWithOrderStats() {
    return this.repository
      .createQueryBuilder('user')
      .leftJoin('user.orders', 'order')
      .select('user.id', 'userId')
      .addSelect('user.name', 'userName')
      .addSelect('COUNT(order.id)', 'orderCount')
      .addSelect('SUM(order.totalAmount)', 'totalSpent')
      .groupBy('user.id')
      .getRawMany();
  }
}
```

---

### 7.3 Transaction、Migration、效能調校

#### Transaction 管理

```typescript
// Prisma Transaction
async function transferMoney(
  fromAccountId: string,
  toAccountId: string,
  amount: number,
): Promise<void> {
  await prisma.$transaction(async (tx) => {
    // 1. 扣款
    const fromAccount = await tx.account.update({
      where: { id: fromAccountId },
      data: { balance: { decrement: amount } },
    });

    if (fromAccount.balance < 0) {
      throw new Error('Insufficient balance');
    }

    // 2. 存款
    await tx.account.update({
      where: { id: toAccountId },
      data: { balance: { increment: amount } },
    });

    // 3. 記錄交易
    await tx.transaction.create({
      data: {
        fromAccountId,
        toAccountId,
        amount,
        type: 'TRANSFER',
      },
    });
  });
}

// TypeORM Transaction
async function transferMoney(
  fromAccountId: string,
  toAccountId: string,
  amount: number,
): Promise<void> {
  await this.dataSource.transaction(async (manager) => {
    const fromAccount = await manager.findOne(Account, {
      where: { id: fromAccountId },
      lock: { mode: 'pessimistic_write' },  // 悲觀鎖
    });

    if (fromAccount.balance < amount) {
      throw new Error('Insufficient balance');
    }

    fromAccount.balance -= amount;
    await manager.save(fromAccount);

    const toAccount = await manager.findOne(Account, {
      where: { id: toAccountId },
    });
    toAccount.balance += amount;
    await manager.save(toAccount);
  });
}
```

#### Migration 最佳實務

```bash
# Prisma Migration
npx prisma migrate dev --name add_user_phone  # 開發環境
npx prisma migrate deploy                      # 正式環境

# TypeORM Migration
npx typeorm migration:generate -d src/data-source.ts -n AddUserPhone
npx typeorm migration:run -d src/data-source.ts
```

```typescript
// TypeORM Migration 範例
import { MigrationInterface, QueryRunner, TableColumn } from 'typeorm';

export class AddUserPhone1234567890 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.addColumn(
      'users',
      new TableColumn({
        name: 'phone',
        type: 'varchar',
        length: '20',
        isNullable: true,
      }),
    );
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropColumn('users', 'phone');
  }
}
```

#### 效能調校重點

| 問題 | 解法 |
|------|------|
| N+1 Query | 使用 `include` / `relations` 預載入 |
| 大量資料 | 分頁、游標分頁、串流處理 |
| 複雜查詢慢 | 建立適當索引、分析執行計畫 |
| 連線不足 | 調整連線池大小 |

```typescript
// 連線池設定（Prisma）
// 在 DATABASE_URL 加上參數
// postgresql://user:pass@host:5432/db?connection_limit=20&pool_timeout=30

// TypeORM 連線池
{
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  extra: {
    max: 20,              // 最大連線數
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000,
  },
}
```

---

### 7.4 連線池與資源管理

#### 連線池概念

```mermaid
graph LR
    subgraph "Node.js Application"
        A[Request 1]
        B[Request 2]
        C[Request 3]
    end
    
    subgraph "Connection Pool"
        D[Conn 1]
        E[Conn 2]
        F[Conn 3]
        G[Conn 4]
        H[Conn 5]
    end
    
    subgraph "Database"
        I[(PostgreSQL)]
    end
    
    A --> D
    B --> E
    C --> F
    D --> I
    E --> I
    F --> I
```

#### 正確的連線管理

```typescript
// prisma/prisma.service.ts
import { Injectable, OnModuleInit, OnModuleDestroy } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit, OnModuleDestroy {
  constructor() {
    super({
      log: [
        { emit: 'event', level: 'query' },
        { emit: 'stdout', level: 'error' },
        { emit: 'stdout', level: 'warn' },
      ],
    });
  }

  async onModuleInit() {
    await this.$connect();
    
    // 開發環境記錄慢查詢
    if (process.env.NODE_ENV === 'development') {
      this.$on('query' as never, (e: any) => {
        if (e.duration > 100) {  // 超過 100ms
          console.warn(`Slow query (${e.duration}ms): ${e.query}`);
        }
      });
    }
  }

  async onModuleDestroy() {
    await this.$disconnect();
  }
}
```

---

## 第 8 章：快取與效能優化

### 8.1 Redis 使用場景

#### Redis 常見用途

```mermaid
graph TD
    A[Redis 使用場景] --> B[快取]
    A --> C[Session 儲存]
    A --> D[Rate Limiting]
    A --> E[排行榜]
    A --> F[Pub/Sub]
    A --> G[分散式鎖]
    
    B --> B1[API Response Cache]
    B --> B2[Database Query Cache]
    C --> C1[User Session]
    D --> D1[API 限流]
    E --> E1[Sorted Set]
    F --> F1[即時通知]
    G --> G1[防止重複執行]
```

#### NestJS Cache 整合

```typescript
// cache/cache.module.ts
import { Module } from '@nestjs/common';
import { CacheModule } from '@nestjs/cache-manager';
import { redisStore } from 'cache-manager-redis-yet';

@Module({
  imports: [
    CacheModule.registerAsync({
      isGlobal: true,
      useFactory: async () => ({
        store: await redisStore({
          socket: {
            host: process.env.REDIS_HOST,
            port: parseInt(process.env.REDIS_PORT, 10),
          },
          ttl: 60 * 1000,  // 預設 60 秒
        }),
      }),
    }),
  ],
})
export class RedisCacheModule {}

// user.service.ts
import { Injectable, Inject } from '@nestjs/common';
import { CACHE_MANAGER } from '@nestjs/cache-manager';
import { Cache } from 'cache-manager';

@Injectable()
export class UserService {
  constructor(
    @Inject(CACHE_MANAGER) private cacheManager: Cache,
    private readonly userRepository: UserRepository,
  ) {}

  async findById(id: string): Promise<User> {
    const cacheKey = `user:${id}`;
    
    // 1. 嘗試從快取取得
    const cached = await this.cacheManager.get<User>(cacheKey);
    if (cached) {
      return cached;
    }

    // 2. 從資料庫取得
    const user = await this.userRepository.findById(id);
    
    // 3. 存入快取
    if (user) {
      await this.cacheManager.set(cacheKey, user, 300 * 1000);  // 5 分鐘
    }

    return user;
  }

  async update(id: string, data: UpdateUserDto): Promise<User> {
    const user = await this.userRepository.update(id, data);
    
    // 更新後清除快取
    await this.cacheManager.del(`user:${id}`);
    
    return user;
  }
}
```

#### 使用 Decorator 進行快取

```typescript
// common/decorators/cache.decorator.ts
import { SetMetadata } from '@nestjs/common';

export const CACHE_KEY_METADATA = 'cache_key';
export const CACHE_TTL_METADATA = 'cache_ttl';

export const Cacheable = (key: string, ttl: number = 60) => {
  return (target: any, propertyKey: string, descriptor: PropertyDescriptor) => {
    SetMetadata(CACHE_KEY_METADATA, key)(target, propertyKey, descriptor);
    SetMetadata(CACHE_TTL_METADATA, ttl)(target, propertyKey, descriptor);
  };
};

// 使用方式
@Controller('api/products')
export class ProductController {
  @Get()
  @Cacheable('products:list', 300)
  async findAll(): Promise<Product[]> {
    return this.productService.findAll();
  }
}
```

---

### 8.2 HTTP Cache / CDN

#### HTTP Cache 標頭設定

```typescript
// common/interceptors/http-cache.interceptor.ts
import {
  Injectable, NestInterceptor, ExecutionContext, CallHandler
} from '@nestjs/common';
import { Response } from 'express';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class HttpCacheInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const response = context.switchToHttp().getResponse<Response>();
    
    return next.handle().pipe(
      tap(() => {
        // 設定快取標頭
        response.setHeader('Cache-Control', 'public, max-age=300');
        response.setHeader('ETag', this.generateETag());
      }),
    );
  }

  private generateETag(): string {
    return `"${Date.now().toString(36)}"`;
  }
}

// 或使用 NestJS 內建的 CacheInterceptor
@Controller('api/public')
@UseInterceptors(CacheInterceptor)
export class PublicController {
  @Get('config')
  @CacheTTL(3600)  // 1 小時
  getPublicConfig() {
    return this.configService.getPublicConfig();
  }
}
```

---

### 8.3 Rate Limit

#### 實作 Rate Limiting

```typescript
// rate-limit/rate-limit.guard.ts
import { Injectable, CanActivate, ExecutionContext, HttpException, HttpStatus } from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { Redis } from 'ioredis';

@Injectable()
export class RateLimitGuard implements CanActivate {
  private redis: Redis;

  constructor(private reflector: Reflector) {
    this.redis = new Redis({
      host: process.env.REDIS_HOST,
      port: parseInt(process.env.REDIS_PORT, 10),
    });
  }

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const response = context.switchToHttp().getResponse();

    // 取得設定
    const limit = this.reflector.get<number>('rateLimit', context.getHandler()) || 100;
    const window = this.reflector.get<number>('rateLimitWindow', context.getHandler()) || 60;

    // 識別用戶（IP 或 User ID）
    const identifier = request.user?.id || request.ip;
    const key = `rate_limit:${context.getHandler().name}:${identifier}`;

    // 使用 Redis 計數
    const current = await this.redis.incr(key);
    
    if (current === 1) {
      await this.redis.expire(key, window);
    }

    // 設定回應標頭
    const ttl = await this.redis.ttl(key);
    response.setHeader('X-RateLimit-Limit', limit);
    response.setHeader('X-RateLimit-Remaining', Math.max(0, limit - current));
    response.setHeader('X-RateLimit-Reset', Date.now() + ttl * 1000);

    if (current > limit) {
      throw new HttpException(
        'Too Many Requests',
        HttpStatus.TOO_MANY_REQUESTS,
      );
    }

    return true;
  }
}

// 使用 Decorator
export const RateLimit = (limit: number, windowSeconds: number = 60) => {
  return applyDecorators(
    SetMetadata('rateLimit', limit),
    SetMetadata('rateLimitWindow', windowSeconds),
    UseGuards(RateLimitGuard),
  );
};

// Controller 使用
@Controller('api/auth')
export class AuthController {
  @Post('login')
  @RateLimit(5, 60)  // 每分鐘最多 5 次
  async login(@Body() dto: LoginDto) {
    return this.authService.login(dto);
  }
}
```

---

### 8.4 Memory Leak 與效能監控

#### 常見 Memory Leak 原因

| 原因 | 說明 | 解法 |
|------|------|------|
| 未清理的 Event Listener | `emitter.on()` 沒有對應的 `off()` | 使用 `once()` 或在銷毀時移除 |
| 全域變數累積 | 全域陣列/物件持續增長 | 定期清理或使用 WeakMap |
| 閉包持有大物件 | Callback 持有不必要的參考 | 縮小閉包範圍 |
| 未關閉的連線 | DB/Redis 連線未正確關閉 | 實作 `onModuleDestroy` |
| Timer 未清除 | `setInterval` 未清除 | 在銷毀時 `clearInterval` |

#### 記憶體監控

```typescript
// monitoring/memory.service.ts
import { Injectable, Logger } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';

@Injectable()
export class MemoryMonitorService {
  private readonly logger = new Logger(MemoryMonitorService.name);

  @Cron(CronExpression.EVERY_MINUTE)
  checkMemoryUsage() {
    const usage = process.memoryUsage();
    
    const formatMB = (bytes: number) => (bytes / 1024 / 1024).toFixed(2);
    
    this.logger.log({
      message: 'Memory usage',
      heapUsed: `${formatMB(usage.heapUsed)} MB`,
      heapTotal: `${formatMB(usage.heapTotal)} MB`,
      rss: `${formatMB(usage.rss)} MB`,
      external: `${formatMB(usage.external)} MB`,
    });

    // 警告門檻
    const heapUsedMB = usage.heapUsed / 1024 / 1024;
    if (heapUsedMB > 500) {
      this.logger.warn(`High memory usage: ${heapUsedMB.toFixed(2)} MB`);
    }
  }
}
```

---

## 第 9 章：安全性設計

### 9.1 身分驗證（JWT / OAuth2 / OIDC）

#### JWT 實作

```typescript
// auth/auth.module.ts
import { Module } from '@nestjs/common';
import { JwtModule } from '@nestjs/jwt';
import { PassportModule } from '@nestjs/passport';
import { JwtStrategy } from './strategies/jwt.strategy';

@Module({
  imports: [
    PassportModule.register({ defaultStrategy: 'jwt' }),
    JwtModule.registerAsync({
      useFactory: (configService: ConfigService) => ({
        secret: configService.get('JWT_SECRET'),
        signOptions: {
          expiresIn: '15m',  // Access Token 短效期
          issuer: 'your-app',
        },
      }),
      inject: [ConfigService],
    }),
  ],
  providers: [AuthService, JwtStrategy],
  exports: [AuthService],
})
export class AuthModule {}

// auth/strategies/jwt.strategy.ts
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PassportStrategy } from '@nestjs/passport';
import { ExtractJwt, Strategy } from 'passport-jwt';

interface JwtPayload {
  sub: string;  // User ID
  email: string;
  roles: string[];
  iat: number;
  exp: number;
}

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor(
    private readonly configService: ConfigService,
    private readonly userService: UserService,
  ) {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      ignoreExpiration: false,
      secretOrKey: configService.get('JWT_SECRET'),
    });
  }

  async validate(payload: JwtPayload) {
    const user = await this.userService.findById(payload.sub);
    if (!user || !user.isActive) {
      throw new UnauthorizedException();
    }
    return { id: user.id, email: user.email, roles: payload.roles };
  }
}

// auth/auth.service.ts
@Injectable()
export class AuthService {
  constructor(
    private readonly jwtService: JwtService,
    private readonly userService: UserService,
    private readonly refreshTokenService: RefreshTokenService,
  ) {}

  async login(dto: LoginDto): Promise<TokenResponse> {
    const user = await this.validateUser(dto.email, dto.password);
    
    const payload: JwtPayload = {
      sub: user.id,
      email: user.email,
      roles: user.roles,
    };

    const accessToken = this.jwtService.sign(payload);
    const refreshToken = await this.refreshTokenService.create(user.id);

    return {
      accessToken,
      refreshToken,
      expiresIn: 900,  // 15 分鐘
    };
  }

  async refresh(refreshToken: string): Promise<TokenResponse> {
    const stored = await this.refreshTokenService.validate(refreshToken);
    if (!stored) {
      throw new UnauthorizedException('Invalid refresh token');
    }

    const user = await this.userService.findById(stored.userId);
    // ... 產生新的 tokens
  }
}
```

#### OAuth2 / OIDC 整合

```typescript
// auth/strategies/google.strategy.ts
import { Injectable } from '@nestjs/common';
import { PassportStrategy } from '@nestjs/passport';
import { Strategy, VerifyCallback } from 'passport-google-oauth20';

@Injectable()
export class GoogleStrategy extends PassportStrategy(Strategy, 'google') {
  constructor(private readonly configService: ConfigService) {
    super({
      clientID: configService.get('GOOGLE_CLIENT_ID'),
      clientSecret: configService.get('GOOGLE_CLIENT_SECRET'),
      callbackURL: configService.get('GOOGLE_CALLBACK_URL'),
      scope: ['email', 'profile'],
    });
  }

  async validate(
    accessToken: string,
    refreshToken: string,
    profile: any,
    done: VerifyCallback,
  ) {
    const { emails, displayName, photos } = profile;
    
    const user = {
      email: emails[0].value,
      name: displayName,
      picture: photos[0]?.value,
      provider: 'google',
    };

    done(null, user);
  }
}
```

---

### 9.2 API Security Best Practices

#### 安全性檢查清單

```typescript
// main.ts - 安全性設定
import helmet from 'helmet';
import * as compression from 'compression';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // 1. Helmet - HTTP 安全標頭
  app.use(helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        imgSrc: ["'self'", 'data:', 'https:'],
        scriptSrc: ["'self'"],
      },
    },
    hsts: {
      maxAge: 31536000,
      includeSubDomains: true,
    },
  }));

  // 2. CORS 設定
  app.enableCors({
    origin: process.env.ALLOWED_ORIGINS?.split(',') || [],
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
    credentials: true,
    maxAge: 86400,
  });

  // 3. 限制請求大小
  app.use(express.json({ limit: '10mb' }));
  app.use(express.urlencoded({ limit: '10mb', extended: true }));

  // 4. 壓縮
  app.use(compression());

  // 5. 全域驗證 Pipe
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,           // 移除未定義的屬性
      forbidNonWhitelisted: true, // 有未定義屬性則報錯
      transform: true,
      transformOptions: {
        enableImplicitConversion: true,
      },
    }),
  );

  await app.listen(3000);
}
```

#### 防止常見攻擊

```typescript
// 1. SQL Injection - 使用參數化查詢
// ❌ 錯誤
const user = await prisma.$queryRaw`SELECT * FROM users WHERE email = ${email}`;

// ✅ 正確（Prisma 自動參數化）
const user = await prisma.user.findUnique({ where: { email } });

// 2. XSS - 輸出編碼
import * as sanitizeHtml from 'sanitize-html';

const cleanContent = sanitizeHtml(userInput, {
  allowedTags: ['b', 'i', 'em', 'strong', 'a'],
  allowedAttributes: {
    'a': ['href'],
  },
});

// 3. CSRF - 使用 CSRF Token
import * as csurf from 'csurf';
app.use(csurf({ cookie: true }));
```

---

### 9.3 資料驗證與 Injection 防護

#### 嚴格的輸入驗證

```typescript
// dto/create-user.dto.ts
import {
  IsString, IsEmail, MinLength, MaxLength,
  Matches, IsOptional, IsEnum
} from 'class-validator';
import { Transform } from 'class-transformer';

export class CreateUserDto {
  @IsEmail()
  @Transform(({ value }) => value.toLowerCase().trim())
  email: string;

  @IsString()
  @MinLength(8)
  @MaxLength(100)
  @Matches(
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$/,
    { message: '密碼必須包含大小寫字母、數字和特殊字元' },
  )
  password: string;

  @IsString()
  @MinLength(2)
  @MaxLength(50)
  @Matches(/^[\u4e00-\u9fa5a-zA-Z\s]+$/, { message: '姓名只能包含中英文字元' })
  @Transform(({ value }) => value.trim())
  name: string;

  @IsOptional()
  @IsString()
  @Matches(/^09\d{8}$/, { message: '請輸入有效的手機號碼' })
  phone?: string;
}
```

---

### 9.4 Secrets 管理與環境變數設計

#### 環境變數最佳實務

```typescript
// config/configuration.ts
import { z } from 'zod';

// 使用 Zod 驗證環境變數
const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'staging', 'production']),
  PORT: z.string().transform(Number).default('3000'),
  
  // Database
  DATABASE_URL: z.string().url(),
  
  // Redis
  REDIS_HOST: z.string(),
  REDIS_PORT: z.string().transform(Number),
  
  // JWT
  JWT_SECRET: z.string().min(32),
  JWT_EXPIRES_IN: z.string().default('15m'),
  
  // External Services
  SMTP_HOST: z.string().optional(),
  SMTP_PORT: z.string().transform(Number).optional(),
});

export type EnvConfig = z.infer<typeof envSchema>;

export function validateEnv(): EnvConfig {
  const result = envSchema.safeParse(process.env);
  
  if (!result.success) {
    console.error('❌ Invalid environment variables:');
    console.error(result.error.format());
    process.exit(1);
  }
  
  return result.data;
}

// main.ts
const config = validateEnv();
```

#### .env 檔案範本

```bash
# .env.example（提交到 Git）
NODE_ENV=development
PORT=3000

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/myapp

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT（請使用至少 32 字元的隨機字串）
JWT_SECRET=your-super-secret-key-at-least-32-characters
JWT_EXPIRES_IN=15m

# 注意：正式環境請使用 Vault 或雲端 Secret Manager
```

#### ⚠️ 重要提醒

> **絕對不要：**
> - 將 `.env` 檔案提交到 Git
> - 在程式碼中硬編碼密鑰
> - 在 Log 中輸出敏感資訊
>
> **建議使用：**
> - HashiCorp Vault
> - AWS Secrets Manager
> - Azure Key Vault
> - GCP Secret Manager

---

## 第 10 章：測試策略

### 10.1 單元測試（Jest / Vitest）

#### Jest 設定

```javascript
// jest.config.js
module.exports = {
  moduleFileExtensions: ['js', 'json', 'ts'],
  rootDir: 'src',
  testRegex: '.*\\.spec\\.ts$',
  transform: {
    '^.+\\.(t|j)s$': 'ts-jest',
  },
  collectCoverageFrom: ['**/*.(t|j)s'],
  coverageDirectory: '../coverage',
  testEnvironment: 'node',
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/$1',
  },
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

#### 單元測試範例

```typescript
// user.service.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { UserService } from './user.service';
import { UserRepository } from './user.repository';
import { NotFoundException } from '@nestjs/common';

describe('UserService', () => {
  let service: UserService;
  let repository: jest.Mocked<UserRepository>;

  beforeEach(async () => {
    const mockRepository = {
      findById: jest.fn(),
      create: jest.fn(),
      update: jest.fn(),
    };

    const module: TestingModule = await Test.createTestingModule({
      providers: [
        UserService,
        { provide: UserRepository, useValue: mockRepository },
      ],
    }).compile();

    service = module.get<UserService>(UserService);
    repository = module.get(UserRepository);
  });

  describe('findById', () => {
    it('should return user when found', async () => {
      // Arrange
      const mockUser = { id: '1', email: 'test@test.com', name: 'Test' };
      repository.findById.mockResolvedValue(mockUser);

      // Act
      const result = await service.findById('1');

      // Assert
      expect(result).toEqual(mockUser);
      expect(repository.findById).toHaveBeenCalledWith('1');
    });

    it('should throw NotFoundException when user not found', async () => {
      // Arrange
      repository.findById.mockResolvedValue(null);

      // Act & Assert
      await expect(service.findById('1')).rejects.toThrow(NotFoundException);
    });
  });

  describe('create', () => {
    it('should create and return new user', async () => {
      // Arrange
      const dto = { email: 'new@test.com', name: 'New User', password: 'pass123' };
      const mockUser = { id: '1', ...dto };
      repository.create.mockResolvedValue(mockUser);

      // Act
      const result = await service.create(dto);

      // Assert
      expect(result).toEqual(mockUser);
      expect(repository.create).toHaveBeenCalledWith(
        expect.objectContaining({ email: dto.email }),
      );
    });
  });
});
```

---

### 10.2 整合測試（Supertest）

```typescript
// test/user.e2e-spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { INestApplication, ValidationPipe } from '@nestjs/common';
import * as request from 'supertest';
import { AppModule } from '../src/app.module';
import { PrismaService } from '../src/prisma/prisma.service';

describe('UserController (e2e)', () => {
  let app: INestApplication;
  let prisma: PrismaService;
  let authToken: string;

  beforeAll(async () => {
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    app.useGlobalPipes(new ValidationPipe({ whitelist: true }));
    
    prisma = app.get<PrismaService>(PrismaService);
    
    await app.init();

    // 取得測試用 Token
    const loginResponse = await request(app.getHttpServer())
      .post('/api/auth/login')
      .send({ email: 'test@test.com', password: 'password123' });
    
    authToken = loginResponse.body.accessToken;
  });

  afterAll(async () => {
    await prisma.$disconnect();
    await app.close();
  });

  describe('GET /api/users/:id', () => {
    it('should return user data', () => {
      return request(app.getHttpServer())
        .get('/api/users/1')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(200)
        .expect((res) => {
          expect(res.body).toHaveProperty('id');
          expect(res.body).toHaveProperty('email');
        });
    });

    it('should return 401 without auth token', () => {
      return request(app.getHttpServer())
        .get('/api/users/1')
        .expect(401);
    });

    it('should return 404 for non-existent user', () => {
      return request(app.getHttpServer())
        .get('/api/users/non-existent-id')
        .set('Authorization', `Bearer ${authToken}`)
        .expect(404);
    });
  });

  describe('POST /api/users', () => {
    it('should create new user', () => {
      return request(app.getHttpServer())
        .post('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          email: `test-${Date.now()}@test.com`,
          name: 'New User',
          password: 'Password123!',
        })
        .expect(201)
        .expect((res) => {
          expect(res.body).toHaveProperty('id');
        });
    });

    it('should return 400 for invalid data', () => {
      return request(app.getHttpServer())
        .post('/api/users')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          email: 'invalid-email',
          name: '',
        })
        .expect(400);
    });
  });
});
```

---

### 10.3 Test Pyramid

```mermaid
graph TD
    subgraph "測試金字塔"
        A[E2E Tests<br/>少量、慢、昂貴]
        B[Integration Tests<br/>適量]
        C[Unit Tests<br/>大量、快、便宜]
    end
    
    A --> |10%| D[驗證完整流程]
    B --> |20%| E[驗證模組整合]
    C --> |70%| F[驗證單一功能]
```

#### 測試比例建議

| 測試類型 | 比例 | 執行時間 | 涵蓋範圍 |
|----------|------|----------|----------|
| 單元測試 | 70% | 毫秒級 | 單一函數/類別 |
| 整合測試 | 20% | 秒級 | 模組間互動 |
| E2E 測試 | 10% | 分鐘級 | 完整使用者流程 |

---

### 10.4 Mock / Stub 使用時機

#### Mock vs Stub vs Spy

| 類型 | 用途 | 範例 |
|------|------|------|
| **Mock** | 完全取代，驗證互動 | 驗證 service 有呼叫 repository |
| **Stub** | 提供預設回傳值 | 讓 repository 回傳固定資料 |
| **Spy** | 包裝真實物件，追蹤呼叫 | 追蹤真實方法被呼叫幾次 |

```typescript
// Mock 範例
const mockEmailService = {
  send: jest.fn().mockResolvedValue({ messageId: '123' }),
};

// 驗證呼叫
expect(mockEmailService.send).toHaveBeenCalledWith(
  'user@test.com',
  'Welcome',
  expect.any(String),
);

// Stub 範例
const stubUserRepository = {
  findById: jest.fn().mockResolvedValue({
    id: '1',
    email: 'test@test.com',
    name: 'Test User',
  }),
};

// Spy 範例
const realService = new UserService(repository);
const spy = jest.spyOn(realService, 'validateUser');

await realService.create(dto);

expect(spy).toHaveBeenCalledTimes(1);
spy.mockRestore();
```

---

> 📌 **第 6-10 章重點回顧**：
> 1. async/await 要正確使用，善用 Promise.all 平行處理
> 2. 長時間任務使用 Queue 處理，避免阻塞主執行緒
> 3. 選擇適合的 ORM（推薦 Prisma），注意 Transaction 與連線池
> 4. 快取策略：Redis + HTTP Cache，注意失效策略
> 5. 安全性是第一優先：驗證、加密、限流、CORS
> 6. 測試金字塔：70% 單元測試、20% 整合測試、10% E2E

---

## 第 11 章：Logging、Monitoring 與 Observability

### 11.1 Logging 設計原則（Winston / Pino）

#### Logging 層級定義

| 層級 | 用途 | 範例 |
|------|------|------|
| **error** | 系統錯誤，需要立即處理 | 資料庫連線失敗、未處理例外 |
| **warn** | 潛在問題，不影響功能 | 重試次數過多、即將到期的 token |
| **info** | 重要業務事件 | 使用者登入、訂單建立 |
| **debug** | 開發除錯資訊 | 詳細執行流程、變數值 |
| **verbose** | 更詳細的資訊 | 詳細請求/回應內容 |

#### Pino Logger 設定（推薦，效能最佳）

```typescript
// common/logger/logger.service.ts
import { Injectable, LoggerService as NestLoggerService } from '@nestjs/common';
import pino, { Logger } from 'pino';

@Injectable()
export class LoggerService implements NestLoggerService {
  private readonly logger: Logger;

  constructor() {
    this.logger = pino({
      level: process.env.LOG_LEVEL || 'info',
      transport:
        process.env.NODE_ENV === 'development'
          ? {
              target: 'pino-pretty',
              options: {
                colorize: true,
                translateTime: 'SYS:standard',
                ignore: 'pid,hostname',
              },
            }
          : undefined,
      formatters: {
        level: (label) => ({ level: label }),
      },
      base: {
        env: process.env.NODE_ENV,
        service: process.env.SERVICE_NAME || 'api',
      },
    });
  }

  log(message: string, context?: string) {
    this.logger.info({ context }, message);
  }

  error(message: string, trace?: string, context?: string) {
    this.logger.error({ context, trace }, message);
  }

  warn(message: string, context?: string) {
    this.logger.warn({ context }, message);
  }

  debug(message: string, context?: string) {
    this.logger.debug({ context }, message);
  }

  // 結構化 Log（推薦）
  logWithData(level: string, message: string, data: Record<string, unknown>) {
    this.logger[level]({ ...data }, message);
  }
}

// 使用範例
@Injectable()
export class OrderService {
  constructor(private readonly logger: LoggerService) {}

  async createOrder(dto: CreateOrderDto): Promise<Order> {
    this.logger.logWithData('info', 'Creating order', {
      userId: dto.userId,
      itemCount: dto.items.length,
    });

    try {
      const order = await this.orderRepository.create(dto);
      
      this.logger.logWithData('info', 'Order created successfully', {
        orderId: order.id,
        totalAmount: order.totalAmount,
      });
      
      return order;
    } catch (error) {
      this.logger.logWithData('error', 'Failed to create order', {
        userId: dto.userId,
        error: error.message,
        stack: error.stack,
      });
      throw error;
    }
  }
}
```

#### Request Logging Middleware

```typescript
// common/middleware/request-logger.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import { v4 as uuidv4 } from 'uuid';

@Injectable()
export class RequestLoggerMiddleware implements NestMiddleware {
  constructor(private readonly logger: LoggerService) {}

  use(req: Request, res: Response, next: NextFunction) {
    const requestId = req.headers['x-request-id'] || uuidv4();
    const startTime = Date.now();

    // 設定 Request ID
    req['requestId'] = requestId;
    res.setHeader('X-Request-Id', requestId);

    // 記錄請求
    this.logger.logWithData('info', 'Incoming request', {
      requestId,
      method: req.method,
      url: req.url,
      userAgent: req.headers['user-agent'],
      ip: req.ip,
    });

    // 攔截回應
    res.on('finish', () => {
      const duration = Date.now() - startTime;
      
      this.logger.logWithData('info', 'Request completed', {
        requestId,
        method: req.method,
        url: req.url,
        statusCode: res.statusCode,
        duration: `${duration}ms`,
      });
    });

    next();
  }
}
```

#### ⚠️ Logging 最佳實務

> **應該記錄：**
> - 所有 API 請求/回應（包含耗時）
> - 重要業務事件（訂單、付款、登入）
> - 錯誤與例外（含堆疊追蹤）
> - 外部服務呼叫結果
>
> **不應該記錄：**
> - 密碼、Token、信用卡號等敏感資訊
> - 大量重複的 Debug 訊息（正式環境）
> - 完整的請求/回應 Body（除非除錯需要）

---

### 11.2 Metrics 與 Tracing（OpenTelemetry）

#### OpenTelemetry 整合

```typescript
// telemetry/telemetry.module.ts
import { Module } from '@nestjs/common';
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

export function initTelemetry() {
  const sdk = new NodeSDK({
    resource: new Resource({
      [SemanticResourceAttributes.SERVICE_NAME]: process.env.SERVICE_NAME || 'order-service',
      [SemanticResourceAttributes.SERVICE_VERSION]: process.env.SERVICE_VERSION || '1.0.0',
      [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]: process.env.NODE_ENV,
    }),
    traceExporter: new OTLPTraceExporter({
      url: process.env.OTEL_EXPORTER_OTLP_TRACES_ENDPOINT,
    }),
    metricReader: new PeriodicExportingMetricReader({
      exporter: new OTLPMetricExporter({
        url: process.env.OTEL_EXPORTER_OTLP_METRICS_ENDPOINT,
      }),
      exportIntervalMillis: 60000,
    }),
    instrumentations: [
      getNodeAutoInstrumentations({
        '@opentelemetry/instrumentation-fs': { enabled: false },
      }),
    ],
  });

  sdk.start();

  process.on('SIGTERM', () => {
    sdk.shutdown().then(() => process.exit(0));
  });
}

// main.ts
import { initTelemetry } from './telemetry/telemetry.module';

// 在 NestJS 初始化之前啟動
initTelemetry();

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // ...
}
```

#### 自訂 Metrics

```typescript
// common/metrics/metrics.service.ts
import { Injectable } from '@nestjs/common';
import { metrics, Counter, Histogram } from '@opentelemetry/api';

@Injectable()
export class MetricsService {
  private readonly meter = metrics.getMeter('order-service');
  
  private readonly orderCounter: Counter;
  private readonly orderAmountHistogram: Histogram;
  private readonly apiLatencyHistogram: Histogram;

  constructor() {
    this.orderCounter = this.meter.createCounter('orders_total', {
      description: 'Total number of orders',
    });

    this.orderAmountHistogram = this.meter.createHistogram('order_amount', {
      description: 'Order amount distribution',
      unit: 'USD',
    });

    this.apiLatencyHistogram = this.meter.createHistogram('api_latency', {
      description: 'API request latency',
      unit: 'ms',
    });
  }

  recordOrder(status: string, amount: number) {
    this.orderCounter.add(1, { status });
    this.orderAmountHistogram.record(amount, { status });
  }

  recordApiLatency(endpoint: string, method: string, statusCode: number, duration: number) {
    this.apiLatencyHistogram.record(duration, {
      endpoint,
      method,
      status_code: statusCode.toString(),
    });
  }
}
```

---

### 11.3 錯誤追蹤（如 Sentry）

#### Sentry 整合

```typescript
// main.ts
import * as Sentry from '@sentry/node';
import { nodeProfilingIntegration } from '@sentry/profiling-node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  release: process.env.SERVICE_VERSION,
  integrations: [
    nodeProfilingIntegration(),
  ],
  tracesSampleRate: process.env.NODE_ENV === 'production' ? 0.1 : 1.0,
  profilesSampleRate: 0.1,
  beforeSend(event) {
    // 過濾敏感資訊
    if (event.request?.headers) {
      delete event.request.headers['authorization'];
      delete event.request.headers['cookie'];
    }
    return event;
  },
});

// common/filters/sentry-exception.filter.ts
import { Catch, ArgumentsHost, HttpException, HttpStatus } from '@nestjs/common';
import { BaseExceptionFilter } from '@nestjs/core';
import * as Sentry from '@sentry/node';

@Catch()
export class SentryExceptionFilter extends BaseExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    // 只回報非預期的錯誤
    if (!(exception instanceof HttpException) || 
        (exception.getStatus() >= 500)) {
      Sentry.captureException(exception, {
        extra: {
          requestId: host.switchToHttp().getRequest()['requestId'],
        },
      });
    }
    
    super.catch(exception, host);
  }
}
```

---

### 11.4 生產環境可觀測性設計

#### 可觀測性三支柱

```mermaid
graph TD
    A[Observability] --> B[Logs]
    A --> C[Metrics]
    A --> D[Traces]
    
    B --> B1[結構化日誌]
    B --> B2[集中式收集]
    B --> B3[搜尋與分析]
    
    C --> C1[系統指標]
    C --> C2[業務指標]
    C --> C3[告警設定]
    
    D --> D1[分散式追蹤]
    D --> D2[效能分析]
    D --> D3[依賴關係圖]
```

#### 健康檢查端點

```typescript
// health/health.controller.ts
import { Controller, Get } from '@nestjs/common';
import {
  HealthCheck, HealthCheckService, HttpHealthIndicator,
  TypeOrmHealthIndicator, MemoryHealthIndicator, DiskHealthIndicator
} from '@nestjs/terminus';

@Controller('health')
export class HealthController {
  constructor(
    private health: HealthCheckService,
    private http: HttpHealthIndicator,
    private db: TypeOrmHealthIndicator,
    private memory: MemoryHealthIndicator,
    private disk: DiskHealthIndicator,
  ) {}

  @Get()
  @HealthCheck()
  check() {
    return this.health.check([
      // 資料庫連線
      () => this.db.pingCheck('database'),
      
      // 記憶體使用量（不超過 500MB）
      () => this.memory.checkHeap('memory_heap', 500 * 1024 * 1024),
      
      // 磁碟空間（至少 10% 剩餘）
      () => this.disk.checkStorage('storage', {
        thresholdPercent: 0.9,
        path: '/',
      }),
    ]);
  }

  @Get('liveness')
  liveness() {
    return { status: 'ok' };
  }

  @Get('readiness')
  @HealthCheck()
  readiness() {
    return this.health.check([
      () => this.db.pingCheck('database'),
    ]);
  }
}
```

---

## 第 12 章：DevOps 與部署

### 12.1 Node.js Build 與 Release 流程

#### Build 流程

```mermaid
graph LR
    A[Source Code] --> B[Install Dependencies]
    B --> C[Lint & Format Check]
    C --> D[Type Check]
    D --> E[Unit Tests]
    E --> F[Build/Compile]
    F --> G[Integration Tests]
    G --> H[Build Docker Image]
    H --> I[Push to Registry]
```

#### package.json Scripts

```json
{
  "scripts": {
    "prebuild": "rimraf dist",
    "build": "nest build",
    "build:prod": "NODE_ENV=production nest build",
    
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:debug": "nest start --debug --watch",
    "start:prod": "node dist/main",
    
    "lint": "eslint \"{src,apps,libs,test}/**/*.ts\" --fix",
    "lint:check": "eslint \"{src,apps,libs,test}/**/*.ts\"",
    "format": "prettier --write \"src/**/*.ts\" \"test/**/*.ts\"",
    "format:check": "prettier --check \"src/**/*.ts\" \"test/**/*.ts\"",
    
    "typecheck": "tsc --noEmit",
    
    "test": "jest",
    "test:watch": "jest --watch",
    "test:cov": "jest --coverage",
    "test:e2e": "jest --config ./test/jest-e2e.json",
    
    "db:migrate": "prisma migrate deploy",
    "db:migrate:dev": "prisma migrate dev",
    "db:generate": "prisma generate",
    "db:seed": "ts-node prisma/seed.ts",
    
    "prepare": "husky install"
  }
}
```

---

### 12.2 Docker 化最佳實務

#### 多階段建置 Dockerfile

```dockerfile
# Dockerfile
# ===== 階段 1: 安裝依賴 =====
FROM node:22-alpine AS deps
WORKDIR /app

# 只複製 package files（利用 Docker 快取）
COPY package.json pnpm-lock.yaml ./
RUN corepack enable pnpm && pnpm install --frozen-lockfile

# ===== 階段 2: 建置 =====
FROM node:22-alpine AS builder
WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

# 產生 Prisma Client
RUN npx prisma generate

# 建置
RUN npm run build

# 移除開發依賴
RUN corepack enable pnpm && pnpm prune --prod

# ===== 階段 3: 執行 =====
FROM node:22-alpine AS runner
WORKDIR /app

# 安全性：不使用 root
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nestjs
USER nestjs

# 只複製必要檔案
COPY --from=builder --chown=nestjs:nodejs /app/dist ./dist
COPY --from=builder --chown=nestjs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nestjs:nodejs /app/package.json ./

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health/liveness || exit 1

EXPOSE 3000

CMD ["node", "dist/main.js"]
```

#### docker-compose.yml（開發環境）

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: builder  # 開發環境使用 builder 階段
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
      - "9229:9229"  # Debug port
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/myapp
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - db
      - redis
    command: npm run start:debug

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

### 12.3 CI/CD Pipeline 設計

#### GitHub Actions 範例

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '22'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ===== 測試 =====
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'pnpm'
      
      - name: Install pnpm
        uses: pnpm/action-setup@v2
        with:
          version: 8
          
      - name: Install dependencies
        run: pnpm install --frozen-lockfile
      
      - name: Lint
        run: pnpm lint:check
        
      - name: Type Check
        run: pnpm typecheck
      
      - name: Unit Tests
        run: pnpm test:cov
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
      
      - name: E2E Tests
        run: pnpm test:e2e
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info

  # ===== 建置 =====
  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=sha,prefix=
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # ===== 部署 =====
  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    environment: staging
    
    steps:
      - name: Deploy to Staging
        run: |
          # 使用 kubectl、ArgoCD 或其他部署工具
          echo "Deploying to staging..."

  deploy-production:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
      - name: Deploy to Production
        run: |
          echo "Deploying to production..."
```

---

### 12.4 Kubernetes / Cloud Run / Serverless 部署模式

#### Kubernetes 部署設定

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  labels:
    app: order-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: order-service
  template:
    metadata:
      labels:
        app: order-service
    spec:
      containers:
        - name: order-service
          image: ghcr.io/org/order-service:latest
          ports:
            - containerPort: 3000
          env:
            - name: NODE_ENV
              value: production
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: order-service-secrets
                  key: database-url
          resources:
            requests:
              memory: "256Mi"
              cpu: "200m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health/liveness
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health/readiness
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: order-service
spec:
  selector:
    app: order-service
  ports:
    - port: 80
      targetPort: 3000
  type: ClusterIP
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-service
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-service
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

## 第 13 章：專案範本與團隊開發規範

### 13.1 企業級 Node.js 專案範本建議

#### 推薦的專案範本結構

```
enterprise-node-template/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   ├── CODEOWNERS
│   └── pull_request_template.md
├── .husky/
│   ├── pre-commit
│   └── commit-msg
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── k8s/
│   ├── base/
│   └── overlays/
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   └── seed.ts
├── src/
│   ├── main.ts
│   ├── app.module.ts
│   ├── config/
│   ├── common/
│   │   ├── decorators/
│   │   ├── filters/
│   │   ├── guards/
│   │   ├── interceptors/
│   │   ├── middleware/
│   │   └── pipes/
│   ├── modules/
│   │   └── [feature]/
│   │       ├── [feature].module.ts
│   │       ├── [feature].controller.ts
│   │       ├── [feature].service.ts
│   │       ├── [feature].repository.ts
│   │       ├── dto/
│   │       ├── entities/
│   │       └── interfaces/
│   └── infrastructure/
├── test/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
├── .env.example
├── .eslintrc.js
├── .prettierrc
├── nest-cli.json
├── package.json
├── pnpm-lock.yaml
├── tsconfig.json
├── tsconfig.build.json
└── README.md
```

---

### 13.2 Coding Style 與 Lint 規範

#### ESLint 設定

```javascript
// .eslintrc.js
module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.json',
    tsconfigRootDir: __dirname,
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint/eslint-plugin', 'import'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:import/recommended',
    'plugin:import/typescript',
    'prettier',
  ],
  root: true,
  env: {
    node: true,
    jest: true,
  },
  ignorePatterns: ['.eslintrc.js', 'dist', 'node_modules'],
  rules: {
    // TypeScript
    '@typescript-eslint/explicit-function-return-type': 'warn',
    '@typescript-eslint/explicit-module-boundary-types': 'warn',
    '@typescript-eslint/no-explicit-any': 'error',
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    '@typescript-eslint/no-floating-promises': 'error',
    '@typescript-eslint/await-thenable': 'error',
    
    // Import
    'import/order': [
      'error',
      {
        groups: ['builtin', 'external', 'internal', 'parent', 'sibling', 'index'],
        'newlines-between': 'always',
        alphabetize: { order: 'asc' },
      },
    ],
    'import/no-duplicates': 'error',
    
    // General
    'no-console': ['warn', { allow: ['warn', 'error'] }],
    'prefer-const': 'error',
    'no-var': 'error',
  },
};
```

#### Prettier 設定

```json
// .prettierrc
{
  "singleQuote": true,
  "trailingComma": "all",
  "tabWidth": 2,
  "semi": true,
  "printWidth": 100,
  "bracketSpacing": true,
  "arrowParens": "always",
  "endOfLine": "lf"
}
```

#### Git Hooks（Husky + lint-staged）

```json
// package.json
{
  "lint-staged": {
    "*.ts": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}
```

```bash
# .husky/pre-commit
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged
```

```bash
# .husky/commit-msg
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx --no -- commitlint --edit "$1"
```

---

### 13.3 Git Flow / Branch Strategy

#### 分支策略

```mermaid
gitGraph
    commit id: "Initial"
    branch develop
    checkout develop
    commit id: "Feature A start"
    branch feature/user-auth
    commit id: "Add login"
    commit id: "Add logout"
    checkout develop
    merge feature/user-auth
    branch release/1.0
    commit id: "Version bump"
    checkout main
    merge release/1.0 tag: "v1.0.0"
    checkout develop
    merge release/1.0
    commit id: "Continue dev"
```

#### 分支命名規範

| 分支類型 | 命名規則 | 範例 |
|----------|----------|------|
| 主要分支 | `main` / `develop` | - |
| 功能分支 | `feature/{ticket-id}-{description}` | `feature/PROJ-123-user-auth` |
| 修復分支 | `bugfix/{ticket-id}-{description}` | `bugfix/PROJ-456-login-error` |
| 熱修分支 | `hotfix/{ticket-id}-{description}` | `hotfix/PROJ-789-security-fix` |
| 發布分支 | `release/{version}` | `release/1.2.0` |

#### Commit Message 規範（Conventional Commits）

```
<type>(<scope>): <subject>

<body>

<footer>
```

| Type | 說明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修復 Bug |
| `docs` | 文件變更 |
| `style` | 程式碼格式（不影響功能） |
| `refactor` | 重構（不影響功能） |
| `perf` | 效能改進 |
| `test` | 測試相關 |
| `chore` | 建置/工具相關 |

範例：
```
feat(auth): add JWT refresh token support

- Implement refresh token generation
- Add token rotation on refresh
- Set up secure cookie storage

Closes #123
```

---

### 13.4 Code Review 重點清單

#### Code Review Checklist

```markdown
## 功能正確性
- [ ] 程式碼是否實現了需求？
- [ ] 邊界條件是否處理？
- [ ] 錯誤處理是否完善？

## 程式碼品質
- [ ] 命名是否清楚且一致？
- [ ] 函數是否單一職責？
- [ ] 是否有重複程式碼？
- [ ] 註解是否必要且有用？

## 安全性
- [ ] 輸入是否有驗證？
- [ ] 敏感資訊是否妥善處理？
- [ ] SQL/NoSQL 查詢是否安全？
- [ ] 認證/授權是否正確？

## 效能
- [ ] 是否有 N+1 查詢問題？
- [ ] 是否需要快取？
- [ ] 是否會阻塞 Event Loop？

## 測試
- [ ] 是否有對應的單元測試？
- [ ] 測試案例是否涵蓋主要場景？
- [ ] 測試是否容易理解和維護？

## 其他
- [ ] 是否需要更新文件？
- [ ] 是否需要資料庫 Migration？
- [ ] 是否有破壞性變更？
```

---

## 第 14 章：常見地雷與反模式

### 14.1 阻塞 Event Loop 的錯誤寫法

```typescript
// ❌ 錯誤：同步的大量運算
function processLargeData(data: any[]) {
  // 這會阻塞 Event Loop！
  for (let i = 0; i < 10000000; i++) {
    // 大量計算
  }
}

// ✅ 正確：分批處理
async function processLargeDataAsync(data: any[]) {
  const batchSize = 1000;
  for (let i = 0; i < data.length; i += batchSize) {
    const batch = data.slice(i, i + batchSize);
    await processBatch(batch);
    // 讓出 Event Loop
    await new Promise(resolve => setImmediate(resolve));
  }
}

// ✅ 正確：使用 Worker Threads
import { Worker, isMainThread, parentPort, workerData } from 'worker_threads';

if (isMainThread) {
  const worker = new Worker(__filename, {
    workerData: { data: largeData },
  });
  worker.on('message', (result) => {
    console.log('Result:', result);
  });
} else {
  const result = heavyComputation(workerData.data);
  parentPort?.postMessage(result);
}
```

---

### 14.2 Promise 使用錯誤

```typescript
// ❌ 錯誤 1：忘記 return Promise
async function getUser(id: string) {
  userRepository.findById(id);  // 沒有 return！
}

// ❌ 錯誤 2：不必要的 async
async function getValue() {
  return 'value';  // 不需要 async
}

// ✅ 正確
function getValue() {
  return 'value';
}

// ❌ 錯誤 3：混用 callback 和 Promise
function fetchData(callback) {
  return fetch('/api').then(callback);  // 混亂！
}

// ✅ 正確：統一使用 Promise
async function fetchData() {
  return fetch('/api').then(res => res.json());
}

// ❌ 錯誤 4：Promise.all 沒有錯誤處理
await Promise.all(items.map(processItem));  // 一個失敗全部失敗

// ✅ 正確：使用 allSettled 或個別處理
const results = await Promise.allSettled(items.map(processItem));
const failed = results.filter(r => r.status === 'rejected');
if (failed.length > 0) {
  // 處理失敗的項目
}
```

---

### 14.3 TypeScript 濫用 any

```typescript
// ❌ 錯誤：到處使用 any
function processData(data: any): any {
  return data.result.items.map((item: any) => item.value);
}

// ✅ 正確：定義明確的型別
interface DataItem {
  value: number;
}

interface ApiResponse {
  result: {
    items: DataItem[];
  };
}

function processData(data: ApiResponse): number[] {
  return data.result.items.map(item => item.value);
}

// ✅ 使用 unknown 取代 any（需要型別檢查）
function parseJson(json: string): unknown {
  return JSON.parse(json);
}

function processUnknown(data: unknown): void {
  // 必須先檢查型別
  if (typeof data === 'object' && data !== null && 'value' in data) {
    console.log((data as { value: unknown }).value);
  }
}
```

---

### 14.4 設計不良的 API 與資料模型

```typescript
// ❌ 錯誤：API 回傳不一致
// GET /api/users/1 回傳 { id, name, email }
// GET /api/users 回傳 [{ userId, userName, userEmail }]  // 命名不一致！

// ✅ 正確：保持一致的命名和結構
// GET /api/users/1 回傳 { id, name, email }
// GET /api/users 回傳 { items: [{ id, name, email }], total: 100, page: 1 }

// ❌ 錯誤：API 回傳過多資料
interface UserResponse {
  id: string;
  name: string;
  email: string;
  password: string;  // ❌ 絕對不要！
  internalNotes: string;  // ❌ 內部資料不應該外洩
}

// ✅ 正確：只回傳必要資料
interface UserPublicResponse {
  id: string;
  name: string;
  email: string;
}

// ❌ 錯誤：深層巢狀的 API
// GET /api/users/1/orders/2/items/3/reviews
// 太深了！

// ✅ 正確：扁平化或拆分
// GET /api/order-items/3/reviews
// 或 GET /api/reviews?orderItemId=3
```

---

## 第 15 章：總結與最佳實務建議

### 15.1 Node.js 在企業長期維運的關鍵成功因素

#### 成功關鍵

```mermaid
mindmap
  root((企業 Node.js<br/>成功關鍵))
    技術選型
      選擇成熟框架(NestJS)
      使用 TypeScript
      選擇合適的 ORM
    團隊規範
      統一 Coding Style
      Code Review 文化
      文件化習慣
    品質保證
      測試覆蓋率 > 80%
      CI/CD 自動化
      監控與告警
    架構設計
      模組化設計
      清晰的分層
      可擴展性考量
```

#### 維運要點

| 面向 | 要點 |
|------|------|
| **可維護性** | TypeScript + 清晰架構 + 充足測試 |
| **可觀測性** | 結構化 Log + Metrics + Tracing |
| **可擴展性** | 無狀態設計 + 水平擴展能力 |
| **安全性** | 定期更新依賴 + 弱掃修復 + 權限最小化 |
| **效能** | 效能監控 + 瓶頸分析 + 持續優化 |

---

### 15.2 技術選型決策建議

#### 2026 年推薦技術棧

| 類別 | 推薦選項 | 替代方案 |
|------|----------|----------|
| **Runtime** | Node.js 22 LTS | - |
| **語言** | TypeScript 5.x | - |
| **Web Framework** | NestJS | Fastify |
| **ORM** | Prisma | TypeORM |
| **驗證** | Zod + class-validator | Joi |
| **測試** | Jest / Vitest | - |
| **套件管理** | PNPM | Yarn |
| **快取** | Redis | - |
| **訊息佇列** | BullMQ | RabbitMQ |
| **Logging** | Pino | Winston |
| **Observability** | OpenTelemetry | - |
| **容器化** | Docker + K8s | Cloud Run |

---

### 15.3 學習路線與進階主題建議

#### 學習路線圖

```mermaid
graph TD
    A[基礎] --> B[進階]
    B --> C[專家]
    
    A --> A1[JavaScript/TypeScript 精通]
    A --> A2[Node.js 核心概念]
    A --> A3[NestJS 基礎]
    A --> A4[資料庫操作]
    
    B --> B1[Clean Architecture]
    B --> B2[微服務設計]
    B --> B3[效能調校]
    B --> B4[安全性深入]
    
    C --> C1[分散式系統]
    C --> C2[Event Sourcing / CQRS]
    C --> C3[領域驅動設計 DDD]
    C --> C4[SRE 實踐]
```

#### 推薦學習資源

| 主題 | 資源 |
|------|------|
| Node.js 官方 | https://nodejs.org/docs |
| NestJS 官方 | https://docs.nestjs.com |
| TypeScript 手冊 | https://www.typescriptlang.org/docs |
| Prisma 文件 | https://www.prisma.io/docs |
| Clean Architecture | 《Clean Architecture》by Robert C. Martin |
| 微服務 | 《Building Microservices》by Sam Newman |

---

## 附錄：檢查清單（Checklist）

### A. 新專案啟動檢查清單

```markdown
## 專案初始化
- [ ] 使用 NestJS CLI 建立專案
- [ ] 設定 TypeScript 嚴格模式
- [ ] 設定 ESLint + Prettier
- [ ] 設定 Husky + lint-staged
- [ ] 建立 .env.example

## 基礎架構
- [ ] 設定 Config Module（環境變數驗證）
- [ ] 設定 Logger Module（Pino）
- [ ] 設定 Database Module（Prisma）
- [ ] 設定 Cache Module（Redis）
- [ ] 設定 Health Check

## 安全性
- [ ] 設定 Helmet
- [ ] 設定 CORS
- [ ] 設定 Rate Limiting
- [ ] 設定 Validation Pipe
- [ ] 設定認證模組（JWT）

## CI/CD
- [ ] 建立 Dockerfile（多階段建置）
- [ ] 建立 docker-compose.yml
- [ ] 建立 GitHub Actions workflow
- [ ] 設定測試覆蓋率門檻

## 文件
- [ ] 設定 Swagger/OpenAPI
- [ ] 撰寫 README.md
- [ ] 建立 CONTRIBUTING.md
```

### B. Code Review 檢查清單

```markdown
## 功能
- [ ] 是否符合需求規格？
- [ ] 邊界條件是否處理？
- [ ] 錯誤情況是否處理？

## 程式碼品質
- [ ] 是否遵循專案程式碼規範？
- [ ] 命名是否清楚有意義？
- [ ] 是否有重複程式碼？
- [ ] 函數是否過長（> 50 行）？
- [ ] 是否濫用 any？

## 安全性
- [ ] 輸入驗證是否完善？
- [ ] 是否有 SQL Injection 風險？
- [ ] 敏感資訊是否妥善處理？
- [ ] 權限檢查是否正確？

## 效能
- [ ] 是否有 N+1 查詢？
- [ ] 是否需要快取？
- [ ] 是否有阻塞 Event Loop 的操作？

## 測試
- [ ] 是否有對應測試？
- [ ] 測試案例是否涵蓋主要場景？
- [ ] 測試是否容易理解？

## 文件
- [ ] API 是否有 Swagger 文件？
- [ ] 複雜邏輯是否有註解？
- [ ] 是否需要更新 README？
```

### C. 上線前檢查清單

```markdown
## 程式碼
- [ ] 所有測試通過
- [ ] 測試覆蓋率達標（>80%）
- [ ] 無 ESLint 錯誤
- [ ] 無 TypeScript 錯誤
- [ ] Code Review 已通過

## 設定
- [ ] 環境變數已設定
- [ ] Secrets 已存放到 Secret Manager
- [ ] Database Migration 已執行
- [ ] 快取已預熱（如需要）

## 監控
- [ ] Health Check 正常
- [ ] Logging 正常輸出
- [ ] Metrics 正常收集
- [ ] 告警規則已設定

## 安全性
- [ ] 弱點掃描已通過
- [ ] 依賴更新到安全版本
- [ ] HTTPS 已啟用
- [ ] 敏感資訊未外洩

## 部署
- [ ] 藍綠部署/滾動更新就緒
- [ ] Rollback 計畫已準備
- [ ] 效能測試已通過
- [ ] 上線時間已通知相關人員
```

### D. 日常維運檢查清單

```markdown
## 每日
- [ ] 檢查錯誤監控系統（Sentry）
- [ ] 檢查 Log 異常
- [ ] 檢查系統健康狀態

## 每週
- [ ] 檢查效能指標趨勢
- [ ] 檢查資源使用率
- [ ] 更新依賴（安全性更新）

## 每月
- [ ] 執行安全掃描
- [ ] 檢視並清理舊 Log
- [ ] 檢視並優化慢查詢
- [ ] 備份驗證

## 每季
- [ ] 依賴全面更新評估
- [ ] 架構檢討
- [ ] 災難復原演練
- [ ] 效能基準測試
```

---

## 版本歷史

| 版本 | 日期 | 說明 |
|------|------|------|
| 1.0.0 | 2026-02-04 | 初版發布 |

---

> **文件維護者**：架構團隊  
> **最後更新**：2026 年 2 月 4 日  
> **適用 Node.js 版本**：22 LTS+  
> **適用 NestJS 版本**：10.x+

