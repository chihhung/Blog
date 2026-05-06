+++
date = '2026-05-06T20:59:33+08:00'
draft = false
title = 'GitHub Repo 建立教學手冊'
tags = ['教學', 'AI開發', 'github', 'devops']
categories = ['教學']
+++

# GitHub Repo 建立教學手冊 — 企業級 AI 資產知識庫

> **版本**：v2.0（2026-05-06）
> **適用對象**：技術主管 / 架構師 / 資深工程師 / DevOps 團隊
> **定位**：企業標準技術白皮書
> **參考範本**：[github/awesome-copilot](https://github.com/github/awesome-copilot)（32.2k+ Stars / 381+ Contributors）
> **最後審閱日期**：2026-05-06

---

## 目錄

- [第 1 章 概述與設計理念](#第-1-章-概述與設計理念)
  - [1.1 為何需要 AI 資產知識庫](#11-為何需要-ai-資產知識庫)
  - [1.2 awesome-copilot 設計理念分析](#12-awesome-copilot-設計理念分析)
  - [1.3 企業版策略差異](#13-企業版策略差異)
- [第 2 章 Repo 建立與初始設定](#第-2-章-repo-建立與初始設定)
  - [2.1 建立 Repository](#21-建立-repository)
  - [2.2 Branch Protection 設定](#22-branch-protection-設定)
  - [2.3 初始設定檔](#23-初始設定檔)
  - [2.4 初始化指令彙整](#24-初始化指令彙整)
- [第 3 章 客製化目錄結構設計](#第-3-章-客製化目錄結構設計)
  - [3.1 整體目錄結構](#31-整體目錄結構)
  - [3.2 各分類目錄說明](#32-各分類目錄說明)
  - [3.3 目錄結構對照圖](#33-目錄結構對照圖)
- [第 4 章 內容規範與模板設計](#第-4-章-內容規範與模板設計)
  - [4.1 檔案命名慣例](#41-檔案命名慣例)
  - [4.2 Frontmatter 規範](#42-frontmatter-規範)
  - [4.3 內容模板](#43-內容模板)
- [第 5 章 資料上架流程](#第-5-章-資料上架流程)
  - [5.1 整體流程](#51-整體流程)
  - [5.2 CONTRIBUTING.md 設計](#52-contributingmd-設計)
  - [5.3 Pull Request Template](#53-pull-request-template)
  - [5.4 Issue Template](#54-issue-template)
  - [5.5 Branch 策略](#55-branch-策略)
- [第 6 章 GitHub Actions 自動化 Workflow](#第-6-章-github-actions-自動化-workflow)
  - [6.1 Workflow 總覽](#61-workflow-總覽)
  - [6.2 內容驗證 Workflow](#62-內容驗證-workflow)
  - [6.3 PR 目標分支檢查](#63-pr-目標分支檢查)
  - [6.4 README 動態更新](#64-readme-動態更新)
  - [6.5 過時內容檢測](#65-過時內容檢測)
  - [6.6 貢獻者自動更新](#66-貢獻者自動更新)
  - [6.7 PR 自動標籤](#67-pr-自動標籤)
  - [6.8 建構腳本說明](#68-建構腳本說明)
- [第 7 章 探索與搜尋機制](#第-7-章-探索與搜尋機制)
  - [7.1 README 動態生成](#71-readme-動態生成)
  - [7.2 分類文件自動生成](#72-分類文件自動生成)
  - [7.3 Marketplace JSON](#73-marketplace-json)
  - [7.4 llms.txt — 機器可讀格式](#74-llmstxt--機器可讀格式)
  - [7.5 標籤系統設計](#75-標籤系統設計)
  - [7.6 awesome-copilot 網站與 Marketplace](#76-awesome-copilot-網站與-marketplace)
- [第 8 章 後續維運與治理](#第-8-章-後續維運與治理)
  - [8.1 CODEOWNERS 設定](#81-codeowners-設定)
  - [8.2 內容生命週期管理](#82-內容生命週期管理)
  - [8.3 過時檢測策略](#83-過時檢測策略)
  - [8.4 品質報告](#84-品質報告)
  - [8.5 安全掃描](#85-安全掃描)
  - [8.6 版本管理](#86-版本管理)
- [第 9 章 團隊導入與最佳實務](#第-9-章-團隊導入與最佳實務)
  - [9.1 導入路線圖](#91-導入路線圖)
  - [9.2 角色與權限設計](#92-角色與權限設計)
  - [9.3 Onboarding 流程](#93-onboarding-流程)
  - [9.4 知識分享文化建立](#94-知識分享文化建立)
  - [9.5 最佳實務](#95-最佳實務)
- [第 10 章 附錄：範本與 Checklist](#第-10-章-附錄範本與-checklist)
  - [10.1 完整目錄結構範本](#101-完整目錄結構範本)
  - [10.2 package.json 範本](#102-packagejson-範本)
  - [10.3 初始化指令 Checklist](#103-初始化指令-checklist)
  - [10.4 快速參考卡](#104-快速參考卡)
  - [10.5 常見問題（FAQ）](#105-常見問題faq)

---

## 第 1 章 概述與設計理念

### 1.1 為何需要 AI 資產知識庫

隨著企業全面導入 AI 工具（GitHub Copilot、Claude Code、Codex、Gemini）進行軟體開發，團隊在日常工作中持續產出大量有價值的 AI 資產。根據 GitHub 官方 awesome-copilot 專案的分類體系，這些資產可歸納為以下類型：

| 資產類型 | 說明 | 檔案慣例 | 企業範例 |
|---------|------|---------|---------|
| **Agents** | 專門化的 AI 代理，整合 MCP Server 與特定領域知識 | `*.agent.md` | Java 重構代理、安全掃描代理 |
| **Instructions** | 編碼標準與規範，依 `applyTo` 模式自動套用至特定檔案類型 | `*.instructions.md` | Spring Boot 編碼規範、Vue 元件標準 |
| **Skills** | 自包含的能力包，含指令 + 腳本 + 參考資料（遵循 [Agent Skills Specification](https://agentskills.io/specification)） | `{folder}/SKILL.md` | 單元測試生成器、API 文件產生器 |
| **Plugins** | 將 Agents + Commands + Skills 打包為可安裝套件，透過 `copilot plugin install` 安裝 | `{folder}/plugin.json` | 企業 Java 開發套件、前端 Vue 工具包 |
| **Hooks** | Copilot Coding Agent 會話期間的自動化觸發（session start/end、user prompt、tool usage） | `{folder}/hooks.json` | Session 初始化載入規範、工具守衛 |
| **Agentic Workflows** | 以 Markdown 撰寫的 AI 驅動 GitHub Actions 自動化（透過 `gh aw` 編譯） | `*.md`（含特定 Frontmatter） | 每日 Issue 報告、PR 自動審查 |
| **Cookbook** | Copy-paste-ready 的 Copilot API 操作配方 | 獨立目錄 | API 呼叫範例、錯誤處理 Hook |
| **Prompts** | 結構化的 AI 提示詞模板（企業自建分類） | `{folder}/prompt.md` | Code Review Prompt、逆向工程 Prompt |
| **教學手冊** | 技術教學文件（企業自建分類） | `*.md` | Claude Code 教學手冊、MCP 教學手冊 |
| **範本** | 可直接複用的文件與程式碼範本（企業自建分類） | `{folder}/*.md` | 系統分析範本、架構設計範本 |

若缺乏統一管理，這些資產將散落於個人電腦、聊天記錄或 Wiki 中，導致：

- **重複造輪子**：相同問題被不同團隊重複解決
- **品質不一**：缺乏標準化的品質控管
- **知識流失**：人員異動時資產隨之消失
- **無法追溯**：缺乏版本控管與變更記錄
- **無法機器消費**：AI Agent 無法系統性讀取與利用團隊知識

### 1.2 awesome-copilot 設計理念分析

GitHub 官方的 [awesome-copilot](https://github.com/github/awesome-copilot) 是目前最具代表性的 AI 資產知識庫（32.2k+ Stars、381+ Contributors），其設計理念值得企業深入參考：

{{< mermaid >}}
graph TB
    subgraph "awesome-copilot 架構（2026 最新）"
        A[Agents<br/>專門化代理] --> G[統一 Frontmatter<br/>YAML Metadata]
        B[Instructions<br/>編碼規範] --> G
        C[Skills<br/>能力包<br/>遵循 agentskills.io] --> G
        D[Plugins<br/>可安裝套件<br/>Claude Code spec] --> G
        E[Hooks<br/>自動化觸發] --> G
        F[Agentic Workflows<br/>AI GitHub Actions<br/>gh aw 編譯] --> G
        CB[Cookbook<br/>API 操作配方] --> G
    end

    G --> H[自動化建構<br/>npm run build<br/>README + marketplace.json]
    G --> I[品質驗證<br/>PR 自動檢查<br/>skill:validate / plugin:validate]
    G --> J[多管道探索]
    J --> J1[網站搜尋<br/>awesome-copilot.github.com]
    J --> J2[Marketplace<br/>copilot plugin install]
    J --> J3[llms.txt<br/>機器可讀格式]
    J --> J4[Learning Hub<br/>教學與指南]
    J --> J5[Tools<br/>MCP Servers + 開發工具]
    G --> K[貢獻流程<br/>staged → main<br/>AI Agent 快速通道 🤖🤖🤖]
{{< /mermaid >}}

**核心設計原則**：

1. **Convention over Configuration**：統一命名慣例（`*.agent.md`、`*.instructions.md`、`SKILL.md`），降低學習成本
2. **Metadata-driven**：所有內容使用 YAML Frontmatter 描述，支援自動化處理與驗證
3. **Staged Branch Strategy**：貢獻先進入 `staged` 分支，經 CI 驗證與人工審查後透過 `chore: publish from staged` 合併至 `main`
4. **Automated Quality Gate**：透過 GitHub Actions 自動驗證命名慣例、Frontmatter 完整性、Skill 結構、Plugin 格式
5. **Multi-channel Discovery**：
   - **網站**：[awesome-copilot.github.com](https://awesome-copilot.github.com/) 提供全文搜尋與過濾
   - **Plugin Marketplace**：`copilot plugin install <name>@awesome-copilot` 一鍵安裝
   - **llms.txt**：結構化清單供 AI Agent 消費
   - **Learning Hub**：涵蓋 Agents、Skills、Instructions、Hooks、Agentic Workflows、MCP Servers 的教學
   - **Tools**：MCP Servers 與開發者工具專區
6. **Plugin 生態系統**：採用 Claude Code spec 格式定義 `plugin.json`，支援本地 Plugin 與 External Plugin（GitHub / Git URL / npm / pip）
7. **MCP Server 整合**：內建 MCP Server 可直接從 repo 搜尋與安裝資源（需 Docker）
8. **AI Agent 貢獻最佳化**：PR 標題包含 `🤖🤖🤖` 可進入快速合併通道
9. **All-Contributors 認可**：支援 Instructions（🧭）、Agents（🎭）、Skills（🧰）、Workflows（⚡）、Plugins（🎁）等自訂貢獻類型

### 1.3 企業客製化策略

企業版知識庫在 awesome-copilot 基礎上，需加入以下考量：

| 面向 | awesome-copilot（開源社群） | 企業版（客製化） |
|------|---------------------------|----------------|
| **存取控制** | Public，任何人可貢獻 | Private / Internal，RBAC 權限控管 |
| **內容類型** | Agents / Instructions / Skills / Plugins / Hooks / Workflows / Cookbook | 加入教學手冊、範本、Prompt Template |
| **品質標準** | 社群 Review + AI Agent 快速通道 | 企業級 Review + 合規審查（無 AI 快速通道） |
| **Plugin 來源** | 接受 External Plugin（GitHub/npm/pip） | 僅接受內部來源，禁止外部未審核 Plugin |
| **命名規範** | 英文 | 支援中英文（目錄用中文、檔案用英文 slug） |
| **安全性** | 基礎 Secret Scan | 企業級安全掃描 + DLP + TruffleHog |
| **維運** | 社群維護 + github-actions[bot] 自動發佈 | 指定團隊 + CODEOWNERS + 定期稽核 |
| **探索管道** | 網站 + Marketplace + llms.txt + Learning Hub + Tools | 內部網站 + README 索引 + llms.txt |
| **MCP 整合** | 內建 MCP Server（Docker） | 可選，視安全政策決定 |
| **AI 協作** | 支援 AI Agent 貢獻（🤖🤖🤖 標記） | 需人工審查，AI 僅輔助撰寫 |

> **實務建議**：不要完全複製 awesome-copilot 的結構，應根據團隊實際需求取捨。小型團隊（< 20 人）建議先從 4-5 個核心分類開始（Agents / Instructions / Skills / Prompts / 教學手冊），再逐步擴展至 Plugins、Hooks、Workflows。

---

## 第 2 章 Repo 建立與初始設定

### 2.1 前置準備

#### 2.1.1 組織（Organization）建立

若公司尚未建立 GitHub Organization，需先完成：

```bash
# 步驟 1：前往 https://github.com/organizations/plan
# 步驟 2：選擇方案（建議 GitHub Enterprise）
# 步驟 3：填寫組織資訊
```

**組織設定建議**：

| 設定項目 | 建議值 | 說明 |
|---------|-------|------|
| Organization name | `{company}-ai-assets` | 清楚表達用途 |
| Default repository permission | `Read` | 最小權限原則 |
| Repository creation | `Members` | 允許成員建立 repo |
| Two-factor authentication | `Required` | 強制 2FA |
| Base permissions | `Read` | 基礎讀取權限 |

#### 2.1.2 Team 建立

```bash
# 建議的 Team 結構
├── ai-assets-admins          # 管理員（2-3 人）
├── ai-assets-maintainers     # 維護者（5-8 人，各領域代表）
├── ai-assets-reviewers       # 審查者（10-15 人，資深工程師）
└── ai-assets-contributors    # 貢獻者（全體開發人員）
```

### 2.2 Repository 建立

#### 2.2.1 建立指令

```bash
# 方式一：GitHub CLI（建議）
gh repo create {org}/ai-assets \
  --description "企業 AI 資產知識庫 — Agents / Skills / Instructions / Plugins / Hooks / Workflows / Prompts / 教學手冊" \
  --internal \
  --license MIT \
  --gitignore Node \
  --clone

# 方式二：透過 Web UI
# 前往 https://github.com/organizations/{org}/repositories/new
```

#### 2.2.2 Repository 設定

```bash
# Branch Protection Rules（main 分支）
gh api repos/{org}/ai-assets/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["validate-content","validate-readme"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":2,"dismiss_stale_reviews":true}' \
  --field restrictions=null

# 啟用 GitHub Advanced Security（若 Enterprise 方案）
gh api repos/{org}/ai-assets \
  --method PATCH \
  --field security_and_analysis='{"secret_scanning":{"status":"enabled"},"secret_scanning_push_protection":{"status":"enabled"}}'
```

**Branch Protection 設定項目**：

| 規則 | 設定 | 說明 |
|------|------|------|
| Require pull request reviews | 2 位審查者 | 確保內容品質 |
| Dismiss stale reviews | 啟用 | 程式碼變更後需重新審查 |
| Require status checks | 啟用 | 通過 CI 才可合併 |
| Require branches to be up to date | 啟用 | 確保分支為最新 |
| Restrict pushes | 僅 admins | 禁止直接推送至 main |
| Require signed commits | 啟用（建議） | 確認提交者身份 |

### 2.3 初始檔案建立

#### 2.3.1 README.md

```markdown
# 🤖 {Company} AI 資產知識庫

> 集中管理企業 AI 開發資產，加速團隊知識累積與 AI 協作效率

## 📋 快速導覽

| 分類 | 數量 | 說明 |
|------|------|------|
| 🤖 [Agents](agents/) | — | 專門化 AI 代理定義 |
| 📋 [Instructions](instructions/) | — | 編碼規範與標準（依 applyTo 模式自動套用） |
| 🎯 [Skills](skills/) | — | 自包含能力包（指令 + 腳本 + 資料） |
| 🔌 [Plugins](plugins/) | — | Agent + Skill + Command 整合套件 |
| 🪝 [Hooks](hooks/) | — | Copilot Coding Agent 自動化觸發動作 |
| ⚡ [Workflows](workflows/) | — | AI 驅動 GitHub Actions 自動化（Agentic Workflows） |
| 🍳 [Cookbook](cookbook/) | — | Copy-paste-ready API 操作配方 |
| 📝 [Prompts](prompts/) | — | 結構化 AI 提示詞模板 |
| 📖 [教學手冊](tutorials/) | — | 技術教學與工具使用指南 |
| 📄 [範本](templates/) | — | 可直接複用的文件與程式碼範本 |

## 🚀 如何使用

### 安裝 Plugin

```bash
# 透過 GitHub Copilot CLI
copilot plugin install <plugin-name>@{org}/ai-assets

# 若 Marketplace 未註冊，先執行一次
copilot plugin marketplace add {org}/ai-assets
copilot plugin install <plugin-name>@{org}/ai-assets
```

### 套用 Instruction

將 `.instructions.md` 檔案複製到專案的 `.github/` 目錄即可自動套用。

### 使用 Agent

在 VS Code Copilot Chat 中使用 `@agent-name` 呼叫已註冊的 Agent。

### 使用 Skill

在 Copilot Chat 中描述任務，Agent 會自動匹配並載入相關 Skill。

## 📖 學習資源

- [Learning Hub](docs/learning-hub/) — 入門教學與進階指南
- [Tools](docs/tools/) — MCP Servers 與開發者工具
- [llms.txt](llms.txt) — 機器可讀的知識庫摘要

## 📥 如何貢獻

請參閱 [CONTRIBUTING.md](CONTRIBUTING.md) 了解貢獻流程。所有 PR 請以 `staged` 分支為目標。

## 📊 貢獻者

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## 📜 授權

本專案採用 [MIT License](LICENSE)。
```

#### 2.3.2 .gitignore

```gitignore
# Dependencies
node_modules/
.pnp.*

# Build outputs
dist/
build/
.next/

# IDE
.vscode/settings.json
.idea/

# OS
.DS_Store
Thumbs.db

# Secrets (嚴禁提交)
.env
.env.local
*.key
*.pem

# Logs
*.log
npm-debug.log*
```

#### 2.3.3 .gitattributes

```gitattributes
# 統一換行符號
* text=auto eol=lf

# Markdown
*.md text eol=lf

# YAML
*.yml text eol=lf
*.yaml text eol=lf

# JSON
*.json text eol=lf

# Shell
*.sh text eol=lf

# Generated files (不納入 diff)
*.lock.yml linguist-generated=true
docs/README.*.md linguist-generated=true
```

#### 2.3.4 .editorconfig

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab
```

#### 2.3.5 LICENSE

建議採用 MIT License（內部使用）或公司自訂授權條款。

### 2.4 初始化指令彙整

```bash
# 完整初始化流程
cd ai-assets

# 建立分支策略
git checkout -b staged
git push -u origin staged

# 建立目錄結構（對齊 awesome-copilot + 企業自建分類）
mkdir -p agents instructions skills plugins hooks workflows cookbook
mkdir -p prompts tutorials templates
mkdir -p .github/workflows .github/ISSUE_TEMPLATE .github/plugin
mkdir -p docs eng scripts data _templates

# 建立初始檔案
touch agents/.gitkeep
touch instructions/.gitkeep
touch skills/.gitkeep
touch plugins/.gitkeep
touch hooks/.gitkeep
touch workflows/.gitkeep
touch cookbook/.gitkeep
touch prompts/.gitkeep
touch tutorials/.gitkeep
touch templates/.gitkeep

# 建立 AGENTS.md（供 AI Agent 理解專案結構）
cat > AGENTS.md << 'EOF'
## Project Overview
企業 AI 資產知識庫，參考 github/awesome-copilot 架構設計。

## Repository Structure
- agents/ — AI 代理定義（*.agent.md）
- instructions/ — 編碼規範（*.instructions.md）
- skills/ — 能力包（{folder}/SKILL.md）
- plugins/ — 可安裝套件（{folder}/plugin.json）
- hooks/ — 自動化觸發（{folder}/hooks.json）
- workflows/ — Agentic Workflows（*.md）
- cookbook/ — API 操作配方
- prompts/ — Prompt 模板
- tutorials/ — 教學手冊
- templates/ — 文件範本

## Setup Commands
npm ci
npm run build

## Development Workflow
All PRs must target the `staged` branch.
EOF

# 初始化 package.json
npm init -y
npm install gray-matter glob

# 提交
git add -A
git commit -m "chore: initialize AI assets repository structure"
git push origin staged

# 建立 PR 合併至 main
gh pr create --base main --head staged --title "chore: initialize repository" --body "Initial repository setup"
```

> **注意事項**：
> - 務必先建立 `staged` 分支再設定 Branch Protection，否則會導致無法推送初始提交
> - `.gitkeep` 檔案用於保留空目錄，待有實際內容後可移除
> - 建議第一次合併由 admin 直接執行，後續嚴格遵循 PR 流程
> - `AGENTS.md` 是供 AI Coding Agent（如 Copilot Coding Agent）理解專案結構的關鍵檔案

---

## 第 3 章 客製化目錄結構設計

### 3.1 整體目錄結構

```
ai-assets/
├── README.md                          # 主頁（動態生成表格索引）
├── CONTRIBUTING.md                    # 貢獻指南
├── AGENTS.md                          # AI Agent 專用專案說明
├── CODE_OF_CONDUCT.md                 # 行為準則
├── SECURITY.md                        # 安全政策
├── LICENSE                            # 授權條款
├── SUPPORT.md                         # 支援政策
├── package.json                       # 建構工具依賴
├── llms.txt                           # 機器可讀索引（供 AI Agent 消費）
├── context7.json                      # Context7 整合設定（選用）
├── .gitignore
├── .gitattributes
├── .editorconfig
├── .codespellrc                       # 拼字檢查設定
│
├── agents/                            # 🤖 AI 代理定義
│   ├── java-refactoring.agent.md
│   ├── security-scanner.agent.md
│   ├── code-reviewer.agent.md
│   └── ...
│
├── instructions/                      # 📋 編碼規範（依 applyTo 自動套用）
│   ├── java-spring-boot.instructions.md
│   ├── vue-typescript.instructions.md
│   ├── sql-database.instructions.md
│   └── ...
│
├── skills/                            # 🎯 能力包（遵循 agentskills.io spec）
│   ├── unit-test-generator/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   ├── references/
│   │   └── assets/
│   ├── api-doc-generator/
│   └── ...
│
├── plugins/                           # 🔌 可安裝套件（Claude Code spec）
│   ├── enterprise-java/
│   │   ├── .github/plugin/plugin.json
│   │   └── README.md
│   ├── frontend-vue/
│   └── external.json                  # 外部 Plugin 註冊表
│
├── hooks/                             # 🪝 自動化觸發
│   ├── session-init/
│   │   ├── README.md
│   │   ├── hooks.json
│   │   └── init-script.sh
│   ├── tool-guardian/
│   └── ...
│
├── workflows/                         # ⚡ Agentic Workflows（gh aw 編譯）
│   ├── pr-auto-review.md
│   ├── daily-issues-report.md
│   ├── weekly-comment-sync.md
│   └── ...
│
├── cookbook/                           # 🍳 API 操作配方
│   ├── error-recovery-hooks/
│   ├── copilot-api-examples/
│   └── ...
│
├── prompts/                           # 📝 Prompt 模板（企業自建）
│   ├── code-review/
│   │   └── prompt.md
│   ├── reverse-engineering/
│   │   └── prompt.md
│   ├── architecture-design/
│   │   └── prompt.md
│   └── ...
│
├── tutorials/                         # 📖 教學手冊（企業自建）
│   ├── claude-code-教學手冊.md
│   ├── copilot-ssdlc-教學手冊.md
│   ├── mcp-教學手冊.md
│   └── ...
│
├── templates/                         # 📄 文件範本（企業自建）
│   ├── system-analysis/
│   ├── architecture-design/
│   └── project-plan/
│
├── docs/                              # 📚 自動生成文件
│   ├── README.agents.md
│   ├── README.skills.md
│   ├── README.instructions.md
│   ├── learning-hub/                  # 學習中心
│   └── tools/                         # 工具與 MCP Server 索引
│
├── eng/                               # 🔧 建構腳本
│   ├── update-readme.mjs
│   ├── generate-marketplace.mjs
│   ├── validate-content.mjs
│   ├── fix-line-endings.sh
│   └── ...
│
├── scripts/                           # 🛠️ 公用腳本
│   ├── lint-frontmatter.mjs
│   └── ...
│
├── .schemas/                          # 📐 JSON Schema 定義
│   ├── plugin.schema.json
│   ├── hooks.schema.json
│   └── ...
│
├── .vscode/                           # 🖥️ VS Code 設定
│   ├── tasks.json                     # 快速新增 Agent/Skill 的 Task
│   └── settings.json
│
├── .github/                           # ⚙️ GitHub 配置
│   ├── workflows/
│   │   ├── validate-content.yml
│   │   ├── validate-readme.yml
│   │   ├── publish.yml
│   │   ├── staleness-report.yml
│   │   ├── contributors.yml
│   │   ├── security-scan.yml
│   │   └── ...
│   ├── ISSUE_TEMPLATE/
│   │   ├── new-agent.yml
│   │   ├── new-skill.yml
│   │   └── bug-report.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   ├── labeler.yml
│   └── plugin/
│       └── marketplace.json           # 自動生成
│
├── _templates/                        # 📋 空白模板（供貢獻者複製）
│   ├── agent.template.md
│   ├── instruction.template.md
│   ├── skill.template/
│   └── ...
│
└── data/                              # 📊 設定與 Metadata
    ├── config.json
    └── tags.json                      # 標準化標籤清單
```

### 3.2 各分類目錄說明

#### 3.2.1 agents/ — AI 代理定義

每個 Agent 為一個 `.agent.md` 檔案，使用 YAML Frontmatter 定義 metadata。根據 awesome-copilot 規範，`description` 欄位為必填（需用單引號包裹），建議包含 `model` 與 `tools` 欄位：

```
agents/
├── java-refactoring.agent.md          # Java 重構代理
├── security-scanner.agent.md          # 安全掃描代理
├── code-reviewer.agent.md             # Code Review 代理
├── database-optimizer.agent.md        # DB 優化代理
├── api-designer.agent.md              # API 設計代理
└── legacy-analyzer.agent.md           # 舊系統分析代理
```

#### 3.2.2 instructions/ — 編碼規範

每個 Instruction 為一個 `.instructions.md` 檔案。`description` 和 `applyTo` 皆為必填欄位，`applyTo` 使用 glob 模式指定自動套用的檔案類型：

```
instructions/
├── java-spring-boot.instructions.md   # applyTo: '**/*.java'
├── vue-typescript.instructions.md     # applyTo: '**/*.{vue,ts}'
├── sql-database.instructions.md       # applyTo: '**/*.sql'
├── python-fastapi.instructions.md     # applyTo: '**/*.py'
├── markdown-docs.instructions.md      # applyTo: '**/*.md'
└── dockerfile.instructions.md         # applyTo: '**/Dockerfile*'
```

#### 3.2.3 skills/ — 能力包

每個 Skill 為一個資料夾，包含 `SKILL.md` 及相關資源。遵循 [Agent Skills Specification](https://agentskills.io/specification)，`name` 必須與資料夾名稱一致（小寫 + 連字號，最多 64 字元），`description` 長度 10-1024 字元，單檔資源不超過 5MB：

```
skills/
├── unit-test-generator/
│   ├── SKILL.md                       # 能力說明與使用方式
│   ├── scripts/
│   │   ├── generate-junit5.sh
│   │   └── generate-vitest.sh
│   ├── references/
│   │   ├── junit5-patterns.md
│   │   └── testing-best-practices.md
│   └── assets/
│       └── test-template.java
├── api-doc-generator/
└── db-migration-helper/
```

#### 3.2.4 plugins/ — 可安裝套件

每個 Plugin 為一個資料夾，包含 `.github/plugin/plugin.json`（採用 Claude Code spec 格式）與 `README.md`。Plugin 內容透過宣告式定義引用 top-level 目錄中的 agents/commands/skills，CI 負責物化（materialize）到 Plugin 目錄中：

```
plugins/
├── enterprise-java/
│   ├── .github/plugin/plugin.json     # name, description, version, agents[], commands[], skills[]
│   └── README.md
├── frontend-vue/
│   ├── .github/plugin/plugin.json
│   └── README.md
└── external.json                      # 外部 Plugin 註冊表（GitHub/npm/pip/git）
```

#### 3.2.5 hooks/ — 自動化觸發

每個 Hook 為一個資料夾，包含 `README.md`（含 Frontmatter）與 `hooks.json`（Hook 事件設定）。支援的事件包括 session start、session end、user prompt、tool usage：

```
hooks/
├── session-init/
│   ├── README.md                      # name, description, tags
│   ├── hooks.json                     # hook 事件設定
│   └── init-script.sh                 # 可執行腳本（需 chmod +x）
├── tool-guardian/
│   ├── README.md
│   ├── hooks.json
│   └── guardian.sh
└── ...
```

#### 3.2.6 workflows/ — Agentic Workflows

每個 Workflow 為一個 `.md` 檔案（非 `.yml`），包含特殊 Frontmatter（`on`、`permissions`、`safe-outputs`）與自然語言指令。透過 `gh aw compile --validate` 進行本地驗證，CI 會阻擋 `.yml` / `.lock.yml` 檔案：

```
workflows/
├── pr-auto-review.md                  # AI 驅動 PR 自動審查
├── daily-issues-report.md             # 每日 Issue 報告
├── weekly-comment-sync.md             # 每週留言同步
└── ...
```

#### 3.2.7 cookbook/ — API 操作配方

Cookbook 提供 copy-paste-ready 的操作配方，如 Copilot API 呼叫範例、錯誤處理 Hook、PyInstaller 建構配方等：

```
cookbook/
├── error-recovery-hooks/              # 錯誤恢復 Hook 配方
├── copilot-api-examples/              # Copilot API 操作範例
└── ...
```

#### 3.2.8 prompts/ — Prompt 模板（企業自建分類）

```
prompts/
├── code-review/
│   └── prompt.md                      # Code Review 用 Prompt
├── reverse-engineering/
│   └── prompt.md                      # 逆向工程用 Prompt
├── architecture-design/
│   └── prompt.md                      # 架構設計用 Prompt
├── ssdlc/
│   ├── threat-modeling.md             # 威脅建模 Prompt
│   └── security-review.md            # 安全審查 Prompt
└── README.md                         # Prompt 使用指南
```

#### 3.2.9 tutorials/ — 教學手冊（企業自建分類）

```
tutorials/
├── claude-code-教學手冊.md
├── copilot-ssdlc-教學手冊.md
├── mcp-教學手冊.md
├── warp-教學手冊.md
├── ai-governance-教學手冊.md
└── README.md                         # 教學手冊索引
```

#### 3.2.10 templates/ — 文件範本（企業自建分類）

```
templates/
├── system-analysis/
│   ├── requirements-spec.md           # 需求規格書範本
│   └── use-case-spec.md              # 使用案例規格書範本
├── architecture-design/
│   ├── architecture-doc.md            # 架構設計文件範本
│   └── api-spec.md                   # API 規格書範本
├── project-plan/
│   └── migration-plan.md             # 架構轉換計畫範本
└── README.md                         # 範本索引
```

### 3.3 目錄結構對照圖

{{< mermaid >}}
graph LR
    subgraph "awesome-copilot 原生分類（7 類）"
        A1[agents/<br/>AI 代理]
        A2[instructions/<br/>編碼規範]
        A3[skills/<br/>能力包]
        A4[plugins/<br/>可安裝套件]
        A5[hooks/<br/>自動化觸發]
        A6[workflows/<br/>Agentic Workflows]
        A7[cookbook/<br/>API 配方]
    end

    subgraph "企業客製化新增（3 類）"
        B1[prompts/<br/>Prompt 模板]
        B2[tutorials/<br/>教學手冊]
        B3[templates/<br/>文件範本]
    end

    subgraph "基礎設施"
        C1[docs/<br/>自動生成文件]
        C2[eng/ + scripts/<br/>建構與公用腳本]
        C3[.github/<br/>CI/CD + 範本]
        C4[data/ + .schemas/<br/>設定與 Schema]
        C5[_templates/<br/>空白模板]
    end

    A4 -->|"Plugin Marketplace"| C3
    A6 -->|"gh aw compile"| C3
{{< /mermaid >}}

> **實務建議**：
> - awesome-copilot 的 `cookbook/` 與企業場景中的 `prompts/` 有部分重疊，但 cookbook 偏向 API 操作範例，prompts 偏向 AI 提示詞模板，建議分開維護
> - 初期建議先啟用 5-6 個核心目錄（Agents / Instructions / Skills / Prompts / 教學手冊 / Plugins），待團隊熟悉後再擴展至 Hooks、Workflows、Cookbook
> - 每個目錄必須有 `README.md` 說明該分類的用途與內容索引
> - `.schemas/` 目錄可存放 JSON Schema 供 IDE 驗證（如 plugin.json、hooks.json 的格式檢查）
> - `_templates/` 目錄存放空白模板，貢獻者可直接複製使用

---

## 第 4 章 內容規範與模板設計

### 4.1 檔案命名慣例

根據 awesome-copilot 最新的 AGENTS.md 與 CONTRIBUTING.md 規範，所有檔案必須遵循以下命名慣例：

| 內容類型 | 檔案格式 | 命名規則 | 範例 | 必填 Frontmatter |
|---------|---------|---------|------|-----------------|
| Agent | `*.agent.md` | 小寫 + 連字號 | `java-refactoring.agent.md` | `description`(必)、`name`(必)、`model`(強烈建議)、`tools`(建議) |
| Instruction | `*.instructions.md` | 小寫 + 連字號 | `vue-typescript.instructions.md` | `description`(必)、`applyTo`(必) |
| Skill | `{folder}/SKILL.md` | 資料夾名小寫 + 連字號（≤64 字元） | `unit-test-generator/SKILL.md` | `name`(必，需與資料夾名一致)、`description`(必，10-1024 字元) |
| Plugin | `{folder}/.github/plugin/plugin.json` | 資料夾名小寫 + 連字號 | `enterprise-java/plugin.json` | `name`(必)、`description`(必)、`version`(必) |
| Hook | `{folder}/README.md` + `hooks.json` | 資料夾名小寫 + 連字號 | `session-init/hooks.json` | `name`(必)、`description`(必)、`tags`(選) |
| Workflow | `*.md` | 小寫 + 連字號 | `daily-issues-report.md` | `name`(必)、`description`(必)、`on`(必)、`permissions`(必) |
| Prompt | `{folder}/prompt.md` | 資料夾名小寫 + 連字號 | `code-review/prompt.md` | `name`(必)、`description`(必) |
| 教學手冊 | `*.md` | 主題名 + 教學手冊 | `claude-code-教學手冊.md` | `name`(必)、`title`(必)、`description`(必) |
| 範本 | `*.md` | 描述性名稱 | `requirements-spec.md` | `name`(必)、`description`(必) |

> **重要規範**：所有 `description` 欄位的值必須用**單引號**包裹（如 `description: 'Java 重構代理'`），這是 awesome-copilot CI 驗證的硬性要求。

### 4.2 Frontmatter 規範

所有內容檔案必須包含 YAML Frontmatter，統一使用 `---` 分隔符號：

#### 4.2.1 Agent Frontmatter

```yaml
---
name: 'Java Refactoring Agent'          # 人類可讀名稱（必填）
description: 'Java 程式碼重構代理，支援 Spring Boot 專案的自動化重構與現代化'
model: 'copilot'                         # 建議指定模型（copilot / claude-code）
tools:                                   # 建議指定可用工具
  - codebase
  - terminal
  - github
version: '1.0.0'
author: '{author-name}'
tags: [java, spring-boot, refactoring]
created: '2026-05-06'
updated: '2026-05-06'
status: active                           # active | deprecated | draft
---
```

#### 4.2.2 Instruction Frontmatter

```yaml
---
description: 'Spring Boot 專案的編碼標準與規範'
applyTo: '**/*.java'                     # glob 模式（必填，需單引號）
tags: [java, spring-boot, coding-standards]
created: '2026-05-06'
updated: '2026-05-06'
---
```

#### 4.2.3 Skill Frontmatter

```yaml
---
name: unit-test-generator                # 必須與資料夾名一致（≤64 字元）
description: '自動生成 JUnit 5 / Vitest 單元測試，支援 mock 與 assertion 最佳實踐'
version: '1.0.0'
author: '{author-name}'
tags: [testing, junit5, vitest]
assets:
  - scripts/generate-junit5.sh
  - references/junit5-patterns.md
created: '2026-05-06'
updated: '2026-05-06'
---
```

> **Skill 特殊限制**：`description` 長度必須在 10-1024 字元之間；單一 asset 檔案大小不得超過 5MB；`name` 僅允許小寫字母、數字與連字號。

#### 4.2.4 Plugin Frontmatter（plugin.json）

```json
{
  "name": "enterprise-java",
  "description": "企業級 Java 開發 Plugin，整合 Spring Boot Agent、編碼規範與測試生成",
  "version": "1.0.0",
  "agents": ["java-refactoring"],
  "commands": [],
  "skills": ["unit-test-generator"]
}
```

#### 4.2.5 Workflow Frontmatter

```yaml
---
name: 'PR Auto Review'
description: 'AI 驅動的 Pull Request 自動審查工作流'
on:
  pull_request:
    types: [opened, synchronize]
permissions:
  pull-requests: write
  contents: read
safe-outputs:
  - pull_request.comment
---
```

#### 4.2.6 Prompt Frontmatter

```yaml
---
name: code-review-prompt
description: '結構化 Code Review Prompt，涵蓋安全性、效能與可維護性'
tags: [code-review, security, performance]
model: [copilot, claude-code, codex]    # 適用的 AI 工具
difficulty: intermediate                 # beginner | intermediate | advanced
created: '2026-05-06'
updated: '2026-05-06'
---
```

#### 4.2.7 教學手冊 Frontmatter

```yaml
---
name: claude-code-tutorial
title: 'Claude Code 教學手冊'
description: 'Claude Code 完整教學，涵蓋安裝、設定、SSDLC 整合與團隊導入'
tags: [claude-code, ai-development, ssdlc]
author: '{author-name}'
version: '1.0.0'
created: '2026-05-06'
updated: '2026-05-06'
status: active
---
```

### 4.3 內容模板

#### 4.3.1 Agent 模板

```markdown
---
name: '{Agent 顯示名稱}'
description: '{一行描述}'
model: 'copilot'
tools:
  - codebase
  - terminal
version: '1.0.0'
author: '{author}'
tags: [{tag1}, {tag2}]
created: '{date}'
updated: '{date}'
status: active
---

# {Agent 名稱}

## 概述

{Agent 的用途與適用場景}

## 知識來源

<knowledge_sources>
- {相關文件、API 文件、編碼規範}
</knowledge_sources>

## 工作流程

<workflow>
1. {步驟 1}
2. {步驟 2}
3. {步驟 3}
</workflow>

## 使用方式

```bash
# 在 VS Code Copilot Chat 中
@{agent-name} {指令}
```

## 限制與注意事項

- {限制 1}
- {限制 2}
```

#### 4.3.2 Instruction 模板

```markdown
---
name: {instruction-name}
description: '{一行描述}'
applyTo: '{glob-pattern}'
tags: [{tag1}, {tag2}]
created: '{date}'
updated: '{date}'
---

# {規範名稱}

## 適用範圍

本規範適用於符合 `{applyTo}` 模式的所有檔案。

## 編碼標準

### {標準 1}

{說明與範例}

### {標準 2}

{說明與範例}

## 範例

### ✅ 正確做法

```text
// Good example
```

### ❌ 錯誤做法

```text
// Bad example
```
```

#### 4.3.3 Skill 模板

```markdown
---
name: {skill-name}
description: '{一行描述（10-1024 字元）}'
version: '1.0.0'
author: '{author}'
tags: [{tag1}, {tag2}]
assets:
  - scripts/{script-file}
  - references/{ref-file}
created: '{date}'
updated: '{date}'
---

# {Skill 名稱}

## 用途

{Skill 的目的與適用場景}

## 使用時機

- {場景 1}
- {場景 2}

## 輸入

| 參數 | 類型 | 必填 | 說明 |
|------|------|------|------|
| {param1} | {type} | ✅ | {說明} |

## 輸出

{輸出說明}

## 範例

```bash
# 使用範例
```

## 參考資料

- {參考連結 1}
- {參考連結 2}
```

#### 4.3.4 Prompt 模板

```markdown
---
name: {prompt-name}
description: '{一行描述}'
tags: [{tag1}, {tag2}]
model: [{model1}, {model2}]
difficulty: intermediate
created: '{date}'
updated: '{date}'
---

# {Prompt 名稱}

## 適用場景

{何時使用此 Prompt}

## Prompt 內容

```
{完整的 Prompt 內容，可直接複製使用}
```

## 使用說明

1. {步驟 1}
2. {步驟 2}

## 預期輸出

{AI 應該產出什麼}

## 變體

### 變體 A：{簡化版}

```
{簡化版 Prompt}
```

### 變體 B：{進階版}

```
{進階版 Prompt}
```

## 注意事項

- {注意事項 1}
- {注意事項 2}
```

> **實務建議**：
> - 建議在 repo 根目錄的 `_templates/` 資料夾存放所有空白模板，貢獻者可直接複製使用（如 `_templates/agent.template.md`、`_templates/skill.template/`）
> - 每個模板應包含足夠的註解說明，降低填寫門檻
> - 所有字串值（尤其是 `description`、`applyTo`）一律使用**單引號**包裹，確保通過 CI 驗證
> - Plugin 的 `plugin.json` 使用 JSON 格式而非 YAML，可搭配 `.schemas/plugin.schema.json` 做 IDE 驗證
> - Frontmatter 的 `tags` 欄位建議制定標準標籤清單，避免同義詞混亂

---

## 第 5 章 資料上架流程

### 5.1 整體流程

{{< mermaid >}}
graph TD
    A[貢獻者準備內容] --> B[Fork / Branch]
    B --> C[建立 / 修改檔案]
    C --> D[本地驗證]
    D --> E[建立 Pull Request<br/>目標: staged 分支]
    E --> F{自動化檢查<br/>GitHub Actions}
    F -->|通過| G[人工審查<br/>Maintainer Review]
    F -->|失敗| C
    G -->|核准| H[合併至 staged]
    G -->|需修改| C
    H --> I[定期發佈<br/>staged → main]
    I --> J[自動更新<br/>README / Marketplace]
{{< /mermaid >}}

### 5.2 CONTRIBUTING.md 設計

```markdown
# 貢獻指南（Contributing Guide）

感謝您願意為 AI 資產知識庫貢獻內容！請依照以下流程進行。

## 🚦 快速開始

### 步驟 1：選擇內容類型

| 類型 | 目錄 | 檔案格式 | 說明 |
|------|------|---------|------|
| Agent | `agents/` | `*.agent.md` | AI 代理定義 |
| Instruction | `instructions/` | `*.instructions.md` | 編碼規範 |
| Skill | `skills/{name}/` | `SKILL.md` + 資源 | 能力包 |
| Plugin | `plugins/{name}/` | `plugin.json` + `README.md` | 整合套件 |
| Hook | `hooks/{name}/` | `hooks.json` + `README.md` | 自動化觸發 |
| Workflow | `workflows/` | `*.md` | AI GitHub Actions |
| Prompt | `prompts/{name}/` | `prompt.md` | Prompt 模板 |
| 教學手冊 | `tutorials/` | `*.md` | 技術教學 |
| 範本 | `templates/{category}/` | `*.md` | 文件範本 |

### 步驟 2：遵循命名慣例

- 檔案名稱使用**小寫 + 連字號**（如 `java-refactoring.agent.md`）
- 資料夾名稱使用**小寫 + 連字號**（如 `unit-test-generator/`）
- 教學手冊可使用中文（如 `claude-code-教學手冊.md`）

### 步驟 3：填寫 Frontmatter

所有內容必須包含 YAML Frontmatter，請參考 `_templates/` 目錄中的模板。

### 步驟 4：建立 Pull Request

- **目標分支**：`staged`（非 `main`）
- 使用 PR Template 填寫 Checklist
- 附上內容截圖或使用範例
- **AI Agent PR**：若由 AI Coding Agent（如 Copilot Coding Agent）產生的 PR，請在標題加上 🤖🤖🤖 標記，將獲得快速審查通道

### 步驟 5：等待審查

- 自動化檢查會在 PR 建立後自動執行
- 至少需要 2 位 Maintainer 核准（AI Agent PR 可降為 1 位）
- 若有修改建議，請在原 PR 上更新

## ⚠️ 重要規則

1. **禁止提交敏感資料**：API Key、密碼、內部 IP 等
2. **禁止提交付費服務推廣**：除非經管理員核准
3. **必須經過測試**：所有 Agent / Skill 需在 GitHub Copilot 中實際測試
4. **保持一致性**：遵循現有內容的風格與格式
```

### 5.3 Pull Request Template

建立 `.github/PULL_REQUEST_TEMPLATE.md`：

```markdown
## 📝 內容說明

<!-- 簡述此 PR 新增或修改的內容 -->

## 📋 內容類型

<!-- 請勾選適用的類型 -->

- [ ] 🤖 Agent
- [ ] 📋 Instruction
- [ ] 🎯 Skill
- [ ] 🔌 Plugin
- [ ] 🪝 Hook
- [ ] ⚡ Workflow
- [ ] 📝 Prompt
- [ ] 📖 教學手冊
- [ ] 📄 範本
- [ ] 🐛 Bug 修復
- [ ] 📝 文件更新

## ✅ 自我檢查清單

### 基本要求

- [ ] 已閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)
- [ ] 內容放置在正確的目錄
- [ ] 檔案遵循命名慣例
- [ ] 包含完整的 YAML Frontmatter
- [ ] 內容結構清晰（使用 Markdown 標題層級）

### 品質要求

- [ ] 已在 GitHub Copilot / Claude Code 中實際測試
- [ ] 無敏感資料（API Key / 密碼 / 內部 IP）
- [ ] 無付費服務推廣內容
- [ ] 範例可正確執行

### 合規要求

- [ ] 符合公司 AI 使用政策
- [ ] 無版權爭議內容
- [ ] PR 目標為 `staged` 分支

## 📸 截圖 / 範例輸出

<!-- 若適用，請附上使用截圖或範例輸出 -->

## 🔗 相關連結

<!-- 相關 Issue、文件、參考資料 -->
```

### 5.4 Issue Template

建立 `.github/ISSUE_TEMPLATE/new-agent.yml`：

```yaml
name: 🤖 新增 Agent
description: 提議新增一個 AI Agent
title: "[Agent] "
labels: ["agent", "new-content"]
body:
  - type: input
    id: agent-name
    attributes:
      label: Agent 名稱
      placeholder: "java-refactoring"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: 功能描述
      description: 此 Agent 要解決什麼問題？
    validations:
      required: true

  - type: dropdown
    id: category
    attributes:
      label: 分類
      options:
        - 程式開發
        - 程式碼審查
        - 安全掃描
        - 文件生成
        - 測試
        - 架構設計
        - 其他
    validations:
      required: true

  - type: textarea
    id: use-cases
    attributes:
      label: 使用場景
      description: 請列舉 2-3 個具體使用場景

  - type: checkboxes
    id: checklist
    attributes:
      label: 確認事項
      options:
        - label: 我已搜尋現有 Agent，確認無重複
          required: true
        - label: 我願意撰寫此 Agent 的內容
```

### 5.5 Branch 策略

{{< mermaid >}}
gitgraph
    commit id: "init"
    branch staged
    checkout staged
    commit id: "feature/new-agent"
    commit id: "feature/new-skill"
    checkout main
    merge staged id: "v1.0.0" tag: "release"
    checkout staged
    commit id: "fix/agent-typo"
    commit id: "feature/new-prompt"
    checkout main
    merge staged id: "v1.1.0" tag: "release"
{{< /mermaid >}}

| 分支 | 用途 | 保護規則 |
|------|------|---------|
| `main` | 正式發佈版本 | 禁止直接推送、需 2 位審查者、需通過 CI |
| `staged` | 整合測試分支，PR 目標 | 需 1 位審查者、需通過 CI |
| `feature/*` | 個人開發分支 | 無限制 |

> **實務建議**：
> - 建議每 1-2 週進行一次 `staged → main` 合併，搭配 Release Notes
> - 每次合併使用 Squash Merge，保持 `main` 的提交記錄乾淨
> - 可設定自動化 Workflow 在 `staged` 推送時自動建立 PR 至 `main`

---

## 第 6 章 GitHub Actions 自動化 Workflow

### 6.1 Workflow 總覽

{{< mermaid >}}
graph TD
    subgraph "PR 觸發"
        W1[validate-content.yml<br/>內容驗證]
        W2[validate-readme.yml<br/>README 一致性]
        W3[check-pr-target.yml<br/>PR 目標分支檢查]
        W4[label-pr-intent.yml<br/>PR 自動標籤]
        W10[validate-workflows.yml<br/>Agentic Workflow 驗證]
    end

    subgraph "合併觸發"
        W5[publish.yml<br/>staged → main 發佈]
        W6[update-readme.yml<br/>README 動態更新]
        W11[fix-line-endings.yml<br/>行尾字元正規化]
    end

    subgraph "定期排程"
        W7[staleness-report.yml<br/>過時內容檢測]
        W8[contributors.yml<br/>貢獻者清單更新]
        W9[quality-report.yml<br/>品質報告]
    end
{{< /mermaid >}}

### 6.2 內容驗證 Workflow

`.github/workflows/validate-content.yml`：

```yaml
name: 📋 Validate Content

on:
  pull_request:
    branches: [staged]
    paths:
      - 'agents/**'
      - 'instructions/**'
      - 'skills/**'
      - 'plugins/**'
      - 'hooks/**'
      - 'workflows/**'
      - 'prompts/**'
      - 'tutorials/**'
      - 'templates/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Validate file naming
        run: node eng/validate-naming.mjs

      - name: Validate frontmatter
        run: node eng/validate-frontmatter.mjs

      - name: Check for secrets
        run: node eng/check-secrets.mjs

      - name: Validate skill structure
        run: node eng/validate-skills.mjs

      - name: Validate plugin structure
        run: node eng/validate-plugins.mjs

      - name: Validate workflow syntax
        run: |
          # 驗證 Agentic Workflow 的 Frontmatter 格式
          # 阻擋 .yml / .lock.yml 檔案被提交到 workflows/ 目錄
          node eng/validate-workflows.mjs

      - name: Fix line endings
        run: bash eng/fix-line-endings.sh
```

### 6.3 PR 目標分支檢查

`.github/workflows/check-pr-target.yml`：

```yaml
name: 🎯 Check PR Target

on:
  pull_request:
    types: [opened, edited]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Verify PR targets staged branch
        if: github.event.pull_request.base.ref != 'staged'
        run: |
          echo "::error::PR 必須以 staged 分支為目標，而非 ${{ github.event.pull_request.base.ref }}"
          echo "請修改 PR 的 base branch 為 staged"
          exit 1
```

### 6.4 README 動態更新

`.github/workflows/update-readme.yml`：

```yaml
name: 📖 Update README

on:
  push:
    branches: [staged]
    paths:
      - 'agents/**'
      - 'instructions/**'
      - 'skills/**'
      - 'plugins/**'
      - 'prompts/**'
      - 'tutorials/**'
      - 'templates/**'

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Generate README tables
        run: node eng/update-readme.mjs

      - name: Generate category docs
        run: node eng/generate-docs.mjs

      - name: Commit changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md docs/
          git diff --staged --quiet || git commit -m "docs: auto-update README and category docs"
          git push
```

### 6.5 過時內容檢測

`.github/workflows/staleness-report.yml`：

```yaml
name: 📊 Staleness Report

on:
  schedule:
    - cron: '0 3 * * 1'  # 每週一 UTC 03:00
  workflow_dispatch:

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Generate staleness report
        run: node eng/staleness-report.mjs

      - name: Create issue if stale content found
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: "📊 每週過時內容報告"
          content-filepath: ./staleness-report.md
          labels: maintenance,staleness
```

### 6.6 貢獻者自動更新

`.github/workflows/contributors.yml`：

```yaml
name: 👥 Update Contributors

on:
  schedule:
    - cron: '0 3 * * 0'  # 每週日 UTC 03:00
  workflow_dispatch:

jobs:
  contributors:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Update contributors list
        uses: akhilmhdh/contributors-readme-action@v2.3.10
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 6.7 PR 自動標籤

`.github/workflows/label-pr.yml`：

```yaml
name: 🏷️ Label PR

on:
  pull_request:
    types: [opened]

jobs:
  label:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
      - name: Auto-label based on paths
        uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}

# 需搭配 .github/labeler.yml
```

`.github/labeler.yml`：

```yaml
agent:
  - changed-files:
    - any-glob-to-any-file: 'agents/**'

instruction:
  - changed-files:
    - any-glob-to-any-file: 'instructions/**'

skill:
  - changed-files:
    - any-glob-to-any-file: 'skills/**'

plugin:
  - changed-files:
    - any-glob-to-any-file: 'plugins/**'

hook:
  - changed-files:
    - any-glob-to-any-file: 'hooks/**'

workflow:
  - changed-files:
    - any-glob-to-any-file: 'workflows/**'

prompt:
  - changed-files:
    - any-glob-to-any-file: 'prompts/**'

tutorial:
  - changed-files:
    - any-glob-to-any-file: 'tutorials/**'

template:
  - changed-files:
    - any-glob-to-any-file: 'templates/**'
```

### 6.8 建構腳本說明

| 腳本 | 用途 | 觸發時機 |
|------|------|---------|
| `eng/update-readme.mjs` | 掃描所有內容，動態生成 README 表格 | Push to staged |
| `eng/generate-docs.mjs` | 生成各分類的 README 文件（`docs/README.*.md`） | Push to staged |
| `eng/generate-marketplace.mjs` | 生成 Plugin Marketplace JSON | Push to staged |
| `eng/validate-naming.mjs` | 驗證檔案命名是否符合慣例 | PR to staged |
| `eng/validate-frontmatter.mjs` | 驗證 YAML Frontmatter 完整性（單引號、必填欄位） | PR to staged |
| `eng/validate-skills.mjs` | 驗證 Skill 結構（agentskills.io spec 合規） | PR to staged |
| `eng/validate-plugins.mjs` | 驗證 Plugin 結構（Claude Code spec plugin.json） | PR to staged |
| `eng/validate-workflows.mjs` | 驗證 Agentic Workflow 格式（阻擋 `.yml` 提交） | PR to staged |
| `eng/check-secrets.mjs` | 掃描是否包含敏感資料 | PR to staged |
| `eng/fix-line-endings.sh` | 正規化行尾字元為 LF | PR to staged |
| `eng/staleness-report.mjs` | 生成過時內容報告 | 每週排程 |

> **實務建議**：
> - 所有建構腳本使用 ES Module（`.mjs`）撰寫，搭配 Node.js 20+
> - 建議使用 `gray-matter` npm 套件解析 YAML Frontmatter
> - 腳本應具備詳細的錯誤訊息，方便貢獻者自行修復問題
> - CI/CD 執行時間建議控制在 2 分鐘內，避免阻塞 PR 流程

---

## 第 7 章 探索與搜尋機制

### 7.1 README 動態生成

`eng/update-readme.mjs` 核心邏輯：

```javascript
import fs from 'fs/promises';
import path from 'path';
import matter from 'gray-matter';

const CATEGORIES = [
  { dir: 'agents', emoji: '🤖', label: 'Agents', ext: '.agent.md' },
  { dir: 'instructions', emoji: '📋', label: 'Instructions', ext: '.instructions.md' },
  { dir: 'skills', emoji: '🎯', label: 'Skills', file: 'SKILL.md' },
  { dir: 'plugins', emoji: '🔌', label: 'Plugins', file: 'plugin.json' },
  { dir: 'hooks', emoji: '🪝', label: 'Hooks', file: 'hooks.json' },
  { dir: 'workflows', emoji: '⚡', label: 'Workflows', ext: '.md' },
  { dir: 'prompts', emoji: '📝', label: 'Prompts', file: 'prompt.md' },
  { dir: 'tutorials', emoji: '📖', label: '教學手冊', ext: '.md' },
  { dir: 'templates', emoji: '📄', label: '範本', ext: '.md' },
];

async function generateReadme() {
  let summaryTable = '| 分類 | 數量 | 說明 |\n|------|------|------|\n';

  for (const cat of CATEGORIES) {
    const items = await scanCategory(cat);
    summaryTable += `| ${cat.emoji} [${cat.label}](${cat.dir}/) | ${items.length} | ${cat.label} |\n`;
  }

  // 更新 README.md 中的表格區塊
  const readme = await fs.readFile('README.md', 'utf-8');
  const updated = readme.replace(
    /<!-- SUMMARY-TABLE:START -->[\s\S]*<!-- SUMMARY-TABLE:END -->/,
    `<!-- SUMMARY-TABLE:START -->\n${summaryTable}\n<!-- SUMMARY-TABLE:END -->`
  );
  await fs.writeFile('README.md', updated);
}

async function scanCategory(category) {
  const dirPath = path.resolve(category.dir);
  const entries = await fs.readdir(dirPath, { withFileTypes: true });
  const items = [];

  for (const entry of entries) {
    if (entry.name === '.gitkeep' || entry.name === 'README.md') continue;

    if (entry.isFile() && category.ext && entry.name.endsWith(category.ext)) {
      const content = await fs.readFile(path.join(dirPath, entry.name), 'utf-8');
      const { data } = matter(content);
      items.push({ name: data.name || entry.name, description: data.description || '', path: `${category.dir}/${entry.name}` });
    }

    if (entry.isDirectory() && category.file) {
      const skillPath = path.join(dirPath, entry.name, category.file);
      try {
        const content = await fs.readFile(skillPath, 'utf-8');
        const { data } = matter(content);
        items.push({ name: data.name || entry.name, description: data.description || '', path: `${category.dir}/${entry.name}/` });
      } catch { /* skip */ }
    }
  }

  return items;
}

generateReadme();
```

### 7.2 分類文件自動生成

每個分類生成獨立的 `docs/README.{category}.md`，包含詳細的表格索引：

```markdown
<!-- docs/README.agents.md（自動生成，勿手動修改） -->

# 🤖 Agents 索引

| 名稱 | 說明 | 標籤 | 更新日期 |
|------|------|------|---------|
| [java-refactoring](../agents/java-refactoring.agent.md) | Java 程式碼重構代理 | `java`, `spring-boot` | 2026-05-06 |
| [security-scanner](../agents/security-scanner.agent.md) | 安全掃描代理 | `security`, `sast` | 2026-05-06 |
| ... | ... | ... | ... |
```

### 7.3 Marketplace JSON

`.github/plugin/marketplace.json`（自動生成）：

```json
{
  "version": "1.0.0",
  "generated": "2026-05-06T00:00:00Z",
  "plugins": [
    {
      "name": "enterprise-java",
      "description": "企業級 Java 開發整合套件",
      "version": "1.0.0",
      "source": "{org}/ai-assets/plugins/enterprise-java",
      "tags": ["java", "spring-boot", "enterprise"]
    }
  ],
  "external": []
}
```

### 7.4 llms.txt — 機器可讀格式

建立 `llms.txt` 供 AI Agent 直接讀取知識庫內容：

```text
# {Company} AI Assets Knowledge Base

## Agents
- java-refactoring: Java 程式碼重構代理，支援 Spring Boot 專案
- security-scanner: 安全掃描代理，整合 SAST/DAST
- code-reviewer: 自動化 Code Review 代理

## Instructions
- java-spring-boot: Spring Boot 編碼標準
- vue-typescript: Vue + TypeScript 元件規範

## Skills
- unit-test-generator: 自動生成 JUnit 5 / Vitest 單元測試
- api-doc-generator: 自動生成 OpenAPI 文件

## Prompts
- code-review: 結構化 Code Review Prompt
- reverse-engineering: 逆向工程分析 Prompt

## Tutorials
- claude-code-教學手冊: Claude Code 完整教學
- copilot-ssdlc-教學手冊: Copilot SSDLC 整合教學
```

### 7.5 標籤系統設計

建立標準化標籤清單 `data/tags.json`：

```json
{
  "languages": ["java", "python", "typescript", "vue", "sql", "bash"],
  "frameworks": ["spring-boot", "fastapi", "vue3", "react", "junit5"],
  "domains": ["security", "testing", "code-review", "refactoring", "architecture"],
  "tools": ["copilot", "claude-code", "codex", "gemini", "mcp"],
  "processes": ["ssdlc", "devops", "ci-cd", "reverse-engineering"],
  "levels": ["beginner", "intermediate", "advanced"]
}
```

> **實務建議**：
> - 標籤使用英文小寫 + 連字號，保持一致性
> - 定期審查標籤清單，合併同義詞（如 `unit-test` 與 `testing`）
> - `llms.txt` 可被 AI Agent 用於快速了解知識庫內容，建議保持簡潔
> - 若團隊規模較大，可考慮建置 Astro / Hugo 靜態網站提供搜尋功能

### 7.6 awesome-copilot 網站與 Marketplace

awesome-copilot 提供官方網站（awesome-copilot.github.com），內含以下探索機制，可作為企業內部知識庫網站的參考：

| 功能 | 說明 | 企業對應 |
|------|------|---------|
| **Plugin Marketplace** | 一鍵安裝 Plugin（`copilot plugin install {name}`） | 建置內部 Marketplace 頁面 |
| **Learning Hub** | 官方與社群學習資源索引 | `docs/learning-hub/` 目錄 |
| **Tools** | MCP Server、開發工具、IDE 整合索引 | `docs/tools/` 目錄 |
| **搜尋功能** | 依分類/標籤/關鍵字搜尋所有資產 | 可使用 GitHub Topics + 搜尋 |

```bash
# Plugin 安裝指令（awesome-copilot 格式）
copilot plugin install enterprise-java

# 加入 Marketplace 註冊
copilot marketplace add --source {org}/ai-assets/plugins/enterprise-java
```

---

## 第 8 章 後續維運與治理

### 8.1 CODEOWNERS 設定

建立 `.github/CODEOWNERS`：

```
# 預設審查者
* @{org}/ai-assets-maintainers

# 各分類負責人
/agents/               @{org}/agent-team
/instructions/         @{org}/standards-team
/skills/               @{org}/skill-team
/plugins/              @{org}/plugin-team
/hooks/                @{org}/agent-team
/workflows/            @{org}/devops-team
/prompts/              @{org}/prompt-team
/tutorials/            @{org}/docs-team
/templates/            @{org}/docs-team

# 基礎設施
/eng/                  @{org}/ai-assets-admins
/.github/              @{org}/ai-assets-admins
```

### 8.2 內容生命週期管理

{{< mermaid >}}
stateDiagram-v2
    [*] --> Draft: 建立內容
    Draft --> Active: PR 審核通過
    Active --> NeedsUpdate: 過時檢測
    NeedsUpdate --> Active: 更新內容
    NeedsUpdate --> Deprecated: 超過 90 天未更新
    Deprecated --> Active: 重新啟用
    Deprecated --> Archived: 確認不再需要
    Archived --> [*]
{{< /mermaid >}}

| 狀態 | Frontmatter `status` | 說明 | 處理方式 |
|------|---------------------|------|---------|
| 草稿 | `draft` | 尚未完成的內容 | 不顯示在 README 索引中 |
| 啟用 | `active` | 目前有效的內容 | 正常顯示與使用 |
| 需更新 | `needs-update` | 過時但仍可用 | Staleness Report 標記 |
| 已棄用 | `deprecated` | 已有替代方案 | 顯示棄用警告 |
| 已封存 | `archived` | 不再維護 | 移至 `_archived/` 目錄 |

### 8.3 過時檢測策略

`eng/staleness-report.mjs` 檢測邏輯：

| 檢測項目 | 閾值 | 動作 |
|---------|------|------|
| 最後更新日期 | > 90 天 | 標記為 `needs-update` |
| 最後更新日期 | > 180 天 | 標記為 `deprecated` |
| 參考連結失效 | 任何失效連結 | 列入報告 |
| Frontmatter 不完整 | 缺少必要欄位 | 列入報告 |
| 相依套件過時 | npm audit 有漏洞 | 高優先級通知 |

### 8.4 品質報告

每週自動生成的品質報告內容：

```markdown
# 📊 AI 資產知識庫品質報告

**生成日期**：2026-05-06
**掃描範圍**：全部 9 個分類

## 📈 總覽

| 指標 | 數值 |
|------|------|
| 總資產數 | 120 |
| Active | 105 |
| Needs Update | 10 |
| Deprecated | 5 |
| 本週新增 | 3 |
| 本週更新 | 7 |

## ⚠️ 需關注項目

### 過時內容（> 90 天未更新）
- `agents/legacy-analyzer.agent.md` — 最後更新 120 天前
- `prompts/batch-migration/prompt.md` — 最後更新 95 天前

### 失效連結
- `tutorials/mcp-教學手冊.md` 第 45 行：https://example.com/dead-link

### Frontmatter 不完整
- `skills/db-migration/SKILL.md`：缺少 `version` 欄位
```

### 8.5 安全掃描

```yaml
# .github/workflows/security-scan.yml
name: 🔒 Security Scan

on:
  pull_request:
    branches: [staged]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Secret scanning
        uses: trufflesecurity/trufflehog@main
        with:
          extra_args: --only-verified

      - name: Check for hardcoded credentials
        run: |
          # 掃描常見的敏感資料模式
          if grep -rn "AKIA[0-9A-Z]\{16\}\|sk-[a-zA-Z0-9]\{48\}\|ghp_[a-zA-Z0-9]\{36\}" \
            --include="*.md" --include="*.json" --include="*.yml" .; then
            echo "::error::偵測到可能的敏感資料！請移除後重新提交。"
            exit 1
          fi
```

### 8.6 版本管理

建議使用 GitHub Releases 進行版本管理：

```bash
# 建立 Release
gh release create v1.0.0 \
  --title "v1.0.0 — 初始發佈" \
  --notes "## 新增內容
  - 10 個 Agents
  - 15 個 Instructions
  - 5 個 Skills
  - 8 個 Prompt Templates
  - 3 份教學手冊"
```

> **實務建議**：
> - 使用 Semantic Versioning（SemVer）：新增內容為 Minor、修正為 Patch、結構變更為 Major
> - 每次 `staged → main` 合併時建立 Release，附上變更清單
> - 過時內容不要直接刪除，先標記 `deprecated` 觀察 30 天，確認無使用者後再封存
> - 安全掃描應設為 Required Status Check，未通過禁止合併

---

## 第 9 章 團隊導入與最佳實務

### 9.1 導入路線圖

{{< mermaid >}}
gantt
    title AI 資產知識庫導入路線圖
    dateFormat  YYYY-MM-DD
    section Phase 1：基礎建設
    建立 Repo 與目錄結構       :done, p1a, 2026-05-06, 3d
    設定 Branch Protection     :done, p1b, after p1a, 1d
    建立 CI/CD Workflow        :active, p1c, after p1b, 5d
    撰寫 CONTRIBUTING.md       :p1d, after p1c, 2d

    section Phase 2：種子內容
    遷移現有 Prompt/教學手冊    :p2a, after p1d, 7d
    建立 3-5 個核心 Agent       :p2b, after p1d, 7d
    建立 5-10 個 Instruction    :p2c, after p1d, 7d
    內部試用與回饋收集          :p2d, after p2a, 5d

    section Phase 3：全面推廣
    全員教育訓練               :p3a, after p2d, 3d
    開放全員貢獻               :p3b, after p3a, 1d
    建立定期 Review 機制        :p3c, after p3b, 3d
    設定品質報告排程            :p3d, after p3c, 2d

    section Phase 4：持續優化
    建立 Marketplace / 網站     :p4a, after p3d, 14d
    引入自動化品質評分          :p4b, after p3d, 14d
    跨團隊知識分享會            :p4c, after p3d, 30d
{{< /mermaid >}}

### 9.2 角色與權限設計

| 角色 | GitHub Team | 權限 | 職責 |
|------|------------|------|------|
| **管理員** | `ai-assets-admins` | Admin | Repo 設定、Workflow 管理、Release 發佈 |
| **維護者** | `ai-assets-maintainers` | Maintain | PR 審查、內容品質把關、過時內容處理 |
| **審查者** | `ai-assets-reviewers` | Write | 參與 PR 審查、提供技術建議 |
| **貢獻者** | `ai-assets-contributors` | Read + Fork | 提交內容、回報問題 |

### 9.3 Onboarding 流程

新成員加入團隊後的知識庫上手流程：

1. **閱讀 README.md**：了解知識庫結構與用途（5 分鐘）
2. **閱讀 CONTRIBUTING.md**：了解貢獻流程（10 分鐘）
3. **瀏覽現有內容**：找到與自己領域相關的 Agent / Instruction / Skill（15 分鐘）
4. **安裝一個 Plugin**：實際體驗使用流程（10 分鐘）
5. **建立第一個貢獻**：將個人常用的 Prompt 或 Instruction 提交為 PR（30 分鐘）

### 9.4 知識分享文化建立

| 機制 | 頻率 | 說明 |
|------|------|------|
| **AI Assets Show & Tell** | 每月 | 展示本月新增的優秀資產 |
| **Prompt 交流會** | 每兩週 | 分享高效 Prompt 設計技巧 |
| **季度回顧** | 每季 | 檢視知識庫成長、品質與使用數據 |
| **貢獻排行榜** | 每月 | 透過 all-contributors 呈現貢獻者 |
| **最佳資產獎** | 每季 | 票選最受歡迎 / 最實用的資產 |

### 9.5 最佳實務

#### 9.5.1 內容撰寫

1. **一個檔案解決一個問題**：避免大而全，保持單一職責
2. **包含具體範例**：所有 Agent / Skill / Prompt 必須包含可執行的範例
3. **說明適用場景**：明確說明何時該用、何時不該用
4. **標註限制與陷阱**：誠實記錄已知限制，避免使用者踩坑
5. **保持更新**：至少每 90 天審視一次內容是否仍然有效

#### 9.5.2 Prompt 設計

1. **結構化**：使用角色設定、背景、任務、約束、輸出格式
2. **可參數化**：使用 `{placeholder}` 讓使用者替換特定內容
3. **提供變體**：針對不同場景提供簡化版與進階版
4. **標註適用模型**：不同 AI 工具的 Prompt 效果可能不同
5. **附上預期輸出**：讓使用者知道正確的輸出長什麼樣

#### 9.5.3 常見反模式

| 反模式 | 說明 | 正確做法 |
|--------|------|---------|
| **垃圾資產** | 未經測試就提交的內容 | 所有內容必須實際測試後才提交 |
| **孤兒內容** | 無人維護的過時資產 | 指定 CODEOWNERS，定期審查 |
| **重複資產** | 功能重疊的多個 Agent/Skill | 提交前搜尋現有內容，考慮擴展而非新增 |
| **敏感洩漏** | Prompt 中包含內部資訊 | 使用佔位符，啟用 Secret Scan |
| **過度設計** | 一個 Agent 試圖解決所有問題 | 保持單一職責，必要時拆分 |

#### 9.5.4 企業擴展建議

| 團隊規模 | 建議做法 |
|---------|---------|
| < 20 人 | 4 個核心目錄（agents + instructions + prompts + tutorials）、1 位維護者 |
| 20-50 人 | 7 個目錄（+ skills + plugins + cookbook）、3 位維護者、每月 Review |
| 50-200 人 | 全部 10 個目錄、5-8 位維護者、每週 Review、建置 Plugin Marketplace |
| > 200 人 | 多 Repo 策略（依部門/技術領域拆分）、專職團隊、靜態網站（含 Learning Hub + 搜尋） |

---

## 第 10 章 附錄：範本與 Checklist

### 10.1 完整目錄結構範本

```
ai-assets/
├── README.md
├── CONTRIBUTING.md
├── AGENTS.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── LICENSE
├── .gitignore
├── .gitattributes
├── .editorconfig
├── .codespellrc
├── package.json
├── llms.txt
├── context7.json
├── agents/
│   ├── README.md
│   └── {name}.agent.md
├── instructions/
│   ├── README.md
│   └── {name}.instructions.md
├── skills/
│   ├── README.md
│   └── {name}/
│       ├── SKILL.md
│       ├── scripts/
│       ├── references/
│       └── assets/
├── plugins/
│   ├── README.md
│   ├── external.json
│   └── {name}/
│       ├── .github/plugin/plugin.json
│       └── README.md
├── hooks/
│   ├── README.md
│   └── {name}/
│       ├── README.md
│       ├── hooks.json
│       └── *.sh
├── workflows/
│   ├── README.md
│   └── {name}.md
├── cookbook/
│   ├── README.md
│   └── {name}/
├── prompts/
│   ├── README.md
│   └── {name}/
│       └── prompt.md
├── tutorials/
│   ├── README.md
│   └── {name}.md
├── templates/
│   ├── README.md
│   └── {category}/
│       └── {name}.md
├── _templates/
│   ├── agent.template.md
│   ├── instruction.template.md
│   ├── skill.template/
│   ├── prompt.template.md
│   └── tutorial.template.md
├── docs/
│   ├── README.agents.md
│   ├── README.skills.md
│   ├── README.instructions.md
│   ├── README.prompts.md
│   ├── learning-hub/
│   └── tools/
├── eng/
│   ├── update-readme.mjs
│   ├── generate-docs.mjs
│   ├── generate-marketplace.mjs
│   ├── validate-naming.mjs
│   ├── validate-frontmatter.mjs
│   ├── validate-skills.mjs
│   ├── validate-plugins.mjs
│   ├── validate-workflows.mjs
│   ├── check-secrets.mjs
│   ├── fix-line-endings.sh
│   └── staleness-report.mjs
├── scripts/
│   ├── lint-frontmatter.mjs
│   └── ...
├── .schemas/
│   ├── plugin.schema.json
│   ├── hooks.schema.json
│   └── ...
├── .vscode/
│   ├── tasks.json
│   └── settings.json
├── .github/
│   ├── workflows/
│   │   ├── validate-content.yml
│   │   ├── check-pr-target.yml
│   │   ├── update-readme.yml
│   │   ├── staleness-report.yml
│   │   ├── contributors.yml
│   │   ├── label-pr.yml
│   │   └── security-scan.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── new-agent.yml
│   │   ├── new-skill.yml
│   │   └── bug-report.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   ├── labeler.yml
│   └── plugin/
│       └── marketplace.json
└── data/
    ├── config.json
    └── tags.json
```

### 10.2 package.json 範本

```json
{
  "name": "ai-assets",
  "version": "1.0.0",
  "description": "企業 AI 資產知識庫",
  "type": "module",
  "scripts": {
    "build": "node eng/update-readme.mjs && node eng/generate-docs.mjs && node eng/generate-marketplace.mjs",
    "validate": "node eng/validate-naming.mjs && node eng/validate-frontmatter.mjs",
    "validate:skills": "node eng/validate-skills.mjs",
    "validate:plugins": "node eng/validate-plugins.mjs",
    "validate:workflows": "node eng/validate-workflows.mjs",
    "validate:secrets": "node eng/check-secrets.mjs",
    "validate:all": "npm run validate && npm run validate:skills && npm run validate:plugins && npm run validate:workflows && npm run validate:secrets",
    "fix:line-endings": "bash eng/fix-line-endings.sh",
    "report:staleness": "node eng/staleness-report.mjs"
  },
  "devDependencies": {
    "gray-matter": "^4.0.3",
    "glob": "^10.3.10"
  }
}
```

### 10.3 初始化指令 Checklist

```markdown
## 🚀 AI 資產知識庫初始化 Checklist

### 1. 組織與權限
- [ ] 建立 GitHub Organization（若尚未建立）
- [ ] 啟用 Two-Factor Authentication
- [ ] 建立 Teams（admins / maintainers / reviewers / contributors）
- [ ] 設定 Team 權限

### 2. Repository 建立
- [ ] 建立 Repository（Internal visibility）
- [ ] 選擇 License
- [ ] 建立 `staged` 分支
- [ ] 設定 Branch Protection（main + staged）
- [ ] 啟用 GitHub Actions

### 3. 檔案結構
- [ ] 建立所有目錄（agents / instructions / skills / plugins / hooks / workflows / cookbook / prompts / tutorials / templates）
- [ ] 建立支援目錄（_templates / .schemas / .vscode / scripts）
- [ ] 建立 README.md
- [ ] 建立 CONTRIBUTING.md
- [ ] 建立 AGENTS.md
- [ ] 建立 CODE_OF_CONDUCT.md
- [ ] 建立 SECURITY.md
- [ ] 建立 SUPPORT.md
- [ ] 建立 llms.txt
- [ ] 建立 .gitignore
- [ ] 建立 .gitattributes
- [ ] 建立 .editorconfig
- [ ] 建立 .codespellrc
- [ ] 建立 CODEOWNERS

### 4. 自動化
- [ ] 建立 validate-content.yml
- [ ] 建立 check-pr-target.yml
- [ ] 建立 validate-workflows.yml（Agentic Workflow 驗證）
- [ ] 建立 update-readme.yml
- [ ] 建立 staleness-report.yml
- [ ] 建立 contributors.yml
- [ ] 建立 label-pr.yml + labeler.yml
- [ ] 建立 security-scan.yml
- [ ] 建立 fix-line-endings.yml
- [ ] 建立 PR Template
- [ ] 建立 Issue Templates

### 5. 建構腳本
- [ ] 初始化 package.json
- [ ] 安裝 devDependencies
- [ ] 實作 update-readme.mjs
- [ ] 實作 generate-marketplace.mjs
- [ ] 實作 validate-naming.mjs
- [ ] 實作 validate-frontmatter.mjs
- [ ] 實作 validate-skills.mjs
- [ ] 實作 validate-plugins.mjs
- [ ] 實作 validate-workflows.mjs
- [ ] 實作 check-secrets.mjs
- [ ] 實作 fix-line-endings.sh

### 6. 種子內容
- [ ] 遷移現有 Prompt 模板
- [ ] 遷移現有教學手冊
- [ ] 建立 3-5 個核心 Agent
- [ ] 建立 5-10 個 Instruction
- [ ] 建立標準標籤清單（data/tags.json）

### 7. 推廣
- [ ] 撰寫團隊公告
- [ ] 舉辦啟動說明會
- [ ] 設定 Onboarding 流程
- [ ] 建立定期 Review 機制
```

### 10.4 快速參考卡

```
╔═══════════════════════════════════════════════════════════════╗
║                    AI 資產知識庫 — 快速參考卡                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📁 目錄結構                                                   ║
║  ├── agents/          → *.agent.md                            ║
║  ├── instructions/    → *.instructions.md                     ║
║  ├── skills/          → {name}/SKILL.md                       ║
║  ├── plugins/         → {name}/plugin.json                    ║
║  ├── hooks/           → {name}/hooks.json                     ║
║  ├── workflows/       → *.md                                  ║
║  ├── prompts/         → {name}/prompt.md                      ║
║  ├── tutorials/       → *-教學手冊.md                          ║
║  └── templates/       → {category}/{name}.md                  ║
║                                                               ║
║  🔀 貢獻流程                                                   ║
║  1. Fork / Branch                                             ║
║  2. 建立內容（使用 _templates/ 模板）                           ║
║  3. PR → staged 分支                                          ║
║  4. 自動化檢查 + 2 位審查者核准                                 ║
║  5. 合併至 staged → 定期發佈至 main                            ║
║                                                               ║
║  🏷️ 命名規則                                                   ║
║  • 檔案名：小寫 + 連字號（java-refactoring.agent.md）          ║
║  • 資料夾：小寫 + 連字號（unit-test-generator/）               ║
║  • 教學手冊：可用中文（claude-code-教學手冊.md）               ║
║                                                               ║
║  ⚠️ 禁止事項                                                   ║
║  • 禁止提交 API Key / 密碼 / 內部 IP                           ║
║  • 禁止直接推送至 main 分支                                    ║
║  • 禁止未經測試的內容                                          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### 10.5 常見問題（FAQ）

**Q1：我應該建立 Agent 還是 Instruction？**

- **Agent**：需要 AI 代理主動執行多步驟任務（如分析程式碼 → 建議重構 → 生成測試）
- **Instruction**：被動套用的編碼規範（如命名慣例、程式碼風格）

**Q2：PR 被 CI 擋下怎麼辦？**

查看 GitHub Actions 的錯誤訊息，常見原因：
- Frontmatter 缺少必要欄位 → 參考 `_templates/` 補齊
- 檔案命名不符慣例 → 改為小寫 + 連字號
- 偵測到敏感資料 → 移除 API Key 等敏感內容

**Q3：如何更新已發佈的內容？**

1. 建立新 Branch
2. 修改內容，更新 Frontmatter 中的 `updated` 日期
3. 建立 PR → staged

**Q4：教學手冊太大怎麼辦？**

- 單一檔案建議不超過 3000 行
- 若內容確實龐大，可拆分為系列文章（如 `part-1`、`part-2`）
- 在 `tutorials/README.md` 中建立索引

**Q5：可以引用外部資源嗎？**

可以，但需注意：
- 標註來源與授權
- 確認連結可存取
- 過時檢測會自動檢查連結有效性

**Q6：如何處理跨團隊的資產共享？**

- 使用 `tags` 欄位標記適用團隊
- 在 README 中建立「按團隊瀏覽」的索引
- 透過 CODEOWNERS 指定各團隊的維護範圍

**Q7：知識庫的內容可以用於生產環境嗎？**

- Agent / Instruction / Skill 可直接安裝使用
- Prompt 模板可直接複製使用
- 所有內容的品質由 Maintainer 把關

**Q8：如何衡量知識庫的使用成效？**

建議追蹤以下指標：
- 每月新增資產數
- PR 提交數與合併率
- 活躍貢獻者數
- Marketplace Plugin 安裝次數
- 團隊滿意度調查

**Q9：支援哪些 AI 工具？**

目前支援：
- GitHub Copilot（Agent / Instruction / Skill / Plugin / Hook / Workflow）
- Claude Code（Agent / Skill / Plugin — 採用 Claude Code spec 格式）
- OpenAI Codex（Prompt）
- Google Gemini（Prompt）

> **注意**：Plugin 格式已統一採用 Claude Code specification，同時相容 GitHub Copilot 與 Claude Code。

**Q10：如何確保內容不會被 AI 訓練使用？**

- Repository 設為 Internal / Private
- 在 `robots.txt` 中禁止爬蟲
- 與 GitHub 確認 Enterprise 方案的資料使用政策

---

> **文件結束**
> 
> 本教學手冊基於 [github/awesome-copilot](https://github.com/github/awesome-copilot) 的設計理念與架構，並針對企業需求進行客製化調整。
> 
> 如有任何問題或建議，請透過 GitHub Issue 提出。
