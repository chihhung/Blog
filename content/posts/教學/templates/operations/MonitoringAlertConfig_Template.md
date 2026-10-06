---
title: "監控與告警設定文件範本（Monitoring & Alert Configuration Template）"
date: 2026-05-18
draft: false
categories: ["教學"]
tags: ["範本", "部署運維", "監控", "告警", "SRE", "Prometheus", "Grafana", "SSDLC"]
---

# 監控與告警設定文件範本（Monitoring & Alert Configuration Template）

> **適用標準**：Google SRE Workbook、ISO/IEC 20000-1:2018（Service Monitoring）
>
> **適用階段**：維運階段（Operations Phase）
>
> **負責角色**：SRE、DevOps Engineer、Tech Lead
>
> **範本版本**：v2.0（2026-10-06）｜對應《軟體開發標準程序教學手冊》v2.0 第 10.2 節

---

## 📑 章節目錄

1. [文件資訊](#1-文件資訊)
2. [監控策略概要](#2-監控策略概要)
3. [SLI / SLO 定義](#3-sli--slo-定義)
4. [監控指標設計](#4-監控指標設計)
5. [告警規則定義](#5-告警規則定義)
6. [Dashboard 設計](#6-dashboard-設計)
7. [告警通知與升級](#7-告警通知與升級)
8. [日誌監控策略](#8-日誌監控策略)
9. [維護與檢討機制](#9-維護與檢討機制)
10. [附錄](#10-附錄)
11. [審查與驗證](#11-審查與驗證)

---

## 📝 範本

---

### 1. 文件資訊

| 項目 | 內容 |
|------|------|
| **文件名稱** | [系統名稱] 監控與告警設定文件 |
| **文件編號** | [專案代碼]-MON-[版本號]-[日期] |
| **版本** | v[X.Y] |
| **建立日期** | [YYYY-MM-DD] |
| **負責人** | [SRE / DevOps] |
| **審核者** | [Tech Lead / SA] |

---

### 2. 監控策略概要

#### 2.1 監控架構

| 層級 | 工具 | 用途 |
|------|------|------|
| Infrastructure | [Prometheus / CloudWatch / Azure Monitor] | 主機/容器/網路 |
| Application | [APM: Datadog / New Relic / OpenTelemetry] | 應用效能 |
| Business | [Custom metrics / Analytics] | 業務指標 |
| Logging | [ELK / Loki / Azure Log Analytics] | 日誌分析 |
| Tracing | [Jaeger / Zipkin / OpenTelemetry] | 分散式追蹤 |

#### 2.2 監控原則

| 原則 | 說明 |
|------|------|
| Four Golden Signals | Latency, Traffic, Errors, Saturation |
| USE Method | Utilization, Saturation, Errors（基礎設施） |
| RED Method | Rate, Errors, Duration（服務） |
| Alerting Philosophy | Alert on symptoms, not causes |

---

### 3. SLI / SLO 定義

#### 3.1 服務層級指標（SLI）

| SLI | 定義 | 量測方式 | 資料來源 |
|-----|------|---------|---------|
| Availability | 成功回應比例 | success_requests / total_requests | [Load Balancer / App] |
| Latency | 回應時間分佈 | P50, P95, P99 | [APM / Prometheus histogram] |
| Throughput | 處理量 | Requests per second | [Metrics] |
| Error Rate | 錯誤回應比例 | 5xx_count / total_count | [Ingress / App] |

#### 3.2 服務層級目標（SLO）

| 服務 | SLO 指標 | 目標值 | Error Budget (月) | 量測視窗 |
|------|---------|--------|-------------------|---------|
| [API Service] | Availability | ≥ 99.9% | 43.2 min（30 天 × 0.1%） | 30 days rolling |
| [API Service] | P95 Latency | < [N]ms | — | 30 days rolling |
| [Web Frontend] | Availability | ≥ 99.5% | 3.6 hr | 30 days rolling |
| [Batch Job] | Success Rate | ≥ 99.0% | — | Per execution |

---

### 4. 監控指標設計

#### 4.1 基礎設施指標

以下為 Prometheus node_exporter 的實際指標名稱；使用率需以 PromQL 計算，不是直接輸出的指標：

| 指標名稱 | 類型 | 描述 | 使用率計算（PromQL） | 閾值 |
|---------|------|------|-------------------|------|
| node_cpu_seconds_total | Counter | 各 CPU 模式累計秒數 | `1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m]))` | warn: 80%, crit: 95% |
| node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes | Gauge | 可用／總記憶體 | `1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes` | warn: 85%, crit: 95% |
| node_filesystem_avail_bytes / node_filesystem_size_bytes | Gauge | 可用／總磁碟空間 | `1 - node_filesystem_avail_bytes / node_filesystem_size_bytes` | warn: 80%, crit: 90% |
| node_network_receive_errs_total | Counter | 網路接收錯誤數 | `rate(node_network_receive_errs_total[5m])` | crit: > [N]/s |

#### 4.2 應用程式指標

指標名稱**必須**依實際的 instrumentation 填寫，並在 Prometheus 查詢介面確認查得到資料。下表為 Spring Boot（Micrometer）的預設名稱；OpenTelemetry 語意慣例為 `http_server_request_duration_seconds_*`，其他框架請以實際輸出為準：

| 指標名稱 | 類型 | 描述 | 標籤 | 閾值 |
|---------|------|------|------|------|
| http_server_requests_seconds_count | Counter | HTTP 請求總數 | method, uri, status, outcome | — |
| http_server_requests_seconds_bucket | Histogram | 請求處理時間（需啟用 `management.metrics.distribution.percentiles-histogram.http.server.requests=true`） | method, uri, status, le | P95 < [N]s |
| hikaricp_connections_active / hikaricp_connections_max | Gauge | DB 連線池使用數／上限 | pool | warn: 80%, crit: 95% |
| jvm_memory_used_bytes | Gauge | JVM 記憶體使用量 | area, id | warn: 85% of max |
| [queue]_depth | Gauge | 訊息佇列深度（依 MQ exporter 名稱） | queue_name | warn: [N], crit: [N] |

#### 4.3 業務指標

| 指標名稱 | 類型 | 描述 | 標籤 | 告警條件 |
|---------|------|------|------|---------|
| [business_metric_1] | Counter | [描述] | [labels] | [condition] |
| [business_metric_2] | Gauge | [描述] | [labels] | [condition] |

---

### 5. 告警規則定義

#### 5.1 告警嚴重度定義

| 嚴重度 | 定義 | 回應時間 | 通知方式 |
|--------|------|---------|---------|
| P1 - Critical | 服務完全中斷 / 資料遺失 | 5 分鐘 | PagerDuty + 電話 + SMS |
| P2 - High | 核心功能受損 / 效能嚴重惡化 | 15 分鐘 | PagerDuty + Teams |
| P3 - Medium | 非核心功能異常 / 效能下降 | 1 小時 | Teams Channel |
| P4 - Low | 預警 / 需關注但無立即影響 | 下個工作日 | Email / Ticket |

#### 5.2 告警規則清單

| Alert ID | 名稱 | 嚴重度 | 條件 | For | 說明 |
|---------|------|--------|------|-----|------|
| ALT-001 | ServiceDown | P1 | up == 0 | 1m | 服務實例離線 |
| ALT-002 | HighErrorRate | P1 | error_rate > 5% | 5m | 錯誤率過高 |
| ALT-003 | HighLatency | P2 | p95_latency > [N]ms | 5m | 回應時間過慢 |
| ALT-004 | HighCPU | P3 | cpu_usage > 80% | 10m | CPU 使用率高 |
| ALT-005 | DiskAlmostFull | P2 | disk_usage > 85% | 5m | 磁碟空間不足 |
| ALT-006 | DBConnectionPoolHigh | P2 | pool_usage > 80% | 5m | DB 連線池接近上限 |
| ALT-007 | CertExpiringSoon | P3 | cert_expiry < 30d | — | 憑證即將到期 |
| ALT-008 | ErrorBudgetFastBurn | P1 | 1h 與 5m 燃燒率皆 > 14.4 | 2m | 2 天內將耗盡 30 天錯誤預算 |
| ALT-009 | ErrorBudgetSlowBurn | P3 | 6h 與 30m 燃燒率皆 > 6 | 15m | 5 天內將耗盡 30 天錯誤預算 |

#### 5.3 告警規則範例（Prometheus Alerting Rules）

告警規則由 Prometheus 評估，觸發後送到 Alertmanager 進行分組、抑制與通知；每個規則檔上線前必須以 `promtool check rules` 檢查語法，並以 `promtool test rules` 驗證觸發邏輯。

```yaml
groups:
  - name: "[service_name].rules"
    rules:
      - alert: "[AlertName]"
        expr: "[PromQL expression]"
        for: "[duration，例 5m]"
        labels:
          severity: "[critical/warning/info]"
          team: "[team_name]"
          service: "[service_name]"
        annotations:
          summary: "[簡短摘要]"
          description: "[詳細描述，可含 {{ $labels }} 和 {{ $value }}]"
          runbook_url: "[Runbook 連結]"
          dashboard_url: "[Dashboard 連結]"
```

---

### 6. Dashboard 設計

#### 6.1 Dashboard 清單

| Dashboard | 用途 | 目標受眾 | 更新頻率 |
|-----------|------|---------|---------|
| Service Overview | 服務健康狀態總覽 | SRE / 管理層 | 10s |
| API Performance | API 效能細節 | SRE / Dev | 10s |
| Infrastructure | 基礎設施資源 | Infra / SRE | 30s |
| Business Metrics | 業務指標 | PM / PO | 1m |
| SLO Tracking | SLO 達成率與 Error Budget | SRE / 管理層 | 1m |

#### 6.2 Service Overview Dashboard 設計

| Panel | 視覺化類型 | 指標 | 說明 |
|-------|----------|------|------|
| Service Status | Stat (up/down) | up{service="..."} | 紅綠燈 |
| Request Rate | Time Series | sum(rate(http_server_requests_seconds_count[5m])) | QPS |
| Error Rate | Time Series | error_rate | 錯誤率趨勢 |
| P95 Latency | Time Series | histogram_quantile(0.95, ...) | 延遲趨勢 |
| Active Users | Stat | active_sessions | 當前活躍用戶 |
| SLO Status | Gauge | slo_compliance | SLO 達標率 |

---

### 7. 告警通知與升級

#### 7.1 通知路由

| 嚴重度 | 工作時間 (09-18) | 非工作時間 | 假日 |
|--------|-----------------|-----------|------|
| P1 | On-call + Team Lead (即時) | On-call + Backup (即時) | On-call + Manager (即時) |
| P2 | On-call (15 min) | On-call (30 min) | On-call (30 min) |
| P3 | Teams Channel | 下個工作日 | 下個工作日 |
| P4 | Email / Ticket | — | — |

#### 7.2 升級機制

| 時間 | 未回應動作 |
|------|-----------|
| T + 5 min | 重新通知 On-call |
| T + 15 min | 通知 Backup On-call |
| T + 30 min | 通知 Team Lead / Manager |
| T + 60 min | 通知 Director / VP |

#### 7.3 On-Call 輪值

| 週次 | Primary | Backup | 電話 |
|------|---------|--------|------|
| Week 1 | [姓名] | [姓名] | [電話] |
| Week 2 | [姓名] | [姓名] | [電話] |

---

### 8. 日誌監控策略

#### 8.1 日誌等級與保留

| Log Level | 用途 | 保留期間 | 告警 |
|-----------|------|---------|------|
| ERROR | 需處理的錯誤 | 90 days | rate > [N]/min → P2 |
| WARN | 潛在問題 | 30 days | rate > [N]/min → P3 |
| INFO | 正常營運記錄 | 14 days | — |
| DEBUG | 開發除錯用 | 3 days (STG only) | — |

#### 8.2 關鍵日誌監控

| # | 監控模式 | 觸發條件 | 告警 |
|---|---------|---------|------|
| 1 | Exception stack trace | rate > [N]/min | P2 |
| 2 | "OutOfMemoryError" | 出現 1 次 | P1 |
| 3 | "Connection refused" | rate > [N]/min | P2 |
| 4 | Authentication failure | rate > [N]/min | P2 (可能攻擊) |
| 5 | [自訂業務異常模式] | [條件] | [等級] |

---

### 9. 維護與檢討機制

| 項目 | 頻率 | 負責人 | 說明 |
|------|------|--------|------|
| Alert Noise 檢討 | 每月 | SRE | 刪除/調整誤報告警 |
| SLO 檢討 | 每季 | SRE + PO | 調整目標值 |
| Dashboard 更新 | 需求變動時 | SRE | 新增/移除指標 |
| Runbook 更新 | 每次事件後 | SRE | 補充處理步驟 |
| On-Call 回顧 | 每月 | SRE Team | 改善值班體驗 |

---

### 10. 附錄

#### 10.1 Prometheus／Alertmanager 設定檔位置

| 檔案 | 位置 | 說明 |
|------|------|------|
| alertmanager.yml | [path] | 通知路由設定 |
| prometheus-rules/ | [path] | 告警規則目錄 |
| grafana-dashboards/ | [path] | Dashboard JSON |

#### 10.2 相關文件

| 文件 | 連結 |
|------|------|
| Runbook | [link] |
| SOP | [link] |
| Incident Response Plan | [link] |

---

### 11. 審查與驗證

> 本節供審查者使用，也用來檢查 AI 依本範本產出的文件是否正確；對應《軟體開發標準程序教學手冊》v2.0 各章的「審查與驗證」。

#### 自動檢查

| 檢查項目 | 方法 |
|---------|------|
| 告警規則語法 | `promtool check rules`（v2.0 範例已通過，7 條規則） |
| 告警邏輯 | `promtool test rules` 以假資料驗證觸發與不觸發（v2.0 範例已實測） |
| 指標存在 | 在 Prometheus 查詢運算式（不含門檻），確認有回傳序列 |

#### 人工審查問題

1. 指標名稱是否與實際 instrumentation 相符？
2. SLO 錯誤預算是否以正確的時間視窗計算？
3. 每個告警是否有 Runbook 與處理動作？
4. 是否採多視窗燃燒率告警，而非單一門檻？

#### AI 常見錯誤

- 使用不存在的指標名稱（例如把 `http_requests_total` 套到 Spring Boot），告警永遠不觸發。
- 錯誤預算算錯（99.9%／30 天應為 43.2 分鐘）。
- YAML 佔位符未加引號，導致設定檔無法解析。

---

## 📖 使用說明

### 建立監控的優先順序

1. **Phase 1**：健康檢查 + 基本告警（Service Up/Down, Error Rate）
2. **Phase 2**：Golden Signals 完整覆蓋（Latency, Traffic, Errors, Saturation）
3. **Phase 3**：SLI/SLO 追蹤 + Error Budget
4. **Phase 4**：業務指標 + 進階分析

### 告警設計原則

| 原則 | 說明 |
|------|------|
| Alert on symptoms | 告警使用者可感知的症狀，非原因 |
| Actionable | 每個告警都必須有對應的處理動作 |
| Low noise | 避免無意義的告警（Alert fatigue） |
| Have a runbook | 每個告警必須連結到 Runbook |

---

## 💡 範例（以 HRMS 人力資源管理系統為例）

---

### 範例：SLI/SLO

| 服務 | SLI | SLO | Error Budget/月 |
|------|-----|-----|----------------|
| HRMS API | Availability | ≥ 99.9% | 43.2 min（30 天滾動視窗） |
| HRMS API | P95 Latency | < 200ms | — |
| 薪資批次作業 | Success Rate | 100%（每月執行 1 次，不容失敗） | 不適用：以執行次數計，失敗一次即為 P1 事件 |
| 出缺勤打卡 | Availability | ≥ 99.95%（工作日 07:00–21:00） | 約 9.2 min（22 個工作日 × 14 小時 × 0.05%） |

### 範例：告警規則

以下規則已以 `promtool check rules`（Prometheus 3.15.0）驗證語法，並以 `promtool test rules` 驗證：錯誤率 2% 時觸發 `HRMSErrorBudgetFastBurn`、0.5% 時不觸發。

```yaml
groups:
  - name: hrms-slo.rules
    rules:
      - record: job:http_server_requests:error_ratio_rate5m
        expr: |
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api",status=~"5.."}[5m]))
          /
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api"}[5m]))
      - record: job:http_server_requests:error_ratio_rate1h
        expr: |
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api",status=~"5.."}[1h]))
          /
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api"}[1h]))
      - record: job:http_server_requests:error_ratio_rate30m
        expr: |
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api",status=~"5.."}[30m]))
          /
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api"}[30m]))
      - record: job:http_server_requests:error_ratio_rate6h
        expr: |
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api",status=~"5.."}[6h]))
          /
          sum by (job) (rate(http_server_requests_seconds_count{job="hrms-api"}[6h]))

      # SLO 99.9%（錯誤預算 0.1%）：多視窗、多燃燒率告警
      - alert: HRMSErrorBudgetFastBurn
        expr: |
          job:http_server_requests:error_ratio_rate1h > (14.4 * 0.001)
          and
          job:http_server_requests:error_ratio_rate5m > (14.4 * 0.001)
        for: 2m
        labels:
          severity: critical
          team: hrms
        annotations:
          summary: "HRMS API 錯誤預算快速消耗"
          description: "最近 1 小時錯誤率 {{ $value | humanizePercentage }}，若持續將在 2 天內耗盡 30 天錯誤預算"
          runbook_url: "https://wiki/runbook/hrms-error-budget"

      - alert: HRMSErrorBudgetSlowBurn
        expr: |
          job:http_server_requests:error_ratio_rate6h > (6 * 0.001)
          and
          job:http_server_requests:error_ratio_rate30m > (6 * 0.001)
        for: 15m
        labels:
          severity: warning
          team: hrms
        annotations:
          summary: "HRMS API 錯誤預算持續消耗"
          description: "最近 6 小時錯誤率 {{ $value | humanizePercentage }}"
          runbook_url: "https://wiki/runbook/hrms-error-budget"

  - name: hrms-batch.rules
    rules:
      - alert: HRMSPayrollJobFailed
        expr: hrms_payroll_job_status == 0
        for: 1m
        labels:
          severity: critical
          team: hrms
          service: hrms-payroll
        annotations:
          summary: "HRMS 薪資計算作業失敗"
          description: "月薪計算批次作業執行失敗，需立即處理"
          runbook_url: "https://wiki/runbook/hrms-payroll-failure"
```

> ⚠️ v1.x 範本使用 `http_requests_total`，但 Spring Boot（Micrometer）實際輸出的是 `http_server_requests_seconds_count`。照抄錯誤的指標名稱，告警規則語法雖然正確，卻**永遠不會觸發**。

---

> 📌 **審閱重點**
>
> - 每個告警是否都有明確的 actionable response？
> - SLO 是否與業務需求對齊（非隨意設定）？
> - 告警是否會產生過多噪音（特別是 P3/P4）？
> - 升級機制是否涵蓋非工作時間？
> - Dashboard 是否能在 30 秒內讓值班人員判斷系統狀態？
