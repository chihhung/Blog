---
title: "版本發行說明範本（Release Notes Template）"
date: 2026-05-18
draft: false
categories: ["教學"]
tags: ["部署運維", "範本", "軟體工程", "版本管理"]
---

# 版本發行說明範本（Release Notes）

> **參照標準**：Keep a Changelog 1.1.0 / SemVer 2.0.0 / ISO/IEC/IEEE 12207:2017（Release Management）  
> **文件用途**：正式記錄每個版本的變更內容，供開發、維運、使用者了解版本差異  
> **適用階段**：部署上線階段（Deployment Phase）— Release Management

---

## 📋 章節目錄

1. [文件資訊](#1-文件資訊)
2. [版本摘要](#2-版本摘要)
3. [新增功能（Added）](#3-新增功能added)
4. [變更項目（Changed）](#4-變更項目changed)
5. [修復項目（Fixed）](#5-修復項目fixed)
6. [棄用項目（Deprecated）](#6-棄用項目deprecated)
7. [移除項目（Removed）](#7-移除項目removed)
8. [安全性修復（Security）](#8-安全性修復security)
9. [已知問題（Known Issues）](#9-已知問題known-issues)
10. [升級指南](#10-升級指南)
11. [相容性說明](#11-相容性說明)

---

## 1. 文件資訊

### 📝 範本

| 項目 | 內容 |
|------|------|
| **產品名稱** | {系統名稱} |
| **版本號** | v{MAJOR}.{MINOR}.{PATCH} |
| **發佈日期** | {YYYY-MM-DD} |
| **版本類型** | Major / Minor / Patch / Hotfix |
| **發佈人** | {Release Manager 姓名} |
| **Git Tag** | {tag name} |
| **Build Number** | #{build} |
| **對應里程碑** | {Sprint/Milestone 名稱} |

### 📖 使用說明

- 版本號遵循 SemVer 2.0.0：
  - **MAJOR**：不相容的 API 變更
  - **MINOR**：向後相容的新功能
  - **PATCH**：向後相容的 Bug 修復
- 每次正式發佈（含 Hotfix）都需要 Release Notes
- Git Tag 與 Build Number 確保可從 Release Notes 追溯到原始碼

### 💡 範例

| 項目 | 內容 |
|------|------|
| **產品名稱** | 人力資源管理系統（HRMS） |
| **版本號** | v2.1.0 |
| **發佈日期** | 2026-05-20 |
| **版本類型** | Minor |
| **發佈人** | 林 DevOps |
| **Git Tag** | v2.1.0 |
| **Build Number** | #489 |
| **對應里程碑** | Sprint 12 |

---

## 2. 版本摘要

### 📝 範本

#### 概述

{用 2-3 句話描述本版本的核心主題與重要變更}

#### 重點亮點

- 🎯 {亮點 1}
- 🎯 {亮點 2}
- 🎯 {亮點 3}

#### 影響範圍

| 影響對象 | 說明 |
|---------|------|
| 前端使用者 | {影響描述} |
| API 消費者 | {影響描述} |
| 維運人員 | {影響描述} |
| 資料庫 | {是否有 Migration} |

### 📖 使用說明

- 版本摘要讓讀者快速了解「這個版本主要做了什麼」
- 重點亮點不超過 5 項，只列最重要的
- 影響範圍協助不同角色判斷是否需要閱讀詳細內容

### 💡 範例

#### 概述

v2.1.0 新增薪資計算自動化排程、請假流程行動推播通知，並修復 4 個已知缺陷。效能優化使報表匯出速度提升 40%。

#### 重點亮點

- 🎯 薪資計算支援自動化月結排程（cron-based）
- 🎯 請假審核結果即時推播通知（WebSocket）
- 🎯 報表匯出效能優化（非同步 + 分頁）
- 🎯 安全性更新：JWT Token 改用 RS256 簽章

#### 影響範圍

| 影響對象 | 說明 |
|---------|------|
| 前端使用者 | 新增推播通知功能；報表匯出 UI 變更（非同步下載） |
| API 消費者 | 新增 2 個 API 端點；1 個端點回傳格式變更（向後相容） |
| 維運人員 | 新增 CronJob 設定；WebSocket 服務需部署 |
| 資料庫 | 有 Migration：新增 notification_logs 表 |

---

## 3. 新增功能（Added）

### 📝 範本

| 功能 ID | 功能描述 | 對應需求 | 影響模組 |
|---------|---------|---------|---------|
| FEAT-{xxx} | {新功能描述} | {需求/User Story ID} | {模組} |

### 📖 使用說明

- 列出所有本版新增的功能（使用者可感知的）
- 功能 ID 連結到需求管理工具（如 Azure DevOps Work Item）
- 依優先級或模組排序

### 💡 範例

| 功能 ID | 功能描述 | 對應需求 | 影響模組 |
|---------|---------|---------|---------|
| FEAT-201 | 薪資計算自動化月結排程（每月 25 日 02:00 執行） | US-089 | Payroll |
| FEAT-202 | 請假審核結果 WebSocket 即時推播通知 | US-092 | Leave, Notification |
| FEAT-203 | 報表匯出改為非同步處理（支援大量資料） | US-095 | Report |
| FEAT-204 | 員工自助查詢薪資條歷史（最近 12 個月） | US-088 | Payroll, Employee |
| FEAT-205 | 系統管理員可設定全域假期日曆 | US-097 | Leave, Admin |

---

## 4. 變更項目（Changed）

### 📝 範本

| 變更 ID | 變更描述 | 影響範圍 | 向後相容 |
|---------|---------|---------|---------|
| CHG-{xxx} | {變更描述} | {影響模組/API} | 是/否 |

### 📖 使用說明

- 列出行為變更但非新功能的項目
- 「向後相容」欄位特別重要 — 不相容變更需在升級指南說明
- 常見變更：API 回傳格式調整、預設值變更、流程調整

### 💡 範例

| 變更 ID | 變更描述 | 影響範圍 | 向後相容 |
|---------|---------|---------|---------|
| CHG-101 | JWT Token 簽章演算法從 HS256 改為 RS256 | Auth API | 是（舊 Token 過期前仍有效） |
| CHG-102 | 報表匯出 API 回傳改為非同步（回傳 Job ID） | Report API | 否（需更新前端呼叫方式） |
| CHG-103 | 密碼過期天數從 180 天縮短為 90 天 | Auth | 是 |
| CHG-104 | 預設分頁筆數從 50 調整為 20 | 全部 List API | 是 |

---

## 5. 修復項目（Fixed）

### 📝 範本

| 缺陷 ID | 修復描述 | 嚴重度 | 影響模組 |
|---------|---------|--------|---------|
| BUG-{xxx} | {修復描述} | Critical/High/Medium/Low | {模組} |

### 📖 使用說明

- 列出本版修復的所有缺陷
- 嚴重度標示讓使用者判斷是否影響其使用情境
- Critical/High 缺陷建議在描述中加註影響範圍

### 💡 範例

| 缺陷 ID | 修復描述 | 嚴重度 | 影響模組 |
|---------|---------|--------|---------|
| BUG-138 | 薪資計算：加班費未計入勞健保基數 | High | Payroll |
| BUG-141 | 請假：跨年度特休計算日期邊界錯誤 | High | Leave |
| BUG-145 | 報表 PDF 頁首日期格式顯示為 UTC 非本地時間 | Medium | Report |
| BUG-148 | 員工姓名超過 50 字元 UI 截斷 | Low | Employee |

---

## 6. 棄用項目（Deprecated）

### 📝 範本

| 項目 | 棄用說明 | 替代方案 | 預計移除版本 |
|------|---------|---------|------------|
| {API/功能} | {棄用原因} | {替代} | v{x.x} |

### 📖 使用說明

- 標示未來將移除的功能/API，給使用者遷移時間
- 必須提供替代方案與預計移除版本
- 棄用不代表立即移除，通常保留 2-3 個 Minor 版本

### 💡 範例

| 項目 | 棄用說明 | 替代方案 | 預計移除版本 |
|------|---------|---------|------------|
| `GET /api/v1/employees/export` | 同步匯出效能不佳 | `POST /api/v2/reports/export-async` | v3.0.0 |
| `X-Auth-Token` Header | 改用標準 Bearer Token | `Authorization: Bearer {token}` | v3.0.0 |

---

## 7. 移除項目（Removed）

### 📝 範本

| 項目 | 移除說明 | 最後支援版本 | 遷移指南 |
|------|---------|------------|---------|
| {API/功能} | {移除原因} | v{x.x} | {遷移步驟/連結} |

### 📖 使用說明

- 列出本版正式移除的功能（之前標示為 Deprecated 的）
- 必須標明最後支援版本，供尚未遷移的使用者參考
- 提供具體遷移指南或連結

### 💡 範例

| 項目 | 移除說明 | 最後支援版本 | 遷移指南 |
|------|---------|------------|---------|
| Legacy XML Report API | 已由 JSON API 完全取代 | v1.9.0 | 參見 Migration Guide v2.0 |

---

## 8. 安全性修復（Security）

### 📝 範本

| 修復 ID | 描述 | CVE/CWE | 嚴重度 | CVSS |
|---------|------|---------|--------|------|
| SEC-FIX-{xxx} | {安全修復描述} | {CVE/CWE 編號} | Critical/High/Medium | {分數} |

### 📖 使用說明

- 安全性修復獨立列出，方便資安團隊追蹤
- 揭露程度視情況：內部已修復可詳述；若有公開 CVE 則引用
- 建議所有使用者盡速升級至包含安全修復的版本

### 💡 範例

| 修復 ID | 描述 | CVE/CWE | 嚴重度 | CVSS |
|---------|------|---------|--------|------|
| SEC-FIX-001 | JWT 改用 RS256 防止 Secret 洩露偽造 | CWE-347 | High | 7.5 |
| SEC-FIX-002 | 修復報表匯出 API 未檢查使用者權限（IDOR） | CWE-639 | High | 8.1 |
| SEC-FIX-003 | 更新 Newtonsoft.Json 至 13.0.3（CVE-2024-21907） | CVE-2024-21907 | Medium | 5.3 |

---

## 9. 已知問題（Known Issues）

### 📝 範本

| 問題 ID | 描述 | 影響 | 暫時方案 | 預計修復版本 |
|---------|------|------|---------|------------|
| KI-{xxx} | {已知問題描述} | {影響範圍} | {Workaround} | v{x.x.x} |

### 📖 使用說明

- 已知問題是此版本存在但尚未修復的限制或缺陷
- 必須提供暫時方案（Workaround）讓使用者應對
- 透明揭露建立使用者信任

### 💡 範例

| 問題 ID | 描述 | 影響 | 暫時方案 | 預計修復版本 |
|---------|------|------|---------|------------|
| KI-001 | Excel 匯出超過 5,000 筆可能逾時 | 大量資料匯出 | 分批匯出（每次 ≤ 3,000 筆） | v2.2.0 |
| KI-002 | Safari 瀏覽器日期選擇器偶有顯示異常 | Safari 使用者 | 使用 Chrome/Edge | v2.1.1 |

---

## 10. 升級指南

### 📝 範本

#### 10.1 前置條件

- {前置條件 1}
- {前置條件 2}

#### 10.2 升級步驟

1. {步驟 1}
2. {步驟 2}
3. {步驟 3}

#### 10.3 資料庫 Migration

```sql
-- Migration 名稱：{名稱}
-- 說明：{Migration 描述}
{SQL 示意}
```

#### 10.4 組態變更

| 組態項目 | 舊值 | 新值 | 說明 |
|---------|------|------|------|
| {key} | {old} | {new} | {原因} |

### 📖 使用說明

- 升級指南提供維運人員明確的升級步驟
- 若為 Minor/Patch 版本且無 Breaking Change，可標註「無需特殊升級步驟」
- 資料庫 Migration 需標示是否可回滾

### 💡 範例

#### 10.1 前置條件

- 確認目前版本為 v2.0.x（不支援從 v1.x 直接升級）
- 備份資料庫
- 確認 WebSocket 相關 Port (8080) 已開通

#### 10.2 升級步驟

1. 停止排程任務（避免薪資計算衝突）
2. 執行資料庫 Migration：`dotnet ef database update`
3. 部署新版應用程式 Image：`hrms:v2.1.0`
4. 部署 Notification WebSocket Service
5. 更新 Kong 路由設定（新增 `/ws` 路由）
6. 設定薪資計算 CronJob：`0 2 25 * *`
7. 驗證健康檢查端點

#### 10.3 資料庫 Migration

```sql
-- Migration: AddNotificationLogs_20260518
-- 可回滾：是
CREATE TABLE notification_logs (
    id BIGSERIAL PRIMARY KEY,
    employee_id INT NOT NULL REFERENCES employees(id),
    type VARCHAR(50) NOT NULL,
    payload JSONB,
    sent_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    read_at TIMESTAMPTZ
);
CREATE INDEX idx_notification_employee ON notification_logs(employee_id, sent_at DESC);
```

#### 10.4 組態變更

| 組態項目 | 舊值 | 新值 | 說明 |
|---------|------|------|------|
| `JWT__Algorithm` | HS256 | RS256 | 安全性升級 |
| `JWT__PublicKeyPath` | (新增) | `/keys/jwt-public.pem` | RS256 公鑰路徑 |
| `Export__Mode` | sync | async | 報表匯出改非同步 |
| `Notification__WebSocketPort` | (新增) | 8080 | 推播服務 Port |

---

## 11. 相容性說明

### 📝 範本

| 相容性項目 | 支援版本/條件 |
|-----------|-------------|
| 瀏覽器 | {支援的瀏覽器版本} |
| 行動裝置 | {支援的 OS 版本} |
| API 版本 | {向後相容到哪個版本} |
| .NET Runtime | {所需版本} |
| 資料庫 | {支援的 DB 版本} |

### 📖 使用說明

- 明確列出本版本的支援環境與相容性限制
- API 向後相容性對 API 消費者特別重要
- 若有 Breaking Change，需在此明確標示

### 💡 範例

| 相容性項目 | 支援版本/條件 |
|-----------|-------------|
| 瀏覽器 | Chrome 100+、Edge 100+、Firefox 110+、Safari 16+ |
| API 版本 | v2 (current)、v1 (deprecated, 至 v3.0 移除) |
| .NET Runtime | .NET 8.0.4+ |
| PostgreSQL | 15.x / 16.x |
| Redis | 7.0+ |
| Kubernetes | 1.27+ |

---

> 📌 **範本使用注意事項**
> 1. 本範本依據 Keep a Changelog 1.1.0 與 SemVer 2.0.0 精神擴展，結合 ISO/IEC/IEEE 12207:2017 Release Management
> 2. 每次正式版本發佈（含 Hotfix）必須產出 Release Notes
> 3. 搭配「CHANGELOG 範本」使用 — CHANGELOG 是累計歷史，Release Notes 是單次詳細說明
> 4. 搭配「部署指引範本」使用 — 升級指南與部署步驟互補
> 5. Release Notes 需存放於版本控制中，與對應 Git Tag 關聯
