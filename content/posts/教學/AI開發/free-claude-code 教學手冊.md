+++
date = '2026-07-01T00:00:00+08:00'
lastmod = '2026-09-08T10:00:00+08:00'
draft = false
title = 'Free Claude Code 教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# Free Claude Code（FCC）企業技術白皮書與導入手冊

> **文件版本**：v3.0（2026-09）
> **對應上游版本**：[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) `v6.1.4`（53,800+ Stars／8,600+ Forks）
> **適用對象**：資深工程師 / 架構師 / DevOps / 平台工程 / AI 開發團隊 / 技術決策者
> **授權條款**：MIT License
> **文件定位**：企業級 AI 輔助開發平台之技術評估、導入、維運與治理手冊
> **語言**：繁體中文
> **最後更新**：2026 年 9 月 8 日

---

## 免責與商標聲明

Free Claude Code（以下簡稱 **FCC**）為**獨立開源專案**，與 Anthropic 無隸屬關係，亦未取得 Anthropic 背書。Claude 與 Claude Code 為 Anthropic 之商標；Codex 為 OpenAI 之商標；其餘產品名稱歸各自權利人所有。

本手冊所述之各 Provider 免費額度、速率限制與服務條款，均由各 Provider 自行制定並可能隨時變更。企業導入前，**務必自行確認各 Provider 之服務條款（ToS）是否允許貴組織的使用情境**（特別是商業用途、團隊共用與自動化呼叫）。本文件僅供技術參考，不構成法律意見。

---

## 目錄

1. [概述（Overview）](#1-概述overview)
   - 1.1 [FCC 是什麼](#11-fcc-是什麼)
   - 1.2 [核心價值主張](#12-核心價值主張)
   - 1.3 [與 Claude Code 官方訂閱的差異](#13-與-claude-code-官方訂閱的差異)
   - 1.4 [適用場景與不適用場景](#14-適用場景與不適用場景)
   - 1.5 [版本演進與重大變更](#15-版本演進與重大變更)
   - 1.6 [架構定位圖](#16-架構定位圖)
2. [系統整體架構（Architecture）](#2-系統整體架構architecture)
   - 2.1 [高階架構圖](#21-高階架構圖)
   - 2.2 [分層架構與原始碼結構](#22-分層架構與原始碼結構)
   - 2.3 [Request Flow：Anthropic Messages 路徑](#23-request-flowanthropic-messages-路徑)
   - 2.4 [Request Flow：OpenAI Responses 路徑](#24-request-flowopenai-responses-路徑)
   - 2.5 [模型路由與階層繼承](#25-模型路由與階層繼承)
   - 2.6 [Fallback Chain 自動故障轉移](#26-fallback-chain-自動故障轉移)
   - 2.7 [Reasoning 推理強度控制](#27-reasoning-推理強度控制)
   - 2.8 [Token 最佳化機制](#28-token-最佳化機制)
   - 2.9 [擴充點（Extension Points）](#29-擴充點extension-points)
3. [安裝與環境建置（Installation）](#3-安裝與環境建置installation)
   - 3.1 [系統需求](#31-系統需求)
   - 3.2 [安裝方式決策](#32-安裝方式決策)
   - 3.3 [方式一：官方安裝腳本（推薦）](#33-方式一官方安裝腳本推薦)
   - 3.4 [方式二：原始碼安裝（稽核 / 開發）](#34-方式二原始碼安裝稽核--開發)
   - 3.5 [啟動 FCC 服務](#35-啟動-fcc-服務)
   - 3.6 [首次設定（以 NVIDIA NIM 為例）](#36-首次設定以-nvidia-nim-為例)
   - 3.7 [啟動 Coding Agent](#37-啟動-coding-agent)
   - 3.8 [安裝驗證](#38-安裝驗證)
   - 3.9 [檔案與目錄配置](#39-檔案與目錄配置)
   - 3.10 [更新與解除安裝](#310-更新與解除安裝)
   - 3.11 [環境建置流程圖](#311-環境建置流程圖)
4. [核心設定（Configuration）](#4-核心設定configuration)
   - 4.1 [設定來源與優先權](#41-設定來源與優先權)
   - 4.2 [Admin UI 設定面板](#42-admin-ui-設定面板)
   - 4.3 [模型設定：MODEL、階層與 Fallback](#43-模型設定model階層與-fallback)
   - 4.4 [Reasoning 設定](#44-reasoning-設定)
   - 4.5 [Proxy 認證與服務連線](#45-proxy-認證與服務連線)
   - 4.6 [速率限制與逾時](#46-速率限制與逾時)
   - 4.7 [請求最佳化開關](#47-請求最佳化開關)
   - 4.8 [Web Tools 設定](#48-web-tools-設定)
   - 4.9 [企業 Proxy（Per-Provider）](#49-企業-proxyper-provider)
   - 4.10 [Messaging 與語音設定](#410-messaging-與語音設定)
   - 4.11 [日誌與診斷設定](#411-日誌與診斷設定)
   - 4.12 [環境變數完整速查表](#412-環境變數完整速查表)
5. [Provider 生態系（50 家供應商）](#5-provider-生態系50-家供應商)
   - 5.1 [Provider 分類全覽](#51-provider-分類全覽)
   - 5.2 [完整 Provider 目錄](#52-完整-provider-目錄)
   - 5.3 [認證模式：API Key 與 Connected Account](#53-認證模式api-key-與-connected-account)
   - 5.4 [免費額度優先組合](#54-免費額度優先組合)
   - 5.5 [重點 Provider 詳解](#55-重點-provider-詳解)
   - 5.6 [訂閱制 Provider 與合規注意事項](#56-訂閱制-provider-與合規注意事項)
   - 5.7 [企業雲 Provider](#57-企業雲-provider)
   - 5.8 [本地 Provider](#58-本地-provider)
   - 5.9 [Provider 選型決策矩陣](#59-provider-選型決策矩陣)
   - 5.10 [混合 Provider 路由策略](#510-混合-provider-路由策略)
6. [Coding Agent 與客戶端整合（Clients）](#6-coding-agent-與客戶端整合clients)
   - 6.1 [十大 Coding Agent 總覽](#61-十大-coding-agent-總覽)
   - 6.2 [Claude Code 整合](#62-claude-code-整合)
   - 6.3 [Codex 整合（CLI / App / VS Code）](#63-codex-整合cli--app--vs-code)
   - 6.4 [其餘 Agent 啟動方式](#64-其餘-agent-啟動方式)
   - 6.5 [VS Code 整合](#65-vs-code-整合)
   - 6.6 [JetBrains ACP 整合](#66-jetbrains-acp-整合)
   - 6.7 [瀏覽器 Code Sessions](#67-瀏覽器-code-sessions)
   - 6.8 [Discord / Telegram 遠端協作](#68-discord--telegram-遠端協作)
   - 6.9 [語音輸入（Voice Notes）](#69-語音輸入voice-notes)
   - 6.10 [客戶端疑難排解](#610-客戶端疑難排解)
7. [開發實戰（AI Development Use Cases）](#7-開發實戰ai-development-use-cases)
   - 7.1 [Web Application 開發](#71-web-application-開發)
   - 7.2 [舊系統逆向工程](#72-舊系統逆向工程)
   - 7.3 [Framework 升級](#73-framework-升級)
   - 7.4 [多模型協作模式](#74-多模型協作模式)
8. [SSDLC（安全開發流程）](#8-ssdlc安全開發流程)
   - 8.1 [AI 輔助 SSDLC 整體流程](#81-ai-輔助-ssdlc-整體流程)
   - 8.2 [Threat Modeling（威脅建模）](#82-threat-modeling威脅建模)
   - 8.3 [Code Review（AI 安全審查）](#83-code-reviewai-安全審查)
   - 8.4 [Security Scan 整合](#84-security-scan-整合)
   - 8.5 [SSDLC 自動化流程](#85-ssdlc-自動化流程)
9. [團隊導入策略（Team Adoption）](#9-團隊導入策略team-adoption)
   - 9.1 [導入階段規劃](#91-導入階段規劃)
   - 9.2 [開發流程設計](#92-開發流程設計)
   - 9.3 [Prompt Template 管理](#93-prompt-template-管理)
   - 9.4 [AI Agent Team 設計](#94-ai-agent-team-設計)
   - 9.5 [治理與濫用防制](#95-治理與濫用防制)
10. [維運與監控（Operations）](#10-維運與監控operations)
    - 10.1 [日誌架構](#101-日誌架構)
    - 10.2 [Token 與成本監控](#102-token-與成本監控)
    - 10.3 [成本控管策略](#103-成本控管策略)
    - 10.4 [速率限制設計](#104-速率限制設計)
    - 10.5 [健康檢查與可觀測性](#105-健康檢查與可觀測性)
11. [品質驗證：測試與 Smoke Testing](#11-品質驗證測試與-smoke-testing)
    - 11.1 [兩層測試策略](#111-兩層測試策略)
    - 11.2 [Hermetic 測試](#112-hermetic-測試)
    - 11.3 [Live Smoke Testing](#113-live-smoke-testing)
    - 11.4 [Smoke Target 對照表](#114-smoke-target-對照表)
    - 11.5 [Smoke 模型覆寫](#115-smoke-模型覆寫)
    - 11.6 [實務執行範例](#116-實務執行範例)
12. [升級、擴展與高可用（Upgrade & Scaling）](#12-升級擴展與高可用upgrade--scaling)
    - 12.1 [升級策略](#121-升級策略)
    - 12.2 [新增自訂 Provider](#122-新增自訂-provider)
    - 12.3 [水平擴展](#123-水平擴展)
    - 12.4 [高可用設計](#124-高可用設計)
    - 12.5 [Dev / Stage / Prod 環境設計](#125-dev--stage--prod-環境設計)
13. [安全、隱私與合規（Security & Compliance）](#13-安全隱私與合規security--compliance)
    - 13.1 [威脅模型](#131-威脅模型)
    - 13.2 [Proxy 認證強化](#132-proxy-認證強化)
    - 13.3 [憑證與金鑰管理](#133-憑證與金鑰管理)
    - 13.4 [資料外流與駐留風險](#134-資料外流與駐留風險)
    - 13.5 [Prompt Injection 與供應鏈風險](#135-prompt-injection-與供應鏈風險)
    - 13.6 [服務條款與授權合規](#136-服務條款與授權合規)
    - 13.7 [安全基線設定檔](#137-安全基線設定檔)
14. [CI/CD 整合](#14-cicd-整合)
    - 14.1 [GitHub Actions 範例](#141-github-actions-範例)
    - 14.2 [CI/CD 整合架構](#142-cicd-整合架構)
    - 14.3 [自建 Runner 注意事項](#143-自建-runner-注意事項)
15. [開發與貢獻指南（Development & Contributing）](#15-開發與貢獻指南development--contributing)
    - 15.1 [開發環境設定](#151-開發環境設定)
    - 15.2 [本地 CI 流程](#152-本地-ci-流程)
    - 15.3 [程式碼規範](#153-程式碼規範)
    - 15.4 [架構原則](#154-架構原則)
    - 15.5 [版本控管規則](#155-版本控管規則)
    - 15.6 [貢獻規則](#156-貢獻規則)
16. [常見問題（FAQ）](#16-常見問題faq)
17. [最佳實務（Best Practices）](#17-最佳實務best-practices)
    - 17.1 [架構設計](#171-架構設計)
    - 17.2 [Prompt Engineering](#172-prompt-engineering)
    - 17.3 [成本最佳化](#173-成本最佳化)
    - 17.4 [安全性](#174-安全性)
    - 17.5 [反模式清單](#175-反模式清單)
18. [範例 Prompt 集](#18-範例-prompt-集)
    - 18.1 [通用開發 Prompt](#181-通用開發-prompt)
    - 18.2 [Code Review Prompt](#182-code-review-prompt)
    - 18.3 [逆向工程 Prompt](#183-逆向工程-prompt)
    - 18.4 [升級評估 Prompt](#184-升級評估-prompt)
    - 18.5 [多模型交叉驗證 Prompt](#185-多模型交叉驗證-prompt)
    - 18.6 [FCC 環境診斷 Prompt](#186-fcc-環境診斷-prompt)
19. [導入檢查清單（Checklist）](#19-導入檢查清單checklist)
    - 19.1 [安裝與環境](#191-安裝與環境)
    - 19.2 [客戶端連線](#192-客戶端連線)
    - 19.3 [模型與路由](#193-模型與路由)
    - 19.4 [安全](#194-安全)
    - 19.5 [合規](#195-合規)
    - 19.6 [團隊導入](#196-團隊導入)
    - 19.7 [維運](#197-維運)
    - 19.8 [開發貢獻](#198-開發貢獻)
20. [附錄（Appendix）](#20-附錄appendix)
    - 20.1 [環境變數全表](#201-環境變數全表)
    - 20.2 [CLI 指令速查](#202-cli-指令速查)
    - 20.3 [API 端點速查](#203-api-端點速查)
    - 20.4 [名詞對照表](#204-名詞對照表)
    - 20.5 [參考資源](#205-參考資源)

---

## 1. 概述（Overview）

### 1.1 FCC 是什麼

Free Claude Code（FCC）是一套以 **Python 3.14 + FastAPI** 建構的**本機 AI 閘道（Local AI Gateway）**。它在開發者機器上啟動一個代理伺服器，同時對外提供兩種業界標準協議端點：

- **Anthropic Messages API**（`POST /v1/messages`）：服務 Claude Code、Cline、JetBrains ACP 等客戶端
- **OpenAI Responses API**（`POST /v1/responses`）：服務 Codex CLI、Codex App、Codex VS Code Extension

FCC 攔截這些請求後，依使用者設定的路由規則，將其**翻譯並轉發**至 50 家 LLM Provider 之一，再把上游回應**正規化**回客戶端期待的協議格式（含 SSE 串流、Tool Use、Thinking／Reasoning 區塊、影像輸入與 Usage 統計）。

對開發者而言，Claude Code 依然是那個 Claude Code；差別在於背後推理的模型可以是 NVIDIA NIM 的免費額度、本機 Ollama 上的量化模型，或企業自有的 Azure OpenAI 部署。

**專案現況（2026-09-08）**

| 指標 | 數值 |
|------|------|
| GitHub Stars | 53,825 |
| Forks | 8,632 |
| 套件版本 | `6.1.4` |
| 支援 Provider | 50 家 |
| 支援 Coding Agent | 10 種 |
| 授權 | MIT License |
| 執行環境 | Python 3.14（硬性需求）、uv 套件管理 |

### 1.2 核心價值主張

**（1）50 家 ToS-Friendly Provider，每月 13 億以上免費 Token**

上游專案明確採取「遵循各 Provider 服務條款」的立場：若某整合方式不再被 Provider 允許，該整合會被移除。這與部分逆向工程型代理專案有本質差異，也是企業評估時的重要區隔點。

**（2）十種 Coding Agent 共用同一份模型目錄**

Claude Code、Codex、Pi、OpenCode、Cline、Hermes、DeepSeek Harness、Grok Build、Muse Code、Aider —— 十種 Agent 共用同一組 Provider 設定與模型路由，不必為每個工具重複維護金鑰。

**（3）Provider 故障不中斷工作流**

當主模型重試耗盡後，FCC 會**自動改用 Fallback 清單中的下一個模型繼續同一輪對話**，無需使用者重啟 turn，且此行為對所有客戶端一致生效。這是 v6 系列最具維運價值的能力。

**（4）終端輸出 Token 最多減少 90%**

透過選配的 [RTK](https://github.com/rtk-ai/rtk) 過濾常見指令輸出，加上 FCC 內建的五項本地最佳化（配額探測、指令前綴偵測、標題生成、建議模式、檔案路徑擷取），大量瑣碎請求根本不會送達上游 Provider。

**（5）跨裝置工作介面**

原生啟動器（終端機）、桌面應用程式（Windows／macOS 系統匣）、VS Code、JetBrains、Codex App、瀏覽器內的 Code Sessions、Discord／Telegram 機器人，以及語音輸入。

**（6）Agent 能力完整保留**

串流回應、Tool Use、原生 interleaved thinking、影像輸入，並可將 Fable、Opus、Sonnet、Haiku 四個 Claude 階層獨立路由至不同模型。

### 1.3 與 Claude Code 官方訂閱的差異

| 比較構面 | Claude Code 官方 | Free Claude Code（FCC） |
|---------|-----------------|------------------------|
| 推理後端 | Anthropic 官方模型 | 50 家 Provider 任選（含本地） |
| 計費模式 | 訂閱制或 API 按量計費 | 依 Provider 而定，可全免費 |
| 模型品質 | Anthropic 前沿模型 | 依所選 Provider 而異，通常低於官方旗艦 |
| 部署形態 | SaaS | 自架本機代理 |
| 資料流向 | 送至 Anthropic | 送至所選 Provider；本地模型可完全離線 |
| 供應商故障 | 需等待官方復原 | 自動 Fallback 至次選模型 |
| 管理介面 | 無 | 內建 Admin UI（Web） |
| 多 Agent 支援 | 僅 Claude Code | 10 種 Coding Agent |
| 協議支援 | Anthropic Messages | Anthropic Messages + OpenAI Responses |
| 推理強度控制 | 由客戶端決定 | 可於閘道層統一覆寫（8 種等級） |
| 觀測與稽核 | 官方主控台 | 本機日誌、Smoke Test、Admin 狀態頁 |
| 官方支援 | Anthropic 提供 | 社群支援（GitHub Issues） |
| 企業合約／SLA | 有 | 無 |

> **決策提醒**：FCC 的價值在於**成本結構、資料主權與供應商彈性**，而非模型品質超越官方。若團隊的核心瓶頸是模型能力上限（如大規模重構、複雜推理），官方訂閱仍是較佳選擇；FCC 更適合作為**成本敏感任務的分流層**或**離線／管制環境的替代方案**。

### 1.4 適用場景與不適用場景

**適用場景**

| 場景 | 說明 | 建議 Provider |
|------|------|--------------|
| 機敏資料開發 | 程式碼不得離開企業網域 | LM Studio / llama.cpp / Ollama |
| 成本敏感專案 | 大量例行程式碼工作 | DeepSeek / Z.ai / OpenRouter 免費模型 |
| 個人開發者 | 無預算但需完整 Agent 體驗 | NVIDIA NIM / Groq / Google AI Studio |
| 既有企業雲 | 已購 Azure／GCP／AWS 額度 | Azure OpenAI / Vertex AI / Bedrock |
| 訂閱資源再利用 | 已有 ChatGPT／Copilot 訂閱 | OpenAI Connected Account / GitHub Copilot |
| 供應商韌性需求 | 不可接受單一供應商中斷 | 多 Provider + Fallback Chain |
| 遠端／行動協作 | 通勤或離開座位時推進任務 | Discord / Telegram Bot + 語音 |
| 模型評測 | 同一任務橫向比較多模型 | OpenRouter / 多 Provider 並行 |

**不適用場景**

| 場景 | 原因 |
|------|------|
| 需要合約級 SLA 的正式生產系統 | FCC 為社群專案，無 SLA 保證 |
| 高度依賴模型頂級推理能力的任務 | 免費模型能力與旗艦模型有落差 |
| 團隊共用單一 Provider 帳號 | 多數 Provider ToS 禁止帳號共用（見 [13.6](#136-服務條款與授權合規)） |
| 需通過嚴格供應鏈稽核的環境 | 需自行完成安裝腳本與依賴稽核 |
| 期待繞過第三方付費牆 | FCC 不提供此能力，亦不應如此期待 |

### 1.5 版本演進與重大變更

以下為由早期版本（本手冊 v1／v2 所依據）升級至 `v6.x` 的**破壞性變更**，既有使用者升級前務必確認：

| 項目 | 舊版行為 | v6.x 現行行為 |
|------|---------|--------------|
| 設定檔位置 | `~/.config/free-claude-code/.env` 或專案內 `.env` | `~/.fcc/.env`（啟動時自動遷移舊路徑） |
| 初始化指令 | `fcc-init` | **已移除**，改由 Admin UI 建立與管理 |
| 啟動方式 | `uvicorn server:app` | `fcc-server`，或桌面應用程式圖示 |
| 專案結構 | 根目錄扁平模組（`api/`、`providers/`…） | `src/free_claude_code/` 標準 src-layout |
| 安裝腳本路徑 | `main/install.sh` | `main/scripts/install.sh` |
| Windows 安裝 | `irm ... \| iex` | `& ([scriptblock]::Create((irm ...)))` |
| Thinking 控制 | `ENABLE_MODEL_THINKING` 等布林旗標 | `REASONING_POLICY` 等八段式推理等級 |
| 模型階層 | Opus / Sonnet / Haiku | **新增 Fable 階層**（`MODEL_FABLE`） |
| 故障處理 | 直接回傳錯誤 | `MODEL_FALLBACKS` 自動轉移 |
| 協議端點 | 僅 `/v1/messages` | 新增 `/v1/responses`（OpenAI Responses） |
| 客戶端 | Claude Code、Codex | 10 種 Coding Agent |
| Provider 數量 | 18 家 | 50 家 |

> ⚠️ **升級注意**：`ENABLE_MODEL_THINKING`、`ENABLE_OPUS_THINKING` 等舊變數已不再讀取。FCC 內建 `config/env_migrations.py` 處理已移除變數，但**推理行為的語意已改變**，升級後應重新檢視 `REASONING_POLICY` 設定。

### 1.6 架構定位圖

```mermaid
graph TB
    subgraph CLIENT["客戶端層（10 種 Agent + 多介面）"]
        CC[Claude Code]
        CX[Codex CLI / App]
        PI[Pi]
        OC[OpenCode]
        CL[Cline]
        HM[Hermes]
        DSH[DeepSeek Harness]
        GB[Grok Build]
        MC[Muse Code]
        AD[Aider]
        IDE[VS Code / JetBrains]
        BOT[Discord / Telegram]
        WEB[瀏覽器 Code Sessions]
    end

    subgraph GATEWAY["FCC 本機閘道（FastAPI :8082）"]
        API["協議端點<br/>/v1/messages<br/>/v1/responses"]
        ADMIN["Admin UI<br/>/admin"]
        ROUTE["路由與 Fallback<br/>Fable / Opus / Sonnet / Haiku"]
        OPT["Token 最佳化<br/>5 項本地攔截 + RTK"]
    end

    subgraph FREE["免費／Freemium Provider"]
        NIM[NVIDIA NIM]
        OR[OpenRouter]
        GRQ[Groq]
        GEM[Google AI Studio]
        CER[Cerebras]
    end

    subgraph SUB["訂閱制 Provider"]
        OAI[OpenAI / ChatGPT]
        GHC[GitHub Copilot]
        ZAI[Z.ai Coding]
        KMC[Kimi Code]
        QWC[QwenCloud Coding]
    end

    subgraph ENT["企業雲 Provider"]
        AZ[Azure OpenAI]
        VTX[Vertex AI]
        BR[Amazon Bedrock]
    end

    subgraph LOCAL["本地 Provider（離線）"]
        LMS[LM Studio]
        LCP[llama.cpp]
        OLL[Ollama]
    end

    CC --> API
    CX --> API
    PI --> API
    OC --> API
    CL --> API
    HM --> API
    DSH --> API
    GB --> API
    MC --> API
    AD --> API
    IDE --> API
    BOT --> API
    WEB --> API

    ADMIN -.設定.- ROUTE
    API --> OPT
    OPT --> ROUTE

    ROUTE --> FREE
    ROUTE --> SUB
    ROUTE --> ENT
    ROUTE --> LOCAL
```

> **實務建議**：初次導入請先用 NVIDIA NIM（免費額度充足、預設模型即可用）走通端到端流程，確認 Agent 行為正常後，再依 [5.9 節](#59-provider-選型決策矩陣)導入正式 Provider 組合。

> **常見錯誤**：將 `ANTHROPIC_BASE_URL` 設為 `http://localhost:8082/v1`（多了 `/v1`）。Anthropic 客戶端應指向服務根路徑 `http://localhost:8082`；只有 Codex 的 `base_url` 才需要 `/v1` 後綴。

---

## 2. 系統整體架構（Architecture）

### 2.1 高階架構圖

```mermaid
graph LR
    subgraph L1["客戶端層"]
        A1["Anthropic 協議客戶端<br/>Claude Code / Cline / JetBrains ACP"]
        A2["OpenAI Responses 客戶端<br/>Codex CLI / Codex App / Codex VS Code"]
        A3["FCC 原生介面<br/>Admin UI / Code Sessions / Bot"]
    end

    subgraph L2["API 層（api/）"]
        B1["routes.py<br/>/v1/messages · /v1/responses<br/>/v1/models · /health · /stop"]
        B2["handlers/<br/>messages · responses · token_count"]
        B3["optimization_handlers.py<br/>本地攔截"]
        B4["admin_routes.py<br/>code_sessions_routes.py"]
        B5["web_tools/<br/>web_search · web_fetch"]
    end

    subgraph L3["應用層（application/）"]
        C1["routing.py<br/>模型階層解析"]
        C2["execution.py<br/>執行與 Fallback"]
        C3["reasoning.py<br/>推理強度決策"]
        C4["connected_accounts.py<br/>訂閱帳號授權"]
        C5["code_sessions/<br/>瀏覽器工作階段"]
    end

    subgraph L4["核心協議層（core/）"]
        D1["anthropic/<br/>Messages 協議正規化<br/>thinking · tool_use · usage"]
        D2["openai_responses/<br/>Responses 協議正規化"]
    end

    subgraph L5["Provider 層（providers/）"]
        E1["openai_chat<br/>多數 Provider 共用"]
        E2["anthropic_messages"]
        E3["openai_responses / openai_codex"]
        E4["gemini · vertex · cloudflare<br/>deepseek · groq · kilo · mistral<br/>github_copilot · lmstudio · opencode"]
        E5["runtime/<br/>factory · registry"]
    end

    subgraph L6["執行環境層（runtime/ · config/ · cli/ · messaging/）"]
        F1["bootstrap.py · asgi.py<br/>服務啟動"]
        F2["provider_manager.py<br/>Provider 生命週期"]
        F3["config/<br/>settings · provider_catalog · admin"]
        F4["cli/launchers/<br/>10 種 Agent 啟動器"]
        F5["messaging/<br/>Discord · Telegram · 語音"]
    end

    A1 --> B1
    A2 --> B1
    A3 --> B4

    B1 --> B2
    B2 --> B3
    B3 --> C1
    B2 --> B5

    C1 --> C3
    C3 --> C2
    C4 -.授權.- C2
    C5 --> C2

    C2 --> D1
    C2 --> D2

    D1 --> E1
    D1 --> E2
    D2 --> E3
    E1 --> E4
    E5 -.建構.- E1

    F1 --> B1
    F2 -.管理.- E5
    F3 -.設定.- C1
    F4 --> A1
    F5 --> B1
```

**分層職責**

| 層級 | 目錄 | 職責 | 不得做的事 |
|------|------|------|-----------|
| API 層 | `api/` | HTTP 端點、認證、請求生命週期、SSE 串流 | 不含 Provider 專屬邏輯 |
| 應用層 | `application/` | 路由決策、執行編排、Fallback、帳號授權 | 不直接組 HTTP 請求 |
| 核心協議層 | `core/` | Anthropic／OpenAI 協議之共用正規化 | 不 import 任何 Provider 實作 |
| Provider 層 | `providers/` | 各家上游 API 的 transport 與差異處理 | 不跨 Provider 互相 import |
| 執行環境層 | `runtime/`、`config/`、`cli/`、`messaging/` | 啟動、設定、CLI 啟動器、訊息平台 | 不承載業務路由邏輯 |

> **架構要點**：專案以合約測試（`tests/contracts/`）強制「`config/provider_catalog.py` 不得 import Provider 實作」等邊界規則。這使得新增 Provider 只需擴充目錄與 factory，不會污染核心協議層——這是評估其可維護性的重要指標。

### 2.2 分層架構與原始碼結構

```text
free-claude-code/
├── src/free_claude_code/
│   ├── api/                       # FastAPI 端點與請求生命週期
│   │   ├── routes.py              # /v1/messages、/v1/responses、/v1/models、/health、/stop
│   │   ├── admin_routes.py        # Admin UI 與 /admin/api/*
│   │   ├── code_sessions_routes.py# 瀏覽器 Code Sessions（SSE 事件流）
│   │   ├── handlers/              # messages / responses / token_count / classifier
│   │   ├── optimization_handlers.py # 本地攔截最佳化
│   │   ├── response_streams.py    # SSE 串流組裝
│   │   ├── web_tools/             # web_search / web_fetch（含 SSRF 防護 egress.py）
│   │   ├── admin_security.py      # Admin 存取控制
│   │   └── admin_static/          # Admin UI 前端資產
│   ├── application/               # 與框架無關的應用邏輯
│   │   ├── routing.py             # 模型階層解析
│   │   ├── execution.py           # 執行編排與 Fallback
│   │   ├── reasoning.py           # 推理強度決策
│   │   ├── model_metadata.py      # 模型能力中繼資料
│   │   ├── connected_accounts.py  # ChatGPT / GitHub Copilot 帳號連結
│   │   └── code_sessions/         # Code Sessions 領域模型與服務
│   ├── core/
│   │   ├── anthropic/             # Anthropic Messages 協議共用邏輯
│   │   └── openai_responses/      # OpenAI Responses 協議共用邏輯
│   ├── providers/                 # 每家 Provider 一個子目錄
│   │   ├── openai_chat/           # 多數 OpenAI 相容 Provider 共用
│   │   ├── anthropic_messages/
│   │   ├── openai_responses/ · openai_codex/
│   │   ├── gemini/ · vertex/ · cloudflare/ · deepseek/ · groq/
│   │   ├── kilo/ · mistral/ · opencode/ · lmstudio/ · github_copilot/
│   │   └── runtime/               # factory 與 registry
│   ├── config/
│   │   ├── settings.py            # Pydantic 設定綱要（純驗證，無 I/O）
│   │   ├── provider_catalog.py    # 50 家 Provider 中繼資料與預設端點
│   │   ├── reasoning.py           # ReasoningPreference 列舉
│   │   ├── env_files.py · env_migrations.py  # .env 讀寫與舊變數遷移
│   │   ├── paths.py               # ~/.fcc 目錄配置
│   │   ├── provider_proxies.py    # Per-Provider 企業 Proxy
│   │   └── admin/                 # Admin UI 設定綱要、驗證與持久化
│   ├── runtime/
│   │   ├── bootstrap.py · asgi.py # 服務啟動與 ASGI 組裝
│   │   ├── provider_manager.py    # Provider 生命週期管理
│   │   ├── codex_app_server.py    # Codex App 協議服務
│   │   ├── codex_catalog.py       # 產生 codex-model-catalog.json
│   │   └── code_sessions_sqlite.py# Code Sessions 持久化（SQLite）
│   ├── cli/
│   │   ├── entrypoints.py         # fcc-server
│   │   ├── launchers/             # 10 種 Agent 啟動器 + 模型目錄產生
│   │   ├── managed/               # 受管 Claude 子行程與診斷
│   │   ├── desktop*.py            # 桌面應用程式與系統匣
│   │   └── process_registry.py    # 行程註冊與清理
│   └── messaging/
│       ├── platforms/             # Discord / Telegram 介面實作
│       ├── session/ · transcript/ · trees/ · rendering/
├── smoke/                         # Live E2E Smoke Tests（prereq / product）
├── tests/                         # Hermetic 單元測試與合約測試
├── e2e/                           # 端對端測試
├── scripts/                       # install / uninstall / ci（.sh 與 .ps1）
├── .env.example                   # 環境變數完整參考（425 行）
├── pyproject.toml                 # 套件定義、entry points、Ruff/Pytest 設定
├── uv.lock                        # 依賴鎖定
├── AGENTS.md                      # Agentic coding 指引
└── CONTRIBUTING.md                # 貢獻與品質流程
```

> **注意**：舊版手冊提及的 `server.py`、`CLAUDE.md`、`PLAN.md` 已不存在於現行版本；`fcc-init` 指令亦已移除。

### 2.3 Request Flow：Anthropic Messages 路徑

此為 Claude Code、Cline、JetBrains ACP 使用的主要路徑。

```mermaid
sequenceDiagram
    autonumber
    participant C as Claude Code
    participant A as API 層 /v1/messages
    participant O as 最佳化攔截
    participant R as 路由層
    participant X as 執行層
    participant N as core/anthropic
    participant P as Provider Transport
    participant U as 上游 Provider

    C->>A: POST /v1/messages（Anthropic 格式）
    A->>A: Bearer Token 驗證（PROXY_AUTH_ENABLED）
    A->>O: 判斷是否為可本地回應的請求
    alt 命中最佳化（配額探測 / 標題 / 建議 / 路徑擷取）
        O-->>C: 直接本地回應（0 上游 Token）
    else 一般請求
        O->>R: 解析 model 名稱
        R->>R: 依 Fable/Opus/Sonnet/Haiku 階層解析目標模型
        R->>X: 交付執行計畫（主模型 + Fallback 清單）
        X->>N: 套用 Reasoning 政策、正規化請求
        N->>P: 轉換為 Provider 原生格式
        P->>U: 發送請求（含 Per-Provider Proxy / 速率限制）
        U-->>P: SSE 串流
        P-->>N: 原生事件
        N-->>A: 正規化為 Anthropic SSE<br/>thinking / tool_use / usage
        A-->>C: SSE 串流
    end

    alt 上游重試耗盡
        X->>X: 取 Fallback 清單下一個模型
        X->>N: 於同一 turn 內重新執行
    end
```

**協議正規化重點**

| 面向 | FCC 處理方式 |
|------|-------------|
| Thinking / Reasoning | 保留原生 interleaved thinking；不支援的上游則轉為對應區塊或省略 |
| Tool Use | 將 Anthropic `tool_use` / `tool_result` 與 OpenAI `tool_calls` 雙向轉換 |
| 影像輸入 | Anthropic image block 轉為上游可接受的多模態格式 |
| Usage 統計 | 補齊 `input_tokens` / `output_tokens`；缺漏時以 `tiktoken` 估算 |
| `max_tokens` 預設 | 客戶端未帶時採 `81920` |
| 串流中斷 | 由 `request_lifetime.py` 統一清理，釋放上游連線與併發額度 |

### 2.4 Request Flow：OpenAI Responses 路徑

Codex 系列客戶端使用 OpenAI Responses 協議（`wire_api = "responses"`），FCC 以獨立的 `core/openai_responses/` 處理。

```mermaid
sequenceDiagram
    autonumber
    participant X as Codex CLI / App / VS Code
    participant A as API 層 /v1/responses
    participant R as 路由層
    participant N as core/openai_responses
    participant P as Provider Transport
    participant U as 上游 Provider

    X->>A: POST /v1/responses
    Note over X,A: 認證 Token 由 fcc-codex --print-proxy-auth-token 提供
    A->>R: 解析 model（fcc 目錄中的 provider/model）
    R->>N: 套用 Reasoning 與模型能力中繼資料
    N->>P: 轉換為上游格式（Chat Completions 或原生 Responses）
    P->>U: 發送請求
    U-->>P: 串流事件
    P-->>N: 原生事件
    N-->>A: 正規化為 Responses 事件流
    A-->>X: SSE 串流
```

> **設計意義**：兩條協議路徑共用同一套路由、Fallback、Reasoning 與 Provider 層。這代表**設定一次即可服務所有 Agent**，是 FCC 相對於「一個工具一個代理」方案的主要架構優勢。

### 2.5 模型路由與階層繼承

**模型參照格式**：`<provider-id>/<exact-provider-model-id>`

範例：`nvidia_nim/nvidia/nemotron-3-super-120b-a12b`、`open_router/openrouter/free`、`lmstudio/qwen3.5-coder`

`config/settings.py` 於載入時即驗證此格式；provider 前綴必須存在於 `SUPPORTED_PROVIDER_IDS`，否則啟動即報錯並列出合法清單。

**四層階層路由**

```text
Claude Code 送出的模型階層      FCC 解析順序
────────────────────────────────────────────────
Fable   → MODEL_FABLE   → 未設定則回落 MODEL
Opus    → MODEL_OPUS    → 未設定則回落 MODEL
Sonnet  → MODEL_SONNET  → 未設定則回落 MODEL
Haiku   → MODEL_HAIKU   → 未設定則回落 MODEL
其他／無法辨識            → MODEL（必填）
```

**混合路由範例**

```dotenv
MODEL="zai/glm-5.2"
MODEL_FABLE="openai/gpt-5.5"
MODEL_OPUS="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
MODEL_SONNET="open_router/openrouter/free"
MODEL_HAIKU="lmstudio/qwen3.5-coder"
```

此設定的效果是：架構級任務走 NIM 大模型、日常編碼走 OpenRouter 免費模型、瑣碎任務走本機模型、其餘一律走 Z.ai。

> **實務建議**：Haiku 階層在 Claude Code 中承擔大量背景小任務（檔案摘要、指令分類）。將 `MODEL_HAIKU` 指向本地模型或極速 Provider（Groq／Cerebras），對整體體感延遲的改善最明顯，同時大幅節省雲端配額。

### 2.6 Fallback Chain 自動故障轉移

`MODEL_FALLBACKS` 是一份**有序**的模型清單。當主模型的重試策略耗盡後，FCC 會依序嘗試清單中的下一個模型，**在同一輪對話內**完成切換，使用者不需重新輸入指令。

```mermaid
graph TD
    START([請求進入]) --> M1[嘗試主模型<br/>MODEL / MODEL_TIER]
    M1 --> OK1{成功?}
    OK1 -->|是| DONE([回傳結果])
    OK1 -->|否，重試耗盡| F1[Fallback #1]
    F1 --> OK2{成功?}
    OK2 -->|是| DONE
    OK2 -->|否| F2[Fallback #2]
    F2 --> OK3{成功?}
    OK3 -->|是| DONE
    OK3 -->|否| FN[…依序至清單結尾]
    FN --> FAIL([回傳錯誤給客戶端])
```

**設定範例**

```dotenv
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
MODEL_FALLBACKS="groq/llama-3.3-70b-versatile,deepseek/deepseek-chat,ollama/qwen3-coder"
```

**設計原則**

| 原則 | 說明 |
|------|------|
| 異質供應商 | Fallback 應跨不同供應商，避免單一雲端區域故障導致全鏈失效 |
| 能力對齊 | Fallback 模型須同樣支援 Tool Use，否則 Agent 會在中途失去工具能力 |
| 收斂於本地 | 建議鏈尾放一個本地模型，確保離線時仍可低速運作 |
| 不得重複 | 設定中出現重複模型參照會在啟動時驗證失敗 |

> ⚠️ **成本警告**：一次失敗的請求可能**依序觸達多個 Provider 並各自消耗配額**。若 Fallback 鏈中含付費 Provider，請務必評估最壞情況的成本，並搭配 [10.3 節](#103-成本控管策略)的預算控管。

### 2.7 Reasoning 推理強度控制

FCC 允許在閘道層**統一覆寫**客戶端送出的推理強度，這是既有 Proxy 方案少見的治理能力。

| 設定值 | 行為 |
|--------|------|
| `client`（預設） | 沿用客戶端送出的 effort；客戶端未指定時採 Provider 預設 |
| `off` | 要求上游關閉推理 |
| `low` / `medium` / `high` / `xhigh` / `max` | 以指定等級覆寫客戶端設定 |
| `inherit` | 僅適用於階層變數，表示沿用根層 `REASONING_POLICY` |

```dotenv
REASONING_POLICY=client
REASONING_FABLE=inherit
REASONING_OPUS=inherit
REASONING_SONNET=inherit
REASONING_HAIKU=inherit
```

**實務組態範例**

```dotenv
# 成本優先：全域降推理，僅架構級任務開高
REASONING_POLICY=low
REASONING_OPUS=high
REASONING_HAIKU=off
```

> **注意**：`REASONING_POLICY` 不可設為 `inherit`（根層無可繼承對象），設定檔驗證會直接拒絕。不支援該控制的 Provider 會保留自身預設行為，FCC 不會因此報錯。

### 2.8 Token 最佳化機制

FCC 的 Token 節省來自兩個獨立來源：**內建本地攔截**與**選配的 RTK 輸出過濾**。

**（1）五項內建本地攔截**（預設全開）

| 最佳化 | 環境變數 | 說明 |
|--------|---------|------|
| 配額／網路探測模擬 | `ENABLE_NETWORK_PROBE_MOCK` | 本地回應 Agent 的連線與配額探測 |
| 標題生成跳過 | `ENABLE_TITLE_GENERATION_SKIP` | 不為對話標題呼叫上游 |
| 建議模式跳過 | `ENABLE_SUGGESTION_MODE_SKIP` | 略過自動建議請求 |
| 檔案路徑擷取模擬 | `ENABLE_FILEPATH_EXTRACTION_MOCK` | 本地完成路徑擷取 |
| 快速指令前綴偵測 | `FAST_PREFIX_DETECTION` | 以本地規則辨識指令前綴，免除分類請求 |

**（2）RTK 終端輸出過濾**

[RTK](https://github.com/rtk-ai/rtk) 為選配元件，於安裝時可勾選。它過濾常見指令的冗長輸出（建置日誌、測試輸出、套件安裝訊息），使進入上下文的內容大幅縮減；官方宣稱可減少最高 90% 的終端輸出 Token。

```mermaid
graph LR
    REQ[Agent 請求] --> CHK{可本地回應?}
    CHK -->|是| LOCAL[本地產生回應<br/>0 上游 Token]
    CHK -->|否| RTKF{終端輸出?}
    RTKF -->|是| RTK[RTK 過濾冗餘]
    RTKF -->|否| PASS[原樣傳遞]
    RTK --> UP[送至上游 Provider]
    PASS --> UP
```

> **實務建議**：在免費額度緊繃的情境（如 NVIDIA NIM 每分鐘請求數限制），保持五項最佳化全開可顯著降低請求數；除非要重現特定 Agent 行為以進行除錯，否則不建議關閉。

### 2.9 擴充點（Extension Points）

| 擴充需求 | 做法 | 主要檔案 |
|---------|------|---------|
| 新增 OpenAI 相容 Provider | 沿用 `openai_chat` transport，僅補中繼資料 | `config/provider_catalog.py` |
| 新增 Anthropic 相容 Provider | 沿用 `anthropic_messages` transport | `config/provider_catalog.py` |
| 新增行為特殊的 Provider | 於 `providers/` 建立子目錄實作差異 | `providers/<name>/` |
| 註冊 Provider 建構 | 於 factory 加入 wiring | `providers/runtime/factory.py` |
| 新增訊息平台 | 實作平台介面 | `messaging/platforms/` |
| 新增 Coding Agent 啟動器 | 新增 launcher 與模型目錄產生器 | `cli/launchers/` |
| 新增設定欄位 | 於 Pydantic 綱要與 Admin 綱要同步宣告 | `config/settings.py`、`config/admin/specs.py` |

> **實務建議**：企業若需接入內部 LLM Gateway（vLLM、TGI、自建閘道），多數情況只需在 `provider_catalog.py` 新增一筆描述並指向自訂 `base_url`，沿用既有 `openai_chat` transport，無須撰寫新的 transport。

> **常見錯誤**：嘗試以 Docker 容器化部署。上游專案在 `CONTRIBUTING.md` 中明確拒絕 Docker 整合的 PR，且 FCC 深度依賴本機路徑（`~/.fcc`）、桌面系統匣與本機 Agent 行程管理。企業如需常駐服務，建議以 systemd（Linux）、launchd（macOS）或工作排程器（Windows）管理，而非容器化。

---

## 3. 安裝與環境建置（Installation）

### 3.1 系統需求

| 項目 | 最低需求 | 建議 | 備註 |
|------|---------|------|------|
| 作業系統 | Windows 10+ / macOS 12+ / Ubuntu 20.04+ | 最新穩定版 | Windows 與 macOS 有桌面應用程式與系統匣 |
| Python | 3.14.0 | 3.14.x 最新 | **硬性需求**，安裝腳本會自動安裝 |
| uv | 0.11.16+ | 最新版 | 專案指定之最低版本 |
| Node.js | 18+ | 22 LTS | 安裝 Claude Code／Codex CLI 所需 |
| 記憶體 | 4 GB | 8 GB+ | 使用本地模型時建議 16 GB 以上 |
| 磁碟空間 | 2 GB | 10 GB+ | 啟用本地 Whisper 或本地模型時需更多 |
| GPU | 非必要 | NVIDIA CUDA 13.0 | 僅本地 Whisper（`cuda`）或本地模型需要 |
| 網路 | 可連外 | — | 純本地 Provider 情境可完全離線 |

> **為何鎖定 Python 3.14**：專案採用 3.14 的原生延遲註解（lazy annotations）與多例外型別語法（`except TypeError, ValueError:`），並在規範中明文禁止 `from __future__ import annotations`。以 3.13 以下版本執行必然失敗。

**取得 Coding Agent 本體**

FCC 只是閘道，Agent 本體需另行安裝（安裝腳本會提示選取並協助安裝）：

```bash
npm install -g @anthropic-ai/claude-code   # Claude Code
npm install -g @openai/codex               # Codex CLI
```

### 3.2 安裝方式決策

| 情境 | 建議方式 | 理由 |
|------|---------|------|
| 個人開發者、快速評估 | 官方安裝腳本 | 一行完成，含桌面應用與 Agent 安裝引導 |
| 企業導入、需供應鏈稽核 | 原始碼安裝 | 可先審閱腳本與依賴、以內部鏡像鎖版 |
| 貢獻程式碼 / 客製 Provider | 原始碼安裝 | 可執行完整 CI 與測試 |
| CI／無人值守環境 | 原始碼安裝 + 環境變數注入 | 不需桌面元件與瀏覽器 |

### 3.3 方式一：官方安裝腳本（推薦）

**macOS / Linux**

```bash
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh
```

**Windows PowerShell**

```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.ps1")))
```

安裝過程會提示選取**至少一個 Coding Agent**，並可選擇是否安裝 RTK。重新執行相同指令即為更新。

**含語音支援的安裝變體**

| 目的 | macOS / Linux 參數 | Windows 參數 |
|------|-------------------|-------------|
| NVIDIA NIM 轉錄 | `sh -s -- --voice-nim` | `-VoiceNim` |
| 本地 Whisper（CPU/CUDA） | `sh -s -- --voice-local` | `-VoiceLocal` |
| 兩種後端皆裝 | `sh -s -- --voice-all` | `-VoiceAll` |
| 本地 Whisper + CUDA 13.0 | `sh -s -- --voice-local --torch-backend cu130` | `-VoiceLocal -TorchBackend cu130` |

```bash
# 範例：安裝並啟用本地 Whisper（CUDA 13.0）
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh -s -- --voice-local --torch-backend cu130
```

> ⚠️ **企業安全提醒**：`curl | sh` 形式的安裝在多數企業安全政策中屬於高風險行為。上游提供 [install.sh](https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh) 與 [install.ps1](https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1) 原始碼供審閱。建議企業先下載、稽核、內部簽章後再散布，勿直接管道執行。

### 3.4 方式二：原始碼安裝（稽核 / 開發）

```bash
# 1. 安裝 uv
curl -LsSf https://astral.sh/uv/install.sh | sh          # macOS / Linux
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"   # Windows

uv self update

# 2. 取得原始碼並鎖定 Python 版本
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code
uv python install 3.14.0

# 3. 直接由 checkout 執行
uv run fcc-server
```

若要以工具形式全域安裝：

```bash
uv tool install git+https://github.com/Alishahryar1/free-claude-code.git
```

> **規範提醒**：專案要求一律使用 `uv run` 執行 Python 指令，**不可**以系統全域直譯器執行，否則依賴解析與 Python 版本皆無法保證。

### 3.5 啟動 FCC 服務

| 平台 | 啟動方式 | 說明 |
|------|---------|------|
| Windows | 桌面或開始功能表的 **Free Claude Code** | 常駐系統匣，可開啟 Admin、重啟、離開 |
| macOS | 桌面或應用程式資料夾的 **Free Claude Code** | 常駐選單列 |
| Linux | `fcc-server` | 需保持該終端機開啟 |
| 全平台（開發） | `uv run fcc-server` | 由原始碼 checkout 執行 |

服務啟動後會**自動開啟 Admin UI**（可用 `FCC_OPEN_BROWSER=false` 關閉）。預設監聽 `0.0.0.0:8082`。

```bash
fcc-server --version    # 僅查詢版本，不啟動服務
```

> ⚠️ **預設綁定 0.0.0.0**：`HOST` 預設為 `0.0.0.0`，意即服務會監聽所有網路介面。在共用網段、咖啡廳 Wi-Fi 或未設防火牆的伺服器上，這等同對外開放。請務必依 [13.2 節](#132-proxy-認證強化)啟用 Proxy 認證，或將 `HOST` 改為 `127.0.0.1`。

### 3.6 首次設定（以 NVIDIA NIM 為例）

1. 於 [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys) 建立 API Key。
2. 開啟服務日誌中顯示的 Admin UI 網址（預設 `http://127.0.0.1:8082/admin`）。
3. 在 `NVIDIA_NIM_API_KEY` 欄位貼上金鑰。
4. `MODEL` 保留預設值 `nvidia_nim/nvidia/nemotron-3-super-120b-a12b`，或於下拉選單搜尋其他模型。
5. 點選 **Apply** 套用。
6. 建議同時於 Admin 啟用 **Proxy Authentication**，以 Bearer Token 保護本機代理。

> **實務建議**：v6 版本已將設定重心從 `.env` 手動編輯移至 Admin UI。除非是自動化部署或 CI 情境，否則優先使用 Admin UI——它會即時驗證模型參照格式與 Provider 連通性，可避免大量手誤。

### 3.7 啟動 Coding Agent

服務啟動後，於任一終端機執行對應指令即可：

```bash
fcc-claude      # Claude Code
fcc-codex       # Codex
fcc-pi          # Pi
fcc-opencode    # OpenCode
fcc-cline       # Cline
fcc-hermes      # Hermes
fcc-dsh         # DeepSeek Harness Web
fcc-grok        # Grok Build
fcc-muse        # Muse Code
fcc-aider       # Aider
```

這些啟動器會自動注入正確的 Base URL、認證 Token 與相容性環境變數，**不需手動設定環境變數**。

### 3.8 安裝驗證

```bash
# 1. 服務健康檢查
curl http://localhost:8082/health

# 2. 模型目錄（應列出所有已設定 Provider 的可用模型）
curl -H "Authorization: Bearer freecc" http://localhost:8082/v1/models

# 3. 版本確認
fcc-server --version
```

**Admin UI 驗證**

於瀏覽器開啟 `http://127.0.0.1:8082/admin`，確認：

- Provider 區塊顯示已設定金鑰之 Provider 為連線正常
- Model Config 中 `MODEL` 已選定且無驗證錯誤
- 狀態頁無啟動警告

**端到端驗證**

```bash
fcc-claude
# 於 Claude Code 中輸入 /model，確認可看到 FCC 提供的模型清單
# 接著送出一則簡單提示（例如「請以繁體中文說明本專案結構」）確認可正常回應
```

### 3.9 檔案與目錄配置

FCC 所有使用者狀態集中於 `~/.fcc/`（Windows 為 `%USERPROFILE%\.fcc\`）：

```text
~/.fcc/
├── .env                        # 主設定檔（Admin UI 讀寫）
├── config.lock                 # 跨行程設定遷移鎖
├── codex-model-catalog.json    # 供 Codex App / VS Code 使用的模型目錄
├── logs/
│   └── server.log              # 服務日誌（JSON sink）
├── auth/
│   ├── openai.json             # ChatGPT 連結帳號憑證
│   ├── openai.lock
│   └── github_copilot.json     # Copilot 連線狀態（憑證仍由原生 CLI 保管）
├── code/
│   ├── code.db                 # 瀏覽器 Code Sessions（SQLite）
│   └── code.lock
├── agent_workspace/            # Messaging Bot 的工作目錄
└── tmp/launchers/              # 各 Agent 啟動器的私有暫存設定
```

**舊路徑自動遷移**：FCC 啟動時會檢查 `~/free-claude-code/.env` 與 `~/.config/free-claude-code/.env`，若存在則遷移至 `~/.fcc/.env`。

> ⚠️ **備份與稽核重點**：`~/.fcc/.env` 與 `~/.fcc/auth/` 內含所有 Provider 金鑰與訂閱憑證，屬最高機密等級。應排除於任何備份同步、雲端硬碟與版本控制之外，並確保檔案權限僅限本人（`chmod 600`）。

### 3.10 更新與解除安裝

**更新**：重新執行 [3.3 節](#33-方式一官方安裝腳本推薦)的安裝指令即可，設定與憑證會保留。

**解除安裝**

```bash
# macOS / Linux
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/uninstall.sh" | sh
```

```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/uninstall.ps1")))
```

| 解除安裝會移除 | 解除安裝會保留 |
|---------------|---------------|
| FCC 本體、桌面啟動器與所有 `fcc-*` 指令 | uv 與 Python |
| `~/.fcc/`（含設定與憑證） | Claude Code、Codex、Pi、OpenCode、Cline、Hermes、DSH、Grok Build、Muse Code、Aider、RTK |
| — | 共用的 PATH 項目 |

> ⚠️ 解除安裝前務必**停止所有執行中的 FCC 指令**，且注意 `~/.fcc/` 會一併刪除——若需保留 Provider 設定，請先備份 `.env`。

**Muse Code 於原生 Windows 的獨立管理**

```powershell
# 僅安裝／更新受管的 Muse 執行檔
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install-muse.ps1")))

# 僅移除該受管執行檔（保留 Muse 資料與其他安裝）
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/uninstall-muse.ps1")))
```

### 3.11 環境建置流程圖

```mermaid
graph TD
    S1[確認系統需求<br/>OS / 記憶體 / Node.js] --> S2{安裝方式}
    S2 -->|快速評估| S3A[執行官方安裝腳本<br/>選取 Agent 與 RTK]
    S2 -->|企業稽核| S3B[稽核 install 腳本<br/>clone + uv run fcc-server]
    S3A --> S4[啟動 FCC<br/>桌面圖示 或 fcc-server]
    S3B --> S4
    S4 --> S5[Admin UI 自動開啟<br/>127.0.0.1:8082/admin]
    S5 --> S6[設定 Provider 金鑰]
    S6 --> S7[選定 MODEL 與階層路由]
    S7 --> S8[設定 MODEL_FALLBACKS]
    S8 --> S9[啟用 Proxy Authentication]
    S9 --> S10[Apply 套用設定]
    S10 --> S11[curl /health 與 /v1/models 驗證]
    S11 --> S12[執行 fcc-claude 端到端驗證]
    S12 --> S13{正常?}
    S13 -->|是| DONE([完成])
    S13 -->|否| DBG[檢視 ~/.fcc/logs/server.log<br/>參閱第 16 章 FAQ]
    DBG --> S6
```

> **常見錯誤**：使用舊版手冊的 `install.sh` 路徑（`main/install.sh`）。正確路徑已移至 `main/scripts/install.sh`；同時 `fcc-init` 指令已移除，勿再嘗試執行。

---

## 4. 核心設定（Configuration）

### 4.1 設定來源與優先權

FCC 的設定由 `config/loader.py` 統一載入，`config/settings.py` 以 Pydantic 綱要驗證。

```mermaid
graph LR
    ENV[作業系統環境變數] --> LOADER[config/loader.py]
    FILE["~/.fcc/.env"] --> LOADER
    ADMIN[Admin UI 寫入] --> FILE
    LOADER --> VALID[Pydantic 驗證<br/>settings.py]
    VALID --> RUN[執行期設定]
    VALID -.驗證失敗.-> ERR[啟動報錯並列出合法值]
```

| 設定方式 | 適用情境 | 生效時機 |
|---------|---------|---------|
| Admin UI | 日常使用（**推薦**） | 點選 Apply 後立即套用；部分項目會提示重啟 |
| `~/.fcc/.env` | 自動化部署、設定即程式碼 | 服務啟動時載入 |
| 作業系統環境變數 | CI／容器化外部注入 | 服務啟動時載入 |

> **重點**：Admin UI 的變更會**寫回 `~/.fcc/.env`**，兩者並非各自獨立的設定來源，而是同一份檔案的兩種編輯介面。因此手動編輯 `.env` 後需重啟服務；而 Admin UI 儲存後會直接覆寫檔案內容。

`.env.example`（425 行）為所有變數的權威參考，升級後應比對是否有新增項目。

### 4.2 Admin UI 設定面板

```text
http://127.0.0.1:8082/admin
```

| 分頁 | 主要設定 |
|------|---------|
| **Providers** | 各家 API Key／Base URL；Connected accounts（ChatGPT、GitHub Copilot）連結與中斷；連通性測試 |
| **Model Config** | `MODEL`、`MODEL_FABLE/OPUS/SONNET/HAIKU`、`MODEL_FALLBACKS`、Reasoning 等級 |
| **Server** | Port、Host、Proxy Authentication 開關與 Token |
| **Messaging** | Discord／Telegram 平台選擇、Token、允許頻道／使用者、允許目錄、語音設定 |
| **Code** | 瀏覽器 Code Sessions 管理與資料夾選取 |
| **Status** | 服務狀態、設定檔路徑、模型目錄重新整理 |

**主要 Admin API 端點**（供自動化整合參考）

| 端點 | 方法 | 用途 |
|------|------|------|
| `/admin/api/config` | GET | 讀取目前設定 |
| `/admin/api/config/apply` | POST | 套用設定變更 |
| `/admin/api/status` | GET | 服務與 Provider 狀態 |
| `/admin/api/providers/local-status` | GET | 本地 Provider 連通狀態 |
| `/admin/api/providers/{id}/test` | POST | 測試單一 Provider |
| `/admin/api/providers/{id}/auth/login` | POST | 啟動 Connected Account 授權 |
| `/admin/api/models` | GET | 取得可用模型清單 |
| `/admin/api/models/refresh` | POST | 重新整理模型目錄 |

> ⚠️ **Admin UI 無獨立密碼**。其防護依賴網路可及性與 `admin_security.py` 的存取控制。**絕不可將 8082 port 直接暴露於公開網路**；遠端管理請使用 SSH Tunnel（見 [13.2 節](#132-proxy-認證強化)）。

### 4.3 模型設定：MODEL、階層與 Fallback

```dotenv
# 必填：所有請求的預設模型
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"

# 選填：階層覆寫（留空則沿用 MODEL）
MODEL_FABLE=
MODEL_OPUS=
MODEL_SONNET=
MODEL_HAIKU=

# 選填：有序 Fallback 清單（逗號分隔，不得重複）
MODEL_FALLBACKS="groq/llama-3.3-70b-versatile,deepseek/deepseek-chat"
```

**驗證規則**

| 規則 | 違反時的行為 |
|------|-------------|
| 必須為 `provider/model` 格式 | 啟動失敗並提示格式 |
| provider 前綴須在支援清單中 | 啟動失敗並列出全部合法 provider id |
| model 後綴不得為空 | 啟動失敗 |
| `MODEL_FALLBACKS` 不得含重複項 | 啟動失敗 |

**模型無法列舉時的處理**：部分 Provider 不提供模型列舉 API。此時於 Admin UI 的 `MODEL` 欄位手動輸入完整參照 `<provider-id>/<exact-provider-model-id>` 即可（稱為 custom model slug）。

### 4.4 Reasoning 設定

```dotenv
REASONING_POLICY=client     # client | off | low | medium | high | xhigh | max
REASONING_FABLE=inherit     # 額外可用 inherit
REASONING_OPUS=inherit
REASONING_SONNET=inherit
REASONING_HAIKU=inherit
```

詳細語意見 [2.7 節](#27-reasoning-推理強度控制)。

### 4.5 Proxy 認證與服務連線

```dotenv
HOST="0.0.0.0"                  # 建議改為 127.0.0.1
PORT=8082
PROXY_AUTH_ENABLED=false        # 建議設為 true
ANTHROPIC_AUTH_TOKEN="freecc"   # 建議改為高強度隨機字串
FCC_OPEN_BROWSER=true           # 無頭環境請設為 false
```

**客戶端 Base URL 對照**

| 客戶端類型 | 設定項 | 正確值 |
|-----------|-------|-------|
| Anthropic 協議（Claude Code、Cline、JetBrains） | `ANTHROPIC_BASE_URL` | `http://localhost:8082` |
| OpenAI Responses 協議（Codex 系列） | `base_url` | `http://127.0.0.1:8082/v1` |

> ⚠️ 這是最常見的設定錯誤來源：**Anthropic 側不加 `/v1`，Codex 側必須加 `/v1`**。

### 4.6 速率限制與逾時

```dotenv
PROVIDER_RATE_LIMIT=1           # 每個時間窗內的最大請求數
PROVIDER_RATE_WINDOW=2          # 時間窗長度（秒）
PROVIDER_MAX_CONCURRENCY=2      # 最大並行請求數
PROVIDER_PROGRESS_TIMEOUT=600   # 串流無進展的逾時（秒）

HTTP_CONNECT_TIMEOUT=10         # 連線逾時（秒）
HTTP_READ_TIMEOUT=120           # 讀取逾時（秒）
HTTP_WRITE_TIMEOUT=10           # 寫入逾時（秒）
```

**調校建議**

| 情境 | 建議設定 |
|------|---------|
| 免費 Provider（額度嚴格） | 維持預設，或降至 `PROVIDER_MAX_CONCURRENCY=1` |
| 付費 Provider（額度充裕） | `PROVIDER_RATE_LIMIT=5`、`PROVIDER_MAX_CONCURRENCY=8` |
| 本地模型（CPU 推理） | `PROVIDER_MAX_CONCURRENCY=1`、`HTTP_READ_TIMEOUT=600` |
| 本地模型（GPU 推理） | `PROVIDER_MAX_CONCURRENCY=2~4` 視 VRAM 而定 |
| 大型推理模型（長思考） | 提高 `HTTP_READ_TIMEOUT` 與 `PROVIDER_PROGRESS_TIMEOUT` |

> **注意**：`PROVIDER_PROGRESS_TIMEOUT` 監控的是「串流是否仍有進展」，而非請求總時長。長時間思考但持續產出事件的模型不會被此逾時中斷。

### 4.7 請求最佳化開關

```dotenv
FAST_PREFIX_DETECTION=true
ENABLE_NETWORK_PROBE_MOCK=true
ENABLE_TITLE_GENERATION_SKIP=true
ENABLE_SUGGESTION_MODE_SKIP=true
ENABLE_FILEPATH_EXTRACTION_MOCK=true
```

全部預設為 `true`。僅在需重現特定 Agent 原生行為以除錯時才逐項關閉。

### 4.8 Web Tools 設定

FCC 於伺服器端提供 `web_search` 與 `web_fetch` 工具，使 Agent 在上游模型不具備網路能力時仍可查詢網路。

```dotenv
ENABLE_WEB_SERVER_TOOLS=true            # 預設開啟，對齊 Claude Code 原生行為
WEB_FETCH_ALLOWED_SCHEMES=http,https    # 允許的 URL scheme
WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false  # 是否允許存取私有網段
```

> ⚠️ **SSRF 風險**：`WEB_FETCH_ALLOW_PRIVATE_NETWORKS=true` 會解除對私有網段、loopback 與 link-local 位址的封鎖，使 Agent 可存取內網服務與雲端 metadata 端點（如 `169.254.169.254`）。**除隔離實驗環境外，務必保持 `false`**。FCC 的 `api/web_tools/egress.py` 即為此防護的實作點。

### 4.9 企業 Proxy（Per-Provider）

FCC 為**每一家** Provider 提供獨立的 Proxy 設定，支援 `http` 與 `socks5` 協議。

```dotenv
# 格式：http://username:password@host:port 或 socks5://host:port
NVIDIA_NIM_PROXY=""
OPENROUTER_PROXY=""
GROQ_PROXY=""
DEEPINFRA_PROXY=""
AZURE_OPENAI_PROXY=""
VERTEX_PROXY=""
LMSTUDIO_PROXY=""
LLAMACPP_PROXY=""
# …其餘 Provider 皆有對應的 <PROVIDER>_PROXY 變數
TELEGRAM_PROXY_URL=""
```

> **實務建議**：企業防火牆環境下，僅需為實際會連外的雲端 Provider 設定 Proxy；本地 Provider（LM Studio／llama.cpp／Ollama）應**留空**，否則本機請求會被錯誤地導向外部 Proxy 而失敗。

### 4.10 Messaging 與語音設定

```dotenv
MESSAGING_PLATFORM="discord"      # discord | telegram | none
DISCORD_BOT_TOKEN=""
ALLOWED_DISCORD_CHANNELS=""
TELEGRAM_BOT_TOKEN=""
ALLOWED_TELEGRAM_USER_ID=""
ALLOWED_DIR=""                    # 絕對路徑，Bot 可存取的目錄
MESSAGING_RATE_LIMIT=1
MESSAGING_RATE_WINDOW=1
MAX_MESSAGE_LOG_ENTRIES_PER_CHAT=""

VOICE_NOTE_ENABLED=true
WHISPER_DEVICE="cpu"              # cpu | cuda | nvidia_nim
WHISPER_MODEL="base"              # tiny/base/small/medium/large-v2/large-v3/large-v3-turbo
HUGGINGFACE_API_KEY=""            # 本地受管制 Whisper 模型需要
```

> ⚠️ **`ALLOWED_DIR` 是遠端存取的唯一邊界**。透過 Discord／Telegram 觸發的 Agent 會在此目錄下執行檔案操作與指令。務必設為專用的沙箱目錄，**絕不可設為家目錄或含機敏資料的專案根目錄**。

### 4.11 日誌與診斷設定

```dotenv
LOG_LEVEL=INFO                      # DEBUG | INFO | WARNING | ERROR | CRITICAL

# 以下皆預設 false，僅供本機除錯
LOG_RAW_API_PAYLOADS=false          # 記錄原始 API 請求／回應
LOG_RAW_SSE_EVENTS=false            # 記錄原始 SSE 事件
LOG_API_ERROR_TRACEBACKS=false      # 記錄 API 錯誤堆疊
LOG_RAW_MESSAGING_CONTENT=false     # 記錄訊息內容預覽
LOG_RAW_CLI_DIAGNOSTICS=false       # 記錄 Agent CLI 的 stderr 與非 JSON stdout
LOG_MESSAGING_ERROR_DETAILS=false   # 記錄訊息平台錯誤細節
DEBUG_PLATFORM_EDITS=false
DEBUG_SUBAGENT_STACK=false
```

> ⚠️ **資料外洩警告**：`LOG_RAW_*` 系列會將 Prompt 全文、工具參數、檔案路徑與模型輸出寫入 `~/.fcc/logs/server.log`。這些內容通常包含原始碼與商業機密。生產或共用環境**必須全部保持 `false`**；除錯後應立即關閉並清理日誌檔。

### 4.12 環境變數完整速查表

| 類別 | 關鍵變數 | 必填 | 預設值 |
|------|---------|------|--------|
| 核心模型 | `MODEL` | ✅ | `nvidia_nim/nvidia/nemotron-3-super-120b-a12b` |
| 階層路由 | `MODEL_FABLE`、`MODEL_OPUS`、`MODEL_SONNET`、`MODEL_HAIKU` | ❌ | 空（沿用 `MODEL`） |
| 故障轉移 | `MODEL_FALLBACKS` | ❌ | 空 |
| 推理控制 | `REASONING_POLICY`、`REASONING_FABLE/OPUS/SONNET/HAIKU` | ❌ | `client` / `inherit` |
| 服務 | `HOST`、`PORT`、`FCC_OPEN_BROWSER` | ❌ | `0.0.0.0` / `8082` / `true` |
| 認證 | `PROXY_AUTH_ENABLED`、`ANTHROPIC_AUTH_TOKEN` | ❌ | `false` / `freecc` |
| Provider 金鑰 | `<PROVIDER>_API_KEY` 等 | 至少一組 | 空 |
| 本地 Provider | `LM_STUDIO_BASE_URL`、`LLAMACPP_BASE_URL`、`OLLAMA_BASE_URL` | ❌ | 見 [5.8 節](#58-本地-provider) |
| 速率／並行 | `PROVIDER_RATE_LIMIT`、`PROVIDER_RATE_WINDOW`、`PROVIDER_MAX_CONCURRENCY`、`PROVIDER_PROGRESS_TIMEOUT` | ❌ | `1` / `2` / `2` / `600` |
| 逾時 | `HTTP_CONNECT_TIMEOUT`、`HTTP_READ_TIMEOUT`、`HTTP_WRITE_TIMEOUT` | ❌ | `10` / `120` / `10` |
| 最佳化 | `FAST_PREFIX_DETECTION`、`ENABLE_*_MOCK`、`ENABLE_*_SKIP` | ❌ | 全 `true` |
| Web Tools | `ENABLE_WEB_SERVER_TOOLS`、`WEB_FETCH_ALLOWED_SCHEMES`、`WEB_FETCH_ALLOW_PRIVATE_NETWORKS` | ❌ | `true` / `http,https` / `false` |
| 企業 Proxy | `<PROVIDER>_PROXY`、`TELEGRAM_PROXY_URL` | ❌ | 空 |
| Messaging | `MESSAGING_PLATFORM`、`*_BOT_TOKEN`、`ALLOWED_*`、`ALLOWED_DIR` | ❌ | 見 [4.10 節](#410-messaging-與語音設定) |
| 語音 | `VOICE_NOTE_ENABLED`、`WHISPER_DEVICE`、`WHISPER_MODEL` | ❌ | `true` / `cpu` / `base` |
| 日誌 | `LOG_LEVEL`、`LOG_RAW_*`、`DEBUG_*` | ❌ | `INFO` / 全 `false` |
| 客戶端相容 | `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`、`CLAUDE_CODE_AUTO_COMPACT_WINDOW` | ❌ | 由 `fcc-*` 啟動器自動注入 |
| Smoke 測試 | `FCC_LIVE_SMOKE`、`FCC_SMOKE_TARGETS`、`FCC_SMOKE_MODEL_*` | ❌ | 見 [第 11 章](#11-品質驗證測試與-smoke-testing) |

完整清單見 [20.1 節](#201-環境變數全表)與上游 `.env.example`。

---

## 5. Provider 生態系（50 家供應商）

### 5.1 Provider 分類全覽

```mermaid
graph TB
    FCC[FCC 閘道]

    subgraph G1["聚合閘道（Aggregator）"]
        A1[OpenRouter]
        A2[Vercel AI Gateway]
        A3[ZenMux]
        A4[TokenRouter]
        A5[NaraRoute]
        A6[Kilo.ai]
        A7[Hugging Face Router]
    end

    subgraph G2["推理雲（Inference Cloud）"]
        B1[NVIDIA NIM]
        B2[Groq]
        B3[Cerebras]
        B4[SambaNova]
        B5[Together AI]
        B6[DeepInfra]
        B7[Fireworks AI]
        B8[Novita AI]
        B9[SiliconFlow]
        B10[Nebius]
        B11[Chutes]
        B12[Featherless]
        B13[W&B Inference]
        B14[LLM7.io]
    end

    subgraph G3["模型原廠（First-party）"]
        C1[DeepSeek]
        C2[Google AI Studio]
        C3[Mistral / Codestral]
        C4[xAI Grok]
        C5[Kimi / Moonshot]
        C6[MiniMax]
        C7[Z.ai / GLM]
        C8[Cohere]
        C9[QwenCloud]
        C10[Poolside AI]
        C11[Agnes AI]
        C12[Wafer]
    end

    subgraph G4["企業雲（Enterprise Cloud）"]
        D1[Azure OpenAI]
        D2[Google Vertex AI]
        D3[Amazon Bedrock]
        D4[Cloudflare Workers AI]
    end

    subgraph G5["訂閱制（Subscription）"]
        E1[OpenAI / ChatGPT]
        E2[GitHub Copilot]
        E3[ClinePass]
        E4[Kimi Code]
        E5[QwenCloud Coding]
        E6[Z.ai Coding Plan]
        E7[OpenCode Zen / Go]
    end

    subgraph G6["本地（Local）"]
        F1[LM Studio]
        F2[llama.cpp]
        F3[Ollama]
        F4[Ollama Cloud]
    end

    FCC --> G1
    FCC --> G2
    FCC --> G3
    FCC --> G4
    FCC --> G5
    FCC --> G6
```

### 5.2 完整 Provider 目錄

下表為 `config/provider_catalog.py` 中登錄的全部 50 家 Provider。「前綴」即模型參照 `<provider-id>/<model-id>` 的第一段。

| # | Provider | 前綴 | 認證設定 | 預設端點 |
|---|----------|------|---------|---------|
| 1 | [NVIDIA NIM](https://build.nvidia.com/settings/api-keys) | `nvidia_nim` | `NVIDIA_NIM_API_KEY` | `https://integrate.api.nvidia.com/v1` |
| 2 | [OpenRouter](https://openrouter.ai/keys) | `open_router` | `OPENROUTER_API_KEY` | `https://openrouter.ai/api/v1` |
| 3 | [Groq](https://console.groq.com/keys) | `groq` | `GROQ_API_KEY` | `https://api.groq.com/openai/v1` |
| 4 | [ClinePass](https://docs.cline.bot/getting-started/clinepass) | `cline_pass` | `CLINE_API_KEY` | `https://api.cline.bot/api/v1` |
| 5 | [OpenAI / ChatGPT](https://learn.chatgpt.com/docs/auth) | `openai` | Admin UI 連結帳號 | `https://chatgpt.com/backend-api/codex` |
| 6 | [GitHub Copilot](https://docs.github.com/en/copilot) | `github_copilot` | Admin UI 連結帳號 | 由 Copilot SDK 決定 |
| 7 | [xAI（Grok）](https://console.x.ai/) | `xai` | `XAI_API_KEY` | `https://api.x.ai/v1` |
| 8 | [QwenCloud Token Plan](https://home.qwencloud.com/api-keys) | `qwencloud` | `QWENCLOUD_API_KEY` | `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` |
| 9 | [QwenCloud Coding Plan](https://home.qwencloud.com/api-keys) | `qwencloud_coding` | `QWENCLOUD_CODING_API_KEY` | `https://coding-intl.dashscope.aliyuncs.com/v1` |
| 10 | [Together AI](https://api.together.ai/settings/api-keys) | `together` | `TOGETHER_API_KEY` | `https://api.together.ai/v1` |
| 11 | [DeepInfra](https://deepinfra.com/dash/api_keys) | `deepinfra` | `DEEPINFRA_API_KEY` | `https://api.deepinfra.com/v1/openai` |
| 12 | [SiliconFlow](https://cloud.siliconflow.com/account/ak) | `siliconflow` | `SILICONFLOW_API_KEY` | `https://api.siliconflow.com/v1` |
| 13 | [Nebius Token Factory](https://tokenfactory.nebius.com/) | `nebius` | `NEBIUS_API_KEY` | `https://api.tokenfactory.nebius.com/v1` |
| 14 | [Chutes](https://chutes.ai/) | `chutes` | `CHUTES_API_KEY` | `https://llm.chutes.ai/v1` |
| 15 | [Featherless AI](https://featherless.ai/account/api-keys) | `featherless` | `FEATHERLESS_API_KEY` | `https://api.featherless.ai/v1` |
| 16 | [Agnes AI](https://agnes-ai.com/) | `agnes` | `AGNES_API_KEY` | `https://apihub.agnes-ai.com/v1` |
| 17 | [ZenMux](https://zenmux.ai/) | `zenmux` | `ZENMUX_API_KEY` | `https://zenmux.ai/api/v1` |
| 18 | [W&B Inference](https://wandb.ai/settings) | `wandb` | `WANDB_API_KEY` | `https://api.inference.wandb.ai/v1` |
| 19 | [Azure OpenAI](https://learn.microsoft.com/azure/foundry/openai/) | `azure_openai` | `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_BASE_URL` | 依資源而定 |
| 20 | [Google AI Studio](https://aistudio.google.com/apikey) | `gemini` | `GEMINI_API_KEY` | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| 21 | [Google Vertex AI](https://cloud.google.com/vertex-ai) | `vertex` | `VERTEX_PROJECT_ID` + ADC | `https://aiplatform.googleapis.com` |
| 22 | [DeepSeek](https://platform.deepseek.com/api_keys) | `deepseek` | `DEEPSEEK_API_KEY` | `https://api.deepseek.com` |
| 23 | [Mistral La Plateforme](https://console.mistral.ai/) | `mistral` | `MISTRAL_API_KEY` | `https://api.mistral.ai/v1` |
| 24 | [Mistral Codestral](https://console.mistral.ai/) | `mistral_codestral` | `CODESTRAL_API_KEY` | `https://codestral.mistral.ai/v1` |
| 25 | [OpenCode Zen](https://opencode.ai/auth) | `opencode_zen` | `OPENCODE_API_KEY` | `https://opencode.ai/zen/v1` |
| 26 | [OpenCode Go](https://opencode.ai/auth) | `opencode_go` | `OPENCODE_API_KEY` | `https://opencode.ai/zen/go/v1` |
| 27 | [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) | `vercel` | `AI_GATEWAY_API_KEY` | `https://ai-gateway.vercel.sh/v1` |
| 28 | [Amazon Bedrock](https://console.aws.amazon.com/bedrock/) | `bedrock` | `AWS_BEARER_TOKEN_BEDROCK` + `BEDROCK_BASE_URL` | `https://bedrock-mantle.us-east-1.api.aws/v1` |
| 29 | [Hugging Face Inference](https://huggingface.co/settings/tokens) | `huggingface` | `HUGGINGFACE_API_KEY` | `https://router.huggingface.co/v1` |
| 30 | [Cohere](https://dashboard.cohere.com/api-keys) | `cohere` | `COHERE_API_KEY` | `https://api.cohere.ai/compatibility/v1` |
| 31 | [Wafer](https://wafer.ai/) | `wafer` | `WAFER_API_KEY` | `https://pass.wafer.ai/v1` |
| 32 | [Kimi API](https://platform.moonshot.ai/) | `kimi` | `KIMI_API_KEY` | `https://api.moonshot.ai/v1` |
| 33 | [Kimi Code](https://www.kimi.com/code/console) | `kimi_code` | `KIMI_CODE_API_KEY` | `https://api.kimi.com/coding/v1` |
| 34 | [Kilo.ai](https://kilo.ai/) | `kilo` | `KILO_API_KEY` | `https://api.kilo.ai/api/gateway` |
| 35 | [MiniMax](https://platform.minimax.io/) | `minimax` | `MINIMAX_API_KEY` | `https://api.minimax.io/v1` |
| 36 | [Cerebras Inference](https://cloud.cerebras.ai/) | `cerebras` | `CEREBRAS_API_KEY` | `https://api.cerebras.ai/v1` |
| 37 | [SambaNova](https://cloud.sambanova.ai/apis) | `sambanova` | `SAMBANOVA_API_KEY` | `https://api.sambanova.ai/v1` |
| 38 | [Fireworks AI](https://fireworks.ai/account/api-keys) | `fireworks` | `FIREWORKS_API_KEY` | `https://api.fireworks.ai/inference/v1` |
| 39 | [Novita AI](https://novita.ai/settings/key-management) | `novita` | `NOVITA_API_KEY` | `https://api.novita.ai/openai/v1` |
| 40 | [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | `cloudflare` | `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` | `https://api.cloudflare.com/client/v4` |
| 41 | [Z.ai Coding Plan](https://z.ai/manage-apikey/apikey-list) | `zai` | `ZAI_API_KEY` | `https://api.z.ai/api/coding/paas/v4` |
| 42 | [Z.ai API（按量）](https://z.ai/manage-apikey/apikey-list) | `zai_api` | `ZAI_API_KEY` | `https://api.z.ai/api/paas/v4` |
| 43 | [TokenRouter](https://www.tokenrouter.com/) | `tokenrouter` | `TOKENROUTER_API_KEY` | `https://api.tokenrouter.com/v1` |
| 44 | [NaraRoute](https://router.bynara.id/) | `nararoute` | `NARAROUTE_API_KEY` | `https://router.bynara.id/v1` |
| 45 | [Poolside AI](https://platform.poolside.ai/) | `poolside` | `POOLSIDE_API_KEY` | `https://inference.poolside.ai/v1` |
| 46 | [LLM7.io](https://dash.llm7.io/) | `llm7` | `LLM7_API_KEY` | `https://api.llm7.io/v1` |
| 47 | [Ollama Cloud](https://ollama.com/settings/keys) | `ollama_cloud` | `OLLAMA_API_KEY` | `https://ollama.com/v1` |
| 48 | [LM Studio](https://lmstudio.ai/) | `lmstudio` | `LM_STUDIO_BASE_URL` | `http://localhost:1234/v1` |
| 49 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | `llamacpp` | `LLAMACPP_BASE_URL` | `http://localhost:8080/v1` |
| 50 | [Ollama](https://ollama.com/) | `ollama` | `OLLAMA_BASE_URL` | `http://localhost:11434` |

> **注意**：上表之模型 ID 範例與可用模型清單會隨各 Provider 調整而變動。請以 Admin UI 的 `MODEL` 下拉選單（即 `/v1/models` 端點）為準，不要硬記特定模型名稱。

### 5.3 認證模式：API Key 與 Connected Account

FCC 將 Provider 的認證方式分為兩類（`ProviderAuthKind`）：

| 模式 | 說明 | 適用 Provider |
|------|------|--------------|
| `CONFIGURATION` | 於設定中填入 API Key 或 Base URL | 絕大多數 Provider |
| `CONNECTED_ACCOUNT` | 於 Admin UI 進行 OAuth／裝置碼授權 | OpenAI（ChatGPT）、GitHub Copilot |

**Connected Account 設定要點**

- **OpenAI / ChatGPT**：使用 ChatGPT 訂閱而非 API Key。於 Admin UI 的 **Providers → Connected accounts** 連結；無頭系統請使用裝置碼流程。連結完成後需**重啟已在執行的 Agent**。
- **GitHub Copilot**：使用已登入的 GitHub 帳號與訂閱。需先在 PATH 上安裝 [Copilot CLI 1.0.83](https://github.com/github/copilot-cli/releases/tag/v1.0.83)，再於 Admin UI 連結；FCC 會沿用原生設定檔，或顯示 GitHub 裝置碼。亦可先執行 `copilot login --device-code`。可用模型與配額取決於訂閱層級與組織政策。中斷連結只會停止 FCC 使用，不影響原生登入。

> ⚠️ FCC 對 GitHub Copilot 的 SDK 與 CLI 版本採**釘選（pin）**策略，因為直接存取端點屬實驗性質。升級 Copilot CLI 前請先確認 FCC 相容性。

### 5.4 免費額度優先組合

若目標是零成本運作，建議以下組合（實際額度以各 Provider 公告為準，可能隨時變更）：

| 角色 | Provider | 說明 |
|------|----------|------|
| 主力模型 | NVIDIA NIM | 免費額度充足，模型選擇多，FCC 預設 Provider |
| 極速小任務 | Groq | LPU 架構，延遲極低，免費額度佳 |
| 大上下文分析 | Google AI Studio | 免費額度 + 超長上下文視窗 |
| 免費聚合 | OpenRouter（`:free` 模型） | 一組金鑰涵蓋多家免費模型 |
| 離線保底 | Ollama / LM Studio | 完全免費、無額度限制，速度取決於硬體 |

```dotenv
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
MODEL_HAIKU="groq/llama-3.3-70b-versatile"
MODEL_FALLBACKS="open_router/openrouter/free,gemini/models/gemini-3.1-flash-lite,ollama/qwen3-coder"
```

> ⚠️ **合規提醒**：多數 Provider 的免費額度僅供**個人非商業使用**。企業導入前務必確認 ToS 是否允許商業用途，切勿以免費帳號支撐營運工作負載。詳見 [13.6 節](#136-服務條款與授權合規)。

### 5.5 重點 Provider 詳解

#### NVIDIA NIM（`nvidia_nim`）

FCC 的預設 Provider，也是官方 Quick Start 採用者。

```dotenv
NVIDIA_NIM_API_KEY="nvapi-your-key"
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
```

- 免費額度充足，適合完整走通評估流程
- 模型目錄可於 [build.nvidia.com](https://build.nvidia.com/explore/discover) 瀏覽
- 支援視覺模型（FCC 有專屬的 vision smoke 測試涵蓋影像工具結果傳遞）

#### OpenRouter（`open_router`）

```dotenv
OPENROUTER_API_KEY="sk-or-your-key"
MODEL="open_router/openrouter/free"
```

- 單一金鑰即可存取數百種模型，含大量 `:free` 標記的免費模型
- 適合作為 Fallback 鏈的中段，或用於橫向比較模型表現
- 免費模型的速率限制與可用性波動較大，不建議作為唯一主力

#### Groq（`groq`）與 Cerebras（`cerebras`）

兩者皆為超低延遲推理供應商，適合承擔 Haiku 階層的高頻小任務。

```dotenv
GROQ_API_KEY="gsk_your-key"
CEREBRAS_API_KEY="your-cerebras-key"
MODEL_HAIKU="groq/llama-3.3-70b-versatile"
```

- 明顯改善 Agent 的互動體感（檔案摘要、指令分類等背景請求）
- 選型時務必確認所選模型**支援 Tool Use**，否則 Agent 會失去工具能力

#### DeepSeek（`deepseek`）

```dotenv
DEEPSEEK_API_KEY="your-deepseek-key"
MODEL="deepseek/deepseek-chat"
```

- 高性價比的付費 Provider，程式碼生成品質穩定
- FCC 使用其 Chat Completions 端點，該端點會回報快取使用量，有助成本分析

#### Google AI Studio（`gemini`）

```dotenv
GEMINI_API_KEY="AIza-your-key"
MODEL="gemini/models/gemini-3.1-flash-lite"
```

- 透過 Gemini 的 OpenAI 相容層接入（非 Vertex AI）
- 超長上下文視窗，適合大型程式庫分析與逆向工程場景

#### Z.ai（`zai` 與 `zai_api`）

兩個前綴共用同一把 `ZAI_API_KEY`，但**端點決定計費方式**：

| 前綴 | 對應方案 |
|------|---------|
| `zai` | Coding Plan（訂閱制） |
| `zai_api` | 按量計費 API |

```dotenv
ZAI_API_KEY="your-zai-key"
MODEL="zai/glm-5.2"          # 訂閱制
# MODEL="zai_api/glm-4.7-flash"  # 按量計費
```

#### Kimi（`kimi` 與 `kimi_code`）

| 前綴 | 金鑰 | 說明 |
|------|------|------|
| `kimi` | `KIMI_API_KEY` | API 點數制 |
| `kimi_code` | `KIMI_CODE_API_KEY` | Kimi Code 訂閱制 |

> ⚠️ 兩者的金鑰與端點**不可互換**。Kimi Code 方案依其社群規範，僅供**個人互動式 Coding Agent 使用**。

#### QwenCloud（`qwencloud` 與 `qwencloud_coding`）

| 前綴 | 金鑰 | 說明 |
|------|------|------|
| `qwencloud` | `QWENCLOUD_API_KEY` | Token Plan |
| `qwencloud_coding` | `QWENCLOUD_CODING_API_KEY` | Coding Plan |

> ⚠️ 金鑰與端點不可互換。Coding Plan 依其條款僅供**本機、個人、互動式 Coding Agent 使用**。

#### OpenCode（`opencode_zen` 與 `opencode_go`）

共用 `OPENCODE_API_KEY`，但需以明確前綴區分端點：

```dotenv
OPENCODE_API_KEY="your-opencode-key"
MODEL="opencode_zen/gpt-5.3-codex"
# MODEL="opencode_go/minimax-m2.7"
```

#### Cloudflare Workers AI（`cloudflare`）

需同時提供兩項憑證：

```dotenv
CLOUDFLARE_API_TOKEN="your-cf-token"
CLOUDFLARE_ACCOUNT_ID="your-account-id"
MODEL="cloudflare/@cf/moonshotai/kimi-k2.6"
```

### 5.6 訂閱制 Provider 與合規注意事項

| Provider | 前綴 | 授權來源 | 使用限制重點 |
|----------|------|---------|-------------|
| OpenAI / ChatGPT | `openai` | ChatGPT 訂閱 | 依 ChatGPT 使用條款 |
| GitHub Copilot | `github_copilot` | GitHub 帳號與訂閱 | 模型與配額受組織政策限制 |
| ClinePass | `cline_pass` | Cline 訂閱 | 依 Cline 條款 |
| Kimi Code | `kimi_code` | Kimi Code 方案 | 個人互動式使用 |
| QwenCloud Coding | `qwencloud_coding` | 阿里雲 Coding Plan | 本機、個人、互動式使用 |
| Z.ai Coding Plan | `zai` | Z.ai 訂閱 | 依 Z.ai 條款 |
| OpenCode Zen / Go | `opencode_zen` / `opencode_go` | OpenCode 帳號 | 依 OpenCode 條款 |

> ⚠️ **這是企業導入的最大合規風險點**。訂閱制方案通常繫結於**個人帳號的互動式使用**。若將其接入 CI 流水線、批次工具或多人共用的伺服器，極可能違反條款並導致帳號停權。企業應優先採用企業雲 Provider（[5.7 節](#57-企業雲-provider)）或按量計費 API。

### 5.7 企業雲 Provider

企業若已有雲端合約與資料處理協議（DPA），優先使用以下 Provider——資料流向、稽核與計費皆納入既有治理框架。

#### Azure OpenAI（`azure_openai`）

```dotenv
AZURE_OPENAI_API_KEY="your-azure-key"
AZURE_OPENAI_BASE_URL="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
MODEL="azure_openai/<deployment-name>"
```

- `AZURE_OPENAI_BASE_URL` 須為**完整的 v1 端點**（含尾端斜線）
- 模型參照使用**部署名稱（deployment name）**，而非模型名稱
- 所選部署必須支援 Chat Completions
- 若部署未出現在下拉選單中，直接以自訂 model slug 手動輸入

#### Google Vertex AI（`vertex`）

```dotenv
VERTEX_PROJECT_ID="your-gcp-project"
VERTEX_LOCATION="global"
MODEL="vertex/google/gemini-3.5-flash"
```

- 使用 **Application Default Credentials（ADC）**，不使用 API Key
- 本機開發：執行一次 `gcloud auth application-default login`
- 伺服器部署：服務帳號金鑰檔或附掛服務帳號皆可
- `VERTEX_LOCATION` 預設 `global`，可依資料駐留需求改為特定區域

#### Amazon Bedrock（`bedrock`）

```dotenv
AWS_BEARER_TOKEN_BEDROCK="your-bedrock-token"
BEDROCK_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/v1"
MODEL="bedrock/openai.gpt-oss-120b"
```

- `BEDROCK_BASE_URL` 必須與金鑰所屬**區域一致**，因為金鑰與模型可用性皆為區域範圍

> **實務建議**：企業導入 FCC 的最佳配置是「**企業雲 Provider 為主 + 本地模型為輔**」。Azure OpenAI／Vertex AI／Bedrock 提供合約保障與資料駐留控制，本地模型則作為離線保底與機敏資料處理管道；免費 Provider 僅用於個人學習與 PoC。

### 5.8 本地 Provider

本地 Provider 是**唯一能保證程式碼完全不離開機器**的選項，也是機敏環境的核心方案。

#### LM Studio（`lmstudio`）

```dotenv
LM_STUDIO_BASE_URL="http://localhost:1234/v1"
MODEL="lmstudio/<model-id>"
```

啟動 LM Studio 的本機伺服器，載入**支援 Tool Use** 的模型，並使用 LM Studio 介面顯示的 model identifier。

#### llama.cpp（`llamacpp`）

```dotenv
LLAMACPP_BASE_URL="http://localhost:8080/v1"
MODEL="llamacpp/<model-id>"
```

以 `llama-server` 啟動 OpenAI 相容的 Chat Completions API，並確保 `--ctx-size` 足以容納 Agent 的系統提示與工具定義。FCC 接受伺服器根路徑或明確的 `/v1` 後綴。

#### Ollama（`ollama`）與 Ollama Cloud（`ollama_cloud`）

```bash
ollama pull llama3.1
ollama serve
```

```dotenv
OLLAMA_BASE_URL="http://localhost:11434"
MODEL="ollama/llama3.1"

# Ollama Cloud（雲端託管，需金鑰）
OLLAMA_API_KEY="your-ollama-key"
# MODEL="ollama_cloud/qwen3-coder:480b"
```

以 `ollama list` 取得完整 tag（例如 `ollama/llama3.1:8b`）。FCC 接受根路徑或 `/v1` 後綴。

> ⚠️ **本地模型的三大前提**：
>
> 1. **必須支援 Tool Use**，否則 Claude Code 的檔案編輯、指令執行等核心能力完全失效。
> 2. **上下文長度必須足夠**。Coding Agent 的系統提示加上工具定義通常已佔數千 Token，`--ctx-size` 建議至少 32K；不足時上游多半回傳 HTTP 400。
> 3. **硬體決定可用性**。7B 級量化模型在 16 GB 記憶體上可運作但品質有限；建議 24 GB 以上 VRAM 搭配 30B 級模型才有堪用的 Agent 體驗。

### 5.9 Provider 選型決策矩陣

```mermaid
graph TD
    Q1{程式碼可否離開企業網域?}
    Q1 -->|不可| LOCAL[本地 Provider<br/>LM Studio / llama.cpp / Ollama]
    Q1 -->|可| Q2{已有企業雲合約?}
    Q2 -->|有| ENT[Azure OpenAI / Vertex AI / Bedrock]
    Q2 -->|無| Q3{用途為商業營運?}
    Q3 -->|是| PAID[按量計費 API<br/>DeepSeek / Mistral / xAI / Together]
    Q3 -->|否，個人學習或 PoC| Q4{延遲敏感?}
    Q4 -->|是| FAST[Groq / Cerebras]
    Q4 -->|否| FREE[NVIDIA NIM / Google AI Studio<br/>OpenRouter 免費模型]

    LOCAL --> FB[設定 MODEL_FALLBACKS<br/>跨供應商備援]
    ENT --> FB
    PAID --> FB
    FAST --> FB
    FREE --> FB
```

**選型評估構面**

| 構面 | 關鍵問題 |
|------|---------|
| 合規 | ToS 是否允許本組織的使用型態？是否需要 DPA？ |
| 資料駐留 | 資料處理地區是否符合法規（GDPR、個資法）？ |
| 能力 | 是否支援 Tool Use、串流、影像、長上下文？ |
| 成本 | 免費額度上限？超額計費？Fallback 最壞成本？ |
| 穩定性 | 是否曾有大規模中斷？是否需跨供應商備援？ |
| 延遲 | 互動式開發的體感是否可接受？ |
| 可觀測 | 是否提供用量儀表板供成本歸屬？ |

### 5.10 混合 Provider 路由策略

**策略 A：成本最佳化（個人／小型團隊）**

```dotenv
MODEL="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
MODEL_OPUS="deepseek/deepseek-chat"
MODEL_HAIKU="groq/llama-3.3-70b-versatile"
MODEL_FALLBACKS="open_router/openrouter/free,ollama/qwen3-coder"
REASONING_POLICY=medium
REASONING_HAIKU=off
```

**策略 B：企業合規（受管制環境）**

```dotenv
MODEL="azure_openai/gpt-5-enterprise-deployment"
MODEL_OPUS="vertex/google/gemini-3.5-flash"
MODEL_HAIKU="ollama/qwen3-coder"
MODEL_FALLBACKS="bedrock/openai.gpt-oss-120b,lmstudio/qwen3.5-coder"
REASONING_POLICY=client
```

**策略 C：完全離線（機敏專案）**

```dotenv
MODEL="lmstudio/qwen3.5-coder"
MODEL_HAIKU="ollama/qwen3-coder:7b"
MODEL_FALLBACKS="llamacpp/local-model"
ENABLE_WEB_SERVER_TOOLS=false
WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false
```

**策略 D：延遲最佳化（互動密集）**

```dotenv
MODEL="cerebras/gpt-oss-120b"
MODEL_OPUS="nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
MODEL_HAIKU="groq/llama-3.3-70b-versatile"
PROVIDER_MAX_CONCURRENCY=6
```

> **實務建議**：依任務複雜度分派模型是 FCC 最大的成本槓桿。架構設計與複雜重構走強模型（Opus 階層）、日常編碼走平衡模型、背景小任務走本地或極速模型。實務上這可讓雲端配額消耗降低五成以上。

> **常見錯誤**：把所有階層都指向同一個昂貴模型，配額在數小時內耗盡；或把 `MODEL_HAIKU` 指向不支援 Tool Use 的模型，導致 Agent 在背景任務中頻繁失敗卻難以察覺。

---

## 6. Coding Agent 與客戶端整合（Clients）

### 6.1 十大 Coding Agent 總覽

| Agent | 啟動指令 | 協議 | 定位 |
|-------|---------|------|------|
| [Claude Code](https://code.claude.com/docs/en/overview) | `fcc-claude` | Anthropic Messages | Anthropic 官方終端 Agent，功能最完整 |
| [Codex](https://github.com/openai/codex) | `fcc-codex` | OpenAI Responses | OpenAI 官方 Agent，含 App 與 VS Code |
| [Pi](https://github.com/earendil-works/pi) | `fcc-pi` | Anthropic Messages | 輕量 Agent Harness |
| [OpenCode](https://github.com/anomalyco/opencode) | `fcc-opencode` | 多協議 | 開源終端 Agent |
| [Cline](https://github.com/cline/cline) | `fcc-cline` | Anthropic Messages | 廣泛使用的 IDE Agent |
| [Hermes](https://github.com/NousResearch/hermes-agent) | `fcc-hermes` | 多協議 | Nous Research Agent |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | `fcc-dsh` | 多協議 | DeepSeek 官方 Web Harness |
| [Grok Build](https://github.com/xai-org/grok-build) | `fcc-grok` | 多協議 | xAI 官方建置 Agent |
| [Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2/) | `fcc-muse` | 多協議 | Meta Muse Code |
| [Aider](https://aider.chat/) | `fcc-aider` | 多協議 | 成熟的 Git 導向配對編程工具 |

**啟動器做了什麼**

`cli/launchers/` 下的各啟動器會在執行 Agent 前自動完成：

1. 讀取目前的 Port 與認證 Token（來自 `~/.fcc/.env`）
2. 注入該 Agent 所需的環境變數或設定檔
3. 產生／更新該 Agent 專屬的模型目錄（如 `~/.fcc/codex-model-catalog.json`）
4. 於 `~/.fcc/tmp/launchers/` 建立私有暫存設定，避免污染使用者原有設定
5. 啟動 Agent 行程並納入 `process_registry` 管理，確保結束時正確清理

> **實務建議**：一律使用 `fcc-*` 啟動器而非手動設定環境變數。手動設定容易遺漏 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` 或 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 等關鍵旗標，導致模型選單為空或上下文提早壓縮。

### 6.2 Claude Code 整合

```bash
fcc-server     # 先啟動服務（或使用桌面圖示）
fcc-claude     # 於另一終端機啟動 Claude Code
```

進入 Claude Code 後，以 `/model` 指令即可看到 FCC 提供的完整模型清單。此功能依賴 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`（由啟動器自動注入），Claude Code 會查詢 `GET /v1/models` 取得目錄。

**手動設定（不建議，僅供特殊情境）**

```bash
# Bash
ANTHROPIC_BASE_URL="http://localhost:8082" \
ANTHROPIC_AUTH_TOKEN="freecc" \
CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1 \
CLAUDE_CODE_AUTO_COMPACT_WINDOW=190000 \
claude
```

```powershell
# PowerShell
$env:ANTHROPIC_BASE_URL="http://localhost:8082"
$env:ANTHROPIC_AUTH_TOKEN="freecc"
$env:CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
$env:CLAUDE_CODE_AUTO_COMPACT_WINDOW="190000"
claude
```

### 6.3 Codex 整合（CLI / App / VS Code）

#### Codex CLI

```bash
npm install -g @openai/codex
fcc-codex
```

#### Codex App

1. 啟動 FCC。
2. 編輯 Codex 設定檔：
   - Windows：`%USERPROFILE%\.codex\config.toml`
   - macOS：`~/.codex/config.toml`

```toml
# 模型目錄路徑（擇一，並替換 YOUR_USERNAME）
model_catalog_json = "C:/Users/YOUR_USERNAME/.fcc/codex-model-catalog.json"
# model_catalog_json = "/Users/YOUR_USERNAME/.fcc/codex-model-catalog.json"

model_provider = "fcc"
model = "nvidia_nim/nvidia/nemotron-3-super-120b-a12b"

[model_providers.fcc]
name = "Free Claude Code"
base_url = "http://127.0.0.1:8082/v1"
wire_api = "responses"

[model_providers.fcc.auth]
command = "fcc-codex"
args = ["--print-proxy-auth-token"]
```

3. 設定或變更模型後**重啟 Codex App**，再於模型選單中選取 FCC 模型。

> **要點**：`[model_providers.fcc.auth]` 的 `command` 會自動讀取 FCC 當前的 Proxy Token，因此變更 Token 後不需回頭修改此檔。

#### Codex in VS Code

安裝 [Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)，建立或編輯 `~/.codex/config.toml`（Windows 為 `%USERPROFILE%\.codex\config.toml`），內容同上（不含 `model_catalog_json` 亦可）。設定後重啟 VS Code。若使用 WSL 版 Codex，請在 WSL 內編輯該檔案。

### 6.4 其餘 Agent 啟動方式

```bash
fcc-pi          # Pi
fcc-opencode    # OpenCode
fcc-cline       # Cline
fcc-hermes      # Hermes
fcc-dsh         # DeepSeek Harness Web
fcc-grok        # Grok Build
fcc-muse        # Muse Code
fcc-aider       # Aider
```

各 Agent 的本體需另行安裝（安裝腳本會協助）。Muse Code 於原生 Windows 由 FCC 以受管執行檔形式安裝，可用專屬腳本單獨管理（見 [3.10 節](#310-更新與解除安裝)）。

### 6.5 VS Code 整合

安裝 [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)，開啟使用者設定 JSON 並加入：

```json
"claudeCode.disableLoginPrompt": true,
"claudeCode.environmentVariables": [
  { "name": "ANTHROPIC_BASE_URL", "value": "http://localhost:8082" },
  { "name": "ANTHROPIC_AUTH_TOKEN", "value": "freecc" },
  { "name": "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY", "value": "1" },
  { "name": "CLAUDE_CODE_AUTO_COMPACT_WINDOW", "value": "190000" },
  { "name": "DISABLE_AUTOUPDATER", "value": "1" },
  { "name": "DISABLE_FEEDBACK_COMMAND", "value": "1" },
  { "name": "DISABLE_ERROR_REPORTING", "value": "1" }
]
```

Port 與認證 Token 需與 Admin UI 一致，設定後重新載入擴充套件。

### 6.6 JetBrains ACP 整合

編輯已安裝的 Claude ACP 設定：

- Windows：`C:\Users\%USERNAME%\AppData\Roaming\JetBrains\acp-agents\installed.json`
- Linux / macOS：`~/.jetbrains/acp.json`

於 `acp.registry.claude-acp` 設定環境變數：

```json
"env": {
  "ANTHROPIC_BASE_URL": "http://localhost:8082",
  "ANTHROPIC_AUTH_TOKEN": "freecc",
  "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
  "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "190000",
  "DISABLE_AUTOUPDATER": "1",
  "DISABLE_FEEDBACK_COMMAND": "1",
  "DISABLE_ERROR_REPORTING": "1"
}
```

Port 與 Token 需與 Admin UI 一致，修改後重啟 IDE。

### 6.7 瀏覽器 Code Sessions

FCC v6 新增在瀏覽器中直接執行 Codex 工作階段的能力，路徑為 `/admin/code`。

**能力**

- 選擇本機資料夾後於瀏覽器內執行 Codex，支援即時與背景模式
- **同一工作階段內可自由切換 Provider 與模型**，不需重啟
- 工作階段狀態持久化於 `~/.fcc/code/code.db`（SQLite）
- 事件透過 SSE（`/admin/api/code/events`）即時推送

**主要端點**

| 端點 | 方法 | 用途 |
|------|------|------|
| `/admin/api/code/bootstrap` | GET | 初始化前端狀態 |
| `/admin/api/code/folder-picker` | POST | 開啟原生資料夾選取對話框 |
| `/admin/api/code/sessions` | GET / POST | 列出／建立工作階段 |
| `/admin/api/code/sessions/{id}/turns` | POST | 送出一輪對話 |
| `/admin/api/code/sessions/{id}/stop` | POST | 中止目前工作 |
| `/admin/api/code/events` | GET（SSE） | 即時事件串流 |

> ⚠️ **權限邊界**：Code Sessions 會在所選資料夾中執行實際的檔案操作與指令。任何能存取 Admin UI 的人即可觸發這些操作，因此 [13.2 節](#132-proxy-認證強化)的網路隔離要求在啟用此功能時更為關鍵。

### 6.8 Discord / Telegram 遠端協作

於 **Admin UI → Messaging** 設定，完成後點選 Apply。

**Discord 設定步驟**

1. 於 [Discord Developer Portal](https://discord.com/developers/applications) 建立 Bot。
2. 啟用 **Message Content Intent**，並以「讀取、傳送、訊息歷史、**管理訊息**」權限邀請 Bot（`/clear` 需要管理訊息權限才能移除使用者提示）。
3. Messaging Platform 選 **discord**。
4. 填入 Bot Token、允許的頻道清單，以及**絕對路徑**的 Allowed Directory。
5. 套用設定，必要時重啟服務。

**Telegram 設定步驟**

1. 以 [@BotFather](https://t.me/BotFather) 建立 Bot。
2. 由 [@userinfobot](https://t.me/userinfobot) 取得數字型使用者 ID；群組中需授予 Bot 刪除訊息權限。
3. Messaging Platform 選 **telegram**。
4. 填入 Bot Token、允許的使用者 ID，以及絕對路徑的 Allowed Directory。
5. 套用設定，必要時重啟服務。

**訊息指令**

| 用法 | 行為 |
|------|------|
| `/stats` | 顯示目前工作階段狀態 |
| 獨立的 `/stop` | 取消所有工作 |
| 回覆某訊息並輸入 `/stop` | 僅取消該筆請求，其餘排隊請求繼續 |
| 獨立的 `/clear` | 重置全部 FCC 狀態，並刪除該聊天中所有追蹤的訊息（含使用者提示、語音訊息、FCC 回覆、Telegram 上線通知與該 clear 指令本身） |
| 回覆某訊息並輸入 `/clear` | 刪除該訊息及其平台回覆子樹，保留其祖先與兄弟節點 |

> ⚠️ **這是 FCC 中風險最高的功能**。它讓即時通訊平台上的訊息能觸發本機的檔案讀寫與指令執行。務必：
>
> - `ALLOWED_DIR` 設為專用沙箱目錄，不含機敏資料
> - 允許清單（頻道／使用者 ID）嚴格限縮至本人
> - 妥善保管 Bot Token；洩漏等同於將本機 Shell 交予他人
> - 企業環境中，除非有明確授權與監控，否則建議停用（`MESSAGING_PLATFORM=none`）

### 6.9 語音輸入（Voice Notes）

安裝語音支援後（見 [3.3 節](#33-方式一官方安裝腳本推薦)），重啟 `fcc-server`，於 **Admin UI → Messaging → Voice** 啟用語音訊息並選擇後端。

| 後端 | `WHISPER_DEVICE` | 需求 |
|------|-----------------|------|
| 本地 Whisper（CPU） | `cpu` | `voice_local` 額外依賴 |
| 本地 Whisper（GPU） | `cuda` | `voice_local` 依賴 + NVIDIA CUDA |
| NVIDIA NIM 轉錄 | `nvidia_nim` | `voice` 依賴 + `NVIDIA_NIM_API_KEY` |

可選模型：`tiny`、`base`、`small`、`medium`、`large-v2`、`large-v3`、`large-v3-turbo`。本地受管制模型需設定 `HUGGINGFACE_API_KEY`。

> **隱私提醒**：選 `cpu` 或 `cuda` 時音訊完全在本機處理；選 `nvidia_nim` 則音訊會上傳至 NVIDIA。討論機敏內容時請使用本地後端。

### 6.10 客戶端疑難排解

**Claude Code 仍要求登入**

即使已正確設定 Base URL 與 Token，Claude Code 仍可能顯示登入畫面。開啟其狀態檔：

- Windows：`%USERPROFILE%\.claude.json`
- macOS / Linux / WSL：`~/.claude.json`

將以下屬性合併進既有 JSON（**不要刪除其他欄位**）：

```json
"hasCompletedOnboarding": true
```

若檔案不存在則建立完整 JSON 物件：

```json
{
  "hasCompletedOnboarding": true
}
```

儲存後重啟 Claude Code 或 IDE。

**其他常見客戶端問題**

| 症狀 | 可能原因 | 處理 |
|------|---------|------|
| `/model` 選單為空 | 未啟用 Gateway Model Discovery | 使用 `fcc-claude` 啟動，或補上 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` |
| Codex 認證失敗 | `base_url` 缺少 `/v1` | 改為 `http://127.0.0.1:8082/v1` |
| Codex 看不到 FCC 模型 | 模型目錄未更新或未重啟 | 重跑 `fcc-codex`，並重啟 Codex App／VS Code |
| 連結帳號後 Agent 仍失敗 | Agent 於連結前啟動 | 重啟該 Agent |
| VS Code 設定無效 | Port 或 Token 與 Admin 不一致 | 對齊後重新載入擴充套件 |
| 工具呼叫行為異常 | 上游模型不支援 Tool Use | 改選具工具能力的模型 |

---

## 7. 開發實戰（AI Development Use Cases）

### 7.1 Web Application 開發

#### 7.1.1 整體流程

```mermaid
graph TD
    A[需求分析] --> B[API 設計]
    B --> C[DB Schema 設計]
    C --> D[後端開發<br/>Spring Boot / FastAPI]
    D --> E[前端開發<br/>Vue / React]
    E --> F[整合測試]
    F --> G[Code Review]
    G --> H[部署]
```

**模型分派建議**

| 階段 | 建議階層 | 理由 |
|------|---------|------|
| 需求分析、API 設計、Schema 設計 | Opus | 需全域一致性與架構判斷 |
| 後端／前端實作 | Sonnet | 品質與成本的平衡點 |
| 測試撰寫、格式整理 | Haiku | 高頻低複雜度 |
| Code Review | Opus | 需跨檔案推理 |

#### 7.1.2 前後端生成範例

**後端 API 生成 Prompt**

```text
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

**前端生成 Prompt**

```text
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

#### 7.1.3 DB Schema 設計

```text
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

### 7.2 舊系統逆向工程

#### 7.2.1 逆向工程流程

```mermaid
graph TD
    A[取得 Legacy 原始碼] --> B[程式碼結構分析]
    B --> C[自動產出文件<br/>架構圖 / 資料流]
    C --> D[業務邏輯萃取]
    D --> E[測試案例生成]
    E --> F[重構策略建議]
    F --> G[逐步重構實作]
    G --> H[比對驗證]
```

> **Provider 選型提醒**：逆向工程需要大量上下文。建議將此類任務路由至長上下文模型（Google AI Studio 的 Gemini 系列、Kimi），或於本地部署高上下文模型。上下文不足會導致模型只看到片段而產生錯誤結論。

#### 7.2.2 Legacy Java 分析

```text
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

#### 7.2.3 自動產出文件

```text
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

### 7.3 Framework 升級

#### 7.3.1 升級流程

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
```

#### 7.3.2 Spring Boot 升級

```text
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

#### 7.3.3 Java 版本升級

```text
請分析以下 Java 8 專案並建議升級至 Java 21 的步驟：

分析重點：
1. 已棄用 API 替代方案
2. 模組化（JPMS）影響評估
3. 可使用的新語法特性（Records, Sealed Classes, Pattern Matching, Virtual Threads）
4. GC 設定調整建議
5. 第三方套件相容性問題

[貼上專案相關檔案]
```

> **實務建議**：大型升級應分批進行——先升級 Java 版本，確認 CI 通過後再升級 Spring Boot，最後才處理第三方套件。

> **常見錯誤**：一次性升級所有套件，導致大量 breaking change 交互糾纏而難以除錯。每次只跨一個主要版本。

### 7.4 多模型協作模式

FCC 讓「同一任務用不同模型交叉驗證」變得可行且低成本。以下為三種實務可用的協作模式。

**模式一：生成／審查分離**

```mermaid
graph LR
    T[任務] --> G["生成模型<br/>MODEL_SONNET<br/>成本較低"]
    G --> C[產出程式碼]
    C --> R["審查模型<br/>MODEL_OPUS<br/>能力較強"]
    R --> V{通過?}
    V -->|是| DONE([提交 PR])
    V -->|否| G
```

以較便宜的模型生成、較強的模型審查，可在控制成本的同時維持品質底線。

**模式二：跨供應商交叉驗證**

對安全關鍵或架構決策，以兩家不同供應商的模型各自分析，再比對差異。共同指出的問題可信度高；只有一方提出的則需人工判斷。這對緩解單一模型的系統性偏誤特別有效。

**模式三：本地初篩 + 雲端深入**

以本地模型完成初步整理（檔案摘要、關鍵字定位、格式轉換），僅將收斂後的上下文送往雲端強模型。此模式同時降低成本與資料外流面積，適合機敏專案。

> **實務建議**：搭配 [2.7 節](#27-reasoning-推理強度控制)的 Reasoning 控制，可讓同一模型在生成階段用 `low`、審查階段用 `high`，進一步壓縮成本。

---

## 8. SSDLC（安全開發流程）

### 8.1 AI 輔助 SSDLC 整體流程

```mermaid
graph TD
    subgraph REQ["需求階段"]
        A1[需求分析] --> A2[Threat Modeling<br/>AI 輔助威脅建模]
        A2 --> A3[安全需求定義]
    end

    subgraph DES["設計階段"]
        B1[架構設計] --> B2[安全架構審查<br/>AI Code Review]
        B2 --> B3[安全設計規範]
    end

    subgraph DEV["開發階段"]
        C1[程式碼開發] --> C2[AI 即時安全檢查]
        C2 --> C3[Secure Coding Review]
        C3 --> C4[單元安全測試]
    end

    subgraph TST["測試階段"]
        D1[SAST 靜態分析] --> D2[DAST 動態測試]
        D2 --> D3[Dependency Check<br/>CVE 掃描]
        D3 --> D4[滲透測試]
    end

    subgraph OPS["部署階段"]
        E1[安全設定審查] --> E2[部署自動化]
        E2 --> E3[運行時監控]
    end

    A3 --> B1
    B3 --> C1
    C4 --> D1
    D4 --> E1
```

> ⚠️ **前置條件**：將 FCC 用於 SSDLC 前，必須先確認**程式碼可否送往所選 Provider**。安全審查往往涉及最機敏的程式碼路徑（認證、加密、金流）。若無法確認 Provider 的資料處理條款，這類任務應限定使用本地模型或企業雲 Provider。

### 8.2 Threat Modeling（威脅建模）

```text
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

### 8.3 Code Review（AI 安全審查）

```text
請對以下程式碼進行安全審查，檢查 OWASP Top 10 風險：

檢查項目：
1. Injection（SQL / NoSQL / Command）
2. Broken Access Control
3. Cryptographic Failures
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery（SSRF）

每個發現需包含：
- 風險等級（Critical / High / Medium / Low）
- 問題描述與觸發條件
- 具體修復建議（含程式碼範例）
- 修復後的驗證方式

[貼上程式碼]
```

### 8.4 Security Scan 整合

```text
請分析以下 pom.xml / package.json 的相依套件：

1. 列出所有已知 CVE 漏洞
2. 按嚴重等級排序（Critical → High → Medium → Low）
3. 提供升級建議（目標版本）
4. 評估升級的 breaking change 風險
5. 建議修復優先順序

[貼上依賴檔案]
```

> ⚠️ **模型知識截止日的限制**：LLM 對 CVE 的認知受限於訓練資料截止時間，**不可作為漏洞掃描的唯一依據**。務必以 OWASP Dependency-Check、Trivy、Snyk 等即時資料庫工具為主，AI 僅用於解讀結果與評估修復風險。

### 8.5 SSDLC 自動化流程

```mermaid
graph LR
    DEV[開發者提交] --> PR[Pull Request]
    PR --> LINT[Linting + Format]
    LINT --> SAST[SAST 掃描<br/>SonarQube]
    SAST --> DEP[Dependency Check<br/>OWASP DC / Trivy]
    DEP --> AI[AI Code Review<br/>經 FCC 路由]
    AI --> TEST[自動化測試]
    TEST --> APPROVE{全部通過?}
    APPROVE -->|是| MERGE[Merge]
    APPROVE -->|否| FIX[退回修復]
    FIX --> DEV
```

> **實務建議**：將 AI 安全審查納入 PR 的必要檢查之一，但定位為**輔助人工審查的加速器**，而非替代品。

> **常見錯誤**：僅依賴 AI 審查而略過傳統 SAST 工具。兩者互補：SAST 擅長已知模式的高召回，AI 擅長理解業務邏輯漏洞。

---

## 9. 團隊導入策略（Team Adoption）

### 9.1 導入階段規劃

```mermaid
graph LR
    subgraph P1["Phase 1：評估（2 週）"]
        P1A[環境建置與腳本稽核]
        P1B[Provider 合規確認]
        P1C[PoC 端到端驗證]
    end

    subgraph P2["Phase 2：試點（4 週）"]
        P2A[Pilot Team 試用]
        P2B[建立 Prompt 範本庫]
        P2C[制定使用規範與治理]
    end

    subgraph P3["Phase 3：推廣（持續）"]
        P3A[全團隊導入]
        P3B[成本與效益追蹤]
        P3C[Provider 組合持續優化]
    end

    P1A --> P1B --> P1C --> P2A --> P2B --> P2C --> P3A --> P3B --> P3C
```

**各階段驗收準則**

| 階段 | 驗收準則 |
|------|---------|
| Phase 1 | 安裝腳本已稽核；Provider ToS 經法務／資安確認；`/health` 與端到端對話驗證通過 |
| Phase 2 | Pilot 團隊回饋收斂；Prompt 範本納入版控；使用規範公告並簽署 |
| Phase 3 | 成本可歸屬至團隊；Fallback 鏈經實測；季度複審機制上線 |

### 9.2 開發流程設計

```mermaid
graph TD
    A[接收任務 / User Story] --> B[經 FCC 啟動 Coding Agent]
    B --> C{任務類型}
    C -->|新功能| D[套用 Prompt Template<br/>產生程式碼骨架]
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

### 9.3 Prompt Template 管理

建議在專案中建立 `prompts/` 目錄並納入版本控制：

```text
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

> **實務建議**：Prompt 應與程式碼同等對待——納入版控、經 PR 審查、記錄變更理由。同時在每份範本中標註**建議使用的模型階層**，讓成本分派成為範本的一部分。

### 9.4 AI Agent Team 設計

```mermaid
graph TD
    PM[Product Manager<br/>需求定義] --> ARCH[Architecture Agent<br/>架構設計]
    ARCH --> BE[Backend Agent<br/>後端開發]
    ARCH --> FE[Frontend Agent<br/>前端開發]
    BE --> QA[QA Agent<br/>測試生成]
    FE --> QA
    QA --> SEC[Security Agent<br/>安全審查]
    SEC --> DEVOPS[DevOps Agent<br/>部署自動化]

    ARCH -.Opus 階層.-> M1[強模型]
    SEC -.Opus 階層.-> M1
    BE -.Sonnet 階層.-> M2[平衡模型]
    FE -.Sonnet 階層.-> M2
    QA -.Haiku 階層.-> M3[快速／本地模型]
```

### 9.5 治理與濫用防制

| 管控面向 | 具體措施 | 對應設定 |
|---------|---------|---------|
| 資料安全 | 禁止將客戶資料／個資送入雲端 Provider | 機敏專案強制本地 Provider |
| 程式碼品質 | AI 產出必須經人工 Code Review | 流程規範 |
| 成本控管 | 設定每日／每月上限與告警 | Provider 平台預算控管 + 模型分級 |
| 存取控管 | 代理必須啟用認證 | `PROXY_AUTH_ENABLED=true` |
| 速率控管 | 雙層限流 | `PROVIDER_RATE_LIMIT`、`MESSAGING_RATE_LIMIT` |
| 遠端存取 | 限制 Bot 可及範圍或停用 | `ALLOWED_DIR`、`MESSAGING_PLATFORM=none` |
| 日誌治理 | 生產環境關閉原始內容記錄 | `LOG_RAW_*=false` |
| 模型標準化 | 統一團隊的 Provider 與模型組合 | 標準化 `.env` 範本 |
| 合規複審 | 定期確認各 Provider ToS 變更 | 季度複審機制 |

> **實務建議**：導入初期指定 1～2 位「AI Champion」負責推廣、範本維護與問題排除，可顯著縮短學習曲線。

> **常見錯誤**：未建立使用規範就全面推廣，導致產出品質不一、成本失控，且無法回答「哪些程式碼曾送往哪個供應商」這個稽核問題。

---

## 10. 維運與監控（Operations）

### 10.1 日誌架構

FCC 使用 Loguru，日誌寫入 `~/.fcc/logs/server.log`（JSON sink），層級由 `LOG_LEVEL` 控制。

```mermaid
graph LR
    REQ[客戶端請求] --> PROXY[FCC 閘道]
    PROXY --> LOG[Loguru]
    LOG --> CONSOLE[主控台輸出]
    LOG --> FILE["~/.fcc/logs/server.log"]

    L1["LOG_RAW_API_PAYLOADS"] -.選配.-> LOG
    L2["LOG_RAW_SSE_EVENTS"] -.選配.-> LOG
    L3["LOG_API_ERROR_TRACEBACKS"] -.選配.-> LOG
    L4["LOG_RAW_CLI_DIAGNOSTICS"] -.選配.-> LOG
    L5["LOG_RAW_MESSAGING_CONTENT"] -.選配.-> LOG
    L6["DEBUG_PLATFORM_EDITS<br/>DEBUG_SUBAGENT_STACK"] -.選配.-> LOG
```

**分環境日誌策略**

| 環境 | `LOG_LEVEL` | `LOG_RAW_API_PAYLOADS` | `LOG_RAW_SSE_EVENTS` | `LOG_API_ERROR_TRACEBACKS` | `LOG_RAW_CLI_DIAGNOSTICS` | `LOG_RAW_MESSAGING_CONTENT` | `DEBUG_*` |
|------|------------|------------------------|----------------------|----------------------------|---------------------------|-----------------------------|-----------|
| 本機除錯 | `DEBUG` | true | true | true | true | true | true |
| 共用測試 | `INFO` | false | false | true | false | false | false |
| 生產／團隊共用 | `INFO` 或 `WARNING` | false | false | false | false | false | false |

> ⚠️ 預設情況下，API 與 SSE 相關的記錄只輸出中繼資料（筆數、長度、識別碼），不含內容。**開啟任一 `LOG_RAW_*` 即等同把原始碼與 Prompt 明文寫入磁碟**，且該檔案不會自動輪替清理。除錯完畢請立即關閉並刪除日誌。

### 10.2 Token 與成本監控

FCC 會正規化 SSE 回應中的 usage 中繼資料，可由三個層面監控：

**（1）日誌分析**

```bash
# 統計今日各模型的請求數（依實際日誌欄位調整）
grep '"usage"' ~/.fcc/logs/server.log | wc -l

# Windows PowerShell
Select-String -Path "$env:USERPROFILE\.fcc\logs\server.log" -Pattern '"usage"' | Measure-Object
```

**（2）Provider 用量面板**

| Provider | 用量面板 |
|----------|---------|
| NVIDIA NIM | build.nvidia.com 主控台 |
| OpenRouter | openrouter.ai/activity |
| DeepSeek | platform.deepseek.com |
| Groq | console.groq.com |
| Azure OpenAI | Azure Monitor / Cost Management |
| Vertex AI | GCP Billing + Cloud Monitoring |
| Bedrock | AWS Cost Explorer |

**（3）自建監控（進階）**

```python
"""將 usage 中繼資料輸出至集中式監控系統的示意。

實作時應掛在回應串流結束的收斂點，並注意不要記錄 prompt 內容本身。
"""

import json
from datetime import UTC, datetime

from loguru import logger


def track_usage(model_ref: str, provider_id: str, usage, user_id: str) -> None:
    record = {
        "timestamp": datetime.now(UTC).isoformat(),
        "model": model_ref,
        "provider": provider_id,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "user": user_id,
    }
    # 轉送至 Prometheus / Grafana Loki / ELK
    logger.info(f"USAGE {json.dumps(record, ensure_ascii=False)}")
```

> **注意**：企業若需要完整的成本歸屬（哪個團隊、哪個專案用掉多少），單靠 FCC 本機日誌不足。建議在每台開發機的日誌上加裝集中式收集（Fluent Bit／Vector），並以 Provider 面板作為對帳基準。

### 10.3 成本控管策略

| 策略 | 實施方式 | 預期效益 |
|------|---------|---------|
| 模型分級 | Haiku 走本地／極速模型，Opus 僅用於架構級任務 | 雲端配額降低 40–60% |
| 開啟內建最佳化 | 保持五項 `ENABLE_*` 為 `true` | 減少瑣碎請求 |
| 啟用 RTK | 安裝時勾選 RTK | 終端輸出 Token 最多降 90% |
| 降低推理等級 | `REASONING_POLICY=low`，僅特定階層開高 | 推理 Token 顯著下降 |
| 免費額度優先 | 主力走免費 Provider，付費僅作 Fallback | 直接成本趨近零 |
| 本地保底 | Fallback 鏈尾放本地模型 | 避免超額後被迫付費 |
| Provider 端硬上限 | 於各 Provider 平台設定消費上限 | 防止失控支出 |
| 限制 Fallback 深度 | Fallback 清單不宜過長，避免單次失敗連鎖消耗 | 控制最壞成本 |

> ⚠️ **Fallback 的隱藏成本**：一次失敗的請求可能依序觸達鏈上多個 Provider 並各自計費。設計 Fallback 鏈時，請以「最壞情況成本 = 鏈上所有付費 Provider 之和」來評估。

### 10.4 速率限制設計

```dotenv
# 保守（免費 Provider，額度嚴格）
PROVIDER_RATE_LIMIT=1
PROVIDER_RATE_WINDOW=5
PROVIDER_MAX_CONCURRENCY=1

# 平衡（預設值）
PROVIDER_RATE_LIMIT=1
PROVIDER_RATE_WINDOW=2
PROVIDER_MAX_CONCURRENCY=2

# 積極（付費 Provider 或高效能本地 GPU）
PROVIDER_RATE_LIMIT=10
PROVIDER_RATE_WINDOW=1
PROVIDER_MAX_CONCURRENCY=8
```

搭配 Messaging 層的獨立限流：

```dotenv
MESSAGING_RATE_LIMIT=1
MESSAGING_RATE_WINDOW=1
```

### 10.5 健康檢查與可觀測性

```bash
# 1. 服務存活
curl -s http://localhost:8082/health

# 2. 模型目錄筆數（需帶認證）
curl -s -H "Authorization: Bearer $FCC_TOKEN" http://localhost:8082/v1/models | jq '.data | length'

# 3. 端到端對話測試（model 需為實際的 FCC 模型參照）
curl -s -X POST http://localhost:8082/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FCC_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "nvidia_nim/nvidia/nemotron-3-super-120b-a12b",
    "max_tokens": 64,
    "messages": [{"role": "user", "content": "ping"}]
  }'
```

**排程化健康檢查腳本**

```bash
#!/usr/bin/env bash
# fcc-healthcheck.sh — 建議以 cron / 工作排程每 5 分鐘執行
set -euo pipefail

BASE="http://localhost:8082"
TOKEN="${FCC_TOKEN:?FCC_TOKEN 未設定}"

if ! curl -fsS --max-time 5 "${BASE}/health" > /dev/null; then
  echo "[CRITICAL] FCC 服務無回應" >&2
  exit 2
fi

count=$(curl -fsS --max-time 10 -H "Authorization: Bearer ${TOKEN}" \
  "${BASE}/v1/models" | jq '.data | length')

if [ "${count}" -eq 0 ]; then
  echo "[WARNING] 模型目錄為空，請檢查 Provider 設定" >&2
  exit 1
fi

echo "[OK] FCC 正常，可用模型 ${count} 個"
```

**建議監控指標**

| 指標 | 來源 | 告警條件 |
|------|------|---------|
| 服務存活 | `/health` | 連續 2 次失敗 |
| 可用模型數 | `/v1/models` | 為 0 |
| Fallback 觸發率 | 日誌 | 短時間內大幅上升（代表主 Provider 異常） |
| 上游錯誤率 | 日誌 | 5xx 比例超過門檻 |
| Token 用量 | Provider 面板 | 達每日預算 80% |
| 串流逾時次數 | 日誌 | 明顯上升（可能需調整逾時設定） |

> **常見錯誤**：只監控服務是否存活，卻未監控 Fallback 觸發率。主 Provider 靜默失效時，服務看似正常，實際上所有流量已改由備援模型承擔——品質下降卻無人察覺。

---

## 11. 品質驗證：測試與 Smoke Testing

### 11.1 兩層測試策略

FCC 將測試明確分為兩層，這個切分方式本身就值得企業借鏡：

```mermaid
graph TD
    subgraph T1["tests/ — Hermetic 測試"]
        A1[單元測試]
        A2[合約測試<br/>架構邊界規則]
        A3[協議正規化測試]
        A4[設定驗證測試]
    end

    subgraph T2["smoke/ — Live E2E 測試"]
        B1["prereq/ — 前置條件<br/>服務、路由、認證、Provider ping"]
        B2["product/ — 產品情境<br/>真實端到端行為"]
    end

    CI[GitHub Actions CI] --> T1
    LOCAL[本機／部署前驗證] --> T2

    T1 -.必須恆綠.-> GATE{可合併?}
    T2 -.功能覆蓋來源.-> GATE
```

| 層級 | 目錄 | 特性 | 執行時機 |
|------|------|------|---------|
| Hermetic | `tests/` | 不呼叫外部服務、不啟子行程；`uv run pytest` 必須全綠 | 每次提交、CI |
| Live Smoke | `smoke/` | 會啟動子行程、呼叫真實 Provider、觸碰本地模型伺服器、可選擇性收發 Bot 訊息 | 僅本機／部署前 |

> **重要原則**：功能覆蓋率來自 `smoke/product/`，而非路由或標頭層級的 ping。`smoke/prereq/` 僅證明「環境可用」，不構成功能驗證。

### 11.2 Hermetic 測試

```bash
uv run pytest -v --tb=short
```

`tests/` 下的子目錄對應原始碼分層：`api/`、`application/`、`config/`、`core/`、`providers/`、`runtime/`、`messaging/`、`cli/`、`scripts/`，另有 `contracts/` 專門驗證架構邊界（例如「`config/provider_catalog.py` 不得 import Provider 實作」）。

> **值得借鏡的做法**：以自動化測試強制架構邊界，使分層不會隨時間腐化。這比僅靠文件約定或人工 Code Review 可靠得多。

### 11.3 Live Smoke Testing

**收集與空跑**

```powershell
uv run pytest smoke --collect-only -q
uv run pytest smoke -n 0 -s --tb=short
```

第二個指令在未設定 `FCC_LIVE_SMOKE=1` 時會跳過所有測試，但仍會將跳過紀錄寫入 `.smoke-results/`，可用於確認覆蓋範圍。

**實際執行**

```powershell
$env:FCC_LIVE_SMOKE = "1"
uv run pytest smoke -n 0 -s --tb=short
```

**Provider 並行執行**（各 Provider 之間並行，單一 Provider 內部維持循序）

```powershell
$env:FCC_LIVE_SMOKE = "1"
$env:FCC_SMOKE_TARGETS = "providers"
uv run pytest smoke -n auto --dist=loadgroup -s --tb=short
```

### 11.4 Smoke Target 對照表

**預設 Target（不發送真實 Bot 訊息、不載入語音後端）**

| Target | 涵蓋情境 | 環境需求 |
|--------|---------|---------|
| `api` | messages、count_tokens 完整負載、錯誤處理、`/stop`、最佳化 | 僅串流測試需已設定的 Provider |
| `auth` | 標準 Bearer 認證、衝突的舊式標頭、無效／缺失認證 | 無（測試自建隔離 Token） |
| `cli` | 服務進入點、Claude CLI 自適應推理、自動 WebSearch、Auto 模式分類器、工作階段清理 | Claude CLI 與 Provider；Auto 模式需連結 OpenAI 帳號；WebSearch 需 `FCC_SMOKE_RUN_WEB_TOOLS=1` |
| `clients` | VS Code 與 JetBrains 協議負載；Pi、OpenCode、Aider、Cline、Hermes、DSH、Grok Build、Muse Code 的 CLI 提示 | 已設定的 Provider；已安裝的 Agent 二進位檔 |
| `config` | 設定優先權、已移除變數的遷移、Proxy 與逾時 | 無 |
| `extensibility` | Provider runtime 與平台 factory 建構 | 無 |
| `messaging` | 假 Discord／Telegram 完整流程、clear 範圍、訊息樹、持久化、語音取消 | 無 |
| `providers` | 多輪文字、自適應推理歷史、工具、斷線、錯誤 | 已設定的 Provider，可選 `FCC_SMOKE_MODEL_*` |
| `tools` | 強制 `tool_use` 與 `tool_result` 續行 | 具工具能力的 Provider |
| `rate_limit` | 斷線清理與後續請求 | 已設定的 Provider |
| `lmstudio` / `llamacpp` / `ollama` | 本地 `/models` 與經代理的 Messages 請求 | 對應的本地伺服器已啟動 |

**選擇性啟用的重度／有副作用 Target**

| Target | 涵蓋情境 | 環境需求 |
|--------|---------|---------|
| `nvidia_nim_cli` | Claude Code CLI 功能矩陣跨多個 NIM 模型 | `NVIDIA_NIM_API_KEY`、Claude CLI |
| `nvidia_nim_vision` | Claude 風格影像工具結果以像素形式抵達視覺模型 | `NVIDIA_NIM_API_KEY`、`FCC_SMOKE_MODEL_NVIDIA_NIM_VISION` |
| `openrouter_free_cli` | Claude Code CLI 功能矩陣跨 OpenRouter 免費模型 | `OPENROUTER_API_KEY`、Claude CLI |
| `telegram` | getMe、傳送、編輯、刪除，可選人工入站測試 | Token 與 chat／user ID |
| `discord` | 頻道存取、傳送、編輯、刪除，可選人工入站測試 | Token 與頻道 ID |
| `voice` | 產生 WAV 經本地 Whisper 或 NVIDIA NIM 轉錄 | `VOICE_NOTE_ENABLED=true`、`FCC_SMOKE_RUN_VOICE=1` |

> ⚠️ `telegram` 與 `discord` target 會**送出並刪除真實訊息**；`voice` 會載入語音後端並可能消耗轉錄配額。務必在專用測試頻道執行。

### 11.5 Smoke 模型覆寫

Provider 的產品層 E2E 測試會**針對每個已設定的 Provider 各執行一次**，與 `MODEL`、`MODEL_FABLE`、`MODEL_OPUS`、`MODEL_SONNET`、`MODEL_HAIKU` 的設定無關。預設模型來自 Provider 目錄與文件，可用 `FCC_SMOKE_MODEL_<PROVIDER>` 覆寫：

```powershell
$env:FCC_SMOKE_MODEL_DEEPSEEK = "deepseek-v4-pro"
$env:FCC_SMOKE_MODEL_NVIDIA_NIM = "nvidia/nemotron-3-super-120b-a12b"
$env:FCC_SMOKE_MODEL_OPEN_ROUTER = "openrouter/free"
```

若未設定任何 Provider smoke 模型，Live 產品 smoke 會以 `missing_env` 失敗，除非明確設定 `FCC_ALLOW_NO_PROVIDER_SMOKE=1`。

> **實務建議**：以免費模型作為 smoke 模型，避免例行驗證消耗付費配額。

### 11.6 實務執行範例

**跨多 Provider 矩陣驗證**

```powershell
$env:FCC_LIVE_SMOKE = "1"
$env:FCC_SMOKE_PROVIDER_MATRIX = "open_router,nvidia_nim,deepseek,lmstudio,llamacpp,ollama"
uv run pytest smoke/product -n 0 -s --tb=short
```

**驗證本地 Ollama 整合**

```powershell
$env:FCC_LIVE_SMOKE = "1"
$env:FCC_SMOKE_TARGETS = "ollama"
$env:OLLAMA_BASE_URL = "http://localhost:11434"
uv run pytest smoke/prereq smoke/product -n 0 -s --tb=short
```

**驗證 Bot 與語音整合**

```powershell
$env:FCC_LIVE_SMOKE = "1"
$env:FCC_SMOKE_TARGETS = "telegram,discord,voice"
$env:FCC_SMOKE_RUN_VOICE = "1"
uv run pytest smoke/product -n 0 -s --tb=short
```

**企業導入建議的驗證順序**

```mermaid
graph TD
    S1["1. uv run pytest（Hermetic 全綠）"] --> S2["2. smoke prereq：服務、認證、Provider 可達"]
    S2 --> S3["3. smoke providers：目標 Provider 端到端"]
    S3 --> S4["4. smoke tools：Tool Use 行為正確"]
    S4 --> S5["5. smoke clients：實際使用的 Agent"]
    S5 --> S6{全數通過?}
    S6 -->|是| GO([核准導入])
    S6 -->|否| FIX[修正設定或更換 Provider]
    FIX --> S2
```

> **常見錯誤**：僅執行 `prereq` 就宣告驗證完成。`prereq` 只證明端點可達與金鑰有效，無法證明 Tool Use、串流與多輪對話在該 Provider 上真正可用——而這三項才是 Coding Agent 能否運作的關鍵。

---

## 12. 升級、擴展與高可用（Upgrade & Scaling）

### 12.1 升級策略

**腳本安裝者**：重新執行安裝指令即可，設定與憑證保留。

```bash
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh
```

**原始碼安裝者**

```bash
cd free-claude-code
cp ~/.fcc/.env ~/.fcc/.env.backup.$(date +%Y%m%d)
git pull origin main
uv sync
uv run fcc-server
```

**升級檢查清單**

1. 備份 `~/.fcc/.env` 與 `~/.fcc/auth/`
2. 檢視上游 commit log 與版本號變更（runtime 變更必伴隨 `pyproject.toml` 版號提升）
3. 比對 `.env.example` 是否有新增或移除的變數
4. 更新程式碼與依賴
5. 重新啟動服務並檢視啟動日誌是否有設定驗證警告
6. 執行 `/health` 與 `/v1/models` 驗證
7. 執行目標 Provider 的 smoke 測試
8. 以實際 Agent 進行一次端到端對話確認

> **版本語意提示**：上游規範要求「runtime 程式碼、封裝、依賴或安裝／CI 腳本的變更，必須在同一 commit 中提升 `pyproject.toml` 版號並更新 `uv lock`」。因此**版號有變動即代表行為可能改變**，純文件變更則不升版。這讓「是否需要重新驗證」的判斷有明確依據。

### 12.2 新增自訂 Provider

多數情況只需三步，不需撰寫新的 transport：

```python
# 1. 於 config/provider_catalog.py 新增預設端點常數
MYCORP_DEFAULT_BASE = "https://llm-gateway.mycorp.internal/v1"

# 2. 於 PROVIDER_CATALOG 註冊描述子
"mycorp": ProviderDescriptor(
    provider_id="mycorp",
    display_name="MyCorp Internal Gateway",
    credential_env="MYCORP_API_KEY",
    credential_attr="mycorp_api_key",
    default_base_url=MYCORP_DEFAULT_BASE,
    proxy_attr="mycorp_proxy",
),

# 3. 於 config/settings.py 加入對應欄位
mycorp_api_key: OptionalNonEmptyString = Field(
    default=None, validation_alias="MYCORP_API_KEY"
)
```

若上游行為與標準 OpenAI Chat Completions 有差異（特殊標頭、非標準串流、認證流程），才需要在 `providers/mycorp/` 實作專屬 transport，並於 `providers/runtime/factory.py` 加入建構 wiring。

> **實務建議**：企業自建的 vLLM、TGI 或內部 LLM Gateway 多半已提供 OpenAI 相容端點，因此上述三步即可完成接入。接入後別忘了在 `tests/` 補上合約測試，並於 `smoke/` 新增對應 target。

### 12.3 水平擴展

> ⚠️ **前提說明**：FCC 的設計定位是**單使用者的本機閘道**——設定、憑證與 Agent 行程管理皆繫結於單一使用者的 `~/.fcc/`。以下架構適用於「多台開發機各自執行 FCC，前方以反向代理統一入口」或「單機多實例分散 Provider 額度」的情境，**不適合作為多租戶共享服務**（每個使用者的憑證與工作階段無法隔離）。

```mermaid
graph TD
    subgraph CLIENTS["客戶端"]
        C1[開發者 A]
        C2[開發者 B]
        C3[開發者 N]
    end

    LB[反向代理<br/>Nginx / HAProxy]

    subgraph INSTANCES["FCC 實例"]
        P1["實例 #1 :8082<br/>Provider 組合 A"]
        P2["實例 #2 :8083<br/>Provider 組合 B"]
        P3["實例 #N :808N<br/>Provider 組合 N"]
    end

    PROV[上游 Provider]

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

**Nginx 設定範例**

```nginx
upstream fcc_gateway {
    least_conn;
    server 127.0.0.1:8082;
    server 127.0.0.1:8083;
    server 127.0.0.1:8084;
}

server {
    listen 443 ssl;
    server_name fcc.internal.example.com;

    ssl_certificate     /etc/ssl/certs/fcc.crt;
    ssl_certificate_key /etc/ssl/private/fcc.key;

    # Admin UI 僅限管理網段
    location /admin {
        allow 10.0.100.0/24;
        deny all;
        proxy_pass http://fcc_gateway;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
    }

    location / {
        proxy_pass http://fcc_gateway;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_set_header Host $host;
        proxy_buffering off;         # SSE 必須關閉緩衝
        proxy_read_timeout 600s;     # 配合長時間串流
        proxy_send_timeout 600s;
    }
}
```

> ⚠️ **必要設定**：`proxy_buffering off` 與足夠長的 `proxy_read_timeout` 是 SSE 串流能正常運作的前提。若省略，使用者會看到回應延遲數十秒後才一次湧出，或在長回應中途斷線。

### 12.4 高可用設計

```mermaid
graph TD
    DNS[DNS / 健康檢查<br/>fcc.example.com]

    subgraph SITE_A["站點 A"]
        LBA[反向代理 A]
        PA1[FCC #1]
        PA2[FCC #2]
        LBA --> PA1
        LBA --> PA2
    end

    subgraph SITE_B["站點 B"]
        LBB[反向代理 B]
        PB1[FCC #3]
        PB2[FCC #4]
        LBB --> PB1
        LBB --> PB2
    end

    DNS --> LBA
    DNS --> LBB

    subgraph FB["應用層備援：MODEL_FALLBACKS"]
        M1[主要 Provider] -.重試耗盡.-> M2[Fallback #1]
        M2 -.失敗.-> M3[Fallback #2]
        M3 -.失敗.-> M4[本地模型保底]
    end

    PA1 --> FB
    PB1 --> FB
```

FCC 的高可用有**兩個獨立層次**，兩者應同時設計：

| 層次 | 機制 | 防範的故障 |
|------|------|-----------|
| 基礎設施層 | 多實例 + 反向代理 + 健康檢查 | FCC 行程或主機故障 |
| 應用層 | `MODEL_FALLBACKS` 跨供應商鏈 | 上游 Provider 中斷或限流 |

> **實務建議**：應用層備援的效益通常高於基礎設施層。FCC 行程本身極少故障，真正的中斷來源幾乎都是上游 Provider。因此優先把 `MODEL_FALLBACKS` 設計好，且**務必跨不同供應商**。

**行程常駐管理**

| 平台 | 建議方式 |
|------|---------|
| Linux | systemd service（`Restart=always`） |
| macOS | launchd，或使用桌面應用程式常駐選單列 |
| Windows | 工作排程器開機執行，或使用桌面應用程式常駐系統匣 |

**systemd 範例**

```ini
[Unit]
Description=Free Claude Code Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=fccuser
Environment="FCC_OPEN_BROWSER=false"
ExecStart=/home/fccuser/.local/bin/fcc-server
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 12.5 Dev / Stage / Prod 環境設計

| 構面 | Dev | Stage | Prod／團隊共用 |
|------|-----|-------|---------------|
| Provider | 本地（Ollama / LM Studio） | 免費雲端（NIM / OpenRouter） | 企業雲或付費 API |
| Reasoning | `client` | `medium` | 依成本政策 |
| 速率限制 | 寬鬆 | 中等 | 嚴格 |
| 認證 | 可關閉 | 啟用 | **必須啟用** |
| Host 綁定 | `127.0.0.1` | `127.0.0.1` | `127.0.0.1` + 反向代理 |
| 日誌 | 全開 | 僅錯誤 | 最小化 |
| Web Tools | 可開 | 可開 | 依政策 |
| Messaging Bot | 可用 | 停用 | **停用** |

**環境切換**

```bash
# 以符號連結切換設定檔（避免手動覆蓋出錯）
ln -sf ~/.fcc/profiles/dev.env   ~/.fcc/.env && fcc-server
ln -sf ~/.fcc/profiles/stage.env ~/.fcc/.env && fcc-server
ln -sf ~/.fcc/profiles/prod.env  ~/.fcc/.env && fcc-server
```

> ⚠️ **注意**：Admin UI 會**直接寫回 `~/.fcc/.env`**。若該路徑為符號連結，Admin 的儲存動作可能覆寫掉來源設定檔。採用多環境設定檔時，建議以自動化方式管理設定並避免同時使用 Admin UI 編輯。

> **常見錯誤**：在前景執行 `fcc-server`，終端機關閉後服務即中斷。請改用 systemd／launchd／工作排程器，或使用桌面應用程式的常駐模式。

---

## 13. 安全、隱私與合規（Security & Compliance）

### 13.1 威脅模型

```mermaid
graph TD
    subgraph ASSETS["受保護資產"]
        A1[Provider API 金鑰<br/>~/.fcc/.env]
        A2[訂閱憑證<br/>~/.fcc/auth/]
        A3[原始碼與商業機密]
        A4[本機檔案系統與 Shell]
    end

    subgraph THREATS["威脅來源"]
        T1[本機代理未認證<br/>同網段任意存取]
        T2[Admin UI 暴露<br/>可改路由與金鑰]
        T3[Messaging Bot Token 外洩<br/>等同遠端 Shell]
        T4[Web Tools SSRF<br/>存取內網與雲端 metadata]
        T5[日誌明文外洩<br/>LOG_RAW_*]
        T6[Prompt Injection<br/>惡意檔案內容操縱 Agent]
        T7[供應鏈<br/>安裝腳本與依賴]
        T8[資料外流<br/>程式碼送至第三方]
    end

    T1 --> A3
    T1 --> A4
    T2 --> A1
    T2 --> A2
    T3 --> A4
    T4 --> A3
    T5 --> A3
    T6 --> A4
    T7 --> A1
    T8 --> A3
```

| 風險 | 嚴重度 | 主要緩解 |
|------|-------|---------|
| 代理未認證且綁定 `0.0.0.0` | 高 | `PROXY_AUTH_ENABLED=true` + `HOST=127.0.0.1` |
| Admin UI 網路暴露 | 高 | 絕不對外開放；遠端管理走 SSH Tunnel |
| Bot Token 外洩 | 高 | 嚴格允許清單、沙箱 `ALLOWED_DIR`、非必要則停用 |
| Web Tools SSRF | 中高 | `WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false` |
| 日誌明文外洩 | 中高 | 生產環境 `LOG_RAW_*=false` |
| Prompt Injection | 中高 | 人工審查 Agent 的破壞性操作、限制工作目錄 |
| 供應鏈 | 中 | 稽核安裝腳本、鎖定依賴、內部鏡像 |
| 資料外流 | 依情境 | Provider 選型與 DPA；機敏專案用本地模型 |

### 13.2 Proxy 認證強化

**最低安全基線**

```dotenv
HOST="127.0.0.1"                     # 僅監聽本機迴環
PROXY_AUTH_ENABLED=true              # 強制 Bearer Token
ANTHROPIC_AUTH_TOKEN="<高強度隨機字串>"
FCC_OPEN_BROWSER=false               # 伺服器環境
```

**產生高強度 Token**

```bash
# macOS / Linux
openssl rand -base64 48
```

```powershell
# Windows PowerShell
[Convert]::ToBase64String((1..48 | ForEach-Object { Get-Random -Max 256 }))
```

> ⚠️ **預設 Token 是 `freecc`**，且 `PROXY_AUTH_ENABLED` 預設為 `false`、`HOST` 預設為 `0.0.0.0`。這組預設值適合單機快速上手，但在任何共用網段上都等同於**對外開放一個可代表你呼叫所有已設定 Provider 的端點**。導入的第一件事就應該是改掉這三項。

**遠端管理：SSH Tunnel**

```bash
# 在本機執行，將遠端主機的 8082 映射至本機
ssh -N -L 8082:127.0.0.1:8082 user@remote-host
# 接著於本機瀏覽器開啟 http://127.0.0.1:8082/admin
```

**若必須經反向代理對外**

- 強制 TLS
- Admin 路徑（`/admin`、`/admin/api/*`）限制來源網段或加上額外認證層
- 保留 FCC 自身的 Bearer 認證，不要以「反向代理已認證」為由關閉
- 依 [12.3 節](#123-水平擴展)設定 SSE 相關參數

### 13.3 憑證與金鑰管理

| 措施 | 說明 |
|------|------|
| 檔案權限 | `chmod 600 ~/.fcc/.env`，`chmod 700 ~/.fcc/auth` |
| 排除備份同步 | `~/.fcc/` 不納入雲端硬碟、備份工具與版本控制 |
| 最小權限金鑰 | 各 Provider 建立專用金鑰，僅授予必要範圍 |
| 定期輪換 | 建立輪換週期（建議每季）與離職／異動時的即時撤銷流程 |
| 消費上限 | 於各 Provider 平台設定硬性支出上限，限制金鑰外洩的損失 |
| 不入版控 | 專案中的 `.env` 一律列入 `.gitignore` |
| 集中管理 | 企業可改以環境變數由 Vault／Secrets Manager 注入，不落地成檔案 |

### 13.4 資料外流與駐留風險

使用 FCC 時，**送往上游的內容包含**：使用者提示、Agent 讀取的檔案內容、工具呼叫參數與結果、終端輸出片段。這些通常就是專案中最敏感的部分。

```mermaid
graph LR
    CODE[專案原始碼] --> AGENT[Coding Agent]
    AGENT --> FCC[FCC 閘道]
    FCC --> D1{Provider 類型}
    D1 -->|本地| LOCAL[留在本機<br/>零外流]
    D1 -->|企業雲| ENT[受 DPA 與區域設定約束]
    D1 -->|第三方 API| TP[依該 Provider 條款<br/>可能用於模型訓練]
```

**評估檢核**

| 問題 | 為何重要 |
|------|---------|
| 該 Provider 是否會將輸入用於模型訓練？ | 直接影響營業秘密風險 |
| 資料處理與儲存位於哪個法域？ | GDPR、個資法、產業法規 |
| 是否提供資料處理協議（DPA）？ | 企業合規的基本要求 |
| 資料保留期限為何？ | 影響事故回溯與刪除權 |
| 免費層與付費層的條款是否不同？ | 免費層常保留更廣的使用權利 |

> **實務建議**：建立**專案分級制度**。將專案分為「可用雲端」「僅限企業雲」「僅限本地」三級，並在各專案的 `.env` 或說明文件中明示等級。這是最容易落地、也最有效的資料治理措施。

### 13.5 Prompt Injection 與供應鏈風險

**Prompt Injection**

Coding Agent 會讀取專案中的檔案內容並納入上下文。若依賴套件的 README、程式碼註解或設定檔中含有惡意指令，可能在 Agent 執行過程中改變其行為（例如誘導其執行指令或外傳資料）。此為所有 Coding Agent 的共通風險，並非 FCC 特有，但 FCC 增加了一層考量：**惡意輸出可能來自能力較弱、對齊較差的免費模型**。

緩解措施：

- 對 Agent 提出的破壞性操作（刪除、覆寫、對外連線、憑證存取）保持人工審查
- 不在未經審視的第三方程式碼庫中以自動核准模式執行 Agent
- 限制 Agent 的工作目錄範圍
- 非必要時關閉 Web Tools（`ENABLE_WEB_SERVER_TOOLS=false`）

**代理設定竄改**

需特別注意：Coding Agent 的 API 端點設定若可被專案層級設定覆寫，惡意專案便可能將流量（連同認證標頭）導向攻擊者控制的伺服器。此類手法已在 Claude Code 生態中出現對應的 CVE。實務上應：

- 檢視專案層級的 Agent 設定檔（如 `.claude/`、`.codex/`）是否被竄改
- 保持 Agent 本體為最新版本
- 對來源不明的專案，先審視其設定檔再啟動 Agent

**供應鏈**

| 風險點 | 緩解 |
|-------|------|
| `curl \| sh` 安裝腳本 | 先下載稽核，內部簽章後散布 |
| Python 依賴 | 以 `uv.lock` 鎖版；企業使用內部 PyPI 鏡像 |
| Agent 二進位檔 | 由官方來源安裝並驗證版本 |
| GitHub Copilot SDK 釘選 | 遵循 FCC 的釘選版本，不擅自升級 |

### 13.6 服務條款與授權合規

這是企業導入 FCC **最容易被忽略、後果卻最嚴重**的面向。

| 檢核項目 | 說明 |
|---------|------|
| 商業使用授權 | 多數免費層僅供個人非商業使用 |
| 帳號共用禁令 | 訂閱制方案幾乎皆禁止多人共用單一帳號 |
| 互動式使用限制 | Kimi Code、QwenCloud Coding 等明訂僅供本機、個人、互動式 Coding Agent 使用，接入 CI 即違規 |
| 自動化呼叫 | 部分方案禁止程式化批次呼叫 |
| 產出物權利 | 確認模型產出的著作權與商業使用條款 |
| 資料使用權 | 確認 Provider 是否可將輸入用於訓練 |
| 條款變更 | Provider 可能隨時調整；需建立定期複審機制 |

> ⚠️ **企業合規建議**：
>
> 1. 免費與訂閱制 Provider **僅用於個人學習與 PoC**，不支撐營運工作負載。
> 2. 正式使用一律採**按量計費 API** 或**企業雲 Provider**，並簽署 DPA。
> 3. 將「Provider 清單與其授權依據」納入資產清冊，指定負責人季度複審。
> 4. 導入前取得法務與資安的正式核可，並保留核可紀錄。

FCC 專案本身採 MIT 授權，可自由使用與修改；但**FCC 的授權不延伸至任何上游 Provider 的服務條款**——這兩者必須分開評估。

### 13.7 安全基線設定檔

以下為企業環境的建議起始基線，可直接作為 `~/.fcc/.env` 的安全區段：

```dotenv
# ===== 網路與認證 =====
HOST="127.0.0.1"
PORT=8082
PROXY_AUTH_ENABLED=true
ANTHROPIC_AUTH_TOKEN="<以 openssl rand -base64 48 產生>"
FCC_OPEN_BROWSER=false

# ===== 日誌（不記錄任何原始內容）=====
LOG_LEVEL=INFO
LOG_RAW_API_PAYLOADS=false
LOG_RAW_SSE_EVENTS=false
LOG_API_ERROR_TRACEBACKS=false
LOG_RAW_MESSAGING_CONTENT=false
LOG_RAW_CLI_DIAGNOSTICS=false
LOG_MESSAGING_ERROR_DETAILS=false
DEBUG_PLATFORM_EDITS=false
DEBUG_SUBAGENT_STACK=false

# ===== Web Tools（封鎖私有網段）=====
ENABLE_WEB_SERVER_TOOLS=true
WEB_FETCH_ALLOWED_SCHEMES=http,https
WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false

# ===== 遠端存取（預設停用）=====
MESSAGING_PLATFORM="none"
ALLOWED_DIR=""

# ===== 模型（企業雲為主，本地保底）=====
MODEL="azure_openai/<deployment-name>"
MODEL_HAIKU="ollama/qwen3-coder"
MODEL_FALLBACKS="vertex/google/gemini-3.5-flash,lmstudio/qwen3.5-coder"
REASONING_POLICY=client
```

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
        with:
          fetch-depth: 0

      - name: Setup Python 3.14
        uses: actions/setup-python@v5
        with:
          python-version: '3.14'

      - name: Install uv
        uses: astral-sh/setup-uv@v8

      - name: Install and start FCC
        env:
          NVIDIA_NIM_API_KEY: ${{ secrets.NVIDIA_NIM_API_KEY }}
          FCC_AUTH_TOKEN: ${{ secrets.FCC_AUTH_TOKEN }}
        run: |
          git clone --depth 1 https://github.com/Alishahryar1/free-claude-code.git /tmp/fcc
          mkdir -p "$HOME/.fcc"
          {
            echo "NVIDIA_NIM_API_KEY=${NVIDIA_NIM_API_KEY}"
            echo "MODEL=nvidia_nim/nvidia/nemotron-3-super-120b-a12b"
            echo "PROXY_AUTH_ENABLED=true"
            echo "ANTHROPIC_AUTH_TOKEN=${FCC_AUTH_TOKEN}"
            echo "HOST=127.0.0.1"
            echo "FCC_OPEN_BROWSER=false"
            echo "MESSAGING_PLATFORM=none"
          } > "$HOME/.fcc/.env"
          cd /tmp/fcc
          uv python install 3.14.0
          nohup uv run fcc-server > /tmp/fcc-server.log 2>&1 &
          # 等待服務就緒，而非固定 sleep
          for i in $(seq 1 30); do
            curl -fsS http://127.0.0.1:8082/health && break
            sleep 2
          done

      - name: Run AI Code Review
        env:
          ANTHROPIC_BASE_URL: http://127.0.0.1:8082
          ANTHROPIC_AUTH_TOKEN: ${{ secrets.FCC_AUTH_TOKEN }}
          CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY: '1'
        run: |
          git diff origin/${{ github.base_ref }}...HEAD > /tmp/pr.diff
          npx @anthropic-ai/claude-code --print \
            "請審查以下 PR diff，找出正確性問題與安全風險，以繁體中文條列說明：$(cat /tmp/pr.diff)" \
            > /tmp/review.md

      - name: Upload review
        uses: actions/upload-artifact@v4
        with:
          name: ai-review
          path: /tmp/review.md
```

> ⚠️ **CI 使用的合規前提**：CI 屬於**自動化、非互動式**使用。**絕不可**在 CI 中使用 Kimi Code、QwenCloud Coding、ClinePass、ChatGPT／Copilot 連結帳號等訂閱制 Provider——這幾乎必然違反其服務條款。CI 情境應使用**明確允許程式化呼叫的按量計費 API** 或企業雲 Provider。

### 14.2 CI/CD 整合架構

```mermaid
graph LR
    DEV[開發者 Push] --> GH[GitHub]
    GH --> GA[GitHub Actions Runner]
    GA --> FCC[FCC 閘道<br/>127.0.0.1:8082]
    FCC --> LLM[允許程式化呼叫的<br/>Provider]
    LLM --> FCC
    FCC --> GA
    GA --> OUT[PR 留言 / Artifact<br/>AI 審查結果]
```

### 14.3 自建 Runner 注意事項

| 事項 | 建議 |
|------|------|
| 金鑰注入 | 一律透過 Secrets，不落地成長存檔案 |
| 認證 | `PROXY_AUTH_ENABLED=true`，Token 由 Secrets 提供 |
| 網路綁定 | `HOST=127.0.0.1`，避免 Runner 網段內其他工作存取 |
| 服務就緒 | 以輪詢 `/health` 取代固定 `sleep` |
| 快取 | 快取 uv 依賴以縮短啟動時間 |
| 清理 | 工作結束後刪除 `~/.fcc/.env` 與日誌 |
| 成本 | 為 CI 使用的金鑰設定獨立的消費上限 |
| 並行 | 多個並行工作會共用 Provider 額度，需調整 `PROVIDER_RATE_LIMIT` |

> **實務建議**：CI 中的 AI 審查應定位為「提供額外視角的建議」，不作為阻擋合併的硬性門檻。免費或中小型模型的誤報率不低，設為硬性門檻會顯著拖慢開發節奏。

---

## 15. 開發與貢獻指南（Development & Contributing）

### 15.1 開發環境設定

```bash
# 安裝 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 取得原始碼
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code

# 安裝指定的 Python 版本
uv python install 3.14.0

# 直接由 checkout 執行
uv run fcc-server
```

> **硬性規範**：一律使用 `uv run` 執行 Python 指令，**不可**以全域 Python 直譯器執行本專案。

### 15.2 本地 CI 流程

開 PR 前必須執行完整的本地 CI 序列：

```bash
./scripts/ci.sh          # macOS / Linux
```

```powershell
.\scripts\ci.ps1         # Windows PowerShell
```

疊代時可用的旗標：

| 平台 | 旗標 |
|------|------|
| macOS / Linux | `--only`、`--skip`、`--dry-run` |
| PowerShell | `-Only`、`-Skip`、`-DryRun` |

**個別修復與測試指令**

```bash
uv run ruff format              # 格式化
uv run ruff check --fix         # Lint 並自動修復
uv run ty check                 # 型別檢查
uv run pytest -v --tb=short     # 測試
```

> **CI 的額外強制規則**：GitHub CI 以 check-only 模式執行 Ruff，並**禁止 `# type: ignore`、`# ty: ignore` 及舊式註解變通寫法**。遇到型別或匯入邊界問題時，必須修正根因而非抑制警告。

### 15.3 程式碼規範

| 項目 | 規範 |
|------|------|
| Python 版本 | 3.14，`target-version = "py314"` |
| 格式化 / Lint | Ruff（line-length 88、double quote） |
| 啟用規則集 | `E`、`W`、`F`、`I`、`UP`、`B`、`C4`、`SIM`、`PERF`、`RUF` |
| 型別檢查 | Ty（不得使用忽略註解） |
| 測試 | Pytest（含 `pytest-asyncio`、`pytest-cov`、`pytest-xdist`、`pytest-playwright`） |
| 日誌 | Loguru |
| 延遲註解 | 使用 3.14 原生 lazy annotations；**禁止** `from __future__ import annotations` |
| 多例外語法 | 可使用 `except TypeError, ValueError:`（3.14 特性） |
| 建置後端 | Hatchling，套件位於 `src/free_claude_code` |

### 15.4 架構原則

| 原則 | 說明 |
|------|------|
| 協議邏輯集中 | 共用的 Anthropic 協議行為放在 `core/anthropic/`，不得從其他 Provider 匯入工具函式 |
| Provider 自治 | Provider 專屬設定留在擁有它的 Provider 內，不上浮至共用設定 |
| 目錄與實作分離 | `config/provider_catalog.py` 不得 import Provider 實作（由合約測試強制） |
| 清除死碼 | 完成遷移後移除相容性程式碼，除非明確需保留已發布介面 |
| 測試覆蓋 | 行為變更須附帶聚焦的測試與相關邊界案例 |

### 15.5 版本控管規則

| 變更類型 | 是否需升版 |
|---------|-----------|
| Runtime 程式碼 | ✅ 需提升 `pyproject.toml` 版號並在同一 commit 更新 `uv lock` |
| 封裝、依賴 | ✅ 同上 |
| 安裝／CI 腳本 | ✅ 同上 |
| 文件 | ❌ |
| 測試、smoke 覆蓋 | ❌ |
| 儲存庫設定 | ❌ |

> **對使用者的意義**：升級時只要比對版號是否變動，即可判斷「是否需要重新執行驗證與 smoke 測試」。版號未變表示僅有文件或測試變更。

### 15.6 貢獻規則

- 於 [Issues](https://github.com/Alishahryar1/free-claude-code/issues) 回報 bug 與功能請求
- **修改 README 前須先開 Issue 討論**
- **不接受 Docker 整合的 PR**
- 回報 bug 時須附上：完整的模型對應設定、失敗當下的作用中模型、完整錯誤訊息、可重現步驟
- 行為變更須附帶聚焦的測試
- 保持變更範圍收斂，避免夾帶不相關的修改

---

## 16. 常見問題（FAQ）

### Q1：Coding Agent 無法連線到 FCC？

依序確認：

1. `fcc-server` 是否執行中（或桌面應用是否常駐）：`curl http://localhost:8082/health`
2. Port 是否被佔用或與 Admin UI 設定不一致
3. `ANTHROPIC_BASE_URL` 是否誤加 `/v1`（Anthropic 側不應加）
4. `ANTHROPIC_AUTH_TOKEN` 是否與 Admin UI 一致
5. 防火牆是否阻擋本機迴環連線
6. 最簡解法：直接使用 `fcc-claude` 等啟動器，避免手動設定

### Q2：API Key 無效或 Provider 連不上？

1. 於 Admin UI 使用該 Provider 的「測試」功能確認
2. 確認金鑰未過期、額度未耗盡
3. 確認金鑰前綴正確（如 NVIDIA NIM 為 `nvapi-`）
4. 企業網路需設定對應的 `<PROVIDER>_PROXY`
5. 確認金鑰與端點配對正確——`kimi` 與 `kimi_code`、`qwencloud` 與 `qwencloud_coding`、`zai` 與 `zai_api` 皆**不可互換**

### Q3：`/model` 選單是空的？

`/model` 依賴 Gateway Model Discovery。使用 `fcc-claude` 啟動即會自動注入 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`。若手動啟動，需自行設定該變數，並確認 `GET /v1/models` 有回應內容。

### Q4：Claude Code 一直要求登入？

編輯 `~/.claude.json`（Windows 為 `%USERPROFILE%\.claude.json`），合併 `"hasCompletedOnboarding": true`，儲存後重啟。詳見 [6.10 節](#610-客戶端疑難排解)。

### Q5：本地模型回傳 HTTP 400？

最常見原因是**上下文長度不足**。Coding Agent 的系統提示與工具定義通常已佔數千 Token：

- llama.cpp：提高 `llama-server` 的 `--ctx-size`（建議 32K 以上）
- LM Studio：於模型載入設定中調高 context length
- Ollama：確認模型本身支援足夠的上下文

其次的原因是**模型不支援 Tool Use**，此時應更換模型。

### Q6：本地模型很慢？

- 使用量化模型（Q4_K_M 等）
- 確認 GPU 加速已啟用（`nvidia-smi` 觀察使用率）
- 降低 `PROVIDER_MAX_CONCURRENCY` 至 1
- 提高 `HTTP_READ_TIMEOUT` 與 `PROVIDER_PROGRESS_TIMEOUT`
- 將 `MODEL_HAIKU` 指向更小的模型，讓背景任務不佔用主模型資源

### Q7：串流中途斷線？

- 提高 `HTTP_READ_TIMEOUT` 與 `PROVIDER_PROGRESS_TIMEOUT`
- 經反向代理時，必須設定 `proxy_buffering off` 與足夠的 `proxy_read_timeout`
- 檢查上游 Provider 是否觸發限流
- 設定 `MODEL_FALLBACKS`，使斷線後可自動改用備援模型

### Q8：Codex 一直認證失敗？

- `base_url` 必須是 `http://127.0.0.1:8082/v1`（**要有 `/v1`**）
- `wire_api` 必須是 `"responses"`
- `[model_providers.fcc.auth]` 應使用 `command = "fcc-codex"` 搭配 `args = ["--print-proxy-auth-token"]`，讓 Token 自動同步
- 設定或換模型後必須重啟 Codex App／VS Code

### Q9：Fallback 沒有生效？

- 確認 `MODEL_FALLBACKS` 中的每個參照皆為合法的 `provider/model` 格式
- 確認清單中無重複項（重複會導致啟動驗證失敗）
- 確認 Fallback 對應的 Provider 已設定金鑰
- Fallback 在**主模型重試耗盡後**才觸發，短暫錯誤可能先由重試機制吸收

### Q10：如何在團隊中統一設定？

建立標準化的 `.env` 範本（不含金鑰），透過內部文件或設定管理工具散布；金鑰由各成員自行申請並填入。切勿共用同一把金鑰——這既違反多數 Provider 的條款，也讓成本無法歸屬。

### Q11：企業防火牆環境如何設定？

為需連外的 Provider 設定對應的 `<PROVIDER>_PROXY`，支援 `http` 與 `socks5`：

```dotenv
NVIDIA_NIM_PROXY="http://user:pass@proxy.corp.local:8080"
OPENROUTER_PROXY="http://user:pass@proxy.corp.local:8080"
```

本地 Provider 的 Proxy 變數應**留空**，否則本機請求會被錯誤地送往外部 Proxy。

### Q12：Voice Note 如何啟用？

重新執行安裝腳本並帶上語音參數（見 [3.3 節](#33-方式一官方安裝腳本推薦)），重啟 `fcc-server`，於 **Admin UI → Messaging → Voice** 啟用並選擇後端與模型。本地受管制模型需 `HUGGINGFACE_API_KEY`；NVIDIA NIM 轉錄需 `NVIDIA_NIM_API_KEY`。

### Q13：Admin UI 打不開？

- 確認服務執行中且 Port 正確
- 確認網址為 `http://127.0.0.1:8082/admin`
- 若為遠端主機，需建立 SSH Tunnel（見 [13.2 節](#132-proxy-認證強化)）
- 若設定了 `FCC_OPEN_BROWSER=false`，需手動開啟

### Q14：可以用 Docker 部署嗎？

上游明確**不接受 Docker 整合的 PR**，且 FCC 深度依賴本機路徑（`~/.fcc`）、桌面系統匣與本機 Agent 行程管理。建議改以 systemd／launchd／工作排程器管理常駐服務。

### Q15：`fcc-init` 指令找不到？

該指令在 v6 已移除。設定檔現由 Admin UI 建立與管理，位置為 `~/.fcc/.env`。舊路徑的設定會在啟動時自動遷移。

### Q16：升級後舊的 Thinking 設定失效了？

`ENABLE_MODEL_THINKING`、`ENABLE_OPUS_THINKING` 等變數已被 `REASONING_POLICY` 與 `REASONING_<TIER>` 取代，語意也從布林開關改為八段式等級。請依 [2.7 節](#27-reasoning-推理強度控制)重新設定。

### Q17：多人可以共用一台 FCC 嗎？

技術上可透過反向代理達成，但**不建議**：FCC 的憑證與工作階段皆繫結於單一使用者的 `~/.fcc/`，無法做租戶隔離；且多數 Provider 的條款禁止帳號共用。正確做法是每位開發者在自己的機器上執行 FCC，各自持有金鑰。

### Q18：使用 FCC 是否合法／合規？

FCC 本身為 MIT 授權的開源專案，專案立場是遵循各 Provider 的服務條款。真正的合規風險在於**你選用的 Provider 及其使用方式**——特別是訂閱制方案用於團隊、CI 或商業營運的情境。導入前請完成 [13.6 節](#136-服務條款與授權合規)的檢核。

### Q19：怎麼知道目前實際用的是哪個模型？

- 於 Claude Code 中執行 `/model` 檢視目前選定的模型
- 查看 Admin UI 的狀態頁
- 檢視 `~/.fcc/logs/server.log` 中的路由紀錄
- 若 Fallback 已觸發，實際使用的模型可能與設定的主模型不同——這是最容易被忽略的情況

### Q20：出現 `undefined ... input_tokens` 或 usage 相關錯誤？

代表上游 Provider 未正確回報 usage 中繼資料。多發生於相容性較差的模型或本地伺服器。處理方式：更新至最新版 FCC、改用相容性較好的模型，或在回報 Issue 時附上完整的模型對應設定與錯誤訊息。

---

## 17. 最佳實務（Best Practices）

### 17.1 架構設計

- **依任務分派模型階層**：架構設計走 Opus、日常實作走 Sonnet、背景任務走 Haiku（本地或極速模型）
- **Fallback 必須跨供應商**：同一家的不同模型無法防範該供應商整體中斷
- **鏈尾放本地模型**：確保完全離線時仍有最低限度的可用性
- **驗證 Tool Use 能力**：任何進入路由或 Fallback 的模型都必須支援工具呼叫
- **設定即程式碼**：以標準化 `.env` 範本管理，金鑰另行注入
- **不要容器化**：改用作業系統層級的服務管理

### 17.2 Prompt Engineering

- **明確指定技術棧與版本**：避免模型混用不同版本的 API
- **提供專案上下文**：架構風格、命名慣例、既有模式
- **分步驟拆解複雜任務**：一次一個關注點，比一次要求全部更可靠
- **要求結構化輸出**：指定格式（Markdown、JSON、Mermaid）便於後續處理
- **標註審查重點**：明確告知希望模型優先檢查什麼
- **範本納入版控**：Prompt 與程式碼同等對待，並在範本中標註建議的模型階層
- **針對較弱模型調整**：使用免費或小型模型時，指令需更明確、任務需更細分

### 17.3 成本最佳化

| 措施 | 效益 | 實施難度 |
|------|------|---------|
| 模型階層分派 | 高 | 低 |
| 保持內建最佳化開啟 | 中 | 極低 |
| 啟用 RTK | 高 | 低 |
| 降低 `REASONING_POLICY` | 中高 | 低 |
| 免費 Provider 為主力 | 高 | 低 |
| 本地模型承接背景任務 | 中高 | 中 |
| 控制 Fallback 鏈長度 | 中 | 低 |
| Provider 端硬性消費上限 | 高（防災） | 低 |

### 17.4 安全性

- **第一天就改掉三項預設值**：`HOST`、`PROXY_AUTH_ENABLED`、`ANTHROPIC_AUTH_TOKEN`
- **Admin UI 永不對外**：遠端管理一律走 SSH Tunnel 或 VPN
- **生產環境關閉所有 `LOG_RAW_*`**
- **保持 `WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false`**
- **Messaging Bot 預設停用**；必須啟用時嚴格限制 `ALLOWED_DIR` 與允許清單
- **建立專案資料分級**：可用雲端／僅限企業雲／僅限本地
- **金鑰最小權限並定期輪換**
- **保持 Agent 本體更新**，並留意專案層級設定檔是否被竄改
- **對 Agent 的破壞性操作保持人工審查**

### 17.5 反模式清單

| 反模式 | 後果 | 正確做法 |
|-------|------|---------|
| 所有階層都指向同一昂貴模型 | 配額迅速耗盡 | 依任務分派階層 |
| Fallback 鏈全在同一供應商 | 無法防範供應商整體中斷 | 跨供應商設計 |
| Fallback 鏈過長且全為付費 | 單次失敗連鎖產生高額成本 | 限制鏈長，鏈尾放本地模型 |
| 團隊共用一把金鑰 | 違反條款、成本無法歸屬 | 各自申請金鑰 |
| 訂閱制 Provider 接入 CI | 極可能違反服務條款 | CI 使用按量計費 API |
| 為了除錯開啟 `LOG_RAW_*` 後忘記關閉 | 原始碼明文長存磁碟 | 除錯後立即關閉並清除日誌 |
| 直接把 8082 對外開放 | 任何人可代表你呼叫所有 Provider | 綁定迴環 + 啟用認證 |
| 只監控服務存活 | Provider 靜默失效無人察覺 | 監控 Fallback 觸發率 |
| 只跑 `smoke/prereq` 就宣告驗證完成 | 未驗證 Tool Use 與串流 | 執行 `smoke/product` |
| 前景執行 `fcc-server` | 終端關閉即中斷 | 使用服務管理器 |
| 未經法務確認即全面導入 | 合規風險 | 導入前完成 ToS 檢核 |

---

## 18. 範例 Prompt 集

### 18.1 通用開發 Prompt

```text
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

### 18.2 Code Review Prompt

```text
請對以下程式碼進行全面 Code Review：

檢查面向：
1. 程式碼品質（可讀性、命名、複雜度）
2. 效能（N+1 查詢、記憶體使用、不必要的迴圈）
3. 安全性（OWASP Top 10）
4. 測試覆蓋率建議
5. 架構合理性與分層邊界

輸出格式：
- 🔴 嚴重問題（必須修正）
- 🟡 建議改善
- 🟢 值得保留的優點

每個問題請說明：觸發條件、影響範圍、具體修正方式。

[貼上程式碼]
```

### 18.3 逆向工程 Prompt

```text
請分析以下 Legacy 系統程式碼：

目標：
1. 繪製系統架構圖（Mermaid）
2. 列出所有業務規則
3. 識別技術債並排序
4. 產出重建的 User Story 清單
5. 建議現代化架構方案

限制：
- 保持業務邏輯不變
- 資料庫結構可重新設計
- 目標技術棧：Spring Boot 3 + PostgreSQL

若資訊不足以判斷某項業務規則，請明確標示為「需確認」，不要臆測。

[貼上程式碼]
```

### 18.4 升級評估 Prompt

```text
請評估以下專案從 [舊版本] 升級到 [新版本] 的影響：

評估項目：
1. Breaking Changes 清單
2. 棄用 API 替代方案
3. 第三方套件相容性
4. 設定變更需求
5. 預估工作量（人天）
6. 風險評估與緩解計畫
7. 建議的分批升級順序

[貼上 pom.xml / build.gradle / package.json]
```

### 18.5 多模型交叉驗證 Prompt

```text
以下是另一個 AI 模型對這段程式碼的分析結論。
請獨立分析同一段程式碼，然後：

1. 列出你同意的結論及理由
2. 列出你不同意的結論及理由
3. 指出對方遺漏的問題
4. 針對有爭議的項目，說明如何以實驗或測試驗證

不要因為對方已提出結論就直接採信。

[貼上前一個模型的分析]
[貼上原始程式碼]
```

### 18.6 FCC 環境診斷 Prompt

```text
我的 Free Claude Code 環境出現以下問題：

症狀：[描述]
錯誤訊息：[完整貼上]

環境資訊：
- FCC 版本：[fcc-server --version 的輸出]
- 作業系統：[版本]
- MODEL：[設定值]
- MODEL_FALLBACKS：[設定值]
- 使用的 Agent：[claude / codex / ...]

請協助：
1. 判斷問題最可能的根因
2. 列出驗證該假設的具體指令
3. 提供修正步驟
4. 說明如何避免再次發生
```

---

## 19. 導入檢查清單（Checklist）

### 19.1 安裝與環境

- [ ] Node.js 22 LTS 已安裝
- [ ] 目標 Coding Agent 本體已安裝
- [ ] uv 已安裝且版本 ≥ 0.11.16
- [ ] Python 3.14.0 已安裝
- [ ] 安裝腳本已完成稽核（企業環境）
- [ ] FCC 已安裝，`fcc-server --version` 可正常回應
- [ ] 至少一個 Provider 已設定且測試通過
- [ ] `MODEL` 已設定且格式驗證通過
- [ ] 服務啟動日誌無設定驗證警告
- [ ] `curl http://localhost:8082/health` 回應正常
- [ ] `GET /v1/models` 可列出模型
- [ ] Admin UI 可正常存取

### 19.2 客戶端連線

- [ ] Anthropic 客戶端的 `ANTHROPIC_BASE_URL` 為 `http://localhost:8082`（**無** `/v1`）
- [ ] Codex 客戶端的 `base_url` 為 `http://127.0.0.1:8082/v1`（**有** `/v1`）
- [ ] `ANTHROPIC_AUTH_TOKEN` 與 Admin UI 一致
- [ ] `fcc-claude` 可正常啟動並完成一次對話
- [ ] `/model` 可列出模型清單
- [ ] VS Code 設定完成（若使用）
- [ ] JetBrains ACP 設定完成（若使用）
- [ ] Codex App／VS Code 的 `config.toml` 設定完成（若使用）
- [ ] Connected Account 連結後已重啟 Agent（若使用）

### 19.3 模型與路由

- [ ] 已確認所選模型支援 Tool Use
- [ ] 已確認上下文長度足夠（本地模型尤須注意）
- [ ] 階層路由（Fable／Opus／Sonnet／Haiku）已依任務複雜度分派
- [ ] `MODEL_FALLBACKS` 已設定且跨不同供應商
- [ ] Fallback 鏈尾已放置本地模型
- [ ] Fallback 最壞情況成本已評估
- [ ] `REASONING_POLICY` 已依成本政策設定

### 19.4 安全

- [ ] `HOST` 已設為 `127.0.0.1`（或已由反向代理正確隔離）
- [ ] `PROXY_AUTH_ENABLED=true`
- [ ] `ANTHROPIC_AUTH_TOKEN` 已改為高強度隨機字串
- [ ] Admin UI **未**對外網路開放
- [ ] 所有 `LOG_RAW_*` 與 `DEBUG_*` 為 `false`
- [ ] `WEB_FETCH_ALLOW_PRIVATE_NETWORKS=false`
- [ ] Messaging Bot 已停用，或 `ALLOWED_DIR` 為專用沙箱且允許清單已限縮
- [ ] `~/.fcc/.env` 權限為 600，且排除於備份同步與版本控制
- [ ] 金鑰輪換週期已建立
- [ ] 各 Provider 已設定消費上限

### 19.5 合規

- [ ] 各 Provider 的 ToS 已檢視，商業使用授權已確認
- [ ] 訂閱制 Provider **未**用於 CI 或團隊共用
- [ ] 未共用單一帳號金鑰
- [ ] 資料處理地區符合法規要求
- [ ] 需要 DPA 的 Provider 已簽署
- [ ] 專案資料分級制度已建立並公告
- [ ] 法務／資安已正式核可，紀錄已保留
- [ ] 季度複審機制已排入行事曆

### 19.6 團隊導入

- [ ] 主要與備援 Provider 組合已選定
- [ ] Prompt Template 目錄已建立並納入版控
- [ ] AI 使用規範已制定並公告
- [ ] Code Review 流程已納入 AI 產出的審查要求
- [ ] 成本監控與告警已建立
- [ ] Pilot Team 試用已完成且回饋已收斂
- [ ] 團隊內部使用指南已撰寫
- [ ] AI Champion 已指派

### 19.7 維運

- [ ] 服務以 systemd／launchd／工作排程器管理（非前景執行）
- [ ] 健康檢查排程已設定
- [ ] Fallback 觸發率已納入監控
- [ ] Token 用量監控與預算告警已建立
- [ ] 升級與回滾流程已文件化
- [ ] `smoke/product` 已針對目標 Provider 驗證通過
- [ ] 故障排除 SOP 已準備
- [ ] `~/.fcc/` 備份與還原程序已驗證

### 19.8 開發貢獻

- [ ] `./scripts/ci.sh`（或 `.\scripts\ci.ps1`）全數通過
- [ ] `uv run ruff format` 已執行
- [ ] `uv run ruff check --fix` 無殘留問題
- [ ] `uv run ty check` 通過，且未使用任何忽略註解
- [ ] `uv run pytest` 全綠
- [ ] 行為變更已附帶聚焦測試
- [ ] Runtime 變更已提升 `pyproject.toml` 版號並更新 `uv lock`
- [ ] 未提交 Docker 整合或未經 Issue 討論的 README 變更

---

## 20. 附錄（Appendix）

### 20.1 環境變數全表

**核心與模型**

| 變數 | 預設 | 說明 |
|------|------|------|
| `MODEL` | `nvidia_nim/nvidia/nemotron-3-super-120b-a12b` | 預設模型（必填） |
| `MODEL_FABLE` / `MODEL_OPUS` / `MODEL_SONNET` / `MODEL_HAIKU` | 空 | 階層覆寫 |
| `MODEL_FALLBACKS` | 空 | 有序 Fallback 清單（逗號分隔） |
| `REASONING_POLICY` | `client` | 根層推理政策 |
| `REASONING_FABLE` / `REASONING_OPUS` / `REASONING_SONNET` / `REASONING_HAIKU` | `inherit` | 階層推理政策 |

**服務與認證**

| 變數 | 預設 | 說明 |
|------|------|------|
| `HOST` | `0.0.0.0` | 監聽位址（建議改 `127.0.0.1`） |
| `PORT` | `8082` | 監聽埠 |
| `PROXY_AUTH_ENABLED` | `false` | 是否強制 Bearer 認證（建議 `true`） |
| `ANTHROPIC_AUTH_TOKEN` | `freecc` | 代理認證 Token（建議改高強度值） |
| `FCC_OPEN_BROWSER` | `true` | 啟動時是否開啟 Admin UI |

**效能與逾時**

| 變數 | 預設 | 說明 |
|------|------|------|
| `PROVIDER_RATE_LIMIT` | `1` | 每時間窗最大請求數 |
| `PROVIDER_RATE_WINDOW` | `2` | 時間窗長度（秒） |
| `PROVIDER_MAX_CONCURRENCY` | `2` | 最大並行請求數 |
| `PROVIDER_PROGRESS_TIMEOUT` | `600` | 串流無進展逾時（秒） |
| `HTTP_CONNECT_TIMEOUT` | `10` | 連線逾時（秒） |
| `HTTP_READ_TIMEOUT` | `120` | 讀取逾時（秒） |
| `HTTP_WRITE_TIMEOUT` | `10` | 寫入逾時（秒） |

**最佳化與 Web Tools**

| 變數 | 預設 | 說明 |
|------|------|------|
| `FAST_PREFIX_DETECTION` | `true` | 本地指令前綴偵測 |
| `ENABLE_NETWORK_PROBE_MOCK` | `true` | 本地回應探測請求 |
| `ENABLE_TITLE_GENERATION_SKIP` | `true` | 跳過標題生成 |
| `ENABLE_SUGGESTION_MODE_SKIP` | `true` | 跳過建議模式 |
| `ENABLE_FILEPATH_EXTRACTION_MOCK` | `true` | 本地路徑擷取 |
| `ENABLE_WEB_SERVER_TOOLS` | `true` | 伺服器端 web 工具 |
| `WEB_FETCH_ALLOWED_SCHEMES` | `http,https` | 允許的 URL scheme |
| `WEB_FETCH_ALLOW_PRIVATE_NETWORKS` | `false` | 是否允許私有網段（**保持 false**） |

**日誌與診斷**

| 變數 | 預設 | 說明 |
|------|------|------|
| `LOG_LEVEL` | `INFO` | 日誌層級 |
| `LOG_RAW_API_PAYLOADS` | `false` | 記錄原始 API 內容 |
| `LOG_RAW_SSE_EVENTS` | `false` | 記錄原始 SSE 事件 |
| `LOG_API_ERROR_TRACEBACKS` | `false` | 記錄 API 錯誤堆疊 |
| `LOG_RAW_MESSAGING_CONTENT` | `false` | 記錄訊息內容 |
| `LOG_RAW_CLI_DIAGNOSTICS` | `false` | 記錄 CLI 診斷輸出 |
| `LOG_MESSAGING_ERROR_DETAILS` | `false` | 記錄訊息錯誤細節 |
| `DEBUG_PLATFORM_EDITS` | `false` | 平台編輯除錯 |
| `DEBUG_SUBAGENT_STACK` | `false` | 子 Agent 堆疊除錯 |

**Messaging 與語音**

| 變數 | 預設 | 說明 |
|------|------|------|
| `MESSAGING_PLATFORM` | `discord` | `discord` / `telegram` / `none` |
| `DISCORD_BOT_TOKEN` / `ALLOWED_DISCORD_CHANNELS` | 空 | Discord 設定 |
| `TELEGRAM_BOT_TOKEN` / `ALLOWED_TELEGRAM_USER_ID` | 空 | Telegram 設定 |
| `TELEGRAM_PROXY_URL` | 空 | Telegram 專用 Proxy |
| `ALLOWED_DIR` | 空 | Bot 可存取的絕對路徑 |
| `MESSAGING_RATE_LIMIT` / `MESSAGING_RATE_WINDOW` | `1` / `1` | 訊息限流 |
| `MAX_MESSAGE_LOG_ENTRIES_PER_CHAT` | 空 | 每個聊天的訊息紀錄上限 |
| `VOICE_NOTE_ENABLED` | `true` | 語音訊息開關 |
| `WHISPER_DEVICE` | `cpu` | `cpu` / `cuda` / `nvidia_nim` |
| `WHISPER_MODEL` | `base` | Whisper 模型 |

**Provider 憑證**（節錄；完整清單見 [5.2 節](#52-完整-provider-目錄)）

`NVIDIA_NIM_API_KEY`、`OPENROUTER_API_KEY`、`GROQ_API_KEY`、`CLINE_API_KEY`、`XAI_API_KEY`、`QWENCLOUD_API_KEY`、`QWENCLOUD_CODING_API_KEY`、`TOGETHER_API_KEY`、`DEEPINFRA_API_KEY`、`SILICONFLOW_API_KEY`、`NEBIUS_API_KEY`、`CHUTES_API_KEY`、`FEATHERLESS_API_KEY`、`AGNES_API_KEY`、`ZENMUX_API_KEY`、`WANDB_API_KEY`、`AZURE_OPENAI_API_KEY`、`AZURE_OPENAI_BASE_URL`、`GEMINI_API_KEY`、`VERTEX_PROJECT_ID`、`VERTEX_LOCATION`、`DEEPSEEK_API_KEY`、`MISTRAL_API_KEY`、`CODESTRAL_API_KEY`、`OPENCODE_API_KEY`、`AI_GATEWAY_API_KEY`、`AWS_BEARER_TOKEN_BEDROCK`、`BEDROCK_BASE_URL`、`HUGGINGFACE_API_KEY`、`COHERE_API_KEY`、`WAFER_API_KEY`、`KIMI_API_KEY`、`KIMI_CODE_API_KEY`、`KILO_API_KEY`、`MINIMAX_API_KEY`、`CEREBRAS_API_KEY`、`SAMBANOVA_API_KEY`、`FIREWORKS_API_KEY`、`NOVITA_API_KEY`、`CLOUDFLARE_API_TOKEN`、`CLOUDFLARE_ACCOUNT_ID`、`ZAI_API_KEY`、`TOKENROUTER_API_KEY`、`TOKENROUTER_BASE_URL`、`NARAROUTE_API_KEY`、`NARAROUTE_BASE_URL`、`POOLSIDE_API_KEY`、`LLM7_API_KEY`、`OLLAMA_API_KEY`、`LM_STUDIO_BASE_URL`、`LLAMACPP_BASE_URL`、`OLLAMA_BASE_URL`

**Per-Provider Proxy**：每家 Provider 皆有對應的 `<PROVIDER>_PROXY` 變數（如 `NVIDIA_NIM_PROXY`、`OPENROUTER_PROXY`、`AZURE_OPENAI_PROXY`、`VERTEX_PROXY`…）。

### 20.2 CLI 指令速查

| 指令 | 功能 |
|------|------|
| `fcc-server` | 啟動 FCC 服務 |
| `fcc-server --version` | 查詢版本（不啟動服務） |
| `fcc-claude` | 啟動 Claude Code |
| `fcc-codex` | 啟動 Codex |
| `fcc-codex --print-proxy-auth-token` | 輸出目前的代理認證 Token（供 Codex 設定用） |
| `fcc-pi` | 啟動 Pi |
| `fcc-opencode` | 啟動 OpenCode |
| `fcc-cline` | 啟動 Cline |
| `fcc-hermes` | 啟動 Hermes |
| `fcc-dsh` | 啟動 DeepSeek Harness Web |
| `fcc-grok` | 啟動 Grok Build |
| `fcc-muse` | 啟動 Muse Code |
| `fcc-aider` | 啟動 Aider |
| `fcc-desktop` | 啟動桌面（GUI）進入點 |
| `uv run fcc-server` | 由原始碼 checkout 啟動 |
| `./scripts/ci.sh` / `.\scripts\ci.ps1` | 執行完整本地 CI |

### 20.3 API 端點速查

**協議端點**

| 端點 | 方法 | 用途 |
|------|------|------|
| `/v1/messages` | POST | Anthropic Messages API |
| `/v1/messages/count_tokens` | POST | Token 計數 |
| `/v1/responses` | POST | OpenAI Responses API |
| `/v1/models` | GET | 模型目錄（Gateway Model Discovery） |
| `/health` | GET | 健康檢查 |
| `/` | GET | 服務資訊 |
| `/stop` | POST | 中止執行中的 CLI 工作 |

**Admin 端點**

| 端點 | 方法 | 用途 |
|------|------|------|
| `/admin` | GET | Admin UI |
| `/admin/api/config` | GET | 讀取設定 |
| `/admin/api/config/apply` | POST | 套用設定 |
| `/admin/api/status` | GET | 服務狀態 |
| `/admin/api/providers/local-status` | GET | 本地 Provider 狀態 |
| `/admin/api/providers/{id}/test` | POST | 測試 Provider |
| `/admin/api/providers/{id}/auth` | GET / POST / DELETE | Connected Account 管理 |
| `/admin/api/models` | GET | 模型清單 |
| `/admin/api/models/refresh` | POST | 重新整理模型目錄 |

**Code Sessions 端點**

| 端點 | 方法 | 用途 |
|------|------|------|
| `/admin/code` | GET | Code Sessions UI |
| `/admin/api/code/bootstrap` | GET | 初始化狀態 |
| `/admin/api/code/sessions` | GET / POST | 列出／建立工作階段 |
| `/admin/api/code/sessions/{id}/turns` | POST | 送出一輪對話 |
| `/admin/api/code/sessions/{id}/stop` | POST | 中止工作 |
| `/admin/api/code/events` | GET（SSE） | 事件串流 |

### 20.4 名詞對照表

| 英文 | 繁體中文 | 說明 |
|------|---------|------|
| Coding Agent | 程式碼代理／編碼代理 | Claude Code、Codex 等終端 AI 開發工具 |
| Provider | 供應商 | 提供模型推理服務的上游 |
| Model Reference | 模型參照 | `provider/model` 格式的模型識別 |
| Model Tier | 模型階層 | Fable／Opus／Sonnet／Haiku |
| Fallback Chain | 備援鏈 | 主模型失敗後依序嘗試的模型清單 |
| Reasoning Effort | 推理強度 | 模型投入推理的程度 |
| Connected Account | 連結帳號 | 以訂閱帳號授權而非 API Key |
| Custom Model Slug | 自訂模型代號 | 手動輸入未列於目錄的模型參照 |
| Hermetic Test | 封閉測試 | 不依賴外部服務的測試 |
| Smoke Test | 冒煙測試 | 對真實服務的端到端驗證 |
| Prereq / Product | 前置／產品 | Smoke 測試的兩種類別 |
| Token Optimization | Token 最佳化 | 減少送往上游的 Token 量 |
| Gateway Model Discovery | 閘道模型發現 | 客戶端自動查詢可用模型 |
| SSE | 伺服器推送事件 | Server-Sent Events，串流回應機制 |
| ToS | 服務條款 | Terms of Service |
| DPA | 資料處理協議 | Data Processing Agreement |

### 20.5 參考資源

**上游專案**

- [free-claude-code GitHub](https://github.com/Alishahryar1/free-claude-code)
- [README](https://github.com/Alishahryar1/free-claude-code/blob/main/README.md)
- [CONTRIBUTING](https://github.com/Alishahryar1/free-claude-code/blob/main/CONTRIBUTING.md)
- [.env.example](https://github.com/Alishahryar1/free-claude-code/blob/main/.env.example)
- [Issues](https://github.com/Alishahryar1/free-claude-code/issues)

**Coding Agent**

- [Claude Code 文件](https://code.claude.com/docs/en/overview)
- [OpenAI Codex](https://github.com/openai/codex)
- [Pi](https://github.com/earendil-works/pi)
- [OpenCode](https://github.com/anomalyco/opencode)
- [Cline](https://github.com/cline/cline)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- [Grok Build](https://github.com/xai-org/grok-build)
- [Aider](https://aider.chat/)
- [RTK](https://github.com/rtk-ai/rtk)

**工具鏈**

- [uv](https://docs.astral.sh/uv/)
- [Ruff](https://github.com/astral-sh/ruff)
- [Ty](https://pypi.org/project/ty/)
- [Loguru](https://github.com/Delgan/loguru)
- [FastAPI](https://fastapi.tiangolo.com/)

**Provider 金鑰申請（節錄）**

- [NVIDIA NIM](https://build.nvidia.com/settings/api-keys)
- [OpenRouter](https://openrouter.ai/keys)
- [Groq](https://console.groq.com/keys)
- [Google AI Studio](https://aistudio.google.com/apikey)
- [DeepSeek](https://platform.deepseek.com/api_keys)
- [Cerebras](https://cloud.cerebras.ai/)
- [Mistral](https://console.mistral.ai/)

---

## 文件維護說明

| 項目 | 內容 |
|------|------|
| 對應上游版本 | `v6.1.4`（2026-09-08 取樣） |
| 建議複審週期 | 每季一次；上游 `pyproject.toml` 版號變動時應加開複審 |
| 重點複審項目 | Provider 目錄增減、環境變數異動、CLI 指令變更、各 Provider ToS 變更 |
| 內容回報 | 若發現手冊與實際行為不符，請至 [Issues](https://github.com/Alishahryar1/free-claude-code/issues) 回報，或直接更新本手冊 |

> **重要提醒**：FCC 是一個迭代極快的專案（53,800+ Stars、378 個開放 Issue、幾乎每日推送）。本手冊記錄的是 2026 年 9 月 8 日的狀態。Provider 清單、模型 ID 與免費額度政策的變動尤其頻繁——**實際設定請一律以 Admin UI 的下拉選單與上游 `.env.example` 為準**。
