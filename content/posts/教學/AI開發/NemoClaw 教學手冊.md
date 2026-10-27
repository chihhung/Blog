+++
date = '2026-10-27T15:17:25+08:00'
draft = false
title = 'NemoClaw 教學手冊'
tags = ['教學','AI開發','NemoClaw','OpenShell','AI Agent','Sandbox','DevSecOps','SSDLC']
categories = ['教學']
+++

# NemoClaw 企業級 AI Agent 沙盒參考堆疊教學手冊（實戰與維運）

> **一句話定位**：NVIDIA NemoClaw 是一套「把受支援的 AI Agent 裝進 NVIDIA OpenShell 沙盒」的**開源參考技術堆疊**。它提供引導式安裝（onboarding）、版本化 Blueprint、託管推理路由、網路政策 preset、狀態保存與生命週期指令；真正執行隔離、攔截網路、保管憑證的是底下的 **OpenShell**。NemoClaw 讓你「少做整合工作」，不會讓 Agent「自動變安全」。
>
> **適用對象**：資深工程師、架構師、DevOps／DevSecOps、資安與維運人員、AI 平台管理者。PM、SA、SD 可依「閱讀路徑」選讀。內容偏實戰與維運，假設讀者熟悉 Linux、Docker、Git，以及至少一種 AI Coding 工具。
>
> **版本基準**：
>
> | 項目 | 內容 |
> |---|---|
> | NemoClaw 版本 | **v0.0.139**（tag commit `a08ae7a`，2026-10-26）；官方文件站 `latest` 已對應此版 |
> | 安裝程式預設版本 | 官方安裝程式預設追蹤 `lkg`（last known good）標籤，研究當日指向 **v0.0.137**（`f00fb1d`，2026-10-21）；要用 v0.0.139 必須明確指定 `NEMOCLAW_INSTALL_TAG=v0.0.139`（第 4 章） |
> | 搭配的 OpenShell | **0.0.116**（Blueprint 的 `min_openshell_version` 與 `max_openshell_version` 都是 0.0.116；`@nvidia/openshell-sdk` 也釘 0.0.116） |
> | 支援的 Agent | OpenClaw（預設）、Hermes、LangChain Deep Agents Code（`dcode` 0.1.71）；三者在官方平台矩陣皆為 *Tested*，但 Hermes 官方註明「尚未宣稱與 OpenClaw 的正式環境同等」 |
> | 專案階段 | **alpha／Early preview**（官方平台矩陣：自 2026-03-16 起），維護者以 best effort 回應、**無 SLA** |
> | 原始碼核對 | `NVIDIA/NemoClaw` tag `v0.0.139`：`docs/`（官方文件原始檔）、`install.sh`、`scripts/install-openshell.sh`、`nemoclaw-blueprint/`（Blueprint 與政策）、`agents/*/`（各 Agent 的 manifest 與政策）、`src/lib/`（CLI 實作） |
> | 研究基準日期 | **2026-10-27**；`main` 追蹤至 `bafe6cc`（2026-10-26，領先 v0.0.139 共 18 個 commit）；另有 Rust 重寫的 `v1` 分支（見 1.7）。1.1 版於同日再核對：沒有新 tag，`lkg` 仍指向 v0.0.137，`main` 仍為 `bafe6cc`（18.11） |
> | 實測狀態 | **未在實機安裝 NemoClaw 或 OpenShell**。所有 NemoClaw／OpenShell 指令都對照 v0.0.139 官方文件與原始碼，標 📖；需要實際環境才能確認的內容標 🧪 並附驗證步驟。手冊內附的 5 支企業自訂審查工具（政策 lint、交付報告比對、架構依賴檢查、逆向工程引用檢查、測試弱化檢查）、安全公告版本下限腳本與 ArchUnit 範例，已在撰寫環境以合成資料實測，標 ✅ |
> | 撰寫環境 | Windows 11 Pro 10.0.26300、Python 3.12.8、PyYAML 6.0.3、OpenJDK 21.0.4、Maven 3.9.9、Node.js 24.16.0（僅用於撰寫與驗證審查工具） |
> | 手冊版本 | **1.1**（2026-10-27；1.0 於同日初版；版本紀錄見 18.13） |
>
> **文件性質**：企業內部教育訓練與開發規範。內容為重新整理、分析與教學化撰寫，不是官方文件翻譯。範例中的主機名稱、帳號、Token、IP、專案與客戶資料**均為虛構**（使用 `example.com`、`corp.example`、`10.x` 等保留或私有範圍）。

---

## 重要聲明（請務必先讀）

1. **NemoClaw 不等於 OpenShell。** NemoClaw 是「參考堆疊」：主機端 CLI（`nemoclaw`／`nemohermes`／`nemo-deepagents`）、Agent 整合層、版本化 Blueprint、政策 preset 與生命週期流程。OpenShell 是「執行環境」：Gateway、沙盒、L7 代理、政策執行、憑證保管。NemoClaw 呼叫 OpenShell 的 API 與 CLI 來建立並設定沙盒，兩者的版本、責任與故障點都不同（第 1、2 章）。
2. **NemoClaw v0.0.139 搭配的是 OpenShell 0.0.116，不是 OpenShell 最新版 v0.1.5。** 同目錄《OpenShell 教學手冊》以 v0.1.5 為基準；兩個版本線在推理路由（`inference.local` 在 OpenShell 0.1.0 移除，但 NemoClaw 0.0.139 仍會用到）、CLI 參數與政策行為上有差異。**在 NemoClaw 管理的環境裡，不要套用 OpenShell v0.1.x 的指令或自行升級 OpenShell**；官方明確要求用 `nemoclaw onboard` 管理 Gateway 與沙盒，避免直接執行 `openshell self-update` 或 `openshell sandbox create`（第 1.9、12 章）。
3. **這是 alpha 專案。** 官方平台矩陣標示 *Stage: alpha*、*Label: Early preview*，介面可能在版本間變動，沒有 SLA。官方「Enterprise Readiness」頁明說：NemoClaw 是「單一主機、單一受信任操作者」的參考工作流程，**不是**多租戶企業控制平面、**沒有**操作者 RBAC、**沒有** SSO 整合、**不支援**離線（air-gapped）安裝。本手冊所有企業建議都以「隔離的非正式環境＋明確風險接受」為前提（第 13、14 章）。
4. **沙盒不是絕對安全。** 官方安全頁的原則是：每一個放行的端點都是可能的資料外洩路徑。沙盒能限制 Agent 碰得到的檔案、程序與網路，但**不會**判斷 Agent 產出的程式碼是否正確，也**不會**阻止 Agent 透過已放行的端點（例如 Deep Agents 預設就放行的 `github.com`）把資料送出去（第 6 章）。
5. **安裝程式預設會送出匿名遙測。** 官方文件寫明：安裝程式與 CLI 預設會嘗試把匿名的操作完成遙測送到 NVIDIA 的固定接收端；要停用，必須在**每一個**執行 NemoClaw 的 shell 先 `export NEMOCLAW_DISABLE_TELEMETRY=1`。企業環境應把這一行寫進標準作業程序（第 4 章）。
6. **`curl … | bash` 必須先下載審查、再固定版本執行。** 官方安裝程式會下載並執行來自 GitHub 的腳本，可能安裝 Node.js、Docker（以 `sudo` 執行 Docker 官方便利腳本）並把使用者加入 `docker` 群組。`docker` 群組成員對 Docker daemon 有等同 root 的影響力。不得要求同仁盲目執行（第 4.3 節）。
7. **AI 說「完成了」不是證據。** 本手冊每個開發、逆向、升級流程都要求可重跑的驗證：政策用 lint 與拒絕測試驗證、程式碼用測試與人工審查驗證、交付報告用 `git diff` 比對驗證（第 6、7、8、9、10 章）。
8. **下一版 NemoClaw 很可能改綁 OpenShell 0.1.5。** `main` 上的 PR #12603（研究日狀態 OPEN，PR 自述 *Not ready for approval or merge*）要把 OpenShell runtime 與 SDK 從 0.0.116 升到 0.1.5。發布後，推理路由、Gateway 設定、volume 與復原流程都會改變，舊沙盒的 volume 也**不會自動複製**。核准新版之前，一律照 12.11 在測試主機演練（第 12 章）。
9. **舊版本有已公告的高風險漏洞。** NVIDIA 在 2026-08-25 發布 Security Bulletin 5872，一次公告 18 個 NemoClaw／OpenShell CVE，最高為 CVSS 9.9 的沙盒逃逸。本手冊的基準版本（v0.0.139／OpenShell 0.0.116）已在修補範圍之後，但企業要盤點每台主機的實際版本，並訂閱後續公告（6.17）。

---

## 標記圖例

| 標記 | 意義 |
|---|---|
| 📖 | 已對照 v0.0.139 官方文件或原始碼，但作者未在實機執行 |
| 🧪 | 尚待實際環境驗證：官方文件未明確說明、或結果取決於你的主機與映像檔；附驗證步驟 |
| ⚠️ | 官方文件之間有落差、版本差異大，或屬實驗性（Experimental）功能 |
| 🏢 | 本手冊的企業建議或自行設計的流程，**不是** NemoClaw／OpenShell 原生功能 |
| ⛔ | 禁止事項、官方不支援或已淘汰的功能 |
| ✅ 已實測 | 作者已在撰寫環境以合成資料實際執行（只限手冊中的審查工具與範例程式，不含 NemoClaw 本身） |

執行位置標記（每個指令區塊前都會標示）：

| 標記 | 執行位置 |
|---|---|
| 🖥️ Host | 執行 NemoClaw 的主機終端機：Linux（Ubuntu 24.04 為主要驗證路徑）、Apple Silicon macOS，或 Windows 上的 WSL 2 Ubuntu |
| 🐧 WSL | Windows 上的 WSL 2 Ubuntu 內部；NemoClaw 在 Windows 上的所有指令都在這裡執行（與 🖥️ Host 相同，特別標示時代表 Windows 情境） |
| 🪟 PowerShell | Windows 原生 PowerShell（只用於 WSL 2、Docker Desktop 的前置準備） |
| 📦 Sandbox | 沙盒內部（`nemoclaw <名稱> connect` 進入後的 shell，或 `nemoclaw <名稱> exec --` 執行的指令） |
| 🔧 CI | CI/CD Runner（GitHub Actions、GitLab CI、Jenkins 等），在沙盒外執行 |

審查方塊（教你檢查 AI 產出時使用）：

| 標記 | 意義 |
|---|---|
| ❌ 壞例 | AI 常見的錯誤產出，只用於審查訓練，**不得複製使用** |
| 🔍 | 檢查方法：用指令或腳本找出問題 |
| ▶️ | 驗證指令與預期結果 |

> ⚠️ **警告**：會造成安全風險、資料遺失或權限擴大的事項。

> ✅ **建議**：本手冊推薦的做法。

> 📌 **註記**：補充說明、版本差異或來源。

### 指令中的名稱慣例

- 官方 CLI 有三個入口：`nemoclaw`（預設 OpenClaw）、`nemohermes`（預設 Hermes）、`nemo-deepagents`（預設 LangChain Deep Agents Code）。三者共用同一套子指令，只是預設 Agent 不同。本手冊以 `nemoclaw` 示範；Deep Agents 專屬內容改用 `nemo-deepagents`。
- 沙盒操作採「沙盒名稱在前」的文法：`nemoclaw <沙盒名稱> <動作>`，例如 `nemoclaw my-assistant status`。全域指令不帶名稱，例如 `nemoclaw status`、`nemoclaw doctor`。
- 範例沙盒名稱：`my-assistant`（OpenClaw）、`dev-order`（Deep Agents，開發用）、`re-legacy`（Deep Agents，逆向工程用）。名稱規則見 4.5。

---

## 閱讀路徑

| 角色 | 必讀 | 選讀 | 可略過 |
|---|---|---|---|
| 初學者（第一次接觸） | 1、2、3、4、17 | 5、11 | 14、15 |
| 資深工程師（要實作） | 1.7～1.9、4～9、11、16 | 10、12 | 15 |
| 架構師（做技術決策） | 1、2、6、7.1～7.3、14 | 9、10、12 | 4.8～4.11 細節 |
| 資安／DevSecOps | 1.4～1.6、2.4、3.6、6、13 | 10、11、14 | 7～9 的 Prompt 細節 |
| 維運人員 | 3、4、5、11、12 | 6.12～6.14 | 7～9 |
| 主管／治理 | 重要聲明、1.5～1.8、13、14.11～14.12、15 | 10 | 4～9 的指令 |

---

## 目錄

- [第1章 NemoClaw 概論](#第1章-nemoclaw-概論)
  - [1.1 設計目的與核心價值](#11-設計目的與核心價值)
  - [1.2 NemoClaw、OpenShell、Agent、LLM、推理服務與工具的關係](#12-nemoclawopenshellagentllm推理服務與工具的關係)
  - [1.3 為什麼自主 Agent 需要檔案、網路、程序與憑證限制](#13-為什麼自主-agent-需要檔案網路程序與憑證限制)
  - [1.4 NemoClaw 與直接在主機執行 Agent 的差異](#14-nemoclaw-與直接在主機執行-agent-的差異)
  - [1.5 優點、限制、導入成本與適用邊界](#15-優點限制導入成本與適用邊界)
  - [1.6 Alpha 階段對企業導入、相容性與維運的影響](#16-alpha-階段對企業導入相容性與維運的影響)
  - [1.7 兩條產品線：v0.0.x（現行）與 v1（開發中）](#17-兩條產品線v00x現行與-v1開發中)
  - [1.8 適合與不適合使用的情境](#18-適合與不適合使用的情境)
  - [1.9 與《OpenShell 教學手冊》的分工與版本差異](#19-與openshell-教學手冊的分工與版本差異)
  - [1.10 本章實務案例與注意事項](#110-本章實務案例與注意事項)
- [第2章 系統架構與元件關係](#第2章-系統架構與元件關係)
  - [2.1 元件總覽](#21-元件總覽)
  - [2.2 圖一：系統元件與資料流架構圖](#22-圖一系統元件與資料流架構圖)
  - [2.3 圖二：Agent 執行任務時的請求流程](#23-圖二agent-執行任務時的請求流程)
  - [2.4 責任邊界與信任邊界](#24-責任邊界與信任邊界)
  - [2.5 Blueprint：版本化的沙盒定義](#25-blueprint版本化的沙盒定義)
  - [2.6 推理路由：附掛式 Provider 與共享路由](#26-推理路由附掛式-provider-與共享路由)
  - [2.7 狀態保存、日誌與生命週期](#27-狀態保存日誌與生命週期)
  - [2.8 故障影響分析](#28-故障影響分析)
  - [2.9 本章實務案例與注意事項](#29-本章實務案例與注意事項)
- [第3章 環境需求與安裝前檢查](#第3章-環境需求與安裝前檢查)
  - [3.1 平台／必要條件／支援狀態／注意事項](#31-平台必要條件支援狀態注意事項)
  - [3.2 硬體需求](#32-硬體需求)
  - [3.3 軟體與依賴](#33-軟體與依賴)
  - [3.4 Windows、WSL 2 與 Docker Desktop](#34-windowswsl-2-與-docker-desktop)
  - [3.5 macOS 與 DGX 平台](#35-macos-與-dgx-平台)
  - [3.6 網路、DNS、Proxy、TLS 與防火牆需求](#36-網路dnsproxytls-與防火牆需求)
  - [3.7 模型推理服務、API Key 與帳號權限](#37-模型推理服務api-key-與帳號權限)
  - [3.8 企業 Proxy、內網 Git、套件倉庫與私有模型的限制](#38-企業-proxy內網-git套件倉庫與私有模型的限制)
  - [3.9 安裝前預檢腳本](#39-安裝前預檢腳本)
  - [3.10 本章實務案例與注意事項](#310-本章實務案例與注意事項)
- [第4章 安裝、初始化與首次啟動](#第4章-安裝初始化與首次啟動)
  - [4.1 安裝流程總覽](#41-安裝流程總覽)
  - [4.2 Step 1：安裝前的環境檢查](#42-step-1安裝前的環境檢查)
  - [4.3 Step 2：官方安裝方式與安全檢查](#43-step-2官方安裝方式與安全檢查)
  - [4.4 Step 3：執行安裝並確認版本](#44-step-3執行安裝並確認版本)
  - [4.5 Step 4：選擇 Agent 與引導式初始化](#45-step-4選擇-agent-與引導式初始化)
  - [4.6 Step 5：模型推理服務設定](#46-step-5模型推理服務設定)
  - [4.7 Step 6：沙盒建立與安全政策確認](#47-step-6沙盒建立與安全政策確認)
  - [4.8 Step 7：Agent 首次啟動](#48-step-7agent-首次啟動)
  - [4.9 Step 8～9：發送測試請求並驗證回應](#49-step-89發送測試請求並驗證回應)
  - [4.10 Step 10：確認檔案、網路與憑證限制有效](#410-step-10確認檔案網路與憑證限制有效)
  - [4.11 Step 11：檢查日誌與服務狀態](#411-step-11檢查日誌與服務狀態)
  - [4.12 非互動安裝（CI 與標準映像）](#412-非互動安裝ci-與標準映像)
  - [4.13 本章實務案例與注意事項](#413-本章實務案例與注意事項)
- [第5章 設定管理與 CLI 操作](#第5章-設定管理與-cli-操作)
  - [5.1 兩套 CLI 的分工](#51-兩套-cli-的分工)
  - [5.2 指令文法](#52-指令文法)
  - [5.3 命令總表](#53-命令總表)
  - [5.4 查看版本與執行狀態](#54-查看版本與執行狀態)
  - [5.5 建立、啟動、停止與連線](#55-建立啟動停止與連線)
  - [5.6 Agent 啟動、互動與任務執行](#56-agent-啟動互動與任務執行)
  - [5.7 模型 Provider 與推理服務設定](#57-模型-provider-與推理服務設定)
  - [5.8 網路政策的檢視、更新與驗證](#58-網路政策的檢視更新與驗證)
  - [5.9 沙盒狀態與日誌查詢](#59-沙盒狀態與日誌查詢)
  - [5.10 狀態保存、恢復與資源清理](#510-狀態保存恢復與資源清理)
  - [5.11 安裝更新、故障復原與解除安裝](#511-安裝更新故障復原與解除安裝)
  - [5.12 常用環境變數](#512-常用環境變數)
  - [5.13 版本差異與淘汰指令](#513-版本差異與淘汰指令)
  - [5.14 偽指令說明（概念用，不可直接執行）](#514-偽指令說明概念用不可直接執行)
  - [5.15 本章實務案例與注意事項](#515-本章實務案例與注意事項)
- [第6章 安全架構與政策管理](#第6章-安全架構與政策管理)
  - [6.1 五層防護與套用時機](#61-五層防護與套用時機)
  - [6.2 沙盒隔離與檔案系統限制](#62-沙盒隔離與檔案系統限制)
  - [6.3 網路：預設拒絕與允許清單](#63-網路預設拒絕與允許清單)
  - [6.4 程序權限與系統呼叫限制](#64-程序權限與系統呼叫限制)
  - [6.5 外部 API 與模型服務存取控制](#65-外部-api-與模型服務存取控制)
  - [6.6 API Key、Token、SSH 金鑰與其他敏感憑證管理](#66-api-keytokenssh-金鑰與其他敏感憑證管理)
  - [6.7 Prompt Injection、惡意程式碼與不可信文件](#67-prompt-injection惡意程式碼與不可信文件)
  - [6.8 透過允許的網路外洩資料](#68-透過允許的網路外洩資料)
  - [6.9 套件安裝、依賴下載與供應鏈攻擊](#69-套件安裝依賴下載與供應鏈攻擊)
  - [6.10 稽核日誌、異常監控與事件處理](#610-稽核日誌異常監控與事件處理)
  - [6.11 教學用最小權限政策範例](#611-教學用最小權限政策範例)
  - [6.12 套用與驗證政策](#612-套用與驗證政策)
  - [6.13 政策更新是增量還是整份替換](#613-政策更新是增量還是整份替換)
  - [6.14 哪些設定可執行期更新、哪些必須重建](#614-哪些設定可執行期更新哪些必須重建)
  - [6.15 不同 Agent 的政策差異](#615-不同-agent-的政策差異)
  - [6.16 審查 AI 產出的政策](#616-審查-ai-產出的政策)
  - [6.17 安全公告與弱點修補管理](#617-安全公告與弱點修補管理)
    - [6.17.1 版本下限檢查腳本](#6171-版本下限檢查腳本)
    - [6.17.2 企業的弱點管理流程（🏢）](#6172-企業的弱點管理流程)
  - [6.18 對照 OWASP Top 10 for Agentic Applications 2026](#618-對照-owasp-top-10-for-agentic-applications-2026)
  - [6.19 本章實務案例與注意事項](#619-本章實務案例與注意事項)
- [第7章 使用 NemoClaw 開發 Web Application](#第7章-使用-nemoclaw-開發-web-application)
  - [7.1 NemoClaw 在開發流程中的角色](#71-nemoclaw-在開發流程中的角色)
  - [7.2 選擇 Agent 與程式碼進出沙盒的方式](#72-選擇-agent-與程式碼進出沙盒的方式)
  - [7.3 開發沙盒的工具鏈](#73-開發沙盒的工具鏈)
  - [7.4 可重複的 AI Agent 開發流程](#74-可重複的-ai-agent-開發流程)
  - [7.5 專案慣例檔：讓 Agent 先讀規則](#75-專案慣例檔讓-agent-先讀規則)
  - [7.6 Prompt 範本與審查方法](#76-prompt-範本與審查方法)
    - [7.6.1 範本 P1：分析需求並建立 SRS](#761-範本-p1分析需求並建立-srs)
    - [7.6.2 範本 P2：產生系統架構與設計規格](#762-範本-p2產生系統架構與設計規格)
    - [7.6.3 範本 P3：REST API 規格與 OpenAPI](#763-範本-p3rest-api-規格與-openapi)
    - [7.6.4 範本 P4：依規格開發後端](#764-範本-p4依規格開發後端)
    - [7.6.5 範本 P5：依規格開發前端（Vue 3＋TypeScript＋Tailwind）](#765-範本-p5依規格開發前端vue-3typescripttailwind)
    - [7.6.6 範本 P6：產生單元測試與整合測試](#766-範本-p6產生單元測試與整合測試)
    - [7.6.7 範本 P7：檢查 Clean Architecture 依賴方向](#767-範本-p7檢查-clean-architecture-依賴方向)
    - [7.6.8 範本 P8：產生安全檢查清單](#768-範本-p8產生安全檢查清單)
    - [7.6.9 範本 P9：執行 Code Review 並修正缺陷](#769-範本-p9執行-code-review-並修正缺陷)
  - [7.7 範例專案結構與程式碼](#77-範例專案結構與程式碼)
  - [7.8 架構守門：ArchUnit 與快篩工具](#78-架構守門archunit-與快篩工具)
  - [7.9 測試策略](#79-測試策略)
  - [7.10 交付報告與誠實性檢查](#710-交付報告與誠實性檢查)
  - [7.11 程式碼品質、弱點掃描與依賴檢查](#711-程式碼品質弱點掃描與依賴檢查)
  - [7.12 建置、部署與交付文件](#712-建置部署與交付文件)
  - [7.13 本章實務案例與注意事項](#713-本章實務案例與注意事項)
- [第8章 既有系統逆向工程](#第8章-既有系統逆向工程)
  - [8.1 原則](#81-原則)
  - [8.2 環境準備：唯讀掛入原始碼、只開推理](#82-環境準備唯讀掛入原始碼只開推理)
  - [8.3 逆向工程流程](#83-逆向工程流程)
  - [8.4 步驟總表](#84-步驟總表)
  - [8.5 Prompt 範本](#85-prompt-範本)
    - [8.5.1 共用前言（每個逆向 Prompt 的開頭都貼上）](#851-共用前言每個逆向-prompt-的開頭都貼上)
    - [8.5.2 範本 R1：盤點程式碼、目錄與模組](#852-範本-r1盤點程式碼目錄與模組)
    - [8.5.3 範本 R2：前後端呼叫關係](#853-範本-r2前後端呼叫關係)
    - [8.5.4 範本 R3：追蹤 API、資料表與 Stored Procedure](#854-範本-r3追蹤-api資料表與-stored-procedure)
    - [8.5.5 範本 R4：重建商業規則與例外處理](#855-範本-r4重建商業規則與例外處理)
    - [8.5.6 範本 R5：批次作業、排程、訊息佇列與外部介接](#856-範本-r5批次作業排程訊息佇列與外部介接)
    - [8.5.7 範本 R6：重建系統架構圖與資料流圖](#857-範本-r6重建系統架構圖與資料流圖)
    - [8.5.8 範本 R7：產生 SRS、SDD、API 規格與資料字典](#858-範本-r7產生-srssddapi-規格與資料字典)
    - [8.5.9 範本 R8 與 R9：行為比對、回歸測試與差異報告](#859-範本-r8-與-r9行為比對回歸測試與差異報告)
  - [8.6 事實與推測的機械檢查](#86-事實與推測的機械檢查)
  - [8.7 大型程式碼庫與上下文窗口限制](#87-大型程式碼庫與上下文窗口限制)
  - [8.8 編碼格式與中文註解](#88-編碼格式與中文註解)
  - [8.9 敏感資料處理](#89-敏感資料處理)
  - [8.10 回歸測試與差異報告](#810-回歸測試與差異報告)
  - [8.11 本章實務案例與注意事項](#811-本章實務案例與注意事項)
- [第9章 Framework 與執行環境升級](#第9章-framework-與執行環境升級)
  - [9.1 升級範圍與官方指南](#91-升級範圍與官方指南)
  - [9.2 標準升級流程](#92-標準升級流程)
  - [9.3 各技術的升級要點](#93-各技術的升級要點)
  - [9.4 Prompt 範本](#94-prompt-範本)
    - [9.4.1 範本 U1：差異分析（只讀不改）](#941-範本-u1差異分析只讀不改)
    - [9.4.2 範本 U2：升級計畫與風險清單](#942-範本-u2升級計畫與風險清單)
    - [9.4.3 範本 U3：最小範圍修改（執行單一批次）](#943-範本-u3最小範圍修改執行單一批次)
  - [9.5 升級前後行為比對](#95-升級前後行為比對)
  - [9.6 升級報告、回復方案與驗收清單](#96-升級報告回復方案與驗收清單)
  - [9.7 本章實務案例與注意事項](#97-本章實務案例與注意事項)
- [第10章 企業 SSDLC 與 AI 協作流程](#第10章-企業-ssdlc-與-ai-協作流程)
  - [10.1 三方分工模型](#101-三方分工模型)
  - [10.2 各階段的 AI 適用範圍](#102-各階段的-ai-適用範圍)
  - [10.3 Git、分支與 Pull Request 規範（🏢）](#103-git分支與-pull-request-規範)
  - [10.4 CI/CD 中的品質與安全關卡](#104-cicd-中的品質與安全關卡)
  - [10.5 測試證據與稽核保存](#105-測試證據與稽核保存)
  - [10.6 本章實務案例與注意事項](#106-本章實務案例與注意事項)
- [第11章 系統維護、監控與故障排除](#第11章-系統維護監控與故障排除)
  - [11.1 診斷的三個起手式](#111-診斷的三個起手式)
  - [11.2 每日巡檢](#112-每日巡檢)
  - [11.3 常見問題卡](#113-常見問題卡)
    - [11.3.1 安裝失敗或版本不相容](#1131-安裝失敗或版本不相容)
    - [11.3.2 CLI 找不到或環境變數未生效](#1132-cli-找不到或環境變數未生效)
    - [11.3.3 Docker、WSL 2 或沙盒啟動失敗](#1133-dockerwsl-2-或沙盒啟動失敗)
    - [11.3.4 Gateway 連線異常](#1134-gateway-連線異常)
    - [11.3.5 Agent 無法回應](#1135-agent-無法回應)
    - [11.3.6 模型推理服務連線失敗](#1136-模型推理服務連線失敗)
    - [11.3.7 API Key 或 Provider 設定錯誤](#1137-api-key-或-provider-設定錯誤)
    - [11.3.8 網路政策阻擋必要服務](#1138-網路政策阻擋必要服務)
    - [11.3.9 檔案權限不足](#1139-檔案權限不足)
    - [11.3.10 狀態保存或恢復失敗](#11310-狀態保存或恢復失敗)
    - [11.3.11 磁碟不足、資源耗盡或效能下降](#11311-磁碟不足資源耗盡或效能下降)
    - [11.3.12 升級後服務無法啟動](#11312-升級後服務無法啟動)
  - [11.4 故障排除紀錄範本](#114-故障排除紀錄範本)
  - [11.5 本章實務案例與注意事項](#115-本章實務案例與注意事項)
- [第12章 版本升級、備份、復原與解除安裝](#第12章-版本升級備份復原與解除安裝)
  - [12.1 版本關係](#121-版本關係)
  - [12.2 升級前的版本盤點](#122-升級前的版本盤點)
  - [12.3 備份範圍](#123-備份範圍)
  - [12.4 測試環境的升級演練](#124-測試環境的升級演練)
  - [12.5 升級程序](#125-升級程序)
  - [12.6 升級失敗時的復原策略](#126-升級失敗時的復原策略)
  - [12.7 沙盒重建與狀態恢復的差異](#127-沙盒重建與狀態恢復的差異)
  - [12.8 解除安裝前的資料保留與憑證撤銷](#128-解除安裝前的資料保留與憑證撤銷)
  - [12.9 升級完成後的驗收](#129-升級完成後的驗收)
  - [12.10 升級檢查清單與維護紀錄表](#1210-升級檢查清單與維護紀錄表)
  - [12.11 下一版升級預警：OpenShell 0.1.5 遷移（`main` 未發布）](#1211-下一版升級預警openshell-015-遷移main-未發布)
  - [12.12 本章實務案例與注意事項](#1212-本章實務案例與注意事項)
- [第13章 企業導入與同仁使用規範](#第13章-企業導入與同仁使用規範)
  - [13.1 適用人員與角色權責](#131-適用人員與角色權責)
  - [13.2 開發環境申請與初始化](#132-開發環境申請與初始化)
  - [13.3 專案目錄與檔案存取規範](#133-專案目錄與檔案存取規範)
  - [13.4 網路白名單申請與審查](#134-網路白名單申請與審查)
  - [13.5 API Key 與憑證管理](#135-api-key-與憑證管理)
  - [13.6 原始碼、個資、客戶資料與機密資料處理](#136-原始碼個資客戶資料與機密資料處理)
  - [13.7 AI 產出程式碼的審查責任](#137-ai-產出程式碼的審查責任)
  - [13.8 測試與品質驗證要求](#138-測試與品質驗證要求)
  - [13.9 日誌、稽核與事件通報](#139-日誌稽核與事件通報)
  - [13.10 版本管理、更新與停用程序](#1310-版本管理更新與停用程序)
  - [13.11 允許／禁止／需經核准的行為](#1311-允許禁止需經核准的行為)
  - [13.12 技術防護、行政規範與人工審查的分層](#1312-技術防護行政規範與人工審查的分層)
  - [13.13 本章實務案例與注意事項](#1313-本章實務案例與注意事項)
- [第14章 企業共用平台建議架構](#第14章-企業共用平台建議架構)
  - [14.1 設計原則](#141-設計原則)
  - [14.2 企業部署架構圖](#142-企業部署架構圖)
  - [14.3 個人開發沙盒與共用測試環境的隔離](#143-個人開發沙盒與共用測試環境的隔離)
  - [14.4 不同專案的檔案、網路與憑證權限分離](#144-不同專案的檔案網路與憑證權限分離)
  - [14.5 私有模型服務與外部託管推理服務的選擇](#145-私有模型服務與外部託管推理服務的選擇)
  - [14.6 企業 Proxy、TLS、DNS 與防火牆整合](#146-企業-proxytlsdns-與防火牆整合)
  - [14.7 稽核、日誌保存與異常通報](#147-稽核日誌保存與異常通報)
  - [14.8 開發、測試與正式環境的權限分離](#148-開發測試與正式環境的權限分離)
  - [14.9 共用設定範本與政策版本管理](#149-共用設定範本與政策版本管理)
  - [14.10 資源成本、模型使用量與維運責任](#1410-資源成本模型使用量與維運責任)
  - [14.11 分階段導入計畫](#1411-分階段導入計畫)
  - [14.12 Alpha 階段的風險接受程序](#1412-alpha-階段的風險接受程序)
  - [14.13 本章實務案例與注意事項](#1413-本章實務案例與注意事項)
- [第15章 效益衡量與導入決策](#第15章-效益衡量與導入決策)
  - [15.1 衡量原則](#151-衡量原則)
  - [15.2 指標定義](#152-指標定義)
  - [15.3 資料收集方法](#153-資料收集方法)
  - [15.4 導入決策門檻](#154-導入決策門檻)
  - [15.5 本章實務案例與注意事項](#155-本章實務案例與注意事項)
- [第16章 實作演練與驗收](#第16章-實作演練與驗收)
  - [16.1 演練 0：安全控制驗證（必做）](#161-演練-0安全控制驗證必做)
  - [16.2 案例 A：新建 Web Application](#162-案例-a新建-web-application)
  - [16.3 案例 B：既有系統逆向工程](#163-案例-b既有系統逆向工程)
  - [16.4 案例 C：Framework 升級](#164-案例-cframework-升級)
  - [16.5 演練評分表](#165-演練評分表)
  - [16.6 本章實務案例與注意事項](#166-本章實務案例與注意事項)
- [第17章 常見問題 FAQ](#第17章-常見問題-faq)
  - [17.1 NemoClaw 是否等於 OpenShell？](#171-nemoclaw-是否等於-openshell)
  - [17.2 NemoClaw 是否會自動保證 AI 產出程式碼安全？](#172-nemoclaw-是否會自動保證-ai-產出程式碼安全)
  - [17.3 Agent 能否讀取沙盒以外的檔案？](#173-agent-能否讀取沙盒以外的檔案)
  - [17.4 如何限制 Agent 的網路連線？](#174-如何限制-agent-的網路連線)
  - [17.5 能否使用私有模型或本地模型？](#175-能否使用私有模型或本地模型)
  - [17.6 如何管理外部 API Key？](#176-如何管理外部-api-key)
  - [17.7 可以在 Windows 環境使用嗎？](#177-可以在-windows-環境使用嗎)
  - [17.8 如何切換或更新 Agent？](#178-如何切換或更新-agent)
  - [17.9 如何保留工作狀態？](#179-如何保留工作狀態)
  - [17.10 如何避免 AI 修改錯誤的程式碼？](#1710-如何避免-ai-修改錯誤的程式碼)
  - [17.11 如何確認模型或 Agent 版本相容？](#1711-如何確認模型或-agent-版本相容)
  - [17.12 Alpha 階段是否適合企業正式上線？](#1712-alpha-階段是否適合企業正式上線)
  - [17.13 `lkg` 與 latest 有什麼不同？](#1713-lkg-與-latest-有什麼不同)
  - [17.14 網路上看到的 `nemoclaw plan`／`nemoclaw apply` 是什麼？](#1714-網路上看到的-nemoclaw-plannemoclaw-apply-是什麼)
  - [17.15 可以讓 Agent 直接用我在主機上的 IDE 專案目錄嗎？](#1715-可以讓-agent-直接用我在主機上的-ide-專案目錄嗎)
  - [17.16 NemoClaw 會把我的資料送給 NVIDIA 嗎？](#1716-nemoclaw-會把我的資料送給-nvidia-嗎)
  - [17.17 NemoClaw 有已知的安全漏洞嗎？](#1717-nemoclaw-有已知的安全漏洞嗎)
  - [17.18 下一版會換成 OpenShell 0.1.5 嗎？](#1718-下一版會換成-openshell-015-嗎)
  - [17.19 `status --json` 的 `liveRoute` 是 `null`，是不是壞了？](#1719-status---json-的-liveroute-是-null是不是壞了)
- [第18章 參考資料與附錄](#第18章-參考資料與附錄)
  - [18.1 官方儲存庫](#181-官方儲存庫)
  - [18.2 官方安裝與快速入門文件](#182-官方安裝與快速入門文件)
  - [18.3 安全與政策文件](#183-安全與政策文件)
  - [18.4 Agent 官方文件](#184-agent-官方文件)
  - [18.5 模型與推理服務](#185-模型與推理服務)
  - [18.6 容器與作業系統](#186-容器與作業系統)
  - [18.7 軟體安全與 SSDLC 標準](#187-軟體安全與-ssdlc-標準)
  - [18.8 Framework 與測試工具官方指南](#188-framework-與測試工具官方指南)
  - [18.9 附錄](#189-附錄)
    - [18.9.1 附錄 1：安裝前檢查清單](#1891-附錄-1安裝前檢查清單)
    - [18.9.2 附錄 2：安裝後驗收清單](#1892-附錄-2安裝後驗收清單)
    - [18.9.3 附錄 3：沙盒安全檢查清單](#1893-附錄-3沙盒安全檢查清單)
    - [18.9.4 附錄 4：AI Agent 開發工作流程（一頁版）](#1894-附錄-4ai-agent-開發工作流程一頁版)
    - [18.9.5 附錄 5：逆向工程 Prompt 範本（一頁版）](#1895-附錄-5逆向工程-prompt-範本一頁版)
    - [18.9.6 附錄 6：Framework 升級 Prompt 範本（一頁版）](#1896-附錄-6framework-升級-prompt-範本一頁版)
    - [18.9.7 附錄 7：故障排除紀錄範本](#1897-附錄-7故障排除紀錄範本)
    - [18.9.8 附錄 8：版本升級與回復檢查清單](#1898-附錄-8版本升級與回復檢查清單)
    - [18.9.9 附錄 9：企業使用規範檢查清單](#1899-附錄-9企業使用規範檢查清單)
  - [18.10 企業自訂審查工具原始碼](#1810-企業自訂審查工具原始碼)
    - [18.10.1 nemoclaw-policy-lint.py](#18101-nemoclaw-policy-lintpy)
    - [18.10.2 check-change-report.py](#18102-check-change-reportpy)
    - [18.10.3 check-layering.py](#18103-check-layeringpy)
    - [18.10.4 check-evidence.py](#18104-check-evidencepy)
    - [18.10.5 check-test-weakening.py](#18105-check-test-weakeningpy)
  - [18.11 上游變更追蹤表（v0.0.139 → `main`＠`bafe6cc`）](#1811-上游變更追蹤表v00139--mainbafe6cc)
  - [18.12 名詞表](#1812-名詞表)
  - [18.13 版本紀錄](#1813-版本紀錄)
- [新進成員快速檢查清單（Checklist）](#新進成員快速檢查清單checklist)

## 第1章 NemoClaw 概論

本章回答四個問題：NemoClaw 是什麼、它和 OpenShell／Agent／模型是什麼關係、它能替企業解決什麼、以及它**還不能**做什麼。讀完本章，你應該能用三句話向主管說明 NemoClaw 的定位，並判斷你的情境適不適合導入。

### 1.1 設計目的與核心價值

官方 README 的定義是：*an open source reference stack for running supported AI agents more safely inside NVIDIA OpenShell sandboxes*（在 OpenShell 沙盒中更安全地執行受支援 AI Agent 的開源參考堆疊）。拆開來看，有三個關鍵字：

| 關鍵字 | 意思 | 對企業的意義 |
|---|---|---|
| reference stack（參考堆疊） | NVIDIA 把「哪個映像檔、哪些預設政策、怎麼接推理服務、怎麼升級」整理成一套可重複的組合 | 不用每個團隊自己拼 Docker、政策 YAML、憑證注入；但也代表你接受它的預設設計 |
| supported agents（受支援的 Agent） | 只有 OpenClaw、Hermes、LangChain Deep Agents Code 有整合層 | Claude Code、Codex、Copilot CLI 等不在 NemoClaw 的支援清單內（OpenShell 本身可以跑，但那是「OpenShell 路徑」，見 1.8） |
| more safely（更安全地） | 相對於「直接在主機跑 Agent」更安全，不是「保證安全」 | 仍需企業的行政規範、人工審查與 CI 驗證 |

NemoClaw 提供的能力，官方歸納為六類：

| 能力 | 具體內容 | 狀態 |
|---|---|---|
| 執行受支援的 Agent | 依 Agent 建立專屬的沙盒映像檔與設定 | Tested |
| 推理路由 | 把模型呼叫交給 OpenShell 管理的路由，憑證留在沙盒外 | Tested |
| 沙盒存取控制 | 透過 OpenShell 套用網路、檔案系統、程序與推理政策 | Sandboxed execution 為 *Tested with limitations* |
| 生命週期 | 主機就緒檢查、建立／更新、狀態與日誌、保留原生 home 的重建與復原 | Tested |
| 託管 MCP | 以 HTTPS Streamable HTTP 連接需驗證的 MCP Server，憑證由 OpenShell 在出口替換 | Tested |
| Agent Skills 與文件 | 提供給 Coding Agent 讀的 Markdown 文件與 skill（`.agents/skills/`） | Tested |

**來源**：[NemoClaw README](https://github.com/NVIDIA/NemoClaw)、[Overview](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/about/overview)、[Platform Support — Capabilities](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/platform-support)

### 1.2 NemoClaw、OpenShell、Agent、LLM、推理服務與工具的關係

很多導入失敗，來自把這幾層混為一談。下表用「誰負責什麼」來區分：

| 層 | 代表元件 | 負責 | 不負責 |
|---|---|---|---|
| 操作者 | 你（開發者／維運） | 選 Agent、選模型、核准網路請求、放寬政策、輪替憑證 | — |
| 參考堆疊 | **NemoClaw** 主機 CLI、Blueprint、整合層、preset | 安裝、onboarding、驗證 Provider、記錄狀態、重建與升級流程 | 隔離本身、政策執行、模型推理 |
| 執行環境 | **OpenShell** Gateway、沙盒、L7 代理 | 網路命名空間隔離、CONNECT 代理、政策執行、TLS 終結、憑證替換、推理路由 | 判斷 Agent 行為是否合理 |
| Agent | OpenClaw、Hermes、Deep Agents Code（`dcode`） | Agent 迴圈、工具呼叫、skill、記憶、沙盒內設定 | 定義沙盒或 Gateway |
| 模型 | Nemotron、GPT、Claude、Gemini、Qwen 等 LLM | 依提示產生文字與工具呼叫 | 遵守企業規範（它只會「傾向」遵守） |
| 推理服務 | NVIDIA Endpoints、OpenAI、Anthropic、OpenRouter、Ollama、vLLM、NIM | 執行模型、計費、限流、資料處理政策 | 沙盒內的任何控制 |
| 工具 | Git、Maven、npm、MCP Server、瀏覽器、Shell | 實際讀寫檔案、連網、建置 | 判斷操作是否被授權（由 OpenShell 政策決定） |

```mermaid
flowchart TB
    OP["操作者<br/>選擇與核准"]
    NC["NemoClaw<br/>主機 CLI、Blueprint、preset"]
    OS["OpenShell 0.0.116<br/>Gateway、L7 代理、政策、憑證"]
    SB["沙盒<br/>Agent 與工具"]
    INF["推理服務<br/>NVIDIA、OpenAI、本地 vLLM 等"]
    EXT["外部服務<br/>Git、套件庫、MCP"]
    OP -->|"onboard、policy、rebuild"| NC
    NC -->|"呼叫 API 與 CLI"| OS
    OS -->|"建立並隔離"| SB
    SB -->|"所有請求"| OS
    OS -->|"核准的推理請求<br/>出口替換憑證"| INF
    OS -->|"核准的端點"| EXT
    OP -.->|"openshell term 核准或拒絕"| OS
```

> 📌 **註記**：官方 Ecosystem 頁的說法是「NemoClaw sits above OpenShell in the operator workflow」——NemoClaw 在操作流程上位於 OpenShell 之上，呼叫 OpenShell 的 API 與 CLI 來建立和設定沙盒。模型與端點則位於 OpenShell 的推理路由之後。

### 1.3 為什麼自主 Agent 需要檔案、網路、程序與憑證限制

官方 Overview 的原文是：自主 Agent 可以發出任意網路請求、存取主機檔案系統、呼叫任何推理端點；沒有控制時，風險會隨 Agent 無人看管的時間而累積。換成企業語言，四類限制各自防的是：

| 限制 | 沒有限制時的典型事故 | NemoClaw／OpenShell 的對應控制 |
|---|---|---|
| 檔案 | Agent 讀到 `~/.ssh/`、`~/.aws/`、其他專案原始碼；誤刪主機檔案 | 沙盒只看得到自己的 `/sandbox`；系統路徑唯讀；Landlock 核心層限制（核心 5.13 以上） |
| 網路 | 被 Prompt Injection 誘導，把程式碼 POST 到攻擊者網站；下載惡意套件 | Deny-by-default 出口、依程式身分（binary）放行主機／方法／路徑；未知請求需操作者核准 |
| 程序 | 以 root 提權、利用 setuid、fork bomb 拖垮主機 | 非 root `sandbox` 使用者、`no-new-privileges`、seccomp、`ulimit -u 512`（best effort） |
| 憑證 | API Key 被寫進對話、記憶檔或 commit；被外洩後持續盜用 | 推理與 MCP 憑證存在 OpenShell Gateway，沙盒內只有 placeholder，於核准端點出口才替換 |

> ⚠️ **警告**：這四類控制都**不**處理「Agent 產出的內容」。Agent 在 `/sandbox` 內寫出含有後門的程式碼、或在已核准的 `github.com` 上開一個公開 repo 推送程式碼，這些都在沙盒的允許範圍內。內容層的風險要靠第 10、13 章的人工審查與 CI 驗證。

### 1.4 NemoClaw 與直接在主機執行 Agent 的差異

| 比較面向 | 直接在主機執行 Agent | 使用 NemoClaw / OpenShell |
|---|---|---|
| 執行環境 | 以開發者帳號直接執行，與 IDE、瀏覽器、其他專案共用同一個作業系統環境 | 每個 Agent 在獨立的 OpenShell 沙盒（容器）中，以 `sandbox` 使用者執行；映像檔以 `@sha256` digest 固定，移除了 `gcc`、`make`、`netcat` 等工具 |
| 檔案存取 | 看得到開發者能看的所有檔案（家目錄、憑證檔、其他 repo）；只能靠 Agent 自身的權限設定或提示自律 | 只能寫 `/sandbox`、`/tmp` 等少數路徑；`/usr`、`/etc` 等唯讀；Landlock 在核心層執行（OpenClaw 為 `best_effort`，Deep Agents 為 `strict`）；主機目錄只能以 `--host-mount` **唯讀**掛入 |
| 網路存取 | 繼承主機所有網路能力；企業通常只能靠 Proxy 或防火牆做粗粒度控制 | Deny-by-default；政策以「主機＋連接埠＋HTTP 方法＋路徑＋發起程式」放行；未列出的請求被攔截並出現在 `openshell term` 等候核准；另有 SSRF 防護封鎖迴環、link-local、雲端 metadata |
| 憑證管理 | API Key 放在環境變數或設定檔，Agent 可直接讀取、可能寫入記錄或 commit | 推理、MCP、Web Search、訊息通道憑證存於 OpenShell Gateway；沙盒內只看到 placeholder；NemoClaw 會從建立沙盒的指令中過濾敏感環境變數 |
| 模型推理 | Agent 直接呼叫任意模型端點，誰的 Key、哪個端點、花多少錢都在 Agent 手上 | 由 onboarding 驗證 Provider 與模型後建立受控路由；附掛式 Provider 只允許特定主機、路徑與程式（例如 NVIDIA Endpoints 只允許 `GET /v1/models`、`POST /v1/chat/completions`） |
| 狀態管理 | 對話、記憶、設定散落在家目錄，升級 Agent 時可能遺失或互相污染 | Agent 原生 home／workspace 由 OpenShell 保存；重建（`rebuild`）時 NemoClaw 會封存、完整性檢查並還原整棵樹；憑證不在封存範圍內 |
| 維運與稽核 | 幾乎沒有統一的狀態、日誌與健康檢查；事後很難重建「Agent 做過什麼」 | `host probe`、`status`、`logs`、`doctor`、`debug` 提供一致的檢查入口；`openshell term` 顯示即時網路活動；但**沒有**集中式 SIEM 匯出與多主機管理（官方列為手動或規劃中） |

> 📌 **註記**：表中「使用 NemoClaw / OpenShell」欄的每一項，都依賴主機是否支援對應機制。例如 macOS 的 Docker VM 核心若不支援 Landlock，檔案系統限制會**靜默降級**為只靠容器掛載（官方 Troubleshooting「Landlock filesystem restrictions silently degraded」）。不要把這張表當成所有平台都成立的保證。

### 1.5 優點、限制、導入成本與適用邊界

**優點**：

- **少寫整合**：一條 `nemoclaw onboard` 就完成 Gateway、Provider、映像檔、政策與沙盒；不需要自己維護 OpenShell 政策檔與憑證注入。
- **預設就比自己拼的嚴格**：Blueprint 在 OpenShell community 沙盒之上再收斂政策、移除工具鏈、固定映像檔 digest、過濾敏感環境變數。
- **生命週期有交易保護**：重建前先封存並驗證原生 home，失敗可續作（`--resume`）。
- **政策可審查**：preset 是 YAML、可版本控管、套用前會預覽將開放的端點。

**限制**（官方明列，非本手冊推測）：

| 限制 | 官方狀態 | 影響 |
|---|---|---|
| 單一主機、單一受信任操作者 | Product Scope | 不能當成多人共用的平台；多使用者主機被視為風險 |
| 無操作者 RBAC | Out of scope | 誰能在主機上執行 `nemoclaw`，誰就能改政策、看日誌 |
| 無 SSO／OIDC／SAML | Roadmap-only | Dashboard 與 Agent Gateway 用裝置配對或 bearer token |
| 無多租戶隔離 | Out of scope | 不同客戶、不同敏感等級的專案不應共用同一台主機 |
| 無集中稽核與 SIEM 匯出 | Manual or admin-only | 需自行匯出 OpenClaw session JSONL 或 Hermes state |
| 無成本控管 | Platform or partner-owned | 預算與限流要在推理服務端設定 |
| 不支援離線安裝 | Unsupported | onboarding 需要連外下載套件、映像檔與驗證 Provider |
| 只支援 Ubuntu／Debian 系 Linux | Unsupported（其他發行版） | 安裝程式假設 `apt-get`；RHEL 系、Fedora 未驗證 |
| 不支援原生 Kubernetes／OpenShift | Unsupported | 沙盒以 Docker 容器執行，不是 K8s Pod |

**導入成本**（🏢 本手冊估計的面向，不是官方數據）：

| 成本項目 | 說明 |
|---|---|
| 主機資源 | 每台至少 4 vCPU／8 GB RAM／20 GB 磁碟（建議 16 GB／40 GB）；本地模型另計 GPU 與記憶體 |
| 推理費用 | 雲端推理依 token 計費，無人看管的 Agent 會持續累積（官方 Provider Trust Tiers 也提醒此風險） |
| 網路治理 | 每個新端點都要走白名單申請與審查（第 13.4 節） |
| 版本追蹤 | 官方約每週發布，且 OpenShell 版本被 NemoClaw 釘住；需要專人追蹤 release notes |
| 教育訓練 | 同仁要學會 sandbox-first CLI、政策審查、`openshell term` 核准流程 |

### 1.6 Alpha 階段對企業導入、相容性與維運的影響

| 面向 | Alpha 代表什麼 | 企業因應（🏢） |
|---|---|---|
| 介面穩定性 | 官方 Enterprise Readiness：*interfaces can change between releases*；例如 `nemoclaw setup`、`setup-spark`、全域 `start`／`stop` 已標示淘汰 | 把 NemoClaw 版本固定在已驗證的 tag；升級前在測試主機演練（第 12 章） |
| 版本相容性 | 每個 NemoClaw 版本只接受特定 OpenShell 版本範圍（v0.0.139 是 0.0.116～0.0.116） | 禁止單獨升級 OpenShell；以 NemoClaw 安裝程式整組升級 |
| 支援 | best effort、無回應時限、無 SLA | 內部指定窗口；問題先查官方 Troubleshooting 與 GitHub Issues |
| 功能成熟度 | 同一功能在不同 Agent／平台成熟度不同（Tested／Tested with limitations／Experimental／Deferred） | 對外或對主管描述能力時，引用平台矩陣的原文狀態，*Tested with limitations* 不等於 *Tested* |
| 資料安全 | DGX Spark Playbook 明言「只在乾淨環境執行，不放個資、機密或敏感憑證」 | 只用合成資料與非正式專案試行（第 14、16 章） |

### 1.7 兩條產品線：v0.0.x（現行）與 v1（開發中）

研究時 NemoClaw 儲存庫同時存在兩條互不相干的程式線（`git` 比對顯示兩者沒有共同祖先）：

| 項目 | v0.0.x 線（本手冊主體） | v1 線（預覽） |
|---|---|---|
| 分支／標籤 | `main`；正式標籤 `v0.0.120`～`v0.0.139` | `v1` 分支；標籤 `v0.1.0-rc1`～`rc9`、`v1.0.0-rc1` |
| 實作 | TypeScript／Node.js CLI | Rust CLI 與 Rust SDK，內嵌 OpenTofu |
| 操作模型 | 互動式 onboarding 精靈＋sandbox-first 指令 | 宣告式 desired-state YAML：`plan`、`apply`、`export`、`destroy` |
| 搭配 OpenShell | 0.0.116 | `versions.json` 記錄 0.1.4 |
| 官方定位 | 文件站 latest、安裝程式預設 | README：「This branch documents v1 development using source-built bundles」；`docs/overview.md`：「v1 has no support policy or enterprise deployment qualification yet」 |
| 銜接 | `nemoclaw config export <沙盒>` 可把現有沙盒匯出成 `nemoclaw.nvidia.com/v1alpha1` 的 `NemoClawConfig` YAML（不含憑證值） | 讀取上述 YAML |

> ⚠️ **警告**：網路上看到 `nemoclaw plan`、`nemoclaw apply` 或 `v1.0.0-rc1` 的教學，屬於 v1 預覽線，指令與本手冊的 v0.0.x 不相容。v1 的 CLI 沒有 Agent 呼叫、訊息通道管理與快照指令（v1 `docs/overview.md`）。本手冊不教 v1 操作，只在第 12 章說明如何為未來遷移保留設定。

v1 線仍在密集開發：研究當日 `v1` 分支（`c2a71f8`）還有新提交，內容包括 Kubernetes／OpenShift 部署指南的補充，以及 Rust 依賴的安全修補。開發活躍不代表可以上線，官方定位仍是「沒有支援政策」。

自己確認 v1 的狀態（🖥️ Host，唯讀；✅ 研究日實際執行）：

```bash
# v1 分支最新提交與預覽標籤
git ls-remote https://github.com/NVIDIA/NemoClaw.git refs/heads/v1 'refs/tags/v1*'
# 官方定位是否仍是「沒有支援政策」
curl -fsSL https://raw.githubusercontent.com/NVIDIA/NemoClaw/v1/docs/overview.md \
  | grep -io "v1 has no support policy[^.]*"
```

| 輸出 | 判讀 |
|---|---|
| `grep` 印出 `v1 has no support policy or enterprise deployment qualification yet` | 仍是預覽，企業不導入 |
| `grep` 沒有輸出 | 官方用語變了：讀新版 `overview.md`，再重新評估是否值得試行 |
| 出現 `refs/tags/v1.0.0`（沒有 `-rc`） | 第一個正式標籤出現，平台管理者應排入評估 |

### 1.8 適合與不適合使用的情境

**適合**：

| 情境 | 理由 |
|---|---|
| 在隔離的開發主機評估 AI Agent 能力 | 官方 Use Case「Controlled agent evaluation」：先用明確的檔案與網路邊界測試 Agent 行為 |
| 讓 Coding Agent（Deep Agents Code）在受控環境閱讀與修改**非正式**專案 | 程式碼與憑證被隔離，網路只開必要端點 |
| 逆向工程舊系統（原始碼唯讀掛入） | `--host-mount` 只提供唯讀，Agent 無法改到原始檔 |
| 需要託管 MCP、但不想把 Token 放進 Agent 設定 | 託管 MCP 只存憑證名稱，值由 OpenShell 在出口替換 |
| 在遠端 Linux 主機以 SSH 操作的無頭伺服器 | 官方 *Headless Linux server* 路徑（Tested with limitations） |

**不適合**：

| 情境 | 理由 | 替代方案（🏢） |
|---|---|---|
| 正式環境、處理真實客戶資料的工作負載 | alpha、無 SLA、無 RBAC／SSO／多租戶 | 等待正式版與企業驗證；先在非正式環境累積證據 |
| 多位同仁共用一台主機 | 官方不支援多使用者主機共用 | 一人一台（或一人一個 VM） |
| 需要 Claude Code、Codex、Copilot CLI 等 Agent | NemoClaw 只整合三個 Agent | 改走「OpenShell 路徑」，參考同目錄《OpenShell 教學手冊》 |
| 完全離線的機房 | 官方不支援 air-gapped | 改用內部私有模型＋其他隔離方案 |
| RHEL、Rocky、Fedora 主機 | 安裝程式假設 `apt-get` | 使用 Ubuntu 24.04 VM |
| K8s／OpenShift 叢集內統一部署 | 官方不支援 | 評估 OpenShell 的 K8s 部署（需自行整合） |

### 1.9 與《OpenShell 教學手冊》的分工與版本差異

同目錄的《OpenShell 教學手冊》以 **OpenShell v0.1.5** 為基準，講的是「自己用 OpenShell 跑任何 Agent」的路徑。本手冊講的是「用 NemoClaw 跑三個受支援 Agent」的路徑，搭配 **OpenShell 0.0.116**。兩者的差異會直接影響指令能不能用：

| 主題 | OpenShell v0.1.5（OpenShell 手冊） | NemoClaw v0.0.139 環境（OpenShell 0.0.116） |
|---|---|---|
| `inference.local` | 0.1.0 起移除 | 仍存在，部分推理選項使用共享路由 `inference.local`（2.6） |
| 建立沙盒 | `openshell sandbox create` | 一律用 `nemoclaw onboard`；直接用 OpenShell 建立的沙盒不受 NemoClaw 管理 |
| 升級 OpenShell | 依 OpenShell 發行說明 | ⛔ 不可單獨升級；超出 `max_openshell_version` 時 onboarding 直接失敗 |
| 政策檔 | 直接編輯並 `openshell policy set` | 優先用 `nemoclaw <名稱> policy add`（preset）；`openshell policy set` 只在 preset 無法表達時使用，而且是整份替換（6.13） |
| 網路核准 | `openshell term` | 相同，`openshell term` 仍是核准介面 |

> ✅ **建議**：讀 OpenShell 手冊是為了理解底層原理（Landlock、L7 代理、Provider）；在 NemoClaw 主機上**操作**時，以本手冊與 NemoClaw 官方文件為準。遇到兩本手冊說法不同時，以 NemoClaw v0.0.139 文件與 OpenShell 0.0.116 行為為準。

> 📌 **註記**：如果 NemoClaw 改綁 OpenShell 0.1.5（PR #12603），上表兩欄的差距會變小，但「從 0.0.116 遷移到 0.1.5」本身就是高風險變更。新版發布後，先讀 12.11 的影響分析，再決定什麼時候換。

### 1.10 本章實務案例與注意事項

**案例**：主管問「我們可以讓全部門用 NemoClaw 寫正式系統嗎？」

建議回答（三句話）：

1. NemoClaw 是 NVIDIA 的 alpha 參考堆疊，能把 AI Agent 關在 OpenShell 沙盒裡，限制它碰得到的檔案、網路與憑證，但它不審查 Agent 寫出來的程式碼。
2. 官方定位是「單一主機、單一受信任操作者」，沒有 RBAC、SSO、多租戶與 SLA，所以現階段只適合隔離的非正式環境試行。
3. 建議依第 14 章五階段計畫，先由 2～3 位資深同仁在獨立主機以合成資料驗證，用第 15 章的指標決定是否擴大。

**注意事項**：

- 描述 NemoClaw 能力時，引用官方平台矩陣的狀態字樣（Tested／Tested with limitations／Experimental），不要自行升級成「已支援」。
- NemoClaw 版本、`lkg` 標籤、OpenShell 釘選版本會變動；每次引用前先核對第 12.2 節的版本盤點結果。
- 「沙盒安全」是相對的：它降低誤操作與被誘導的爆炸半徑，不消除風險。

## 第2章 系統架構與元件關係

本章把 NemoClaw 主機上實際跑起來的東西逐一拆開：誰是控制面、誰是資料面、信任邊界畫在哪裡、哪個元件壞了會影響什麼。官方架構頁有一句話最能說明分工：*OpenShell … has no opinions about what runs inside. NemoClaw is an opinionated reference stack built on OpenShell*（OpenShell 不管沙盒裡跑什麼；NemoClaw 是建在 OpenShell 上、帶有明確主張的參考堆疊）。

### 2.1 元件總覽

| # | 元件 | 所屬 | 執行位置 | 責任 |
|---|---|---|---|---|
| 1 | 開發人員工作站 | 企業 | 筆電／桌機（可能是 Windows） | 撰寫需求、審查產出、透過 SSH 或 WSL 操作 NemoClaw 主機 |
| 2 | NemoClaw 主機 CLI | NemoClaw | 🖥️ Host（Node.js 程式，`bin/nemoclaw.js`） | onboarding 精靈、Provider 驗證、Blueprint 解析、記錄狀態、呼叫 `openshell` |
| 3 | Blueprint 與 runner | NemoClaw | 🖥️ Host（`nemoclaw-blueprint/`） | 定義映像檔 digest、政策、推理 profile；runner 依 resolve → verify → plan → apply 執行 |
| 4 | OpenShell Gateway | OpenShell | 🖥️ Host 程序（預設連接埠 8080；Linux 以 `systemctl --user` 的 `openshell-gateway` 服務管理） | 憑證儲存、推理代理、政策引擎、裝置驗證、沙盒生命週期 |
| 5 | `openshell` CLI 與 TUI | OpenShell | 🖥️ Host | 低階操作；`openshell term` 是網路請求的核准介面 |
| 6 | 沙盒容器 | OpenShell | Docker daemon（或合格的 rootless Podman） | Landlock＋seccomp＋網路命名空間；以 `sandbox` 使用者執行 Agent |
| 7 | Agent Runtime | Agent 上游 | 📦 Sandbox | OpenClaw／Hermes／`dcode` 的迴圈、工具、記憶 |
| 8 | NemoClaw 整合層 | NemoClaw | 📦 Sandbox | OpenClaw：TypeScript plugin 與 `/nemoclaw` 指令；Hermes：`/sandbox/.hermes/config.yaml`；Deep Agents：`/sandbox/.deepagents/config.toml` 與 `.mcp.json` |
| 9 | 推理服務 | 供應商／自建 | 雲端或本機（Ollama、vLLM、NIM、llama.cpp） | 模型推理、計費、限流 |
| 10 | 外部整合 | 第三方／內部 | 網際網路或內網 | Git、套件庫、MCP Server、訊息平台 |
| 11 | 主機端狀態 | NemoClaw | 🖥️ Host `~/.nemoclaw/`、`~/.local/state/` | 沙盒登錄（`sandboxes.json`）、onboarding 進度、重建備份；**不含**憑證值 |

### 2.2 圖一：系統元件與資料流架構圖

```mermaid
flowchart LR
    DEV["開發人員工作站<br/>IDE、瀏覽器、SSH"]
    subgraph HOST["NemoClaw 主機（Ubuntu 24.04／WSL 2／macOS Apple Silicon）"]
        direction TB
        subgraph NCL["NemoClaw（參考堆疊）"]
            CLI["nemoclaw CLI<br/>onboard、status、policy、rebuild"]
            BP["Blueprint<br/>映像檔 digest、政策、preset"]
            ST["主機狀態<br/>~/.nemoclaw/ 登錄與備份"]
        end
        subgraph OSL["OpenShell 0.0.116（執行環境）"]
            GW["Gateway<br/>憑證庫、政策引擎、推理代理"]
            TERM["openshell term<br/>核准介面"]
            subgraph SBX["沙盒容器"]
                AG["Agent Runtime<br/>OpenClaw／Hermes／dcode"]
                INT["NemoClaw 整合層"]
                WS["/sandbox 工作區"]
            end
        end
    end
    NATIVE["附掛式原生 Provider<br/>NVIDIA、OpenAI、Anthropic 等"]
    SHARED["共享路由 inference.local<br/>本地 NIM、未附掛的相容端點"]
    EXT["核准的外部端點<br/>內部 Git、Nexus、MCP"]
    DEV -->|"SSH 或 WSL 終端機"| CLI
    DEV -->|"SSH 轉埠看 Dashboard"| AG
    CLI -->|"呼叫 openshell"| GW
    BP -->|"定義沙盒與政策"| SBX
    CLI -->|"記錄狀態"| ST
    GW -->|"建立與控制"| SBX
    AG -->|"placeholder 憑證<br/>受限路徑"| NATIVE
    AG -->|"inference.local"| GW
    GW -->|"注入憑證"| SHARED
    AG -.->|"經 L7 代理<br/>依政策放行"| EXT
    TERM -.->|"核准或拒絕"| GW
```

**資料流向**：Agent 的所有出站請求都經過 OpenShell 的代理與政策引擎；原生 Provider 路徑由沙盒附掛的 Provider 在出口改寫 placeholder；共享路由路徑由 Gateway 注入憑證。

**控制流向**：操作者 → `nemoclaw` CLI → `openshell` CLI／API → Gateway → 沙盒。Agent 本身**不能**反向修改政策或憑證。

### 2.3 圖二：Agent 執行任務時的請求流程

以「開發者請 Deep Agents Code 依規格新增一支 API，Agent 需要讀程式碼、呼叫模型、從內部 Nexus 下載依賴」為例：

```mermaid
sequenceDiagram
    autonumber
    actor Dev as 開發者
    participant CLI as nemo-deepagents CLI
    participant GW as OpenShell Gateway
    participant AG as dcode（沙盒內）
    participant LLM as 推理服務
    participant NX as 內部 Nexus
    participant UK as 未核准主機
    Dev->>CLI: nemo-deepagents launch dev-order
    CLI->>GW: 檢查就緒、修復轉埠
    CLI->>AG: 啟動 dcode TUI
    Dev->>AG: 輸入任務 Prompt
    AG->>AG: 讀 /sandbox/work 內的規格與程式碼
    AG->>LLM: 推理請求（placeholder 憑證）
    Note over AG,LLM: 經 OpenShell 代理；出口替換為真實憑證
    LLM-->>AG: 回應與工具呼叫建議
    AG->>Dev: 要求核准 shell 指令（互動模式）
    Dev-->>AG: 核准 mvn -q test
    AG->>NX: GET /repository/maven-public/...
    Note over AG,NX: 符合 corp-maven-readonly preset，放行
    AG->>UK: POST https://paste.example.net
    GW-->>AG: CONNECT 403（拒絕）
    GW->>Dev: openshell term 顯示待核准請求
    Dev-->>GW: 按 x 拒絕
    AG-->>Dev: 回報修改清單與測試結果
```

> 📌 **註記**：步驟 7 的「要求核准 shell 指令」是 Deep Agents Code 互動模式的預設行為（human-in-the-loop）。無頭模式 `dcode -n` 會**自動核准非 shell 工具**（包含檔案寫入與編輯），但同時停用 shell 執行（官方 Run Deep Agents Code 頁）。這個差異會影響第 7 章的工作流程設計。

### 2.4 責任邊界與信任邊界

官方 Trusted Computing Base 頁把元件分成「受信任」與「不受信任」兩群：

| 受信任（TCB 內） | 不受信任 |
|---|---|
| 操作者 | Agent 程序 |
| NemoClaw 主機 CLI | Agent 可寫入的設定與狀態 |
| OpenShell 控制面 | 可變的環境變數 |
| 容器 Runtime | 沙盒使用者寫出的狀態檔 |
| 不可變的映像檔內容 | 網路回應（包含模型回應、網頁、套件） |

```mermaid
flowchart TB
    subgraph T1["信任區：主機與控制面"]
        OPR["操作者帳號"]
        NCLI["nemoclaw CLI"]
        OSGW["OpenShell Gateway<br/>憑證庫"]
        RT["Docker／Podman"]
    end
    subgraph T2["受限區：沙盒"]
        AGT["Agent 程序"]
        CFG["Agent 可寫設定<br/>openclaw.json、config.toml"]
        WSP["/sandbox 工作區"]
    end
    subgraph T3["外部：不受信任輸入"]
        MDL["模型回應"]
        WEB["網頁、文件、套件"]
        REPO["待分析的原始碼"]
    end
    OPR --> NCLI --> OSGW --> RT --> AGT
    AGT --> CFG
    AGT --> WSP
    MDL --> AGT
    WEB --> AGT
    REPO --> WSP
```

**三個常被忽略的邊界事實**：

1. **同一個 UID**：在 OpenShell 管理的拓撲中，沙盒內的 supervisor、Agent Gateway 與 Agent 都以同一個 `sandbox` UID 執行。官方說明：OpenShell 隔離了沙盒，但同 UID 的惡意 Agent 可以對同伴程序送信號或冒充；NemoClaw 的健康檢查證明的是「服務可用」，不是「程序來源」。
2. **繞過受管入口就沒有保護**：官方 Known Limitations：若 Agent Runtime 不是從 NemoClaw 管理的 Gateway 路徑啟動，網路政策與推理驗證**不會**生效。不要用 `docker exec` 或自己啟動的容器跑 Agent。
3. **Agent 設定不保證不可變**：官方 TCB 頁明言 NemoClaw 不提供「佈建後的設定與狀態不可變」。Agent 可以改自己的 `openclaw.json`，但這些設定**無法**放寬 OpenShell 網路政策或建立憑證綁定。

### 2.5 Blueprint：版本化的沙盒定義

Blueprint 是 `nemoclaw-blueprint/` 下的一組 YAML，v0.0.139 的 `blueprint.yaml` 重點如下（📖 摘自原始碼）：

```yaml
version: "0.1.0"
# Requires OpenShell MCP/JSON-RPC L7 policy support from NVIDIA/OpenShell#1865.
min_openshell_version: "0.0.116"
max_openshell_version: "0.0.116"
min_openclaw_version: "2026.3.11"
digest: "sha256:b3d832b5...a3a9a"
profiles: [default, ncp, nim-local, vllm, routed]
components:
  sandbox:
    image: "ghcr.io/nvidia/openshell-community/sandboxes/openclaw@sha256:b3d832b5...a3a9a"
    forward_ports: [18789]
  inference:
    profiles:
      default:
        provider_type: "nvidia"
        endpoint: "https://integrate.api.nvidia.com/v1"
        model: "nvidia/nemotron-3-super-120b-a12b"
  policy:
    base: "sandboxes/openclaw/policy.yaml"
```

Runner 的生命週期是：

```mermaid
flowchart LR
    R["resolve<br/>找到 Blueprint、檢查版本範圍"] --> V["verify<br/>比對 digest"]
    V --> P["plan<br/>決定要建立或更新的資源"]
    P --> A["apply<br/>呼叫 openshell CLI"]
    A --> S["status<br/>回報結果"]
```

> 📌 **註記**：`digest` 欄位與映像檔的 `@sha256` 必須同時更新（原始碼註解引用 issue #1438）。這讓「registry 被竄改或有人誤推 `:latest`」無法悄悄換掉沙盒映像檔。企業若自建映像檔（`--from <Dockerfile>`），這層保護就要由企業自己的映像檔簽章與掃描補上（6.9）。

### 2.6 推理路由：附掛式 Provider 與共享路由

NemoClaw v0.0.139 有兩條推理路徑，取決於你選的 Provider（📖 Architecture、About Inference Routing）：

| 路徑 | 適用 | 資料流 | 憑證 |
|---|---|---|---|
| 附掛式原生 Provider（sandbox-attached） | NVIDIA Endpoints、OpenAI、Anthropic、Google Gemini、OpenRouter、Hermes Provider；Personal 層以外新建的託管相容端點；合格的新本地 Ollama／vLLM／llama.cpp | Agent → 供應商原生主機名（例如 `integrate.api.nvidia.com`）→ 經 OpenShell 附掛政策限制主機、路徑、方法與程式 | 沙盒內是 placeholder，出口改寫 |
| 共享路由 `inference.local` | 自有的本地 NVIDIA NIM、沒有附掛的相容端點、Model Router、保留的共享選擇、Personal 層新建的託管相容端點 | Agent → `inference.local` → OpenShell Gateway → Provider 端點 | Gateway 在 L7 代理注入 |
| Bedrock | 透過「Other Anthropic-compatible endpoint」輸入 Bedrock Runtime URL | 主機本地 adapter | AWS 憑證留在主機 adapter |

以 NVIDIA Endpoints 為例，附掛的 `nemoclaw-nvidia-prod-v1` Provider 只允許 `GET /v1/models` 與 `POST /v1/chat/completions`（**不**允許 embeddings），而且只限列出的 Agent 程式。

> ⚠️ **警告**：舊版沙盒（例如較早建立、沒有附掛 Provider 的 OpenClaw Ollama 沙盒）可以繼續切換模型，但**不能** `--resume` 或 `rebuild`；官方要求先備份，再以 `--fresh --name <名稱> --recreate-sandbox` 重新 onboarding。升級前要先確認每個沙盒走哪條路（12.2）。

### 2.7 狀態保存、日誌與生命週期

| 操作 | 結果 | 會不會動到 Agent 原生 home |
|---|---|---|
| Inspect：`host probe`、`status`、`logs` | 只讀 | 不會 |
| Configure：`inference set`、`policy add`、`mcp add` | 更新對應資源 | 不會（但部分變更觸發重建，見 6.14） |
| Stop／Start | 停止／啟動同一個沙盒 | 不會，狀態留在 OpenShell 儲存 |
| Recover | 修復停止或降級的 Agent 與轉埠 | 不會 |
| Rebuild | 封存整棵原生 home／workspace → 刪除舊沙盒 → 以新映像檔重建 → 還原 | 會搬移，但內容保留；憑證不在封存內 |
| Destroy | 刪除沙盒與其持久化狀態 | **會刪除**，無法復原 |
| Uninstall | 移除主機安裝；預設保留 `rebuild-backups/`、`backups/`、`sandboxes.json` | 依旗標而定 |

日誌與監控入口：

| 需求 | 指令 | 位置 |
|---|---|---|
| 沙盒生命週期與 Gateway 輸出 | `nemoclaw <名稱> logs [--follow]` | 🖥️ Host |
| 即時網路活動與核准 | `openshell term` | 🖥️ Host |
| 單一沙盒健康檢查 | `nemoclaw <名稱> doctor` | 🖥️ Host |
| 問題回報用的診斷包 | `nemoclaw debug --sandbox <名稱> --output <檔案>` | 🖥️ Host |
| OpenClaw 對話紀錄 | `nemoclaw <名稱> sessions export` | 🖥️ Host（匯出到主機） |

### 2.8 故障影響分析

| 故障元件 | 症狀 | 影響範圍 | 資料風險 | 第一步 |
|---|---|---|---|---|
| Docker daemon | `docker info` 失敗；所有沙盒不可用 | 主機上全部沙盒 | 低（狀態在 volume） | 啟動 Docker，`nemoclaw <名稱> start` |
| OpenShell Gateway | `connect` 退出、`status` 顯示 Gateway down | 全部沙盒的推理與網路 | 低 | Linux：`systemctl --user restart openshell-gateway`，再 `recover` |
| Agent 內部 Gateway（OpenClaw／Hermes） | Dashboard 打不開、Agent 不回應 | 單一沙盒 | 低 | `nemoclaw <名稱> recover` 或 `gateway restart` |
| 推理服務 | `status` 的 Inference 行為 `unauthorized` 或逾時 | 使用該 Provider 的沙盒 | 無 | 檢查 Key、端點、政策（11.3） |
| 網路政策 | `CONNECT tunnel failed, response 403` | 該沙盒的特定端點 | 無 | `nemoclaw <名稱> logs --tail 50` 確認拒絕紀錄 |
| 主機登錄 `sandboxes.json` 損壞 | `list`、`onboard` 報 JSON 無效 | 主機的沙盒管理 | 中 | 依官方指示備份壞檔後移除（11.3） |
| 主機重開機 | 沙盒顯示 Stopped | 全部 | 低 | 依「Reconnect after a host reboot」步驟（11.3）；官方不保證自動復原 |
| 主機磁碟滿 | 映像檔推送失敗、OOM | 全部 | 中 | `nemoclaw gc --dry-run`、清理 Docker（11.3） |

### 2.9 本章實務案例與注意事項

**案例**：資安審查時被問「Agent 拿得到 API Key 嗎？」

正確回答要分路徑：

1. 推理憑證（NVIDIA、OpenAI 等）：存在 OpenShell Gateway，沙盒內只有 placeholder；但沙盒內的 Agent **可以使用**這把 Key 呼叫被允許的路徑（例如 `POST /v1/chat/completions`），因此仍要在供應商端設定預算與限流。
2. 託管 MCP：NemoClaw 只記錄憑證名稱與擁有者中繼資料，值由 OpenShell 在核准出口替換。
3. 例外：OpenClaw 的 Gateway auth token 會被寫到 `/tmp/nemoclaw-proxy-env.sh`，讓沙盒 shell 能連本機 Gateway（官方 Filesystem Controls 頁明載）；WhatsApp 這類 QR 配對的 session 憑證會存在沙盒內。
4. 若同仁把 Key 直接寫進 `openclaw.json` 或 `.env`，沙盒就讀得到——這是行政規範要禁止的（第 13 章），而且 `rebuild` 會因私有封存的憑證掃描失敗而中止。

**注意事項**：

- 架構圖中的「OpenShell 0.0.116」是 v0.0.139 的釘選版本；每次升級 NemoClaw 都要重新確認（`grep openshell_version nemoclaw-blueprint/blueprint.yaml`）。
- 不要把 `openshell term` 的一次性核准當成正式白名單：它在沙盒刪除重建後就消失（6.3）。

## 第3章 環境需求與安裝前檢查

NemoClaw 的平台支援狀態由官方的 `ci/platform-matrix.json` 統一產生，文件與 README 都從這份 JSON 渲染。本章的表格以 v0.0.139 的平台矩陣為準；官方的用法說明也適用於企業：*A "Tested with limitations" row is not a "Tested" row*（「有限制的已測試」不等於「已測試」）。

### 3.1 平台／必要條件／支援狀態／注意事項

| 平台 | 必要條件 | 支援狀態 | 注意事項 |
|---|---|---|---|
| Linux（Ubuntu 24.04） | Docker Engine；`apt-get` 可用 | **Tested**（主要驗證路徑，有 CI） | Ubuntu 24.04 有主機層 onboarding 驗證；Ubuntu 26.04 只有 userspace 層 CI，Docker、AppArmor、Landlock 與實際 onboarding 驗證仍待完成 |
| Linux（Ubuntu 22.04、Fedora、Rocky、Alma、NixOS、Arch） | — | **未確認**（官方：may work but are not validated）；非 Ubuntu／Debian 系另列 *Unsupported* | 安裝程式假設 `apt-get`；Fedora 有已知卡住問題（issue #899） |
| Linux＋原生 rootless Podman | `NEMOCLAW_GATEWAY_RUNTIME=podman`、cgroups v2、`lsof`、目前使用者的 Podman socket | Tested with limitations | 不支援自訂 `--from` Dockerfile 與唯讀主機掛載；託管 vLLM 仍需要 Docker |
| DGX OS（Spark） | Docker | **Tested**（有 CI） | 可用 Express 安裝；雙機 vLLM 為 Experimental |
| DGX OS（Station GB300） | Docker | Tested with limitations（無 CI） | 只在一台實機驗證；DGX OS 7.6.x 完整 E2E 仍待完成 |
| macOS（Apple Silicon） | Colima 或 Docker Desktop；建議 Xcode Command Line Tools | Tested with limitations（有 CI） | 先啟動容器 Runtime；Homebrew Colima 需同時 `brew install colima docker`；Docker VM 核心可能不支援 Landlock |
| macOS（Intel x86_64） | — | ⛔ **Unsupported** | 安裝程式在下載前即拒絕 |
| Windows 11／10（build 19041+）＋WSL 2 | Docker Desktop（WSL backend）或合格的 rootless Podman | Tested with limitations（無 CI） | 所有 NemoClaw 指令在 WSL 內執行；官方以 x86-64 測試 |
| 原生 Windows（不經 WSL） | — | **未確認／無安裝路徑** | 官方只提供 WSL 2 路徑 |
| NVIDIA RTX 工作站 GPU（Linux） | NVIDIA Container Toolkit、CDI | Deferred | 託管 vLLM 需 `NEMOCLAW_EXPERIMENTAL=1` 或 `NEMOCLAW_PROVIDER=install-vllm` |
| N1x Linux | — | Deferred | 實機 Express E2E 未完成，不可宣稱支援 |
| Kubernetes／OpenShift | — | ⛔ Unsupported | 沙盒是 Docker 容器，不是 Pod |
| 離線（air-gapped） | — | ⛔ Unsupported | onboarding 需要下載與 Provider 驗證（issue #4872、#2218） |
| 多使用者共用主機 | — | ⛔ Unsupported | onboarding 會警告多使用者主機 |

**來源**：[Platform Support](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/platform-support)、[Prerequisites](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/prerequisites)、[`ci/platform-matrix.json`](https://github.com/NVIDIA/NemoClaw/blob/main/ci/platform-matrix.json)

### 3.2 硬體需求

| 資源 | 最低 | 建議 | 說明 |
|---|---|---|---|
| CPU | 4 vCPU | 4+ vCPU | — |
| RAM | 8 GB | 16 GB | 沙盒映像檔推送時，容器 Runtime、k3s、Gateway 與匯出管線同時執行，管線會在記憶體中緩衝解壓縮的 layer；低於 8 GB 可能觸發 OOM（exit 137） |
| 磁碟 | 20 GB 可用 | 40 GB 可用 | 沙盒映像檔壓縮後約 2.4 GB；每次重建可能留下舊映像檔（用 `nemoclaw gc` 清理） |
| Swap | — | 記憶體不足 8 GB 時至少 8 GB | 官方的緩解做法，代價是變慢 |
| GPU | 雲端推理不需要 | 本地推理依模型而定 | 只支援 NVIDIA GPU；需 NVIDIA Container Toolkit 與健康的 CDI；AMD／Intel／Apple Metal ⛔ Unsupported |

> 🏢 **企業建議**：Coding Agent 開發主機以 8 vCPU／32 GB／100 GB SSD 起跳。理由：Java＋Node 專案本身的建置、Testcontainers 啟動的資料庫容器、再加上沙盒映像檔與重建備份，20 GB 很快用完。

自己檢查主機是否達標（🖥️ Host，唯讀；📖 指令為標準 Linux 工具）：

```bash
# 🖥️ Host：主機資源檢查（不修改系統）
echo "CPU: $(nproc)"
free -g | awk '/^Mem:/{print "RAM(GB): "$2} /^Swap:/{print "Swap(GB): "$2}'
df -BG --output=avail,target ~ /var/lib/docker 2>/dev/null
nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv,noheader 2>/dev/null \
  || echo "GPU: 無（只用雲端推理時可接受）"
```

| 項目 | 通過標準 | 常見誤判 |
|---|---|---|
| `CPU` | ≥ 4（企業建議 ≥ 8） | VM 的 vCPU 被超額分配時，數字對但效能不夠，要看虛擬化平台的保證值 |
| `RAM(GB)` | ≥ 8（企業建議 ≥ 32） | `free -g` 無條件捨去：16 GB 主機常顯示 `15`，仍算通過 |
| `Swap(GB)` | RAM < 8 GB 時 ≥ 8 | Swap 只能避免 OOM，不能讓速度變快 |
| `avail` | 家目錄與 `/var/lib/docker` 都 ≥ 20G | 兩者在同一個分割區時，只會列出一行 |
| GPU | 本地推理才需要 | `memory.used` 接近 `memory.total` 代表 GPU 已被占滿 |

> ⚠️ **警告**：v0.0.139 在 Ollama 回報「可用 GPU 記憶體 0 MB」時，會把它當成「整張 VRAM 都可用」（`main` 的 #13748 已修正）。GPU 被其他程序占滿的主機，onboarding 可能選出放不下的模型。先用上面的 `nvidia-smi` 確認 `memory.used`，必要時先停掉占用 GPU 的程序。

### 3.3 軟體與依賴

| 依賴 | 版本 | 誰負責安裝 | 備註 |
|---|---|---|---|
| Node.js | 22.19 以上 | 安裝程式可透過 nvm 安裝 | 透過 nvm 安裝時需要 `sha256sum` 或 `shasum` |
| npm | 10 以上 | 隨 Node.js | 全域 prefix 不可寫時，CLI 會寫 shim 到 `~/.local/bin/nemoclaw` |
| 容器 Runtime | Docker Engine／Docker Desktop／Colima；或合格的 rootless Podman | 安裝程式可在 Linux 安裝 Docker（需 `sudo`） | 會把使用者加入 `docker` 群組（見 3.6 警告） |
| `strings`（binutils） | — | 需自行安裝 | 安裝程式用它驗證 OpenShell 執行檔 |
| `zstd` | — | Debian／Ubuntu 上自動以 `apt-get` 安裝 | 原生 Linux Ollama 路徑需要 |
| `git` | — | 需自行安裝 | bootstrap 安裝程式用 `git fetch` 取得指定版本 |
| OpenShell | 0.0.116 | **由 NemoClaw 安裝程式安裝** | ⛔ 不要自行安裝其他版本 |

> ⚠️ **警告**：官方 Prerequisites 頁的 *OpenShell Lifecycle* 警告：在 NemoClaw 管理的環境中，需要建立或重建 OpenShell Gateway 或沙盒時，用 `nemoclaw onboard`；避免 `openshell self-update`、`npm update -g openshell` 或直接 `openshell sandbox create`，除非你打算自己管理 OpenShell，事後再重跑 `nemoclaw onboard`。

### 3.4 Windows、WSL 2 與 Docker Desktop

Windows 的正確心智模型是：**Windows 只負責提供 WSL 2 與 Docker Desktop；NemoClaw 本身完全在 WSL 的 Ubuntu 裡執行**。官方原文：*All NemoClaw commands run inside WSL, not in PowerShell.*

| 步驟 | 執行位置 | 指令或動作 | 預期結果 |
|---|---|---|---|
| 1. 確認 Windows 版本 | 🪟 PowerShell | `[System.Environment]::OSVersion.Version` | Build 19041 以上 |
| 2. 啟用 WSL 2 | 🪟 PowerShell（系統管理員） | `wsl --install --no-distribution` | 啟用 WSL 與 Virtual Machine Platform；可能要求重開機 |
| 3. 安裝並註冊 Ubuntu | 🪟 PowerShell（系統管理員） | `wsl --install -d Ubuntu-24.04` | 第一次啟動時建立 Unix 帳號；**不要**加 `--no-launch` |
| 4. 確認是 WSL 2 | 🪟 PowerShell | `wsl -l -v` | `Ubuntu-24.04  Running  2` |
| 5. 安裝 Docker Desktop | Windows | 啟用 WSL 2 backend 與該發行版的 WSL integration | Settings → Resources → WSL integration 已勾選 |
| 6. 驗證 Docker | 🐧 WSL | `docker info` | 印出 Server 資訊 |

官方也提供 bootstrap 腳本一次完成 2～5 步（📖 Windows Preparation）：

```powershell
# 🪟 PowerShell：先下載到暫存檔，審查後再執行（不要直接管線執行）
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/NVIDIA/NemoClaw/main/scripts/bootstrap-windows.ps1' -OutFile "$env:TEMP\bootstrap-windows.ps1"
Get-Content "$env:TEMP\bootstrap-windows.ps1" | Select-Object -First 80   # 先看內容
Get-Help "$env:TEMP\bootstrap-windows.ps1" -Detailed                    # 看參數：-DistroName、-InstallDockerDesktop 等
powershell.exe -ExecutionPolicy Bypass -File "$env:TEMP\bootstrap-windows.ps1"
```

> ⚠️ **警告**：bootstrap 腳本會要求系統管理員權限、啟用 Windows 功能、透過 `winget` 安裝 Docker Desktop。腳本網址指向 `main` 分支而不是版本標籤；企業應先下載、比對 SHA-256、經資安審查後放到內部檔案庫，再由端點管理工具發佈。`-ExecutionPolicy Bypass` 只影響該 PowerShell 程序。

Windows 特有的注意事項：

| 項目 | 說明 |
|---|---|
| Dashboard 綁定 | WSL 上 Dashboard 轉埠綁定所有介面（讓 Windows 主機連得到），非 WSL 環境只綁 `127.0.0.1`；企業防火牆要確認 WSL 虛擬網卡不對外 |
| Windows 端 Ollama | 只在綁定 loopback `11434`、Docker Desktop 可達、且對不受信任的 `Host` 標頭回 `403` 時才重用；⛔ 不要設 `OLLAMA_HOST=0.0.0.0:11434` |
| 同時兩個 Ollama | 不要在 Windows 與 WSL 同時於 `11434` 執行 Ollama |
| `--host-mount` | 只支援 Linux 與 WSL 2 上的 Docker；原生 Windows 與 macOS 不支援 |
| Cursor 等 IDE Agent | 若 Coding Agent 的終端機被組織政策鎖住，官方建議改由 Agent 產生 `.ps1`／`.bat` 檔、經人工檢視後手動執行，且檔案內不可嵌入真實憑證 |

### 3.5 macOS 與 DGX 平台

- **macOS（Apple Silicon）**：先啟動 Docker Desktop 或 Colima；NemoClaw 會驗證釘選的官方 OpenShell Homebrew formula，並只在每次 Homebrew 操作前後暫時信任該 formula。Colima 建議至少 `colima start --cpu 4 --memory 8`。
- **DGX Spark**：官方主要驗證平台之一，安裝時可選 Express（自動選擇託管 vLLM 與 Balanced 政策）；官方另有 [DGX Spark Playbook](https://build.nvidia.com/spark/nemoclaw)（GitHub 版本：[dgx-spark-playbooks／nvidia／nemoclaw](https://github.com/NVIDIA/dgx-spark-playbooks/tree/main/nvidia/nemoclaw)）。Playbook 開宗明義要求「只使用乾淨環境，不放個資、機密或敏感憑證」。
- **DGX Station**：Tested with limitations，安裝前需依官方「Prepare DGX Station」頁完成準備；安裝程式可能以結束碼 `10`（需要重開機）或 `11`（需要重新登入）暫停。

macOS 自我檢查（🖥️ Host，唯讀；🧪 `docker info` 的欄位以你的 Docker 版本為準）：

```bash
uname -m      # 預期 arm64；x86_64 代表 Intel Mac，不在支援矩陣內
docker info --format 'OS={{.OperatingSystem}} CPUs={{.NCPU}} MemGiB={{div .MemTotal 1073741824}}'
colima status 2>/dev/null   # 使用 Colima 時才有輸出
```

判讀方式：沙盒能用的是 Docker VM 的資源，不是 Mac 本機的資源。即使 Mac 有 36 GB 記憶體，`MemGiB` 低於 8 時仍會遇到 3.2 說的 OOM。這時調高 Docker Desktop 的資源設定，或用 `colima start --cpu 4 --memory 8` 重建 VM。

DGX Station 安裝程式的結束碼處理（🖥️ Host；📖 結束碼 10、11 出自官方「Prepare DGX Station」頁；🧪 未實機執行）：

```bash
# 沿用 4.3 已下載並審查過的 nemoclaw.sh
NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG=v0.0.139 bash nemoclaw.sh; rc=$?
case $rc in
  0)  echo "完成：繼續 4.4 的版本確認" ;;
  10) echo "需要重新開機：重開後用同一行指令重跑" ;;
  11) echo "需要重新登入：登出再登入後用同一行指令重跑" ;;
  *)  echo "失敗（$rc）：保留完整輸出，依 11.3.1 排查" ;;
esac
```

❌ 壞例：看到結束碼 `10` 就判定「安裝失敗」，改用其他安裝方式重裝。結束碼 10、11 是安裝程式預期中的暫停點，照提示重開機或重新登入後重跑即可。

### 3.6 網路、DNS、Proxy、TLS 與防火牆需求

| 需求 | 用途 | 企業注意事項 |
|---|---|---|
| 連到 `www.nvidia.com`、`github.com`、`raw.githubusercontent.com` | 下載安裝程式與指定版本原始碼 | 若只允許內部鏡像，需另建 Git mirror（🧪，官方未提供離線安裝） |
| 連到容器 registry（`ghcr.io`；本地 NIM 另需 `nvcr.io` 與 NGC 登入） | 拉取 digest 固定的沙盒映像檔 | 若用企業 registry 代理，確認 digest 不變 |
| 連到 `registry.npmjs.org` | 安裝 CLI 與相依套件 | 可走企業 npm 代理（🧪） |
| 推理服務端點 | Provider 驗證與 Agent 推理 | 例如 `integrate.api.nvidia.com`、`api.openai.com` |
| DNS（UDP 53） | 容器內名稱解析 | 官方 preflight 會執行 `docker run --rm busybox nslookup nemoclaw-dns-probe-<亂數>.invalid`；封鎖 UDP 53、只走 DNS over TLS 的企業網路會失敗（解法見 11.3） |
| HTTP Proxy | 沙盒出口 | 沙盒預設代理是 OpenShell 注入的 `10.200.0.1:3128`；企業 Proxy 以 `NEMOCLAW_PROXY_HOST`、`NEMOCLAW_PROXY_PORT` 在 onboarding 前設定，屬**建置期**設定，變更要重新 onboarding |
| TLS 攔截（MITM Proxy） | 企業 Proxy 重新簽章 | onboarding 前設定 `NEMOCLAW_CORPORATE_CA_BUNDLE=/path/corp-ca.pem`，NemoClaw 會驗證並把 CA 烤進映像檔；既有沙盒要 `rebuild` |

> ⚠️ **警告（docker 群組）**：官方 Prerequisites 頁警告：*Members of the docker group can control the daemon with root-level impact.* 個人開發機加入 `docker` 群組是常見做法，但**共用或受管主機**應使用組織核准的 Docker 存取方式。這也是「一人一台主機」的原因之一。

### 3.7 模型推理服務、API Key 與帳號權限

onboarding 精靈提供的推理選項與對應的憑證環境變數（📖 Quickstart）：

| 選項 | 適用 | 憑證變數 | 平台矩陣狀態 |
|---|---|---|---|
| NVIDIA Endpoints | `build.nvidia.com` 上的託管模型（含 Nemotron） | `NVIDIA_INFERENCE_API_KEY` | Tested |
| OpenRouter | 託管的 OpenAI 相容 Provider | `OPENROUTER_API_KEY` | Tested |
| OpenAI | `https://api.openai.com/v1` | `OPENAI_API_KEY` | Tested |
| 其他 OpenAI 相容端點 | LocalAI、vLLM、NIM、SGLang、企業 AI Gateway | `COMPATIBLE_API_KEY` | Tested with limitations |
| Anthropic | Anthropic Messages API | `ANTHROPIC_API_KEY` | Tested |
| 其他 Anthropic 相容端點 | 含 AWS Bedrock Runtime（主機端 adapter） | 依端點 | Tested with limitations |
| Google Gemini | Google 的 OpenAI 相容端點 | 依 Provider | Tested |
| Local Ollama | 主機上的 Ollama | 無 | Tested with limitations |
| Local vLLM／llama.cpp／NIM | 本機 GPU 推理 | 依路徑 | Tested with limitations／Experimental |
| Model Router | 從 NVIDIA Endpoints 模型池中逐請求選模 | `NVIDIA_INFERENCE_API_KEY` | Experimental |

帳號權限的最低要求（🏢）：

- 推理 API Key 使用**專案專屬、低額度、可撤銷**的 Key，不用個人主帳號 Key。
- 在供應商端設定每日／每月預算與速率上限（NemoClaw 不做計費控管）。
- 若要讓 Agent 存取內部 Git，申請**唯讀、單一 repo、有到期日**的 Token（第 7、13 章）。

### 3.8 企業 Proxy、內網 Git、套件倉庫與私有模型的限制

| 企業設施 | 現況（v0.0.139） | 做法 | 狀態 |
|---|---|---|---|
| 企業 HTTP Proxy | 支援建置期設定 | `NEMOCLAW_PROXY_HOST`／`PORT` 後 onboarding | 📖 |
| 企業 TLS 攔截 CA | 支援 | `NEMOCLAW_CORPORATE_CA_BUNDLE` | 📖 |
| 內網 Git（Bitbucket、GitLab） | 沒有內建 preset | 自訂 preset＋`--trusted-private-host`（6.11） | 📖 機制／🧪 路徑規則 |
| 內部 Maven／npm 代理（Nexus、Artifactory） | 官方 preset 只有公開的 `npm`、`pypi`、`brew`、`huggingface` | 自訂 preset 指向內部代理 | 📖 機制／🧪 實測 |
| 私有模型服務（vLLM、企業 AI Gateway） | 「其他 OpenAI 相容端點」 | onboarding 時輸入 base URL 與 `COMPATIBLE_API_KEY` | 📖 |
| 完全離線 | ⛔ 不支援 | 不建議用 NemoClaw | — |
| 私有 IP 的端點 | OpenShell 預設以 SSRF 防護封鎖私有、迴環、link-local | 自訂 preset 必須用 `--trusted-private-host <精確主機名>` 明確信任，NemoClaw 會解析並把位址釘死 | 📖 |

> 📌 **註記**：官方 Customize Network Policy 頁提醒，不要依賴 `host.docker.internal` 作為一般的主機服務路徑，因為它會繞過 OpenShell 政策路徑且不一定可達。要讓沙盒連主機上的 HTTP 服務，應把服務開在 Gateway 可達的主機 IP，並用自訂 preset 放行。

### 3.9 安裝前預檢腳本

以下腳本只讀取資訊、不安裝任何東西。執行位置：🖥️ Host（Linux 或 WSL Ubuntu）。🧪 本腳本依官方需求撰寫，未在 Linux 實機執行；請先在測試主機驗證輸出。

```bash
#!/usr/bin/env bash
# preflight-nemoclaw.sh — 🏢 企業自訂預檢（唯讀，不修改系統）
set -u
pass(){ printf '  [PASS] %s\n' "$1"; }
fail(){ printf '  [FAIL] %s\n' "$1"; FAILED=1; }
warn(){ printf '  [WARN] %s\n' "$1"; }
FAILED=0

echo "== 作業系統與核心"
. /etc/os-release 2>/dev/null && echo "  $PRETTY_NAME"
[[ "${ID:-}" == "ubuntu" && "${VERSION_ID:-}" == "24.04" ]] && pass "Ubuntu 24.04（官方主要驗證路徑）" || warn "不是 Ubuntu 24.04，屬未驗證或有限制平台"
kver=$(uname -r | cut -d. -f1-2)
awk -v v="$kver" 'BEGIN{split(v,a,".");exit !(a[1]>5||(a[1]==5&&a[2]>=13))}' && pass "核心 $kver ≥ 5.13（Landlock 可用）" || fail "核心 $kver < 5.13，檔案系統限制會降級"
grep -qi microsoft /proc/version && warn "偵測到 WSL：Windows 路徑為 Tested with limitations"

echo "== 硬體"
cpus=$(nproc); mem=$(awk '/MemTotal/{printf "%d",$2/1024/1024}' /proc/meminfo); disk=$(df -BG --output=avail "$HOME" | tail -1 | tr -dc 0-9)
(( cpus >= 4 )) && pass "CPU $cpus 核" || fail "CPU $cpus 核 < 4"
(( mem >= 8 )) && pass "RAM ${mem} GB" || fail "RAM ${mem} GB < 8（需 swap）"
(( disk >= 20 )) && pass "家目錄可用 ${disk} GB" || fail "家目錄可用 ${disk} GB < 20"

echo "== 軟體"
command -v node >/dev/null && node -e 'const [a,b]=process.versions.node.split(".").map(Number);process.exit(a>22||(a===22&&b>=19)?0:1)' \
  && pass "Node.js $(node -v)" || warn "Node.js 缺少或低於 22.19（安裝程式可用 nvm 安裝）"
for c in git strings sha256sum curl; do command -v "$c" >/dev/null && pass "$c 存在" || fail "$c 不存在"; done
command -v zstd >/dev/null && pass "zstd 存在" || warn "zstd 不存在（Debian/Ubuntu 會自動安裝）"

echo "== 容器 Runtime"
if docker info >/dev/null 2>&1; then
  pass "Docker 可用：$(docker version --format '{{.Server.Version}}' 2>/dev/null)"
  id -nG | grep -qw docker && warn "目前帳號在 docker 群組（等同 root 影響力，確認符合公司規範）"
  docker run --rm busybox nslookup registry.npmjs.org >/dev/null 2>&1 && pass "容器內 DNS 正常" || fail "容器內 DNS 失敗（見 11.3 企業防火牆 DNS）"
else
  fail "docker info 失敗（未安裝、未啟動或沒有權限）"
fi

echo "== 網路與 Proxy"
env | grep -iE '^(https?_proxy|no_proxy)=' | sed 's/=.*@/=***@/' || true
for u in https://www.nvidia.com https://github.com https://registry.npmjs.org https://ghcr.io; do
  curl -sS -o /dev/null -m 10 -w "%{http_code}" "$u" >/dev/null 2>&1 && pass "可連 $u" || fail "無法連 $u"
done
for v in REQUESTS_CA_BUNDLE CURL_CA_BUNDLE SSL_CERT_FILE NEMOCLAW_CORPORATE_CA_BUNDLE; do
  [[ -n "${!v:-}" ]] && warn "$v=${!v}（NemoClaw 會依序作為企業 CA 來源）"
done

echo "== 多使用者"
users=$(who | awk '{print $1}' | sort -u | wc -l)
(( users <= 1 )) && pass "目前只有 $users 位登入使用者" || warn "有 $users 位使用者登入，官方不支援多使用者共用主機"

exit $FAILED
```

▶️ **預期結果**：全部 `[PASS]` 時結束碼為 `0`；任何 `[FAIL]` 結束碼為 `1`。`[WARN]` 需要人工判斷。

安裝完成後，改用官方的唯讀就緒報告（📖 System Readiness）：

```bash
# 🖥️ Host：不會修改主機、Docker、Gateway、憑證、政策或沙盒狀態
nemoclaw host probe
nemoclaw host probe --json > host-probe-$(date +%Y%m%d).json
echo "exit=$?"   # 0＝supported、2＝incompatible、3＝inconclusive
```

### 3.10 本章實務案例與注意事項

**案例**：同仁的 Windows 筆電裝了 Docker Desktop，但 `nemoclaw onboard` 卡在 DNS 檢查。

診斷順序：

1. 🐧 WSL：`docker run --rm busybox nslookup registry.npmjs.org`。失敗代表是容器 DNS，不是 NemoClaw。
2. 若公司封鎖 UDP 53、只允許 DNS over TLS（TCP 853），容器不會繼承主機的 DoT 設定。官方解法：在 Docker Desktop 設定 GUI 指定企業 DNS。
3. 若 DNS 伺服器回 `NXDOMAIN`／`REFUSED`，代表解析器有回應但拒絕，要找 DNS 管理員檢查轉送規則，不是開 UDP 53。
4. 修好後重跑 `nemoclaw onboard --resume`。

**注意事項**：

- 平台狀態以研究日為準，每次升級前重新查看 Platform Support 頁。
- Ubuntu 26.04 目前只有 userspace CI，不要因為「新版」就選它。
- WSL 上的 Dashboard 綁定所有介面，筆電在公共網路時要確認 Windows 防火牆設定。

## 第4章 安裝、初始化與首次啟動

本章以「在一台乾淨的 Ubuntu 24.04（或 WSL 2 Ubuntu 24.04）主機上，安裝 NemoClaw v0.0.139、建立一個 Deep Agents Code 開發沙盒、並驗證限制有效」為主線，OpenClaw 與 Hermes 的差異在各步驟註明。每個指令都標示執行位置、前提、預期結果、失敗排查，以及是否會改動系統。

### 4.1 安裝流程總覽

```mermaid
flowchart TD
    A["Step 1 安裝前檢查<br/>preflight 腳本"] --> B["Step 2 下載並審查安裝程式<br/>固定版本、關閉遙測"]
    B --> C["Step 3 執行安裝<br/>Node.js、Docker、OpenShell、CLI"]
    C --> D["Step 4 選擇 Agent<br/>onboarding 精靈"]
    D --> E["Step 5 推理服務<br/>Provider、模型、憑證"]
    E --> F["Step 6 沙盒與政策<br/>名稱、政策層級、preset"]
    F --> G["Step 7 首次啟動<br/>launch 或 connect"]
    G --> H["Step 8～9 測試請求<br/>確認回應"]
    H --> I["Step 10 驗證限制<br/>檔案、網路、憑證"]
    I --> J["Step 11 日誌與狀態<br/>status、logs、doctor"]
    J --> K{"全部通過？"}
    K -- 否 --> L["依 11.3 排查<br/>onboard --resume"]
    L --> D
    K -- 是 --> M["記錄版本盤點<br/>12.2"]
```

### 4.2 Step 1：安裝前的環境檢查

| 項目 | 內容 |
|---|---|
| 執行位置 | 🖥️ Host（Linux 或 🐧 WSL） |
| 前提 | 已完成第 3 章的平台確認；Windows 已完成 3.4 |
| 指令 | `bash preflight-nemoclaw.sh`（3.9 的腳本） |
| 預期結果 | 結束碼 `0`，沒有 `[FAIL]` |
| 失敗排查 | 依 `[FAIL]` 項目處理；DNS 失敗見 11.3 |
| 是否修改系統 | 否（只讀取資訊；會拉取並執行 `busybox` 測試映像檔） |

### 4.3 Step 2：官方安裝方式與安全檢查

官方安裝指令是：

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

在企業環境，**不要直接執行這一行**。先理解它做了什麼（📖 摘自 v0.0.139 `install.sh` 與 `scripts/install.sh`）：

| 階段 | 動作 | 會修改系統嗎 |
|---|---|---|
| bootstrap | 解析要安裝的版本：`NEMOCLAW_INSTALL_REF` ＞ `NEMOCLAW_INSTALL_TAG` ＞ 預設 `lkg` | 否 |
| bootstrap | 在暫存目錄 `git init` 並 `git fetch --depth 1` 該版本 | 暫存目錄 |
| bootstrap | 若已安裝較新版本，拒絕以 `lkg` 降級 | 否 |
| bootstrap | 檢查下載的 `scripts/install.sh` 非空且以 shebang 開頭，然後執行 | 否 |
| 安裝 | 第三方軟體聲明（需接受） | 否 |
| 安裝 | 必要時以 nvm 安裝 Node.js（驗證 nvm 安裝程式的完整性） | 是：家目錄 |
| 安裝 | Linux 上若無 Docker，下載 Docker 官方便利腳本並以 `sudo` 執行、啟動服務、把使用者加入 `docker` 群組 | **是：系統層級** |
| 安裝 | 安裝 OpenShell 0.0.116（比對官方 checksum 檔）與 Gateway 使用者服務 | 是 |
| 安裝 | 以 `npm link` 或 `~/.local/bin/nemoclaw` shim 安裝 CLI | 是 |
| 安裝 | 若有既有沙盒：先全部備份、必要時汰換 Gateway、執行 `upgrade-sandboxes --auto` | 是 |
| 安裝 | 前置檢查通過後自動啟動 `nemoclaw onboard` | 是：建立沙盒 |

> ⚠️ **警告（供應鏈）**：bootstrap 對下載的 payload 只做「非空、以 shebang 開頭」的檢查，**沒有**簽章或雜湊比對；完整性依賴 HTTPS 與 GitHub。版本標籤本身有 SSH 簽章（`git cat-file -p` 可看到 `BEGIN SSH SIGNATURE`），但驗證需要 NVIDIA 的公鑰，官方文件未提供驗證步驟（🧪）。

企業建議的安全安裝程序（🏢）：

```bash
# 🖥️ Host：1. 下載而不執行
mkdir -p ~/nemoclaw-install && cd ~/nemoclaw-install
curl -fsSL --proto '=https' --proto-redir '=https' https://www.nvidia.com/nemoclaw.sh -o nemoclaw.sh
sha256sum nemoclaw.sh | tee nemoclaw.sh.sha256

# 2. 與 GitHub 上的固定版本比對（兩者應相同；不同時停止並通報）
curl -fsSL "https://raw.githubusercontent.com/NVIDIA/NemoClaw/v0.0.139/install.sh" -o install-v0.0.139.sh
sha256sum install-v0.0.139.sh
diff -q nemoclaw.sh install-v0.0.139.sh && echo "SAME" || echo "DIFFERENT：交資安審查"

# 3. 審查重點（至少看這幾處）
grep -n 'DEFAULT_INSTALL_REF=' nemoclaw.sh            # 預設版本來源
grep -n 'github.com/NVIDIA/NemoClaw.git' nemoclaw.sh  # 下載來源
grep -n 'verify_downloaded_script' nemoclaw.sh        # 完整性檢查方式
bash nemoclaw.sh --help                               # 只印說明，不安裝
```

| 項目 | 內容 |
|---|---|
| 執行位置 | 🖥️ Host |
| 前提 | 可連 `www.nvidia.com` 與 `raw.githubusercontent.com` |
| 預期結果 | `SAME`；`--help` 印出選項與環境變數清單 |
| 失敗排查 | `DIFFERENT`：可能是 `nemoclaw.sh` 已更新到比 v0.0.139 新的 bootstrap；以 GitHub 標籤版本為準，並請資安比對差異 |
| 是否修改系統 | 否（只下載檔案）🧪 `www.nvidia.com/nemoclaw.sh` 與 GitHub 檔案是否逐位元相同，需實際比對 |

### 4.4 Step 3：執行安裝並確認版本

```bash
# 🖥️ Host：每個新 shell 都要先設定
export NEMOCLAW_DISABLE_TELEMETRY=1      # 關閉預設遙測（官方：每個 shell 都要設）
export NEMOCLAW_NO_EXPRESS=1             # 🏢 不使用 Express 自動選擇，改為逐項確認

# 固定版本安裝；NEMOCLAW_INSTALL_REF 要清空，否則它的優先順序較高
NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG=v0.0.139 \
  NEMOCLAW_AGENT=langchain-deepagents-code \
  bash ~/nemoclaw-install/install-v0.0.139.sh
```

> 📌 **註記**：官方文件的寫法是 `curl … | NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG=vX.Y.Z bash`，環境變數必須放在管線右側的 `bash` 前面才讀得到。上例改為執行已審查的本地檔案，效果相同。不指定時安裝的是 `lkg`（研究當日為 v0.0.137），與文件站 latest（v0.0.139）不一致。

| 項目 | 內容 |
|---|---|
| 執行位置 | 🖥️ Host |
| 前提 | Step 2 審查通過；有 `sudo` 權限（若需安裝 Docker） |
| 預期結果 | 依序完成 Node.js、Docker、OpenShell、CLI 安裝，接著進入 onboarding 精靈 |
| 失敗排查 | 印出 `newgrp docker` → 執行後重跑；`nemoclaw: command not found` → `source ~/.bashrc` 或把 `~/.local/bin` 加入 `PATH`；`strings` 缺少 → `sudo apt-get install -y binutils` |
| 是否修改系統 | **是**：安裝套件、加入群組、建立使用者服務、建立 `~/.nemoclaw/` |

安裝後的版本確認（若安裝程式已直接進入精靈，可在另一個終端機執行）：

```bash
# 🖥️ Host
nemoclaw --version          # 預期：nemoclaw v0.0.139
nemo-deepagents --version   # 同一套 CLI 的別名
openshell --version         # 預期：openshell 0.0.116（🧪 實際輸出格式依 OpenShell 0.0.116）
nemoclaw agents list        # 預期列出 openclaw、hermes、langchain-deepagents-code
```

`nemoclaw agents list` 的官方預期輸出：

```text
openclaw                   Gateway-based AI agent with plugin ecosystem (openclaw.ai)
hermes                     Self-improving AI agent with learning loop (Nous Research)
langchain-deepagents-code  Terminal coding agent built on the Deep Agents SDK
```

> ✅ **建議**：`nemoclaw --version` 的版本來自建置身分（build identity），不是 `package.json`（後者寫 `0.1.0`，只是備援值）。版本對不上時，以 `--version` 為準並記錄到 12.2 的盤點表。

### 4.5 Step 4：選擇 Agent 與引導式初始化

| Agent | 入口 | 選擇方式 | 適合 |
|---|---|---|---|
| OpenClaw（預設） | `nemoclaw onboard` | 不加 `--agent` | 常駐助理、Dashboard、訊息通道 |
| Hermes | `nemohermes onboard` | `--agent hermes` 或 `NEMOCLAW_AGENT=hermes` | 自我學習型 Agent；提供 OpenAI 相容 API（連接埠 8642～8652） |
| LangChain Deep Agents Code | `nemo-deepagents onboard` | `--agent langchain-deepagents-code`（別名 `dcode`、`deepagents`、`langchain`） | 終端機 Coding Agent，無 Dashboard |

```bash
# 🖥️ Host：建立開發用 Deep Agents 沙盒（若安裝程式沒有自動進入精靈）
nemo-deepagents onboard --name dev-order
```

精靈依序詢問：Agent（若入口未指定）→ 推理 Provider 與模型 → 憑證 → 沙盒名稱 → 檢閱畫面 → 選擇性的 Web Search 與訊息通道 → 政策層級與 preset。

**沙盒名稱規則**（📖 Troubleshooting「Invalid sandbox name」）：1～19 個字元、小寫、字母開頭、只含字母數字與單一連字號、字母或數字結尾、不可有 `--`；不可與全域指令同名（`onboard`、`list`、`setup`、`start`、`stop`、`status`、`debug`、`uninstall`、`credentials`、`help`）。

> 🏢 **命名規範**：`<用途>-<專案代號>`，例如 `dev-order`、`re-legacy`、`up-billing`。19 字元限制來自 OpenShell 0.0.116 的路由名稱限制（官方 Update Sandboxes 頁）。

### 4.6 Step 5：模型推理服務設定

精靈的推理選單（📖 Quickstart）：

```text
  1) NVIDIA Endpoints
  2) OpenRouter
  3) OpenAI
  4) Other OpenAI-compatible endpoint
  5) Anthropic
  6) Other Anthropic-compatible endpoint
  7) Google Gemini
  8) Local Ollama (localhost:11434)
  9) Model Router (experimental)
  Choose [1]:
```

不想在精靈中貼 Key 時，事先以不留歷史紀錄的方式放進環境變數（📖 Credential Rotation 的寫法）：

```bash
# 🖥️ Host：讀入時不回顯、不寫入 shell 歷史
printf 'NVIDIA inference API key: ' >&2
IFS= read -r -s NVIDIA_INFERENCE_API_KEY; printf '\n' >&2
export NVIDIA_INFERENCE_API_KEY
nemo-deepagents onboard --name dev-order
unset NVIDIA_INFERENCE_API_KEY
```

| 項目 | 內容 |
|---|---|
| 執行位置 | 🖥️ Host |
| 前提 | 已取得專案專屬、低額度的 API Key |
| 預期結果 | 精靈驗證 Provider 與模型後進入檢閱畫面，提供 **Apply configuration**／Edit／**Exit onboarding** |
| 失敗排查 | 驗證失敗 → 檢查 Key 與網路；相容端點失敗見 11.3 |
| 是否修改系統 | 選 Apply 後在 OpenShell Gateway 註冊 Provider 與憑證 |

> ⚠️ **警告**：使用企業私有模型時，選 **Other OpenAI-compatible endpoint**，輸入內部 base URL。官方 Platform Support 對這一列的註記是：它宣稱的是「轉接器」，不是所有相容端點都能用；企業 AI Gateway 的工具呼叫格式要實測（🧪，見 11.3「Tool calls appear as assistant text」）。

### 4.7 Step 6：沙盒建立與安全政策確認

精靈會問政策層級（📖 Network Policies — Policy Tiers）：

| 層級 | 套用的 preset | 本手冊建議 |
|---|---|---|
| Restricted | 無層級預設（只有基準政策） | 🏢 **企業首選**：之後只加審查過的自訂 preset |
| Balanced（預設） | `npm`、`pypi`、`huggingface`、`brew-balanced`、`brave`（及所選 Web Search） | 只用於個人評估 |
| Open | 再加上 `brew`、`weather`、`public-reference`、`slack`、`discord`、`telegram`、`jira`、`outlook` 等 | ⛔ 企業不使用 |
| Personal | `personal-open-internet`（強制）：所有程式可連任何公開與私有位址的 80／443 | ⛔ 企業禁止 |

非互動模式指定層級：

```bash
# 🖥️ Host
NEMOCLAW_POLICY_TIER=restricted nemo-deepagents onboard --name dev-order \
  --non-interactive --yes-i-accept-third-party-software
```

> ⚠️ **警告（Personal 層）**：官方原文：*An agent can send workspace data or sandbox-visible credentials to an arbitrary reachable service on either port without an operator approval prompt.* 而且 Personal 一旦套用，NemoClaw **拒絕**就地移除，只能另建沙盒。

> ⚠️ **警告（Deep Agents 的基準政策）**：即使選 Restricted，Deep Agents Code 的 Agent 專屬基準政策（`agents/langchain-deepagents-code/policy-additions.yaml`）仍包含 `github.com` 與 `api.github.com` 的 `access: full`（L4，不檢查方法與路徑），以及 `pypi`。這代表 Agent 預設就能對 GitHub 推送資料。若企業不允許，必須在 onboarding 後以 `nemo-deepagents dev-order policy exclude github --dry-run` 預覽、再以 `--force` 移除（📖 v0.0.139 原始碼 `src/lib/policy/baseline-exclusion.ts` 為這個 key 註明的影響是「Git operations and GitHub API or source access may stop working」；見 6.15）。

### 4.8 Step 7：Agent 首次啟動

```bash
# 🖥️ Host：確認就緒
nemo-deepagents dev-order status

# 一步完成連線與啟動 TUI
nemo-deepagents launch dev-order

# 或分兩步：先進沙盒 shell，再自己啟動
nemo-deepagents dev-order connect
```

```bash
# 📦 Sandbox（connect 之後）
dcode status     # 印出沙盒名稱、harness、推理路由、Provider、模型、端點後結束
dcode            # 啟動互動式 TUI
```

| 項目 | 內容 |
|---|---|
| 執行位置 | `status`／`launch`／`connect`：🖥️ Host；`dcode`：📦 Sandbox |
| 前提 | onboarding 完成並印出 ready 摘要 |
| 預期結果 | `status` 顯示 Agent 行（例如 `Agent: LangChain Deep Agents Code vX.Y.Z`）與健康的 Inference 行 |
| 失敗排查 | `connect` 因 Gateway down 退出 → 11.3「Gateway 連線異常」；OpenClaw 卡在裝置配對 → `nemoclaw onboard --resume` |
| 是否修改系統 | `launch` 在 Linux 會發佈 24 小時的就緒租約（不含憑證）；其餘否 |

OpenClaw 的差異：用 `nemoclaw my-assistant dashboard-url --quiet` 取得含驗證片段的 Dashboard URL（**把它當密碼對待**），或 `nemoclaw launch my-assistant` 進入 `openclaw tui`。

### 4.9 Step 8～9：發送測試請求並驗證回應

```bash
# 🖥️ Host：Deep Agents 無頭模式（沒有核准 UI，會自動核准非 shell 工具；測試用簡單問題即可）
nemo-deepagents dev-order connect
```

```bash
# 📦 Sandbox
dcode -n "Reply with only: hello-nemoclaw" --json
```

▶️ 預期 stdout 只有一個 JSON 物件，`data.status` 為 `success`、`data.exit_code` 為 `0`、`data.response` 含 `hello-nemoclaw`；程序結束碼與 `data.exit_code` 相同。

```json
{
  "schema_version": 1,
  "command": "non-interactive",
  "data": {
    "status": "success",
    "exit_code": 0,
    "response": "hello-nemoclaw",
    "completion": { "thread_id": "thread-id", "duration_ms": 842, "response_bytes": 14 }
  }
}
```

OpenClaw 版本（📖 Commands — agent）：

```bash
# 🖥️ Host：OpenClaw 必須指定 --agent、--session-id、--session-key 或 --to 其中之一
nemoclaw my-assistant agent --session-id smoke-1 -m "Reply with only: hello-nemoclaw"
```

失敗時的判讀：`timeout` 結束碼 `124`；stderr 會有 `error_class`、`category`、`retryable`、`correlation_id`，用 `correlation_id` 對照 `logs`。

### 4.10 Step 10：確認檔案、網路與憑證限制有效

這一步是**驗收的核心**：沒有做這一步，就不能宣稱「已在沙盒中執行」。以下以 `exec` 從主機送指令進沙盒（以 `sandbox` 使用者、`HOME=/sandbox` 執行）。🧪 錯誤訊息的確切字樣依映像檔而定。

```bash
# 🖥️ Host：控制有效性驗證（🏢 企業自訂驗收腳本）
S=dev-order
run(){ nemo-deepagents "$S" exec -- bash -lc "$1"; }

echo "== 1. 身分：應為 sandbox，不是 root"
run 'id -un'

echo "== 2. 系統路徑唯讀：應失敗"
run 'touch /usr/local/bin/evil 2>&1 || echo BLOCKED-OK'

echo "== 3. 工作區可寫：應成功"
run 'mkdir -p /sandbox/work && touch /sandbox/work/.probe && echo WRITE-OK'

echo "== 4. 主機機密不可見：應找不到"
run 'ls /home/*/.ssh /root/.ssh 2>&1 | head -3; echo CHECKED'

echo "== 5. 未核准網路：應被拒（CONNECT 403）"
run 'python3 -c "import urllib.request as u; u.urlopen(\"https://example.com\", timeout=10)" 2>&1 | tail -1'

echo "== 6. 環境中沒有真實推理金鑰：應無輸出"
run 'env | grep -E "nvapi-[A-Za-z0-9]{8}|sk-[A-Za-z0-9]{16}" || echo NO-RAW-KEY'

echo "== 7. Landlock 狀態（看 onboarding 輸出或 doctor）"
nemo-deepagents "$S" doctor
```

▶️ 預期結果：

| 檢查 | 預期 | 若不符 |
|---|---|---|
| 1 | `sandbox` | ⛔ 停止使用，檢查是否用了自訂映像檔或直接容器 |
| 2 | `BLOCKED-OK` 或 `Read-only file system`／`Permission denied` | 檢查 Landlock 是否降級（核心版本） |
| 3 | `WRITE-OK` | 檢查 `/sandbox` 權限 |
| 4 | `No such file or directory` | ⛔ 若看得到主機檔案，代表有不當掛載 |
| 5 | `Tunnel connection failed: 403` 類訊息；同時 `exec` 會在 stderr 附加 `recent network policy denial detected for example.com:443` 提示 | 若成功連線，檢查是否誤選 Personal／Open 層 |
| 6 | `NO-RAW-KEY` | ⛔ 若出現真實 Key，立即撤銷並調查 |
| 7 | 無 Landlock 降級警告 | 依 11.3 處理 |

> 📌 **註記**：檢查 5 的 `exec` 失敗提示是官方功能：`exec` 指令非零結束時，NemoClaw 會查詢沙盒稽核紀錄，在 stderr 附上被拒的 `host:port` 與後續指令（`logs --tail 50`、`policy list`、`policy add`）。設定 `NEMOCLAW_NO_POLICY_HINT=1` 可關閉。

### 4.11 Step 11：檢查日誌與服務狀態

```bash
# 🖥️ Host
nemoclaw status                         # 全域：沙盒清單、輔助服務、Gateway 健康
nemo-deepagents dev-order status --json > status-dev-order.json
nemo-deepagents dev-order logs --tail 100
nemo-deepagents dev-order logs --follow  # 持續串流，Ctrl+C 結束
openshell term                           # 即時網路活動；j/k 選沙盒、Enter 進入
nemoclaw doctor                          # 主機與 Gateway 唯讀檢查（不需沙盒）
```

> ✅ **建議**：把 `status --json`、`host probe --json` 與 4.10 的驗收輸出存成「安裝證據」，附在環境申請單上（13.2）。

### 4.12 非互動安裝（CI 與標準映像）

```bash
# 🔧 CI 或 🖥️ Host：完全非互動（變數要放在 bash 這一側）
export NEMOCLAW_DISABLE_TELEMETRY=1
NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG=v0.0.139 \
NEMOCLAW_NON_INTERACTIVE=1 \
NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1 \
NEMOCLAW_AGENT=langchain-deepagents-code \
NEMOCLAW_PROVIDER=build \
NEMOCLAW_POLICY_TIER=restricted \
NEMOCLAW_SANDBOX_NAME=ci-smoke \
NVIDIA_INFERENCE_API_KEY="$NVIDIA_INFERENCE_API_KEY" \
  bash ./install-v0.0.139.sh
```

`NEMOCLAW_PROVIDER` 可用值（📖 `install.sh --help`）：`build`、`openrouter`、`openai`、`anthropic`、`anthropicCompatible`、`gemini`、`ollama`、`custom`、`nim-local`、`vllm`、`routed`、`hermes-provider`、`llama-cpp`、`install-llama-cpp`（別名 `cloud`→`build`、`nim`→`nim-local`）。

> ⚠️ **警告**：非互動模式遇到上一次失敗的 onboarding session 會**拒絕執行並以非零結束**，避免腳本無限重試。必須明確選擇 `--fresh`（丟棄紀錄）或 `--resume`（續作），見 11.3。

### 4.13 本章實務案例與注意事項

**案例**：新進同仁照網路教學執行 `curl | bash`，裝到的是 v0.0.137，文件卻寫 v0.0.139 的功能。

原因是安裝程式預設追蹤 `lkg` 標籤。處理方式：

1. `nemoclaw --version` 確認實際版本。
2. 以 `NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG=v0.0.139` 重跑已審查的安裝程式（既有沙盒會先被備份並升級）。
3. `nemoclaw upgrade-sandboxes --check` 確認沒有過期沙盒。
4. 部門標準作業程序改為「一律指定版本標籤」。

**注意事項**：

- 每個新 shell 都要 `export NEMOCLAW_DISABLE_TELEMETRY=1`；建議寫進 `~/.bashrc`，並在 13.2 的申請檢查表列為必要項目。
- 首次 onboarding 跳過 Web Search 與訊息通道；兩者之後變更都需要重建沙盒。
- 4.10 的驗收沒有全部通過前，不得把任何專案原始碼放進沙盒。

## 第5章 設定管理與 CLI 操作

NemoClaw 主機上有兩套 CLI：`nemoclaw`（含 `nemohermes`、`nemo-deepagents` 別名）與 `openshell`。官方 CLI Selection Guide 的經驗法則是：**會改變 NemoClaw 如何建立、重建、保存或設定沙盒的事，先用 `nemoclaw`；要檢查或變更即時的 OpenShell Gateway、TUI、原始政策、轉埠或推理路由時，才用 `openshell`。** 本章所有指令皆為 📖（v0.0.139 官方 Commands 參考與 CLI 原始碼）。

### 5.1 兩套 CLI 的分工

| 任務 | 用 `nemoclaw` | 用 `openshell` |
|---|---|---|
| 建立／重建沙盒 | ✅ `onboard`、`rebuild` | ⛔ 不要用 `openshell sandbox create` 建 NemoClaw 沙盒 |
| 套用 preset | ✅ `policy add`／`remove` | — |
| 整份替換政策 | 匯出用 `policy get` | ✅ `openshell policy set --policy <檔> --wait <沙盒>` |
| 即時核准網路請求 | — | ✅ `openshell term` |
| 檢視生效政策 | `policy list`、`policy explain` | ✅ `openshell policy get <沙盒>` |
| 傳檔 | ✅ `upload`／`download`（會檢查沙盒是否存活、拒絕含 symlink 的目錄） | `openshell sandbox upload`／`download`（刻意繞過 wrapper 時） |
| 轉埠 | 受管轉埠用 `recover` 修復 | 使用者自建轉埠用 `openshell forward start --background <port> <沙盒>` |
| 憑證 | ✅ `credentials list`／`add`／`reset` | `openshell provider list`（只看名稱） |

### 5.2 指令文法

```text
nemoclaw <全域指令> [選項]               例：nemoclaw status、nemoclaw doctor、nemoclaw list
nemoclaw <沙盒名稱> <沙盒動作> [選項]    例：nemoclaw dev-order status、nemoclaw dev-order policy list
nemoclaw <沙盒名稱> exec [選項] -- <指令>  例：nemoclaw dev-order exec --workdir /sandbox/work -- ls -la
```

- 省略沙盒名稱時，需要名稱的動作會印出正確格式並結束。
- 沙盒可以剛好叫 `doctor`：`nemoclaw doctor status` 操作名為 `doctor` 的沙盒；`nemoclaw doctor` 仍是全域檢查。
- `nemoclaw use <名稱>` 設定預設沙盒（取代手改 `~/.nemoclaw/sandboxes.json`）。
- `nemoclaw completion bash` 產生補全腳本：`source <(nemoclaw completion bash)`。

### 5.3 命令總表

| 操作目的 | 命令 | 執行位置 | 預期結果 | 注意事項 |
|---|---|---|---|---|
| 查看 CLI 版本 | `nemoclaw --version` | 🖥️ Host | `nemoclaw v0.0.139` | 不是 `nemoclaw version` |
| 主機就緒報告 | `nemoclaw host probe [--json]` | 🖥️ Host | 結束碼 0／2／3 | 唯讀 |
| 主機與 Gateway 檢查 | `nemoclaw doctor [--json]` | 🖥️ Host | 各項檢查結果 | 不需要沙盒 |
| 全域狀態 | `nemoclaw status [--json]` | 🖥️ Host | 沙盒清單、Gateway、輔助服務 | 只看 `NEMOCLAW_GATEWAY_PORT` 選定的 Gateway |
| 列出沙盒 | `nemoclaw list [--json]` | 🖥️ Host | 名稱、模型、Provider、preset；`●` 表示有連線中的 session | JSON 會遮蔽可辨識的憑證值 |
| 列出可用 Agent | `nemoclaw agents list` | 🖥️ Host | 三個 Agent 名稱 | 全域指令；`<名稱> agents list` 是 OpenClaw 內的 Agent |
| 建立沙盒 | `nemoclaw onboard [--agent …] [--name …]` | 🖥️ Host | ready 摘要 | 互動精靈；CI 用 `--non-interactive` |
| 續作中斷的 onboarding | `nemoclaw onboard --resume` | 🖥️ Host | 從檢查點繼續 | 只用於中斷，不用於重建完成的沙盒 |
| 重新建立同名沙盒 | `nemoclaw onboard --fresh --name <名稱> --recreate-sandbox` | 🖥️ Host | 新沙盒 | ⚠️ 原沙盒會被取代，先備份 |
| 單一沙盒狀態 | `nemoclaw <名稱> status [--json]` | 🖥️ Host | Agent 版本、Inference 健康、恢復提示 | 會實際送一次推理請求驗證憑證 |
| 單一沙盒健康檢查 | `nemoclaw <名稱> doctor [--json]` | 🖥️ Host | Docker、OpenShell、Gateway、路由、模型呼叫 | `--fix` 嘗試修復（OpenClaw） |
| 連線進沙盒 | `nemoclaw <名稱> connect` | 🖥️ Host → 📦 | 進入沙盒 shell | 會先做就緒等待與路由調和 |
| 連線並啟動 Agent | `nemoclaw launch <名稱>` | 🖥️ Host | 直接進 Agent TUI | Linux 有 24 小時就緒租約 |
| 單次 Agent 回合 | `nemoclaw <名稱> agent …` | 🖥️ Host | Agent 回應 | OpenClaw 需 `--agent`／`--session-id` 等選擇器；Deep Agents 轉給 `dcode` |
| 在沙盒執行指令 | `nemoclaw <名稱> exec -- <指令>` | 🖥️ Host | 指令輸出與結束碼 | 以 `sandbox` 使用者執行；取代 `docker exec`（後者以 root 執行） |
| 停止沙盒 | `nemoclaw <名稱> stop` | 🖥️ Host | 狀態 `Stopped`，所有狀態保留 | 釋放 CPU／記憶體／GPU |
| 啟動沙盒 | `nemoclaw <名稱> start` | 🖥️ Host | 回到 Ready，修復 Gateway 與轉埠 | 主機重開機後使用 |
| 修復沙盒 | `nemoclaw <名稱> recover` | 🖥️ Host | 恢復就緒與轉埠 | 不開 SSH session |
| 重啟沙盒內 Gateway | `nemoclaw <名稱> gateway restart` | 🖥️ Host | Gateway 重新啟動 | 設定或 plugin 只在啟動時讀取時使用 |
| 重建沙盒 | `nemoclaw <名稱> rebuild [--yes]` | 🖥️ Host | 以新映像檔重建並還原原生 home | 升級 Agent 版本的正規方式 |
| 刪除沙盒 | `nemoclaw <名稱> destroy [--yes]` | 🖥️ Host | 沙盒與持久化狀態刪除 | ⛔ 不可復原，先 `download` |
| 查看日誌 | `nemoclaw <名稱> logs [--follow] [--tail N] [--since 10m]` | 🖥️ Host | 生命週期與 Gateway 輸出 | `--tail` 與 `-n` 相同 |
| 即時網路活動與核准 | `openshell term` | 🖥️ Host | TUI | 遠端主機要先 SSH 過去 |
| 查看推理設定 | `nemoclaw inference get [--json]` | 🖥️ Host | Provider、模型、端點 | 不會驗證憑證 |
| 切換模型／Provider | `nemoclaw inference set --provider <p> --model <m> [--sandbox <名稱>]` | 🖥️ Host | 路由更新 | 部分變更會觸發重建（6.14） |
| 列出憑證 | `nemoclaw credentials list` | 🖥️ Host | Provider 名稱 | 不顯示值 |
| 註冊憑證 | `nemoclaw credentials add <名稱> --type <t> --credential <ENV>` | 🖥️ Host | 註冊到 Gateway | 值從環境變數讀，不放在 argv |
| 移除憑證 | `nemoclaw credentials reset <名稱>` | 🖥️ Host | 從 Gateway 移除 | 有原生附掛時會拒絕 |
| 查看 preset | `nemoclaw <名稱> policy list` | 🖥️ Host | 已套用與可用的 preset | 標示 `[from <tier> tier]` |
| 預覽並套用 preset | `nemoclaw <名稱> policy add <preset> --dry-run` 後去掉 `--dry-run` 加 `--yes` | 🖥️ Host | 顯示將開放的端點 | 增量套用（6.13） |
| 套用自訂 preset | `nemoclaw <名稱> policy add --from-file <檔> [--trusted-private-host <主機>]` | 🖥️ Host | 命名空間化寫入即時政策 | 先跑 6.16 的 lint |
| 移除 preset | `nemoclaw <名稱> policy remove <preset> --yes` | 🖥️ Host | 收窄出口 | — |
| 匯出基礎政策 | `nemoclaw <名稱> policy get > current-policy.yaml` | 🖥️ Host | 已遮蔽憑證的 YAML | 憑證值被換成 `[STRIPPED_BY_MIGRATION]` |
| 給 Agent 看的政策摘要 | `nemoclaw <名稱> policy explain [--json]` | 🖥️ Host | 已遮蔽的允許／阻擋說明 | OpenClaw 會寫到 `/sandbox/.openclaw/workspace/POLICY.md` |
| 下載檔案 | `nemoclaw <名稱> download <沙盒路徑> [主機目的地]` | 🖥️ Host | 檔案複製到主機 | 拒絕含 symlink 的目錄 |
| 上傳檔案 | `nemoclaw <名稱> upload <主機路徑> [沙盒目的地]` | 🖥️ Host | 檔案複製進沙盒 | 相對路徑以目前目錄解析 |
| 雙向掛載 | `nemoclaw <名稱> share mount [沙盒路徑] [本機目錄]` | 🖥️ Host | SSHFS 掛到 `~/.nemoclaw/mounts/<名稱>` | ⚠️ 雙向即時同步，見 7.2 |
| 備份所有沙盒 | `nemoclaw backup-all` | 🖥️ Host | 寫入 `~/.nemoclaw/rebuild-backups/` | 停止中的沙盒會暫時啟動 |
| 檢查需要升級的沙盒 | `nemoclaw upgrade-sandboxes --check` | 🖥️ Host | 列出過期沙盒 | 唯讀；有問題時非零結束 |
| 更新 CLI | `nemoclaw update [--check]` | 🖥️ Host | 執行受管安裝流程 | 企業用固定版本重跑安裝程式（12.5） |
| 清理孤兒映像檔 | `nemoclaw gc --dry-run`，確認後 `nemoclaw gc --yes` | 🖥️ Host | 移除未使用的沙盒映像檔 | — |
| 收集診斷包 | `nemoclaw debug --sandbox <名稱> --output debug.tgz` | 🖥️ Host | 系統、Docker、Gateway 日誌、狀態 | 上傳前檢查是否含敏感資訊 |
| 解除安裝 | `nemoclaw uninstall [--yes] [--keep-openshell]` | 🖥️ Host | 移除執行資源，預設保留備份 | ⛔ `--destroy-user-data`、`--delete-models` 不可逆 |
| 匯出 v1 設定 | `nemoclaw config export <名稱> --output nemoclaw.yaml` | 🖥️ Host | `v1alpha1` YAML，檔案權限 `0600` | 不含憑證值 |

### 5.4 查看版本與執行狀態

```bash
# 🖥️ Host：每日開工檢查（唯讀）
nemoclaw --version
nemoclaw status
nemo-deepagents dev-order status
```

`nemoclaw <名稱> status` 的關鍵欄位（🧪 實際排版依版本）：

| 欄位 | 意義 | 異常時 |
|---|---|---|
| Phase | `Ready`／`Stopped`／`Error` | `Stopped` → `start`；`Error` → `recover` 或 `rebuild` |
| Agent | 執行中的 Agent 與版本 | 顯示過期警告 → `rebuild` |
| Inference | 從沙盒內走 Agent 實際路徑送出的推理檢查 | `unauthorized`（HTTP 401／403）→ 憑證問題（11.3） |
| Recovery hints | 建議的修復指令 | 照做前先讀說明 |

### 5.5 建立、啟動、停止與連線

```bash
# 🖥️ Host：一天的生命週期
nemo-deepagents onboard --name dev-order        # 建立（第一次）
nemo-deepagents launch dev-order                 # 進 TUI 工作
nemo-deepagents dev-order stop                   # 下班釋放資源（狀態保留）
nemo-deepagents dev-order start                  # 隔天恢復
nemo-deepagents dev-order connect                # 只要 shell 時
```

> 📌 **註記**：全域的 `nemoclaw start`／`nemoclaw stop` 已淘汰。停止沙盒請用 `nemoclaw <名稱> stop`；公開網址 tunnel 用 `nemoclaw tunnel start`／`stop`。

### 5.6 Agent 啟動、互動與任務執行

| Agent | 互動 | 單次任務（自動化） | 從主機轉送 |
|---|---|---|---|
| OpenClaw | `nemoclaw launch <名稱>` 或 Dashboard | `nemoclaw <名稱> agent --session-id <id> -m "<訊息>" [--json]` | `exec -- openclaw agent --agent main -m "…"` |
| Hermes | Dashboard 或 OpenAI 相容 API（`127.0.0.1:8642`，Bearer 用 `gateway-token --quiet`） | API 呼叫 | `exec -- hermes --version` |
| Deep Agents Code | `nemo-deepagents launch <名稱>` → `dcode` TUI | 📦 `dcode -n "<任務>" --json` | `nemo-deepagents <名稱> agent -n "<任務>" --json` |

Deep Agents 的兩種模式差異是工作流程設計的關鍵（📖 Run Deep Agents Code）：

| 模式 | 檔案寫入與編輯 | Shell 執行 | 適用 |
|---|---|---|---|
| 互動 TUI `dcode` | 破壞性工具需逐次核准 | 需核准（或依 shell allowlist） | 開發、重構、需要人在迴圈中 |
| 無頭 `dcode -n` | **自動核准** | **停用** | 唯讀分析、產文件、摘要 |
| `--dcode-auto-approval thread-opt-in` | 允許個別 thread 選擇 Auto 模式（`dcode -y`） | 依模式 | ⛔ 企業預設不開啟 |

> ⚠️ **警告**：官方明言 *Headless `dcode -n` has no approval UI and automatically approves non-shell tool requests, including file writes and edits.* 用 `dcode -n` 做「分析」時，仍要確認工作目錄是可丟棄的副本，或原始碼以 `--host-mount` 唯讀掛入。

管線輸入的等待期限（v0.0.139 與 `main` 的差異）：

- **v0.0.139**：官方文件寫「沙盒內的 OpenClaw 解析器最多等 30 秒的管線輸入」。但 OpenShell 要等到主機端 stdin 結束（EOF）才會啟動沙盒內的程式，所以只要產生輸入的程式不關閉管線，沙盒內的計時根本不會開始，指令會一直卡到外層逾時（Issue #13621）。
- **`main`（#13646，尚未發布）**：改由主機端先讀完管線輸入。期限是正整數的 `--timeout`，沒有指定時為 30 秒，輸入上限 4 MiB。逾時、超過上限或讀取失敗時，指令以結束碼 1 結束、印出處理建議，而且**不會**啟動這一輪對話。

```bash
# 🖥️ Host（📖 v0.0.139 Commands 參考）
# ✅ 好例：訊息用 -m 直接給，或從檔案導入（檔案讀完就是 EOF）
nemoclaw my-assistant agent --session-id ci-1 -m "列出 src/main 下的套件" --json
nemoclaw my-assistant agent --session-id ci-1 --timeout 300 < prompt.txt

# ❌ 壞例：產生器不會結束（tail -f），v0.0.139 會卡住直到外層逾時
tail -f prompt.txt | nemoclaw my-assistant agent --session-id ci-1
```

▶️ 在 CI 中驗證不會卡住：外層一定要再包一層 `timeout`，並分辨結束碼。

```bash
# 🔧 CI
timeout 600 nemoclaw my-assistant agent --session-id "ci-$CI_JOB_ID" --timeout 300 < prompt.txt; rc=$?
[ "$rc" -eq 124 ] && echo "外層逾時：檢查輸入是否有 EOF（v0.0.139 已知行為）"
```

> 📌 **註記**：v0.0.139 對不支援的 `--dcode-auto-approval thread-opt-in`（例如用在 OpenClaw，或自訂 Dockerfile／映像檔）要到「建立沙盒」這一步才會拒絕。在那之前，Gateway 可能已經啟動，精靈也可能已經問過推理 Provider。`main`（#13567）已改成在 onboarding 開始前就拒絕。在 v0.0.139 遇到這種半途失敗時，先用 `nemoclaw list` 確認沒有留下半成品沙盒，再用正確參數重跑。

### 5.7 模型 Provider 與推理服務設定

```bash
# 🖥️ Host
nemoclaw inference get --json
nemoclaw my-assistant inference get

# OpenClaw／Hermes：切換到同 Provider 的另一個模型（官方範例）
nemoclaw my-assistant inference set --provider nvidia-prod --model nvidia/nemotron-3-super-120b-a12b

# OpenClaw／Hermes：切換到企業私有 OpenAI 相容端點（憑證名稱用 --credential-env 指定）
export COMPATIBLE_API_KEY='<由密碼庫取得>'
nemoclaw my-assistant inference set --provider compatible-endpoint \
  --endpoint-url https://llm-gw.corp.example/v1 --credential-env COMPATIBLE_API_KEY \
  --model corp-coder-32b
unset COMPATIBLE_API_KEY
```

官方列出的標準 Provider ID：`nvidia-prod`、`nvidia-nim`、`nvidia-router`、`openai-api`、`openrouter-api`、`anthropic-prod`、`compatible-anthropic-endpoint`、`gemini-api`、`compatible-endpoint`、`hermes-provider`、`llama-cpp-local`、`ollama-local` 等。私有端點若在 RFC1918 位址，還要以 `NEMOCLAW_TRUSTED_PRIVATE_HOSTS` 明確信任（🧪 企業 AI Gateway 的實際驗證行為需實測）。

> ⚠️ **警告（Deep Agents）**：官方 Run Deep Agents Code 頁指出，Deep Agents 的模型與 Provider 設定是烤進映像檔的，`config set` 不支援，要變更請「重新 onboarding 該沙盒」。`inference set` 的官方說明只涵蓋 OpenClaw 與 Hermes。對 Deep Agents 沙盒，切換模型以 `nemo-deepagents onboard --name dev-order`（相同名稱、改選模型）為準，並先做 12.3 的備份（🧪）。

### 5.8 網路政策的檢視、更新與驗證

```bash
# 🖥️ Host
nemoclaw dev-order policy list                       # 已套用的 preset
nemoclaw dev-order policy explain                    # 已遮蔽的允許／阻擋摘要
openshell policy get dev-order                       # OpenShell 實際生效政策
nemoclaw dev-order policy add pypi --dry-run         # 預覽
nemoclaw dev-order policy add pypi --yes             # 套用（增量）
nemoclaw dev-order policy remove pypi --yes          # 移除
nemoclaw dev-order policy exclude github --dry-run   # 預覽移除基準項目的影響
```

詳細設計與審查見第 6 章。

### 5.9 沙盒狀態與日誌查詢

```bash
# 🖥️ Host
nemoclaw dev-order logs --since 30m
nemoclaw dev-order logs --follow
nemoclaw debug --quick --sandbox dev-order
nemoclaw debug --sandbox dev-order --output ~/nemoclaw-debug-$(date +%Y%m%d%H%M).tgz
```

OpenShell TUI 操作（📖 Approve Network Requests）：

| 按鍵 | 動作 |
|---|---|
| `j`／`k` | 選擇沙盒或規則 |
| `Enter` | 進入沙盒檢視、查看規則詳情 |
| `r` | 切到 Network Rules 面板 |
| `a` | 核准選取的待審規則（加入目前沙盒實例的執行中政策） |
| `x` | 拒絕選取的待審規則 |
| `A` | 核准全部待審規則（需再按 `y` 或 `Enter` 確認）——⛔ 企業禁止使用 |

用 `status --json` 判讀推理路由（🖥️ Host；📖 欄位名稱出自 v0.0.139 Commands 參考的 `status` 說明，🧪 實際值依你的 Provider 而定）：

```bash
nemoclaw dev-order status --json \
  | jq '{provider, model, recordedRoute, liveRoute, routeDrift, inferenceHealth, failureLayer, openshellVersion}'
```

| 看到的值 | 正確解讀 | 下一步 |
|---|---|---|
| `liveRoute: null`、`routeDrift: null`，Provider 是原生附掛（NVIDIA、固定託管、原生本地） | **正常**。這類沙盒不讀共享路由，所以兩個欄位永遠是 `null`（自 #12886 起，v0.0.139 已包含） | 改看 `recordedRoute` 與 `inferenceHealth` |
| `routeDrift` 不是 `null` | 共享路由和沙盒紀錄的路由不一致 | 先處理 drift，再相信任何端點資訊 |
| `failureLayer` 不是 `null`（例如 `docker_unreachable`） | 發生前置故障；此時 `inferenceHealth` 會被設成 `null`，避免顯示過時的健康狀態 | 依 `failureLayer` 先修 Docker 或容器 |
| `inferenceHealth` 為 `ok` | 不一定代表模型真的回答過：官方說明 `ok` 也可能是「路由可達但沒有送請求」或原生 NVIDIA 降級 | 要確認，就照 4.9 送一次測試請求 |

❌ 誤判例：監控腳本把 `liveRoute == null` 當成故障並發出告警。原生附掛 Provider 的沙盒會因此天天誤報；官方 Issue #13552 就曾把這個行為誤報成退化，`main` 的 #13648 隨後補上了文件說明。

### 5.10 狀態保存、恢復與資源清理

```bash
# 🖥️ Host：獨立備份（不依賴 rebuild 的內建封存）
SANDBOX=dev-order
BACKUP_DIR=~/.nemoclaw/backups/$(date +%Y%m%d-%H%M%S)
mkdir -p "$BACKUP_DIR"
nemo-deepagents "$SANDBOX" download /sandbox/.deepagents/config.toml "$BACKUP_DIR/"
nemo-deepagents "$SANDBOX" download /sandbox/.deepagents/agent/AGENTS.md "$BACKUP_DIR/agent/"
nemo-deepagents "$SANDBOX" download /sandbox/.deepagents/agent/memories/ "$BACKUP_DIR/agent/memories/"
nemo-deepagents "$SANDBOX" download /sandbox/.deepagents/agent/skills/ "$BACKUP_DIR/agent-skills/"
nemo-deepagents "$SANDBOX" download /sandbox/work/ "$BACKUP_DIR/work/"   # 🏢 專案工作目錄

# 清理
nemoclaw gc --dry-run
```

### 5.11 安裝更新、故障復原與解除安裝

```bash
# 🖥️ Host：更新（🏢 企業以固定版本重跑已審查的安裝程式，見 12.5）
nemoclaw upgrade-sandboxes --check
nemoclaw update --check

# 解除安裝（預設保留 rebuild-backups/、backups/、sandboxes.json）
nemoclaw uninstall
```

| 旗標 | 效果 | 風險 |
|---|---|---|
| `--yes` | 不詢問 | — |
| `--keep-openshell` | 保留 OpenShell | — |
| `--delete-models` | 刪除 Ollama 回報的**所有**模型（包含其他應用程式使用的） | ⛔ 不可逆 |
| `--destroy-user-data` | 一併刪除使用者資料 | ⛔ 不可逆 |
| `--all-gateway-ports` | 移除所有 Gateway 連接埠的環境 | 影響同主機其他環境 |

### 5.12 常用環境變數

| 變數 | 用途 | 生效時機 |
|---|---|---|
| `NEMOCLAW_DISABLE_TELEMETRY=1` | 關閉匿名遙測 | 每個 shell |
| `NEMOCLAW_INSTALL_TAG`／`NEMOCLAW_INSTALL_REF` | 指定安裝版本（REF 優先） | 安裝 |
| `NEMOCLAW_NON_INTERACTIVE=1`、`NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1` | 非互動安裝 | 安裝／onboarding |
| `NEMOCLAW_NO_EXPRESS=1` | 跳過 Express 提示 | 安裝 |
| `NEMOCLAW_AGENT` | `openclaw`、`hermes`、`langchain-deepagents-code` | 安裝／onboarding |
| `NEMOCLAW_SANDBOX_NAME` | 沙盒名稱 | onboarding |
| `NEMOCLAW_PROVIDER`、`NEMOCLAW_MODEL`、`NEMOCLAW_ENDPOINT_URL` | 推理選擇 | onboarding |
| `NEMOCLAW_POLICY_TIER` | `restricted`、`balanced`、`open`、`personal` | onboarding |
| `NEMOCLAW_POLICY_MODE` | `suggested`、`custom`、`skip` | onboarding |
| `NEMOCLAW_TRUSTED_PRIVATE_HOSTS` | 逗號分隔的精確私有主機 | 推理、託管 MCP、自訂 preset 註冊 |
| `NEMOCLAW_PROXY_HOST`／`NEMOCLAW_PROXY_PORT` | 沙盒出口 Proxy（預設 `10.200.0.1:3128`） | **建置期**，變更需重新 onboarding |
| `NEMOCLAW_CORPORATE_CA_BUNDLE` | 企業 CA PEM | 建置期，既有沙盒需 `rebuild` |
| `NEMOCLAW_GATEWAY_PORT` | OpenShell Gateway 連接埠（預設 8080） | 所有指令 |
| `NEMOCLAW_LOG_LEVEL` | `error`、`warn`、`info`、`debug` | 所有指令 |
| `NEMOCLAW_RESOURCE_PROFILE`、`NEMOCLAW_CPU`、`NEMOCLAW_RAM` | 沙盒 CPU／記憶體 | onboarding |
| `NEMOCLAW_SANDBOX_READY_TIMEOUT` | 建立後就緒等待秒數（預設 180） | onboarding |
| `NEMOCLAW_LOCAL_INFERENCE_TIMEOUT` | 本地推理驗證逾時（預設 180） | onboarding |
| `NEMOCLAW_EXPERIMENTAL=1` | 顯示實驗性 Provider | onboarding（⛔ 企業預設不開） |
| `NEMOCLAW_NO_POLICY_HINT=1` | 關閉 `exec` 失敗時的政策提示 | `exec` |
| `NEMOCLAW_NO_CONNECT_HINT=1` | 關閉 `connect` 的提示 | `connect` |

### 5.13 版本差異與淘汰指令

| 指令 | 狀態 | 改用 |
|---|---|---|
| `nemoclaw setup` | 淘汰（相容別名） | `nemoclaw onboard` |
| `nemoclaw setup-spark` | 淘汰 | 標準安裝程式＋`nemoclaw onboard` |
| `nemoclaw start`（全域） | 淘汰 | `nemoclaw <名稱> start` 或 `nemoclaw tunnel start` |
| `nemoclaw stop`（全域） | 淘汰 | `nemoclaw tunnel stop` |
| `nemoclaw <名稱> config set`（OpenClaw） | 不支援 | 進沙盒用 `openclaw configure`／`openclaw config set` |
| `nemoclaw <名稱> config set`（Deep Agents） | 不支援 | 重新 onboarding |
| `NEMOCLAW_DISABLE_DEVICE_AUTH=1` | 無效（OpenClaw 2026.9.1 已移除繞過） | 依正常配對流程 |
| v1 線的 `plan`／`apply`／`destroy` | 屬另一條產品線 | 見 1.7，不適用 v0.0.x |

### 5.14 偽指令說明（概念用，不可直接執行）

有些企業需求目前**沒有**官方指令。為了說明概念，本手冊以 `# 偽指令` 標記，**不可複製執行**：

```text
# 偽指令：概念示意，NemoClaw v0.0.139 沒有這些指令
nemoclaw fleet status --all-hosts          # 多主機集中管理（官方：Manual or admin-only）
nemoclaw audit export --siem splunk        # 集中稽核匯出（官方：Manual or admin-only）
nemoclaw rbac grant reviewer alice         # 操作者 RBAC（官方：Out of scope）
nemoclaw budget set --monthly 200usd       # 成本上限（官方：Platform or partner-owned）
```

對應的企業替代做法分別見 14.7（稽核）、13.1（角色）、14.10（成本）。

### 5.15 本章實務案例與注意事項

**案例**：同仁用 `docker exec -it <容器> bash` 進沙盒除錯，結果在裡面以 root 改了檔案。

- 官方說明：`docker exec` 以 root 執行並落在不同的環境；支援的替代是 `nemoclaw <名稱> exec`（以 `sandbox` 使用者、`HOME=/sandbox` 執行）或 `connect`。
- `exec` 結束後，NemoClaw 會驗證並必要時還原 OpenClaw 設定的權限契約；`docker exec` 不會。
- 處置：`nemoclaw <名稱> doctor` 檢查，必要時 `rebuild`；並在 13.11 的禁止清單加入「不得以 `docker exec` 操作 NemoClaw 沙盒」。

**注意事項**：

- 表格中的旗標以 v0.0.139 為準；升級後先跑 `nemoclaw help` 與 `nemoclaw <名稱> --help`（🧪）比對。
- 會刪資料的指令（`destroy`、`uninstall --destroy-user-data`、`--recreate-sandbox`）一律先 `download` 或 `backup-all`。

## 第6章 安全架構與政策管理

本章是全書的核心。前半（6.1～6.10）說明 NemoClaw 在每一層提供什麼控制、控制的極限在哪裡；後半（6.11～6.16）手把手寫出一份**教學用最小權限政策**，套用、驗證、並教你如何審查 AI 幫你寫的政策。所有政策格式依 v0.0.139 的 Blueprint 與官方 preset 原始檔（📖），搭配 OpenShell 0.0.116。

### 6.1 五層防護與套用時機

| 層 | 保護什麼 | 執行點 | 何時套用 | 能否執行期變更 |
|---|---|---|---|---|
| 網路 | 只允許政策列出的主機／連接埠／方法／路徑／程式 | OpenShell Gateway 與 L7 代理 | 每個請求 | ✅ 可熱更新 |
| 檔案系統 | 系統路徑唯讀，只有 `/sandbox`、`/tmp` 等可寫 | Landlock（核心）＋容器掛載 | 沙盒建立時鎖定 | ❌ 需重建 |
| 程序 | 阻擋提權與危險系統呼叫、限制程序數 | seccomp、`no-new-privileges`、非 root 使用者、`ulimit` | 沙盒建立時鎖定 | ❌ 需重建 |
| Gateway 驗證 | 哪些裝置與客戶端能連到 Agent Gateway | OpenClaw 裝置配對、Hermes bearer token | 建立時 | 部分 |
| 推理 | Agent 能用哪些模型、走哪條路由 | OpenShell 推理路由與附掛 Provider | 每個請求 | ✅ 可熱更新 |

> 📌 **註記**：官方 Security Best Practices 頁強調，OpenShell 執行 NemoClaw 所設定的平台機制（網路命名空間隔離、seccomp、SSRF 防護、TLS 終結、Gateway 驗證）。NemoClaw 決定「設成什麼」，OpenShell 決定「怎麼擋」。

### 6.2 沙盒隔離與檔案系統限制

各 Agent 的檔案系統基準（📖 `nemoclaw-blueprint/policies/openclaw-sandbox.yaml`、`agents/*/policy-additions.yaml`）：

| 項目 | OpenClaw | Hermes | Deep Agents Code |
|---|---|---|---|
| 可寫 | `/sandbox`（`include_workdir: true`）、`/tmp`、`/dev/null`、`/dev/pts`、`/sandbox/.openclaw`、`/sandbox/.nemoclaw`、`/home/linuxbrew` | `/sandbox`、`/tmp` 等 | `/sandbox`、`/sandbox/.deepagents`、`/run/nemoclaw-dcode-mcp`、`/tmp`、`/dev/null` |
| 唯讀 | `/usr`、`/lib`、`/proc`、`/dev/urandom`、`/app`、`/etc`、`/var/log`、`/var/lib/dpkg` | 同類 | 同上，另加 `/opt/venv`（保護釘選的 `dcode` harness） |
| Landlock | `best_effort`（核心不支援時靜默降級） | `best_effort` | **`strict`**（無法執行時沙盒啟動失敗，fail closed） |
| 執行身分 | `sandbox:sandbox` | `sandbox:sandbox` | `sandbox:sandbox` |

**主機目錄的兩種帶入方式**：

| 方式 | 方向 | 支援 | 安全性 |
|---|---|---|---|
| `nemoclaw onboard --host-mount /主機/目錄:/sandbox/目錄` | 主機 → 沙盒，**唯讀** | Linux／WSL 2 上的 Docker；macOS、原生 Windows、Podman、K8s 不支援 | ✅ 適合逆向工程：Agent 改不到原始檔 |
| `nemoclaw <名稱> share mount` | **雙向** SSHFS | 主機需有 SSHFS | ⚠️ 主機端編輯即時進沙盒、沙盒端寫入即時回主機；等於把沙盒的寫入能力延伸到主機目錄 |

> ⚠️ **警告**：`--host-mount` 只在 onboarding 時宣告，**沒有讀寫模式**。不要為了「讓 Agent 直接改主機上的專案」而改用 `share mount` 掛整個家目錄；應改為在沙盒內 `git clone` 工作副本（7.2）。

### 6.3 網路：預設拒絕與允許清單

**運作方式**（📖 Network Policies、Security Best Practices）：

1. 沙盒的所有出站流量都經過 OpenShell 的 CONNECT 代理。
2. 政策比對「主機＋連接埠＋發起程式」；有 `protocol: rest` 的端點再比對 HTTP 方法與路徑（L7）。
3. 未列出的請求被擋下、記錄，並出現在 `openshell term` 等候核准。
4. OpenShell 另外硬性封鎖未指定、迴環、link-local 位址（含常見的雲端 metadata 範圍）；私有位址需要明確的 `allowed_ips`（由 NemoClaw 的 `--trusted-private-host` 產生）。

**程式身分（binary）比對**：OpenShell 讀取 `/proc/<pid>/exe`（核心可信的執行檔路徑，不是 `argv[0]`），往上走訪程序樹找祖先程式，並在第一次使用時計算執行檔的 SHA-256；執行期間若執行檔被替換，雜湊不符會立即拒絕。路徑支援 glob：`*` 比對一層、`**` 遞迴。

**L4 與 L7 的差別**：

| 寫法 | 檢查內容 | 用途 | 風險 |
|---|---|---|---|
| 沒有 `protocol`（例如 `access: full`） | 主機、連接埠、程式 | 無法被 L7 檢查的協定（Git over HTTPS 的部分客戶端、WebSocket 相容問題） | 放行後整條 TCP 串流都不看內容 |
| `protocol: rest`＋`enforcement: enforce`＋`rules` | 再加上每個 HTTP 請求的方法與路徑 | REST API、套件庫 | 規則寫太寬（`POST /**`）等於沒限制 |
| `protocol: websocket`／`json-rpc`／`mcp` | 對應協定的方法（MCP 可再比對 tool） | WebSocket、MCP | — |

**核准的持久性**（官方兩頁的說法需合併理解）：

| 情境 | 結果 |
|---|---|
| 在 `openshell term` 核准 | 合併為該沙盒政策的新版本，同一沙盒實例內重啟仍有效 |
| `destroy` 後重新 onboarding | 回到 Blueprint 基準，一次性核准消失 |
| 要讓未來的沙盒也有效 | 寫成 preset（6.11）或改基準政策 |

> ⚠️ **警告**：官方 Best Practices：*If you approve a broad domain (such as a CDN that hosts arbitrary content), the agent can fetch anything from that domain until you destroy and recreate the sandbox.* 企業規範：`openshell term` 只能核准「已有申請單、範圍精確」的請求，禁止 `A`（全部核准）。

### 6.4 程序權限與系統呼叫限制

| 控制 | 預設 | 由誰執行 | 限制 |
|---|---|---|---|
| 非 root | Agent、Gateway、supervisor 以 `sandbox` 執行（OpenShell 0.0.116 拒絕 root OCI 使用者） | 映像檔＋OpenShell | 同 UID，彼此無隔離（2.4） |
| `no-new-privileges` | OpenShell 以 `prctl(PR_SET_NO_NEW_PRIVS)` 設定 | OpenShell | — |
| seccomp | 過濾危險系統呼叫、socket domain | OpenShell | — |
| Capabilities | OpenShell 負責受管程序的 capability | OpenShell | 直接用 Docker 啟動時要自己加 `--cap-drop=ALL` |
| 程序數 | `ulimit -u 512` | 映像檔 entrypoint | **best effort**：Runtime 不允許時只記警告；Deep Agents 較嚴格（每次啟動都套用並驗證） |
| 檔案描述元 | `ulimit -n 65536` | 同上 | 同上 |
| PATH 鎖定 | `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`（Deep Agents 加 `/opt/venv/bin`） | entrypoint | — |
| 移除工具鏈 | 清除 `gcc`、`g++`、`cpp`、`make`、`netcat` 系列 | Dockerfile | 自訂映像檔要自己決定（7.3） |

> ✅ **建議**：若需要硬性的資源上限（fail closed），官方建議由容器 Runtime 設定；企業共用主機應另以 Docker 的 `--memory`、`--cpus` 或 `NEMOCLAW_RESOURCE_PROFILE`（Blueprint 定義的 `creator`、`developer` 等 profile）限制（🧪 實際效果依 Runtime）。

### 6.5 外部 API 與模型服務存取控制

| 對象 | 控制方式 | 審查重點 |
|---|---|---|
| 推理服務 | 附掛 Provider 限制主機、路徑、方法、程式；或共享路由 `inference.local` | 不要在政策中額外開放推理供應商的其他路徑（例如檔案上傳 API） |
| 託管 MCP | `nemoclaw <名稱> mcp add <名稱> --url https://… --env <TOKEN_ENV>`；可加 `--deny-tool 'delete_*'` | 只接受 HTTPS Streamable HTTP；deny 規則只比對工具名稱、不檢查參數 |
| 一般 REST API | 自訂 preset，`protocol: rest`＋精確路徑 | 讀寫分離（6.11） |
| Web Search | `brave`／`tavily` preset＋獨立 Provider | 搜尋查詢本身就是一種外送資料 |

託管 MCP 範例（📖 Commands — mcp add）：

```bash
# 🖥️ Host：Token 只存在當下 shell，註冊後立即 unset
export LOCAL_MCP_TOKEN='<由密碼庫取得>'
nemo-deepagents dev-order mcp add jira-ro \
  --url https://mcp.corp.example/mcp \
  --env LOCAL_MCP_TOKEN \
  --trusted-private-host mcp.corp.example \
  --deny-tool 'create_*' --deny-tool 'delete_*' --deny-tool 'update_*'
unset LOCAL_MCP_TOKEN
nemo-deepagents dev-order mcp status jira-ro
```

### 6.6 API Key、Token、SSH 金鑰與其他敏感憑證管理

| 憑證 | NemoClaw 的處理 | 企業規範（🏢） |
|---|---|---|
| 推理 API Key | 註冊到 OpenShell Gateway；沙盒內為 placeholder | 專案專屬、設預算上限、季度輪替 |
| 託管 MCP Token | 只記錄名稱與擁有者；值由 Gateway 保管 | 唯讀 scope 優先 |
| Web Search Key | 沙盒專屬 Provider；變更需重建 | 非必要不開 |
| 訊息通道 Token（Slack 等） | Gateway 保管；登錄檔只存 SHA-256 | ⛔ 企業預設禁止訊息通道 |
| GitHub Token | NemoClaw 不保存；需要時呼叫 `gh auth token` | 用 OS keychain；限單一 repo |
| SSH 私鑰 | 沒有內建機制 | ⛔ 不得放進沙盒；Git 一律走 HTTPS＋受控 Token |
| 舊版 `~/.nemoclaw/credentials.json` | 早期版本以明文 JSON（權限 0600）儲存；升級後第一次 onboarding 自動遷移 | 遷移後確認檔案已移除或清空（🧪） |

憑證輪替與緊急處置（📖 Credential Rotation）：

```bash
# 🖥️ Host：輪替推理 Key（沿用既有沙盒）
printf 'New NVIDIA inference API key: ' >&2
IFS= read -r -s NVIDIA_INFERENCE_API_KEY; printf '\n' >&2
export NVIDIA_INFERENCE_API_KEY
nemoclaw onboard --name dev-order --non-interactive --yes --yes-i-accept-third-party-software
unset NVIDIA_INFERENCE_API_KEY

# 驗證新 Key 真的能用（status 會實際送推理請求；credentials list 只證明 Provider 存在）
nemo-deepagents dev-order status
```

外洩時的處置順序（官方 Emergency Rotation）：

1. **先**在上游供應商撤銷外洩的憑證——不要依賴本機清理。
2. 推理或 Web Search：若沒有立即可用的替代 Key，`nemoclaw credentials reset <Provider 名稱>` 移除。
3. 訊息通道：`channels remove` 或以新憑證重新 onboarding。
4. 🏢 依 13.9 通報資安，保存 `debug` 診斷包與 `logs` 輸出。

### 6.7 Prompt Injection、惡意程式碼與不可信文件

Agent 讀到的每一份文件、網頁、Issue、套件 README、程式碼註解，都可能夾帶指令。沙盒不能阻止 Agent「被說服」，只能縮小「被說服之後能做什麼」。

| 攻擊情境 | 例子 | 沙盒擋得住嗎 | 補強控制（🏢） |
|---|---|---|---|
| 文件夾帶「把 .env 貼到某網址」 | 待分析的舊系統 README 有隱藏指令 | 目的地未核准則擋（CONNECT 403） | 不在沙盒放 `.env`；拒絕 TUI 中的未知請求 |
| 利用已核准端點外送 | 指示 Agent 建立公開 GitHub Gist 或 repo | ❌ 若 `github.com` 為 `access: full` 則擋不住 | 排除 Deep Agents 的 `github` 基準項目，改用內部 Git 精確路徑（6.11） |
| 惡意套件 | 依賴混淆（dependency confusion）的 npm 套件 | ❌ 若 `npm` preset 已開 | 改走企業代理庫並開啟掃描；Restricted 層 |
| 誘導執行破壞性指令 | 「請執行 `rm -rf /sandbox/work`」 | 只能影響沙盒內 | Deep Agents 互動模式逐次核准 shell；工作副本可丟棄 |
| 竄改測試讓 CI 綠燈 | 刪除失敗的測試或加 `@Disabled` | ❌ 屬內容層 | 7.10 交付報告比對＋人工 review |
| 在程式碼植入後門 | 加一條未授權的 API 路由 | ❌ 屬內容層 | Code Review、SAST、架構測試 |

> ✅ **建議**：把「Agent 會讀到的不可信內容」與「Agent 能寫出去的通道」分開。逆向工程時原始碼唯讀掛入、網路只開推理；開發時只開專案 repo 與內部代理庫。兩者同時寬鬆時風險最大。

### 6.8 透過允許的網路外洩資料

官方原則：*Each allowed endpoint is a potential data exfiltration path.* 實務上要逐條問三個問題：

1. **這條規則允許「寫」嗎？**（`POST`、`PUT`、`PATCH`、`DELETE`、L4 `access: full`）
2. **寫的對象是誰能看到的？**（公開 SaaS、內部系統、自己的 repo）
3. **哪些程式能用？**（只有 `git`？還是任何 Python 腳本？）

| 常見規則 | 外洩風險 | 收斂方式 |
|---|---|---|
| Deep Agents 基準的 `github.com`／`api.github.com` `access: full` | 可推送到任何 GitHub repo、建立 Gist | `policy exclude github`，改用內部 Git preset |
| `pypi` preset 的 binaries 包含 `python3*` | 沙盒內任何 Python 腳本都能連 PyPI | PyPI 只開 GET／HEAD（官方 preset 已是如此）；上傳路徑不開 |
| 官方 `outlook` preset 允許 `graph.microsoft.com` 的 `PATCH /**` | 可修改信箱資料 | Open 層才有；企業不用 Open |
| 推理服務本身 | Prompt 內容就是外送資料 | 依資料分級選擇私有或外部模型（13.6） |
| Personal 層 | 任何 80／443 目的地 | ⛔ 禁用 |

### 6.9 套件安裝、依賴下載與供應鏈攻擊

| 供應鏈環節 | NemoClaw 的現況 | 企業補強 |
|---|---|---|
| 安裝程式 | HTTPS 下載；payload 只檢查 shebang | 4.3 的下載審查與固定版本 |
| OpenShell 執行檔 | 安裝時比對官方 checksum 檔；`strings` 驗證 | 內部鏡像時保留 checksum |
| 沙盒映像檔 | `@sha256` digest 釘選；三個 Agent 映像檔需屬同一發佈批次 | 企業 registry 代理不得改寫 digest |
| 自訂映像檔（`--from`） | 由你負責；NemoClaw 只做 secret-safety 排除（`.env*`、`.ssh/`、`*.pem`、`*.key` 等不進 build context） | 映像檔掃描（Trivy 等）、SBOM（CycloneDX／SPDX）、簽章 |
| 執行期套件安裝（npm、pip、brew） | Balanced 層預設開 `npm`、`pypi`、`brew-balanced` | Restricted 層＋內部代理庫 preset；官方也建議能在建置期裝的就不要在執行期裝 |
| 本地模型映像檔 | v0.0.139 起 llama.cpp 映像檔有 Sigstore 簽章 | 驗證簽章後再使用（🧪） |

參考標準：[SLSA](https://slsa.dev/)、[NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)、[CycloneDX](https://cyclonedx.org/)。

### 6.10 稽核日誌、異常監控與事件處理

| 資料來源 | 取得方式 | 內容 | 限制 |
|---|---|---|---|
| 生命週期與 Gateway 日誌 | `nemoclaw <名稱> logs` | onboarding、Gateway、政策拒絕 | 拒絕紀錄可讀性仍在改善（issue #4760） |
| 即時網路活動 | `openshell term` | 主機、連接埠、程式、方法 | 互動式，不是長期儲存 |
| OpenClaw 對話 | `nemoclaw <名稱> sessions export --format tar --out x.tgz` | session JSONL、trajectory | 需手動逐沙盒匯出 |
| Hermes 狀態 | `nemoclaw <名稱> sessions export` | 單一 JSONL | 同上 |
| Deep Agents 追蹤 | `--observability` 送 OTLP 到主機端 collector | 有界內容的 trace | 內容可能含敏感資料；本地接收端無驗證 |
| 診斷包 | `nemoclaw debug --output` | 系統、Docker、Gateway | 上傳前要檢查 |

```mermaid
flowchart TD
    A["偵測<br/>CONNECT 403 異常增加、未知 binary、推理費用暴增"] --> B["遏止<br/>nemoclaw 名稱 stop"]
    B --> C["保全證據<br/>logs、debug 診斷包、sessions export"]
    C --> D{"憑證可能外洩？"}
    D -- 是 --> E["上游撤銷憑證<br/>credentials reset"]
    D -- 否 --> F["分析<br/>政策、核准紀錄、Agent 對話"]
    E --> F
    F --> G["根因修正<br/>收斂 preset、更新規範"]
    G --> H["復原<br/>rebuild 或 destroy 後重建"]
    H --> I["事後檢討<br/>更新 13.11 允許／禁止表"]
```

> 🏢 **企業建議**：在主機上以 cron 每小時執行 `nemoclaw <名稱> logs --since 1h` 並轉送到企業日誌平台（🧪 輸出格式未保證穩定，解析前需實測）。官方目前把 SIEM 整合列為 *Manual or admin-only*。

### 6.11 教學用最小權限政策範例

**情境**：開發沙盒 `dev-order` 要讓 Deep Agents Code 開發 `order-service`。需求只有三項：

1. 從內部 Nexus 的 `maven-public` 代理庫**讀取** Maven 依賴。
2. 從內部 Git **clone／fetch** `demo/order-service` 這一個 repo。
3. 推送到同一 repo——**寫入權限另外申請、預設不套用**。

設計原則：一個 preset 一個用途；讀與寫拆成不同 preset；路徑寫到 repo 層級；程式只放行真正發起連線的那一個。

```yaml
# presets/corp-maven-readonly.yaml（🏢 企業自訂；✅ 已通過 6.16 lint）
preset:
  name: corp-maven-readonly
  description: "內部 Nexus Maven 代理庫（唯讀）；核准單 CHG-2026-0412"
network_policies:
  corp_maven_readonly:
    name: corp_maven_readonly
    endpoints:
      - host: nexus.corp.example
        port: 443
        protocol: rest
        enforcement: enforce
        rules:
          - allow: { method: GET, path: "/repository/maven-public/**" }
          - allow: { method: HEAD, path: "/repository/maven-public/**" }
    binaries:
      - { path: /usr/lib/jvm/java-21-openjdk-amd64/bin/java }
```

```yaml
# presets/corp-git-order-read.yaml（🏢 企業自訂；✅ 已通過 6.16 lint）
preset:
  name: corp-git-order-read
  description: "內部 Git：order-service 唯讀（clone／fetch）"
network_policies:
  corp_git_order_read:
    name: corp_git_order_read
    endpoints:
      - host: git.corp.example
        port: 443
        protocol: rest
        enforcement: enforce
        rules:
          - allow: { method: GET, path: "/scm/demo/order-service.git/info/refs" }
          - allow: { method: POST, path: "/scm/demo/order-service.git/git-upload-pack" }
    binaries:
      - { path: /usr/bin/git }
```

```yaml
# presets/corp-git-order-write.yaml（🏢 企業自訂；需另經核准才套用）
preset:
  name: corp-git-order-write
  description: "內部 Git：order-service 推送（需另經核准）"
network_policies:
  corp_git_order_write:
    name: corp_git_order_write
    endpoints:
      - host: git.corp.example
        port: 443
        protocol: rest
        enforcement: enforce
        rules:
          - allow: { method: POST, path: "/scm/demo/order-service.git/git-receive-pack" }
    binaries:
      - { path: /usr/bin/git }
```

**逐欄解說**：

| 欄位 | 寫法 | 為什麼 |
|---|---|---|
| `preset.name` | 小寫 RFC 1123 label，且不與官方 preset 同名 | 官方規則；檔名（去掉 `.yaml`）要與 `preset.name` 一致才能用名稱套用 |
| `network_policies` 的 key | 用底線（`corp_maven_readonly`） | 與官方 preset 慣例一致；`npm_yarn`、`personal_open_internet` 是保留鍵 |
| `protocol: rest`＋`enforcement: enforce` | 明確寫出 | 沒寫 `protocol` 就只有 L4；🏢 本手冊一律明寫 `enforce`，不依賴預設值 |
| 讀寫分離 | Git 的 smart HTTP：讀＝`GET …/info/refs`＋`POST …/git-upload-pack`；寫＝`POST …/git-receive-pack` | 只套用讀 preset 時，Agent 無法 `git push` |
| 路徑到 repo 層級 | `/scm/demo/order-service.git/…` | 其他 repo 一律拒絕；換專案就另一份 preset |
| `binaries` | 只放 `git`；Maven 放 `java` | Maven 的 `mvn` 是腳本，實際連線的程序是 `java`；OpenShell 看的是 `/proc/<pid>/exe` |
| 不寫 `allowed_ips` | 改在套用時用 `--trusted-private-host` | 官方禁止自訂 preset 宣告 `allowed_ips`；NemoClaw 會解析並把位址釘死 |

> 🧪 **待驗證**：(1) Git 的 `info/refs` 請求帶查詢字串 `?service=git-upload-pack`，路徑規則是否只比對路徑部分，需實機確認；(2) `java` 的實際路徑取決於自訂映像檔（7.3）；(3) Git 用 `git-remote-https` 子程序連線，政策以祖先程式 `git` 比對（官方 `github` preset 也只列 `/usr/bin/git`），但請以 `openshell term` 回報的 binary 為準。

> ⚠️ **新增網路目的地的風險**：每加一條端點，就問 6.8 的三個問題，並在申請單（13.4）寫明「允許的方法、路徑、程式、資料敏感度、到期日」。內部系統一樣算外洩通道——內部 Wiki 允許 `POST`，Agent 就能把程式碼貼上去。

### 6.12 套用與驗證政策

```bash
# 🖥️ Host：1. 靜態檢查（6.16）
python3 nemoclaw-policy-lint.py preset presets/corp-*.yaml

# 2. 預覽（私有主機必須明確信任；dry-run 會顯示產生的位址釘選）
nemo-deepagents dev-order policy add \
  --from-file presets/corp-maven-readonly.yaml \
  --trusted-private-host nexus.corp.example --dry-run

# 3. 套用唯讀 preset
nemo-deepagents dev-order policy add --from-file presets/corp-maven-readonly.yaml \
  --trusted-private-host nexus.corp.example --yes
nemo-deepagents dev-order policy add --from-file presets/corp-git-order-read.yaml \
  --trusted-private-host git.corp.example --yes

# 4. 確認生效
nemo-deepagents dev-order policy list
openshell policy get dev-order | grep -A3 corp_
```

驗證「該通的通、不該通的不通」（📦 透過 `exec` 執行；🧪 輸出依環境）：

| # | 測試 | 指令（`nemo-deepagents dev-order exec -- bash -lc '…'`） | 預期 |
|---|---|---|---|
| V1 | 允許的 repo 可 clone | `git clone https://git.corp.example/scm/demo/order-service.git /sandbox/work/order-service` | 成功 |
| V2 | 其他 repo 被拒 | `git ls-remote https://git.corp.example/scm/demo/payment.git` | `CONNECT tunnel failed, response 403` 或 HTTP 403 |
| V3 | 推送被拒（未套用寫入 preset） | `cd /sandbox/work/order-service && git push origin HEAD:ai/test` | 被拒 |
| V4 | 允許的程式以外被拒 | `curl -sS https://nexus.corp.example/repository/maven-public/` | 被拒（`curl` 不在 binaries） |
| V5 | 未列出主機被拒 | `curl -sS https://example.com` | 被拒 |
| V6 | 拒絕有紀錄 | 🖥️ `nemo-deepagents dev-order logs --tail 50` | 看得到 V2～V5 的拒絕 |

> ✅ **建議**：把 V1～V6 寫成腳本，每次修改 preset 後重跑，結果附在變更單上。只測「能通」不測「不能通」的政策驗收，不算完成。

### 6.13 政策更新是增量還是整份替換

這是最常出錯的地方。四種方式的語意不同：

| 方式 | 語意 | 保存在哪 | 刪除重建後 |
|---|---|---|---|
| `nemoclaw <名稱> policy add <preset>` 或 `--from-file` | **增量**：把 preset 以命名空間化的 key 合併進即時政策；同名且內容相同則不變，不同則預覽後再套用 | OpenShell 即時政策 | 若用 onboarding 重建會回到所選層級＋preset；`rebuild` 會整份帶過去 |
| `openshell term` 核准 | **增量**：合併為新的政策版本 | OpenShell 即時政策 | 消失 |
| `openshell policy update <沙盒> --add-endpoint host:443:read-only:rest:enforce` | **增量**（OpenShell CLI 的動態變更，官方 Network Policies 頁範例） | OpenShell 即時政策 | 消失 |
| `openshell policy set --policy <檔> --wait <沙盒>` | **整份替換**：不合併，檔案裡沒有的項目全部消失 | OpenShell 即時政策（成為持久的即時政策） | 依重建方式 |
| 修改 Blueprint 基準政策檔後 `nemoclaw onboard` | 改變**未來**沙盒的基準 | 原始碼樹 | 生效 |

> ⚠️ **警告（整份替換）**：官方 Replace the Live Network Policy 頁原文：*Applying a file that contains only one part silently removes the other entries.* 正確流程是：`nemoclaw <名稱> policy get > current-policy.yaml`（不要加 `--raw`）→ 只在 `network_policies` 下新增 → 把每一個 `[STRIPPED_BY_MIGRATION]` 換回正確的 OpenShell 憑證綁定或 resolver placeholder → `openshell policy set`。`openshell policy set` **不接受** preset 格式（`preset:` 開頭）的檔案。`managed_inference` 項目不可移除。

### 6.14 哪些設定可執行期更新、哪些必須重建

| 設定 | 生效方式 | 操作 |
|---|---|---|
| 網路 preset | 執行期，下一個請求生效 | `policy add`／`remove` |
| 網路允許清單（單一端點） | 執行期 | `openshell term` 核准或 `openshell policy update` |
| 推理模型（同 Provider） | 執行期（OpenClaw／Hermes） | `inference set` |
| 推理 Provider | 執行期路由更新，必要時重建映像檔 | `inference set`；Deep Agents 需重新 onboarding |
| 託管 MCP 的 deny-tool | 執行期 | `mcp update` |
| Gateway 程序環境、只在啟動讀取的 plugin 狀態 | 重啟 Gateway 後 | `gateway restart` |
| Dashboard 轉送連接埠 | 下次 `connect` | `NEMOCLAW_DASHBOARD_PORT=<port> nemoclaw <名稱> connect` |
| Dashboard 綁定位址 | 需重建 | `NEMOCLAW_DASHBOARD_BIND=0.0.0.0 nemoclaw onboard --recreate-sandbox`（⛔ 企業不開） |
| 訊息通道新增、啟用、停用、Token | 需重建 | `channels add`／`stop`／`start` 後接受重建 |
| Web Search Provider | 需重建 | 重新 onboarding 並重建 |
| 檔案系統配置 | **建立時鎖定** | `onboard --recreate-sandbox` |
| 程序控制（seccomp、使用者） | **建立時鎖定** | 重建 |
| 沙盒名稱 | 建立時鎖定 | 以新名稱 onboarding |
| GPU 直通 | 建立時鎖定 | `--gpu`／`--sandbox-gpu-device` 重新 onboarding |
| 企業 Proxy（`NEMOCLAW_PROXY_HOST`） | 建置期 | 重新 onboarding |
| 企業 CA | 建置期 | `rebuild` |
| Deep Agents 自動核准能力 | 建置期（烤進唯讀檔） | `rebuild --dcode-auto-approval …` |
| `--host-mount` | 建立時 | 重新 onboarding |

**來源**：[Understand Runtime Changes](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/configure-sandboxes/understand-runtime-changes)、[How It Works — Protection Layers](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/about/how-it-works)

### 6.15 不同 Agent 的政策差異

不可假設三個 Agent 能套用完全相同的政策：

| 面向 | OpenClaw | Hermes | Deep Agents Code |
|---|---|---|---|
| 基準政策檔 | `nemoclaw-blueprint/policies/openclaw-sandbox.yaml` | `agents/hermes/policy-additions.yaml` | `agents/langchain-deepagents-code/policy-additions.yaml` |
| 基準網路項目 | `nvidia`、`managed_inference`、`clawhub`、`openclaw_api`、`openclaw_docs`、`npm_registry` | `managed_inference`、`nvidia`、`nous_research`、`pypi` | `managed_inference`、`observability-otlp-local`、`github`（`access: full`）、`pypi` |
| 可排除的基準項目（`policy exclude`） | `nvidia`、`clawhub`、`openclaw_api`、`openclaw_docs`、`npm_registry` | `nvidia`、`nous_research`、`pypi` | `github`、`observability-otlp-local`、`pypi` |
| 不可排除 | `managed_inference` | `managed_inference` | `managed_inference` |
| 發起連線的程式 | `/usr/local/bin/openclaw`、`node` | Hermes 的 Python | `/usr/local/bin/dcode`、`/opt/venv/bin/python3*` |
| 自訂 preset 的 binaries | 用 `openshell term` 回報的路徑 | 同左 | 官方提醒常見為 `/usr/local/bin/dcode` 或 `/opt/venv/bin/python3*`（後者等於所有沙盒內 Python） |
| 訊息通道 preset | 支援 | 支援 | 不適用（沒有訊息 bridge） |

可排除清單出自 v0.0.139 `src/lib/policy/baseline-exclusion.ts`（📖）。沒有列在清單裡的基準項目，`policy exclude` 會拒絕。

### 6.16 審查 AI 產出的政策

讓 AI 幫忙寫 preset 很有效率，但 AI 的預設傾向是「先讓它能動」。以下教你三步審查：工具快篩 → 人工逐條 → 拒絕測試。

**1. 工具快篩：`nemoclaw-policy-lint.py`（✅ 已實測）**

本手冊附的 🏢 企業自訂 lint 工具（完整原始碼見 18.10.1），規則如下：

| 規則 | 等級 | 檢查 |
|---|---|---|
| N01 | ERROR／WARN | `preset.name` 非 RFC 1123、與官方同名；缺 description |
| N02 | ERROR | 使用官方保留鍵 `npm_yarn`、`personal_open_internet` |
| N03 | ERROR | host 為 `*`、`0.0.0.0`、CIDR、或萬用字元只到頂級網域（`*.com`） |
| N04 | ERROR | 自訂 preset 宣告 `allowed_ips` |
| N05 | WARN／ERROR | 沒有 `binaries`（規則不授權任何程式）；沒有 `network_policies` |
| N06 | WARN | 沒有 `protocol`（L4-only） |
| N07 | ERROR | 有 `protocol` 卻沒寫 `enforcement: enforce`，或沒有 `rules` |
| N08 | ERROR／WARN | `method: "*"`；`PUT`／`PATCH`／`DELETE` 配 `/**`；`POST /**` |
| N10 | ERROR／WARN | binaries 為 `/**`、`/usr/bin/*` 等；直譯器（`python3*`、`node`、`curl`） |
| N11 | ERROR | 疑似明文憑證（`nvapi-`、`sk-`、`ghp_`、`xoxb-`、`AKIA`、`Bearer …`） |
| N12 | ERROR | 仍有 `[STRIPPED_BY_MIGRATION]` |
| N13 | ERROR | 整份 policy 模式：缺 `version`、是 preset 格式、缺 `managed_inference` |
| N14 | WARN | `tls: skip` |

❌ **壞例**（AI 在「讓 Agent 能呼叫內部 API」的要求下產生；只用於審查訓練）：

```yaml
# 壞例：AI 產生的「先讓它能動」preset，只用於審查訓練
preset:
  name: Corp_API
network_policies:
  npm_yarn:
    name: npm_yarn
    endpoints:
      - host: "*"
        port: 443
      - host: api.corp.example
        port: 443
        protocol: rest
        allowed_ips: ["10.0.0.0/8"]
        rules:
          - allow: { method: "*", path: "/**" }
          - allow: { method: DELETE, path: "/**" }
    binaries:
      - { path: "/**" }
  helper:
    name: helper
    endpoints:
      - host: "*.com"
        port: 443
        protocol: rest
        enforcement: enforce
        headers: { Authorization: "Bearer abcdefghijklmnopqrstuvwxyz123456" }
        rules:
          - allow: { method: POST, path: "/**" }
    binaries:
      - { path: /usr/bin/curl }
```

🔍 執行 lint（✅ 實際輸出）：

```text
$ python3 nemoclaw-policy-lint.py preset bad-preset.yaml
ERROR N11 bad-preset.yaml network_policies.helper.endpoints[0].headers.Authorization: 疑似明文憑證；改用 OpenShell provider／placeholder
ERROR N01 bad-preset.yaml preset.name: 'Corp_API' 不是小寫 RFC 1123 label
WARN  N01 bad-preset.yaml preset.description: 缺少 description（審查與 policy list 時難以辨識）
ERROR N02 bad-preset.yaml network_policies.npm_yarn: 'npm_yarn' 是官方保留鍵
ERROR N10 bad-preset.yaml network_policies.npm_yarn: binary '/**' 範圍過大
ERROR N03 bad-preset.yaml network_policies.npm_yarn.endpoints[0]: host '*' 是全開或 CIDR 目的地，官方會拒絕
WARN  N06 bad-preset.yaml network_policies.npm_yarn.endpoints[0]: '*' 沒有 protocol（L4-only，access=None）；只看主機與程式，不檢查方法與路徑
ERROR N04 bad-preset.yaml network_policies.npm_yarn.endpoints[1]: 自訂 preset 不得宣告 allowed_ips（改用 --trusted-private-host）
ERROR N07 bad-preset.yaml network_policies.npm_yarn.endpoints[1]: 'api.corp.example' 有 protocol 但未明確寫 enforcement: enforce
ERROR N08 bad-preset.yaml network_policies.npm_yarn.endpoints[1].rules[0]: 'api.corp.example' method '*' 等於允許所有方法
ERROR N08 bad-preset.yaml network_policies.npm_yarn.endpoints[1].rules[1]: 'api.corp.example' DELETE /**：寫入／刪除方法不可配全路徑
WARN  N10 bad-preset.yaml network_policies.helper: binary '/usr/bin/curl' 是直譯器或通用下載工具，等於沙盒內任何腳本都能用
ERROR N03 bad-preset.yaml network_policies.helper.endpoints[0]: host '*.com' 萬用字元範圍過大（只到頂級網域）
WARN  N08 bad-preset.yaml network_policies.helper.endpoints[0].rules[0]: '*.com' POST /**：請收斂到實際 API 路徑
結果：10 ERROR，4 WARN
```

好例（6.11 的三份 preset）的輸出是 `結果：0 ERROR，0 WARN`，結束碼 `0`。整份 policy 模式的壞例（只放新端點就要 `policy set`、還留著 `[STRIPPED_BY_MIGRATION]`）會得到 `N12` 與 `N13` 兩個 ERROR。

> 📌 **註記**：拿官方 preset 跑這支工具，一定會出現 `N01`（因為與官方同名）——工具只用於**自訂** preset。它也會對官方 preset 標出值得注意的寬鬆處，例如 `pypi` 的 binaries 包含 `python3*`（N10 WARN）、`outlook` 的 `PATCH /**`（N08 ERROR）、Deep Agents 基準的 `github` 為 L4（N06 WARN）。這些是官方的設計取捨，企業要知情後再決定是否採用。

**2. 人工逐條審查清單**：

- [ ] 每個 host 都有申請單，且是精確主機名（不是 `*.corp.example`）。
- [ ] 每條 `rules` 的方法與路徑都能對應到實際需要的 API；`POST` 有理由。
- [ ] 讀與寫分在不同 preset；寫入 preset 有獨立核准。
- [ ] binaries 只有真正發起連線的程式；不含 `python3*`、`node`、`curl`，除非有理由。
- [ ] 沒有 `allowed_ips`、沒有 `tls: skip`、沒有任何憑證字串。
- [ ] 私有主機在套用時以 `--trusted-private-host` 指定，並在 dry-run 輸出中確認釘選的位址正確。

**3. 拒絕測試**：6.12 的 V1～V6 全部符合預期，才可在變更單上簽核。

### 6.17 安全公告與弱點修補管理

NemoClaw 與 OpenShell 都在快速迭代，漏洞會集中公告。2026-08-25，NVIDIA Product Security 發布 **Security Bulletin 5872**（*Security Bulletin: NVIDIA NemoClaw and OpenShell - August 2026*），一次公告 18 個 CVE。以下依官方 CSAF 原始資料（`NVIDIA/product-security` 儲存庫的 `2026/5872`）整理：

| CVE | 元件 | 弱點類型（CWE） | CVSS 3.1 | 受影響版本 |
|---|---|---|---|---|
| CVE-2026-65093 | OpenShell | 沙盒逃逸（CWE-427） | 9.9 Critical | 0～0.0.33 |
| CVE-2026-65083 | OpenShell | 沙盒建立 API 的禁止清單不完整（CWE-184） | 9.9 Critical | 0～0.0.33 |
| CVE-2026-65091 | OpenShell | 惡意 Gateway 造成 OS 指令注入（CWE-78） | 8.8 High | 0～0.0.33 |
| CVE-2026-65092 | OpenShell | 以路徑穿越繞過 L7 REST 網路政策（CWE-22） | 8.5 High | 0～0.0.33 |
| CVE-2026-65086 | OpenShell | 沙盒 exec 處理器指令注入（CWE-78） | 6.8 Medium | 0～0.0.33 |
| CVE-2026-65085 | OpenShell | 推理代理輸出編碼不當（CWE-116） | 5.2 Medium | 0～0.0.33 |
| CVE-2026-65105 | NemoClaw | 推理服務未驗證即可存取（CWE-306，相鄰網路） | 8.1 High | 0～0.0.25 |
| CVE-2026-65098 | NemoClaw | 遠端存取輔助流程的弱驗證（CWE-1390） | 8.1 High | 0～0.0.4 |
| CVE-2026-65084 | NemoClaw | 部署流程憑證驗證不當（CWE-295） | 8.1 High | 0～0.0.1 |
| CVE-2026-65081 | NemoClaw | 安裝流程執行不受信任的程式碼（CWE-494） | 8.1 High | 0～0.0.21 |
| CVE-2026-65099 | NemoClaw | CLI 指令注入（CWE-78） | 7.8 High | 0～0.0.1 |
| CVE-2026-65096 | NemoClaw | Telegram bridge 指令注入（CWE-78） | 7.8 High | 0～0.0.1 |
| CVE-2026-65090 | NemoClaw | NIM 管理元件指令注入（CWE-78） | 7.8 High | 0～0.0.17 |
| CVE-2026-65089 | NemoClaw | `status`／`logs` 外掛指令注入（CWE-78） | 7.8 High | 0～0.0.3 |
| CVE-2026-65097 | NemoClaw | 安裝腳本下載程式碼未做完整性檢查（CWE-494） | 7.5 High | 0～0.0.21 |
| CVE-2026-65082 | NemoClaw | 遷移指令程式碼注入（CWE-94） | 7.0 High | 0～0.0.17 |
| CVE-2026-65087 | NemoClaw | 憑證保護不足（CWE-522） | 5.6 Medium | 0～0.0.1 |
| CVE-2026-65088 | NemoClaw | 以可見的敏感資訊啟動程序（CWE-214） | 5.5 Medium | 0～0.0.17 |

本手冊基準 NemoClaw v0.0.139／OpenShell 0.0.116 都高於所有受影響範圍。這張表的價值在於提醒我們三件事：

| 從公告學到的 | 對應的本手冊控制 |
|---|---|
| 兩個 CWE-494（安裝時執行或下載未驗證的程式碼） | 4.3「先下載、比對、審查，再固定版本執行」不是多餘的程序 |
| CWE-22 可以繞過 L7 路徑規則 | 不要只靠路徑規則保護敏感 API；Git 寫入 preset 之外，還要搭配 Token 權限（6.11、14.4） |
| CWE-306 推理服務未驗證（相鄰網路） | 本地推理服務只綁 loopback，主機防火牆擋掉同網段（3.4、14.6） |

> 📌 **註記**：公告的「Updated Version」欄寫法不一致。例如 CVE-2026-65105 的受影響範圍是 `0 to 0.0.25`，修補欄卻寫 `f06796ff3; 0.0.25`。遇到這種模稜兩可的寫法，以保守方式解讀：版本必須**高於**受影響範圍的上限。

#### 6.17.1 版本下限檢查腳本

`check-security-floor.sh`（🏢 本手冊自行撰寫；✅ 版本比較邏輯已用假的 `nemoclaw`／`openshell` 指令實測；🧪 實機的 `--version` 輸出格式以實際為準）：

```bash
#!/usr/bin/env bash
# check-security-floor.sh — 🏢 確認主機上的 NemoClaw／OpenShell 高於已知安全公告的受影響範圍（唯讀）
# 基準：NVIDIA Security Bulletin 5872（2026-08-25）。有新公告時，只改下面兩個值並走 PR。
NEMOCLAW_MIN=0.0.26    # 公告中 NemoClaw 受影響範圍最高到 0.0.25 → 至少要 0.0.26
OPENSHELL_MIN=0.0.34   # 公告中 OpenShell 受影響範圍最高到 0.0.33，修補版 v0.0.34
ver_ge() { [ "$(printf '%s\n%s\n' "$1" "$2" | sort -V | head -n1)" = "$2" ]; }   # $1 >= $2
extract() { grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1; }
rc=0
check() {  # 名稱 實際版本 最低版本
  if [ -z "$2" ]; then echo "UNKNOWN  $1：讀不到版本"; rc=1
  elif ver_ge "$2" "$3"; then echo "OK       $1 $2（>= $3）"
  else echo "VULN     $1 $2（< $3，依公告 5872 升級）"; rc=1; fi
}
check nemoclaw  "$(nemoclaw --version 2>/dev/null | extract)"  "$NEMOCLAW_MIN"
check openshell "$(openshell --version 2>/dev/null | extract)" "$OPENSHELL_MIN"
exit $rc
```

實測輸出（✅ 以假指令模擬三種主機）：

```text
--- 假設 nemoclaw=0.0.139 openshell=0.0.116
OK       nemoclaw 0.0.139（>= 0.0.26）
OK       openshell 0.0.116（>= 0.0.34）
exit=0
--- 假設 nemoclaw=0.0.25 openshell=0.0.33
VULN     nemoclaw 0.0.25（< 0.0.26，依公告 5872 升級）
VULN     openshell 0.0.33（< 0.0.34，依公告 5872 升級）
exit=1
--- 假設 nemoclaw=0.0.9 openshell=0.0.100
VULN     nemoclaw 0.0.9（< 0.0.26，依公告 5872 升級）
OK       openshell 0.0.100（>= 0.0.34）
exit=1
```

**審查 AI 寫的版本比較程式時，最常見的錯誤**：

| ❌ 壞例 | 為什麼錯 | 🔍 怎麼抓 |
|---|---|---|
| `[[ "$v" > "0.0.34" ]]` 字串比較 | 字串比較會判定 `0.0.100` < `0.0.34`、`0.0.9` > `0.0.26` | 用上面第三組測資（`0.0.9`、`0.0.100`）跑一次 |
| 讀不到版本時當成通過 | `openshell` 不在 PATH 時會靜默放行 | 刪掉假的 `openshell` 再跑，必須出現 `UNKNOWN` 且結束碼 1 |
| 把下限寫成公告的「修補版」欄位 | 修補欄寫法不一致（見上方註記） | 對照公告的「Affected Versions」欄重算 |

#### 6.17.2 企業的弱點管理流程（🏢）

| 步驟 | 做法 | 驗證方式 |
|---|---|---|
| 1. 訂閱 | 平台管理者訂閱 [NVIDIA Product Security](https://www.nvidia.com/en-us/security/) 公告，並 watch [NVIDIA/product-security](https://github.com/NVIDIA/product-security) 儲存庫（提供機器可讀的 CSAF JSON） | 訂閱紀錄截圖存檔 |
| 2. 判定 | 公告發布後 1 個工作天內，比對核准版本與受影響範圍 | 判定結果寫入維護紀錄表（12.10） |
| 3. 盤點 | 對所有主機執行 `check-security-floor.sh`（更新下限後） | 結束碼 0 的主機數 ÷ 總主機數 |
| 4. 修補時限 | Critical：7 天；High：30 天；Medium：90 天（🏢 依企業弱點管理政策調整） | 逾期主機清單 |
| 5. 無法如期修補 | 停用該主機上的沙盒（`nemoclaw <名稱> stop`），走 14.12 風險接受 | 簽核單 |

### 6.18 對照 OWASP Top 10 for Agentic Applications 2026

OWASP GenAI Security Project 在 2025-12-09 發布 *OWASP Top 10 for Agentic Applications for 2026*（ASI01～ASI10），是目前最常被稽核引用的 Agent 風險清單。下表把每一項對到 NemoClaw 的控制與本手冊章節，並寫出**沙盒管不到、要靠企業補強**的部分：

| 編號 | 風險 | NemoClaw／OpenShell 的控制 | 管不到的部分（企業補強） | 🔍 怎麼驗證 |
|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | 網路預設拒絕，限制被劫持後能把資料送去哪裡（6.3） | 沙盒不判斷意圖；被文件裡的指令誘導改程式，仍可能發生（6.7） | 16.1 演練 0 的 Prompt Injection 題目 |
| ASI02 | Tool Misuse & Exploitation | Deep Agents 互動模式逐次核准；`dcode -n` 停用 shell（5.6） | 核准者沒看清楚就按下核准 | 抽查核准紀錄；見下方「核准卡路徑」註記 |
| ASI03 | Identity & Privilege Abuse | 憑證放在 Gateway，沙盒內只有 placeholder（6.6） | Provider 是 Gateway 範圍，同一主機的沙盒共用（14.4）；Git Token 權限要另外收斂 | 13.5 的 placeholder 檢查；用 AI Token 推送 `main` 應被拒絕 |
| ASI04 | Agentic Supply Chain Vulnerabilities | 映像檔以 digest 釘選；OpenShell 版本鎖定（12.1） | 安裝腳本與套件來源要自己審查（4.3、6.9） | 4.3 的 `diff -q`；6.17 公告中的 CWE-494 案例 |
| ASI05 | Unexpected Code Execution (RCE) | Landlock、seccomp、非 root、唯讀系統路徑（6.2、6.4） | 程式碼在 CI 執行時已離開沙盒 | 4.10 控制有效性驗證；CI Runner 也要隔離 |
| ASI06 | Memory & Context Poisoning | 無直接控制；`rebuild` 會完整保留 Agent 的原生 home | `AGENTS.md`、Agent 記憶檔被改了也會一路帶下去 | PR 審查必看 `AGENTS.md` 的 diff；敏感專案定期重建全新沙盒 |
| ASI07 | Insecure Inter-Agent Communication | 一個沙盒只跑一種 Agent | 訊息通道（Telegram、Slack 等）是對外入口；6.17 表中的 CVE-2026-65096 就發生在 Telegram bridge | `nemoclaw <名稱> channels list` 應為空（🏢 企業預設不開通道） |
| ASI08 | Cascading Failures | 無；同一主機的沙盒共用 Gateway 與 Provider（2.8） | 一個 Gateway 故障或一把 Key 外洩，會影響整台主機 | 2.8 故障影響分析；不同敏感等級分主機（14.4） |
| ASI09 | Human-Agent Trust Exploitation | 無 | Agent 宣稱「完成」「測試通過」 | `check-change-report.py`（7.10）、`check-test-weakening.py`（13.8） |
| ASI10 | Rogue Agents | 出口拒絕與日誌（6.10）；可隨時 `stop`／`destroy` | 偵測要靠企業日誌平台（14.7） | 14.7 偵測規則的觸發演練 |

> 📌 **註記**：v0.0.139 的 Deep Agents Code 編輯核准卡會把絕對路徑縮寫成檔名，例如對 `/tmp/square.py` 的編輯只顯示 `square.py`（`main` 的 #13591 已修正）。在 v0.0.139 上核准編輯前，先在卡片的 diff 內容或 `dcode` 的工具呼叫紀錄確認完整路徑，不要只看檔名。

> ✅ **建議**：稽核要求「Agent 風險評估」時，直接用上表當底稿：每一列都填入貴單位的實測證據（截圖、指令輸出、PR 連結）。評估重點放在「管不到的部分」那一欄，那才是企業要負責補強的地方。

### 6.19 本章實務案例與注意事項

**案例**：Agent 回報「Maven 下載依賴時 403，請幫我在政策加上 `repo.maven.apache.org`」。

錯誤處理：直接在 `openshell term` 按 `a` 核准，或請 AI 產生 `host: "*.apache.org"` 的 preset。

正確處理：

1. `nemo-deepagents dev-order logs --tail 50` 確認被拒的 host 與 binary（可能其實是 `java` 以外的程式，例如被誘導的 `curl`）。
2. 企業規範是走內部 Nexus：確認專案的 `settings.xml` 指向 `nexus.corp.example`，而不是放行公開 Maven Central。
3. 若真的需要新端點，走 13.4 白名單申請，以 6.11 格式撰寫、6.16 審查、6.12 驗證。

**注意事項**：

- `openshell term` 的核准不寫入基準政策，`destroy` 後消失；`rebuild` 則會把目前的即時政策整份帶到新沙盒。
- 政策 YAML 放進 Git（14.9），每次變更走 PR，CI 自動跑 lint。
- 本章的 Git 路徑規則與 binary 路徑標 🧪，第一次導入時務必以 V1～V6 實測。

## 第7章 使用 NemoClaw 開發 Web Application

本章以一個虛構的企業專案「訂單服務 order-service」（Vue 3＋TypeScript＋Tailwind CSS 前端、Java 21＋Spring Boot 後端、Hexagonal Architecture、PostgreSQL）為主線，建立一套可重複的 AI Agent 開發流程。重點不在「AI 能寫多少程式」，而在「怎麼讓 AI 在受控環境寫、寫完怎麼證明是對的」。

### 7.1 NemoClaw 在開發流程中的角色

| 工作 | 誰負責 | NemoClaw 的角色 |
|---|---|---|
| 隔離 Agent 的執行環境 | NemoClaw＋OpenShell | ✅ 主要價值 |
| 限制 Agent 能連的 Git、套件庫、模型 | NemoClaw preset＋OpenShell | ✅ 主要價值 |
| 寫程式、改程式 | Agent（Deep Agents Code） | 提供執行環境 |
| 編輯器、除錯器 | IDE（VS Code、IntelliJ） | ❌ 不取代 |
| 版本控制、分支、PR | Git＋Git Server | ❌ 不取代 |
| 編譯、單元測試、整合測試 | Maven／Gradle／npm、JUnit、Playwright | ❌ 不取代 |
| 品質與安全掃描 | SonarQube、SAST、SCA、Trivy | ❌ 不取代 |
| 建置與部署 | CI/CD | ❌ 不取代 |
| 架構規範 | 專案的架構文件與 ArchUnit 測試 | ❌ 不取代 |
| 決定要不要合併 | 人 | ❌ 不取代 |

> ✅ **建議**：把 NemoClaw 想成「讓 AI Coding Agent 上班的隔離辦公室」。辦公室有門禁（網路政策）、保險箱（憑證）、監視器（日誌）；但它不負責驗收產品——驗收是 CI 與 Code Review 的事。

### 7.2 選擇 Agent 與程式碼進出沙盒的方式

**Agent 選擇**：三個受支援 Agent 中，**LangChain Deep Agents Code（`dcode`）** 是官方定位的「終端機 Coding Agent」，最適合本章。OpenClaw 與 Hermes 是常駐助理型，雖然也能操作檔案，但不是為程式開發設計。

**程式碼怎麼進出沙盒**：

| 方式 | 方向 | 適用 | 評估 |
|---|---|---|---|
| 在沙盒內 `git clone` 工作副本（搭配 6.11 的 Git preset） | 雙向（push 需寫入 preset） | 開發 | ✅ **建議**：Agent 的修改只存在分支上，經 PR 才進主線 |
| `nemoclaw <名稱> upload`／`download` | 單次複製 | 規格文件、測試資料 | ✅ 簡單、可稽核 |
| `--host-mount`（唯讀） | 主機 → 沙盒 | 參考文件、舊系統原始碼 | ✅ 逆向工程首選（第 8 章）；開發時無法寫回 |
| `share mount`（SSHFS 雙向） | 雙向即時 | 與 IDE 共同編輯 | ⚠️ 主機目錄等於對 Agent 開放寫入；只掛單一工作副本，不可掛家目錄 |

```mermaid
flowchart LR
    DEV["開發者工作站<br/>IDE"] -->|"1. 撰寫規格<br/>docs/spec/*.md"| GIT["內部 Git<br/>demo/order-service"]
    GIT -->|"2. clone（讀 preset）"| SBX["沙盒 dev-order<br/>/sandbox/work/order-service"]
    SBX -->|"3. Agent 在 ai/ 分支修改"| SBX
    SBX -->|"4. push ai/ 分支（寫 preset，另經核准）"| GIT
    GIT -->|"5. 開 PR"| CI["CI/CD<br/>建置、測試、掃描"]
    CI -->|"6. 結果"| REV["人工 Code Review"]
    REV -->|"7. 合併或退回"| GIT
    DEV -.->|"8. 本機 checkout 分支驗證"| GIT
```

### 7.3 開發沙盒的工具鏈

官方受管映像檔的實際內容（📖 v0.0.139 原始碼）：

| 項目 | Deep Agents Code 受管映像 | 影響 |
|---|---|---|
| 基底 | `node:24.22.1-trixie-slim`（digest 釘選） | 有 Node.js 24 與 npm，可跑前端工具（需 npm preset 或內部代理庫） |
| Python | `/opt/venv`（唯讀，`dcode` harness 用） | 不能在 `/opt/venv` 安裝套件 |
| Git | 有 | 可 clone |
| JDK／Maven／Gradle | **沒有** | 沙盒內不能直接建置 Java |
| 編譯器（`gcc`、`make`） | 被移除 | 原生模組無法編譯 |

三種做法：

| 做法 | 說明 | 狀態 |
|---|---|---|
| A. Agent 只改碼，建置測試在 CI | Agent 推送 `ai/` 分支，由 CI 跑 `mvn verify`、`npm test`，結果回饋給開發者再交給 Agent | ✅ **起步建議**；最符合「工具負責客觀驗證」 |
| B. 由操作者用 `exec` 在沙盒跑前端測試 | 例如 `nemo-deepagents dev-order exec --workdir /sandbox/work/order-service/web -- npm test` | 🧪 需 `npm` 或內部 npm 代理 preset |
| C. 自訂映像檔加入 JDK 與 Maven | `nemoclaw onboard --from <Dockerfile>`；官方允許以受管 Dockerfile 為基礎就地修改（需在 NemoClaw 原始碼樹執行 CLI） | 🧪 進階；需自行承擔映像檔安全與相容性 |

做法 C 的 Dockerfile 片段（🧪 **未實測**；只示意要補的東西，不是完整檔案）：

```dockerfile
# 以 v0.0.139 原始碼的 agents/langchain-deepagents-code/Dockerfile 為基礎，在最後一個 stage 加入：
ARG NEMOCLAW_TOOL_DISCLOSURE=progressive
ENV NEMOCLAW_TOOL_DISCLOSURE=${NEMOCLAW_TOOL_DISCLOSURE}
# 企業 CA（官方要求自訂 Dockerfile 自行實作企業 CA 建置契約，見 3.6）
ARG NEMOCLAW_CORPORATE_CA_B64
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends openjdk-21-jdk-headless maven \
 && rm -rf /var/lib/apt/lists/*
USER sandbox
```

> ⚠️ **警告**：官方說明 `--from` 提供的 Dockerfile「定義完整映像檔」，NemoClaw **不會**疊在受管 Runtime 之上；自訂映像檔也失去官方「三個 Agent 同一發佈批次」的驗證。rootless Podman 路徑不接受自訂 Dockerfile。採用做法 C 前，先在 14 章的試行環境完成映像檔掃描與 4.10 驗收。

> 📌 **註記（審批邊界）**：Deep Agents 互動模式下，Agent 想執行 `mvn test` 這類 shell 指令會先請你核准；無頭 `dcode -n` 則**停用 shell 執行**。所以「讓 Agent 自己跑測試」只在互動模式、且你逐次核准時成立。這也是本手冊建議以 CI 作為測試真相來源的原因之一。

### 7.4 可重複的 AI Agent 開發流程

```mermaid
flowchart TD
    S0["0. 準備<br/>規格放進 docs/spec、AGENTS.md 就位"] --> S1["1. Agent 讀規格與既有程式<br/>提出計畫（不改檔）"]
    S1 --> G1{"人工核准計畫？"}
    G1 -- 修改 --> S1
    G1 -- 核准 --> S2["2. Agent 在 ai/ 分支小步實作"]
    S2 --> S3["3. Agent 補測試、執行允許的檢查"]
    S3 --> S4["4. Agent 輸出交付報告<br/>修改清單、測試結果、未完成事項"]
    S4 --> T1["5. 工具驗證<br/>check-change-report、check-layering"]
    T1 -- 不通過 --> S2
    T1 -- 通過 --> S5["6. push ai/ 分支、開 PR"]
    S5 --> T2["7. CI：建置、單元、整合、E2E、SAST、SCA、ArchUnit"]
    T2 -- 失敗 --> S2
    T2 -- 通過 --> R1{"8. 人工 Code Review"}
    R1 -- 退回 --> S2
    R1 -- 核准 --> M["9. 合併"]
```

每一步的輸入、輸出與品質門檻整理在第 10 章的 SSDLC 表。

### 7.5 專案慣例檔：讓 Agent 先讀規則

Deep Agents Code 會讀取 `AGENTS.md`（使用者層級在 `/sandbox/.deepagents/agent/AGENTS.md`；專案層級放在 repo 根目錄，依 Deep Agents Code 上游行為，🧪 以實際版本為準）。在 repo 根目錄放一份：

```markdown
# AGENTS.md — order-service（給 AI Agent 的專案規則）

## 先讀
1. docs/spec/ 下的需求與規格；與程式衝突時，以規格為準並回報衝突。
2. docs/architecture.md 的分層規則。

## 架構（Hexagonal）
- com.example.order.domain：實體、值物件、Port 介面。不得 import Spring、JPA、Jackson。
- com.example.order.application：Use Case，只依賴 domain。
- com.example.order.adapter.web / adapter.persistence：Spring Controller、JPA Repository。
- 依賴方向只能 adapter → application → domain。

## 規則
- 修改前先提出計畫（檔案清單、理由、風險），等人類回覆「核准」再動手。
- 不新增第三方依賴；需要時在計畫中提出。
- 不修改 .env*、*-prod.yml、CI 設定、資料庫 migration 既有檔案（只能新增）。
- 每個商業規則都要有對應的單元測試。
- 不得刪除或停用（@Disabled、.skip）既有測試。

## 交付報告格式（必須照抄標題）
## 修改清單
| 檔案 | 動作 | 理由 |
## 測試結果
| 指令 | 結束碼 | 摘要 |
## 未完成與待確認
```

### 7.6 Prompt 範本與審查方法

以下每個範本都遵守同一個骨架：**先讀 → 先計畫 → 等核准 → 小步修改 → 交付報告**。每個範本後面附「如何審查 AI 產出」。

#### 7.6.1 範本 P1：分析需求並建立 SRS

```text
你是本專案的系統分析師。請在不修改任何程式碼的前提下完成：
1. 閱讀 docs/spec/requirements-raw.md 與既有程式（src/），整理成 SRS 草稿，存成 docs/spec/SRS.md。
2. SRS 章節：目的與範圍、角色、使用案例（UC-xx，每個含前置條件、主要流程、例外流程）、
   功能需求（FR-xx）、非功能需求（NFR-xx：效能、安全、稽核、可用性）、資料需求、待確認問題（Q-xx）。
3. 每條 FR 都要能追溯到原始需求的段落（寫出段落標題）。
4. 原始需求沒寫的內容，一律列入「待確認問題」，不得自行補齊。
完成後只輸出：新增的檔案路徑、FR／NFR／Q 的數量、你認為最模糊的三個需求。
```

**如何審查**：

| 檢查 | 方法 |
|---|---|
| 是否偷改程式 | 🔍 `git status --porcelain` 只應出現 `docs/spec/SRS.md` |
| 是否憑空補需求 | 🔍 隨機抽 5 條 FR，回原始需求找段落；找不到的就是幻覺 |
| 待確認問題是否太少 | 需求越模糊，Q 應越多；Q 為 0 是警訊 |

❌ **壞例**：「FR-12 系統應支援 OAuth2 單一登入」——原始需求只寫「使用者需登入」，SSO 是 AI 自行補的。

#### 7.6.2 範本 P2：產生系統架構與設計規格

```text
請依 docs/spec/SRS.md 與 docs/architecture.md（Hexagonal Architecture）產生 docs/design/SDD.md：
1. 元件圖（Mermaid）：domain、application、adapter.web、adapter.persistence 的類別與依賴方向。
2. 每個 Use Case 的序列圖（Mermaid），標出經過的 Port。
3. 資料模型：實體、欄位、型別、約束；PostgreSQL DDL 草稿（不要建立 migration 檔）。
4. 每個設計決策附理由與替代方案（ADR 格式，最多 5 則）。
5. 列出與 SRS 不一致或 SRS 未定義而必須假設的地方。
不要修改 src/。完成後回報檔案路徑與假設清單。
```

**如何審查**：Mermaid 圖能否渲染（貼到 Mermaid Live Editor 或用 18.10 的檢查方式）；依賴箭頭是否只從 adapter 指向 application／domain；每個假設是否都進了 Q 清單。

#### 7.6.3 範本 P3：REST API 規格與 OpenAPI

```text
請依 SDD.md 為「建立訂單」與「查詢訂單」撰寫 docs/api/openapi.yaml（OpenAPI 3.1）：
- 路徑：POST /api/v1/orders、GET /api/v1/orders/{orderId}
- 請求與回應 schema 要有 required、format、minimum、maxLength。
- 錯誤回應統一用 application/problem+json（RFC 9457），列出 400、404、409、422。
- 金額欄位用字串表示的十進位數（避免浮點誤差），並說明理由。
- 不要產生程式碼。完成後執行你被允許的檢查，回報結果。
```

**如何審查**：🔍 用 CI 中的 OpenAPI linter（如 Redocly、Spectral）驗證；檢查是否把內部欄位（資料庫 ID、內部狀態碼）暴露到回應。

#### 7.6.4 範本 P4：依規格開發後端

```text
任務：實作「建立訂單」Use Case（UC-01）。
限制：
- 先讀 AGENTS.md、docs/spec/SRS.md 的 UC-01、docs/design/SDD.md、docs/api/openapi.yaml。
- 先輸出計畫：要新增／修改的檔案、每個檔案的職責、對應的 FR 編號、要新增的測試。等我回覆「核准」。
- 核准後在 ai/uc-01-place-order 分支實作，遵守 Hexagonal 分層：
  domain（Order、OrderRepository Port）→ application（PlaceOrderService）→ adapter（Controller、JPA）。
- 金額超過 50,000（不含）時狀態為 PENDING_REVIEW；金額必須 > 0。
- 不新增依賴；不修改既有 migration；不碰 .env* 與 *-prod.yml。
- 完成後依 AGENTS.md 的格式輸出交付報告。
```

**如何審查**：

| 檢查 | 方法 |
|---|---|
| 分層是否正確 | ✅ `python3 check-layering.py src/main/java com.example.order`（7.8），以及 CI 的 ArchUnit |
| 報告是否誠實 | ✅ `python3 check-change-report.py .ai-reports/uc-01.md origin/main`（7.10） |
| 邊界值 | 50,000 本身是否「不需覆核」？規格寫「超過」，測試要有 `50000` 與 `50000.01` 兩筆 |
| 是否偷加依賴 | 🔍 `git diff origin/main -- pom.xml package.json` |

#### 7.6.5 範本 P5：依規格開發前端（Vue 3＋TypeScript＋Tailwind）

```text
任務：在 web/ 實作「建立訂單」頁面。
- 先讀 docs/api/openapi.yaml 與 web/src 既有的元件、路由、API client 慣例。
- 技術：Vue 3 Composition API + <script setup lang="ts">、Tailwind CSS、既有的 API client。
- 表單欄位：客戶編號（必填，最多 20 字）、金額（必填，> 0，最多兩位小數）。
- 前端驗證只是使用者體驗；以後端回傳的 problem+json 為準顯示錯誤。
- 路由 /orders/new；成功後導到 /orders/{orderId}。
- 不新增 npm 套件；樣式只用 Tailwind 既有 class，不寫 inline style。
- 先列計畫等核准；完成後輸出交付報告（含 npm run lint、npm run test:unit 的結束碼）。
```

**如何審查**：是否用 `v-html` 顯示後端訊息（XSS 風險）；是否把金額轉成 `Number` 做運算；是否把 API base URL 寫死。前端若採 Angular，相同骨架改成 Angular 的元件、Reactive Forms 與 HttpClient 慣例即可。

#### 7.6.6 範本 P6：產生單元測試與整合測試

```text
請為 PlaceOrderService 與 Order 補測試：
- 單元測試（JUnit 5）：金額邊界（0、0.01、50000、50000.01）、null 金額、客戶編號空白。
- 整合測試：以 Testcontainers 啟動 PostgreSQL，驗證 JPA adapter 的 save/findById。
- E2E（Playwright）：建立訂單成功與金額為 0 時的錯誤訊息。
- 測試名稱用「條件_預期結果」；不得使用 Thread.sleep；不得修改正式程式碼來讓測試通過，
  若發現正式程式碼的缺陷，回報而不是修改。
完成後輸出交付報告。
```

**如何審查**：🔍 `git diff --stat origin/main -- src/main` 應為空（只動測試）；❌ 壞例：Agent 為了讓測試過，把 `compareTo(...) > 0` 改成 `>= 0`。

#### 7.6.7 範本 P7：檢查 Clean Architecture 依賴方向

```text
請只做分析、不修改：
1. 列出 src/main/java 下所有違反「adapter → application → domain」方向的 import，含檔案:行號。
2. 列出 domain 套件中所有 Spring、JPA、Jackson 相依。
3. 對每個違規提出最小修正方案（例如抽出 Port 介面），估計影響的檔案數。
輸出成 docs/review/architecture-findings.md。
```

**如何審查**：用 7.8 的兩個工具交叉比對——AI 列出的違規數應與工具相同；AI 多列的要求它附證據，少列的就是漏看。

#### 7.6.8 範本 P8：產生安全檢查清單

```text
請依 OWASP ASVS 4.0.3 Level 2 與本專案的 openapi.yaml，產生 docs/security/checklist-uc01.md：
- 只列與 UC-01 相關的條目（輸入驗證、授權、錯誤處理、日誌、敏感資料）。
- 每條寫：ASVS 編號、檢查方法（程式碼位置或測試名稱）、目前狀態（符合／不符合／無法判斷）。
- 「無法判斷」要說明缺少什麼資訊。不得修改程式碼。
```

**如何審查**：抽查「符合」的條目是否真的有對應程式或測試；ASVS 編號是否存在（[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)）。

#### 7.6.9 範本 P9：執行 Code Review 並修正缺陷

```text
請 review 分支 ai/uc-01-place-order 相對於 origin/main 的變更：
1. 先只輸出問題清單：嚴重度（高／中／低）、檔案:行號、問題、建議修法。不要修改。
2. 我會勾選要修的項目；你只修勾選的項目，每項一個 commit，commit 訊息引用問題編號。
3. 修完後重新輸出交付報告。
```

**如何審查**：AI 自我 review 有盲點（會偏袒自己寫的程式）。人工 reviewer 仍必須看完整 diff；把 AI 的清單當成「起點」而不是「結論」。

### 7.7 範例專案結構與程式碼

```text
order-service/
├── AGENTS.md
├── docs/{spec,design,api,security,review}/
├── pom.xml
├── src/main/java/com/example/order/
│   ├── domain/            Order.java、OrderRepository.java（Port）
│   ├── application/       PlaceOrderService.java
│   └── adapter/
│       ├── web/           OrderController.java
│       └── persistence/   InMemoryOrderRepository.java（正式版為 JPA）
├── src/main/resources/db/migration/V1__create_orders.sql
├── src/test/java/com/example/order/   OrderTest.java、ArchitectureTest.java
└── web/                   Vue 3 + TypeScript + Tailwind
```

核心領域與 Use Case（✅ 已在撰寫環境以 Java 21＋Maven 3.9.9 編譯並通過測試；為了縮小依賴，範例中的 adapter 以純 Java 示意）：

```java
// src/main/java/com/example/order/domain/Order.java
package com.example.order.domain;

import java.math.BigDecimal;

public record Order(String id, String customerId, BigDecimal amount) {
    public static final BigDecimal REVIEW_THRESHOLD = new BigDecimal("50000");

    public Order {
        if (amount == null || amount.signum() <= 0) {
            throw new IllegalArgumentException("amount must be positive");
        }
    }

    public boolean needsManagerReview() {
        return amount.compareTo(REVIEW_THRESHOLD) > 0;
    }
}
```

```java
// src/main/java/com/example/order/domain/OrderRepository.java
package com.example.order.domain;

import java.util.Optional;

/** 輸出 Port：由 adapter.persistence 實作。 */
public interface OrderRepository {
    void save(Order order);

    Optional<Order> findById(String id);
}
```

```java
// src/main/java/com/example/order/application/PlaceOrderService.java
package com.example.order.application;

import com.example.order.domain.Order;
import com.example.order.domain.OrderRepository;
import java.math.BigDecimal;
import java.util.UUID;

/** Use Case：只依賴 domain 的 Port，不知道資料存在哪裡。 */
public class PlaceOrderService {
    private final OrderRepository repository;

    public PlaceOrderService(OrderRepository repository) {
        this.repository = repository;
    }

    public Order place(String customerId, BigDecimal amount) {
        Order order = new Order(UUID.randomUUID().toString(), customerId, amount);
        repository.save(order);
        return order;
    }
}
```

正式專案的 Spring Boot Web adapter（🧪 示意，未在撰寫環境編譯；需 Spring Boot 3.x 與 Jakarta Validation）：

```java
// src/main/java/com/example/order/adapter/web/OrderController.java
package com.example.order.adapter.web;

import com.example.order.application.PlaceOrderService;
import com.example.order.domain.Order;
import jakarta.validation.Valid;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import java.math.BigDecimal;
import java.net.URI;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/orders")
class OrderController {
    private final PlaceOrderService service;

    OrderController(PlaceOrderService service) {
        this.service = service;
    }

    record CreateOrderRequest(@NotBlank @Size(max = 20) String customerId,
                              @DecimalMin(value = "0.01") BigDecimal amount) { }

    record OrderResponse(String orderId, String status) { }

    @PostMapping
    ResponseEntity<OrderResponse> create(@Valid @RequestBody CreateOrderRequest req) {
        Order order = service.place(req.customerId(), req.amount());
        String status = order.needsManagerReview() ? "PENDING_REVIEW" : "CREATED";
        return ResponseEntity.created(URI.create("/api/v1/orders/" + order.id()))
                .body(new OrderResponse(order.id(), status));
    }
}
```

資料庫 migration（🧪 Flyway 慣例；PostgreSQL 語法）：

```sql
-- src/main/resources/db/migration/V1__create_orders.sql
CREATE TABLE orders (
    id           VARCHAR(36)    PRIMARY KEY,
    customer_id  VARCHAR(20)    NOT NULL,
    amount       NUMERIC(15, 2) NOT NULL CHECK (amount > 0),
    status       VARCHAR(20)    NOT NULL,
    created_at   TIMESTAMPTZ    NOT NULL DEFAULT now()
);
CREATE INDEX idx_orders_customer ON orders (customer_id);
```

不同資料庫的差異（請 Agent 產生 DDL 時明確指定目標資料庫）：

| 項目 | PostgreSQL | Oracle | DB2 | SQL Server |
|---|---|---|---|---|
| 十進位金額 | `NUMERIC(15,2)` | `NUMBER(15,2)` | `DECIMAL(15,2)` | `DECIMAL(15,2)` |
| 時區時間 | `TIMESTAMPTZ` | `TIMESTAMP WITH TIME ZONE` | `TIMESTAMP`（另存時區） | `DATETIMEOFFSET` |
| 字串 | `VARCHAR(n)` | `VARCHAR2(n CHAR)` | `VARCHAR(n)` | `NVARCHAR(n)`（Unicode） |
| Testcontainers 模組 | `postgresql` | `oracle-free` | `db2`（需接受授權） | `mssqlserver`（需接受授權） |

前端元件（🧪 示意，未在撰寫環境建置）：

```vue
<!-- web/src/views/OrderCreate.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createOrder, type ProblemDetail } from '@/api/orders'

const customerId = ref('')
const amount = ref('')
const error = ref<string | null>(null)
const router = useRouter()

async function submit() {
  error.value = null
  if (!/^\d+(\.\d{1,2})?$/.test(amount.value) || amount.value === '0') {
    error.value = '金額必須大於 0，最多兩位小數'
    return
  }
  try {
    const res = await createOrder({ customerId: customerId.value, amount: amount.value })
    await router.push(`/orders/${res.orderId}`)
  } catch (e) {
    error.value = (e as ProblemDetail).detail ?? '建立失敗'
  }
}
</script>

<template>
  <form class="mx-auto max-w-md space-y-4 p-6" @submit.prevent="submit">
    <label class="block">
      <span class="text-sm font-medium">客戶編號</span>
      <input v-model.trim="customerId" maxlength="20" required class="mt-1 w-full rounded border px-3 py-2" />
    </label>
    <label class="block">
      <span class="text-sm font-medium">金額</span>
      <input v-model.trim="amount" inputmode="decimal" required class="mt-1 w-full rounded border px-3 py-2" />
    </label>
    <p v-if="error" class="text-sm text-red-600" role="alert">{{ error }}</p>
    <button type="submit" class="rounded bg-blue-600 px-4 py-2 text-white">建立訂單</button>
  </form>
</template>
```

> 📌 **註記**：錯誤訊息用 `{{ error }}` 文字插值（Vue 會跳脫），不用 `v-html`；金額保持字串傳給後端，由後端以 `BigDecimal` 解析。這兩點都是 7.6.5 審查時要確認的。

### 7.8 架構守門：ArchUnit 與快篩工具

**ArchUnit 測試**（✅ 已實測：正常時 `mvn test` 通過；在 `domain.Order` 注入一個參照 `adapter.web.OrderController` 的方法後，測試失敗並指出違規）：

```java
// src/test/java/com/example/order/ArchitectureTest.java
package com.example.order;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;
import static com.tngtech.archunit.library.Architectures.layeredArchitecture;

import com.tngtech.archunit.core.importer.ImportOption;
import com.tngtech.archunit.junit.AnalyzeClasses;
import com.tngtech.archunit.junit.ArchTest;
import com.tngtech.archunit.lang.ArchRule;

@AnalyzeClasses(packages = "com.example.order", importOptions = ImportOption.DoNotIncludeTests.class)
class ArchitectureTest {

    @ArchTest
    static final ArchRule layers = layeredArchitecture()
            .consideringOnlyDependenciesInLayers()
            .layer("Domain").definedBy("..domain..")
            .layer("Application").definedBy("..application..")
            .layer("Adapter").definedBy("..adapter..")
            .whereLayer("Adapter").mayNotBeAccessedByAnyLayer()
            .whereLayer("Application").mayOnlyBeAccessedByLayers("Adapter")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers("Application", "Adapter");

    @ArchTest
    static final ArchRule domainIsFrameworkFree = noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.springframework..", "jakarta.persistence..", "com.fasterxml.jackson..");
}
```

`pom.xml` 的測試依賴（✅ 撰寫環境使用的版本）：

```xml
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>5.11.4</version>
  <scope>test</scope>
</dependency>
<dependency>
  <groupId>com.tngtech.archunit</groupId>
  <artifactId>archunit-junit5</artifactId>
  <version>1.3.0</version>
  <scope>test</scope>
</dependency>
```

違規時的實際輸出（✅ 節錄）：

```text
[ERROR] Tests run: 2, Failures: 1, Errors: 0, Skipped: 0 <<< FAILURE! -- in com.example.order.ArchitectureTest
Architecture Violation [Priority: MEDIUM] - Rule 'Layered architecture considering only dependencies in layers, ...
Method <com.example.order.domain.Order.debug(com.example.order.adapter.web.OrderController)> has parameter of type <com.example.order.adapter.web.OrderController> in (Order.java:0)
```

**快篩工具 `check-layering.py`**（✅ 已實測；完整原始碼見 18.10.3）：不需要編譯，Agent 交付前就能跑，適合放在 pre-commit：

```text
$ python3 check-layering.py src/main/java com.example.order
結果：0 項違規

$ python3 check-layering.py src/main/java com.example.order    # 注入違規後
L01 src/main/java/com/example/order/domain/Order.java:4: domain → com.example.order.adapter.web.OrderController
結果：1 項違規
```

> 📌 **註記**：`check-layering.py` 只看 `import` 敘述，抓不到完整類別名稱（FQCN）直接使用與反射；ArchUnit 分析位元組碼，才是正式守門。兩者並用：快篩給 Agent 即時回饋，ArchUnit 在 CI 擋合併。

### 7.9 測試策略

| 層級 | 工具 | 在哪跑 | 範例狀態 |
|---|---|---|---|
| 單元 | JUnit 5 | 沙盒（若有 JDK）或 CI | ✅ `OrderTest` |
| 架構 | ArchUnit | CI | ✅ `ArchitectureTest` |
| 整合 | Testcontainers＋PostgreSQL | **CI**（沙盒內沒有 Docker） | 🧪 |
| E2E | Playwright | CI | 🧪 |

單元測試（✅ 已實測通過）：

```java
// src/test/java/com/example/order/OrderTest.java
package com.example.order;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.example.order.domain.Order;
import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

class OrderTest {
    @Test
    void amountAboveThresholdNeedsReview() {
        assertTrue(new Order("1", "c1", new BigDecimal("50000.01")).needsManagerReview());
        assertFalse(new Order("2", "c1", new BigDecimal("50000")).needsManagerReview());
    }

    @Test
    void nonPositiveAmountIsRejected() {
        assertThrows(IllegalArgumentException.class, () -> new Order("3", "c1", BigDecimal.ZERO));
    }
}
```

Testcontainers 整合測試（🧪 示意；需 Docker，因此在 CI 執行）：

```java
@Testcontainers
@SpringBootTest
class JpaOrderRepositoryIT {
    @Container
    @ServiceConnection
    static PostgreSQLContainer<?> db = new PostgreSQLContainer<>("postgres:16-alpine");

    @Autowired
    OrderRepository repository;

    @Test
    void savesAndFindsOrder() {
        var order = new Order("it-1", "c1", new BigDecimal("100.00"));
        repository.save(order);
        assertThat(repository.findById("it-1")).contains(order);
    }
}
```

Playwright E2E（🧪 示意）：

```ts
// web/e2e/order-create.spec.ts
import { test, expect } from '@playwright/test'

test('金額為 0 時顯示錯誤', async ({ page }) => {
  await page.goto('/orders/new')
  await page.getByLabel('客戶編號').fill('C001')
  await page.getByLabel('金額').fill('0')
  await page.getByRole('button', { name: '建立訂單' }).click()
  await expect(page.getByRole('alert')).toContainText('金額必須大於 0')
})
```

### 7.10 交付報告與誠實性檢查

Agent 的交付報告必須照 AGENTS.md 的格式。`check-change-report.py`（✅ 已實測；完整原始碼見 18.10.2）把報告與 `git diff` 比對：

| 結果 | 意義 |
|---|---|
| `UNREPORTED` | 實際有改、報告沒寫——**最危險**，代表有變更沒人審 |
| `PHANTOM` | 報告說改了、實際沒改——報告不可信 |
| `FORBIDDEN` | 碰到 `.env*`、`*.pem`、`*.key`、`*application-prod*` |
| `NOEVIDENCE` | 測試結果沒有結束碼 |
| `TESTFAIL` | 有測試結束碼非 0，Agent 卻宣稱完成 |

好例報告（✅ 實際輸出）：

```text
$ python3 check-change-report.py .ai-reports/good.md base
報告列出 2 檔、實際變更 2 檔、測試 1 筆、問題 0 項
```

❌ 壞例報告：少報一個新檔、多報一個沒改的檔、偷改 `.env.local`、測試失敗卻說完成：

```text
$ python3 check-change-report.py .ai-reports/bad.md base
UNREPORTED .env.local: 實際有變更，報告未列出
UNREPORTED src/main/java/demo/C.java: 實際有變更，報告未列出
PHANTOM    src/main/java/demo/B.java: 報告列出，但 Git 沒有這個變更
FORBIDDEN  .env.local: 變更碰到禁止路徑
TESTFAIL   `mvn -q test`: 結束碼 1
NOEVIDENCE `npm run e2e`: 結束碼 '通過' 不是數字
報告列出 2 檔、實際變更 3 檔、測試 2 筆、問題 6 項
```

> ⚠️ **警告**：報告中的「結束碼 0」仍是 Agent 自己寫的。`check-change-report.py` 只證明「報告與 Git 一致」；測試是否真的通過，以 CI 的結果為準。

### 7.11 程式碼品質、弱點掃描與依賴檢查

這些工具在沙盒外的 CI 執行（第 10 章有完整 pipeline）。🏢 建議的最低組合：

| 類別 | 後端 | 前端 | 門檻 |
|---|---|---|---|
| 靜態分析／品質 | SonarQube 或 SpotBugs＋PMD | ESLint＋`vue-tsc --noEmit` | 新增程式碼無 Blocker／Critical |
| SAST | Semgrep 或 CodeQL | 同左 | 高風險 0 |
| SCA（依賴弱點） | OWASP Dependency-Check 或 Trivy | `npm audit --omit=dev` 或 Trivy | 無已知 Critical；High 需例外單 |
| 授權 | CycloneDX SBOM＋授權政策 | 同左 | 無禁用授權 |
| 機密掃描 | gitleaks | 同左 | 0 |

### 7.12 建置、部署與交付文件

| 交付物 | 產生者 | 驗收者 |
|---|---|---|
| SRS、SDD、OpenAPI | Agent 草擬、SA／架構師修訂 | 需求方、架構師 |
| 程式碼與測試 | Agent 實作、開發者修訂 | Code Reviewer |
| 交付報告（每個 PR） | Agent | `check-change-report.py`＋Reviewer |
| CI 報告（測試、覆蓋率、掃描） | CI | QA、資安 |
| SBOM | CI | 資安 |
| 部署說明、回復步驟 | 開發者（可請 Agent 草擬） | 維運 |

### 7.13 本章實務案例與注意事項

**案例**：Agent 交付 UC-01，報告寫「測試全部通過」，CI 卻失敗在 `ArchitectureTest`。

追查：

1. `check-change-report.py` 顯示 `UNREPORTED src/main/java/com/example/order/domain/OrderMapper.java`——Agent 為了方便，在 domain 放了一個依賴 JPA Entity 的 mapper，卻沒寫進報告。
2. Agent 在沙盒內沒有 JDK（7.3），報告中的「`mvn -q test` 結束碼 0」是它「預期」的結果，不是實際執行的結果。
3. 處置：退回 PR；在 AGENTS.md 加一條「沒有實際執行的指令不得寫進測試結果表，改寫在『未完成與待確認』」；在 pre-commit 加入 `check-layering.py`。

**注意事項**：

- 所有 Prompt 都要求「先計畫、等核准」，但模型不一定遵守。真正的控制是：寫入 preset 預設不套用、只能推 `ai/` 分支、主線受分支保護。
- 不要讓 Agent 同時擁有「改程式」與「改 CI 設定」的能力；CI 檔案列入 AGENTS.md 的禁止清單，並由 CODEOWNERS 保護。
- 範例中的 Spring、Testcontainers、Playwright 程式碼標 🧪，導入時以專案實際版本為準。

## 第8章 既有系統逆向工程

案例：一套沒有完整文件的企業舊系統「legacy-billing」（Java 8＋Struts／Spring 混用、JSP 前端、Oracle Stored Procedure、夜間批次、MQ 介接）。目標是在 NemoClaw 管控下，讓 Agent 協助盤點、追蹤、重建規格，並產出可驗證的文件與回歸測試。逆向工程是 NemoClaw 最能發揮的情境：原始碼可以**唯讀**掛入，Agent 改不到原始檔。

### 8.1 原則

| 原則 | 做法 |
|---|---|
| 先盤點、再分析、最後才談修改 | 本章所有 Prompt 都禁止修改原始碼 |
| 事實與推測分開 | 文件中每條結論標 `[事實]` 或 `[推測]`；事實必附「來源：路徑:行號」 |
| 證據可驗證 | 用 `check-evidence.py`（8.6）機械檢查引用存在、行號在範圍內 |
| 不連正式環境 | 沙盒網路只開推理服務；不給資料庫連線 |
| 資訊不足就問 | 每份文件都有「待確認問題 Q-xx」 |
| 不憑空補邏輯 | 找不到的程式邏輯寫「未找到」，不寫「應該是」 |

### 8.2 環境準備：唯讀掛入原始碼、只開推理

```bash
# 🖥️ Host：1. 準備一份「去敏」後的原始碼副本（見 8.9），不要直接掛正式 repo
cp -a /srv/src/legacy-billing /srv/re/legacy-billing-snapshot-20261027
gitleaks detect --no-git --source /srv/re/legacy-billing-snapshot-20261027 --report-path /srv/re/gitleaks.json

# 2. 建立逆向工程沙盒：原始碼唯讀掛入、Restricted 層
export NEMOCLAW_DISABLE_TELEMETRY=1
NEMOCLAW_POLICY_TIER=restricted nemo-deepagents onboard --name re-legacy \
  --host-mount /srv/re/legacy-billing-snapshot-20261027:/sandbox/src

# 3. 移除 Deep Agents 預設的 GitHub 與 PyPI 出口（逆向工程不需要）
nemo-deepagents re-legacy policy exclude github --dry-run
nemo-deepagents re-legacy policy exclude github --force
nemo-deepagents re-legacy policy exclude pypi --force
nemo-deepagents re-legacy policy list
```

```bash
# 🖥️ Host：4. 驗證唯讀與輸出目錄
nemo-deepagents re-legacy exec -- bash -lc 'touch /sandbox/src/x 2>&1 || echo RO-OK'
nemo-deepagents re-legacy exec -- bash -lc 'awk "\$2==\"/sandbox/src\"{print \$2,\$4}" /proc/mounts'
nemo-deepagents re-legacy exec -- bash -lc 'mkdir -p /sandbox/re-out && echo OUT-OK'
```

| 項目 | 內容 |
|---|---|
| 執行位置 | 🖥️ Host |
| 前提 | Linux 或 WSL 2 上的 Docker（`--host-mount` 不支援 macOS 與 Podman） |
| 預期結果 | `RO-OK`；`/proc/mounts` 中 `/sandbox/src` 的選項含 `ro`；`OUT-OK` |
| 失敗排查 | onboarding 拒絕 `--host-mount` → 檢查平台與 Gateway 是否為 NemoClaw 管理的 Docker driver |
| 是否修改系統 | 建立沙盒與政策變更；原始碼副本不會被修改 |

> 📌 **註記**：`--host-mount` 掛入的是「主機目錄的即時唯讀視圖」，主機端之後修改副本，沙盒內會看到。所以要掛的是「凍結的快照副本」，並在文件中記錄快照日期與來源 commit。

### 8.3 逆向工程流程

```mermaid
flowchart TD
    A["1. 盤點<br/>目錄、模組、語言、建置檔"] --> B["2. 呼叫關係<br/>JSP、Action、Controller、Service"]
    B --> C["3. 資料追蹤<br/>API、資料表、Stored Procedure"]
    C --> D["4. 商業規則<br/>條件、例外、錯誤碼"]
    D --> E["5. 批次與介接<br/>排程、MQ、檔案交換、外部系統"]
    E --> F["6. 架構圖與資料流圖<br/>Mermaid"]
    F --> G["7. 文件<br/>SRS、SDD、API、資料字典"]
    G --> H["8. 行為比對<br/>文件 vs 實際執行"]
    H --> I["9. 回歸測試與差異報告"]
    A -.->|"每步都產出待確認問題 Q-xx"| Q["待確認問題清單<br/>交給系統負責人"]
    D -.-> Q
    E -.-> Q
```

### 8.4 步驟總表

| 步驟 | AI 的工作 | 輸出 | 人工檢查 |
|---|---|---|---|
| 1. 盤點 | 列出目錄、模組、檔案數、語言、框架版本、建置檔、設定檔 | `inventory.md`、`modules.csv` | 數字與 `find`／`wc` 結果相符 |
| 2. 呼叫關係 | 從 URL／JSP 追到 Action／Controller、Service、DAO | `call-graph.md`（Mermaid） | 抽 3 條路徑人工追 |
| 3. 資料追蹤 | 列出每支 DAO 用到的資料表、SQL、SP 與參數 | `data-access.md` | SP 名稱與 DB 物件清單比對 |
| 4. 商業規則 | 抽出條件判斷、例外處理、錯誤碼 | `business-rules.md`（標 `[事實]`／`[推測]`） | `check-evidence.py`＋業務人員確認 |
| 5. 批次與介接 | 排程設定、批次程式、MQ queue、檔案格式、外部 URL | `integration.md` | 與維運排程表比對 |
| 6. 圖 | 系統架構圖、資料流圖 | `architecture.md` | 圖中每個節點都能在 1～5 找到出處 |
| 7. 文件 | SRS、SDD、API 規格、資料字典 | `SRS.md`、`SDD.md`、`api.md`、`data-dictionary.md` | 架構師與系統負責人審 |
| 8. 行為比對 | 依文件設計測試案例，在測試環境執行並比對 | `behavior-diff.md` | QA |
| 9. 回歸測試 | 產生 characterization tests 與差異報告 | `src/test/...`、`regression-report.md` | Code Review |

### 8.5 Prompt 範本

#### 8.5.1 共用前言（每個逆向 Prompt 的開頭都貼上）

```text
【逆向工程共同規則】
- 原始碼在 /sandbox/src（唯讀）。所有輸出寫到 /sandbox/re-out/。
- 禁止修改、移動、刪除 /sandbox/src 下任何檔案；禁止嘗試連線任何資料庫或外部系統。
- 每條結論標示：
  [事實]：原始碼可直接證實，必須附（來源：相對於 /sandbox/src 的路徑:起始行-結束行）。
  [推測]：根據命名、註解或慣例推論，必須附（依據：…；待確認 Q-xx）。
- 找不到就寫「未找到」，並列出你搜尋過的路徑與關鍵字；不得補寫不存在的邏輯。
- 檔案可能是 MS950（Big5）編碼；讀到亂碼時回報檔名，不要猜內容。
- 遇到看起來像密碼、金鑰、身分證號、帳號的字串，以 *** 遮蔽，並在報告中列出位置。
- 最後輸出：產出檔案清單、[事實]／[推測] 數量、待確認問題清單。
```

#### 8.5.2 範本 R1：盤點程式碼、目錄與模組

```text
（貼上共用前言）
任務：盤點 /sandbox/src。
1. 目錄樹（深度 3）與每個頂層目錄的用途推測。
2. 依副檔名統計檔案數與行數（java、jsp、xml、properties、sql、sh、js）。
3. 建置工具與版本（pom.xml、build.gradle、build.xml），列出主要框架與版本。
4. 設定檔清單（*.properties、*.xml、*.yml），標出疑似含連線資訊的檔案（只列路徑，內容遮蔽）。
5. 模組清單 modules.csv：模組名稱、路徑、主要套件、檔案數、對外介面（URL／Queue／檔案）。
輸出 /sandbox/re-out/inventory.md、/sandbox/re-out/modules.csv。
```

**如何審查**：

```bash
# 🖥️ Host：用指令重算，比對 Agent 報的數字
nemo-deepagents re-legacy exec -- bash -lc 'cd /sandbox/src && find . -name "*.java" | wc -l && find . -name "*.jsp" | wc -l'
nemo-deepagents re-legacy download /sandbox/re-out/ ./re-out/
```

數字對不上時，要求 Agent 列出它統計的檔案清單——差異通常是它只掃了部分目錄（上下文不足）。

#### 8.5.3 範本 R2：前後端呼叫關係

```text
（貼上共用前言）
任務：建立「請款單查詢」功能的呼叫鏈。
起點：web.xml、struts-config.xml、@RequestMapping 中與 invoice 相關的 URL。
對每條 URL 追到：JSP → Action/Controller 方法 → Service 方法 → DAO 方法 → SQL 或 SP。
輸出 call-graph.md：
- 一張 Mermaid flowchart。
- 一張表：URL｜Action/Controller（路徑:行）｜Service（路徑:行）｜DAO（路徑:行）｜資料表/SP。
追不到的環節寫「未找到」並列出搜尋過的關鍵字。
```

**如何審查**：隨機抽 3 條鏈，自己用 `grep -n` 追一次。❌ 壞例：表格中 Service 欄寫 `InvoiceService.query()`，但該類別實際沒有 `query` 方法——這就是幻覺，`check-evidence.py` 的 BADLINE 或人工追查會抓到。

#### 8.5.4 範本 R3：追蹤 API、資料表與 Stored Procedure

```text
（貼上共用前言）
任務：列出所有資料存取。
1. 每個 DAO／Mapper：方法、SQL（原文）、讀寫的資料表、使用的 SP 與參數方向（IN/OUT）。
2. 動態 SQL（字串串接）另列一節，標出可能的 SQL Injection 位置（[事實]＋行號）。
3. 若 /sandbox/src 內有 *.sql 或 SP 原始碼，列出 SP 內部再呼叫的 SP 與資料表。
4. 產生 data-access.md 與 tables.csv（資料表、被哪些模組讀、被哪些模組寫）。
```

**如何審查**：資料表清單交給 DBA 與實際 schema 比對；SQL Injection 位置交給資安複核。

#### 8.5.5 範本 R4：重建商業規則與例外處理

```text
（貼上共用前言）
任務：重建「請款金額計算」的商業規則。
1. 找出所有與金額、稅率、折扣、四捨五入相關的程式碼。
2. 每條規則一行：[事實] 規則描述（來源：路徑:行-行）。
3. 例外處理：每個 catch、錯誤碼、錯誤訊息，對應到使用者看得到的結果。
4. 命名或註解暗示、但程式沒有實作的規則，標 [推測] 並開 Q-xx。
5. 不同模組實作不一致的規則，另列「規則衝突」一節。
輸出 business-rules.md。
```

**如何審查**：先跑 8.6 的 `check-evidence.py`；通過後，請業務人員逐條確認 `[事實]` 的描述是否等於程式行為（工具只證明「行號存在」，不證明「描述正確」）。

#### 8.5.6 範本 R5：批次作業、排程、訊息佇列與外部介接

```text
（貼上共用前言）
任務：盤點非同步與外部介接。
1. 排程：crontab、Quartz、Spring @Scheduled、shell script；列出排程時間、程式入口、輸入輸出檔案。
2. 訊息佇列：MQ queue/topic 名稱、發送端、接收端、訊息格式（欄位）。
3. 檔案交換：檔名規則、編碼、固定長度欄位定義。
4. 外部系統：URL、主機名、介面規格；URL 中的主機名照列，帳密遮蔽。
5. 每項標出重跑（rerun）與失敗處理邏輯。
輸出 integration.md。
```

#### 8.5.7 範本 R6：重建系統架構圖與資料流圖

```text
（貼上共用前言）
任務：依 inventory.md、call-graph.md、data-access.md、integration.md 繪製：
1. 系統架構圖（Mermaid flowchart）：模組、資料庫、MQ、外部系統。
2. 「請款」端到端資料流圖：資料從畫面輸入、經過哪些模組與資料表、到產出檔案。
圖中每個節點都要在註解中標註出處（引用前述文件的章節）。不得出現前述文件沒有的節點。
```

#### 8.5.8 範本 R7：產生 SRS、SDD、API 規格與資料字典

```text
（貼上共用前言）
任務：把前述分析整理成正式文件草稿：
- SRS.md：功能需求依 call-graph 的功能分組；每條 FR 標 [事實]（附來源）或 [推測]（附 Q）。
- SDD.md：模組設計、類別職責、例外處理策略。
- api.md：對外 URL 與參數（從 web.xml、Action、Controller 整理）。
- data-dictionary.md：資料表、欄位、型別、用途（用途若是推測必須標 [推測]）。
文件開頭註明：原始碼快照日期 2026-10-27、來源 commit（由我提供）、本文件為 AI 草稿需人工審查。
```

#### 8.5.9 範本 R8 與 R9：行為比對、回歸測試與差異報告

```text
（貼上共用前言）
任務 R8：依 business-rules.md 為每條 [事實] 規則設計測試案例：輸入、預期輸出、依據規則編號。
輸出 behavior-cases.csv。不要執行，不要連線任何環境。

任務 R9：以 behavior-cases.csv 產生 characterization tests（JUnit 5）草稿：
- 測試只描述「目前的行為」，即使看起來像 bug 也照現況斷言，並在測試名稱加 _currentBehavior。
- 產出到 /sandbox/re-out/tests/，不要放進 /sandbox/src。
- 另外輸出 regression-report.md 範本：案例編號｜舊系統結果｜新系統結果｜差異｜判定（預期／缺陷／待確認）。
```

**如何審查**：測試要由人在**測試環境**對舊系統實際執行，把結果填回 `behavior-cases.csv` 的「實際輸出」欄；只有實際跑過的案例，才能作為重構或改版的基準。

### 8.6 事實與推測的機械檢查

`check-evidence.py`（✅ 已實測；完整原始碼見 18.10.4）檢查五件事：

| 結果 | 意義 |
|---|---|
| `MISSING` | `[事實]` 沒有來源 |
| `BADFILE` | 來源檔案不存在 |
| `BADLINE` | 行號超出檔案長度或起訖顛倒 |
| `NOBASIS` | `[推測]` 沒有「依據：」或沒有 `Q-xx` |
| `UNTAGGED` | 條列含「必須／一律／會自動／禁止／只能」等結論字眼卻沒標示 |

好例（✅ 實際輸出）：

```markdown
- [事實] 訂單金額超過 50,000 時需主管覆核（不含 50,000）。（來源：src/main/java/com/example/order/domain/Order.java:6-6）（來源：src/main/java/com/example/order/domain/Order.java:15-17）
- [事實] 金額必須大於 0，否則拋出 IllegalArgumentException。（來源：src/main/java/com/example/order/domain/Order.java:8-12）
- [推測] 覆核門檻可能依客戶等級不同。（依據：Order.java 只有單一常數 REVIEW_THRESHOLD；待確認 Q-01）
```

```text
$ python3 check-evidence.py docs/business-rules.md .
結果：事實 2 條、推測 1 條、問題 0 項
```

❌ 壞例（只用於審查訓練）：

```markdown
- [事實] 訂單一律於建立後 30 天自動結案。
- [事實] 覆核門檻定義於設定檔。（來源：src/main/resources/application.yml:12）
- [事實] 金額檢查位於 Order 建構子。（來源：src/main/java/com/example/order/domain/Order.java:80-95）
- [推測] VIP 客戶免覆核。
- 系統會自動通知主管。
```

```text
$ python3 check-evidence.py docs/bad-rules.md .
MISSING  docs/bad-rules.md:3: [事實] 沒有來源
BADFILE  docs/bad-rules.md:4: src/main/resources/application.yml 不存在
BADLINE  docs/bad-rules.md:5: src/main/java/com/example/order/domain/Order.java:80-95 超出 1–17
NOBASIS  docs/bad-rules.md:6: [推測] 需要「依據：」與待確認編號 Q-xx
UNTAGGED docs/bad-rules.md:7: 疑似結論但未標示 [事實]／[推測]
結果：事實 3 條、推測 1 條、問題 5 項
```

> ⚠️ **警告**：工具通過只代表「引用的位置存在」。最常見的高級錯誤是「行號正確、描述錯誤」（例如程式寫 `> 0`，文件寫「大於等於 0」）。抽查比例 🏢 建議：`[事實]` 至少 20%，涉及金額、權限、法規的規則 100%。

### 8.7 大型程式碼庫與上下文窗口限制

| 問題 | 症狀 | 做法 |
|---|---|---|
| 一次讀不完 | Agent 只分析前幾個目錄就下結論 | 先跑 R1 產生 `modules.csv`，再**逐模組**下 Prompt |
| 跨模組追蹤斷線 | 呼叫鏈在模組邊界「未找到」 | 每個模組產出「對外介面摘要」，跨模組時只給摘要＋目標模組原始碼 |
| 上下文壓縮遺失細節 | 長對話後忘記早先的規則 | 每次新任務重貼共用前言；結果寫進檔案，不靠對話記憶 |
| 重複分析浪費 token | 每次都重新讀全部 | 以 `inventory.md`、`call-graph.md` 作為索引，下一步只讀需要的檔案 |

逐模組批次分析（🖥️ Host；🧪 依 `dcode -n` 的 JSON 介面撰寫，未實機執行）：

```bash
#!/usr/bin/env bash
# re-batch.sh — 🏢 逐模組執行無頭分析；dcode -n 停用 shell、只能讀檔與寫檔
set -euo pipefail
PREAMBLE=$(cat re-preamble.txt)               # 8.5.1 共用前言
while IFS=, read -r module path _; do
  [[ "$module" == "module" ]] && continue      # 跳過 CSV 標題
  prompt="${PREAMBLE}
任務：只分析 /sandbox/src/${path}，產出 /sandbox/re-out/modules/${module}.md（對外介面摘要＋商業規則）。"
  nemo-deepagents re-legacy agent -n "$prompt" --json > "out-${module}.json" || true
  jq -r '.data.status + " " + (.data.exit_code|tostring)' "out-${module}.json"
done < modules.csv
```

### 8.8 編碼格式與中文註解

台灣企業的舊系統常見 MS950（Big5）或混用 UTF-8：

```bash
# 🖥️ Host：在主機端（不是沙盒）偵測編碼，轉出 UTF-8 副本再掛入
cd /srv/re/legacy-billing-snapshot-20261027
find . -name "*.java" -exec file -i {} + | grep -v 'charset=utf-8\|charset=us-ascii' | head
# 轉碼到新目錄，保留原始副本不動（🧪 確認無亂碼後再掛入）
mkdir -p ../legacy-billing-utf8
find . -type f \( -name "*.java" -o -name "*.jsp" -o -name "*.properties" \) | while read -r f; do
  mkdir -p "../legacy-billing-utf8/$(dirname "$f")"
  iconv -f CP950 -t UTF-8 "$f" > "../legacy-billing-utf8/$f" 2>/dev/null || cp "$f" "../legacy-billing-utf8/$f"
done
```

| 注意 | 說明 |
|---|---|
| `.properties` 的 `\uXXXX` | Java 舊版 properties 以 Unicode escape 存中文，請 Agent 解碼後再引用 |
| 轉碼後行號 | `iconv` 不改變行數，行號引用仍有效 |
| 中文註解與程式不一致 | 舊系統常見「註解寫 A、程式做 B」——以程式為 `[事實]`，註解內容只能作為 `[推測]` 的依據 |

### 8.9 敏感資料處理

| 風險 | 掛入前的處理（🖥️ Host） |
|---|---|
| 設定檔中的資料庫帳密 | `gitleaks detect --no-git` 掃描；以 `sed` 在副本中遮蔽後再掛入 |
| SQL dump、測試資料含真實客戶資料 | ⛔ 不放進副本；改用合成資料 |
| 日誌檔 | ⛔ 不放進副本 |
| 正式環境主機名、IP | 可保留（逆向需要），但推理服務若在外部，屬資料外送，需依 13.6 分級 |
| 個資欄位定義（身分證、帳號） | 欄位名稱可保留；樣本值一律移除 |

> ⚠️ **警告**：原始碼本身就可能是機密資料。把整個舊系統送進**外部**推理服務前，必須依 13.6 取得資料擁有者核准；高機密系統應改用企業私有模型（14.5）。

### 8.10 回歸測試與差異報告

| 測試類型 | 目的 | 產生方式 | 執行位置 |
|---|---|---|---|
| Characterization test | 鎖住「目前行為」，作為重構基準 | R9 草稿＋人工修訂 | CI／測試環境 |
| Golden master | 批次輸出檔逐位元比對 | 在測試環境跑舊批次，保存輸出 | 測試環境 |
| 契約測試 | 外部介接格式不變 | 依 `integration.md` 撰寫 | CI |

差異報告範本：

| 案例 | 規則 | 舊系統結果 | 新系統／文件預期 | 差異 | 判定 | 負責人 |
|---|---|---|---|---|---|---|
| BC-001 | BR-03 | 1,050.00 | 1,050.00 | 無 | 一致 | — |
| BC-002 | BR-07 | 999.99（無條件捨去） | 1,000.00（四捨五入） | 0.01 | 待確認 Q-12 | 業務窗口 |

### 8.11 本章實務案例與注意事項

**案例**：Agent 產出的 `business-rules.md` 寫「[事實] 逾期 90 天自動轉呆帳（來源：BatchJob.java:120-135）」，`check-evidence.py` 通過，但業務人員說實際是 180 天。

追查：`BatchJob.java:120-135` 確實有 `90`，但那是「提醒」的天數；轉呆帳的 `180` 在另一個 SP 裡（沙盒內只有 Java 原始碼，沒有 SP 原始碼）。Agent 把兩件事混在一起。

改善：

1. 共用前言加一條：「同一數值出現多次時，列出所有出現位置，不得只取第一個」。
2. 向 DBA 申請 SP 原始碼（去敏後）一併掛入。
3. 金額、天數、比率類規則改為 100% 人工確認。

**注意事項**：

- 掛入的是凍結快照；文件要記錄快照日期與來源 commit，避免之後原始碼變動造成文件失效。
- `dcode -n` 會自動核准檔案寫入；輸出目錄 `/sandbox/re-out` 與唯讀的 `/sandbox/src` 分開，是讓「自動核准」也安全的前提。
- 逆向產出的所有文件都是草稿，必須經系統負責人簽核才能成為正式規格。

## 第9章 Framework 與執行環境升級

案例：把「order-service」從 Java 11＋Spring Boot 2.7＋Vue 2＋Node 16 升級到 Java 21＋Spring Boot 3.x＋Vue 3＋Node 22。升級是 AI Agent 很能幫忙、也很容易闖禍的工作：機械式修改量大（`javax` → `jakarta`、Options API → Composition API），但 Breaking Change 的影響要靠測試與人判斷。**本章的鐵則：未經測試與人工審查的批次自動升級結果，不得視為可上線成果。**

### 9.1 升級範圍與官方指南

| 對象 | 典型升級 | 主要 Breaking Change | 官方指南 |
|---|---|---|---|
| Java | 8／11 → 17／21 | 移除的 API、強封裝（`--add-opens`）、`SecurityManager` 淘汰 | [Oracle JDK 21 Migration Guide](https://docs.oracle.com/en/java/javase/21/migrate/index.html) |
| Spring Boot | 2.7 → 3.x | Java 17 基線、`javax.*` → `jakarta.*`、Spring Security 6 設定方式、屬性改名 | [Spring Boot 3.0 Migration Guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide) |
| Spring Framework | 5.3 → 6.x | 同上；部分 API 移除 | [Spring Framework Versions](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions) |
| Vue | 2 → 3 | 全域 API、`v-model`、過濾器移除、事件匯流排 | [Vue 3 Migration Guide](https://v3-migration.vuejs.org/) |
| Angular | 逐大版升級 | 每版不同 | [Angular Update Guide](https://angular.dev/update-guide) |
| TypeScript | 4.x → 5.x | 型別檢查變嚴 | [TypeScript Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/overview.html) |
| Node.js | 16 → 22 LTS | OpenSSL 3、原生模組重編 | [Node.js Releases](https://nodejs.org/en/about/previous-releases) |
| Maven／Gradle | 外掛版本、Gradle 8 → 9 | 外掛相容性 | [Maven Release History](https://maven.apache.org/docs/history.html)、[Gradle Upgrading](https://docs.gradle.org/current/userguide/upgrading_version_8.html) |
| 資料庫驅動 | ojdbc8 → ojdbc11、mssql-jdbc 12 | 預設加密（SQL Server `encrypt=true`）、時區處理 | 各廠商 Release Notes |
| Docker 基底映像 | `openjdk:11` → `eclipse-temurin:21-jre` | 基底 OS 改變、使用者權限 | 映像檔供應商說明 |

> ✅ **建議**：機械式重構可以先用確定性工具（例如 [OpenRewrite](https://docs.openrewrite.org/) 的 Spring Boot 3 recipe），再讓 Agent 處理工具處理不了的部分。確定性工具的輸出可重現、可審查，比讓 LLM 逐檔改穩定。

### 9.2 標準升級流程

```mermaid
flowchart TD
    U1["1. 盤點目前版本與依賴<br/>mvn dependency:tree、npm ls"] --> U2["2. 確認官方支援矩陣<br/>Java × Spring Boot × DB 驅動 × 中介軟體"]
    U2 --> U3["3. 研究 Breaking Changes<br/>Migration Guide 逐條對照"]
    U3 --> U4["4. 升級計畫與風險清單<br/>分批、順序、回復點"]
    U4 --> G1{"人工核准計畫？"}
    G1 -- 否 --> U3
    G1 -- 是 --> U5["5. 建立回復基線<br/>tag、分支、建置產物、DB 備份"]
    U5 --> U6["6. 逐步修改<br/>每批一個 PR"]
    U6 --> U7["7. 編譯、單元、整合、E2E"]
    U7 -- 失敗 --> U6
    U7 --> U8["8. 效能、安全、執行環境檢查"]
    U8 --> U9["9. 升級前後行為比對"]
    U9 --> U10["10. 升級報告、回復方案、驗收清單"]
```

| 步驟 | Agent 可協助 | 必須由工具或人完成 |
|---|---|---|
| 1. 盤點 | 整理依賴樹、找出已停止維護的套件 | 在 CI 實際執行 `mvn dependency:tree`、`npm ls --all` |
| 2. 支援矩陣 | 彙整官方文件 | 人確認企業中介軟體（WebLogic、WebSphere、AP Server）的支援聲明 |
| 3. Breaking Changes | 逐條對照 Migration Guide 與程式碼使用點 | — |
| 4. 計畫 | 草擬分批計畫與風險清單 | 架構師核准 |
| 5. 基線 | 產生指令清單 | 人執行 tag 與備份 |
| 6. 修改 | 小步修改 | Code Review |
| 7. 測試 | 補測試 | **CI 執行** |
| 8. 非功能 | 草擬檢查項目 | 效能測試、弱點掃描工具 |
| 9. 行為比對 | 設計比對案例 | 測試環境實際執行 |
| 10. 報告 | 草擬 | 人簽核 |

### 9.3 各技術的升級要點

**Java 11 → 21**：

- 先升 Java 17 再升 21，分兩個 PR，讓問題容易定位。
- 搜尋 `--illegal-access`、`sun.misc.Unsafe`、反射存取 JDK 內部類別的程式。
- `maven-compiler-plugin` 改用 `<release>21</release>`；確認 Lombok、MapStruct、Mockito 等需要配合 JDK 版本的工具已升級。

**Spring Boot 2.7 → 3.x**：

- 先在 2.7 上清掉所有 deprecation 警告（官方 Migration Guide 的建議）。
- `javax.persistence`、`javax.validation`、`javax.servlet` → `jakarta.*`；第三方函式庫也必須有 Jakarta 版本。
- Spring Security：`WebSecurityConfigurerAdapter` 已移除，改用 `SecurityFilterChain` bean。
- 屬性改名：使用 `spring-boot-properties-migrator` 在啟動時列出。

**Vue 2 → 3**：

- 先升到 Vue 2.7（內建 Composition API），再用 `@vue/compat` 過渡到 Vue 3。
- 搜尋 `Vue.filter`、`$on`／`$off`、`.sync`、`v-model` 的自訂元件用法。
- UI 元件庫（Element UI → Element Plus 等）通常是最大的工作量，要先確認目標版本。

**資料庫驅動與中介軟體**：

- SQL Server JDBC 10 起預設 `encrypt=true`，舊環境沒有正式憑證會連不上——這是設定變更，不是程式錯誤。
- Oracle 驅動升級後確認 `TIMESTAMP WITH TIME ZONE` 與 `DATE` 的對應行為。
- 企業 AP Server 是否支援 Jakarta EE 10，是能否升 Spring Boot 3 的前提。

### 9.4 Prompt 範本

#### 9.4.1 範本 U1：差異分析（只讀不改）

```text
任務：分析 order-service 從 Spring Boot 2.7.18 升級到 3.3.x 的影響。不要修改任何檔案。
1. 讀 pom.xml、所有 Java 原始碼、application*.yml。
2. 依 Spring Boot 3.0 Migration Guide 的章節，逐條列出本專案受影響的地方：
   章節｜受影響檔案:行號｜目前寫法｜需要的修改｜自動化可行性（OpenRewrite 可處理／需人工）。
3. 列出所有 javax.* import（數量與檔案清單）。
4. 列出沒有 Jakarta 相容版本的第三方依賴，附你查到的依據；查不到就寫「未確認」。
5. 列出測試覆蓋不足、升級後難以驗證的模組。
輸出 docs/upgrade/impact-analysis.md。
```

**如何審查**：🔍 `grep -rn "import javax\." src/main/java | wc -l`，與報告數字比對；「未確認」的依賴由人到官方 Maven Central 或專案網站確認，不能讓 Agent 猜版本號。

#### 9.4.2 範本 U2：升級計畫與風險清單

```text
依 docs/upgrade/impact-analysis.md 產生 docs/upgrade/plan.md：
- 分批：每批一個 PR，每批都能獨立建置與測試通過。建議順序：
  (1) 清 deprecation (2) Java 17 (3) Spring Boot 3 + jakarta (4) Security 設定 (5) Java 21。
- 每批：修改範圍、預估檔案數、驗證方式、回復方式、風險（高／中／低）與緩解。
- 標出需要人工決策的地方（例如替換不再維護的函式庫）。
不要修改程式碼。
```

#### 9.4.3 範本 U3：最小範圍修改（執行單一批次）

```text
只執行 docs/upgrade/plan.md 的「批次 3：Spring Boot 3 + jakarta」。
- 在 ai/upgrade-batch-3 分支作業；只做計畫列出的修改，不順手重構、不改格式、不升級計畫外的依賴。
- 每類修改一個 commit（pom.xml、javax→jakarta、屬性改名）。
- 遇到計畫沒預料到的問題，停下來回報，不要自行擴大範圍。
- 完成後輸出交付報告（修改清單、測試結果、未完成與待確認），並附 git diff --stat。
```

**如何審查**：

| 檢查 | 方法 |
|---|---|
| 範圍是否膨脹 | 🔍 `git diff --stat origin/main` 的檔案數 vs 計畫預估；超出 20% 要求解釋 |
| 是否混入格式化 | 🔍 `git diff -w --stat`（忽略空白）與 `git diff --stat` 差很多，代表有大量空白變更 |
| 是否偷改測試 | 🔍 `git diff origin/main -- src/test` 逐行看；刪除斷言或加 `@Disabled` 一律退回 |
| 報告誠實性 | ✅ `check-change-report.py` |

❌ **壞例**：Agent 為了讓編譯通過，把找不到 Jakarta 版本的函式庫整段註解掉，報告寫「已移除未使用的依賴」。對策：計畫中「需要人工決策」的項目，Prompt 明確要求停下來回報。

### 9.5 升級前後行為比對

| 比對項目 | 方法 | 工具 |
|---|---|---|
| API 回應 | 同一組請求打舊版與新版，比對 JSON（忽略時間戳、ID） | 契約測試、錄製回放 |
| 錯誤格式 | Spring Boot 3 的錯誤回應格式可能改變 | E2E |
| 資料庫寫入 | 同一批交易，比對資料表內容 | Testcontainers＋比對 SQL |
| 效能 | p95 延遲、記憶體、啟動時間 | JMeter、Gatling |
| 安全標頭 | `Strict-Transport-Security`、CSRF 行為 | ZAP baseline |
| 日誌格式 | 監控與告警依賴的欄位是否改變 | 人工比對 |

### 9.6 升級報告、回復方案與驗收清單

升級報告範本：

| 欄位 | 內容 |
|---|---|
| 升級範圍 | Java 11 → 21、Spring Boot 2.7.18 → 3.3.x |
| 批次與 PR | 批次 1～5，PR #101～#105 |
| 測試結果 | CI 連結；單元／整合／E2E 通過數與失敗數 |
| 行為差異 | 9.5 的比對結果與判定 |
| 已知問題 | 編號、影響、暫行方案 |
| 回復方案 | 回到 tag `pre-upgrade-20261027` 的部署步驟、資料庫是否需要回復 |
| 簽核 | 開發、QA、資安、維運 |

驗收清單：

- [ ] 所有批次的 CI 全綠（不是 Agent 報告說綠）。
- [ ] 沒有被停用或刪除的測試；覆蓋率不低於升級前。
- [ ] SCA 掃描沒有新增 Critical／High。
- [ ] 9.5 的行為比對差異都有判定與負責人。
- [ ] 回復方案在測試環境演練過一次。
- [ ] 部署環境（JRE、AP Server、容器基底）已同步升級並驗證。

### 9.7 本章實務案例與注意事項

**案例**：Agent 一次 PR 改了 412 個檔案（計畫預估 180），CI 全綠。

審查發現：其中 230 個檔案只是 import 排序與空白調整（Agent 的格式化習慣），真正的邏輯變更被淹沒；而且一支 `@Scheduled` 批次因 Spring Boot 3 的排程執行緒池預設改變而變成序列執行——CI 沒有效能測試，所以沒抓到。

改善：

1. Prompt 加入「不改格式」，並在 CI 加入 formatter check 讓格式化變更獨立成 PR。
2. 批次作業加入執行時間的監控與 9.5 的效能比對。
3. 退回重做，按計畫拆成 5 個 PR。

**注意事項**：

- 升級用的沙盒同樣只開必要端點（內部 Maven 代理、內部 Git）；讓 Agent 自己上網找「最新版本」會引入未審查的依賴。
- 版本號由人確認並寫進計畫；Agent 只負責照計畫修改。
- 升級完成不等於可上線：仍需走第 10 章的 SSDLC 關卡。

## 第10章 企業 SSDLC 與 AI 協作流程

本章把 NemoClaw 放進企業的安全軟體開發生命週期（SSDLC）。核心是三方分工：**人員負責決策、AI 負責受控輔助、工具負責客觀驗證**。任何一方都不能取代另外兩方。參考框架：[NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)、[OWASP SAMM](https://owaspsamm.org/)、[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)、[OWASP Top 10](https://owasp.org/Top10/)、[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)。

### 10.1 三方分工模型

```mermaid
flowchart LR
    subgraph HUMAN["人員：決策與負責"]
        H1["定義需求與驗收標準"]
        H2["核准計畫與網路白名單"]
        H3["Code Review 與合併"]
        H4["上線決策"]
    end
    subgraph AI["AI Agent：受控輔助（在 NemoClaw 沙盒內）"]
        A1["草擬文件"]
        A2["實作與重構"]
        A3["產生測試"]
        A4["交付報告"]
    end
    subgraph TOOL["工具：客觀驗證（在 CI 內）"]
        T1["建置與測試"]
        T2["SAST、SCA、機密掃描"]
        T3["ArchUnit、交付報告比對"]
        T4["政策 lint"]
    end
    H1 --> A1
    A1 --> H2
    H2 --> A2
    A2 --> A3 --> A4
    A4 --> T1 --> T2 --> T3
    T3 --> H3 --> H4
    T4 --> H2
```

| 角色 | 擁有 | 不能做 |
|---|---|---|
| 人員 | 決策權、核准權、責任 | 把「AI 說通過」當成通過 |
| AI Agent | 在沙盒內讀寫工作副本、呼叫核准的端點 | 合併主線、改 CI、改政策、取得正式憑證 |
| 工具 | 可重現的判定（通過／失敗） | 理解需求是否正確 |

### 10.2 各階段的 AI 適用範圍

| 階段 | 輸入 | AI 工作 | 輸出產物 | 品質門檻 | 人工核准點 |
|---|---|---|---|---|---|
| 需求分析 | 原始需求、訪談紀錄 | 整理 SRS 草稿、找出模糊處（7.6.1） | SRS 草稿、Q 清單 | 每條 FR 可追溯；Q 清單已回覆 | 需求方簽核 SRS |
| 系統分析與設計 | SRS、架構規範 | 草擬 SDD、序列圖、DDL、ADR（7.6.2） | SDD、OpenAPI | Mermaid 可渲染；依賴方向正確 | 架構師核准 |
| 程式開發 | SDD、OpenAPI、AGENTS.md | 依核准計畫小步實作（7.6.4～7.6.5） | `ai/` 分支、交付報告 | `check-change-report` 0 問題；`check-layering` 0 違規 | 開發者核准計畫 |
| 程式碼審查 | PR diff | 產生問題清單草稿（7.6.9） | Review 意見 | 高嚴重度問題全部處理 | **Code Reviewer 核准合併** |
| 單元測試 | 程式碼、規則 | 補邊界與例外測試（7.6.6） | 測試程式 | CI 通過；覆蓋率不下降；無停用測試 | Reviewer 確認測試有斷言 |
| 整合測試 | API、資料庫 | 草擬 Testcontainers 測試 | 整合測試 | CI 通過 | QA |
| 效能測試 | 非功能需求 | 草擬 JMeter／Gatling 腳本 | 腳本 | 在測試環境由工具量測 | 效能負責人 |
| 弱點掃描 | 原始碼、映像檔 | 解讀掃描結果、草擬修補 | 修補 PR | 無 Critical；High 有例外單 | 資安 |
| UAT | 驗收案例 | 草擬測試案例與資料（合成） | UAT 案例 | 業務人員實際操作 | **業務簽核** |
| 部署與上線 | 建置產物、部署說明 | 草擬部署與回復步驟 | Runbook | 演練過回復 | **變更管理會議** |
| 維運與問題追蹤 | 日誌（去敏）、錯誤報告 | 初步分析根因 | 分析報告 | 可重現步驟 | 維運負責人 |

> ⚠️ **警告**：「部署與上線」階段的 AI 只能**草擬文件**，不得持有部署憑證或連線正式環境。NemoClaw 沙盒在 alpha 階段不應有任何通往正式環境的網路路徑（14.8）。

### 10.3 Git、分支與 Pull Request 規範（🏢）

| 規則 | 說明 |
|---|---|
| Agent 只能推 `ai/*` 分支 | Git Server 的分支權限限制 AI 用的 Token；寫入 preset 也只放行特定 repo 的 `git-receive-pack` |
| 主線受保護 | `main`／`release/*` 需要 PR、CI 通過、至少一位人類核准 |
| Commit 標示 AI 參與 | Commit 訊息加 trailer，例如 `AI-Assisted: NemoClaw v0.0.139 / dcode 0.1.71 / sandbox dev-order` |
| PR 必附交付報告 | 放在 `.ai-reports/<分支名>.md`，CI 自動比對 |
| CODEOWNERS | `.github/`、CI 設定、`presets/`、`AGENTS.md` 由指定人員審查 |
| 不讓 Agent 改 CI | AGENTS.md 禁止；CODEOWNERS 強制 |

PR 範本（`.github/pull_request_template.md`）：

```markdown
## 變更摘要

## AI 參與
- [ ] 本 PR 有 AI Agent 參與（NemoClaw 沙盒：___，Agent／版本：___）
- [ ] 交付報告：`.ai-reports/___.md`
- [ ] 我已閱讀完整 diff，不只是交付報告

## 驗證
- [ ] CI 全綠（連結：___）
- [ ] 沒有停用或刪除既有測試
- [ ] 沒有新增未核准的依賴

## 安全
- [ ] 沒有憑證、個資、客戶資料
- [ ] 沒有修改 CI、政策 preset、AGENTS.md（若有，已由 CODEOWNERS 審查）
```

### 10.4 CI/CD 中的品質與安全關卡

以下 GitHub Actions 範例示意關卡順序（🧪 未在實際 repo 執行；工具版本請依企業標準固定）：

```yaml
# .github/workflows/ai-pr-gates.yml
name: ai-pr-gates
on:
  pull_request:
    branches: [main]
jobs:
  gates:
    runs-on: ubuntu-24.04
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: 機密掃描
        run: docker run --rm -v "$PWD:/repo" zricethehacker/gitleaks:v8.21.2 detect --source /repo --no-banner

      - name: AI 交付報告比對（僅 ai/ 分支）
        if: startsWith(github.head_ref, 'ai/')
        run: |
          report=".ai-reports/${GITHUB_HEAD_REF#ai/}.md"
          test -f "$report" || { echo "缺少交付報告 $report"; exit 1; }
          python3 tools/check-change-report.py "$report" "origin/${GITHUB_BASE_REF}"

      - name: 架構快篩
        run: python3 tools/check-layering.py src/main/java com.example.order

      - name: 政策 preset lint（若有變更）
        run: |
          pip install pyyaml==6.0.3
          files=$(git diff --name-only "origin/${GITHUB_BASE_REF}" -- 'presets/*.yaml')
          [ -z "$files" ] || python3 tools/nemoclaw-policy-lint.py preset $files

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '21'
          cache: maven

      - name: 建置、單元測試、ArchUnit、整合測試（Testcontainers）
        run: mvn -B -ntp verify

      - name: 依賴弱點掃描
        run: mvn -B -ntp org.owasp:dependency-check-maven:check -DfailBuildOnCVSS=9

      - name: 前端
        working-directory: web
        run: |
          npm ci
          npm run lint
          npx vue-tsc --noEmit
          npm run test:unit

      - name: SBOM
        run: mvn -B -ntp org.cyclonedx:cyclonedx-maven-plugin:makeAggregateBom
```

> 📌 **註記**：`check-change-report.py` 需要 `fetch-depth: 0` 才能取得 base 分支；`GITHUB_HEAD_REF` 的 `/` 會成為報告檔名的一部分，請依專案的分支命名調整。

### 10.5 測試證據與稽核保存

| 證據 | 來源 | 保存位置（🏢） | 保存期限建議 |
|---|---|---|---|
| 交付報告 | Agent | repo `.ai-reports/` | 隨程式碼 |
| CI 執行紀錄與報告 | CI | CI 系統、artifact 庫 | 依企業稽核規範 |
| 政策變更紀錄 | PR | `presets/` 的 Git 歷史 | 永久 |
| `openshell term` 核准紀錄 | 操作者手動記錄 | 變更單 | 依規範 |
| 沙盒日誌 | `nemoclaw <名稱> logs` | 日誌平台（14.7） | 依規範 |
| Agent 對話紀錄 | `sessions export`（OpenClaw／Hermes） | 受控儲存（含敏感資料） | 依規範，需存取控制 |
| 安裝驗收（4.10） | 操作者 | 環境申請單 | 隨環境 |

### 10.6 本章實務案例與注意事項

**案例**：稽核要求「證明這個上線版本中 AI 寫的程式都經過人工審查」。

可提出的證據鏈：

1. Git 歷史中帶 `AI-Assisted` trailer 的 commit 清單（`git log --grep='AI-Assisted'`）。
2. 每個相關 PR 的人工核准紀錄與 PR 範本勾選（「我已閱讀完整 diff」）。
3. CI 對每個 PR 的 `check-change-report`、ArchUnit、掃描結果。
4. 該時期使用的 NemoClaw 版本與政策 preset 版本（12.2 的盤點表、`presets/` 的 Git tag）。

**注意事項**：

- 品質門檻要在 CI 強制，而不是寫在 Prompt 裡「請確保測試通過」。
- AI 參與的程度越高，Code Review 的標準越不能降低；reviewer 疲勞是真實風險，PR 要小。
- 工具版本（gitleaks、Dependency-Check、PyYAML）要固定，避免 CI 結果因工具升級而漂移。

## 第11章 系統維護、監控與故障排除

官方 Troubleshooting 頁超過 3,000 行、上百個情境。本章整理企業最常遇到的 12 類問題，每類依「症狀／可能原因／檢查方式／解決方法（風險由低到高）／驗證方式／預防措施」六欄呈現。所有診斷指令標示執行位置；會刪資料或重新初始化的步驟以 ⛔ 標示。

### 11.1 診斷的三個起手式

```bash
# 🖥️ Host：任何問題先跑這三個（都是唯讀）
nemoclaw doctor                       # 主機、Runtime、OpenShell CLI、登錄、Gateway
nemoclaw <名稱> status                # 單一沙盒：Phase、Agent、Inference、恢復提示
nemoclaw <名稱> logs --tail 100       # 最近的生命週期、Gateway、政策拒絕
```

需要回報上游或交給內部支援時：

```bash
# 🖥️ Host：收集診斷包（上傳前人工檢查是否含主機名、內部 URL、使用者名稱）
nemoclaw debug --sandbox <名稱> --output ~/nemoclaw-debug-$(date +%Y%m%d%H%M).tgz
tar tzf ~/nemoclaw-debug-*.tgz | head -50
```

### 11.2 每日巡檢

| 檢查 | 指令（🖥️ Host） | 正常 | 異常處理 |
|---|---|---|---|
| CLI 版本未漂移 | `nemoclaw --version` | 與 12.2 盤點表一致 | 查是誰升級（`~/.nemoclaw/` 時間戳） |
| 全域狀態 | `nemoclaw status` | Gateway healthy | 11.3.4 |
| 沙盒健康 | `nemoclaw <名稱> status` | `Ready`、Inference healthy | 11.3.5～11.3.7 |
| 過期沙盒 | `nemoclaw upgrade-sandboxes --check` | 結束碼 0 | 排入維護窗口 `rebuild` |
| 政策漂移 | `nemoclaw <名稱> policy list` 與 Git 中的 preset 清單比對 | 一致 | 查 `openshell term` 是否有未記錄的核准 |
| 拒絕紀錄 | `nemoclaw <名稱> logs --since 24h` | 拒絕次數在基準內 | 異常增加 → 6.10 事件流程 |
| 磁碟 | `df -h ~ /var/lib/docker` | 可用 > 20% | 11.3.11 |
| 推理費用 | 供應商主控台 | 在預算內 | 暫停沙盒、查用量 |

把上表做成一支腳本，每天開工跑一次（🏢；🧪 依官方指令撰寫、未實機執行；`list --json` 的欄位名稱沿用 12.2 的假設，第一次使用前先確認）：

```bash
#!/usr/bin/env bash
# nemoclaw-daily.sh — 🏢 每日巡檢（唯讀）。任何一項異常就以結束碼 1 結束，方便排程判斷
APPROVED=${APPROVED:-0.0.139}          # 平台管理者公告的核准版本
PRESET_LIST=${PRESET_LIST:-presets.txt} # 從 presets repo 匯出的「應有 preset」清單，每行一個
rc=0
v=$(nemoclaw --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
[ "$v" = "$APPROVED" ] && echo "OK   版本 $v" || { echo "FAIL 版本 $v ≠ 核准 $APPROVED"; rc=1; }
nemoclaw upgrade-sandboxes --check >/dev/null 2>&1 && echo "OK   沙盒映像檔為最新" || { echo "WARN 有過期沙盒，排入維護窗口"; rc=1; }
for s in $(nemoclaw list --json | jq -r '.sandboxes[].name'); do
  nemoclaw "$s" status --json | jq -r --arg s "$s" \
    '"\(if .failureLayer == null and .inferenceHealth == "ok" then "OK  " else "FAIL" end) \($s) phase=\(.phase) inference=\(.inferenceHealth) failure=\(.failureLayer)"'
  nemoclaw "$s" policy list 2>/dev/null | sort > "/tmp/$s.policy"
  if [ -f "$PRESET_LIST" ] && ! diff -q <(sort "$PRESET_LIST") "/tmp/$s.policy" >/dev/null; then
    echo "FAIL $s 政策與 presets repo 不一致：diff <(sort $PRESET_LIST) /tmp/$s.policy"; rc=1
  fi
done
exit $rc
```

| 輸出 | 判讀 |
|---|---|
| 全部 `OK`、結束碼 0 | 可以開工 |
| `FAIL 版本` | 有人自行升級或安裝程式抓到 `lkg`：查 `~/.nemoclaw/` 時間戳，依 13.10 處理 |
| `FAIL <沙盒> … failure=docker_unreachable` | Docker 沒在跑：11.3.3 |
| `FAIL <沙盒> … inference=unauthorized` | Key 失效或被撤銷：11.3.7 |
| `FAIL <沙盒> 政策…不一致` | 有人在 `openshell term` 核准了未記錄的規則，或 preset 被移除：6.10 |

> ⚠️ **警告**：`policy list` 的輸出格式不是穩定介面，直接 `diff` 可能因格式差異誤報。第一次使用時，先人工對照輸出，再調整 `presets.txt` 的寫法。這一段標 🧪 就是這個原因。

### 11.3 常見問題卡

#### 11.3.1 安裝失敗或版本不相容

| 欄位 | 說明 |
|---|---|
| 症狀 | 安裝程式中止；或 onboarding 印出 `openshell <version> is above the maximum supported by this NemoClaw release` |
| 可能原因 | 平台不支援（Intel Mac、非 apt 發行版）；Node.js 太舊；缺 `sha256sum`／`strings`；有人自行升級了 OpenShell |
| 檢查方式 | 🖥️ `openshell --version`；`grep -n openshell_version "$(npm root -g)/nemoclaw/nemoclaw-blueprint/blueprint.yaml"`（🧪 路徑依 npm 全域 prefix 或 `~/.local` shim 安裝方式而定）；`node -v`；`command -v sha256sum strings` |
| 解決方法 | ① 依錯誤安裝缺少的工具（`sudo apt-get install -y binutils`）② 以固定版本重跑已審查的安裝程式，讓它安裝相容的 OpenShell ③ 確認不是在不支援的平台 |
| 驗證方式 | `nemoclaw doctor` 全部通過；`nemoclaw --version` 為預期版本 |
| 預防措施 | 禁止單獨 `openshell self-update`／`npm update -g openshell`（13.11）；版本固定寫進環境申請單 |

#### 11.3.2 CLI 找不到或環境變數未生效

| 欄位 | 說明 |
|---|---|
| 症狀 | `nemoclaw: command not found`；或 `NEMOCLAW_DISABLE_TELEMETRY` 設了卻好像沒效 |
| 可能原因 | nvm／fnm 沒更新目前 shell 的 PATH；CLI 以 shim 裝在 `~/.local/bin`；環境變數放在管線左側（`VAR=1 curl … \| bash` 只影響 `curl`） |
| 檢查方式 | 🖥️ `ls -l ~/.local/bin/nemoclaw`；`echo $PATH`；`env \| grep NEMOCLAW_` |
| 解決方法 | ① `source ~/.bashrc` 或開新終端機 ② 把 `~/.local/bin` 加入 PATH ③ 安裝相關變數改放在 `bash` 那一側或先 `export` |
| 驗證方式 | `command -v nemoclaw`、`nemoclaw --version` |
| 預防措施 | 在 `~/.bashrc` 固定 `export NEMOCLAW_DISABLE_TELEMETRY=1`；SOP 統一寫法 |

#### 11.3.3 Docker、WSL 2 或沙盒啟動失敗

| 欄位 | 說明 |
|---|---|
| 症狀 | `docker info` 失敗；`Cannot connect to the Docker daemon`；`permission denied`；onboarding 逾時 `did not become ready within Ns`；exit 137 |
| 可能原因 | Docker 未啟動；使用者不在 `docker` 群組（或群組未在目前 shell 生效）；Docker Desktop 沒開 WSL integration；記憶體不足被 OOM；cgroup v2 問題 |
| 檢查方式 | 🖥️ `systemctl status docker`；`id -nG`；🐧 `docker info`；🪟 `wsl -l -v`；`dmesg \| grep -i oom`（🧪 需權限） |
| 解決方法 | ① 啟動 Docker（Linux `sudo systemctl start docker`；Windows 開 Docker Desktop）② `newgrp docker` 後重跑 ③ Docker Desktop → Settings → Resources → WSL integration 勾選發行版 ④ 記憶體不足時建立 swap（官方步驟：4 GB `/swapfile`）⑤ 提高 `NEMOCLAW_SANDBOX_READY_TIMEOUT` |
| 驗證方式 | `docker run --rm busybox true` 成功；`nemoclaw onboard --resume` 完成 |
| 預防措施 | 主機規格依 3.2 的企業建議；WSL 主機固定 Docker Desktop 版本 |

#### 11.3.4 Gateway 連線異常

| 欄位 | 說明 |
|---|---|
| 症狀 | `connect` 因 Gateway down 退出；`status` 顯示 Gateway unhealthy；連接埠 8080 被占用 |
| 可能原因 | OpenShell Gateway 程序沒啟動（主機重開機後最常見）；連接埠衝突；systemd user manager 不可用 |
| 檢查方式 | 🖥️ `systemctl --user status openshell-gateway`；`ss -ltnp \| grep 8080`；`nemoclaw doctor` |
| 解決方法 | ① Linux：`systemctl --user restart openshell-gateway`，再 `nemoclaw <名稱> recover` ② macOS：重跑 NemoClaw 安裝程式讓它修復受管的 Homebrew 服務（官方建議，不要直接 `brew services`）③ 連接埠衝突：停掉占用程序，或依官方指引以 `NEMOCLAW_GATEWAY_PORT` 使用替代連接埠 |
| 驗證方式 | `nemoclaw status` Gateway healthy；`nemoclaw <名稱> connect` 成功 |
| 預防措施 | 開機後的「Reconnect after a host reboot」步驟寫成 SOP；官方不保證重開機後自動復原 |

#### 11.3.5 Agent 無法回應

| 欄位 | 說明 |
|---|---|
| 症狀 | Dashboard 打不開；TUI 沒反應；`dcode -n` 逾時（結束碼 124） |
| 可能原因 | 沙盒內 Agent Gateway 停了；沙盒 Stopped；推理逾時；OpenClaw 裝置配對未完成（`scope upgrade pending approval`） |
| 檢查方式 | 🖥️ `nemoclaw <名稱> status`；`nemoclaw <名稱> logs --tail 100`；📦 `dcode status` |
| 解決方法 | ① `nemoclaw <名稱> recover` ② `nemoclaw <名稱> gateway restart` ③ 沙盒 Stopped：`nemoclaw <名稱> start` ④ OpenClaw 配對：`nemoclaw onboard --resume` ⑤ 仍失敗：`rebuild`（會保留原生 home） |
| 驗證方式 | 4.9 的測試請求成功 |
| 預防措施 | 監控 `status --json` 的 Phase；推理逾時見 11.3.6 |

#### 11.3.6 模型推理服務連線失敗

| 欄位 | 說明 |
|---|---|
| 症狀 | `status` 的 Inference 行逾時；Agent 回報 TLS 或連線錯誤；本地 Ollama／vLLM 不可達 |
| 可能原因 | 推理端點不可達（企業防火牆）；企業 TLS 攔截但未設 CA；本地服務沒啟動或綁錯介面；IPv6 解析問題 |
| 檢查方式 | 🖥️ `nemoclaw <名稱> status`（會從沙盒內走實際路徑探測）；`curl -sS -m 10 https://integrate.api.nvidia.com/v1/models -o /dev/null -w '%{http_code}'`；本地：`curl -sS http://127.0.0.1:11434/api/tags` |
| 解決方法 | ① 開通防火牆到推理端點 ② 設 `NEMOCLAW_CORPORATE_CA_BUNDLE` 後 `rebuild` ③ 啟動本地服務 ④ 慢速網路或大模型：`export NEMOCLAW_LOCAL_INFERENCE_TIMEOUT=300` 後重新 onboarding |
| 驗證方式 | `status` Inference healthy；4.9 測試成功 |
| 預防措施 | 推理端點列入網路白名單基準；本地服務設為系統服務 |

#### 11.3.7 API Key 或 Provider 設定錯誤

| 欄位 | 說明 |
|---|---|
| 症狀 | `status` 回報 `unauthorized`（HTTP 401／403）；onboarding 驗證失敗；換了 Key 仍用舊的 |
| 可能原因 | Key 過期或撤銷；額度用完；選錯 Provider；Hermes 原生 NVIDIA 路由的憑證參照過期 |
| 檢查方式 | 🖥️ `nemoclaw credentials list`（只證明存在）；`nemoclaw <名稱> status`（實際驗證）；`nemoclaw inference get` |
| 解決方法 | ① 依 6.6 以新 Key 重跑 `nemoclaw onboard --name <名稱>` ② Hermes 憑證參照過期：`nemoclaw <名稱> rebuild --yes` ③ 沒有替代 Key 且需立即停用：`nemoclaw credentials reset <Provider>` |
| 驗證方式 | `nemoclaw <名稱> agent …` 或 `dcode -n` 回覆預期字串 |
| 預防措施 | Key 到期前 14 天輪替；供應商端設額度告警 |

#### 11.3.8 網路政策阻擋必要服務

| 欄位 | 說明 |
|---|---|
| 症狀 | `CONNECT tunnel failed, response 403`；`exec` 失敗時 stderr 出現 `recent network policy denial detected for <host>:<port>` |
| 可能原因 | 端點不在政策中；binary 不符（例如 preset 只放行 `git`，卻用 `curl`）；方法或路徑不符；私有 IP 被 SSRF 防護擋下；Personal 層以外的 `host.docker.internal` 路徑 |
| 檢查方式 | 🖥️ `nemoclaw <名稱> logs --tail 50`（看被拒的 host、binary）；`nemoclaw <名稱> policy list`；`openshell policy get <名稱>`；`openshell term` 觀察即時請求 |
| 解決方法 | ① 確認需求是否合理（可能是被誘導的請求）② 已有核准的 preset 卻沒套用：`policy add` ③ 新需求：走 13.4 申請、6.11 撰寫、6.16 審查 ④ 私有主機：`--trusted-private-host` ⑤ 一次性需求：在 `openshell term` 核准單一規則 |
| 驗證方式 | 6.12 的 V1～V6 |
| 預防措施 | preset 放 Git 並在 onboarding 時一併套用；官方提醒：能在建置期安裝的套件就不要在執行期下載 |

#### 11.3.9 檔案權限不足

| 欄位 | 說明 |
|---|---|
| 症狀 | `Permission denied`、`Read-only file system`；`tmux` 顯示 `fork failed: Permission denied`；Deep Agents 啟動失敗 |
| 可能原因 | 寫到唯讀路徑（設計如此）；`--host-mount` 本來就是唯讀；Landlock `strict`（Deep Agents）無法執行而 fail closed；用 `docker exec` 以 root 改過檔案造成擁有者錯亂 |
| 檢查方式 | 📦 `id`、`ls -ld <路徑>`；🖥️ `nemoclaw <名稱> doctor`；`awk '$2=="/sandbox/src"{print $4}' /proc/mounts`（📦） |
| 解決方法 | ① 改寫到 `/sandbox` 或 `/tmp` ② 需要寫回主機時改用 `download` 或 Git，而不是要求讀寫掛載 ③ 核心不支援 Landlock：升級到 5.13 以上的核心 ④ 權限錯亂：`rebuild` |
| 驗證方式 | 4.10 的檢查 2、3 符合預期 |
| 預防措施 | 禁止 `docker exec` 操作沙盒；工作目錄統一在 `/sandbox/work` |

#### 11.3.10 狀態保存或恢復失敗

| 欄位 | 說明 |
|---|---|
| 症狀 | `rebuild` 中斷；`backup-all` 報 incomplete backup；`sandboxes.json` 不是有效 JSON；沙盒在登錄中但 Gateway 找不到 |
| 可能原因 | 重建過程被中斷；原生 home 內放了憑證導致封存的憑證掃描失敗；登錄檔損壞；Gateway 重建後遺失沙盒 |
| 檢查方式 | 🖥️ `nemoclaw list --json`；`ls -la ~/.nemoclaw/rebuild-backups/`；`python3 -m json.tool ~/.nemoclaw/sandboxes.json` |
| 解決方法 | ① 中斷的重建：以相同設定重跑 `nemoclaw <名稱> rebuild`（官方：不要手動刪 `onboard-session.json` 或 `.onboard-rebuild-<名稱>.json`）② 封存失敗：移除原生 home 內的明文憑證 ③ 登錄檔損壞：`cp ~/.nemoclaw/sandboxes.json ~/.nemoclaw/sandboxes.json.bad && rm ~/.nemoclaw/sandboxes.json`（官方步驟；⛔ 先備份）④ 沙盒已不存在：⛔ `nemoclaw <名稱> destroy` 清除紀錄後重新 onboarding，再以獨立備份還原 |
| 驗證方式 | `nemoclaw list` 正常；`status` Ready；工作目錄內容完整 |
| 預防措施 | 重建前額外做 5.10 的獨立備份；不在原生 home 放憑證 |

#### 11.3.11 磁碟不足、資源耗盡或效能下降

| 欄位 | 說明 |
|---|---|
| 症狀 | 映像檔推送失敗；建置變慢或卡住；主機回應遲緩；DGX Spark 上本地 vLLM 負載時主機凍結 |
| 可能原因 | 舊沙盒映像檔累積；`rebuild-backups/` 累積；容器 Runtime 資源配置不足（Colima、Docker Desktop）；本地模型吃滿記憶體 |
| 檢查方式 | 🖥️ `df -h`；`docker system df`；`du -sh ~/.nemoclaw/rebuild-backups/`；`nemoclaw resources --json` |
| 解決方法 | ① `nemoclaw gc --dry-run` 後 `nemoclaw gc --yes` ② 清理過期的 `rebuild-backups/`（⛔ 確認已有其他備份）③ 調高 Docker Desktop／Colima 的 CPU 與記憶體 ④ 停止不用的沙盒（`stop`）⑤ 本地模型改用較小的 profile |
| 驗證方式 | 可用空間 > 20%；onboarding 或 rebuild 完成 |
| 預防措施 | 每週例行 `gc`；備份保留策略（12.3） |

#### 11.3.12 升級後服務無法啟動

| 欄位 | 說明 |
|---|---|
| 症狀 | 升級後 `Installation completed with warnings`；沙盒 not Ready；`connect` 警告 Agent 版本過期；舊沙盒無法 resume 或 rebuild |
| 可能原因 | 升級程序中某沙盒的備份或自動重建失敗；舊版沙盒沒有原生 Provider 附掛（2.6）；OpenShell Gateway 版本不符 |
| 檢查方式 | 🖥️ 安裝程式輸出的 recovery 訊息；`nemoclaw upgrade-sandboxes --check`；`nemoclaw <名稱> status` |
| 解決方法 | ① 依安裝程式提示的備份路徑與指令處理（`nemoclaw onboard --resume`／`nemoclaw <名稱> rebuild`）② 舊版沒有附掛的沙盒：先備份，再 `nemoclaw onboard --fresh --name <名稱> --recreate-sandbox`（⛔ 會取代原沙盒）③ 無法修復：依 12.6 回復到舊版 |
| 驗證方式 | `upgrade-sandboxes --check` 結束碼 0；4.10 驗收重跑通過 |
| 預防措施 | 先在測試主機演練（12.4）；升級前 `backup-all`＋獨立備份 |

### 11.4 故障排除紀錄範本

| 欄位 | 填寫內容 |
|---|---|
| 紀錄編號 | TS-2026-0001 |
| 日期時間 | 2026-10-27 14:30 |
| 主機與沙盒 | dev-host-07／dev-order |
| 版本 | NemoClaw v0.0.139、OpenShell 0.0.116、dcode 0.1.71 |
| 症狀 | （使用者觀察到的現象、錯誤訊息原文） |
| 問題卡分類 | 11.3.x |
| 診斷步驟與輸出 | （指令＋重點輸出；敏感資訊遮蔽） |
| 根因 | — |
| 解決方法 | — |
| 驗證結果 | — |
| 預防措施 | — |
| 是否需更新規範或 preset | 是／否，PR 連結 |

### 11.5 本章實務案例與注意事項

**案例**：週一早上，整個部門的 NemoClaw 主機都顯示沙盒 Stopped。

原因：週末 OS 自動更新後重開機。官方說明重開機後容器 Runtime、OpenShell Gateway 與沙盒可能都沒有執行，自動復原不保證。

處置 SOP：

1. 🖥️ `sudo systemctl start docker`（若未自動啟動）。
2. 🖥️ `systemctl --user status openshell-gateway`，必要時 `restart`。
3. 🖥️ 每個沙盒 `nemoclaw <名稱> start`。
4. 🖥️ `nemoclaw <名稱> status` 確認 Ready，重跑 4.10 的檢查 1、5。

**注意事項**：

- 解決方法依「風險由低到高」排列；不要一開始就 `destroy` 或 `--recreate-sandbox`。
- 回報上游問題前，先確認版本是否為最新的 `lkg` 或 latest，並搜尋 GitHub Issues。
- 安全漏洞走 `SECURITY.md` 的私密管道，⛔ 不開公開 Issue。

## 第12章 版本升級、備份、復原與解除安裝

NemoClaw 約每週發布一版，而且它把 OpenShell、Agent 版本、沙盒映像檔都綁在一起。本章的前提是：**不要假設有完整的自動回復**。官方提供的是「重建時保留原生 home」與「升級前備份」；版本回退、跨版本還原，都需要人工備份與演練。

### 12.1 版本關係

```mermaid
flowchart TB
    NC["NemoClaw CLI v0.0.139<br/>安裝程式：lkg 或指定 tag"]
    BP["Blueprint<br/>min/max_openshell_version = 0.0.116"]
    OS["OpenShell 0.0.116<br/>CLI、Gateway、SDK"]
    IMG["沙盒映像檔<br/>三個 Agent 同一發佈批次<br/>以 sha256 digest 釘選"]
    AG["Agent 版本<br/>烤進映像檔：OpenClaw、Hermes、dcode 0.1.71"]
    MDL["模型<br/>由推理服務決定"]
    PRJ["專案依賴<br/>Maven、npm"]
    NC --> BP --> OS
    NC --> IMG --> AG
    AG -.->|"呼叫"| MDL
    AG -.->|"在工作副本中"| PRJ
```

| 元件 | 誰決定版本 | 如何升級 | 注意 |
|---|---|---|---|
| NemoClaw CLI | 安裝程式（預設 `lkg`） | 重跑安裝程式（指定 tag） | `nemoclaw update` 也走同一套安裝流程 |
| OpenShell | Blueprint 的版本範圍 | 隨 NemoClaw 安裝程式 | ⛔ 不可單獨升級 |
| 沙盒映像檔與 Agent | NemoClaw 版本 | `nemoclaw <名稱> rebuild` 或 `upgrade-sandboxes` | 官方：**不要在沙盒內就地更新 Agent**（Agent 綁在映像檔） |
| 模型 | 推理服務 | `inference set` 或重新 onboarding | 模型行為變化不在 NemoClaw 控制內 |
| 專案依賴 | 專案 | 第 9 章 | — |

### 12.2 升級前的版本盤點

🏢 盤點腳本（🧪 依官方指令撰寫，未實機執行；`--json` 欄位結構以實際輸出為準）：

```bash
#!/usr/bin/env bash
# nemoclaw-inventory.sh — 記錄目前環境與依賴版本（唯讀）
set -u
OUT=${1:-inventory-$(hostname)-$(date +%Y%m%d%H%M).md}
{
  echo "# NemoClaw 環境盤點 $(date -Iseconds)"
  echo "## 主機"
  echo '```text'
  . /etc/os-release; echo "OS: $PRETTY_NAME"; echo "Kernel: $(uname -r)"
  echo "Docker: $(docker version --format '{{.Server.Version}}' 2>/dev/null || echo n/a)"
  echo "Node: $(node -v 2>/dev/null)  npm: $(npm -v 2>/dev/null)"
  echo '```'
  echo "## NemoClaw 與 OpenShell"
  echo '```text'
  nemoclaw --version
  openshell --version 2>/dev/null || echo "openshell: n/a"
  echo '```'
  echo "## 沙盒"
  echo '```json'
  nemoclaw list --json
  echo '```'
  for s in $(nemoclaw list --json | jq -r '.sandboxes[].name' 2>/dev/null); do
    echo "### $s"
    echo '```text'
    nemoclaw "$s" status 2>&1 | sed -n '1,40p'
    nemoclaw "$s" policy list 2>&1
    echo '```'
  done
  echo "## 需要升級的沙盒"
  echo '```text'
  nemoclaw upgrade-sandboxes --check 2>&1; echo "exit=$?"
  echo '```'
} > "$OUT"
echo "已寫入 $OUT"
```

> 📌 **註記**：`nemoclaw list --json` 的頂層欄位包含 `schemaVersion`、預設沙盒、復原中繼資料與沙盒清單（官方 Commands 說明）；上面以 `.sandboxes[].name` 取名稱是 🧪 假設，請先執行一次確認欄位名稱。

### 12.3 備份範圍

| 對象 | 位置 | 是否在 `rebuild` 內建封存中 | 建議備份方式 |
|---|---|---|---|
| Agent 原生 home／workspace | 沙盒內（OpenShell 儲存） | ✅ 是 | `backup-all`＋5.10 的獨立 `download` |
| 專案工作副本 | 沙盒 `/sandbox/work` | ✅ 是（在 home 下） | 優先 `git push` 到 `ai/` 分支；其次 `download` |
| OpenShell 政策 | OpenShell | 以即時政策整份帶過去 | `nemoclaw <名稱> policy get > policy-<名稱>.yaml`（憑證已遮蔽） |
| 自訂 preset 原始檔 | 企業 Git repo `presets/` | — | Git |
| 主機狀態 | `~/.nemoclaw/`（`config.json`、`sandboxes.json` 等） | — | 複製到安全位置（⛔ 不放進映像檔、Git 或支援包——官方安全建議） |
| 重建備份 | `~/.nemoclaw/rebuild-backups/` | — | 依保留政策 |
| 推理與 MCP 憑證 | OpenShell Gateway | ❌ **不在任何封存中** | 由企業密碼庫保管原始值；重建後重新註冊 |
| 設定匯出（為 v1 準備） | — | — | `nemoclaw config export <名稱> --output <檔>`（不含憑證值） |

> ⚠️ **警告**：官方 Persist Sandbox State 頁說明，`destroy` 會刪除沙盒的持久化狀態；Deep Agents 會清除整個保留的 `/sandbox` 根目錄。`destroy` 前必須先 `download` 需要的檔案。

### 12.4 測試環境的升級演練

| 步驟 | 動作 | 通過條件 |
|---|---|---|
| 1 | 在測試主機安裝與正式（試行）主機相同的版本，建立相同 preset 的沙盒 | 4.10 驗收通過 |
| 2 | 放入合成資料的工作副本 | — |
| 3 | 執行 12.2 盤點 | 存檔 |
| 4 | 依 12.5 升級到目標版本 | 安裝程式無 warning |
| 5 | `upgrade-sandboxes --check` | 結束碼 0 |
| 6 | 重跑 4.10、6.12 V1～V6 | 全部符合 |
| 7 | 跑一次 7.6.4 的開發任務 | 交付報告與 CI 通過 |
| 8 | 演練 12.6 的回復 | 能回到升級前狀態 |
| 9 | 讀新版 release notes，標出影響本企業的項目 | 寫進升級單 |

### 12.5 升級程序

```bash
# 🖥️ Host：1. 盤點與備份
bash nemoclaw-inventory.sh
nemoclaw backup-all
for s in dev-order re-legacy; do nemoclaw "$s" policy get > "policy-$s-$(date +%Y%m%d).yaml"; done

# 2. 取得並審查新版安裝程式（同 4.3）
NEW=v0.0.140          # 🧪 範例版本號，依實際 release 填寫
curl -fsSL "https://raw.githubusercontent.com/NVIDIA/NemoClaw/${NEW}/install.sh" -o "install-${NEW}.sh"
curl -fsSL "https://raw.githubusercontent.com/NVIDIA/NemoClaw/${NEW}/nemoclaw-blueprint/blueprint.yaml" \
  | grep -E '^(min|max)_openshell_version'          # 確認新版要求的 OpenShell 範圍

# 3. 升級（安裝程式會再備份一次、必要時汰換 Gateway、執行 upgrade-sandboxes --auto）
export NEMOCLAW_DISABLE_TELEMETRY=1
NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG="$NEW" bash "install-${NEW}.sh"

# 4. 確認
nemoclaw --version
nemoclaw upgrade-sandboxes --check; echo "exit=$?"
```

安裝程式的結果判讀（📖 Update Sandboxes）：

| 訊息 | 意義 | 處理 |
|---|---|---|
| Confirmed recovery | 既有沙盒已復原並升級 | 進行驗收 |
| `Installation completed with warnings` | 復原未確認，或記錄的沙盒在 Gateway 上找不到 | 依提示檢查，**不要**直接開始新 onboarding |
| 非零結束、備份被略過或失敗 | 升級在一般 onboarding 前中止 | 依保留的備份路徑處理 |

> 📌 **註記**：若既有 OpenShell 版本落在新版支援範圍外，安裝程式會在備份後汰換 Gateway 再替換 OpenShell；版本未知或範圍無效時會停止而不汰換。官方另有「手動準備的升級」流程（`backup-all --retire-legacy-forwards`＋`openshell gateway destroy`＋`NEMOCLAW_OPENSHELL_UPGRADE_PREPARED=1`），只在官方指示時使用。

### 12.6 升級失敗時的復原策略

| 情境 | 策略 | 支援程度 |
|---|---|---|
| 單一沙盒升級後異常 | `nemoclaw <名稱> rebuild`（以目前映像檔重建並還原 home） | 📖 官方支援 |
| 重建中斷 | 以相同設定重跑 `rebuild`（續作交易） | 📖 官方支援 |
| 新版 CLI 本身有問題，要回到舊版 | 明確指定舊版 tag 重跑安裝程式（`NEMOCLAW_INSTALL_TAG=v0.0.139`）；`lkg` 不會自動降級，`nemoclaw update` 有 `--allow-downgrade` | 🧪 官方未提供完整的降級保證：已用新映像檔重建的沙盒、新版寫入的狀態格式，舊版不一定讀得懂 |
| 沙盒無法修復 | 以獨立備份（5.10）＋重新 onboarding＋`upload` 還原 | 🏢 人工程序 |
| 主機整體損壞 | 新主機依第 4 章重建，從 Git 與獨立備份還原 | 🏢 人工程序（官方：獨立的機隊備份與災難復原是操作者責任） |

回復計畫範本：

| 欄位 | 內容 |
|---|---|
| 升級單號 | CHG-2026-0420 |
| 升級前版本 | NemoClaw v0.0.139／OpenShell 0.0.116 |
| 目標版本 | （填寫） |
| 回復觸發條件 | 4.10 任一項失敗；6.12 V1～V6 任一項不符；CI 任務成功率下降 > 20% |
| 回復步驟 | 1. 停止所有沙盒 2. 以舊版 tag 重跑安裝程式 3. 各沙盒 `upgrade-sandboxes --check` 4. 無法啟動者以獨立備份重新 onboarding＋`upload` 5. 重跑 4.10 |
| 資料保全 | `backup-all` 路徑、獨立備份路徑、`policy get` 匯出檔 |
| 預估時間 | （填寫） |
| 決策者 | （填寫） |

### 12.7 沙盒重建與狀態恢復的差異

| | `rebuild` | 獨立備份＋重新 onboarding＋`upload` |
|---|---|---|
| 觸發 | 升級 Agent、套用建置期設定 | 沙盒損壞、跨主機搬移、版本回退 |
| 搬移內容 | 完整原生 home／workspace（不需 allowlist） | 只有你下載的檔案 |
| 政策 | 目前的 OpenShell 即時政策整份帶過去 | 回到 onboarding 選的層級＋preset；自訂 preset 要重新套用 |
| 憑證 | 不在封存內；主機端設定重新套用 | 需重新註冊 |
| 主機端擁有的設定（推理、政策、訊息） | 依主機紀錄重新套用 | 依新 onboarding |
| 風險 | 原生 home 有明文憑證時會中止 | 漏下載檔案就遺失 |

怎麼證明 `rebuild` 沒有弄丟東西（🖥️ Host；🧪 未實機執行）：

```bash
# 1. 重建前：記錄政策與工作區檔案指紋
nemoclaw dev-order policy list | sort > before-policy.txt
nemoclaw dev-order exec -- sh -c \
  'cd /sandbox/work && find . -type f -not -path "*/.git/*" -exec sha256sum {} + | sort -k2' > before-files.txt
# 2. 重建
nemoclaw dev-order rebuild
# 3. 重建後：重新記錄並比對（兩個 diff 都應沒有輸出）
nemoclaw dev-order policy list | sort > after-policy.txt
nemoclaw dev-order exec -- sh -c \
  'cd /sandbox/work && find . -type f -not -path "*/.git/*" -exec sha256sum {} + | sort -k2' > after-files.txt
diff before-policy.txt after-policy.txt && diff before-files.txt after-files.txt && echo "rebuild 前後一致"
```

選擇範例：

| 情境 | 選擇 | 理由 |
|---|---|---|
| NemoClaw 從 v0.0.137 升到 v0.0.139，要讓 Agent 跟著升級 | `rebuild` | 只有換映像檔，原生 home 要完整帶過去 |
| 懷疑沙盒被 Prompt Injection 改過 `AGENTS.md` 或 Agent 記憶 | 獨立備份＋重新 onboarding | `rebuild` 會把被污染的 home 一起帶過去（6.18 的 ASI06） |
| 主機要退役，沙盒搬到新主機 | 獨立備份＋重新 onboarding＋`upload` | 封存與憑證都不能跨主機搬移 |

### 12.8 解除安裝前的資料保留與憑證撤銷

```bash
# 🖥️ Host：解除安裝前檢查表的指令部分
nemoclaw list
for s in $(nemoclaw list --json | jq -r '.sandboxes[].name'); do   # 🧪 欄位名稱見 12.2 註記
  nemoclaw "$s" download /sandbox/work/ "./final-backup/$s/work/"
done
nemoclaw credentials list          # 記下 Provider 名稱，到上游供應商撤銷對應 Key
nemoclaw uninstall                 # 預設保留 rebuild-backups/、backups/、sandboxes.json
```

| 步驟 | 動作 |
|---|---|
| 1 | 所有工作副本已推送到 Git 或下載 |
| 2 | 需要的對話紀錄已 `sessions export`（OpenClaw／Hermes） |
| 3 | 到推理供應商、MCP Server、Git Server **撤銷** NemoClaw 使用的 Key 與 Token（解除安裝不會撤銷上游憑證） |
| 4 | 執行 `nemoclaw uninstall`（多個 Gateway 連接埠時依提示使用 `--all-gateway-ports`） |
| 5 | 確認保留的 `~/.nemoclaw/` 內容，依資料保存規範決定是否刪除 |
| 6 | ⛔ `--delete-models` 會刪除 Ollama 回報的所有模型（包含其他應用程式使用的），確認後才使用 |
| 7 | 從資產清冊移除主機或標註停用 |

> 📌 **註記**：`nemoclaw uninstall` 執行的是已安裝套件內附的 `uninstall.sh`；若本機腳本遺失，CLI 不會自動下載遠端版本，而是印出對應版本的網址讓你下載審查後手動執行。只有 CLI 已損壞時才使用官方的 `curl … uninstall.sh | bash` 形式。

### 12.9 升級完成後的驗收

- [ ] `nemoclaw --version` 為目標版本；12.2 盤點表已更新。
- [ ] `nemoclaw upgrade-sandboxes --check` 結束碼 0。
- [ ] 每個沙盒 `status` 為 Ready、Inference healthy、Agent 版本為新版。
- [ ] 4.10 控制有效性驗證全部通過。
- [ ] 6.12 V1～V6 全部符合（政策沒有在升級中被放寬或遺失）。
- [ ] `policy list` 與 Git 中的 preset 清單一致。
- [ ] 一個代表性開發任務的交付報告與 CI 通過。
- [ ] 新版 release notes 中影響企業的項目已評估並記錄。

每一項的驗證指令與通過標準（▶️）：

| 驗收項目 | 指令（🖥️ Host） | 通過標準 |
|---|---|---|
| 版本 | `nemoclaw --version` | 等於目標版本 |
| 安全下限 | `bash check-security-floor.sh`（6.17.1） | 結束碼 0 |
| 沙盒映像檔 | `nemoclaw upgrade-sandboxes --check; echo $?` | `0` |
| 沙盒健康 | `nemoclaw <名稱> status --json \| jq '{phase, inferenceHealth, failureLayer}'` | `failureLayer` 為 `null`，`inferenceHealth` 為 `ok`（並照 4.9 實際送一次請求） |
| 控制有效 | 4.10 的驗收腳本 | 全部 PASS |
| 政策未被放寬 | 12.7 的 `policy list` 前後比對 | `diff` 沒有輸出 |
| 交付流程 | 選一個代表性任務跑完第 7 章流程 | CI 綠燈、`check-change-report.py` 0 項問題 |

❌ 壞例的驗收紀錄：「升級完成，Agent 可以正常對話」。這句話只證明推理通了，沒有證明政策沒被放寬、憑證沒有外洩、版本是對的。驗收紀錄要附上表中每一列的指令輸出。

### 12.10 升級檢查清單與維護紀錄表

升級檢查清單：

- [ ] 已閱讀目標版本 release notes 與 Platform Support 變更。
- [ ] 已確認目標版本的 OpenShell 版本範圍。
- [ ] 已在測試主機完成 12.4 演練。
- [ ] 已執行 12.2 盤點並存檔。
- [ ] 已 `backup-all`、獨立備份、`policy get` 匯出。
- [ ] 已通知使用者並排定維護窗口。
- [ ] 已準備 12.6 回復計畫並指定決策者。
- [ ] 升級後已完成 12.9 驗收。

維護紀錄表：

| 日期 | 主機 | 作業類型 | 變更前版本 | 變更後版本 | 執行者 | 驗收結果 | 備註／單號 |
|---|---|---|---|---|---|---|---|
| 2026-10-27 | dev-host-07 | 新安裝 | — | v0.0.139／OS 0.0.116 | （姓名） | 4.10 通過 | CHG-2026-0412 |
| | | 升級／rebuild／preset 變更／憑證輪替 | | | | | |

### 12.11 下一版升級預警：OpenShell 0.1.5 遷移（`main` 未發布）

研究日（2026-10-27）的狀態：

| 項目 | 狀態 | 來源 |
|---|---|---|
| `main` 的 Blueprint | `min_openshell_version` 與 `max_openshell_version` 仍為 `0.0.116` | `nemoclaw-blueprint/blueprint.yaml`＠`bafe6cc` |
| 升級 PR | #12603「upgrade OpenShell runtime and SDK to 0.1.5」：OPEN，PR 自述 *Not ready for approval or merge*，完整驗證尚未完成 | PR 描述 |
| 維護者決定 | 授權「進行 v0.1.5 依賴更新與驗證」，**不是**授權合併或發布；上游的 TLS、Personal 層網路存取與 GPU 問題仍未解決 | PR 描述引用的維護者留言 |
| 前置工作（已合併） | #13635、#13763：讓受信任的 E2E 控制器可以驗證 OpenShell 0.1.3／0.1.5 候選版 | PR 描述 |
| 最近一次完整 E2E | 74 通過、9 失敗、19 跳過；失敗集中在 Docker MCP bridge（三個 Agent）、Hermes GPU、Pi、Personal 層對外存取、受保護映像檔的 GPU 本地推理 | PR 描述 |

PR #13635 的重現測試在 0.1.x 候選版上發現 Gateway 設定、volume 掛載許可、受管啟動、復原查詢與原生推理都有不相容。下一版若改綁 0.1.5，預期影響如下：

| 影響面 | 預期變化 | 企業要準備的事 |
|---|---|---|
| 推理路由 | OpenShell 0.1.0 已移除 `inference.local`；PR 改用「附掛到沙盒的原生推理 Provider」 | 盤點仍走共享路由的沙盒（`status --json` 的 `recordedRoute`），升級後逐一驗證 4.9 |
| Gateway 與 SDK | CLI、SDK、Gateway、supervisor、映像檔與雜湊全部更新 | 自寫的腳本若解析 OpenShell 輸出，要重新測試 |
| 舊 volume | PR 原則是「保留舊 volume 不變、**不做自動複製**；所有權無法證明時，在修改前停止」 | 升級前一定要有 12.3 的獨立備份；做好「舊沙盒資料要手動搬」的準備 |
| 憑證與 Provider | PR 宣稱保留憑證保管方式與操作者擁有的 Provider | 升級後跑 13.5 的 placeholder 檢查，確認憑證沒有落地 |
| GPU | 維護者要求保留 GPU 支援，但 GPU 相關 E2E 仍有失敗 | 用本地 GPU 推理的主機最後才升級 |
| 備份 | 安裝程式在升級 OpenShell 前會用嚴格模式執行 `backup-all`，有一般沙盒被略過或失敗就中止 | 升級前把所有沙盒啟動起來，避免被略過而中止（📖 Commands 參考） |

自己追蹤進度（🖥️ Host，唯讀；✅ 研究日實際執行，以下是當日輸出）：

```bash
gh pr view 12603 -R NVIDIA/NemoClaw --json state,isDraft,mergedAt,title
# {"isDraft":false,"mergedAt":null,"state":"OPEN","title":"chore(deps): upgrade OpenShell runtime and SDK to 0.1.5"}

curl -fsSL https://raw.githubusercontent.com/NVIDIA/NemoClaw/main/nemoclaw-blueprint/blueprint.yaml \
  | grep -E '^(min|max)_openshell_version'
# min_openshell_version: "0.0.116"
# max_openshell_version: "0.0.116"

git ls-remote --tags https://github.com/NVIDIA/NemoClaw.git \
  | grep -E 'refs/tags/v0\.0\.[0-9]+\^\{\}$' | sed -E 's#\^\{\}##' | sort -k2 -V | tail -3
# f00fb1da…  refs/tags/v0.0.137
# 7312e7f4…  refs/tags/v0.0.138
# a08ae7aa…  refs/tags/v0.0.139

git ls-remote https://github.com/NVIDIA/NemoClaw.git 'refs/tags/lkg^{}'
# f00fb1da…  refs/tags/lkg^{}      ← 與 v0.0.137 相同
```

| 觀察到的變化 | 代表什麼 | 平台管理者的動作 |
|---|---|---|
| `mergedAt` 不再是 `null` | 0.1.5 已進入 `main` | 開始準備 12.4 演練環境；暫停核准任何新版本 |
| Blueprint 的 `max_openshell_version` 變成 `0.1.5` | 下一個 tag 會帶 0.1.5 | 讀該版 release notes，逐項對照上方影響表 |
| 出現新 tag，且 `lkg` 指向它 | 官方認為它是 last known good | 仍不能直接升級：在測試主機完成 12.4、12.9 才核准 |

> ⚠️ **警告**：PR 描述與 E2E 結果是「開發中的狀態」，合併前後都可能改變。本節只用來提早準備，正式升級時以當時的 release notes 與實測結果為準。

### 12.12 本章實務案例與注意事項

**案例**：同仁在沙盒內執行 `openclaw update` 想升級 OpenClaw，結果指令卡住，之後 `connect` 警告版本不一致。

說明：官方 Enterprise Readiness 頁明言不要在沙盒內就地更新 Agent，因為 Agent 綁在映像檔版本；官方 Troubleshooting 也有「`openclaw update` hangs or times out inside the sandbox」一節。正確做法是升級 NemoClaw 後執行 `nemoclaw <名稱> rebuild`。

**注意事項**：

- 升級是「整組」的：NemoClaw、OpenShell、映像檔、Agent 一起動；不要嘗試只換其中一個。
- 憑證永遠不在封存內；企業密碼庫才是憑證的真相來源。
- 為未來的 v1 遷移，可定期執行 `nemoclaw config export` 保留宣告式設定（不含憑證）。

## 第13章 企業導入與同仁使用規範

本章是一份可以直接改寫成內部規範的範本（🏢 全章皆為企業建議，不是 NemoClaw 原生功能）。原則只有一條：**不可只依賴 Agent 的自我約束**——每一條規範都要對應到技術防護、行政規範或人工審查其中至少一層。

### 13.1 適用人員與角色權責

| 角色 | 職責 | 不可兼任 |
|---|---|---|
| 使用者（開發者） | 在核准的主機與沙盒中使用 Agent；審查 AI 產出；維護交付報告 | 不得自行核准自己的白名單申請 |
| 主機操作者 | 安裝、升級、備份、`openshell term` 核准；官方定義的「單一受信任操作者」 | 通常與使用者同一人（一人一台主機） |
| 政策審查者 | 審查 preset 與白名單申請（6.16） | 不得是申請人本人 |
| 平台管理者 | 標準映像、標準 preset、版本基準、盤點 | — |
| 資安 | 資料分級、事件處理、例外核准 | — |
| 專案負責人 | 決定專案是否可用 AI、資料能否送外部模型 | — |
| Code Reviewer | 審查 AI 參與的 PR | 不得是該 PR 的唯一作者 |

> 📌 **註記**：NemoClaw 沒有操作者 RBAC（官方：Out of scope）。主機上能執行 `nemoclaw` 的帳號就擁有全部操作權。角色分離只能靠「一人一台主機」加上行政與審查流程達成。

### 13.2 開發環境申請與初始化

申請單必填欄位：

| 欄位 | 範例 |
|---|---|
| 申請人／主管 | — |
| 用途 | 新開發／逆向工程／升級 |
| 專案與資料分級 | order-service／內部（13.6） |
| 主機 | 專用 VM：Ubuntu 24.04、8 vCPU、32 GB、100 GB |
| NemoClaw 版本 | v0.0.139（依平台管理者公告的基準） |
| Agent | LangChain Deep Agents Code |
| 推理服務 | 企業私有端點／外部（需資料擁有者核准） |
| 政策層級與 preset | Restricted＋`corp-maven-readonly`＋`corp-git-order-read` |
| 到期日 | 最長 90 天，可續約 |

初始化完成的證據（附在申請單）：

- [ ] 3.9 預檢腳本輸出（結束碼 0）。
- [ ] `nemoclaw host probe --json` 輸出。
- [ ] 4.10 控制有效性驗證輸出。
- [ ] 6.12 V1～V6 輸出。
- [ ] `~/.bashrc` 已含 `export NEMOCLAW_DISABLE_TELEMETRY=1`。
- [ ] 12.2 盤點表。

### 13.3 專案目錄與檔案存取規範

| 規範 | 技術防護 | 行政規範 | 人工審查 |
|---|---|---|---|
| 工作副本只放在沙盒 `/sandbox/work/<專案>` | 沙盒檔案系統限制 | 本規範 | — |
| 原始碼以 `git clone` 進沙盒；逆向工程以 `--host-mount` 唯讀掛入 | 唯讀掛載、Git preset 的 repo 路徑 | 本規範 | 環境申請時審查 |
| ⛔ 不得以 `share mount` 掛家目錄或多個專案 | — | 本規範 | 抽查 `share status` |
| ⛔ 不得把 `.env`、金鑰、憑證檔放進沙盒 | 部分：rebuild 的憑證掃描 | 本規範 | 交付報告的 FORBIDDEN 檢查 |
| ⛔ 不得以 `docker exec` 操作沙盒 | — | 本規範 | — |
| 一個沙盒只處理一個專案 | Git preset 綁定 repo | 本規範 | — |

範例與驗證：

```bash
# 🖥️ Host：抽查沙盒內有沒有不該出現的檔案（🧪 未實機執行；預期沒有任何輸出）
nemoclaw dev-order exec -- sh -c \
  'find /sandbox -maxdepth 4 \( -name ".env" -o -name ".env.*" -o -name "*.pem" -o -name "*.key" -o -name "id_rsa*" -o -name "id_ed25519*" \) 2>/dev/null'
# 抽查共享掛載：應只有核准過的唯讀來源，或沒有任何掛載
nemoclaw dev-order share status
# 一個沙盒一個專案：工作目錄下應只有一個專案
nemoclaw dev-order exec -- ls /sandbox/work
```

| 情境 | 判定 |
|---|---|
| ✅ `/sandbox/work/order-service` 是唯一的專案，由 `git clone` 建立 | 符合 |
| ❌ `share mount` 掛了 `~/projects`，裡面有 5 個專案 | 違反「一個沙盒一個專案」，也讓 Agent 能寫主機目錄 |
| ❌ `find` 找到 `/sandbox/work/order-service/.env.local` | 違反憑證檔規範；同時檢查它是否已進入 Git 歷史（13.5） |

### 13.4 網路白名單申請與審查

```mermaid
flowchart LR
    A["申請人<br/>填寫申請單"] --> B["撰寫 preset YAML<br/>可請 AI 草擬"]
    B --> C["lint<br/>nemoclaw-policy-lint.py"]
    C -- ERROR --> B
    C -- 通過 --> D["政策審查者<br/>6.16 人工清單"]
    D -- 退回 --> B
    D -- 核准 --> E["合併到 presets/ repo<br/>PR＋CODEOWNERS"]
    E --> F["套用<br/>policy add --dry-run 後套用"]
    F --> G["驗證<br/>V1～V6 拒絕測試"]
    G --> H["結案<br/>附驗證輸出"]
```

申請單欄位：

| 欄位 | 說明 |
|---|---|
| 目的地 | 精確主機名與連接埠 |
| 方法與路徑 | 例如 `GET /repository/maven-public/**` |
| 發起程式 | `openshell term` 回報的 binary |
| 讀或寫 | 寫入另需專案負責人核准 |
| 資料敏感度 | 可能送出的資料類型 |
| 私有位址 | 是否需要 `--trusted-private-host` |
| 到期日 | 預設與環境同步 |

### 13.5 API Key 與憑證管理

| 規範 | 說明 |
|---|---|
| 來源 | 一律由企業密碼庫取得；⛔ 不得使用個人帳號的 Key |
| 範圍 | 專案專屬、最小權限、有額度上限 |
| 輸入方式 | `read -r -s` 讀入環境變數，onboarding 後 `unset`（6.6）；⛔ 不得貼在 Agent 對話、Prompt、文件中 |
| 保存 | 只存在 OpenShell Gateway；⛔ 不得寫入 `openclaw.json`、`.env`、Git |
| 輪替 | 每 90 天，或人員異動、主機轉移、疑似外洩時 |
| 撤銷 | 主機停用前在上游撤銷（12.8） |
| 正式環境憑證 | ⛔ 一律禁止進入任何沙盒或主機 |

範例與驗證：

❌ 壞例：在 Agent 對話中貼上「這是我的 key `sk-proj-…`，幫我測一下 API」。Key 會成為推理請求的一部分送到推理服務，也會留在 Agent 的對話紀錄裡。這把 Key 要當成已外洩，立刻在上游撤銷。

▶️ 驗證 1：主機上的設定檔與 shell 歷史沒有明文 Key（🖥️ Host；只印檔名、不印內容；🧪 樣式依你使用的供應商調整）：

```bash
grep -rlE 'nvapi-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9_-]{20,}' ~/.nemoclaw ~/.bash_history ~/.zsh_history 2>/dev/null \
  && echo "❌ 發現疑似明文 Key（只列檔名）" || echo "✅ 未發現"
```

▶️ 驗證 2：沙盒內拿到的是 placeholder，不是真實值（🧪）。做法是不印出值，只比對雜湊的前 8 碼：

```bash
# 📦 透過 exec 在沙盒內執行：列出名稱含 KEY／TOKEN 的變數，只印長度與雜湊前 8 碼
nemoclaw dev-order exec -- sh -c 'for v in $(env | cut -d= -f1 | grep -iE "key|token"); do
  printf "%s len=%s sha=%s\n" "$v" "$(printenv "$v" | wc -c)" "$(printenv "$v" | sha256sum | cut -c1-8)"; done'
# 🖥️ Host：用同樣算法算真實 Key 的雜湊（Key 由 read -r -s 讀入，算完立刻 unset）
read -r -s REAL_KEY; printf '%s\n' "$REAL_KEY" | sha256sum | cut -c1-8; unset REAL_KEY
```

判讀方式：兩邊雜湊**不同**才是正確的，代表沙盒內只有 placeholder。雜湊相同，代表真實 Key 進了沙盒，立即依 6.6 輪替並通報資安。

▶️ 驗證 3：CI 擋下進入 Git 的 Key，以 [gitleaks](https://github.com/gitleaks/gitleaks) 為例：`gitleaks detect --source . --redact`，結束碼非 0 就擋下 PR。

### 13.6 原始碼、個資、客戶資料與機密資料處理

| 資料分級 | 例子 | 可放進沙盒 | 可送外部推理服務 | 可送企業私有模型 |
|---|---|---|---|---|
| 公開 | 開源程式碼、公開文件 | ✅ | ✅ | ✅ |
| 內部 | 一般內部系統原始碼、設計文件 | ✅ | 需專案負責人核准 | ✅ |
| 機密 | 核心系統原始碼、資安設定、架構細節 | 需資安核准 | ⛔ | 需資安核准 |
| 極機密／受法規保護 | 客戶個資、帳務資料、正式環境憑證 | ⛔ | ⛔ | ⛔ |

> ⚠️ **警告**：明確禁止將生產環境憑證、客戶個資、未授權的原始資料或機密文件提供給外部模型服務。Prompt 的內容、Agent 讀進來的檔案、工具回傳的結果，**全部**都會成為送給推理服務的資料。

分級練習（答案在表格右欄，先遮住自己判斷）：

| 情境 | 判定 | 理由 |
|---|---|---|
| 把開源的 Spring PetClinic 放進沙盒，用 NVIDIA Endpoints 分析 | ✅ 可以 | 公開等級 |
| 把核心帳務系統的原始碼放進沙盒，用外部託管模型做逆向 | ⛔ 不可以 | 機密等級禁止送外部推理；改用企業私有模型並經資安核准 |
| 從正式環境匯出 100 筆客戶資料當測試資料 | ⛔ 不可以 | 受法規保護的資料不得進沙盒；改用合成資料 |
| 內部系統原始碼，但其中的測試資料檔有真實身分證號 | ⛔ 先去敏 | 檔案分級以「最高等級的內容」為準（8.9） |

▶️ 放進沙盒前的快篩（🖥️ Host；只計數、不印內容；📖 標準 `grep`）。以台灣身分證字號與 Email 樣式為例：

```bash
grep -rEoh '\b[A-Z][12][0-9]{8}\b' ./src-copy | wc -l      # 疑似身分證字號筆數
grep -rEoh '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' ./src-copy | sort -u | wc -l   # 不重複 Email 數
```

數字大於 0 不一定違規（測試碼裡可能是假資料），但每一筆都要有人確認來源。快篩只能找出「有樣式的資料」，客戶名稱、地址、帳號這類沒有固定樣式的資料，仍要靠 8.9 的人工去敏流程。

### 13.7 AI 產出程式碼的審查責任

| 原則 | 說明 |
|---|---|
| 作者責任 | 提交 PR 的人對 AI 產出負完全責任，等同自己寫的程式 |
| 完整閱讀 | Reviewer 必須看完整 diff，不能只看交付報告或 AI 的自我 review |
| 小 PR | 單一 PR 建議不超過 400 行有效變更；超過要拆 |
| 可追溯 | Commit trailer 標示 AI 參與（10.3） |
| 不降標準 | AI 產出的程式碼適用同一套品質與安全門檻 |

PR 描述範例：

| ✅ 好例 | ❌ 壞例 |
|---|---|
| 「新增 UC-01 下單 API。AI 參與：dcode 產生 Service 與測試初稿，我改寫了庫存檢查的並行處理。驗證：`mvn verify` 綠燈、`check-change-report.py` 0 項、手動測了庫存不足的情境。風險：`OrderRepository` 新增一個查詢，請 DBA 看索引。」 | 「依 AI 產出完成需求，測試皆通過。」 |
| 說清楚 AI 做了什麼、人改了什麼、用什麼證據驗證、哪裡需要別人注意 | 沒有範圍、沒有證據、沒有風險；Reviewer 無從判斷 |

Reviewer 的機械檢查（🔧 CI 或本機；📖 標準 Git 指令）：

```bash
git diff --shortstat origin/main...HEAD                         # 有效變更是否 ≤ 400 行
git log --format=%B origin/main..HEAD | grep -c '^AI-Assisted:'  # AI 參與的 commit 是否都有 trailer（10.3）
python3 check-change-report.py .ai-reports/$(git branch --show-current).md origin/main   # 報告是否誠實（7.10）
python3 check-test-weakening.py origin/main                      # 有沒有弱化測試（13.8）
```

> ⚠️ **警告**：機械檢查全部通過，只代表「沒有明顯的作弊跡象」，不代表程式正確。Reviewer 仍然要讀完整個 diff。

### 13.8 測試與品質驗證要求

- 每個 AI 參與的 PR 必須通過第 10.4 節的 CI 關卡；不接受「本機已測」或「Agent 已測」。
- 新增或修改的商業規則必須有對應的單元測試；邊界值必測。
- 禁止停用、刪除既有測試或降低斷言；確需調整時另開 PR 並說明理由。
- 交付報告必須通過 `check-change-report.py`。

「不得停用、刪除測試或降低斷言」這條規範要能被自動檢查，否則只靠 Reviewer 的眼睛。`check-test-weakening.py`（🏢 本手冊自行撰寫；✅ 已實測；完整原始碼見 18.10.5）比對基準分支與工作目錄，找出五種弱化測試的跡象：

| 代號 | 抓什麼 |
|---|---|
| `DELETED` | 測試檔被刪除，或被改名到非測試路徑 |
| `FEWERTESTS` | 測試檔中的測試案例（`@Test`、`it(`、`test(`）變少 |
| `FEWERASSERT` | 斷言（`assert*`、`assertThat`、`expect(`、`verify(`）變少 |
| `DISABLED` | 新增 `@Disabled`、`@Ignore`、`.skip(`、`xit(`、`.only(` |
| `SKIPBUILD` | `pom.xml`、`build.gradle`、`package.json` 等新增 `skipTests`、`testFailureIgnore`、`passWithNoTests` |

好例：只新增一個測試案例（✅ 實際輸出）：

```text
$ python3 check-test-weakening.py base
檢查 1 個變更檔案，發現 0 項
exit=0
```

❌ 壞例：Agent 為了讓 CI 變綠，刪掉一個測試檔、拿掉一個測試案例與兩個斷言、加上 `@Disabled` 與 `it.skip`，還在 `pom.xml` 加了 `skipTests`（✅ 實際輸出）：

```text
$ python3 check-test-weakening.py base
SKIPBUILD   pom.xml: 略過測試設定 0 → 1
DELETED     src/test/java/demo/LegacyTest.java: 測試檔被刪除
FEWERTESTS  src/test/java/demo/OrderServiceTest.java: 測試案例 2 → 1
FEWERASSERT src/test/java/demo/OrderServiceTest.java: 斷言 3 → 1
DISABLED    src/test/java/demo/OrderServiceTest.java: 停用標記 0 → 1
FEWERTESTS  web/src/order.spec.ts: 測試案例 2 → 1
DISABLED    web/src/order.spec.ts: 停用標記 0 → 1
檢查 4 個變更檔案，發現 7 項
exit=1
```

放進 10.4 的 CI 關卡（🔧 CI；GitHub Actions 片段，需要 `fetch-depth: 0` 才拿得到基準分支）：

```yaml
      - name: 測試弱化檢查
        run: python3 tools/check-test-weakening.py "origin/${{ github.base_ref }}"
```

處理原則：工具回報的是「需要人看」的清單，不是自動定罪。重構時合併兩個測試案例，也會出現 `FEWERTESTS`；這種情況由 Reviewer 在 PR 留言說明理由後放行。但 `SKIPBUILD` 一律退回。

### 13.9 日誌、稽核與事件通報

| 事件 | 通報對象 | 時限（🏢 建議） | 保全證據 |
|---|---|---|---|
| 憑證疑似外洩 | 資安 | 立即 | `logs`、`debug` 包、時間點 |
| 未知目的地的連線嘗試異常增加 | 資安、平台管理者 | 當日 | `logs --since`、`openshell term` 截圖 |
| AI 產出含惡意或可疑程式碼 | 資安、專案負責人 | 當日 | PR、交付報告、對話紀錄 |
| 沙盒內出現主機檔案或非預期掛載 | 資安 | 立即 | 4.10 輸出 |
| 推理費用異常 | 專案負責人 | 當日 | 供應商報表 |

處理流程見 6.10。NemoClaw 自身的安全漏洞依 [SECURITY.md](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md) 的私密管道回報，⛔ 不開公開 Issue。

證據保全範例（🖥️ Host；🧪 未實機執行）。重點是**先保全、再處理**，並且記下雜湊值，證明證據事後沒被改過：

```bash
case_id=INC-$(date +%Y%m%d-%H%M)
mkdir -p ~/evidence/$case_id && cd ~/evidence/$case_id
date -Iseconds > collected-at.txt
nemoclaw dev-order logs --since 24h > sandbox.log 2>&1
nemoclaw dev-order status --json > status.json 2>&1
nemoclaw dev-order policy list > policy.txt 2>&1
nemoclaw debug --sandbox dev-order --output ./debug.tgz
sha256sum * > SHA256SUMS            # 移交資安時一併附上
```

通報內容範例：

| 欄位 | ✅ 好例 | ❌ 壞例 |
|---|---|---|
| 事件 | dev-order 沙盒 10:05～10:20 對 `paste.example.net` 有 37 次被拒連線 | 沙盒怪怪的 |
| 影響 | 未成功連出；工作副本含內部原始碼（內部等級） | 不知道 |
| 已採取動作 | 10:25 `stop` 沙盒；證據在 `~/evidence/INC-20261027-1025`，附 `SHA256SUMS` | 重開了，現在好了 |

❌ 最常見的錯誤是先 `destroy` 或 `rebuild`「讓它恢復正常」。這兩個動作都會毀掉證據。

### 13.10 版本管理、更新與停用程序

| 項目 | 規範 |
|---|---|
| 版本基準 | 平台管理者公告「核准版本」；主機只能安裝核准版本 |
| 更新 | 依 12.4 演練、12.5 程序；個人不得自行升級 |
| 例外 | 安全修補可加速，但仍需 12.9 驗收 |
| 停用 | 依 12.8；憑證撤銷是必要步驟 |
| 逾期 | 環境到期未續約，平台管理者通知後停用 |

核准版本公告範例（🏢；放在平台管理者的公告頁或 presets repo 的 `APPROVED.md`）：

```text
NemoClaw 核准版本：v0.0.139（a08ae7a）／OpenShell 0.0.116
核准日期：2026-10-27　下次檢視：2026-11-10 或新安全公告發布時
安裝指令：NEMOCLAW_INSTALL_REF= NEMOCLAW_INSTALL_TAG=v0.0.139 bash nemoclaw.sh（先依 4.3 審查）
已知限制：管線輸入可能卡住（5.6）；OpenShell 0.1.5 遷移尚未發布（12.11）
安全下限：check-security-floor.sh 須通過（6.17.1）
```

▶️ 驗證主機符合公告：11.2 的 `nemoclaw-daily.sh`（版本）加上 6.17.1 的 `check-security-floor.sh`（安全下限），兩者結束碼都要是 0。

### 13.11 允許／禁止／需經核准的行為

| 類別 | 行為 |
|---|---|
| ✅ **允許** | 在核准主機上以核准版本建立 Restricted 層沙盒 |
| ✅ 允許 | 使用已核准的標準 preset |
| ✅ 允許 | 以合成資料或公開資料進行開發與測試 |
| ✅ 允許 | 讓 Agent 草擬文件、程式、測試，並提交到 `ai/*` 分支 |
| ✅ 允許 | 以 `--host-mount` 唯讀掛入去敏後的原始碼快照進行逆向工程 |
| ✅ 允許 | 使用 `status`、`logs`、`doctor`、`debug` 等唯讀診斷 |
| ⛔ **禁止** | 將生產環境憑證、客戶個資、未授權原始資料或機密文件提供給外部模型服務 |
| ⛔ 禁止 | 使用 Personal 或 Open 政策層級 |
| ⛔ 禁止 | 在 `openshell term` 使用「全部核准」（`A`）或核准未申請的目的地 |
| ⛔ 禁止 | 單獨升級 OpenShell、在沙盒內就地更新 Agent |
| ⛔ 禁止 | 以 `docker exec` 操作沙盒；繞過 NemoClaw 受管入口啟動 Agent |
| ⛔ 禁止 | 把 API Key 貼進對話、Prompt、文件或寫入沙盒設定檔 |
| ⛔ 禁止 | 多人共用同一台 NemoClaw 主機 |
| ⛔ 禁止 | 沙盒有任何通往正式環境的網路路徑 |
| ⛔ 禁止 | 讓 Agent 修改 CI 設定、政策 preset、AGENTS.md 後未經 CODEOWNERS 審查即合併 |
| ⛔ 禁止 | 啟用訊息通道（Slack、Discord、Telegram、WhatsApp 等）與 Dashboard 對外綁定 |
| ⚠️ **需經核准** | 新增網路目的地（13.4） |
| ⚠️ 需經核准 | 任何寫入類 preset（例如 `corp-git-order-write`） |
| ⚠️ 需經核准 | 把「內部」等級資料送外部推理服務（13.6） |
| ⚠️ 需經核准 | 使用自訂映像檔（`--from`） |
| ⚠️ 需經核准 | 開啟 Deep Agents 的 `--dcode-auto-approval thread-opt-in` |
| ⚠️ 需經核准 | 使用 `share mount` 雙向掛載 |
| ⚠️ 需經核准 | 開啟 `NEMOCLAW_EXPERIMENTAL=1` 的實驗功能 |
| ⚠️ 需經核准 | 託管 MCP Server 的新增 |

### 13.12 技術防護、行政規範與人工審查的分層

| 風險 | 技術防護（NemoClaw／OpenShell／CI） | 行政規範（本章） | 人工審查 |
|---|---|---|---|
| 資料外洩到網際網路 | Deny-by-default、preset、SSRF 防護 | 白名單申請、資料分級 | preset 審查、`openshell term` 核准 |
| 憑證外洩 | Gateway 保管、placeholder、rebuild 憑證掃描 | 憑證管理規範 | 交付報告 FORBIDDEN 檢查 |
| 誤改主機檔案 | 沙盒檔案系統、唯讀掛載 | 目錄規範 | — |
| 惡意依賴 | Restricted 層、內部代理庫 | 依賴新增需核准 | SCA 結果審查 |
| 錯誤或惡意程式碼 | CI、ArchUnit、SAST | 審查責任 | Code Review |
| 報告不實 | `check-change-report.py` | 交付報告格式 | Reviewer 看完整 diff |
| 版本漂移 | 版本範圍檢查（max_openshell_version） | 核准版本 | 盤點表 |
| 濫用推理預算 | —（NemoClaw 不控管） | 額度規範 | 每週費用檢視 |

用這張表做稽核的範例：抽一列風險，**三層各提出一個證據**。只要缺一層，就要說明為什麼可以接受。

| 風險：憑證外洩 | 證據 |
|---|---|
| 技術防護 | 13.5 驗證 2 的輸出：沙盒內的雜湊與真實 Key 不同 |
| 行政規範 | 同仁簽署的使用規範，以及 13.2 申請檢查表中的憑證管理項目 |
| 人工審查 | 最近 10 個 AI 參與的 PR 中，`check-change-report.py` 沒有出現 `FORBIDDEN` 的紀錄 |

### 13.13 本章實務案例與注意事項

**案例**：專案負責人想讓外包廠商的工程師也用部門的 NemoClaw 主機。

評估：官方不支援多使用者共用主機，也沒有 RBAC；外包人員能執行 `nemoclaw` 就能改政策、看到所有沙盒的日誌與對話。

建議：由外包廠商依本章規範自行申請獨立主機（或企業提供獨立 VM），資料分級與憑證完全分開；不得共用主機或 Gateway。

**注意事項**：

- 規範要隨 NemoClaw 版本調整；每次核准新版本時，平台管理者檢查 13.11 是否需要更新。
- 「需經核准」的項目要有到期日；核准不是永久的。
- 規範的有效性要量測（第 15 章），而不是只看簽署率。

## 第14章 企業共用平台建議架構

本章提出適用大型企業與金融業的 NemoClaw **試行**架構（🏢 全章為本手冊的建議設計，不是 NVIDIA 官方架構）。設計前提來自官方的產品邊界：單一主機、單一受信任操作者、無 RBAC、無多租戶、無集中管理、無 SLA。因此「共用平台」的意思是**共用標準與周邊服務**，不是共用 NemoClaw 主機。

### 14.1 設計原則

| 原則 | 對應的官方限制 | 設計 |
|---|---|---|
| 一人一主機 | 不支援多使用者主機 | 每位使用者一台 VM（VDI 或開發用 VM 池） |
| 一專案一沙盒 | 沙盒以名稱隔離、同主機共用 Gateway | 不同專案用不同沙盒；不同敏感等級用不同主機 |
| 共用的是標準 | 無集中管理 | 標準 VM 映像、標準 preset repo、版本基準、盤點腳本 |
| 只通非正式環境 | alpha、無 SLA | 網路區段與正式環境完全隔離 |
| 周邊服務做治理 | 無 SIEM、無成本控管 | 企業 AI Gateway、日誌平台、密碼庫 |

每條原則的驗證方式（🖥️ Host；📖 標準 Linux 指令）：

| 原則 | ▶️ 驗證指令 | 通過標準 |
|---|---|---|
| 一人一主機 | `getent group docker` | 只列出這台 VM 的申請人一個帳號 |
| 一專案一沙盒 | `nemoclaw list` 對照專案登記表 | 每個沙盒名稱都對得到一個已登記的專案 |
| 共用的是標準 | `nemoclaw --version` 與核准公告比對（13.10） | 版本一致 |
| 只通非正式環境 | 14.8 的連線測試 | 到正式網段的連線全部失敗 |

### 14.2 企業部署架構圖

```mermaid
flowchart TB
    subgraph USERZ["使用者區"]
        U1["開發者筆電<br/>瀏覽器、SSH"]
    end
    subgraph DEVZ["AI 開發隔離區（非正式網段）"]
        direction TB
        subgraph VM1["個人 VM：dev-host-07（開發者 A）"]
            N1["NemoClaw v0.0.139<br/>OpenShell 0.0.116"]
            S1["沙盒 dev-order"]
            S2["沙盒 re-legacy"]
        end
        subgraph VM2["個人 VM：dev-host-08（開發者 B）"]
            N2["NemoClaw"]
            S3["沙盒 up-billing"]
        end
        AGENTLOG["日誌轉送代理<br/>logs 定時匯出"]
    end
    subgraph SVCZ["共用服務區"]
        GIT["內部 Git<br/>ai/* 分支權限"]
        NEXUS["Nexus／Artifactory<br/>代理庫＋弱點掃描"]
        AIGW["企業 AI Gateway<br/>私有模型、額度、稽核"]
        CI["CI/CD Runner<br/>建置、測試、掃描"]
        VAULT["密碼庫<br/>API Key、Token"]
        SIEM["日誌平台／SIEM"]
        PRESET["presets repo<br/>標準政策與版本基準"]
    end
    subgraph EXTZ["外部（經企業 Proxy）"]
        EXTLLM["外部推理服務<br/>需核准"]
        GHCR["ghcr.io、github.com<br/>安裝與映像檔"]
    end
    PROD["正式環境<br/>⛔ 無任何路徑"]
    U1 -->|"SSH"| VM1
    U1 -->|"SSH"| VM2
    S1 -->|"corp-git preset"| GIT
    S1 -->|"corp-maven preset"| NEXUS
    S1 -->|"推理"| AIGW
    S3 -->|"推理"| AIGW
    AIGW -.->|"核准後"| EXTLLM
    N1 -.->|"安裝與升級"| GHCR
    GIT --> CI
    CI --> NEXUS
    AGENTLOG --> SIEM
    VAULT -.->|"操作者取用"| N1
    PRESET -.->|"標準 preset"| N1
    DEVZ -.-x PROD
```

### 14.3 個人開發沙盒與共用測試環境的隔離

| 項目 | 個人開發主機 | 共用測試環境 |
|---|---|---|
| 使用者 | 一人 | 多人（但 NemoClaw 不在此） |
| NemoClaw | 有 | **沒有** |
| 用途 | Agent 開發、逆向、升級 | 部署 CI 產物、UAT、整合測試 |
| 資料 | 合成資料 | 遮罩後測試資料 |
| 連線 | 只到共用服務區 | 由 CI 部署，不由沙盒直連 |

> ✅ **建議**：沙盒**不直連**共用測試環境。Agent 的產出經 Git → CI → 部署到測試環境；測試結果回到 PR。這樣 Agent 永遠只碰得到「程式碼」，碰不到「環境」。

▶️ 驗證「沙盒不直連測試環境」（🖥️ Host 透過 `exec` 在沙盒內執行；🧪 主機名稱請換成貴單位實際的測試環境）：

```bash
nemoclaw dev-order exec -- sh -c \
  'curl -s -o /dev/null -w "%{http_code}\n" --max-time 5 https://uat-api.corp.example/health; echo "exit=$?"'
```

通過標準：連線被沙盒代理拒絕（4.10 的拒絕樣態），或 `curl` 以非 0 結束碼失敗。如果得到 `200`，代表有某個 preset 放行了測試環境，要用 `policy list` 找出是哪一個。

### 14.4 不同專案的檔案、網路與憑證權限分離

| 隔離面 | 做法 |
|---|---|
| 檔案 | 一專案一沙盒；工作副本只在該沙盒 |
| 網路 | preset 綁定 repo 路徑（`/scm/<project>/<repo>.git/…`）；不同專案不共用寫入 preset |
| 憑證 | Git Token 一專案一個、只授權該 repo；推理 Key 依專案分開以利成本歸屬 |
| 敏感等級 | 機密專案用獨立主機與私有模型；不與內部等級專案共用主機 |

> ⚠️ **警告**：同一主機上的沙盒共用同一個 OpenShell Gateway 與憑證庫。官方說明 `nemoclaw credentials add` 註冊的 Provider 是 **Gateway 範圍**，會附掛到之後建立或重建的**每一個**沙盒；`credentials reset` 也會從所有使用中的沙盒卸除。不同敏感等級的專案若共用主機，憑證邊界就無法分開。

▶️ 驗證 Git Token 只能動自己的 repo 與 `ai/*` 分支（🔧 在沙盒外，用該 Token 執行；🧪 依 Git Server 的權限模型而定）：

```bash
# 預期：讀自己的 repo 成功
git ls-remote https://git.corp.example/scm/order/order-service.git >/dev/null && echo "OK 可讀自己的 repo"
# 預期：讀別的專案失敗（403／404）
git ls-remote https://git.corp.example/scm/pay/payment-core.git >/dev/null 2>&1 || echo "OK 讀不到別的專案"
# 預期：推送到 main 被拒
git push --dry-run origin HEAD:main 2>&1 | grep -qiE 'denied|forbidden|protected' && echo "OK main 受保護"
```

❌ 壞例：為了方便，整個部門共用一把有「所有 repo 寫入權」的 Token。只要任何一個沙盒被 Prompt Injection，Agent 就能推送到所有專案。

### 14.5 私有模型服務與外部託管推理服務的選擇

| 面向 | 企業私有模型（vLLM／NIM／企業 AI Gateway） | 外部託管（NVIDIA Endpoints、OpenAI、Anthropic 等） |
|---|---|---|
| 資料外送 | 不出企業 | 送到供應商 |
| NemoClaw 支援 | 「Other OpenAI-compatible endpoint」（Tested with limitations）或本地 vLLM／NIM | Tested |
| 能力 | 取決於自建模型 | 通常較強 |
| 成本 | GPU 資本支出與維運 | 依 token 計費 |
| 工具呼叫相容性 | 需實測（官方 Troubleshooting 有「Tool calls appear as assistant text」） | 官方驗證 |
| 稽核 | 企業 AI Gateway 可記錄每次請求 | 依供應商 |
| 適用資料等級 | 內部、機密（經核准） | 公開、內部（經核准） |

> ✅ **建議**：所有推理流量經企業 AI Gateway（統一入口、額度、稽核、模型路由），NemoClaw 只設定一個「OpenAI 相容端點」指向它。這也補上 NemoClaw 沒有成本控管與集中稽核的缺口。

### 14.6 企業 Proxy、TLS、DNS 與防火牆整合

| 項目 | 設定點 | 說明 |
|---|---|---|
| 主機出口 | 主機的 `HTTP(S)_PROXY` | NemoClaw 會把 `localhost`、`inference.local` 等加入 `NO_PROXY` |
| 沙盒出口 Proxy | `NEMOCLAW_PROXY_HOST`／`PORT`（建置期） | 預設 `10.200.0.1:3128`（OpenShell 注入） |
| TLS 攔截 | `NEMOCLAW_CORPORATE_CA_BUNDLE` | 只接受 CA 憑證，拒絕整包 OS 信任庫 |
| DNS | Docker daemon 的 `dns` 設定 | 企業封鎖 UDP 53 時必要（11.3） |
| 防火牆 | VM 網段 ACL | 只允許到共用服務區與核准的外部端點；明確拒絕正式網段 |
| UFW 自動修復 | `NEMOCLAW_AUTO_FIX_FIREWALL=1` | ⛔ 企業主機由網管管理防火牆，不開啟 |

### 14.7 稽核、日誌保存與異常通報

NemoClaw 官方把集中稽核與 SIEM 整合列為 *Manual or admin-only*。🏢 建議的補強：

| 資料 | 收集方式 | 頻率 | 偵測規則範例 |
|---|---|---|---|
| 沙盒日誌 | 每台 VM 以 cron 執行 `nemoclaw <名稱> logs --since 1h`，送日誌平台 | 每小時 | 單一沙盒每小時拒絕 > 50 次 |
| 版本盤點 | 12.2 腳本 | 每日 | 版本與核准基準不符 |
| 政策漂移 | `policy list` 與 presets repo 比對 | 每日 | 出現未在 repo 中的 preset |
| 推理流量 | 企業 AI Gateway | 即時 | 單一 Key 的 token 用量超過基準 3 倍 |
| Git 推送 | Git Server 稽核 | 即時 | AI Token 推送到 `ai/*` 以外的分支（應被權限擋下） |

排程範例（🏢；🧪 未實機執行）。cron 的 PATH 很短，一定要寫絕對路徑：

```bash
command -v nemoclaw    # 先查出絕對路徑，例如 /home/dev/.local/bin/nemoclaw
# crontab -e
0 * * * * NEMOCLAW_DISABLE_TELEMETRY=1 /home/dev/.local/bin/nemoclaw dev-order logs --since 1h >> /var/log/nemoclaw/dev-order.log 2>&1
```

偵測規則怎麼驗證：規則寫好後，**一定要故意觸發一次**，確認告警真的會發出來。沒有被觸發測試過的規則，等於沒有規則。

1. 在沙盒內對一個未放行的網址發出請求（例如 4.10 的拒絕測試），重複 60 次，超過「每小時 50 次」的門檻。
2. 等下一次排程把日誌送到日誌平台。
3. 確認日誌平台出現告警，並把告警截圖附在 14.12 的風險接受文件中。
4. 如果沒有告警：先看日誌平台裡被拒那一行的實際格式，再修正規則的比對條件（日誌格式不是穩定介面，標 🧪 就是這個原因）。

### 14.8 開發、測試與正式環境的權限分離

| 權限 | 開發（NemoClaw 主機） | 測試 | 正式 |
|---|---|---|---|
| AI Agent 可存取 | 工作副本、內部 Git（限 repo）、代理庫、AI Gateway | ⛔ | ⛔ |
| 部署權限 | ⛔ | CI 服務帳號 | 變更管理流程 |
| 資料 | 合成 | 遮罩 | 真實 |
| 憑證 | 開發用、低權限 | CI 密碼庫 | 正式密碼庫 |

▶️ 驗證網路層的分離（🖥️ Host，在 NemoClaw VM 上**沙盒外**執行；這一層靠的是企業防火牆，不是 NemoClaw）：

```bash
for t in prod-db.corp.example:1521 prod-api.corp.example:443; do
  timeout 5 bash -c "</dev/tcp/${t%:*}/${t#*:}" 2>/dev/null && echo "❌ 連得到 $t" || echo "✅ 連不到 $t"
done
```

這個測試要在主機上做，原因是：沙盒內連不到正式環境，可能只是政策擋住了；主機連不到，才證明網段真的隔離。兩層都要通過。

### 14.9 共用設定範本與政策版本管理

`presets` repo 結構建議：

```text
nemoclaw-platform/
├── VERSION-BASELINE.md          核准的 NemoClaw／OpenShell 版本
├── presets/
│   ├── corp-maven-readonly.yaml
│   ├── corp-npm-readonly.yaml
│   ├── corp-ai-gateway.yaml
│   └── projects/
│       └── order-service/
│           ├── corp-git-order-read.yaml
│           └── corp-git-order-write.yaml
├── tools/
│   ├── nemoclaw-policy-lint.py
│   ├── check-change-report.py
│   ├── check-layering.py
│   ├── check-evidence.py
│   ├── preflight-nemoclaw.sh
│   └── nemoclaw-inventory.sh
├── templates/
│   ├── AGENTS.md
│   └── pull_request_template.md
└── .github/
    ├── CODEOWNERS               presets/ 由政策審查者審查
    └── workflows/lint.yml       每個 PR 跑 nemoclaw-policy-lint.py
```

版本規則：preset 每次變更打 tag（例如 `presets-2026.10.27`）；主機盤點表記錄套用的 tag；NemoClaw 版本基準更新時，所有 preset 要在測試主機重跑 6.12 驗證。

### 14.10 資源成本、模型使用量與維運責任

| 成本項目 | 量測 | 責任 |
|---|---|---|
| VM（CPU、記憶體、磁碟） | 虛擬化平台報表 | 平台管理者 |
| GPU（若自建模型） | GPU 使用率 | AI 平台團隊 |
| 外部推理費用 | AI Gateway 或供應商報表，依專案 Key 歸屬 | 專案負責人 |
| 維運人力 | 升級、事件、支援工時 | 平台管理者 |
| 教育訓練 | 時數 | 各部門 |

推理成本估算範例（🏢；以下單價與用量都是**虛構**的教學數字，實際請以供應商報價與 AI Gateway 的報表為準）：

| 項目 | 數值 |
|---|---|
| 每個開發任務的平均輸入 token | 1,200,000（Agent 反覆讀檔，輸入遠大於輸出） |
| 每個開發任務的平均輸出 token | 60,000 |
| 假設單價 | 輸入每百萬 token 3 元、輸出每百萬 token 15 元 |
| 每任務成本 | 1.2 × 3 ＋ 0.06 × 15 ＝ 4.5 元 |
| 每人每月 60 個任務 × 20 人 | 4.5 × 60 × 20 ＝ 5,400 元／月 |

審查這類估算時要問三件事：(1) token 數是實測值還是猜的？（以第一階段的 AI Gateway 數據為準）(2) 有沒有算到重試與失敗的任務？(3) 單價是不是最新報價？

### 14.11 分階段導入計畫

```mermaid
flowchart LR
    P1["第一階段<br/>個人 PoC<br/>2～3 位資深同仁<br/>合成資料"] --> G1{"安全驗收<br/>4.10、6.12"}
    G1 -- 通過 --> P2["第二階段<br/>隔離測試環境試辦<br/>標準 VM、preset repo、日誌轉送"]
    G1 -- 不通過 --> P1
    P2 --> G2{"維運演練<br/>升級、回復、事件"}
    G2 -- 通過 --> P3["第三階段<br/>選定專案試行<br/>1～2 個內部等級專案"]
    P3 --> P4["第四階段<br/>安全與效益評估<br/>第 15 章指標"]
    P4 --> G3{"導入決策<br/>風險接受"}
    G3 -- 核准 --> P5["第五階段<br/>依核准結果擴大<br/>仍限非正式環境"]
    G3 -- 不核准 --> X["暫停或調整範圍"]
```

| 階段 | 目標 | 範圍 | 退出條件 |
|---|---|---|---|
| 1. 個人 PoC | 確認安裝、控制有效性、基本開發流程 | 2～3 人、合成資料、各自 VM | 4.10 與 6.12 全通過；完成第 16 章三個演練 |
| 2. 隔離試辦 | 建立標準與周邊服務 | 標準 VM 映像、presets repo、AI Gateway、日誌轉送 | 完成一次升級演練與一次事件演練 |
| 3. 專案試行 | 在真實（非正式、內部等級）專案驗證 | 1～2 個專案、5～10 人 | 連續 4 週收集第 15 章指標 |
| 4. 評估 | 安全與效益 | 資安、架構、專案代表 | 書面評估報告 |
| 5. 擴大 | 依核准範圍 | 依決策 | 每季重新評估；NemoClaw 脫離 alpha 前不進正式環境工作負載 |

### 14.12 Alpha 階段的風險接受程序

| 步驟 | 內容 |
|---|---|
| 1. 風險說明 | 列出官方限制（1.5）、本企業的補強控制（13.12）、剩餘風險 |
| 2. 範圍限定 | 非正式環境、資料等級上限、人數上限、期限 |
| 3. 簽核 | 專案負責人、資安主管、資訊主管 |
| 4. 監控 | 14.7 的偵測規則 |
| 5. 重新評估 | 每次 NemoClaw 大版本或每季 |
| 6. 中止條件 | 重大事件、官方停止維護、出現未修補的高風險漏洞 |

風險接受單範例：

| 欄位 | ✅ 好例 | ❌ 壞例 |
|---|---|---|
| 範圍 | 訂單組 3 人、3 台 VM、資料等級上限「內部」、只開 Restricted 層 | 研發處 |
| 期限 | 2026-11-01～2027-01-31，到期自動失效 | 無 |
| 補強控制 | 13.12 全表；14.7 偵測規則已觸發測試（附截圖） | 依公司規範 |
| 剩餘風險 | 無 RBAC：VM 擁有者可自行改政策；以每日巡檢的政策比對（11.2）偵測 | 無 |
| 中止條件 | 任一憑證外洩事件；出現影響核准版本的 Critical 公告且 7 天內無法修補（6.17.2） | 發生重大事件時 |
| 簽核 | 專案負責人、資安主管、資訊主管（三人） | 專案負責人 |

### 14.13 本章實務案例與注意事項

**案例**：金融業資訊處想用一台高規 GPU 伺服器讓 20 位同仁共用 NemoClaw。

評估：官方不支援多使用者主機、沒有 RBAC 與多租戶隔離、Provider 憑證是 Gateway 範圍。20 人共用等於 20 人共享同一組憑證、互相看得到沙盒與日誌。

建議架構：GPU 伺服器改當**企業私有模型服務**（vLLM 或 NIM，經企業 AI Gateway 對外），20 位同仁各自一台輕量 VM 跑 NemoClaw，推理統一指向 AI Gateway。這樣 GPU 被共用、NemoClaw 主機仍是一人一台。

**注意事項**：

- 架構圖中的「正式環境無任何路徑」要以網段 ACL 實際驗證，而不是只畫在圖上。
- 第五階段的「擴大」仍限非正式環境；是否允許處理更高等級資料，要等 NemoClaw 有正式版與企業驗證後重新評估。
- 本章架構是試行建議，各企業需依自身網路、資安與法規調整。

## 第15章 效益衡量與導入決策

本章提供可量化的評估指標（🏢 全章為本手冊設計的方法）。原則：**不憑空宣稱生產力提升百分比**。所有數字都要有基準值、有取得方法、有適用限制；沒有基準值的指標，不能拿來比較。

### 15.1 衡量原則

| 原則 | 說明 |
|---|---|
| 先有基準 | 導入前用相同類型的任務量測「不用 AI」或「用既有工具」的數字 |
| 同類比較 | 新開發、逆向、升級分開統計；不同規模的任務不混在一起平均 |
| 品質與速度一起看 | 只看速度會鼓勵跳過審查；每個速度指標都配一個品質指標 |
| 安全指標獨立 | 安全事件與政策誤阻擋不能被效益抵銷 |
| 樣本足夠 | 第三階段至少 4 週、每類任務至少 10 件才下結論 |
| 記錄限制 | 模型版本、Agent 版本、任務難度都會影響結果，要一併記錄 |

### 15.2 指標定義

| 指標 | 定義 | 計算方式 | 基準值取得 | 適用限制 |
|---|---|---|---|---|
| 需求分析與文件產製時間 | 從原始需求到 SRS 經需求方簽核的工時 | Σ（人員實際投入工時），不含等待時間 | 導入前 3～5 份同類 SRS 的工時紀錄 | 需求複雜度差異大；以功能點或 UC 數正規化 |
| 逆向工程工時 | 完成一個模組的盤點、呼叫鏈、商業規則、文件並通過人工確認的工時 | Σ 人員工時 ÷ 模組數（或 ÷ 千行程式） | 過去人工逆向的工時紀錄；沒有時以首個模組人工完成作基準 | 程式碼品質、編碼、文件殘缺程度影響大 |
| Framework 升級工時 | 一次升級從盤點到驗收的工時 | Σ 人員工時（含 review 與修正） | 過去同類升級的工時 | 依賴數量、測試覆蓋率影響大 |
| 測試覆蓋率變化 | 導入後新增程式碼的行覆蓋率與分支覆蓋率 | CI 覆蓋率報告（JaCoCo、Vitest） | 導入前 3 個月同專案新增程式碼的覆蓋率 | 覆蓋率高不代表斷言有效；搭配突變測試更佳 |
| 缺陷發現率 | 每千行新增程式碼在 Code Review、CI、測試、UAT、上線後各階段發現的缺陷數 | 缺陷數 ÷ KLOC，依階段分列 | 導入前同專案的缺陷追蹤資料 | 越早發現越好；上線後缺陷是最重要的負向指標 |
| AI 產出審查退回率 | AI 參與的 PR 被退回（Request changes）的比例 | 退回次數 ÷ AI 參與 PR 數 | 同期人工 PR 的退回率 | 退回率低可能代表審查變鬆，要搭配抽查 |
| 交付報告不實率 | `check-change-report.py` 回報 UNREPORTED／PHANTOM／TESTFAIL 的比例 | 有問題的報告數 ÷ 報告總數 | 無（新指標），以第一階段數據為基準 | 反映 Agent 與 Prompt 品質 |
| 安全政策阻擋次數 | 沙盒每日被拒絕的連線數 | `logs` 中的拒絕紀錄計數 | 第一階段穩定後的每日中位數 | 突然增加可能是攻擊或誘導，也可能是新需求 |
| 政策誤阻擋 | 必要服務被擋、需要申請白名單的次數與等待時間 | 白名單申請單數；從阻擋到開通的時間 | 第二階段數據 | 誤阻擋多代表標準 preset 不足；不能因此放寬層級 |
| Agent 任務完成率 | 任務在不需人工大幅重寫下被接受的比例 | 被合併的任務數 ÷ 指派任務數 | 無；以第一階段為基準 | 任務切割大小影響很大 |
| 模型推理成本 | 每個任務、每個 PR 的推理費用 | AI Gateway 或供應商報表 ÷ 任務數 | 第一階段 | 模型價格變動要正規化 |
| 平均處理時間 | 從指派到交付報告的時間 | 時間戳差 | 第一階段 | 含等待人工核准的時間要分開 |
| 升級失敗率 | NemoClaw 升級需要回復或大量手動修復的比例 | 失敗次數 ÷ 升級次數 | 第二階段演練 | 樣本少時以個案檢討為主 |
| 復原時間 | 從發現故障到 4.10 驗收重新通過的時間 | 時間戳差 | 第二階段演練 | — |

### 15.3 資料收集方法

| 資料 | 來源 | 自動化程度 |
|---|---|---|
| 工時 | 工時系統，任務單加上「AI 參與」標籤 | 半自動 |
| PR 與審查 | Git Server API（PR、review 狀態、commit trailer） | 自動 |
| CI 結果、覆蓋率、掃描 | CI artifact | 自動 |
| 交付報告檢查結果 | CI 中 `check-change-report.py` 的輸出 | 自動 |
| 拒絕紀錄 | 14.7 的日誌轉送 | 自動 |
| 推理費用 | AI Gateway | 自動 |
| 缺陷 | 缺陷追蹤系統，加註發現階段與是否為 AI 參與的程式 | 半自動 |

### 15.4 導入決策門檻

第四階段的決策建議以「必要條件＋效益條件」兩段判斷：

| 類型 | 條件 | 不符時 |
|---|---|---|
| 必要（安全） | 試行期間無憑證外洩、無資料外送事件 | 不擴大 |
| 必要（安全） | 4.10、6.12 驗收在每次升級後都通過 | 不擴大 |
| 必要（品質） | AI 參與程式碼的上線後缺陷率不高於基準 | 不擴大 |
| 必要（治理） | 交付報告不實率呈下降趨勢且低於 10% | 改善 Prompt 與流程後再評估 |
| 效益 | 至少一類任務（新開發、逆向、升級）的工時中位數低於基準，且品質指標不變差 | 縮小範圍到有效的任務類型 |
| 成本 | 推理＋維運成本低於節省的工時成本 | 調整模型或範圍 |

決策計算範例（🏢；以下為**虛構**的教學數字）：

| 指標 | 基準 | 試行 8 週 | 是否達標 |
|---|---|---|---|
| 憑證外洩、資料外送事件 | — | 0 | ✅ 必要條件 |
| 升級後 4.10／6.12 驗收 | — | 2 次升級都通過 | ✅ 必要條件 |
| 上線後缺陷率（每 KLOC） | 0.8 | 0.7 | ✅ 必要條件 |
| 交付報告不實率 | — | 第 1～4 週 22%，第 5～8 週 8% | ✅ 下降且 < 10% |
| 新開發任務工時中位數 | 16 小時（n=12） | 11 小時（n=14） | ✅ 效益 |
| 逆向工程工時中位數 | 40 小時（n=3） | 38 小時（n=4） | ⚠️ 樣本太少，不下結論 |
| 每月推理＋維運成本 | — | 5,400＋（0.2 人月） | 與節省工時比較 |

結論寫法：「新開發任務達到擴大條件；逆向工程樣本不足，延長試行 4 週再評估；不擴大到機密等級專案。」❌ 錯誤寫法是「整體效率提升 31%」：這個數字混了不同任務類型，而且沒有附上樣本數。

### 15.5 本章實務案例與注意事項

**案例**：試行 4 週後，專案經理報告「逆向工程工時下降 60%」。

審查：

1. 基準是什麼？——是另一個規模小一半的模組的人工工時，基準不可比。
2. 品質呢？——`check-evidence.py` 通過，但業務人員抽查 `[事實]` 的錯誤率是 18%（8.11 那類錯誤），修正工時沒算進去。
3. 改善：以同一模組的另一半作人工基準；工時計入「人工確認與修正」；把抽查錯誤率列為品質指標。

**注意事項**：

- 指標是用來改善流程的，不是用來評比個人；否則會鼓勵隱瞞問題。
- 模型或 Agent 版本變更後，指標要重新建立基準。
- 對外報告效益時，附上樣本數、期間、基準來源與限制。

## 第16章 實作演練與驗收

本章設計四個演練：演練 0 驗證安全控制（其他演練的前提），案例 A、B、C 分別對應新開發、逆向工程、Framework 升級。全部使用小型、可重現、合成資料的專案，⛔ 不得使用真實客戶資料或正式系統原始碼。每個案例都包含：實作目標、前置條件、操作步驟、Prompt、預期輸出、驗收標準、常見錯誤、安全檢查、人工審查點。

### 16.1 演練 0：安全控制驗證（必做）

| 項目 | 內容 |
|---|---|
| 目標 | 證明沙盒的檔案、網路、憑證控制在你的主機上真的有效 |
| 前置條件 | 已依第 4 章建立 `dev-order`（Deep Agents、Restricted 層） |
| 操作步驟 | 1. 執行 4.10 的驗收腳本 2. 套用 6.11 的兩份唯讀 preset 3. 執行 6.12 的 V1～V6 4. 在 `openshell term` 觀察 V5 的待審請求並按 `x` 拒絕 5. `logs --tail 50` 截取拒絕紀錄 |
| 預期輸出 | 4.10 表格全部符合；V1 成功、V2～V5 被拒；V6 看得到拒絕紀錄 |
| 驗收標準 | 全部符合才可進行 A、B、C |
| 常見錯誤 | 選了 Balanced 層導致 `pypi` 等可通；忘了 Deep Agents 基準的 `github` 是 `access: full` |
| 安全檢查 | 檢查 6 的 `NO-RAW-KEY` |
| 人工審查點 | 政策審查者確認 preset 與驗證輸出 |

### 16.2 案例 A：新建 Web Application

| 項目 | 內容 |
|---|---|
| 目標 | 以 AI Agent 完成「建立訂單」功能：SRS → SDD → OpenAPI → 後端 → 前端 → 測試 → 交付 |
| 前置條件 | 演練 0 通過；內部 Git 有空 repo `demo/order-service`（含 7.5 的 AGENTS.md 與 `docs/spec/requirements-raw.md`）；CI 已設定 10.4 的關卡 |
| 合成需求 | 「業務人員可建立訂單，輸入客戶編號與金額；金額需大於 0；金額超過 5 萬元需主管覆核；可依訂單編號查詢。」 |

操作步驟：

| 步驟 | 動作 | 位置 |
|---|---|---|
| A1 | `git clone` repo 到 `/sandbox/work/order-service` | 📦（經 `connect`） |
| A2 | 執行範本 P1（7.6.1）產生 SRS | 📦 `dcode` TUI |
| A3 | 人工審查 SRS、回答 Q 清單、commit | 👤 |
| A4 | 執行 P2、P3 產生 SDD 與 OpenAPI | 📦 |
| A5 | 執行 P4：審查計畫 → 回覆「核准」→ 實作 | 📦 |
| A6 | 執行 P6 補測試 | 📦 |
| A7 | 本機跑 `check-layering.py`、`check-change-report.py` | 🖥️ 或 📦 |
| A8 | 套用寫入 preset（經核准）、push `ai/uc-01-place-order` | 🖥️ `policy add`；📦 `git push` |
| A9 | 開 PR、等 CI | 👤／🔧 |
| A10 | Code Review、合併；移除寫入 preset | 👤；🖥️ `policy remove corp-git-order-write --yes` |

Prompt：使用 7.6.1～7.6.6，Prompt 中的需求以上述合成需求為準。

預期輸出：

```text
docs/spec/SRS.md                    UC-01、UC-02；FR 約 6～10 條；Q 至少 2 條（例如「主管覆核流程」「金額幣別」）
docs/design/SDD.md                  元件圖、序列圖、DDL 草稿
docs/api/openapi.yaml               2 個路徑、problem+json 錯誤
src/main/java/com/example/order/... domain、application、adapter
src/test/java/...                   OrderTest（含 50000／50000.01 邊界）、ArchitectureTest
web/src/views/OrderCreate.vue       表單與錯誤顯示
.ai-reports/uc-01-place-order.md    交付報告
```

驗收標準：

- [ ] CI 全綠：`mvn verify`（含 ArchUnit）、前端 lint 與 unit test。
- [ ] `check-change-report.py` 0 問題；`check-layering.py` 0 違規。
- [ ] 邊界測試包含 `50000`（不需覆核）與 `50000.01`（需覆核）。
- [ ] OpenAPI 通過 linter；錯誤格式為 `application/problem+json`。
- [ ] 沒有新增未核准的依賴（`git diff origin/main -- pom.xml web/package.json`）。
- [ ] 前端沒有 `v-html`、金額以字串傳送。

常見錯誤：

| 錯誤 | 如何發現 |
|---|---|
| SRS 自行加入 SSO、權限角色 | 7.6.1 的抽查 |
| `>= 50000` 寫成覆核條件 | 邊界測試 |
| domain 放了 JPA annotation | ArchUnit `domainIsFrameworkFree` |
| 報告宣稱跑過 `mvn test`，但沙盒沒有 JDK | 7.13 案例；以 CI 為準 |
| 寫入 preset 用完沒移除 | `policy list` |

安全檢查：寫入 preset 只在 A8～A10 期間存在；推送的分支名稱符合 `ai/*`；`.ai-reports` 中沒有憑證或內部 URL 以外的敏感資料。

人工審查點：A3（SRS 簽核）、A5（計畫核准）、A10（Code Review 合併）。

### 16.3 案例 B：既有系統逆向工程

| 項目 | 內容 |
|---|---|
| 目標 | 對一個小型「舊系統」完成盤點、呼叫鏈、資料存取、商業規則、文件與回歸測試草稿 |
| 前置條件 | 演練 0 通過；準備合成的舊系統原始碼（🏢 建議：以案例 A 產出的 order-service 為底，刻意加入 MS950 編碼的註解檔、一支 Stored Procedure 檔與一支排程批次，作為「舊系統」） |
| 環境 | 依 8.2 建立 `re-legacy`：`--host-mount` 唯讀、Restricted、排除 `github` 與 `pypi` |

操作步驟：

| 步驟 | 動作 | 對應 |
|---|---|---|
| B1 | 主機端轉碼並建立凍結快照（8.8） | 🖥️ |
| B2 | 建立 `re-legacy`、驗證唯讀 | 8.2 |
| B3 | R1 盤點，主機端重算數字比對 | 8.5.2 |
| B4 | R2 呼叫鏈、R3 資料存取 | 8.5.3、8.5.4 |
| B5 | R4 商業規則 → `check-evidence.py` → 人工抽查 | 8.5.5、8.6 |
| B6 | R5 批次與介接、R6 圖 | 8.5.6、8.5.7 |
| B7 | R7 文件草稿 | 8.5.8 |
| B8 | R8／R9 行為案例與 characterization tests 草稿 | 8.5.9 |
| B9 | 在測試環境實際執行行為案例，填寫差異報告 | 8.10 |
| B10 | `download /sandbox/re-out/` 交付 | 🖥️ |

預期輸出：`inventory.md`、`modules.csv`、`call-graph.md`、`data-access.md`、`business-rules.md`、`integration.md`、`architecture.md`、`SRS.md`、`SDD.md`、`api.md`、`data-dictionary.md`、`behavior-cases.csv`、`tests/`、`regression-report.md`。

驗收標準：

- [ ] `check-evidence.py business-rules.md` 0 問題。
- [ ] `[事實]` 抽查 ≥ 20%，金額相關 100%；錯誤率 < 5%。
- [ ] 盤點數字與主機端 `find`／`wc` 結果一致。
- [ ] 刻意埋入的 SP 與批次都有被找到（找不到要在文件寫「未找到」並列出搜尋過的關鍵字）。
- [ ] `/sandbox/src` 內容未變（主機端比對快照的 `sha256sum`）。

常見錯誤：同一數值多處出現只取第一個（8.11）；把註解內容當成 `[事實]`；MS950 亂碼被猜成內容。

安全檢查：快照已跑過 gitleaks；沙盒 `policy list` 只剩推理相關項目；`re-out` 中的遮蔽字串（`***`）位置有列出。

人工審查點：B3（盤點正確性）、B5（商業規則抽查）、B9（行為比對判定）。

### 16.4 案例 C：Framework 升級

| 項目 | 內容 |
|---|---|
| 目標 | 把小型專案從舊版本升級，完成差異分析、計畫、分批修改、測試、報告與回復方案 |
| 前置條件 | 演練 0 通過；🏢 準備一個「Spring Boot 2.7＋Java 11＋`javax.*`」的合成專案（可請 Agent 依 7.7 的領域模型產生，再由人確認可在舊版建置） |
| 環境 | `up-order` 沙盒、Restricted＋`corp-maven-readonly`＋該 repo 的 Git 讀 preset |

操作步驟：

| 步驟 | 動作 | 對應 |
|---|---|---|
| C1 | 舊版基線：tag `pre-upgrade`，CI 全綠截圖 | 9.2 步驟 5 |
| C2 | U1 差異分析 → 人工以 `grep` 驗證數字 | 9.4.1 |
| C3 | U2 計畫 → 架構師核准 | 9.4.2 |
| C4 | 每批執行 U3 → PR → CI | 9.4.3 |
| C5 | 行為比對（9.5）：至少 API 回應與錯誤格式 | 9.5 |
| C6 | 升級報告與回復方案 | 9.6 |
| C7 | 在測試環境演練回復到 `pre-upgrade` | 9.6 |

Prompt：9.4.1～9.4.3。

預期輸出：`docs/upgrade/impact-analysis.md`、`docs/upgrade/plan.md`、每批一個 PR、`docs/upgrade/report.md`。

驗收標準：

- [ ] 每個批次 PR 的 CI 全綠；沒有停用測試。
- [ ] `grep -rn "import javax\." src/main/java` 只剩 JDK 本身的 `javax`（例如 `javax.crypto`），不剩 Jakarta EE 相關的 `javax.persistence`、`javax.validation`、`javax.servlet`。
- [ ] 每批 `git diff --stat` 的檔案數與計畫預估差異 < 20%，或有書面解釋。
- [ ] 錯誤回應格式的差異已在報告中記錄與判定。
- [ ] 回復演練成功。

常見錯誤：一次改完所有批次；混入格式化；註解掉找不到 Jakarta 版本的依賴（9.4.3 壞例）；Agent 自行挑選依賴版本。

安全檢查：升級沙盒沒有公開 Maven Central 的出口（只走內部 Nexus）；新依賴經 SCA 掃描。

人工審查點：C3（計畫核准）、C4（每批 Code Review）、C6（報告簽核）。

### 16.5 演練評分表

| 項目 | 配分 | 評分標準 |
|---|---|---|
| 演練 0 安全驗證 | 20 | 全部符合才給分；任一項不符 0 分 |
| 流程遵循（先計畫、等核准、小步） | 20 | 依 commit 與對話紀錄 |
| 工具驗證（lint、check-*、CI） | 20 | 全部通過 |
| 審查品質（找到刻意埋的錯誤） | 20 | 講師在案例中埋 3 個錯誤，找到 1 個 6 分 |
| 文件與報告 | 10 | 交付報告、升級報告、差異報告完整 |
| 安全操作 | 10 | 無禁止行為（13.11） |

### 16.6 本章實務案例與注意事項

**案例**：教育訓練中，一位學員在案例 A 的 A8 之後忘了移除寫入 preset，隔天繼續用同一沙盒做案例 C。

影響：案例 C 期間 Agent 仍能推送到 order-service repo。雖然 Git Server 的 `ai/*` 分支權限擋住了主線，但仍可能推送與案例 C 無關的分支。

改善：寫入 preset 的套用與移除寫進同一個腳本（套用、push、移除）；每日巡檢（11.2）比對 `policy list` 與核准清單。

**注意事項**：

- 演練用的合成專案放在獨立的 Git 群組，與真實專案隔離。
- 講師可以預先在案例 B 的「舊系統」裡埋入矛盾的註解與重複的魔術數字，訓練學員抓出 Agent 的錯誤。
- 演練產出（交付報告、工具輸出）可作為 15 章指標的第一批基準資料。

## 第17章 常見問題 FAQ

所有回答以 v0.0.139 官方文件與原始碼為準；有平台或版本限制的地方會註明。

### 17.1 NemoClaw 是否等於 OpenShell？

不是。NemoClaw 是參考堆疊（主機 CLI、Blueprint、Agent 整合層、preset、生命週期流程），OpenShell 是底層執行環境（Gateway、沙盒、L7 代理、政策執行、憑證保管）。NemoClaw 呼叫 OpenShell 的 API 與 CLI 來建立並設定沙盒。v0.0.139 綁定 OpenShell 0.0.116；你可以不用 NemoClaw 而直接用 OpenShell（「OpenShell 路徑」），但那就要自己準備映像檔、政策、Provider 與整合（1.2、1.9）。

🔍 **自己驗證**：`nemoclaw --version` 與 `openshell --version` 會印出兩個不同的版本號（v0.0.139 與 0.0.116），證明它們是兩套軟體。

### 17.2 NemoClaw 是否會自動保證 AI 產出程式碼安全？

不會。NemoClaw 控制的是 Agent「能碰什麼」（檔案、網路、程序、憑證），不判斷 Agent「寫了什麼」。程式碼的正確性與安全性要靠測試、SAST／SCA、ArchUnit 與人工 Code Review（第 7、10 章）。

🔍 **自己驗證**：拿一個 AI 產出的 PR，跑一次 `check-change-report.py` 與 `check-test-weakening.py`（7.10、13.8），看看沙盒之外還需要多少層檢查。

### 17.3 Agent 能否讀取沙盒以外的檔案？

在正常設定下不能：沙盒只看得到自己的檔案系統，系統路徑唯讀，Landlock 在核心層限制。例外：(1) 你以 `--host-mount` 掛入的主機目錄（唯讀）；(2) 你以 `share mount` 建立的 SSHFS 雙向掛載；(3) 核心低於 5.13 或 macOS Docker VM 不支援 Landlock 時，OpenClaw 的 `best_effort` 會降級為只靠容器掛載（Deep Agents 是 `strict`，無法執行會直接啟動失敗）。用 4.10 的檢查 4 驗證。

🔍 **自己驗證**：`nemoclaw <名稱> exec -- ls /home /mnt /Users 2>&1` 不應看到主機的家目錄內容；`nemoclaw <名稱> share status` 應沒有非預期的掛載。

### 17.4 如何限制 Agent 的網路連線？

網路預設拒絕。onboarding 時選 Restricted 層，之後只用 `nemoclaw <名稱> policy add` 套用審查過的 preset（6.11～6.12）；必要時以 `policy exclude` 移除不需要的基準項目（例如 Deep Agents 的 `github`）。一次性需求在 `openshell term` 核准單一規則。避免 `openshell policy set` 整份替換，除非 preset 無法表達（6.13）。

🔍 **自己驗證**：`nemoclaw <名稱> policy list` 看目前套用的 preset；在沙盒內 `curl` 一個未放行的網址，應被拒絕（4.10）。

### 17.5 能否使用私有模型或本地模型？

可以，但支援程度不同：企業私有的 OpenAI 相容端點走「Other OpenAI-compatible endpoint」（Tested with limitations，相容性需實測）；本地 Ollama 為 Tested with limitations；本地 vLLM 在 DGX Spark 為 Tested、在一般 Linux GPU 主機需 `NEMOCLAW_EXPERIMENTAL=1` 或 `NEMOCLAW_PROVIDER=install-vllm`；本地 NIM 與 llama.cpp 為 Experimental。只支援 NVIDIA GPU。私有 IP 端點需以 `NEMOCLAW_TRUSTED_PRIVATE_HOSTS` 明確信任（3.7、14.5）。

🔍 **自己驗證**：`nemoclaw <名稱> status --json | jq '{provider, model, recordedRoute, inferenceHealth}'`，確認 Provider 是你預期的私有端點，再照 4.9 送一次請求。

### 17.6 如何管理外部 API Key？

在 onboarding 前以 `read -r -s` 讀入環境變數，onboarding 完成後 `unset`；NemoClaw 把它註冊到 OpenShell Gateway，沙盒內只有 placeholder。用 `nemoclaw credentials list` 查看名稱、`nemoclaw <名稱> status` 實際驗證、以新值重跑 `nemoclaw onboard --name <名稱>` 輪替、`nemoclaw credentials reset` 移除。外洩時先在上游撤銷（6.6）。注意：Provider 憑證是 Gateway 範圍，同一主機的沙盒共用（14.4）。

🔍 **自己驗證**：照 13.5 的驗證 2，比對沙盒內變數的雜湊與真實 Key 的雜湊，兩者必須不同。

### 17.7 可以在 Windows 環境使用嗎？

可以，但只有「Windows 10（build 19041+）或 11 ＋ WSL 2 ＋ Docker Desktop（WSL backend）或合格的 rootless Podman」這條路，平台矩陣狀態是 **Tested with limitations**、沒有專屬 CI，官方以 x86-64 測試。所有 NemoClaw 指令都在 WSL 的 Ubuntu 裡執行，不在 PowerShell。原生 Windows 沒有安裝路徑；`--host-mount` 在 WSL 2 的 Docker 上可用（3.4）。

🔍 **自己驗證**：在 PowerShell 執行 `wsl -l -v`，Ubuntu 的 VERSION 要是 `2`；在 WSL 內執行 `docker info` 能成功，才繼續安裝（3.4）。

### 17.8 如何切換或更新 Agent？

官方規則是「每個沙盒名稱只對應一種 Agent」，同名 onboarding 另一種 Agent 會被拒絕（`Sandbox 'X' already exists as OpenClaw`）。要換 Agent，建議以新名稱 onboarding（例如 `nemohermes onboard --name my-hermes`），讓兩者並存；若一定要沿用名稱，官方做法是先 `nemoclaw <名稱> destroy` 再以新 Agent onboarding（⛔ `destroy` 不可復原，先 `download` 需要的檔案）。要更新 Agent 版本，升級 NemoClaw 後執行 `nemoclaw <名稱> rebuild`；⛔ 不要在沙盒內就地更新 Agent（例如 `openclaw update`），因為 Agent 版本綁在映像檔（12.1）。

🔍 **自己驗證**：`nemoclaw list` 確認沙盒名稱與 Agent 的對應；rebuild 後 `nemoclaw <名稱> status` 的 Agent 版本應是新版。

### 17.9 如何保留工作狀態？

日常的 stop／start／reconnect／Gateway 重啟，OpenShell 會保留 Agent 的原生 home 與工作區。`rebuild` 會封存、驗證並還原整棵原生 home。`destroy` 會刪除，無法復原。🏢 建議再加一層：工作副本推送到 Git，重要檔案以 `nemoclaw <名稱> download` 做獨立備份；升級前 `nemoclaw backup-all`（5.10、12.3）。憑證不在任何封存中。

🔍 **自己驗證**：用 12.7 的檔案指紋比對，確認 `rebuild` 前後工作區一致。

### 17.10 如何避免 AI 修改錯誤的程式碼？

多層防護：(1) 技術上，工作副本只在沙盒、Git 寫入 preset 只放行特定 repo、Token 只能推 `ai/*` 分支、主線受保護；逆向工程以唯讀掛載；(2) 流程上，Prompt 要求先計畫、等核准、小步修改；Deep Agents 互動模式逐次核准 shell 指令；(3) 驗證上，`check-change-report.py` 比對報告與 `git diff`、ArchUnit、CI 測試；(4) 最後由人 Code Review（7.6、10.3）。

🔍 **自己驗證**：用 AI Token 執行 `git push --dry-run origin HEAD:main`，應被拒絕（14.4）。

### 17.11 如何確認模型或 Agent 版本相容？

NemoClaw 版本：`nemoclaw --version`；OpenShell 範圍：`nemoclaw-blueprint/blueprint.yaml` 的 `min_openshell_version`／`max_openshell_version`；Agent 版本：`nemoclaw <名稱> status` 的 Agent 行（Deep Agents 的 manifest 期望 `dcode` 0.1.71）；模型：onboarding 會驗證 Provider 與模型，`nemoclaw <名稱> status` 會實際送一次推理請求。平台與 Provider 的相容狀態以 Platform Support 頁為準（12.2）。

🔍 **自己驗證**：`curl -fsSL https://raw.githubusercontent.com/NVIDIA/NemoClaw/v0.0.139/nemoclaw-blueprint/blueprint.yaml | grep openshell_version`，比對 `openshell --version`。

### 17.12 Alpha 階段是否適合企業正式上線？

不適合處理正式環境工作負載或真實客戶資料。官方標示 alpha／Early preview、無 SLA、介面可能變動，且明列無 RBAC、無 SSO、無多租戶、無集中稽核、不支援離線。適合的是：在隔離的非正式環境、以合成或內部等級資料、經明確風險接受後試行（14.11、14.12）。

🔍 **自己驗證**：讀官方 Platform Support 頁頂端的 Stage／Label，再對照 14.12 的風險接受單是否已簽核。

### 17.13 `lkg` 與 latest 有什麼不同？

`lkg`（last known good）是管理者推進的標籤，官方安裝程式預設安裝它；研究當日 `lkg` 指向 v0.0.137，而官方文件站 latest 已是 v0.0.139。企業應一律以 `NEMOCLAW_INSTALL_TAG=<版本>` 指定版本，並清空 `NEMOCLAW_INSTALL_REF`（4.4）。

🔍 **自己驗證**：`git ls-remote https://github.com/NVIDIA/NemoClaw.git 'refs/tags/lkg^{}' 'refs/tags/v0.0.139^{}'`，兩行的 commit 不同，就代表 `lkg` 不是最新版（12.11 有研究日的輸出）。

### 17.14 網路上看到的 `nemoclaw plan`／`nemoclaw apply` 是什麼？

那是 Rust 重寫的 v1 預覽線（`v1` 分支、`v0.1.0-rc*`、`v1.0.0-rc1` 標籤），採宣告式 YAML 的 plan／apply／destroy，搭配 OpenShell 0.1.4，官方明言尚無支援政策與企業部署驗證。與本手冊的 v0.0.x 不相容；可用 `nemoclaw config export` 為將來的遷移保留設定（1.7）。

🔍 **自己驗證**：`nemoclaw --help` 中沒有 `plan`／`apply`；v1 的狀態用 1.7 的指令確認。

### 17.15 可以讓 Agent 直接用我在主機上的 IDE 專案目錄嗎？

不建議。`--host-mount` 只能唯讀；`share mount` 雖然雙向，但等於讓 Agent 寫入主機目錄。建議在沙盒內 `git clone` 工作副本，Agent 在 `ai/*` 分支上工作，你在 IDE 端 checkout 該分支檢視（7.2）。

🔍 **自己驗證**：`nemoclaw <名稱> share status` 應沒有掛載；若用了 `--host-mount`，在沙盒內 `touch` 該目錄下的檔案應失敗（唯讀）。

### 17.16 NemoClaw 會把我的資料送給 NVIDIA 嗎？

安裝程式與 CLI 預設會嘗試送出**匿名的操作完成遙測**到 NVIDIA 的固定接收端；以 `export NEMOCLAW_DISABLE_TELEMETRY=1` 在每個 shell 停用。推理請求的內容則送到你選擇的推理服務（若選 NVIDIA Endpoints 就是 NVIDIA）。Prompt、Agent 讀進來的檔案、工具結果都會成為推理請求的一部分，依 13.6 資料分級決定推理服務。

🔍 **自己驗證**：`echo $NEMOCLAW_DISABLE_TELEMETRY` 在每個新 shell 都應印出 `1`；把它寫進 `~/.bashrc` 後，開一個新終端機再確認一次。

### 17.17 NemoClaw 有已知的安全漏洞嗎？

有，而且是集中公告的。NVIDIA Security Bulletin 5872（2026-08-25）一次公告 18 個 CVE，影響 NemoClaw 0.0.25 以前與 OpenShell 0.0.33 以前的版本，最高為 CVSS 9.9 的沙盒逃逸。v0.0.139／OpenShell 0.0.116 已不在受影響範圍內。企業要訂閱 NVIDIA Product Security 公告，並用版本下限腳本盤點所有主機（6.17）。

🔍 **自己驗證**：執行 `bash check-security-floor.sh`（6.17.1），兩行都要是 `OK`，結束碼 0。

### 17.18 下一版會換成 OpenShell 0.1.5 嗎？

很可能，但研究日還沒有。`main` 的 PR #12603 正在把 OpenShell 升到 0.1.5，PR 自己標示「尚未可以核准或合併」，完整 E2E 仍有失敗。發布後，推理路由、Gateway、舊 volume 的處理都會改變，舊 volume 不會自動複製。核准前要照 12.11 的影響表在測試主機演練（12.4）。

🔍 **自己驗證**：`gh pr view 12603 -R NVIDIA/NemoClaw --json state,mergedAt`，以及 `main` 的 `blueprint.yaml` 中的 `max_openshell_version`（12.11）。

### 17.19 `status --json` 的 `liveRoute` 是 `null`，是不是壞了？

如果沙盒用的是原生附掛的 Provider（NVIDIA、固定託管或原生本地），`liveRoute` 與 `routeDrift` 永遠是 `null`，這是設計如此，不是故障。改看 `recordedRoute` 與 `inferenceHealth`（5.9）。

🔍 **自己驗證**：`nemoclaw <名稱> status --json | jq '{provider, recordedRoute, liveRoute, inferenceHealth}'`；再照 4.9 送一次測試請求，能得到回應就代表推理正常。

## 第18章 參考資料與附錄

研究日期：**2026-10-27**。下表的「適用版本」以研究當日可確認者為準；外部標準與框架文件以該站最新版為準。

### 18.1 官方儲存庫

| 名稱 | 網址 | 用途 | 適用版本／研究日期 |
|---|---|---|---|
| NemoClaw | [github.com/NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | 原始碼、Issue、Discussions | `main`＠`bafe6cc`（2026-10-26） |
| NemoClaw v0.0.139 原始碼 | [tree/v0.0.139](https://github.com/NVIDIA/NemoClaw/tree/v0.0.139) | 本手冊核對基準 | v0.0.139（`a08ae7a`） |
| 安裝程式 | [install.sh（v0.0.139）](https://github.com/NVIDIA/NemoClaw/blob/v0.0.139/install.sh) | bootstrap 行為與參數 | v0.0.139 |
| Blueprint | [blueprint.yaml（v0.0.139）](https://github.com/NVIDIA/NemoClaw/blob/v0.0.139/nemoclaw-blueprint/blueprint.yaml) | OpenShell 版本範圍、映像檔 digest | v0.0.139 |
| 政策與 preset | [nemoclaw-blueprint/policies（v0.0.139）](https://github.com/NVIDIA/NemoClaw/tree/v0.0.139/nemoclaw-blueprint/policies) | 基準政策、層級、preset 原始檔 | v0.0.139 |
| Agent 整合 | [agents/（v0.0.139）](https://github.com/NVIDIA/NemoClaw/tree/v0.0.139/agents) | 各 Agent 的 manifest 與政策 | v0.0.139 |
| 平台矩陣 | [ci/platform-matrix.json](https://github.com/NVIDIA/NemoClaw/blob/main/ci/platform-matrix.json) | 支援狀態唯一來源 | main |
| 安全政策 | [SECURITY.md](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md) | 漏洞私密回報管道 | main |
| NVIDIA 安全公告原始資料 | [NVIDIA/product-security](https://github.com/NVIDIA/product-security) | 機器可讀的 CSAF 公告（`2026/5872` 為 NemoClaw／OpenShell 2026 年 8 月公告） | 研究日 |
| OpenShell 0.1.5 升級 PR | [NVIDIA/NemoClaw#12603](https://github.com/NVIDIA/NemoClaw/pull/12603) | 下一版預警（12.11） | 研究日：OPEN |
| v1 預覽線 | [tree/v1](https://github.com/NVIDIA/NemoClaw/tree/v1) | Rust 重寫、desired-state YAML | `v1`＠`c2a71f8`（2026-10-27） |
| 社群範例 | [NVIDIA/nemoclaw-community](https://github.com/NVIDIA/nemoclaw-community) | 社群範例與 Blueprint 模式 | 研究日 |
| OpenShell | [github.com/NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | 底層執行環境 | 最新 v0.1.5；NemoClaw 使用 0.0.116 |
| OpenShell 0.0.116 | [Release v0.0.116](https://github.com/NVIDIA/OpenShell/releases/tag/v0.0.116) | NemoClaw v0.0.139 綁定版本 | 2026-08-28 發布 |
| DGX Spark Playbooks | [NVIDIA/dgx-spark-playbooks](https://github.com/NVIDIA/dgx-spark-playbooks) | DGX Spark 上的 NemoClaw 流程 | 研究日 |

### 18.2 官方安裝與快速入門文件

| 名稱 | 網址 | 用途 |
|---|---|---|
| NemoClaw 文件首頁 | [docs.nvidia.com/nemoclaw/latest](https://docs.nvidia.com/nemoclaw/latest/) | 文件入口（latest＝v0.0.139） |
| Overview | [about/overview](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/about/overview) | 定位與能力 |
| Architecture Overview | [about/how-it-works](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/about/how-it-works) | 元件、保護層 |
| Ecosystem | [about/ecosystem](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/about/ecosystem) | NemoClaw 與 OpenShell 路徑比較 |
| Architecture Details | [reference/architecture](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/architecture) | Blueprint、推理路由、主機狀態 |
| Prerequisites | [get-started/prerequisites](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/prerequisites) | 硬體、軟體、平台 |
| Windows Preparation | [additional-setup/windows-preparation](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/additional-setup/windows-preparation) | WSL 2 與 Docker Desktop |
| Quickstart（OpenClaw） | [get-started/quickstart](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/quickstart) | 首次安裝 |
| Quickstart（Hermes） | [hermes/get-started/quickstart](https://docs.nvidia.com/nemoclaw/latest/user-guide/hermes/get-started/quickstart) | Hermes |
| Quickstart（Deep Agents） | [deepagents/get-started/quickstart](https://docs.nvidia.com/nemoclaw/latest/user-guide/deepagents/get-started/quickstart) | Deep Agents Code |
| Run Deep Agents Code | [run-deep-agents-code](https://docs.nvidia.com/nemoclaw/latest/user-guide/deepagents/manage-sandboxes/operate-sandboxes/run-deep-agents-code) | `dcode` 互動與無頭模式 |
| Platform Support | [reference/platform-support](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/platform-support) | 支援狀態 |
| Enterprise Readiness | [reference/enterprise-readiness](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/enterprise-readiness) | 企業能力邊界 |
| CLI Commands | [reference/commands](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/commands) | 指令參考 |
| CLI Selection Guide | [reference/cli-selection-guide](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/cli-selection-guide) | `nemoclaw` 與 `openshell` 分工 |
| System Readiness | [reference/system-readiness](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/system-readiness) | `host probe` |
| Host Files and State | [reference/host-files-and-state](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/host-files-and-state) | `~/.nemoclaw/` |
| Troubleshooting | [reference/troubleshooting](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/troubleshooting) | 故障排除 |
| Update Sandboxes | [update-sandboxes](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/operate-sandboxes/update-sandboxes) | 升級 |
| Recover and Rebuild | [recover-and-rebuild-sandboxes](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/operate-sandboxes/recover-and-rebuild-sandboxes) | 復原與重建 |
| Uninstall | [uninstall-nemoclaw](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/operate-sandboxes/uninstall-nemoclaw) | 解除安裝 |
| Understand Runtime Changes | [understand-runtime-changes](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/configure-sandboxes/understand-runtime-changes) | 執行期 vs 重建 |
| Persist Sandbox State | [create-and-restore-snapshots](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/state-and-backups/create-and-restore-snapshots) | 狀態保存 |
| Transfer State Manually | [transfer-state-manually](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/state-and-backups/transfer-state-manually) | 手動備份 |
| Understand Sandbox State | [understand-sandbox-state](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/state-and-backups/understand-sandbox-state) | `--host-mount`、工作區 |
| Deploy to a Headless Server | [deploy-to-headless-server](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/deployment/deploy-to-headless-server) | 遠端主機 |
| Release Notes | [release-notes](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/release-notes) | 版本變更 |
| Use Docs with Coding Agents | [resources/agent-skills](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/resources/agent-skills) | 給 Coding Agent 的文件入口 |

### 18.3 安全與政策文件

| 名稱 | 網址 | 用途 |
|---|---|---|
| Network Policies | [reference/network-policies](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/reference/network-policies) | 基準政策、層級 |
| Customize Network Policy | [customize-network-policy](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/network-policy/customize-network-policy) | 政策工作流程選擇 |
| Apply Policy Presets | [apply-policy-presets](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/network-policy/configure-policies/apply-policy-presets) | preset 套用 |
| Create Custom Policy Presets | [create-custom-policy-presets](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/network-policy/configure-policies/create-custom-policy-presets) | 自訂 preset 規則 |
| Replace the Live Network Policy | [replace-live-network-policy](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/network-policy/configure-policies/replace-live-network-policy) | 整份替換 |
| Approve Network Requests | [approve-network-requests](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/network-policy/approve-network-requests) | `openshell term` 核准 |
| Security Best Practices | [security/best-practices](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/best-practices) | 控制與風險取捨 |
| Filesystem Controls | [filesystem-controls](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/security-controls/filesystem-controls) | 檔案系統 |
| Process Controls | [process-controls](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/security-controls/process-controls) | 程序 |
| Credential Storage | [credential-storage](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/credential-storage) | 憑證儲存 |
| Credential Rotation | [credential-rotation](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/credential-rotation) | 輪替與緊急處置 |
| Corporate CA Trust | [configure-corporate-ca-trust](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/configure-corporate-ca-trust) | 企業 CA |
| Trusted Computing Base | [trusted-computing-base](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/security/trusted-computing-base) | 信任邊界 |
| Review Sandbox Hardening | [review-sandbox-hardening](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/manage-sandboxes/configure-sandboxes/review-sandbox-hardening) | 容器強化 |
| Monitor Sandbox Activity | [monitor-sandbox-activity](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/monitoring/monitor-sandbox-activity) | 監控與除錯 |
| NVIDIA Product Security | [nvidia.com/security](https://www.nvidia.com/en-us/security/) | 安全公告訂閱、漏洞回報 |
| Security Bulletin 5872 | [a_id/5872](https://nvidia.custhelp.com/app/answers/detail/a_id/5872) | 2026-08 NemoClaw／OpenShell 公告（6.17） |
| Canadian Centre for Cyber Security AV26-849 | [AV26-849](https://cyber.gc.ca/en/alerts-advisories/nvidia-security-advisory-av26-849) | 第三方對公告 5872 的轉述與影響範圍 |
| OpenShell 文件 | [docs.nvidia.com/openshell/latest](https://docs.nvidia.com/openshell/latest/) | ⚠️ latest 為 v0.1.5，與 NemoClaw 使用的 0.0.116 不同 |
| OpenShell 原始碼 docs | [NVIDIA/OpenShell/docs](https://github.com/NVIDIA/OpenShell/tree/main/docs) | 文件原始檔 |
| OpenShell 範例 | [NVIDIA/OpenShell/examples](https://github.com/NVIDIA/OpenShell/tree/main/examples) | 政策範例 |

### 18.4 Agent 官方文件

| 名稱 | 網址 | 用途 |
|---|---|---|
| OpenClaw | [openclaw.ai](https://openclaw.ai) | 預設 Agent |
| OpenClaw Docs | [docs.openclaw.ai](https://docs.openclaw.ai) | OpenClaw 設定與指令 |
| Hermes | [get-hermes.ai](https://get-hermes.ai/) | Hermes Agent |
| LangChain Deep Agents Code | [Deep Agents Code Overview](https://docs.langchain.com/oss/python/deepagents/code/overview) | `dcode` |

> 📌 **註記**：`openclaw.ai` 與 `docs.openclaw.ai` 取自官方 NemoClaw README 與 Ecosystem 頁；研究當日在撰寫環境連線時被 TLS 層拒絕（`TLSV1_ALERT_ACCESS_DENIED`），無法驗證頁面內容（🧪）。其餘本章連結皆已逐一確認回應 200。

### 18.5 模型與推理服務

| 名稱 | 網址 | 用途 |
|---|---|---|
| NVIDIA Build（NVIDIA Endpoints） | [build.nvidia.com](https://build.nvidia.com/) | 託管模型與 API Key |
| DGX Spark NemoClaw Playbook | [build.nvidia.com/spark/nemoclaw](https://build.nvidia.com/spark/nemoclaw) | DGX Spark 本地推理流程 |
| vLLM | [docs.vllm.ai](https://docs.vllm.ai/) | 本地／私有推理伺服器 |
| Ollama | [ollama.com](https://ollama.com/) | 本地模型 |

### 18.6 容器與作業系統

| 名稱 | 網址 | 用途 |
|---|---|---|
| Docker Engine Security | [docs.docker.com/engine/security](https://docs.docker.com/engine/security/) | daemon 攻擊面、`docker` 群組風險 |
| Docker seccomp | [seccomp profiles](https://docs.docker.com/engine/security/seccomp/) | 系統呼叫過濾 |
| Docker Desktop WSL 2 | [Docker Desktop WSL](https://docs.docker.com/desktop/features/wsl/) | WSL backend |
| WSL 安裝 | [Install WSL](https://learn.microsoft.com/windows/wsl/install) | Windows 前置 |
| Landlock | [Landlock LSM](https://docs.kernel.org/userspace-api/landlock.html) | 核心檔案系統限制 |

### 18.7 軟體安全與 SSDLC 標準

| 名稱 | 網址 | 用途 |
|---|---|---|
| OWASP Top 10 | [owasp.org/Top10](https://owasp.org/Top10/) | Web 風險 |
| OWASP ASVS | [ASVS](https://owasp.org/www-project-application-security-verification-standard/) | 安全驗證標準（7.6.8） |
| OWASP SAMM | [owaspsamm.org](https://owaspsamm.org/) | 成熟度模型 |
| OWASP Top 10 for LLM | [genai.owasp.org/llm-top-10](https://genai.owasp.org/llm-top-10/) | LLM 應用風險（Prompt Injection 等） |
| OWASP Top 10 for Agentic Applications 2026 | [genai.owasp.org](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Agent 風險 ASI01～ASI10（6.18） |
| gitleaks | [github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 偵測進入 Git 的祕密（13.5） |
| NIST SSDF SP 800-218 | [csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final) | 安全開發框架 |
| SLSA | [slsa.dev](https://slsa.dev/) | 供應鏈完整性 |
| CycloneDX | [cyclonedx.org](https://cyclonedx.org/) | SBOM |
| SPDX | [spdx.dev](https://spdx.dev/) | SBOM／授權 |
| gitleaks | [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | 機密掃描 |
| OWASP Dependency-Check | [Dependency-Check](https://owasp.org/www-project-dependency-check/) | 依賴弱點 |
| Trivy | [trivy.dev](https://trivy.dev/) | 映像檔與依賴掃描 |

### 18.8 Framework 與測試工具官方指南

| 名稱 | 網址 | 用途 |
|---|---|---|
| Oracle JDK 21 Migration Guide | [JDK 21 Migration](https://docs.oracle.com/en/java/javase/21/migrate/index.html) | Java 升級 |
| Spring Boot 3.0 Migration Guide | [Spring Boot 3.0 Migration](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide) | Spring Boot 升級 |
| Spring Framework Versions | [Spring Framework Versions](https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions) | 支援矩陣 |
| Vue 3 Migration Guide | [v3-migration.vuejs.org](https://v3-migration.vuejs.org/) | Vue 升級 |
| Angular Update Guide | [angular.dev/update-guide](https://angular.dev/update-guide) | Angular 升級 |
| TypeScript Release Notes | [TypeScript Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/overview.html) | TS 升級 |
| Node.js Releases | [Node.js Releases](https://nodejs.org/en/about/previous-releases) | LTS 時程 |
| Maven Release History | [Maven History](https://maven.apache.org/docs/history.html) | Maven 版本 |
| Gradle Upgrading | [Upgrading Gradle 8](https://docs.gradle.org/current/userguide/upgrading_version_8.html) | Gradle 升級 |
| OpenRewrite | [docs.openrewrite.org](https://docs.openrewrite.org/) | 確定性重構 recipe |
| JUnit 5 User Guide | [JUnit 5](https://junit.org/junit5/docs/current/user-guide/) | 單元測試 |
| ArchUnit User Guide | [ArchUnit](https://www.archunit.org/userguide/html/000_Index.html) | 架構測試（7.8） |
| Testcontainers for Java | [java.testcontainers.org](https://java.testcontainers.org/) | 整合測試 |
| Playwright | [playwright.dev](https://playwright.dev/docs/intro) | E2E |

### 18.9 附錄

#### 18.9.1 附錄 1：安裝前檢查清單

- [ ] 平台為 Ubuntu 24.04（或 WSL 2 Ubuntu 24.04／Apple Silicon macOS），已確認 3.1 的支援狀態。
- [ ] 主機為個人專用（非多使用者共用）。
- [ ] CPU ≥ 4、RAM ≥ 8 GB（建議 16 GB 以上）、可用磁碟 ≥ 20 GB（建議 40 GB 以上）。
- [ ] 核心 ≥ 5.13（Landlock）。
- [ ] Docker 可用；`docker` 群組的使用符合公司規範。
- [ ] `git`、`strings`（binutils）、`sha256sum`、`curl` 已安裝。
- [ ] 容器內 DNS 正常（`docker run --rm busybox nslookup registry.npmjs.org`）。
- [ ] 可連 `www.nvidia.com`、`github.com`、`ghcr.io`、`registry.npmjs.org` 與推理端點。
- [ ] 企業 Proxy 與 CA 已準備（`NEMOCLAW_PROXY_HOST`、`NEMOCLAW_CORPORATE_CA_BUNDLE`）。
- [ ] 已取得專案專屬、低額度的推理 API Key（存於密碼庫）。
- [ ] 已決定版本（`NEMOCLAW_INSTALL_TAG`）與 Agent。
- [ ] 環境申請單已核准（13.2）。

#### 18.9.2 附錄 2：安裝後驗收清單

- [ ] `nemoclaw --version` 為核准版本；`openshell --version` 為 Blueprint 指定版本。
- [ ] `nemoclaw host probe` 結束碼 0。
- [ ] `nemoclaw doctor` 全部通過。
- [ ] `nemoclaw <名稱> status`：Ready、Inference healthy、Agent 版本正確。
- [ ] 4.9 的測試請求回覆預期字串。
- [ ] 4.10 控制有效性驗證 7 項全部符合。
- [ ] `~/.bashrc` 含 `export NEMOCLAW_DISABLE_TELEMETRY=1`。
- [ ] 12.2 盤點表已存檔並附在申請單。

#### 18.9.3 附錄 3：沙盒安全檢查清單

- [ ] 政策層級為 Restricted（不是 Balanced、Open、Personal）。
- [ ] `policy list` 只有核准的 preset。
- [ ] Deep Agents 的 `github` 基準項目已依需求排除或保留並記錄理由。
- [ ] 所有自訂 preset 通過 `nemoclaw-policy-lint.py`（0 ERROR）。
- [ ] 6.12 V1～V6 全部符合。
- [ ] 沒有寫入 preset 長期掛著。
- [ ] 沙盒內沒有 `.env`、私鑰、正式環境憑證。
- [ ] 未啟用訊息通道、Dashboard 未對外綁定、未開 `NEMOCLAW_EXPERIMENTAL`。
- [ ] 沒有 `share mount` 掛家目錄。
- [ ] 沙盒無任何通往正式環境的路徑。

#### 18.9.4 附錄 4：AI Agent 開發工作流程（一頁版）

1. 規格放進 `docs/spec/`；AGENTS.md 就位（7.5）。
2. Agent 讀規格與程式 → 提出計畫（不改檔）。
3. 人工核准計畫。
4. Agent 在 `ai/<任務>` 分支小步實作、補測試。
5. Agent 輸出交付報告（修改清單、測試結果、未完成與待確認）。
6. 工具驗證：`check-change-report.py`、`check-layering.py`。
7. 套用寫入 preset（經核准）→ push → 移除寫入 preset。
8. 開 PR → CI（建置、測試、ArchUnit、SAST、SCA、機密掃描）。
9. 人工 Code Review（看完整 diff）→ 合併或退回。

#### 18.9.5 附錄 5：逆向工程 Prompt 範本（一頁版）

```text
【逆向工程共同規則】原始碼在 /sandbox/src（唯讀），輸出寫到 /sandbox/re-out/。禁止修改原始碼、禁止連線資料庫或外部系統。
每條結論標 [事實]（來源：路徑:起-迄）或 [推測]（依據：…；待確認 Q-xx）。找不到寫「未找到」並列出搜尋過的路徑與關鍵字。
MS950 亂碼回報檔名不猜內容；疑似機密以 *** 遮蔽並列出位置。最後輸出：檔案清單、[事實]／[推測] 數量、待確認問題。

R1 盤點：目錄樹（深度 3）、檔案數與行數、建置工具與框架版本、設定檔清單 → inventory.md、modules.csv
R2 呼叫鏈：URL → JSP → Action/Controller → Service → DAO → SQL/SP（表格附路徑:行）→ call-graph.md
R3 資料存取：DAO 方法、SQL 原文、資料表、SP 與參數、動態 SQL 位置 → data-access.md、tables.csv
R4 商業規則：條件、例外、錯誤碼；未實作的命名暗示標 [推測]；規則衝突另列 → business-rules.md
R5 批次與介接：排程、MQ、檔案交換、外部 URL、重跑與失敗處理 → integration.md
R6 圖：系統架構圖、端到端資料流圖（節點都要能追溯到 R1～R5）→ architecture.md
R7 文件：SRS、SDD、api、data-dictionary（開頭註明快照日期與 commit）
R8 行為案例：每條 [事實] 規則的輸入與預期輸出 → behavior-cases.csv（不執行）
R9 回歸測試：characterization tests 草稿（_currentBehavior）與 regression-report.md 範本
```

#### 18.9.6 附錄 6：Framework 升級 Prompt 範本（一頁版）

```text
U1 差異分析（不改檔）：依官方 Migration Guide 逐條列出 章節｜檔案:行號｜目前寫法｜需要的修改｜自動化可行性；
   列出 javax.* 數量；列出沒有 Jakarta 版本的依賴（查不到寫「未確認」）；列出測試覆蓋不足的模組 → impact-analysis.md
U2 計畫（不改檔）：分批（每批可獨立建置與測試）、每批範圍、預估檔案數、驗證、回復、風險與緩解、需人工決策處 → plan.md
U3 單批修改：只做計畫中的批次 N；在 ai/upgrade-batch-N 分支；不順手重構、不改格式、不升級計畫外依賴；
   每類修改一個 commit；遇到計畫外問題停下回報；完成後輸出交付報告與 git diff --stat
```

#### 18.9.7 附錄 7：故障排除紀錄範本

| 欄位 | 填寫內容 |
|---|---|
| 紀錄編號／日期時間 | |
| 主機／沙盒／版本 | NemoClaw（填寫）／OpenShell（填寫）／Agent（填寫） |
| 症狀（錯誤訊息原文） | |
| 問題卡分類（11.3.x） | |
| 診斷步驟與輸出（已遮蔽） | |
| 根因 | |
| 解決方法 | |
| 驗證結果 | |
| 預防措施 | |
| 是否更新規範或 preset（PR） | |

#### 18.9.8 附錄 8：版本升級與回復檢查清單

- [ ] 已閱讀 release notes 與 Platform Support 變更。
- [ ] 已確認新版 `min/max_openshell_version`。
- [ ] 測試主機演練（12.4）通過。
- [ ] 12.2 盤點、`backup-all`、獨立備份、`policy get` 匯出完成。
- [ ] 回復計畫（12.6）已填寫並指定決策者。
- [ ] 以固定 tag 執行已審查的安裝程式。
- [ ] `upgrade-sandboxes --check` 結束碼 0。
- [ ] 12.9 升級後驗收全部通過；若不通過，依回復計畫執行。
- [ ] 維護紀錄表（12.10）已更新。

#### 18.9.9 附錄 9：企業使用規範檢查清單

- [ ] 我只在核准的個人主機上、以核准版本使用 NemoClaw。
- [ ] 我沒有把生產環境憑證、客戶個資、未授權原始資料或機密文件提供給外部模型服務。
- [ ] 我的 API Key 來自密碼庫，沒有貼在對話、Prompt、文件或沙盒設定檔中。
- [ ] 我只使用 Restricted 層與核准的 preset；新目的地都有申請單。
- [ ] 我沒有在 `openshell term` 使用全部核准，也沒有核准未申請的目的地。
- [ ] 我沒有用 `docker exec` 操作沙盒，也沒有單獨升級 OpenShell 或在沙盒內更新 Agent。
- [ ] 我提交的 AI 參與 PR 都附交付報告，並已親自閱讀完整 diff。
- [ ] 我沒有停用或刪除既有測試。
- [ ] 發現異常時，我知道依 13.9 通報。
- [ ] 主機停用前，我會撤銷上游憑證（12.8）。

### 18.10 企業自訂審查工具原始碼

以下 5 支工具皆為 🏢 本手冊自行撰寫（不是 NVIDIA 官方工具），✅ 已在撰寫環境（Python 3.12.8、PyYAML 6.0.3、Git 2.45.2）以合成資料實測。授權依企業內部規範使用。

#### 18.10.1 nemoclaw-policy-lint.py

用途：靜態檢查自訂 preset 與整份 policy（6.16）。需要 `python3 -m pip install pyyaml`。

```python
#!/usr/bin/env python3
"""nemoclaw-policy-lint.py — 企業自訂檢查：NemoClaw 自訂 preset 與整份 OpenShell policy 的審查輔助工具。

不是 NVIDIA 官方工具。規則依 NemoClaw v0.0.139 文件（Create Custom Policy Presets、
Network Policies、Security Best Practices）整理，並加上本手冊的企業收斂規則。
它只做靜態檢查，不連線、不呼叫 nemoclaw／openshell。

用法：
  python3 nemoclaw-policy-lint.py preset  my-api.yaml [...]
  python3 nemoclaw-policy-lint.py policy  current-policy.yaml
結束碼：0＝無 ERROR；1＝有 ERROR；2＝用法或檔案錯誤。
"""
import re
import sys

try:
    import yaml
except ImportError:
    print("需要 PyYAML：python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)

MAINTAINED = {
    "brave", "brew", "brew-balanced", "claude-code", "discord", "github", "gmail",
    "huggingface", "jira", "local-inference", "local-memory", "npm", "openclaw-pricing",
    "outlook", "personal-open-internet", "public-reference", "pypi", "slack", "tavily",
    "teams", "telegram", "weather", "wechat", "whatsapp",
}
RESERVED_KEYS = {"npm_yarn", "personal_open_internet"}
RFC1123 = re.compile(r"^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$")
CATCH_ALL = {"*", "0.0.0.0", "0.0.0.0/0", "::", "::/0", "**"}
WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}
BROAD_BINARIES = {"/**", "/usr/bin/*", "/usr/bin/**", "/usr/local/bin/*", "/usr/local/bin/**", "/bin/*"}
INTERPRETER = re.compile(r"/(python3?[^/]*|node|bash|sh|curl|wget)$")
SECRET = re.compile(
    r"(nvapi-[A-Za-z0-9_-]{8,}|sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|"
    r"xox[abp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|Bearer\s+[A-Za-z0-9._-]{16,})"
)

findings = []


def report(level, rule, where, msg):
    findings.append((level, rule, where, msg))


def walk_strings(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_strings(v, f"{path}.{k}" if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def check_endpoint(where, ep):
    host = str(ep.get("host", ""))
    if not host:
        report("ERROR", "N03", where, "endpoint 缺少 host")
    elif host in CATCH_ALL or "/" in host:
        report("ERROR", "N03", where, f"host '{host}' 是全開或 CIDR 目的地，官方會拒絕")
    elif host.startswith("*.") and host.count(".") < 2:
        report("ERROR", "N03", where, f"host '{host}' 萬用字元範圍過大（只到頂級網域）")
    if "allowed_ips" in ep and host != "host.openshell.internal":
        report("ERROR", "N04", where, "自訂 preset 不得宣告 allowed_ips（改用 --trusted-private-host）")
    if ep.get("tls") == "skip":
        report("WARN", "N14", where, "tls: skip 會關閉 L7 檢查，需附 Raw TLS Passthrough 核准紀錄")
    protocol = ep.get("protocol")
    if protocol is None:
        report("WARN", "N06", where, f"'{host}' 沒有 protocol（L4-only，access={ep.get('access')}）；只看主機與程式，不檢查方法與路徑")
        return
    if ep.get("enforcement") != "enforce":
        report("ERROR", "N07", where, f"'{host}' 有 protocol 但未明確寫 enforcement: enforce")
    rules = ep.get("rules") or []
    if not rules and not ep.get("access"):
        report("ERROR", "N07", where, f"'{host}' 有 protocol 但沒有 rules")
    for j, r in enumerate(rules):
        allow = (r or {}).get("allow") or {}
        method = str(allow.get("method", "")).upper()
        path = str(allow.get("path", ""))
        rw = f"{where}.rules[{j}]"
        if method == "*":
            report("ERROR", "N08", rw, f"'{host}' method '*' 等於允許所有方法")
        elif method in {"PUT", "PATCH", "DELETE"} and path in {"/**", "/*", "**"}:
            report("ERROR", "N08", rw, f"'{host}' {method} {path}：寫入／刪除方法不可配全路徑")
        elif method == "POST" and path in {"/**", "**"}:
            report("WARN", "N08", rw, f"'{host}' POST /**：請收斂到實際 API 路徑")


def check_policies(where_root, policies):
    if not isinstance(policies, dict) or not policies:
        report("ERROR", "N05", where_root, "缺少 network_policies 或內容為空")
        return
    for key, pol in policies.items():
        where = f"{where_root}.{key}"
        if key in RESERVED_KEYS:
            report("ERROR", "N02", where, f"'{key}' 是官方保留鍵")
        pol = pol or {}
        bins = pol.get("binaries") or []
        if not bins:
            report("WARN", "N05", where, "沒有 binaries：此規則不授權任何程式，請求仍會失敗")
        for b in bins:
            p = str((b or {}).get("path", ""))
            if p in BROAD_BINARIES:
                report("ERROR", "N10", where, f"binary '{p}' 範圍過大")
            elif INTERPRETER.search(p.rstrip("*")):
                report("WARN", "N10", where, f"binary '{p}' 是直譯器或通用下載工具，等於沙盒內任何腳本都能用")
        for i, ep in enumerate(pol.get("endpoints") or []):
            check_endpoint(f"{where}.endpoints[{i}]", ep or {})


def lint(mode, path):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        doc = yaml.safe_load(text) or {}
    except (OSError, yaml.YAMLError) as exc:
        print(f"{path}: 無法讀取或解析：{exc}", file=sys.stderr)
        sys.exit(2)
    for where, value in walk_strings(doc):
        if SECRET.search(value):
            report("ERROR", "N11", where, "疑似明文憑證；改用 OpenShell provider／placeholder")
    if "[STRIPPED_BY_MIGRATION]" in text:
        report("ERROR", "N12", path, "仍有 [STRIPPED_BY_MIGRATION]，不可直接 openshell policy set")
    if mode == "preset":
        meta = doc.get("preset") or {}
        name = str(meta.get("name", ""))
        if not RFC1123.match(name):
            report("ERROR", "N01", "preset.name", f"'{name}' 不是小寫 RFC 1123 label")
        elif name in MAINTAINED:
            report("ERROR", "N01", "preset.name", f"'{name}' 與官方維護的 preset 同名")
        if not meta.get("description"):
            report("WARN", "N01", "preset.description", "缺少 description（審查與 policy list 時難以辨識）")
    else:
        if "preset" in doc:
            report("ERROR", "N13", path, "openshell policy set 不接受 preset 格式檔")
        if "version" not in doc:
            report("ERROR", "N13", path, "整份 policy 缺少 version")
        if "managed_inference" not in (doc.get("network_policies") or {}):
            report("ERROR", "N13", path, "整份替換會移除 managed_inference（推論路由會中斷）")
    check_policies("network_policies", doc.get("network_policies"))


def main(argv):
    if len(argv) < 3 or argv[1] not in {"preset", "policy"}:
        print(__doc__, file=sys.stderr)
        return 2
    for path in argv[2:]:
        before = len(findings)
        lint(argv[1], path)
        for level, rule, where, msg in findings[before:]:
            print(f"{level:5} {rule} {path} {where}: {msg}")
    errors = sum(1 for f in findings if f[0] == "ERROR")
    warns = sum(1 for f in findings if f[0] == "WARN")
    print(f"結果：{errors} ERROR，{warns} WARN")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

#### 18.10.2 check-change-report.py

用途：比對 AI 交付報告與實際 Git 變更（7.10）。

```python
#!/usr/bin/env python3
"""check-change-report.py — 企業自訂檢查：比對 AI Agent 交付報告與實際 Git 變更。

AI 說「我改了這些檔案、測試都通過」不是證據。本工具檢查：
  UNREPORTED  實際有變更、報告卻沒列出的檔案（最危險：沒人審）
  PHANTOM     報告列出、實際沒有變更的檔案（報告不可信）
  NOEVIDENCE  「測試結果」表沒有任何指令與結束碼
  TESTFAIL    測試結果有非 0 結束碼
  FORBIDDEN   變更碰到禁止路徑（預設：.env*、*.pem、*.key、正式環境設定）

報告格式（Prompt 範本要求 Agent 輸出）：
  ## 修改清單          表格第一欄為檔案路徑
  ## 測試結果          表格欄位：指令｜結束碼｜摘要
用法：
  python3 check-change-report.py REPORT.md [BASE_REF]   （BASE_REF 預設 origin/main）
結束碼：0＝通過；1＝有問題；2＝用法錯誤。
"""
import fnmatch
import re
import subprocess
import sys

FORBIDDEN = [".env", ".env.*", "*.pem", "*.key", "*application-prod*.yml", "*application-prod*.properties"]


def section_rows(text, title):
    rows, inside = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line[3:].strip().startswith(title)
            continue
        if inside and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and not re.fullmatch(r":?-{3,}:?", cells[0]) and cells[0] not in {"檔案", "指令"}:
                rows.append(cells)
    return rows


def git_changed(base):
    def run(*args):
        out = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
        if out.returncode != 0:
            print(out.stderr.strip(), file=sys.stderr)
            sys.exit(2)
        return {l.strip() for l in out.stdout.splitlines() if l.strip()}
    changed = run("diff", "--name-only", f"{base}...HEAD")
    changed |= run("diff", "--name-only")              # 未 commit 的修改
    changed |= run("ls-files", "--others", "--exclude-standard")  # 新增未追蹤
    return changed


def main(argv):
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    base = argv[2] if len(argv) > 2 else "origin/main"
    with open(argv[1], encoding="utf-8") as fh:
        text = fh.read()
    reported = {r[0].strip("`") for r in section_rows(text, "修改清單") if r[0]}
    report_path = argv[1].replace("\\", "/").lstrip("./")
    actual = {f for f in git_changed(base) if f != report_path and not f.startswith(".ai-reports/")}
    problems = []
    for f in sorted(actual - reported):
        problems.append(("UNREPORTED", f, "實際有變更，報告未列出"))
    for f in sorted(reported - actual):
        problems.append(("PHANTOM", f, "報告列出，但 Git 沒有這個變更"))
    for f in sorted(actual):
        name = f.rsplit("/", 1)[-1]
        if any(fnmatch.fnmatch(name, p) or fnmatch.fnmatch(f, p) for p in FORBIDDEN):
            problems.append(("FORBIDDEN", f, "變更碰到禁止路徑"))
    tests = [r for r in section_rows(text, "測試結果") if len(r) >= 2 and r[0]]
    if not tests:
        problems.append(("NOEVIDENCE", "-", "測試結果表沒有任何指令與結束碼"))
    for r in tests:
        code = r[1].strip("`")
        if not re.fullmatch(r"-?\d+", code):
            problems.append(("NOEVIDENCE", r[0], f"結束碼 '{r[1]}' 不是數字"))
        elif code != "0":
            problems.append(("TESTFAIL", r[0], f"結束碼 {code}"))
    for kind, f, msg in problems:
        print(f"{kind:10} {f}: {msg}")
    print(f"報告列出 {len(reported)} 檔、實際變更 {len(actual)} 檔、測試 {len(tests)} 筆、問題 {len(problems)} 項")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

#### 18.10.3 check-layering.py

用途：Java 專案 Hexagonal 依賴方向快篩（7.8）。

```python
#!/usr/bin/env python3
"""check-layering.py — 企業自訂檢查：Java 專案 Clean／Hexagonal 依賴方向快篩。

套件命名慣例（依專案調整 LAYERS）：
  <root>.domain..        核心：實體、值物件、領域服務、Port 介面
  <root>.application..   Use Case：協調 domain、呼叫 Port
  <root>.adapter..       轉接：Web Controller、JPA Repository、外部 API Client
規則：
  L01 domain 不得 import application／adapter
  L02 domain 不得 import 框架（Spring、JPA、Jackson、Servlet）
  L03 application 不得 import adapter
  L04 application 不得 import Web／持久化框架（允許 jakarta.transaction 等可另行調整）
用法：python3 check-layering.py src/main/java com.example.order
結束碼：0＝無違規；1＝有違規；2＝用法錯誤。
這是 CI 前的快篩，正式守門請用 ArchUnit（見手冊 7.8）。
"""
import pathlib
import re
import sys

IMPORT = re.compile(r"^\s*import\s+(static\s+)?([\w.]+)")
FRAMEWORK = ("org.springframework.", "jakarta.persistence.", "javax.persistence.",
             "com.fasterxml.jackson.", "jakarta.servlet.", "org.hibernate.")
WEB_PERSIST = ("org.springframework.web.", "org.springframework.data.", "jakarta.persistence.",
               "javax.persistence.", "jakarta.servlet.", "org.hibernate.")


def layer_of(pkg, root):
    rest = pkg[len(root) + 1:] if pkg.startswith(root + ".") else ""
    head = rest.split(".", 1)[0]
    return head if head in {"domain", "application", "adapter"} else None


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    src, root = pathlib.Path(argv[1]), argv[2]
    violations = 0
    for java in sorted(src.rglob("*.java")):
        text = java.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^\s*package\s+([\w.]+);", text, re.M)
        if not m:
            continue
        layer = layer_of(m.group(1), root)
        if layer not in {"domain", "application"}:
            continue
        for no, line in enumerate(text.splitlines(), 1):
            im = IMPORT.match(line)
            if not im:
                continue
            target = im.group(2)
            tl = layer_of(target, root)
            rule = None
            if layer == "domain" and tl in {"application", "adapter"}:
                rule = "L01"
            elif layer == "domain" and target.startswith(FRAMEWORK):
                rule = "L02"
            elif layer == "application" and tl == "adapter":
                rule = "L03"
            elif layer == "application" and target.startswith(WEB_PERSIST):
                rule = "L04"
            if rule:
                violations += 1
                print(f"{rule} {java.as_posix()}:{no}: {layer} → {target}")
    print(f"結果：{violations} 項違規")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

#### 18.10.4 check-evidence.py

用途：逆向工程文件的事實／推測引用檢查（8.6）。

```python
#!/usr/bin/env python3
"""check-evidence.py — 企業自訂檢查：逆向工程文件的「事實／推測」引用檢查。

Prompt 範本要求 Agent 在文件中這樣標示：
  - [事實] 訂單金額超過 50,000 需主管覆核。（來源：src/main/java/x/OrderService.java:88-97）
  - [推測] 狀態 9 可能代表人工結案。（依據：OrderStatus.java:12 只有常數、無註解；待確認 Q-07）
規則：
  MISSING   [事實] 沒有「來源：路徑:行號」
  BADFILE   來源檔案不存在
  BADLINE   行號超出檔案長度，或起訖顛倒
  NOBASIS   [推測] 沒有「依據：」或沒有待確認編號（Q-xx）
  UNTAGGED  條列看起來是結論（含「必須／會／一律」）卻沒有標示 [事實] 或 [推測]
用法：python3 check-evidence.py docs/SDD.md <原始碼根目錄>
結束碼：0＝通過；1＝有問題；2＝用法錯誤。
"""
import pathlib
import re
import sys

CITE = re.compile(r"來源：\s*([\w./\\-]+?):(\d+)(?:-(\d+))?\s*[）)]")
CLAIM_WORDS = ("必須", "一律", "會自動", "禁止", "只能")


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    doc, root = pathlib.Path(argv[1]), pathlib.Path(argv[2])
    problems = 0
    facts = guesses = 0
    for no, line in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if not s.startswith(("-", "*", "|")):
            continue
        where = f"{doc.as_posix()}:{no}"
        if "[事實]" in s:
            facts += 1
            cites = CITE.findall(s)
            if not cites:
                print(f"MISSING  {where}: [事實] 沒有來源")
                problems += 1
            for path, start, end in cites:
                target = root / path
                if not target.is_file():
                    print(f"BADFILE  {where}: {path} 不存在")
                    problems += 1
                    continue
                total = len(target.read_text(encoding="utf-8", errors="replace").splitlines())
                a, b = int(start), int(end or start)
                if a < 1 or b > total or a > b:
                    print(f"BADLINE  {where}: {path}:{start}{'-' + end if end else ''} 超出 1–{total}")
                    problems += 1
        elif "[推測]" in s:
            guesses += 1
            if "依據：" not in s or not re.search(r"Q-\d+", s):
                print(f"NOBASIS  {where}: [推測] 需要「依據：」與待確認編號 Q-xx")
                problems += 1
        elif any(w in s for w in CLAIM_WORDS) and not s.startswith("|"):
            print(f"UNTAGGED {where}: 疑似結論但未標示 [事實]／[推測]")
            problems += 1
    print(f"結果：事實 {facts} 條、推測 {guesses} 條、問題 {problems} 項")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

#### 18.10.5 check-test-weakening.py

用途：找出 AI 變更中刪除或弱化測試的跡象（13.8）。只用 Python 標準函式庫與 Git。

```python
#!/usr/bin/env python3
"""check-test-weakening.py — 企業自訂檢查：找出 AI 變更中「刪除或弱化測試」的跡象。

Agent 想讓 CI 變綠時，最便宜的做法是改測試而不是改程式。本工具比對 BASE 與工作目錄：
  DELETED    測試檔被刪除或改名到非測試路徑
  FEWERTESTS 測試檔中的測試案例數減少（@Test、@ParameterizedTest、it(、test(）
  FEWERASSERT 測試檔中的斷言數減少（assert*、assertThat、expect(、verify(）
  DISABLED   新增停用標記（@Disabled、@Ignore、.skip(、xit(、xdescribe(、.only(）
  SKIPBUILD  建置設定新增略過測試（skipTests、maven.test.skip、testFailureIgnore、--passWithNoTests）

它只看文字差異，不執行測試；結果是「需要人看」的清單，不是定罪。
用法：
  python3 check-test-weakening.py [BASE_REF]   （BASE_REF 預設 origin/main；在 repo 根目錄執行）
結束碼：0＝沒有發現；1＝有發現；2＝用法或 Git 錯誤。
"""
import re
import subprocess
import sys

TEST_PATH = re.compile(r"(^|/)(src/test/|tests?/|__tests__/)|(Test|Tests|IT)\.java$|\.(test|spec)\.[cm]?[jt]sx?$")
BUILD_FILE = re.compile(r"(^|/)(pom\.xml|build\.gradle(\.kts)?|package\.json|vitest\.config\.[cm]?[jt]s|jest\.config\.[cm]?[jt]s)$")
CASE = re.compile(r"@(Test|ParameterizedTest|RepeatedTest)\b|(^|[^\w.])(it|test)\s*\(")
ASSERT = re.compile(r"\bassert\w*\s*\(|\bassertThat\s*\(|\bexpect\s*\(|\bverify\s*\(")
DISABLE = re.compile(r"@Disabled\b|@Ignore\b|\.(skip|only)\s*\(|\bx(it|describe|test)\s*\(")
SKIP = re.compile(r"skipTests|maven\.test\.skip|testFailureIgnore|passWithNoTests|-x\s+test\b")


def git(*args, check=True):
    out = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
    if check and out.returncode != 0:
        print(out.stderr.strip(), file=sys.stderr)
        sys.exit(2)
    return out


def old_text(base, path):
    out = git("show", f"{base}:{path}", check=False)
    return out.stdout if out.returncode == 0 else ""


def new_text(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return ""


def count(pattern, text, per_line=False):
    lines = [l for l in text.splitlines() if not l.lstrip().startswith(("//", "*", "#"))]
    if per_line:
        return sum(1 for l in lines if pattern.search(l))
    return sum(len(pattern.findall(l)) for l in lines)


# (代號, 樣式, 以行計數, 增加才算問題, 訊息)；前三條只看測試檔，最後一條只看建置設定
RULES = [
    ("FEWERTESTS", CASE, False, False, "測試案例"),
    ("FEWERASSERT", ASSERT, False, False, "斷言"),
    ("DISABLED", DISABLE, False, True, "停用標記"),
]
BUILD_RULE = ("SKIPBUILD", SKIP, True, True, "略過測試設定")


def compare(rules, path, before, after):
    found = []
    for code, pattern, per_line, worse_if_more, label in rules:
        b, a = count(pattern, before, per_line), count(pattern, after, per_line)
        if (a > b) if worse_if_more else (a < b):
            found.append((code, path, f"{label} {b} → {a}"))
    return found


def inspect(base, row):
    parts = row.split("\t")
    kind, old_path, path = parts[0][0], parts[1], parts[-1]
    if kind == "D" and TEST_PATH.search(old_path):
        return [("DELETED", old_path, "測試檔被刪除")]
    if kind == "R" and TEST_PATH.search(old_path) and not TEST_PATH.search(path):
        return [("DELETED", old_path, f"測試檔改名到非測試路徑 {path}")]
    before, after = old_text(base, old_path), new_text(path)
    if TEST_PATH.search(path):
        return compare(RULES, path, before, after)
    if BUILD_FILE.search(path):
        return compare([BUILD_RULE], path, before, after)
    return []


def main(argv):
    base = argv[1] if len(argv) > 1 else "origin/main"
    git("rev-parse", "--verify", base)
    status = git("diff", "--name-status", "-M", base).stdout.splitlines()
    status += [f"A\t{p}" for p in git("ls-files", "--others", "--exclude-standard").stdout.splitlines()]
    findings = [f for row in status for f in inspect(base, row)]
    for kind, path, msg in findings:
        print(f"{kind:11} {path}: {msg}")
    print(f"檢查 {len(status)} 個變更檔案，發現 {len(findings)} 項")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

### 18.11 上游變更追蹤表（v0.0.139 → `main`＠`bafe6cc`）

`main` 領先 v0.0.139 共 18 個 commit，都還沒有發布。下表說明每一項對 v0.0.139 使用者的意義，以及手冊在哪裡說明。追蹤方法：`gh api repos/NVIDIA/NemoClaw/compare/v0.0.139...main --jq '.commits[].commit.message | split("\n")[0]'`。

| PR | 類別 | 內容 | 對 v0.0.139 使用者的意義 | 手冊章節 |
|---|---|---|---|---|
| #13635、#13763 | E2E | 讓受信任的 E2E 控制器能驗證 OpenShell 0.1.3／0.1.5 候選版 | 無直接影響；是 0.1.5 遷移的前置工作 | 12.11 |
| #13646 | agent | 管線輸入改由主機端計時（30 秒或 `--timeout`，上限 4 MiB） | v0.0.139 上，不關閉的管線會讓指令卡住 | 5.6 |
| #13567 | onboard | 不支援的 `--dcode-auto-approval thread-opt-in` 在 onboarding 前就拒絕 | v0.0.139 會半途才失敗 | 5.6 |
| #13648 | 文件 | 說明原生 Provider 沙盒的 `liveRoute`／`routeDrift` 為 `null` | 行為在 v0.0.139 已存在，監控不要誤報 | 5.9、17.19 |
| #13134 | sandbox | `status` 與 recovery 失敗時會顯示 Gateway 名稱或埠號 | v0.0.139 的錯誤訊息較難判斷是哪個 Gateway | 11.3.4 |
| #13748 | inference | Ollama 回報 0 MB 可用 GPU 記憶體時，不再誤當成整張 VRAM 可用 | GPU 被占滿時可能選到放不下的模型 | 3.2 |
| #13137 | inference | 託管 vLLM 的 Key 改為原子寫入，中斷不再留下空檔 | v0.0.139 中斷後可能留下壞的 Key 檔，之後 onboarding 一直失敗 | 11.3.7 |
| #13237 | inference | 只換模型時，從沙盒內驗證沿用的 HTTPS adapter 路由 | `inference set` 只換模型時，驗證可能誤判 | 5.7 |
| #13591 | dcode | 編輯核准卡顯示完整路徑 | v0.0.139 只顯示檔名，核准前要自己確認路徑 | 6.18 |
| #13620 | hermes | 沒有搜尋 Provider 時，不再提供 `web_search`／`web_extract` | v0.0.139 的 Hermes 會嘗試匿名搜尋、被政策擋下，回覆可能是空的或沒有依據 | 6.15 |
| #13696 | hermes | 下載 Hermes 原始碼封存遇到 HTTP 429 時，退避時間拉長到 60／120 秒 | 建置映像檔時偶發 429 失敗，重跑即可 | 11.3.3 |
| #12813 | config | Hermes Dashboard 停用且埠號被重新配置時，`config export` 也能匯出 | v0.0.139 的 `config export` 對這種沙盒會失敗 | 12.11 |
| #13630、#13446、#13645 | uninstall | 無 systemd user manager 的 Linux 能正確移除 unit；多 Gateway 清理不再誤判預設埠；Docker 沒在跑時給出正確提示 | v0.0.139 解除安裝可能留下殘餘或給出誤導的訊息 | 12.8 |
| #13772 | 文件 | 改用核准過的遙測說明文字 | 行為不變，仍以 `NEMOCLAW_DISABLE_TELEMETRY=1` 停用 | 4.4、17.16 |
| #13753 | CI | 調整專案 CI 設定 | 無 | — |

> ✅ **建議**：每次核准新版本前，用同樣的方式產生「上一個核准版本 → 新版本」的追蹤表，逐列判斷影響，存進維護紀錄（12.10）。

### 18.12 名詞表

| 名詞 | 說明 |
|---|---|
| Agent Runtime | 沙盒內執行的 Agent 程式（OpenClaw、Hermes、`dcode`） |
| Blueprint | NemoClaw 的版本化沙盒定義：映像檔 digest、政策、推理 profile |
| `dcode` | LangChain Deep Agents Code 的執行檔 |
| Express 安裝 | DGX Spark、DGX Station、WSL 上的推薦預設安裝模式 |
| Gateway（OpenShell） | 主機上的 OpenShell 控制程序：憑證、政策、推理代理、生命週期 |
| Gateway（Agent） | 沙盒內 OpenClaw／Hermes 自己的 Gateway（Dashboard、API） |
| `inference.local` | OpenShell 0.0.x 的共享推理路由虛擬主機名 |
| `lkg` | last known good，安裝程式預設安裝的標籤 |
| onboarding | `nemoclaw onboard` 的引導式初始化流程 |
| Placeholder | 沙盒內代替真實憑證的佔位值，於核准出口替換 |
| Preset | 可套用到沙盒的政策片段（YAML，`preset:` 開頭） |
| Provider | OpenShell 中的外部服務憑證與存取定義 |
| Sandbox-first 文法 | `nemoclaw <沙盒名稱> <動作>` |
| Tier | 政策層級：Restricted、Balanced、Open、Personal |
| 附掛式 Provider | 附掛到沙盒、限制主機／路徑／程式的原生推理 Provider |
| ASI | OWASP Top 10 for Agentic Applications 的條目代號（ASI01～ASI10） |
| CSAF | Common Security Advisory Framework，機器可讀的安全公告格式；NVIDIA 公告以此格式發布 |
| `liveRoute`／`recordedRoute` | `status --json` 中「目前共享路由」與「沙盒紀錄的路由」；原生附掛 Provider 的 `liveRoute` 永遠是 `null` |
| PSIRT | Product Security Incident Response Team，廠商的產品資安事件處理小組 |

### 18.13 版本紀錄

| 版本 | 日期 | 變更 |
|---|---|---|
| 1.0 | 2026-10-27 | 初版。基準 NemoClaw v0.0.139（`a08ae7a`）／OpenShell 0.0.116；`main` 追蹤至 `bafe6cc`。附 4 支已實測的審查工具與 ArchUnit 範例 |
| 1.1 | 2026-10-27 | 同一基準再核對（無新 tag；`lkg` 仍為 v0.0.137；`main` 仍為 `bafe6cc`）。新增：6.17 安全公告與弱點修補（Bulletin 5872、版本下限腳本）、6.18 OWASP Agentic Top 10 對照、12.11 OpenShell 0.1.5 遷移預警、18.11 上游變更追蹤表、第 5 支審查工具 `check-test-weakening.py`；第 3、5、11～15、17 章的規範補上範例與驗證方法；FAQ 新增 17.17～17.19 並為每題加入自我驗證 |

---

## 新進成員快速檢查清單（Checklist）

第一週照這張表做，每一項都做完才開始在專案中使用 AI Agent。

**第 1 天：理解**：

- [ ] 讀完「重要聲明」與第 1 章，能說出 NemoClaw 與 OpenShell 的差別。
- [ ] 讀完 13.11 允許／禁止／需經核准表。
- [ ] 知道自己專案的資料分級（13.6），以及能不能用外部推理服務。

**第 2 天：環境**：

- [ ] 提出環境申請（13.2），取得個人主機。
- [ ] 跑 3.9 預檢腳本，結束碼 0。
- [ ] 依 4.3 下載並比對安裝程式，以固定 tag 安裝。
- [ ] `~/.bashrc` 加入 `export NEMOCLAW_DISABLE_TELEMETRY=1`。

**第 3 天：驗收**：

- [ ] 以 Restricted 層建立 Deep Agents 沙盒。
- [ ] 完成 4.9 測試請求與 4.10 控制有效性驗證。
- [ ] 套用標準唯讀 preset，完成 6.12 V1～V6。
- [ ] 在 `openshell term` 練習拒絕一個未核准請求。

**第 4 天：開發流程**：

- [ ] 完成 16.1 演練 0 與 16.2 案例 A 的 A1～A7。
- [ ] 親手跑一次 `check-change-report.py`、`check-layering.py`、`check-test-weakening.py`，看懂輸出。
- [ ] 找出講師在案例中埋入的至少一個錯誤。

**第 5 天：維運與收尾**：

- [ ] 練習 `stop`、`start`、`logs`、`doctor`、`download` 備份。
- [ ] 讀 11.3 的 12 張問題卡，知道遇到 403 與 `unauthorized` 時先看哪裡。
- [ ] 讀 6.17、6.18，知道去哪裡查安全公告，以及 OWASP Agentic Top 10 中哪些風險要靠人補強。
- [ ] 簽署 18.9.9 企業使用規範檢查清單。

**每天開工**：

- [ ] `nemoclaw status`、`nemoclaw <名稱> status` 正常（或直接跑 11.2 的 `nemoclaw-daily.sh`，結束碼 0）。
- [ ] `nemoclaw <名稱> policy list` 沒有多出未核准的 preset。
- [ ] 寫入 preset 用完就移除。

