+++
date = '2025-10-31T00:00:00+08:00'
draft = false
title = 'Jenkins CI_CD 教學手冊'
tags = ['教學', '工具']
categories = ['教學']
+++

# Jenkins CI/CD 教學手冊

## 文件資訊

| 項目 | 內容 |
| --- | --- |
| **文件版本** | 2.0 |
| **最後更新** | 2026-10-02 |
| **版本基準** | Jenkins LTS **2.580.1**（2026-09-30）、Java 21／25（controller 與所有 agent）、Helm chart `jenkins` 5.9.64、plugin 版本以 2026-10-02 的 update center 為準；完整矩陣見 [1.4 版本基準與相容性矩陣](#14-版本基準與相容性矩陣) |
| **文件定位** | 企業標準技術白皮書／內部標準教材：**Jenkins 的規劃、安裝、Pipeline 開發、分散式建置、部署、安全、組態即程式碼、監控、備份升級與供應鏈安全** |
| **適用對象** | 新進 Java 開發人員（第 1–13 章）、DevOps／平台工程師、系統管理員、架構師、資安與稽核人員 |
| **前置知識** | Java 與 Maven 基礎、Git、Linux 指令列、容器基本概念；第 14 章以後需要 Kubernetes 基本概念 |
| **姊妹文件** | 《git使用教學》、《Kubernetes教學手冊》、《Podman使用教學》、《Prometheus與Grafana教學手冊》、《OpenTelemetry教學手冊》、《GitLab使用教學》、《github使用教學》 |
| **前一版本** | 1.0（2024-03-10，以 Jenkins LTS 2.401.x、JDK 11／17 為基準） |
| **Created by** | Eric Cheng |

> 📌 **v2.0 改版重點**：章節重新編排為 24 章與 9 個附錄，全面對齊 Jenkins LTS 2.580.1。
>
> - **修正錯誤**：修正 v1.0 中已不適用或會造成故障的內容。例如 Java 需求（2.555.1 起只支援 Java 21／25，v1.0 寫 JDK 11）、Compose 把 `docker.sock` 掛進 controller、在 controller 上執行建置、11 個有語法錯誤、無法通過 Declarative 驗證的 Jenkinsfile（`when` 內直接寫布林運算式、`environment` 引用變數、雙引號字串跨行、非法跳脫字元）、已棄用的 Checkstyle／PMD／FindBugs／Extended Choice Parameter plugin、已停止服務的 Katacoda 與 A Cloud Guru 連結，以及在 PowerShell 區塊中使用 bash 續行符號等。
> - **新增內容**：版本與支援政策、容量規劃、Linux 套件庫新 GPG key、Helm 部署、Plugin 版本鎖定、GitHub App 驗證、Scripted Pipeline 與 CPS、Shared Library 與單元測試、Coverage／Warnings NG 品質門檻、Kubernetes agent、無 Docker daemon 的映像建置、GitOps、SSO（OIDC／SAML／LDAP）、Content Security Policy、JCasC 與 Job DSL、Prometheus／OpenTelemetry 監控、備份與升級、高可用與災難復原、SBOM／簽章與臺灣法規對應、企業導入路線、檢查清單與實作練習。
> - **追溯依據**：所有差異見 [F.2 v1.0 → v2.0 更正對照表](#f2-v10--v20-更正對照表)，查證依據見 [附錄 G：查證紀錄](#附錄-g查證紀錄)。

### 閱讀指引

| 讀者角色 | 建議閱讀章節 |
| --- | --- |
| 第一次接觸 Jenkins 的 Java 開發人員 | 第 1、2 章 → 3.2 → 第 4 章 → 第 10 章 → 第 13 章 |
| Pipeline 作者／技術主管 | 第 8–13 章 → 第 16 章 → 第 23 章 |
| 平台工程師／系統管理員 | 第 3、5 章 → 第 14、15 章 → 第 17–20 章 |
| Kubernetes 平台團隊 | 3.6 → 第 14、15 章 → 18.5 → 20.4 |
| 資安／稽核人員 | 第 7 章 → 第 17 章 → 第 21 章 → 24.3 |
| 架構師／決策者 | 第 1 章 → 第 2 章 → 3.1 → 第 20、22 章 |

### 本文慣例

| 標記 | 意義 |
| --- | --- |
| ✅／❌ | 建議做法／不建議做法 |
| ⚠️ | 容易出錯或有風險的地方 |
| 💡 | 實務技巧 |
| 📌 | 版本差異或改版說明 |
| 🔒 | 只在 CloudBees CI（商業版）提供的功能 |
| 🧪 | 實驗性功能，行為可能在後續版本變更 |
| `<尖括號>` | 需依環境替換的值 |
| `example.internal` | 範例內部網域，請替換為實際網域 |

> ⚠️ 本手冊的 Jenkinsfile 範例皆以本機啟動的 Jenkins 2.580.1 透過 `pipeline-model-converter/validate` 端點驗證，JCasC 範例以 `configuration-as-code/check` 端點驗證（見 [附錄 G：查證紀錄](#附錄-g查證紀錄)）。範例中的工具名稱統一為 `maven-3.9`、`jdk-21`，憑證 ID 與網域請依實際環境替換。

## 📑 目錄

<!-- TOC-AUTO-BEGIN -->

- [1. Jenkins 概觀與版本基準](#1-jenkins-概觀與版本基準)
  - [1.1 Jenkins 的定位與適用場景](#11-jenkins-的定位與適用場景)
  - [1.2 CI／CD 基本概念](#12-cicd-基本概念)
  - [1.3 發行週期：Weekly 與 LTS](#13-發行週期weekly-與-lts)
  - [1.4 版本基準與相容性矩陣](#14-版本基準與相容性矩陣)
  - [1.5 從 v1.0 基準到 2.580.1 的重大變化](#15-從-v10-基準到-25801-的重大變化)
  - [1.6 Jenkins 與 CloudBees CI](#16-jenkins-與-cloudbees-ci)
  - [1.7 本章重點](#17-本章重點)
- [2. 架構與核心概念](#2-架構與核心概念)
  - [2.1 Controller、Agent、Executor 與 Queue](#21-controlleragentexecutor-與-queue)
  - [2.2 Agent 類型與連線方式](#22-agent-類型與連線方式)
  - [2.3 Item 類型](#23-item-類型)
  - [2.4 Pipeline 執行模型](#24-pipeline-執行模型)
  - [2.5 JENKINS_HOME 目錄結構](#25-jenkins_home-目錄結構)
  - [2.6 Workspace、Artifact、Stash 與 Fingerprint](#26-workspaceartifactstash-與-fingerprint)
  - [2.7 參考架構](#27-參考架構)
  - [2.8 本章重點](#28-本章重點)
- [3. 安裝與初始設定](#3-安裝與初始設定)
  - [3.1 系統需求與容量規劃](#31-系統需求與容量規劃)
  - [3.2 快速體驗：WAR 檔](#32-快速體驗war-檔)
  - [3.3 Linux 套件安裝（systemd）](#33-linux-套件安裝systemd)
  - [3.4 Windows 安裝（MSI）](#34-windows-安裝msi)
  - [3.5 Docker／Podman 容器部署](#35-dockerpodman-容器部署)
  - [3.6 Kubernetes（Helm）部署](#36-kuberneteshelm部署)
  - [3.7 Setup Wizard 與初始安全設定](#37-setup-wizard-與初始安全設定)
  - [3.8 反向代理與 TLS](#38-反向代理與-tls)
  - [3.9 離線（封閉網路）安裝](#39-離線封閉網路安裝)
  - [3.10 本章重點](#310-本章重點)
- [4. 介面導覽與系統管理](#4-介面導覽與系統管理)
  - [4.1 介面配置（2.516.1 起的新版標頭）](#41-介面配置25161-起的新版標頭)
  - [4.2 Manage Jenkins 功能分區](#42-manage-jenkins-功能分區)
  - [4.3 Views 與 Dashboard](#43-views-與-dashboard)
  - [4.4 系統設定要點](#44-系統設定要點)
  - [4.5 Script Console 與管理介面的風險](#45-script-console-與管理介面的風險)
  - [4.6 本章重點](#46-本章重點)
- [5. Plugin 管理](#5-plugin-管理)
  - [5.1 Plugin 架構與相依關係](#51-plugin-架構與相依關係)
  - [5.2 選擇 Plugin 的評估準則](#52-選擇-plugin-的評估準則)
  - [5.3 以 plugins.txt 與 Plugin Installation Manager Tool 管理](#53-以-pluginstxt-與-plugin-installation-manager-tool-管理)
  - [5.4 已棄用 Plugin 與替代方案](#54-已棄用-plugin-與替代方案)
  - [5.5 更新策略與離線 update center](#55-更新策略與離線-update-center)
  - [5.6 本章重點](#56-本章重點)
- [6. Job 類型與 Freestyle](#6-job-類型與-freestyle)
  - [6.1 何時仍使用 Freestyle](#61-何時仍使用-freestyle)
  - [6.2 Freestyle 設定區塊](#62-freestyle-設定區塊)
  - [6.3 建置觸發與 Cron 語法](#63-建置觸發與-cron-語法)
  - [6.4 參數化建置](#64-參數化建置)
  - [6.5 Freestyle 遷移至 Pipeline](#65-freestyle-遷移至-pipeline)
  - [6.6 本章重點](#66-本章重點)
- [7. 憑證與機密管理](#7-憑證與機密管理)
  - [7.1 Credentials 架構與類型](#71-credentials-架構與類型)
  - [7.2 憑證作用域](#72-憑證作用域)
  - [7.3 在 Pipeline 使用憑證](#73-在-pipeline-使用憑證)
  - [7.4 遮罩的限制與常見外洩途徑](#74-遮罩的限制與常見外洩途徑)
  - [7.5 外部機密管理](#75-外部機密管理)
  - [7.6 以 JCasC 管理憑證](#76-以-jcasc-管理憑證)
  - [7.7 本章重點](#77-本章重點)
- [8. SCM 整合](#8-scm-整合)
  - [8.1 Git plugin 與 checkout](#81-git-plugin-與-checkout)
  - [8.2 GitHub 整合（GitHub App 驗證）](#82-github-整合github-app-驗證)
  - [8.3 GitLab 整合](#83-gitlab-整合)
  - [8.4 Bitbucket 與其他 SCM](#84-bitbucket-與其他-scm)
  - [8.5 Webhook 觸發與輪詢](#85-webhook-觸發與輪詢)
  - [8.6 Multibranch Pipeline 與 Organization Folder](#86-multibranch-pipeline-與-organization-folder)
  - [8.7 分支策略與 Pipeline 對應](#87-分支策略與-pipeline-對應)
  - [8.8 本章重點](#88-本章重點)
- [9. 建置工具整合（Maven、Gradle 與多語言）](#9-建置工具整合mavengradle-與多語言)
  - [9.1 工具管理策略](#91-工具管理策略)
  - [9.2 Maven 最佳實務](#92-maven-最佳實務)
  - [9.3 Pipeline 中的 Maven 建置](#93-pipeline-中的-maven-建置)
  - [9.4 Gradle](#94-gradle)
  - [9.5 相依套件快取](#95-相依套件快取)
  - [9.6 版本號與發佈](#96-版本號與發佈)
  - [9.7 其他語言的建置範例](#97-其他語言的建置範例)
  - [9.8 本章重點](#98-本章重點)
- [10. Declarative Pipeline 完整語法](#10-declarative-pipeline-完整語法)
  - [10.1 結構總覽](#101-結構總覽)
  - [10.2 agent](#102-agent)
  - [10.3 environment 與字串內插](#103-environment-與字串內插)
  - [10.4 options](#104-options)
  - [10.5 parameters 與 triggers](#105-parameters-與-triggers)
  - [10.6 when 條件](#106-when-條件)
  - [10.7 parallel 與循序 stages](#107-parallel-與循序-stages)
  - [10.8 matrix](#108-matrix)
  - [10.9 input（人工核准）](#109-input人工核准)
  - [10.10 post 與建置結果](#1010-post-與建置結果)
  - [10.11 script 區塊與 Declarative 的限制](#1011-script-區塊與-declarative-的限制)
  - [10.12 完整範例：Spring Boot 服務 Pipeline](#1012-完整範例spring-boot-服務-pipeline)
  - [10.13 本章重點](#1013-本章重點)
- [11. Scripted Pipeline、CPS 與進階模式](#11-scripted-pipelinecps-與進階模式)
  - [11.1 Scripted Pipeline 語法](#111-scripted-pipeline-語法)
  - [11.2 CPS 限制與 @NonCPS](#112-cps-限制與-noncps)
  - [11.3 Script Security 沙箱與 Script Approval](#113-script-security-沙箱與-script-approval)
  - [11.4 Durability 與效能設定](#114-durability-與效能設定)
  - [11.5 資源鎖定與 milestone](#115-資源鎖定與-milestone)
  - [11.6 錯誤處理模式](#116-錯誤處理模式)
  - [11.7 Pipeline 開發工具](#117-pipeline-開發工具)
  - [11.8 本章重點](#118-本章重點)
- [12. Shared Libraries](#12-shared-libraries)
  - [12.1 用途與目錄結構](#121-用途與目錄結構)
  - [12.2 設定 Library：受信任與非受信任](#122-設定-library受信任與非受信任)
  - [12.3 vars：自訂全域 step](#123-vars自訂全域-step)
  - [12.4 src 類別與 resources](#124-src-類別與-resources)
  - [12.5 Pipeline 範本：封裝整條 Declarative Pipeline](#125-pipeline-範本封裝整條-declarative-pipeline)
  - [12.6 版本管理與發佈流程](#126-版本管理與發佈流程)
  - [12.7 單元測試：JenkinsPipelineUnit](#127-單元測試jenkinspipelineunit)
  - [12.8 本章重點](#128-本章重點)
- [13. 測試報告、覆蓋率與品質門檻](#13-測試報告覆蓋率與品質門檻)
  - [13.1 JUnit 測試報告](#131-junit-測試報告)
  - [13.2 程式碼覆蓋率：Coverage plugin](#132-程式碼覆蓋率coverage-plugin)
  - [13.3 靜態分析：Warnings Next Generation](#133-靜態分析warnings-next-generation)
  - [13.4 SonarQube 品質門檻](#134-sonarqube-品質門檻)
  - [13.5 品質門檻設計](#135-品質門檻設計)
  - [13.6 回報到 GitHub Checks 與 GitLab MR](#136-回報到-github-checks-與-gitlab-mr)
  - [13.7 HTML 報告與安全限制](#137-html-報告與安全限制)
  - [13.8 本章重點](#138-本章重點)
- [14. Agent 與雲端節點](#14-agent-與雲端節點)
  - [14.1 Agent 規劃與 Label 設計](#141-agent-規劃與-label-設計)
  - [14.2 固定 agent：SSH 與 Windows](#142-固定-agentssh-與-windows)
  - [14.3 Docker agent](#143-docker-agent)
  - [14.4 Kubernetes plugin](#144-kubernetes-plugin)
  - [14.5 其他雲端 agent](#145-其他雲端-agent)
  - [14.6 Agent 安全與隔離](#146-agent-安全與隔離)
  - [14.7 本章重點](#147-本章重點)
- [15. 容器映像建置與 Kubernetes 上的 Jenkins](#15-容器映像建置與-kubernetes-上的-jenkins)
  - [15.1 映像建置方式比較](#151-映像建置方式比較)
  - [15.2 BuildKit rootless（Kubernetes agent）](#152-buildkit-rootlesskubernetes-agent)
  - [15.3 Buildah 與 Jib](#153-buildah-與-jib)
  - [15.4 映像標籤、Digest 與推送](#154-映像標籤digest-與推送)
  - [15.5 在 Kubernetes 上執行 Jenkins controller（Helm 進階設定）](#155-在-kubernetes-上執行-jenkins-controllerhelm-進階設定)
  - [15.6 本章重點](#156-本章重點)
- [16. 部署策略與環境管理](#16-部署策略與環境管理)
  - [16.1 環境與晉升模型](#161-環境與晉升模型)
  - [16.2 人工核准與職責分離](#162-人工核准與職責分離)
  - [16.3 部署到 Kubernetes](#163-部署到-kubernetes)
  - [16.4 GitOps：Jenkins 負責 CI，Argo CD 負責 CD](#164-gitopsjenkins-負責-ciargo-cd-負責-cd)
  - [16.5 Blue-Green 部署](#165-blue-green-部署)
  - [16.6 Canary 部署](#166-canary-部署)
  - [16.7 回滾](#167-回滾)
  - [16.8 資料庫結構遷移](#168-資料庫結構遷移)
  - [16.9 部署到 VM 與傳統主機](#169-部署到-vm-與傳統主機)
  - [16.10 本章重點](#1610-本章重點)
- [17. 安全強化](#17-安全強化)
  - [17.1 威脅模型](#171-威脅模型)
  - [17.2 驗證（Security Realm）](#172-驗證security-realm)
  - [17.3 授權策略](#173-授權策略)
  - [17.4 建置的執行身分（Authorize Project）](#174-建置的執行身分authorize-project)
  - [17.5 Controller 與 Agent 隔離](#175-controller-與-agent-隔離)
  - [17.6 Web 安全：CSRF、CSP、Markup 與 Resource Root URL](#176-web-安全csrfcspmarkup-與-resource-root-url)
  - [17.7 Script Approval 與 Script Console 管控](#177-script-approval-與-script-console-管控)
  - [17.8 API Token、CLI 與服務帳號](#178-api-tokencli-與服務帳號)
  - [17.9 安全公告與漏洞處理流程](#179-安全公告與漏洞處理流程)
  - [17.10 稽核與集中記錄](#1710-稽核與集中記錄)
  - [17.11 本章重點](#1711-本章重點)
- [18. Configuration as Code（JCasC）與 Job DSL](#18-configuration-as-codejcasc與-job-dsl)
  - [18.1 為何要把 Jenkins 設定程式碼化](#181-為何要把-jenkins-設定程式碼化)
  - [18.2 JCasC 基礎](#182-jcasc-基礎)
  - [18.3 JCasC 實務](#183-jcasc-實務)
  - [18.4 Job DSL](#184-job-dsl)
  - [18.5 在 Kubernetes 上管理設定](#185-在-kubernetes-上管理設定)
  - [18.6 Jenkins 設定的 GitOps 流程](#186-jenkins-設定的-gitops-流程)
  - [18.7 本章重點](#187-本章重點)
- [19. 監控、日誌、效能與通知](#19-監控日誌效能與通知)
  - [19.1 監控什麼](#191-監控什麼)
  - [19.2 Prometheus metrics plugin](#192-prometheus-metrics-plugin)
  - [19.3 OpenTelemetry：Pipeline 追蹤](#193-opentelemetrypipeline-追蹤)
  - [19.4 日誌](#194-日誌)
  - [19.5 JVM 與效能調校](#195-jvm-與效能調校)
  - [19.6 建置保留與磁碟管理](#196-建置保留與磁碟管理)
  - [19.7 通知](#197-通知)
  - [19.8 本章重點](#198-本章重點)
- [20. 備份、升級與高可用](#20-備份升級與高可用)
  - [20.1 備份策略](#201-備份策略)
  - [20.2 還原與演練](#202-還原與演練)
  - [20.3 升級程序](#203-升級程序)
  - [20.4 高可用與災難復原](#204-高可用與災難復原)
  - [20.5 本章重點](#205-本章重點)
- [21. 軟體供應鏈安全與合規](#21-軟體供應鏈安全與合規)
  - [21.1 威脅與框架](#211-威脅與框架)
  - [21.2 SBOM（軟體物料清單）](#212-sbom軟體物料清單)
  - [21.3 弱點掃描](#213-弱點掃描)
  - [21.4 簽章與 Provenance](#214-簽章與-provenance)
  - [21.5 Pipeline 的供應鏈防護清單](#215-pipeline-的供應鏈防護清單)
  - [21.6 臺灣法規與稽核對應](#216-臺灣法規與稽核對應)
  - [21.7 本章重點](#217-本章重點)
- [22. 企業導入路線與參考架構](#22-企業導入路線與參考架構)
  - [22.1 導入路線圖](#221-導入路線圖)
  - [22.2 平台團隊與治理模型](#222-平台團隊與治理模型)
  - [22.3 以 DORA 指標衡量成效](#223-以-dora-指標衡量成效)
  - [22.4 DevOps 文化實務](#224-devops-文化實務)
  - [22.5 參考情境一：金融機構（示意）](#225-參考情境一金融機構示意)
  - [22.6 參考情境二：製造業多語言環境（示意）](#226-參考情境二製造業多語言環境示意)
  - [22.7 舊 Jenkins 整併與遷移](#227-舊-jenkins-整併與遷移)
  - [22.8 AI 輔助的 Pipeline 維運](#228-ai-輔助的-pipeline-維運)
  - [22.9 本章重點](#229-本章重點)
- [23. 故障排除](#23-故障排除)
  - [23.1 排除問題的方法](#231-排除問題的方法)
  - [23.2 Pipeline 常見錯誤](#232-pipeline-常見錯誤)
  - [23.3 Agent 連線問題](#233-agent-連線問題)
  - [23.4 效能問題](#234-效能問題)
  - [23.5 Controller 啟動問題](#235-controller-啟動問題)
  - [23.6 診斷用唯讀腳本](#236-診斷用唯讀腳本)
  - [23.7 收集支援資訊](#237-收集支援資訊)
  - [23.8 本章重點](#238-本章重點)
- [24. 檢查清單](#24-檢查清單)
  - [24.1 安裝與平台建置](#241-安裝與平台建置)
  - [24.2 Pipeline 品質](#242-pipeline-品質)
  - [24.3 安全基準](#243-安全基準)
  - [24.4 正式上線前](#244-正式上線前)
  - [24.5 LTS 升級](#245-lts-升級)
- [附錄 A：指令與 API 速查](#附錄-a指令與-api-速查)
  - [A.1 Jenkins CLI](#a1-jenkins-cli)
  - [A.2 REST API](#a2-rest-api)
  - [A.3 常用 Pipeline step 速查](#a3-常用-pipeline-step-速查)
  - [A.4 Git、容器與 Kubernetes 常用指令](#a4-git容器與-kubernetes-常用指令)
- [附錄 B：範本索引](#附錄-b範本索引)
- [附錄 C：Plugin 建議清單](#附錄-cplugin-建議清單)
  - [C.1 基準 plugin（2026-10-02）](#c1-基準-plugin2026-10-02)
  - [C.2 依情境選用](#c2-依情境選用)
  - [C.3 已棄用與不建議](#c3-已棄用與不建議)
- [附錄 D：學習資源](#附錄-d學習資源)
  - [D.1 官方文件](#d1-官方文件)
  - [D.2 線上課程](#d2-線上課程)
  - [D.3 社群](#d3-社群)
  - [D.4 實戰練習](#d4-實戰練習)
  - [D.5 書籍](#d5-書籍)
  - [D.6 v1.0 學習資源連結查證結果](#d6-v10-學習資源連結查證結果)
- [附錄 E：認證](#附錄-e認證)
  - [E.1 Jenkins 相關認證現況](#e1-jenkins-相關認證現況)
  - [E.2 相關技術認證與本手冊章節對應](#e2-相關技術認證與本手冊章節對應)
- [附錄 F：版本紀錄](#附錄-f版本紀錄)
  - [F.1 版本歷程與章節對照](#f1-版本歷程與章節對照)
  - [F.2 v1.0 → v2.0 更正對照表](#f2-v10--v20-更正對照表)
- [附錄 G：查證紀錄](#附錄-g查證紀錄)
  - [G.1 待確認事項](#g1-待確認事項)
- [附錄 H：術語表](#附錄-h術語表)
- [附錄 I：實作練習](#附錄-i實作練習)
  - [I.1 基礎（第 1–6 章）](#i1-基礎第-16-章)
  - [I.2 Pipeline 開發（第 7–13 章）](#i2-pipeline-開發第-713-章)
  - [I.3 平台與部署（第 14–16 章）](#i3-平台與部署第-1416-章)
  - [I.4 營運與治理（第 17–21 章）](#i4-營運與治理第-1721-章)
  - [I.5 綜合專題](#i5-綜合專題)

<!-- TOC-AUTO-END -->

---

## 1. Jenkins 概觀與版本基準

### 1.1 Jenkins 的定位與適用場景

Jenkins 是以 Java 開發的開源自動化伺服器，由 Continuous Delivery Foundation（CDF，隸屬 Linux Foundation）託管。Jenkins 本身只提供排程、執行與擴充框架，**建置、測試、部署、通知與整合等功能都透過 plugin 提供**（2026-10 的 update center 共列出 2,116 個 plugin）。這種架構讓 Jenkins 幾乎能整合任何工具，但也代表 plugin 的選擇與版本治理是導入成敗的關鍵（見 [5. Plugin 管理](#5-plugin-管理)）。

| 比較面向 | Jenkins（自建） | GitHub Actions／GitLab CI（平台內建） |
| --- | --- | --- |
| 部署型態 | 自行架設與維運 controller 與 agent | SaaS 或隨 Git 平台自建 |
| 擴充方式 | Plugin、Shared Library、任意腳本 | Marketplace actions／CI templates |
| Pipeline 定義 | `Jenkinsfile`（Groovy DSL） | YAML |
| 適合場景 | 多種 SCM 並存、封閉網路、需要高度客製化、既有大量 Jenkins 資產、需在特定硬體或內網環境執行 | 程式碼已集中於單一平台、團隊想減少維運負擔 |
| 主要成本 | 維運人力、plugin 治理、資安更新 | 執行時數或 runner 維運、平台綁定 |

✅ 適合導入或續用 Jenkins 的情境：

- 組織同時使用 GitLab、GitHub、Bitbucket 或其他 SCM，需要一致的 CI/CD 平台
- 建置環境位於封閉網路（金融、政府、製造業 OT 網段），需要完全自主掌控
- 已有大量 Jenkins Job 與 Shared Library，遷移成本高於持續改善
- 需要複雜的流程控制（人工核准、跨專案觸發、資源鎖定、矩陣建置）

⚠️ 需要審慎評估的情境：新團隊、程式碼全部在單一 Git 平台、沒有專職平台團隊。這時平台內建 CI 的總持有成本通常較低。

> 📌 **Jenkins X 不是 Jenkins**：Jenkins X 是另一個以 Tekton 為基礎、專為 Kubernetes 設計的 CDF 專案，與本手冊的 Jenkins 沒有程式碼或設定上的相容性。v1.0 把 Jenkins X 文件列為 Jenkins 官方文件，v2.0 已更正（見 [附錄 D：學習資源](#附錄-d學習資源)）。

### 1.2 CI／CD 基本概念

| 名詞 | 定義 | Jenkins 中的實作 |
| --- | --- | --- |
| 持續整合（CI） | 每次提交都自動建置與測試，讓整合問題儘早出現 | Multibranch Pipeline＋Webhook 觸發，執行編譯、單元測試、靜態分析 |
| 持續交付（Continuous Delivery） | 每次通過 CI 的版本都**可以**隨時部署，正式部署仍需人工決定 | Pipeline 產生可部署產物，`input` 步驟控制正式環境部署 |
| 持續部署（Continuous Deployment） | 通過所有自動化關卡後**自動**部署到正式環境 | 品質門檻全自動化，搭配 Canary／自動回滾（第 16 章） |

```mermaid
flowchart LR
    A[開發者提交程式碼] --> B[Webhook 觸發]
    B --> C[Checkout]
    C --> D[編譯與單元測試]
    D --> E[靜態分析與品質門檻]
    E --> F[打包與映像建置]
    F --> G[SBOM 與弱點掃描]
    G --> H[部署至測試環境]
    H --> I[整合與驗收測試]
    I --> J{核准}
    J -->|通過| K[部署至正式環境]
    J -->|退回| L[通知開發者]

    subgraph CI[持續整合]
        C
        D
        E
        F
        G
    end
    subgraph CD[持續交付／部署]
        H
        I
        J
        K
    end
```

一條成熟的 Pipeline 應具備以下特性：

1. **可重現**：相同的 commit 產生相同的產物（固定工具版本、鎖定相依套件、使用容器化 agent）
2. **快速回饋**：單元測試與靜態分析在 10 分鐘內完成；較慢的測試放在後段或平行執行
3. **一次建置、多處部署**：產物只建置一次，以同一個映像 digest 或 artifact 版本推進到各環境
4. **可追溯**：每個部署都能追溯到 commit、建置編號、測試報告、SBOM 與核准人
5. **以程式碼管理**：Pipeline（`Jenkinsfile`）、系統設定（JCasC）與 Job 定義（Job DSL）都放在版本控制中

### 1.3 發行週期：Weekly 與 LTS

Jenkins 有兩條發行線：

| 發行線 | 版本號範例 | 週期 | 適用 |
| --- | --- | --- | --- |
| **Weekly** | 2.584 | 每週發行，包含新功能與修正 | 測試環境、plugin 開發者、想搶先使用新功能的團隊 |
| **LTS（Long-Term Support）** | 2.580.1 | 每 12 週選定一個 weekly 作為基準，再於其上發行 `.1`、`.2`、`.3` 三個修補版，每 4 週一版；每版發行前 2 週會先有 RC | **正式環境的標準選擇** |

```mermaid
gantt
    title LTS 12 週發行節奏（示意）
    dateFormat YYYY-MM-DD
    axisFormat %m/%d
    section 2.568 線
    2.568.3        :milestone, 2026-09-02, 0d
    section 2.580 線
    2.580.1 RC     :milestone, 2026-09-16, 0d
    2.580.1        :milestone, 2026-09-30, 0d
    2.580.2（預估） :milestone, 2026-10-28, 0d
    2.580.3（預估） :milestone, 2026-11-25, 0d
```

✅ 正式環境的版本策略建議：

- 使用 LTS，並在每個 `.1` 發行後 2–4 週內完成評估與升級；安全公告修補版（任何一條線）應在公告後 7 天內處理
- 保留一套與正式環境相同 plugin 組合的**預備環境（staging controller）**，先在預備環境升級並執行冒煙測試（第 20 章）
- 訂閱 [Jenkins 安全公告](https://www.jenkins.io/security/advisories/)；2026 年 1–9 月已發布 9 次公告，其中 5 次影響 core

### 1.4 版本基準與相容性矩陣

以下為本手冊撰寫時（2026-10-02）的版本基準。plugin 版本只列代表性項目，完整建議清單見 [附錄 C：Plugin 建議清單](#附錄-cplugin-建議清單)。

| 元件 | 版本 | 說明 |
| --- | --- | --- |
| Jenkins LTS | **2.580.1**（2026-09-30） | 上一條 LTS 線為 2.568.3（2026-09-02） |
| Jenkins Weekly | 2.584（2026-09-28） | 僅供參考 |
| Java（執行 Jenkins） | **Java 21 或 Java 25** | 2.555.1 起不再支援 Java 17；controller、所有 agent、CLI client 都適用 |
| Java（執行建置） | 任意版本 | 建置用 JDK 與執行 agent 的 JDK 互相獨立，可用工具安裝或容器提供 Java 8／11／17 |
| 官方容器映像 | `jenkins/jenkins:2.580.1-lts-jdk21`、`-jdk25`、`-rhel-ubi9-jdk21`、`-windowsservercore-ltsc2022`／`ltsc2025` | Debian 基底映像自 2.528.1 起改為 Debian 13（Trixie）；Windows Server 2019 映像自 2.568.1 起停止提供 |
| Agent 映像 | `jenkins/inbound-agent:3391.va_37fa_a_305d6d-3-jdk21` | remoting 版本隨 core 更新 |
| Linux 套件 | `pkg.jenkins.io/debian-stable`、`pkg.jenkins.io/rpm-stable` | 2.541.1 起 RPM 統一為 `rpm-stable`，並更換 GPG key（`jenkins.io-2026.key`） |
| Helm chart | `jenkins/jenkins` 5.9.64（appVersion 2.568.3） | 以 `controller.image.tag` 指定 2.580.1 |
| Pipeline（aggregator） | `workflow-aggregator` 608.v67378e9d3db_1 | |
| Pipeline: Declarative | 2.2293.v6e7193cec599 | |
| Configuration as Code | 2131.vb_a_13ed96f755 | |
| Kubernetes plugin | 4557.ve746270f672f | |
| Git plugin | 5.10.1 | |
| Pipeline Graph View | 1041.v107d70db_b_1a_f | setup wizard 建議 plugin，取代 Stage View 的地位 |

> 💡 plugin 版本號採用「`<流水號>.v<git hash>`」格式（例如 `4557.ve746270f672f`），流水號越大越新。比較版本時不要只看小數點後的雜湊值。

### 1.5 從 v1.0 基準到 2.580.1 的重大變化

v1.0 以 LTS 2.401.x 為基準。以下整理此後各 LTS 線影響導入與升級的變化，詳細升級步驟見第 20 章。

| LTS 線 | 變化 | 對本手冊的影響 |
| --- | --- | --- |
| 2.426.1 | 支援 Java 21；最後一條支援 Java 11 的 LTS 線 | — |
| 2.479.1 | **必須使用 Java 17 以上**；升級為 Spring Security 6、Jakarta EE 9；LDAP 等 plugin 必須同步升級 | 3.1、20.3 |
| 2.492.1 | YUI 預設停用；agent protocol 清單不可再設定，JCasC 的 `agentProtocols` 區段會導致啟動中止 | 18.3 |
| 2.504.1 | YUI 完全移除；移除 jCIFS 與 j-Interop（不能再從 UI 安裝 Windows 服務或以 DCOM 啟動 Windows agent） | 3.4、14.2 |
| 2.516.1 | 標頭列重新設計（Manage Jenkins 移到右上角）；本機使用者密碼上限 72 bytes（bcrypt）；Cookie 預設 `SameSite=Lax` | 4.1、17.2 |
| 2.528.1 | 容器映像改用 Debian 13；Timestamper 必須先升級；JCasC `myViewsTabBar` 棄用 | 3.5、20.3 |
| 2.541.1 | Core 內建 Content Security Policy（預設不強制）；RPM 套件庫統一；Linux 套件更換 GPG key | 3.3、17.6 |
| 2.555.1 | **必須使用 Java 21 或 25**；Java 17 映像停止提供；`DefaultCrumbIssuer` 不再納入 IP，JCasC 必須移除 `crumbIssuer` 區段 | 3.1、18.3、20.3 |
| 2.568.1 | 停止提供 Windows Server 2019 controller 映像 | 3.4 |
| 2.580.1 | 9 個 detached plugin 不再打包在 `jenkins.war`（離線環境需預先放入 plugin） | 5.5、20.3 |

### 1.6 Jenkins 與 CloudBees CI

CloudBees CI 是以 Jenkins LTS 為基礎的商業發行版，主要差異如下。本手冊以開源 Jenkins 為主，只在必要時以 🔒 標示商業版功能。

| 能力 | 開源 Jenkins | 🔒 CloudBees CI |
| --- | --- | --- |
| Controller 數量 | 各自獨立，需自行建立治理方式（JCasC＋Git） | Operations Center 集中管理多個 controller |
| 高可用 | 單一 controller（active／passive 需自行設計，見 20.4） | 提供 HA（active／active）模式 |
| Plugin 治理 | 自行以 `plugins.txt` 鎖定版本並測試相容性 | CloudBees Assurance Program 提供經驗證的 plugin 組合 |
| RBAC | Matrix 或 Role-based Strategy plugin | 內建 RBAC 與群組委派 |
| 支援 | 社群 | 商業支援與 SLA |

### 1.7 本章重點

- 正式環境使用 LTS，並把安全公告當作最高優先的變更
- 2.555.1 之後 controller **與所有 agent** 都必須執行 Java 21 或 25；建置用的 JDK 版本則不受限制
- Jenkins 的能力來自 plugin，plugin 治理與版本鎖定是導入的第一項工程（第 5 章）
- 以 Pipeline、JCasC、Job DSL 把 Jenkins 本身也納入版本控制，是本手冊所有企業實務的基礎

## 2. 架構與核心概念

### 2.1 Controller、Agent、Executor 與 Queue

```mermaid
flowchart TB
    subgraph Controller[Jenkins Controller]
        UI[Web UI／REST API／CLI]
        Q[Build Queue]
        S[Scheduler 與 Load Balancer]
        P[Plugin 與設定<br/>JENKINS_HOME]
        CPS[Pipeline 引擎<br/>CPS 解譯 Groovy]
    end
    subgraph A1[Agent：linux-agent-01]
        E1[Executor 1]
        E2[Executor 2]
        W1[Workspace]
    end
    subgraph A2[Cloud Agent：Kubernetes Pod]
        E3[Executor]
        W2[Workspace]
    end
    UI --> Q --> S
    S -->|分派| E1
    S -->|分派| E3
    CPS -.->|遠端執行 sh／bat 等 step| A1
    CPS -.->|遠端執行 step| A2
```

| 元件 | 職責 | 設計重點 |
| --- | --- | --- |
| **Controller**（舊稱 master） | 提供 UI／API、保存設定與建置紀錄、排程、執行 Pipeline 的 Groovy 邏輯（CPS） | 只負責協調，**不執行建置**；`JENKINS_HOME` 需要可靠的儲存與備份 |
| **Agent**（舊稱 slave／node） | 透過 remoting 與 controller 連線，在自己的 workspace 執行建置步驟 | 依工具鏈、作業系統或安全等級區分 label；建議容器化或可拋棄式 |
| **Executor** | Agent 上的執行槽，一個 executor 同時執行一個建置（或一個 `node {}` 區塊） | 數量通常等於 CPU 核心數或更少；容器化 agent 通常設為 1 |
| **Build Queue** | 等待可用 executor 的工作佇列 | 佇列持續累積代表 agent 容量不足或 label 設定錯誤 |
| **Label** | 標記 agent 能力（如 `linux && docker`），Pipeline 以 label 表達式選擇 agent | 以「能力」命名而非主機名稱，方便擴充與替換 |

> ⚠️ **Built-in node（內建節點）不應執行建置**：在 controller 上執行建置會讓建置程式碼直接存取 `JENKINS_HOME`（含所有憑證的加密金鑰），也會與 controller 搶奪 CPU 與記憶體。官方硬體建議明確指出「在 controller 配置 executor 通常是不良做法」。請把 built-in node 的 executor 數設為 `0`（JCasC：`jenkins.numExecutors: 0`）。v1.0 的多個範例使用 `agent any` 且未設定此值，等同允許在 controller 上執行建置。

### 2.2 Agent 類型與連線方式

| 類型 | 生命週期 | 典型實作 | 適用 |
| --- | --- | --- | --- |
| **Permanent agent**（固定節點） | 長期存在，由管理者建立 | VM、實體機、Windows／macOS 建置機 | 需要特殊硬體、授權軟體、macOS／iOS 簽章 |
| **Cloud agent**（動態節點） | 依需求建立、建置後銷毀 | Kubernetes plugin、Amazon EC2、Azure VM Agents、Docker plugin | 一般 Linux 建置；彈性擴充、環境一致 |

| 連線方式 | 方向 | 連接埠 | 說明 |
| --- | --- | --- | --- |
| **SSH**（SSH Build Agents plugin） | Controller → Agent | Agent 的 22 | Controller 以 SSH 登入並啟動 `agent.jar`；適合 Linux 固定節點 |
| **Inbound（TCP）** | Agent → Controller | Controller 的 TCP agent port（容器映像慣例 50000） | Agent 主動連線；需開放額外連接埠 |
| **Inbound（WebSocket）** | Agent → Controller | 與 Web UI 相同的 HTTP(S) 埠 | ✅ 不需額外連接埠，能穿過反向代理與負載平衡器；新部署建議使用 |

Inbound agent 的啟動指令格式如下（取自 2.580.1 的 agent 頁面）：

```bash
java -jar agent.jar \
  -url https://jenkins.example.internal/ \
  -secret @/home/jenkins/agent-secret \
  -name "linux-agent-01" \
  -webSocket \
  -workDir "/home/jenkins/agent"
```

> 💡 `-secret @<檔案>` 從檔案讀取密鑰，避免密鑰出現在行程清單與 shell 歷史。Agent 的 Java 版本也必須是 21 或 25。

### 2.3 Item 類型

| 類型 | 定義方式 | 使用建議 |
| --- | --- | --- |
| **Pipeline** | `Jenkinsfile`（Declarative 或 Scripted） | 單一分支或特定用途的流程（例如排程維運工作） |
| **Multibranch Pipeline** | 掃描 repository 的分支、PR、tag，各自依 `Jenkinsfile` 建立子 Job | ✅ 應用程式 CI/CD 的**預設選擇** |
| **Organization Folder** | 掃描整個 GitHub organization／GitLab group／Bitbucket project，自動建立 Multibranch | 大型組織統一治理 |
| **Folder** | 分組容器，可設定 folder 層級的憑證、Shared Library 與權限 | 依團隊或產品線分隔 |
| **Freestyle project** | UI 表單設定 | 只用於簡單維運工作；新專案不建議（第 6 章） |
| **Multi-configuration（Matrix）project** | UI 表單設定的矩陣建置 | 以 Declarative `matrix` 取代（10.8） |

每次執行 Job 產生一個 **Run**（UI 上稱為 Build），保存在 `jobs/<name>/builds/<編號>/`，內容包括主控台記錄、測試結果、產物與 Pipeline 的流程圖節點（FlowNode）。

### 2.4 Pipeline 執行模型

Pipeline 的 Groovy 程式碼**在 controller 上**以 CPS（Continuation Passing Style）方式解譯執行，只有 `sh`、`bat`、`checkout` 等 step 會透過 remoting 在 agent 上執行。這個模型帶來三個重要後果：

1. **Pipeline 可以在 controller 重啟後繼續**：CPS 會把執行狀態序列化保存，重啟後從中斷點恢復（受 durability 設定影響，見 11.4）
2. **Groovy 邏輯會消耗 controller 資源**：在 Pipeline 中解析大型 JSON、執行大量迴圈或字串處理，都會拖慢整個 controller。重度運算應放到 agent 的 `sh` 步驟中
3. **不是所有 Groovy 語法都能使用**：CPS 轉換後部分寫法行為不同（例如閉包、`each` 的某些用法），且沙箱會限制可呼叫的方法（11.2、11.3）

```mermaid
sequenceDiagram
    participant C as Controller（CPS 引擎）
    participant A as Agent
    C->>C: 解譯 Jenkinsfile Groovy 程式碼
    C->>A: 配置 executor 與 workspace（node／agent）
    C->>A: 執行 sh 'mvn -B verify'
    A-->>C: 回傳結束碼與輸出
    C->>C: 依結果決定下一步（when、post）
    C->>A: junit、archiveArtifacts（檔案從 agent 讀取）
```

### 2.5 JENKINS_HOME 目錄結構

| 路徑 | 內容 | 備份 |
| --- | --- | --- |
| `config.xml` | 全域設定（安全領域、授權策略、雲端設定等） | ✅ 必要 |
| `*.xml`（根目錄其他檔案） | 各 plugin 的全域設定 | ✅ 必要 |
| `credentials.xml` | 全域憑證（加密後） | ✅ 必要，需搭配 `secrets/` |
| `secrets/` | `master.key`、`hudson.util.Secret` 等加密金鑰 | ✅ 必要，**與備份分開存放並嚴格控管** |
| `jobs/<name>/config.xml` | Job 設定 | ✅ 必要 |
| `jobs/<name>/builds/` | 建置紀錄、主控台記錄、測試結果、產物 | 依保存政策 |
| `users/` | 本機使用者、API token、個人設定 | ✅ 必要 |
| `nodes/` | 固定 agent 的設定 | ✅ 必要 |
| `plugins/` | 已安裝的 `.jpi` 與解壓後的目錄 | 可由 `plugins.txt` 重建 |
| `workspace/` | Built-in node 的 workspace | ❌ 不需要 |
| `caches/`、`war/`、`logs/` | 快取、解壓後的 war、系統記錄 | ❌ 不需要 |
| `fingerprints/` | 產物指紋紀錄 | 視需求 |

> ⚠️ `secrets/master.key` 與 `credentials.xml` 一起外洩，就等於所有憑證外洩。備份檔需要加密，並限制可存取的人員（第 20 章）。

### 2.6 Workspace、Artifact、Stash 與 Fingerprint

| 機制 | 位置 | 保存期間 | 用途 |
| --- | --- | --- | --- |
| Workspace | Agent 上 | 直到被清除或 agent 銷毀 | 建置過程的工作目錄 |
| Stash／unstash | Controller 暫存 | 該次 Pipeline 結束即刪除（可用 `preserveStashes` 保留） | 同一次 Pipeline 不同 stage／agent 之間傳遞小型檔案 |
| Artifact（`archiveArtifacts`） | Controller（或外部 artifact manager） | 依 build discarder 設定 | 保存建置產物供下載 |
| Fingerprint | Controller | 長期 | 追蹤產物在不同 Job 間的流向 |

✅ 大型產物（JAR、容器映像、安裝包）應推送到 Nexus、Artifactory、Harbor 等儲存庫，Jenkins 只保存報告與中繼資料。Stash 適合 5 MB 以內的檔案，大量使用會拖慢 controller。

### 2.7 參考架構

| 規模 | 建置量 | 架構 |
| --- | --- | --- |
| 小型（單一團隊） | 每日 < 200 次 | 1 個 controller（4 vCPU／8 GB）、built-in node 0 executor、2–4 個固定或 Docker agent |
| 中型（事業單位） | 每日 200–2,000 次 | 1 個 controller（8 vCPU／16–32 GB、SSD）、Kubernetes 動態 agent、JCasC＋Git 管理設定、外部 artifact 儲存庫、Prometheus 監控 |
| 大型（企業） | 每日 > 2,000 次或多個獨立組織 | 依組織或安全等級拆分多個 controller（每個 controller 皆以 JCasC 建立），共用 Shared Library 與 plugin 清單；考慮 🔒 CloudBees CI 的集中管理 |

```mermaid
flowchart LR
    Dev[開發者] -->|push／PR| SCM[(GitLab／GitHub)]
    SCM -->|Webhook| LB[反向代理／Ingress<br/>TLS 終止]
    LB --> C[Jenkins Controller<br/>JCasC＋plugins.txt]
    C -->|Kubernetes API| K8s[Kubernetes 叢集<br/>動態 Pod agent]
    C -->|SSH／WebSocket| VM[固定 agent<br/>Windows／macOS]
    K8s --> Repo[(Nexus／Harbor)]
    C --> Mon[Prometheus／OTel]
    C --> Vault[(Vault／Secrets Manager)]
    Git[(設定 Git repo<br/>JCasC／Job DSL／Shared Library)] --> C
```

> 💡 拆分 controller 的時機：單一 controller 的 JVM heap 超過 16–24 GB 仍頻繁 Full GC、啟動時間超過 15 分鐘、不同團隊對 plugin 版本有衝突需求，或資安分級要求隔離（例如正式環境部署與一般 CI 分開）。

### 2.8 本章重點

- Controller 只負責協調，built-in node 的 executor 設為 0
- 新部署的 inbound agent 使用 WebSocket，不需要開放 50000 埠
- Pipeline 的 Groovy 程式碼在 controller 上執行，重度運算要放到 agent 的 `sh` 步驟
- `secrets/` 是 Jenkins 最敏感的目錄；備份要加密並與一般備份分開控管

## 3. 安裝與初始設定

### 3.1 系統需求與容量規劃

**官方最低與建議需求**（2.580.1 安裝文件）：

| 項目 | 最低 | 小型團隊建議 | 說明 |
| --- | --- | --- | --- |
| 記憶體 | 256 MB | 4 GB 以上 | 實際需求從數百 MB 到數十 GB，取決於 Job 數量、建置紀錄與 plugin |
| 磁碟 | 1 GB（容器建議 10 GB） | 50 GB 以上 | `JENKINS_HOME` 建議放在獨立的 SSD 磁碟或 PV |
| Java | **Java 21 或 25** | Eclipse Temurin 21 | Controller、agent、CLI 都適用；只測試 HotSpot JVM，不建議 OpenJ9 |
| 瀏覽器 | 近期版本的 Chrome、Edge、Firefox、Safari | — | |

**企業容量規劃參考**（經驗值，需以實際監控資料校正）：

| 規模 | Controller | JVM heap（`-Xmx`） | `JENKINS_HOME` | 同時建置數 |
| --- | --- | --- | --- | --- |
| 小型 | 4 vCPU／8 GB | 4 GB | 100 GB SSD | ≤ 20 |
| 中型 | 8 vCPU／16–32 GB | 8–16 GB | 300–500 GB SSD | 20–150 |
| 大型 | 16 vCPU／64 GB | 16–24 GB | 1 TB 以上（建置紀錄與產物外移） | > 150，或拆分 controller |

> ⚠️ 不要讓 heap 超過實體記憶體的 70%，也不建議單一 controller 使用 32 GB 以上的 heap（G1 GC 停頓時間會明顯增加）。容量不足時優先**拆分 controller、外移產物、縮短建置保留期間**，而不是無限加大 heap。

**網路需求**：

| 方向 | 連接埠 | 用途 |
| --- | --- | --- |
| 使用者 → Controller | 443（經反向代理）或 8080 | Web UI、REST API、Webhook、WebSocket agent |
| Inbound TCP agent → Controller | 50000（可自訂） | 只有使用 TCP inbound agent 才需要；改用 WebSocket 即可關閉 |
| Controller → SSH agent | 22 | SSH Build Agents |
| Controller → 外部 | 443 | update center（`updates.jenkins.io`）、SCM、artifact 儲存庫；封閉網路見 3.9 |

### 3.2 快速體驗：WAR 檔

適合在個人電腦上學習或驗證 plugin，**不適合正式環境**。

```powershell
# Windows：確認 Java 版本（必須是 21 或 25）
java -version

# 下載指定的 LTS 版本（建議固定版本號，不要用 latest）
New-Item -ItemType Directory -Force -Path C:\Jenkins | Out-Null
Invoke-WebRequest -Uri "https://get.jenkins.io/war-stable/2.580.1/jenkins.war" -OutFile "C:\Jenkins\jenkins.war"

# 指定 JENKINS_HOME 後啟動
$env:JENKINS_HOME = "C:\Jenkins\home"
java -Xmx2g -jar C:\Jenkins\jenkins.war --httpPort=8080

# 另開視窗讀取初始管理員密碼
Get-Content "$env:JENKINS_HOME\secrets\initialAdminPassword"
```

```bash
# Linux／macOS
java -version
curl -fLO https://get.jenkins.io/war-stable/2.580.1/jenkins.war
export JENKINS_HOME="$HOME/jenkins-home"
java -Xmx2g -jar jenkins.war --httpPort=8080
cat "$JENKINS_HOME/secrets/initialAdminPassword"
```

> 📌 v1.0 在 PowerShell 中使用 `C:\Users\%USERNAME%\...`（`%USERNAME%` 是 cmd.exe 語法，PowerShell 不會展開）與 bash 的 `\` 續行，兩者在 PowerShell 都無法執行，v2.0 已更正。

<!-- markdownlint-disable-next-line MD028 -->
> 💡 下載後可以用 `https://get.jenkins.io/war-stable/2.580.1/jenkins.war.sha256` 比對 SHA-256 雜湊值（PowerShell：`Get-FileHash C:\Jenkins\jenkins.war -Algorithm SHA256`）。

### 3.3 Linux 套件安裝（systemd）

**Debian／Ubuntu**（2.541.1 起使用新的 `jenkins.io-2026.key`）：

```bash
sudo apt update
sudo apt install -y fontconfig openjdk-21-jre

sudo install -m 0755 -d /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install -y jenkins
```

**RHEL／Rocky／AlmaLinux／Fedora／openSUSE**（2.541.1 起統一使用 `rpm-stable` 套件庫）：

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
  https://pkg.jenkins.io/rpm-stable/jenkins.repo
sudo dnf upgrade -y
sudo dnf install -y fontconfig java-21-openjdk
sudo dnf install -y jenkins
sudo systemctl daemon-reload
sudo systemctl enable --now jenkins
```

> ⚠️ 升級到 2.541.1 以上時，套件管理工具會要求接受新的 GPG key。舊的 `redhat-stable`／`opensuse-stable` 會自動轉向 `rpm-stable`；如需降版到 2.541.1 以前，要改用 `redhat-stable-legacy` 套件庫。

**以 systemd drop-in 調整設定**：主要的 unit 檔是唯讀的，所有自訂都放在 `override.conf`。

```bash
sudo systemctl edit jenkins
```

```ini
[Service]
Environment="JAVA_HOME=/usr/lib/jvm/java-21-openjdk"
Environment="JAVA_OPTS=-Djava.awt.headless=true -Xms4g -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication -XX:+AlwaysPreTouch -Duser.timezone=Asia/Taipei"
Environment="JENKINS_PORT=8080"
Environment="JENKINS_LISTEN_ADDRESS=127.0.0.1"
Environment="CASC_JENKINS_CONFIG=/var/lib/jenkins/casc/"
# 大型實例啟動較慢時延長逾時
TimeoutStartSec=900
```

```bash
sudo chmod 0600 /etc/systemd/system/jenkins.service.d/override.conf
sudo systemctl restart jenkins
sudo systemctl status jenkins
journalctl -u jenkins -f
```

> 💡 `JENKINS_LISTEN_ADDRESS=127.0.0.1` 讓 Jenkins 只接受本機連線，再由同一台主機上的反向代理對外提供 HTTPS（3.8）。

### 3.4 Windows 安裝（MSI）

Windows 的 controller 使用 MSI 安裝程式安裝為 Windows 服務。2.504.1 起已移除「從 Jenkins UI 安裝為服務」的功能，只能使用 MSI。

1. 先安裝 Java 21（例如 Eclipse Temurin 21 MSI）
2. 從 [jenkins.io/download](https://www.jenkins.io/download/) 下載 LTS 的 Windows 安裝程式
3. **服務帳號**：選擇專用的本機或網域帳號（需具備「以服務方式登入（Log on as a service）」權限），**不要使用 LocalSystem**。LocalSystem 等同 Windows 的 root，一旦 Jenkins 或 plugin 被入侵，影響範圍是整台主機
4. 指定連接埠與 Java 目錄，完成安裝

**無人值守安裝**（適合以 Ansible、SCCM、Intune 大量部署）：

```powershell
# 先建立服務帳號並授予 Log on as a service 權限（略）
$svcPassword = Read-Host -AsSecureString "服務帳號密碼"
$plain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($svcPassword))

msiexec.exe /i "C:\Install\jenkins.msi" /qn /norestart `
  INSTALLDIR="D:\Jenkins" `
  JAVA_HOME="<JDK 21 安裝目錄，例如 C:\Program Files\Eclipse Adoptium\jdk-21.x.x-hotspot>" `
  PORT=8080 `
  SERVICE_USERNAME="CORP\svc-jenkins" `
  SERVICE_PASSWORD="$plain" `
  /L*v "C:\Install\jenkins-install.log"
```

**服務管理**：

```powershell
Get-Service Jenkins
Restart-Service Jenkins

# 查看實際的 JENKINS_HOME 與 JVM 參數（設定在安裝目錄的 jenkins.xml）
Select-String -Path "D:\Jenkins\jenkins.xml" -Pattern "JENKINS_HOME|<arguments>"
```

MSI 安裝程式（`jenkinsci/packaging` 的 `msi/build/jenkins.wxs`）寫入 `jenkins.xml` 的預設值如下：

| 設定 | 預設值 |
| --- | --- |
| `JENKINS_HOME`（`<env>`） | 服務帳號的 `%LocalAppData%\Jenkins\.jenkins`；以 LocalSystem 執行時為 `%ProgramData%\Jenkins\.jenkins` |
| `<executable>` | 安裝時選擇的 `<JAVA_HOME>\bin\java.exe` |
| `<arguments>` | `-Xrs -Xmx256m -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle -jar "<安裝目錄>\jenkins.war" --httpPort=<PORT> --webroot="<JENKINS_ROOT>war"` |

⚠️ 預設 heap 只有 **256 MB**，正式使用前一定要調高。編輯 `jenkins.xml` 的 `<arguments>`（先備份原檔），只修改 JVM 參數，其餘保持不變：

```xml
<arguments>-Xrs -Xms4g -Xmx4g -XX:+UseG1GC -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle -jar "D:\Jenkins\jenkins.war" --httpPort=8080 --webroot="C:\Users\svc-jenkins\AppData\Local\Jenkins\war"</arguments>
```

修改後執行 `Restart-Service Jenkins`。v1.0 把這段 XML 放在 PowerShell 區塊中，直接執行會出錯，v2.0 已分開。

> 📌 容器化的 Windows controller 只提供 Windows Server Core 2022／2025 映像（2019 已於 2.568.1 停止提供）。Windows 建置通常以 **Windows agent** 處理即可，controller 建議放在 Linux。

### 3.5 Docker／Podman 容器部署

✅ 正式的容器部署原則：

- 固定映像版本（`jenkins/jenkins:2.580.1-lts-jdk21`），不要使用 `latest` 或 `lts`
- `JENKINS_HOME` 使用具名 volume 或持久化磁碟
- **不要把 `/var/run/docker.sock` 掛進 controller**：任何能在 controller 執行程式碼的人（包括有 Script Console 或建置權限者）都能藉此取得主機 root 權限。建置容器映像改在 agent 上進行（第 15 章）
- controller 的 executor 設為 0，建置交給 agent

**以 Dockerfile 預先安裝 plugin**：

```dockerfile
FROM jenkins/jenkins:2.580.1-lts-jdk21

# 關閉 setup wizard，改由 JCasC 完成初始設定
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc/jenkins.yaml

COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

COPY --chown=jenkins:jenkins casc/ /usr/share/jenkins/ref/casc/
```

`plugins.txt` 的寫法見 [5.3 以 plugins.txt 與 Plugin Installation Manager Tool 管理](#53-以-pluginstxt-與-plugin-installation-manager-tool-管理)，JCasC 見第 18 章。

**Compose 範例：controller＋WebSocket inbound agent**（Docker Compose v2 與 `podman compose` 皆可使用，不需要 `version:` 欄位）：

```yaml
name: jenkins

services:
  controller:
    build: .
    image: registry.example.internal/platform/jenkins-controller:2.580.1-1
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:8080"   # 只對本機開放，由反向代理對外
    environment:
      JAVA_OPTS: >-
        -Djenkins.install.runSetupWizard=false
        -Xms2g -Xmx2g -XX:+UseG1GC
        -Duser.timezone=Asia/Taipei
    # JCasC 會把 /run/secrets/<名稱> 的內容代入 ${<名稱>}，例如 ${jenkins_admin_password}
    secrets:
      - jenkins_admin_password
    volumes:
      - jenkins_home:/var/jenkins_home

  agent-1:
    image: jenkins/inbound-agent:3391.va_37fa_a_305d6d-3-jdk21
    restart: unless-stopped
    depends_on:
      - controller
    environment:
      JENKINS_URL: http://controller:8080/
      JENKINS_AGENT_NAME: agent-1
      JENKINS_SECRET: "@/run/secrets/agent1_secret"   # agent.jar 的 -secret @檔案 語法
      JENKINS_WEB_SOCKET: "true"
      JENKINS_AGENT_WORKDIR: /home/jenkins/agent
    secrets:
      - agent1_secret
    volumes:
      - agent1_work:/home/jenkins/agent

secrets:
  jenkins_admin_password:
    file: ./secrets/jenkins_admin_password
  agent1_secret:
    file: ./secrets/agent1_secret

volumes:
  jenkins_home:
  agent1_work:
```

> 💡 `agent-1` 需要先在 controller 建立同名的固定節點（JCasC 範例見 [18.2 JCasC 基礎](#182-jcasc-基礎)），再把節點頁面上的 secret 寫入 `./secrets/agent1_secret`。`JENKINS_URL`、`JENKINS_AGENT_NAME`、`JENKINS_SECRET`、`JENKINS_WEB_SOCKET`、`JENKINS_AGENT_WORKDIR` 都是 `jenkins/inbound-agent` 映像啟動腳本支援的環境變數；`JENKINS_SECRET` 以 `@` 開頭時，`agent.jar` 會從該檔案讀取 secret，避免 secret 出現在 `docker inspect` 結果中。

**官方的 Docker-in-Docker 教學環境**：jenkins.io 的 Docker 安裝教學使用 `docker:dind`（`--privileged`）搭配自訂映像，**只適合學習用途**。正式環境請改用第 14、15 章的 Kubernetes agent 與無 daemon 映像建置。

### 3.6 Kubernetes（Helm）部署

官方 Helm chart `jenkins/jenkins`（5.9.64）預設就以 JCasC 設定 controller、以 Kubernetes plugin 動態建立 Pod agent、controller executor 為 0。

```bash
helm repo add jenkins https://charts.jenkins.io
helm repo update
helm upgrade --install jenkins jenkins/jenkins \
  --namespace jenkins --create-namespace \
  --version 5.9.64 \
  -f values-prod.yaml
```

`values-prod.yaml` 範例：

```yaml
controller:
  image:
    tag: "2.580.1-lts-jdk21"     # 明確指定時，chart 不會再附加 tagLabel
  numExecutors: 0
  admin:
    createSecret: false
    existingSecret: jenkins-admin   # 事先以 kubectl 或 External Secrets Operator 建立
    userKey: jenkins-admin-user
    passwordKey: jenkins-admin-password
  javaOpts: "-Xms4g -Xmx4g -XX:+UseG1GC -Duser.timezone=Asia/Taipei"
  resources:
    requests:
      cpu: "2"
      memory: "6Gi"
    limits:
      memory: "6Gi"
  jenkinsUrl: https://jenkins.example.internal/
  installPlugins:
    - kubernetes:4557.ve746270f672f
    - workflow-aggregator:608.v67378e9d3db_1
    - git:5.10.1
    - configuration-as-code:2131.vb_a_13ed96f755
  installLatestPlugins: false        # 相依 plugin 安裝最低相容版本，避免意外升級
  initializeOnce: true               # 只在第一次安裝時下載 plugin
  ingress:
    enabled: true
    ingressClassName: nginx
    hostName: jenkins.example.internal
    tls:
      - secretName: jenkins-tls
        hosts:
          - jenkins.example.internal
  JCasC:
    configScripts:
      welcome: |
        jenkins:
          systemMessage: "本 Jenkins 由 JCasC 管理，請勿在 UI 直接修改設定"

persistence:
  enabled: true
  storageClass: fast-ssd
  size: 200Gi

agent:
  enabled: true
  image:
    repository: "jenkins/inbound-agent"
    tag: "3391.va_37fa_a_305d6d-3-jdk21"
  resources:
    requests:
      cpu: "500m"
      memory: "1Gi"
    limits:
      memory: "2Gi"

networkPolicy:
  enabled: true
```

> ⚠️ Chart 的 `controller.replicas` 最大只能是 1。Jenkins controller 是單一實例應用程式，不能以增加副本達成高可用（見 [20.4 高可用與災難復原](#204-高可用與災難復原)）。

<!-- markdownlint-disable-next-line MD028 -->
> 💡 Jenkins Kubernetes Operator（`jenkinsci/kubernetes-operator`）仍在維護，但社群與官方文件以 Helm chart 為主要部署方式；新導入建議使用 Helm＋JCasC。

### 3.7 Setup Wizard 與初始安全設定

以 WAR、套件或 MSI 安裝時，第一次開啟 Jenkins 會進入 Setup Wizard：

1. **解鎖**：輸入 `JENKINS_HOME/secrets/initialAdminPassword` 的內容
2. **安裝 plugin**：選擇「Install suggested plugins」。2.580.1 的建議清單包括 Folders、OWASP Markup Formatter、Build Timeout、Credentials Binding、Timestamper、Workspace Cleanup、Ant、Gradle、Pipeline、GitHub Branch Source、Pipeline: GitHub Groovy Libraries、Pipeline Graph View、Git、SSH Build Agents、Matrix Authorization Strategy、LDAP、Email Extension、Mailer、Dark Theme
3. **建立第一個管理員帳號**：不要略過此步驟；略過時帳號會是 `admin`，密碼為初始密碼
4. **設定 Jenkins URL**：填入使用者實際存取的 HTTPS 網址（例如 `https://jenkins.example.internal/`），Webhook、通知連結與 agent 連線都依賴此設定

**完成 wizard 後立即檢查的安全設定**（Manage Jenkins → Security）：

| 項目 | 建議值 |
| --- | --- |
| Security Realm | 企業環境改用 LDAP／Active Directory／OIDC／SAML（[17.2 驗證（Security Realm）](#172-驗證security-realm)） |
| Authorization | Matrix-based 或 Role-based，**不要使用「Anyone can do anything」或「Legacy mode」** |
| Built-in node executors | `0` |
| Agent TCP port | 使用 WebSocket agent 時設為 Disable |
| Markup Formatter | Safe HTML（OWASP Markup Formatter） |
| CSRF Protection | 預設啟用，不要關閉 |
| API token | 不允許建立 legacy token |

> 📌 2.555.1 起 CSRF crumb 不再包含用戶端 IP；JCasC 若仍保留 `crumbIssuer.standard.excludeClientIPFromCrumb` 區段，Jenkins 會中止啟動（[18.3 JCasC 實務](#183-jcasc-實務)）。

### 3.8 反向代理與 TLS

正式環境應由反向代理（Nginx、Apache、HAProxy、Ingress）負責 TLS，Jenkins 只監聽本機或叢集內部位址。以下是 jenkins.io 官方 Nginx 範例的重點設定，已加上 HTTPS 與 WebSocket：

```nginx
upstream jenkins {
  keepalive 32;
  server 127.0.0.1:8080;
}

# WebSocket agent 與 HTTP keepalive 都需要
map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      '';
}

server {
  listen 443 ssl;
  http2 on;
  server_name jenkins.example.internal;

  ssl_certificate     /etc/nginx/tls/jenkins.crt;
  ssl_certificate_key /etc/nginx/tls/jenkins.key;
  ssl_protocols       TLSv1.2 TLSv1.3;

  ignore_invalid_headers off;

  location / {
    proxy_pass         http://jenkins;
    proxy_redirect     default;
    proxy_http_version 1.1;

    proxy_set_header   Connection        $connection_upgrade;
    proxy_set_header   Upgrade           $http_upgrade;
    proxy_set_header   Host              $http_host;
    proxy_set_header   X-Real-IP         $remote_addr;
    proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Proto $scheme;
    proxy_max_temp_file_size 0;

    client_max_body_size    100m;   # 依上傳的 artifact／plugin 大小調整
    proxy_connect_timeout   90;
    proxy_send_timeout      90;
    proxy_read_timeout      90;
    proxy_request_buffering off;    # HTTP 模式的 Jenkins CLI 需要
  }
}

server {
  listen 80;
  server_name jenkins.example.internal;
  return 301 https://$host$request_uri;
}
```

設定完成後到 Manage Jenkins → System 確認 **Jenkins URL** 為 `https://jenkins.example.internal/`。若 Manage Jenkins 頁面出現「It appears that your reverse proxy set up is broken」警示，通常是 `X-Forwarded-Proto`、`Host` 標頭或 Jenkins URL 不一致。

### 3.9 離線（封閉網路）安裝

封閉網路無法連到 `updates.jenkins.io`，需要事先在可連網的建置機準備所有檔案：

```bash
# 在可連網的機器上：依 plugins.txt 下載 plugin 及其相依項目
curl -fLO https://github.com/jenkinsci/plugin-installation-manager-tool/releases/download/2.15.0/jenkins-plugin-manager-2.15.0.jar
curl -fLO https://get.jenkins.io/war-stable/2.580.1/jenkins.war

java -jar jenkins-plugin-manager-2.15.0.jar \
  --war jenkins.war \
  --plugin-file plugins.txt \
  --plugin-download-directory ./plugins \
  --verbose

# 封裝後經由核准的媒體或檔案交換區傳入封閉網路
tar czf jenkins-2.580.1-offline.tgz jenkins.war plugins/ plugins.txt
sha256sum jenkins-2.580.1-offline.tgz > jenkins-2.580.1-offline.tgz.sha256
```

在封閉網路中，把 `plugins/*.jpi` 放到 `JENKINS_HOME/plugins/`（或打包進容器映像）後再啟動 Jenkins。

> ⚠️ 2.580.1 起，bouncycastle API、Instance Identity、SSH server、JavaMail API 等 9 個 detached plugin 不再打包於 `jenkins.war`。連網環境會自動下載；**離線環境必須把它們列入 `plugins.txt`**，否則依賴它們的 plugin 會無法載入。plugin-installation-manager-tool 會依 `--war` 指定的版本自動解析這些相依項目。

<!-- markdownlint-disable-next-line MD028 -->
> 💡 大型封閉網路可以架設內部 update center 鏡像（例如以 Nexus／Artifactory 的 generic proxy 或 `jenkins-infra/update-center2` 產生的靜態站台），再到 Manage Jenkins → Plugins → Advanced settings 修改 Update Site URL。

### 3.10 本章重點

- 正式環境使用 Linux 套件、容器映像或 Helm 部署固定版本的 LTS，並以 Java 21 執行
- 不要掛載 `docker.sock`、不要在 controller 執行建置、不要使用 LocalSystem 執行 Windows 服務
- 由反向代理負責 TLS 與 WebSocket，並正確設定 Jenkins URL
- 離線環境要預先下載 plugin，2.580.1 起還要把 detached plugin 列入清單

## 4. 介面導覽與系統管理

### 4.1 介面配置（2.516.1 起的新版標頭）

2.516.1 重新設計了頁首，v1.0 的截圖與「左側選單 → Manage Jenkins」說明已不適用：

| 區域 | 位置 | 內容 |
| --- | --- | --- |
| 頁首左側 | 上方 | Jenkins 標誌與**麵包屑導覽**（Dashboard › Folder › Job › #建置編號），每一層都有下拉選單可直接跳到設定、建置紀錄等動作 |
| 頁首右側 | 上方 | 搜尋（command palette，快捷鍵 `Ctrl`+`K`／`⌘`+`K`）、**Manage Jenkins（齒輪圖示）**、通知、使用者選單（個人設定、API token、登出）、More actions（Support Core 等 plugin 動作） |
| 側邊欄 | 左側 | 目前頁面可執行的動作（New Item、Build Now、Configure、Pipeline Overview 等） |
| 主內容 | 中央 | Job 清單（Dashboard）、建置狀態、Pipeline 流程圖 |
| 建置執行狀態 | Dashboard 左下 | Build Queue 與各 agent 的 executor 狀態 |

**Pipeline 視覺化**：2.580.1 的 setup wizard 建議安裝 **Pipeline Graph View**，在 Job 與建置頁面提供「Pipeline Overview」（stage 流程圖、每個 step 的記錄、平行分支）。舊的 Pipeline: Stage View 仍可安裝，但已不在建議清單中。Blue Ocean 雖仍有維護發行，但已多年沒有新功能，新導入不建議依賴。

> 💡 個人化設定（使用者選單 → Appearance）可切換 Dark Theme、調整主控台字型；2.528.1 起每位使用者也可以選擇自己的 Views Tab Bar 樣式。

### 4.2 Manage Jenkins 功能分區

以下為 2.580.1 安裝本手冊建議 plugin 後的 Manage Jenkins 頁面（部分項目由 plugin 提供）：

| 分區 | 項目 | 用途 | 管理建議 |
| --- | --- | --- | --- |
| System Configuration | System | Jenkins URL、系統訊息、全域屬性、各 plugin 全域設定 | 以 JCasC 管理 |
| | Tools | JDK、Maven、Gradle、Git 等工具安裝設定 | 優先改用容器化 agent（9.1） |
| | Plugins | 安裝、更新、停用 plugin，進階設定（proxy、update site） | 以 `plugins.txt` 管理（5.3） |
| | Nodes | 固定 agent 管理、built-in node 設定 | executor 數 0 |
| | Clouds | Kubernetes、EC2、Azure VM 等動態 agent 設定 | 以 JCasC 管理 |
| | Configuration as Code | 檢視、重新載入、匯出 JCasC | 第 18 章 |
| | Appearance | 主題、主控台顯示 | |
| | Managed files | Config File Provider 管理的 `settings.xml`、`.npmrc` 等 | 9.2 |
| | Lockable Resources | 共用資源（測試環境、硬體裝置）鎖定 | 11.5 |
| Security | Security | 安全領域、授權策略、agent 連線、CSRF、API token、CSP | 第 17 章 |
| | Credentials | 憑證管理 | 第 7 章 |
| | Credential Providers | 啟用的憑證來源與類型 | 停用不需要的 provider |
| | Users | 本機使用者（只有使用 Jenkins 自有使用者資料庫時） | 企業環境改用 SSO |
| Status Information | System Information | 系統屬性、環境變數、plugin 清單、thread dump | 故障排除（第 23 章） |
| | Logs | 系統記錄與自訂 log recorder | 23.1 |
| | Load Statistics | 佇列長度與 executor 使用率 | 容量規劃 |
| | About Jenkins | 版本與第三方授權 | |
| Troubleshooting | Manage Old Data | plugin 移除後殘留的舊設定資料 | 升級後檢查 |
| Tools and Actions | Reload Configuration from Disk | 從磁碟重新讀取所有設定 | ⚠️ 會中斷進行中的操作，以 JCasC reload 取代 |
| | Jenkins CLI | 下載 `jenkins-cli.jar` 與指令說明 | 附錄 A |
| | Script Console | 以管理員權限執行任意 Groovy | ⚠️ 見 4.5 |
| | Prepare for Shutdown | 停止接受新建置，等待執行中的建置結束 | 維護前使用 |

### 4.3 Views 與 Dashboard

| View 類型 | 來源 | 用途 |
| --- | --- | --- |
| List View | Core | 依名稱、正規表示式或手動勾選列出 Job |
| My View | Core | 顯示目前使用者有權限的 Job |
| Folder | Folders plugin | ✅ **建議的主要組織方式**：可設定權限、憑證、Shared Library，取代大量 View |
| Build Monitor View | Build Monitor plugin | 大型螢幕顯示建置狀態（團隊看板） |

✅ 組織 Job 的建議做法：

1. 以 **Folder** 依「事業單位／產品／團隊」分層，每個團隊在自己的 folder 內管理 Multibranch Pipeline
2. 以 **Organization Folder** 自動對應 GitHub organization 或 GitLab group，新的 repository 自動出現
3. View 只用於跨 folder 的看板需求（例如「所有正式環境部署 Job」），以正規表示式篩選並以 JCasC 定義

```mermaid
flowchart TD
    Root[Dashboard] --> BU1[Folder：payments]
    Root --> BU2[Folder：channels]
    Root --> Ops[Folder：platform-ops]
    BU1 --> T1[Organization Folder：payments-gitlab-group]
    T1 --> R1[Multibranch：payment-api]
    T1 --> R2[Multibranch：settlement-batch]
    BU2 --> R3[Multibranch：mobile-bff]
    Ops --> J1[Pipeline：nightly-backup-verify]
    Ops --> J2[Pipeline：seed-job（Job DSL）]
```

### 4.4 系統設定要點

Manage Jenkins → System 中最常需要調整的設定（JCasC 鍵名見第 18 章）：

| 設定 | 建議值 | 說明 |
| --- | --- | --- |
| Jenkins URL | `https://jenkins.example.internal/` | 必須與使用者實際存取的網址一致 |
| System Admin e-mail address | `jenkins-noreply@example.internal` | 通知信寄件者 |
| System Message | 維運公告、變更凍結通知 | 支援 Safe HTML |
| `# of executors`（built-in node） | `0` | 在 Nodes → Built-In Node 設定 |
| Quiet period | `5` 秒 | 合併短時間內的多次觸發 |
| SCM checkout retry count | `2` | 減少網路瞬斷造成的失敗 |
| Global properties → Environment variables | 只放非機密的全域變數（例如內部 registry 位址） | 機密一律使用 Credentials |
| Global Build Discarders | 依 Job 類型設定保留天數與筆數（19.6） | 避免磁碟耗盡 |

> ⚠️ 不要在 Global properties 放置密碼或 token：這些值會以明文出現在系統設定、`config.xml` 與每次建置的環境變數中。

### 4.5 Script Console 與管理介面的風險

Script Console（Manage Jenkins → Script Console）可以用 controller 的權限執行任意 Groovy 程式碼，**等同於 controller 主機上的完整權限**，包括讀取 `secrets/` 並解密所有憑證。

✅ 管理原則：

- 只有少數平台管理員擁有 `Overall/Administer` 權限，並使用個人帳號（非共用帳號）登入，以 Audit Trail plugin 記錄操作（[17.10 稽核與集中記錄](#1710-稽核與集中記錄)）
- 例行性的管理動作改用 **JCasC、Job DSL 或 REST API**，不要依賴 Script Console 腳本
- 一定要使用 Script Console 時，先在預備環境測試，並把腳本保存在 Git 中審查

以下為唯讀的查詢範例（不修改任何設定），可在 Script Console 執行：

```groovy
import jenkins.model.Jenkins

def j = Jenkins.get()
println "Jenkins 版本：${Jenkins.VERSION}"
println "Java 版本：${System.getProperty('java.version')}（${System.getProperty('java.vendor')}）"
println "Built-in node executors：${j.numExecutors}"
println "Agent 數量：${j.nodes.size()}"
def rt = Runtime.runtime
println String.format('Heap：已使用 %,d MB／上限 %,d MB',
        (rt.totalMemory() - rt.freeMemory()).intdiv(1024 * 1024),
        rt.maxMemory().intdiv(1024 * 1024))

// 列出所有啟用中的 plugin 與版本（可轉成 plugins.txt）
j.pluginManager.plugins
    .findAll { it.isEnabled() }
    .sort { it.shortName }
    .each { println "${it.shortName}:${it.version}" }
```

> 📌 v1.0 的「設定全域建置記錄保留策略」腳本會直接改寫所有 Job 並呼叫 `item.save()`，在 Multibranch 子 Job 上不會生效（會被下次掃描覆蓋），也無法追蹤變更。v2.0 改用 Global Build Discarders 與 Jenkinsfile 的 `buildDiscarder` 選項（[19.6 建置保留與磁碟管理](#196-建置保留與磁碟管理)）。

### 4.6 本章重點

- 2.516.1 起 Manage Jenkins 位於頁首右側齒輪圖示，Pipeline 視覺化改用 Pipeline Graph View
- 以 Folder 與 Organization Folder 組織 Job，View 只用於跨團隊看板
- 系統設定以 JCasC 管理；Global properties 不放機密
- Script Console 等同主機完整權限，只限少數管理員使用並保留稽核紀錄

## 5. Plugin 管理

### 5.1 Plugin 架構與相依關係

Plugin 以 `.jpi`（或 `.hpi`）檔案形式放在 `JENKINS_HOME/plugins/`，啟動時由 core 載入。每個 plugin 都宣告：

- **最低 core 版本**（`Jenkins-Version`）：例如 Coverage 3.3394 需要 2.555.3 以上，Warnings NG 13.10294 需要 2.555.3 以上
- **相依 plugin 與最低版本**：例如 `workflow-aggregator` 只是一個「聚合」plugin，本身沒有功能，會帶入約 20 個 Pipeline 相關 plugin
- **Detached plugin**：原本屬於 core、後來拆分出來的功能（JUnit、Mailer、Matrix Authorization 等）。2.580.1 起這些 plugin 不再打包在 `jenkins.war` 中，由 update center 依需要下載

```mermaid
flowchart TD
    WA[workflow-aggregator<br/>Pipeline] --> WJ[workflow-job]
    WA --> WCPS[workflow-cps]
    WA --> PMD[pipeline-model-definition<br/>Declarative]
    WA --> PGL[pipeline-groovy-lib<br/>Shared Library]
    WA --> WDS[workflow-durable-task-step<br/>sh／bat]
    PMD --> CB[credentials-binding]
    WCPS --> SS[script-security<br/>沙箱]
    K8s[kubernetes] --> WDS
    K8s --> KC[kubernetes-client-api]
    GBS[github-branch-source] --> SCMAPI[scm-api]
    GBS --> GIT[git]
```

> ⚠️ 相依鏈中任何一個 plugin 有漏洞，都會影響整個 Jenkins。plugin 數量越少，攻擊面與升級風險越小。一般企業 controller 建議控制在 150 個以內（含相依項目）。

### 5.2 選擇 Plugin 的評估準則

安裝任何 plugin 前，先在 [plugins.jenkins.io](https://plugins.jenkins.io/) 確認以下項目：

| 準則 | 判斷方式 | 不建議安裝的訊號 |
| --- | --- | --- |
| 維護狀態 | 最近一次發行日期、GitHub 活動、是否標示「up for adoption」 | 超過 2 年沒有發行；標示需要新維護者 |
| 安全公告 | plugin 頁面的 Security warnings 區塊 | 有「尚未修補」的公告 |
| 棄用狀態 | update center 的 `deprecations` 清單 | 標示 deprecated |
| Health score | plugin 頁面的健康分數（測試、相依項目更新、CI 狀態等） | 分數偏低 |
| 安裝數 | plugin 頁面的安裝趨勢 | 安裝數極少且下降中 |
| 替代方案 | 能否用 Pipeline step、`sh` 指令或既有 plugin 達成 | 只為單一小功能引入大量相依 |

> 💡 很多需求不需要 plugin：呼叫 REST API 可以用 `sh 'curl ...'`；解析 JSON／YAML 可以用 Pipeline Utility Steps 的 `readJSON`／`readYaml`；發送 Teams／Slack 訊息也可以直接呼叫 webhook。

### 5.3 以 plugins.txt 與 Plugin Installation Manager Tool 管理

✅ **企業標準做法**：plugin 清單與版本放在 Git，以 [Plugin Installation Manager Tool](https://github.com/jenkinsci/plugin-installation-manager-tool)（2.15.0）安裝；容器映像中的 `jenkins-plugin-cli` 就是同一個工具。UI 上的「Install」只用於預備環境的評估。

**本手冊的基準 `plugins.txt`**（2026-10-02 的 update center 版本，已以 2.580.1 解析相依並確認無安全警示）：

```text
configuration-as-code:2131.vb_a_13ed96f755
job-dsl:3732.v9a_c49a_61a_313
cloudbees-folder:6.1106.v3a_d9a_6d2465e
workflow-aggregator:608.v67378e9d3db_1
pipeline-graph-view:1041.v107d70db_b_1a_f
pipeline-groovy-lib:806.v408277b_33d1d
pipeline-utility-steps:3.810.va_7672d206740
pipeline-milestone-step:152.v6e22b_8cfc66c
lockable-resources:1560.va_b_cd589f23eb_
timestamper:1.30
ansicolor:542.v03d235fee02d
build-timeout:1.41
ws-cleanup:0.49
git:5.10.1
github-branch-source:1983.vfa_27ed961853
gitlab-branch-source:744.vb_d0403d08ec7
credentials-binding:728.v902a_273b_8947
ssh-agent:433.v9e73d67c3f74
hashicorp-vault-plugin:384.vda_86ec66c537
kubernetes:4557.ve746270f672f
docker-workflow:653.v2f2c08eff0ec
junit:1431.vc0d98912a_756
coverage:3.3394.v60e914558d29
warnings-ng:13.10294.v3c81839da_a_e7
sonar:2.19.0
pipeline-maven:1760.v9a_a_e6dcb_0444
config-file-provider:1013.v73c323e52b_1f
matrix-auth:3.3
role-strategy:918.v91e5468d8db_2
oic-auth:4.718.ve731df6ca_88a_
ldap:825.v2fca_37dd5b_cb_
authorize-project:534.v2f208c45e11c
audit-trail:456.v39d2fd1ed556
prometheus:860.v532442b_44e9a_
opentelemetry:3.1603.ve3fa_cc8a_b_f5e
email-ext:2038.v7b_8817a_499d9
mailer:534.v1b_36f5864073
antisamy-markup-formatter:173.v680e3a_b_69ff3
versioncolumn:400.v3c5c3004f31d
support-core:1865.v45d40b_778b_cb_
```

各 plugin 的用途與替代說明見 [附錄 C：Plugin 建議清單](#附錄-cplugin-建議清單)。

**常用指令**：

```bash
PIMT="java -jar jenkins-plugin-manager-2.15.0.jar --war jenkins.war"

# 1. 檢查清單能否解析、是否有安全警示（不下載）
$PIMT -f plugins.txt --no-download --view-security-warnings

# 2. 列出可更新的版本，輸出成新的 plugins.txt 供審查
$PIMT -f plugins.txt --available-updates --output txt > plugins-updates.txt

# 3. 下載到指定目錄（用於建立映像或離線套件）
$PIMT -f plugins.txt -d ./plugins --verbose
```

> 💡 `--latest false` 讓相依 plugin 使用「最低相容版本」而非最新版，可降低意外升級的風險；Helm chart 的對應設定是 `controller.installLatestPlugins: false`。

**變更流程**：

```mermaid
flowchart LR
    A[提出 plugin 變更<br/>修改 plugins.txt 的 MR／PR] --> B[CI：PIMT 解析與<br/>安全警示檢查]
    B --> C[建立新的 controller 映像]
    C --> D[部署至預備 controller<br/>執行冒煙 Pipeline]
    D --> E{審查通過?}
    E -->|是| F[排程更新正式 controller]
    E -->|否| A
```

### 5.4 已棄用 Plugin 與替代方案

以下為 v1.0 使用或企業常見、但目前已棄用、有未修補漏洞或不建議新導入的 plugin（依 2026-10-02 update center 資料）：

| Plugin | 狀態 | 替代方案 |
| --- | --- | --- |
| Checkstyle、PMD、FindBugs（`checkstyle`、`pmd`、`findbugs`） | 已棄用並自 update center 下架 | **Warnings Next Generation**（`recordIssues`，13.3） |
| JaCoCo（`jacoco`）、Cobertura（`cobertura`）、Code Coverage API（`code-coverage-api`） | 長期未發行（Cobertura 最後發行於 2021、Code Coverage API 於 2023） | **Coverage**（`recordCoverage`，13.2） |
| Extended Choice Parameter | **已棄用且有多個未修補漏洞**（SECURITY-1350、1351、2232 等） | Active Choices（`uno-choice`）或 Declarative 內建參數 |
| Office 365 Connector | 已自 update center 下架；Microsoft 365 Connectors 已停用 | Teams Workflows webhook＋`httpRequest` 或 `curl`（19.7） |
| Build Pipeline、Delivery Pipeline 類視覺化 plugin | 以 Freestyle 串接為前提 | Pipeline＋Pipeline Graph View |
| Maven Integration（Maven project 類型） | 仍有維護，但官方建議改用 Pipeline | Pipeline＋Pipeline Maven Integration（9.3） |
| Pipeline: Stage View | 仍可安裝，不在建議清單 | Pipeline Graph View |
| Folder-based Authorization Strategy（`folder-auth`） | **有未修補漏洞**（SECURITY-3062） | Matrix Authorization（folder 層級權限）或 Role-based Strategy |
| GitHub Pull Request Builder（`ghprb`） | **有未修補漏洞** | GitHub Branch Source（Multibranch） |
| Environment Injector（`envinject`） | 與 Java 17+ 的模組系統衝突，需要 `--add-opens` | Pipeline `environment`／`withEnv` |

> ⚠️ 已安裝的 plugin 若出現在 Manage Jenkins 的安全警示或棄用通知中，請在下一次維護窗口前移除或替換，並在 [24.5 LTS 升級](#245-lts-升級) 的升級檢查清單中追蹤。

### 5.5 更新策略與離線 update center

| 更新類型 | 頻率 | 做法 |
| --- | --- | --- |
| 安全公告修補 | 公告後 7 天內 | 只更新受影響的 plugin，於預備環境驗證後上線 |
| 例行更新 | 每月一次 | 以 `--available-updates` 產生差異清單，整批驗證 |
| Core LTS 升級 | 每季（跟隨 `.1` 或 `.2`） | **升級前後各更新一次 plugin**（官方升級指南要求），見 [20.3 升級程序](#203-升級程序) |

**離線或受控網路**：

- 在 Manage Jenkins → Plugins → Advanced settings 把 Update Site 改成內部鏡像，或完全停用線上更新，只透過映像或 `plugins/` 目錄部署
- 2.580.1 起 detached plugin 不在 war 中，離線部署時 plugin 清單必須完整（由 PIMT 以 `--war` 解析即可得到）
- 以 PIMT 的 `--jenkins-update-center` 與 `--jenkins-update-center-download-url` 參數指向內部鏡像

### 5.6 本章重點

- Plugin 清單與版本放在 Git，以 Plugin Installation Manager Tool 建置映像或離線套件
- 安裝前檢查維護狀態、安全公告與棄用狀態；能用 Pipeline step 或指令解決的需求就不要加 plugin
- Checkstyle／PMD／FindBugs／JaCoCo plugin 改用 Warnings NG 與 Coverage；移除 Extended Choice Parameter 等有未修補漏洞的 plugin
- Core 升級前後都要更新 plugin

## 6. Job 類型與 Freestyle

### 6.1 何時仍使用 Freestyle

Freestyle project 以 UI 表單設定，設定內容存在 `config.xml`，無法隨程式碼一起審查與版本控制。v2.0 的定位是：

| 情境 | 建議 |
| --- | --- |
| 應用程式 CI/CD | ❌ 不使用 Freestyle，改用 Multibranch Pipeline |
| 簡單的維運工作（例如每日清理暫存檔、呼叫一支腳本） | ⚠️ 可以使用，但建議改成 Pipeline 並以 Job DSL 建立，方便追蹤 |
| 既有大量 Freestyle Job | 依 [6.5 Freestyle 遷移至 Pipeline](#65-freestyle-遷移至-pipeline) 的優先順序逐步遷移 |
| 學習 Jenkins 基本概念 | ✅ 適合用來理解觸發、建置步驟、後置動作的概念 |

### 6.2 Freestyle 設定區塊

| 區塊 | 內容 | Pipeline 對應 |
| --- | --- | --- |
| General | 描述、捨棄舊建置、參數化、限制執行節點（label） | `options { buildDiscarder() }`、`parameters {}`、`agent { label }` |
| Source Code Management | Git repository、憑證、分支 | `checkout scm` |
| Build Triggers | 定期建置、SCM 輪詢、遠端觸發、其他 Job 完成後觸發 | `triggers {}`、Multibranch webhook |
| Build Environment | 清除 workspace、逾時、時間戳記、憑證綁定 | `options { timeout() }`、`withCredentials` |
| Build Steps | Shell、Windows batch、Maven、Gradle 等步驟 | `steps { sh … }` |
| Post-build Actions | 測試報告、產物保存、通知、觸發其他 Job | `post {}` 與對應 step |

#### 範例：每日清理暫存目錄的 Freestyle Job

1. New Item → 名稱 `ops-clean-tmp` → Freestyle project
2. General：勾選「Discard old builds」，保留 14 天、最多 30 筆；「Restrict where this project can be run」填 `linux && ops`
3. Build Triggers：勾選「Build periodically」，排程 `H 2 * * *`
4. Build Environment：勾選「Terminate a build if it's stuck」（逾時 30 分鐘）與「Add timestamps to the Console Output」
5. Build Steps → Execute shell：

   ```bash
   #!/usr/bin/env bash
   set -euo pipefail
   # 刪除 7 天前的暫存檔，只處理指定目錄
   find /data/app/tmp -type f -mtime +7 -print -delete
   df -h /data
   ```

6. Post-build Actions：E-mail Notification，收件者填維運群組信箱

> ⚠️ Freestyle 的 shell 步驟預設以 `/bin/sh -xe` 執行；在腳本第一行加上 `#!/usr/bin/env bash` 與 `set -euo pipefail`，才能在管線指令失敗時正確中止。

### 6.3 建置觸發與 Cron 語法

Jenkins 的排程語法為 5 個欄位：`分 時 日 月 星期`，並支援 `H`（hash）分散負載：

| 寫法 | 意義 |
| --- | --- |
| `H * * * *` | 每小時一次，分鐘由 Job 名稱雜湊決定（不同 Job 錯開） |
| `H/15 * * * *` | 每 15 分鐘一次（起始分鐘錯開） |
| `H 2 * * 1-5` | 週一到週五凌晨 2 點的某一分鐘 |
| `H(0-29) 3 * * *` | 每天 3:00–3:29 之間的某一分鐘 |
| `H H(0-5) * * *` | 每天 0:00–5:59 之間的某個時間 |
| `@midnight` | 每天 0:00–2:59 之間（等同 `H H(0-2) * * *`） |
| `TZ=Asia/Taipei`（第一行） | 指定排程時區；之後的排程以此時區解讀 |

```text
TZ=Asia/Taipei
# 週一到週五 08:00–08:59 之間執行夜間測試的結果彙整
H 8 * * 1-5
```

✅ 一律使用 `H`，避免所有 Job 在整點同時啟動造成尖峰（v1.0 範例的 `0 2 * * *` 會讓所有 Job 同時在 2:00 執行）。

**觸發方式比較**：

| 方式 | 延遲 | 對 SCM 的負擔 | 建議 |
| --- | --- | --- | --- |
| Webhook（GitHub／GitLab／Bitbucket） | 秒級 | 低 | ✅ 預設方式（[8.5 Webhook 觸發與輪詢](#85-webhook-觸發與輪詢)） |
| SCM 輪詢（Poll SCM） | 依排程 | 高（大量 Job 時會拖慢 SCM） | 只在無法接收 webhook 時使用，排程至少 `H/15` |
| 定期建置（Build periodically） | 依排程 | 無 | 夜間建置、定期掃描、維運工作 |
| 上游 Job 觸發 | 秒級 | 無 | 改用 Pipeline 的 `build job:` step 或 `triggers { upstream(...) }` |
| 遠端觸發（Trigger builds remotely） | 秒級 | 無 | ⚠️ 不建議：token 寫在 URL；改用具備 API token 的服務帳號呼叫 REST API |

### 6.4 參數化建置

| 參數類型 | 用途 | 注意事項 |
| --- | --- | --- |
| String | 版本號、目標主機 | 在 shell 中使用時要加上引號，避免指令注入 |
| Choice | 部署環境（dev／sit／uat） | 第一個選項為預設值 |
| Boolean | 是否執行選擇性步驟 | |
| Password | ⚠️ 不建議 | 值會（加密後）保存在每一筆建置紀錄中，執行者每次都要手動輸入，也容易在 shell 中被意外輸出；改用 Credentials 參數或 `withCredentials` |
| Credentials | 讓使用者在執行時選擇憑證 | 需搭配憑證權限控管 |
| File | 上傳檔案 | 在 Pipeline 中支援度有限 |
| Active Choices（plugin） | 動態選項（例如從 registry 讀取 tag 清單） | 腳本需經 Script Approval |

> ⚠️ **指令注入**：使用者輸入的參數若直接拼接進 shell 字串（例如 `sh "deploy.sh ${params.TARGET}"`），輸入 `x; rm -rf /` 就會執行任意指令。Pipeline 中請以環境變數傳遞並在 shell 內加上引號：`sh 'deploy.sh "$TARGET"'`（Groovy 單引號字串不內插），詳見 [10.3 environment 與字串內插](#103-environment-與字串內插)。

### 6.5 Freestyle 遷移至 Pipeline

**遷移優先順序**：

1. 正式環境部署 Job（最需要稽核與審查）
2. 經常修改設定的 Job
3. 多個 Freestyle 以上下游串接的流程（改成單一 Pipeline 的多個 stage）
4. 其餘維運 Job（以 Job DSL 批次建立）

**對照範例**：一個「Git checkout → Maven 建置 → 發佈 JUnit 報告 → 保存 JAR → 寄信」的 Freestyle Job，改寫成 Declarative Pipeline：

```groovy
pipeline {
    agent { label 'linux && maven' }
    options {
        buildDiscarder(logRotator(daysToKeepStr: '30', numToKeepStr: '50'))
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
    }
    triggers {
        pollSCM('H/15 * * * *')   // 能接收 webhook 時請移除，改用 Multibranch
    }
    tools {
        jdk 'jdk-21'
        maven 'maven-3.9'
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn -B -ntp clean verify'
            }
        }
    }
    post {
        always {
            junit testResults: '**/target/surefire-reports/*.xml', allowEmptyResults: true
        }
        success {
            archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
        }
        failure {
            mail to: 'team-payments@example.internal',
                 subject: "建置失敗：${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "請查看 ${env.BUILD_URL}"
        }
    }
}
```

> 💡 遷移時可先在 Freestyle Job 的設定頁逐一對照 6.2 的表格。社群的「Convert To Pipeline」plugin 已因 RCE 漏洞（SECURITY-2963、2966）不再建議使用，請手動改寫。

### 6.6 本章重點

- 新的應用程式 CI/CD 一律使用 Multibranch Pipeline；Freestyle 只保留給簡單維運工作
- 排程使用 `H` 分散負載，並以 `TZ=` 明確指定時區
- 參數不要直接拼接進 shell 字串；不要使用 Password 參數保存機密
- Freestyle 遷移以正式環境部署 Job 為第一優先

## 7. 憑證與機密管理

### 7.1 Credentials 架構與類型

Jenkins 的 Credentials plugin 提供統一的憑證儲存與存取介面。憑證以 controller 的 `secrets/` 金鑰加密後存放，Pipeline 只以 **ID** 引用，不在程式碼中出現實際值。

```mermaid
flowchart LR
    subgraph Providers[憑證來源 Credentials Provider]
        P1[Jenkins 內建儲存<br/>System／Folder／User]
        P2[Kubernetes Secret<br/>kubernetes-credentials-provider]
        P3[AWS Secrets Manager<br/>唯讀 provider]
        P4[HashiCorp Vault<br/>Vault credentials／withVault]
    end
    Providers --> API[Credentials API<br/>以 ID 查詢]
    API --> B1[withCredentials]
    API --> B2[environment credentials]
    API --> B3[checkout／sshagent／<br/>docker.withRegistry 等 step]
    B1 --> M[主控台輸出遮罩]
```

| 類型 | 用途 | Pipeline 綁定方式 |
| --- | --- | --- |
| Username with password | Git over HTTPS、Nexus、資料庫帳號 | `usernamePassword(...)`、`credentials()` 產生 `_USR`／`_PSW` |
| Secret text | API token、Webhook URL、SonarQube token | `string(...)` |
| Secret file | `kubeconfig`、`settings.xml`、服務帳號 JSON 金鑰 | `file(...)`（取得暫存檔路徑） |
| SSH Username with private key | Git over SSH、部署到 Linux 主機 | `sshUserPrivateKey(...)`、`sshagent([...])` |
| Certificate（PKCS#12） | 用戶端憑證驗證、程式碼簽章 | `certificate(...)` |
| GitHub App | GitHub Branch Source 的 API 與 checkout 驗證 | 由 SCM 設定使用（[8.2 GitHub 整合（GitHub App 驗證）](#82-github-整合github-app-驗證)） |
| GitLab Personal／Group Access Token | GitLab Branch Source | 由 SCM 設定使用（[8.3 GitLab 整合](#83-gitlab-整合)） |
| Vault Token／AppRole 等 | 存取 HashiCorp Vault | `withVault(...)` |

### 7.2 憑證作用域

| 作用域 | 誰可以使用 | 適用 |
| --- | --- | --- |
| **System** | 只有 Jenkins 本身（例如連線 agent、SCM 掃描、寄信），Job **不能**使用 | Agent SSH 金鑰、Kubernetes cloud 憑證、SMTP 帳號 |
| **Global** | 所有 Job（只要知道 ID） | 少數真正全域共用的唯讀憑證 |
| **Folder** | 該 folder 內的 Job | ✅ **建議預設**：團隊與環境專屬的憑證放在對應的 folder |
| **User** | 以該使用者身分執行的建置（需搭配 Authorize Project） | 個人測試；正式流程不建議 |

✅ 建議的憑證分層：

```text
Dashboard
├── （System）agent-ssh-key、k8s-cloud-token、smtp-relay
├── （Global）nexus-readonly、sonar-token-readonly
├── payments/                         ← Folder credentials
│   ├── gitlab-payments-token
│   ├── nexus-deployer-payments
│   └── prod/                         ← 子 folder：只有正式部署 Job 放在這裡
│       └── kubeconfig-prod-payments
└── channels/
    └── ...
```

> ⚠️ Global 憑證可被**任何** Job 引用。只要有人能修改任何一個 Jenkinsfile（例如在 PR 中），就可能把 Global 憑證送到外部。正式環境憑證務必放在權限受控的 folder，並限制哪些分支或 Job 可以執行部署（[17.4 建置的執行身分（Authorize Project）](#174-建置的執行身分authorize-project)）。

### 7.3 在 Pipeline 使用憑證

#### 方法一：`environment` 區塊搭配 `credentials()`

```groovy
pipeline {
    agent { label 'linux' }
    environment {
        // Username with password：自動產生 NEXUS、NEXUS_USR、NEXUS_PSW
        NEXUS = credentials('nexus-deployer-payments')
        // Secret text：直接取得值
        SONAR_TOKEN = credentials('sonar-token')
    }
    stages {
        stage('Publish') {
            steps {
                // ✅ 單引號：由 shell 展開環境變數，Groovy 不內插
                sh 'mvn -B -ntp deploy -Dnexus.user="$NEXUS_USR" -Dnexus.password="$NEXUS_PSW"'
            }
        }
    }
}
```

#### 方法二：`withCredentials` 限縮使用範圍（✅ 建議，憑證只在區塊內有效）

```groovy
pipeline {
    agent { label 'linux' }
    environment {
        CHART_VERSION = '1.4.2'
    }
    stages {
        stage('Deploy') {
            steps {
                withCredentials([
                    file(credentialsId: 'kubeconfig-sit-payments', variable: 'KUBECONFIG'),
                    usernamePassword(credentialsId: 'harbor-robot-payments',
                                     usernameVariable: 'REG_USER',
                                     passwordVariable: 'REG_PASS')
                ]) {
                    sh '''
                        set -euo pipefail
                        echo "$REG_PASS" | helm registry login harbor.example.internal -u "$REG_USER" --password-stdin
                        helm upgrade --install payment-api oci://harbor.example.internal/charts/payment-api \
                          --version "$CHART_VERSION" --namespace payments-sit --wait
                    '''
                }
            }
        }
    }
}
```

#### 方法三：SSH 金鑰（`sshagent`）

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Tag') {
            steps {
                sshagent(credentials: ['gitlab-deploy-key']) {
                    sh '''
                        git tag -a "v${BUILD_NUMBER}" -m "release ${BUILD_NUMBER}"
                        git push origin "v${BUILD_NUMBER}"
                    '''
                }
            }
        }
    }
}
```

> 💡 `sshagent` 需要 SSH Agent plugin，且 agent 上要有 `ssh-agent` 指令。Windows agent 建議改用 HTTPS＋token。

### 7.4 遮罩的限制與常見外洩途徑

Jenkins 只會把憑證的**原始值**在主控台輸出中替換為 `****`。以下情況**不會**被遮罩：

| 外洩途徑 | 範例 | 防範 |
| --- | --- | --- |
| Groovy 字串內插 | `sh "curl -u admin:${PASS} ..."`（雙引號） | 一律用單引號字串，讓 shell 展開變數。Jenkins 會在記錄中警告「A secret was passed to "sh" using Groovy String interpolation, which is insecure」 |
| 編碼後的值 | `echo $PASS \| base64`、URL encode 後的 token | 不要對機密做任何轉換後輸出 |
| 拆字或部分輸出 | `echo ${PASS:0:4}` | 禁止任何形式的輸出 |
| 寫入檔案並保存為產物 | 把 `settings.xml` 一起 `archiveArtifacts` | 在 `post { cleanup { ... } }` 刪除，或寫到 workspace 以外 |
| 指令列參數 | `mvn -Dpassword=$PASS`（同主機其他使用者可用 `ps` 看到） | 改用環境變數或設定檔（Config File Provider） |
| `set -x` 偵錯模式 | shell 回顯展開後的指令 | 使用憑證的區塊內不要 `set -x` |
| 測試報告、HTML 報告 | 測試把連線字串寫入報告 | 程式碼審查與報告掃描 |

> ⚠️ 遮罩不是安全邊界。**任何可以修改 Jenkinsfile 的人都能取得該 Pipeline 可用的所有憑證**（例如把值寫到外部網址）。真正的控管手段是「憑證放在哪個 folder」與「誰能修改哪些 Pipeline、哪些分支能部署」（第 17 章）。

### 7.5 外部機密管理

| 方案 | 運作方式 | 適用 |
| --- | --- | --- |
| **HashiCorp Vault plugin** | `withVault` 在建置時讀取機密並設為環境變數；也可作為 JCasC 的 secret source | 已有 Vault 的組織；需要動態機密（資料庫短效帳號） |
| **Kubernetes Credentials Provider** | 把帶有 `jenkins.io/credentials-type` 標籤的 Kubernetes Secret 映射為 Jenkins 憑證（唯讀） | Jenkins 跑在 Kubernetes，機密由 External Secrets Operator 同步 |
| **AWS Secrets Manager Credentials Provider** | 把帶有 `jenkins:credentials:type` 標籤的 Secrets Manager 機密映射為 Jenkins 憑證（唯讀） | AWS 環境 |
| **Azure Key Vault plugin** | 以 Key Vault 作為 credentials provider 與 JCasC secret source | Azure 環境 |

**Vault 範例**（KV v2，engine version 預設為 2）：

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Integration Test') {
            steps {
                withVault(configuration: [vaultUrl: 'https://vault.example.internal',
                                          vaultCredentialId: 'vault-approle-ci',
                                          engineVersion: 2],
                          vaultSecrets: [[path: 'kv/payments/sit/db',
                                          secretValues: [[envVar: 'DB_USER', vaultKey: 'username'],
                                                         [envVar: 'DB_PASS', vaultKey: 'password']]]]) {
                    sh './gradlew integrationTest'
                }
            }
        }
    }
}
```

**Kubernetes Secret 映射為 Jenkins 憑證**：

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: nexus-deployer-payments          # 即 Jenkins 憑證 ID
  namespace: jenkins                     # Jenkins controller 所在的 namespace
  labels:
    "jenkins.io/credentials-type": "usernamePassword"
  annotations:
    "jenkins.io/credentials-description": "Nexus deployer（由 External Secrets 同步）"
type: Opaque
stringData:
  username: payments-deployer
  password: "<由 External Secrets Operator 自 Vault 同步，勿手動填寫>"
```

> 💡 外部機密管理的主要效益是**集中輪替與稽核**。Jenkins 端的憑證 ID 保持不變，輪替在 Vault／Secrets Manager 完成，Pipeline 不需要修改。

### 7.6 以 JCasC 管理憑證

JCasC 可以宣告憑證，但**實際值不能寫在 YAML 中**，要以變數引用 secret source（環境變數、`/run/secrets/` 檔案、Kubernetes Secret、Vault）：

```yaml
credentials:
  system:
    domainCredentials:
      - credentials:
          - usernamePassword:
              scope: GLOBAL
              id: "nexus-readonly"
              description: "Nexus 唯讀帳號"
              username: "ci-reader"
              password: "${nexus_readonly_password}"
          - string:
              scope: GLOBAL
              id: "sonar-token"
              description: "SonarQube analysis token"
              secret: "${sonar_token}"
          - basicSSHUserPrivateKey:
              scope: SYSTEM
              id: "agent-ssh-key"
              description: "SSH agent 連線金鑰"
              username: "jenkins"
              privateKeySource:
                directEntry:
                  privateKey: "${readFile:/run/secrets/agent_ssh_key}"
```

Folder 層級的憑證以 Job DSL 建立 folder 時一併宣告，或由團隊管理員在 UI 中維護。

> ⚠️ JCasC 的匯出功能（`/configuration-as-code/viewExport`）會輸出加密後的 `{AQAAABAAAAAQ...}` 字串。這些密文只能由同一個 controller 的 `secrets/` 解密，不能用在其他 controller，也不應提交到 Git。

### 7.7 本章重點

- 憑證以 ID 引用，預設放在 folder 層級；System 範圍只給 Jenkins 本身使用
- 一律用單引號字串讓 shell 展開機密變數；遮罩只能防止意外輸出，不能防止惡意取用
- 能修改 Pipeline 的人就能取得其可用的憑證，正式環境憑證必須搭配 folder 權限與分支控管
- 大型組織以 Vault／Kubernetes Secret／Secrets Manager 集中管理與輪替機密

## 8. SCM 整合

### 8.1 Git plugin 與 checkout

| 寫法 | 使用時機 |
| --- | --- |
| `checkout scm` | ✅ Multibranch／Organization Folder：取出觸發此次建置的分支或 PR（含 merge 結果），憑證沿用 branch source 設定 |
| `git url: ..., branch: ..., credentialsId: ...` | 單一分支 Pipeline 的簡化寫法 |
| `checkout scmGit(...)` | 需要淺層複製、子模組、sparse checkout、指定參考 repository 等進階選項 |

**大型 repository 的進階 checkout**（Declarative 預設會自動 checkout，先以 `skipDefaultCheckout()` 關閉）：

```groovy
pipeline {
    agent { label 'linux' }
    options {
        skipDefaultCheckout()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[url: 'https://gitlab.example.internal/payments/monorepo.git',
                                         credentialsId: 'gitlab-payments-token']],
                    extensions: [
                        cloneOption(shallow: true, depth: 20, noTags: false, timeout: 20),
                        sparseCheckout(sparseCheckoutPaths: [[path: 'services/payment-api/'],
                                                             [path: 'build-logic/']]),
                        submodule(recursiveSubmodules: true, parentCredentials: true),
                        cleanBeforeCheckout(deleteUntrackedNestedRepositories: true)
                    ])
            }
        }
    }
}
```

| 擴充選項 | 效果 | 注意事項 |
| --- | --- | --- |
| `cloneOption(shallow: true, depth: N)` | 只取最近 N 個 commit，大幅減少時間與磁碟 | 需要完整歷史的工具（例如 SonarQube 的 blame、`git describe`）要調大 depth |
| `sparseCheckout` | 只取出指定目錄 | Monorepo 適用 |
| `cloneOption(reference: '/cache/repo.git')` | 以 agent 上的參考 repository 加速 | 參考 repository 要定期更新 |
| `cleanBeforeCheckout` | 每次建置前清除未追蹤檔案 | 固定 agent 建議開啟 |
| `submodule(parentCredentials: true)` | 子模組沿用主 repository 的憑證 | |

> ⚠️ Git plugin 5.x 的 `git` 指令來自 agent 本身。請確保 agent 映像中的 Git 版本足夠新（建議 2.40 以上），並設定 Manage Jenkins → Security → Git Host Key Verification 為「Known hosts file」或「Manually provided keys」，**不要使用「No verification」**。

### 8.2 GitHub 整合（GitHub App 驗證）

✅ 連接 GitHub（含 GitHub Enterprise Server）時，使用 **GitHub App** 而不是個人 Personal Access Token：

| 比較 | Personal Access Token | GitHub App |
| --- | --- | --- |
| 身分 | 綁定個人帳號；人員離職即失效 | 組織擁有的應用程式 |
| API rate limit | 每小時 5,000 次（與該使用者共用） | 每個安裝獨立計算，隨 repository 數增加 |
| 權限 | 粗略（scope） | 細緻（逐項權限、可限定 repository） |
| 狀態回報 | Commit status | Commit status 與 Checks API |

**建立步驟**：

1. GitHub organization → Settings → Developer settings → GitHub Apps → New GitHub App
2. Webhook URL 填 `https://jenkins.example.internal/github-webhook/`，並設定 Webhook secret
3. 權限：Commit statuses（Read and write）、Contents（Read-only；需要推送 tag 時改 Read and write）、Metadata（Read-only）、Pull requests（Read-only）；使用 Checks 回報時加上 Checks（Read and write）
4. 產生 private key，並轉換為 Jenkins 需要的 PKCS#8 格式：

   ```bash
   openssl pkcs8 -topk8 -inform PEM -outform PEM \
     -in jenkins-ci.2026-10-02.private-key.pem \
     -out converted-github-app.pem -nocrypt
   ```

5. 把 App 安裝到 organization（可限定 repository）
6. 在 Jenkins 新增「GitHub App」類型憑證（或以 JCasC 宣告，金鑰由 secret source 提供）：

   ```yaml
   credentials:
     system:
       domainCredentials:
         - credentials:
             - gitHubApp:
                 id: "github-app"
                 description: "GitHub App：jenkins-ci"
                 appID: "123456"
                 privateKey: "${github_app_private_key}"
   ```

7. Manage Jenkins → System → GitHub → GitHub Server：設定 API URL（GitHub Enterprise 為 `https://github.example.internal/api/v3`）與 Webhook shared secret

> 💡 GitHub App 憑證在 Multibranch 中被 `withCredentials` 取用時，可透過「repository access strategy」與「default permissions strategy」限縮到只讀取目前 repository，降低 PR 中惡意程式碼取得寫入權限的風險。

### 8.3 GitLab 整合

使用 **GitLab Branch Source** plugin（Multibranch／Organization Folder）。舊的 `gitlab-plugin` 適合 Freestyle 或單一 Pipeline 的觸發，兩者不要在同一個 Job 混用。

```yaml
credentials:
  system:
    domainCredentials:
      - credentials:
          - gitlabPersonalAccessToken:
              scope: SYSTEM
              id: "gitlab-ci-token"
              description: "GitLab 服務帳號 token（api scope）"
              token: "${gitlab_ci_token}"
          - string:
              scope: SYSTEM
              id: "gitlab-webhook-secret"
              description: "GitLab webhook secret token"
              secret: "${gitlab_webhook_secret}"
unclassified:
  gitLabServers:
    servers:
      - name: "gitlab-internal"
        serverUrl: "https://gitlab.example.internal"
        credentialsId: "gitlab-ci-token"
        manageWebHooks: true
        manageSystemHooks: false
        webhookSecretCredentialsId: "gitlab-webhook-secret"
```

> 📌 GitLab Branch Source 已把 `secretToken` 標示為 deprecated，改以 `webhookSecretCredentialsId` 引用 Secret text 憑證。plugin README 的 JCasC 範例仍是舊寫法；在 2.580.1 搭配目前版本使用 `secretToken`，`configuration-as-code/check` 會直接回報「'secretToken' is deprecated」並拒絕套用。

| 項目 | 說明 |
| --- | --- |
| Token | 建議使用 GitLab **Group Access Token** 或服務帳號的 PAT，scope 為 `api`；只有需要 system hook 時才給管理員權限 |
| Webhook 路徑 | `https://jenkins.example.internal/gitlab-webhook/post`（plugin 自動管理時會自動建立） |
| System hook 路徑 | `https://jenkins.example.internal/gitlab-systemhook/post`（新專案自動出現在 Organization Folder） |
| Webhook secret | 必須設定（`webhookSecretCredentialsId`），Jenkins 會驗證 webhook 的 `X-Gitlab-Token` |

### 8.4 Bitbucket 與其他 SCM

| SCM | Plugin | Webhook 路徑 |
| --- | --- | --- |
| Bitbucket Cloud／Data Center | Bitbucket Branch Source（`cloudbees-bitbucket-branch-source`） | `/bitbucket-scmsource-hook/notify` |
| Gitea | Gitea plugin | `/gitea-webhook/post` |
| 任意 Git 伺服器 | Git plugin＋Generic Webhook Trigger | 依 plugin 設定 |
| Subversion | Subversion plugin | 以輪詢或 post-commit hook 呼叫 REST API |

### 8.5 Webhook 觸發與輪詢

```mermaid
sequenceDiagram
    participant Dev as 開發者
    participant SCM as GitHub／GitLab
    participant RP as 反向代理
    participant J as Jenkins
    Dev->>SCM: git push／建立 MR／PR
    SCM->>RP: POST /github-webhook/（或 /gitlab-webhook/post）
    RP->>J: 轉送（保留 Host 與 X-Forwarded-*）
    J->>J: 驗證 webhook secret
    J->>J: 比對 Multibranch 的 branch source
    J->>J: 建立或排入對應分支／PR 的建置
    J-->>SCM: 回報 commit status／Checks（pending → success／failure）
```

✅ Webhook 的部署注意事項：

- Jenkins URL 必須是 SCM 能連到的位址；若 Jenkins 在內網而 SCM 是 SaaS，只對 webhook 路徑開放公開入口（或使用 SCM 的 IP 允許清單），**不要把整個 Jenkins UI 暴露到網際網路**
- 一定要設定 webhook secret
- 保留低頻率的週期掃描（例如 `H H * * *`）作為 webhook 遺失時的補救，不要以高頻輪詢取代 webhook

### 8.6 Multibranch Pipeline 與 Organization Folder

Multibranch 以 **branch source** 定義「掃描哪個 repository」，以 **traits（Behaviours）** 定義「發現哪些分支、PR、tag，以及信任哪些 fork」。

| Trait | 建議設定 | 原因 |
| --- | --- | --- |
| Discover branches | 「Exclude branches that are also filed as PRs」 | 避免同一個分支在 branch 與 PR 各建置一次 |
| Discover pull requests from origin | 「Merging the pull request with the current target branch revision」 | 驗證合併後的結果 |
| Discover pull requests from forks | Trust：「From users with Admin or Write permission」 | ⚠️ fork 的 PR 可修改 Jenkinsfile；信任外部 fork 等同允許任何人在 Jenkins 執行程式碼 |
| Discover tags | 視發佈流程需要 | 搭配 Basic Branch Build Strategies 避免掃描時一次建置所有歷史 tag |
| Orphaned Item Strategy | 刪除已不存在分支的 Job，保留 7–14 天 | 控制 Job 數量與磁碟 |

> ⚠️ **不受信任的 PR**：對於不受信任來源的 PR，Jenkins 會改用**目標分支**的 Jenkinsfile 執行，但 PR 的程式碼（例如 `pom.xml`、測試、建置腳本）仍會被執行。公開專案或外部協作者的 PR 應在隔離的 agent 上建置，且無法取用部署憑證（[17.4 建置的執行身分（Authorize Project）](#174-建置的執行身分authorize-project)）。

**以 Job DSL 建立 Multibranch（GitHub）**：

```groovy
// Job DSL：建立 folder 與 Multibranch Pipeline
folder('payments') {
    displayName('Payments 產品線')
    description('由 seed job 管理，請勿在 UI 修改')
}

multibranchPipelineJob('payments/payment-api') {
    branchSources {
        branchSource {
            source {
                github {
                    id('payments-payment-api')
                    repoOwner('example-org')
                    repository('payment-api')
                    repositoryUrl('https://github.com/example-org/payment-api')
                    configuredByUrl(true)
                    credentialsId('github-app')
                    traits {
                        gitHubBranchDiscovery {
                            strategyId(1)   // 1：排除同時是 PR 的分支
                        }
                        gitHubPullRequestDiscovery {
                            strategyId(1)   // 1：與目標分支合併後建置
                        }
                        gitHubForkDiscovery {
                            strategyId(1)
                            trust {
                                gitHubTrustPermissions()
                            }
                        }
                    }
                }
            }
        }
    }
    factory {
        workflowBranchProjectFactory {
            scriptPath('Jenkinsfile')
        }
    }
    orphanedItemStrategy {
        discardOldItems {
            daysToKeep(14)
        }
    }
}
```

**以 Job DSL 建立 Organization Folder（GitLab group）**：

```groovy
// Job DSL：GitLab group 對應 Organization Folder
organizationFolder('payments-gitlab') {
    displayName('Payments（GitLab group）')
    organizations {
        gitLabSCMNavigator {
            projectOwner('payments')
            serverName('gitlab-internal')
            credentialsId('gitlab-ci-token')
            traits {
                subGroupProjectDiscoveryTrait()
                gitLabBranchDiscovery {
                    strategyId(1)
                }
                originMergeRequestDiscoveryTrait {
                    strategyId(1)
                }
            }
        }
    }
    projectFactories {
        workflowMultiBranchProjectFactory {
            scriptPath('Jenkinsfile')
        }
    }
    orphanedItemStrategy {
        discardOldItems {
            daysToKeep(14)
        }
    }
}
```

### 8.7 分支策略與 Pipeline 對應

| 分支策略 | 分支 | Pipeline 行為（以 `when` 實作，見 [10.6 when 條件](#106-when-條件)） |
| --- | --- | --- |
| **Trunk-based／GitHub Flow**（✅ 建議） | `main`＋短期 feature 分支、PR | PR：建置、測試、品質門檻；`main`：再加上映像建置、部署 dev／sit；tag `v*`：部署 uat／prod |
| GitLab Flow（環境分支） | `main` → `pre-production` → `production` | 合併到環境分支即觸發該環境部署 |
| Git Flow | `develop`、`release/*`、`hotfix/*`、`main` | `develop`：部署 dev；`release/*`：部署 sit／uat；`main`＋tag：部署 prod |

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Build & Test') {
            steps {
                sh './mvnw -B -ntp verify'
            }
        }
        stage('Deploy DEV') {
            when {
                branch 'main'
            }
            steps {
                echo '部署至 dev'
            }
        }
        stage('Deploy PROD') {
            when {
                buildingTag()
                tag pattern: 'v\\d+\\.\\d+\\.\\d+', comparator: 'REGEXP'
            }
            steps {
                echo "部署 ${env.TAG_NAME} 至 prod"
            }
        }
    }
}
```

> 📌 v1.0 的分支條件範例在 `environment` 區塊中，以寫在一般雙引號字串內、跨越多行的三元運算式計算 `BRANCH_TYPE`；一般雙引號字串不能跨行，Pipeline 直接出現語法錯誤。v2.0 改以 `when { branch ... }` 判斷，需要計算時放在 `script {}` 區塊中。

### 8.8 本章重點

- Multibranch 中使用 `checkout scm`；大型 repository 以淺層複製與 sparse checkout 加速
- GitHub 使用 GitHub App，GitLab 使用 Group Access Token；webhook 一定要設定 secret
- Fork PR 只信任具寫入權限的使用者，並在隔離 agent 上建置
- 以 Job DSL 建立 Multibranch 與 Organization Folder，分支策略優先採用 trunk-based

## 9. 建置工具整合（Maven、Gradle 與多語言）

### 9.1 工具管理策略

| 方式 | 做法 | 優點 | 缺點 |
| --- | --- | --- | --- |
| **容器化 agent**（✅ 建議） | `agent { docker { image 'maven:3.9.16-eclipse-temurin-21' } }` 或 Kubernetes Pod 中的 `maven` 容器 | 版本由映像固定、可重現、不同專案互不干擾 | 需要容器執行環境 |
| **Maven／Gradle Wrapper**（✅ 建議並用） | repository 內的 `mvnw`／`gradlew` 指定工具版本 | 開發者本機與 CI 一致 | 仍需要 agent 提供 JDK |
| Global Tool Configuration | Manage Jenkins → Tools 定義 `jdk-21`、`maven-3.9`，Pipeline 以 `tools {}` 引用 | 不需容器；適合 Windows／固定 agent | 自動安裝需連網；版本變更影響所有 Job |

> 📌 版本基準（2026-10-02）：Maven 3.9.16 為穩定基準；Maven **3.10.0** 於 2026-10-01 發行，導入前請先以專案實際建置驗證；Maven 4 仍在 RC 階段。Gradle 為 9.8.0。官方映像 `maven:3.9.16-eclipse-temurin-21`、`maven:3.10.0-eclipse-temurin-21`、`gradle:9.8.0-jdk21` 皆已確認存在。

**以 JCasC 定義工具**（不使用自動安裝，路徑由 agent 映像或組態管理工具提供）：

```yaml
tool:
  jdk:
    installations:
      - name: "jdk-21"
        home: "/opt/java/jdk-21"
      - name: "jdk-17"
        home: "/opt/java/jdk-17"
  maven:
    installations:
      - name: "maven-3.9"
        home: "/opt/maven/apache-maven-3.9.16"
```

> 💡 建置用的 JDK 與執行 agent 的 JDK 互相獨立。即使 agent 必須以 Java 21 執行，仍然可以用 `tools { jdk 'jdk-17' }` 或 `maven:3.9.16-eclipse-temurin-17` 映像建置 Java 17 的專案。

### 9.2 Maven 最佳實務

| 項目 | 建議 | 原因 |
| --- | --- | --- |
| 批次模式 | `mvn -B -ntp` | 關閉互動與下載進度輸出，主控台記錄縮小 90% 以上 |
| 目標 | PR 用 `verify`，發佈用 `deploy` | `install` 會寫入共用的本機 repository，造成 Job 之間互相污染 |
| 版本 | 以 `-Drevision=<版本>`（CI-friendly versions）或 `versions:set` 設定 | 不要在 CI 中修改 `pom.xml` 再提交回去 |
| `settings.xml` | 以 Config File Provider 管理，帳密由 Credentials 注入 | 不要把 `settings.xml` 放在 repository 或 agent 映像中 |
| 鏡像 | 所有相依套件透過內部 Nexus／Artifactory 代理 | 速度、可用性、供應鏈控管（第 21 章） |
| 測試失敗處理 | 不要用 `-Dmaven.test.failure.ignore=true` 讓建置「成功」；由 `junit` step 把結果標記為 UNSTABLE | 避免失敗的測試被忽略 |
| 平行建置 | `-T 1C` | 多模組專案縮短時間（需確認 plugin 是 thread-safe） |

**以 Config File Provider 管理 `settings.xml`**（JCasC）：

```yaml
unclassified:
  globalConfigFiles:
    configs:
      - mavenSettings:
          id: "maven-settings-nexus"
          name: "Maven settings（內部 Nexus）"
          comment: "所有 Maven 專案共用；帳密由 Credentials 注入"
          isReplaceAll: true
          serverCredentialMappings:
            - serverId: "nexus"
              credentialsId: "nexus-deployer"
          content: |
            <settings xmlns="http://maven.apache.org/SETTINGS/1.2.0">
              <mirrors>
                <mirror>
                  <id>nexus</id>
                  <mirrorOf>*</mirrorOf>
                  <url>https://nexus.example.internal/repository/maven-public/</url>
                </mirror>
              </mirrors>
              <servers>
                <server>
                  <id>nexus</id>
                </server>
              </servers>
            </settings>
```

`serverCredentialMappings` 會在建置時把 `nexus-deployer` 憑證的帳號密碼填入 `<server id="nexus">`，`settings.xml` 本身不含任何機密。

### 9.3 Pipeline 中的 Maven 建置

#### 方式一：容器化 agent＋Config File Provider（✅ 建議）

```groovy
pipeline {
    agent {
        docker {
            image 'maven:3.9.16-eclipse-temurin-21'
            label 'linux && docker'
            args '-v maven-repo-cache:/root/.m2/repository'
        }
    }
    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '30'))
    }
    stages {
        stage('Build & Test') {
            steps {
                configFileProvider([configFile(fileId: 'maven-settings-nexus', variable: 'MAVEN_SETTINGS')]) {
                    sh 'mvn -B -ntp -s "$MAVEN_SETTINGS" clean verify'
                }
            }
            post {
                always {
                    junit testResults: '**/target/surefire-reports/*.xml,**/target/failsafe-reports/*.xml',
                          allowEmptyResults: true
                }
            }
        }
        stage('Publish') {
            when {
                branch 'main'
            }
            steps {
                configFileProvider([configFile(fileId: 'maven-settings-nexus', variable: 'MAVEN_SETTINGS')]) {
                    sh 'mvn -B -ntp -s "$MAVEN_SETTINGS" deploy -DskipTests -Drevision="1.4.${BUILD_NUMBER}"'
                }
            }
        }
    }
}
```

#### 方式二：Pipeline Maven Integration（`withMaven`）

`withMaven` 會自動設定 Maven 與 settings，並在建置後**自動發佈** JUnit、SpotBugs 等報告與產物指紋，也能追蹤上下游 Maven 專案的相依觸發。

```groovy
pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('Build') {
            steps {
                withMaven(maven: 'maven-3.9',
                          jdk: 'jdk-21',
                          mavenSettingsConfig: 'maven-settings-nexus',
                          mavenLocalRepo: '.repository',
                          publisherStrategy: 'EXPLICIT',
                          options: [junitPublisher(healthScaleFactor: 1.0),
                                    artifactsPublisher(disabled: true)]) {
                    sh 'mvn -B clean verify'
                }
            }
        }
    }
}
```

> ⚠️ `withMaven` 的自動發佈會把建置產物複製到 controller。大型專案請以 `publisherStrategy: 'EXPLICIT'` 只啟用需要的 publisher，並停用 `artifactsPublisher`，產物改推送到 Nexus。

### 9.4 Gradle

```groovy
pipeline {
    agent {
        docker {
            image 'gradle:9.8.0-jdk21'
            label 'linux && docker'
        }
    }
    environment {
        GRADLE_USER_HOME = "${env.WORKSPACE}/.gradle-home"
    }
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'nexus-reader',
                                                  usernameVariable: 'ORG_GRADLE_PROJECT_nexusUser',
                                                  passwordVariable: 'ORG_GRADLE_PROJECT_nexusPassword')]) {
                    sh './gradlew --no-daemon --build-cache --console=plain clean build'
                }
            }
            post {
                always {
                    junit testResults: '**/build/test-results/test/*.xml', allowEmptyResults: true
                }
            }
        }
    }
}
```

| 建議 | 說明 |
| --- | --- |
| 使用 `./gradlew` | 版本由 `gradle/wrapper/gradle-wrapper.properties` 固定，並在 CI 驗證 wrapper checksum（`distributionSha256Sum`） |
| `--no-daemon` | 容器化或短命 agent 中不需要 daemon |
| `ORG_GRADLE_PROJECT_<name>` | Gradle 會把此環境變數視為 project property，避免把帳密寫在 `gradle.properties` |
| Build Cache | 以內部 Gradle remote cache（Develocity 或自建 HTTP cache）加速 |

### 9.5 相依套件快取

| Agent 類型 | 快取策略 |
| --- | --- |
| 固定 agent | 每個 agent 一份本機 repository；以 `mvn -Dmaven.repo.local=...` 依 Job 分隔，避免平行建置互相覆寫 |
| Docker agent | 以具名 volume 掛載 `/root/.m2/repository`（9.3 範例） |
| Kubernetes agent | 以 PVC（ReadWriteMany）或節點本機的 hostPath 快取；或完全依賴內部 Nexus 代理，接受較長的下載時間以換取隔離性（14.4） |

> ⚠️ 共用快取可能被惡意建置寫入竄改過的套件（快取毒化）。處理不受信任 PR 的 agent 不應與正式發佈 Pipeline 共用快取。

### 9.6 版本號與發佈

```mermaid
flowchart LR
    A[PR 建置<br/>verify] -->|合併| B[main 建置<br/>1.4.BUILD_NUMBER-SNAPSHOT 或 1.4.BUILD_NUMBER]
    B --> C[推送至 Nexus<br/>maven-snapshots／maven-releases]
    C --> D[建置容器映像<br/>tag＝版本＋commit SHA]
    D --> E[依 digest 晉升至各環境]
```

✅ 建議做法：

- 版本號由 Pipeline 決定（例如 `1.4.${BUILD_NUMBER}` 或 `git describe`），以 Maven CI-friendly `${revision}` 傳入，不在 CI 中修改並提交 `pom.xml`
- 正式版產物在 Nexus 設為不可覆寫（disable redeploy）
- 同一個產物只建置一次，之後各環境以相同版本或映像 digest 晉升（[16.1 環境與晉升模型](#161-環境與晉升模型)）

### 9.7 其他語言的建置範例

企業中 Java 以外的專案也應走相同的流程：容器化工具鏈、固定版本、測試報告轉成 JUnit XML、相依套件經內部代理。

| 語言 | 映像（2026-10-02 確認存在） | 相依套件代理 | 測試報告 |
| --- | --- | --- | --- |
| Node.js | `node:24-bookworm-slim`（Active LTS）、`node:22-bookworm-slim` | `.npmrc` 的 `registry=` 指向 Nexus npm proxy（Config File Provider 管理） | `jest-junit`、`mocha-junit-reporter` |
| Python | `python:3.13-slim`、`python:3.14-slim` | `PIP_INDEX_URL` 指向 Nexus PyPI proxy | `pytest --junitxml` |
| .NET | `mcr.microsoft.com/dotnet/sdk:10.0`（LTS） | `nuget.config` 指向 Nexus NuGet proxy | `dotnet test --logger "junit"`（JunitXml.TestLogger） |
| Go | `golang:1.26-bookworm` | `GOPROXY` 指向 Nexus Go proxy 或 Athens | `gotestsum --junitfile` |

```groovy
pipeline {
    agent none
    options {
        timeout(time: 30, unit: 'MINUTES')
    }
    stages {
        stage('Polyglot Build') {
            parallel {
                stage('Node.js') {
                    agent {
                        docker {
                            image 'node:24-bookworm-slim'
                            label 'linux && docker'
                        }
                    }
                    steps {
                        dir('web') {
                            configFileProvider([configFile(fileId: 'npmrc-nexus', targetLocation: '.npmrc')]) {
                                sh 'npm ci && npm run lint && npm test -- --ci --reporters=default --reporters=jest-junit'
                            }
                        }
                    }
                    post {
                        always {
                            junit testResults: 'web/junit.xml', allowEmptyResults: true
                        }
                    }
                }
                stage('Python') {
                    agent {
                        docker {
                            image 'python:3.13-slim'
                            label 'linux && docker'
                        }
                    }
                    environment {
                        PIP_INDEX_URL = 'https://nexus.example.internal/repository/pypi-proxy/simple'
                        PIP_DISABLE_PIP_VERSION_CHECK = '1'
                    }
                    steps {
                        dir('analytics') {
                            sh '''
                                python -m venv .venv
                                . .venv/bin/activate
                                pip install -r requirements.txt -r requirements-dev.txt
                                pytest --junitxml=reports/pytest.xml --cov=src --cov-report=xml:reports/coverage.xml
                            '''
                        }
                    }
                    post {
                        always {
                            junit testResults: 'analytics/reports/pytest.xml', allowEmptyResults: true
                            recordCoverage(tools: [[parser: 'COBERTURA', pattern: 'analytics/reports/coverage.xml']], id: 'python-coverage', name: 'Python 覆蓋率')
                        }
                    }
                }
                stage('.NET') {
                    agent {
                        docker {
                            image 'mcr.microsoft.com/dotnet/sdk:10.0'
                            label 'linux && docker'
                        }
                    }
                    environment {
                        DOTNET_CLI_TELEMETRY_OPTOUT = '1'
                        DOTNET_NOLOGO = '1'
                    }
                    steps {
                        dir('billing-service') {
                            sh '''
                                dotnet restore --configfile nuget.config
                                dotnet build -c Release --no-restore
                                dotnet test -c Release --no-build --logger "junit;LogFilePath=TestResults/junit.xml"
                            '''
                        }
                    }
                    post {
                        always {
                            junit testResults: 'billing-service/**/TestResults/junit.xml', allowEmptyResults: true
                        }
                    }
                }
                stage('Go') {
                    agent {
                        docker {
                            image 'golang:1.26-bookworm'
                            label 'linux && docker'
                        }
                    }
                    environment {
                        GOPROXY = 'https://nexus.example.internal/repository/go-proxy/,direct'
                        GOFLAGS = '-mod=readonly'
                    }
                    steps {
                        dir('gateway') {
                            sh '''
                                go vet ./...
                                go run gotest.tools/gotestsum@v1.13.0 --junitfile reports/junit.xml -- -race -coverprofile=reports/cover.out ./...
                            '''
                        }
                    }
                    post {
                        always {
                            junit testResults: 'gateway/reports/junit.xml', allowEmptyResults: true
                            recordCoverage(tools: [[parser: 'GO_COV', pattern: 'gateway/reports/cover.out']], id: 'go-coverage', name: 'Go 覆蓋率')
                        }
                    }
                }
            }
        }
    }
}
```

> 💡 `configFileProvider` 的 `targetLocation` 會把 `.npmrc` 寫入目前目錄，建置結束後自動刪除；`.npmrc` 中的 token 可透過 Config File Provider 的憑證對應填入，不必寫在 repository。Windows 原生的 .NET Framework 專案則需要 Windows agent（`agent { label 'windows && msbuild' }`）與 `bat`／`powershell` step。

### 9.8 本章重點

- 優先使用容器化 agent 與 Wrapper 固定工具版本；Global Tools 只用於固定 agent
- `settings.xml` 以 Config File Provider 管理，帳密以 `serverCredentialMappings` 注入
- Maven 使用 `-B -ntp verify`，測試結果交給 `junit` step 判定 UNSTABLE
- 快取要依信任等級分隔，正式發佈不與不受信任的 PR 共用快取

## 10. Declarative Pipeline 完整語法

### 10.1 結構總覽

Declarative Pipeline 是 Jenkins 官方建議的 Pipeline 寫法：結構固定、可在執行前驗證、支援從指定 stage 重新執行（Restart from Stage）。以下骨架列出所有區段（directive），實務上只需要其中一部分：

```groovy
pipeline {
    agent none                       // 必填：pipeline 層級的執行環境
    environment {                    // 環境變數
        APP_NAME = 'payment-api'
    }
    options {                        // 執行選項
        timeout(time: 1, unit: 'HOURS')
    }
    parameters {                     // 建置參數
        booleanParam(name: 'SKIP_IT', defaultValue: false, description: '略過整合測試')
    }
    triggers {                       // 觸發條件
        cron('H 2 * * 1-5')
    }
    stages {
        stage('Build') {
            agent { label 'linux' }  // stage 層級 agent
            environment {            // stage 層級環境變數
                MAVEN_OPTS = '-Xmx1g'
            }
            options {                // stage 層級選項
                timeout(time: 20, unit: 'MINUTES')
            }
            when {                   // 執行條件
                not { expression { params.SKIP_IT } }
            }
            steps {
                echo "Building ${APP_NAME}"
            }
            post {                   // stage 結束後動作
                always {
                    echo 'stage 結束'
                }
            }
        }
    }
    post {                           // pipeline 結束後動作
        failure {
            echo '建置失敗'
        }
    }
}
```

| 區段 | Pipeline 層級 | Stage 層級 | 說明 |
| --- | --- | --- | --- |
| `agent` | 必填 | 選填 | `agent none` 表示由各 stage 自行指定 |
| `environment` | ✅ | ✅ | |
| `options` | ✅ | ✅（部分選項） | 見 10.4 |
| `parameters` | ✅ | ❌ | |
| `triggers` | ✅ | ❌ | Multibranch 通常不需要 |
| `tools` | ✅ | ✅ | 需要 Global Tool Configuration |
| `input` | ❌ | ✅ | 見 10.9 |
| `when` | ❌ | ✅ | 見 10.6 |
| `steps`／`stages`／`parallel`／`matrix` | — | 四擇一 | 一個 stage 只能有其中一種 |
| `post` | ✅ | ✅ | 見 10.10 |

### 10.2 agent

| 寫法 | 說明 |
| --- | --- |
| `agent any` | 任一可用 agent。⚠️ 若 built-in node 有 executor，可能在 controller 執行；正式環境建議改用 label |
| `agent none` | Pipeline 層級不配置 agent，各 stage 自行指定；`input` 等待期間不會占用 executor |
| `agent { label 'linux && docker' }` | 以 label 表達式選擇（支援 `&&`、`\|\|`、`!`） |
| `agent { node { label 'linux'; customWorkspace '/data/ws/payment' } }` | 指定 workspace 路徑 |
| `agent { docker { image '...'; label '...'; args '...' } }` | 在具備 Docker 的 agent 上，以容器執行 steps（Docker Pipeline plugin） |
| `agent { dockerfile { filename 'ci/Dockerfile'; dir '.' } }` | 先以 repository 中的 Dockerfile 建立映像再執行 |
| `agent { kubernetes { yaml '...'; defaultContainer 'maven' } }` | 動態建立 Pod（Kubernetes plugin，[14.4 Kubernetes plugin](#144-kubernetes-plugin)） |

**stage 層級 agent 與 `reuseNode`**：

```groovy
pipeline {
    agent { label 'linux && docker' }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'maven:3.9.16-eclipse-temurin-21'
                    reuseNode true      // 在 pipeline 層級配置的同一個 agent 與 workspace 上啟動容器
                }
            }
            steps {
                sh 'mvn -B -ntp package -DskipTests'
            }
        }
        stage('Scan') {
            agent {
                docker {
                    image 'aquasec/trivy:0.75.0'
                    args '--entrypoint=""'
                    reuseNode true
                }
            }
            steps {
                sh 'trivy fs --exit-code 0 --format table .'
            }
        }
    }
}
```

> 💡 沒有 `reuseNode true` 時，stage 層級的 docker agent 會另外配置 executor 與 workspace，前一個 stage 的產出不會出現在新的 workspace 中，需要 `stash`／`unstash` 傳遞。

### 10.3 environment 與字串內插

```groovy
pipeline {
    agent { label 'linux' }
    environment {
        APP_NAME     = 'payment-api'                         // 字串常數
        IMAGE_REPO   = "harbor.example.internal/payments/${APP_NAME}"   // 可引用先前定義的變數
        GIT_SHORT    = "${env.GIT_COMMIT?.take(8) ?: 'local'}"
        NEXUS        = credentials('nexus-deployer-payments')  // 函式呼叫
    }
    stages {
        stage('Info') {
            steps {
                // Groovy 雙引號：由 Groovy 內插（適合非機密值）
                echo "Image: ${IMAGE_REPO}:${GIT_SHORT}"
                // 單引號：交給 shell 展開（機密與使用者輸入一律使用這種寫法）
                sh 'echo "Deploying $APP_NAME as $NEXUS_USR"'
                script {
                    // 執行期間計算的值，以 env.X 指派
                    env.BUILD_TS = new Date().format('yyyyMMddHHmm', TimeZone.getTimeZone('Asia/Taipei'))
                }
                sh 'echo "Build timestamp: $BUILD_TS"'
            }
        }
    }
}
```

| 規則 | 說明 |
| --- | --- |
| `environment` 的值 | 只能是字串（單／雙引號）或函式呼叫；❌ 不能是變數名稱、三元運算式或多行運算式（v1.0 第 10 章的 `APP_NAME = config.appName` 即因此驗證失敗） |
| 複雜計算 | 放在 `script {}` 中，以 `env.NAME = ...` 指派 |
| `env.X` 的型別 | 一律是字串；`env.FLAG = false` 之後 `if (env.FLAG)` 會是 true（非空字串），請比較 `env.FLAG == 'true'` |
| 常用內建變數 | `BUILD_NUMBER`、`BUILD_URL`、`JOB_NAME`、`WORKSPACE`、`BRANCH_NAME`、`CHANGE_ID`（PR 編號）、`CHANGE_TARGET`、`TAG_NAME`、`GIT_COMMIT`、`NODE_NAME`；完整清單在 `<Jenkins URL>/env-vars.html` |

> ⚠️ **Shell 注入**：`sh "deploy.sh ${params.TARGET}"` 會讓 Groovy 先把使用者輸入拼進指令。Declarative 會把參數同時設為環境變數，請寫成 `sh 'deploy.sh "$TARGET"'`。

### 10.4 options

| 選項 | 層級 | 用途 |
| --- | --- | --- |
| `buildDiscarder(logRotator(numToKeepStr: '30', daysToKeepStr: '30', artifactNumToKeepStr: '5'))` | Pipeline | 建置保留政策 |
| `disableConcurrentBuilds(abortPrevious: true)` | Pipeline | 同一分支有新建置時中止舊建置（PR 建置適用）；不加參數則排隊等待 |
| `timeout(time: 30, unit: 'MINUTES')` | 兩者 | 逾時中止；stage 層級可細分 |
| `retry(count: 2, conditions: [agent(), nonresumable()])` | 兩者 | 只在 agent 中斷或 controller 重啟後無法恢復時重試，**不重試一般失敗** |
| `timestamps()` | 兩者 | 主控台加上時間戳記（Timestamper） |
| `ansiColor('xterm')` | 兩者 | 顯示 ANSI 顏色（AnsiColor plugin） |
| `skipDefaultCheckout()` | 兩者 | 不自動 checkout |
| `skipStagesAfterUnstable()` | Pipeline | 測試失敗（UNSTABLE）後略過後續 stage |
| `parallelsAlwaysFailFast()` | Pipeline | 所有 `parallel` 預設 fail-fast |
| `preserveStashes(buildCount: 5)` | Pipeline | 保留 stash 供 Restart from Stage 使用 |
| `durabilityHint('PERFORMANCE_OPTIMIZED')` | Pipeline | 降低 I/O（[11.4 Durability 與效能設定](#114-durability-與效能設定)） |
| `quietPeriod(10)` | Pipeline | 觸發後等待秒數 |
| `checkoutToSubdirectory('src')` | Pipeline | checkout 到子目錄 |
| `newContainerPerStage()` | Pipeline | 搭配 docker agent，每個 stage 使用新容器 |
| `lock('sit-env')` | 兩者 | 鎖定共用資源（[11.5 資源鎖定與 milestone](#115-資源鎖定與-milestone)） |
| `disableResume()` | Pipeline | controller 重啟後不恢復（避免重複部署） |

### 10.5 parameters 與 triggers

```groovy
pipeline {
    agent { label 'linux' }
    parameters {
        choice(name: 'TARGET_ENV', choices: ['sit', 'uat'], description: '部署環境（第一個為預設值）')
        string(name: 'IMAGE_TAG', defaultValue: '', description: '要部署的映像 tag，空白表示使用本次建置')
        booleanParam(name: 'RUN_PERF_TESTS', defaultValue: false, description: '是否執行效能測試')
        text(name: 'RELEASE_NOTE', defaultValue: '', description: '版本說明')
        password(name: 'NOT_RECOMMENDED', defaultValue: '', description: '❌ 示範用途：請改用 Credentials')
    }
    triggers {
        cron('TZ=Asia/Taipei\nH 2 * * 1-5')
        upstream(upstreamProjects: 'payments/payment-lib/main', threshold: hudson.model.Result.SUCCESS)
    }
    stages {
        stage('Show') {
            steps {
                echo "TARGET_ENV=${params.TARGET_ENV}, RUN_PERF_TESTS=${params.RUN_PERF_TESTS}"
            }
        }
    }
}
```

> ⚠️ 參數與觸發條件會在 Pipeline **第一次執行後**才寫入 Job 設定。新建的 Job 第一次建置不會顯示參數畫面，且使用預設值。Multibranch 的每個分支都會套用 Jenkinsfile 中的 `triggers`，請以 `when` 或分支判斷避免所有 feature 分支都排程執行。

### 10.6 when 條件

| 條件 | 範例 | 說明 |
| --- | --- | --- |
| `branch` | `branch 'main'`、`branch pattern: 'release/.*', comparator: 'REGEXP'` | 只適用 Multibranch |
| `buildingTag()` | `buildingTag()` | 正在建置 tag |
| `tag` | `tag 'v*'`、`tag pattern: 'v\\d+.*', comparator: 'REGEXP'` | 建置符合的 tag |
| `changeRequest()` | `changeRequest target: 'main'` | PR／MR 建置 |
| `changeset` | `changeset 'services/payment/**'` | 本次變更包含符合的檔案 |
| `changelog` | `changelog '.*\\[skip-it\\].*'` | commit 訊息符合 |
| `environment` | `environment name: 'DEPLOY_ENV', value: 'sit'` | 環境變數等於某值 |
| `equals` | `equals expected: 'uat', actual: params.TARGET_ENV` | 兩值相等 |
| `expression` | `expression { params.RUN_PERF_TESTS }` | 任意 Groovy 布林運算式 |
| `triggeredBy` | `triggeredBy 'TimerTrigger'`、`triggeredBy cause: 'UserIdCause'` | 依觸發原因 |
| `not`／`allOf`／`anyOf` | `allOf { branch 'main'; not { changeRequest() } }` | 組合條件 |
| `beforeAgent true` | | 先判斷條件再配置 agent（✅ 節省資源） |
| `beforeInput true` | | 先判斷條件再顯示 input |
| `beforeOptions true` | | 先判斷條件再套用 stage options（例如 lock、timeout） |

```groovy
pipeline {
    agent none
    parameters {
        booleanParam(name: 'RUN_PERF_TESTS', defaultValue: false, description: '是否執行效能測試')
    }
    stages {
        stage('Perf Test') {
            agent { label 'perf' }
            when {
                beforeAgent true
                anyOf {
                    branch 'main'
                    expression { params.RUN_PERF_TESTS }   // ✅ 布林參數必須包在 expression 中
                }
            }
            steps {
                sh './run-perf.sh'
            }
        }
        stage('Deploy SIT') {
            agent { label 'deploy' }
            when {
                beforeAgent true
                allOf {
                    branch 'main'
                    not { changeRequest() }
                    triggeredBy cause: 'UserIdCause'
                }
            }
            steps {
                echo '僅在 main 分支且由使用者手動觸發時部署'
            }
        }
    }
}
```

> 📌 **v1.0 最常見的錯誤**：在 `when` 中直接寫 `params.RUN_PERF_TESTS` 或 `params.ENABLE_PROFILING`。Declarative 只接受上表中的條件，裸露的布林運算式會產生「Expected a when condition」錯誤，Pipeline 根本無法啟動。v1.0 有 8 個範例、共 22 處犯了此錯誤（以 2.580.1 的驗證端點逐一確認）。

### 10.7 parallel 與循序 stages

```groovy
pipeline {
    agent none
    options {
        parallelsAlwaysFailFast()
    }
    stages {
        stage('Verify') {
            parallel {
                stage('Unit Test') {
                    agent { label 'linux' }
                    steps {
                        sh './mvnw -B -ntp test'
                    }
                }
                stage('Static Analysis') {
                    agent { label 'linux' }
                    steps {
                        sh './mvnw -B -ntp -DskipTests spotbugs:check checkstyle:check'
                    }
                }
                stage('Frontend') {
                    agent { label 'linux && node' }
                    stages {                      // 平行分支內的循序 stages
                        stage('Install') {
                            steps {
                                sh 'npm ci'
                            }
                        }
                        stage('Test') {
                            steps {
                                sh 'npm test -- --ci'
                            }
                        }
                    }
                }
            }
        }
    }
}
```

| 規則 | 說明 |
| --- | --- |
| 巢狀限制 | `parallel` 內的 stage 不能再有 `parallel`（可以有循序 `stages`） |
| Fail-fast | `failFast true`（單一 parallel）或 `parallelsAlwaysFailFast()`（全域）：任一分支失敗即中止其他分支 |
| 資源 | 每個分支各自配置 agent；分支數量不要超過 agent 容量，否則只會在佇列等待 |

### 10.8 matrix

`matrix` 以多個軸（axis）的組合產生平行 stage，取代舊的 Multi-configuration project：

```groovy
pipeline {
    agent none
    stages {
        stage('Compatibility') {
            matrix {
                axes {
                    axis {
                        name 'JDK'
                        values '17', '21', '25'
                    }
                    axis {
                        name 'DB'
                        values 'postgres16', 'oracle19c'
                    }
                }
                excludes {
                    exclude {
                        axis {
                            name 'JDK'
                            values '25'
                        }
                        axis {
                            name 'DB'
                            values 'oracle19c'
                        }
                    }
                }
                agent {
                    docker {
                        image "maven:3.9.16-eclipse-temurin-${JDK}"
                        label 'linux && docker'
                    }
                }
                stages {
                    stage('Test') {
                        steps {
                            sh 'mvn -B -ntp verify -Pit-${DB}'
                        }
                    }
                }
            }
        }
    }
}
```

> 💡 軸的值會成為環境變數（`$JDK`、`$DB`）。在 `docker.image` 這類需要 Groovy 求值的位置用雙引號內插；在 `sh` 中用單引號讓 shell 展開。

### 10.9 input（人工核准）

```groovy
pipeline {
    agent none
    stages {
        stage('Deploy PROD') {
            agent { label 'deploy-prod' }
            when {
                beforeAgent true
                beforeInput true
                buildingTag()
            }
            input {
                message '確認部署到正式環境？'
                ok '部署'
                submitter 'payments-release-managers'   // 群組或使用者 ID，逗號分隔
                submitterParameter 'APPROVER'           // 核准人 ID 寫入此變數
                parameters {
                    string(name: 'CHANGE_TICKET', defaultValue: '', description: '變更單號（必填）')
                }
            }
            steps {
                echo "核准人：${APPROVER}，變更單：${CHANGE_TICKET}"
            }
        }
    }
}
```

> ⚠️ stage 層級的 `input` 會在**配置 agent 之前**等待，因此不占用 executor。若在 `steps` 中呼叫 `input` step，等待期間會一直占用 agent。務必搭配 `options { timeout(...) }` 避免建置永遠等待（[16.2 人工核准與職責分離](#162-人工核准與職責分離)）。

### 10.10 post 與建置結果

| 條件 | 執行時機 |
| --- | --- |
| `always` | 無論結果都執行 |
| `success`／`failure`／`unstable`／`aborted` | 對應結果 |
| `changed` | 結果與上一次不同 |
| `fixed` | 上一次失敗或不穩定，本次成功 |
| `regression` | 上一次成功，本次失敗、不穩定或中止 |
| `unsuccessful` | 結果不是 SUCCESS |
| `notBuilt` | 結果為 NOT_BUILT |
| `cleanup` | 所有其他 post 條件之後，最後執行（清理 workspace、刪除暫存資源） |

| 結果 | 意義 | 設定方式 |
| --- | --- | --- |
| SUCCESS | 成功 | |
| UNSTABLE | 建置完成但品質未達標（測試失敗、品質門檻） | `junit` 有失敗的測試、`unstable('原因')`、品質門檻 |
| FAILURE | 建置失敗 | 指令結束碼非 0、`error('原因')` |
| ABORTED | 被中止 | 使用者中止、`timeout`、新建置中止舊建置 |
| NOT_BUILT | 未建置 | stage 因 `when` 被略過 |

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Test') {
            steps {
                sh './mvnw -B -ntp verify'
            }
        }
    }
    post {
        always {
            junit testResults: '**/target/surefire-reports/*.xml', allowEmptyResults: true
        }
        fixed {
            echo "建置已恢復：${env.BUILD_URL}"
        }
        regression {
            echo "建置轉為失敗，通知最近提交者"
        }
        cleanup {
            cleanWs(deleteDirs: true, notFailBuild: true)
        }
    }
}
```

### 10.11 script 區塊與 Declarative 的限制

`script {}` 可以在 `steps` 中撰寫 Scripted 語法（迴圈、條件、變數、呼叫 Shared Library 的類別），但：

| 限制 | 說明 | 對策 |
| --- | --- | --- |
| 方法過大 | 整個 Pipeline 會被編譯成一個 Groovy 方法，超過 JVM 64 KB 上限會出現「Method code too large」 | 把邏輯搬到 Shared Library（第 12 章） |
| `script` 過多 | Declarative 的可讀性與可驗證性下降 | 單一 `script` 區塊超過 15 行即應考慮抽到 Library |
| 不能直接寫 Groovy 宣告 | 在 `pipeline {}` 外可以 `def` 函式，但會受沙箱與 CPS 限制 | 只放極簡單的輔助函式 |
| 驗證 | Declarative 驗證不會檢查 `script` 內容的語意 | 以 Replay 或單元測試驗證（[11.7 Pipeline 開發工具](#117-pipeline-開發工具)） |

### 10.12 完整範例：Spring Boot 服務 Pipeline

以下範例整合本章內容，適用 Multibranch：PR 只做建置、測試、品質檢查；`main` 推送映像並部署 SIT；`v*` tag 經核准後部署正式環境。映像建置、品質門檻、部署細節分別見第 13、15、16 章。

```groovy
pipeline {
    agent none
    options {
        buildDiscarder(logRotator(numToKeepStr: '50', artifactNumToKeepStr: '5'))
        disableConcurrentBuilds(abortPrevious: true)
        timeout(time: 60, unit: 'MINUTES')
        timestamps()
        skipStagesAfterUnstable()
    }
    environment {
        APP_NAME   = 'payment-api'
        REGISTRY   = 'harbor.example.internal'
        IMAGE_REPO = "${REGISTRY}/payments/${APP_NAME}"
    }
    stages {
        stage('Build & Test') {
            agent {
                docker {
                    image 'maven:3.9.16-eclipse-temurin-21'
                    label 'linux && docker'
                    args '-v maven-repo-cache:/root/.m2/repository'
                }
            }
            steps {
                configFileProvider([configFile(fileId: 'maven-settings-nexus', variable: 'MAVEN_SETTINGS')]) {
                    sh 'mvn -B -ntp -s "$MAVEN_SETTINGS" clean verify'
                }
                stash name: 'app-jar', includes: 'target/*.jar'
            }
            post {
                always {
                    junit testResults: 'target/surefire-reports/*.xml', allowEmptyResults: true
                    recordCoverage(tools: [[parser: 'JACOCO', pattern: 'target/site/jacoco/jacoco.xml']],
                                   qualityGates: [[threshold: 70.0, metric: 'LINE', baseline: 'PROJECT', criticality: 'UNSTABLE']])
                    recordIssues(tools: [spotBugs(pattern: 'target/spotbugsXml.xml'),
                                         checkStyle(pattern: 'target/checkstyle-result.xml')],
                                 qualityGates: [[threshold: 1, type: 'NEW', criticality: 'UNSTABLE']])
                }
            }
        }
        stage('Image') {
            when {
                beforeAgent true
                anyOf {
                    branch 'main'
                    buildingTag()
                }
            }
            agent {
                kubernetes {
                    yamlFile 'ci/buildkit-pod.yaml'
                    defaultContainer 'buildkit'
                }
            }
            steps {
                unstash 'app-jar'
                script {
                    env.IMAGE_TAG = env.TAG_NAME ?: "${env.BUILD_NUMBER}-${env.GIT_COMMIT.take(8)}"
                }
                withCredentials([usernamePassword(credentialsId: 'harbor-robot-payments',
                                                  usernameVariable: 'REG_USER', passwordVariable: 'REG_PASS')]) {
                    sh '''
                        set -eu
                        mkdir -p ~/.docker
                        AUTH=$(printf '%s:%s' "$REG_USER" "$REG_PASS" | base64 | tr -d '\\n')
                        printf '{"auths":{"%s":{"auth":"%s"}}}' "$REGISTRY" "$AUTH" > ~/.docker/config.json
                        buildctl-daemonless.sh build \
                          --frontend dockerfile.v0 --local context=. --local dockerfile=. \
                          --output type=image,name="$IMAGE_REPO:$IMAGE_TAG",push=true
                    '''
                }
            }
        }
        stage('Deploy SIT') {
            when {
                beforeAgent true
                branch 'main'
            }
            agent { label 'deploy' }
            options {
                lock(resource: 'payments-sit')
            }
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-sit-payments', variable: 'KUBECONFIG')]) {
                    sh 'helm upgrade --install "$APP_NAME" ./chart -n payments-sit --set image.tag="$IMAGE_TAG" --wait --timeout 10m'
                }
            }
        }
        stage('Deploy PROD') {
            when {
                beforeAgent true
                beforeInput true
                tag pattern: 'v\\d+\\.\\d+\\.\\d+', comparator: 'REGEXP'
            }
            options {
                timeout(time: 2, unit: 'HOURS')
            }
            input {
                message '部署到正式環境？'
                ok '部署'
                submitter 'payments-release-managers'
                submitterParameter 'APPROVER'
            }
            agent { label 'deploy-prod' }
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-prod-payments', variable: 'KUBECONFIG')]) {
                    sh 'helm upgrade --install "$APP_NAME" ./chart -n payments-prod --set image.tag="$IMAGE_TAG" --wait --timeout 15m'
                }
                echo "核准人：${APPROVER}"
            }
        }
    }
    post {
        failure {
            emailext to: 'team-payments@example.internal',
                     subject: "[FAILED] ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "建置失敗：${env.BUILD_URL}console"
        }
    }
}
```

> 💡 範例中 `IMAGE_TAG` 在 `Image` stage 以 `env.IMAGE_TAG` 設定後，後續 stage（即使在不同 agent）都可讀取。`ci/buildkit-pod.yaml` 見 [15.2 BuildKit rootless（Kubernetes agent）](#152-buildkit-rootlesskubernetes-agent)。

### 10.13 本章重點

- `when` 只接受內建條件，布林運算式必須包在 `expression {}` 中；加上 `beforeAgent true` 節省資源
- `environment` 的值只能是字串或函式呼叫，複雜計算放在 `script {}` 並以 `env.X` 指派
- 機密與使用者輸入一律以單引號字串交給 shell 展開
- 人工核准使用 stage 層級 `input` 搭配 `timeout`，不占用 executor
- 本章所有範例皆已通過 Jenkins 2.580.1 的 Declarative 驗證

## 11. Scripted Pipeline、CPS 與進階模式

### 11.1 Scripted Pipeline 語法

Scripted Pipeline 是以 `node` 為起點的 Groovy 程式，彈性最高，但沒有 Declarative 的結構驗證、`post`、`when`、Restart from Stage 等功能。

| 比較 | Declarative | Scripted |
| --- | --- | --- |
| 結構 | 固定區段，執行前驗證 | 任意 Groovy 程式 |
| 學習門檻 | 低 | 需要 Groovy 與 CPS 知識 |
| 錯誤處理 | `post` 條件 | `try`／`catch`／`finally` |
| Restart from Stage | ✅ | ❌ |
| 建議用途 | ✅ 應用程式 Pipeline 的標準寫法 | Shared Library 內部實作、高度動態的流程（例如依設定檔產生 stage） |

```groovy
// Scripted Pipeline：依 services.yaml 動態產生平行建置
node('linux') {
    stage('Checkout') {
        checkout scm
    }

    def services = []
    stage('Plan') {
        def cfg = readYaml file: 'services.yaml'
        services = cfg.services.findAll { it.enabled }.collect { it.name }
        echo "本次建置：${services}"
    }

    stage('Build') {
        def branches = [:]
        for (svc in services) {
            def name = svc   // 迴圈變數必須先複製，否則所有閉包都會拿到最後一個值
            branches[name] = {
                node('linux && docker') {
                    checkout scm
                    dir("services/${name}") {
                        sh './mvnw -B -ntp verify'
                    }
                }
            }
        }
        branches.failFast = true
        parallel branches
    }
}
```

**Scripted 的錯誤處理**：

```groovy
node('linux') {
    try {
        stage('Test') {
            checkout scm
            sh './mvnw -B -ntp verify'
        }
        currentBuild.result = 'SUCCESS'
    } catch (org.jenkinsci.plugins.workflow.steps.FlowInterruptedException e) {
        // 使用者中止或 timeout：不要吞掉，保留 ABORTED 狀態
        currentBuild.result = 'ABORTED'
        throw e
    } catch (err) {
        currentBuild.result = 'FAILURE'
        throw err
    } finally {
        junit testResults: '**/target/surefire-reports/*.xml', allowEmptyResults: true
        cleanWs(notFailBuild: true)
    }
}
```

> ⚠️ `catch (err)` 若沒有重新拋出，使用者按下「中止」或 `timeout` 觸發時建置仍會繼續執行，甚至顯示為成功。一定要先處理 `FlowInterruptedException` 並重新拋出。

### 11.2 CPS 限制與 @NonCPS

Pipeline 的 Groovy 程式碼經過 CPS 轉換，以便在任何一個 step 之間暫停、序列化並在 controller 重啟後恢復。這帶來以下限制：

| 限制 | 症狀 | 對策 |
| --- | --- | --- |
| **不可序列化的物件跨越 step** | `java.io.NotSerializableException: java.util.regex.Matcher` | 在 `@NonCPS` 方法中處理，或把物件設為區域變數並在 step 之前釋放（`m = null`） |
| **CPS 與非 CPS 方法互相呼叫** | 記錄出現「expected to call ... but wound up catching ...」，結果錯誤 | 傳給 Java／Groovy 內建方法的閉包（例如 `sort { a, b -> }`、`toSorted`）放到 `@NonCPS` 方法中 |
| **`@NonCPS` 方法不能呼叫 step** | 在 `@NonCPS` 方法中呼叫 `sh`、`echo` 會失敗或行為異常 | `@NonCPS` 只做純運算，回傳結果後再由一般方法呼叫 step |
| **效能** | 大量迴圈、字串處理使 controller CPU 飆高 | 把資料處理交給 agent 上的腳本（`sh 'python3 parse.py'`） |

```groovy
// ✅ 正確：@NonCPS 只做純運算，不呼叫任何 step
@NonCPS
def parseVersion(String text) {
    def m = (text =~ /version\s*=\s*"([^"]+)"/)
    return m.find() ? m.group(1) : null
}

@NonCPS
def sortByPriority(List<Map> items) {
    return items.sort(false) { a, b -> a.priority <=> b.priority }
}

node('linux') {
    checkout scm
    def text = readFile 'gradle.properties'
    def version = parseVersion(text)
    echo "版本：${version}"
    def ordered = sortByPriority(readYaml(file: 'deploy-order.yaml').targets)
    for (t in ordered) {
        echo "部署 ${t.name}"
    }
}
```

### 11.3 Script Security 沙箱與 Script Approval

所有使用者撰寫的 Pipeline（Jenkinsfile、非受信任的 Shared Library）都在 **Groovy 沙箱**中執行，只能呼叫白名單中的方法。呼叫未核准的方法時建置會失敗，並在 Manage Jenkins → In-process Script Approval 出現待核准項目。

| 原則 | 說明 |
| --- | --- |
| 預設拒絕 | 能用 Pipeline step 完成的事（`readJSON`、`readYaml`、`writeFile`、`httpRequest`）就不要核准對應的 Java API |
| 高風險方法一律拒絕 | `java.lang.Runtime.exec`、`java.io.File`、`groovy.lang.GroovyShell`、`jenkins.model.Jenkins.get`、`hudson.model.*` 的寫入方法、反射相關方法，核准後等同讓所有 Pipeline 作者取得 controller 權限 |
| 集中審查 | Script Approval 只有管理員能操作，核准前需有第二人覆核並記錄原因 |
| 改用受信任的 Library | 確實需要特權操作時，封裝在**受信任的全域 Shared Library**（不在沙箱中執行）並嚴格控管該 repository 的寫入權限（[12.2 設定 Library：受信任與非受信任](#122-設定-library受信任與非受信任)） |

> ⚠️ 受信任的全域 Shared Library 等同 controller 上的管理員程式碼。對該 repository 有寫入權限的人，實際上就擁有 Jenkins 管理員權限。

### 11.4 Durability 與效能設定

| Durability 等級 | 行為 | 適用 |
| --- | --- | --- |
| `MAX_SURVIVABILITY`（預設） | 每個 step 後同步寫入狀態，controller 意外停止也能恢復 | 正式部署 Pipeline |
| `SURVIVABLE_NONATOMIC` | 每個 step 後寫入但不保證原子性 | 一般建置 |
| `PERFORMANCE_OPTIMIZED` | 只在 Pipeline 結束或正常關機時寫入，I/O 大幅降低；controller 異常停止時執行中的建置無法恢復 | ✅ 大部分 CI 建置（可重跑） |

設定方式：

- 全域：Manage Jenkins → System → Pipeline Speed/Durability Settings
- 單一 Pipeline：`options { durabilityHint('PERFORMANCE_OPTIMIZED') }`
- Multibranch：分支屬性策略中的「Pipeline branch speed/durability override」

**其他效能要點**：

| 問題 | 改善方式 |
| --- | --- |
| 主控台記錄過大（單次數百 MB） | Maven 加 `-ntp`、測試輸出導向檔案、移除 `set -x` |
| 大量短 `sh` step | 合併成一個 `sh '''...'''` 腳本；每個 step 都有 controller 往返與狀態寫入成本 |
| `readFile`／`readJSON` 讀取大檔 | 在 agent 上以 `jq`、`python3` 處理，只把結果傳回 |
| 數百個平行分支 | 以 `matrix` 或分批執行，平行數不超過 agent 容量 |
| 大型 `stash` | 改推送至 artifact 儲存庫 |

### 11.5 資源鎖定與 milestone

**Lockable Resources**：確保同一時間只有一個建置使用共用的測試環境、裝置或授權：

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Integration Test') {
            options {
                // 從標記為 sit-env 的資源池中取得一個，資源名稱寫入 LOCKED_ENV
                lock(label: 'sit-env', quantity: 1, variable: 'LOCKED_ENV')
            }
            steps {
                sh 'echo "使用環境：$LOCKED_ENV" && ./run-it.sh "$LOCKED_ENV"'
            }
        }
        stage('Deploy UAT') {
            steps {
                // inversePrecedence：較新的建置優先取得鎖
                lock(resource: 'payments-uat', inversePrecedence: true) {
                    milestone(ordinal: 10, label: 'deploy-uat')
                    sh './deploy.sh uat'
                }
            }
        }
    }
}
```

**Milestone**：較新的建置通過某個 milestone 後，尚未通過該 milestone 的較舊建置會被自動中止，避免舊版本在新版本之後部署。常與 `lock(inversePrecedence: true)` 和 `input` 搭配使用。

```mermaid
sequenceDiagram
    participant B10 as 建置 #10
    participant B11 as 建置 #11
    participant L as lock: payments-uat
    B10->>L: 取得鎖，開始部署
    B11->>L: 等待鎖
    B10->>B10: 通過 milestone 10
    B10-->>L: 釋放鎖
    B11->>L: 取得鎖
    B11->>B11: 通過 milestone 10
```

若較新的 #11 先通過 milestone 10，而 #10 尚未通過，#10 會被自動中止。

### 11.6 錯誤處理模式

| Step | 用途 | 範例 |
| --- | --- | --- |
| `catchError` | 捕捉錯誤並設定建置與 stage 結果，Pipeline 繼續執行 | `catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') { sh './flaky-check.sh' }` |
| `warnError` | 錯誤時把建置與 stage 設為 UNSTABLE 並繼續 | `warnError('lint 失敗') { sh 'npm run lint' }` |
| `unstable` | 主動把建置設為 UNSTABLE | `unstable('覆蓋率下降')` |
| `error` | 主動讓建置失敗 | `error('缺少變更單號')` |
| `retry` | 重試區塊 | `retry(count: 3) { sh './download-deps.sh' }` |
| `timeout` | 限制區塊執行時間 | `timeout(time: 5, unit: 'MINUTES') { ... }` |
| `sh returnStatus: true` | 取得結束碼而不拋錯 | `def rc = sh(script: './check.sh', returnStatus: true)` |
| `sh returnStdout: true` | 取得輸出（記得 `.trim()`） | `def sha = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()` |

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Optional Checks') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE', message: '授權檢查失敗，不影響建置') {
                    sh './license-check.sh'
                }
                script {
                    def rc = sh(script: './api-compat-check.sh', returnStatus: true)
                    if (rc == 2) {
                        unstable('API 相容性有警告')
                    } else if (rc != 0) {
                        error("API 相容性檢查失敗，結束碼 ${rc}")
                    }
                }
            }
        }
        stage('Download') {
            steps {
                retry(count: 3) {
                    timeout(time: 2, unit: 'MINUTES') {
                        sh 'curl -fsSLo tool.tgz https://nexus.example.internal/repository/tools/tool-1.2.3.tgz'
                    }
                }
            }
        }
    }
}
```

> ⚠️ `retry` 只適合處理暫時性的外部錯誤（網路、下載）。對測試或建置步驟使用 `retry` 會掩蓋不穩定的測試（flaky test），應修正根本原因。

### 11.7 Pipeline 開發工具

| 工具 | 位置 | 用途 |
| --- | --- | --- |
| **Snippet Generator** | Job 頁面 → Pipeline Syntax（`/pipeline-syntax`） | 以表單產生任一 step 的正確語法 |
| **Declarative Directive Generator** | 同上，切換分頁 | 產生 `options`、`when`、`agent` 等區段 |
| **Steps Reference** | `<Jenkins URL>/pipeline-syntax/html`、[jenkins.io/doc/pipeline/steps](https://www.jenkins.io/doc/pipeline/steps/) | 已安裝 plugin 的完整 step 參考 |
| **Replay** | 建置頁面 → Replay | 修改這次建置使用的 Jenkinsfile／Library 後重新執行，不需提交 |
| **Restart from Stage** | 建置頁面（Declarative） | 從指定 stage 重新執行 |
| **Declarative 驗證** | REST API 或 CLI | 提交前檢查語法 |
| **JenkinsPipelineUnit** | Shared Library 測試框架 | [12.7 單元測試：JenkinsPipelineUnit](#127-單元測試jenkinspipelineunit) |

**提交前驗證 Jenkinsfile**：

```bash
# 方法一：REST API（需要 API token；Jenkins 2.580.1 實測可用）
curl -fsS -u "$JENKINS_USER:$JENKINS_TOKEN" \
  -X POST -F "jenkinsfile=<Jenkinsfile" \
  https://jenkins.example.internal/pipeline-model-converter/validate

# 方法二：Jenkins CLI
java -jar jenkins-cli.jar -s https://jenkins.example.internal/ -webSocket \
  -auth "@$HOME/.jenkins-cli-auth" declarative-linter < Jenkinsfile
```

> 💡 可以把上述指令加入 Git pre-commit hook 或 IDE 的外部工具。VS Code 的「Jenkins Pipeline Linter Connector」擴充套件也是呼叫同一個端點。本手冊的 Jenkinsfile 範例都以此端點驗證。

### 11.8 本章重點

- 應用程式 Pipeline 使用 Declarative，Scripted 用於 Shared Library 內部與動態流程
- `catch` 一定要重新拋出 `FlowInterruptedException`，否則中止與逾時會失效
- `@NonCPS` 只做純運算；不可序列化的物件不要跨越 step
- Script Approval 預設拒絕；特權操作封裝在受信任 Library 並控管其寫入權限
- 可重跑的 CI 建置使用 `PERFORMANCE_OPTIMIZED`；以 `lock` 與 `milestone` 確保部署順序

## 12. Shared Libraries

### 12.1 用途與目錄結構

Shared Library 把重複的 Pipeline 邏輯集中在一個 Git repository，讓數百個 Jenkinsfile 共用同一套經過測試的建置、掃描、部署步驟。它是企業建立「黃金路徑（golden path）」的核心工具（[22.2 平台團隊與治理模型](#222-平台團隊與治理模型)）。

```text
jenkins-shared-library/
├── vars/                              # 全域變數（自訂 step），檔名即 step 名稱
│   ├── mavenBuild.groovy
│   ├── mavenBuild.txt                 # 說明文件，顯示在 Pipeline Syntax 頁面
│   ├── notifyTeams.groovy
│   └── standardJavaPipeline.groovy    # 封裝整條 Declarative Pipeline
├── src/                               # Groovy 類別（標準 Java 套件結構）
│   └── com/example/ci/
│       ├── Version.groovy
│       └── TeamsCard.groovy
├── resources/                         # 非 Groovy 檔案，以 libraryResource 讀取
│   └── com/example/ci/
│       ├── pod-maven.yaml
│       └── teams-card.json
├── test/groovy/                       # JenkinsPipelineUnit 單元測試
│   └── MavenBuildTest.groovy
├── build.gradle
└── CHANGELOG.md
```

| 目錄 | 內容 | 執行方式 |
| --- | --- | --- |
| `vars/` | 每個檔案定義一個全域 step，`call()` 方法是進入點 | 在 Jenkinsfile 中直接以檔名呼叫：`mavenBuild(goals: 'verify')` |
| `src/` | 一般 Groovy 類別 | `import com.example.ci.Version` 後使用 |
| `resources/` | YAML、JSON、腳本範本 | `libraryResource 'com/example/ci/pod-maven.yaml'` |

### 12.2 設定 Library：受信任與非受信任

| 設定位置 | 信任等級 | 沙箱 | 適用 |
| --- | --- | --- | --- |
| Manage Jenkins → System → **Global Trusted Pipeline Libraries** | 受信任 | ❌ 不在沙箱中執行，可呼叫任何 Java API | 平台團隊維護、需要特權操作的 Library；**repository 寫入權限必須嚴格控管** |
| Manage Jenkins → System → **Global Untrusted Pipeline Libraries** | 非受信任 | ✅ 沙箱 | 全公司共用、但不需要特權的 Library |
| Folder → Pipeline Libraries | 非受信任 | ✅ 沙箱 | 團隊自己的 Library |
| Jenkinsfile 中 `library identifier: ..., retriever: ...` 動態載入 | 非受信任 | ✅ 沙箱 | 臨時測試 |

**以 JCasC 設定**（已以 2.580.1 的 `configuration-as-code/check` 驗證）：

```yaml
unclassified:
  globalLibraries:
    libraries:
      - name: "corp-pipeline-lib"
        defaultVersion: "v2.3.0"
        allowVersionOverride: true
        implicit: false
        includeInChangesets: false
        retriever:
          modernSCM:
            libraryPath: "."
            scm:
              git:
                remote: "https://gitlab.example.internal/platform/jenkins-shared-library.git"
                credentialsId: "gitlab-ci-token"
  globalUntrustedLibraries:
    libraries:
      - name: "corp-utils"
        defaultVersion: "v1.8.0"
        allowVersionOverride: true
        retriever:
          modernSCM:
            scm:
              git:
                remote: "https://gitlab.example.internal/platform/jenkins-utils.git"
                credentialsId: "gitlab-ci-token"
```

| 選項 | 建議 | 說明 |
| --- | --- | --- |
| `defaultVersion` | 固定的 tag（例如 `v2.3.0`） | ❌ 不要用 `main`：Library 的任何提交都會立刻影響所有 Pipeline |
| `allowVersionOverride` | `true` | 讓 Jenkinsfile 以 `@Library('corp-pipeline-lib@v2.4.0-rc1')` 測試新版本 |
| `implicit` | `false` | `true` 會自動載入到所有 Pipeline，難以追蹤相依關係 |
| `includeInChangesets` | `false` | 避免 Library 的變更出現在每個專案的變更紀錄與觸發條件 |

### 12.3 vars：自訂全域 step

`vars/mavenBuild.groovy`：

```groovy
// vars/mavenBuild.groovy
def call(Map config = [:]) {
    String goals = config.get('goals', 'clean verify')
    String settingsId = config.get('settingsId', 'maven-settings-nexus')
    boolean publishTests = config.get('publishTests', true)

    // 只允許英數、空白與 Maven 常用符號，避免把任意字串拼進 shell
    if (!(goals ==~ /[A-Za-z0-9 :._\-=]+/)) {
        error "mavenBuild: goals 含有不允許的字元：${goals}"
    }

    try {
        configFileProvider([configFile(fileId: settingsId, variable: 'MAVEN_SETTINGS')]) {
            withEnv(["MVN_GOALS=${goals}"]) {
                sh 'mvn -B -ntp -s "$MAVEN_SETTINGS" $MVN_GOALS'
            }
        }
    } finally {
        if (publishTests) {
            junit testResults: '**/target/surefire-reports/*.xml', allowEmptyResults: true
        }
    }
}
```

`vars/mavenBuild.txt`（顯示在 Pipeline Syntax → Global Variables Reference）：

```text
mavenBuild(goals: 'clean verify', settingsId: 'maven-settings-nexus', publishTests: true)
  以 Config File Provider 的 settings.xml 執行 Maven，並發佈 JUnit 報告。
  goals 只允許英數、空白與 : . _ - = 字元。
```

**在 Jenkinsfile 中使用**：

```groovy
@Library('corp-pipeline-lib@v2.3.0') _

pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('Build') {
            steps {
                mavenBuild(goals: 'clean verify')
            }
        }
    }
}
```

> 💡 `@Library('name@version') _` 結尾的底線是必要的語法（註解需要附加在某個宣告上）。也可以使用 `library 'corp-pipeline-lib@v2.3.0'` step 在執行期間動態載入。

### 12.4 src 類別與 resources

`src/com/example/ci/Version.groovy`：

```groovy
package com.example.ci

/** 語意化版本計算，不呼叫任何 Pipeline step，可直接以 JUnit 測試 */
class Version implements Serializable {
    private static final long serialVersionUID = 1L
    final int major
    final int minor
    final int patch

    Version(int major, int minor, int patch) {
        this.major = major
        this.minor = minor
        this.patch = patch
    }

    static Version parse(String text) {
        def parts = text.replaceFirst(/^v/, '').tokenize('.')
        if (parts.size() != 3) {
            throw new IllegalArgumentException("不是有效的版本號：${text}")
        }
        return new Version(parts[0] as int, parts[1] as int, parts[2] as int)
    }

    Version nextPatch() {
        return new Version(major, minor, patch + 1)
    }

    @Override
    String toString() {
        return "${major}.${minor}.${patch}"
    }
}
```

需要呼叫 Pipeline step 的類別，必須把 Pipeline 的 `script` 物件（`this`）傳進去：

```groovy
// src/com/example/ci/Notifier.groovy
package com.example.ci

class Notifier implements Serializable {
    private static final long serialVersionUID = 1L
    private final def steps

    Notifier(steps) {
        this.steps = steps
    }

    void teams(String credentialsId, String text) {
        def payload = groovy.json.JsonOutput.toJson([text: text])
        steps.withCredentials([steps.string(credentialsId: credentialsId, variable: 'TEAMS_WEBHOOK')]) {
            steps.writeFile file: 'teams-payload.json', text: payload
            steps.sh 'curl -fsS -H "Content-Type: application/json" -d @teams-payload.json "$TEAMS_WEBHOOK"'
        }
    }
}
```

```groovy
// 在 Jenkinsfile 的 script 區塊中使用
@Library('corp-pipeline-lib@v2.3.0') _
import com.example.ci.Notifier

pipeline {
    agent { label 'linux' }
    stages {
        stage('Notify') {
            steps {
                script {
                    new Notifier(this).teams('teams-webhook-payments', "部署完成：${env.JOB_NAME} #${env.BUILD_NUMBER}")
                }
            }
        }
    }
}
```

**resources 的使用**（例如共用的 Kubernetes Pod 範本）：

```groovy
// vars/withMavenPod.groovy：以 Library 內的 Pod 範本建立 Kubernetes agent
def call(Closure body) {
    def podYaml = libraryResource 'com/example/ci/pod-maven.yaml'
    podTemplate(yaml: podYaml) {
        node(POD_LABEL) {
            container('maven') {
                body()
            }
        }
    }
}
```

### 12.5 Pipeline 範本：封裝整條 Declarative Pipeline

把整條 Declarative Pipeline 放在 `vars/` 中，各專案的 Jenkinsfile 只需要幾行設定，平台團隊即可集中推行標準（品質門檻、掃描、部署核准）：

```groovy
// vars/standardJavaPipeline.groovy
def call(Map cfg) {
    String appName = cfg.appName ?: error('standardJavaPipeline: 必須指定 appName')
    String jdk = cfg.get('jdk', '21')
    double coverage = cfg.get('minLineCoverage', 70.0) as double

    pipeline {
        agent none
        options {
            buildDiscarder(logRotator(numToKeepStr: '50'))
            disableConcurrentBuilds(abortPrevious: true)
            timeout(time: 60, unit: 'MINUTES')
            timestamps()
        }
        environment {
            APP_NAME = "${appName}"
        }
        stages {
            stage('Build & Test') {
                agent {
                    docker {
                        image "maven:3.9.16-eclipse-temurin-${jdk}"
                        label 'linux && docker'
                    }
                }
                steps {
                    mavenBuild(goals: 'clean verify', publishTests: true)
                }
                post {
                    always {
                        recordCoverage(tools: [[parser: 'JACOCO']],
                                       qualityGates: [[threshold: coverage, metric: 'LINE', baseline: 'PROJECT', criticality: 'UNSTABLE']])
                    }
                }
            }
            stage('Deploy DEV') {
                when {
                    beforeAgent true
                    branch 'main'
                }
                agent { label 'deploy' }
                steps {
                    echo "部署 ${APP_NAME} 至 dev"
                }
            }
        }
    }
}
```

各專案的 `Jenkinsfile` 只剩：

```groovy
@Library('corp-pipeline-lib@v2.3.0') _

standardJavaPipeline(appName: 'payment-api', jdk: '21', minLineCoverage: 75)
```

> ⚠️ 封裝整條 Pipeline 時，`vars` 中只能有一個 `pipeline {}`，且必須是 `call` 方法的最後一個陳述式。提供「逃生口」（例如 `cfg.extraStages` 或允許專案改用自己的 Jenkinsfile），避免特殊需求的專案被迫繞過平台標準。

### 12.6 版本管理與發佈流程

```mermaid
flowchart LR
    A[Library MR／PR] --> B[CI：單元測試＋<br/>JenkinsPipelineUnit]
    B --> C[合併到 main]
    C --> D[建立 tag v2.4.0-rc1]
    D --> E["試點專案以<br/>@Library('lib@v2.4.0-rc1') 驗證"]
    E --> F[建立正式 tag v2.4.0<br/>更新 CHANGELOG]
    F --> G[以 JCasC 調整<br/>defaultVersion]
```

| 原則 | 說明 |
| --- | --- |
| 語意化版本 | 不相容的變更（參數改名、預設行為改變）提升主版號 |
| 不可變 tag | 已發佈的 tag 不得移動；設定 Git 伺服器的 protected tags |
| 程式碼審查 | 受信任 Library 至少兩人審查；CODEOWNERS 指定平台團隊 |
| 棄用流程 | 舊參數保留至少一個次版本，並以 `echo` 輸出棄用警告 |

### 12.7 單元測試：JenkinsPipelineUnit

[JenkinsPipelineUnit](https://github.com/jenkinsci/JenkinsPipelineUnit)（v1.31，2026-07）以模擬（mock）的方式在本機執行 Pipeline 腳本，驗證呼叫了哪些 step、參數是否正確。它**需要 Java 21**，使用與 Jenkins 相同的 Groovy 2.4.21，目前不相容 Groovy 4；本身的測試以 JUnit Jupiter 6.1.3 撰寫。

`build.gradle`：

```groovy
plugins {
    id 'groovy'
}

repositories {
    mavenCentral()
    maven { url 'https://repo.jenkins-ci.org/releases/' }
}

dependencies {
    implementation 'org.codehaus.groovy:groovy-all:2.4.21'
    testImplementation 'com.lesfurets:jenkins-pipeline-unit:1.31'
    testImplementation 'org.junit.jupiter:junit-jupiter:6.1.3'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher:6.1.3'
}

test {
    useJUnitPlatform()
}

sourceSets {
    main { groovy { srcDirs = ['src', 'vars'] } }
    test { groovy { srcDirs = ['test/groovy'] } }
}
```

`test/groovy/MavenBuildTest.groovy`：

```groovy
import com.lesfurets.jenkins.unit.BasePipelineTest
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

import static org.junit.jupiter.api.Assertions.assertThrows
import static org.junit.jupiter.api.Assertions.assertTrue

class MavenBuildTest extends BasePipelineTest {

    @Override
    @BeforeEach
    void setUp() throws Exception {
        super.setUp()
        helper.registerAllowedMethod('configFile', [Map]) { Map m -> m }
        helper.registerAllowedMethod('configFileProvider', [List, Closure]) { List l, Closure c -> c() }
        helper.registerAllowedMethod('junit', [Map], null)
    }

    @Test
    void runsMavenWithGivenGoals() {
        def script = loadScript('vars/mavenBuild.groovy')
        script.call(goals: 'clean verify')
        assertTrue(helper.callStack.any { it.methodName == 'sh' && it.argsToString().contains('$MVN_GOALS') })
        assertTrue(helper.callStack.any { it.methodName == 'junit' })
    }

    @Test
    void rejectsUnsafeGoals() {
        def script = loadScript('vars/mavenBuild.groovy')
        helper.registerAllowedMethod('error', [String]) { String msg -> throw new IllegalStateException(msg) }
        assertThrows(IllegalStateException) {
            script.call(goals: 'verify; curl http://evil.example')
        }
    }
}
```

> 💡 JenkinsPipelineUnit 驗證的是「呼叫了哪些 step」，不會真的執行 Jenkins。發佈前仍要以 `@Library('...@<rc tag>')` 在試點專案上實際執行一次（12.6 的流程）。

### 12.8 本章重點

- Library 以固定 tag 作為 `defaultVersion`，新版本先以 rc tag 在試點專案驗證
- 受信任 Library 不在沙箱中執行，其 repository 寫入權限等同 Jenkins 管理員權限
- `vars` 提供自訂 step 與整條 Pipeline 範本；`src` 放純邏輯類別，需要 step 時傳入 `this`
- 以 JenkinsPipelineUnit 撰寫單元測試，並在 Library 自己的 CI 中執行

## 13. 測試報告、覆蓋率與品質門檻

### 13.1 JUnit 測試報告

`junit` step（JUnit plugin）解析 JUnit XML 格式的報告，產生測試趨勢圖、失敗測試清單，並在有失敗測試時把建置設為 **UNSTABLE**。幾乎所有語言的測試框架都能輸出此格式（Maven Surefire／Failsafe、Gradle、pytest `--junitxml`、Jest `jest-junit`、Go `go-junit-report`）。

```groovy
pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('Test') {
            steps {
                sh './mvnw -B -ntp verify'
            }
            post {
                always {
                    junit testResults: '**/target/surefire-reports/TEST-*.xml, **/target/failsafe-reports/TEST-*.xml',
                          allowEmptyResults: false,
                          skipPublishingChecks: false,
                          stdioRetention: 'FAILED',
                          healthScaleFactor: 1.0
                }
            }
        }
    }
}
```

| 參數 | 建議值 | 說明 |
| --- | --- | --- |
| `testResults` | 明確的路徑樣式 | 多個樣式以逗號分隔 |
| `allowEmptyResults` | 測試必定存在的專案設 `false` | 找不到報告時讓建置失敗，避免「沒有執行任何測試卻顯示成功」 |
| `stdioRetention` | `'FAILED'` | 只保留失敗測試的標準輸出，節省 controller 磁碟 |
| `skipPublishingChecks` | `false` | 搭配 GitHub Checks 時在 PR 上顯示測試結果（13.6） |
| `skipMarkingBuildUnstable` | 一般為 `false` | 設為 `true` 時測試失敗不影響建置結果（不建議） |

> ⚠️ 不要在 Maven 加上 `-Dmaven.test.failure.ignore=true` 之後又忽略 UNSTABLE 結果。測試失敗應該阻擋合併與部署；若有不穩定測試，應標記並修正，而不是全面忽略。

### 13.2 程式碼覆蓋率：Coverage plugin

**Coverage** plugin（`recordCoverage`）取代了 JaCoCo、Cobertura、Code Coverage API 等舊 plugin，支援 JaCoCo、Cobertura、Clover、Go cover、LCOV、OpenCover、PIT（突變測試）等格式，並可針對「修改的程式行」計算覆蓋率。

```groovy
pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('Test') {
            steps {
                sh './mvnw -B -ntp verify'   // pom.xml 中已設定 jacoco-maven-plugin 的 report goal
            }
            post {
                always {
                    discoverReferenceBuild(referenceJob: 'payments/payment-api/main')
                    recordCoverage(tools: [[parser: 'JACOCO', pattern: '**/target/site/jacoco/jacoco.xml']],
                                   id: 'jacoco',
                                   name: 'JaCoCo 覆蓋率',
                                   sourceCodeRetention: 'MODIFIED',
                                   sourceDirectories: [[path: 'src/main/java']],
                                   qualityGates: [
                                       [threshold: 70.0, metric: 'LINE', baseline: 'PROJECT', criticality: 'UNSTABLE'],
                                       [threshold: 80.0, metric: 'LINE', baseline: 'MODIFIED_LINES', criticality: 'UNSTABLE'],
                                       [threshold: -1.0, metric: 'LINE', baseline: 'PROJECT_DELTA', criticality: 'NOTE']
                                   ])
                }
            }
        }
    }
}
```

| Baseline | 意義 | 建議用途 |
| --- | --- | --- |
| `PROJECT` | 整個專案的覆蓋率 | 底線門檻（例如 70%） |
| `MODIFIED_LINES` | 本次變更的程式行 | ✅ PR 的主要門檻：新寫的程式要有測試（例如 80%） |
| `MODIFIED_FILES` | 本次變更的檔案 | 較寬鬆的變更門檻 |
| `PROJECT_DELTA`／`MODIFIED_LINES_DELTA`／`MODIFIED_FILES_DELTA` | 與參考建置相比的差值 | 防止覆蓋率持續下降 |
| `INDIRECT` | 間接影響的程式碼 | 進階分析 |

> 💡 `MODIFIED_LINES` 與 `*_DELTA` 需要知道「和誰比較」：以 `discoverReferenceBuild` 指定參考 Job（通常是目標分支），PR 建置才能正確計算差異。

<!-- markdownlint-disable-next-line MD028 -->
> 📌 v1.0 使用 JaCoCo plugin 的 `jacoco(execPattern: ..., minimumInstructionCoverage: ...)`，並在第 4 章的必要 plugin 清單中列出已自 update center 下架的 `checkstyle` plugin。v2.0 覆蓋率全面改用 `recordCoverage`，靜態分析改用 `recordIssues`。品質門檻的失敗等級使用 `criticality`（`NOTE`、`UNSTABLE`、`ERROR`、`FAILURE`）。

### 13.3 靜態分析：Warnings Next Generation

**Warnings NG**（`recordIssues`）可解析超過 100 種工具的報告，取代已下架的 Checkstyle、PMD、FindBugs plugin。

```groovy
pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('Static Analysis') {
            steps {
                sh './mvnw -B -ntp -DskipTests verify checkstyle:checkstyle pmd:pmd pmd:cpd spotbugs:spotbugs'
            }
            post {
                always {
                    discoverReferenceBuild(referenceJob: 'payments/payment-api/main')
                    recordIssues(enabledForFailure: true,
                                 aggregatingResults: false,
                                 sourceCodeRetention: 'MODIFIED',
                                 tools: [java(),
                                         javaDoc(),
                                         checkStyle(pattern: '**/target/checkstyle-result.xml'),
                                         pmdParser(pattern: '**/target/pmd.xml'),
                                         cpd(pattern: '**/target/cpd.xml'),
                                         spotBugs(pattern: '**/target/spotbugsXml.xml', useRankAsPriority: true)],
                                 qualityGates: [
                                     [threshold: 1, type: 'NEW_ERROR', criticality: 'FAILURE'],
                                     [threshold: 1, type: 'NEW_HIGH', criticality: 'UNSTABLE'],
                                     [threshold: 10, type: 'NEW', criticality: 'UNSTABLE']
                                 ])
                }
            }
        }
    }
}
```

| 品質門檻類型 | 意義 |
| --- | --- |
| `TOTAL`、`TOTAL_ERROR`／`HIGH`／`NORMAL`／`LOW` | 目前所有問題數 |
| `NEW`、`NEW_ERROR`／`HIGH`／`NORMAL`／`LOW` | ✅ 相對於參考建置**新增**的問題（建議以此為主，避免既有技術債阻擋所有建置） |
| `DELTA`、`DELTA_*` | 與參考建置的數量差 |
| `TOTAL_MODIFIED`、`NEW_MODIFIED` | 只計算本次修改檔案中的問題 |

| 常用 tool | 報告來源 |
| --- | --- |
| `java()`、`javaDoc()`、`mavenConsole()` | 直接解析主控台輸出中的編譯器與 Maven 警告 |
| `checkStyle()`、`pmdParser()`、`cpd()`、`spotBugs()` | Maven／Gradle plugin 產生的 XML |
| `errorProne()` | Error Prone 編譯器外掛 |
| `esLint()` | ESLint checkstyle 格式輸出 |
| `owaspDependencyCheck()`、`trivy()` | 相依套件弱點報告（第 21 章） |
| `sonarQube()` | SonarQube 的問題報告 |
| `taskScanner(includePattern: '**/*.java', highTags: 'FIXME', normalTags: 'TODO')` | 程式碼中的待辦標記 |

### 13.4 SonarQube 品質門檻

```mermaid
sequenceDiagram
    participant J as Jenkins Pipeline
    participant S as SonarQube
    J->>S: mvn sonar:sonar（withSonarQubeEnv 注入 URL 與 token）
    S-->>J: 回傳 analysis task ID
    S->>S: 背景計算 Quality Gate
    S->>J: Webhook POST /sonarqube-webhook/
    J->>J: waitForQualityGate 收到結果
    J->>J: 未通過 → abortPipeline 使建置失敗
```

**JCasC 設定**：

```yaml
unclassified:
  sonarglobalconfiguration:
    buildWrapperEnabled: true
    installations:
      - name: "sonarqube"
        serverUrl: "https://sonarqube.example.internal"
        credentialsId: "sonar-token"
```

**Pipeline**：

```groovy
pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh './mvnw -B -ntp verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=payments_payment-api'
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
```

✅ 設定要點：

- 在 SonarQube 的 Administration → Configuration → Webhooks 新增 `https://jenkins.example.internal/sonarqube-webhook/`，並設定 secret（Jenkins 端在 SonarQube server 設定中填入同一個 secret）
- `waitForQualityGate` 一定要包在 `timeout` 中；webhook 遺失時才不會無限等待
- `sonar-maven-plugin` 的版本應在 `pom.xml` 的 `pluginManagement` 中固定，避免每次解析最新版
- PR 分析（branch／PR decoration）需要 SonarQube Developer Edition 以上或 SonarQube Cloud；Community Build 只分析主分支

### 13.5 品質門檻設計

| 關卡 | PR 建置 | 主分支建置 | 正式發佈 |
| --- | --- | --- | --- |
| 編譯與單元測試 | 必須全部通過（FAILURE） | 同左 | 同左 |
| 新增程式碼覆蓋率（`MODIFIED_LINES`） | ≥ 80%（UNSTABLE） | — | — |
| 專案覆蓋率（`PROJECT`） | 不低於參考建置（NOTE） | ≥ 70%（UNSTABLE） | ≥ 70%（FAILURE） |
| 新增靜態分析問題 | `NEW_ERROR` ≥ 1 → FAILURE；`NEW_HIGH` ≥ 1 → UNSTABLE | 同左 | 同左 |
| SonarQube Quality Gate | 通過（PR decoration） | 通過 | 通過 |
| 相依套件高風險弱點（第 21 章） | 新增即 UNSTABLE | Critical → FAILURE | Critical／High → FAILURE |

> 💡 搭配 `options { skipStagesAfterUnstable() }`：品質門檻把建置設為 UNSTABLE 後，後續的映像建置與部署 stage 會自動略過。合併規則（GitHub branch protection／GitLab「Pipelines must succeed」）要求 Jenkins 回報的狀態為成功。

### 13.6 回報到 GitHub Checks 與 GitLab MR

| 平台 | 機制 | 設定 |
| --- | --- | --- |
| GitHub | **Checks API**（`checks-api`＋`github-checks` plugin，需使用 GitHub App 憑證） | `junit`、`recordCoverage`、`recordIssues` 會自動發佈對應的 Check run，在 PR 中逐行顯示註解；以 `skipPublishingChecks: true` 關閉 |
| GitHub | Commit status | GitHub Branch Source 自動回報建置狀態 |
| GitLab | Pipeline 狀態 | GitLab Branch Source 自動以 `jenkinsci/<job>` 名稱回報 commit status，可在專案設定為合併前提 |

### 13.7 HTML 報告與安全限制

測試框架產生的 HTML 報告（例如 Playwright、Allure、Gatling）可以用 HTML Publisher plugin 的 `publishHTML` 發佈。Jenkins 預設以 Content Security Policy 限制這些檔案中的 JavaScript 與 CSS，因此報告可能無法正常顯示。

| 做法 | 說明 |
| --- | --- |
| ✅ 設定 **Resource Root URL** | Manage Jenkins → Security → Resource Root URL，指定另一個網域（例如 `https://jenkins-files.example.internal/`）提供使用者上傳或建置產生的檔案；這些檔案在獨立的網域中執行，不影響 Jenkins 本身的安全 |
| ⚠️ 放寬 `hudson.model.DirectoryBrowserSupport.CSP` | 會讓惡意建置產物在 Jenkins 網域執行腳本、竊取使用者 session，**不建議** |
| 改用外部報告伺服器 | 把報告上傳到物件儲存或報告平台，Jenkins 只放連結 |

### 13.8 本章重點

- `junit` 讓測試失敗成為 UNSTABLE；`allowEmptyResults: false` 防止「沒有測試卻成功」
- 覆蓋率用 Coverage plugin（`recordCoverage`），靜態分析用 Warnings NG（`recordIssues`），PR 以「新增程式碼」為門檻
- SonarQube 以 webhook＋`waitForQualityGate` 包在 `timeout` 中
- HTML 報告透過 Resource Root URL 提供，不要放寬全域 CSP

## 14. Agent 與雲端節點

### 14.1 Agent 規劃與 Label 設計

| 規劃面向 | 建議 |
| --- | --- |
| Label 命名 | 以**能力**命名：`linux`、`windows`、`docker`、`maven`、`node`、`gpu`、`macos-xcode16`；避免主機名稱 |
| 信任分級 | `ci-untrusted`（外部 PR）、`ci`（一般建置）、`deploy`／`deploy-prod`（部署專用，網路可達正式環境） |
| Executor 數 | 固定 agent：CPU 核心數的 50–100%；容器化或雲端 agent：1 |
| 生命週期 | ✅ 優先使用可拋棄的雲端 agent（每次建置全新環境）；固定 agent 用於特殊硬體或授權 |
| Java | Agent 程序必須以 Java 21 或 25 執行（2.555.1 起） |

```mermaid
flowchart LR
    subgraph Trust0[信任等級：低]
        U[ci-untrusted<br/>外部 PR、fork]
    end
    subgraph Trust1[信任等級：中]
        C[ci<br/>內部分支、PR]
    end
    subgraph Trust2[信任等級：高]
        D[deploy<br/>dev／sit／uat]
        P[deploy-prod<br/>正式環境]
    end
    U -. 無法存取 .-> Cred[(部署憑證)]
    C -. 無法存取 .-> Cred
    D --> Cred
    P --> Cred
```

### 14.2 固定 agent：SSH 與 Windows

**Linux 固定 agent（SSH Build Agents）**，以 JCasC 定義：

```yaml
jenkins:
  nodes:
    - permanent:
        name: "linux-build-01"
        labelString: "linux docker maven ci"
        numExecutors: 4
        remoteFS: "/home/jenkins/agent"
        mode: EXCLUSIVE
        retentionStrategy: "always"
        launcher:
          ssh:
            host: "build-01.example.internal"
            port: 22
            credentialsId: "agent-ssh-key"
            javaPath: "/usr/lib/jvm/java-21-openjdk/bin/java"
            launchTimeoutSeconds: 60
            maxNumRetries: 3
            retryWaitTime: 15
            sshHostKeyVerificationStrategy:
              knownHostsFileKeyVerificationStrategy: {}
```

| 設定 | 說明 |
| --- | --- |
| `mode: EXCLUSIVE` | 只執行 label 符合的建置（避免 `agent any` 跑到此節點） |
| `sshHostKeyVerificationStrategy` | ✅ 使用 known_hosts 驗證主機金鑰；❌ 不要用「Non verifying」 |
| `javaPath` | 明確指定 Java 21 路徑 |

**Windows 固定 agent**：2.504.1 移除了 DCOM（「Let Jenkins control this Windows agent as a Windows service」）啟動方式，請改用以下其中一種：

| 方式 | 做法 |
| --- | --- |
| ✅ Inbound（WebSocket）＋Windows 服務 | 以 [WinSW](https://github.com/winsw/winsw) 等服務包裝工具把 `java -jar agent.jar -url ... -secret @secret.txt -name ... -webSocket -workDir D:\jenkins` 註冊為 Windows 服務，以專用服務帳號執行 |
| SSH（Windows OpenSSH Server） | SSH Build Agents plugin 支援連線 Windows 的 OpenSSH，設定方式與 Linux 相同 |

**WinSW 設定範例**（WinSW 最新穩定版為 2.12.0；把 `WinSW-x64.exe` 改名為 `jenkins-agent.exe`，與同名的 `jenkins-agent.xml` 放在同一目錄）：

```xml
<service>
  <id>jenkins-agent</id>
  <name>Jenkins Agent (win-build-01)</name>
  <description>Jenkins inbound agent，以 WebSocket 連線 controller</description>
  <executable>C:\Program Files\Eclipse Adoptium\jdk-21\bin\java.exe</executable>
  <arguments>-Xmx1g -jar D:\jenkins\agent.jar -url https://jenkins.example.internal/ -secret @D:\jenkins\agent-secret.txt -name win-build-01 -webSocket -workDir D:\jenkins\work</arguments>
  <log mode="roll-by-size">
    <sizeThreshold>10240</sizeThreshold>
    <keepFiles>8</keepFiles>
  </log>
  <onfailure action="restart" delay="10 sec"/>
</service>
```

```powershell
# 以系統管理員身分執行
Set-Location D:\jenkins
Invoke-WebRequest -Uri "https://jenkins.example.internal/jnlpJars/agent.jar" -OutFile "D:\jenkins\agent.jar"
.\jenkins-agent.exe install
# 服務登入帳號建議使用群組受管理服務帳戶（gMSA），密碼由 AD 自動輪替
sc.exe config jenkins-agent obj= "CORP\svc-jenkins-agt$"
icacls D:\jenkins\agent-secret.txt /inheritance:r /grant "CORP\svc-jenkins-agt$:R" /grant "Administrators:F"
Start-Service jenkins-agent
```

> 💡 Windows agent 上的建置會以服務帳號身分執行。需要存取網路磁碟或簽章憑證時，使用網域服務帳號並只授予必要權限；不要以 LocalSystem 執行。

### 14.3 Docker agent

| 機制 | Plugin | 運作方式 | 適用 |
| --- | --- | --- | --- |
| `agent { docker { ... } }` | Docker Pipeline | 在具備 Docker 的 agent 上，以容器執行 steps（workspace 以 volume 掛入） | 已有 Docker 主機的團隊 |
| Docker Cloud | Docker plugin | 依需求在 Docker 主機上啟動整個 agent 容器 | 小型環境的動態 agent |

```groovy
pipeline {
    agent none
    stages {
        stage('Backend') {
            agent {
                docker {
                    image 'maven:3.9.16-eclipse-temurin-21'
                    label 'linux && docker'
                    registryUrl 'https://harbor.example.internal'
                    registryCredentialsId 'harbor-robot-ci'
                    args '--network=ci-net -v maven-repo-cache:/root/.m2/repository'
                    alwaysPull true
                }
            }
            steps {
                sh 'mvn -B -ntp verify'
            }
        }
        stage('Frontend') {
            agent {
                docker {
                    image 'node:24-bookworm-slim'
                    label 'linux && docker'
                }
            }
            steps {
                sh 'npm ci && npm run build'
            }
        }
    }
}
```

> ⚠️ Docker agent 主機上的 Docker daemon 等同 root。任何能修改 Jenkinsfile 的人都可以 `args '-v /:/host'` 掛載主機根目錄。使用 Docker agent 時，主機只能用於建置（不放其他服務與機密），並依信任等級分開主機；更好的做法是改用 Kubernetes agent 搭配 Pod Security（14.4、14.6）。

### 14.4 Kubernetes plugin

Kubernetes plugin 依建置需求動態建立 Pod，每個 Pod 自動包含一個連回 controller 的 `jnlp` 容器，以及 Pipeline 指定的工具容器。

```mermaid
sequenceDiagram
    participant C as Jenkins Controller
    participant K as Kubernetes API
    participant P as Agent Pod
    C->>K: 建立 Pod（jnlp＋maven＋buildkit 容器）
    K->>P: 排程並啟動容器
    P->>C: jnlp 容器以 WebSocket 連線
    C->>P: 在 maven 容器中執行 sh 步驟
    C->>K: 建置結束，刪除 Pod
```

**Cloud 設定（JCasC）**：

```yaml
jenkins:
  clouds:
    - kubernetes:
        name: "kubernetes"
        namespace: "jenkins-agents"
        jenkinsUrl: "http://jenkins.jenkins.svc.cluster.local:8080/"
        webSocket: true
        containerCapStr: "100"
        maxRequestsPerHostStr: "64"
        podRetention: "never"
        waitForPodSec: 600
        templates:
          - name: "maven-jdk21"
            label: "k8s-maven"
            nodeUsageMode: EXCLUSIVE
            serviceAccount: "jenkins-agent"
            idleMinutes: 0
            yaml: |
              apiVersion: v1
              kind: Pod
              spec:
                automountServiceAccountToken: false
                securityContext:
                  runAsUser: 1000
                  runAsGroup: 1000
                  fsGroup: 1000
                  runAsNonRoot: true
                  seccompProfile:
                    type: RuntimeDefault
                containers:
                  - name: maven
                    image: maven:3.9.16-eclipse-temurin-21
                    command: ["sleep"]
                    args: ["infinity"]
                    env:
                      - name: MAVEN_CONFIG
                        value: /home/jenkins/.m2
                    resources:
                      requests:
                        cpu: "1"
                        memory: 2Gi
                      limits:
                        memory: 3Gi
                    securityContext:
                      allowPrivilegeEscalation: false
                      capabilities:
                        drop: ["ALL"]
```

**在 Jenkinsfile 中宣告 Pod**（範本放在 repository 的 `ci/pod.yaml`，或使用 cloud 中定義的 label）：

```groovy
pipeline {
    agent {
        kubernetes {
            inheritFrom 'maven-jdk21'
            defaultContainer 'maven'
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                    - name: node
                      image: node:24-bookworm-slim
                      command: ["sleep"]
                      args: ["infinity"]
                      resources:
                        requests:
                          cpu: "500m"
                          memory: 1Gi
            '''
        }
    }
    stages {
        stage('Backend') {
            steps {
                sh 'mvn -B -ntp -Dmaven.repo.local=/home/jenkins/agent/.m2 verify'
            }
        }
        stage('Frontend') {
            steps {
                container('node') {
                    sh 'npm ci && npm test -- --ci'
                }
            }
        }
    }
}
```

| 設定 | 建議 |
| --- | --- |
| `webSocket: true` | Agent 透過 controller 的 HTTP 服務連線，不需要開放 50000 埠與額外的 Service |
| Agent namespace | 與 controller 分開，設定 ResourceQuota、LimitRange、NetworkPolicy |
| `automountServiceAccountToken: false` | 建置容器預設不需要 Kubernetes API 權限；需要部署時改用專用 kubeconfig 憑證 |
| Pod Security | Namespace 套用 Pod Security Admission `restricted`（或至少 `baseline`）；不允許 privileged 容器 |
| 資源 | 每個容器都設定 requests 與 memory limits，避免 OOM 影響同節點的其他 Pod |
| `podRetention: never` | 建置結束即刪除；除錯時暫時改為 `onFailure` |
| `idleMinutes` | 0（每次全新 Pod）；建置頻繁且需要暖快取時可設 5–10 |

> ⚠️ 建置容器的 `command` 必須讓容器保持執行（例如 `sleep infinity`），否則容器啟動後立即結束，Pipeline 會卡在等待容器。Kubernetes plugin 會自動加入 `jnlp` 容器，不需要自行定義（除非要指定映像版本）。

### 14.5 其他雲端 agent

| Plugin | 環境 | 特點 |
| --- | --- | --- |
| Amazon EC2 | AWS | 依 AMI 動態建立 EC2 執行個體，支援 Spot、閒置自動終止；搭配 IAM role 而非存取金鑰 |
| Azure VM Agents | Azure | 依映像建立 VM，支援 Managed Identity |
| Google Compute Engine | GCP | 依執行個體範本建立 VM |
| Docker plugin | Docker 主機 | 小型環境的動態容器 agent |

適用情境：需要完整 VM 的建置（Windows、需 privileged 權限的整合測試、GPU）、或尚未導入 Kubernetes 的組織。

### 14.6 Agent 安全與隔離

| 控制 | 說明 |
| --- | --- |
| **Agent → Controller 安全** | 自 2.326 起永遠啟用，agent 無法任意讀寫 controller 檔案；不要以系統屬性關閉 |
| 依信任等級分開 agent | 外部 PR 只能在 `ci-untrusted` 執行，該 agent 網路上無法連到內部系統與部署目標 |
| 限制 Job 可使用的 agent | 以 Job Restrictions 等 plugin 或 folder 層級的 cloud 設定，讓只有 `prod` folder 的 Job 能使用 `deploy-prod` |
| 可拋棄式 agent | 雲端 agent 每次建置後銷毀，避免前一次建置留下的惡意檔案或憑證 |
| 不在 agent 上保存長期憑證 | 憑證由 Jenkins 在建置時注入，結束即刪除 |
| 網路出口控管 | 建置環境只能連到內部 artifact 儲存庫與必要的外部網址（防止資料外洩與相依套件混淆攻擊） |

### 14.7 本章重點

- Label 以能力與信任等級命名；部署 agent 與一般建置 agent 分開
- 固定 agent 使用 SSH（驗證主機金鑰）或 WebSocket inbound；Windows 不再支援 DCOM 啟動
- Kubernetes agent 使用 WebSocket、獨立 namespace、非 root、resource limits，並關閉 service account token 自動掛載
- Docker agent 主機等同 root，需依信任等級分開或改用 Kubernetes

## 15. 容器映像建置與 Kubernetes 上的 Jenkins

### 15.1 映像建置方式比較

| 方式 | 需要的權限 | 風險 | 建議 |
| --- | --- | --- | --- |
| 掛載主機 `docker.sock` | 主機 Docker daemon（等同 root） | ❌ 建置可控制整台主機與其上所有容器 | 不使用（v1.0 的 Compose 範例即為此作法） |
| Docker-in-Docker（`docker:dind`） | `privileged: true` | ⚠️ privileged 容器可逃逸到節點 | 只用於隔離的專用節點或學習環境 |
| **BuildKit rootless** | 非 root；需放寬 seccomp／AppArmor，或使用 `--oci-worker-no-process-sandbox` | 低 | ✅ Kubernetes 上的首選 |
| Buildah／Podman rootless | 非 root；需要 user namespace 或 `/dev/fuse` | 低 | ✅ RHEL／OpenShift 環境 |
| Kaniko | 以 root 在容器內執行（不需 privileged） | 中 | ⚠️ Google 已於 2025-06 封存原專案；Chainguard 維護分支（`chainguard-forks/kaniko`）。新導入建議改用 BuildKit |
| 雲端建置服務（AWS CodeBuild、Google Cloud Build） | 由雲端服務提供 | 低 | 已使用公有雲的團隊 |
| Jib（Maven／Gradle plugin） | 不需容器執行環境 | 低 | ✅ 純 Java 應用，不需要 Dockerfile |

### 15.2 BuildKit rootless（Kubernetes agent）

`ci/buildkit-pod.yaml`（第 10 章完整範例使用的 Pod 範本），參考 `moby/buildkit` 的官方 `job.rootless.yaml`：

```yaml
apiVersion: v1
kind: Pod
spec:
  automountServiceAccountToken: false
  containers:
    - name: buildkit
      image: moby/buildkit:v0.33.1-rootless
      command: ["cat"]
      tty: true
      env:
        - name: BUILDKITD_FLAGS
          value: --oci-worker-no-process-sandbox
      securityContext:
        runAsUser: 1000
        runAsGroup: 1000
        seccompProfile:
          type: Unconfined
        appArmorProfile:
          type: Unconfined
      resources:
        requests:
          cpu: "1"
          memory: 2Gi
        limits:
          memory: 4Gi
      volumeMounts:
        - name: buildkitd
          mountPath: /home/user/.local/share/buildkit
  volumes:
    - name: buildkitd
      emptyDir: {}
```

```groovy
pipeline {
    agent {
        kubernetes {
            yamlFile 'ci/buildkit-pod.yaml'
            defaultContainer 'buildkit'
        }
    }
    environment {
        IMAGE = "harbor.example.internal/payments/payment-api:${env.BUILD_NUMBER}"
    }
    stages {
        stage('Build & Push') {
            steps {
                withCredentials([file(credentialsId: 'harbor-dockerconfig-payments', variable: 'DOCKER_CONFIG_JSON')]) {
                    sh '''
                        set -eu
                        export DOCKER_CONFIG="$(mktemp -d)"
                        cp "$DOCKER_CONFIG_JSON" "$DOCKER_CONFIG/config.json"
                        buildctl-daemonless.sh build \
                          --frontend dockerfile.v0 \
                          --local context=. \
                          --local dockerfile=. \
                          --opt build-arg:APP_VERSION="$BUILD_NUMBER" \
                          --export-cache type=registry,ref=harbor.example.internal/payments/payment-api:buildcache,mode=max \
                          --import-cache type=registry,ref=harbor.example.internal/payments/payment-api:buildcache \
                          --output type=image,name="$IMAGE",push=true \
                          --metadata-file build-metadata.json
                        rm -rf "$DOCKER_CONFIG"
                    '''
                }
                archiveArtifacts artifacts: 'build-metadata.json', fingerprint: true
            }
        }
    }
}
```

| 重點 | 說明 |
| --- | --- |
| `command: ["cat"]`＋`tty: true` | 讓容器保持執行，等待 Jenkins 呼叫 `sh` |
| `BUILDKITD_FLAGS=--oci-worker-no-process-sandbox` | 不建立 PID namespace，降低對節點設定的需求（官方範例的做法） |
| `seccompProfile`／`appArmorProfile: Unconfined` | rootless BuildKit 需要；`appArmorProfile` 欄位需要 Kubernetes 1.30 以上。若叢集以 Pod Security `restricted` 強制，需為建置 namespace 設定例外 |
| Registry 快取 | `--export-cache`／`--import-cache` 讓每次全新 Pod 也能重用層快取 |
| `--metadata-file` | 輸出包含映像 **digest** 的 JSON，供後續簽章與部署使用（16.1、21.4） |
| 憑證 | 以 Secret file 型態保存 `config.json`（Harbor robot account），建置後刪除 |

### 15.3 Buildah 與 Jib

**Buildah（rootless，以 vfs 儲存驅動避免需要 `/dev/fuse`）**：

```bash
#!/usr/bin/env bash
set -euo pipefail
export STORAGE_DRIVER=vfs
buildah bud --layers --format oci -t "harbor.example.internal/payments/payment-api:${BUILD_NUMBER}" .
buildah push --digestfile image.digest "harbor.example.internal/payments/payment-api:${BUILD_NUMBER}"
cat image.digest
```

**Jib（不需要 Dockerfile 與容器執行環境）**：

```bash
./mvnw -B -ntp compile com.google.cloud.tools:jib-maven-plugin:3.5.2:build \
  -Djib.to.image="harbor.example.internal/payments/payment-api:${BUILD_NUMBER}" \
  -Djib.to.auth.username="$REG_USER" \
  -Djib.to.auth.password="$REG_PASS"
```

> 💡 Jib 會把相依套件、資源、類別分層，程式碼變更時只需推送最上層，速度很快。Jib 的帳密參數會出現在行程清單中，正式環境建議改用 `~/.docker/config.json` 或 credential helper。

### 15.4 映像標籤、Digest 與推送

| 原則 | 說明 |
| --- | --- |
| 唯一且不可變的 tag | `<版本>-<commit 短 SHA>` 或 `<建置編號>-<commit 短 SHA>`；registry 設定 tag immutability |
| 以 digest 部署 | 部署清單使用 `image@sha256:...`，避免 tag 被覆寫後部署到不同內容 |
| 一次建置、逐環境晉升 | dev／sit／uat／prod 使用同一個 digest；需要時以 `crane copy` 或 registry replication 複製到正式環境 registry，而不是重新建置 |
| 基底映像 | 使用組織核可的基底映像並固定 digest；以 Renovate／Dependabot 自動更新 |
| 不在映像中放機密 | 建置參數與層歷史可被讀取，機密以 BuildKit `--secret` 掛載 |

### 15.5 在 Kubernetes 上執行 Jenkins controller（Helm 進階設定）

延續 [3.6 Kubernetes（Helm）部署](#36-kuberneteshelm部署) 的基本安裝，正式環境還需要以下設定：

```yaml
controller:
  image:
    tag: "2.580.1-lts-jdk21"
  numExecutors: 0
  javaOpts: >-
    -XX:InitialRAMPercentage=50 -XX:MaxRAMPercentage=70
    -XX:+UseG1GC -XX:+UseStringDeduplication
    -Duser.timezone=Asia/Taipei
  resources:
    requests:
      cpu: "2"
      memory: 8Gi
    limits:
      memory: 8Gi
  # 機密以 Kubernetes Secret 掛載到 /run/secrets，JCasC 以 ${<secret>-<key>} 引用
  additionalExistingSecrets:
    - name: jenkins-casc-secrets
      keyName: gitlab-ci-token
    - name: jenkins-casc-secrets
      keyName: sonar-token
  JCasC:
    defaultConfig: true
    configScripts:
      tools: |
        tool:
          git:
            installations:
              - name: "Default"
                home: "git"
  sidecars:
    configAutoReload:
      enabled: true       # ConfigMap 變更後自動重新載入 JCasC
  prometheus:
    enabled: true         # 建立 ServiceMonitor，抓取 /prometheus
    scrapeInterval: 60s
  podSecurityContextOverride:
    runAsUser: 1000
    runAsNonRoot: true
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  nodeSelector:
    workload: platform
  priorityClassName: platform-critical

persistence:
  enabled: true
  storageClass: fast-ssd
  size: 300Gi

networkPolicy:
  enabled: true
```

| 項目 | 建議 |
| --- | --- |
| JVM 記憶體 | 以 `MaxRAMPercentage` 依容器 limit 計算 heap；memory requests 等於 limits，避免被驅逐 |
| 儲存 | `ReadWriteOnce` 的 SSD 類 StorageClass；啟用 VolumeSnapshot 作為備份手段之一（20.1） |
| 排程 | 以 `nodeSelector`／`priorityClassName` 放在平台專用節點，避免與建置 Pod 搶資源 |
| JCasC 機密 | `additionalExistingSecrets` 掛載的鍵在 JCasC 中以 `${<secret 名稱>-<key>}` 引用，例如 `${jenkins-casc-secrets-sonar-token}` |
| 升級 | 先更新 `plugins.txt`／`installPlugins` 與映像 tag，在預備環境以 `helm upgrade --dry-run` 與實際部署驗證（20.3） |
| Ingress | 只對 webhook 路徑開放外部入口時，使用 chart 的 `secondaryingress` 設定 |

### 15.6 本章重點

- 不要掛載 `docker.sock`；Kubernetes 上以 BuildKit rootless 建置映像，純 Java 專案可用 Jib
- Kaniko 原專案已封存，新導入改用 BuildKit 或 Buildah
- 映像以唯一 tag 推送、以 digest 部署並逐環境晉升
- Helm 部署 controller 時固定映像版本、以 Secret 掛載 JCasC 機密，並啟用 ServiceMonitor

## 16. 部署策略與環境管理

### 16.1 環境與晉升模型

```mermaid
flowchart LR
    B["建置一次<br/>image@sha256:abc"] --> DEV[dev<br/>自動部署]
    DEV -->|自動測試通過| SIT[sit<br/>自動部署]
    SIT -->|整合測試通過| UAT[uat<br/>核准後部署]
    UAT -->|驗收通過＋變更核准| PROD[prod<br/>核准後部署<br/>Canary／Blue-Green]
```

| 原則 | 說明 |
| --- | --- |
| **一次建置、逐環境晉升** | 所有環境部署同一個映像 digest 或產物版本；環境差異只在設定（Helm values、ConfigMap、Secret） |
| 環境設定與程式碼分離 | 每個環境的設定放在部署 repository（GitOps）或 Helm values 檔，機密由 Vault／External Secrets 提供 |
| 越接近正式環境，控管越嚴 | dev 自動部署；uat／prod 需要核准、限定 agent、限定憑證 folder |
| 部署可追溯 | 記錄「哪個 commit、哪個 digest、誰核准、何時部署到哪裡」（16.2、21.6） |
| 部署可回復 | 每次部署都要有明確的回滾方式並定期演練（16.7） |

### 16.2 人工核准與職責分離

```groovy
pipeline {
    agent none
    options {
        disableResume()   // controller 重啟後不自動恢復，避免核准後重複部署
    }
    stages {
        stage('Approve PROD') {
            options {
                timeout(time: 4, unit: 'HOURS')
            }
            input {
                message '核准部署 payment-api 到正式環境'
                ok '核准部署'
                submitter 'payments-release-managers,cab-approvers'
                submitterParameter 'APPROVER'
                parameters {
                    string(name: 'CHANGE_TICKET', defaultValue: '', description: '變更單號（例如 CHG-2026-1234）')
                }
            }
            steps {
                script {
                    if (!(env.CHANGE_TICKET ==~ /CHG-\d{4}-\d+/)) {
                        error "變更單號格式錯誤：${env.CHANGE_TICKET}"
                    }
                    def causes = currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause')
                    def triggeredBy = causes ? causes[0].userId : null
                    if (triggeredBy && env.APPROVER == triggeredBy) {
                        error '觸發者不得核准自己的部署（職責分離）'
                    }
                }
                echo "核准人：${APPROVER}，變更單：${CHANGE_TICKET}"
            }
        }
    }
}
```

| 控制項 | 做法 |
| --- | --- |
| 指定核准者 | `submitter` 使用群組（LDAP／SSO 群組），不要寫個人帳號 |
| 職責分離 | 開發者不能核准自己的變更；上例以 `currentBuild.getBuildCauses()` 取得手動觸發者並與核准人比對；更嚴謹的做法是由核准系統（ITSM）的 API 驗證變更單狀態與核准人 |
| 等待逾時 | stage 層級 `timeout`，逾時視為不核准（ABORTED） |
| 不占用 executor | stage 層級 `input` 在配置 agent 前等待 |
| 稽核紀錄 | 核准人、時間、變更單號寫入建置描述（`currentBuild.description`）並送到集中記錄（[17.10 稽核與集中記錄](#1710-稽核與集中記錄)） |

> 💡 與 ITSM（ServiceNow、Jira Service Management）整合時，常見做法是由 Pipeline 呼叫 ITSM API 建立或查詢變更單，取代人工輸入；核准結果以 webhook 或輪詢回到 Jenkins。

### 16.3 部署到 Kubernetes

**Helm（4.x）**：

```bash
#!/usr/bin/env bash
set -euo pipefail
# 以 digest 部署；--rollback-on-failure 取代 Helm 3 的 --atomic（Helm 4 已標示 deprecated）
helm upgrade --install payment-api oci://harbor.example.internal/charts/payment-api \
  --version "${CHART_VERSION}" \
  --namespace payments-sit \
  --values "deploy/values-sit.yaml" \
  --set image.repository=harbor.example.internal/payments/payment-api \
  --set image.digest="${IMAGE_DIGEST}" \
  --rollback-on-failure \
  --wait \
  --timeout 10m
helm history payment-api --namespace payments-sit --max 5
```

| 旗標 | Helm 4.3 行為 |
| --- | --- |
| `--wait` | 單獨使用代表 `watcher` 策略（以 kstatus 判斷資源就緒）；未指定時為 `hookOnly` |
| `--rollback-on-failure` | 失敗時自動回滾到上一個成功版本，並預設啟用 `--wait=watcher`；`--atomic` 仍可用但已 deprecated |
| `--timeout` | 等待的上限（預設 5 分鐘） |

**kubectl／Kustomize**：

```bash
#!/usr/bin/env bash
set -euo pipefail
cd deploy/overlays/sit
kustomize edit set image payment-api="harbor.example.internal/payments/payment-api@${IMAGE_DIGEST}"
kubectl apply -k . --server-side --field-manager=jenkins
kubectl rollout status deployment/payment-api -n payments-sit --timeout=10m
```

> ⚠️ 部署憑證（kubeconfig）應對應到**只能操作該 namespace** 的 ServiceAccount（RBAC），並以 Secret file 憑證保存在對應環境的 folder。不要讓 Jenkins 使用叢集管理員的 kubeconfig。

### 16.4 GitOps：Jenkins 負責 CI，Argo CD 負責 CD

在 GitOps 模式中，Jenkins 不直接連線正式叢集，而是**更新部署 repository** 中的映像版本，由叢集內的 Argo CD（v3.5）或 Flux 自動同步：

```mermaid
sequenceDiagram
    participant J as Jenkins
    participant R as Registry
    participant G as GitOps repo（deploy-config）
    participant A as Argo CD
    participant K as Kubernetes
    J->>R: 推送映像，取得 digest
    J->>G: 建立 MR：更新 overlays/prod 的 image digest
    G->>G: 審查與核准（取代 Jenkins input）
    G-->>A: 合併後觸發同步
    A->>K: 套用資源
    A-->>J: （選用）以通知或 API 回報同步結果
```

```groovy
pipeline {
    agent { label 'linux' }
    parameters {
        string(name: 'IMAGE_DIGEST', defaultValue: '', description: 'sha256:...')
    }
    stages {
        stage('Update GitOps repo') {
            steps {
                dir('deploy-config') {
                    git url: 'https://gitlab.example.internal/payments/deploy-config.git',
                        branch: 'main', credentialsId: 'gitlab-gitops-bot'
                    withCredentials([usernamePassword(credentialsId: 'gitlab-gitops-bot',
                                                      usernameVariable: 'GIT_USER', passwordVariable: 'GIT_TOKEN')]) {
                        sh '''
                            set -euo pipefail
                            BRANCH="release/payment-api-${BUILD_NUMBER}"
                            git checkout -b "$BRANCH"
                            cd overlays/prod
                            kustomize edit set image payment-api="harbor.example.internal/payments/payment-api@${IMAGE_DIGEST}"
                            cd ../..
                            git -c user.name="jenkins-bot" -c user.email="jenkins-bot@example.internal" \
                              commit -am "payment-api: ${IMAGE_DIGEST} (build ${BUILD_NUMBER})"
                            git push "https://${GIT_USER}:${GIT_TOKEN}@gitlab.example.internal/payments/deploy-config.git" "$BRANCH" \
                              -o merge_request.create -o merge_request.target=main \
                              -o merge_request.title="Deploy payment-api build ${BUILD_NUMBER} to prod"
                        '''
                    }
                }
            }
        }
    }
}
```

| 比較 | Jenkins 直接部署 | GitOps（Argo CD／Flux） |
| --- | --- | --- |
| 正式叢集憑證 | 存放在 Jenkins | 不需要（叢集主動拉取） |
| 核准方式 | Jenkins `input` | GitOps repo 的 MR 審查與 protected branch |
| 漂移偵測 | 無 | 持續比對並可自動修正 |
| 回滾 | 重新執行舊版本部署 | `git revert` |
| 適用 | 傳統 VM、尚未導入 GitOps 的環境 | ✅ Kubernetes 正式環境的建議模式 |

> 💡 `git push -o merge_request.create` 是 GitLab 的 push option；GitHub 可改用 `gh pr create`。

### 16.5 Blue-Green 部署

Blue-Green 同時保留兩套完整環境，切換流量即完成部署，回滾只需切回。

```mermaid
flowchart LR
    U[使用者] --> S[Service／Ingress<br/>selector: version=green]
    S --> G[Green v1.5<br/>新版本]
    S -. 切換前 .-> B[Blue v1.4<br/>舊版本，保留供回滾]
```

```bash
#!/usr/bin/env bash
set -euo pipefail
NS=payments-prod
NEW_COLOR="${NEW_COLOR:?需要 NEW_COLOR（blue 或 green）}"

# 1. 部署新顏色的 Deployment（不接流量）
helm upgrade --install "payment-api-${NEW_COLOR}" ./chart -n "$NS" \
  --set color="${NEW_COLOR}" --set image.digest="${IMAGE_DIGEST}" --wait --timeout 10m

# 2. 對新版本執行冒煙測試（透過不對外的 preview Service）
./smoke-test.sh "http://payment-api-${NEW_COLOR}-preview.${NS}.svc.cluster.local:8080"

# 3. 切換正式 Service 的 selector
kubectl -n "$NS" patch service payment-api \
  -p "{\"spec\":{\"selector\":{\"app\":\"payment-api\",\"color\":\"${NEW_COLOR}\"}}}"
```

> ⚠️ Blue-Green 需要兩倍的運算資源，且資料庫 schema 必須同時相容新舊版本（先擴充、後收斂的 expand／contract 遷移）。

### 16.6 Canary 部署

Canary 先把小比例流量導向新版本，觀察指標後逐步擴大。✅ 建議以 **Argo Rollouts**（v1.10）或 Flagger 實作流量切分與自動分析，Jenkins 只負責觸發與等待結果：

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: payment-api
  namespace: payments-prod
spec:
  replicas: 10
  selector:
    matchLabels:
      app: payment-api
  strategy:
    canary:
      steps:
        - setWeight: 10
        - pause: { duration: 10m }
        - analysis:
            templates:
              - templateName: http-error-rate
        - setWeight: 50
        - pause: { duration: 15m }
        - setWeight: 100
  template:
    metadata:
      labels:
        app: payment-api
    spec:
      containers:
        - name: payment-api
          image: harbor.example.internal/payments/payment-api@sha256:0000000000000000000000000000000000000000000000000000000000000000
```

```groovy
pipeline {
    agent { label 'deploy-prod' }
    stages {
        stage('Canary') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-prod-payments', variable: 'KUBECONFIG')]) {
                    sh '''
                        set -euo pipefail
                        kubectl argo rollouts set image payment-api \
                          payment-api="harbor.example.internal/payments/payment-api@${IMAGE_DIGEST}" -n payments-prod
                        kubectl argo rollouts status payment-api -n payments-prod --timeout 60m
                    '''
                }
            }
        }
    }
    post {
        failure {
            withCredentials([file(credentialsId: 'kubeconfig-prod-payments', variable: 'KUBECONFIG')]) {
                sh 'kubectl argo rollouts abort payment-api -n payments-prod'
            }
        }
    }
}
```

| 策略 | 資源成本 | 回滾速度 | 風險暴露 | 適用 |
| --- | --- | --- | --- | --- |
| Rolling update（Kubernetes 預設） | 低 | 中 | 全部使用者逐步接觸新版 | 一般服務 |
| Blue-Green | 高（兩倍） | 秒級 | 切換瞬間全部 | 需要瞬間切換、易回滾的服務 |
| Canary | 中 | 秒級 | 小比例 | ✅ 高流量、可觀測性完整的服務 |

### 16.7 回滾

| 情境 | 回滾方式 |
| --- | --- |
| Helm 部署失敗 | `--rollback-on-failure` 自動回滾；手動：`helm rollback payment-api <revision> -n <ns>` |
| GitOps | `git revert` 部署 repository 的提交，由 Argo CD 同步 |
| Argo Rollouts | `kubectl argo rollouts abort`（停在穩定版本）或 `undo` |
| Blue-Green | 切回舊顏色的 selector |
| 資料庫遷移 | 只採用向後相容的遷移；破壞性變更延到下一個版本，並在變更單中寫明回滾計畫 |

✅ 回滾 Pipeline 本身也要以 Jenkinsfile 管理，並每季在預備環境演練一次。

### 16.8 資料庫結構遷移

應用程式部署常伴隨資料庫結構變更。遷移腳本應與程式碼一起版本控制，由 Pipeline 在部署**之前**執行，並遵守「先擴充、後收斂」（expand／contract）原則，讓新舊版本程式都能使用同一個 schema。

| 階段 | 動作 | 範例 |
| --- | --- | --- |
| 擴充（expand） | 只新增：新欄位（可為 NULL 或有預設值）、新資料表、新索引 | `ALTER TABLE payment ADD COLUMN channel VARCHAR(20) NULL` |
| 部署新版程式 | 新程式同時寫入新舊欄位，讀取新欄位 | |
| 資料回填 | 批次把舊資料轉到新欄位 | 以獨立的維運 Pipeline 分批執行 |
| 收斂（contract） | 確認不再需要回滾到舊版後，才移除舊欄位 | 下一個版本再執行 |

```groovy
pipeline {
    agent { label 'deploy' }
    parameters {
        choice(name: 'TARGET_ENV', choices: ['sit', 'uat'], description: '目標環境')
    }
    stages {
        stage('DB Migrate') {
            agent {
                docker {
                    image 'flyway/flyway:13.9.0'
                    args '--entrypoint=""'
                    label 'deploy && docker'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: "db-migrator-payments-${params.TARGET_ENV}",
                                                  usernameVariable: 'FLYWAY_USER', passwordVariable: 'FLYWAY_PASSWORD')]) {
                    sh '''
                        set -eu
                        export FLYWAY_URL="jdbc:postgresql://pg-${TARGET_ENV}.example.internal:5432/payments"
                        flyway -locations=filesystem:db/migration info
                        flyway -locations=filesystem:db/migration -validateMigrationNaming=true validate
                        flyway -locations=filesystem:db/migration migrate
                    '''
                }
            }
        }
        stage('Deploy App') {
            steps {
                echo "部署應用程式到 ${params.TARGET_ENV}（16.3）"
            }
        }
    }
}
```

| 原則 | 說明 |
| --- | --- |
| 遷移帳號與應用程式帳號分開 | 只有遷移帳號具有 DDL 權限，憑證放在對應環境的 folder |
| 先 `validate` 再 `migrate` | 確認已執行的腳本沒有被修改（checksum） |
| 不可修改已發佈的遷移腳本 | 修正一律以新的版本號腳本處理 |
| 正式環境另行核准 | 大型資料表的 DDL 可能鎖表，需評估執行時間並安排維護窗口 |
| 回滾策略 | 優先以「向前修正」（新的遷移腳本）處理；破壞性變更延到收斂階段 |

### 16.9 部署到 VM 與傳統主機

尚未容器化的應用，建議由 Jenkins 呼叫 **Ansible**，而不是在 Pipeline 中撰寫大量 SSH 指令：

```groovy
pipeline {
    agent { label 'deploy' }
    stages {
        stage('Deploy to VMs') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ansible-deploy-key',
                                                   keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                    sh '''
                        set -euo pipefail
                        ansible-playbook -i inventories/sit/hosts.yml deploy.yml \
                          --private-key "$SSH_KEY" -u "$SSH_USER" \
                          -e "app_version=${BUILD_NUMBER}" \
                          --diff
                    '''
                }
            }
        }
    }
}
```

> 💡 Ansible playbook 以 `serial` 參數控制每批更新的主機數，搭配負載平衡器的摘除與加回，即可實作 VM 環境的滾動部署。

### 16.10 本章重點

- 一次建置、以 digest 逐環境晉升；環境差異只在設定
- 正式部署使用 stage 層級 `input`＋`timeout`＋群組核准，並保留職責分離與稽核紀錄
- Helm 4 改用 `--rollback-on-failure`；Kubernetes 正式環境優先採用 GitOps，Jenkins 不持有正式叢集憑證
- Canary 以 Argo Rollouts／Flagger 實作，Jenkins 負責觸發與等待結果；回滾流程要定期演練
- 資料庫遷移在部署前執行，遵守 expand／contract 原則，遷移帳號與應用程式帳號分開

## 17. 安全強化

### 17.1 威脅模型

Jenkins 同時擁有**原始碼、建置環境、各環境的部署憑證**，是攻擊者橫向移動與供應鏈攻擊的高價值目標。

```mermaid
flowchart TB
    subgraph 外部
        A1[未授權存取 UI／API]
        A2[惡意 PR／fork]
        A3[有漏洞的 plugin]
    end
    subgraph 內部
        A4[過度授權的帳號]
        A5[Script Console／受信任 Library 濫用]
        A6[憑證外洩]
    end
    A1 --> J[Jenkins Controller]
    A2 --> AG[Agent 上執行任意程式碼]
    A3 --> J
    A4 --> J
    A5 --> J
    AG --> A6
    J --> A6
    A6 --> T[正式環境／原始碼／制品庫遭入侵]
```

| 威脅 | 主要控制 | 章節 |
| --- | --- | --- |
| 未授權存取 | SSO＋MFA、關閉匿名讀取、反向代理與網路分段 | 17.2、3.8 |
| 權限過大 | 最小權限的 Matrix／Role-based 授權，管理員人數最少化 | 17.3 |
| 建置以 SYSTEM 身分執行 | Authorize Project（建置以觸發者身分執行） | 17.4 |
| 惡意 Pipeline 程式碼 | 分支／fork 信任設定、agent 隔離、憑證 folder 化 | 8.6、14.6、7.2 |
| Controller 被入侵 | built-in node 0 executor、agent → controller 安全、Script Approval | 17.5、17.7 |
| Web 攻擊（XSS／CSRF） | CSRF、CSP、Safe HTML、Resource Root URL | 17.6 |
| Plugin 漏洞 | 安全公告處理流程、精簡 plugin | 17.9、第 5 章 |
| 無法追溯 | Audit Trail、集中記錄 | 17.10 |

### 17.2 驗證（Security Realm）

| 方式 | Plugin | 建議 |
| --- | --- | --- |
| **OpenID Connect（OIDC）** | OpenId Connect Authentication（`oic-auth`） | ✅ 首選：對接 Keycloak、Microsoft Entra ID、Okta 等，由 IdP 負責 MFA |
| SAML 2.0 | SAML | 已有 SAML IdP（ADFS 等）時使用 |
| LDAP／Active Directory | LDAP、Active Directory | 沒有 SSO 時的企業目錄整合；務必使用 LDAPS |
| Jenkins 自有使用者資料庫 | Core | 只用於實驗環境或緊急帳號；2.516.1 起密碼上限 72 bytes（bcrypt） |

**OIDC 範例**（Keycloak；已以 2.580.1＋`oic-auth` 4.718 驗證）：

```yaml
jenkins:
  securityRealm:
    oic:
      clientId: "jenkins"
      clientSecret: "${oidc_client_secret}"
      serverConfiguration:
        wellKnown:
          wellKnownOpenIDConfigurationUrl: "https://sso.example.internal/realms/corp/.well-known/openid-configuration"
          scopesOverride: "openid profile email groups"
      userNameField: "preferred_username"
      fullNameFieldName: "name"
      emailFieldName: "email"
      groupsFieldName: "groups"
      logoutFromOpenidProvider: true
      postLogoutRedirectUrl: "https://jenkins.example.internal/"
      properties:
        - pkce
        - escapeHatch:
            username: "break-glass-admin"
            secret: "${oidc_escape_hatch_password}"
            group: "jenkins-admins"
```

| 設定 | 說明 |
| --- | --- |
| `pkce` | 啟用 PKCE，防止授權碼攔截 |
| `groupsFieldName` | IdP 必須在 ID token 或 userinfo 中提供群組 claim，Jenkins 授權才能以群組設定 |
| `escapeHatch` | 「破窗」緊急帳號：IdP 故障時仍能登入。密碼存放在保險箱，使用後立即輪替並檢討 |
| `logoutFromOpenidProvider` | 登出時一併結束 IdP session |

**LDAP 範例**：

```yaml
jenkins:
  securityRealm:
    ldap:
      configurations:
        - server: "ldaps://ldap.example.internal:636"
          rootDN: "dc=example,dc=internal"
          managerDN: "cn=svc-jenkins-bind,ou=service,dc=example,dc=internal"
          managerPasswordSecret: "${ldap_bind_password}"
          userSearchBase: "ou=people"
          userSearch: "uid={0}"
          groupSearchBase: "ou=groups"
          groupSearchFilter: "(&(objectClass=groupOfNames)(cn={0}))"
          groupMembershipStrategy:
            fromGroupSearch:
              filter: "(&(objectClass=groupOfNames)(member={0}))"
          displayNameAttributeName: "displayName"
          mailAddressAttributeName: "mail"
      cache:
        size: 200
        ttl: 300
      userIdStrategy: "caseInsensitive"
      groupIdStrategy: "caseInsensitive"
```

> 📌 2.479.1 升級到 Spring Security 6 時，LDAP plugin 必須同步升級到相容版本（官方升級指南）。升級 core 前務必先更新 LDAP、Active Directory、SAML、OIDC 等驗證 plugin，否則可能無法登入（[20.3 升級程序](#203-升級程序)）。

### 17.3 授權策略

| 策略 | Plugin | 適用 |
| --- | --- | --- |
| Matrix-based security | Matrix Authorization Strategy | 中小型組織；搭配 **folder 層級的 matrix** 給團隊權限 |
| Role-based Strategy | Role-based Authorization Strategy | 大型組織；以正規表示式把 Job 分組並對應角色 |
| Logged-in users can do anything | Core | ❌ 只用於個人實驗環境 |
| Anyone can do anything／Legacy mode | Core | ❌ 不使用 |

**最小權限原則**：

| 角色 | 權限 |
| --- | --- |
| 平台管理員（2–4 人） | `Overall/Administer` |
| 所有登入使用者 | `Overall/Read`（必要時加 `Job/Discover`） |
| 團隊開發者 | 該團隊 folder 的 `Job/Read`、`Job/Build`、`Job/Cancel`、`Job/Workspace`、`Run/Replay` |
| 發佈管理者 | `prod` 子 folder 的 `Job/Read`、`Job/Build`；`input` 核准 |
| 唯讀稽核 | `Overall/Read`、`Job/Read`、`Job/ExtendedRead`（檢視設定但不可修改） |

> ⚠️ `Job/Configure` 與 `Run/Replay` 都能改變 Pipeline 實際執行的程式碼，等同取得該 Job 可用的所有憑證。正式部署 Job 不授予這兩個權限；Multibranch 的 Pipeline 內容由 Git 審查流程控管。

**Role-based Strategy 範例**：

```yaml
jenkins:
  authorizationStrategy:
    roleBased:
      roles:
        global:
          - name: "admin"
            description: "Jenkins 平台管理員"
            permissions:
              - "Overall/Administer"
            entries:
              - group: "jenkins-admins"
          - name: "reader"
            description: "所有登入使用者"
            permissions:
              - "Overall/Read"
            entries:
              - group: "authenticated"
        items:
          - name: "payments-developer"
            description: "Payments 團隊：可執行與檢視（不含 prod）"
            pattern: "payments/(?!prod/).*"
            permissions:
              - "Job/Read"
              - "Job/Build"
              - "Job/Cancel"
              - "Job/Workspace"
              - "Run/Replay"
            entries:
              - group: "payments-devs"
          - name: "payments-release"
            description: "Payments 正式部署"
            pattern: "payments/prod/.*"
            permissions:
              - "Job/Read"
              - "Job/Build"
            entries:
              - group: "payments-release-managers"
```

**Matrix 搭配 folder 權限**（全域只給讀取，團隊權限設在 folder，以 Job DSL 建立）：

```groovy
// Job DSL：建立 prod 子 folder，阻斷繼承並只授權發佈管理者
folder('payments')
folder('payments/prod') {
    properties {
        authorizationMatrix {
            inheritanceStrategy {
                nonInheriting()
            }
            entries {
                group {
                    name('payments-release-managers')
                    permissions(['Job/Read', 'Job/Build'])
                }
                group {
                    name('jenkins-admins')
                    permissions(['Job/Read', 'Job/Build', 'Job/Configure', 'Job/Cancel'])
                }
            }
        }
    }
}
```

### 17.4 建置的執行身分（Authorize Project）

預設情況下，建置以 **SYSTEM** 身分執行，可以觸發任何 Job、讀取任何 Job 的產物。安裝 **Authorize Project** plugin 並設定全域策略，讓建置以「觸發建置的使用者」身分執行：

```yaml
security:
  queueItemAuthenticator:
    authenticators:
      - global:
          strategy: "triggeringUsersAuthorizationStrategy"
```

| 效果 | 說明 |
| --- | --- |
| `build job: '...'` | 只能觸發觸發者有 `Job/Build` 權限的 Job |
| `copyArtifacts` | 只能複製觸發者看得到的 Job 產物 |
| User 範圍憑證 | 可以使用觸發者自己的 User 憑證 |

> 💡 由 webhook 或排程觸發的建置沒有「使用者」，會以匿名身分執行，可能因權限不足失敗。為這類建置在 Job 層級設定「Run as specific user」（服務帳號），或為匿名身分授予最小必要權限。

### 17.5 Controller 與 Agent 隔離

| 控制 | 設定 |
| --- | --- |
| Built-in node 不執行建置 | `jenkins.numExecutors: 0` |
| Agent → Controller 存取控制 | 2.326 起永遠啟用，不得以系統屬性停用 |
| 停用不使用的 TCP agent port | 全部使用 WebSocket／SSH 時：`jenkins.slaveAgentPort: -1` |
| Agent 依信任分級 | [14.6 Agent 安全與隔離](#146-agent-安全與隔離) |
| Controller 網路 | 只有反向代理可連入 8080；controller 對外連線限制在 SCM、update center（或內部鏡像）、IdP、agent |

### 17.6 Web 安全：CSRF、CSP、Markup 與 Resource Root URL

```yaml
jenkins:
  disableRememberMe: true
  markupFormatter:
    rawHtml:
      disableSyntaxHighlighting: false
security:
  apiToken:
    creationOfLegacyTokenEnabled: false
    tokenGenerationOnCreationEnabled: false
    usageStatisticsEnabled: true
  contentSecurityPolicy:
    enforce: true
  gitHostKeyVerificationConfiguration:
    sshHostKeyVerificationStrategy: "knownHostsFileVerificationStrategy"
  globalJobDslSecurityConfiguration:
    useScriptSecurity: true
unclassified:
  resourceRoot:
    url: "https://jenkins-files.example.internal/"
```

| 設定 | 說明 |
| --- | --- |
| CSRF | 預設啟用；2.555.1 起 crumb 不再綁定用戶端 IP，JCasC 不可再設定 `crumbIssuer.standard.excludeClientIPFromCrumb` |
| **Content Security Policy**（2.541.1 起 core 內建） | `contentSecurityPolicy.enforce: true` 啟用強制模式；預設只回報（`Content-Security-Policy-Report-Only`）。啟用前先在預備環境確認所有 plugin 頁面正常；舊的 CSP plugin 需停用或升級到 2.x |
| Markup Formatter | `rawHtml` 是 OWASP Markup Formatter 提供的 **Safe HTML**（會過濾腳本），不是原始 HTML |
| Resource Root URL | 讓建置產物、HTML 報告在獨立網域提供，避免惡意檔案在 Jenkins 網域執行腳本 |
| `disableRememberMe` | 停用「記住我」，session 隨瀏覽器關閉失效（SSO 環境由 IdP 管理 session） |
| Legacy API token | 不允許建立；使用者自行產生具名稱的 token，定期檢視使用統計並撤銷未使用的 token |
| Git host key 驗證 | 使用 known_hosts，避免中間人攻擊 |
| Job DSL script security | 以沙箱執行 Job DSL 腳本（`useScriptSecurity: true`） |

### 17.7 Script Approval 與 Script Console 管控

| 控制 | 做法 |
| --- | --- |
| 預設拒絕 | `security.scriptApproval.approvedSignatures` 以 JCasC 管理，每一項都要有變更紀錄與理由 |
| 定期清理 | 每季檢視已核准的簽章，移除不再使用的項目 |
| Script Console | 只有管理員；操作由 Audit Trail 記錄（`logScriptUsage`） |
| Groovy init scripts（`init.groovy.d`） | 只在映像建置時放入，由 Git 審查；不要在執行中的 controller 上手動新增 |
| 受信任 Shared Library | 寫入權限比照管理員管理（[12.2 設定 Library：受信任與非受信任](#122-設定-library受信任與非受信任)） |

### 17.8 API Token、CLI 與服務帳號

| 用途 | 做法 |
| --- | --- |
| 外部系統呼叫 Jenkins REST API | 建立專用服務帳號（SSO 環境可用本機帳號或 IdP 的 service account），產生具名 API token，只授予必要權限 |
| CLI | 使用 `-webSocket` 或 `-http` 模式＋`-auth @檔案`；SSH CLI 預設停用 |
| Token 管理 | 記錄每個 token 的擁有者、用途、到期日；離職或系統下線時撤銷 |
| 呼叫方式 | API token 透過 HTTP Basic 驗證傳送，**一定要走 HTTPS**；使用 API token 時不需要 CSRF crumb |

> ⚠️ WebSocket 模式的 CLI 需要先設定 Jenkins URL；未設定時握手會回傳 403，回應標頭為 `X-CLI-Error: Jenkins URL is not configured`（2.580.1 實測）。

### 17.9 安全公告與漏洞處理流程

Jenkins 安全團隊以**安全公告（Security Advisory）**發布 core 與 plugin 漏洞，通常在週三發布，並會提前在 `jenkinsci-advisories` 郵件清單預告。2026 年 1–9 月共有 9 次公告，其中 5 次影響 core（2026-02-18、03-18、06-10、08-05、09-02）；例如 2026-06-10 修補了 2.567／LTS 2.555.2 以前可由攻擊者控制的 `config.xml` 觸發的反序列化問題。

```mermaid
flowchart LR
    A[訂閱 jenkinsci-advisories<br/>與安全公告 RSS] --> B[公告發布]
    B --> C[比對 plugins.txt<br/>PIMT --view-security-warnings]
    C --> D{受影響且可利用?}
    D -->|是| E[評估暫時緩解措施<br/>停用 plugin／限制權限]
    E --> F[預備環境更新與測試]
    F --> G[正式環境更新<br/>目標 7 天內]
    D -->|否| H[記錄評估結果<br/>排入例行更新]
    G --> I[更新稽核紀錄]
    H --> I
```

| 嚴重度（CVSS） | 修補目標 |
| --- | --- |
| Critical／High | 7 天內（可被未授權使用者利用者 72 小時內） |
| Medium | 30 天內 |
| Low | 下一次例行更新 |

> 💡 Manage Jenkins 頁面的「Warnings」與 update center 的安全警示會列出已安裝 plugin 的已知漏洞。也可以把 `PIMT --view-security-warnings` 加入每日排程，結果送到資安團隊。

### 17.10 稽核與集中記錄

```yaml
unclassified:
  audit-trail:
    logBuildCause: true
    logCredentialsUsage: true
    displayUserName: true
    pattern: ".*/(?:configSubmit|doDelete|postBuildResult|enable|disable|cancelQueue|stop|toggleLogKeep|doWipeOutWorkspace|createItem|createView|toggleOffline|cancelQuietDown|quietDown|restart|exit|safeExit)/?.*"
    loggers:
      - logFile:
          log: "/var/log/jenkins/audit-%g.log"
          limit: 100
          count: 10
```

| 記錄來源 | 內容 | 保存 |
| --- | --- | --- |
| Audit Trail plugin | 設定變更、建置觸發者、憑證使用、Script Console 使用 | 送到 SIEM，保存期限依法規（21.6） |
| Job Configuration History plugin | Job 與系統設定的差異歷史 | 補充 Audit Trail 的「改了什麼」 |
| 系統記錄（`journalctl`／容器 stdout） | 登入失敗、錯誤 | 集中到 ELK／Loki |
| 建置紀錄 | 誰觸發、誰核准、部署了什麼 | 依保存政策；正式部署紀錄另存到不可竄改的儲存 |

### 17.11 本章重點

- 以 OIDC／SAML 對接 SSO 並由 IdP 負責 MFA，保留一個受控的破窗帳號
- 授權採最小權限：全域只給讀取，團隊權限設在 folder；`Job/Configure` 與 `Run/Replay` 視同憑證存取權
- 以 Authorize Project 讓建置以觸發者身分執行
- 啟用 Content Security Policy 強制模式與 Resource Root URL；停用 legacy API token
- 建立安全公告處理流程，Critical／High 7 天內修補；Audit Trail 記錄送 SIEM

## 18. Configuration as Code（JCasC）與 Job DSL

### 18.1 為何要把 Jenkins 設定程式碼化

| 問題（UI 手動設定） | JCasC＋Job DSL 的解法 |
| --- | --- |
| 設定散落在 `config.xml`，無法審查與追溯 | YAML／Groovy 放在 Git，透過 MR／PR 審查 |
| 預備環境與正式環境設定不一致 | 同一份設定，以變數區分環境 |
| 災難復原要從備份還原整個 `JENKINS_HOME` | 新 controller＋JCasC＋Job DSL 即可重建設定與 Job（建置紀錄另行備份） |
| 新增團隊或專案需要管理員手動操作 | 修改 seed 設定即可自動建立 folder、權限、Multibranch |
| 升級時不清楚哪些設定已棄用 | JCasC 在啟動時檢查並拒絕已棄用的設定 |

```mermaid
flowchart LR
    G[(jenkins-config repo<br/>casc/*.yaml<br/>jobs/*.groovy<br/>plugins.txt)] -->|MR 審查| CI[設定驗證 Pipeline<br/>check 端點／預備環境]
    CI --> IMG[controller 映像<br/>或 Helm values]
    IMG --> C[Jenkins Controller]
    C -->|啟動時套用| J[JCasC：系統設定、憑證、雲端、安全]
    J -->|jobs: 區段| D[Job DSL：folder、Multibranch、Organization Folder]
```

### 18.2 JCasC 基礎

**載入位置**（依序）：

1. 環境變數 `CASC_JENKINS_CONFIG`：單一檔案、目錄（載入其中所有 `.yaml`／`.yml`）或 URL，可用逗號分隔多個來源
2. 系統屬性 `casc.jenkins.config`
3. 預設：`$JENKINS_HOME/jenkins.yaml`

**根層級鍵**：

| 鍵 | 內容 |
| --- | --- |
| `jenkins` | Core 設定：安全領域、授權、節點、雲端、executor、系統訊息、視圖 |
| `credentials` | 系統範圍憑證 |
| `security` | 安全相關的全域設定（API token、CSP、Script Approval、建置授權等） |
| `tool` | 工具安裝（JDK、Maven、Git） |
| `unclassified` | 其餘 plugin 的全域設定（位置、郵件、Shared Library、SonarQube 等） |
| `appearance` | 主題等外觀設定 |
| `jobs` | Job DSL 腳本（需要 Job DSL plugin） |
| `configuration-as-code` | JCasC 本身的行為設定 |

**完整的基礎範例**（含第 3.5 節 Compose 範例需要的 inbound agent 節點）：

```yaml
configuration-as-code:
  deprecated: reject      # 預設值：遇到已棄用設定即中止啟動
  unknown: reject

jenkins:
  systemMessage: "本 Jenkins 由 JCasC 管理（jenkins-config repo），請勿在 UI 修改設定"
  numExecutors: 0
  mode: EXCLUSIVE
  slaveAgentPort: -1
  securityRealm:
    local:
      allowsSignup: false
      users:
        - id: "admin"
          password: "${jenkins_admin_password}"
  authorizationStrategy:
    loggedInUsersCanDoAnything:
      allowAnonymousRead: false
  nodes:
    - permanent:
        name: "agent-1"
        labelString: "linux docker"
        remoteFS: "/home/jenkins/agent"
        numExecutors: 2
        launcher:
          inbound:
            webSocket: true

unclassified:
  location:
    url: "https://jenkins.example.internal/"
    adminAddress: "jenkins-noreply@example.internal"
  timestamper:
    allPipelines: true
  buildDiscarders:
    configuredBuildDiscarders:
      - "jobBuildDiscarder"
      - simpleBuildDiscarder:
          discarder:
            logRotator:
              daysToKeepStr: "60"
              numToKeepStr: "100"
              artifactDaysToKeepStr: "14"
              artifactNumToKeepStr: "10"
```

> 💡 不知道某個設定的 YAML 寫法時，先在預備環境的 UI 設定好，再到 Manage Jenkins → Configuration as Code → **View Configuration**（`/configuration-as-code/viewExport`）匯出對照；`/configuration-as-code/reference` 列出目前安裝的 plugin 支援的所有鍵。匯出結果包含加密後的機密，不能直接提交到 Git。

### 18.3 JCasC 實務

**機密**：YAML 中只寫變數，值由 secret source 提供（[7.6 以 JCasC 管理憑證](#76-以-jcasc-管理憑證)）：

| 來源 | 寫法 | 說明 |
| --- | --- | --- |
| 環境變數 | `${SONAR_TOKEN}` | 簡單，但環境變數可能出現在 System Information 頁面與行程資訊 |
| 檔案（Docker／Kubernetes Secret） | `${sonar_token}` 對應 `/run/secrets/sonar_token` | ✅ 建議；目錄可用環境變數 `SECRETS` 修改 |
| 讀取任意檔案 | `${readFile:/path/to/file}`、`${trim:${readFile:...}}` | 憑證檔、金鑰 |
| Base64 | `${base64:...}`、`${decodeBase64:...}`、`${readFileBase64:...}` | PKCS#12 等二進位檔 |
| Vault／AWS／Azure | 對應的 secret source plugin | 集中管理 |
| 預設值 | `${VAR:-預設值}` | 變數不存在時使用 |
| 跳脫 | `^${NOT_A_VARIABLE}` | 輸出字面上的 `${...}`（例如 Job DSL 腳本中的 Groovy 字串） |

**多檔合併**：`CASC_JENKINS_CONFIG` 指向目錄時，所有檔案會合併。相同的清單項目（例如兩個檔案都定義 `jenkins.nodes`）會**衝突並中止**，因此請依主題切分檔案：

```text
casc/
├── 00-jenkins.yaml          # jenkins: 核心設定
├── 10-security.yaml         # jenkins.securityRealm／authorizationStrategy、security:
├── 20-credentials.yaml      # credentials:
├── 30-clouds.yaml           # jenkins.clouds:
├── 40-tools.yaml            # tool:
├── 50-unclassified.yaml     # unclassified:
└── 90-jobs.yaml             # jobs:
```

**重新載入**：

| 方式 | 指令 |
| --- | --- |
| UI | Manage Jenkins → Configuration as Code → Reload existing configuration |
| CLI | `java -jar jenkins-cli.jar -s https://jenkins.example.internal/ -webSocket -auth @auth reload-jcasc-configuration` |
| REST | `curl -X POST -u "$USER:$TOKEN" https://jenkins.example.internal/configuration-as-code/reload` |
| Kubernetes | Helm chart 的 `configAutoReload` sidecar 監看 ConfigMap 並自動觸發 |
| 驗證（不套用） | `curl -X POST -u "$USER:$TOKEN" --data-binary @jenkins.yaml -H 'Content-Type: application/x-yaml' https://jenkins.example.internal/configuration-as-code/check`；回傳 `[]` 表示通過 |

> ⚠️ Reload 只套用 YAML 中**有出現**的設定；從 YAML 刪除某個設定，不代表 Jenkins 會移除它（例如刪掉的節點仍然存在）。最可靠的方式是以新容器重新啟動 controller，讓所有設定從 YAML 重新產生。

**已棄用設定導致啟動中止**（升級時最常見的問題）：

| 設定 | 自哪一版起 | 處理 |
| --- | --- | --- |
| `jenkins.agentProtocols` | 2.492.1 | 刪除；不需要 TCP agent 時改設 `slaveAgentPort: -1` |
| `jenkins.crumbIssuer.standard.excludeClientIPFromCrumb` | 2.555.1 | 刪除整個 `crumbIssuer` 區段；2.580.1 的 check 端點會回報「Invalid configuration elements」 |
| `jenkins.myViewsTabBar` | 2.516.1／2.528.1 | 刪除，改由使用者個人設定 |
| GitLab Branch Source 的 `secretToken` | plugin 目前版本 | 改用 `webhookSecretCredentialsId`（[8.3 GitLab 整合](#83-gitlab-整合)） |

若需要過渡期，可在 YAML 加上以下設定讓 JCasC 只發出警告（升級完成後應移除）：

```yaml
configuration-as-code:
  deprecated: warn
```

### 18.4 Job DSL

Job DSL 以 Groovy DSL 描述 Job，最適合建立 **folder、Multibranch、Organization Folder、維運用 Pipeline Job** 等「Job 的外殼」；Pipeline 邏輯仍然寫在 Jenkinsfile 中。

**在 JCasC 中直接執行 Job DSL**：

```yaml
jobs:
  - file: /var/jenkins_home/casc/jobs/seed.groovy
  - script: >
      folder('platform-ops') {
        displayName('平台維運')
      }
```

**維運用 Pipeline Job**（Pipeline 內容取自 Git）：

```groovy
// Job DSL：每日驗證備份可還原的 Pipeline Job
folder('platform-ops') {
    displayName('平台維運')
}

pipelineJob('platform-ops/backup-restore-verify') {
    description('每日以最新備份在隔離環境啟動 Jenkins 並執行冒煙測試（第 20 章）')
    logRotator {
        daysToKeep(30)
    }
    properties {
        pipelineTriggers {
            triggers {
                cron {
                    spec('TZ=Asia/Taipei\nH 5 * * *')
                }
            }
        }
    }
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        url('https://gitlab.example.internal/platform/jenkins-ops.git')
                        credentials('gitlab-ci-token')
                    }
                    branch('*/main')
                }
            }
            scriptPath('pipelines/backup-restore-verify.Jenkinsfile')
            lightweight(true)
        }
    }
}
```

**依團隊清單批次建立 folder 與 Organization Folder**：

```groovy
// Job DSL：teams 清單可改為讀取 YAML（readFileFromWorkspace）
def teams = [
    [id: 'payments', name: 'Payments', gitlabGroup: 'payments', devs: 'payments-devs'],
    [id: 'channels', name: 'Channels', gitlabGroup: 'channels', devs: 'channels-devs'],
]

teams.each { t ->
    folder(t.id) {
        displayName(t.name)
        properties {
            authorizationMatrix {
                entries {
                    group {
                        name(t.devs)
                        permissions(['Job/Read', 'Job/Build', 'Job/Cancel', 'Job/Workspace'])
                    }
                }
            }
        }
    }
    organizationFolder("${t.id}/gitlab") {
        displayName("${t.name}（GitLab group）")
        organizations {
            gitLabSCMNavigator {
                projectOwner(t.gitlabGroup)
                serverName('gitlab-internal')
                credentialsId('gitlab-ci-token')
                traits {
                    subGroupProjectDiscoveryTrait()
                    gitLabBranchDiscovery {
                        strategyId(1)
                    }
                    originMergeRequestDiscoveryTrait {
                        strategyId(1)
                    }
                }
            }
        }
        projectFactories {
            workflowMultiBranchProjectFactory {
                scriptPath('Jenkinsfile')
            }
        }
    }
}
```

| 實務要點 | 說明 |
| --- | --- |
| API 參考 | `<Jenkins URL>/plugin/job-dsl/api-viewer/index.html` 列出目前安裝的 plugin 所支援的所有 DSL 方法 |
| Script Security | `useScriptSecurity: true`（17.6）讓 seed 腳本在沙箱中執行 |
| 移除策略 | Seed job 的「Action for removed jobs」設為 `DISABLE` 或 `DELETE`，避免 DSL 移除的 Job 殘留 |
| 測試 | 以 Job DSL 的 Gradle 範例專案或在預備 controller 執行 seed，確認產生的 Job 正確 |

> 💡 本章與第 8、17 章的 Job DSL 範例，都已在本機 Jenkins 2.580.1 以 `DslScriptLoader` 實際執行並成功建立 Job。

### 18.5 在 Kubernetes 上管理設定

| 設定來源 | Helm chart 對應 | 變更流程 |
| --- | --- | --- |
| JCasC YAML | `controller.JCasC.configScripts`（產生 ConfigMap） | 修改 values → `helm upgrade` → sidecar 自動 reload |
| JCasC 機密 | `controller.additionalExistingSecrets`（掛載到 `/run/secrets`） | External Secrets Operator 從 Vault 同步 |
| Plugin | `controller.installPlugins` 或自建映像 | 變更後重新部署（重新啟動 controller） |
| Job | JCasC `jobs:` 區段的 Job DSL | 同 JCasC |

> ⚠️ Plugin 的變更一定需要重新啟動 controller。建議以**自建映像**固定 plugin（[3.5 Docker／Podman 容器部署](#35-dockerpodman-容器部署)），Helm 只負責部署映像，避免每次 Pod 重建都從網路下載 plugin。

### 18.6 Jenkins 設定的 GitOps 流程

```groovy
pipeline {
    agent { label 'linux' }
    environment {
        STAGING_URL = 'https://jenkins-staging.example.internal'
    }
    stages {
        stage('Validate JCasC') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jenkins-staging-api',
                                                  usernameVariable: 'J_USER', passwordVariable: 'J_TOKEN')]) {
                    sh '''
                        set -euo pipefail
                        for f in casc/*.yaml; do
                          result=$(curl -fsS -u "$J_USER:$J_TOKEN" -X POST \
                            -H 'Content-Type: application/x-yaml' --data-binary @"$f" \
                            "$STAGING_URL/configuration-as-code/check")
                          echo "$f: $result"
                          [ "$result" = "[]" ] || exit 1
                        done
                    '''
                }
            }
        }
        stage('Validate plugins') {
            steps {
                sh 'java -jar tools/jenkins-plugin-manager-2.15.0.jar --war tools/jenkins.war -f plugins.txt --no-download --view-security-warnings'
            }
        }
        stage('Build controller image') {
            when {
                branch 'main'
            }
            steps {
                echo '以 BuildKit 建置 controller 映像並推送（第 15 章）'
            }
        }
    }
}
```

> 💡 **漂移偵測**：每日排程匯出正式 controller 的設定（`viewExport`），與 Git 中的 YAML 比對，發現有人在 UI 手動修改時發出告警。

### 18.7 本章重點

- 系統設定用 JCasC、Job 外殼用 Job DSL、建置邏輯用 Jenkinsfile，三者都放在 Git
- 機密以 secret source 注入；依主題切分 YAML 檔案避免合併衝突
- 升級前以 `check` 端點驗證 YAML；2.492.1／2.555.1 起已棄用的 `agentProtocols`、`crumbIssuer` 設定會導致啟動中止
- Plugin 變更以重建映像部署；以每日匯出比對偵測 UI 手動修改

## 19. 監控、日誌、效能與通知

### 19.1 監控什麼

| 層級 | 指標 | 告警條件（建議起點） |
| --- | --- | --- |
| 可用性 | Controller 是否回應、`/login` HTTP 200 | 連續 2 分鐘失敗 |
| 佇列 | 佇列長度、卡住的項目、等待時間 | 佇列 > 20 持續 15 分鐘；任何項目 stuck |
| 容量 | Executor 使用率、上線 agent 數 | 使用率 > 90% 持續 30 分鐘；agent 離線 |
| JVM | Heap 使用率、GC 時間、執行緒數、死結 | Old Gen 使用率 > 85%；GC 時間占比 > 10%；任何 deadlock |
| 磁碟 | `JENKINS_HOME` 可用空間 | < 20% 警告、< 10% 緊急 |
| 建置成效 | 成功率、平均建置時間、失敗類型 | 主分支連續失敗；建置時間較基準增加 50% |
| 健康檢查 | Metrics plugin 健康檢查分數 | 分數 < 1 |
| 安全 | 有安全警示的 plugin 數、登入失敗 | > 0 |

### 19.2 Prometheus metrics plugin

Prometheus metrics plugin（860.v532442b_44e9a_）在 `/prometheus/` 提供 Prometheus 格式的指標。以下指標名稱取自本機 Jenkins 2.580.1 實際抓取的結果：

| 類別 | 指標 |
| --- | --- |
| 可用性 | `default_jenkins_up`、`default_jenkins_uptime`、`default_jenkins_version_info` |
| 佇列 | `jenkins_queue_size_value`、`jenkins_queue_buildable_value`、`jenkins_queue_blocked_value`、`jenkins_queue_stuck_value`、`jenkins_queue_pending_value` |
| Executor／節點 | `jenkins_executor_count_value`、`jenkins_executor_in_use_value`、`jenkins_executor_free_value`、`jenkins_node_online_value`、`jenkins_node_offline_value`、`default_jenkins_executors_queue_length` |
| 建置計數 | `jenkins_runs_success_total`、`jenkins_runs_failure_total`、`jenkins_runs_unstable_total`、`jenkins_runs_aborted_total` |
| 等待與執行時間 | `jenkins_job_queuing_duration`、`jenkins_job_building_duration`、`jenkins_job_total_duration`（summary） |
| 每個 Job 的建置 | `default_jenkins_builds_duration_milliseconds_summary`、`default_jenkins_builds_last_build_result_ordinal` 等（`default_jenkins_builds_*`） |
| 健康檢查 | `jenkins_health_check_score`、`jenkins_health_check_count` |
| Plugin | `jenkins_plugins_active`、`jenkins_plugins_failed`、`jenkins_plugins_withUpdate` |
| 磁碟 | `default_jenkins_file_store_available_bytes`、`default_jenkins_file_store_capacity_bytes`、`default_jenkins_disk_usage_bytes`（需要 CloudBees Disk Usage Simple plugin） |
| JVM | `vm_memory_heap_usage`、`vm_gc_*`、`vm_deadlock_count`、`jvm_memory_bytes_used`、`jvm_threads_current` |

**JCasC 設定**：

```yaml
unclassified:
  prometheusConfiguration:
    path: "prometheus"
    useAuthenticatedEndpoint: true
    defaultNamespace: "default"
    collectingMetricsPeriodInSeconds: 120
    collectDiskUsage: true
    collectNodeStatus: true
    countSuccessfulBuilds: true
    countFailedBuilds: true
    countUnstableBuilds: true
    countAbortedBuilds: true
    countNotBuiltBuilds: true
    perBuildMetrics: false
    processingDisabledBuilds: false
```

> ⚠️ `useAuthenticatedEndpoint: true` 時，抓取帳號需要 `Metrics/View` 權限，Prometheus 以 basic auth（服務帳號＋API token）抓取。不開啟驗證時 `/prometheus/` 會公開所有 Job 名稱與建置資訊，只能在網路層嚴格限制來源。`perBuildMetrics` 會為每次建置產生時間序列，大型實例應保持關閉以避免高基數。

**Prometheus 抓取設定**：

```yaml
scrape_configs:
  - job_name: jenkins
    metrics_path: /prometheus/
    scheme: https
    basic_auth:
      username: svc-prometheus
      password_file: /etc/prometheus/secrets/jenkins-api-token
    static_configs:
      - targets: ["jenkins.example.internal"]
```

**告警規則範例**（PromQL）：

```yaml
groups:
  - name: jenkins
    rules:
      - alert: JenkinsDown
        expr: up{job="jenkins"} == 0 or default_jenkins_up == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Jenkins controller 無法抓取或未就緒"
      - alert: JenkinsQueueBacklog
        expr: jenkins_queue_size_value > 20
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "建置佇列持續累積（{{ $value }} 個項目）"
      - alert: JenkinsQueueStuck
        expr: jenkins_queue_stuck_value > 0
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "有建置卡在佇列中（label 無對應 agent 或 cloud 無法建立 Pod）"
      - alert: JenkinsExecutorSaturation
        expr: jenkins_executor_in_use_value / clamp_min(jenkins_executor_count_value, 1) > 0.9
        for: 30m
        labels:
          severity: warning
        annotations:
          summary: "Executor 使用率超過 90%"
      - alert: JenkinsDiskLow
        expr: default_jenkins_file_store_available_bytes / default_jenkins_file_store_capacity_bytes < 0.1
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "JENKINS_HOME 磁碟可用空間低於 10%"
      - alert: JenkinsHealthCheckFailed
        expr: jenkins_health_check_score < 1
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Jenkins 健康檢查未全部通過"
```

> 💡 Kubernetes 上以 Helm chart 的 `controller.prometheus.enabled: true` 建立 ServiceMonitor（[15.5 在 Kubernetes 上執行 Jenkins controller（Helm 進階設定）](#155-在-kubernetes-上執行-jenkins-controllerhelm-進階設定)）。Grafana 儀表板設計與 PromQL 細節請參考姊妹手冊《Prometheus與Grafana教學手冊》。

### 19.3 OpenTelemetry：Pipeline 追蹤

OpenTelemetry plugin 把每次建置轉成**分散式追蹤（trace）**：Pipeline 是根 span，每個 stage、step 是子 span，可在 Jaeger、Grafana Tempo、Elastic 中分析哪個步驟最慢、失敗集中在哪裡。

```yaml
unclassified:
  openTelemetry:
    endpoint: "http://otel-collector.observability.svc:4317"
    serviceName: "jenkins"
    serviceNamespace: "ci"
    exportOtelConfigurationAsEnvironmentVariables: true
    ignoredSteps: "dir,echo,isUnix,pwd,properties"
    authentication:
      noAuthentication: {}
    observabilityBackends:
      - grafana:
          grafanaBaseUrl: "https://grafana.example.internal"
          grafanaOrgId: "1"
          tempoDataSourceIdentifier: "tempo"
```

| 功能 | 說明 |
| --- | --- |
| 建置追蹤 | 每個 stage／step 的開始、結束時間與結果 |
| 環境變數傳遞 | `exportOtelConfigurationAsEnvironmentVariables: true` 把 `OTEL_EXPORTER_OTLP_ENDPOINT`、`TRACEPARENT` 傳給建置，讓 Maven（OTel Maven extension）、測試程式的 span 串接到同一個 trace |
| 指標 | 同時輸出 Jenkins 的 OTel 指標（可與 Prometheus plugin 二擇一） |
| 日誌 | 可設定把建置主控台記錄送到 Loki／Elasticsearch，減輕 controller 磁碟負擔 |

> 💡 Collector 的部署與設定見《OpenTelemetry教學手冊》。

### 19.4 日誌

| 日誌 | 位置 | 處理方式 |
| --- | --- | --- |
| 系統記錄 | systemd：`journalctl -u jenkins`；容器：stdout；Windows：`<JENKINS_HOME>\jenkins.err.log` | 送到 ELK／Loki |
| 自訂 log recorder | Manage Jenkins → System Log → Add recorder（例如 `hudson.plugins.git`、`org.csanchez.jenkins.plugins.kubernetes` 設為 FINE） | 只在除錯期間開啟，結束後移除 |
| 建置主控台記錄 | `jobs/<name>/builds/<n>/log` | 依建置保留政策；可經 OTel plugin 外送 |
| 稽核記錄 | Audit Trail（[17.10 稽核與集中記錄](#1710-稽核與集中記錄)） | 送到 SIEM |

### 19.5 JVM 與效能調校

**Controller JVM 參數建議**（Java 21）：

```text
-Xms8g -Xmx8g
-XX:+UseG1GC
-XX:+UseStringDeduplication
-XX:+AlwaysPreTouch
-XX:+ParallelRefProcEnabled
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/var/lib/jenkins/heapdumps
-Xlog:gc*,safepoint:file=/var/log/jenkins/gc.log:time,uptime,level,tags:filecount=10,filesize=20m
-Djava.awt.headless=true
-Duser.timezone=Asia/Taipei
```

| 參數 | 理由 |
| --- | --- |
| `-Xms` 等於 `-Xmx` | 避免 heap 動態擴縮造成停頓；容器中改用 `-XX:MaxRAMPercentage` |
| G1GC | Java 21 預設即為 G1；大 heap 下停頓時間穩定 |
| GC log | 事後分析 Full GC 與停頓的必要資料 |
| Heap dump | OOM 時保留現場；確保磁碟空間足夠（約等於 heap 大小） |

**常見效能問題**：

| 症狀 | 常見原因 | 處理 |
| --- | --- | --- |
| UI 緩慢、CPU 高 | 大量 Pipeline 同時執行複雜 Groovy 邏輯 | 把運算移到 agent（[11.4 Durability 與效能設定](#114-durability-與效能設定)）；檢視 thread dump |
| Heap 持續上升 | 建置紀錄過多、某 plugin 記憶體洩漏 | 縮短建置保留；以 heap dump 分析 |
| 啟動很慢 | Job 與建置紀錄數量龐大 | 清理舊資料、拆分 controller |
| 磁碟 I/O 高 | `MAX_SURVIVABILITY` 加上大量短 step | 一般建置改 `PERFORMANCE_OPTIMIZED`、合併 `sh` 步驟 |
| SCM 掃描拖慢系統 | Organization Folder 頻繁全量掃描 | 以 webhook 為主，週期掃描降為每日 |

### 19.6 建置保留與磁碟管理

| 機制 | 設定 |
| --- | --- |
| Jenkinsfile 的 `buildDiscarder` | `options { buildDiscarder(logRotator(numToKeepStr: '50', artifactNumToKeepStr: '5')) }` |
| **Global Build Discarders**（Manage Jenkins → System） | 全域的預設保留政策，對沒有設定的 Job 也生效（JCasC 範例見 [18.2 JCasC 基礎](#182-jcasc-基礎)） |
| Orphaned Item Strategy | Multibranch／Organization Folder 刪除已不存在的分支 Job（[8.6 Multibranch Pipeline 與 Organization Folder](#86-multibranch-pipeline-與-organization-folder)） |
| Workspace 清理 | `cleanWs()`（`post { cleanup { } }`）；雲端 agent 隨 Pod 銷毀 |
| 產物外移 | 大型產物推送到 Nexus／Artifactory，Jenkins 只保存報告 |
| 重要建置保留 | 正式部署建置以 `keep-build`（CLI）或 UI「Keep this build forever」保留，並另存部署紀錄 |

### 19.7 通知

> 📌 Microsoft 365 Connectors（Office 365 Connector plugin 使用的 Incoming Webhook）已停止服務，Office 365 Connector plugin 也已自 update center 下架。Teams 通知改用 **Teams Workflows**（Power Automate）的 webhook URL，以 Adaptive Card 格式傳送。

```groovy
pipeline {
    agent { label 'linux' }
    stages {
        stage('Build') {
            steps {
                sh './mvnw -B -ntp verify'
            }
        }
    }
    post {
        failure {
            // Email：通知造成失敗的提交者與觸發者
            emailext subject: "[${currentBuild.currentResult}] ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "建置結果：${currentBuild.currentResult}\n詳細資訊：${env.BUILD_URL}",
                     recipientProviders: [culprits(), requestor(), developers()],
                     to: 'team-payments@example.internal'
            // Slack
            slackSend channel: '#payments-ci', color: 'danger',
                      tokenCredentialId: 'slack-bot-token',
                      message: "建置失敗：${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|開啟>)"
        }
        fixed {
            script {
                // Teams Workflows webhook：以 Adaptive Card 傳送
                def card = [
                    type: 'message',
                    attachments: [[
                        contentType: 'application/vnd.microsoft.card.adaptive',
                        content: [
                            '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                            type: 'AdaptiveCard',
                            version: '1.5',
                            body: [[type: 'TextBlock', weight: 'Bolder', text: "建置已恢復：${env.JOB_NAME} #${env.BUILD_NUMBER}"]],
                            actions: [[type: 'Action.OpenUrl', title: '開啟建置', url: env.BUILD_URL]]
                        ]
                    ]]
                ]
                writeFile file: 'teams-card.json', text: groovy.json.JsonOutput.toJson(card)
            }
            withCredentials([string(credentialsId: 'teams-workflow-webhook-payments', variable: 'TEAMS_URL')]) {
                sh 'curl -fsS -H "Content-Type: application/json" -d @teams-card.json "$TEAMS_URL"'
            }
        }
    }
}
```

| 原則 | 說明 |
| --- | --- |
| 只通知需要行動的人 | 失敗通知給造成失敗的提交者（`culprits()`）與觸發者；成功通知通常不需要 |
| 使用 `fixed`／`regression` | 只在狀態改變時通知，減少噪音 |
| Webhook URL 是機密 | 以 Secret text 憑證保存，不寫在 Jenkinsfile |
| 封裝到 Shared Library | 統一訊息格式（[12.4 src 類別與 resources](#124-src-類別與-resources)） |

### 19.8 本章重點

- 以 Prometheus plugin 監控可用性、佇列、executor、磁碟與 JVM，`/prometheus/` 需驗證
- 以 OpenTelemetry plugin 追蹤 Pipeline 各 stage 的時間與失敗
- Controller 以固定 heap 的 G1GC 執行，保留 GC log 與 heap dump
- 以 Global Build Discarders 與 Orphaned Item Strategy 控制磁碟；Teams 通知改用 Workflows webhook

## 20. 備份、升級與高可用

### 20.1 備份策略

把 Jenkins 的資產分成三類，分別用不同方式保護：

| 類別 | 內容 | 保護方式 |
| --- | --- | --- |
| **可由程式碼重建** | 系統設定、雲端、安全、Job 外殼、plugin 清單、Shared Library | Git（JCasC、Job DSL、`plugins.txt`、controller 映像） |
| **需要備份的狀態** | 建置紀錄、測試報告、Job 的下一個建置編號、使用者 API token、folder 憑證、`secrets/` | 檔案或快照備份（本節） |
| **不需要備份** | workspace、`caches/`、`war/`、暫存 | 排除 |

| 方法 | 優點 | 注意事項 |
| --- | --- | --- |
| **儲存層快照**（LVM、ZFS、EBS／Azure Disk snapshot、Kubernetes VolumeSnapshot） | 快速、一致性好、對 Jenkins 影響小 | 需在快照前讓 Jenkins 進入安靜狀態或接受 crash-consistent；快照要複製到另一個區域 |
| **檔案備份（tar／rsync）** | 簡單、可攜 | 執行期間檔案仍在變動；排除不需要的目錄 |
| ThinBackup plugin（2.1.5） | UI 設定、可排程、可只備份設定 | 備份檔放在 controller 本機，仍需另外外送 |

**檔案備份腳本範例**（Linux 套件安裝；以 `age` 加密後上傳到物件儲存）：

```bash
#!/usr/bin/env bash
# /usr/local/sbin/jenkins-backup.sh：每日 02:30 由 systemd timer 執行
set -euo pipefail

JENKINS_HOME=/var/lib/jenkins
STAMP=$(date +%Y%m%d-%H%M%S)
WORK=/var/backups/jenkins
ARCHIVE="${WORK}/jenkins-home-${STAMP}.tar.zst"
RECIPIENT_FILE=/etc/jenkins-backup/age-recipients.txt   # 備份加密公鑰
BUCKET=s3://backup-jenkins-prod/daily

mkdir -p "$WORK"

# 排除可重建或不需要的目錄；secrets/ 一併備份但整個封存檔會加密
tar --zstd -cf "$ARCHIVE" -C "$JENKINS_HOME" \
  --exclude='./workspace' \
  --exclude='./caches' \
  --exclude='./war' \
  --exclude='./logs' \
  --exclude='./plugins/*/' \
  --exclude='./jobs/*/workspace*' \
  --exclude='./.cache' \
  --exclude='./tmp' \
  .

age -R "$RECIPIENT_FILE" -o "${ARCHIVE}.age" "$ARCHIVE"
sha256sum "${ARCHIVE}.age" > "${ARCHIVE}.age.sha256"
rm -f "$ARCHIVE"

aws s3 cp "${ARCHIVE}.age" "${BUCKET}/" --only-show-errors
aws s3 cp "${ARCHIVE}.age.sha256" "${BUCKET}/" --only-show-errors

# 本機只保留 3 份
ls -1t "${WORK}"/jenkins-home-*.tar.zst.age | tail -n +4 | xargs -r rm -f
```

| 原則 | 說明 |
| --- | --- |
| 加密 | 備份含 `secrets/` 與加密後的憑證，等同所有憑證；**一定要加密**，解密私鑰與備份分開保存 |
| 異地 | 至少一份複製到不同區域或不同帳號（防勒索軟體與帳號遭入侵） |
| 不可變 | 物件儲存啟用 Object Lock／WORM，保存期間內不可刪除 |
| RPO | 每日備份＋儲存層每小時快照，可達 RPO ≤ 1 小時 |
| 保存期限 | 依稽核要求（[21.6 臺灣法規與稽核對應](#216-臺灣法規與稽核對應)） |

### 20.2 還原與演練

**還原步驟**：

1. 準備新的 controller（相同 Jenkins 版本與 plugin 組合；以 controller 映像或 `plugins.txt` 安裝）
2. 停止 Jenkins，清空或備份新主機的 `JENKINS_HOME`
3. 解密並解壓縮備份到 `JENKINS_HOME`，修正擁有者（`chown -R jenkins:jenkins`）
4. 若 Jenkins URL 不同，修改 JCasC 的 `unclassified.location.url`
5. 啟動 Jenkins，檢查 Manage Jenkins 的警示、Old Data、plugin 載入錯誤
6. 驗證：登入（SSO）、憑證可用（執行一個使用憑證的測試 Job）、agent 連線、webhook 觸發、最近的建置紀錄可瀏覽

> ⚠️ `secrets/master.key` 必須和 `credentials.xml`、各 Job 的 `config.xml` 來自**同一份備份**，否則所有憑證都無法解密。

✅ **演練**：以 [18.4 Job DSL](#184-job-dsl) 的 `platform-ops/backup-restore-verify` Job 每日在隔離環境（無法連到正式部署目標）以最新備份啟動 Jenkins 並執行冒煙測試；每半年進行一次完整的災難復原演練並記錄實際 RTO。

### 20.3 升級程序

**升級前準備**：

| 檢查項目 | 說明 |
| --- | --- |
| 閱讀升級指南 | [jenkins.io/doc/upgrade-guide](https://www.jenkins.io/doc/upgrade-guide/)：**跨越的每一條 LTS 線都要看**（例如從 2.401.x 升到 2.580.1，需閱讀 2.414 至 2.580 各線的說明） |
| Java 版本 | 2.555.1 起 controller 與所有 agent 都必須是 Java 21／25；先升級 Java，再升級 Jenkins |
| Plugin | **升級前先把 plugin 更新到最新**，升級後再更新一次（官方要求） |
| 必須同步升級的 plugin | 2.479.1：LDAP、Reverse Proxy Auth、CAS、Windows Negotiate SSO；2.516.1：Active Directory 2.40 以上、Entra ID 580.v2f665882b_a_71 以上、Customizable Header；2.528.1：Timestamper |
| JCasC | 移除 `agentProtocols`、`crumbIssuer`、`myViewsTabBar` 等已棄用設定（[18.3 JCasC 實務](#183-jcasc-實務)） |
| 離線環境 | 2.580.1 起 detached plugin 不在 war 中，先放入 `plugins/` |
| 備份 | 升級前完成一次完整備份與儲存層快照 |

**升級流程**：

```mermaid
flowchart TD
    A[閱讀升級指南<br/>確認 Java 與 plugin 需求] --> B[正式環境：更新 plugin 至最新]
    B --> C[預備環境：複製正式設定<br/>升級 core 與 plugin]
    C --> D[冒煙測試：登入、代表性 Pipeline、<br/>agent、webhook、部署到測試環境]
    D --> E{通過?}
    E -->|否| F[修正 plugin／設定<br/>或延後升級]
    F --> C
    E -->|是| G[公告維護窗口<br/>Prepare for Shutdown]
    G --> H[備份與快照]
    H --> I[正式環境升級 core]
    I --> J[更新 plugin 並重新啟動]
    J --> K[驗證與觀察 24 小時]
```

**各安裝方式的升級指令**：

```bash
# Debian／Ubuntu：指定版本並鎖定
sudo apt update
sudo apt install -y jenkins=2.580.1
sudo apt-mark hold jenkins

# RHEL 系列：指定版本（版本鎖定需 dnf versionlock 外掛）
sudo dnf install -y jenkins-2.580.1
sudo dnf versionlock add jenkins

# 容器／Helm：修改映像 tag（例如 2.580.1-lts-jdk21）後重新部署
helm upgrade jenkins jenkins/jenkins -n jenkins --version 5.9.64 -f values-prod.yaml \
  --set controller.image.tag=2.580.1-lts-jdk21
```

**回退計畫**：

| 情境 | 做法 |
| --- | --- |
| Core 升級後異常 | 停止服務 → 還原升級前的儲存層快照 → 安裝舊版 core → 啟動 |
| 單一 plugin 異常 | Manage Jenkins → Plugins → Installed 的「Downgrade」（Jenkins 保留上一版 `.bak`），或以舊版 `.jpi` 取代 |
| RPM 降版到 2.541.1 以前 | 需改用 `redhat-stable-legacy` 套件庫（2.541.1 起統一為 `rpm-stable`） |
| 2.516.1 以後降版 | 需手動建立 `legacyIds` 檔案以避免啟動緩慢（官方升級指南說明） |

> ⚠️ Core 降版不保證能讀取新版寫入的設定格式。**回退的可靠手段是還原快照**，不是直接安裝舊版。

### 20.4 高可用與災難復原

開源 Jenkins 的 controller 是**單一實例**應用程式：同一個 `JENKINS_HOME` 不能由兩個 controller 同時使用，也不能透過增加副本擴充。高可用的設計重點是「縮短故障後的恢復時間」：

| 方案 | RTO（參考） | RPO | 說明 |
| --- | --- | --- | --- |
| **Kubernetes StatefulSet（replicas: 1）＋PV** | 5–15 分鐘 | 0（PV 保留） | 節點故障時 Pod 自動重建並重新掛載 PV；需注意 RWO 磁碟的跨可用區限制 |
| VM＋共用儲存的 active／passive | 10–30 分鐘 | 0 | 以叢集軟體（Pacemaker 等）確保**同時只有一台**掛載與啟動，避免資料損毀 |
| 以程式碼重建（JCasC＋Job DSL＋映像）＋還原建置紀錄 | 30–120 分鐘 | 依備份頻率 | ✅ 災難復原（跨區域）的基本能力；建置紀錄可接受部分遺失時最簡單 |
| 依組織拆分多個 controller | — | — | 縮小單一故障的影響範圍 |
| 🔒 CloudBees CI HA（active／active） | 秒到分鐘 | 0 | 商業版功能 |

```mermaid
flowchart LR
    subgraph RegionA[主要區域]
        C1[Jenkins Controller<br/>StatefulSet replicas=1]
        PV1[(PV：JENKINS_HOME)]
        C1 --- PV1
    end
    subgraph RegionB[災備區域]
        IMG[controller 映像<br/>＋JCasC／Job DSL]
        PV2[(還原的 JENKINS_HOME)]
    end
    PV1 -->|每小時快照／每日加密備份| OBJ[(異地物件儲存<br/>Object Lock)]
    OBJ -->|災難時還原| PV2
    G[(Git：jenkins-config)] --> IMG
```

✅ 降低對單一 controller 依賴的設計：

- **Controller 故障期間不影響正式環境運作**：部署採 GitOps（16.4），即使 Jenkins 停機，正式環境仍由 Argo CD 維持
- **Webhook 遺失可補救**：Multibranch 保留每日掃描（8.5）
- **建置可重跑**：CI 建置使用 `PERFORMANCE_OPTIMIZED`，controller 重啟後重新觸發即可
- **重要紀錄不只存在 Jenkins**：部署紀錄、核准紀錄、測試報告另存到外部系統（21.6）

### 20.5 本章重點

- 設定以程式碼重建，狀態以加密、異地、不可變的備份保護；`secrets/` 與其他檔案必須來自同一份備份
- 每日自動還原驗證，每半年完整災難復原演練
- 升級前閱讀所有跨越 LTS 線的升級指南，先升 Java、升級前後都更新 plugin，回退以快照還原
- 開源 Jenkins 無法 active／active；以 Kubernetes 自動重建、程式碼重建與 GitOps 降低停機影響

## 21. 軟體供應鏈安全與合規

### 21.1 威脅與框架

CI/CD 是軟體供應鏈的核心環節。近年的重大事件（建置系統遭植入後門、相依套件被劫持、CI 憑證外洩）都顯示：**只保護原始碼與正式環境不夠，建置過程本身也必須可信**。

| 框架 | 重點 | 在 Jenkins 的落實 |
| --- | --- | --- |
| **SLSA**（Supply-chain Levels for Software Artifacts） | 建置來源可驗證（provenance）、建置平台隔離、不可竄改 | 以 Pipeline 產生 provenance 並簽章；建置在可拋棄 agent；JCasC 管理平台 |
| **NIST SSDF**（SP 800-218） | 安全開發框架：保護軟體、產出安全軟體、回應弱點 | 品質門檻、弱點掃描、SBOM、漏洞處理流程 |
| **OWASP Top 10 CI/CD Security Risks** | 流程控制不足、身分與存取管理不足、相依套件鏈濫用、Pipeline 執行汙染（PPE）、憑證衛生不足等 10 項 | 第 7、8、14、17 章的控制 |

```mermaid
flowchart LR
    S[原始碼<br/>簽章 commit／分支保護] --> B[建置<br/>可拋棄 agent<br/>相依套件經內部代理]
    B --> T[測試與掃描<br/>SAST／SCA／Secret]
    T --> A[產物<br/>SBOM＋簽章＋provenance]
    A --> R[(Registry／Nexus<br/>不可覆寫)]
    R --> D[部署<br/>admission 驗證簽章]
```

### 21.2 SBOM（軟體物料清單）

| 工具 | 格式 | 用途 |
| --- | --- | --- |
| CycloneDX Maven plugin（2.9.3） | CycloneDX JSON／XML | 從 Maven 相依樹產生，最精確 |
| Syft（v1.54.0） | CycloneDX、SPDX | 掃描容器映像或檔案系統，涵蓋 OS 套件 |

```groovy
pipeline {
    agent { label 'linux && maven' }
    stages {
        stage('SBOM') {
            steps {
                sh '''
                    set -euo pipefail
                    ./mvnw -B -ntp org.cyclonedx:cyclonedx-maven-plugin:2.9.3:makeAggregateBom \
                      -DoutputFormat=json -DoutputName=bom
                    syft "harbor.example.internal/payments/payment-api@${IMAGE_DIGEST}" \
                      -o cyclonedx-json=image-sbom.cdx.json
                '''
                archiveArtifacts artifacts: 'target/bom.json, image-sbom.cdx.json', fingerprint: true
            }
        }
    }
}
```

> 💡 SBOM 應與產物一起保存（Nexus／Registry 的 OCI artifact 或 Dependency-Track），讓新的 CVE 公布時能快速查出受影響的版本與部署位置。

### 21.3 弱點掃描

| 類型 | 工具（範例） | 階段 | 門檻建議 |
| --- | --- | --- | --- |
| 相依套件（SCA） | OWASP Dependency-Check、Grype（v0.119.0）、Trivy（v0.75.0） | PR 與主分支 | 新增 Critical／High → UNSTABLE；正式發佈有 Critical → FAILURE |
| 容器映像 | Trivy、Grype | 映像建置後 | 同上，另檢查基底映像是否為核可版本 |
| 靜態程式碼（SAST） | SonarQube、Semgrep、SpotBugs＋FindSecBugs | PR | 新增高風險問題 → UNSTABLE |
| IaC／設定 | Trivy config、Checkov | PR | Kubernetes manifest 不允許 privileged、hostPath |
| 機密 | Gitleaks（v8.30.1） | PR | 發現即 FAILURE，並輪替外洩的機密 |

```groovy
pipeline {
    agent { label 'linux && docker' }
    stages {
        stage('Image Scan') {
            agent {
                docker {
                    image 'aquasec/trivy:0.75.0'
                    args '--entrypoint=""'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    trivy image --scanners vuln --severity CRITICAL,HIGH \
                      --format json --output trivy-report.json \
                      --exit-code 0 \
                      "harbor.example.internal/payments/payment-api@${IMAGE_DIGEST}"
                '''
            }
            post {
                always {
                    recordIssues(tools: [trivy(pattern: 'trivy-report.json')],
                                 qualityGates: [[threshold: 1, type: 'TOTAL_ERROR', criticality: 'FAILURE'],
                                                [threshold: 1, type: 'NEW_HIGH', criticality: 'UNSTABLE']])
                }
            }
        }
        stage('Secret Scan') {
            agent {
                docker {
                    image 'zricethezav/gitleaks:v8.30.1'
                    args '--entrypoint=""'
                    reuseNode true
                }
            }
            steps {
                sh 'gitleaks git --redact --report-format sarif --report-path gitleaks.sarif .'
            }
        }
    }
}
```

> 💡 掃描以 `--exit-code 0` 輸出報告，再交給 Warnings NG 的品質門檻判斷，可以區分「既有問題」與「新增問題」，避免歷史技術債阻擋所有建置。Trivy 在 Warnings NG 中的嚴重度對應：Critical → ERROR、High → HIGH。

### 21.4 簽章與 Provenance

**以 Cosign（v3.1.3）簽章映像與附加 SBOM attestation**，金鑰保存在 Vault 或雲端 KMS，不落地在 agent：

```groovy
pipeline {
    agent { label 'linux' }
    environment {
        IMAGE_REF = "harbor.example.internal/payments/payment-api@${params.IMAGE_DIGEST}"
    }
    parameters {
        string(name: 'IMAGE_DIGEST', defaultValue: '', description: 'sha256:...')
    }
    stages {
        stage('Sign & Attest') {
            steps {
                withCredentials([string(credentialsId: 'vault-token-cosign', variable: 'VAULT_TOKEN')]) {
                    sh '''
                        set -euo pipefail
                        export VAULT_ADDR=https://vault.example.internal
                        cosign sign --key hashivault://cosign-payments "$IMAGE_REF"
                        cosign attest --key hashivault://cosign-payments \
                          --type cyclonedx --predicate image-sbom.cdx.json "$IMAGE_REF"
                    '''
                }
            }
        }
    }
}
```

| 項目 | 說明 |
| --- | --- |
| 只簽 digest | 永遠簽 `image@sha256:...`，不要簽 tag |
| 金鑰管理 | `--key hashivault://`、`awskms://`、`azurekms://`、`gcpkms://`、`k8s://`；只有 `deploy`／`release` agent 能取得簽章權限 |
| 透明度記錄 | Cosign 預設上傳到公開的 Rekor 透明度記錄；內部映像若不能公開中繼資料，請以 `--signing-config` 指向內部的 Rekor／TSA，或依 Cosign v3 文件關閉上傳（參數在 v3 有調整，導入時請以 `cosign sign --help` 確認） |
| 部署端驗證 | Kubernetes 以 Sigstore policy-controller、Kyverno 或 OPA Gatekeeper 在 admission 階段驗證簽章，未簽章或簽章不符的映像拒絕部署 |
| Provenance | 以 `cosign attest --type slsaprovenance1` 附加建置來源資訊（commit、建置 URL、Jenkinsfile、builder 身分）；Jenkins 沒有內建 SLSA provenance 產生器，需在 Shared Library 中組出 predicate |

### 21.5 Pipeline 的供應鏈防護清單

| 風險（OWASP CI/CD Top 10） | 控制 |
| --- | --- |
| 流程控制不足 | 主分支保護、強制 MR／PR 審查、正式部署需核准（16.2） |
| 身分與存取管理不足 | SSO＋MFA、最小權限、服務帳號與 token 盤點（17.2、17.8） |
| 相依套件鏈濫用 | 所有相依套件經內部代理（Nexus／Artifactory）、鎖定版本、阻擋相依套件混淆（內部套件命名空間） |
| Pipeline 執行汙染（PPE） | 不受信任 PR 使用目標分支的 Jenkinsfile、在隔離 agent 執行、無法取得憑證（8.6、14.6） |
| Pipeline 存取控制不足 | 憑證放在 folder、Authorize Project（7.2、17.4） |
| 憑證衛生不足 | 外部機密管理、輪替、遮罩與單引號字串（7.4、7.5） |
| 系統設定不安全 | JCasC、安全基準、定期稽核（第 18 章、24.3） |
| 第三方服務治理不足 | Plugin 治理與 Webhook secret（第 5 章、8.5） |
| 產物完整性驗證不足 | 簽章與 admission 驗證（21.4） |
| 記錄與可視性不足 | Audit Trail、建置紀錄外送（17.10） |

### 21.6 臺灣法規與稽核對應

以下為常見法遵要求與本手冊控制措施的對應。**條文編號與適用範圍請以全國法規資料庫及主管機關最新公告為準**，並由組織的法遵單位確認。

| 要求來源 | 要求重點 | Jenkins 對應控制 |
| --- | --- | --- |
| 資通安全管理法及其子法（資通安全責任等級分級辦法、資通安全事件通報及應變辦法） | 依責任等級辦理資安防護、存取控制、事件通報 | SSO 與最小權限（17.2–17.3）、安全公告處理（17.9）、稽核記錄送 SIEM（17.10）、事件時能快速撤銷憑證與停用 Pipeline |
| 金管會「金融資安行動方案」、銀行公會相關自律規範 | 系統開發安全、變更管理、職責分離、紀錄保存 | 正式部署核准與職責分離（16.2）、變更單號串接、部署紀錄保存、程式碼審查 |
| 個人資料保護法 | 測試資料不得使用未經處理的正式個資 | 測試環境資料遮罩；Pipeline 不得把正式資料複製到測試環境 |
| ISO/IEC 27001:2022 附錄 A（8.25 安全開發生命週期、8.28 安全程式設計、8.32 變更管理、8.9 組態管理） | 安全開發、變更與組態管理 | 品質與安全門檻（第 13、21 章）、JCasC／Job DSL（第 18 章）、核准流程（16.2） |

**稽核時常被要求提供的證據**：

| 證據 | 來源 |
| --- | --- |
| 正式環境變更清單（何時、何版本、誰核准） | 部署 Pipeline 的建置紀錄、`input` 核准人、變更單號（另存到外部系統） |
| 權限設定與定期審查紀錄 | JCasC 的授權設定（Git 歷史）、每季權限審查紀錄 |
| 弱點掃描與修補紀錄 | Warnings NG 報告、Dependency-Track、修補 MR |
| 系統設定變更紀錄 | Git（JCasC）＋Audit Trail＋Job Configuration History |
| 備份與還原演練紀錄 | 20.2 的演練 Job 與報告 |

### 21.7 本章重點

- 以 SLSA、NIST SSDF、OWASP CI/CD Top 10 為框架檢視 Pipeline
- 每次發佈產生 SBOM，執行 SCA／映像／機密掃描，以「新增問題」為門檻
- 以 Cosign 簽章映像與附加 attestation，金鑰放在 KMS／Vault，部署端以 admission 驗證
- 部署、核准、權限、掃描、備份演練的紀錄都要能在稽核時提出

## 22. 企業導入路線與參考架構

### 22.1 導入路線圖

```mermaid
flowchart LR
    P0[階段 0：盤點<br/>2–4 週] --> P1[階段 1：平台基礎<br/>1–2 個月]
    P1 --> P2[階段 2：試點<br/>1–2 個月]
    P2 --> P3[階段 3：推廣<br/>3–6 個月]
    P3 --> P4[階段 4：持續改善]
```

| 階段 | 目標 | 主要工作 | 完成標準 |
| --- | --- | --- | --- |
| 0 盤點 | 了解現況 | 盤點既有 Jenkins（版本、plugin、Job 數、Freestyle 比例）、SCM、部署方式、資安要求 | 現況報告與差距分析 |
| 1 平台基礎 | 建立可重建、安全的平台 | Helm／映像＋JCasC＋`plugins.txt`、SSO、授權模型、Kubernetes agent、監控、備份（第 3、5、14、17–20 章） | 可在 1 小時內從 Git 重建一個新的 controller |
| 2 試點 | 驗證黃金路徑 | 選 2–3 個代表性專案，以 Shared Library 的標準 Pipeline 完成 CI、品質門檻、部署到 SIT（第 10–13、16 章） | 試點專案的部署頻率與前置時間可量測 |
| 3 推廣 | 擴大到所有團隊 | Organization Folder 自動納管、Freestyle 遷移、教育訓練、內部文件 | 80% 專案使用標準 Pipeline |
| 4 持續改善 | 以數據驅動改善 | DORA 指標、建置時間與失敗原因分析、plugin 精簡、每季升級 | 指標逐季改善 |

### 22.2 平台團隊與治理模型

| 角色 | 職責 |
| --- | --- |
| **平台團隊**（Platform Engineering） | 維運 Jenkins 平台、維護 Shared Library 與黃金路徑、plugin 治理、升級、監控、對內支援 |
| 應用程式團隊 | 維護自己的 Jenkinsfile 與測試、遵循黃金路徑、提出平台需求 |
| 資安團隊 | 制定安全基準、審查受信任 Library 與 Script Approval、追蹤安全公告與掃描結果 |
| 稽核／法遵 | 定義紀錄保存與證據需求（[21.6 臺灣法規與稽核對應](#216-臺灣法規與稽核對應)） |

**黃金路徑（Golden Path）**：平台團隊提供「照著做就能安全上線」的預設路徑，而不是強制規定：

| 黃金路徑元件 | 實作 |
| --- | --- |
| 專案範本 | 包含 `Jenkinsfile`（呼叫 `standardJavaPipeline`）、Dockerfile、Helm chart、品質設定的 repository 範本 |
| 標準 Pipeline | Shared Library 的 `vars/standardJavaPipeline.groovy` 等（[12.5 Pipeline 範本：封裝整條 Declarative Pipeline](#125-pipeline-範本封裝整條-declarative-pipeline)） |
| 自動納管 | Organization Folder 掃描 GitLab group／GitHub organization（[8.6 Multibranch Pipeline 與 Organization Folder](#86-multibranch-pipeline-與-organization-folder)） |
| 文件與支援 | 內部入口網站、FAQ、每週 office hour |
| 逃生口 | 特殊需求的團隊可使用自訂 Jenkinsfile，但仍需通過相同的安全門檻 |

**治理會議節奏**：

| 會議 | 頻率 | 議題 |
| --- | --- | --- |
| Plugin 與安全審查 | 每月 | 新 plugin 申請、安全公告處理狀況、Script Approval 項目 |
| 平台變更審查 | 每次升級前 | LTS 升級計畫、預備環境測試結果 |
| 指標回顧 | 每季 | DORA 指標、建置時間、失敗原因、平台可用性 |

### 22.3 以 DORA 指標衡量成效

| 指標 | 定義 | 從 Jenkins 取得資料的方式 |
| --- | --- | --- |
| 部署頻率 | 一段時間內部署到正式環境的次數 | 正式部署 Job 的成功建置數（Prometheus `default_jenkins_builds_success_build_count_total` 或 REST API） |
| 變更前置時間 | 從 commit 到正式環境運作的時間 | 部署建置的時間 − 對應 commit 的時間（`GIT_COMMIT` 的 commit 時間） |
| 變更失敗率 | 造成故障、需要回滾或修補的部署比例 | 部署紀錄＋事件管理系統（回滾 Pipeline 執行次數） |
| 失敗部署恢復時間 | 部署造成故障後恢復服務所需時間 | 事件管理系統 |
| 重工率（Rework rate） | 非計畫性的修補部署比例 | 以 hotfix 分支或標記統計 |

> 💡 DORA 指標的目的是**團隊自我改善**，不是比較團隊績效。把指標當成考核工具，會導致拆小部署、隱藏失敗等扭曲行為。

### 22.4 DevOps 文化實務

| 實務 | 在 Jenkins 的具體做法 |
| --- | --- |
| 主分支隨時可發佈 | 主分支建置失敗時團隊優先修復（「stop the line」）；以 `regression` 通知提交者 |
| 小批量、頻繁整合 | PR 生命週期 < 2 天；PR 建置 10 分鐘內回饋 |
| 自動化優先 | 任何重複兩次以上的人工步驟都要評估自動化 |
| 無責檢討（Blameless postmortem） | 部署事故後檢討流程與系統，而非追究個人；改善項目落實到 Pipeline（例如新增檢查） |
| 共享責任 | 開發團隊能看到自己服務的建置、部署與監控數據 |
| 持續學習 | 平台團隊定期分享 Pipeline 最佳實務與失敗案例 |

### 22.5 參考情境一：金融機構（示意）

> 以下情境綜合常見的金融業導入經驗，用於說明架構與決策，**不代表特定機構的實際資料**。

| 項目 | 內容 |
| --- | --- |
| 現況 | 3 套各自維護的 Jenkins（2.3xx 版）、約 1,200 個 Job（七成 Freestyle）、部署以人工登入主機執行腳本 |
| 限制 | 封閉網路、正式環境變更需經變更管理委員會（CAB）核准、須保存變更紀錄供金檢 |
| 架構決策 | 依安全等級拆分為「一般 CI controller」與「正式部署 controller」；兩者皆以 Helm＋JCasC 部署於內部 Kubernetes；離線 update center 鏡像（[3.9 離線（封閉網路）安裝](#39-離線封閉網路安裝)） |
| 關鍵控制 | SSO＋MFA；正式部署只能由 `prod` folder 中的 Pipeline、在 `deploy-prod` agent 執行；`input` 核准串接 ITSM 變更單；所有部署紀錄送 SIEM |
| 遷移策略 | 先遷移正式部署 Job（最高稽核價值），再以 Organization Folder 納管各應用程式 repository；Freestyle 以 Job DSL 重建為 Pipeline |
| 量測 | 部署前置時間、部署失敗率、稽核證據準備時間 |

### 22.6 參考情境二：製造業多語言環境（示意）

| 項目 | 內容 |
| --- | --- |
| 現況 | Java 後端、.NET 桌面程式、嵌入式 C/C++ 韌體、Python 資料分析並存；Windows 與 Linux 建置機混用 |
| 架構決策 | 單一 controller＋多種 agent：Kubernetes Pod（Java、Python、前端）、Windows 固定 agent（.NET、簽章）、專用硬體 agent（韌體燒錄與硬體在環測試，以 Lockable Resources 管理裝置） |
| 關鍵控制 | Label 依能力命名（`windows && msbuild`、`hil && board-x1`）；韌體映像簽章；OT 網段的 agent 只能以 WebSocket 主動連線 controller |
| 量測 | 建置排隊時間、硬體資源使用率、韌體發佈週期 |

### 22.7 舊 Jenkins 整併與遷移

```mermaid
flowchart TD
    A[盤點舊 controller<br/>Job、plugin、憑證、agent] --> B[分類 Job<br/>保留／遷移／淘汰]
    B --> C[新平台以 JCasC 建立<br/>只安裝必要 plugin]
    C --> D[憑證重新建立<br/>（不搬移舊 credentials.xml）]
    D --> E[以 Job DSL／Organization Folder<br/>建立新 Job]
    E --> F[平行運作一段時間<br/>比對結果]
    F --> G[切換 webhook 與排程]
    G --> H[舊 controller 唯讀<br/>保留建置紀錄至期限後下線]
```

| 原則 | 說明 |
| --- | --- |
| 不搬移整個 `JENKINS_HOME` | 舊的 plugin 設定與殘留資料會一起帶過去；新平台從程式碼建立 |
| 憑證重新建立 | 藉機輪替所有憑證，並放到正確的 folder 層級 |
| 淘汰長期未執行的 Job | 6 個月未執行的 Job 先停用、3 個月後刪除 |
| 平行運作 | 關鍵 Pipeline 新舊平台同時執行一段時間，比對產物與結果 |

### 22.8 AI 輔助的 Pipeline 維運

生成式 AI 可以協助撰寫 Jenkinsfile、分析建置失敗原因、整理升級指南，但必須遵守以下原則：

| 原則 | 說明 |
| --- | --- |
| 不送出機密 | 建置記錄、`config.xml`、JCasC 匯出檔可能含有憑證或內部資訊；只能送到組織核可、具資料保護約定的 AI 服務 |
| 一律驗證 | AI 產生的 Jenkinsfile 必須通過 Declarative 驗證（[11.7 Pipeline 開發工具](#117-pipeline-開發工具)）、Shared Library 單元測試與程式碼審查；本手冊在 v1.0 中發現的 11 個語法錯誤範例，正是未經驗證的典型問題 |
| 以官方文件為準 | plugin 參數、JCasC 鍵名常隨版本變更（例如 8.3 的 `secretToken`），請以 Snippet Generator、`/configuration-as-code/reference` 確認 |
| 人做決策 | 是否核准部署、是否接受 Script Approval、是否放寬安全設定，由負責人決定 |

### 22.9 本章重點

- 依「盤點 → 平台基礎 → 試點 → 推廣 → 持續改善」分階段導入，平台基礎完成的標準是「能從 Git 重建 controller」
- 平台團隊提供黃金路徑與逃生口，以 DORA 指標支持團隊自我改善
- 依安全等級拆分 controller 與 agent；舊平台遷移時從程式碼重建並輪替憑證
- AI 產出的 Pipeline 與設定一律經過驗證與審查

## 23. 故障排除

### 23.1 排除問題的方法

```mermaid
flowchart TD
    A[收到問題回報] --> B{影響範圍?}
    B -->|單一 Job| C[檢視主控台記錄<br/>Pipeline Overview 找出失敗 step]
    B -->|多個 Job／整個平台| D[檢查 controller 健康<br/>監控、系統記錄、磁碟]
    C --> E{最近有變更?}
    D --> E
    E -->|Jenkinsfile／Library| F[比對 commit，用 Replay 驗證修正]
    E -->|Plugin／Core 升級| G[檢查升級指南與 plugin 已知問題<br/>必要時回退]
    E -->|環境（agent、網路、憑證）| H[檢查 agent 記錄、連線、憑證有效期]
    F --> I[修正並記錄]
    G --> I
    H --> I
```

✅ 基本原則：

- 先看**第一個**錯誤訊息，而不是最後一行（後續錯誤通常是連鎖反應）
- 在預備環境重現；不要在正式 controller 上直接試驗修正
- 調整 log 層級時建立專用的 log recorder，問題解決後移除（[19.4 日誌](#194-日誌)）

### 23.2 Pipeline 常見錯誤

| 錯誤訊息（節錄） | 原因 | 解決方式 |
| --- | --- | --- |
| `Expected a when condition` | `when` 中直接寫布林運算式 | 改為 `expression { params.X }`（[10.6 when 條件](#106-when-條件)） |
| `Environment variable values must either be single quoted, double quoted, or function calls` | `environment` 中使用變數、三元運算式 | 改到 `script { env.X = ... }`（[10.3 environment 與字串內插](#103-environment-與字串內插)） |
| `No such DSL method 'xxx' found among steps` | 對應 plugin 未安裝或拼字錯誤 | 以 Snippet Generator 確認 step 名稱；安裝 plugin |
| `Invalid parameter "xxx", did you mean "yyy"?` | step 參數名稱錯誤（Declarative 驗證可提前發現） | 以 Snippet Generator 產生正確參數 |
| `Tool type "maven" does not have an install of "xxx" configured` | `tools {}` 名稱與 Manage Jenkins → Tools 不一致 | 統一工具名稱（本手冊為 `maven-3.9`、`jdk-21`）或改用容器化 agent |
| `RejectedAccessException: Scripts not permitted to use method ...` | 沙箱阻擋未核准的方法 | 改用 Pipeline step；確有必要再由管理員評估核准（[11.3 Script Security 沙箱與 Script Approval](#113-script-security-沙箱與-script-approval)） |
| `java.io.NotSerializableException` | 不可序列化的物件跨越 step | 移到 `@NonCPS` 方法（[11.2 CPS 限制與 @NonCPS](#112-cps-限制與-noncps)） |
| `Method code too large` | Pipeline 太大，超過 JVM 方法大小上限 | 把邏輯移到 Shared Library |
| `A secret was passed to "sh" using Groovy String interpolation, which is insecure` | 機密在雙引號字串中被 Groovy 內插 | 改用單引號，讓 shell 展開（[7.4 遮罩的限制與常見外洩途徑](#74-遮罩的限制與常見外洩途徑)） |
| `Could not find credentials entry with ID 'xxx'` | 憑證 ID 錯誤，或憑證位於其他 folder／System 範圍 | 確認憑證所在 folder 與作用域（[7.2 憑證作用域](#72-憑證作用域)） |
| `There are no nodes with the label 'xxx'` | label 無對應 agent 或 cloud 範本 | 確認 label 表達式；檢查 cloud 設定 |
| 建置一直停在 `Waiting for next available executor` | Agent 不足、label 錯誤、Pod 無法排程 | 檢查佇列原因（23.6 腳本）；Kubernetes 檢查 Pod 事件 |
| `script returned exit code 1` | Shell 指令失敗 | 往上找實際錯誤；`sh` 預設 `-xe`，在腳本中加 `set -euo pipefail` 讓錯誤更早出現 |
| `hudson.plugins.git.GitException ... returned status code 128` | 憑證錯誤、主機金鑰驗證失敗、網路 | 檢查 Git Host Key Verification 設定與 known_hosts；確認憑證權限 |
| Controller 重啟後，執行中的建置沒有恢復而直接失敗（使用 `disableResume()` 的建置開頭會顯示 `Resume disabled by user, switching to high-performance, low-durability mode.`） | `PERFORMANCE_OPTIMIZED` 或 `disableResume()` 的預期行為 | 重新觸發建置；需要可恢復的 Pipeline 改用 `MAX_SURVIVABILITY` |

### 23.3 Agent 連線問題

| 症狀 | 常見原因 | 檢查與處理 |
| --- | --- | --- |
| WebSocket agent 無法連線，HTTP 400／404 | 反向代理未轉送 `Upgrade`／`Connection` 標頭 | 依 [3.8 反向代理與 TLS](#38-反向代理與-tls) 設定 `proxy_http_version 1.1` 與 Upgrade 標頭 |
| Agent 啟動即結束，訊息提及 Java 版本 | Agent 不是 Java 21／25 | 升級 agent 的 Java；容器 agent 使用 `-jdk21` 映像 |
| `Unexpected termination of the channel` | 網路中斷、agent 被 OOM 殺掉、負載平衡器閒置逾時 | 檢查 agent 系統記錄與 `dmesg`；調高負載平衡器的閒置逾時 |
| Inbound agent 驗證失敗 | secret 與節點名稱不符、節點被重建後 secret 改變 | 重新取得節點頁面的 secret |
| TCP inbound agent 無法連線 | Agent TCP port 已停用（`slaveAgentPort: -1`） | 改用 `-webSocket`，或開放並指定固定 port |
| Kubernetes Pod 一直 `Pending` | 資源不足、nodeSelector／taint 不符、ResourceQuota 用盡 | `kubectl describe pod`、檢查 namespace quota |
| Pod `ImagePullBackOff` | 映像名稱錯誤、registry 憑證未設定 | 設定 `imagePullSecrets` 或 registry mirror |
| 建置卡在等待容器 | 工具容器未設定 `sleep infinity`／`cat`＋`tty` 而直接結束 | 修正 Pod 範本（[14.4 Kubernetes plugin](#144-kubernetes-plugin)） |
| SSH agent 連線失敗 | 主機金鑰未在 known_hosts、Java 路徑錯誤 | 更新 known_hosts；設定 `javaPath` |

### 23.4 效能問題

**收集 thread dump**（controller 緩慢、卡住時最重要的資料）：

```bash
# 方法一：Jenkins UI（需管理員）：<Jenkins URL>/threadDump
# 方法二：JDK 工具（在 controller 主機上，以 jenkins 使用者執行），間隔 10 秒取 3 次
PID=$(pgrep -u jenkins -f 'jenkins.war' | head -1)
for i in 1 2 3; do
  jcmd "$PID" Thread.print -l > "/tmp/jenkins-threads-$(date +%H%M%S).txt"
  sleep 10
done
# GC 與 heap 概況
jcmd "$PID" GC.heap_info
```

| 觀察 | 可能原因 |
| --- | --- |
| 大量執行緒停在同一個 plugin 的方法 | 該 plugin 的效能問題或死結；查詢 plugin 的已知問題 |
| 許多 `CpsVmExecutorService` 執行緒忙碌 | Pipeline Groovy 運算過重（[11.4 Durability 與效能設定](#114-durability-與效能設定)） |
| GC log 顯示頻繁 Full GC | Heap 不足或記憶體洩漏；取 heap dump 分析 |
| 執行緒停在 SCM 或網路呼叫 | 外部系統（SCM、LDAP、update center）回應緩慢 |

### 23.5 Controller 啟動問題

| 症狀（系統記錄） | 原因 | 處理 |
| --- | --- | --- |
| Java 版本過舊的錯誤，Jenkins 拒絕啟動 | 2.555.1 起需要 Java 21／25 | 安裝 Java 21，設定 `JAVA_HOME` 或 systemd `JENKINS_JAVA_CMD`（[3.3 Linux 套件安裝（systemd）](#33-linux-套件安裝systemd)） |
| JCasC 回報 `'agentProtocols' is deprecated` 等並中止 | YAML 含已棄用設定 | 移除該設定（[18.3 JCasC 實務](#183-jcasc-實務)）；過渡期可設 `deprecated: warn` |
| `Failed Loading plugin ...`、相依 plugin 版本不足 | plugin 組合不一致；離線環境缺少 detached plugin | 以 PIMT 重新解析完整清單（[5.3 以 plugins.txt 與 Plugin Installation Manager Tool 管理](#53-以-pluginstxt-與-plugin-installation-manager-tool-管理)） |
| `java.net.BindException: Address already in use` | 連接埠被占用 | 檢查其他服務或殘留的 Jenkins 行程 |
| 啟動時間極長、systemd 逾時 | Job 與建置紀錄過多 | 調高 `TimeoutStartSec`；清理舊資料 |
| `No space left on device` | 磁碟滿 | 清理建置紀錄、workspace；擴充磁碟 |
| 登入後畫面空白、樣式錯亂 | 反向代理改寫路徑、CSP 強制模式與舊 plugin 不相容 | 檢查 Jenkins URL 與代理設定；暫時將 CSP 改回 report-only 並找出不相容的 plugin |

### 23.6 診斷用唯讀腳本

以下腳本只讀取狀態，可在 Script Console 執行（已在 2.580.1 實測）：

```groovy
import jenkins.model.Jenkins

// 1. 佇列中每個項目等待的原因
Jenkins.get().queue.items.each { item ->
    println "${item.task.fullDisplayName} | 已等待 ${(System.currentTimeMillis() - item.inQueueSince).intdiv(1000)} 秒 | 原因：${item.why}"
}

// 2. 離線的 agent 與原因
Jenkins.get().computers.findAll { it.offline && it.name }.each { c ->
    println "離線：${c.name} | 原因：${c.offlineCauseReason ?: '（無）'}"
}

// 3. 停用或載入失敗的 plugin
Jenkins.get().pluginManager.with { pm ->
    pm.plugins.findAll { !it.isEnabled() }.each { println "已停用：${it.shortName} ${it.version}" }
    pm.failedPlugins.each { println "載入失敗：${it.name} -> ${it.cause}" }
}
```

### 23.7 收集支援資訊

| 工具 | 用途 |
| --- | --- |
| **Support Core plugin** | Manage Jenkins → Support（或頁首 More actions），產生包含系統資訊、plugin 清單、thread dump、記錄、設定摘要的 support bundle；可啟用 **Support Bundle Anonymization** 遮蔽 Job 名稱、使用者等資訊 |
| CLI `support` 指令 | `java -jar jenkins-cli.jar -s <URL> -webSocket -auth @auth support > bundle.zip` |
| System Information 頁面 | 系統屬性、環境變數、plugin 版本 |
| `/manage/about` | 版本與授權資訊 |

> ⚠️ Support bundle 可能包含內部主機名稱、環境變數與設定內容。對外提供（例如向社群或廠商求助）前務必啟用匿名化並人工檢查內容。

### 23.8 本章重點

- 先界定影響範圍，再看第一個錯誤；在預備環境重現與修正
- 多數 Pipeline 錯誤可透過 Declarative 驗證與 Snippet Generator 提前發現
- Agent 問題優先檢查 Java 版本、反向代理的 WebSocket 標頭與 label
- 效能問題以 thread dump、GC log 為依據；求助時使用匿名化的 support bundle

## 24. 檢查清單

### 24.1 安裝與平台建置

| # | 項目 | 參考 |
| --- | --- | --- |
| 1 | 使用 LTS 2.580.1（或之後的 LTS），以固定版本的套件、映像或 Helm 部署 | 3.3–3.6 |
| 2 | Controller 與所有 agent 使用 Java 21 或 25 | 1.4 |
| 3 | Built-in node 的 executor 為 0 | 2.1 |
| 4 | 未掛載 `docker.sock`；Windows 服務不以 LocalSystem 執行 | 3.4、3.5 |
| 5 | 反向代理提供 HTTPS 與 WebSocket，Jenkins URL 設定正確 | 3.8 |
| 6 | `plugins.txt` 固定版本並放在 Git，以 PIMT 安裝 | 5.3 |
| 7 | 系統設定以 JCasC 管理，Job 以 Job DSL／Organization Folder 建立 | 第 18 章 |
| 8 | Agent 使用 WebSocket 或 SSH（主機金鑰驗證）；未使用的 TCP agent port 已停用 | 2.2、14.2 |
| 9 | 監控（Prometheus／OTel）與告警已上線 | 第 19 章 |
| 10 | 備份、異地複製、每日還原驗證已上線 | 20.1–20.2 |

### 24.2 Pipeline 品質

| # | 項目 | 參考 |
| --- | --- | --- |
| 1 | 使用 Multibranch／Organization Folder 與 Declarative Pipeline | 8.6、第 10 章 |
| 2 | Jenkinsfile 提交前通過 Declarative 驗證 | 11.7 |
| 3 | 設定 `buildDiscarder`、`timeout`、`disableConcurrentBuilds(abortPrevious: true)`（PR） | 10.4 |
| 4 | `when` 使用 `beforeAgent true`；布林條件包在 `expression {}` | 10.6 |
| 5 | 機密與使用者輸入一律以單引號字串交給 shell | 7.4、10.3 |
| 6 | 測試報告（`junit`）、覆蓋率（`recordCoverage`）、靜態分析（`recordIssues`）以新增程式碼為門檻 | 第 13 章 |
| 7 | 工具版本以容器映像或 Wrapper 固定 | 9.1 |
| 8 | 重複邏輯放在 Shared Library，以固定 tag 引用並有單元測試 | 第 12 章 |
| 9 | 產物只建置一次，以 digest 逐環境晉升 | 15.4、16.1 |
| 10 | 失敗通知只送給需要行動的人（`regression`／`fixed`） | 19.7 |

### 24.3 安全基準

| # | 項目 | 參考 |
| --- | --- | --- |
| 1 | SSO（OIDC／SAML）＋MFA；破窗帳號受控 | 17.2 |
| 2 | Matrix／Role-based 授權，全域只給讀取，管理員 2–4 人 | 17.3 |
| 3 | 正式部署 Job 未授予 `Job/Configure`、`Run/Replay` 給一般開發者 | 17.3 |
| 4 | Authorize Project 已啟用 | 17.4 |
| 5 | 憑證放在 folder 層級；正式環境憑證只有 `prod` folder 可用 | 7.2 |
| 6 | 外部 fork PR 只信任具寫入權限者，並在隔離 agent 執行 | 8.6、14.6 |
| 7 | CSP 強制模式、Resource Root URL、Safe HTML 已設定 | 17.6 |
| 8 | Legacy API token 停用；服務帳號 token 有盤點與到期管理 | 17.8 |
| 9 | Script Approval 以 JCasC 管理並定期清理；受信任 Library 的寫入權限受控 | 11.3、17.7 |
| 10 | 無已棄用或有未修補漏洞的 plugin | 5.4 |
| 11 | 安全公告處理流程與修補時限已定義並執行 | 17.9 |
| 12 | Audit Trail 送 SIEM；設定變更可追溯到 Git | 17.10 |
| 13 | SBOM、弱點掃描、映像簽章與 admission 驗證已上線 | 第 21 章 |

### 24.4 正式上線前

| # | 項目 |
| --- | --- |
| 1 | 預備 controller 與正式 controller 的 core、plugin、JCasC 一致 |
| 2 | 代表性 Pipeline（建置、測試、映像、部署 SIT）在預備環境通過 |
| 3 | Webhook 從各 SCM 實際觸發成功；每日掃描作為備援 |
| 4 | Agent 擴充測試：同時觸發預期尖峰 1.5 倍的建置，佇列可於可接受時間內消化 |
| 5 | 監控與告警已實際觸發測試（例如停止一個 agent） |
| 6 | 還原演練完成，RTO／RPO 符合目標 |
| 7 | 操作手冊（runbook）、值班聯絡方式、升級與回退程序已文件化 |
| 8 | 使用者文件與教育訓練完成 |

### 24.5 LTS 升級

| # | 項目 | 參考 |
| --- | --- | --- |
| 1 | 已閱讀所有跨越 LTS 線的升級指南 | 20.3 |
| 2 | Java 版本符合新版需求（controller 與 agent） | 1.5 |
| 3 | 升級前已更新 plugin；確認必須同步升級的 plugin | 20.3 |
| 4 | JCasC 以 `check` 端點驗證，已移除棄用設定 | 18.3 |
| 5 | 已棄用與有安全警示的 plugin 已處理 | 5.4 |
| 6 | 預備環境升級與冒煙測試通過 | 20.3 |
| 7 | 完整備份與儲存層快照已完成 | 20.1 |
| 8 | 維護窗口已公告；使用 Prepare for Shutdown | 4.2 |
| 9 | 升級後再次更新 plugin，觀察 24 小時監控指標 | 20.3 |
| 10 | 回退計畫（快照還原）已演練 | 20.3 |

## 附錄 A：指令與 API 速查

### A.1 Jenkins CLI

```bash
# 下載 CLI（版本與 controller 相同）
curl -fsSLO https://jenkins.example.internal/jnlpJars/jenkins-cli.jar

# 驗證檔：內容為「使用者:API token」，權限 600
printf '%s:%s' "svc-ci" "<API token>" > ~/.jenkins-cli-auth
chmod 600 ~/.jenkins-cli-auth

J="java -jar jenkins-cli.jar -s https://jenkins.example.internal/ -webSocket -auth @$HOME/.jenkins-cli-auth"

$J who-am-i                                  # 確認身分與權限
$J version
$J list-plugins | sort                       # 已安裝 plugin
$J list-jobs payments                        # 列出 folder 內的 Job
$J build payments/payment-api/main -s -v     # 觸發並等待完成、輸出記錄
$J build ops-job -p TARGET_ENV=sit -s        # 帶參數
$J console payments/payment-api/main 42      # 取得建置記錄
$J stop-builds payments/payment-api/main
$J declarative-linter < Jenkinsfile          # 驗證 Jenkinsfile
$J reload-jcasc-configuration                # 重新載入 JCasC
$J check-configuration < jenkins.yaml        # 檢查 JCasC（不套用）
$J export-configuration > exported.yaml      # 匯出 JCasC
$J offline-node linux-build-01 -m "維護中"
$J online-node linux-build-01
$J keep-build payments/payment-api/main 42   # 永久保留某次建置
$J quiet-down                                # 停止接受新建置
$J cancel-quiet-down
$J safe-restart                              # 等待執行中的建置完成後重新啟動
```

> 💡 以上指令名稱取自 2.580.1 的 `help` 輸出。WebSocket 模式需要先設定 Jenkins URL（[17.8 API Token、CLI 與服務帳號](#178-api-tokencli-與服務帳號)）。

### A.2 REST API

| 用途 | 方法與路徑 |
| --- | --- |
| 任意物件的 JSON | `GET <物件 URL>/api/json?tree=...`（以 `tree` 只取需要的欄位，避免回應過大） |
| 列出 Job 與狀態 | `GET /api/json?tree=jobs[name,color,url]` |
| 觸發建置 | `POST /job/<name>/build` |
| 帶參數觸發 | `POST /job/<name>/buildWithParameters?TARGET_ENV=sit` |
| 最近一次建置 | `GET /job/<name>/lastBuild/api/json?tree=number,result,timestamp,duration` |
| 建置記錄 | `GET /job/<name>/<n>/consoleText` |
| 佇列 | `GET /queue/api/json?tree=items[id,why,inQueueSince,task[name]]` |
| 節點 | `GET /computer/api/json?tree=computer[displayName,offline,offlineCauseReason]` |
| 取得／更新 Job 設定 | `GET`／`POST /job/<name>/config.xml` |
| 驗證 Jenkinsfile | `POST /pipeline-model-converter/validate`（表單欄位 `jenkinsfile`） |
| 驗證 JCasC | `POST /configuration-as-code/check`（body 為 YAML） |
| 重新載入 JCasC | `POST /configuration-as-code/reload` |
| Prometheus 指標 | `GET /prometheus/` |

```bash
# Folder／Multibranch 的路徑：每一層都是 /job/<名稱>；分支名稱中的 / 需編碼為 %2F
BASE=https://jenkins.example.internal
JOB="job/payments/job/payment-api/job/feature%252Flogin"   # 分支 feature/login
curl -fsS -u "$J_USER:$J_TOKEN" "$BASE/$JOB/lastBuild/api/json?tree=number,result"

# 觸發帶參數的建置，從回應標頭取得佇列項目 URL
curl -fsS -u "$J_USER:$J_TOKEN" -X POST -D - -o /dev/null \
  "$BASE/job/platform-ops/job/deploy/buildWithParameters?TARGET_ENV=sit" | grep -i '^location:'
```

> 💡 使用 API token 時不需要 CSRF crumb。Multibranch 的分支名稱若含 `/`，URL 中要寫成 `%252F`（`%2F` 再編碼一次）。

### A.3 常用 Pipeline step 速查

| Step | 用途 | 範例 |
| --- | --- | --- |
| `sh`／`bat`／`powershell` | 執行指令 | `sh(script: 'git rev-parse HEAD', returnStdout: true).trim()` |
| `checkout scm` | 取出原始碼 | |
| `dir` | 切換目錄 | `dir('frontend') { sh 'npm ci' }` |
| `withEnv` | 設定環境變數 | `withEnv(['MAVEN_OPTS=-Xmx1g']) { ... }` |
| `withCredentials` | 綁定憑證 | 7.3 |
| `stash`／`unstash` | 跨 agent 傳遞小型檔案 | `stash name: 'jar', includes: 'target/*.jar'` |
| `archiveArtifacts` | 保存產物 | `archiveArtifacts artifacts: 'target/*.jar', fingerprint: true` |
| `junit`／`recordCoverage`／`recordIssues` | 報告與品質門檻 | 第 13 章 |
| `readJSON`／`readYaml`／`writeJSON`／`readProperties` | 讀寫設定檔（Pipeline Utility Steps） | `def cfg = readYaml file: 'app.yaml'` |
| `fileExists`／`readFile`／`writeFile` | 檔案操作 | |
| `timeout`／`retry`／`waitUntil` | 流程控制 | 11.6 |
| `catchError`／`warnError`／`unstable`／`error` | 結果控制 | 11.6 |
| `input` | 人工核准 | 10.9 |
| `lock`／`milestone` | 資源鎖定與順序 | 11.5 |
| `build` | 觸發其他 Job | `build job: 'payments/integration-test', wait: true, parameters: [string(name: 'VERSION', value: env.VERSION)]` |
| `cleanWs` | 清除 workspace | `cleanWs(deleteDirs: true, notFailBuild: true)` |
| `emailext`／`slackSend` | 通知 | 19.7 |

### A.4 Git、容器與 Kubernetes 常用指令

```bash
# Git：建置中取得資訊
git rev-parse --short=8 HEAD               # 短 commit SHA
git describe --tags --always --dirty       # 最近的 tag
git log -1 --format='%an <%ae> %s'         # 最近提交者與訊息
git diff --name-only "origin/${CHANGE_TARGET:-main}"...HEAD   # PR 變更的檔案

# 容器映像（無 daemon）
buildctl-daemonless.sh build --frontend dockerfile.v0 --local context=. --local dockerfile=. \
  --output type=image,name=harbor.example.internal/payments/payment-api:1.4.2,push=true
crane digest harbor.example.internal/payments/payment-api:1.4.2       # 取得 digest
trivy image --severity CRITICAL,HIGH harbor.example.internal/payments/payment-api:1.4.2
cosign verify --key cosign.pub "harbor.example.internal/payments/payment-api@${IMAGE_DIGEST}"

# Kubernetes
kubectl -n payments-sit rollout status deployment/payment-api --timeout=10m
kubectl -n payments-sit get events --sort-by=.lastTimestamp | tail -20
kubectl -n jenkins-agents get pods -l jenkins/label=k8s-maven
helm -n payments-sit history payment-api --max 5
helm -n payments-sit rollback payment-api 12
```

## 附錄 B：範本索引

本手冊中可直接改寫套用的範本（皆已依 [附錄 G：查證紀錄](#附錄-g查證紀錄) 的方法驗證）：

| 類別 | 範本 | 位置 |
| --- | --- | --- |
| 安裝 | systemd drop-in（JVM、JCasC 路徑） | [3.3 Linux 套件安裝（systemd）](#33-linux-套件安裝systemd) |
| 安裝 | Windows MSI 無人值守安裝 | [3.4 Windows 安裝（MSI）](#34-windows-安裝msi) |
| 安裝 | Controller Dockerfile（預裝 plugin）、Compose（controller＋WebSocket agent） | [3.5 Docker／Podman 容器部署](#35-dockerpodman-容器部署) |
| 安裝 | Helm values（基本、正式環境進階） | [3.6 Kubernetes（Helm）部署](#36-kuberneteshelm部署)、[15.5 在 Kubernetes 上執行 Jenkins controller（Helm 進階設定）](#155-在-kubernetes-上執行-jenkins-controllerhelm-進階設定) |
| 安裝 | Nginx 反向代理（HTTPS＋WebSocket） | [3.8 反向代理與 TLS](#38-反向代理與-tls) |
| 安裝 | 離線 plugin 下載 | [3.9 離線（封閉網路）安裝](#39-離線封閉網路安裝) |
| Plugin | 基準 `plugins.txt` | [5.3 以 plugins.txt 與 Plugin Installation Manager Tool 管理](#53-以-pluginstxt-與-plugin-installation-manager-tool-管理) |
| 憑證 | `withCredentials`、`sshagent`、Vault、Kubernetes Secret 映射 | [7.3 在 Pipeline 使用憑證](#73-在-pipeline-使用憑證)、[7.5 外部機密管理](#75-外部機密管理) |
| 憑證 | JCasC 憑證宣告 | [7.6 以 JCasC 管理憑證](#76-以-jcasc-管理憑證) |
| SCM | GitHub App、GitLab server 設定（JCasC） | [8.2 GitHub 整合（GitHub App 驗證）](#82-github-整合github-app-驗證)、[8.3 GitLab 整合](#83-gitlab-整合) |
| SCM | Multibranch／Organization Folder（Job DSL） | [8.6 Multibranch Pipeline 與 Organization Folder](#86-multibranch-pipeline-與-organization-folder) |
| 建置 | Maven（容器化＋Config File Provider、`withMaven`）、Gradle | [9.3 Pipeline 中的 Maven 建置](#93-pipeline-中的-maven-建置)、[9.4 Gradle](#94-gradle) |
| Pipeline | Declarative 各區段範例、完整 Spring Boot Pipeline | 第 10 章、[10.12 完整範例：Spring Boot 服務 Pipeline](#1012-完整範例spring-boot-服務-pipeline) |
| Pipeline | Scripted 動態平行、錯誤處理、`@NonCPS` | [11.1 Scripted Pipeline 語法](#111-scripted-pipeline-語法)、[11.2 CPS 限制與 @NonCPS](#112-cps-限制與-noncps) |
| Pipeline | `lock`／`milestone`、`catchError`／`retry` | [11.5 資源鎖定與 milestone](#115-資源鎖定與-milestone)、[11.6 錯誤處理模式](#116-錯誤處理模式) |
| Library | Shared Library 結構、`vars`、`src`、整條 Pipeline 範本、JenkinsPipelineUnit 測試 | 第 12 章 |
| 品質 | JUnit、Coverage、Warnings NG、SonarQube | 第 13 章 |
| Agent | SSH 固定 agent、Kubernetes cloud 與 Pod 範本（JCasC） | [14.2 固定 agent：SSH 與 Windows](#142-固定-agentssh-與-windows)、[14.4 Kubernetes plugin](#144-kubernetes-plugin) |
| 映像 | BuildKit rootless Pod 範本與 Pipeline | [15.2 BuildKit rootless（Kubernetes agent）](#152-buildkit-rootlesskubernetes-agent) |
| 部署 | 核准與職責分離、Helm 4、Kustomize、GitOps MR、Blue-Green、Argo Rollouts Canary、Ansible | 第 16 章 |
| 安全 | OIDC、LDAP、Role-based、folder 權限、CSP 等安全基準（JCasC） | 第 17 章 |
| 設定 | JCasC 基礎、Job DSL 維運 Job 與團隊批次建立、設定驗證 Pipeline | 第 18 章 |
| 監控 | Prometheus plugin 設定、抓取設定、告警規則、OpenTelemetry、通知 | 第 19 章 |
| 維運 | 加密備份腳本、升級指令 | [20.1 備份策略](#201-備份策略)、[20.3 升級程序](#203-升級程序) |
| 供應鏈 | SBOM、Trivy／Gitleaks 掃描、Cosign 簽章 | 第 21 章 |
| 故障排除 | 診斷用唯讀 Groovy 腳本、thread dump 收集 | [23.4 效能問題](#234-效能問題)、[23.6 診斷用唯讀腳本](#236-診斷用唯讀腳本) |

## 附錄 C：Plugin 建議清單

### C.1 基準 plugin（2026-10-02）

| Plugin（ID） | 版本 | 用途 | 章節 |
| --- | --- | --- | --- |
| Configuration as Code（`configuration-as-code`） | 2131.vb_a_13ed96f755 | 系統設定程式碼化 | 18 |
| Job DSL（`job-dsl`） | 3732.v9a_c49a_61a_313 | Job 程式碼化 | 18 |
| Folders（`cloudbees-folder`） | 6.1106.v3a_d9a_6d2465e | Folder 與 folder 層級設定 | 4、7 |
| Pipeline（`workflow-aggregator`） | 608.v67378e9d3db_1 | Pipeline 全套 | 10–11 |
| Pipeline Graph View（`pipeline-graph-view`） | 1041.v107d70db_b_1a_f | Pipeline 視覺化 | 4 |
| Pipeline: Groovy Libraries（`pipeline-groovy-lib`） | 806.v408277b_33d1d | Shared Library | 12 |
| Pipeline Utility Steps（`pipeline-utility-steps`） | 3.810.va_7672d206740 | `readYaml`、`readJSON` 等 | A.3 |
| Pipeline: Milestone Step（`pipeline-milestone-step`） | 152.v6e22b_8cfc66c | 部署順序控制 | 11 |
| Lockable Resources（`lockable-resources`） | 1560.va_b_cd589f23eb_ | 資源鎖定 | 11 |
| Timestamper（`timestamper`） | 1.30 | 主控台時間戳記 | 10 |
| AnsiColor（`ansicolor`） | 542.v03d235fee02d | 主控台顏色 | 10 |
| Build Timeout（`build-timeout`） | 1.41 | Freestyle 逾時 | 6 |
| Workspace Cleanup（`ws-cleanup`） | 0.49 | `cleanWs` | 10 |
| Git（`git`） | 5.10.1 | Git SCM | 8 |
| GitHub Branch Source（`github-branch-source`） | 1983.vfa_27ed961853 | GitHub Multibranch、GitHub App | 8 |
| GitLab Branch Source（`gitlab-branch-source`） | 744.vb_d0403d08ec7 | GitLab Multibranch | 8 |
| Credentials Binding（`credentials-binding`） | 728.v902a_273b_8947 | `withCredentials` | 7 |
| SSH Agent（`ssh-agent`） | 433.v9e73d67c3f74 | `sshagent` | 7 |
| HashiCorp Vault（`hashicorp-vault-plugin`） | 384.vda_86ec66c537 | 外部機密 | 7 |
| Kubernetes（`kubernetes`） | 4557.ve746270f672f | Kubernetes agent | 14 |
| Docker Pipeline（`docker-workflow`） | 653.v2f2c08eff0ec | Docker agent | 14 |
| JUnit（`junit`） | 1431.vc0d98912a_756 | 測試報告 | 13 |
| Coverage（`coverage`） | 3.3394.v60e914558d29 | 覆蓋率 | 13 |
| Warnings（`warnings-ng`） | 13.10294.v3c81839da_a_e7 | 靜態分析與掃描報告 | 13、21 |
| SonarQube Scanner（`sonar`） | 2.19.0 | SonarQube 品質門檻 | 13 |
| Pipeline Maven Integration（`pipeline-maven`） | 1760.v9a_a_e6dcb_0444 | `withMaven` | 9 |
| Config File Provider（`config-file-provider`） | 1013.v73c323e52b_1f | `settings.xml` 管理 | 9 |
| Matrix Authorization Strategy（`matrix-auth`） | 3.3 | 授權 | 17 |
| Role-based Authorization Strategy（`role-strategy`） | 918.v91e5468d8db_2 | 授權（大型組織） | 17 |
| OpenId Connect Authentication（`oic-auth`） | 4.718.ve731df6ca_88a_ | SSO | 17 |
| LDAP（`ldap`） | 825.v2fca_37dd5b_cb_ | 目錄整合 | 17 |
| Authorize Project（`authorize-project`） | 534.v2f208c45e11c | 建置執行身分 | 17 |
| Audit Trail（`audit-trail`） | 456.v39d2fd1ed556 | 稽核記錄 | 17 |
| Prometheus metrics（`prometheus`） | 860.v532442b_44e9a_ | 監控 | 19 |
| OpenTelemetry（`opentelemetry`） | 3.1603.ve3fa_cc8a_b_f5e | Pipeline 追蹤 | 19 |
| Email Extension（`email-ext`）、Mailer（`mailer`） | 2038.v7b_8817a_499d9、534.v1b_36f5864073 | 郵件通知 | 19 |
| OWASP Markup Formatter（`antisamy-markup-formatter`） | 173.v680e3a_b_69ff3 | Safe HTML | 17 |
| Versions Node Monitors（`versioncolumn`） | 400.v3c5c3004f31d | 檢查 agent 的 Java 版本 | 20 |
| Support Core（`support-core`） | 1865.v45d40b_778b_cb_ | 支援資訊收集 | 23 |

### C.2 依情境選用

| 情境 | Plugin（ID，2026-10-02 版本） |
| --- | --- |
| Bitbucket | Bitbucket Branch Source（`cloudbees-bitbucket-branch-source` 937.3.10） |
| SAML SSO | SAML（`saml` 4.623.v7875d61cd9f5） |
| Active Directory | Active Directory（`active-directory` 2.971.v653d8b_6e5548） |
| AWS | Amazon EC2（`ec2`）、AWS Secrets Manager Credentials Provider |
| Azure | Azure VM Agents（`azure-vm-agents`）、Azure Key Vault（`azure-keyvault`） |
| Kubernetes 憑證 | Kubernetes Credentials Provider（`kubernetes-credentials-provider`） |
| Slack | Slack Notification（`slack` 795.v4b_9705b_e6d47） |
| HTTP 呼叫 | HTTP Request（`http_request` 1.659.v1b_9d9e942a_e6） |
| 動態參數 | Active Choices（`uno-choice` 2.8.10；腳本需經 Script Approval） |
| 設定變更歷史 | Job Configuration History（`jobConfigHistory` 1380.v762185b_9a_793） |
| 備份 | ThinBackup（`thinBackup` 2.1.5） |
| Node.js | NodeJS（`nodejs` 1.6.6） |
| 相依套件弱點 | OWASP Dependency-Check（`dependency-check-jenkins-plugin` 5.6.5） |
| GitHub Checks | Checks API（`checks-api`）、GitHub Checks（`github-checks`） |
| HTML 報告 | HTML Publisher（`htmlpublisher` 429；搭配 Resource Root URL） |

### C.3 已棄用與不建議

見 [5.4 已棄用 Plugin 與替代方案](#54-已棄用-plugin-與替代方案)。重點：Checkstyle／PMD／FindBugs → Warnings NG；JaCoCo／Cobertura／Code Coverage API → Coverage；Extended Choice Parameter、Folder-based Authorization、GitHub Pull Request Builder 有未修補漏洞；Office 365 Connector 已下架。

## 附錄 D：學習資源

以下連結皆於 2026-10-02 查證。

### D.1 官方文件

| 資源 | 說明 |
| --- | --- |
| [Jenkins User Handbook](https://www.jenkins.io/doc/book/) | 官方使用手冊（安裝、Pipeline、管理、安全、擴充） |
| [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/) | Declarative／Scripted 語法完整參考 |
| [Pipeline Steps Reference](https://www.jenkins.io/doc/pipeline/steps/) | 所有 plugin 提供的 step 與參數 |
| [Pipeline Best Practices](https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/) | 官方 Pipeline 最佳實務 |
| [Scaling Pipelines](https://www.jenkins.io/doc/book/pipeline/scaling-pipeline/)、[CPS method mismatches](https://www.jenkins.io/doc/book/pipeline/cps-method-mismatches/) | Durability 設定與 CPS 限制 |
| [Extending with Shared Libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/) | Shared Library |
| [Configuration as Code](https://www.jenkins.io/doc/book/managing/casc/) | JCasC |
| [Securing Jenkins](https://www.jenkins.io/doc/book/security/securing-jenkins/)、[Controller isolation](https://www.jenkins.io/doc/book/security/controller-isolation/)、[Content Security Policy](https://www.jenkins.io/doc/book/security/csp/) | 安全 |
| [Java Support Policy](https://www.jenkins.io/doc/book/platform-information/support-policy-java/) | Java 版本支援 |
| [LTS Upgrade Guide](https://www.jenkins.io/doc/upgrade-guide/)、[LTS Changelog](https://www.jenkins.io/changelog-stable/) | 升級指南與變更紀錄 |
| [Security Advisories](https://www.jenkins.io/security/advisories/) | 安全公告 |
| [Plugins Index](https://plugins.jenkins.io/) | Plugin 搜尋、版本、安全警示、健康分數 |
| [Tutorials](https://www.jenkins.io/doc/tutorials/) | 官方入門教學（Maven、Node.js、Python、Multibranch） |
| [Kubernetes 安裝](https://www.jenkins.io/doc/book/installing/kubernetes/)、[Helm charts](https://github.com/jenkinsci/helm-charts) | Kubernetes 部署 |

### D.2 線上課程

| 課程 | 平台 | 說明 |
| --- | --- | --- |
| [Jenkins Essentials（LFS267）](https://training.linuxfoundation.org/training/jenkins-essentials-lfs267/) | Linux Foundation | 付費（US$299）、20–25 小時、含實作與數位徽章；涵蓋容器與雲端擴充、Multibranch、IaC 與 GitOps |
| [Continuous Integration and Continuous Delivery (CI/CD)](https://www.coursera.org/learn/continuous-integration-and-continuous-delivery-ci-cd) | Coursera（IBM） | CI/CD 概念與 Jenkins、GitHub Actions、Tekton 實作 |
| [Learn Jenkins by Building a CI/CD Pipeline](https://www.freecodecamp.org/news/learn-jenkins-by-building-a-ci-cd-pipeline/) | freeCodeCamp | 免費影音課程（2022），以 Docker 與 GitHub 建立 Pipeline |
| [Jenkins, From Zero To Hero](https://www.udemy.com/course/jenkins-from-zero-to-hero/) | Udemy | 熱門入門課程（2025-04 更新）；Udemy 頁面無法以自動化工具驗證，請以瀏覽器確認 |

> ⚠️ 第三方課程的 Jenkins 版本常落後。學習時請對照本手冊 [1.5 從 v1.0 基準到 2.580.1 的重大變化](#15-從-v10-基準到-25801-的重大變化) 的版本差異，特別是 Java 需求、Pipeline Graph View、Coverage／Warnings NG 等變化。

### D.3 社群

| 資源 | 說明 |
| --- | --- |
| [Jenkins Community（Discourse）](https://community.jenkins.io/) | 官方討論區，問題與公告 |
| [r/jenkinsci](https://www.reddit.com/r/jenkinsci/) | 官方認可的 Reddit 社群（v1.0 誤植為 r/Jenkins） |
| [Stack Overflow：jenkins 標籤](https://stackoverflow.com/questions/tagged/jenkins) | 問答 |
| [Jenkins Mailing Lists](https://www.jenkins.io/mailing-lists/) | 含 `jenkinsci-advisories` 安全公告預告 |
| [Participate](https://www.jenkins.io/participate/) | 參與貢獻、SIG、Office Hours |
| [Jenkins Blog](https://www.jenkins.io/blog/) | 版本與功能公告 |
| [Meetup：Jenkins 主題](https://www.meetup.com/topics/jenkins/) | 各地聚會 |

### D.4 實戰練習

| 資源 | 說明 |
| --- | --- |
| [jenkins-docs/simple-java-maven-app](https://github.com/jenkins-docs/simple-java-maven-app) | 官方教學使用的 Maven 範例專案（持續維護） |
| [jenkins-docs/building-a-multibranch-pipeline-project](https://github.com/jenkins-docs/building-a-multibranch-pipeline-project) | 官方 Multibranch 教學專案 |
| [jenkinsci/pipeline-examples](https://github.com/jenkinsci/pipeline-examples) | Pipeline 範例集；⚠️ 最後更新於 2023-08，部分範例需依新版語法調整 |
| [jenkinsci/JenkinsPipelineUnit](https://github.com/jenkinsci/JenkinsPipelineUnit) | Shared Library 單元測試框架（v1.31） |
| 本機練習環境 | 依 [3.5 Docker／Podman 容器部署](#35-dockerpodman-容器部署) 的 Compose 範例在本機啟動 controller＋agent |

> 📌 v1.0 推薦的 Katacoda 已於 2022 年停止服務，該連結回傳 404，已移除。

### D.5 書籍

| 書名 | 作者／出版 | 說明 |
| --- | --- | --- |
| *Learning Continuous Integration with Jenkins*（第 3 版） | Nikhil Pathania／Packt，2024-01 | 涵蓋雲端、容器、IaC、GitOps 與 AI 輔助撰寫 Pipeline，三本中最新 |
| *Jenkins 2: Up and Running* | Brent Laster／O'Reilly，2018 | Pipeline 概念說明完整，但版本較舊 |
| *Jenkins: The Definitive Guide* | John Ferguson Smart／O'Reilly，2011 | ⚠️ Jenkins 1.x 時代，內容多已過時，僅供歷史參考 |

### D.6 v1.0 學習資源連結查證結果

| v1.0 項目 | 查證結果（2026-10-02） | v2.0 處理 |
| --- | --- | --- |
| Jenkins 官方文檔、Pipeline 語法參考、外掛程式索引 | 正常 | 保留並擴充（D.1） |
| Jenkins X 文檔 | 網站存在，但 Jenkins X 是以 Tekton 為基礎的另一個專案，與 Jenkins 不相容 | 移除，於 1.1 說明差異 |
| Udemy「jenkins-beginner-to-guru」 | 頁面拒絕自動化存取（403），搜尋查無此課程名稱 | 改列可查證的熱門課程並註明需人工確認 |
| Coursera「continuous-integration-deployment」 | 404 | 改為 IBM「Continuous Integration and Continuous Delivery (CI/CD)」 |
| A Cloud Guru「devops-engineer」 | 301 轉址到 Pluralsight 首頁（A Cloud Guru 已併入 Pluralsight），原課程不存在 | 移除 |
| Jenkins 用戶社群（community.jenkins.io） | 正常 | 保留 |
| Stack Overflow jenkins 標籤 | 存在（網站拒絕自動化工具抓取） | 保留 |
| Reddit r/Jenkins | 官方社群為 r/jenkinsci | 更正 |
| Meetup Jenkins 主題 | 正常 | 保留 |
| jenkins-docs/simple-java-maven-app | 正常，持續維護 | 保留 |
| jenkinsci/pipeline-examples | 存在，最後更新 2023-08 | 保留並加註 |
| Katacoda Jenkins | 404（服務已於 2022 年關閉） | 移除 |
| 書籍 3 本 | 皆存在；*Learning CI with Jenkins* 已有 2024 年第 3 版 | 更新版本資訊 |
| 「Blue Ocean CLI」（`npm install -g blueocean-cli`） | npm registry 回傳 404，**此套件不存在** | 移除 |
| 「JenkinsFile Runner」 | 專案存在，但最新版仍為 1.0-beta-32（2023-11） | 不列為推薦工具 |

## 附錄 E：認證

### E.1 Jenkins 相關認證現況

| 認證 | 現況（2026-10-02） | 說明 |
| --- | --- | --- |
| CloudBees Certified Jenkins Engineer（CJE） | ⚠️ **無法確認**：社群回報 CloudBees 網站的報名連結失效，官方未公告停辦也未提供新的報名管道 | 有意報考者請直接洽詢 CloudBees；v1.0 列出的考試主題權重無官方依據，v2.0 已移除 |
| Linux Foundation Jenkins Essentials（LFS267） | 課程提供數位徽章，非正式認證考試 | 適合作為內部教育訓練 |

### E.2 相關技術認證與本手冊章節對應

| 認證 | 發證單位 | 相關章節 |
| --- | --- | --- |
| Certified Kubernetes Administrator（CKA） | CNCF／Linux Foundation | 3.6、14.4、15、16.3 |
| AWS Certified DevOps Engineer – Professional | AWS | 14.5、16、19、21 |
| Microsoft Certified: DevOps Engineer Expert（AZ-400） | Microsoft | 7.5、8、13、16 |
| Google Cloud Professional Cloud DevOps Engineer | Google Cloud | 16、19、22.3 |
| Docker Certified Associate（DCA） | Mirantis（2019 年隨 Docker Enterprise 移轉） | 3.5、15 |
| CompTIA Security+、ISC2 CSSLP 等資安認證 | CompTIA、ISC2 | 7、17、21 |

> 💡 企業內部可依本手冊的閱讀指引（文件資訊後）設計內部認證：每個角色完成指定章節的實作（例如以 JCasC 建立 controller、撰寫通過品質門檻的 Pipeline、完成一次還原演練），比單純通過選擇題更能反映實務能力。

## 附錄 F：版本紀錄

### F.1 版本歷程與章節對照

| 版本 | 日期 | 說明 |
| --- | --- | --- |
| 1.0 | 2024-03-10 | 初版：19 章＋附錄 A–G，以 Jenkins LTS 2.401.x 為基準，對象為新進 Java 開發者 |
| 2.0 | 2026-10-02 | 重新編排為 24 章＋附錄 A–I；對齊 Jenkins LTS 2.580.1、Java 21／25；以企業標準技術白皮書等級改寫；所有程式碼範例以本機 Jenkins 2.580.1 驗證；修正 F.2 所列問題；精簡無法查證的虛構腳本（原 21,038 行） |

**章節對照（v1.0 → v2.0）**：

| v1.0 | v2.0 |
| --- | --- |
| 教學手冊說明 | 文件資訊、閱讀指引 |
| 第 1 章 Jenkins 簡介與核心概念 | 1. 概觀與版本基準、2. 架構與核心概念 |
| 第 2 章 環境安裝與基本設定 | 3. 安裝與初始設定、17. 安全強化 |
| 第 3 章 Jenkins 介面導覽 | 4. 介面導覽與系統管理 |
| 第 4 章 Plugin 管理與基礎設定 | 5. Plugin 管理、9.1 工具管理 |
| 第 5 章 Freestyle Project 入門 | 6. Job 類型與 Freestyle |
| 第 6 章 憑證與密碼管理 | 7. 憑證與機密管理 |
| 第 7 章 Git 整合與版本控制 | 8. SCM 整合 |
| 第 8 章 Maven 建置整合 | 9. 建置工具整合（Maven、Gradle 與多語言） |
| 第 9 章 Pipeline 基礎與 Declarative Syntax | 10. Declarative Pipeline 完整語法 |
| 第 10 章 Jenkinsfile 結構深度分析 | 10、11. Scripted Pipeline 與 CPS、12. Shared Libraries |
| 第 11 章 測試報告與程式碼覆蓋率整合 | 13. 測試報告、覆蓋率與品質門檻 |
| 第 12 章 靜態程式碼分析與品質檢查 | 13.3–13.5 |
| （第 12 章後的「總結」） | 移除（內容併入各章「本章重點」） |
| 第 13 章 Pipeline 故障排除與除錯技巧 | 11.6–11.7、23. 故障排除 |
| 第 14 章 部署策略與環境管理 | 16. 部署策略與環境管理 |
| 第 15 章 監控、通知與效能優化 | 19. 監控、日誌、效能與通知 |
| 第 16 章 企業級 CI/CD 架構設計 | 2.7 參考架構、20.4 高可用、21.6 法規對應、22. 企業導入 |
| 第 17 章 容器化與雲端整合 | 14. Agent 與雲端節點、15. 容器映像建置與 Kubernetes 上的 Jenkins |
| 第 18 章 DevOps 文化與實務 | 22.2–22.4 |
| 第 19 章 實務案例研究 | 22.5–22.7 |
| 附錄 A 常用指令參考 | 附錄 A 指令與 API 速查 |
| 附錄 B 配置範例 | 附錄 B 範本索引（範例改放在各章） |
| 附錄 C 故障排除指南 | 23. 故障排除 |
| 附錄 D 最佳實踐清單 | 24. 檢查清單 |
| 附錄 E 工具和資源 | 附錄 C Plugin 建議清單、附錄 D 學習資源 |
| 附錄 F 認證考試對照 | 附錄 E 認證 |
| 附錄 G 版本更新歷史 | 附錄 F 版本紀錄 |
| — | 新增：17 安全強化、18 JCasC 與 Job DSL、20 備份升級與高可用、21 供應鏈安全、附錄 G 查證紀錄、附錄 H 術語表、附錄 I 實作練習（取代 v1.0 各章的「練習作業」與「認證對應知識點」） |

### F.2 v1.0 → v2.0 更正對照表

| # | v1.0 位置 | v1.0 內容 | 問題 | v2.0 更正 |
| --- | --- | --- | --- | --- |
| 1 | 2.2 系統需求 | Java：JDK 11 或更高版本 | 2.479.1 起需要 Java 17，2.555.1 起只支援 Java 21／25（controller 與所有 agent） | 1.4、3.1 |
| 2 | 2.4 方法一 | 下載 `war-stable/latest` | 版本不固定，無法重現與回退 | 指定 2.580.1 並比對 SHA-256（3.2） |
| 3 | 2.4 方法一 | PowerShell 中使用 `C:\Users\%USERNAME%\...` | `%USERNAME%` 是 cmd.exe 語法，PowerShell 不會展開 | 改用 `$env:JENKINS_HOME`（3.2） |
| 4 | 2.4 方法二 | PowerShell 區塊中以 `\` 續行的 `docker run` | PowerShell 無法執行 bash 續行 | 改為 Compose 與正確的 shell 標示（3.5） |
| 5 | 2.4、2 章案例 | Compose 使用 `version: '3.8'` | Compose v2 已不使用 `version` 欄位 | 移除（3.5） |
| 6 | 2.4、2 章案例、17 章 | 把 `/var/run/docker.sock` 掛進 controller | 能執行建置或 Script Console 的人即可取得主機 root | 禁止；改用 agent 與無 daemon 映像建置（3.5、15.1） |
| 7 | 2 章案例 | `jenkins/inbound-agent:latest`，`JENKINS_SECRET` 明文寫在 Compose | 版本不固定；secret 外洩 | 固定映像版本、`JENKINS_SECRET=@檔案`、WebSocket（3.5） |
| 8 | 2.4 方法三、2.4 JVM 設定 | 在 PowerShell 區塊中放 `jenkins.xml` 的 XML；未提及 MSI 預設 heap | XML 無法在 PowerShell 執行；MSI 預設 `-Xmx256m` 不足 | 分開 XML 區塊並說明預設值（3.4） |
| 9 | 2.4 方法三 | 未說明服務帳號 | 預設 LocalSystem 權限過大 | 使用專用服務帳號（3.4） |
| 10 | 2.3 | 「啟用 Prevent Cross Site Request Forgery exploits」 | CSRF 保護已預設啟用且無法在 UI 關閉；2.555.1 起 crumb 不再綁定 IP | 17.6 |
| 11 | 2.5 | 代理設定在「Manage Plugins → Advanced」 | 新版名稱為 Plugins → Advanced settings | 4.2 |
| 12 | 2.4 | Script Console 逐一改寫所有 Job 的 `buildDiscarder` | 對 Multibranch 子 Job 無效、無法追蹤 | Global Build Discarders 與 `buildDiscarder` 選項（19.6） |
| 13 | 第 3 章 | 「左側選單 → Manage Jenkins」等舊版介面描述 | 2.516.1 起標頭重新設計 | 4.1 |
| 14 | 4.3、4.4、4.6 | 必要 plugin 清單含 `checkstyle`、`jacoco`、`maven-plugin`、`blueocean` | Checkstyle 已下架；JaCoCo 長期未發行；Maven project 與 Blue Ocean 不建議新導入 | 基準清單與替代方案（5.3、5.4、附錄 C） |
| 15 | 4.4 | `init.groovy.d` 腳本在啟動時從 update center 安裝 plugin | 每次啟動版本可能不同、無法審查 | `plugins.txt`＋Plugin Installation Manager Tool（5.3） |
| 16 | 4.4 | `install-jenkins-plugins.sh` 以表單參數呼叫 `/pluginManager/installNecessaryPlugins` | 該端點需要 XML（`<install plugin="..."/>`），範例無法安裝 | 改用 PIMT（5.3） |
| 17 | 4.7 | `check-plugin-updates.sh` 以 `jq` 解析 `update-center.json` 並讀取 `securityWarnings` | `update-center.json` 是 JSONP 格式，且無此欄位 | `PIMT --available-updates --view-security-warnings`（5.3、17.9） |
| 18 | 4.6 `jenkins-plugins.yml` | plugin ID `blue-ocean` | 正確 ID 為 `blueocean` | 附錄 C 以實際 ID 列出 |
| 19 | 第 1 章等 | 「Master」 | 2020 年起官方用語為 controller | 全面改用 controller／agent |
| 20 | 多處 | 大量 `agent any`，且未將 built-in node executor 設為 0 | 建置可能在 controller 上執行 | 2.1、10.2、17.5 |
| 21 | 5.4 | 定期建置與 SCM 輪詢為主要觸發方式 | 輪詢拖慢 SCM 與 Jenkins | Webhook 為主、每日掃描為輔（6.3、8.5） |
| 22 | 8–11、19 章多個範例 | `tools { maven 'Maven-3.9'; jdk 'JDK-17' }`、`'Maven 3.8.6'`、`'OpenJDK 17'` 等不一致的工具名稱 | 4 個範例因工具名稱不存在而驗證失敗 | 統一為 `maven-3.9`、`jdk-21`，並建議容器化（9.1） |
| 23 | 9.3、9.5、第 9 章案例、10.1、12.3、第 13 章案例、14.2、19.1 的 8 個 Jenkinsfile | `when { params.X }` 等裸布林運算式 | 共 22 處「Expected a when condition」，Pipeline 無法啟動 | `expression { params.X }`（10.6） |
| 24 | 7.6 分支特定建置策略 | `environment` 中以跨多行的三元運算式計算 `BRANCH_TYPE`，寫在一般雙引號字串內 | 一般雙引號字串不能跨行，產生「end of line reached within a simple string」語法錯誤 | 以 `when { branch }` 判斷，需要計算時放在 `script {}`（8.7、10.3） |
| 25 | 10.2 | `environment { APP_NAME = config.appName }` | 「Environment variable values must either be single quoted, double quoted, or function calls」 | 10.3 |
| 26 | 7.7 GitHub Webhook | 以 Script Console 呼叫 `gitHubConfig.setOverrideHookUrl(...)` 設定 webhook | 以 Script Console 修改設定無法追蹤 | 以 JCasC／GitHub App 設定（8.2） |
| 27 | 18.1 | `sh """..."""` 中的 `grep -o "[0-9]\+%"` | `\+` 在 Groovy 雙引號字串中是非法跳脫，產生「unexpected char: ''」 | 不需要 Groovy 內插的 shell 一律使用單引號三引號字串（10.3） |
| 28 | 9.3、9.6、10.2 | 在 `script {}` 中呼叫 `input` 並讀取 `env.DEPLOYER` | `submitterParameter` 的值是 `input` 的回傳值，`env.DEPLOYER` 為空；等待期間占用 agent、未設逾時 | stage 層級 `input`＋`timeout`（10.9、16.2） |
| 29 | 11.3 | `jacoco(execPattern: ..., minimumInstructionCoverage: ...)` | JaCoCo plugin 已由 Coverage plugin 取代 | `recordCoverage`（13.2） |
| 30 | 12 章 | Checkstyle、PMD plugin 與自行解析 XML 的 Groovy | plugin 已下架；在 controller 上解析 XML 消耗資源 | `recordIssues`（13.3） |
| 31 | 7.7 | Webhook Payload URL 使用 `http://` | 未加密傳輸，secret 與內容可被攔截 | HTTPS＋secret（8.5） |
| 32 | 15 章 | Teams 通知 | Microsoft 365 Connectors 已停用、Office 365 Connector plugin 已下架 | Teams Workflows webhook（19.7） |
| 33 | 16.2 | SOX、GDPR、ISO 27001「合規檢查」腳本 | 以字串比對模擬合規，無法作為合規依據 | 改為控制措施與稽核證據對應（21.6） |
| 34 | 17.1 | `docker:24-dind` 搭配 `--privileged` 又同時掛載 `docker.sock` | 兩種做法互相矛盾，且都會給予主機層級權限 | BuildKit rootless（15.2） |
| 35 | 17.1 | `gcr.io/kaniko-project/executor:latest` | Kaniko 原專案已於 2025-06 封存；`latest` 不可重現 | 15.1 說明現況與替代 |
| 36 | 17.2 | Kubernetes Deployment 使用 `jenkins/jenkins:lts-jdk17` 並掛載 `docker.sock` | Java 17 映像已於 2.555.1 停止提供；以 Deployment 自建維護成本高 | 官方 Helm chart（3.6、15.5） |
| 37 | 16、19 章 | 大量無法查證的架構與效益數字 | 讀者可能誤以為實際數據 | 案例改為明確標示的示意情境（22.5、22.6） |
| 38 | 附錄 E.1 | 「Blue Ocean CLI：`npm install -g blueocean-cli`」 | npm 上不存在此套件 | 移除（D.6） |
| 39 | 附錄 E.2 | Katacoda、A Cloud Guru、Coursera、Udemy、Jenkins X、r/Jenkins 連結 | 失效、轉址或不正確 | D.6 逐項更正 |
| 40 | 附錄 F | CloudBees CJE 考試主題與權重 | 無官方依據；認證現況不明 | 附錄 E |
| 41 | 附錄 G | 「Version 1.1.0（預計 2024-06-01）」等未實現的計畫 | 過期資訊 | 附錄 F |
| 42 | 第 12 章後 | 插入「## 總結」並寫「完成前 12 章」 | 打斷章節結構 | 移除 |
| 43 | 附錄 D、E、G | 內容包在 ```` ```markdown ```` 程式碼區塊中 | 標題不會成為真正的標題，也無法連結 | 改為一般 Markdown |
| 44 | 第 15–19 章 | 小節標題樣式與前 14 章不同（「目標導向」「架構願景」等） | 結構不一致 | 全書統一為「章 → 節」編號 |
| 45 | 目錄 | 只列章名與部分附錄小節；未使用 TOC 標記 | 323 個標題中大多數小節無法從目錄連結；「注意事項」等標題重複 14 次造成錨點重複 | H2＋H3 自動目錄、所有小節唯一編號（附錄 G） |
| 46 | 全文 | 行尾空白、清單與標題前缺空行（MD009 15、MD032 30、MD022 19 處） | Markdown 格式問題 | 已修正（附錄 G） |

## 附錄 G：查證紀錄

查證日期：2026-10-02。方法：

- **版本號與發行資訊**：Jenkins LTS changelog、`updates.jenkins.io` 的 update center JSON（以 `version=2.580.1` 取得，共 2,116 個 plugin 的版本、相依、棄用與安全警示）、Docker Hub tag API、GitHub Releases（`gh api`）
- **官方文件**：以 `gh api` 讀取 `jenkins-infra/jenkins.io` 原始 AsciiDoc（Java 支援政策、LTS 升級指南 2.479.1–2.580.1、安裝、反向代理、systemd、安全公告）
- **原始碼**：`jenkinsci/packaging`（MSI）、`jenkinsci/docker-agent`（inbound agent 啟動腳本）、`jenkinsci/helm-charts`（`values.yaml`、`_helpers.tpl`）、`jenkinsci/gitlab-branch-source-plugin`、`jenkinsci/coverage-plugin`、`jenkinsci/plugin-util-api-plugin`、`jenkinsci/warnings-ng-plugin`、`jenkinsci/analysis-model`、`helm/helm`、`moby/buildkit`、`sigstore/cosign`
- **實機驗證**：在本機以 Java 21 啟動 Jenkins **2.580.1** WAR，安裝 146 個 plugin（含相依），以 JCasC 建立管理員、節點與工具設定後，對本手冊所有程式碼區塊執行：
  - Declarative Jenkinsfile：`POST /pipeline-model-converter/validate`
  - Scripted Pipeline、Shared Library、Groovy 腳本：在 Jenkins 的 Groovy 環境（含 Pipeline 預設匯入）編譯
  - 未註冊的 step／symbol 檢查：比對 Jenkins 實際註冊的 724 個 step 名稱與 `@Symbol`
  - JCasC：`POST /configuration-as-code/check`
  - Job DSL：以 `DslScriptLoader` 實際執行並建立 Job
  - Script Console 範例（唯讀）：實際執行
  - CLI：`declarative-linter`、`help`（WebSocket 模式）
  - Prometheus 指標名稱：實際抓取 `/prometheus/`；告警規則與抓取設定以 `promtool` 3.15.0 驗證
  - JenkinsPipelineUnit 測試：以 Maven＋GMavenPlus 建立 Library 專案實際執行
  - bash：`bash -n`；PowerShell：PowerShell 語法剖析器；YAML／JSON：解析
- **網頁與連結**：WebFetch、HTTP 狀態檢查、網路搜尋；無法自動化存取的網站另行註明

**驗證結果統計**：

| 驗證類型 | 區塊數 | 結果 |
| --- | --- | --- |
| Declarative Jenkinsfile（`pipeline-model-converter/validate`） | 42 | 全部通過 |
| Scripted Pipeline／Shared Library／Groovy（編譯） | 11 | 全部通過 |
| JenkinsPipelineUnit 測試（Maven 實際執行） | 2 個區塊（`build.gradle` 對應設定與測試類別），2 個測試 | 全部通過 |
| JCasC（`configuration-as-code/check`） | 20 | 全部通過 |
| Job DSL（`DslScriptLoader` 實際執行） | 5 | 全部通過，共建立 folder、Multibranch、Organization Folder、Pipeline Job |
| Script Console 唯讀腳本（實際執行） | 2 | 全部通過 |
| Prometheus 告警規則與抓取設定（`promtool` 3.15.0） | 2 | 全部通過（6 條規則） |
| YAML（含 Compose、Helm values、Kubernetes manifest） | 28 | 全部可解析 |
| bash（`bash -n`） | 23 | 全部通過 |
| PowerShell（語法剖析） | 4 | 全部通過 |
| XML | 2 | 全部可解析 |
| Mermaid 圖表 | 28 | 以 `mermaid` 11 官方 parser（jsdom）逐一解析全部通過；過程中修正 2 處含 `@` 的節點標籤（改以雙引號包住） |

**格式與連結驗證**：

| 檢查 | 結果 |
| --- | --- |
| repo `check-toc.ps1` | 標題 253 個、TOC 連結 242 個；找不到對應標題 0、未收錄的編號標題 0、重複錨點 0（v1.0：323 個標題，大多數小節未收錄於目錄，「注意事項」等錨點重複最多 14 次） |
| repo `check-md.ps1` | 未標語言的程式碼區塊 0、其他格式問題 0（v1.0：MD032 30、MD022 19、MD009 15） |
| repo `test-mermaid-syntax.ps1` | 未發現語法問題 |
| Hugo 實際渲染（`hugo -d <暫存目錄>`） | 頁內連結 604 個（254 個不同目標）全部對應到標題 ID，只有佈景主題的 `#top` 未對應（預期） |
| 檔案格式 | UTF-8（無 BOM）、CRLF，與原檔一致 |

**查證項目與結論**：

| # | 項目 | 結論 | 依據 |
| --- | --- | --- | --- |
| 1 | LTS 版本 | 2.580.1（2026-09-30）；前一線 2.568.3（2026-09-02）；Weekly 2.584（2026-09-28） | changelog-stable、changelog |
| 2 | Java 需求 | 2.555.1 起 Java 21 或 25；適用 controller、agent、CLI；建置用 JDK 不受限 | `support-policy-java.adoc`、`2-555-1.adoc` |
| 3 | LTS 週期 | 每 12 週選基準，`.1`／`.2`／`.3` 每 4 週一版，發行前 2 週 RC | `download/lts/index.adoc` |
| 4 | 各 LTS 線重大變化 | 2.479.1（Java 17、Spring Security 6）、2.492.1（agentProtocols）、2.504.1（YUI、jCIFS 移除）、2.516.1（標頭、bcrypt 72 bytes、SameSite）、2.528.1（Trixie、Timestamper）、2.541.1（CSP、RPM 統一、新 GPG key）、2.555.1（Java 21、crumb 不含 IP）、2.568.1（Windows 2019 映像）、2.580.1（detached plugin 移出 war） | `content/_data/upgrades/*.adoc` |
| 5 | 容器映像 tag | `2.580.1-lts-jdk21`、`-jdk25`、`-rhel-ubi9-jdk21`、`-windowsservercore-ltsc2022／2025` 等；inbound-agent `3391.va_37fa_a_305d6d-3-jdk21` | Docker Hub API |
| 6 | Linux 套件 | Debian：`jenkins.io-2026.key`、`/etc/apt/keyrings/jenkins-keyring.asc`；RPM：`rpm-stable/jenkins.repo`；Java 套件 `openjdk-21-jre`／`java-21-openjdk` | `installing/linux.adoc` |
| 7 | MSI 預設值 | `JENKINS_HOME`＝服務帳號 `%LocalAppData%\Jenkins\.jenkins`（LocalSystem 時 `%ProgramData%\Jenkins\.jenkins`）；`-Xmx256m`；無人值守屬性 `INSTALLDIR`、`PORT`、`JAVA_HOME`、`SERVICE_USERNAME`、`SERVICE_PASSWORD` | `packaging/msi/build/jenkins.wxs`、`installing/windows.adoc` |
| 8 | Inbound agent 環境變數 | 支援 `JENKINS_URL`、`JENKINS_SECRET`、`JENKINS_AGENT_NAME`、`JENKINS_WEB_SOCKET`、`JENKINS_AGENT_WORKDIR` 等；無 `JENKINS_SECRET_FILE`，以 `JENKINS_SECRET=@檔案` 讀檔 | `docker-agent/jenkins-agent` |
| 9 | Agent 啟動指令 | `java -jar agent.jar -url ... -secret ... -name "..." -webSocket -workDir "..."` | 本機 2.580.1 節點頁面 |
| 10 | Helm chart | 5.9.64、appVersion 2.568.3；明確指定 `controller.image.tag` 時不附加 tagLabel；`replicas` 最大 1；`additionalExistingSecrets` 在 JCasC 以 `${secret-key}` 引用 | `helm-charts` 原始碼 |
| 11 | Setup wizard 建議 plugin | 含 Pipeline Graph View、Dark Theme；不含 Stage View | `jenkins/core/.../platform-plugins.json` |
| 12 | Manage Jenkins 分區 | System Configuration、Security、Status Information、Troubleshooting、Tools and Actions | 本機 2.580.1 |
| 13 | Plugin 棄用與漏洞 | Checkstyle／PMD／FindBugs、Extended Choice Parameter 列於 deprecations；Extended Choice Parameter、Folder-based Authorization、GHPRB 有未修補警示；Office 365 Connector、`blueocean-cli` 不存在 | update center JSON、npm registry |
| 14 | 基準 `plugins.txt` | 40 個 plugin 以 2.580.1 解析通過，無安全警示 | PIMT 2.15.0 `--no-download --view-security-warnings` |
| 15 | GitLab Branch Source JCasC | `secretToken` 已 deprecated（check 端點拒絕）；改用 `webhookSecretCredentialsId` | 原始碼 `GitLabServer.java`＋本機驗證 |
| 16 | GitHub App | 需要 PKCS#8 私鑰；權限 Commit statuses（RW）、Contents（R）、Metadata（R）、Pull requests（R）；JCasC `gitHubApp` | `github-branch-source` 文件 |
| 17 | Shared Library JCasC | `globalLibraries` 與 `globalUntrustedLibraries` 皆有效 | 本機 check 與 schema |
| 18 | JenkinsPipelineUnit | v1.31（2026-07）；需 Java 21、Groovy 2.4.21；範例測試 2 個通過 | GitHub Releases、本機 Maven 執行 |
| 19 | Coverage／Warnings NG 門檻 | 失敗等級欄位為 `criticality`（`NOTE`／`UNSTABLE`／`ERROR`／`FAILURE`）；Coverage baseline 與 Warnings NG 門檻類型列舉 | `plugin-util-api`、`coverage-plugin`、`warnings-ng-plugin` 原始碼 |
| 20 | Trivy 嚴重度對應 | Critical → ERROR、High → HIGH | `analysis-model` 的 `TrivyParser` |
| 21 | SonarQube JCasC | `unclassified.sonarglobalconfiguration.installations` | `sonarqube-plugin` 測試資源 |
| 22 | BuildKit rootless | `moby/buildkit:v0.33.1-rootless`；`BUILDKITD_FLAGS=--oci-worker-no-process-sandbox`、seccomp／AppArmor Unconfined | `moby/buildkit` 範例 |
| 23 | Kaniko | 原專案 2025-06-03 封存；Chainguard 維護分支 | GitHub API |
| 24 | Helm 4 | 4.3.0；`--atomic` deprecated → `--rollback-on-failure`；`--wait` 預設 watcher | `helm/helm` 原始碼 |
| 25 | 安全 JCasC | `oic`（含 `pkce`、`escapeHatch`）、`ldap`、`globalMatrix`、`roleBased`、`queueItemAuthenticator`、`contentSecurityPolicy.enforce`、`resourceRoot`、`audit-trail` 皆通過 check | 本機 schema 與 check |
| 26 | JCasC 棄用設定 | `agentProtocols` 回報 deprecated；`crumbIssuer.standard.excludeClientIPFromCrumb` 回報為無效屬性 | 本機 check |
| 27 | WebSocket CLI | 未設定 Jenkins URL 時握手回 403（`X-CLI-Error: Jenkins URL is not configured`） | 本機實測 |
| 28 | 2026 安全公告 | 1–9 月 9 次，5 次影響 core（02-18、03-18、06-10、08-05、09-02） | `content/security/advisory/2026-*.adoc` |
| 29 | Prometheus 指標名稱 | 第 19 章所列指標皆存在於本機 `/prometheus/` | 本機抓取 |
| 30 | 工具版本 | Maven 3.9.16／3.10.0（2026-10-01）、Maven 4 仍為 RC；Gradle 9.8.0；Jib 3.5.2；Trivy 0.75.0；Syft 1.54.0；Grype 0.119.0；Cosign 3.1.3；Gitleaks 8.30.1；Argo CD 3.5.3；Argo Rollouts 1.10.0；CycloneDX Maven 2.9.3 | GitHub Releases、Docker Hub |
| 31 | v1.0 Declarative 範例 | 42 個中 15 個驗證失敗：11 個語法錯誤（`when` 22 處、`environment` 2 處、字串 1 處、跳脫字元 1 處等）＋4 個僅工具名稱不存在 | 本機驗證端點 |
| 32 | 學習資源 | 見 [D.6 v1.0 學習資源連結查證結果](#d6-v10-學習資源連結查證結果) | WebFetch、HTTP 狀態、網路搜尋 |

**驗證過程中發現並修正的錯誤**（撰寫 v2.0 草稿時）：

| 項目 | 發現方式 | 修正 |
| --- | --- | --- |
| GitLab Branch Source 的 `secretToken` | JCasC check 回報 deprecated | 改為 `webhookSecretCredentialsId`（8.3） |
| Job DSL 範例缺少父 folder | DslScriptLoader 回報「unknown parent path」 | 補上 `folder('platform-ops')`（18.4） |
| Coverage plugin README 的 `unstable: true` | 原始碼比對 | 改用 `criticality` |
| Compose 中虛構的 `JENKINS_SECRET_FILE` | 比對 `docker-agent` 啟動腳本 | 改為 `JENKINS_SECRET=@檔案`（3.5） |
| 職責分離範例依賴未安裝 plugin 的 `BUILD_USER_ID` | step 與變數檢查 | 改用 `currentBuild.getBuildCauses()`（16.2） |
| 2026 安全公告影響 core 的次數 | 讀取公告原始檔 | 由「2 次」更正為「5 次」（17.9） |

### G.1 待確認事項

| # | 項目 | 狀態與後續 |
| --- | --- | --- |
| 1 | 2.580.2／2.580.3 與下一條 LTS 基準 | 預估 2.580.2 約 2026-10-28；發行後檢視 changelog 與升級指南，更新 1.3–1.5、20.3 |
| 2 | Helm chart 對應 2.580.1 的 appVersion | 目前 5.9.64 的 appVersion 為 2.568.3；新版 chart 發行後更新 3.6、15.5 |
| 3 | Weekly 中的實驗性新版 Dashboard／Job UI | 2.58x weekly 已加入初步實作；進入 LTS 時更新第 4 章 |
| 4 | CloudBees CJE 認證現況 | 官方報名管道不明；確認後更新附錄 E |
| 5 | Cosign v3 關閉公開透明度記錄的參數 | 文件範例仍有 `--tlog-upload=false`，但選項清單已無此參數；以實際版本 `--help` 確認後更新 21.4 |
| 6 | 臺灣法規條號 | 資通安全管理法 2025 年修正後的子法條號、金管會「金融資安行動方案」最新版次、銀行公會自律規範全文，需以全國法規資料庫與主管機關公告確認（21.6） |
| 7 | Udemy 課程頁面 | 網站拒絕自動化存取，D.2 所列課程需以瀏覽器人工確認 |
| 8 | MSI 實際安裝結果 | `JENKINS_HOME` 與預設 heap 取自 MSI 原始碼，尚未以實際 Windows 安裝確認 |
| 9 | Maven 3.10.0 | 2026-10-01 剛發行，相容性需以實際專案驗證後再列為基準 |
| 10 | Kaniko 分支的長期維護 | 追蹤 Chainguard 分支的發行狀況（15.1） |
| 11 | JenkinsPipelineUnit 對 Groovy 4 的支援 | 官方 issue #521 追蹤中 |
| 12 | 上游文件與實作不一致 | GitLab Branch Source README（`secretToken`）、Coverage README（`unstable: true`）、Cosign 文件範例；上游更新後移除 v2.0 中的對應說明 |

## 附錄 H：術語表

| 術語 | 說明 |
| --- | --- |
| Agent | 執行建置的節點，透過 remoting 與 controller 連線（舊稱 slave） |
| Agent → Controller 安全 | 限制 agent 對 controller 的存取，2.326 起永遠啟用 |
| Artifact | 建置產物；大型產物應存放在外部儲存庫 |
| Authorize Project | 讓建置以觸發者或指定使用者身分執行的 plugin |
| Branch Source | Multibranch 用來掃描 repository 分支、PR、tag 的設定 |
| Built-in node | Controller 本身的節點（舊稱 master node），不應執行建置 |
| CloudBees CI | 以 Jenkins LTS 為基礎的商業發行版 |
| Cloud（Jenkins） | 動態建立 agent 的設定（Kubernetes、EC2 等） |
| Content Security Policy（CSP） | 限制網頁可載入資源的瀏覽器安全機制；2.541.1 起 Jenkins core 內建 |
| Controller | Jenkins 主伺服器，負責 UI、排程、設定與 Pipeline 解譯（舊稱 master） |
| CPS（Continuation Passing Style） | Pipeline 解譯 Groovy 的方式，讓 Pipeline 可在重啟後恢復 |
| Credentials | 憑證；Pipeline 以 ID 引用 |
| Declarative Pipeline | 結構固定、可驗證的 Pipeline 語法（`pipeline {}`） |
| Detached plugin | 從 core 拆分出來的 plugin；2.580.1 起不再打包於 war |
| Digest | 容器映像內容的 SHA-256 雜湊，部署時應以 digest 指定 |
| DORA 指標 | 衡量軟體交付效能的指標：部署頻率、前置時間、變更失敗率、恢復時間、重工率 |
| Durability | Pipeline 狀態寫入磁碟的頻率等級（`MAX_SURVIVABILITY`、`PERFORMANCE_OPTIMIZED` 等） |
| Executor | Agent 上的執行槽 |
| Folder | 組織 Job 的容器，可設定權限、憑證與 Library |
| GitHub App | GitHub 的應用程式身分，用於 API 與 checkout 驗證 |
| GitOps | 以 Git 為部署狀態的唯一來源，由叢集內控制器自動同步 |
| Golden Path（黃金路徑） | 平台團隊提供的標準、安全的預設做法 |
| `input` | Pipeline 的人工核准步驟 |
| JCasC（Jenkins Configuration as Code） | 以 YAML 管理 Jenkins 系統設定 |
| `JENKINS_HOME` | Jenkins 的資料目錄 |
| Job DSL | 以 Groovy DSL 描述與建立 Job 的 plugin |
| Label | 標記 agent 能力的標籤，Pipeline 以 label 表達式選擇 agent |
| LTS（Long-Term Support） | 每 12 週選定基準、每 4 週發行修補版的穩定發行線 |
| Milestone | 確保較新的建置通過後，較舊的建置不會在其後部署的機制 |
| Multibranch Pipeline | 依 repository 的分支與 PR 自動建立 Pipeline 的 Job 類型 |
| `@NonCPS` | 標記不經 CPS 轉換的方法，只能做純運算 |
| Organization Folder | 掃描整個 GitHub organization／GitLab group 自動建立 Multibranch |
| PIMT（Plugin Installation Manager Tool） | 依 `plugins.txt` 解析與下載 plugin 的官方工具（容器中的 `jenkins-plugin-cli`） |
| Pipeline Graph View | Pipeline 視覺化 plugin，取代 Stage View 的建議選擇 |
| PPE（Poisoned Pipeline Execution） | 透過修改 Pipeline 定義在 CI 中執行惡意程式碼的攻擊 |
| Provenance | 描述產物如何、由誰、從哪些來源建置的中繼資料（SLSA） |
| Remoting | Controller 與 agent 之間的通訊程式庫（`agent.jar`） |
| Replay | 修改本次建置的 Pipeline 內容後重新執行的功能 |
| Resource Root URL | 以獨立網域提供建置產物與報告，避免 XSS 影響 Jenkins |
| SBOM（Software Bill of Materials） | 軟體物料清單，列出產物包含的所有元件 |
| Script Approval | 管理員核准沙箱外方法呼叫的機制 |
| Script Console | 以 controller 權限執行任意 Groovy 的管理介面 |
| Scripted Pipeline | 以 `node {}` 為起點、彈性較高的 Pipeline 語法 |
| Shared Library | 集中管理、可在多個 Pipeline 共用的 Groovy 程式庫 |
| SLSA | 軟體供應鏈完整性框架（Supply-chain Levels for Software Artifacts） |
| Stash | 在同一次 Pipeline 不同 stage／agent 間暫存傳遞的小型檔案 |
| Update center | 提供 plugin 與版本資訊的服務（`updates.jenkins.io`） |
| WebSocket agent | 透過 HTTP(S) WebSocket 連線的 inbound agent，不需額外 TCP 連接埠 |
| Weekly | 每週發行、包含最新功能的發行線 |
| Workspace | 建置執行時在 agent 上的工作目錄 |

## 附錄 I：實作練習

每個練習都有可驗證的完成標準，適合作為新進人員訓練或內部認證（[附錄 E：認證](#附錄-e認證)）。練習環境可依 [3.5 Docker／Podman 容器部署](#35-dockerpodman-容器部署) 的 Compose 範例在本機建立。

### I.1 基礎（第 1–6 章）

| # | 練習 | 完成標準 |
| --- | --- | --- |
| 1 | 以 WAR 在本機啟動 Jenkins 2.580.1，完成 Setup Wizard | `java -version` 顯示 21；Manage Jenkins → About 顯示 2.580.1 |
| 2 | 以 Compose 啟動 controller＋WebSocket agent | Agent 顯示上線；built-in node executor 為 0；未掛載 `docker.sock` |
| 3 | 以 PIMT 從 `plugins.txt` 建立 controller 映像 | `--view-security-warnings` 無警示；容器啟動後 plugin 清單與 `plugins.txt` 一致 |
| 4 | 在 Script Console 執行 4.5 的唯讀腳本，輸出 plugin 清單 | 輸出可直接作為 `plugins.txt` 使用 |
| 5 | 建立一個 Freestyle 維運 Job，再改寫為 Declarative Pipeline | 兩者行為一致；排程使用 `H` 與 `TZ=Asia/Taipei` |

### I.2 Pipeline 開發（第 7–13 章）

| # | 練習 | 完成標準 |
| --- | --- | --- |
| 6 | 以 `jenkins-docs/simple-java-maven-app` 建立 Multibranch Pipeline | PR 與主分支各自建置；PR 建置顯示在 SCM 的 commit status |
| 7 | 撰寫包含 `options`、`when`、`parallel`、`post` 的 Jenkinsfile | 通過 `declarative-linter`；`when` 使用 `beforeAgent true` |
| 8 | 以 `withCredentials` 使用 Secret text，並故意用雙引號內插一次 | 觀察到「A secret was passed to "sh" using Groovy String interpolation」警告，改為單引號後警告消失 |
| 9 | 加入 `junit`、`recordCoverage`、`recordIssues` 與品質門檻 | 故意加入一個失敗測試時建置變為 UNSTABLE，後續 stage 因 `skipStagesAfterUnstable()` 被略過 |
| 10 | 撰寫 `matrix` 在 JDK 17／21 上測試 | 兩個組合平行執行並各自產生測試報告 |
| 11 | 建立 Shared Library：`vars/mavenBuild.groovy`＋JenkinsPipelineUnit 測試 | Library CI 中測試通過；Jenkinsfile 以 `@Library('...@v1.0.0') _` 呼叫 |
| 12 | 以 Replay 修改一次建置的 Jenkinsfile 驗證修正 | 修正確認後再提交到 Git |

### I.3 平台與部署（第 14–16 章）

| # | 練習 | 完成標準 |
| --- | --- | --- |
| 13 | 在 kind／k3d 叢集以 Helm 安裝 Jenkins，並以 JCasC 設定 Kubernetes cloud | Pipeline 以 `agent { kubernetes { ... } }` 執行，結束後 Pod 自動刪除 |
| 14 | 以 BuildKit rootless 建置並推送映像到本機 registry | 不使用 `docker.sock`、不使用 privileged；取得映像 digest |
| 15 | 以 Helm 部署到 SIT namespace，加入 stage 層級 `input` 與 `timeout` 部署到 UAT | 核准人寫入建置描述；逾時時建置為 ABORTED |
| 16 | 以 GitOps 方式更新部署 repository 的映像 digest | Jenkins 不持有叢集憑證；Argo CD 同步成功 |

### I.4 營運與治理（第 17–21 章）

| # | 練習 | 完成標準 |
| --- | --- | --- |
| 17 | 以 JCasC 設定 OIDC（例如本機 Keycloak）與 Role-based 授權 | 開發者帳號只能操作自己團隊的 folder；破窗帳號可登入 |
| 18 | 啟用 Authorize Project，驗證 `build job:` 受觸發者權限限制 | 無權限的使用者觸發時下游 Job 失敗 |
| 19 | 以 Job DSL seed 建立 folder 與 Organization Folder | 刪除 DSL 中的項目後，seed 執行會依移除策略處理 |
| 20 | 設定 Prometheus 抓取 `/prometheus/` 並建立 19.2 的告警規則 | `promtool check rules` 通過；停止 agent 後觸發告警 |
| 21 | 執行 20.1 的備份腳本並在另一台主機還原 | 憑證可正常使用；記錄實際 RTO |
| 22 | 在預備環境模擬一次 LTS 升級（例如 2.568.3 → 2.580.1） | 依 24.5 檢查清單完成，並寫出升級報告 |
| 23 | 為映像產生 SBOM、執行 Trivy 掃描並以 Cosign 簽章 | `cosign verify` 成功；Warnings NG 顯示掃描結果 |

### I.5 綜合專題

以一個包含前端（Node.js）、後端（Spring Boot）、資料庫遷移（Flyway）的專案，完成以下整條流程，並以 [24.2 Pipeline 品質](#242-pipeline-品質)、[24.3 安全基準](#243-安全基準) 的檢查清單自我評分：

1. Organization Folder 自動納管，PR 建置 10 分鐘內完成
2. 品質門檻：新增程式碼覆蓋率 ≥ 80%、無新增高風險靜態分析問題、無 Critical 弱點
3. 主分支產生映像、SBOM、簽章，並以 digest 部署 SIT
4. Tag 經核准後以 Canary 部署到模擬的正式環境，失敗時自動中止
5. 所有設定（JCasC、Job DSL、Shared Library、`plugins.txt`）都在 Git，能在 1 小時內重建平台
