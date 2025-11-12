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
- 對象是剛入職 0–2 年的 PM
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

<https://github.com/github/spec-kit> 請了解本網站的內容

<https://github.com/github/spec-kit/blob/main/spec-driven.md> 這是SDD的方法論

<https://github.com/github/spec-kit?tab=readme-ov-file#-detailed-process> 這是執行步驟

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
- 文件請放在專案的 .github\教學\分析與設計\ 目錄下,檔名為:spec-kit使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

-----------------------------------------------------------------
# BDD(Behavior-Driven Development)行為驅動開發使用教學

## 角色設定
- 你是一位資深系統分析師（Senior System Analyst），專長是使用 Behavior-Driven Development（BDD，行為驅動開發）進行需求分析與系統設計。
- 你目前要帶領新進系統分析師（SA）學習 BDD 的概念、流程與實作方法。
## 背景
- 請根據以下目錄，撰寫一份完整的《BDD行為驅動開發使用教學手冊》。
- 內容需包含章節標題、說明重點、實務示例（含 Gherkin 語法範例）、圖解建議與最佳實務。
- 語言使用繁體中文，教學風格清楚、有層次、可作為企業內訓教材使用。
## 任務說明

手冊章節目錄

第一章　認識 BDD：行為驅動開發的核心理念
- 什麼是 BDD
- BDD 與 TDD、ATDD 的差異
- 為什麼要導入 BDD
- BDD 的價值與應用場景
- BDD 在軟體開發生命週期（SDLC）中的位置

第二章　BDD 的三大支柱
- Discovery（需求探索）
- Formulation（範例定義）
- Automation（自動化驗證）

第三章　BDD 的核心語法：Gherkin
- Gherkin 語法結構與規則
- Feature、Scenario、Scenario Outline
- Given / When / Then 的使用說明
- 範例：從需求敘述轉為 Gherkin 規格
- 常見錯誤與最佳實務

第四章　BDD 與系統分析的整合應用
- 如何將業務需求轉化為可執行行為
- 與利害關係人共創範例（Example Mapping）
- User Story 與 BDD 的結合方式
- Acceptance Criteria（驗收準則）的撰寫指引
- 從 BDD 到 Use Case 的對應關係

第五章　BDD 開發流程與角色分工
- BDD 工作流（Workflow）全貌
- 三方會談（Three Amigos：BA/SA、Dev、QA）
- SA 在 BDD 流程中的責任與產出
- 實務文件產出範例（Feature File、Acceptance Criteria）
- 維護與版本控管實務

第六章　BDD 自動化測試實作
- 常見 BDD 工具比較（Cucumber、Behave、SpecFlow、JBehave）
- 環境安裝與專案結構
- Feature 與 Step Definitions 的關聯
- BDD 自動化與 CI/CD 整合
- 測試報告與追蹤機制

第七章　BDD 實戰案例
- 案例一：登入驗證流程（Web 系統）
- 案例二：銀行轉帳業務流程
- 案例三：批次系統的業務規則驗證
- 案例四：API 行為測試（RESTful 服務）
- 案例回顧與行為重構技巧

第八章　導入策略與組織落地
- 如何在現有開發流程導入 BDD
- 教育訓練與團隊文化轉型
- 導入 BDD 常見阻力與應對方式
- BDD 與敏捷 / DevOps 的結合
- 衡量導入成效的指標（KPI）

第九章　高階應用與延伸
- BDD 與 AI 協作：從自然語言生成行為規格
- BDD 與 Spec-Driven Development（SDD）的結合
- BDD 在大型系統（微服務 / 金融系統）中的挑戰
- 版本演進與回歸測試策略

第十章　附錄
- Gherkin 語法速查表
- BDD 文件模板（Feature 模板、Example Mapping 模板）
- 常見工具與外掛清單
- 推薦閱讀與進階學習資源
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
- 文件請放在專案的 content\doc\教學\分析與設計\ 目錄下,檔名為:BDD行為驅動開發使用教學手冊.md，並使用 Markdown 格式撰寫。
- 請分段回覆

----------------------------------------------------------------
# TDD(Test-Driven Development)測試驅動開發教學手冊使用教學

## 角色設定
- 你是一位資深的系統開發工程師,專長使用TDD(Test-Driven Development)測試驅動開發
## 背景
- 代領新人PG 使用Test-Driven Development 
- 針對新進PG 產出教學手冊
## 任務說明

TDD（Test-Driven Development）測試驅動開發使用教學手冊

目錄

一、前言
1. 教學目的  
2. 適用對象  
3. 預期學習成果  
4. 教學手冊架構說明  

二、TDD 概念與原則
1. 什麼是 TDD（Test-Driven Development）  
2. TDD 的核心循環：Red → Green → Refactor  
3. TDD 與傳統開發流程的差異  
4. 為什麼使用 TDD：好處與挑戰  
5. 單元測試 vs. 集成測試 vs. 系統測試  

三、TDD 實踐步驟
1. Step 1：撰寫失敗的測試（Red）  
2. Step 2：撰寫最簡單的實作通過測試（Green）  
3. Step 3：重構程式碼（Refactor）  
4. Step 4：重複循環與迭代開發  
5. 驗收標準（Definition of Done）與測試覆蓋率要求  

四、TDD 開發環境與工具
1. 測試框架介紹（JUnit、pytest、Mocha、Jest 等）  
2. IDE 與工具設定（IntelliJ、VS Code、Eclipse）  
3. 持續整合（CI）與自動化測試  
4. 測試覆蓋率工具（JaCoCo、Coverage.py 等）  
5. 測試資料與 Mock 工具（Mockito、MockWebServer、Faker 等）  

五、撰寫良好測試的技巧
1. 測試命名規範與可讀性  
2. 安排測試結構（Arrange–Act–Assert 模式）  
3. 單一職責原則（Single Responsibility Principle in Tests）  
4. 使用 Mock、Stub、Fake、Spy 的正確時機  
5. 常見測試陷阱與避免方式  

六、實作範例
1. 範例一：計算機（Calculator）類別的 TDD 實作  
2. 範例二：RESTful API 的 TDD 開發流程  
3. 範例三：資料庫操作（Repository）的 TDD 測試  
4. 範例四：前端元件（React/Vue）TDD 實作示範  
5. 範例五：整合測試與端對端測試  

七、TDD 在團隊開發中的應用
1. TDD 與敏捷開發（Agile、Scrum）的結合  
2. Pair Programming 與 TDD  
3. Code Review 與測試審查重點  
4. 在 CI/CD Pipeline 中整合測試流程  
5. 建立團隊 TDD 實踐文化  

八、TDD 常見問題與最佳實踐
1. 常見誤區與修正方式  
2. 測試覆蓋率與品質間的平衡  
3. 與 Legacy Code 整合的策略  
4. 大型專案中導入 TDD 的建議  
5. 實務經驗分享與成功案例  

九、進階主題
1. BDD（行為驅動開發）與 TDD 的差異與結合  
2. 使用 Property-Based Testing 提升測試覆蓋率  
3. 測試驅動的設計（Test-Driven Design）  
4. 自動化測試報告與品質儀表板  
5. TDD 與 AI 輔助開發的未來展望  

十、附錄
1. 推薦學習資源（書籍、網站、影片）  
2. 常用測試工具與框架清單  
3. TDD 範本專案連結與練習題  
4. 專有名詞中英對照表  

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
- 文件請放在專案的 content\doc\教學\分析與設計\ 目錄下,檔名為:TDD(Test-Driven Development)測試驅動開發教學手冊使用教學.md，並使用 Markdown 格式撰寫。
- 請分段回覆

------------------------------------------------------------------
願望清單
己完成

## 專案管理相關文件

### 專案管理指引

### 專案啟動流程指引

### 專案風險管理指引

### 專案溝通管理指引

### 專案品質管理指引

### 敏捷專案管理指引

### 金融專案合規要求手冊

### 客戶需求訪談與分析技巧

### BDD教學

### TDD教學

未完成

### 「微服務安全性設計指南」

### 「微服務監控與運維手冊」

### 「微服務實戰案例集」



### Apache Karaf教學

### sping boot 3 and spring framework 6 升級至 spring boot 4 and spring framework 7

### spring security 教學

### spring batch  教學

### spring webflux

### java function programming

### java streamming

### jdk 1.8 至jdk 25 升級特性 教學

------------------------------------------------------------------------------

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


------------------------------------------------------------------------------

1. 請針對本文逐章節,一步一步檢查內容是否足夠完整
2. 目錄和內容是否一致, 都有被生成, 若沒有請在生成
3. 同時更新目錄與子目錄
4. 請修正md檔格式問題

------------------------------------------------------------
# BDD(Behavior-Driven Development)行為驅動開發使用教學

## 角色設定
- 你是一位資深的系統分析師,專長使用（Behavior-Driven Development）行為驅動開發,
## 背景
- 代領新新SA 使用Behavior-Driven Development
- 針對新進SA 產出教學手冊
## 任務
- 請出教學手冊目錄內容,使用md 格式
-----------------------------------------------------------

hugo new "posts/教學/分析與設計/TDD(Test-Driven Development)測試驅動開發教學手冊使用教學.md"