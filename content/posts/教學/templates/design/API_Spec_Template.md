---
title: "API 規格文件範本（API Specification Template）"
date: 2026-05-18
draft: false
categories: ["教學"]
tags: ["設計開發", "範本", "API", "軟體工程", "OpenAPI"]
---

# API 規格文件範本（API Specification Document）

> **參照標準**：OpenAPI Specification 3.1（OAS 3.1）/ Linux Foundation 標準  
> **文件用途**：定義 RESTful API 的端點、請求/回應格式、認證機制與錯誤處理規範  
> **適用階段**：系統設計階段（Detail Design Phase）

---

## 📋 章節目錄

1. [文件資訊](#1-文件資訊)
2. [API 概述](#2-api-概述)
3. [認證與授權](#3-認證與授權)
4. [共用規範](#4-共用規範)
5. [端點定義](#5-端點定義)
6. [資料模型](#6-資料模型schemas)
7. [錯誤處理](#7-錯誤處理)
8. [版本策略](#8-版本策略)
9. [OpenAPI 規格檔](#9-openapi-規格檔)
10. [附錄](#10-附錄)

---

## 1. 文件資訊

### 📝 範本

| 項目 | 內容 |
|------|------|
| **文件編號** | API-{專案代碼}-{序號} |
| **API 名稱** | {系統名稱} API |
| **API 版本** | v{主版本} |
| **文件版本** | v{主版本}.{次版本} |
| **狀態** | 草稿 / 審核中 / 已發布 |
| **建立日期** | {YYYY-MM-DD} |
| **最後更新** | {YYYY-MM-DD} |
| **負責人** | {姓名/角色} |
| **Base URL** | `https://{domain}/api/v{version}` |

### 📖 使用說明

- API 版本與文件版本分開管理：API 版本影響端點路徑，文件版本追蹤文件修訂
- Base URL 需區分環境（DEV/SIT/UAT/PROD）
- 依據 OpenAPI 3.1 info 物件結構設計

### 💡 範例

| 項目 | 內容 |
|------|------|
| **文件編號** | API-HRM-001 |
| **API 名稱** | HRMS API |
| **API 版本** | v1 |
| **Base URL** | `https://api.company.com/hrms/v1` |

---

## 2. API 概述

### 📝 範本

#### 2.1 API 目的

{描述此 API 提供的服務範圍與主要功能}

#### 2.2 目標使用者

| 使用者類型 | 說明 | 權限範圍 |
|-----------|------|---------|
| {類型} | {說明} | {可存取的資源} |

#### 2.3 API 資源總覽

| 資源（Resource） | Base Path | 說明 | 支援操作 |
|----------------|-----------|------|---------|
| {資源名稱} | `/{resource}` | {描述} | GET, POST, PUT, DELETE |

### 📖 使用說明

- API 設計遵循 REST 架構風格，以資源（Resource）為中心
- 資源命名使用複數名詞（如 `/employees`，非 `/employee`）
- 使用者類型對應不同的 OAuth Scope 或角色

### 💡 範例

#### 2.3 API 資源總覽

| 資源 | Base Path | 說明 | 支援操作 |
|------|-----------|------|---------|
| Employees | `/employees` | 員工基本資料管理 | GET, POST, PUT, PATCH |
| Leaves | `/leaves` | 請假申請與管理 | GET, POST, PUT, DELETE |
| Payrolls | `/payrolls` | 薪資記錄查詢 | GET |
| Departments | `/departments` | 部門組織管理 | GET, POST, PUT |

---

## 3. 認證與授權

### 📝 範本

#### 3.1 認證機制

| 項目 | 規格 |
|------|------|
| 認證方式 | {OAuth 2.0 / API Key / Bearer Token} |
| Token 格式 | {JWT / Opaque} |
| Token 位置 | {Authorization Header / Cookie} |
| Token 有效期 | {時間} |
| 刷新機制 | {Refresh Token / Re-authenticate} |

#### 3.2 授權模型

| Scope / Role | 描述 | 可存取資源 |
|-------------|------|-----------|
| {scope} | {描述} | {資源清單} |

#### 3.3 請求範例

```http
GET /api/v1/employees HTTP/1.1
Host: api.company.com
Authorization: Bearer {access_token}
Content-Type: application/json
```

### 📖 使用說明

- 依據 OAuth 2.0 RFC 6749 與 OpenAPI 3.1 Security Scheme 規範
- Token 必須透過 HTTPS 傳輸，禁止在 URL Query Parameter 中傳遞
- API Key 適用於 Server-to-Server 場景，使用者互動場景建議 OAuth 2.0

### 💡 範例

#### 3.1 認證機制

| 項目 | 規格 |
|------|------|
| 認證方式 | OAuth 2.0 Authorization Code Flow（使用者）/ Client Credentials（系統） |
| Token 格式 | JWT（RS256 簽章） |
| Token 位置 | `Authorization: Bearer {token}` |
| Token 有效期 | Access Token: 15 分鐘 / Refresh Token: 7 天 |

#### 3.2 授權模型

| Scope | 描述 | 可存取資源 |
|-------|------|-----------|
| `employee:read` | 讀取員工資料 | GET /employees |
| `employee:write` | 修改員工資料 | POST/PUT /employees |
| `leave:manage` | 管理假勤（含審核） | ALL /leaves |
| `payroll:read` | 查詢薪資 | GET /payrolls |

---

## 4. 共用規範

### 📝 範本

#### 4.1 HTTP 方法語義

| 方法 | 語義 | 冪等性 | 安全性 |
|------|------|--------|--------|
| GET | 讀取資源 | 是 | 是 |
| POST | 建立資源 | 否 | 否 |
| PUT | 完整更新資源 | 是 | 否 |
| PATCH | 部分更新資源 | 否 | 否 |
| DELETE | 刪除資源 | 是 | 否 |

#### 4.2 分頁規範

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalPages": 5,
    "totalCount": 98
  }
}
```

**分頁參數：**

| 參數 | 型別 | 預設值 | 說明 |
|------|------|--------|------|
| `page` | integer | 1 | 頁碼（從 1 開始） |
| `pageSize` | integer | 20 | 每頁筆數（最大 100） |
| `sort` | string | - | 排序欄位（如 `createdAt:desc`） |

#### 4.3 日期時間格式

| 格式 | 標準 | 範例 |
|------|------|------|
| 日期時間 | ISO 8601 / RFC 3339 | `2026-05-18T10:30:00+08:00` |
| 純日期 | ISO 8601 | `2026-05-18` |
| 時區 | UTC 偏移量 | `+08:00` |

#### 4.4 共用 HTTP Headers

| Header | 用途 | 必填 | 範例 |
|--------|------|------|------|
| `Content-Type` | 請求/回應格式 | 是 | `application/json` |
| `Accept` | 期望回應格式 | 否 | `application/json` |
| `X-Request-Id` | 請求追蹤 ID | 是 | `uuid-v4` |
| `X-Correlation-Id` | 跨服務追蹤 ID | 否 | `uuid-v4` |

### 📖 使用說明

- 分頁設計避免一次回傳過多資料，保護伺服器效能
- 日期時間一律使用 ISO 8601 格式，避免時區混亂
- `X-Request-Id` 用於日誌追蹤與問題排查，建議每個請求必帶
- 所有字串使用 UTF-8 編碼

### 💡 範例

請求假勤清單（含分頁與排序）：

```http
GET /api/v1/leaves?page=2&pageSize=10&sort=startDate:desc HTTP/1.1
Host: api.company.com
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
X-Request-Id: 550e8400-e29b-41d4-a716-446655440000
Accept: application/json
```

---

## 5. 端點定義

### 📝 範本

#### 5.1 {資源名稱}

##### `{HTTP Method} /{path}`

**描述**：{端點功能描述}

**路徑參數（Path Parameters）：**

| 參數 | 型別 | 必填 | 說明 |
|------|------|------|------|
| `{param}` | {type} | 是/否 | {描述} |

**查詢參數（Query Parameters）：**

| 參數 | 型別 | 必填 | 預設值 | 說明 |
|------|------|------|--------|------|
| `{param}` | {type} | 是/否 | {default} | {描述} |

**請求 Body（Request Body）：**

```json
{
  "field1": "{type} - {描述}",
  "field2": "{type} - {描述}"
}
```

**回應（Response）：**

| HTTP Status | 說明 | 回應 Body |
|-------------|------|-----------|
| 200 OK | 成功 | {回應結構} |
| 201 Created | 建立成功 | {回應結構} |
| 400 Bad Request | 參數錯誤 | Error Object |
| 401 Unauthorized | 未認證 | Error Object |
| 403 Forbidden | 無權限 | Error Object |
| 404 Not Found | 資源不存在 | Error Object |

**回應 Body 範例：**

```json
{
  "data": { ... },
  "meta": {
    "requestId": "uuid",
    "timestamp": "ISO-8601"
  }
}
```

### 📖 使用說明

- 每個端點需定義：路徑、方法、參數、請求體、回應碼、回應體
- 路徑參數使用 `{id}` 格式，代表資源唯一識別碼
- 回應結構統一使用 `{ data, meta, errors }` 信封格式
- 列出所有可能的 HTTP Status Code，包含錯誤場景

### 💡 範例

#### 5.1 假勤管理（Leaves）

##### `POST /leaves`

**描述**：員工提交請假申請

**請求 Body：**

```json
{
  "leaveType": "annual",
  "startDate": "2026-06-01",
  "endDate": "2026-06-03",
  "reason": "家庭旅遊",
  "delegateId": "E20260015"
}
```

| 欄位 | 型別 | 必填 | 說明 |
|------|------|------|------|
| `leaveType` | string | 是 | 假別代碼（annual/sick/personal/official） |
| `startDate` | string(date) | 是 | 請假起始日 |
| `endDate` | string(date) | 是 | 請假結束日 |
| `reason` | string | 是 | 請假事由（最長 500 字） |
| `delegateId` | string | 否 | 職務代理人員工編號 |

**回應：**

```json
// 201 Created
{
  "data": {
    "id": "LV-20260601-001",
    "employeeId": "E20260001",
    "leaveType": "annual",
    "startDate": "2026-06-01",
    "endDate": "2026-06-03",
    "days": 3,
    "status": "pending",
    "createdAt": "2026-05-18T10:30:00+08:00"
  },
  "meta": {
    "requestId": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-05-18T10:30:00+08:00"
  }
}
```

##### `GET /leaves/{id}`

**描述**：查詢單筆請假紀錄

**路徑參數：**

| 參數 | 型別 | 必填 | 說明 |
|------|------|------|------|
| `id` | string | 是 | 請假單編號 |

**回應：**

| HTTP Status | 說明 |
|-------------|------|
| 200 OK | 回傳請假紀錄 |
| 404 Not Found | 請假單不存在 |

---

## 6. 資料模型（Schemas）

### 📝 範本

#### 6.1 {Schema 名稱}

| 欄位 | 型別 | 必填 | 說明 | 驗證規則 |
|------|------|------|------|---------|
| `{field}` | {type} | 是/否 | {描述} | {min/max/pattern/enum} |

#### 6.2 列舉值（Enums）

| Enum 名稱 | 值 | 說明 |
|-----------|------|------|
| {EnumName} | `value1` | {描述} |
| | `value2` | {描述} |

### 📖 使用說明

- Schema 定義可重複使用的資料結構（對應 OpenAPI components/schemas）
- 每個欄位需定義型別、必填性、驗證規則
- 列舉值需完整列出所有合法值

### 💡 範例

#### 6.1 LeaveRequest Schema

| 欄位 | 型別 | 必填 | 說明 | 驗證規則 |
|------|------|------|------|---------|
| `leaveType` | string | 是 | 假別 | enum: annual, sick, personal, official |
| `startDate` | string(date) | 是 | 起始日 | format: date, ≥ today |
| `endDate` | string(date) | 是 | 結束日 | format: date, ≥ startDate |
| `reason` | string | 是 | 事由 | minLength: 1, maxLength: 500 |
| `delegateId` | string | 否 | 代理人 | pattern: `^E\d{8}$` |

#### 6.2 LeaveStatus Enum

| 值 | 說明 |
|------|------|
| `pending` | 待審核 |
| `approved` | 已核准 |
| `rejected` | 已駁回 |
| `cancelled` | 已取消 |

---

## 7. 錯誤處理

### 📝 範本

#### 7.1 錯誤回應格式

```json
{
  "errors": [
    {
      "code": "{ERROR_CODE}",
      "message": "{人類可讀的錯誤訊息}",
      "field": "{引發錯誤的欄位（選填）}",
      "detail": "{詳細說明（選填）}"
    }
  ],
  "meta": {
    "requestId": "{uuid}",
    "timestamp": "{ISO-8601}"
  }
}
```

#### 7.2 錯誤代碼清單

| HTTP Status | Error Code | 說明 | 處理建議 |
|-------------|-----------|------|---------|
| 400 | `VALIDATION_ERROR` | 請求參數驗證失敗 | 修正請求參數後重試 |
| 400 | `INVALID_DATE_RANGE` | 日期範圍無效 | 確認 endDate ≥ startDate |
| 401 | `TOKEN_EXPIRED` | Token 已過期 | 使用 Refresh Token 取得新 Token |
| 401 | `INVALID_TOKEN` | Token 無效 | 重新登入取得 Token |
| 403 | `INSUFFICIENT_SCOPE` | 權限不足 | 確認帳號具有對應 Scope |
| 404 | `RESOURCE_NOT_FOUND` | 資源不存在 | 確認 ID 是否正確 |
| 409 | `CONFLICT` | 資源衝突 | 取得最新版本後重試 |
| 422 | `BUSINESS_RULE_VIOLATION` | 違反業務規則 | 參考 detail 欄位說明 |
| 429 | `RATE_LIMIT_EXCEEDED` | 超過請求頻率限制 | 等待後重試，參考 Retry-After header |
| 500 | `INTERNAL_ERROR` | 伺服器內部錯誤 | 聯繫技術支援 |

#### 7.3 Rate Limiting

| 項目 | 規格 |
|------|------|
| 限制方式 | {Per User / Per API Key / Per IP} |
| 限制量 | {N} requests / {時間單位} |
| 回應 Header | `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` |

### 📖 使用說明

- 錯誤格式遵循 RFC 7807 Problem Details 精神，結構統一
- Error Code 使用大寫蛇形命名（UPPER_SNAKE_CASE）
- 400 系列為客戶端錯誤，500 系列為伺服器錯誤
- 錯誤訊息不應洩漏系統內部資訊（如 Stack Trace、DB 結構）

### 💡 範例

```json
// 422 Unprocessable Entity
{
  "errors": [
    {
      "code": "BUSINESS_RULE_VIOLATION",
      "message": "特休假額不足",
      "field": "leaveType",
      "detail": "申請 3 天特休假，但剩餘假額僅 2 天"
    }
  ],
  "meta": {
    "requestId": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-05-18T10:30:00+08:00"
  }
}
```

---

## 8. 版本策略

### 📝 範本

#### 8.1 版本管理規則

| 項目 | 策略 |
|------|------|
| 版本格式 | {URL Path / Header / Query Parameter} |
| 版本命名 | v{major}（如 v1, v2） |
| 向後相容 | {相容性保證描述} |
| 棄用通知 | {提前 N 個月通知} |
| 並行支援 | {同時支援 N 個版本} |

#### 8.2 Breaking Change 定義

以下變更視為 Breaking Change（需升版）：
- {Breaking Change 類型 1}
- {Breaking Change 類型 2}

以下變更為 Non-Breaking（不需升版）：
- {Non-Breaking Change 類型 1}
- {Non-Breaking Change 類型 2}

### 📖 使用說明

- URL Path 版本管理（如 `/api/v1/`）最直觀，業界最常見
- Breaking Change：移除欄位、更改欄位型別、更改必填性、更改行為
- Non-Breaking Change：新增選填欄位、新增端點、新增回應欄位

### 💡 範例

#### 8.1 版本管理規則

| 項目 | 策略 |
|------|------|
| 版本格式 | URL Path（`/api/v1/...`） |
| 版本命名 | v1, v2（Major 版本） |
| 向後相容 | 同一 Major 版本內保證向後相容 |
| 棄用通知 | 新版本發布後，舊版本至少維護 12 個月 |
| 並行支援 | 最多同時維護 2 個 Major 版本 |

---

## 9. OpenAPI 規格檔

### 📝 範本

以下為本 API 的 OpenAPI 3.1 規格定義：

```yaml
openapi: 3.1.0
info:
  title: "{API 名稱}"
  description: "{API 描述}"
  version: "{版本}"
  contact:
    name: "{團隊名稱}"
    email: "{聯絡信箱}"

servers:
  - url: https://{domain}/api/v1
    description: "Production"
  - url: https://dev-{domain}/api/v1
    description: "Development"

security:
  - bearerAuth: []

paths:
  /{resource}:
    get:
      summary: "{描述}"
      operationId: "{operationId}"
      tags:
        - "{Tag}"
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: pageSize
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        '200':
          description: "Success"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/{ResponseSchema}'
    post:
      summary: "{描述}"
      operationId: "{operationId}"
      tags:
        - "{Tag}"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/{RequestSchema}'
      responses:
        '201':
          description: "Created"
        '400':
          description: "Bad Request"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
        meta:
          $ref: '#/components/schemas/Meta'

    Error:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
        field:
          type: string
        detail:
          type: string
      required: [code, message]

    Meta:
      type: object
      properties:
        requestId:
          type: string
          format: uuid
        timestamp:
          type: string
          format: date-time
```

### 📖 使用說明

- OpenAPI 3.1 規格檔可直接用於自動生成 API 文件（如 Swagger UI、Redoc）
- 建議將 yaml 檔案納入版本控制，與程式碼同步更新
- 可搭配 CI/CD Pipeline 自動驗證 API 實作是否符合規格（Contract Testing）
- `$ref` 用於引用可重複使用的 Schema，避免重複定義

### 💡 範例

```yaml
openapi: 3.1.0
info:
  title: "HRMS API"
  description: "人力資源管理系統 API"
  version: "1.0.0"
  contact:
    name: "HRMS Development Team"
    email: "hrms-dev@company.com"

servers:
  - url: https://api.company.com/hrms/v1
    description: "Production"
  - url: https://dev-api.company.com/hrms/v1
    description: "Development"

paths:
  /leaves:
    post:
      summary: "提交請假申請"
      operationId: "createLeave"
      tags:
        - "Leaves"
      security:
        - bearerAuth: [leave:manage]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LeaveRequest'
      responses:
        '201':
          description: "請假申請建立成功"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LeaveResponse'
        '422':
          description: "業務規則驗證失敗"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
```

---

## 10. 附錄

### 📝 範本

#### 10.1 環境 URL 對照

| 環境 | Base URL | 說明 |
|------|----------|------|
| DEV | `https://dev-api.{domain}/api/v1` | 開發環境 |
| SIT | `https://sit-api.{domain}/api/v1` | 整合測試 |
| UAT | `https://uat-api.{domain}/api/v1` | 使用者驗收 |
| PROD | `https://api.{domain}/api/v1` | 正式環境 |

#### 10.2 變更紀錄

| 日期 | 版本 | 變更內容 | 類型 |
|------|------|---------|------|
| {日期} | {版本} | {變更描述} | Breaking / Non-Breaking |

#### 10.3 相關工具

| 工具 | 用途 | 連結 |
|------|------|------|
| Swagger UI | API 互動式文件 | {URL} |
| Postman Collection | API 測試集合 | {URL} |

### 📖 使用說明

- 環境 URL 需與 DevOps 團隊確認，確保 DNS 與 SSL 憑證就緒
- 變更紀錄標記 Breaking / Non-Breaking 協助使用者評估升級影響
- Postman Collection 可匯出分享給前端或第三方開發者

### 💡 範例

#### 10.2 變更紀錄

| 日期 | 版本 | 變更內容 | 類型 |
|------|------|---------|------|
| 2026-05-18 | v1.0 | 初版發布：Employees, Leaves, Payrolls API | - |
| 2026-06-01 | v1.1 | 新增 `delegateId` 欄位於 LeaveRequest | Non-Breaking |
| 2026-07-15 | v1.2 | 新增 `/leaves/{id}/approve` 端點 | Non-Breaking |

---

> 📌 **範本使用注意事項**
> 1. 本範本依據 OpenAPI Specification 3.1 標準編製
> 2. 建議同時維護本文件（人類可讀）與 OpenAPI yaml 檔案（機器可讀）
> 3. API 設計建議遵循：REST 最佳實踐、一致命名、最小暴露原則
> 4. 所有 API 端點需通過 Security Review 後方可發布
> 5. 建議搭配 Contract Testing 確保 API 實作與規格一致
