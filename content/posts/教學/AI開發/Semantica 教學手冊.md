+++
date = '2026-08-20T13:57:07+08:00'
draft = false
title = 'Semantica 教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# Semantica 教學手冊

> **Semantica —— AI Agent 的 Context Graph、Knowledge Graph 與 Decision Intelligence 基礎設施層完整導入指南**
> 適用對象：資深 Software Architect、SA、Backend/Frontend Engineer、AI Agent 平台團隊、DevSecOps、Tech Lead、企業導入負責人
> 文件性質：企業內部「AI Agent Context / Knowledge Graph / Decision Intelligence / Provenance」基礎設施導入、開發與維運培訓教材
> 版本基準：`semantica-agi/semantica`（MIT License），研究基準為官方 GitHub `main` 分支與 `docs.getsemantica.ai`
> 　　　　　最新穩定版 **v0.6.5**（2026-08-11），研究/查證日期：2026-08-20
> 技術堆疊：Python ≥3.8、pip、可選 Neo4j/FalkorDB/Apache AGE/AWS Neptune（LPG）、內嵌 Oxigraph/Blazegraph/Jena/RDF4J/Anzo（RDF）、FAISS/Qdrant/Weaviate/Milvus/Pinecone/PgVector（Vector）、MIT License

---

## ⚠️ 重要聲明（請務必先讀）

1. **Semantica 是一個真實存在、仍在快速迭代中的開源專案。** 本手冊撰寫時已透過官方 GitHub Repository（`github.com/semantica-agi/semantica`）、官方文件站（`docs.getsemantica.ai`）與 PyPI（`pypi.org/project/semantica`）逐項查證，**並非虛構專案**。但 Semantica 平均每 3-6 週釋出一次 minor 版本（v0.4.0 → v0.6.5 僅約 4 個月），CLI 指令、Python API 簽章、設定鍵、目錄結構都可能隨版本演進調整。**任何指令、程式碼、路徑在正式導入前，務必以官方最新 `README.md`、`docs.getsemantica.ai`、`CHANGELOG`/Release Notes 與你實際安裝的版本為準**（例如執行 `semantica --help`、`python -c "import semantica; print(semantica.__version__)"` 逐一核對）。

2. **本手冊是彙整、重組、補充企業導入實務，而不是官方文件的翻譯。** 本書不逐字翻譯官方文件，而是依真實官方 README、`docs.getsemantica.ai` 各 Guide 頁面重新查證後，以繁體中文重新組織、延伸為企業教材，並大量補充 Scenario／Example／比較表／Checklist／企業導入建議（三大情境：Web Application 開發、逆向工程、Framework Upgrade，皆為本手冊原創的企業導入設計，非 Semantica 官方案例）。

3. **本手冊採用五層 Provenance 標示法，請務必先理解這套標示法，它貫穿全書每一個具體事實與主張：**

   | 標示 | 意義 | 使用時機 |
   |---|---|---|
   | **官方已實作** | 官方 README／`docs.getsemantica.ai`／GitHub Release Notes 明確確認已出貨的功能 | 有明確官方文件出處可查，本手冊會附上頁面名稱 |
   | **Source-confirmed** | 官方文件僅簡略提及或未提及，需以原始碼／`--help` 輸出為準 | 用於官方文件覆蓋不到、但可合理推斷存在的細節 |
   | **Roadmap/Issue（規劃中）** | 官方 Roadmap 或 Issue/PR 討論中，尚未 merge/發布 | 用於區分「已規劃」與「已出貨」，避免混淆 |
   | **建議架構** | 本手冊作者針對企業導入的建議，**非 Semantica 官方功能** | 用於企業落地建議、原創比較表、原創案例（例如三大情境、銀行案例、K8s HA 設計、Observability 整合、AI Agent Team 分工，皆屬此類） |
   | **推測/Hypothesis** | 無法從任何層級來源確認，僅為合理推論 | 用於誠實標示研究缺口，提醒讀者自行以官方最新版本查證 |

   凡是標成「建議架構」或「推測/Hypothesis」的內容，**都不是 Semantica 的官方功能或官方保證**，請勿在企業內部溝通或對外簡報時誤植為官方承諾。

4. **Semantica 不是什麼**：它不是 LangChain、LlamaIndex 的替代品，不是向量資料庫（Vector Database）的替代品，不是 LLM 本身，也不是 Agent Framework（例如 Agno、CrewAI）的替代品。**Semantica 是坐落在這些元件之下的 Context / Knowledge Graph / Decision Intelligence / Provenance / Reasoning / Accountability 基礎設施層**，詳見第 2 章。

5. **技術能力 ≠ 法規合規聲明**：本手冊第 39 章的銀行案例會示範 Semantica 如何提升「可追溯性」與「可問責性」，但**不代表安裝 Semantica 就等於符合 SOX、Basel III、個資法或其他金融/醫療法規**。合規與否仍需由企業法遵、稽核與法務部門實質認定，Semantica 官方文件本身也在 Provenance Guide 中明確指出：「Provenance records faithfully document where data came from, but do not verify source accuracy」（忠實記錄資料來源，不代表驗證資料本身正確）（官方已實作，`docs.getsemantica.ai/guides/provenance`）。

6. **第 19、20、21、39 章的企業案例聲明**：本手冊中出現的 Web Application／Legacy Java／銀行案例（例如 Vue3 + Spring Boot 4 網銀系統、Legacy 保單核保系統、Spring Boot 3→4 升版案例）均為**教學示範用途之虛構情境**，用於示範 Semantica 與既有企業技術堆疊（Java 25、Spring Boot 4.x、Vue3、PostgreSQL 等）的整合模式，並非真實客戶專案。涉及既有框架的深入機制，請參閱本 Repository 既有手冊（若存在對應路徑）。

7. **MIT License 授權範圍聲明**：Semantica 採 MIT License，本手冊對授權條款的說明僅供參考，實際權利義務請以官方 `LICENSE` 檔案逐字內容為準，本手冊不構成法律意見。

8. **命名易混淆警示（企業溝通與檢索時務必注意）**：「Semantica」一詞在業界**至少對應三個互不相關的實體**，企業內部簡報、採購評估或網路搜尋時極易張冠李戴，請務必核對 Repository URL 是否為 `github.com/semantica-agi/semantica`：
   - **`ai-semantica.com`（"Semantica AI"）**：一個完全無關的 AI 品牌能見度／SEO 分析工具（追蹤品牌在 ChatGPT／Perplexity 等 AI 回答中的曝光度），自己也有一套名稱相同但用途完全不同的「MCP server」（工具如 `get_visibility_metrics`）。
   - **其他 GitHub 上同樣命名為 `semantica` 但非本專案分支的獨立 Repository**（例如 `Hawksight-AI/semantica`）：與 `semantica-agi/semantica` 沒有任何關聯，不可混用其文件或程式碼。
   - 本手冊全書所述的 Semantica，**專指且僅指** `github.com/semantica-agi/semantica`（首頁 `getsemantica.ai`，文件站 `docs.getsemantica.ai`，PyPI 套件名 `semantica`，維護者信箱網域 `getsemantica.ai`）（Source-confirmed，2026-08-20 查證）。

9. 官方權威來源與研究來源分級，請見附錄 A（Official References）與附錄 B（Research Sources）。

---

## 符號約定

### Provenance 五層標示

本文以括號文字直接標示於句末，例如「... (官方已實作，`docs.getsemantica.ai/guides/decision-intelligence`)」或「... (建議架構)」。標示意義同上表，全書一致使用，不再重複解釋。

### Mermaid 圖表慣例

- 所有架構圖、流程圖、序列圖均以 Mermaid 語法呈現，可直接在支援 Mermaid 的 Markdown 檢視器（GitHub、VS Code 外掛等）中渲染。
- 節點標籤若包含括號、冒號、斜線等特殊字元，一律以雙引號包住整個標籤（例如 `A["Context Graph (In-Memory)"]`），避免解析錯誤。
- 實線箭頭代表已從官方文件或原始碼確認的關係（官方已實作／Source-confirmed）；虛線箭頭代表本手冊依現有事實合理推論、但官方未逐一列點確認的路徑（建議架構），圖說明會另外標註。

### 程式碼區塊慣例

- 標示為「示意」或「非逐字官方範例」的程式碼區塊，是本手冊為了幫助理解而重新撰寫或改編的概念示範，**不是官方文件的逐字引用**，不可直接複製貼上當作生產環境設定。
- 未標示「示意」的程式碼區塊，是官方 README 或 `docs.getsemantica.ai` 中可查證的真實範例（會標明出處頁面）。
- Shell 指令一律以 ```bash 標示（同時適用 Linux/WSL2/macOS Bash 與 Windows Git Bash）；Windows PowerShell 專屬指令會另外以 ```powershell 標示。

### 章節固定小節

重要章節盡量包含以下小節：Scenario／Process／Example（具體案例）／AI Prompt 範例／本章 Checklist 與小結。

---

## 版本與相容性速查表

| 項目 | 值 | 來源標示 |
|---|---|---|
| Repository | `semantica-agi/semantica` | 官方已實作 |
| 專案定位（官方 Tagline） | "Graph-Native Infrastructure for Context and Accountable AI Systems" | 官方已實作 |
| 最新穩定版 | v0.6.5（2026-08-11） | 官方已實作 |
| License | MIT | 官方已實作 |
| 主要語言 | Python | 官方已實作 |
| Python 需求版本 | ≥3.8（官方 `pyproject.toml` 唯一明確版本下限） | 官方已實作 |
| 套件管理 | pip（`pip install semantica`） | 官方已實作 |
| CLI 執行檔 | `semantica`／`semantica-server`／`semantica-worker`／`semantica-explorer`／`semantica-mcp`（共 5 個，`pyproject.toml [project.scripts]` 逐一核對確認） | 官方已實作 |
| MCP Server | 獨立套件化（v0.5.0 起），stdio-based，12 個 tools（逐一核對名稱確認）＋ 官方文件提及的 read-only resources（本次查證未能獨立核對確切數量，見第 16.5 節備註） | 官方已實作（12 tools）／Source-confirmed（resources 數量） |
| 版本演進重點 | v0.3.0（首個穩定版）→ v0.4.0（bi-temporal + SHACL/SKOS + Datalog）→ v0.5.0（MCP Server 獨立套件化、Ontology Hub、Windsurf/Cline/Continue/VS Code 外掛）→ v0.5.1（Arrow/Feather 攝取、Docker/K8s Explorer 部署範本）→ v0.6.0（跨後端 SPARQL、Databricks/SQLite connector）→ v0.6.5（6 項安全性修補、新增 Altair Anzo RDF 後端） | 官方已實作，GitHub Releases（2026-08-20 重新逐版查證） |
| GitHub 星數／Forks | **9,593★／1,009 forks**（2026-08-20 直接以 GitHub API 查證，非快取頁面數字） | Source-confirmed |
| Repository 建立／最近更新 | 建立於 2025-06-25；最近一次 push 為 2026-08-19（查證前一日，屬持續積極維護中的專案） | Source-confirmed |
| 第三方採用佐證 | Hacker News「Show HN: Semantica」發佈串（2026-01-07）、GitHub Trending 收錄；用於佐證專案並非虛構但**非官方背書**，不構成企業採用建議 | Source-confirmed |
| Windows 官方支援 | 支援，但 `[all]` extras 在 v0.5.0 前有已知安裝失敗問題（v0.5.0 已修復），且需另裝 Microsoft Visual C++ Redistributable | 官方已實作，`docs.getsemantica.ai/installation` |
| Docker/K8s 部署範本 | v0.5.1 起提供 Knowledge Explorer 的 Docker/K8s/雲端部署範本 | 官方已實作（範圍限於 Explorer，非完整生產部署藍圖，見第 29 章） |
| Graph Store 後端 | LPG：Neo4j、FalkorDB、Apache AGE、AWS Neptune；RDF：內嵌 Oxigraph、Blazegraph、Apache Jena、Eclipse RDF4J、**Altair Anzo**（v0.6.5 新增，經 SPARQL） | 官方已實作 |
| Vector Store 後端 | FAISS、Qdrant、Weaviate、Milvus、Pinecone、PgVector、SQLite、in-memory | 官方已實作 |
| 原生 Agent Framework 整合 | Agno、CrewAI（first-class，`pip install semantica[agno]` / `[crewai]`） | 官方已實作 |
| 間接整合 | LangChain、LlamaIndex、AutoGen、OpenAI Agents（透過 REST API／MCP） | 官方已實作 |
| Editor/Agent Plugin | Claude Code、Cursor、Codex CLI、Windsurf、Cline、Continue、VS Code、**OpenClaw**（共 8 個，2026-08-20 重新核對確認官方清單為 8 個，先前版本手冊漏列 OpenClaw） | 官方已實作 |

---

## 目錄

> 目錄與子目錄皆為可點擊錨點連結，可直接跳轉至本文對應章節／小節。

- [1. 文件說明與如何使用本手冊](#1-文件說明與如何使用本手冊)
  - [1.1 這份手冊要解決什麼問題](#11-這份手冊要解決什麼問題)
  - [1.2 如何閱讀這份手冊](#12-如何閱讀這份手冊)
  - [1.3 與官方文件的差異](#13-與官方文件的差異)
  - [1.4 本章 Checklist 與小結](#14-本章-checklist-與小結)
- [2. Semantica 簡介與定位](#2-semantica-簡介與定位)
  - [2.1 官方定位](#21-官方定位)
  - [2.2 Semantica 不是什麼](#22-semantica-不是什麼)
  - [2.3 分層定位圖](#23-分層定位圖)
  - [2.4 與既有 AI 生態系的整合關係](#24-與既有-ai-生態系的整合關係)
  - [2.5 Scenario：企業第一次接觸 Semantica](#25-scenario企業第一次接觸-semantica)
  - [2.6 AI Prompt 範例（初次評估）](#26-ai-prompt-範例初次評估)
  - [2.7 本章 Checklist 與小結](#27-本章-checklist-與小結)
- [3. 核心概念總覽](#3-核心概念總覽)
  - [3.1 Context Graph vs Knowledge Graph：最容易搞混的一組](#31-context-graph-vs-knowledge-graph最容易搞混的一組)
  - [3.2 Semantica 如何整合這些概念](#32-semantica-如何整合這些概念)
  - [3.3 Scenario：選型決策](#33-scenario選型決策)
  - [3.4 本章 Checklist 與小結](#34-本章-checklist-與小結)
- [4. Architecture 深入解析](#4-architecture-深入解析)
  - [4.1 官方四層架構](#41-官方四層架構)
  - [4.2 企業級擴充架構圖（整合官方模組 + Master Prompt 要求的完整資料源清單）](#42-企業級擴充架構圖整合官方模組--master-prompt-要求的完整資料源清單)
  - [4.3 逐層解釋（企業導入視角）](#43-逐層解釋企業導入視角)
  - [4.4 官方核心設計原則](#44-官方核心設計原則)
  - [4.5 6 步驟 Quickstart Pipeline（官方已實作，`docs.getsemantica.ai/quickstart`）](#45-6-步驟-quickstart-pipeline官方已實作docsgetsemanticaaiquickstart)
  - [4.6 本章 Checklist 與小結](#46-本章-checklist-與小結)
- [5. Installation（安裝）](#5-installation安裝)
  - [5.1 前置需求](#51-前置需求)
  - [5.2 Windows 安裝（venv）](#52-windows-安裝venv)
  - [5.3 Linux / macOS 安裝（venv）](#53-linux--macos-安裝venv)
  - [5.4 使用 conda](#54-使用-conda)
  - [5.5 WSL2](#55-wsl2)
  - [5.6 Extras（依需求安裝的可選套件）](#56-extras依需求安裝的可選套件)
  - [5.7 Docker](#57-docker)
  - [5.8 Podman](#58-podman)
  - [5.9 Kubernetes（概覽，完整生產部署見第 29 章）](#59-kubernetes概覽完整生產部署見第-29-章)
  - [5.10 驗證安裝](#510-驗證安裝)
  - [5.11 企業推薦安裝方式對照表](#511-企業推薦安裝方式對照表)
  - [5.12 Troubleshooting 速查（完整版見第 42 章）](#512-troubleshooting-速查完整版見第-42-章)
  - [5.13 本章 Checklist 與小結](#513-本章-checklist-與小結)
- [6. Configuration（設定）](#6-configuration設定)
  - [6.1 官方已確認的環境變數](#61-官方已確認的環境變數)
  - [6.2 Provenance 儲存設定](#62-provenance-儲存設定)
  - [6.3 LLM Provider 設定](#63-llm-provider-設定)
  - [6.4 Graph / Vector Store Backend 設定](#64-graph--vector-store-backend-設定)
  - [6.5 Policy Engine 設定（governance，非傳統 access control）](#65-policy-engine-設定governance非傳統-access-control)
  - [6.6 Configuration 完整性總表](#66-configuration-完整性總表)
  - [6.7 本章 Checklist 與小結](#67-本章-checklist-與小結)
- [7. Knowledge Graph 建模與軟體開發 Ontology 設計](#7-knowledge-graph-建模與軟體開發-ontology-設計)
  - [7.1 基本建模元素](#71-基本建模元素)
  - [7.2 官方 API 範例：建立節點與邊](#72-官方-api-範例建立節點與邊)
  - [7.3 軟體開發專用 Ontology 設計（建議架構）](#73-軟體開發專用-ontology-設計建議架構)
  - [7.4 Mermaid：軟體開發 Ontology 關係圖（建議架構）](#74-mermaid軟體開發-ontology-關係圖建議架構)
  - [7.5 建立範例：把 Requirement 到 Code 的鏈路寫進 Context Graph](#75-建立範例把-requirement-到-code-的鏈路寫進-context-graph)
  - [7.6 Scenario：新進工程師理解遺留系統](#76-scenario新進工程師理解遺留系統)
  - [7.7 本章 Checklist 與小結](#77-本章-checklist-與小結)
- [8. Entity Resolution 與 Conflict Detection](#8-entity-resolution-與-conflict-detection)
  - [8.1 問題起點](#81-問題起點)
  - [8.2 官方 Deduplication API](#82-官方-deduplication-api)
  - [8.3 Conflict Detection：不應該因為衝突就直接覆蓋](#83-conflict-detection不應該因為衝突就直接覆蓋)
  - [8.4 概念模型：保留衝突，而非覆蓋](#84-概念模型保留衝突而非覆蓋)
  - [8.5 為什麼這對銀行、金融、醫療系統特別重要](#85-為什麼這對銀行金融醫療系統特別重要)
  - [8.6 AI Prompt 範例](#86-ai-prompt-範例)
  - [8.7 本章 Checklist 與小結](#87-本章-checklist-與小結)
- [9. Temporal Intelligence](#9-temporal-intelligence)
  - [9.1 核心概念](#91-核心概念)
  - [9.2 官方 API](#92-官方-api)
  - [9.3 Scenario：Framework Upgrade 的版本歷史保留](#93-scenarioframework-upgrade-的版本歷史保留)
  - [9.4 本章 Checklist 與小結](#94-本章-checklist-與小結)
- [10. Reasoning Engine](#10-reasoning-engine)
  - [10.1 LLM Reasoning vs Deterministic Graph Reasoning](#101-llm-reasoning-vs-deterministic-graph-reasoning)
  - [10.2 官方 8 種推理模式](#102-官方-8-種推理模式)
  - [10.3 Forward Chaining 範例（官方已實作）](#103-forward-chaining-範例官方已實作)
  - [10.4 Rete 規則引擎範例（README 逐字，官方已實作）](#104-rete-規則引擎範例readme-逐字官方已實作)
  - [10.5 Datalog 範例（README 逐字，官方已實作）](#105-datalog-範例readme-逐字官方已實作)
  - [10.6 Explanation Generator：可解釋的推理路徑](#106-explanation-generator可解釋的推理路徑)
  - [10.7 使用時機與常見陷阱](#107-使用時機與常見陷阱)
  - [10.8 Scenario：Framework Upgrade 的 Deterministic 驗證](#108-scenarioframework-upgrade-的-deterministic-驗證)
  - [10.9 本章 Checklist 與小結](#109-本章-checklist-與小結)
- [11. Decision Intelligence](#11-decision-intelligence)
  - [11.1 核心模型](#111-核心模型)
  - [11.2 `record_decision()` 完整簽章](#112-record_decision-完整簽章)
  - [11.3 決策查詢與因果追溯 API](#113-決策查詢與因果追溯-api)
  - [11.4 完整範例（README 逐字，官方已實作）](#114-完整範例readme-逐字官方已實作)
  - [11.5 實際案例：AI Agent 決定修改 Spring Boot Controller](#115-實際案例ai-agent-決定修改-spring-boot-controller)
  - [11.6 本章 Checklist 與小結](#116-本章-checklist-與小結)
- [12. Provenance／W3C PROV-O](#12-provenancew3c-prov-o)
  - [12.1 「可追溯」不等於「可解釋」](#121-可追溯不等於可解釋)
  - [12.2 W3C PROV-O 映射表](#122-w3c-prov-o-映射表)
  - [12.3 `ProvenanceManager` 核心方法](#123-provenancemanager-核心方法)
  - [12.4 完整範例：CVE 追蹤（官方已實作，SOC 使用案例）](#124-完整範例cve-追蹤官方已實作soc-使用案例)
  - [12.5 企業案例：Requirement → Deployment 的 Provenance Graph](#125-企業案例requirement--deployment-的-provenance-graph)
  - [12.6 何時不需要 Provenance（官方誠實列出的限制，官方已實作）](#126-何時不需要-provenance官方誠實列出的限制官方已實作)
  - [12.7 本章 Checklist 與小結](#127-本章-checklist-與小結)
- [13. Ontology／OWL／SHACL／SKOS](#13-ontologyowlshaclskos)
  - [13.1 官方 Ontology 定義](#131-官方-ontology-定義)
  - [13.2 官方 API：自動生成與驗證](#132-官方-api自動生成與驗證)
  - [13.3 SHACL Validation（官方已實作，v0.4.0 起，`docs.getsemantica.ai/guides/shacl-validation`）](#133-shacl-validation官方已實作v040-起docsgetsemanticaaiguidesshacl-validation)
  - [13.4 SKOS（詞彙控制）](#134-skos詞彙控制)
  - [13.5 銀行企業 Ontology 範例（建議架構）](#135-銀行企業-ontology-範例建議架構)
  - [13.6 本章 Checklist 與小結](#136-本章-checklist-與小結)
- [14. Graph Analytics](#14-graph-analytics)
  - [14.1 官方 API（README 逐字，官方已實作）](#141-官方-apireadme-逐字官方已實作)
  - [14.2 軟體架構情境下的應用](#142-軟體架構情境下的應用)
  - [14.3 Scenario：影響分析](#143-scenario影響分析)
  - [14.4 本章 Checklist 與小結](#144-本章-checklist-與小結)
- [15. GraphRAG](#15-graphrag)
  - [15.1 官方定義的檢索流程](#151-官方定義的檢索流程)
  - [15.2 Traditional RAG vs GraphRAG vs Semantica GraphRAG](#152-traditional-rag-vs-graphrag-vs-semantica-graphrag)
  - [15.3 何時該用 Vector Search / Graph Search / Hybrid Search（建議架構）](#153-何時該用-vector-search--graph-search--hybrid-search建議架構)
  - [15.4 Scenario：逆向工程問答](#154-scenario逆向工程問答)
  - [15.5 本章 Checklist 與小結](#155-本章-checklist-與小結)
- [16. MCP Server 完整介紹](#16-mcp-server-完整介紹)
  - [16.1 架構：不是網路 API，而是本機 stdio Server](#161-架構不是網路-api而是本機-stdio-server)
  - [16.2 安裝與啟動](#162-安裝與啟動)
  - [16.3 Claude Desktop / Claude Code 設定範例](#163-claude-desktop--claude-code-設定範例)
  - [16.4 曝露的 12 個 Tools](#164-曝露的-12-個-tools)
  - [16.5 Read-only Resources](#165-read-only-resources)
  - [16.6 Security Model](#166-security-model)
  - [16.7 Scenario：Claude Code 透過 MCP 查詢 Context](#167-scenarioclaude-code-透過-mcp-查詢-context)
  - [16.8 本章 Checklist 與小結](#168-本章-checklist-與小結)
- [17. AI Agent 整合](#17-ai-agent-整合)
  - [17.1 Claude Code](#171-claude-code)
  - [17.2 GitHub Copilot](#172-github-copilot)
  - [17.3 Codex CLI](#173-codex-cli)
  - [17.4 Cursor](#174-cursor)
  - [17.5 LangChain / LlamaIndex](#175-langchain--llamaindex)
  - [17.6 Agno（first-class 整合，README 逐字，官方已實作）](#176-agnofirst-class-整合readme-逐字官方已實作)
  - [17.7 CrewAI（first-class 整合）](#177-crewaifirst-class-整合)
  - [17.8 REST API 概覽](#178-rest-api-概覽)
  - [17.9 整合方式總覽表](#179-整合方式總覽表)
  - [17.10 本章 Checklist 與小結](#1710-本章-checklist-與小結)
- [18. 企業資料 Ingestion](#18-企業資料-ingestion)
  - [18.1 官方支援的資料源](#181-官方支援的資料源)
  - [18.2 Databricks Ingestion（README 逐字，官方已實作）](#182-databricks-ingestionreadme-逐字官方已實作)
  - [18.3 Snowflake Ingestion（README 逐字，官方已實作）](#183-snowflake-ingestionreadme-逐字官方已實作)
  - [18.4 企業 Ingestion 架構（建議架構，整合官方模組重新繪製）](#184-企業-ingestion-架構建議架構整合官方模組重新繪製)
  - [18.5 資料正規化（README 逐字，官方已實作）](#185-資料正規化readme-逐字官方已實作)
  - [18.6 Pipeline DSL（README 逐字，官方已實作）](#186-pipeline-dslreadme-逐字官方已實作)
  - [18.7 本章 Checklist 與小結](#187-本章-checklist-與小結)
- [19. 情境 A 實戰：AI Agent 開發 Web Application](#19-情境-a-實戰ai-agent-開發-web-application)
  - [19.1 情境設定](#191-情境設定)
  - [19.2 目標：建立跨開發生命週期的圖關係](#192-目標建立跨開發生命週期的圖關係)
  - [19.3 Process：15 個實作步驟](#193-process15-個實作步驟)
  - [19.4 範例：AI Agent 開發新 API 端點](#194-範例ai-agent-開發新-api-端點)
  - [19.5 ArchUnit + Semantica：架構規則的雙重驗證](#195-archunit--semantica架構規則的雙重驗證)
  - [19.6 AI Prompt 範例](#196-ai-prompt-範例)
  - [19.7 本章 Checklist 與小結](#197-本章-checklist-與小結)
- [20. 情境 B 實戰：AI 輔助逆向工程](#20-情境-b-實戰ai-輔助逆向工程)
  - [20.1 全流程](#201-全流程)
  - [20.2 極重要的邊界釐清：Semantica 不是完整的 Source Code Static Analyzer](#202-極重要的邊界釐清semantica-不是完整的-source-code-static-analyzer)
  - [20.3 20 個實作步驟](#203-20-個實作步驟)
  - [20.4 AI Agent 必須能回答的問題（逐一對應 KG 查詢）](#204-ai-agent-必須能回答的問題逐一對應-kg-查詢)
  - [20.5 範例：找出高風險模組](#205-範例找出高風險模組)
  - [20.6 AI Prompt 範例](#206-ai-prompt-範例)
  - [20.7 本章 Checklist 與小結](#207-本章-checklist-與小結)
- [21. 情境 C 實戰：AI 輔助 Framework Upgrade](#21-情境-c-實戰ai-輔助-framework-upgrade)
  - [21.1 全流程](#211-全流程)
  - [21.2 Semantica 負責的內容](#212-semantica-負責的內容)
  - [21.3 實作步驟](#213-實作步驟)
  - [21.4 官方 Migration Rule 轉換為 Forward Chaining 規則（示意）](#214-官方-migration-rule-轉換為-forward-chaining-規則示意)
  - [21.5 最終可回答的 7 個關鍵問題](#215-最終可回答的-7-個關鍵問題)
  - [21.6 AI Prompt 範例](#216-ai-prompt-範例)
  - [21.7 本章 Checklist 與小結](#217-本章-checklist-與小結)
- [22. AI SSDLC 完整流程](#22-ai-ssdlc-完整流程)
  - [22.1 AI-Assisted SSDLC 十二階段（建議架構）](#221-ai-assisted-ssdlc-十二階段建議架構)
  - [22.2 每階段對應的 Semantica 節點類型](#222-每階段對應的-semantica-節點類型)
  - [22.3 本章 Checklist 與小結](#223-本章-checklist-與小結)
- [23. AI Agent Team 設計](#23-ai-agent-team-設計)
  - [23.1 多角色 Agent 團隊架構（建議架構）](#231-多角色-agent-團隊架構建議架構)
  - [23.2 各 Agent 角色與 Semantica 互動方式](#232-各-agent-角色與-semantica-互動方式)
  - [23.3 共享 Context 的關鍵設計原則（建議架構）](#233-共享-context-的關鍵設計原則建議架構)
  - [23.4 本章 Checklist 與小結](#234-本章-checklist-與小結)
- [24. Security Architecture](#24-security-architecture)
  - [24.1 官方已確認的安全相關事實](#241-官方已確認的安全相關事實)
  - [24.2 企業必須自行補強的安全層（建議架構）](#242-企業必須自行補強的安全層建議架構)
  - [24.3 Prompt Injection 與 Graph Poisoning 防禦](#243-prompt-injection-與-graph-poisoning-防禦)
  - [24.4 MCP / Agent Tool Security](#244-mcp--agent-tool-security)
  - [24.5 本章 Checklist 與小結](#245-本章-checklist-與小結)
- [25. 資料治理與 Governance](#25-資料治理與-governance)
  - [25.1 五層治理模型（建議架構）](#251-五層治理模型建議架構)
  - [25.2 關鍵治理維度](#252-關鍵治理維度)
  - [25.3 本章 Checklist 與小結](#253-本章-checklist-與小結)
- [26. Observability](#26-observability)
  - [26.1 四個觀測維度（建議架構）](#261-四個觀測維度建議架構)
  - [26.2 建議監控指標（建議架構，Semantica 未內建現成 Dashboard，需企業自行從 API 擷取指標）](#262-建議監控指標建議架構semantica-未內建現成-dashboard需企業自行從-api-擷取指標)
  - [26.3 與既有 Observability 生態系整合（建議架構）](#263-與既有-observability-生態系整合建議架構)
  - [26.4 本章 Checklist 與小結](#264-本章-checklist-與小結)
- [27. Performance／Scalability](#27-performancescalability)
  - [27.1 官方效能數據](#271-官方效能數據)
  - [27.2 大型 KG 的效能考量（建議架構）](#272-大型-kg-的效能考量建議架構)
  - [27.3 環境分層架構（建議架構）](#273-環境分層架構建議架構)
  - [27.4 本章 Checklist 與小結](#274-本章-checklist-與小結)
- [28. High Availability／Backup／DR](#28-high-availabilitybackupdr)
  - [28.1 建議架構圖](#281-建議架構圖)
  - [28.2 HA 設計原則](#282-ha-設計原則)
  - [28.3 Backup／DR 策略](#283-backupdr-策略)
  - [28.4 RPO／RTO 建議基準（建議架構，企業應依實際風險容忍度調整）](#284-rporto-建議基準建議架構企業應依實際風險容忍度調整)
  - [28.5 本章 Checklist 與小結](#285-本章-checklist-與小結)
- [29. Docker／Podman／Kubernetes 部署](#29-dockerpodmankubernetes-部署)
  - [29.1 官方部署範本的實際範圍](#291-官方部署範本的實際範圍)
  - [29.2 Docker Compose 範例（建議架構）](#292-docker-compose-範例建議架構)
  - [29.3 Podman 對照](#293-podman-對照)
  - [29.4 Kubernetes 部署範例（建議架構）](#294-kubernetes-部署範例建議架構)
  - [29.5 本章 Checklist 與小結](#295-本章-checklist-與小結)
- [30. CLI 完整參考](#30-cli-完整參考)
  - [30.1 五個 CLI 執行檔（官方已實作，`docs.getsemantica.ai/cli-setup`）](#301-五個-cli-執行檔官方已實作docsgetsemanticaaicli-setup)
  - [30.2 `semantica` 主指令群組（官方已實作，README 指令清單）](#302-semantica-主指令群組官方已實作readme-指令清單)
  - [30.3 `semantica-server`（官方已實作）](#303-semantica-server官方已實作)
  - [30.4 `semantica-worker`（官方已實作）](#304-semantica-worker官方已實作)
  - [30.5 `semantica-explorer`（官方已實作）](#305-semantica-explorer官方已實作)
  - [30.6 `semantica-mcp`（官方已實作，第 16 章已詳述）](#306-semantica-mcp官方已實作第-16-章已詳述)
  - [30.7 驗證清單](#307-驗證清單)
  - [30.8 本章 Checklist 與小結](#308-本章-checklist-與小結)
- [31. Python API 完整參考](#31-python-api-完整參考)
  - [31.1 核心模組一覽（官方已實作，README「Core Modules」）](#311-核心模組一覽官方已實作readmecore-modules)
  - [31.2 API 使用時機速查（每個模組的「何時使用」）](#312-api-使用時機速查每個模組的何時使用)
  - [31.3 Common Mistakes（跨模組常見錯誤，建議架構）](#313-common-mistakes跨模組常見錯誤建議架構)
  - [31.4 Version Notes](#314-version-notes)
  - [31.5 Export 模組完整範例（README 逐字，官方已實作）](#315-export-模組完整範例readme-逐字官方已實作)
  - [31.6 Visualization 模組完整範例（README 逐字，官方已實作）](#316-visualization-模組完整範例readme-逐字官方已實作)
  - [31.7 本章 Checklist 與小結](#317-本章-checklist-與小結)
- [32. Testing](#32-testing)
  - [32.1 測試分層（建議架構）](#321-測試分層建議架構)
  - [32.2 Golden Knowledge Graph 概念（建議架構）](#322-golden-knowledge-graph-概念建議架構)
  - [32.3 本章 Checklist 與小結](#323-本章-checklist-與小結)
- [33. Evaluation 指標](#33-evaluation-指標)
  - [33.1 各面向指標（建議架構，整合官方模組能力設計的評估框架）](#331-各面向指標建議架構整合官方模組能力設計的評估框架)
  - [33.2 本章 Checklist 與小結](#332-本章-checklist-與小結)
- [34. Maintenance](#34-maintenance)
  - [34.1 每日／每週／每月維護 Checklist（建議架構）](#341-每日每週每月維護-checklist建議架構)
  - [34.2 本章 Checklist 與小結](#342-本章-checklist-與小結)
- [35. Upgrade SOP](#35-upgrade-sop)
  - [35.1 標準流程](#351-標準流程)
  - [35.2 各步驟說明（建議架構）](#352-各步驟說明建議架構)
  - [35.3 讓 AI Agent 協助升級（建議架構）](#353-讓-ai-agent-協助升級建議架構)
  - [35.4 本章 Checklist 與小結](#354-本章-checklist-與小結)
- [36. 企業導入方法論與 RACI](#36-企業導入方法論與-raci)
  - [36.1 五階段導入方法論（建議架構）](#361-五階段導入方法論建議架構)
  - [36.2 RACI 表](#362-raci-表)
  - [36.3 本章 Checklist 與小結](#363-本章-checklist-與小結)
- [37. AI Agent + Semantica 開發 SOP](#37-ai-agent--semantica-開發-sop)
  - [37.1 開發前 Checklist](#371-開發前-checklist)
  - [37.2 開發中 Checklist](#372-開發中-checklist)
  - [37.3 開發後 Checklist](#373-開發後-checklist)
  - [37.4 本章 Checklist 與小結](#374-本章-checklist-與小結)
- [38. AI Agent Prompt Engineering 範本](#38-ai-agent-prompt-engineering-範本)
  - [38.1 Requirement Analysis Prompt](#381-requirement-analysis-prompt)
  - [38.2 Architecture Analysis Prompt](#382-architecture-analysis-prompt)
  - [38.3 Reverse Engineering Prompt](#383-reverse-engineering-prompt)
  - [38.4 Coding Prompt](#384-coding-prompt)
  - [38.5 Code Review Prompt](#385-code-review-prompt)
  - [38.6 Framework Upgrade Prompt](#386-framework-upgrade-prompt)
  - [38.7 Impact Analysis Prompt](#387-impact-analysis-prompt)
  - [38.8 Security Review Prompt](#388-security-review-prompt)
  - [38.9 Test Generation Prompt](#389-test-generation-prompt)
  - [38.10 Decision Recording Prompt](#3810-decision-recording-prompt)
  - [38.11 Audit Prompt](#3811-audit-prompt)
  - [38.12 本章 Checklist 與小結](#3812-本章-checklist-與小結)
- [39. 銀行企業案例](#39-銀行企業案例)
  - [39.1 情境設定](#391-情境設定)
  - [39.2 為什麼 Semantica 特別適合高可追溯性需求的企業 AI](#392-為什麼-semantica-特別適合高可追溯性需求的企業-ai)
  - [39.3 技術能力 ≠ 法規合規聲明（重申）](#393-技術能力--法規合規聲明重申)
  - [39.4 範例：AML 高風險交易規則（README 案例改編）](#394-範例aml-高風險交易規則readme-案例改編)
  - [39.5 本章 Checklist 與小結](#395-本章-checklist-與小結)
- [40. 與其他技術比較](#40-與其他技術比較)
  - [40.1 比較說明（避免貶低其他工具）](#401-比較說明避免貶低其他工具)
  - [40.2 本章 Checklist 與小結](#402-本章-checklist-與小結)
- [41. 常見錯誤](#41-常見錯誤)
  - [41.1 本章 Checklist 與小結](#411-本章-checklist-與小結)
- [42. Troubleshooting](#42-troubleshooting)
  - [42.1 本章 Checklist 與小結](#421-本章-checklist-與小結)
- [43. 完整企業 Reference Architecture](#43-完整企業-reference-architecture)
  - [43.1 元件說明](#431-元件說明)
  - [43.2 本章 Checklist 與小結](#432-本章-checklist-與小結)
- [44. Demo Project](#44-demo-project)
  - [44.1 專案骨架（建議架構）](#441-專案骨架建議架構)
  - [44.2 關鍵程式碼：`scripts/03_build_kg.py`（示意）](#442-關鍵程式碼scripts03_build_kgpy示意)
  - [44.3 關鍵程式碼：`src/agents/migration_agent.py`（示意，對應第 21 章）](#443-關鍵程式碼srcagentsmigration_agentpy示意對應第-21-章)
  - [44.4 本章 Checklist 與小結](#444-本章-checklist-與小結)
- [45. 學習路線](#45-學習路線)
  - [45.1 本章 Checklist 與小結](#451-本章-checklist-與小結)
- [46. FAQ：最終 20 個問題](#46-faq最終-20-個問題)
- [47. 結論](#47-結論)
- [附錄 A：官方參考來源](#附錄-a官方參考來源)
- [附錄 B：研究來源分級](#附錄-b研究來源分級)
- [附錄 C：全書 Checklist 總覽](#附錄-c全書-checklist-總覽)

---

## 1. 文件說明與如何使用本手冊

### 1.1 這份手冊要解決什麼問題

企業導入 LLM/AI Agent 開發時最常遇到的痛點不是「AI 不夠聰明」，而是：

- AI 給出的答案「聽起來合理」但無法回溯到具體的需求文件、程式碼行、資料庫欄位或官方規格
- 同一個問題問兩次，AI Agent 給出不一致的答案，而且沒有人知道「上一次為什麼這樣決定」
- 修改一個 Java Class 之後，沒有人（包含 AI Agent 自己）能回答「這個改動會影響哪些下游模組」
- 稽核／法遵單位要求「這個 AI 決策的依據是什麼」時，工程團隊只能回頭翻 Slack 對話紀錄

Semantica 的定位正是解決「AI Agent 缺乏可查詢、可追溯、可問責的上下文」這個基礎設施問題（見第 2 章）。本手冊教你如何在企業內部落地。

### 1.2 如何閱讀這份手冊

- **第一次接觸 Semantica**：依序閱讀第 2、3、4 章建立心智模型，再讀第 5 章動手安裝，跑一次第 4 章對應的 Quickstart。
- **已熟悉 KG/GraphRAG，想快速導入企業場景**：直接跳到第 19-21 章的三大情境，遇到不熟的概念再回頭查第 7-16 章。
- **維運／SRE 角色**：直接看第 26-29、34-35 章。
- **架構師／導入負責人**：看第 36 章企業導入方法論、第 40 章技術比較、第 43 章 Reference Architecture。
- **要準備教育訓練或內部 Prompt 範本**：直接用第 37、38 章。

### 1.3 與官方文件的差異

官方文件（`docs.getsemantica.ai`）以「單一功能點」為單位介紹（例如「怎麼用 ProvenanceManager」），本手冊額外提供：**跨章節的企業情境串接**（例如同一個 Spring Boot Controller 修改案例，會同時出現在第 11 章 Decision Intelligence、第 12 章 Provenance、第 21 章 Framework Upgrade），以及**官方文件沒有的企業落地建議**（K8s HA、RACI、SOP、Prompt 範本），這些落地建議都會明確標示「建議架構」。

### 1.4 本章 Checklist 與小結

- [ ] 已理解五層 Provenance 標示法的意義
- [ ] 已理解「官方功能」與「本手冊原創企業建議」的界線
- [ ] 已根據自己的角色（開發／架構／維運）選好閱讀路徑

---

## 2. Semantica 簡介與定位

### 2.1 官方定位

Semantica 官方自我定位為「The Accountability and Context Layer for AI」——AI 的問責與上下文層（官方已實作，`getsemantica.ai`）。README 的技術性描述是「Graph-Native Infrastructure for Context and Accountable AI Systems」（官方已實作）。它是一個開源 Python framework，用來建立 Context Graph 與 Decision Intelligence Layer，可以加掛在 LangGraph、CrewAI、LlamaIndex 等既有 Agent Framework 之上（官方已實作，README）。

### 2.2 Semantica 不是什麼

這是全書最重要的一句話，因為企業導入最常見的第一個錯誤就是搞錯定位（另見第 41 章「常見錯誤」）：

| 常見誤解 | 實際情況 |
|---|---|
| Semantica 是 LangChain 的替代品 | 不是。Semantica 提供 Context/KG/Decision 基礎設施，LangChain 提供 Agent 編排；兩者可以疊加使用 |
| Semantica 是 LlamaIndex 的替代品 | 不是。LlamaIndex 專注 RAG 索引與檢索，Semantica 專注結構化知識與決策問責 |
| Semantica 是向量資料庫（Vector DB）的替代品 | 不是。Semantica **內部使用**向量庫（FAISS 等）做語意檢索，但核心價值是圖結構 + Provenance + Decision，而非單純相似度搜尋 |
| Semantica 是 LLM 的替代品 | 不是。Semantica 本身不訓練也不提供 LLM 推論，`semantica.llms` 模組是透過 LiteLLM 呼叫既有 LLM Provider |
| Semantica 是 Agent Framework（取代 Agno/CrewAI） | 不是。Semantica 對 Agno、CrewAI 是 first-class 整合對象，而非取代對象 |

### 2.3 分層定位圖

```mermaid
graph TB
    LLM["LLM<br/>(GPT / Claude / Gemini / Llama ...)"]
    AF["Agent Framework<br/>(Agno / CrewAI / LangGraph / 自研 Agent)"]
    TOOLS["Tools / MCP"]
    SEM["Semantica<br/>Accountability &amp; Context Layer"]
    KG["Knowledge Graph / Context Graph"]
    STORE["Graph Store / RDF Store / Vector Store"]
    DATA["Enterprise Data<br/>(Git, Source Code, DB, Docs, API ...)"]

    LLM --> AF --> TOOLS --> SEM --> KG --> STORE --> DATA
```

逐層解釋（建議架構，整合官方模組說明重新繪製）：

1. **LLM**：負責語言理解、生成、假設提出，但天生無狀態、無法自證答案來源。
2. **Agent Framework**：負責規劃、工具呼叫、多步驟編排。
3. **Tools / MCP**：Agent 與外部世界互動的介面，Semantica 透過 MCP Server 曝露 12 個 tools（見第 16 章）。
4. **Semantica Accountability & Context Layer**：本手冊的核心——把「LLM 說了什麼」升級為「LLM 依據哪些證據、走過哪些推理步驟，做出了哪個可查詢的決策」。
5. **Knowledge Graph / Context Graph**：結構化知識的實際承載體（第 3、7 章詳述兩者差異）。
6. **Graph Store / RDF Store / Vector Store**：底層儲存後端，可依企業既有基礎設施選擇 Neo4j、Oxigraph、PgVector 等（第 5、27 章）。
7. **Enterprise Data**：一切的源頭——原始碼、需求文件、資料庫、API 規格、Kafka 事件等（第 18 章）。

### 2.4 與既有 AI 生態系的整合關係

| 對象 | 整合方式 | 標示 |
|---|---|---|
| Claude Code | MCP Server（stdio）＋ Editor Plugin | 官方已實作 |
| GitHub Copilot | 目前無官方原生 plugin，可透過 REST API／Repository Context 間接整合 | 建議架構 |
| Codex CLI | Editor Plugin Bundle | 官方已實作 |
| Cursor | MCP Server ＋ Editor Plugin | 官方已實作 |
| VS Code | Editor Plugin Bundle | 官方已實作 |
| LangChain / LlamaIndex | 透過 REST API 或 MCP 呼叫 | 官方已實作 |
| Agno / CrewAI | `pip install semantica[agno]` / `[crewai]`，first-class SDK 整合 | 官方已實作 |
| 自研 AI Agent | REST API（`semantica-server`，109 endpoints）或直接 import Python 模組 | 官方已實作 |

第 17 章會針對每一種整合方式提供更完整的設定與程式碼範例。

### 2.5 Scenario：企業第一次接觸 Semantica

> 情境：某銀行的 AI 平台團隊導入 Claude Code 協助開發，但半年後稽核部門要求「說明過去 3 個月 AI 產生的程式碼修改，各自依據什麼理由、誰核准、是否測試過」。團隊發現 Git commit message 與 Slack 對話無法系統化重建這條軌跡。

這正是 Semantica 要解決的問題：把「AI Agent 的每一次決策」變成 Knowledge Graph 裡一個可查詢、可回溯、有因果鏈的節點（見第 11 章 Decision Intelligence、第 39 章銀行案例）。

### 2.6 AI Prompt 範例（初次評估）

```text
你是企業 AI 平台架構師。請比較 Semantica 與我們目前使用的 [LangChain + Pinecone] 堆疊，
明確指出：(1) 兩者的定位差異 (2) Semantica 可以疊加而非取代的部分
(3) 導入 Semantica 需要新增哪些基礎設施（Graph Store／RDF Store）
(4) 對現有 Agent 開發流程的影響範圍。
不要假設功能存在，若不確定請標明「需查證」。
```

### 2.7 本章 Checklist 與小結

- [ ] 已能清楚說明 Semantica「是什麼」與「不是什麼」
- [ ] 已理解 Semantica 在 LLM → Agent → Semantica → KG → Store → Data 分層中的位置
- [ ] 已識別自己團隊現有的 Agent Framework 與 Semantica 的整合路徑

---

## 3. 核心概念總覽

企業導入時最常見的混淆，是把 Vector Database、Knowledge Graph、Context Graph、GraphRAG、Decision Graph、Provenance Graph、Causal Graph 這幾個名詞當成同一件事。它們目的不同，不應混為一談：

| 技術 | 目的 | Semantica 對應模組 | 標示 |
|---|---|---|---|
| Vector Database | Semantic similarity（語意相似度檢索） | `semantica.vector_store`（FAISS/Qdrant/…） | 官方已實作 |
| Knowledge Graph | Structured relationships（結構化實體關係） | `semantica.kg`（`GraphBuilder` 等） | 官方已實作 |
| Context Graph | AI Agent operational context（Agent 當下可用的結構化上下文，含節點/邊的 temporal validity window，thread-safe in-memory property graph） | `semantica.context.ContextGraph` / `AgentContext` | 官方已實作，`docs.getsemantica.ai/guides/context-graphs` |
| GraphRAG | Graph + Retrieval（圖檢索增強生成） | `semantica.kg` + `semantica.vector_store` 混合檢索 | 官方已實作，`docs.getsemantica.ai/guides/graphrag` |
| Decision Graph | Decision lifecycle（決策生命週期：record → trace → precedent → impact） | `ContextGraph.record_decision()` 等 | 官方已實作，`docs.getsemantica.ai/guides/decision-intelligence` |
| Provenance Graph | Source / lineage（來源與世系追溯，W3C PROV-O） | `semantica.provenance.ProvenanceManager` | 官方已實作，`docs.getsemantica.ai/guides/provenance` |
| Causal Graph | Cause / effect（決策之間的因果鏈） | `get_causal_chain()` / `trace_decision_causality()` | 官方已實作 |

### 3.1 Context Graph vs Knowledge Graph：最容易搞混的一組

官方文件對 `ContextGraph` 的定義（官方已實作，`docs.getsemantica.ai/guides/context-graphs`）：

> A **ContextGraph** is a thread-safe, in-memory property graph that structures knowledge as nodes (entities) and edges (relationships)。

關鍵差異（整理自官方 Context Graph／KG Guide）：

- **Context Graph**：偏向 Agent 執行當下「即時可用」的工作記憶，特徵是 in-memory、thread-safe、內建 temporal validity window、整合 FAISS 向量索引做 hybrid retrieval。適合單一 Agent Session 或 Agent Team 共享上下文（見第 23 章）。
- **Knowledge Graph（`semantica.kg`）**：偏向企業長期沉澱、可持久化、可跑 Graph Analytics（centrality、community detection）、可匯出 RDF/Cypher 的知識資產。

企業實務上，通常是：Ingestion Pipeline 先建出持久化的 Knowledge Graph，再由 `AgentContext` 在執行期把相關子圖與向量索引載入成 Context Graph 供 Agent 查詢（建議架構）。

### 3.2 Semantica 如何整合這些概念

```mermaid
flowchart LR
    subgraph Store["持久化層"]
        KG["Knowledge Graph<br/>(semantica.kg)"]
        PROV["Provenance Graph<br/>(ProvenanceManager)"]
        DEC["Decision Graph<br/>(record_decision 節點)"]
    end
    subgraph Runtime["執行期"]
        CTX["Context Graph / AgentContext<br/>(In-Memory + FAISS)"]
        AGENT["AI Agent"]
    end
    KG -->|"載入相關子圖"| CTX
    PROV -.->|"每個節點/邊皆有 source_id"| KG
    DEC -.->|"因果鏈接回 KG 實體"| KG
    CTX <--> AGENT
    AGENT -->|"record_decision()"| DEC
```

### 3.3 Scenario：選型決策

> 團隊已經有 Pinecone 做 RAG，該不該再導入 Semantica？

判斷準則（建議架構）：

- 如果需求僅止於「找出語意相似的文件片段」→ Vector DB 已足夠，不必強行導入 Semantica。
- 如果需求包含「這個答案的推理路徑是什麼」「兩個實體之間有什麼關係」「這個 AI 決策半年後能否被稽核」→ 需要 Context Graph + Decision Intelligence + Provenance，這正是 Semantica 的價值主張。
- 兩者非互斥：Semantica 內部本來就整合向量檢索（`vector_store` 模組可直接指向既有 Pinecone/PgVector），可視為在既有 RAG 堆疊上加一層問責與圖結構。

### 3.4 本章 Checklist 與小結

- [ ] 能用一句話分別解釋 Vector DB、KG、Context Graph、GraphRAG、Decision Graph、Provenance Graph、Causal Graph
- [ ] 理解 Context Graph 是「執行期工作記憶」，Knowledge Graph 是「持久化知識資產」
- [ ] 已能判斷團隊現有問題屬於「單純語意檢索」還是「需要問責與圖結構」

---

## 4. Architecture 深入解析

### 4.1 官方四層架構

官方 Architecture 文件（官方已實作，`docs.getsemantica.ai/architecture`）將 Semantica 描述為四層模組化設計：

1. **Ingestion Layer**：從任意來源載入資料，統一轉為 `SourceDocument`（支援 PDF、資料庫、網頁、Kafka streams、email、程式碼庫等）。
2. **Processing Layer**：把原始文字轉為結構化、豐富化的文件，包含 Parse、Normalize、Semantic Extraction、QA 步驟。
3. **Intelligence Layer**：持久化知識儲存與 Embedding 基礎設施，涵蓋 Knowledge Graph、Vector Store、Ontology、Temporal Model。
4. **Application Layer**：交付 GraphRAG、Agent Memory、Decision Tracking、Visualization、Multi-Agent Systems 等能力。

官方也描述了 8 步驟線性資料流：**Ingest → Parse → Normalize → Extract → Build KG → QA → Store → Deliver**（官方已實作），每個階段皆維持 Provenance 追蹤。

### 4.2 企業級擴充架構圖（整合官方模組 + Master Prompt 要求的完整資料源清單）

```mermaid
flowchart TB
    subgraph Sources["Enterprise Data Sources"]
        GIT["Git / Source Code"]
        DOC["Documents (PDF/DOCX/XLSX)"]
        DB["Database"]
        API["API"]
        KAFKA["Kafka"]
        SNOW["Snowflake"]
        DBX["Databricks"]
        MCPIN["MCP"]
    end

    Sources --> ING["Ingestion<br/>(semantica.ingest)"]
    ING --> PARSE["Parsing<br/>(semantica.parse)"]
    PARSE --> NORM["Normalization<br/>(semantica.normalize)"]
    NORM --> SPLIT["Splitting<br/>(semantica.split)"]
    SPLIT --> EXTRACT["Semantic Extraction<br/>(semantica.semantic_extract)"]

    subgraph ExtractDetail["Entity / Relation / Event / Triplet Extraction"]
        NER["NamedEntityRecognizer"]
        REL["RelationExtractor"]
        EVT["EventDetector"]
        TRIP["TripletExtractor"]
    end
    EXTRACT --> ExtractDetail

    ExtractDetail --> CONFLICT["Conflict Detection<br/>(semantica.conflicts)"]
    CONFLICT --> DEDUP["Entity Resolution / Deduplication<br/>(semantica.deduplication)"]
    DEDUP --> KGBUILD["Knowledge Graph<br/>(semantica.kg.GraphBuilder)"]

    subgraph Intelligence["Ontology / Reasoning / Provenance / Decision / Temporal"]
        ONT["Ontology<br/>(semantica.ontology)"]
        REASON["Reasoning<br/>(semantica.reasoning)"]
        PROV2["Provenance<br/>(semantica.provenance)"]
        DECI["Decision Intelligence<br/>(ContextGraph.record_decision)"]
        TEMP["Temporal Intelligence<br/>(BiTemporalFact)"]
    end
    KGBUILD --> Intelligence

    subgraph Backend["Graph Store / RDF Store / Vector Store"]
        LPGDB["LPG: Neo4j / FalkorDB / Apache AGE / Neptune"]
        RDFDB["RDF: Oxigraph / Blazegraph / Jena / RDF4J / Anzo"]
        VECDB["Vector: FAISS / Qdrant / Weaviate / Milvus / Pinecone / PgVector"]
    end
    Intelligence --> Backend

    subgraph AppLayer["AI Agent / GraphRAG / MCP / REST / CLI / Visualization"]
        AGENT2["AI Agent"]
        GRAG["GraphRAG"]
        MCP2["MCP Server"]
        REST["REST API"]
        CLI2["CLI"]
        VIZ["Visualization / Explorer"]
    end
    Backend --> AppLayer
```

### 4.3 逐層解釋（企業導入視角）

1. **Enterprise Data Sources**：對企業 Web 開發／逆向工程／Framework Upgrade 情境而言，最關鍵的來源是 Git（原始碼與 commit history）、Database schema、API 規格（OpenAPI/Swagger）——這些會在第 18-21 章詳述。
2. **Ingestion → Parsing → Normalization → Splitting**：官方提供 `FileIngestor`、`WebIngestor`、`ParquetIngestor`、`DatabricksIngestor`、`SnowflakeIngestor` 等（官方已實作，README／Quickstart），`TextSplitter` 支援 entity-aware、relation-aware 等 GraphRAG 導向切分策略（官方已實作）。
3. **Semantic Extraction**：`NamedEntityRecognizer`、`RelationExtractor`、`EventDetector`、`TripletExtractor`，支援 pattern／ML／LLM 三種抽取方法並可 fallback chain（官方已實作，`docs.getsemantica.ai/guides/semantic-extraction`）。
4. **Conflict Detection → Entity Resolution → Deduplication**：這是企業資料品質的關鍵防線，避免不同來源的衝突資料被靜默覆蓋（見第 8 章）。
5. **Knowledge Graph + Ontology/Reasoning/Provenance/Decision/Temporal**：Intelligence Layer 是 Semantica 的核心價值所在，第 7-14 章逐一深入。
6. **Graph Store / RDF Store / Vector Store**：官方明確設計為「可替換，不必改動應用程式碼」（官方已實作），企業可依既有基礎設施選型（第 27 章效能考量）。
7. **AI Agent / GraphRAG / MCP / REST / CLI / Visualization**：Application Layer 是企業團隊實際互動的介面，第 15-17、30-31 章詳述。

### 4.4 官方核心設計原則

（官方已實作，`docs.getsemantica.ai/architecture`）

- **Modularity**：「Import only what you need: the framework never forces a full stack.」——可只匯入 `semantica.provenance` 而不必安裝整個 KG pipeline。
- **Pluggability**：自訂元件可透過 `PluginRegistry` 註冊，不需修改核心程式碼。
- **Provenance by Default**：「Every node and edge carries a `source_id` pointing back to the originating document, extraction method, and timestamp.」——這是 Semantica 與一般 KG 工具最大的差異點。
- **Configuration over Convention**：集中設定管理，支援環境變數覆寫，方便多環境部署。

### 4.5 6 步驟 Quickstart Pipeline（官方已實作，`docs.getsemantica.ai/quickstart`）

```python
# 1. Ingest
from semantica.ingest import FileIngestor
ingestor = FileIngestor()
sources = ingestor.ingest("data/report.pdf")

# 2. Parse
from semantica.parse import DocumentParser
parser = DocumentParser()
parsed = parser.parse(sources[0])

# 3. Extract
from semantica.semantic_extract import NERExtractor, RelationExtractor
ner = NERExtractor(method="pattern")
entities = ner.extract(parsed)
rel = RelationExtractor(method="rule")
relationships = rel.extract(parsed, entities=entities)

# 4. Build Graph
from semantica.kg import GraphBuilder
builder = GraphBuilder(merge_entities=True)
graph = builder.build({"entities": entities, "relationships": relationships})

# 5. Visualize
from semantica.visualization import KGVisualizer
viz = KGVisualizer(layout="force")
viz.visualize_network(graph, output="html", file_path="graph.html")

# 6. Export
from semantica.export import RDFExporter
exporter = RDFExporter()
exporter.export(graph, file_path="graph.ttl", format="turtle")
```

這 6 步驟不需要任何 LLM API Key（pattern-based extraction），適合作為第一次上手的驗證流程（見第 5.5 節）。

### 4.6 本章 Checklist 與小結

- [ ] 已理解官方四層架構（Ingestion/Processing/Intelligence/Application）
- [ ] 已理解「Provenance by Default」是 Semantica 架構上最核心的設計原則
- [ ] 已成功在本機執行過一次 6 步驟 Quickstart（建議在讀完第 5 章安裝後回來完成）

---

## 5. Installation（安裝）

### 5.1 前置需求

- Python ≥3.8（官方 `pyproject.toml`／`docs.getsemantica.ai/installation` 明確的唯一版本下限）。**「建議 3.11+」為本手冊依 Python 生態系一般最佳實務提出的建議架構，並非官方文件逐字要求**——2026-08-20 重新查證官方文件時，僅找到 ≥3.8 下限，未見官方明確寫出 3.11+ 字樣，正式導入前請以你查閱當下的官方 Installation 頁面為準（官方已實作：下限；建議架構：3.11+ 建議）
- pip
- Windows 使用者需額外安裝 **Microsoft Visual C++ Redistributable**（PyTorch 相依性需求）（官方已實作）

### 5.2 Windows 安裝（venv）

```powershell
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
venv\Scripts\activate

# 安裝 Semantica（核心）
pip install semantica

# 驗證安裝
python -c "import semantica; print(semantica.__version__)"
```

> ⚠️ **已知問題**：v0.5.0 之前，Windows 上 `pip install semantica[all]` 曾經安裝失敗，已於 **v0.5.0 修復**（官方已實作，`docs.getsemantica.ai/installation`）。若你的版本早於 v0.5.0 且在 Windows 遇到 `[all]` 安裝失敗，請先升級。

### 5.3 Linux / macOS 安裝（venv）

```bash
python -m venv venv
source venv/bin/activate
pip install semantica
python -c "import semantica; print(semantica.__version__)"
```

### 5.4 使用 conda

```bash
conda create -n semantica python=3.11
conda activate semantica
pip install semantica
```

### 5.5 WSL2

Semantica 官方文件未特別列出 WSL2 專屬章節，但因其本質是標準 Python 套件，WSL2 上的安裝方式等同 Linux 安裝步驟（5.3 節）（Source-confirmed）。企業若在 Windows 開發機上使用 WSL2 作為 Java/Node 開發環境，建議 Semantica 也安裝在同一個 WSL2 distro 內，避免 Windows/WSL2 檔案系統路徑轉換造成 `SEMANTICA_KG_PATH` 等路徑設定錯誤（建議架構）。

### 5.6 Extras（依需求安裝的可選套件）

（官方已實作，README／`docs.getsemantica.ai/installation`）

```bash
pip install semantica[all]               # 全部功能
pip install semantica[agno]              # Agno 多代理整合
pip install semantica[crewai]            # CrewAI 整合
pip install semantica[graph-neo4j]       # Neo4j（LPG）
pip install semantica[db-databricks]     # Databricks
pip install semantica[db-snowflake]      # Snowflake
pip install semantica[explorer]          # Knowledge Explorer 視覺化儀表板
pip install semantica[gpu]               # GPU 加速
pip install semantica[viz]               # 視覺化相依套件
pip install semantica[llm-openai]        # OpenAI LLM Provider
pip install semantica[llm-anthropic]     # Anthropic LLM Provider
pip install semantica[llm-gemini]        # Google Gemini LLM Provider
pip install semantica[llm-groq]          # Groq LLM Provider
pip install semantica[llm-ollama]        # Ollama（本機 LLM）
pip install semantica[cloud]             # 雲端儲存整合
```

企業建議：正式環境**不要**直接裝 `[all]`，而是依實際使用的 Graph Store／Vector Store／LLM Provider 精準安裝對應 extras，降低攻擊面與映像檔大小（建議架構）。

### 5.7 Docker

官方自 **v0.5.1** 起提供 Knowledge Explorer 的 Docker 部署範本（官方已實作，GitHub Release Notes v0.5.1）。完整生產環境的 Semantica Server + Worker 容器化仍建議企業自行封裝（見第 29 章），示意 Dockerfile：

```dockerfile
# 示意 Dockerfile，非官方逐字範例
FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir "semantica[explorer]"

ENV SEMANTICA_KG_PATH=/data/knowledge_graph.json
ENV SEMANTICA_LOG_LEVEL=INFO

EXPOSE 8000
CMD ["semantica-server"]
```

### 5.8 Podman

Podman 與 Docker 指令高度相容，上述 Dockerfile 可直接以 `podman build` / `podman run` 建置與執行（建議架構，Semantica 官方文件未特別提及 Podman）：

```bash
podman build -t semantica-server:0.6.5 .
podman run -d --name semantica -p 8000:8000 -v semantica_data:/data semantica-server:0.6.5
```

### 5.9 Kubernetes（概覽，完整生產部署見第 29 章）

v0.5.1 起提供 Knowledge Explorer 的 K8s 部署範本（官方已實作），但涵蓋範圍限於 Explorer 視覺化元件，**不是完整生產級 HA 部署藍圖**。企業自行設計 Deployment/Service/Ingress 時，請參考第 29 章的建議架構。

### 5.10 驗證安裝

```bash
semantica --help
semantica doctor
python -c "import semantica; print(semantica.__version__)"
```

`semantica doctor` 提供健康檢查（官方已實作，README 命令清單），建議每次安裝後立即執行，確認相依套件、LLM Provider Key、Graph/Vector Store 連線狀態正常。

### 5.11 企業推薦安裝方式對照表

| 環境 | 建議方式 | 理由 |
|---|---|---|
| 開發者本機 | venv + 精準 extras | 快速迭代，避免污染系統 Python |
| CI/CD | Docker（自建映像） | 可重現、可版本化 |
| 正式環境（單機/小規模） | Docker/Podman + 外接 Graph/Vector Store | 隔離、易於備份 |
| 正式環境（企業規模） | Kubernetes（見第 29 章） | 可水平擴充、可搭配既有 K8s 維運體系 |

### 5.12 Troubleshooting 速查（完整版見第 42 章）

| 症狀 | 可能原因 | 解法 |
|---|---|---|
| `pip install semantica[all]` 在 Windows 失敗 | 版本早於 v0.5.0，或缺少 VC++ Redistributable | 升級至 v0.5.0+，安裝 VC++ Redistributable |
| `import semantica` 找不到模組 | 未啟動虛擬環境 | 確認 `venv\Scripts\activate`（Windows）或 `source venv/bin/activate`（Linux/Mac） |
| GPU 相關套件安裝失敗 | CUDA 版本不相容 | 改用 CPU-only 安裝，或對齊官方支援的 CUDA 版本 |

### 5.13 本章 Checklist 與小結

- [ ] 已在目標作業系統成功執行 `python -c "import semantica; print(semantica.__version__)"`
- [ ] 已依實際需求選擇精準 extras，而非無腦裝 `[all]`
- [ ] 已執行 `semantica doctor` 確認環境健康
- [ ] 已決定正式環境的容器化策略（Docker/Podman/K8s）

---

## 6. Configuration（設定）

### 6.1 官方已確認的環境變數

（官方已實作，`docs.getsemantica.ai/cli-setup` 與 MCP Server 文件）

| 環境變數 | 用途 | 何時需要 | Production 建議 |
|---|---|---|---|
| `SEMANTICA_KG_PATH` | 指向持久化 Knowledge Graph 檔案的路徑 | MCP Server／需要跨 Session 持久化時 | 使用絕對路徑，避免相對路徑在不同工作目錄下失效 |
| `SEMANTICA_LOG_LEVEL` | 日誌詳細程度（DEBUG/INFO/WARNING） | 除錯或降低正式環境日誌量 | 正式環境建議 `INFO`，除錯時暫時調成 `DEBUG` |
| `SEMANTICA_CORS_ORIGINS` | REST API 允許的 CORS 來源（逗號分隔） | `semantica-server` 對外提供服務時 | 正式環境務必明確列出白名單網域，切勿設為 `*` |

### 6.2 Provenance 儲存設定

`ProvenanceManager` 支援 in-memory 或 SQLite 持久化（官方已實作，`docs.getsemantica.ai/guides/provenance`）：

```python
from semantica.provenance import ProvenanceManager

# 開發／測試：記憶體模式，重啟即遺失
prov = ProvenanceManager()

# 正式環境：SQLite 持久化，官方建議
prov = ProvenanceManager(storage_path="provenance.db")
```

SQLite 後端使用 Write-Ahead Logging、原子交易，支援並發讀取（官方已實作）。企業導入建議：**正式環境一律使用 `storage_path`**，否則稽核軌跡會在服務重啟後遺失，違背 Provenance 存在的意義（建議架構）。

### 6.3 LLM Provider 設定

Semantica 透過 `semantica.llms` + LiteLLM 支援多家 LLM Provider（官方已實作，README）：OpenAI、Anthropic Claude、Google Gemini、Mistral、Meta Llama、Groq、Cohere、Azure OpenAI、AWS Bedrock、Ollama、DeepSeek、HuggingFace。

設定方式遵循各 LLM Provider 慣例（例如 `OPENAI_API_KEY`、`ANTHROPIC_API_KEY` 等環境變數），細節請以 LiteLLM 官方文件與 Semantica 對應版本的 `semantica.llms` 原始碼為準（Source-confirmed——本手冊查證時官方文件未列出 Semantica 專屬的 LLM Key 環境變數命名慣例，可能直接沿用各 Provider SDK 的標準命名）。

**Security 注意事項**：LLM API Key 絕對不可寫死於程式碼或 commit 進 Git；企業建議透過 Secret Manager（Vault、AWS Secrets Manager、Kubernetes Secret）注入環境變數（建議架構，見第 24 章）。

### 6.4 Graph / Vector Store Backend 設定

依選用後端不同，設定方式也不同，範例（示意，依官方模組介面重新整理）：

```python
# Vector Store：選用 PgVector 而非預設 in-memory
from semantica.vector_store import VectorStore

vs = VectorStore(
    backend="pgvector",
    connection_string="postgresql://user:pass@localhost:5432/semantica",
    dimension=1536,
)
```

```python
# Graph Store：選用 Neo4j 而非預設 in-memory
# 需先 pip install semantica[graph-neo4j]
from semantica.kg import GraphBuilder

builder = GraphBuilder(
    backend="neo4j",
    uri="bolt://localhost:7687",
    auth=("neo4j", "password"),
)
```

> 上列兩段程式碼為**示意**，實際建構子參數名稱請以你安裝版本的 `help(VectorStore)` / `help(GraphBuilder)` 為準（Source-confirmed）。

### 6.5 Policy Engine 設定（governance，非傳統 access control）

官方 Policy Engine（官方已實作，`docs.getsemantica.ai/guides/policy-engine`）用來檢查決策是否符合預先定義的規則，但**明確不會自動阻擋動作**：

> "Policy evaluation returns compliance status (`True`/`False`) but does not automatically block actions."（官方已實作）

```python
from semantica.policy import Policy  # 示意 import 路徑，請以實際版本模組路徑為準

attribution_policy = Policy(
    policy_id="pol-attr-001",
    name="Nation-State Attribution",
    rules={
        "min_independent_sources": 2,
        "required_approver_role": "senior_analyst",
        "allowed_outcomes": ["nation_state_attributed"],
        "min_confidence": 0.85,
    },
)
```

**重要限制**（官方已實作）：以下規則型別**不支援**，使用會導致非預期行為：`disallowed_outcomes`、`mandatory_fields`、`requires_mfa`、複雜巢狀條件。企業設計 Policy 時務必只用官方支援的 `min_*` / `max_*` / `required_*` / `allowed_outcomes` 模式。

### 6.6 Configuration 完整性總表

| 設定目的 | 何時需要 | 預設值 | Production 建議 | Security 注意事項 |
|---|---|---|---|---|
| Provenance 持久化 | 需要跨重啟保留稽核軌跡 | in-memory（不持久化） | 一律設定 `storage_path` | SQLite 檔案需納入備份策略（第 28 章） |
| KG 檔案路徑 | MCP Server 或需要載入既有圖 | 未設定則使用預設暫存路徑 | 使用絕對路徑 | 檔案存取權限需限縮給執行 Semantica 的服務帳號 |
| CORS 白名單 | REST API 對外服務 | 依實作可能預設寬鬆 | 明確列出白名單網域 | 切勿設為 `*`，避免 CSRF/資料外洩風險 |
| LLM Provider Key | 使用 LLM-based extraction/reasoning | 無 | 透過 Secret Manager 注入 | 絕不可 commit 進版控 |
| Graph/Vector Store 連線字串 | 使用外部後端而非 in-memory | in-memory | 使用 Secret 管理連線密碼 | 開啟 TLS，限制網路存取來源 |

### 6.7 本章 Checklist 與小結

- [ ] 已確認正式環境 `ProvenanceManager` 使用 `storage_path` 持久化，而非預設 in-memory
- [ ] LLM API Key、DB 連線密碼皆透過 Secret Manager 注入，未寫死於程式碼
- [ ] `SEMANTICA_CORS_ORIGINS` 已設定明確白名單（若對外提供 REST API）
- [ ] Policy Engine 規則只使用官方支援的規則型別（避免 `disallowed_outcomes` 等不支援型別）

---

## 7. Knowledge Graph 建模與軟體開發 Ontology 設計

### 7.1 基本建模元素

（官方已實作，`semantica.kg` / `ContextGraph` API）

- **Node（節點）**：代表一個 Entity（實體），例如一個 Class、一個 API、一個 Requirement。
- **Edge（邊）**：代表 Relationship（關係），有方向性，例如 `CALLS`、`DEPENDS_ON`。
- **Property（屬性）**：節點或邊上的鍵值屬性，例如 `confidence`、`source_id`、`created_at`。
- **Event / Fact**：由 `EventDetector` / `TripletExtractor` 抽取出的結構化陳述。
- **Source**：每個節點/邊皆攜帶 `source_id`，回指原始文件（Provenance by Default，見 4.4 節）。
- **Decision / Agent / Activity**：Decision Intelligence（第 11 章）與 Provenance（第 12 章）的一級公民節點型別。
- **Version / Temporal Fact**：Bi-temporal 模型下同一實體的歷史版本（第 9 章）。

### 7.2 官方 API 範例：建立節點與邊

（官方已實作，`docs.getsemantica.ai/guides/context-graphs`）

```python
from semantica.context import ContextGraph

graph = ContextGraph(advanced_analytics=True)

graph.add_node("APT29", "ThreatActor", "Russian state-sponsored group",
               origin="Russia", motivation="espionage")
graph.add_edge("APT29", "SUNBURST", "uses", weight=1.0)

neighbors = graph.get_neighbors("APT29", hops=2)
graph.save_to_file("cti_graph.json")
```

### 7.3 軟體開發專用 Ontology 設計（建議架構）

Semantica 官方沒有內建「軟體開發 Ontology」，這是本手冊針對第 19-21 章三大情境原創設計的實體與關係模型，用於統一 Requirement → Code → Test → Deployment 的知識表示：

**實體類型（Node Types）**：

```text
Project · System · Application · Module · Package · Class · Method · API
Database · Table · Column · Requirement · BusinessRule · ArchitectureDecision
Technology · Framework · Version · Dependency · Test · Deployment
Agent · Decision · Evidence · Source · Document
```

**關係類型（Edge Types）**：

```text
DEPENDS_ON · CALLS · IMPLEMENTS · EXPOSES · READS · WRITES · USES
DEFINED_BY · IMPLEMENTS_REQUIREMENT · TESTED_BY · DEPLOYED_TO
MIGRATED_TO · REPLACED_BY · CAUSED_BY · SUPPORTED_BY · DERIVED_FROM · DECIDED_BY
```

### 7.4 Mermaid：軟體開發 Ontology 關係圖（建議架構）

```mermaid
erDiagram
    Requirement ||--o{ BusinessRule : "IMPLEMENTS_REQUIREMENT"
    BusinessRule ||--o{ ArchitectureDecision : "DECIDED_BY"
    ArchitectureDecision ||--o{ CodeClass : "DEFINED_BY"
    CodeClass ||--o{ Method : "CONTAINS"
    Method ||--o{ API : "EXPOSES"
    API ||--o{ Database : "READS/WRITES"
    CodeClass ||--o{ Test : "TESTED_BY"
    CodeClass ||--o{ Deployment : "DEPLOYED_TO"
    CodeClass ||--o{ Dependency : "DEPENDS_ON"
    Method ||--o{ Method : "CALLS"
```

### 7.5 建立範例：把 Requirement 到 Code 的鏈路寫進 Context Graph

```python
# 示意程式碼，示範如何用官方 ContextGraph API 承載本手冊的軟體開發 Ontology
from semantica.context import ContextGraph

graph = ContextGraph(advanced_analytics=True)

graph.add_node("REQ-1024", "Requirement", "支援信用卡分期付款")
graph.add_node("BR-018", "BusinessRule", "分期期數上限 24 期，最低金額 3000 元")
graph.add_node("AD-007", "ArchitectureDecision", "使用 Strategy Pattern 實作分期計算")
graph.add_node("InstallmentController", "Class", "com.bank.payment.InstallmentController")
graph.add_node("calculateInstallment", "Method", "計算分期金額")

graph.add_edge("BR-018", "REQ-1024", "IMPLEMENTS_REQUIREMENT")
graph.add_edge("AD-007", "BR-018", "DECIDED_BY")
graph.add_edge("InstallmentController", "AD-007", "DEFINED_BY")
graph.add_edge("calculateInstallment", "InstallmentController", "CONTAINS")
```

### 7.6 Scenario：新進工程師理解遺留系統

> 新人被指派修改 `InstallmentController`，透過 GraphRAG 查詢（第 15 章）「這個 Class 依據哪個 Business Rule？該規則的來源需求是什麼？」，Context Graph 直接回傳 REQ-1024 → BR-018 → AD-007 → InstallmentController 的完整鏈路，取代翻找過期 Confluence 文件。

### 7.7 本章 Checklist 與小結

- [ ] 已理解 Node/Edge/Property 是 Semantica KG 的基本建模單位
- [ ] 已理解本手冊的軟體開發 Ontology 屬於「建議架構」，非 Semantica 官方內建 Schema
- [ ] 已能設計出自己團隊的實體/關係類型清單（可從第 7.3 節清單增刪）

---

## 8. Entity Resolution 與 Conflict Detection

### 8.1 問題起點

同一個實體常常以多種形式出現：

```text
Customer
CUSTOMER
customer_id
CRM Customer
Core Banking Customer
```

若不做 Entity Resolution，Knowledge Graph 會產生大量重複節點，破壞 Graph Analytics（第 14 章）的準確性。

### 8.2 官方 Deduplication API

（官方已實作，`docs.getsemantica.ai/guides/deduplication`／README）

```python
from semantica.deduplication import DuplicateDetector, EntityMerger

detector = DuplicateDetector(similarity_threshold=0.75, use_clustering=True)
groups = detector.detect_duplicate_groups(entities)

merger = EntityMerger(preserve_provenance=True)
ops = merger.merge_duplicates(entities, strategy="keep_most_complete")
```

官方支援四種比對策略，從快速的 Jaro-Winkler 字串相似度基準，到 **hybrid_v2**（Blocking + 語意 Embedding 比對，適合混合型資料）（官方已實作，Concepts 頁面摘要）。`preserve_provenance=True` 確保合併後仍能追溯每個原始來源（呼應第 12 章 Provenance）。

### 8.3 Conflict Detection：不應該因為衝突就直接覆蓋

官方明確設計哲學（官方已實作，`docs.getsemantica.ai/guides/conflict-resolution`）：

> 當來源之間有分歧時，Semantica「flags and resolves the conflict rather than silently picking one value」——標記並解決衝突，而非靜默選擇其中一個值。

```python
from semantica.conflicts import ConflictDetector, ConflictResolver

detector = ConflictDetector()
conflicts = detector.detect_conflicts(entities_from_multiple_sources)

resolver = ConflictResolver()
resolved = resolver.resolve_conflicts(conflicts, strategy="credibility_weighted")
resolved = resolver.resolve_conflicts(conflicts, strategy="most_recent")
```

支援的衝突型別（官方已實作）：value（數值）、type（型別）、relationship（關係）、temporal（時間）、logical（邏輯）衝突。解決策略包含 credibility-weighted（來源可信度加權）、most-recent（最新優先）、voting（多數決）。

### 8.4 概念模型：保留衝突，而非覆蓋

```text
Fact A ── Source A ── Timestamp A
Fact B ── Source B ── Timestamp B
        ↓
     Conflict
        ↓
  Resolution Strategy
        ↓
   Final Assertion（同時保留原始 Fact A / Fact B 的 Provenance）
```

### 8.5 為什麼這對銀行、金融、醫療系統特別重要

若 CRM 系統與核心銀行系統對同一位客戶的「信用評等」記錄不同值，直接覆蓋會讓稽核人員永遠無法重建「當初核貸決策當下看到的是哪個評等」。Semantica 的 Conflict Detection + Provenance 組合，讓企業可以誠實地保留兩個 Fact，並記錄「當時採用哪一個、為什麼」（建議架構，結合官方 Provenance／Conflict 模組的企業解讀）。

### 8.6 AI Prompt 範例

```text
以下是同一個 Customer 實體在 CRM 與核心銀行系統的兩筆記錄，欄位值不同。
請使用 ConflictDetector 找出衝突欄位，並用 credibility_weighted 策略解決，
但保留兩筆原始 Fact 的 Provenance，不要直接覆蓋。輸出你選擇的最終值與理由。
```

### 8.7 本章 Checklist 與小結

- [ ] 已理解 Entity Resolution 與 Conflict Detection 是兩個不同但相關的步驟
- [ ] 已知道官方支援的 4 種相似度比對策略與 3 種衝突解決策略
- [ ] 團隊的衝突解決策略已明確定義（不是預設「後寫入者覆蓋」）

---

## 9. Temporal Intelligence

### 9.1 核心概念

（官方已實作，`docs.getsemantica.ai/concepts`，v0.4.0 起完整 bi-temporal 堆疊）

- **Valid Time**：事實在現實世界中成立的時間範圍
- **Transaction Time**：系統記錄該事實的時間（`recorded_at`）
- **Bi-temporal Data**：同時追蹤 Valid Time 與 Transaction Time，兩者不必相同（例如「上週才發現這筆交易其實在三個月前就已違規」）
- **Time Travel / Historical State**：查詢某個時間點的圖狀態
- **Allen Interval Algebra**：官方支援全部 13 種時間區間關係（BEFORE、MEETS、OVERLAPS、DURING、EQUALS 等）（官方已實作，Reasoning Guide）

### 9.2 官方 API

```python
from semantica.kg import BiTemporalFact, TemporalGraphQuery
from datetime import datetime

fact = BiTemporalFact(
    valid_from=datetime(2024, 3, 1),
    valid_until=datetime(2025, 1, 1),
    recorded_at=datetime(2024, 3, 5),
)

# Point-in-time 快照
snapshot = graph.state_at("2024-01-01")

# 時間範圍查詢
tq = TemporalGraphQuery()
facts = tq.query_time_range(kg, start_time="2024-01-01", end_time="2024-12-31")
```

### 9.3 Scenario：Framework Upgrade 的版本歷史保留

> 企業要從 Spring Boot 3.5 升級到 Spring Boot 4.x，過程中需要同時保留「升級前」與「升級後」兩個版本的 API 依賴關係圖，才能在升級失敗時快速比對回滾範圍。

```python
# 示意：用 Bi-temporal Fact 表示同一個依賴關係在升級前後的狀態
graph.add_node("spring-boot-3.5", "Version", "Spring Boot 3.5.x")
graph.add_node("spring-boot-4.0", "Version", "Spring Boot 4.0.x")

fact_before = BiTemporalFact(
    valid_from=datetime(2025, 1, 1),
    valid_until=datetime(2026, 6, 1),   # 升級專案啟動日
    recorded_at=datetime(2025, 1, 1),
)
fact_after = BiTemporalFact(
    valid_from=datetime(2026, 6, 1),
    valid_until=None,                    # 目前仍有效
    recorded_at=datetime(2026, 6, 1),
)
```

同樣的模型可套用在 Java 21 → Java 25 升版案例（第 21 章）。

### 9.4 本章 Checklist 與小結

- [ ] 已理解 Valid Time 與 Transaction Time 的差異
- [ ] 已能用 Bi-temporal Fact 表示「升級前/升級後」兩個版本並存的狀態
- [ ] 已知道 `state_at()` 可做 Point-in-time 快照查詢，適合稽核情境

---

## 10. Reasoning Engine

### 10.1 LLM Reasoning vs Deterministic Graph Reasoning

企業關鍵規則（例如授信門檻、法規門檻）不應完全交給 LLM 自由發揮——LLM 的推理結果無法保證可重現、可驗證。Semantica 提供 **8 種互補的推理引擎**（官方已實作，`docs.getsemantica.ai/guides/reasoning`），核心哲學是：

> AI Agent 可以負責提出假設，但企業關鍵規則應盡量由 deterministic engine 驗證（建議架構，基於官方 Reasoning Guide 的企業解讀）。

```mermaid
flowchart TB
    LLM2["LLM"] --> HYPO["Hypothesis（假設）"]
    HYPO --> SEM2["Semantica"]
    SEM2 --> RULES["Rules（規則）"]
    RULES --> EVID["Evidence（證據）"]
    EVID --> DETVAL["Deterministic Validation"]
    DETVAL --> DECISION2["Decision"]
```

### 10.2 官方 8 種推理模式

（官方已實作，`docs.getsemantica.ai/guides/reasoning`）

| 引擎 | 用途 | 對應類別 |
|---|---|---|
| Forward Chaining | 從既有事實反覆套用規則，直到無新結論（fixpoint） | `Reasoner.forward_chain()` |
| Backward Chaining | 從目標往回推導，找出最小證明鏈 | `Reasoner.backward_chain()` |
| Datalog | 任意深度的遞迴推理（Horn clause） | `DatalogReasoner` |
| SPARQL | 對已推理豐富化的 working memory 做三元組查詢 | `SPARQLReasoner` |
| RETE | 高效評估 100+ 條規則集的 alpha/beta network 演算法 | `ReteEngine` |
| Temporal | Allen 13 種時間區間關係推理 | `TemporalReasoningEngine` |
| LLM-based | 以圖為 grounded context 的自由格式查詢 | `GraphReasoner` |
| Explanation | 把推理結果轉為自然語言說明 | `ExplanationGenerator` |

### 10.3 Forward Chaining 範例（官方已實作）

```python
reasoner = Reasoner()  # 示意，實際 import 路徑請以你安裝版本為準
reasoner.add_fact("ThreatActor(APT29)")
reasoner.add_fact("Exploits(APT29, CVE-2025-3400)")
reasoner.add_rule("IF ThreatActor(X) AND Exploits(X, Y) AND CriticalVuln(Y) THEN HighRiskActor(X)")

derived = reasoner.forward_chain()
```

### 10.4 Rete 規則引擎範例（README 逐字，官方已實作）

```python
from semantica.reasoning import ReteEngine, Rule, Fact, RuleType

rete = ReteEngine()
rete.build_network([
    Rule(
        rule_id="aml_flag",
        name="Flag high-risk transactions",
        conditions=[
            {"field": "amount", "operator": ">", "value": 10_000},
            {"field": "country", "operator": "in", "value": ["IR", "KP", "SY"]},
        ],
        conclusion="flag_for_compliance_review",
        rule_type=RuleType.IMPLICATION,
    ),
])

rete.add_fact(Fact("tx_001", "transaction", [{"amount": 15_000, "country": "IR"}]))
flagged = rete.match_patterns()
```

### 10.5 Datalog 範例（README 逐字，官方已實作）

```python
from semantica.reasoning import DatalogReasoner

engine = DatalogReasoner()
engine.add_fact("parent(tom, bob)")
engine.add_rule("ancestor(X, Y) :- parent(X, Y).")
engine.add_rule("ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).")
ancestors = engine.query("ancestor(tom, ?X)")
```

### 10.6 Explanation Generator：可解釋的推理路徑

（官方已實作）`ExplanationGenerator` 把任何 `InferenceResult` 轉為人類可讀的說明、逐步 `ReasoningPath`、以及帶有支持證據的 `Justification`，支援 simple/detailed/verbose 三種詳細程度。`InferenceResult` 攜帶 `conclusion`、`confidence`、`premises`（支持事實）、`rule_used`（觸發的規則）。

### 10.7 使用時機與常見陷阱

（官方已實作，Reasoning Guide 摘要）

**適合使用推理引擎**：複雜的邏輯關係網域、政策執行、需要可解釋性的多步驟推理、隱含關係偵測。

**常見陷阱**：在簡單查詢上過度使用推理引擎、圖資料品質差會被推理放大、把「推理出的事實」誤當成「已驗證的事實」、規則過度複雜、在大型資料集上使用無界遞迴。

### 10.8 Scenario：Framework Upgrade 的 Deterministic 驗證

> AI Agent 提出假設：「這個 Controller 應該替換成 Spring Boot 4.x 的新 API」。Semantica 用 Forward Chaining 套用預先定義的 Migration Rule（第 21 章），驗證這個假設是否符合官方 Breaking Change 清單，才允許 Agent 真正修改程式碼。

### 10.9 本章 Checklist 與小結

- [ ] 已理解 LLM Reasoning（假設提出）與 Deterministic Reasoning（規則驗證）的分工
- [ ] 已知道 8 種推理引擎各自的適用情境
- [ ] 企業關鍵規則（授信、法規、安全）已設計對應的 Forward Chaining / Rete 規則，而非完全交給 LLM 判斷

---

## 11. Decision Intelligence

本章是全書最重要的章節之一：把「AI Agent 做了什麼決定」變成一個可查詢、有因果鏈、可稽核的 Graph 節點。

### 11.1 核心模型

```text
Decision → Reasoning → Evidence → Source → Cause → Outcome → Downstream Impact
```

官方明確定位（官方已實作，`docs.getsemantica.ai/guides/decision-intelligence`）：

> 「Every agent decision is a first-class object in Semantica: recorded, causally linked, and searchable by precedent.」

### 11.2 `record_decision()` 完整簽章

（官方已實作，`docs.getsemantica.ai/guides/decision-intelligence`；README Quickstart 範例與此一致）

```python
context.record_decision(
    category: str,           # 決策類型（例如 "threat_classification"、"vendor_selection"）
    scenario: str,           # 情境描述
    reasoning: str,          # 決策理由
    outcome: str,            # 結果或採取的行動
    confidence: float,       # 0.0–1.0 信心分數
    decision_maker: str,     # 做決策的 Agent/元件識別碼
    entities: list = None,   # 選填，相關實體清單
)
# 回傳：該決策節點的 UUID 字串
```

> ⚠️ **版本命名差異提醒**：README 的簡化 Quickstart 範例僅示範 `category` / `scenario` / `reasoning` / `outcome` / `confidence` 五個參數；`docs.getsemantica.ai` 的 Decision Intelligence Guide 額外列出 `decision_maker` 與 `entities`。兩者並不衝突（後者是更完整的簽章），但**查詢類方法名稱在不同官方頁面出現過 `find_similar_decisions()`（README）與 `find_precedents()`（Guide）兩種名稱**，本手冊研判為同一能力的別名或版本間命名調整，正式導入前請務必以你安裝版本執行 `dir(context)` 或 `help(context.record_decision)` 逐一核對實際可用的方法名稱（Source-confirmed）。

### 11.3 決策查詢與因果追溯 API

```python
# 尋找相似的既有決策（README 命名）
similar = graph.find_similar_decisions("cloud vendor", max_results=5)

# 尋找先例（Guide 命名，混合 70% 語意相似 + 30% 圖鄰近度）
precedents = context.find_precedents(query_text="cloud vendor selection", limit=5)

# 因果鏈追溯（上游/下游）
chain = context.get_causal_chain(decision_id="...", direction="upstream", max_depth=3)

# 決策影響分析
impact = graph.analyze_decision_impact(decision_id="...")

# 政策合規檢查
compliant = graph.check_decision_rules({"category": "vendor_selection"})

# 完整稽核情境（含連結數、上下游決策清單）
explainability = context.trace_decision_explainability(decision_id="...")

# 進階因果分析（含信心衰減指標，例如「2-hop 距離，信心衰減至 84%」）
causality = context.trace_decision_causality(decision_id="...")

# 決策統計洞察
insights = graph.get_decision_insights()
# 回傳：total_decisions、confidence_stats、categories、outcomes 分布
```

### 11.4 完整範例（README 逐字，官方已實作）

```python
from semantica.context import ContextGraph

graph = ContextGraph(advanced_analytics=True)

decision_id = graph.record_decision(
    category="vendor_selection",
    scenario="Choose cloud provider for HIPAA workload",
    reasoning="AWS offers BAA, mature HIPAA tooling, existing team expertise",
    outcome="selected_aws",
    confidence=0.93,
)

chain = graph.trace_decision_chain(decision_id)        # 因果世系
similar = graph.find_similar_decisions("cloud vendor", max_results=5)
impact = graph.analyze_decision_impact(decision_id)    # 下游影響
compliant = graph.check_decision_rules({"category": "vendor_selection"})
```

### 11.5 實際案例：AI Agent 決定修改 Spring Boot Controller

> Scenario：AI Agent 在 Framework Upgrade 專案中，需要把 `PaymentController` 的 `@RequestMapping` 改為 Spring Boot 4.x 建議的 `@Mapping` 精簡註解。

```mermaid
sequenceDiagram
    participant Agent as AI Agent
    participant KG as Knowledge Graph
    participant Sem as Semantica
    Agent->>KG: 查詢 PaymentController 相關 Context
    KG-->>Agent: 回傳依賴的 API、Migration Rule、Breaking Change 節點
    Agent->>Sem: 查詢 Evidence（官方 Migration Guide 條目）
    Sem-->>Agent: 回傳官方文件引用
    Agent->>Agent: 進行決策（是否替換、如何替換）
    Agent->>Sem: record_decision(category="framework_migration", ...)
    Sem->>KG: 建立 causal relationship（AD 決策 → PaymentController Class 節點）
    Sem-->>Agent: 回傳 decision_id，可供後續 audit trail 查詢
```

```python
# 示意：延續 Quickstart 模式，記錄一次 Framework Upgrade 決策
decision_id = graph.record_decision(
    category="framework_migration",
    scenario="Spring Boot 3.x -> 4.x：PaymentController 使用已棄用的 @RequestMapping 全參數形式",
    reasoning=(
        "官方 Spring Boot 4.0 Migration Guide 明確標示 @RequestMapping(method=...) "
        "為 deprecated，建議替換為 @GetMapping/@PostMapping 精簡註解；"
        "本專案已於 Impact Analysis（第 21 章）確認僅影響 3 個下游 API 呼叫端"
    ),
    outcome="replaced_with_get_post_mapping",
    confidence=0.91,
    decision_maker="migration-agent-01",
    entities=["PaymentController", "spring-boot-4.0-migration-guide"],
)
```

### 11.6 本章 Checklist 與小結

- [ ] 已能寫出符合官方簽章的 `record_decision()` 呼叫
- [ ] 已理解 `trace_decision_chain` / `get_causal_chain` / `analyze_decision_impact` 分別回答什麼問題
- [ ] 已知道 README 與官方 Guide 的方法命名可能有差異，導入前務必以實際安裝版本核對
- [ ] 團隊已定義：哪些 AI Agent 決策「必須」呼叫 `record_decision()`（建議：所有會修改生產程式碼、資料庫、部署設定的決策）

---

## 12. Provenance／W3C PROV-O

### 12.1 「可追溯」不等於「可解釋」

企業導入時最容易混淆的五個詞（建議架構，基於官方 Provenance Guide 的企業解讀）：

| 概念 | 定義 | Semantica 對應能力 |
|---|---|---|
| Traceability（可追溯性） | 能否找到資料的來源 | `ProvenanceManager.get_lineage()` |
| Explainability（可解釋性） | 能否用人類可理解的方式說明「為什麼」 | `ExplanationGenerator`（第 10 章） |
| Auditability（可稽核性） | 第三方能否獨立驗證整個決策過程 | Provenance + Decision Intelligence 組合 |
| Reproducibility（可重現性） | 同樣輸入是否能重現同樣結論 | Deterministic Reasoning（第 10 章），LLM 部分無法完全保證 |
| Accountability（可問責性） | 是否能明確歸屬「誰／哪個 Agent／依據什麼政策」做出決策 | Decision Intelligence + Policy Engine（第 11、6.5 節） |

一份「完美記錄來源」的 Provenance 鏈，資料本身仍可能是錯的——官方原文明確提醒（官方已實作，`docs.getsemantica.ai/guides/provenance`）：

> "Provenance records faithfully document where data came from, but do not verify source accuracy."

### 12.2 W3C PROV-O 映射表

（官方已實作）

| PROV-O 詞彙 | ProvenanceEntry 欄位 | 用途 |
|---|---|---|
| `prov:Entity` | `entity_id` | 被追蹤的物件 |
| `prov:Activity` | `activity_id` | 產生該物件的流程 |
| `prov:Agent` | `agent_id`, `agent_type` | 誰／什麼執行了該活動 |
| `prov:wasGeneratedBy` | （衍生欄位） | Entity → Activity 連結 |
| `prov:wasDerivedFrom` | `parent_entity_id`, `derived_from_id` | 世系前驅 |
| `prov:used` | `used_entities` | 該活動消費的實體 |
| `prov:generatedAtTime` | `timestamp` | ISO 日期時間 |
| `prov:qualifiedInvalidation` | `invalidated`, `invalidation_reason` | 撤回記錄 |
| `prov:Bundle` | `bundle_id` | 依攝取批次分組 |

Checksum 欄位是 Semantica 的擴充（非 PROV-O 標準詞彙）：每筆記錄的 SHA-256 校驗碼包含前一筆記錄的校驗碼，形成串接式的完整稽核鏈（官方已實作）。

### 12.3 `ProvenanceManager` 核心方法

（官方已實作，`docs.getsemantica.ai/guides/provenance`）

| 方法 | 功能 |
|---|---|
| `track_entity()` | 記錄實體，附來源、時間戳、信心分數；重複呼叫會建立版本鏈（存檔前次記錄） |
| `track_property_source()` | 把個別屬性值歸因到特定來源，支援多來源衝突偵測 |
| `get_lineage(entity_id)` | 取得完整版本歷史（`first_seen`/`last_updated`/`lineage_chain`） |
| `trace_lineage(entity_id, max_depth=None)` | 取得原始 Provenance 記錄鏈，供完整性驗證 |
| `track_chunk()` | 記錄來源片段（byte range、`parent_chunk_id`），對應 `prov:wasDerivedFrom`，是 GDPR 刪除工作流程的關鍵 |
| `track_relationship()` | 邊（關係）的 Provenance，簽章類似 `track_entity()`，KG 抽取流程會自動呼叫 |
| `get_all_sources(property_key)` | 多來源比對，回傳 source/confidence/location 清單 |
| `get_statistics()` | 稽核摘要：`total_entries`、`entity_types`、`unique_sources` |
| `verify_chain(entity_id)` | 完整性驗證，走訪整條 Provenance 鏈偵測竄改 |
| `invalidate(entity_id, reason)` | 撤回/更正，**永不硬刪除**（符合 21 CFR Part 11 等稽核需求），改記錄 tombstone |

### 12.4 完整範例：CVE 追蹤（官方已實作，SOC 使用案例）

```python
from semantica.provenance import ProvenanceManager

prov = ProvenanceManager(storage_path="soc_provenance.db")

# 初始 NVD 攝取
prov.track_entity(
    entity_id="cve-2023-44487",
    source="NVD_feed_2023-10-10",
    metadata={"cvss_score": 7.5},
    confidence=0.98,
    entity_type="vulnerability",
    activity_id="nvd_feed_ingestion",
)

# 六週後：NVD 更新分數
prov.track_entity(
    entity_id="cve-2023-44487",
    source="NVD_feed_2023-11-22",
    metadata={"cvss_score": 7.5, "known_exploited": True},
    confidence=0.98,
    entity_type="vulnerability",
    activity_id="nvd_feed_update",
)

lineage = prov.get_lineage("cve-2023-44487")
print(f"First seen: {lineage['first_seen']}")
print(f"Last updated: {lineage['last_updated']}")
for entry in lineage["lineage_chain"]:
    print(f"  [{entry['timestamp'][:19]}] {entry['source_document']}")
```

### 12.5 企業案例：Requirement → Deployment 的 Provenance Graph

```mermaid
flowchart LR
    REQ["Requirement<br/>REQ-1024"] -->|"wasDerivedFrom"| AD["Architecture Decision<br/>AD-007"]
    AD -->|"wasAssociatedWith"| ACT["AI Agent Activity<br/>coding-agent-03"]
    ACT -->|"used"| SRC["Source File<br/>InstallmentController.java"]
    ACT -->|"wasGeneratedBy"| CHANGE["Code Change<br/>commit a1b2c3d"]
    CHANGE -->|"used"| TEST["Test<br/>InstallmentControllerTest"]
    TEST -->|"wasGeneratedBy"| DEPLOY["Deployment<br/>prod-2026-08-20"]
```

### 12.6 何時不需要 Provenance（官方誠實列出的限制，官方已實作）

- 沒有合規需求的簡單原型（Simple prototypes without compliance requirements）
- 短暫、無狀態的工作流程（Ephemeral/stateless workflows）
- 高頻、低延遲、對 overhead 敏感的系統
- 單一來源、內部完全信任的資料

### 12.7 本章 Checklist 與小結

- [ ] 已能區分 Traceability／Explainability／Auditability／Reproducibility／Accountability 五個詞
- [ ] 正式環境已使用 `storage_path` 持久化 `ProvenanceManager`（呼應第 6.2 節）
- [ ] 已理解 Provenance 記錄「來源」不等於驗證「正確性」
- [ ] 已知道 `invalidate()` 是撤回機制而非刪除，符合稽核要求

---

## 13. Ontology／OWL／SHACL／SKOS

### 13.1 官方 Ontology 定義

（官方已實作，`docs.getsemantica.ai/concepts`）

> Ontology「定義你知識的 schema 與規則：存在哪些實體類型、哪些關係有效、有哪些約束條件」。

Semantica 可自動生成 Ontology，也可匯入既有 OWL/RDF 格式；v0.5.0 起在 Knowledge Explorer 新增視覺化編輯器與 SHACL 驗證（官方已實作，GitHub Release Notes）。

### 13.2 官方 API：自動生成與驗證

（README 逐字，官方已實作）

```python
from semantica.ontology import OntologyGenerator, OntologyValidator

gen = OntologyGenerator(base_uri="https://semantica.dev/ontology/")
ontology = gen.generate_ontology(data)
classes = gen.infer_classes(data)
props = gen.infer_properties(data, classes)

validator = OntologyValidator()
report = validator.validate(ontology)
# → ValidationResult(valid=True, consistent=True, satisfiable=True)
```

### 13.3 SHACL Validation（官方已實作，v0.4.0 起，`docs.getsemantica.ai/guides/shacl-validation`）

SHACL（Shapes Constraint Language）用來對圖資料強制執行結構約束。企業案例（建議架構，示範用途）：

```text
每個 API
必須有
    owner（負責團隊）
    version（版本號）
    authentication（認證機制）
    authorization（授權機制）
    test（對應測試案例）
```

```turtle
# 示意 SHACL Shape，非官方逐字語法，實際語法請以你安裝版本的 SHACL Validation Guide 為準
:APIShape a sh:NodeShape ;
    sh:targetClass :API ;
    sh:property [
        sh:path :owner ;
        sh:minCount 1 ;
    ] ;
    sh:property [
        sh:path :hasTest ;
        sh:minCount 1 ;
        sh:message "每個 API 必須至少關聯一個測試案例" ;
    ] .
```

### 13.4 SKOS（詞彙控制）

SKOS（Simple Knowledge Organization System）用於管理受控詞彙表（例如統一「客戶」「顧客」「Customer」為同一概念的同義詞集合），Semantica 提供 SKOS Vocabulary Management（官方已實作，站點導覽確認有對應 Guide 頁面存在；本手冊未逐字查證其完整 API 細節，正式使用前請查閱 `docs.getsemantica.ai` 對應頁面——Source-confirmed）。

### 13.5 銀行企業 Ontology 範例（建議架構）

```mermaid
graph TB
    Account --> Customer
    Loan --> Customer
    Credit --> Customer
    Transaction --> Account
    Payment --> Transaction
    Risk --> Customer
    Risk --> Loan
    Compliance -.->|"validates"| Transaction
    Compliance -.->|"validates"| Loan
```

### 13.6 本章 Checklist 與小結

- [ ] 已能用 `OntologyGenerator` 自動從資料推斷 Class 與 Property
- [ ] 已設計至少一條 SHACL Shape，強制關鍵實體（例如 API）必須具備治理所需欄位
- [ ] 已理解 SKOS 用於詞彙同義詞管理，與 OWL/SHACL（結構約束）用途不同

---

## 14. Graph Analytics

### 14.1 官方 API（README 逐字，官方已實作）

```python
from semantica.kg import (
    GraphBuilder,
    CentralityCalculator,
    CommunityDetector,
    PathFinder,
    LinkPredictor,
)

kg = GraphBuilder(merge_entities=True, enable_temporal=True).build(sources)

analyzer = GraphAnalyzer()
analysis = analyzer.analyze_graph(kg)

centrality = CentralityCalculator()
degree = centrality.calculate_degree_centrality(kg)
betweenness = centrality.calculate_betweenness_centrality(kg)

communities = CommunityDetector().detect_communities(kg, method="louvain")
path = PathFinder().find_shortest_path(kg, "alice_chen", "contract_001")
predictions = LinkPredictor().predict_links(kg, top_k=10)
```

### 14.2 軟體架構情境下的應用

| 分析類型 | 軟體架構問題 |
|---|---|
| Centrality（中心性） | 哪個 Class／API 是系統中最關鍵的樞紐（改動風險最高）？ |
| Community Detection（社群偵測） | 哪些 Class 實際上形成一個高耦合模組，適合拆成獨立微服務？ |
| Link Prediction（連結預測） | 兩個看似無關的模組，是否有隱藏的耦合風險？ |
| Shortest Path（最短路徑） | 從這個 Requirement 到那個 Database Table，中間經過哪些元件？ |
| Multi-hop Traversal（多跳查詢） | 修改這個 Service，三層之內會影響哪些 API？ |
| Impact Analysis（影響分析） | 完整的下游影響清單，用於升版/重構前評估（第 20、21 章） |

### 14.3 Scenario：影響分析

> 如果修改某個 Java Service，哪些 API、DB Table、Test、Frontend Module 可能受到影響？

```python
# 示意：以 PathFinder + get_neighbors 組合模擬 Impact Analysis
impacted_apis = graph.get_neighbors("PaymentService", hops=2, edge_types=["EXPOSES"])
impacted_tables = graph.get_neighbors("PaymentService", hops=2, edge_types=["READS", "WRITES"])
impacted_tests = graph.get_neighbors("PaymentService", hops=1, edge_types=["TESTED_BY"])
```

### 14.4 本章 Checklist 與小結

- [ ] 已能執行 Centrality／Community Detection／Link Prediction 三種分析
- [ ] 已能用 Multi-hop Traversal 回答「修改 X 會影響什麼」的企業問題
- [ ] 已把 Graph Analytics 結果串接進第 20、21 章的逆向工程/升版影響分析流程

---

## 15. GraphRAG

### 15.1 官方定義的檢索流程

（官方已實作，`docs.getsemantica.ai/guides/graphrag`）

```mermaid
flowchart LR
    Q["User Question"] --> ER["Entity Resolution"]
    ER --> GQ["Graph Query"]
    GQ --> MH["Multi-hop Traversal"]
    MH --> VS["Vector Search"]
    VS --> EV["Evidence"]
    EV --> LLM3["LLM"]
    LLM3 --> A["Answer（含來源引用）"]
```

官方描述：「GraphRAG 結合向量搜尋與結構化圖遍歷，過程為使用者問題 → 混合檢索實體與關係 → 帶來源標註的上下文組裝 → LLM 依據圖事實生成回答」，這消除了傳統 RAG 的幻覺與不可追溯問題（官方已實作）。

### 15.2 Traditional RAG vs GraphRAG vs Semantica GraphRAG

| 維度 | Traditional RAG | GraphRAG（通用概念） | Semantica GraphRAG |
|---|---|---|---|
| 檢索單位 | 文字片段（chunk） | 實體與關係 | 實體 + 關係 + Decision + Provenance |
| 多跳推理 | 不支援 | 支援 | 支援（Multi-hop Traversal） |
| 答案可追溯性 | 弱（僅回傳片段） | 中（回傳子圖） | 強（每個節點/邊皆有 `source_id`，見 4.4 節） |
| 決策紀錄整合 | 無 | 通常無 | 有（可查詢先前相似決策，第 11 章） |

### 15.3 何時該用 Vector Search / Graph Search / Hybrid Search（建議架構）

- **純 Vector Search**：問題本質是「找出語意相似的內容」，不需要結構化關係（例如「這份文件有沒有提過退款政策」）。
- **純 Graph Search**：問題本質是「這兩者之間有什麼關係／路徑」，例如依賴分析、影響分析。
- **Hybrid Search**：大多數企業問答場景（例如「這個 API 的權限規則是什麼，依據哪份文件」）需要同時具備語意相似與結構關係，是 Semantica 的預設優勢場景。

### 15.4 Scenario：逆向工程問答

> 工程師問：「這個 `LegacyOrderService` 有哪些隱藏的 Business Rule？」GraphRAG 先用 Entity Resolution 定位 `LegacyOrderService` 節點，Multi-hop Traversal 找出關聯的 `BusinessRule` 節點，Vector Search 補上原始 comment/commit message 中的語意線索，最後 LLM 根據這些帶來源的證據生成回答，而非憑空生成。

### 15.5 本章 Checklist 與小結

- [ ] 已理解 GraphRAG 比 Traditional RAG 多了「結構化多跳關係」與「答案可追溯到節點」
- [ ] 已能判斷什麼問題該用 Vector / Graph / Hybrid Search
- [ ] 已在第 20 章逆向工程情境實際跑過一次 GraphRAG 問答

---

## 16. MCP Server 完整介紹

### 16.1 架構：不是網路 API，而是本機 stdio Server

Semantica MCP Server 是獨立套件 `semantica-mcp`（v0.5.0 起獨立套件化，官方已實作，GitHub Release Notes），實作 Model Context Protocol（開放標準，讓 AI 助理存取本機工具與資料源）。**關鍵特性**：透過 `stdio` 通訊，而非網路連接埠，在使用者本機權限下執行，無網路曝露面（官方已實作）。

```mermaid
flowchart LR
    AGENT3["AI Agent<br/>(Claude Code / Cursor / ...)"] -->|"stdio"| MCP3["Semantica MCP Server<br/>(semantica-mcp)"]
    MCP3 --> GRAPH2["Knowledge Graph<br/>(local .json / SQLite)"]
```

### 16.2 安裝與啟動

（官方已實作，`docs.getsemantica.ai/guides/mcp-server`／`cli-setup`）

```bash
pip install semantica
semantica-mcp
# 或
python -m semantica.mcp_server
```

### 16.3 Claude Desktop / Claude Code 設定範例

（官方已實作，`docs.getsemantica.ai/guides/mcp-server`）

`claude_desktop_config.json`（macOS 路徑：`~/Library/Application Support/Claude/claude_desktop_config.json`；Windows 路徑：`%APPDATA%\Claude\claude_desktop_config.json`，Source-confirmed，官方頁面示範的是 macOS 路徑）：

```json
{
  "mcpServers": {
    "semantica": {
      "command": "semantica-mcp",
      "env": {
        "SEMANTICA_KG_PATH": "/absolute/path/to/knowledge_graph.json",
        "SEMANTICA_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

**關鍵要求**：`SEMANTICA_KG_PATH` 務必使用絕對路徑，確保跨重啟後資料仍能持久化（官方已實作）。

### 16.4 曝露的 12 個 Tools

（官方已實作，`docs.getsemantica.ai/guides/mcp-server`）

| 分類 | Tools |
|---|---|
| Extraction（抽取） | `extract_entities`、`extract_relations` |
| Graph 操作 | `add_entity`、`add_relationship` |
| Decision Intelligence | `record_decision`、`query_decisions`、`find_precedents`、`get_causal_chain` |
| Analytics／Reasoning | `run_reasoning`、`get_graph_analytics`、`get_graph_summary`、`export_graph` |

### 16.5 Read-only Resources

以下 3 個 URI 資源在官方 MCP 說明中皆可查得存在，但**本手冊 2026-08-20 重新查證時，未能獨立取得官方文件逐字確認「恰好 3 個」這個總數**（官方 MCP Reference 頁面本次查證未能完整讀取），正式導入前請直接以你安裝版本的 MCP client（例如 Claude Desktop 的 resources 列表）或官方 MCP Reference 頁面實際列出的數量為準（Source-confirmed：以下三個 URI 存在；建議自行核對總數）。

| URI | 用途 |
|---|---|
| `semantica://graph/summary` | 節點數、決策數、Server 狀態 |
| `semantica://decisions/list` | 最近最多 50 筆決策紀錄 |
| `semantica://schema/info` | Server 版本、能力、工具清單 |

### 16.6 Security Model

（官方已實作）

- **天生本機隔離**：無網路曝露，僅子行程通訊，不需要 API Key，行程在使用者的檔案權限下執行
- **Read/Write 分離**：Extract／Query 類工具偏向讀取，Manipulation／Decision-recording 類工具會寫入；具體呼叫順序由 LLM 依自然語言提示自主決定（官方已實作——這代表**企業仍需自行透過 Prompt/Policy 層限制哪些 Agent 可以呼叫寫入型工具**，MCP Server 本身不做工具層級的權限分級，見第 24 章 Security Architecture）
- **稽核**：`record_decision` 自動擷取 category、scenario、reasoning、outcome、confidence、decision maker；`get_causal_chain` 可取得上下游決策依賴，構成完整稽核鏈

### 16.7 Scenario：Claude Code 透過 MCP 查詢 Context

```mermaid
sequenceDiagram
    participant Dev as 工程師
    participant CC as Claude Code
    participant MCP as Semantica MCP
    participant KG as Knowledge Graph
    Dev->>CC: "為什麼 PaymentController 要改成這樣？"
    CC->>MCP: get_causal_chain(decision_id)
    MCP->>KG: 查詢因果鏈
    KG-->>MCP: 回傳決策節點與證據
    MCP-->>CC: 結構化結果
    CC-->>Dev: 附帶引用來源的回答
```

### 16.8 本章 Checklist 與小結

- [ ] 已完成 `semantica-mcp` 安裝與 Claude Desktop/Code 設定
- [ ] `SEMANTICA_KG_PATH` 已使用絕對路徑
- [ ] 已理解 MCP Server 本身不做工具層級權限分級，企業需另外設計限制（第 24 章）
- [ ] 已知道 12 個 Tools 與 3 個 Resources 的分類

---

## 17. AI Agent 整合

### 17.1 Claude Code

Claude Code 透過 MCP 與 Semantica 整合（官方已實作，Editor Plugin Bundle 清單包含 Claude Code）：

```mermaid
flowchart TB
    CC2["Claude Code"] --> MCP4["MCP"]
    MCP4 --> SEM3["Semantica"]
    SEM3 --> KG3["Knowledge Graph"]
    KG3 --> DP["Decision / Provenance"]
```

設定方式與第 16.3 節相同。企業導入建議：在 `CLAUDE.md` 中明確要求「涉及生產程式碼修改的決策，必須呼叫 `record_decision`」（建議架構，見第 38 章 Prompt 範本）。

### 17.2 GitHub Copilot

Semantica 官方 Editor Plugin 清單目前**未列出 GitHub Copilot**（僅列出 Claude Code、Cursor、Codex CLI、Windsurf、Cline、Continue、VS Code、OpenClaw，共 8 個——注意 VS Code 本身是編輯器，Copilot 是其上的擴充套件，兩者不完全等同）。企業若要讓 Copilot 使用 Semantica context，目前可行路徑為（建議架構）：

1. 透過 REST API（`semantica-server`，第 17.6 節）曝露查詢端點，讓 Copilot Chat 的 `@workspace` 或自訂 extension 呼叫。
2. 讓 CI/Pre-commit 流程把 Semantica 查到的相關 Context（例如相關 Requirement、Business Rule）以註解或 PR 說明形式提供給 Copilot 參考，作為間接的 Repository Context 補充。

### 17.3 Codex CLI

官方 Editor Plugin Bundle 已列出 Codex CLI（官方已實作），整合方式與 Cursor／Claude Code 類似，透過 MCP 或 Plugin 存取 Semantica Context。

### 17.4 Cursor

Cursor 支援 MCP，設定方式與 Claude Desktop 相同（在 Cursor 的 MCP 設定檔中加入 `semantica-mcp` 條目）（官方已實作）。

### 17.5 LangChain / LlamaIndex

官方定位為「透過 REST API 或 MCP 整合」，而非原生 SDK（官方已實作，README）。典型模式（建議架構，示意程式碼）：

```python
# 示意：LangChain Tool 包裝 Semantica REST API
import requests
from langchain.tools import tool

@tool
def query_semantica_decisions(category: str) -> str:
    """查詢 Semantica 中某類別的歷史決策"""
    resp = requests.get(f"http://localhost:8000/api/decisions?category={category}")
    return resp.json()
```

### 17.6 Agno（first-class 整合，README 逐字，官方已實作）

```python
from agno.agent import Agent
from agno.team import Team
from semantica.context import ContextGraph
from semantica.vector_store import VectorStore
from integrations.agno import AgnoSharedContext, AgnoKGToolkit

shared = AgnoSharedContext(
    vector_store=VectorStore(backend="faiss"),
    knowledge_graph=ContextGraph(advanced_analytics=True),
    decision_tracking=True,
)

researcher = Agent(
    name="Researcher",
    memory=shared.bind_agent("researcher"),
    tools=[AgnoKGToolkit(context=shared)],
)
# 所有 Agent 讀寫同一個 Context Graph，無需額外同步機制
```

### 17.7 CrewAI（first-class 整合）

`pip install semantica[crewai]` 提供類似的共享 Context 機制（官方已實作，README），具體 API 請以你安裝版本的 `integrations.crewai` 模組為準（Source-confirmed，本手冊未逐字查證 CrewAI 整合的完整程式碼範例）。

### 17.8 REST API 概覽

`semantica-server`（FastAPI/uvicorn，綁定 `0.0.0.0:8000`，官方已實作，`cli-setup`）提供 109 個 endpoints（Source-confirmed，來自第三方文章統計，實際數量請以你安裝版本的 OpenAPI schema `http://localhost:8000/docs` 為準）。關鍵端點分組（README 已確認）：`enrich`、`graph`、`decisions`、`reasoning`、`provenance`、`ontology`、`embeddings`、`search`、`export`、`pipeline`、`temporal`、`deduplication`。

```bash
semantica-server
curl http://localhost:8000/health
curl http://localhost:8000/api/info
```

範例端點：

```text
POST /api/enrich/extract                         — NER 與關係抽取
GET  /api/decisions?category=...                 — 查詢決策
GET  /api/graph/node/{id}/neighbors?depth=N       — 圖遍歷
POST /api/reasoning/forward-chain                 — 規則推理
```

### 17.9 整合方式總覽表

| 對象 | 整合方式 | 是否需 REST/MCP | 標示 |
|---|---|---|---|
| Claude Code | MCP + Editor Plugin | MCP | 官方已實作 |
| Cursor | MCP + Editor Plugin | MCP | 官方已實作 |
| Codex CLI | Editor Plugin | MCP | 官方已實作 |
| GitHub Copilot | 無官方原生 Plugin | REST（間接） | 建議架構 |
| LangChain / LlamaIndex | Tool 包裝呼叫 | REST／MCP | 官方已實作（整合方式），示意程式碼為本手冊原創 |
| Agno | first-class SDK | 直接 import | 官方已實作 |
| CrewAI | first-class SDK | 直接 import | 官方已實作 |
| 自研 Agent | 直接 import Python 模組或呼叫 REST | 皆可 | 官方已實作 |

### 17.10 本章 Checklist 與小結

- [ ] 已針對團隊實際使用的 Agent Framework／Editor 選定整合路徑
- [ ] 若使用 GitHub Copilot，已理解目前無官方原生整合，需透過 REST API 間接串接
- [ ] 已確認 `semantica-server` 的 CORS 設定符合第 6 章的 Security 建議

---

## 18. 企業資料 Ingestion

### 18.1 官方支援的資料源

（官方已實作，README／Architecture／Integrations 頁面）

| 類別 | 支援格式/來源 |
|---|---|
| 檔案 | PDF、DOCX、XLSX、CSV、JSON、Parquet、Apache Arrow/Feather（v0.5.1 起） |
| Web | 網頁抓取（`WebIngestor`） |
| Git | 原始碼庫（Source-confirmed 具體 Ingestor 類名，README 僅列出「Git」為支援來源之一） |
| 資料庫 | 一般資料庫連接、SQLite（v0.6.0 起） |
| 企業資料平台 | Databricks（`DatabricksIngestor`）、Snowflake（`SnowflakeIngestor`） |
| 串流 | Kafka streams（Architecture 頁面列為支援來源） |
| 文件解析加值 | Docling 整合（`/integrations/docling`，用於複雜版面 PDF 解析） |
| MCP | 可作為資料源之一（Architecture 頁面列出） |

### 18.2 Databricks Ingestion（README 逐字，官方已實作）

```python
from semantica.ingest import DatabricksIngestor

databricks = DatabricksIngestor(
    host="https://adb-xxx.azuredatabricks.net",
    token="dapi-xxxxxxxx",  # 或 OAuth M2M
    http_path="/sql/1.0/warehouses/xxxxxxxx",
    catalog="main",
)
customers = databricks.ingest_table("customers", limit=10_000)
lineage = databricks.get_table_lineage("customers")
```

### 18.3 Snowflake Ingestion（README 逐字，官方已實作）

```python
from semantica.ingest import SnowflakeIngestor

snowflake = SnowflakeIngestor(
    account="myaccount",
    user="myuser",
    password="mypassword",  # 或 key_pair、OAuth
    warehouse="COMPUTE_WH",
    database="MYDB",
)
orders = snowflake.ingest_table("ORDERS", limit=10_000)
```

### 18.4 企業 Ingestion 架構（建議架構，整合官方模組重新繪製）

```mermaid
flowchart TB
    subgraph Sources2["企業資料源"]
        S1["Git Repository"]
        S2["需求文件 (PDF/DOCX)"]
        S3["Database Schema"]
        S4["OpenAPI/Swagger 規格"]
        S5["Kafka 事件"]
        S6["Databricks/Snowflake"]
    end
    Sources2 --> ING2["semantica.ingest"]
    ING2 --> PARSE2["semantica.parse<br/>(含 Docling 複雜版面解析)"]
    PARSE2 --> NORM2["semantica.normalize"]
    NORM2 --> EXTRACT2["semantica.semantic_extract"]
    EXTRACT2 --> KG4["Knowledge Graph"]
```

### 18.5 資料正規化（README 逐字，官方已實作）

```python
from semantica.normalize import (
    TextNormalizer,
    EntityNormalizer,
    DateNormalizer,
    NumberNormalizer,
    DataCleaner,
)

text = TextNormalizer().normalize("  Acme Corp.'s Q4 report...  ")
canonical = EntityNormalizer().normalize_entity("ACME Corp.")
dt = DateNormalizer().normalize_date("3 weeks ago")
price = NumberNormalizer().normalize_number("$1.25M USD")
clean = DataCleaner().clean_data(records, remove_duplicates=True)
```

### 18.6 Pipeline DSL（README 逐字，官方已實作）

```python
from semantica.pipeline import PipelineBuilder, ExecutionEngine

builder = PipelineBuilder()
builder.add_step("ingest", step_type="ingest", source="./contracts/")
builder.add_step("extract", step_type="ner_extract")
builder.add_step("build_kg", step_type="kg_build", merge_entities=True)

pipeline = (
    builder
    .connect_steps("ingest", "extract")
    .connect_steps("extract", "build_kg")
    .set_parallelism(4)
    .build(name="contracts_pipeline")
)

engine = ExecutionEngine()
result = engine.execute_pipeline(pipeline)
```

### 18.7 本章 Checklist 與小結

- [ ] 已盤點企業實際需要接入的資料源（Git／DB／API 規格／需求文件）
- [ ] 已針對每個資料源選擇對應 Ingestor（`FileIngestor`／`DatabricksIngestor`／`SnowflakeIngestor` 等）
- [ ] 已用 Pipeline DSL 串接 Ingest → Extract → Build KG，而非手動逐步呼叫（利於排程與重跑）

---

## 19. 情境 A 實戰：AI Agent 開發 Web Application

> ⚠️ 本章 Vue3 + Spring Boot 4 銀行 Web Application 為**教學示範用途之虛構情境**（見開篇重要聲明第 6 點），示範 Semantica 與企業技術堆疊的整合模式，非真實客戶專案。

### 19.1 情境設定

企業技術堆疊：

- **Frontend**：Vue 3、TypeScript、Tailwind CSS、PrimeVue、Pinia、Vue Router、i18n、Micro Frontend / Module Federation
- **Backend**：Java 25、Spring Boot 4.x、Spring Framework 7.x、Jakarta EE、Maven、OpenAPI/Swagger、JUnit 5、ArchUnit
- **Infrastructure**：PostgreSQL、Oracle、DB2、Redis、Kafka、SFTP、Docker/Podman、Kubernetes、Jenkins、GitHub Actions、GitLab CI/CD

### 19.2 目標：建立跨開發生命週期的圖關係

```mermaid
flowchart TB
    REQ2["Requirement"] --> BR2["Business Rule"]
    BR2 --> AD2["Architecture Decision"]
    AD2 --> DM["Domain Model"]
    DM --> API2["API"]
    API2 --> DB5["Database"]
    DB5 --> CODE["Source Code"]
    CODE --> TEST2["Test"]
    TEST2 --> DEPLOY2["Deployment"]
    DEPLOY2 --> RE["Runtime Event"]
    RE --> AIDEC["AI Decision"]
    AIDEC -.->|"回饋"| BR2
```

這條鏈路直接對應第 7 章的軟體開發 Ontology（`IMPLEMENTS_REQUIREMENT`、`DECIDED_BY`、`DEFINED_BY`、`EXPOSES`、`READS`/`WRITES`、`TESTED_BY`、`DEPLOYED_TO` 等關係）。

### 19.3 Process：15 個實作步驟

1. **Requirement ingestion**：把 PRD/User Story（PDF/Confluence 匯出）用 `FileIngestor` + `NERExtractor` 匯入，建立 `Requirement` 節點。
2. **Architecture ingestion**：把 ADR（Architecture Decision Record）文件匯入，建立 `ArchitectureDecision` 節點，並用 `IMPLEMENTS_REQUIREMENT`／`DECIDED_BY` 連回 Requirement。
3. **Git ingestion**：匯入 commit history、PR 說明，建立 `Class`／`Method` 節點與 `DEFINED_BY` 關係。
4. **Code analysis**：（見第 20 章邊界說明）Semantica 本身非完整 Static Analyzer，此步驟通常需搭配外部 AST 工具，再把結果匯入 KG。
5. **API analysis**：解析 OpenAPI/Swagger 規格，建立 `API` 節點與 `EXPOSES` 關係。
6. **DB analysis**：解析 PostgreSQL/Oracle/DB2 schema，建立 `Table`／`Column` 節點與 `READS`/`WRITES` 關係。
7. **KG creation**：用 `GraphBuilder(merge_entities=True)` 組裝以上所有節點。
8. **Entity resolution**：跑 `DuplicateDetector`，處理同一個 API 在 Swagger 與程式碼註解中命名不一致的情況。
9. **Conflict detection**：跑 `ConflictDetector`，處理 ADR 文件與實際程式碼不一致的情況（常見於文件未同步更新）。
10. **Provenance**：確認每個節點都有 `source_id`（commit hash、文件頁碼）。
11. **Decision tracking**：AI Agent 每次程式碼修改前，先 `record_decision()`。
12. **AI coding**：Agent 透過 MCP 查詢相關 Context，產生程式碼變更。
13. **Testing**：JUnit 5 測試結果回寫為 `TESTED_BY` 關係。
14. **Deployment**：CI/CD（Jenkins/GitHub Actions/GitLab CI）部署事件記錄為 `DEPLOYED_TO` 關係。
15. **Audit**：稽核人員透過 `trace_decision_chain()` 重建「這次上線的每一行改動依據什麼」。

### 19.4 範例：AI Agent 開發新 API 端點

```python
# 示意：串接 Requirement -> API -> Code -> Decision 的完整範例
graph.add_node("REQ-2201", "Requirement", "支援信用卡分期查詢 API")
graph.add_node("API-installment-query", "API", "GET /api/v1/installments/{accountId}")
graph.add_edge("API-installment-query", "REQ-2201", "IMPLEMENTS_REQUIREMENT")

decision_id = graph.record_decision(
    category="api_design",
    scenario="設計信用卡分期查詢 API，需決定分頁策略",
    reasoning="依據 ArchUnit 規則與既有 API 慣例，採用 cursor-based pagination 而非 offset",
    outcome="cursor_based_pagination_adopted",
    confidence=0.88,
    decision_maker="coding-agent-vue-spring",
    entities=["API-installment-query", "REQ-2201"],
)
```

### 19.5 ArchUnit + Semantica：架構規則的雙重驗證

ArchUnit（Java 靜態架構測試框架）驗證程式碼是否符合分層規則（例如 Controller 不可直接呼叫 Repository），這是**編譯期/測試期**的驗證；Semantica 的 Knowledge Graph 則記錄**這些規則背後的架構決策理由**（`ArchitectureDecision` 節點），兩者互補而非重疊（建議架構）。

### 19.6 AI Prompt 範例

```text
你是 Backend 開發 Agent。在修改 InstallmentController.java 前，
請先透過 MCP 查詢 Semantica Context Graph：
(1) 這個 Class 關聯的 Requirement 與 Business Rule 是什麼
(2) 是否有既有的類似 API 設計決策（find_precedents）
(3) 修改後會影響哪些下游 API/Test（Multi-hop Traversal）
完成修改後，務必呼叫 record_decision() 記錄本次決策，
並在 PR 說明中附上 decision_id。
```

### 19.7 本章 Checklist 與小結

- [ ] Requirement／Architecture／Git／API／DB 五種來源皆已 ingestion 進 KG
- [ ] 每次 AI Agent 的程式碼修改都有對應 `record_decision()` 呼叫
- [ ] Deployment 事件已回寫為 `DEPLOYED_TO` 關係，形成完整生命週期鏈
- [ ] 稽核人員可獨立用 `trace_decision_chain()` 重建任一次上線的完整依據

---

## 20. 情境 B 實戰：AI 輔助逆向工程

> ⚠️ 本章 Legacy Java/Spring 應用為教學示範用途之虛構情境。

### 20.1 全流程

```mermaid
flowchart TB
    LEGACY["Legacy System"] --> SRC2["Source Code"]
    SRC2 --> SA["Static Analysis"]
    SA --> AST["AST"]
    AST --> CMA["Class / Method / API"]
    CMA --> DEP2["Dependency"]
    DEP2 --> DB6["Database"]
    DB6 --> BR3["Business Rule"]
    BR3 --> CG["Call Graph"]
    CG --> AG["Architecture Graph"]
    AG --> KG5["Knowledge Graph"]
    KG5 --> AGENT4["AI Agent"]
    AGENT4 --> REPORT["Reverse Engineering Report"]
```

### 20.2 極重要的邊界釐清：Semantica 不是完整的 Source Code Static Analyzer

這是本章、也是全書最容易被誤解的一點。企業必須理解以下工具鏈的分工（建議架構，基於官方模組能力範圍的誠實劃分）：

| 元件 | 負責什麼 | 是否為 Semantica 官方模組 |
|---|---|---|
| Static Analyzer（例如 SonarQube、Checkstyle） | 程式碼品質規則、Code Smell、安全弱點掃描 | **不是**，需搭配外部工具 |
| AST Analyzer（例如 JavaParser、Tree-sitter） | 把原始碼解析成抽象語法樹，取得精確的 Class/Method/欄位結構 | **不是**，需搭配外部工具產出結構化資料，再匯入 Semantica |
| Code Intelligence（例如 LSP、ctags） | IDE 層級的符號索引、跳轉定義 | **不是** |
| Dependency Analyzer（例如 Maven Dependency Tree、jdeps） | 模組/套件間的依賴關係 | **不是**，但結果可匯入 KG 的 `DEPENDS_ON` 關係 |
| **Semantica Knowledge Graph** | 把以上工具產出的結構化結果，整合成可查詢、有 Provenance、有 Decision 記錄的統一知識圖，並疊加 Business Rule／Requirement 等非程式碼實體 | **是** |
| AI Agent | 依據 KG 提供的證據進行推理、生成報告、提出重構建議 | 使用 Semantica 提供的 Context，本身不是 Semantica 模組 |

**實務結論**：企業逆向工程流程通常是「AST 工具（例如 JavaParser）掃描原始碼 → 產出結構化 JSON → 用 Semantica 的 `TripletExtractor`/`GraphBuilder` 把這些結構化資料組裝成 Knowledge Graph → AI Agent 透過 GraphRAG 查詢」，而不是期待 Semantica 自己去解析 `.java` 檔案的語法樹（建議架構）。

### 20.3 20 個實作步驟

1. 掃描 Legacy Code（外部 AST 工具，例如 JavaParser／Tree-sitter）
2. 建立 Code Entity（`Class`／`Method`／`Package` 節點）
3. 建立 Class / Method / Package 關係（`CONTAINS`／`CALLS`）
4. 建立 Call Graph（`CALLS` 邊的完整圖）
5. 建立 Dependency Graph（Maven Dependency Tree 匯入為 `DEPENDS_ON`）
6. 建立 Database Relationship（JPA/MyBatis mapping 解析為 `READS`/`WRITES`）
7. 建立 API Relationship（Controller 註解解析為 `EXPOSES`）
8. 建立 Business Rule（用 LLM-based `RelationExtractor` 從 comment/commit message 中萃取隱含規則）
9. 建立 Configuration Relationship（`application.yml`／`web.xml` 解析）
10. 建立 Requirement-to-Code Traceability（若有 Jira/Confluence，用 Entity Resolution 比對 ticket 編號）
11. 建立 Code-to-Test Traceability（`TESTED_BY`）
12. 建立 Code-to-Database Traceability（`READS`/`WRITES`）
13. 建立 Code-to-Deployment Traceability（`DEPLOYED_TO`）
14. 找出孤兒程式（`CentralityCalculator` 找出零連接或極低連接度節點）
15. 找出重複邏輯（`DuplicateDetector` 應用於 Method 層級的語意相似度）
16. 找出循環依賴（`PathFinder`／Graph Analytics 偵測環路）
17. 找出高風險模組（Centrality 高 + 無 Test 覆蓋的交集）
18. 找出架構違規（結合 ArchUnit 規則掃描結果匯入 KG，再用 SHACL 驗證，見第 13 章）
19. 找出可能的 Business Rule（LLM Reasoning 提出假設 → Deterministic Rule 驗證，見第 10 章）
20. 將分析結果交給 AI Agent，生成 Reverse Engineering Report

### 20.4 AI Agent 必須能回答的問題（逐一對應 KG 查詢）

| 問題 | 對應查詢 |
|---|---|
| 系統有哪些模組？ | Community Detection |
| 哪些 Class 最重要？ | Degree/Betweenness Centrality |
| 哪些 API 最重要？ | Centrality（限定 `API` 節點類型） |
| 哪些 DB Table 被使用？ | Multi-hop Traversal（`READS`/`WRITES`） |
| 哪些程式相互依賴？ | `DEPENDS_ON` 邊查詢 |
| 哪些 Business Rule 隱藏在程式碼？ | LLM-based Extraction + Reasoning 驗證 |
| 哪些程式沒有 Test？ | 反向查詢缺少 `TESTED_BY` 邊的 `Class` 節點 |
| 哪些程式存在循環依賴？ | Graph Analytics 環路偵測 |
| 哪些模組修改風險最高？ | Centrality × 無 Test 覆蓋 × 高 Churn（commit 頻率） |
| 如果修改 Class X，會影響什麼？ | Multi-hop Impact Analysis（第 14 章） |
| 這個結論的來源在哪裡？ | `ProvenanceManager.get_lineage()` |

### 20.5 範例：找出高風險模組

```python
# 示意：結合 Centrality 與 Test 覆蓋率找出高風險模組
high_centrality = centrality.calculate_betweenness_centrality(kg)
untested_classes = [
    node for node in kg.nodes
    if node.type == "Class" and not graph.get_neighbors(node.id, edge_types=["TESTED_BY"])
]
high_risk = [n for n in high_centrality if n.id in {u.id for u in untested_classes}]
```

### 20.6 AI Prompt 範例

```text
你是逆向工程 Agent。針對 LegacyOrderService 模組：
(1) 使用 get_graph_analytics 找出其 Centrality 排名
(2) 查詢是否有對應的 TESTED_BY 關係
(3) 使用 run_reasoning 檢查是否符合既有 Business Rule
(4) 產出風險評估報告，每個結論都必須附上 source_id 引用，
    不可產出無法追溯來源的陳述。
```

### 20.7 本章 Checklist 與小結

- [ ] 團隊已明確理解 Semantica 不做 AST 解析，已選定外部 AST/Static Analysis 工具
- [ ] 20 個實作步驟已對應到具體 Semantica API 呼叫
- [ ] AI Agent 產出的逆向工程結論皆可用 `get_lineage()` 回溯來源
- [ ] 已識別出孤兒程式、循環依賴、高風險模組清單

---

## 21. 情境 C 實戰：AI 輔助 Framework Upgrade

> ⚠️ 本章 Spring Boot 3.x→4.x、Java 21→25 升版案例為教學示範用途之虛構情境。

### 21.1 全流程

```mermaid
flowchart TB
    CUR["Current System"] --> INV["Code Inventory"]
    INV --> DEPG["Dependency Graph"]
    DEPG --> FAG["Framework API Graph"]
    FAG --> DEPR["Deprecated API"]
    DEPR --> BC["Breaking Change"]
    BC --> CC2["Configuration Change"]
    CC2 --> MR["Migration Rule"]
    MR --> IA["Impact Analysis"]
    IA --> AGENT5["AI Agent"]
    AGENT5 --> CM["Code Modification"]
    CM --> TEST3["Test"]
    TEST3 --> DR["Decision Record"]
    DR --> MAT["Migration Audit Trail"]
```

### 21.2 Semantica 負責的內容

- **版本關係**：用 Bi-temporal Fact 表示 `spring-boot-3.5` → `spring-boot-4.0` 的版本節點（第 9 章）
- **元件關係**：哪些 `Class` 使用了哪個 Framework `API`
- **Dependency 關係**：Maven POM 依賴樹匯入為 `DEPENDS_ON`
- **Migration Rule**：官方 Migration Guide 條目轉為 Forward Chaining 規則（第 10 章）
- **Breaking Change**：標記為特殊型別節點，`CAUSED_BY` 連回官方 Release Notes
- **Affected Component**：Multi-hop Impact Analysis 結果
- **Decision / Rationale / Source**：每次 AI Agent 修改都呼叫 `record_decision()`
- **Test Result**：JUnit 5 測試結果回寫
- **Migration Result**：最終上線狀態記錄

### 21.3 實作步驟

1. **Inventory**：掃描全部原始碼，列出使用的 Framework API 清單（外部 AST 工具 + Semantica KG 匯入，呼應第 20.2 節的分工原則）
2. **Dependency Graph**：Maven Dependency Tree 匯入
3. **Compatibility Analysis**：比對目前使用的 API 版本 vs 目標版本官方相容性清單
4. **Breaking Change Detection**：解析官方 Migration Guide / Release Notes，建立 `BreakingChange` 節點
5. **Impact Analysis**：Multi-hop Traversal 找出受影響的所有 Class/API/Test
6. **Migration Plan**：依風險排序（Centrality × 使用頻率）產出修改順序
7. **AI Code Modification**：Agent 依 Migration Rule 逐一修改，每次修改前用 Forward Chaining 驗證假設（第 10.8 節案例）
8. **Test**：JUnit 5 執行，結果回寫 `TESTED_BY`
9. **Regression**：比對升級前後的 Golden Knowledge Graph（第 32 章）
10. **Decision Record**：`record_decision()` 記錄每一次修改的理由與來源
11. **Audit**：`trace_decision_chain()` 產出完整升版稽核報告

### 21.4 官方 Migration Rule 轉換為 Forward Chaining 規則（示意）

```python
# 示意：把 Spring Boot 4.0 官方 Migration Guide 的一條規則轉為 Semantica Rule
reasoner.add_rule(
    "IF UsesAnnotation(X, 'RequestMapping') AND HasMethodAttribute(X) "
    "THEN ShouldMigrateTo(X, 'GetMapping_or_PostMapping')"
)
```

### 21.5 最終可回答的 7 個關鍵問題

（對應 Master Prompt 原始需求，逐一標示查詢方式）

1. **為什麼這個 Java Class 必須修改？** → `get_causal_chain(decision_id, direction="upstream")` 回溯到觸發修改的 `BreakingChange` 節點
2. **為什麼這個 Spring API 必須替換？** → `ProvenanceManager.get_lineage()` 回到官方 Migration Guide 條目
3. **哪些程式會受到 Spring Boot 升級影響？** → Multi-hop Impact Analysis（第 14 章）
4. **這個修改依據哪一份官方文件？** → Provenance `source_id` 直接指向官方 Migration Guide URL/版本
5. **AI Agent 為什麼選擇這個 migration strategy？** → `record_decision()` 的 `reasoning` 欄位 + `trace_decision_explainability()`
6. **這次修改是否已經測試？** → 查詢 `TESTED_BY` 邊是否存在，以及對應測試結果
7. **如果 migration 失敗，哪些 downstream component 會受到影響？** → `analyze_decision_impact()` + Multi-hop Traversal

### 21.6 AI Prompt 範例

```text
你是 Framework Upgrade Agent，正在處理 Java 21 -> 25、Spring Boot 3.5 -> 4.0 升版。
修改 PaymentController.java 前，請依序：
(1) 查詢此 Class 使用的所有 Framework API（Multi-hop Traversal）
(2) 查詢是否有對應的 Deprecated API / Breaking Change 節點
(3) 用 run_reasoning 驗證你的修改方案是否符合已定義的 Migration Rule
(4) 呼叫 record_decision()，reasoning 欄位必須引用官方 Migration Guide 的具體條目
(5) 修改後執行對應測試，並回寫 TESTED_BY 關係
不可在沒有官方文件依據的情況下，自行假設某個 API 已被棄用。
```

### 21.7 本章 Checklist 與小結

- [ ] 官方 Migration Guide 的關鍵規則已轉換為 Forward Chaining 規則
- [ ] 每個 Breaking Change 節點都有 Provenance 指回官方文件
- [ ] AI Agent 的每次程式碼修改都有 `record_decision()` 且可回答第 21.5 節的 7 個問題
- [ ] 已建立升級前後的 Golden Knowledge Graph 供 Regression 比對（第 32 章）

---

## 22. AI SSDLC 完整流程

### 22.1 AI-Assisted SSDLC 十二階段（建議架構）

每個階段都應產生：`Evidence`、`Decision`、`Source`、`Actor`、`Agent`、`Timestamp`、`Version`、`Outcome` 八項紀錄，全部可映射到 Semantica 的 Decision + Provenance 節點：

```mermaid
flowchart LR
    R1["1. Requirement"] --> D1["2. Design"]
    D1 --> A1["3. Architecture"]
    A1 --> C1["4. Coding"]
    C1 --> T1["5. Testing"]
    T1 --> S1["6. Security"]
    S1 --> RV["7. Review"]
    RV --> B1["8. Build"]
    B1 --> DP2["9. Deployment"]
    DP2 --> MO["10. Monitoring"]
    MO --> MT["11. Maintenance"]
    MT --> AU2["12. Audit"]
    AU2 -.->|"回饋"| R1
```

### 22.2 每階段對應的 Semantica 節點類型

| SSDLC 階段 | 主要 Semantica 節點/操作 |
|---|---|
| Requirement | `Requirement` 節點 + Ingestion |
| Design | `ArchitectureDecision` 節點 |
| Architecture | Ontology 定義（第 7、13 章） |
| Coding | `Class`/`Method` 節點 + `record_decision()` |
| Testing | `Test` 節點 + `TESTED_BY` 邊 |
| Security | Policy Engine `check_compliance()`（第 6.5、24 章） |
| Review | Decision 節點的 `find_precedents()` 交叉比對 |
| Build | CI/CD Pipeline 事件記錄 |
| Deployment | `Deployment` 節點 + `DEPLOYED_TO` 邊 |
| Monitoring | Runtime Event 節點（第 19.2 節） |
| Maintenance | 定期 Graph Health Check（第 34 章） |
| Audit | `trace_decision_chain()` + `ProvenanceManager` 稽核匯出 |

### 22.3 本章 Checklist 與小結

- [ ] 12 個階段都已明確對應到 Semantica 的節點類型或 API 呼叫
- [ ] Security 與 Review 階段已納入 Policy Engine 檢查，而非僅依賴人工

---

## 23. AI Agent Team 設計

### 23.1 多角色 Agent 團隊架構（建議架構）

```mermaid
flowchart TB
    subgraph SemLayer["Semantica（共同 Context / Accountability Layer）"]
        KGT["Knowledge Graph"]
        DGT["Decision Graph"]
        PVT["Provenance"]
    end
    subgraph Team["Multi-Agent Team"]
        ReqA["Requirement Agent"]
        ArchA["Architecture Agent"]
        RevA["Reverse Engineering Agent"]
        CodeA["Coding Agent"]
        TestA["Test Agent"]
        SecA["Security Agent"]
        MigA["Migration Agent"]
        CRA["Code Review Agent"]
        DocA["Documentation Agent"]
        ComA["Compliance Agent"]
        AudA["Audit Agent"]
    end
    SemLayer <--> Team
```

### 23.2 各 Agent 角色與 Semantica 互動方式

| Agent | 主要職責 | 讀/寫 Semantica |
|---|---|---|
| Requirement Agent | 解析需求文件，建立 `Requirement` 節點 | 寫 |
| Architecture Agent | 記錄 ADR，建立 `ArchitectureDecision` | 寫 |
| Reverse Engineering Agent | 分析既有系統（第 20 章） | 讀+寫 |
| Coding Agent | 修改程式碼，`record_decision()` | 讀+寫 |
| Test Agent | 執行測試，回寫 `TESTED_BY` | 寫 |
| Security Agent | 跑 Policy Engine 檢查 | 讀 |
| Migration Agent | Framework Upgrade（第 21 章） | 讀+寫 |
| Code Review Agent | 用 `find_precedents()` 比對既有決策一致性 | 讀 |
| Documentation Agent | 從 KG 反向生成文件 | 讀 |
| Compliance Agent | 稽核 Policy 合規狀態 | 讀 |
| Audit Agent | `trace_decision_chain()` 產出稽核報告 | 讀 |

### 23.3 共享 Context 的關鍵設計原則（建議架構）

- 所有 Agent 應共用**同一個** Knowledge Graph 實例（或同一個持久化檔案/資料庫），而非各自維護獨立副本，否則會出現第 8 章描述的 Conflict 問題。
- 寫入型操作（`record_decision`、`add_entity`）建議限制在特定角色（Coding/Migration/Requirement Agent），Review/Audit/Compliance Agent 應設計為唯讀，降低誤寫風險（呼應第 16.6 節 MCP Read/Write 分離限制）。
- Agno 的 `AgnoSharedContext`（第 17.6 節）是官方提供的具體實作範例。

### 23.4 本章 Checklist 與小結

- [ ] 已定義每個 Agent 角色的讀/寫權限邊界
- [ ] 所有 Agent 共用同一個 Knowledge Graph，而非各自獨立副本
- [ ] Review/Audit/Compliance 類 Agent 已限制為唯讀

---

## 24. Security Architecture

### 24.1 官方已確認的安全相關事實

- v0.6.5（2026-08-11）修補 **6 個具體命名的安全漏洞**，並額外修正 25+ 項正確性問題（官方已實作，GitHub Release Notes，2026-08-20 重新逐項查證）：
  1. **11 個 API Router 缺少身份驗證**（missing authentication across 11 API routers，範圍遠大於先前僅知的「Explorer API 路由」，實際涵蓋 Server 端多數路由群組）
  2. **Cypher Injection**（Neptune／Neo4j／FalkorDB 等 LPG 後端）
  3. **SPARQL Injection**
  4. **SSRF**（Server-Side Request Forgery，發生於 Ontology fetch 與 Web Ingestor）
  5. **WebSocket 缺少 Origin 驗證**
  6. **ReDoS**（Regular Expression Denial of Service，發生於 SPARQL prefix 宣告的正規表示式解析）

  這代表**早於 v0.6.5 的版本，Semantica Server 的多數 API 路由（不只 Explorer）可能缺乏身份驗證，且存在注入式攻擊風險**，企業務必升級至 v0.6.5 以上版本再對外開放任何 REST API 或 Explorer，並在升級前假設舊版本已曝露於上述 6 類風險（建議架構的風險研判，修補內容本身為官方已實作）。
- MCP Server 本身天生本機隔離、無網路曝露（第 16.6 節）。
- Policy Engine **不會自動阻擋動作**，只回傳合規狀態（第 6.5 節）——這代表 Policy Engine 不能單獨作為 Access Control 機制。
- 官方文件**未描述**內建的 RBAC/ABAC 存取控制機制（Policy Engine Guide 明確指出：「does not describe RBAC, ABAC, or explicit access control enforcement mechanisms」）。

### 24.2 企業必須自行補強的安全層（建議架構）

由於 Semantica 本身不提供完整的存取控制，企業導入時應自行設計以下防禦層：

| 安全項目 | 建議做法 |
|---|---|
| Authentication | REST API（`semantica-server`）前方加 API Gateway 做身份驗證（例如 OAuth2/OIDC），Semantica 本身不內建 | 
| Authorization / RBAC / ABAC | 在應用層（呼叫 Semantica 的 Agent 編排層）實作角色權限控管，而非依賴 Semantica 本身 |
| Secret Management | LLM API Key、DB 連線密碼透過 Vault/AWS Secrets Manager/K8s Secret 注入（第 6.3 節） |
| Encryption / TLS | Graph/Vector Store 連線需開啟 TLS；`semantica-server` 前方建議加 Reverse Proxy 終止 TLS |
| Audit Log | 善用 Decision Intelligence + Provenance（第 11、12 章）作為應用層稽核，但需另外保護底層 SQLite/DB 檔案存取權限 |
| Data Masking / PII | Ingestion 階段可用 `TextNormalizer`/自訂 Extractor 過濾 PII，Semantica 未內建自動 PII 偵測機制（Source-confirmed，需自行實作或搭配第三方 PII 偵測工具） |

### 24.3 Prompt Injection 與 Graph Poisoning 防禦

**核心問題**：如果 Semantica Knowledge Graph 被污染，AI Agent 是否會因此產生錯誤決策？

**答案：會。** 因為 GraphRAG（第 15 章）與 Reasoning（第 10 章）都直接信任 KG 內容作為 grounded context，若攻擊者能夠寫入偽造的 `Entity`/`Decision`/`BusinessRule` 節點，下游 Agent 的推理與決策都會被污染（建議架構，基於架構原理的風險分析，非官方安全公告）。

防禦架構（建議架構）：

```mermaid
flowchart TB
    EXT["外部/不可信輸入<br/>(文件上傳、Web Ingestion、第三方 API)"] -->|"需驗證"| GATE["輸入驗證閘道<br/>(Schema/SHACL 驗證)"]
    GATE --> ING3["Ingestion"]
    ING3 --> QUARANTINE["隔離區<br/>(低信心/新來源節點先標記 pending)"]
    QUARANTINE -->|"人工/Policy 審核通過"| KG6["正式 Knowledge Graph"]
    KG6 --> AGENT6["AI Agent 讀取"]
    WRITE["寫入型 Agent 操作"] -->|"僅限授權 Agent"| KG6
```

具體防禦措施（建議架構）：

1. **輸入驗證**：對外部來源（尤其是 Web Ingestion、使用者上傳文件）套用 SHACL 驗證（第 13.3 節），拒絕不符合 Schema 的節點。
2. **信心分級**：低信心（低 `confidence` 分數）或新來源的節點先標記為待審核，不直接進入 Agent 可查詢的正式圖。
3. **寫入權限最小化**：呼應第 23.3 節，只有明確授權的 Agent 角色能呼叫 `add_entity`/`add_relationship`。
4. **Provenance 交叉驗證**：定期用 `verify_chain()`（第 12.3 節）偵測是否有節點的 Provenance 鏈被竄改。
5. **Decision Rule 護欄**：關鍵決策（例如影響生產環境的程式碼修改）強制通過 Forward Chaining/Policy Engine 驗證，不允許 Agent 僅憑 GraphRAG 檢索結果就直接執行（呼應第 10.1 節 Deterministic Validation 原則）。

### 24.4 MCP / Agent Tool Security

呼應第 16.6 節：MCP Server 不做工具層級權限分級，因此企業必須在 **Prompt 層與應用層**補強，例如：

- 在 `CLAUDE.md`／Agent 系統提示中明確列出「哪些工具只能在特定情境下呼叫」
- 對高風險 MCP tools（例如 `add_entity`、`record_decision`）考慮加上人工核准（Human-in-the-loop）流程，而非讓 Agent 全自動執行

### 24.5 本章 Checklist 與小結

- [ ] 已確認使用 v0.6.5 以上版本（避免 Explorer API 未驗證漏洞）
- [ ] REST API 前方已加裝 Authentication/Authorization 層（Semantica 本身不提供）
- [ ] 已針對 Graph Poisoning 風險設計輸入驗證與信心分級機制
- [ ] 高風險寫入型 MCP tools 已考慮人工核准流程

---

## 25. 資料治理與 Governance

### 25.1 五層治理模型（建議架構）

```text
Data Governance        — 資料本身的所有權、品質、保存政策
Knowledge Governance    — Knowledge Graph 的結構與內容治理
Ontology Governance     — Schema/Ontology 變更的審核流程
Decision Governance     — 哪些決策需要人工核准（Policy Engine，第 6.5 節）
Agent Governance        — 哪些 Agent 有哪些權限（第 23.3、24.4 節）
```

### 25.2 關鍵治理維度

| 維度 | 說明 | 對應 Semantica 能力 |
|---|---|---|
| Data ownership | 誰對哪個資料源負責 | Provenance `source_document` 欄位 |
| Source authority | 衝突時哪個來源優先 | Conflict Resolution `credibility_weighted` 策略（第 8.3 節） |
| Data quality | 資料品質評估 | Evaluation 指標（第 33 章） |
| Version | Schema/Ontology 版本管理 | `OntologyGenerator` + Bi-temporal（第 9 章） |
| Lineage | 世系追溯 | `ProvenanceManager.get_lineage()` |
| Retention | 保存期限政策 | 企業需自訂（Semantica 未內建自動保存期限機制，Source-confirmed） |
| Access control | 存取權限 | 企業需自訂（第 24.2 節） |
| Conflict policy | 衝突解決政策 | `ConflictResolver` 策略選擇（第 8.3 節） |
| Resolution policy | 決策例外處理 | Policy Engine `record_exception()`（第 6.5 節） |

### 25.3 本章 Checklist 與小結

- [ ] 五層治理模型已各自指定負責團隊/角色
- [ ] Source Authority 優先順序已明確定義（例如：官方系統 > CRM > 人工輸入）
- [ ] Retention／Access Control 政策已由企業自行補強文件化（非 Semantica 內建）

---

## 26. Observability

### 26.1 四個觀測維度（建議架構）

```text
Agent Observability      + Graph Observability
Decision Observability   + Provenance Observability
```

### 26.2 建議監控指標（建議架構，Semantica 未內建現成 Dashboard，需企業自行從 API 擷取指標）

| 指標 | 資料來源 |
|---|---|
| Agent decision count | `graph.get_decision_insights()`（第 11.3 節） |
| Decision latency | 應用層自行埋點（`record_decision()` 呼叫前後計時） |
| Graph size（node/edge count） | `get_graph_summary`（MCP resource / REST `/api/graph`） |
| Extraction accuracy | 對照人工標註樣本（第 33 章 Evaluation） |
| Conflict count | `ConflictDetector.detect_conflicts()` 回傳筆數 |
| Duplicate count | `DuplicateDetector.detect_duplicate_groups()` 回傳筆數 |
| Provenance completeness | `ProvenanceManager.get_statistics()` |
| Rule violation | Policy Engine `check_compliance()` 回傳 False 的筆數 |
| Failed reasoning | `InferenceResult` 中未能得出結論的查詢比例 |
| MCP calls | 應用層或 MCP Server 日誌埋點統計 |

### 26.3 與既有 Observability 生態系整合（建議架構）

Semantica 官方文件未提供原生 OpenTelemetry/Prometheus exporter（Source-confirmed），企業可透過以下方式整合：

```python
# 示意：在呼叫 Semantica API 的應用層包一層 OpenTelemetry span
from opentelemetry import trace

tracer = trace.get_tracer("semantica.integration")

with tracer.start_as_current_span("record_decision") as span:
    decision_id = graph.record_decision(...)
    span.set_attribute("semantica.decision_id", decision_id)
    span.set_attribute("semantica.category", "framework_migration")
```

- **Prometheus**：定期呼叫 `get_graph_summary`／`get_decision_insights` 等 API，轉為自訂 Exporter 曝露 metrics endpoint。
- **Grafana**：基於上述 Prometheus metrics 建立 Dashboard（節點數成長趨勢、決策信心分布、衝突數量）。
- **ELK**：`SEMANTICA_LOG_LEVEL=DEBUG` 輸出的日誌可直接接入 Logstash/Filebeat。

### 26.4 本章 Checklist 與小結

- [ ] 已針對 Decision／Graph／Provenance 三個維度定義關鍵監控指標
- [ ] 已理解 Semantica 本身不提供原生 OTel/Prometheus exporter，需自行封裝
- [ ] Rule violation／Failed reasoning 已納入告警機制，而非僅記錄

---

## 27. Performance／Scalability

### 27.1 官方效能數據

（官方已實作，README「Performance」章節，基準測試於 v0.6.5，118,000 節點的生產圖）

| 指標 | 改善幅度 |
|---|---|
| Node search | 24 ms → 0.004 ms（6,000 倍） |
| Embedding cache hit | 10 倍吞吐量提升 |
| Semantic deduplication | 6.98 倍加速 |
| Candidate generation | 63.6% 加速 |

### 27.2 大型 KG 的效能考量（建議架構）

- **Million nodes / Billion edges**：預設 in-memory 後端（`ContextGraph`）適合中小型圖；達到百萬節點規模建議切換至 Neo4j/FalkorDB 等外部 Graph Store（第 6.4 節）。
- **Graph traversal**：Multi-hop Traversal 的 `hops` 參數若設太大，在大圖上會導致查詢時間指數增長，建議限制在 2-3 hop 並搭配索引後端。
- **Entity resolution／Deduplication**：`hybrid_v2` 策略雖然精準度較高，但計算成本也較高，大批量資料建議先用 blocking 策略縮小比對範圍（第 8.2 節）。
- **Vector search／Hybrid search**：FAISS 適合中小規模，Qdrant/Weaviate/Milvus 更適合水平擴充的正式環境（第 5.6 節 extras 對應）。
- **Batch ingestion vs Streaming ingestion**：Pipeline DSL 的 `set_parallelism(N)`（第 18.6 節）可調整批次處理平行度；Kafka 來源適合串流 ingestion 模式。

### 27.3 環境分層架構（建議架構）

```mermaid
flowchart LR
    DEV2["Development<br/>(in-memory / SQLite)"] --> TESTENV["Test<br/>(單機 Neo4j/PgVector)"]
    TESTENV --> PROD2["Production<br/>(叢集 Graph Store + Vector Store)"]
    PROD2 --> DIST["Distributed Production<br/>(多節點 Neo4j Cluster / FalkorDB Cluster)"]
```

### 27.4 本章 Checklist 與小結

- [ ] 已依圖規模（節點數量級）選擇對應的 Graph/Vector Store 後端
- [ ] Multi-hop Traversal 的 `hops` 參數已設定合理上限
- [ ] 大批量資料的 Entity Resolution 已採用 blocking 策略降低計算成本

---

## 28. High Availability／Backup／DR

> ⚠️ 本章內容為**建議架構**。Semantica 官方文件未提供完整的企業級 HA/DR 藍圖（僅 v0.5.1 起提供 Knowledge Explorer 的 Docker/K8s 部署範本，範圍有限），以下是本手冊依據標準 Python 服務 + 資料庫 HA 實務原則提出的企業落地建議。

### 28.1 建議架構圖

```mermaid
flowchart TB
    LB["Load Balancer"] --> API3["Semantica API<br/>(semantica-server ×N)"]
    API3 --> SVC["Semantica Service Layer"]
    SVC --> GS["Graph Store<br/>(Neo4j Cluster / FalkorDB)"]
    SVC --> VS2["Vector Store<br/>(Qdrant Cluster / PgVector)"]
    SVC --> OS["Object Storage<br/>(備份 SQLite Provenance DB / KG Export)"]
```

### 28.2 HA 設計原則

- `semantica-server` 本身可水平擴充多副本（stateless，狀態存於外部 Graph/Vector Store），搭配 Load Balancer 做健康檢查與流量分配。
- Graph Store／Vector Store 的 HA 依各自產品能力（例如 Neo4j Causal Cluster、Qdrant 的分散式模式），而非 Semantica 本身提供。
- `semantica-worker`（背景工作行程，第 30 章）建議獨立部署多副本，避免 ingestion pipeline 成為單點故障。

### 28.3 Backup／DR 策略

| 資料 | 備份方式 | 建議頻率 |
|---|---|---|
| Provenance SQLite DB | 檔案層備份 + `verify_chain()` 定期校驗 | 每日 |
| Knowledge Graph（若用 in-memory/JSON） | `graph.save_to_file()` 匯出 + 版控/物件儲存 | 每次重大變更後 |
| Graph Store（Neo4j 等外部） | 依產品原生備份機制（例如 Neo4j `neo4j-admin backup`） | 依 RPO 需求 |
| Vector Store | 依產品原生快照機制 | 依 RPO 需求 |

### 28.4 RPO／RTO 建議基準（建議架構，企業應依實際風險容忍度調整）

| 環境等級 | RPO | RTO |
|---|---|---|
| 開發/測試 | 24 小時 | 不要求 |
| 一般正式環境 | 1 小時 | 4 小時 |
| 高風險（金融/醫療） | 15 分鐘 | 1 小時 |

### 28.5 本章 Checklist 與小結

- [ ] `semantica-server` 已設計為多副本水平擴充，狀態外置於 Graph/Vector Store
- [ ] Provenance SQLite DB 已納入每日備份與定期 `verify_chain()` 校驗
- [ ] RPO/RTO 已依系統風險等級明確定義並演練過災難復原流程

---

## 29. Docker／Podman／Kubernetes 部署

### 29.1 官方部署範本的實際範圍

**務必先理解範圍限制**：官方在 v0.5.1 提供的 Docker/K8s 部署範本，是針對 **Knowledge Explorer**（視覺化儀表板）的部署，而非完整的 Semantica Server + Worker + Graph Store 生產部署藍圖（官方已實作，GitHub Release Notes v0.5.1；範圍限制為本手冊研判）。以下第 29.2-29.4 節的完整生產部署設計，除非另有標示，皆屬**建議架構**。

### 29.2 Docker Compose 範例（建議架構）

```yaml
# 示意 docker-compose.yml，非官方逐字範例
version: "3.9"
services:
  semantica-server:
    build: .
    command: semantica-server
    ports:
      - "8000:8000"
    environment:
      SEMANTICA_KG_PATH: /data/knowledge_graph.json
      SEMANTICA_LOG_LEVEL: INFO
      SEMANTICA_CORS_ORIGINS: "https://internal.example.com"
    volumes:
      - semantica_data:/data
    depends_on:
      - postgres

  semantica-worker:
    build: .
    command: semantica-worker
    environment:
      SEMANTICA_KG_PATH: /data/knowledge_graph.json
    volumes:
      - semantica_data:/data
    depends_on:
      - postgres

  postgres:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_DB: semantica
      POSTGRES_PASSWORD_FILE: /run/secrets/pg_password
    secrets:
      - pg_password
    volumes:
      - pg_data:/var/lib/postgresql/data

volumes:
  semantica_data:
  pg_data:

secrets:
  pg_password:
    file: ./secrets/pg_password.txt
```

### 29.3 Podman 對照

```bash
podman play kube semantica-pod.yaml   # 可將上述 compose 轉為 Kubernetes YAML 後用 podman play kube 啟動
```

### 29.4 Kubernetes 部署範例（建議架構）

```yaml
# 示意 Deployment，非官方逐字範例
apiVersion: apps/v1
kind: Deployment
metadata:
  name: semantica-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: semantica-server
  template:
    metadata:
      labels:
        app: semantica-server
    spec:
      containers:
        - name: semantica-server
          image: registry.internal/semantica-server:0.6.5
          ports:
            - containerPort: 8000
          envFrom:
            - configMapRef:
                name: semantica-config
            - secretRef:
                name: semantica-secrets
          readinessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 5
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 15
---
apiVersion: v1
kind: Service
metadata:
  name: semantica-server
spec:
  selector:
    app: semantica-server
  ports:
    - port: 80
      targetPort: 8000
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: semantica-server-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: semantica-server
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

ConfigMap／Secret／Ingress 依企業既有 K8s 慣例設定（`SEMANTICA_CORS_ORIGINS` 等非敏感設定放 ConfigMap，LLM API Key／DB 密碼放 Secret）。

### 29.5 本章 Checklist 與小結

- [ ] 已理解官方 Docker/K8s 範本僅涵蓋 Explorer，生產部署需自行設計
- [ ] `semantica-server` 已設定 readiness/liveness probe
- [ ] 敏感設定（API Key、DB 密碼）已放入 Secret 而非 ConfigMap
- [ ] 已依流量規模設定 HPA（HorizontalPodAutoscaler）

---

## 30. CLI 完整參考

> ⚠️ 以下指令群組彙整自官方 README 與 `docs.getsemantica.ai/cli-setup`，但**各子指令的完整旗標（flags）本手冊未逐一查證**，正式使用前請務必執行對應的 `--help` 取得你安裝版本的精確參數（Source-confirmed，除非另外標明「官方已實作」）。

### 30.1 五個 CLI 執行檔（官方已實作，`docs.getsemantica.ai/cli-setup`）

`pip install semantica` 會註冊 5 個執行檔：

| 執行檔 | 用途 |
|---|---|
| `semantica` | 通用 CLI，用於 pipeline 執行、抽取、圖操作 |
| `semantica-server` | FastAPI/uvicorn REST API Server，預設綁定 `0.0.0.0:8000` |
| `semantica-worker` | 背景工作行程進入點 |
| `semantica-explorer` | 瀏覽器互動式 Knowledge Graph 探索儀表板 |
| `semantica-mcp` | MCP Server（stdio），供 Claude Desktop/Cursor/Windsurf 等 MCP client 使用 |

### 30.2 `semantica` 主指令群組（官方已實作，README 指令清單）

```bash
semantica --help           # 分組指令參考
semantica doctor           # 健康檢查
```

指令群組（官方已實作）：

```text
ingest · parse · extract · kg · reason · decision · temporal · provenance
ontology · embed · deduplicate · validate · export · visualize · pipeline
server · explorer · mcp · shell · init · watch
```

每個群組底下的實際子指令與旗標，請執行 `semantica <group> --help` 查詢（例如 `semantica kg --help`）（Source-confirmed）。

### 30.3 `semantica-server`（官方已實作）

```bash
semantica-server
curl http://localhost:8000/health
curl http://localhost:8000/api/info
```

### 30.4 `semantica-worker`（官方已實作）

```bash
semantica-worker
```

### 30.5 `semantica-explorer`（官方已實作）

```bash
pip install "semantica[explorer]"
semantica-explorer --graph my_graph.json
# 預設開啟於 http://127.0.0.1:8000
```

功能（官方已實作，README）：即時 Sigma.js 畫布、時間軸拖曳、決策因果鏈視覺化、實體去重介面、Ontology 視覺編輯器、PROV-O 世系視覺化。

### 30.6 `semantica-mcp`（官方已實作，第 16 章已詳述）

```bash
semantica-mcp
semantica-mcp --help
```

### 30.7 驗證清單

```bash
semantica --help
semantica-server --help
semantica-worker --help
semantica-explorer --help
semantica-mcp --help
python -c "import semantica; print(semantica.__version__)"
```

### 30.8 本章 Checklist 與小結

- [ ] 已確認自己安裝版本的 `semantica --help` 輸出與本章一致（若不一致，以你的版本為準）
- [ ] 已知道 5 個 CLI 執行檔各自的用途，不會混淆 `semantica-server`（REST）與 `semantica-mcp`（stdio）
- [ ] 正式環境的 `semantica-explorer` 存取已限制在內網或加上身份驗證（呼應第 24.1 節 Explorer API 未驗證漏洞警示）

---

## 31. Python API 完整參考

> 本章彙整第 4-21 章已出現過的官方模組，並補充完整 import 路徑一覽表，作為速查用途。每個模組的完整使用時機與範例請回頭參照對應章節。

### 31.1 核心模組一覽（官方已實作，README「Core Modules」）

| 模組 | 用途 | 詳細章節 |
|---|---|---|
| `semantica.context` | `ContextGraph`／`AgentContext`，Context Graph 與 Decision Intelligence | 第 3、11 章 |
| `semantica.ingest` | 檔案、Web、資料庫、Databricks、Snowflake、API、串流、MCP 攝取 | 第 18 章 |
| `semantica.parse`（示意路徑） | 文件解析（`DocumentParser`／`DoclingParser`） | 第 4.5 節 |
| `semantica.normalize` | 文字、實體、日期、數字正規化 | 第 18.5 節 |
| `semantica.split` | Entity-aware／Relation-aware／GraphRAG 導向切分 | 第 4.4 節 |
| `semantica.semantic_extract` | NER、關係抽取、事件、三元組 | 第 4.3 節 |
| `semantica.conflicts` | 衝突偵測與解決 | 第 8.3 節 |
| `semantica.deduplication` | 實體去重、Blocking、聚類 | 第 8.2 節 |
| `semantica.kg` | 圖建構、Centrality、社群偵測、Link Prediction | 第 7、14 章 |
| `semantica.reasoning` | Rete、Datalog、SPARQL、Forward Chaining（可解釋） | 第 10 章 |
| `semantica.vector_store` | FAISS、Qdrant、Weaviate、Milvus、Pinecone、PgVector | 第 6.4 節 |
| `semantica.provenance` | W3C PROV-O 世系追蹤 | 第 12 章 |
| `semantica.ontology` | OWL 生成、SHACL 驗證、SKOS | 第 13 章 |
| `semantica.pipeline` | 宣告式、平行化 Pipeline DSL | 第 18.6 節 |
| `semantica.export` | RDF、OWL、Parquet、Cypher、JSON-LD | 第 31.5 節 |
| `semantica.visualization` | 力導向圖、Ontology 階層、時間軸 | 第 31.6 節 |
| `semantica.policy`（示意路徑） | Policy Engine | 第 6.5 節 |
| `semantica.llms` | LiteLLM 整合，多 LLM Provider | 第 6.3 節 |

> ⚠️ **模組路徑查證備註（2026-08-20）**：`semantica.parse` 與 `semantica.policy` 標示為「示意路徑」，因為本手冊重新查證時，能確認**功能本身確實存在**（文件解析、Policy Engine 皆有對應的 CLI 指令群組與官方 Guide 頁面），但**未能獨立取得官方原始碼或 README 對這兩個模組確切 import 路徑的逐字確認**。其餘模組路徑（`semantica.context`、`semantica.ingest`、`semantica.kg`、`semantica.provenance` 等）皆已透過 GitHub 原始碼結構交叉核對確認無誤。正式導入前，這兩個模組請務必以 `python -c "import semantica; help(semantica)"` 或官方原始碼實際核對。

### 31.2 API 使用時機速查（每個模組的「何時使用」）

| 模組 | 何時使用 | 常見誤用 |
|---|---|---|
| `ContextGraph` | 需要 Agent 執行期共享的 in-memory 圖 + Decision Intelligence | 誤用於需要持久化大型企業 KG 的場景（應改用 `semantica.kg` + 外部 Graph Store） |
| `semantica.kg` | 需要持久化、可跑 Graph Analytics 的企業知識資產 | 誤用於單次 Agent Session 的暫時性上下文（過度重量級） |
| `semantica.reasoning` | 需要可解釋、可重現的規則驗證 | 誤用於單純語意相似度查詢（應改用 `vector_store`） |
| `semantica.provenance` | 需要稽核、合規、來源追溯 | 誤用於高頻低延遲、無合規需求的系統（overhead 不划算，第 12.6 節） |
| `semantica.conflicts` | 多來源資料可能衝突 | 誤用於單一可信來源的場景（不必要的複雜度） |

### 31.3 Common Mistakes（跨模組常見錯誤，建議架構）

1. 把 `ContextGraph`（in-memory）誤當成正式生產環境的唯一持久化層——重啟即遺失，務必 `save_to_file()` 或改用外部 Graph Store。
2. 忘記在 `ProvenanceManager` 設定 `storage_path`，導致稽核軌跡無法跨重啟保留（第 6.2 節）。
3. 對所有資料一律用 LLM-based extraction，忽略 pattern-based/rule-based 方法在明確結構化資料上更快、更確定（第 10.7 節推理陷阱同理適用於抽取）。
4. 誤以為 Policy Engine 會自動阻擋不合規決策（第 6.5、24.1 節已明確澄清不會）。

### 31.4 Version Notes

Semantica 平均每 3-6 週釋出一次 minor 版本，模組間的方法簽章可能微調（例如第 11.2 節提到的 `find_similar_decisions` vs `find_precedents` 命名差異）。企業導入建議：**將 Semantica 版本鎖定在 `requirements.txt`/`pyproject.toml` 的明確版本號**（而非 `semantica>=0.6`），並在升級前依第 35 章 Upgrade SOP 走完整回歸測試（建議架構）。

### 31.5 Export 模組完整範例（README 逐字，官方已實作）

```python
from semantica.export import (
    RDFExporter,
    JSONExporter,
    ParquetExporter,
    LPGExporter,
)

kg = {"entities": [...], "relationships": [...]}

# RDF/Turtle
rdf = RDFExporter()
rdf.export(kg, "kg_audit.ttl", format="turtle")
rdf.export(kg, "kg_audit.jsonld", format="json-ld")

# Parquet
ParquetExporter(compression="snappy").export_knowledge_graph(kg, "kg_snapshot")

# Neo4j Cypher
LPGExporter().export(kg, "kg_import.cypher")
```

### 31.6 Visualization 模組完整範例（README 逐字，官方已實作）

```python
from semantica.visualization import (
    KGVisualizer,
    OntologyVisualizer,
    EmbeddingVisualizer,
    TemporalVisualizer,
)

viz = KGVisualizer(layout="force", color_scheme="default")
viz.visualize_network(kg, output="interactive", file_path="kg.html")
viz.visualize_communities(kg, communities, output="interactive")

OntologyVisualizer().visualize_hierarchy(ontology, output="interactive")
TemporalVisualizer().visualize_timeline(kg, output="interactive")
```

### 31.7 本章 Checklist 與小結

- [ ] 已建立團隊內部的模組速查表（可直接複用本章 31.1、31.2 節表格）
- [ ] Semantica 版本已鎖定明確版本號，而非浮動版本範圍
- [ ] 已避免 31.3 節列出的 4 個常見誤用模式

---

## 32. Testing

### 32.1 測試分層（建議架構）

```text
Unit Test           — 單一模組（例如 ConflictDetector）的邏輯正確性
Integration Test     — Ingestion → Extract → KG Build 的端到端流程
Graph Test           — KG 結構完整性（節點/邊數量、Schema 符合度）
Ontology Test        — SHACL 驗證通過率（第 13.3 節）
Reasoning Test        — Forward Chaining 規則的正確性（給定 Fact，驗證預期 Conclusion）
Provenance Test       — verify_chain() 完整性驗證
Decision Test         — record_decision() 的因果鏈是否正確建立
Agent Test            — AI Agent 在給定 Context 下是否做出預期決策
MCP Test              — MCP Server 12 個 tools 的介面測試
Regression Test        — 見 32.2 節 Golden Knowledge Graph
```

### 32.2 Golden Knowledge Graph 概念（建議架構）

用於 Framework Upgrade（第 21 章）與逆向工程（第 20 章）的回歸測試核心概念：在升級/重構前，先用 `graph.save_to_file()` 匯出一份「已知正確」的 Knowledge Graph 快照（Golden KG）。升級/重構後，重新產生 KG，與 Golden KG 做結構化差異比對（節點數、關鍵路徑、Centrality 排名是否劇烈變動），任何非預期差異都應觸發人工複查。

```python
# 示意：Golden KG 比對流程
golden = load_graph("golden_kg_v3.5.json")
current = load_graph("current_kg_v4.0.json")

diff = compare_graphs(golden, current)  # 示意函式，需企業自行實作
if diff.unexpected_node_removals or diff.unexpected_edge_removals:
    raise RegressionError("KG 結構出現非預期差異，請人工複查")
```

### 32.3 本章 Checklist 與小結

- [ ] 10 種測試分層已至少覆蓋 Integration／Reasoning／Provenance／Regression 四項
- [ ] Framework Upgrade／逆向工程專案已建立 Golden Knowledge Graph 基準

---

## 33. Evaluation 指標

### 33.1 各面向指標（建議架構，整合官方模組能力設計的評估框架）

**Extraction（抽取品質）**：Precision、Recall、F1（對照人工標註樣本評估 NER/RelationExtractor 準確度）。

**Entity Resolution**：Precision、Recall、False Merge（誤合併不同實體）、False Split（未能合併同一實體）。

**Knowledge Graph**：Completeness（應有節點/邊是否齊全）、Consistency（是否有邏輯矛盾，可用 `OntologyValidator` 輔助）、Accuracy（抽樣人工驗證）。

**Reasoning**：Correctness（推理結論正確率）、Explainability（`ExplanationGenerator` 輸出是否人類可理解）、Determinism（同樣輸入是否得到同樣結論，這是 Deterministic Reasoning 相對 LLM Reasoning 的核心優勢）。

**Provenance**：Coverage（多少比例的節點/邊有完整 Provenance）、Completeness（`get_statistics()` 檢視）、Traceability（抽樣測試 `get_lineage()` 是否能回溯到原始文件）。

**AI Agent**：Decision accuracy（決策正確率，需人工複核抽樣）、Decision reproducibility（同樣情境下是否做出一致決策）、Evidence coverage（決策的 `reasoning` 欄位是否引用了具體 Evidence，而非空泛陳述）、Unsupported decision rate（沒有對應 Evidence/Provenance 支撐的決策比例，此指標應趨近於零）。

### 33.2 本章 Checklist 與小結

- [ ] Extraction／Entity Resolution 已建立人工標註基準樣本，定期評估 Precision/Recall
- [ ] 「Unsupported decision rate」已納入團隊 KPI，並設定可接受上限（建議：< 5%）

---

## 34. Maintenance

### 34.1 每日／每週／每月維護 Checklist（建議架構）

**每日**：

- [ ] 檢查 `SEMANTICA_LOG_LEVEL` 日誌是否有異常 ERROR
- [ ] 確認 Provenance SQLite DB 備份成功（第 28.3 節）
- [ ] 檢查 Policy Engine `check_compliance()` 是否有大量 False 結果堆積未處理

**每週**：

- [ ] 檢視 Conflict Detection 累積數量，處理待決衝突（第 8.3 節）
- [ ] 檢視 Duplicate Detection 是否有新的合併候選待審核
- [ ] 檢查 Graph 成長趨勢（節點/邊數量），評估是否需要調整 Graph Store 後端規模（第 27 章）

**每月**：

- [ ] Ontology 審查：是否有新的實體/關係型別需要正式納入 Schema（第 13 章）
- [ ] Rule 維護：Forward Chaining／Rete 規則是否仍符合最新業務邏輯（第 10 章）
- [ ] `verify_chain()` 全面掃描，確認 Provenance 完整性未遭竄改
- [ ] Performance Tuning：檢視 Graph Analytics 查詢延遲，必要時調整索引/快取策略

### 34.2 本章 Checklist 與小結

- [ ] 已將本章 Checklist 排入團隊 On-call/維運排班表
- [ ] Conflict／Duplicate 待審核佇列已有明確負責人與 SLA

---

## 35. Upgrade SOP

### 35.1 標準流程

```mermaid
flowchart TB
    RN["Release Note"] --> DIFF["API Diff"]
    DIFF --> DEPDIFF["Dependency Diff"]
    DEPDIFF --> COMPAT["Compatibility Test"]
    COMPAT --> REGR["Regression"]
    REGR --> KGMIG["KG Migration"]
    KGMIG --> ONTMIG["Ontology Migration"]
    ONTMIG --> PROVVAL["Provenance Validation"]
    PROVVAL --> ROLLOUT["Production Rollout"]
```

### 35.2 各步驟說明（建議架構）

1. **Release Note**：逐字閱讀官方 GitHub Releases，特別留意 Breaking Change 標記（呼應第 21 章 Framework Upgrade 的方法論，這裡是把同樣方法用在 Semantica 自身升級上）。
2. **API Diff**：比對第 31 章模組清單中，本次升級是否有方法簽章變更（例如第 11.2 節提到的命名差異）。
3. **Dependency Diff**：檢查 `pyproject.toml`/`setup.py` 相依套件版本是否有變動，尤其是 Graph/Vector Store 相關 extras。
4. **Compatibility Test**：在獨立測試環境安裝新版本，執行第 32 章測試套件。
5. **Regression**：比對 Golden Knowledge Graph（第 32.2 節），確認升級未改變既有 KG 結構語意。
6. **KG Migration**：若新版本改變了內部儲存格式，執行官方提供的 migration script（若有）或自行撰寫轉換腳本。
7. **Ontology Migration**：若 Ontology Schema 有變動，同步更新 SHACL Shape。
8. **Provenance Validation**：`verify_chain()` 確認升級過程未破壞既有稽核鏈完整性。
9. **Production Rollout**：採藍綠部署或滾動升級，搭配第 28 章 HA 架構降低風險。

### 35.3 讓 AI Agent 協助升級（建議架構）

可將本章流程本身，設計成一組由 Migration Agent（第 23 章）執行的 SOP，例如：Agent 讀取 Release Note，用 Reasoning Engine 比對 API Diff，自動標記受影響的企業程式碼（透過第 21 章方法論），但**Production Rollout 步驟應保留人工核准關卡**，不建議完全自動化。

### 35.4 本章 Checklist 與小結

- [ ] 已建立 Semantica 自身版本升級的獨立測試環境（與生產環境隔離）
- [ ] 升級前已比對 Golden Knowledge Graph 確認無非預期結構變化
- [ ] Production Rollout 保留人工核准關卡

---

## 36. 企業導入方法論與 RACI

### 36.1 五階段導入方法論（建議架構）

| Phase | 目標 | 人員 | 技術 | Deliverables | KPI | Risk | Exit Criteria |
|---|---|---|---|---|---|---|---|
| **Phase 1：PoC** | 驗證核心價值主張 | 1-2 位工程師 | in-memory ContextGraph，單一資料源 | 6 步驟 Quickstart 跑通、1 個真實文件的 KG | 是否能回答預設的 3-5 個問題 | 選錯示範情境導致高層誤判價值 | Demo 通過內部評審 |
| **Phase 2：Pilot** | 單一團隊/單一情境試點 | 3-5 人小組 | 外部 Graph/Vector Store、MCP 整合 Claude Code | 第 19/20/21 章任一情境的完整落地 | Decision 記錄覆蓋率、Provenance 完整度 | 資料品質不佳導致 Entity Resolution 效果差 | 試點團隊願意持續使用 |
| **Phase 3：Production** | 正式上線單一情境 | 加入 DevOps/Security | 第 28、29 章 HA/K8s 部署 | 正式環境監控（第 26 章）、備份策略（第 28.3 節） | Uptime、Decision Latency | Security Architecture 未落實（第 24 章） | 通過內部 Security Review |
| **Phase 4：Enterprise Scale** | 擴展至多團隊/多情境 | 建立平台團隊 | 統一 Ontology 治理（第 25 章） | 跨團隊 Ontology 標準、共用 Graph Store | 使用團隊數、KG 節點成長 | Ontology 各自為政造成孤島 | Ontology Governance 流程上線 |
| **Phase 5：AI Governance** | 全企業問責與稽核體系 | 加入法遵/稽核 | Policy Engine 全面部署 | 稽核報告範本、RACI 落地 | Unsupported decision rate（第 33.1 節） | 稽核需求與技術能力落差 | 通過外部/內部稽核驗證 |

### 36.2 RACI 表

| Role | Requirement Ingestion | KG 建模/Ontology | AI Agent Coding | Decision Recording | Security Review | Production 部署 | 稽核 |
|---|---|---|---|---|---|---|---|
| PM | A | C | I | I | I | I | I |
| SA | C | R | C | C | C | A | C |
| Architect | C | A | C | C | R | R | C |
| Developer | I | C | R | R | I | C | I |
| AI Engineer | R | R | A | A | C | C | I |
| Data Engineer | R | R | I | I | I | C | I |
| DevOps | I | I | I | I | C | A | I |
| Security | I | I | I | C | A | R | R |
| DBA | I | C | I | I | I | C | I |
| Compliance | I | C | I | R | R | I | A |
| Auditor | I | I | I | C | I | I | R |

（R=Responsible／A=Accountable／C=Consulted／I=Informed，建議架構，企業可依組織實際狀況調整）

### 36.3 本章 Checklist 與小結

- [ ] 已確認目前處於哪個 Phase，並明確該 Phase 的 Exit Criteria
- [ ] RACI 表已依組織實際角色調整並取得各方共識
- [ ] Phase 5（AI Governance）已排入年度目標，而非無限期擱置

---

## 37. AI Agent + Semantica 開發 SOP

### 37.1 開發前 Checklist

- [ ] 建立 Project Context（第 3、7 章 Ontology 設計）
- [ ] 建立 Ontology（第 13 章，含 SHACL 驗證規則）
- [ ] 建立 Source（確認資料源與 Ingestor 對應，第 18 章）
- [ ] 建立 KG（跑過一次完整 Ingestion Pipeline）
- [ ] 驗證資料（Entity Resolution + Conflict Detection 已執行，第 8 章）

### 37.2 開發中 Checklist

- [ ] AI Agent 查詢 Context（透過 MCP 或直接 API，第 16、17 章）
- [ ] 查詢相關 precedent（`find_precedents()`／`find_similar_decisions()`，第 11.3 節）
- [ ] 建立 Decision（`record_decision()`，第 11.2 節）
- [ ] 記錄 Evidence（`reasoning` 欄位引用具體 Provenance `source_id`）
- [ ] 執行 deterministic rules（Forward Chaining/Policy Engine 驗證，第 10、6.5 章）

### 37.3 開發後 Checklist

- [ ] Test（JUnit 5 等測試結果回寫 `TESTED_BY`，第 32 章）
- [ ] Review（Code Review Agent 用 `find_precedents()` 交叉比對一致性，第 23.2 節）
- [ ] Provenance（確認新節點/邊皆有完整 `source_id`）
- [ ] Audit（`trace_decision_chain()` 可完整重建本次修改的依據）
- [ ] Deployment（`DEPLOYED_TO` 關係已記錄，第 19.3 節）

### 37.4 本章 Checklist 與小結

- [ ] 本 SOP 已納入團隊 PR Template 或 CI Pipeline 檢查項
- [ ] 新進工程師 Onboarding 文件已引用本章三個階段 Checklist

---

## 38. AI Agent Prompt Engineering 範本

> 核心原則：AI Agent **不可只回答答案**，必須引用 Semantica context、Knowledge Graph、Evidence、Decision、Provenance（呼應開篇重要聲明與第 20.6、21.6 節範例）。以下 11 種範本皆為建議架構。

### 38.1 Requirement Analysis Prompt

```text
你是 Requirement Analysis Agent。請分析以下需求文件，並：
(1) 抽取出結構化的 Requirement 節點
(2) 查詢 Knowledge Graph 是否已存在類似需求（避免重複建立）
(3) 標示每個抽取結果的 confidence 分數與來源頁碼
不要臆測文件未明確陳述的內容。
```

### 38.2 Architecture Analysis Prompt

```text
你是 Architecture Analysis Agent。請針對 [模組名稱]：
(1) 查詢其關聯的 ArchitectureDecision 節點
(2) 用 Graph Analytics 找出其 Centrality 排名
(3) 說明此模組的架構決策依據哪些官方文件或先前決策（find_precedents）
所有結論必須附上 source_id。
```

### 38.3 Reverse Engineering Prompt

（同第 20.6 節範例，此處為通用版）

```text
你是逆向工程 Agent。針對 [Class/Module 名稱]：
(1) 使用 get_graph_analytics 找出其 Centrality 排名
(2) 查詢是否有對應的 TESTED_BY 關係
(3) 使用 run_reasoning 檢查是否符合既有 Business Rule
(4) 產出風險評估報告，每個結論都必須附上 source_id 引用
```

### 38.4 Coding Prompt

```text
你是 Coding Agent。修改 [檔案路徑] 前，請先：
(1) 透過 MCP 查詢此檔案關聯的 Requirement／Business Rule／既有 Decision
(2) 查詢修改後的 Multi-hop Impact（會影響哪些下游 API/Test）
完成修改後，務必呼叫 record_decision()，reasoning 欄位需具體引用查到的 Evidence。
```

### 38.5 Code Review Prompt

```text
你是 Code Review Agent。請針對這次程式碼變更：
(1) 用 find_precedents() 查詢是否有類似的既有決策
(2) 檢查本次變更是否有對應的 record_decision() 記錄
(3) 若無對應 Decision 記錄，標記為「Unsupported Change」並要求補充
```

### 38.6 Framework Upgrade Prompt

（同第 21.6 節範例）

### 38.7 Impact Analysis Prompt

```text
你是 Impact Analysis Agent。若修改 [元件名稱]：
(1) 用 Multi-hop Traversal（2-3 hop）列出所有可能受影響的 API/DB Table/Test
(2) 用 analyze_decision_impact() 查詢過去類似修改的實際影響範圍
(3) 產出影響範圍清單，並標示信心程度（依 Centrality 與歷史資料量）
```

### 38.8 Security Review Prompt

```text
你是 Security Review Agent。請針對本次變更：
(1) 用 check_decision_rules() 檢查是否符合已定義的 Security Policy
(2) 若涉及新增 API，確認是否有對應的 authentication/authorization 節點屬性（第 13.3 節 SHACL Shape）
(3) 若發現不符合政策，記錄為 Policy Exception 並標記需要的核准角色
```

### 38.9 Test Generation Prompt

```text
你是 Test Generation Agent。請針對 [Class/Method 名稱]：
(1) 查詢其關聯的 BusinessRule 節點
(2) 依據 BusinessRule 內容生成對應的測試案例
(3) 測試案例需涵蓋 BusinessRule 中的邊界條件（例如金額上下限）
```

### 38.10 Decision Recording Prompt

```text
你是任何執行決策的 Agent，在呼叫 record_decision() 時，請確保：
(1) category 使用團隊已定義的標準分類（避免自創分類造成查詢困難）
(2) reasoning 至少引用一個具體的 source_id 或既有 Decision id
(3) confidence 反映真實不確定性，不要一律填 1.0
(4) entities 欄位列出所有相關節點 id，以利後續因果鏈查詢
```

### 38.11 Audit Prompt

```text
你是 Audit Agent。請針對 [時間範圍] 內的所有 Decision：
(1) 使用 get_decision_insights() 取得統計概覽
(2) 找出 confidence < 0.7 的決策清單，標記需要人工複核
(3) 找出沒有對應 Evidence（reasoning 中未引用任何 source_id）的決策，標記為 Unsupported
(4) 產出稽核報告，格式需包含 decision_id、category、reasoning、outcome、confidence、source
```

### 38.12 本章 Checklist 與小結

- [ ] 11 種範本已依團隊實際 Agent 角色（第 23 章）分配並納入各 Agent 的系統提示
- [ ] 所有範本皆強制要求「引用 Evidence／Provenance」而非直接給答案

---

## 39. 銀行企業案例

> ⚠️ 本章為**教學示範用途之虛構情境**，非真實客戶專案（見開篇重要聲明第 6 點）。

### 39.1 情境設定

銀行 Web Application 涉及的核心實體：Account、Customer、Loan、Credit、Transaction、Payment、Risk、Compliance、Audit。

```mermaid
graph TB
    Customer2["Customer"] --> Account2["Account"]
    Customer2 --> Loan2["Loan"]
    Customer2 --> Credit2["Credit"]
    Account2 --> Transaction2["Transaction"]
    Transaction2 --> Payment2["Payment"]
    Loan2 --> Risk2["Risk"]
    Transaction2 -.->|"validated by"| Compliance2["Compliance"]
    Loan2 -.->|"validated by"| Compliance2
    Compliance2 --> Audit2["Audit"]
```

### 39.2 為什麼 Semantica 特別適合高可追溯性需求的企業 AI

- **Decision Intelligence**（第 11 章）讓每一次核貸/風控決策都有 `record_decision()` 記錄，可用 `find_precedents()` 確保同類案件判斷一致。
- **Provenance**（第 12 章）確保「這筆交易被標記為高風險」可以回溯到具體的規則版本與資料來源，符合官方文件提及的 SR 11-7 模型稽核軌跡、Basel III BCBS 239 等適用場景（官方已實作，Provenance Guide「Use Cases」）。
- **Conflict Detection**（第 8 章）避免 CRM 與核心銀行系統的客戶資料衝突被靜默覆蓋，這在授信決策中至關重要。

### 39.3 技術能力 ≠ 法規合規聲明（重申）

**必須再次強調**：Semantica 提供的是「技術能力」（Technical capability）——結構化記錄、追溯、問責的基礎設施。這不等於「實質法規合規」（Actual regulatory compliance）。是否符合 SOX、Basel III、洗錢防制法等規範，最終仍須由企業法遵、稽核與法務部門依實際流程與控制措施認定，Semantica 官方文件本身也未做出合規保證（官方已實作的限制聲明，見第 12.1、12.6 節）。

### 39.4 範例：AML 高風險交易規則（README 案例改編）

```python
from semantica.reasoning import ReteEngine, Rule, Fact, RuleType

rete = ReteEngine()
rete.build_network([
    Rule(
        rule_id="aml_flag",
        name="Flag high-risk transactions",
        conditions=[
            {"field": "amount", "operator": ">", "value": 10_000},
            {"field": "country", "operator": "in", "value": ["IR", "KP", "SY"]},
        ],
        conclusion="flag_for_compliance_review",
        rule_type=RuleType.IMPLICATION,
    ),
])

rete.add_fact(Fact("tx_001", "transaction", [{"amount": 15_000, "country": "IR"}]))
flagged = rete.match_patterns()

# 每筆標記都應同步記錄決策
graph.record_decision(
    category="aml_screening",
    scenario="tx_001: $15,000 匯款至受制裁國家",
    reasoning="觸發 aml_flag 規則（金額 > $10,000 且目的地國家在制裁清單）",
    outcome="flagged_for_compliance_review",
    confidence=0.97,
    decision_maker="rete-engine-aml",
    entities=["tx_001"],
)
```

### 39.5 本章 Checklist 與小結

- [ ] 已理解 Semantica 提供「技術可追溯性」而非「法規合規保證」，兩者不可混淆
- [ ] AML/授信等高風險決策規則已用 Rete/Forward Chaining 實作，而非完全交給 LLM 判斷
- [ ] 每筆自動化風控標記都有對應 `record_decision()`，確保可稽核

---

## 40. 與其他技術比較

| Technology | Vector | KG | GraphRAG | Provenance | Decision | Reasoning |
|---|---:|---:|---:|---:|---:|---:|
| Vector DB（Pinecone/Qdrant 等） | ✓ | | | | | |
| Neo4j | | ✓ | | | | |
| LangChain | | | | | | |
| LlamaIndex | | | | | | |
| 通用 GraphRAG 方案 | | ✓ | ✓ | | | |
| **Semantica** | ✓（內建 vector_store 模組） | ✓ | ✓ | ✓ | ✓ | ✓ |

### 40.1 比較說明（避免貶低其他工具）

- **Vector DB**：專精語意相似度檢索，效能與擴充性成熟，Semantica 本身就內建可切換的 vector_store 後端整合，**不是取代關係**。
- **Neo4j**：專精圖儲存與查詢引擎，Semantica 可以把 Neo4j 當作其 `semantica.kg` 的後端選項之一（第 6.4 節），**是搭配關係，而非競爭關係**。
- **LangChain / LlamaIndex**：專精 Agent 編排與 RAG 索引，Semantica 透過 REST/MCP 整合（第 17.5 節），**是互補關係**。
- **Semantica 的獨特定位**：它是同時涵蓋 KG + GraphRAG + Provenance + Decision + Reasoning 的**基礎設施層**（Infrastructure / Accountability Layer），而不是要在任何單一維度上「贏過」專精該維度的工具。

### 40.2 本章 Checklist 與小結

- [ ] 團隊已理解 Semantica 是疊加層，選型討論不應變成「Semantica vs LangChain 二選一」的錯誤框架
- [ ] 已依第 3.3 節判斷準則，確認現有問題確實需要 Provenance/Decision/Reasoning，而非僅需 Vector Search

---

## 41. 常見錯誤

1. **把 Semantica 當 Vector DB**：只用來做語意檢索，浪費了 Decision Intelligence 與 Provenance 的價值（第 2.2 節）。
2. **把 Semantica 當 LLM**：誤以為裝了 Semantica 就能提升模型推理能力，實際上它是外部知識與問責層，不改變 LLM 本身能力。
3. **把 Semantica 當 Agent Framework**：試圖用它取代 Agno/CrewAI/LangGraph 的編排邏輯（第 2.2 節）。
4. **所有資料全部丟進 KG**：未經 Ingestion Pipeline 篩選、Ontology 約束就把所有原始資料塞進圖，導致 Graph Analytics 失準、查詢效能下降（第 27 章）。
5. **沒有 Ontology**：跳過第 7、13 章的 Schema 設計，導致實體命名混亂（第 8 章 Entity Resolution 問題的根源）。
6. **沒有 Source Authority**：多來源衝突時沒有預先定義誰優先（第 25.2 節）。
7. **不做 Entity Resolution**：直接把「Customer」「CUSTOMER」「customer_id」當三個不同節點（第 8.1 節）。
8. **衝突資料直接 overwrite**：違背官方「flag and resolve, not silently overwrite」的核心設計哲學（第 8.3 節）。
9. **沒有 Provenance**：正式環境用 in-memory `ProvenanceManager`，重啟即遺失稽核軌跡（第 6.2、12.7 節）。
10. **所有 reasoning 都交給 LLM**：企業關鍵規則應搭配 Deterministic Reasoning 驗證（第 10.1 節）。
11. **沒有 Graph quality evaluation**：從未評估 Precision/Recall/Completeness（第 33 章）。
12. **沒有 access control**：誤以為 MCP Server 或 Policy Engine 會自動做存取控制（第 16.6、24.1 節已明確澄清都不會）。
13. **沒有 backup**：Graph Store／Provenance DB 沒有備份策略（第 28.3 節）。
14. **沒有 versioning**：Semantica 版本浮動安裝（`semantica>=0.6`），升級後 API 簽章變動導致 Production 出錯（第 31.4 節）。
15. **沒有 decision lifecycle**：只呼叫 `record_decision()` 但從未查詢 `find_precedents()`／`trace_decision_chain()`，決策記錄形同黑洞，沒有真正被使用（第 11 章）。

### 41.1 本章 Checklist 與小結

- [ ] 已逐條對照 15 項常見錯誤，確認團隊現況
- [ ] 已指派負責人修正目前踩到的錯誤項目

---

## 42. Troubleshooting

| 問題 | Symptom | Cause | Diagnosis | Solution | Prevention |
|---|---|---|---|---|---|
| pip install 失敗 | `pip install semantica[all]` 報錯 | Windows 缺少 VC++ Redistributable，或版本早於 v0.5.0 | 檢查 Python 版本與 Semantica 版本 | 安裝 VC++ Redistributable，升級至 v0.5.0+ | CI 映像檔預先包含 VC++ Redistributable |
| Python version 問題 | `import semantica` 報 SyntaxError | Python < 3.8（官方下限） | `python --version` | 升級至 ≥3.8，本手冊建議 3.11+（建議架構，非官方逐字要求） | venv 建立時鎖定 Python 版本 |
| dependency conflict | pip 解析相依套件失敗 | 多個 extras 版本要求衝突 | `pip install --dry-run` 檢視衝突套件 | 精簡安裝的 extras（第 5.6 節），避免同時裝過多後端 | 使用 `pip-compile`/`poetry lock` 鎖定版本 |
| LLM provider 問題 | LLM-based extraction 報認證錯誤 | API Key 未設定或已過期 | 檢查對應 Provider 環境變數 | 透過 Secret Manager 重新注入 Key（第 6.3 節） | Key 輪替流程自動化 |
| Graph Store 連線失敗 | `GraphBuilder(backend="neo4j")` 連線逾時 | Neo4j 服務未啟動或網路規則阻擋 | 檢查 `bolt://` 連線與防火牆規則 | 確認服務健康、開放對應 port | 健康檢查納入啟動流程（第 29.4 節 readinessProbe） |
| Vector Store 失敗 | `VectorStore(backend="pgvector")` 初始化錯誤 | PgVector extension 未安裝 | `SELECT * FROM pg_extension` 檢查 | `CREATE EXTENSION vector;` | 資料庫初始化腳本包含 extension 安裝 |
| MCP 失敗 | Claude Desktop 顯示 MCP Server 無回應 | `SEMANTICA_KG_PATH` 路徑錯誤或非絕對路徑 | 檢查 `claude_desktop_config.json` 設定 | 改用絕對路徑（第 16.3 節） | 設定範本納入路徑驗證腳本 |
| Entity Resolution 異常 | 大量誤合併（False Merge） | `similarity_threshold` 設定過低 | 檢視 `DuplicateDetector` 參數 | 調高 threshold 或改用更保守策略（第 8.2 節） | 定期用第 33 章指標評估 False Merge/Split 率 |
| Graph 太大 | 查詢效能急遽下降 | in-memory 後端已超出合理規模 | 檢查節點/邊數量級 | 切換至外部 Graph Store（第 27.2 節） | 提前規劃第 27.3 節環境分層架構 |
| Query 太慢 | Multi-hop Traversal 逾時 | `hops` 參數過大或索引缺失 | 檢視查詢的 hop 數與後端索引狀態 | 限制在 2-3 hop，補建索引 | 查詢前先做 Impact Analysis 範圍估算 |
| Provenance 不完整 | `get_statistics()` 顯示大量節點缺少來源 | Ingestion 流程未一致呼叫 Provenance 追蹤 | 抽樣檢查新節點的 `source_id` | 統一透過 Pipeline DSL（第 18.6 節）確保每步驟都記錄 Provenance | Code Review 檢查是否遺漏 Provenance 呼叫 |
| Decision 查不到 | `find_precedents()` 找不到預期的既有決策 | `category` 命名不一致（同義但拼法不同） | 檢查歷史決策的 `category` 分布 | 建立團隊標準分類清單（第 38.10 節） | Decision Recording Prompt 強制使用標準分類 |
| Docker 問題 | 容器啟動後立即結束 | 環境變數缺失導致啟動即 crash | `docker logs` 檢視錯誤訊息 | 補齊必要環境變數（第 6.1 節） | Compose 檔案設定 `depends_on` 與健康檢查 |
| Kubernetes 問題 | Pod 一直 CrashLoopBackOff | Readiness/Liveness Probe 設定過於嚴格，或 ConfigMap 未掛載 | `kubectl describe pod` 檢視事件 | 調整 probe 的 `initialDelaySeconds`，確認 ConfigMap/Secret 已正確掛載 | 部署前先在單一 replica 驗證健康檢查邏輯 |

### 42.1 本章 Checklist 與小結

- [ ] 團隊已將本章表格納入內部 Runbook
- [ ] 高頻問題（Provenance 不完整、Query 太慢）已建立自動化監控告警（第 26 章）

---

## 43. 完整企業 Reference Architecture

> 本章整合第 4、19、24、28、29 章的內容，繪製單一完整架構圖，供架構師簡報使用（建議架構）。

```mermaid
flowchart TB
    Users["Users"] --> WebApp["Web Application"]
    WebApp --> FE["Frontend<br/>(Vue3/TypeScript/PrimeVue)"]
    WebApp --> BE["Backend<br/>(Java25/Spring Boot 4.x)"]
    FE --> AIAgent2["AI Agent"]
    BE --> AIAgent2

    subgraph SemBlock["Semantica"]
        CTXG["Context Graph"]
        KGG["Knowledge Graph"]
        DIG["Decision Intelligence"]
        PROVG["Provenance"]
        REASG["Reasoning"]
        ONTG["Ontology"]
        GAG["Graph Analytics"]
    end
    AIAgent2 --> SemBlock

    subgraph Backends["儲存層"]
        GS2["Graph Store<br/>(Neo4j/FalkorDB/AGE)"]
        VS3["Vector Store<br/>(Qdrant/PgVector)"]
        ED["Enterprise Data<br/>(Git/DB/API/文件)"]
    end
    SemBlock --> Backends
```

### 43.1 元件說明

| 元件 | 說明 | 對應章節 |
|---|---|---|
| Web Application | 企業前後端應用，AI Agent 的服務對象與資料來源之一 | 第 19 章 |
| AI Agent | 開發、逆向工程、升版三大情境的執行者 | 第 17、20、21、23 章 |
| Context Graph | Agent 執行期工作記憶 | 第 3 章 |
| Knowledge Graph | 持久化企業知識資產 | 第 7 章 |
| Decision Intelligence | 決策記錄與因果追溯 | 第 11 章 |
| Provenance | W3C PROV-O 世系與稽核 | 第 12 章 |
| Reasoning | Deterministic 規則驗證 | 第 10 章 |
| Ontology | Schema 與約束管理 | 第 13 章 |
| Graph Analytics | Centrality/社群/影響分析 | 第 14 章 |
| Graph Store / Vector Store | 底層可替換儲存後端 | 第 6.4、27 章 |
| Enterprise Data | 資料源頭 | 第 18 章 |

### 43.2 本章 Checklist 與小結

- [ ] 本圖已用於內部架構評審簡報，並取得利害關係人共識
- [ ] 每個元件都已對應到明確的負責團隊（呼應第 36.2 節 RACI）

---

## 44. Demo Project

### 44.1 專案骨架（建議架構）

```text
semantica-ai-software-engineering-demo/
├── README.md
├── requirements.txt
├── config/
│   └── semantica.yaml           # Graph/Vector Store、LLM Provider 設定（第 6 章）
├── data/
│   ├── requirements/            # 需求文件範例
│   └── legacy-source/           # 逆向工程情境用的範例原始碼
├── ontology/
│   └── software_dev_ontology.ttl   # 第 7、13 章的軟體開發 Ontology
├── scripts/
│   ├── 01_ingest.py
│   ├── 02_extract.py
│   ├── 03_build_kg.py
│   ├── 04_deduplicate.py
│   ├── 05_record_decisions.py
│   └── 06_export_report.py
├── src/
│   └── agents/
│       ├── requirement_agent.py
│       ├── coding_agent.py
│       ├── migration_agent.py
│       └── audit_agent.py
├── tests/
│   ├── test_kg_build.py
│   ├── test_reasoning_rules.py
│   └── golden_kg/
│       └── golden_kg_baseline.json   # 第 32.2 節 Golden KG
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml       # 第 29.2 節
├── k8s/
│   └── semantica-server.yaml    # 第 29.4 節
├── mcp/
│   └── claude_desktop_config.example.json  # 第 16.3 節
└── docs/
    └── architecture.md
```

### 44.2 關鍵程式碼：`scripts/03_build_kg.py`（示意）

```python
"""示意腳本：串接 Ingest -> Extract -> Build KG -> Deduplicate -> Export"""
from semantica.ingest import FileIngestor
from semantica.semantic_extract import NERExtractor, RelationExtractor
from semantica.kg import GraphBuilder
from semantica.deduplication import DuplicateDetector, EntityMerger
from semantica.export import RDFExporter

def main():
    sources = FileIngestor().ingest("data/requirements/")

    ner = NERExtractor(method="pattern")
    rel = RelationExtractor(method="rule")

    all_entities, all_relationships = [], []
    for source in sources:
        entities = ner.extract(source)
        relationships = rel.extract(source, entities=entities)
        all_entities.extend(entities)
        all_relationships.extend(relationships)

    detector = DuplicateDetector(similarity_threshold=0.75, use_clustering=True)
    groups = detector.detect_duplicate_groups(all_entities)
    merger = EntityMerger(preserve_provenance=True)
    merged_ops = merger.merge_duplicates(all_entities, strategy="keep_most_complete")

    kg = GraphBuilder(merge_entities=True, enable_temporal=True).build({
        "entities": all_entities,
        "relationships": all_relationships,
    })

    RDFExporter().export(kg, "data/output/kg_snapshot.ttl", format="turtle")

if __name__ == "__main__":
    main()
```

### 44.3 關鍵程式碼：`src/agents/migration_agent.py`（示意，對應第 21 章）

```python
"""示意 Migration Agent：查詢 Breaking Change、驗證 Migration Rule、記錄決策"""
from semantica.context import ContextGraph

class MigrationAgent:
    def __init__(self, graph: ContextGraph):
        self.graph = graph

    def propose_migration(self, class_id: str, target_framework: str) -> str:
        breaking_changes = self.graph.get_neighbors(class_id, edge_types=["CAUSED_BY"])
        if not breaking_changes:
            raise ValueError(f"{class_id} 無對應 BreakingChange 節點，禁止臆測性修改")

        decision_id = self.graph.record_decision(
            category="framework_migration",
            scenario=f"{class_id} 遷移至 {target_framework}",
            reasoning=f"依據 {breaking_changes[0].id} 官方 Breaking Change 記錄",
            outcome="migration_proposed",
            confidence=0.85,
            decision_maker="migration-agent-demo",
            entities=[class_id],
        )
        return decision_id
```

### 44.4 本章 Checklist 與小結

- [ ] Demo Project 已能在本機完整跑通 `scripts/01_ingest.py` 至 `06_export_report.py`
- [ ] `tests/golden_kg/` 已建立基準快照供團隊練習 Regression Test（第 32.2 節）
- [ ] 新進成員已能依此 Demo 骨架複製到自己團隊的實際專案

---

## 45. 學習路線

| Level | 主題 | 學習目標 | 必學概念 | 實作 | 驗收標準 |
|---|---|---|---|---|---|
| 1 | Semantica 基礎 | 理解定位與安裝 | 第 2、5 章 | 完成安裝 + `semantica doctor` | 能解釋 Semantica「是什麼／不是什麼」 |
| 2 | Knowledge Graph | 建立第一個 KG | 第 4.5、7 章 | 跑完 6 步驟 Quickstart | 能用 `add_node`/`add_edge` 建立自訂圖 |
| 3 | Context Graph | 理解執行期上下文 | 第 3 章 | 建立一個 `AgentContext` 並查詢 | 能解釋 Context Graph 與 KG 的差異 |
| 4 | GraphRAG | 混合檢索問答 | 第 15 章 | 對 Demo Project 資料跑一次 GraphRAG 問答 | 答案能附上 `source_id` |
| 5 | Decision Intelligence | 決策記錄與追溯 | 第 11 章 | 完成 5 次 `record_decision()` 並互相關聯 | 能用 `trace_decision_chain()` 重建因果鏈 |
| 6 | Provenance | 稽核與世系 | 第 12 章 | 設定 SQLite 持久化並跑 `verify_chain()` | 能對任一節點完整回溯來源 |
| 7 | AI Agent + MCP | 讓 Claude Code 使用 Semantica | 第 16、17 章 | 完成 MCP 設定並在 Claude Code 中查詢 | Claude Code 可成功呼叫至少 3 個 MCP tools |
| 8 | 逆向工程 | 分析既有系統 | 第 20 章 | 對 Demo Project 的 legacy-source 跑完整分析 | 能回答第 20.4 節列出的 11 個問題 |
| 9 | Framework Upgrade | AI 輔助升版 | 第 21 章 | 模擬一次 Java/Spring Boot 升版決策鏈 | 能回答第 21.5 節的 7 個關鍵問題 |
| 10 | 企業 AI Governance | 治理與稽核 | 第 24-26、36 章 | 完成一次內部 Security Review + RACI 制定 | 通過內部治理評審 |

### 45.1 本章 Checklist 與小結

- [ ] 團隊已依角色分配對應 Level（開發者著重 1-5、7-9；架構師著重全部；稽核著重 1、6、10）
- [ ] 每個 Level 都已有對應的內部教育訓練時段排定

---

## 46. FAQ：最終 20 個問題

**1. Semantica 到底解決什麼問題？**
解決 AI Agent 缺乏「可查詢、可追溯、可問責的結構化上下文」的問題——讓 Agent 的每個答案、每個決策都能回溯到具體來源與因果鏈（第 1、2 章）。

**2. 為什麼 AI Agent 需要 Context Graph？**
因為 LLM 本身無狀態，單純的對話歷史或向量檢索無法表達實體間的結構化關係與跨 Session 的一致決策記憶（第 3.1 節）。

**3. Knowledge Graph 與 Vector DB 有什麼不同？**
Vector DB 做語意相似度檢索；Knowledge Graph 表達結構化的實體與關係，並可疊加 Provenance／Decision／Reasoning。Semantica 內部同時整合兩者（第 3 章）。

**4. Semantica 與 LangChain 的關係？**
互補關係。LangChain 負責 Agent 編排與工具呼叫，Semantica 負責其下的 Context/KG/Decision 基礎設施，透過 REST/MCP 整合（第 2.4、17.5、40 章）。

**5. Semantica 與 LlamaIndex 的關係？**
同上，互補而非取代。LlamaIndex 專精 RAG 索引，Semantica 提供更結構化、可問責的知識層（第 40 章）。

**6. Semantica 與 GraphRAG 的關係？**
GraphRAG 是一種檢索模式（圖 + 向量混合檢索），Semantica 原生實作了這個模式，並額外整合 Decision/Provenance（第 15 章）。

**7. Semantica 如何記錄 AI Decision？**
透過 `record_decision()` API，把決策記錄為圖中的一級公民節點，包含 category、scenario、reasoning、outcome、confidence 等欄位，並可建立因果鏈（第 11 章）。

**8. Semantica 如何實現 Provenance？**
透過 `ProvenanceManager`，依 W3C PROV-O 標準追蹤每個實體/關係的來源、產生活動、代理人，並用 SHA-256 串接式校驗碼確保完整性（第 12 章）。

**9. W3C PROV-O 為什麼重要？**
它是國際標準的來源追溯詞彙表，讓 Provenance 記錄可互通、可匯出給稽核方，而非企業自創、無法被外部驗證的私有格式（第 12.2 節）。

**10. Semantica 是否需要 LLM？**
不一定。Pattern-based/Rule-based 的 Ingestion、Extraction、Reasoning 完全不需要 LLM API Key（第 4.5 節 Quickstart 即為範例）；LLM-based 方法（例如語意抽取、GraphRAG 生成）才需要透過 `semantica.llms` 呼叫外部 LLM Provider。

**11. Entity Resolution 為什麼重要？**
避免同一實體因命名差異被誤判為多個節點，破壞 Graph Analytics 準確性與查詢完整性（第 8.1 節）。

**12. Conflict Detection 如何工作？**
偵測多來源資料的 value/type/relationship/temporal/logical 衝突，標記而非靜默覆蓋，再依 credibility-weighted／most-recent／voting 等策略解決，同時保留原始 Fact 的 Provenance（第 8.3 節）。

**13. 如何做 Reverse Engineering？**
用外部 AST/Static Analysis 工具掃描原始碼，把結構化結果匯入 Semantica KG，疊加 Business Rule、Requirement、Test 等企業實體，再由 AI Agent 透過 GraphRAG 與 Graph Analytics 產出報告（第 20 章，特別注意第 20.2 節的工具分工邊界）。

**14. 如何做 Framework Upgrade？**
把官方 Migration Guide 轉為 Deterministic Rule，建立 Breaking Change 節點，用 Multi-hop Impact Analysis 找出受影響範圍，AI Agent 依規則驗證後修改程式碼並記錄決策（第 21 章）。

**15. 如何讓 Claude Code 使用 Semantica？**
安裝 `semantica-mcp`，在 Claude Desktop/Code 設定檔加入 MCP Server 條目，指定絕對路徑的 `SEMANTICA_KG_PATH`（第 16.3、17.1 章）。

**16. 如何讓 GitHub Copilot 使用 Semantica？**
目前無官方原生 Plugin，需透過 REST API 或 CI 流程間接提供 Context（第 17.2 節，標示為建議架構）。

**17. 如何透過 MCP 整合 Agent？**
Agent 端設定 MCP Client 指向 `semantica-mcp`（stdio），即可呼叫 12 個 tools 與 3 個 resources（第 16 章）。

**18. 如何部署 Production？**
Docker/Podman 容器化 `semantica-server`／`semantica-worker`，外接 Graph Store／Vector Store，搭配 Kubernetes 做水平擴充與 HPA，並落實第 24 章 Security（第 28、29 章）。

**19. 如何維護 Knowledge Graph？**
依第 34 章每日/每週/每月 Checklist，持續處理 Conflict/Duplicate 待審核佇列、審查 Ontology、驗證 Provenance 完整性。

**20. 企業導入 Semantica 最重要的成功條件是什麼？**
不是技術安裝，而是**組織紀律**：堅持所有關鍵 AI 決策都呼叫 `record_decision()`、堅持 Ontology 治理不各自為政、堅持 Provenance 持久化而非圖方便用 in-memory、以及明確區分「技術可追溯性」與「法規合規」的界線（第 25、36、39.3 節）。

---

## 47. 結論

Semantica 提供的不是「讓 AI 看起來更聰明」的技巧，而是一套讓 AI Agent 能夠：

```text
Know（掌握結構化知識）
 ↓
Understand（理解實體間關係）
 ↓
Reason（可解釋的推理）
 ↓
Decide（有記錄的決策）
 ↓
Explain（可說明理由）
 ↓
Trace（可回溯來源）
 ↓
Audit（可被稽核）
 ↓
Improve（持續依先例改善）
```

的基礎設施。企業導入的價值不在於取代既有的 LLM、Agent Framework 或 Vector Database，而在於補上這些工具長期缺乏的一塊：**問責（Accountability）**。

本手冊三大情境（Web Application 開發、逆向工程、Framework Upgrade）示範的核心手法是一致的：**任何交給 AI Agent 的關鍵決策，都應該可以被追問「為什麼」「依據什麼」「誰核准」「測試過了嗎」「如果錯了，誰會受影響」，並且這些答案能在數秒內從 Knowledge Graph 中查到，而不是靠工程師事後翻找 Slack 紀錄或猜測。**

這正是 Explainable AI（可解釋）、Traceable AI（可追溯）、Auditable AI（可稽核）、Governed AI（可治理）在企業軟體工程場景中的具體落地方式。

---

## 附錄 A：官方參考來源

| 來源 | URL | 用途 |
|---|---|---|
| GitHub Repository | `https://github.com/semantica-agi/semantica` | 原始碼、README、Release Notes |
| 官方文件站 | `https://docs.getsemantica.ai/` | Concepts、Guides、Cookbook、FAQ |
| PyPI | `https://pypi.org/project/semantica/` | 套件安裝、版本資訊 |
| 官方網站 | `https://getsemantica.ai/` | 產品定位、企業方案 |
| GitHub Releases | `https://github.com/semantica-agi/semantica/releases` | Changelog |
| Discord | `https://discord.gg/sV34vps5hH` | 社群討論 |
| GitHub API（直接查證） | `api.github.com/repos/semantica-agi/semantica` | 2026-08-20 用於直接核對星數／Forks／建立日期／最近 Push 時間，避免搜尋引擎快取的過期數字（見開篇重要聲明第 8 點與版本速查表） |

**第三方交叉驗證來源（僅用於佐證專案真實存在與活躍度，不單獨作為事實依據，優先順序低於上述官方來源）**：Hacker News「Show HN: Semantica」發佈串（2026-01-07）、GitHub Trending 收錄頁面、獨立部落格評測文章。

**⚠️ 命名易混淆來源警示**：搜尋「Semantica」時常見以下**非本手冊所述專案**的無關結果，查證/採購評估時務必辨明：`ai-semantica.com`（AI 品牌能見度／SEO 分析工具，與本專案完全無關）、GitHub 上其他同名但非本專案分支的 Repository（例如 `Hawksight-AI/semantica`）。詳見開篇重要聲明第 8 點。

## 附錄 B：研究來源分級

本手冊撰寫時，依下列優先順序處理不同來源間的資訊差異（呼應開篇重要聲明第 3 點的五層 Provenance 標示）：

```text
官方最新 Release
    >
官方文件（docs.getsemantica.ai）
    >
GitHub README / main 分支
    >
PyPI metadata
    >
第三方文章（僅用於交叉驗證，不單獨作為事實依據）
```

本手冊查證時點（2026-08-20）確認的版本基準為 **v0.6.5**（2026-08-11 發布），為當時最新版本，無更新版本存在。查證方式包含直接呼叫 GitHub API（避免搜尋引擎快取數字）、讀取 `pyproject.toml`／`README` 原始檔、比對 GitHub Releases 逐版 Changelog、以及嘗試存取 `docs.getsemantica.ai` 各 Guide 頁面。查證結果：手冊原始版本記載的核心事實（Repository 存在性、版本號、CLI 指令、MCP 12 個 tools、模組清單、後端支援清單、Agno/CrewAI first-class 整合等）**皆與官方來源相符**，僅在少數細節（RDF 後端清單不完整、Editor Plugin 少列 OpenClaw、v0.6.5 安全修補描述過於簡略、部分模組確切 import 路徑與 MCP resources 確切數量未能逐字確認）有需要補強或軟化語氣之處，已於本次更新逐一修正並標示對應 Provenance 等級。若你閱讀本手冊時 Semantica 已發布更新版本，請依本附錄的優先順序重新查證所有標示為「官方已實作」的內容。

## 附錄 C：全書 Checklist 總覽

> 以下彙整全書各章節末的 Checklist，供企業導入時逐項勾選使用（完整說明請回頭參閱各章節）。

**基礎建置**：

- [ ] 已理解 Semantica「是什麼／不是什麼」（第 2 章）
- [ ] 已完成安裝並執行 `semantica doctor`（第 5 章）
- [ ] Provenance 已設定 SQLite 持久化（第 6.2 章）
- [ ] 已設計軟體開發 Ontology 並套用 SHACL 驗證（第 7、13 章）

**核心能力**：

- [ ] Entity Resolution／Conflict Detection 策略已明確定義（第 8 章）
- [ ] 企業關鍵規則已用 Deterministic Reasoning 實作（第 10 章）
- [ ] 所有關鍵 AI 決策都呼叫 `record_decision()`（第 11 章）
- [ ] Provenance 覆蓋率已納入監控指標（第 12、26 章）

**企業情境落地**：

- [ ] Web Application 開發情境已完成 Requirement→Deployment 全鏈路建模（第 19 章）
- [ ] 逆向工程情境已釐清 Semantica 與外部 AST 工具的分工邊界（第 20 章）
- [ ] Framework Upgrade 情境可回答第 21.5 節 7 個關鍵問題（第 21 章）

**治理與維運**：

- [ ] Security Architecture 已補強 Semantica 未內建的 Authentication/Authorization（第 24 章）
- [ ] RACI 與五階段導入方法論已與利害關係人取得共識（第 36 章）
- [ ] HA/Backup/DR、Docker/K8s 生產部署已完成（第 28、29 章）
- [ ] 每日/每週/每月維護 Checklist 已排入 On-call 排班（第 34 章）
- [ ] Semantica 版本已鎖定明確版本號，升級走完整 SOP（第 31.4、35 章）

**團隊賦能**：

- [ ] AI Agent Team 角色與讀寫權限已明確劃分（第 23 章）
- [ ] 11 種 Prompt 範本已分配給對應 Agent（第 38 章）
- [ ] 學習路線 Level 1-10 已排入內部教育訓練（第 45 章）

---

*本手冊完。如發現內容與你實際安裝的 Semantica 版本不符，請以官方最新文件為準，並歡迎更新本手冊對應章節的 Provenance 標示。*

