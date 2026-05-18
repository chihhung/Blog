---
title: "非功能性需求設計規格範本（NFR Design Specification Template）"
date: 2026-05-18
draft: false
categories: ["教學"]
tags: ["範本", "設計開發", "NFR", "效能", "可用性", "SSDLC"]
---

# 非功能性需求設計規格範本（NFR Design Specification Template）

> **適用標準**：ISO/IEC 25010:2023（SQuaRE - 系統與軟體品質模型）、ISO/IEC/IEEE 29148:2018  
> **適用階段**：系統設計階段（Design Phase）  
> **負責角色**：系統架構師（SA）、效能工程師、SRE

---

## 📑 章節目錄

1. [文件資訊](#1-文件資訊)
2. [品質屬性總覽](#2-品質屬性總覽)
3. [效能設計（Performance）](#3-效能設計performance)
4. [可用性設計（Availability）](#4-可用性設計availability)
5. [延展性設計（Scalability）](#5-延展性設計scalability)
6. [可靠性設計（Reliability）](#6-可靠性設計reliability)
7. [可維護性設計（Maintainability）](#7-可維護性設計maintainability)
8. [可觀測性設計（Observability）](#8-可觀測性設計observability)
9. [安全性設計（Security）](#9-安全性設計security)
10. [相容性設計（Compatibility）](#10-相容性設計compatibility)
11. [驗證與測試策略](#11-驗證與測試策略)

---

## 📝 範本

---

### 1. 文件資訊

| 項目 | 內容 |
|------|------|
| **文件名稱** | [系統名稱] 非功能性需求設計規格 |
| **文件編號** | [專案代碼]-NFR-[版本號] |
| **版本** | v[X.Y] |
| **建立日期** | [YYYY-MM-DD] |
| **撰寫者** | [SA 姓名] |
| **審核者** | [技術主管] |

---

### 2. 品質屬性總覽

> 依 ISO/IEC 25010:2023 品質模型分類

| 品質屬性 | 子特性 | 目標等級 | 優先級 | 驗證方式 |
|---------|--------|---------|--------|---------|
| 效能效率 | 時間行為、資源利用、容量 | [目標] | [High/Med/Low] | [效能測試] |
| 可用性 | 成熟度、容錯性、可恢復性 | [目標] | [High/Med/Low] | [HA 測試] |
| 延展性 | 水平/垂直擴展能力 | [目標] | [High/Med/Low] | [負載測試] |
| 可靠性 | 容錯、一致性 | [目標] | [High/Med/Low] | [Chaos 測試] |
| 可維護性 | 模組化、可測試性、可修改性 | [目標] | [High/Med/Low] | [Code Review] |
| 安全性 | 機密性、完整性、可用性 | [目標] | [High/Med/Low] | [安全測試] |
| 相容性 | 瀏覽器、裝置、整合 | [目標] | [High/Med/Low] | [相容測試] |

---

### 3. 效能設計（Performance）

#### 3.1 效能目標

| 指標 | 日常目標 | 尖峰目標 | 測量方式 |
|------|---------|---------|---------|
| 回應時間（P50） | < [N]ms | < [N]ms | APM / Load test |
| 回應時間（P95） | < [N]ms | < [N]ms | APM / Load test |
| 回應時間（P99） | < [N]ms | < [N]ms | APM / Load test |
| 吞吐量（TPS） | ≥ [N] | ≥ [N] | Load test |
| 並發用戶 | [N] | [N] | Load test |
| 錯誤率 | < [N]% | < [N]% | Monitoring |

#### 3.2 效能設計策略

| 策略 | 適用場景 | 設計方案 |
|------|---------|---------|
| 快取 | [高頻讀取、低頻更新] | [快取層級/策略/TTL] |
| 非同步處理 | [非即時、耗時任務] | [Message Queue + Worker] |
| 連接池 | [DB/HTTP 連線] | [Pool size + timeout 設定] |
| 分頁查詢 | [大量資料列表] | [Cursor-based / Offset pagination] |
| 批次處理 | [大量寫入] | [Batch size + 排程策略] |
| CDN | [靜態資源] | [CDN provider + cache policy] |

#### 3.3 效能預算（Performance Budget）

| 資源 | 預算 | 目前值 | 狀態 |
|------|------|--------|------|
| 首頁載入（FCP） | < [N]s | [N]s | [✅/⚠️/❌] |
| 最大內容繪製（LCP） | < [N]s | [N]s | [✅/⚠️/❌] |
| 累計版面偏移（CLS） | < [N] | [N] | [✅/⚠️/❌] |
| 互動至下一次繪製（INP） | < [N]ms | [N]ms | [✅/⚠️/❌] |
| JS Bundle Size | < [N]KB | [N]KB | [✅/⚠️/❌] |
| API Response Size | < [N]KB (avg) | [N]KB | [✅/⚠️/❌] |

---

### 4. 可用性設計（Availability）

#### 4.1 SLA 定義

| 服務 | SLA 目標 | 允許停機/月 | 計算方式 |
|------|---------|-----------|---------|
| [核心服務] | [99.9%] | [~43.8 min] | Uptime / Total time |
| [次要服務] | [99.5%] | [~3.6 hr] | |
| [背景服務] | [99.0%] | [~7.3 hr] | |

#### 4.2 高可用設計

| 元件 | HA 模式 | Failover 時間 | 健康檢查 |
|------|---------|-------------|---------|
| [元件] | [Active-Active / Active-Passive / N+1] | [N]s | [HTTP/TCP/Custom] |

#### 4.3 停機策略

| 停機類型 | 通知時間 | 持續時間 | 影響範圍 | 核准 |
|---------|---------|---------|---------|------|
| 計畫性維護 | [N 天前] | [N hr] | [描述] | [PM/業務] |
| 緊急修復 | [即時] | [N hr] | [描述] | [Tech Lead] |

---

### 5. 延展性設計（Scalability）

#### 5.1 擴展策略

| 維度 | 策略 | 設計 |
|------|------|------|
| 水平擴展（Scale-Out） | [無狀態 + Load Balancer] | [Auto-scaling rules] |
| 垂直擴展（Scale-Up） | [資料庫 / 特殊運算] | [上限與遷移計畫] |
| 資料擴展 | [分區 / Sharding] | [分區策略] |

#### 5.2 容量規劃

| 時間軸 | 預估用戶 | 預估資料量 | 預估 TPS | 對應架構 |
|--------|---------|-----------|---------|---------|
| 上線 | [N] | [N] GB | [N] | [架構描述] |
| 6 個月 | [N] | [N] GB | [N] | [是否需擴展] |
| 1 年 | [N] | [N] GB | [N] | [擴展方案] |
| 3 年 | [N] | [N] GB | [N] | [重大架構變更?] |

---

### 6. 可靠性設計（Reliability）

#### 6.1 容錯設計

| 故障場景 | 影響 | 容錯機制 | 降級方案 |
|---------|------|---------|---------|
| [單節點故障] | [描述] | [自動 failover] | [N/A] |
| [DB 連線失敗] | [描述] | [Circuit Breaker] | [顯示快取資料] |
| [外部 API 超時] | [描述] | [Retry + Timeout] | [預設值/離線模式] |
| [整個 AZ 故障] | [描述] | [Multi-AZ 部署] | [部分功能降級] |

#### 6.2 Circuit Breaker 設計

| 服務 | Open 條件 | Half-Open 條件 | Close 條件 | Fallback |
|------|-----------|---------------|-----------|---------|
| [服務] | [N 次失敗 in M 秒] | [N 秒後] | [N 次成功] | [降級方案] |

#### 6.3 Retry 策略

| 場景 | 最大重試 | 退避策略 | 可重試條件 |
|------|---------|---------|-----------|
| [HTTP call] | [N] 次 | [Exponential backoff + jitter] | [5xx, timeout, network error] |
| [DB operation] | [N] 次 | [Fixed interval] | [Deadlock, connection lost] |

---

### 7. 可維護性設計（Maintainability）

| 品質指標 | 目標 | 度量方式 |
|---------|------|---------|
| 程式碼覆蓋率 | ≥ [N]% | [CI/CD report] |
| 技術債指標 | [SQALE ≤ N days] | [SonarQube] |
| 模組耦合度 | [低耦合] | [Architecture fitness test] |
| 部署頻率 | [≥ N 次/週] | [CI/CD metrics] |
| 修復前置時間 | [< N hr] | [DORA metrics] |

---

### 8. 可觀測性設計（Observability）

#### 8.1 三大支柱

| 支柱 | 工具 | 設計 |
|------|------|------|
| Metrics | [Prometheus / CloudWatch] | [RED + USE metrics] |
| Logging | [ELK / Loki] | [Structured JSON, correlation ID] |
| Tracing | [Jaeger / Zipkin / OTEL] | [Distributed tracing, 100% sampling for errors] |

#### 8.2 SLI/SLO 定義

| SLI（指標） | SLO（目標） | 計算方式 | 告警閾值 |
|------------|-----------|---------|---------|
| Availability | [99.9%] | successful requests / total requests | < 99.8% → Warning |
| Latency (P95) | [< 200ms] | histogram_quantile(0.95) | > 300ms → Warning |
| Error Rate | [< 0.1%] | 5xx / total requests | > 1% → Critical |
| Throughput | [≥ N TPS] | rate(requests_total[5m]) | < N*0.7 → Warning |

---

### 9. 安全性設計（Security）

> 詳見安全設計文件（SecurityDesign_Template.md），此處僅摘要 NFR 指標

| 安全指標 | 目標 | 驗證方式 |
|---------|------|---------|
| 漏洞修復 SLA（Critical） | [< 24 hr] | [弱點管理系統] |
| 漏洞修復 SLA（High） | [< 7 days] | [弱點管理系統] |
| 第三方套件更新 | [< 30 days after patch] | [SCA 工具] |
| 安全事件回應時間 | [< 1 hr] | [SIEM 告警] |

---

### 10. 相容性設計（Compatibility）

#### 10.1 瀏覽器支援

| 瀏覽器 | 版本 | 支援等級 |
|--------|------|---------|
| Chrome | Latest 2 versions | Full |
| Firefox | Latest 2 versions | Full |
| Safari | Latest 2 versions | Full |
| Edge | Latest 2 versions | Full |
| IE | — | Not supported |

#### 10.2 裝置支援

| 裝置類型 | 解析度範圍 | 支援等級 |
|---------|-----------|---------|
| Desktop | ≥ 1280px | Full |
| Tablet | 768px – 1279px | Full |
| Mobile | 320px – 767px | [Full / Partial] |

---

### 11. 驗證與測試策略

| NFR 類別 | 測試類型 | 工具 | 頻率 | Pass 準則 |
|---------|---------|------|------|----------|
| 效能 | 負載測試 | [JMeter / k6 / Locust] | [Sprint / Release] | [滿足 §3 指標] |
| 效能 | 壓力測試 | [同上] | [Release] | [系統優雅降級] |
| 可用性 | Failover 測試 | [Chaos Engineering] | [每月] | [RTO 內恢復] |
| 延展性 | 彈性測試 | [Auto-scale + Load] | [Release] | [自動擴展正常] |
| 安全 | 滲透測試 | [外部廠商] | [每年] | [無 Critical/High] |
| 相容性 | 跨瀏覽器測試 | [BrowserStack / Playwright] | [Sprint] | [所有支援的瀏覽器通過] |

---

## 📖 使用說明

### 各章節填寫指引

| 章節 | 填寫時機 | 負責人 | 重點說明 |
|------|---------|--------|---------|
| §2 品質總覽 | 需求確認後 | SA/PM | 與業務確認優先級 |
| §3 效能 | 設計階段 | SA/效能工程師 | 指標需可量測、可驗證 |
| §4 可用性 | 設計階段 | SA/SRE | SLA 需業務簽核 |
| §5 延展性 | 設計階段 | SA | 含成長預估 |
| §6 可靠性 | 設計階段 | SA | 定義降級方案 |
| §7 可維護性 | 開發啟動時 | Tech Lead | 定義品質門檻 |
| §8 可觀測性 | 設計/部署前 | SRE | SLI/SLO 需量化 |
| §11 測試策略 | 測試規劃時 | QA/SA | 每項 NFR 需有驗證方式 |

### NFR 撰寫原則（SMART）

- **S**pecific：明確指定指標和數值
- **M**easurable：可量測（有工具可度量）
- **A**chievable：可達成（技術可行）
- **R**elevant：與業務相關
- **T**ime-bound：有時間範圍（尖峰/日常）

---

## 💡 範例（以 HRMS 人力資源管理系統為例）

---

### 範例：效能目標

| 指標 | 日常 | 尖峰（月初薪資結算） | 測量 |
|------|------|-------------------|------|
| P50 回應時間 | < 100ms | < 150ms | Application Insights |
| P95 回應時間 | < 200ms | < 400ms | Application Insights |
| P99 回應時間 | < 500ms | < 1000ms | Application Insights |
| TPS | ≥ 500 | ≥ 1500 | k6 load test |
| 並發用戶 | 2,000 | 5,000 | k6 load test |
| API 錯誤率 | < 0.1% | < 0.5% | Prometheus |

### 範例：快取策略

| 資源 | 快取層 | 策略 | TTL | 失效方式 |
|------|--------|------|-----|---------|
| 員工基本資料 | Redis L2 | Cache-Aside | 30 min | Write-Through invalidation |
| 假別餘額 | Redis L2 | Cache-Aside | 5 min | Event-driven invalidation |
| 部門組織樹 | Redis L2 | Cache-Aside | 1 hr | Manual refresh |
| 靜態設定值 | Application L1 | Read-Through | 24 hr | Restart / Admin refresh |

### 範例：SLI/SLO

| SLI | SLO | Error Budget/月 | 告警 |
|-----|-----|----------------|------|
| API 可用性 | 99.9% | 43.8 min downtime | < 99.8% → P1 |
| 請假 API P95 延遲 | < 200ms | — | > 300ms for 5min → P2 |
| 薪資計算批次完成時間 | < 2 hr | — | > 1.5hr → P3 |
| 登入成功率 | > 99.5% | — | < 99% → P1 |

---

> 📌 **審閱重點**  
> - 每項 NFR 是否都有量化指標（非模糊描述）？  
> - 日常 vs 尖峰是否分別定義目標？  
> - 每項 NFR 是否都有對應的驗證/測試方式？  
> - SLI/SLO 是否與 SLA 對齊？  
> - 容量規劃是否考慮 3 年成長？
