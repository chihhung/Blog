---
title: "DoR／DoD 範本（Definition of Ready & Definition of Done Template）"
date: 2026-10-06
draft: false
categories: ["教學"]
tags: ["範本", "專案管理", "敏捷", "品質管理"]
---

# DoR／DoD 範本（Definition of Ready & Definition of Done）

> **參照標準**：Scrum Guide 2020（Definition of Done）/ 業界 Definition of Ready 慣例
>
> **文件用途**：定義工作項目「可以排入 Sprint」與「可以標示完成」的條件，每一條都要能指出證據
>
> **適用階段**：專案啟動時制定，每季回顧時檢討
>
> **範本版本**：v2.0（2026-10-06）｜對應《軟體開發標準程序教學手冊》v2.0 第 2.4 節

---

## 📋 章節目錄

1. [Definition of Ready](#1-definition-of-ready)
2. [Definition of Done](#2-definition-of-done)
3. [自動化對應](#3-自動化對應)
4. [審查與驗證](#4-審查與驗證)

---

## 1. Definition of Ready

### 📝 範本

```markdown
## Definition of Ready（Story 可以排入 Sprint 的條件）
- [ ] {條件 1}　證據：{在哪裡可以確認}
- [ ] {條件 2}　證據：{…}
```

### 📖 使用說明

- DoR 防止「需求不清就開工」；未符合 DoR 的 Story 不得排入 Sprint
- 每一條都寫出證據所在，避免「感覺已經準備好」

### 💡 範例

```markdown
## Definition of Ready
- [ ] 符合 INVEST 原則　　　　　　　證據：Story 頁面的 INVEST 檢查表
- [ ] 至少 1 個正常與 1 個例外的 Gherkin 驗收條件　證據：Story 頁面的驗收條件
- [ ] 相依的 API／資料表已存在或排入同一 Sprint　證據：相依 Story 狀態
- [ ] UI 需求附 Figma 連結　　　　　證據：Story 欄位
- [ ] 估點 ≤ 8 點　　　　　　　　　證據：Story Points 欄位
- [ ] 涉及個資的欄位已在資料分級表中　證據：資料分級對照表版本
```

---

## 2. Definition of Done

### 📝 範本

```markdown
## Definition of Done（Story 可以標示完成的條件）
- [ ] {條件 1}　證據：{CI 紀錄／PR 連結／簽核}
```

### 📖 使用說明

- DoD 適用於所有 Story；團隊不得對個別 Story 降低標準
- 能自動化的條件交給 CI 與分支保護，不靠人記得

### 💡 範例

```markdown
## Definition of Done
- [ ] 程式碼已合併至 main，PR 至少 1 位 Reviewer 核准（L1 專案 2 位）　證據：PR 連結
- [ ] CI 全數通過：建置、單元／整合測試、SAST、SCA、Secrets 掃描　證據：CI 執行紀錄
- [ ] 新增程式碼行覆蓋率 ≥ 80%、分支覆蓋率 ≥ 70%　證據：SonarQube 品質閘門
- [ ] 每條驗收條件都有自動化測試或手動測試紀錄　證據：RTM
- [ ] API 異動已更新 OpenAPI；設計異動已更新 SDD 或新增 ADR　證據：PR 中的檔案變更
- [ ] 已部署到測試環境並由 PO 驗收　證據：PO 於 Story 留言確認
- [ ] PR 說明已填寫 AI 參與範圍（如有使用 AI）　證據：PR 說明
```

---

## 3. 自動化對應

### 📝 範本

| DoD 條件 | 自動化方式 | 未自動化時的人工確認者 |
|---------|-----------|-------------------|
| {條件} | {分支保護必要檢查／CI Job／品質閘門} | {角色} |

### 📖 使用說明

- 目標是讓 DoD 中大部分條件由工具強制，人工只確認需要判斷的部分

### 💡 範例

| DoD 條件 | 自動化方式 | 未自動化時的人工確認者 |
|---------|-----------|-------------------|
| PR 核准 | 分支保護：Require approvals（1／2 位）、最後一次推送需重新核准 | — |
| CI 通過 | 分支保護：Require status checks（build、security-scan） | — |
| 覆蓋率 | SonarQube 品質閘門 + `sonar.qualitygate.wait=true` | — |
| 驗收條件有測試 | RTM 前向追溯腳本 | QA |
| PO 驗收 | — | PO |

---

## 4. 審查與驗證

> 本節供審查者使用，也用來檢查 AI 依本範本產出的 DoR／DoD 是否正確。

### 自動檢查

| 檢查項目 | 方法 |
|---------|------|
| 每條都有證據 | `grep -c "證據：" dod.md` 等於條件數 |
| 分支保護與 DoD 一致 | `gh api repos/{owner}/{repo}/rulesets` 檢查必要檢查與核准人數 |
| 已完成 Story 符合 DoD | 抽查本 Sprint 已完成 Story 的證據連結 |

### 人工審查問題

1. 每一條都能指出證據嗎？
2. 有沒有「程式碼品質良好」等無法判定的條款？
3. 過去一個月是否有不符 DoD 卻被標示完成的 Story？
4. DoD 是否涵蓋安全掃描與文件更新？

### AI 常見錯誤

- 產生無法驗證的條款（「測試充分」「品質良好」）。
- 遺漏安全掃描與文件更新。
- DoR 與 DoD 混用（把「已部署」放進 DoR）。

---

> 📌 **範本使用注意事項**
>
> 1. DoR／DoD 由團隊共同制定並公開張貼
> 2. 搭配「User Story 範本」「Pull Request 範本」使用
