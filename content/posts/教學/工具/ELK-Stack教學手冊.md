+++
date = '2026-01-29T19:09:08+08:00'
draft = false
title = 'ELK Stack教學手冊'
tags = ['教學', '工具', 'Visualization','ELK stack']
categories = ['教學']
+++

# Logstash / Elasticsearch / Kibana（ELK Stack）教學手冊

## 文件資訊

| 項目 | 內容 |
| --- | --- |
| **文件版本** | 2.0 |
| **最後更新** | 2026-10-01 |
| **版本基準** | Elastic Stack 9.5.4（2026-09-15 發佈）：Elasticsearch／Logstash／Kibana／Filebeat 同版；相容說明涵蓋 8.19.x（支援至 2027-07-15） |
| **文件定位** | 企業標準技術白皮書／內部標準教材 |
| **適用對象** | 資深軟體工程師、系統架構師、SRE／DevOps 工程師、資安與稽核人員 |
| **前置知識** | Linux 基礎、Java／Spring Boot 應用程式、基本網路與 TLS 概念 |
| **使用情境** | 企業級 Logs Visualization 平台（與 Prometheus／Grafana 並存的 Observability 架構） |
| **前一版本** | 1.0（2026-01-29，以 Elastic Stack 8.12 為基準） |
| **Created by** | Eric Cheng |

> 📌 **v2.0 改版重點**：全面對齊 Elastic Stack 9.5；修正 v1.0 中已移除、已失效或錯誤的設定（`_flush/synced`、`yum downgrade`、Filebeat `type: log`、Logstash `ssl => false`、`elasticsearch.yml` 內的 index 層級設定、Kibana `i18n.locale: "zh-TW"`、ILM `freeze` 等）；改以 Data Stream、ECS、API Key 與 TLS 為預設做法；新增授權層級、容量規劃、Data Tiers、ES|QL、Alerting、Streams、Snapshot／SLM、OpenTelemetry（EDOT）、Kubernetes（ECK）、故障排除手冊與 9.x 版本演進等章節。完整差異見 [附錄 D 版本紀錄](#附錄-d版本紀錄)，查證依據見 [附錄 E 查證紀錄](#附錄-e查證紀錄)。

### 閱讀指引

| 讀者角色 | 建議閱讀章節 |
| --- | --- |
| 初次接觸 ELK | 第一章 → 第二章 2.1–2.3 → 第三章 3.7 → 第五章 → 第六章 |
| 應用程式開發人員 | 第五章 5.3、5.5 → 第六章 → 第十章 10.2 |
| 架構師 | 第一章 1.5–1.6 → 第二章 → 第十章 → 第十一章 → 第十二章 |
| SRE／DevOps | 第三章 → 第四章 → 第七章 → 第八章 → 第十三章 |
| 資安／稽核人員 | 第一章 1.5 → 第九章 → 附錄 A.6 |
| 技術主管／決策者 | 第一章 → 第二章 2.5–2.7 → 第十章 10.5 → 第十四章 |

### 本文慣例

| 標記 | 意義 |
| --- | --- |
| `> 🆕 **v2.0 新增**` | 本版新增的章節或內容 |
| `> ⚠️ **v2.0 更正**` | 修正 v1.0 錯誤或已過時的內容 |
| `> 📌 **8.19 差異**` | 仍在 8.19.x 的環境需注意的不同之處 |
| `> ⚠️ **實務注意**` | 容易出錯、需特別留意之處 |
| `> 💰 **授權**` | 該功能需要付費訂閱（Platinum／Enterprise）才能使用 |
| GA／Technical Preview／Beta | 依 Elastic 官方功能成熟度分類；Technical Preview 與 Beta 功能**不建議**直接用於正式環境 |
| `https://localhost:9200` | 9.x 預設啟用 TLS；範例中的 `--cacert`、`-u`、API Key 請依實際環境替換 |

## 目錄

<!-- TOC-AUTO-BEGIN -->

- [文件資訊](#文件資訊)
  - [閱讀指引](#閱讀指引)
  - [本文慣例](#本文慣例)
- [第一章：Logs Visualization 與 ELK Stack 概述](#第一章logs-visualization-與-elk-stack-概述)
  - [1.1 為什麼需要 Logs Visualization](#11-為什麼需要-logs-visualization)
    - [1.1.1 傳統 Log 管理的痛點](#111-傳統-log-管理的痛點)
    - [1.1.2 Logs Visualization 帶來的價值](#112-logs-visualization-帶來的價值)
    - [1.1.3 實務案例](#113-實務案例)
  - [1.2 Logs、Metrics 與 Traces 的差異與互補](#12-logsmetrics-與-traces-的差異與互補)
    - [1.2.1 對比表](#121-對比表)
    - [1.2.2 互補使用流程](#122-互補使用流程)
  - [1.3 ELK Stack 架構總覽](#13-elk-stack-架構總覽)
    - [1.3.1 元件簡介](#131-元件簡介)
    - [1.3.2 從 ELK 到 Elastic Stack 的演進](#132-從-elk-到-elastic-stack-的演進)
  - [1.4 ELK 在 Observability 架構中的角色](#14-elk-在-observability-架構中的角色)
    - [1.4.1 Observability 分層職責](#141-observability-分層職責)
  - [1.5 授權模式與功能層級](#15-授權模式與功能層級)
    - [1.5.1 授權沿革](#151-授權沿革)
    - [1.5.2 Basic（免費）與付費功能對照](#152-basic免費與付費功能對照)
    - [1.5.3 與 OpenSearch 的差異](#153-與-opensearch-的差異)
  - [1.6 版本發佈節奏與支援策略](#16-版本發佈節奏與支援策略)
  - [1.7 與 AI 輔助開發的關係](#17-與-ai-輔助開發的關係)
    - [1.7.1 AI 輔助場景](#171-ai-輔助場景)
    - [1.7.2 實務應用範例](#172-實務應用範例)
  - [1.8 💡 本章實務建議](#18--本章實務建議)
- [第二章：系統整體架構設計](#第二章系統整體架構設計)
  - [2.1 ELK Stack 架構圖](#21-elk-stack-架構圖)
    - [2.1.1 基礎架構（小型環境）](#211-基礎架構小型環境)
    - [2.1.2 企業級架構（大型環境）](#212-企業級架構大型環境)
  - [2.2 各元件角色說明](#22-各元件角色說明)
    - [2.2.1 Logstash：資料處理引擎](#221-logstash資料處理引擎)
    - [2.2.2 Elasticsearch：分散式搜尋引擎](#222-elasticsearch分散式搜尋引擎)
    - [2.2.3 Kibana：視覺化與管理平台](#223-kibana視覺化與管理平台)
    - [2.2.4 Filebeat 與 Elastic Agent](#224-filebeat-與-elastic-agent)
  - [2.3 單節點 vs 多節點架構](#23-單節點-vs-多節點架構)
    - [2.3.1 架構選擇決策表](#231-架構選擇決策表)
    - [2.3.2 節點角色說明](#232-節點角色說明)
  - [2.4 Data Tiers 與資料溫度](#24-data-tiers-與資料溫度)
  - [2.5 容量規劃與 Sizing](#25-容量規劃與-sizing)
    - [2.5.1 儲存容量估算公式](#251-儲存容量估算公式)
    - [2.5.2 估算範例](#252-估算範例)
    - [2.5.3 Shard 與節點數估算](#253-shard-與節點數估算)
  - [2.6 Production 建議架構](#26-production-建議架構)
    - [2.6.1 中型企業建議架構（日誌量 50–200 GB／天）](#261-中型企業建議架構日誌量-50200-gb天)
    - [2.6.2 硬體規格建議](#262-硬體規格建議)
    - [2.6.3 關鍵設計原則](#263-關鍵設計原則)
  - [2.7 高可用與災難備援](#27-高可用與災難備援)
    - [2.7.1 叢集內高可用](#271-叢集內高可用)
    - [2.7.2 跨機房災難備援](#272-跨機房災難備援)
  - [2.8 與 Prometheus／Grafana 並存架構](#28-與-prometheusgrafana-並存架構)
    - [2.8.1 整合策略](#281-整合策略)
    - [2.8.2 Grafana 連結 Kibana 範例](#282-grafana-連結-kibana-範例)
  - [2.9 💡 本章實務建議](#29--本章實務建議)
- [第三章：系統安裝](#第三章系統安裝)
  - [3.1 環境需求總覽](#31-環境需求總覽)
    - [3.1.1 作業系統支援](#311-作業系統支援)
    - [3.1.2 版本選擇原則](#312-版本選擇原則)
    - [3.1.3 硬體需求（單節點最低配置）](#313-硬體需求單節點最低配置)
    - [3.1.4 網路埠需求](#314-網路埠需求)
  - [3.2 系統前置調校](#32-系統前置調校)
  - [3.3 Elasticsearch 安裝](#33-elasticsearch-安裝)
    - [3.3.1 RPM 安裝（RHEL 系列）](#331-rpm-安裝rhel-系列)
    - [3.3.2 DEB 安裝（Ubuntu／Debian）](#332-deb-安裝ubuntudebian)
    - [3.3.3 自動安全設定（Security Auto-configuration）](#333-自動安全設定security-auto-configuration)
    - [3.3.4 加入其他節點（Enrollment Token）](#334-加入其他節點enrollment-token)
    - [3.3.5 Docker 快速安裝（單節點、啟用安全性）](#335-docker-快速安裝單節點啟用安全性)
    - [3.3.6 安裝後驗證](#336-安裝後驗證)
  - [3.4 Kibana 安裝](#34-kibana-安裝)
    - [3.4.1 套件安裝](#341-套件安裝)
    - [3.4.2 以 Enrollment Token 連線 Elasticsearch](#342-以-enrollment-token-連線-elasticsearch)
    - [3.4.3 設定加密金鑰](#343-設定加密金鑰)
    - [3.4.4 安裝驗證](#344-安裝驗證)
  - [3.5 Logstash 安裝](#35-logstash-安裝)
    - [3.5.1 套件安裝](#351-套件安裝)
    - [3.5.2 建立寫入用的角色與 API Key](#352-建立寫入用的角色與-api-key)
    - [3.5.3 建立基本 Pipeline 並測試](#353-建立基本-pipeline-並測試)
    - [3.5.4 Docker 安裝](#354-docker-安裝)
    - [3.5.5 安裝驗證](#355-安裝驗證)
  - [3.6 Filebeat 安裝](#36-filebeat-安裝)
  - [3.7 Docker Compose 開發環境](#37-docker-compose-開發環境)
  - [3.8 常見安裝問題排除](#38-常見安裝問題排除)
    - [3.8.1 問題一：Elasticsearch 無法啟動](#381-問題一elasticsearch-無法啟動)
    - [3.8.2 問題二：Logstash Pipeline 錯誤](#382-問題二logstash-pipeline-錯誤)
    - [3.8.3 問題三：Kibana 無法連線 Elasticsearch](#383-問題三kibana-無法連線-elasticsearch)
    - [3.8.4 問題四：磁碟空間不足](#384-問題四磁碟空間不足)
    - [3.8.5 快速診斷腳本](#385-快速診斷腳本)
  - [3.9 💡 本章實務建議](#39--本章實務建議)
- [第四章：系統設定](#第四章系統設定)
  - [4.1 Elasticsearch 設定](#41-elasticsearch-設定)
    - [4.1.1 設定檔位置與設定層級](#411-設定檔位置與設定層級)
    - [4.1.2 elasticsearch.yml 範例（多節點）](#412-elasticsearchyml-範例多節點)
    - [4.1.3 JVM Heap 設定](#413-jvm-heap-設定)
    - [4.1.4 Index Template 與 Component Template](#414-index-template-與-component-template)
    - [4.1.5 Shard 數量規劃](#415-shard-數量規劃)
    - [4.1.6 Ingest Pipeline](#416-ingest-pipeline)
  - [4.2 Logstash 設定](#42-logstash-設定)
    - [4.2.1 設定檔結構](#421-設定檔結構)
    - [4.2.2 logstash.yml 重要設定](#422-logstashyml-重要設定)
    - [4.2.3 pipelines.yml 與多 Pipeline](#423-pipelinesyml-與多-pipeline)
    - [4.2.4 Input 設定範例](#424-input-設定範例)
    - [4.2.5 Filter 設定範例](#425-filter-設定範例)
    - [4.2.6 Output 設定範例](#426-output-設定範例)
    - [4.2.7 Persistent Queue 與 Dead Letter Queue](#427-persistent-queue-與-dead-letter-queue)
    - [4.2.8 以 Keystore 管理機密](#428-以-keystore-管理機密)
    - [4.2.9 完整 Java 應用程式 Log Pipeline](#429-完整-java-應用程式-log-pipeline)
  - [4.3 Kibana 設定](#43-kibana-設定)
    - [4.3.1 主設定檔](#431-主設定檔)
    - [4.3.2 Data View 設定](#432-data-view-設定)
    - [4.3.3 Spaces 與團隊隔離](#433-spaces-與團隊隔離)
    - [4.3.4 Advanced Settings](#434-advanced-settings)
  - [4.4 💡 本章實務建議](#44--本章實務建議)
- [第五章：三者如何串接](#第五章三者如何串接)
  - [5.1 End-to-End 資料流](#51-end-to-end-資料流)
  - [5.2 收集端選型](#52-收集端選型)
  - [5.3 實際串接範例：Spring Boot 應用程式](#53-實際串接範例spring-boot-應用程式)
    - [5.3.1 步驟 1：應用程式 Log 設定](#531-步驟-1應用程式-log-設定)
    - [5.3.2 步驟 2：Filebeat filestream 設定](#532-步驟-2filebeat-filestream-設定)
    - [5.3.3 步驟 3：Logstash Pipeline 設定](#533-步驟-3logstash-pipeline-設定)
    - [5.3.4 步驟 4：驗證資料流](#534-步驟-4驗證資料流)
  - [5.4 Filebeat 進階整合](#54-filebeat-進階整合)
    - [5.4.1 Filebeat vs Logstash 比較](#541-filebeat-vs-logstash-比較)
    - [5.4.2 推薦架構](#542-推薦架構)
    - [5.4.3 Filebeat Module 使用](#543-filebeat-module-使用)
    - [5.4.4 從 log input 遷移至 filestream](#544-從-log-input-遷移至-filestream)
    - [5.4.5 Filebeat 直送 Elasticsearch](#545-filebeat-直送-elasticsearch)
  - [5.5 ECS 與欄位命名規範](#55-ecs-與欄位命名規範)
  - [5.6 Elastic Agent 與 Fleet](#56-elastic-agent-與-fleet)
  - [5.7 💡 本章實務建議](#57--本章實務建議)
- [第六章：系統使用](#第六章系統使用)
  - [6.1 Kibana 操作教學](#61-kibana-操作教學)
    - [6.1.1 Discover：Log 查詢](#611-discoverlog-查詢)
    - [6.1.2 Dashboard 與 Lens](#612-dashboard-與-lens)
    - [6.1.3 分享與匯出](#613-分享與匯出)
  - [6.2 查詢語法詳解](#62-查詢語法詳解)
    - [6.2.1 KQL（Kibana Query Language）](#621-kqlkibana-query-language)
    - [6.2.2 Lucene Query Syntax（進階）](#622-lucene-query-syntax進階)
    - [6.2.3 ES|QL（Elasticsearch Query Language）](#623-esqlelasticsearch-query-language)
    - [6.2.4 實用查詢範例](#624-實用查詢範例)
  - [6.3 告警（Alerting）](#63-告警alerting)
    - [6.3.1 Log 相關的規則類型](#631-log-相關的規則類型)
    - [6.3.2 Connector 與授權](#632-connector-與授權)
    - [6.3.3 建立 Log 告警規則（UI）](#633-建立-log-告警規則ui)
    - [6.3.4 告警設計原則](#634-告警設計原則)
  - [6.4 Streams 與 Log 解析](#64-streams-與-log-解析)
  - [6.5 實務使用情境](#65-實務使用情境)
    - [6.5.1 情境一：問題追蹤](#651-情境一問題追蹤)
    - [6.5.2 情境二：錯誤分析](#652-情境二錯誤分析)
    - [6.5.3 情境三：系統行為回溯（稽核）](#653-情境三系統行為回溯稽核)
    - [6.5.4 情境四：與 Grafana Metrics 搭配分析](#654-情境四與-grafana-metrics-搭配分析)
  - [6.6 💡 本章實務建議](#66--本章實務建議)
- [第七章：系統維護](#第七章系統維護)
  - [7.1 Data Stream 與 Index 管理](#71-data-stream-與-index-管理)
    - [7.1.1 Data Stream 基本操作](#711-data-stream-基本操作)
    - [7.1.2 Index Lifecycle Management（ILM）](#712-index-lifecycle-managementilm)
    - [7.1.3 Data Stream Lifecycle（DSL）](#713-data-stream-lifecycledsl)
    - [7.1.4 LogsDB 索引模式](#714-logsdb-索引模式)
    - [7.1.5 手動清理](#715-手動清理)
  - [7.2 Snapshot 與 SLM](#72-snapshot-與-slm)
    - [7.2.1 建立 Snapshot Repository](#721-建立-snapshot-repository)
    - [7.2.2 Snapshot Lifecycle Management（SLM）](#722-snapshot-lifecycle-managementslm)
    - [7.2.3 還原與演練](#723-還原與演練)
  - [7.3 效能調校](#73-效能調校)
    - [7.3.1 寫入效能調校](#731-寫入效能調校)
    - [7.3.2 查詢效能調校](#732-查詢效能調校)
    - [7.3.3 Logstash 效能調校](#733-logstash-效能調校)
  - [7.4 健康檢查與監控](#74-健康檢查與監控)
    - [7.4.1 Elasticsearch 健康檢查](#741-elasticsearch-健康檢查)
    - [7.4.2 監控指標清單](#742-監控指標清單)
    - [7.4.3 Stack Monitoring](#743-stack-monitoring)
    - [7.4.4 整合 Prometheus 監控](#744-整合-prometheus-監控)
  - [7.5 日常維運作業](#75-日常維運作業)
  - [7.6 💡 本章實務建議](#76--本章實務建議)
- [第八章：系統升級](#第八章系統升級)
  - [8.1 版本策略與升級路徑](#81-版本策略與升級路徑)
  - [8.2 升級前準備](#82-升級前準備)
    - [8.2.1 升級檢查清單](#821-升級檢查清單)
    - [8.2.2 Upgrade Assistant](#822-upgrade-assistant)
    - [8.2.3 處理 7.x 建立的索引](#823-處理-7x-建立的索引)
    - [8.2.4 備份策略](#824-備份策略)
  - [8.3 各元件升級流程](#83-各元件升級流程)
    - [8.3.1 升級順序](#831-升級順序)
    - [8.3.2 Elasticsearch Rolling Upgrade](#832-elasticsearch-rolling-upgrade)
    - [8.3.3 Kibana 升級](#833-kibana-升級)
    - [8.3.4 Logstash 升級](#834-logstash-升級)
    - [8.3.5 Beats 與 Elastic Agent 升級](#835-beats-與-elastic-agent-升級)
  - [8.4 8.19 → 9.x 重大變更對照](#84-819--9x-重大變更對照)
  - [8.5 回復策略](#85-回復策略)
    - [8.5.1 Elasticsearch 回復方式](#851-elasticsearch-回復方式)
    - [8.5.2 其他元件回復](#852-其他元件回復)
  - [8.6 💡 本章實務建議](#86--本章實務建議)
- [第九章：安全性與權限管理](#第九章安全性與權限管理)
  - [9.1 Security 基本概念](#91-security-基本概念)
    - [9.1.1 Elastic Security 架構](#911-elastic-security-架構)
    - [9.1.2 9.x 預設的安全狀態](#912-9x-預設的安全狀態)
    - [9.1.3 TLS 憑證規劃](#913-tls-憑證規劃)
    - [9.1.4 憑證到期管理與輪替](#914-憑證到期管理與輪替)
  - [9.2 身分驗證](#92-身分驗證)
  - [9.3 使用者與角色管理](#93-使用者與角色管理)
    - [9.3.1 內建角色](#931-內建角色)
    - [9.3.2 建立自訂角色](#932-建立自訂角色)
    - [9.3.3 實務角色設計](#933-實務角色設計)
    - [9.3.4 收集端最小權限](#934-收集端最小權限)
  - [9.4 企業資安考量](#94-企業資安考量)
    - [9.4.1 敏感資料處理](#941-敏感資料處理)
    - [9.4.2 稽核日誌](#942-稽核日誌)
    - [9.4.3 網路安全建議](#943-網路安全建議)
    - [9.4.4 法規與內控對照](#944-法規與內控對照)
  - [9.5 💡 本章實務建議](#95--本章實務建議)
- [第十章：最佳實務與導入建議](#第十章最佳實務與導入建議)
  - [10.1 導入常見踩雷點](#101-導入常見踩雷點)
  - [10.2 結構化 Log 設計原則](#102-結構化-log-設計原則)
    - [10.2.1 推薦的 Log 格式（ECS JSON）](#1021-推薦的-log-格式ecs-json)
    - [10.2.2 Log 設計原則](#1022-log-設計原則)
  - [10.3 與 AI 分析結合](#103-與-ai-分析結合)
    - [10.3.1 AI 輔助查詢範例](#1031-ai-輔助查詢範例)
    - [10.3.2 將 Log 作為 AI Prompt 輸入](#1032-將-log-作為-ai-prompt-輸入)
    - [10.3.3 Elastic 內建 AI 功能與治理](#1033-elastic-內建-ai-功能與治理)
  - [10.4 與 Prometheus／Grafana 分工](#104-與-prometheusgrafana-分工)
    - [10.4.1 分工建議](#1041-分工建議)
  - [10.5 導入路線圖](#105-導入路線圖)
  - [10.6 💡 本章實務建議](#106--本章實務建議)
- [第十一章：OpenTelemetry 與 EDOT 整合](#第十一章opentelemetry-與-edot-整合)
  - [11.1 為什麼要導入 OpenTelemetry](#111-為什麼要導入-opentelemetry)
  - [11.2 EDOT 元件](#112-edot-元件)
  - [11.3 以 EDOT Collector 收集 Log 檔](#113-以-edot-collector-收集-log-檔)
  - [11.4 Mapping 模式：otel 與 ecs](#114-mapping-模式otel-與-ecs)
  - [11.5 Wired Streams 端點](#115-wired-streams-端點)
  - [11.6 選型：Filebeat 與 EDOT Collector](#116-選型filebeat-與-edot-collector)
  - [11.7 💡 本章實務建議](#117--本章實務建議)
- [第十二章：Kubernetes 部署（ECK）](#第十二章kubernetes-部署eck)
  - [12.1 ECK 概述與相容性](#121-eck-概述與相容性)
  - [12.2 安裝 ECK Operator](#122-安裝-eck-operator)
  - [12.3 部署 Elasticsearch 與 Kibana](#123-部署-elasticsearch-與-kibana)
  - [12.4 Kubernetes Log 收集](#124-kubernetes-log-收集)
  - [12.5 資源、儲存與排程建議](#125-資源儲存與排程建議)
  - [12.6 升級與維運](#126-升級與維運)
  - [12.7 💡 本章實務建議](#127--本章實務建議)
- [第十三章：故障排除與營運手冊](#第十三章故障排除與營運手冊)
  - [13.1 排查總流程](#131-排查總流程)
  - [13.2 叢集 Red／Yellow](#132-叢集-redyellow)
  - [13.3 磁碟水位與唯讀索引](#133-磁碟水位與唯讀索引)
  - [13.4 JVM 記憶體與 Circuit Breaker](#134-jvm-記憶體與-circuit-breaker)
  - [13.5 寫入被拒（429）](#135-寫入被拒429)
  - [13.6 Logstash 背壓與管線阻塞](#136-logstash-背壓與管線阻塞)
  - [13.7 Filebeat 不收或重複收](#137-filebeat-不收或重複收)
  - [13.8 Kibana 異常](#138-kibana-異常)
  - [13.9 Mapping 爆量與欄位衝突](#139-mapping-爆量與欄位衝突)
  - [13.10 💡 本章實務建議](#1310--本章實務建議)
- [第十四章：版本演進與新功能（9.0→9.5）](#第十四章版本演進與新功能9095)
  - [14.1 9.x 版本時間軸](#141-9x-版本時間軸)
  - [14.2 各版本重點（與 Log 平台相關）](#142-各版本重點與-log-平台相關)
  - [14.3 對 Log 平台的影響評估](#143-對-log-平台的影響評估)
  - [14.4 💡 本章實務建議](#144--本章實務建議)
- [附錄 A：檢查清單](#附錄-a檢查清單)
  - [A.1 安裝檢查清單](#a1-安裝檢查清單)
  - [A.2 設定檢查清單](#a2-設定檢查清單)
  - [A.3 上線檢查清單](#a3-上線檢查清單)
  - [A.4 維運檢查清單](#a4-維運檢查清單)
  - [A.5 升級檢查清單](#a5-升級檢查清單)
  - [A.6 安全檢查清單](#a6-安全檢查清單)
- [附錄 B：常見 Q&A](#附錄-b常見-qa)
  - [B.1 Q1：忘記 elastic 密碼怎麼辦？](#b1-q1忘記-elastic-密碼怎麼辦)
  - [B.2 Q2：單節點叢集為什麼一直是 yellow？](#b2-q2單節點叢集為什麼一直是-yellow)
  - [B.3 Q3：Log 已經寫進去，但 Discover 查不到？](#b3-q3log-已經寫進去但-discover-查不到)
  - [B.4 Q4：如何讓保存期限依服務不同？](#b4-q4如何讓保存期限依服務不同)
  - [B.5 Q5：可以不用 Logstash 嗎？](#b5-q5可以不用-logstash-嗎)
  - [B.6 Q6：Basic 授權能不能發送告警到 Teams？](#b6-q6basic-授權能不能發送告警到-teams)
  - [B.7 Q7：Kibana 可以顯示繁體中文嗎？](#b7-q7kibana-可以顯示繁體中文嗎)
  - [B.8 Q8：從 8.x 升到 9.x，Filebeat 要注意什麼？](#b8-q8從-8x-升到-9xfilebeat-要注意什麼)
  - [B.9 Q9：升級後發現問題，可以降版嗎？](#b9-q9升級後發現問題可以降版嗎)
  - [B.10 Q10：ELK 和 OpenSearch 可以混用嗎？](#b10-q10elk-和-opensearch-可以混用嗎)
- [附錄 C：指令與 API 速查](#附錄-c指令與-api-速查)
  - [C.1 Elasticsearch](#c1-elasticsearch)
  - [C.2 Logstash](#c2-logstash)
  - [C.3 Kibana](#c3-kibana)
  - [C.4 Filebeat 與 Elastic Agent](#c4-filebeat-與-elastic-agent)
- [附錄 D：版本紀錄](#附錄-d版本紀錄)
  - [D.1 版本歷程](#d1-版本歷程)
  - [D.2 v1.0 → v2.0 更正表](#d2-v10--v20-更正表)
  - [D.3 v2.0 新增章節](#d3-v20-新增章節)
- [附錄 E：查證紀錄](#附錄-e查證紀錄)
  - [E.1 待確認事項](#e1-待確認事項)
- [附錄 F：參考資料](#附錄-f參考資料)
  - [F.1 Elastic 官方文件（9.x）](#f1-elastic-官方文件9x)
  - [F.2 版本、支援與授權](#f2-版本支援與授權)
  - [F.3 舊版文件（8.x，供 8.19 環境參考）](#f3-舊版文件8x供-819-環境參考)
  - [F.4 原始碼與社群資源](#f4-原始碼與社群資源)

<!-- TOC-AUTO-END -->

---

## 第一章：Logs Visualization 與 ELK Stack 概述

### 1.1 為什麼需要 Logs Visualization

在現代企業級系統中，Log 是系統運行的「黑盒子記錄器」，記錄了系統每一個關鍵時刻的狀態與行為。當系統從單體走向微服務、從實體機走向容器與雲端，Log 的數量、來源與格式都呈倍數成長，集中化的 Log 平台已是維運、資安與稽核的基礎建設。

#### 1.1.1 傳統 Log 管理的痛點

| 痛點 | 說明 | 對企業的影響 |
| --- | --- | --- |
| **分散儲存** | Log 散落在各台伺服器、容器與雲端服務 | 事故時需逐台登入，MTTR 拉長 |
| **格式不一** | 各系統 Log 格式、時區、欄位名稱不統一 | 無法跨系統關聯分析 |
| **查詢困難** | 只能用 `grep`、`tail` 等指令 | 無法聚合、統計與視覺化 |
| **無法關聯** | 缺乏 Trace ID 等關聯鍵 | 跨服務問題難以定位根因 |
| **保存期限** | 磁碟有限、容器重啟即遺失 | 無法滿足稽核與法規保存要求 |
| **存取控管** | 直接登入主機看 Log | 權限過大、無存取紀錄，違反最小權限原則 |

#### 1.1.2 Logs Visualization 帶來的價值

```text
┌─────────────────────────────────────────────────────────────┐
│                    Logs Visualization 價值                   │
├─────────────────────────────────────────────────────────────┤
│  ✅ 集中管理：所有 Log 統一收集、儲存、查詢                    │
│  ✅ 快速搜尋：秒級查詢 TB 級 Log 資料                         │
│  ✅ 視覺化分析：Dashboard 呈現趨勢與異常                      │
│  ✅ 即時告警：異常 Log Pattern 自動通知                       │
│  ✅ 歷史回溯：依保存政策完整保存，支援稽核與事故分析           │
│  ✅ 存取治理：以角色控管誰能看哪些 Log，並留下稽核紀錄         │
└─────────────────────────────────────────────────────────────┘
```

#### 1.1.3 實務案例

> **情境**：某銀行核心系統發生交易失敗，需在 5 分鐘內定位問題。
>
> - **沒有 ELK**：需登入 10+ 台伺服器，逐一 grep Log，耗時 30 分鐘以上
> - **有 ELK**：在 Kibana 輸入 Transaction ID 或 `trace.id`，數秒內找到完整交易鏈路

---

### 1.2 Logs、Metrics 與 Traces 的差異與互補

組織已導入 Prometheus + Grafana 作為 Metrics 平台，ELK 與其為互補關係；若再加上分散式追蹤（Traces），即構成 Observability 的三大支柱。

```mermaid
graph TB
    subgraph "Observability 三大支柱"
        M[Metrics<br/>Prometheus + Grafana]
        L[Logs<br/>ELK Stack]
        T[Traces<br/>Jaeger / Elastic APM / Tempo]
    end

    M -->|"數值趨勢<br/>告警觸發"| Alert[發現問題]
    Alert -->|"深入分析"| L
    L -->|"以 trace.id 追蹤請求鏈路"| T

    style M fill:#e1f5fe
    style L fill:#fff3e0
    style T fill:#f3e5f5
```

#### 1.2.1 對比表

| 面向 | Metrics（Prometheus） | Logs（ELK） | Traces |
| --- | --- | --- | --- |
| **資料類型** | 數值型（Counter、Gauge、Histogram） | 文字型事件（訊息、堆疊、業務欄位） | Span 樹狀結構 |
| **用途** | 趨勢監控、告警、容量規劃 | 問題排查、稽核、行為分析 | 跨服務延遲與呼叫鏈路分析 |
| **查詢方式** | PromQL | KQL／Lucene／ES\|QL | Trace ID 檢索、服務地圖 |
| **資料量** | 相對小（已聚合） | 相對大（完整內容） | 中等（常需取樣） |
| **保存週期** | 通常 15–90 天 | 依法規 30 天至數年 | 通常 7–30 天 |
| **典型問題** | 「CPU 何時飆高？」 | 「CPU 飆高時發生什麼事？」 | 「哪個下游服務拖慢請求？」 |

#### 1.2.2 互補使用流程

```mermaid
sequenceDiagram
    participant G as Grafana
    participant P as Prometheus
    participant K as Kibana
    participant E as Elasticsearch

    rect rgb(225, 245, 254)
        G->>P: 1. Dashboard 顯示錯誤率上升
        P->>G: 2. Alert 觸發通知
    end
    rect rgb(255, 243, 224)
        G->>K: 3. 點擊 Data Link 跳轉 Kibana
        K->>E: 4. 查詢同時段 Error Log
        E->>K: 5. 返回詳細錯誤堆疊
        K->>K: 6. 定位根因
    end
```

---

### 1.3 ELK Stack 架構總覽

ELK Stack 由三個核心元件組成，實務上再加上輕量收集器（Beats 或 Elastic Agent），因此 Elastic 官方自 5.0 起改稱 **Elastic Stack**。

```mermaid
graph LR
    subgraph "資料來源"
        A1[Application Log]
        A2[System Log]
        A3[Access Log]
    end

    subgraph "收集層"
        B[Filebeat / Elastic Agent<br/>/ OTel Collector]
    end

    subgraph "ELK Stack"
        L[Logstash<br/>收集 & 處理]
        E[Elasticsearch<br/>儲存 & 索引]
        K[Kibana<br/>視覺化 & 查詢]
    end

    A1 --> B
    A2 --> B
    A3 --> B
    B --> L
    B -.->|"直送（簡單場景）"| E
    L --> E
    E --> K

    style L fill:#f9ca24
    style E fill:#6ab04c
    style K fill:#eb4d4b
```

#### 1.3.1 元件簡介

| 元件 | 角色 | 類比 | 9.5 版重點 |
| --- | --- | --- | --- |
| **Elasticsearch** | 分散式搜尋與分析引擎 | 資料庫 + 搜尋引擎 | Lucene 10.5、內建 OpenJDK 26、LogsDB 預設用於 `logs-*-*` |
| **Logstash** | 資料收集與處理引擎 | ETL 工具 | 內建 JDK 21（9.4 起最低 JDK 21）、預設禁止以 root 執行 |
| **Kibana** | 視覺化、查詢與管理介面 | BI 報表 + 管理主控台 | Discover／Lens／ES\|QL、Alerting、Streams、Dashboards API |
| **Filebeat** | 輕量 Log 收集器 | 日誌搬運工 | 只支援 `filestream` input；預設以 fingerprint 識別檔案 |
| **Elastic Agent** | 統一代理程式（可由 Fleet 集中管理） | 多合一收集器 | 9.5 起內建 EDOT Collector（OpenTelemetry） |

#### 1.3.2 從 ELK 到 Elastic Stack 的演進

| 時期 | 典型架構 | 說明 |
| --- | --- | --- |
| 早期 | Logstash → Elasticsearch → Kibana | Logstash 同時負責收集與處理，資源消耗高 |
| 5.x–7.x | Beats → Logstash → Elasticsearch → Kibana | Beats 取代 Logstash 的收集角色 |
| 8.x | Beats／Elastic Agent → (Logstash／Ingest Pipeline) → Data Stream | 預設啟用安全性、Data Stream 成為時序資料標準 |
| 9.x | Beats／Elastic Agent／OTel → Data Stream（LogsDB）→ Kibana（ES\|QL、Streams） | OpenTelemetry 原生支援、Log 儲存最佳化、AI 輔助分析 |

> 💡 **建議**：本手冊仍沿用「ELK」稱呼以便溝通，但設計時應以 Elastic Stack 9.x 的完整元件與 Data Stream 模型為準。

---

### 1.4 ELK 在 Observability 架構中的角色

```mermaid
graph TB
    subgraph "應用層"
        App[Java / Spring Boot 應用]
    end

    subgraph "Observability Platform"
        subgraph "Metrics"
            Prom[Prometheus]
            Graf[Grafana]
        end

        subgraph "Logs"
            FB[Filebeat]
            LS[Logstash]
            ES[Elasticsearch]
            Kib[Kibana]
        end

        subgraph "Traces"
            Trc[Jaeger / Elastic APM]
        end
    end

    subgraph "告警與通知"
        AM[Alertmanager]
        Teams[MS Teams / Email]
    end

    App -->|"Metrics"| Prom
    App -->|"Logs"| FB
    App -->|"Traces"| Trc

    Prom --> Graf
    FB --> LS --> ES --> Kib

    Prom --> AM --> Teams
    Kib -->|"Kibana Alerting Rule"| Teams

    style ES fill:#6ab04c
    style Prom fill:#e17055
```

> ⚠️ **v2.0 更正**：v1.0 圖中以「Elasticsearch Watcher → Teams」作為 Log 告警路徑。Watcher 屬付費功能且已非主要告警機制，9.x 建議改用 **Kibana Alerting Rules + Connectors**（見 [6.3 告警（Alerting）](#63-告警alerting)）。

#### 1.4.1 Observability 分層職責

| 層級 | 工具 | 回答的問題 |
| --- | --- | --- |
| **What** | Metrics（Prometheus） | 發生了什麼？（錯誤率上升） |
| **Why** | Logs（ELK） | 為什麼發生？（NullPointerException） |
| **Where** | Traces（Jaeger／Elastic APM） | 在哪裡發生？（Service A → Service B） |

---

### 1.5 授權模式與功能層級

> 🆕 **v2.0 新增**

企業導入前必須先釐清授權，因為多項「看起來是標準功能」的能力其實屬於付費訂閱，若規劃時未注意，常在上線前才發現無法使用。

#### 1.5.1 授權沿革

| 時間 | 變更 | 對企業的意義 |
| --- | --- | --- |
| 2021-01（7.11） | Elasticsearch、Kibana 原始碼由 Apache 2.0 改為 SSPL／Elastic License 2.0（ELv2）雙授權 | 雲端業者 fork 出 OpenSearch |
| 2024-08 | 原始碼再加入 **AGPLv3** 選項 | 重新符合 OSI 開源定義；企業自用不受影響 |
| 目前 | 官方發行版（下載的套件／映像）採 Elastic License，內含免費的 Basic 功能 | 自建使用 Basic 功能免費；進階功能需訂閱 |

> ⚠️ **實務注意**：AGPLv3 主要影響「修改原始碼並對外提供服務」的情境。企業內部直接使用官方發行版，依 Elastic License 與訂閱合約為準，導入前請由法務確認。

#### 1.5.2 Basic（免費）與付費功能對照

| 功能 | Basic（免費） | 付費（Platinum／Enterprise） | 本手冊章節 |
| --- | --- | --- | --- |
| TLS 加密、內建使用者／角色、API Key | ✅ | ✅ | 第九章 |
| ILM、Data Stream、Data Tiers、SLM | ✅ | ✅ | 第七章 |
| Discover、Lens、Dashboard、ES\|QL | ✅ | ✅ | 第六章 |
| Kibana Alerting（Index、Server log 等基本 Connector） | ✅ | ✅ | 6.3 |
| 外部通知 Connector（Email、Slack、MS Teams、Webhook 等） | ❌ | ✅ | 6.3 |
| Watcher | ❌ | ✅ | 6.3 |
| Field／Document Level Security | ❌ | ✅ | 9.3 |
| 稽核日誌（Audit Logging） | ❌ | ✅ | 9.4 |
| SAML／OIDC／LDAP／AD 單一登入 | ❌ | ✅ | 9.2 |
| Machine Learning 異常偵測 | ❌ | ✅ | 10.3 |
| Cross-Cluster Replication | ❌ | ✅ | 2.7 |
| Searchable Snapshots（Frozen Tier） | ❌ | Enterprise | 2.4、7.1 |
| AI Assistant／Agent Builder | ❌ | Enterprise | 10.3 |

> 💰 **授權**：Platinum 已不再提供給新客戶，新採購以 Enterprise 為主。各功能所屬層級會隨版本調整，簽約前請以 [Elastic Subscriptions](https://www.elastic.co/subscriptions) 頁面與合約為準（本表待確認項目見 [E.1 待確認事項](#e1-待確認事項)）。

#### 1.5.3 與 OpenSearch 的差異

| 面向 | Elastic Stack 9.x | OpenSearch |
| --- | --- | --- |
| 來源 | Elastic 官方 | 2021 年自 Elasticsearch 7.10.2 fork，現由 Linux Foundation 下的 OpenSearch Software Foundation 管理 |
| 授權 | AGPLv3／SSPL／ELv2；發行版採 Elastic License | Apache 2.0 |
| API 相容性 | — | 與 7.10 相容，之後各自演進；ES\|QL、LogsDB 等為 Elastic 獨有 |
| 客戶端 | `elasticsearch-java` 等官方 Client | `opensearch-java` 等獨立 Client |

> 💡 **建議**：兩者已不可互換。選定後即以該產品的官方文件、Client 與相容性矩陣為準，避免混用網路教學。

---

### 1.6 版本發佈節奏與支援策略

> 🆕 **v2.0 新增**

Elastic Stack 約每 3 個月發佈一個 minor 版本，各元件（ES、Logstash、Kibana、Beats）**同步發版、同版號**。

| 版本 | 發佈日 | 支援結束（EOS） | 最新 Patch（2026-10-01） |
| --- | --- | --- | --- |
| **9.5** | 2026-08-04 | 支援中 | 9.5.4（2026-09-15） |
| 9.4 | 2026-05-05 | 支援中 | 9.4.7（2026-09-15） |
| 9.3 | 2026-02-03 | 2026-08-04 | 9.3.8 |
| 9.2 | 2025-10-23 | 2026-05-05 | 9.2.8 |
| 9.1 | 2025-07-29 | 2026-02-03 | 9.1.10 |
| 9.0 | 2025-04-15 | 2025-10-23 | 9.0.8 |
| **8.19** | 2025-07-29 | **2027-07-15** | 8.19.22（2026-09-23） |
| 7.17 | 2022-02 | 2026-01-15 | 7.17.29 |

> ⚠️ **實務注意**：9.x 的每個 minor 版本在「其後第二個 minor 發佈時」即停止支援（例如 9.3 於 9.5 發佈當天 EOS），支援期約 6 個月，企業應規劃**每半年至少升級一次 minor**。8.19 是 8.x 最後一版，支援至 2027-07-15，可作為升級 9.x 的跳板，但不建議長期停留。

---

### 1.7 與 AI 輔助開發的關係

ELK 收集的結構化 Log 是 AI 分析的絕佳資料來源。9.x 起 Kibana 內建 AI Assistant、Agent Builder 與 Streams 的 AI 解析建議，但無論使用內建或外部 AI，**資料治理與人工判斷**仍是前提（見 [10.3 與 AI 分析結合](#103-與-ai-分析結合)）。

#### 1.7.1 AI 輔助場景

```mermaid
graph LR
    subgraph "Log 資料"
        E[Elasticsearch]
    end

    subgraph "AI 應用"
        A1[異常偵測<br/>Anomaly Detection]
        A2[根因分析<br/>Root Cause Analysis]
        A3[Log 解析建議<br/>Streams Processing]
        A4["自然語言查詢<br/>NL to ES|QL"]
    end

    E --> A1
    E --> A2
    E --> A3
    E --> A4
```

#### 1.7.2 實務應用範例

**1. 自然語言查詢**

```text
👤 使用者問：「昨天下午 3 點到 4 點，訂單服務有多少 Error？」

🤖 AI 轉換為 ES|QL：
FROM logs-*
| WHERE service.name == "order-service" AND log.level == "ERROR"
  AND @timestamp >= "2026-09-30T15:00:00+08:00" AND @timestamp < "2026-09-30T16:00:00+08:00"
| STATS errors = COUNT(*)
```

**2. 異常 Pattern 識別**

```text
🤖 AI 分析結果：
「偵測到異常 Pattern：每週三 14:00-14:30 期間，
  payment-service 的 Connection Timeout 錯誤率上升 300%。
  建議檢查該時段是否有排程任務造成資源競爭。」
```

**3. 根因分析輔助**

```text
👤 問：「交易 TXN-20260930-001 為什麼失敗？」

🤖 AI 分析 Log 鏈路後回答：
「交易失敗根因：
  1. order-service 收到請求 (14:32:01.123)
  2. 呼叫 inventory-service 檢查庫存 (14:32:01.456)
  3. inventory-service 回應 timeout (14:32:06.789) ← 瓶頸
  4. order-service 拋出 ServiceUnavailableException

  建議：檢查 inventory-service 該時段的資源使用狀況」
```

> ⚠️ **實務注意**：AI 回答須以原始 Log 驗證；將 Log 送往外部 LLM 前必須完成去識別化，並遵循組織的 AI 使用政策。

---

### 1.8 💡 本章實務建議

- Logs Visualization 解決傳統 Log 管理的分散、難查、難關聯與存取失控問題。
- ELK 與 Prometheus／Grafana、Tracing 互補，共同構成完整 Observability；告警改用 Kibana Alerting。
- 導入前先確認授權層級：外部通知 Connector、FLS／DLS、稽核日誌、SSO 皆為付費功能。
- 採用 9.x 最新 minor 版，並建立每半年升級一次的節奏；8.19 僅作為過渡。
- 結構化 Log 是 AI 分析的基礎，但 AI 結論需人工驗證、資料需先去識別化。

---

## 第二章：系統整體架構設計

### 2.1 ELK Stack 架構圖

#### 2.1.1 基礎架構（小型環境）

適用於開發、測試、POC 或每日 Log 量低於 10 GB 的非關鍵系統。

```mermaid
graph TB
    subgraph "Application Servers"
        App1[App Server 1 + Filebeat]
        App2[App Server 2 + Filebeat]
        App3[App Server 3 + Filebeat]
    end

    subgraph "ELK Stack - Single Node"
        LS[Logstash]
        ES[Elasticsearch]
        K[Kibana]
    end

    App1 -->|"Beats 5044 / TLS"| LS
    App2 -->|"Beats 5044 / TLS"| LS
    App3 -->|"Beats 5044 / TLS"| LS

    LS -->|"Bulk API 9200 / HTTPS"| ES
    ES -->|"Query"| K

    User[使用者] -->|"HTTPS 5601"| K
```

#### 2.1.2 企業級架構（大型環境）

```mermaid
graph TB
    subgraph "Application Layer"
        App1[App Server 1]
        App2[App Server 2]
        App3[App Server N...]
    end

    subgraph "Collection Layer"
        FB1[Filebeat 1]
        FB2[Filebeat 2]
        FB3[Filebeat N]
    end

    subgraph "Buffer Layer"
        Kafka[Apache Kafka]
    end

    subgraph "Processing Layer"
        LS1[Logstash 1]
        LS2[Logstash 2]
    end

    subgraph "Storage Layer - ES Cluster"
        ES1[Master 1]
        ES2[Master 2]
        ES3[Master 3]
        H1[Hot Data 1]
        H2[Hot Data 2]
        W1[Warm Data 1]
        W2[Warm Data 2]
    end

    subgraph "Presentation Layer"
        LB[Load Balancer]
        K1[Kibana 1]
        K2[Kibana 2]
    end

    App1 --> FB1
    App2 --> FB2
    App3 --> FB3

    FB1 --> Kafka
    FB2 --> Kafka
    FB3 --> Kafka

    Kafka --> LS1
    Kafka --> LS2

    LS1 --> H1
    LS2 --> H2

    ES1 --- ES2 --- ES3
    H1 -.->|"ILM 移轉"| W1
    H2 -.->|"ILM 移轉"| W2

    User[使用者] --> LB
    LB --> K1
    LB --> K2
    K1 --> H1
    K2 --> H2
```

> 💡 **建議**：Logstash 的 Elasticsearch output 應列出多個節點（或指向專用的 coordinating 節點），由 Client 端負載平衡；不要讓所有寫入集中在單一 data 節點。

---

### 2.2 各元件角色說明

#### 2.2.1 Logstash：資料處理引擎

```text
┌─────────────────────────────────────────────────────────────┐
│                      Logstash Pipeline                       │
├─────────────┬─────────────────────────┬────────────────────┤
│   INPUT     │        FILTER           │      OUTPUT        │
├─────────────┼─────────────────────────┼────────────────────┤
│ • beats     │ • grok (正規表達式解析)  │ • elasticsearch    │
│ • kafka     │ • dissect (分隔字元解析) │ • kafka            │
│ • tcp/udp   │ • date (時間解析)        │ • file / s3        │
│ • http      │ • mutate (欄位修改)      │ • stdout (除錯)    │
│ • jdbc      │ • geoip / useragent     │ • pipeline (轉送)  │
└─────────────┴─────────────────────────┴────────────────────┘
```

**核心功能**：

- 從多種來源收集資料（Beats、Kafka、HTTP、JDBC 等）
- 解析、轉換、enrichment（grok、dissect、translate、geoip）
- 以 Persistent Queue 與 Dead Letter Queue 提供緩衝與錯誤隔離
- 輸出到多種目的地，並支援 pipeline-to-pipeline 分流

#### 2.2.2 Elasticsearch：分散式搜尋引擎

```text
┌─────────────────────────────────────────────────────────────┐
│                    Elasticsearch Cluster                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │  Master     │  │  Master     │  │  Master     │          │
│  │  Node 1     │  │  Node 2     │  │  Node 3     │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│         │               │               │                   │
│  ┌──────┴───────────────┴───────────────┴──────┐            │
│  │              Cluster State                   │            │
│  └──────────────────────────────────────────────┘            │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │  Data       │  │  Data       │  │  Data       │          │
│  │  Node 1     │  │  Node 2     │  │  Node N     │          │
│  │  ┌───────┐  │  │  ┌───────┐  │  │  ┌───────┐  │          │
│  │  │Shard 0│  │  │  │Shard 1│  │  │  │Shard 2│  │          │
│  │  │Primary│  │  │  │Primary│  │  │  │Primary│  │          │
│  │  └───────┘  │  │  └───────┘  │  │  └───────┘  │          │
│  │  ┌───────┐  │  │  ┌───────┐  │  │  ┌───────┐  │          │
│  │  │Shard 1│  │  │  │Shard 2│  │  │  │Shard 0│  │          │
│  │  │Replica│  │  │  │Replica│  │  │  │Replica│  │          │
│  │  └───────┘  │  │  └───────┘  │  │  └───────┘  │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
└─────────────────────────────────────────────────────────────┘
```

**核心概念**：

| 概念 | 說明 |
| --- | --- |
| **Cluster** | 多個 Node 組成的叢集，以 `cluster.name` 識別 |
| **Node** | 單一 Elasticsearch 實例，依 `node.roles` 承擔不同職責 |
| **Index** | 文件的邏輯集合，對應一組 Shard |
| **Data Stream** | 時序資料（Log、Metrics）的標準存放方式：對外是一個名稱，對內由多個隱藏的 backing index 組成，只能附加寫入 |
| **Backing Index** | Data Stream 背後的實際索引，命名如 `.ds-logs-app-default-2026.10.01-000001`，由 rollover 產生 |
| **Shard** | Index 的水平分割單位（一個 Lucene 索引） |
| **Replica** | Shard 的副本，提供 HA 與查詢擴展 |
| **Mapping** | 欄位型別定義（`keyword`、`text`、`date`、`long` 等） |

> 💡 **建議**：Log 類資料一律使用 Data Stream，命名遵循 `{type}-{dataset}-{namespace}`（例如 `logs-orderservice-prod`），即可自動套用內建的 `logs` 範本、ILM 與 LogsDB（見 [7.1 Data Stream 與 Index 管理](#71-data-stream-與-index-管理)）。

#### 2.2.3 Kibana：視覺化與管理平台

```text
┌──────────────────────────────────────────────────────────────────────┐
│                          Kibana 功能模組                              │
├──────────────┬──────────────┬──────────────┬──────────────┬─────────┤
│   Discover   │  Dashboards  │   Alerting   │   Streams    │  Stack  │
│              │  / Lens      │   / Cases    │              │  Mgmt   │
├──────────────┼──────────────┼──────────────┼──────────────┼─────────┤
│ • Log 查詢   │ • 圖表建立   │ • 規則告警   │ • Log 解析   │ • ILM   │
│ • KQL/ES|QL  │ • 儀表板組合 │ • 通知連線   │ • 路由分流   │ • 權限  │
│ • 時間篩選   │ • 分享匯出   │ • 事件管理   │ • 資料品質   │ • 空間  │
└──────────────┴──────────────┴──────────────┴──────────────┴─────────┘
```

#### 2.2.4 Filebeat 與 Elastic Agent

| 面向 | Filebeat | Elastic Agent |
| --- | --- | --- |
| 定位 | 單一用途的 Log 收集器 | 統一代理程式（Log、Metrics、Security、OTel） |
| 設定管理 | 各主機的 `filebeat.yml`（可用 Ansible 等派送） | 由 Kibana **Fleet** 集中管理 Policy，或 standalone |
| 資料解析 | Processors + Modules | Integrations（內含 ingest pipeline、Dashboard） |
| 適用場景 | 既有 Beats 架構、需完全自主控管設定 | 新建置、需要集中管理大量主機 |

> 💡 **建議**：既有 Filebeat 架構可繼續使用（9.x 仍完整支援）；新專案若主機數多、需要集中管理，優先評估 Elastic Agent + Fleet（見 [5.6 Elastic Agent 與 Fleet](#56-elastic-agent-與-fleet)）。

---

### 2.3 單節點 vs 多節點架構

#### 2.3.1 架構選擇決策表

| 面向 | 單節點 | 多節點叢集 |
| --- | --- | --- |
| **適用場景** | 開發、測試、POC | 正式環境、大流量 |
| **Log 量** | < 10 GB／天 | > 10 GB／天 |
| **可用性** | 無 HA；Replica 無法配置（叢集為 yellow） | 支援 HA |
| **擴展性** | 有限 | 水平擴展 |
| **成本** | 低 | 較高 |
| **維運複雜度** | 簡單 | 較複雜 |

> ⚠️ **實務注意**：單節點叢集的 Replica 無處配置，`logs-*-*` 內建範本預設 1 個 Replica，因此狀態會是 **yellow**。開發環境可在 `logs@custom` 中設定 `index.number_of_replicas: 0`；正式環境不可只用單節點。

#### 2.3.2 節點角色說明

```mermaid
graph TB
    subgraph "Elasticsearch Node Roles"
        M[master<br/>叢集狀態管理]
        H[data_hot<br/>寫入與近期查詢]
        W[data_warm / data_cold<br/>較舊資料]
        F[data_frozen<br/>Searchable Snapshot]
        I[ingest<br/>Ingest Pipeline]
        C["coordinating only<br/>node.roles: []"]
    end

    M -->|"管理"| H
    C -->|"路由查詢 / 彙整結果"| H
    I -->|"處理後寫入"| H
    H -.->|"ILM 移轉"| W
    W -.->|"ILM 移轉"| F
```

| 節點角色（`node.roles`） | 職責 | 建議數量／配置 |
| --- | --- | --- |
| `master` | 叢集狀態管理、Index 建立／刪除、Shard 配置 | 3 個專用節點（奇數，跨可用區） |
| `voting_only` | 只參與選舉投票，不會成為 master | 兩機房架構的仲裁節點 |
| `data_content` | 非時序資料（一般 Index） | 通常與 `data_hot` 同節點 |
| `data_hot` | 新寫入與近期查詢的 Log | NVMe SSD，依寫入量擴充 |
| `data_warm`／`data_cold` | 較舊、查詢頻率低的資料 | 大容量磁碟，可使用較低規格 |
| `data_frozen` | 以 Searchable Snapshot 掛載的極冷資料 | 💰 Enterprise；需物件儲存 |
| `ingest` | 執行 Ingest Pipeline | 可與 hot 節點共用，或獨立擴充 |
| `ml` | Machine Learning 工作 | 💰 付費功能 |
| `remote_cluster_client` | 跨叢集查詢／複寫 | 需要 CCS／CCR 時 |
| `transform` | Transform 工作 | 需要時 |
| （空陣列）`[]` | Coordinating only：路由與彙整 | 高查詢量或大量聚合時 |

> ⚠️ **v2.0 更正**：v1.0 以「Master／Data／Ingest／Coordinating」四種節點描述，未涵蓋 Data Tiers 角色；8.x 起建議以 `data_hot`、`data_warm` 等角色取代泛用的 `data` 角色。

---

### 2.4 Data Tiers 與資料溫度

> 🆕 **v2.0 新增**

Log 的查詢頻率會隨時間急遽下降，Data Tiers 讓不同年齡的資料放在不同成本的硬體上，由 ILM 自動搬移。

```mermaid
graph LR
    H["Hot<br/>0–7 天<br/>NVMe SSD"] -->|"rollover 後 7 天"| W["Warm<br/>7–30 天<br/>SATA SSD / HDD"]
    W -->|"30 天"| C["Cold<br/>30–90 天<br/>大容量 HDD"]
    C -->|"90 天"| F["Frozen<br/>90 天以上<br/>物件儲存"]
    F -->|"保存期滿"| D[Delete]

    style H fill:#ff6b6b
    style W fill:#feca57
    style C fill:#54a0ff
    style F fill:#c8d6e5
    style D fill:#576574
```

| Tier | 資料特性 | 硬體建議 | Replica | 授權 |
| --- | --- | --- | --- | --- |
| Hot | 持續寫入、查詢最頻繁 | 高 CPU、NVMe SSD | 1 | Basic |
| Warm | 唯讀、偶爾查詢 | 中等 CPU、大容量 SSD／HDD | 1 | Basic |
| Cold | 很少查詢 | 大容量 HDD；可用 Searchable Snapshot 省去 Replica | 0–1 | Basic（Searchable Snapshot 需 Enterprise） |
| Frozen | 幾乎不查詢、需長期保存 | 小量本機快取 + S3／MinIO 等物件儲存 | 0（由快照保護） | 💰 Enterprise |

> 💡 **建議**：Basic 授權可用 Hot／Warm／Cold 三層 + 一般 Snapshot 長期保存；若法規要求「可隨時查詢」數年的 Log，Frozen Tier 的成本效益通常優於全部放在 Warm／Cold。

---

### 2.5 容量規劃與 Sizing

> 🆕 **v2.0 新增**

#### 2.5.1 儲存容量估算公式

```text
所需儲存（各 Tier 分別計算）
  = 每日原始 Log 量 × 索引膨脹係數 × (1 + Replica 數) × 該 Tier 保存天數
    ÷ (1 − 磁碟保留比例)

索引膨脹係數：standard 模式約 1.0–1.3；LogsDB 模式約 0.4–0.6（需以實際資料測量）
磁碟保留比例：建議 ≥ 25%（high watermark 90% 之外，再保留 rollover 與 merge 的空間）
```

#### 2.5.2 估算範例

**條件**：每日原始 Log 100 GB、LogsDB（膨脹係數以 0.5 計）、Replica 1、Hot 7 天、Warm 23 天、Cold 60 天（合計 90 天）。

| Tier | 計算 | 所需容量 |
| --- | --- | --- |
| Hot | 100 × 0.5 × 2 × 7 ÷ 0.75 | ≈ 0.93 TB |
| Warm | 100 × 0.5 × 2 × 23 ÷ 0.75 | ≈ 3.07 TB |
| Cold | 100 × 0.5 × 1 × 60 ÷ 0.75（Cold 不設 Replica、由 Snapshot 保護） | ≈ 4.0 TB |

#### 2.5.3 Shard 與節點數估算

| 項目 | 建議值 | 說明 |
| --- | --- | --- |
| 單一 Shard 大小 | 10–50 GB | 內建 `logs` ILM 在 primary shard 50 GB 時 rollover |
| 單一 Shard 文件數 | < 2 億筆 | 過多會影響 merge 與查詢 |
| 每節點 Shard 上限 | `cluster.max_shards_per_node` 預設 1000（不含 frozen） | 實際上限受 Heap 與欄位數影響 |
| Hot 節點寫入能力 | 以壓測為準 | 依文件大小與解析複雜度差異極大 |

> ⚠️ **實務注意**：上述公式只用於預算與採購初估。正式規劃必須以實際 Log 在 9.5 環境進行 **1–3 天的寫入與查詢壓測**（可用 Elastic 官方的 Rally 工具），再依結果調整。

---

### 2.6 Production 建議架構

#### 2.6.1 中型企業建議架構（日誌量 50–200 GB／天）

```mermaid
graph TB
    subgraph "Collection"
        FB[Filebeat x N]
    end

    subgraph "Processing"
        LS1[Logstash 1]
        LS2[Logstash 2]
    end

    subgraph "Elasticsearch Cluster"
        subgraph "Master Nodes（跨 3 個可用區）"
            M1[Master 1<br/>4 vCPU / 8 GB]
            M2[Master 2<br/>4 vCPU / 8 GB]
            M3[Master 3<br/>4 vCPU / 8 GB]
        end

        subgraph "Hot Tier"
            D1[Hot 1<br/>16 vCPU / 64 GB / 2 TB NVMe]
            D2[Hot 2<br/>16 vCPU / 64 GB / 2 TB NVMe]
            D3[Hot 3<br/>16 vCPU / 64 GB / 2 TB NVMe]
        end

        subgraph "Warm Tier"
            W1[Warm 1<br/>8 vCPU / 64 GB / 8 TB]
            W2[Warm 2<br/>8 vCPU / 64 GB / 8 TB]
        end
    end

    subgraph "Visualization"
        K1[Kibana 1]
        K2[Kibana 2]
    end

    FB --> LS1
    FB --> LS2
    LS1 --> D1
    LS1 --> D2
    LS2 --> D2
    LS2 --> D3
    M1 --- M2 --- M3
    D1 -.-> W1
    D3 -.-> W2
    K1 --> D1
    K2 --> D3
```

#### 2.6.2 硬體規格建議

| 元件 | CPU | Memory | Disk | 數量 |
| --- | --- | --- | --- | --- |
| **ES Master** | 4 vCPU | 8–16 GB | 50 GB SSD | 3 |
| **ES Hot Data** | 16 vCPU | 64 GB | 2–4 TB NVMe SSD | 3+ |
| **ES Warm Data** | 8 vCPU | 64 GB | 8–16 TB SSD／HDD | 2+ |
| **Logstash** | 8 vCPU | 16 GB（Heap 4–8 GB） | 100 GB（Persistent Queue 用） | 2+ |
| **Kibana** | 4 vCPU | 8 GB | 20 GB | 2 |

> 💡 **建議**：Data 節點記憶體約一半給 JVM Heap（9.x 預設自動計算），另一半留給作業系統的檔案系統快取；Lucene 查詢效能高度依賴這部分快取。

#### 2.6.3 關鍵設計原則

```text
┌─────────────────────────────────────────────────────────────┐
│                  Production 架構設計原則                     │
├─────────────────────────────────────────────────────────────┤
│  1. 3 個專用 Master Node，分散在不同可用區／機櫃              │
│  2. Data Node 依 Hot / Warm / Cold 分層，由 ILM 自動搬移      │
│  3. Hot 節點使用本機 NVMe SSD，避免 NFS 等網路檔案系統         │
│  4. Logstash 部署 2+ 台並啟用 Persistent Queue              │
│  5. 寫入量大或來源不穩定時，加入 Kafka 作為 Buffer Layer       │
│  6. Kibana 2+ 台，前端加 Load Balancer 與 TLS                │
│  7. 全鏈路 TLS、API Key 最小權限、Snapshot 每日備份           │
└─────────────────────────────────────────────────────────────┘
```

---

### 2.7 高可用與災難備援

> 🆕 **v2.0 新增**

#### 2.7.1 叢集內高可用

| 機制 | 設定 | 效果 |
| --- | --- | --- |
| 3 個 Master 跨可用區 | 各可用區 1 個 master 節點 | 任一可用區失效仍能選出 master |
| Shard Allocation Awareness | `node.attr.zone: zone-a` + `cluster.routing.allocation.awareness.attributes: zone` | Primary 與 Replica 不會放在同一可用區 |
| Replica ≥ 1 | Index 範本設定 | 單一節點失效不遺失資料 |
| Client 端多節點 | Logstash／Kibana 設定多個 `hosts` | 單一節點失效不中斷寫入與查詢 |

```yaml
# elasticsearch.yml（以 zone-a 的節點為例）
node.attr.zone: zone-a
cluster.routing.allocation.awareness.attributes: zone
# 強制感知：某一 zone 全部失效時，不把其 replica 擠到剩下的 zone
cluster.routing.allocation.awareness.force.zone.values: zone-a,zone-b,zone-c
```

#### 2.7.2 跨機房災難備援

| 方案 | RPO／RTO | 授權 | 適用 |
| --- | --- | --- | --- |
| Snapshot 至異地物件儲存 + 還原 | RPO＝快照間隔；RTO＝還原時間（小時級） | Basic | 大多數 Log 平台 |
| 雙寫（Kafka 分送兩個叢集） | RPO≈0；RTO 分鐘級 | Basic | 關鍵稽核 Log |
| Cross-Cluster Replication（CCR） | RPO 秒級；RTO 分鐘級 | 💰 付費 | 需要熱備援的大型環境 |

> 💡 **建議**：Log 平台多半可接受小時級 RTO，「每日 Snapshot 到異地 + 定期還原演練」是成本最低的做法；稽核類 Log 若需零遺失，則在 Kafka 層雙寫。

---

### 2.8 與 Prometheus／Grafana 並存架構

```mermaid
graph TB
    subgraph "Application"
        App[Java / Spring Boot]
    end

    subgraph "Metrics Pipeline"
        Prom[Prometheus]
        Graf[Grafana]
    end

    subgraph "Logs Pipeline"
        FB[Filebeat]
        LS[Logstash]
        ES[Elasticsearch]
        Kib[Kibana]
    end

    subgraph "Alerting"
        AM[Alertmanager]
        Teams[MS Teams / Email]
    end

    App -->|"/actuator/prometheus"| Prom
    App -->|"Log File"| FB

    Prom --> Graf
    FB --> LS --> ES --> Kib

    Prom --> AM --> Teams
    Kib -->|"Alerting Rule + Connector"| Teams

    Graf -.->|"Data Link 至 Kibana"| Kib
    Graf -.->|"Elasticsearch 資料來源（選用）"| ES
```

#### 2.8.1 整合策略

| 策略 | 說明 |
| --- | --- |
| **統一時間軸** | 所有系統以 UTC 儲存，Grafana 與 Kibana 以使用者時區顯示（Kibana `dateFormat:tz`） |
| **Deep Link 整合** | Grafana Panel 的 Data Link 帶入時間範圍與服務名稱，跳轉至 Kibana Discover |
| **共用告警通道** | Alertmanager 與 Kibana Connector 指向相同的 Teams／Email 通道，並統一告警命名 |
| **Correlation ID** | Log 與 Trace 使用相同的 `trace.id`（OpenTelemetry／Micrometer Tracing 自動注入 MDC） |
| **PromQL in Elastic（9.5 GA）** | 9.5 起 Elastic 可原生接收 Prometheus 指標並支援 PromQL，可評估是否整併；本手冊仍以既有 Prometheus 為主 |

#### 2.8.2 Grafana 連結 Kibana 範例

在 Grafana Panel 的 **Data links** 設定以下 URL（使用 Grafana 內建變數帶入時間範圍與標籤）：

```text
https://kibana.company.com/app/discover#/?_g=(time:(from:'${__from:date:iso}',to:'${__to:date:iso}'))&_a=(query:(language:kuery,query:'service.name:"${__field.labels.service}" and log.level:"ERROR"'))
```

> ⚠️ **v2.0 更正**：v1.0 使用 `alerting.notification_channels` 的 YAML 設定，該機制屬 Grafana Legacy Alerting，已於 Grafana 11 移除；請改用 Panel Data Links 或 Grafana Alerting 的 Contact point／通知範本。

---

### 2.9 💡 本章實務建議

- 正式環境至少 3 個專用 Master，Data 節點依 Hot／Warm／Cold 分層。
- Log 一律寫入 Data Stream（`logs-{dataset}-{namespace}`），自動套用 ILM 與 LogsDB。
- 以容量公式做預算初估，再用實際 Log 壓測定案；Shard 控制在 10–50 GB。
- 以 Allocation Awareness 跨可用區配置 Replica，並以異地 Snapshot 作為最低限度的 DR。
- 與 Grafana 以 Data Link、統一時區與 `trace.id` 串接，告警通道統一管理。

---

## 第三章：系統安裝

### 3.1 環境需求總覽

#### 3.1.1 作業系統支援

| OS | 支援狀態 | 建議 |
| --- | --- | --- |
| RHEL 8／9 系列（含 Rocky Linux、AlmaLinux、Oracle Linux） | ✅ 支援 | 企業首選 |
| Ubuntu 22.04／24.04 LTS | ✅ 支援 | 常見於雲端與容器主機 |
| Debian 11／12 | ✅ 支援 | |
| SLES 15、Amazon Linux 2023 | ✅ 支援 | |
| Windows Server | ⚠️ 支援但不建議 | 僅限開發測試；正式環境以 Linux 為主 |
| 容器（Docker／Kubernetes） | ✅ 官方映像 | Kubernetes 建議使用 ECK（第十二章） |

> ⚠️ **v2.0 更正**：v1.0 列出的 RHEL／CentOS 7、Ubuntu 18.04、Debian 10 皆已結束原廠支援，不應再用於新建置。各版本的精確支援清單以 [Elastic Support Matrix](https://www.elastic.co/support/matrix) 為準（見 [E.1 待確認事項](#e1-待確認事項)）。

#### 3.1.2 版本選擇原則

```text
┌─────────────────────────────────────────────────────────────┐
│                    版本選擇建議                              │
├─────────────────────────────────────────────────────────────┤
│  ✅ 所有元件使用「完全相同的版本號」（如都用 9.5.4）           │
│  ✅ 選擇最新 minor 的最新 patch（非 RC / Beta）               │
│  ✅ 參考 Elastic 官方 Support Matrix 與 Breaking Changes      │
│  ✅ Beats / Logstash / Agent 可落後 ES，但不可新於 ES         │
│  ⚠️  避免跨大版本混用（如 ES 9.x + Kibana 8.x）               │
└─────────────────────────────────────────────────────────────┘

目前建議版本：9.5.4（2026-09-15）
仍在 8.x 者：先升到 8.19.x（支援至 2027-07-15），再規劃升級 9.x
```

> ⚠️ **v2.0 更正**：v1.0 建議 8.12.x，該版本已於 2024 年結束支援。
>
> 📌 **8.19 差異**：8.19 的 Elastic Agent、Beats、Logstash 可搭配所有 9.x 版本的 Elasticsearch，方便分階段升級（見 [8.1 版本策略與升級路徑](#81-版本策略與升級路徑)）。

#### 3.1.3 硬體需求（單節點最低配置）

| 元件 | CPU | Memory | Disk |
| --- | --- | --- | --- |
| **Elasticsearch** | 2 vCPU | 4 GB（建議 8 GB） | 50 GB SSD |
| **Logstash** | 2 vCPU | 4 GB | 20 GB |
| **Kibana** | 1 vCPU | 2 GB | 10 GB |

> 💡 **建議**：以上僅適用開發測試；正式環境規格見 [2.6.2 硬體規格建議](#262-硬體規格建議)。

#### 3.1.4 網路埠需求

| 元件 | 預設埠 | 用途 | 開放對象 |
| --- | --- | --- | --- |
| Elasticsearch | 9200 | HTTP（REST API，9.x 預設 HTTPS） | Logstash、Kibana、管理主機 |
| Elasticsearch | 9300 | Transport（節點間通訊，TLS） | 僅叢集節點之間 |
| Kibana | 5601 | Web UI 與 API | 使用者（建議經 Reverse Proxy／LB） |
| Logstash | 5044 | Beats Input | Filebeat 主機 |
| Logstash | 9600 | Monitoring API（預設只綁 `127.0.0.1`） | 本機或監控主機 |
| Fleet Server | 8220 | Elastic Agent 註冊與 Policy 下發 | Elastic Agent 主機 |
| OTel Collector | 4317／4318 | OTLP gRPC／HTTP | 應用程式與 Agent 模式 Collector |

---

### 3.2 系統前置調校

> 🆕 **v2.0 新增**

正式環境啟動 Elasticsearch 前，需先完成以下系統調校；若綁定非 localhost 位址（production mode），未通過的項目會在 bootstrap check 階段直接讓節點無法啟動。

| 項目 | 建議值 | 套件安裝（RPM／DEB）是否自動處理 |
| --- | --- | --- |
| `vm.max_map_count` | ≥ 262144 | ✅ 套件會自動設定；tar／Docker 主機需自行設定 |
| 最大開檔數（nofile） | ≥ 65535 | ✅ systemd unit 已設定 `LimitNOFILE=65535` |
| 最大執行緒數（nproc） | ≥ 4096 | ✅ systemd unit 已設定 |
| 關閉 Swap | `swapoff -a` 或 `bootstrap.memory_lock: true` | ❌ 需自行處理 |
| 時間同步 | chrony／NTP | ❌ 需自行處理（時間偏差會造成 Log 時序錯亂與憑證錯誤） |
| 檔案系統 | 本機 XFS／ext4 | ❌ 避免 NFS 等網路檔案系統 |

```bash
# 1. 關閉 Swap（並註解 /etc/fstab 中的 swap 行）
sudo swapoff -a

# 2. 或者：鎖定記憶體（需搭配 systemd override）
#    elasticsearch.yml 加入 bootstrap.memory_lock: true 後執行：
sudo systemctl edit elasticsearch
# 在編輯器中加入：
# [Service]
# LimitMEMLOCK=infinity

# 3. 非套件安裝（tar／Docker 主機）才需要手動設定 vm.max_map_count
echo "vm.max_map_count=262144" | sudo tee /etc/sysctl.d/99-elasticsearch.conf
sudo sysctl --system

# 4. 確認時間同步
timedatectl status | grep -i synchronized
```

> ⚠️ **v2.0 更正**：v1.0 以 `/etc/security/limits.conf` 調整 nofile。以 systemd 啟動的服務**不會讀取** `limits.conf`，必須用 `systemctl edit` 建立 override；套件安裝的預設值已足夠，通常不需修改。

---

### 3.3 Elasticsearch 安裝

#### 3.3.1 RPM 安裝（RHEL 系列）

```bash
# 1. 匯入 GPG Key
sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

# 2. 建立 9.x Repo 檔案（預設停用，安裝時才指定啟用，避免 dnf update 意外升級）
sudo tee /etc/yum.repos.d/elasticsearch.repo << 'EOF'
[elasticsearch]
name=Elasticsearch repository for 9.x packages
baseurl=https://artifacts.elastic.co/packages/9.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
EOF

# 3. 安裝指定版本（安裝輸出會顯示 elastic 使用者的初始密碼，請立即保存到密碼保管庫）
sudo dnf install -y --enablerepo=elasticsearch elasticsearch-9.5.4

# 4. 啟動服務
sudo systemctl daemon-reload
sudo systemctl enable --now elasticsearch
```

#### 3.3.2 DEB 安裝（Ubuntu／Debian）

```bash
# 1. 匯入 GPG Key
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

# 2. 新增 9.x Repository
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" \
  | sudo tee /etc/apt/sources.list.d/elastic-9.x.list

# 3. 安裝指定版本並鎖定，避免 apt upgrade 意外升級
sudo apt-get update && sudo apt-get install -y elasticsearch=9.5.4
sudo apt-mark hold elasticsearch

# 4. 啟動服務
sudo systemctl daemon-reload
sudo systemctl enable --now elasticsearch
```

> ⚠️ **v2.0 更正**：v1.0 使用 `packages/8.x` 套件庫且未鎖定版本。正式環境應**固定版本**並以變更管理流程升級，避免例行 OS 更新時連帶升級 Elasticsearch。

#### 3.3.3 自動安全設定（Security Auto-configuration）

以 RPM／DEB 首次安裝時，Elasticsearch 會自動完成下列設定：

| 自動產生項目 | 位置 | 說明 |
| --- | --- | --- |
| `elastic` 超級使用者密碼 | 安裝輸出（只顯示一次） | 遺失可用 `elasticsearch-reset-password` 重設 |
| HTTP 層 CA 與憑證 | `/etc/elasticsearch/certs/http_ca.crt`、`http.p12` | Client 需信任 `http_ca.crt` |
| Transport 層憑證 | `/etc/elasticsearch/certs/transport.p12` | 節點間 TLS |
| 安全設定 | `elasticsearch.yml` 末段的 `xpack.security.*` 區塊 | 請勿手動刪除 |
| Keystore 密碼項目 | `elasticsearch-keystore` | 存放憑證密碼 |

```bash
# 遺失 elastic 密碼時重設（-i 為互動輸入自訂密碼）
sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -i
```

> 💡 **建議**：自動產生的自簽 CA 適合快速建置；正式環境建議改用企業 PKI 簽發的憑證（見 [9.1.3 TLS 憑證規劃](#913-tls-憑證規劃)）。

#### 3.3.4 加入其他節點（Enrollment Token）

```bash
# 在既有節點：產生節點加入用的 Enrollment Token（有效 30 分鐘）
sudo /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node

# 在既有節點：確認 elasticsearch.yml 中的 transport.host 綁定到可被其他節點連線的介面
#   transport.host: 0.0.0.0

# 在新節點：安裝套件後「啟動前」執行重新設定
sudo /usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <token>

# 在新節點：啟動
sudo systemctl enable --now elasticsearch
```

> ⚠️ **實務注意**：以 Enrollment Token 加入的節點共用第一個節點自動產生的 CA。大型叢集若採企業 PKI 與固定的 `discovery.seed_hosts`，請改用 [4.1.2](#412-elasticsearchyml-範例多節點) 的明確設定方式，不要混用。

#### 3.3.5 Docker 快速安裝（單節點、啟用安全性）

```bash
# 建立網路
docker network create elastic

# 啟動 Elasticsearch（-it 前景執行，以便看到 elastic 密碼與 Kibana Enrollment Token）
docker run --name es01 --net elastic -p 127.0.0.1:9200:9200 -it -m 2GB \
  docker.elastic.co/elasticsearch/elasticsearch:9.5.4

# 另開終端：複製 CA 憑證到本機
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
```

> ⚠️ **v2.0 更正**：v1.0 的 Docker 範例以 `xpack.security.enabled=false` 關閉安全性並對外開放 9200。關閉安全性僅可用於隔離的本機實驗，**任何共用或連網環境都不得關閉**；埠號也應只綁定 `127.0.0.1`。
>
> 💡 **建議**：只想在筆電快速體驗時，可使用官方的 `curl -fsSL https://elastic.co/start-local | sh` 腳本一次啟動 Elasticsearch 與 Kibana（僅限本機開發）。

#### 3.3.6 安裝後驗證

```bash
# 檢查服務狀態
sudo systemctl status elasticsearch --no-pager

# 以 HTTPS + CA + 帳密驗證（9.x 預設）
export ELASTIC_PASSWORD='<安裝時顯示的密碼>'
sudo curl --cacert /etc/elasticsearch/certs/http_ca.crt \
  -u "elastic:${ELASTIC_PASSWORD}" "https://localhost:9200/_cluster/health?pretty"
```

預期輸出（單節點）：

```json
{
  "cluster_name" : "elasticsearch",
  "status" : "green",
  "number_of_nodes" : 1,
  "unassigned_shards" : 0
}
```

> ⚠️ **v2.0 更正**：v1.0 以 `curl localhost:9200` 驗證。9.x 預設啟用 TLS 與認證，未帶 `https://`、CA 與帳密的請求會失敗。

---

### 3.4 Kibana 安裝

#### 3.4.1 套件安裝

```bash
# RHEL 系列（沿用 3.3.1 建立的 elasticsearch.repo）
sudo dnf install -y --enablerepo=elasticsearch kibana-9.5.4

# Ubuntu／Debian（沿用 3.3.2 的 Repository）
sudo apt-get install -y kibana=9.5.4 && sudo apt-mark hold kibana
```

#### 3.4.2 以 Enrollment Token 連線 Elasticsearch

```bash
# 1. 在 Elasticsearch 節點產生 Kibana 用的 Enrollment Token
sudo /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

# 2. 在 Kibana 主機執行設定（自動寫入 elasticsearch.hosts、CA 與 service account token）
sudo /usr/share/kibana/bin/kibana-setup --enrollment-token <token>

# 3. 啟動
sudo systemctl enable --now kibana
```

> 💡 **建議**：Enrollment 會讓 Kibana 以 `elastic/kibana` **Service Account Token** 連線 Elasticsearch，比 v1.0 在 `kibana.yml` 寫入 `kibana_system` 明文密碼更安全。

#### 3.4.3 設定加密金鑰

Kibana 需要固定的加密金鑰來保護 Saved Objects 中的機密（例如 Connector 的密碼）、Session 與報表；未設定時每次重啟會產生暫時金鑰，導致告警 Connector 失效。

```bash
# 產生三組金鑰（輸出可直接貼入 kibana.yml）
sudo /usr/share/kibana/bin/kibana-encryption-keys generate -q
```

```yaml
# /etc/kibana/kibana.yml（多台 Kibana 必須使用相同的值）
xpack.encryptedSavedObjects.encryptionKey: "<32 字元以上>"
xpack.reporting.encryptionKey: "<32 字元以上>"
xpack.security.encryptionKey: "<32 字元以上>"
```

> ⚠️ **實務注意**：建議以 `kibana-keystore add` 存放金鑰，而非明文寫在 `kibana.yml`。`encryptedSavedObjects` 的金鑰一旦遺失，已加密的 Connector 機密將無法解密。

#### 3.4.4 安裝驗證

```bash
# 檢查服務狀態
sudo systemctl status kibana --no-pager

# 檢查整體狀態（available 表示正常）
curl -s -u "elastic:${ELASTIC_PASSWORD}" http://localhost:5601/api/status | jq '.status.overall.level'

# 開啟瀏覽器：http://<kibana-host>:5601（正式環境請啟用 HTTPS，見 4.3.1）
```

---

### 3.5 Logstash 安裝

#### 3.5.1 套件安裝

```bash
# RHEL 系列
sudo dnf install -y --enablerepo=elasticsearch logstash-9.5.4

# Ubuntu／Debian
sudo apt-get install -y logstash=1:9.5.4-1 && sudo apt-mark hold logstash
```

> ⚠️ **實務注意**：Logstash DEB 套件版本字串帶有 epoch（例如 `1:9.5.4-1`），請先以 `apt-cache madison logstash` 確認可用版本字串。

#### 3.5.2 建立寫入用的角色與 API Key

Logstash 不應使用 `elastic` 超級使用者寫入。以下建立最小權限的 API Key（在 Kibana **Dev Tools** 執行）：

```text
POST /_security/api_key
{
  "name": "logstash-writer",
  "role_descriptors": {
    "logstash_writer": {
      "cluster": ["monitor", "manage_index_templates", "manage_ilm"],
      "indices": [
        {
          "names": ["logs-*"],
          "privileges": ["auto_configure", "create_doc", "view_index_metadata"]
        }
      ]
    }
  }
}
```

回應中的 `id` 與 `api_key` 以 `id:api_key` 格式提供給 Logstash（`encoded` 欄位是 Base64 版本，供 HTTP Header 使用）。

> 💡 **建議**：Logstash 只寫入 Data Stream 時，`create_doc` + `auto_configure` 已足夠；若 Logstash 不需管理範本（`manage_template => false`），可再移除 `manage_index_templates` 與 `manage_ilm`。

#### 3.5.3 建立基本 Pipeline 並測試

```bash
# 1. 以 Logstash Keystore 保存 API Key（避免明文）
sudo -u logstash /usr/share/logstash/bin/logstash-keystore --path.settings /etc/logstash create
sudo -u logstash /usr/share/logstash/bin/logstash-keystore --path.settings /etc/logstash add ES_API_KEY

# 2. 複製 Elasticsearch CA
sudo mkdir -p /etc/logstash/certs
sudo cp /etc/elasticsearch/certs/http_ca.crt /etc/logstash/certs/   # 不同主機時以 scp 複製
sudo chown -R logstash:logstash /etc/logstash/certs

# 3. 建立基本設定檔
sudo tee /etc/logstash/conf.d/basic.conf << 'EOF'
input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["https://es-node-01:9200"]
    api_key => "${ES_API_KEY}"
    ssl_certificate_authorities => ["/etc/logstash/certs/http_ca.crt"]
    data_stream => "true"
    data_stream_type => "logs"
    data_stream_dataset => "generic"
    data_stream_namespace => "default"
  }
}
EOF

# 4. 以 logstash 使用者測試設定檔語法（9.0 起預設禁止以 root 執行）
sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash \
  --config.test_and_exit -f /etc/logstash/conf.d/basic.conf

# 5. 啟動服務
sudo systemctl enable --now logstash
```

> ⚠️ **v2.0 更正**：v1.0 以 `sudo /usr/share/logstash/bin/logstash --config.test_and_exit` 測試。Logstash 9.0 起 `allow_superuser` 預設為 `false`，以 root 執行會直接拒絕啟動；應以 `sudo -u logstash` 執行並指定 `--path.settings`。v1.0 的 `index => "logs-%{+YYYY.MM.dd}"` 每日索引寫法也已改為 Data Stream。

#### 3.5.4 Docker 安裝

```bash
mkdir -p ~/logstash/pipeline
cat > ~/logstash/pipeline/logstash.conf << 'EOF'
input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["https://es01:9200"]
    api_key => "${ES_API_KEY}"
    ssl_certificate_authorities => ["/usr/share/logstash/config/certs/http_ca.crt"]
    data_stream => "true"
  }
}
EOF

docker run -d --name logstash --net elastic -p 5044:5044 \
  -e ES_API_KEY='<id:api_key>' \
  -v ~/logstash/pipeline:/usr/share/logstash/pipeline:ro \
  -v "$PWD/http_ca.crt:/usr/share/logstash/config/certs/http_ca.crt:ro" \
  docker.elastic.co/logstash/logstash:9.5.4
```

> 📌 **8.19 差異**：Logstash 9.0 起官方映像改以 UBI9 為基底（8.x 為 Ubuntu），若自建衍生映像使用 `apt-get` 需改為 `microdnf`。

#### 3.5.5 安裝驗證

```bash
# 檢查服務狀態與 Log
sudo systemctl status logstash --no-pager
sudo tail -f /var/log/logstash/logstash-plain.log

# Monitoring API（預設只綁定 127.0.0.1:9600）
curl -s "localhost:9600/_node/stats/pipelines?pretty" | jq '.pipelines | keys'
```

---

### 3.6 Filebeat 安裝

> 🆕 **v2.0 新增**

```bash
# RHEL 系列
sudo dnf install -y --enablerepo=elasticsearch filebeat-9.5.4

# Ubuntu／Debian
sudo apt-get install -y filebeat=9.5.4 && sudo apt-mark hold filebeat

# 驗證設定與輸出連線
sudo filebeat test config -c /etc/filebeat/filebeat.yml
sudo filebeat test output -c /etc/filebeat/filebeat.yml

# 啟動
sudo systemctl enable --now filebeat
```

> ⚠️ **實務注意**：Filebeat 9.x 只要設定檔中出現已棄用的 `log` 或 `container` input，就會**拒絕啟動**；請直接使用 `filestream` input（設定範例見 [5.3.2](#532-步驟-2filebeat-filestream-設定)）。

---

### 3.7 Docker Compose 開發環境

> 🆕 **v2.0 新增**

以下為「啟用安全性、HTTP 不加密」的單節點開發環境，適合開發人員本機練習 Pipeline 與查詢。**不可用於正式環境**。

```bash
# .env
STACK_VERSION=9.5.4
ELASTIC_PASSWORD=ChangeMe_Elastic_123
KIBANA_PASSWORD=ChangeMe_Kibana_123
KIBANA_ENCRYPTION_KEY=ReplaceWithA32CharOrLongerRandomString
```

```yaml
# docker-compose.yml
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}
    environment:
      - node.name=es01
      - cluster.name=elk-dev
      - discovery.type=single-node
      - ELASTIC_PASSWORD=${ELASTIC_PASSWORD}
      - xpack.security.enabled=true
      - xpack.security.http.ssl.enabled=false   # 僅限本機開發
      - xpack.license.self_generated.type=basic
      - ES_JAVA_OPTS=-Xms1g -Xmx1g
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata01:/usr/share/elasticsearch/data
    ports:
      - "127.0.0.1:9200:9200"
    healthcheck:
      test: ["CMD-SHELL", "curl -s -u elastic:${ELASTIC_PASSWORD} http://localhost:9200/_cluster/health | grep -qE '\"status\":\"(green|yellow)\"'"]
      interval: 10s
      timeout: 10s
      retries: 30

  setup:
    image: docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}
    depends_on:
      es01:
        condition: service_healthy
    command: >
      bash -c '
        until curl -s -X POST -u "elastic:${ELASTIC_PASSWORD}"
          -H "Content-Type: application/json"
          http://es01:9200/_security/user/kibana_system/_password
          -d "{\"password\":\"${KIBANA_PASSWORD}\"}" | grep -q "^{}"; do sleep 5; done;
        echo "kibana_system password set";
      '

  kibana:
    image: docker.elastic.co/kibana/kibana:${STACK_VERSION}
    depends_on:
      setup:
        condition: service_completed_successfully
    environment:
      - SERVERNAME=kibana
      - ELASTICSEARCH_HOSTS=http://es01:9200
      - ELASTICSEARCH_USERNAME=kibana_system
      - ELASTICSEARCH_PASSWORD=${KIBANA_PASSWORD}
      - XPACK_ENCRYPTEDSAVEDOBJECTS_ENCRYPTIONKEY=${KIBANA_ENCRYPTION_KEY}
    ports:
      - "127.0.0.1:5601:5601"

  logstash:
    image: docker.elastic.co/logstash/logstash:${STACK_VERSION}
    depends_on:
      es01:
        condition: service_healthy
    environment:
      - ELASTIC_PASSWORD=${ELASTIC_PASSWORD}
    volumes:
      - ./pipeline:/usr/share/logstash/pipeline:ro
    ports:
      - "127.0.0.1:5044:5044"

volumes:
  esdata01:
```

```ruby
# ./pipeline/logstash.conf（開發環境方便起見使用 elastic 帳號，正式環境請改用 API Key）
input {
  beats { port => 5044 }
}

output {
  elasticsearch {
    hosts => ["http://es01:9200"]
    user => "elastic"
    password => "${ELASTIC_PASSWORD}"
    data_stream => "true"
  }
}
```

```bash
docker compose up -d
docker compose ps
# 瀏覽 http://localhost:5601，以 elastic / ${ELASTIC_PASSWORD} 登入
```

> ⚠️ **實務注意**：Compose 檔案已不需要 `version:` 欄位（Docker Compose v2 會忽略並提出警告）。Kibana 不允許以 `elastic` 超級使用者連線 Elasticsearch，必須使用 `kibana_system` 或 Service Account Token。

---

### 3.8 常見安裝問題排除

#### 3.8.1 問題一：Elasticsearch 無法啟動

```bash
# 查看錯誤日誌
sudo journalctl -u elasticsearch --no-pager -n 100
sudo tail -n 100 /var/log/elasticsearch/<cluster_name>.log
```

| 錯誤訊息（節錄） | 原因 | 解決方式 |
| --- | --- | --- |
| `max virtual memory areas vm.max_map_count [65530] is too low` | 非套件安裝未調整 | 依 [3.2](#32-系統前置調校) 設定 `vm.max_map_count` |
| `memory locking requested ... but memory is not locked` | 啟用 `memory_lock` 但未設定 `LimitMEMLOCK` | `systemctl edit elasticsearch` 加入 `LimitMEMLOCK=infinity` |
| `the default discovery settings are unsuitable for production use` | 多節點未設定 discovery | 設定 `discovery.seed_hosts` 與 `cluster.initial_master_nodes` |
| `AccessDeniedException: /var/lib/elasticsearch` | 資料目錄權限錯誤 | `chown -R elasticsearch:elasticsearch` 資料與 Log 目錄 |
| `OutOfMemoryError` 或啟動即被 OOM Killer 終止 | 手動 Heap 設定過大或主機記憶體不足 | 移除手動 Heap 設定，改用自動 Heap（見 [4.1.3](#413-jvm-heap-設定)） |

> ⚠️ **v2.0 更正**：v1.0 建議直接修改 `/etc/elasticsearch/jvm.options` 設定 Heap。官方不建議修改該檔案；若需手動設定，應在 `/etc/elasticsearch/jvm.options.d/` 下新增 `*.options` 檔案。

#### 3.8.2 問題二：Logstash Pipeline 錯誤

```bash
# 以 logstash 使用者測試設定檔語法
sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash \
  --config.test_and_exit -f /etc/logstash/conf.d/

# 查看詳細錯誤（暫時調高 Log 等級，不需重啟）
curl -s -X PUT "localhost:9600/_node/logging?pretty" -H 'Content-Type: application/json' \
  -d '{ "logger.logstash.outputs.elasticsearch" : "DEBUG" }'
```

| 常見錯誤 | 原因 | 解決方式 |
| --- | --- | --- |
| `Unknown setting 'ssl' for beats` | 9.0 已移除舊 SSL 選項 | 改用 `ssl_enabled` 等新選項（見 [4.2.4](#424-input-設定範例)） |
| `Logstash cannot be run as superuser` | 以 root 執行 | 改用 `sudo -u logstash`，不要設定 `allow_superuser: true` |
| `PKIX path building failed` | 未信任 Elasticsearch CA | 設定 `ssl_certificate_authorities` |
| `403 ... unauthorized for API key` | API Key 權限不足 | 檢查角色是否包含 `create_doc`、`auto_configure` |

#### 3.8.3 問題三：Kibana 無法連線 Elasticsearch

```bash
# 檢查 Elasticsearch 是否正常（帶 CA 與帳密）
curl --cacert /etc/elasticsearch/certs/http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" https://es-node-01:9200

# 檢查 Kibana Log（9.x 預設輸出到 /var/log/kibana/kibana.log）
sudo tail -n 100 /var/log/kibana/kibana.log

# 確認連線設定
sudo grep -E '^elasticsearch\.' /etc/kibana/kibana.yml
```

| 錯誤訊息（節錄） | 原因 | 解決方式 |
| --- | --- | --- |
| `self-signed certificate in certificate chain` | Kibana 未信任 ES 的 CA | 設定 `elasticsearch.ssl.certificateAuthorities` |
| `Unable to retrieve version information from Elasticsearch nodes` | 位址、防火牆或 TLS 設定錯誤 | 檢查 `elasticsearch.hosts` 是否為 `https://` 與連線可達性 |
| `value of "elastic" is forbidden` | 以 `elastic` 超級使用者連線 | 改用 Enrollment（Service Account Token）或 `kibana_system` |
| `[security_exception] unable to authenticate user [kibana_system]` | `kibana_system` 密碼未設定或錯誤 | `elasticsearch-reset-password -u kibana_system` |

#### 3.8.4 問題四：磁碟空間不足

```bash
# 檢查各節點磁碟使用
curl -s --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" \
  "https://localhost:9200/_cat/allocation?v&h=node,disk.percent,disk.used,disk.avail,shards"
```

> ⚠️ **實務注意**：磁碟達 95%（flood stage）時，Elasticsearch 會將相關索引設為唯讀，寫入全部失敗。不要手動 `DELETE` Data Stream 的 backing index 了事，應先依 [13.3 磁碟水位與唯讀索引](#133-磁碟水位與唯讀索引) 處理，並檢討 ILM 保存期限。

#### 3.8.5 快速診斷腳本

```bash
#!/bin/bash
# elk-health-check.sh
# 使用方式：ES_URL=https://es-node-01:9200 ES_CA=/etc/elasticsearch/certs/http_ca.crt \
#           ES_AUTH="elastic:密碼" KB_URL=http://localhost:5601 ./elk-health-check.sh
set -u
ES_URL="${ES_URL:-https://localhost:9200}"
ES_CA="${ES_CA:-/etc/elasticsearch/certs/http_ca.crt}"
KB_URL="${KB_URL:-http://localhost:5601}"

es() { curl -s --cacert "$ES_CA" -u "$ES_AUTH" "$ES_URL$1"; }

echo "=== Elasticsearch ==="
es "/_cluster/health?pretty" || echo "ES not responding"
es "/_health_report?pretty" | jq '{status, indicators: (.indicators | map_values(.status))}' 2>/dev/null

echo ""
echo "=== Logstash ==="
curl -s "localhost:9600/_node/stats/pipelines" | jq '.pipelines | map_values(.events)' 2>/dev/null \
  || echo "Logstash API not responding (only bound to 127.0.0.1 by default)"

echo ""
echo "=== Kibana ==="
curl -s -u "$ES_AUTH" "$KB_URL/api/status" | jq -r '.status.overall.level' 2>/dev/null \
  || echo "Kibana not responding"

echo ""
echo "=== Disk / Memory ==="
df -h | grep -E "Filesystem|/var/lib/elasticsearch|/$"
free -h
```

---

### 3.9 💡 本章實務建議

- 所有元件安裝**完全相同的版本**（9.5.4），並以 `--enablerepo`／`apt-mark hold` 鎖定，避免意外升級。
- 保留 9.x 預設的自動安全設定；所有範例改用 `https://` + CA + API Key／Service Account Token。
- 系統調校以 systemd override 為準，不要依賴 `limits.conf`；Heap 預設交由 Elasticsearch 自動計算。
- Logstash 以 `logstash` 使用者執行與測試，機密放入 Keystore。
- Filebeat 9.x 只使用 `filestream` input；Docker Compose 環境僅供本機開發。

---

## 第四章：系統設定

### 4.1 Elasticsearch 設定

#### 4.1.1 設定檔位置與設定層級

```text
/etc/elasticsearch/elasticsearch.yml        # 節點層級（靜態）設定
/etc/elasticsearch/jvm.options              # JVM 預設值（請勿修改）
/etc/elasticsearch/jvm.options.d/*.options  # 自訂 JVM 設定（Heap、GC Log 等）
/etc/elasticsearch/log4j2.properties        # Log 設定
/etc/elasticsearch/certs/                   # 自動產生或自行放置的憑證
```

Elasticsearch 的設定分為三個層級，**放錯位置會導致節點無法啟動**：

| 層級 | 設定方式 | 範例 | 生效時機 |
| --- | --- | --- | --- |
| 節點（靜態） | `elasticsearch.yml` | `cluster.name`、`node.roles`、`path.data`、`xpack.security.*` | 重啟節點 |
| 叢集（動態） | `PUT _cluster/settings` | `cluster.routing.allocation.*`、`indices.recovery.max_bytes_per_sec` | 立即 |
| 索引 | Index Template 或 `PUT <index>/_settings` | `index.refresh_interval`、`index.number_of_replicas` | 新索引或立即 |

> ⚠️ **v2.0 更正**：v1.0 在 `elasticsearch.yml` 中設定 `index.refresh_interval`。自 5.0 起索引層級設定**不可**放在 `elasticsearch.yml`，節點會因 unknown／invalid setting 無法啟動；應改在 Index Template 設定（見 [7.3.1](#731-寫入效能調校)）。

#### 4.1.2 elasticsearch.yml 範例（多節點）

```yaml
# /etc/elasticsearch/elasticsearch.yml（Hot Data 節點範例）

# ======================== 叢集與節點 ========================
cluster.name: prod-elk-cluster
node.name: es-hot-01
node.roles: [ data_hot, data_content, ingest ]
node.attr.zone: zone-a

# ======================== 路徑 ========================
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch

# ======================== 網路 ========================
network.host: 10.0.1.21
http.port: 9200
transport.port: 9300

# ======================== 叢集發現 ========================
discovery.seed_hosts:
  - 10.0.1.11:9300
  - 10.0.1.12:9300
  - 10.0.1.13:9300
# 只在「第一次組成叢集」時於 master 候選節點設定，叢集成立後必須移除
# cluster.initial_master_nodes: [ es-master-01, es-master-02, es-master-03 ]

# ======================== 記憶體 ========================
bootstrap.memory_lock: true

# ======================== Shard 配置 ========================
cluster.routing.allocation.awareness.attributes: zone

# ======================== 安全性（企業 PKI 憑證） ========================
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: full
xpack.security.transport.ssl.keystore.path: certs/transport.p12
xpack.security.transport.ssl.truststore.path: certs/transport.p12
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.keystore.path: certs/http.p12
```

| 節點類型 | `node.roles` 範例 |
| --- | --- |
| 專用 Master | `[ master ]` |
| Hot Data | `[ data_hot, data_content, ingest ]` |
| Warm Data | `[ data_warm ]` |
| Cold Data | `[ data_cold ]` |
| Coordinating only | `[ ]` |
| 單節點（開發） | 不設定（預設擁有所有角色）並設 `discovery.type: single-node` |

> ⚠️ **v2.0 更正**：v1.0 範例將 `xpack.security.http.ssl.enabled` 設為 `false` 並註明「內網可關閉」。內網同樣存在橫向移動風險，且 Log 常含個資，HTTP 層 TLS 應一律開啟。憑證的 keystore 密碼請以 `elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password` 等指令存放。

#### 4.1.3 JVM Heap 設定

9.x 預設會依節點角色與主機記憶體**自動決定 Heap 大小**，官方建議大多數正式環境直接採用預設值。

| 情境 | 建議 |
| --- | --- |
| 一般情況 | 不設定，交由自動計算（Data 節點約為記憶體的一半） |
| 必須手動設定（例如與其他程序共用主機） | 在 `jvm.options.d/heap.options` 設定，`-Xms` 與 `-Xmx` 相同 |
| 手動設定上限 | 不超過實體記憶體 50%，且低於 Compressed OOPs 門檻（多數系統約 26–30 GB） |
| 容器環境 | 以容器記憶體限制計算；ECK 以 Pod `resources.limits.memory` 自動推導 |

```bash
# /etc/elasticsearch/jvm.options.d/heap.options（僅在需要手動設定時建立）
-Xms16g
-Xmx16g
```

```bash
# 確認 Compressed OOPs 是否啟用（啟動 Log 會顯示）
sudo grep "compressed ordinary object pointers" /var/log/elasticsearch/prod-elk-cluster.log
# 預期：heap size [16gb], compressed ordinary object pointers [true]
```

| 實體記憶體 | 自動 Heap（約略） | 說明 |
| --- | --- | --- |
| 8 GB | 約 4 GB | 開發環境 |
| 16 GB | 約 8 GB | 小型生產 |
| 32 GB | 約 16 GB | 中型生產 |
| 64 GB 以上 | 約 31 GB 以下 | 大型生產；剩餘記憶體作為檔案系統快取 |

> ⚠️ **v2.0 更正**：v1.0 建議「一律手動設為實體記憶體 50%、不超過 31 GB」。31 GB 並非所有平台都能維持 Compressed OOPs；手動設定時應以啟動 Log 確認，且官方建議優先使用自動 Heap。

#### 4.1.4 Index Template 與 Component Template

9.x 內建名為 `logs` 的 Index Template（priority 100，pattern `logs-*-*`），由以下 Component Template 組成：

| Component Template | 內容 | 可否修改 |
| --- | --- | --- |
| `logs@mappings` | `data_stream.*` 欄位、關閉日期自動偵測 | ❌ 受管理，升級會覆寫 |
| `logs@settings` | ILM 政策 `logs`、`best_compression`、`ignore_malformed`、預設 ingest pipeline `logs@default-pipeline`、啟用 failure store | ❌ |
| `ecs@mappings` | 依 ECS 欄位名稱自動對應型別的 dynamic templates | ❌ |
| `logs@custom` | 使用者自訂（預設不存在） | ✅ 所有 `logs-*-*` 共用的客製化放這裡 |

**方式一：全域客製化（建議優先使用）**

```text
PUT _component_template/logs@custom
{
  "template": {
    "settings": {
      "index.refresh_interval": "10s"
    },
    "mappings": {
      "properties": {
        "app": {
          "properties": {
            "order_id":  { "type": "keyword" },
            "user_id":   { "type": "keyword" },
            "amount":    { "type": "scaled_float", "scaling_factor": 100 }
          }
        }
      }
    }
  }
}
```

**方式二：特定應用的專屬範本（需要不同保存期限或 Shard 數時）**

```text
PUT _index_template/logs-orderservice
{
  "index_patterns": ["logs-orderservice-*"],
  "data_stream": {},
  "priority": 200,
  "composed_of": ["logs@mappings", "logs@settings", "logs@custom", "ecs@mappings"],
  "ignore_missing_component_templates": ["logs@custom"],
  "template": {
    "settings": {
      "index.lifecycle.name": "logs-orderservice-policy",
      "index.number_of_shards": 2
    }
  },
  "_meta": { "owner": "order-team", "description": "訂單服務 Log，保存 180 天" }
}
```

> ⚠️ **v2.0 更正**：v1.0 建立 pattern 為 `logs-*`、priority 0、使用 `index.lifecycle.rollover_alias` 的範本。這與內建 `logs` 範本重疊（實際會被 priority 100 的內建範本蓋過），且 `rollover_alias` 是舊式別名 rollover 的設定，Data Stream 不需要。自訂範本的 priority 必須**大於 100**，並沿用 `logs@*` Component Template。

#### 4.1.5 Shard 數量規劃

```text
┌─────────────────────────────────────────────────────────────┐
│                    Shard 規劃建議（9.x）                     │
├─────────────────────────────────────────────────────────────┤
│  • 單一 Shard 建議大小：10–50 GB；文件數 < 2 億               │
│  • Data Stream 以 rollover 控制大小，不需預先切每日索引        │
│  • 內建 logs ILM：primary shard 50 GB 或 30 天 rollover       │
│  • Primary Shard 數 ≈ 每次 rollover 前的資料量 ÷ 30 GB         │
│  • cluster.max_shards_per_node 預設 1000，勿以調高解決問題     │
│                                                             │
│  範例：單一服務每日 100 GB，每日 rollover                    │
│  → 每個 backing index 約 100 GB → 3–4 個 Primary Shard       │
│  範例：小型服務每日 1 GB → 1 個 Primary Shard，依大小 rollover │
└─────────────────────────────────────────────────────────────┘
```

> 💡 **建議**：小服務過多、每個都切多個 Shard，是「Shard 爆量」最常見的原因。小流量的 Data Stream 一律 1 個 Primary Shard，讓 rollover 依大小（而非每日）觸發。

#### 4.1.6 Ingest Pipeline

> 🆕 **v2.0 新增**

Ingest Pipeline 在 Elasticsearch 內執行輕量解析，適合「Filebeat／Agent 直送 Elasticsearch、不經 Logstash」的架構。

| 套用方式 | 範圍 | 說明 |
| --- | --- | --- |
| 建立名為 `logs@custom` 的 Ingest Pipeline | 所有 `logs-*-*` | 內建 `logs@default-pipeline` 會先補 `@timestamp`，再呼叫 `logs@custom`（不存在時略過） |
| 寫入端指定 `pipeline` | 單一來源 | Filebeat `output.elasticsearch.pipeline`、Logstash `pipeline =>` |
| 範本設定 `index.final_pipeline` | 特定 Data Stream | 在所有其他 pipeline 之後執行，適合強制遮蔽 |

```text
PUT _ingest/pipeline/app-plaintext-logs
{
  "description": "解析 Spring Boot 純文字 Log",
  "processors": [
    {
      "grok": {
        "field": "message",
        "patterns": [
          "%{TIMESTAMP_ISO8601:_tmp.ts}\\s+%{LOGLEVEL:log.level}\\s+%{NUMBER:process.pid:long}\\s+---\\s+\\[%{DATA:process.thread.name}\\]\\s+%{JAVACLASS:log.logger}\\s+:\\s+%{GREEDYDATA:_tmp.msg}"
        ]
      }
    },
    { "date": { "field": "_tmp.ts", "formats": ["ISO8601", "yyyy-MM-dd HH:mm:ss.SSS"], "timezone": "Asia/Taipei" } },
    { "set": { "field": "message", "copy_from": "_tmp.msg" } },
    { "remove": { "field": "_tmp", "ignore_missing": true } }
  ],
  "on_failure": [
    { "set": { "field": "event.kind", "value": "pipeline_error" } },
    { "set": { "field": "error.message", "value": "{{ _ingest.on_failure_message }}" } }
  ]
}
```

```text
# 以模擬 API 驗證，不寫入任何資料
POST _ingest/pipeline/app-plaintext-logs/_simulate
{
  "docs": [
    { "_source": { "message": "2026-09-30T14:30:00.123+08:00  INFO 12345 --- [main] c.c.o.OrderService : Order created" } }
  ]
}
```

> 💡 **建議**：最省事的做法是讓應用程式直接輸出 ECS JSON（見 [5.3.1](#531-步驟-1應用程式-log-設定)），Pipeline 只需處理例外情況。`date` processor 的 `timezone` 只在時間字串不含時區時才生效。複雜解析、跨來源 enrichment 或需要緩衝時，仍以 Logstash 為主（選型見 [5.2](#52-收集端選型)）。

---

### 4.2 Logstash 設定

#### 4.2.1 設定檔結構

```text
/etc/logstash/
├── logstash.yml           # 主設定
├── pipelines.yml          # Pipeline 定義（多 Pipeline）
├── jvm.options            # JVM 設定（Heap）
├── log4j2.properties      # Log 設定
├── logstash.keystore      # 機密（以 logstash-keystore 管理）
└── conf.d/                # Pipeline 設定檔目錄
    ├── 01-input.conf
    ├── 02-filter.conf
    └── 03-output.conf
/var/lib/logstash/
├── queue/                 # Persistent Queue
└── dead_letter_queue/     # DLQ
```

#### 4.2.2 logstash.yml 重要設定

| 設定 | 9.5 預設值 | 建議 |
| --- | --- | --- |
| `pipeline.workers` | CPU 核心數 | 一般維持預設；filter 很重時可略增 |
| `pipeline.batch.size` | 125 | 寫入 ES 為主時可調至 250–1000，需同步增加 Heap |
| `pipeline.batch.delay` | 50（ms） | 維持預設 |
| `queue.type` | `memory` | 正式環境建議 `persisted` |
| `queue.max_bytes` | `1024mb` | 依磁碟與可容忍中斷時間調整 |
| `dead_letter_queue.enable` | `false` | 建議 `true`，保存 mapping 錯誤等無法寫入的事件 |
| `api.http.host` | `127.0.0.1` | 需外部監控時再綁定內網位址並啟用 API 認證 |
| `api.http.port` | `9600-9700` | 維持預設 |
| `pipeline.ecs_compatibility` | `v8` | 維持預設，搭配 Data Stream |
| `pipeline.buffer.type` | `heap` | 維持預設 |
| `allow_superuser` | `false` | **不要**改為 `true` |
| `config.reload.automatic` | `false` | 開發環境可開啟；正式環境以部署流程控制 |

```yaml
# /etc/logstash/logstash.yml（正式環境範例）
node.name: logstash-01
path.data: /var/lib/logstash
path.logs: /var/log/logstash

pipeline.workers: 8
pipeline.batch.size: 500
pipeline.batch.delay: 50

queue.type: persisted
queue.max_bytes: 8gb

dead_letter_queue.enable: true
dead_letter_queue.max_bytes: 2gb

api.http.host: 127.0.0.1
```

```bash
# /etc/logstash/jvm.options（Heap：一般 4–8 GB，Xms 與 Xmx 相同，勿超過主機記憶體一半）
-Xms6g
-Xmx6g
```

> ⚠️ **v2.0 更正**：v1.0 在 `logstash.yml` 中設定 `output.elasticsearch.bulk_max_size: 5000`。這是 **Filebeat** 的設定，Logstash 沒有此選項；Logstash 的批次大小由 `pipeline.batch.size` 決定。

#### 4.2.3 pipelines.yml 與多 Pipeline

將不同來源拆成獨立 Pipeline，可隔離故障並分別調校。

```yaml
# /etc/logstash/pipelines.yml
- pipeline.id: beats-intake
  path.config: "/etc/logstash/conf.d/beats-intake.conf"
  pipeline.workers: 2

- pipeline.id: app-logs
  path.config: "/etc/logstash/conf.d/app-logs.conf"
  queue.type: persisted

- pipeline.id: audit-logs
  path.config: "/etc/logstash/conf.d/audit-logs.conf"
  queue.type: persisted
  queue.max_bytes: 16gb
```

```ruby
# beats-intake.conf：依來源分流（Pipeline-to-Pipeline）
input {
  beats {
    port => 5044
    ssl_enabled => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.pkcs8.key"
  }
}

output {
  if [fields][log_type] == "audit" {
    pipeline { send_to => ["audit-logs"] }
  } else {
    pipeline { send_to => ["app-logs"] }
  }
}
```

```ruby
# app-logs.conf
input {
  pipeline { address => "app-logs" }
}
# filter / output 略（見 4.2.5、4.2.6）
```

> ⚠️ **實務注意**：使用 `pipelines.yml` 時，以 `-f` 指定設定檔或 `--path.config` 會讓 Logstash 忽略 `pipelines.yml`。以 systemd 啟動時不要在 `startup.options` 加入 `-f`。

#### 4.2.4 Input 設定範例

```ruby
# 從 Filebeat 接收（TLS + 雙向驗證）
input {
  beats {
    port => 5044
    ssl_enabled => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.pkcs8.key"
    ssl_certificate_authorities => ["/etc/logstash/certs/ca.crt"]
    ssl_client_authentication => "required"
  }
}

# 從 Kafka 接收
input {
  kafka {
    bootstrap_servers => "kafka01:9093,kafka02:9093,kafka03:9093"
    topics => ["app-logs"]
    group_id => "logstash-app-logs"
    consumer_threads => 3
    codec => json
    security_protocol => "SSL"
    ssl_truststore_location => "/etc/logstash/certs/kafka-truststore.jks"
    ssl_truststore_password => "${KAFKA_TRUSTSTORE_PASSWORD}"
  }
}

# 從 TCP 接收（例如 Logback LogstashTcpSocketAppender 的 JSON Lines）
input {
  tcp {
    port => 5000
    codec => json_lines
    ssl_enabled => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.pkcs8.key"
  }
}
```

| v1.0／8.x 舊選項 | 9.x 新選項 | 適用 Plugin |
| --- | --- | --- |
| `ssl` | `ssl_enabled` | beats、tcp、http、elasticsearch 等 |
| `ssl_verify_mode` | `ssl_client_authentication`（`none`／`optional`／`required`） | beats、tcp、http |
| `cipher_suites` | `ssl_cipher_suites` | beats |
| `tls_min_version`／`tls_max_version` | `ssl_supported_protocols` | beats |
| `ssl_peer_metadata` | `enrich` 選項中的 `ssl_peer_metadata` | beats |

> ⚠️ **v2.0 更正**：v1.0 的 `ssl => false` 在 Logstash 9.0 已被移除，Pipeline 會因未知選項無法啟動。Kafka 範例的連接埠也改為 TLS 埠（9093）並加入 `security_protocol`。
>
> ⚠️ **實務注意**：beats input 的私鑰需為 **PKCS#8** 格式，可用 `openssl pkcs8 -topk8 -nocrypt -in logstash.key -out logstash.pkcs8.key` 轉換。

#### 4.2.5 Filter 設定範例

```ruby
# /etc/logstash/conf.d/02-filter.conf
filter {
  # 1. JSON 格式 Log（應用程式以 ECS JSON 輸出時，Filebeat 已解析，此段可省略）
  if [fields][log_format] == "json" {
    json {
      source => "message"
      skip_on_invalid_json => true
    }
  }

  # 2. 純文字 Log（Log4j2／Logback Pattern）——以 ECS 欄位名稱作為目標
  if [fields][log_format] == "plain" {
    grok {
      match => {
        "message" => "%{TIMESTAMP_ISO8601:[@metadata][ts]} %{LOGLEVEL:[log][level]} \[%{DATA:[process][thread][name]}\] %{JAVACLASS:[log][logger]} - %{GREEDYDATA:[@metadata][msg]}"
      }
      tag_on_failure => ["_grok_app_failure"]
    }

    date {
      match => [ "[@metadata][ts]", "yyyy-MM-dd HH:mm:ss.SSS", "ISO8601" ]
      target => "@timestamp"
      timezone => "Asia/Taipei"
    }

    if [@metadata][msg] {
      mutate { replace => { "message" => "%{[@metadata][msg]}" } }
    }
  }

  # 3. 補上環境資訊
  mutate {
    add_field => { "[service][environment]" => "production" }
  }

  # 4. 敏感資料遮蔽（完整規則見 9.4.1）
  mutate {
    gsub => [
      "message", "[A-Z][12]\d{8}", "[ID_MASKED]",
      "message", "\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b", "[CARD_MASKED]"
    ]
  }
}
```

> ⚠️ **v2.0 更正**：v1.0 以 `if [type] == "java-app"` 判斷來源。`type` 欄位源自已移除的 document type 概念，Filebeat 9.x 也不會自動產生；應改用 `fields.*`、`event.dataset` 或 `data_stream.dataset` 等明確欄位。暫存欄位放在 `[@metadata]` 下，不會被寫入 Elasticsearch，可省去 `remove_field`。

#### 4.2.6 Output 設定範例

```ruby
# /etc/logstash/conf.d/03-output.conf
output {
  elasticsearch {
    hosts => ["https://es-hot-01:9200", "https://es-hot-02:9200", "https://es-hot-03:9200"]
    api_key => "${ES_API_KEY}"
    ssl_certificate_authorities => ["/etc/logstash/certs/http_ca.crt"]

    # 寫入 Data Stream：logs-<dataset>-<namespace>
    data_stream => "true"
    data_stream_type => "logs"
    data_stream_dataset => "app"
    data_stream_namespace => "prod"
    # 事件本身帶有 data_stream.dataset 等欄位時，會優先依欄位自動路由
    data_stream_auto_routing => true
  }

  # 除錯用：只在開發環境開啟
  # stdout { codec => rubydebug { metadata => true } }
}
```

> ⚠️ **v2.0 更正**：v1.0 Output 使用 `document_type => "_doc"`、HTTP 明文位址與每日索引名稱。`document_type` 對 8.x 以上叢集已無作用且為棄用選項；`cacert`、`ssl`、`ssl_certificate_verification` 等舊 SSL 選項自 Elasticsearch output 12.0 起會讓 Plugin 無法啟動，應改用 `ssl_certificate_authorities`、`ssl_enabled`、`ssl_verification_mode`。

#### 4.2.7 Persistent Queue 與 Dead Letter Queue

> 🆕 **v2.0 新增**

| 機制 | 用途 | 注意事項 |
| --- | --- | --- |
| Persistent Queue（PQ） | Logstash 重啟或 ES 短暫不可用時，事件暫存在本機磁碟不遺失 | 佔用磁碟；`queue.max_bytes` 滿時會對上游施加背壓 |
| Dead Letter Queue（DLQ） | 保存 ES 回應 400／404（如 mapping 衝突）而無法寫入的事件 | 需定期檢視並重送，否則只是延後遺失 |

```ruby
# dlq-reprocess.conf：讀取 DLQ、修正後重新寫入
input {
  dead_letter_queue {
    path => "/var/lib/logstash/dead_letter_queue"
    pipeline_id => "app-logs"
    commit_offsets => true
  }
}

filter {
  # 例：mapping 衝突時將問題欄位改名後重送
  mutate { rename => { "[app][amount]" => "[app][amount_raw]" } }
}

output {
  elasticsearch {
    hosts => ["https://es-hot-01:9200"]
    api_key => "${ES_API_KEY}"
    ssl_certificate_authorities => ["/etc/logstash/certs/http_ca.crt"]
    data_stream => "true"
  }
}
```

#### 4.2.8 以 Keystore 管理機密

```bash
# 建立 Keystore 並設定保護密碼（密碼透過環境變數提供給 systemd 服務）
echo 'LOGSTASH_KEYSTORE_PASS=<keystore-password>' | sudo tee -a /etc/sysconfig/logstash   # Debian：/etc/default/logstash
sudo chmod 600 /etc/sysconfig/logstash
sudo -u logstash env LOGSTASH_KEYSTORE_PASS='<keystore-password>' \
  /usr/share/logstash/bin/logstash-keystore --path.settings /etc/logstash create

# 新增機密
sudo -u logstash env LOGSTASH_KEYSTORE_PASS='<keystore-password>' \
  /usr/share/logstash/bin/logstash-keystore --path.settings /etc/logstash add ES_API_KEY

# 在 Pipeline 中以 ${ES_API_KEY} 引用
```

#### 4.2.9 完整 Java 應用程式 Log Pipeline

```ruby
# /etc/logstash/conf.d/java-app-pipeline.conf
input {
  beats {
    port => 5044
    ssl_enabled => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.pkcs8.key"
  }
}

filter {
  # 多行 Stack Trace 已在 Filebeat 以 multiline parser 合併（見 5.3.2）
  grok {
    match => {
      "message" => "%{TIMESTAMP_ISO8601:[@metadata][ts]}\s+%{LOGLEVEL:[log][level]}\s+%{NUMBER:[process][pid]:int}\s+---\s+\[%{DATA:[process][thread][name]}\]\s+%{JAVACLASS:[log][logger]}\s+:\s+%{GREEDYDATA:[@metadata][msg]}"
    }
    tag_on_failure => ["_grok_springboot_failure"]
  }

  date {
    match => ["[@metadata][ts]", "yyyy-MM-dd HH:mm:ss.SSS", "ISO8601"]
    target => "@timestamp"
    timezone => "Asia/Taipei"
  }

  if [@metadata][msg] {
    mutate { replace => { "message" => "%{[@metadata][msg]}" } }
  }

  # 標記含例外的事件
  if [message] =~ /Exception|Error/ {
    mutate { add_tag => ["exception"] }
  }

  # 以 Filebeat 帶入的欄位決定 Data Stream 與服務名稱
  mutate {
    copy => {
      "[fields][app_name]" => "[service][name]"
      "[fields][env]"      => "[service][environment]"
    }
  }
  mutate {
    add_field => { "[data_stream][dataset]" => "%{[fields][app_name]}" }
  }
  # dataset 不可含 "-"，例如 order-service → order_service
  mutate { gsub => ["[data_stream][dataset]", "-", "_"] }
  # 移除收集端資訊前請確認不再需要（host.name 對排查很有用，建議保留）
  mutate { remove_field => ["[fields]", "[agent][ephemeral_id]"] }
}

output {
  elasticsearch {
    hosts => ["https://es-hot-01:9200", "https://es-hot-02:9200"]
    api_key => "${ES_API_KEY}"
    ssl_certificate_authorities => ["/etc/logstash/certs/http_ca.crt"]
    data_stream => "true"
    data_stream_namespace => "prod"
  }
}
```

> ⚠️ **實務注意**：`data_stream.dataset` 只能包含小寫英數、`_` 與 `.`，不可含 `-`（`-` 是 Data Stream 名稱的分隔字元）。應用程式名稱如 `order-service`，需在設定時改為 `order_service`。

---

### 4.3 Kibana 設定

#### 4.3.1 主設定檔

```yaml
# /etc/kibana/kibana.yml

# ======================== Server ========================
server.port: 5601
server.host: "0.0.0.0"
server.name: "kibana-prod-01"
server.publicBaseUrl: "https://kibana.company.com"   # 告警通知與報表中的連結會使用此網址

# ======================== HTTPS（直接對外或 LB 以 TLS 回源時） ========================
server.ssl.enabled: true
server.ssl.certificate: /etc/kibana/certs/kibana.crt
server.ssl.key: /etc/kibana/certs/kibana.key

# ======================== Elasticsearch 連線 ========================
# kibana-setup（Enrollment）會自動寫入 hosts、CA 與 service account token
elasticsearch.hosts: ["https://es-coord-01:9200", "https://es-coord-02:9200"]
elasticsearch.ssl.certificateAuthorities: ["/etc/kibana/certs/http_ca.crt"]
# elasticsearch.serviceAccountToken 建議以 kibana-keystore 存放

# ======================== 加密金鑰（以 kibana-keystore 存放，多台 Kibana 必須一致） ========================
# xpack.encryptedSavedObjects.encryptionKey
# xpack.reporting.encryptionKey
# xpack.security.encryptionKey

# ======================== Log ========================
logging:
  appenders:
    file:
      type: file
      fileName: /var/log/kibana/kibana.log
      layout:
        type: json
  root:
    appenders: [default, file]
    level: info

# ======================== 介面語系 ========================
# 可用值：en（預設）、zh-CN、ja-JP、fr-FR、de-DE
i18n.locale: "en"

# ======================== 逾時 ========================
elasticsearch.requestTimeout: 30000
```

> ⚠️ **v2.0 更正**：
>
> - v1.0 設定 `i18n.locale: "zh-TW"`。Kibana 9.5 只內建 `zh-CN`、`ja-JP`、`fr-FR`、`de-DE` 翻譯，**沒有繁體中文**；企業內部建議維持 `en` 或依使用者接受度採用 `zh-CN`。
> - v1.0 在 `kibana.yml` 設定 `server.defaultRoute`。該設定已於 8.0 移出 `kibana.yml`，改為 **Advanced Settings** 的 `defaultRoute`（見 [4.3.4](#434-advanced-settings)）。
> - v1.0 以 `elasticsearch.username`／`password` 明文連線；改用 Enrollment 產生的 Service Account Token 並存於 keystore。

#### 4.3.2 Data View 設定

> ⚠️ **v2.0 更正**：v1.0 標題為「Index Pattern」。自 8.0 起 Kibana 已更名為 **Data View**；Saved Objects 匯出時的型別名稱仍為 `index-pattern`。

透過 Kibana UI 設定：

1. 進入 **Stack Management** → **Data Views**
2. 點擊 **Create data view**
3. 設定：
   - Name：`App Logs（prod）`
   - Index pattern：`logs-*-prod`
   - Timestamp field：`@timestamp`
4. 點擊 **Save data view to Kibana**

或使用 API（需認證與 `kbn-xsrf` 標頭）：

```bash
curl -s -X POST "https://kibana.company.com/api/data_views/data_view" \
  -H "Authorization: ApiKey ${KIBANA_API_KEY}" \
  -H "kbn-xsrf: true" \
  -H "Content-Type: application/json" \
  -d '{
    "data_view": {
      "name": "App Logs（prod）",
      "title": "logs-*-prod",
      "timeFieldName": "@timestamp"
    }
  }'
```

#### 4.3.3 Spaces 與團隊隔離

> 🆕 **v2.0 新增**

| 做法 | 說明 |
| --- | --- |
| 每個團隊或產品線一個 Space | Dashboard、Saved Search、告警規則彼此隔離 |
| 角色指派 Space 權限 | 例如 `order-team` 只能在 `order` Space 使用 Discover／Dashboard |
| 資料權限仍由 Elasticsearch 角色控制 | Space 只隔離 Kibana 物件，**不能**取代索引權限 |

```bash
curl -s -X POST "https://kibana.company.com/api/spaces/space" \
  -H "Authorization: ApiKey ${KIBANA_API_KEY}" -H "kbn-xsrf: true" -H "Content-Type: application/json" \
  -d '{ "id": "order", "name": "訂單系統", "disabledFeatures": [] }'
```

#### 4.3.4 Advanced Settings

在 **Stack Management** → **Advanced Settings**（各 Space 可個別設定）：

| 設定 | 建議值 | 說明 |
| --- | --- | --- |
| `dateFormat:tz` | `Asia/Taipei` | 顯示時區（資料仍以 UTC 儲存） |
| `defaultRoute` | `/app/discover` | 進入 Kibana 的預設頁面（取代 v1.0 的 `server.defaultRoute`） |
| `dateFormat` | `YYYY-MM-DD HH:mm:ss.SSS` | 與應用程式 Log 格式一致，方便比對 |
| `observability:logSources` | `logs-*-*,logs-*` | Observability Logs 相關介面使用的資料來源 |

---

### 4.4 💡 本章實務建議

- 分清節點、叢集、索引三個設定層級；索引設定一律放在 Index／Component Template。
- 多節點以明確的 `discovery.seed_hosts` 與企業 PKI 憑證建置，`cluster.initial_master_nodes` 只在首次組成叢集時使用。
- Heap 優先採自動計算；手動設定時以啟動 Log 確認 Compressed OOPs。
- 客製 `logs-*-*` 先用 `logs@custom`；需要不同保存期限時再建 priority > 100 的專屬範本。
- Logstash 9.x：改用新 SSL 選項、Data Stream output、PQ + DLQ、Keystore；以 `[@metadata]` 存放暫存欄位。
- Kibana：Enrollment + Service Account Token、固定加密金鑰、語系只用支援的值、`defaultRoute` 改到 Advanced Settings。

---

## 第五章：三者如何串接

### 5.1 End-to-End 資料流

```mermaid
sequenceDiagram
    participant App as Application
    participant FB as Filebeat
    participant LS as Logstash
    participant ES as Elasticsearch
    participant K as Kibana
    participant User as 使用者

    App->>App: 寫入 ECS JSON Log 檔
    FB->>App: filestream 監控檔案變化
    FB->>LS: 傳送事件（Beats 5044 / TLS）
    LS->>LS: 解析、轉換、遮蔽、路由
    LS->>ES: Bulk 寫入 Data Stream（HTTPS 9200）
    ES->>ES: 依範本建立 backing index（LogsDB）
    User->>K: 開啟 Kibana（HTTPS 5601）
    K->>ES: 查詢 Log（KQL / ES|QL）
    ES->>K: 返回結果
    K->>User: 顯示查詢與視覺化結果
```

| 階段 | 元件 | 關鍵設定 | 對應章節 |
| --- | --- | --- | --- |
| 產生 | 應用程式 | ECS JSON 格式、輸出 `trace.id` | [5.3.1](#531-步驟-1應用程式-log-設定) |
| 收集 | Filebeat | `filestream` + 唯一 `id`、`ndjson` parser | [5.3.2](#532-步驟-2filebeat-filestream-設定) |
| 處理 | Logstash | 新 SSL 選項、`[@metadata]`、遮蔽 | [4.2](#42-logstash-設定) |
| 儲存 | Elasticsearch | Data Stream、`logs@custom`、ILM | [4.1.4](#414-index-template-與-component-template)、[7.1](#71-data-stream-與-index-管理) |
| 使用 | Kibana | Data View、Discover、Alerting | [第六章](#第六章系統使用) |

---

### 5.2 收集端選型

> 🆕 **v2.0 新增**

| 架構 | 適用情境 | 優點 | 缺點 |
| --- | --- | --- | --- |
| Filebeat → Elasticsearch（Ingest Pipeline） | Log 已是 JSON、解析需求簡單 | 元件最少、延遲低 | 無緩衝；解析能力有限 |
| Filebeat → Logstash → Elasticsearch | 需要複雜解析、遮蔽、多目的地 | 處理能力最強、PQ 緩衝 | 多一層需維運 |
| Filebeat → Kafka → Logstash → Elasticsearch | 大流量、尖峰明顯、需重播 | 削峰、解耦、可重送 | 架構最複雜 |
| Elastic Agent + Fleet | 主機數多、需集中管理、同時收 Metrics／Security | 集中 Policy 管理、Integrations 現成 | 需 Fleet Server |
| OTel SDK／EDOT Collector | 已採用 OpenTelemetry、Logs／Traces／Metrics 一致化 | 廠商中立、與 Trace 天然關聯 | 欄位語意與 ECS 不同（見第十一章） |

```mermaid
graph TD
    Q1{"Log 已是結構化 JSON？"}
    Q1 -->|是| Q2{"需要遮蔽、多目的地或複雜轉換？"}
    Q1 -->|否| LS["Filebeat → Logstash"]
    Q2 -->|否| Q3{"主機數多、需集中管理？"}
    Q2 -->|是| LS
    Q3 -->|是| AG["Elastic Agent + Fleet"]
    Q3 -->|否| FB["Filebeat → Elasticsearch"]
    LS --> Q4{"尖峰流量大或需重播？"}
    Q4 -->|是| KF[加入 Kafka 緩衝層]
    Q4 -->|否| DONE[維持兩層架構]
```

---

### 5.3 實際串接範例：Spring Boot 應用程式

#### 5.3.1 步驟 1：應用程式 Log 設定

**方式 A（建議）：Spring Boot 3.4+／4.x 內建 Structured Logging**

```yaml
# application.yml
spring:
  application:
    name: order-service

logging:
  file:
    name: /var/log/myapp/order-service.json
  structured:
    format:
      file: ecs          # 檔案輸出 ECS JSON；console 仍為一般格式
    ecs:
      service:
        name: order-service
        version: 1.4.2
        environment: prod
  logback:
    rollingpolicy:
      max-file-size: 100MB
      max-history: 7
      total-size-cap: 5GB
```

**方式 B：Logback + ECS Encoder（舊版 Spring Boot 或非 Spring 專案）**

```xml
<!-- logback-spring.xml；需加入依賴 co.elastic.logging:logback-ecs-encoder -->
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="LOG_PATH" value="/var/log/myapp"/>
    <property name="APP_NAME" value="order-service"/>

    <appender name="ECS_JSON_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_PATH}/${APP_NAME}.json</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>${LOG_PATH}/${APP_NAME}.%d{yyyy-MM-dd}.%i.json</fileNamePattern>
            <maxFileSize>100MB</maxFileSize>
            <maxHistory>7</maxHistory>
            <totalSizeCap>5GB</totalSizeCap>
        </rollingPolicy>
        <encoder class="co.elastic.logging.logback.EcsEncoder">
            <serviceName>${APP_NAME}</serviceName>
            <serviceEnvironment>prod</serviceEnvironment>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="ECS_JSON_FILE"/>
    </root>
</configuration>
```

> ⚠️ **v2.0 更正**：v1.0 使用 `TimeBasedRollingPolicy`（無大小上限，單日暴量時會塞爆磁碟）與 `LogstashEncoder`（非 ECS 欄位名稱，需額外轉換）。9.x 內建的 `logs-*-*` 範本以 ECS 為準，應用端直接輸出 ECS 可省去大部分解析與 mapping 設定。
>
> 💡 **建議**：導入 Micrometer Tracing／OpenTelemetry 後，`traceId`、`spanId` 會放入 MDC 並隨結構化 Log 輸出；請在 Logstash 或 Ingest Pipeline 統一為 ECS 的 `trace.id`、`span.id`，以便與 APM／Tracing 關聯。

#### 5.3.2 步驟 2：Filebeat filestream 設定

```yaml
# /etc/filebeat/filebeat.yml
filebeat.inputs:
  # JSON（ECS）Log
  - type: filestream
    id: order-service-json            # 必填且全機唯一；變更會導致重複收集
    paths:
      - /var/log/myapp/order-service*.json
    parsers:
      - ndjson:
          target: ""                  # 解析後的欄位放在事件根層
          overwrite_keys: true
          expand_keys: true           # "log.level" 這類點號鍵展開為物件
          add_error_key: true
    fields:
      app_name: order-service
      env: prod
      log_format: json

  # 純文字 Log（含多行 Stack Trace）
  - type: filestream
    id: order-service-plain
    paths:
      - /var/log/myapp/order-service.log
    parsers:
      - multiline:
          type: pattern
          pattern: '^\d{4}-\d{2}-\d{2}'
          negate: true
          match: after
    fields:
      app_name: order-service
      env: prod
      log_format: plain

processors:
  - add_host_metadata: ~

output.logstash:
  hosts: ["logstash-01:5044", "logstash-02:5044"]
  loadbalance: true
  ssl.certificate_authorities: ["/etc/filebeat/certs/ca.crt"]
  # 若 Logstash 設定 ssl_client_authentication => "required"，需提供 Client 憑證
  ssl.certificate: "/etc/filebeat/certs/filebeat.crt"
  ssl.key: "/etc/filebeat/certs/filebeat.key"

# 讓 Metricbeat／Elastic Agent 收集 Filebeat 自身指標（只綁本機）
http.enabled: true
http.host: localhost
http.port: 5066
```

> ⚠️ **v2.0 更正**：
>
> - v1.0 使用 `type: log` 與 `json.keys_under_root`。Filebeat 9.x 只要設定中出現 `log` input 就會拒絕啟動（除非加上 `allow_deprecated_use: true`，不建議）；改用 `filestream` 與 `parsers.ndjson`。
> - `filestream` 每個 input **必須**有唯一 `id`；省略或變更 `id` 會造成重複收集。
> - v1.0 以 `monitoring.elasticsearch` 讓 Filebeat 自行上報監控資料（legacy internal collection）。建議改為開放本機 `http` endpoint，由 Metricbeat 或 Elastic Agent 收集（見 [7.4.3](#743-stack-monitoring)）。
>
> 📌 **8.19 差異**：Filebeat 9.0 起 `filestream` 預設以 **fingerprint**（檔案前 1024 bytes 的雜湊）識別檔案；9.5 起預設啟用 growing fingerprint，小於 1024 bytes 的檔案也會立即收集。從 8.x 升級時若無法遷移狀態，檔案會被重新收集一次。

#### 5.3.3 步驟 3：Logstash Pipeline 設定

應用程式已輸出 ECS JSON 時，Logstash 只需處理路由與遮蔽：

```ruby
# /etc/logstash/conf.d/spring-boot.conf
input {
  beats {
    port => 5044
    ssl_enabled => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.pkcs8.key"
    ssl_certificate_authorities => ["/etc/logstash/certs/ca.crt"]
    ssl_client_authentication => "required"
  }
}

filter {
  # 以應用程式名稱決定 Data Stream：logs-order_service-prod
  mutate {
    add_field => {
      "[data_stream][dataset]"   => "%{[fields][app_name]}"
      "[data_stream][namespace]" => "%{[fields][env]}"
    }
  }
  mutate { gsub => ["[data_stream][dataset]", "-", "_"] }

  # 統一 Trace 欄位名稱（MDC 輸出的 traceId → ECS trace.id）
  if [traceId] {
    mutate { rename => { "[traceId]" => "[trace][id]" "[spanId]" => "[span][id]" } }
  }

  # 標記含 Stack Trace 的事件
  if [error][stack_trace] {
    mutate { add_tag => ["has_stacktrace"] }
  }

  mutate { remove_field => ["[fields]"] }
}

output {
  elasticsearch {
    hosts => ["https://es-hot-01:9200", "https://es-hot-02:9200"]
    api_key => "${ES_API_KEY}"
    ssl_certificate_authorities => ["/etc/logstash/certs/http_ca.crt"]
    data_stream => "true"
  }
}
```

#### 5.3.4 步驟 4：驗證資料流

```bash
# 1. 檢查 Filebeat 設定與輸出連線
sudo filebeat test config
sudo filebeat test output

# 2. 檢查 Logstash 是否收到並送出資料
curl -s localhost:9600/_node/stats/pipelines | jq '.pipelines.main.events'

# 3. 檢查 Data Stream 是否建立、套用哪個範本與 ILM
curl -s --cacert http_ca.crt -H "Authorization: ApiKey ${ES_API_KEY_ENCODED}" \
  "https://es-hot-01:9200/_data_stream/logs-order_service-prod?pretty" \
  | jq '.data_streams[] | {name, template, ilm_policy, index_mode}'

# 4. 檢查筆數
curl -s --cacert http_ca.crt -H "Authorization: ApiKey ${ES_API_KEY_ENCODED}" \
  "https://es-hot-01:9200/logs-order_service-prod/_count" | jq '.count'

# 5. 在 Kibana Discover 選擇對應的 Data View 查詢
```

---

### 5.4 Filebeat 進階整合

#### 5.4.1 Filebeat vs Logstash 比較

| 面向 | Filebeat | Logstash |
| --- | --- | --- |
| **定位** | 輕量級資料收集器（Go） | 資料處理引擎（JVM） |
| **資源消耗** | 低（數十 MB 記憶體） | 高（Heap 通常 1–8 GB） |
| **處理能力** | 基本（Processors、Parsers） | 強大（完整 Filter Plugin 生態） |
| **緩衝** | 本機 registry，可選磁碟佇列 | Persistent Queue + DLQ |
| **部署位置** | Application Server | 集中處理 Server |
| **使用場景** | 收集 + 轉發 | 複雜解析 + 轉換 + 路由 |

#### 5.4.2 推薦架構

```mermaid
graph LR
    subgraph "App Servers"
        A1[App 1 + Filebeat]
        A2[App 2 + Filebeat]
        A3[App N + Filebeat]
    end

    subgraph "Processing Layer"
        LS1[Logstash 1]
        LS2[Logstash 2]
    end

    subgraph "Storage"
        ES[Elasticsearch Cluster]
    end

    A1 -->|"loadbalance"| LS1
    A1 -.-> LS2
    A2 --> LS1
    A2 -.-> LS2
    A3 --> LS2
    A3 -.-> LS1
    LS1 --> ES
    LS2 --> ES
```

> 💡 **建議**：`output.logstash` 開啟 `loadbalance: true` 並列出所有 Logstash，任一台故障時 Filebeat 會自動改送其他節點。

#### 5.4.3 Filebeat Module 使用

```bash
# 啟用 Module（設定檔位於 /etc/filebeat/modules.d/）
sudo filebeat modules enable system nginx
sudo filebeat modules list

# 載入 Module 的 Ingest Pipeline 與 Dashboard（需能直接連線 Elasticsearch／Kibana）
sudo filebeat setup --pipelines --modules system,nginx \
  -E output.logstash.enabled=false \
  -E 'output.elasticsearch.hosts=["https://es-hot-01:9200"]' \
  -E 'output.elasticsearch.api_key=${ES_SETUP_API_KEY}' \
  -E 'output.elasticsearch.ssl.certificate_authorities=["/etc/filebeat/certs/http_ca.crt"]'
sudo filebeat setup --dashboards

sudo systemctl restart filebeat
```

> ⚠️ **實務注意**：Module 的解析在 Elasticsearch 的 Ingest Pipeline 中執行。輸出到 Logstash 時，Logstash 的 Elasticsearch output 必須加上 `pipeline => "%{[@metadata][pipeline]}"`（並以條件判斷該欄位存在），否則 Module 資料不會被解析。新建置建議改用 Elastic Agent 的 Integrations（見 [5.6](#56-elastic-agent-與-fleet)）。

#### 5.4.4 從 log input 遷移至 filestream

> 🆕 **v2.0 新增**

從 8.x 的 `log` input 遷移時，使用 `take_over` 讓 filestream 接手既有的讀取位置，避免整批重新收集：

```yaml
filebeat.inputs:
  - type: filestream
    id: order-service-json        # 新的唯一 ID
    paths:
      - /var/log/myapp/order-service*.json
    take_over:
      enabled: true               # 接手相同路徑上 log input 的 registry 狀態
    parsers:
      - ndjson:
          target: ""
          overwrite_keys: true
```

| 步驟 | 動作 |
| --- | --- |
| 1 | 在 8.19 上先完成 `log` → `filestream`（`take_over`）遷移並觀察數日 |
| 2 | 確認 Elasticsearch 無重複資料、無遺漏 |
| 3 | 移除 `take_over` 設定（保留亦可），再升級至 9.x |

#### 5.4.5 Filebeat 直送 Elasticsearch

適用於 Log 已是 ECS JSON、無需複雜轉換的情境：

```yaml
output.elasticsearch:
  hosts: ["https://es-hot-01:9200", "https://es-hot-02:9200"]
  api_key: "${ES_API_KEY}"            # 以 filebeat keystore 存放，格式 id:api_key
  ssl.certificate_authorities: ["/etc/filebeat/certs/http_ca.crt"]
  index: "logs-order_service-prod"    # 符合 logs-*-*，自動套用內建範本、ILM 與 LogsDB
  pipeline: "app-plaintext-logs"      # 純文字 Log 才需要（見 4.1.6）

setup.template.enabled: false         # 使用 Elasticsearch 內建的 logs-*-* 範本
```

```bash
# 以 Filebeat Keystore 存放 API Key
sudo filebeat keystore create
sudo filebeat keystore add ES_API_KEY
```

> ⚠️ **實務注意**：Filebeat 自訂 `index` 時，`setup.template.*` 與 `setup.ilm.*` 的搭配需依版本文件確認（見 [E.1 待確認事項](#e1-待確認事項)）；上線前請以 `GET _data_stream/<name>` 確認套用的是內建 `logs` 範本。

---

### 5.5 ECS 與欄位命名規範

> 🆕 **v2.0 新增**

ECS（Elastic Common Schema）是 Elastic 的欄位命名標準。統一欄位名稱後，跨服務查詢、Dashboard 與告警規則才能共用。

| 用途 | ECS 欄位 | 型別 | 範例 |
| --- | --- | --- | --- |
| 時間 | `@timestamp` | date | `2026-09-30T06:30:00.123Z` |
| 訊息 | `message` | match_only_text | `Order created` |
| 等級 | `log.level` | keyword | `ERROR` |
| Logger | `log.logger` | keyword | `com.company.order.OrderService` |
| 服務名稱 | `service.name` | keyword | `order-service` |
| 環境 | `service.environment` | keyword | `prod` |
| 版本 | `service.version` | keyword | `1.4.2` |
| 主機 | `host.name` | keyword | `app-server-01` |
| 追蹤 | `trace.id`、`span.id`、`transaction.id` | keyword | `4bf92f3577b34da6a3ce929d0e0e4736` |
| 錯誤 | `error.type`、`error.message`、`error.stack_trace` | keyword／text／wildcard | `java.net.SocketTimeoutException` |
| HTTP | `http.request.method`、`url.path`、`http.response.status_code` | keyword／long | `POST`、`/api/orders`、`500` |
| 耗時 | `event.duration` | long（**奈秒**） | `150000000`（150 ms） |
| 資料集 | `data_stream.dataset`、`data_stream.namespace` | constant_keyword | `order_service`、`prod` |

**自訂欄位原則**：

| 原則 | 說明 |
| --- | --- |
| 不要佔用 ECS 名稱 | 業務欄位放在自有命名空間，例如 `app.order_id`、`app.amount` |
| 型別一致 | 同名欄位在所有服務中型別必須相同，否則會發生 mapping 衝突（事件進 DLQ 或 failure store） |
| 數值與時間 | 耗時統一用 `event.duration`（奈秒）或自訂 `app.duration_ms`，不要混用 |
| 個資最小化 | `user.id` 可接受，姓名、身分證、卡號不得寫入（見 [9.4.1](#941-敏感資料處理)） |

---

### 5.6 Elastic Agent 與 Fleet

> 🆕 **v2.0 新增**

```mermaid
graph LR
    subgraph "主機群"
        A1[Elastic Agent]
        A2[Elastic Agent]
        A3[Elastic Agent]
    end

    FS[Fleet Server<br/>8220]
    KB[Kibana Fleet UI<br/>Agent Policy]
    ES[Elasticsearch]

    KB -->|"Policy"| ES
    FS -->|"讀取 Policy"| ES
    A1 -->|"註冊 / 取得 Policy"| FS
    A2 --> FS
    A3 --> FS
    A1 -->|"資料"| ES
    A2 --> ES
    A3 --> ES
```

| 項目 | 說明 |
| --- | --- |
| Fleet Server | Agent 的控制平面，負責註冊與 Policy 下發（預設 8220 埠） |
| Agent Policy | 一組 Integrations 設定，套用到一群 Agent |
| Integrations | 現成的收集設定 + Ingest Pipeline + Dashboard（例如 Nginx、System、Custom Logs） |
| 輸出 | 直送 Elasticsearch，或輸出到 Logstash（Logstash 端使用 `elastic_agent` input） |
| 9.5 新功能 | Elastic Agent 內建 EDOT Collector，可同時執行 OpenTelemetry 收集（見第十一章） |
| 授權 | Fleet 與大多數 Integrations 在 Basic 授權即可使用 |

```bash
# 在主機上安裝並註冊 Agent（Enrollment Token 由 Kibana Fleet 介面產生）
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-9.5.4-linux-x86_64.tar.gz
tar xzvf elastic-agent-9.5.4-linux-x86_64.tar.gz
cd elastic-agent-9.5.4-linux-x86_64
sudo ./elastic-agent install \
  --url=https://fleet-server.company.com:8220 \
  --enrollment-token=<token> \
  --certificate-authorities=/etc/pki/company-ca.crt
```

> 💡 **建議**：既有 Filebeat 架構不必急於遷移；新增大量主機、或需要同時收集 Metrics／資安資料時，再評估以 Elastic Agent + Fleet 統一管理。

---

### 5.7 💡 本章實務建議

- 應用端直接輸出 ECS JSON（Spring Boot 3.4+ 內建），是降低整體解析成本最有效的一步。
- Filebeat 9.x 只用 `filestream`，每個 input 都要有唯一 `id`；8.x 先用 `take_over` 完成遷移再升級。
- 依「是否結構化、是否需複雜處理、主機規模」選擇 Filebeat 直送、Logstash、Kafka 或 Elastic Agent。
- Data Stream 名稱遵循 `logs-{dataset}-{namespace}`，dataset 以底線取代連字號。
- 全鏈路 TLS：Filebeat → Logstash（mTLS）→ Elasticsearch（HTTPS + API Key）。

---

## 第六章：系統使用

### 6.1 Kibana 操作教學

#### 6.1.1 Discover：Log 查詢

```mermaid
graph TB
    subgraph "Discover 介面"
        A[時間選擇器]
        B["查詢列<br/>KQL / Lucene / ES|QL"]
        C[欄位清單]
        D[文件表格]
        E[文件詳情]
        P[Patterns 分頁]
    end

    A --> D
    B --> D
    C --> D
    D --> E
    D --> P
```

**基本操作**：

1. **選擇 Data View**：左上角下拉選單（或切換為 ES|QL 模式直接撰寫 `FROM` 查詢）
2. **設定時間範圍**：右上角時間選擇器；先縮小時間範圍再下條件，查詢最快
3. **輸入搜尋條件**：查詢列輸入 KQL；複雜統計改用 ES|QL
4. **新增顯示欄位**：從左側欄位清單點擊 `+`，建議固定 `service.name`、`log.level`、`message`
5. **檢視文件詳情**：展開任一筆 Log，可檢視原始 JSON、並以「Surrounding documents」查看前後文
6. **Patterns**：將大量相似訊息自動歸類，快速找出新出現的錯誤型態

> 💡 **建議**：常用查詢以 **Save** 存成 Saved Search（Discover Session），供 Dashboard 引用並與團隊共用，避免每人各自撰寫不一致的條件。

#### 6.1.2 Dashboard 與 Lens

**建立 Dashboard 步驟**：

1. 進入 **Analytics** → **Dashboards** → **Create dashboard**
2. 點擊 **Create visualization**（預設開啟 Lens）
3. 將欄位拖曳到工作區，Lens 會建議合適的圖表類型：
   - **Bar／Line**：趨勢分析
   - **Metric**：單一 KPI
   - **Table**：明細或 Top N
   - **Donut／Treemap**：比例分布（類別不宜超過 6 個）
4. 設定 Data View、篩選條件與 Breakdown
5. **Save and return** 加入 Dashboard，並設定 Dashboard 層級的篩選控制項（Controls）

**範例：Error Rate Dashboard**

```text
1. Line Chart（Lens）：
   - Data View: logs-*-prod
   - Horizontal axis: @timestamp（自動間隔）
   - Vertical axis: Count
   - Breakdown: log.level（Top 5）

2. Metric：
   - Filter: log.level : "ERROR"
   - Value: Count，Time range 跟隨 Dashboard

3. Table：
   - Filter: log.level : "ERROR"
   - Rows: service.name（Top 10）、error.type（Top 5）
   - Metric: Count，依 Count 遞減排序

4. Controls：service.environment、service.name 下拉選單
```

> 🆕 **v2.0 新增**：9.5 起 **Dashboards & Visualizations API 為 GA**，可將 Dashboard 以程式碼管理（版本控制、跨環境部署）。在此之前，跨環境搬移以 Saved Objects 匯出／匯入（`.ndjson`）為主。

#### 6.1.3 分享與匯出

| 需求 | 操作 | 授權 |
| --- | --- | --- |
| 分享查詢結果 | Discover → **Share** → 複製連結（可選短網址） | Basic |
| 匯出 CSV | Discover → **Share** → **Export** → **CSV** → Generate | Basic |
| 匯出 Dashboard PDF／PNG | Dashboard → **Share** → **Export** | 💰 付費 |
| 排程報表 | 報表的 Schedule 功能 | 💰 付費 |
| 搬移 Dashboard 到其他環境 | Stack Management → Saved Objects → Export／Import | Basic |

> ⚠️ **實務注意**：CSV 匯出有筆數與大小上限（`xpack.reporting.csv.maxRows` 等設定），大量稽核資料應以 ES|QL 或 Scroll／PIT API 由後端批次匯出，並保留匯出紀錄。

---

### 6.2 查詢語法詳解

| 語言 | 適用 | 特點 |
| --- | --- | --- |
| **KQL** | Discover 日常篩選、Dashboard 篩選、告警條件 | 語法簡單、支援自動完成 |
| **Lucene** | 需要正規表達式、模糊搜尋、權重 | 功能多但易寫錯 |
| **ES\|QL** | 統計、轉換、Join、臨時解析 | 管線式語法，一次完成篩選 → 計算 → 彙整 |

#### 6.2.1 KQL（Kibana Query Language）

```text
# 基本語法
欄位名稱: 值

# 範例
log.level: ERROR
service.name: "order-service"
message: "timeout"
```

| 需求 | KQL 語法 |
| --- | --- |
| 精確匹配 | `log.level: "ERROR"` |
| 片語匹配 | `message: "connection timed out"` |
| 萬用字元 | `service.name: order*` |
| 多值匹配 | `log.level: (ERROR or WARN)` |
| 範圍查詢 | `http.response.status_code >= 500 and http.response.status_code < 600` |
| 日期數學 | `@timestamp >= now-1d/d` |
| 存在檢查 | `error.stack_trace: *` |
| 組合條件 | `service.name: order* and log.level: ERROR` |
| 排除條件 | `not log.level: DEBUG` |

> ⚠️ **實務注意**：`message: *timeout*` 這類**前置萬用字元**查詢需掃描大量詞彙，資料量大時非常慢；對 `message`（text）欄位直接用 `message: timeout` 即可利用全文索引。

#### 6.2.2 Lucene Query Syntax（進階）

```text
# 萬用字元
message:timeout*
message:time?ut

# 正規表達式（對 keyword 欄位較有意義）
error.type:/.*Timeout.*/

# 模糊搜尋（容許 2 個字元差異）
message:tiemout~2

# 範圍搜尋
http.response.status_code:[500 TO 599]
@timestamp:[2026-09-01 TO 2026-09-30]

# 權重
message:error^2 OR message:warning
```

#### 6.2.3 ES|QL（Elasticsearch Query Language）

> 🆕 **v2.0 新增**

ES|QL 以 `|` 串接處理步驟，適合在 Discover 直接做統計與臨時解析；9.x 起已是 Kibana 的一級查詢語言。

**1. 近 1 小時錯誤最多的服務**

```sql
FROM logs-*
| WHERE @timestamp >= NOW() - 1 hour AND log.level == "ERROR"
| STATS errors = COUNT(*) BY service.name
| SORT errors DESC
| LIMIT 10
```

**2. 每 5 分鐘的錯誤率**

```sql
FROM logs-*-prod
| WHERE @timestamp >= NOW() - 24 hours
| EVAL is_error = CASE(log.level == "ERROR", 1, 0)
| STATS total = COUNT(*), errors = SUM(is_error) BY bucket = BUCKET(@timestamp, 5 minutes)
| EVAL error_rate = ROUND(errors * 100.0 / total, 2)
| SORT bucket
```

**3. 查詢當下解析未結構化欄位（不需重新索引）**

```sql
FROM logs-order_service-prod
| WHERE message LIKE "*Read timed out*"
| GROK message "Read timed out after %{NUMBER:timeout_ms:int} ms"
| STATS avg_timeout = AVG(timeout_ms), cnt = COUNT(*) BY host.name
```

**4. 以 LOOKUP JOIN 補上服務負責團隊（9.1 起 GA）**

```sql
FROM logs-*-prod
| WHERE log.level == "ERROR"
| LOOKUP JOIN service_owners ON service.name
| STATS errors = COUNT(*) BY service.name, team.name
| SORT errors DESC
```

```text
# service_owners 需為 lookup 模式的索引（單一 Shard）
PUT service_owners
{
  "settings": { "index.mode": "lookup" },
  "mappings": {
    "properties": {
      "service.name": { "type": "keyword" },
      "team.name":    { "type": "keyword" }
    }
  }
}
```

> ⚠️ **實務注意**：ES|QL 預設最多回傳 1,000 筆（可用 `LIMIT` 調整，上限預設 10,000）；它適合統計與分析，不適合用來大量匯出原始資料。

#### 6.2.4 實用查詢範例

| 需求 | KQL | ES\|QL |
| --- | --- | --- |
| 特定交易的完整鏈路 | `trace.id: "4bf92f35..."` | `FROM logs-* \| WHERE trace.id == "4bf92f35..." \| SORT @timestamp` |
| 今日所有 5xx | `http.response.status_code >= 500 and @timestamp >= now/d` | `FROM logs-* \| WHERE http.response.status_code >= 500 AND @timestamp >= NOW() - 1 day` |
| 慢請求（> 3 秒） | `event.duration > 3000000000` | `FROM logs-* \| WHERE event.duration > 3000000000 \| STATS COUNT(*) BY url.path` |
| 排除健康檢查 | `not url.path: ("/health" or /actuator/*)` | `FROM logs-* \| WHERE NOT url.path LIKE "/actuator/*"` |
| 含例外的 Log | `error.stack_trace: * or message: Exception` | `FROM logs-* \| WHERE error.stack_trace IS NOT NULL` |

> ⚠️ **v2.0 更正**：v1.0 的「實用查詢範例」混用了 KQL 的 `>=` 與 Lucene 的 `[500 TO 599]`，在同一查詢列中無法執行；`@timestamp` 比較也未考慮時區。上表已依語言分開。KQL 的萬用字元在加上雙引號後會被視為一般字元，因此 `/actuator/*` 不可加引號；Lucene 中 `/` 代表正規表達式，需寫成 `\/actuator\/*`。

---

### 6.3 告警（Alerting）

> 🆕 **v2.0 新增**

#### 6.3.1 Log 相關的規則類型

| 規則類型 | 用途 | 查詢方式 | 授權 |
| --- | --- | --- | --- |
| Elasticsearch query | 查詢結果筆數超過門檻 | KQL、Query DSL、ES\|QL | Basic |
| Log threshold | 特定條件的 Log 筆數或比率超過門檻 | 條件式 UI | Basic |
| Custom threshold | 自訂聚合（Count、Average 等）門檻 | 條件式 UI | Basic |
| Anomaly detection | ML 偵測異常 | ML Job | 💰 付費 |

#### 6.3.2 Connector 與授權

| Connector | 用途 | 授權 |
| --- | --- | --- |
| Server log | 寫入 Kibana Log | Basic |
| Index | 將告警寫入索引，供稽核與二次分析 | Basic |
| Email、Slack、Microsoft Teams、Webhook | 通知 | 💰 付費 |
| PagerDuty、Opsgenie、ServiceNow、Jira | 事件管理 | 💰 付費 |

> 💡 **建議**：Basic 授權環境可用「Index Connector 寫入告警索引」+「Prometheus／Alertmanager 或既有監控讀取該索引」的方式轉發；或由 Grafana 以 Elasticsearch 資料來源建立告警，統一由 Alertmanager 通知。

#### 6.3.3 建立 Log 告警規則（UI）

1. **Stack Management** → **Rules** → **Create rule**
2. 選擇 **Elasticsearch query**，查詢類型選 **ES|QL**：

   ```sql
   FROM logs-*-prod
   | WHERE log.level == "ERROR" AND service.name == "payment-service"
   | STATS errors = COUNT(*) BY service.name
   | WHERE errors > 50
   ```

3. 設定時間欄位 `@timestamp`、時間視窗 5 分鐘、檢查頻率 1 分鐘
4. 加入 Action（Connector），訊息中帶入 `{{context.link}}` 讓收件者一鍵跳轉 Kibana
5. 設定 Action 頻率（例如「狀態變更時」或摘要通知），避免告警風暴

#### 6.3.4 告警設計原則

| 原則 | 說明 |
| --- | --- |
| 可行動 | 每則告警都要有負責人與處理手冊（Runbook）連結 |
| 不重複 | 系統層級指標（CPU、延遲）由 Prometheus 告警；Log 告警聚焦「錯誤內容」與「業務事件」 |
| 有門檻與視窗 | 以「5 分鐘內 > N 筆」取代「出現一筆就告警」 |
| 可追溯 | 以 Index Connector 保存告警紀錄，供事後檢討 |
| 分級 | P1 電話／簡訊、P2 即時通訊、P3 Email 摘要 |

> ⚠️ **v2.0 更正**：v1.0 以 Elasticsearch **Watcher** 作為 Log 告警。Watcher 為付費功能且設定以 JSON 撰寫、難以維護；9.x 建議使用 Kibana Alerting。既有 Watcher 可持續運作，但新規則不建議再以 Watcher 建立。

---

### 6.4 Streams 與 Log 解析

> 🆕 **v2.0 新增**

Streams 是 Kibana 中集中管理 Log「解析、分流、保存與品質」的介面，9.1 為 Preview、**9.2 起 GA**。

| 能力 | 說明 |
| --- | --- |
| Classic streams | 直接套用在既有的 Data Stream，不需搬移資料 |
| Wired streams | 送到受管理端點（9.4+ 為 `logs.otel` 或 `logs.ecs`；9.2–9.3 為 `logs`），具階層與設定繼承 |
| Processing | 以 Grok／Dissect 等處理器解析，可由 AI 建議解析規則（需設定 Generative AI Connector） |
| Partitioning | 依條件將資料分流至子 Stream（僅 wired streams） |
| Retention | 設定保存期限，或套用 ILM Policy |
| Data quality | 監看解析失敗與欄位問題，失敗文件保存在 failure store 供檢查 |

```mermaid
graph LR
    SRC[Filebeat / Agent / OTel] --> W["logs.otel / logs.ecs<br/>（wired stream）"]
    W --> C1["logs.otel.nginx<br/>子 Stream"]
    W --> C2["logs.otel.app<br/>子 Stream"]
    C1 --> R1[保存 30 天]
    C2 --> R2[保存 180 天]
```

> ⚠️ **實務注意**：Streams 會改變 Log 的處理與保存位置，屬於平台治理範疇；導入前應由平台團隊決定「哪些資料走 wired streams、哪些維持現有 Logstash／範本」，避免兩套規則並存。自建環境的啟用方式與 AI 功能授權見 [E.1 待確認事項](#e1-待確認事項)。

---

### 6.5 實務使用情境

#### 6.5.1 情境一：問題追蹤

**場景**：使用者回報訂單失敗，提供訂單編號 `ORD-20260930-001`

```mermaid
sequenceDiagram
    participant User as 工程師
    participant K as Kibana
    participant ES as Elasticsearch

    User->>K: 1. 查詢 app.order_id: "ORD-20260930-001"
    K->>ES: 2. 執行查詢
    ES->>K: 3. 返回相關 Log
    K->>User: 4. 取得 trace.id
    User->>K: 5. 以 trace.id 查詢完整鏈路
    User->>User: 6. 定位 ERROR 與 Stack Trace
```

**查詢步驟**：

```text
1. Discover 輸入：app.order_id: "ORD-20260930-001"
2. 時間範圍放寬至涵蓋交易時間（例如前後 1 小時）
3. 從結果取得 trace.id，改查：trace.id: "<值>"
4. 依 @timestamp 遞增排序，新增欄位 service.name、log.level、message、event.duration
5. 找到 ERROR，展開檢視 error.stack_trace；必要時以 Surrounding documents 看前後文
```

#### 6.5.2 情境二：錯誤分析

**場景**：Grafana 告警顯示 Error Rate 上升

```sql
// 告警觸發前後 30 分鐘，依錯誤類型統計（ES|QL 註解使用 // 或 /* */）
FROM logs-*-prod
| WHERE @timestamp >= "2026-09-30T06:00:00Z" AND @timestamp < "2026-09-30T07:00:00Z"
  AND log.level == "ERROR"
| STATS cnt = COUNT(*) BY service.name, error.type
| SORT cnt DESC
| LIMIT 20
```

```text
後續步驟：
1. 鎖定最多的錯誤類型，例如 error.type: "java.net.SocketTimeoutException" 且 service.name: payment-service
2. 開啟 Patterns 分頁，確認是否為新出現的訊息型態
3. 到 Grafana 檢查同時段 payment-service 的連線池、延遲與下游服務指標
```

#### 6.5.3 情境三：系統行為回溯（稽核）

**場景**：稽核要求提供特定使用者過去 7 天的操作紀錄

```text
查詢語法（KQL）：
user.id: "U12345" and event.action: * and @timestamp >= now-7d

顯示欄位：
@timestamp、event.action、source.ip、url.path、http.response.status_code

匯出步驟：
1. Discover 執行查詢並設定顯示欄位
2. Share → Export → CSV → Generate
3. 於 Stack Management → Reporting 下載
4. 依稽核程序登記匯出原因、申請人與檔案保存位置
```

> ⚠️ **實務注意**：稽核查詢本身也應被記錄。啟用稽核日誌（付費功能）或以 Kibana Reporting 紀錄保存匯出軌跡；匯出的 CSV 屬敏感資料，應依資料分級加密保存。

#### 6.5.4 情境四：與 Grafana Metrics 搭配分析

```mermaid
graph LR
    subgraph "Grafana"
        A[發現 CPU 飆高]
        B[檢視 Alert 詳情]
    end

    subgraph "Kibana"
        C[查詢同時段 Log]
        D[識別異常 Pattern]
    end

    A --> B
    B -->|"Data Link"| C
    C --> D
    D -->|"以 trace.id / host.name 關聯"| A
```

```text
# Grafana Alert 觸發時間：2026-09-30 14:30（Asia/Taipei）
# 目標服務：inventory-service；觀察到 CPU > 90%

Kibana 查詢（KQL，時間選擇器設定 14:25–14:35）：
service.name: "inventory-service"

可能發現：
- 大量 DEBUG Log 輸出（Log 等級設定錯誤）
- 重複的 SQL Query（N+1 問題）
- 頻繁 GC 或 OutOfMemoryError
- 大量 Exception 被拋出並重試
```

---

### 6.6 💡 本章實務建議

- 日常篩選用 KQL，統計與臨時解析用 ES|QL；兩種語法不要混在同一查詢列。
- 以 ECS 欄位（`service.name`、`log.level`、`trace.id`）撰寫查詢，Dashboard 與告警才能跨服務共用。
- Log 告警改用 Kibana Alerting；外部通知 Connector 需付費，Basic 環境可透過 Index Connector 或 Grafana 轉發。
- 常用查詢存為 Saved Search，Dashboard 9.5 起可用 API 以程式碼管理。
- Streams 屬平台治理功能，導入前先決定與既有 Logstash／範本的分工。

---

## 第七章：系統維護

### 7.1 Data Stream 與 Index 管理

#### 7.1.1 Data Stream 基本操作

```text
# 列出所有 logs Data Stream 及其範本、ILM、索引模式
GET _data_stream/logs-*?filter_path=data_streams.name,data_streams.template,data_streams.ilm_policy,data_streams.index_mode

# 查看某個 Data Stream 的 backing index
GET _data_stream/logs-order_service-prod

# 手動 rollover（例如修改 mapping 後讓新設定立即生效）
POST logs-order_service-prod/_rollover

# 查看 backing index 的 ILM 進度與錯誤
GET .ds-logs-order_service-prod-*/_ilm/explain?only_errors=true
```

| 規則 | 說明 |
| --- | --- |
| 只能附加寫入 | Data Stream 不支援以 `_id` 更新；需修正資料時用 `_update_by_query` 或針對 backing index 操作 |
| write index 不可刪 | 目前的 write index 需先 rollover 才能刪除 |
| 刪除整個 Data Stream | `DELETE _data_stream/<name>` 會刪除**所有** backing index，務必確認 |
| Mapping 變更 | 修改範本後只影響 rollover 後的新 backing index |

#### 7.1.2 Index Lifecycle Management（ILM）

```mermaid
graph LR
    subgraph "ILM 階段（min_age 自 rollover 起算）"
        H[Hot<br/>寫入 & 查詢<br/>rollover]
        W[Warm<br/>唯讀 & forcemerge]
        C[Cold<br/>低頻查詢]
        D[Delete<br/>刪除]
    end

    H -->|"7 天後"| W
    W -->|"30 天後"| C
    C -->|"180 天後"| D

    style H fill:#ff6b6b
    style W fill:#feca57
    style C fill:#54a0ff
    style D fill:#576574
```

> ⚠️ **實務注意**：內建的 `logs` ILM 政策只做 rollover（primary shard 50 GB 或 30 天），**沒有刪除階段**——未自訂保存期限時，Log 會無限累積直到磁碟滿。請勿直接修改受管理的內建政策，應自建政策並透過 `logs@custom` 或專屬範本套用。

```text
PUT _ilm/policy/logs-standard-180d
{
  "policy": {
    "_meta": { "owner": "platform-team", "description": "一般應用 Log：Hot 7 天、Warm 至 30 天、Cold 至 180 天" },
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_primary_shard_size": "50gb",
            "max_age": "1d"
          },
          "set_priority": { "priority": 100 }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "forcemerge": { "max_num_segments": 1 },
          "set_priority": { "priority": 50 }
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": {
          "set_priority": { "priority": 0 }
        }
      },
      "delete": {
        "min_age": "180d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

```text
# 套用到所有 logs-*-*（寫入 logs@custom；已存在時需合併原有內容）
PUT _component_template/logs@custom
{
  "template": {
    "settings": {
      "index.lifecycle.name": "logs-standard-180d"
    }
  }
}
```

| 項目 | 說明 |
| --- | --- |
| 階段搬移 | 叢集有 `data_warm`／`data_cold` 節點時，ILM 會自動執行 `migrate` 動作搬移到對應 Tier |
| `max_primary_shard_size` | 優於 `max_size`（後者為所有 primary 的總和，Shard 數變動時不易掌握） |
| 保存期限 | `delete.min_age` 從 rollover 起算，實際保存期間 ≈ rollover 週期 + `min_age` |
| Frozen | 以 `searchable_snapshot` 動作搬到 Frozen Tier，💰 需 Enterprise 授權 |

> ⚠️ **v2.0 更正**：v1.0 的 ILM 範例有三個問題：(1) Cold 階段使用 `freeze` 動作——該功能已移除，9.x 中只是為相容而保留的 no-op；(2) Warm 階段的 `shrink` 需將所有 Shard 先集中到單一節點，對 Log 平台效益有限且易卡住，已移除；(3) `max_size` 改為 `max_primary_shard_size`。

#### 7.1.3 Data Stream Lifecycle（DSL）

DSL 是較簡單的保存期限管理方式：只需設定「保存多久」，由 Elasticsearch 自動決定 rollover 與合併。

```text
# 對既有 Data Stream 設定保存 90 天
PUT _data_stream/logs-debug_tool-dev/_lifecycle
{
  "data_retention": "90d"
}

# 查詢生效中的生命週期
GET _data_stream/logs-debug_tool-dev/_lifecycle
```

| 比較 | ILM | DSL |
| --- | --- | --- |
| 設定複雜度 | 高（多階段） | 低（保存期限） |
| Data Tiers 搬移 | ✅ | ❌（資料停留在原節點） |
| Searchable Snapshot | ✅ | ❌ |
| 適用 | 正式環境、多 Tier | 開發測試環境、單一 Tier 的小型叢集 |

> 💡 **建議**：同一個 Data Stream 同時設定 ILM 與 DSL 時，預設以 ILM 為準（`index.lifecycle.prefer_ilm: true`）；避免混用造成維運人員誤判。

#### 7.1.4 LogsDB 索引模式

| 項目 | 說明 |
| --- | --- |
| 預設行為 | 9.0 起新建立的 `logs-*-*` Data Stream 預設啟用 LogsDB；由 8.x 升級的叢集，只有在升級當時尚無任何 `logs-*-*` Data Stream 時，新建的才會自動啟用 |
| 效益 | 官方數據：儲存空間最多可減少約 60%，寫入效能約降低 10–20%（依資料集而異） |
| 原理 | 依 `host.name`、`@timestamp` 排序儲存、合成（synthetic）`_source`、進階壓縮 |
| 自訂範本啟用 | 在範本 settings 加入 `"index.mode": "logsdb"` |
| 確認方式 | `GET _data_stream/<name>` 的 `index_mode` 欄位 |

> ⚠️ **實務注意**：合成 `_source` 會依 mapping 重建原始文件，欄位順序、陣列重複值等可能與寫入時不同；若有「必須原樣保存」的稽核需求，請在上線前驗證，並確認授權對 synthetic source 的影響（見 [E.1 待確認事項](#e1-待確認事項)）。

#### 7.1.5 手動清理

```text
# 列出 backing index 與大小（依建立時間排序）
GET _cat/indices/.ds-logs-*?v&h=index,health,docs.count,store.size,creation.date.string&s=creation.date

# 刪除特定 backing index（非 write index）
DELETE .ds-logs-order_service-prod-2026.06.01-000001
```

> ⚠️ **v2.0 更正**：v1.0 以 Shell 腳本解析索引名稱中的日期並刪除、並建議使用 Curator。Curator 已停止維護；Data Stream 的 backing index 名稱日期是「建立日」而非資料日期，以名稱判斷容易誤刪。保存期限應一律交由 ILM／DSL 管理，手動刪除只用於緊急處理。

---

### 7.2 Snapshot 與 SLM

> 🆕 **v2.0 新增**

Snapshot 是 Elasticsearch **唯一受支援的備份方式**；直接複製資料目錄無法保證一致性。

#### 7.2.1 建立 Snapshot Repository

**共享檔案系統（fs）**：所有節點都必須掛載同一路徑，且在每個節點的 `elasticsearch.yml` 設定 `path.repo` 後重啟。

```yaml
# elasticsearch.yml（所有 master 與 data 節點）
path.repo: ["/mnt/es-backup"]
```

```text
PUT _snapshot/fs_backup
{
  "type": "fs",
  "settings": { "location": "/mnt/es-backup/prod" }
}
```

**S3 相容物件儲存（建議）**：9.x 內建 S3 Repository，不需另外安裝 Plugin。

```bash
# 每個節點設定存取金鑰（存於 keystore）
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add s3.client.default.access_key
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add s3.client.default.secret_key
```

```text
# 重新載入 keystore 中可熱更新的設定
POST _nodes/reload_secure_settings

PUT _snapshot/s3_backup
{
  "type": "s3",
  "settings": {
    "bucket": "elk-prod-snapshots",
    "base_path": "prod-cluster",
    "client": "default"
  }
}

# 驗證所有節點都能存取
POST _snapshot/s3_backup/_verify
```

> ⚠️ **v2.0 更正**：v1.0 直接建立 `fs` repository，漏掉 `path.repo` 設定，實際執行會失敗；且備份路徑若只掛載在單一節點，Snapshot 會因其他節點無法寫入而失敗。

#### 7.2.2 Snapshot Lifecycle Management（SLM）

```text
PUT _slm/policy/nightly-snapshots
{
  "schedule": "0 30 1 * * ?",
  "name": "<nightly-snap-{now/d}>",
  "repository": "s3_backup",
  "config": {
    "indices": ["logs-*"],
    "include_global_state": true
  },
  "retention": {
    "expire_after": "30d",
    "min_count": 7,
    "max_count": 60
  }
}

# 立即執行一次並確認結果
POST _slm/policy/nightly-snapshots/_execute
GET _slm/policy/nightly-snapshots?human
GET _slm/stats
```

| 設定 | 說明 |
| --- | --- |
| `schedule` | Cron 格式（秒 分 時 日 月 週），時間以 UTC 計算 |
| `include_global_state` | 包含範本、ILM 政策與 Kibana 等功能狀態（feature states），還原整個平台時需要 |
| `retention` | 自動刪除過期快照，同時保留最少份數 |

#### 7.2.3 還原與演練

```text
# 列出快照
GET _snapshot/s3_backup/_all?verbose=false

# 還原單一 Data Stream 到新名稱（不影響現有資料）
POST _snapshot/s3_backup/nightly-snap-2026.09.30/_restore
{
  "indices": "logs-order_service-prod",
  "include_global_state": false,
  "rename_pattern": "logs-(.+)",
  "rename_replacement": "restored-logs-$1"
}
```

> 💡 **建議**：每季至少執行一次「在獨立環境完整還原」的演練，量測 RTO 並留存紀錄；從未還原過的備份不能視為有效備份。

---

### 7.3 效能調校

#### 7.3.1 寫入效能調校

| 手段 | 做法 | 注意事項 |
| --- | --- | --- |
| 延長 refresh 間隔 | `logs@custom` 設定 `index.refresh_interval: 10s`–`30s` | Log 晚數秒可查通常可接受 |
| 合適的 Bulk 大小 | 每批 5–15 MB；Logstash 以 `pipeline.batch.size` 調整 | 過大會造成記憶體壓力與 429 |
| 控制 Shard 數 | 小流量 Data Stream 一律 1 個 Primary | 過多小 Shard 反而降低效能 |
| 減少欄位 | 不需要搜尋的欄位設 `index: false` 或不收集 | 欄位越多，mapping 與 Heap 開銷越大 |
| 使用 LogsDB | 9.x 預設 | 寫入約慢 10–20%，換取大幅節省儲存 |
| 分散寫入 | Logstash 列出多個 Hot 節點 | 避免單一節點成為瓶頸 |

> ⚠️ **v2.0 更正**：v1.0 在 `elasticsearch.yml` 中設定 `index.refresh_interval`、`thread_pool.write.queue_size: 1000`。前者為索引層級設定，放在 yml 會導致節點無法啟動；後者加大佇列只會掩蓋背壓、增加記憶體壓力，正確做法是找出寫入瓶頸並擴充節點。

#### 7.3.2 查詢效能調校

```text
# 1. 先縮小時間範圍，再以 filter（不計分、可快取）過濾
GET logs-*-prod/_search
{
  "size": 100,
  "_source": ["@timestamp", "log.level", "service.name", "message"],
  "query": {
    "bool": {
      "filter": [
        { "range": { "@timestamp": { "gte": "now-1h" } } },
        { "term":  { "log.level": "ERROR" } }
      ]
    }
  },
  "sort": [{ "@timestamp": "desc" }]
}
```

| 原則 | 說明 |
| --- | --- |
| 避免前置萬用字元 | `*error*` 需掃描全部詞彙；改用全文查詢或 `wildcard` 型別欄位 |
| 聚合用 keyword | 對 `text` 欄位聚合需要 fielddata，會耗盡 Heap |
| 限制回傳欄位 | 以 `_source` 或 `fields` 只取需要的欄位 |
| 避免超大 `size` | 大量匯出改用 PIT + `search_after` |
| Dashboard 時間範圍 | 預設 15 分鐘至 24 小時；長期趨勢改用彙整後的資料 |

#### 7.3.3 Logstash 效能調校

```bash
# 觀察 Pipeline 的 flow metrics（吞吐量、背壓、worker 使用率）
curl -s localhost:9600/_node/stats/pipelines | jq '.pipelines[] | .flow'
```

| 指標（flow） | 判讀 |
| --- | --- |
| `input_throughput` vs `output_throughput` | 輸入持續大於輸出 → 下游（ES）或 filter 是瓶頸 |
| `queue_backpressure` | 數值高表示 input 被阻塞 |
| `worker_concurrency` 接近 `pipeline.workers` | worker 已滿載，考慮增加 worker 或優化 filter |
| `worker_utilization` | 接近 100% 表示 CPU 或 filter 運算是瓶頸 |

```yaml
# logstash.yml（依壓測結果調整）
pipeline.workers: 8          # 預設為 CPU 核心數
pipeline.batch.size: 500     # 預設 125；增大需同步增加 Heap
pipeline.batch.delay: 50     # 預設 50 ms
```

> 💡 **建議**：grok 是最常見的 CPU 瓶頸。能用 `dissect` 就不用 `grok`；grok pattern 以 `^` 錨定開頭，並在 `tag_on_failure` 中統計失敗率。

---

### 7.4 健康檢查與監控

#### 7.4.1 Elasticsearch 健康檢查

```text
# 叢集狀態
GET _cluster/health?filter_path=status,number_of_nodes,unassigned_shards,active_shards_percent_as_number

# 健康報告（8.7+）：直接指出問題、影響與建議處置
GET _health_report

# 節點資源概況
GET _cat/nodes?v&h=name,node.role,heap.percent,ram.percent,cpu,load_1m,disk.used_percent

# 未配置的 Shard 與原因
GET _cat/shards?v&h=index,shard,prirep,state,unassigned.reason&s=state
```

`_health_report` 的主要指標：

| 指標 | 檢查內容 |
| --- | --- |
| `master_is_stable` | Master 是否穩定 |
| `shards_availability` | 是否有未配置的 Primary／Replica |
| `disk` | 磁碟水位 |
| `shards_capacity` | Shard 數是否接近上限 |
| `ilm`／`slm` | 生命週期與快照政策是否卡住 |
| `data_stream_lifecycle` | DSL 是否有錯誤 |
| `repository_integrity` | Snapshot Repository 是否損壞 |

#### 7.4.2 監控指標清單

| 指標 | 正常範圍 | 告警閾值 |
| --- | --- | --- |
| Cluster Status／`_health_report` | green | yellow 持續 > 15 分鐘、red 立即 |
| JVM Heap Used | 週期性波動、GC 後回落 | 持續 > 85% |
| Old GC 時間 | 偶發 | 每分鐘 > 數秒或頻繁 Full GC |
| Disk Used | < 80% | ≥ 85%（low watermark） |
| Indexing Rate | 穩定 | 突降 50% 或歸零 |
| Search Latency | < 500 ms | 持續 > 1 s |
| Rejected（write／search thread pool） | 0 | > 0 且持續增加 |
| Unassigned Shards | 0 | > 0 持續 > 15 分鐘 |
| Logstash `queue_backpressure` | 接近 0 | 持續偏高 |
| Snapshot 成功率 | 100% | 任一次失敗 |

#### 7.4.3 Stack Monitoring

| 方式 | 說明 | 建議 |
| --- | --- | --- |
| Metricbeat（`elasticsearch-xpack`、`kibana-xpack`、`logstash-xpack`、`beat-xpack` module） | 由外部收集各元件指標 | ✅ 建議 |
| Elastic Agent（Elasticsearch／Kibana／Logstash Integrations） | 由 Fleet 統一管理收集 | ✅ 建議 |
| Legacy internal collection | 元件自行上報 | ❌ 已棄用；Logstash 9.x 需 `xpack.monitoring.allow_legacy_collection: true` 才能使用 |

> 💡 **建議**：監控資料應送往**獨立的監控叢集**，避免正式叢集故障時連監控資料都看不到。

#### 7.4.4 整合 Prometheus 監控

```text
# 建立 exporter 專用的唯讀監控角色與使用者
PUT _security/role/prometheus_exporter
{
  "cluster": ["monitor"],
  "indices": [ { "names": ["*"], "privileges": ["monitor"] } ]
}

PUT _security/user/prometheus_exporter
{
  "password": "<strong-password>",
  "roles": ["prometheus_exporter"]
}
```

```yaml
# docker-compose.yml（prometheus-community/elasticsearch_exporter，2026-07 最新版 v1.11.0）
services:
  elasticsearch-exporter:
    image: quay.io/prometheuscommunity/elasticsearch-exporter:v1.11.0
    command:
      - '--es.uri=https://prometheus_exporter:${EXPORTER_PASSWORD}@es-coord-01:9200'
      - '--es.ca=/certs/http_ca.crt'
      - '--es.all'
      - '--es.indices'
    volumes:
      - ./certs/http_ca.crt:/certs/http_ca.crt:ro
    ports:
      - "9114:9114"
```

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'elasticsearch'
    static_configs:
      - targets: ['elasticsearch-exporter:9114']
```

> ⚠️ **v2.0 更正**：v1.0 使用 `latest` 標籤、HTTP 無認證位址與 Compose `version: '3'`。正式環境應固定映像版本、以專用唯讀帳號連線並信任 CA；Compose 檔案不需 `version` 欄位。

---

### 7.5 日常維運作業

> 🆕 **v2.0 新增**

| 頻率 | 作業 | 工具／指令 |
| --- | --- | --- |
| 每日 | 確認 `_health_report` 為 green、無未配置 Shard | `GET _health_report` |
| 每日 | 確認昨夜 Snapshot 成功 | `GET _slm/stats` |
| 每日 | 檢查磁碟水位、Heap、拒絕數 | Stack Monitoring／Grafana |
| 每日 | 檢查 Logstash DLQ 與 failure store 是否有新增 | DLQ 目錄大小、`GET logs-*::failures/_search` |
| 每週 | 檢查 ILM 錯誤、Shard 數成長趨勢 | `GET */_ilm/explain?only_errors=true`、`GET _cat/shards?v` |
| 每週 | 檢視新增欄位數量（防止 mapping explosion） | `GET logs-*/_mapping` 欄位統計 |
| 每月 | 容量趨勢檢討、保存期限是否符合規範 | 2.5 容量公式 |
| 每月 | 檢查新 patch 版本與安全公告 | Elastic Security Announcements |
| 每季 | Snapshot 還原演練、權限盤點、憑證到期檢查 | 7.2.3、9.3、9.1.4 |
| 每半年 | 升級至最新 minor 版 | 第八章 |

---

### 7.6 💡 本章實務建議

- 內建 `logs` ILM 沒有刪除階段，上線前一定要自訂保存期限並透過 `logs@custom` 套用。
- ILM 不再使用 `freeze`、避免 `shrink`；rollover 以 `max_primary_shard_size` 控制。
- 以 SLM 每日快照到物件儲存，並每季做還原演練；`fs` repository 需在所有節點設定 `path.repo`。
- 寫入調校靠 refresh 間隔、Bulk 大小、Shard 數，而非加大 thread pool 佇列。
- 監控以 `_health_report` 為主，Metricbeat／Agent 送往獨立監控叢集；Prometheus exporter 固定版本並使用唯讀帳號。

---

## 第八章：系統升級

### 8.1 版本策略與升級路徑

> 🆕 **v2.0 新增**

```mermaid
graph LR
    V7["7.17.x"] -->|"必經"| V819["8.19.x（最新 patch）"]
    V8X["8.0–8.17"] -->|"先升到"| V819
    V818["8.18.x"] -->|"僅可升到"| V90["9.0.x"]
    V818 -->|"或先升到"| V819
    V819 -->|"可直接升到任一 9.x"| V95["9.5.x"]
    V90 --> V95
    V9X["9.1–9.4"] -->|"直接升級"| V95
```

| 目前版本 | 升級到 9.5 的路徑 | 備註 |
| --- | --- | --- |
| 7.17.x | 7.17 → 8.19.x → 9.5.x | 7.x 建立的索引需先處理（見 [8.2.3](#823-處理-7x-建立的索引)） |
| 8.0–8.17 | 先升到 8.19.x 最新 patch → 9.5.x | |
| 8.18.x | 只能直接升到 9.0.x；要升 9.1 以上需先到 8.19.x | 8.18 與 9.0 同時發佈的特例 |
| 8.19.x | 可直接升到任一 9.x | 官方建議的跳板版本 |
| 9.0–9.4 | 直接升到 9.5.x | 目標版本需比目前版本新（版號與發佈日皆較新） |

**元件版本相容性**：

| 規則 | 說明 |
| --- | --- |
| Elasticsearch 與 Kibana | 必須**同版本**（Kibana 不支援與不同版本的 Elasticsearch 長期並存） |
| Logstash、Beats、Elastic Agent | 可落後 Elasticsearch，但不可新於 Elasticsearch |
| 8.19 的 Logstash／Beats／Agent | 相容所有 9.x Elasticsearch，可延後升級收集端 |
| Elasticsearch Client（Java 等） | 依 Client 的相容性說明；9.x 叢集建議使用 9.x Client |

---

### 8.2 升級前準備

#### 8.2.1 升級檢查清單

```text
┌─────────────────────────────────────────────────────────────┐
│                    升級前檢查清單                            │
├─────────────────────────────────────────────────────────────┤
│  □ 1. 確認升級路徑（8.1）與目標版本的支援期限                 │
│  □ 2. 閱讀目標版本之前「每一個」版本的 Breaking Changes        │
│  □ 3. 執行 Kibana Upgrade Assistant，處理所有 Critical 項目    │
│  □ 4. 檢視 Deprecation Logs，確認應用程式未使用將移除的 API     │
│  □ 5. 處理 7.x 建立的索引（reindex / 唯讀 / 封存）             │
│  □ 6. 執行 Snapshot 並確認成功                                │
│  □ 7. 匯出 Kibana Saved Objects、備份所有設定檔               │
│  □ 8. 確認 Plugin、Client、Logstash Plugin 與新版相容          │
│  □ 9. 在與正式環境一致的測試環境完成升級演練                   │
│  □ 10. 確認 Cluster Health 為 green、磁碟有足夠餘裕            │
│  □ 11. 準備回復計畫（8.5）並通知相關人員維護時間                │
└─────────────────────────────────────────────────────────────┘
```

#### 8.2.2 Upgrade Assistant

| 步驟 | 動作 |
| --- | --- |
| 1 | Kibana → **Stack Management** → **Upgrade Assistant** |
| 2 | 檢視 Elasticsearch 與 Kibana 的棄用問題，依 Critical → Warning 順序處理 |
| 3 | 對需要重建的舊索引，直接在介面執行 reindex 或設為唯讀 |
| 4 | 檢視 Deprecation Logs，找出仍使用將移除功能的應用程式 |
| 5 | 全部 Critical 項目清除後才開始升級 |

> ⚠️ **實務注意**：官方明確要求「不要略過 Upgrade Assistant」。從 8.x 升到 9.x 時，必須在 **8.19** 上執行 Upgrade Assistant，才能看到所有與 9.x 相關的檢查項目。

#### 8.2.3 處理 7.x 建立的索引

9.x 無法讀取 7.x（含）以前建立的索引，升級前必須擇一處理：

| 方式 | 適用 | 說明 |
| --- | --- | --- |
| Reindex | 仍需寫入或頻繁查詢 | 轉成 8.x／9.x 格式；小於 10 GB 可在 Upgrade Assistant 介面完成，較大者用 Reindex API |
| 設為唯讀 | 只需查詢的歷史資料 | 標記為唯讀以相容舊格式 |
| 封存（Archive） | 很少查詢的歷史快照 | 透過封存功能直接存取 7.x 快照，不需 reindex |
| 刪除 | 已超過保存期限 | 依保存政策刪除 |

#### 8.2.4 備份策略

```text
# 1. 立即執行一次 SLM 快照（Repository 設定見 7.2）
POST _slm/policy/nightly-snapshots/_execute

# 2. 確認快照狀態為 SUCCESS
GET _snapshot/s3_backup/_current
GET _slm/policy/nightly-snapshots?human
```

```bash
# 3. 匯出 Kibana Saved Objects（每個 Space 需分別匯出）
curl -s -X POST "https://kibana.company.com/api/saved_objects/_export" \
  -H "Authorization: ApiKey ${KIBANA_API_KEY}" \
  -H "kbn-xsrf: true" -H "Content-Type: application/json" \
  -d '{"type": ["dashboard", "visualization", "lens", "index-pattern", "search", "map", "tag"], "includeReferencesDeep": true}' \
  > kibana-saved-objects-default-$(date +%Y%m%d).ndjson

# 4. 備份設定檔與 keystore
sudo tar -czvf elk-config-backup-$(date +%Y%m%d).tar.gz \
  /etc/elasticsearch /etc/logstash /etc/kibana /etc/filebeat
```

> ⚠️ **實務注意**：設定檔備份中含有 keystore 與憑證私鑰，屬機敏資料，應加密保存並限制存取。

---

### 8.3 各元件升級流程

#### 8.3.1 升級順序

```mermaid
graph LR
    A[1. Elasticsearch<br/>Rolling Upgrade] --> B[2. Kibana]
    B --> C[3. Fleet Server]
    C --> D[4. Logstash]
    D --> E[5. Beats / Elastic Agent]
```

Elasticsearch 叢集內的節點順序：

| 順序 | 節點 | 說明 |
| --- | --- | --- |
| 1 | Data 節點，依 Tier：frozen → cold → warm → hot → content | 先升較冷的資料層 |
| 2 | 其他非 master 節點：ML、ingest、coordinating、transform、remote_cluster_client | |
| 3 | Master-eligible 節點（含 voting_only）**最後** | 新版 master 才能管理所有節點 |

#### 8.3.2 Elasticsearch Rolling Upgrade

```bash
# 以下以單一節點為例，依 8.3.1 順序逐台執行

# 1.（選用）停用 Replica 配置，避免節點重啟時大量搬移 Shard
curl -s -X PUT --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" \
  "https://es-node:9200/_cluster/settings" -H 'Content-Type: application/json' \
  -d '{ "persistent": { "cluster.routing.allocation.enable": "primaries" } }'

# 2.（選用）暫停非必要寫入並執行 flush，加速 Shard 復原
curl -s -X POST --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" "https://es-node:9200/_flush"

# 3.（選用，有 ML 時）啟用 ML upgrade mode
curl -s -X POST --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" \
  "https://es-node:9200/_ml/set_upgrade_mode?enabled=true"

# 4. 停止節點
sudo systemctl stop elasticsearch

# 5. 升級套件（指定目標版本）
sudo dnf install -y --enablerepo=elasticsearch elasticsearch-9.5.4
# 或：sudo apt-mark unhold elasticsearch && sudo apt-get install -y elasticsearch=9.5.4 && sudo apt-mark hold elasticsearch

# 6. 合併設定檔變更（.rpmnew／.dpkg-dist）；不要設定 cluster.initial_master_nodes

# 7. 升級 Plugin（若有）
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin list

# 8. 啟動節點並確認已加入叢集
sudo systemctl start elasticsearch
curl -s --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" "https://es-node:9200/_cat/nodes?v&h=name,version,node.role"

# 9. 重新啟用 Shard 配置
curl -s -X PUT --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" \
  "https://es-node:9200/_cluster/settings" -H 'Content-Type: application/json' \
  -d '{ "persistent": { "cluster.routing.allocation.enable": null } }'

# 10. 等待 green 再處理下一台（可用 _cat/recovery 觀察復原進度）
curl -s --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" \
  "https://es-node:9200/_cluster/health?wait_for_status=green&timeout=30m&pretty"

# 11. 全部完成後關閉 ML upgrade mode
curl -s -X POST --cacert http_ca.crt -u "elastic:${ELASTIC_PASSWORD}" \
  "https://es-node:9200/_ml/set_upgrade_mode?enabled=false"
```

> ⚠️ **v2.0 更正**：
>
> - v1.0 步驟 2 使用 `POST _flush/synced`。Synced flush 已於 **8.0 移除**，該請求會失敗；改用 `POST _flush`。
> - v1.0 寫「對下一個節點重複步驟 1–8」且未說明節點順序；正確順序為 Data（由冷到熱）→ 其他 → Master 最後。
> - 混合版本叢集只在 Rolling Upgrade 期間有效，**一旦開始就必須完成所有節點**，不可長期停留在混合狀態。

#### 8.3.3 Kibana 升級

```bash
# 1. 停止「所有」Kibana 執行個體（不支援新舊版本 Kibana 同時連線同一叢集）
sudo systemctl stop kibana   # 每台都要執行

# 2. 升級套件
sudo dnf install -y --enablerepo=elasticsearch kibana-9.5.4

# 3. 先啟動一台，等待 Saved Objects migration 完成
sudo systemctl start kibana
sudo tail -f /var/log/kibana/kibana.log    # 觀察 migration 完成訊息

# 4. 確認狀態後，再啟動其餘執行個體
curl -s -u "elastic:${ELASTIC_PASSWORD}" https://kibana.company.com/api/status | jq '.version.number, .status.overall.level'
```

#### 8.3.4 Logstash 升級

```bash
# 1. 停止 Logstash（Persistent Queue 會保留未處理事件）
sudo systemctl stop logstash

# 2. 升級套件
sudo dnf install -y --enablerepo=elasticsearch logstash-9.5.4

# 3. 更新額外安裝的 Plugin
sudo -u logstash /usr/share/logstash/bin/logstash-plugin update

# 4. 以 logstash 使用者驗證設定檔相容性（9.x 已移除的 SSL 選項會在此報錯）
sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash --config.test_and_exit

# 5. 啟動並驗證
sudo systemctl start logstash
curl -s localhost:9600 | jq '.version'
```

#### 8.3.5 Beats 與 Elastic Agent 升級

| 元件 | 方式 | 注意事項 |
| --- | --- | --- |
| Filebeat | 套件升級後重啟 | 8.x → 9.x 前必須先完成 `log` → `filestream` 遷移（見 [5.4.4](#544-從-log-input-遷移至-filestream)） |
| Fleet 管理的 Elastic Agent | Kibana Fleet → Agents → **Upgrade agent**（可分批、排程） | 先升級 Fleet Server |
| Standalone Elastic Agent | `elastic-agent upgrade <version>` 或重新安裝 | |

---

### 8.4 8.19 → 9.x 重大變更對照

> 🆕 **v2.0 新增**

| 元件 | 變更 | 影響與處置 | 版本 |
| --- | --- | --- | --- |
| Elasticsearch | 無法讀取 7.x 建立的索引 | 升級前 reindex／唯讀／封存 | 9.0 |
| Elasticsearch | Lucene 10；內建 OpenJDK 隨版本更新（9.5.4 為 OpenJDK 26） | 使用內建 JDK 即可 | 9.0+ |
| Elasticsearch | 新 `logs-*-*` Data Stream 預設 LogsDB | 評估儲存與 synthetic source 影響 | 9.0 |
| Elastic Stack | Enterprise Search（App Search、Workplace Search）不再提供 | 改用 Elasticsearch 原生搜尋功能 | 9.0 |
| Logstash | 移除舊 SSL 選項（`ssl`、`ssl_verify_mode` 等） | 改用 `ssl_enabled`、`ssl_client_authentication` | 9.0 |
| Logstash | 預設禁止以 superuser 執行（`allow_superuser: false`） | 以 `logstash` 使用者執行 | 9.0 |
| Logstash | Docker 映像改為 UBI9 基底 | 衍生映像改用 `microdnf` | 9.0 |
| Logstash | 移除 Modules 功能、Enterprise Search Plugin、Ingest Converter | 改用 Integrations 或自建 Pipeline | 9.0 |
| Logstash | Legacy internal monitoring 需明確啟用 | 改用 Metricbeat／Agent 收集 | 9.0 |
| Logstash | 最低 JDK 21 | 使用內建 JDK（9.5.4 內建 21.0.12） | 9.4 |
| Logstash | Kafka integration：移除 `default`、`uniform_sticky` partitioner；`linger_ms` 預設改為 5 ms；移除 `concurrency :legacy`；pipe output 不再內建 | 檢查 Kafka output 設定 | 9.5 |
| Filebeat | 設定含 `log`／`container` input 即拒絕啟動 | 改用 `filestream`（或暫時 `allow_deprecated_use: true`） | 9.0 |
| Filebeat | `filestream` 預設 `file_identity` 改為 fingerprint | 無法遷移狀態的檔案會被重收一次 | 9.0 |
| Filebeat | 預設啟用 growing fingerprint | 小於 1024 bytes 的檔案也會立即收集 | 9.5 |

> 💡 **建議**：本表僅列出與 Log 平台最相關的項目；正式升級前仍須逐一閱讀 [Elasticsearch](https://www.elastic.co/docs/release-notes/elasticsearch/breaking-changes)、[Kibana](https://www.elastic.co/docs/release-notes/kibana/breaking-changes)、[Logstash](https://www.elastic.co/docs/release-notes/logstash/breaking-changes)、[Beats](https://www.elastic.co/docs/release-notes/beats/breaking-changes) 的 Breaking Changes。

---

### 8.5 回復策略

> ⚠️ **v2.0 更正**：v1.0 的回復步驟為 `yum downgrade elasticsearch-8.10.0` 後還原設定與資料。**Elasticsearch 不支援降版**：節點一旦以新版啟動，資料目錄即被升級，舊版無法再讀取；混合版本叢集也只在 Rolling Upgrade 期間有效。

#### 8.5.1 Elasticsearch 回復方式

| 時間點 | 可行做法 |
| --- | --- |
| 尚未停止任何節點 | 取消升級即可 |
| 已開始 Rolling Upgrade | **只能往前**：排除問題後完成所有節點的升級 |
| 升級完成後發現嚴重問題 | 另建**舊版本的新叢集**，從升級前的 Snapshot 還原 |

```text
# 在「舊版本」的新叢集上，註冊同一個 Repository（唯讀）後還原升級前快照
PUT _snapshot/s3_backup
{
  "type": "s3",
  "settings": { "bucket": "elk-prod-snapshots", "base_path": "prod-cluster", "readonly": true }
}

POST _snapshot/s3_backup/nightly-snap-2026.09.30/_restore
{
  "indices": "logs-*",
  "include_global_state": true
}
```

> ⚠️ **實務注意**：Snapshot 只能還原到**相同或更新**版本的叢集，新版叢集產生的快照無法還原到舊版。因此「升級前快照」是唯一的回退依據，升級後寫入的新資料需另以 Kafka 重播或接受遺失。

#### 8.5.2 其他元件回復

| 元件 | 回復方式 |
| --- | --- |
| Kibana | 只能搭配回復後的舊版 Elasticsearch；Saved Objects 以升級前匯出的 `.ndjson` 匯入（新版匯出的檔案無法匯入舊版） |
| Logstash | 可降版套件；PQ 中的事件格式需確認相容，必要時先排空佇列再降版 |
| Filebeat／Agent | 可降版套件；注意 registry 狀態可能已被新版轉換，需評估是否重收 |

```bash
# 匯入升級前備份的 Saved Objects（舊版 Kibana）
curl -s -X POST "https://kibana.company.com/api/saved_objects/_import?overwrite=true" \
  -H "Authorization: ApiKey ${KIBANA_API_KEY}" -H "kbn-xsrf: true" \
  --form file=@kibana-saved-objects-default-20260930.ndjson
```

---

### 8.6 💡 本章實務建議

- 8.x 一律先升到 8.19 最新 patch，在 8.19 上清空 Upgrade Assistant 的 Critical 項目，再升 9.x。
- 升級順序：Elasticsearch（Data 由冷到熱 → 其他 → Master）→ Kibana（全部停機後升級）→ Fleet Server → Logstash → Beats／Agent。
- `_flush/synced` 已移除；Rolling Upgrade 一旦開始就必須完成。
- Elasticsearch 不能降版，「升級前快照 + 舊版新叢集還原」是唯一回退方式，務必演練。
- 每半年規劃一次 minor 升級，避免版本落後導致一次跨越多個 Breaking Changes。

---

## 第九章：安全性與權限管理

### 9.1 Security 基本概念

#### 9.1.1 Elastic Security 架構

```mermaid
graph TB
    subgraph "Security Layer"
        Auth[Authentication<br/>身分驗證：Realm / API Key / Service Account]
        Authz[Authorization<br/>權限控管：Role / Space]
        Enc[Encryption<br/>傳輸加密：HTTP + Transport TLS]
        Audit[Audit Logging<br/>稽核日誌]
    end

    User[使用者 / 應用程式] --> Auth
    Auth --> Authz
    Authz --> ES[Elasticsearch]
    Enc -.->|"TLS"| ES
    ES --> Audit
```

> 📌 **名詞區分**：本章的「Elastic Security 架構」指 Elastic Stack 的**平台安全機制**；Kibana 中名為 **Elastic Security** 的 SIEM／XDR 解決方案是另一個產品，不在本手冊範圍。

#### 9.1.2 9.x 預設的安全狀態

| 項目 | 9.x 預設 | 說明 |
| --- | --- | --- |
| 認證與授權 | ✅ 啟用 | 新安裝即需帳密或 API Key |
| HTTP 層 TLS | ✅ 自動產生憑證 | 套件安裝與 Docker 首次啟動時產生 |
| Transport 層 TLS | ✅ 自動產生憑證 | 多節點正式模式下為強制要求（bootstrap check） |
| Enrollment Token | ✅ 啟用 | 供 Kibana 與新節點加入 |
| `action.destructive_requires_name` | ✅ `true` | 禁止以萬用字元一次刪除多個索引 |

> ⚠️ **v2.0 更正**：v1.0 的「啟用 Security」段落是 7.x 時代需要手動開啟的做法。9.x 安全性預設即啟用，重點已轉為「憑證治理、最小權限與稽核」。

#### 9.1.3 TLS 憑證規劃

| 憑證 | 用途 | 建議來源 |
| --- | --- | --- |
| Transport 憑證 | ES 節點之間 | 叢集專用 CA（可用 `elasticsearch-certutil`），每節點一張 |
| HTTP 憑證 | Client → ES（Kibana、Logstash、應用程式） | 企業 PKI；SAN 需涵蓋所有節點 DNS／IP |
| Kibana 憑證 | 瀏覽器 → Kibana | 企業 PKI 或對外憑證（通常放在 LB／Reverse Proxy） |
| Logstash Beats input 憑證 | Filebeat → Logstash | 企業 PKI；需要 mTLS 時另發 Client 憑證 |

```bash
# 以 elasticsearch-certutil 建立叢集專用 CA 與 Transport 憑證（PKCS#12）
cd /usr/share/elasticsearch
sudo bin/elasticsearch-certutil ca --out /tmp/elastic-stack-ca.p12
sudo bin/elasticsearch-certutil cert --ca /tmp/elastic-stack-ca.p12 \
  --name es-hot-01 --dns es-hot-01.company.local --ip 10.0.1.21 \
  --out /tmp/es-hot-01-transport.p12

# HTTP 憑證：互動式精靈，可產生 CSR 交由企業 PKI 簽發
sudo bin/elasticsearch-certutil http
```

```yaml
# elasticsearch.yml
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: full     # 驗證主機名稱
xpack.security.transport.ssl.keystore.path: certs/transport.p12
xpack.security.transport.ssl.truststore.path: certs/transport.p12

xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.keystore.path: certs/http.p12
```

```bash
# keystore 密碼存入 Elasticsearch keystore（不可寫在 yml）
sudo bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password
sudo bin/elasticsearch-keystore add xpack.security.transport.ssl.truststore.secure_password
sudo bin/elasticsearch-keystore add xpack.security.http.ssl.keystore.secure_password
```

> ⚠️ **v2.0 更正**：v1.0 使用 `verification_mode: certificate`（只驗證憑證鏈、不驗證主機名稱）。正式環境建議 `full`，並確保憑證 SAN 正確。

#### 9.1.4 憑證到期管理與輪替

```text
# 查詢各節點載入的憑證與到期日
GET _ssl/certificates?filter_path=*.path,*.subject_dn,*.expiry
```

| 作業 | 做法 |
| --- | --- |
| 到期監控 | 以上述 API 每日檢查，到期前 60 天告警 |
| 同一 CA 換發 | 以新檔案覆蓋相同路徑，Elasticsearch 會自動偵測檔案變更並重新載入 |
| 更換 CA | 先將新舊 CA 同時加入 truststore，全部節點更新後再移除舊 CA |
| Client 端 | Kibana、Logstash、Filebeat 的 CA 設定需同步更新 |

---

### 9.2 身分驗證

> 🆕 **v2.0 新增**

| 方式 | 用途 | 授權 |
| --- | --- | --- |
| Native realm | Elasticsearch 內建使用者 | Basic |
| File realm | 緊急管理帳號（存於各節點檔案） | Basic |
| API Key | 程式化存取（Logstash、Filebeat、腳本、CI/CD） | Basic |
| Service Account | Elastic 元件專用（`elastic/kibana`、`elastic/fleet-server`） | Basic |
| PKI realm | 以 Client 憑證驗證 | Basic |
| LDAP／Active Directory | 企業目錄整合 | 💰 付費 |
| SAML／OpenID Connect | 單一登入（Keycloak、Entra ID 等） | 💰 付費 |
| Kerberos、JWT | 特定整合 | 💰 付費 |

**API Key 管理原則**：

```text
# 建立具有效期限與最小權限的 API Key
POST _security/api_key
{
  "name": "filebeat-app-servers",
  "expiration": "180d",
  "role_descriptors": {
    "filebeat_writer": {
      "cluster": ["monitor"],
      "indices": [
        { "names": ["logs-*"], "privileges": ["auto_configure", "create_doc"] }
      ]
    }
  },
  "metadata": { "owner": "platform-team", "ticket": "CHG-20261001-01" }
}

# 查詢即將到期或指定名稱的 API Key
GET _security/api_key?name=filebeat-*

# 撤銷
DELETE _security/api_key
{ "name": "filebeat-app-servers" }
```

> 💡 **建議**：每組收集端（例如每個環境的 Filebeat 群）使用不同 API Key，並設定有效期限、於 `metadata` 記錄負責人與變更單號；撤銷單一 Key 不會影響其他來源。

---

### 9.3 使用者與角色管理

#### 9.3.1 內建角色

| 角色 | 說明 | 適用對象 |
| --- | --- | --- |
| `superuser` | 完整權限 | 僅限緊急使用，日常不使用 |
| `kibana_admin` | Kibana 所有功能的管理權限 | Kibana 管理員 |
| `editor`／`viewer` | Kibana 所有功能的編輯／唯讀權限（含資料讀取） | 快速授權，正式環境建議改用自訂角色 |
| `monitoring_user` | 檢視 Stack Monitoring | 監控人員 |
| `remote_monitoring_collector` | 收集監控資料 | Metricbeat |
| `kibana_system` | Kibana 伺服器連線 Elasticsearch | 只給 `kibana_system` 使用者，**不可**指派給人 |
| `logstash_system` | Logstash **上報監控資料** | 不具寫入 Log 的權限 |
| `beats_system` | Beats 上報監控資料 | 不具寫入 Log 的權限 |
| `logstash_admin` | 管理 Logstash 集中管理的 Pipeline | 平台管理員 |
| `ingest_admin` | 管理 Ingest Pipeline 與範本 | 平台管理員 |

> ⚠️ **v2.0 更正**：v1.0 將 `logstash_system`、`beats_system` 描述為「Logstash」「Filebeat」使用的角色，容易被誤用為寫入帳號。這兩個角色只用於上報監控資料；寫入 Log 應使用自訂角色或 API Key（見 [9.3.4](#934-收集端最小權限)）。

#### 9.3.2 建立自訂角色

**做法一（Basic 授權即可）：以 Data Stream namespace 區分環境**

```bash
# 使用 Kibana Role API，一次定義資料權限與 Kibana Space 權限
curl -s -X PUT "https://kibana.company.com/api/security/role/app_developer" \
  -H "Authorization: ApiKey ${KIBANA_API_KEY}" -H "kbn-xsrf: true" -H "Content-Type: application/json" \
  -d '{
    "elasticsearch": {
      "cluster": [],
      "indices": [
        { "names": ["logs-*-dev", "logs-*-sit"], "privileges": ["read", "view_index_metadata"] }
      ]
    },
    "kibana": [
      { "base": ["read"], "spaces": ["dev"] }
    ]
  }'
```

**做法二（💰 付費）：Document／Field Level Security**

```text
PUT _security/role/order_team_prod_reader
{
  "indices": [
    {
      "names": ["logs-*-prod"],
      "privileges": ["read"],
      "query": { "term": { "service.name": "order-service" } },
      "field_security": { "grant": ["*"], "except": ["user.email", "client.ip"] }
    }
  ]
}
```

```text
# 建立使用者（未導入 SSO 時）
POST _security/user/dev_user
{
  "password": "<strong-password>",
  "roles": ["app_developer"],
  "full_name": "開發人員",
  "email": "dev@company.com"
}
```

> ⚠️ **v2.0 更正**：v1.0 的自訂角色在 Basic 授權下使用了 `query`（Document Level Security），該功能需付費授權，否則角色建立後無法生效。Basic 環境應以 `logs-*-<namespace>` 的命名方式在索引層級隔離環境。

#### 9.3.3 實務角色設計

```text
┌─────────────────────────────────────────────────────────────┐
│                    角色設計建議                              │
├──────────────┬──────────────────────────────────────────────┤
│ 角色         │ 權限範圍                                     │
├──────────────┼──────────────────────────────────────────────┤
│ elk_admin    │ 平台管理（範本、ILM、SLM、角色），非 superuser │
│ ops_team     │ 讀取所有 logs-*-*，可建立 Dashboard 與告警     │
│ dev_team     │ 只能讀取 logs-*-dev、logs-*-sit                │
│ security     │ 讀取所有 Log 與稽核資料                        │
│ auditor      │ 唯讀，可匯出 CSV；匯出行為需被記錄            │
│ business     │ 僅能檢視指定 Space 的 Dashboard                │
└──────────────┴──────────────────────────────────────────────┘
```

#### 9.3.4 收集端最小權限

> 🆕 **v2.0 新增**

| 收集端 | Cluster 權限 | Index 權限（`logs-*`） | 備註 |
| --- | --- | --- | --- |
| Logstash（只寫入 Data Stream） | `monitor` | `auto_configure`、`create_doc` | 需管理範本時再加 `manage_index_templates` |
| Filebeat 直送 | `monitor` | `auto_configure`、`create_doc` | 執行 `filebeat setup` 時另用管理用 Key |
| Prometheus exporter | `monitor` | `monitor`（`*`） | 唯讀 |
| Metricbeat（Stack Monitoring） | 內建 `remote_monitoring_collector`、`remote_monitoring_agent` | — | 寫入獨立監控叢集 |

---

### 9.4 企業資安考量

#### 9.4.1 敏感資料處理

**原則**：敏感資料在**寫入 Elasticsearch 之前**遮蔽；查詢時才過濾（FLS）只能作為第二道防線。

```ruby
# Logstash：敏感資料遮蔽
filter {
  mutate {
    gsub => [
      # 身分證字號與新式居留證號（英文字母 + 1/2/8/9 開頭 + 8 碼數字）
      "message", "\b[A-Z][1289]\d{8}\b", "[ID_MASKED]",
      # 信用卡號（13–19 碼，允許空白或連字號分隔）
      "message", "\b(?:\d[ -]?){12,18}\d\b", "[CARD_MASKED]",
      # 台灣手機號碼
      "message", "\b09\d{2}-?\d{3}-?\d{3}\b", "[MOBILE_MASKED]",
      # Email
      "message", "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[EMAIL_MASKED]"
    ]
  }

  # 以 HMAC 將使用者 ID 假名化：仍可關聯同一使用者，但無法還原
  if [user][id] {
    fingerprint {
      source => "[user][id]"
      target => "[user][id]"
      method => "SHA256"
      key => "${USER_ID_HMAC_KEY}"
    }
  }

  # 移除任何層級中名稱為敏感字的欄位
  prune {
    blacklist_names => ["^password$", "^passwd$", "^token$", "^secret$", "^authorization$"]
  }
}
```

```text
# Ingest Pipeline 版本（Basic 可用 gsub；redact processor 為付費功能）
PUT _ingest/pipeline/logs@custom
{
  "description": "所有 logs-*-* 共用的遮蔽規則（由 logs@default-pipeline 自動呼叫）",
  "processors": [
    { "gsub": { "field": "message", "pattern": "\\b[A-Z][1289]\\d{8}\\b", "replacement": "[ID_MASKED]", "ignore_missing": true } },
    { "gsub": { "field": "message", "pattern": "\\b09\\d{2}-?\\d{3}-?\\d{3}\\b", "replacement": "[MOBILE_MASKED]", "ignore_missing": true } }
  ]
}
```

> ⚠️ **實務注意**：
>
> - `prune` 只處理事件的第一層欄位；巢狀欄位需另以 `remove_field` 指定完整路徑。
> - 正規表達式遮蔽必然存在漏網與誤判，應搭配「應用程式不記錄敏感資料」的開發規範與定期抽樣稽核。
> - v1.0 的信用卡規則只比對 16 碼且要求固定分隔，已擴充為 13–19 碼。

#### 9.4.2 稽核日誌

> 💰 **授權**：Elasticsearch 與 Kibana 的稽核日誌皆為付費功能。

```yaml
# elasticsearch.yml（所有節點）
xpack.security.audit.enabled: true
xpack.security.audit.logfile.events.include:
  - access_denied
  - authentication_failed
  - connection_denied
  - tampered_request
  - run_as_denied
  - anonymous_access_denied
  - security_config_change
# 輸出：/var/log/elasticsearch/<cluster_name>_audit.json
```

```yaml
# kibana.yml
xpack.security.audit.enabled: true
```

| 建議 | 說明 |
| --- | --- |
| 稽核日誌送往獨立叢集 | 以 Filebeat 收集 `_audit.json` 到獨立的稽核／監控叢集，避免管理員自行刪改 |
| 謹慎開啟 `access_granted` | 量極大，僅在調查期間短期開啟 |
| 保存期限 | 依主管機關規範與內部政策訂定，建議至少 1 年 |

#### 9.4.3 網路安全建議

```text
┌─────────────────────────────────────────────────────────────┐
│                    網路安全建議                              │
├─────────────────────────────────────────────────────────────┤
│  1. 9200／9300 只對必要來源開放；9300 僅限叢集節點之間        │
│  2. Kibana 經 Reverse Proxy / LB 對外，啟用 HTTPS（TLS 1.2+）│
│  3. Logstash 5044 僅開放給 Filebeat 主機，建議 mTLS           │
│  4. Logstash 9600 維持只綁 127.0.0.1                         │
│  5. API Key 設定有效期限並定期輪替；離職／異動即撤銷           │
│  6. 啟用稽核日誌（付費）並集中保存                            │
│  7. 敏感資料在寫入前遮蔽，不依賴查詢時過濾                    │
│  8. 訂閱 Elastic Security Announcements，安全修補 30 天內完成 │
└─────────────────────────────────────────────────────────────┘
```

#### 9.4.4 法規與內控對照

> 🆕 **v2.0 新增**

| 控制目標 | 參考依據（舉例） | ELK 實作 |
| --- | --- | --- |
| 日誌集中保存與完整性 | ISO/IEC 27001:2022 A.8.15 Logging | 集中收集、唯讀角色、Snapshot、稽核叢集分離 |
| 活動監控 | ISO/IEC 27001:2022 A.8.16 Monitoring activities | Kibana Alerting、異常偵測（付費） |
| 時鐘同步 | ISO/IEC 27001:2022 A.8.17 Clock synchronization | 所有主機 NTP／chrony；以 UTC 儲存 |
| 個資最小化與安全維護 | 個人資料保護法 | 寫入前遮蔽、假名化、FLS（付費）、保存期限 |
| 存取控管與存取紀錄 | 金融業資安相關規範與內控制度 | RBAC、SSO（付費）、稽核日誌（付費） |
| 保存期限 | 主管機關與內部政策 | ILM `delete.min_age`、Snapshot 保存政策 |

> ⚠️ **實務注意**：本表為技術對照示例，實際適用條文與保存期限請由法遵與資安單位確認。

---

### 9.5 💡 本章實務建議

- 保留 9.x 預設安全設定；正式環境改用企業 PKI，`verification_mode: full`，並監控憑證到期。
- 人員使用 SSO（付費）或 Native 使用者；程式一律使用有期限、最小權限的 API Key。
- Basic 授權以 `logs-*-<namespace>` 命名在索引層級隔離環境；DLS／FLS 屬付費功能。
- 敏感資料在 Logstash 或 `logs@custom` Ingest Pipeline 寫入前遮蔽，並以 HMAC 假名化識別碼。
- 稽核日誌（付費）送往獨立叢集保存；網路層只開放必要埠並採 mTLS。

---

## 第十章：最佳實務與導入建議

### 10.1 導入常見踩雷點

| # | ❌ 常見錯誤 | ✅ 正確做法 | 參考章節 |
| --- | --- | --- | --- |
| 1 | Log 量估算錯誤 | 先在測試環境量測實際 Log 量與 LogsDB 壓縮比，再套用容量公式 | [2.5](#25-容量規劃與-sizing) |
| 2 | 沒有自訂保存期限，以為內建 ILM 會刪資料 | 內建 `logs` 政策只 rollover 不刪除；上線前以 `logs@custom` 套用自訂政策 | [7.1.2](#712-index-lifecycle-managementilm) |
| 3 | 所有 Log 都收集 | 過濾 DEBUG、Health Check、重複的框架 Log | [5.3.2](#532-步驟-2filebeat-filestream-設定) |
| 4 | 每個服務每天一個索引、多個 Shard | Data Stream + 依大小 rollover；小流量 1 個 Primary | [4.1.5](#415-shard-數量規劃) |
| 5 | 沒有監控 ELK 本身 | `_health_report` + Stack Monitoring（獨立監控叢集） | [7.4](#74-健康檢查與監控) |
| 6 | 直接在 Production 調整設定 | 設定以版本控制管理，先在測試環境驗證 | [第八章](#第八章系統升級) |
| 7 | 關閉 Security 圖方便 | 9.x 預設安全設定不得關閉；全鏈路 TLS + API Key | [第九章](#第九章安全性與權限管理) |
| 8 | 沒有備份或從未還原過 | SLM 每日快照 + 每季還原演練 | [7.2](#72-snapshot-與-slm) |
| 9 | Logstash 與應用程式部署在同一台 | Filebeat 在 App Server，Logstash 獨立部署 | [5.4.2](#542-推薦架構) |
| 10 | 使用純文字 Log 格式 | 應用端輸出 ECS JSON | [5.3.1](#531-步驟-1應用程式-log-設定) |
| 11 | 同名欄位型別不一致（mapping 衝突） | 制定欄位規範，自訂欄位放在 `app.*` 命名空間 | [5.5](#55-ecs-與欄位命名規範) |
| 12 | 規劃時忽略授權 | 外部通知、DLS／FLS、稽核、SSO 皆需付費，預算階段即確認 | [1.5](#15-授權模式與功能層級) |
| 13 | 延用網路上的 7.x／8.x 舊教學 | 以 9.x 官方文件與 Breaking Changes 為準 | [第十四章](#第十四章版本演進與新功能9095) |
| 14 | 長期不升級 | 每半年升級一次 minor，8.19 只作為過渡 | [1.6](#16-版本發佈節奏與支援策略) |

---

### 10.2 結構化 Log 設計原則

#### 10.2.1 推薦的 Log 格式（ECS JSON）

```json
{
  "@timestamp": "2026-09-30T06:30:00.123Z",
  "log.level": "INFO",
  "log.logger": "com.company.order.OrderService",
  "process.thread.name": "http-nio-8080-exec-1",
  "message": "Order created successfully",
  "service.name": "order-service",
  "service.version": "1.4.2",
  "service.environment": "prod",
  "host.name": "app-server-01",
  "trace.id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span.id": "00f067aa0ba902b7",
  "user.id": "U12345",
  "event.duration": 150000000,
  "app": {
    "order_id": "ORD-20260930-001",
    "amount": 1500,
    "product_count": 3
  }
}
```

#### 10.2.2 Log 設計原則

| 原則 | 說明 |
| --- | --- |
| **結構化** | 使用 JSON（ECS），非純文字 |
| **標準欄位** | `@timestamp`（UTC）、`log.level`、`service.name`、`trace.id` 必備 |
| **業務欄位** | 包含足夠的業務 Context（訂單編號等），放在 `app.*` 命名空間 |
| **型別一致** | 同名欄位在所有服務型別相同；耗時統一單位 |
| **適量** | Production 預設 INFO；DEBUG 只在排查期間以動態調整開啟 |
| **可關聯** | 包含 `trace.id`，可與 APM／Tracing 關聯 |
| **不含個資** | 不記錄密碼、Token、身分證、卡號；使用者以 ID 或假名識別 |
| **事件化** | 重要業務事件使用一致的 `event.action`（例如 `order.created`），便於統計與稽核 |

---

### 10.3 與 AI 分析結合

#### 10.3.1 AI 輔助查詢範例

```text
👤 使用者問：「昨天有多少訂單失敗？失敗的主要原因是什麼？」

🤖 AI 轉換為 ES|QL：
FROM logs-order_service-prod
| WHERE log.level == "ERROR"
  AND @timestamp >= DATE_TRUNC(1 day, NOW()) - 1 day
  AND @timestamp <  DATE_TRUNC(1 day, NOW())
| STATS failures = COUNT(*) BY error.type
| SORT failures DESC

📊 AI 整理結果：
「昨天共有 156 筆訂單失敗，主要原因：
  1. PaymentTimeoutException: 78 筆 (50%)
  2. InventoryNotAvailableException: 45 筆 (29%)
  3. UserNotFoundException: 33 筆 (21%)

  建議：優先調查 payment-service 的連線問題」
```

> ⚠️ **實務注意**：`DATE_TRUNC(1 day, NOW())` 以 UTC 計算日界；若需以台灣時間的「昨天」統計，應明確換算時間範圍。AI 產生的查詢必須由人檢查時間範圍與條件後再採信結果。

#### 10.3.2 將 Log 作為 AI Prompt 輸入

```text
# 範例：將「已去識別化」的 Error Log 整理給 AI 分析

Prompt：
"""
以下是系統錯誤日誌（已移除個資），請分析可能的根因並提供解決建議：

[2026-09-30T06:30:01Z] ERROR order-service OrderService - Failed to process order
  java.net.SocketTimeoutException: Read timed out
    at java.base/sun.nio.ch.NioSocketImpl.timedRead(NioSocketImpl.java:288)
    at com.company.payment.PaymentClient.charge(PaymentClient.java:89)
    at com.company.order.OrderService.processOrder(OrderService.java:45)

[2026-09-30T06:30:02Z] WARN order-service ConnectionPool - Pool exhausted, waiting for connection
  pool_size: 10, active: 10, waiting: 5

[2026-09-30T06:30:03Z] ERROR order-service PaymentClient - Connection refused to payment-service:8080
"""

AI 回應：
「根據日誌分析，問題可能是：
1. payment-service 回應緩慢導致連線池耗盡（10 個連線全部占用）
2. payment-service 可能過載或部分執行個體已停止

建議行動：
1. 檢查 payment-service 健康狀態與同時段延遲指標
2. 檢視 Connection Pool 與 Timeout 設定是否合理
3. 加入 Circuit Breaker 與重試退避，避免連鎖故障」
```

#### 10.3.3 Elastic 內建 AI 功能與治理

> 🆕 **v2.0 新增**

| 功能 | 說明 | 狀態／授權 |
| --- | --- | --- |
| AI Assistant（Observability） | 以對話方式解釋 Log、產生 ES\|QL、協助根因分析 | 💰 Enterprise；需設定 LLM Connector |
| Agent Builder | 建立可查詢 Elasticsearch 資料的自訂 AI Agent | 9.3 起 GA；💰 Enterprise |
| Streams AI 解析建議 | 依樣本 Log 建議 Grok／Dissect 規則 | 需 Generative AI Connector |
| Log 異常偵測、Log rate analysis | ML 自動找出異常與變化原因 | 💰 付費 |
| Workflows | 結合腳本與 AI 推理的自動化流程（9.4 GA，9.5 支援人工核准） | 依授權 |

**導入 AI 的治理檢查**：

| 檢查項目 | 說明 |
| --- | --- |
| 資料是否離開組織 | 外部 LLM Connector 會將查詢內容與 Log 片段送出；優先使用內部部署或核准的模型服務 |
| 去識別化 | 送出前完成遮蔽與假名化（見 [9.4.1](#941-敏感資料處理)） |
| 權限繼承 | AI 只能讀取使用者本身有權限的資料 |
| 結果驗證 | AI 結論必須以原始 Log 與指標佐證，不得直接作為事故結論 |
| 紀錄保存 | 保存 AI 對話與產生的查詢，供事後稽核 |

---

### 10.4 與 Prometheus／Grafana 分工

```mermaid
graph TB
    subgraph "問題發現"
        P[Prometheus + Grafana]
        N1[監控指標異常<br/>Error Rate ↑ / Latency ↑]
    end

    subgraph "問題分析"
        E[ELK Stack]
        N2[查詢詳細 Log<br/>找到 Error Message]
    end

    subgraph "根因定位"
        T[Tracing - Jaeger / Elastic APM]
        N3[追蹤完整請求鏈路<br/>定位瓶頸服務]
    end

    P --- N1
    E --- N2
    T --- N3
    P --> E --> T
```

#### 10.4.1 分工建議

| 問題類型 | 使用工具 | 說明 |
| --- | --- | --- |
| 系統層級監控 | Prometheus + Grafana | CPU、Memory、Disk、Network |
| 應用層級監控 | Prometheus + Grafana | Request Rate、Error Rate、Latency |
| 問題詳細分析 | ELK | Error Log、Stack Trace、業務 Log |
| 請求鏈路追蹤 | Jaeger／Elastic APM | 微服務呼叫鏈路、效能瓶頸 |
| 即時告警 | Alertmanager（指標）＋ Kibana Alerting（Log） | 統一通知通道與命名 |
| 歷史趨勢分析 | Grafana + Kibana | 長期趨勢、容量規劃 |

> 💡 **建議**：Elastic 9.5 已將 Prometheus 指標接收與 PromQL 列為 GA，並提供 Grafana Dashboard 遷移工具。若組織希望減少平台數量，可另行評估整併；在評估完成前，維持「Prometheus 管指標、ELK 管 Log」的分工最穩定。

---

### 10.5 導入路線圖

> 🆕 **v2.0 新增**

```mermaid
graph LR
    P1["階段一：基礎建置<br/>（1–2 個月）"] --> P2["階段二：標準化<br/>（2–3 個月）"]
    P2 --> P3["階段三：維運成熟<br/>（3–6 個月）"]
    P3 --> P4["階段四：智慧化<br/>（持續）"]
```

| 階段 | 目標 | 主要工作 | 完成標準 |
| --- | --- | --- | --- |
| 一、基礎建置 | 平台可用 | 叢集建置（3 Master + Hot／Warm）、TLS、API Key、SLM、ILM、首批 3–5 個服務接入 | 首批服務 Log 可查詢、每日快照成功 |
| 二、標準化 | 一致的資料 | ECS JSON 規範、欄位命名、Data Stream 命名、遮蔽規則、Dashboard 範本 | 新服務依規範一週內接入 |
| 三、維運成熟 | 可靠與可控 | Stack Monitoring、告警與 Runbook、容量檢討、升級演練、權限盤點 | 季度還原演練與升級演練完成 |
| 四、智慧化 | 提升效率 | ES\|QL 分析範本、異常偵測、AI Assistant（依授權）、與 Tracing 整合 | MTTR 有可量測的下降 |

---

### 10.6 💡 本章實務建議

- 上線前逐項檢查 10.1 的 14 個踩雷點，特別是「內建 ILM 不刪資料」與「授權」。
- 以 ECS JSON 作為全公司 Log 標準，自訂欄位一律放在 `app.*`。
- AI 是加速器而非裁判：資料先去識別化、結論需佐證、對話需留存。
- 維持 Prometheus 管指標、ELK 管 Log 的分工，以 `trace.id` 與 Data Link 串接。
- 依四階段路線圖推進，每階段設定可驗收的完成標準。

---

## 第十一章：OpenTelemetry 與 EDOT 整合

> 🆕 **v2.0 新增**

### 11.1 為什麼要導入 OpenTelemetry

OpenTelemetry（OTel）是 CNCF 的可觀測性標準，統一定義 Traces、Metrics、Logs 的資料模型與傳輸協定（OTLP）。Elastic 9.x 已將 OTel 作為一級資料來源。

| 面向 | 傳統 Beats／Logstash | OpenTelemetry |
| --- | --- | --- |
| 標準 | Elastic 專有（ECS） | 廠商中立（OTel Semantic Conventions） |
| 涵蓋範圍 | 以 Log 為主 | Traces、Metrics、Logs 一致 |
| 關聯 | 需自行帶入 `trace.id` | Log 自動帶有 TraceId／SpanId |
| 可攜性 | 綁定 Elastic | 可同時送往多個後端 |
| 成熟度（Log） | 非常成熟 | 已穩定，但檔案收集與解析的生態仍在快速發展 |

> 💡 **建議**：已有穩定的 Filebeat／Logstash 架構不必全面改寫；新的微服務、或已導入 OTel Tracing 的團隊，可優先讓 Log 也走 OTel，以取得 Trace 與 Log 的天然關聯。

---

### 11.2 EDOT 元件

EDOT（Elastic Distributions of OpenTelemetry）是 Elastic 維護、與上游相容的 OTel 發行版。

| 元件 | 說明 |
| --- | --- |
| EDOT Collector | Elastic 的 OTel Collector 發行版；**9.5 起內建於 Elastic Agent**，可由 Agent 套件中的 `otelcol` 執行 |
| EDOT SDK／Agent | Java、.NET、Node.js、Python、PHP 及行動裝置 SDK；Java 以 `-javaagent` 方式零程式碼導入 |
| Elasticsearch exporter | Collector 將資料寫入 Elasticsearch 的元件，支援 `otel`、`ecs` 等 mapping 模式 |

| 部署模式 | 用途 |
| --- | --- |
| Agent 模式 | 部署在每台主機／每個節點，收集本機 Log 與指標，並接收應用程式的 OTLP 資料 |
| Gateway 模式 | 集中接收 Agent 模式 Collector 的 OTLP 資料（4317 gRPC／4318 HTTP），做批次與轉換後寫入 Elasticsearch |

```mermaid
graph LR
    subgraph "應用主機"
        APP[Java App<br/>EDOT Java Agent]
        FILE[Log 檔案]
        C1[EDOT Collector<br/>Agent 模式]
    end

    GW[EDOT Collector<br/>Gateway 模式]
    ES[Elasticsearch]
    KB[Kibana]

    APP -->|"OTLP"| C1
    FILE -->|"filelog receiver"| C1
    C1 -->|"OTLP 4317"| GW
    GW -->|"elasticsearch exporter"| ES
    ES --> KB
```

---

### 11.3 以 EDOT Collector 收集 Log 檔

```bash
# 下載 Elastic Agent 套件（內含 EDOT Collector）
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-9.5.4-linux-x86_64.tar.gz
tar xzvf elastic-agent-9.5.4-linux-x86_64.tar.gz
cd elastic-agent-9.5.4-linux-x86_64

# 設定連線資訊（API Key 權限同 9.3.4 的收集端最小權限）
export ELASTIC_ENDPOINT="https://es-hot-01:9200"
export ELASTIC_API_KEY="<encoded-api-key>"

# 以 OTel Collector 模式執行
sudo -E ./otelcol --config otel.yml
```

```yaml
# otel.yml（Agent 模式：收集主機 Log 檔與應用程式 JSON Log）
extensions:
  file_storage:
    directory: /var/lib/otelcol/file_storage   # 保存讀取位置，重啟不重收

receivers:
  filelog/platformlogs:
    include: [ /var/log/*.log ]
    start_at: end
    storage: file_storage
    retry_on_failure:
      enabled: true

  filelog/applogs:
    include: [ /var/log/myapp/*.json ]
    start_at: end
    storage: file_storage
    operators:
      - type: json_parser
        timestamp:
          parse_from: attributes["@timestamp"]
          layout_type: gotime
          layout: "2006-01-02T15:04:05.000Z07:00"

processors:
  resourcedetection:
    detectors: ["system"]
    system:
      hostname_sources: ["os"]

exporters:
  elasticsearch/otel:
    endpoints: ["${env:ELASTIC_ENDPOINT}"]
    api_key: ${env:ELASTIC_API_KEY}
    tls:
      ca_file: /etc/otelcol/certs/http_ca.crt
    mapping:
      mode: otel

service:
  extensions: [file_storage]
  pipelines:
    logs/platformlogs:
      receivers: [filelog/platformlogs]
      processors: [resourcedetection]
      exporters: [elasticsearch/otel]
    logs/applogs:
      receivers: [filelog/applogs]
      processors: [resourcedetection]
      exporters: [elasticsearch/otel]
```

> ⚠️ **實務注意**：`filelog` receiver 未設定 `storage` 時，Collector 重啟後會依 `start_at` 重新開始讀取，可能遺漏或重複資料。正式環境務必搭配 `file_storage` extension，並將目錄放在持久化磁碟。

---

### 11.4 Mapping 模式：otel 與 ecs

| 面向 | `otel`（EDOT 預設） | `ecs` |
| --- | --- | --- |
| 欄位結構 | 保留 OTel 語意：`resource.attributes.*`、`attributes.*`、`body.text` 等 | 轉換為 ECS 欄位名稱（`service.name`、`host.name`…） |
| Data Stream | OTel 原生 Data Stream（名稱含 `.otel`，例如 `logs-generic.otel-default`） | 一般 `logs-*-*` |
| 與既有 Dashboard／告警相容 | 需確認查詢欄位；Kibana 對常用欄位提供別名 | 與 Filebeat／ECS 資料一致 |
| 建議 | 新建的 OTel-first 專案 | 與既有 ECS 資料混用、沿用既有 Dashboard |

> 💡 **建議**：同一個服務的 Log 只選一種 mapping 模式。若既有告警與 Dashboard 都以 ECS 欄位撰寫，先用 `ecs` 模式平滑導入，再逐步評估改為 `otel`。

---

### 11.5 Wired Streams 端點

Streams 的 wired streams（見 [6.4](#64-streams-與-log-解析)）提供受管理的寫入端點：

| 版本 | 寫入目標 |
| --- | --- |
| 9.2–9.3 | `logs` |
| 9.4 以上 | `logs.otel`（OTel 格式）或 `logs.ecs`（ECS 格式） |

```yaml
# EDOT Collector 寫入 wired stream（9.4+）
exporters:
  elasticsearch/otel:
    endpoints: ["${env:ELASTIC_ENDPOINT}"]
    api_key: ${env:ELASTIC_API_KEY}
    logs_index: logs.otel
    mapping:
      mode: otel
```

> ⚠️ **實務注意**：使用 wired streams 時，需手動建立涵蓋 `logs,logs.*` 的 Data View，並加入 Kibana Advanced Settings 的 `observability:logSources`，相關介面才會顯示這些資料。

---

### 11.6 選型：Filebeat 與 EDOT Collector

| 情境 | 建議 |
| --- | --- |
| 既有 Filebeat → Logstash 架構穩定 | 維持現狀 |
| 新微服務、已導入 OTel Tracing | 應用程式以 EDOT SDK 輸出 Log 與 Trace，Collector 以 Gateway 模式集中 |
| Kubernetes 叢集 | 評估 EDOT Collector（DaemonSet）或 Elastic Agent Kubernetes Integration |
| 需要 Logstash 的複雜解析與遮蔽 | Collector 可輸出 OTLP 至 Logstash（`otlp` input 依 Logstash 版本確認）或維持 Filebeat |
| 多後端（同時送 Elastic 與其他平台） | OTel Collector 的多 exporter 最具彈性 |

---

### 11.7 💡 本章實務建議

- OTel 是長期方向，但不必為了導入而重寫穩定的 Filebeat／Logstash 架構。
- EDOT Collector 9.5 起內建於 Elastic Agent；`filelog` receiver 一定要搭配 `file_storage`。
- 同一服務只選一種 mapping 模式；既有 ECS Dashboard 多時先用 `ecs` 模式。
- 以 Trace 與 Log 的自動關聯作為導入 OTel 的主要效益指標。

---

## 第十二章：Kubernetes 部署（ECK）

> 🆕 **v2.0 新增**

### 12.1 ECK 概述與相容性

ECK（Elastic Cloud on Kubernetes）是 Elastic 官方的 Kubernetes Operator，以 CRD 管理 Elasticsearch、Kibana、Logstash、Beats、Elastic Agent 的部署、TLS、擴縮與 Rolling Upgrade。

| 項目 | 內容（2026-10-01） |
| --- | --- |
| 最新版本 | ECK 3.5.0（2026-08-04） |
| Kubernetes | 1.31–1.36；OpenShift 4.16–4.22；GKE、AKS、EKS |
| Elasticsearch／Kibana | 8.x、9.x |
| Beats／Elastic Agent | 8.x、9.x |
| Logstash | 8.12 以上、9.x |
| Helm | 3.2.0 以上 |
| 授權 | ECK 本身可用 Basic；Enterprise 授權可啟用進階 Operator 功能 |

> 💡 **建議**：在 Kubernetes 上請使用 ECK，而非自行撰寫 StatefulSet 部署 Elasticsearch；ECK 會依正確順序執行 Rolling Upgrade、管理憑證與 PodDisruptionBudget。

---

### 12.2 安裝 ECK Operator

```bash
# 方式一：YAML Manifest
kubectl create -f https://download.elastic.co/downloads/eck/3.5.0/crds.yaml
kubectl apply -f https://download.elastic.co/downloads/eck/3.5.0/operator.yaml

# 方式二：Helm
helm repo add elastic https://helm.elastic.co
helm repo update
helm install elastic-operator elastic/eck-operator -n elastic-system --create-namespace

# 確認 Operator 運作
kubectl -n elastic-system get pods
kubectl -n elastic-system logs -f statefulset.apps/elastic-operator
```

---

### 12.3 部署 Elasticsearch 與 Kibana

```yaml
# elk-prod.yaml
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: elk-prod
  namespace: logging
spec:
  version: 9.5.4
  nodeSets:
    - name: master
      count: 3
      config:
        node.roles: ["master"]
      podTemplate:
        spec:
          containers:
            - name: elasticsearch
              resources:
                requests: { cpu: "2", memory: 8Gi }
                limits: { memory: 8Gi }
      volumeClaimTemplates:
        - metadata:
            name: elasticsearch-data
          spec:
            accessModes: ["ReadWriteOnce"]
            storageClassName: fast-ssd
            resources:
              requests:
                storage: 50Gi

    - name: hot
      count: 3
      config:
        node.roles: ["data_hot", "data_content", "ingest"]
      podTemplate:
        spec:
          containers:
            - name: elasticsearch
              resources:
                requests: { cpu: "8", memory: 32Gi }
                limits: { memory: 32Gi }
      volumeClaimTemplates:
        - metadata:
            name: elasticsearch-data
          spec:
            accessModes: ["ReadWriteOnce"]
            storageClassName: fast-ssd
            resources:
              requests:
                storage: 1Ti
---
apiVersion: kibana.k8s.elastic.co/v1
kind: Kibana
metadata:
  name: elk-prod
  namespace: logging
spec:
  version: 9.5.4
  count: 2
  elasticsearchRef:
    name: elk-prod
```

```bash
kubectl create namespace logging
kubectl apply -f elk-prod.yaml
kubectl -n logging get elasticsearch,kibana

# 取得 elastic 使用者密碼（Secret 名稱為 <叢集名稱>-es-elastic-user）
kubectl -n logging get secret elk-prod-es-elastic-user -o go-template='{{.data.elastic | base64decode}}'

# 本機存取 Kibana（Service 名稱為 <名稱>-kb-http）
kubectl -n logging port-forward service/elk-prod-kb-http 5601
```

| 項目 | 說明 |
| --- | --- |
| Heap | ECK 依容器 `limits.memory` 自動推導 Heap，不需設定 `ES_JAVA_OPTS` |
| `vm.max_map_count` | 建議在節點層級設定（DaemonSet／節點初始化腳本）；無法設定時才以 `node.store.allow_mmap: false` 替代（會降低效能） |
| TLS | ECK 預設為 HTTP 與 Transport 自動簽發憑證；可改用自備憑證（`spec.http.tls.certificate`） |
| 服務名稱 | `elk-prod-es-http`（ES）、`elk-prod-kb-http`（Kibana） |

---

### 12.4 Kubernetes Log 收集

以 ECK 的 `Beat` 資源部署 Filebeat DaemonSet，使用 autodiscover 搭配 `filestream` 與 `container` parser：

```yaml
apiVersion: beat.k8s.elastic.co/v1beta1
kind: Beat
metadata:
  name: filebeat
  namespace: logging
spec:
  type: filebeat
  version: 9.5.4
  elasticsearchRef:
    name: elk-prod
  config:
    filebeat.autodiscover:
      providers:
        - type: kubernetes
          node: ${NODE_NAME}
          hints.enabled: true
          hints.default_config:
            type: filestream
            id: kubernetes-container-logs-${data.kubernetes.pod.name}-${data.kubernetes.container.id}
            paths:
              - /var/log/containers/*-${data.kubernetes.container.id}.log
            parsers:
              - container: ~
            prospector.scanner.symlinks: true
    processors:
      - add_host_metadata: {}
  daemonSet:
    podTemplate:
      spec:
        serviceAccountName: filebeat
        automountServiceAccountToken: true
        dnsPolicy: ClusterFirstWithHostNet
        hostNetwork: true
        securityContext:
          runAsUser: 0
        containers:
          - name: filebeat
            env:
              - name: NODE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: spec.nodeName
            volumeMounts:
              - name: varlogcontainers
                mountPath: /var/log/containers
              - name: varlogpods
                mountPath: /var/log/pods
        volumes:
          - name: varlogcontainers
            hostPath:
              path: /var/log/containers
          - name: varlogpods
            hostPath:
              path: /var/log/pods
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: filebeat
  namespace: logging
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: filebeat
rules:
  - apiGroups: [""]
    resources: ["namespaces", "pods", "nodes"]
    verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: filebeat
subjects:
  - kind: ServiceAccount
    name: filebeat
    namespace: logging
roleRef:
  kind: ClusterRole
  name: filebeat
  apiGroup: rbac.authorization.k8s.io
```

> ⚠️ **實務注意**：Filebeat 9.x 已不能使用 `container` input；Kubernetes 容器 Log 應以 `filestream` + `parsers: - container` 收集，且每個 input 的 `id` 必須唯一（上例以 Pod 名稱與 Container ID 組成）。

| 替代方案 | 說明 |
| --- | --- |
| Elastic Agent（Fleet 管理）+ Kubernetes Integration | 同時收集容器 Log、K8s 指標與事件；9.5 起 Kubernetes 監控方案為 GA |
| EDOT Collector DaemonSet | OTel-first 架構（見第十一章） |

應用程式可透過 Pod annotation（hints）調整收集方式，例如排除不需收集的 Pod：

```yaml
metadata:
  annotations:
    co.elastic.logs/enabled: "false"
```

> ⚠️ **實務注意**：其他 hints 註解（例如指定 parser、multiline）的鍵名會隨 Filebeat 版本與 input 類型調整，正式使用前請以 9.5 的 Hints based autodiscover 文件確認（見 [E.1 待確認事項](#e1-待確認事項)）。

---

### 12.5 資源、儲存與排程建議

| 項目 | 建議 |
| --- | --- |
| 記憶體 | `requests.memory` 等於 `limits.memory`，避免被驅逐；Heap 由 ECK 自動推導 |
| CPU | 設定 requests；limits 可不設或設高，避免 GC 被節流 |
| 儲存 | 使用本機 NVMe 或高效能 SSD 的 StorageClass；`volumeBindingMode: WaitForFirstConsumer` |
| 反親和 | ECK 預設對同一叢集的 Pod 設定 soft anti-affinity；正式環境可改為 hard |
| 可用區 | 依 ECK 文件設定 zone awareness，讓 Primary／Replica 分散在不同可用區 |
| 中斷預算 | ECK 預設建立 PodDisruptionBudget；節點維護前確認叢集為 green |
| 專用節點池 | Elasticsearch 使用專用 Node Pool（taint／toleration），避免與應用程式搶資源 |

---

### 12.6 升級與維運

| 作業 | 做法 |
| --- | --- |
| 升級 Elastic Stack | 修改 `spec.version`（例如 9.4.7 → 9.5.4）並 `kubectl apply`，ECK 依正確順序執行 Rolling Upgrade |
| 升級 ECK Operator | 先套用新版 CRD，再升級 Operator；依 ECK Release Notes 確認相容性 |
| Snapshot | 以 `spec.secureSettings` 注入 S3 憑證，再用 SLM API 建立政策（見 [7.2](#72-snapshot-與-slm)） |
| 擴充節點 | 修改 nodeSet 的 `count`；縮減時 ECK 會先搬移資料 |
| 設定變更 | 修改 `config` 後 ECK 會逐台重啟 |

```yaml
# 以 secureSettings 注入 S3 憑證
spec:
  secureSettings:
    - secretName: es-s3-credentials   # 內含 s3.client.default.access_key／secret_key
```

---

### 12.7 💡 本章實務建議

- Kubernetes 上一律以 ECK 3.5 管理 Elastic Stack，升級改 `spec.version` 即可。
- 記憶體 requests = limits，Heap 交給 ECK 推導；`vm.max_map_count` 在節點層級設定。
- 容器 Log 以 `filestream` + `container` parser 收集，`id` 需唯一。
- Elasticsearch 使用專用節點池與高效能 StorageClass，並設定跨可用區分散。

---

## 第十三章：故障排除與營運手冊

> 🆕 **v2.0 新增**

### 13.1 排查總流程

```mermaid
graph TD
    S[收到異常：查不到 Log / 告警 / 使用者回報] --> H{"_health_report<br/>是否 green？"}
    H -->|否| R[依指標處理<br/>13.2–13.5]
    H -->|是| I{"Data Stream 最新資料<br/>時間是否正常？"}
    I -->|否| P{"Logstash 有收到事件嗎？"}
    I -->|是| K[Kibana / 查詢問題<br/>13.8]
    P -->|否| F[Filebeat / 收集端<br/>13.7]
    P -->|是| L[Logstash / 寫入<br/>13.5–13.6、13.9]
```

```text
# 1. 叢集健康
GET _health_report

# 2. 某 Data Stream 最新一筆資料時間
GET logs-order_service-prod/_search
{ "size": 1, "sort": [{ "@timestamp": "desc" }], "_source": ["@timestamp", "service.name"] }

# 3. 解析失敗或被拒的文件（failure store）
GET logs-order_service-prod::failures/_search
{ "size": 5, "sort": [{ "@timestamp": "desc" }] }
```

---

### 13.2 叢集 Red／Yellow

| 狀態 | 意義 | 影響 |
| --- | --- | --- |
| Yellow | 所有 Primary 已配置，部分 Replica 未配置 | 資料可讀寫，但容錯能力下降 |
| Red | 至少一個 Primary 未配置 | 該索引部分資料無法查詢或寫入 |

```text
# 找出未配置的 Shard
GET _cat/shards?v&h=index,shard,prirep,state,unassigned.reason&s=state

# 讓 Elasticsearch 說明原因（不帶 body 時解釋第一個未配置的 Shard）
GET _cluster/allocation/explain
{
  "index": ".ds-logs-order_service-prod-2026.09.30-000012",
  "shard": 0,
  "primary": true
}
```

| 常見原因（explain 輸出） | 處置 |
| --- | --- |
| 節點離開叢集（`NODE_LEFT`） | 確認節點狀態；節點回來後會自動復原 |
| 磁碟超過 watermark | 見 [13.3](#133-磁碟水位與唯讀索引) |
| Allocation awareness／filter 限制 | 檢查 `node.attr.*` 與 `index.routing.allocation.*` 設定 |
| 單節點叢集設定 Replica | 開發環境將 Replica 設為 0 |
| 重試次數用盡（`max_retries`） | 修正根因後執行 `POST _cluster/reroute?retry_failed=true` |
| 資料損毀或 Primary 所在節點永久遺失 | 從 Snapshot 還原該索引；**最後手段**才使用 `allocate_stale_primary`（可能遺失資料） |

---

### 13.3 磁碟水位與唯讀索引

| 水位 | 預設值 | 行為 |
| --- | --- | --- |
| low | 85% | 不再將新的 Shard 配置到該節點 |
| high | 90% | 嘗試將 Shard 搬離該節點 |
| flood_stage | 95% | 該節點上有 Shard 的索引被設為 `index.blocks.read_only_allow_delete`，**寫入全部失敗** |

> 📌 大容量磁碟另有 `max_headroom` 上限（low 200 GB、high 150 GB、flood_stage 100 GB），避免大磁碟保留過多空間。

**處理步驟**：

```text
# 1. 確認各節點磁碟使用
GET _cat/allocation?v&h=node,disk.percent,disk.avail,shards&s=disk.percent:desc

# 2. 找出最大的 backing index
GET _cat/indices/.ds-logs-*?v&h=index,store.size,creation.date.string&s=store.size:desc&bytes=gb

# 3. 釋放空間：刪除已超過保存期限的 backing index（或縮短 ILM 保存期限後等待執行）
DELETE .ds-logs-debug_tool-dev-2026.08.01-000003

# 4. 磁碟降到 high watermark 以下後，唯讀封鎖會自動解除；確認是否仍有封鎖
GET logs-*/_settings/index.blocks.read_only_allow_delete?flat_settings=true
```

> ⚠️ **實務注意**：不要以調高 watermark 作為長期解法；應檢討保存期限、LogsDB、Tier 配置或擴充節點。水位問題常是「內建 ILM 不刪資料」造成（見 [7.1.2](#712-index-lifecycle-managementilm)）。

---

### 13.4 JVM 記憶體與 Circuit Breaker

**典型錯誤**：

```text
circuit_breaking_exception: [parent] Data too large, data for [<http_request>] would be [...], which is larger than the limit of [...]
```

```text
# 檢查各 breaker 使用量與觸發次數
GET _nodes/stats/breaker?filter_path=nodes.*.name,nodes.*.breakers.parent,nodes.*.breakers.fielddata

# 檢查 Heap 使用與 GC
GET _nodes/stats/jvm?filter_path=nodes.*.name,nodes.*.jvm.mem.heap_used_percent,nodes.*.jvm.gc
```

| 原因 | 處置 |
| --- | --- |
| 大型聚合（高基數 `terms`、過多 bucket） | 縮小時間範圍、降低 `size`、改用 composite 聚合分頁 |
| 對 `text` 欄位聚合（fielddata） | 改用 `keyword` 欄位；不要開啟 fielddata |
| Shard 數過多 | 合併小 Data Stream、調整 rollover 條件 |
| 欄位數過多 | 控制動態欄位（見 [13.9](#139-mapping-爆量與欄位衝突)） |
| Heap 本身過小 | 確認自動 Heap 是否受容器或手動設定限制 |

---

### 13.5 寫入被拒（429）

**典型錯誤**：`es_rejected_execution_exception` 或 HTTP 429 Too Many Requests。

```text
GET _cat/thread_pool/write?v&h=node_name,active,queue,rejected,completed
```

| 原因 | 處置 |
| --- | --- |
| 寫入量超過 Hot 節點能力 | 擴充 Hot 節點、增加 Primary Shard 分散寫入 |
| 寫入集中在少數節點（hot spot） | Logstash 列出所有 Hot 節點；確認 Shard 平均分布 |
| Bulk 過大或過小 | 調整為每批 5–15 MB |
| 磁碟 I/O 瓶頸 | 確認使用本機 SSD，避免網路儲存 |

> 💡 **建議**：Logstash 與 Filebeat 遇到 429 會自動退避重試，短暫的拒絕不會遺失資料；但持續發生表示容量不足，應擴充而非加大 `thread_pool.write.queue_size`。

---

### 13.6 Logstash 背壓與管線阻塞

```bash
# 1. Pipeline flow 與各 Plugin 耗時
curl -s localhost:9600/_node/stats/pipelines | jq '.pipelines[] | {flow, plugins: [.plugins.filters[] | {name, ms: .events.duration_in_millis, out: .events.out}]}'

# 2. 熱點執行緒
curl -s "localhost:9600/_node/hot_threads?human=true&threads=5"

# 3. Persistent Queue 與 DLQ 使用量
curl -s localhost:9600/_node/stats/pipelines | jq '.pipelines[] | {queue: .queue, dlq: .dead_letter_queue}'
```

| 症狀 | 可能原因 | 處置 |
| --- | --- | --- |
| `queue_backpressure` 高、ES 無錯誤 | Filter 運算瓶頸（grok） | 改用 dissect、增加 worker 或 Logstash 節點 |
| Log 出現大量 429／重試 | Elasticsearch 寫入能力不足 | 見 [13.5](#135-寫入被拒429) |
| Log 出現 400 mapping 錯誤 | 欄位型別衝突 | 檢查 DLQ，修正欄位規範（見 [13.9](#139-mapping-爆量與欄位衝突)） |
| PQ 持續增長 | 下游長時間不可用 | 先恢復下游；PQ 滿時會對 Filebeat 施加背壓 |
| 啟動失敗 `Unknown setting` | 9.x 已移除的選項 | 見 [4.2.4](#424-input-設定範例) 新舊選項對照 |

---

### 13.7 Filebeat 不收或重複收

| 症狀 | 可能原因 | 處置 |
| --- | --- | --- |
| 啟動即失敗 | 設定含 `log`／`container` input | 改用 `filestream` |
| 新檔案一直不收 | 8.x–9.4：檔案小於 1024 bytes（fingerprint） | 升級 9.5（growing fingerprint）或調整 `file_identity` |
| 升級後整批重收 | `filestream` 缺少 `id` 或 `id` 被修改；狀態無法遷移到 fingerprint | 固定 `id`；8.x 先以 `take_over` 遷移 |
| 權限不足 | Filebeat 無法讀取應用程式 Log | 調整檔案群組或 ACL，避免以 root 以外的方式繞過 |
| Log 輪替後遺失尾段 | 輪替後檔案過早關閉 | 檢查 `close.on_state_change.*` 設定 |
| 送不出去 | TLS 或認證錯誤 | `filebeat test output` |

```bash
# 前景除錯（先停止服務）
sudo systemctl stop filebeat
sudo filebeat -e -c /etc/filebeat/filebeat.yml -d "input,harvester,publisher"

# 檢視 registry（讀取位置）
sudo ls -l /var/lib/filebeat/registry/filebeat/
```

---

### 13.8 Kibana 異常

| 症狀 | 可能原因 | 處置 |
| --- | --- | --- |
| `Kibana server is not ready yet` | 無法連線 Elasticsearch，或 Saved Objects migration 進行中／失敗 | 檢查 `kibana.log`；確認 ES 為 green 且版本相同 |
| 升級後無法啟動 | 多台 Kibana 版本不一致 | 停止所有執行個體，統一版本後再啟動 |
| 告警 Connector 失效 | `xpack.encryptedSavedObjects.encryptionKey` 未固定或不一致 | 所有 Kibana 使用相同金鑰（見 [3.4.3](#343-設定加密金鑰)） |
| Dashboard 很慢 | 時間範圍過大、高基數聚合 | 縮短預設時間範圍；以 Inspect 檢視查詢耗時 |
| 登入後看不到資料 | 角色缺少索引權限或 Space 權限 | 檢查角色的 `indices` 與 `kibana.spaces` |

```bash
curl -s -u "elastic:${ELASTIC_PASSWORD}" https://kibana.company.com/api/status \
  | jq '{version: .version.number, overall: .status.overall.level, core: .status.core}'
```

---

### 13.9 Mapping 爆量與欄位衝突

| 問題 | 說明 | 處置 |
| --- | --- | --- |
| 欄位數超過上限 | `index.mapping.total_fields.limit` 預設 1000；內建 `logs@settings` 啟用 `ignore_dynamic_beyond_limit`，超過的欄位**不會被索引**（但保留在 `_source`） | 找出動態欄位來源，改為 `flattened` 或停止輸出 |
| 欄位型別衝突 | 同名欄位一個服務送字串、另一個送數字 | 內建範本啟用 `ignore_malformed` 與 failure store；制定欄位規範 |

```text
# 找出有欄位被忽略的文件
GET logs-*-prod/_search
{
  "size": 5,
  "query": { "exists": { "field": "_ignored" } },
  "_source": ["service.name"],
  "fields": ["_ignored"]
}

# 查看 failure store 中的失敗原因
GET logs-*-prod::failures/_search
{
  "size": 5,
  "_source": ["error.type", "error.message", "document.index"]
}
```

```text
# 將不可控的動態結構改為 flattened（寫入 logs@custom）
PUT _component_template/logs@custom
{
  "template": {
    "mappings": {
      "properties": {
        "app": {
          "properties": {
            "extra": { "type": "flattened" }
          }
        }
      }
    }
  }
}
```

---

### 13.10 💡 本章實務建議

- 先看 `_health_report`，再看「最新資料時間」，再沿收集鏈路逐段排查。
- Red／Yellow 一律先用 `_cluster/allocation/explain` 找原因，不要直接 reroute。
- 磁碟水位問題的根因多半是保存期限；不要以調高 watermark 長期解決。
- 429 與 circuit breaker 代表容量或查詢設計問題，擴充或修正查詢，而非放大佇列與門檻。
- 定期檢查 `_ignored` 與 failure store，及早發現欄位規範被破壞。

---

## 第十四章：版本演進與新功能（9.0→9.5）

> 🆕 **v2.0 新增**

### 14.1 9.x 版本時間軸

```mermaid
graph LR
    A["9.0<br/>2025-04-15"] --> B["9.1 / 8.19<br/>2025-07-29"]
    B --> C["9.2<br/>2025-10-23"]
    C --> D["9.3<br/>2026-02-03"]
    D --> E["9.4<br/>2026-05-05"]
    E --> F["9.5<br/>2026-08-04"]
```

| 版本 | 發佈日 | 支援狀態（2026-10-01） | 最新 Patch |
| --- | --- | --- | --- |
| 9.5 | 2026-08-04 | ✅ 支援中（本手冊基準） | 9.5.4 |
| 9.4 | 2026-05-05 | ✅ 支援中 | 9.4.7 |
| 9.3 | 2026-02-03 | ❌ 2026-08-04 結束 | 9.3.8 |
| 9.2 | 2025-10-23 | ❌ 2026-05-05 結束 | 9.2.8 |
| 9.1 | 2025-07-29 | ❌ 2026-02-03 結束 | 9.1.10 |
| 9.0 | 2025-04-15 | ❌ 2025-10-23 結束 | 9.0.8 |
| 8.19 | 2025-07-29 | ✅ 支援至 2027-07-15 | 8.19.22 |

---

### 14.2 各版本重點（與 Log 平台相關）

| 版本 | 重點 | 成熟度 |
| --- | --- | --- |
| **9.0** | Lucene 10；新 `logs-*-*` Data Stream 預設 LogsDB；7.x 索引不再支援；Enterprise Search 移除 | GA |
| 9.0 | Filebeat：`log`／`container` input 預設拒絕啟動；`filestream` 預設 fingerprint | GA |
| 9.0 | Logstash：移除舊 SSL 選項、預設禁止 superuser、UBI9 映像、移除 Modules | GA |
| **9.1／8.19** | ES\|QL `LOOKUP JOIN` GA、ES\|QL 跨叢集查詢 GA；Streams 首次推出 | GA／Preview |
| 9.1／8.19 | 8.19 的 Agent／Beats／Logstash 相容所有 9.x Elasticsearch | — |
| **9.2** | Streams GA；ES\|QL 支援多欄位與比較條件的 lookup join、Discover 原生時間序列分析 | GA |
| 9.2 | 內建 `logs` 範本啟用 failure store | GA |
| **9.3** | Agent Builder GA；以 Pattern 為基礎的 Log 壓縮；ES\|QL 時間序列分析改善 | GA |
| **9.4** | Workflows GA；ES\|QL 時間序列函數（`rate`、`changes` 等）GA；Prometheus／PromQL 支援推出 | GA／Technical Preview |
| 9.4 | ES\|QL 子查詢、近似查詢、邏輯 View | Technical Preview |
| 9.4 | Wired streams 端點改為 `logs.otel`／`logs.ecs`；Logstash 最低 JDK 21 | GA |
| **9.5** | 原生 PromQL 與 Grafana／Datadog Dashboard 遷移工具 GA；Dashboards & Visualizations API GA | GA |
| 9.5 | Columnar Mode（以欄式儲存、無倒排索引的索引模式），主打更低的儲存與長期保存成本 | Technical Preview |
| 9.5 | Elastic Agent 內建 EDOT Collector；Kubernetes 監控方案 GA | GA |
| 9.5 | Filebeat 預設 growing fingerprint；Logstash Kafka integration 預設值調整 | GA |
| 9.5 | Workflows 支援人工核准（可送至 Slack 等外部工具）、自然語言撰寫 Workflow | GA |

---

### 14.3 對 Log 平台的影響評估

| 新功能 | 對本手冊架構的影響 | 建議 |
| --- | --- | --- |
| LogsDB（9.0 預設） | 儲存成本最多可降約 60% | 新叢集直接採用；由 8.x 升級者評估既有 Data Stream 是否改用 |
| failure store（9.2） | 解析或 mapping 失敗的文件不再直接遺失 | 納入每日維運檢查（見 [7.5](#75-日常維運作業)） |
| ES\|QL + LOOKUP JOIN | 查詢時即可補上服務負責人等資訊，減少寫入時 enrichment | 建立團隊共用的 ES\|QL 查詢範本 |
| Streams（9.2 GA） | 提供 Logstash 以外的解析與分流選項 | 由平台團隊決定使用範圍，避免規則分散 |
| EDOT Collector（9.5 內建於 Agent） | OTel 收集正式進入 Elastic 主線 | 新服務優先評估 OTel（第十一章） |
| PromQL（9.5 GA） | Elastic 可同時承擔 Metrics | 另案評估是否整併 Prometheus 長期儲存 |
| Columnar Mode（9.5 TP） | 長期保存的 Log 可能進一步降低成本 | 僅在測試環境評估，待 GA 後再規劃 |
| Agent Builder／Workflows | AI 輔助調查與自動化處置 | 依授權與 AI 治理政策試點（見 [10.3.3](#1033-elastic-內建-ai-功能與治理)） |

> ⚠️ **實務注意**：Technical Preview 功能可能在後續版本變更或移除，不在 Elastic 正式支援範圍，正式環境不建議依賴。

---

### 14.4 💡 本章實務建議

- 以「最新 minor 的最新 patch」為基準，並在 minor 版本 EOS 前完成升級。
- 每次 minor 升級前，以本章表格為索引，再到官方 Release Notes 確認細節。
- 新功能先在測試環境驗證，GA 後才規劃上線；Technical Preview 只做評估。
- 將 LogsDB、failure store、ES|QL 列為 9.x 平台的標準能力，納入設計與維運規範。

---

## 附錄 A：檢查清單

### A.1 安裝檢查清單

- [ ] 作業系統在 Elastic Support Matrix 支援清單內（RHEL 8／9 系列、Ubuntu 22.04／24.04 等）
- [ ] 所有元件版本完全一致（9.5.4），並以 `--enablerepo`／`apt-mark hold` 鎖定
- [ ] Swap 已關閉或已設定 `bootstrap.memory_lock` + `LimitMEMLOCK=infinity`
- [ ] 非套件安裝的主機已設定 `vm.max_map_count=262144`
- [ ] 時間同步（chrony／NTP）正常
- [ ] 資料目錄使用本機 SSD（XFS／ext4），非 NFS
- [ ] `elastic` 密碼、`http_ca.crt` 已妥善保存
- [ ] 防火牆只開放必要埠（9200、9300 限叢集、5601、5044；9600 維持本機）
- [ ] 服務設定開機自動啟動

### A.2 設定檢查清單

- [ ] `cluster.name`、`node.name`、`node.roles` 已依角色設定
- [ ] 多節點：`discovery.seed_hosts` 正確；叢集成立後已移除 `cluster.initial_master_nodes`
- [ ] HTTP 與 Transport TLS 均啟用，`verification_mode: full`
- [ ] Heap 採自動計算，或手動設定且確認 Compressed OOPs 為 `true`
- [ ] `elasticsearch.yml` 中沒有任何 `index.*` 設定
- [ ] `logs@custom` 已設定自訂 ILM 政策（含 delete 階段）
- [ ] Logstash 使用新 SSL 選項、Data Stream output、API Key（存於 keystore）
- [ ] Logstash 啟用 Persistent Queue 與 DLQ
- [ ] Kibana 三組加密金鑰已設定且所有執行個體一致
- [ ] Kibana `i18n.locale` 為支援值；`defaultRoute`、`dateFormat:tz` 已於 Advanced Settings 設定
- [ ] 敏感資料遮蔽規則已部署並以樣本驗證

### A.3 上線檢查清單

- [ ] `_health_report` 為 green
- [ ] Filebeat 已部署至 App Server，`filestream` 每個 input 有唯一 `id`
- [ ] 資料寫入預期的 Data Stream（`logs-{dataset}-{namespace}`），`index_mode` 為 `logsdb`
- [ ] Kibana Data View 已建立，可查詢到資料
- [ ] 基本 Dashboard 與 Saved Search 已建立
- [ ] 告警規則已設定，通知通道已測試
- [ ] SLM 快照政策已設定，且已成功執行一次
- [ ] Stack Monitoring 已啟用（獨立監控叢集）或 Prometheus exporter 已接入
- [ ] 角色與 Space 依團隊設定完成，已移除日常使用 `elastic` 帳號的情況

### A.4 維運檢查清單

**每日**：

- [ ] `_health_report` 狀態與未配置 Shard
- [ ] 前一日 Snapshot 成功
- [ ] 磁碟使用率 < 80%、Heap 無持續高水位
- [ ] Write／Search thread pool 無持續拒絕
- [ ] Logstash 無持續背壓；DLQ 與 failure store 無異常增加
- [ ] 無未處理的告警

**每週／每月**：

- [ ] ILM 無錯誤（`_ilm/explain?only_errors=true`）
- [ ] Shard 數與欄位數成長趨勢正常
- [ ] 容量趨勢與保存期限檢討
- [ ] 檢查新版本與安全公告

### A.5 升級檢查清單

- [ ] 確認升級路徑（8.x 先到 8.19）
- [ ] 閱讀目標版本之前所有版本的 Breaking Changes
- [ ] Upgrade Assistant 無 Critical 項目
- [ ] 7.x 建立的索引已處理
- [ ] 升級前 Snapshot 成功
- [ ] Kibana Saved Objects 已依 Space 匯出；設定檔與 keystore 已備份
- [ ] 測試環境演練通過
- [ ] 回復計畫已準備（舊版新叢集 + 快照還原）
- [ ] 已通知相關人員維護時間

### A.6 安全檢查清單

- [ ] 安全性未被關閉，所有連線皆為 TLS
- [ ] 正式環境使用企業 PKI 憑證，到期監控已設定
- [ ] 人員帳號：SSO（付費）或 Native 使用者，無共用帳號
- [ ] 程式存取一律使用具有效期限、最小權限的 API Key
- [ ] `kibana_system`、`logstash_system`、`beats_system` 未被指派給人或用於寫入資料
- [ ] Basic 授權下以 namespace 隔離環境；付費授權下評估 DLS／FLS
- [ ] 敏感資料於寫入前遮蔽，抽樣稽核無外洩
- [ ] 稽核日誌（付費）已啟用並送往獨立叢集
- [ ] 每季權限盤點完成

---

## 附錄 B：常見 Q&A

### B.1 Q1：忘記 elastic 密碼怎麼辦？

在任一節點執行 `sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -i`。該工具需要節點正常運作；若叢集無法使用 `elastic`，可先以 file realm 建立緊急管理帳號（`elasticsearch-users useradd`）。

### B.2 Q2：單節點叢集為什麼一直是 yellow？

`logs-*-*` 內建範本預設 1 個 Replica，單節點無處配置。開發環境在 `logs@custom` 設定 `index.number_of_replicas: 0`；正式環境應改為多節點。

### B.3 Q3：Log 已經寫進去，但 Discover 查不到？

依序檢查：(1) 時間選擇器範圍與時區；(2) Data View 的 index pattern 是否涵蓋該 Data Stream；(3) 使用者角色是否有該索引的 `read` 權限；(4) `@timestamp` 是否被解析成錯誤時間（例如未來時間）；(5) 是否寫入 failure store。

### B.4 Q4：如何讓保存期限依服務不同？

為該服務建立 priority > 100 的專屬 Index Template（見 [4.1.4](#414-index-template-與-component-template)），在其中指定不同的 ILM 政策；或對單一 Data Stream 使用 DSL 設定 `data_retention`。

### B.5 Q5：可以不用 Logstash 嗎？

可以。Log 已是 ECS JSON 且不需複雜轉換時，Filebeat 或 Elastic Agent 直送 Elasticsearch（必要時搭配 Ingest Pipeline）即可。需要複雜解析、遮蔽、多目的地或緩衝時才加入 Logstash（見 [5.2](#52-收集端選型)）。

### B.6 Q6：Basic 授權能不能發送告警到 Teams？

Kibana 的 Microsoft Teams、Email、Slack、Webhook 等 Connector 需付費授權。Basic 環境可用 Index Connector 寫入告警索引，再由既有監控系統（例如 Grafana／Alertmanager）讀取並通知（見 [6.3.2](#632-connector-與授權)）。

### B.7 Q7：Kibana 可以顯示繁體中文嗎？

Kibana 9.5 內建語系只有英文、簡體中文（`zh-CN`）、日文、法文、德文，沒有繁體中文。企業內部可選擇英文或簡體中文；`i18n.locale: "zh-TW"` 不是有效值。

### B.8 Q8：從 8.x 升到 9.x，Filebeat 要注意什麼？

必須先把所有 `log`／`container` input 改為 `filestream`（每個都有唯一 `id`），並在 8.19 上以 `take_over` 完成遷移，確認無重複與遺漏後再升級；否則 Filebeat 9.x 會拒絕啟動，或因 file identity 改變而重收（見 [5.4.4](#544-從-log-input-遷移至-filestream)）。

### B.9 Q9：升級後發現問題，可以降版嗎？

不行。Elasticsearch 不支援降版，Rolling Upgrade 一旦開始就必須完成。唯一回退方式是建立舊版本的新叢集，從升級前的 Snapshot 還原（見 [8.5](#85-回復策略)）。

### B.10 Q10：ELK 和 OpenSearch 可以混用嗎？

不建議。兩者自 2021 年分家後各自演進，API、Client、功能（例如 ES|QL、LogsDB）與授權都不同。選定其一後，Client、收集端與文件都應以該產品為準（見 [1.5.3](#153-與-opensearch-的差異)）。

---

## 附錄 C：指令與 API 速查

### C.1 Elasticsearch

| 目的 | 指令／API |
| --- | --- |
| 叢集健康 | `GET _cluster/health`、`GET _health_report` |
| 節點概況 | `GET _cat/nodes?v&h=name,node.role,heap.percent,disk.used_percent` |
| 未配置原因 | `GET _cluster/allocation/explain` |
| Data Stream | `GET _data_stream/logs-*`、`POST <ds>/_rollover` |
| ILM 錯誤 | `GET */_ilm/explain?only_errors=true` |
| 快照 | `GET _slm/stats`、`POST _slm/policy/<id>/_execute` |
| 憑證 | `GET _ssl/certificates` |
| 重設密碼 | `bin/elasticsearch-reset-password -u <user> -i` |
| Enrollment Token | `bin/elasticsearch-create-enrollment-token -s kibana｜node` |
| 新節點加入 | `bin/elasticsearch-reconfigure-node --enrollment-token <token>` |
| Keystore | `bin/elasticsearch-keystore add <setting>` |

### C.2 Logstash

| 目的 | 指令／API |
| --- | --- |
| 測試設定 | `sudo -u logstash bin/logstash --path.settings /etc/logstash --config.test_and_exit` |
| Pipeline 統計 | `curl localhost:9600/_node/stats/pipelines` |
| 熱點執行緒 | `curl localhost:9600/_node/hot_threads` |
| 動態調整 Log 等級 | `PUT localhost:9600/_node/logging` |
| Keystore | `bin/logstash-keystore --path.settings /etc/logstash add <KEY>` |
| Plugin 更新 | `bin/logstash-plugin update` |

### C.3 Kibana

| 目的 | 指令／API |
| --- | --- |
| 狀態 | `GET /api/status` |
| 以 Token 連線 ES | `bin/kibana-setup --enrollment-token <token>` |
| 產生加密金鑰 | `bin/kibana-encryption-keys generate` |
| Keystore | `bin/kibana-keystore add <setting>` |
| Data View | `POST /api/data_views/data_view` |
| Saved Objects | `POST /api/saved_objects/_export`、`POST /api/saved_objects/_import` |
| Space | `POST /api/spaces/space` |
| 角色 | `PUT /api/security/role/<name>` |

### C.4 Filebeat 與 Elastic Agent

| 目的 | 指令 |
| --- | --- |
| 驗證設定 | `filebeat test config` |
| 驗證輸出 | `filebeat test output` |
| 前景除錯 | `filebeat -e -d "input,harvester,publisher"` |
| Module | `filebeat modules enable <name>`、`filebeat setup --pipelines --modules <name>` |
| Keystore | `filebeat keystore add <KEY>` |
| 安裝 Agent | `elastic-agent install --url=<fleet> --enrollment-token=<token>` |
| 執行 EDOT Collector | `./otelcol --config otel.yml` |

---

## 附錄 D：版本紀錄

### D.1 版本歷程

| 版本 | 日期 | 內容 | 作者 |
| --- | --- | --- | --- |
| 1.0 | 2026-01-29 | 初版，以 Elastic Stack 8.12 為基準 | Eric Cheng |
| 2.0 | 2026-10-01 | 全面對齊 Elastic Stack 9.5.4；修正 v1.0 錯誤與過時內容 41 項；新增 4 章與 40 餘節；補齊附錄 | Eric Cheng |

### D.2 v1.0 → v2.0 更正表

| # | v1.0 位置 | v1.0 內容 | 問題 | v2.0 修正 | 對應章節 |
| --- | --- | --- | --- | --- | --- |
| 1 | 開頭 | 版本資訊重複（兩個「最後更新」）、行尾空白斷行 | 格式問題 | 文件資訊表格、TOC 自動產生 | [文件資訊](#文件資訊) |
| 2 | 1.4、2.5 | Elasticsearch Watcher 發送 Teams 告警 | 付費功能、已非主要機制 | Kibana Alerting Rules + Connectors | [6.3](#63-告警alerting) |
| 3 | 2.3 | 以 Master／Data／Ingest／Coordinating 描述節點 | 未涵蓋 Data Tiers 角色 | `data_hot`／`data_warm` 等 `node.roles` | [2.3.2](#232-節點角色說明) |
| 4 | 2.5 | Grafana `alerting.notification_channels` | Legacy Alerting，Grafana 11 已移除 | Panel Data Links | [2.8.2](#282-grafana-連結-kibana-範例) |
| 5 | 3.1 | 支援 RHEL／CentOS 7、Ubuntu 18.04、Debian 10 | 已結束原廠支援 | RHEL 8／9 系列、Ubuntu 22.04／24.04 等 | [3.1.1](#311-作業系統支援) |
| 6 | 3.1 | 建議版本 8.12.x | 已結束支援 | 9.5.4；8.x 先到 8.19 | [3.1.2](#312-版本選擇原則) |
| 7 | 3.2–3.4 | `packages/8.x` 套件庫、未鎖定版本 | 版本落後、可能意外升級 | `packages/9.x`、指定版本並鎖定 | [3.3.1](#331-rpm-安裝rhel-系列) |
| 8 | 3.2 | Docker `xpack.security.enabled=false`、對外開放 9200 | 不安全 | 保留安全性、只綁 127.0.0.1 | [3.3.5](#335-docker-快速安裝單節點啟用安全性) |
| 9 | 3.2、3.5、7.x | `curl localhost:9200` 無 TLS 與認證 | 9.x 預設 HTTPS + 認證 | `https://` + `--cacert` + 帳密／API Key | [3.3.6](#336-安裝後驗證) |
| 10 | 3.5 | 以 `/etc/security/limits.conf` 調整 nofile | systemd 服務不讀取該檔 | `systemctl edit` override；套件預設已足夠 | [3.2](#32-系統前置調校) |
| 11 | 3.5、4.1 | 直接修改 `jvm.options` | 官方不建議 | `jvm.options.d/*.options` | [3.8.1](#381-問題一elasticsearch-無法啟動) |
| 12 | 3.3、3.5、8.2 | `sudo .../logstash --config.test_and_exit` | 9.0 起禁止以 root 執行 | `sudo -u logstash ... --path.settings` | [3.5.3](#353-建立基本-pipeline-並測試) |
| 13 | 3.3、4.2、5.2 | `index => "logs-%{+YYYY.MM.dd}"` 每日索引 | 未使用 Data Stream | `data_stream => "true"` | [4.2.6](#426-output-設定範例) |
| 14 | 3.4、4.3 | `kibana.yml` 寫入 `kibana_system` 明文密碼、`http://` 連線 | 不安全 | Enrollment + Service Account Token + CA | [3.4.2](#342-以-enrollment-token-連線-elasticsearch) |
| 15 | 4.1、7.2 | `elasticsearch.yml` 設定 `index.refresh_interval` | 索引設定不可放 yml，節點無法啟動 | 放在 `logs@custom` | [4.1.1](#411-設定檔位置與設定層級) |
| 16 | 4.1 | `xpack.security.http.ssl.enabled: false`（內網可關閉） | 不安全 | 一律開啟 | [4.1.2](#412-elasticsearchyml-範例多節點) |
| 17 | 3.5、4.1 | Heap 一律手動 50%、≤ 31 GB | 未反映自動 Heap；31 GB 不保證 Compressed OOPs | 優先自動 Heap；手動時以 Log 確認 | [4.1.3](#413-jvm-heap-設定) |
| 18 | 4.1 | 範本 pattern `logs-*`、priority 0、`rollover_alias` | 與內建 `logs` 範本重疊且被覆蓋；舊式 rollover | `logs@custom` 或 priority > 100 的專屬範本 | [4.1.4](#414-index-template-與-component-template) |
| 19 | 4.2 | beats input `ssl => false` | 9.0 已移除 | `ssl_enabled`、`ssl_client_authentication` 等 | [4.2.4](#424-input-設定範例) |
| 20 | 4.2 | `if [type] == "java-app"` | `type` 欄位不再自動產生 | `fields.*`、`data_stream.dataset` | [4.2.5](#425-filter-設定範例) |
| 21 | 4.2 | Output `document_type => "_doc"`、HTTP 位址 | 棄用且無作用；不安全 | Data Stream + `ssl_certificate_authorities` | [4.2.6](#426-output-設定範例) |
| 22 | 4.3 | `i18n.locale: "zh-TW"` | 無此語系 | `en`／`zh-CN` 等支援值 | [4.3.1](#431-主設定檔) |
| 23 | 4.3 | `server.defaultRoute` | 8.0 起移出 `kibana.yml` | Advanced Settings `defaultRoute` | [4.3.4](#434-advanced-settings) |
| 24 | 4.3 | 標題「Index Pattern」 | 8.0 起更名 | Data View | [4.3.2](#432-data-view-設定) |
| 25 | 5.2 | `TimeBasedRollingPolicy` + `LogstashEncoder` | 無大小上限；非 ECS | Spring Boot ECS Structured Logging／ECS Encoder + 大小上限 | [5.3.1](#531-步驟-1應用程式-log-設定) |
| 26 | 5.2 | Filebeat `type: log` + `json.keys_under_root` | 9.x 拒絕啟動 | `filestream` + 唯一 `id` + `ndjson` parser | [5.3.2](#532-步驟-2filebeat-filestream-設定) |
| 27 | 5.2 | Filebeat `monitoring.elasticsearch` | Legacy internal collection | `http` endpoint + Metricbeat／Agent | [7.4.3](#743-stack-monitoring) |
| 28 | 6.2 | KQL `>=` 與 Lucene `[500 TO 599]` 混用 | 無法執行 | 依語言分開並新增 ES\|QL | [6.2.4](#624-實用查詢範例) |
| 29 | 6.3 | Share → CSV Reports | 介面已調整 | Share → Export → CSV | [6.1.3](#613-分享與匯出) |
| 30 | 7.1 | ILM `freeze`、`shrink`、`max_size` | freeze 已移除（no-op）；shrink 效益有限 | 移除；改用 `max_primary_shard_size` | [7.1.2](#712-index-lifecycle-managementilm) |
| 31 | 7.1 | Curator／腳本依名稱日期刪除 | Curator 停止維護；易誤刪 | ILM／DSL 管理保存期限 | [7.1.5](#715-手動清理) |
| 32 | 7.2 | `thread_pool.write.queue_size: 1000` | 掩蓋背壓 | 找出瓶頸並擴充 | [7.3.1](#731-寫入效能調校) |
| 33 | 7.2 | `logstash.yml` 設定 `output.elasticsearch.bulk_max_size` | Filebeat 的設定，Logstash 無此選項 | `pipeline.batch.size` | [4.2.2](#422-logstashyml-重要設定) |
| 34 | 7.3 | exporter `latest`、無認證、Compose `version` | 不穩定、不安全 | 固定 v1.11.0、唯讀帳號、CA | [7.4.4](#744-整合-prometheus-監控) |
| 35 | 8.1 | 建立 `fs` repository | 漏掉 `path.repo` | 所有節點設定 `path.repo`；建議 S3 | [7.2.1](#721-建立-snapshot-repository) |
| 36 | 8.2 | `POST _flush/synced` | 8.0 已移除 | `POST _flush` | [8.3.2](#832-elasticsearch-rolling-upgrade) |
| 37 | 8.2 | 未說明節點升級順序 | 易造成問題 | Data（冷→熱）→ 其他 → Master 最後 | [8.3.1](#831-升級順序) |
| 38 | 8.3 | `yum downgrade elasticsearch` | Elasticsearch 不支援降版 | 舊版新叢集 + 升級前快照還原 | [8.5](#85-回復策略) |
| 39 | 9.1 | `verification_mode: certificate` | 不驗證主機名稱 | `full` | [9.1.3](#913-tls-憑證規劃) |
| 40 | 9.2 | `logstash_system`、`beats_system` 列為 Logstash／Filebeat 角色 | 只用於上報監控 | 寫入用自訂角色／API Key | [9.3.1](#931-內建角色) |
| 41 | 9.2 | 自訂角色使用 DLS `query` | 付費功能，Basic 無效 | namespace 隔離；DLS 標示付費 | [9.3.2](#932-建立自訂角色) |

### D.3 v2.0 新增章節

| 章節 | 內容 |
| --- | --- |
| 1.3.2、1.5、1.6 | Elastic Stack 演進、授權模式與功能層級、版本發佈節奏 |
| 2.2.4、2.4、2.5、2.7 | Filebeat 與 Elastic Agent、Data Tiers、容量規劃、高可用與災難備援 |
| 3.2、3.3.3–3.3.5、3.4.2–3.4.3、3.6、3.7 | 系統前置調校、自動安全設定、Enrollment、加密金鑰、Filebeat 安裝、Docker Compose 開發環境 |
| 4.1.6、4.2.3、4.2.7、4.2.8、4.3.3、4.3.4 | Ingest Pipeline、多 Pipeline、PQ／DLQ、Keystore、Spaces、Advanced Settings |
| 5.2、5.4.4、5.4.5、5.5、5.6 | 收集端選型、log→filestream 遷移、直送 Elasticsearch、ECS 規範、Elastic Agent 與 Fleet |
| 6.2.3、6.3、6.4 | ES\|QL、告警、Streams |
| 7.1.3、7.1.4、7.2、7.5 | DSL、LogsDB、Snapshot 與 SLM、日常維運作業 |
| 8.1、8.2.2、8.2.3、8.4 | 升級路徑、Upgrade Assistant、7.x 索引處理、8.19→9.x 重大變更 |
| 9.1.4、9.2、9.3.4、9.4.4 | 憑證輪替、身分驗證、收集端最小權限、法規對照 |
| 10.3.3、10.5 | Elastic 內建 AI 與治理、導入路線圖 |
| 第十一章 | OpenTelemetry 與 EDOT 整合 |
| 第十二章 | Kubernetes 部署（ECK） |
| 第十三章 | 故障排除與營運手冊 |
| 第十四章 | 版本演進與新功能（9.0→9.5） |
| 附錄 A.6、B、C、E | 安全檢查清單、Q&A、指令速查、查證紀錄 |

---

## 附錄 E：查證紀錄

本版內容於 **2026-10-01** 依下列來源查證。

| # | 查證項目 | 結論 | 來源 |
| --- | --- | --- | --- |
| 1 | 最新版本與支援期限 | 9.5.4、9.4.7（2026-09-15）；8.19.22，8.19 支援至 2027-07-15；9.3 於 2026-08-04 EOS | [endoflife.date](https://endoflife.date/elasticsearch)、[GitHub Releases](https://github.com/elastic/elasticsearch/releases) |
| 2 | 9.5／9.4 新功能 | PromQL GA、Dashboards API GA、Columnar Mode TP（9.5）；Workflows GA、PromQL TP（9.4） | [Elastic 9.5](https://www.elastic.co/blog/whats-new-elastic-9-5-0)、[Elastic 9.4](https://www.elastic.co/blog/whats-new-elastic-9-4-0) |
| 3 | 9.1–9.3 新功能 | LOOKUP JOIN GA（9.1）；Streams GA（9.2）；Agent Builder GA（9.3） | [Elastic 9.1](https://www.elastic.co/blog/whats-new-elastic-9-1-0)、[Streams](https://www.elastic.co/docs/solutions/observability/streams/streams) |
| 4 | ES 9.5.4 內建元件 | Lucene 10.5.1、OpenJDK 26.0.2 | `elastic/elasticsearch` v9.5.4 `build-tools-internal/version.properties` |
| 5 | Logstash 9.5.4 內建元件 | Adoptium JDK 21.0.12、JRuby 10.0.6.0 | `elastic/logstash` v9.5.4 `versions.yml` |
| 6 | Logstash 設定預設值 | `allow_superuser` false、`pipeline.batch.size` 125、`queue.type` memory、`api.http.host` 127.0.0.1、`pipeline.buffer.type` heap、`pipeline.ecs_compatibility` v8 | `elastic/logstash` v9.5.4 `logstash-core/lib/logstash/environment.rb` |
| 7 | Logstash 以 root 執行 | 錯誤訊息 `Logstash cannot be run as superuser.` | `elastic/logstash` v9.5.4 `runner.rb` |
| 8 | Logstash 9.0–9.5 Breaking Changes | SSL 選項、UBI9、Modules 移除、JDK 21（9.4）、Kafka 預設值（9.5） | [Logstash breaking changes](https://www.elastic.co/docs/release-notes/logstash/breaking-changes) |
| 9 | Logstash ES output | `document_type` 對 8.x 無作用；12.0 起舊 SSL 選項使 Plugin 無法啟動；`data_stream` 預設 `auto` | `logstash-plugins/logstash-output-elasticsearch` `docs/index.asciidoc` |
| 10 | Filebeat 9.x 行為 | `log`／`container` input 拒絕啟動；fingerprint 預設；9.5 growing fingerprint；`filestream` 需唯一 `id`；`take_over` | [Filebeat filestream](https://www.elastic.co/docs/reference/beats/filebeat/filebeat-input-filestream)、[File identity](https://www.elastic.co/docs/reference/beats/filebeat/file-identity) |
| 11 | 內建 logs 範本 | priority 100、`logs-*-*`、組成順序 `logs@mappings`→`logs@settings`→`logs@custom`→`ecs@mappings`；failure store 啟用 | `elastic/elasticsearch` v9.5.4 `logs@template.json`、`logs@settings.json` |
| 12 | 內建 logs ILM 政策 | 只有 hot rollover（50 GB／30 天），無 delete | `elastic/elasticsearch` v9.5.4 `logs@lifecycle.json` |
| 13 | `logs@custom` ingest pipeline | `logs@default-pipeline` 補 `@timestamp` 後呼叫 `logs@custom` | `elastic/elasticsearch` v9.5.4 `logs@default-pipeline.json` |
| 14 | LogsDB 預設 | 9.0 起新 `logs-*-*` 預設啟用；升級叢集條件；最多省約 60% | [Logs data stream](https://www.elastic.co/docs/manage-data/data-store/data-streams/logs-data-stream) |
| 15 | ILM freeze | `FreezeAction` 為取代已移除功能的 no-op | `elastic/elasticsearch` v9.5.4 `FreezeAction.java` |
| 16 | JVM Heap | 預設依角色與記憶體自動設定，官方建議採用預設 | [Important settings](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/important-settings-configuration) |
| 17 | 升級路徑 | 9.1+ 需從 8.19 出發；8.18 只能到 9.0；7.x 索引處理三方式 | [Prepare to upgrade](https://www.elastic.co/docs/deploy-manage/upgrade/prepare-to-upgrade) |
| 18 | Rolling Upgrade 與降版 | 節點順序 frozen→cold→warm→hot→其他→master；不支援降版 | [Upgrade Elasticsearch](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/elasticsearch) |
| 19 | Kibana 語系 | 內建翻譯：zh-CN、ja-JP、fr-FR、de-DE | `elastic/kibana` v9.5.4 `x-pack/.i18nrc.json` |
| 20 | Kibana 設定 | `server.publicBaseUrl`、`elasticsearch.serviceAccountToken`、`elasticsearch.ssl.certificateAuthorities` | [Kibana settings](https://www.elastic.co/docs/reference/kibana/configuration-reference/general-settings) |
| 21 | Streams | 9.1 Preview、9.2 GA；wired 端點 9.4+ `logs.otel`／`logs.ecs` | [Streams](https://www.elastic.co/docs/solutions/observability/streams/streams)、[Logs index template](https://www.elastic.co/docs/solutions/observability/logs/logs-index-template-defaults) |
| 22 | EDOT Collector | 9.5 起內建於 Elastic Agent；`otel` mapping 為預設；`filelog` 範例設定 | [EDOT Collector](https://www.elastic.co/docs/reference/edot-collector)、[Stream log files with EDOT](https://www.elastic.co/docs/solutions/observability/logs/stream-any-log-file-using-edot-collector) |
| 23 | ECK | 3.5.0（2026-08-04）；K8s 1.31–1.36；安裝 URL | [ECK](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s)、[ECK quickstart](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s/install-using-yaml-manifest-quickstart) |
| 24 | redact processor | 商業授權功能 | [Redact processor](https://www.elastic.co/docs/reference/enrich-processor/redact-processor) |
| 25 | 訂閱層級 | Platinum 不再提供新客戶；DLS／FLS、稽核、SSO、Watcher 等屬付費 | [Subscriptions](https://www.elastic.co/subscriptions) |
| 26 | Prometheus exporter | prometheus-community/elasticsearch_exporter v1.11.0（2026-07-13） | [GitHub Releases](https://github.com/prometheus-community/elasticsearch_exporter/releases) |

### E.1 待確認事項

| # | 項目 | 說明 | 建議確認方式 |
| --- | --- | --- | --- |
| 1 | 9.x 作業系統支援清單 | Support Matrix 為動態頁面，本次未能取得 9.x 完整 OS 清單 | 直接開啟 Support Matrix 或洽 Elastic 支援 |
| 2 | 各功能所屬訂閱層級 | 1.5.2 表格依訂閱頁面整理，個別功能（如外部 Connector、Log 分析功能）可能隨版本調整 | 以合約與最新 Subscriptions 頁面為準 |
| 3 | LogsDB／synthetic source 與授權 | 未取得 Basic 授權下 synthetic source 行為的明確說明 | 查 9.5 的 synthetic `_source` 文件並實測 |
| 4 | Filebeat 自訂 `index` 的 setup 設定 | 9.x 中 `setup.template.*`／`setup.ilm.*` 與自訂 Data Stream 名稱的搭配 | 依 9.5 Filebeat 文件於測試環境驗證 |
| 5 | Filebeat Modules 在 9.x 的 input 型態 | 各 Module 是否皆已改用 `filestream` | 逐一檢查 `modules.d` 與 Release Notes |
| 6 | Streams 自建環境啟用與 AI 授權 | 文件未明列自建環境啟用步驟與 AI 建議功能的授權 | 測試環境實測、查 Kibana 9.5 文件 |
| 7 | Logstash `otlp` input | 是否已內建、成熟度 | 查 Logstash 9.5 Plugin 清單 |
| 8 | Hints autodiscover 註解鍵名 | `filestream` 情境下 parser／multiline 相關鍵名 | 查 9.5 Hints based autodiscover 文件 |
| 9 | Columnar Mode 各變體成熟度 | 官方摘要對 Logs 變體為 GA 或 Technical Preview 描述不一致 | 查 9.5 Release Notes |
| 10 | OTel 原生 Data Stream 命名與 Kibana 欄位別名 | `logs-*.otel-*` 命名與常用欄位別名範圍 | 實際寫入後以 `GET _data_stream` 確認 |
| 11 | ECK zone awareness 設定方式 | 3.5 的建議設定（downward node labels 等） | 查 ECK 3.5 文件 |
| 12 | Kibana 9.x 功能權限 ID | 細緻的 feature privilege 名稱（是否有版本化 ID） | 以 `GET /api/security/privileges` 查詢 |

---

## 附錄 F：參考資料

### F.1 Elastic 官方文件（9.x）

> ⚠️ **v2.0 更正**：自 9.0 起 Elastic 官方文件改版至 `www.elastic.co/docs/`；v1.0 使用的 `www.elastic.co/guide/...` 為 8.x 以前的舊版文件（下列 F.3 保留供 8.19 環境參考）。

- [Elastic Docs（首頁）](https://www.elastic.co/docs)
- [Elasticsearch Reference](https://www.elastic.co/docs/reference/elasticsearch)
- [部署與管理（Deploy and manage）](https://www.elastic.co/docs/deploy-manage)
- [升級（Upgrade）](https://www.elastic.co/docs/deploy-manage/upgrade)
- [Logstash Reference](https://www.elastic.co/docs/reference/logstash)
- [Kibana：Explore and analyze](https://www.elastic.co/docs/explore-analyze)
- [Filebeat Reference](https://www.elastic.co/docs/reference/beats/filebeat)
- [ES|QL Reference](https://www.elastic.co/docs/reference/query-languages/esql)
- [Elastic Common Schema（ECS）](https://www.elastic.co/docs/reference/ecs)
- [Data streams](https://www.elastic.co/docs/manage-data/data-store/data-streams)
- [Streams](https://www.elastic.co/docs/solutions/observability/streams/streams)
- [EDOT Collector](https://www.elastic.co/docs/reference/edot-collector)
- [Elastic Cloud on Kubernetes（ECK）](https://www.elastic.co/docs/deploy-manage/deploy/cloud-on-k8s)

### F.2 版本、支援與授權

- [Release Notes（全產品）](https://www.elastic.co/docs/release-notes)
- [Elasticsearch Breaking Changes](https://www.elastic.co/docs/release-notes/elasticsearch/breaking-changes)
- [Logstash Breaking Changes](https://www.elastic.co/docs/release-notes/logstash/breaking-changes)
- [Elastic Support Matrix](https://www.elastic.co/support/matrix)
- [Elastic Subscriptions](https://www.elastic.co/subscriptions)
- [Elastic Product End of Life Dates](https://www.elastic.co/support/eol)
- [endoflife.date：Elasticsearch](https://endoflife.date/elasticsearch)

### F.3 舊版文件（8.x，供 8.19 環境參考）

- [Elastic 官方文件（舊版入口）](https://www.elastic.co/guide/index.html)
- [Elasticsearch Reference 8.19](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index.html)
- [Logstash Reference 8.19](https://www.elastic.co/guide/en/logstash/8.19/index.html)
- [Kibana Guide 8.19](https://www.elastic.co/guide/en/kibana/8.19/index.html)
- [Filebeat Reference 8.19](https://www.elastic.co/guide/en/beats/filebeat/8.19/index.html)

### F.4 原始碼與社群資源

- [elastic/elasticsearch](https://github.com/elastic/elasticsearch)
- [elastic/logstash](https://github.com/elastic/logstash)
- [elastic/kibana](https://github.com/elastic/kibana)
- [elastic/beats](https://github.com/elastic/beats)
- [elastic/cloud-on-k8s](https://github.com/elastic/cloud-on-k8s)
- [prometheus-community/elasticsearch_exporter](https://github.com/prometheus-community/elasticsearch_exporter)
- [Spring Boot：Structured Logging](https://docs.spring.io/spring-boot/reference/features/logging.html#features.logging.structured)
- [Elastic Discuss 論壇](https://discuss.elastic.co/)
