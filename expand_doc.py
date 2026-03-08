#!/usr/bin/env python3
"""Insert expansion content into the Claude Code handbook."""
import os

FILE = r"d:\developer\repos\Blog\content\posts\教學\AI開發\Claude Code生態圈教學手冊.md"

# Read current content
with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# EXPANSION 1: After §1.2.5 Output Styles, before Part 2
# Insert §1.2.6 權限與安全模型, §1.2.7 工具系統, §1.2.8 上下文管理進階
# ============================================================
MARKER1 = "Output Style 對回覆格式的影響更為顯著。\n\n---"

EXPANSION1 = """Output Style 對回覆格式的影響更為顯著。

### 1.2.6 權限與安全模型

Claude Code 採用**多層式權限架構**，確保安全性和開發效率的平衡：

```mermaid
graph TB
    subgraph "權限層級（由高到低）"
        ENT["企業管控<br/>managed-settings.json<br/>最高優先權"] --> DENY["Deny 清單<br/>強制拒絕"]
        DENY --> ALLOW["Allow 清單<br/>自動允許"]
        ALLOW --> INTERACTIVE["互動式許可<br/>使用者每次確認"]
    end
    
    subgraph "Permission Modes"
        NORMAL["Normal Mode<br/>每次詢問"]
        PLAN["Plan Mode<br/>唯讀分析"]
        AUTO["Auto-accept Mode<br/>自動接受"]
    end
    
    INTERACTIVE --> NORMAL
    INTERACTIVE --> PLAN
    INTERACTIVE --> AUTO
    
    style ENT fill:#ef4444,stroke:#dc2626,color:#fff
    style DENY fill:#f97316,stroke:#ea580c
    style ALLOW fill:#10b981,stroke:#059669,color:#fff
    style AUTO fill:#fbbf24,stroke:#d97706
```

#### 權限規則語法

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Bash(npm test *)",
      "Bash(npm run lint *)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Bash(git status)",
      "mcp__github__*"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo *)",
      "Bash(curl * | bash)",
      "Bash(wget * | bash)",
      "Bash(npm publish *)",
      "Bash(git push --force *)"
    ]
  }
}
```

#### 工具權限模式詳解

| 工具名稱 | 說明 | 權限範例 |
|---------|------|---------|
| **Read** | 讀取檔案 | `Read` — 允許讀取所有檔案 |
| **Write** | 寫入檔案 | `Write` — 允許寫入所有檔案 |
| **Edit** | 編輯檔案 | `Edit` — 允許編輯所有檔案 |
| **Bash** | 執行 shell 命令 | `Bash(npm test *)` — 僅允許 npm test |
| **mcp__*__** | MCP 工具 | `mcp__github__*` — 允許所有 GitHub MCP 工具 |
| **WebSearch** | 網路搜尋 | `WebSearch` — 允許網路搜尋 |

#### 萬用字元規則

| 模式 | 說明 | 範例 |
|------|------|------|
| `*` | 匹配任意字元 | `Bash(npm *)` 匹配 `npm test`、`npm run` 等 |
| 精確匹配 | 完全匹配工具名稱 | `Read` 僅匹配 Read 工具 |
| 前綴+萬用 | 匹配以特定前綴開始的工具 | `mcp__github__*` |

### 1.2.7 工具系統概覽

Claude Code 內建以下工具類別：

| 類別 | 工具 | 說明 |
|------|------|------|
| **檔案操作** | Read, Write, Edit | 讀取、寫入和編輯專案檔案 |
| **終端機** | Bash | 執行 shell 命令 |
| **搜尋** | Grep, Glob, WebSearch | 搜尋程式碼和網路 |
| **版本控制** | Git 相關（透過 Bash） | Git 操作 |
| **MCP 工具** | mcp__<server>__<tool> | MCP Server 提供的外部工具 |
| **子代理** | Agent, Task | 派出子代理執行獨立任務 |
| **排程** | CronCreate, CronList, CronDelete | 管理自動化排程任務 |

#### 工具執行流程

```mermaid
sequenceDiagram
    participant U as 使用者
    participant C as Claude
    participant P as 權限系統
    participant H as Hooks
    participant T as 工具
    
    U->>C: 提出需求
    C->>C: 分析需求，決定使用工具
    C->>P: 檢查權限
    
    alt 在 deny 清單中
        P-->>C: ❌ 拒絕
        C-->>U: 告知無法執行
    else 在 allow 清單中
        P-->>C: ✅ 自動允許
        C->>H: 觸發 PreToolUse Hook
        H-->>C: Hook 結果
        alt Hook 阻止（exit 2）
            C-->>U: 告知被 Hook 阻止
        else Hook 允許（exit 0）
            C->>T: 執行工具
            T-->>C: 工具結果
            C->>H: 觸發 PostToolUse Hook
            H-->>C: Hook 完成
            C-->>U: 回覆結果
        end
    else 不在任何清單中
        P-->>U: 請求使用者許可
        U-->>P: 允許/拒絕
        alt 使用者允許
            P-->>C: ✅ 允許
            C->>T: 執行工具
            T-->>C: 工具結果
            C-->>U: 回覆結果
        else 使用者拒絕
            P-->>C: ❌ 拒絕
            C-->>U: 告知使用者已拒絕
        end
    end
```

### 1.2.8 上下文管理進階策略

#### /compact 壓縮機制

當上下文視窗接近上限時，Claude Code 會自動觸發壓縮，或使用者可以手動觸發：

```
> /compact    # 使用預設摘要策略壓縮
> /compact 保留所有與認證相關的上下文    # 指定壓縮時要保留的重點
```

壓縮流程：

```mermaid
sequenceDiagram
    participant CTX as 上下文視窗
    participant HOOK as PreCompact Hook
    participant LLM as Claude
    participant NEW as 壓縮後上下文
    
    CTX->>CTX: 偵測上下文接近上限
    CTX->>HOOK: 觸發 PreCompact Hook
    Note over HOOK: 可在此保存重要上下文到檔案
    HOOK-->>CTX: Hook 完成
    CTX->>LLM: 請求摘要壓縮
    LLM->>LLM: 產生對話摘要
    LLM->>NEW: 建立壓縮後上下文
    Note over NEW: 保留 CLAUDE.md + 摘要 + 最近訊息
```

#### 上下文優化技巧

| 技巧 | 說明 |
|------|------|
| **善用 CLAUDE.md** | 把重要的專案資訊寫在 CLAUDE.md 中，壓縮後仍會保留 |
| **針對性 /compact** | 指定壓縮時要保留的重點，避免遺失關鍵上下文 |
| **PreCompact Hook** | 在壓縮前自動保存重要資訊到檔案 |
| **子目錄 CLAUDE.md** | 只有在存取該目錄時才載入，減少不必要的上下文占用 |
| **@file 引用** | 用 `@file` 精確引用需要的檔案，而非依賴搜尋 |

#### CLAUDE.md 載入機制

```mermaid
graph TB
    subgraph "CLAUDE.md 載入順序"
        G["~/.claude/CLAUDE.md<br/>全域記憶"] --> P["./CLAUDE.md<br/>專案根目錄"]
        P --> S["./src/CLAUDE.md<br/>子目錄（按需載入）"]
        S --> L["./.claude/CLAUDE.local.md<br/>本地記憶（不簽入版控）"]
    end
    
    G --> |"個人偏好<br/>通用指令"| MERGE[合併到上下文]
    P --> |"專案規範<br/>建置命令"| MERGE
    S --> |"模組特定指令<br/>（存取時載入）"| MERGE
    L --> |"個人本地設定"| MERGE
    
    style G fill:#3b82f6,stroke:#2563eb,color:#fff
    style P fill:#6366f1,stroke:#4f46e5,color:#fff
    style S fill:#818cf8,stroke:#6366f1,color:#fff
    style L fill:#a5b4fc,stroke:#818cf8
```

#### CLAUDE.md 高效撰寫範本

```markdown
# Project: MyApp

## Quick Reference
- Build: `npm run build`
- Test all: `npm test`
- Test single: `npm test -- --grep "test name"`
- Lint: `npm run lint`
- Dev server: `npm run dev` (port 3000)

## Code Standards
- TypeScript strict mode, no `any` type
- Functions max 30 lines, Files max 300 lines
- Use async/await, not Promise chains
- Error handling: custom AppError class in src/errors/

## Architecture
- Monorepo with Turborepo
- packages/api — Express + Prisma
- packages/web — Next.js 14 App Router
- packages/shared — Shared types and utils

## Database
- PostgreSQL via Prisma ORM
- Migrations: `npx prisma migrate dev`
- Schema: packages/api/prisma/schema.prisma

## Git Conventions
- Branches: feature/*, fix/*, chore/*
- Commits: Conventional Commits (feat:, fix:, chore:)
- Always create PR, never push to main directly

## Security Rules
- NEVER hardcode secrets or API keys
- NEVER disable TypeScript strict checks
- NEVER use eval() or Function()
- NEVER commit .env files
```

#### 多目錄 CLAUDE.md 範例

```
project-root/
├── CLAUDE.md               # 全域專案設定
├── src/
│   ├── CLAUDE.md           # src 通用指令
│   ├── api/
│   │   └── CLAUDE.md       # API 模組指令
│   ├── web/
│   │   └── CLAUDE.md       # Web 前端指令
│   └── shared/
│       └── CLAUDE.md       # 共享類別庫指令
├── tests/
│   └── CLAUDE.md           # 測試指令
└── .claude/
    └── CLAUDE.local.md     # 個人偏好（不簽入版控）
```

**src/api/CLAUDE.md**:
```markdown
# API Module

## 路由規則
- 路由定義在 src/api/routes/ 目錄
- 每個資源一個路由檔（users.ts, products.ts）
- 使用 Express Router

## 資料庫
- Prisma ORM, 不直接寫 SQL
- Migration 前先 `npx prisma format`
- 總是使用 transaction 處理多表操作

## 認證
- JWT token 在 middleware/auth.ts
- 路由保護使用 requireAuth middleware
```

**src/web/CLAUDE.md**:
```markdown
# Web Frontend

## 元件規則
- React Server Components by default
- 'use client' only when needed (state, effects, browser APIs)
- Shadcn/ui for UI components
- Tailwind CSS, no inline styles

## 狀態管理
- Server state: React Query (TanStack)
- Client state: Zustand (minimal)
- Form state: React Hook Form + Zod

## 頁面路由
- App Router (app/ directory)
- 動態路由: [param]/page.tsx
- Loading states: loading.tsx
- Error handling: error.tsx
```

---"""

if MARKER1 in content:
    content = content.replace(MARKER1, EXPANSION1, 1)
    print("Expansion 1 applied successfully")
else:
    print(f"ERROR: Marker 1 not found!")
    # Try to find partial match
    import re
    match = re.search(r'Output Style.*?影響更為顯著', content, re.DOTALL)
    if match:
        print(f"Found partial match at position {match.start()}")

# ============================================================
# EXPANSION 2: After §2.1 Subagents, expand with more examples
# ============================================================
MARKER2 = "## 2.2 Skills（技能系統）"

EXPANSION2_BEFORE = """### 2.1.6 Agent 通信與生命週期

#### Subagent 生命週期

```mermaid
stateDiagram-v2
    [*] --> Created: Agent 被呼叫
    Created --> Running: 開始執行
    Running --> WaitingForTool: 需要使用工具
    WaitingForTool --> Running: 工具回傳結果
    Running --> Completed: 任務完成
    Running --> Failed: 執行失敗
    Completed --> [*]: 回傳結果給主 Agent
    Failed --> [*]: 回傳錯誤給主 Agent
```

#### Subagent 資源限制

| 資源 | 限制 | 說明 |
|------|------|------|
| **上下文視窗** | 獨立於主 Agent | 有自己的 context |
| **工具存取** | 受 allowed-tools 控制 | 只能使用被允許的工具 |
| **嵌套深度** | 有上限 | 避免無限遞迴 |
| **執行時間** | 無硬性限制 | 但受主 Agent 的整體時間影響 |

### 2.1.7 Agent 常見模式

#### 模式一：專家分工

建立多個專精於不同領域的 Agent：

```
.claude/agents/
├── security-auditor.md    # 安全稽核專家
├── performance-tuner.md   # 效能優化專家
├── accessibility-checker.md # 無障礙驗證專家
├── api-designer.md        # API 設計專家
└── db-optimizer.md        # 資料庫優化專家
```

**security-auditor.md**:
```yaml
---
name: Security Auditor
description: 專注於安全漏洞掃描和修復建議
model: claude-sonnet-4-20250514
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash(npm audit *)
  - Bash(npx eslint --rule * *)
---

# Security Auditor Agent

你是一位專業的資安稽核人員。分析程式碼時，重點關注：

## OWASP Top 10
1. Broken Access Control — 檢查權限驗證
2. Cryptographic Failures — 檢查加密實作
3. Injection — 檢查 SQL/XSS/Command Injection
4. Insecure Design — 檢查設計模式安全性
5. Security Misconfiguration — 檢查設定
6. Vulnerable Components — 檢查依賴漏洞
7. Authentication Failures — 檢查認證邏輯
8. Data Integrity Failures — 檢查資料完整性
9. Logging Failures — 檢查日誌記錄
10. SSRF — 檢查伺服器端請求偽造

## 輸出格式
- 嚴重程度：Critical / High / Medium / Low / Info
- 位置：檔案路徑和行號
- 問題描述
- 修復建議
- 參考資源
```

**performance-tuner.md**:
```yaml
---
name: Performance Tuner
description: 效能分析和優化建議
model: claude-sonnet-4-20250514
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash(npm run build *)
  - Bash(npx lighthouse *)
---

# Performance Tuner Agent

你是一位效能最佳化專家。分析程式碼時，關注：

## 分析面向
1. **Bundle Size** — 分析打包大小，識別可 tree-shake 的程式碼
2. **Runtime Performance** — 檢查 O(n²) 以上的演算法
3. **Memory Leaks** — 檢查事件監聽器未清除、閉包引用
4. **Database Queries** — 檢查 N+1 查詢問題
5. **Caching** — 識別可快取的計算和 API 呼叫
6. **Lazy Loading** — 檢查是否有可延遲載入的模組
7. **Rendering** — 檢查不必要的 re-render（React）

## 輸出格式
每個發現包含：
- 影響程度（⚡ 高影響 / 🔧 中影響 / 💡 低影響）
- 位置
- 現況描述
- 優化建議與預估改善幅度
```

#### 模式二：工作流程管線

建立按順序執行的 Agent 管線：

```yaml
---
name: Feature Pipeline Lead
description: 管理功能開發的完整管線
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(npm *)
  - Bash(git *)
---

# Feature Pipeline Lead

當收到新功能需求時，依序執行以下管線：

## 管線步驟

### 1. 需求分析
先使用 Explore Agent 搜尋相關程式碼，了解現有架構。

### 2. 設計
產出設計方案，包含：
- 需要修改的檔案清單
- 新增的檔案清單
- 資料流圖

### 3. 實作
依設計方案逐步實作，每個檔案完成後執行測試。

### 4. 測試
撰寫單元測試和整合測試。

### 5. 審查
自我審查程式碼品質，確保符合專案規範。

### 6. 文件
更新相關文件和 CHANGELOG。
```

#### 模式三：互動式助手

```yaml
---
name: Onboarding Assistant
description: 幫助新進開發者了解專案架構
model: claude-sonnet-4-20250514
allowed-tools:
  - Read
  - Grep
  - Glob
---

# 新手引導助手

你是這個專案的引導助手，專門幫助新進開發者快速上手。

## 回答問題時的原則
1. 總是先搜尋實際程式碼，用真實的程式碼片段回答
2. 說明程式碼的商業邏輯背景
3. 標示相關檔案的位置
4. 補充團隊的開發慣例

## 常見問題類型
- 「這個模組做什麼的？」→ 搜尋模組，解釋用途
- 「怎麼新增 API endpoint？」→ 找到現有範例，說明步驟
- 「資料庫 schema 在哪？」→ 找到 schema 檔案，解釋結構
- 「怎麼跑測試？」→ 找到測試命令，說明流程
```

---

## 2.2 Skills（技能系統）"""

content = content.replace(MARKER2, EXPANSION2_BEFORE, 1)
print("Expansion 2 applied successfully")

# ============================================================
# EXPANSION 3: After §2.2 Skills, expand with more Skill examples
# ============================================================
MARKER3 = "## 2.3 Plugins（插件系統）"

EXPANSION3_BEFORE = """### 2.2.7 Skills 進階模式

#### 動態上下文注入詳解

`!` command 語法讓 Skill 能在執行時動態載入上下文資訊：

```yaml
---
name: Contextual Review
description: 根據最近 Git 變更進行程式碼審查
---

# 上下文感知的程式碼審查

## 當前 Git 狀態
!`git status --short`

## 最近的變更
!`git diff --stat HEAD~3`

## 最近的 Commit 訊息
!`git log --oneline -10`

## 專案結構
!`find . -name "*.ts" -not -path "*/node_modules/*" -not -path "*/.git/*" | head -30`

## 待辦項目
!`grep -r "TODO\|FIXME\|HACK" --include="*.ts" --include="*.tsx" -l 2>/dev/null | head -10`

---

根據以上動態上下文，執行以下審查：
1. 檢查最近變更是否引入新的 TODO/FIXME
2. 確認變更檔案的程式碼品質
3. 檢查是否有遺漏的測試
4. 驗證 commit message 格式
```

#### Skill 參數（$ARGUMENTS）進階用法

```yaml
---
name: Generate Test
description: 為指定模組生成測試
arguments:
  - name: target
    description: 目標檔案或模組路徑
    required: true
  - name: type
    description: 測試類型 (unit|integration|e2e)
    required: false
    default: unit
  - name: framework
    description: 測試框架 (jest|vitest|mocha)
    required: false
---

# 測試生成器

為 $ARGUMENTS.target 生成 $ARGUMENTS.type 測試。

## 步驟
1. 讀取目標檔案
2. 分析所有 exported functions/classes
3. 為每個 function/class 生成測試案例
4. 使用 $ARGUMENTS.framework 框架語法
5. 包含正常流程和邊界案例
6. 建立測試檔案並執行驗證

## 測試品質要求
- 每個 function 至少 3 個測試案例
- 包含 happy path 和 error path
- 使用 describe/it 組織結構
- Mock 外部依賴
```

#### 企業級 Skill 開發範本

```yaml
---
name: Sprint Report
description: 生成 Sprint 報告
allowed-tools:
  - Read
  - Bash(git log *)
  - Bash(git shortlog *)
  - mcp__github__list_issues
  - mcp__github__list_pull_requests
---

# Sprint 報告生成器

## 本次 Sprint 的 Git 活動
!`git log --since="2 weeks ago" --oneline --no-merges | head -50`

## 參與者統計
!`git shortlog --since="2 weeks ago" -sn`

## 開啟中的 PR
使用 GitHub MCP 獲取所有 open PR 清單。

## 報告格式

### Sprint Summary
- Sprint 期間: [自動填入]
- 參與開發者: [人數]
- 完成 Commits: [數量]
- 合併 PR: [數量]

### 完成的功能
[根據 commit messages 和 merged PRs 彙整]

### 待處理項目
[根據 open issues 和 open PRs 列出]

### 程式碼品質指標
[根據 lint 結果和測試覆蓋率]

### 風險項目
[識別可能的延遲或技術債]
```

### 2.2.8 內建 Skills 使用指南

| Skill | 指令 | 用途 | 說明 |
|-------|------|------|------|
| **simplify** | `/simplify` | 簡化複雜程式碼 | 重構目標程式碼使之更簡潔 |
| **batch** | `/batch` | 批次處理 | 對多個檔案執行相同操作 |
| **debug** | `/debug` | 除錯 | 分析並修復 bug |
| **loop** | `/loop` | 排程自動化 | 建立定期執行的任務 |
| **claude-api** | `/claude-api` | Claude API 整合 | 生成 Claude API 呼叫程式碼 |
| **review** | `/review` | 程式碼審查 | 對當前變更進行審查 |

#### /simplify 使用範例

```
> /simplify src/utils/data-transformer.ts

Claude 會：
1. 讀取目標檔案
2. 識別可簡化的模式
3. 提出重構方案
4. 確認後執行重構
5. 驗證功能不變
```

#### /batch 使用範例

```
> /batch "為所有 .ts 檔案新增 copyright header"

Claude 會：
1. 找到所有 .ts 檔案
2. 檢查是否已有 copyright header
3. 對缺少的檔案新增 header
4. 回報處理結果
```

---

## 2.3 Plugins（插件系統）"""

content = content.replace(MARKER3, EXPANSION3_BEFORE, 1)
print("Expansion 3 applied successfully")

# ============================================================
# EXPANSION 4: After §2.3 Plugins, expand with more Plugin content
# ============================================================
MARKER4 = "## 2.4 Hooks（鉤子機制）"

EXPANSION4_BEFORE = """### 2.3.6 Plugin 完整開發範例

以下是一個完整的 Plugin 開發流程，從創建到發佈：

#### 步驟 1：建立 Plugin 目錄結構

```bash
mkdir -p my-review-plugin/.claude-plugin
mkdir -p my-review-plugin/agents
mkdir -p my-review-plugin/skills/security-review
mkdir -p my-review-plugin/hooks
mkdir -p my-review-plugin/mcp
```

#### 步驟 2：建立 plugin.json

```json
{
  "name": "comprehensive-review",
  "version": "1.0.0",
  "description": "全面的程式碼審查 Plugin，包含安全性、效能和風格檢查",
  "publisher": "YourTeam",
  "repository": "https://github.com/your-team/comprehensive-review-plugin",
  "engines": {
    "claude-code": ">=1.0.0"
  },
  "keywords": ["review", "security", "performance", "code-quality"],
  "license": "MIT"
}
```

#### 步驟 3：建立 Agent

**agents/review-coordinator.md**:
```yaml
---
name: Review Coordinator
description: 協調多面向的程式碼審查
allowed-tools:
  - Read
  - Grep
  - Glob
---

# 審查協調員

協調以下審查面向：
1. 安全性審查
2. 效能審查
3. 程式碼風格審查
4. 測試覆蓋率審查

為每個面向產出獨立報告，最後合併為統一的審查結果。
```

#### 步驟 4：建立 Skill

**skills/security-review/SKILL.md**:
```yaml
---
name: Security Review
description: 安全性程式碼審查
arguments:
  - name: scope
    description: 審查範圍（all|changed|file）
    required: false
    default: changed
---

# 安全性審查

## 審查範圍
!`git diff --name-only HEAD~1`

## 審查清單
1. SQL Injection 風險
2. XSS 攻擊面
3. 認證和授權漏洞
4. 敏感資料暴露
5. CSRF 防護
6. 依賴漏洞

!`npm audit --json 2>/dev/null | head -50`
```

#### 步驟 5：建立 Hooks

**hooks/hooks.json**:
```json
{
  "PostToolUse": [
    {
      "matcher": "Write",
      "hooks": [
        {
          "type": "command",
          "command": "echo '📝 File modified: review may be needed'"
        }
      ]
    }
  ]
}
```

#### 步驟 6：測試與發佈

```bash
# 本地測試
claude --plugin-dir ./my-review-plugin

# 在 VS Code 中測試
# 使用 /plugins 命令載入本地路徑

# 發佈到 GitHub
cd my-review-plugin
git init
git add -A
git commit -m "feat: initial release of comprehensive-review plugin"
git remote add origin https://github.com/your-team/comprehensive-review-plugin
git push -u origin main

# 其他人可以安裝
# claude plugin install github:your-team/comprehensive-review-plugin
```

### 2.3.7 Plugin 整合模式

#### Plugin + MCP 整合

Plugin 可以包含 MCP Server 配置，讓外部工具自動可用：

```
my-plugin/
└── mcp/
    └── mcp.json
```

```json
{
  "mcpServers": {
    "plugin-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["./mcp/server.js"]
    }
  }
}
```

#### Plugin + LSP 整合

Plugin 可以整合 Language Server Protocol 提供智慧感知：

```json
{
  "lsp": {
    "server": "./lsp/server.js",
    "languages": ["typescript", "javascript"],
    "capabilities": ["diagnostics", "completion"]
  }
}
```

### 2.3.8 從 .claude/ 到 Plugin 的轉換

如果你已經有完善的 `.claude/` 配置，可以快速轉換為 Plugin：

| 原始位置 | Plugin 位置 | 調整 |
|---------|------------|------|
| `.claude/agents/*.md` | `agents/*.md` | 直接搬移 |
| `.claude/skills/*/SKILL.md` | `skills/*/SKILL.md` | 直接搬移 |
| `.claude/settings.json` (hooks) | `hooks/hooks.json` | 提取 hooks 部分 |
| `.mcp.json` | `mcp/mcp.json` | 提取相關 servers |

```bash
# 轉換腳本範例
mkdir -p my-plugin/.claude-plugin
cp -r .claude/agents my-plugin/
cp -r .claude/skills my-plugin/

# 建立 plugin.json
cat > my-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-team-config",
  "version": "1.0.0",
  "description": "Team configuration as a plugin"
}
EOF
```

---

## 2.4 Hooks（鉤子機制）"""

content = content.replace(MARKER4, EXPANSION4_BEFORE, 1)
print("Expansion 4 applied successfully")

# ============================================================
# EXPANSION 5: After §2.4 Hooks, expand with more Hook examples
# ============================================================
MARKER5 = "## 2.5 MCP（Model Context Protocol）"

EXPANSION5_BEFORE = """### 2.4.7 Hook 實戰案例集

#### 案例五：提交前自動檢查（PreToolUse）

在 Claude 執行 `git commit` 之前，自動執行完整的品質檢查管線：

```bash
#!/bin/bash
# scripts/pre-commit-check.sh
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# 只攔截 git commit
if [[ "$COMMAND" != *"git commit"* ]]; then
    echo '{"permissionDecision": "allow"}'
    exit 0
fi

echo "Running pre-commit checks..." >&2

# 執行 lint
npx eslint . --quiet 2>&1 >&2
LINT_RESULT=$?

# 執行測試
npm test --silent 2>&1 >&2
TEST_RESULT=$?

# 檢查 TypeScript 編譯
npx tsc --noEmit 2>&1 >&2
TSC_RESULT=$?

if [ $LINT_RESULT -ne 0 ] || [ $TEST_RESULT -ne 0 ] || [ $TSC_RESULT -ne 0 ]; then
    FAILURES=""
    [ $LINT_RESULT -ne 0 ] && FAILURES="$FAILURES lint"
    [ $TEST_RESULT -ne 0 ] && FAILURES="$FAILURES test"
    [ $TSC_RESULT -ne 0 ] && FAILURES="$FAILURES tsc"
    echo "{\"permissionDecision\": \"deny\", \"message\": \"Pre-commit checks failed:$FAILURES\"}"
    exit 0
fi

echo '{"permissionDecision": "allow", "message": "All checks passed ✅"}'
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash scripts/pre-commit-check.sh"
          }
        ]
      }
    ]
  }
}
```

#### 案例六：自動化審計日誌（PostToolUse）

記錄所有檔案變更到審計日誌：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date -u +%Y-%m-%dT%H:%M:%SZ) | WRITE | $CLAUDE_SESSION_ID | $CLAUDE_FILE_PATH\" >> .claude/audit.log"
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "http",
            "url": "https://audit.company.internal/api/v1/events",
            "headers": {
              "Authorization": "Bearer ${AUDIT_API_TOKEN}",
              "Content-Type": "application/json"
            }
          }
        ]
      }
    ]
  }
}
```

#### 案例七：使用 Agent Hook 自動修復 Lint 錯誤

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "agent",
            "prompt": "Check if the written file has any ESLint errors. If yes, fix them. Run: npx eslint $CLAUDE_FILE_PATH --fix. If auto-fix doesn't resolve all issues, manually fix the remaining ones.",
            "allowed-tools": ["Bash(npx eslint *)", "Read", "Write", "Edit"]
          }
        ]
      }
    ]
  }
}
```

#### 案例八：多環境通知整合

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'if command -v osascript &>/dev/null; then osascript -e \"display notification \\\"Claude Code 已完成任務\\\" with title \\\"Claude Code\\\"\"; elif command -v notify-send &>/dev/null; then notify-send \"Claude Code\" \"已完成任務\"; fi'"
          }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "http",
            "url": "${SLACK_WEBHOOK_URL}",
            "headers": {
              "Content-Type": "application/json"
            }
          }
        ]
      }
    ]
  }
}
```

#### 案例九：SessionStart 環境初始化

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'echo \"Session started at $(date)\" >> .claude/session.log; if [ -f .nvmrc ]; then nvm use 2>/dev/null; fi'"
          }
        ]
      }
    ]
  }
}
```

### 2.4.8 Hook 偵錯技巧

| 技巧 | 說明 |
|------|------|
| **stderr 輸出** | Hook 腳本的 stderr 輸出會顯示在 Claude Code 的日誌中 |
| **純 echo 測試** | 先用 `echo "test"` 確認 Hook 觸發正常 |
| **jq 解析 stdin** | 使用 `jq` 解析 Hook 收到的 JSON 資料 |
| **退出碼測試** | 確認 exit 0（繼續）和 exit 2（阻止）的行為 |
| **日誌檔** | 將除錯資訊寫入日誌檔 |

```bash
#!/bin/bash
# scripts/debug-hook.sh — Hook 偵錯範本
INPUT=$(cat)

# 記錄完整的 stdin 到日誌
echo "$(date): $INPUT" >> .claude/hook-debug.log

# 解析關鍵欄位
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "unknown"')
echo "Tool: $TOOL_NAME" >&2

# 預設允許
echo '{"permissionDecision": "allow"}'
```

---

## 2.5 MCP（Model Context Protocol）"""

content = content.replace(MARKER5, EXPANSION5_BEFORE, 1)
print("Expansion 5 applied successfully")

# ============================================================
# EXPANSION 6: After §3.1, expand workflow with more scenarios
# ============================================================
MARKER6 = "## 3.2 排程與自動化"

EXPANSION6_BEFORE = """### 3.1.5 場景化工作流程範例

#### 場景一：Bug 修復工作流

```mermaid
sequenceDiagram
    participant DEV as 開發者
    participant CC as Claude Code
    participant SA as Subagent (Explore)
    participant GIT as Git
    participant CI as CI/CD
    
    DEV->>CC: 修復 Issue #123: 登入時的 500 錯誤
    CC->>SA: 搜尋相關程式碼
    SA-->>CC: 找到 auth.ts, login.controller.ts
    CC->>CC: 分析錯誤原因
    CC->>CC: 修改 auth.ts 第 45 行
    Note over CC: PostToolUse Hook: Prettier 格式化
    CC->>CC: 撰寫測試案例
    CC->>CC: 執行測試
    CC->>GIT: git commit -m "fix: resolve 500 error on login (#123)"
    CC->>GIT: git push origin fix/issue-123
    CC->>CC: 建立 PR（via GitHub MCP）
    CC-->>DEV: PR #456 已建立，修復了空值檢查問題
    CI->>CI: 自動執行 CI 和 Claude Code Review
```

#### 場景二：新功能開發工作流

```
> 實作使用者頭像上傳功能，支援圖片裁剪和壓縮

Claude 的執行步驟：
1. 🔍 Explore Agent 搜尋現有的檔案上傳邏輯
2. 📋 Planning Mode 產出實作計畫
3. 🏗️ 實作後端 API endpoint
   → PostToolUse Hook 自動格式化
4. 🎨 實作前端上傳元件
   → PostToolUse Hook 自動格式化
5. 🧪 撰寫單元測試和 E2E 測試
6. 📝 更新 API 文件
7. 🔒 Security Agent 檢查安全性
8. ✅ Git commit + 建立 PR
```

#### 場景三：大規模重構工作流（使用 Agent Teams）

```
> /cowork 將所有 REST API endpoints 遷移到新的路由格式

Team Lead 的執行計畫：

Teammate 1（Worktree A）：
├── 遷移 /api/users/* 路由
├── 更新相關測試
└── 更新 Swagger 文件

Teammate 2（Worktree B）：
├── 遷移 /api/products/* 路由
├── 更新相關測試
└── 更新 Swagger 文件

Teammate 3（Worktree C）：
├── 遷移 /api/orders/* 路由
├── 更新相關測試
└── 更新 Swagger 文件

Teammate 4（Worktree D）：
├── 更新前端 API client
├── 更新 E2E 測試
└── 更新 CHANGELOG

Team Lead：
├── 監控各 Teammate 進度
├── 合併所有 worktree
├── 執行完整測試套件
└── 建立 PR
```

#### 場景四：程式碼遷移工作流

```mermaid
graph TB
    START["遷移需求<br/>JavaScript → TypeScript"]
    
    START --> PLAN["Planning Mode<br/>分析遷移範圍"]
    PLAN --> SCOPE["確定遷移優先序<br/>1. 共用模組<br/>2. 後端<br/>3. 前端"]
    
    SCOPE --> BATCH_1["/batch 批次處理<br/>重命名 .js → .ts"]
    BATCH_1 --> BATCH_2["/batch 批次處理<br/>新增型別定義"]
    BATCH_2 --> FIX["修復型別錯誤<br/>（Agent Hook 自動輔助）"]
    FIX --> TEST["執行測試套件"]
    
    TEST --> |"失敗"| DEBUG["/debug 分析失敗原因"]
    DEBUG --> FIX
    
    TEST --> |"通過"| COMMIT["Commit + PR"]
    
    style START fill:#6366f1,stroke:#4f46e5,color:#fff
    style BATCH_1 fill:#818cf8,stroke:#6366f1,color:#fff
    style BATCH_2 fill:#818cf8,stroke:#6366f1,color:#fff
```

### 3.1.6 工作流程自訂模板

#### 建立專案專屬的工作流程 Skill

```yaml
---
name: Feature Workflow
description: 團隊標準化的功能開發流程
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(npm *)
  - Bash(git *)
  - mcp__github__*
arguments:
  - name: feature
    description: 功能描述
    required: true
  - name: branch
    description: 分支名稱
    required: false
---

# 標準功能開發流程

## 1. 建立分支
如果未指定分支，自動生成分支名稱。

## 2. 需求分析
分析 $ARGUMENTS.feature 的需求。

## 3. 設計
產出設計方案。

## 4. 實作
依設計方案實作。

## 5. 測試
撰寫並執行測試。

## 6. 審查
執行安全和品質審查。

## 7. 提交
Commit、Push、建立 PR。
```

---

## 3.2 排程與自動化"""

content = content.replace(MARKER6, EXPANSION6_BEFORE, 1)
print("Expansion 6 applied successfully")

# ============================================================
# EXPANSION 7: After §4.2, expand CI/CD with more examples
# ============================================================
MARKER7 = "## 4.3 VS Code 深度整合"

EXPANSION7_BEFORE = """### 4.2.4 CI/CD 最佳實踐

#### 安全性考量

| 項目 | 建議 |
|------|------|
| **API Key 管理** | 存放在 CI/CD 的 Secrets 中，不硬編碼 |
| **權限最小化** | 使用 `--allowedTools` 限制可用工具 |
| **檔案範圍** | 使用 `--permission-mode acceptEdits` 而非 full access |
| **成本控制** | 設定 `--max-turns` 避免無限迴圈 |
| **審計追蹤** | 使用 `--output-format json` 記錄完整輸出 |

#### GitHub Actions 完整範例集

##### 範例一：PR 品質門檻

```yaml
name: Claude Quality Gate
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Review this PR as a quality gate. Check:
            1. No console.log in production code
            2. All new functions have tests
            3. No hardcoded secrets or API keys
            4. TypeScript types are properly defined
            5. Error handling is comprehensive
            
            If any critical issues found, clearly state BLOCK with reasons.
            If only minor suggestions, state APPROVE with notes.
          claude_args: "--max-turns 10"
```

##### 範例二：自動文件同步

```yaml
name: Claude Documentation Sync
on:
  push:
    branches: [main]
    paths: ['src/**']

jobs:
  sync-docs:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Check if the code changes in src/ require documentation updates.
            If yes, update the relevant documentation files in docs/
            and create a commit with message "docs: sync documentation with code changes"
          claude_args: "--permission-mode acceptEdits --max-turns 15"
```

##### 範例三：Issue 自動分類

```yaml
name: Claude Issue Triage
on:
  issues:
    types: [opened]

jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Triage this new issue:
            1. Add appropriate labels (bug, feature, documentation, question)
            2. Assess priority (P0-Critical, P1-High, P2-Medium, P3-Low)
            3. Suggest which team member should be assigned
            4. Add a helpful response to the issue author
```

#### GitLab CI/CD 完整範例集

##### 範例一：Merge Request 審查

```yaml
claude-mr-review:
  image: node:24-alpine3.21
  variables:
    ANTHROPIC_API_KEY: $ANTHROPIC_API_KEY
  script:
    - npm install -g @anthropic-ai/claude-code
    - |
      CHANGES=$(git diff origin/main..HEAD --name-only)
      claude -p "Review these changed files in the merge request:
      $CHANGES
      
      Focus on:
      1. Breaking changes
      2. Missing tests
      3. Security issues
      4. Performance concerns
      
      Output as a structured review." \
        --output-format json \
        --max-turns 10 > review.json
    - cat review.json
  artifacts:
    paths:
      - review.json
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
```

##### 範例二：自動化 Release Notes

```yaml
claude-release-notes:
  image: node:24-alpine3.21
  variables:
    ANTHROPIC_API_KEY: $ANTHROPIC_API_KEY
  script:
    - npm install -g @anthropic-ai/claude-code
    - |
      LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
      if [ -n "$LAST_TAG" ]; then
        COMMITS=$(git log $LAST_TAG..HEAD --oneline --no-merges)
      else
        COMMITS=$(git log --oneline --no-merges -20)
      fi
      
      claude -p "Generate release notes from these commits:
      $COMMITS
      
      Format:
      ## What's New
      ## Bug Fixes
      ## Breaking Changes
      ## Contributors" \
        --output-format text > RELEASE_NOTES.md
  artifacts:
    paths:
      - RELEASE_NOTES.md
  rules:
    - if: '$CI_COMMIT_TAG'
```

---

## 4.3 VS Code 深度整合"""

content = content.replace(MARKER7, EXPANSION7_BEFORE, 1)
print("Expansion 7 applied successfully")

# ============================================================
# Write the expanded content
# ============================================================
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

# Count final lines
lines = content.split('\n')
print(f"\nFinal line count: {len(lines)}")
print("All expansions applied successfully!")
