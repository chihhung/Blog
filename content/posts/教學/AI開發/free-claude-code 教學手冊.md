+++
date = '2026-05-02T17:01:09+08:00'
draft = false
title = 'Free Claude Code 教學手冊'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

在人工智慧領域，「prompt」指的是用戶輸入給 AI 模型的文字指令或問題，用來引導模型產生回應。它是你與 AI 溝通的起點，影響 AI 回應的內容、品質與風格。

🧠 Prompt 是什麼？

- 是一段文字、問題或指令，用來告訴 AI 你想要什麼樣的回應。
- 在語言模型（如 ChatGPT）中，prompt 可以是簡單的問題，也可以是複雜的任務描述。
- 好的 prompt 能讓 AI 更準確地理解你的需求，產生有價值的內容。

✍️ Prompt 的用途

- 問問題：例如「台灣和日本的時差是多少？」
- 請求創作：例如「幫我寫一篇關於氣候變遷的文章。」
- 角色扮演：例如「假設你是面試官，請問我三個技術問題。」
- 資料整理：例如「請將以下資訊整理成表格。」

🔧 如何撰寫高品質的 Prompt？

| 技巧 | 說明 | 範例 |
| --- | --- | --- |
| 明確具體 | 避免模糊用詞 | 「請列出三個影響員工流動率的因素」 |
| 設定格式 | 指定回應方式 | 「請用條列式說明」 |
| 提供背景 | 增加上下文 | 「假設你是 HR 經理，請撰寫招募建議書」 |
| 指定語氣 | 控制風格 | 「請用正式且精煉的語氣撰寫報告」 |
| 範例引導 | 示範期望格式 | 「請參考以下格式翻譯這段文字」 |
======================================================

# 如何撰寫專案的 Prompt

## 角色設定

- 確定 AI 的角色，例如「專案經理」、「技術架構師」或「UI/UX 設計師」，這有助於 AI 理解其應該採取的視角。

## 任務描述

- 清楚描述 AI 需要完成的任務，例如「撰寫專案計劃」、「設計系統架構」或「撰寫使用者故事」。

## 具體要求

- 提供明確的指示和期望結果，例如「請使用 Markdown 格式撰寫文檔」或「請提供 API 的詳細設計」。

## 範例和格式

- 如果有特定的格式或範例，請在 Prompt 中提供，這樣 AI 可以更好地理解你的需求。

# 如何建立專案的 Prompt

1. 確定專案目標：明確定義專案的最終目標和需求，這將成為撰寫 Prompt 的基礎。

2. 收集相關資訊：蒐集與專案相關的所有資訊，包括技術細節、業務需求和使用者故事等。

3. 撰寫初步 Prompt：根據收集的資訊，撰寫一個初步的 Prompt，描述你希望 AI 完成的任務。

4. 測試和調整：使用初步的 Prompt 進行測試，觀察 AI 的回應是否符合預期。根據結果調整 Prompt，使其更精確。

# 如何撰寫prompt產生專案範本

## 角色設定

- 你是一位資深專案經理,同時也是資深技術架構師，負責設計一個大型共用平台專案。

## 任務描述

- 有一個大型專案需要透過AI完成SSDLC的開發任務.
- 首先針對SSDLC 的各個階段，列出有那些階段，並且針對每個階段，列出各階段的工作項目.
- 針對每個工作項目，列出所需的技術細節和業務需求。
- 建立各階段範本所需的prompt,並且確保這些prompt能夠清楚地指導團隊成員如何使用這些範本。
- 先透你產出的prompt,讓AI能夠理解專案的需求和範本的使用方式。
- 請一步步建立專案的 prompt，並確保這些 prompt 能夠清楚地指導AI建立專案範本。
- AI在建立專案範本時，必須遵循以下步驟：
  1. 確認專案目標和需求。
  2. 收集相關資訊，包括技術細節和業務需求。
  3. 撰寫初步的 Prompt，描述希望 AI 完成的任務。
  4. 測試和調整 Prompt，以確保其精確性和有效性。
  5. 生成專案範本時,可時必須包含以下內容：
     - 各階段的工作項目清單
     - 每個工作項目的技術細節和業務需求
     - 各階段的範本與範例同時增加指導說明
  5. 最終生成專案範本，並確保其符合 SSDLC 的各個階段要求。

## 具體要求

- 請使用 Markdown 格式撰寫文檔
- 提供範例和格式，讓 AI 能夠更好地理解你的需求。
- 請把產出各階段的範本與範例，放在專案文件夾中，.github\prompts\
- 可針針對不同階段在.github\prompts\ 中建立不同的子目錄，例如：
  - .github\prompts\需求分析
  - .github\prompts\設計開發
  - .github\prompts\測試驗收
  - .github\prompts\部署運維
- 在不同階段下不同的子目錄中，放置對應的範本和範例文件，依其功能給予清晰的命名，副檔名統一為 .md。
- 你需要逐步建立專案的 prompt，並確保這些 prompt 能夠清楚地指導團隊成員如何使用這些範本。

# 建立專案資料庫設計指引

## 角色設定

你是一位資深的資料庫架構師與系統分析師，熟悉金融業大型系統的資料庫設計，並精通多種關聯式資料庫（Oracle、DB2、PostgreSQL、SQL Server）。

## 專案背景

- 銀行大型共用平台
- 支援多租戶與跨系統資料整合
- 遵循 SSDLC 安全規範
- 需具備高可用（HA）與高擴充性（Scalability）

## 任務

建立一份「專案資料庫設計指引」，需包含：

1. 資料庫命名規範（資料庫、Schema、Table、Column、Index、View、Function、Trigger）
2. 欄位設計準則（資料型別、長度、允許 Null、預設值）
3. 主鍵、外鍵與唯一鍵設計規範
4. 索引策略（單欄、多欄、唯一索引、全文索引）
5. 資料分區與分表策略
6. 資料庫正規化與反正規化設計
7. 資料安全規範（加密、遮蔽、存取權限、稽核）
8. 資料庫版本控管與變更管理方法
9. 性能調校原則與監控方法
10. 資料庫備份與災難復原計劃
11. 資料庫容量規劃
12. 資料庫升級與遷移策略
13. 資料庫日誌管理
14. 資料庫測試與驗證
15. 資料庫文件與註解
16. 資料庫自動化與工具
17. 資料庫監控與維護
18. 資料庫性能測試

## 輸出要求

- 使用繁體中文
- 以 Markdown 格式輸出
- 每個章節需條列化
- 提供 Oracle ,DB2 ,SQL Server,PostgreSQL 的 SQL 範例
- 安全部分需符合 OWASP 與 PCI DSS 要求
- 其他資料庫相關的最佳實踐與建議
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:資料庫設計指引.md，並使用 Markdown 格式撰寫

# 專案前端開發指引

## 角色設定

你是一位資深的前端架構師與 UI/UX 專家，熟悉大型金融級 Web 專案的開發規範與最佳實踐。

## 專案背景

- 採前後分離架構，前端為 SPA (Single-Page Application)。
- 採用 Vue 3.x、TypeScript、Tailwind CSS 開發，支援微前端架構。
- 後端為 Spring Boot 3.5.x，透過 RESTful API 與前端串接。
- 專案需支援多語系、RWD、跨瀏覽器相容性（Chrome/Edge/Firefox/Safari）。
- 開發工具使用 VS Code，版本管理使用 GitHub。

## 任務

請建立一份「前端開發指引」，內容需完整且適用於上述專案背景，至少包含以下章節：

1. 專案目錄與檔案結構規範
2. 命名規範（檔案、資料夾、變數、函式、元件）
3. 程式撰寫風格與 Lint 設定（ESLint、Prettier）
4. 元件開發規範（Vue 單檔元件 SFC 結構、Props、Emit、Slots 使用）
5. 樣式與 Tailwind CSS 規範（RWD、顏色與字型設定、共用樣式）
6. API 串接與資料存取規範（Axios、錯誤處理、攔截器設定）
7. 狀態管理規範（Pinia/其他）
8. 多語系處理規範（i18n 結構、翻譯檔命名）
9. 測試規範（單元測試、E2E 測試）
10. 安全性考量（XSS、防止 CSRF、敏感資訊處理）
11. 版本控制與分支策略
12. 專案建置與部署流程
13. 程式碼審查（Code Review）規範
14. 常見錯誤處理與 Debug 流程

## 產出要求

- 請以 Markdown 格式輸出
- 每個章節需有詳細說明與範例程式碼
- 提供必要的設定檔範例（如 eslint.config.js、tailwind.config.js、vite.config.ts 等）
- 內容需明確、可直接被開發團隊採用
文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:前端開發指引.md，並使用 Markdown 格式撰寫

# UI/UX 開發指引

## 角色設定

你是一位資深 UI/UX 設計師與前端架構師，熟悉銀行與大型平台系統的使用者體驗設計、易用性規範、無障礙設計，以及 Vue 3、Tailwind CSS、TypeScript 等前端技術。

## 專案背景

- 系統性質：大型共用平台（金融業為主）
- 架構：前後端分離，前端採微前端 + SPA 架構
- 前端技術：Vue 3.x、Tailwind CSS、TypeScript
- 使用者族群：內部員工、企業客戶與一般客戶
支援裝置：桌機、平板、手機（RWD）

## 任務描述

請依以下需求產出 完整的 UI/UX 開發指引 文件，內容需涵蓋以下面向：

1. 設計原則

   - 銀行系統的安全性與一致性要求
   - 清晰的資訊層次與導航設計
   - 金融資料顯示與重點突顯的規範
   - 無障礙（WCAG 2.1 AA 級）與多語系支援

2. UI 元件規範

   - 樣式（字體、字級、間距、顏色、按鈕樣式）
   - 響應式排版（Desktop/Tablet/Mobile 規格）
   - 常用元件設計（表單、按鈕、表格、圖表、提示訊息）

3. UX 流程規範

   - 表單驗證與錯誤回饋
   - 使用者引導（Onboarding）
   - 搜尋、篩選與排序互動設計
   - 資料載入與 Loading/Empty/Error 狀態設計

4. 設計資產與交付

   - 原型與設計稿（Figma/Sketch）
   - 設計 Token（顏色、字型、間距等）
   - 元件庫與設計系統（Storybook 或自建）
   - 前端實作規範

5. Vue 3 + Tailwind CSS 最佳實踐

   - 元件命名與資料綁定規範
   - 可重用 UI 元件與樣式變數管理

6. 檢測與驗證

   - UI 測試（Visual Regression Testing）
   - 可用性測試（Usability Testing）
   - 無障礙檢測（Accessibility Audit）

## 產出格式

- 請以 Markdown 文件 形式輸出，結構清楚、條列分明，並附上範例程式碼與設計圖示（以描述方式）。
- 內容需明確、可直接被開發團隊採用
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:UIUX指引.md，並使用 Markdown 格式撰寫。

# 系統分析指引

## 角色設定

你是一位資深的系統分析師與解決方案架構師，擁有超過15年在大型金融系統與企業級平台開發的經驗，熟悉 SSDLC（安全軟體開發生命週期）、系統分析方法論（例如 UML、DFD、用例分析）、需求訪談技巧與系統整合。

## 專案背景

- 專案性質：大型共用平台（前後端分離架構）
- 技術棧：前端 Vue 3.x + Tailwind CSS + TypeScript，後端 Spring Boot 3.5.x + Clean Architecture
- 資料庫：Oracle、DB2、PostgreSQL
- 支援 REST API、批次處理、SFTP/FTPS、MQ
- 遵循 SSDLC 與 OWASP 安全規範

## 產出目標

請產生一份《專案系統分析指引》，內容需包含：

1. **系統分析階段目標與產出物**
   - 明確描述該階段的工作範圍與目標
   - 列出需產出的文件、圖表、規格書清單
2. **需求收集與分析流程**
   - 如何進行需求訪談、需求驗證與優先級排序
   - 涉及的角色與職責
3. **系統分析方法與工具**
   - UML、DFD、ERD、用例圖、活動圖等使用時機
   - 分析模型與資料流設計
4. **跨系統整合分析**
   - API 與批次整合點的需求分析
   - 資料交換格式與協定（JSON、XML、CSV）
5. **安全與合規考量**
   - SSDLC 中的安全分析步驟
   - 法規遵循（如 GDPR、ISO 27001、金融資安規範）
6. **版本控管與審核流程**
   - 分析文件如何進行版本管理與審核
7. **範例與模板**
   - 提供需求規格書、用例描述表、系統功能列表的範例模板

## 產出格式

- 使用 Markdown 格式
- 條列式與分段說明
- 關鍵步驟需搭配範例或模板格式
- 以繁體中文撰寫
- 文件請放在專案的 .github\指引\需求分析\目錄下,檔名為:系統分析指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

# 架構設計指引

## 角色設定

- 你是一位資深系統架構師與解決方案專家，熟悉銀行及大型企業級系統開發，具備豐富的微服務架構、雲端部署、資料庫設計、資安防護、效能調校與高可用性設計經驗。

## 專案背景

- 專案性質：大型共用平台，支援多業務系統
- 前端技術：Vue 3.x、Tailwind CSS、TypeScript、微前端架構
- 後端技術：Spring Boot 3.5.x（Java 21）、Clean Architecture
- 支援資料庫：Oracle、DB2、SQL Server、PostgreSQL
- 部署方式：容器化（Podman / Kubernetes）
- 必須支援：RWD、RESTful API（Swagger）、多語系
- SSDLC 安全需求：OWASP Top 10 防護、身分驗證、授權控管、API 安全、日誌監控

## 任務描述

請依據上述背景，產生完整的「系統架構設計指引文件」。
內容需包含：

1. 架構設計原則
2. 系統整體架構圖（微服務拆分與 API Gateway）
3. 前後端分離與微前端設計
4. 後端分層架構（Clean Architecture）
5. 資料庫設計原則（多資料庫支援、分片、讀寫分離）
6. 效能優化方案（快取、CDN、非同步處理、負載平衡）
7. 高可用性與災難復原設計（Active-Active / Active-Standby）
8. 安全機制（身分驗證、授權、加密、API 防護、資安日誌）
9. 系統監控與日誌管理（APM、分散式追蹤、日誌聚合）
10. 開發與部署流程（CI/CD、測試策略、自動化部署）

## 產出格式要求

- 以 Markdown 格式輸出
- 每個章節有簡短說明 + 清單
- 架構圖與流程圖用 Mermaid 語法產生
- 重要技術詞彙加粗
- 提供範例設定（如 application.yml、資料庫 schema 範例）
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:架構設計指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

# 系統設計指引

## 角色設定

你是一位資深系統架構師與系統分析師，熟悉大型金融系統、微服務架構、前後端分離設計、資料庫設計、安全規範（如 OWASP、ISO 27001）與系統整合模式。
你具備將系統需求轉換成可落地、可維運且具擴展性的系統設計文件的能力。

## 專案背景

- 專案名稱：[專案名稱]

- 系統型態：大型共用平台 / 微服務架構 / 金融業系統
- 前端技術：Vue 3.x + TypeScript + Tailwind CSS
- 後端技術：Spring Boot 3.5.x（Clean Architecture）
- 資料庫：Oracle / DB2 / SQL Server / PostgreSQL
- 其他元件：Redis / Kafka / SFTP / API Gateway / CDN / 多語系
- 系統需求來源：已完成系統分析文件（SAD）

## 任務描述

請產生**「專案系統設計指引」**文件，內容需指導開發團隊如何從系統分析文件轉換到系統設計文件，並涵蓋以下重點：

1. 系統架構設計

   - 分層架構圖（前端、後端、資料庫、外部系統）
   - 微服務拆分原則與邊界劃分
   - API Gateway、Load Balancer、CDN 與 Cache 使用策略
   - 高可用（HA）與災難復原（DR）設計

2. 模組與服務設計

   - 每個服務的職責、依賴關係與通訊方式（REST / gRPC / MQ）
   - 資料流與控制流設計圖
   - 同步與非同步處理策略

3. 資料庫設計

   - 資料模型設計規範（ERD、正規化、索引策略）
   - 分庫分表 / 讀寫分離策略
   - 資料安全與加密規範

4. 安全性設計

   - 認證與授權機制（OAuth2 / OpenID Connect / SAML）
   - API 安全（JWT、HMAC、Rate Limit）
   - 資料傳輸加密（HTTPS / TLS）
   - OWASP Top 10 防護策略

5. 整合與介接設計

   - 外部系統 API 規範
   - 批次作業設計（Spring Batch / Quartz）
   - SFTP / FTPS 上傳下載流程

6. 系統非功能需求設計

   - 性能與擴展性（水平 / 垂直擴展）
   - 系統監控與日誌規範（Prometheus / ELK）
   - SLA 與 SLO 指標設定

7. 交付格式與附錄

   - 統架構圖（高層 / 模組 / 部署架構）
   - 資料庫設計文件（ERD、Schema）
   - API 規格文件（Swagger / OpenAPI）
   - 安全性檢核清單

## 輸出要求

- 產出完整的「系統設計指引」初稿（Markdown 格式）
- 使用結構化標題（H1~H3）
- 附帶必要的範例圖（可用mermaid）
- 語言使用繁體中文，專業且條列清楚
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:系統設計指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

# 後端開發指引

## 角色設定

你是一位資深後端架構師與全端開發專家，熟悉大型金融級平台的後端開發、微服務架構、API 設計、資料庫優化、安全性與效能調校，並熟悉 SSDLC（安全軟體開發生命週期）最佳實務。

## 專案背景

- 專案類型：大型共用平台（支援前後端分離，微前端架構）

- 前端：Vue 3.x、Tailwind CSS、TypeScript

- 後端：Spring Boot 3.5.x（Java 17+）、RESTful API、Clean Architecture

- 資料庫：支援 Oracle、DB2、SQL Server、PostgreSQL（可能需讀寫分離與分片設計）

整合：MQ、SFTP/FTPS、批次處理、Teams 通知、Swagger API 文件

- 安全性：OAuth2.1 / OpenID Connect、RBAC 權限管理、資料加密、防注入、防 XSS/CSRF

- 部署：容器化（Podman/Kubernetes）、CI/CD、自動化測試、監控與日誌

## 任務描述

請產生一份「後端開發指引」，內容需符合 SSDLC 要求，並包含以下章節：

1. 開發原則

   - 架構模式（如 Clean Architecture、分層設計）
   - 模組化與可維護性原則
   - 版本控制與分支策略（Git Flow / Trunk-based）

2. 專案結構與命名規範

   - Maven/Gradle 專案目錄結構
   - package 命名規則
   - 檔案與類別命名規範

3. API 設計規範

   - RESTful API 命名與版本化策略
   - 請求與回應格式（JSON Schema 範例）
   - 錯誤處理與錯誤碼設計

4. 資料庫存取與 ORM 規範

   - JPA/QueryDSL 使用規範
   - SQL 最佳化原則
   - 資料庫交易管理策略

5. 安全性規範（符合 SSDLC）

   - 身分驗證與授權
   - 輸入驗證與資料清理
   - 日誌與敏感資訊遮蔽

6. 效能與擴展性指引

   - Cache 機制（Redis）
   - 非同步與批次處理
   - 資源限制與連線池設定

7. 測試與品質保證

   - 單元測試（JUnit 5）與整合測試策略
   - 測試覆蓋率要求
   - SonarQube 規範

8. 部署與維運指引

   - CI/CD 流程
   - 容器化規範（Dockerfile / Podman）
   - 監控與警報設定（Prometheus / Grafana）

## 產出要求

- 以繁體中文撰寫
- 條列式清楚列出細節，必要時附範例程式碼或配置範例
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:後端開發指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------

# code review 指引

## 角色

你是一位資深前後端工程師，負責確保程式碼品質與可維護性，並協助團隊成員提升開發技能。

## 目的

確保所有程式碼在合併前都經過充分的檢查與評審，以降低潛在的錯誤與技術負債。

## 流程

1. 提交 PR（Pull Request）
2. 指定 reviewers
3. 進行程式碼檢查
4. 提供建議與意見
5. 確認修改後合併

## 檢查項目

- 程式碼風格（命名、排版）
- 邏輯正確性
- 測試覆蓋率
- 效能考量
- 安全性檢查

## 工具

- GitHub PR Review
- Gitlab Merge Request
- SonarQube
- ESLint / Prettier

## 產出要求

- 以繁體中文撰寫
- 條列式清楚列出細節，必要時附範例程式碼或配置範例
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:code review 指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------------------

# refactor 重構指引

## 角色

你是一位資深前後端工程師，負責確保程式碼品質與可維護性，並協助團隊成員提升開發技能。

## 目的

1. 提高可讀性
   - 讓程式碼更容易理解，降低未來維護的難度。
2. 改善結構與設計
   - 優化架構，使程式更具彈性、可擴充性。
3. 減少重複（DRY 原則）
   - 把重複的邏輯抽出來，讓程式碼更簡潔。
4. 提升可測試性
   - 更清晰的結構有助於單元測試與整合測試。
5. 降低技術債（Technical Debt）
   - 清理過時或混亂的程式碼，避免未來出現更多問題。
6. 促進團隊協作
   - 統一風格與結構，讓不同開發者更容易接手。

## 常見的重構手法

1. 提煉函數（Extract Function）
   - 將重複的程式碼片段提煉成獨立的函數，提高重用性。
2. 內聯函數（Inline Function）
   - 將簡單的函數內容直接放回呼叫處，減少不必要的函數呼叫。
3. 提煉類別（Extract Class）
   - 將大型類別拆分成多個小型類別，降低複雜度。
4. 合併類別（Merge Class）
   - 將功能相近的類別合併，簡化系統結構。
5. 變更函數簽名（Change Function Signature）
   - 調整函數的參數或返回值，以符合新的需求或設計。
6. 移除死程式碼（Remove Dead Code）
   - 刪除不再使用或冗餘的程式碼，減少維護負擔。
7. 簡化條件表達式（Simplify Conditional Expressions）
   - 將複雜的條件邏輯簡化，提升可讀性與可維護性。
8. 重命名變數與函數（Rename Variables and Functions）
   - 使用更具描述性的名稱，提升程式碼可讀性。
9. 提煉常數（Extract Constants）
   - 將魔法數字或字串提煉成具名常數，提高程式碼可讀性與可維護性。
10. 使用設計模式（Apply Design Patterns）
    - 根據需求選擇合適的設計模式，如單例模式、工廠模式、策略模式等，提升程式碼結構與可維護性。

## 產出要求

- 以繁體中文撰寫
- 條列式清楚列出細節，必要時附範例程式碼或配置範例
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:refactor 重構指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------------

# 程式寫作指引

## 角色設定

你是一位資深前後端工程師，負責撰寫高品質的程式碼，並協助團隊成員提升開發技能。

## 目的

- 提供一套程式寫作的最佳實踐與指引，幫助開發人員撰寫高品質、可維護的程式碼,包含安全性、效能與可維護性。
- 促進團隊內部的知識分享與技能提升。
- 建立一致的開發標準與流程，降低溝通成本。
- 提升程式碼的可讀性與可維護性。
- 降低潛在的錯誤與技術負債。
- 前端包含：Vue 3.x、Angular、Tailwind CSS、TypeScript
- 後端包含：Spring Boot 3.x、Java 17+

## 內容範圍

1. 程式碼風格與命名規範
2. 註解與文件撰寫
3. 錯誤處理與日誌紀錄
4. 單元測試與測試驅動開發（TDD）
5. 性能優化與資源管理
6. 安全性考量（如 OWASP Top 10）
7. 可測試性與測試覆蓋率
8. 版本控制與持續整合
9. 文件與註解
10. 其他最佳實踐
11. 持續學習與知識分享

## 格式與風格

- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:程式寫作指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------

# 安全程式碼指引

## 角色設定

- 你是一位資深的軟體安全架構師，熟悉 SSDLC（安全軟體開發生命週期）以及 OWASP Top 10，精通 Java、Spring Boot、Python、JavaScript 、vue3 等語言的安全開發。

## 對象

文件的讀者是新進的專案成員（軟體工程師與實習生），他們對安全開發概念不熟，需要一份淺顯易懂但實務導向的 安全程式碼指引。

## 任務說明

- 請產生一份完整的「安全程式碼指引」，內容需包含：

- 文件目的：為什麼要寫安全程式碼，與業務和合規的關聯。

- 通用安全開發原則（如最小權限、輸入驗證、錯誤處理、加密使用原則）。

- 程式語言安全指引：

  - Java/Spring Boot
  - Python
  - JavaScript/TypeScript/vue3
- 每種語言需列舉常見安全漏洞與安全寫法範例。
- OWASP Top 10 對應對策：逐項簡述常見風險（如 SQL Injection、XSS、敏感資料外洩），並提供程式碼範例。

- 日常開發檢查清單（Checklist）：開發者每天、每個 Pull Request 應檢查的安全要點。

- 常見錯誤與反例：用「錯誤範例 → 正確範例」方式讓新進成員快速理解。

- 延伸資源：建議參考的文件（OWASP、CWE、公司內規）。
-

## 產出要求

- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 條列式、分章節，避免過於學術，要以「實務開發」為導向。

- 每個安全原則盡可能附上簡單程式碼範例。
- 必須同時考慮安全性、效能與可維護性
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:安全程式碼指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------

# 測試與品質保證指引

## 角色設定

- 你是一位資深的 軟體測試經理與品質保證專家，熟悉敏捷開發、DevOps、銀行與金融業專案的測試規範與品質標準。

## 文件目的

- 這份文件是給 新進專案成員 用來快速理解專案的 測試流程與品質保證規範。

- 內容要 清楚、易懂、可操作，並可作為團隊的 標準作業指引（SOP）。

## 文件請包含以下章節

1. 測試與品質保證的角色與責任  
2. 測試流程與各階段（單元測試、整合測試、系統測試、UAT、壓力測試）  
3. 測試計畫與測試案例設計  
4. 測試自動化與工具建議  
5. 缺陷管理流程（Bug lifecycle）  
6. 測試品質指標與衡量方式  
7. 測試與 CI/CD、版本控管、DevOps 的關聯  
8. 常見錯誤與避免方式  
9. 新進成員的最佳實務與建議  
10. 測試與品質保證檢查清單（Checklist）

## 產出要求

- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\指引\設計開發\目錄下,檔名為:測試與品質保證指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------

# git使用教學

## 角色設定

-你是一位資深的軟體架構師與團隊技術主管，熟悉 Git 版本控制與團隊協作規範。

## 背景

- 這是一個大型專案，開發團隊有新進成員需要學習如何在專案中正確使用 Git，以避免衝突、版本錯誤與協作混亂。

## 任務說明

請撰寫一份「專案 Git 教學手冊」，作為新進開發同仁的學習指引。內容需包含以下部分：

1. Git 基本觀念：什麼是版本控制、為什麼使用 Git

2. 環境設定：Git 安裝、帳號設定（個人與公司帳號區隔）、SSH/HTTPS 設定

3. 專案流程：

   - 如何 clone 專案

   - 建立與切換 branch 的規範（例如：main/dev/feature/hotfix 分支策略）

   - commit message 規範（例如：feat, fix, docs, style, refactor）

   - pull / fetch / merge / rebase 的正確用法

   - push 前要注意的檢查事項

   - 如何處理 conflict

4. 團隊協作：Pull Request (PR) / Merge Request (MR) 流程、code review 規範

5. 常見錯誤排解：例如誤 push、commit 錯誤訊息、如何 reset/revert

6. 最佳實務：如何保持 commit 歷史乾淨、如何同步 main 分支、避免 force push 的時機

7. 專案專屬規範：若有公司或部門內特別的 Git 規範，也請加入

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:git使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------

# github使用教學

## 角色設定

- 你是一位資深的軟體架構師兼專案經理，熟悉 Git/GitHub 在團隊協作中的最佳實務。

## 任務說明

- 請幫我撰寫一份 「專案中 GitHub 教學手冊」，提供給新進開發同仁使用。手冊的目的是幫助同仁快速理解並遵循專案中的 GitHub 使用規範，避免版本混亂並提升團隊合作效率。

## 文件需求

手冊需包含以下內容：

1. Git/GitHub 基礎概念：什麼是 Git？什麼是 GitHub？為何要使用？
2. 環境設定：如何安裝 Git、設定帳號、SSH/Token 配置。
3. 基本操作流程（結合專案規範）：
   - clone 專案
   - 建立 feature branch 命名規範
   - commit message 撰寫規範
   - push 到 remote
   - 建立 Pull Request (PR)
   - code review 流程與 merge 規範

4. 日常工作流程建議：如何同步 main 分支、避免衝突。
5. 常見錯誤與解決方式（如 merge conflict、rebase、誤刪檔案）。
6. 專案專屬規範（例如：branch 命名規則、commit message 格式、PR review 流程）。
7. 附錄：常用 Git 指令清單、圖解流程。

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:github使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------

# GitLab 使用教學

## 角色設定

- 你是一位資深的軟體架構師兼專案經理，熟悉 Git 與 GitLab 的版本控管、分支策略、CI/CD，以及大型專案團隊的協作流程。

## 背景

本專案是一個大型平台開發，團隊包含新進與資深成員，使用 GitLab 作為版本控管與協作工具。需要建立一份 GitLab 教學手冊，讓新進同仁能快速上手，並遵循專案內的標準操作流程。

## 任務說明

請撰寫一份 GitLab 教學手冊，內容需包含：

1. GitLab 基本介紹（Git vs. GitLab，為什麼要用 GitLab）
2. 專案的 GitLab 工作流程說明（Clone、Pull、Commit、Push、Merge Request 等）
3. 專案規範（分支策略、Commit message 規範、Merge Request 流程、Code Review 要求）
4. GitLab CI/CD 的基本介紹與專案中的使用方式
5. 常見問題與解決方式（例如：Merge 衝突處理、錯誤回復方式）
6. 開發同仁需要遵循的最佳實務建議

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:GitLab使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------

# Maven使用教學

## 角色設定

-你是一位 資深的系統架構師與前後端開發主管，熟悉 Maven 與大型專案的管理方式。

## 任務說明

-請幫我撰寫一份 專案中 Maven 教學手冊，主要目的是給新進開發同仁使用，協助他們快速熟悉並在專案中正確使用 Maven。

## 文件需求

內容需要包含：

1. Maven 基本介紹
   - Maven 的用途與優勢
   - 在專案中的角色
2. 環境建置
   - 如何安裝 Maven
   - 與 JDK、IDE（例如 IntelliJ、VS Code、Eclipse）的整合
   - 驗證安裝成功的方法
3. Maven 專案結構
   - 標準目錄結構說明（src/main/java、src/test/java、pom.xml 等）
   - 在專案中的實際應用
4. pom.xml 說明
   - 常用標籤與設定（groupId、artifactId、version、dependencies、plugins）
   - 如何新增與管理依賴
5. 常用指令
   - mvn clean install、mvn package、mvn test、mvn dependency:tree 等
6. 專案最佳實務
   - 依賴管理建議
   - 避免版本衝突的方法
   - 使用公司內部 Nexus/Artifactory（如果有的話）
7. 常見問題排解 (FAQ)
   - 常見錯誤訊息與解決方式
   - 專案中注意事項
8. 附錄
   - 官方文件與教學資源連結

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Maven使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------

# Visual Studio Code使用教學

## 角色設定

- 你是一位資深的軟體架構師與專案經理，熟悉大型專案的開發環境與工具配置。

## 專案背景

1. 本專案採用 前後端分離架構
   - 前端：Vue 3 + TypeScript + Tailwind CSS
   - 後端：Spring Boot (Java)
2. IDE/編輯器統一使用 Visual Studio Code
   - 新進開發同仁需要快速熟悉 VS Code 在專案中的使用方式

## 任務說明

請幫我撰寫一份 專案中 Visual Studio Code 教學手冊，內容需包含：

1. VS Code 安裝與環境設定
   - 安裝步驟
   - 推薦字型與主題
   - 專案必要的 Extensions 清單（例如 Prettier、ESLint、Java Extension Pack 等）

2. 專案開發環境配置
   - 如何開啟專案
   - 前端、後端工作區設定（Workspace Settings）
   - 編碼規範設定（ESLint、Prettier、Checkstyle 等）
3. 日常開發操作
   - Git 與 GitHub/GitLab 整合
   - 常用快捷鍵
   - 偵錯（Debugging）與斷點設定
   - 終端機與多工作區使用
4. 專案特定開發流程指引

- 如何執行/偵錯前端 (npm/yarn scripts)
- 如何執行/偵錯後端 (Spring Boot 啟動)
- 如何進行測試與查看測試報告

5. 最佳實務
   - 常見問題 (FAQ) 與解決方式
   - 建議的工作習慣（如自動存檔、自動格式化）

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Visual Studio Code使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------

# IntelliJ IDEA Community Edition使用教學

## 角色設定

- 你是一位資深的 Java 後端開發架構師，熟悉使用 IntelliJ IDEA Community Edition 進行專案開發。

## 任務說明

- 請幫我撰寫一份「IntelliJ IDEA Community Edition 教學手冊」，用於專案內部培訓，協助新進開發同仁快速熟悉並正確使用 IDE。

## 文件內容範圍

請包含以下章節：

1. IntelliJ IDEA CE 下載與安裝
2. 開發環境基本設定（JDK、Maven、Encoding、Code Style）
3. 匯入專案與建立新專案
4. 與 Git/GitHub/GitLab 的整合
5. 專案編譯與執行（含 Maven、Spring Boot）
6. Debug 與單元測試
7. 常用快捷鍵與開發小技巧
8. 專案最佳實務（例如：Code Formatting、註解、套件管理）

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:IntelliJ IDEA Community Edition使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------

# Podman使用教學

## 角色設定

- 你是一位專案的資深架構師與講師，請幫我撰寫一份 Podman 教學手冊，對象是「新進開發同仁」，他們 完全沒有 Podman 經驗驗。

## 背景

- 專案導向：讓新進同仁了解如何在你們專案環境中使用 Podman。
- 基礎學習：因為同仁沒學過 Podman，要有入門到進階的學習脈絡。
- 認證導向：內容也要涵蓋足夠的知識，幫助通過 Podman 認證考試

## 任務說明

1. 基礎入門

- 什麼是 Podman，與 Docker 的差異
- Podman 的安裝、環境設定與基本指令
- 容器、映像檔、Pod 的基本概念

2. 專案實務應用

- 在我們專案中如何使用 Podman（請提供一般企業常見的專案範例）
- 建立、管理、除錯開發環境容器的方法
- Podman 與 CI/CD、微服務架構、Spring Boot/前端服務等的整合方式

3. 進階操作

- Podman Compose 使用
- 映像檔最佳化與安全性
- Volume、Network、Registry 的應用

4. 考照準備

- Podman 認證相關知識範圍整理
- 常見考題練習與解說

5. 附錄

- 常見錯誤排查
- 最佳實務建議

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Podman使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------

# Podman Desktop使用教學

## 角色設定

- 你是一位熟悉容器技術與教學設計的資深架構師與講師，請幫我撰寫一份 Podman Desktop 教學手冊

## 背景

- 對象是新進開發同仁，這些同仁 沒有學過 Podman Desktop。

## 任務說明

手冊需要具備以下要求：

1. 基礎入門：
   - 介紹 Podman 與 Podman Desktop 的背景、核心概念、與 Docker 的比較。
   - 安裝 Podman Desktop（Windows 10/11 為主），基本操作介面導覽。

2. 專案實務應用：
   - 如何在專案中使用 Podman Desktop 進行程式開發與容器管理。
   - 建立容器、管理映像檔、Volume、Network 的範例操作。
   - 如何在專案環境中模擬、測試與部署應用程式。
   - 與 VS Code / IntelliJ 等 IDE 的整合方式。
3. 進階操作與最佳實務：
   - Podman CLI 與 Desktop 的搭配使用。
   - Compose 支援與多容器應用管理。
   - 安全性與資源管理最佳實踐。
   - 與 Kubernetes/OpenShift 的對接基礎。
4. 認證考試準備：
   - Podman 認證需要的知識範圍與重點整理。
   - 常見考題型態與解題練習。
   - 提供學習地圖與練習資源連結。
5. 學習結構：
   - 章節設計：從入門 → 實務 → 進階 → 認證準備。
   - 每章提供：目標、步驟教學（附指令與截圖）、常見錯誤與排解、練習題。

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Podman Desktop使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------

# Jenkins + CI/CD 教學手冊

## 角色設定

- 你是 Jenkins 與 CI/CD 專家兼技術講師
- 新進 Java 開發者，未接觸過 Jenkins

## 背景

- 技術棧：Java 17、Maven、JUnit、Log4j2、Git、GitLab
- 目標：建立從程式提交到自動建置、測試、程式碼品質檢查、打包與(可選)部署的 Pipeline
- 環境：Windows 開發端 + Jenkins Server (可為本機或遠端)

## 學習與認證目標

- Jenkins 核心概念：Master/Agent、節點、Executor、Queue
- 安裝與基本設定
- Jenkins Plugin 基礎 (Git, Pipeline, Maven, JUnit, Credentials Binding)
- 憑證與密碼管理 (Credentials)
- Freestyle vs Pipeline vs Multibranch
- Jenkinsfile 結構：pipeline, agent, stages, steps, post
- Declarative vs Scripted Pipeline
- 與 GitHub Webhook 整合
- Maven 建置/測試/報表 (Surefire, Jacoco)
- 測試報告與程式碼覆蓋率發布
- 靜態程式碼品質 (可建議使用 SpotBugs / Checkstyle)
- 參數化建置、條件執行 (when)
- 並行 (parallel) 與 matrix
- Artifact 保存與部署 (例如打包 JAR)
- 常見錯誤排查
- 最佳實務 (可維護性、安全性、重用 Shared Library)
- 與 Jenkins & CI/CD 認證考試主題對應表
-

## 產出要求

1. 目錄 (TOC)
2. 逐章內容 (由淺入深)
3. 每章含：學習目標、核心概念、步驟、範例、常見錯誤、延伸閱讀
4. 附 Jenkinsfile 範例：
   - 最簡版本
   - 含 Maven 測試 + JUnit 報告發布
   - 含 Jacoco 覆蓋率
   - 含參數化與條件
   - 含平行測試
5. 每個 Jenkinsfile 附註解
6. 提供在 Windows 本機快速測試 Jenkins 的方式 (Docker 或 War)
7. 提供將該教學加入現有專案 README / Wiki 的建議摘要
8. 認證對應表：每節對應認證知識點
9. 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
10. 使用 Markdown 格式，含標題、編號與條列
11. 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
12. 每節結尾提供實務案例或注意事項
13. 最後附上「檢查清單（Checklist）」方便新進成員快速使用
14. 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Jenkins CI/CD 教學手冊.md，並使用 Markdown 格式撰寫。
15. 請分段回覆

--------------------------------------------------------

# Hexagonal Architecture設計教學

## 角色設定

- 你是一位資深的軟體架構師，也是教學設計專家

## 背景

- 本專案採用 Hexagonal Architecture（六邊形架構），新進同仁大多沒有相關經驗

## 任務說明

Hexagonal Architecture 教學手冊 — 目錄
Part 1. 基礎概念

1. 認識 Hexagonal Architecture（六邊形架構）
   - Hexagonal 的由來與核心理念
   - 與傳統分層架構（Layered Architecture）的比較
   - Ports & Adapters 模式的核心概念
2. Hexagonal Architecture 的設計目標
   - 解耦業務邏輯與基礎設施
   - 減少技術債務與提升可測試性
   - 支援 Domain-Driven Design（DDD）的角色
3. Hexagonal 與其他架構模式的關係
   - 與 Clean Architecture 的異同
   - 與 Onion Architecture 的異同
   - 適用場景與限制

Part 2. 核心組件與實作模式
4. Ports & Adapters 詳解

- 定義與職責
- 輸入 Port / 輸出 Port
- 主動 Adapter / 被動 Adapter

5. Domain 層的角色
   - Entity / Value Object
   - Use Case / Application Service
   - Domain Service
6. Infrastructure 層的角色
   - Repository 與持久化策略
   - API / UI / CLI 作為 Adapter
   - 外部系統整合（MQ、FTP、第三方 API）

Part 3. 專案實務應用
7. 專案中導入 Hexagonal Architecture 的步驟

- 現有系統重構的策略
- 新專案的建置範本
- 與 Spring Boot / FastAPI 等框架結合

8. 範例專案（逐步拆解）
   - 業務需求說明
   - 架構圖與 Ports/Adapters 定義
   - 程式碼示例（Java + Spring Boot）
   - 單元測試與整合測試
9. 常見錯誤與反模式
   - Port 與 Adapter 混淆
   - Domain 層洩漏基礎設施細節
   - 過度工程化導致維護成本上升

Part 4. 進階應用與最佳實務
10. 與 DDD 結合

- Bounded Context 與 Hexagonal 邊界
- 聚合（Aggregate）與 Ports 的對應

11. 與微服務結合

- 單體轉微服務的分割策略
- Hexagonal 在微服務 API 設計的角色

12. 測試策略

- 使用 Mock / Stub 取代基礎設施
- 測試 Use Case 而非 Adapter
- 測試金字塔與 Hexagonal

Part 5. 認證與職涯應用
13. Hexagonal Architecture 認證考試重點

- 核心知識點整理
- 常見考題類型
- 官方教材與參考資源

14. 模擬考題與解析

- 單選題
- 多選題
- 情境題（案例分析）

15. 職場應用與最佳實務

- 在大型專案中的價值
- 與團隊協作的溝通方式
- 架構文件與設計決策記錄（ADR）

16. 附錄

- 常見名詞對照表（Ports, Adapters, Domain, Infrastructure 等）
- 推薦書籍與線上資源
- 範例專案 GitHub 連結（可加）

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Hexagonal Architecture設計教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------

# Onion Architecture 設計教學

## 角色設定

- 你是一位資深的軟體架構師與專案導師。

## 背景

- 我正在進行一個專案，開發團隊成員中有一些新進同仁，完全沒學過 Onion Architecture。我希望他們能透過一份完整的 Onion Architecture 教學手冊 學會在專案中使用 Onion Architecture 進行開發，並且這份手冊的內容能幫助同仁將來去考取 Onion Architecture 認證。

## 任務說明

Onion Architecture 教學手冊目錄
第 1 章：緒論

1.1 教學手冊的目的與對象
1.2 為什麼需要 Onion Architecture
1.3 與傳統分層架構、Hexagonal Architecture、Clean Architecture 的比較
1.4 如何透過本手冊準備 Onion Architecture 認證

第 2 章：Onion Architecture 基礎概念

2.1 Onion Architecture 的核心理念
2.2 各層級設計原則（Domain、Application、Infrastructure、Presentation）
2.3 依賴反轉原則 (Dependency Inversion Principle)
2.4 Onion Architecture 的優點與限制

第 3 章：分層解析

3.1 Domain Layer - 實體與商業規則
3.2 Application Layer - 用例與服務
3.3 Infrastructure Layer - 技術支援與外部資源
3.4 Presentation Layer - 使用者介面與 API
3.5 層與層之間的互動與依賴管理

第 4 章：實作指南

4.1 在專案中導入 Onion Architecture 的步驟
4.2 專案目錄與模組結構設計
4.3 使用 Spring Boot 建立 Onion 架構範例
4.4 Repository 與 Service 的設計實例
4.5 測試策略：單元測試、整合測試、端到端測試

第 5 章：最佳實務

5.1 常見錯誤與如何避免
5.2 如何重構現有系統到 Onion Architecture
5.3 在大型專案中的應用經驗分享
5.4 與團隊協作的開發規範

第 6 章：進階議題

6.1 Onion Architecture 與 DDD (Domain-Driven Design) 的整合
6.2 與 CQRS (Command Query Responsibility Segregation) 的結合
6.3 在微服務 (Microservices) 架構中的應用
6.4 與事件驅動架構 (Event-Driven Architecture) 的關聯

第 7 章：認證指南

7.1 Onion Architecture 認證考試介紹
7.2 常見考點與知識重點整理
7.3 模擬題與解析
7.4 推薦學習資源與延伸閱讀

第 8 章：附錄

8.1 範例專案程式碼 (Java + Spring Boot)
8.2 常見 FAQ
8.3 設計圖示範例 (UML、分層圖)
8.4 術語表 (Glossary)

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Onion Architecture 設計教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------

# Microservices Architecture 設計教學

## 角色設定

- 你是一位資深的系統架構師與專案導師。
- 請幫我撰寫一份專案教學手冊，主題是 Microservices Architecture 設計。

## 背景

- 這份手冊是寫給新進開發同仁，他們 沒有學過 Microservices Architecture，需要在專案中依循手冊學會使用 Microservices Architecture 設計進行開發。

## 任務說明

Microservices Architecture 教學手冊目錄（含常用設計模式，完整版）

Part I. 基礎認識

1. 微服務架構簡介
1.1 為什麼需要微服務
1.2 單體架構 vs. 微服務架構
1.3 微服務的核心特徵
1.4 適用與不適用場景
2. 微服務與業界標準
2.1 SOA 與微服務的差異
2.2 Cloud Native 與微服務
3.3 與 Microservices Architecture 認證的關聯

Part II. 微服務設計原則
3. 微服務設計的基本原則
3.1 單一職責原則 (SRP)
3.2 鬆耦合與高內聚
3.3 可獨立部署與演進
3.4 API First 思維
4. 微服務邊界劃分
4.1 Domain-Driven Design (DDD) 與微服務
4.2 Bounded Context
4.3 業務能力導向的拆分
4.4 避免過度切分的陷阱

Part III. 技術架構
5. 微服務通訊模式
5.1 同步通訊 (REST, gRPC)
5.2 非同步通訊 (Message Queue, Event Streaming)
5.3 API Gateway 與 Service Mesh
6. 資料管理策略
6.1 每個服務獨立資料庫
6.2 分散式交易與 Saga Pattern
6.3 CQRS 與 Event Sourcing
6.4 Outbox Pattern 與資料一致性保證
7. 配置與服務發現
7.1 Service Registry
7.2 Configuration Management
7.3 負載平衡與流量導向

Part IV. 微服務設計模式 (Design Patterns)
8. 分解模式 (Decomposition Patterns)
8.1 Database per Service
8.2 Strangler Fig Pattern
8.3 Self-Contained Service Pattern
8.4 DDD 與 Bounded Context 拆分
9. 通訊模式 (Communication Patterns)
9.1 API Gateway Pattern
9.2 Backend for Frontend (BFF)
9.3 Service Mesh Pattern
9.4 Aggregator Pattern
9.5 Event-Driven Messaging Pattern
10. 資料管理模式 (Data Management Patterns)
10.1 Saga Pattern
10.2 CQRS Pattern
10.3 Event Sourcing Pattern
10.4 Outbox Pattern
10.5Event Streaming
11. 可靠性模式 (Reliability Patterns)
11.1 Circuit Breaker Pattern
11.2 Retry Pattern（含指數退避）
11.3 Timeout Pattern
11.4 Bulkhead Pattern
11.5 Fail Fast Pattern
11.6 Fallback Pattern
12. 監控與觀測模式 (Observability Patterns)
12.1 Health Check API
12.2 Log Aggregation
12.3 Distributed Tracing
12.4 Metrics Collection
12.5 Correlation ID Pattern
13. 部署模式 (Deployment Patterns)
13.1 Blue-Green Deployment
13.2 Canary Deployment
13.3 Service Discovery
13.4 Sidecar Pattern
13.5 Ambassador Pattern
13.6 Adapter Pattern

Part V. 跨領域議題
14. 微服務的安全性設計
14.1 API 安全 (OAuth2, JWT)
14.2 Zero Trust 架構
14.3 身份與存取管理 (IAM)
15. 微服務的可靠性
15.1 Resilience Patterns 與實作
15.2 Observability 工具鏈整合
15.3 分散式追蹤實作 (OpenTelemetry, Jaeger, Zipkin)
16. DevOps 與 CI/CD
16.1 容器化 (Docker, Podman)
16.2 Kubernetes 與微服務部署
16.3 自動化測試、滾動更新與回滾

Part VI. 微服務在專案中的實踐
17. 微服務專案導入流程
17.1 單體轉型微服務策略
17.2 團隊協作與組織模式 (Conway’s Law)
17.3 版本管理與 API 演進
18. 微服務專案範例
18.1 架構設計圖示
18.2 服務拆分案例
18.3 實作範例 (Spring Boot, FastAPI, NestJS 等)

Part VII. 認證與進階學習
19. Microservices Architecture 認證指南
19.1 認證考試範疇與重點
19.2 常見考題類型與解題技巧
19.3 推薦學習資源與模擬測驗
20. 深入學習與最佳實踐
20.1 微服務反模式 (Anti-patterns)
20.2 微服務與 Serverless 的比較
20.3 未來趨勢：AI 驅動的微服務

Part VIII. 附錄
21. 工具與資源清單
21.1 微服務開發框架比較
21.2 測試與監控工具
21.3 推薦書籍與線上課程

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Microservices Architecture 設計教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------

# 「微服務安全性設計指南」

# 「微服務監控與運維手冊」

# 「微服務實戰案例集」

---------------------------------------------------------

# GitHub使用hugo建立個人網頁教學

## 角色設定

- 你是一位熟悉 GitHub Pages 與 Hugo 靜態網站架設的資深專案經理與技術顧問。

## 背景

-請你撰寫一份「使用 Hugo 在 GitHub 上建立個人網頁」的完整教學文件。

## 任務說明

1. 教學步驟要完整、清楚、可直接操作。

2. 使用 Windows 10 作業系統環境。

3. 教學應包含以下章節：

   - 前置條件與工具安裝（Git、Hugo、VS Code、GitHub 帳號）
   - 建立 Hugo 專案
   - 本機預覽網站
   - 選擇與設定 Hugo Theme
   - 部署到 GitHub Pages（含建立 Repository 與 GitHub Actions 自動部署設定）
   - 維護與更新內容的流程
   - （可選）設定自訂網域（Custom Domain）

4. 每個步驟請附上範例指令與說明。

5. 最後請幫我生成一份「教學大綱」與「完整操作教學文件」。

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:GitHub使用hugo建立個人網頁教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------

# XXXXXXX使用教學

## 角色設定

## 背景

## 任務說明

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Podman使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------------------

# Jmeter使用教學

## 角色設定

- 你是一位資深的 JMeter 測試工程師與專業講師。

## 背景

- 我要在專案中引導新進開發同仁學習使用 JMeter 進行壓力測試。這些同仁完全沒學過 JMeter。

## 需求

請幫我撰寫一份完整的「JMeter 教學手冊」，內容需要：  

1. 從零開始，涵蓋 JMeter 的基礎概念、安裝與環境設定。  
2. 說明如何建立與執行壓力測試腳本，並分析測試結果。  
3. 包含專案中常見的應用情境（例如 API 測試、資料庫壓測、Web 應用壓測）。  
4. 加入最佳實務與效能測試的注意事項。  
5. 對應 JMeter 認證考試需要的知識點。  
6. 請先生成一份「教學手冊目錄」，再逐章展開詳細內容。  
請用清楚、循序漸進、容易理解的方式撰寫，適合完全沒學過 JMeter 的新進人員使用。

## 任務說明

JMeter 教學手冊目錄
Part 1. 基礎入門

1. JMeter 簡介
   - JMeter 的定位與用途
   - 常見測試類型 (壓力測試、負載測試、功能測試)
   - JMeter 與其他效能測試工具比較

2. 安裝與環境設定
   - 系統需求與下載方式
   - Windows / Linux / Mac 安裝流程
   - JMeter 目錄結構說明
   - 常見安裝問題與解決方式
3. JMeter 使用者介面 (GUI)
   - JMeter 元件總覽 (Test Plan, Thread Group, Sampler, Listener, Config 等)
   - 建立第一個測試計畫 (Hello World 測試)

Part 2. 測試計畫設計
4. 測試計畫基礎

- Test Plan 與 Thread Group 設定
- 使用 Sampler 進行請求 (HTTP, JDBC, FTP, JMS 等)
- 使用 Listener 收集與查看結果

5. 參數化與資料驅動測試
   - CSV Data Set Config
   - User Defined Variables
   - Properties 與環境變數

6. 控制元件與邏輯控制器
   - Loop Controller, If Controller, Transaction Controller
   - 調整測試流程的技巧

7. Assertion 與驗證
   - Response Assertion
   - Duration Assertion
   - Size Assertion

Part 3. 進階應用
8. 報表與結果分析

- Summary Report, Aggregate Report
- Graph Results, Response Time Graph
- HTML Dashboard Report 生成
- 效能瓶頸診斷方法

9. 測試最佳實務
   - 模擬真實使用者行為
   - Thread 數與 Ramp-up 設定策略
   - 分散式測試 (Remote / Distributed Testing)

10. 整合與自動化

- 與 CI/CD 工具整合 (Jenkins, GitLab CI)
- 非 GUI 模式測試
- 指令列執行與參數傳遞

Part 4. 專案實戰
11. API 測試實戰

- REST API 壓測
- SOAP 測試範例

12. Web 應用效能測試

- 網頁載入與多資源請求模擬
- 登入與 Session 管理

13. 資料庫效能測試

- JDBC Sampler 測試
- SQL 壓測案例

14. 企業專案案例

- 金融系統批次交易測試
- 雲端服務平台壓測
- 高併發應用效能測試

Part 5. JMeter 認證與進階知識
15. 認證考試重點整理

- 測試理論與 JMeter 架構
- JMeter 常見組件與用途
- 壓測設計與結果分析題型

16. 考試模擬題與解析

- 單選題 / 多選題
- 實作題

17. 進階學習方向

- JMeter 插件 (JMeter Plugins)
- 與 Gatling、Locust 的比較
- 測試效能調校技巧

Part 6. 附錄
18. 常見錯誤與排除方法
19. 測試報告範本
20. 學習資源與參考書目

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Jmeter使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------------------

# Linux使用教學

## 角色設定

- 你是一位資深的 Linux 系統工程師兼軟體架構師。

## 背景

- 專案開發環境使用 Linux（請指明版本，例如 Ubuntu 20.04 / CentOS 8 / Rocky Linux 9）。
- 開發語言：Java / Python / Node.js（可依專案實際情況替換）。
- 工具鏈：Git / Maven / Podman / Jenkins / VS Code Remote SSH。
- 團隊成員有許多新進同仁，完全沒有使用過 Linux。

## 任務說明

Linux 教學手冊目錄（專案 + 認證導向）

1. 前言
1.1 本手冊目的
1.2 適用對象
1.3 專案環境說明（Ubuntu / CentOS / Rocky Linux）
1.4 學習方法與建議
2. Linux 基礎概念
2.1 Linux 與開源精神簡介
2.2 Linux 系統架構（Kernel、Shell、應用程式）
2.3 檔案系統階層結構（/bin, /etc, /home, /var …）
2.4 使用者與群組管理
2.5 檔案與目錄權限（rwx, chmod, chown）
[認證對應：LFCS Domain 1, RHCSA Chapter 1]
3. Linux 常用指令
3.1 檔案與目錄操作（ls, cd, cp, mv, rm, mkdir, rmdir）
3.2 檔案檢視與搜尋（cat, less, head, tail, grep, find）
3.3 檔案壓縮與解壓縮（tar, gzip, bzip2, zip, unzip）
3.4 權限管理（chmod, chown, umask）
3.5 程序管理（ps, top, kill, jobs, systemctl）
3.6 網路工具（ping, curl, wget, netstat, ss）
3.7 軟體件管理（apt / yum / dnf）
[認證對應：LPI Essential, RHCSA 基礎操作]

4. 開發環境操作
4.1 安裝與設定 JDK
4.2 安裝與設定 Python
4.3 安裝與設定 Node.js
4.4 資料庫客戶端（psql, sqlplus, mysql）
4.5 使用 Git 與 GitLab/GitHub
4.6 容器化開發工具（Podman / Docker 基礎）
4.7 Maven/Gradle 編譯與部署
[專案應用：開發環境搭建流程]

5. 專案日常任務
5.1 SSH 遠端登入（ssh, ssh-keygen, config）
5.2 檔案傳輸（scp, sftp, rsync）
5.3 Log 查詢與分析（tail -f, journalctl, grep）
5.4 錯誤排查技巧（dmesg, systemctl, top, df, free）
5.5 排程任務（cron, at, systemd timer）
[認證對應：LFCS Domain 2, RHCSA 排程管理]

6. Linux 系統安全與最佳實務
6.1 sudo 與使用者權限控管
6.2 SSH 安全性（禁止 root 登入、金鑰登入）
6.3 防火牆設定（firewalld, ufw）
6.4 SELinux / AppArmor 基本操作
[認證對應：RHCSA 安全管理章節]

7. CI/CD 與 Linux 整合
7.1 Jenkins 於 Linux 的安裝與設定
7.2 Jenkins Pipeline 與 Shell Script
7.3 Linux 與容器整合（Podman / Docker + Jenkins）
7.4 自動化部署流程範例（build → test → deploy）
[專案應用案例：實際 CI/CD pipeline 設定]

8. Linux 認證導向補充
8.1 LFCS 認證重點整理
8.2 RHCSA 認證重點整理
8.3 LPI Linux Essentials 認證重點整理
8.4 練習題與模擬試題
[專案應用：考照導向學習地圖]

9. 附錄
9.1 常見錯誤與解決方法
9.2 Linux 學習資源推薦（網站、書籍、影片）
9.3 常用指令速查表（Cheat Sheet）
9.4 專案內部 FAQ

## 產出要求

- 提供一份 完整的教學手冊目錄（樹狀結構）。
- 每章節需有 簡介、學習目標、內容教學、實務練習、專案應用案例。
- 同時標註對應 Linux 認證考試重點，方便同仁學習時兼顧考照。。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Linux使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------------------------------------

# Vim使用教學

## 角色設定

- 你是一位資深的軟體架構師兼 Vim 專家。

## 背景

- 我們的專案需要開發同仁熟悉 Vim，在 Linux 環境中進行程式開發與日常操作。新進同仁多數沒有使用過 Vim。

## 任務說明

Vim 教學手冊》目錄
前言

- Vim 在專案中的角色
- 為什麼要學習 Vim
- 本手冊的學習方式與使用建議
第一篇：Vim 基礎入門

1. Vim 簡介
   - Vim 與 Vi 的關係
   - Vim 的特色與優勢
   - Vim 與 IDE 的比較
2. 安裝與環境設定
   - 在 Linux、macOS、Windows 安裝 Vim
   - 基本設定檔 .vimrc 建立
   - 字體、編碼與顯示調整
3. Vim 的操作模式
   - 一般模式 (Normal Mode)
   - 插入模式 (Insert Mode)
   - 視覺模式 (Visual Mode)
   - 命令列模式 (Command-Line Mode)
   - 模式切換練習
4. 文字編輯基礎
   - 游標移動
   - 插入與刪除文字
   - 複製、貼上、刪除、取代
   - Undo / Redo
5. 檔案操作
   - 開啟、儲存、關閉檔案
   - 多檔案切換
   - 分割視窗 (Split) 與分頁 (Tab)
第二篇：進階編輯技巧
6. 搜尋與取代
   - 基本文字搜尋
   - 正規表示式搜尋
   - 全檔取代與範圍取代
7. 巨集與自動化
   - 錄製巨集
   - 執行與重複巨集
   - 自動化編輯案例
8. 多檔案編輯與快速導覽
   - 標記 (Mark)
   - 快速跳轉 (Jump List, Tag Jump)
   - 編輯多個檔案的技巧
9. 文本處理進階
   - 對齊與縮排
   - 區塊選取與編輯
   - 自動補全
第三篇：專案開發實務
10. Vim 與程式開發

- 語法高亮 (Syntax Highlight)
- 自動縮排與程式碼格式化
- 編譯與除錯整合

11. 插件管理

- 常見插件管理工具 (vim-plug, Vundle)
- 常用開發插件介紹
- LSP 與自動補全 (coc.nvim, nvim-lspconfig)

12. Git 與版本控制整合

- Vim 與 Git 基本操作
- Fugitive.vim 插件使用
- 比對檔案與版本差異

13. 日常開發案例

- 快速尋找函數定義
- 多檔案同時修改
- 專案目錄快速導覽 (NERDTree, Telescope)
- 第四篇：考試與認證準備

14. Vim 認證簡介

- 常見 Vim 認證種類
- 認證考試範圍

15. 模擬練習題

- 基礎操作練習
- 進階編輯技巧題目
- 專案實務題目

16. 學習路線圖

- 從初學者到進階使用者
- 推薦學習資源
- 考試準備建議
附錄
- Vim 常用快捷鍵速查表
- 常見錯誤排解
- 推薦書籍與網站
- 練習建議

## 產出要求

- 提供一份 完整的教學手冊目錄（樹狀結構）。
- 每章節需有 簡介、學習目標、內容教學、實務練習、專案應用案例。
- 同時標註對應 Linux 認證考試重點，方便同仁學習時兼顧考照。。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為:Vim使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------------------------------------

# Bash使用教學

## 角色設定

- 你是一位資深的 Linux / Shell Script 專家與軟體培訓講師。

## 背景

- 目前公司專案開發環境會使用 Bash 來撰寫與執行腳本。團隊有新進開發同仁，他們大多沒有學過 Bash。希望能提供一份完整的 Bash 教學手冊，指引同仁能在專案中正確使用 Bash 進行程式開發，並能具備考取 Bash 認證（如 Linux Foundation 或 LPI 相關認證）的能力。

## 任務說明

Bash 教學手冊 目錄

第 1 部分：基礎入門
1.1 認識 Bash 與 Shell
1.2 Bash 與 Linux/Unix 的關係
1.3 Bash 環境與版本檢查
1.4 常見開發環境介紹（WSL、Linux、macOS、容器環境）
1.5 基本命令列操作（ls、cd、pwd、man、help）
1.6 編輯器使用：vim / nano / VS Code 結合 Bash

第 2 部分：Bash 核心語法
2.1 變數與資料型態（字串、數字、環境變數）
2.2 參數與引數（$0、$#、$@、$*）
2.3 運算子與算術計算（expr、let、$(( ))、bc）
2.4 條件判斷（if、test、[ ]、[[ ]]）
2.5 迴圈結構（for、while、until、select）
2.6 函式（定義、呼叫、參數傳遞、回傳值）
2.7 輸入與輸出（read、echo、printf）
2.8 管線與重新導向（|、>、>>、2>、&>）

第 3 部分：進階主題
3.1 陣列與字串處理
3.2 正則表達式與 grep/sed/awk
3.3 檔案與目錄操作自動化
3.4 使用 cron 與排程任務
3.5 Bash 腳本除錯（set -x, trap）
3.6 錯誤處理與退出狀態碼（$?, exit）
3.7 Bash 腳本最佳實務（可讀性、模組化、安全性）

第 4 部分：專案應用實戰
4.1 自動化專案建置腳本
4.2 系統環境初始化與設定檔管理
4.3 日誌分析與檔案過濾（grep、awk、sed 實戰）
4.4 批次檔案處理（壓縮、搬移、清理）
4.5 FTP / SFTP / SCP 自動化檔案傳輸
4.6 專案 CI/CD 腳本案例（搭配 GitLab CI、Jenkins）

第 5 部分：考試準備
5.1 Bash 認證考試介紹（LPI, Linux Foundation 等）
5.2 常見考試範疇與題型解析
5.3 範例考題與練習題
5.4 模擬測驗與解答解析
5.5 考試技巧與時間管理

第 6 部分：附錄
6.1 常用 Bash 指令速查表
6.2 Shell 腳本錯誤排查清單
6.3 Bash 相關學習資源（書籍、網站、課程）
6.4 專案內部 Bash 腳本規範

## 產出要求

- 提供一份 完整的教學手冊目錄（樹狀結構）。
- 每章節需有 簡介、學習目標、內容教學、實務練習、專案應用案例。
- 同時標註對應 Linux 認證考試重點，方便同仁學習時兼顧考照。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為:Bash使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------------------------------------

# PowerShell使用教學

## 角色設定

- 你是一位資深的軟體架構師兼講師

## 背景

- 我們的專案會用到 PowerShell，需要讓新進同仁（沒有 PowerShell 經驗）能快速上手，並且能透過學習此手冊通過 PowerShell 認證考試

## 任務說明

PowerShell 教學手冊目錄
第 1 部分：基礎入門

1. 認識 PowerShell
   - PowerShell 的歷史與用途
   - 與 CMD、Bash 的差異
   - PowerShell Core vs Windows PowerShell
2. 安裝與環境設定
   - 在 Windows 與跨平台安裝 PowerShell
   - PowerShell ISE 與 VS Code 整合
   - 基本環境變數設定
3. 基本操作
   - 常用指令（Get-Help、Get-Command、Get-Member）
   - 管道 (Pipeline) 與物件導向特性
   - 輸出與重新導向
第 2 部分：核心語法
4. 變數與資料型態
   - 宣告與使用變數
   - 常見資料型別（字串、數字、陣列、雜湊表）
   - 型態轉換與檢查
5. 運算子與流程控制
   - 比較運算子與邏輯運算子
   - 條件判斷（if, switch）
   - 迴圈語法（for, foreach, while, do-while）
6. 函數與模組
   - 定義與呼叫函數
   - 參數與回傳值
   - 匯入與建立模組
第 3 部分：進階技巧
7. 物件與管道操作
   - Select-Object、Where-Object、Sort-Object
   - Format-Table、Format-List
   - 對象操作與屬性方法存取
8. 錯誤處理與除錯
   - Try/Catch/Finally
   - 錯誤物件 $Error
   - 除錯工具與斷點
9. 檔案與系統管理
   - 檔案與目錄操作
   - 註冊表操作
   - 系統服務與程序管理
第 4 部分：專案實務應用
10. 自動化腳本撰寫

- 常見自動化範例（批次檔轉換、日誌管理）
- 系統排程整合

11. 開發環境整合

- 與 Git/GitHub/GitLab 的整合
- 與 CI/CD（Jenkins, Azure DevOps, GitLab CI）的應用

12. 系統與網路操作

- WMI 與 CIM 指令
- 遠端管理 (PowerShell Remoting)
- 網路測試與自動化
第 5 部分：認證考試重點

13. PowerShell 認證簡介

- 認證種類與考試結構
- 常見考試主題整理

14. 認證題型解析與模擬題

- 單選/多選題範例
- 情境題練習
- 解題技巧與常見陷阱
第 6 部分：附錄

15. 常用指令速查表
16. 實用範例腳本
17. 章末練習題與參考答案

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為:PowerShell使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# Clean Code教學

## 角色設定

- 你是一位資深軟體架構師與教學設計專家，請幫我撰寫一份「專案中用到 Clean Code 的教學手冊」，對象是新進開發同仁，他們之前沒有學過 Clean Code。

## 背景

- 幫助新進開發同仁理解 Clean Code 的核心概念與最佳實踐。  
- 指引他們在專案中如何應用 Clean Code 原則進行程式開發。  
- 協助同仁具備通過 Clean Code 認證的知識基礎。  

## 任務說明

- Clean Code 簡介（什麼是乾淨程式碼、為什麼重要、與專案品質的關係）  
- Clean Code 原則（命名、函式、類別、物件、註解、格式、錯誤處理、測試等）  
- 實務範例（Java 或專案中主要語言的範例，展示「不良程式碼」與「改善後程式碼」對照）  
- 在專案中的實際應用指引（專案規範、程式碼審查流程、常見反模式與改善方法）  
- 與認證考試相關的重點整理（考試常見題型、必讀觀念、練習題）

## 產出要求

- 用淺顯易懂的語言解釋，適合初學者。  
- 每個章節附帶程式碼範例與最佳實踐指引。  
- 提供章節小結與練習題，方便自我檢測學習效果。
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Clean Code教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# Clean Architecture教學

## 角色設定

- 你是一位資深軟體架構師與教學設計專家，請幫我撰寫一份「專案中用到 Clean Architecture 的教學手冊」，對象是新進開發同仁，他們之前沒有學過 Clean Architecture。

## 背景

1. 幫助新進同仁理解 Clean Architecture 的基本概念與設計哲學。
2. 能在專案中依照 Clean Architecture 進行程式開發（以 Java/Spring Boot 為例，或給出通用程式語言範例）。
3. 最後具備考取 Clean Architecture 認證 的能力。

## 任務說明

1. 基礎篇：Clean Architecture 的核心概念、原則、常見誤解。
   - Clean Architecture 的背景、目的與優勢
   - 核心原則（獨立性、可測試性、可維護性、依賴反轉）
   - Clean Architecture 與傳統三層架構、MVC 的比較
   - 常見誤解與迷思
2. 架構篇：解釋 Entities、Use Cases、Interface Adapters、Frameworks & Drivers 各層責任，並配合圖解。
   - Entities 層：企業核心業務規則
   - Use Cases 層：應用業務規則
   - Interface Adapters 層：轉換器（Controllers、Presenters、Gateways）
   - Frameworks & Drivers 層：外部工具與框架（DB、Web、UI）
   - 以圖解方式呈現依賴方向與分層關係
3. 實作篇：以專案範例（如會員管理系統）示範如何按照 Clean Architecture 撰寫程式碼。
   - 專案案例：會員管理系統 (註冊、登入、查詢會員資料)
   - 對照傳統 MVC 與 Clean Architecture 的程式碼差異
   - 程式碼目錄結構範例（以 Spring Boot 為例）
   - 具體程式碼範例（含 Entities、Use Cases、Adapters、Frameworks 層實作）
   - 單元測試與整合測試策略
4. 專案應用篇：我們專案中具體的規範、程式碼目錄結構、開發規則。
   - 我們專案內 Clean Architecture 的落地規則
   - 專案目錄結構標準
   - 開發規範（命名、依賴注入、封裝原則）
   - 新功能開發流程（從 Use Case 設計到交付）
   - 常見錯誤範例與修正建議
5. 認證輔導篇：整理 Clean Architecture 認證考試的範圍、推薦書單、重點摘要與模擬題。
   - Clean Architecture 認證考試介紹與報名資訊
   - 考試範圍與題型分析
   - 推薦書單（如《Clean Architecture: A Craftsman's Guide to Software Structure and Design》）
   - 重點摘要與學習路線圖
   - 模擬題與解答

## 產出要求

- 使用淺顯易懂的說明，避免艱澀專有名詞。
- 內容要有圖例/程式碼範例/最佳實務/常見錯誤對比。
- 請用教科書式的條列方式編排，讓新同仁可以循序漸進學習。
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Clean Architecture教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# Refactoring重構教學

## 角色設定

- 你是一位資深軟體架構師與教學設計專家，請幫我撰寫一份「Refactoring（重構）教學手冊」，對象是新進開發同仁，他們之前沒有學過 Refactoring。

## 背景

- 新進同仁，沒有學過 Refactoring。
- 能在專案中實際運用 Refactoring，並有能力通過相關認證考試。

## 任務說明

- Refactoring 的基本概念與原則
- 常見的壞味道（Code Smells）與判斷方式
- 重構方法（例如 Extract Method, Rename Variable, Introduce Parameter Object…）
- 專案中應如何選擇與實踐
- 實務範例（Java 或你們專案使用的語言）
- 與測試（TDD/單元測試）的關聯
- 考試重點、練習題與模擬題
- 最佳實務與團隊規範

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為: Refactoring重構教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------------

# Design Pattern教學

## 角色設定

- 你是一位資深軟體架構師兼講師，熟悉 Design Pattern（設計模式）並且了解業界專案開發實務與認證考試內容。

## 背景

1. 請你幫我撰寫一份 Design Pattern 教學手冊，使用對象是 專案中新進開發同仁，他們 沒有學過 Design Pattern。
2. 請根據以上結構，幫我生成一份 完整且條理清晰的 Design Pattern 教學手冊，讓新進同仁可以：
   - 由淺入深快速掌握設計模式。
   - 能夠應用到專案實務開發。
   - 具備通過 Design Pattern 認證考試的能力。

## 任務說明

手冊需求如下：

1. 基礎入門
   - 說明什麼是 Design Pattern、為什麼要用、它在軟體工程中的角色。
   - 與專案開發相關的實際價值（如：可維護性、重複使用性、團隊協作）。
2. 核心內容
   - 依照三大分類（創建型、結構型、行為型）逐一介紹常見設計模式（如 Singleton, Factory, Observer, Strategy, Decorator 等）。
   - 每個模式需包含：定義、適用場景、UML 圖、Java範例程式碼、專案實務案例。
3. 專案應用指南
   - 如何在我們的專案中導入設計模式。
   - 範例：在 [專案背景，例如 Spring Boot/微服務/銀行系統] 中，哪些地方適合用哪種 Design Pattern。
   - 新進同仁該如何在日常開發中練習應用。
4. 學習與練習
   - 提供練習題與小型實作任務。
   - 舉例：請用 Strategy Pattern 改寫一段 if-else 過多的程式。
5. 認證考試準備
   - 介紹常見的 Design Pattern 認證（如 OCP Design Patterns 或相關考試）。
   - 提供考點重點、模擬試題與解答。
7. 附錄
   - 推薦書籍、學習資源、線上課程連結。
   - UML 圖繪製工具與程式碼產生工具建議

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:
Design Pattern教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------------------------------

# Design Pattern教學2

## 角色設定

- 你是一位資深軟體架構師兼講師，熟悉 Design Pattern（設計模式）並且了解業界專案開發實務與認證考試內容。
- 請你幫我撰寫一份 Design Pattern 教學手冊，使用對象是 專案中新進開發同仁，他們 沒有學過 Design Pattern。

## 背景

## 任務說明

第 1 章：設計模式概論

- 設計模式的定義與歷史背景（Gang of Four, GoF）
- 為什麼需要設計模式（解決重複問題、提升維護性、降低耦合度）
- 設計模式與軟體工程、架構設計的關聯
- 在專案開發（例如 Spring Boot / 微服務 / 銀行系統）中的價值與應用場景
- 簡單案例（例如 Singleton）作為導入

第 2 章：設計模式分類與全貌

- 三大類別：創建型、結構型、行為型
- 每一類別的主要設計模式清單與簡介
- UML 與程式碼示例（只需簡單範例，詳細會在後續章節展開）
- 一張表格：整理模式 → 定義 → 適用場景

第 3 章：創建型模式

- 簡介（解決物件建立問題，避免硬編碼與耦合）
- Singleton、Factory Method、Abstract Factory、Builder、Prototype
    每個模式需有：定義、適用場景、UML 圖、範例程式碼、專案應用案例

第 4 章：結構型模式

- 簡介（解決類別/物件結構關係，提升可重用性）
- Adapter、Bridge、Composite、Decorator、Facade、Flyweight、Proxy
- 每個模式需有：定義、適用場景、UML 圖、範例程式碼、專案應用案例

第 5 章：行為型模式

- 簡介（解決物件之間的互動與責任分配問題）
- Chain of Responsibility、Command、Interpreter、Iterator、Mediator、Memento、Observer、State、Strategy、Template Method、Visitor
- 每個模式需有：定義、適用場景、UML 圖、範例程式碼、專案應用案例

第 6 章：專案應用指南

- 如何在我們的專案（例如 Spring Boot、微服務架構、銀行系統）導入設計模式
- 常見錯誤做法與改進範例（例如 if-else 過多 → 使用 Strategy Pattern）
- 不同設計模式在專案中的最佳實踐案例

第 7 章：學習與練習

- 小型練習題（如：請用 Factory Pattern 改寫物件建立程式碼）
- 中型專案實作（如：用 Observer + Strategy 模式完成訂單通知系統）
- 思考題與解答

第 8 章：認證考試準備

- 常見 Design Pattern 認證簡介（如 OCP Java 認證的設計模式部分）
- 考試重點整理（每個模式的用途、優缺點、應用場景）
- 模擬試題與解答

第 9 章：附錄與資源

- 推薦書籍（GoF《設計模式》、Head First Design Patterns 等）
- 線上學習資源（Udemy、Coursera、YouTube 教學頻道）
- UML 繪圖工具、程式碼產生工具建議

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:
Design Pattern教學(二).md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------------

# 統一建模語言(UML)教學

## 角色設定

- 你是一位資深的系統架構師與軟體設計講師，熟悉 UML（統一建模語言）的各種圖表與應用。

## 背景

- 請幫我撰寫一份 UML 教學手冊，對象是「新進開發同仁」，這些同仁 完全沒有 UML 經驗。

## 任務說明

1. 基礎概念：UML 的起源、用途、在軟體開發專案中的角色與價值。
2. 常用圖表教學：逐一說明 UML 的常用圖表（用例圖、類別圖、序列圖、活動圖、狀態圖、元件圖、部署圖等），包含：
3. 定義與用途
   - 符號與元素說明
   - 範例圖（可用文字或mermaid畫出圖來示範）
3. 實務應用情境（專案中什麼時候該用哪種圖表）
   - 專案實作指引：如何在我們的專案中使用 UML 來進行程式開發（例如：需求分析 → 用例圖，系統設計 → 類別圖、序列圖）。
4. 工具介紹：常用 UML 繪圖工具（如 Visual Paradigm、StarUML、PlantUML），並簡單示範如何上手。
5. 實務範例：以一個小型專案案例，完整展示從需求到設計的 UML 建模流程。
6. 認證考試準備：整理 UML 認證（如 OMG UML Certification）的重點知識、題型範例與學習路線圖。
7. 附錄：推薦的書籍、線上資源、練習題。

## 產出要求

- 條列式 + 圖例解說
- 用淺顯易懂的語言，循序漸進
- 強調「實務應用」而不是單純理論
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:統一建模語言(UML)教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------------

# 物件導向分析與設計 (OOAD) 教學

## 角色設定

- 你是一位資深的系統架構師與教育訓練講師，請幫我撰寫一份「物件導向分析與設計 (OOAD) 教學手冊」，使用對象是新進開發同仁，他們沒有學過 OOAD。

## 背景

1. 指引同仁如何在專案中應用 OOAD 進行程式開發。
2. 教導如何使用統一建模語言 (UML) 來支援 OOAD。
3. 幫助同仁具備考取 UML 認證的能力。

## 任務說明

請依以下架構撰寫：

- 前言與學習目標
- OOAD 基礎概念（物件、類別、封裝、繼承、多型、抽象）
- OOAD 流程（需求分析 → 分析模型 → 設計模型 → 實作）
- UML 與 OOAD 的關係（各種 UML 圖：Use Case、Class、Sequence、Activity、State、Component、Deployment）
- 專案實務應用範例（以一個簡單系統做 end-to-end 的分析與設計）
- 常見錯誤與最佳實務
- UML 認證考試重點與學習資源
- 結語與延伸閱讀

## 產出要求

- 請用清楚的章節標題、圖示說明、程式碼範例與練習題，讓新進同仁能夠逐步學習並實際應用。
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:物件導向分析與設計 (OOAD) 教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# 資料流程圖(DFD)教學

## 角色設定

- 你是一位資深系統分析師與專案講師，請你幫我撰寫一份 資料流程圖 (DFD) 教學手冊，提供給專案中新進的開發同仁使用。

## 背景

- 這些同仁從未學過資料流程圖 (DFD)，因此手冊需要由淺入深，兼顧理論與實務。

## 任務說明

1. 基礎概念
   - 什麼是資料流程圖 (DFD)
   - DFD 的用途與價值
   - 在系統分析與程式開發中的角色
2. DFD 元素與符號
   - 外部實體 (External Entity)
   - 處理程序 (Process)
   - 資料流 (Data Flow)
   - 資料儲存 (Data Store)
   - 符號標準與繪製規範
3. DFD 層次
   - Level 0 (Context Diagram)
   - Level 1 與更細分的層次
   - 如何由高層分解到細節
4. 繪製步驟與方法
   - 蒐集需求與識別資料流
   - 步驟化的繪製流程
   - 常見錯誤與避免方式
5. 專案實務應用
   - 如何在專案需求分析文件中使用 DFD
   - 如何讓程式開發與 DFD 對應
   - 與 ER Model、UML 的關聯
6. 練習與案例
   - 提供簡單案例 (例如 ATM 提款系統、訂單管理系統)
   - 從 Context Diagram 到 Level 1 的完整範例
   - 練習題目與參考解答
7. 認證準備
   - 國際/業界常見 DFD 認證或相關考試介紹
   - 必考知識點整理
   - 模擬試題
8. 附錄
   - 常用繪圖工具介紹 (如 Visio、Draw.io、Lucidchart)
   - 進一步學習資源 (書籍、網站、課程)

## 產出要求

- 請用 教學手冊格式 撰寫，語氣清楚、循序漸進，適合完全初學者閱讀。
- 手冊內容要能幫助同仁 在專案中使用 DFD 進行程式開發，同時也能夠應付 DFD 認證考試。
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:資料流程圖(DFD)教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# Entity-Relationship Model (ER Model，實體關係模型)教學

## 角色設定

- 你是一位資深的系統架構師與資料建模專家，請幫我撰寫一份 Entity-Relationship Model (ER Model, 實體關係模型) 教學手冊，目標讀者是 新進開發同仁，他們 完全沒有學過 ER Model。

## 背景

讓 AI 幫你生成一份完整的「Entity-Relationship Model (ER Model) 教學手冊」，而且要符合三個目標：

- 對象是新進同仁，沒有學過 ER Model → 內容要淺顯易懂。
- 專案中實際會用到 → 要有專案應用情境與實作範例。
- 能幫助考過 ER Model 認證 → 需要包含考試重點、題型模擬。

## 任務說明

這份手冊需要符合以下需求：
1.基礎知識

- 解釋 ER Model 的基本概念（實體、屬性、關係、鍵值）。
- 使用清楚的圖解與範例。
- 說明 ERD (Entity-Relationship Diagram) 的符號與規則。
2.專案應用
- 說明如何在專案中設計 ER Model。
- 提供案例（例如銀行系統、電商平台）來展示如何從需求轉換成 ERD。
- 介紹如何將 ER Model 轉換為資料庫 schema（如 DB2、PostgreSQL、Oracle）。
3.進階主題
- 強實體、弱實體、關聯度 (cardinality)、正規化。
- 常見設計錯誤與最佳實務。
4.認證準備
- 說明 ER Model 相關認證的內容與考試範圍。
- 提供練習題與模擬考題（選擇題、實作題）。
- 列出重點知識摘要（cheat sheet）。

5.學習路徑

- 建議的學習步驟（從基礎到進階）。
- 推薦工具（如 mermaid、draw.io、Lucidchart、ERwin、DBeaver）。
- 進一步學習資源（書籍、網站、線上課程）。

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為: Entity-Relationship Model (ER Model，實體關係模型)教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------

# Object-Relational Mapping (ORM) 物件關聯對映教學

## 角色設定

- 你是一位資深的系統架構師與專案導師，請幫我撰寫一份
「Object-Relational Mapping (ORM) 物件關聯對映教學手冊」。

## 背景

- 對象是新進開發同仁，完全沒有學過 ORM。
- 目標是讓同仁能在專案中正確使用 ORM 進行程式開發。
- 手冊也需要包含足夠的知識與範例，幫助同仁準備 ORM 相關認證考試。

## 任務說明

1. ORM 簡介（為什麼需要 ORM、解決了什麼問題、與 SQL/資料庫互動的關係）
2. ORM 的基本概念（實體、對應、Session、Transaction、Lazy/Eager Loading 等）
3. ORM 工具與框架簡介（例如 Hibernate、JPA、Spring Data JPA、SQLAlchemy 等）
4. 安裝與設定（以主流語言 Java 和 Python 為例）
5. 基本 CRUD 範例（建立、查詢、更新、刪除）
6. 關聯對映（One-to-One、One-to-Many、Many-to-Many）
7. 進階主題（快取、批次處理、效能最佳化、N+1 問題）
8. 在專案中的最佳實務（命名規則、錯誤處理、測試方法）
9. 常見錯誤與排錯技巧
10. 認證考試重點與練習題
11. 結論與學習資源（推薦書籍、官方文件、線上課程）

## 產出要求

- 請用淺顯易懂的語言，並搭配圖解與程式碼範例。
- 範例要同時提供 Java（Hibernate/JPA）與 Python（SQLAlchemy）的寫法，方便同仁比較。
- 每個章節要有「小結」幫助複習。
- 請以正式文件的口吻，編排清晰，方便直接當成公司內部教材使用。
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為: Object-Relational Mapping (ORM) 物件關聯對映教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# Domain-Driven Design教學

## 角色設定

- 你是一位資深軟體架構師兼講師，請你幫我撰寫一份 Domain-Driven Design (DDD) 教學手冊，內容給專案中新進的開發同仁使用。這些同仁 從未學過 DDD，需要能夠循序漸進地學會並應用在專案中。

## 背景

- 用淺顯易懂的語言，逐步引導初學者。
- 加入圖示/表格/範例程式碼，讓讀者容易理解。
- 文件結構完整，能直接作為新進同仁的學習教材。
- 能幫助同仁未來參加並通過 Domain-Driven Design 認證。
- 前端使用vue 3.x, 後端使用sprint boot,使用前後分離的作法。

## 任務說明

1. 基礎概念介紹：Domain、Subdomain、Bounded Context、Ubiquitous Language、Entity、Value Object、Aggregate、Repository、Service、Factory 等。
2. DDD 在專案中的實際應用方式：如何從需求分析到建立模型，如何劃分 Bounded Context，如何定義 Aggregates，如何設計 Repository 與 Service。
3. 程式範例：使用 Java/Spring Boot（或我們專案中常用的技術）展示 DDD 的設計與實作方式。
4. 專案實務指引：如何在團隊中推行 DDD、與架構設計結合、與測試 (TDD/Unit Test) 結合。
5. 常見錯誤與避免方式。
6. 學習與認證路徑：推薦的書籍、線上課程、DDD 認證資訊，以及考取認證需要的知識重點。
7. 附錄：常見 UML 圖 (Class Diagram、Context Map) 的使用，對應到 DDD 的最佳實踐。

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Domain-Driven Design教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------------

# Domain-Driven Design 教學(一)

## 角色設定

- 你是一位資深軟體架構師與DDD專家，熟悉 Eric Evans 的 Domain-Driven Design 與戰術/戰略設計。

## 背景

- 本專案需要新進開發同仁學習並應用 Domain-Driven Design (DDD)，但他們之前沒有接觸過 DDD。
我們需要一份完整的 DDD 教學手冊，同仁可以依此手冊學習，在專案中正確應用 DDD，並最終能通過 DDD 認證考試。

## 任務說明

Domain-Driven Design 教學手冊目錄
第一篇：基礎入門
1.什麼是 Domain-Driven Design (DDD)

- 背景與歷史
- 為什麼需要 DDD
- 與傳統開發方式的差異

2. DDD 的核心理念
   - Domain（領域）的重要性
   - Ubiquitous Language（通用語言）
   - Model-Driven Design（模型驅動設計）
3. DDD 的兩大面向
   - 戰略設計 (Strategic Design)
   - 戰術設計 (Tactical Design)

第二篇：DDD 戰略設計 (Strategic Design)
4. 子域 (Subdomain) 的分類

- 核心領域 (Core Domain)
- 支援子域 (Supporting Subdomain)
- 通用子域 (Generic Subdomain)

5. 限界上下文 (Bounded Context)
   - 定義與識別方法
   - 界定上下文的準則
   - 限界上下文的邊界劃分範例
6. 上下文映射 (Context Mapping)
   - Context Map 基本圖示
   - 上下文之間的關係模式（Partnership、Shared Kernel、Customer-Supplier、Conformist 等）
7. 案例分析
   - 如何將真實專案切分為子域與限界上下文
   - 分析銀行/金融系統案例

第三篇：DDD 戰術設計 (Tactical Design)
8. 核心構件介紹

- Entity（實體）
- Value Object（值物件）
- Aggregate（聚合）與 Aggregate Root
- Repository（倉儲）
- Service（領域服務 / 應用服務）
- Factory（工廠）

9. 戰術設計實作
   - Java / Spring Boot 範例
   - Repository 與資料庫整合（JPA / Spring Data）
   - Aggregate 設計原則與範例
   - Value Object 與不可變性
10. 領域事件 (Domain Events)

- Event Sourcing
- CQRS 與 DDD 的結合

11. 模組化與分層架構

- Domain Layer、Application Layer、Infrastructure Layer、Interface Layer
- 在專案中實作 Onion / Hexagonal / Clean Architecture

第四篇：DDD 與實務應用
12. 在微服務架構中的 DDD

- Bounded Context 與微服務的對應
- 微服務邊界設計

13. 與敏捷、Scrum 的整合

- Event Storming
- Domain Storytelling

14. 專案最佳實踐

- 常見錯誤與反模式
- 成功案例分享

第五篇：學習檢測與認證準備
15. 章節小測驗

- 每章提供練習題

16. DDD 認證考試重點整理

- 必考核心概念
- 常見題型與解題思路

17. 模擬測驗題庫

- 單選題 / 多選題 / 案例題

附錄

- A. 常用圖示與設計範例
- B. 推薦書籍與學習資源
- C. DDD 在企業應用的成功案例

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:Domain-Driven Design教學(一).md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# SQL使用教學

## 角色設定

- 你是一位資深的資料庫工程師與專案培訓講師，請幫我撰寫一份完整的 SQL 教學手冊，對象是新進開發同仁，他們從未學過 SQL。

## 背景

- 教學手冊（基礎 → 進階 → 專案實務）
- 結合專案實際 SQL 使用情境（查詢、更新、交易、效能優化）
- 幫助同仁未來能考取 SQL 認證（如 IBM DB2,Oracle SQL, Microsoft SQL, PostgreSQL 認證）
- 包含範例、練習題、最佳實務

## 任務說明

1. 從基礎開始（SQL 基本語法、資料表、查詢、條件、排序、聚合函數、子查詢）。
2. 漸進到進階主題（JOIN、索引、交易處理、儲存程序、效能優化）。
3. 結合我們專案常用的 SQL 實務範例，幫助同仁能在專案中正確撰寫與維護 SQL。
4. 包含練習題與答案，讓同仁能自我檢測學習成果。
5. 特別設計章節幫助同仁準備 SQL 認證（例如 IBM DB2, Oracle SQL, Microsoft SQL Server, PostgreSQL 的 SQL 認證），整理常考題型與解題技巧。
6. 提供最佳實務（安全性、防止 SQL Injection、效能調校）。

## 產出要求

- 請用條理分明的章節方式撰寫，語言清楚簡單，適合完全沒學過 SQL 的新手閱讀。
請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為:SQL使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# html5 與CSS3 程式語言教學

## 角色設定

- 你是一位資深的前端架構師，熟悉 HTML5 與 CSS3 的程式設計，以及在大型專案中的最佳實務。

## 任務說明

- 請幫我撰寫一份「專案中 HTML5 與 CSS3 教學手冊」，給新進開發同仁閱讀，內容需指引他們在專案中如何使用 HTML5 與 CSS3 進行程式開發。

## 文件內容範圍

文件需包含以下章節：

- 前言（說明 HTML5 與 CSS3 在專案中的角色與重要性）
- 開發環境設定（專案中使用的工具、編輯器、套件建議）
- HTML5 開發規範（語意化標籤、表單、媒體、結構最佳實務）
- CSS3 開發規範（選擇器、Flexbox、Grid、動畫、RWD 規範）
- 專案中的命名規則與檔案結構（CSS/HTML 組織方式）
- 常見錯誤與解決方法
- 開發最佳實務（效能優化、可維護性、跨瀏覽器相容性）
- 範例程式碼
- 結語（提醒遵循專案標準的重要性）

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: html5 與CSS3 程式語言教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------

# Javascript程式語言教學

## 角色設定

- 你是一位資深前端架構師，負責撰寫一份 JavaScript 教學手冊，提供給新進開發同仁使用。

## 專案背景

- 本專案採用前後端分離架構，前端使用 Vue 3.x / React/Angular 。
- 使用 JavaScript（含 ES6+）作為主要開發語言。
搭配 Tailwind CSS 與 RESTful API 進行前端開發。

## 任務說明

- 請撰寫一份 「JavaScript 教學手冊」，內容需清楚、完整，適合新進同仁閱讀，並能指引他們在專案中正確使用 JavaScript。

## 文件內容範圍

1. JavaScript 基本概念

   - 語言特性（動態型別、事件驅動、非同步處理）
   - ES6+ 常用語法 (let/const, arrow function, template literals, 解構賦值, modules)

2. 程式開發規範
   - 程式碼風格 (命名規則、縮排、註解)
   - 使用 ESLint / Prettier（若有）
   - 專案中常用的 Utility Functions 與撰寫方式

3. 專案中常見應用範例
   - DOM 操作與事件處理
   - 非同步處理 (Promise, async/await, fetch API)
   - 與後端 API 溝通 (RESTful API 呼叫範例)
   - 錯誤處理與例外狀況處理

4. 專案最佳實務
   - 模組化程式設計
   - 重複程式碼抽取共用方法
   - 安全性注意事項（避免 XSS、輸入驗證）
   - 效能優化建議（Debounce/Throttle、Lazy Loading）

5. 測試與除錯
   - 使用瀏覽器 DevTools 進行除錯
   - 基本單元測試 (若專案採用 Jest / Vitest)

6. 學習資源與進階閱讀
   - 官方文件連結
   - 推薦教學資源（MDN, JavaScript.info）

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: html5 與CSS3 程式語言教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------

# TypeScript程式語言教學

## 角色設定

- 你是一位資深的前端架構師與技術導師，熟悉 TypeScript 與大型專案開發規範。

## 任務說明

- 請幫我撰寫一份 專案中 TypeScript 教學手冊，目標讀者是新進開發同仁，內容需指引他們如何在專案中正確使用 TypeScript 進行程式開發。

## 文件內容範圍

1. TypeScript 基礎
   - 介紹 TypeScript 與 JavaScript 的差異
   - 型別系統（基本型別、物件、陣列、泛型）
   - 介面 (Interface)、型別別名 (Type Alias)
   - Enum、Union / Intersection types
2. 專案規範
   - 專案中 TypeScript 的版本與設定（tsconfig.json）
   - 檔案命名規則與專案目錄結構
   - 型別宣告的最佳實踐
   - 使用 any 的限制與替代方法
3. 程式開發指引
   - 如何撰寫可讀性與可維護性的 TypeScript 程式碼
   - 常見錯誤與最佳解法
   - 與第三方套件整合（例如：React、Vue、Angular、Node.js 的寫法差異）
4. 範例程式碼
   - 提供清楚的程式碼範例（Class、Interface、泛型、模組化）
   - 範例需符合專案風格
5. 實務建議
   - 如何在開發過程中善用 TypeScript 的型別檢查
   - 如何進行除錯與測試
   - 在團隊協作中如何統一程式風格（搭配 ESLint/Prettier）

## 產出要求

- 請產生一份完整、條理清楚的文件，並以 章節方式編排，可直接提供給新進人員使用。
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: TypeScript程式語言教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------------------------

# Java程式語言教學

## 角色設定

- 你是一位資深 Java 系統架構師與 OCP 認證講師，熟悉大型系統開發與 Java 國際認證考試範圍。你的任務是幫助新進開發同仁快速學會 Java，並具備考取 Java 認證的能力。

## 任務說明

- 請撰寫一份完整的 Java 教學手冊，適合 完全沒學過 Java 的新進同仁，內容需兼顧 專案實務開發 與 Java 認證考試。

## 文件內容範圍

1. Java 語言簡介
   - Java 的歷史、特性與應用
   - 為什麼專案使用 Java
   - Java 認證路線（OCA → OCP）簡介
2. 開發環境與工具
   - JDK 安裝（版本：Java 21）
   - IDE 設定（IntelliJ IDEA / VS Code）
   - Build 工具（Maven/Gradle）
3. Java 基礎語法（認證必考 + 專案實務）
   - Hello World 程式
   - 基本資料型別、變數、常數
   - 運算子與型別轉換
   - 流程控制（if, switch, for, while, do-while）
   - 認證陷阱題（例如：switch 搭配字串、型別提升 rules）
4. 物件導向程式設計 (OOP)
   - 類別與物件
   - 建構子與初始化順序
   - 方法（overloading vs overriding）
   - 封裝、繼承、多型
   - 介面與抽象類別
   - 存取修飾詞 (public, private, protected, default)
   - 認證考點：方法解析順序、物件存活範圍、final/abstract 差異
5. 核心 API 與工具
   - 字串與 StringBuilder
   - 陣列與集合框架（List, Set, Map）
   - java.time API（LocalDate, LocalDateTime）
   - 包裝類別 (Wrapper Classes) 與自動裝箱 (Autoboxing)
   - 認證陷阱題：equals vs ==, hashCode 規則
6. 例外處理與錯誤管理
   - try, catch, finally
   - throws 與 throw
   - Checked vs Unchecked Exception
   - 認證考點：例外捕捉順序、try-with-resources
7. 進階語法與認證內容
   - 泛型 (Generics)
   - Lambda 與 Functional Interface
   - Stream API
   - 模組化 (Java Modules)
   - 認證考點：泛型型別推斷、stream 終端操作 vs 中間操作

8. 多執行緒與並行處理（認證 + 專案）
   - Thread 與 Runnable
   - Executor Service
   - synchronized 與 Concurrent API
   - 認證陷阱題：死鎖、競爭條件
9. 專案實務應用
   - 建立 RESTful API (Spring Boot 範例)
   - 資料庫存取（JDBC, JPA）
   - 日誌（SLF4J/Logback）
   - 單元測試（JUnit 5）
10. 認證模擬練習

- 每章附帶 5~10 題練習題（單選/多選）
- 解析常見考點陷阱
- 提供模擬小測驗

11. 最佳實務與專案規範

- 命名規則、程式碼風格
- 常見錯誤排查
- 安全性考量（SQL Injection, XSS）

12. 附錄

- 認證官方考綱（Oracle OCP Java SE 17 Programmer）
- 推薦學習資源（Oracle Docs、Java SE Tutorial、Mock Exam）
- 專案內部工具與 Library

## 產出要求

-請以正式文件格式撰寫，章節分明，包含：

- 語法解說
- 範例程式碼
- 認證考點提醒
- 小練習題與解析
- 請產生一份完整、條理清楚的文件，並以 章節方式編排，可直接提供給新進人員使用。
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: Java程式語言教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------

# Python程式語言教學

## 角色設定

- 你是一位資深軟體架構師與專業講師，熟悉 Python 語言、企業級專案開發以及 Python 國際認證（例如 PCEP、PCAP）。

## 任務說明

- 請你幫我撰寫一份完整的 Python 教學手冊，用於公司專案中新進開發同仁的培訓。這份手冊必須讓沒有 Python 基礎的同仁能夠快速上手，並在日後能夠參加並通過 Python 認證考試。

## 文件內容範圍

1. Python 基礎入門
   - Python 安裝與環境設置（Windows/Linux）
   -語法基礎（變數、資料型態、運算子）
   - 流程控制（if、for、while、例外處理）
   - 函式、模組與套件管理（pip、venv）
2. 進階應用
   - 面向物件程式設計（class、繼承、封裝）
   - 檔案處理與例外處理
   - 常用標準函式庫（datetime、os、sys、json、logging 等）
   - 測試與除錯（unittest、pytest）
3. 專案實務應用
   - 如何在專案中撰寫乾淨且可維護的程式碼
   - PEP 8 程式碼風格規範
   - 與專案相關的 Python 技術（例如 RESTful API、批次處理、資料處理等）
   - 與團隊協作工具的整合（Git、CI/CD 測試流程）
4. Python 認證考試指引
   - 針對 PCEP 與 PCAP 認證的考試範圍
   - 常見考題類型與練習題
   - 應考技巧與學習路線規劃

## 教學目標

- 幫助新進同仁從零基礎快速學會 Python。
- 他們能夠在專案中正確使用 Python 開發。
- 協助他們具備考取 Python 認證（PCEP/PCAP）的能力。

## 產出要求

- 條列式章節（由淺入深，循序漸進）
- 需包含程式碼範例與實作練習
- 每章後面附上小測驗題目
- 提供認證考試對應章節標註
- 請產生一份完整、條理清楚的文件，並以 章節方式編排，可直接提供給新進人員使用。
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: Python程式語言教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------

# C# 程式語言教學

## 角色設定

- 你是一位資深 C# 系統架構師與技術講師，熟悉大型專案的程式設計與 C# 認證考試內容。
請你幫我撰寫一份 C# 教學手冊，對象是「從未學過 C# 的新進開發同仁」。

## 任務說明

- 請你幫我撰寫一份完整的 C# 教學手冊，用於公司專案中新進開發同仁的培訓。這份手冊必須讓沒有 C# 基礎的同仁能夠快速上手，並在日後能夠參加並通過 C# 認證考試。

## 文件內容範圍

教學手冊需求：

1. 基礎入門
   - 介紹 C# 與 .NET 基本概念
   - 開發環境設定（Visual Studio / VS Code）
   - 基本語法（變數、型別、流程控制、函式、例外處理）
2. 物件導向程式設計 (OOP)
   - 類別、物件、建構子
   - 繼承、多型、介面、抽象類別
   - 封裝與存取修飾詞
3. 進階語法與實務
   - 泛型 (Generics)
   - 委派與事件 (Delegates & Events)
   - LINQ 語法與集合操作
   - 非同步程式設計 (async/await)
4. 專案實務應用
   - 專案中如何使用 C#（依照公司專案場景說明，例如 Web API、桌面應用或微服務）
   - 與資料庫存取（Entity Framework / ADO.NET）
   - 單元測試 (xUnit / NUnit)
   - 錯誤處理與日誌紀錄
5. 認證考試對應
   - 列出 C# 認證考試（如 Microsoft C# certification）的主要範圍
   - 在每章節結尾加入「認證考點提示」
   - 附上範例考題與練習題
6. 附錄
   - 常見問題 FAQ
   - 學習資源（官方文件、練習網站、書籍）
   - 建議學習路徑（讓同仁能循序漸進到達考照水準）

## 產出要求

- 章節清楚，採用 教科書風格
- 每個主題包含 解說 + 範例程式碼 + 小練習題
- 用淺顯易懂的文字，適合沒程式基礎的人
- 保持專業與完整性
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: C#程式語言教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------

# Thymeleaf使用教學

## 角色設定

- 你是一位資深的系統架構師與講師，請幫我撰寫一份 Thymeleaf 教學手冊，使用對象是 新進開發同仁。

## 背景

- 假設他們 完全沒有學過 Thymeleaf。

## 任務說明

手冊要包含以下重點：

1. 基礎概念：Thymeleaf 是什麼、特色、與 JSP/其他模板引擎比較。
2. 環境建置：在 Spring Boot 專案中如何整合 Thymeleaf（含 Maven/Gradle 設定）。
3. 語法教學：
   - 基本標籤語法（th:text, th:if, th:each 等）
   - 屬性處理（th:attr, th:classappend）
   - 模板繼承與片段 (Layout, th:fragment, th:replace)
   - 表單處理（th:form, th:field, 與後端 model 綁定）
   - 國際化 (i18n) 支援
4. 實務應用範例：
   - 頁面渲染流程（Controller → Model → View）
   - 建立一個簡單的「會員註冊/登入頁面」範例
   - 與 Spring Security 整合的範例
5. 常見錯誤與除錯技巧
6. 專案中使用規範：如何在團隊中一致化使用 Thymeleaf（命名規範、模板結構建議）。
7. 延伸學習資源：官方文件、教學網站、社群。
8. Thymeleaf 認證考試參考：建議的考試範圍、常見題型、練習方向。

## 產出要求

- 請用 簡單易懂的語言、範例程式碼、逐步教學 撰寫，讓同仁看完後能馬上上手，並具備考取 Thymeleaf 認證 的能力。
請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為:hymeleaf使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------

# Vue3 前端framework教學

## 角色設定

- 你是一位資深前端架構師與 Vue.js 專家，精通 Vue 3.x 在大型專案中的應用，並熟悉 Vue 3 官方認證考試範圍。  
  
## 任務說明

- 請幫我撰寫一份「Vue 3.x 教學手冊」，給完全沒有學過 Vue 3 的新進開發同仁使用。
- 教學手冊：讓完全沒學過 Vue 3.x 的新人能循序漸進上手。
- 專案應用：針對你們專案開發實際會用到的 Vue 3.x 技術。
- 認證考試：補充 Vue 3.x 官方認證或常見考點，幫助同仁準備考試。

## 文件內容範圍

1. Vue 3.x 基礎（Composition API、響應式系統、模板語法、生命週期、指令等）  
2. Vue Router、Pinia 狀態管理、與 REST API 串接  
3. 專案中實際會用到的開發規範與最佳實務（例如：組件設計模式、檔案結構、TypeScript 搭配、Tailwind CSS 整合）  
4. 對應 Vue 3 認證考試的知識點與練習題（例如：單元測試、效能優化、常見陷阱）  
5. 範例程式碼（循序漸進，從簡單到專案實例）  
6. 建議的學習路徑與資源（文件、官方教材、練習網站）  

## 產出要求

- 分章節撰寫（類似教科書或內部培訓教材）。
- 每章有「概念說明 → 程式碼範例 → 專案應用指引 → 認證考點提示」。
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 最後附上練習題與參考答案。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: Vue3 前端framework教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------------

# PrimeVue使用教學

## 角色設定

- 你是一位資深前端架構師與PrimeVue專家，精通 Vue 3.x和PrimeVue 在大型專案中的應用，並熟悉 Vue 3.x和PrimeVue 官方認證考試範圍。  

## 背景

手冊需要達到以下目標：

1. 基礎入門：簡介 PrimeVue 與 Vue 的關係、安裝與設定方式。
2. 核心元件：介紹常用的 PrimeVue 元件（如 DataTable、Dialog、Dropdown、Button、Form 元件等），並提供簡單程式範例。
3. 專案實務應用：說明如何在專案中正確使用 PrimeVue（包含版型設計、元件最佳實踐、與 Tailwind CSS 或 Vue Router 整合）。
4. 進階主題：包含自訂樣式、Theme 切換、國際化 (i18n) 支援、最佳化效能。
5. 實作演練：設計幾個練習，例如「建立一個會員管理表單」「建立一個可分頁查詢的 DataTable」。
6. 測驗題目：提供章節後的小測驗，幫助同仁檢驗學習成果，並模擬 PrimeVue 認證考試 題型。
7. 附錄：常見問題 FAQ、官方資源連結、最佳學習路徑建議。

## 任務說明

目錄
第一章：基礎入門
1.1 PrimeVue 簡介
1.2 PrimeVue 與 Vue.js 的關係
1.3 安裝與設定（使用 npm / yarn / Vite / Vue CLI）
1.4 建立第一個 PrimeVue 專案
1.5 Hello World 範例
第二章：核心元件介紹
2.1 按鈕（Button）與圖示（IconButton）
2.2 表單元件（InputText、Password、Dropdown、Checkbox、RadioButton、Calendar、Slider）
2.3 資料顯示元件（DataTable、Listbox、Card、Panel、TabView、Accordion）
2.4 對話框與通知（Dialog、Toast、ConfirmDialog）
2.5 版面配置（Grid、Toolbar、Menubar、Sidebar）
👉 每個元件包含：用途、屬性 (props)、事件 (events)、程式碼範例
第三章：專案實務應用
3.1 在專案中規劃 PrimeVue 元件結構
3.2 與 Tailwind CSS 整合（統一設計風格）
3.3 與 Vue Router 整合（建立多頁應用）
3.4 與 Vuex / Pinia 整合（狀態管理）
3.5 表單驗證實務（PrimeVue + Vuelidate / vee-validate）
第四章：進階主題
4.1 PrimeVue 主題與樣式（Theme 切換）
4.2 自訂樣式與 CSS 變數
4.3 元件客製化（新增內容 ✅）
　- 使用 CSS 修改樣式（Scoped Style / 全域 Style）
　- 使用 Tailwind CSS 客製化 PrimeVue 元件
　- 覆寫 PrimeVue 的 CSS Variables 與 Theme
　- 使用 pt (Pass Through) API 調整 DOM 結構與屬性
　- 建立自訂封裝元件（Wrapper Component）
　- 在專案中定義可重複使用的 UI 樣式規範
4.4 i18n 國際化支援（語系切換）
4.5 效能最佳化（Lazy Loading、虛擬捲動 Virtual Scroller）
4.6 無障礙 (Accessibility, a11y) 支援
第五章：實作演練
5.1 練習一：會員管理表單

- 使用 InputText、Password、Dropdown、Button
- 新增/修改/刪除會員資料
5.2 練習二：分頁查詢的 DataTable
- 資料載入
- 分頁、排序、篩選功能
5.3 練習三：彈出式對話框應用
- 建立新增紀錄 Dialog
- Toast 顯示通知

5.4 綜合專案：簡易任務管理系統 (Task Manager)

- 新增/刪除任務
- 使用 DataTable、Dialog、Toast、Calendar
第六章：認證模擬測驗
6.1 單選題範例（基礎 API、屬性、事件）
6.2 程式碼題（填空/錯誤修正）
6.3 情境題（最佳實務應用）
6.4 答案與解析
第七章：附錄
7.1 常見問題 FAQ
7.2 官方文件與資源
7.3 推薦學習路徑
7.4 參考書籍與社群

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為:PrimeVue使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------------

# Angular 前端framework教學

## 角色設定

- 你是一位資深的前端架構師與講師，熟悉 Angular 開發與認證考試內容。
請幫我撰寫一份 Angular 教學手冊，提供給專案中新進的開發同仁使用。

## 任務說明

1. 受眾：新進同仁，完全沒有學過 Angular。
2. 內容目標：

- 從基礎開始（Angular 架構、模組、元件、資料繫結、服務、路由等）。
- 涵蓋實務開發中會用到的功能（表單處理、HTTP 呼叫、RxJS、State Management、測試、最佳實務）。
- 融合專案中實際會用到的 Angular 開發方式（例如專案框架、程式碼規範、API 呼叫模式、UI/UX 指引）。
-幫助同仁能夠參加並考過 Angular 官方認證。

## 文件內容範圍

1. 前言（為什麼要學 Angular、專案背景）。
2. 基礎篇（Angular 架構概念、環境建置）。
3. 進階篇（常見模組、RxJS、最佳實務）。
4. 專案實務篇（如何在專案中使用 Angular、範例程式碼）。
5. 認證準備篇（認證考試重點、模擬題）。
6. 附錄（常見問題、資源連結）。

## 產出要求

-清楚、結構化、帶有程式碼範例，適合初學者循序漸進學習。

- 請依上述需求產出完整的 Angular 教學手冊（可分章節、逐步展開）。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: Angular 前端framework教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------

# PrimeNG使用教學

## 角色設定

- 你是一位資深前端架構師與PrimeNG專家，精通Angular和PrimeNG 在大型專案中的應用，並熟悉 Angular和PrimeNG 官方認證考試範圍。  
- 「請扮演一位 PrimeNG 專家講師，幫我撰寫一份 專案用的 PrimeNG 教學手冊，目標對象是 從未學過 PrimeNG 的新進開發同仁。

## 背景

內容需包含：

1. PrimeNG 基礎概念：什麼是 PrimeNG、安裝與環境設定、與 Angular 的整合方式。
2. 常用元件教學：例如 Button、Table、Form、Dialog、Menu、Chart，提供程式碼範例與實際應用案例。
3. 專案實務應用指引：如何在企業專案中正確使用 PrimeNG（包含最佳實務與注意事項）。
4. 客製化元件方法：如何覆寫樣式、整合 Tailwind / SCSS、擴充元件功能。
5. PrimeNG 認證考試導引：考試重點、常見題型、準備方向。
6. 附錄：練習題、專案範例連結或模擬考題。

## 任務說明

PrimeNG 教學手冊目錄
第 1 部分：基礎入門

1. PrimeNG 簡介
   - 什麼是 PrimeNG
   - 為什麼選擇 PrimeNG
   - 在企業專案中的角色
2. 環境安裝與設定
   - 建立 Angular 專案
   - 安裝 PrimeNG 與 PrimeIcons
   - 主題 (Themes) 與樣式設定
   - 整合 PrimeFlex
3. PrimeNG 基本使用流程
   - 匯入元件模組
   - 建立第一個 PrimeNG 頁面
   - 理解 Angular 與 PrimeNG 的關係
第 2 部分：常用元件教學
4. 按鈕與圖示 (Button, SplitButton, Icons)
5. 表單元件
   - InputText, Password, Textarea
   - Dropdown, MultiSelect, Listbox
   - Checkbox, RadioButton, ToggleButton
   - Calendar, DatePicker, Slider
6. 表格 (DataTable)
   - 基本表格顯示
   - 排序、分頁、篩選
   - 可編輯表格
   - Lazy Loading 與 API 整合
   - 匯出功能 (CSV/Excel/PDF)
7. 對話框與訊息元件
   - Dialog, ConfirmDialog, Sidebar
   - Toast, Messages
8. 選單與導覽元件
   - Menubar, TieredMenu, ContextMenu
   - TabMenu, Breadcrumb
   - Steps, MegaMenu
9. 圖表 (Charts)
   - 基本圖表 (Pie, Bar, Line)
   - 複合圖表與客製化
10. 其他實用元件

- FileUpload
- Accordion, Panel, Card
- ProgressBar, Skeleton, Avatar
第 3 部分：專案實務應用

11. PrimeNG 與 Angular Forms 整合
12. 企業專案中常見的 UI 模式

- CRUD 表單設計
- 大量資料表格處理策略
- 即時通知與狀態提示

13. 效能最佳化

- Lazy Loading
- 處理大量 DOM 元素
- 處理圖片與資源載入
第 4 部分：進階與客製化

14. 樣式客製化

- 覆寫 PrimeNG 預設樣式
- 使用 SCSS/Tailwind 客製化
- 主題切換 (Theme Switching)

15. 元件擴充與封裝

- 建立共用元件 (Shared Components)
- 包裝 PrimeNG 元件以符合專案需求

16. 無障礙 (Accessibility, A11y) 與多語系支援
第 5 部分：認證導向學習
17. PrimeNG 認證簡介

- 考試形式與範圍
- 準備方法

18. 考試重點整理

- 常用元件 API
- 常見陷阱與最佳實務

19. 模擬試題與解析
第 6 部分：附錄
20. 練習題與專案實戰

- 建立小型 CRUD 系統
- 整合表單、表格與對話框

21. 學習資源

- 官方文件、範例程式碼
- 社群資源與教學影片

22.常見問題 (FAQ)

## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為:PrimeNG使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------

# React 前端framework教學

## 角色設定

- 你是一位資深的前端架構師與技術講師，請幫我撰寫一份 React 教學手冊，內容要給「新進開發同仁」閱讀，他們 完全沒有學過 React。

## 任務說明

手冊要達到兩個目的：

1. 指引同仁能在我們專案中正確使用 React 進行程式開發。
2. 幫助同仁能準備並考取 React 認證。

## 文件內容範圍

手冊需要包含以下章節：

1. 基礎概念：React 的核心原理、JSX、Component、Props、State、Hooks 等。
2. 專案實務：如何依照我們專案架構開發（例如：元件拆分規範、狀態管理策略、API 呼叫方式、UI/UX 開發流程）。
3. 進階主題：React Router、Context API、狀態管理（Redux/Zustand）、效能最佳化。
4. 測試與品質：如何撰寫 React 測試（Jest、React Testing Library）、程式碼規範、Lint/Formatter 使用。
5. 實戰演練：專案中會用到的範例程式（如表單處理、API 資料綁定、前後端整合）。
6. 認證準備指南：React 認證常見考點、練習題範例與學習資源。

## 產出要求

- 從零基礎開始，循序漸進。
- 每個章節都附上 程式碼範例 與 專案實際應用案例。
- 最後附上 知識檢核題，讓同仁自我測驗。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\framework\ 目錄下,檔名為: React前端framework教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------

# Spring Framework教學

## 角色設定

- 你是一位資深的 Java 與 Spring 架構師，同時熟悉教學設計與 Spring Framework 認證考試內容。

## 任務說明

請幫我撰寫一份 Spring Framework 教學手冊，給新進開發同仁使用，這些同仁：

- 沒有學過 Spring Framework，Java 基礎程度中等。
- 需要能在專案中正確使用 Spring Framework 進行程式開發。
- 需要具備足夠知識與實作能力，以通過 Spring Professional Certification 認證考試。

## 文件內容範圍

手冊內容需求:

1. 基礎概念：IoC、DI、AOP、Bean 管理、ApplicationContext。
2. 核心模組：Spring Core、Spring Context、Spring Beans、Spring Expression Language。
3. Web 開發：Spring MVC、REST API 建立。
4. 資料存取：Spring JDBC、Spring Data JPA、Transaction 管理。
5. 進階主題：Spring Security、Spring Boot 與 Spring Framework 的差異與整合。
6. 實作範例：以簡單專案案例展示配置、程式碼撰寫與專案結構。
7. 最佳實務：在專案中如何設計模組化、可維護性強的 Spring 應用程式。
8. 認證導向：附上認證考試重點章節對應、練習題示範。

## 產出要求

- 分章節撰寫（類似教科書或內部培訓教材）。
- 每章有「概念說明 → 程式碼範例 → 專案應用指引 → 認證考點提示」。
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 最後附上練習題與參考答案。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\framework\ 目錄下,檔名為: Spring Framework教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------

# Spring Boot 教學

## 角色設定

- 你是一位資深的Java架構師與Spring專家，同時熟悉Spring Boot認證考試的內容與範例。

## 任務說明

- 請幫我撰寫一份「Spring Boot 教學手冊」，對象是新進開發同仁，他們不曾學過Spring Boot。  
此手冊需要同時滿足：

1. 幫助新進同仁快速學會在專案中使用Spring Boot進行程式開發。  
2. 涵蓋Spring Boot認證考試的重要知識與考點，讓同仁能夠準備考試。  
3. 內容需包含基礎教學、實務應用與進階考試重點。

## 文件內容範圍

1. Spring Boot 簡介（特點、與Spring Framework的差異、專案常見應用場景）  
2. 開發環境建置（JDK、Maven/Gradle、IDEA、Spring Initializr、VS code）  
3. Spring Boot 基礎（專案結構、主程式、application.properties設定、依賴注入）  
4. RESTful API 開發（Controller、Service、Repository）  
5. 與資料庫整合（JPA、Transaction、DB連線設定）  
6. 常用功能（Validation、Exception Handling、Logging、Security、Spring batch 簡介）  
7. 測試與品質（JUnit、Spring Boot Test、MockMvc）  
8. 部署與實務應用（內嵌伺服器、Docker、雲端部署簡介）  
9. 認證考試重點（必考知識、練習題、模擬題示範）  
10. 常見問題與最佳實務（FAQ + Best Practices）  

## 產出要求

- 以教學手冊的方式撰寫，條理清楚，逐步教學。  
- 搭配完整範例程式碼與輸出結果。  
- 重要概念搭配圖解。  
- 每章節後附小練習或測驗題，幫助理解並準備認證考試。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\framework\ 目錄下,檔名為: Spring Boot 教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆
----------------------------------------------------f-

# 補充內容

1. 請針對本文逐章節,一步一步檢查內容是否足夠完整
2. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
3. 同時更新目錄與子目錄

-------------------------------------------

# 專案review指引

## 角色設定

- 你是一位資深的專案經理兼部門主管，長期負責跨部門專案管理與專案稽核，熟悉專案管理流程、PMBOK、敏捷與銀行/金融業務專案執行方式。

## 任務說明

- 請撰寫一份 《專案 Review 指引》 文件，對象是 新進部門主管。此文件要幫助主管有效地審視與管理部門專案，確保進度、品質、風險與資源使用得當。

## 文件需求

請包含以下內容：

1. 文件目的與重要性
   - 為什麼主管需要做專案 review？
   - 主管在專案治理中的角色與責任。
2. 專案 Review 的流程與步驟
   - 準備階段（收集專案資訊、建立檢視清單）
   - 審查階段（進度、成本、品質、風險、資源、依存關係）
   - 討論與回饋階段（如何主持會議、提出建議、追蹤改善事項）
   - 後續跟進（如何確保改進落實、如何紀錄 review 結果）
3. 專案 Review 的重點檢核項目
   - 專案目標與商業價值對齊程度
   - 進度與里程碑狀況
   - 成本與預算控管
   - 風險與議題管理
   - 品質保證與測試狀況
   - 資源配置與團隊狀態
   - 利害關係人溝通與滿意度
4. 最佳實務與常見錯誤
   - 主管應如何提供支持而不是微觀管理
   - 常見的 review 誤區（只看數字、不關注風險、不給具體行動建議）
   - 有效的提問與引導技巧
5. 範例與工具
   - 建議的專案 review 問題清單
   - Review 報告或會議紀錄範例格式
   - 可用的專案管理工具（如 Jira、MS Project、Excel Dashboard）
6. 結語
   - 如何透過持續 review 建立部門專案治理文化
   - 鼓勵主管用 review 作為溝通與提升團隊的機會

## 產出要求

- 採用正式的專案管理文件格式
- 條列清晰，適合主管快速理解與應用
- 可搭配表格、檢核清單或範例模板
- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的主管閱讀
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:專案review指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

_________________________________________________

# 通用 Prompt 模板

## 角色設定

你是一位擁有 {{年數}} 年 {{領域}} 專案經驗的資深專案經理，熟悉 {{方法論/框架}}。

## 任務說明

請為新進專案經理撰寫一份「{{文件主題}}」文件，讓初學者能快速理解並應用在實務專案中。

## 內容範圍

{{章節 1}}

{{章節 2}}

{{章節 3}}

{{章節 4}}

{{章節 5}}

## 格式與風格

使用 {{格式類型，例如 Markdown}} 格式，含標題、編號與條列

每節結尾提供實務案例或注意事項

用淺顯易懂的語言，適合 {{讀者層級，例如初入行的 PM}} 閱讀

全文長度約 {{字數，例如 3000 字}}
______________________________________________

# 專案管理相關文件

## 專案管理指引

## 專案啟動流程指引

## 專案風險管理指引

## 專案溝通管理指引

## 專案品質管理指引

## 敏捷專案管理指引

## 金融專案合規要求手冊

## 客戶需求訪談與分析技巧

# 專案管理指引

## 角色設定

你是一位擁有 15 年跨國金融 IT 專案經驗的資深專案經理，熟悉 PMP、Agile 與 SSDLC 流程。

## 任務說明

你要為新進專案經理撰寫一份「專案管理指引」文件，內容要清楚、結構化，讓初學者可以快速上手。

## 內容範圍與格式

- 明確列出章節、細節、輸出格式。

- 文件內容需包含：

  1. 專案管理流程概述（啟動、規劃、執行、監控、收尾）

  2. 各階段關鍵任務與檢核點

  3. 常見風險類型與應對措施

  4. 溝通與會議管理技巧

  5. 文件與報告管理

  6. 附錄：範例與模板（如專案計劃書、風險登錄表）

## 範例與模板連結

- 輸出格式採 Markdown，含標題與編號。
- 使用 Markdown 格式，含標題、編號與條列
- 每節結尾提供實務案例
- 用淺顯易懂的語言，適合初入行的 PM 閱讀
- 請提供相關的參考資料與連結
- 以繁體中文撰寫
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:專案管理指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

## 風格與語氣要求

- 用淺顯易懂的語言、搭配專業案例，條列清晰、避免過度艱澀的術語。

-----------------------------------------------

# 專案啟動流程指引

# 角色設定

你是一位擁有 15 年以上經驗的資深專案經理，熟悉 PMP 與敏捷專案管理，能清楚規劃專案啟動階段的各項工作。  
你的目標是撰寫一份「專案啟動流程指引」，內容需簡單易懂，讓新進專案經理能快速上手。

# 專案背景

- 公司屬於大型金融科技企業
- 專案類型包含系統開發、基礎架構升級與法遵專案
- 對象是剛入職 0-2 年的 PM
- 使用語言為繁體中文
- 文件要可作為內部培訓教材

# 任務目標

1. 定義專案啟動的流程階段與順序（例如：專案立案 → 需求初步確認 → 組建團隊 → 啟動會議）
2. 說明每個階段的工作內容、負責角色、輸出成果（Deliverables）
3. 提供關鍵檢核點（Checkpoints）與常見風險提醒
4. 製作一張簡明流程圖或表格
5. 提供一個專案啟動文件的範本結構

# 產出規格

- 採用條列與表格混合，方便閱讀
- 內容結構需清楚分段（章節編號 + 標題）
- 適度使用案例或情境說明
- 避免過度學術化，偏實務操作
- 最後附上一份 5 條「成功專案啟動的關鍵建議」
- 請提供相關的參考資料與連結

# 輸出格式

- Markdown 格式
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:專案啟動流程指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

# 專案風險管理指引

## 角色設定  

你是一位擁有 12 年金融 IT 專案管理經驗的資深專案經理，熟悉風險管理與合規流程。

## 任務說明  

請為新進專案經理撰寫一份「專案風險管理指引」文件，讓初學者能快速理解如何識別、分析與應對專案風險。

## 內容範圍  

1. 專案風險管理的定義與重要性  
2. 風險分類（技術、管理、外部、合規）  
3. 風險識別方法（訪談、檢核表、歷史資料）  
4. 風險評估（概率、影響、優先級）  
5. 風險應對策略（規避、轉移、減輕、接受）  
6. 風險監控與更新流程  
7. 附錄：風險登錄表模板與範例  

格式與風格  

- 使用 Markdown 格式，含標題、編號與條列  
- 每節結尾提供實務案例  
- 用淺顯易懂的語言，適合初入行的 PM 閱讀  
- 請提供相關的參考資料與連結
- 以繁體中文撰寫
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:專案風險管理指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

---------------------------------------

# 專案溝通管理指引

## 角色設定

你是一位擁有 15 年經驗的資深專案經理，熟悉銀行與金融業大型系統專案管理，專長於跨部門協作與溝通管理。

## 任務說明

背景：公司要培訓新進專案經理（PM），他們需要一份「專案溝通管理指引」，用來指導在專案不同階段如何規劃、執行與監控溝通，確保專案干係人資訊透明、決策高效、衝突可控。

## 內容範圍

請根據專案管理知識體系（PMBOK 第七版）與實務經驗，產出一份完整的「專案溝通管理指引」文件，包含：

1. 目的與重要性  
2. 溝通目標  
3. 溝通角色與責任  
4. 溝通計畫（對象、頻率、方式、內容）  
5. 溝通紀錄與追蹤機制  
6. 衝突與異議處理  
7. 溝通成效評估方式  
8. 最佳實務案例

## 格式要求

- 使用條列清單與小標題，層次清楚。
- 採繁體中文撰寫，適合企業內部培訓文件。
- 內容需兼顧理論與實務，並附帶簡短範例。
- 文件風格正式、專業、易讀。
- 請提供相關的參考資料與連結
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:專案溝通管理指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------

# 專案品質管理指引

## 角色設定

你是一位擁有 PMP 資格的資深專案經理，熟悉 PMBOK 的專案品質管理流程，且有10年以上金融業大型專案經驗。

## 任務說明

請依照下列要求，為剛入職的新進 PM 撰寫一份《專案品質管理指引》，內容要包含：

1. 品質管理的重要性與目標
2. 品質規劃、品質保證、品質控制的詳細流程
3. 常用品質工具與方法（檢核表、魚骨圖、控制圖等）
4. 專案品質指標範例
5. 品質稽核流程
6. 銀行系統專案品質管控實務案例
7. 常見問題與解法
8. 附錄：檢核清單範例

## 內容範圍

請使用淺顯中文撰寫，格式清晰（含目錄、章節標題、條列清單），並在每個章節附一個簡單案例。

## 格式要求

- 使用條列清單與小標題，層次清楚。
- 採繁體中文撰寫，適合企業內部培訓文件。
- 內容需兼顧理論與實務，並附帶簡短範例。
- 文件風格正式、專業、易讀。
- 請提供相關的參考資料與連結
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:專案品質管理指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------

# 敏捷專案管理指引

## 角色設定

你是一位擁有 15 年經驗的資深專案經理，精通敏捷專案管理（Agile）、Scrum、Kanban，熟悉金融業與大型平台專案開發的實務案例。  
你需要編寫一份「敏捷專案管理指引」，用於培訓新進專案經理（PM）。

## 文件目的

- 幫助新進 PM 快速理解並掌握敏捷專案管理的核心概念與實務操作
- 提供可直接套用到專案的流程與範例
- 讓新進 PM 在銀行與金融業的 IT 專案中能正確應用敏捷方法

# 文件內容需求

1. **前言**  
   - 敏捷專案管理的定義與重要性  
   - 與傳統瀑布式開發的差異  

2. **敏捷專案管理核心原則**  
   - Agile Manifesto 四大價值、十二項原則  
   - 在金融/銀行專案中的適用性說明  

3. **常用敏捷方法**  
   - Scrum（角色、事件、產出物）  
   - Kanban（看板設計、在制品限制）  
   - 混合模式（ScrumBan）  

4. **敏捷專案管理流程**  
   - 需求收集與優先級排序  
   - Sprint 規劃、每日站會、Sprint Review、Sprint Retrospective  
   - 待辦清單管理（Product Backlog、Sprint Backlog）  
   - 工作拆解與估時（Story Points、Planning Poker）  

5. **敏捷工具與實務應用**  
   - Jira / Trello / Azure DevOps 使用要點  
   - 团队協作技巧與溝通模式  
   - 與利害關係人互動的策略  

6. **敏捷專案管理在銀行系統的特別注意事項**  
   - 法規與稽核配合  
   - 敏感資料安全與保密要求  
   - 跨部門溝通與外包管理  

7. **常見問題與解決策略（FAQ）**  
   - 團隊抗拒敏捷  
   - 需求變動過於頻繁  
   - 開發與業務優先級衝突  

8. **結論與建議**  
   - 如何在不同規模專案中靈活應用敏捷  
   - 新進 PM 的學習資源清單（書籍、網站、社群）

## 文件格式

- 採 Markdown 格式，包含標題、子標題、項目符號、表格與範例
- 每個章節至少舉一個實務案例
- 使用清晰易讀的語言，避免過度專業術語

## 輸出語言

- 正體中文
- 文件風格正式、專業、易讀。
- 請提供相關的參考資料與連結
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:敏捷專案管理指引.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------

# 金融專案合規要求手冊

## 角色設定

你是一位具有 15 年金融業專案管理經驗的資深專案經理，熟悉國際與台灣金融法規（如：巴賽爾協定、AML、KYC、GDPR、個資法等），且曾負責銀行、保險、證券業的大型系統建置與合規審查。  

## 任務說明

請撰寫一份《金融專案合規要求手冊》，用於指導新進專案經理在規劃與執行金融專案時，如何確保符合法規與內部稽核要求。  

手冊需涵蓋以下範疇：  

1. 金融專案中常見的合規要求概述  
2. 主要法規與標準（國內/國際）  
3. 專案生命周期各階段的合規檢查清單  
4. 專案文件與紀錄保存要求  
5. 風險管理與稽核應對  
6. 案例示例與常見錯誤  

## 格式要求  

- 條列式、分段清楚  
- 每章節附簡要說明與具體操作指引  
- 附加合規檢查清單  
- 專業但易理解的語氣
- 文件風格正式、專業、易讀。
- 請提供相關的參考資料與連結
- 文件請放在專案的 .github\指引\專案管理\目錄下,檔名為:金融專案合規要求手冊.md，並使用 Markdown 格式撰寫。
- 請分段回覆

## 額外要求  

- 特別標註與台灣金融業相關的法規  
- 英文專有名詞附中文解釋  
- 提供大型與中小型金融專案的差異建議  

--------------------------------------

# 客戶需求訪談與分析技巧

## 角色設定

你是一位擁有 15 年以上經驗的資深專案經理，熟悉金融、IT 與大型系統整合專案，並具備專業的客戶需求訪談與需求分析技巧。

## 專案背景

- 目標讀者：剛入職 0–2 年的新進 PM
- 使用情境：公司內部 PM 培訓教材
- 教材目的：教導 PM 如何有效進行客戶需求訪談、蒐集資訊、分析需求，並將需求轉換成可執行的規格

## 任務描述

請撰寫一份完整的《客戶需求訪談與分析技巧指引》，內容需包含：

1. 前置準備  
   - 訪談前需蒐集的資料  
   - 訪談議程與問題設計方法  
   - 如何確認訪談目標與參與人員
2. 訪談進行技巧  
   - 開場與建立信任感的方法  
   - 問答技巧（開放式、封閉式、追問、澄清）  
   - 控制時間與議題的方法
3. 訪談紀錄與整理  
   - 記錄重點的技巧  
   - 訪談紀錄格式範例  
   - 如何避免資訊遺漏或誤解
4. 需求分析方法  
   - 需求分類（功能性 / 非功能性）  
   - 優先順序設定方法（如 MoSCoW、Kano）  
   - 確認需求真實性與可行性的方法
5. 常見錯誤與避免方法  
   - 訪談偏誤、假設過多  
   - 需求分析中常犯的錯誤與解決方案
6. 附錄  
   - 訪談問題範例清單  
   - 訪談紀錄表格模板  
   - 需求分析報告範例

## 輸出格式

- 使用清晰的標題與小節
- 每個重點以條列方式呈現，並附上簡短案例
- 文字專業、易懂、可直接用於培訓文件
- 請用繁體中文撰寫。
- 請提供相關的參考資料與連結
- 文件請放在專案的 .github\指引\需求分析\ 目錄下,檔名為:客戶需求訪談與分析技巧.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------

# common_platform 專案建置 prompt

## 角色設定

你是一個資深的架構師與專業的程式設計師,程經開發過,單體,container, 微服務等不同架構的應用系統期用平台.這個平台適用於所有web application.

## 專案背景

要開發一個大型共用的平台專案.這個平台適用於所有web application.未來其它專案可以拿本專案為基礎, 在依自己的專案去擴充與客制化.

## 任務描述

1.平台採前後分離的架構,前端必需支援微前端架構,找出目前業界最常用的微前端架構 CSS使用:Tailwind CSS, 開發語這使用Typescript開發,支援log,exception,多語系,監控等功能,前端系統的設定檔必需統一在一個地方設定.

2.前端為SPA (Single-Page Application), 開發同時考量網頁要有RWD效果,注重UI/UX,同時列出UI/UX規則.

3.前端因客戶技術走向,分二個子專案

第一個前專的子專案,前端架構採用 VUE3.x最新版,Vue 3 打造的現代化 UI 元件庫,使用 PrimeVue.

第二個前專的子專案,前端架構採用 Angular 最新版,  Angular UI 元件庫,使用 PrimeNG.

4.後端採用Clean architecture , serverless 架構,使用restful api與後端整合,使用Swagger自動建立清晰明瞭的REST API文件.

5.後端技術框架採用Spring boot 3.5.x最新版,serverless架構, 依客戶需求可以設計成單體或微服務,系統可跑在container, VM上.

5.後端資料庫設計,使用ER model做資料庫設計, ORM, 使用JPA實作, 資料庫支援,oracle,db2,sql server,postgresql.

6.平台支援功能有 cache , 與MQ ,sftp,ftps, batch, teams,line,log,exception,多語系,監控 等機制

7.後端系統的設定檔必需統一在一個地方處理.

8.程式碼使用github去管理,專案使用Maven建置.使用archunit測試各層功能,單元測試使用junit5,SonarQube 代碼品質檢查.

9.開發工具,前端使用,vs code, 後端使用intellj community/vs code來開發專案.

10.開發與測試使用container, 使用podman.

11.在多個container下要有統一可以收log,看問題,並可以視覺化看cup.request等監控指標,等機制.

12.本專案可同時使用vs code/ intellj community 開發,如何以上面的需求建立所需的專案結構和目錄與做專案的初始化

13.同時提供寫作的範例與寫作的提引

----------------------------------------

6.在common_platform,分前端二個子專案與後端一個子專案

b.後端技術框架採用,可依設定動態綁定Spring boot/Micronaut/Quarkus/Helidon/JEE,依CA架構,格離技術框架,serverless架構, 依客戶需求可以設計成單體或微服務,系統可跑在container, VM上.

5.後端,資料庫設計,使用ER model做資料庫設計, ORM, 使用JPA實作, 資料庫支援,oracle,db2,sql server,postgresql.

6.平台支援功能有 cache , 與MQ ,sftp,ftps, batch, teams,line,log,exception,多語系,監控 等機制

7.後端系統的設定檔必需統一在一個地方處理.

8.程式碼使用github去管理,專案使用Maven建置.使用archunit測試各層功能,單元測試使用junit5,SonarQube 代碼品質檢查.

9.開發工具,前端使用,vs code, 後端使用intellj community/vs code來開發專案.

10.開發與測試使用container, 使用podman.

11.在多個container下要有統一可以收log,看問題,並可以視覺化看cup.request等監控指標,等機制.

12.提供四個工具, 一個desktop設定, 由editor 產生json, 在由json 產生spa首頁, 一個為頁面產生器,由editor 產生json, 在由json網頁, 一個為電文產生器, 一個為列印憑證產生器

13.未來其它專案可以拿本專案為基礎, 在依自己的專案去擴充

14.在common_platform,分前端與後端二個子專案

15.如何在vs code/ intellj community 中建立所需的專案結構和目錄與做專案的初始化

common_platform

二.本專軟硬體架構 prompt
1.

git 設定 prompt

同一部電腦,有三個 git 帳號,

1. 私人gitlab 帳號:chihhung.cheng@gmail.com   Server: github

2, 公司gitlab copilot 帳號:IISI-1104358   Server: github

3. 公司內部 帳號: 1104358   Server: gitlab

電腦內部git應如何設定, vscode 應如何設定

使用vscode中的 github copilot 建立一個java專案, 本專案主要是要成員如何使用vscode 撰寫java程式,教成員如何使用vs code寫程式,同時教成員java 程式,

同時上傳至github, 與成員共用,專案使用maven來管理.

--------------------------------------------------------------------------------------
# spec-kit使用教學

## 參考網站
https://github.com/github/spec-kit 請了解本網站的內容

https://github.com/github/spec-kit/blob/main/spec-driven.md 這是SDD的方法論

https://github.com/github/spec-kit?tab=readme-ov-file#-detailed-process 這是執行步驟

## 角色設定
- 你是一位使用SDD的專家與資深軟體開發工程師
## 背景
- 目前使用spec-kit 透過AI 來協助軟體開發
## 任務說明

教學手冊 大綱
前言
- 目的與適用對象
- 背景說明：為何採用 SDD + Spec-Kit → AI 助手流程
- 本手冊使用假設：你已具備基本軟體開發流程、版本控制 (GitHub)、且團隊準備導入 AI 輔助開發

第一章：概念理解

1. SDD 是什麼？
- 傳統開發 vs Spec-Driven 開發的差異
- 規格（spec）在開發中的角色提升
- 為何在 AI 助手輔助開發中更重要

2. Spec-Kit 概覽
- Spec-Kit 的定位、工具組成（CLI、模板、提示） 
- 支援的 AI 助手 / 智能代理 (agents) 

3. SDD 中的關鍵 artefacts（工件）
- Constitution（項目守則）
- Spec（什麼要做 & 為什麼）
- Plan（如何做／技術規劃）
- Tasks（可執行工作單元）
- Implementation（實作）

4.流程概覽：SDD 的階段／步驟
- Specify → Plan → Tasks → Implement + 迭代
- 如何與 AI 助手互動（人員角色、AI 角色、輸入／回饋）

5. 為什麼這對我們團隊／共用平台開發特別有價值（針對你的背景）
- 多系統、多資料庫、多模組、微前端＋後端、AI 輔助開發…
- 規格先行，有助於：共用平台維護、模組化、團隊協作、AI 代理可信度提升

第二章：環境準備

1. 前置條件
- 已有 GitHub 倉庫、版本控制流程
- 團隊有 AI 助手（如 GitHub Copilot、Claude Code…）
- Spec-Kit 支援的系統／CLI 要求(Python、uvx／uv、shell／PowerShell)

2. 安裝 Spec-Kit CLI
- 安裝命令範例(persistent 安裝／一次性使用)
- 建立專案初始目錄、使用 specify init <PROJECT_NAME>
- 生成 .specify/ 與 .github/ 等目錄結構

3. 建立團隊守則（Constitution）
- 使用 /speckit.constitution 指令範例
- 守則內容範例：程式碼品質、測試標準、技術棧約束、AI 代理使用規範
- 為什麼守則在團隊／平台開發中重要

4. 模板與提示文件說明
- 說明 .specify/templates 結構：spec-template.md、plan-template.md、tasks-template.md … 
- 如何針對團隊／平台需求自訂模板（技術棧、資料庫、語言、微服務架構）

5. GitHub 倉庫分支與版本控制建議
- 建議在每個 spec 變更或重大功能前建立分支
- 如何與 CI/CD、代碼審查流程整合

第三章：使用流程詳細說明

1. Step 1：撰寫 Spec (/speckit.specify)
- 指令範例：/speckit.specify Build an application that … 
- Spec 應包含的內容：目標、用戶情境、成功標準、邊界條件、排除項目
- 實務建議：如何使 Spec 清晰、可讀、可機器理解（為 AI 助手用）
- 審查與澄清：若發現模糊或未定義部分，使用 /speckit.clarify 進行補充

2. Step 2：撰寫 Plan (/speckit.plan)
- 指令範例：/speckit.plan The application uses Vite …
- Plan 包含的內容：技術棧、架構圖、資料流、服務接口、資料庫方案、整合點、非功能需求（效能、安全、可伸縮）
- 團隊如何審查 Plan：技術導師／架構師角色，對齊 Constitution、Spec

3. Step 3：拆分 Tasks (/speckit.tasks)
- 指令作用：從 Plan 拆成可執行單元（user stories、工作項目） 
- Task 文件內容範例：描述、驗收準則、依賴項、預估時間、負責人
- 建議：在任務中明確寫明 AI 助手角色與人員角色分工

4. Step 4：預實作檢查／一致性分析 (/speckit.analyze + /speckit.checklist)
- 分析是否 Spec ↔ Plan ↔ Tasks 三者一致，是否違反 Constitution
- Checklist 檢查點：安全、可測性、國際化、多資料庫支援、異步處理需求、介面契約、可維護性
- 團隊評審會議建議：定期檢查這些 artefacts

5. Step 5：實作 (/speckit.implement)
- 指令：/speckit.implement 將從 Tasks → AI 助手／人員實作
- 如何與團隊現有開發流程整合（版本分支、提交、代碼審查、單元測試、微服務部署）
- AI 助手使用建議：由人員綁定 Task、提醒 AI 助手先讀 Spec/Plan再出碼

6. Step 6：迭代與維護
- 當需求變更、技術棧變更、團隊規模變化時，如何更新 Spec → Plan → Tasks → Implementation
- Spec 可視為「活文件」而不是一次性檔案
- 如何管理版本、回滾、追蹤決策脈絡（可使用 Git 分支、標籤）
- 如何回顧與改進：每個 Sprint／Iteration 檢查 Spec→實作是否偏離、找出改善點

第四章：實務案例與應用指引

1. 案例：從零開始開發新微服務（Greenfield）
- 示範 Spec → Plan → Tasks → Implementation 流程
- 團隊應用 AI 助手配合 Spec-Kit 的實作細節

2. 案例：在既有大型平台中導入（Brownfield）
- 如何在已有系統（如你所管理的共用平台、支援多 db、多服務、多微前端）中使用 SDD
- 如何拆舊、制定守則、更新規格、分支策略

3. 團隊角色與分工建議
- Spec 擁有者（可能是產品／架構師）
- Plan 擁有者（技術架構師）
- Task 拆分者（開發領導／組長）
- 實作者（開發人員 + AI 助手）
- 質量保證／審查者（測試／DevOps）

4. AI 助手最佳實務
- 如何給 AI 助手讀取 Spec/Plan/Tasks 前文脈
- 避免 AI 助手「自由發揮」而偏離 Spec：用明確 prompt、鏈接 artefact
- 人員 review AI 產出的程式碼：確保符合 Spec、符合團隊守則
- 如何處理 AI 產出的偏差、Hallucination、重進流程

5. 團隊導入建議與變革管理
- 如何讓團隊從「vibe-coding」轉向「spec-first」文化
- 初期試點建議：選擇一個中型功能導入 SDD
- 學習曲線與阻力：如何克服（培訓、範例、mentor）
- 成效指標：例如開發速度、錯誤率、可維護性、AI 助手價值提升

6. 與你的平台背景對應建議
- 多資料庫、多批次工作、SFTP/FTPS、微服務：如何在 Spec 中涵蓋這些複雜需求
- 與 AI 導入的 SSDLC（安全軟體開發生命週期）整合：Spec 可納入安全要求、測試策略、代碼掃描流程
- 如何使 Spec-Kit 的流程與你目前的 Spring Boot +微前端 +批次架構契合

第五章：常見問題 (FAQ) & 陷阱
1. 為什麼這麼早寫 Spec？會不會拖慢開發？
2. 我們已有成熟流程，導入 SDD 會不會衝突？
3. AI 助手總是出錯／偏離 Spec，怎麼辦？
4. 我們已有遺留系統（Brownfield），該如何漸進導入？
5. Spec 過於龐大、有人不願寫，怎麼鼓勵？
6. 如何確保 Spec 與實作、代碼、測試保持同步？
7. 維護 Spec 負擔大，怎麼處理？

第六章：附錄

- 模板範例檔案（constitution.md、spec.md、plan.md、tasks.md）
- Spec-Kit CLI 聊天/提示指令清單
- 團隊守則範本（針對你共用平台的例子）
- 推薦資源與進一步閱讀（官方 Spec-Kit repo、相關文章）
- 變更記錄與版本管理建議


## 產出要求

- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為:spec-kit使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆
------------------------------------------------------------------------------
# OpenSpec使用教學
## 角色設定
你是一位 Spec-Driven Development（SDD）專家與資深軟體架構師，
熟悉 OpenSpec（https://github.com/Fission-AI/OpenSpec） 的方法論與實務操作，
並具備在銀行或大型企業導入 AI 輔助開發的經驗。

## 背景
我們的團隊目前使用 OpenSpec，透過 AI 協助軟體開發，
目標是讓「規格（Spec）」成為開發的唯一真實來源（Single Source of Truth），
並讓新進同仁能快速理解：
- 為什麼要用 OpenSpec
- 如何在日常專案中正確使用 OpenSpec
- 如何與 AI 協作產出高品質、可落地的系統規格

## 目標讀者
- 新進軟體工程師（Junior / Mid-level）
- 新進系統分析師（SA）
- 尚未接觸過 SDD 或 OpenSpec 的同仁

## 任務
請產出一份「OpenSpec 使用教學手冊」，作為公司內部正式訓練教材。

## 教學手冊內容需求
請至少包含以下章節，並以「實務導向」撰寫：

1. OpenSpec 是什麼？
   - 為什麼會有 OpenSpec
   - 與傳統 PRD / SRS / 設計文件的差異
   - OpenSpec 在 SDD 中扮演的角色

2. Spec-Driven Development（SDD）核心概念
   - 規格優先（Spec First）
   - 規格即合約（Spec as Contract）
   - 規格可被 AI 理解與執行

3. OpenSpec 文件結構說明
   - 常見 Spec 類型（如：Product Spec、System Spec、API Spec）
   - 每一種 Spec 的用途與撰寫原則
   - 好的 Spec 與壞的 Spec 範例比較

4. 使用 OpenSpec 的標準工作流程
   - 從需求想法到 Spec
   - 與 AI 互動修正 Spec 的方式
   - Spec 如何驅動設計、程式碼與測試

5. 新進同仁實作範例（重要）
   - 一個簡單系統案例（例如：使用者查詢、資料新增、批次處理或 API）
   - 從「需求描述」→「OpenSpec 文件」→「可開發規格」
   - 示範如何向 AI 詢問與優化 Spec

6. 常見錯誤與反模式（Anti-Patterns）
   - 規格寫得像程式碼
   - 規格過於抽象或過度細節化
   - 把 AI 當成自動寫 Code 工具而非 Spec 協作者

7. 導入 OpenSpec 的最佳實務（Best Practices）
   - 團隊協作方式
   - Spec Review 重點
   - 如何版本控管 Spec（搭配 Git）

8. 給新進同仁的學習建議
   - 上手順序
   - 常見卡關點
   - 如何從「會寫」進階到「寫得好」

## 產出格式
- 使用繁體中文
- 採用「教學手冊」語氣（清楚、條列、可教學）
- 可加入表格、條列清單與小結
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為:OpenSpec使用教學.md，並使用 Markdown 格式撰寫。
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 請分段回覆

## 額外加分
- 若能加入「與 AI 對話的 Prompt 範例」更佳
- 若能標註「這一段在實務中常見於銀行或大型系統」更佳
------------------------------------------------------------------------------
# BMAD-METHOD使用教學

你是一位精通 BMAD-METHOD（https://github.com/bmad-code-org/BMAD-METHOD）的資深軟體開發工程師與 AI 協作專家，
同時具備企業級系統開發、規格驅動開發（Spec-Driven Development）與新人培訓經驗。

## 【背景】
- 組織已導入 BMAD-METHOD，並使用 AI（如 ChatGPT）輔助軟體開發
- 目標讀者為「新進軟體工程師 / 系統分析師 / 專案成員」
- 讀者對 BMAD-METHOD 尚不熟悉，但具備基本軟體開發概念
- 使用情境以企業內部系統、銀行系統或大型專案為主

## 【任務】
請你產出一份「BMAD-METHOD 使用教學手冊」，內容需：
- 結構清楚、循序漸進
- 可直接作為公司內部教育訓練教材
- 結合理論、實務流程與 AI Prompt 範例
- 使用「繁體中文」
- 風格專業、清楚、偏向工程實務導向

## 【教學手冊需包含的章節】

1. BMAD-METHOD 是什麼
   - 方法論背景與設計目的
   - BMAD 與傳統開發流程（如 Waterfall / Agile / Scrum）的差異
   - 為什麼 BMAD 特別適合「AI 協作開發」

2. BMAD-METHOD 的核心概念
   - B（Business）
   - M（Model）
   - A（Architecture）
   - D（Delivery）
   - 各階段的目標、輸入、輸出（Artifacts）

3. BMAD-METHOD 整體流程說明
   - 從需求發想到交付的完整流程
   - 每個階段與 AI 的互動方式
   - 建議的文件與產出物

4. 各階段詳細教學（重點章節）
   - Business：需求澄清、問題定義、商業目標
   - Model：資料模型、業務規則、流程建模
   - Architecture：系統架構、模組切分、非功能需求
   - Delivery：實作、測試、驗收、交付

   每個階段請包含：
   - 新手該做什麼
   - 常見錯誤
   - 與 AI 協作的最佳實務

5. AI Prompt 實戰範例（非常重要）
   - 每個 BMAD 階段至少提供 2-3 個實用 Prompt
   - Prompt 要可直接複製使用
   - 清楚說明「這個 Prompt 會產出什麼」

6. BMAD-METHOD 與其他方法論比較
   - 與 Scrum / SAFe / SDD / Spec-Kit 的差異
   - 適用與不適用情境

7. 新進同仁快速上手指南
   - 第 1 週可以怎麼用 BMAD
   - 建議學習順序
   - 團隊內導入建議

8. 常見問題（FAQ）
   - BMAD 是否取代 SA / PG？
   - BMAD 是否一定要用 AI？
   - 如何在既有（Brownfield）系統中導入？

## 【輸出格式】
- 使用繁體中文
- 採用「教學手冊」語氣（清楚、條列、可教學）
- 可加入表格、條列清單與小結
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 使用 Markdown 格式，含標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出。
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為:BMAD-METHOD使用教學.md
- 請用 教學手冊風格，結構清晰，包含 章節、步驟、範例指令。適合新進同仁快速上手。
- 請分段回覆

## 額外加分
- 若能加入「與 AI 對話的 Prompt 範例」更佳
- 若能標註「這一段在實務中常見於銀行或大型系統」更佳

------------------------------------------------------------------------------
# Java 1.7 → Java 25 升版教學手冊生成 Prompt（完整版）

## 🧑‍💼 角色設定（Role）

你是一位：

- 資深 Java 系統架構師  
- Oracle Java OCP 國際認證講師  
- 熟悉大型企業系統、銀行核心系統、批次系統（Batch）、Web / API 系統  
- 熟悉 Java SE 7 ～ Java SE 25 所有重大語言與平台演進  
- 具備升版評估、風險控管、實務轉換、教育訓練設計能力  

你的任務是為「**已具 Java 1.7 基礎的開發同仁**」，設計一套 **可實際用於企業升版 + Java 認證準備** 的完整教學手冊。

## 🏗️ 讀者背景（Audience）

- 具備 Java 1.7～8 實務經驗  
- 曾開發：
  - Web / API 系統  
  - Batch / 排程系統  
  - 舊版 Java EE / Spring 專案  
- 對 Lambda、模組化、Reactive、Virtual Thread 等概念不熟或僅略懂  
- 目標：
  - 能安全升版既有系統  
  - 理解 Java 現代設計哲學  
  - 具備報考 Java OCP（新版）的能力  

## 🎯 教學目標（Objectives）

請確保教學手冊能讓讀者：

1. 理解 Java 1.7 → Java 25 的整體演進脈絡  
2. 掌握每個 LTS 與關鍵版本的核心變革  
3. 能判斷舊系統升版時的風險與處理策略  
4. 能寫出符合 Java 17+ / 21+ / 25 現代風格的程式碼  
5. 具備 Java OCP 認證所需的語言與 API 知識  

## 📘 教學手冊整體結構（請嚴格依此產出）

### 第一章：Java 平台演進總覽（1.7 → 25）

- Java 版本生命週期說明（LTS vs 非 LTS）  
- 為何企業應升級至 Java 17 / 21 / 25  
- Java 設計哲學的重大轉變  
- Java 與 JVM、生態系的角色變化  

### 第二章：Java 7 → Java 8（現代 Java 的分水嶺）

- Lambda Expression  
- Functional Interface  
- Stream API（map / filter / reduce）  
- Optional 的正確使用方式  
- Default Method  
- 實務對照：
  - Java 7 寫法 vs Java 8 寫法  
- 常見誤用與 OCP 考點  

### 第三章：Java 9 ～ Java 11（模組化與平台重整）

- Java Platform Module System（JPMS）  
- jlink / jdeps  
- 移除 Java EE 模組的影響  
- HTTP Client API  
- var（區域型別推斷）  
- TLS / Security 強化  
- 升版衝擊與因應策略  

### 第四章：Java 12 ～ Java 16（語言精煉期）

- Switch Expression（新語法）  
- Text Blocks  
- Records（Preview → 正式）  
- Pattern Matching（instanceof）  
- ZGC / Shenandoah 簡介  
- Preview Feature 使用與風險  

### 第五章：Java 17（LTS，企業升版首選）

- Java 17 作為企業基準版的理由  
- Sealed Class  
- 強封裝（Strong Encapsulation）  
- 移除與淘汰 API 清單  
- 與 Spring Boot / Jakarta EE 的相容性  

### 第六章：Java 18 ～ Java 20（為並行革命鋪路）

- Foreign Function & Memory API（演進）  
- Vector API  
- JVM 效能最佳化重點  
- 新 GC 行為觀察  

### 第七章：Java 21（LTS，Virtual Thread 時代）

- Virtual Thread（Project Loom）  
- Structured Concurrency  
- Scoped Value  
- 傳統 Thread Pool vs Virtual Thread  
- 對 Web / Batch / MQ 系統的影響  
- 實務建議（何時適合用、何時不適合）  

### 第八章：Java 22 ～ Java 25（未來 Java 的樣貌）

- Pattern Matching 完整體系  
- Record Pattern  
- Class File API  
- 最新 GC / JVM 優化  
- Java 在 Cloud-Native、AI、High Concurrency 的定位  

### 第九章：舊系統升版實務指南（企業必讀）

- Java 1.7 → 17 / 21 / 25 升版路線圖  
- 常見升版風險：
  - Unsafe API  
  - 反射  
  - ClassLoader  
  - 編碼 / TLS / 加密  
- 建議升版策略（分階段）  
- 升版 Checklist（可直接使用）  

### 第十章：Java OCP 認證對照與準備建議

- Java OCP（新版）考試範圍對照  
- 必考語言特性整理  
- 常見陷阱題解析方向  
- 建議學習與實作順序  

### 第十一章：總結與學習地圖

- Java 現代化能力成熟度模型  
- 從 Java 7 工程師 → Java 25 架構師  
- 持續學習建議與官方資源  

## ✍️ 撰寫風格要求（非常重要）

- 使用繁體中文  
- 風格：
  - 教學導向  
  - 架構師視角  
  - 搭配實務經驗說明  
- 每個重要語法或功能請提供：
  - 為何出現  
  - 解決什麼問題  
  - 舊寫法 vs 新寫法  
  - 企業實務建議  
- 程式碼請使用：
  - Java 17+ 為主  
  - 清楚註解  
  - 可直接用於教學  

## 📦 最終輸出格式

- 請以正式文件格式撰寫，章節分明，包含：
- 語法解說
- 範例程式碼
- 認證考點提醒
- 小練習題與解析
- 請產生一份完整、條理清楚的文件，並以 章節方式編排，可直接提供給新進人員使用。
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\程式語言\ 目錄下,檔名為: Java25升版教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆


-------------------------------------------------------------------------
# claude agent skills教學手冊

## 角色設定（Role）
你是一位 Claude Agent Skills 的專家，同時也是資深軟體架構師與 AI 工程顧問，
熟悉 Anthropic Claude 的 Agents & Tools 架構、Agent Skills 設計理念、
以及如何在企業級軟體開發中實際導入 Agent Skills 來輔助開發、測試與文件產出。

你熟悉以下官方資源，並以其為主要依據：
- Claude Agent Skills 官方文件
  https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic skills GitHub Repository
  https://github.com/anthropics/skills/blob/main/README.md

---

## 背景（Background）
我們目前在軟體開發流程中，開始導入 Claude Agent 與 Agent Skills，
用於協助：
- 需求與規格文件產生（PRD / SRS / Spec）
- 程式碼生成與重構
- 測試案例與測試資料產生
- 文件與教學手冊撰寫
- 重複性工程任務自動化

本教學手冊的讀者為「新進軟體工程師 / 系統分析師 / AI 導入成員」，
假設他們：
- 具備基本軟體工程概念
- 不一定熟悉 Claude Agent 或 Agent Skills
- 需要「從 0 到實務導入」的清楚指引

---

## 任務（Task）
請你產出一份【Claude Agent Skills 使用教學手冊】，內容需符合以下要求：

### 一、文件定位
- 教學性質：內部教育訓練用
- 語言：繁體中文
- 風格：專業、結構清楚、偏實務導向
- 適合直接轉為 Word / Markdown / 簡報教材

---

### 二、教學手冊必備章節（請完整產出）

#### 1️⃣ Claude Agent 與 Agent Skills 基礎概念
- 什麼是 Claude Agent
- 什麼是 Agent Skills
- Agent / Tool / Skill 的差異與關係
- 為什麼要使用 Agent Skills（解決什麼問題）

#### 2️⃣ Agent Skills 的設計理念
- Skill 的責任邊界（Single Responsibility）
- Skill 與 Prompt 的差異
- 為何 Skill 是「可重用、可組合」的能力單元
- 官方 skills repo 的設計原則說明

#### 3️⃣ 官方 Skills Repository 結構說明
- skills GitHub 專案的目錄結構
- skill 的命名慣例
- skill 定義中包含哪些關鍵元素（用途、輸入、輸出、限制）

#### 4️⃣ Agent Skills 的使用方式
- 如何在 Agent 中呼叫 Skill（概念層級說明）
- Skill 在任務流程中扮演的角色
- 單一 Skill vs 多 Skill 組合的使用情境

#### 5️⃣ 實務範例（重點章節）
請至少提供 3 個實務導向範例，例如：
- 「需求文件產生 Skill」
- 「程式碼 Review / 重構 Skill」
- 「測試案例產生 Skill」
每個範例需包含：
- 使用情境說明
- Skill 的職責描述
- Agent 如何搭配 Skill 運作
- 實際 Prompt / Skill 呼叫示意（文字即可）

#### 6️⃣ 新手常見錯誤與最佳實務
- Skill 設計過大 / 過小的問題
- 把 Skill 當成一次性 Prompt 的錯誤用法
- 如何讓 Skill 更容易被重用
- 如何讓 Agent 行為更穩定

#### 7️⃣ 團隊導入建議
- 適合先從哪些類型的 Skill 開始
- 如何建立內部 Skill Library
- 如何與既有開發流程（如需求 → 開發 → 測試）整合
- 導入 Agent Skills 的成熟度階段建議（初階 / 中階 / 進階）

---

### 三、額外要求
- 多使用條列式、表格化說明（文字描述即可）
- 概念與實務需平衡，不要只講理論
- 避免過度行銷式語言，請偏工程實作觀點
- 內容需可直接交給新進同仁閱讀理解

---

## 輸出格式（Output）
- 使用 Markdown
- 標題層級清楚（# / ## / ###）
- 可直接作為《Claude Agent Skills 教學手冊》初版內容
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\AI開發\ 目錄下,檔名為: "claude agent skills教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-----------------------------------------------------------------

# 任務：產生《Claude Code使用教學手冊（新進同仁版）》
## 你的角色設定
你是一位 **Claude Code 專家與資深軟體架構師**，具備以下經驗：
- 熟悉 Anthropic Claude 平台與 Claude Code 的設計理念
- 實際使用 Claude Code 協助企業級軟體開發（Web / Batch / API / Spec-driven）
- 能將複雜概念轉換為「新進工程師也能理解並實作」的教學內容
- 熟悉企業內部 SDLC、程式碼審查、資安與合規需求
## 背景說明
公司目前導入 **Claude Code** 作為 AI 協作開發工具，應用情境包含：
- 規格理解與補強（PRD / SRS / Spec）
- 程式碼產生、重構與解說
- 單元測試、測試案例產生
- Code Review 輔助
- Batch / API / 前後端開發輔助
- 新進人員 Onboarding 加速
本手冊的讀者為：
- 新進軟體工程師（PG / SA / Tech Lead 初階）
- 具備基本程式設計能力，但 **尚未系統性使用過 Claude Code**
## 教學手冊產出目標
請產出一份 **可作為公司內部正式文件** 的教學手冊，需具備：
- 清楚章節結構
- 實務導向（可直接照做）
- 大量 Prompt 範例
- 「怎麼用、什麼時候用、怎麼用得好」
- 明確區分「新手常犯錯誤」與「最佳實務」
## 教學手冊建議章節結構（請完整產出）
### 第 1 章：Claude Code 是什麼？
- Claude Code 的定位（不是取代工程師，而是協作）
- 與一般聊天式 AI 的差異
- 適合與不適合的使用情境
- Claude Code 在企業開發流程中的角色
### 第 2 章：Claude Code 的基本操作觀念
- Prompt ≠ 問問題
- 好 Prompt 的核心結構（角色 / 背景 / 任務 / 輸出格式）
- 單輪 vs 多輪對話策略
- 如何逐步「收斂」出可用結果
### 第 3 章：新進工程師必學的 Prompt 範本
請提供「可直接複製使用」的 Prompt，例如：
- 程式碼解讀 Prompt
- 新功能開發 Prompt
- 舊系統重構 Prompt
- Bug 分析 Prompt
- 單元測試產生 Prompt
- Code Review Prompt
- 規格補齊 Prompt
### 第 4 章：Claude Code 在實務開發中的典型流程
- 從需求文字 → 程式碼
- 從舊程式碼 → 可維護設計
- 從「我看不懂」→「我能修改」
- 搭配 Git / PR / Review 的使用方式
### 第 5 章：常見錯誤與 Anti-Pattern
- 問太籠統
- 一次丟太多責任
- 沒有限制輸出格式
- 盲目相信 AI 結果
- 沒做人工驗證
### 第 6 章：Claude Code 使用最佳實務（Best Practices）
- Prompt 模組化
- 對話紀錄如何保存
- 與團隊共用 Prompt 的方式
- 什麼情況「不該用 Claude Code」
### 第 7 章：企業內部使用注意事項
- 資安與機敏資料原則
- 原始碼與客戶資料保護
- 法遵與稽核觀點
- AI 產出責任歸屬說明
### 第 8 章：進階應用（選讀）
- Spec-Driven Development（SDD）
- 將 Claude Code 當成虛擬 Pair Programmer
- 長任務拆解技巧
- Prompt Chain 與角色切換
## 撰寫風格與格式要求
- 使用 **繁體中文**
- 語氣：專業、務實、內部教學文件風格
- 每個章節搭配「重點摘要」
- Prompt 範例請使用 Markdown code block
- 適合轉成 Word / Confluence / Notion 文件
## 最終輸出
- 請直接輸出完整《Claude Code 使用教學手冊（新進同仁版）》內容，不要只給大綱。
使用 Markdown
- 標題層級清楚（# / ## / ###）
- 可直接作為《Claude code 教學手冊》初版內容
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\AI開發\ 目錄下,檔名為: "claude code教學手冊(新手版).md"，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------------
# 產生《Claude Code使用教學手冊（資深同仁版）》
## 你的角色設定
你是一位「Claude Code 使用專家」與「資深軟體架構師」，  
具備多年企業級系統開發經驗，熟悉 AI Assisted Development、LLM Coding Workflow、Spec-driven Development 與企業內部開發規範。

請你根據以下背景與需求，產出一份【Claude Code 教學手冊】。

────────────────────
## 背景說明
- 組織已開始導入 Claude Code 作為日常軟體開發輔助工具
- 使用者對象為「資深工程師 / Tech Lead / 系統分析師 / 架構師」
- 讀者已具備完整的程式設計、系統設計、Git、CI/CD、測試與文件經驗
- 教學重點不是「怎麼用介面」，而是：
  - 如何把 Claude Code 融入專業開發流程
  - 如何寫出高品質 Prompt
  - 如何避免 AI 產生低品質或危險程式碼
  - 如何讓 AI 成為「架構與實作的加速器」

────────────────────
## 【教學手冊目標】
1. 協助資深同仁正確理解 Claude Code 的定位與能力邊界
2. 建立「AI 協作式開發」的正確心法
3. 教會如何在實務中：
   - 重構舊系統
   - 設計新模組
   - 撰寫高品質程式碼
   - 補齊測試與文件
4. 提供可複製、可落地的 Prompt 範本

────────────────────
## 【內容結構需求】
請至少包含以下章節（可自行優化標題）：

1️⃣ Claude Code 是什麼？（給資深工程師的視角）
- Claude Code 與傳統 Copilot / ChatGPT Coding 的差異
- 適合用來做什麼？不適合做什麼？
- 在企業環境中的合理定位

2️⃣ 資深工程師使用 Claude Code 的正確心法
- 把 AI 當成「資深 Pair Programmer」而非新人工具
- 為什麼「規格比程式碼更重要」
- Prompt 即設計文件的延伸

3️⃣ 高品質 Prompt 設計原則（重點章節）
- 好 Prompt vs 壞 Prompt 對照
- 必備元素：
  - 角色
  - 背景
  - 技術約束
  - 非功能需求
  - 輸出格式
- 常見錯誤 Prompt 範例與改寫示範

4️⃣ Claude Code 在實務開發流程中的應用
- 需求釐清 / PRD 補強
- 架構設計與技術選型
- 程式碼生成與重構
- 測試案例補齊
- 技術文件與 README 生成

5️⃣ 企業級實戰範例
- 範例一：請 Claude Code 協助重構 Legacy Code
- 範例二：請 Claude Code 根據規格產生模組骨架
- 範例三：請 Claude Code 產生測試與安全檢查建議
（每個範例請包含「Prompt → AI 輸出 → 專家講評」）

6️⃣ 風險、限制與最佳實踐
- AI 可能產生的風險（錯誤邏輯、安全性、過度自信）
- 如何做 Code Review 與 AI Output Review
- 在銀行 / 企業內部的安全使用原則

7️⃣ 團隊導入建議
- 適合哪些角色優先使用
- Claude Code 與現有開發流程（Git / CI / Review）的整合方式
- 建議的內部使用規範（Do / Don't）

────────────────────
【輸出格式要求】
- 使用 Markdown（md）格式
- 條列清楚、段落分明
- 技術用語精準、偏企業級
- 可直接作為「內部正式教學文件」

────────────────────
【寫作風格】
- 專業、務實、偏架構與實戰
- 避免行銷語氣
- 適合給「不需要被教寫 for-loop 的人」閱讀
## 最終輸出
- 請直接輸出完整《Claude Code 使用教學手冊（資深同仁版）》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 可直接作為《Claude code 教學手冊》初版內容
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\AI開發\ 目錄下,檔名為: "claude code教學手冊(資深同仁版).md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-----------------------------------------------------------------------
# Anthropic Model Context Protocol (MCP) 教學手冊生成 Prompt

## 角色定義
你是一位資深的軟體開發工程師和技術文件撰寫專家，專精於 Anthropic Model Context Protocol (MCP) 的實作與應用。你需要為資深技術同仁撰寫一份完整且實用的 MCP 教學手冊。

## 目標讀者
- 資深軟體開發工程師
- 具備 API 開發經驗
- 熟悉 JSON-RPC 協議
- 需要快速上手 MCP 並應用於實際專案

## 教學手冊結構要求

### 第一章：MCP 概述與核心概念
1. **什麼是 MCP？**
   - MCP 的定義與核心價值
   - 與 USB-C 類比的解釋
   - MCP 在 AI 應用生態系統中的定位

2. **為什麼需要 MCP？**
   - 解決的核心問題
   - 對開發者、AI 應用、終端用戶的價值
   - 實際應用場景範例

3. **MCP 架構概覽**
   - Client-Server 架構說明
   - MCP Host、Client、Server 的角色與關係
   - 本地伺服器 vs 遠端伺服器的差異

### 第二章：MCP 技術架構深度解析

1. **分層架構**
   - 資料層（Data Layer）詳解
   - 傳輸層（Transport Layer）詳解
   - 層與層之間的互動關係

2. **資料層協議（Data Layer Protocol）**
   - JSON-RPC 2.0 基礎
   - 生命週期管理（Lifecycle Management）
   - 能力協商機制（Capability Negotiation）

3. **MCP 核心原語（Primitives）**
   
   **Server 端原語：**
   - **Tools**：可執行函數的定義與實作
   - **Resources**：資料來源的設計與使用
   - **Prompts**：可重用模板的建立與應用
   
   **Client 端原語：**
   - **Sampling**：語言模型完成請求
   - **Elicitation**：用戶互動與確認機制
   - **Logging**：除錯與監控日誌
   
   **通用原語：**
   - **Tasks**（實驗性）：持久化執行包裝器

4. **通知機制（Notifications）**
   - 即時更新的設計
   - 工具列表變更通知
   - 事件驅動架構

### 第三章：傳輸層深度解析

1. **STDIO Transport**
   - 適用場景：本地進程通訊
   - 配置方式與範例
   - 效能特性與限制

2. **Streamable HTTP Transport**
   - 適用場景：遠端伺服器通訊
   - HTTP POST 與 Server-Sent Events
   - 認證機制（Bearer Token、API Keys、OAuth）
   - 安全性最佳實踐

### 第四章：實戰開發指南

1. **開發環境設置**
   - SDK 選擇與安裝
   - 開發工具介紹（MCP Inspector）
   - 專案結構建議

2. **開發 MCP Server**
   
   **基礎範例：**
   - 最簡單的 MCP Server 實作
   - 註冊與初始化流程
   - 處理客戶端請求
   
   **進階範例：**
   - 實作 Tools（以資料庫查詢為例）
   - 實作 Resources（以檔案系統為例）
   - 實作 Prompts（以互動模板為例）
   - 動態工具列表管理
   - 發送通知

3. **開發 MCP Client**
   
   **基礎範例：**
   - 連接到 MCP Server
   - 初始化與能力協商
   - 探索可用工具
   
   **進階範例：**
   - 執行工具並處理回應
   - 處理伺服器通知
   - 錯誤處理與重試機制
   - 多伺服器管理

4. **整合到 AI 應用**
   - Claude Desktop 整合範例
   - Claude Code 整合範例
   - 自訂 AI 應用整合流程
   - 工具註冊與動態更新

### 第五章：完整實戰範例

請提供至少 3 個完整的端到端範例：

1. **範例一：檔案系統 MCP Server**
   - 功能：提供檔案讀寫、搜尋功能
   - 包含完整程式碼
   - 測試與除錯步驟

2. **範例二：資料庫查詢 MCP Server**
   - 功能：提供資料庫 schema 查詢、SQL 執行
   - 包含完整程式碼
   - 安全性考量

3. **範例三：API 整合 MCP Server**
   - 功能：整合外部 API（如 GitHub、Notion）
   - 包含認證處理
   - 錯誤處理與重試

### 第六章：最佳實踐與設計模式

1. **MCP Server 設計原則**
   - 單一職責原則
   - 工具命名規範
   - 參數設計與驗證
   - 錯誤處理標準

2. **效能優化**
   - 連接池管理
   - 快取策略
   - 批次處理
   - 非同步操作

3. **安全性考量**
   - 認證與授權
   - 輸入驗證
   - 敏感資料處理
   - 速率限制

4. **測試策略**
   - 單元測試
   - 整合測試
   - 使用 MCP Inspector 進行測試
   - 模擬與 Mock

### 第七章：進階主題

1. **Tasks 實驗性功能**
   - 延遲結果檢索
   - 狀態追蹤
   - 適用場景

2. **自訂傳輸層**
   - 何時需要自訂傳輸層
   - 實作指南
   - 注意事項

3. **多語言 SDK 比較**
   - Python SDK 特性
   - TypeScript SDK 特性
   - 其他語言支援

4. **偵錯與監控**
   - 日誌記錄最佳實踐
   - 效能監控
   - 錯誤追蹤

### 第八章：疑難排解

1. **常見問題與解決方案**
   - 連接問題
   - 初始化失敗
   - 工具執行錯誤
   - 通知未收到

2. **除錯技巧**
   - 使用 MCP Inspector
   - 日誌分析
   - 網路追蹤

3. **效能問題診斷**
   - 識別瓶頸
   - 優化策略

### 第九章：實際案例研究

請包含至少 2 個真實世界的案例：

1. **企業內部工具整合**
   - 情境描述
   - 解決方案設計
   - 實作細節
   - 經驗教訓

2. **產品功能增強**
   - 情境描述
   - 架構設計
   - 擴展性考量
   - 成效評估

### 第十章：資源與參考

1. **官方資源**
   - 官方文件連結
   - GitHub 儲存庫
   - 規範文件

2. **社群資源**
   - 範例專案
   - 開源伺服器實作
   - 社群討論區

3. **學習路徑建議**
   - 初學者路徑
   - 進階開發者路徑
   - 持續學習資源

## 輸出格式要求

1. **文件格式**：Markdown 格式，清晰的階層結構
2. **程式碼範例**：包含完整可執行的程式碼，附帶註解
3. **圖表說明**：使用 Mermaid 圖表說明架構和流程
4. **實用性導向**：每個概念都要有對應的實作範例
5. **中文撰寫**：使用繁體中文，技術術語可保留英文並加註說明

## 特殊要求

1. **實戰導向**：著重於可立即應用的知識和程式碼
2. **完整性**：每個範例都要能獨立執行
3. **深度與廣度並重**：既要涵蓋基礎概念，也要探討進階主題
4. **最佳實踐**：明確指出建議做法和應避免的陷阱
5. **版本資訊**：明確標註使用的 MCP 版本和相關工具版本

## 參考資料
- 官方文件：https://modelcontextprotocol.io/docs/getting-started/intro
- 架構說明：https://modelcontextprotocol.io/docs/learn/architecture
- GitHub：https://github.com/modelcontextprotocol
- 規範文件：https://modelcontextprotocol.io/specification/2025-11-25

## 最終輸出
- 請直接輸出完整《Anthropic Model Context Protocol (MCP) 教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 可直接作為《Claude code 教學手冊》初版內容
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\AI開發\ 目錄下,檔名為: "Anthropic Model Context Protocol (MCP) 教學手冊".md"，並使用 Markdown 格式撰寫。
- 請分段回覆
---

請根據以上要求，生成一份完整、實用、專業的 MCP 教學手冊。
-----------------------------------------------------------------------
# Claude Code 生態圈教學手冊生成 Prompt

## 角色設定
你是一位精通 Claude Code 的技術文件撰寫專家和資深軟體開發工程師,擁有豐富的 AI 輔助開發經驗。

## 任務目標
為資深軟體工程師團隊撰寫一份完整且深入的「Claude Code 生態圈教學手冊」,涵蓋所有擴充功能與最佳實踐。

## 手冊結構要求

### 第一部分:基礎概念 (Foundation)
1. **Claude Code 簡介**
   - 產品定位與核心價值
   - 與傳統 IDE 的差異
   - 適用場景與限制
   - 安裝與環境配置

2. **核心架構概覽**
   - 系統架構圖
   - 各組件之間的關係
   - 資料流與執行流程

### 第二部分:核心功能詳解

#### 2.1 Subagents (子代理)
- **概念說明**:什麼是 Subagents 及其設計理念
- **使用場景**:
  - 任務分解與並行處理
  - 專業領域分工(前端/後端/測試等)
  - 複雜專案的模組化管理
- **實作範例**:
  - 建立自訂 Subagent 的完整流程
  - 配置檔案結構與參數說明
  - 多個 Subagents 協作的實戰案例
- **進階技巧**:
  - Subagent 的優先級設定
  - 錯誤處理與容錯機制
  - 效能優化建議

#### 2.2 Skills (技能系統)
- **Skills 架構**:
  - Skills 的定義與分類
  - 內建 Skills vs 自訂 Skills
  - Skills 的生命週期
- **開發自訂 Skills**:
  - Skill 開發框架說明
  - API 介面定義
  - 輸入/輸出格式規範
- **實用 Skills 範例**:
  - 程式碼審查 Skill
  - 自動化測試生成 Skill
  - 文件生成 Skill
  - 重構建議 Skill
- **Skills 管理**:
  - 版本控制策略
  - Skills 市場與分享機制
  - 安全性考量

#### 2.3 Plugins (插件系統)
- **Plugin 生態系統**:
  - 官方 Plugins 目錄
  - 第三方 Plugin 資源
  - Plugin 安全性檢核
- **Plugin 開發指南**:
  - 開發環境設置
  - Plugin 架構與接口
  - 事件監聽與觸發機制
  - 與 IDE 的整合方式
- **常用 Plugins 推薦**:
  - Git 整合插件
  - 資料庫管理插件
  - API 測試插件
  - 部署自動化插件
- **Plugin 最佳實踐**:
  - 效能優化
  - 記憶體管理
  - 錯誤處理

#### 2.4 Hooks (鉤子機制)
- **Hooks 系統概述**:
  - 事件驅動架構
  - 可用的 Hook 類型清單
  - Hook 的執行順序
- **Hook 類別詳解**:
  - Pre-execution Hooks(執行前)
  - Post-execution Hooks(執行後)
  - Error Hooks(錯誤處理)
  - Lifecycle Hooks(生命週期)
- **實作案例**:
  - 程式碼品質檢查 Hook
  - 自動備份 Hook
  - 日誌記錄 Hook
  - 通知整合 Hook
- **進階應用**:
  - 條件式 Hook 觸發
  - Hook 鏈式組合
  - 非同步 Hook 處理

#### 2.5 MCP (Model Context Protocol)
- **MCP 核心概念**:
  - 什麼是 MCP 及其重要性
  - Context 管理策略
  - Token 使用優化
- **MCP Server 架構**:
  - Server 的設置與配置
  - 自訂 Context Providers
  - 多 Server 協調機制
- **Context 優化技巧**:
  - 動態 Context 選擇
  - Context 緩存策略
  - 相關性評分機制
- **MCP 實戰應用**:
  - 大型專案的 Context 管理
  - 跨檔案參考優化
  - 歷史對話利用
- **整合範例**:
  - 連接外部知識庫
  - API 文件整合
  - 企業內部資源接入

### 第三部分:整合與最佳實踐

#### 3.1 生態圈組件整合
- **完整工作流範例**:
  - 需求分析 → 設計 → 開發 → 測試 → 部署的完整流程
  - 各組件在流程中的角色
- **組件協作模式**:
  - Subagents + Skills 的組合應用
  - Hooks + MCP 的進階整合
  - Plugins 的生態協調

#### 3.2 團隊協作策略
- **配置標準化**:
  - 團隊共享配置模板
  - 版本控制最佳實踐
- **協作流程設計**:
  - Code Review 流程優化
  - 知識共享機制
- **權限與安全**:
  - 敏感資訊保護
  - API Key 管理

#### 3.3 效能優化
- **Token 使用優化**
- **回應時間改善**
- **批次處理策略**
- **快取機制應用**

#### 3.4 疑難排解
- **常見問題 FAQ**
- **錯誤碼對照表**
- **Debug 技巧**
- **社群資源索引**

### 第四部分:進階主題

#### 4.1 企業級應用
- 私有部署方案
- 企業知識庫整合
- 合規性考量
- 審計與日誌

#### 4.2 CI/CD 整合
- GitHub Actions 整合
- GitLab CI 配置
- Jenkins Pipeline 設定

#### 4.3 客製化開發
- 深度客製化場景
- API 擴展開發
- 內部工具鏈整合

### 第五部分:附錄
- **完整 API 參考**
- **配置檔案範本**
- **術語表**
- **學習資源推薦**
- **社群貢獻指南**

---

## 撰寫要求

### 內容品質
1. **深度與廣度平衡**:既要有理論深度,又要有實踐廣度
2. **實用性優先**:每個概念都要有可執行的程式碼範例
3. **循序漸進**:從基礎到進階,適合不同層級的讀者
4. **實戰導向**:提供真實專案場景的應用案例

### 格式規範
1. **使用清晰的 Markdown 格式**
2. **程式碼範例需完整可執行,包含必要的註解**
3. **圖表說明(用 Mermaid 語法描述架構圖)**
4. **重點資訊使用特別標註(✨ 最佳實踐、⚠️ 注意事項、💡 小技巧)**

### 程式碼範例要求
- 使用多種語言示範(TypeScript/JavaScript,Java 等)
- 包含完整的錯誤處理
- 註解要說明「為什麼」而非「是什麼」
- 提供可直接複製使用的完整範例

### 特別強調
- **版本資訊**:標註功能的最低版本需求
- **效能提示**:說明各功能的效能影響
- **安全警告**:明確標示安全相關的注意事項
- **社群實踐**:引用社群的最佳實踐案例

## 輸出格式
請以 Markdown 格式輸出完整手冊,並確保:
- 目錄結構清晰,方便跳轉
- 每個章節獨立完整,可單獨閱讀
- 提供快速參考(Quick Reference)章節
- 包含實用的速查表(Cheat Sheet)


## 參考資料
- 官方文件: https://code.claude.com/docs/en/overview
- 請搜尋最新的官方文件和社群最佳實踐

## 最終輸出
- 請直接輸出完整《Claude Code 生態圈教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 可直接作為《Claude code 教學手冊》初版內容
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\AI開發\ 目錄下,檔名為: "Claude Code生態圈教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆



請開始撰寫這份完整的 Claude Code 生態圈教學手冊。
--------------------------------------------------------------
# github copilot 生態圏教學手冊 
## 參考網站:  https://docs.github.com/en/copilot
## 角色設定 - 你是一位使用github copilot的專家與資深軟體開發工程師 
## 背景 - 目前使用github copilot透過AI 來協助軟體開發 
## 任務說明 需要產生github copilot生態圏教學手冊,給資深同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
------------------------------------------------------------------------------
# github copilot生態圏教學手冊 
## 角色設定（Role）
你是一位「GitHub Copilot 生態圈專家」與「大型企業資深軟體架構師」，具備以下背景：
- 10+ 年企業級系統開發經驗
- 熟悉 GitHub Copilot、Copilot Chat、Copilot for CLI、Copilot for PR、Copilot Workspace 等完整生態圈
- 熟悉 Java / Spring Boot、JavaScript / TypeScript、Python、CI/CD、Cloud Native、DevSecOps
- 熟悉企業資安、SSDLC、OWASP Top 10、Code Review 與合規要求
- 曾實際在大型組織導入 AI-assisted development

---

## 背景說明（Context）
組織目前已正式導入 GitHub Copilot，使用對象為：
- 資深工程師
- Tech Lead / Architect
- 需要對程式碼品質、資安與可維運性負責的人員

此教學手冊 **不是給新手**，而是：
- 幫助資深同仁「正確、有效、安全地」使用 Copilot
- 將 Copilot 納入既有開發流程（SSDLC / CI/CD / Code Review）
- 避免誤用、過度依賴、資安與法遵風險
## 任務目標（Objective）
請產出一份 **《GitHub Copilot 生態圈教學手冊》**，需符合以下條件：
1. **內容深度：資深工程師等級**
   - 不解釋基礎 Git / IDE 操作
   - 重點在「思維轉換、使用策略、架構層級應用」
2. **完整涵蓋 GitHub Copilot 生態圈**
   - GitHub Copilot（Inline completion）
   - Copilot Chat（IDE / GitHub）
   - Copilot for Pull Request / Code Review
   - Copilot for CLI
   - Copilot Workspace（若適用）
   - 與 GitHub 平台（Issues / PR / Actions）的整合關係
3. **強調企業級實務**
   - 企業開發流程中的使用時機
   - 與 Code Review、資安掃描、單元測試的關係
   - 如何避免 AI 產出不安全或不合規程式碼
4. **必須包含「Prompt Engineering」章節**
   - Inline 註解 Prompt 寫法
   - Copilot Chat 對話範例
   - Bad Prompt vs Good Prompt 對照
   - 適合資深工程師的 Prompt Pattern
5. **必須包含「反模式（Anti-pattern）」**
   - 常見錯誤用法
   - 過度信任 Copilot 的風險
   - Copilot 不適合做的事情
6. **必須包含「導入建議與治理（Governance）」**
   - 團隊使用規範
   - Code Review 要點
   - 資安與法遵注意事項
   - Copilot 在 SSDLC 各階段的定位
## 教學手冊結構要求（Structure）
請至少包含以下章節（可自行擴充）：
1. GitHub Copilot 生態圈全貌總覽
2. Copilot 與「資深工程師角色」的正確關係
3. Copilot 在實際開發流程中的使用時機
4. Copilot Prompt Engineering（重點章節）
5. Copilot + Code Review + Testing 最佳實務
6. 資安、法遵與風險控管
7. 常見誤用與反模式
8. 團隊導入與治理建議
9. 進階應用案例（如重構、Batch、API、架構輔助）
10. 總結：如何把 Copilot 變成「資深工程師的放大器」
## 輸出格式（Output Format）
- 使用 **Markdown（.md）**
- 適合直接轉成：
  - 內部 Wiki
  - 教學手冊
  - 投影片內容來源
- 範例、Prompt、程式碼請使用 code block
- 使用繁體中文（台灣用語）
- 請直接輸出完整《github copilot生態圈教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 可直接作為《github copilot教學手冊》初版內容
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合初入行的開發人員閱讀,合新進同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教寫\AI開發\ 目錄下,檔名為: "github copilot生態圈教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

## 品質要求（Quality Bar）
- 不可流於行銷文宣
- 需具備實戰深度與可操作性
- 語氣專業、清楚、有條理
- 適合在「企業內部教育訓練」使用

## 開始產生教學手冊
請依上述條件，直接產出完整的《GitHub Copilot生態圈教學手冊》。





-----------------------------------------------------------------------
# 渣打工項追蹤_20260101.xlsx 專案進度統統

## 角色你是一個excel專案, 同時也是專案的PM, 你會將WBS寫在excel 中,用它來控制專案進度

## tab 定義 
- 專案統計 tab 其中有 B2 為基準日, 第二欄為title , 欄位有:A2:項次	B2:專案代碼	C2:專案名稱	D2:預計完成百分比	E2:實際完成百分比	F2:燈號	G2:議題	H2:action 等欄位

- 台灣假日2025 tab A欄放假日日期欄,有title,資料由A2開使放
- 台灣假日2026 tab A欄放假日日期欄,有title,資料由A2開使放
- 台灣假日2027(暫定) tab  A欄放假日日期欄,有title,資料由A2開使放

- 工項追蹤 tab, 欄位說明 A1:控制項目	B1:項次	C1:專案代碼	D1:專案名稱	E1:工項	F1:預計開始	G1:預計完成	H1:預計完成百分比	I1:實際開始	J1:實際完成	K1:實際完成百分比	L1:負責人	M1:落後原因/追趕方式/預計達標日	N1其他說明
- A1:控制項目 中 P:大項, T: 為P的子項 
- F1:預計開始	G1:預計完成	由規劃規人員手動填入
- H1:預計完成百分比	: 必需依專案統計 tab 其中有 B2 為基準日, 由F1:預計開始	G1:預計完成算出,完成百分比, 同時依台灣假日2025,台灣假日2026 ,台灣假日2027(暫定) tab 扣除假日,當基準日變後會重新計算
- 每個子項算完,在累算回它的大項
- 在把每個專案的統合寫回專案統計tab,的D2:預計完成百分比	E2:實際完成百分比
- 專案統計tab D2:預計完成百分比 小於 E2:實際完成百分比 則 F2:燈號 為藍色, 
- 專案統計tab D2:預計完成百分比 大於 E2:實際完成百分比 10% 則F2:燈號 為黃色,需人工寫入G2:議題	H2:action 等欄位
- 專案統計tab D2:預計完成百分比 大於 E2:實際完成百分比 20% 則F2:燈號 為紅色,,需人工寫入G2:議題	H2:action 等欄位
- K1:實際完成百分比由人工填入, 系統必需計算回大項
- 若有空值則不計算
-----------------------------------------------------------------------
# 微前端教學手冊 

## 微前端 (Micro-Frontend) 是一種將大型前端應用拆解成多個獨立、可部署的小型前端應用（微應用），以實現技術棧自由、團隊獨立開發與部署的架構模式，主要解決單體應用複雜度高、開發效率低下的問題。設計上常使用一個父應用（基座）來整合子應用，技術應用包含 Webpack Module Federation 實現模組共享、Router 路由管理、Isolation 隔離技術，並可根據需求選擇不同框架（React, Vue）實現跨技術棧整合。 
## 角色設定 - 你是一位微前端 (Micro-Frontend)的專家與資深軟體開發工程師 
## 背景 - 目前使用微前端透過AI 來協助軟體開發 
## 任務說明 需要產生微前端教學手冊,給資深同仁使用,請先產生prompt 來請AI 幫我產生教學手冊

------------------------------------------------------------------
# 微前端教學手冊
## 角色設定
你是一位微前端（Micro-Frontend）架構專家與資深前端/全端軟體工程師，
具備以下實務經驗：
- 曾在大型企業或金融級系統導入微前端架構
- 熟悉 Monorepo / Multirepo 架構取捨
- 熟悉 Webpack Module Federation、Vite Federation
- 熟悉 Vue / React /Angular 混合微前端實戰
- 熟悉企業級 CI/CD、權限控管、資安與效能議題

## 背景說明
本文件用於企業內部「資深工程師」教育訓練，
讀者假設：
- 已具備前端工程基礎（Vue / React / Angular/ TypeScript）
- 了解 SPA、Router、Build Tool 基本原理
- 曾參與中大型系統開發

目標不是入門教學，而是：
👉 幫助資深工程師「正確設計、落地、治理微前端架構」

## 任務說明
請產生一份【微前端（Micro-Frontend）教學手冊】，需符合以下要求：

### 一、內容深度要求
- 不要寫成新手教學或名詞解釋堆砌
- 著重「為什麼要這樣設計」、「踩過哪些坑」、「企業級最佳實務」
- 每個技術選型都需說明：
  - 適用情境
  - 不適用情境
  - 常見誤區

### 二、教學手冊結構（必須完整涵蓋）
1. 微前端的核心價值與真正要解決的問題
   - 什麼情況「不該用微前端」
   - 微前端 vs 單體前端 vs Monorepo

2. 微前端主流架構模式比較
   - 基座（Shell / Container）模式
   - Runtime Integration vs Build-time Integration
   - iframe / Web Components / Module Federation 比較

3. Module Federation 深度解析
   - 基本運作原理（Host / Remote）
   - Shared Library 設計策略
   - 版本衝突與依賴治理
   - 與 Vite / Webpack 的差異

4. 路由與狀態管理設計
   - 全域 Router vs 子應用 Router
   - 狀態共享邊界（哪些該共享，哪些不該）
   - Event Bus / Global Store 的使用準則

5. 隔離與安全性設計
   - CSS / JS 隔離策略
   - 微前端下的資安風險
   - 權限、Token、SSO 整合模式

6. CI/CD 與部署策略
   - 子應用獨立部署
   - 版本相容性控管
   - 灰度發布與回滾策略

7. 效能與可維運性
   - 首屏載入優化
   - 過度拆分的反效果
   - Monitoring / Logging 建議

8. AI 輔助微前端開發實務
   - 如何用 AI 產生子應用模板
   - 用 AI Review 微前端架構設計
   - 用 AI 協助 Dependency / 風險分析

### 三、實務導向要求
- 請加入「實戰經驗總結」章節
- 請列出至少 10 個「企業導入微前端常見失敗原因」
- 適合用於內部技術分享或新架構導入 Workshop

### 四、輸出格式
- ## 最終輸出
- 請直接輸出完整《微前端教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- - 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: "微前端教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
---------------------------------------------------------------
# 期望目標
## Metrics visualization
### Prometheus
### Grafana

## Logs Visualization
### Logstash
### Elasticsearch
### Kibana

## Queue Management interface
### Distributed Messaging

## Load Balancet
## Distributed Cache
------------------------------------------------------------------
# Metrics visualization手冊 
## Metrics visualization使用Prometheus與Grafana。 
## 角色設定 - 你是Metrics visualization的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Metrics visualization 透過AI 來協助軟體開發 
## 任務說明 需要產生Metrics visualization教學手冊,給資深同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-----------------------------------------------------------------------------------------------
# 任務：產生 Metrics Visualization 教學手冊（Prometheus + Grafana）
## 角色設定
你是一位 Metrics Visualization 與 Observability 領域的專家，
同時也是資深軟體架構師與資深後端開發工程師，
具備大型分散式系統、微服務架構、金融級系統（高可用、高可觀測性）的實戰經驗。
## 目標讀者
- 資深後端工程師
- 系統架構師
- SRE / DevOps 工程師
- 對「可觀測性（Observability）」已有基礎，但希望系統化深化的人員

**假設讀者已熟悉：**
- Linux / Container / Kubernetes（概念層級即可）
- RESTful API、微服務架構
- 基本系統監控概念（CPU / Memory / Latency）

## 背景說明
目前團隊使用 AI 協助軟體開發與系統設計，
希望透過 Metrics Visualization（Prometheus + Grafana）
建立「可量化、可預測、可回饋」的系統觀測能力，
並能支援：
- 架構決策
- 效能瓶頸分析
- SLA / SLO 管理
- 事故回溯（Postmortem）
- AI 輔助診斷與預警

## 教學手冊撰寫要求

### 1️⃣ 教學定位
- **不是入門手冊**
- 重點放在「設計思維、實務經驗、踩雷提醒」
- 解釋「為什麼要這樣設計」，而不是只說「怎麼做」

### 2️⃣ 技術範圍（必須涵蓋）
#### Metrics 與 Observability 基礎
- Metrics vs Logs vs Traces（以架構視角解釋）
- 為什麼 Metrics 是「第一層防線」
- RED / USE / Golden Signals 模型
- Metrics 過度蒐集的反模式（Anti-pattern）

#### Prometheus（深入但務實）
- Prometheus 架構與資料流
- Pull Model 的設計哲學
- Target / Job / Instance 設計原則
- Label 設計 Best Practices（避免 Cardinality Explosion）
- 常見 Exporter 類型（Node / JVM / App / DB）
- Recording Rules 與 Alert Rules 的設計思維
- PromQL 思考模型（不是語法速查）

#### Grafana（決策層與視覺層）
- Dashboard 設計的「故事線」概念
- 不同角色的 Dashboard 設計（Dev / Ops / Manager）
- 指標選擇與視覺化類型對應關係
- Anti-pattern Dashboard 範例
- Grafana 與 Prometheus 的責任邊界

#### Metrics 與架構決策
- 如何用 Metrics 驗證架構假設
- Scaling / Bottleneck / Capacity Planning
- SLA / SLO / Error Budget 與 Metrics 的關係
- Metrics 如何影響系統設計而不是事後補救

#### AI 輔助 Metrics 分析
- 適合交給 AI 分析的 Metrics 類型
- Prompt 設計範例（讓 AI 幫你解讀 PromQL / Dashboard）
- AI 在 Metrics 分析的限制與風險
- 人與 AI 的責任分工

### 3️⃣ 文件結構要求
- 使用 **Markdown**
- 有清楚的章節、標題、條列
- 適度加入：
  - 架構示意說明（文字描述即可）
  - 真實世界情境（如：流量暴增、效能劣化）
  - 設計決策的 trade-off

### 4️⃣ 風格要求
- 專業、務實、不說教
- 偏向「內部技術手冊」
- 可直接拿來做內訓或技術分享
- 適度使用表格與重點整理

## 產出結果
- 請產出一份 **完整的《Metrics Visualization 教學手冊（Prometheus + Grafana）》**，
- 適合提供給資深工程師閱讀與實作。
- 請直接輸出完整《Metrics Visualization 教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Metrics Visualization 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
-----------------------------------------------------------------
# Logs Visualization教學手冊 
## Logs Visualization使用Logstash, Elasticsearch ,Kibana。 
## 角色設定 - 你是Logs Visualization的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Logs Visualization透過AI 來協助軟體開發 
## 任務說明 需要產生Logs Visualization教學手冊,給資深同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-----------------------------------------------------------------
# 任務：產生 Logs Visualization（ELK Stack）資深教學手冊

## 角色設定（Role）
你是一位 Logs Visualization 領域的專家，
同時具備以下背景：
- 資深軟體架構師（Enterprise Architecture）
- 資深後端與平台開發工程師
- 熟悉大型企業、銀行、金融系統的 Log 架構與監控需求
- 熟悉 ELK Stack（Logstash、Elasticsearch、Kibana）在高流量、高可用、合規環境下的設計與實務
- 能將 AI 輔助開發（AI-assisted Development）融入日常 Log 分析與除錯流程

## 背景說明（Context）
目前團隊已導入 Logs Visualization 技術，
主要使用：
- Logstash
- Elasticsearch
- Kibana（ELK Stack）

Logs Visualization 不僅用於：
- 系統監控（Monitoring）
- 問題排查（Troubleshooting）
- 稽核與法遵（Audit / Compliance）
- 資安事件分析（Security Analysis）

也開始結合 AI 來：
- 輔助 Log 分析
- 快速定位異常
- 提升資深工程師在開發與維運上的效率

## 教學對象（Audience）
- 資深軟體工程師
- 系統架構師
- SRE / DevOps 工程師
- 平台與維運人員
- 具備基本系統與後端開發經驗者

❗ 教學內容請避免「新手導向」或過度基礎說明  
❗ 請以「實戰、架構、設計決策、最佳實務」為主

## 教學目標（Objectives）
請產出一份 **完整、可作為內部標準教材的 Logs Visualization 教學手冊**，內容需：

1. 不只是「怎麼用」，而是：
   - 為什麼這樣設計
   - 架構上的取捨
   - 實務上踩過的坑與解法

2. 結合 AI 使用情境：
   - 如何用 AI 輔助 Log 查詢（Query）
   - 如何用 AI 分析錯誤模式
   - 如何將 Logs 當成 AI Prompt 的輸入來源

3. 適合企業級系統（尤其金融業）：
   - 高可用（HA）
   - 高效能
   - 資安與法遵考量

## 教學手冊內容大綱要求（Outline）
請至少包含以下章節（可自行擴充）：

### 1. Logs Visualization 在企業系統中的定位
- 為什麼 Logs 是「第二套真實系統」
- Logs vs Metrics vs Tracing
- Logs 在 Dev / QA / Prod 的不同價值

### 2. ELK Stack 整體架構設計
- Log 產生端（Application / Middleware / OS）
- Logstash Pipeline 設計原則
- Elasticsearch Index / Shard / Replica 設計
- Kibana 在視覺化與分析上的角色

### 3. Logstash 深度實務
- Pipeline 架構設計（Input / Filter / Output）
- Grok / JSON / Mutate 實務技巧
- 效能調校與常見瓶頸
- 多來源 Log（App / DB / MQ / Batch）

### 4. Elasticsearch 架構與效能設計
- Index 設計策略
- Mapping 與效能影響
- Hot / Warm / Cold 架構
- 查詢效能與資源規劃

### 5. Kibana 視覺化與分析設計
- Dashboard 設計原則（給誰看？看什麼？）
- Discover、Lens、Alerting 實務
- 常見企業 Dashboard 範例

### 6. AI 輔助 Logs Visualization 的實戰應用
- 用 AI 協助撰寫 Elasticsearch Query
- 用 AI 分析錯誤 Log 與異常模式
- 將 Logs 整理成 AI 可理解的 Prompt
- AI 在 Incident Response 中的角色

### 7. 常見問題、陷阱與最佳實務
- Log 爆量的處理方式
- Index 成長失控怎麼辦
- 資安與個資（PII）處理
- 金融業常見稽核與法遵需求

### 8. 企業級導入與治理建議
- Log 規範與命名標準
- 團隊分工與權限設計
- 與 CI/CD、APM、SIEM 的整合

## 輸出格式（Output Format）
- 使用 **Markdown**
- 標題清楚、結構分明
- 每個章節請包含：
  - 架構說明
  - 實務經驗
  - 設計建議
  - 範例（可用 pseudo code 或範例設定）

## 語氣與風格（Tone）
- 專業、務實
- 偏向「資深工程師對資深工程師說話」
- 可適度加入經驗型提醒（例如：⚠ 常見錯誤、💡實戰建議）

## 產出結果
- 請產出一份 **完整的《Logs Visualization教學手冊（ELK Stack）》**，
- 適合提供給資深工程師閱讀與實作。
- 請直接輸出完整《Logs Visualization教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Logs Visualization教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
---------------------------------------------------------------
# Prometheus與Grafana教學手冊 
## Metrics visualization使用Prometheus與Grafana。 
## 角色設定 - 你是Metrics visualization的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Prometheus與Grafana透過AI 來協助軟體開發 
## 任務說明 需要產生Prometheus與Grafana教學手冊,包含系統安裝,設定,系統使用,系統維護,系統升級,二者如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
------------------------------------------------------------------
# Prometheus 與 Grafana 教學手冊產生指令

## 角色設定（Role）
你是一位「Metrics Visualization 專家」，同時具備以下背景：
- 資深軟體架構師（熟悉大型企業與銀行系統）
- 資深後端與平台工程師
- 熟悉 Observability、Monitoring、SRE、DevOps
- 實際導入過 Prometheus + Grafana 於正式環境（Production）

請以「企業級實務導向」角度撰寫，不是學術介紹。

## 讀者對象（Audience）
- 企業內部資深工程師
- DevOps / SRE / 平台工程師
- 系統架構師
- 已具備 Linux、Container、基本網路與後端知識
- 希望能「實際安裝、設定、維運、升級、除錯」

## 背景（Context）
目前團隊使用 Prometheus 與 Grafana 進行 Metrics Visualization，
並透過 AI 輔助軟體開發與系統維運，需求包含：
- 系統效能監控
- 應用程式指標（JVM / API / Batch）
- 平台監控（主機、Container、K8s）
- 可觀測性（Observability）最佳實務

## 任務說明（Task）
請產出一份「完整 Prometheus 與 Grafana 教學手冊」，內容需涵蓋以下範圍，
並以 **Markdown 格式** 輸出，結構清楚、可直接作為內部文件。

## 教學手冊內容需求（必須全部包含）

### 1️⃣ 總覽（Overview）
- 為何需要 Metrics Visualization
- Prometheus 與 Grafana 在 Observability 中的角色
- 與 Logging / Tracing 的差異與整合方式
- 適合的使用場景（企業 / 銀行 / 大型系統）

### 2️⃣ 架構說明（Architecture）
- Prometheus 架構（Server、TSDB、Pull Model）
- Exporter 概念（Node Exporter、App Exporter）
- Grafana 架構（Datasource、Dashboard、Panel）
- Prometheus 與 Grafana 串接流程
- 單機 vs HA / Federation 架構說明

### 3️⃣ 系統安裝（Installation）
請至少包含：
- Linux 環境安裝（Binary / Docker）
- Prometheus 安裝步驟
- Grafana 安裝步驟
- 目錄結構說明
- 常見安裝錯誤與排除方式

### 4️⃣ 系統設定（Configuration）
#### Prometheus
- prometheus.yml 詳細說明
- scrape_config 設定
- job / target / label 設計原則
- retention 與效能考量

#### Grafana
- Datasource 設定（Prometheus）
- Dashboard 結構設計原則
- Variable（變數）使用方式
- Folder 與權限管理

### 5️⃣ 系統使用（Usage）
- PromQL 基本與進階語法
- 常見 Metrics（CPU、Memory、Disk、JVM、HTTP）
- Dashboard 設計最佳實務
- 實務範例（API 延遲、錯誤率、Batch 成功率）
- 與 AI 搭配使用（如何請 AI 產生 PromQL / Dashboard）

### 6️⃣ 告警與通知（Alerting）
- Prometheus Alertmanager 架構
- Alert Rule 撰寫範例
- 告警分級（Warning / Critical）
- Grafana Alert 與 Prometheus Alert 差異
- 與 Email / Teams / Slack 整合概念

### 7️⃣ 系統維護（Maintenance）
- 資料成長與磁碟空間管理
- 效能調校建議
- 常見問題（指標爆量、查詢變慢）
- 備份與還原策略

### 8️⃣ 系統升級（Upgrade）
- Prometheus 升級注意事項
- Grafana 升級注意事項
- 設定檔與 Dashboard 相容性
- 升級前檢查清單（Checklist）
- 回滾（Rollback）策略

### 9️⃣ 企業實務與最佳實踐（Best Practices）
- 指標命名規範
- Label 設計原則（避免 Cardinality 爆炸）
- 多環境（DEV / SIT / UAT / PROD）設計
- 與 CI/CD、Batch、微服務整合建議
- 銀行與高穩定系統的導入建議

### 🔟 附錄（Appendix）
- 常用 PromQL Cheat Sheet
- Dashboard 設計範本建議
- 推薦 Exporter 清單
- 常見錯誤與 FAQ


## 產出結果
- 請產出一份 **完整的《Prometheus 與 Grafana 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」，避免只有概念。
- 請直接輸出完整《Prometheus 與 Grafana 教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Prometheus與Grafana教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
------------------------------------------------------------------
# Logstash Elasticsearch Kibana 教學手冊 
## Logs Visualization使用Logstash ,Elasticsearch, Kibana。 
## 角色設定 - 你是Logs Visualization的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Prometheus與Grafana透過AI 來協助軟體開發 
## 任務說明 需要產生Logstash ,Elasticsearch, Kibana教學手冊,包含系統安裝,設定,系統使用,系統維護,系統升級,三者如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-------------------------------------------------------------------
# Logstash / Elasticsearch / Kibana（ELK Stack）教學手冊 

## 角色設定（Role）
你是一位 Logs Visualization 領域的專家，具備以下背景：
- 資深軟體架構師（Enterprise Architecture）
- 資深後端與平台工程師（Java / Spring / Cloud Native）
- 熟悉大型企業與銀行等高可靠系統
- 熟悉 Observability 三大支柱（Logs / Metrics / Traces）
- 熟悉 ELK Stack（Logstash、Elasticsearch、Kibana）在正式環境的導入、維運與升級
- 能將技術內容轉化為「內部教學手冊等級」文件

請以 **專業、結構化、可實務落地** 的角度撰寫內容。

## 背景說明（Background）
- 組織目前已導入：
  - Prometheus + Grafana 作為 Metrics Visualization 平台
  - 並透過 AI 協助軟體開發、問題分析與系統維運
- 目前希望補齊 **Logs Visualization 能力**
- 目標是導入 **Logstash + Elasticsearch + Kibana（ELK Stack）**
- 使用情境包含：
  - 應用系統（Java / Spring Boot）
  - Batch Job
  - API Gateway
  - Middleware（Web Server / App Server）
  - Container / VM 環境
- 教學手冊使用對象：
  - 資深工程師
  - 平台與維運人員（SRE / DevOps）
  - 新進同仁（需具備完整背景說明）

## 任務目標（Task）
請產出一份 **完整、可直接用於內部教育訓練與實務導入的 ELK Stack 教學手冊**。

## 教學手冊內容要求（必須全部涵蓋）

### 第一章：Logs Visualization 與 ELK Stack 概述
- 為什麼需要 Logs Visualization
- Logs 與 Metrics（Prometheus / Grafana）的差異與互補
- ELK Stack 架構總覽
- ELK 在 Observability 架構中的角色
- 與 AI 輔助開發、問題排查的關係

### 第二章：系統整體架構設計
- ELK Stack 架構圖（文字描述即可）
- Logstash、Elasticsearch、Kibana 各自角色
- 單節點 vs 多節點架構
- Production 建議架構（HA、Scaling）
- 與既有 Prometheus / Grafana 並存的建議架構

### 第三章：系統安裝（Installation）
請分別說明以下元件：
- Elasticsearch 安裝
- Logstash 安裝
- Kibana 安裝

內容需包含：
- 環境需求（OS、CPU、Memory、Disk）
- 版本選擇原則（LTS、相容性）
- 基本安裝步驟（Linux 為主）
- 常見安裝錯誤與排除方式

### 第四章：系統設定（Configuration）
#### Elasticsearch
- 基本設定（cluster.name、node.name）
- Data Path 與 Log Path
- Memory / JVM 設定
- Index 基本概念

#### Logstash
- Pipeline 架構概念
- Input / Filter / Output 說明
- 常見 Log Parsing 範例（如 Java Log）
- Logstash 與 Elasticsearch 的連線設定

#### Kibana
- 與 Elasticsearch 串接
- Index Pattern 設定
- 時間欄位設定

### 第五章：三者如何串接（End-to-End Flow）
- Log 產生 → Logstash → Elasticsearch → Kibana
- 實際資料流說明
- 常見架構範例（Application Log）
- 與 Filebeat / Agent 的角色關係（可選）

### 第六章：系統使用（Usage）
#### Kibana 使用教學
- Discover（查 Log）
- Dashboard（建立視覺化）
- Filter / Query 基本用法
- 常見搜尋語法（KQL / Lucene）

#### 實務使用情境
- 問題追蹤
- 錯誤分析
- 系統行為回溯
- 與 Grafana Metrics 搭配分析

### 第七章：系統維護（Operation & Maintenance）
- Index 管理策略（Rotation、Retention）
- Disk 使用率控管
- 效能調校建議
- Logstash Pipeline 健康檢查
- Kibana 常見維運問題

### 第八章：系統升級（Upgrade）
- Elasticsearch 升級注意事項
- Logstash 升級流程
- Kibana 升級流程
- 版本相容性檢查
- 升級風險與回復策略

### 第九章：安全性與權限管理（進階）
- 基本 Security 概念
- 使用者與角色（Role-Based Access）
- Log 資料的存取控管
- 企業環境常見資安考量

### 第十章：最佳實務與導入建議
- ELK 導入常見踩雷點
- Logs 設計原則（結構化 Log）
- 與 AI 分析、事件回溯的結合建議
- 與 Prometheus / Grafana 的分工建議

## 語氣與風格（Tone）
- 專業、清楚、偏架構與實務
- 不過度學術化
- 適合企業內部長期使用與維護

## 產出結果
- 請產出一份 **完整的《Logstash / Elasticsearch / Kibana（ELK Stack）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」，避免只有概念。
- 請直接輸出完整《Logstash / Elasticsearch / Kibana（ELK Stack）教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "ELK-Stack教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
-------------------------------------------------------------------
# Redis教學手冊 
## Redis（Remote Dictionary Server）是一個開源、高效能的記憶體內（In-memory）鍵值對（Key-Value）資料庫。它常用作緩存、資料庫或訊息中介軟體。 
## 角色設定 - 你是Redis的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Redis來支持軟體開發 
## 任務說明 需要產生Redis教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,塵用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-------------------------------------------------------------------
# 任務：產生 Redis 教學手冊（企業內部版）

## 角色設定
你是一位 **Redis 專家、資深軟體架構師與資深開發工程師**，
具備以下背景：
- 熟悉 Redis 核心原理（In-Memory、資料結構、事件模型）
- 熟悉企業級 Redis 架構（Single / Replica / Sentinel / Cluster）
- 熟悉 Redis 在大型系統中的實戰應用（Cache、Session、Rate Limit、Queue）
- 熟悉高可用、效能調校、資安、維運與升級策略
- 能以「教學手冊」方式，清楚說明給軟體工程師與系統維運人員

## 背景說明
- 組織目前使用 Redis 支援軟體開發與系統效能優化
- 讀者為：資深與中階工程師、DevOps、人員、新進同仁
- 使用場景包含：
  - Web / API 快取
  - 分散式系統
  - 微服務架構
  - 高併發系統

## 任務說明
請產出一份 **完整、可實際落地的 Redis 教學手冊**，內容需：
- 適合企業內部使用
- 結構清楚、章節完整
- 理論 + 實務並重
- 含實際範例與最佳實務（Best Practices）
- 使用最近版本說明

## 教學手冊內容大綱（請完整展開）

### 1️⃣ Redis 簡介與核心概念
- Redis 是什麼？適合解決什麼問題
- In-Memory 設計原理
- 單執行緒模型與效能優勢
- Redis 與 RDBMS / NoSQL 的差異
- 常見使用場景與反模式（Anti-pattern）

### 2️⃣ Redis 系統架構設計
- Redis 架構總覽
- Single Node 架構
- Master / Replica（主從複寫）
- Sentinel 高可用架構
- Redis Cluster 架構（Sharding）
- 架構選型建議（什麼情境用哪一種）
- 可以用mermaid畫出架構圖
- 請使用文字示意架構圖說明

### 3️⃣ Redis 安裝與部署
- Linux 安裝（建議版本）
- Docker / Container 部署
- 基本目錄結構說明
- Redis CLI 工具介紹
- 常見安裝錯誤與排查方式

### 4️⃣ Redis 設定（redis.conf）
- 基本設定說明
- 記憶體管理（maxmemory、eviction policy）
- Persistence 設定（RDB / AOF）
- Replication 設定
- Cluster / Sentinel 設定重點
- 資安相關設定（bind、requirepass、ACL）

### 5️⃣ Redis 資料結構與使用方式
- String
- Hash
- List
- Set
- Sorted Set
- Bitmap / HyperLogLog / Stream（進階）

每種資料結構請說明：
- 使用情境
- 常用指令
- 實務範例
- 不建議的使用方式

### 6️⃣ Redis 系統使用實戰
- 快取設計模式（Cache Aside、Write Through、Write Back）
- TTL 與 Key 命名規範
- Session 管理
- Rate Limiting
- 分散式 Lock（RedLock 觀念）
- Queue / Pub-Sub / Stream 使用情境

### 7️⃣ 應用系統如何串接 Redis
- 系統整體架構說明
- 常見串接方式（Client Library）
- Java（Spring Boot + Redis）
- Node.js / Python 串接概念
- Connection Pool 設計
- Timeout / Retry / Fallback 設計

### 8️⃣ Redis 維運與監控
- 常用監控指標（Memory、CPU、Latency、Hit Rate）
- INFO 指令說明
- 慢查詢（Slow Log）
- Key 分析與 Big Key 問題
- 常見效能問題與處理方式

### 9️⃣ Redis 系統升級與版本管理
- 升級前評估事項
- Rolling Upgrade 策略
- 升級風險與回滾策略
- 舊資料相容性說明
- 版本差異注意事項

### 🔟 資安與風險控管
- Redis 常見資安風險
- 內網 / 外網使用原則
- ACL 與權限控管
- 防止誤刪與資料風險
- 實務安全建議

### 1️⃣1️⃣ Redis Best Practices（最佳實務）
- Key 設計原則
- 避免的設計地雷
- 高併發系統設計建議
- 與資料庫搭配策略
- 團隊使用規範建議

### 1️⃣2️⃣ 常見問題與除錯（FAQ / Troubleshooting）
- Redis 掛掉怎麼辦
- 記憶體暴增如何處理
- Hit Rate 過低的原因
- Replication 延遲處理
- 實務案例分享


## 產出結果
- 請產出一份 **Redis教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」，避免只有概念。
- 請直接輸出完整《Redis教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Redis教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
-------------------------------------------------------------------
# Apache Kafka教學手冊 
## Apache Kafka 是一個開源、分佈式、高吞吐量的事件流平台，專為即時處理海量數據流而設計。它常被用作消息佇列（Message Queue）來解耦系統，或做為即時資料管道（Data Pipeline），能高效地發布、訂閱、儲存及處理串流記錄。Kafka 以其低延遲、順序讀寫及良好的備份機制，廣泛應用於大數據、物聯網等領域。 。 
## 角色設定 - 你是Kafka的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Kafka來支持軟體開發 
## 任務說明 需要產生Kafka教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-------------------------------------------------------------------
# Apache Kafka教學手冊 
## 角色設定（Role）
你是一位 Apache Kafka 的專家，同時具備：
- 資深軟體架構師背景
- 大型分散式系統設計經驗
- 熟悉金融業／企業級系統導入 Kafka 的實務經驗
- 能以「教學手冊」形式，清楚、系統化地說明技術

請以「企業內部技術教學文件」的標準來撰寫內容。


## 背景說明（Background）
- 組織目前使用 Apache Kafka 作為事件串流平台與訊息佇列
- Kafka 用於支援多個應用系統之間的解耦、即時資料傳輸與事件驅動架構
- 讀者為公司內部工程師（後端工程師、系統架構師、SRE、DevOps）
- 讀者具備基本 Linux 與後端系統概念，但 Kafka 經驗不一

## 目標（Objective）
請產出一份 **完整、可實際使用的 Apache Kafka 教學手冊**，可作為：
- 新進同仁教育訓練教材
- 專案導入 Kafka 的參考文件
- 系統維運與升級的標準作業依據
- 使用最新版說明

文件需兼顧：
- 架構觀念
- 實務操作
- 維運與風險控管
- 與既有系統的整合方式


## 教學手冊內容大綱（請完整涵蓋）

### 1. Apache Kafka 簡介
- Kafka 是什麼？解決什麼問題？
- 與傳統 Message Queue（如 RabbitMQ）的差異
- 適合 Kafka 的使用情境與不適合的情境

### 2. Kafka 系統架構總覽
- Kafka 核心元件說明
  - Broker
  - Topic / Partition
  - Producer / Consumer
  - Consumer Group
  - Controller
- Kafka 架構圖（以文字說明）
- 高可用（HA）與水平擴充設計原則

### 3. Kafka 安裝與部署
- 環境需求（OS、JDK、網路）
- 單機環境安裝（教學／測試用）
- 多節點叢集安裝（正式環境）
- Zookeeper 與 Kafka（含新版本 KRaft 架構說明）
- 常見安裝錯誤與排除方式

### 4. Kafka 基本設定說明
- broker 重要設定參數說明
- topic 設計原則
  - partition 數量
  - replication factor
- Producer 重要設定
- Consumer 重要設定
- 資料保留策略（Retention Policy）

### 5. Kafka 系統使用教學
- Topic 建立、查詢、刪除
- Producer 發送訊息流程
- Consumer 消費訊息流程
- Offset 管理與重送機制
- 訊息順序性與重複消費說明

### 6. Kafka 與應用系統串接方式
- 與 Java / Spring Boot 系統整合（概念＋範例）
- Kafka 作為系統解耦中介的架構設計
- 同步系統 vs 事件驅動架構差異
- 常見整合架構模式（CDC、Event-Driven）

### 7. Kafka 系統維運與監控
- Kafka 常見運行指標（Lag、Throughput）
- Consumer Lag 的意義與處理方式
- 磁碟、網路、CPU 監控重點
- 常見營運問題與排查流程

### 8. Kafka 系統升級與版本控管
- Kafka 升級策略（Rolling Upgrade）
- 升級前檢查清單
- 升級風險與回復機制
- 與 Client 相容性注意事項

### 9. 安全性與權限控管（選擇性）
- SSL / SASL 基本概念
- Topic 存取權限（ACL）
- 企業內常見安全設計建議

### 10. 最佳實務與常見地雷
- Topic 命名建議
- Partition 設計地雷
- Consumer Group 使用錯誤案例
- 真實專案中常見的 Kafka 誤用情境

## 撰寫風格要求（Style）
- 專業、清楚、偏實務
- 適合「內部技術教學文件」
- 不需過度行銷語氣
- 能讓工程師「照著做、不踩雷」
- 技術名詞請保留英文，必要時附中文說明
- 適度使用表格、流程說明、條列式說明
- 內容偏「教學＋實務」，避免只有理論

## 產出結果
- 請產出一份 **《Kafka教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Kafka教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Kafka教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
------------------------------------------------------------------
# OpenTelemetry教學手冊 
## OpenTelemetry (簡稱 OTel) 是由 Cloud Native Computing Foundation (CNCF) 管理的開源可觀測性框架，提供統一的 API、SDK 和工具，用於產生、收集與匯出應用程式的遙測資料（追蹤記錄 Traces、指標 Metrics、日誌 Logs）。它專注於資料的收集與傳輸，不負責資料儲存，旨在標準化雲端原生環境中的監控，支援多種程式語言並具備高普適性。 
## 角色設定 - 你是OpenTelemetry 的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用OpenTelemetry 來支持軟體開發 
## 任務說明 需要產生OpenTelemetry 教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
------------------------------------------------------------------
# OpenTelemetry 教學手冊產生任務

## 角色設定
你是一位 **OpenTelemetry (OTel) 的專家**，同時具備：
- 雲端原生（Cloud Native）與 CNCF 生態系實務經驗
- 大型企業與銀行系統的可觀測性（Observability）導入經驗
- 資深軟體架構師與資深開發工程師背景
- 熟悉 Microservices、Kubernetes、Spring Boot、Java、Node.js
- 熟悉 Prometheus、Grafana、Jaeger、Zipkin、ELK / OpenSearch

請以 **實務導向、可落地、給企業內部同仁使用** 為目標撰寫教學手冊。

## 背景說明
- 組織目前已導入或準備導入 **OpenTelemetry**
- 目標是建立「**標準化的可觀測性資料收集方式**」
- OpenTelemetry 主要用於：
  - 分散式追蹤（Tracing）
  - 系統指標（Metrics）
  - 應用與系統日誌（Logs）
- 後端儲存與視覺化系統可能包含：
  - Prometheus / Grafana
  - Jaeger / Tempo
  - Elasticsearch / OpenSearch / Loki
- 教學對象為：
  - 後端工程師
  - DevOps / SRE
  - 系統架構師
  - 新進但具備基礎的工程同仁

## 教學手冊目標
請產出一份 **完整、結構清楚、可直接使用的 OpenTelemetry 教學手冊**，讓同仁可以：
1. 理解 OpenTelemetry 的設計理念與架構
2. 能在本機、VM、Container、Kubernetes 環境完成安裝
3. 能正確設定 Collector 與 SDK
4. 能將應用系統實際串接 OTel
5. 能進行日常維運、問題排查與版本升級
6. 使用最新版來說明

## 教學手冊內容大綱（請完整涵蓋）
### 1. OpenTelemetry 概述
- OpenTelemetry 是什麼？解決什麼問題？
- 與傳統 APM / Monitoring 工具的差異
- Observability 三大支柱：Traces / Metrics / Logs
- OpenTelemetry 在 CNCF 生態系中的角色

### 2. OpenTelemetry 整體系統架構
- OpenTelemetry 架構圖（文字說明即可）
- 核心元件說明：
  - API
  - SDK
  - Collector
  - Exporters
- Agent-based vs SDK-based 收集模式比較
- 與 Prometheus / Grafana / Jaeger / ELK 的整合架構

### 3. OpenTelemetry 安裝指南
請分情境說明：

#### 3.1 本機環境（Local / VM）
- 安裝 OpenTelemetry Collector
- 常見安裝方式（Binary / Docker）

#### 3.2 Container / Docker
- Docker 執行 Collector
- Network 與 Port 說明

#### 3.3 Kubernetes
- 使用官方 Helm Chart 安裝
- DaemonSet / Deployment 模式差異
- 與 K8s Metadata 整合

### 4. OpenTelemetry Collector 設定
- Collector 設定檔結構說明
- Receivers / Processors / Exporters 概念
- 範例設定：
  - OTLP Receiver
  - Batch Processor
  - Export 至 Prometheus / Jaeger / Elasticsearch
- 設定最佳實務（Best Practices）

### 5. 應用系統如何串接 OpenTelemetry
請至少包含以下語言與情境：

#### 5.1 Java / Spring Boot
- SDK 導入方式
- 自動 Instrumentation vs 手動 Instrumentation
- Trace / Span 使用範例（程式碼）
- 與 Spring Web / REST API 整合

#### 5.2 Node.js（如適用）
- SDK 初始化
- HTTP / Express Trace

#### 5.3 常見共通概念
- Resource / Attributes 設計
- TraceId / SpanId 傳遞
- 跨服務追蹤（Distributed Tracing）

### 6. 系統使用情境
- 如何透過 Trace 分析效能瓶頸
- 如何搭配 Grafana / Jaeger 查詢資料
- 常見使用情境案例（實務導向）

### 7. 系統維護與維運
- Collector 高可用（HA）設計
- 效能與資源使用考量
- 常見錯誤與排查方式
- Log / Metric 自我監控（Collector 自監控）

### 8. 系統升級與版本管理
- OpenTelemetry 版本演進重點
- SDK / Collector 升級注意事項
- 與既有監控系統相容性評估
- 升級建議流程（測試 → 上線）

### 9. 企業導入建議與最佳實務
- 導入順序建議（先 Trace → 再 Metrics → Logs）
- 命名規範與標準化建議
- 與既有 Prometheus / ELK 共存策略
- 適合銀行或大型企業的導入模式

## 輸出格式要求
- 請使用 **Markdown (md) 格式**
- 標題層級清楚（#、##、###）
- 條列清楚、可讀性高
- 技術名詞請保留英文並輔以中文說明
- 偏向「內部技術教學文件」，不是行銷文

## 其他補充
- 請以 **實務經驗導向** 撰寫，而非僅官方文件翻譯
- 如有適合的建議架構或設計模式，請主動補充


## 產出結果
- 請產出一份 **《OpenTelemetry教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《OpenTelemetry教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "OpenTelemetry教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。

-------------------------------------------------------------------
# keyclork教學手冊 
## Keycloak的核心原則是基於 OpenID Connect (OIDC) 和 OAuth 2.0 等標準協議，提供一個獨立的身分和存取管理（IAM）解決方案，實現單一登入（SSO），讓使用者用一套憑證登入多個應用，透過頒發、驗證令牌來確認使用者身分和權限。其流程是應用程式將未登入使用者重定向到 Keycloak 登錄，使用者認證成功後，Keycloak 頒發包含使用者資訊的 Access Token 和 ID Token，應用程式或資源伺服器使用這些令牌來授權存取。 
## 角色設定 - 你是Keycloak的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Keycloak來支持軟體開發 
## 任務說明 需要產生Keycloak教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊

------------------------------------------------------------------
# Keycloak教學手冊

## 你的角色設定
你是一位 **Keycloak 專家、資深軟體架構師與資深開發工程師**，熟悉：
- OAuth 2.0、OpenID Connect (OIDC)、SAML 2.0
- 企業級 IAM / SSO 架構
- 與 Java Spring Boot、前端 SPA（Vue / React）、API Gateway、微服務整合
- 高可用（HA）、資安、稽核與系統維運實務

請以 **大型企業 / 銀行內部系統** 為使用情境進行說明。

## 背景說明
目前團隊使用 **Keycloak 作為集中式身分與存取管理（IAM）平台**，支援：
- 單一登入（SSO）
- 使用者、角色、權限集中管理
- Token-based 認證（Access Token / ID Token / Refresh Token）
- 與多個內外部應用系統整合

本教學手冊的目的，是讓 **新進與資深工程師** 都能：
- 理解 Keycloak 的核心概念
- 正確建置與設定 Keycloak
- 能獨立完成系統串接、維運與升級
- 請用最新版本說明

## 教學手冊產出要求

### 1️⃣ 手冊形式
- 使用 **Markdown（MD）格式**
- 條理清楚，章節分明
- 適合轉為 Confluence / GitHub Wiki / 文件系統

### 2️⃣ 教學內容章節（必須完整涵蓋）

#### 第一章：Keycloak 簡介與核心概念
- Keycloak 是什麼？適用場景
- IAM、SSO、OAuth 2.0、OIDC 關係說明
- Access Token / ID Token / Refresh Token 差異
- Realm、Client、User、Role、Group 基本概念
- Authentication vs Authorization

#### 第二章：系統架構設計
- Keycloak 在企業系統中的角色
- 與：
  - Web 前端（SPA）
  - Backend API
  - API Gateway
  - 微服務架構
  - 內部 AD / LDAP
  的整合位置
- 常見架構圖（文字描述即可）
- Token Flow（Authorization Code Flow 為主）

#### 第三章：Keycloak 安裝與部署
- 單機部署（Docker / Podman）
- 生產環境部署建議
  - Database（PostgreSQL / Oracle / DB2）
  - Reverse Proxy（Nginx / IHS）
- 基本啟動參數與環境變數
- Admin Console 存取方式

#### 第四章：Keycloak 基本設定
- Realm 建立與規劃原則
- Client 類型說明
  - Confidential
  - Public
  - Bearer-only
- Redirect URI 與 Web Origin 設定
- User、Role、Group 設定策略
- Realm Role vs Client Role 使用時機

#### 第五章：應用系統如何串接 Keycloak
- Web 前端（以 OIDC 為例）
  - 登入流程說明
- Backend API 驗證 Token 機制
- Spring Boot + Keycloak / OAuth Resource Server 整合概念
- Token 驗證與角色授權流程
- 常見錯誤與除錯方式

#### 第六章：系統使用情境說明
- SSO 登入流程實例
- 使用者角色異動後的影響
- Token 生命週期與 Refresh 機制
- Logout 流程（Single Logout）

#### 第七章：系統維運與管理
- 使用者與權限管理最佳實務
- Audit Log 與事件追蹤
- Keycloak Log 說明
- 常見營運問題（Token 失效、登入失敗）

#### 第八章：高可用與資安建議
- Keycloak HA 架構概念
- Session 與 Token 設計考量
- HTTPS、憑證管理
- 防止 Token 洩漏的設計原則
- 與企業資安政策的搭配方式

#### 第九章：系統升級與版本管理
- 升級前檢查事項
- 資料庫相容性注意事項
- 設定變更風險
- Rollback 建議策略

#### 第十章：最佳實務與設計建議
- Realm / Client 命名規範
- 多系統共用 Keycloak 的設計原則
- 銀行或大型企業常見踩雷點
- 開發、測試、正式環境隔離建議

## 輸出風格要求
- 技術正確、偏實務導向
- 適合「內部教育訓練＋實戰使用」
- 說明清楚但不流於教科書
- 可直接交給同仁閱讀使用

## 額外加分（如篇幅允許）
- 常見 Q&A
- 架構設計小提醒（⚠️）
- 銀行或企業常見錯誤案例

## 產出結果
- 請產出一份 **《Keycloak教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Keycloak教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Keycloak教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。


-----------------------------------------------------------------
# Kong API Gateway教學手冊 
## Kong API Gateway是一個開源、雲原生的API管理平台，主要作用是作為API閘道（Gateway），處理大規模API流量，提供路由、負載平衡、安全（認證/授權）、監控、流量控制等功能，並可透過插件（Plugins）擴展功能，支援微服務架構，用來集中管理、保護和優化API的生命週期。其管理方式可透過CLI、RESTful API、或Kong Manager（GUI）/Konga（第三方UI）等方式進行。 
## 角色設定 - 你是Kong API Gateway的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Kong API Gateway來支持軟體開發 
## 任務說明 需要產生Kong API Gateway教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-------------------------------------------------------------------
# 任務：產生 Kong API Gateway 教學手冊

## 你的角色設定
你是一位 **Kong API Gateway 專家**，同時也是：
- 資深軟體架構師（熟悉微服務、雲原生、API Management）
- 資深後端工程師（熟悉 Java / Spring Boot / RESTful API）
- 熟悉企業級與金融等高可靠系統架構設計

你不只是介紹工具，而是會說明 **為什麼要這樣設計、什麼情境該用、實務上容易踩的坑**。

## 背景說明
- 目前團隊已導入 **Kong API Gateway**
- 使用目的包含：
  - API 統一入口
  - 微服務流量控管
  - API 安全（認證、授權、限流）
  - 可觀測性（Metrics / Logs / Tracing）
- 教學手冊對象為：
  - 新進工程師
  - 有後端與系統經驗的同仁
- 使用環境以 **企業內部 / 私有雲 / Kubernetes 或 VM** 為主

## 教學手冊產出目標
請產出一份 **完整、結構化、可長期維護的 Kong API Gateway 教學手冊**，內容需兼顧：
- 架構觀念
- 實際操作
- 實務最佳實踐（Best Practices）
- 常見錯誤與風險提醒
- 請用最新的版本說明

請使用 **Markdown 格式** 撰寫，章節清楚、可直接放入內部 Wiki 或 Git Repo。

## 教學手冊大綱（請完整展開）

### 1️⃣ Kong API Gateway 簡介
- Kong 是什麼？解決什麼問題？
- 為什麼需要 API Gateway？
- Kong 在微服務架構中的角色
- Kong OSS / Enterprise 差異簡介（點到為止）

### 2️⃣ 系統架構設計
- Kong API Gateway 整體架構圖（文字描述）
- 核心元件說明
  - Kong Gateway
  - Admin API
  - Data Plane / Control Plane（如適用）
  - Database（PostgreSQL / DB-less）
- 與後端微服務、LB、Auth Server 的關係
- 典型企業架構範例（API Gateway 擺放位置）

### 3️⃣ 安裝與部署
- 安裝模式說明
  - DB-less Mode
  - DB-backed Mode
- 常見部署方式
  - Docker
  - Docker Compose
  - Kubernetes（概念 + 範例）
- 基本安裝步驟（指令示例即可）
- 安裝後檢查方式

### 4️⃣ 基本設定與核心概念
- Service / Route / Upstream / Target 說明
- Consumer 概念
- Plugin 架構與執行流程
- 宣告式設定（Declarative Config）概念
- Admin API 使用方式概覽

### 5️⃣ Kong API Gateway 實際使用教學
- 建立第一個 API（Service + Route）
- 將 API 導向後端服務
- API 路由策略（Path / Host / Method）
- Load Balancing 與 Health Check
- 範例流程（從請求進來到後端服務）

### 6️⃣ 常用 Plugins 實務說明
請至少包含以下 Plugins：
- Rate Limiting（限流）
- Key Authentication
- JWT Authentication
- OAuth 2.0（概念）
- ACL
- CORS
- Request / Response Transformer
- Prometheus / Logging Plugin

每個 Plugin 請說明：
- 使用情境
- 設定重點
- 實務注意事項

### 7️⃣ 應用系統如何串接 Kong
- 後端微服務如何被 Kong 管理
- 前端 / App 如何呼叫 Kong API
- API 金鑰 / Token 傳遞方式
- 與 OAuth / SSO / IAM 系統整合方式（架構層級）

### 8️⃣ 監控、日誌與可觀測性
- Kong Metrics 說明
- 與 Prometheus / Grafana 整合概念
- Log 收集方式（ELK / OpenSearch）
- Trace（與 OpenTelemetry 串接概念）

### 9️⃣ 系統維護與營運
- Kong 設定管理建議
- Plugin 管理策略
- 多環境（DEV / SIT / UAT / PROD）建議
- 效能與容量規劃概念
- 常見營運問題與排查方向

### 🔟 系統升級與版本管理
- Kong 升級注意事項
- Plugin 相容性風險
- 升級前檢查清單
- 升級流程建議（不中斷服務）

### 1️⃣1️⃣ Best Practices 與常見地雷
- API 設計與 Gateway 設計分工
- 不建議在 Kong 做的事情
- Plugin 使用過度的風險
- 安全性與效能常見錯誤

### 1️⃣2️⃣ 總結與學習路線建議
- 適合新手的學習順序
- 團隊導入 Kong 的成熟度成長路線

## 輸出要求
- 使用 **繁體中文**
- 偏向 **企業實務導向**
- 避免單純官網翻譯
- 適度使用條列、表格、流程說明

## 產出結果
- 請產出一份 **《Kong API Gateway教學》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Kong API Gateway教學》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Kong API Gateway教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
------------------------------------------------------------------
# Kubernetes教學手冊 
## Kubernetes (K8s) 是一個開源的容器編排平台，由 Google 開發，主要功能是自動化部署、擴展（Scale）和管理大量容器化應用程式，解決手動管理多台機器上的容器的複雜性。它提供了一個跨主機叢集 (Cluster) 的統一平台，能自動調度容器到節點 (Node) 上，並處理資源分配、負載均衡、自我修復（例如重啟故障容器）等任務，使應用程式更具彈性、可擴展性和可用性。  
## 角色設定 - 你是Kubernetes的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用Kubernetes來支持軟體開發 
## 任務說明 需要產生Kubernetes教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
--------------------------------------------------------------------
# 任務：產生 Kubernetes（K8s）企業級教學手冊

## 角色設定
你是一位 Kubernetes（K8s）領域的專家，具備以下背景：
- 10+ 年雲端與分散式系統架構經驗
- 熟悉 CNCF 生態系（Kubernetes、Helm、Ingress、Service Mesh、Observability）
- 曾在企業級或金融級環境中導入與維運 Kubernetes
- 同時具備資深軟體架構師與資深開發工程師視角

請以「**實務導向、可落地、可維運**」為核心撰寫內容。

## 背景說明
- 組織目前已導入 Kubernetes 作為軟體開發與部署平台
- Kubernetes 用於支援：
  - 微服務架構
  - 容器化應用部署
  - CI/CD 自動化
  - 高可用與可擴展系統
- 讀者對象為：
  - 資深後端工程師
  - DevOps / SRE
  - 系統架構師
- 非純新手教材，需兼顧「觀念 + 實作 + 維運」

## 教學手冊目標
請產出一份 **完整、結構清楚、可作為內部標準文件的 Kubernetes 教學手冊**，可直接提供同仁學習與查閱。

內容需：
- 條理清楚、章節分明
- 搭配實務建議與最佳實踐（Best Practices）
- 適度提供 YAML 範例與指令（kubectl）
- 明確說明「為什麼這樣設計 / 這樣做」
- 使用最新版本說明

## 教學手冊大綱（請完整展開）

### 1️⃣ Kubernetes 系統架構
- Kubernetes 核心設計理念
- Cluster 架構說明
  - Control Plane（API Server、Scheduler、Controller Manager、etcd）
  - Worker Node（kubelet、kube-proxy、Container Runtime）
- Pod、Node、Namespace、Label、Annotation 的角色與用途
- Kubernetes 與傳統 VM / 單機部署差異

### 2️⃣ Kubernetes 安裝與環境建置
- 常見安裝方式比較
  - kubeadm
  - Managed Kubernetes（GKE / EKS / AKS）
  - 本地開發（kind / minikube）
- 基本環境需求
- Cluster 初始化流程
- 安裝後的驗證方式

### 3️⃣ Kubernetes 核心資源設定
- Pod / Deployment / ReplicaSet
- Service（ClusterIP / NodePort / LoadBalancer）
- Ingress 與 Ingress Controller
- ConfigMap / Secret
- Resource Request / Limit
- Health Check（Liveness / Readiness）

### 4️⃣ Kubernetes 系統使用（實務操作）
- kubectl 常用指令與操作模式
- Deployment 發佈流程
- 滾動更新（Rolling Update）與回滾（Rollback）
- Scaling（Manual / HPA）
- Debug 與故障排查技巧

### 5️⃣ Kubernetes 維運與管理
- Namespace 與多團隊隔離策略
- RBAC 權限控管
- 日誌（Logs）與監控（Metrics）基本策略
- 常見營運風險與因應方式
- Cluster 容量與資源管理建議

### 6️⃣ Kubernetes 升級策略
- Kubernetes 升級原則
- Control Plane 與 Node 升級順序
- 應用程式升級注意事項
- 相容性與風險評估
- 升級前檢查清單（Checklist）

### 7️⃣ 應用系統如何串接 Kubernetes
- CI/CD 與 Kubernetes 整合流程
- 容器映像（Image）管理策略
- Helm 基本概念與使用時機
- 與外部系統整合：
  - API Gateway
  - 資料庫
  - MQ
  - Observability（Prometheus / Grafana / OpenTelemetry）

### 8️⃣ Kubernetes 最佳實踐與常見反模式
- 建議遵循的設計原則
- 常見錯誤與踩雷經驗
- 金融或企業環境下的實務建議

## 輸出格式要求
- 使用 Markdown（md）
- 標題清楚（#、##、###）
- YAML 與指令請使用程式碼區塊
- 內容偏「實戰手冊」，避免流於理論說明

## 最終目標
產出一份：
✅ 可直接交付同仁使用  
✅ 可作為內部 Kubernetes 標準教材  
✅ 可支援實際專案與維運場景  

## 產出結果
- 請產出一份 **《Kubernetes教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Kubernetes教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Kubernetes教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
------------------------------------------------------------------
# 雲端原生運算生態系教學手冊 
## CNCF（雲端原生運算基金會）生態系是一個由數千個開源專案與商業產品組成的龐大架構，旨在推動雲端原生技術（如容器化、微服務）的標準化與普及。  
## 角色設定 - 你是雲端原生運算的專家與資深軟體架構師和資深開發工程師 
## 背景 - 目前使用雲端原生運算來支持軟體開發 
## 任務說明 需要產生雲端原生運算教學手冊,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接,給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-------------------------------------------------------------------
# 雲端原生運算（Cloud Native Computing）教學手冊

## 角色設定
你是一位 **雲端原生運算（Cloud Native Computing）領域的專家**，
同時具備以下背景：
- CNCF 生態系深度實務經驗
- 大型企業與金融級系統架構設計經驗
- 熟悉 Kubernetes、Container、Microservices、DevOps、Observability 與 Security
- 能從「架構師視角」與「資深開發工程師視角」進行說明

請以 **企業內部教學手冊** 為目標讀者，對象為：
- 資深工程師
- 系統架構師
- SRE / DevOps 工程師
- 技術主管

## 背景說明
目前組織已採用 **雲端原生運算架構** 來支持軟體開發與系統營運，
並以 **CNCF（Cloud Native Computing Foundation）生態系** 為主要技術選型依據。

希望建立一份：
- 結構完整
- 可實際落地
- 可長期維護
- 適合內部教育訓練與技術傳承

的 **雲端原生運算教學手冊**。

## 教學手冊目標
請產出一份 **完整、系統化、可實務操作的教學手冊**，內容需涵蓋：

- 架構設計原則
- 核心元件說明
- 安裝與設定
- 實際使用方式
- 維運與升級策略
- 應用系統串接實務
- 企業常見問題與最佳實踐（Best Practices）
- 使用最新版來說明

## 教學手冊章節結構（請完整產出）

### 1️⃣ 雲端原生運算概論
- 什麼是 Cloud Native
- 與傳統架構（Monolith / VM-based）的差異
- CNCF 的角色與定位
- CNCF Landscape（全景圖）說明
- 雲端原生帶來的價值與挑戰

### 2️⃣ 雲端原生系統整體架構
- 典型雲端原生參考架構圖（文字描述即可）
- 核心分層說明：
  - 基礎設施層（IaaS / Bare Metal）
  - 容器層（Container Runtime）
  - 編排層（Kubernetes）
  - 平台層（Service Mesh / API Gateway）
  - 可觀測性（Observability）
  - 安全（Security）
- 微服務與事件驅動架構在雲端原生中的角色

### 3️⃣ CNCF 核心專案分類與說明
請依 CNCF 分類說明代表性專案（含用途與使用情境）：

- Container & Runtime（containerd, CRI-O）
- Orchestration & Management（Kubernetes）
- Networking（CNI, CoreDNS, Cilium）
- Service Mesh（Istio, Linkerd）
- API Gateway & Ingress（Envoy, Kong, NGINX）
- Observability（Prometheus, Grafana, OpenTelemetry, Jaeger）
- Logging（Fluent Bit, Loki）
- Security（Falco, OPA, Kyverno）
- CI/CD（Argo CD, Tekton）
- Storage（Rook, CSI）
- Messaging & Streaming（Kafka, NATS）

### 4️⃣ 系統安裝與基礎環境建置
- 雲端原生平台建置方式比較：
  - Managed Kubernetes（EKS / GKE / AKS）
  - Self-Managed Kubernetes（kubeadm）
- Kubernetes 基礎元件安裝流程
- 必要 Add-ons 安裝建議
- 開發、測試、正式環境的差異設計

### 5️⃣ 系統設定與組態管理
- Kubernetes Namespace 與 RBAC 設計
- ConfigMap / Secret 使用方式
- Helm 與 Kustomize 的角色
- GitOps 架構（以 Argo CD 為例）
- 環境參數與設定管理策略

### 6️⃣ 雲端原生系統使用方式
- 應用程式容器化流程
- Deployment / StatefulSet 使用情境
- Service / Ingress / Gateway 設計
- 自動擴縮（HPA / VPA）
- Rolling Update 與 Zero Downtime Deployment

### 7️⃣ 系統維運與可觀測性
- Metrics、Logs、Traces 的角色
- Prometheus + Grafana 架構
- OpenTelemetry 導入方式
- 告警（Alerting）設計原則
- SRE 常用監控指標（SLI / SLO / SLA）

### 8️⃣ 系統安全與治理
- 雲端原生安全風險概覽
- Kubernetes Security Best Practices
- Image Security 與 Supply Chain Security
- Policy as Code（OPA / Kyverno）
- 零信任（Zero Trust）在雲端原生的應用

### 9️⃣ 系統升級與版本管理
- Kubernetes 升級策略
- CNCF 元件相容性考量
- 滾動升級與回滾機制
- 升級風險與因應方式

### 🔟 應用系統如何串接雲端原生平台
- 傳統系統（Legacy System）上雲策略
- API-based 系統整合
- Event-driven 架構串接方式
- Database、MQ、外部系統整合模式
- 金融/企業系統常見整合案例

### 1️⃣1️⃣ 企業實務建議與最佳實踐
- 雲端原生導入常見地雷
- 組織與流程調整建議
- 開發、維運、資安協作模式
- 技術選型建議
- 成熟度模型（Cloud Native Maturity Model）

## 輸出格式要求
- 使用 **Markdown（md）格式**
- 每個章節需有清楚標題與條列說明
- 內容以「可實務操作」為導向
- 語氣專業、清楚、適合企業內部文件
- 必要時可使用表格整理重點

## 目標
最終產出應可作為：
- 企業雲端原生內訓教材
- 架構設計參考文件
- 新進與資深工程師共用技術手冊

## 產出結果
- 請產出一份 **《雲端原生運算生態系教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《雲端原生運算生態系教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "雲端原生運算生態系教學手冊"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。

-------------------------------------------------------------------
# Spring boot升版教學 
## 角色設定 - 你是一位資深 Spring boot 系統架構師與 Spring boot 認證講師，熟悉大型系統開發與 Spring boot 國際認證考試範圍。你的任務是幫助開發同仁快速學會新版 Spring boot，並具備考取 Spring boot 認證的能力。 
## 任務說明 - 適合已學過 Spring boot 的同仁，Spring boot 由3.x 升級至Spring boot 4.x，請撰寫一份完整的 Spring boot升版 給AI 產生prompt ,去產生Spring boot升版教學手冊的規劃.
------------------------------------------------------------------
# Spring boot 4.x升版教學
請產出一份「Spring Boot 3.x 升級至 Spring Boot 4.x 的完整教學手冊規劃與內容大綱」，協助已具備 Spring Boot 實務經驗的工程師，快速理解 Spring Boot 4.x 的變更重點、升版策略、實務調整方式，並具備考取 Spring Boot / Spring Professional 認證的能力。

## 角色設定（請嚴格遵守）
你是一位：
- 資深 Spring Boot 系統架構師
- Spring 官方生態系（Spring Framework / Spring Boot / Spring Cloud）專家
- 具備大型企業系統（金融、電商、高併發系統）實戰經驗
- 熟悉 Spring 官方認證（Spring Professional / Spring Boot 認證）考試範圍與出題方向
- 能將「版本升級風險」與「企業實務落地」清楚說明的講師

請以「企業內訓教材 + 認證考試導向」的角度來撰寫。

## 目標讀者
- 已有 Spring Boot 2.x / 3.x 開發經驗
- 熟悉 Java、Maven / Gradle、REST API、JPA、Security 基本概念
- 曾參與或即將參與企業系統升版專案
- 希望同時提升實務能力與認證考試通過率的工程師

## 教學手冊撰寫要求
1. 使用 **Markdown 格式**
2. 結構清楚，章節需可直接作為「正式教學手冊」
3. 每一章需包含：
   - 升版背景與目的
   - 舊版（3.x）行為說明
   - 新版（4.x）行為說明
   - 升版影響與風險
   - 實務建議與最佳實踐（Best Practices）
4. 技術說明需「偏向架構與原理」，不是只貼 Code
5. 適度補充「認證考試常考觀念」與「易錯點提醒」

## 教學手冊內容規劃（必須全部涵蓋）

### 第一章：Spring Boot 4.x 概覽
- Spring Boot 4.x 的設計目標與核心理念
- 與 Spring Boot 3.x 的定位差異
- Spring 生態系版本對齊說明（Spring Framework、Spring Security、Spring Data）

### 第二章：Spring Boot 3.x → 4.x 升版總覽
- 官方升版策略說明
- 升版路徑建議（是否需先停留在 3.x 最新版）
- 升版風險評估清單（Checklist）

### 第三章：Java 與 JVM 版本要求變更
- Spring Boot 4.x 支援的 Java 版本
- 為何淘汰舊版 Java
- 對企業系統的實際影響
- 認證考試常見 Java 升版觀念

### 第四章：Spring Framework 核心變更
- Spring Framework 主要破壞性變更（Breaking Changes）
- Bean Lifecycle、Context 初始化差異
- 常見相容性問題與解法

### 第五章：Spring Web / REST API 變更
- Spring MVC / WebFlux 行為調整
- Request / Response 綁定與驗證差異
- 錯誤處理（Exception Handling）最佳化建議

### 第六章：Spring Security 重大調整
- Security 預設行為變更
- Authorization / Authentication 架構調整
- 舊版設定方式的淘汰與替代方案
- 升版時最容易踩雷的 Security 問題

### 第七章：Spring Data 與資料存取層
- JPA / JDBC / R2DBC 行為差異
- Repository API 是否有破壞性調整
- 交易管理（Transaction）注意事項

### 第八章：設定檔與組態管理變更
- application.yml / properties 行為變化
- Auto Configuration 調整重點
- Cloud Native 設定建議

### 第九章：Observability 與 Monitoring
- Logging、Metrics、Tracing 新趨勢
- 與 OpenTelemetry / Micrometer 的整合方向
- 企業實務監控建議

### 第十章：測試與品質保證
- Spring Boot Test 行為變更
- 測試失敗常見原因
- 升版時的測試策略

### 第十一章：企業升版實戰流程
- 升版前準備事項
- PoC 與試點升級策略
- Rollback 與風險控管
- CI/CD 升版建議流程

### 第十二章：認證考試重點整理
- Spring Boot 4.x 相關考試重點
- 常見陷阱題與觀念澄清
- 適合考前複習的章節整理

## 輸出品質要求
- 用詞精準、偏工程師語言
- 避免行銷式描述
- 清楚標示「Breaking Change」「必調整」「建議調整」
- 讓讀者能「看完就知道怎麼升版」

## 最終輸出
請輸出：
1. 完整教學手冊章節內容
2. 適合企業內訓使用的結構
3. 可直接交付給團隊使用的教學文件

## 產出結果
- 請產出一份 **《Spring boot 4.x升版教學》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Spring boot 4.x升版教學》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: "Spring boot 4.x升版教學.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
-------------------------------------------------------------------
# 資料轉置教學指引 
## 角色設定 - 你是資深軟體架構師和資深開發工程師 
## 背景 - 目前必需處理舊系統的資料轉置到新系統 
## 任務說明 舊系統的資料轉置到新系統教學手冊,從系統的分析,設計,資料如何轉置,資料如何驗證等流程的設計步驟與方法論,可以使用什麼工具等,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
------------------------------------------------------------------
# 系統資料轉置教學指引

## 🎯 使用目的
本 Prompt 用於請 AI 產生一份 **「舊系統資料轉置到新系統的完整教學手冊」**，適合大型企業、金融、核心系統專案使用，提供系統分析師與工程師作為實務指引。

## 🧑‍💻 角色設定（Role）

你是一位 **資深軟體架構師與資深資料工程師**，具備多年大型企業系統、金融系統與核心系統（Core System）  
**資料轉置（Data Migration / Data Transformation）** 的實戰經驗。

## 📘 教學手冊目標（Objectives）

請產出一份完整的教學手冊，協助團隊：

- 正確理解資料轉置的 **全生命週期**
- 降低資料錯誤、遺失、語意錯誤的風險
- 建立 **可重複、可驗證、可回溯** 的轉置流程
- 作為內部教育訓練與專案執行標準參考文件

## 👥 讀者對象與背景假設（Audience & Assumptions）

### 讀者具備能力
- 基本程式設計能力（Java / Python / SQL 任一）
- 熟悉關聯式資料庫（Oracle / DB2 / PostgreSQL / SQL Server）

### 系統背景
- **舊系統可能為**
  - Mainframe / COBOL
  - 舊版 RDBMS
  - 檔案系統（CSV / 固定長度檔 / TXT）
- **新系統可能為**
  - 現代化單體或微服務系統
  - 正規化 / 半正規化資料模型
  - 支援 Batch / API / Event-driven 架構

## 🧭 教學手冊章節結構（請完整展開）

### 第 1 章：資料轉置整體概念與常見失敗原因
- Data Migration vs Data Transformation 差異
- 為何資料轉置是高風險專案
- 常見失敗原因與風險分析

### 第 2 章：舊系統分析（As-Is Analysis）
- 資料來源盤點（DB / 檔案 / 外部系統）
- 資料結構分析（Table / File Layout）
- Key 與邏輯關聯分析
- 資料品質檢測（Null、重複、異常值）

### 第 3 章：新系統設計（To-Be Design）
- 新系統資料模型設計原則
- 舊欄位 → 新欄位 Mapping 規則
- Code / Enum / Reference Data 對應策略
- 歷史資料保留與否的決策考量

### 第 4 章：資料轉置策略與架構設計
- 一次性轉置 vs 分批轉置
- Online vs Batch
- Big Bang vs Parallel Run
- Rollback 與 Re-run 設計

### 第 5 章：資料轉置流程設計（ETL Flow）
- Extract（資料抽取）
- Transform（資料轉換）
- Load（資料載入）
- Staging Table 設計
- Error Handling 與 Retry 機制

### 第 6 章：資料驗證與比對機制（Critical）
- 筆數驗證（Record Count）
- 金額 / 數值驗證（Sum / Balance Check）
- Key-based 資料比對
- 抽樣驗證（Sampling）
- 自動化驗證報表設計

### 第 7 章：工具與技術選型建議
- SQL / Stored Procedure
- ETL 工具（Talend、Informatica、Airflow）
- 程式語言（Java / Spring Batch / Python）
- 檔案處理工具
- 驗證與測試輔助工具

### 第 8 章：測試策略與上線前檢核
- Unit Test（轉換邏輯）
- Integration Test（流程驗證）
- UAT 驗證模式
- 上線前 Checklist

### 第 9 章：實務經驗與最佳實踐（Best Practices）
- 常見踩雷案例
- 與業務單位的資料驗證合作方式
- 文件化、稽核與可追溯性設計
- 金融與核心系統常見合規考量

## ✍️ 撰寫風格與輸出要求（Writing Guidelines）

- 使用條列式與結構化說明
- 強調「實務經驗 + 架構思維」
- 可使用：
  - 表格
  - 流程圖描述
  - 偽程式碼（Pseudo Code）
- 避免過度學術化，聚焦專案可落地性

## 產出結果
- 請產出一份 **《系統資料轉置教學指引》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《系統資料轉置教學指引》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\指引\設計開發\ 目錄下,檔名為: "系統資料轉置教學指引"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
----------------------------------------------------------------
# Cobol教學手冊
## 角色設定 - 你是資深軟體架構師和Cobol資深開發工程師 
## 背景 - 目前必需使用Cobol語言開發主機上的系統
## 任務說明 - 系統必需使用Cobol語言開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-----------------------------------------------------------------
# 任務：產生 COBOL 教學手冊（Markdown）
## 角色設定
你是一位「資深主機系統架構師」與「資深 COBOL 開發工程師」，  
具備以下經驗：
- 10 年以上大型主機（Mainframe）系統開發與維運經驗
- 熟悉 COBOL（Enterprise COBOL / GnuCOBOL）
- 熟悉批次系統（Batch）、線上交易（Online / CICS）、檔案處理（VSAM / Sequential File）
- 熟悉金融、保險、政府或大型企業核心系統架構
- 擅長將複雜主機概念用「工程師可理解」的方式說明

## 背景說明
- 公司目前**必須使用 COBOL 語言開發主機系統**
- 系統屬於**長期維運型核心系統**
- 使用對象包含：
  - 新進工程師（不熟 COBOL）
  - 有 Java / C / Python 背景但沒碰過主機的工程師
  - 需要快速上手維護既有 COBOL 系統的同仁

## 教學手冊目標
請產出一份：
- **實務導向**
- **可直接給同仁閱讀與使用**
- **Markdown（.md）格式**
- **結構清楚、可長期維護**

的「COBOL 教學手冊」。

## 教學手冊內容需求（請完整涵蓋）

### 1️⃣ COBOL 與主機系統概覽
- 為什麼 COBOL 至今仍被大量使用
- COBOL 在大型主機系統中的角色
- Batch 系統 vs Online 系統（CICS）
- COBOL 與資料庫（DB2）/ 檔案系統的關係

### 2️⃣ COBOL 程式基本結構
- COBOL Program Structure
  - IDENTIFICATION DIVISION
  - ENVIRONMENT DIVISION
  - DATA DIVISION
  - PROCEDURE DIVISION
- 每個 DIVISION 的用途與常見寫法
- 基本程式範例（可編譯）

### 3️⃣ 資料型態與資料結構
- PIC 語法完整說明
- 數值型、文字型、符號位（SIGN）
- REDEFINES / OCCURS
- Working-Storage vs Linkage Section
- 常見錯誤與陷阱

### 4️⃣ 檔案處理（主機實務重點）
- Sequential File 基本操作
- READ / WRITE / OPEN / CLOSE
- EOF 控制寫法
- 檔案 Layout（Record Layout）設計原則
- 實務範例（Batch 檔案讀寫）

### 5️⃣ 批次程式（Batch Job）設計
- Batch 程式生命週期
- Return Code（RC）設計原則
- 程式錯誤處理與異常控制
- 批次程式撰寫範例
- 可維運的 Batch 設計 Best Practice

### 6️⃣ 與資料庫（DB2）互動（概念層級）
- Embedded SQL 基本概念
- SELECT / INSERT / UPDATE / DELETE 範例
- SQLCODE / SQLSTATE 處理方式
- 主機系統中資料一致性的觀念（Commit / Rollback）

### 7️⃣ COBOL 程式設計規範（非常重要）
- 命名規則（Program / Variable / Paragraph）
- 排版與可讀性原則
- 註解撰寫建議
- 避免「維護地獄」的寫法
- 常見 Anti-pattern

### 8️⃣ 舊系統維護與現代化觀點
- 如何「讀懂」舊 COBOL 程式
- 如何安全修改老程式
- 與現代系統（Java / API / MQ）整合概念
- COBOL 在未來系統中的定位

### 9️⃣ 新手常見問題（FAQ）
- 為什麼 COBOL 看起來這麼冗長？
- 為什麼不用改成 Java？
- 初學者最容易踩的雷
- 如何有效學習與除錯 COBOL


## 輸出格式要求
- 使用 **Markdown（.md）**
- 標題層級清楚（#、##、###）
- 程式碼請使用 Markdown code block
- 內容請以「教學手冊」語氣撰寫
- 適度加入「實務提醒」、「注意事項」、「最佳實務」

## 風格要求
- 專業、務實、不空談
- 以「資深工程師帶新人的口吻」撰寫
- 偏重「實際會遇到的主機系統問題」
- 適合長期作為公司內部技術文件

## 產出結果
- 請產出一份 **《Cobol教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Cobol教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為: "Cobol教學手冊"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。
-------------------------------------------------------------
# COBOL 教學手冊(2)

## 角色與背景設定

你是一位擁有 20 年以上經驗的資深軟體架構師和 COBOL 專家，專精於大型主機系統開發。你需要為團隊成員撰寫一份完整的 COBOL 教學手冊，幫助他們快速上手並掌握在主機環境下使用 COBOL 進行系統開發。

## 目標讀者

- 具備基礎程式設計經驗的開發人員
- 需要轉換到主機 COBOL 開發的工程師
- 團隊新進成員

## 教學手冊需求

### 1. 內容結構要求

請按照以下章節架構生成完整的教學手冊：

#### 第一章：COBOL 概述
- COBOL 歷史與發展
- COBOL 在現代企業系統中的角色
- COBOL 與其他語言的比較
- 主機環境介紹（IBM z/OS 或類似環境）

#### 第二章：開發環境設置
- 主機連線與登入
- TSO/ISPF 基本操作
- JCL (Job Control Language) 基礎
- 開發工具介紹（編輯器、編譯器、除錯工具）

#### 第三章：COBOL 語法基礎
- 程式結構（IDENTIFICATION、ENVIRONMENT、DATA、PROCEDURE DIVISION）
- 資料型別與變數宣告
- PICTURE 子句詳解
- LEVEL 編號系統（01-49, 66, 77, 88）

#### 第四章：基本程式設計
- 資料處理（MOVE、COMPUTE、ADD、SUBTRACT、MULTIPLY、DIVIDE）
- 條件判斷（IF-THEN-ELSE、EVALUATE）
- 迴圈控制（PERFORM）
- 字串處理（STRING、UNSTRING、INSPECT）

#### 第五章：檔案處理
- 循序檔案（Sequential File）
- 索引檔案（INDEXED File / VSAM KSDS）
- 相對檔案（Relative File）
- 檔案操作（OPEN、READ、WRITE、REWRITE、DELETE、CLOSE）

#### 第六章：進階主題
- COPYBOOK 的使用與管理
- 副程式呼叫（CALL statement）
- 資料庫存取（DB2、IMS）
- CICS 交易處理基礎
- 錯誤處理與除錯技巧

#### 第七章：最佳實踐
- 程式碼撰寫規範
- 命名慣例
- 註解撰寫標準
- 效能優化建議
- 維護性考量

#### 第八章：實戰範例
- 簡單報表程式
- 檔案更新程式
- 批次處理程式
- 線上交易程式（CICS）

#### 附錄
- COBOL 保留字清單
- 常用 JCL 範例
- 錯誤訊息對照表
- 學習資源與參考文獻

### 2. 撰寫風格要求

- **清晰易懂**：使用淺顯的語言解釋技術概念
- **循序漸進**：從基礎到進階，遵循學習曲線
- **實例豐富**：每個概念都搭配完整的程式碼範例
- **註解詳細**：範例程式碼必須包含中文註解說明
- **實務導向**：提供真實開發場景的應用說明

### 3. 程式碼範例規格

每個範例程式碼都應包含：
- 完整可執行的 COBOL 程式碼
- 逐行中文註解
- 輸入/輸出範例
- 執行結果說明
- 常見錯誤提醒

### 4. 格式要求

- 使用 Markdown 格式
- 程式碼使用 \`\`\`cobol 語法高亮
- 適當使用表格整理資訊
- 重要概念使用粗體或引用框標示
- 章節之間清楚分隔

### 5. 特別注意事項

- 強調 COBOL 的欄位限制（第 7 欄開始、第 72 欄結束）
- 說明固定格式與自由格式的差異
- 提供主機環境特有的注意事項
- 包含編譯選項說明（CICS、DB2 等）
- 說明測試與除錯流程

內容應該：
1. 總字數至少 10,000 字以上
2. 包含至少 20 個完整的程式碼範例
3. 每章都有學習目標和重點摘要
4. 提供練習題目供學員自我評估
5. 包含故障排除（Troubleshooting）章節

## 額外考量

- 如果可能，請提供 VS Code 或其他現代 IDE 的 COBOL 開發環境設置建議
- 說明如何在 Windows 或 Mac 上進行 COBOL 學習（使用模擬器或雲端環境）
- 提供版本管理（Git）在 COBOL 專案中的應用建議

## 產出結果
- 請產出一份 **《Cobol教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Cobol教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為: "Cobol教學手冊(2).md"，並使用 Markdown 格式撰寫。
- 請分段回覆

**請基於以上需求，生成一份專業、完整、實用的 COBOL 教學手冊。**

-----------------------------------------------------------------
# C 語言教學手冊
## 角色設定 - 你是資深軟體架構師和C資深開發工程師 
## 背景 - 目前必需使用C語言開發主機上的系統
## 任務說明 - 系統必需使用C語言開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊
-----------------------------------------------------------------
# 請求:生成 C 語言系統開發教學手冊

## 角色定位
你是一位擁有 20 年以上經驗的資深軟體架構師和 C 語言專家,專精於系統層級開發。

## 目標讀者
- 具備基礎程式設計概念的工程師
- 需要快速上手 C 語言進行系統開發的團隊成員
- 有其他語言背景,轉換到 C 語言開發的工程師

## 教學手冊需求

### 內容結構
請建立一份完整的 Markdown 格式教學手冊,包含以下章節:

1. **C 語言基礎**
   - 資料型別與變數
   - 運算子與表達式
   - 控制流程(if/switch/loop)
   - 函數定義與呼叫

2. **記憶體管理**
   - 指標基礎與進階應用
   - 動態記憶體配置(malloc/calloc/realloc/free)
   - 記憶體洩漏預防
   - 常見陷阱與最佳實踐

3. **資料結構**
   - 陣列與字串處理
   - 結構體(struct)與聯合(union)
   - 鏈結串列
   - 堆疊與佇列實作

4. **系統程式設計**
   - 檔案 I/O 操作
   - 錯誤處理機制
   - 多檔案專案組織
   - Makefile 使用

5. **進階主題**
   - 函數指標
   - 前置處理器與巨集
   - 位元操作
   - 多執行緒基礎(pthread)

6. **開發規範與最佳實踐**
   - 命名規範
   - 程式碼風格指南
   - 除錯技巧
   - 效能優化建議

### 格式要求
- 使用 Markdown 格式
- 每個概念提供完整的程式碼範例
- 加入常見錯誤示範與正確寫法對比
- 提供實用的程式碼模板
- 包含檢查清單(checklist)供團隊參考

### 特殊需求
- 著重於主機系統開發情境
- 強調記憶體安全與資源管理
- 提供可直接複製使用的程式碼片段
- 包含實際專案範例

請生成這份教學手冊,確保內容專業、實用且易於理解。

## 產出結果
- 請產出一份 **《C語言教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《C語言教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為: "C語言教學手冊"，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------------------------------
# C++教學手冊
## 角色設定 - 你是資深軟體架構師和C++資深開發工程師 
## 背景 - 目前必需使用C++語言開發主機上的系統
## 任務說明 - 系統必需使用C++語言開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔

----------------------------------------------------------------
# 請求AI生成C++教學手冊的Prompt

請以資深軟體架構師和C++資深開發工程師的角色,為我們團隊創建一份完整的C++教學手冊。

## 背景資訊
- **目標讀者**: 需要使用C++開發主機系統的開發團隊成員
- **技術層級**: 涵蓋從基礎到進階的內容
- **應用場景**: 主機系統開發(高效能、可靠性、系統級程式設計)

## 教學手冊需求

### 1. 內容結構
請包含以下章節:
- C++基礎語法與概念
- 物件導向程式設計(OOP)
- 記憶體管理(指標、智慧指標、RAII)
- STL標準模板庫(容器、演算法、迭代器)
- 現代C++(C++11/14/17/20/23新特性)
- 多執行緒與並行程式設計
- 效能優化與最佳實踐
- 系統開發常見模式與架構
- 錯誤處理與除錯技巧
- 程式碼品質與可維護性

### 2. 每個章節應包含
- 清晰的概念說明
- 實用的程式碼範例(附註解)
- 常見陷阱與注意事項
- 最佳實踐建議
- 實際應用場景

### 3. 格式要求
- 使用Markdown格式
- 程式碼使用適當的語法高亮標記
- 重點內容使用適當的強調格式
- 包含目錄(Table of Contents)
- 章節之間邏輯清晰、循序漸進

### 4. 特別強調
- 主機系統開發的特殊需求(如效能、穩定性、資源管理)
- 企業級開發的程式碼規範
- 團隊協作的最佳實踐
- 可維護性與可擴展性的設計原則

### 5. 附加需求
- 提供快速參考(Quick Reference)章節
- 包含推薦的開發工具與環境設定
- 提供延伸學習資源

請產生一份完整、專業、實用的C++教學手冊,以Markdown格式輸出。

## 產出結果
- 請產出一份 **《C++語言教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《C++語言教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\程式語言\ 目錄下,檔名為: "C++語言教學手冊"，並使用 Markdown 格式撰寫。
- 請分段回覆
- 請直接輸出完整教學手冊內容，不需要再詢問確認。

-------------------------------------------------------------------

# JQuery教學手冊
## 角色設定 - 你是資深軟體架構師和JQuery資深開發工程師 
## 背景 - 目前必需使用JQuery開發web application的系統
## 任務說明 - 系統必需使用JQuery 最新版開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔

-------------------------------------------------------------------
# jQuery教學手冊產生

## 角色設定
你是一位 **資深軟體架構師** 與 **jQuery 資深開發工程師**，具備多年企業級 Web Application 開發與維運經驗，熟悉 jQuery 最新版本（4.0+）、瀏覽器相容性、效能最佳化、安全性與現代前端架構整合。

## 背景說明
目前系統 **必須使用 jQuery 最新版**,4.0.0版 開發 Web Application，  
系統多為既有專案或大型企業系統，需兼顧：
- 可維護性
- 可讀性
- 與既有後端（如 Java / Spring / REST API）整合
- 與現代前端技術（ES6、模組化、CSS Framework）共存
- 可參考:https://jquery.com/

本教學手冊主要對象為：
- 有 JavaScript 基礎的工程師
- 需要在專案中「正確且長期維運地使用 jQuery」的同仁

## 任務說明
請產生一份 **完整、結構化、實務導向的 jQuery 教學手冊**，並以 **Markdown（.md）格式輸出**，內容需可直接作為內部技術文件使用。

## 教學手冊內容需求
請至少包含以下章節（可依需要擴充）：

### 1. jQuery 簡介與定位
- jQuery 的核心理念
- 為何在現代系統中仍需要 jQuery
- jQuery 與原生 JavaScript（Vanilla JS）的差異
- 適合使用 jQuery 的情境 vs 不適合的情境

### 2. 環境準備與版本建議
- jQuery 最新穩定版本說明
- CDN 與本地安裝方式
- 與 HTML5 / ES6 的搭配注意事項
- 瀏覽器相容性說明

### 3. jQuery 核心語法與觀念
- `$()` 選擇器原理
- 常用 Selector（ID / Class / Attribute / Traversing）
- Chaining 設計模式
- jQuery Object vs DOM Object

### 4. DOM 操作實戰
- 元素新增 / 刪除 / 修改
- Class 與 Style 操作
- 表單欄位處理
- 動態畫面更新的最佳實務

### 5. 事件處理（Events）
- on / off / one 的正確使用方式
- Event Delegation（事件代理）
- 常見錯誤與效能陷阱
- 與動態 DOM 搭配的事件設計

### 6. Ajax 與後端整合
- `$.ajax`, `$.get`, `$.post`
- JSON 資料處理
- 與 RESTful API 整合
- 錯誤處理與 Timeout 設計
- 與後端（如 Spring Boot）的實務範例

### 7. 模組化與程式碼結構建議
- jQuery 在大型專案中的結構設計
- 命名空間（Namespace）技巧
- 避免全域污染的寫法
- 可維護的檔案與目錄結構建議

### 8. 效能與最佳實務（Best Practices）
- Selector Cache
- 減少 DOM 操作次數
- 事件綁定最佳化
- 常見 Anti-patterns

### 9. 安全性注意事項
- XSS 風險與防範
- 使用 `.text()` vs `.html()`
- 與後端資料互動的安全建議

### 10. 與現代前端技術共存
- jQuery + Bootstrap / Tailwind
- jQuery 與 Vue / React 共存注意事項
- 逐步汰換 jQuery 的策略建議（如未來規劃）

### 11. 常見問題與除錯技巧
- Debug 技巧
- 常見錯誤整理
- Console 與開發工具使用方式

### 12. 實務範例與範本
- 常見功能範例（CRUD、表單驗證、列表更新）
- 可直接複製使用的程式碼範本

## 撰寫風格與格式要求
- 使用 **清楚的標題階層（# / ## / ###）**
- 程式碼請使用 Markdown code block
- 語氣專業、務實，偏向企業內部技術文件
- 以「為什麼要這樣寫」為導向，而不只是語法說明
- 適度加入 ⚠️ 注意事項 / ✅ 建議 / ❌ 常見錯誤

## 產出結果
- 請產出一份 **《Query教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Query教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: "Query教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
----------------------------------------------------------------
# Node.js生態系教學手冊
## 角色設定 - 你是資深軟體架構師和node.js生態系資深開發工程師 
## 背景 - 目前必需使用node.js生態系開發web application的系統
## 任務說明 - 系統使用node.js生態系最新版開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
----------------------------------------------------------------
# 任務：產生 Node.js 生態系教學手冊（Markdown）

## 你的角色設定
你是一位【資深軟體架構師】與【Node.js 生態系資深開發工程師】，
具備以下背景能力：
- 熟悉 Node.js 最新 LTS 版本（以目前官方建議版本為準）
- 熟悉現代 Web Application 架構與企業級系統設計
- 熟悉 JavaScript / TypeScript
- 熟悉前後端分離、API First、Cloud Native、Microservices 架構
- 熟悉 DevOps、CI/CD、安全性與效能最佳化

你的任務是為「企業內部開發同仁」撰寫一份 **可實際落地的 Node.js 生態系教學手冊**。

## 教學手冊目標讀者
- 具備基礎程式能力（Java / C# / Python / JS 皆可）
- 對 Node.js 有基本概念，但未必熟悉完整生態系
- 實際要參與 Web Application 或 Backend API 專案開發

## 教學手冊撰寫目標
- 以「**實務導向、架構導向、企業導向**」為主
- 不只是教語法，而是教 **怎麼用 Node.js 正確打造系統**
- 適合用作：
  - 新人訓練教材
  - 專案開發規範參考
  - 架構設計與技術選型依據

## 教學手冊輸出格式
- **請使用 Markdown（.md）格式**
- 使用清楚的標題階層（#、##、###）
- 適度使用：
  - 表格
  - 條列清單
  - 範例程式碼（請標註語言）
- 所有範例請以 **最新版 Node.js 生態系** 為基準

## 教學手冊內容大綱（請完整展開）

### 1. Node.js 與生態系總覽
- Node.js 是什麼？適合解決什麼問題？
- 與 Java / Spring Boot、Python / FastAPI 的差異
- Node.js 在企業系統中的常見使用場景
- 單體、微服務、Serverless 架構定位

### 2. Node.js 核心基礎
- Node.js 執行模型（Event Loop、Non-blocking I/O）
- CommonJS vs ES Modules
- NPM、Yarn、PNPM 生態比較
- 專案目錄結構最佳實務

### 3. TypeScript 在 Node.js 的標準用法
- 為什麼企業專案一定要用 TypeScript
- tsconfig 設計原則
- 型別設計與 Domain Model
- 常見反模式與避坑指南

### 4. Web Framework 生態系
- Express（歷史定位與限制）
- Fastify（高效能）
- NestJS（企業級主流）
- Framework 選型建議與比較表

### 5. RESTful API 與 Backend 架構設計
- Controller / Service / Repository 分層
- DTO、Validation、Error Handling 設計
- OpenAPI / Swagger 文件化
- Clean Architecture / Hexagonal Architecture 應用

### 6. 非同步處理與背景任務
- async / await 正確使用方式
- Queue（BullMQ / RabbitMQ / Kafka）
- 排程任務（cron）
- 長時間任務設計原則

### 7. 資料庫與 ORM / Query Builder
- PostgreSQL / MySQL / MongoDB 使用場景
- Prisma / TypeORM / Sequelize 比較
- Transaction、Migration、效能調校
- 連線池與資源管理

### 8. 快取與效能優化
- Redis 使用場景
- HTTP Cache / CDN
- Rate Limit
- Memory Leak 與效能監控

### 9. 安全性設計（非常重要）
- 身分驗證（JWT / OAuth2 / OIDC）
- API Security Best Practices
- 資料驗證與 Injection 防護
- Secrets 管理與環境變數設計

### 10. 測試策略
- 單元測試（Jest / Vitest）
- 整合測試（Supertest）
- Test Pyramid
- Mock / Stub 使用時機

### 11. Logging、Monitoring 與 Observability
- Logging 設計原則（Winston / Pino）
- Metrics 與 Tracing（OpenTelemetry）
- 錯誤追蹤（如 Sentry）
- 生產環境可觀測性設計

### 12. DevOps 與部署
- Node.js Build 與 Release 流程
- Docker 化最佳實務
- CI/CD Pipeline 設計
- Kubernetes / Cloud Run / Serverless 部署模式

### 13. 專案範本與團隊開發規範
- 企業級 Node.js 專案範本建議
- Coding Style 與 Lint 規範
- Git Flow / Branch Strategy
- Code Review 重點清單

### 14. 常見地雷與反模式
- 阻塞 Event Loop 的錯誤寫法
- Promise 使用錯誤
- TypeScript 濫用 any
- 設計不良的 API 與資料模型

### 15. 總結與最佳實務建議
- Node.js 在企業長期維運的關鍵成功因素
- 技術選型決策建議
- 學習路線與進階主題建議

## 撰寫風格要求
- 語氣專業、清楚、有條理
- 偏向「資深工程師帶團隊」的說明方式
- 不流於入門教科書，而是實戰與架構觀點

## 產出結果
- 請產出一份 **《Node.js生態系教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Node.js生態系教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: "Node.js生態系教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# 軟體開發的標準程序教學手冊
## 角色設定 - 你是資深軟體架構師和資深開發工程師 
## 背景 - 目前必需建立軟體開發的標準程序
## 任務說明 - 建立軟體開發的標準,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
---------------------------------------------------------------------------
# 軟體開發標準程序（Software Development Standard Process）教學手冊 生成 Prompt

## 你的角色設定
你是一位 **資深軟體架構師（Software Architect）與資深開發工程師（Senior Software Engineer）**，
擁有多年大型企業系統、金融系統、核心系統與雲端原生系統的實務經驗，
熟悉 SDLC、SSDLC、Clean Architecture、DevOps、CI/CD、資安規範與企業級治理。

你的任務是 **為企業建立一套可落地、可稽核、可持續改善的軟體開發標準程序**，
並將其整理成「教學手冊」形式，讓不同資歷的工程師都能依循。

## 背景說明
- 組織需要建立 **一致、標準化的軟體開發流程**
- 專案涵蓋：
  - 核心系統、Web 系統、API、批次系統
  - 單體架構與微服務架構
  - On-Premise、私有雲、混合雲
- 需符合：
  - 企業內控制度
  - 資安與稽核需求
  - 可維運、可交接、可擴充原則

## 產出目標
請產生一份 **「軟體開發標準程序教學手冊」Markdown（`.md`）檔案**，需符合以下要求：

### 一、文件整體要求
- 使用 **Markdown 格式**
- 條理清楚、章節分明
- 適合：
  - 新人培訓
  - 資深工程師對齊共識
  - 專案查核與流程稽核
- 內容偏向「實務可落地」，避免只有理論

### 二、建議章節結構（請完整展開）
請至少包含下列章節（可視需要補充）：

1. 前言與目的  
   - 為什麼需要軟體開發標準程序  
   - 對組織與工程師的價值  

2. 軟體開發生命週期（SDLC）總覽  
   - 各階段說明
   - 與實務專案的關係  

3. 需求管理（Requirements Engineering）
   - 需求來源與分類（業務 / 法規 / 技術）
   - 功能性與非功能性需求
   - 需求文件標準（BRD / FRD / SRD）
   - 需求異動管理流程  

4. 系統分析與設計
   - 系統架構設計原則
   - 邏輯架構 / 實體架構
   - API 設計規範
   - 資料庫設計與資料治理
   - 非功能性設計（效能、可用性、資安）  

5. 開發實作規範
   - 程式碼風格與命名規範
   - 架構分層原則
   - 重用性與模組化
   - Secure Coding 基本原則  

6. 測試策略與品質保證
   - 測試類型（Unit / Integration / System / UAT）
   - 測試責任分工
   - 測試資料管理
   - 缺陷（Bug）管理流程  

7. 版本控制與組態管理
   - Git 分支策略
   - 版號管理原則
   - 設定檔與環境管理  

8. CI/CD 與部署流程
   - 自動化建置流程
   - 部署策略（Blue-Green / Rolling）
   - 回滾（Rollback）與風險控管  

9. 資安與 SSDLC
   - 安全需求納入時機
   - 程式碼掃描與弱點管理
   - 權限、稽核與日誌  

10. 上線、維運與監控
    - 上線檢核清單
    - 監控與告警
    - 問題處理與 RCA  

11. 文件化與知識交接
    - 必備文件清單
    - 文件維護責任  

12. 持續改善與流程治理
    - 專案回顧（Post-mortem）
    - 指標與成熟度模型
    - 流程優化建議  

### 三、寫作風格要求
- 使用 **專業但清楚的工程語言**
- 適度搭配：
  - 條列清單
  - 表格（Markdown Table）
  - 實務提醒（Best Practice / 注意事項）
- 避免空泛口號，偏向「怎麼做」

### 四、輸出格式
- 僅輸出 **Markdown 內容**
- 不需額外解說 Prompt 本身
- 文件可直接另存為 `.md` 使用

## 產出結果
- 請產出一份 **《軟體開發標準程序（Software Development Standard Process）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《軟體開發標準程序（Software Development Standard Process）教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\指引\設計開發\ 目錄下,檔名為: "軟體開發標準程序（Software Development Standard Process）教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------
# 軟體開發的平行測試的標準程序與平行測試計劃書教學手冊 
## 角色設定 - 你是資深軟體架構師和資深開發工程師,同時也是資深專案PM 
## 背景 - 目前必需平行測試的標準程序與平行測試計劃書 
## 任務說明 - 建立軟體開發平行測試的標準程序與平行測試計劃書,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔

--------------------------------------------------------------
# 軟體開發平行測試（Parallel Run / Parallel Testing）標準程序與計劃書教學手冊

## 角色設定
你是一位：
- 資深軟體架構師
- 資深開發工程師
- 資深專案經理（PM）
- 熟悉大型企業與金融系統導入專案
- 熟悉 SSDLC（Secure Software Development Life Cycle）
- 熟悉 ISO 27001、內控、稽核與風險控管

你的任務是撰寫一份 **企業級教學手冊（Markdown 格式）**，
作為公司平行測試的標準作業指引（SOP）與計劃書範本。

# 🎯 文件產出要求

請產出：

- 完整 Markdown 格式
- 可直接作為公司內部標準文件
- 內容包含：
  - 標準程序（SOP）
  - 計劃書範本（Template）
  - 管控機制
  - 風險管理
  - 成功判定標準
  - 稽核與軌跡留存要求
  - 實務案例說明
  - 表格範本

# 📘 文件必須包含以下章節

# 1️⃣ 平行測試概論

- 什麼是平行測試（Parallel Run）
- 與 UAT / SIT / Regression Test 差異
- 適用場景：
  - 核心系統轉換
  - 舊系統下線
  - 批次系統重寫
  - 金融交易系統
- 平行測試的目標
- 平行測試成功的關鍵因素

# 2️⃣ 平行測試標準作業流程（SOP）

請用流程圖概念條列說明：

1. 平行測試評估
2. 測試範圍定義
3. 測試資料準備
4. 測試環境建置
5. 平行執行
6. 差異比對
7. 差異分析
8. 修正與重測
9. 結案判定
10. 切換上線決策

並說明：

- 每階段負責角色（RACI）
- 產出文件
- 風險點
- 控制點

# 3️⃣ 平行測試計劃書範本（完整模板）

請提供可直接使用的標準模板，包含：

## 3.1 專案基本資訊
- 專案名稱
- 系統名稱
- 測試期間
- 負責人

## 3.2 測試範圍
- 功能範圍
- 批次範圍
- 交易範圍
- 不納入範圍

## 3.3 測試策略
- 同步方式（Real-time / Batch）
- 資料來源
- 比對方式（欄位級、總額級、筆數級）
- 自動化工具

## 3.4 測試資料設計
- 全量測試 / 抽樣測試
- 邊界值
- 異常資料
- 高風險交易

## 3.5 差異判定標準
- 容忍誤差（Tolerance）
- 可接受差異
- 必須修正差異

## 3.6 風險評估
- 技術風險
- 業務風險
- 法規風險
- 資安風險

## 3.7 成功標準（Exit Criteria）

# 4️⃣ 差異比對設計

請說明：

- 欄位比對
- 數值容差設計
- 浮點數誤差處理
- 日期與時區差異
- BigDecimal 精度問題
- 金額四捨五入差異

並提供：

- SQL 比對範例
- 批次比對邏輯範例
- API 回傳比對範例

# 5️⃣ 自動化平行測試設計

請說明：

- 比對自動化架構
- CI/CD 整合
- 測試報表產出
- 差異自動分類
- 日誌與追蹤機制

# 6️⃣ 金融系統平行測試實務案例

請設計一個：

「銀行核心帳務系統升級平行測試案例」

內容包含：

- 測試週期規劃
- 批次日結流程
- 差異處理流程
- 高風險交易監控
- 上線決策會議

# 7️⃣ 風險管理與內控設計

包含：

- 分權機制
- 雙人覆核
- 日誌保存
- 稽核需求
- 法遵要求
- ISO 27001 對應

# 8️⃣ 常見錯誤與失敗案例分析

- 平行時間太短
- 測試資料不完整
- 忽略例外交易
- 沒有定義容忍誤差
- 沒有設計回滾計畫

# 9️⃣ 標準表單範本（請提供表格）

- 差異記錄表
- 風險評估表
- 上線核准單
- 測試每日報表
- 問題追蹤清單

# 🔟 企業級最佳實踐（Best Practice）

- 平行測試至少 N 個週期
- 高風險系統建議全量比對
- 自動化比對比例 ≥ 90%
- 必須保留完整稽核軌跡

# 📌 文件格式要求

- 使用清楚標題
- 使用表格
- 使用條列式說明
- 適合企業培訓教材
- 可直接納入公司標準流程文件
- 請以繁體中文撰寫
- 產出完整 Markdown 檔案內容

## 產出結果
- 請產出一份 **《軟體開發平行測試（Parallel Run / Parallel Testing）標準程序與計劃書教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《軟體開發平行測試（Parallel Run / Parallel Testing）標準程序與計劃書教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\指引\專案管理\ 目錄下,檔名為: "軟體開發平行測試（Parallel Run / Parallel Testing）標準程序與計劃書教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
---------------------------------------------------------------
# RWD教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - RWD（Responsive Web Design，響應式網頁設計）是一種現代網頁設計技術，透過彈性網格、圖片與 CSS 媒體查詢，讓網站內容能自動偵測裝置螢幕尺寸（桌機、平板、手機），調整版面配置與內容呈現，提供最佳視覺與瀏覽體驗，只需維護一組網址與代碼。 
## 背景 - 目前必需使用RWD開發web application的系統。 
## 任務說明 - 系統必需使用RWD最新版開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
-----------------------------------------------------------------
# RWD（Responsive Web Design）企業級教學手冊產生任務

## 角色設定
你是一位：
- 資深軟體架構師
- 資深前端工程師（精通 HTML5 / CSS3 / JavaScript / TypeScript）
- 熟悉現代前端框架（Vue 3 / React）
- 熟悉 Tailwind CSS / Bootstrap 5
- 熟悉大型企業級 Web Application 架構設計
- 熟悉可維護性、可擴展性、可測試性設計原則

請用「企業級教學手冊」的標準來撰寫內容。

## 技術背景說明

RWD（Responsive Web Design）是一種透過：
- 彈性網格（Flexible Grid）
- 彈性圖片（Flexible Media）
- CSS Media Queries
- 現代 CSS（Flexbox / Grid）
- Mobile-First 設計策略

來讓網站適應不同裝置（Desktop / Tablet / Mobile）的設計方法。

目標：
- 一組程式碼
- 一組網址
- 支援所有裝置
- 提供最佳使用者體驗（UX）
- 使用最新版本說明

## 任務目標

請產生一份：

✅ 給企業內部工程師使用  
✅ 可作為標準開發規範  
✅ 適合大型 Web Application 系統  
✅ Markdown（.md）格式完整教學手冊  

# 教學手冊內容必須包含

請完整產出以下章節，內容需深入、專業、可實戰：

# 1️⃣ RWD 核心概念

- 為什麼需要 RWD？
- RWD vs Adaptive Design 差異
- Mobile First 設計哲學
- UX 與效能考量
- SEO 對 RWD 的影響

# 2️⃣ RWD 技術基礎

## 2.1 Viewport 設定
- meta viewport 說明
- 實務範例

## 2.2 Flexible Layout
- 百分比
- rem / em
- vw / vh
- clamp()

## 2.3 CSS Media Queries
- 語法
- 常見 breakpoint 設計策略
- 企業建議 breakpoint 規範表

## 2.4 Flexbox 詳解
- 主軸/交叉軸
- 常見 Layout Pattern

## 2.5 CSS Grid 詳解
- grid-template
- auto-fit / auto-fill
- 真實案例

# 3️⃣ 現代 RWD 架構設計（企業級）

- Layout 分層設計
- Header / Sidebar / Content 響應式設計
- Dashboard 響應式實務
- 表單 RWD 設計策略
- 表格（Data Table）在手機的處理方式
- Modal / Drawer 在不同裝置設計

# 4️⃣ 與現代框架整合

## 4.1 Vue 3 + RWD
- 組件化 RWD 設計
- Composition API 與 Layout 管理
- 動態偵測螢幕尺寸

## 4.2 Tailwind CSS 響應式設計
- sm/md/lg/xl/2xl 使用方式
- Mobile First 設計
- 實戰範例

## 4.3 Bootstrap 5 Grid System
- container / row / col
- Breakpoint 系統解析

# 5️⃣ 圖片與媒體最佳化

- Responsive Image（srcset / sizes）
- Picture 元素
- WebP/AVIF
- Lazy Loading
- 效能優化策略

# 6️⃣ RWD 效能優化

- 減少重排（Reflow）
- 減少重繪（Repaint）
- Critical CSS
- 避免不必要的 Media Query
- Lighthouse 指標優化

# 7️⃣ 常見錯誤與反模式

- 固定寬度設計
- 使用 px 當作主要單位
- 忽略可點擊範圍
- 忽略觸控裝置
- 表格未優化
- 字體過小

# 8️⃣ 企業級 RWD 開發標準規範

請制定：

- Breakpoint 標準
- 命名規範
- Layout 架構規範
- 元件設計原則
- Code Review 檢查清單
- UI/UX 檢核表

# 9️⃣ 測試與驗證

- Chrome DevTools 模擬
- 真機測試
- 自動化測試建議
- 視覺回歸測試（Visual Regression）

# 🔟 範例專案（完整實戰範例）

請提供：
- 一個完整 Dashboard Layout 範例
- 手機版展開 Sidebar
- 表格在手機變為卡片式顯示
- 使用 Flexbox + Media Query

請提供可直接執行的 HTML + CSS 範例。

# 文件輸出要求

- 使用 Markdown 格式
- 使用清楚的章節結構
- 提供實際程式碼範例
- 提供架構圖（使用文字圖）
- 內容需深入（適合資深工程師）
- 不可僅止於入門教學
- 必須具備企業級思維

## 產出結果
- 請產出一份 **《RWD（Responsive Web Design）企業級教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《RWD（Responsive Web Design）企業級教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: "RWD（Responsive Web Design）企業級教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Tailwind CSS教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Tailwind CSS 是一個以「實用優先」（Utility-First）為核心理念的開源 CSS 框架。它不提供預設的 UI 元件（如按鈕或導覽列），而是提供大量原子化的 CSS 類別（Class），讓開發者直接在 HTML 中組合出獨特的設計。  
## 背景 - 目前必需使用Tailwind CSS開發web application的系統。 
## 任務說明 - 系統必需使用Tailwind CSS最新版開發,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
-------------------------------------------------------------------
# Tailwind CSS 教學手冊（企業級 Web Application 版本）

## 角色設定
你是一位：
- 資深軟體架構師
- 資深前後端開發工程師
- 具有大型企業級系統開發經驗
- 熟悉 Vue 3、TypeScript、微前端架構
- 熟悉設計系統（Design System）與前端工程化

請以「企業內部技術教學手冊」的標準撰寫內容。

---

## 技術背景

Tailwind CSS 是一個 Utility-First CSS Framework。
本專案要求：

- 必須使用 Tailwind CSS 最新穩定版本
- 必須符合企業級大型專案開發標準
- 使用最新版說明
- 需可整合：
  - Vue 3+
  - Angular 19+
  - TypeScript
  - Vite
  - 微前端架構
  - Design System
  - CI/CD 流程
  - 多語系系統
  - 深色模式（Dark Mode）
  - RWD 響應式設計

## 目標

請產出一份完整的「Tailwind CSS 教學手冊.md」檔案內容。

輸出格式必須為：

- 純 Markdown
- 使用清楚的階層式目錄
- 每一章節需包含：
  - 原理說明
  - 架構說明
  - 實務建議
  - 程式範例
  - 企業最佳實踐
  - 常見錯誤
  - 效能建議

## 教學手冊內容必須包含以下章節

# 1. 為什麼選擇 Tailwind CSS
- Utility-First 理念
- 與傳統 CSS / SCSS 比較
- 與 Bootstrap 比較
- 優缺點分析
- 適合的專案類型

# 2. 安裝與專案初始化
- 使用 Vite + Vue 3 安裝流程
- PostCSS 設定
- tailwind.config.js 說明
- content 掃描最佳實踐
- 專案目錄結構建議

# 3. Tailwind 核心概念
- Utility Classes
- Responsive Design
- State variants（hover, focus）
- Breakpoints
- Dark Mode
- Arbitrary Values
- JIT 原理說明

# 4. 設計系統（Design System）整合
- 建立自訂 theme
- colors 設計策略
- spacing 規範
- typography 設計
- 設計 token 管理
- 企業品牌色整合

# 5. 元件開發最佳實踐
- Button 設計範例
- Card 設計範例
- Form 設計範例
- Layout 設計範例
- 可維護性設計
- 如何避免 class 爆炸

# 6. 大型專案架構設計建議
- 與微前端整合方式
- Tailwind 與組件庫策略
- 可擴充性設計
- 團隊協作規範
- 命名規範建議

# 7. 效能優化
- Purge 機制
- Tree-shaking
- CSS 體積優化
- CDN vs 本地建置比較
- Production Build 注意事項

# 8. 與 Vue 3 + TypeScript 整合實戰
- 動態 class 綁定
- computed class 管理
- 條件式樣式設計
- 組件抽象化技巧

# 9. 常見錯誤與踩雷整理
- class 過多問題
- 重複樣式問題
- 無法維護的問題
- 與第三方 UI Library 衝突
- Dark mode 設計錯誤

# 10. 企業級最佳實踐總結
- 開發規範
- Code Review 建議
- 專案模板設計建議
- 可長期維護策略

## 撰寫風格要求

- 以技術架構師角度撰寫
- 強調「為什麼這樣做」
- 強調可維護性
- 強調大型系統觀點
- 不要只寫 API 說明
- 必須有完整程式範例

## 產出結果
- 請產出一份 **《Tailwind CSS教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Tailwind CSS教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\framework\ 目錄下,檔名為: "Tailwind CSS教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------------
# github copilot cli教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - GitHub Copilot CLI 是一款將 AI 輔助開發能力直接帶入終端機（Terminal）的工具，讓開發者無需離開命令列即可編寫、偵錯與理解程式碼。
## 背景 - 目前必需使用github copilot cli開發web application的系統。 
## 任務說明 - 系統必需使用github copilot cli最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,應用系統如何串接MCP,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
-----------------------------------------------------------------
# GitHub Copilot CLI 教學手冊產生任務

## 🎯 角色設定
你是一位：
- 資深軟體架構師
- 資深前後端開發工程師
- DevOps 專家
- 熟悉企業級系統導入與標準化流程
- 熟悉 AI 輔助開發（AI-assisted development）與 MCP（Model Context Protocol）

請以「企業級導入標準文件」的嚴謹程度撰寫教學手冊。

## 📌 背景說明

目前公司開發 Web Application 系統，必須：

- 使用 GitHub Copilot CLI 最新版
- 將 AI 輔助能力整合至終端機開發流程
- 導入標準化開發流程
- 與既有系統（GitHub、CI/CD、Container、MCP Server）整合
- 建立可維護、可升級、可治理的 AI 開發模式
- 參考: https://github.com/github/copilot-cli
- 使用最新版本說明

目標是建立一份可供內部工程師使用的標準教學手冊（Markdown 格式）。

## 📦 輸出要求

請產出：

- 完整 Markdown (.md) 教學手冊
- 結構清晰（目錄 + 章節）
- 包含架構圖（使用 mermaid）
- 包含範例指令
- 包含實務建議
- 包含企業導入風險控管建議
- 內容不可簡略，需達企業培訓等級
- 適用 Windows / macOS / Linux

# 📘 教學手冊必須包含以下章節

# 1️⃣ GitHub Copilot CLI 架構說明

- Copilot CLI 架構概念
- 與 GitHub Copilot (IDE 版本) 的差異
- AI 呼叫流程
- Token / API 認證流程
- CLI 與 GitHub 雲端服務關係
- CLI 在企業環境中的位置

請提供：

- 架構說明
- mermaid 架構圖

# 2️⃣ 安裝與環境建置

請包含：

- Windows 安裝方式
- macOS 安裝方式
- Linux 安裝方式
- Node.js 需求版本
- Git 需求版本
- 驗證安裝成功方式
- 代理伺服器（Proxy）環境設定
- 公司防火牆限制處理方式

# 3️⃣ 基本設定與認證

- GitHub 登入流程
- Token 產生方式
- 企業 GitHub 組織授權
- CLI config 設定說明
- 安全設定建議
- Token 週期管理建議

# 4️⃣ Web Application 開發應用方式

請以企業專案角度說明：

- 建立專案骨架
- 自動產生程式碼
- 解釋現有程式
- 重構建議
- 測試程式產生
- Dockerfile 產生
- CI/CD YAML 產生
- 安全性掃描輔助

請包含：

- 實際 CLI 指令範例
- 使用情境說明
- 團隊開發最佳實踐

# 5️⃣ 與 MCP (Model Context Protocol) 串接方式

請說明：

- MCP 架構概念
- CLI 如何串接 MCP Server
- 自訂工具（Tooling）設計方式
- 與企業內部 API 整合方式
- Context 管理方式
- 安全與權限控管

請提供：

- mermaid 架構圖
- CLI + MCP 串接範例

# 6️⃣ DevOps 整合模式

請說明：

- 與 GitHub Actions 整合
- 與 CI/CD Pipeline 整合
- 容器化開發流程
- AI 輔助 Code Review
- Pull Request 自動說明產生
- Commit message 產生最佳實務

# 7️⃣ 系統維護與治理

請包含：

- CLI 版本管理策略
- 企業升版流程
- AI 使用紀錄稽核建議
- 使用權限控管
- Token 失效處理
- 效能監控建議
- 成本控管建議

# 8️⃣ 系統升級策略

請說明：

- 升級流程標準程序
- 升級前測試流程
- 企業環境灰度升級建議
- 版本回滾策略
- 與 MCP 相容性驗證

# 9️⃣ 企業導入最佳實踐

請整理：

- 開發團隊使用規範
- AI 輔助開發風險
- 原始碼洩漏風險管理
- Prompt 設計標準化
- AI 產出程式碼審核流程
- 內部教育訓練建議

# 🔟 風險與限制說明

請說明：

- Copilot CLI 限制
- Token 限制
- Rate Limit
- 網路依賴風險
- 法規與合規性建議

# 📌 文件格式要求

- 必須為完整 Markdown
- 含目錄（自動目錄格式）
- 含程式碼區塊
- 含 mermaid 圖
- 不可簡略
- 適合直接放入公司 Git Repository

# 📎 額外要求

請用企業培訓手冊等級撰寫，內容具備：

- 清楚
- 架構化
- 可落地
- 可直接導入企業專案
- 提供實務建議而非理論說明

## 產出結果
- 請產出一份 **《github copilot cli教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《github copilot cli教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "github copilot cli教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Chrome DevTools 教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Chrome DevTools（Chrome 開發者工具）是直接內建在 Google Chrome 瀏覽器中的一組網頁製作與除錯工具。它能讓開發者即時編輯網頁、診斷問題，並協助優化網站效能。
## 背景 - 目前必需使用Chrome DevTools協助網頁製作與除錯,開發web application的系統。 
## 任務說明 - 系統必需使用Chrome DevTools最新版開發,包含系統架構,安裝,設定,系統使用,系統如何debug,診斷問題,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
-------------------------------------------------------------------
# Chrome DevTools 教學手冊產生指令

## 角色設定
你是一位資深軟體架構師、資深前端工程師、資深後端工程師，同時熟悉大型企業級 Web Application 架構設計與效能優化。

## 背景說明
目前團隊必須使用最新版 Chrome DevTools 協助 Web Application 開發、除錯與效能優化。
系統包含：
- 前端：HTML5 / CSS3 / JavaScript / TypeScript / Vue / React 等 SPA 架構
- 後端：RESTful API / Spring Boot / Node.js
- 部署架構：Nginx / API Gateway / CDN / 微服務架構
- DevOps：CI/CD / Docker / Kubernetes
- 請使用最新版本說明

本教學手冊將作為團隊標準技術文件與內部培訓教材。

## 任務要求

請產出一份 **完整、系統化、專業級的 Markdown 教學手冊 (.md 格式)**

必須包含以下內容：

# 📘 文件結構要求

## 第一章：Chrome DevTools 架構與核心原理
- DevTools 整體架構說明
- Browser 與 Rendering Pipeline
- DOM / CSSOM / Render Tree
- JavaScript Engine (V8) 運作原理
- Network Request Lifecycle
- DevTools 與 Chromium 架構關係

## 第二章：安裝與環境設定
- Chrome 最新版安裝
- 開啟 DevTools 的方式
- 常用快捷鍵整理（Windows / Mac）
- 常用設定（Theme / Docking / Workspace / Overrides）
- 與 VSCode 整合
- Source Map 設定
- Local Overrides 設定方式

## 第三章：Elements 面板完整教學
- DOM 即時編輯
- CSS 即時修改
- Box Model 分析
- Layout Debug
- Grid / Flexbox 視覺化工具
- 事件監聽器檢查
- 強制狀態（:hover / :active）

## 第四章：Console 深入教學
- console API 使用
- log / warn / error / table
- 斷言與除錯技巧
- 操作 DOM 的 console 技巧
- Performance 分析 console 技巧

## 第五章：Sources 面板（JS 除錯核心）
- 設定 Breakpoint
- Conditional Breakpoint
- XHR / Fetch Breakpoint
- Event Listener Breakpoint
- Watch 變數
- Call Stack 分析
- Async Stack Trace
- Blackbox Script
- Snippets 使用

## 第六章：Network 面板（API 與效能分析）
- Request/Response 結構
- Header / Payload 分析
- API Debug 技巧
- 模擬慢速網路
- Cache 行為分析
- HTTP/1.1 vs HTTP/2 分析
- WebSocket 除錯

## 第七章：Performance 面板（效能優化核心）
- Recording 操作
- FPS 分析
- Main Thread 分析
- Long Task 問題診斷
- Reflow / Repaint 分析
- Lighthouse 使用方式
- Core Web Vitals 分析

## 第八章：Memory 面板
- Heap Snapshot
- Allocation Timeline
- 記憶體洩漏診斷流程
- SPA 常見 Memory Leak 問題

## 第九章：Application 面板
- LocalStorage / SessionStorage
- IndexedDB
- Cookies
- Service Worker
- PWA Debug

## 第十章：Security 面板
- HTTPS 分析
- Mixed Content 問題
- CORS Debug
- CSP 分析

## 第十一章：企業級 Web Application Debug 標準流程
- 前端問題診斷流程
- API 錯誤排查流程
- 效能瓶頸診斷流程
- 記憶體問題診斷流程
- 生產環境 Debug 建議
- 團隊 Debug SOP

## 第十二章：最佳實踐與團隊規範
- 團隊使用規範
- Debug Checklist
- 效能優化 Checklist
- Code Review 與 DevTools 使用建議

# 📌 文件要求

1. 必須使用 Markdown 格式
2. 必須具備清楚標題階層（# / ## / ###）
3. 必須包含：
   - 圖解說明（以 mermaid 或 ASCII 圖示）
   - 表格整理
   - 實務案例
   - Debug 範例
4. 內容必須適合：
   - 初階工程師
   - 中階工程師
   - 架構師
5. 內容必須具備企業級思維，而非基礎教學而已
6. 使用最新版 Chrome DevTools 功能

## 產出結果
- 請產出一份 **《Chrome DevTools 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Chrome DevTools 教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Chrome DevTools 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

---

# 📌 額外要求

請在最後增加：

- 常見問題 FAQ
- 面試常考 DevTools 問題
- 團隊培訓建議
- 延伸學習資源

---

請輸出完整 Markdown 文件內容。
-----------------------------------------------------------------------
# Chrome DevTools mcp 教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Chrome DevTools MCP （模型上下文協定）是 Google 開發的伺服器。它允許 Claude、Cursor 或 Gemini CLI 等 AI 助理直接「看到」Chrome 瀏覽器並與之互動。這項技術使人工智慧能夠像人類工程師一樣使用開發工具，克服了人工智慧只能「查看靜態程式碼」的傳統限制。 
## 任務說明 - 系統必需使用Chrome DevTools MCP最新版協助AI開發,包含系統架構,系統安裝,設定,系統使用,系統維護,系統升級安裝,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生教學手冊 md 檔
-------------------------------------------------------------------
# Chrome DevTools MCP（Model Context Protocol）教學手冊

## 角色設定
你是一位：
- 資深軟體架構師
- 資深前端與後端工程師
- DevOps 與 AI 開發整合專家
- 熟悉 Chrome DevTools、MCP（Model Context Protocol）、LLM 工具整合

你的任務是撰寫一份**企業等級標準教學手冊**，提供開發團隊使用最新版 Chrome DevTools MCP 來協助 AI 開發。

## 技術背景說明

Chrome DevTools MCP 是 Google 提供的 MCP Server。
它允許 AI 助理（例如 Claude、Cursor、Gemini CLI 等）：

- 直接看到 Chrome 瀏覽器畫面
- 讀取 DOM 結構
- 操作 DevTools
- 分析 Network / Performance / Console
- 模擬使用者操作
- 自動偵錯前端應用程式

這突破了傳統 AI 只能查看靜態程式碼的限制。

## 目標讀者

- 前端工程師
- 全端工程師
- AI 工具整合工程師
- DevOps 工程師
- 架構師

讀者具備：
- Node.js 基礎
- Chrome DevTools 基礎
- CLI 操作能力
- 基本 AI 工具使用經驗

## 產出要求

請產生一份完整 Markdown (.md) 教學手冊，內容需包含：

# 一、總覽與架構設計

- MCP 是什麼？
- Chrome DevTools MCP 架構說明
- 系統元件圖
- AI ↔ MCP Server ↔ Chrome ↔ Web App 互動流程圖
- 適用場景說明
- 與傳統 AI 靜態分析比較

# 二、系統架構設計

請說明：

- 單機開發架構
- 團隊共享架構
- CI/CD 整合架構
- 雲端整合架構
- 安全隔離建議
- 權限控制建議
- 沙箱執行模式建議

請提供：

- 架構圖（文字圖示即可）
- Component 說明
- Port 說明
- 通訊流程說明

# 三、安裝與環境建置（最新版）

請說明：

- 系統需求
- Chrome 版本需求
- Node.js 版本需求
- 安裝步驟
- CLI 安裝方式
- 本地啟動方式
- Docker 安裝方式（如適用）
- 設定檔範例
- 啟動參數說明

請附：
- 指令範例
- 常見錯誤排除

# 四、設定與整合

請說明如何整合：

- Claude
- Cursor
- Gemini CLI
- 其他 MCP Client

說明：

- MCP 設定檔範例
- 權限設定
- Host 設定
- 安全限制
- Headless 模式設定

# 五、實戰使用教學

請提供實際案例：

1. 自動偵錯前端錯誤
2. 自動分析 Network 請求
3. 效能瓶頸分析
4. DOM 結構檢查
5. 自動化 UI 測試
6. 表單流程驗證
7. SPA 狀態追蹤

每個案例請包含：

- 問題場景
- AI 指令範例
- MCP 執行流程
- 結果說明
- 最佳實務建議

# 六、企業使用最佳實務

請說明：

- 安全控管
- 資料隱私保護
- 權限管理
- 日誌記錄
- 稽核機制
- 版本管理策略
- 團隊共用規範
- 與 SSDLC 整合建議

# 七、系統維護與監控

請說明：

- Log 管理
- 異常處理
- 連線監控
- 效能監控
- MCP Server 健康檢查
- Chrome crash 處理

# 八、升級與版本管理

請說明：

- 升級策略
- 版本相容性檢查
- 重大版本升級流程
- 回滾機制
- 企業環境升級 SOP

# 九、風險與限制

請說明：

- 安全風險
- AI 操作風險
- 權限濫用風險
- 資料洩漏風險
- Browser sandbox 限制
- 無法取代人工的部分

# 十、未來發展與延伸整合

請說明：

- 與 CI/CD 整合
- 與 Playwright 整合
- 與 Puppeteer 整合
- 與 E2E 測試框架整合
- 與可觀測性系統整合
- 未來 AI Agent 發展方向

## 文件風格要求

- 使用專業企業級文件風格
- 條列清楚
- 架構完整
- 可直接作為內部標準文件
- 使用清楚章節編號
- 每章節包含「設計建議」
- 每章節包含「實務建議」

## 重要要求

- 使用最新版 Chrome DevTools MCP
- 不要使用過時資訊
- 提供完整架構觀念
- 提供企業等級建議
- 文件長度需完整且深入
- 使用 Markdown 格式輸出
- 內容可直接儲存為 .md 檔

## 產出結果
- 請產出一份 **《Chrome DevTools MCP（Model Context Protocol）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Chrome DevTools MCP（Model Context Protocol）教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\工具\ 目錄下,檔名為: "Chrome DevTools MCP（Model Context Protocol）教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------------
# opencode 生態系教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - OpenCode 是一個開源的 AI 編碼代理 (AI coding agent)，專為終端機 (Terminal)、桌面應用程式及 IDE 擴充功能設計，可協助進行代碼編寫、調試和分析。它支援多種 AI 模型 (包括本地模型)，並內建 build 和 plan 模式，可使用 Tab 鍵切換，能有效替代付費的代碼 AI 工具。
## 參考: https://github.com/anomalyco/opencode
## 背景 - 目前必需使用OpenCode開發web application的系統。 
## 任務說明 - 系統必需使用OpenCode最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生opencode 生態系教學手冊 md 檔

-------------------------------------------------------------------
# OpenCode 生態系教學手冊產生指令

## 角色設定
你是一位：
- 資深軟體架構師
- 資深前後端開發工程師
- DevOps 與 AI 開發工具專家
- 具大型企業導入 AI 開發工具經驗的技術顧問

請以「企業內部正式教學手冊」標準撰寫內容。

---

## 背景說明

本公司未來 Web Application 專案必須全面使用 **OpenCode 最新版** 作為主要 AI 開發工具。

OpenCode 是：
- 開源 AI Coding Agent
- 支援 Terminal / Desktop / IDE Extension
- 支援多種模型（含本地模型）
- 具備 Plan / Build 模式（Tab 切換）
- 可替代付費 AI Coding 工具
- 可整合 CI/CD 與專案自動化流程
- 使用最新版本說明
- 參考: https://github.com/anomalyco/opencode

目標：
建立一份完整的《OpenCode 生態系教學手冊》，供內部工程師使用。

## 任務要求

請產出一份完整且可直接發佈的：

# 《OpenCode 生態系教學手冊》

格式要求：
- 使用 Markdown 格式
- 結構清楚（章節編號）
- 適合企業標準作業程序（SOP）
- 具實務案例
- 包含最佳實踐（Best Practices）
- 包含架構圖（用 Mermaid 表示）
- 包含安裝與設定範例
- 包含企業導入策略

## 必須包含章節

### 第一章：OpenCode 生態系總覽
- OpenCode 核心理念
- 與傳統 AI Coding Tool 差異
- 與 GitHub Copilot / Claude Code 等工具比較
- 適用場景分析

### 第二章：系統架構設計

請包含：

1. OpenCode 在 Web Application 開發架構中的角色
2. 與前端（Vue / React / Tailwind）整合方式
3. 與後端（Spring Boot / Node.js / FastAPI）整合方式
4. 與 Git / CI/CD 整合架構
5. 與本地模型 / 雲端模型整合架構
6. Plan / Build 模式運作流程

請使用 Mermaid 畫出：

- 整體開發架構圖
- AI Agent 運作流程圖

### 第三章：安裝與環境建置

請包含：

- Windows / macOS / Linux 安裝步驟
- 終端機模式設定
- IDE 擴充設定
- 模型設定（雲端 API / 本地模型）
- 環境變數設定
- Proxy 設定
- 企業網路限制處理方式

### 第四章：專案導入標準流程（SOP）

請設計：

- 新專案導入流程
- 舊專案導入流程
- Branch 管理策略
- PR 與 Code Review 搭配方式
- 團隊協作模式
- 安全開發流程（SSDLC 整合方式）

### 第五章：實戰操作教學

請示範：

1. 使用 Plan 模式設計系統架構
2. 使用 Build 模式產生程式碼
3. 自動產生測試
4. 重構（Refactor）
5. Debug
6. 批次修改專案
7. 生成文件（README / API 文件）

請附實際指令範例。

### 第六章：最佳實踐（Best Practices）

包含：

- Prompt 撰寫策略
- Token 控制策略
- 避免幻覺（Hallucination）
- 如何做 Code Validation
- 與 SonarQube / 測試工具整合
- 大型專案使用策略
- 多模組專案管理建議

### 第七章：系統維護與治理

請包含：

- 模型版本管理策略
- OpenCode 版本管理
- 日誌管理
- 成本控制
- 權限管理
- 風險控管

### 第八章：系統升級策略

- 升級前檢查清單
- 版本相容性測試
- 回滾策略
- CI/CD 驗證流程

### 第九章：企業導入建議

請包含：

- 導入階段規劃
- 教育訓練策略
- 試點專案規劃
- 成本效益分析
- KPI 設計

### 第十章：常見問題與故障排除

- API 失敗
- 模型回應不穩
- 權限問題
- IDE 無法連線
- 效能問題

## 內容風格要求
- 專業
- 可實際落地
- 適合 100+ 人工程團隊
- 避免空泛描述
- 提供實際範例

## 產出結果
- 請產出一份 **《opencode 生態系教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《opencode 生態系教學手冊》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "opencode 生態系教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

-------------------------------------------------------------------
# OpenClaw生態系教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - OpenClaw（曾用名 Clawdbot）是一款在 2026 年迅速爆紅的開源個人 AI 助手與 AI 代理（Agent）框架。它被視為從單純的聊天工具轉向「主動執行任務」的關鍵轉折點，常被描述為「真正會做事」的 AI 員工。。
## 參考: https://openclaw.ai/ , https://github.com/openclaw/openclaw
## 背景 - 目前必需使用OpenClaw開發web application的系統。 
## 任務說明 - 系統必需使用OpenClaw最新版開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生OpenClaw生態系教學手冊 md 檔

-------------------------------------------------------------------
# OpenClaw 生態系教學手冊

## 角色設定
你是一位：
- 資深軟體架構師
- 資深前後端開發工程師
- 熟悉 AI Agent 架構設計
- 熟悉大型 Web Application 架構
- 熟悉 DevOps、自動化部署與微服務架構

你必須用「企業級標準」撰寫教學手冊。

## 技術背景說明

本系統將使用：

- OpenClaw 最新穩定版本
- Web Application 架構
- API-first 設計
- 微服務架構
- 容器化部署
- CI/CD 自動化流程
- Agent 任務導向設計模式

OpenClaw（曾用名 Clawdbot）是一款 2026 年迅速爆紅的開源 AI Agent 框架，
被視為從聊天工具轉向「主動執行任務型 AI」的重要轉折。

官方網站：
- https://openclaw.ai/
- https://docs.openclaw.ai/

GitHub：
- https://github.com/openclaw/openclaw

## 任務目標

請產生一份完整的：
- 請以 8000-10000 行 Markdown 文件規模產出，
- 並以「企業標準技術白皮書」等級撰寫。

# 《OpenClaw 生態系教學手冊》

輸出格式必須為：

- Markdown (.md)
- 條列清楚
- 架構圖使用 Mermaid
- 包含程式碼範例
- 包含目錄（Table of Contents）
- 可直接作為企業內部標準文件

# 文件內容必須包含以下章節

## 1️⃣ OpenClaw 核心概念

- Agent 架構設計
- 任務導向模型 (Task-driven Agent)
- 工具調用（Tool Calling）機制
- Memory 設計
- Workflow 設計模式
- 與傳統 LLM Chat 的差異
- 典型應用場景

## 2️⃣ 系統架構設計

請設計企業級 Web Application 架構，包含：

- Frontend
- Backend API
- OpenClaw Agent Service
- Tool Service
- Database
- Message Queue
- Cache
- Logging & Monitoring

請提供：

- Mermaid 架構圖
- 元件說明
- 資料流說明
- 任務流程說明

## 3️⃣ 安裝與環境建置

請包含：

- 本機開發環境建置
- Docker 安裝方式
- Production 部署方式
- 必要環境變數設定
- 設定檔範例
- OpenClaw CLI 使用方式

## 4️⃣ OpenClaw 開發實作教學

請提供：

- 建立第一個 Agent
- 建立自訂 Tool
- 設計任務流程
- Memory 使用範例
- API 整合範例
- 錯誤處理設計

必須包含：

- 程式碼範例請使用java
- 專案目錄結構建議
- 設計原則說明

## 5️⃣ 企業級最佳實務

請包含：

- Agent 模組化設計
- 權限控管設計
- 多 Agent 協作模式
- 安全性設計
- Prompt Engineering 標準
- 可觀測性設計（Logging / Metrics / Tracing）

## 6️⃣ 系統維運與監控

請包含：

- 健康檢查機制
- Agent 任務監控
- 失敗重試機制
- Rate Limit 設計
- Logging 設計
- 警報機制
- 常見問題排除

## 7️⃣ 系統升級策略

請包含：

- OpenClaw 升版策略
- 相容性檢查
- Migration 流程
- Rolling Upgrade 設計
- Zero Downtime 設計

## 8️⃣ DevOps 整合

請包含：

- GitHub Actions / GitLab CI 設計範例
- 自動化測試
- 容器化部署
- Kubernetes 部署範例
- Helm 設計建議

## 9️⃣ 安全設計

請包含：

- API 金鑰管理
- Agent 權限隔離
- 資料加密
- 憑證管理
- OWASP 風險說明

## 🔟 實戰案例

請設計 2-3 個完整實戰案例，例如：

- 自動報表產生 Agent
- 智能客服 Agent
- 任務自動化 Agent

需包含：

- 架構說明
- 設計流程
- 程式碼範例
- 優化建議

# 重要要求

- 所有內容必須使用繁體中文
- 架構設計必須符合大型企業標準
- 不得寫成簡略說明
- 必須具有教學性與實務性
- 必須可直接交給團隊使用

## 產出結果
- 請產出一份 **《OpenClaw生態系教學手冊.md》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《OpenClaw生態系教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "OpenClaw生態系教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-----------------------------------------------------------
# OpenAI Codex生態系教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - OpenAI Codex 是一款由 OpenAI 開發的人工智慧模型，專門用於解析自然語言並生成程式碼。
## 參考: https://openai.com/zh-Hant/codex/
## 背景 - 目前必需使用OpenAI Codex開發web application的系統。 
## 任務說明 - 系統必需使用OpenAI Codex最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生OpenAI Codex生態系教學手冊 md 檔
-------------------------------------------------------------------
# 任務：產生 OpenAI Codex 生態系教學手冊

## 角色設定

你是一位 **資深軟體架構師、資深 AI 工程師與資深全端開發工程師**，擁有多年大型企業系統開發經驗，熟悉：

* AI 輔助開發（AI Assisted Development）
* AI Coding Agent
* DevOps / DevSecOps
* Web Application Architecture
* 微服務架構 (Microservices)
* 雲原生架構 (Cloud Native)
* CI/CD 自動化

你的任務是撰寫一份 **完整、可教學、可實務落地的 OpenAI Codex 生態系教學手冊**。

## 技術背景

OpenAI Codex 是 OpenAI 開發的 AI 模型，專門用於：

* 自然語言轉程式碼
* 程式碼理解
* 程式碼重構
* 程式碼測試
* AI Coding Agent
* 自動化開發流程

Codex 能與以下工具整合：

* IDE（VS Code / JetBrains）
* GitHub
* CLI
* API
* CI/CD Pipeline
* AI Agent Framework

本手冊需說明 **Codex 在現代軟體開發中的完整應用生態系**。

參考資料：

https://openai.com/zh-Hant/codex/

## 任務目標

請產生一份完整的：
- 請以 8000-10000 行 Markdown 文件規模產出，
- 並以「企業標準技術白皮書」等級撰寫。
- 請產生一份 **完整的 OpenAI Codex 生態系教學手冊**。
- 文件需 **結構清晰、可作為企業內部教學文件**。

## 手冊內容要求

請包含以下章節：
# 1 OpenAI Codex 介紹

內容需包含：

* Codex 是什麼
* Codex 與 GPT 的差異
* Codex 的核心能力
* Codex 在軟體開發中的角色
* AI Coding Agent 的概念
* Codex 使用情境

# 2 Codex 生態系

說明 Codex 可以整合的工具：

### IDE

* VS Code
* JetBrains IDE

### CLI 工具

* Codex CLI
* GitHub Copilot CLI

### 開發工具

* Git
* GitHub
* GitLab

### AI Agent

* AI Coding Agent
* 自動開發 Agent

### DevOps

* CI/CD Pipeline
* 自動化測試

# 3 Codex 系統架構

說明企業使用 Codex 的架構：

包含：

* 開發環境
* AI 服務層
* API 層
* IDE integration
* Agent 層
* DevOps Pipeline

請提供：

* 架構說明
* 架構圖（Mermaid）

例如：

* AI Developer Workflow
* AI Assisted Development Architecture

# 4 Codex 安裝與環境建置

包含：

### 開發環境需求

* OS
* Node.js
* Python
* Docker

### 安裝流程

* 安裝 CLI
* 設定 API Key
* IDE 整合

提供：

* Windows
* Linux
* Mac

安裝範例。

# 5 Codex 基本使用

包含：

### 自然語言生成程式碼

範例：

```
Create a REST API using Spring Boot
```

### 程式碼解釋

### 程式碼重構

### 程式碼除錯

### 測試生成

# 6 Codex 在 Web Application 開發的應用

包含：

前端開發

* HTML
* CSS
* Tailwind
* Vue / React

後端開發

* Node.js
* Python
* Java Spring Boot

資料庫

* PostgreSQL
* MySQL
* MongoDB

請提供完整範例。

# 7 Codex 與 AI Coding Agent

說明：

* AI Agent 自動開發
* AI Agent 架構
* Multi Agent 開發模式

請說明：

* Agent 任務分工
* Agent workflow

# 8 Codex 在 DevOps 的應用

說明：

* 自動產生 CI/CD
* 自動產生測試
* 自動 Code Review
* 自動安全掃描

整合：

* GitHub Actions
* Jenkins
* GitLab CI

# 9 Codex 在大型系統開發的最佳實務

請提供：

* AI Coding Best Practice
* Prompt Engineering
* Team Development Workflow
* Code Review Strategy
* AI Governance

# 10 Codex 安全性

說明：

* API Key 管理
* 安全開發
* AI 安全風險
* Prompt Injection 防護

# 11 Codex 系統維護

包含：

* Monitoring
* Logging
* Performance
* 成本控制

# 12 Codex 系統升級

包含：

* 模型升級策略
* API 版本管理
* 系統相容性

# 13 常見問題（FAQ）

例如：

* Codex 與 Copilot 差異
* Codex 是否可以離線使用
* Codex 成本如何控制


# 14 未來發展

說明：

* AI Developer
* Autonomous Coding
* AI Software Factory

# 文件品質要求

文件必須：

* 結構清晰
* 可教學
* 可實務操作
* 提供程式碼範例
* 提供架構圖（Mermaid）
* 適合企業內部培訓

# Markdown要求

文件需：

* 使用 Markdown 格式
* 使用清晰的標題層級
* 使用 code block
* 使用 Mermaid 圖表

# 目標

讓開發人員能：

* 快速理解 Codex
* 使用 Codex 開發 Web Application
* 在團隊中建立 AI 開發流程
* 建立 AI 驅動的軟體開發模式

## 產出結果
- 請產出一份 **《OpenAI Codex生態系教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《OpenAI Codex生態系教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "OpenAI Codex生態系教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# SuperClaude Framework生態系教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - SuperClaude Framework 是一個專為增強 Anthropic 的 Claude Code 命令列工具而設計的開源配置框架。它的核心目標是將 Claude 從一個簡單的 AI 助手轉換為具備專業軟體工程流程的「自動化開發機器」。
## 參考:
- https://github.com/SuperClaude-Org/SuperClaude_Framework
- https://www.superclaude.sh/
- https://www.superclaude.sh/docs
## 背景 - 目前必需使用SuperClaude Framework開發web application的系統。 
## 任務說明 - 系統必需使用SuperClaude Framework最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生SuperClaude Framework生態系教學手冊 md 檔

-------------------------------------------------------------------
# SuperClaude Framework 生態系教學手冊 — AI 生成 Prompt

## 角色設定
你是一位資深軟體架構師，同時具備豐富的前後端開發經驗，熟悉 AI 輔助開發工具鏈。
你的任務是撰寫一份完整、專業、可直接供工程師同仁使用的《SuperClaude Framework 生態系教學手冊》，格式為 Markdown（.md）。

## 背景說明

SuperClaude Framework（目前最新穩定版為 v4.2.0）是一個專為 Anthropic Claude Code 命令列工具設計的開源配置框架。它透過「行為指令注入」與「元件協同編排」，將 Claude Code 從普通 AI 助手轉化為具備完整專業軟體工程流程的「自動化開發平台」。

核心數據：
- 30 個 Slash 指令（涵蓋開發全生命週期）
- 16 個專業 AI 代理人（Agents）
- 7 種行為模式（Behavioral Modes）
- 8 個 MCP Server 整合

本系統已決定採用 SuperClaude Framework 最新版（v4.2.0）作為 Web Application 開發的標準框架。

---

## 手冊撰寫任務

請產生一份完整的《SuperClaude Framework 生態系教學手冊》，內容必須涵蓋以下所有章節，語言使用**繁體中文**，技術術語可保留英文原文。

---

## 手冊目錄結構（請依此結構展開撰寫）

### 第一章：SuperClaude Framework 概覽

1.1 什麼是 SuperClaude Framework？
  - 定義與定位（meta-programming configuration framework）
  - 與原生 Claude Code 的差異比較
  - 核心設計理念（行為指令注入、元件協同編排）
  - 版本資訊（v4.2.0 為現行穩定版，v5.0 TypeScript Plugin 系統開發中）

1.2 生態系架構圖解
  - 整體架構層次說明（配置層 → 指令層 → 代理人層 → MCP 整合層）
  - 各元件角色與職責

1.3 核心能力數據
  - 30 個 Slash 指令概覽
  - 16 個 Agents 概覽
  - 7 種 Modes 概覽
  - 8 個 MCP Servers 概覽

---

### 第二章：系統需求與安裝

2.1 環境需求
  - 作業系統支援（macOS / Linux / Windows WSL）
  - Node.js 版本需求
  - Python 版本需求（pipx 安裝方式）
  - Claude Code CLI 前置條件

2.2 安裝方式（詳述三種方式）

**方式一：pipx 安裝（官方推薦）**
```bash
# 從 PyPI 安裝
pipx install superclaude

# 安裝所有 30 個 Slash 指令
superclaude install

# 驗證安裝
superclaude install --list
superclaude doctor
```

**方式二：Git Clone 直接安裝**
```bash
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
./install.sh
```

**方式三：npm 安裝**
```bash
npm install -g @bifrost_inc/superclaude
```

2.3 MCP Servers 安裝（選配，可提升 2-3x 效能）
  - 列出 8 個 MCP Servers 及其功能說明
  - Tavily（主要 Web 搜尋）、Context7（官方文件查詢）、Sequential-Thinking（多步推理）、Serena（Session 持久化與記憶）、Playwright（跨瀏覽器自動化）、Magic（UI 元件生成）、Morphllm-Fast-Apply（情境感知程式碼修改）、Chrome DevTools（效能分析）
  - 安裝指令：
```bash
superclaude mcp --list              # 列出可用 MCP Servers
superclaude mcp                     # 互動式安裝
superclaude mcp --servers tavily --servers context7  # 安裝指定 Server
```

2.4 效能比較
  - 無 MCP：功能完整，標準效能
  - 有 MCP：2-3x 更快，節省 30-50% Token 用量

2.5 安裝驗證與測試
  - 執行 `superclaude doctor` 健康檢查
  - 在 Claude Code 中輸入 `/sc` 確認指令載入
  - 重啟 Claude Code 後確認 30 個指令可用

---

### 第三章：系統設定與配置

3.1 框架配置檔說明
  - `CLAUDE.md`：主要配置文件說明
  - `.claude/` 目錄結構
  - `.env.example` 環境變數配置

3.2 關鍵文件說明（開發者必讀）

| 文件 | 用途 | 建議閱讀時機 |
|------|------|------------|
| PLANNING.md | 架構設計原則、絕對規則 | Session 開始前、實作前 |
| TASK.md | 當前任務、優先順序、待辦清單 | 每日、開始工作前 |
| KNOWLEDGE.md | 累積洞見、最佳實踐、故障排除 | 遭遇問題時、學習模式時 |
| CONTRIBUTING.md | 貢獻指引、工作流程 | 提交 PR 前 |

3.3 專案整合設定
  - 如何在既有 Web Application 專案中整合 SuperClaude
  - 建立專案專屬的 CLAUDE.md 配置
  - 設定團隊統一的工作流程規則

3.4 MCP Server 進階配置
  - airis-mcp-gateway 使用說明
  - 各 MCP Server 的連接設定
  - 自訂 MCP Server 整合

---

### 第四章：30 個 Slash 指令完整指南

說明：所有指令均以 `/sc:` 前綴使用（例如 `/sc:implement`）。
請依以下分類，為每個指令提供：功能說明、語法格式、使用範例、最佳使用場景。

4.1 規劃與設計類（4 個指令）
  - `/sc:brainstorm` — 結構化腦力激盪
  - `/sc:design` — 系統架構設計
  - `/sc:estimate` — 時程與工作量估算
  - `/sc:spec-panel` — 規格分析面板

4.2 開發類（5 個指令）
  - `/sc:implement` — 程式碼實作
  - `/sc:build` — 建置工作流程
  - `/sc:improve` — 程式碼改善
  - `/sc:cleanup` — 重構與清理
  - `/sc:explain` — 程式碼解釋

4.3 測試與品質類（4 個指令）
  - `/sc:test` — 測試生成
  - `/sc:analyze` — 程式碼分析
  - `/sc:troubleshoot` — 除錯流程
  - `/sc:reflect` — 回顧與反思

4.4 文件類（2 個指令）
  - `/sc:document` — 文件生成
  - `/sc:help` — 指令幫助

4.5 版本控制類（1 個指令）
  - `/sc:git` — Git 操作自動化

4.6 專案管理類（3 個指令）
  - `/sc:pm` — 專案管理
  - `/sc:task` — 任務追蹤
  - `/sc:workflow` — 工作流程自動化

4.7 研究與分析類（2 個指令）
  - `/sc:research` — 深度網路研究（Deep Research）
  - `/sc:business-panel` — 商業分析面板

4.8 工具類（9 個指令）
  - `/sc:agent` — AI 代理人調用
  - `/sc:index-repo` — 儲存庫索引
  - `/sc:index` — 索引別名
  - `/sc:recommend` — 指令推薦
  - `/sc:select-tool` — 工具選擇
  - `/sc:spawn` — 平行任務執行
  - `/sc:load` — 載入 Session
  - `/sc:save` — 儲存 Session
  - `/sc` — 顯示所有指令

---

### 第五章：16 個 AI 代理人（Agents）使用指南

5.1 代理人系統概述
  - 代理人自動協調機制
  - 如何根據情境自動選擇代理人
  - 手動調用代理人的方式

5.2 各代理人詳細說明（請逐一描述以下 16 個）：
  PM Agent（專案管理）、Deep Research Agent（深度研究）、Security Engineer Agent（資安工程）、Frontend Architect Agent（前端架構）、Backend Engineer Agent（後端工程）、DevOps Agent（部署運維）、Code Reviewer Agent（程式碼審查）、Database Agent（資料庫設計）、API Designer Agent（API 設計）、Testing Agent（測試策略）、Documentation Agent（文件撰寫）、Performance Agent（效能優化）、Architecture Agent（系統架構）、UX Agent（使用者體驗）、Data Agent（資料分析）、Integration Agent（系統整合）

5.3 Web Application 開發的代理人協作流程
  - 典型全端開發流程中各代理人的分工
  - 代理人之間的交接與協作範例

---

### 第六章：7 種行為模式（Behavioral Modes）

6.1 各模式說明與適用場景

| 模式名稱 | 中文說明 | 最佳使用場景 |
|---------|---------|------------|
| Brainstorming Mode | 腦力激盪模式 | 需求探索、功能規劃初期 |
| Business Panel Mode | 商業面板模式 | 多專家策略分析、商業決策 |
| Deep Research Mode | 深度研究模式 | 技術調研、競品分析 |
| Orchestration Mode | 編排模式 | 複雜多工具協調 |
| Token-Efficiency Mode | 省 Token 模式 | 長對話、大型程式庫分析 |
| Task Management Mode | 任務管理模式 | 系統性工作組織 |
| Introspection Mode | 自省模式 | 元認知分析、品質回顧 |

6.2 模式切換方法與技巧
6.3 Web Application 開發中各階段建議使用的模式

---

### 第七章：Deep Research 深度研究功能

7.1 Deep Research 架構說明
  - 三種智能策略：Planning-Only、Intent-Planning、Unified（預設）
  - Multi-Hop Reasoning（最多 5 次迭代搜尋）
  - 品質評分機制（信心閾值 0.6 起跳，目標 0.8）
  - Cross-session 學習（案例累積記憶）

7.2 研究深度等級對照表

| 深度 | 來源數 | Hop 次數 | 時間 | 適用場景 |
|------|--------|---------|------|---------|
| Quick | 5-10 | 1 | ~2 分鐘 | 快速事實查詢 |
| Standard | 10-20 | 3 | ~5 分鐘 | 一般研究（預設） |
| Deep | 20-40 | 4 | ~8 分鐘 | 全面分析 |
| Exhaustive | 40+ | 5 | ~10 分鐘 | 學術級研究 |

7.3 Research 指令使用範例
```
/sc:research "React Server Components 最新最佳實踐"
/sc:research "我們專案的競品技術棧分析"
/sc:research "TypeScript 5.x 新特性對現有程式碼的影響"
```

---

### 第八章：Web Application 開發實戰工作流

8.1 標準 Web Application 開發流程（使用 SuperClaude）

**Phase 1：需求分析與規劃**
```
/sc:brainstorm "電商平台核心功能需求"
/sc:spec-panel "使用者認證模組規格分析"
/sc:estimate "MVP 版本開發工作量"
```

**Phase 2：系統架構設計**
```
/sc:design "前後端分離架構設計（React + Node.js + PostgreSQL）"
/sc:research "最新微服務架構最佳實踐"
/sc:business-panel "技術選型評估"
```

**Phase 3：開發實作**
```
/sc:implement "使用者認證 API（JWT + Refresh Token）"
/sc:implement "商品列表頁面元件（React + TypeScript）"
/sc:build "Docker 容器化配置"
```

**Phase 4：測試與品質保證**
```
/sc:test "使用者認證模組單元測試"
/sc:analyze "程式碼品質分析與安全性檢查"
/sc:troubleshoot "API 回應時間異常問題"
```

**Phase 5：文件與部署**
```
/sc:document "API 文件自動生成"
/sc:git "功能分支合併與 Release 準備"
/sc:workflow "CI/CD Pipeline 設定"
```

8.2 Session 管理與跨日工作銜接
```
# 結束工作前儲存
/sc:save "電商平台開發 - Day 3 進度"

# 隔天繼續
/sc:load "電商平台開發 - Day 3 進度"
```

8.3 常見 Web Application 場景的 Prompt 範例集（至少 10 個實用範例）

---

### 第九章：Flags 旗標使用指南

9.1 什麼是 Flags
9.2 常用 Flags 列表與說明
9.3 在 Web Application 開發中的 Flags 應用範例

---

### 第十章：系統維護與管理

10.1 日常維護作業
  - 使用 `superclaude doctor` 進行健康檢查
  - 查看已安裝的指令與狀態
  - MCP Server 連線狀態確認

10.2 常見問題排除（Troubleshooting）

| 問題現象 | 可能原因 | 解決方案 |
|---------|---------|---------|
| 指令無回應 | Claude Code 未重啟 | 重啟 Claude Code |
| MCP 連線失敗 | Server 未啟動 | 執行 `superclaude mcp` 重新設定 |
| 指令不存在 | 安裝不完整 | 執行 `superclaude install` 重新安裝 |
| Token 用量過高 | 未啟用效率模式 | 使用 Token-Efficiency Mode |
| Research 結果品質低 | 未安裝 Tavily MCP | 安裝 Tavily MCP Server |

10.3 記錄檔與診斷
  - 如何查看 Claude Code 記錄
  - 回報問題的正確方式（GitHub Issues）

10.4 備份與還原
  - 配置文件備份策略
  - 跨機器同步設定

---

### 第十一章：系統升級

11.1 版本管理策略
  - 了解目前版本：`superclaude --version`
  - 查看 CHANGELOG.md 了解版本異動

11.2 升級步驟（pipx 方式）
```bash
# 升級 SuperClaude
pipx upgrade superclaude

# 重新安裝指令（升級後必做）
superclaude install

# 更新 MCP Servers
superclaude mcp

# 驗證升級結果
superclaude doctor
```

11.3 升級注意事項
  - v4.x → v5.0 的重大變更預告（TypeScript Plugin 系統）
  - 升級前的備份作業清單
  - 升級後的驗證測試清單
  - 向下相容性說明

11.4 從 Git 直接升級
```bash
cd SuperClaude_Framework
git pull origin master
./install.sh
```

---

### 第十二章：團隊協作最佳實踐

12.1 團隊導入 SuperClaude 的建議步驟
  - 評估與試點（Pilot）
  - 標準化配置管理
  - 培訓計畫建議

12.2 統一工作流程規範
  - 建立團隊共用的 CLAUDE.md 模板
  - 指令使用規範文件
  - Code Review 整合 SuperClaude 的方式

12.3 知識管理
  - 維護團隊的 KNOWLEDGE.md
  - 累積 Prompt 最佳實踐庫
  - 建立內部指令範本庫

12.4 效能衡量指標
  - 開發速度提升指標
  - Token 用量監控
  - 程式碼品質指標

---

### 附錄

A. 快速參考卡（Quick Reference Card）
  - 30 個指令一覽表（含中文說明）
  - 7 種模式切換速查
  - 常用 Flags 速查

B. 相關資源連結
  - GitHub Repository：https://github.com/SuperClaude-Org/SuperClaude_Framework
  - 官方網站：https://www.superclaude.sh/
  - 官方文件：https://www.superclaude.sh/docs
  - PyPI：https://pypi.org/project/superclaude/
  - npm：https://www.npmjs.com/package/@bifrost_inc/superclaude
  - CHANGELOG：https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/CHANGELOG.md

C. 版本歷程摘要
  - v4.2.0（2026/01/18）：Deep Research 強化、MCP 整合優化
  - v4.1.x：代理人系統強化、文件重寫
  - v4.0.x：架構重整、效能優化
  - v5.0（開發中）：TypeScript Plugin 系統

D. 詞彙表（Glossary）
  - 關鍵術語中英對照

---

# 格式要求

1. 使用標準 Markdown 格式
2. 每個章節開頭提供一段「章節摘要」（2-3 句話說明本章重點）
3. 程式碼區塊必須標注語言類型（bash、typescript、yaml 等）
4. 重要注意事項使用 `> ⚠️ **注意**：` 格式標注
5. 最佳實踐使用 `> 💡 **提示**：` 格式標注
6. 表格用於對比說明，確保欄寬適當
7. 每個指令都要有至少 2 個實際使用範例
8. 文末附上「版本資訊」（本手冊基於 SuperClaude Framework v4.2.0 撰寫，最後更新：2026-03）

---

# 特別要求

1. **實用性優先**：所有範例必須是真實可用的，避免過於抽象的說明
2. **Web Application 場景導向**：所有範例盡量以 Web Application 開發為情境
3. **由淺入深**：新手可以從第一章開始閱讀，進階用戶可以直接跳到對應章節
4. **自給自足**：手冊本身就應該是完整的，不依賴讀者另外查閱外部文件
5. **中文優先**：使用流暢的繁體中文，技術術語保留英文並在第一次出現時加上中文說明

請現在開始產生完整的《SuperClaude Framework 生態系教學手冊》Markdown 文件。

## 產出結果
- 請產出一份 **《SuperClaude Framework生態系教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《SuperClaude Framework生態系教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "SuperClaude Framework生態系教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# prompt engineering vs context engineering vs harness engineering比較教學
## 角色設定 - 你是資深軟體架構師和AI開發工程師
## 技術說明 - 在 AI 開發領域，提示工程 (Prompt Engineering)、情境工程 (Context Engineering) 與 線束工程 (Harness Engineering) 代表了從「如何對話」到「如何構建系統」的演進過程。這三者的核心差異可以用一句話概括：提示工程管「怎麼說」，情境工程管「知道什麼」，而線束工程管「在什麼環境做事」。

## 背景 - 目前必需使用github copilot開發web application的系統。 
## 任務說明 - 教導同仁三者的差別,應如何使用,是否有對應工具,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生prompt engineering vs context engineering vs harness engineering比較教學 md 檔
-------------------------------------------------------------------
# Prompt Engineering vs Context Engineering vs Harness Engineering 比較教學手冊產生器

## 角色設定
你是資深軟體架構師、AI系統設計專家，以及具備大型企業系統（特別是銀行/金融系統）經驗的技術顧問，同時熟悉 AI 輔助開發工具（如 GitHub Copilot）。

## 背景
目前團隊使用 GitHub Copilot 開發大型 Web Application，採用現代架構（如 Clean Architecture / Microservices / API First）。  
開發過程中需要有效運用 AI 提升生產力，但團隊對以下三種工程方法理解不足：

- Prompt Engineering（提示工程）
- Context Engineering（情境工程）
- Harness Engineering（線束工程 / 系統工程）

## 任務目標
請產出一份完整、可實務落地的 Markdown 教學手冊，主題為：

「Prompt Engineering vs Context Engineering vs Harness Engineering 比較與實務應用」

## 文件要求

### 1. 核心概念說明
- 清楚定義三者：
  - Prompt Engineering（怎麼說）
  - Context Engineering（知道什麼）
  - Harness Engineering（在什麼環境做事）
- 說明三者的演進關係（從單次互動 → 有記憶 → 有系統）

### 2. 詳細比較表（重點）
請提供表格比較以下面向：
- 定義
- 關注重點
- 控制範圍
- 複雜度
- 使用時機
- 對開發流程影響
- 在 GitHub Copilot 中的應用方式

### 3. 實務案例（Web Application）
請用實際開發場景說明三者差異，例如：
- API 開發
- Batch Job（如資料處理）
- 前端 UI 開發
- 除錯（Debug）

每個案例需包含：
- 不同工程方法的做法
- 範例 Prompt / Context / Harness 設計

### 4. GitHub Copilot 實戰應用
說明：
- Prompt Engineering 如何寫出高品質註解
- Context Engineering 如何利用：
  - 檔案結構
  - 命名規則
  - 文件（README, ADR）
- Harness Engineering 如何透過：
  - 開發框架
  - 測試工具
  - CI/CD
  - MCP / Agent（如有）

### 5. 工具與技術建議
請列出對應工具，例如：
- Prompt Engineering：ChatGPT、Copilot Chat
- Context Engineering：Vector DB、RAG、文件系統
- Harness Engineering：LangChain、AutoGen、CI/CD pipeline

### 6. 架構設計觀點（非常重要）
請從「系統架構師」角度說明：
- 如何從 Prompt → Context → Harness 演進
- 在大型系統中如何分層設計 AI 能力
- 如何避免 AI 使用混亂（Anti-pattern）

### 7. 最佳實務（Best Practices）
- 團隊開發規範建議
- 文件設計方式
- Prompt Template 設計
- AI 使用治理（Governance）

### 8. 常見錯誤（Anti-pattern）
例如：
- 過度依賴 Prompt
- Context 混亂
- 沒有 Harness 導致不可控

### 9. 結論
用架構思維總結三者定位：
- Prompt = Interface
- Context = Data Layer
- Harness = System Layer

## 輸出格式
- 使用 Markdown
- 結構清楚（# / ## / ###）
- 包含表格、範例、程式碼區塊
- 內容需具備「可教學 + 可落地實作」

## 額外要求（重要）
- 所有範例需貼近企業級 Web Application（如銀行系統）
- 優先使用 Java / Spring Boot / API 設計情境
- 語言使用「繁體中文」

## 產出結果
- 請產出一份 **《使用github copilot下的Prompt Engineering vs Context Engineering vs Harness Engineering教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《使用github copilot下的Prompt Engineering vs Context Engineering vs Harness Engineering教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "使用github copilot下的Prompt Engineering vs Context Engineering vs Harness Engineering教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Superpowers教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - AI 開發框架：Superpowers (GitHub 熱門項目)
這是一個由 Jesse Vincent (obra) 開發的開源 AI 代理技能框架 (Agentic Skills Framework)，旨在讓 AI（如 Claude Code）遵循專業的工程規範，而不僅僅是生成簡單的程式碼。
核心價值：強制 AI 執行「工程級」開發，建立寫程式的「紀律」，防止 AI 因為偷懶而不寫測試或不釐清需求。
關鍵技能 (Skills)：
- Brainstorming：使用蘇格拉底式提問釐清需求，避免盲目開發。
- Test-Driven Development (TDD)：強制「紅燈-綠燈-重構」循環，沒有先寫失敗的測試就不准寫程式碼。
- Writing Plans：將大任務拆解成 2-5 分鐘可完成的極小步驟。
- Systematic Debugging：分四階段進行根因分析，而非憑感覺修 Bug。
- Git Worktrees：自動創建隔離的開發環境，確保主分支安全。
適用場景：適合需要長期維護、高品質要求的生產級項目 。

## 參考:
- https://github.com/obra/superpowers
- https://claude.com/plugins/superpowers
## 背景 - 目前必需使用superpowers開發web application的系統。 
## 任務說明 - 系統必需使用superpowers最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生superpowers教學手冊 md 檔

-------------------------------------------------------------------
# Superpowers教學手冊（工程級完整版）

## 角色設定
你是「資深軟體架構師 + 資深前後端工程師 + AI Agent 系統設計專家」，熟悉 AI Agent 開發框架、DevOps、Clean Architecture、TDD、微服務架構，以及企業級系統導入。

## 技術背景
本文件針對 AI Agent 技能框架 **Superpowers**（由 Jesse Vincent / obra 開發）進行完整教學。

Superpowers 核心理念：
- 強制 AI 遵守工程紀律（Engineering Discipline）
- 避免 AI 直接產出低品質程式碼
- 導入「可維護、可測試、可擴展」的開發模式

核心 Skills：
- Brainstorming（需求釐清）
- Test-Driven Development（TDD）
- Writing Plans（微步驟拆解）
- Systematic Debugging（系統化除錯）
- Git Worktrees（隔離開發環境）

## 任務目標
請產出一份「完整、可落地、企業等級」的 **Superpowers 教學手冊（Markdown 格式）**，內容需可直接提供團隊使用。

## 文件要求

### 1️⃣ 文件格式
- 使用 Markdown
- 結構清晰（# / ## / ###）
- 每章節需包含：
  - 說明
  - 圖解（使用 Mermaid）
  - 實務範例
  - Best Practices
  - 常見錯誤（Anti-patterns）

---

### 2️⃣ 必須包含章節（不可省略）

## 第 1 章：Superpowers 概述
- 什麼是 Superpowers
- 與 Prompt Engineering / Agent Framework 的差異
- 適用場景（企業系統 / AI Coding / Agent 團隊）
- 核心價值（工程紀律）

---

## 第 2 章：整體系統架構設計
- Superpowers 在 AI 開發架構中的位置
- 與以下整合：
  - Claude Code / OpenAI / Cursor
  - GitHub / CI/CD
- 架構圖（Mermaid）

---

## 第 3 章：安裝與環境建置
- 安裝步驟（CLI / Plugin / Repo）
- 專案初始化
- 建議目錄結構（Monorepo / Microservices）
- Dev Container / Docker（如適用）

---

## 第 4 章：核心 Skills 詳解（重點章節）

### Brainstorming
- 蘇格拉底式提問設計
- Prompt 範例

### TDD（必須深入）
- Red → Green → Refactor
- 範例（Java / Python / Node.js 任選）
- 測試策略（Unit / Integration）

### Writing Plans
- 任務拆解方法
- 2~5 分鐘微任務設計

### Systematic Debugging
- 四階段：
  1. 問題重現
  2. 假設建立
  3. 驗證
  4. 修復

### Git Worktrees
- 多分支開發
- AI Agent 隔離環境

---

## 第 5 章：實戰開發流程（End-to-End）

請設計完整流程：

1. 需求分析（Brainstorming）
2. 任務拆解（Planning）
3. 測試設計（TDD）
4. 開發實作
5. Debugging
6. Merge & Release

需包含：
- 流程圖（Mermaid）
- 範例（Web Application）

---

## 第 6 章：與企業系統整合

請說明如何整合：
- Spring Boot / FastAPI / Node.js
- 微服務架構
- API Gateway
- DB（Oracle / PostgreSQL / DB2）
- MQ（Kafka / RabbitMQ）

---

## 第 7 章：CI/CD 與 DevOps

- GitHub Actions / GitLab CI
- 自動測試（強制 TDD）
- 自動部署
- 品質控管（SonarQube）

---

## 第 8 章：系統維運（Maintenance）

- 如何維持 AI 產出品質
- 技術債控制
- Debug 流程標準化
- Log / Monitoring

---

## 第 9 章：系統升級與版本管理

- Superpowers 升級策略
- Prompt / Skills 版本控管
- 相容性處理

---

## 第 10 章：最佳實務（Best Practices）

- AI 不可跳過測試
- 強制 Planning
- 小步提交
- Clean Architecture

---

## 第 11 章：反模式（Anti-patterns）

請列出常見錯誤，例如：
- AI 直接寫 code
- 沒有測試
- 無計畫開發
- Debug 憑感覺

---

## 第 12 章：企業導入策略（重要）

- 團隊導入方式
- Governance（治理）
- Code Review 機制
- AI 使用規範

---

## 第 13 章：完整範例專案

請提供：
- 專案架構
- 範例程式碼
- 測試案例
- 開發流程示範

---

## 輸出要求

- 文件必須「極度詳細」
- 可直接作為內部培訓教材
- 所有流程需具備「工程可落地性」
- 必須包含：
  - Mermaid 圖
  - 程式碼範例
  - Prompt 範例

---

## 額外加分（如能做到）

- 加入 AI Agent Team 協作模式
- 多 Agent 分工（Planner / Developer / Tester）
- 與 MCP（Model Context Protocol）整合

---

## 產出結果
- 請產出一份 **《Superpowers教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Superpowers教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Superpowers教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# oh-my-openagent教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Oh My OpenCode (OMO) 是一款針對 OpenCode（開源終端 AI 編碼代理）開發的強力增強插件。它將原本單一的 AI 助手升級為一個具備多代理協作（Multi-Agent Collaboration）能力的開發團隊，被視為 Anthropic Claude Code 或 OpenAI Codex 的開源替代方案。 
核心功能與特點
- 多代理系統：內建多個專屬 Agent（如前端、架構、文件整理等），能根據任務自動分配最適合的角色處理。
- 模式切換：
 - Plan 模式：AI 僅提供建議和計劃，不改動程式碼，適合初期討論。
 - Build 模式：確認方案後，AI 可直接執行並修改檔案。
- 模型靈活性：支援切換本地或雲端多種模型（如 Claude 3.5、GPT-4、Gemini、DeepSeek 等），並可透過 Google 的 Antigravity 進行身份驗證。
- 項目理解：會生成 AGENTS.md 檔案，幫助 AI 更精準地理解項目結構與開發任務。
## 參考:
- https://github.com/code-yeongyu/oh-my-openagent
- https://github.com/code-yeongyu/oh-my-openagent/releases
## 背景 - 目前必需使用oh-my-openagent開發web application的系統。 
## 任務說明 - 系統必需使用oh-my-openagent最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生oh-my-openagent教學手冊 md 檔


--------------------------------------------------------------------
# oh-my-openagent（Oh My OpenCode, OMO）教學手冊產生器 Prompt

## 🎯 角色設定（System Role）
你是一位：
- 資深軟體架構師（Software Architect）
- 資深全端工程師（Full-Stack Engineer）
- AI Agent 系統設計專家（Agentic System Expert）
- 熟悉企業級系統（金融業等級）與 SSDLC（Secure SDLC）

請以「可落地實作 + 團隊教學」為導向，產出一份 **完整、專業、企業可用的教學手冊**。

---

## 📌 任務說明（Task）
請產出一份 **oh-my-openagent（OMO）教學手冊（Markdown 格式）**，內容需涵蓋：

- 系統架構設計
- 安裝與環境建置
- 設定與最佳實務
- 多代理（Multi-Agent）協作設計
- 開發流程（Plan / Build 模式）
- 實務應用（Web Application）
- 維運（Maintenance）
- 升級（Upgrade）
- 安全（SSDLC）
- 團隊導入策略

---

## 🧠 技術背景（Context）

oh-my-openagent（OMO）是一個：
- OpenCode 的增強插件（AI Coding Agent Framework）
- 支援 Multi-Agent 協作（如 Architect / Backend / Frontend / QA / Docs）
- 支援 Plan / Build 雙模式
- 支援多模型（Claude / GPT / Gemini / DeepSeek / Local LLM）
- 使用 AGENTS.md 讓 AI 理解專案結構

---

## 🏗️ 請輸出以下章節（必須完整）

# 1️⃣ 總覽（Overview）
- 什麼是 OMO
- 與傳統 AI Coding（Copilot / ChatGPT）差異
- 與 Agent Framework（AutoGPT / CrewAI / OpenDevin）比較
- 適用場景（企業 / 個人 / 大型平台）

---

# 2️⃣ 系統架構設計（Architecture）
請包含：
- OMO 架構圖（使用 Mermaid）
- Agent 分工設計（Architect / FE / BE / QA / DevOps）
- Multi-Agent 協作流程
- 與現有系統整合（CI/CD / Git / API）

---

# 3️⃣ 安裝與環境建置（Installation）
請提供：
- 前置需求（Node.js / Python / Git / OpenCode）
- 安裝步驟（CLI）
- 設定檔說明
- 本地模型 vs 雲端模型配置
- 常見錯誤排除

---

# 4️⃣ 設定與專案初始化（Configuration）
- AGENTS.md 設計原則
- 專案目錄結構（企業級）
- Prompt Template 設計
- Agent 行為定義（Role-based AI）

---

# 5️⃣ Multi-Agent 設計實務（核心章節🔥）
請詳細說明：
- 如何設計 Agent（職責、輸入、輸出）
- Agent Communication Pattern
- Task Routing（任務分派）
- Orchestration（編排）
- 與微服務架構對應

---

# 6️⃣ 開發流程（Plan / Build 模式）
請說明：
- Plan Mode：需求分析 / 架構設計
- Build Mode：自動生成程式碼
- Code Review Flow（AI + 人類）
- Git Flow 整合

---

# 7️⃣ Web Application 實戰（重點🔥）
請提供完整範例：
- 前端（Vue / React + Tailwind）
- 後端（Spring Boot / FastAPI）
- API 設計
- DB 設計（支援多資料庫）
- OMO 如何協助開發（實際流程）

---

# 8️⃣ 測試與品質（Testing & Quality）
- 單元測試（JUnit / PyTest）
- E2E 測試
- AI 自動測試生成
- Code Quality（SonarQube）

---

# 9️⃣ 維運（Maintenance）
- Logging / Monitoring
- Agent Debug 方法
- 效能優化（Prompt / Token / Latency）
- 成本控制

---

# 🔟 升級與版本管理（Upgrade）
- OMO 升級策略
- Agent 版本控制
- Prompt Versioning
- 與專案版本同步

---

# 1️⃣1️⃣ 安全（SSDLC）
請務必包含：
- Secure Prompt Design（防 Prompt Injection）
- Secrets 管理
- 權限控管（RBAC）
- Code Security Scan
- 供應鏈安全（Dependency）

---

# 1️⃣2️⃣ 團隊導入策略（Enterprise Adoption）
- 導入階段（PoC → Pilot → Production）
- 開發流程改造
- 與 DevOps 整合
- 教育訓練建議

---

# 1️⃣3️⃣ 最佳實務（Best Practices）
- Prompt Engineering vs Agent Design
- Context Engineering
- 避免 AI 亂改程式
- 成本 vs 效能平衡

---

# 1️⃣4️⃣ 常見問題（FAQ）
- 為什麼 Agent 不準？
- 為什麼 Build Mode 改壞？
- 多模型如何選擇？

---

# 1️⃣5️⃣ 附錄（Appendix）
- 常用指令
- Prompt 範本
- AGENTS.md 範例

---

## 📄 輸出格式要求
- 使用 Markdown（.md）
- 所有程式碼使用 code block
- 架構圖使用 Mermaid
- 條列清晰（適合內部培訓）
- 內容需「可實作」，避免空泛描述

---

## ⚠️ 特別要求（重要）
- 以「企業級大型系統」為主（非玩具專案）
- 必須結合：
  - Clean Architecture
  - 微服務（Microservices）
  - CI/CD
  - 多環境（Dev / SIT / UAT / Prod）
- 強調：
  - AI Agent 協作設計（核心）
  - 可維護性（Maintainability）
  - 可擴展性（Scalability）

---

## 🎯 輸出目標
產出一份：
👉 可直接給工程團隊使用的「oh-my-openagent 教學手冊.md」
👉 可作為公司內部標準文件（Engineering Playbook）

## 產出結果
- 請產出一份 **《oh-my-openagent（Oh My OpenCode, OMO）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《oh-my-openagent（Oh My OpenCode, OMO）教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "oh-my-openagent（Oh My OpenCode, OMO）教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
---------------------------------------------------------------
# copilot-cli 教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - GitHub Copilot CLI 
1. 核心功能與優勢
- 自然語言轉指令：可以直接詢問「如何用 macOS 啟動 Redis？」或「幫我把目前分支同步到 main」，AI 會自動生成對應的 shell 或 Git 指令。
- 智慧代理（Agentic Workflow）：支援自主任務執行，例如自動掃描 codebase、產生單元測試或修復程式碼 Bug。
- 上下文管理：能自動讀取專案內的檔案架構與依賴關係，提供更精準的建議。
- GitHub 整合：無需切換畫面即可建立 Pull Request (PR)、更新 Issue 或產生 PR 摘要。
- 安全性控管：所有指令執行與檔案修改皆須經過使用者手動確認（除非開啟 YOLO 模式），並遵循組織的 Copilot 治理政策。
## 參考:
- https://github.com/features/copilot/cli
- https://github.com/github/copilot-cli
## 背景 - 目前必需使用copilot-cli開發web application的系統。 
## 任務說明 - 系統必需使用copilot-cli最新版開發,包含系統架構,安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生copilot-cli教學手冊 md 檔


---------------------------------------------------------------
# GitHub Copilot CLI 教學手冊產生器 Prompt

## 🎯 角色設定
你是：
- 資深軟體架構師（熟悉企業級系統設計）
- 資深 DevOps / SRE 工程師
- 資深前後端工程師（熟悉 Vue / Spring Boot / 微服務架構）
- 熟悉 AI Agent / Copilot CLI / Developer Productivity Engineering

---

## 🧠 背景說明
本專案為「大型企業級 Web Application 平台」，具有以下特性：

- 前端：Vue 3 + TypeScript + Tailwind CSS（Micro-Frontend）
- 後端：Spring Boot 3.x（Clean Architecture）
- 架構：微服務 + API Gateway + MQ + Cache
- DB：Oracle / DB2 / PostgreSQL（支援分片與讀寫分離）
- DevOps：GitHub + CI/CD + Docker/Podman
- 安全：SSDLC + 程式碼掃描 + 權限控管
- 整合：FTP / SFTP / Teams / Batch Job

目前目標：
👉 導入 **GitHub Copilot CLI（最新版）** 提升開發效率與自動化能力

---

## 📌 任務目標
請產出一份完整的：

👉「GitHub Copilot CLI 教學手冊（Markdown 格式）」

需符合：
- 可作為公司內部標準教材
- 適合新手 + 進階工程師
- 可直接落地實務使用
- 結構清晰、分章節完整

---

## 📚 教學手冊內容要求

請依以下章節完整輸出：

---

# 1️⃣ Copilot CLI 概述
- 什麼是 Copilot CLI
- 與 ChatGPT / IDE Copilot / Agent Framework 差異
- 適用場景（CLI / DevOps / Backend / Infra）

---

# 2️⃣ 系統架構整合設計
- Copilot CLI 在企業架構中的角色
- 與以下整合方式：
  - 開發流程（Dev Workflow）
  - CI/CD Pipeline
  - Git Flow / Trunk-based Development
  - 微服務架構
- Agentic Workflow 設計模式

👉 請畫出（用 Mermaid）：
- Copilot CLI + DevOps 架構圖

---

# 3️⃣ 安裝與環境設定
- 支援平台（Windows / macOS / Linux）
- 安裝步驟（最新版）
- GitHub 登入與權限設定
- CLI 初始化設定
- 常見錯誤與排除

---

# 4️⃣ 核心功能教學（重點）
逐一說明並附範例：

## 4.1 自然語言轉指令
- Shell 指令生成
- Git 操作（branch / merge / rebase）

## 4.2 Agentic Workflow
- 自動產生程式碼
- 自動修 bug
- 自動產生測試

## 4.3 Codebase Context 分析
- 如何理解專案
- 如何問問題效果最好

## 4.4 GitHub 整合
- 建立 PR
- PR Summary 自動生成
- Issue 管理

---

# 5️⃣ 進階使用技巧（企業級）
- Prompt Engineering（CLI 版本）
- Context Engineering（如何讓 AI 更準）
- 多步驟任務拆解（Task chaining）
- 與其他工具整合：
  - Docker
  - Kubernetes
  - Terraform

---

# 6️⃣ 安全與治理（非常重要）
- YOLO Mode 說明與風險
- 指令審核機制
- 資安控管（避免敏感資料外洩）
- 企業治理策略（Copilot Policy）

---

# 7️⃣ 實戰案例（重點）
請提供「實際企業場景」：

### 案例 1：
👉 Spring Boot 專案自動產生 API

### 案例 2：
👉 自動修復 Bug + 產測試

### 案例 3：
👉 自動建立 PR + Summary

### 案例 4：
👉 Batch Job（如 R91 類型）開發輔助

---

# 8️⃣ 最佳實務（Best Practices）
- 如何寫 prompt（CLI 版本）
- 如何避免錯誤建議
- 如何做人機協作（Human-in-the-loop）
- 適合與不適合使用的場景

---

# 9️⃣ 維運與升級
- 如何更新 Copilot CLI
- 版本管理策略
- 常見問題（FAQ）
- 效能與成本考量

---

# 🔟 附錄
- 常用指令速查表
- Prompt 範本（可直接用）
- CLI 指令 Cheat Sheet

---

## 📌 輸出格式要求
- 使用 Markdown（.md）
- 標題層級清楚（# / ## / ###）
- 每段需有：
  - 說明
  - 範例
- 必須包含：
  - Mermaid 圖
  - 表格整理
  - 實務案例

---

## 🚀 加分要求（務必做到）
- 結合「大型企業架構」
- 結合「AI Agent 思維」
- 結合「DevOps 自動化」
- 提供「可直接複製使用」的指令與 Prompt

---

## ❗ 注意事項
- 不可只寫概念，需具體可操作
- 不可過於簡略，需具教學價值
- 所有範例需「貼近企業開發場景」

---

## 產出結果
- 請產出一份 **《Copilot CLI教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Copilot CLI教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Copilot CLI教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-----------------------------------------------------------------
# 使用vs code and copilot開發java web應用程式教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 使用vs code and copilot開發java web應用程式
使用 VS Code 搭配 GitHub Copilot 開發 Java Web 應用程式（如 Spring Boot）是目前非常高效的開發流程。透過 AI 的輔助，你可以快速生成樣板程式碼、進行除錯並加速開發進度。
。
## 參考:
- https://code.visualstudio.com/docs
- https://code.visualstudio.com/updates/v1_113
- https://code.visualstudio.com/
## 背景 - 使用vs code and copilot開發java web application的系統。 
## 任務說明 - 系統必需使用vs code and copilot最新版開發,包含安裝,設定,系統使用,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用vs code and copilot開發java web應用程式教學手冊 md 檔

--------------------------------------------------------------------
# 任務：產生《VS Code + GitHub Copilot 開發 Java Web 應用程式教學手冊》

## 🎯 角色設定
你是一位「資深軟體架構師 + 資深 Java 後端工程師 + DevOps 專家 + 技術講師」，具備大型企業（如銀行系統）開發經驗，熟悉 Spring Boot、Clean Architecture、微服務架構與 AI 輔助開發（GitHub Copilot）。

---

## 🎯 任務目標
請產生一份**完整且可落地的教學手冊（Markdown 格式）**，主題為：

👉 使用 **VS Code + GitHub Copilot 最新版** 開發 **Java Web 應用程式（Spring Boot）**

手冊需適用於：
- 初學者（快速上手）
- 中階工程師（提升效率）
- 企業團隊（建立標準）

---

## 📚 手冊內容要求（務必完整）

請依照以下章節結構輸出：

---

# 📖 1. 總覽
- VS Code 在 Java 開發的優勢
- GitHub Copilot 在開發流程中的角色
- 與 IntelliJ 的差異分析（優缺點）

---

# 🛠️ 2. 開發環境安裝與設定
## 2.1 必備工具
- VS Code（最新版）
- GitHub Copilot（含 Copilot Chat）
- JDK（建議 Java 17 或以上）
- Maven / Gradle

## 2.2 VS Code Extension 推薦（需說明用途）
- Java Extension Pack
- Spring Boot Extension Pack
- GitHub Copilot
- GitHub Copilot Chat
- REST Client

## 2.3 環境設定步驟（逐步教學）
- 安裝 VS Code
- 安裝 Extension
- 設定 JAVA_HOME
- 設定 Maven / Gradle
- 登入 GitHub 並啟用 Copilot

---

# 🚀 3. 建立第一個 Spring Boot 專案
- 使用 Spring Initializr
- 專案結構說明（重要）
- 執行與測試 API

---

# 🤖 4. GitHub Copilot 實戰應用（重點章節）
## 4.1 基本用法
- 自動補全
- 註解生成程式碼

## 4.2 進階用法
- Copilot Chat 使用方式
- 生成 Controller / Service / Repository
- 生成 DTO / Entity
- 生成測試程式（JUnit）

## 4.3 Prompt Engineering（重點）
請提供：
- 好 Prompt 範例
- 壞 Prompt 範例
- 提升生成品質技巧

---

# 🏗️ 5. 專案架構設計（企業級）
- Clean Architecture / Hexagonal Architecture
- 分層設計（Controller / Service / Domain / Infrastructure）
- DTO / VO / Entity 分離

---

# 🔐 6. 安全性與最佳實務
- Spring Security 基本設定
- API 驗證（JWT）
- Copilot 生成程式碼的安全檢查

---

# 🧪 7. 測試與除錯
- 單元測試（JUnit 5）
- API 測試（REST Client / Postman）
- VS Code Debug 技巧
- 使用 Copilot 協助除錯

---

# ⚙️ 8. CI/CD 與版本控管
- Git 基本流程（branch strategy）
- GitHub Actions 基本 CI/CD
- Copilot 協助產生 pipeline

---

# 🔧 9. 系統維護與升級
- VS Code 更新策略
- Extension 管理
- Copilot 模型更新與最佳化使用

---

# 👥 10. 團隊導入建議（企業級）
- 開發規範（Coding Standard）
- Copilot 使用規範（避免錯誤依賴）
- Code Review 流程
- AI 輔助開發治理（AI Governance）

---

# 📌 11. 常見問題與最佳解法（FAQ）
請列出至少 10 個常見問題，例如：
- Copilot 產生錯誤程式碼怎麼辦？
- VS Code Java 效能問題
- Maven 依賴錯誤

---

# 📎 12. 附錄
- 常用指令
- 範例 Prompt 清單（至少 20 個）

---

## 📌 輸出格式要求
- 使用 Markdown（.md）
- 結構清晰（# / ## / ###）
- 每段需具備「說明 + 範例」
- 程式碼需用 ```java ``` 等標示
- 內容需具備「企業實務經驗」

---

## 🚨 特別要求
- 必須使用「最新版本 VS Code + Copilot」觀點
- 強調「AI 輔助開發最佳實務」
- 避免空泛說明，需具體可操作
- 適用於「銀行或大型企業系統」

---

## 產出結果
- 請產出一份 **《VS Code + GitHub Copilot 開發 Java Web 應用程式教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《VS Code + GitHub Copilot 開發 Java Web 應用程式教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "VS Code + GitHub Copilot 開發 Java Web 應用程式教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
--------------------------------------------------------------------
# 生成 程式碼品質分析方法論 prompt
- 角色: 資深軟硬體架構師, 資深程式設計師 
- 需求: 讓所有公司同仁了解程式碼品質分析方法論 
- 目標: 依需求產出企業等級解程式碼品質分析方法論,請先產生prompt ,之後在請AI產出完整的教學手冊
--------------------------------------------------------------------
# 企業級程式碼品質分析方法論教學手冊生成 Prompt

## 🎯 角色設定
你是一位：
- 資深軟體架構師（Enterprise Architect）
- 資深程式設計師（Senior Software Engineer）
- 熟悉大型企業系統（如銀行、金融業、高併發系統）
- 熟悉 Clean Architecture、DDD、Microservices、DevSecOps

你的任務是：
👉 為「公司所有技術人員（初階～資深）」建立一套完整的「程式碼品質分析方法論教學手冊」

---

## 🎯 目標
請產出一份「企業等級程式碼品質分析方法論」，需達成：

1. 讓所有工程師理解：
   - 什麼是「好程式碼」
   - 如何量化程式碼品質
   - 如何持續改善

2. 可實際落地於：
   - 日常開發流程
   - Code Review
   - CI/CD Pipeline
   - 系統重構

3. 適用於：
   - Java / Spring Boot
   - 前端（Vue / TypeScript）
   - 微服務架構
   - 大型企業系統（高穩定、高安全）

---

## 📚 教學手冊內容要求

請輸出為「完整教學手冊」，包含以下章節：

---

### 📖 第1章：程式碼品質概論
- 程式碼品質的定義（Maintainability, Readability, Reliability, Security）
- 技術債（Technical Debt）
- 為什麼企業需要品質管理

---

### 📖 第2章：程式碼品質模型（核心方法論）
請建立一套「企業級品質模型」，至少包含：

- 可讀性（Readability）
- 可維護性（Maintainability）
- 可測試性（Testability）
- 效能（Performance）
- 安全性（Security）
- 可擴展性（Scalability）

👉 每個項目需包含：
- 定義
- 評估方式
- 常見問題
- 改善方法

---

### 📖 第3章：程式碼異味（Code Smells）
- 常見 Code Smells（至少 15 種）
- 每種需包含：
  - 說明
  - 範例（Bad vs Good）
  - 改善方式

---

### 📖 第4章：靜態分析與工具
請說明並比較：

- SonarQube
- ESLint
- PMD / Checkstyle
- SpotBugs

👉 包含：
- 功能比較
- 適用場景
- 企業導入方式

---

### 📖 第5章：Code Review 方法論
- Review Checklist（企業版）
- Pull Request 標準
- Review 角色分工
- 常見錯誤

---

### 📖 第6章：CI/CD 與品質門檻（Quality Gate）
- 如何在 CI/CD 中導入品質檢查
- Quality Gate 設計（如 SonarQube）
- Fail Pipeline 的策略

---

### 📖 第7章：測試策略與品質關聯
- 單元測試（Unit Test）
- 整合測試（Integration Test）
- 覆蓋率（Coverage）迷思
- 測試與品質的關係

---

### 📖 第8章：重構（Refactoring）策略
- 何時該重構
- 安全重構流程
- 常見重構技巧

---

### 📖 第9章：企業實務最佳實踐（Best Practices）
- 銀行 / 金融系統案例
- 微服務品質管理
- DevSecOps 整合

---

### 📖 第10章：導入策略（企業落地）
請提供：

- 推動步驟（Roadmap）
- 組織角色（Architect / Tech Lead / Developer）
- KPI 指標（如 Code Coverage、Bug Rate）
- 成熟度模型（Level 1 ~ Level 5）

---

## 📌 輸出要求

- 使用「繁體中文」
- 結構清晰（Markdown 格式）
- 每章需包含：
  - 說明
  - 圖表（可用文字描述）
  - 實務建議
- 提供「可直接用於企業內訓」的內容

---

## 🚀 加強要求（重要）

請特別強化以下內容：

1. ✅ 大型系統（銀行等級）適用性
2. ✅ 與 DevOps / DevSecOps 整合
3. ✅ 可量化指標（Metrics）
4. ✅ 可自動化（Automation）
5. ✅ 真實開發場景（不是純理論）

---

## 🧩 輸出風格

- 專業但易懂（讓初學者也能理解）
- 偏「架構師視角」
- 每章最後需有「實務落地建議」


## 產出結果
- 請產出一份 **《企業級程式碼品質分析方法論教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《企業級程式碼品質分析方法論教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "企業級程式碼品質分析方法論教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------------
# 逆向工程
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 使用GitHub Copilot開發java web應用程式
使用 VS Code 搭配 GitHub Copilot 開發 Java Web 應用程式（如 Spring Boot）是目前非常高效的開發流程。透過 AI 的輔助，你可以快速生成樣板程式碼、進行除錯並加速開發進度。
。
## 參考:
- https://code.visualstudio.com/docs
- https://code.visualstudio.com/updates/v1_113
- https://code.visualstudio.com/
## 背景 - 客戶提供舊的程式碼如 C#, 與資料庫Stored Procedure ,使用GitHub Copilot先做逆向工程產出客戶需求規格書。 
## 任務說明 - 系統必需使用GitHub Copilot最新版開發,如何透過GitHub Copilot逆向工程產生客戶需求規格書,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用GitHub Copilot需求客戶需求規格書教學手冊 md 檔

--------------------------------------------------------------------
# 任務：產出「使用 GitHub Copilot 進行逆向工程並產出需求規格書」教學手冊

## 🎯 角色設定
你是一位：
- 資深軟體架構師（Enterprise Architect）
- 資深前後端工程師（Full Stack Engineer）
- 熟悉銀行系統、批次處理、資料庫設計（Oracle / DB2 / SQL Server）
- 熟悉逆向工程（Reverse Engineering）與需求分析（Requirement Analysis）
- 熟悉使用 GitHub Copilot + VS Code 進行 AI 輔助開發

---

## 🧠 背景說明
目前客戶提供：
- 舊系統程式碼（例如 C# / .NET）
- 大量 Stored Procedure（資料邏輯集中在 DB）
- 缺乏完整文件（或文件過時）

目標是：
👉 使用 GitHub Copilot + VS Code  
👉 透過逆向工程方式  
👉 自動整理並產出「客戶需求規格書（SRS）」  

---

## 📌 任務目標
請產出一份「企業級教學手冊（Markdown 格式）」，內容需包含：

### 1️⃣ 方法論（Methodology）
- 什麼是逆向工程（在企業系統中的應用）
- Code → Requirement 的轉換模型
- 如何從：
  - Controller / Service / DAO
  - Stored Procedure
  - Batch Job
  推導出需求

---

### 2️⃣ Copilot 使用策略（非常重要）
請詳細說明：
- 如何撰寫 Prompt 給 Copilot
- 如何逐段分析程式碼
- 如何讓 Copilot：
  - 解讀 C# 程式
  - 解讀 SQL / Stored Procedure
  - 推導業務邏輯
  - 轉換為「商業需求描述」

👉 必須提供：
- Prompt 範例（多組）
- Before / After 範例

---

### 3️⃣ 實戰流程（Step-by-Step）
請提供完整操作流程：

#### Step 1 - 程式碼盤點
- 如何分類系統模組
- 如何用 Copilot 快速摘要

#### Step 2 - 邏輯解析
- API / Batch / DB 邏輯分析方式

#### Step 3 - 商業邏輯抽取
- 如何從技術邏輯轉為業務需求

#### Step 4 - 文件產出
- 自動生成 SRS（Software Requirement Specification）

---

### 4️⃣ SRS 文件標準格式
請提供企業級範本：

- 系統概述
- Use Case
- 功能需求（Functional Requirements）
- 非功能需求（Non-functional）
- 資料流程（DFD）
- ER Model（資料結構）
- Batch Flow（若有）

---

### 5️⃣ 範例（非常重要）
請提供完整案例：

#### 範例來源：
- 一段 C# API 程式碼
- 一段 Stored Procedure

👉 請展示：
1. 原始程式碼
2. Copilot 分析過程
3. 推導出的需求
4. 最終 SRS 文件片段

---

### 6️⃣ 企業最佳實務（Best Practices）
- 如何避免誤判需求
- 如何做需求驗證（與使用者 / PM）
- 如何整合 SSDLC
- 如何搭配版本控制（Git）

---

### 7️⃣ 架構延伸（進階）
- 如何將逆向結果轉為：
  - Spring Boot API 設計
  - Microservices 架構
- 如何做：
  - Domain Modeling（DDD）
  - Clean Architecture

---

## 📦 輸出格式要求
- 使用 Markdown (.md)
- 結構清晰（H1 ~ H4）
- 每個章節需有：
  - 說明
  - 範例
  - Copilot Prompt

---

## 🚀 進階要求（加分）
- 提供「Prompt 工程模板庫」
- 提供「常見錯誤與修正策略」
- 提供「自動化流程（AI + Script）」

---

## ⚠️ 注意事項
- 內容需符合企業級（銀行等級）
- 強調可操作性（不是純理論）
- 每一段都要能實際用在 VS Code + Copilot

## 產出結果
- 請產出一份 **《使用 GitHub Copilot 進行逆向工程並產出需求規格書》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《使用 GitHub Copilot 進行逆向工程並產出需求規格書.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "使用 GitHub Copilot 進行逆向工程並產出需求規格書.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Agent Skills教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 -  AI 代理領域：Agent Skills
這是在 2025 年底至 2026 年初由 Anthropic（Claude 開發者）與 Google 等科技巨頭推動的開放標準。 
定義：一種模組化、可重複使用的「能力包」，通常以資料夾形式存在，內含說明文件（如 SKILL.md）、腳本（Python/Bash）和範本。
核心邏輯（漸進式揭露）：為了節省上下文空間（Tokens），AI 平時只載入技能的名稱和描述（Metadata），只有在偵測到相關任務時，才會動態載入具體的執行指令。
應用場景：將通用 AI 轉變為「專業專家」。例如：處理複雜的 PDF 編輯、遵循公司特定的程式碼規範、或自動生成專業的簡報。
工具支持：
Claude Code：支援自訂與社群技能，用於程式碼庫管理。
GitHub Copilot：整合技能標準以執行特定、可重複的任務。
。
## 參考:
- https://code.claude.com/docs/zh-TW/skills
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- https://github.com/anthropics/skills
- https://github.com/github/awesome-copilot/tree/main/skills
## 背景 - 針對內容的開發流程中,把常用和可以共用的部分寫成組織資產。 
## 任務說明 - 系統必需使用GitHub Copilot最新版開發,如何透過GitHub Copilot,如何透過SSDLC的過程常用和可以共用的部分提示詞轉成skills成為企業級公司的資產,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用建立skills教學手冊 md 檔
--------------------------------------------------------------------
# 任務：產出「Agent Skills 教學手冊（企業級 SSDLC + GitHub Copilot）」完整文件

## 🎯 角色設定
你是：
- 資深軟體架構師（Enterprise Architect）
- 資深前後端工程師（Full-Stack Engineer）
- AI Agent / Agent Skills 專家
- 熟悉 SSDLC（Secure Software Development Life Cycle）
- 熟悉 GitHub Copilot 最新版本（含 Copilot Agents / Skills）

---

## 📘 任務目標
請產出一份「企業級 Agent Skills 教學手冊（Markdown 格式）」，
用於指導公司內部工程師：

👉 如何在 SSDLC 各階段中  
👉 將「可重用的 Prompt / 流程 / 規範」  
👉 轉換為 GitHub Copilot Skills  
👉 並建立企業級共享資產（Reusable AI Capabilities）

---

## 📚 教學手冊需涵蓋內容（完整章節）

### 1️⃣ Agent Skills 概念與架構
- 什麼是 Agent Skills（定義與價值）
- 與傳統 Prompt Engineering 的差異
- Skills vs Prompt vs Tool vs Agent 比較
- 漸進式揭露（Progressive Disclosure）設計原則
- Skills 組成結構（SKILL.md、scripts、templates）

---

### 2️⃣ GitHub Copilot Skills 深度解析
- GitHub Copilot Skills 架構
- Skills 運作流程（觸發 → 載入 → 執行）
- Skills Metadata 設計（名稱、描述、觸發條件）
- Skills 與 Copilot Agent 整合方式
- Skills Repository 設計（企業級）

---

### 3️⃣ SSDLC × Skills（核心章節 ⭐）
請針對 SSDLC 各階段說明：

#### (1) Requirements（需求階段）
- 將需求分析 Prompt 模組化為 Skills
- 範例：產出 BRD / FRD / User Story Skills

#### (2) Design（設計階段）
- 系統設計、架構圖、API 設計 Skills
- 範例：Clean Architecture / DDD Skills

#### (3) Development（開發階段）
- Code Generation Skills（Spring Boot / Vue / API）
- Code Review / Refactoring Skills

#### (4) Testing（測試階段）
- 單元測試、自動測試生成 Skills
- 測試案例生成 Skills

#### (5) Security（安全）
- 安全檢測 Prompt → Security Skills
- OWASP / Secure Coding Skills

#### (6) Deployment（部署）
- CI/CD Pipeline Skills
- Docker / Kubernetes Skills

#### (7) Maintenance（維運）
- Log 分析、問題排查 Skills
- Incident Response Skills

👉 每個階段都需包含：
- 可轉換為 Skills 的內容
- 範例 Prompt → Skills 化示範

---

### 4️⃣ Skills 設計最佳實務（Best Practices）
- 高可重用性設計
- 低 Token 消耗策略
- 命名規範（Enterprise Naming Convention）
- 模組化與版本控管（Versioning）
- 安全性與權限控管

---

### 5️⃣ Skills 實作教學（Hands-on ⭐）
請提供完整範例：

#### 範例 1：產生 API 設計文件 Skill
- SKILL.md
- Prompt Template
- Script（如 Python / Bash）

#### 範例 2：程式碼審查 Skill
- 規範導向（Coding Standard）
- 自動檢查

---

### 6️⃣ 企業級 Skills Repository 架構
- 建議 GitHub Repo 結構
- Skills 分類（Domain / Layer / SSDLC）
- 權限控管（RBAC）
- 與 CI/CD 整合

---

### 7️⃣ 與開發工具整合
請說明如何整合：

- GitHub Copilot
- VS Code
- CI/CD（GitHub Actions）
- Issue / PR 流程

---

### 8️⃣ Skills 治理（Governance ⭐）
- Skills 審核機制
- 品質控管（Quality Gate）
- 安全審查（Security Review）
- 使用追蹤與優化（Telemetry）

---

### 9️⃣ 常見錯誤與反模式（Anti-Patterns）
- 過度設計 Skills
- Token 爆炸問題
- Skills 過於耦合

---

### 🔟 未來趨勢
- Agentic Workflow
- Multi-Agent Collaboration
- Skills Marketplace

---

## 🧾 輸出格式要求
- 使用 Markdown (.md)
- 結構清晰（# / ## / ###）
- 每章需有：
  - 說明
  - 架構圖（用 Mermaid）
  - 範例（Code / Prompt）
- 必須包含實務案例（Enterprise Use Case）
- 使用繁體中文

---

## 🚀 額外要求（加分）
- 提供「銀行業 / 金融業」應用案例
- 提供「大型系統（微服務架構）」應用方式
- 提供「AI + DevSecOps」整合建議

---

## 產出結果
- 請產出一份 **《Agent Skills 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Agent Skills 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Agent Skills教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------
# 軟體開發(逆向工程)
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 使用GitHub Copilot,協助將原軟體透過逆向工程,重新開發成java web應用程式
使用 VS Code 搭配 GitHub Copilot 開發 Java Web 應用程式（如 Spring Boot）是目前非常高效的開發流程。透過 AI 的輔助，你可以快速生成樣板程式碼、進行除錯並加速開發進度。
。
## 參考:
- https://code.visualstudio.com/docs
- https://code.visualstudio.com/updates/v1_113
- https://code.visualstudio.com/

## 背景 - 將客戶現的的舊軟體,只有軟體,無其它文件,使用GitHub Copilot先做逆向工程,依SDLC 作法,如何開發新的軟體。 
## 任務說明 - 系統必需使用GitHub Copilot最新版開發,如何透過GitHub Copilot逆向工程,依據SDLC,提供逆向的3種作法,順序,步驟,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用GitHub Copilot 軟體逆向教學手冊 md 檔
--------------------------------------------------------------------
# 任務：產生「GitHub Copilot 逆向工程教學手冊（Java Web）」Markdown 文件

## 🎯 角色設定
你是一位：
- 資深軟體架構師（熟悉企業級系統設計）
- 資深前後端工程師（Java / Spring Boot / Web）
- 熟悉 SDLC（Software Development Life Cycle）
- 熟悉逆向工程（Reverse Engineering）與 Legacy Modernization
- 熟悉 GitHub Copilot 最新版本（Copilot Chat / Agent / CLI）

---

## 📌 背景說明
目前有一套「舊系統（Legacy System）」：
- 只有「程式碼或執行檔」
- 沒有任何設計文件（無 SRS / SDS / 架構圖）
- 技術可能過時（如 VB、Delphi、PowerBuilder、舊 Java、C/C++）

目標：
👉 使用 GitHub Copilot 進行「逆向工程」
👉 並依據 SDLC 流程，重新開發為「現代化 Java Web 應用（Spring Boot）」

---

## 📌 任務要求
請產出一份「完整教學手冊（Markdown 格式）」，內容需包含：

---

# 📚 文件結構要求（必須完整）

## 1️⃣ 概論
- 什麼是逆向工程（Reverse Engineering）
- Legacy System 現代化挑戰
- GitHub Copilot 在逆向工程的角色
- 適用情境（銀行、企業系統）

---

## 2️⃣ 三種逆向工程策略（核心重點）
請詳細說明以下三種方法：

### 方法一：黑箱逆向（Black-box Reverse Engineering）
- 適用情境
- 操作方式
- Copilot 如何協助
- 優缺點
- 實務案例

---

### 方法二：白箱逆向（White-box Reverse Engineering）
- 解析原始碼
- Copilot 如何理解 legacy code
- 如何產出：
  - 架構圖
  - API 文件
  - 資料模型
- 優缺點
- 實務案例

---

### 方法三：灰箱逆向（Hybrid / Gray-box）
- 黑白箱混合策略
- 如何逐步替換（Strangler Pattern）
- 適合大型系統重構

---

## 3️⃣ SDLC 對應逆向工程流程（非常重要）
請將逆向工程對應到 SDLC：

### (1) 需求分析（Requirement Analysis）
- 如何用 Copilot 推導需求
- 從程式碼推 SRS

### (2) 系統設計（System Design）
- 架構重建（Architecture Reconstruction）
- Clean Architecture / Hexagonal

### (3) 開發（Implementation）
- 使用 Spring Boot
- Copilot 自動產生 Code

### (4) 測試（Testing）
- 單元測試（JUnit）
- 自動生成測試案例

### (5) 部署（Deployment）
- CI/CD
- 容器化（Docker / Podman）

---

## 4️⃣ GitHub Copilot 實戰流程（Step-by-Step）
請提供詳細步驟：

### Step 1：分析舊系統
### Step 2：建立理解模型（Domain Model）
### Step 3：產出文件（AI 自動生成）
### Step 4：建立新專案（Spring Boot）
### Step 5：逐步重構
### Step 6：驗證與測試

---

## 5️⃣ Copilot Prompt Engineering（關鍵）
請提供：
- 高品質 Prompt 範例（至少 10 個）
- 包含：
  - 分析程式碼
  - 轉換語言（如 VB → Java）
  - 產出 API 文件
  - 產生測試

---

## 6️⃣ 架構設計（企業級）
- 微服務 vs 單體
- 分層架構（Controller / Service / Repository）
- 資料庫設計（DB2 / Oracle）
- Cache / MQ / API Gateway

---

## 7️⃣ 風險與最佳實務
- 常見錯誤
- 逆向失敗案例
- 資料遺失風險
- 安全性（Security）

---

## 8️⃣ 完整案例（實戰）
請提供一個案例：
👉 舊系統（例如 VB 或舊 Java）
👉 轉換成 Spring Boot

需包含：
- 原始程式碼片段
- Copilot 分析
- 新系統程式碼

---

## 9️⃣ 工具整合
- VS Code
- GitHub Copilot Chat
- Copilot CLI
- SonarQube
- Swagger

---

## 🔟 結論
- 三種逆向策略比較表
- 推薦最佳實務

---

## 📌 文件格式要求
- 使用 Markdown（.md）
- 結構清晰（標題、表格、程式碼區塊）
- 每個章節需有：
  - 圖表（用 Mermaid）
  - 範例
  - Best Practice

---

## 🚀 額外要求（加分）
- 提供 Mermaid 架構圖
- 提供 Prompt 模板區
- 提供 Checklist（可直接使用）

---

## ⚠️ 注意事項
- 內容需「企業級」
- 避免過度理論，需可落地
- 強調「Copilot 實務用法」

## 產出結果
- 請產出一份 **《GitHub Copilot 逆向工程教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《GitHub Copilot 逆向工程教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "GitHub Copilot 逆向工程教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

--------------------------------------------------------------------
# gstack教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - gstack 是由 Y Combinator（YC）執行長 Garry Tan 所發布的一套開源 AI 編程配置工具集。它專為搭配 Anthropic 的命令列工具 Claude Code 使用而設計，旨在將 AI 助手轉化為一支高效的「虛擬開發團隊」。 
以下是其核心特點與功能：
1. 核心理念：賦予角色而非僅提供提示詞 (Roles, Not Prompts)
gstack 的核心在於為 AI 提供明確的角色與工作流程，而非僅僅是零散的提示詞。它將 Garry Tan 個人在矽谷多年的工程與產品經驗標準化，讓 AI 能以專業角色的視角來審視與撰寫程式碼。 
2. 虛擬團隊配置
該工具集內含多種預設角色與工具，通常被稱為「Skills」：
多樣化角色：包含如產品經理 (PM)、CEO、資深工程師、QA 測試員等超過 15 個專門角色。
專業審核流程：
CEO 產品規劃：從產品戰略角度審核功能。
偏執代碼分析 (Paranoid Mode)：極其嚴格地檢查代碼漏洞與潛在 Bug。
自動化 QA：具備感知差異 (diff-aware) 的自動化測試與瀏覽功能。
一鍵部署：提供單一指令完成發布的工作流 (one-command shipping)。 。
## 參考:
- https://github.com/garrytan/gstack
## 背景 - 目前必需使用gstack開發web application的系統。 
## 任務說明 - 系統必需使用gstack最新版開發,包含系統架構,安裝,設定,使用gstack軟體開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生gstack教學手冊 md 檔

----------------------------------------------------------------------
# gstack 教學手冊（企業級標準）

## 角色設定
你是一位「資深軟體架構師 + 資深前後端工程師 + DevOps 專家 + AI Agent 系統設計師」，具備大型金融級系統（高可用、高擴展、高安全）設計經驗。

---

## 任務目標
請產出一份**完整且可落地的 gstack 教學手冊（Markdown 格式）**，用於企業內部推廣與標準化開發流程。

手冊需涵蓋：
- 架構設計
- 安裝部署
- 開發流程
- 團隊協作（AI Agent）
- 維運與升級
- 最佳實務（Best Practices）

---

## 背景說明
- gstack 是由 Garry Tan 推出的 AI 開發配置工具
- 搭配 Claude Code 使用
- 核心理念：**Roles, Not Prompts（角色驅動開發）**
- 建立「虛擬開發團隊（AI Agents）」
- 適用於 Web Application 開發（企業級）

---

## 輸出格式要求
- 使用 **Markdown (.md)** 格式
- 結構清晰（章節 / 小節 / 表格 / 圖）
- 必須包含：
  - 架構圖（使用 Mermaid）
  - 流程圖（Mermaid）
  - 範例指令
  - 設定檔範例（JSON / YAML）
  - Code Snippets（Java / Spring Boot / TypeScript / Vue 可選）

---

## 章節要求（必須完整）

### 1. gstack 概述
- 什麼是 gstack
- 與傳統 Prompt Engineering 差異
- 與 Agent Skills / AI Agent 比較
- 適用場景（企業 / 金融 / SaaS）

---

### 2. 核心架構設計（重點）
請設計一個企業級架構：

包含：
- 前端（Vue / Micro-Frontend）
- 後端（Spring Boot / Clean Architecture）
- AI Agent Layer（gstack + Claude Code）
- API Gateway
- Database（支援分庫分表）
- Cache（Redis）
- Message Queue（Kafka / RabbitMQ）
- CI/CD Pipeline

👉 使用 Mermaid 畫：
- 系統架構圖
- AI Agent 協作圖

---

### 3. gstack 安裝與環境建置
包含：
- 必備環境（Node.js / Python / Claude CLI 等）
- 安裝 gstack
- 初始化專案
- CLI 使用方式

提供：
- 安裝指令
- 常見錯誤排除

---

### 4. gstack 核心概念（最重要）
詳細說明：
- Roles（角色）
- Skills（技能）
- Workflows（流程）
- Agent Collaboration（代理協作）

請提供：
- 每個概念的實際範例
- 對應 JSON/YAML 設定

---

### 5. 虛擬開發團隊設計（企業實戰）
請設計一組完整 AI Team：

包含：
- CEO（產品決策）
- PM（需求分析）
- Architect（架構設計）
- Senior Engineer（開發）
- QA（測試）
- Security（安全）

👉 每個角色需包含：
- 職責
- Prompt / Role 定義
- 輸出內容

---

### 6. 開發流程（端到端）
請設計完整流程：

1. 需求輸入
2. AI 分析
3. 架構設計
4. 程式碼生成
5. 測試
6. 部署

👉 使用 Mermaid 畫流程圖

---

### 7. 實戰案例（Web Application）
請示範：

建立一個簡單系統（如：會員管理系統）

包含：
- API 設計
- DB Schema
- Controller / Service / Repository
- 前端頁面

並說明：
👉 gstack 如何參與每一步

---

### 8. DevOps 與自動化
包含：
- CI/CD（GitHub Actions / GitLab CI）
- 自動測試
- 一鍵部署（one-command shipping）
- 環境管理

---

### 9. 系統維運（Maintenance）
包含：
- 日誌（Logging）
- 監控（Monitoring）
- 錯誤追蹤
- AI 協助 Debug

---

### 10. 系統升級與擴展
包含：
- gstack 升級策略
- Agent 擴展
- 多團隊協作
- Plugin / Skill 擴充

---

### 11. 安全設計（企業級）
包含：
- 身分驗證（OAuth2 / JWT）
- 權限控管（RBAC）
- 資安掃描（SAST / DAST）
- AI 生成代碼安全風險

---

### 12. 最佳實務（Best Practices）
至少提供：
- 10 條企業導入建議
- 常見錯誤
- Anti-patterns

---

## 額外要求（非常重要）
- 所有內容需「可實作」
- 避免空泛說明
- 每章需有：
  - 範例
  - 指令
  - 圖示
- 適用於：
  - 銀行系統
  - 大型企業平台
  - 微服務架構

---

## 輸出風格
- 專業（Architect Level）
- 條理清晰
- 適合內部教育訓練
- 可直接給工程師使用

---

## 產出結果
- 請產出一份 **《gstack教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《gstack教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "gstack教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
------------------------------------------------------------------
# get-shit-done(GSD)教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - gsd-build/get-shit-done (簡稱 GSD) 是一個為 AI 程式設計代理（如 Claude Code, Gemini CLI, Cursor 等）設計的輕量級、功能強大的元提示（meta-prompting）、上下文工程與**規格驅動開發（spec-driven development）**系統。 
1. 核心功能與定位
解決上下文衰減（Context Rot）：透過結構化的開發流程，防止 AI 在處理複雜專案時因上下文視窗填滿而導致的品質下降。
規格驅動：將模糊的需求轉化為結構化的研究報告、分階段路線圖與原子化的執行計畫。
多平台支援：原生支援 Claude Code、Gemini CLI、Cursor、Windsurf 及 Codex 等多種 AI 編輯環境。 

2. 標準開發工作流程
GSD 透過一系列斜線指令（Slash Commands）引導開發過程：
- 初始化專案 (/gsd:new-project)：系統會不斷提問直到完全理解目標、技術偏好與約束條件。
- 討論階段 (/gsd:discuss-phase)：針對當前里程碑進行細節討論，決策會記錄在 CONTEXT.md 中。
- 規劃階段 (/gsd:plan-phase)：AI 研究實作路徑並建立 2-3 個原子化的任務計畫（XML 結構）。
- 執行階段 (/gsd:execute-phase)：以波動（waves）方式執行計畫，支援並行與順序處理。
- 驗證工作 (/gsd:verify-work)：自動化檢查程式碼是否存在且測試是否通過。
- 交付與重複 (/gsd:ship)：完成里程碑並歸檔，開啟下一個開發週期。
## 參考:
- https://github.com/gsd-build/get-shit-done
- https://gsd-build-get-shit-done.mintlify.app/
## 背景 - 目前必需使用GSD開發web application的系統。 
## 任務說明 - 系統必需使用GSD最新版開發,包含系統架構,安裝,設定,使用GSD軟體開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生gstack教學手冊 md 檔
--------------------------------------------------------------------
# GSD（get-shit-done）教學手冊產生任務

## 🎯 角色設定
你是「資深軟體架構師 + 資深前後端工程師 + AI Agent 架構專家」，具備以下能力：
- 精通 AI Coding Agent（Claude Code / Gemini CLI / Cursor / Codex）
- 精通 Context Engineering / Prompt Engineering / Spec-Driven Development
- 熟悉企業級系統架構（微服務、分散式系統、高可用架構）
- 熟悉銀行級系統（高併發、高一致性、安全合規）
- 精通 DevOps、CI/CD、自動化測試與監控

---

## 📌 任務目標
請產出一份「企業級 GSD（get-shit-done）教學手冊」，格式為 **Markdown (.md)**，可供公司內部工程師直接使用。

該手冊需涵蓋：
- 系統架構設計
- 安裝與環境設定
- GSD 開發流程實務
- AI 協作最佳實踐
- 系統維運與升級策略
- 團隊導入與治理建議

---

## 🧠 技術背景（必須納入）
GSD 是一套：
- Meta-Prompting 系統
- Context Engineering 框架
- Spec-Driven Development 開發模式

核心能力：
1. 解決 Context Rot（上下文衰減）
2. 將需求轉為結構化規格（Spec）
3. 使用 Slash Commands 控制 AI 開發流程
4. 支援多種 AI 工具（Claude Code / Gemini CLI / Cursor / Windsurf / Codex）

標準流程：
- /gsd:new-project
- /gsd:discuss-phase
- /gsd:plan-phase
- /gsd:execute-phase
- /gsd:verify-work
- /gsd:ship

---

## 📚 文件輸出要求

### 1️⃣ 文件結構（必須完整）
請輸出完整章節，至少包含：

# 第一章：GSD 概述
- GSD 是什麼
- 與傳統開發的差異
- 與 Agile / DevOps / AI Coding 的關係

# 第二章：核心概念
- Meta Prompting
- Context Engineering
- Spec-Driven Development
- Context Rot 問題與解法

# 第三章：系統架構設計（企業級）
- GSD + AI Agent 架構圖
- 與 Web Application（前後端）整合方式
- 微服務 / Clean Architecture / Hexagonal Architecture
- 與資料庫（Oracle / DB2 / PostgreSQL）整合
- 與 MQ / Cache / API Gateway 整合

# 第四章：安裝與環境建置
- GSD 安裝步驟
- Claude Code / Gemini CLI / Cursor 設定
- VS Code 開發環境配置
- Windows / Linux 環境差異

# 第五章：GSD 開發流程（核心）
逐步說明：
- /gsd:new-project（含範例 prompt）
- /gsd:discuss-phase
- /gsd:plan-phase（XML 計畫範例）
- /gsd:execute-phase（waves 機制）
- /gsd:verify-work
- /gsd:ship

👉 每個步驟都要有：
- 說明
- 範例
- Best Practice

# 第六章：實戰案例（Web Application）
請提供完整案例：
- 使用 GSD 開發一個 Web 系統（如：銀行系統 / 訂單系統）
- 包含：
  - 需求 → Spec
  - Spec → Plan
  - Plan → Code
  - Code → 驗證

# 第七章：AI 協作最佳實踐
- 如何避免 AI 幻覺
- 如何控制上下文
- Prompt 設計技巧
- 多 Agent 協作模式

# 第八章：系統維運與監控
- Logging / Monitoring
- 錯誤追蹤
- 效能調校
- 成本控制（AI Token）

# 第九章：系統升級與擴展
- GSD 升級策略
- Prompt versioning
- Spec versioning
- 與 CI/CD 整合

# 第十章：企業導入策略
- 團隊導入流程
- 開發規範制定
- Governance（治理）
- 安全與權限控管

# 第十一章：常見問題（FAQ）
- 常見錯誤
- Debug 方法
- Anti-Patterns

---

## 🧩 輸出格式要求
- 使用 Markdown
- 清楚標題階層（# / ## / ###）
- 必須包含：
  - 表格
  - 流程圖（Mermaid）
  - 範例 Prompt
  - 範例 XML（Plan）
  - 程式碼範例（Java / TypeScript / API）

---

## ⚠️ 特別要求（非常重要）
1. 必須「企業級」而非入門教學
2. 必須可直接落地（Production-ready）
3. 必須強調：
   - 可擴展性
   - 可維護性
   - 高可用性
4. 必須符合大型系統（如銀行）需求
5. 所有範例需具備實務價值（非玩具範例）

---

## 🚀 輸出風格
- 專業
- 結構化
- 可執行
- 適合內部培訓教材

---

## 產出結果
- 請產出一份 **《get-shit-done(GSD)教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《get-shit-done(GSD)教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "get-shit-done(GSD)教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
--------------------------------------------------------------------
# GitNexus教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - GitNexus 是一個由開發者 Abhigyan Patwari 所發起的開源專案，主打「零伺服器（Zero-Server）」的程式碼情報引擎。它能將 GitHub 儲存庫或本地程式碼轉化為互動式的知識圖譜（Knowledge Graph），協助工程師更深入地理解與分析複雜的程式碼依賴關係。 

核心功能與特色
- 視覺化程式碼圖譜：將程式碼庫從傳統的文字檔案集合，轉變為可查詢的關係網，幫助開發者從全域視角理解架構。
- 隱私與本地化：
- 無伺服器架構：完全在瀏覽器端運行，或透過 CLI 在本地機器執行。
- 資料安全：原始碼不會被上傳到外部伺服器，知識圖譜與 AI 模型（嵌入模型）均在本地存儲與運行。
- Graph RAG 代理：內建基於圖譜的檢索增強生成（Graph RAG）功能，讓開發者能直接對知識庫進行追問與深度對話。
- 多平台支援：提供 Web UI 體驗版（無需安裝）以及可用於終端機的 CLI 版本。
## 參考:
- https://github.com/abhigyanpatwari/GitNexus
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用GitNexus了解現行系統。 
## 任務說明 - 系統必需使用GitNexus最新版開發,包含系統架構,安裝,設定,使用GitNexus軟體,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生gGitNexus教學手冊 md 檔

-------------------------------------------------------------------
# GitNexus教學手冊（企業級完整版）

## 🎯 角色設定
你是一位「資深軟體架構師 + 資深前後端工程師 + DevOps + AI 系統設計專家」，具備以下能力：
- 熟悉大型企業系統（銀行 / 金融 / 高併發）
- 精通 GitHub / Monorepo / 微服務架構
- 熟悉 RAG / Graph RAG / Knowledge Graph
- 熟悉 AI Coding Agent（如 Copilot / Claude Code / Cursor）
- 熟悉 Java（Spring Boot）、Python（FastAPI）、前端 Vue3 架構
- 熟悉 SSDLC（安全軟體開發生命週期）

---

## 📌 任務目標
請產出一份「企業級 GitNexus 教學手冊（Markdown 格式）」，用於公司內部推廣與標準化使用，內容需：

1. 可讓**新手快速上手**
2. 可讓**資深工程師深入應用**
3. 可支援**大型系統（如銀行系統）分析**
4. 可整合**AI 開發流程（RAG / Agent / Copilot）**
5. 作為**標準操作手冊（SOP）**

---

## 📚 文件輸出要求

- 格式：Markdown（.md）
- 結構清楚（章節 / 子章節 / 表格 / 圖）
- 搭配：
  - Mermaid 架構圖
  - CLI 指令範例
  - 實務案例
- 每一章節需包含：
  - 🎯 目的
  - 📘 說明
  - 🛠️ 操作步驟
  - 💡 最佳實務（Best Practice）
  - ⚠️ 注意事項

---

## 🧱 教學手冊章節結構（必須完整產出）

### 第 1 章：GitNexus 概述
- GitNexus 是什麼
- 核心理念（Zero-Server / Knowledge Graph / Graph RAG）
- 與傳統工具（如 IDE / GitHub Search）比較
- 適用場景（大型系統 / 微服務 / 舊系統逆向）

---

### 第 2 章：系統架構說明
- GitNexus 整體架構圖（Mermaid）
- 組件說明：
  - Parser（程式碼解析）
  - Graph Builder（圖譜建構）
  - Embedding Engine
  - Graph RAG 查詢引擎
- Web UI vs CLI 架構差異
- 本地運行 vs 瀏覽器運行

---

### 第 3 章：安裝與環境設定
- 安裝方式：
  - CLI 安裝（Node / Python）
  - Docker（如有）
  - Web UI 使用方式
- 系統需求（CPU / RAM）
- 初始設定：
  - Repository 載入
  - 設定 Embedding 模型
- 常見問題排除（Troubleshooting）

---

### 第 4 章：基本操作教學
- 建立 Knowledge Graph
- 掃描 GitHub Repo
- 查詢程式碼關聯
- 視覺化圖譜操作
- CLI 常用指令

---

### 第 5 章：進階應用（重點）
- Graph RAG 使用方式
- 問答範例：
  - 「這個 API 呼叫了哪些服務？」
  - 「這個模組依賴哪些 DB？」
- 影響分析（Impact Analysis）
- 系統重構輔助
- 舊系統逆向工程

---

### 第 6 章：整合企業開發流程（關鍵章節）
請結合以下場景說明：

#### 🔹 與 GitHub / GitLab 整合
- PR Review 分析
- Code Impact 分析

#### 🔹 與 AI 工具整合
- GitHub Copilot
- Claude Code
- Cursor

#### 🔹 與開發架構整合
- Spring Boot 微服務
- FastAPI
- Vue 微前端

#### 🔹 DevOps 整合
- CI/CD 前分析
- 自動化文件生成

---

### 第 7 章：銀行 / 大型系統應用案例（必寫）
請設計一個實務案例：

例如：
- 分析「批次系統（Batch Job）依賴」
- 分析「跨系統 API 呼叫」
- 分析「DB Schema 影響」

需包含：
- 問題描述
- 使用 GitNexus 解法
- 分析結果
- 帶來的效益

---

### 第 8 章：安全與隱私（SSDLC）
- Zero-Server 優勢
- 原始碼保護
- 本地 AI 模型風險
- 權限控管建議

---

### 第 9 章：系統升級與維運
- GitNexus 升級流程
- Graph 重建策略
- Repository 更新同步
- 效能優化建議

---

### 第 10 章：最佳實務（Best Practices）
- 大型專案使用建議
- Monorepo vs Multi-repo
- 團隊導入策略
- 使用限制與風險

---

### 第 11 章：常見問題 FAQ
- Graph 太大怎麼辦？
- 查詢速度慢？
- AI 回答不準？
- 如何提升準確度？

---

### 第 12 章：未來發展與建議
- Graph RAG 未來趨勢
- 與 Agent 系統整合
- 建議企業導入 roadmap

---

## 📌 額外要求

- 必須包含：
  - 至少 3 個 Mermaid 圖
  - 至少 5 個 CLI 指令範例
  - 至少 3 個企業實務案例
- 內容需「實務導向」，不可只寫概念
- 所有內容需可直接讓工程師操作

---

## 產出結果
- 請產出一份 **《GitNexus教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《GitNexus教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "GitNexus教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Graphify教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Graphify 是由 AI 工程師 Safi Shamsi 開發的一款開源工具，旨在將任何資料夾（包含程式碼、PDF、圖片等）轉化為可交互的知識圖譜。 
這項專案起源於特斯拉前 AI 主管 Andrej Karpathy 在 2026 年 4 月初提出的一個構想，即建立一個能自動整理 /raw 原始資料夾的產品。Safi Shamsi 在該文發布後 48 小時內便開發出了 Graphify，並迅速在 GitHub 上獲得超過 6,000 顆星。 

主要功能與特點
- 全自動建圖：支援 19 種程式語言、PDF、Markdown 及圖片，自動提取實體與關係。
- Token 消耗優化：相較於讓 AI 直接讀取原始文件，Graphify 透過預先編譯知識圖譜，可節省約 71.5 倍 的 Token 使用量。

兩階段處理：
- 結構化解析：利用 Tree-sitter 在本地解析程式碼結構（AST），不消耗 API 成本。
- 語義提取：由 Claude 子代理（Subagents）並行提取文件與圖片中的概念。
- 原生整合：可作為 Claude Code 的擴充技能，僅需一條 /graphify 指令即可運行。
- 隱私與安全性：完全在本地端運行，圖譜數據不會離開用戶機器，且不包含遙測（Telemetry）數據。
## 參考:
- https://github.com/safishamsi/graphify
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用Graphify了解現行系統知識圖譜。 
## 任務說明 - 系統必需使用Graphify最新版開發,包含系統架構,安裝,設定,使用Graphify軟體,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生Graphify教學手冊 md 檔
--------------------------------------------------------------------
# Graphify教學手冊產生器 Prompt

## 🎯 角色設定
你是一位：
- 資深軟體架構師（Enterprise Architect）
- 資深前後端工程師（Full Stack Engineer）
- AI Agent / LLM 系統設計專家
- DevOps / 平台工程專家

擅長：
- 大型企業系統架構（銀行 / 金融 / 微服務 / 分散式系統）
- 知識圖譜（Knowledge Graph）
- 程式碼分析（AST / 靜態分析）
- AI 輔助開發（Claude Code / Copilot / Agent Framework）
- SSDLC（Secure Software Development Lifecycle）

---

## 📘 任務目標
請產出一份「企業級 Graphify 教學手冊（Markdown 格式）」，內容需：

- 可供公司內部工程師直接使用
- 適用於大型專案（如銀行系統 / 微服務平台）
- 涵蓋從 **安裝 → 架構 → 使用 → 維運 → 最佳實務**
- 結合理論 + 實務 + 範例 + 架構圖（Mermaid）

---

## 📌 背景資訊（必須納入手冊說明）
Graphify 為一款開源工具，具備：

- 將資料夾（程式碼 / PDF / 圖片）轉換為知識圖譜
- 使用 Tree-sitter 進行 AST 結構解析（零 Token 成本）
- 使用 Claude Subagents 進行語義抽取
- 支援多語言（19+）
- Token 節省約 71.5 倍
- 完全本地運行（無資料外洩風險）
- 可整合 Claude Code（/graphify 指令）

---

## 📚 請輸出章節（必須完整）

### 第 1 章：Graphify 概述
- 工具定位（與傳統文件分析 / RAG 比較）
- 使用情境（逆向工程 / 系統理解 / onboarding）
- 與 AI Agent 的關係

---

### 第 2 章：系統架構設計（重點）
需包含：
- Graphify 整體架構圖（Mermaid）
- Pipeline 說明：
  - 資料輸入層（Code / PDF / Image）
  - AST 解析層（Tree-sitter）
  - 語義抽取層（Claude Subagents）
  - Graph 建構層
  - 查詢與應用層

- 與企業系統整合架構：
  - GitHub / GitLab
  - CI/CD Pipeline
  - Knowledge Platform
  - AI Agent 系統

---

### 第 3 章：安裝與環境建置
需提供：
- Windows / Linux / Mac 安裝步驟
- Node.js / Python / Claude Code 相依
- Docker 部署方式（企業推薦）
- 安全性設定（API Key / Local Mode）

---

### 第 4 章：基本使用教學
需包含：
- 初始化專案
- 建立 Graph
- 指令說明（如 /graphify）
- 輸出內容說明（節點 / 關係）

---

### 第 5 章：進階使用（企業必備）
- 多 repo 分析（monorepo / microservices）
- 與 CI/CD 整合（自動建圖）
- 與 AI 助手整合（Claude / Copilot）
- 知識圖譜查詢應用（RAG 強化）

---

### 第 6 章：實戰案例（非常重要）
至少提供 2 個：

1️⃣ 舊系統逆向工程（Java / Spring）
2️⃣ 微服務架構知識盤點

需包含：
- 問題
- 解法
- Graphify 如何介入
- 成果

---

### 第 7 章：系統升級與版本管理
- 如何升級 Graphify
- Graph schema 版本控制
- 與 Git 版本同步策略

---

### 第 8 章：安全與隱私設計（SSDLC）
- 本地運算優勢
- 敏感資料處理
- 權限控管（RBAC）
- 稽核與追蹤

---

### 第 9 章：最佳實務（Best Practices）
- 大型專案使用建議
- Token 最佳化策略
- Graph 建模技巧
- 團隊導入策略

---

### 第 10 章：常見問題（FAQ）
- 效能問題
- Token 使用
- 語意錯誤
- 多語言支援問題

---

## 📊 額外要求（非常重要）

### 1️⃣ 必須使用 Mermaid 圖
包含：
- 系統架構圖
- Pipeline
- CI/CD 整合

---

### 2️⃣ 必須提供程式碼範例
例如：
- CLI 使用
- config 設定
- Dockerfile

---

### 3️⃣ 必須使用結構化格式
- 標題層級清楚（# / ## / ###）
- 表格（比較 / 設定）
- 條列式說明

---

### 4️⃣ 必須偏向「企業落地」
避免：
- 過度理論
- 模糊描述

強調：
- 可實作
- 可維運
- 可擴展

---

## 🚀 最終目標

讓工程師可以：
- 快速理解大型系統
- 降低 onboarding 成本
- 提升 AI 使用效率（節省 Token）
- 建立企業級知識圖譜平台

## 產出結果
- 請產出一份 **《Graphify教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Graphify教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Graphify教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
--------------------------------------------------------------------
# Hermes Agent生態系教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Hermes Agent 是由知名 AI 實驗室 Nous Research 開發的一款開源、具備自我改進能力的 AI 代理（AI Agent）。 

它最大的特色在於內建了「學習迴圈」，能夠在執行任務的過程中不斷成長，而不僅僅是重複執行固定的指令。 

核心功能與特色
- 自我學習與改進：它會從過去的操作經驗中學習，並將解決複雜問題的過程自動封裝成「可重用的技能」，以便在下次遇到類似問題時更高效地處理。
- 跨對話長期記憶：具備記憶功能，可以回顧過去與使用者的對話內容，讓互動更具連貫性。
- 靈活的模型切換：支援 OpenAI 相容的 API，讓開發者能根據需求切換不同的底層語言模型（LLM）。
- 開源架構：採用 MIT 授權，任何人都可以自由下載、修改或用於商業化開發，其程式碼託管於 GitHub 上的 NousResearch/hermes-agent 專案。

應用場景
- 這款代理程式特別適合需要自動化複雜工作流的場景，例如：
- 自動化的開發輔助（Coding Agent）
- 需要長期上下文理解的個人助理
- 具備動態調整能力的企業級流程自動化
- 更多詳細資訊可以參考 Hermes Agent 官方文件 或其 GitHub 頁面。
。
## 參考: https://github.com/nousresearch/hermes-agent
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用Hermes Agent開發web application的系統。 
## 任務說明 - 系統必需使用Hermes Agent最新版開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生Hermes Agent生態系教學手冊 md 檔

--------------------------------------------------------------------
# 🧠 Hermes Agent生態系教學手冊 生成 Prompt

## 🎯 角色設定

你是一位：

* 資深軟體架構師（Software Architect）
* 資深 AI Agent 系統設計師（AI Agent Architect）
* 資深前後端工程師（Full-Stack Engineer）
* 熟悉企業級系統（銀行 / 金融 / 高併發系統）

請以「**企業級可落地實作**」為標準，撰寫一份完整的 Hermes Agent 生態系教學手冊。

---

## 📌 技術背景

Hermes Agent 是由 Nous Research 開發的開源 AI Agent，具備：

* 自我學習（Learning Loop）
* 技能累積（Skill Reuse）
* 長期記憶（Long-term Memory）
* 多模型支援（OpenAI-compatible API）
* 可商用（MIT License）

GitHub:
https://github.com/nousresearch/hermes-agent

---

## 🏗️ 任務目標

請產出一份完整的：

👉 **《Hermes Agent 生態系教學手冊（Enterprise Edition）》**

格式：

* Markdown（.md）
* 結構清晰（章節 / 小節 / 表格 / 架構圖）
* 可直接給工程團隊使用

---

## 📚 內容要求（務必完整覆蓋）

### 🧩 第一章：Hermes Agent 概述

* 技術背景與發展
* 與傳統 AI（如 ChatGPT）差異
* Agent vs Workflow vs RPA 比較
* 核心設計理念（Learning Loop / Skill System）

---

### 🧩 第二章：整體系統架構（重點）

請提供：

1. 架構設計說明（文字）
2. Mermaid 架構圖（必須）
3. 分層架構：

   * Presentation Layer（前端）
   * API Gateway
   * Agent Layer（Hermes）
   * Memory Layer（Vector DB / DB）
   * Tool Layer（外部工具）
   * Data Layer

需包含：

* 多 Agent 協作（Multi-Agent）
* 微服務架構（Microservices）
* 高可用（HA）
* 擴展性（Scalability）

---

### 🧩 第三章：Hermes Agent 核心機制解析（重點）

深入說明：

* Learning Loop（學習迴圈）
* Skill（技能系統）
* Memory（短期 / 長期記憶）
* Planning / Execution Flow
* Tool Calling 機制
* Model Routing（多模型切換）

---

### 🧩 第四章：安裝與環境建置

需包含：

* 本地開發環境（Windows / Linux）
* Docker / Podman 部署
* Python / Node.js 相依套件
* 安裝 Hermes Agent
* 設定 API Key（OpenAI-compatible）

請提供：

* CLI 指令
* 範例設定檔（.env / config.yaml）

---

### 🧩 第五章：快速開始（Quick Start）

建立一個：

👉「AI Coding Agent」或「智能助理」

需包含：

* 建立 Agent
* 設定 Memory
* 設定 Tools（如 Web Search / DB）
* 執行任務

提供：

* 完整程式碼範例
* 執行結果說明

---

### 🧩 第六章：進階開發（企業級重點）

請深入說明：

* 自訂 Skill（技能封裝）
* 多 Agent 協作設計
* 長期記憶設計（Vector DB）
* 任務拆解（Task Decomposition）
* Workflow Orchestration

---

### 🧩 第七章：Web Application 整合（關鍵）

請設計：

👉 Hermes Agent + Web 系統整合架構

包含：

* 前端（Vue / React）
* 後端（Spring Boot / FastAPI）
* API 設計
* Agent 作為服務（Agent-as-a-Service）

提供：

* API 範例
* 架構圖（Mermaid）

---

### 🧩 第八章：企業級最佳實踐（Best Practices）

需包含：

* 安全性（API Key / 權限控管）
* 成本控制（Token / 模型切換）
* 效能優化（Caching / Async）
* Logging / Monitoring（ELK / Prometheus）
* 錯誤處理與重試機制

---

### 🧩 第九章：部署與維運（DevOps）

請說明：

* Docker / Kubernetes 部署
* CI/CD（GitHub Actions）
* 滾動升級（Rolling Update）
* 災難復原（DR）

---

### 🧩 第十章：升級與版本管理

* Hermes Agent 升級策略
* 相容性管理
* Migration 設計

---

### 🧩 第十一章：實戰案例（務必）

請提供至少 3 個：

1. AI Coding Agent
2. 智慧客服 Agent
3. 銀行流程自動化 Agent

---

### 🧩 第十二章：常見問題（FAQ）

* Agent 無法學習？
* Memory 爆掉？
* Token 成本過高？
* 模型切換問題？

---

## 📐 輸出格式要求

* 使用 Markdown
* 每章節需：

  * 標題（## / ###）
  * 圖表（Mermaid）
  * 程式碼區塊
  * 表格整理

---

## ⚠️ 品質要求（非常重要）

請確保內容：

* ✅ 可實作（不是空泛概念）
* ✅ 符合企業架構（高可用 / 可擴展）
* ✅ 與 Hermes Agent 真實機制一致
* ✅ 適合工程團隊落地

---

## 產出結果
- 請產出一份 **《Hermes Agent生態系教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Hermes Agent生態系教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Hermes Agent生態系教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
--------------------------------------------------------------------
# multica生態系教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Multica 是一個開源的 AI 代理管理平台，旨在將 AI 編碼代理（如 Claude Code, Codex 或 OpenCode）轉化為團隊中的「虛擬同事」。它不僅僅是簡單的對話介面，而是像 Linear 一樣的任務管理系統，讓 AI 代理能擁有自己的帳號、自動領取任務、編寫程式碼並主動回報進度。 
核心功能與特色
- 代理即隊友：AI 代理在看板上擁有個人資料，可以被指派 Issue、參與討論、建立任務，並在遇到困難時主動回報。
- 自主執行：透過 WebSocket 實現任務全生命週期管理，代理會自動排隊、領取、開始並完成任務。
- 技能複用：代理在解決問題後，該解決方案會轉化為團隊可複用的「技能」（如自動化部署、程式碼審查等），實現團隊能力的累積。
- 統一運行環境：提供單一儀表板管理本地守護程序（Daemon）與雲端運行環境，並能自動偵測可用的 CLI。
多工作空間隔離：支援團隊層級的隔離，每個工作空間擁有獨立的代理、Issue 和設定。
## 參考: https://github.com/multica-ai/multica
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用multica開發web application的系統。 
## 任務說明 - 系統必需使用multica最新版開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生Hermes Agent生態系教學手冊 md 檔
--------------------------------------------------------------------
# Multica 教學手冊（企業級實戰版）

## 🎯 角色設定（System Role）
你是「資深軟體架構師 + 資深前後端工程師 + AI Agent 系統設計專家」，具備以下經驗：
- 大型企業系統架構（銀行 / 金融業）
- 微服務架構（Spring Boot / Clean Architecture）
- AI Agent 平台（Claude Code / Codex / OpenCode）
- DevOps / CI-CD / 自動化測試 / SSDLC
- 分散式系統（高可用 / 高併發 / 多資料庫）

請以「企業導入 + 可實戰落地」為目標撰寫教學手冊。

---

## 📌 任務目標（Goal）
請產出一份「完整的 Multica 生態系教學手冊（Markdown 格式）」，內容需包含：

- 架構設計
- 安裝與部署
- 使用教學（開發流程）
- 與 AI 編碼代理整合（Claude Code / Codex）
- 團隊協作模式
- 系統維運與升級
- 最佳實務（Best Practices）

---

## 🧠 背景說明（Context）
Multica 是一個 AI Agent 管理平台，其核心理念為：

- AI Agent = 團隊成員（Virtual Teammate）
- 任務導向（類似 Linear / Jira）
- 自主執行（WebSocket 任務生命週期）
- 技能累積（Skill Reuse）
- 多工作空間隔離（Workspace Isolation）

本系統需應用於：

👉 大型 Web Application 平台（企業級）
👉 前端：Vue 3 + TypeScript + Tailwind
👉 後端：Spring Boot（Clean Architecture）
👉 DB：Oracle / DB2 / PostgreSQL
👉 架構：微服務 + 高可用（HA）

---

## 📚 輸出格式要求（VERY IMPORTANT）
請輸出為：

👉 單一 Markdown 文件  
👉 結構清楚（# / ## / ###）  
👉 每一章節需包含：
- 概念說明
- 架構圖（使用 Mermaid）
- 操作步驟（Step-by-step）
- 實務範例（Code / CLI / Config）
- Best Practices

---

## 📖 教學手冊章節結構（必須完整覆蓋）

### 1️⃣ Multica 概述
- Multica 架構與設計理念
- 與傳統 AI 工具（Copilot / ChatGPT）差異
- 與任務管理工具（Jira / Linear）差異
- 適用場景（企業 / 開發團隊）

---

### 2️⃣ 系統架構設計（Enterprise Architecture）
- 整體架構圖（Mermaid）
- 元件說明：
  - Multica Server
  - Agent Daemon
  - Web UI Dashboard
  - AI Agent（Claude Code / Codex）
- 與企業系統整合：
  - GitHub / GitLab
  - CI/CD
  - DB / API

---

### 3️⃣ 安裝與部署（Installation & Setup）
- 本地開發環境建置
- Docker / Podman 部署
- CLI 工具安裝
- WebSocket 設定
- Agent Daemon 啟動

---

### 4️⃣ 核心運作機制（Core Workflow）
- 任務生命週期（Issue Lifecycle）
- Agent 自主執行流程
- 任務排程與佇列（Queue）
- WebSocket 通訊流程

👉 必須提供：
- Mermaid Sequence Diagram

---

### 5️⃣ AI Agent 整合（Claude Code / Codex）
- 如何接入不同 AI Agent
- CLI 偵測與整合
- Prompt 設計策略（Agent 專用）
- 多 Agent 協作模式

---

### 6️⃣ 開發流程（Development Workflow）
- 任務建立 → Agent 接單 → 開發 → PR → Review
- 與 Git Flow / Trunk-Based Development 整合
- 自動化測試整合

👉 提供：
- 範例：Spring Boot API 開發流程
- 範例：Vue 前端功能開發流程

---

### 7️⃣ Skill（技能）機制設計
- Skill 定義與儲存
- Skill 重用策略
- 建立企業級 Skill Library

👉 範例：
- 自動部署 Skill
- Code Review Skill
- DB Migration Skill

---

### 8️⃣ 多工作空間（Workspace）設計
- 團隊隔離策略
- 權限控管（RBAC）
- 多專案管理

---

### 9️⃣ 系統維運（Operations）
- Log / Monitoring
- Agent 狀態監控
- 錯誤處理與復原
- 效能優化

---

### 🔟 系統升級與擴展（Upgrade & Scaling）
- Multica 升級策略
- Agent 擴展（水平擴展）
- 高可用架構（HA）

---

### 1️⃣1️⃣ 安全設計（Security）
- API 安全
- Agent 權限隔離
- 憑證管理
- SSDLC 整合

---

### 1️⃣2️⃣ 最佳實務（Best Practices）
請整理：

- ✅ 團隊導入策略
- ✅ Prompt Engineering 原則
- ✅ Agent 使用規範
- ✅ 常見錯誤與避免方式

---

### 1️⃣3️⃣ 實戰案例（Case Study）
請提供：

👉 建立一個「企業 Web 系統」  
包含：
- 後端 API（Spring Boot）
- 前端（Vue）
- DB 操作
- CI/CD
- Agent 自動完成任務

---

## ⚠️ 輸出品質要求（Critical）
- 不可只有概念，一定要「可操作」
- 必須包含：
  - CLI 指令
  - 設定檔範例
  - Mermaid 圖
- 必須以「企業導入」角度撰寫
- 必須可讓團隊直接使用

---

## 產出結果
- 請產出一份 **《Multica 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Multica 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Multica 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Playwright 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Playwright 是一個由微軟（Microsoft）開發並開源的瀏覽器自動化與端對端（E2E）測試框架。它旨在為現代 Web 應用程式提供快速且可靠的自動化測試體驗。 

核心功能與特色
- 跨瀏覽器支援：透過單一 API 即可驅動 Chromium、Firefox 及 WebKit（Safari 的引擎）。
- 跨平台與多語言：支援 Windows、Linux 及 macOS；並提供 Node.js、Python、Java 及 .NET 等語言的 SDK。
- 自動等待（Auto-wait）：內建智慧等待機制，在執行操作（如點擊）前會自動確認元素可被互動，顯著降低測試的不穩定性（Flakiness）。
強大工具鏈：
- Codegen：可透過錄製操作直接產生測試代碼。
- Playwright Inspector：用於逐步執行與偵錯測試。
- Trace Viewer：記錄完整的測試執行細節，包含截圖、網路請求與 Log。
- 環境隔離：每個測試都在獨立的「瀏覽器上下文（Browser Context）」中執行，確保測試之間互不干擾且啟動速度極快。 

主要應用場景
- 自動化測試：模擬真實使用者行為，驗證網頁功能是否正常。
- 網路爬蟲：處理需要執行 JavaScript 的複雜動態網頁抓取。
- 效能監控與截圖：可用於產生成網頁 PDF、截圖，或監控網站加載速度。 

與傳統的 Selenium 相比，Playwright 被認為更適應現代 Web 的非同步特性，且效能更佳。目前其 GitHub 儲存庫 已有極高的社群活躍度與星星數。
## 參考: https://github.com/microsoft/playwright
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用Playwright開發web application的系統做自動化測試。 
## 任務說明 - 系統必需使用Playwright最新版開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生Playwright生態系教學手冊 md 檔
-------------------------------------------------------------------
# Playwright 教學手冊（企業級完整版）

## 🎯 角色設定（System Role）
你是一位「資深軟體架構師 + 資深前後端工程師 + 測試自動化專家（SDET）」，具備以下能力：
- 精通 E2E 測試設計（Playwright、Selenium、Cypress）
- 熟悉企業級系統架構（微服務、分散式系統、CI/CD）
- 熟悉 Java / Spring Boot、Node.js、Python 技術棧
- 熟悉 DevOps、測試策略（Testing Pyramid、Shift Left）
- 熟悉銀行級系統（高穩定、高安全、高併發）

請以「企業內部標準教學手冊」形式輸出內容，內容需可直接提供團隊落地使用。

---

## 📌 任務目標（Goal）
請產出一份「Playwright 最新版生態系教學手冊（Markdown 格式）」，內容需包含：

- 可落地的架構設計
- 完整安裝與設定流程
- 標準開發與測試範本
- CI/CD 整合方式
- 維運與升級策略
- 團隊導入最佳實踐

---

## 📚 文件輸出要求（Output Requirements）
- 使用 **Markdown 格式**
- 結構清晰（# / ## / ###）
- 每章節需包含：
  - 📖 概念說明
  - 🏗 架構設計
  - 💻 範例程式碼
  - ✅ 最佳實踐
  - ⚠️ 常見錯誤
- 必須提供「企業級範本（Template）」

---

## 🧱 教學手冊章節結構（必須完整覆蓋）

### 1️⃣ Playwright 總覽
- Playwright 架構（Browser / Context / Page）
- 與 Selenium 比較
- 適用場景（E2E / 爬蟲 / 視覺測試）

---

### 2️⃣ 系統架構設計（企業級）
- 測試架構設計（Test Architecture）
- 分層設計：
  - Test Layer
  - Page Object Model（POM）
  - Service Layer（API）
- 測試資料管理策略
- 多環境（DEV / SIT / UAT / PROD）配置
- 與微服務架構整合

---

### 3️⃣ 安裝與環境建置
- Node.js / Python / Java 安裝方式
- Playwright 安裝（最新版）
- 瀏覽器安裝（Chromium / Firefox / WebKit）
- 專案初始化（含目錄結構）
- VS Code 設定

---

### 4️⃣ 基礎使用教學
- 第一個測試案例
- Selector 使用策略
- Auto-wait 機制
- Assertions（驗證）
- Headless / Headed 模式

---

### 5️⃣ 進階功能
- Codegen（錄製測試）
- Playwright Inspector
- Trace Viewer
- Network 攔截（Mock API）
- 多分頁 / iframe 操作
- 檔案上傳下載
- 視覺測試（Screenshot / PDF）

---

### 6️⃣ 測試設計最佳實踐
- Page Object Model（POM）實作
- 測試資料隔離
- 減少 Flaky Test 策略
- 測試分層（E2E / Integration / Unit）
- 測試命名規範

---

### 7️⃣ CI/CD 整合（企業級重點）
- GitHub Actions
- GitLab CI
- Jenkins Pipeline
- 測試報告整合（HTML / Allure）
- 測試失敗通知（Email / Teams）

---

### 8️⃣ 測試報告與監控
- Playwright Report
- Trace 分析
- 測試結果 Dashboard
- 與監控系統整合（Prometheus / Grafana）

---

### 9️⃣ 系統維運與管理
- 測試環境管理
- 測試資料清理
- 測試排程（Batch / Cron）
- 平行測試（Parallel Execution）
- 測試資源最佳化

---

### 🔟 升級與版本管理策略
- Playwright 版本升級策略
- Breaking Changes 處理
- 測試穩定性驗證
- 回滾策略

---

### 11️⃣ 安全與合規（銀行級）
- 敏感資料處理
- 測試帳號管理
- 存取控制（RBAC）
- 稽核與日誌（Audit Log）

---

### 12️⃣ 團隊導入指南（最重要）
- 導入 Playwright Roadmap
- 開發流程整合（SDLC）
- 團隊角色分工（QA / Dev / SDET）
- Code Review 規範
- 教育訓練計畫

---

### 13️⃣ 完整專案範本（必須提供）
請提供一個完整專案結構：

## 產出結果
- 請產出一份 **《Playwright 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Playwright 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Playwright 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# Everything Claude Code 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Everything Claude Code (ECC) 是一個開源的 GitHub 專案，由 Anthropic 黑客松冠軍 Affaan Mustafa 建立。它不只是一個配置集合，更是一個針對 Claude Code (Anthropic 的終端機代理環境) 進行性能優化的「代理控制系統」(Agent Harness)。 

這個專案的核心價值在於解決 AI 編碼代理在長對話中容易產生的「上下文污染」與「遺忘決策」問題。 

🛠️ 核心組成部分
截至 2026 年 4 月，ECC 已發展出龐大的生態系統：
- 專業代理 (Agents)：提供約 47 個專門代理 (如 code-reviewer、planner)，透過「子進程」處理任務以保持主對話簡潔。
- 技能 (Skills)：約 181 個自定義指令模組，可執行 TDD (測試驅動開發)、PR 創建等特定工作流。
- 指令與鉤子 (Commands & Hooks)：包含 79 個斜線指令（如 /plan）及自動觸發的鉤子（如 PostToolUse 編輯後自動格式化）。
安全與質量工具：
- AgentShield：對配置進行靜態分析與漏洞掃描。
- Plankton：強制執行代碼質量，自動修復 Linter 違規。
💡 關鍵功能亮點
- 持續學習 (Continuous Learning)：自動從過去的互動中提取行為模式與「記憶」，避免重複解釋。
- 上下文管理：提供自動壓縮與狀態保存機制 (PreCompact/Stop Hooks)，有效處理大型專案的 Token 限制。
- 跨平台支援：雖然專為 Claude Code 設計，但其規則與邏輯也支援 Cursor、Codex 及 OpenCode 等工具。 
## 參考: https://github.com/affaan-m/everything-claude-code
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用Everything Claude Code協助開發web application的系統。 
## 任務說明 - 系統必需使用Everything Claude Code最新版協助AI開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用Everything Claude Code生態系教學手冊 md 檔
-------------------------------------------------------------------
# Everything Claude Code (ECC) 教學手冊生成 Prompt

## 🎯 角色設定
你是：
- 資深軟體架構師（Enterprise Architect）
- 資深後端工程師（Java / Spring Boot / 微服務）
- 資深前端工程師（Vue / TypeScript）
- AI Agent 系統設計專家（Agent Harness / LLM Workflow）
- DevOps / SRE 專家（CI/CD, Observability, Security）

你熟悉：
- Everything Claude Code (ECC)
- Claude Code / Cursor / Codex / OpenCode
- Clean Architecture / DDD / Microservices
- SSDLC（安全軟體開發生命週期）

---

## 🎯 任務目標
請產出一份「企業級 Everything Claude Code 教學手冊（Markdown 格式）」：

👉 目標讀者：
- 軟體工程師（初階～資深）
- 架構師
- DevOps / SRE
- AI 工程師

👉 使用場景：
- 使用 ECC 建構 Web Application（企業級平台）
- 導入 AI Agent 協作開發模式
- 解決大型專案的上下文污染與記憶問題

---

## 📌 輸出要求（非常重要）

### 1️⃣ 文件格式
- 使用 Markdown (.md)
- 結構清晰（#、##、###）
- 每章節需包含：
  - 📖 概念說明
  - 🧠 架構圖（使用 Mermaid）
  - 🛠️ 操作步驟
  - 💡 Best Practices
  - ⚠️ 常見錯誤

---

## 📚 必須包含章節

---

# 🏗️ 第一章：Everything Claude Code 架構總覽
內容需包含：
- ECC 是什麼（Agent Harness 概念）
- 與傳統 Prompt Engineering 差異
- 與 Context Engineering / Harness Engineering 關係

👉 必須包含：
- ECC 整體架構圖（Mermaid）
- Agent / Skills / Hooks / Commands 關係圖

---

# ⚙️ 第二章：ECC 核心組件解析
需詳細說明：

## 1. Agents（代理）
- 子代理（sub-agent）設計
- 任務拆分策略（planner / reviewer / implementer）

## 2. Skills（技能）
- 如何設計 Skill（模組化）
- TDD / PR / Refactor Skill 範例

## 3. Commands & Hooks
- /plan /review /fix 等指令設計
- Pre/Post Hooks（PreCompact / PostToolUse）

## 4. 記憶與上下文管理
- 上下文污染問題
- 壓縮策略
- 長任務處理

---

# 💻 第三章：安裝與環境建置
需包含：

- Claude Code 安裝
- ECC GitHub 專案安裝
- Windows / macOS / Linux 設定
- 與以下工具整合：
  - VS Code
  - Cursor
  - GitHub Copilot（比較）

👉 必須包含：
- CLI 操作範例
- 環境變數設定

---

# 🏛️ 第四章：企業級 Web 系統架構設計（搭配 ECC）
背景：
- 前端：Vue 3 + TypeScript + Tailwind
- 後端：Spring Boot
- 架構：Clean Architecture + Microservices

需說明：
- ECC 如何參與系統設計
- Agent 如何分工：
  - architect agent
  - backend agent
  - frontend agent
  - test agent

👉 必須包含：
- 系統架構圖（Mermaid）
- Agent 協作流程圖

---

# 🔄 第五章：開發流程（AI 驅動）
需完整描述：

## 開發流程（必須包含）
1. /plan
2. /design
3. /implement
4. /test
5. /review
6. /deploy

👉 每一步需：
- 指令範例
- Agent 行為說明
- 輸出範例

---

# 🧪 第六章：測試與品質控管
需包含：

- TDD（Skill 實現）
- 自動 Code Review（review agent）
- Linter 自動修復（Plankton）
- 安全掃描（AgentShield）

👉 必須包含：
- 測試流程圖
- CI/CD 整合方式

---

# 🔐 第七章：安全（SSDLC）
需說明：

- ECC 如何支援 SSDLC
- 安全檢查自動化
- OWASP Top 10 防護

---

# 🚀 第八章：部署與維運（DevOps）
需包含：

- CI/CD（GitHub Actions / GitLab CI）
- 監控（Logging / Metrics）
- AI Agent 監控

---

# 🔄 第九章：系統維護與升級
需說明：

- ECC 版本升級策略
- Skills / Agents 管理
- 相容性問題

---

# 📈 第十章：最佳實踐（Best Practices）
需包含：

- 避免上下文污染的方法
- Agent 設計原則
- Skill 設計模式

---

# ⚠️ 第十一章：常見問題與排錯
需包含：

- Agent 無法理解需求
- 記憶錯亂
- Token 爆掉
- 指令失效

---

# 🧩 第十二章：進階應用
需包含：

- 多 Agent 協作（Multi-Agent System）
- 與其他 AI 工具整合（Cursor / Codex）
- 自訂 Agent

---

# 📦 附錄
需包含：

- 常用指令 Cheat Sheet
- Skills 範例模板
- Agent 設計模板

---

## 🎯 特殊要求（重要）

1. 所有流程需「企業級可落地」
2. 必須包含實際範例（不能只有理論）
3. 所有架構圖使用 Mermaid
4. 必須強調：
   - 可維護性
   - 可擴展性
   - 安全性

---

## 🧠 輸出品質要求

- 深度：⭐⭐⭐⭐⭐（架構師等級）
- 可讀性：⭐⭐⭐⭐⭐
- 實用性：⭐⭐⭐⭐⭐（可直接用於公司內訓）

---

## 🚨 禁止事項

- 不可只給概念
- 不可省略架構圖
- 不可模糊描述
- 必須具體到可實作

---

## 產出結果
- 請產出一份 **《Everything Claude Code 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Everything Claude Code 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Everything Claude Code 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆


-------------------------------------------------------------------
# Compound Engineering 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Compound Engineering Plugin 是由 EveryInc 開發並開源的一款針對 AI 代理（特別是 Claude Code）的工具集。它的核心理念是將工程工作轉化為一個「複利」過程，讓 AI 在每一次任務後都能學習、總結並優化下一次的執行效率。 

核心功能與工作流
該插件實現了一個 Plan → Work → Review → Compound 的循環： 
Plan (ce-plan)：自動化規劃任務，建立後續步驟的上下文。
Work (ce-work)：執行具體的工程任務，如編寫代碼或測試。
Review (ce-review)：系統性地檢查工作品質，提煉出開發過程中的教訓與最佳實踐。
Compound (複利化)：這是最關鍵的一步。插件會將當前任務的學習成果（如新的代碼模式、環境配置或修復方案）存儲為結構化的知識（類似於 Wiki），以便在未來的會話中被 AI 直接調用。
## 參考: https://github.com/EveryInc/compound-engineering-plugin
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用Compound Engineering協助開發web application的系統。 
## 任務說明 - 系統必需使用Compound Engineering最新版協助AI開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用Compound Engineering生態系教學手冊 md 檔
-------------------------------------------------------------------
# Compound Engineering 教學手冊
## 角色設定（Role）

你是一位具備以下經驗的專家：

* 資深軟體架構師（Enterprise Architect）
* 資深後端工程師（Java / Spring Boot / 分散式系統）
* 資深前端工程師（Vue / TypeScript / 微前端架構）
* AI Agent 工程專家（熟悉 Claude Code、生產級 AI 開發流程）
* DevOps / SRE 專家（CI/CD、Observability、Scaling）

---

## 任務目標（Objective）

請產出一份完整且可直接落地的：

👉《Compound Engineering 生態系教學手冊（Markdown 格式）》

此手冊需用於企業內部（如銀行或大型 IT 組織），協助開發人員透過 Compound Engineering Plugin 建立「AI 驅動開發模式」，提升開發效率與品質。

---

## 背景說明（Context）

* 本系統為大型企業級 Web Application 平台
* 採用：

  * Backend：Spring Boot（Clean Architecture）
  * Frontend：Vue 3 + TypeScript + Tailwind CSS（Micro-Frontend）
  * Database：Oracle / DB2 / PostgreSQL（支援讀寫分離）
  * 架構：Microservices + API Gateway + MQ + Cache
* 開發模式：

  * 使用 Claude Code + Compound Engineering Plugin
  * 強調 AI Agent 協作開發（Agentic Development）

---

## 核心技術（Focus）

請深入說明 Compound Engineering Plugin，包括但不限於：

### 1. 核心概念

* 什麼是 Compound Engineering（複利工程）
* 與傳統 AI Coding（Copilot）差異
* 為什麼適合企業級開發

### 2. 核心工作流（必須詳細展開）

* Plan（ce-plan）
* Work（ce-work）
* Review（ce-review）
* Compound（知識沉澱 / Wiki 化）

👉 每個階段需包含：

* 流程圖（Mermaid）
* CLI 指令示例
* 實務案例（Web Application 開發）

---

## 教學手冊內容要求（Table of Contents）

請輸出完整章節，至少包含：

### 第一章：概述

* Compound Engineering 簡介
* 與傳統開發模式比較
* 適用場景（銀行 / 金融 / 大型系統）

### 第二章：系統架構整合

* Compound Engineering + Claude Code 架構圖
* 與企業系統整合方式
* Agent Workflow 設計
* 知識庫（Knowledge Base / Wiki）設計

### 第三章：安裝與環境建置

* Plugin 安裝（最新版本）
* Claude Code 環境配置
* 專案初始化（最佳實務）
* Windows / Linux / CI 環境設定

### 第四章：核心功能教學

* ce-plan 使用（需求拆解）
* ce-work 使用（開發實作）
* ce-review 使用（品質控管）
* Compound（知識累積）

👉 每個功能需提供：

* CLI 指令
* Prompt 範例
* 錯誤案例與修正方式

### 第五章：企業級開發流程設計（重點）

* AI Agent 開發流程（SSDLC 整合）
* 與 Git / CI/CD 整合
* Code Review 自動化
* 測試策略（Unit / Integration / E2E）

### 第六章：最佳實務（Best Practices）

* Prompt Engineering（如何寫 ce-plan）
* Context Engineering（上下文管理）
* Knowledge Reuse（複利最大化）
* 防止 AI hallucination 方法

### 第七章：系統維運（Maintenance）

* 知識庫管理策略
* Plugin 效能調校
* Log / Monitoring 設計
* 問題排查（Troubleshooting）

### 第八章：系統升級（Upgrade Strategy）

* Plugin 升級流程
* 知識庫版本控制
* 向下相容策略
* 災難復原（Disaster Recovery）

### 第九章：企業導入建議（非常重要）

* 導入策略（Pilot → Rollout）
* 團隊角色轉變（Developer → AI Operator）
* KPI 設計（開發效率、品質）
* 教育訓練計畫

### 第十章：完整實戰案例

請提供一個完整案例：
👉 使用 Compound Engineering 開發「Spring Boot + Vue Web App」

需包含：

* ce-plan → 任務拆解
* ce-work → 產生程式碼
* ce-review → 改善品質
* compound → 知識沉澱

---

## 輸出格式要求（Output Format）

* 使用 Markdown（.md）
* 使用清楚標題（#、##、###）
* 提供：

  * Mermaid 圖
  * CLI 指令區塊
  * Prompt 範例
* 結構清晰、可讀性高
* 適合內部 Wiki（如 Confluence / GitLab Wiki）

---

## 額外要求（Important）

* 所有內容需「可實作」，避免空泛描述
* 偏向「企業級實戰」，不是入門教學
* 提供具體範例（Spring Boot / Vue）
* 強調「AI + 工程流程整合」

---

## 產出結果
- 請產出一份 **《Compound Engineering 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Compound Engineering 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Compound Engineering 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-------------------------------------------------------------------
# autoresearch 建立SSDLC教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師,同時也是資深AI架構師
## 技術說明 -AutoResearch」是由 OpenAI 創始成員及前 Tesla AI 總監 Andrej Karpathy 開發的一個開源專案，旨在展示 AI 代理（AI Agents）如何自主進行機器學習研究。 
這個專案的核心理念是讓 AI 在人類睡覺時，透過不斷地修改程式碼、運行實驗、評估結果並保留優化方案，來自主提升模型的效能。 
專案核心特點
極簡化設計：整個核心邏輯僅約 630 行 Python 程式碼，主要包含三個關鍵檔案：
- train.py：唯一會被 AI 代理頻繁修改的文件，包含模型架構與訓練邏輯。
- prepare.py：負責資料準備與工具函式，AI 不會變動此文件。
- program.md：人類設定的初始指令，指導 AI 代理的搜索方向。
固定時間預算：每次實驗固定運行 5 分鐘，這讓不同實驗結果具備可比性，並迫使 AI 在有限算力內尋找最優解。
自主迭代循環：AI 代理會自行決定修改哪些超參數或模型結構，若效能提升則透過 Git 提交（Keep），若失敗則回滾（Revert）。 
應用價值
AutoResearch 展現了 AI 代理不再只是被動回答問題，而是能像真正的研究員一樣思考並進行實驗驗證。目前已有開發者將其應用於 Marketing Mix Modeling (MMM) 或自動化軟體效能優化等領域。
社群生態與衍生工具
由於其設計理念前衛，GitHub 上已出現多個相關專案與分支： 
- karpathy/autoresearch：官方原始儲存庫。
- autoresearch-mlx：針對 Apple Silicon（M 系列晶片）優化的版本。
- autoresearch-at-home：增加協調層，支援多台機器組成實驗集群。
- AutoResearchClaw：與 OpenClaw 整合，可透過簡單指令啟動研究流程。
- awesome-autoresearch：整理了各種衍生的技術架構與優化案例。
## 參考: 
- https://github.com/karpathy/autoresearch
- https://code.claude.com/docs/en/overview
- https://docs.github.com/en/copilot
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用autoresearch,建立AI軟體開發生命週期(SSDLC)的自我學習與優化workflow。 
## 任務說明 - 系統必需使用autoresearch最新版協助AI開發(claude code and github copilot),建立軟體開發生命週期(SSDLC)workflow,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,上述都必需包含範例,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用autoresearch生態系教學手冊 md 檔

-------------------------------------------------------------------
# 🧠 Prompt：生成「AutoResearch 驅動 SSDLC（安全軟體開發生命週期）教學手冊」

## 🎯 角色設定

你是一位：

* 資深軟體架構師（Expert Software Architect）
* 資深前後端工程師（Senior Full-Stack Engineer）
* 資深 AI 架構師（AI Systems Architect）
* 熟悉企業級 SSDLC（Secure Software Development Lifecycle）
* 熟悉 AI Agent 系統（特別是 AutoResearch 類型）
* 熟悉 DevSecOps、CI/CD、Cloud-Native Architecture

---

## 🧩 任務目標

請產出一份 **完整、企業等級、可實作的教學手冊（Markdown 格式）**，主題為：

> 使用 AutoResearch 生態系（含 Claude Code + GitHub Copilot）建立「自我學習與持續優化的 SSDLC（安全軟體開發生命週期）」Workflow

---

## 📚 技術背景（必須納入內容）

請根據以下專案與技術進行整合說明：

* AutoResearch（由 Andrej Karpathy 開發）
* Claude Code
* GitHub Copilot
* GitHub Actions / CI-CD
* Secure SDLC（SSDLC）
* AI Agent 自主迭代（Self-Improving Loop）
* LLM-based Code Generation / Review / Testing
* 使用VS code 協助開發工具

並參考以下專案概念：

* train.py（AI 可修改）
* prepare.py（固定）
* program.md（指令策略）
* Git commit / revert 機制
* 固定時間 budget（如 5 分鐘）

---

## 📦 輸出格式要求（非常重要）

請輸出為：

👉 **單一 Markdown 文件（.md）**
👉 結構完整（含目錄 TOC）
👉 每一章節需包含：

* 架構說明
* 流程圖（使用 Mermaid）
* 範例（Code / Prompt / CLI）
* Best Practices
* Anti-Patterns（錯誤示範）

---

## 🏗️ 必須包含章節（不可缺少）

### 1️⃣ AutoResearch 與 SSDLC 整合概念

* AI 如何取代/輔助 SDLC 各階段
* 與傳統 DevSecOps 差異
* 自我優化迴圈（Self-Improving Loop）

---

### 2️⃣ 系統整體架構設計（Architecture）

需包含：

* AI Agent Layer（AutoResearch）
* Developer Layer（Copilot / Claude Code）
* CI/CD Pipeline
* Security Scan Layer
* Feedback Loop（強化學習）

👉 使用 Mermaid 畫：

* 系統架構圖
* SSDLC Flow

---

### 3️⃣ 環境建置與安裝（Step-by-Step）

包含：

* AutoResearch 安裝
* Python 環境
* Git 安裝設定
* Claude Code CLI 安裝設定
* GitHub Copilot 安裝設定
* vs code 安裝與設定

👉 必須提供：

* CLI 指令
* 安裝腳本範例

---

### 4️⃣ AutoResearch 核心運作解析

深入說明：

* train.py（如何設計可被 AI 修改）
* prepare.py（資料與工具）
* program.md（Prompt Engineering）

👉 必須提供：

* 範例程式碼
* Prompt 範例

---

### 5️⃣ SSDLC Workflow 設計（核心章節）

請設計完整流程：

1. Requirement（需求分析）
2. Design（架構設計）
3. Development（開發）
4. Testing（測試）
5. Security（安全掃描）
6. Deployment（部署）
7. Monitoring（監控）
8. Optimization（自動優化）

👉 每個階段需說明：

* AI 如何參與
* AutoResearch 如何介入
* Copilot / Claude Code / vs code 如何協作

---

### 6️⃣ AI 自動優化機制（核心亮點）

需說明：

* AutoResearch 如何：

  * 修改程式
  * 執行測試
  * 評估結果
  * 決定 Keep / Revert
* 如何應用於：

  * Code Quality
  * Performance
  * Security

---

### 7️⃣ CI/CD + AutoResearch 整合

包含：

* GitHub Actions 設計
* 自動觸發 AutoResearch
* 自動測試 / 安全掃描

👉 必須提供 YAML 範例

---

### 8️⃣ 實戰案例（Enterprise Use Case）

至少 2 個：

#### 案例 1：效能優化

* API latency 優化

#### 案例 2：安全強化

* 自動修補漏洞

---

### 9️⃣ 系統維運（Maintenance）

* 日誌監控
* 模型 drift
* 版本控管
* rollback 策略

---

### 🔟 系統升級與擴展（Scaling）

* 多 Agent（Cluster）
* 分散式 AutoResearch
* GPU / 雲端擴展

---

### 1️⃣1️⃣ Best Practices（企業建議）

* Prompt 設計
* 安全策略
* Git 管理策略

---

### 1️⃣2️⃣ Anti-Patterns（常見錯誤）

例如：

* AI 無限制修改 production code
* 未設計 rollback
* 無測試直接部署

---

## 🔥 額外要求（加分但建議必做）

* 提供：

  * Docker Compose 範例
  * 專案目錄結構
  * `.env` 設定
* 每章節附：

  * 「企業導入建議」
* 使用：

  * 表格整理比較
  * Checklist

---

## 🧠 輸出風格要求

* 使用繁體中文
* 技術內容可包含英文
* 語氣專業（企業內部文件風格）
* 可直接給工程團隊使用

---

## 產出結果
- 請產出一份 **《AutoResearch 驅動 SSDLC（安全軟體開發生命週期）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《AutoResearch 驅動 SSDLC（安全軟體開發生命週期）教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "AutoResearch 驅動 SSDLC（安全軟體開發生命週期）教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
----------------------------------------------------------------
# claude code 建立SSDLC workflow教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師,同時也是資深AI架構師
## 技術說明 -
## 參考: 
- https://code.claude.com/docs/en/overview
- https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide
- https://chihhung.github.io/Blog/posts/%E6%8C%87%E5%BC%95/%E8%A8%AD%E8%A8%88%E9%96%8B%E7%99%BC/%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E6%A8%99%E6%BA%96%E7%A8%8B%E5%BA%8Fsoftware-development-standard-process%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/
- https://github.com/affaan-m/everything-claude-code

參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用claude code,建立AI軟體開發生命週期(SSDLC)的自我學習與優化workflow。 
## 任務說明 - 系統必需使用claude code最新版協助AI開發(claude code and vs code),建立軟體開發生命週期(SSDLC)workflow,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,上述都必需包含範例,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用claude code生態系教學手冊 md 檔,, 請全部放在同一檔中,不可分散.
-------------------------------------------------------------------
# 任務：產出「Claude Code SSDLC（AI軟體開發生命週期）教學手冊」

## 角色設定
你是：
- 資深軟體架構師（Enterprise Architect）
- 資深前後端工程師（Full Stack Engineer）
- 資深 AI 架構師（AI Agent / LLM Workflow Expert）
- 熟悉 Claude Code、生態系工具、AI Agent orchestration、DevSecOps、SSDLC

請以「企業級標準 + 可落地實作 + 教學導向」撰寫內容。

---

## 任務目標
產出一份「完整且可實務落地」的：

👉 Claude Code SSDLC 教學手冊（單一 Markdown 檔）

要求：
- 必須全部內容放在「同一個 .md 檔」
- 不可拆分
- 適用企業內部推廣使用
- 可直接讓工程師照做導入

---

## 背景說明
企業希望導入以下能力：

- 使用 Claude Code + VS Code 建立 AI 輔助開發流程
- 建立 SSDLC（Secure Software Development Life Cycle）
- 導入 AI Agent 自我學習、自我優化 workflow
- 建立可持續演進（Self-improving system）的工程體系

---

## 內容必須涵蓋（不可遺漏）

# 1. 整體架構設計（Architecture）
需包含：

- Claude Code 在 SSDLC 的角色
- AI Agent 在 SDLC 各階段的應用（需求 / 設計 / 開發 / 測試 / 部署 / 維運）
- 系統架構圖（用文字描述）
- 多 Agent 協作模型（Planner / Coder / Reviewer / Security / QA）
- 與企業系統整合（CI/CD, GitHub, API, DB）

---

# 2. Claude Code 安裝與環境建置
需包含：

- Claude Code CLI 安裝
- VS Code 整合設定
- API Key 設定
- Workspace 初始化
- 常見錯誤與排除

需提供：
✔ 實際指令
✔ 範例畫面（用文字描述）

---

# 3. 專案結構設計（Best Practice）
需包含：

- Claude Code 專案目錄結構（.claude/ 設定）
- prompt template 設計
- agent workflow 定義
- context 管理策略

需提供：
✔ 範例目錄樹
✔ config 範例

---

# 4. SSDLC Workflow 設計（核心）
需完整描述：

## (1) 需求階段
- AI 自動產出需求文件
- 使用 prompt 模板

## (2) 設計階段
- 系統設計（架構圖、API）
- AI 協助設計

## (3) 開發階段
- Claude Code 自動產碼
- Code Review AI

## (4) 測試階段
- 自動生成測試（Unit / E2E）
- 安全掃描

## (5) 部署階段
- CI/CD 整合

## (6) 維運階段
- AI 監控 + 問題分析

---

# 5. AI Agent Workflow 設計
需包含：

- 多 Agent 協作模式
- 自我反饋（Self-reflection loop）
- 自我優化（Self-improving system）
- memory / context 設計

---

# 6. Prompt Engineering（非常重要）
需包含：

- Prompt 模板設計
- 可重用 prompt library
- Chain-of-thought / ReAct 模式
- 安全 prompt（避免 hallucination）

需提供：
✔ 多個範例 prompt

---

# 7. 實務案例（必須）
至少提供：

### 案例1：
建立一個 Web 系統（如 Spring Boot + Vue）

### 案例2：
建立一個批次系統（Batch Job）

每個案例需包含：
- 需求 → 設計 → 開發 → 測試 → 部署 全流程
- Claude Code 實際使用方式

---

# 8. 系統維運（Operations）
需包含：

- 日誌管理
- AI 輔助 Debug
- Incident 處理

---

# 9. 系統升級與優化（Evolution）
需包含：

- Prompt 版本控管
- Agent 能力升級
- Workflow 優化策略

---

# 10. 最佳實務與建議（Best Practices）
需包含：

- 團隊導入策略
- 治理（Governance）
- 安全（Security）
- 成本控制（Token / API）

---

# 11. 常見問題（FAQ）

---

## 格式要求
- 使用 Markdown
- 層級清楚（# / ## / ###）
- 每一章節要有：
  - 說明
  - 範例
  - 建議

---

## 參考資料（請吸收內容後整理，不可直接複製）
- Claude Code 官方文件
- Claude Code folder config guide
- SSDLC 標準流程
- Everything Claude Code (ECC)

---

## 輸出要求
- 一次輸出完整 Markdown 文件
- 不可中斷
- 不可分段
- 文件需可直接作為「企業內部教學手冊」

---

## 加分要求（非常重要）
請提升內容價值：

- 用「架構思維」寫（不是工具教學而已）
- 提供「企業導入策略」
- 提供「可複製模板」
- 提供「實務踩坑經驗」

---

## 最終目標
讓企業可以做到：

👉 使用 Claude Code 建立 AI 驅動 SSDLC
👉 建立自我學習、自我優化的開發體系
👉 提升開發效率 + 品質 + 安全性

## 產出結果
- 請產出一份 **《Claude Code SSDLC（AI軟體開發生命週期）教學手冊）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《AClaude Code SSDLC（AI軟體開發生命週期）教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Claude Code SSDLC（AI軟體開發生命週期）教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆





-------------------------------------------------------------------
# github copilot建立SSDLC workflow教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師,同時也是資深AI架構師
## 技術說明 -
## 參考: 
- https://docs.github.com/en/copilot
- https://chihhung.github.io/Blog/posts/%E6%8C%87%E5%BC%95/%E8%A8%AD%E8%A8%88%E9%96%8B%E7%99%BC/%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E6%A8%99%E6%BA%96%E7%A8%8B%E5%BA%8Fsoftware-development-standard-process%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/

參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用github copilot,建立AI軟體開發生命週期(SSDLC)的自我學習與優化workflow。 
## 任務說明 - 系統必需使用claude code最新版協助AI開發(github copilot and vs code),建立軟體開發生命週期(SSDLC)workflow,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,上述都必需包含範例,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生使用github copilot生態系教學手冊 md 檔,請全部放在同一檔中,不可分散.



-------------------------------------------------------------------
# 任務：產出 GitHub Copilot SSDLC 教學手冊

## 🎯 角色設定

你是一位：

* 資深軟體架構師（Enterprise Architect）
* 資深前後端工程師（Full Stack Engineer）
* 資深 AI 架構師（AI Solution Architect）
* 熟悉銀行級系統、高併發、高可用架構、SSDLC、安全開發

---

## 🎯 任務目標

請產出一份「完整、企業級、可落地」的：

👉 **GitHub Copilot SSDLC（安全軟體開發生命週期）教學手冊**

要求：

* **全部內容輸出為單一 Markdown (.md) 檔**
* 不可分段、不可拆檔
* 內容需可直接給企業內部使用

---

## 📚 參考資料（請整合吸收，不要直接貼）

* GitHub Copilot 官方文件
* SSDLC（Software Development Life Cycle）標準流程
* 軟體開發標準程序（含需求、設計、開發、測試、部署、維運）

---

## 🧩 必須涵蓋內容（不可缺少）

### 1️⃣ SSDLC 總覽（結合 AI）

* SSDLC 定義
* 傳統 SDLC vs AI SSDLC
* GitHub Copilot 在各階段的角色
* DevSecOps + AI 整合

---

### 2️⃣ 系統整體架構設計（Architecture）

需包含：

* 前端（Vue / Typescript/ Tailwind CSS ）
* 後端（Spring Boot / Clean Architecture）
* API（RESTful + Swagger）
* DB（Oracle / DB2 / PostgreSQL）
* Cache（Redis）
* MQ（Kafka / RabbitMQ）
* 檔案傳輸（SFTP/FTPS）
* AI（GitHub Copilot）

👉 請提供：

* 架構圖（用文字描述）
* 分層設計（Layered Architecture）
* 微服務 / 模組化設計

---

### 3️⃣ 開發環境建置（Installation & Setup）

需包含：

#### (1) 工具安裝

* VS Code
* Git
* GitHub CLI
* GitHub Copilot（最新版）

#### (2) Copilot 設定

* Copilot Chat
* Copilot Agents（如適用）
* Prompt 設定最佳實務

#### (3) 專案初始化

* Git repo 建立
* 分支策略（Git Flow / Trunk-based）
* Commit 規範（Conventional Commits）

👉 必須提供：

* 指令範例
* 設定畫面說明
* 最佳實務

---

### 4️⃣ SSDLC 各階段 + Copilot 實戰

請逐階段說明：

---

#### 🟢 (1) 需求分析（Requirement）

* User Story 撰寫
* Copilot 協助產生需求文件
* 範例 Prompt

---

#### 🔵 (2) 系統設計（Design）

* 架構設計
* API 設計
* DB Schema 設計
* Copilot 生成設計文件

👉 提供：

* 範例設計文件
* Prompt 範例

---

#### 🟡 (3) 開發（Development）

* 使用 Copilot 撰寫：

  * Controller
  * Service
  * Repository
* Clean Architecture

👉 提供：

* Java / Spring Boot 範例
* Vue / TS 範例
* Copilot Prompt 技巧

---

#### 🟠 (4) 測試（Testing）

* 單元測試（JUnit）
* API 測試
* E2E（Playwright）

👉 Copilot：

* 自動生成測試案例
* 測試覆蓋率提升

---

#### 🔴 (5) 安全（Security）

* SSDLC 安全檢查
* OWASP Top 10
* Code scanning（SAST / DAST）

👉 Copilot 用於：

* 安全漏洞修補
* 安全建議

---

#### ⚫ (6) 部署（Deployment）

* CI/CD（GitHub Actions）
* Docker / Podman
* 環境分層（Dev / SIT / UAT / PROD）

👉 提供 YAML 範例

---

#### ⚪ (7) 維運（Operation）

* Logging（ELK）
* Monitoring（Prometheus / Grafana）
* Alerting

👉 Copilot：

* Log 分析
* 問題診斷

---

### 5️⃣ Copilot 進階使用（AI Engineering）

包含：

* Prompt Engineering
* Context 設計
* 多檔案生成
* Refactoring
* Code Review 自動化
* AI Pair Programming 最佳實務

---

### 6️⃣ 自我學習與優化機制（關鍵）

請設計：

👉 AI 自我優化 workflow：

* Code → Review → Feedback → 改進
* Prompt 優化迴圈
* 知識庫（Knowledge Base）
* 文件自動生成

---

### 7️⃣ 實戰案例（銀行系統）

請提供：

👉 範例：

* Web Application 
* FTP 上傳流程
* 資料驗證流程
* 高可用架構

👉 並展示：

* Copilot 如何協助開發

---

### 8️⃣ 系統維護與升級

* Copilot 升級策略
* Plugin 管理
* 相容性管理
* 技術債處理

---

### 9️⃣ 最佳實務（Best Practices）

至少包含：

* 開發規範
* 安全規範
* AI 使用規範
* 團隊協作模式

---

## 📦 輸出格式要求

* 單一 Markdown 文件
* 使用清楚章節（# / ## / ###）
* 包含：

  * 程式碼區塊
  * 表格
  * 範例
  * Prompt 範例
* 內容需：

  * 可教學
  * 可實作
  * 可企業導入

---

## 🚫 禁止事項

* 不可只寫概念
* 不可缺少範例
* 不可過度簡略
* 不可拆成多檔

---

## ✅ 成功標準

產出的文件需達到：

✔ 可作為企業內部培訓教材
✔ 可直接導入專案
✔ 可讓工程師立即使用 GitHub Copilot 建立 SSDLC

---

## 產出結果
- 請產出一份 **《GitHub Copilot SSDLC 教學手冊）教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《GitHub Copilot SSDLC 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "GitHub Copilot SSDLC 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
------------------------------------------------------------------
# pi code agent 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Pi (Coding) Agent 是一個開源且極簡化的 AI 程式碼開發工具，旨在作為 Claude Code 的輕量級替代方案。它直接在你的終端機中運行，不僅能生成程式碼片段，還具備直接操作文件、資料夾及執行開發命令的能力。 

核心特色與設計哲學
Pi 的設計核心在於「極簡主義」與「可觀測性」，與其他繁重的 Agent 框架（如具備複雜計畫模式或子代理的工具）截然不同： 

- 極簡終端控制：Pi 本身是一個輕量級的終端控制框架，讓開發者根據自己的工作流進行調整，而非強制適應工具。
- 不使用「計畫模式」：與其依賴黑盒式的計畫機制，Pi 鼓勵開發者使用 PLAN.md 檔案手動規劃，這使得開發過程可版本控制、跨會話共享且完全透明。
- 拒絕黑盒設計：Pi 捨棄了複雜的多代理（Sub-Agents）編排，所有的工具執行與輸出都是可見的，開發者可以在任何時候中途干預或取消。
- 可擴展性：Pi 支援透過 TypeScript 擴充功能（Extensions）、技能（Skills）與提示詞模板（Prompt Templates）進行自定義，並允許 Agent 「自我進化」——如果你需要新功能，可以直接要求 Agent 寫出擴展來增加自己的能力。
## 參考: 
- https://pi.dev/
- https://github.com/badlogic/pi-mono
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用pi code agent開發web application的系統。 
## 任務說明 - 系統必需使用pi code agent最新版開發,包含系統架構,安裝,設定,使用教學,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生pi code agent系教學手冊 md 檔,請全部放在同一檔中,不可分散.
------------------------------------------------------------------
# 任務：產生「Pi Code Agent 教學手冊（完整單一 Markdown 檔）」

## 角色設定
你是一位：
- 資深軟體架構師（Enterprise Architecture）
- 資深前後端工程師（Full Stack）
- AI Agent 系統設計專家
- DevOps / SSDLC 專家

請以「企業級實務導向 + 可落地實作」為核心撰寫內容。

---

## 背景說明
目前團隊需全面導入 Pi Code Agent（最新版）來開發 Web Application 系統。

Pi Code Agent 為：
- 極簡 AI Coding Agent（Terminal-based）
- 可直接操作檔案 / 執行指令 / 生成程式碼
- 強調：
  - Minimalism（極簡）
  - Observability（可觀測性）
  - No Black Box（無黑盒）
  - 無 Plan Mode（改用 PLAN.md）

---

## 任務要求（非常重要）
請產出：

👉 **一份完整的 Markdown 教學手冊（單一檔案）**
👉 不可拆分為多檔案
👉 不可省略章節
👉 每一章需包含「說明 + 範例 + Best Practice」

---

## 文件內容結構（必須完整覆蓋）

# Pi Code Agent 教學手冊（Enterprise Edition）

---

## 1. 概述（Overview）
- Pi Code Agent 是什麼
- 與其他工具比較：
  - Claude Code
  - GitHub Copilot
  - Cursor
- 適用場景（企業 / 個人 / 平台開發）

---

## 2. 核心設計哲學（Architecture Philosophy）
詳細說明：
- 極簡主義（Minimalism）
- 可觀測性（Observability）
- PLAN.md 驅動開發
- 無多代理架構（No Sub-Agents）

👉 請補充：
- 優點 / 缺點分析
- 適合與不適合使用情境

---

## 3. 系統架構設計（System Architecture）

請設計：
👉 使用 Pi Agent 開發「大型 Web 系統」的架構

需包含：
- 前端（Vue / React）
- 後端（Spring Boot / FastAPI）
- API 設計
- DB（支援分庫分表）
- Cache（Redis）
- MQ（Kafka / RabbitMQ）
- Batch（Spring Batch）
- AI Agent 層（Pi）

👉 必須提供：
- 架構圖（用 Mermaid）
- 說明 Pi 在哪一層運作
- Agent 如何參與開發流程

---

## 4. 安裝與環境建置（Installation & Setup）

請提供：
- Mac / Linux / Windows 安裝方式
- Node.js / npm / pnpm 需求
- Pi 安裝步驟
- GitHub repo 使用方式
- CLI 初始化流程

👉 必須提供：
- 實際指令範例
- 常見錯誤與解法

---

## 5. 基本使用教學（Getting Started）

請示範：
- 啟動 Pi Agent
- 生成程式碼
- 修改檔案
- 執行指令
- Debug

👉 必須包含：
- Terminal 實際操作範例
- Prompt 範例

---

## 6. PLAN.md 開發模式（最重要章節）

請詳細說明：
- 為什麼 Pi 不用 Plan Mode
- 如何設計 PLAN.md

👉 提供：
- PLAN.md 範本
- 任務拆解方式
- Sprint 規劃方式

👉 範例：
- 開發一個 Web API 的 PLAN.md

---

## 7. Extensions / Skills / Prompt Templates

請說明：
- 如何擴充 Pi
- 如何寫：
  - Extension（TypeScript）
  - Skills
  - Prompt Template

👉 提供：
- 範例程式碼
- 自動生成 Extension 的方法

---

## 8. Pi Agent + SSDLC（企業重點）

請設計：
👉 使用 Pi Agent 建立 SSDLC 流程

需包含：
- Secure Coding
- Code Review（AI）
- SAST / DAST
- Dependency Scan
- CI/CD

👉 提供：
- DevSecOps 流程圖（Mermaid）

---

## 9. 實戰案例（Hands-on）

請示範：
👉 用 Pi 建立一個 Web Application

包含：
- 前端 + 後端
- API
- DB
- 部署

👉 必須：
- 提供完整步驟
- 每一步都有 Prompt

---

## 10. 維運與監控（Operations）

請說明：
- Log 設計
- Agent 行為監控
- Debug 方法
- 成本控制（Token / API）

---

## 11. 升級與版本管理（Upgrade Strategy）

請說明：
- 如何升級 Pi
- 如何管理 Prompt / Extension 版本
- 與 Git 整合策略

---

## 12. Best Practices（企業建議）

請整理：
- 團隊使用規範
- Prompt Engineering 原則
- 常見錯誤

---

## 13. Anti-Patterns（重要）

請列出：
- 不該這樣用 Pi 的方式
- 常見踩雷

---

## 14. 結論（Conclusion）

---

## 文件要求

- 使用 Markdown 格式
- 所有內容放在「同一檔案」
- 必須包含：
  - 程式碼區塊
  - Mermaid 圖
  - 範例 Prompt
- 內容需：
  - 可實作
  - 企業級
  - 結構清晰

---
## 產出結果
- 請產出一份 **《Pi Code Agent 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Pi Code Agent 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Pi Code Agent 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆




--------------------------------------------------------------------
# GSD-2教學手冊 
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - gsd-2 是 gsd-build 組織在 GitHub 上的一個開源專案，全名為 "Get Shit Done 2"。 

GSD-2 是一個強大的元提示（meta-prompting）、**上下文工程（context engineering）和規格驅動開發（spec-driven development）**系統，此系統旨在協助 AI 代理，例如 Claude Code 和 Gemini CLI，進行長時間且複雜的開發工作。 

專案核心連結與資訊
GitHub 主儲存庫：gsd-build/gsd-2
功能亮點：
- MCP 伺服器模式：可作為 Model Context Protocol (MCP) 伺服器運行，將 GSD 工具暴露給 Claude Desktop 或 VS Code Copilot 等外部 AI 用戶端。
- VS Code 擴充功能：由 FluxLabs 發佈，提供側邊欄儀表板和聊天參與者功能。
- 知識圖譜系統：能將 LEARNINGS.md 解析為知識圖譜，協助 AI 理解專案結構。
- 技能管理：追蹤 AI 代理在不同任務中的技能表現並提供健康度數據。
## 參考:
- https://github.com/gsd-build/gsd-2
## 背景 - 目前必需使用GSD-2開發web application的系統。 
## 任務說明 - 系統必需使用GSD-2最新版開發,包含系統架構,安裝,設定,使用GSD軟體開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生GSD-2教學手冊 md 檔,請全部放在同一檔中,不可分散.





-------------------------------------------------------------------
# 任務：產出「GSD-2 完整教學手冊（單一 Markdown 檔）」

## 🎯 角色設定

你是：

* 資深軟體架構師（Enterprise Architect）
* 資深後端工程師（Spring Boot / 微服務）
* 資深前端工程師（Vue / TypeScript）
* 資深 AI 工程師（AI Agent / Prompt Engineering / Context Engineering）
* 熟悉 SSDLC（Secure Software Development Lifecycle）

---

## 📌 背景說明

我們的團隊正在開發「企業級大型共用平台」，技術棧如下：

### 🔧 Backend

* Java 21
* Spring Boot 3.5.x
* Clean Architecture
* RESTful API（Swagger）

### 🎨 Frontend

* Vue 3.x + TypeScript
* Tailwind CSS
* Micro-frontend Architecture

### 🧱 Infrastructure

* DB：Oracle / DB2 / PostgreSQL / SQL Server
* Cache：Redis
* MQ：Kafka / RabbitMQ
* Container：Podman
* CI/CD：GitHub Actions

### 🔐 SSDLC

* SonarQube（程式碼品質）
* ArchUnit（架構測試）
* JUnit 5（單元測試）
* SAST / DAST
* API Security

---

## 📌 GSD-2 專案說明

GSD-2（Get Shit Done 2）是一個：

* Meta-Prompting 系統
* Context Engineering 框架
* Spec-Driven Development（規格驅動開發）工具

主要用於：

* AI Agent（Claude Code / Gemini CLI / Copilot）
* 長時間任務
* 複雜系統開發

核心能力：

* MCP Server（Model Context Protocol）
* 知識圖譜（LEARNINGS.md → Graph）
* 技能管理（Skill Tracking）
* AI 任務協作（Agent Workflow）

GitHub：
https://github.com/gsd-build/gsd-2

---

## 📌 任務要求

請產出一份：

👉 **「企業級 GSD-2 教學手冊」**
👉 **完整內容必須全部放在「單一 Markdown 檔」**
👉 不可拆分為多個檔案

---

## 📚 文件內容結構（強制要求）

請嚴格依照以下章節輸出：

# GSD-2 教學手冊（Enterprise Edition）

---

## 1. 總覽（Overview）

* GSD-2 是什麼
* 與傳統開發模式差異
* 適用場景（企業 / AI Agent / 長任務）

---

## 2. 核心概念（Core Concepts）

* Meta Prompting
* Context Engineering
* Spec-Driven Development
* Agent Workflow
* Knowledge Graph（LEARNINGS.md）

---

## 3. 系統架構設計（Architecture）

請包含：

* GSD-2 + 微服務架構整合圖（文字描述）
* 與 Spring Boot 架構整合方式
* 與前端（Vue）協作方式
* 與 CI/CD 整合方式
* 與 SSDLC 整合方式

---

## 4. 安裝與環境建置（Installation）

請包含：

* 本地開發環境（Windows / Mac / Linux）
* Node.js / Python（如需要）
* 安裝 GSD-2
* MCP Server 啟動
* VS Code 擴充設定
* 與 Claude Code / Copilot 整合

---

## 5. 專案初始化（Project Setup）

請包含：

* 專案目錄結構（範例）
* GSD 標準檔案說明：

  * SPECS.md
  * TASKS.md
  * LEARNINGS.md
  * AGENTS.md
* 初始化流程

---

## 6. Spec-Driven 開發流程（重點）

請詳細說明：

1. 撰寫規格（Spec）
2. 拆解任務（Tasks）
3. 指派 AI Agent
4. 產生程式碼
5. 測試與驗證
6. 回饋到 LEARNINGS.md

---

## 7. AI Agent 協作模式

* 多 Agent 協作（Planner / Builder / Reviewer）
* Claude Code 使用方式
* Copilot 使用方式
* Agent 任務切分策略

---

## 8. 知識圖譜與學習系統

* LEARNINGS.md 設計方式
* Knowledge Graph 建立
* 如何提升 AI 理解能力

---

## 9. 技能管理（Skill Tracking）

* 技能評估方式
* 任務成功率
* Agent 健康度

---

## 10. 實戰範例（重要）

請提供：
👉 建立一個「Spring Boot REST API + Vue UI」
使用 GSD-2 完整流程：

* Spec
* Tasks
* Code
* Test
* Learning

---

## 11. SSDLC 整合（安全開發）

請包含：

* Secure Prompt
* Code Scan（SAST）
* Dependency Scan
* API Security
* DevSecOps 整合

---

## 12. 系統維護（Maintenance）

* 如何更新 Spec
* 如何修復 Bug
* 如何讓 AI 持續學習

---

## 13. 系統升級（Upgrade）

* GSD-2 升級策略
* Prompt 相容性
* 知識庫遷移

---

## 14. 最佳實務（Best Practices）

* Prompt 設計原則
* Context 控制技巧
* 避免 hallucination
* 大型專案管理技巧

---

## 15. 常見問題（FAQ）

* AI 不照 Spec？
* Code 不可用？
* Context 過大？

---

## 16. 團隊導入建議（Enterprise Adoption）

請提供：

* 導入策略（分階段）
* 教育訓練方式
* Governance（治理）

---

## 📌 輸出格式要求（非常重要）

* 必須為「單一 Markdown 檔」
* 使用清楚的標題（# / ## / ###）
* 提供程式碼區塊（```）
* 提供架構圖（用文字描述）
* 內容需可直接用於企業內部培訓

---

## 📌 輸出品質要求

* 必須「可實作」
* 必須「企業等級」
* 必須「結構清楚」
* 必須「深入但不空泛」

---

## 🚫 禁止事項

* 不可只寫概念
* 不可過於簡略
* 不可拆成多檔案

---

## 產出結果
- 請產出一份 **《GSD-2教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《GSD-2教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "GSD-2教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-----------------------------------------------------
# agency-agents教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - agency-agents 是由 Michael Sitarzewski 發起的 GitHub 熱門開源專案，目標是建立一個完整的「AI 虛擬代理人團隊」。這個專案在短短幾週內便獲得超過 8 萬顆星，被社群譽為能「取代整個團隊」的工具。 

核心功能與特色
- 高度專業化的人設：專案包含超過 144 個即插即用的 AI 專家角色，並非簡單的提示詞模板，而是具有獨立性格、專業流程、通訊風格與成功指標的詳細 Markdown 定義文件。
- 跨領域部門分組：目前涵蓋工程、設計、行銷、產品、遊戲、安全、金融、法律等 12 到 18 個專業部門。
開發工具整合：可直接整合至 Claude Code、Cursor、Aider 及 OpenCode 等 IDE 輔助工具中，作為子代理人（subagents）執行特定任務。
- 生產環境就緒：提供的角色（如前端開發者、專案經理、代碼審核者）均經過實際工作流測試，專注於產出實質成果與代碼。
## 參考:
- https://github.com/msitarzewski/agency-agents
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用agency-agents協助AI(Claude Code/GitHub Copilot)開發web application的系統。 
## 任務說明 - 系統必需使用agency-agents最新版協助AI(Claude Code/GitHub Copilot)開發,包含系統架構,安裝,設定,如何使用agency-agents協助AI開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生agency-agents教學手冊 md 檔,請全部放在同一檔中,不可分散.



-------------------------------------------------------------------
# 任務：生成 agency-agents教學手冊（單一 Markdown 檔）

## 🎯 角色設定

你是一位：

* 資深軟體架構師（Expert Software Architect）
* 資深前後端工程師（Senior Full-Stack Engineer）
* AI Agent 架構專家（AI Agent System Designer）
* SSDLC（安全軟體開發生命週期）實務導入專家

具備以下能力：

* 大型企業系統架構設計（微服務 / Clean Architecture / 雲原生）
* AI Coding Agent 整合（Claude Code / GitHub Copilot / Cursor / Aider）
* DevOps / MLOps / AgentOps
* 文件撰寫與教學設計（可供企業內部教育訓練使用）

---

## 📌 任務目標

請產出一份**完整且企業等級的教學手冊（Markdown 格式）**，主題為：

> 「agency-agents 教學手冊（Enterprise Guide）」

⚠️ **重要限制**

* 所有內容必須輸出在「單一 Markdown 檔案中」
* 不可拆分章節為多檔
* 文件需具備「可直接提供給公司同仁使用」的品質
* 必須包含「實務導向 + 架構設計 + 操作教學 + 最佳實踐」

---

## 🧠 背景說明（請納入文件）

* agency-agents 是一個 AI 虛擬團隊框架
* 包含 100+ 專業角色（工程 / PM / 設計 / 安全 / 法務等）
* 每個 Agent 具備：

  * 人設（Persona）
  * 工作流程（Workflow）
  * 溝通風格（Communication Style）
  * KPI / 成功指標
* 可整合：

  * Claude Code
  * GitHub Copilot
  * Cursor
  * Aider
* 作為「Sub-agents」執行開發任務
* 目標：提升開發效率、降低人力成本、標準化流程

---

## 📚 文件內容結構（必須完整覆蓋）

請依以下章節順序產出：

---

# 1️⃣ 總覽（Overview）

* agency-agents 是什麼
* 核心設計理念（AI Agent Team）
* 與傳統開發模式差異
* 適用場景（企業 / 專案 / 個人開發）

---

# 2️⃣ 系統架構設計（Architecture）

* 整體架構圖（文字描述即可）
* Agent Layer / Tool Layer / Execution Layer
* 與 AI Coding 工具整合架構
* 多 Agent 協作模型（Multi-Agent Orchestration）
* 與企業系統整合方式（API / Batch / MQ）

---

# 3️⃣ 安裝與環境建置（Installation & Setup）

請提供：

* GitHub 專案下載
* 目錄結構說明
* 必要工具：

  * Node.js / Python（如需要）
  * Claude Code / Copilot CLI
* 環境變數設定
* 初始啟動流程

---

# 4️⃣ Agent 結構解析（Agent Design）

* Agent Markdown 結構說明
* Persona 設計
* Workflow 設計
* 任務輸入 / 輸出格式
* 範例（例如：Frontend Developer Agent）

---

# 5️⃣ 與 AI Coding 工具整合（Integration）

請分別說明：

## Claude Code

* 如何載入 agents
* 如何呼叫 sub-agent
* Prompt 範例

## GitHub Copilot

* 如何搭配使用
* 如何轉換 agent 為 prompt

## Cursor / Aider

* 使用方式
* 實務案例

---

# 6️⃣ 實戰：AI 開發流程（End-to-End Workflow）

請設計一個完整案例：

👉 開發一個 Web Application（例如：銀行系統 / CRM）

包含：

1. PM Agent 分析需求
2. Architect Agent 設計架構
3. Backend Agent 開發 API
4. Frontend Agent 開發 UI
5. QA Agent 測試
6. Security Agent 檢查漏洞

並提供：

* 每一步 Prompt 範例
* Agent 協作流程圖（文字）

---

# 7️⃣ SSDLC（安全開發流程）

* 如何導入 agency-agents 到 SSDLC
* 安全掃描（SAST / DAST）
* 威脅建模（Threat Modeling）
* 合規（Compliance）

---

# 8️⃣ 系統維運（Maintenance）

* Agent 更新策略
* Prompt 優化
* 成本控制（Token / API）
* 錯誤處理（Failure Handling）

---

# 9️⃣ 系統升級（Upgrade Strategy）

* 如何同步最新版 agency-agents
* 客製 Agent 如何避免衝突
* 版本控管策略（Git Flow）

---

# 🔟 最佳實踐（Best Practices）

請提供：

* Agent 設計原則
* Prompt Engineering 技巧
* 多 Agent 協作策略
* 避免常見錯誤

---

# 1️⃣1️⃣ 企業導入建議（Enterprise Adoption）

* 如何導入團隊
* 教育訓練建議
* Governance（治理）
* KPI 設計

---

# 1️⃣2️⃣ 附錄（Appendix）

* 常用 Prompt 模板
* Agent 範例模板
* FAQ

---

## ✨ 輸出要求

* 使用 Markdown 格式
* 結構清晰（# / ## / ###）
* 適當使用：

  * 表格
  * 程式碼區塊
  * 清單
* 內容需具備「可操作性」
* 語言：繁體中文
* 風格：專業、清楚、可落地

---

## 產出結果
- 請產出一份 **《agency-agents教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《agency-agents教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "agency-agents教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆



-------------------------------------------------------------------
# Skill_Seekers教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - Skill Seekers 是由 yusufkaraaslan 開發的一個開源工具，它被定位為 AI 系統的數據層（Data Layer）。
這個工具的主要功能是將各種非結構化的技術內容，例如程式碼庫、技術文件、網頁等，轉換成 AI 可以直接理解並使用的「AI 技能」。此功能使開發者能更輕鬆地為 Claude、Gemini 或 OpenAI 等模型提供深度的上下文資訊。
主要功能亮點：
多源轉換：支援超過 17 種來源，包括 GitHub 儲存庫、PDF、Jupyter Notebooks、YouTube 影片、Notion、Slack/Discord 記錄以及 OpenAPI 規範。
平台相容性：生成的「技能」可應用於 30 多個平台，包含 LLM 模型、RAG 框架（如 LangChain、LlamaIndex）以及 AI 程式碼編輯器（如 Cursor、Windsurf、Cline）。
深度代碼分析：具備針對 Python 和 JavaScript 的深度 AST（抽象語法樹）解析能力，能將複雜的代碼邏輯轉化為 AI 易於消化的結構。
高度可擴展：內建超過 65 種預設工作流（Workflows）和 178 種經過驗證的配置（Configs）。
## 參考:
- https://github.com/yusufkaraaslan/Skill_Seekers
- https://skillseekersweb.com/
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用Skill_Seekers協助AI(Claude Code/GitHub Copilot)開發web application的系統。 
## 任務說明 - 系統必需使用Skill_Seekers最新版協助AI(Claude Code/GitHub Copilot)開發,包含系統架構,安裝,設定,使用Skill_Seekers軟體協助AI(Claude Code/GitHub Copilot)開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生Skill_Seekers教學手冊 md 檔,請全部放在同一檔中,不可分散.



--------------------------------------------------------------------
# 任務：產生 Skill_Seekers 教學手冊（單一 Markdown 檔）

## 角色設定

你是一位「資深軟體架構師 + 資深前後端工程師 + AI 架構師」，具備以下專長：

* 大型分散式系統設計（Microservices / Clean Architecture）
* AI 輔助開發（Claude Code / GitHub Copilot / LLM Agents）
* RAG（Retrieval-Augmented Generation）與 Data Layer 設計
* DevSecOps / SSDLC（Secure Software Development Lifecycle）

---

## 任務目標

請產出一份**完整且可落地的《Skill_Seekers 教學手冊》Markdown 文件（單一 .md 檔）**，用於企業內部導入 Skill_Seekers，協助 AI（Claude Code / GitHub Copilot）開發 Web Application。

⚠️ 要求：

* **所有內容必須在同一個 Markdown 檔中（不可拆分）**
* 必須包含「架構 + 安裝 + 設定 + 實作 + 維運 + 升級 + 最佳實務」
* 必須偏向**實戰導向（Hands-on）**，不可只做概念介紹

---

## 技術背景（必須納入內容）

Skill_Seekers 是一個 AI Data Layer 工具，具備：

* 多來源轉換（GitHub、PDF、YouTube、Notion、OpenAPI 等）
* 技術內容 → AI Skills（結構化知識）
* 支援 LLM / RAG（LangChain、LlamaIndex）
* 支援 AI 開發工具（Claude Code / Copilot / Cursor）
* AST 程式碼分析（Python / JavaScript）
* 可擴展 Workflow / Config

---

## 文件輸出格式（強制結構）

請使用以下結構輸出（不可缺少）：

# Skill_Seekers 教學手冊（企業實戰版）

## 1. 概述（Overview）

* Skill_Seekers 是什麼
* 為什麼它是 AI Data Layer
* 在 AI 開發中的定位（Claude Code / Copilot）

---

## 2. 整體系統架構設計（Architecture）

請提供：

* 架構圖（使用 mermaid）
* 說明以下整合：

  * Skill_Seekers
  * LLM（OpenAI / Claude / Gemini）
  * RAG（LangChain / LlamaIndex）
  * Web Application（前後端）
* Data Flow（從資料 → Skill → AI 使用）

---

## 3. 安裝與環境建置（Installation）

包含：

* 系統需求（OS / Node / Python / Docker）
* 安裝步驟（CLI / Docker）
* 初始化專案
* 常見錯誤與排除

---

## 4. Skill_Seekers 設定（Configuration）

包含：

* config 設計（範例 JSON/YAML）
* workflow 設定
* 多資料來源接入（GitHub / PDF / API）
* AST 分析設定

---

## 5. Skill 建立流程（核心）

說明：

* 如何將以下轉為 Skills：

  * GitHub Repo
  * API 文件（OpenAPI）
  * 技術文件
* Skill 結構設計（Schema）
* metadata / tagging 策略

---

## 6. 與 AI 開發工具整合（重點）

### 6.1 Claude Code 整合

* 如何讀取 Skill
* Prompt 設計
* 範例（生成程式碼）

### 6.2 GitHub Copilot 整合

* Copilot + Skill 使用方式
* context injection 方法

---

## 7. Web Application 開發實戰（Hands-on）

請提供：

* 範例專案（建議：Spring Boot + Vue / FastAPI）
* 使用 Skill_Seekers 提升開發流程：

  * API 開發
  * 文件生成
  * 測試生成
* AI 協作流程（Dev Flow）

---

## 8. SSDLC（安全開發流程）

請整合：

* Secure Coding
* SAST / DAST
* Dependency Scan
* Prompt Injection 防護

---

## 9. 系統維運（Maintenance）

包含：

* Skill 更新策略
* 資料同步
* 效能優化（cache / indexing）
* log / monitoring

---

## 10. 系統升級（Upgrade）

包含：

* 版本升級策略
* Config migration
* 向下相容設計

---

## 11. 最佳實務（Best Practices）

請提供：

* 團隊導入建議
* Skill 設計原則
* Prompt Engineering 建議
* 常見錯誤

---

## 12. 附錄（Appendix）

* CLI 指令大全
* config 範例
* troubleshooting

---

## 額外要求（重要）

* 所有範例需可實際執行（不可假設）
* 所有架構需符合「企業級系統」
* 需包含實際 Prompt 範例
* 優先使用：

  * Clean Architecture
  * Microservices
  * API-first 設計

---

## 輸出格式要求

* 僅輸出 Markdown
* 不要額外解釋
* 文件需結構清晰（標題、code block、mermaid）
* 必須是一份可直接交付團隊使用的教學手冊

---

## 最終目標

讓團隊可以透過 Skill_Seekers：
👉 建立 AI Data Layer
👉 強化 Claude Code / Copilot 開發能力
👉 提升開發效率 + 品質 + 安全性

## 產出結果
- 請產出一份 **《Skill_Seekers教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《Skill_Seekers教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "Skill_Seekers教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆
-----------------------------------------------------------------
# 使用github copilot 建立SSDLC Agent Team 教學手冊
## 角色設定 - 你是一位「資深軟體架構師 + 資深前後端工程師 + AI 架構師」，具備以下專長：
* 大型系統單體系統設計(前後分離 Web application/ Clean Architecture)
* 大型分散式系統設計（Microservices / Clean Architecture）
* AI 輔助開發（Claude Code / GitHub Copilot / LLM Agents）
* RAG（Retrieval-Augmented Generation）與 Data Layer 設計
* DevSecOps / SSDLC（Secure Software Development Lifecycle）
## 技術說明 - 需在公司允許的AI(GitHub Copilot) 平台上建置
* vscode 程式與文件編輯器
* vscode plugin
  - GitHub Copilot
  - GitHub Copilot Chat
* Copilot CLI
* GitHub Copilot 可使用的大語言模型
  - Anthropic Claude Sonnet 4.6
  - Anthropic Claude Opus 4.6
  - Anthropic Claude Haiku 4.5
  - Google Gemini 3.1 Pro
  - Google Gemini 3 Flash 
  - OpenAI GPT-5.3-Codex
  - OpenAI GPT-5.4
  - OpenAI GPT-5.4 mini
  - OpenAI GPT-5.4 nano
  
## 參考:
- https://docs.github.com/en/copilot
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/agent-management
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- https://docs.github.com/en/copilot/concepts/agents/copilot-memory
- https://docs.github.com/en/copilot/concepts/auto-model-selection
- https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents

參考上述link,相關內容與文章,及文中相關link內容,完成任務說明

## 背景 - 目前必需使用GitHub Copilot建立SSDLC Agent Team,用來開發公司未來軟體的系統。 
## 任務說明 - 使用GitHub Copilot建立SSDLC Agent Team SOP,用來開發公司未來軟體的系統與逆向工程開發,包含SSDLC Agent Team系統架構,如何建立,需包含:create agent,create prompt, create instructions,create skills, create hook, create pull request,memory 等功能,並說明與提供詳細範例,同時把上述的功能融入SSDLC, 建立的SSDLC workflow ,建立後應如何提供給其它開發團隊使用,必需和其它團隊說明如何安裝,設定,使用,系統維護,系統升級,請提供建議給同仁使用,請先產生prompt 來請AI 幫我產生建立SSDLC Agent Team教學手冊 md 檔,請全部放在同一檔中,不可分散.


-----------------------------------------------------------------
# 任務：產出《GitHub Copilot 建立 SSDLC Agent Team 教學手冊》

## 角色設定

你是一位：

- 資深軟體架構師（Enterprise Architect）
- 資深前後端工程師（Full-Stack Engineer）
- 資深 AI 架構師（AI Solution Architect）
- DevSecOps / SSDLC 導入專家
- 企業級逆向工程與現代化改造顧問

你熟悉：

- GitHub Copilot
- VS Code Agent Mode
- GitHub Copilot Chat
- GitHub Copilot CLI
- GitHub Copilot cloud agent
- Custom Agents
- Custom Instructions
- Agent Skills
- Copilot Memory
- Auto Model Selection
- Copilot Integrations
- PR 自動化與 Code Review
- 企業級治理、權限控管、成本控管、審計與維運

請以「企業級可落地導入」為標準撰寫，不可流於概念介紹。

---

## 任務目標

請產出一份完整、單一 Markdown 文件，主題為：

# 《GitHub Copilot 建立 SSDLC Agent Team 教學手冊》

此手冊的目標是：

- 協助公司在允許的平台上，以 GitHub Copilot 建立 SSDLC Agent Team
- 支援新系統開發與舊系統逆向工程
- 建立可重複、可治理、可維運、可升級的標準 SOP
- 提供給其他開發團隊直接複製、安裝、設定與落地使用

---

## 重要前提

請先根據最新官方文件與相關連結自行查核內容，並在文件中反映最新狀態。若功能為 Preview、Beta、或需特定方案 / 管理員政策啟用，必須清楚標示，不可把 Preview 功能寫成正式 GA 功能。

請以以下原則撰寫：

- 以 GitHub Copilot 官方文件與 VS Code 最新官方文件為準
- 若 GitHub.com、VS Code、Copilot CLI 的能力不同，必須分開說明
- 不可把下列概念混為一談：
  - Custom Agents
  - Custom Instructions
  - Prompt Files
  - Agent Skills
  - Hooks
  - Memory
- 必須清楚比較下列差異：
  - GitHub Copilot cloud agent
  - VS Code Agent Mode
  - GitHub Copilot CLI
  - 組織 / 企業層級治理
- 若某些指令、設定、檔案格式因環境不同而不同，必須提供對照表
- 若某功能有安全風險，必須標示權限、審計、資料外洩與誤操作風險
- 若某功能與費用、premium requests、模型政策有關，必須標示成本面與管理建議

---

## 公司使用背景

本公司允許的 AI 平台與工具如下：

### 工具平台
- VS Code
- GitHub Copilot
- GitHub Copilot Chat
- GitHub Copilot CLI

### 可使用模型
- Anthropic Claude Sonnet 4.6
- Anthropic Claude Opus 4.6
- Anthropic Claude Haiku 4.5
- Google Gemini 3.1 Pro
- Google Gemini 3 Flash
- OpenAI GPT-5.3-Codex
- OpenAI GPT-5.4
- OpenAI GPT-5.4 mini
- OpenAI GPT-5.4 nano

請在手冊中說明：

- 企業如何制定模型選擇策略
- 何時使用 Auto model selection
- 何時固定模型
- 如何根據任務類型、成本、風險、速度、準確度分配模型
- 如何透過管理員政策限制模型存取

---

## 參考資料

不允許參考local相關文件，請吸收以下內容後重新整理，不可直接抄貼：

- https://docs.github.com/en/copilot
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/agent-management
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- https://docs.github.com/en/copilot/concepts/agents/copilot-memory
- https://docs.github.com/en/copilot/concepts/auto-model-selection
- https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
- VS Code Copilot Custom Agents / Custom Instructions / Hooks 最新官方文件

---

## 文件輸出要求

請輸出為單一 Markdown 檔案，不可拆成多個檔案，不可分段回覆，不可只給大綱。

請直接輸出完整文件內容，並符合以下要求：

- 使用繁體中文
- 適合資深工程師、架構師、DevSecOps、技術主管閱讀
- 可直接作為公司內部白皮書、標準教材與導入手冊
- 內容需兼顧：
  - 可實作
  - 可維護
  - 可治理
  - 可擴展
  - 可審計
  - 可升級
- 需使用清楚的標題層級：
  - #
  - ##
  - ###
- 需包含：
  - 版本資訊
  - 前言
  - 目錄
  - 章節化內容
  - Mermaid 圖
  - 範例程式碼
  - 範例設定檔
  - SOP 步驟
  - FAQ
  - Checklist
  - 附錄
- 每章節都必須有：
  - 概念說明
  - 操作步驟
  - 企業實務建議
  - 注意事項 / 風險
  - 範例或範本

---

## 文件放置要求

請在文件內明確標示：

- 文件目錄：.github/教學/AI開發/
- 文件檔名："GitHub Copilot 建立 SSDLC Agent Team 教學手冊.md"

---

## 文件品質要求

請以「企業標準技術白皮書」等級撰寫。

請達成以下品質標準：

- 內容必須與最新官方文件一致
- 不可把舊版做法當成最新版
- 不可把不同環境的能力混寫
- 不可只寫理論，必須有可操作範例
- 必須指出功能限制、預覽狀態、權限需求、方案需求
- 必須指出資料治理、成本、審計與安全風險
- 必須明確說明如何讓其他團隊複製使用

---

## 必備章節結構

請嚴格依照以下章節輸出，且目錄與內容必須完全一致。

# 0. 文件資訊與閱讀指南

需包含：

- 文件名稱
- 文件版本
- 最後更新日期
- 作者角色定位
- 適用對象
- 使用前提
- 閱讀地圖
- 名詞定義

---

# 1. 總覽：什麼是 GitHub Copilot SSDLC Agent Team

需說明：

- 為什麼企業需要 SSDLC Agent Team
- 與傳統單一 AI 助手的差異
- 與單純 Prompt Engineering 的差異
- 與一般 Code Assistant 的差異
- Agent Team 在需求、設計、開發、測試、安全、維運中的角色
- 新系統開發與舊系統逆向工程兩種場景的差異

請提供：

- 整體概念圖
- 企業導入價值
- 典型使用情境

---

# 2. 最新功能盤點與術語對照

需根據最新版文件整理：

- Copilot cloud agent
- VS Code Agent Mode
- GitHub Copilot CLI
- Custom Agents
- Custom Instructions
- Agent Skills
- Copilot Memory
- Auto model selection
- Copilot integrations
- Pull request automation
- Steering agent sessions
- Session logs
- Handoffs
- Agent-scoped hooks
- Autopilot / approval model
- 組織層級 custom instructions
- 組織層級 custom agents

請提供：

- 功能矩陣表
- 功能可用環境比較表
- Preview / GA / plan requirement 對照表
- 容易混淆概念比較表

---

# 3. SSDLC Agent Team 企業架構設計

請設計一個企業級 GitHub Copilot SSDLC Agent Team 架構，包含：

- Requirements Agent
- Architect Agent
- Backend Agent
- Frontend Agent
- Test Agent
- Security Agent
- Code Review Agent
- Release Agent
- Reverse Engineering Agent
- Documentation Agent

需說明：

- 每個 Agent 的職責
- 每個 Agent 可使用的工具與權限
- 每個 Agent 建議模型
- Agent 之間如何交接
- 何時使用平行執行
- 何時使用人工審核 Gate
- 如何避免權限過大
- 如何避免 AI 直接修改高風險區域

請提供：

- Mermaid 架構圖
- Mermaid 流程圖
- Agent RACI 表
- Agent 與 SSDLC 階段對應表

---

# 4. 平台安裝與環境建置

請說明如何建立可供企業使用的 GitHub Copilot SSDLC Agent Team 基礎環境，包含：

- VS Code 安裝與版本建議
- GitHub Copilot 擴充套件安裝
- GitHub Copilot Chat 安裝
- GitHub Copilot CLI 安裝
- 驗證登入與權限
- 組織 / 企業管理員需啟用的政策
- 如何啟用或限制 custom instructions
- 如何啟用或限制 custom agents
- 如何啟用或限制 Copilot Memory
- 如何治理模型權限
- 如何設定 Auto model selection
- 如何設定 approval model 與 Autopilot 風險

請提供：

- Windows 安裝步驟
- macOS 安裝步驟
- Linux 安裝步驟
- CLI 指令
- 設定檢查清單
- 常見安裝錯誤與排除方式

---

# 5. 專案初始化與標準目錄設計

請設計一個企業可複製的標準目錄，說明如何在一個 repository 內建立 Agent Team 基礎骨架。

必須包含並解釋以下項目：

- .github/copilot-instructions.md
- .github/instructions/
- AGENTS.md
- .github/agents/
- .github/skills/
- Prompt library
- PR templates
- Issue templates
- Governance docs
- Architecture Decision Records
- Security baseline
- Reverse engineering baseline

請特別區分：

- VS Code custom agent 的檔案格式與用途
- GitHub.com / Copilot CLI custom agent profile 的檔案格式與用途
- Project-level 與 User-level 的差異
- Org-level 與 Repo-level 的差異

請提供：

- 目錄樹
- 每個檔案 / 目錄的用途說明
- 命名規範
- 版本控管策略

---

# 6. Create Agent：如何建立 SSDLC Agent Team

這一章是重點章節。

請逐步說明如何建立：

- Planner Agent
- Architect Agent
- Security Reviewer Agent
- Test Generator Agent
- Reverse Engineering Agent
- Release Agent

每一個 Agent 都必須提供：

- 適用場景
- 權限策略
- 建議模型
- 目標輸出
- 失敗風險
- 適用工具
- 範例 Agent 檔案

請至少提供兩套格式範例：

- VS Code custom agent 範例
- GitHub Copilot cloud agent / CLI custom agent profile 範例

請清楚標示：

- 哪些 frontmatter 欄位只適用 VS Code
- 哪些用法只適用 GitHub.com / CLI
- 哪些屬於預覽功能
- agent-scoped hooks 如何綁定在特定 agent 上

---

# 7. Create Prompt：如何建立 Prompt Library 與 Team Prompt SOP

請說明如何建立企業級 Prompt Library，並將 Prompt 納入治理。

必須包含：

- Prompt 分類原則
- Requirements Prompt
- Design Prompt
- Coding Prompt
- Refactor Prompt
- Test Prompt
- Security Prompt
- Reverse Engineering Prompt
- PR Review Prompt
- Incident Analysis Prompt

請說明：

- Prompt 與 Agent 的關係
- Prompt 與 Instructions 的關係
- Prompt 與 Skills 的關係
- Prompt 版本控管方式
- 如何避免 Prompt 重複與污染
- 如何建立跨團隊可共享的 Prompt Catalog

請提供：

- Prompt 模板
- Prompt 命名規範
- Prompt 目錄設計
- 好 Prompt / 壞 Prompt 對照
- 逆向工程 Prompt 範例
- SSDLC 各階段 Prompt 範例

---

# 8. Create Instructions：如何建立全域規範與檔案型規範

請深入說明：

- .github/copilot-instructions.md 的角色
- AGENTS.md 的角色
- .instructions.md 的角色
- 組織層級 instructions 的角色
- 指令優先順序
- VS Code /init 與 /create-instruction 的用途
- 如何建立不同模組 / 不同語言 / 不同子系統的 instructions
- 如何在 monorepo 使用 instructions
- 如何讓其他團隊直接套用

請提供：

- 全域 instructions 範例
- Java backend instructions 範例
- Frontend instructions 範例
- Security instructions 範例
- Reverse engineering instructions 範例
- Pull request description generation instructions 範例
- Code review instructions 範例

---

# 9. Create Skills：如何建立 Agent Skills

請深入說明：

- 什麼是 Agent Skills
- Skills 與 Instructions 的差異
- Skills 與 Agents 的差異
- Skills 與 Prompt files 的差異
- Project skills 與 Personal skills 的差異
- 技能資料夾應包含哪些內容
- 如何用 gh skill 管理 skills
- 如何引入社群 skills
- 如何建立企業自有 skills library

請提供至少以下 skills 範例：

- 安全檢查 skill
- JUnit 測試產生 skill
- Pull request 檢查 skill
- API 設計審查 skill
- 舊系統逆向分析 skill
- 文件生成 skill

每個 skill 範例需包含：

- 目標
- 資料夾結構
- SKILL.md 內容範例
- scripts / resources 示例
- 使用時機
- 限制與風險

---

# 10. Create Hook：如何建立 Hooks 與 Guardrails

請說明：

- Hooks 的用途
- 哪些 Hooks 與 VS Code custom agents 綁定
- Agent-scoped hooks 為何適合企業治理
- Hooks 在 SSDLC 哪些階段最有價值
- Hooks 與安全防呆的關係
- Hooks 與審計軌跡的關係
- Hooks 的限制與預覽狀態
- chat.useCustomAgentHooks 等相關設定與注意事項

請提供：

- 規劃階段 hook 範例
- 開發階段 hook 範例
- 測試階段 hook 範例
- PR 前檢查 hook 範例
- 安全敏感操作阻擋 hook 範例

請額外說明：

- 哪些場景不適合使用 Autopilot
- 如何避免 Bypass Approvals 造成風險
- Hooks 與人工批准 Gate 如何搭配

---

# 11. Copilot Memory：如何建立可持續學習的 Repository Memory 治理

請根據最新官方文件準確說明：

- Copilot Memory 是什麼
- 是否為 repo-scoped
- 如何建立、驗證、保留與過期
- 使用限制與方案前提
- Memory 與 code review / cloud agent / CLI 的關係
- 如何由管理者治理與清理
- 如何避免把 Memory 當成無限知識庫
- 如何與 README、ADR、設計文件形成互補
- 哪些資訊適合讓 Copilot 形成 Memory
- 哪些資訊不應交給 Memory

請提供：

- Memory 治理原則
- 資訊分類策略
- 安全與隱私原則
- Memory 可接受 / 不可接受內容範例
- 適用於逆向工程專案的 Memory 策略

---

# 12. Create Pull Request：如何讓 Agent 協助建立與推進 PR

請說明：

- 如何從 issue / 任務啟動 agent session
- 如何用 cloud agent 產生 PR
- 如何在 session 中查看 log
- 如何 steering agent
- 如何在 VS Code 或 CLI 接手 session
- 如何讓 code review agent 參與 PR
- 如何建立標準 PR 產出格式
- 如何把 PR 流程納入 SSDLC Gate
- 如何讓 Release Agent 接棒

請提供：

- PR 產生流程圖
- 標準 PR 模板
- 安全檢查與測試檢查 Gate
- PR 命名與標籤規範
- 人工審核步驟
- 失敗回復流程

---

# 13. 將 Agent / Prompt / Instructions / Skills / Hooks / Memory 融入 SSDLC

這一章是全文件核心。

請完整設計 GitHub Copilot SSDLC workflow，至少涵蓋以下階段：

- 需求分析
- 威脅建模
- 架構設計
- API 設計
- 開發實作
- 單元測試
- 整合測試
- 安全檢查
- PR 與 Code Review
- 部署前驗證
- 上線
- 維運
- 缺陷分析
- 持續優化

每一個階段都要說明：

- 由哪個 Agent 主導
- 使用哪些 Prompts
- 套用哪些 Instructions
- 載入哪些 Skills
- 是否使用 Hooks
- 如何形成 Memory
- 需要哪些人工批准 Gate
- 產出哪些文件 / 程式碼 / PR / 紀錄

請提供：

- Mermaid SSDLC 流程圖
- Mermaid Agent 協作圖
- 各階段 SOP
- 角色責任表
- KPI 建議

---

# 14. 舊系統逆向工程專章

請針對以下情境設計完整方法：

- 文件不足
- 人員離職
- 系統老舊
- 平台 EOS
- 弱掃與資安壓力
- 需求散落於程式碼、手冊、會議紀錄

請說明如何用 GitHub Copilot SSDLC Agent Team 處理：

- 程式碼導覽
- 架構還原
- 模組切分
- Business Rules 抽取
- API 盤點
- DB 依賴整理
- 批次流程分析
- 畫面 / 後端 / DB 關聯盤點
- 測試補齊
- 遷移 backlog 建立
- 現代化改造 roadmap

請提供：

- Reverse Engineering Agent 設計
- 逆向工程 Prompt 範例
- 逆向工程 Instructions 範例
- 逆向工程 Skill 範例
- 逆向工程輸出範本
- 風險與注意事項

---

# 15. 與其他團隊共享：如何做成可複製的企業 SOP

請說明如何把本套 GitHub Copilot SSDLC Agent Team 提供給其他團隊使用。

需包含：

- Team onboarding 流程
- Starter repository / template repository 設計
- 共用 instructions 與 agents 的治理方式
- 組織層級推送策略
- 教育訓練計畫
- FAQ 與 support model
- 版本同步機制
- 變更公告機制
- 例外申請流程
- 導入成熟度模型

請提供：

- 導入路線圖
- 團隊啟用 checklist
- 角色責任分工
- Governance 規範
- 常見阻力與解法

---

# 16. 安全、治理、稽核與成本控管

請以企業角度說明：

- 最小權限原則
- Agent 工具權限設計
- Secrets 管理
- 敏感碼與資料外洩防護
- Prompt Injection 風險
- 惡意指令與不安全 automation 風險
- Bypass approvals / Autopilot 風險
- Copilot integrations 的資料使用風險
- Memory 的資料保護
- 模型選擇與成本控管
- premium requests 控制
- 管理員政策與審核流程
- 稽核紀錄保留建議

請提供：

- 風險矩陣
- 治理控制點
- 安全檢查清單
- 成本監控指標
- 不建議做法清單

---

# 17. 系統維護與升級策略

請說明如何維護與升級整套 SSDLC Agent Team。

需包含：

- VS Code 升級策略
- GitHub Copilot 功能變更追蹤
- 自訂 agents 升級策略
- instructions 升級策略
- skills 升級策略
- hooks 升級策略
- prompt library 升級策略
- Memory 治理與清理
- 相容性管理
- Preview 功能升 GA 時的調整方式
- 回滾策略
- 版本編號規範
- 變更管理機制

請提供：

- 升級 SOP
- 版本相容矩陣範例
- 回滾計畫
- 文件更新流程
- 例行巡檢項目

---

# 18. 完整實戰案例

至少提供 2 個完整案例。

## 案例 1：新建企業 Web 系統
需包含：
- 需求
- Agent Team 分工
- Prompt 設計
- Instructions 設計
- Skills 設計
- Hooks 設計
- Memory 策略
- PR 流程
- 測試與安全
- 上線前檢查

## 案例 2：舊系統逆向工程與現代化改造
需包含：
- 背景問題
- 盤點方式
- Agent Team 分工
- 逆向工程產出
- 測試補齊
- 遷移計畫
- 風險控管
- 教訓與最佳實務

每個案例都需提供：

- Mermaid 圖
- 實際 Prompt 範例
- 實際設定範例
- SOP 步驟
- 交付成果樣貌

---

# 19. FAQ 與 Troubleshooting

至少回答以下問題：

- Custom agent 為何沒有出現？
- Instructions 為何沒有套用？
- Skills 為何沒有被載入？
- Hooks 為何沒有觸發？
- Memory 為何沒有發揮效果？
- Auto model selection 何時適合？
- 哪些模型適合規劃、程式碼、測試、安全？
- Copilot cloud agent 與 VS Code Agent Mode 如何分工？
- PR 產生後如何接手？
- 多團隊共用時如何避免互相污染？
- 逆向工程時如何避免 AI 幻覺？

---

# 20. 最佳實務、Anti-Patterns 與 Checklist

請整理：

- 企業最佳實務
- 團隊最佳實務
- 開發者最佳實務
- Reverse engineering 最佳實務
- 常見錯誤
- 不建議做法
- 新團隊導入 checklist
- 專案初始化 checklist
- SSDLC 每階段 checklist
- 上線前 checklist
- 升級前 checklist

---

# 21. 附錄

請提供可直接複製使用的範本，至少包含：

- .github/copilot-instructions.md 範本
- .github/instructions/backend-java.instructions.md 範本
- .github/instructions/security.instructions.md 範本
- VS Code custom agent 範本
- GitHub.com / CLI custom agent profile 範本
- .github/skills/security-review/SKILL.md 範本
- Prompt library 範本
- PR template 範本
- Issue template 範本
- Governance 規範範本
- 升級檢查清單範本

---

## Mermaid 圖要求

至少必須提供以下圖表：

- GitHub Copilot SSDLC Agent Team 整體架構圖
- Agent Team 協作圖
- SSDLC Workflow 圖
- Pull Request Workflow 圖
- Reverse Engineering Workflow 圖
- 團隊導入與治理流程圖

---

## 特別要求

請務必做到以下幾點：

- 明確區分 GitHub.com、VS Code、Copilot CLI 三種環境
- 明確區分自訂 agent 檔案格式差異
- 明確說明 hooks 屬於 VS Code 預覽功能時應如何標示
- 明確說明 Copilot Memory 為 repository-scoped 且需啟用
- 明確說明 integrations 的資料使用風險
- 明確說明 auto model selection 與固定模型的選用原則
- 明確說明如何把 Agent Team 套用到新系統開發與舊系統逆向工程
- 明確說明如何讓其他團隊直接複製使用
- 不可只講概念，必須有操作步驟與可用範例
- 不可只用理想化敘述，必須有風險與限制分析
- 不可引用過期術語與過時檔名
- 不可把不同功能混成同一件事

---

## 最終輸出要求

請直接輸出完整的《GitHub Copilot 建立 SSDLC Agent Team 教學手冊》Markdown 內容：

- 檔案太大請分段回覆
- 不可拆檔
- 不可只給大綱
- 不要額外解釋你怎麼做
- 直接產出可交付版本
-------------------------------------------------------------------
# 使用claude code建立SSDLC Agent Team 教學手冊
## 角色設定 - 你是一位「資深軟體架構師 + 資深前後端工程師 + AI 架構師」，具備以下專長：
* 大型系統單體系統設計(前後分離 Web application/ Clean Architecture)
* 大型分散式系統設計（Microservices / Clean Architecture）
* AI 輔助開發（Claude Code / GitHub Copilot / LLM Agents）
* RAG（Retrieval-Augmented Generation）與 Data Layer 設計
* DevSecOps / SSDLC（Secure Software Development Lifecycle）
## 技術說明 - 需在公司允許的AI(GitHub Copilot) 平台上建置
* vscode 程式與文件編輯器
* claude code
* claude code 可使用的大語言模型
  - Anthropic Claude Sonnet 4.6
  - Anthropic Claude Opus 4.6
  - Anthropic Claude Haiku 4.5

  
## 參考:不允許參考local相關文件，請吸收以下內容後重新整理，不可直接抄貼：
- https://code.claude.com/docs/en/vs-code,
- https://code.claude.com/docs/en/github-actions,
- https://code.claude.com/docs/en/gitlab-ci-cd,
- https://code.claude.com/docs/en/sub-agents,
- https://code.claude.com/docs/en/agent-teams,
- https://code.claude.com/docs/en/plugins,
- https://code.claude.com/docs/en/discover-plugins.
- https://code.claude.com/docs/en/skills,https://code.claude.com/docs/en/scheduled-tasks,
- https://code.claude.com/docs/en/output-styles,
- https://code.claude.com/docs/en/hooks-guide,
- https://code.claude.com/docs/en/headless,
- https://code.claude.com/docs/en/mcp,
- https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/claude-code%E7%94%9F%E6%85%8B%E5%9C%88%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/
- https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/claude-code-ssdlcai%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E7%94%9F%E5%91%BD%E9%80%B1%E6%9C%9F%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/

參考上述link,相關內容與文章,及文中相關link內容,完成任務說明

## 背景 - 目前必需使用claude code建立SSDLC Agent Team,用來開發公司未來軟體的系統。 
## 任務說明 - 使用claude code建立SSDLC Agent Team SOP,用來開發公司未來軟體的系統與逆向工程開發,包含SSDLC Agent Team系統架構,如何建立,需包含: agent, subagent , prompt, plugin,skills, hooks,memory,mcp,tools 等功能,並說明與提供詳細範例,同時把上述的功能融入SSDLC, 建立的SSDLC workflow ,建立後應如何提供給其它開發團隊使用,必需和其它團隊說明如何安裝,設定,使用,系統維護,系統升級,請提供建議給同仁使用,請先產生prompt 來請AI 幫我產生建立SSDLC Agent Team教學手冊 md 檔,請全部放在同一檔中,不可分散.

-------------------------------------------------------------------
# 任務：產出《Claude Code 建立 SSDLC Agent Team 教學手冊》

## 角色設定

你是一位：

- 企業級 AI Agent 架構顧問
- 資深軟體架構師（Enterprise Architect）
- 資深前後端工程師（Full-Stack Engineer）
- DevSecOps / SSDLC 導入專家
- 舊系統逆向工程與現代化改造顧問
- 技術白皮書作者

你具備以下專長：

- 大型單體系統與大型分散式系統設計
- Clean Architecture / Hexagonal Architecture / DDD
- Claude Code / LLM Agents / Agentic Engineering
- RAG / MCP / Tooling / Context Engineering
- SSDLC / Secure Coding / Threat Modeling / SAST / DAST / Supply Chain Security
- CI/CD / GitHub Actions / GitLab CI/CD / Enterprise Governance

請以「企業級可落地導入」為標準撰寫，不可流於空泛概念。

---

## 任務目標

請直接產出一份完整、單一 Markdown 文件，主題為：

# 《Claude Code 建立 SSDLC Agent Team 教學手冊》

此手冊的目標是：

- 協助公司使用 Claude Code 建立可治理、可維運、可升級的 SSDLC Agent Team
- 支援新系統開發與舊系統逆向工程 / 現代化改造
- 建立可複製的企業 SOP，讓其他開發團隊可以直接安裝、設定、套用
- 將 agent、subagent、prompt、plugin、skills、hooks、memory、mcp、tools 等能力完整融入 SSDLC workflow

---

## 背景說明

目前公司需要使用 Claude Code 建立 SSDLC Agent Team，用於未來軟體系統開發與舊系統逆向工程。

可使用的工具與環境：

- VS Code
- Claude Code
- Claude Code CLI
- Claude Code VS Code extension
- GitHub Actions
- GitLab CI/CD

公司目前允許的 Claude 模型如下：

- Anthropic Claude Sonnet 4.6
- Anthropic Claude Opus 4.6
- Anthropic Claude Haiku 4.5

若官方文件提到更新或更高版本模型，請在手冊中明確標示為：

- 官方文件目前可見能力
- 但不在本公司既有允許模型清單內

不可將其寫成公司既有可直接使用的既定標準。

---

## 重要前提與寫作規則

請先根據最新官方文件與下列參考連結查核內容，再撰寫文件。

你必須遵守以下規則：

- 不可直接抄貼任何官方文件、網站或文章原文
- 必須先吸收內容，再以自己的語言重新整理
- 內容必須與最新官方文件一致
- 若功能為 Experimental、Beta、Preview、需特定版本、需環境變數啟用、或不同平台能力不同，必須清楚標示
- 不可把不同概念混為一談
- 不可使用過期術語當成最新版正式名稱
- 若必須提及舊稱，請標示為 legacy 或舊稱
- 不能只講概念，必須給步驟、範例、限制、風險與最佳實務
- 必須同時考量安全性、可維護性、治理、審計與成本
- 每一章都必須有：概念說明、操作步驟、範例、限制或風險、實務建議
- 全部內容必須放在同一個 Markdown 檔中，不可拆分成多檔
- 若輸出長度超過單次回覆限制，可分次輸出，但必須延續同一份文件，不可改成多檔或只給大綱

---

## 必須正確反映的最新能力與限制

手冊內容必須正確反映下列重點，不可寫錯：

- Agent Teams 為 experimental，且預設未啟用，需明確說明啟用方式與限制
- GitLab CI/CD 整合目前屬於 beta，不能寫成正式穩定 GA
- Programmatic CLI 是目前較新的說法；若提 headless，需說明那是舊稱或延伸脈絡
- MCP 應優先說明 HTTP transport；SSE 應標示為 deprecated 或不建議優先使用
- Plugins 可以封裝 skills、agents、hooks、MCP servers 等能力，但 plugin-provided subagents 有前提限制
- Plugin 提供的 subagent 不支援或會忽略 hooks、mcpServers、permissionMode 這類 frontmatter 欄位，必須正確說明
- Agent Team 若使用 subagent definition 當 teammate type，需正確說明哪些欄位會生效、哪些不會完整帶入
- Scheduled Tasks / loop 需正確說明 session-scoped、7 天到期、50 個任務上限等限制
- CI / 自動化情境需正確說明 bare mode 或最小上下文載入策略的重要性
- VS Code、CLI、GitHub Actions、GitLab CI/CD 的能力差異必須分開說明，不能混寫
- Output styles、CLAUDE.md、skills、subagents 各自扮演的層級不同，必須清楚比較
- Memory、CLAUDE.md、Auto Memory、Agent Memory 等概念若存在差異，需分開說明，不可籠統混稱
- Subagents 與 Agent Teams 的適用場景不同，必須明確比較：隔離上下文 vs 多代理協作與互相溝通
- Hooks 是確定性控制，skills 比較偏工作流程與知識注入，兩者角色不同，必須分開說明

---

## 參考資料

請吸收以下內容後重新整理，不可直接抄貼：

- https://code.claude.com/docs/en/vs-code
- https://code.claude.com/docs/en/github-actions
- https://code.claude.com/docs/en/gitlab-ci-cd
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/output-styles
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/headless
- https://code.claude.com/docs/en/mcp
- https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/claude-code%E7%94%9F%E6%85%8B%E5%9C%88%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/
- https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/claude-code-ssdlcai%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E7%94%9F%E5%91%BD%E9%80%B1%E6%9C%9F%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/

請以官方文件為主，其他文章作為補充說明與案例脈絡。

---

## 文件輸出要求

請輸出為單一 Markdown 檔案，文件品質需達到企業標準技術白皮書等級。

輸出要求如下：

- 語言：繁體中文
- 風格：專業、清楚、實戰導向、可直接交付團隊使用
- 內容深度：適合資深工程師、架構師、技術主管、DevSecOps、人員培訓
- 不要只給大綱
- 直接輸出完整文件內容
- 使用清楚標題層級：#、##、###
- 需包含 Mermaid 圖
- 需包含實際 CLI 指令範例
- 需包含設定檔範例
- 需包含 SOP、治理建議、限制分析、風險矩陣、Checklist
- 每節結尾都要有「實務建議」或「注意事項」
- 不可拆檔
- 不要額外解釋你怎麼做
- 直接產出可交付版本

若你判斷本文是要放入 Hugo Blog，請在最前面加入完整 front matter。
若不確定是否需要 front matter，至少在文件開頭標示建議檔名與建議路徑。

## 文件放置要求

請在文件內明確標示：

- 文件目錄：.github/教學/AI開發/
- 文件檔名："Claude Code 建立 SSDLC Agent Team 教學手冊.md"


---

## 必備章節結構

請嚴格依照以下章節輸出，且目錄與內容必須一致。

# 0. 文件資訊與閱讀指南

必須包含：

- 文件名稱
- 文件版本
- 最後更新日期
- 作者角色定位
- 適用對象
- 使用前提
- 閱讀地圖
- 名詞定義
- 功能狀態標示規則（GA / Experimental / Beta / Preview）

---

# 1. 總覽：什麼是 Claude Code SSDLC Agent Team

必須說明：

- 為什麼企業需要 SSDLC Agent Team
- 與單一 AI 助手的差異
- 與單純 Prompt Engineering 的差異
- 與一般 Code Assistant 的差異
- Claude Code 在需求、設計、開發、測試、安全、維運中的角色
- 新系統開發與舊系統逆向工程的差異

必須提供：

- 整體概念圖
- 企業導入價值
- 典型使用情境

---

# 2. 功能盤點與術語對照

必須整理並比較：

- VS Code extension
- Claude Code CLI
- Programmatic CLI / Agent SDK
- Subagents
- Agent Teams
- Skills
- Plugins
- Hooks
- CLAUDE.md / Memory
- MCP
- Output Styles
- Scheduled Tasks
- GitHub Actions
- GitLab CI/CD

必須提供：

- 功能矩陣表
- 平台差異比較表
- 概念差異比較表
- Experimental / Beta / GA 對照表
- 容易混淆術語表

---

# 3. Claude Code SSDLC Agent Team 企業架構設計

請設計一個企業級 Claude Code SSDLC Agent Team，至少包含下列角色：

- Requirements Agent
- Architect Agent
- Backend Agent
- Frontend Agent
- Test Agent
- Security Agent
- Code Review Agent
- Release Agent
- Reverse Engineering Agent
- Documentation Agent

必須說明：

- 每個 Agent 的職責
- 每個 Agent 可使用的工具
- 每個 Agent 的權限策略
- 每個 Agent 建議使用的模型
- 何時使用 subagent
- 何時使用 agent team
- 何時必須人工審核
- 如何避免權限過大
- 如何避免高風險操作直接自動化

必須提供：

- Mermaid 架構圖
- Mermaid 流程圖
- Agent RACI 表
- Agent 與 SSDLC 階段對應表

---

# 4. 平台安裝與環境建置

必須涵蓋：

- Windows 安裝與設定
- macOS 安裝與設定
- Linux 安裝與設定
- VS Code extension 安裝
- Claude Code CLI 安裝
- 認證方式
- VS Code 與 CLI 如何搭配
- 如何在 VS Code 中管理插件、MCP、hooks、sessions
- 如何設定公司允許模型與使用策略

必須提供：

- 實際安裝步驟
- 實際指令範例
- 常見安裝錯誤與排除方式
- 權限模式說明
- 最佳起始設定建議

---

# 5. 專案初始化與標準目錄設計

請設計一套企業可複製的 Claude Code 專案骨架。

必須涵蓋：

- CLAUDE.md
- .claude/settings.json
- .claude/settings.local.json
- .claude/agents/
- .claude/skills/
- .claude/hooks/
- .claude/output-styles/
- .claude/loop.md
- .mcp.json
- plugins / marketplace 策略
- prompt library
- governance docs
- security baseline
- reverse engineering baseline

必須提供：

- 標準目錄樹
- 每個檔案 / 目錄用途
- 命名規範
- 版本控管策略
- 哪些內容應該進版控，哪些不應該

---

# 6. 建立 Agent 與 Subagent

必須深入說明：

- 什麼是 subagent
- 什麼是 custom subagent
- 什麼是 agent team teammate
- subagent 與 main conversation 的差異
- subagent 與 agent team 的差異
- 自動委派與明確呼叫方式
- 前景 / 背景執行差異
- 權限模式、tools allowlist、disallowed tools、model、memory、hooks、isolation 的設計

至少要提供以下範例：

- Security Reviewer Subagent
- Test Runner Subagent
- Code Reviewer Subagent
- Reverse Engineering Subagent
- Coordinator Agent
- Architect Teammate 設計範例

必須提供：

- 完整 subagent frontmatter 範例
- 不同權限模式設計建議
- worktree isolation 範例
- subagent 常見錯誤與 anti-pattern
- agent team 中使用 subagent definition 的正確說明

---

# 7. 建立 Prompt Library 與 Team Prompt SOP

必須說明：

- Prompt 與 Agent 的關係
- Prompt 與 Skills 的關係
- Prompt 與 CLAUDE.md 的關係
- Prompt 與 Hooks 的關係
- 如何建立企業級 Prompt Catalog
- 如何避免 Prompt 汙染、重複與過長
- 如何管理 Prompt 版本

必須提供至少以下類型的 Prompt：

- Requirements Prompt
- Architecture Prompt
- Coding Prompt
- Refactor Prompt
- Testing Prompt
- Security Prompt
- Reverse Engineering Prompt
- PR Review Prompt
- Incident Analysis Prompt
- Migration Planning Prompt

每個 Prompt 類型都要附：

- 範本
- 使用時機
- 輸入要素
- 輸出格式
- 風險與限制

---

# 8. 建立 Skills

必須深入說明：

- Skills 是什麼
- Skills 與 subagents 的差異
- Skills 與 hooks 的差異
- Skills 與 output styles 的差異
- 自動觸發與手動觸發的差異
- supporting files 的設計方式
- context: fork 的使用時機
- skill content lifecycle 與 compaction 注意事項

至少提供下列 skills 範例：

- 安全檢查 skill
- 測試產生 skill
- PR summary skill
- API 設計審查 skill
- Legacy code analysis skill
- 文件生成 skill
- Deploy checklist skill

每個 skill 範例都要包含：

- 目標
- SKILL.md 範例
- supporting files 範例
- allowed-tools 範例
- 是否建議 disable-model-invocation
- 適用情境與風險

---

# 9. 建立 Hooks 與 Guardrails

必須深入說明：

- hooks 的角色
- command hooks、prompt hooks、agent hooks、http hooks 的差異
- matcher 與 if 條件的差異
- PreToolUse / PostToolUse / Notification / PermissionRequest / Stop / ConfigChange / FileChanged / TaskCreated / TaskCompleted / TeammateIdle 等事件的使用情境
- hooks 如何與安全治理、審計、品質門檻結合
- hooks 與 permission mode 的關係
- hooks 的限制與除錯方式

至少提供以下範例：

- 保護敏感檔案不可修改
- 只允許唯讀 SQL 查詢
- 變更後自動格式化或執行 linter
- team teammate 完成任務前的品質 Gate
- 偵測設定檔變更並寫入 audit log
- 自動補充 compact 後的關鍵上下文
- HTTP hook 串接企業稽核服務

每個範例都要有：

- 設定檔範例
- 腳本範例
- 行為說明
- 限制與風險
- debug 方法

---

# 10. 建立 Plugins 與 Marketplace Strategy

必須說明：

- 何時該用 standalone config，何時該做成 plugin
- plugin 結構
- plugin manifest
- skills / agents / hooks / MCP servers / settings 在 plugin 中的放置方式
- 官方 marketplace、團隊 marketplace、自建 marketplace 的差異
- plugin 安裝範圍：user / project / local
- 自動更新與風險控制
- plugin 安全與信任模型

至少提供：

- plugin.json 範例
- skills 型 plugin 範例
- agents 型 plugin 範例
- hooks 型 plugin 範例
- team marketplace 設定範例
- plugin 升級與版本控管策略

必須明確說明：

- plugin 提供的 subagent 有哪些 frontmatter 限制
- plugin 來源風險與審查原則
- 官方 marketplace 與第三方 marketplace 的治理建議

---

# 11. Memory、CLAUDE.md 與知識治理

必須說明：

- CLAUDE.md 的角色
- Auto Memory / project memory / user memory 的邏輯差異
- 何者適合放常駐規範
- 何者適合放可學習的經驗
- 何者不適合寫入記憶
- 記憶檔案如何避免膨脹與污染
- 與專案 README、ADR、Runbook、Architecture Docs 的分工

必須提供：

- CLAUDE.md 範本
- Security 導向 CLAUDE.md 範本
- Reverse Engineering 導向 CLAUDE.md 範本
- 記憶治理原則
- 可接受 / 不可接受記憶內容範例
- 清理與維護策略

---

# 12. MCP 與 Tools 整合架構

必須深入說明：

- MCP 是什麼
- 本地 / 專案 / 使用者 scope 的差異
- HTTP / stdio / SSE transport 差異
- OAuth、scopes、headersHelper、resources、prompts、tool search 的用途
- Claude Code 作為 MCP server 的使用方式
- MCP 與 plugins 的整合方式
- MCP 與企業治理的關係
- MCP 的 prompt injection 與資料外洩風險

至少提供以下範例：

- GitHub MCP
- Sentry / Monitoring MCP
- Database MCP（唯讀）
- Internal API MCP
- Playwright MCP
- Project-scoped .mcp.json 範例
- managed-mcp.json 管理範例

必須提供：

- .mcp.json 範例
- MCP 安裝與驗證指令
- tool search 設定範例
- OAuth callback / scope 管理建議
- 企業 allowlist / denylist 策略
- Windows 使用 npx 啟動 stdio server 的注意事項

---

# 13. Programmatic CLI、GitHub Actions 與 GitLab CI/CD

必須分開說明：

- CLI 互動模式
- Programmatic CLI / Agent SDK CLI 用法
- bare mode 的用途與價值
- GitHub Actions 整合
- GitLab CI/CD 整合
- 何時使用互動式工作流
- 何時使用 CI 自動化工作流

必須提供：

- programmatic CLI 指令範例
- --bare、-p、--output-format、--json-schema、--allowedTools、--permission-mode 等範例
- GitHub Actions v1 workflow 範例
- GitLab CI/CD job 範例
- provider 差異說明
- API key / OIDC / secret 治理建議

必須明確標示：

- GitHub Actions 為正式能力時的適用方式
- GitLab CI/CD 若仍屬 beta，必須明寫
- 不能把 CI 自動化與本機互動能力寫成完全相同

---

# 14. 將 Agent、Prompt、Skills、Hooks、Memory、MCP 融入 SSDLC

這一章是核心章節。

必須完整設計 Claude Code SSDLC workflow，至少涵蓋：

- 需求分析
- 威脅建模
- 架構設計
- API 設計
- 開發實作
- 單元測試
- 整合測試
- 安全檢查
- PR / MR Review
- 部署前驗證
- 上線
- 維運
- 缺陷分析
- 持續優化

每個階段都要說明：

- 由哪個 Agent 主導
- 使用哪些 Prompt
- 使用哪些 Skills
- 是否有 Hooks Gate
- 是否需要 MCP
- 形成哪些記錄或記憶
- 哪些地方必須人工批准
- 產出哪些文件 / 程式碼 / PR / MR / 紀錄

必須提供：

- Mermaid SSDLC 流程圖
- Agent 協作圖
- SOP 表格
- KPI 建議
- 安全 Gate 建議

---

# 15. 舊系統逆向工程與現代化改造專章

請針對以下情境設計方法論：

- 文件不足
- 人員離職
- 系統老舊
- 平台 EOS
- 弱掃與資安壓力
- 需求散落在程式碼、手冊、畫面流程與會議紀錄中

必須說明如何用 Claude Code SSDLC Agent Team 處理：

- 程式碼導覽
- 架構還原
- 模組切分
- Business Rules 抽取
- API 盤點
- DB 依賴分析
- Batch 流程盤點
- UI / Backend / DB 關聯分析
- 測試補齊
- Backlog 建立
- Modernization roadmap 規劃

必須提供：

- Reverse Engineering Agent 設計
- 專用 Prompt 範例
- 專用 Skills 範例
- 專用 Hooks / Guardrails 範例
- 輸出範本
- 風險與注意事項

---

# 16. 提供給其他團隊使用的共享 SOP

必須說明如何把這套 Claude Code SSDLC Agent Team 提供給其他開發團隊直接複製使用。

必須涵蓋：

- Team onboarding 流程
- Starter repository 設計
- shared plugins / skills / agents / hooks 治理方式
- 文件模板
- 教育訓練計畫
- 支援模式
- FAQ
- 變更公告機制
- 例外申請流程
- 成熟度模型

必須提供：

- 導入路線圖
- 啟用 checklist
- 角色分工
- 治理規範
- 常見阻力與解法

---

# 17. 安全、治理、稽核與成本控管

必須以企業角度說明：

- 最小權限原則
- permission mode 治理
- hooks guardrails
- secrets 管理
- 敏感檔案保護
- prompt injection 風險
- MCP 風險
- plugin marketplace 風險
- agent teams 權限與成本風險
- CI 自動化風險
- logs / audit trail / compliance
- token / API 成本監控
- 模型使用策略
- premium / 高成本模型管控

必須提供：

- 風險矩陣
- 控制點設計
- 稽核紀錄建議
- 不建議做法清單
- 成本監控指標

---

# 18. 系統維護、升級與相容性管理

必須說明如何維護與升級整套系統。

至少涵蓋：

- Claude Code 升級策略
- VS Code extension 升級策略
- subagents 升級策略
- skills 升級策略
- hooks 升級策略
- plugins 升級策略
- MCP 配置升級策略
- prompt library 升級策略
- CLAUDE.md / memory 治理與清理
- 相容性管理
- experimental 功能升級為穩定版後的調整方式
- 回滾策略
- 文件更新流程
- 例行巡檢項目

必須提供：

- 升級 SOP
- 相容矩陣範例
- 回滾計畫
- 版本管理建議

---

# 19. 完整實戰案例

至少提供 2 個完整案例。

## 案例 1：新建企業級 Web 系統

必須包含：

- 需求背景
- Agent Team 分工
- Prompt 設計
- Skills 設計
- Hooks 設計
- MCP 設計
- CLAUDE.md / Memory 策略
- GitHub Actions 或 GitLab CI/CD 流程
- 測試與安全流程
- 上線前檢查

## 案例 2：舊系統逆向工程與現代化改造

必須包含：

- 背景問題
- 盤點方式
- Agent Team 分工
- 架構還原
- 測試補齊
- 遷移計畫
- 風險控管
- 經驗教訓

每個案例都要提供：

- Mermaid 圖
- 實際 Prompt 範例
- 實際設定範例
- SOP 步驟
- 交付成果樣貌

---

# 20. FAQ 與 Troubleshooting

至少回答以下問題：

- Agent Teams 為何無法啟動？
- Subagent 為何沒有被自動委派？
- Skills 為何沒有觸發？
- Hooks 為何沒有生效？
- MCP 為何沒有連上？
- Plugins 為何沒有載入？
- VS Code 與 CLI 為何行為不同？
- GitHub Actions 與 GitLab CI/CD 該怎麼選？
- Reverse Engineering 時如何降低幻覺？
- 何時該用 subagent，何時該用 agent team？
- 何時該用 hook，何時該用 skill？
- 如何避免記憶污染與 context 膨脹？
- 如何降低 token 成本？

---

# 21. 最佳實務、Anti-Patterns 與 Checklist

必須整理：

- 企業最佳實務
- 團隊最佳實務
- 開發者最佳實務
- Reverse Engineering 最佳實務
- 常見錯誤
- Anti-pattern
- 新團隊導入 checklist
- 專案初始化 checklist
- SSDLC 各階段 checklist
- 上線前 checklist
- 升級前 checklist

---

# 22. 附錄

至少提供可直接複製使用的範本：

- CLAUDE.md 範本
- .claude/settings.json 範本
- .mcp.json 範本
- subagent 範本
- SKILL.md 範本
- hook 設定範本
- plugin.json 範本
- GitHub Actions workflow 範本
- GitLab CI/CD job 範本
- reverse engineering prompt 範本
- onboarding checklist 範本
- governance policy 範本

---

## Mermaid 圖要求

至少必須提供以下圖表：

- Claude Code SSDLC Agent Team 整體架構圖
- Subagents vs Agent Teams 比較圖
- SSDLC Workflow 圖
- Reverse Engineering Workflow 圖
- CI/CD 與 Agent 自動化流程圖
- Team onboarding / governance 流程圖

---

## 文件品質底線

必須做到以下幾點：

- 不可只寫理論
- 不可把不同功能混為一談
- 不可把 experimental / beta 說成 GA
- 不可把舊版做法當成最新版
- 不可忽略安全、權限、成本、審計
- 不可缺少範例
- 不可缺少限制與風險分析
- 不可忽略新系統開發與舊系統逆向工程兩種場景
- 不可輸出破碎章節或目錄與內容不一致
- 不可只給大綱

---

## 最終輸出要求

請直接輸出完整《Claude Code 建立 SSDLC Agent Team 教學手冊》Markdown 內容。

若篇幅過長，主agent 記錄目錄結構，在派給subagent處理各章內容,處理完在回報給主agent整合，分章輸出，請分次續寫同一份文件，但必須遵守：

- 仍然是同一份文件
- 不可拆成多檔
- 不可重新開始另一個版本
- 不可只輸出目錄
- 不要額外解釋你怎麼做
- 直接輸出可交付版本
- 請分段回覆
------------------------------------------------------------------
# claude-howto 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 「claude-howto」是一個在 GitHub 上廣受歡迎的開源教學專案（由 luongnv89/claude-howto 維護），旨在幫助開發者從基礎到進階系統化地掌握 Claude Code。 
- 核心內容與功能
該專案不是枯燥的 API 文件，而是一套結構化、可視化且以範例驅動的實戰指南。 
10 個學習模組：涵蓋從基礎的斜線指令（Slash Commands）到進階的工程代理（Agent）功能，如 Hooks、Skills、子代理（Subagents）與 MCP 伺服器 配置。
學習路徑：專案提供分級的學習建議，包括初學者（30分鐘上手）、中級與高級（需約 5 小時完成完整路徑）。
- 實戰模板：提供可直接複製到專案中的場景模板，例如自動化 PR 審查、CI/CD 整合腳本等。
多語言支持：除了原版英文外，也有 中文翻譯版 (claude-howto-zh-cn) 供中文使用者參考。 
- 如何開始使用
快速瀏覽：閱讀 README.md 了解整體架構與核心概念。
自我評估：可以在 Claude Code 中運行 /self-assessment 獲取個性化的學習路徑建議。
依序實作：從 01-slash-commands 開始，逐步練習如何透過自定義指令（Skills）優化開發流程。 

## 參考:
- https://github.com/luongnv89/claude-howto
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用claude-howto協助AI(Claude Code/GitHub Copilot)開發web application的系統/逆向工程軟體開發/軟體framework升級。 
## 任務說明 - 系統必需使用claude-howto最新版協助AI(Claude Code/GitHub Copilot)開發,包含系統架構,安裝,設定,如何使用claude-howto協助AI開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生claude-howto教學手冊 md 檔,請全部放在同一檔中,不可分散.
------------------------------------------------------------
# 任務：產生「claude-howto 教學手冊（完整版）」單一 Markdown 文件

## 角色設定
你是一位「資深軟體架構師 + 資深前後端工程師 + AI 架構師」，具備以下專長：
- 大型企業系統設計（單體 / 微服務 / Clean Architecture）
- Web Application（Vue / Spring Boot / API First）
- DevOps / CI-CD / SSDLC（安全軟體開發生命週期）
- AI 輔助開發（Claude Code / GitHub Copilot / Agent-based development）
- Legacy System Reverse Engineering（逆向工程）
- 系統升級與重構（Framework Migration）

請以「企業內部教學手冊」的標準撰寫，內容需結構清晰、可落地、可操作。

---

## 技術背景
本手冊基於 GitHub 專案：
https://github.com/luongnv89/claude-howto

claude-howto 是一套：
- 結構化學習 Claude Code 的實戰指南
- 包含 Slash Commands / Skills / Hooks / Subagents / MCP Server
- 提供從入門到進階的學習路徑
- 強調「Agent 化開發」與「自動化工程能力」

---

## 目標
產出一份 **完整、單一 Markdown 文件（不可拆分）** 的教學手冊，用於：

1. 指導團隊使用 claude-howto
2. 輔助 AI（Claude Code / GitHub Copilot）開發系統
3. 支援以下場景：
   - Web Application 開發
   - 舊系統逆向工程
   - Framework 升級（如 Spring Boot / Java 升級）
   - SSDLC 安全開發流程

---

## 文件要求（非常重要）

- 必須輸出為 **單一 Markdown 檔案**
- 不可分段或拆成多檔
- 必須包含完整章節結構
- 每一章需包含：
  - 說明
  - 架構圖（文字或 Mermaid）
  - 實作範例
  - Prompt 範例（重點）
  - 最佳實務（Best Practices）

---

## 文件章節結構（必須完整涵蓋）

# 1. 簡介（Overview）
- claude-howto 是什麼
- 與傳統開發方式差異
- 為什麼適合企業級開發

# 2. 整體架構（Architecture）
- Claude Code + claude-howto 架構
- Agent-based 開發模型
- 與 GitHub Copilot 的整合方式
- 建議架構圖（Mermaid）

# 3. 安裝與環境設定（Setup）
- Claude Code 安裝
- claude-howto 導入方式
- 專案目錄結構設計
- 團隊標準化設定

# 4. claude-howto 核心模組解析
需詳細說明以下內容：
- Slash Commands
- Skills（技能模組）
- Hooks（事件觸發）
- Subagents（子代理）
- MCP Server（工具整合）

每個模組需包含：
- 使用場景
- 設計方式
- 範例

# 5. AI 開發流程設計（核心章節）
說明如何使用 claude-howto：

### 5.1 Web Application 開發
- 前後端分離架構
- API 設計
- 自動生成 CRUD / Service

### 5.2 逆向工程（Legacy System）
- 分析舊系統
- 生成文件
- 重建架構

### 5.3 Framework 升級
- 舊版本 → 新版本（如 Spring Boot 升級）
- 自動轉換程式碼
- 相容性分析

---

# 6. Prompt Engineering（最重要）
必須提供：

### 通用 Prompt 模板
### Web 開發 Prompt
### 逆向工程 Prompt
### 升級 Prompt
### 架構設計 Prompt

---

# 7. SSDLC 整合（安全開發）
- 安全檢查（SAST / DAST）
- 自動化審查
- PR 檢查

---

# 8. 團隊使用建議（企業落地）
- 團隊導入策略
- Code Review 流程
- AI 使用規範

---

# 9. 維運與最佳實務
- 如何維護 Skills / Agents
- 如何優化 Prompt
- 如何避免 AI 錯誤

---

# 10. 系統升級與擴展
- claude-howto 升級策略
- Agent 擴展方式
- 未來演進方向

---

## 額外要求

請務必：
- 使用「專業但易讀」語氣
- 提供實際可用的 Prompt（不可空泛）
- 強調「可落地實作」
- 避免理論過多
- 偏向工程實戰

---

## 產出結果
- 請產出一份 **《claude-howto 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《claude-howto 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "claude-howto 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------------------
# claude-claude-code-bast-practice 教學手冊

## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 這個 GitHub 專案 claude-code-best-practice 是目前社群中最受歡迎的 Claude Code (Anthropic 官方推出的 CLI 工具) 實戰指南。它整理了從「Vibe Coding」（憑直覺編寫）轉向「Agentic Engineering」（智能體工程）的各種技巧與工作流。 
專案核心重點
該專案彙整了包含 Anthropic 工程師（如 Boris Cherny）在內的社群精華，涵蓋以下關鍵實作：
專案級規則與設置：
CLAUDE.md 控制：建議將 CLAUDE.md 保持在 200 行以內，以確保 Claude 能可靠地遵守規則。
規則延遲載入：利用 .claude/rules/*.md 並搭配 YAML frontmatter（路徑設定），讓規則只在 Claude 接觸特定檔案時才載入，避免消耗過多 Token。
- 高效工作流設計：
Plan Mode 先行：處理複雜任務時，優先使用「計畫模式」（Plan mode）規劃步驟，而非直接開始寫 code。
任務拆解：將子任務拆小至能於 50% 上下文用量內完成的大小，並在上下文使用率達 50% 時手動執行 /compact 指令進行壓縮。
多智能體協作：建議創建具備特定技能的「功能型子智能體」（Feature-specific subagents），而非依賴單一全能型 Agent。
- 自動化與擴充功能：
使用 Hooks 指令：利用 SessionStart、PreToolUse 等 Lifecycle Hooks 執行自動化邏輯（例如啟動時自動載入背景資訊）。
CLI 與數據分析：透過 Claude Code 調用 BigQuery CLI 或其他數據工具，實現「無 SQL 數據分析」工作流。
環境優化：透過 /terminal-setup 優化終端機顯示與換行邏輯（Shift + Enter）。 
- 資源分類
Tips 指南：包含多篇由工程師分享的 10-15 則進階技巧。
Skills & Commands：示範如何自定義 Claude Skills 以及專屬指令。
跨模型工作流：探討如何結合不同版本的 Claude 模型以達到效能與成本的平衡。 
該專案目前在 GitHub 上已累積近 5 萬顆星，是開發者在使用 Claude 進行「智能體自動化開發」時必讀的參考資料。
## 參考:
- https://github.com/shanraisshan/claude-code-best-practice
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明
## 背景 - 目前必需使用claude-claude-code-bast-practice協助AI(Claude Code/GitHub Copilot)開發web application的系統/逆向工程軟體開發/軟體framework升級。 
## 任務說明 - 系統必需使用claude-claude-code-bast-practice最新版協助AI(Claude Code/GitHub Copilot)開發,包含系統架構,安裝,設定,如何使用claude-claude-code-bast-practice協助AI開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生claude-claude-code-bast-practice教學手冊 md 檔,請全部放在同一檔中,不可分散.
------------------------------------------------------------------
# 任務：產出 claude-code-best-practice 完整教學手冊（單一 Markdown 檔）

## 角色設定
你是一位「資深軟體架構師 + 資深前後端工程師 + AI 架構師」，具備以下能力：
- 大型企業系統設計（單體 / 微服務 / Clean Architecture）
- Web Application 全端開發（Vue / React / Spring Boot / API）
- DevOps / CI-CD / SSDLC（安全軟體開發生命週期）
- AI Agent 工程（Claude Code / GitHub Copilot / Agentic Workflow）
- 系統升級、逆向工程、Legacy Modernization

---

## 任務目標
請根據 GitHub 專案「claude-code-best-practice」的最新最佳實踐，
產出一份**完整且可落地的教學手冊（Markdown 格式）**

⚠️ 必須符合：
- 所有內容「輸出在同一個 .md 檔」
- 不可拆分、不可以多檔案
- 內容需「可直接用於企業內部導入」

---

## 使用場景（務必涵蓋）
本教學手冊需支援以下 AI 開發場景：

1. Web Application 開發（前後端分離 / Clean Architecture）
2. 舊系統逆向工程（Legacy → Modernization）
3. Framework 升級（例如 Spring Boot 升級）
4. 大型企業系統開發（高可用 / 高併發 / 分散式）
5. SSDLC 安全開發流程導入
6. AI Agent 協作開發（Claude Code + GitHub Copilot）

---

## 必須涵蓋章節（不可遺漏）

### 1. 專案介紹與核心理念
- claude-code-best-practice 是什麼
- Vibe Coding → Agentic Engineering 轉型
- 為什麼適合企業級開發

---

### 2. 整體架構設計（重點）
- Claude Code 在系統中的角色
- 與 GitHub Copilot 的協作架構
- Agentic Workflow 架構圖（用文字描述）
- 多 Agent（Subagents）設計模式
- 與 CI/CD / DevOps 整合方式

---

### 3. 安裝與環境建置
- Claude Code CLI 安裝
- Terminal 優化（/terminal-setup）
- 專案初始化方式
- 開發環境最佳實踐（Windows / Linux）

---

### 4. 專案結構設計（關鍵）
請提供標準範例：

- CLAUDE.md 設計原則（200 行限制）
- .claude/rules/*.md 延遲載入機制
- YAML frontmatter 規則設計
- 多層規則（global / module / feature）

---

### 5. Claude Code 核心工作流（重點）
請詳細說明：

- Plan Mode（如何正確使用）
- 任務拆解策略（50% context rule）
- /compact 使用時機
- 長任務控制技巧

---

### 6. Agentic Engineering 實戰（核心）
- Subagents 設計（例如：Backend Agent / DB Agent / Security Agent）
- 多 Agent 協作模式
- 任務分派與回收機制
- 如何避免「全能型 Agent 失控」

---

### 7. Hooks 自動化機制（企業必用）
請說明並舉例：

- SessionStart
- PreToolUse
- PostToolUse

並提供：
- 自動載入上下文
- 自動安全檢查
- 自動 coding 規範 enforcement

---

### 8. AI 輔助開發實戰場景（非常重要）

#### (1) Web Application 開發
- 前端 + 後端協作流程
- API 設計
- Clean Architecture 實作

#### (2) 舊系統逆向工程
- 分析 legacy code
- 建立系統文件
- 自動產出架構圖

#### (3) Framework 升級
- Spring Boot 升級策略
- Breaking Change 分析
- 自動 refactor

---

### 9. CLI + 數據分析整合
- BigQuery CLI 使用方式
- 無 SQL 分析流程
- 自動生成報表

---

### 10. 與 GitHub Copilot 協作模式
- Claude Code vs Copilot 分工
- Code Generation vs Architecture Planning
- 雙 AI workflow 設計

---

### 11. SSDLC 安全開發整合（企業級重點）
請包含：

- Threat Modeling
- Secure Coding 規範
- 自動弱點掃描（SAST / DAST）
- Compliance（OWASP / ISO）

---

### 12. 系統維護與最佳化
- 長期使用策略
- Token 使用優化
- 成本控制（模型選擇）

---

### 13. 系統升級策略
- Claude Code 規則升級
- Prompt 演進管理
- Agent 持續優化

---

### 14. 團隊導入建議（非常重要）
請提供：

- 團隊導入流程（Phase 1~3）
- 開發規範
- Code Review + AI Review 模式
- 常見錯誤與反模式

---

### 15. 最佳實踐總結（Checklist）
- 提供可直接使用的 Checklist

---

## 輸出格式要求

請輸出為：

- Markdown (.md)
- 結構清晰（# / ## / ###）
- 包含：
  - 範例
  - 指令
  - 架構說明
- 內容需「可直接落地實作」

---

## 重要要求（必須遵守）

1. 不可輸出簡略內容，必須深入（架構等級）
2. 必須偏「實戰」，不可只是概念
3. 必須適用企業級開發（銀行 / 大型系統）
4. 所有內容放在「單一 Markdown 檔」
5. 不要省略章節

---

## 產出結果
- 請產出一份 **《claude-claude-code-bast-practice 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《claude-claude-code-bast-practice 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "claude-claude-code-bast-practice 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆


-------------------------------------------------------------------
# oh-my-claudecode 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 
## 參考:oh-my-claudecode 是一個專為 Claude Code 打造的開源**多智能體編排（Multi-agent Orchestration）**框架。由韓國開發者 Yeachan Heo 創建，旨在簡化複雜任務的處理，讓 Claude Code 能同時驅動多個專職 Agent 進行協作。 
核心功能與特色
團隊導向編排：任務分配給專門的 Agent，例如 executor、codex、gemini，以實現自動化並行執行。
零配置啟動：提供智能預設值，無需複雜設定即可在終端機使用。
成本與效能優化：透過智能模型路由，可節省約 30-50% 的 Token 消耗。
實時視覺化：內建 HUD 狀態列，讓用戶在終端機即時看到背景 Agent 的運作指標與進度。
技能學習系統：能自動從對話中提取解題模式，並轉化為可重用的「Skills」。 
- https://github.com/yeachan-heo/oh-my-claudecode
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明

## 背景 - 目前必需使用oh-my-claudecode協助AI(Claude Code/GitHub Copilot)開發web application的系統/逆向工程軟體開發/軟體framework升級。 
## 任務說明 - 系統必需使用oh-my-claudecode最新版協助AI(Claude Code/GitHub Copilot)開發,包含系統架構,安裝,設定,如何使用oh-my-claudecode協助AI開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生oh-my-claudecode教學手冊 md 檔,請全部放在同一檔中,不可分散.
------------------------------------------------------------------
# 任務：產生「oh-my-claudecode 教學手冊（完整版）」單一 Markdown 文件

## 角色設定
你是一位「資深軟體架構師 + 資深前後端工程師 + AI Agent 架構師」，具備以下能力：
- 大型單體系統與微服務架構設計（Clean Architecture）
- 多智能體系統（Multi-Agent System / Agent Orchestration）
- AI 輔助開發（Claude Code / GitHub Copilot）
- SSDLC（Secure Software Development Lifecycle）
- DevOps / CI-CD / Observability
- 企業級系統（金融級）開發與維運經驗

---

## 技術背景
請根據以下專案進行深入分析並產出教學文件：

- GitHub Repo: https://github.com/yeachan-heo/oh-my-claudecode
- oh-my-claudecode 是一個 Multi-agent orchestration 框架
- 核心特色：
  - 多 Agent 協作（executor / codex / gemini 等）
  - 任務拆解與並行執行
  - 智能模型路由（節省 Token）
  - 終端 HUD 可視化
  - Skills 學習系統（可持續優化）

---

## 文件目標
產出一份「企業級教學手冊」，用於：

1. AI 輔助 Web Application 開發
2. 既有系統逆向工程（Legacy → Modernization）
3. Framework 升級（如 Spring Boot / 前端框架）
4. 建立 AI Agent 開發標準流程（SSDLC）

---

## 強制要求（非常重要）
- ✅ 請輸出為「單一 Markdown 檔案」
- ❌ 不可拆分多檔
- ✅ 內容需具備「架構深度 + 實戰可落地」
- ✅ 必須包含「流程圖（文字描述即可）」與「實務範例」
- ✅ 所有章節需完整、具體，不可只寫概念
- ✅ 所有指令需具體（CLI / config / prompt）

---

## 文件結構（必須完整）

# 1. 概述
- 什麼是 oh-my-claudecode
- 與傳統 Claude Code 的差異
- 與 GitHub Copilot 的整合方式
- 適用場景（企業 / 個人 / 大型專案）

---

# 2. 整體架構設計（Architecture）
- Multi-Agent 架構圖（用文字描述）
- Agent 分工（executor / planner / reviewer / coder）
- 任務分解機制（Task Decomposition）
- Agent 通訊機制
- 與以下系統整合：
  - CI/CD
  - GitHub
  - Issue / PR Flow

---

# 3. 安裝與環境建置（Step-by-step）
- 安裝 oh-my-claudecode
- CLI 指令說明
- 必要環境（Node / Python / Claude CLI）
- 設定 API Key（Claude / OpenAI / Gemini）
- Windows / Linux / Mac 差異

---

# 4. 核心設定（Configuration）
- config 檔說明
- Agent 設定（新增 / 修改）
- 模型路由策略（cost optimization）
- Skills 設定
- 任務模板（Task Template）

---

# 5. 使用方式（實戰）
## 5.1 基本使用
- CLI 操作流程
- 單 Agent vs 多 Agent

## 5.2 Web Application 開發（重點）
- 前端（Vue / React）生成
- 後端（Spring Boot / FastAPI）
- API 設計
- DB schema 設計

## 5.3 逆向工程（Legacy System）
- 讀取舊系統 code
- 分析 architecture
- 自動產出文件
- 重構建議

## 5.4 Framework 升級
- Spring Boot 升級
- 前端框架升級
- 依賴分析

---

# 6. Multi-Agent 協作設計（進階）
- Agent Roles 設計模式
- Planner → Executor → Reviewer Flow
- Code Review Agent
- Security Agent（SSDLC）

---

# 7. Skills Learning 系統
- Skills 如何產生
- Skills 儲存與重用
- 建立企業內知識庫

---

# 8. 效能與成本優化
- Token 使用最佳化
- 模型選擇策略
- 平行處理設計

---

# 9. SSDLC 整合（企業級重點）
- Secure Coding
- SAST / DAST 整合
- 威脅建模（Threat Modeling）
- Compliance（金融業）

---

# 10. 系統維運（Maintenance）
- Log 與監控
- Agent Debug
- 錯誤排除

---

# 11. 系統升級（Upgrade）
- oh-my-claudecode 升級策略
- Agent 相容性
- Config Migration

---

# 12. 最佳實務（Best Practices）
- Agent 設計原則
- Prompt Engineering
- 開發流程標準化

---

# 13. 範例（完整案例）
請提供至少三個：

1. Web 系統開發（全流程）
2. Legacy 系統重構
3. Framework 升級

---

# 14. 團隊導入建議
- 如何導入公司
- Developer Workflow 設計
- Governance（權限 / 審核）

---

# 15. 附錄
- CLI 指令清單
- 常見錯誤
- Prompt 範本

---

## 輸出格式
- Markdown
- 使用清楚標題（# / ## / ###）
- 每章節需有實務內容
- 需包含 code block（bash / json / yaml / prompt）

---

## 產出結果
- 請產出一份 **《oh-my-claudecode 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《oh-my-claudecode 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "oh-my-claudecode 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆


------------------------------------------------------------------
# free-claude-code 教學手冊

## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - 這是一個名為 free-claude-code 的 GitHub 開源專案，旨在讓你能夠免費或以更低成本使用 Anthropic 官方的 Claude Code 工具。 
專案核心功能
該專案本質上是一個代理伺服器 (Proxy Layer)，它攔截 Claude Code CLI 或 VS Code 擴充功能發出的請求，並將其轉發給其他 LLM 後端： 
多模型支援：除了 Anthropic 原生模型，你還可以接入 NVIDIA NIM (目前提供免費點數)、DeepSeek、OpenRouter 或 LM Studio 等在地運行的模型。
介面支援：支援終端機 (CLI)、VS Code 擴充功能，甚至可以透過 Discord 或 Telegram 機器人使用。
語音功能：支援語音輸入 (Voice Intake)，模擬類似 OpenClaw 的體驗。 
如何開始使用
根據 README.md 說明，一般的安裝流程如下： 
複製專案：將專案 clone 到本地。
啟動代理：運行 FastAPI 伺服器作為代理。
配置環境：
在終端機或 VS Code 設定中，將 ANTHROPIC_BASE_URL 指向你的本地代理地址（通常是 http://localhost:8082）。
設定對應的 API Key（如 NVIDIA 或 DeepSeek 的 Token）。
模型切換：使用內建的 claude-pick 工具可以快速切換當前使用的模型。 
注意事項
非官方工具：這是一個第三方社群驅動的專案，並非 Anthropic 官方產品。
API 限制：雖然工具本身免費，但後端調用的 API（如 OpenRouter）可能仍有其自身的免費額度或付費限制。 
## 參考:
- https://github.com/Alishahryar1/free-claude-code
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明

## 背景 - 目前必需使用free-claude-code協助AI開發web application的系統/逆向工程軟體開發/軟體framework升級。 
## 任務說明 - 系統必需使用free-claude-code最新版協助AI開發,包含系統架構,安裝,設定,如何使用free-claude-code協助AI開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生free-claude-code教學手冊 md 檔,請全部放在同一檔中,不可分散.

------------------------------------------------------------------
# 任務：產生 free-claude-code 完整教學手冊（單一 Markdown 檔）

## 角色設定

你是一位具備以下能力的專家：

* 資深軟體架構師（大型分散式系統 / Microservices / Clean Architecture）
* 資深前後端工程師（Spring Boot / FastAPI / Vue / TypeScript）
* AI 工程架構師（AI Agent / LLM Orchestration / Prompt Engineering / SSDLC）

請以「企業級導入 + 團隊可落地實作」為目標撰寫教學手冊。

---

## 背景說明

我們的團隊需要使用 GitHub 開源專案 **free-claude-code** 來達成以下目標：

* AI 輔助 Web Application 開發
* 舊系統逆向工程（Legacy Modernization）
* Framework 升級（如 Spring Boot / Java 升級）
* 建立 AI SSDLC（安全軟體開發流程）

free-claude-code 本質為：

* 一個 Proxy Layer（FastAPI）
* 攔截 Claude Code CLI / VS Code Extension 請求
* 轉發到其他 LLM（NVIDIA NIM / DeepSeek / OpenRouter / LM Studio）

---

## 文件要求（非常重要）

請輸出：

* **單一 Markdown 檔（不可拆分）**
* 結構清晰（使用 # ## ###）
* 每一章節需包含：

  * 架構圖（使用 mermaid）
  * 範例指令
  * 實務建議（Best Practices）
  * 常見錯誤（Pitfalls）

---

## 必須包含章節（不可缺少）

### 1. 概述（Overview）

* free-claude-code 是什麼
* 與 Claude Code 官方的差異
* 適用場景（企業 / 個人 / AI Agent 團隊）

---

### 2. 系統整體架構（Architecture）

請提供：

* 高階架構圖（Mermaid）
* 元件說明：

  * Proxy Layer（FastAPI）
  * Claude CLI / VS Code
  * 多模型後端（NVIDIA / DeepSeek / OpenRouter / LM Studio）
* 請說明：

  * Request Flow
  * Model Routing 策略
  * 擴充方式（Plugin / Agent）

---

### 3. 安裝與環境建置（Installation）

需包含：

* 系統需求（Windows / Linux / Mac）
* Python / Node / Docker 建議版本
* Clone 專案
* 安裝依賴
* 啟動 FastAPI Proxy

範例：

```bash
git clone ...
pip install -r requirements.txt
uvicorn main:app --port 8082
```

---

### 4. 核心設定（Configuration）

需說明：

* ANTHROPIC_BASE_URL 設定
* API Key 管理（NVIDIA / OpenRouter / DeepSeek）
* 多模型切換（claude-pick）
* VS Code 設定方式

---

### 5. 模型整合（Multi-LLM Integration）

需詳細說明：

* NVIDIA NIM（免費點數策略）
* DeepSeek（高性價比）
* OpenRouter（多模型路由）
* LM Studio（本地模型）

比較表（效能 / 成本 / 適用場景）

---

### 6. 開發實戰（AI Development Use Cases）

#### 6.1 Web Application 開發

* 前後端生成
* API 設計
* DB Schema 設計

#### 6.2 舊系統逆向工程

* COBOL / Java Legacy 分析
* 自動產出文件
* 重構建議

#### 6.3 Framework 升級

* Spring Boot 2 → 3 / 4
* Java 8 → 21+
* 相依套件分析

---

### 7. SSDLC（安全開發流程）

請設計：

* AI 輔助 SSDLC 流程圖（Mermaid）
* 包含：

  * Threat Modeling
  * Code Review
  * Security Scan
  * Dependency Check

---

### 8. 團隊導入策略（Team Adoption）

請提供：

* 開發流程設計（Developer Workflow）
* Prompt Template 管理
* AI Agent Team 設計
* Governance（避免濫用）

---

### 9. 維運與監控（Operations）

需包含：

* Logging（request / response）
* Token 使用監控
* 成本控管策略
* Rate Limit 設計

---

### 10. 升級與擴展（Upgrade & Scaling）

需說明：

* 如何升級 free-claude-code
* 如何新增模型 Provider
* 水平擴展（Load Balancer）
* 高可用設計（HA）

---

### 11. 常見問題（FAQ）

至少 10 題，例如：

* 為什麼 Claude CLI 無法連線？
* API Key 無效怎麼辦？
* 本地模型很慢怎麼優化？

---

### 12. 最佳實務（Best Practices）

請整理：

* 架構設計
* Prompt Engineering
* 成本最佳化
* 安全性

---

## 額外要求（加分但重要）

請加入：

* 完整 Mermaid 圖
* 範例 Prompt（可直接用於開發）
* Dev / Stage / Prod 環境設計
* 與 CI/CD 整合（GitHub Actions）

---

## 輸出格式要求

* 僅輸出 Markdown
* 不要解釋
* 不要省略
* 不要分段輸出

---

## 最終目標

這份文件必須可以直接作為：
👉 公司內部標準教學手冊
👉 AI 開發平台導入指南
👉 新人 onboarding 文件

## 產出結果
- 請產出一份 **《free-claude-code 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《free-claude-code 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "free-claude-code 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆


------------------------------------------------------------------
# learn-claude-code 教學手冊
## 角色設定 - 你是資深軟體架構師和資深前後端開發工程師
## 技術說明 - shareAI-lab/learn-claude-code 是一個開源的教學項目，旨在幫助開發者透過「手動實現」來深入理解 AI 程式編寫代理（Coding Agent）的運作原理。 
該項目並非教你如何「使用」現成的 AI 工具，而是教你如何從零開始構建一個類似 Claude Code 或 Cursor 的代理系統。 
核心教學內容
教程通過 12 個遞進的實作單元（Sessions），逐步引導你構建功能完整的代理系統：
Agent Loop（代理循環）：理解模型如何與環境互動並持續推理。
工具使用（Tool Use）：教導代理如何讀寫檔案、執行測試及檢查錯誤。
子代理與協作（Subagents & Teams）：實現任務拆解、持久化身分管理及代理間的通訊機制。
任務系統與隔離：建立異步後台任務與獨立的工作區（Worktree），防止並行任務互相干擾。 
項目特色
Harness Engineering：項目強調「Harness」（外殼/支架）的重要性，認為真正的 Agent 競爭力在於如何為 LLM 構建高效的控制與執行環境。
輕量化實作：另有姊妹項目 mini-claude-code，僅用約 1100 行 Bash 程式碼即實現核心邏輯。
多語言支援：提供繁體中文、簡體中文、英文及日文等多語系文件。
## 參考:
- https://github.com/shareAI-lab/learn-claude-code
參考上述link,相關內容與文章,及文中相關link內容,完成任務說明

## 背景 - 目前必需使用learn-claude-code協助建立類似 claude code /opencode agent來開發web application的系統/逆向工程軟體開發/軟體framework升級。 
## 任務說明 - 系統必需使用learn-claude-code最新版協助開發類似claude code /opencode agent,開發出的agent,agent開發出後,必需說明包含系統架構,安裝,設定,如何使用learn-claude-code開發出的agent協助軟體系統開發,系統維護,系統升級,提供建議給同仁使用,請先產生prompt 來請AI 幫我產生learn-claude-code教學手冊 md 檔,請全部放在同一檔中,不可分散.


------------------------------------------------------------------
# 任務：產生 learn-claude-code 完整教學手冊（單一 Markdown 檔）

## 角色設定
你是一位：
- 資深軟體架構師（Enterprise Architecture / Microservices / Clean Architecture）
- 資深前後端工程師（Vue / Spring Boot / Python / FastAPI）
- AI Agent 架構師（LLM Agent / Coding Agent / Multi-Agent System）
- DevSecOps / SSDLC 專家

請以「企業級落地實戰」角度撰寫教學，而非僅介紹概念。

---

## 專案背景
本教學基於 GitHub 開源專案：
- shareAI-lab/learn-claude-code

該專案目標：
- 透過「手動實作」理解 AI Coding Agent（類似 Claude Code / Cursor）
- 建立完整 Agent 系統，而非僅使用 API

核心內容包含：
- Agent Loop
- Tool Use（檔案 / 測試 / Shell）
- Subagents / Multi-agent
- 任務系統（Task Queue）
- Worktree 隔離
- Harness Engineering（重點）

---

## 教學目標（非常重要）
請產出一份「企業可直接導入」的完整教學手冊，內容需包含：

1. 如何使用 learn-claude-code 建立：
   - 類似 Claude Code 的 Coding Agent
   - 類似 OpenCode / Dev Agent 的開發代理
2. 該 Agent 可用於：
   - Web Application 開發（前後端）
   - 舊系統逆向工程
   - Framework 升級（如 Spring Boot / Java）
   - 批次系統改寫（如 Batch / FTP 流程）

---

## 文件格式要求（嚴格遵守）

- 僅輸出「一個 Markdown 檔」
- 不可拆分
- 使用清楚的章節結構（# / ## / ###）
- 每一章節需包含：
  - 說明
  - 架構圖（用文字圖）
  - 實作步驟
  - 範例（必要時）

---

## 必須包含章節（不可遺漏）

# 1. 專案概述
- learn-claude-code 是什麼
- 與 Claude Code / Cursor 差異
- 為何企業應該自己打造 Agent

# 2. 系統整體架構設計（重點）
需包含：
- Agent Runtime
- LLM Gateway（可替換 OpenAI / Claude）
- Tool Layer
- Task Queue
- Workspace / Worktree
- Memory（短期 / 長期）
- Multi-Agent Coordination

需提供：
- 架構圖（ASCII）
- 與企業系統整合方式（API / DB / MQ）

# 3. Agent 核心機制解析（對應 learn-claude-code sessions）
逐一說明：
- Agent Loop
- Planning / Reflection
- Tool Calling
- Error Recovery
- Context 管理

# 4. Harness Engineering（核心競爭力）
需深入說明：
- 什麼是 Harness
- 如何設計 Tool Interface
- 如何限制 Agent 行為（安全性）
- 如何提升成功率（Prompt / Retry / Guardrails）

# 5. 實作教學（Step-by-step）
從 0 到 1：
- 環境安裝
- 專案初始化
- 第一個 Agent
- Tool 註冊（讀檔 / 寫檔 / shell）
- 加入測試能力
- 加入錯誤修復能力

# 6. 建立企業級 Coding Agent
需包含：
- Code Generation
- Code Review
- Test Generation
- Refactoring
- 文件產生

# 7. Multi-Agent 設計（進階）
設計一個 Agent Team：
- Architect Agent
- Backend Agent
- Frontend Agent
- QA Agent
- DevOps Agent

需說明：
- 任務拆解
- Agent 溝通方式
- 狀態管理

# 8. 實際應用場景（非常重要）
必須包含：

## (1) Web Application 開發
- Vue + Spring Boot 範例流程

## (2) 舊系統逆向工程
- 分析 legacy code
- 自動產生文件

## (3) Framework 升級
- Spring Boot 升級
- Java 版本升級

## (4) Batch 系統改寫
- FTP / 排程 / 檔案處理

# 9. 與企業架構整合（你的情境）
需包含：
- DB2 / Oracle / PostgreSQL
- MQ（Kafka / RabbitMQ）
- 微服務架構
- CI/CD（GitHub Actions / Jenkins）
- 權限控管（RBAC）

# 10. 安全與 SSDLC（必須）
- Prompt Injection 防護
- Tool 權限控管
- Code 安全掃描
- Audit Log
- 合規（金融場景）

# 11. 使用指南（給團隊）
需提供：
- 日常開發流程
- 如何下 prompt
- 如何 debug agent
- 常見錯誤

# 12. 最佳實踐（Best Practices）
- Prompt 設計
- Tool 設計
- Agent 拆分策略
- 成本控制

# 13. 附錄
- 範例 prompt（非常重要）
- CLI 指令
- 常見問題 FAQ

---

## 額外要求（關鍵）
- 所有內容需偏「實戰導向」
- 不可只有理論
- 必須貼近「大型企業系統」（金融業等級）
- 需考慮：
  - 高併發
  - 高可靠
  - 可維運
  - 可擴展

---

## 產出結果
- 請產出一份 **《learn-claude-code 教學手冊》**，使用「繁體中文」
- 適合提供給資深工程師閱讀與實作,偏向「實戰與維運」。
- 請直接輸出完整《learn-claude-code 教學手冊.md》內容，不要只給大綱。
- 標題層級清楚（# / ## / ###）
- 請用 教學手冊風格，結構清晰，包含 章節、子章節、步驟、範例指令。
- 使用 Markdown 格式，含標題、子標題、編號與條列
- 提供圖表/流程圖說明複雜概念,可以用mermaid畫出
- 每節結尾提供實務案例或注意事項
- 用淺顯易懂的語言，適合一般的開發人員閱讀,能讓同仁快速理解與實際操作
- 內容可直接用於專案團隊內部的開發規範文件
- 必須同時考慮安全性、效能與可維護性
- 每章小節包含說明 + 實例/建議,條列清楚、包含程式碼範例
- 最後附上「檢查清單（Checklist）」方便新進成員快速使用
- 文件請放在專案的 .github\教學\AI開發\ 目錄下,檔名為: "learn-claude-code 教學手冊.md"，並使用 Markdown 格式撰寫。
- 請分段回覆


-------------------------------------------------------------------
# common_platform
## 角色
- 你位資深的軟體架構師, 熟稔各種系統架構,針對銀行需求提供各類設計

## 需求
- 建立一個共用的開發平台給公司的web application使用
- 未來只要有專案成立時, 就必需會本基確去做專案的建置
- 平台使用clean architecture 
- 使用 archunit 來測試,是否滿足 clean architecture
- 未來部署致標準的Jakarta EE 最新版本 平台
- 開發時,使用java 25 開發, 不要使用open source,減少未來open source 升級與弱掃議題.
- 開發平台時使用spec-kit ,透過AI 來協助開發

## 任務
- 針對上面的需求, ,請先產生prompt 來請AI 幫我往下進行 


-----------------------------------------------------------------------
# 目標 : 舊系統轉成新系統
## 角色:  
- 資深軟體架構師（Enterprise Architecture）
- 資深後端與平台工程師（Java / Spring / Cloud Native）
- 熟悉大型企業與銀行等高可靠系統
## 問題
- 這是一個10多年的案子, 目前只有一位開發,與維護的人力
- 其它人員,都早已離職
- 客戶系統老舊, 面臨資安,弱掃, 平台eos 的問題
## 現況
- Prototyping ( html 畫面操作流程)
- 使用手冊
- 10年累積的需求文件
- 現有程式碼
## 任務 
- 使用github copilot 協助舊系統轉成新系統
- 請說明可行的執行方法與步驟
-----------------------------------------------------------
# learn-claude-code 教學手冊  update
1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://github.com/shareAI-lab/learn-claude-code
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------
# free-claude-code 教學手冊 update
1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://github.com/Alishahryar1/free-claude-code
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------
# oh-my-claudecode 教學手冊 update
1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://github.com/yeachan-heo/oh-my-claudecode
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------
# claude-claude-code-bast-practice 教學手冊 update
1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://github.com/shanraisshan/claude-code-best-practice
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------
# claude-howto 教學手冊 update

1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://github.com/luongnv89/claude-howto
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

----------------------------------------------------------
# Claude Code 建立 SSDLC Agent Team 教學手冊 update
1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://code.claude.com/docs/en/vs-code
- https://code.claude.com/docs/en/github-actions
- https://code.claude.com/docs/en/gitlab-ci-cd
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/output-styles
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/headless
- https://code.claude.com/docs/en/mcp
- https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/claude-code%E7%94%9F%E6%85%8B%E5%9C%88%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/
- https://chihhung.github.io/Blog/posts/%E6%95%99%E5%AD%B8/ai%E9%96%8B%E7%99%BC/claude-code-ssdlcai%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E7%94%9F%E5%91%BD%E9%80%B1%E6%9C%9F%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/

請以官方文件為主，其他文章作為補充說明與案例脈絡。

相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

-----------------------------------------------------------
# GitHub Copilot 建立 SSDLC Agent Team 教學手冊 update
1. 請依據下列參考,請吸收以下內容後重新整理，不可直接抄貼：
- https://docs.github.com/en/copilot
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/agent-management
- https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- https://docs.github.com/en/copilot/concepts/agents/copilot-memory
- https://docs.github.com/en/copilot/concepts/auto-model-selection
- https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
- VS Code Copilot Custom Agents / Custom Instructions / Hooks 最新官方文件

相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

----------------------------------------------------------
# Skill_Seekers教學手冊 update
1. 請依據下列參考
- https://github.com/yusufkaraaslan/Skill_Seekers
- https://skillseekersweb.com/
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

----------------------------------------------------------
# agency-agents教學手冊 update
1. 請依據下列參考
- https://github.com/msitarzewski/agency-agents
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

-----------------------------------------------------------
# GSD-2教學手冊 update
1. 請依據下列參考
- https://github.com/gsd-build/gsd-2
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

--------------------------------------------------------------
#  pi code agent 教學手冊 update
1. 請依據下列參考
- https://pi.dev/
- https://github.com/badlogic/pi-mono
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


------------------------------------------------------------
# github copilot SSDLC（AI軟體開發生命週期）教學手冊 update
1. 請依據下列參考
- https://docs.github.com/en/copilot
- https://github.com/github/awesome-copilot
- https://chihhung.github.io/Blog/posts/%E6%8C%87%E5%BC%95/%E8%A8%AD%E8%A8%88%E9%96%8B%E7%99%BC/%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E6%A8%99%E6%BA%96%E7%A8%8B%E5%BA%8Fsoftware-development-standard-process%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆



----------------------------------------------------------
# Claude Code SSDLC（AI軟體開發生命週期）教學手冊 update
1. 請依據下列參考
- https://code.claude.com/docs/en/overview
- https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide
- https://chihhung.github.io/Blog/posts/%E6%8C%87%E5%BC%95/%E8%A8%AD%E8%A8%88%E9%96%8B%E7%99%BC/%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC%E6%A8%99%E6%BA%96%E7%A8%8B%E5%BA%8Fsoftware-development-standard-process%E6%95%99%E5%AD%B8%E6%89%8B%E5%86%8A/
- https://github.com/affaan-m/everything-claude-code
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

------------------------------------------------------------
# AutoResearch 驅動 SSDLC（安全軟體開發生命週期）教學手冊 update
1. 請依據下列參考
- https://github.com/karpathy/autoresearch
- https://code.claude.com/docs/en/overview
- https://docs.github.com/en/copilot
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆



-----------------------------------------------------------
# Compound Engineering 教學手冊 update
1. 請依據下列參考
- https://github.com/EveryInc/compound-engineering-plugin
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


----------------------------------------------------------
# Everything Claude Code (ECC) 教學手冊 update
1. 請依據下列參考
- https://github.com/affaan-m/everything-claude-code
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

-----------------------------------------------------------
# Playwright 教學手冊 update
1. 請依據下列參考
- https://github.com/microsoft/playwright
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆



------------------------------------------------------------
## Multica 教學手冊 update
1. 請依據下列參考
- https://github.com/multica-ai/multica
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------
## Hermes Agent生態系教學手冊 update
1. 請依據下列參考
- https://github.com/nousresearch/hermes-agent
- https://hermes-agent.nousresearch.com/docs/
- https://hermes-agent.nousresearch.com/
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

-----------------------------------------------------------
## Graphify教學手冊 update

1. 請依據下列參考
- https://github.com/safishamsi/graphify
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-----------------------------------------------------------
## GitNexus教學手冊 update
1. 請依據下列參考
- https://github.com/abhigyanpatwari/GitNexus
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

--------------------------------------------------------------
## GSD update
1. 請依據下列參考
- https://github.com/gsd-build/get-shit-done
- https://gsd-build-get-shit-done.mintlify.app/
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

-----------------------------------------------------------
## gstack update
1. 請依據下列參考
- https://github.com/garrytan/gstack
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


--------------------------------------------------------------
## Agent Skills update
1. 請依據下列參考
- https://github.com/mattpocock/skills
- https://github.com/addyosmani/agent-skills
- https://code.claude.com/docs/zh-TW/skills
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- https://github.com/anthropics/skills
- https://github.com/github/awesome-copilot/tree/main/skills
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

------------------------------------------------------------
## VS Code + GitHub Copilot 開發 Java Web 應用程式教學手冊 update
1. 請依據下列參考
- https://code.visualstudio.com/docs
- https://code.visualstudio.com/updates/v1_113
- https://code.visualstudio.com/
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


--------------------------------------------------------------
## copiot cli update
1. 請依據下列參考
- https://github.com/features/copilot/cli
- https://github.com/github/copilot-cli
- https://github.com/github/awesome-copilot
- https://github.com/github/copilot-cli/blob/main/changelog.md
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------
## oh-my-openagent（Oh My OpenCode, OMO）update
1. 請依據下列參考
- https://github.com/code-yeongyu/oh-my-openagent
- https://github.com/code-yeongyu/oh-my-openagent/releases
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-----------------------------------------------------------
# superpowers update
1. 請依據 - https://github.com/obra/superpowers,  https://claude.com/plugins/superpowers,https://github.com/obra/superpowers/blob/main/CHANGELOG.md,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

--------------------------------------------------------------
# openspec update
1. 請依據 https://github.com/Fission-AI/OpenSpec, https://github.com/Fission-AI/OpenSpec/blob/main/CHANGELOG.md,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


------------------------------------------------------------
# speck-kit update
1. 請依據 https://github.com/github/spec-kit, https://github.com/github/spec-kit/blob/main/spec-driven.md , https://github.com/github/spec-kit#-detailed-process, https://github.com/github/spec-kit/blob/main/docs/upgrade.md ,https://github.com/github/spec-kit/blob/main/CHANGELOG.md ,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-------------------------------------------------------------------
# opencode update
1. 請依據  https://github.com/anomalyco/opencode , https://opencode.ai/docs/zh-tw ,https://github.com/code-yeongyu/oh-my-openagent,https://openwork.software/docs/openwork,https://github.com/different-ai/openwork ,相相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-------------------------------------------------------------------
# claude code update
1. 請依據 
- https://code.claude.com/docs/en/overview, 
- https://code.claude.com/docs/en/how-claude-code-works ,
- https://code.claude.com/docs/en/remote-control,
- https://code.claude.com/docs/en/vs-code,
- https://code.claude.com/docs/en/github-actions,
- https://code.claude.com/docs/en/gitlab-ci-cd,
- https://code.claude.com/docs/en/sub-agents,
- https://code.claude.com/docs/en/agent-teams,
- https://code.claude.com/docs/en/plugins,
- https://code.claude.com/docs/en/discover-plugins.
- https://code.claude.com/docs/en/skills,https://code.claude.com/docs/en/scheduled-tasks,
- https://code.claude.com/docs/en/output-styles,
- https://code.claude.com/docs/en/hooks-guide,
- https://code.claude.com/docs/en/headless,
- https://code.claude.com/docs/en/mcp,
- https://code.claude.com/docs/en/troubleshooting,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-------------------------------------------------------------------
# openclaw update
1. 請依據  https://openclaw.ai/ , https://github.com/openclaw/openclaw ,https://docs.openclaw.ai/ ,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-----------------------------------------------------------------
# OpenAI Codex update
1. 請依據  
- https://developers.openai.com/codex/cli
- https://developers.openai.com/codex
- https://openai.com/zh-Hant/codex/ 

相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆


-----------------------------------------------------------------
# vs code update
1. 請依據 
- https://code.visualstudio.com/docs ,
- https://code.visualstudio.com/updates/v1_111#_agent-scoped-hooks-preview ,
相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
-------------------------------------------------------------------
# SuperClaude Framework 生態系教學手冊  update
1. 請依據 ## 參考:
- https://github.com/SuperClaude-Org/SuperClaude_Framework
- https://www.superclaude.sh/
- https://www.superclaude.sh/docs ,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆
---------------------------------------------------------------

# BMAD-METHOD update
1. 請依據  https://github.com/bmad-code-org/BMAD-METHOD ,相關內容與文章中相關link連接內容,針對本文逐章節,一步一步檢查內容是否最新的,同時是否足夠與完整, 若不足請在增加內容
2. 依本文產出的目錄內容,上網查詢並研究,一步一步檢查內容是否最新的,同時是否內容足夠與完整, 若不足請在增加內容
3. 並以「企業標準技術白皮書」等級撰寫。 
4. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
5. 同時更新目錄與子目錄
6. 請修正md檔格式問題
7. 回覆問題時請用繁體中文
8. 請分段回覆

-----------------------------------------------------------------
# 願望清單
1. Karpathy's method  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
agent memory use karpathy's method in github
2. AutoResearch
3. graphify--->ok
4. GitNexus--> ok
5. hermes-agent --> OK
6. multica -->ok
7. 使用github copilot 建立SSDLC Agent Team sop
8. https://github.com/donnemartin/system-design-primer
9. Awesome DESIGN https://github.com/VoltAgent/awesome-design-md
10. https://github.com/nextlevelbuilder/ui-ux-pro-max-skill





