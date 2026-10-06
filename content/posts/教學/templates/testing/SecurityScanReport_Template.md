---
title: "安全測試與弱點掃描報告範本（Security Scan Report Template）"
date: 2026-05-18
draft: false
categories: ["教學"]
tags: ["範本", "測試驗收", "資安", "弱點掃描", "OWASP", "SSDLC"]
---

# 安全測試與弱點掃描報告範本（Security Scan Report Template）

> **適用標準**：OWASP WSTG v4.2（Web Security Testing Guide）、CVSS v4.0（相容 v3.1）、EPSS v4、CISA KEV、CWE、OWASP ASVS 5.0.0
>
> **適用階段**：測試驗證階段（Testing Phase）
>
> **負責角色**：AppSec 工程師、資安測試人員、QA Lead
>
> **範本版本**：v2.0（2026-10-06）｜對應《軟體開發標準程序教學手冊》v2.0 第 9.2、9.4 節

---

## 📑 章節目錄

1. [文件資訊](#1-文件資訊)
2. [測試摘要](#2-測試摘要)
3. [測試範圍與方法](#3-測試範圍與方法)
4. [弱點總覽](#4-弱點總覽)
5. [弱點詳細報告](#5-弱點詳細報告)
6. [合規檢核結果](#6-合規檢核結果)
7. [修復計畫](#7-修復計畫)
8. [結論與建議](#8-結論與建議)
9. [附錄](#9-附錄)
10. [審查與驗證](#10-審查與驗證)

---

## 📝 範本

---

### 1. 文件資訊

| 項目 | 內容 |
|------|------|
| **文件名稱** | [系統名稱] 安全測試報告 |
| **文件編號** | [專案代碼]-STR-[版本號]-[日期] |
| **版本** | v[X.Y] |
| **測試日期** | [YYYY-MM-DD] ~ [YYYY-MM-DD] |
| **測試人員** | [AppSec 團隊 / 外部廠商] |
| **審核者** | [CISO / 資安主管] |
| **資料分級** | Confidential |

---

### 2. 測試摘要

| 項目 | 內容 |
|------|------|
| 測試類型 | [SAST / DAST / SCA / Penetration Test / 組合] |
| 受測版本 | [Application version / Commit hash] |
| 測試結果總評 | [✅ PASS / ⚠️ CONDITIONAL PASS / ❌ FAIL] |
| 上線決策 | [可上線 / 修復後可上線 / 不可上線] |

#### 弱點統計

| 嚴重度 | 數量 | 已修復 | 待修復 | 接受風險 |
|--------|------|--------|--------|---------|
| Critical | [N] | [N] | [N] | [N] |
| High | [N] | [N] | [N] | [N] |
| Medium | [N] | [N] | [N] | [N] |
| Low | [N] | [N] | [N] | [N] |
| Info | [N] | — | — | — |
| **Total** | **[N]** | **[N]** | **[N]** | **[N]** |

---

### 3. 測試範圍與方法

#### 3.1 測試範圍

| 項目 | 內容 |
|------|------|
| 目標系統 | [系統名稱 + URL/IP] |
| 測試範圍 | [In-scope modules / endpoints] |
| 排除範圍 | [Out-of-scope，如第三方元件] |
| 認證帳號 | [測試用帳號角色清單（不含密碼）] |

#### 3.2 測試方法

| 測試類型 | 工具 | 版本 | 說明 |
|---------|------|------|------|
| SAST（靜態分析） | [SonarQube / Checkmarx / Semgrep] | [ver] | 原始碼分析 |
| DAST（動態分析） | [OWASP ZAP / Burp Suite Pro] | [ver] | 執行期掃描 |
| SCA（套件分析） | [Snyk / OWASP Dependency-Check / Trivy] | [ver] | 第三方套件弱點 |
| 手動測試 | [Burp Suite / Custom scripts] | — | 邏輯弱點 |
| Container Scan | [Trivy / Aqua] | [ver] | 容器映像掃描 |

#### 3.3 測試依據

| 標準/指南 | 涵蓋項目 |
|-----------|---------|
| OWASP Top 10:2025 | A01~A10 |
| OWASP API Security Top 10 (2023) | 全部 |
| OWASP ASVS 5.0.0 | [Level 1 / Level 2 / Level 3] |
| CWE Top 25 (2023) | 常見弱點 |

---

### 4. 弱點總覽

#### 4.1 依嚴重度分佈

| 嚴重度 | CVSS 分數範圍 | 修復 SLA | 數量 |
|--------|-------------|---------|------|
| Critical | 9.0 – 10.0 | 24 小時內緩解、7 天內修復 | [N] |
| High | 7.0 – 8.9 | 7 天 | [N] |
| Medium | 4.0 – 6.9 | 30 天 | [N] |
| Low | 0.1 – 3.9 | 90 天 | [N] |
| Info | 0.0 | 視需要 | [N] |

#### 4.2 依類型分佈

| 弱點類型（CWE） | 數量 | 嚴重度分佈 |
|----------------|------|-----------|
| [CWE-XXX: 弱點名稱] | [N] | [C:N / H:N / M:N / L:N] |
| [CWE-XXX: 弱點名稱] | [N] | [C:N / H:N / M:N / L:N] |

#### 4.3 依 OWASP Top 10 分佈

| OWASP Category | 弱點數量 | 最高嚴重度 |
|----------------|---------|-----------|
| A01:2025 Broken Access Control（含 SSRF） | [N] | [Critical/High/...] |
| A02:2025 Security Misconfiguration | [N] | |
| A03:2025 Software Supply Chain Failures | [N] | |
| A04:2025 Cryptographic Failures | [N] | |
| A05:2025 Injection | [N] | |
| A06:2025 Insecure Design | [N] | |
| A07:2025 Authentication Failures | [N] | |
| A08:2025 Software or Data Integrity Failures | [N] | |
| A09:2025 Security Logging and Alerting Failures | [N] | |
| A10:2025 Mishandling of Exceptional Conditions | [N] | |

---

### 5. 弱點詳細報告

#### VULN-[NNN]: [弱點標題]

| 項目 | 內容 |
|------|------|
| **弱點 ID** | VULN-[NNN] |
| **嚴重度** | [Critical / High / Medium / Low] |
| **CVSS 分數** | [N.N]（CVSS 版本：[4.0 / 3.1]） |
| **CVSS Vector** | [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N] |
| **EPSS** | [機率，例 0.0123；查詢日期]（第三方套件 CVE 才有） |
| **CISA KEV** | [是（加入日期）/ 否] |
| **可達性** | [可達 / 不可達（附分析依據）/ 未分析] |
| **CWE** | CWE-[NNN]: [名稱] |
| **OWASP** | [A01:2025 / A05:2025 / ...] |
| **發現工具** | [SAST / DAST / Manual] |
| **受影響元件** | [模組/檔案/API endpoint] |
| **狀態** | [Open / Fixed / Accepted / False Positive] |

**描述：**

[詳細描述弱點的性質與成因]

**影響：**

[描述此弱點被利用後可能造成的危害]

**重現步驟：**

1. [步驟 1]
2. [步驟 2]
3. [步驟 3]

**證據：**

```text
[Request/Response 片段或截圖參考]
```

**修復建議：**

[具體的修復方法與安全程式碼範例]

```text
// 修復前（不安全）
[insecure code snippet]

// 修復後（安全）
[secure code snippet]
```

**參考資源：**

- [相關 CVE / CWE / OWASP 頁面連結]

---

### 6. 合規檢核結果

#### 6.1 OWASP ASVS 合規

| ASVS Chapter | 檢核項數 | 通過 | 未通過 | N/A | 合規率 |
|-------------|---------|------|--------|-----|--------|
| V1: Encoding and Sanitization | [N] | [N] | [N] | [N] | [N]% |
| V2: Validation and Business Logic | [N] | [N] | [N] | [N] | [N]% |
| V3: Web Frontend Security | [N] | [N] | [N] | [N] | [N]% |
| V4: API and Web Service | [N] | [N] | [N] | [N] | [N]% |
| V6: Authentication | [N] | [N] | [N] | [N] | [N]% |
| V7: Session Management | [N] | [N] | [N] | [N] | [N]% |
| V8: Authorization | [N] | [N] | [N] | [N] | [N]% |
| V11: Cryptography | [N] | [N] | [N] | [N] | [N]% |
| V12: Secure Communication | [N] | [N] | [N] | [N] | [N]% |
| V13: Configuration | [N] | [N] | [N] | [N] | [N]% |
| V14: Data Protection | [N] | [N] | [N] | [N] | [N]% |
| V16: Security Logging and Error Handling | [N] | [N] | [N] | [N] | [N]% |

> ASVS 5.0.0 共 17 章（V1–V17）；不適用的章節（例如未使用 WebRTC 的 V17）標示 N/A，不要刪除列，讓審查者知道已評估過。

---

### 7. 修復計畫

#### 7.1 修復優先順序

| # | 弱點 ID | 嚴重度 | 排序依據（CVSS／EPSS／KEV／可達性） | 修復 SLA | 負責人 | 預計修復日 | 狀態 |
|---|---------|--------|--------------------------------|---------|--------|-----------|------|
| 1 | VULN-002 | Critical | 列於 KEV → 一律 Critical | 24 hr 緩解／7 days 修復 | [姓名] | [日期] | [Open/Fixed] |
| 2 | VULN-001 | High | CVSS 4.0 7.1、可達 | 7 days | [姓名] | [日期] | [Open/Fixed] |

#### 7.2 風險接受記錄

無法於 SLA 內修復的弱點，必須另填《風險接受單範本》，下表只記錄摘要：

| 弱點 ID | 嚴重度 | 接受理由 | 補償控制 | 核准人 | 到期日 |
|---------|--------|---------|---------|--------|--------|
| [VULN-NNN] | [Med] | [理由] | [補償措施] | [CISO] | [日期] |

---

### 8. 結論與建議

| 項目 | 內容 |
|------|------|
| **上線決策** | [✅ 可上線 / ⚠️ 條件式上線 / ❌ 不可上線] |
| **條件** | [需修復 N 個 Critical/High 弱點後重測] |
| **長期建議** | [改善建議摘要] |
| **下次掃描建議** | [時機/範圍] |

---

### 9. 附錄

#### 9.1 工具掃描完整報告

| 工具 | 報告位置 |
|------|---------|
| [SAST report] | [path/URL] |
| [DAST report] | [path/URL] |
| [SCA report] | [path/URL] |

#### 9.2 測試環境細節

[補充測試環境配置細節]

---

### 10. 審查與驗證

> 本節供審查者使用，也用來檢查 AI 依本範本產出的文件是否正確；對應《軟體開發標準程序教學手冊》v2.0 各章的「審查與驗證」。

#### 自動檢查

| 檢查項目 | 方法 |
|---------|------|
| CVSS 分數可重算 | 以 FIRST 官方計算器（或 Python `cvss` 套件）依向量重算分數 |
| EPSS／KEV | `https://api.first.org/data/v1/epss?cve=...`；CISA KEV JSON |
| 重測 | 修復後以相同工具重新掃描 |

#### 人工審查問題

1. Critical／High 弱點是否都有修復計畫或風險接受單？
2. 排序是否同時考慮 CVSS、EPSS、KEV 與可達性？
3. False Positive 是否有驗證依據？
4. SCA 是否涵蓋間接依賴？

#### AI 常見錯誤

- 手填 CVSS 分數與向量不符（v1.x 範例 7.5 實為 6.5）。
- 沿用 OWASP Top 10:2021 分類與 ASVS 4.0.3 章節。
- 以佔位 CVE 編號（CVE-2024-XXXXX）搭配真實套件版本，造成誤導。

---

## 📖 使用說明

### CVSS 嚴重度定義

| 嚴重度 | CVSS | 定義 | 修復 SLA |
|--------|------|------|---------|
| Critical | 9.0-10.0 | 可遠端利用、無需認證、影響核心資料 | 24 小時內緩解、7 天內修復 |
| High | 7.0-8.9 | 需部分條件、影響機密或完整性 | 7 天 |
| Medium | 4.0-6.9 | 需較多條件或影響有限 | 30 天 |
| Low | 0.1-3.9 | 影響極小或需物理接觸 | 90 天 |

### 弱點排序規則（CVSS + EPSS + KEV）

CVSS 只描述「被利用時有多嚴重」，不回答「會不會被利用」。排序規則（對應《軟體開發標準程序教學手冊》9.2）：

1. 列於 CISA KEV → 不論分數，一律以 Critical 處理
2. CVSS ≥ 7.0 且 EPSS ≥ 0.1 → 升一級
3. CVSS ≥ 7.0 但經確認「不可達」→ 降一級，並記錄分析依據與複核日期
4. 其他 → 依 CVSS 等級

> CVSS v4.0 與 v3.1 的分數區間相同，但分數不能直接比較。新弱點優先採用 v4.0；NVD 只提供 v3.1 分數時沿用 v3.1，並在「CVSS 分數」欄註明版本。

### 弱點管理流程

```mermaid
graph LR
    A[掃描發現] --> B[驗證確認]
    B -->|True Positive| C[分級評估]
    B -->|False Positive| D[標記 FP]
    C --> E{嚴重度}
    E -->|Critical/High| F[立即修復]
    E -->|Medium/Low| G[排入 Backlog]
    F --> H[驗證修復]
    G --> H
    H -->|Pass| I[關閉]
    H -->|Fail| F
```

---

## 💡 範例（以 HRMS 人力資源管理系統為例）

---

### 範例：弱點報告

#### VULN-001: IDOR - 員工薪資資訊未授權存取

| 項目 | 內容 |
|------|------|
| **嚴重度** | High |
| **CVSS** | 7.1（CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N） |
| **CWE** | CWE-639: Authorization Bypass Through User-Controlled Key |
| **OWASP** | A01:2025 Broken Access Control |
| **ASVS 5.0** | 8.2.2（資料層級授權） |
| **受影響 API** | GET /api/salary/{employeeId} |
| **狀態** | Fixed |

**描述：**\
一般員工角色可透過修改 URL 中的 employeeId 參數，存取其他員工的薪資資訊，API 未驗證當前用戶是否有權限存取目標員工資料。

**重現步驟：**

1. 以一般員工帳號 (EMP-001) 登入系統
2. 正常查詢自己的薪資 GET /api/salary/EMP-001 → 200 OK
3. 修改 URL 為 GET /api/salary/EMP-042 → 200 OK（應為 403）

**修復建議：**

```java
// 修復前
@GetMapping("/api/salary/{employeeId}")
public SalaryDto getSalary(@PathVariable String employeeId) {
    return salaryService.findByEmployeeId(employeeId);
}

// 修復後 - 加入權限檢查
@GetMapping("/api/salary/{employeeId}")
@PreAuthorize("hasRole('HR') or #employeeId == authentication.principal.employeeId")
public SalaryDto getSalary(@PathVariable String employeeId) {
    return salaryService.findByEmployeeId(employeeId);
}
```

---

#### VULN-002: 第三方套件高風險 CVE

| 項目 | 內容 |
|------|------|
| **嚴重度** | Critical |
| **CVE** | CVE-2021-44228（Log4Shell） |
| **CVSS** | 10.0（CVSS v3.1，NVD；未提供 v4.0 分數時沿用 v3.1） |
| **EPSS** | 0.99999（FIRST EPSS API，2026-10-05） |
| **CISA KEV** | 是（2021-12-10 加入） |
| **受影響套件** | log4j-core 2.14.1 |
| **修復版本** | ≥ 2.17.1 |
| **OWASP** | A03:2025 Software Supply Chain Failures |
| **狀態** | Fixed |

> 範例說明：v1.x 範本的 VULN-001 寫「7.5（CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N）」，但該向量以 CVSS 3.1 計算實為 **6.5 Medium**。分數必須由計算器依向量產生，不可手填；審查時以 FIRST 官方計算器重算。

---

> 📌 **審閱重點**
>
> - 所有 Critical/High 弱點是否都有修復計畫或接受風險記錄？
> - False Positive 是否有驗證依據？
> - 修復建議是否具體可行（非僅描述問題）？
> - SCA 掃描是否涵蓋所有直接與間接依賴？
> - 合規結果是否滿足上線的最低門檻？
