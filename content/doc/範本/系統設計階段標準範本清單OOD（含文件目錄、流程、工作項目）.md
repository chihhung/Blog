# 系統設計階段標準範本清單OOD（含文件目錄、流程、工作項目）

## 文件目錄 (Deliverables)

1. 系統設計總覽文件 (System Design Specification, SDS)
   - 設計目標與範疇
   - 架構原則與設計考量
   - 系統邊界與外部介面
2. 架構設計文件 (Architecture Design Document, ADD)
   - 系統整體架構圖 (Logical / Physical)
   - 分層架構 (Layered Architecture)
   - 模組/子系統劃分與責任定義
   - 技術棧與設計決策紀錄 (ADR)
3. 資料設計文件 (Data Design Document, DDD)
   - 資料模型 (ERD)
   - 類別圖 (Class Diagram)
   - 資料表設計與正規化說明
   - 交易與一致性設計
4. 物件導向設計文件 (Object-Oriented Design Document)
   - 類別與責任 (CRC 卡片)
   - 類別圖 / 物件圖
   - 繼承、多型設計
   - 設計模式應用
5. 介面設計文件 (Interface Design Specification, IDS)
   - API 設計 (REST/GraphQL)
   - 資料交換格式 (JSON, XML)
    UI/UX Wireframe、螢幕設計稿
6. 流程與行為設計文件 (Behavioral Design Specification)
   - Use Case Realization
   - Sequence Diagram
   - State Diagram
   - Activity Diagram
7. 安全設計文件 (Security Design Document)
   - 認證與授權設計
   - 資料加密與存取控制
   - 威脅模型 (Threat Modeling)
8. 基礎設施與部署設計文件 (Deployment Design)
   - 系統拓撲圖
   - 伺服器/容器配置
   - CI/CD 流程設計

## 系統設計流程 (Workflow, OOD)

1. 輸入：系統分析成果 (SRS, Use Case, 需求模型)

2. 架構設計：確立系統整體架構 (分層、模組、技術棧)

3. 物件設計：
   - 辨識類別與物件
   - 定義屬性與方法
   - 設計關聯 (繼承、組合、依賴)

4. 資料設計：類別模型 → 資料模型 (ERD, Schema)
5. 流程設計：序列圖、活動圖、狀態圖
6. 介面設計：API、UI、外部系統介面
7. 設計模式應用：選擇合適的設計模式 (e.g. Factory, Observer)
8. 非功能性需求設計：效能、安全、可維護性、擴展性
9. 設計評審：進行設計文件審查與驗證
10. 輸出：系統設計規格文件集
## 工作項目清單 (Tasks)
1. 架構面
   - 定義系統架構與技術選型
   - 劃分子系統與模組
   - 撰寫設計決策紀錄 (ADR)
2. 物件導向設計 (OOD)
   - 建立 Class Diagram / Object Diagram
   - 撰寫 CRC 卡片
   - 設計關鍵類別與協作模型
   - 套用設計模式
3. 資料面
   - 設計 ERD 與 Schema
   - 規劃交易一致性策略
   - 建立資料存取設計 (DAO/Repository)
4. 行為面
   - 繪製 Sequence Diagram
   - 設計 State / Activity Diagram
   - 定義 Use Case Realization
5. 介面與整合面
   - 撰寫 API 規格書 (Swagger / OpenAPI)
   - 外部介面協議設計 (MQ, SFTP, WebService)
   - UI Wireframe 設計

6. 品質與安全
   - 撰寫安全設計文件
   - 效能與可用性設計
   - 安排設計審查會議 (Review & Walkthrough)
7. 輸出產物
   - 系統設計規格書 (SDS)
   - 模組設計文件 (MDD)
   - 資料設計文件 (DDD)
   - API / UI 設計文件
   - 部署設計文件

這樣整理後，系統設計階段的 文件、流程、工作項目 就是完整的 範本清單了。