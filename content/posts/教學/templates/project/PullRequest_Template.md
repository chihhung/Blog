---
title: "Pull Request 說明範本（Pull Request Template）"
date: 2026-10-06
draft: false
categories: ["教學"]
tags: ["範本", "版本控制", "Code Review", "AI 輔助開發"]
---

# Pull Request 說明範本（Pull Request Template）

> **參照標準**：GitHub Pull Request Templates / Conventional Commits 1.0.0
>
> **文件用途**：統一 PR 說明格式，讓 Reviewer 知道改了什麼、為什麼改、如何驗證，以及 AI 參與了哪些部分
>
> **適用階段**：開發階段，每個 PR
>
> **範本版本**：v2.0（2026-10-06）｜對應《軟體開發標準程序教學手冊》v2.0 第 1.5、7.1 節

---

## 📋 章節目錄

1. [放置位置](#1-放置位置)
2. [PR 說明內容](#2-pr-說明內容)
3. [自動檢查 PR 說明](#3-自動檢查-pr-說明)
4. [審查與驗證](#4-審查與驗證)

---

## 1. 放置位置

### 📝 範本

| 平台 | 檔案位置 |
|------|---------|
| GitHub | `.github/pull_request_template.md` |
| GitLab | `.gitlab/merge_request_templates/Default.md` |
| Azure DevOps | `.azuredevops/pull_request_template.md` |

### 📖 使用說明

- 範本放在預設分支後，開 PR 時會自動帶入
- PR 標題採 Conventional Commits 格式（例：`feat(leave): 新增特休額度檢查`），便於自動產生 CHANGELOG

### 💡 範例

```text
.github/
├── pull_request_template.md
├── CODEOWNERS
└── workflows/
```

---

## 2. PR 說明內容

### 📝 範本

```markdown
## 變更摘要
{一到三句話說明改了什麼}（工作項目：{編號}）

## 變更原因
{為什麼需要這個變更；連結需求或事件}

## 變更類型
- [ ] 新功能（feat）　- [ ] 修正（fix）　- [ ] 重構（refactor）　- [ ] 不相容變更（BREAKING CHANGE）

## 驗證方式
- [ ] 自動化測試：{新增／修改的測試}
- [ ] 手動驗證：{步驟與結果}

## AI 參與範圍
- 使用工具：{工具名稱與版本，或「未使用」}
- AI 產生：{檔案／方法}
- 人工修改：{修改了 AI 產出的哪些部分與原因}
- 人工驗證方式：{如何確認 AI 產出正確}

## 審查重點
{請 Reviewer 特別注意的地方}

## 檢查清單
- [ ] 文件已更新（OpenAPI、SDD、ADR、README）
- [ ] 無機敏資訊（密碼、Token、真實個資）
- [ ] 資料庫變更可與舊版程式並存（Expand／Contract）
```

### 📖 使用說明

- 「驗證方式」必須能證明功能正確，「看起來沒問題」不算
- 「AI 參與範圍」讓 Reviewer 分配審查力道；作者必須能解釋 AI 產生的每一行
- 不相容變更必須說明影響與遷移方式

### 💡 範例

```markdown
## 變更摘要
申請特休時檢查剩餘額度，不足時回傳 422 Problem Details（工作項目：HRMS-412）

## 變更原因
主管每月約退件 40 筆額度不足的申請（需求 FR-LV-002）

## 變更類型
- [x] 新功能（feat）

## 驗證方式
- [x] 自動化測試：`LeaveQuotaPolicyTest`（6 個案例，含剛好等於額度的邊界值）、`LeaveControllerIT`（422 回應格式）
- [x] 手動驗證：測試環境以 E20260001 申請 3 天（剩 2 天）→ 422，畫面顯示正確訊息

## AI 參與範圍
- 使用工具：GitHub Copilot（公司核准版本）
- AI 產生：`LeaveQuotaPolicy#check` 初版、`LeaveQuotaPolicyTest` 4 個案例
- 人工修改：補上半天假的額度計算（AI 版本只處理整天）；補上邊界值測試
- 人工驗證方式：本機 `mvn verify` 通過；PIT mutation score 85%

## 審查重點
- 半天假（0.5 天）的比較是否有浮點誤差（已改用 BigDecimal）

## 檢查清單
- [x] 文件已更新（OpenAPI：新增 422 回應）
- [x] 無機敏資訊
- [x] 無資料庫變更
```

---

## 3. 自動檢查 PR 說明

### 📝 範本

```yaml
# .github/workflows/pr-description.yml：檢查 PR 說明的必要段落
name: PR description check

on:
  pull_request:
    types: [opened, edited, synchronize]

permissions:
  contents: read

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Require sections
        env:
          BODY: ${{ github.event.pull_request.body }}
        run: |
          for section in "## 變更摘要" "## 驗證方式" "## AI 參與範圍"; do
            if ! printf '%s' "$BODY" | grep -qF "$section"; then
              echo "::error::PR 說明缺少段落：$section"
              exit 1
            fi
          done
```

### 📖 使用說明

- PR 說明屬使用者可控內容，必須透過 `env` 傳入，**不可**在 `run:` 中直接寫 `${{ github.event.pull_request.body }}`，否則可能造成指令注入
- 此 Job 設為分支保護的必要檢查

### 💡 範例

PR 說明缺少「AI 參與範圍」時，Job 輸出：

```text
Error: PR 說明缺少段落：## AI 參與範圍
```

---

## 4. 審查與驗證

> 本節供審查者使用，也用來檢查 AI 依本範本產出的 PR 說明是否正確。

### 自動檢查

| 檢查項目 | 方法 |
|---------|------|
| 必要段落存在 | 第 3 節的 workflow（以 `actionlint` 檢查語法） |
| PR 標題格式 | `npx commitlint` 檢查 PR 標題（Conventional Commits） |
| 關聯工作項目 | 正規表示式檢查標題或說明含工作項目編號 |

### 人工審查問題

1. 「驗證方式」能否真的證明功能正確？
2. AI 產生的部分，作者能否解釋每一行？
3. 不相容變更是否標示並說明遷移方式？
4. 文件是否與程式同步更新？

### AI 常見錯誤

- 產生空泛的變更摘要（「優化程式碼」）。
- 驗證方式寫「已測試」而沒有具體測試名稱。
- 在 workflow 的 `run:` 中直接嵌入 `${{ github.event.pull_request.body }}`。

---

> 📌 **範本使用注意事項**
>
> 1. 範本放在 Repository 預設分支，所有 PR 自動套用
> 2. 搭配「DoR／DoD 範本」與《程式寫作指引》的 Code Review 規則使用
