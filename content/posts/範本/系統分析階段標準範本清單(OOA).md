+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = '系統分析階段標準範本清單(OOA)'
tags = ['範本']
categories = ['範本']
+++
1️⃣ 需求規格文件 (SRS – Software Requirement Specification)

目錄：

01_SRS/
├── 01_前言.md                  # 文件目的、系統範疇、名詞定義
├── 02_整體描述.md              # 系統目標、利害關係人、作業環境、限制
├── 03_功能性需求.md            # 按模組/使用案例列需求
├── 04_非功能性需求.md          # 效能、安全性、可用性、法規
├── 05_系統介面需求.md          # 外部系統介接、API、資料交換
└── 附錄_參考資料.md

2️⃣ 使用案例文件 (Use Case Specification)

目錄：

02_Use_Case/
├── 00_使用案例總覽圖.png
├── UC01_名稱_說明.md           # 前置條件、後置條件、主要/替代流程
├── UC02_名稱_說明.md
├── UCxx_...md
├── 使用案例活動圖/
│   ├── UC01_活動圖.png
│   └── UC02_活動圖.png
└── 使用案例需求對應表.xlsx

3️⃣ 系統模型文件 (UML Models)

目錄：

03_System_Model/
├── Object_Model/               # 物件模型
│   ├── 類別圖_ClassDiagram.png
│   └── 物件圖_ObjectDiagram.png
├── Interaction_Model/          # 互動模型
│   ├── UC01_序列圖.png
│   ├── UC02_序列圖.png
│   └── 通訊圖_Communication.png
├── State_Model/                # 狀態模型
│   ├── ClassA_狀態圖.png
│   └── ClassB_狀態圖.png
└── Supplementary_Model/        # 補充模型
    ├── 組件圖_Component.png
    └── 部署圖_Deployment.png

4️⃣ 資料模型文件 (Data Model Specification)

目錄：

04_Data_Model/
├── ER_Model.png
├── Class_Table_Mapping.xlsx    # 類別 ↔ 資料表對應
└── Data_Dictionary.xlsx

5️⃣ 需求追蹤矩陣 (RTM – Requirement Traceability Matrix)

目錄：

05_RTM/
└── Requirement_Traceability_Matrix.xlsx

6️⃣ 驗證與審查文件 (Validation & Review)

目錄：

06_Validation_Review/
├── 需求審查會議紀錄.md
├── 問題清單與解決狀態.xlsx
└── 需求基線確認_Baseline_Approval.pdf

7️⃣ 文件總覽 (README)

目錄：

README.md      # 系統分析階段產出物說明與目錄導引

✅ 總結

物件導向方法論下的系統分析階段交付物：

1. 需求規格書 (SRS)
2. 使用案例文件 (Use Case Diagram + Specification + Activity Diagram)
3. 系統模型 (UML – 類別圖、序列圖、狀態圖、組件圖)
4. 資料模型 (ERD + 資料字典 + 類別/資料表對應)
5. 需求追蹤矩陣 (RTM)
6. 驗證與審查文件 (會議紀錄、問題清單、需求基線)

這份清單 既符合物件導向分析 (OOA) 的精神，又有完整的交付文件目錄，能支援大型專案