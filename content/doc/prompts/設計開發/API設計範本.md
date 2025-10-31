# API 設計範本

## Prompt 目標

指導 AI 進行RESTful API設計，產生完整的API規格文檔和設計指南。

## 角色設定

你是一位資深API架構師，具備豐富的API設計經驗，熟悉RESTful設計原則、OpenAPI規範和API最佳實務。

## 任務描述

請協助我完成 {專案名稱} 的API設計工作。

### API 背景資訊

- **專案名稱**: {填入專案名稱}
- **API 類型**: {填入API類型，如：RESTful、GraphQL、gRPC}
- **主要功能領域**: {填入主要業務領域}
- **預期使用者**: {填入API使用者類型，如：前端應用、第三方系統、移動應用}
- **安全等級**: {填入安全要求等級}

### API 設計要求

請按照以下結構進行API設計：

#### 1. API 概覽設計
- API 目標和範圍定義
- 資源模型設計
- URL 結構規劃
- HTTP 方法對應

#### 2. 資料模型設計
- 實體關係模型
- JSON Schema 定義
- 資料驗證規則
- 錯誤回應格式

#### 3. 端點詳細設計
- CRUD 操作設計
- 查詢和篩選設計
- 分頁機制設計
- 排序機制設計

#### 4. 安全性設計
- 身份驗證機制
- 授權控制設計
- API 金鑰管理
- 速率限制設計

#### 5. 版本控制策略
- 版本控制方法
- 向後相容性規劃
- 廢棄策略設計
- 遷移指南規劃

#### 6. 文檔和測試
- OpenAPI 規格撰寫
- 使用範例提供
- 測試案例設計
- 錯誤處理指南

## 輸出格式

```markdown
# {專案名稱} API 設計規格

## 1. API 概覽

### 1.1 API 目標
**主要目標:** [API 的主要用途和目標]
**次要目標:** [輔助功能和延伸應用]
**成功標準:** [API 品質和使用量指標]

### 1.2 API 設計原則
- **RESTful 設計**: 遵循 REST 架構風格
- **一致性**: 統一的命名和回應格式
- **可預測性**: 直觀的 URL 結構和行為
- **可擴展性**: 支援未來功能擴展
- **安全性**: 內建安全機制

### 1.3 基礎 URL 結構
**Base URL:** `https://api.{domain}.com/v1`
**URL 模式:** `/{resource}/{id}/{sub-resource}`

### 1.4 HTTP 方法對應
| HTTP 方法 | 用途 | 冪等性 | 安全性 |
|-----------|------|--------|--------|
| GET | 查詢資源 | 是 | 是 |
| POST | 建立資源 | 否 | 否 |
| PUT | 更新/替換資源 | 是 | 否 |
| PATCH | 部分更新資源 | 否 | 否 |
| DELETE | 刪除資源 | 是 | 否 |

## 2. 資料模型設計

### 2.1 核心實體模型

#### 實體: User (使用者)
```json
{
  "id": "string (UUID)",
  "username": "string (3-50字元)",
  "email": "string (email格式)",
  "firstName": "string (1-50字元)",
  "lastName": "string (1-50字元)",
  "role": "string (enum: admin, user, guest)",
  "status": "string (enum: active, inactive, suspended)",
  "createdAt": "string (ISO 8601 datetime)",
  "updatedAt": "string (ISO 8601 datetime)"
}
```

#### 實體: Product (產品)
```json
{
  "id": "string (UUID)",
  "name": "string (1-200字元)",
  "description": "string (可選，最多1000字元)",
  "price": "number (正數，最多2位小數)",
  "category": "string",
  "sku": "string (產品編號)",
  "inventory": {
    "quantity": "integer (非負整數)",
    "reserved": "integer (非負整數)"
  },
  "images": ["string (URL陣列)"],
  "attributes": {
    "color": "string",
    "size": "string",
    "weight": "number"
  },
  "isActive": "boolean",
  "createdAt": "string (ISO 8601 datetime)",
  "updatedAt": "string (ISO 8601 datetime)"
}
```

### 2.2 標準回應格式

#### 成功回應格式
```json
{
  "success": true,
  "data": {
    // 實際資料內容
  },
  "meta": {
    "timestamp": "ISO 8601 datetime",
    "requestId": "UUID",
    "pagination": {  // 僅分頁查詢時包含
      "page": 1,
      "limit": 20,
      "total": 100,
      "totalPages": 5
    }
  }
}
```

#### 錯誤回應格式
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "錯誤訊息",
    "details": "詳細錯誤說明",
    "field": "發生錯誤的欄位 (驗證錯誤時)"
  },
  "meta": {
    "timestamp": "ISO 8601 datetime",
    "requestId": "UUID"
  }
}
```

## 3. API 端點設計

### 3.1 使用者管理 API

#### 取得使用者清單
**端點:** `GET /users`
**描述:** 取得使用者清單，支援分頁和篩選

**查詢參數:**
- `page` (integer, optional): 頁碼，預設為 1
- `limit` (integer, optional): 每頁筆數，預設為 20，最大 100
- `role` (string, optional): 角色篩選
- `status` (string, optional): 狀態篩選
- `search` (string, optional): 搜尋使用者名稱或信箱

**回應範例:**
```json
{
  "success": true,
  "data": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "username": "john_doe",
      "email": "john@example.com",
      "firstName": "John",
      "lastName": "Doe",
      "role": "user",
      "status": "active",
      "createdAt": "2024-01-01T00:00:00Z",
      "updatedAt": "2024-01-01T00:00:00Z"
    }
  ],
  "meta": {
    "timestamp": "2024-01-01T12:00:00Z",
    "requestId": "req_123456",
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 1,
      "totalPages": 1
    }
  }
}
```

#### 建立新使用者
**端點:** `POST /users`
**描述:** 建立新的使用者帳號

**請求主體:**
```json
{
  "username": "new_user",
  "email": "user@example.com",
  "firstName": "New",
  "lastName": "User",
  "password": "securePassword123",
  "role": "user"
}
```

**回應:**
- **201 Created**: 使用者建立成功
- **400 Bad Request**: 請求資料驗證失敗
- **409 Conflict**: 使用者名稱或信箱已存在

#### 取得特定使用者
**端點:** `GET /users/{userId}`
**描述:** 根據 ID 取得特定使用者資訊

**路徑參數:**
- `userId` (string, required): 使用者 UUID

**回應:**
- **200 OK**: 成功取得使用者資訊
- **404 Not Found**: 使用者不存在

#### 更新使用者
**端點:** `PUT /users/{userId}`
**描述:** 完整更新使用者資訊

**端點:** `PATCH /users/{userId}`
**描述:** 部分更新使用者資訊

#### 刪除使用者
**端點:** `DELETE /users/{userId}`
**描述:** 刪除特定使用者

**回應:**
- **204 No Content**: 成功刪除
- **404 Not Found**: 使用者不存在

### 3.2 產品管理 API

#### 取得產品清單
**端點:** `GET /products`
**描述:** 取得產品清單，支援多種篩選和排序

**查詢參數:**
- `page` (integer): 頁碼
- `limit` (integer): 每頁筆數
- `category` (string): 產品類別篩選
- `minPrice` (number): 最低價格
- `maxPrice` (number): 最高價格
- `inStock` (boolean): 是否有庫存
- `sortBy` (string): 排序欄位 (name, price, createdAt)
- `sortOrder` (string): 排序順序 (asc, desc)
- `search` (string): 搜尋產品名稱或描述

[其他產品相關端點...]

## 4. 安全性設計

### 4.1 身份驗證
**驗證方式:** JWT (JSON Web Token)
**Token 位置:** Authorization Header
**格式:** `Authorization: Bearer <token>`

#### 登入端點
**端點:** `POST /auth/login`
**請求:**
```json
{
  "username": "user@example.com",
  "password": "userPassword"
}
```

**回應:**
```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600,
    "tokenType": "Bearer",
    "user": {
      "id": "user-id",
      "username": "user@example.com",
      "role": "user"
    }
  }
}
```

### 4.2 授權控制
**授權模型:** RBAC (Role-Based Access Control)

| 端點 | Admin | User | Guest |
|------|-------|------|-------|
| GET /users | ✓ | ✗ | ✗ |
| POST /users | ✓ | ✗ | ✗ |
| GET /users/{id} | ✓ | ✓ (自己) | ✗ |
| GET /products | ✓ | ✓ | ✓ |
| POST /products | ✓ | ✗ | ✗ |

### 4.3 速率限制
- **一般使用者**: 100 請求/分鐘
- **進階使用者**: 1000 請求/分鐘
- **管理員**: 無限制

**限制回應標頭:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640995200
```

## 5. 版本控制

### 5.1 版本控制策略
**版本控制方法:** URL 路徑版本控制
**格式:** `/v{major}/...`
**範例:** `/v1/users`, `/v2/users`

### 5.2 版本相容性政策
- **主版本 (Major)**: 破壞性變更
- **次版本 (Minor)**: 新增功能，向後相容
- **修補版本 (Patch)**: 錯誤修正

### 5.3 版本生命週期
- **目前版本**: 完整支援
- **前一版本**: 維護支援 (12個月)
- **舊版本**: 僅安全性修正 (6個月)

## 6. 錯誤處理

### 6.1 HTTP 狀態碼使用
| 狀態碼 | 說明 | 使用時機 |
|--------|------|----------|
| 200 | OK | 成功取得資源 |
| 201 | Created | 成功建立資源 |
| 204 | No Content | 成功刪除或更新 |
| 400 | Bad Request | 請求格式錯誤 |
| 401 | Unauthorized | 未驗證身份 |
| 403 | Forbidden | 權限不足 |
| 404 | Not Found | 資源不存在 |
| 409 | Conflict | 資源衝突 |
| 422 | Unprocessable Entity | 驗證失敗 |
| 429 | Too Many Requests | 超過速率限制 |
| 500 | Internal Server Error | 伺服器錯誤 |

### 6.2 錯誤碼定義
| 錯誤碼 | 說明 | HTTP狀態 |
|--------|------|----------|
| VALIDATION_ERROR | 資料驗證失敗 | 422 |
| RESOURCE_NOT_FOUND | 資源不存在 | 404 |
| DUPLICATE_RESOURCE | 資源重複 | 409 |
| INSUFFICIENT_PERMISSIONS | 權限不足 | 403 |
| RATE_LIMIT_EXCEEDED | 超過速率限制 | 429 |

## 7. 測試策略

### 7.1 測試類型
- **合約測試**: 驗證 API 符合 OpenAPI 規格
- **整合測試**: 驗證端對端功能
- **效能測試**: 驗證回應時間和吞吐量
- **安全測試**: 驗證授權和輸入驗證

### 7.2 測試資料
提供標準測試資料集，包含：
- 有效和無效的請求範例
- 邊界值測試案例
- 錯誤情境測試案例

## 8. 監控和分析

### 8.1 關鍵指標
- **可用性**: 99.9% uptime
- **回應時間**: 95%請求 < 200ms
- **錯誤率**: < 0.1%
- **吞吐量**: > 1000 RPS

### 8.2 日誌記錄
記錄內容包含：
- 請求/回應日誌
- 錯誤和例外日誌
- 效能指標日誌
- 安全事件日誌
```

## API 設計最佳實務

### Richardson 成熟度模型
- **Level 0**: HTTP 作為傳輸機制
- **Level 1**: 資源導向設計
- **Level 2**: HTTP 動詞和狀態碼
- **Level 3**: 超媒體控制 (HATEOAS)

### 命名慣例
- **資源名稱**: 使用複數名詞 (`/users`, `/products`)
- **URL 結構**: 小寫字母，使用連字號分隔 (`/user-profiles`)
- **查詢參數**: 駝峰式命名 (`sortBy`, `pageSize`)
- **JSON 欄位**: 駝峰式命名 (`firstName`, `createdAt`)

## 品質檢查清單

- [ ] API 端點設計符合 RESTful 原則
- [ ] 資料模型結構清楚完整
- [ ] 錯誤處理機制完善
- [ ] 安全性機制適當
- [ ] 版本控制策略明確
- [ ] 文檔描述詳細準確
- [ ] 測試案例覆蓋全面
- [ ] 效能要求可達成

## 使用範例

### 範例：取得使用者清單 (含篩選)
```bash
curl -X GET "https://api.example.com/v1/users?page=1&limit=10&role=admin&status=active" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
     -H "Content-Type: application/json"
```

### 範例：建立新產品
```bash
curl -X POST "https://api.example.com/v1/products" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
     -H "Content-Type: application/json" \
     -d '{
       "name": "新產品",
       "description": "產品描述",
       "price": 99.99,
       "category": "electronics",
       "sku": "PROD-001"
     }'
```

## 注意事項

1. 遵循 OpenAPI 3.0 規範撰寫文檔
2. 考慮 API 的演進和向後相容性
3. 實作適當的快取機制
4. 提供清楚的錯誤訊息
5. 設計合理的預設值和限制
6. 考慮國際化和本地化需求
