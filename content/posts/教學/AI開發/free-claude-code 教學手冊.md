+++
date = '2026-07-01T00:00:00+08:00'
draft = false
title = 'Free Claude Code 教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# free-claude-code 教學手冊

> **版本**：2026-07 ｜ **對應專案**：[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)
> **適用對象**：資深工程師 / 架構師 / DevOps / AI 開發團隊
> **授權**：MIT License
> **定位**：企業級 AI 輔助開發實戰手冊
> **語言**：繁體中文
> **文件更新日期**：2026 年 7 月 1 日

---

## 目錄

1. [概述（Overview）](#1-概述overview)
2. [系統整體架構（Architecture）](#2-系統整體架構architecture)
3. [安裝與環境建置（Installation）](#3-安裝與環境建置installation)
4. [核心設定（Configuration）](#4-核心設定configuration)
5. [模型整合（Multi-LLM Integration）](#5-模型整合multi-llm-integration)
   - 5.3 NVIDIA NIM
   - 5.4 OpenRouter
   - 5.5 DeepSeek
   - 5.6 LM Studio
   - 5.7 llama.cpp
   - 5.8 Ollama
   - 5.9 Google AI Studio（Gemini）
   - 5.10 Mistral La Plateforme
   - 5.11 Mistral Codestral
   - 5.12 OpenCode Zen
   - 5.13 OpenCode Go
   - 5.14 Wafer
   - 5.15 Kimi（Moonshot）
   - 5.16 Cerebras Inference
   - 5.17 Groq
   - 5.18 Fireworks AI
   - 5.19 Cloudflare
   - 5.20 Z.ai
6. [開發實戰（AI Development Use Cases）](#6-開發實戰ai-development-use-cases)
7. [SSDLC（安全開發流程）](#7-ssdlc安全開發流程)
8. [團隊導入策略（Team Adoption）](#8-團隊導入策略team-adoption)
9. [維運與監控（Operations）](#9-維運與監控operations)
10. [Smoke Testing 與啟動驗證（Startup Validation）](#10-smoke-testing-與啟動驗證startup-validation)
11. [升級與擴展（Upgrade & Scaling）](#11-升級與擴展upgrade--scaling)
12. [常見問題（FAQ）](#12-常見問題faq)
13. [最佳實務（Best Practices）](#13-最佳實務best-practices)
14. [CI/CD 整合](#14-cicd-整合)
15. [開發與貢獻指南（Development & Contributing）](#15-開發與貢獻指南development--contributing)
16. [範例 Prompt 集](#16-範例-prompt-集)
17. [檢查清單（Checklist）](#17-檢查清單checklist)
18. [Admin UI 管理介面](#18-admin-ui-管理介面)
19. [Codex CLI 整合（fcc-codex）](#19-codex-cli-整合fcc-codex)

---

## 1. 概述（Overview）

### 1.1 free-claude-code 是什麼

free-claude-code 是一個開源 **Anthropic Messages API 相容代理伺服器**（Proxy），以 Python FastAPI 建構，目前在 GitHub 上擁有超過 **37,900 顆星**（6,000+ forks）。它攔截 Claude Code CLI、Codex CLI、VS Code Extension 或 JetBrains ACP 發出的 API 請求，將其轉發至多種 LLM 後端，讓開發者能以**免費或低成本**方式使用 Claude Code 的完整開發體驗。

**核心特色：**

- **十八大 Provider 後端**：NVIDIA NIM、OpenRouter、DeepSeek、LM Studio、llama.cpp、Ollama，以及 Google AI Studio、Mistral、OpenCode、Wafer、Kimi、Cerebras、Groq、Fireworks AI、Cloudflare、Z.ai 等
- **Per-Model Routing**：可將 Opus / Sonnet / Haiku 各級流量路由至不同 Provider
- **Admin UI 管理介面**：Web 介面（`/admin`），可視化管理 Provider 設定、監控狀態
- **Claude Code `/model` Picker 原生支援**：透過 `/v1/models` 端點整合，含 `(no thinking)` 變體
- **Gateway Model Discovery**：設定 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` 啟用原生模型發現
- **Codex CLI 整合**：透過 `fcc-codex` 指令將 OpenAI Codex CLI 流量路由至各 Provider
- **Streaming、Tool Use、Thinking Block** 完整支援
- **Request Optimization**：自動以本地方式回應 Claude Code 的 trivial probe，節省延遲與配額
- **Startup Model Validation**：啟動時驗證已設定模型的可用性
- **Live Smoke Testing**：內建 Smoke Test 機制，逐 Provider 驗證端對端連通性
- **Discord / Telegram Bot** 遠端 Coding Session（含 `/stop`、`/clear`、`/stats` 指令）
- **Voice Note 語音輸入**（Whisper / NVIDIA NIM，支援 CPU / CUDA / NIM 三種裝置）

### 1.2 與 Claude Code 官方的差異

| 比較項目 | Claude Code 官方 | free-claude-code |
|---------|-----------------|-----------------|
| API 後端 | Anthropic API（付費） | 多模型 Proxy（免費/低成本） |
| 模型選擇 | Claude 系列 | 18 種 Provider 任意相容模型 |
| 計費方式 | 按 Token 付費 | 依 Provider 而定（可免費） |
| Tool Use | 完整支援 | 透過 Proxy 轉譯支援 |
| Thinking Block | 原生支援 | Proxy 正規化處理 |
| 部署方式 | SaaS | 自架 Proxy |
| 資料隱私 | 資料送至 Anthropic | 可選擇本地模型（完全離線） |
| Smoke Testing | 無 | 內建 Provider Smoke Test |
| 啟動驗證 | 無 | 啟動時自動驗證模型設定 |
| 管理介面 | 無 | Admin UI（`/admin`）Web 介面 |
| Codex CLI | 不支援 | `fcc-codex` 整合支援 |
| 模型發現 | Claude Code 內建 | Gateway Model Discovery |

### 1.3 適用場景

- **企業內部開發**：需要資料不外流，使用本地模型（LM Studio / Ollama）
- **個人開發者**：利用免費 NVIDIA NIM 點數或 OpenRouter 免費模型
- **AI Agent 團隊**：多模型路由，依任務類型分配不同模型
- **成本敏感專案**：透過 DeepSeek 等高性價比模型降低開發成本
- **逆向工程 / 升級專案**：利用大型模型進行 Legacy 程式碼分析
- **遠端協作**：透過 Discord / Telegram Bot 在行動裝置上進行 Coding Session

### 1.4 架構定位圖

```mermaid
graph TB
    subgraph "開發端"
        CLI[Claude Code CLI]
        COD[Codex CLI]
        VSC[VS Code Extension]
        JB[JetBrains ACP]
        BOT[Discord / Telegram Bot]
    end

    subgraph "Proxy Layer"
        FCC[free-claude-code<br/>FastAPI :8082]
        ADM[Admin UI<br/>:8082/admin]
    end

    subgraph "雲端 Provider"
        NIM[NVIDIA NIM]
        OR[OpenRouter]
        DS[DeepSeek]
        GEM[Google AI Studio]
        MST[Mistral]
        KIM[Kimi Moonshot]
        CER[Cerebras]
        GRQ[Groq]
        FWK[Fireworks AI]
        CLF[Cloudflare]
        ZAI[Z.ai]
        WAF[Wafer]
    end

    subgraph "本地 Provider"
        LMS[LM Studio]
        LC[llama.cpp]
        OL[Ollama]
    end

    CLI -->|Anthropic Messages API| FCC
    COD -->|OpenAI API| FCC
    VSC -->|Anthropic Messages API| FCC
    JB -->|Anthropic Messages API| FCC
    BOT -->|Anthropic Messages API| FCC
    ADM -.- FCC

    FCC --> NIM
    FCC --> OR
    FCC --> DS
    FCC --> GEM
    FCC --> MST
    FCC --> KIM
    FCC --> CER
    FCC --> GRQ
    FCC --> FWK
    FCC --> CLF
    FCC --> ZAI
    FCC --> WAF
    FCC --> LMS
    FCC --> LC
    FCC --> OL
```

> **實務建議**：初次導入建議先使用 NVIDIA NIM（免費點數）或 Google AI Studio（免費額度）驗證整體流程，確認可行後再切換至正式 Provider。

> **常見錯誤**：將 `ANTHROPIC_BASE_URL` 設為 `http://localhost:8082/v1`（多加了 `/v1`），正確應為 `http://localhost:8082`。

---

## 2. 系統整體架構（Architecture）

### 2.1 高階架構圖

```mermaid
graph LR
    subgraph "Client Layer"
        A1[Claude Code CLI]
        A1B[Codex CLI]
        A2[VS Code Extension]
        A3[JetBrains ACP]
        A4[Messaging Bot<br/>Discord / Telegram]
        A5[Voice Input<br/>Whisper]
    end

    subgraph "Proxy Core（FastAPI）"
        ADM[Admin UI<br/>/admin]
        B1[API Routes<br/>/v1/messages<br/>/v1/models<br/>/v1/messages/count_tokens]
        B2[Service Layer<br/>Request Optimization]
        B3[Model Router<br/>Opus / Sonnet / Haiku / Fallback]
        B4[SSE Stream Handler<br/>Thinking / Tool / Usage Normalization]
        B5[Rate Limiter<br/>Concurrency Control]
        B6[Auth Layer<br/>ANTHROPIC_AUTH_TOKEN]
        B7[Startup Validation<br/>Model & Provider Check]
    end

    subgraph "雲端 Provider Layer"
        C1[OpenAI Chat Transport<br/>NVIDIA NIM / Cerebras / Groq]
        C2[Anthropic Messages Transport<br/>OpenRouter / DeepSeek / Kimi / Wafer / Z.ai / Fireworks]
        C3[OpenAI Transport<br/>Google AI Studio / Mistral / OpenCode / Cloudflare]
    end

    subgraph "本地 Provider Layer"
        D1[LM Studio / llama.cpp / Ollama]
    end

    A1 --> B1
    A1B --> B1
    A2 --> B1
    A3 --> B1
    A4 --> B1
    A5 --> A4
    ADM -.- B1

    B1 --> B2
    B2 --> B3
    B3 --> B4
    B4 --> C1
    B4 --> C2
    B4 --> C3
    B4 --> D1
    B3 --> B5
    B1 --> B6
    B7 -.->|啟動時驗證| B3
```

### 2.2 專案結構

```
free-claude-code/
├── server.py              # ASGI entry point（Uvicorn 啟動入口）
├── api/                   # FastAPI routes、service layer、routing、optimizations
├── admin/                 # Admin UI 前端（Web 管理介面）
├── core/                  # 共用 Anthropic 協議 helpers 與 SSE 工具
├── providers/             # Provider transports、registry、rate limiting
├── messaging/             # Discord / Telegram adapters、sessions、voice
├── cli/                   # Package entry points 與 Claude/Codex process management
├── config/                # Settings、provider catalog、logging
├── smoke/                 # Live smoke tests（逐 Provider 端對端驗證）
├── tests/                 # Unit 與 contract tests
├── .env.example           # 環境變數範本（canonical reference）
├── pyproject.toml         # 套件定義與腳本
├── uv.lock                # 依賴鎖定檔
├── AGENTS.md              # Agentic coding 指引（與 CLAUDE.md 同步）
├── CLAUDE.md              # Claude Code agentic directive
└── PLAN.md                # 架構設計決策紀錄
```

### 2.3 Request Flow 說明

```mermaid
sequenceDiagram
    participant Client as Claude Code CLI/IDE
    participant Proxy as free-claude-code Proxy
    participant Router as Model Router
    participant Provider as LLM Provider

    Client->>Proxy: POST /v1/messages<br/>(Anthropic Messages API)
    Proxy->>Proxy: Auth 驗證（ANTHROPIC_AUTH_TOKEN）
    Proxy->>Proxy: Request Optimization<br/>（trivial probe 本地回應）
    Proxy->>Router: 解析 model name<br/>（claude-3-opus → MODEL_OPUS）
    Router->>Router: 選擇 Provider + Model
    Router->>Provider: 轉發請求<br/>（OpenAI Chat / Anthropic Messages）
    Provider-->>Proxy: SSE Stream Response
    Proxy->>Proxy: 正規化處理<br/>（thinking blocks / tool calls / usage）
    Proxy-->>Client: SSE Stream<br/>（Anthropic 格式）
```

### 2.4 Model Routing 策略

Model Routing 是 free-claude-code 的核心機制：

```
Claude Code 發送的 model name     →  Proxy 路由決策
─────────────────────────────────────────────
claude-3-opus-*                  →  MODEL_OPUS（若有設定）
claude-3.5-sonnet-*              →  MODEL_SONNET（若有設定）
claude-3-haiku-*                 →  MODEL_HAIKU（若有設定）
其他 / fallback                  →  MODEL（必須設定）
```

**路由繼承規則**：

- 若 `MODEL_OPUS` 未設定 → 自動使用 `MODEL`（fallback）
- 若 `ENABLE_OPUS_THINKING` 未設定 → 繼承 `ENABLE_MODEL_THINKING`
- Picker-safe ID 自動路由回原始 Provider/Model，無需額外 `.env` 修改

**混合 Provider 範例**：

```dotenv
NVIDIA_NIM_API_KEY="nvapi-your-key"
OPENROUTER_API_KEY="sk-or-your-key"

MODEL_OPUS="nvidia_nim/moonshotai/kimi-k2.5"
MODEL_SONNET="open_router/deepseek/deepseek-r1-0528:free"
MODEL_HAIKU="lmstudio/unsloth/GLM-4.7-Flash-GGUF"
MODEL="nvidia_nim/z-ai/glm4.7"
```

### 2.5 Request Optimization 機制

Proxy 內建多項請求最佳化，可在不消耗上游配額的情況下自動回應 Claude Code 的探測請求：

| 最佳化項目 | 環境變數 | 說明 |
|-----------|---------|------|
| 網路探測模擬 | `ENABLE_NETWORK_PROBE_MOCK=true` | 本地回應 Claude Code 的網路連線探測 |
| 標題生成跳過 | `ENABLE_TITLE_GENERATION_SKIP=true` | 跳過對話標題生成請求 |
| 建議模式跳過 | `ENABLE_SUGGESTION_MODE_SKIP=true` | 跳過建議模式相關請求 |
| 檔案路徑擷取模擬 | `ENABLE_FILEPATH_EXTRACTION_MOCK=true` | 本地模擬檔案路徑擷取 |
| 快速前綴偵測 | `FAST_PREFIX_DETECTION=true` | 加速請求前綴辨識 |

### 2.6 擴充方式

| 擴充類型 | 做法 |
|---------|-----|
| 新增 OpenAI 相容 Provider | 繼承 `OpenAIChatTransport` |
| 新增 Anthropic 相容 Provider | 繼承 `AnthropicMessagesTransport` |
| 註冊 Provider 中繼資料 | 修改 `config.provider_catalog` 並於 `providers.registry` 新增 factory wiring |
| 新增 Messaging 平台 | 實作 `MessagingPlatform` interface（位於 `messaging/`） |

> **實務建議**：企業若需整合內部私有模型（如 vLLM），建議走 `AnthropicMessagesTransport` 路線，因多數企業 LLM Gateway 已支援此協議。

> **常見錯誤**：嘗試用 Docker 打包部署 — 專案目前明確拒絕 Docker 整合 PR，建議用 systemd / PM2 管理。

---

## 3. 安裝與環境建置（Installation）

### 3.0 快速安裝（Quick Install）

若只需快速體驗，可使用官方安裝腳本一鍵完成安裝與啟動：

**macOS / Linux：**

```bash
curl -fsSL https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/install.sh | sh
```

**Windows PowerShell：**

```powershell
irm https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/install.ps1 | iex
```

安裝完成後，執行 `fcc-init` 建立設定檔，再執行 `fcc-server` 啟動 Proxy。

> **注意**：快速安裝適合個人快速評估；企業環境建議採用 3.2 節的完整手動安裝流程。

### 3.1 系統需求

| 項目 | 最低需求 | 建議版本 |
|-----|---------|---------|
| 作業系統 | Windows 10+ / Ubuntu 20.04+ / macOS 12+ | 最新穩定版 |
| Python | 3.14 | 3.14（專案指定，見 `.python-version`） |
| uv（套件管理） | 最新版 | 最新版（透過 `uv self update` 更新） |
| Node.js | 18+（Claude Code CLI 需要） | 22 LTS |
| Claude Code CLI | 2.1.126+（Model Picker 支援） | 最新版 |
| 記憶體 | 4 GB | 8 GB+（本地模型需 16 GB+） |

> **注意**：Python 3.14 為專案硬性要求。專案使用了 Python 3.14 的語法特性（例如 `except TypeError, ValueError:` 多型別例外語法），這些特性僅在 3.14 正式版中支援。

### 3.2 安裝步驟

#### Step 1：安裝 Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
```

#### Step 2：安裝 uv 與 Python 3.14

**Windows PowerShell：**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv self update
uv python install 3.14
```

**macOS / Linux：**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
uv python install 3.14
```

#### Step 3：Clone 專案

```bash
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code
```

#### Step 4：設定環境變數

```bash
# Linux / macOS
cp .env.example .env

# Windows PowerShell
Copy-Item .env.example .env
```

編輯 `.env` 檔，至少設定以下項目：

```dotenv
# 選擇一個 Provider（以 NVIDIA NIM 為例）
NVIDIA_NIM_API_KEY="nvapi-your-key"
MODEL="nvidia_nim/z-ai/glm4.7"

# Proxy 認證 Token（自定密碼，Claude Code 會送回同樣的值）
ANTHROPIC_AUTH_TOKEN="freecc"
```

> **安全提醒**：`ANTHROPIC_AUTH_TOKEN` 建議使用自訂的強密碼。若留空，則僅適用於本地 / 私有測試環境。

#### Step 5：啟動 Proxy

**方式一（套件指令，推薦）：**

```bash
uv tool install git+https://github.com/Alishahryar1/free-claude-code.git
fcc-init      # 建立 ~/.config/free-claude-code/.env（從內建範本）
fcc-server    # 啟動 Proxy（等同 free-claude-code 指令）
```

**方式二（直接從原始碼執行）：**

```bash
uv run uvicorn server:app --host 0.0.0.0 --port 8082
```

> `fcc-init` 會從專案根目錄的 `.env.example` 建立使用者設定檔，路徑為 `~/.config/free-claude-code/.env`。
>
> `fcc-server` 是新的標準啟動指令，等同舊版的 `free-claude-code`。

#### Step 6：啟動 Claude Code

**推薦方式（`fcc-claude`）：**

```bash
fcc-claude
```

`fcc-claude` 會自動讀取 Admin UI 設定的 Port 與 Auth Token，並設定 `CLAUDE_CODE_AUTO_COMPACT_WINDOW=190000`，無須手動設定環境變數。

**手動方式（PowerShell）：**

```powershell
$env:ANTHROPIC_AUTH_TOKEN="freecc"; $env:ANTHROPIC_BASE_URL="http://localhost:8082"; claude
```

**手動方式（Bash）：**

```bash
ANTHROPIC_AUTH_TOKEN="freecc" ANTHROPIC_BASE_URL="http://localhost:8082" claude
```

### 3.3 驗證安裝

```bash
# 確認 Proxy 運行中
curl http://localhost:8082/v1/models

# 預期回應：列出所有可用模型的 JSON
```

**Admin UI 驗證：**

在瀏覽器開啟 `http://127.0.0.1:8082/admin`，確認可正常顯示 Web 管理介面，且已設定的 Provider 狀態顯示為「連線中」。

### 3.4 環境建置架構

```mermaid
graph TD
    subgraph "開發環境建置流程"
        S1[安裝 Node.js 22 LTS] --> S2[安裝 Claude Code CLI]
        S2 --> S3[安裝 uv + Python 3.14]
        S3 --> S4[Clone free-claude-code<br/>或使用 Quick Install]
        S4 --> S5[fcc-init 建立設定檔<br/>或手動編輯 .env]
        S5 --> S6[fcc-server 啟動 Proxy :8082]
        S6 --> S6A[Startup Validation<br/>自動驗證模型設定]
        S6A --> S6B[確認 Admin UI<br/>:8082/admin]
        S6B --> S7[執行 fcc-claude<br/>或手動設定 ANTHROPIC_BASE_URL]
        S7 --> S8[啟動 Claude Code]
        S8 --> S9[執行 /model 驗證]
    end
```

> **實務建議**：使用 `fcc-claude` 取代手動設定環境變數，可避免設定錯誤並自動啟用對話歷史壓縮。

> **常見錯誤**：忘記在 `.env` 設定 `ANTHROPIC_AUTH_TOKEN`，導致認證失敗。

---

## 4. 核心設定（Configuration）

`.env.example` 是所有變數的完整清單（canonical reference）。以下分類說明最常修改的設定。

### 4.1 ANTHROPIC_BASE_URL 設定

| 客戶端 | 設定方式 |
|-------|---------|
| CLI（Bash） | `export ANTHROPIC_BASE_URL="http://localhost:8082"` |
| CLI（PowerShell） | `$env:ANTHROPIC_BASE_URL="http://localhost:8082"` |
| VS Code Extension | `settings.json` 設定（見 [4.5 節](#45-vs-code-extension-設定)） |
| JetBrains ACP | `installed.json` 設定（見 [4.6 節](#46-jetbrains-acp-設定)） |

> ⚠️ **不要** 在 URL 末尾加上 `/v1`，正確格式為 `http://localhost:8082`

### 4.2 API Key 管理

```dotenv
# 雲端 Provider Keys
NVIDIA_NIM_API_KEY=""          # 從 build.nvidia.com/settings/api-keys 取得
OPENROUTER_API_KEY=""          # 從 openrouter.ai/keys 取得
DEEPSEEK_API_KEY=""            # 從 platform.deepseek.com/api_keys 取得
GEMINI_API_KEY=""              # 從 aistudio.google.com/apikey 取得
MISTRAL_API_KEY=""             # 從 console.mistral.ai/api-keys 取得
CODESTRAL_API_KEY=""           # 從 console.mistral.ai（Codestral 專用）取得
OPENCODE_API_KEY=""            # 從 opencode.ai 取得（Zen 與 Go 共用）
WAFER_API_KEY=""               # 從 wafer.ai 取得
KIMI_API_KEY=""                # 從 platform.moonshot.ai/api-keys 取得
CEREBRAS_API_KEY=""            # 從 cloud.cerebras.ai 取得
GROQ_API_KEY=""                # 從 console.groq.com/keys 取得
FIREWORKS_API_KEY=""           # 從 fireworks.ai/api-keys 取得
CLOUDFLARE_API_TOKEN=""        # 從 dash.cloudflare.com/profile/api-tokens 取得
CLOUDFLARE_ACCOUNT_ID=""       # 從 Cloudflare Dashboard 右側取得
ZAI_API_KEY=""                 # 從 api.z.ai 取得

# 本地 Provider（不需要 Key）
LM_STUDIO_BASE_URL="http://localhost:1234/v1"
LLAMACPP_BASE_URL="http://localhost:8080/v1"
OLLAMA_BASE_URL="http://localhost:11434"
```

**安全建議：**

- 不要將 API Key 提交至版本控制
- 使用 `.gitignore` 排除 `.env`
- 生產環境使用環境變數注入（而非檔案）
- 定期輪換 API Key

### 4.3 多模型切換（Model Routing）

```dotenv
# Fallback 模型（必須設定）
MODEL="nvidia_nim/z-ai/glm4.7"

# 各級模型（選填，未設定則繼承 MODEL）
MODEL_OPUS=
MODEL_SONNET=
MODEL_HAIKU=

# Thinking 模式控制
ENABLE_MODEL_THINKING=true
ENABLE_OPUS_THINKING=
ENABLE_SONNET_THINKING=
ENABLE_HAIKU_THINKING=
```

**Model 名稱格式**：`provider_id/model/name`

**合法 Provider ID**：`nvidia_nim` | `open_router` | `deepseek` | `lmstudio` | `llamacpp` | `ollama`

**Claude Code Model Picker**：

Claude Code 2.1.126+ 支援透過 `/model` 指令直接在 CLI 中選擇模型。Proxy 的 `/v1/models` 端點會列出所有已設定 Provider 的可用模型。每個模型另提供 `(no thinking)` 變體，當模型不支援 thinking 或遇到 adaptive-thinking 請求失敗時可選用。Picker-safe ID 會自動路由回正確的 Provider/Model，無需修改 `.env` 或另行啟動。

### 4.4 Smoke Model 覆寫

Proxy 啟動時會針對每個已設定的 Provider 執行一次 Smoke Test。若 `MODEL` / `MODEL_*` 指向的模型不適合 Smoke Test（例如付費模型），可透過以下變數覆寫 Smoke Test 使用的模型：

```dotenv
FCC_SMOKE_MODEL_NVIDIA_NIM=
FCC_SMOKE_MODEL_OPEN_ROUTER=
FCC_SMOKE_MODEL_DEEPSEEK=
FCC_SMOKE_MODEL_LMSTUDIO=
FCC_SMOKE_MODEL_LLAMACPP=
FCC_SMOKE_MODEL_OLLAMA=
```

### 4.5 VS Code Extension 設定

打開 VS Code Settings JSON，加入：

```json
{
  "claudeCode.environmentVariables": [
    { "name": "ANTHROPIC_BASE_URL", "value": "http://localhost:8082" },
    { "name": "ANTHROPIC_AUTH_TOKEN", "value": "freecc" }
  ]
}
```

設定後重新載入 Extension。首次可能仍會出現登入畫面，選擇 Anthropic Console 路徑即可，後續流量由 Proxy 處理。

### 4.6 JetBrains ACP 設定

編輯 Claude ACP 設定檔：

- **Windows**：`C:\Users\%USERNAME%\AppData\Roaming\JetBrains\acp-agents\installed.json`
- **Linux/macOS**：`~/.jetbrains/acp.json`

在 `acp.registry.claude-acp` 下設定環境變數：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:8082",
    "ANTHROPIC_AUTH_TOKEN": "freecc"
  }
}
```

修改後重新啟動 IDE。

### 4.7 Rate Limit 與 Timeout

```dotenv
PROVIDER_RATE_LIMIT=1          # 每個視窗內的最大請求數
PROVIDER_RATE_WINDOW=3         # Rate limit 視窗（秒）
PROVIDER_MAX_CONCURRENCY=5     # 最大並行請求數
HTTP_READ_TIMEOUT=300          # 讀取 timeout（秒）
HTTP_WRITE_TIMEOUT=10          # 寫入 timeout（秒）
HTTP_CONNECT_TIMEOUT=10        # 連線 timeout（秒）
```

> **實務建議**：免費 Provider 建議降低 concurrency（1-2），本地模型可根據硬體提高。`HTTP_READ_TIMEOUT` 預設為 300 秒，因部分大型模型回應時間較長。

### 4.8 安全與診斷

```dotenv
# Proxy 認證 Token
ANTHROPIC_AUTH_TOKEN=

# 基本診斷 Logging
LOG_RAW_API_PAYLOADS=false              # 記錄原始 API 請求/回應
LOG_RAW_SSE_EVENTS=false                # 記錄原始 SSE 事件
LOG_API_ERROR_TRACEBACKS=false          # 記錄 API 錯誤堆疊（可能洩漏請求衍生資料）
LOG_RAW_MESSAGING_CONTENT=false         # 記錄 Messaging 文字預覽（可能洩漏使用者內容）
LOG_RAW_CLI_DIAGNOSTICS=false           # 記錄 Claude CLI stderr 與非 JSON stdout
LOG_MESSAGING_ERROR_DETAILS=false       # 記錄 Messaging 錯誤與 CLI 錯誤字串

# 進階 Debug Flags
DEBUG_PLATFORM_EDITS=false              # 除錯平台編輯操作
DEBUG_SUBAGENT_STACK=false              # 除錯子 Agent 堆疊
```

> ⚠️ **安全警告**：Raw logging 可能暴露 prompt、tool arguments、路徑與模型輸出。僅在本地 debug 時開啟，生產環境務必關閉。

### 4.9 Web Tools

```dotenv
ENABLE_WEB_SERVER_TOOLS=true
WEB_FETCH_ALLOWED_SCHEMES=http,https
WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false
```

這些工具會從 Proxy 發出 outbound HTTP 請求。

> ⚠️ 除非在受控環境中，否則保持 `WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false`。

### 4.10 Proxy 設定（企業防火牆）

```dotenv
# Per-provider proxy 支援（http 與 socks5 協議）
# 格式：http://username:password@host:port
NVIDIA_NIM_PROXY=""
OPENROUTER_PROXY=""
LMSTUDIO_PROXY=""
LLAMACPP_PROXY=""
```

> **常見錯誤**：企業網路需要 HTTP Proxy 才能存取外部 API，但忘記設定此項導致連線失敗。

### 4.11 Agent Config（Messaging Bot 專用）

以下設定影響 Discord / Telegram Bot 的 Claude Code 執行環境：

```dotenv
CLAUDE_WORKSPACE="./agent_workspace"    # Claude Code 工作目錄
ALLOWED_DIR=""                          # 允許存取的目錄路徑
CLAUDE_CLI_BIN="claude"                 # Claude CLI 執行檔路徑
FAST_PREFIX_DETECTION=true              # 加速請求前綴辨識
ENABLE_NETWORK_PROBE_MOCK=true          # 本地回應網路探測
ENABLE_TITLE_GENERATION_SKIP=true       # 跳過標題生成
ENABLE_SUGGESTION_MODE_SKIP=true        # 跳過建議模式
ENABLE_FILEPATH_EXTRACTION_MOCK=true    # 本地模擬檔案路徑擷取
```

### 4.12 Messaging Rate Limit

```dotenv
MESSAGING_RATE_LIMIT=1     # Messaging 每視窗最大請求數
MESSAGING_RATE_WINDOW=1    # Messaging rate limit 視窗（秒）
```

### 4.13 環境變數分類速查表

| 類別 | 關鍵變數 | 必填 |
|------|---------|------|
| 核心 | `MODEL`、`ANTHROPIC_AUTH_TOKEN`、`PORT` | ✅（PORT 選填，預設 8082） |
| 模型路由 | `MODEL_OPUS`、`MODEL_SONNET`、`MODEL_HAIKU` | ❌ |
| Thinking | `ENABLE_MODEL_THINKING`、`ENABLE_*_THINKING` | ❌ |
| 雲端 Provider Key（原有） | `NVIDIA_NIM_API_KEY`、`OPENROUTER_API_KEY`、`DEEPSEEK_API_KEY` | 至少一個 |
| 雲端 Provider Key（新增） | `GEMINI_API_KEY`、`MISTRAL_API_KEY`、`CODESTRAL_API_KEY`、`OPENCODE_API_KEY`、`WAFER_API_KEY`、`KIMI_API_KEY`、`CEREBRAS_API_KEY`、`GROQ_API_KEY`、`FIREWORKS_API_KEY`、`CLOUDFLARE_API_TOKEN`、`ZAI_API_KEY` | 至少一個 |
| Cloudflare 專用 | `CLOUDFLARE_ACCOUNT_ID` | Cloudflare 必填 |
| 本地 Provider | `LM_STUDIO_BASE_URL`、`LLAMACPP_BASE_URL`、`OLLAMA_BASE_URL` | ❌ |
| Model Discovery | `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` | ❌ |
| 對話壓縮 | `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | ❌（fcc-claude 自動設定） |
| Rate Limit | `PROVIDER_RATE_LIMIT`、`PROVIDER_RATE_WINDOW`、`PROVIDER_MAX_CONCURRENCY` | ❌ |
| Timeout | `HTTP_READ_TIMEOUT`、`HTTP_WRITE_TIMEOUT`、`HTTP_CONNECT_TIMEOUT` | ❌ |
| Proxy | `NVIDIA_NIM_PROXY`、`OPENROUTER_PROXY`、`LMSTUDIO_PROXY`、`LLAMACPP_PROXY` | ❌ |
| Smoke Test | `FCC_SMOKE_MODEL_*` | ❌ |
| Messaging | `MESSAGING_PLATFORM`、`MESSAGING_RATE_LIMIT`、`MESSAGING_RATE_WINDOW` | ❌ |
| Agent | `CLAUDE_WORKSPACE`、`ALLOWED_DIR`、`CLAUDE_CLI_BIN` | ❌ |
| 安全 | `LOG_RAW_*`、`DEBUG_*`、`WEB_FETCH_ALLOW_PRIVATE_NETWORKS` | ❌ |
| 語音 | `VOICE_NOTE_ENABLED`、`WHISPER_DEVICE`、`WHISPER_MODEL`、`HF_TOKEN` | ❌ |

### 4.14 Admin UI 設定

Admin UI 是 free-claude-code 內建的 Web 管理介面，Proxy 啟動後自動可用：

```text
http://127.0.0.1:8082/admin
```

**主要功能：**

- 透過圖形介面編輯各 Provider API Key 與設定參數
- 驗證設定後即時套用，無需重啟 Proxy
- 即時檢視各 Provider 連通性狀態（綠燈 / 紅燈）
- 設定 Model Routing 分級（OPUS / SONNET / HAIKU / FALLBACK）
- 設定 Discord / Telegram Bot 訊息整合
- 設定語音轉文字後端（Voice Transcription）
- 頁尾顯示目前設定檔路徑

> **安全注意**：Admin UI 預設僅限本機迴環位址（`127.0.0.1`）存取，不對外公開。企業環境若需遠端管理，應透過 SSH Tunnel 或 VPN，避免直接暴露管理介面。

### 4.15 Gateway Model Discovery

設定以下環境變數可啟用 Claude Code 原生模型發現功能，讓 `/model` Picker 直接列出 Proxy 支援的所有模型：

```dotenv
CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1
```

啟用後，Claude Code 的 `/model` 選擇器會自動查詢 `GET /v1/models`，顯示所有已設定 Provider 的可用模型清單，包含 `(no thinking)` 變體，無需手動維護模型列表。

> **注意**：此功能需要 Claude Code CLI 2.1.126 或更新版本。

---

## 5. 模型整合（Multi-LLM Integration）

### 5.1 Provider 總覽

```mermaid
graph LR
    FCC[free-claude-code<br/>Proxy]

    subgraph "雲端 Provider（原有）"
        NIM[NVIDIA NIM<br/>免費點數]
        OR[OpenRouter<br/>多模型路由]
        DS[DeepSeek<br/>高性價比]
    end

    subgraph "雲端 Provider（新增）"
        GEM[Google AI Studio<br/>Gemini 系列]
        MST[Mistral<br/>La Plateforme]
        CST[Mistral Codestral<br/>程式碼專用]
        OZN[OpenCode Zen<br/>OpenAI 相容]
        OGO[OpenCode Go<br/>MiniMax]
        WAF[Wafer<br/>DeepSeek 相容]
        KIM[Kimi Moonshot<br/>長上下文]
        CER[Cerebras<br/>超低延遲]
        GRQ[Groq<br/>超低延遲]
        FWK[Fireworks AI<br/>多模型]
        CLF[Cloudflare<br/>邊緣推理]
        ZAI[Z.ai<br/>GLM 系列]
    end

    subgraph "本地 Provider"
        LMS[LM Studio<br/>GUI 介面]
        LC[llama.cpp<br/>CLI 高效能]
        OL[Ollama<br/>簡單易用]
    end

    FCC --> NIM
    FCC --> OR
    FCC --> DS
    FCC --> GEM
    FCC --> MST
    FCC --> CST
    FCC --> OZN
    FCC --> OGO
    FCC --> WAF
    FCC --> KIM
    FCC --> CER
    FCC --> GRQ
    FCC --> FWK
    FCC --> CLF
    FCC --> ZAI
    FCC --> LMS
    FCC --> LC
    FCC --> OL
```

### 5.2 Provider 技術規格

| Provider | 前綴 | Transport 協議 | API Key 變數 | 預設 Base URL |
|---------|------|---------------|-------------|---------------|
| NVIDIA NIM | `nvidia_nim/...` | OpenAI Chat | `NVIDIA_NIM_API_KEY` | `https://integrate.api.nvidia.com/v1` |
| OpenRouter | `open_router/...` | Anthropic Messages | `OPENROUTER_API_KEY` | `https://openrouter.ai/api/v1` |
| DeepSeek | `deepseek/...` | Anthropic Messages | `DEEPSEEK_API_KEY` | `https://api.deepseek.com/anthropic` |
| Google AI Studio | `gemini/...` | OpenAI Chat | `GEMINI_API_KEY` | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| Mistral | `mistral/...` | OpenAI Chat | `MISTRAL_API_KEY` | `https://api.mistral.ai/v1` |
| Mistral Codestral | `mistral_codestral/...` | OpenAI Chat | `CODESTRAL_API_KEY` | `https://codestral.mistral.ai/v1` |
| OpenCode Zen | `opencode/...` | OpenAI Chat | `OPENCODE_API_KEY` | `https://opencode.ai/zen/v1` |
| OpenCode Go | `opencode_go/...` | OpenAI Chat | `OPENCODE_API_KEY` | `https://opencode.ai/zen/go/v1` |
| Wafer | `wafer/...` | Anthropic Messages | `WAFER_API_KEY` | `https://pass.wafer.ai/v1/messages` |
| Kimi (Moonshot) | `kimi/...` | Anthropic Messages | `KIMI_API_KEY` | `https://api.moonshot.ai/anthropic/v1/messages` |
| Cerebras | `cerebras/...` | OpenAI Chat | `CEREBRAS_API_KEY` | `https://api.cerebras.ai/v1` |
| Groq | `groq/...` | OpenAI Chat | `GROQ_API_KEY` | `https://api.groq.com/openai/v1` |
| Fireworks AI | `fireworks/...` | Anthropic Messages | `FIREWORKS_API_KEY` | `https://api.fireworks.ai/inference/v1/messages` |
| Cloudflare | `cloudflare/...` | Anthropic Messages | `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` | `https://api.cloudflare.com/client/v4/accounts/<id>/ai/v1/messages` |
| Z.ai | `zai/...` | Anthropic Messages | `ZAI_API_KEY` | `https://api.z.ai/api/anthropic/v1/messages` |
| LM Studio | `lmstudio/...` | Anthropic Messages | 無需 | `http://localhost:1234/v1` |
| llama.cpp | `llamacpp/...` | Anthropic Messages | 無需 | `http://localhost:8080/v1` |
| Ollama | `ollama/...` | Anthropic Messages | 無需 | `http://localhost:11434` |

### 5.3 NVIDIA NIM

**取得 API Key**：前往 [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)

```dotenv
NVIDIA_NIM_API_KEY="nvapi-your-key"
MODEL="nvidia_nim/z-ai/glm4.7"
```

**可用模型（常用）**：

- `nvidia_nim/z-ai/glm4.7` — 通用型
- `nvidia_nim/z-ai/glm5` — 進階版
- `nvidia_nim/moonshotai/kimi-k2.5` — 長上下文
- `nvidia_nim/minimaxai/minimax-m2.5` — 高性能

**特點**：

- 使用 OpenAI Chat 格式，Proxy 自動轉譯為 Anthropic SSE
- 提供免費額度，適合初期試驗
- 模型選擇豐富，可瀏覽 [build.nvidia.com](https://build.nvidia.com/explore/discover)

### 5.4 OpenRouter

**取得 API Key**：前往 [openrouter.ai/keys](https://openrouter.ai/keys)

```dotenv
OPENROUTER_API_KEY="sk-or-your-key"
MODEL="open_router/stepfun/step-3.5-flash:free"
```

**特點**：

- 支援數百種模型（含免費模型）
- 使用 Anthropic Messages 格式
- 自動路由至最便宜/最快的 Provider
- [免費模型列表](https://openrouter.ai/collections/free-models)
- [全部模型列表](https://openrouter.ai/models)
- Proxy 會依 thinking 支援情況自動過濾 OpenRouter 模型變體

### 5.5 DeepSeek

**取得 API Key**：前往 [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)

```dotenv
DEEPSEEK_API_KEY="your-deepseek-key"
MODEL="deepseek/deepseek-chat"
```

**特點**：

- 使用 DeepSeek 的 Anthropic 相容端點（`api.deepseek.com/anthropic`），而非 OpenAI Chat 端點
- 極高性價比（Token 費用約為 Claude 的 1/10）
- 程式碼生成品質優異

### 5.6 LM Studio（本地模型）

```dotenv
LM_STUDIO_BASE_URL="http://localhost:1234/v1"
MODEL="lmstudio/your-loaded-model"
```

**特點**：

- GUI 介面，易於操作
- 支援 GGUF 量化模型
- 建議選擇支援 Tool Use 的模型以獲得最佳 Claude Code 體驗
- 資料完全不離開本地
- 使用 LM Studio 顯示的 model identifier

### 5.7 llama.cpp（本地模型）

```dotenv
LLAMACPP_BASE_URL="http://localhost:8080/v1"
MODEL="llamacpp/local-model"
```

**特點**：

- 高效能推理引擎
- 需手動啟動 `llama-server`，並確保支援 Anthropic-compatible `/v1/messages` 端點
- 注意 `--ctx-size` 需足夠大（Claude Code prompt 較長，建議 8192 以上）
- 若 llama.cpp 回傳 HTTP 400，通常代表 context size 不足或功能不支援

### 5.8 Ollama（本地模型）

```bash
# 安裝模型
ollama pull llama3.1
ollama serve
```

```dotenv
OLLAMA_BASE_URL="http://localhost:11434"
MODEL="ollama/llama3.1"
```

**特點**：

- 最簡單的本地模型方案
- `OLLAMA_BASE_URL` 不需加 `/v1`
- 使用 `ollama list` 查看已安裝模型的完整 tag（例如 `ollama/llama3.1:8b`）

### 5.9 Google AI Studio（Gemini）

**取得 API Key**：前往 [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

```dotenv
GEMINI_API_KEY="AIza-your-key"
MODEL="gemini/models/gemini-3.1-flash-lite"
```

**可用模型（常用）**：

- `gemini/models/gemini-3.1-flash-lite` — 快速輕量版
- `gemini/models/gemini-3.1-flash` — 標準版
- `gemini/models/gemini-3.1-pro` — 進階版（較高成本）

**特點**：

- 使用 OpenAI Chat 格式，Proxy 自動轉譯為 Anthropic SSE
- Gemini 系列提供免費額度，適合日常開發
- 上下文視窗超大（最高 1M tokens），適合大型程式庫分析

### 5.10 Mistral La Plateforme

**取得 API Key**：前往 [console.mistral.ai/api-keys](https://console.mistral.ai/api-keys)

```dotenv
MISTRAL_API_KEY="your-mistral-key"
MODEL="mistral/mistral-small-latest"
```

**可用模型（常用）**：

- `mistral/mistral-small-latest` — 高性價比
- `mistral/mistral-large-latest` — 高品質推理
- `mistral/open-mistral-nemo` — 免費開源版

**特點**：

- 歐洲在地化雲端服務，符合 GDPR 合規需求
- 程式碼生成與指令遵循表現優秀
- 提供免費開源模型與付費商業模型

### 5.11 Mistral Codestral

**取得 API Key**：前往 [console.mistral.ai](https://console.mistral.ai)（Codestral 專用）

```dotenv
CODESTRAL_API_KEY="your-codestral-key"
MODEL="mistral_codestral/codestral-latest"
```

**特點**：

- 專為程式碼生成最佳化的模型
- 支援 80+ 程式語言
- 提供 Fill-in-the-Middle（FIM）補全能力
- 與 Mistral La Plateforme 使用不同 Key 與端點

### 5.12 OpenCode Zen

**取得 API Key**：前往 [opencode.ai](https://opencode.ai)

```dotenv
OPENCODE_API_KEY="your-opencode-key"
MODEL="opencode/gpt-5.3-codex"
```

**特點**：

- OpenAI Chat 相容端點，主打程式碼任務
- 與 OpenCode Go 共用同一 API Key

### 5.13 OpenCode Go

**取得 API Key**：同 OpenCode Zen，使用 `OPENCODE_API_KEY`

```dotenv
OPENCODE_API_KEY="your-opencode-key"
MODEL="opencode_go/minimax-m2.7"
```

**特點**：

- 使用 MiniMax M2.7 模型
- 與 Zen 端點不同（`/zen/go/v1`）
- 適合多模態與長上下文任務

### 5.14 Wafer

**取得 API Key**：前往 [wafer.ai](https://wafer.ai)

```dotenv
WAFER_API_KEY="your-wafer-key"
MODEL="wafer/DeepSeek-V4-Pro"
```

**特點**：

- 使用 Anthropic Messages 格式
- 主打 DeepSeek 系列高性能模型
- 延遲表現優秀，適合即時開發場景

### 5.15 Kimi（Moonshot）

**取得 API Key**：前往 [platform.moonshot.ai/api-keys](https://platform.moonshot.ai/api-keys)

```dotenv
KIMI_API_KEY="your-kimi-key"
MODEL="kimi/kimi-k2.5"
```

**可用模型（常用）**：

- `kimi/kimi-k2.5` — 標準版，128K 上下文
- `kimi/moonshot-v1-128k` — 超長上下文版

**特點**：

- Moonshot AI 出品，擅長長上下文理解
- 使用 Anthropic Messages 端點，整合無縫
- 中文理解能力優異，適合中文文件分析

### 5.16 Cerebras Inference

**取得 API Key**：前往 [cloud.cerebras.ai](https://cloud.cerebras.ai)

```dotenv
CEREBRAS_API_KEY="your-cerebras-key"
MODEL="cerebras/llama3.1-8b"
```

**可用模型（常用）**：

- `cerebras/llama3.1-8b` — 超快速小型模型
- `cerebras/llama3.1-70b` — 大型高品質模型

**特點**：

- 基於 Cerebras Wafer Scale Engine，推理速度業界最快（2000+ tokens/s）
- 適合需要極低延遲的互動式開發場景
- 免費額度充足，適合快速原型

### 5.17 Groq

**取得 API Key**：前往 [console.groq.com/keys](https://console.groq.com/keys)

```dotenv
GROQ_API_KEY="gsk_your-key"
MODEL="groq/llama-3.3-70b-versatile"
```

**可用模型（常用）**：

- `groq/llama-3.3-70b-versatile` — 通用高品質
- `groq/llama3-8b-8192` — 快速輕量
- `groq/mixtral-8x7b-32768` — MoE 架構

**特點**：

- LPU 架構，推理速度極快（500+ tokens/s）
- 免費額度相當充足，適合個人開發者
- 適合需要快速回應的 Code Review 與補全任務

### 5.18 Fireworks AI

**取得 API Key**：前往 [fireworks.ai/api-keys](https://fireworks.ai/api-keys)

```dotenv
FIREWORKS_API_KEY="fw_your-key"
MODEL="fireworks/accounts/fireworks/models/llama-v3p3-70b-instruct"
```

**特點**：

- 使用 Anthropic Messages 格式（`/inference/v1/messages`）
- 提供豐富的開源模型選擇（Llama、Mistral、Qwen 等）
- 高吞吐量設計，適合團隊並行使用

### 5.19 Cloudflare

**取得憑證**：前往 Cloudflare Dashboard（API Token + Account ID）

```dotenv
CLOUDFLARE_API_TOKEN="your-cf-token"
CLOUDFLARE_ACCOUNT_ID="your-account-id"
MODEL="cloudflare/anthropic/claude-sonnet-4-5"
```

**特點**：

- 基於 Cloudflare Workers AI，全球邊緣節點部署
- 支援 Anthropic 與開源模型
- 已有 Cloudflare 帳戶者可低成本試用
- 需同時設定 `CLOUDFLARE_API_TOKEN` 和 `CLOUDFLARE_ACCOUNT_ID`

### 5.20 Z.ai

**取得 API Key**：前往 [api.z.ai](https://api.z.ai)

```dotenv
ZAI_API_KEY="your-zai-key"
MODEL="zai/glm-5.1"
```

**可用模型（常用）**：

- `zai/glm-5.1` — GLM 最新版
- `zai/glm4.7` — 穩定版

**特點**：

- 智譜 AI（Zhipu AI）出品，使用 Anthropic Messages 格式
- GLM 系列中文理解能力優異
- 成本相對低廉，適合中文開發場景

### 5.21 Provider 比較表（完整版）

| Provider | 費用 | 延遲 | Tool Use | Thinking | 資料隱私 | 適用場景 |
|---------|------|------|----------|----------|---------|---------|
| NVIDIA NIM | 免費額度 | 低 | ✅ | ✅ | 雲端 | 初期驗證 / 一般開發 |
| OpenRouter | 免費+付費 | 中 | ✅ | ✅ | 雲端 | 多模型切換 / 成本最佳化 |
| DeepSeek | 極低 | 中 | ✅ | ✅ | 雲端 | 高性價比日常開發 |
| Google AI Studio | 免費額度 | 低-中 | ✅ | 部分 | 雲端 | 大上下文分析 / 多模態 |
| Mistral | 低-中 | 中 | ✅ | 部分 | 歐洲雲端 | GDPR 合規 / 開源模型 |
| Mistral Codestral | 低 | 低-中 | ✅ | ❌ | 歐洲雲端 | 程式碼補全 / FIM |
| OpenCode Zen | 低 | 低 | ✅ | 部分 | 雲端 | 程式碼生成 |
| OpenCode Go | 低 | 低 | ✅ | 部分 | 雲端 | 多模態任務 |
| Wafer | 低 | 低 | ✅ | ✅ | 雲端 | 即時開發 / 高性能 |
| Kimi (Moonshot) | 低-中 | 中 | ✅ | 部分 | 雲端 | 長上下文 / 中文理解 |
| Cerebras | 免費額度 | 極低 | ✅ | ❌ | 雲端 | 超快速互動式開發 |
| Groq | 免費額度 | 極低 | ✅ | ❌ | 雲端 | 快速 Code Review |
| Fireworks AI | 低 | 低 | ✅ | 部分 | 雲端 | 高吞吐量團隊使用 |
| Cloudflare | 低 | 低（邊緣） | ✅ | 部分 | 邊緣雲端 | 已有 CF 帳戶者 |
| Z.ai | 極低 | 中 | ✅ | ✅ | 雲端 | 中文場景 / 低成本 |
| LM Studio | 免費 | 依硬體 | 部分 | 部分 | 完全本地 | 企業機密環境 |
| llama.cpp | 免費 | 依硬體 | 部分 | 部分 | 完全本地 | 高效能本地推理 |
| Ollama | 免費 | 依硬體 | 部分 | 部分 | 完全本地 | 快速本地測試 |

### 5.22 混合 Provider 策略（推薦）

```dotenv
# 高品質任務（架構設計、複雜重構）→ 強模型
MODEL_OPUS="nvidia_nim/moonshotai/kimi-k2.5"

# 一般開發（程式碼生成、Code Review）→ 平衡模型
MODEL_SONNET="open_router/deepseek/deepseek-r1-0528:free"

# 簡單任務（格式化、小修改）→ 快速模型
MODEL_HAIKU="lmstudio/unsloth/GLM-4.7-Flash-GGUF"

# Fallback
MODEL="nvidia_nim/z-ai/glm4.7"
```

> **實務建議**：根據任務複雜度分配不同等級的模型，可大幅降低成本。架構設計用 Opus 級、日常 Coding 用 Sonnet 級、小任務用 Haiku 級。

> **常見錯誤**：所有任務都用最貴的模型，導致配額很快耗盡。

---

## 6. 開發實戰（AI Development Use Cases）

### 6.1 Web Application 開發

#### 6.1.1 整體流程

```mermaid
graph TD
    A[需求分析] --> B[API 設計]
    B --> C[DB Schema 設計]
    C --> D[後端開發<br/>Spring Boot / FastAPI]
    D --> E[前端開發<br/>Vue / React]
    E --> F[整合測試]
    F --> G[Code Review]
    G --> H[部署]

    style A fill:#e1f5fe
    style B fill:#e1f5fe
    style C fill:#e1f5fe
    style D fill:#fff3e0
    style E fill:#fff3e0
    style F fill:#e8f5e9
    style G fill:#e8f5e9
    style H fill:#f3e5f5
```

#### 6.1.2 前後端生成範例

**後端 API 生成 Prompt：**

```
請根據以下需求設計 Spring Boot REST API：

功能：使用者管理系統（CRUD）
技術棧：
- Spring Boot 3.x
- Spring Data JPA
- PostgreSQL
- Bean Validation

要求：
1. 分層架構（Controller → Service → Repository）
2. DTO / Entity 分離
3. 統一例外處理（@ControllerAdvice）
4. API 文件（OpenAPI 3.0）
5. 分頁與排序支援

請產生完整的程式碼，包含 package 結構。
```

**前端生成 Prompt：**

```
請根據以下 OpenAPI spec 產生 Vue 3 前端：

API Base URL: /api/v1/users
功能：使用者 CRUD 介面

要求：
1. Composition API + TypeScript
2. Pinia 狀態管理
3. Axios HTTP 客戶端
4. Element Plus UI 組件
5. 表格分頁、搜尋、排序
6. 表單驗證
```

#### 6.1.3 DB Schema 設計

**Prompt 範例：**

```
請設計以下系統的資料庫 Schema：

系統：電子商務平台
資料庫：PostgreSQL

需要的 Entity：
- User（使用者）
- Product（商品）
- Order（訂單）
- OrderItem（訂單明細）

要求：
1. 使用正規化設計（至少 3NF）
2. 包含適當的 Index
3. 包含 audit 欄位（created_at, updated_at, created_by）
4. 使用 UUID 作為主鍵
5. 產生 Flyway migration SQL
```

### 6.2 舊系統逆向工程

#### 6.2.1 逆向工程流程

```mermaid
graph TD
    A[取得 Legacy 原始碼] --> B[程式碼結構分析]
    B --> C[自動產出文件<br/>架構圖 / 資料流]
    C --> D[業務邏輯萃取]
    D --> E[測試案例生成]
    E --> F[重構策略建議]
    F --> G[逐步重構實作]
    G --> H[比對驗證]

    style A fill:#ffebee
    style B fill:#fff3e0
    style C fill:#fff3e0
    style D fill:#e8f5e9
    style E fill:#e8f5e9
    style F fill:#e1f5fe
    style G fill:#e1f5fe
    style H fill:#f3e5f5
```

#### 6.2.2 Legacy Java 分析

**Prompt 範例：**

```
請分析以下 Java Legacy 程式碼並產出以下文件：

1. 類別關係圖（Mermaid class diagram）
2. 主要業務流程（Mermaid sequence diagram）
3. 資料模型（ER Diagram）
4. 技術債清單（Technical Debt Inventory）
5. 重構優先順序建議

分析重點：
- 哪些類別職責過重（God Class）
- 哪些方法過長（Long Method）
- 循環依賴問題
- 缺少介面抽象的地方
- 硬編碼的設定值

[貼上程式碼或指定檔案路徑]
```

#### 6.2.3 自動產出文件

**Prompt 範例：**

```
請為以下 COBOL 程式產出完整的系統文件：

文件結構：
1. 程式概述（功能說明、輸入輸出）
2. 業務規則清單
3. 資料欄位說明（COPYBOOK 解析）
4. 處理流程圖（Mermaid flowchart）
5. 異常處理邏輯
6. 與其他系統的介面說明
7. 重建為 Java/Spring Boot 的對照表

[貼上 COBOL 原始碼]
```

### 6.3 Framework 升級

#### 6.3.1 升級流程

```mermaid
graph TD
    A[現況評估] --> B[相依套件分析]
    B --> C[Breaking Change 掃描]
    C --> D[升級計畫制定]
    D --> E[逐步升級實作]
    E --> F[自動化測試]
    F --> G{通過?}
    G -->|是| H[Code Review]
    G -->|否| I[修復問題]
    I --> F
    H --> J[部署]

    style A fill:#e1f5fe
    style C fill:#ffebee
    style F fill:#e8f5e9
```

#### 6.3.2 Spring Boot 升級

**Spring Boot 2 → 3 升級 Prompt：**

```
請協助將以下 Spring Boot 2.7 專案升級至 Spring Boot 3.2：

分析要求：
1. javax → jakarta namespace 遷移清單
2. Spring Security 設定變更
3. 已棄用 API 替代方案
4. 相依套件相容性檢查
5. 設定檔（application.yml）變更
6. 測試程式碼修改

產出：
1. 詳細的升級步驟清單
2. 每個步驟的程式碼修改範例
3. 可能的風險與緩解策略
4. 升級後的驗證清單

[貼上 pom.xml 與主要程式碼]
```

#### 6.3.3 Java 版本升級

**Java 8 → 21 升級 Prompt：**

```
請分析以下 Java 8 專案並建議升級至 Java 21 的步驟：

分析重點：
1. 已棄用 API 替代方案
2. 模組化（JPMS）影響評估
3. 可使用的新語法特性（Records, Sealed Classes, Pattern Matching, Virtual Threads）
4. GC 設定調整建議
5. 第三方套件相容性問題

[貼上專案相關檔案]
```

> **實務建議**：大型升級建議分批進行 — 先升級 Java 版本，確認 CI 通過後再升級 Spring Boot，最後再處理第三方套件。

> **常見錯誤**：一次性升級所有套件導致大量 breaking changes 難以 debug。建議每次只改一個主要版本。

---

## 7. SSDLC（安全開發流程）

### 7.1 AI 輔助 SSDLC 整體流程

```mermaid
graph TD
    subgraph "需求階段"
        A1[需求分析] --> A2[Threat Modeling<br/>AI 輔助威脅建模]
        A2 --> A3[安全需求定義]
    end

    subgraph "設計階段"
        B1[架構設計] --> B2[安全架構審查<br/>AI Code Review]
        B2 --> B3[安全設計規範]
    end

    subgraph "開發階段"
        C1[程式碼開發] --> C2[AI 即時安全檢查]
        C2 --> C3[Secure Coding Review]
        C3 --> C4[單元安全測試]
    end

    subgraph "測試階段"
        D1[SAST 靜態分析] --> D2[DAST 動態測試]
        D2 --> D3[Dependency Check<br/>CVE 掃描]
        D3 --> D4[滲透測試]
    end

    subgraph "部署階段"
        E1[安全設定審查] --> E2[部署自動化]
        E2 --> E3[運行時監控]
    end

    A3 --> B1
    B3 --> C1
    C4 --> D1
    D4 --> E1
```

### 7.2 Threat Modeling（威脅建模）

**AI 輔助威脅建模 Prompt：**

```
請對以下系統進行 STRIDE 威脅建模：

系統：線上銀行轉帳服務
架構：
- 前端：Vue 3 SPA
- API Gateway：Spring Cloud Gateway
- 後端：Spring Boot 3 Microservices
- 資料庫：PostgreSQL + Redis
- 認證：OAuth 2.0 + JWT

請產出：
1. 資料流圖（Data Flow Diagram）
2. STRIDE 威脅分析表
3. 每個威脅的風險等級（高/中/低）
4. 緩解措施建議
5. 安全控制清單
```

### 7.3 Code Review（AI 安全審查）

**安全審查 Prompt：**

```
請對以下程式碼進行安全審查，檢查 OWASP Top 10 風險：

檢查項目：
1. SQL Injection
2. XSS（Cross-Site Scripting）
3. CSRF
4. Broken Authentication
5. Sensitive Data Exposure
6. Security Misconfiguration
7. Insecure Deserialization
8. Known Vulnerabilities（Dependencies）
9. Insufficient Logging
10. Server-Side Request Forgery（SSRF）

每個發現需包含：
- 風險等級
- 問題描述
- 修復建議（含程式碼範例）

[貼上程式碼]
```

### 7.4 Security Scan 整合

**Dependency Check Prompt：**

```
請分析以下 pom.xml / package.json 的相依套件：

1. 列出所有已知 CVE 漏洞
2. 按嚴重等級排序（Critical → High → Medium → Low）
3. 提供升級建議（目標版本）
4. 評估升級的 breaking change 風險
5. 建議修復優先順序

[貼上依賴檔案]
```

### 7.5 SSDLC 自動化流程

```mermaid
graph LR
    DEV[開發者提交] --> PR[Pull Request]
    PR --> LINT[Linting + Format]
    LINT --> SAST[SAST 掃描<br/>SonarQube]
    SAST --> DEP[Dependency Check<br/>OWASP DC]
    DEP --> AI[AI Code Review<br/>Claude Code]
    AI --> TEST[自動化測試]
    TEST --> APPROVE{全部通過?}
    APPROVE -->|是| MERGE[Merge]
    APPROVE -->|否| FIX[退回修復]
    FIX --> DEV
```

> **實務建議**：將 AI 安全審查整合到 CI/CD pipeline 中，作為 PR 合併的必要檢查之一。

> **常見錯誤**：僅依賴 AI 審查而忽略傳統 SAST 工具。AI 與傳統工具應互補，不應取代。

---

## 8. 團隊導入策略（Team Adoption）

### 8.1 導入階段規劃

```mermaid
graph LR
    subgraph "Phase 1（2 週）"
        P1A[環境建置]
        P1B[POC 驗證]
        P1C[選定 Provider]
    end

    subgraph "Phase 2（4 週）"
        P2A[Pilot Team 試用]
        P2B[建立 Prompt 範本]
        P2C[制定使用規範]
    end

    subgraph "Phase 3（持續）"
        P3A[全團隊推廣]
        P3B[效果追蹤]
        P3C[持續優化]
    end

    P1A --> P1B --> P1C --> P2A --> P2B --> P2C --> P3A --> P3B --> P3C
```

### 8.2 開發流程設計（Developer Workflow）

```mermaid
graph TD
    A[接收任務/User Story] --> B[啟動 Claude Code<br/>透過 free-claude-code Proxy]
    B --> C{任務類型}
    C -->|新功能| D[使用 Prompt Template<br/>產生程式碼骨架]
    C -->|Bug Fix| E[提供錯誤資訊<br/>AI 診斷根因]
    C -->|重構| F[分析現有程式碼<br/>AI 建議重構方案]
    D --> G[人工審查 AI 產出]
    E --> G
    F --> G
    G --> H[修改調整]
    H --> I[提交 PR]
    I --> J[AI + 人工 Code Review]
    J --> K[Merge]
```

### 8.3 Prompt Template 管理

建議在專案中建立 `prompts/` 目錄：

```
prompts/
├── architecture/
│   ├── api-design.md
│   ├── db-schema.md
│   └── system-design.md
├── coding/
│   ├── backend-crud.md
│   ├── frontend-component.md
│   └── unit-test.md
├── review/
│   ├── code-review.md
│   └── security-review.md
└── legacy/
    ├── reverse-engineering.md
    ├── migration.md
    └── upgrade.md
```

### 8.4 AI Agent Team 設計

```mermaid
graph TD
    PM[Product Manager<br/>需求定義] --> ARCH[Architecture Agent<br/>架構設計]
    ARCH --> BE[Backend Agent<br/>後端開發]
    ARCH --> FE[Frontend Agent<br/>前端開發]
    BE --> QA[QA Agent<br/>測試生成]
    FE --> QA
    QA --> SEC[Security Agent<br/>安全審查]
    SEC --> DEVOPS[DevOps Agent<br/>部署自動化]

    subgraph "模型分配"
        ARCH -.->|Opus 級| M1[強模型]
        BE -.->|Sonnet 級| M2[平衡模型]
        FE -.->|Sonnet 級| M2
        QA -.->|Haiku 級| M3[快速模型]
        SEC -.->|Opus 級| M1
    end
```

### 8.5 Governance（避免濫用）

| 管控面向 | 具體措施 |
|---------|---------|
| 資料安全 | 禁止將客戶資料 / PII 送入 AI |
| 程式碼品質 | AI 產出必須經人工 Code Review |
| 成本控管 | 設定每日/每月 Token 上限 |
| 合規性 | 記錄所有 AI 互動 Log |
| 授權管理 | 使用 `ANTHROPIC_AUTH_TOKEN` 控管存取 |
| 模型選擇 | 統一團隊使用的 Provider 與模型 |
| Rate Limit | 透過 `PROVIDER_RATE_LIMIT` 與 `MESSAGING_RATE_LIMIT` 雙層控管 |

> **實務建議**：導入初期指定 1-2 位「AI Champion」負責推廣與支援，降低學習曲線。

> **常見錯誤**：未建立明確的使用規範就全面推廣，導致品質不一且成本失控。

---

## 9. 維運與監控（Operations）

### 9.1 Logging 架構

```mermaid
graph LR
    REQ[Client Request] --> PROXY[free-claude-code Proxy]
    PROXY --> LOG[Loguru Logger]
    LOG --> CONSOLE[Console Output]
    LOG --> FILE[server.log]

    subgraph "可選 Log 層級"
        L1[API Payloads<br/>LOG_RAW_API_PAYLOADS]
        L2[SSE Events<br/>LOG_RAW_SSE_EVENTS]
        L3[Error Traces<br/>LOG_API_ERROR_TRACEBACKS]
        L4[CLI Diagnostics<br/>LOG_RAW_CLI_DIAGNOSTICS]
        L5[Debug Flags<br/>DEBUG_PLATFORM_EDITS<br/>DEBUG_SUBAGENT_STACK]
    end
```

**建議的 Logging 策略：**

| 環境 | RAW_API_PAYLOADS | RAW_SSE | ERROR_TRACES | CLI_DIAGNOSTICS | DEBUG_* |
|-----|-----------------|---------|-------------|----------------|---------|
| Development | true | true | true | true | true |
| Staging | false | false | true | false | false |
| Production | false | false | false | false | false |

### 9.2 Token 使用監控

free-claude-code 在 SSE response 中正規化了 token usage metadata。可透過以下方式監控：

1. **Proxy Log 分析**：解析 `server.log` 中的 usage 資訊
2. **Provider Dashboard**：各 Provider 通常提供用量面板
   - NVIDIA NIM：build.nvidia.com dashboard
   - OpenRouter：openrouter.ai/activity
   - DeepSeek：platform.deepseek.com

3. **自建監控**（進階）：

```python
# 範例：在 Proxy 加入 usage tracking middleware
import json
from datetime import datetime

async def track_usage(request, response):
    usage = {
        "timestamp": datetime.utcnow().isoformat(),
        "model": request.model,
        "provider": request.provider,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "user": request.headers.get("x-user-id", "unknown")
    }
    # 寫入監控系統（Prometheus / Grafana / ELK）
    logger.info(f"USAGE: {json.dumps(usage)}")
```

### 9.3 成本控管策略

| 策略 | 實施方式 |
|-----|---------|
| 模型分級 | 簡單任務用 Haiku 級，複雜任務用 Opus 級 |
| Rate Limit | 設定 `PROVIDER_RATE_LIMIT` 與 `PROVIDER_RATE_WINDOW` |
| 每日上限 | 在 Provider 平台設定消費上限 |
| 免費優先 | 優先使用 NVIDIA NIM 免費額度 / OpenRouter 免費模型 |
| 本地模型 | 非敏感任務可使用本地模型（零成本） |
| Request 最佳化 | Proxy 自動以本地方式回應 trivial probe（可節省 5-10% 配額） |

### 9.4 Rate Limit 設計

```dotenv
# 保守設定（免費 Provider）
PROVIDER_RATE_LIMIT=1
PROVIDER_RATE_WINDOW=5
PROVIDER_MAX_CONCURRENCY=2

# 積極設定（付費 Provider / 本地模型）
PROVIDER_RATE_LIMIT=10
PROVIDER_RATE_WINDOW=1
PROVIDER_MAX_CONCURRENCY=10
```

### 9.5 健康檢查

```bash
# 簡單健康檢查
curl -s http://localhost:8082/v1/models | jq '.data | length'

# 完整流程測試
curl -X POST http://localhost:8082/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-secret-token" \
  -d '{
    "model": "claude-3-haiku-20240307",
    "max_tokens": 100,
    "messages": [{"role": "user", "content": "ping"}]
  }'
```

> **實務建議**：建立排程化健康檢查腳本，在 Provider 異常時自動告警。

> **常見錯誤**：未監控 Token 使用量，月底才發現超出預算。建議設定每日告警閾值。

---

## 10. Smoke Testing 與啟動驗證（Startup Validation）

### 10.1 概述

free-claude-code 內建兩層啟動驗證機制：

1. **Startup Model Validation**：啟動時驗證 `MODEL`、`MODEL_OPUS`、`MODEL_SONNET`、`MODEL_HAIKU` 中參照的模型是否能被已設定的 Provider 解析。驗證失敗會在啟動日誌中報告，但不會阻止 Proxy 啟動（graceful degradation）。
2. **Live Smoke Tests**：位於 `smoke/` 目錄，逐 Provider 執行端對端請求驗證。

### 10.2 Startup Validation 行為

```mermaid
graph TD
    START[Proxy 啟動] --> LOAD[載入 .env 設定]
    LOAD --> VALIDATE[驗證 MODEL / MODEL_* 設定]
    VALIDATE --> CHECK{模型可解析?}
    CHECK -->|是| OK[正常啟動]
    CHECK -->|否| WARN[記錄驗證警告<br/>不顯示 traceback]
    WARN --> OK
    OK --> SMOKE[執行 Smoke Test<br/>若已設定]
```

**驗證項目**：

- Model 名稱格式是否符合 `provider_id/model/name`
- 對應 Provider 的 API Key 或 Base URL 是否已設定
- Provider 是否已在 registry 中註冊

**錯誤報告**：啟動驗證失敗時會以簡潔格式輸出，不顯示完整 traceback，方便快速定位問題。

### 10.3 Smoke Test 覆寫

當 `MODEL` 指向的模型不適合用於 Smoke Test（例如高成本模型），可使用 `FCC_SMOKE_MODEL_*` 變數覆寫：

```dotenv
# 使用免費模型進行 Smoke Test，避免消耗付費配額
FCC_SMOKE_MODEL_NVIDIA_NIM="nvidia_nim/z-ai/glm4.7"
FCC_SMOKE_MODEL_OPEN_ROUTER="open_router/stepfun/step-3.5-flash:free"
FCC_SMOKE_MODEL_DEEPSEEK=""
FCC_SMOKE_MODEL_LMSTUDIO=""
FCC_SMOKE_MODEL_LLAMACPP=""
FCC_SMOKE_MODEL_OLLAMA=""
```

> 每個已設定的 Provider 都會執行一次 Smoke Test，即使 `MODEL` / `MODEL_*` 指向不同的 Provider。

### 10.4 Smoke Test 架構

```mermaid
graph LR
    STARTUP[Proxy 啟動] --> DETECT[偵測已設定的 Provider]
    DETECT --> NIM_S[Smoke: NVIDIA NIM]
    DETECT --> OR_S[Smoke: OpenRouter]
    DETECT --> DS_S[Smoke: DeepSeek]
    DETECT --> LOCAL_S[Smoke: LM Studio / llama.cpp / Ollama]

    NIM_S --> RESULT[結果彙整]
    OR_S --> RESULT
    DS_S --> RESULT
    LOCAL_S --> RESULT

    RESULT --> LOG[輸出至啟動日誌]
```

**Smoke Test 驗證項目**：

- Provider 端點是否可達
- API Key 是否有效
- 模型是否存在且可回應
- SSE streaming 是否正常
- reasoning-only streams 是否正確處理

### 10.5 執行 Smoke Test

Smoke Test 預設在 CI 中自動執行。本地執行方式：

```bash
# 執行所有測試（含 smoke）
uv run pytest

# 僅執行 smoke 目錄
uv run pytest smoke/
```

> **實務建議**：部署前先執行 Smoke Test 驗證所有 Provider 連通性，避免上線後才發現問題。

---

## 11. 升級與擴展（Upgrade & Scaling）

### 11.1 如何升級 free-claude-code

```bash
cd free-claude-code

# 備份設定
cp .env .env.backup

# 拉取最新版
git pull origin main

# 更新依賴
uv sync

# 重新啟動
uv run uvicorn server:app --host 0.0.0.0 --port 8082
```

**升級檢查清單：**

1. ✅ 備份 `.env` 設定
2. ✅ 檢查 CHANGELOG / commit log 中的 breaking changes
3. ✅ `git pull` 更新程式碼
4. ✅ `uv sync` 更新依賴
5. ✅ 比對 `.env.example` 是否有新增變數（特別注意 `FCC_SMOKE_MODEL_*`、`DEBUG_*` 等新變數）
6. ✅ 重新啟動 Proxy
7. ✅ 檢查啟動驗證日誌是否有警告
8. ✅ 執行健康檢查確認運作正常

### 11.2 如何新增 Model Provider

```python
# 1. OpenAI 相容 Provider：繼承 OpenAIChatTransport
class MyCustomTransport(OpenAIChatTransport):
    """自訂 Provider Transport"""
    pass

# 2. Anthropic 相容 Provider：繼承 AnthropicMessagesTransport
class MyAnthropicTransport(AnthropicMessagesTransport):
    """自訂 Anthropic 相容 Transport"""
    pass

# 3. 在 config/provider_catalog.py 註冊 provider metadata
# 4. 在 providers/registry.py 加入 factory wiring
```

### 11.3 水平擴展（Load Balancer）

```mermaid
graph TD
    subgraph "Client Layer"
        C1[Claude Code #1]
        C2[Claude Code #2]
        C3[Claude Code #N]
    end

    LB[Load Balancer<br/>Nginx / HAProxy]

    subgraph "Proxy Layer（多實例）"
        P1[FCC Instance #1<br/>:8082]
        P2[FCC Instance #2<br/>:8083]
        P3[FCC Instance #N<br/>:808N]
    end

    subgraph "LLM Providers"
        PROV[NVIDIA / OpenRouter / DeepSeek / Local]
    end

    C1 --> LB
    C2 --> LB
    C3 --> LB
    LB --> P1
    LB --> P2
    LB --> P3
    P1 --> PROV
    P2 --> PROV
    P3 --> PROV
```

**Nginx 設定範例：**

```nginx
upstream fcc_proxy {
    least_conn;
    server 127.0.0.1:8082;
    server 127.0.0.1:8083;
    server 127.0.0.1:8084;
}

server {
    listen 80;
    server_name fcc.internal.company.com;

    location / {
        proxy_pass http://fcc_proxy;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_set_header Host $host;
        proxy_buffering off;        # SSE 需要關閉 buffering
        proxy_read_timeout 300s;    # 長時間 streaming
    }
}
```

### 11.4 高可用設計（HA）

```mermaid
graph TD
    subgraph "高可用架構"
        DNS[DNS Round Robin<br/>fcc.company.com]

        subgraph "Site A"
            LBA[LB-A]
            PA1[FCC #1]
            PA2[FCC #2]
            LBA --> PA1
            LBA --> PA2
        end

        subgraph "Site B"
            LBB[LB-B]
            PB1[FCC #3]
            PB2[FCC #4]
            LBB --> PB1
            LBB --> PB2
        end

        DNS --> LBA
        DNS --> LBB
    end

    subgraph "Provider Failover"
        PRIMARY[Primary: NVIDIA NIM]
        FALLBACK[Fallback: OpenRouter]
        PRIMARY -.->|失敗| FALLBACK
    end

    PA1 --> PRIMARY
    PA2 --> PRIMARY
    PB1 --> PRIMARY
    PB2 --> PRIMARY
```

### 11.5 Dev / Stage / Prod 環境設計

| 環境 | Provider | 模型 | Rate Limit | Logging |
|-----|---------|------|-----------|---------|
| Dev | LM Studio / Ollama | 本地模型 | 寬鬆 | 全開 |
| Stage | NVIDIA NIM（免費） | glm4.7 | 中等 | Error only |
| Prod | DeepSeek / OpenRouter | 付費模型 | 嚴格 | 最小化 |

**環境切換策略：**

```bash
# Dev
cp .env.dev .env && uv run uvicorn server:app --port 8082

# Stage
cp .env.stage .env && uv run uvicorn server:app --port 8082

# Prod
cp .env.prod .env && uv run uvicorn server:app --port 8082
```

> **實務建議**：使用 systemd（Linux）或 NSSM（Windows）管理 Proxy 程序，確保開機自動啟動與異常自動重啟。

> **常見錯誤**：直接在 foreground 執行 Proxy，終端關閉後服務中斷。

---

## 12. 常見問題（FAQ）

### Q1：為什麼 Claude CLI 無法連線到 Proxy？

**可能原因與解法：**

1. Proxy 未啟動 → 確認 `uv run uvicorn server:app --port 8082` 正在執行
2. `ANTHROPIC_BASE_URL` 設定錯誤 → 確認為 `http://localhost:8082`（不含 `/v1`）
3. `ANTHROPIC_AUTH_TOKEN` 不一致 → CLI 與 `.env` 中的 Token 必須相同
4. 防火牆阻擋 → 確認 port 8082 未被擋

### Q2：API Key 無效怎麼辦？

1. 確認 API Key 前綴正確（NVIDIA: `nvapi-`、OpenRouter: `sk-or-`）
2. 確認 Key 未過期
3. 確認 Provider 帳戶餘額/配額未用完
4. 檢查 `.env` 中 Key 的格式（注意引號與空格）

### Q3：本地模型很慢怎麼優化？

1. 使用量化模型（Q4_K_M 或更小）
2. 增加 GPU VRAM（建議 16 GB+）
3. 調整 `--ctx-size` 至合理範圍（8192-16384）
4. 使用 `PROVIDER_MAX_CONCURRENCY=1` 避免 GPU 搶佔
5. 考慮使用 llama.cpp 替代 Ollama（效能更高）

### Q4：出現 `undefined ... input_tokens` 或 `$.speed` 錯誤？

1. 更新 free-claude-code 至最新版（舊版本可能在 streaming 回應中產生無效的 usage metadata）
2. 確認 `ANTHROPIC_BASE_URL` 不含 `/v1`
3. 確認 Proxy 對 `/v1/messages` 回傳 Server-Sent Events
4. 檢查 `server.log` 是否有上游 400/500 錯誤

### Q5：LM Studio / llama.cpp 回傳 HTTP 400？

1. 確認本地 server 支援 `POST /v1/messages`
2. 確認模型與 runtime 支援請求的 context length 和 tools
3. llama.cpp 需要足夠的 `--ctx-size`
4. Base URL 需包含 `/v1`（`http://localhost:1234/v1`）

### Q6：VS Code Extension 仍顯示登入畫面？

1. 確認 `settings.json` 中的環境變數已設定
2. 重新載入 Extension 或重啟 VS Code
3. 首次登入畫面可能仍會出現一次，選擇 Anthropic Console 路徑即可
4. 當 `ANTHROPIC_BASE_URL` 在 Extension 程序中生效後，本地 Proxy 即接手處理

### Q7：Streaming 中途斷線怎麼辦？

`incomplete chunked read`、`server disconnected` 或 peer closing body 等錯誤通常來自上游 Provider 或 Gateway。

- 減少 `PROVIDER_MAX_CONCURRENCY`
- 增加 `HTTP_READ_TIMEOUT`（預設已為 300 秒）
- 稍後重試（可能是 Provider 暫時性問題）

### Q8：不同模型的 Tool Call 支援不一致？

- Tool Call 支援取決於模型本身與 Provider
- 部分 OpenAI 相容模型的 Tool Call delta 格式不正確、遺漏 tool name，或以純文字回傳 tool calls
- 嘗試換用其他模型或 Provider，確認問題並非 Proxy 本身造成

### Q9：如何在團隊中統一 Proxy 設定？

1. 架設團隊共用 Proxy 實例
2. 透過內部 DNS 統一 `ANTHROPIC_BASE_URL`
3. 使用同一個 `ANTHROPIC_AUTH_TOKEN`
4. 在 Proxy 端統一設定 Provider 與模型

### Q10：如何知道目前使用的是哪個模型？

- 在 Claude Code CLI 中執行 `/model` 查看當前模型
- Model Picker 顯示所有可用的 Provider 模型
- 選擇 `(no thinking)` 變體可要求 Claude Code 發送 non-thinking 請求

### Q11：企業防火牆環境如何設定？

1. 設定 Provider Proxy：`NVIDIA_NIM_PROXY="http://proxy.company.com:8080"`（支援 http 與 socks5）
2. 確認 Proxy 允許 HTTPS 流量至 Provider endpoint
3. 若使用本地模型則無需外部網路

### Q12：Voice Note 功能如何啟用？

```bash
# 安裝語音依賴
uv sync --extra voice_local    # 本地 Whisper（cpu / cuda）
uv sync --extra voice          # NVIDIA NIM 語音
uv sync --extra voice --extra voice_local  # 兩者皆安裝
```

```dotenv
# 設定 .env
VOICE_NOTE_ENABLED=true
WHISPER_DEVICE="cpu"           # cpu | cuda | nvidia_nim
WHISPER_MODEL="base"           # cpu/cuda: tiny/base/small/medium/large-v2/large-v3
                               # nvidia_nim: nvidia/parakeet-ctc-1.1b-asr 或 openai/whisper-large-v3
HF_TOKEN=""                    # Hugging Face Token（若使用 cpu/cuda 模式）
```

使用 `WHISPER_DEVICE="nvidia_nim"` 搭配 `voice` extra 與 `NVIDIA_NIM_API_KEY` 可使用 NVIDIA 託管的轉錄服務。語音裝置設定（STT）與聊天模型設定（`MODEL=nvidia_nim/...`）彼此獨立。

### Q13：啟動時出現模型驗證警告怎麼辦？

1. 檢查 `MODEL` 格式是否為 `provider_id/model/name`
2. 確認對應 Provider 的 API Key 已設定
3. 驗證警告不會阻止 Proxy 啟動，但建議修正以確保路由正確

### Q14：Admin UI 無法存取怎麼辦？

1. 確認 Proxy 正常運行（`fcc-server` 或 `uv run uvicorn server:app --port 8082`）
2. 確認存取 URL 為 `http://127.0.0.1:8082/admin`（不是 `localhost`，也不含尾斜線）
3. Admin UI 僅限本機迴環位址存取，遠端連線會被拒絕
4. 若需遠端存取，請使用 SSH Tunnel：`ssh -L 8082:127.0.0.1:8082 user@server`

### Q15：如何啟用 Gateway Model Discovery？

設定環境變數後重新啟動 Claude Code：

**Bash：**

```bash
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1
fcc-claude
```

**PowerShell：**

```powershell
$env:CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1; fcc-claude
```

啟用後，Claude Code 的 `/model` 選擇器會顯示所有 Proxy 支援的模型，無需手動輸入模型名稱。

### Q16：`fcc-claude` 與手動設定環境變數有何差異？

`fcc-claude` 除了自動設定 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_AUTH_TOKEN` 外，還會：

- 自動從 Admin UI 讀取目前的 Port 設定，無需硬編碼
- 自動設定 `CLAUDE_CODE_AUTO_COMPACT_WINDOW=190000`（啟用對話歷史自動壓縮至 190k tokens）
- 確保 Proxy 未啟動時提供明確錯誤訊息

建議優先使用 `fcc-claude`，僅在腳本自動化場景才手動設定環境變數。

---

## 13. 最佳實務（Best Practices）

### 13.1 架構設計

| 實務 | 說明 |
|-----|------|
| Proxy 與開發環境分離 | Proxy 運行在獨立程序，避免與開發工具耦合 |
| 多環境配置 | Dev / Stage / Prod 使用不同 `.env` |
| Provider 備援 | 設定至少兩個 Provider，一個主要一個備援 |
| 本地+雲端混合 | 敏感資料用本地模型，一般開發用雲端 |
| 統一入口 | 團隊共用 Proxy，透過 Load Balancer 分流 |

### 13.2 Prompt Engineering

| 實務 | 說明 |
|-----|------|
| 結構化 Prompt | 使用明確的角色、背景、任務、輸出格式 |
| 上下文充足 | 提供足夠的程式碼上下文，避免 AI 猜測 |
| 分步驟指示 | 複雜任務拆成小步驟，每步明確 |
| 範例驅動 | 提供期望輸出的範例 |
| 約束條件 | 明確列出限制（語言、框架、版本、風格） |

### 13.3 成本最佳化

| 實務 | 節省幅度 |
|-----|---------|
| 使用 Model Routing 分級 | ~40% |
| 優先使用免費模型（NIM / OpenRouter Free） | ~80% |
| 本地模型處理簡單任務 | ~90% |
| Request Optimization（Proxy 自動） | ~5-10% |
| 控制 Prompt 長度 | ~20% |

### 13.4 安全性

| 實務 | 說明 |
|-----|------|
| 設定 `ANTHROPIC_AUTH_TOKEN` | 防止未授權存取 Proxy |
| 關閉 Raw Logging | 生產環境不記錄敏感內容 |
| 關閉 Debug Flags | `DEBUG_PLATFORM_EDITS=false`、`DEBUG_SUBAGENT_STACK=false` |
| 禁用 Private Network Access | `WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false` |
| API Key 不入版控 | `.env` 加入 `.gitignore` |
| 定期輪換 Key | 每月更換 Provider API Key |
| PII 保護 | 禁止將個人資料送入 AI |

---

## 14. CI/CD 整合

### 14.1 GitHub Actions 範例

```yaml
name: AI-Assisted Code Review

on:
  pull_request:
    branches: [main, develop]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.14'

      - name: Install uv
        uses: astral-sh/setup-uv@v8

      - name: Start free-claude-code proxy
        env:
          NVIDIA_NIM_API_KEY: ${{ secrets.NVIDIA_NIM_API_KEY }}
          MODEL: "nvidia_nim/z-ai/glm4.7"
          ANTHROPIC_AUTH_TOKEN: ${{ secrets.FCC_AUTH_TOKEN }}
        run: |
          git clone https://github.com/Alishahryar1/free-claude-code.git /tmp/fcc
          cd /tmp/fcc
          cp /dev/null .env
          echo "NVIDIA_NIM_API_KEY=$NVIDIA_NIM_API_KEY" >> .env
          echo "MODEL=$MODEL" >> .env
          echo "ANTHROPIC_AUTH_TOKEN=$ANTHROPIC_AUTH_TOKEN" >> .env
          uv run uvicorn server:app --host 0.0.0.0 --port 8082 &
          sleep 5

      - name: Run AI Code Review
        env:
          ANTHROPIC_BASE_URL: "http://localhost:8082"
          ANTHROPIC_AUTH_TOKEN: ${{ secrets.FCC_AUTH_TOKEN }}
        run: |
          # 使用 Claude Code CLI 進行 Code Review
          npx @anthropic-ai/claude-code --print \
            "請檢查此 PR 的程式碼變更，找出潛在問題：$(git diff origin/main...HEAD)"
```

> **注意**：專案 CI 使用 `astral-sh/setup-uv` Action（目前版本 v8），請確保版本與專案一致。

### 14.2 CI/CD 整合架構

```mermaid
graph LR
    DEV[開發者 Push] --> GH[GitHub]
    GH --> GA[GitHub Actions]
    GA --> FCC[free-claude-code Proxy]
    FCC --> LLM[LLM Provider]
    LLM --> FCC
    FCC --> GA
    GA --> COMMENT[PR Comment<br/>AI Review 結果]
```

---

## 15. 開發與貢獻指南（Development & Contributing）

### 15.1 開發環境設定

```bash
# 安裝 uv（若尚未安裝）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安裝 Python 3.14
uv python install 3.14

# Clone 專案
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code

# 安裝依賴
uv sync
```

### 15.2 開發指令

提交前必須依序執行以下檢查（CI 亦強制執行相同流程）：

```bash
# 1. 程式碼格式化
uv run ruff format

# 2. Linting 檢查
uv run ruff check

# 3. 型別檢查
uv run ty check

# 4. 執行測試
uv run pytest
```

> **重要**：這四個步驟必須全部通過才能提交 PR。CI 在 push / merge 時會強制執行同樣的檢查。

### 15.3 程式碼規範

| 規範 | 說明 |
|------|------|
| Formatter | Ruff（設定為 py314） |
| Type Checker | Ty（不使用 `# type: ignore` 或 `# ty: ignore`） |
| Logger | Loguru |
| 測試框架 | Pytest |
| 例外語法 | Python 3.14 支援 `except TypeError, ValueError:` 語法 |

### 15.4 架構原則

根據 `AGENTS.md` 與 `PLAN.md`，專案遵循以下設計原則：

- **共用工具**：共用的 Anthropic 協議邏輯放在 `core/anthropic/` 模組中，Provider 之間不互相 import
- **DRY 原則**：抽取共用基底類別消除重複，偏好 composition 而非 copy-paste
- **封裝**：使用 accessor method 存取內部狀態，不從外部直接操作 `_attribute`
- **Provider 特定設定**：Provider 特定欄位放在 Provider constructor 中，不放入基底 `ProviderConfig`
- **無死碼**：移除未使用的程式碼與硬編碼值，使用 settings/config 取代字面值
- **效能**：字串累加使用 list accumulation、於 init 時快取環境變數、迭代優先於遞迴
- **平台無關命名**：共用程式碼中使用通用名稱（如 `PLATFORM_EDIT`）而非平台特定名稱
- **最大測試覆蓋率**：所有功能都應有測試覆蓋，偏好 live smoke test 以及早期發現問題

### 15.5 貢獻規則

- 透過 [Issues](https://github.com/Alishahryar1/free-claude-code/issues) 回報 bug 與功能請求
- 保持變更小且有對應的測試覆蓋
- **不要**提交 Docker 整合 PR
- **不要**提交 README 修改 PR（請改開 Issue）
- 提交 PR 前執行完整檢查流程
- Python 3.14 的 `except X, Y` 語法僅在正式版中支援，Alpha 版不支援，提交 PR 前請留意

### 15.6 Package Scripts

`pyproject.toml` 定義了以下可執行腳本：

| 指令 | 功能 |
|------|------|
| `free-claude-code` | 以設定的 host 與 port 啟動 Proxy |
| `fcc-init` | 建立使用者設定範本於 `~/.config/free-claude-code/.env` |

### 15.7 Cognitive Workflow

專案建議的開發認知流程（源自 `AGENTS.md`）：

1. **ANALYZE**：閱讀相關檔案，不做猜測
2. **PLAN**：釐清邏輯、識別根因或必要變更、按依賴順序排列
3. **EXECUTE**：修復根因而非症狀，增量式提交
4. **VERIFY**：執行 CI 檢查與相關 Smoke Test，透過日誌或輸出確認修復
5. **SPECIFICITY**：精確完成要求的範圍，不多也不少
6. **PROPAGATION**：變更可能影響多個檔案，正確傳播更新

---

## 16. 範例 Prompt 集

### 16.1 通用開發 Prompt

```
你是一位資深 Java 工程師。請根據以下需求產生程式碼：

需求：[描述功能]
技術棧：Spring Boot 3.2 + Java 21 + PostgreSQL
架構：Clean Architecture（Controller → UseCase → Repository）

要求：
1. 使用 Records 作為 DTO
2. 使用 Bean Validation
3. 統一例外處理
4. 完整的 JavaDoc
5. 對應的 JUnit 5 測試

請產生完整可執行的程式碼。
```

### 16.2 Code Review Prompt

```
請對以下程式碼進行全面 Code Review：

檢查面向：
1. 程式碼品質（可讀性、命名、複雜度）
2. 效能（N+1 查詢、記憶體使用）
3. 安全性（OWASP Top 10）
4. 測試覆蓋率建議
5. 架構合理性

輸出格式：
- 🔴 嚴重問題
- 🟡 建議改善
- 🟢 優點

[貼上程式碼]
```

### 16.3 逆向工程 Prompt

```
請分析以下 Legacy 系統程式碼：

目標：
1. 繪製系統架構圖（Mermaid）
2. 列出所有業務規則
3. 識別技術債
4. 產出重建的 User Story 清單
5. 建議現代化架構方案

限制：
- 保持業務邏輯不變
- 資料庫結構可重新設計
- 目標技術棧：Spring Boot 3 + PostgreSQL

[貼上程式碼]
```

### 16.4 升級評估 Prompt

```
請評估以下專案從 [舊版本] 升級到 [新版本] 的影響：

評估項目：
1. Breaking Changes 清單
2. 棄用 API 替代方案
3. 第三方套件相容性
4. 設定變更需求
5. 預估工作量（人天）
6. 風險評估與緩解計畫

[貼上 pom.xml / build.gradle / package.json]
```

---

## 17. 檢查清單（Checklist）

### 17.1 初始安裝檢查

- [ ] Node.js 22 LTS 已安裝
- [ ] Claude Code CLI 已安裝（`npm install -g @anthropic-ai/claude-code`）
- [ ] uv 已安裝且為最新版（`uv self update`）
- [ ] Python 3.14 已安裝（`uv python install 3.14`）
- [ ] free-claude-code 已 clone（或透過 Quick Install 安裝）
- [ ] `fcc-init` 已執行，設定檔已建立（`~/.config/free-claude-code/.env`）
- [ ] 至少一個 Provider API Key 已設定
- [ ] `ANTHROPIC_AUTH_TOKEN` 已設定
- [ ] Proxy 啟動成功（`fcc-server` 或 `uv run uvicorn server:app --port 8082`）
- [ ] 啟動驗證日誌無錯誤警告
- [ ] `curl http://localhost:8082/v1/models` 回應正常
- [ ] Admin UI 可正常存取（`http://127.0.0.1:8082/admin`）

### 17.2 客戶端連線檢查

- [ ] `ANTHROPIC_BASE_URL` 設為 `http://localhost:8082`（無 `/v1`）
- [ ] `ANTHROPIC_AUTH_TOKEN` 與 `.env` 一致
- [ ] Claude Code CLI 可正常啟動（`fcc-claude` 或手動設定）
- [ ] VS Code Extension 設定完成（`settings.json`）
- [ ] JetBrains ACP 設定完成（`installed.json`）
- [ ] `/model` 可列出可用模型
- [ ] `(no thinking)` 變體可正常選取
- [ ] Codex CLI 整合已確認（若使用 `fcc-codex`）
- [ ] `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` 已設定（若需 Model Discovery）

### 17.3 團隊導入檢查

- [ ] 已選定主要 Provider 與備援 Provider
- [ ] 已建立 Prompt Template 目錄
- [ ] 已制定 AI 使用規範
- [ ] 已設定成本監控
- [ ] 已建立 Code Review 流程
- [ ] 已完成 Pilot Team 試用
- [ ] 已撰寫團隊內部使用指南

### 17.4 安全檢查

- [ ] `.env` 已加入 `.gitignore`
- [ ] Raw Logging 已關閉（Production）
- [ ] Debug Flags 已關閉（Production）
- [ ] `WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false`
- [ ] API Key 定期輪換計畫已建立
- [ ] PII 保護規範已告知團隊
- [ ] `ANTHROPIC_AUTH_TOKEN` 使用強密碼

### 17.5 維運檢查

- [ ] Proxy 使用 systemd / NSSM 管理（非 foreground）
- [ ] 健康檢查排程已設定
- [ ] Token 使用量監控已建立
- [ ] 備份與升級流程已文件化
- [ ] Smoke Test 已驗證所有 Provider 連通性
- [ ] 故障排除 SOP 已準備

### 17.6 開發貢獻檢查

- [ ] 已執行 `uv run ruff format`
- [ ] 已執行 `uv run ruff check`
- [ ] 已執行 `uv run ty check`
- [ ] 已執行 `uv run pytest`
- [ ] 新增功能已附帶測試覆蓋
- [ ] 未使用 `# type: ignore` 或 `# ty: ignore`
- [ ] 變更已正確傳播至所有受影響檔案

---

---

## 18. Admin UI 管理介面

### 18.1 功能概述

Admin UI 是 free-claude-code 內建的 Web 管理介面，Proxy 啟動後即可在瀏覽器存取：

```text
http://127.0.0.1:8082/admin
```

Admin UI 採用純本機迴環存取設計，不需要額外認證即可使用，但也因此**不對外網路開放**，確保管理操作安全。

### 18.2 主要功能

```mermaid
graph TD
    ADM[Admin UI<br/>127.0.0.1:8082/admin]

    subgraph "Provider 管理"
        P1[API Key 設定]
        P2[Base URL 設定]
        P3[連通性狀態檢視]
    end

    subgraph "模型路由"
        R1[MODEL_OPUS 設定]
        R2[MODEL_SONNET 設定]
        R3[MODEL_HAIKU 設定]
        R4[MODEL Fallback 設定]
    end

    subgraph "整合設定"
        I1[Discord Bot 設定]
        I2[Telegram Bot 設定]
        I3[Voice Transcription 設定]
    end

    subgraph "系統資訊"
        S1[設定檔路徑]
        S2[Port 設定]
        S3[Auth Token]
    end

    ADM --> P1
    ADM --> P2
    ADM --> P3
    ADM --> R1
    ADM --> R2
    ADM --> R3
    ADM --> R4
    ADM --> I1
    ADM --> I2
    ADM --> I3
    ADM --> S1
    ADM --> S2
    ADM --> S3
```

### 18.3 使用流程

1. 啟動 Proxy：`fcc-server`
2. 開啟瀏覽器，前往 `http://127.0.0.1:8082/admin`
3. 在 Provider 設定區域填入 API Key，點擊「驗證」確認連通性
4. 設定 Model Routing（Opus / Sonnet / Haiku 分級）
5. 點擊「儲存」套用設定（無需重啟 Proxy）
6. 頁尾可確認設定檔儲存路徑

### 18.4 遠端存取方案

Admin UI 僅限本機存取。若需從遠端機器管理，請使用 SSH Tunnel：

```bash
# 在本機執行，將遠端 Proxy 的 Admin UI 映射至本機 8082 port
ssh -L 8082:127.0.0.1:8082 user@remote-server
# 接著開啟瀏覽器存取 http://127.0.0.1:8082/admin
```

> **安全建議**：生產環境勿直接對外暴露 Admin UI。應透過 SSH Tunnel、VPN 或 Bastion Host 進行管理。

### 18.5 Admin UI 與 .env 設定優先權

Admin UI 設定與 `.env` 設定並存，優先權如下：

| 設定方式 | 優先權 | 說明 |
| -------- | ------ | ---- |
| Admin UI 即時設定 | 高 | 儲存後立即生效，不需重啟 |
| `.env` 設定檔 | 中 | Proxy 啟動時載入 |
| 系統環境變數 | 低 | 覆蓋 `.env`，但低於 Admin UI |

---

## 19. Codex CLI 整合（fcc-codex）

### 19.1 概述

除 Claude Code CLI 外，free-claude-code 自版本更新後亦支援 **OpenAI Codex CLI**。透過 `fcc-codex` 指令，可將 Codex CLI 的流量路由至 Proxy 支援的任何 LLM Provider，達到「免費使用 Codex CLI 功能」的效果。

### 19.2 前置需求

**安裝 Codex CLI：**

```bash
npm install -g @openai/codex
```

驗證安裝：

```bash
codex --version
```

### 19.3 使用 fcc-codex 啟動

```bash
fcc-codex
```

`fcc-codex` 會自動執行以下動作：

1. 讀取 Proxy 目前的 Port 設定（來自 Admin UI / `.env`）
2. 在 Proxy 的 `/v1/models` 建立 `fcc` 臨時 Provider 的模型目錄
3. 移除 Codex CLI 官方的 OpenAI 憑證，改由 Proxy 接管
4. 啟動 Codex CLI 並串接至 Proxy

### 19.4 使用範例

```bash
# 啟動後與一般 Codex CLI 操作相同
fcc-codex

# Codex CLI 中的常用操作：
# - 直接提問：>  請解釋這段程式碼的功能
# - 產生程式碼：> 產生一個 FastAPI 的 CRUD 範例
# - 執行任務：> 分析並修復這個 Python 腳本的 bug
```

### 19.5 模型設定

`fcc-codex` 使用與 Claude Code 相同的模型路由設定（`MODEL`、`MODEL_OPUS`、`MODEL_SONNET`、`MODEL_HAIKU`），無需額外設定。

若要為 Codex CLI 使用特定模型，直接修改 `.env` 中的 `MODEL` 變數即可：

```dotenv
# Codex CLI 使用的模型（與 Claude Code 共用路由）
MODEL="groq/llama-3.3-70b-versatile"       # 超低延遲
MODEL="gemini/models/gemini-3.1-flash"      # 大上下文
MODEL="cerebras/llama3.1-70b"              # 極速推理
```

### 19.6 VS Code 整合（Codex）

若使用 VS Code Codex Extension，可在 `settings.json` 設定指向 Proxy：

```json
{
  "codex.apiBaseUrl": "http://localhost:8082/v1",
  "codex.apiKey": "freecc"
}
```

> **實務建議**：Codex CLI 適合偏好指令列操作的開發者，或在自動化腳本中批次處理程式碼任務的場景。

> **常見錯誤**：忘記先啟動 Proxy 就執行 `fcc-codex`，導致連線失敗。請確認 `fcc-server` 已在背景運行。

---

> **文件維護**：本手冊應隨 free-claude-code 版本更新同步修訂。建議每季度審查一次內容正確性。

> **回報問題**：若發現手冊內容與實際行為不符，請至 [Issues](https://github.com/Alishahryar1/free-claude-code/issues) 回報或更新本手冊。
