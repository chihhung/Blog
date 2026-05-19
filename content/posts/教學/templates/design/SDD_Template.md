+++
date = '2026-05-19T10:00:00+08:00'
draft = false
title = 'SDD（系統設計文件）範本'
tags = ['範本', '設計開發', '軟體工程']
categories = ['教學']
+++

# SDD（系統設計文件｜System Design Document）範本

> **版本**：1.0  
> **參照標準**：ISO/IEC/IEEE 42010:2022、ISO/IEC 25010:2023、ISO/IEC/IEEE 15288:2023  
> **適用對象**：系統架構師、資深開發工程師、技術主管  
> **文件性質**：系統技術架構與設計決策文件

---

## 📋 使用說明

SDD 用於制定技術解決方案，規劃「**系統要如何實作**」。內容涵蓋系統架構、資料庫綱要（Schema）、API 介面規格、模組劃分與資安規範，確保系統具備擴展性與穩定性。

### 何時使用本範本

- 系統設計階段，將需求（PRD/FRD/SRD）轉化為技術方案
- 重大架構變更前的設計評審
- 跨團隊技術溝通的基準文件

### 與其他文件的關係

```
PRD（做什麼） → SDD（如何設計） → TSD（如何實作）
     ↑                ↑                ↑
   產品經理          架構師           開發工程師
```

### 填寫原則

1. **決策可追溯**：每個設計決策需記錄原因與替代方案
2. **圖文並茂**：架構圖、序列圖、ER 圖等應完整呈現
3. **安全優先**：每個模組需考慮資安面向
4. **可演進**：設計應預留擴展空間

---

## 📄 範本正文

---

# [系統/模組名稱] 系統設計文件（SDD）

## 1. 文件資訊

| 項目 | 內容 |
|------|------|
| **文件編號** | SDD-[專案代碼]-[序號] |
| **版本** | v0.1 |
| **建立日期** | YYYY-MM-DD |
| **最後更新** | YYYY-MM-DD |
| **撰寫者** | [架構師姓名] |
| **審核者** | [審核者姓名 / 角色] |
| **核准者** | [核准者姓名 / 角色] |
| **狀態** | 草稿 / 審查中 / 已核准 |

### 版本歷程

| 版本 | 日期 | 修改人 | 修改內容摘要 |
|------|------|--------|-------------|
| v0.1 | YYYY-MM-DD | [姓名] | 初版建立 |

### 審核紀錄

| 審核者 | 角色 | 審核日期 | 結果 | 備註 |
|--------|------|----------|------|------|
| | | | 通過 / 有條件通過 / 退回 | |

### 關聯文件

| 文件名稱 | 文件編號 | 版本 | 關聯性 |
|---------|---------|------|--------|
| 產品需求文件（PRD） | PRD-XXX-001 | v1.0 | 需求來源 |
| 功能需求文件（FRD） | FRD-XXX-001 | v1.0 | 功能規格 |
| 系統需求規格書（SRD） | SRD-XXX-001 | v1.0 | 系統規格 |

---

## 2. 系統概述

### 2.1 系統背景與目標

> 簡述本系統的業務背景、核心問題，以及本設計文件欲達成的技術目標。

**系統名稱**：[系統名稱]  
**系統簡述**：[一段話描述系統用途]  
**設計目標**：
1. [技術目標 1，例：支援每秒 1,000 筆交易處理]
2. [技術目標 2，例：系統可用率 ≥ 99.99%]
3. [技術目標 3，例：水平擴展能力，支援 10 倍流量成長]

### 2.2 設計約束

| 約束類型 | 描述 | 影響範圍 |
|---------|------|---------|
| 技術約束 | 例：須使用企業標準技術棧（Java 21 + Spring Boot 3.x） | 開發框架選型 |
| 合規約束 | 例：須符合 PCI DSS 及個資法要求 | 資料處理與儲存 |
| 基礎設施約束 | 例：部署於企業私有雲 Kubernetes 環境 | 部署架構 |
| 整合約束 | 例：須整合現有 SAP ERP 系統 | 介面設計 |
| 效能約束 | 例：回應時間 95th percentile < 200ms | 架構與技術選型 |

### 2.3 利害關係人與關注面向

| 利害關係人 | 角色 | 主要關注面向 |
|-----------|------|-------------|
| 業務部門 | 產品擁有者 | 功能完整性、使用體驗 |
| 維運團隊 | SRE | 可觀測性、自動化部署 |
| 資安團隊 | 資安官 | 資安合規、弱點管理 |
| 開發團隊 | 工程師 | 可維護性、開發效率 |
| DBA | 資料庫管理 | 資料一致性、效能 |

---

## 3. 系統架構

### 3.1 架構風格

> 說明選用的架構風格與理由。

**選用架構**：[微服務架構 / 單體架構 / 模組化單體 / 事件驅動架構 / ...]

**選型理由**：

| 評估面向 | 替代方案 A | 替代方案 B | **選定方案** |
|---------|-----------|-----------|-------------|
| 開發複雜度 | 低 | 高 | 中 |
| 擴展能力 | 低 | 高 | 高 |
| 維運成本 | 低 | 高 | 中 |
| 團隊熟悉度 | 高 | 低 | 中 |
| **綜合評分** | | | ✅ |

### 3.2 系統架構圖（System Architecture Diagram）

> 繪製系統整體架構圖，展示各元件之間的關係。

```
[提供架構圖，建議使用 Mermaid、C4 Model 或 draw.io]

範例（C4 Context Diagram）：

┌──────────────────────────────────────────────┐
│              [System Name]                    │
│                                               │
│  ┌─────────┐  ┌──────────┐  ┌────────────┐  │
│  │ Web App │  │ API GW   │  │ Admin App  │  │
│  └────┬────┘  └────┬─────┘  └─────┬──────┘  │
│       │            │              │          │
│  ┌────▼────────────▼──────────────▼──────┐   │
│  │         Backend Services              │   │
│  │  ┌──────┐ ┌──────┐ ┌──────────────┐  │   │
│  │  │User  │ │Order │ │Notification  │  │   │
│  │  │Svc   │ │Svc   │ │Service       │  │   │
│  │  └──┬───┘ └──┬───┘ └──────┬───────┘  │   │
│  └─────┼────────┼────────────┼───────────┘   │
│        │        │            │               │
│  ┌─────▼────────▼────────────▼───────────┐   │
│  │         Data Layer                    │   │
│  │  ┌──────┐ ┌──────┐ ┌──────────────┐  │   │
│  │  │RDB   │ │Redis │ │Message Queue │  │   │
│  │  └──────┘ └──────┘ └──────────────┘  │   │
│  └───────────────────────────────────────┘   │
└──────────────────────────────────────────────┘
```

### 3.3 部署架構圖（Deployment Diagram）

> 繪製實際部署拓撲，包含網路區段、伺服器規格、叢集配置。

| 環境 | 配置 | 用途 |
|------|------|------|
| 開發環境（DEV） | 單節點 | 開發測試 |
| 測試環境（SIT） | 雙節點 | 整合測試 |
| 預生產環境（UAT） | 與 PRD 同規格 | 使用者驗收 |
| 生產環境（PRD） | 多節點叢集、HA 配置 | 正式服務 |

### 3.4 技術棧（Technology Stack）

| 層級 | 技術選型 | 版本 | 選型理由 |
|------|---------|------|---------|
| 前端 | React / Vue.js | 18.x / 3.x | 元件化、生態系成熟 |
| 後端 | Java + Spring Boot | 21 + 3.4.x | 企業標準、效能穩定 |
| API Gateway | Kong / Spring Cloud Gateway | 3.x | 流量控制、認證整合 |
| 資料庫 | PostgreSQL | 16.x | ACID、JSONB 支援 |
| 快取 | Redis | 7.x | 高效能、叢集支援 |
| 訊息佇列 | Apache Kafka | 3.7.x | 高吞吐、事件溯源 |
| 容器編排 | Kubernetes | 1.30.x | 自動擴展、自癒 |
| CI/CD | GitHub Actions / GitLab CI | — | 自動化建置部署 |
| 監控 | Prometheus + Grafana | — | 指標收集與視覺化 |
| 日誌 | ELK Stack | 8.x | 集中式日誌管理 |

---

## 4. 模組劃分（Module Decomposition）

### 4.1 模組清單

| 模組編號 | 模組名稱 | 職責描述 | 負責團隊 |
|---------|---------|---------|---------|
| M-001 | 使用者管理模組 | 使用者註冊、登入、權限管理 | 帳戶團隊 |
| M-002 | 訂單處理模組 | 訂單建立、狀態管理、取消 | 交易團隊 |
| M-003 | 通知服務模組 | Email、SMS、推播通知 | 平台團隊 |
| M-004 | 報表分析模組 | 資料統計、報表產出 | 數據團隊 |

### 4.2 模組依賴關係

```
[使用依賴關係圖呈現各模組之間的依賴]

M-002（訂單） ──依賴──► M-001（使用者）
M-003（通知） ◄──被調用── M-002（訂單）
M-004（報表） ──讀取──► M-001, M-002
```

### 4.3 模組詳細設計

#### M-001：使用者管理模組

**職責**：
- 使用者註冊與身分驗證
- 角色與權限管理（RBAC）
- 個人資料維護

**對外介面**：
| API | 方法 | 描述 |
|-----|------|------|
| /api/v1/users | POST | 建立使用者 |
| /api/v1/users/{id} | GET | 查詢使用者 |
| /api/v1/auth/login | POST | 登入驗證 |
| /api/v1/auth/token/refresh | POST | Token 續期 |

**內部類別結構**：
```
user-service/
├── controller/
│   ├── UserController
│   └── AuthController
├── service/
│   ├── UserService
│   ├── AuthService
│   └── RoleService
├── repository/
│   ├── UserRepository
│   └── RoleRepository
├── domain/
│   ├── User
│   ├── Role
│   └── Permission
└── config/
    └── SecurityConfig
```

---

## 5. 資料庫綱要設計（Database Schema）

### 5.1 資料庫選型與策略

| 決策 | 選擇 | 理由 |
|------|------|------|
| 主要資料庫 | PostgreSQL 16 | ACID 事務、JSONB 支援、擴充性 |
| 快取層 | Redis 7.x | 低延遲讀取、Session 管理 |
| 搜尋引擎 | Elasticsearch 8.x | 全文搜尋、日誌分析 |
| 資料分割策略 | 依租戶分表 | 資料隔離、效能保障 |

### 5.2 實體關聯圖（ER Diagram）

```
[使用 ER 圖工具或 Mermaid 繪製]

範例：
┌─────────────┐       ┌─────────────────┐
│   USERS     │       │  USER_ROLES     │
├─────────────┤       ├─────────────────┤
│ PK user_id  │──────►│ FK user_id      │
│ username    │       │ FK role_id      │
│ email       │       │ assigned_at     │
│ password    │       └────────┬────────┘
│ status      │                │
│ created_at  │       ┌────────▼────────┐
│ updated_at  │       │    ROLES        │
└─────────────┘       ├─────────────────┤
                      │ PK role_id      │
                      │ role_name       │
                      │ description     │
                      └─────────────────┘
```

### 5.3 資料表設計

#### USERS 資料表

| 欄位名稱 | 資料型別 | 空值 | 預設值 | 說明 |
|---------|---------|------|--------|------|
| user_id | BIGSERIAL | NOT NULL | AUTO | 主鍵 |
| username | VARCHAR(50) | NOT NULL | — | 使用者帳號 |
| email | VARCHAR(254) | NOT NULL | — | 電子郵件（唯一） |
| password_hash | VARCHAR(256) | NOT NULL | — | 密碼雜湊值（bcrypt） |
| display_name | VARCHAR(100) | NULL | — | 顯示名稱 |
| status | VARCHAR(20) | NOT NULL | 'ACTIVE' | 帳號狀態 |
| last_login_at | TIMESTAMPTZ | NULL | — | 最後登入時間 |
| created_at | TIMESTAMPTZ | NOT NULL | NOW() | 建立時間 |
| updated_at | TIMESTAMPTZ | NULL | — | 更新時間 |
| created_by | VARCHAR(50) | NOT NULL | — | 建立者 |
| updated_by | VARCHAR(50) | NULL | — | 更新者 |

**索引設計**：
| 索引名稱 | 索引欄位 | 類型 | 用途 |
|---------|---------|------|------|
| PK_USERS | user_id | PRIMARY KEY | 主鍵查詢 |
| UQ_USERS_EMAIL | email | UNIQUE | 避免重複 Email |
| IDX_USERS_STATUS | status | B-TREE | 狀態篩選 |

### 5.4 資料遷移策略

| 策略項目 | 說明 |
|---------|------|
| 遷移工具 | Flyway / Liquibase |
| 命名規範 | V{版本}_{日期}_{描述}.sql |
| 回滾策略 | 每個遷移腳本需附帶回滾 SQL |
| 資料量評估 | 預估各表資料量，決定是否需分區 |

---

## 6. API 介面規格（API Specification）

### 6.1 API 設計原則

| 原則 | 說明 |
|------|------|
| RESTful 風格 | 使用 HTTP Method 表達操作語意 |
| 版本控制 | URI 路徑版本（/api/v1/）|
| 統一回應格式 | 遵循標準 Response Envelope |
| 分頁與篩選 | 統一使用 page/size/sort 參數 |
| 冪等性 | PUT/DELETE 需具備冪等性 |

### 6.2 API 清單

| API 路徑 | 方法 | 描述 | 認證 | 限流 |
|---------|------|------|------|------|
| /api/v1/users | GET | 查詢使用者清單 | Bearer Token | 100/min |
| /api/v1/users | POST | 建立使用者 | Bearer Token | 10/min |
| /api/v1/users/{id} | GET | 查詢單一使用者 | Bearer Token | 200/min |
| /api/v1/users/{id} | PUT | 更新使用者 | Bearer Token | 20/min |
| /api/v1/users/{id} | DELETE | 刪除使用者 | Bearer Token | 5/min |
| /api/v1/auth/login | POST | 使用者登入 | 無 | 20/min |

### 6.3 API 詳細規格

#### POST /api/v1/users

**描述**：建立新使用者

**Request**：
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecureP@ss123",
  "displayName": "John Doe"
}
```

**Response（201 Created）**：
```json
{
  "success": true,
  "code": "0000",
  "message": "使用者建立成功",
  "data": {
    "userId": 12345,
    "username": "john_doe",
    "email": "john@example.com",
    "displayName": "John Doe",
    "status": "PENDING_VERIFICATION",
    "createdAt": "2026-05-19T10:30:00Z"
  },
  "timestamp": "2026-05-19T10:30:00Z",
  "traceId": "abc123-def456"
}
```

**Error Response（409 Conflict）**：
```json
{
  "success": false,
  "code": "E2001",
  "message": "Email 已被使用",
  "errors": [
    {
      "field": "email",
      "message": "此 Email 已註冊，請使用其他 Email"
    }
  ],
  "timestamp": "2026-05-19T10:30:00Z",
  "traceId": "abc123-def456"
}
```

### 6.4 認證與授權設計

| 項目 | 設計 |
|------|------|
| 認證協定 | OAuth 2.0 + OpenID Connect |
| Token 類型 | JWT (RS256) |
| Access Token 效期 | 30 分鐘 |
| Refresh Token 效期 | 7 天 |
| Token 儲存 | HttpOnly Secure Cookie |
| 授權模式 | RBAC（Role-Based Access Control） |

---

## 7. 資安規範（Security Design）

### 7.1 安全架構

| 安全層級 | 防護措施 | 參照標準 |
|---------|---------|---------|
| 網路層 | WAF、DDoS 防護、網路區段隔離 | NIST SP 800-41 |
| 傳輸層 | TLS 1.3、憑證管理 | NIST SP 800-52 |
| 應用層 | 輸入驗證、CSRF/XSS 防護、API 限流 | OWASP ASVS v4.0.3 |
| 資料層 | 加密儲存、存取控制、資料遮罩 | NIST SP 800-111 |
| 認證層 | MFA、Token 管理、Session 控制 | NIST SP 800-63B |

### 7.2 威脅模型摘要

| 威脅 | STRIDE 類型 | 風險等級 | 緩解措施 |
|------|------------|---------|---------|
| SQL Injection | Tampering | 高 | Parameterized Query、ORM |
| XSS 攻擊 | Spoofing | 高 | 輸出編碼、CSP Header |
| 未授權存取 | Elevation of Privilege | 高 | RBAC、API Gateway 驗證 |
| 資料外洩 | Information Disclosure | 高 | 加密、存取日誌、DLP |

### 7.3 敏感資料處理

| 資料類型 | 分類 | 處理方式 |
|---------|------|---------|
| 密碼 | 極機密 | bcrypt 雜湊（cost factor ≥ 12） |
| 個資（身分證、電話） | 機密 | AES-256-GCM 加密儲存 |
| API Key / Secret | 極機密 | 保險箱服務（Vault） |
| 一般業務資料 | 內部 | 存取控制、稽核日誌 |

### 7.4 稽核日誌設計

| 日誌類型 | 記錄內容 | 保留期限 |
|---------|---------|---------|
| 認證日誌 | 登入/登出、驗證失敗 | 1 年 |
| 授權日誌 | 權限變更、存取拒絕 | 1 年 |
| 資料異動日誌 | CRUD 操作、異動前後值 | 依法規（3-7 年） |
| 系統日誌 | 錯誤、效能、健康檢查 | 90 天 |

---

## 8. 非功能性設計

### 8.1 效能設計

| 指標 | 目標值 | 設計策略 |
|------|--------|---------|
| API 回應時間 | P95 < 200ms | 快取、索引優化、非同步 |
| 吞吐量 | ≥ 1,000 TPS | 水平擴展、連線池 |
| 資料庫查詢 | P95 < 50ms | 查詢優化、讀寫分離 |

### 8.2 高可用設計

| 元件 | HA 策略 | SLA 目標 |
|------|---------|---------|
| 應用服務 | 多副本部署 + 負載平衡 | 99.99% |
| 資料庫 | 主從複製 + 自動故障轉移 | 99.99% |
| 快取 | Redis Sentinel / Cluster | 99.95% |
| 訊息佇列 | 多 Broker 叢集 | 99.99% |

### 8.3 可擴展性設計

| 擴展面向 | 策略 | 觸發條件 |
|---------|------|---------|
| 水平擴展 | Kubernetes HPA | CPU > 70% or QPS > 閾值 |
| 資料庫擴展 | 讀寫分離 → 分庫分表 | 單表 > 5,000 萬筆 |
| 快取擴展 | Redis Cluster 增加節點 | 記憶體 > 80% |

---

## 9. 整合設計（Integration Design）

### 9.1 外部系統整合

| 外部系統 | 整合方式 | 協定 | 資料格式 | 說明 |
|---------|---------|------|---------|------|
| SSO 服務 | 同步 API | OIDC | JSON | 身分驗證 |
| ERP 系統 | 非同步 MQ | AMQP | JSON | 訂單同步 |
| 金流服務 | 同步 API | REST | JSON | 付款處理 |
| 通知服務 | 非同步 MQ | Kafka | JSON | 訊息推播 |

### 9.2 整合序列圖

```
[使用 Mermaid Sequence Diagram 呈現關鍵整合流程]

範例：使用者登入流程

Client → API GW: POST /auth/login
API GW → Auth Svc: 驗證憑證
Auth Svc → User DB: 查詢使用者
User DB → Auth Svc: 回傳使用者資料
Auth Svc → SSO: 驗證 Token
SSO → Auth Svc: 驗證結果
Auth Svc → API GW: JWT Token
API GW → Client: 登入成功 + Token
```

---

## 10. 錯誤處理與容錯設計

### 10.1 錯誤碼規範

| 錯誤碼範圍 | 類別 | 範例 |
|-----------|------|------|
| 0000 | 成功 | 操作成功 |
| E1xxx | 認證/授權錯誤 | E1001：未認證 |
| E2xxx | 業務邏輯錯誤 | E2001：資料重複 |
| E3xxx | 資料驗證錯誤 | E3001：必填欄位缺失 |
| E4xxx | 外部服務錯誤 | E4001：第三方服務逾時 |
| E9xxx | 系統錯誤 | E9001：未預期錯誤 |

### 10.2 容錯模式

| 模式 | 適用場景 | 實作方式 |
|------|---------|---------|
| Circuit Breaker | 外部服務調用 | Resilience4j CircuitBreaker |
| Retry | 暫態故障 | 指數退避（Exponential Backoff） |
| Bulkhead | 資源隔離 | 執行緒池隔離 |
| Fallback | 服務降級 | 預設值 / 快取資料 |
| Timeout | 所有外部調用 | 連線 5s、讀取 10s |

---

## 11. 可觀測性設計（Observability）

### 11.1 監控指標

| 指標類型 | 指標名稱 | 告警閾值 |
|---------|---------|---------|
| RED 指標 | Request Rate | 異常波動 > 50% |
| RED 指標 | Error Rate | > 1% |
| RED 指標 | Duration (P95) | > 500ms |
| 系統指標 | CPU Usage | > 80% |
| 系統指標 | Memory Usage | > 85% |
| 業務指標 | 交易成功率 | < 99% |

### 11.2 日誌規範

| 日誌等級 | 使用情境 | 範例 |
|---------|---------|------|
| ERROR | 需要立即處理的錯誤 | 資料庫連線失敗 |
| WARN | 潛在問題，需關注 | 重試成功、接近限流 |
| INFO | 業務流程關鍵節點 | 使用者登入、訂單建立 |
| DEBUG | 開發除錯資訊 | 方法入參、SQL 語句 |

### 11.3 分散式追蹤

| 項目 | 設計 |
|------|------|
| 追蹤框架 | OpenTelemetry |
| Trace ID 傳遞 | HTTP Header（traceparent） |
| 取樣率 | 生產環境 10%、錯誤 100% |
| 視覺化 | Jaeger / Grafana Tempo |

---

## 12. 設計決策記錄（ADR）

### ADR-001：資料庫選型

| 項目 | 內容 |
|------|------|
| **狀態** | 已接受 |
| **日期** | YYYY-MM-DD |
| **決策者** | 架構師團隊 |
| **背景** | 系統需要 ACID 事務支援，同時需處理半結構化資料 |
| **決策** | 選用 PostgreSQL 16 作為主資料庫 |
| **替代方案** | MySQL 8.x、MongoDB 7.x |
| **理由** | 1. JSONB 支援半結構化資料<br/>2. 效能優於 MySQL<br/>3. 擴展生態成熟 |
| **影響** | 團隊需培訓 PostgreSQL 特有功能 |

---

## 範例：電商系統 SDD 摘要

### 架構選型
- **架構風格**：微服務架構
- **通訊方式**：同步 REST + 非同步 Kafka
- **服務網格**：Istio

### 核心服務
| 服務 | 技術棧 | 資料庫 |
|------|--------|--------|
| 使用者服務 | Spring Boot 3.4 | PostgreSQL |
| 訂單服務 | Spring Boot 3.4 | PostgreSQL + Redis |
| 商品服務 | Spring Boot 3.4 | PostgreSQL + Elasticsearch |
| 支付服務 | Spring Boot 3.4 | PostgreSQL |
| 通知服務 | Spring Boot 3.4 | Redis |

### 資安設計重點
- API Gateway 統一認證（JWT + OAuth 2.0）
- 敏感資料 AES-256-GCM 加密
- 全面稽核日誌，保留 3 年

---

> 📌 **填寫提醒**  
> 1. SDD 應由架構師主導撰寫，與開發團隊、DBA、資安團隊協同審查  
> 2. 架構圖建議使用 C4 Model 分層呈現（Context → Container → Component）  
> 3. 每個設計決策需記錄 ADR（Architecture Decision Record）  
> 4. 完成後需安排正式的設計審查（Design Review）會議
