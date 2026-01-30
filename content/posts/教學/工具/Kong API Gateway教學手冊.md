+++
date = '2026-01-30T19:39:19+08:00'
draft = false
title = 'Kong API Gateway教學手冊'

tags = ['教學', '工具', 'Kong','APIM']
categories = ['教學']
+++

# Kong API Gateway教學手冊

> **版本**：1.0  
> **最後更新**：2026 年 1 月  
> **適用對象**：後端工程師、系統架構師、DevOps 工程師  
> **定位**：企業內部標準教材 
> **文件維護**：內部技術團隊
> **最後更新**: 2026年1月29日  
> **適用於**: Kong 3.9.x（2026 年最新穩定版）
> **Created by**: Eric Cheng


## 目錄

1. [Kong API Gateway 簡介](#1-kong-api-gateway-簡介)
   - [1.1 Kong 是什麼？解決什麼問題？](#11-kong-是什麼解決什麼問題)
   - [1.2 為什麼需要 API Gateway？](#12-為什麼需要-api-gateway)
   - [1.3 Kong 在微服務架構中的角色](#13-kong-在微服務架構中的角色)
   - [1.4 Kong OSS / Enterprise 差異簡介](#14-kong-oss--enterprise-差異簡介)
2. [系統架構設計](#2-系統架構設計)
   - [2.1 Kong API Gateway 整體架構圖](#21-kong-api-gateway-整體架構圖)
   - [2.2 核心元件說明](#22-核心元件說明)
   - [2.3 與後端微服務、LB、Auth Server 的關係](#23-與後端微服務lbauth-server-的關係)
   - [2.4 典型企業架構範例](#24-典型企業架構範例)
3. [安裝與部署](#3-安裝與部署)
   - [3.1 安裝模式說明](#31-安裝模式說明)
   - [3.2 常見部署方式](#32-常見部署方式)
   - [3.3 安裝後檢查方式](#33-安裝後檢查方式)
4. [基本設定與核心概念](#4-基本設定與核心概念)
   - [4.1 Service / Route / Upstream / Target 說明](#41-service--route--upstream--target-說明)
   - [4.2 Consumer 概念](#42-consumer-概念)
   - [4.3 Plugin 架構與執行流程](#43-plugin-架構與執行流程)
   - [4.4 宣告式設定（Declarative Config）](#44-宣告式設定declarative-config)
   - [4.5 Admin API 使用方式概覽](#45-admin-api-使用方式概覽)
5. [Kong API Gateway 實際使用教學](#5-kong-api-gateway-實際使用教學)
   - [5.1 建立第一個 API（Service + Route）](#51-建立第一個-apiservice--route)
   - [5.2 API 路由策略](#52-api-路由策略)
   - [5.3 Load Balancing 與 Health Check](#53-load-balancing-與-health-check)
   - [5.4 完整請求流程範例](#54-完整請求流程範例)
6. [常用 Plugins 實務說明](#6-常用-plugins-實務說明)
   - [6.1 Rate Limiting（限流）](#61-rate-limiting限流)
   - [6.2 Key Authentication](#62-key-authentication)
   - [6.3 JWT Authentication](#63-jwt-authentication)
   - [6.4 OAuth 2.0（概念）](#64-oauth-20概念)
   - [6.5 ACL（存取控制清單）](#65-acl存取控制清單)
   - [6.6 CORS](#66-cors)
   - [6.7 Request / Response Transformer](#67-request--response-transformer)
   - [6.8 Prometheus Plugin](#68-prometheus-plugin)
   - [6.9 Logging Plugins](#69-logging-plugins)
7. [應用系統如何串接 Kong](#7-應用系統如何串接-kong)
   - [7.1 後端微服務如何被 Kong 管理](#71-後端微服務如何被-kong-管理)
   - [7.2 前端 / App 如何呼叫 Kong API](#72-前端--app-如何呼叫-kong-api)
   - [7.3 與 OAuth / SSO / IAM 系統整合](#73-與-oauth--sso--iam-系統整合)
8. [監控、日誌與可觀測性](#8-監控日誌與可觀測性)
   - [8.1 Kong Metrics 說明](#81-kong-metrics-說明)
   - [8.2 與 Prometheus / Grafana 整合](#82-與-prometheus--grafana-整合)
   - [8.3 Log 收集（ELK / OpenSearch）](#83-log-收集elk--opensearch)
   - [8.4 Trace（OpenTelemetry 整合）](#84-traceopentelemetry-整合)
9. [系統維護與營運](#9-系統維護與營運)
   - [9.1 Kong 設定管理建議](#91-kong-設定管理建議)
   - [9.2 Plugin 管理策略](#92-plugin-管理策略)
   - [9.3 多環境建議](#93-多環境建議)
   - [9.4 效能與容量規劃](#94-效能與容量規劃)
   - [9.5 常見營運問題與排查](#95-常見營運問題與排查)
10. [系統升級與版本管理](#10-系統升級與版本管理)
    - [10.1 Kong 升級注意事項](#101-kong-升級注意事項)
    - [10.2 Plugin 相容性風險](#102-plugin-相容性風險)
    - [10.3 升級前檢查清單](#103-升級前檢查清單)
    - [10.4 升級流程（滾動升級）](#104-升級流程滾動升級)
11. [Best Practices 與常見地雷](#11-best-practices-與常見地雷)
    - [11.1 API 設計與 Gateway 設計分工](#111-api-設計與-gateway-設計分工)
    - [11.2 不建議在 Kong 做的事情](#112-不建議在-kong-做的事情)
    - [11.3 Plugin 使用過度的風險](#113-plugin-使用過度的風險)
    - [11.4 安全性與效能常見錯誤](#114-安全性與效能常見錯誤)
    - [11.5 設定範例：生產環境最佳實踐](#115-設定範例生產環境最佳實踐)
12. [總結與學習路線建議](#12-總結與學習路線建議)
    - [12.1 適合新手的學習順序](#121-適合新手的學習順序)
    - [12.2 團隊導入 Kong 的成熟度成長路線](#122-團隊導入-kong-的成熟度成長路線)
    - [12.3 推薦學習資源](#123-推薦學習資源)
13. [檢查清單（Checklist）](#13-檢查清單checklist)
    - [🚀 新服務上線檢查清單](#-新服務上線檢查清單)
    - [🔧 日常維運檢查清單](#-日常維運檢查清單)
    - [📋 升級前檢查清單](#-升級前檢查清單)
    - [🔒 安全性檢查清單](#-安全性檢查清單)
14. [附錄](#14-附錄)
    - [A. 常用指令速查表](#a-常用指令速查表)
    - [B. 環境變數參考](#b-環境變數參考)

---

## 1. Kong API Gateway 簡介

### 1.1 Kong 是什麼？解決什麼問題？

**Kong** 是一個開源、高效能、可擴展的 **API Gateway（API 閘道）**，建構於 **Nginx** 與 **OpenResty（Lua）** 之上。它作為 API 的統一入口，處理所有進入系統的 API 請求。

#### Kong 主要解決的問題

| 問題類型 | 傳統做法的痛點 | Kong 的解決方案 |
|---------|--------------|----------------|
| **API 入口分散** | 每個微服務獨立暴露端點，難以管理 | 統一入口，集中管理所有 API |
| **重複實作橫切關注點** | 每個服務都要實作認證、限流、日誌 | 透過 Plugin 機制統一處理 |
| **流量控管困難** | 無法有效控制 API 呼叫頻率 | 內建 Rate Limiting、熔斷機制 |
| **缺乏可觀測性** | 難以追蹤 API 呼叫狀況 | 整合 Prometheus、OpenTelemetry |
| **安全性分散管理** | 各服務自行處理認證授權 | 集中式安全策略管理 |

### 1.2 為什麼需要 API Gateway？

在微服務架構中，API Gateway 扮演「前門警衛」的角色：

```mermaid
graph LR
    subgraph "外部世界"
        Client[客戶端<br/>Web/App/Partner]
    end
    
    subgraph "API Gateway 層"
        Kong[Kong API Gateway<br/>認證/限流/路由/日誌]
    end
    
    subgraph "內部微服務"
        S1[用戶服務]
        S2[訂單服務]
        S3[支付服務]
        S4[通知服務]
    end
    
    Client --> Kong
    Kong --> S1
    Kong --> S2
    Kong --> S3
    Kong --> S4
```

#### API Gateway 核心功能

1. **請求路由（Routing）**：根據路徑、Host、Method 將請求導向正確的後端服務
2. **負載均衡（Load Balancing）**：分散流量到多個後端實例
3. **認證授權（Authentication/Authorization）**：驗證 API Key、JWT、OAuth Token
4. **限流熔斷（Rate Limiting/Circuit Breaker）**：保護後端服務不被過載
5. **請求轉換（Request/Response Transformation）**：修改 Header、Body
6. **可觀測性（Observability）**：收集 Metrics、Logs、Traces

### 1.3 Kong 在微服務架構中的角色

```mermaid
graph TB
    subgraph "DMZ / Edge"
        LB[Load Balancer<br/>F5 / Nginx / Cloud LB]
    end
    
    subgraph "API Gateway 層"
        Kong1[Kong Node 1]
        Kong2[Kong Node 2]
    end
    
    subgraph "Service Mesh / 內部網路"
        Auth[IAM / Keycloak]
        SVC1[Service A]
        SVC2[Service B]
        SVC3[Service C]
    end
    
    subgraph "資料層"
        DB[(Database)]
        Cache[(Redis Cache)]
    end
    
    LB --> Kong1
    LB --> Kong2
    Kong1 --> SVC1
    Kong1 --> SVC2
    Kong2 --> SVC2
    Kong2 --> SVC3
    Kong1 -.-> Auth
    Kong2 -.-> Auth
    SVC1 --> DB
    SVC2 --> Cache
```

**Kong 的定位**：
- 位於 **Load Balancer 之後、微服務之前**
- 處理「南北向」流量（外部進入內部）
- 不處理「東西向」流量（服務間通訊），那是 Service Mesh 的職責

### 1.4 Kong OSS / Enterprise 差異簡介

| 特性 | Kong OSS（開源版） | Kong Enterprise |
|-----|-------------------|-----------------|
| **授權** | Apache 2.0 | 商業授權 |
| **核心功能** | ✅ 完整 | ✅ 完整 |
| **Admin API** | ✅ | ✅ |
| **Kong Manager（GUI）** | ❌ | ✅ |
| **RBAC 權限控管** | ❌ | ✅ |
| **開發者入口網站** | ❌ | ✅ |
| **進階 Plugin** | 部分 | 全部（含 OPA、Vault 整合） |
| **官方技術支援** | ❌ 社群支援 | ✅ 24/7 支援 |
| **適用情境** | 中小型專案、學習 | 大型企業、金融業 |

> 💡 **實務建議**：企業內部若有合規需求（如金融業），建議評估 Enterprise 版。若預算有限，OSS 版搭配自建監控也可滿足大部分需求。

---

## 2. 系統架構設計

### 2.1 Kong API Gateway 整體架構圖

```mermaid
graph TB
    subgraph "Kong Gateway 架構"
        subgraph "Data Plane（資料平面）"
            DP1[Kong Proxy Node 1<br/>處理實際 API 請求]
            DP2[Kong Proxy Node 2<br/>處理實際 API 請求]
        end
        
        subgraph "Control Plane（控制平面）"
            CP[Kong Control Plane<br/>管理設定與 Plugin]
            AdminAPI[Admin API<br/>:8001]
            Manager[Kong Manager<br/>:8002]
        end
        
        subgraph "資料儲存"
            PG[(PostgreSQL<br/>儲存設定)]
            ConfigFile[kong.yml<br/>DB-less 模式]
        end
    end
    
    Client[外部請求] --> DP1
    Client --> DP2
    Admin[管理員] --> AdminAPI
    Admin --> Manager
    CP --> PG
    CP --> ConfigFile
    CP -.->|同步設定| DP1
    CP -.->|同步設定| DP2
```

### 2.2 核心元件說明

#### 2.2.1 Kong Gateway（Proxy）

- **職責**：處理所有進入的 API 請求
- **監聽埠**：
  - `:8000` - HTTP Proxy
  - `:8443` - HTTPS Proxy
- **特性**：無狀態（Stateless），可水平擴展

#### 2.2.2 Admin API

- **職責**：提供 RESTful API 管理 Kong 設定
- **監聽埠**：`:8001`（HTTP）、`:8444`（HTTPS）
- **用途**：新增 Service、Route、Plugin、Consumer 等

```bash
# 範例：查詢所有 Services
curl -X GET http://localhost:8001/services

# 範例：新增一個 Service
curl -X POST http://localhost:8001/services \
  --data name=my-service \
  --data url=http://backend:8080
```

#### 2.2.3 Data Plane / Control Plane

**傳統模式（Traditional）**：
- 單一節點同時處理 Proxy 與管理功能
- 適合小型部署

**混合模式（Hybrid Mode）**：
- Control Plane：集中管理設定
- Data Plane：分散處理請求
- 適合大型、多區域部署

```mermaid
graph LR
    subgraph "Control Plane（管理區）"
        CP[Control Plane<br/>集中設定]
    end
    
    subgraph "Data Plane - Region A"
        DP_A1[DP Node 1]
        DP_A2[DP Node 2]
    end
    
    subgraph "Data Plane - Region B"
        DP_B1[DP Node 1]
        DP_B2[DP Node 2]
    end
    
    CP -->|WebSocket 同步| DP_A1
    CP -->|WebSocket 同步| DP_A2
    CP -->|WebSocket 同步| DP_B1
    CP -->|WebSocket 同步| DP_B2
```

#### 2.2.4 Database（PostgreSQL / DB-less）

| 模式 | 說明 | 適用情境 |
|-----|------|---------|
| **DB-backed** | 使用 PostgreSQL 儲存設定 | 動態管理、多節點共享設定 |
| **DB-less** | 使用 YAML 檔案宣告設定 | GitOps、Kubernetes、CI/CD |

### 2.3 與後端微服務、LB、Auth Server 的關係

```mermaid
sequenceDiagram
    participant Client as 客戶端
    participant LB as Load Balancer
    participant Kong as Kong Gateway
    participant Auth as Auth Server<br/>(Keycloak)
    participant Backend as 後端服務
    
    Client->>LB: 1. HTTPS 請求
    LB->>Kong: 2. 轉發請求
    Kong->>Kong: 3. 執行 Pre-Plugins<br/>(Rate Limit, Auth)
    Kong->>Auth: 4. 驗證 Token（可選）
    Auth-->>Kong: 5. Token 有效
    Kong->>Backend: 6. 轉發到後端
    Backend-->>Kong: 7. 回應
    Kong->>Kong: 8. 執行 Post-Plugins<br/>(Transform, Log)
    Kong-->>LB: 9. 回應
    LB-->>Client: 10. 最終回應
```

### 2.4 典型企業架構範例

#### 情境：銀行內部 API 平台

```mermaid
graph TB
    subgraph "外部區域（DMZ）"
        Internet[Internet]
        WAF[WAF<br/>Web Application Firewall]
        ExtLB[External LB]
    end
    
    subgraph "API Gateway 區"
        Kong_Ext[Kong External<br/>對外 API]
    end
    
    subgraph "內部區域"
        IntLB[Internal LB]
        Kong_Int[Kong Internal<br/>內部 API]
        
        subgraph "核心服務"
            CoreBanking[核心銀行系統]
            AccountSvc[帳戶服務]
            PaymentSvc[支付服務]
        end
        
        subgraph "共用服務"
            Keycloak[Keycloak IAM]
            Redis[(Redis Cache)]
        end
    end
    
    Internet --> WAF --> ExtLB --> Kong_Ext
    Kong_Ext --> IntLB
    IntLB --> Kong_Int
    Kong_Int --> CoreBanking
    Kong_Int --> AccountSvc
    Kong_Int --> PaymentSvc
    Kong_Ext -.-> Keycloak
    Kong_Int -.-> Keycloak
    Kong_Ext -.-> Redis
```

> ⚠️ **實務注意**：
> - Kong 不應直接暴露在 Internet，前面應有 WAF 和 Load Balancer
> - 內部 API 與外部 API 建議使用不同的 Kong 實例（隔離風險）
> - Admin API 絕對不能對外開放

---

## 3. 安裝與部署

### 3.1 安裝模式說明

#### 3.1.1 DB-less Mode（無資料庫模式）

**特點**：
- 使用 YAML 檔案（`kong.yml`）宣告所有設定
- 無需 PostgreSQL
- 設定透過檔案或 Admin API 載入
- **適合**：Kubernetes、GitOps、CI/CD 流程

**限制**：
- 部分 Plugin 無法使用（如 OAuth2 需要儲存 Token）
- 無法透過 Admin API 動態新增設定（需重新載入）

#### 3.1.2 DB-backed Mode（資料庫模式）

**特點**：
- 使用 PostgreSQL 儲存所有設定
- 可透過 Admin API 動態管理
- 多個 Kong 節點共享設定
- **適合**：傳統部署、需要動態管理的環境

### 3.2 常見部署方式

#### 3.2.1 Docker 單機部署

**DB-less 模式**：

```bash
# 1. 建立設定檔 kong.yml
cat > kong.yml <<EOF
_format_version: "3.0"

services:
  - name: demo-service
    url: http://httpbin.org
    routes:
      - name: demo-route
        paths:
          - /demo
EOF

# 2. 啟動 Kong（DB-less）
docker run -d --name kong \
  -e "KONG_DATABASE=off" \
  -e "KONG_DECLARATIVE_CONFIG=/kong/declarative/kong.yml" \
  -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
  -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
  -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
  -v "$(pwd)/kong.yml:/kong/declarative/kong.yml:ro" \
  -p 8000:8000 \
  -p 8001:8001 \
  kong:3.9
```

#### 3.2.2 Docker Compose 部署（含 PostgreSQL）

```yaml
# docker-compose.yml
version: '3.8'

services:
  kong-database:
    image: postgres:15-alpine
    container_name: kong-database
    environment:
      POSTGRES_USER: kong
      POSTGRES_PASSWORD: kongpass
      POSTGRES_DB: kong
    volumes:
      - kong_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U kong"]
      interval: 10s
      timeout: 5s
      retries: 5

  kong-migration:
    image: kong:3.9
    command: kong migrations bootstrap
    depends_on:
      kong-database:
        condition: service_healthy
    environment:
      KONG_DATABASE: postgres
      KONG_PG_HOST: kong-database
      KONG_PG_USER: kong
      KONG_PG_PASSWORD: kongpass
    restart: on-failure

  kong:
    image: kong:3.9
    container_name: kong
    depends_on:
      kong-migration:
        condition: service_completed_successfully
    environment:
      KONG_DATABASE: postgres
      KONG_PG_HOST: kong-database
      KONG_PG_USER: kong
      KONG_PG_PASSWORD: kongpass
      KONG_PROXY_ACCESS_LOG: /dev/stdout
      KONG_ADMIN_ACCESS_LOG: /dev/stdout
      KONG_PROXY_ERROR_LOG: /dev/stderr
      KONG_ADMIN_ERROR_LOG: /dev/stderr
      KONG_ADMIN_LISTEN: 0.0.0.0:8001
      KONG_PROXY_LISTEN: 0.0.0.0:8000, 0.0.0.0:8443 ssl
    ports:
      - "8000:8000"   # Proxy HTTP
      - "8443:8443"   # Proxy HTTPS
      - "8001:8001"   # Admin API
    healthcheck:
      test: ["CMD", "kong", "health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

volumes:
  kong_data:
```

**啟動指令**：

```bash
# 啟動所有服務
docker-compose up -d

# 檢查狀態
docker-compose ps

# 查看 Kong 日誌
docker-compose logs -f kong
```

#### 3.2.3 Kubernetes 部署

使用官方 Helm Chart：

```bash
# 1. 新增 Kong Helm Repo
helm repo add kong https://charts.konghq.com
helm repo update

# 2. 建立 namespace
kubectl create namespace kong

# 3. 安裝 Kong（DB-less 模式 + Ingress Controller）
helm install kong kong/kong \
  --namespace kong \
  --set ingressController.installCRDs=false \
  --set env.database=off \
  --set admin.enabled=true \
  --set admin.http.enabled=true

# 4. 安裝 Kong（DB-backed 模式）
helm install kong kong/kong \
  --namespace kong \
  --set env.database=postgres \
  --set postgresql.enabled=true \
  --set postgresql.auth.username=kong \
  --set postgresql.auth.password=kongpass \
  --set admin.enabled=true
```

**Kubernetes CRD 範例（KongIngress）**：

```yaml
# kong-ingress.yaml
apiVersion: configuration.konghq.com/v1
kind: KongIngress
metadata:
  name: demo-kong-ingress
route:
  strip_path: true
  preserve_host: false
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: demo-ingress
  annotations:
    konghq.com/override: demo-kong-ingress
spec:
  ingressClassName: kong
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /demo
            pathType: Prefix
            backend:
              service:
                name: demo-service
                port:
                  number: 80
```

### 3.3 安裝後檢查方式

```bash
# 1. 檢查 Kong 版本
curl -s http://localhost:8001 | jq '.version'

# 2. 檢查節點狀態
curl -s http://localhost:8001/status | jq

# 3. 檢查已載入的 Plugin
curl -s http://localhost:8001/plugins/enabled | jq

# 4. 測試 Proxy 功能（需先設定 Service/Route）
curl -i http://localhost:8000/demo

# 5. 健康檢查端點
curl -s http://localhost:8001/status | jq '.database.reachable'
```

**預期輸出範例**：

```json
{
  "database": {
    "reachable": true
  },
  "memory": {
    "workers_lua_vms": [...],
    "lua_shared_dicts": {...}
  },
  "server": {
    "connections_active": 1,
    "connections_accepted": 10,
    "connections_handled": 10,
    "connections_reading": 0,
    "connections_writing": 1,
    "connections_waiting": 0,
    "total_requests": 50
  }
}
```

> ⚠️ **常見安裝問題**：
> - **Port 衝突**：確認 8000、8001 未被佔用
> - **資料庫連線失敗**：檢查 PostgreSQL 是否啟動、帳密是否正確
> - **Migration 失敗**：確認資料庫版本相容（PostgreSQL 12+）

---

## 4. 基本設定與核心概念

### 4.1 Service / Route / Upstream / Target 說明

Kong 的核心物件關係：

```mermaid
graph LR
    subgraph "Kong 內部物件"
        Route[Route<br/>路由規則]
        Service[Service<br/>服務定義]
        Upstream[Upstream<br/>上游服務群]
        Target1[Target 1<br/>實際節點]
        Target2[Target 2<br/>實際節點]
    end
    
    Client[請求] --> Route
    Route --> Service
    Service --> Upstream
    Upstream --> Target1
    Upstream --> Target2
```

#### 4.1.1 Service（服務）

代表一個後端服務的抽象定義。

```bash
# 建立 Service（直接指定 URL）
curl -X POST http://localhost:8001/services \
  --data name=user-service \
  --data url=http://user-backend:8080

# 建立 Service（指定 Upstream）
curl -X POST http://localhost:8001/services \
  --data name=user-service \
  --data host=user-upstream \
  --data port=80 \
  --data protocol=http
```

| 參數 | 說明 |
|-----|------|
| `name` | 服務名稱（唯一識別） |
| `url` | 後端服務完整 URL |
| `host` | 後端主機名或 Upstream 名稱 |
| `port` | 後端埠號 |
| `protocol` | http 或 https |
| `path` | 請求路徑前綴 |
| `connect_timeout` | 連線逾時（毫秒） |
| `read_timeout` | 讀取逾時（毫秒） |

#### 4.1.2 Route（路由）

定義請求如何匹配到特定 Service。

```bash
# 建立 Route
curl -X POST http://localhost:8001/services/user-service/routes \
  --data name=user-route \
  --data "paths[]=/api/users" \
  --data "methods[]=GET" \
  --data "methods[]=POST" \
  --data strip_path=true
```

| 參數 | 說明 |
|-----|------|
| `paths` | 匹配的 URL 路徑 |
| `hosts` | 匹配的 Host Header |
| `methods` | 匹配的 HTTP Method |
| `headers` | 匹配的 Header |
| `strip_path` | 是否移除匹配的路徑前綴 |
| `preserve_host` | 是否保留原始 Host Header |

#### 4.1.3 Upstream / Target（上游與目標）

用於負載均衡場景。

```bash
# 建立 Upstream
curl -X POST http://localhost:8001/upstreams \
  --data name=user-upstream \
  --data algorithm=round-robin

# 新增 Target（後端實例）
curl -X POST http://localhost:8001/upstreams/user-upstream/targets \
  --data target=user-backend-1:8080 \
  --data weight=100

curl -X POST http://localhost:8001/upstreams/user-upstream/targets \
  --data target=user-backend-2:8080 \
  --data weight=100
```

| 負載均衡演算法 | 說明 |
|--------------|------|
| `round-robin` | 輪詢（預設） |
| `consistent-hashing` | 一致性雜湊（適合快取場景） |
| `least-connections` | 最少連線數 |
| `latency` | 最低延遲 |

### 4.2 Consumer 概念

**Consumer** 代表使用 API 的用戶端（應用程式、用戶）。

```bash
# 建立 Consumer
curl -X POST http://localhost:8001/consumers \
  --data username=mobile-app \
  --data custom_id=app-001

# 為 Consumer 建立認證憑證（API Key）
curl -X POST http://localhost:8001/consumers/mobile-app/key-auth \
  --data key=my-secret-api-key
```

**Consumer 的用途**：
- 綁定認證憑證（API Key、JWT、OAuth）
- 設定個別的 Rate Limiting
- ACL 權限控管

### 4.3 Plugin 架構與執行流程

```mermaid
sequenceDiagram
    participant Client
    participant Kong
    participant Backend
    
    Client->>Kong: 1. 請求進入
    Note over Kong: 2. Certificate Phase
    Note over Kong: 3. Rewrite Phase
    Note over Kong: 4. Access Phase<br/>(Auth, Rate Limit, ACL)
    Kong->>Backend: 5. Proxy 到後端
    Backend-->>Kong: 6. 後端回應
    Note over Kong: 7. Header Filter Phase
    Note over Kong: 8. Body Filter Phase
    Note over Kong: 9. Log Phase
    Kong-->>Client: 10. 回應客戶端
```

#### Plugin 執行順序

| 階段 | 說明 | 常見 Plugin |
|-----|------|------------|
| **Certificate** | TLS 憑證處理 | - |
| **Rewrite** | 請求改寫 | Request Transformer |
| **Access** | 存取控制 | Key-Auth, JWT, Rate Limiting, ACL |
| **Header Filter** | 回應 Header 處理 | Response Transformer |
| **Body Filter** | 回應 Body 處理 | Response Transformer |
| **Log** | 日誌記錄 | File Log, HTTP Log, Prometheus |

#### Plugin 作用範圍

Plugin 可以套用在不同層級：

```bash
# 全域（所有請求）
curl -X POST http://localhost:8001/plugins \
  --data name=rate-limiting \
  --data config.minute=100

# Service 層級
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=rate-limiting \
  --data config.minute=50

# Route 層級
curl -X POST http://localhost:8001/routes/user-route/plugins \
  --data name=rate-limiting \
  --data config.minute=20

# Consumer 層級
curl -X POST http://localhost:8001/consumers/mobile-app/plugins \
  --data name=rate-limiting \
  --data config.minute=1000
```

**優先順序**：Consumer > Route > Service > Global

### 4.4 宣告式設定（Declarative Config）

DB-less 模式使用 YAML 檔案定義所有設定：

```yaml
# kong.yml
_format_version: "3.0"
_transform: true

services:
  - name: user-service
    url: http://user-backend:8080
    routes:
      - name: user-route
        paths:
          - /api/users
        strip_path: true
    plugins:
      - name: rate-limiting
        config:
          minute: 100
          policy: local

  - name: order-service
    url: http://order-backend:8080
    routes:
      - name: order-route
        paths:
          - /api/orders
        methods:
          - GET
          - POST

consumers:
  - username: mobile-app
    keyauth_credentials:
      - key: mobile-app-key-001

plugins:
  - name: prometheus
  - name: correlation-id
    config:
      header_name: X-Request-ID
      generator: uuid
```

**載入設定**：

```bash
# 方式 1：啟動時載入
docker run -e KONG_DECLARATIVE_CONFIG=/kong.yml ...

# 方式 2：透過 Admin API 動態載入
curl -X POST http://localhost:8001/config \
  -F config=@kong.yml
```

### 4.5 Admin API 使用方式概覽

| 操作 | HTTP Method | 端點範例 |
|-----|-------------|---------|
| 列出所有 | GET | `/services`, `/routes`, `/plugins` |
| 取得單一 | GET | `/services/{name or id}` |
| 新增 | POST | `/services` |
| 更新（部分）| PATCH | `/services/{name or id}` |
| 更新（完整）| PUT | `/services/{name or id}` |
| 刪除 | DELETE | `/services/{name or id}` |

**常用指令速查**：

```bash
# 列出所有 Services
curl -s http://localhost:8001/services | jq

# 列出所有 Routes
curl -s http://localhost:8001/routes | jq

# 列出所有 Plugins
curl -s http://localhost:8001/plugins | jq

# 列出特定 Service 的 Routes
curl -s http://localhost:8001/services/user-service/routes | jq

# 列出所有 Consumers
curl -s http://localhost:8001/consumers | jq
```

> 💡 **實務建議**：
> - 使用 [decK](https://docs.konghq.com/deck/) 工具管理設定（GitOps）
> - Admin API 應限制內部網路存取
> - 生產環境建議關閉 Admin API 的 HTTP，僅開放 HTTPS

---

## 5. Kong API Gateway 實際使用教學

### 5.1 建立第一個 API（Service + Route）

**情境**：將 `/api/demo` 路由到 `httpbin.org`

```bash
# Step 1: 建立 Service
curl -X POST http://localhost:8001/services \
  --data name=demo-service \
  --data url=http://httpbin.org

# Step 2: 建立 Route
curl -X POST http://localhost:8001/services/demo-service/routes \
  --data name=demo-route \
  --data "paths[]=/api/demo" \
  --data strip_path=true

# Step 3: 測試
curl -i http://localhost:8000/api/demo/get
```

**預期結果**：

```
HTTP/1.1 200 OK
Content-Type: application/json
...

{
  "args": {},
  "headers": {
    "Host": "httpbin.org",
    ...
  },
  "origin": "...",
  "url": "http://httpbin.org/get"
}
```

### 5.2 API 路由策略

#### 5.2.1 基於 Path 路由

```bash
# /api/v1/users → user-service-v1
curl -X POST http://localhost:8001/services/user-service-v1/routes \
  --data "paths[]=/api/v1/users"

# /api/v2/users → user-service-v2
curl -X POST http://localhost:8001/services/user-service-v2/routes \
  --data "paths[]=/api/v2/users"
```

#### 5.2.2 基於 Host 路由

```bash
# api.example.com → external-api-service
curl -X POST http://localhost:8001/services/external-api/routes \
  --data "hosts[]=api.example.com"

# internal-api.local → internal-api-service
curl -X POST http://localhost:8001/services/internal-api/routes \
  --data "hosts[]=internal-api.local"
```

#### 5.2.3 基於 Method 路由

```bash
# GET /users → user-read-service
curl -X POST http://localhost:8001/services/user-read-service/routes \
  --data "paths[]=/users" \
  --data "methods[]=GET"

# POST, PUT, DELETE /users → user-write-service
curl -X POST http://localhost:8001/services/user-write-service/routes \
  --data "paths[]=/users" \
  --data "methods[]=POST" \
  --data "methods[]=PUT" \
  --data "methods[]=DELETE"
```

### 5.3 Load Balancing 與 Health Check

```bash
# Step 1: 建立 Upstream
curl -X POST http://localhost:8001/upstreams \
  --data name=user-upstream \
  --data algorithm=round-robin \
  --data healthchecks.active.healthy.interval=5 \
  --data healthchecks.active.unhealthy.interval=5 \
  --data healthchecks.active.http_path=/health \
  --data healthchecks.active.healthy.successes=2 \
  --data healthchecks.active.unhealthy.http_failures=3

# Step 2: 新增 Targets
curl -X POST http://localhost:8001/upstreams/user-upstream/targets \
  --data target=user-backend-1:8080 \
  --data weight=100

curl -X POST http://localhost:8001/upstreams/user-upstream/targets \
  --data target=user-backend-2:8080 \
  --data weight=100

curl -X POST http://localhost:8001/upstreams/user-upstream/targets \
  --data target=user-backend-3:8080 \
  --data weight=50  # 權重較低，分配較少流量

# Step 3: 建立 Service 指向 Upstream
curl -X POST http://localhost:8001/services \
  --data name=user-service \
  --data host=user-upstream

# Step 4: 建立 Route
curl -X POST http://localhost:8001/services/user-service/routes \
  --data "paths[]=/api/users"
```

#### Health Check 類型

| 類型 | 說明 |
|-----|------|
| **Active** | Kong 主動定期檢查後端健康 |
| **Passive** | 根據實際請求結果判斷健康狀態 |

```yaml
# YAML 設定範例
upstreams:
  - name: user-upstream
    algorithm: round-robin
    healthchecks:
      active:
        http_path: /health
        healthy:
          interval: 5
          successes: 2
        unhealthy:
          interval: 5
          http_failures: 3
          tcp_failures: 3
          timeouts: 3
      passive:
        healthy:
          successes: 5
        unhealthy:
          http_failures: 5
          tcp_failures: 5
          timeouts: 5
```

### 5.4 完整請求流程範例

```mermaid
sequenceDiagram
    participant Client as 客戶端
    participant Kong as Kong Gateway<br/>:8000
    participant Auth as Auth Plugin
    participant RateLimit as Rate Limit Plugin
    participant Backend as 後端服務
    
    Client->>Kong: GET /api/users<br/>Header: apikey=xxx
    Kong->>Kong: 匹配 Route: /api/users
    Kong->>Auth: 驗證 API Key
    Auth-->>Kong: ✅ 驗證通過
    Kong->>RateLimit: 檢查限流
    RateLimit-->>Kong: ✅ 未超過限制
    Kong->>Backend: GET /users<br/>(strip_path=true)
    Backend-->>Kong: 200 OK + JSON
    Kong->>Kong: 記錄日誌、收集 Metrics
    Kong-->>Client: 200 OK + JSON
```

---

## 6. 常用 Plugins 實務說明

### 6.1 Rate Limiting（限流）

**使用情境**：
- 防止 API 被惡意刷爆
- 依據客戶等級提供不同配額
- 保護後端服務

```bash
# 全域限流：每分鐘 100 次
curl -X POST http://localhost:8001/plugins \
  --data name=rate-limiting \
  --data config.minute=100 \
  --data config.policy=local

# 針對特定 Service
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=rate-limiting \
  --data config.minute=50 \
  --data config.hour=1000 \
  --data config.policy=redis \
  --data config.redis_host=redis \
  --data config.redis_port=6379
```

| 參數 | 說明 |
|-----|------|
| `second/minute/hour/day/month/year` | 各時間單位的限制數 |
| `policy` | `local`（單節點）、`cluster`（DB）、`redis`（分散式） |
| `limit_by` | `consumer`、`credential`、`ip`、`header` |
| `hide_client_headers` | 是否隱藏 `X-RateLimit-*` Header |

> ⚠️ **實務注意**：
> - 多節點環境必須使用 `redis` 或 `cluster` policy
> - `local` policy 各節點獨立計算，總限制會是「節點數 × 設定值」

### 6.2 Key Authentication

**使用情境**：
- 簡單的 API 存取控制
- 識別不同的 API 呼叫方

```bash
# Step 1: 啟用 Key Auth Plugin
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=key-auth \
  --data config.key_names=apikey \
  --data config.hide_credentials=true

# Step 2: 建立 Consumer
curl -X POST http://localhost:8001/consumers \
  --data username=partner-app

# Step 3: 為 Consumer 建立 API Key
curl -X POST http://localhost:8001/consumers/partner-app/key-auth \
  --data key=partner-secret-key-001

# Step 4: 測試
curl -i http://localhost:8000/api/users \
  -H "apikey: partner-secret-key-001"
```

| 參數 | 說明 |
|-----|------|
| `key_names` | Key 的 Header/Query 參數名稱 |
| `key_in_header` | 允許從 Header 傳遞（預設 true） |
| `key_in_query` | 允許從 Query String 傳遞（預設 true） |
| `key_in_body` | 允許從 Body 傳遞 |
| `hide_credentials` | 轉發給後端時是否移除 Key |

### 6.3 JWT Authentication

**使用情境**：
- 與 OAuth/OIDC 系統整合
- 無狀態的 Token 驗證
- 適合分散式系統

```bash
# Step 1: 啟用 JWT Plugin
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=jwt \
  --data config.claims_to_verify=exp

# Step 2: 建立 Consumer
curl -X POST http://localhost:8001/consumers \
  --data username=jwt-user

# Step 3: 為 Consumer 建立 JWT 憑證
curl -X POST http://localhost:8001/consumers/jwt-user/jwt \
  --data algorithm=HS256 \
  --data key=my-jwt-issuer \
  --data secret=my-jwt-secret

# Step 4: 產生 JWT Token（範例）
# Header: {"alg": "HS256", "typ": "JWT"}
# Payload: {"iss": "my-jwt-issuer", "exp": 1893456000}
# 使用 secret 簽名

# Step 5: 測試
curl -i http://localhost:8000/api/users \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..."
```

**使用 RS256（非對稱加密）**：

```bash
# 建立 RSA Key Pair 的 JWT 憑證
curl -X POST http://localhost:8001/consumers/jwt-user/jwt \
  --data algorithm=RS256 \
  --data key=my-jwt-issuer \
  --data rsa_public_key="-----BEGIN PUBLIC KEY-----..."
```

> 💡 **實務建議**：
> - 生產環境建議使用 RS256（非對稱），避免 Secret 外洩風險
> - 可搭配 Keycloak 等 IdP 使用 JWKS 端點動態取得公鑰

### 6.4 OAuth 2.0（概念）

Kong 支援作為 OAuth 2.0 Provider，但實務上建議：

```mermaid
graph LR
    Client[Client] --> Kong[Kong Gateway]
    Kong --> Auth[Keycloak / Auth0<br/>OAuth Provider]
    Auth --> Kong
    Kong --> Backend[Backend Service]
```

**推薦做法**：
1. 使用外部 OAuth Provider（Keycloak、Auth0、Okta）
2. Kong 負責驗證 Access Token（使用 JWT Plugin）
3. 不在 Kong 實作完整 OAuth Flow

```bash
# 與 Keycloak 整合範例（驗證 JWT）
curl -X POST http://localhost:8001/plugins \
  --data name=jwt \
  --data config.uri_param_names=access_token \
  --data config.claims_to_verify=exp
```

### 6.5 ACL（存取控制清單）

**使用情境**：
- 限制特定 Consumer 群組才能存取 API
- 實現 RBAC（Role-Based Access Control）

```bash
# Step 1: 啟用 ACL Plugin
curl -X POST http://localhost:8001/services/admin-service/plugins \
  --data name=acl \
  --data config.allow=admin-group \
  --data config.hide_groups_header=true

# Step 2: 將 Consumer 加入群組
curl -X POST http://localhost:8001/consumers/admin-user/acls \
  --data group=admin-group

# 需搭配認證 Plugin（如 Key Auth）一起使用
```

### 6.6 CORS

**使用情境**：
- 前端 SPA 呼叫 API
- 跨域資源共享控制

```bash
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=cors \
  --data "config.origins[]=https://app.example.com" \
  --data "config.methods[]=GET" \
  --data "config.methods[]=POST" \
  --data "config.methods[]=PUT" \
  --data "config.methods[]=DELETE" \
  --data "config.headers[]=Content-Type" \
  --data "config.headers[]=Authorization" \
  --data config.credentials=true \
  --data config.max_age=3600
```

| 參數 | 說明 |
|-----|------|
| `origins` | 允許的來源（支援萬用字元 `*`） |
| `methods` | 允許的 HTTP Method |
| `headers` | 允許的 Request Header |
| `exposed_headers` | 允許前端存取的 Response Header |
| `credentials` | 是否允許攜帶 Cookie |
| `max_age` | Preflight 快取時間（秒） |

> ⚠️ **安全注意**：避免使用 `origins: *` 搭配 `credentials: true`

### 6.7 Request / Response Transformer

**使用情境**：
- 添加/修改/移除 Header
- 修改 Request Body
- API 版本轉換

```bash
# Request Transformer：添加 Header
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=request-transformer \
  --data "config.add.headers[]=X-Custom-Header:custom-value" \
  --data "config.add.headers[]=X-Request-Source:kong" \
  --data "config.remove.headers[]=X-Forwarded-Host"

# Response Transformer：修改回應
curl -X POST http://localhost:8001/services/user-service/plugins \
  --data name=response-transformer \
  --data "config.add.headers[]=X-Kong-Proxy:true" \
  --data "config.remove.headers[]=Server"
```

### 6.8 Prometheus Plugin

**使用情境**：
- 收集 Kong Metrics
- 整合 Prometheus + Grafana 監控

```bash
# 啟用 Prometheus Plugin（全域）
curl -X POST http://localhost:8001/plugins \
  --data name=prometheus \
  --data config.per_consumer=true \
  --data config.status_code_metrics=true \
  --data config.latency_metrics=true \
  --data config.bandwidth_metrics=true \
  --data config.upstream_health_metrics=true

# Prometheus 端點
curl http://localhost:8001/metrics
```

**主要 Metrics**：

| Metric | 說明 |
|--------|------|
| `kong_http_requests_total` | 總請求數 |
| `kong_request_latency_ms` | 請求延遲 |
| `kong_upstream_latency_ms` | 後端回應延遲 |
| `kong_bandwidth_bytes` | 流量統計 |
| `kong_upstream_target_health` | 後端健康狀態 |

### 6.9 Logging Plugins

#### File Log

```bash
curl -X POST http://localhost:8001/plugins \
  --data name=file-log \
  --data config.path=/var/log/kong/access.log \
  --data config.reopen=true
```

#### HTTP Log（送至 ELK）

```bash
curl -X POST http://localhost:8001/plugins \
  --data name=http-log \
  --data config.http_endpoint=http://logstash:5044 \
  --data config.method=POST \
  --data config.content_type="application/json" \
  --data config.timeout=10000 \
  --data config.keepalive=60000
```

#### TCP Log

```bash
curl -X POST http://localhost:8001/plugins \
  --data name=tcp-log \
  --data config.host=logstash \
  --data config.port=5000
```

---

## 7. 應用系統如何串接 Kong

### 7.1 後端微服務如何被 Kong 管理

```mermaid
graph TB
    subgraph "Kong Gateway"
        Route1[Route: /api/users]
        Route2[Route: /api/orders]
        Service1[Service: user-service]
        Service2[Service: order-service]
    end
    
    subgraph "後端微服務"
        UserSvc[User Service<br/>:8081]
        OrderSvc[Order Service<br/>:8082]
    end
    
    Route1 --> Service1 --> UserSvc
    Route2 --> Service2 --> OrderSvc
```

**後端服務無需修改**，只需確保：
1. 提供健康檢查端點（`/health` 或 `/actuator/health`）
2. 正確處理 `X-Forwarded-*` Header
3. 信任來自 Kong 的請求（內網隔離）

### 7.2 前端 / App 如何呼叫 Kong API

#### JavaScript（Fetch API）

```javascript
// 使用 API Key
const response = await fetch('https://api.example.com/api/users', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'apikey': 'your-api-key'
  }
});

// 使用 JWT Token
const response = await fetch('https://api.example.com/api/users', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${accessToken}`
  }
});
```

#### Java / Spring Boot（RestTemplate）

```java
@Service
public class ApiService {
    
    private final RestTemplate restTemplate;
    
    @Value("${kong.api.base-url}")
    private String kongBaseUrl;
    
    @Value("${kong.api.key}")
    private String apiKey;
    
    public UserResponse getUsers() {
        HttpHeaders headers = new HttpHeaders();
        headers.set("apikey", apiKey);
        headers.setContentType(MediaType.APPLICATION_JSON);
        
        HttpEntity<Void> entity = new HttpEntity<>(headers);
        
        ResponseEntity<UserResponse> response = restTemplate.exchange(
            kongBaseUrl + "/api/users",
            HttpMethod.GET,
            entity,
            UserResponse.class
        );
        
        return response.getBody();
    }
}
```

#### Java / Spring Boot（WebClient）

```java
@Service
public class ApiService {
    
    private final WebClient webClient;
    
    public ApiService(WebClient.Builder webClientBuilder,
                      @Value("${kong.api.base-url}") String kongBaseUrl,
                      @Value("${kong.api.key}") String apiKey) {
        this.webClient = webClientBuilder
            .baseUrl(kongBaseUrl)
            .defaultHeader("apikey", apiKey)
            .build();
    }
    
    public Mono<UserResponse> getUsers() {
        return webClient.get()
            .uri("/api/users")
            .retrieve()
            .bodyToMono(UserResponse.class);
    }
}
```

### 7.3 與 OAuth / SSO / IAM 系統整合

```mermaid
sequenceDiagram
    participant User as 使用者
    participant App as 前端應用
    participant Kong as Kong Gateway
    participant Keycloak as Keycloak
    participant Backend as 後端服務
    
    User->>App: 1. 存取應用
    App->>Keycloak: 2. 導向登入頁
    User->>Keycloak: 3. 輸入帳密
    Keycloak-->>App: 4. 回傳 Auth Code
    App->>Keycloak: 5. 交換 Access Token
    Keycloak-->>App: 6. 回傳 JWT Token
    App->>Kong: 7. API 請求 + Bearer Token
    Kong->>Kong: 8. JWT Plugin 驗證 Token
    Kong->>Backend: 9. 轉發請求
    Backend-->>Kong: 10. 回應
    Kong-->>App: 11. 回應
```

**Kong JWT Plugin 搭配 Keycloak 設定**：

```bash
# 使用 Keycloak 的 JWKS 端點驗證
curl -X POST http://localhost:8001/plugins \
  --data name=jwt \
  --data config.claims_to_verify=exp \
  --data config.key_claim_name=iss
```

**Keycloak 公鑰設定**：

```bash
# 取得 Keycloak 的 JWKS
curl https://keycloak.example.com/realms/myrealm/protocol/openid-connect/certs

# 在 Kong 建立 Consumer 與 JWT 憑證
curl -X POST http://localhost:8001/consumers \
  --data username=keycloak-realm

curl -X POST http://localhost:8001/consumers/keycloak-realm/jwt \
  --data algorithm=RS256 \
  --data key=https://keycloak.example.com/realms/myrealm \
  --data rsa_public_key="-----BEGIN PUBLIC KEY-----..."
```

---

## 8. 監控、日誌與可觀測性

### 8.1 Kong Metrics 說明

Kong 內建多種 Metrics 端點：

| 端點 | 說明 |
|-----|------|
| `/status` | 基本狀態資訊 |
| `/metrics` | Prometheus 格式 Metrics（需啟用 Plugin） |

### 8.2 與 Prometheus / Grafana 整合

#### Step 1: 啟用 Prometheus Plugin

```bash
curl -X POST http://localhost:8001/plugins \
  --data name=prometheus \
  --data config.per_consumer=true \
  --data config.status_code_metrics=true \
  --data config.latency_metrics=true
```

#### Step 2: Prometheus 設定

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'kong'
    scrape_interval: 15s
    static_configs:
      - targets: ['kong:8001']
    metrics_path: /metrics
```

#### Step 3: Grafana Dashboard

推薦使用官方 Dashboard：[Kong Official Dashboard](https://grafana.com/grafana/dashboards/7424)

**關鍵監控指標**：

| 指標 | 說明 | 告警閾值建議 |
|-----|------|-------------|
| `kong_http_requests_total` | 請求總數 | - |
| `kong_request_latency_ms` | 端到端延遲 | P99 > 1000ms |
| `kong_upstream_latency_ms` | 後端延遲 | P99 > 500ms |
| `kong_http_requests_total{code="5xx"}` | 5xx 錯誤 | > 1% |
| `kong_upstream_target_health` | 後端健康 | = 0 |

### 8.3 Log 收集（ELK / OpenSearch）

```mermaid
graph LR
    Kong[Kong Gateway] -->|HTTP Log Plugin| Logstash[Logstash]
    Logstash --> ES[(Elasticsearch)]
    ES --> Kibana[Kibana]
```

#### HTTP Log Plugin 設定

```bash
curl -X POST http://localhost:8001/plugins \
  --data name=http-log \
  --data config.http_endpoint=http://logstash:5044 \
  --data config.method=POST \
  --data config.content_type="application/json" \
  --data config.flush_timeout=2 \
  --data config.retry_count=3
```

#### Logstash Pipeline

```ruby
# logstash.conf
input {
  http {
    port => 5044
    codec => json
  }
}

filter {
  mutate {
    add_field => { "[@metadata][index]" => "kong-logs" }
  }
  
  date {
    match => [ "started_at", "UNIX_MS" ]
    target => "@timestamp"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "kong-logs-%{+YYYY.MM.dd}"
  }
}
```

### 8.4 Trace（OpenTelemetry 整合）

```bash
# 啟用 OpenTelemetry Plugin
curl -X POST http://localhost:8001/plugins \
  --data name=opentelemetry \
  --data config.endpoint=http://otel-collector:4318/v1/traces \
  --data config.resource_attributes.service.name=kong-gateway \
  --data config.headers.Authorization="Bearer xxx"
```

**完整可觀測性架構**：

```mermaid
graph TB
    Kong[Kong Gateway]
    
    subgraph "Metrics"
        Prometheus[Prometheus]
        Grafana[Grafana]
    end
    
    subgraph "Logs"
        Logstash[Logstash]
        ES[(Elasticsearch)]
        Kibana[Kibana]
    end
    
    subgraph "Traces"
        OTel[OTel Collector]
        Jaeger[Jaeger]
    end
    
    Kong -->|Prometheus Plugin| Prometheus --> Grafana
    Kong -->|HTTP Log Plugin| Logstash --> ES --> Kibana
    Kong -->|OpenTelemetry Plugin| OTel --> Jaeger
```

---

## 9. 系統維護與營運

### 9.1 Kong 設定管理建議

#### 使用 decK 進行設定管理

[decK](https://docs.konghq.com/deck/) 是官方推薦的設定管理工具：

```bash
# 安裝 decK
brew install kong/deck/deck  # macOS
# 或下載 binary

# 匯出當前設定
deck dump -o kong.yaml

# 比較差異
deck diff -s kong.yaml

# 同步設定
deck sync -s kong.yaml

# 驗證設定檔
deck validate -s kong.yaml
```

#### GitOps 工作流程

```mermaid
graph LR
    Dev[開發人員] -->|修改 kong.yaml| Git[Git Repository]
    Git -->|PR Review| Review[Code Review]
    Review -->|Merge| Main[Main Branch]
    Main -->|CI/CD| Pipeline[Pipeline]
    Pipeline -->|deck sync| Kong[Kong Gateway]
```

### 9.2 Plugin 管理策略

| 策略 | 說明 |
|-----|------|
| **最小化原則** | 只啟用必要的 Plugin |
| **分層管理** | Global → Service → Route → Consumer |
| **版本控制** | 所有設定納入 Git 管理 |
| **測試驗證** | 變更前在測試環境驗證 |

### 9.3 多環境建議

| 環境 | Kong 配置建議 |
|-----|--------------|
| **DEV** | 單節點、DB-less、寬鬆限流 |
| **SIT/UAT** | 雙節點、DB-backed、模擬生產設定 |
| **PROD** | 多節點 HA、DB-backed/Hybrid、嚴格限流 |

```bash
# 不同環境使用不同設定檔
deck sync -s kong-dev.yaml --kong-addr http://kong-dev:8001
deck sync -s kong-uat.yaml --kong-addr http://kong-uat:8001
deck sync -s kong-prod.yaml --kong-addr http://kong-prod:8001
```

### 9.4 效能與容量規劃

#### 硬體建議

| 規模 | CPU | Memory | 備註 |
|-----|-----|--------|------|
| 小型（< 1K RPS） | 2 cores | 4 GB | 單節點可應付 |
| 中型（1K-10K RPS） | 4 cores | 8 GB | 建議雙節點 |
| 大型（> 10K RPS） | 8+ cores | 16+ GB | 多節點 + 水平擴展 |

#### 調校參數

```nginx
# nginx.conf 關鍵參數
worker_processes auto;
worker_connections 16384;

# Kong 環境變數
KONG_NGINX_WORKER_PROCESSES=auto
KONG_NGINX_PROXY_PROXY_BUFFER_SIZE=160k
KONG_NGINX_PROXY_PROXY_BUFFERS=64 160k
```

### 9.5 常見營運問題與排查

| 問題 | 可能原因 | 排查方式 |
|-----|---------|---------|
| **502 Bad Gateway** | 後端服務不可用 | 檢查 Upstream 健康狀態 |
| **504 Gateway Timeout** | 後端回應太慢 | 調整 timeout 設定、檢查後端效能 |
| **429 Too Many Requests** | 觸發限流 | 檢查 Rate Limiting 設定 |
| **401 Unauthorized** | 認證失敗 | 檢查 API Key/JWT 設定 |
| **高延遲** | Plugin 過多、後端慢 | 檢查 Plugin 數量、後端 Latency |

```bash
# 常用排查指令
# 查看 Kong 錯誤日誌
docker logs kong 2>&1 | grep -i error

# 檢查 Upstream 健康狀態
curl -s http://localhost:8001/upstreams/user-upstream/health | jq

# 檢查 Plugin 執行狀態
curl -s http://localhost:8001/plugins | jq '.data[] | {name, enabled}'
```

---

## 10. 系統升級與版本管理

### 10.1 Kong 升級注意事項

#### 升級前準備

1. **閱讀 Release Notes**：了解 Breaking Changes
2. **備份設定**：`deck dump -o backup.yaml`
3. **備份資料庫**：`pg_dump kong > kong_backup.sql`
4. **測試環境先行**：在非生產環境驗證

#### 版本相容性

| Kong 版本 | PostgreSQL | OpenResty | 備註 |
|----------|------------|-----------|------|
| 3.9.x | 12-16 | 1.25.x | 當前穩定版 |
| 3.8.x | 12-16 | 1.25.x | |
| 3.7.x | 12-15 | 1.21.x | |

### 10.2 Plugin 相容性風險

- 官方 Plugin 通常向後相容
- 第三方 Plugin 需確認版本支援
- 自訂 Plugin 需重新測試

```bash
# 檢查已啟用的 Plugin
curl -s http://localhost:8001/plugins | jq '.data[].name' | sort | uniq
```

### 10.3 升級前檢查清單

```markdown
## Kong 升級前檢查清單

### 準備階段
- [ ] 確認當前版本：`curl localhost:8001 | jq '.version'`
- [ ] 閱讀目標版本 Release Notes
- [ ] 確認 PostgreSQL 版本相容性
- [ ] 確認所有 Plugin 相容性
- [ ] 備份設定：`deck dump -o backup-$(date +%Y%m%d).yaml`
- [ ] 備份資料庫：`pg_dump kong > kong_backup_$(date +%Y%m%d).sql`

### 測試階段
- [ ] 在測試環境執行升級
- [ ] 執行功能測試
- [ ] 執行效能測試
- [ ] 驗證所有 Plugin 正常運作

### 執行階段
- [ ] 通知相關團隊
- [ ] 準備 Rollback 計畫
- [ ] 執行滾動升級
- [ ] 監控錯誤率與延遲

### 驗證階段
- [ ] 確認所有節點版本一致
- [ ] 確認健康檢查正常
- [ ] 確認 Metrics 收集正常
- [ ] 確認日誌無異常
```

### 10.4 升級流程（滾動升級）

```mermaid
sequenceDiagram
    participant LB as Load Balancer
    participant Kong1 as Kong Node 1
    participant Kong2 as Kong Node 2
    participant DB as PostgreSQL
    
    Note over LB,DB: 階段 1: 準備
    Kong1->>DB: 執行 Migration
    
    Note over LB,DB: 階段 2: 升級 Node 1
    LB->>Kong2: 流量導向 Node 2
    Kong1->>Kong1: 停止舊版、啟動新版
    Kong1->>Kong1: 健康檢查通過
    LB->>Kong1: 恢復流量
    
    Note over LB,DB: 階段 3: 升級 Node 2
    LB->>Kong1: 流量導向 Node 1
    Kong2->>Kong2: 停止舊版、啟動新版
    Kong2->>Kong2: 健康檢查通過
    LB->>Kong2: 恢復流量
    
    Note over LB,DB: 階段 4: 驗證
```

**升級指令範例**：

```bash
# 1. 執行 Migration（僅需執行一次）
docker run --rm kong:3.9 kong migrations up

# 2. 執行 Migration finish（如有）
docker run --rm kong:3.9 kong migrations finish

# 3. 滾動重啟各節點
kubectl rollout restart deployment/kong -n kong
```

---

## 11. Best Practices 與常見地雷

### 11.1 API 設計與 Gateway 設計分工

| 職責 | 應該在哪裡處理 |
|-----|---------------|
| **認證（Authentication）** | Kong（JWT、Key Auth） |
| **授權（Authorization）** | Kong（ACL）+ 後端服務 |
| **限流（Rate Limiting）** | Kong |
| **路由（Routing）** | Kong |
| **業務邏輯** | 後端服務 |
| **資料驗證（Validation）** | 後端服務 |
| **業務錯誤處理** | 後端服務 |

### 11.2 不建議在 Kong 做的事情

| ❌ 不建議 | 原因 |
|----------|------|
| 複雜業務邏輯 | 維護困難、效能影響 |
| 資料庫查詢 | 違反單一職責 |
| 大量資料轉換 | 消耗記憶體、增加延遲 |
| Session 管理 | 使用 JWT 或外部 Session Store |
| 檔案上傳處理 | 直接到後端或 CDN |

### 11.3 Plugin 使用過度的風險

```mermaid
graph LR
    Request[請求] --> P1[Plugin 1]
    P1 --> P2[Plugin 2]
    P2 --> P3[Plugin 3]
    P3 --> P4[Plugin 4]
    P4 --> P5[Plugin 5]
    P5 --> Backend[後端]
    
    style P1 fill:#f9f,stroke:#333
    style P2 fill:#f9f,stroke:#333
    style P3 fill:#f9f,stroke:#333
    style P4 fill:#f9f,stroke:#333
    style P5 fill:#f9f,stroke:#333
```

**每增加一個 Plugin**：
- 增加約 0.5-2ms 延遲
- 增加記憶體消耗
- 增加除錯複雜度

> 💡 **建議**：單一 Route 上的 Plugin 數量控制在 5 個以內

### 11.4 安全性與效能常見錯誤

#### 安全性錯誤

| ❌ 錯誤做法 | ✅ 正確做法 |
|-----------|-----------|
| Admin API 對外開放 | 限制內網存取 |
| 使用 HTTP 傳輸 | 使用 HTTPS |
| API Key 寫在程式碼 | 使用環境變數或 Vault |
| 允許所有 CORS Origin | 明確指定允許的 Origin |
| 不設定限流 | 依據業務需求設定合理限流 |

#### 效能錯誤

| ❌ 錯誤做法 | ✅ 正確做法 |
|-----------|-----------|
| 過短的 Health Check 間隔 | 5-10 秒為宜 |
| 過大的 Log 內容 | 只記錄必要資訊 |
| 同步呼叫外部服務驗證 Token | 使用 JWT 本地驗證 |
| 不設定 Timeout | 設定合理的 Timeout |

### 11.5 設定範例：生產環境最佳實踐

```yaml
# kong-production.yaml
_format_version: "3.0"

services:
  - name: user-service
    url: http://user-upstream
    connect_timeout: 5000
    write_timeout: 60000
    read_timeout: 60000
    retries: 3
    routes:
      - name: user-route
        paths:
          - /api/users
        strip_path: true
        preserve_host: false
    plugins:
      - name: rate-limiting
        config:
          minute: 100
          policy: redis
          redis_host: redis
          redis_port: 6379
      - name: jwt
        config:
          claims_to_verify:
            - exp
      - name: correlation-id
        config:
          header_name: X-Request-ID
          generator: uuid#counter

upstreams:
  - name: user-upstream
    algorithm: round-robin
    healthchecks:
      active:
        http_path: /actuator/health
        healthy:
          interval: 5
          successes: 2
        unhealthy:
          interval: 5
          http_failures: 3
    targets:
      - target: user-service-1:8080
        weight: 100
      - target: user-service-2:8080
        weight: 100

plugins:
  - name: prometheus
    config:
      per_consumer: true
      status_code_metrics: true
      latency_metrics: true
  - name: http-log
    config:
      http_endpoint: http://logstash:5044
      method: POST
      content_type: application/json
      flush_timeout: 2
```

---

## 12. 總結與學習路線建議

### 12.1 適合新手的學習順序

```mermaid
graph TD
    A[1. 理解 API Gateway 概念] --> B[2. 本機安裝 Kong]
    B --> C[3. 建立 Service + Route]
    C --> D[4. 學習核心 Plugin<br/>Key Auth, Rate Limiting]
    D --> E[5. 理解 Consumer 概念]
    E --> F[6. 學習進階 Plugin<br/>JWT, ACL, Transformer]
    F --> G[7. 監控與日誌整合]
    G --> H[8. 生產環境部署]
    H --> I[9. 維運與升級]
```

### 12.2 團隊導入 Kong 的成熟度成長路線

| 階段 | 特徵 | 目標 |
|-----|------|------|
| **Level 1: 入門** | 單一服務使用、基本路由 | 理解概念、完成 POC |
| **Level 2: 基礎** | 多服務管理、基本認證限流 | 穩定運行、基本監控 |
| **Level 3: 進階** | GitOps 管理、完整可觀測性 | 自動化部署、完整監控告警 |
| **Level 4: 成熟** | 多環境管理、HA 架構 | 零停機升級、災難復原 |
| **Level 5: 專家** | 自訂 Plugin、深度整合 | 效能調優、安全加固 |

### 12.3 推薦學習資源

| 資源 | 連結 |
|-----|------|
| Kong 官方文件 | https://docs.konghq.com |
| Kong 官方部落格 | https://konghq.com/blog |
| Kong GitHub | https://github.com/Kong/kong |
| decK 文件 | https://docs.konghq.com/deck |
| Kong Plugin Hub | https://docs.konghq.com/hub |

---

## 13. 檢查清單（Checklist）

### 🚀 新服務上線檢查清單

```markdown
## 新服務上線到 Kong 檢查清單

### 前置準備
- [ ] 後端服務已部署並可存取
- [ ] 後端服務有健康檢查端點
- [ ] 已確認 API 規格（Path、Method、認證方式）
- [ ] 已確認限流需求

### Kong 設定
- [ ] 建立 Service（設定正確的 URL/Upstream）
- [ ] 建立 Route（設定正確的 Path、Host、Method）
- [ ] 設定 Health Check（如使用 Upstream）
- [ ] 設定認證 Plugin（Key Auth / JWT）
- [ ] 設定 Rate Limiting
- [ ] 設定 CORS（如需要）
- [ ] 設定 Logging

### 測試驗證
- [ ] 測試正常請求是否成功
- [ ] 測試認證失敗情況
- [ ] 測試限流觸發情況
- [ ] 測試後端服務不可用情況
- [ ] 確認 Metrics 有收集到
- [ ] 確認 Log 有輸出

### 文件更新
- [ ] 更新 API 文件
- [ ] 更新 kong.yaml 設定檔
- [ ] 通知相關團隊
```

### 🔧 日常維運檢查清單

```markdown
## Kong 日常維運檢查清單

### 每日檢查
- [ ] 檢查 Kong 節點健康狀態
- [ ] 檢查 5xx 錯誤率
- [ ] 檢查 P99 延遲
- [ ] 檢查 Upstream 健康狀態

### 每週檢查
- [ ] 檢查磁碟空間（Log）
- [ ] 檢查 Rate Limiting 觸發統計
- [ ] 檢查 Consumer 使用狀況
- [ ] 備份設定：`deck dump`

### 每月檢查
- [ ] 檢查是否有新版本
- [ ] 檢視 Plugin 使用狀況
- [ ] 檢視安全性公告
- [ ] 容量規劃檢討
```

### 📋 升級前檢查清單

```markdown
## Kong 升級前檢查清單

### 準備階段
- [ ] 確認當前版本
- [ ] 閱讀目標版本 Release Notes
- [ ] 確認 Breaking Changes
- [ ] 確認 PostgreSQL 版本相容性
- [ ] 確認所有 Plugin 相容性
- [ ] 備份設定：`deck dump -o backup.yaml`
- [ ] 備份資料庫

### 測試階段
- [ ] 在測試環境升級
- [ ] 執行功能測試
- [ ] 執行效能測試
- [ ] 驗證所有 Plugin 正常

### 執行階段
- [ ] 選擇低峰時段
- [ ] 通知相關團隊
- [ ] 準備 Rollback 計畫
- [ ] 執行滾動升級
- [ ] 監控錯誤率與延遲

### 驗證階段
- [ ] 確認所有節點版本一致
- [ ] 確認健康檢查正常
- [ ] 確認 Metrics 正常
- [ ] 確認 Log 無異常
- [ ] 執行 Smoke Test
```

### 🔒 安全性檢查清單

```markdown
## Kong 安全性檢查清單

### 網路安全
- [ ] Admin API 限制內網存取
- [ ] Proxy 使用 HTTPS
- [ ] 設定 TLS 1.2+
- [ ] 關閉不必要的端口

### 認證授權
- [ ] 所有 API 都有認證
- [ ] 使用強密碼/複雜 Key
- [ ] JWT 使用 RS256
- [ ] 設定 Token 過期時間

### 存取控制
- [ ] 設定合理的 Rate Limiting
- [ ] 設定 ACL 權限
- [ ] 限制 CORS Origin

### 日誌與監控
- [ ] 啟用存取日誌
- [ ] 啟用錯誤日誌
- [ ] 設定異常告警
- [ ] 定期檢視安全日誌
```

---

## 14. 附錄

### A. 常用指令速查表

```bash
# ===== 查詢指令 =====
# 查詢 Kong 版本
curl -s localhost:8001 | jq '.version'

# 查詢所有 Services
curl -s localhost:8001/services | jq

# 查詢所有 Routes
curl -s localhost:8001/routes | jq

# 查詢所有 Plugins
curl -s localhost:8001/plugins | jq

# 查詢所有 Consumers
curl -s localhost:8001/consumers | jq

# 查詢 Upstream 健康狀態
curl -s localhost:8001/upstreams/{upstream}/health | jq

# 查詢 Kong 狀態
curl -s localhost:8001/status | jq

# ===== 建立指令 =====
# 建立 Service
curl -X POST localhost:8001/services \
  --data name=my-service \
  --data url=http://backend:8080

# 建立 Route
curl -X POST localhost:8001/services/my-service/routes \
  --data name=my-route \
  --data "paths[]=/api"

# 建立 Consumer
curl -X POST localhost:8001/consumers \
  --data username=my-consumer

# 啟用 Plugin
curl -X POST localhost:8001/services/my-service/plugins \
  --data name=rate-limiting \
  --data config.minute=100

# ===== 刪除指令 =====
# 刪除 Service
curl -X DELETE localhost:8001/services/my-service

# 刪除 Route
curl -X DELETE localhost:8001/routes/my-route

# 刪除 Plugin
curl -X DELETE localhost:8001/plugins/{plugin-id}

# ===== decK 指令 =====
# 匯出設定
deck dump -o kong.yaml

# 比較差異
deck diff -s kong.yaml

# 同步設定
deck sync -s kong.yaml

# 驗證設定
deck validate -s kong.yaml
```

### B. 環境變數參考

| 變數 | 說明 | 預設值 |
|-----|------|-------|
| `KONG_DATABASE` | 資料庫類型 | postgres |
| `KONG_PG_HOST` | PostgreSQL 主機 | 127.0.0.1 |
| `KONG_PG_PORT` | PostgreSQL 埠號 | 5432 |
| `KONG_PG_USER` | PostgreSQL 使用者 | kong |
| `KONG_PG_PASSWORD` | PostgreSQL 密碼 | - |
| `KONG_PG_DATABASE` | 資料庫名稱 | kong |
| `KONG_PROXY_LISTEN` | Proxy 監聽地址 | 0.0.0.0:8000, 0.0.0.0:8443 ssl |
| `KONG_ADMIN_LISTEN` | Admin API 監聽地址 | 127.0.0.1:8001 |
| `KONG_DECLARATIVE_CONFIG` | DB-less 設定檔路徑 | - |
| `KONG_LOG_LEVEL` | 日誌等級 | notice |
| `KONG_PROXY_ACCESS_LOG` | Proxy 存取日誌路徑 | /dev/stdout |
| `KONG_PROXY_ERROR_LOG` | Proxy 錯誤日誌路徑 | /dev/stderr |

---

> 📝 **文件維護說明**
> - 本文件應隨 Kong 版本更新而更新
> - 如有問題或建議，請聯繫平台團隊
> - 最後更新：2026 年 1 月

