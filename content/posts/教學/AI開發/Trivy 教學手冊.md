+++
date = '2026-10-03T15:51:29+08:00'
draft = false
title = 'Trivy 教學手冊'
tags = ['教學', 'AI開發', 'DevSecOps', 'Trivy', 'SBOM', 'Kubernetes', 'Supply Chain Security']
categories = ['教學']


# Trivy 企業級 AI Agent 軟體開發安全掃描教學手冊

> **Version**：1.1
> **Updated**：2026-10-03
> **Applicable Trivy Version**：**v0.75.0**（2026-10-01 發布，GitHub Release 標示為 Latest、Immutable Release）
> **相關元件版本**：trivy-action **v0.36.0**（`action.yaml` 預設安裝 Trivy **v0.70.0**，必須以 `version: v0.75.0` 明確指定）、setup-trivy **v0.3.1**（安全下限 ≥ v0.2.6，**避開 v0.3.0**）、Trivy Operator **v0.34.0**（Helm Chart 0.36.0，內建 Trivy 0.74.0）、Trivy Server Helm Chart **0.27.0**（Trivy 0.75.0）、trivy-aws plugin **v0.15.1**、trivy-mcp plugin **v0.0.20**
> **Audience**：PM、SA、Software Architect、Frontend / Backend Developer、DevOps、DevSecOps、Security Engineer、AI Engineer、AI Agent Developer、Platform Team、Reviewer
> **文件狀態**：所有 CLI、參數、Target、Scanner、報告格式皆對照 Trivy 官方文件（trivy.dev/docs/latest）、GitHub Release、CHANGELOG 與 Security Advisory 查證。**官方文件未說明者一律標示「官方資料未說明」，不推測、不補完。**

---

## 關於本手冊

### 這份手冊要解決的問題

市面上大部分 Trivy 文章只回答一個問題：「`trivy image` 怎麼下？」。這個問題花十分鐘就能學會。

本手冊要回答的是企業真正卡關的問題：

> **當 AI Coding Agent 每天替團隊產出數千行程式碼、升級數十個相依套件、修改 Dockerfile 與 Kubernetes YAML 時，如何讓 Trivy 成為「每一次變更都必須通過」的標準 Security Control，而且這道控制本身不會被 AI Agent 為了讓 Pipeline 變綠而關掉？**

這個問題底下有四個層次：

1. **工具層**：Trivy 能掃什麼（Target）、找出什麼（Scanner）、輸出什麼（Report）。
2. **流程層**：什麼時候掃、在哪裡掃、掃完由誰處理（SSDLC、CI/CD、Security Gate）。
3. **AI Agent 層**：AI Agent 如何讀懂掃描結果、哪些可以自動修、哪些必須等人核准。
4. **治理層**：Exception、到期日、Owner、稽核、升級、KPI。

### 本手冊的標示慣例

為避免把「企業建議」誤認為「Trivy 官方規範」，全書使用以下標籤：

| 標籤 | 意義 | 範例 |
|------|------|------|
| **【官方】** | Trivy 官方文件或原始碼明確支援的功能與行為 | `trivy image --format cyclonedx` |
| **【官方·Experimental】** | 官方標示 EXPERIMENTAL，可能在後續版本不相容變更 | `trivy k8s`、`--vex`、crypto scanner |
| **【企業建議】** | 本手冊依企業實務提出的做法，**不是** Trivy 規範 | CRITICAL 且有 Fixed Version 即 Fail |
| **【AI Agent 流程】** | 本手冊為 AI Agent 設計的作業流程 | Scan → Understand → Fix → Verify |
| **【Security Policy】** | 須由企業 Security Team 核定的政策，本手冊僅提供範本 | Exception 最長效期 |

### 2026 年必須知道的三件事

| 事件 | 影響 | 本手冊對應章節 |
|------|------|----------------|
| **2026-03 Trivy 生態系供應鏈遭入侵**（GHSA-69fq-xp46-6x23 / CVE-2026-33634） | 惡意 v0.69.4、trivy-action 76/77 個 tag 被竄改、setup-trivy 全部 tag 被竄改 | 第 14、20、41、45 章 |
| **v0.53 起 `trivy aws` 移出核心** | Cloud 掃描改由 trivy-aws plugin 提供 | 第 12 章 |
| **v0.75 新增 crypto scanner（CBOM）** | 可盤點容器映像中的憑證與金鑰，屬 Experimental | 第 4、6 章 |

### 建議閱讀路線

| 角色 | 必讀章節 | 選讀章節 |
|------|----------|----------|
| PM / SA | 1、2、3、31、57、58、59、61 | 36、37 |
| Architect | 2、3、13、32、35、60 | 24、25、36 |
| Developer | 4–9、14、16、21–23、46 | 44、45、51、52 |
| DevOps / Platform | 14、15、17、18、19、20、40、41、43 | 10、11、44 |
| DevSecOps / Security | 5–12、16、38、39、55、59 | 33、34、36 |
| AI Engineer / AI Agent Developer | 26–30、42、47–49、54、55、附錄 F | 24、25 |

### 變更紀錄

| 版本 | 日期 | 變更摘要 |
|------|------|----------|
| 1.1 | 2026-10-03 | 修正 trivy-action 預設 Trivy 版本（v0.70.0）；setup-trivy 改以 v0.3.1 為範例並註明 v0.3.0 不可用；補 Operator 內建版本、Trivy Server Helm Chart；補 v0.70–v0.75 版本差異；新增 Trivy MCP Server（26.4–26.6、30.4、附錄 F）、VS Code Extension（14.10）、偵測覆蓋範圍（5.9）、VEX OCI 探索；第 34、42、45、54、55、56、60 章拆分子節；第 51–58、60、61 章補實務案例 / 注意事項 |
| 1.0 | 2026-10-03 | 初版（以 Trivy v0.75.0 為基準） |

---

## 目錄

- [關於本手冊](#關於本手冊)
  - [這份手冊要解決的問題](#這份手冊要解決的問題)
  - [本手冊的標示慣例](#本手冊的標示慣例)
  - [2026 年必須知道的三件事](#2026-年必須知道的三件事)
  - [建議閱讀路線](#建議閱讀路線)
  - [變更紀錄](#變更紀錄)
- [1. 文件說明](#1-文件說明)
  - [1.1 文件目的](#11-文件目的)
  - [1.2 適用對象](#12-適用對象)
  - [1.3 適用系統](#13-適用系統)
  - [1.4 適用開發流程](#14-適用開發流程)
  - [1.5 Trivy 在企業 SSDLC 中的角色](#15-trivy-在企業-ssdlc-中的角色)
  - [1.6 Trivy 與 AI Agent 的關係](#16-trivy-與-ai-agent-的關係)
  - [1.7 本文件使用的 Trivy 版本](#17-本文件使用的-trivy-版本)
  - [1.8 v0.53 以後的重要版本差異](#18-v053-以後的重要版本差異)
  - [1.9 文件更新策略](#19-文件更新策略)
  - [實務案例](#實務案例)
  - [注意事項](#注意事項)
- [2. Trivy 是什麼](#2-trivy-是什麼)
  - [2.1 Trivy 定位](#21-trivy-定位)
  - [2.2 發展背景與 Aqua Security](#22-發展背景與-aqua-security)
  - [2.3 Trivy 的五個核心領域](#23-trivy-的五個核心領域)
  - [2.4 Trivy 與各類安全工具的差異](#24-trivy-與各類安全工具的差異)
  - [2.5 Trivy 不是什麼](#25-trivy-不是什麼)
  - [2.6 Trivy 的價值與限制總表](#26-trivy-的價值與限制總表)
  - [實務案例](#實務案例-1)
  - [注意事項](#注意事項-1)
- [3. Trivy 核心概念](#3-trivy-核心概念)
  - [3.1 六大要素](#31-六大要素)
  - [3.2 Trivy Overall Architecture](#32-trivy-overall-architecture)
  - [3.3 Target × Scanner Matrix](#33-target--scanner-matrix)
  - [3.4 Scan Flow](#34-scan-flow)
  - [3.5 CI/CD Flow](#35-cicd-flow)
  - [3.6 AI Agent Integration Flow](#36-ai-agent-integration-flow)
  - [3.7 Trivy 的三種執行模式](#37-trivy-的三種執行模式)
  - [實務案例](#實務案例-2)
  - [注意事項](#注意事項-2)
- [4. Trivy Targets](#4-trivy-targets)
  - [4.1 Container Image](#41-container-image)
  - [4.2 Filesystem](#42-filesystem)
  - [4.3 Git Repository](#43-git-repository)
  - [4.4 Rootfs](#44-rootfs)
  - [4.5 Virtual Machine Image（Experimental）](#45-virtual-machine-imageexperimental)
  - [4.6 Kubernetes](#46-kubernetes)
  - [4.7 SBOM](#47-sbom)
  - [4.8 Dockerfile / IaC / Terraform / Kubernetes YAML](#48-dockerfile--iac--terraform--kubernetes-yaml)
  - [4.9 Cryptographic Asset（v0.75 新增，Experimental）](#49-cryptographic-assetv075-新增experimental)
  - [實務案例](#實務案例-3)
  - [注意事項](#注意事項-3)
- [5. Vulnerability Scanner](#5-vulnerability-scanner)
  - [5.1 基本概念](#51-基本概念)
  - [5.2 Severity](#52-severity)
  - [5.3 CVSS](#53-cvss)
  - [5.4 Vulnerability Status](#54-vulnerability-status)
  - [5.5 EOL 偵測](#55-eol-偵測)
  - [5.6 偵測精準度](#56-偵測精準度)
  - [5.7 VEX](#57-vex)
  - [5.8 企業處理流程：Block / Warn / Monitor / Accept](#58-企業處理流程block--warn--monitor--accept)
  - [5.9 v0.69–v0.75 新增的偵測覆蓋範圍](#59-v069v075-新增的偵測覆蓋範圍)
  - [實務案例](#實務案例-4)
  - [注意事項](#注意事項-4)
- [6. SBOM](#6-sbom)
  - [6.1 SBOM 是什麼](#61-sbom-是什麼)
  - [6.2 為什麼需要 SBOM](#62-為什麼需要-sbom)
  - [6.3 支援格式](#63-支援格式)
  - [6.4 SBOM Generation](#64-sbom-generation)
  - [6.5 SBOM Consumption 與 SBOM Vulnerability Scanning](#65-sbom-consumption-與-sbom-vulnerability-scanning)
  - [6.6 SBOM Attestation](#66-sbom-attestation)
  - [6.7 KBOM 與 CBOM](#67-kbom-與-cbom)
  - [6.8 供應鏈流程](#68-供應鏈流程)
  - [6.9 SBOM 管理建議](#69-sbom-管理建議)
  - [實務案例](#實務案例-5)
  - [注意事項](#注意事項-5)
- [7. Misconfiguration / IaC Security](#7-misconfiguration--iac-security)
  - [7.1 IaC 與 Misconfiguration](#71-iac-與-misconfiguration)
  - [7.2 基本範例](#72-基本範例)
  - [7.3 Dockerfile 範例](#73-dockerfile-範例)
  - [7.4 Kubernetes YAML 範例](#74-kubernetes-yaml-範例)
  - [7.5 Terraform 範例](#75-terraform-範例)
  - [7.6 Inline Ignore 與自訂規則](#76-inline-ignore-與自訂規則)
  - [7.7 不要把所有 Misconfiguration 都當成漏洞](#77-不要把所有-misconfiguration-都當成漏洞)
  - [實務案例](#實務案例-6)
  - [注意事項](#注意事項-6)
- [8. Secret Scanner](#8-secret-scanner)
  - [8.1 偵測對象](#81-偵測對象)
  - [8.2 基本範例](#82-基本範例)
  - [8.3 Secret Configuration（trivy-secret.yaml）](#83-secret-configurationtrivy-secretyaml)
  - [8.4 False Positive](#84-false-positive)
  - [8.5 重要安全原則](#85-重要安全原則)
  - [8.6 Secret 事件處理流程](#86-secret-事件處理流程)
  - [8.7 Git History 與 CI/CD Secret](#87-git-history-與-cicd-secret)
  - [實務案例](#實務案例-7)
  - [注意事項](#注意事項-7)
- [9. License Scanner](#9-license-scanner)
  - [9.1 基本概念](#91-基本概念)
  - [9.2 Trivy 的 License 分類](#92-trivy-的-license-分類)
  - [9.3 範例](#93-範例)
  - [9.4 License 的治理原則](#94-license-的治理原則)
  - [實務案例](#實務案例-8)
  - [注意事項](#注意事項-8)
- [10. Kubernetes Security](#10-kubernetes-security)
  - [10.1 掃描範圍](#101-掃描範圍)
  - [10.2 基本指令](#102-基本指令)
  - [10.3 必要權限](#103-必要權限)
  - [10.4 Compliance](#104-compliance)
  - [10.5 KBOM](#105-kbom)
  - [10.6 架構](#106-架構)
  - [實務案例](#實務案例-9)
  - [注意事項](#注意事項-9)
- [11. Trivy Operator](#11-trivy-operator)
  - [11.1 概念](#111-概念)
  - [11.2 報告類型](#112-報告類型)
  - [11.3 安裝](#113-安裝)
  - [11.4 Trivy CLI vs Trivy Operator](#114-trivy-cli-vs-trivy-operator)
  - [實務案例](#實務案例-10)
  - [注意事項](#注意事項-10)
- [12. Cloud Security](#12-cloud-security)
  - [12.1 先講清楚：Trivy 目前的 Cloud 能力](#121-先講清楚trivy-目前的-cloud-能力)
  - [12.2 trivy-aws plugin](#122-trivy-aws-plugin)
  - [12.3 以 IaC 左移取代事後掃描](#123-以-iac-左移取代事後掃描)
  - [實務案例](#實務案例-11)
  - [注意事項](#注意事項-11)
- [13. Trivy 系統架構](#13-trivy-系統架構)
  - [13.1 完整架構](#131-完整架構)
  - [13.2 元件說明](#132-元件說明)
  - [13.3 Client / Server 模式](#133-client--server-模式)
  - [實務案例](#實務案例-12)
  - [注意事項](#注意事項-12)
- [14. Trivy 安裝](#14-trivy-安裝)
  - [14.1 先讀這一段：2026-03 供應鏈事件](#141-先讀這一段2026-03-供應鏈事件)
  - [14.2 安裝方式總覽](#142-安裝方式總覽)
  - [14.3 Windows](#143-windows)
  - [14.4 Linux](#144-linux)
  - [14.5 macOS](#145-macos)
  - [14.6 Docker / Container](#146-docker--container)
  - [14.7 CI/CD Runner](#147-cicd-runner)
  - [14.8 Kubernetes](#148-kubernetes)
  - [14.9 版本驗證](#149-版本驗證)
  - [14.10 開發者工具：VS Code Extension 與 MCP Plugin](#1410-開發者工具vs-code-extension-與-mcp-plugin)
  - [實務案例](#實務案例-13)
  - [注意事項](#注意事項-13)
- [15. Trivy Configuration](#15-trivy-configuration)
  - [15.1 三種設定來源與優先順序](#151-三種設定來源與優先順序)
  - [15.2 產生預設設定檔](#152-產生預設設定檔)
  - [15.3 常用設定項目](#153-常用設定項目)
  - [15.4 企業建議設定範例](#154-企業建議設定範例)
  - [15.5 CI 中避免被 Repo 內設定檔左右](#155-ci-中避免被-repo-內設定檔左右)
  - [實務案例](#實務案例-14)
  - [注意事項](#注意事項-14)
- [16. .trivyignore](#16-trivyignore)
  - [16.1 Why：為什麼需要 Ignore](#161-why為什麼需要-ignore)
  - [16.2 兩種格式](#162-兩種格式)
  - [16.3 治理要求](#163-治理要求)
  - [16.4 CI 自動檢查 Ignore 檔](#164-ci-自動檢查-ignore-檔)
  - [實務案例](#實務案例-15)
  - [注意事項](#注意事項-15)
- [17. Trivy Database / Cache](#17-trivy-database--cache)
  - [17.1 三種資料來源](#171-三種資料來源)
  - [17.2 常用指令](#172-常用指令)
  - [17.3 Cache](#173-cache)
  - [17.4 企業環境的五個問題](#174-企業環境的五個問題)
  - [17.5 Proxy 與企業 CA](#175-proxy-與企業-ca)
  - [實務案例](#實務案例-16)
  - [注意事項](#注意事項-16)
- [18. Report Format](#18-report-format)
  - [18.1 支援格式](#181-支援格式)
  - [18.2 依用途分類](#182-依用途分類)
  - [18.3 一次掃描、多種輸出：trivy convert](#183-一次掃描多種輸出trivy-convert)
  - [18.4 Template](#184-template)
  - [18.5 SARIF 與 GitHub Code Scanning](#185-sarif-與-github-code-scanning)
  - [18.6 給 AI Agent 的 JSON 摘要](#186-給-ai-agent-的-json-摘要)
  - [實務案例](#實務案例-17)
  - [注意事項](#注意事項-17)
- [19. CI/CD 整合](#19-cicd-整合)
  - [19.1 標準 Pipeline](#191-標準-pipeline)
  - [19.2 官方整合清單](#192-官方整合清單)
  - [19.3 GitLab CI](#193-gitlab-ci)
  - [19.4 Jenkins](#194-jenkins)
  - [19.5 Azure DevOps](#195-azure-devops)
  - [實務案例](#實務案例-18)
  - [注意事項](#注意事項-18)
- [20. GitHub Actions](#20-github-actions)
  - [20.1 2026-03 事件後的 GitHub Actions 安全原則](#201-2026-03-事件後的-github-actions-安全原則)
  - [20.2 完整 Workflow](#202-完整-workflow)
  - [20.3 逐步說明](#203-逐步說明)
  - [20.4 使用 trivy-action 的寫法](#204-使用-trivy-action-的寫法)
  - [20.5 DB 快取預熱 Workflow](#205-db-快取預熱-workflow)
  - [20.6 Dependency Graph 提交](#206-dependency-graph-提交)
  - [實務案例](#實務案例-19)
  - [注意事項](#注意事項-19)
- [21. Web Application Security](#21-web-application-security)
  - [21.1 企業 Web Application 的掃描分層](#211-企業-web-application-的掃描分層)
  - [21.2 前端相依的特殊考量](#212-前端相依的特殊考量)
  - [21.3 後端相依的特殊考量](#213-後端相依的特殊考量)
  - [實務案例](#實務案例-20)
  - [注意事項](#注意事項-20)
- [22. Java / Spring Boot 專案](#22-java--spring-boot-專案)
  - [22.1 案例環境](#221-案例環境)
  - [22.2 Step 1：掃描 Maven Dependency](#222-step-1掃描-maven-dependency)
  - [22.3 Step 2：掃描 Source Repository](#223-step-2掃描-source-repository)
  - [22.4 Step 3：產生 SBOM](#224-step-3產生-sbom)
  - [22.5 Step 4：建立 Container Image](#225-step-4建立-container-image)
  - [22.6 Step 5：掃描 Image](#226-step-5掃描-image)
  - [22.7 Step 6：掃描 Dockerfile](#227-step-6掃描-dockerfile)
  - [22.8 Step 7：掃描 Kubernetes YAML](#228-step-7掃描-kubernetes-yaml)
  - [22.9 Step 8：CI/CD Security Gate](#229-step-8cicd-security-gate)
  - [22.10 常見問題](#2210-常見問題)
  - [實務案例](#實務案例-21)
  - [注意事項](#注意事項-21)
- [23. Vue / Angular 專案](#23-vue--angular-專案)
  - [23.1 案例環境](#231-案例環境)
  - [23.2 Package Dependency 與 Lock File](#232-package-dependency-與-lock-file)
  - [23.3 Secret 與 Configuration](#233-secret-與-configuration)
  - [23.4 Docker Image](#234-docker-image)
  - [23.5 SBOM](#235-sbom)
  - [23.6 CI/CD](#236-cicd)
  - [實務案例](#實務案例-22)
  - [注意事項](#注意事項-22)
- [24. Legacy System Reverse Engineering](#24-legacy-system-reverse-engineering)
  - [24.1 背景](#241-背景)
  - [24.2 Security Baseline 流程](#242-security-baseline-流程)
  - [24.3 執行步驟](#243-執行步驟)
  - [24.4 Legacy 系統的特殊情況](#244-legacy-系統的特殊情況)
  - [24.5 Security Baseline 產出物](#245-security-baseline-產出物)
  - [實務案例](#實務案例-23)
  - [注意事項](#注意事項-23)
- [25. Software Framework Upgrade](#25-software-framework-upgrade)
  - [25.1 升級安全流程](#251-升級安全流程)
  - [25.2 適用的升級類型](#252-適用的升級類型)
  - [25.3 Before / After 掃描](#253-before--after-掃描)
  - [25.4 比較腳本](#254-比較腳本)
  - [25.5 SBOM 差異](#255-sbom-差異)
  - [25.6 Security Upgrade Report 範本](#256-security-upgrade-report-範本)
  - [實務案例](#實務案例-24)
  - [注意事項](#注意事項-24)
- [26. AI Agent + Trivy](#26-ai-agent--trivy)
  - [26.1 從「AI 寫 Code」到「AI Security Feedback Loop」](#261-從ai-寫-code到ai-security-feedback-loop)
  - [26.2 AI Agent 什麼時候必須執行 Trivy](#262-ai-agent-什麼時候必須執行-trivy)
  - [26.3 AI Agent 呼叫 Trivy 的設計原則](#263-ai-agent-呼叫-trivy-的設計原則)
  - [26.4 Trivy MCP Server：讓 AI Agent 以標準工具呼叫 Trivy](#264-trivy-mcp-server讓-ai-agent-以標準工具呼叫-trivy)
  - [26.5 安裝與 IDE 設定](#265-安裝與-ide-設定)
  - [26.6 MCP 與 CLI 的分工](#266-mcp-與-cli-的分工)
  - [實務案例](#實務案例-25)
  - [注意事項](#注意事項-25)
- [27. AI Agent 使用 Trivy 的標準流程](#27-ai-agent-使用-trivy-的標準流程)
  - [27.1 十步驟](#271-十步驟)
  - [27.2 核心原則](#272-核心原則)
  - [實務案例](#實務案例-26)
  - [注意事項](#注意事項-26)
- [28. AI Agent Prompt Engineering](#28-ai-agent-prompt-engineering)
  - [28.1 Repository Security Scan Prompt](#281-repository-security-scan-prompt)
  - [28.2 Container Security Scan Prompt](#282-container-security-scan-prompt)
  - [28.3 Kubernetes Security Scan Prompt](#283-kubernetes-security-scan-prompt)
  - [28.4 Dependency Upgrade Prompt](#284-dependency-upgrade-prompt)
  - [28.5 Framework Upgrade Security Prompt](#285-framework-upgrade-security-prompt)
  - [28.6 Reverse Engineering Security Prompt](#286-reverse-engineering-security-prompt)
  - [28.7 SBOM Analysis Prompt](#287-sbom-analysis-prompt)
  - [28.8 Secret Finding Response Prompt](#288-secret-finding-response-prompt)
  - [28.9 CI/CD Failure Analysis Prompt](#289-cicd-failure-analysis-prompt)
  - [28.10 Security Regression Verification Prompt](#2810-security-regression-verification-prompt)
  - [實務案例](#實務案例-27)
  - [注意事項](#注意事項-27)
- [29. AI Agent 不可以做的事情](#29-ai-agent-不可以做的事情)
  - [29.1 禁止清單](#291-禁止清單)
  - [29.2 三區分類](#292-三區分類)
  - [實務案例](#實務案例-28)
  - [注意事項](#注意事項-28)
- [30. AI Agent Security Guardrail](#30-ai-agent-security-guardrail)
  - [30.1 Guardrail 總表](#301-guardrail-總表)
  - [30.2 CODEOWNERS 範例](#302-codeowners-範例)
  - [30.3 Guardrail 架構](#303-guardrail-架構)
  - [30.4 MCP Server Guardrail](#304-mcp-server-guardrail)
  - [實務案例](#實務案例-29)
  - [注意事項](#注意事項-29)
- [31. Trivy + SSDLC](#31-trivy--ssdlc)
  - [31.1 SSDLC 階段對應](#311-ssdlc-階段對應)
  - [實務案例](#實務案例-30)
  - [注意事項](#注意事項-30)
- [32. Trivy + Clean Architecture](#32-trivy--clean-architecture)
  - [32.1 Trivy 能檢查什麼](#321-trivy-能檢查什麼)
  - [32.2 四種品質的組合](#322-四種品質的組合)
  - [實務案例](#實務案例-31)
  - [注意事項](#注意事項-31)
- [33. Trivy + OWASP](#33-trivy--owasp)
  - [33.1 OWASP Top 10 能力對照](#331-owasp-top-10-能力對照)
  - [33.2 必須明確區分的六類問題](#332-必須明確區分的六類問題)
  - [實務案例](#實務案例-32)
  - [注意事項](#注意事項-32)
- [34. Trivy + SAST / DAST / SCA](#34-trivy--sast--dast--sca)
  - [34.1 工具定位比較](#341-工具定位比較)
  - [34.2 工具組合架構](#342-工具組合架構)
  - [34.3 結果彙整與去重](#343-結果彙整與去重)
  - [34.4 選型建議](#344-選型建議)
  - [實務案例](#實務案例-33)
  - [注意事項](#注意事項-33)
- [35. Enterprise DevSecOps Reference Architecture](#35-enterprise-devsecops-reference-architecture)
  - [35.1 架構圖](#351-架構圖)
  - [35.2 元件職責](#352-元件職責)
  - [實務案例](#實務案例-34)
  - [注意事項](#注意事項-34)
- [36. Banking / Enterprise Environment](#36-banking--enterprise-environment)
  - [36.1 金融業環境特性與對策](#361-金融業環境特性與對策)
  - [36.2 金融業導入流程](#362-金融業導入流程)
  - [實務案例](#實務案例-35)
  - [注意事項](#注意事項-35)
- [37. GitHub / GitLab Enterprise Governance](#37-github--gitlab-enterprise-governance)
  - [37.1 治理層級](#371-治理層級)
  - [37.2 關鍵機制](#372-關鍵機制)
  - [37.3 Reusable Workflow 範例](#373-reusable-workflow-範例)
  - [實務案例](#實務案例-36)
  - [注意事項](#注意事項-36)
- [38. Security Gate](#38-security-gate)
  - [38.1 Trivy Capability vs Company Policy](#381-trivy-capability-vs-company-policy)
  - [38.2 企業 Gate 範例](#382-企業-gate-範例)
  - [38.3 Gate 判斷流程](#383-gate-判斷流程)
  - [實務案例](#實務案例-37)
  - [注意事項](#注意事項-37)
- [39. False Positive / Exception Management](#39-false-positive--exception-management)
  - [39.1 名詞區分](#391-名詞區分)
  - [39.2 Exception Record 範例](#392-exception-record-範例)
  - [39.3 Exception 生命週期](#393-exception-生命週期)
  - [39.4 VEX 範例（OpenVEX）](#394-vex-範例openvex)
  - [實務案例](#實務案例-38)
  - [注意事項](#注意事項-38)
- [40. Trivy 維運](#40-trivy-維運)
  - [40.1 維運範圍](#401-維運範圍)
  - [40.2 維運 Checklist](#402-維運-checklist)
  - [實務案例](#實務案例-39)
  - [注意事項](#注意事項-39)
- [41. Trivy 升級策略](#41-trivy-升級策略)
  - [41.1 升級流程](#411-升級流程)
  - [41.2 升級類型](#412-升級類型)
  - [41.3 升級前檢查清單](#413-升級前檢查清單)
  - [41.4 新舊版結果比較](#414-新舊版結果比較)
  - [實務案例](#實務案例-40)
  - [注意事項](#注意事項-40)
- [42. Trivy 升級對 AI Agent 的要求](#42-trivy-升級對-ai-agent-的要求)
  - [42.1 十一個必要步驟](#421-十一個必要步驟)
  - [42.2 Upgrade Report 範本](#422-upgrade-report-範本)
  - [42.3 升級工作的範圍與禁止事項](#423-升級工作的範圍與禁止事項)
  - [實務案例](#實務案例-41)
  - [注意事項](#注意事項-41)
- [43. Performance Optimization](#43-performance-optimization)
  - [43.1 優化手段](#431-優化手段)
  - [43.2 大型企業降低 CI 影響的做法](#432-大型企業降低-ci-影響的做法)
  - [實務案例](#實務案例-42)
  - [注意事項](#注意事項-42)
- [44. Troubleshooting](#44-troubleshooting)
  - [44.1 DB Download Failure](#441-db-download-failure)
  - [44.2 Network Failure](#442-network-failure)
  - [44.3 Proxy](#443-proxy)
  - [44.4 Certificate](#444-certificate)
  - [44.5 Registry Authentication](#445-registry-authentication)
  - [44.6 Docker Socket](#446-docker-socket)
  - [44.7 Permission](#447-permission)
  - [44.8 Kubernetes Authentication](#448-kubernetes-authentication)
  - [44.9 Slow Scan](#449-slow-scan)
  - [44.10 Out of Disk](#4410-out-of-disk)
  - [44.11 Large Image](#4411-large-image)
  - [44.12 False Positive](#4412-false-positive)
  - [44.13 Missing Vulnerability](#4413-missing-vulnerability)
  - [44.14 Unexpected Severity](#4414-unexpected-severity)
  - [44.15 SBOM 問題](#4415-sbom-問題)
  - [44.16 Java Dependency 問題](#4416-java-dependency-問題)
  - [實務案例](#實務案例-43)
  - [注意事項](#注意事項-43)
- [45. 常見錯誤](#45-常見錯誤)
  - [45.1 掃描範圍錯誤](#451-掃描範圍錯誤)
  - [45.2 資料與效能錯誤](#452-資料與效能錯誤)
  - [45.3 治理錯誤](#453-治理錯誤)
  - [45.4 供應鏈與版本錯誤](#454-供應鏈與版本錯誤)
  - [實務案例](#實務案例-44)
  - [注意事項](#注意事項-44)
- [46. 實戰 Lab](#46-實戰-lab)
  - [46.1 Lab 1：Container Image Scan](#461-lab-1container-image-scan)
  - [46.2 Lab 2：Source Repository Scan](#462-lab-2source-repository-scan)
  - [46.3 Lab 3：Secret Scan](#463-lab-3secret-scan)
  - [46.4 Lab 4：IaC Scan](#464-lab-4iac-scan)
  - [46.5 Lab 5：Kubernetes Scan（Experimental）](#465-lab-5kubernetes-scanexperimental)
  - [46.6 Lab 6：SBOM Generation](#466-lab-6sbom-generation)
  - [46.7 Lab 7：SBOM Scan](#467-lab-7sbom-scan)
  - [46.8 Lab 8：License Scan](#468-lab-8license-scan)
  - [46.9 Lab 9：GitHub Actions](#469-lab-9github-actions)
  - [46.10 Lab 10：Docker + Kubernetes](#4610-lab-10docker--kubernetes)
  - [46.11 Lab 11：Spring Boot](#4611-lab-11spring-boot)
  - [46.12 Lab 12：Vue](#4612-lab-12vue)
  - [46.13 Lab 13：Angular](#4613-lab-13angular)
  - [46.14 Lab 14：Legacy Reverse Engineering](#4614-lab-14legacy-reverse-engineering)
  - [46.15 Lab 15：Framework Upgrade](#4615-lab-15framework-upgrade)
  - [46.16 Lab 16：AI Agent Security Feedback Loop](#4616-lab-16ai-agent-security-feedback-loop)
  - [實務案例](#實務案例-45)
  - [注意事項](#注意事項-45)
- [47. 完整 AI Agent 實戰案例](#47-完整-ai-agent-實戰案例)
  - [47.1 系統架構](#471-系統架構)
  - [47.2 任務](#472-任務)
  - [47.3 執行流程](#473-執行流程)
  - [47.4 各步驟細節](#474-各步驟細節)
  - [47.5 AI Agent 產出的 Security Report](#475-ai-agent-產出的-security-report)
  - [實務案例](#實務案例-46)
  - [注意事項](#注意事項-46)
- [48. Reverse Engineering 實戰](#48-reverse-engineering-實戰)
  - [48.1 情境](#481-情境)
  - [48.2 AI Agent 執行順序](#482-ai-agent-執行順序)
  - [48.3 指令](#483-指令)
  - [48.4 最終輸出](#484-最終輸出)
  - [實務案例](#實務案例-47)
  - [注意事項](#注意事項-47)
- [49. Framework Upgrade 實戰](#49-framework-upgrade-實戰)
  - [49.1 情境](#491-情境)
  - [49.2 比較項目](#492-比較項目)
  - [49.3 Security Upgrade Report](#493-security-upgrade-report)
  - [實務案例](#實務案例-48)
  - [注意事項](#注意事項-48)
- [50. Trivy 教學案例程式碼規範](#50-trivy-教學案例程式碼規範)
  - [實務案例](#實務案例-49)
  - [注意事項](#注意事項-49)
- [51. 命令速查表](#51-命令速查表)
  - [51.1 主要命令總覽](#511-主要命令總覽)
  - [51.2 各命令：常用參數、CI/CD 用法、AI Agent 用法](#512-各命令常用參數cicd-用法ai-agent-用法)
  - [實務案例](#實務案例-50)
  - [注意事項](#注意事項-50)
- [52. Trivy Cheat Sheet](#52-trivy-cheat-sheet)
  - [實務案例](#實務案例-51)
  - [注意事項](#注意事項-51)
- [53. Enterprise Checklist](#53-enterprise-checklist)
  - [53.1 Developer Checklist](#531-developer-checklist)
  - [53.2 AI Agent Checklist](#532-ai-agent-checklist)
  - [53.3 Reviewer Checklist](#533-reviewer-checklist)
  - [53.4 DevSecOps Checklist](#534-devsecops-checklist)
  - [53.5 Platform Team Checklist](#535-platform-team-checklist)
  - [53.6 Security Team Checklist](#536-security-team-checklist)
  - [53.7 Release Checklist](#537-release-checklist)
  - [53.8 Framework Upgrade Checklist](#538-framework-upgrade-checklist)
  - [53.9 Reverse Engineering Checklist](#539-reverse-engineering-checklist)
  - [實務案例](#實務案例-52)
  - [注意事項](#注意事項-52)
- [54. AI Agent Standard Operating Procedure](#54-ai-agent-standard-operating-procedure)
  - [54.1 SOP 步驟](#541-sop-步驟)
  - [54.2 SOP 流程圖](#542-sop-流程圖)
  - [54.3 停止條件與回報對象](#543-停止條件與回報對象)
  - [實務案例](#實務案例-53)
  - [注意事項](#注意事項-53)
- [55. AI Agent Security Policy](#55-ai-agent-security-policy)
  - [55.1 Policy 範本](#551-policy-範本)
  - [55.2 Policy 落地：文字規則對應技術控制](#552-policy-落地文字規則對應技術控制)
  - [實務案例](#實務案例-54)
  - [注意事項](#注意事項-54)
- [56. Trivy 與企業 AI Coding Standard](#56-trivy-與企業-ai-coding-standard)
  - [56.1 規範領域對照](#561-規範領域對照)
  - [56.2 整合架構](#562-整合架構)
  - [56.3 導入檢核](#563-導入檢核)
  - [實務案例](#實務案例-55)
  - [注意事項](#注意事項-55)
- [57. 建議企業導入 Roadmap](#57-建議企業導入-roadmap)
  - [57.1 Phase 1：Developer Local Scan](#571-phase-1developer-local-scan)
  - [57.2 Phase 2：Repository CI Scan](#572-phase-2repository-ci-scan)
  - [57.3 Phase 3：Container Scan](#573-phase-3container-scan)
  - [57.4 Phase 4：SBOM](#574-phase-4sbom)
  - [57.5 Phase 5：IaC / Kubernetes](#575-phase-5iac--kubernetes)
  - [57.6 Phase 6：Cloud](#576-phase-6cloud)
  - [57.7 Phase 7：AI Agent Integration](#577-phase-7ai-agent-integration)
  - [57.8 Phase 8：Enterprise Security Governance](#578-phase-8enterprise-security-governance)
  - [實務案例](#實務案例-56)
  - [注意事項](#注意事項-56)
- [58. KPI / Metrics](#58-kpi--metrics)
  - [實務案例](#實務案例-57)
  - [注意事項](#注意事項-57)
- [59. Governance Model](#59-governance-model)
  - [59.1 治理層級](#591-治理層級)
  - [59.2 責任分工](#592-責任分工)
  - [59.3 RACI（R＝執行、A＝負責、C＝諮詢、I＝告知）](#593-racir執行a負責c諮詢i告知)
  - [實務案例](#實務案例-58)
  - [注意事項](#注意事項-58)
- [60. Final Reference Architecture](#60-final-reference-architecture)
  - [60.1 架構圖](#601-架構圖)
  - [60.2 元件與責任邊界](#602-元件與責任邊界)
  - [60.3 資料流說明](#603-資料流說明)
  - [實務案例](#實務案例-59)
  - [注意事項](#注意事項-59)
- [61. 最後的企業建議](#61-最後的企業建議)
  - [61.1 如果公司準備正式導入 Trivy，應該如何開始？](#611-如果公司準備正式導入-trivy應該如何開始)
  - [61.2 第一個 30 天](#612-第一個-30-天)
  - [61.3 核心問題回答索引](#613-核心問題回答索引)
  - [61.4 結語](#614-結語)
  - [實務案例](#實務案例-60)
  - [注意事項](#注意事項-60)
- [Appendix A - CLI Cheat Sheet](#appendix-a---cli-cheat-sheet)
  - [A.1 全域參數（所有子命令通用）](#a1-全域參數所有子命令通用)
  - [A.2 常用掃描參數](#a2-常用掃描參數)
  - [A.3 常用環境變數](#a3-常用環境變數)
- [Appendix B - AI Agent Prompt](#appendix-b---ai-agent-prompt)
  - [B.1 通用前置 Prompt（放在所有 Trivy 任務最前面）](#b1-通用前置-prompt放在所有-trivy-任務最前面)
- [Appendix C - Security Checklist](#appendix-c---security-checklist)
  - [C.1 新進成員快速 Checklist](#c1-新進成員快速-checklist)
  - [C.2 PR 安全 Checklist](#c2-pr-安全-checklist)
  - [C.3 Release 安全 Checklist](#c3-release-安全-checklist)
- [Appendix D - Troubleshooting](#appendix-d---troubleshooting)
- [Appendix E - Reference Architecture](#appendix-e---reference-architecture)
- [Appendix F - AI Agent 執行規範（AGENTS.md / CLAUDE.md / copilot-instructions.md）](#appendix-f---ai-agent-執行規範agentsmd--claudemd--copilot-instructionsmd)
- [Appendix G - 版本指令差異對照表](#appendix-g---版本指令差異對照表)
- [References](#references)
- [Technical Review Checklist](#technical-review-checklist)
  - [已知限制與使用前需再確認的項目](#已知限制與使用前需再確認的項目)

---

## 1. 文件說明

### 1.1 文件目的

本手冊的目的是建立一套 **「Trivy + AI Agent + SSDLC + CI/CD + Container + Kubernetes + Cloud + SBOM」** 的企業級安全開發方法，讓：

- 開發人員知道**何時、如何**在本機執行 Trivy。
- AI Coding Agent 知道**何時必須**執行 Trivy、如何解讀結果、哪些修正可以自動執行、哪些必須停下來等待人工核准。
- DevSecOps 知道如何把 Trivy 放進 CI/CD、Registry、Kubernetes 與 Cloud。
- Security Team 知道如何管理 Exception、VEX、到期日與稽核證據。
- Platform Team 知道如何安全地安裝、升級、快取與離線運作 Trivy。

### 1.2 適用對象

| 角色 | 在本手冊中的責任 |
|------|------------------|
| PM | 把安全掃描納入時程與驗收條件；追蹤 KPI |
| SA | 在需求階段定義安全需求（SBOM、License、Secret 政策） |
| Architect | 決定掃描點、Security Gate 位置、Reference Architecture |
| Developer | 本機掃描、修正 Finding、提出 Exception |
| DevOps | CI/CD 整合、DB 快取、Registry 認證 |
| DevSecOps | 掃描政策、Gate 門檻、Exception 審核流程 |
| Security Engineer | Finding 風險評估、VEX、Secret 事件應變 |
| AI Engineer | 設計 AI Agent 的 Trivy 工具呼叫與 Guardrail |
| AI Agent Developer | 撰寫 Prompt、AGENTS.md 規則、驗證 AI 行為 |

### 1.3 適用系統

- 企業大型 Web Application（Vue / Angular 前端 + Java / Spring Boot 後端）。
- 容器化系統（Docker / OCI Image、Kubernetes、OpenShift）。
- 以 Terraform / CloudFormation / Azure ARM / Helm / Ansible 管理的基礎設施。
- 正在進行 **Reverse Engineering** 的 Legacy System。
- 正在進行 **Framework Upgrade**（Java、Spring Boot、Node.js、Vue、Angular、Base Image、Kubernetes）的系統。

### 1.4 適用開發流程

```mermaid
flowchart LR
    A["需求"] --> B["設計"]
    B --> C["開發 / AI Agent 實作"]
    C --> D["建置"]
    D --> E["測試"]
    E --> F["部署"]
    F --> G["維運"]
    G --> H["維護 / 升級"]
    C -.->|"trivy fs / repo"| T["Trivy"]
    D -.->|"trivy image / SBOM"| T
    F -.->|"trivy config / k8s"| T
    G -.->|"Trivy Operator"| T
    H -.->|"Before / After 比對"| T
```

### 1.5 Trivy 在企業 SSDLC 中的角色

Trivy 在 SSDLC（Secure Software Development Life Cycle，安全軟體開發生命週期）中扮演的是 **「自動化偵測（Detection）控制點」**：

| 定位 | 說明 |
|------|------|
| 是什麼 | 多 Target、多 Scanner 的安全掃描器，產出可機器處理的 Finding 與 SBOM |
| 不是什麼 | 不是完整 SAST、不是 DAST、不是 WAF、不是 Runtime Protection、不是完整 CSPM |
| 產出 | Vulnerability、Misconfiguration、Secret、License、SBOM、Compliance Report |
| 消費者 | Developer、AI Agent、CI/CD Gate、GitHub Code Scanning、SIEM、稽核 |

### 1.6 Trivy 與 AI Agent 的關係

AI Agent 寫程式的速度遠超過人類 Review 的速度。Trivy 對 AI Agent 的價值有三個：

1. **客觀的回饋訊號**：AI Agent 修改了 `pom.xml`，Trivy 可以立刻告訴它新增了哪些 CVE。
2. **可驗證的完成條件**：「修好了」不是 AI 說了算，而是 Re-scan 的結果說了算。
3. **自動化的 Guardrail**：CI/CD 中的 Trivy Gate 是 AI Agent 無法「說服」的關卡。

但也必須防範三種風險：

1. AI Agent 為了讓 Pipeline Pass 而加入 `.trivyignore`、把 `exit-code` 改成 0、或移除 Scan Step。
2. AI Agent 把 Secret Finding 的原文貼進對話、Log 或 Ticket。
3. AI Agent 對 License 自行下法律結論。

這三種風險在第 29、30、55 章與附錄 F 有完整規範。

### 1.7 本文件使用的 Trivy 版本

| 項目 | 版本 | 發布日 | 狀態 |
|------|------|--------|------|
| Trivy | v0.75.0 | 2026-10-01 | Latest、Immutable Release |
| Trivy（前一版） | v0.74.0 | 2026-08-14 | 可作為保守釘選版本 |
| trivy-action | v0.36.0 | 2026-04-22 | Latest；`action.yaml` 的 `version` 預設為 **v0.70.0**，內部以 SHA 固定 setup-trivy v0.2.6 |
| setup-trivy | v0.3.1 | 2026-06-03 | Latest；v0.3.0（2026-06-02）無法載入，**不可使用**；安全下限 ≥ v0.2.6 |
| Trivy Operator | v0.34.0 | 2026-08-24 | Latest，內建 Trivy 0.74.0；Helm Chart 0.36.0；專案仍標示 incubating |
| Trivy Server Helm Chart | 0.27.0 | 2026-10-01 | 內建 Trivy 0.75.0（`helm/trivy`） |
| trivy-aws plugin | v0.15.1 | 約 2 年前 | 維護頻率低，請見第 12 章 |
| trivy-mcp plugin | v0.0.20 | 約 10 個月前 | 0.0.x 早期版本，請見第 26.4 節 |

> **【企業建議】** 文件以 v0.75.0 為基準撰寫，但企業正式環境應「釘選版本、在測試環境驗證後再升級」。v0.75.0 發布僅數日，建議先在非正式 Pipeline 試行一個週期。
>
> **注意版本落差**：同一組織內 CLI（v0.75.0）、trivy-action 預設值（v0.70.0）、Operator 內建版本（0.74.0）可能各不相同。使用 trivy-action 時**一律明確指定 `version`**，並在升級時同步檢查 Operator 與 Server 的 Trivy 版本（第 41 章）。

### 1.8 v0.53 以後的重要版本差異

| 版本 | 變更 | 類型 | 對使用者的影響 |
|------|------|------|----------------|
| v0.75.0 | 報告 template 移除 `getHostByName` | **Breaking** | 自訂 template 使用此函式會解析失敗 |
| v0.75.0 | 新增 `crypto` scanner（CBOM） | Experimental | 僅支援 image + CycloneDX |
| v0.75.0 | `--config=""`、`--ignorefile=""` 可停用設定檔載入 | 新功能 | CI 可避免被 repo 內設定檔左右 |
| v0.75.0 | uv workspace、Echo 修補版 Python 套件偵測 | 新功能 | Python 專案 Finding 可能增加 |
| v0.74.0 | RapidFort curated image 偵測；JAR `Bundle-License` / pom `<url>` 轉 SPDX ID | 新功能 | 授權辨識更完整 |
| v0.73.0 | trivy.yaml 支援自訂 Maven mirrors | 新功能 | 企業內部 Nexus / Artifactory |
| v0.73.0 | VEX 以 OCI artifact 原生探索（含 in-toto referrers） | 新功能 | VEX 可與映像一起發布 |
| v0.72.0 | Bottlerocket OS、.NET self-contained runtime、OpenAI 與 GitHub App token 規則 | 新功能 | 覆蓋範圍擴大 |
| v0.72.0 | 發行流程改用 GoReleaser `dockers_v2` | **Breaking（CI）** | 官方發行流程變更，使用者 CLI 不受影響 |
| v0.71.0 | CycloneDX 1.7、讀取 `settings.xml` 的 `<mirrors>` | 新功能 | Java 企業環境 |
| v0.71.0 | Azure 與 Maven settings Secret 規則；可自訂 Secret 略過的目錄 / 檔案 / 副檔名；Ubuntu 26.04 | 新功能 | Secret 與 OS 覆蓋 |
| v0.70.0 | `pylock.toml`（PEP 751）、Client/Server JSON 含 Server 版本、template 必須 `.tpl` | 新功能 / 行為變更 | Python、報告追蹤 |
| v0.69.0 | misconf providers mapping 改用 ID（非 AVDID） | **Breaking** | 自訂 check / mapping 需檢查 |
| v0.69.0 | Ansible 掃描初始支援、trivy.yaml JSON Schema | 新功能 | IaC 覆蓋擴大 |
| v0.68.0 | `--cacert`、ReportID、ArtifactID、Fingerprint | 新功能 | 企業 CA、報告追蹤 |
| v0.67.0 | `--list-all-pkgs` 預設改為 true | 行為變更 | JSON 報告變大 |
| v0.57.0 | `trivy auth` 更名為 `trivy registry` | 更名 | 舊腳本需修改 |
| v0.57.0 | 指定的 ignore file 不存在時報錯 | 行為變更 | CI 路徑錯誤會直接失敗 |
| v0.55.0 | 刪除已棄用的 SBOM flags | **Breaking** | 舊 SBOM 指令需改寫 |
| v0.54.0 | `--vuln-type` 更名為 `--pkg-types` | 更名 | trivy-action 仍保留 `vuln-type` input |
| v0.53.0 | 移除 `trivy aws` 子命令 | **Breaking** | 改用 trivy-aws plugin |
| v0.53.0 | 新增 `trivy clean` 子命令 | 新功能 | 取代舊的清除快取 flag |

完整的「舊指令 / 新指令」對照表見 **附錄 G**。

### 1.9 文件更新策略

| 觸發條件 | 更新動作 | 負責角色 |
|----------|----------|----------|
| Trivy Minor 版本發布 | 檢查 CHANGELOG 的 BREAKING CHANGES，更新 1.8 與附錄 G | DevSecOps |
| Trivy Security Advisory 發布 | 24 小時內評估、更新第 41、45 章 | Security Team |
| trivy-action / setup-trivy 新版 | 更新第 20 章 SHA pin 範例、核對 `action.yaml` 的 `version` 預設值 | Platform Team |
| Operator / Server Helm Chart / MCP plugin 新版 | 更新 1.7 版本表與第 11、13、26 章 | Platform Team |
| 企業 Security Policy 變更 | 更新第 38、39、55 章 | Security Team |
| 每季 | 全文 Technical Review | Architecture Governance |

### 實務案例

某金融業 Java 團隊在 2026 年 Q2 導入 Trivy，初期沿用網路文章中的 `--vuln-type os,library` 與 `trivy aws` 指令，結果在 v0.6x 的 Runner 上一個 flag 被警告、一個子命令根本不存在。導入 1.8 節的版本差異表後，團隊建立「所有 Trivy 指令只能從內部手冊複製」的規則，CI 失敗率明顯下降。

### 注意事項

- 本手冊的指令以 **Trivy v0.75.0** 為準，舊版本執行可能出現不支援的 flag。
- 任何標示 **Experimental** 的功能，不建議直接作為 Production Security Gate 的唯一依據。
- 手冊中的 Gate 門檻、Exception 效期皆為 **【企業建議】**，必須經企業 Security Team 核定後才生效。

---

## 2. Trivy 是什麼

### 2.1 Trivy 定位

Trivy 官方的自我描述是 **「Unified security scanner」**（統一的安全掃描器）。它把過去需要多種工具才能完成的掃描，整合在同一個 CLI 與同一套報告格式中：

| 過去需要的工具類型 | Trivy 對應能力 |
|--------------------|----------------|
| Container Image Scanner | `trivy image` |
| SCA（Software Composition Analysis，軟體組成分析） | `trivy fs` / `trivy repo` 的 vuln scanner |
| Secret Scanner | `--scanners secret` |
| IaC Scanner | `trivy config` / `--scanners misconfig` |
| License Scanner | `--scanners license` |
| SBOM Generator | `--format cyclonedx / spdx / spdx-json` |
| SBOM Scanner | `trivy sbom` |
| Kubernetes Scanner | `trivy k8s`（Experimental） |

### 2.2 發展背景與 Aqua Security

- Trivy 由 **Aqua Security** 維護，以 Apache-2.0 授權開源，原始碼位於 `github.com/aquasecurity/trivy`。
- 官方文件位於 `trivy.dev`，每個 Minor 版本都有獨立文件版本（v0.50 至 v0.75）。
- Aqua Security 另有商業產品，官方文件的「Commercial / Comparison」頁面說明開源版與商業版差異。**本手冊只涵蓋開源版。**
- 相關開源專案：trivy-db、trivy-java-db、trivy-checks、trivy-action、setup-trivy、trivy-operator、trivy-aws、trivy-mcp（MCP Server plugin）、trivy-vscode-extension。

### 2.3 Trivy 的五個核心領域

| 領域 | 說明 | Trivy 的角色 |
|------|------|--------------|
| Security Scanner | 偵測已知弱點、錯誤設定、敏感資訊 | 核心定位 |
| DevSecOps | 把安全左移到開發與 CI/CD | 提供 CLI、Exit Code、SARIF |
| Software Supply Chain Security | 管理相依套件、SBOM、VEX、Attestation | 產生與掃描 SBOM、支援 VEX |
| Container Security | 映像檔中的 OS 套件與應用程式相依 | 核心能力 |
| Cloud Native Security | Kubernetes、IaC、Cloud 設定 | `trivy k8s`、`trivy config`、Operator |

### 2.4 Trivy 與各類安全工具的差異

| 工具類型 | 全名 | 主要目的 | Trivy 能否取代 |
|----------|------|----------|----------------|
| SAST | Static Application Security Testing | 分析**自有原始碼**的邏輯漏洞（SQL Injection、XSS 路徑） | **不能**。Trivy 不做資料流 / 污點分析 |
| DAST | Dynamic Application Security Testing | 對**執行中**的應用程式發送攻擊請求 | **不能**。Trivy 不執行應用程式 |
| SCA | Software Composition Analysis | 找出第三方相依套件的已知漏洞 | **可以**執行主要 SCA 功能 |
| Container Scanner | — | 掃描映像檔 OS 套件與應用相依 | **核心能力** |
| Secret Scanner | — | 找出硬編碼的金鑰、密碼、Token | **可以**，規則可自訂 |
| IaC Scanner | Infrastructure as Code Scanner | 找出 Dockerfile、K8s、Terraform 的錯誤設定 | **可以** |
| SBOM Generator | Software Bill of Materials | 產生軟體物料清單 | **可以**（CycloneDX、SPDX） |
| CSPM | Cloud Security Posture Management | 持續監控雲端帳號設定 | **部分**：僅 AWS 且需 plugin，非完整 CSPM |

### 2.5 Trivy 不是什麼

> **【官方】** Trivy 是「偵測」工具，不是「修補」工具，也不是「執行期防護」工具。

Trivy **不負責**：

- 找出自有程式碼的業務邏輯漏洞（例如越權存取、IDOR）。
- 驗證身分驗證 / 授權流程是否正確。
- 偵測未公開的 0-day 漏洞（只能比對已收錄的 Advisory）。
- 判斷某個 CVE 在你的程式中是否「真的可被利用」（可透過 VEX 由人來聲明）。
- 自動修改程式碼或升級套件。
- 做出法律層面的 License 合規結論。
- 驗證 Clean Architecture 的分層依賴（請用 ArchUnit）。

### 2.6 Trivy 的價值與限制總表

| 面向 | 價值 | 限制 |
|------|------|------|
| 覆蓋面 | 一個工具涵蓋 Image、FS、Repo、IaC、K8s、SBOM | Cloud 僅 AWS 且需 plugin |
| 速度 | 本機與 CI 皆可快速執行，支援快取 | 首次需下載 DB；Java 需額外 Java DB |
| 整合 | SARIF、CycloneDX、SPDX、GitHub snapshot | k8s 報告僅 table / json |
| 準確度 | 使用多個 Vendor Advisory 來源 | 仍有 False Positive / False Negative |
| 成本 | 開源、免費 | 企業需自行維運 DB Mirror 與治理 |

### 實務案例

某電商平台過去同時使用三套工具：一套掃 Image、一套掃 npm、一套掃 Terraform，報告格式各不相同，Security Team 每週花兩天整理。改用 Trivy 後統一輸出 JSON 與 SARIF，由一支 Python 腳本彙整成 Dashboard。但團隊也清楚記錄：「SQL Injection 仍由 SAST 負責、登入流程弱點仍由 DAST 與滲透測試負責」，避免誤以為導入 Trivy 就完成 AppSec。

### 注意事項

- 不要在對外簡報中寫「導入 Trivy 即符合 OWASP Top 10」，這是過度宣稱。
- Trivy 找到 0 個 Finding，**不代表**系統是安全的，只代表在已知資料庫與已啟用的 Scanner 範圍內沒有發現問題。

---

## 3. Trivy 核心概念

### 3.1 六大要素

Trivy 的運作可以用六個要素理解：

```text
Target（掃描什麼）
   +
Scanner（找出什麼）
   +
Data Source（比對依據：Vulnerability DB、Java DB、Checks Bundle）
   +
Policy（過濾與判斷：severity、ignore、VEX、Rego）
   +
Report（輸出：table、json、sarif、cyclonedx、spdx…）
   +
CI/CD Gate（決策：exit-code、企業門檻）
```

| 要素 | 說明 | 主要 CLI / 設定 |
|------|------|-----------------|
| Target | 被掃描的對象 | `image`、`fs`、`repo`、`rootfs`、`vm`、`k8s`、`sbom`、`config` |
| Scanner | 偵測的問題類型 | `--scanners vuln,misconfig,secret,license,crypto` |
| Data Source | 比對資料 | `--db-repository`、`--java-db-repository`、`--checks-bundle-repository` |
| Policy | 篩選與抑制 | `--severity`、`--ignore-unfixed`、`--ignorefile`、`--vex`、`--ignore-policy` |
| Report | 輸出格式 | `--format`、`--output`、`--template`、`trivy convert` |
| CI/CD Gate | 是否讓流程失敗 | `--exit-code`、`--exit-on-eol` |

### 3.2 Trivy Overall Architecture

```mermaid
flowchart TB
    subgraph Input["輸入 Targets"]
        I1["Container Image"]
        I2["Filesystem / Rootfs"]
        I3["Git Repository"]
        I4["VM Image"]
        I5["Kubernetes Cluster"]
        I6["SBOM 檔案"]
    end
    subgraph Core["Trivy Core"]
        A["Artifact Analyzer<br/>解析套件與設定檔"]
        S1["Vulnerability Scanner"]
        S2["Misconfiguration Scanner"]
        S3["Secret Scanner"]
        S4["License Scanner"]
        S5["Crypto Scanner - Experimental"]
    end
    subgraph Data["Data Sources"]
        D1["trivy-db"]
        D2["trivy-java-db"]
        D3["trivy-checks bundle"]
        D4["VEX 文件"]
    end
    subgraph Output["輸出"]
        O1["table / json"]
        O2["sarif"]
        O3["cyclonedx / spdx"]
        O4["template / github"]
    end
    Input --> A
    A --> S1 & S2 & S3 & S4 & S5
    D1 --> S1
    D2 --> S1
    D3 --> S2
    D4 --> S1
    S1 & S2 & S3 & S4 & S5 --> Output
```

### 3.3 Target × Scanner Matrix

**【官方】** 下表依官方文件整理各 Target 預設與可用的 Scanner（✓＝可用；★＝預設啟用；—＝不適用 / 官方未說明）：

| Target | vuln | misconfig | secret | license | crypto |
|--------|------|-----------|--------|---------|--------|
| `trivy image` | ★ | ✓ | ★ | ✓ | ✓（Experimental） |
| `trivy fs` | ★ | ✓ | ★ | ✓ | — |
| `trivy repo` | ★ | ✓ | ★ | ✓ | — |
| `trivy rootfs` | ★ | ✓ | ★ | ✓ | — |
| `trivy vm`（Experimental） | ★ | ✓ | ★ | ✓ | — |
| `trivy config` | — | ★ | — | — | — |
| `trivy sbom` | ★ | — | — | ✓ | — |
| `trivy k8s`（Experimental） | ★ | ★ | ★ | — | — |

> **注意**：`image` / `fs` / `repo` / `vm` 的 `--scanners` 預設值為 `vuln,secret`；`sbom` 預設僅 `vuln`。**License 與 Misconfiguration 預設不啟用**，必須明確指定。這是許多團隊以為「Trivy 沒掃 License」的原因。
>
> `trivy k8s` 另有專屬的 `rbac` scanner，預設值為 `vuln,misconfig,secret,rbac`。

```mermaid
flowchart LR
    subgraph T["Targets"]
        T1["image"]
        T2["fs / repo"]
        T3["config"]
        T4["sbom"]
        T5["k8s"]
    end
    subgraph S["Scanners"]
        V["vuln"]
        M["misconfig"]
        SE["secret"]
        L["license"]
    end
    T1 --> V & SE
    T1 -.-> M & L
    T2 --> V & SE
    T2 -.-> M & L
    T3 --> M
    T4 --> V
    T4 -.-> L
    T5 --> V & M & SE
```

實線＝預設啟用；虛線＝需以 `--scanners` 明確啟用（k8s 為 Experimental，另含 rbac scanner）。

### 3.4 Scan Flow

```mermaid
sequenceDiagram
    participant U as Developer / AI Agent
    participant T as Trivy CLI
    participant C as Cache
    participant R as DB Repository
    participant A as Analyzer
    U->>T: trivy fs --scanners vuln,secret .
    T->>C: 檢查 DB 是否需更新
    alt DB 過期或不存在
        T->>R: 下載 trivy-db / java-db
        R-->>C: 儲存至 cache-dir
    end
    T->>A: 解析 lock file、套件、設定檔
    A-->>T: 套件清單與檔案內容
    T->>T: 比對 Advisory、執行規則
    T->>T: 套用 severity / ignore / VEX
    T-->>U: 輸出報告與 Exit Code
```

### 3.5 CI/CD Flow

```mermaid
flowchart LR
    A["Commit / PR"] --> B["Build + Unit Test"]
    B --> C["trivy fs / repo<br/>vuln + secret + misconfig"]
    C --> D["Build Image"]
    D --> E["trivy image"]
    E --> F["產生 SBOM<br/>CycloneDX"]
    F --> G["trivy config<br/>K8s YAML / Terraform"]
    G --> H{"Security Gate"}
    H -->|"Pass"| I["Push Registry / Deploy"]
    H -->|"Fail"| J["通知 Owner<br/>AI Agent 分析"]
    J --> A
```

### 3.6 AI Agent Integration Flow

```mermaid
flowchart TB
    A["AI Agent 接收任務"] --> B["Plan"]
    B --> C["Baseline Scan<br/>trivy fs --format json"]
    C --> D["Implement"]
    D --> E["Test"]
    E --> F["Re-scan"]
    F --> G["Compare Before / After"]
    G --> H{"新增 HIGH / CRITICAL<br/>或 Secret？"}
    H -->|"否"| I["產生 Security Report"]
    H -->|"是，可安全自動修"| D
    H -->|"是，需人工判斷"| K["停止並請求 Human Approval"]
    I --> J["Human Review"]
    K --> J
    J --> L["Commit / PR"]
```

### 3.7 Trivy 的三種執行模式

| 模式 | 說明 | 適用情境 |
|------|------|----------|
| Standalone（預設） | CLI 自行下載 DB、自行掃描 | 開發者本機、一般 CI |
| Client / Server | `trivy server` 集中持有 DB，Client 以 `--server` 連線 | 大型企業多 Runner 共用 DB |
| Operator | 在 Kubernetes 叢集內持續掃描，結果存成 CRD | Production 叢集持續監控 |

### 實務案例

某團隊的 AI Agent 被要求「升級 Spring Boot」。過去 AI Agent 只跑 `mvn test` 就宣告完成；導入 3.6 的流程後，AI Agent 必須在升級前執行 Baseline Scan，升級後 Re-scan，並以 JSON diff 列出「新增 2 個 HIGH、移除 11 個 CRITICAL」。Reviewer 從此有了客觀依據。

### 注意事項

- Target × Scanner 的「預設值」會隨版本變動，CI 中**務必明確寫出 `--scanners`**，不要依賴預設。
- `trivy config` 只做 misconfig；若要同時掃 Secret，請用 `trivy fs --scanners misconfig,secret`。

---

## 4. Trivy Targets

**【官方】** v0.75.0 官方文件列出的 Target 為：Container Image、Filesystem、Rootfs、Code Repository、Virtual Machine Image、Kubernetes、SBOM。另外 `trivy config` 以設定檔為對象，專做 Misconfiguration 掃描。

| CLI | 別名 | Target | 狀態 |
|-----|------|--------|------|
| `trivy image` | `i` | Container Image（本機、Registry、tar） | Stable |
| `trivy filesystem` | `fs` | 本機目錄 / 檔案 | Stable |
| `trivy repository` | `repo` | 本機或遠端 Git Repository | Stable |
| `trivy rootfs` | — | 已展開的根檔案系統（例如容器內 `/`） | Stable |
| `trivy vm` | — | VM 映像檔、AWS AMI、EBS Snapshot | **Experimental** |
| `trivy kubernetes` | `k8s` | Kubernetes Cluster | **Experimental** |
| `trivy sbom` | — | CycloneDX / SPDX SBOM 檔或 Attestation | Stable |
| `trivy config` | `conf` | IaC 設定檔 | Stable |

### 4.1 Container Image

#### 4.1.1 掃描對象

| 對象 | 說明 |
|------|------|
| Docker Image | 本機 Docker Engine 中的映像檔 |
| OCI Image | 符合 OCI Image Spec 的映像檔 |
| Registry Image | 直接從 Registry 拉取 manifest 與 layer，不需本機 Docker |
| Local Image | 本機 Docker / containerd / Podman 中的映像檔 |
| Image tar | `docker save` 產生的 tar 檔（`--input`） |
| Image Layer | 逐層分析，報告會標示 Finding 來自哪一層 |
| OS Packages | apk、dpkg、rpm 等 OS 套件 |
| Application Dependencies | 映像檔內的 jar、node_modules、Python site-packages、Go binary 等 |

`--image-src` 決定映像來源的優先順序，預設為 `docker,containerd,podman,remote`。

#### 4.1.2 基本範例

**Linux / macOS（Bash）**：

```bash
# 掃描公開映像檔（僅示範，企業環境不建議用 latest）
trivy image nginx:latest

# 只看 HIGH 與 CRITICAL，且只看已有修補版本的弱點
trivy image --severity HIGH,CRITICAL --ignore-unfixed nginx:1.27.5

# 以 digest 掃描，確保掃描對象與部署對象一致
trivy image nginx@sha256:<digest>

# 掃描 docker save 產生的 tar
docker save -o app.tar registry.example.com/app:1.4.2
trivy image --input app.tar
```

**Windows（PowerShell）**：

```powershell
# Windows 需已安裝 Docker Desktop 或可連線的 Registry
trivy image --severity HIGH,CRITICAL --ignore-unfixed nginx:1.27.5

# 掃描 tar 檔
docker save -o app.tar registry.example.com/app:1.4.2
trivy image --input .\app.tar
```

#### 4.1.3 預期結果

報告分為兩段：

1. **Report Summary**：每個 Target（OS 層、各語言 lock file / jar）各掃到幾個 Vulnerability、Secret。
2. **Detailed Tables**：每筆 Finding 的 Library、Vulnerability ID、Severity、Status、Installed Version、Fixed Version、Title。

#### 4.1.4 為什麼企業環境不應只用 `latest`

| 方式 | 範例 | 問題 / 優點 |
|------|------|-------------|
| `latest` | `nginx:latest` | 內容隨時變動；今天掃的跟明天部署的可能不是同一個映像檔 |
| Version tag | `nginx:1.27.5` | 可讀性高，但 tag 仍可被覆寫（mutable） |
| Digest | `nginx@sha256:...` | 內容雜湊，**不可變**；掃描與部署保證是同一份 |
| Immutable artifact | Registry 開啟 tag immutability | 防止 tag 被覆寫，搭配 digest 最可靠 |

> **【企業建議】** CI 中 `trivy image` 與 `kubectl apply` 應使用**同一個 digest**。2026-03 的事件中，攻擊者就是透過覆寫 mutable tag（Docker Hub 的 `0.69.5`、`0.69.6`、`latest`）散布惡意映像檔，以 digest 引用者不受影響。

#### 4.1.5 常見問題

| 問題 | 原因 | 解法 |
|------|------|------|
| `unable to inspect the image` | 本機無 Docker、權限不足、Registry 需認證 | 確認 Docker socket、使用 `TRIVY_USERNAME` / `TRIVY_PASSWORD` 或 `trivy registry login` |
| 掃描非常慢 | 映像檔過大、首次下載 DB | 使用快取、限制 `--scanners`、`--max-image-size`（Experimental） |
| 多架構映像掃錯平台 | 預設掃描本機平台 | 使用 `--platform linux/amd64` |

#### 4.1.6 安全注意事項

- Registry 密碼**不要**放在命令列參數（會留在 shell history 與 process list），改用環境變數或 `--password-stdin`。官方 CLI 說明也明確寫著「TRIVY_PASSWORD should be used for security reasons」。
- 掃描未知來源的映像檔時，Trivy 只做靜態分析不執行映像，但仍應在隔離的 Runner 進行。

### 4.2 Filesystem

#### 4.2.1 掃描對象

`trivy fs` 掃描本機目錄，適合在**建置前**找出問題：

| 對象 | 範例 |
|------|------|
| 原始碼 | `src/` 內硬編碼的 Secret |
| Dependency Lock File | `pom.xml`、`gradle.lockfile`、`package-lock.json`、`pnpm-lock.yaml`、`yarn.lock` |
| IaC | `Dockerfile`、`k8s/*.yaml`、`*.tf`、Helm Chart |
| Configuration | `application.yml`、`.env` |
| Build Artifact | `target/*.jar`、`dist/` |

#### 4.2.2 範例

```bash
# 預設：vuln + secret
trivy fs .

# 企業建議：明確列出 Scanner
trivy fs --scanners vuln,secret,misconfig --severity HIGH,CRITICAL .

# 包含 License（預設不啟用）
trivy fs --scanners license --license-full .

# 跳過不需掃描的目錄
trivy fs --skip-dirs "node_modules,**/test/fixtures" .
```

```powershell
trivy fs --scanners vuln,secret,misconfig --severity HIGH,CRITICAL .
```

#### 4.2.3 預期結果

以 Lock file 為單位列出 Vulnerability，以檔案為單位列出 Secret 與 Misconfiguration。

#### 4.2.4 常見問題

- **Maven 專案沒有掃出傳遞相依**：`pom.xml` 掃描時 Trivy 會嘗試解析 parent 與遠端 POM，企業內網需設定 Maven mirror（見第 22 章）。若已執行 `mvn package`，掃描 `target/*.jar` 通常更完整。
- **npm 專案沒有結果**：缺少 `package-lock.json`。Trivy 以 lock file 為準，只有 `package.json` 無法解析確切版本。

#### 4.2.5 安全注意事項

- `trivy fs` 會讀取目錄中的所有檔案，若目錄中有 `.env` 或私鑰，報告中會出現 Secret Finding，報告本身即成為敏感資料。

### 4.3 Git Repository

#### 4.3.1 本機與遠端

```bash
# 本機 repo（含 .git）
trivy repo .

# 遠端公開 repo
trivy repo https://github.com/example/example

# 指定 branch / tag / commit
trivy repo --branch release/2.x https://github.com/example/example
trivy repo --tag v1.4.2 https://github.com/example/example
trivy repo --commit <commit-sha> https://github.com/example/example
```

私有遠端 repo 以環境變數提供 Token（Bash）：

```bash
export GITHUB_TOKEN="<從 Secret Manager 取得，勿寫死>"
trivy repo https://github.com/example/private-repo
```

> v0.75.0 起，遠端 repo URL 中若含有帳密，產生報告時會被移除（fix: strip credentials from remote repository URL in artifact name）。但仍**不應**把 Token 寫在 URL 中。

#### 4.3.2 `trivy fs` vs `trivy repo`

| 面向 | `trivy fs` | `trivy repo` |
|------|------------|--------------|
| 對象 | 任意目錄 | Git repository（本機或遠端） |
| 遠端掃描 | 不支援 | 支援，會 clone 後掃描 |
| 指定版本 | 不適用 | `--branch`、`--tag`、`--commit` |
| 未 commit 的檔案 | 會掃 | 本機 repo 會掃工作目錄 |
| 報告中的 Git metadata | v0.68 起偵測到 Git 資訊時 artifact type 為 repository | 有 |
| 典型用途 | 開發者本機、CI checkout 後 | 稽核特定版本、Reverse Engineering |

#### 4.3.3 Repository Scan 在各情境的用途

| 情境 | 用途 |
|------|------|
| AI Reverse Engineering | 不需建置即可盤點 Legacy repo 的相依、Secret、IaC 問題 |
| Legacy System Analysis | 以 `--tag` 掃描歷史 release，比較各版本安全狀態 |
| Framework Upgrade | 以 `--branch` 分別掃描 `main` 與 `upgrade/spring-boot-4` |
| CI/CD | PR 時掃描變更後的 repo 狀態 |

### 4.4 Rootfs

`trivy rootfs` 掃描已展開的根檔案系統，常見用法是**在映像檔建置過程中掃描自身**：

```dockerfile
# 多階段建置中的掃描階段（官方 Embed in Dockerfile 文件的作法）
FROM registry.example.com/base/eclipse-temurin:25-jre AS runtime
COPY --from=build /app/target/app.jar /app/app.jar

FROM runtime AS scan
COPY --from=registry.example.com/security/trivy:0.75.0 /usr/local/bin/trivy /usr/local/bin/trivy
RUN trivy rootfs --no-progress --scanners vuln,secret --exit-code 1 --severity CRITICAL /
```

> **注意**：在建置中掃描需要能下載 DB，或預先放入離線 DB。正式 CI 仍建議用 `trivy image` 掃描最終映像檔。

### 4.5 Virtual Machine Image（Experimental）

```bash
# 本機 VM 映像檔
trivy vm --scanners vuln disk.vmdk

# AWS AMI 與 EBS Snapshot（需 AWS 認證與 --aws-region）
trivy vm --scanners vuln --aws-region ap-northeast-1 ami:<ami-id>
trivy vm --aws-region ap-northeast-1 ebs:<snapshot-id>
```

適合「黃金映像（Golden Image）」與雲端 AMI 的上線前檢查。由於屬 Experimental，不建議作為唯一的上線 Gate。

### 4.6 Kubernetes

`trivy k8s` 連線至 Kubernetes Cluster 掃描 Workload、Image、RBAC 與 Node 設定。詳見第 10 章。

### 4.7 SBOM

`trivy sbom` 以既有的 CycloneDX / SPDX SBOM 為輸入，重新比對最新弱點資料。詳見第 6 章。

### 4.8 Dockerfile / IaC / Terraform / Kubernetes YAML

`trivy config` 專門掃描設定檔：

```bash
trivy config .
trivy config --severity HIGH,CRITICAL ./deploy
```

**【官方】** v0.75.0 預設的 misconfig scanners：`azure-arm`、`cloudformation`、`dockerfile`、`helm`、`kubernetes`、`terraform`、`terraformplan-json`、`terraformplan-snapshot`、`ansible`。詳見第 7 章。

### 4.9 Cryptographic Asset（v0.75 新增，Experimental）

```bash
trivy image --scanners crypto --format cyclonedx --output cbom.cdx.json registry.example.com/app:1.4.2
```

| 項目 | 說明 |
|------|------|
| 掃描內容 | `.pem`、`.der`、`.crt`、`.cer`、`.key` 中的 X.509 憑證、公鑰與私鑰 |
| 輸出 | CycloneDX 的 `cryptographic-asset` 元件（CBOM，Cryptography Bill of Materials） |
| 限制 | **僅支援 container image + CycloneDX 輸出**，Experimental |
| 安全性 | 官方說明私鑰的值不會被寫入報告 |
| 用途 | 盤點即將到期的憑證、弱演算法、後量子（ML-DSA）準備度 |

### 實務案例

某保險公司的 Platform Team 發現：同一個 `app:2.3` tag 在三個環境的 digest 都不同，因為不同時間重新 build 又 push 了。導入「以 digest 掃描、以 digest 部署」後，稽核時可以明確證明「Production 執行的映像檔就是 CI 掃描通過的那一個」。

### 注意事項

- `trivy vm` 與 `trivy k8s` 都是 **Experimental**，CLI 與輸出格式可能在後續版本變更。
- `trivy fs` 與 `trivy image` 的結果**不會相同**：`fs` 看不到 OS 套件，`image` 看不到未打包進映像的 IaC 檔。兩者都要掃。

---

## 5. Vulnerability Scanner

### 5.1 基本概念

| 名詞 | 說明 |
|------|------|
| CVE | Common Vulnerabilities and Exposures，公開弱點的統一編號 |
| GHSA | GitHub Security Advisory 編號 |
| OS Package | apk、dpkg、rpm 等系統套件 |
| Language Package | Maven、npm、PyPI、Go module 等應用程式相依 |
| Non-packaged Software | 未經套件管理器安裝、但 Trivy 能辨識版本的軟體（例如 Go binary、jar） |
| Kubernetes Components | api-server、kubelet 等元件（`trivy k8s`） |
| Fixed Version | 已修補此弱點的版本 |
| Unfixed Vulnerability | 尚無修補版本的弱點 |
| EOL | End of Life，OS 已停止支援 |

### 5.2 Severity

**【官方】** Trivy 的 Severity 分為：

| Severity | 說明 |
|----------|------|
| UNKNOWN | 資料來源未提供嚴重度；v0.72 起資料缺失時也會落入 UNKNOWN |
| LOW | 低 |
| MEDIUM | 中 |
| HIGH | 高 |
| CRITICAL | 嚴重 |

Severity 的來源可能是 Vendor Advisory（例如 Red Hat、Debian、Ubuntu）或 NVD。`--vuln-severity-source` 可指定優先順序，預設為 `auto`：

```bash
# 以 NVD 優先，其次 GHSA
trivy image --vuln-severity-source nvd,ghsa registry.example.com/app:1.4.2
```

> **為什麼同一個 CVE 在不同映像檔的 Severity 不同？** 因為 OS Vendor 會依自身打包方式重新評估。例如某 CVE 在 NVD 是 HIGH，在 Debian 可能被評為 LOW。報告中的 `SeveritySource` 欄位會告訴你來源。

### 5.3 CVSS

JSON 報告的 `CVSS` 欄位會列出各來源的 CVSS 分數與向量（v0.58 起含 CVSS v4）。

```json
{
  "VulnerabilityID": "CVE-2025-XXXXX",
  "PkgName": "com.fasterxml.jackson.core:jackson-databind",
  "InstalledVersion": "2.15.0",
  "FixedVersion": "2.15.4",
  "Status": "fixed",
  "Severity": "HIGH",
  "SeveritySource": "ghsa",
  "CVSS": {
    "ghsa": { "V3Vector": "CVSS:3.1/AV:N/AC:L/...", "V3Score": 7.5 }
  }
}
```

### 5.4 Vulnerability Status

**【官方】** 可被 `--ignore-status` 指定的狀態：

| Status | 意義 | 是否會被偵測 |
|--------|------|--------------|
| `fixed` | 已有修補版本 | 是 |
| `affected` | 受影響、尚無修補 | 是 |
| `will_not_fix` | Vendor 表示不打算修補 | 是 |
| `fix_deferred` | 延後修補 | 是 |
| `end_of_life` | 元件已 EOL，未做影響分析 | 是 |
| `unknown` / `not_affected` / `under_investigation` | 官方說明這些狀態不會被偵測 | 否 |

`--ignore-unfixed` 是 `--ignore-status affected,will_not_fix,fix_deferred,end_of_life` 的簡寫，只顯示 `fixed`。

### 5.5 EOL 偵測

```bash
# OS 已 EOL 時以 exit code 2 結束
trivy image --exit-on-eol 2 registry.example.com/legacy-app:3.1
```

> **【企業建議】** Legacy 系統常跑在 EOL 的 Base Image 上，此時大量 CVE 狀態會是 `end_of_life` 或 `affected`。`--exit-on-eol` 可以讓 Gate 明確區分「有弱點」與「底層已無人維護」。

### 5.6 偵測精準度

`--detection-priority`：

| 值 | 說明 |
|----|------|
| `precise`（預設） | 降低 False Positive |
| `comprehensive` | 偵測更多，可能增加 False Positive |

### 5.7 VEX

VEX（Vulnerability Exploitability eXchange）是一份聲明文件，說明「某 CVE 在某產品中是否可被利用」。Trivy 支援 OpenVEX、CSAF、CycloneDX VEX：

```bash
# 使用本機 VEX 檔（--vex 為 Experimental）
trivy image --vex ./vex/app.openvex.json --show-suppressed registry.example.com/app:1.4.2
```

被 VEX 抑制的 Finding 可用 `--show-suppressed` 顯示，JSON 中為 `ExperimentalModifiedFindings`。

VEX 文件的來源：

| 來源 | 用法 | 說明 |
|------|------|------|
| 本機檔案 | `--vex ./app.openvex.json` | 最直接 |
| VEX Repository | `--vex repo`、`trivy vex repo` | v0.54 起支援，可訂閱公開 VEX Repository |
| OCI artifact | `--vex oci` | v0.54 起可從 Registry 取得 VEX attestation；v0.73 起可原生探索存成 OCI artifact 的 VEX，並從一般 in-toto OCI referrers 中找出 OpenVEX |
| SBOM 引用 | CycloneDX SBOM 內的外部參照 | v0.60 起初步支援 |

> **【企業建議】** VEX 與映像一起以 OCI artifact 發布，可讓下游（其他團隊、客戶）取得同一份「不受影響」聲明。

### 5.8 企業處理流程：Block / Warn / Monitor / Accept

**【企業建議】** Trivy 只提供 Severity 與 Status，**不規定**企業該如何處理。以下為範本，必須依組織 Security Policy 調整：

| 處理等級 | 觸發條件範例 | 動作 |
|----------|-------------|------|
| Block | CRITICAL 且 `Status=fixed` | CI 失敗，必須修正或取得核准 Exception |
| Warn | HIGH 且 `Status=fixed` | CI 通過但產生 Ticket，設定修正期限 |
| Monitor | MEDIUM、或 HIGH/CRITICAL 但 unfixed | 納入儀表板與定期檢視 |
| Accept | 經風險評估、有 Owner 與到期日 | 以 `.trivyignore.yaml` 或 VEX 記錄 |

```mermaid
flowchart TD
    F["Trivy Finding"] --> S{"Severity"}
    S -->|"CRITICAL"| C{"有 Fixed Version？"}
    S -->|"HIGH"| H{"有 Fixed Version？"}
    S -->|"MEDIUM / LOW"| M["Monitor / Track"]
    S -->|"UNKNOWN"| U["人工判讀"]
    C -->|"是"| B["Block"]
    C -->|"否"| R["風險評估 + 補償控制"]
    H -->|"是"| W["Warn + 期限內修正"]
    H -->|"否"| R
    R --> A["Accept with Expiration"]
```

### 5.9 v0.69–v0.75 新增的偵測覆蓋範圍

**【官方】** 完整清單以官方 Scanning Coverage 頁面為準，以下為近期重要變化：

| 類別 | 項目 | 版本 | 對企業的意義 |
|------|------|------|--------------|
| OS | Ubuntu 26.04 LTS | v0.71 | 新 LTS 可被正確偵測與判斷 EOL |
| OS | Bottlerocket OS 弱點比對 | v0.72 | AWS 容器專用 OS |
| OS | Rocky modular 套件、ActiveState 映像 | v0.69 | RHEL 系與商用映像 |
| 第三方修補版 | Echo、Root.io、Seal、RapidFort curated image | v0.63–v0.75 | 使用商用「修補後重建」套件時，改以該廠商的 Advisory 比對，避免以上游版本誤報 |
| Python | `pylock.toml`（PEP 751） | v0.70 | 新的標準 lock file |
| Python | uv workspace（含 virtual workspace） | v0.75 | workspace 成員的相依不再被視為 dev，預設就會回報 |
| Python | Echo 修補版套件（版本後綴 `+echo.N`） | v0.75 | 改以 Echo OSV feed 比對 |
| .NET | self-contained 部署內嵌的 runtime | v0.72 | 過去容易漏掃的 runtime 弱點 |
| Go | `-trimpath` 建置的 binary 以 ELF symbol table 判斷版本 | v0.70 | Go binary 辨識率提高 |
| Java | `settings.xml` mirrors / proxy、`trivy.yaml` Maven mirrors | v0.70–v0.73 | 企業內網 Maven 解析 |
| Node.js | pnpm workspace 重疊套件、multi-document lock、`package-lock.json` boolean `resolved` | v0.72–v0.75 | monorepo 解析穩定性 |
| Julia | Julia 生態系弱點掃描 | v0.69 | 資料科學團隊 |

> **升級提醒**：覆蓋範圍擴大會讓 Finding 數「合理地」增加。升級 Trivy 後的差異應以第 41.4 節的新舊版比較檢視，不要誤判為程式退化。

### 實務案例

某團隊的 Gate 原本設定「任何 HIGH 都 Fail」，結果一個 Debian Base Image 有 40 個 HIGH 但全部 `affected`（無修補），團隊無法前進，最後把 Gate 整個關掉。改為「CRITICAL 且 fixed 才 Block、unfixed 進入風險評估」後，Gate 重新啟用且三個月內沒有再被關閉。

### 注意事項

- 不要自行發明 CVE 風險分數；以 Vendor / NVD 的 Severity 為輸入，以企業 Policy 決定處理等級。
- `--ignore-unfixed` 是過濾顯示，不代表風險消失；unfixed 的 CRITICAL 仍需風險評估。

---

## 6. SBOM

### 6.1 SBOM 是什麼

SBOM（Software Bill of Materials，軟體物料清單）是一份機器可讀的清單，記錄軟體由哪些元件組成、各元件的版本、來源、授權與相依關係。

### 6.2 為什麼需要 SBOM

| 需求 | SBOM 的作用 |
|------|-------------|
| Software Supply Chain | 知道你的軟體裡有什麼，才能管理供應鏈風險 |
| Dependency Transparency | 讓客戶、稽核、主管機關看到相依組成 |
| Software Inventory | 企業層級盤點所有系統用了哪些套件 |
| 新 CVE 爆發時的應變 | 不用重新建置，直接以 SBOM 查詢哪些系統受影響 |
| 法規要求 | 美國 EO 14028 與 NTIA 最低要素、各國金融監理逐步要求提供 SBOM |

> **SBOM 不只是掃描報告，而是 Software Supply Chain Governance 的重要資料。** 掃描報告會過時，SBOM 則可以在未來任何時間點重新比對新的 CVE。

### 6.3 支援格式

| 格式 | `--format` 值 | 說明 |
|------|---------------|------|
| CycloneDX | `cyclonedx` | OWASP 主導，JSON 格式；v0.71 起支援 CycloneDX 1.7 |
| SPDX（tag-value） | `spdx` | Linux Foundation 主導，ISO/IEC 5962 |
| SPDX JSON | `spdx-json` | SPDX 的 JSON 表示法 |
| GitHub Dependency Snapshot | `github` | 提交至 GitHub Dependency Graph |

### 6.4 SBOM Generation

```bash
# Container Image → CycloneDX
trivy image --format cyclonedx --output app-1.4.2.cdx.json registry.example.com/app:1.4.2

# Container Image → SPDX tag-value
trivy image --format spdx --output app-1.4.2.spdx registry.example.com/app:1.4.2

# Container Image → SPDX JSON
trivy image --format spdx-json --output app-1.4.2.spdx.json registry.example.com/app:1.4.2

# 原始碼目錄 → CycloneDX
trivy fs --format cyclonedx --output source.cdx.json .

# CycloneDX 同時附帶弱點資訊（CycloneDX 可內嵌 vulnerabilities）
trivy image --format cyclonedx --scanners vuln --output app-with-vuln.cdx.json registry.example.com/app:1.4.2
```

> **注意**：SBOM 輸出時，未以 `--scanners` 指定 vuln 的話，預設只產出元件清單。要包含弱點請明確加上 `--scanners vuln`。

### 6.5 SBOM Consumption 與 SBOM Vulnerability Scanning

```bash
# 以最新 DB 重新掃描既有 SBOM
trivy sbom app-1.4.2.cdx.json

# SBOM 也可以掃 License
trivy sbom --scanners vuln,license app-1.4.2.cdx.json

# 掃描 CycloneDX attestation（in-toto）
trivy sbom app-1.4.2.cdx.intoto.jsonl
```

| 時機 | 用途 |
|------|------|
| 建置時 | 產生 SBOM，與映像檔一起保存 |
| 每日排程 | 以最新 DB 掃描所有 Production SBOM，找出新揭露的 CVE |
| 事件應變 | 新 0-day 公布時，直接查詢 SBOM 判斷受影響範圍 |

### 6.6 SBOM Attestation

SBOM Attestation 是把 SBOM 以簽章方式綁定到映像檔，證明「這份 SBOM 確實屬於這個 digest」。官方文件以 cosign 示範：

```bash
# 1. 產生 SBOM
trivy image --format cyclonedx --output sbom.cdx.json registry.example.com/app@sha256:<digest>

# 2. 以 cosign 建立 attestation（keyless 或企業金鑰）
cosign attest --type cyclonedx --predicate sbom.cdx.json registry.example.com/app@sha256:<digest>

# 3. 從 OCI / Rekor 取得 SBOM 進行掃描（--sbom-sources 為 Experimental）
trivy image --sbom-sources oci registry.example.com/app@sha256:<digest>
```

### 6.7 KBOM 與 CBOM

| 類型 | 指令 | 說明 |
|------|------|------|
| KBOM | `trivy k8s --format cyclonedx --output kbom.cdx.json` | Kubernetes Bill of Materials：控制平面、節點元件、Addon 版本 |
| CBOM | `trivy image --scanners crypto --format cyclonedx ...` | 密碼學資產清單（v0.75，Experimental） |

> 官方說明 KBOM 的弱點比對目前對原生 Kubernetes 效果較好，部分雲端託管發行版可能不準確。

### 6.8 供應鏈流程

```mermaid
flowchart LR
    A["Source"] --> B["Dependency"]
    B --> C["Build"]
    C --> D["SBOM<br/>trivy image --format cyclonedx"]
    D --> E["Container"]
    E --> F["Registry<br/>SBOM Attestation"]
    F --> G["Deployment"]
    G --> H["Runtime"]
    H -.->|"每日 trivy sbom 重掃"| D
```

### 6.9 SBOM 管理建議

| 項目 | 【企業建議】 |
|------|-------------|
| 命名 | `<system>-<component>-<version>-<digest前12碼>.cdx.json` |
| 保存位置 | 與映像檔一起放在 Registry（OCI artifact / attestation），另備份至 Artifact Repository |
| 保存期限 | 至少與系統生命週期相同；金融業依稽核要求 |
| 格式選擇 | 對內以 CycloneDX 為主（弱點、VEX、CBOM 支援完整）；對外依客戶要求提供 SPDX |
| 重掃頻率 | Production SBOM 每日重掃 |

### 實務案例

某次 Java 函式庫爆出 CRITICAL 0-day 時，有 SBOM 的團隊在 30 分鐘內以 `trivy sbom` 批次查出 14 個受影響系統；沒有 SBOM 的團隊花了兩天逐一重新建置與掃描。

### 注意事項

- `trivy fs` 產生的 SBOM 只含 lock file 內的應用相依，不含 OS 套件；交付用 SBOM 應以**最終映像檔**為準。
- `trivy sbom` 不支援 `--skip-dirs` / `--skip-files`（v0.63 起停用）。

---

## 7. Misconfiguration / IaC Security

### 7.1 IaC 與 Misconfiguration

IaC（Infrastructure as Code）把基礎設施寫成程式碼。Misconfiguration 是指設定違反安全最佳實務，例如容器以 root 執行、S3 Bucket 公開。

**【官方】** Trivy 的 IaC 覆蓋範圍：

| 類型 | 說明 |
|------|------|
| Dockerfile | 基礎映像、USER、HEALTHCHECK 等 |
| Kubernetes YAML | Pod Security、資源限制、權限 |
| Helm | 會先 render 再檢查，可帶 `--helm-values`、`--helm-set` |
| Terraform / OpenTofu | HCL、Terraform plan JSON、plan snapshot |
| CloudFormation | AWS 範本 |
| Azure ARM Template | Azure 範本 |
| Ansible | v0.69 起初始支援 |

規則來自 **trivy-checks** bundle，預設從 `mirror.gcr.io/aquasec/trivy-checks:2` 下載。

### 7.2 基本範例

```bash
trivy config .
trivy config --severity HIGH,CRITICAL ./deploy

# Helm Chart 帶入 values
trivy config --helm-values ./charts/app/values-prod.yaml ./charts/app

# Terraform 帶入變數檔
trivy config --tf-vars ./env/prod.tfvars ./terraform

# 同時掃 Secret
trivy fs --scanners misconfig,secret ./deploy
```

### 7.3 Dockerfile 範例

**有問題的 Dockerfile**：

```dockerfile
FROM eclipse-temurin:latest
COPY target/app.jar /app.jar
EXPOSE 22 8080
CMD ["java", "-jar", "/app.jar"]
```

可能的 Finding（ID 以實際報告為準）：

| 問題 | 常見對應規則 |
|------|-------------|
| 使用 `latest` tag | AVD-DS-0001 |
| 未指定非 root `USER` | AVD-DS-0002 |
| 缺少 `HEALTHCHECK` | AVD-DS-0026 |
| 開放 22 port | 依規則集而定 |

**修正後**：

```dockerfile
FROM eclipse-temurin:25-jre-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app
COPY --chown=app:app target/app.jar app.jar
USER app
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
```

### 7.4 Kubernetes YAML 範例

**有問題的 Deployment**：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
spec:
  replicas: 2
  selector:
    matchLabels: { app: order-api }
  template:
    metadata:
      labels: { app: order-api }
    spec:
      containers:
        - name: app
          image: registry.example.com/order-api:latest
          securityContext:
            privileged: true
```

**修正後**：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
spec:
  replicas: 2
  selector:
    matchLabels: { app: order-api }
  template:
    metadata:
      labels: { app: order-api }
    spec:
      automountServiceAccountToken: false
      securityContext:
        runAsNonRoot: true
        seccompProfile: { type: RuntimeDefault }
      containers:
        - name: app
          image: registry.example.com/order-api@sha256:<digest>
          securityContext:
            privileged: false
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities: { drop: ["ALL"] }
          resources:
            requests: { cpu: "250m", memory: "512Mi" }
            limits: { cpu: "1", memory: "1Gi" }
```

### 7.5 Terraform 範例

```hcl
resource "aws_s3_bucket" "reports" {
  bucket = "corp-reports-example"
}

resource "aws_s3_bucket_public_access_block" "reports" {
  bucket                  = aws_s3_bucket.reports.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "reports" {
  bucket = aws_s3_bucket.reports.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}
```

Trivy 可找出的典型問題類型：

| 類型 | 範例 |
|------|------|
| Privileged Container | `privileged: true` |
| Root User | 未設 `runAsNonRoot`、Dockerfile 無 `USER` |
| Exposed Port | Security Group 對 `0.0.0.0/0` 開放管理埠 |
| Insecure Kubernetes Setting | 掛載 hostPath、hostNetwork、缺少資源限制 |
| Public Cloud Resource | S3 公開存取、資料庫公開 |
| Weak IAM | IAM Policy 使用 `*` 權限 |
| Encryption | 未啟用儲存加密、未強制 TLS |
| Network | 缺少 Network Policy、預設 Security Group 過寬 |
| Storage | 未啟用版本控制、日誌 |

### 7.6 Inline Ignore 與自訂規則

```dockerfile
# trivy:ignore:AVD-DS-0026
FROM registry.example.com/base/batch-runner:2.1
```

```hcl
# 理由：公開網站靜態檔，經 SEC-EXC-2026-031 核准，到期日 2026-12-31
#trivy:ignore:<報告中的 check ID>
resource "aws_s3_bucket" "static_site" {
  bucket = "corp-public-website"
}
```

> **【企業建議】** Inline Ignore 必須附帶理由註解與 Ticket 編號，並在 Code Review 時特別檢視。AI Agent **不得**自行新增 Inline Ignore（見第 29 章）。

自訂 Rego 規則：

```bash
trivy config --config-check ./policies --check-namespaces user ./deploy
```

### 7.7 不要把所有 Misconfiguration 都當成漏洞

| 概念 | 意義 | 範例 |
|------|------|------|
| Finding | 掃描器的觀察結果 | 「S3 Bucket 未阻擋公開存取」 |
| Risk | 在企業情境下的實際風險 | 此 Bucket 存放的是公開網站靜態檔，風險低 |
| Policy | 企業規定 | 「僅 `public-web` 標籤的 Bucket 可公開」 |
| Exception | 經核准的例外 | Exception ID、Owner、到期日 |
| Remediation | 修正動作 | 套用 Public Access Block |

```mermaid
flowchart LR
    F["Finding"] --> R["Risk 評估"]
    R --> P{"符合 Policy？"}
    P -->|"是"| E["Exception 記錄"]
    P -->|"否"| M["Remediation"]
    M --> V["Re-scan 驗證"]
```

### 實務案例

某團隊第一次對 Helm Chart 執行 `trivy config`，出現 230 個 Finding。逐項檢視後發現 180 個來自第三方 Chart 的預設值。團隊建立「僅檢查自有 Chart + values-prod.yaml render 結果」的掃描範圍，並以 Policy 決定哪些規則在 Production 必須 Block，Finding 降到 27 個可執行的修正項目。

### 注意事項

- Helm Chart 未帶入 Production values 時，掃描結果與實際部署會有落差。
- 規則 ID 會隨 trivy-checks 版本調整；v0.69 起 provider mapping 改用 ID，自訂 Rego 規則升級時需回歸測試。

---

## 8. Secret Scanner

### 8.1 偵測對象

| 類型 | 範例 |
|------|------|
| API Key | 雲端服務、SaaS 的 API Key |
| Password | 設定檔中的明文密碼 |
| Token | GitHub Token、JWT、Slack Token |
| Private Key | RSA、EC 私鑰 |
| Credential | 各種帳密組合 |
| Cloud Credential | AWS Access Key、Azure、GCP 金鑰（v0.71 新增 Azure 規則） |
| Database Credential | JDBC URL 中的帳密 |
| AI 服務 Key | v0.72 新增 OpenAI 規則 |
| GitHub App Token | v0.72 支援新的 stateless installation token 格式 |
| Maven 設定 | v0.71 新增 `settings.xml` / `settings-security.xml` 密碼規則 |

### 8.2 基本範例

```bash
trivy fs --scanners secret .
trivy image --scanners secret registry.example.com/app:1.4.2
```

### 8.3 Secret Configuration（trivy-secret.yaml）

預設讀取工作目錄的 `trivy-secret.yaml`，可用 `--secret-config` 指定路徑：

```yaml
# trivy-secret.yaml
rules:
  - id: corp-internal-api-key
    category: Corporate
    title: Corporate Internal API Key
    severity: CRITICAL
    keywords:
      - corp_api_key
    regex: (?i)corp_api_key\s*[:=]\s*['"]?[A-Za-z0-9]{32}

allow-rules:
  - id: test-fixtures
    description: 測試資料中的假金鑰
    path: .*/src/test/resources/fixtures/.*

disable-rules:
  - slack-web-hook
```

> v0.75 起可用 `--secret-config=""` 停用設定檔載入，避免 CI 受 repo 內被竄改的設定檔影響（例如攻擊者加入 allow-rules 讓真實 Secret 被略過）。
>
> v0.71 起可自訂 Secret Scanner 預設略過的目錄、檔案與副檔名；設定鍵名請以該版 Secret Scanner 官方文件為準。擴大略過範圍等同弱化 Scanner，應由 DevSecOps 審核。v0.75 起 Secret 掃描改用單次 Aho-Corasick 比對，大型映像與原始碼樹的掃描較快且較省記憶體。

### 8.4 False Positive

| 原因 | 處理方式 |
|------|----------|
| 測試資料中的假金鑰 | `allow-rules` 限定路徑 |
| 文件範例字串 | 使用明顯的佔位符（`<YOUR_API_KEY>`） |
| 高熵但非 Secret 的字串 | 經 Security 確認後以 `.trivyignore.yaml` 依路徑忽略 |

### 8.5 重要安全原則

> **Trivy 找到 Secret 後，不應把 Secret 本身再輸出給 AI Agent、Log 或 Ticket。**

Trivy 報告會以遮罩方式呈現匹配內容，但周邊程式碼行、檔案路徑仍會輸出，報告本身仍屬敏感資料：

| 動作 | 允許 | 禁止 |
|------|------|------|
| 告知 AI Agent | Rule ID、檔案路徑、行號、Severity | 原始值、未遮罩的程式碼行 |
| 寫入 Ticket | Rule ID、檔案路徑、Owner | 原始值、截圖 |
| CI Log | 摘要計數 | 完整 table 輸出（若 Log 對外可見） |
| SARIF 上傳 | 視 Code Scanning 權限控管 | 上傳至公開 repo |

### 8.6 Secret 事件處理流程

```mermaid
flowchart LR
    A["Detect<br/>Trivy Secret Finding"] --> B["Redact<br/>報告與 Log 遮罩"]
    B --> C["Revoke / Rotate<br/>立即撤銷並輪替"]
    C --> D["Investigate<br/>查存取紀錄"]
    D --> E["Prevent Recurrence<br/>Secret Manager、Pre-commit"]
```

| 步驟 | 動作 | 負責 |
|------|------|------|
| Detect | Trivy 偵測 | CI / Developer |
| Redact | 停止擴散：確認報告與 Log 不外流 | DevSecOps |
| Revoke / Rotate | **先撤銷再修程式**：只刪除程式碼中的 Secret 不夠，因為它已在 Git 歷史中 | Secret Owner |
| Investigate | 查詢該憑證在曝光期間的使用紀錄 | Security Team |
| Prevent Recurrence | 改用 Secret Manager、加入 pre-commit 掃描 | Tech Lead |

### 8.7 Git History 與 CI/CD Secret

- **Git History**：官方文件未說明 Trivy 支援逐一掃描完整 commit 歷史。若需歷史掃描，應搭配專門工具；`trivy repo --commit` 只能掃描指定 commit 的狀態。
- **CI/CD Secret**：2026-03 事件的惡意程式就是從 CI Runner 的記憶體與檔案系統竊取 Secret。CI 中的 Trivy 本身也必須以最小權限執行（第 20、30 章）。

### 實務案例

某開發者把含有資料庫密碼的 `application-prod.yml` commit 進 repo，Trivy 在 PR 中偵測到。團隊依 8.6 流程：先由 DBA 輪替密碼，再從程式碼移除並改用 Kubernetes Secret + External Secrets，最後在 pre-commit 加入 `trivy fs --scanners secret`。事後查證該密碼在曝光期間未被使用。

### 注意事項

- **永遠先 Revoke / Rotate**，不要只刪除程式碼。
- 不要把 Secret Finding 加入 `.trivyignore` 了事，除非 Security Team 確認是 False Positive。

---

## 9. License Scanner

### 9.1 基本概念

| 名詞 | 說明 |
|------|------|
| Open Source License | 開源授權條款，例如 MIT、Apache-2.0、GPL-3.0 |
| License Compliance | 使用與散布軟體時遵守授權條款 |
| Dependency License | 相依套件的授權 |
| License Risk | 授權條款對商業使用、散布、原始碼公開的影響 |
| UNKNOWN License | 無法辨識或無法解析的授權；v0.75 起無法解析的授權名稱會以 UNKNOWN Severity 報告 |

### 9.2 Trivy 的 License 分類

**【官方】** Trivy 依授權類別給予 Severity：

| 類別 | Severity | 常見範例 |
|------|----------|----------|
| Forbidden | CRITICAL | 依組織政策定義 |
| Restricted | HIGH | GPL 系列（依預設分類） |
| Reciprocal | MEDIUM | MPL、EPL 等 |
| Notice | LOW | Apache-2.0、BSD |
| Permissive | LOW | MIT 等 |
| Unencumbered | LOW | Unlicense、CC0 |
| Unknown | UNKNOWN | 無法辨識 |

分類可在 `trivy.yaml` 中依企業政策自訂：

```yaml
license:
  forbidden:
    - AGPL-3.0
  restricted:
    - GPL-2.0
    - GPL-3.0
  reciprocal:
    - MPL-2.0
    - EPL-2.0
  notice:
    - Apache-2.0
    - BSD-3-Clause
  permissive:
    - MIT
```

### 9.3 範例

```bash
# 容器映像檔
trivy image --scanners license --severity HIGH,CRITICAL registry.example.com/app:1.4.2

# 原始碼，並深入檢查原始碼標頭與 LICENSE 檔
trivy fs --scanners license --license-full .

# 以 SBOM 掃 License
trivy sbom --scanners license app.cdx.json
```

Java 專案在 v0.72–v0.74 間強化了 JAR 授權偵測（內嵌 `pom.xml`、`LICENSE` 檔、`Bundle-License`、pom `<url>` 轉 SPDX ID），v0.73 起可讀取 Jenkins plugin manifest 的授權；Node.js 自 v0.69 起可從 `package-lock.json` 解析授權。v0.75 起 `license.id` 使用標準 SPDX 大小寫，修正 CycloneDX 輸出無法通過 schema 驗證的問題。

### 9.4 License 的治理原則

> **License 掃描結果需要配合公司法務 / Open Source Governance Policy，而不是由 AI Agent 自行判定法律結論。**

| 誰 | 做什麼 |
|----|--------|
| Trivy | 偵測授權名稱、分類、Severity |
| AI Agent | 彙整清單、標示「需法務檢視」項目、**不下結論** |
| Developer | 提供使用方式（是否修改、是否散布、是否 SaaS） |
| 法務 / OSPO | 判定是否可用、是否需揭露原始碼、是否需標示 |

### 實務案例

某 AI Agent 在升級前端套件時發現新增一個 AGPL-3.0 的間接相依，它直接在 PR 描述寫「AGPL 可用於內部系統，無風險」。法務檢視後指出該系統會以 SaaS 形式對外提供，AGPL 條款可能適用。之後團隊在 AGENTS.md 加入「License 結論必須由法務提供」規則（附錄 F）。

### 注意事項

- License 掃描**預設不啟用**，必須明確指定 `--scanners license`。
- OS 套件的授權資訊可能不完整；`--license-full` 會增加掃描時間。

---

## 10. Kubernetes Security

> **【官方·Experimental】** `trivy kubernetes`（別名 `trivy k8s`）在官方 CLI 說明中標示為 **[EXPERIMENTAL] Scan kubernetes cluster**，功能與輸出可能不相容變更。

### 10.1 掃描範圍

官方將 Kubernetes 掃描分為三類：

| 類別 | 範例 | 掃描內容 |
|------|------|----------|
| Cluster infrastructure | api-server、kubelet、addons | Vulnerability、Node 設定（node-collector） |
| Cluster configuration | Role、ClusterRole | RBAC、Misconfiguration |
| Application workloads | Deployment、Pod、Service、ConfigMap、Secret | Image 弱點、Secret、Misconfiguration |

| 資源 / 元件 | Trivy 檢查 |
|-------------|-----------|
| Workload / Pod / Deployment | Security Context、資源限制、特權 |
| Service | 暴露方式 |
| ConfigMap / Secret | 明文敏感資訊 |
| RBAC | 過寬權限（`rbac` scanner） |
| Image | 映像檔中的 Vulnerability、Secret |
| Security Context | runAsNonRoot、capabilities、readOnlyRootFilesystem |

### 10.2 基本指令

```bash
# 使用 kubeconfig 的目前 context，輸出摘要
trivy k8s --report summary

# 指定 context
trivy k8s kind-kind --report summary

# 指定 namespace
trivy k8s --include-namespaces order,payment --report summary

# 只看 CRITICAL 的完整報告
trivy k8s --severity CRITICAL --report all

# 只看 misconfig 或只看 secret
trivy k8s --scanners misconfig --report summary
trivy k8s --scanners secret --report summary

# 不下載與掃描映像檔（加快速度，但不會有 Image 弱點）
trivy k8s --report summary --skip-images

# 輸出 JSON
trivy k8s --format json --output k8s-result.json
```

| Flag | 說明 |
|------|------|
| `--report summary` / `all` | 摘要或完整；CLI 說明預設為 `all` |
| `--scanners` | `vuln,misconfig,secret,rbac`（預設全部） |
| `--format` | `table`、`json`、`cyclonedx`（KBOM） |
| `--include-namespaces` / `--exclude-namespaces` | 不可同時使用；exclude 需 ClusterRole |
| `--include-kinds` / `--exclude-kinds` | 不可同時使用 |
| `--skip-images` | 不掃 Workload 映像檔 |
| `--disable-node-collector` | 不執行 node-collector Job |
| `--exclude-owned` | 排除有 ownerReference 的資源（例如由 Deployment 產生的 ReplicaSet / Pod） |
| `--k8s-version` | 指定版本以檢查過時 API |

### 10.3 必要權限

**【官方】** 掃描帳號至少需要以下 API group 的 `list` 權限：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: trivy-scanner-readonly
rules:
  - apiGroups: [""]
    resources: ["*"]
    verbs: ["list"]
  - apiGroups: ["apps", "batch", "networking.k8s.io", "rbac.authorization.k8s.io"]
    resources: ["*"]
    verbs: ["list"]
```

若啟用 node-collector（預設啟用），還需要建立 / 刪除 Job、建立 namespace、讀取 `nodes/proxy`、`pods/log` 等權限，詳見官方文件。

> **【企業建議】** 掃描用帳號應為**專用 ServiceAccount**，權限以上述最小集合為主。若組織政策不允許掃描工具在 Production 建立 Job，請使用 `--disable-node-collector`。

### 10.4 Compliance

```bash
trivy k8s --compliance k8s-pss-baseline-0.1 --report summary
trivy k8s --compliance k8s-cis-1.23 --report all --format json --output cis.json
```

**【官方】** 內建 Kubernetes compliance：

| ID | 標準 |
|----|------|
| `k8s-nsa-1.0` | NSA、CISA Kubernetes Hardening Guidance v1.0 |
| `k8s-cis-1.23` | CIS Benchmark for Kubernetes v1.23 |
| `eks-cis-1.4` | CIS Benchmark for EKS v1.4 |
| `rke2-cis-1.24` | CIS Benchmark for RKE2 v1.24 |
| `k8s-pss-baseline-0.1` | Pod Security Standards Baseline |
| `k8s-pss-restricted-0.1` | Pod Security Standards Restricted |

### 10.5 KBOM

```bash
trivy k8s --format cyclonedx --output kbom.cdx.json
trivy sbom kbom.cdx.json
```

### 10.6 架構

```mermaid
flowchart TB
    D["Developer"] --> I["Container Image"]
    I --> R["Registry"]
    R --> K["Kubernetes"]
    K --> T["Trivy<br/>trivy k8s / Operator"]
    T --> F["Security Findings"]
    F --> A["AI Agent<br/>分析與分類"]
    A --> M["Remediation<br/>PR：修 YAML / 升 Base Image"]
    M --> D
```

### 實務案例

某團隊在 OpenShift 測試叢集執行 `trivy k8s --report summary`，發現 60% 的 Deployment 未設資源限制、12 個 ServiceAccount 綁定 `cluster-admin`。由於掃描不改變叢集狀態，團隊將其排入每週例行檢查，並把修正納入 Helm Chart 的 CI `trivy config` 檢查，避免問題再進入叢集。

### 注意事項

- `trivy convert` **不支援** `trivy k8s` 的 JSON 報告（官方 Reporting 文件明確說明）。
- k8s 掃描結果會含 Secret Finding，輸出檔應視為敏感資料。
- 大型叢集請使用 `--include-namespaces` 分批掃描，並調整 `--qps` / `--burst` 避免壓垮 API Server。

---

## 11. Trivy Operator

### 11.1 概念

Trivy Operator 以 **Kubernetes Operator Pattern** 運作：監看叢集狀態變化（例如新 Pod 建立），自動觸發掃描，並把結果存成 Kubernetes **CRD（Custom Resource Definition）** 報告，可透過 `kubectl` 或 Kubernetes API 存取。

> **【官方】** 專案 README 說明：雖盡量維持相容，但專案仍處於 incubating，部分 API 與 CRD 可能變更。

### 11.2 報告類型

| 報告 | 說明 | 查詢方式 |
|------|------|----------|
| Vulnerability Reports | Workload 映像檔弱點 | `kubectl get vulnerabilityreports -A -o wide` |
| ConfigAudit Reports | Kubernetes 資源設定稽核 | `kubectl get configauditreports -A -o wide` |
| Exposed Secret Reports | 映像檔中暴露的 Secret | `kubectl get exposedsecretreports -A` |
| RBAC Assessment Reports | 角色權限評估 | `kubectl get rbacassessmentreports -A` |
| Infra Assessment Reports | 核心元件設定評估 | `kubectl get infraassessmentreports -A` |
| Cluster Compliance Reports | NSA、CIS、PSS 合規報告 | `kubectl get clustercompliancereports` |
| SBOM Reports | Workload SBOM | `kubectl get sbomreports -A` |

另外 ConfigAudit 會檢查資源是否使用即將移除的過時 API。

### 11.3 安裝

```bash
# 方式一：Helm repository
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update
helm install trivy-operator aqua/trivy-operator \
  --namespace trivy-system --create-namespace \
  --version 0.36.0

# 方式二：OCI registry（Helm 3.8+）
helm install trivy-operator oci://ghcr.io/aquasecurity/helm-charts/trivy-operator \
  --namespace trivy-system --create-namespace \
  --version 0.36.0
```

企業 values 範例（鍵名以該版 Chart 的 `values.yaml` 為準，安裝前請以 `helm show values` 核對）：

```yaml
# values-enterprise.yaml
trivy:
  ignoreUnfixed: true
  severity: "HIGH,CRITICAL"
operator:
  scanJobsConcurrentLimit: 3
```

```bash
helm show values aqua/trivy-operator --version 0.36.0 > default-values.yaml
helm upgrade --install trivy-operator aqua/trivy-operator \
  -n trivy-system --version 0.36.0 -f values-enterprise.yaml
```

### 11.4 Trivy CLI vs Trivy Operator

| 能力 | Trivy CLI | Trivy Operator |
|------|-----------|----------------|
| Local Scan | ✓ 核心用途 | ✗ |
| CI/CD | ✓ 核心用途 | ✗（非設計目的） |
| Kubernetes | ✓ `trivy k8s`（Experimental，一次性掃描） | ✓ 叢集內常駐 |
| Continuous Monitoring | 需自行排程 | ✓ 事件驅動自動掃描 |
| Report Resource | 檔案（JSON、SARIF…） | Kubernetes CRD |
| Cluster Governance | 間接 | ✓ Compliance Report、RBAC Assessment |
| 部署前阻擋 | ✓ CI Gate | 需搭配 Admission Controller（例如 Kyverno） |
| 資源消耗 | 執行時 | 常駐 Operator 與 Scan Job |

```mermaid
flowchart LR
    subgraph Shift-Left
        C1["Developer 本機<br/>trivy fs"] --> C2["CI/CD<br/>trivy image / config"]
    end
    subgraph Runtime
        O1["Trivy Operator"] --> O2["CRD Reports"]
        O2 --> O3["Prometheus / SIEM / Dashboard"]
    end
    C2 -->|"部署"| O1
```

### 實務案例

某團隊在 CI 中已經 Gate 掉 CRITICAL，但上線三個月後，同一映像檔被揭露了新的 CRITICAL。Trivy Operator 在 DB 更新後自動重新產生 VulnerabilityReport，團隊的告警規則因此發出通知。CI 管的是「進來時乾淨」，Operator 管的是「跑著時仍然乾淨」。

### 注意事項

- Operator 的 Scan Job 會消耗叢集資源，大型叢集需限制併發數。
- Operator 內建的 Trivy 版本通常落後 CLI（v0.34.0 內建 0.74.0），同一映像在 CI 與叢集的結果可能略有差異；稽核時應記錄兩邊的 Trivy 與 DB 版本。
- 離線環境需設定 Operator 使用的 DB repository 指向內部 Mirror（第 17 章）。
- 報告 CRD 會增加 etcd 資料量，需規劃保留與清理。

---

## 12. Cloud Security

### 12.1 先講清楚：Trivy 目前的 Cloud 能力

> **【官方】** v0.53.0 起 `trivy aws` 子命令**已從 Trivy 核心移除**，改由獨立的 **trivy-aws plugin** 提供。v0.75.0 的官方 Target 文件中**沒有** Cloud 帳號作為 Target。

| 能力 | 提供方式 | 狀態 |
|------|----------|------|
| AWS 帳號設定掃描 | trivy-aws plugin（`trivy aws`） | Plugin；最新 v0.15.1 約為兩年前發布 |
| AWS AMI / EBS Snapshot | `trivy vm ami:` / `ebs:` | Experimental |
| 雲端 IaC 設定檢查 | `trivy config`（Terraform、CloudFormation、Azure ARM） | Stable |
| 私有 Registry（ECR、ACR、GAR） | `trivy image` 認證整合 | Stable |
| Azure / GCP 帳號即時掃描 | — | 官方資料未說明開源版支援 |
| 完整 CSPM | — | **不是** Trivy 開源版的定位 |

> v0.68 CHANGELOG 有「cli: Add trivy cloud support」項目，但官方開源文件未提供對應的 Cloud 帳號掃描 Target 說明，本手冊不將其視為開源 Cloud 掃描能力。

### 12.2 trivy-aws plugin

```bash
trivy plugin install github.com/aquasecurity/trivy-aws

# 使用與 AWS CLI 相同的認證機制（環境變數、profile、IAM Role）
trivy aws --region ap-northeast-1
trivy aws --region ap-northeast-1 --service s3
trivy aws --region ap-northeast-1 --service s3 --service ec2
trivy aws --region ap-northeast-1 --update-cache
```

plugin README 列出的服務包括：accessanalyzer、api-gateway、athena、cloudfront、cloudtrail、cloudwatch、codebuild、documentdb、dynamodb、ec2、ecr、ecs、efs、eks、elasticache、elasticsearch、elb、emr、iam、kinesis、kms、lambda、mq、msk、neptune、rds、redshift、s3、sns、sqs、ssm、workspaces。

> **【企業建議】** 由於 plugin 發布頻率低，正式導入前請：(1) 在非 Production 帳號驗證；(2) 以唯讀 IAM Role 執行；(3) 評估是否以專門的 CSPM 工具作為主要 Cloud 控制，Trivy 作為 IaC 左移檢查。

### 12.3 以 IaC 左移取代事後掃描

對大多數企業，更穩定的做法是**在 Terraform / CloudFormation 進入雲端之前就擋下錯誤設定**：

```bash
# Terraform 原始碼
trivy config ./terraform

# Terraform plan JSON（反映實際變數與模組展開）
terraform plan -out tfplan
terraform show -json tfplan > tfplan.json
trivy config tfplan.json
```

| 檢查類型 | 範例 |
|----------|------|
| IAM | 過寬 Policy、`*` Action |
| S3 / Storage | 公開存取、未加密、未啟用日誌 |
| EC2 / Network | Security Group 開放 `0.0.0.0/0` |
| RDS | 公開存取、未加密、無備份 |
| Encryption | KMS 設定 |

### 實務案例

某團隊原打算用 `trivy aws` 作為 Cloud 唯一控制，評估後發現 plugin 更新頻率不符合金融業對工具維護性的要求。最後的架構是：Terraform PR 用 `trivy config` 擋錯誤設定（左移），帳號層級的持續監控交由雲端原生安全服務，兩者結果彙整至 SIEM。

### 注意事項

- 不要在對外文件宣稱「Trivy 已完整支援所有 Cloud Provider」。
- Cloud 掃描所需的認證資訊必須使用短期憑證（IAM Role / OIDC），不得把 Access Key 寫入 CI 設定。

---

## 13. Trivy 系統架構

### 13.1 完整架構

```mermaid
flowchart TB
    U["Developer / AI Agent"] --> CLI["Trivy CLI"]
    CLI --> CFG["Configuration<br/>CLI flags、TRIVY_* env、trivy.yaml"]
    CLI --> TS["Target Scanner<br/>Artifact Analyzer"]
    TS --> V["Vuln"]
    TS --> M["Misconf"]
    TS --> S["Secret"]
    TS --> L["License"]
    TS --> SB["SBOM"]
    V --> DB["Vulnerability DB<br/>trivy-db / trivy-java-db"]
    M --> CK["Checks Bundle<br/>trivy-checks"]
    DB --> P["Policy / Rules<br/>severity、ignore、VEX、Rego"]
    CK --> P
    S --> P
    L --> P
    SB --> REP["Reports"]
    P --> REP
    REP --> CI["CI/CD Gate"]
    REP --> SIEM["SIEM / Dashboard"]
    REP --> AI["AI Agent"]
    CACHE[("Cache<br/>fs / memory / redis")] -.-> TS
    CACHE -.-> DB
```

### 13.2 元件說明

| 元件 | 說明 | 預設位置 / 來源 |
|------|------|-----------------|
| Trivy CLI | 單一執行檔，含所有 Target 與 Scanner | GitHub Release、套件庫、容器映像 |
| Configuration | 三層設定來源，優先序見第 15 章 | `trivy.yaml` |
| Artifact Analyzer | 解析 OS、lock file、jar、設定檔 | 內建 |
| trivy-db | 弱點資料庫（OCI artifact） | `mirror.gcr.io/aquasec/trivy-db:2`，後援 `ghcr.io/aquasecurity/trivy-db:2` |
| trivy-java-db | Java 套件索引（jar SHA1 → GAV） | `mirror.gcr.io/aquasec/trivy-java-db:1`，後援 `ghcr.io/aquasecurity/trivy-java-db:1` |
| trivy-checks | Misconfiguration 規則 bundle | `mirror.gcr.io/aquasec/trivy-checks:2` |
| Cache | 映像層分析結果、DB | Linux 預設 `~/.cache/trivy`；`--cache-backend` 支援 `fs`、`memory`、`redis`（Experimental） |
| VEX | 抑制不可利用的弱點 | 本機檔、VEX Repository、OCI |
| Plugin / Module | 擴充子命令與 WASM 模組 | `trivy plugin`、`trivy module` |
| Server | Client/Server 模式集中 DB | `trivy server` |

### 13.3 Client / Server 模式

```bash
# Server（集中持有 DB）
trivy server --listen 0.0.0.0:4954 --token-header Trivy-Token --token "$TRIVY_SERVER_TOKEN"

# Client
trivy image --server http://trivy.internal:4954 --token "$TRIVY_SERVER_TOKEN" registry.example.com/app:1.4.2
```

> **【企業建議】** Server 模式下 Token 必須來自 Secret Manager，Server 應僅開放內網，並以 TLS 反向代理保護。

在 Kubernetes 中部署 Server 可使用官方 repo 內的 `helm/trivy` Chart（Chart 0.27.0 內建 Trivy 0.75.0）。Chart values 鍵名請以 `helm show values` 核對；Client 端的 Trivy 版本應與 Server 一致。

### 實務案例

某企業有 200 個 CI Runner，每個 Runner 每天下載 DB 造成大量對外流量。改為內部 DB Mirror + 部分團隊使用 Client/Server 模式後，對外流量大幅下降，DB 版本也更一致。

### 注意事項

- Client/Server 模式下，Client 與 Server 的 Trivy 版本應一致，避免協定或欄位差異（v0.70 起 JSON 輸出包含 Server 版本資訊）。
- Cache 目錄可能含映像層分析結果，請設定適當權限。

---

## 14. Trivy 安裝

### 14.1 先讀這一段：2026-03 供應鏈事件

> **【官方】GHSA-69fq-xp46-6x23 / CVE-2026-33634（Critical）**
>
> - 2026-03-19：攻擊者以遭竊憑證發布惡意 **Trivy v0.69.4**（GitHub Release、deb、rpm、GHCR、ECR Public、Docker Hub、`get.trivy.dev` 皆受影響，曝露約 3 小時）。
> - 同日：`aquasecurity/trivy-action` 77 個 tag 中有 76 個被 force-push 成竊取憑證的惡意程式（約 12 小時）；`aquasecurity/setup-trivy` 全部 7 個 tag 被替換（約 4 小時）。
> - 2026-03-22：攻擊者另以 Docker Hub 憑證推送惡意 `aquasec/trivy:0.69.5`、`0.69.6`（約 10 小時）。
> - **未受影響**：以 digest 引用的映像、從原始碼建置、Homebrew 官方 formula（從原始碼建置）、v0.69.3 以前版本（v0.69.3 受 Immutable Release 保護）。

**這件事告訴我們：連安全掃描工具本身都是供應鏈的一部分。** 本章所有安裝方式都附帶驗證步驟。

### 14.2 安裝方式總覽

**【官方】** 官方文件把安裝方式分為 Official 與 Community：

| 方式 | 類型 | 平台 |
|------|------|------|
| 容器映像 | Official | `docker.io/aquasec/trivy`、`ghcr.io/aquasecurity/trivy`、`public.ecr.aws/aquasecurity/trivy` |
| GitHub Release 執行檔 | Official | Linux、macOS、Windows、FreeBSD |
| Install Script | Official | Linux / macOS |
| RHEL / CentOS RPM repo | Official | Linux |
| Debian / Ubuntu DEB repo | Official | Linux |
| Homebrew | Official | macOS / Linux |
| FreeBSD pkg | Official | FreeBSD |
| Arch、OpenSUSE、MacPorts、Nix、asdf / mise | Community | 各平台 |

> 官方安裝文件未將 winget、Scoop、Chocolatey 列為 Official 或 Community 安裝方式。企業 Windows 環境建議採用 **GitHub Release zip + 簽章驗證 + 內部軟體派送**。

### 14.3 Windows

#### Step 1：下載

自 GitHub Release `v0.75.0` 下載 Windows 64-bit zip 與對應的 `.sigstore.json`（檔名以 Release 頁面為準，官方文件格式為 `trivy_x.xx.x_windows-64bit.zip`）以及 `trivy_0.75.0_checksums.txt`。

#### Step 2：驗證雜湊（PowerShell）

```powershell
$zip = "trivy_0.75.0_windows-64bit.zip"
$expected = (Select-String -Path .\trivy_0.75.0_checksums.txt -Pattern $zip).Line.Split(" ")[0]
$actual = (Get-FileHash -Algorithm SHA256 .\$zip).Hash.ToLower()
if ($expected -ne $actual) { throw "Checksum mismatch: $zip" } else { "Checksum OK" }
```

#### Step 3：驗證簽章（需安裝 cosign）

```powershell
cosign verify-blob `
  --certificate-identity-regexp 'https://github\.com/aquasecurity/' `
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' `
  --bundle .\trivy_0.75.0_windows-64bit.zip.sigstore.json `
  .\trivy_0.75.0_windows-64bit.zip
```

#### Step 4：解壓縮並加入 PATH

```powershell
$dest = "C:\Tools\trivy\0.75.0"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Expand-Archive -Path .\trivy_0.75.0_windows-64bit.zip -DestinationPath $dest -Force

# 使用者層級 PATH（企業環境建議由端點管理工具統一派送）
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$dest*") {
  [Environment]::SetEnvironmentVariable("Path", "$userPath;$dest", "User")
}
```

#### Step 5：版本確認（重新開啟 PowerShell）

```powershell
trivy --version
```

> Windows 上掃描容器映像需要 Docker Desktop 或可連線的 Registry；`trivy fs`、`trivy config`、`trivy sbom` 不需要 Docker。

### 14.4 Linux

**Debian / Ubuntu（官方 repo）**：

```bash
sudo apt-get install -y wget gnupg
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install -y trivy=0.75.0
```

**RHEL / Rocky / Alma（官方 repo）**：

```bash
cat << 'EOF' | sudo tee /etc/yum.repos.d/trivy.repo
[trivy]
name=Trivy repository
baseurl=https://aquasecurity.github.io/trivy-repo/rpm/releases/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://aquasecurity.github.io/trivy-repo/rpm/public.key
EOF
sudo yum -y install trivy-0.75.0
```

**Release 執行檔 + 簽章驗證（建議用於 CI 映像與離線環境）**：

```bash
VERSION=0.75.0
FILE="trivy_${VERSION}_Linux-64bit.tar.gz"
BASE="https://github.com/aquasecurity/trivy/releases/download/v${VERSION}"
curl -sSLO "${BASE}/${FILE}"
curl -sSLO "${BASE}/${FILE}.sigstore.json"

cosign verify-blob \
  --certificate-identity-regexp 'https://github\.com/aquasecurity/' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  --bundle "${FILE}.sigstore.json" \
  "${FILE}"

tar -xzf "${FILE}" trivy
sudo install -m 0755 trivy /usr/local/bin/trivy
trivy --version
```

> **【企業建議】** 官方的 Install Script 方式（`curl ... install.sh | sh`）很方便，但它從 `main` 分支取得腳本。企業 CI 映像建議改用「固定版本 Release + cosign 驗證」並建置成內部 Base Image。

### 14.5 macOS

```bash
# Homebrew 官方 formula（從原始碼建置，2026-03 事件中未受影響）
brew install trivy
trivy --version
```

### 14.6 Docker / Container

```bash
# 固定版本，並建議以 digest 引用
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$HOME/.cache/trivy:/root/.cache/" \
  aquasec/trivy:0.75.0 image registry.example.com/app:1.4.2
```

驗證容器映像簽章：

```bash
cosign verify \
  --certificate-identity-regexp 'https://github\.com/aquasecurity/' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  ghcr.io/aquasecurity/trivy:0.75.0
```

> 掛載 Docker socket 等同給予容器主機的 Docker 控制權，只應在受控的 CI Runner 使用。

### 14.7 CI/CD Runner

| 方式 | 建議 |
|------|------|
| GitHub Actions | 使用 `aquasecurity/setup-trivy`（範例 v0.3.1；安全下限 ≥ v0.2.6；避開 v0.3.0）或 `trivy-action`（≥ v0.35.0，並明確指定 `version`），**以完整 commit SHA 固定**（第 20 章） |
| GitLab / Jenkins / Azure DevOps | 使用企業內部建置、已驗證簽章的 Trivy Runner 映像 |
| 自架 Runner | 將 Trivy 預裝於 Runner 映像，版本由 Platform Team 管理 |

### 14.8 Kubernetes

| 方式 | 用途 |
|------|------|
| Trivy Operator（Helm） | 叢集內持續掃描（第 11 章） |
| `trivy server` 部署於內部 | Client/Server 模式的集中 DB |
| CronJob 執行 `trivy` | 定期掃描 SBOM 或映像清單 |

### 14.9 版本驗證

```bash
trivy --version
```

輸出會包含 Trivy 版本，以及本機 Vulnerability DB、Java DB、Check Bundle 的版本與更新時間（若已下載）。

> **【企業建議】** CI 的第一個 Trivy step 一律執行 `trivy --version` 並保存輸出，作為稽核證據：「這次掃描用的是哪一版 Trivy、哪一天的 DB」。

### 14.10 開發者工具：VS Code Extension 與 MCP Plugin

| 工具 | 識別 | 用途 | 說明 |
|------|------|------|------|
| Aqua Trivy VS Code Extension | Marketplace ID `AquaSecurityOfficial.trivy-vulnerability-scanner`（最新 1.8.11） | 在編輯器內掃描工作區並以樹狀檢視呈現 Finding | 呼叫本機 Trivy 執行檔；應指向企業核准版本 |
| trivy-mcp plugin | `trivy plugin install mcp@v0.0.20` | 讓 IDE AI Agent 以 MCP 工具呼叫 Trivy | 詳見第 26.4–26.6 節與第 30.4 節 |

> **【企業建議】** Extension 與 plugin 皆屬第三方元件，應納入 IDE 擴充套件允許清單。兩者都不具備 Gate 效力，只提供開發階段回饋。

### 實務案例

2026-03-19 事件當晚，某企業 Platform Team 依「所有 Trivy 安裝都要驗章」的規範，CI Runner 映像的 Trivy 是 3 月初已驗章的 v0.69.2，未受影響；但有兩個團隊直接用 `trivy-action@0.34.0`（mutable tag），事後需輪替這兩個 repo 可存取的所有 Secret。

### 注意事項

- **不要**在 CI 使用 `version: latest`。
- **不要**以 mutable tag 引用 GitHub Action。
- 安裝來源、版本、驗章結果應記錄於變更單。

---

## 15. Trivy Configuration

### 15.1 三種設定來源與優先順序

**【官方】** 優先順序由高到低：

| 優先 | 來源 | 範例 |
|------|------|------|
| 1 | CLI flags | `--severity HIGH,CRITICAL` |
| 2 | 環境變數 | `TRIVY_SEVERITY=HIGH,CRITICAL` |
| 3 | 設定檔 | `trivy.yaml` 中的 `severity` |
| 4 | 預設值 | 內建預設 |

環境變數命名規則：`TRIVY_` + flag 名稱大寫、`-` 改為 `_`。例如 `--skip-db-update` → `TRIVY_SKIP_DB_UPDATE`。

> trivy-action 的優先順序為：Action inputs > 環境變數 > trivy.yaml > 預設值。

### 15.2 產生預設設定檔

v0.69 起官方提供 trivy.yaml 的 JSON Schema。最可靠的作法是讓 Trivy 自己產生完整預設設定，再刪減：

```bash
trivy image --generate-default-config
# 產生 trivy-default.yaml，所有鍵名以此檔為準
```

### 15.3 常用設定項目

| 設定 | CLI flag | 說明 |
|------|----------|------|
| severity | `--severity` | 顯示的嚴重度 |
| scanners | `--scanners` | 啟用的 Scanner |
| ignorefile | `--ignorefile` | Ignore 檔路徑；空字串停用 |
| exit-code | `--exit-code` | 有 Finding 時的結束碼 |
| skip-dirs / skip-files | `--skip-dirs` / `--skip-files` | 支援 glob |
| cache | `--cache-dir`、`--cache-backend` | 快取位置 |
| timeout | `--timeout` | 預設 5m0s |
| output / format | `--output` / `--format` | 報告輸出 |
| DB update | `--skip-db-update`、`--db-repository` | 弱點 DB |
| Java DB | `--skip-java-db-update`、`--java-db-repository` | Java 索引 DB |
| policy | `--config-check`、`--ignore-policy` | 自訂 Rego |
| VEX | `--vex` | Experimental |
| 企業 CA | `--cacert` | v0.68 新增 |

### 15.4 企業建議設定範例

> 以下鍵名請以 `trivy-default.yaml` 核對；不同版本可能有差異。

```yaml
# trivy.yaml —— 企業 CI 共用設定（由 DevSecOps 維護，Repo 不得自行修改）
timeout: 15m
severity:
  - HIGH
  - CRITICAL
exit-code: 1
format: json

cache:
  dir: /var/cache/trivy

db:
  repository:
    - registry.internal.example.com/mirror/aquasec/trivy-db:2
  java-repository:
    - registry.internal.example.com/mirror/aquasec/trivy-java-db:1

scan:
  scanners:
    - vuln
    - secret
    - misconfig
  skip-dirs:
    - "**/node_modules"
    - "**/src/test/resources/fixtures"

vulnerability:
  ignore-unfixed: false

ignorefile: .trivyignore.yaml

secret:
  config: /etc/trivy/trivy-secret.yaml

license:
  forbidden:
    - AGPL-3.0
  restricted:
    - GPL-2.0
    - GPL-3.0
```

### 15.5 CI 中避免被 Repo 內設定檔左右

v0.75 起，空字串可停用設定檔載入：

```bash
trivy fs --config="" --ignorefile="" --secret-config="" /workspace/project
```

| 情境 | 建議 |
|------|------|
| 一般團隊 CI | 使用中央管理的 `--config /etc/trivy/trivy.yaml`，ignore 檔由 repo 提供但需 Review |
| 高風險 / 外部貢獻 PR | 停用 repo 內設定檔，避免 PR 透過修改 `trivy.yaml` 或 `trivy-secret.yaml` 繞過掃描 |
| Release Gate | 一律使用中央設定 |

### 實務案例

某 AI Agent 為了讓 PR 通過，在 repo 的 `trivy.yaml` 加入 `severity: [LOW]`，導致 CI 只顯示 LOW。團隊之後改為 CI 以 `--config /etc/trivy/enterprise.yaml` 指定中央設定，並在 CODEOWNERS 把 `trivy.yaml`、`.trivyignore*`、`trivy-secret.yaml` 指派給 DevSecOps。

### 注意事項

- 不同 Trivy 版本的設定鍵可能變動，升級時用 `--generate-default-config` 比對。
- 環境變數優先於設定檔，CI 中殘留的 `TRIVY_*` 變數可能造成意外行為。

---

## 16. .trivyignore

### 16.1 Why：為什麼需要 Ignore

| 情境 | 是否適合 Ignore |
|------|-----------------|
| 經確認的 False Positive | 適合，需有證據 |
| 無修補版本、已有補償控制 | 適合，需有到期日 |
| 弱點程式碼路徑在本產品中不可達 | 優先使用 VEX；或 Ignore 並說明 |
| 「修起來很麻煩」 | **不適合** |
| 「讓 Pipeline 先過」 | **不適合** |

### 16.2 兩種格式

**【官方】純文字 `.trivyignore`**（預設讀取）：

```text
# Accept the risk until 2026-12-31 — SEC-EXC-2026-014, owner: team-order
CVE-2025-12345 exp:2026-12-31

# False positive confirmed by security — SEC-FP-2026-003
AVD-DS-0026

# 測試資料中的假金鑰
generic-unwanted-rule
```

**【官方·Experimental】YAML `.trivyignore.yaml`**（需以 `--ignorefile` 明確指定）：

```yaml
vulnerabilities:
  - id: CVE-2025-12345
    paths:
      - "app/target/order-api.jar"
    expired_at: 2026-12-31
    statement: "SEC-EXC-2026-014 | owner=team-order | 無修補版本，已以 WAF 規則阻擋攻擊向量"
  - id: CVE-2025-23456
    purls:
      - "pkg:maven/org.example/legacy-lib@1.2.3"
    expired_at: 2026-11-30
    statement: "SEC-EXC-2026-020 | owner=team-batch | 升級排入 2026Q4"

misconfigurations:
  - id: AVD-DS-0002
    paths:
      - "docker/legacy-batch/Dockerfile"
    expired_at: 2026-12-31
    statement: "SEC-EXC-2026-021 | Legacy 程式需 root，已排入改寫"

secrets:
  - id: generic-unwanted-rule
    paths:
      - "src/test/resources/fixtures/sample.env"
    statement: "SEC-FP-2026-003 | 測試假資料"

licenses:
  - id: GPL-3.0
    paths:
      - "tools/dev-only/script.py"
    statement: "LEGAL-2026-007 | 僅開發工具，不隨產品散布"
```

```bash
trivy image --ignorefile ./.trivyignore.yaml --show-suppressed registry.example.com/app:1.4.2
```

| 欄位 | 必填 | 說明 |
|------|------|------|
| `id` | ✓ | CVE、check ID、secret rule ID、License 名稱 |
| `paths` | | 限定檔案路徑，未設則全域生效 |
| `purls` | | 限定套件（僅 vulnerabilities） |
| `expired_at` | | 到期日，到期後自動失效 |
| `statement` | | 理由（不參與過濾，但可用於治理） |

### 16.3 治理要求

以下為 **【企業建議 / Security Policy 範本】**：

| 規則 | 說明 |
|------|------|
| 必須有到期日 | 純文字檔用 `exp:`，YAML 用 `expired_at` |
| 必須有 Exception ID | 寫在註解或 `statement` |
| 必須有 Owner | 寫在 `statement` |
| 必須限定範圍 | 盡量使用 `paths` / `purls`，避免全域忽略 |
| 最長效期 | CRITICAL ≤ 30 天、HIGH ≤ 90 天（範例，依企業政策） |
| Review | ignore 檔由 CODEOWNERS 指定 Security 審核 |
| 禁止 | 永久忽略所有 HIGH / CRITICAL；以萬用方式忽略整類 Finding |

```mermaid
flowchart LR
    F["Finding"] --> R["Risk Assessment"]
    R --> T["Temporary Exception"]
    T --> O["Owner"]
    O --> E["Expiration Date"]
    E --> V["Review"]
    V -->|"到期仍未修"| R
    V -->|"已修正"| X["移除 Ignore"]
```

### 16.4 CI 自動檢查 Ignore 檔

以下 Python 腳本會拒絕缺少到期日、超過最長效期或缺少 Exception ID 的條目（`.trivyignore.yaml`）：

```python
"""檢查 .trivyignore.yaml 是否符合企業治理規則。"""
import sys
from datetime import date, timedelta

import yaml

MAX_DAYS = 90
SECTIONS = ("vulnerabilities", "misconfigurations", "secrets", "licenses")


def main(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    errors = []
    limit = date.today() + timedelta(days=MAX_DAYS)
    for section in SECTIONS:
        for item in data.get(section, []) or []:
            rid = item.get("id", "<no-id>")
            expired = item.get("expired_at")
            statement = str(item.get("statement", ""))
            if expired is None:
                errors.append(f"{section}/{rid}: 缺少 expired_at")
            elif expired > limit:
                errors.append(f"{section}/{rid}: 到期日超過 {MAX_DAYS} 天")
            if "SEC-" not in statement and "LEGAL-" not in statement:
                errors.append(f"{section}/{rid}: statement 缺少 Exception ID")
    for e in errors:
        print(f"[trivyignore] {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ".trivyignore.yaml"))
```

> Secrets 類的 False Positive 若經確認為永久性測試資料，可由 Security Policy 另行規定免到期日；腳本可依需求調整。

### 實務案例

某團隊的 `.trivyignore` 在兩年間累積到 312 條，其中 40% 對應的套件早已升級、條目根本沒用，另有 6 條 CRITICAL 從未被重新評估。導入 YAML 格式 + 到期日 + CI 檢查後，第一次清理移除 190 條，剩餘條目都有 Owner。

### 注意事項

- `.trivyignore.yaml` 目前為 Experimental，必須以 `--ignorefile` 明確指定才會載入。
- v0.57 起，指定的 ignore 檔不存在時 Trivy 會報錯，CI 路徑錯誤會直接失敗。
- AI Agent **不得**新增或延長任何 Ignore 條目（第 29 章）。

---

## 17. Trivy Database / Cache

### 17.1 三種資料來源

| 資料 | 用途 | 預設來源（依序） |
|------|------|------------------|
| Vulnerability DB（trivy-db） | 所有 Vulnerability 比對 | `mirror.gcr.io/aquasec/trivy-db:2` → `ghcr.io/aquasecurity/trivy-db:2` |
| Java DB（trivy-java-db） | 以 jar SHA1 辨識 GAV | `mirror.gcr.io/aquasec/trivy-java-db:1` → `ghcr.io/aquasecurity/trivy-java-db:1` |
| Checks Bundle（trivy-checks） | Misconfiguration 規則 | `mirror.gcr.io/aquasec/trivy-checks:2` |

v0.56 起 `--db-repository`、`--java-db-repository` 可指定多個來源，依優先順序嘗試。

### 17.2 常用指令

```bash
# 只下載 / 更新 DB，不掃描（CI 預熱、排程更新）
trivy image --download-db-only
trivy image --download-java-db-only

# 掃描時不更新 DB（使用既有快取）
trivy image --skip-db-update --skip-java-db-update --skip-check-update registry.example.com/app:1.4.2

# 完全離線：不更新 DB，也不對外查詢相依資訊
trivy fs --skip-db-update --skip-java-db-update --skip-check-update --offline-scan .

# 清理快取（v0.53 新增 clean 子命令）
trivy clean --scan-cache
trivy clean --all
```

### 17.3 Cache

| 項目 | 說明 |
|------|------|
| 預設位置 | Linux `~/.cache/trivy`；可用 `--cache-dir` 或 `TRIVY_CACHE_DIR` 指定 |
| Backend | `fs`（預設）、`memory`、`redis://...`（Experimental） |
| 內容 | DB、Java DB、Checks Bundle、映像層與檔案分析結果 |
| 併發 | v0.68 起支援多個程序併發讀取 DB |

### 17.4 企業環境的五個問題

**1. 如何避免每次 Pipeline 重複下載？**

- GitHub Actions：trivy-action 內建快取（預設開啟），並可用排程 workflow 每日預先更新快取（第 20 章）。
- 自架 Runner：將 `--cache-dir` 指向 Runner 持久磁碟或共用 volume。
- 大型組織：使用 Client/Server 模式或內部 DB Mirror。

**2. 如何降低 CI 時間？**

- DB 預熱 + `--skip-db-update`。
- 限縮 `--scanners` 與 `--skip-dirs`。
- 第 43 章有完整效能調校。

**3. 如何處理無 Internet 環境（Air-Gapped）？**

```bash
# 在可連網的中繼機以 ORAS 下載 DB
oras pull ghcr.io/aquasecurity/trivy-db:2
oras pull ghcr.io/aquasecurity/trivy-java-db:1

# 解壓到離線環境的 cache 目錄
mkdir -p /opt/trivy-cache/db /opt/trivy-cache/java-db
tar -xzf db.tar.gz -C /opt/trivy-cache/db
tar -xzf javadb.tar.gz -C /opt/trivy-cache/java-db

# 離線掃描
trivy image --cache-dir /opt/trivy-cache \
  --skip-db-update --skip-java-db-update --skip-check-update --offline-scan \
  registry.internal.example.com/app:1.4.2
```

> 官方文件「Connectivity and Network considerations」與「Self-Hosting Trivy's Databases」有完整說明。

**4. 如何建立企業內部 Mirror？**

```mermaid
flowchart LR
    U1["mirror.gcr.io / ghcr.io"] -->|"排程同步 oras copy<br/>或 Registry Proxy Cache"| M["企業內部 OCI Registry<br/>Harbor / Artifactory / Nexus"]
    M --> R1["CI Runners<br/>--db-repository 指向內部"]
    M --> R2["Developer 本機"]
    M --> R3["Trivy Operator"]
    M --> R4["Air-Gapped 環境<br/>匯出 / 匯入"]
```

```bash
trivy image \
  --db-repository registry.internal.example.com/mirror/aquasec/trivy-db:2 \
  --java-db-repository registry.internal.example.com/mirror/aquasec/trivy-java-db:1 \
  --checks-bundle-repository registry.internal.example.com/mirror/aquasec/trivy-checks:2 \
  registry.internal.example.com/app:1.4.2
```

**5. 如何監控 DB 更新失敗？**

| 監控項目 | 作法 |
|----------|------|
| DB 年齡 | 解析 `trivy --version` 或 JSON 報告中的 DB UpdatedAt，超過門檻（例如 48 小時）告警 |
| 同步作業 | Mirror 同步 Job 失敗即告警 |
| CI 錯誤 | 收集 `failed to download vulnerability DB` 類錯誤 |

### 17.5 Proxy 與企業 CA

```bash
export HTTPS_PROXY="http://proxy.internal.example.com:8080"
export NO_PROXY="registry.internal.example.com,.internal.example.com"
trivy image --cacert /etc/pki/ca-trust/source/anchors/corp-root-ca.pem registry.example.com/app:1.4.2
```

```powershell
$env:HTTPS_PROXY = "http://proxy.internal.example.com:8080"
trivy image --cacert C:\certs\corp-root-ca.pem registry.example.com/app:1.4.2
```

> 不要用 `--insecure` 解決憑證問題；正確作法是以 `--cacert` 提供企業 CA。

### 實務案例

某銀行的開發網段無法連外。Platform Team 在 DMZ 建立 Harbor，以排程每 6 小時用 `oras copy` 同步三個 DB artifact，並在同步後執行一次 `trivy image --download-db-only` 驗證可用性。所有 Runner 與 Operator 都指向內部 Harbor，對外連線只剩 DMZ 的同步主機。

### 注意事項

- 長期 `--skip-db-update` 而未更新快取，會讓掃描結果過時，造成「掃描通過但其實有新 CVE」。
- Java DB 對 jar 辨識很重要，Java 專案不建議跳過 Java DB。

---

## 18. Report Format

### 18.1 支援格式

**【官方】** `trivy image` 的 `--format` 可用值：

| 格式 | 說明 | Vuln | Misconf | Secret | License |
|------|------|------|---------|--------|---------|
| `table` | 預設，人類閱讀 | ✓ | ✓ | ✓ | ✓ |
| `json` | 完整結構化資料 | ✓ | ✓ | ✓ | ✓ |
| `sarif` | SARIF 2.1.0，可上傳 Code Scanning | ✓ | ✓ | ✓ | ✓ |
| `template` | Go template（含 junit、html、asff 等內建範本） | 依範本 | 依範本 | 依範本 | 依範本 |
| `cyclonedx` | SBOM，可含弱點 | ✓ | — | — | ✓ |
| `spdx` / `spdx-json` | SBOM | — | — | — | ✓ |
| `github` | GitHub dependency snapshot | 套件清單 | — | — | — |
| `cosign-vuln` | Cosign 弱點掃描紀錄（attestation predicate） | ✓ | — | — | — |

`trivy k8s` 的 format 僅支援 `table`、`json`、`cyclonedx`。

### 18.2 依用途分類

| 類別 | 格式 | 消費者 |
|------|------|--------|
| Human Report | `table`、`template`（html） | Developer、Reviewer |
| Machine Report | `json` | AI Agent、腳本、Dashboard |
| Security Platform Report | `sarif`、`template`（asff、junit、gitlab） | GitHub Code Scanning、AWS Security Hub、CI 測試報告 |
| SBOM | `cyclonedx`、`spdx`、`spdx-json`、`github` | 供應鏈治理、客戶、Dependency Graph |
| CI/CD Gate | `--exit-code` 搭配任一格式 | Pipeline |

### 18.3 一次掃描、多種輸出：`trivy convert`

```bash
# 只掃一次
trivy image --format json --output result.json registry.example.com/app:1.4.2

# 轉換為其他格式（可再加過濾條件）
trivy convert --format sarif --output result.sarif result.json
trivy convert --format cyclonedx --output result.cdx.json result.json
trivy convert --format table --severity CRITICAL result.json
```

> `trivy convert` 不支援 `trivy k8s` 的 JSON 報告。

### 18.4 Template

```bash
# 內建範本（容器映像中位於 /contrib；rpm 安裝位於 /usr/local/share/trivy/templates）
trivy image --format template --template "@contrib/html.tpl" -o report.html registry.example.com/app:1.4.2
trivy image --format template --template "@contrib/junit.tpl" -o junit.xml registry.example.com/app:1.4.2
```

| 重點 | 說明 |
|------|------|
| 副檔名 | v0.70 起範本檔必須為 `.tpl` |
| 安全性 | 官方警告：範本可讀取環境變數，**只使用可信任的範本** |
| v0.75 Breaking | 移除 `getHostByName`，使用此函式的自訂範本會解析失敗 |

### 18.5 SARIF 與 GitHub Code Scanning

```bash
trivy fs --scanners vuln,secret,misconfig --format sarif --output trivy.sarif .
```

上傳至 GitHub Code Scanning 後，Finding 會出現在 Security 分頁與 PR 的 annotation。重點：

- 需要 `security-events: write` 權限。
- trivy-action 產生 SARIF 時，預設會輸出所有嚴重度；若要套用 `severity` 過濾，需設 `limit-severities-for-sarif: true`。
- 上傳 step 建議加 `if: always()`，讓 Gate 失敗時仍能上傳結果。
- 私有 repo 使用 Code Scanning 需要對應的 GitHub 授權（GitHub Advanced Security / Code Security）；沒有授權時可改用 Job Summary 呈現。

### 18.6 給 AI Agent 的 JSON 摘要

AI Agent 不需要整份 JSON。用 `jq` 萃取最小必要欄位，可大幅減少 Token 並避免敏感內容外洩：

```bash
trivy fs --scanners vuln --format json --output vuln.json .

jq '[.Results[]? | .Target as $t | .Vulnerabilities[]? |
     {target: $t, id: .VulnerabilityID, pkg: .PkgName,
      installed: .InstalledVersion, fixed: .FixedVersion,
      severity: .Severity, status: .Status}]' vuln.json > vuln-summary.json
```

Secret 只給 Rule ID 與位置：

```bash
jq '[.Results[]? | .Target as $t | .Secrets[]? |
     {target: $t, rule: .RuleID, severity: .Severity,
      start: .StartLine, end: .EndLine}]' secret.json > secret-summary.json
```

### 實務案例

某團隊原本把 `table` 輸出直接貼給 AI Agent 分析，一份映像檔報告就超過 3 萬 Token，而且包含 Secret 的遮罩程式碼行。改為 18.6 的摘要 JSON 後，Token 降到原本的十分之一，AI Agent 的建議也更聚焦。

### 注意事項

- SBOM 格式（cyclonedx、spdx）不是給人看的報告，也不包含 Misconfiguration 與 Secret。
- 報告會被保存為稽核證據，請建立保存期限與存取控制（第 30 章）。

---

## 19. CI/CD 整合

### 19.1 標準 Pipeline

以下為 **【企業建議】** 的標準 Pipeline：

```mermaid
flowchart TB
    A["Commit"] --> B["Build"]
    B --> C["Unit Test"]
    C --> D["SAST<br/>非 Trivy"]
    D --> E["Dependency Scan<br/>trivy fs --scanners vuln"]
    E --> F["Trivy Repo Scan<br/>secret + misconfig"]
    F --> G["Build Image"]
    G --> H["Trivy Image Scan"]
    H --> I["Generate SBOM<br/>CycloneDX"]
    I --> J["IaC Scan<br/>trivy config"]
    J --> K["Kubernetes Scan<br/>Staging 叢集，選用"]
    K --> L{"Security Gate"}
    L -->|"Pass"| M["Deploy"]
    L -->|"Fail"| N["通知 + AI Agent 分析"]
```

| 階段 | 指令 | 失敗條件（範例） |
|------|------|------------------|
| Dependency + Secret + IaC | `trivy fs --scanners vuln,secret,misconfig` | 任何 Secret；CRITICAL fixed vuln |
| Image | `trivy image` | CRITICAL fixed vuln；OS EOL |
| SBOM | `trivy image --format cyclonedx` | 產生失敗 |
| IaC | `trivy config` | HIGH / CRITICAL misconfig |
| Gate | 彙整上述結果 | 依第 38 章 |

### 19.2 官方整合清單

**【官方】** 官方 Tutorials 列出的 CI/CD 整合：GitHub Actions、CircleCI、Travis CI、GitLab CI、Bitbucket Pipelines、AWS CodePipeline、AWS Security Hub、Azure DevOps。Jenkins 未列於官方 Tutorials，以 Shell 步驟呼叫 CLI 即可。

### 19.3 GitLab CI

```yaml
# .gitlab-ci.yml（節錄）
variables:
  TRIVY_VERSION: "0.75.0"
  TRIVY_CACHE_DIR: ".trivycache/"
  TRIVY_NO_PROGRESS: "true"

trivy_container_scan:
  stage: test
  image:
    name: registry.internal.example.com/security/trivy:0.75.0
    entrypoint: [""]
  cache:
    key: trivy-db
    paths:
      - .trivycache/
  script:
    - trivy --version
    - trivy image --download-db-only
    - >
      trivy image --format template --template "@/contrib/gitlab.tpl"
      --output gl-container-scanning-report.json
      "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
    - trivy image --exit-code 1 --severity CRITICAL --ignore-unfixed "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
  artifacts:
    when: always
    reports:
      container_scanning: gl-container-scanning-report.json
```

| 重點 | 說明 |
|------|------|
| `entrypoint: [""]` | 覆寫映像預設 entrypoint，讓 `script` 生效 |
| 兩次掃描 | 第一次產報告（不 fail），第二次作為 Gate |
| `TRIVY_USERNAME` / `TRIVY_PASSWORD` | 私有 Registry 認證請用 GitLab masked + protected 變數 |

### 19.4 Jenkins

```groovy
pipeline {
  agent { label 'linux-docker' }
  environment {
    TRIVY_CACHE_DIR = '/var/cache/trivy'
    TRIVY_NO_PROGRESS = 'true'
  }
  stages {
    stage('Trivy FS') {
      steps {
        sh 'trivy --version'
        sh 'trivy fs --scanners vuln,secret,misconfig --format json --output trivy-fs.json .'
        sh 'trivy convert --format table --severity HIGH,CRITICAL trivy-fs.json'
      }
    }
    stage('Build Image') {
      steps {
        sh 'docker build -t registry.internal.example.com/app:${GIT_COMMIT} .'
      }
    }
    stage('Trivy Image Gate') {
      steps {
        sh '''
          trivy image --format json --output trivy-image.json registry.internal.example.com/app:${GIT_COMMIT}
          trivy image --format cyclonedx --output sbom.cdx.json registry.internal.example.com/app:${GIT_COMMIT}
          CRIT=$(jq '[.Results[]?.Vulnerabilities[]? | select(.Severity=="CRITICAL" and .Status=="fixed")] | length' trivy-image.json)
          echo "CRITICAL (fixed) = ${CRIT}"
          test "${CRIT}" -eq 0
        '''
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'trivy-*.json,sbom.cdx.json', allowEmptyArchive: true
    }
  }
}
```

> **【官方】** `trivy convert` 支援 `--exit-code`、`--severity`、`--ignorefile`、`--ignore-policy`，但**沒有** `--ignore-unfixed`，其 `--scanners` 也只用於摘要表呈現。因此「掃一次、多條件判斷」建議直接以 `jq` 解析 JSON（如上），或以第二次 `trivy image --skip-db-update --ignore-unfixed --exit-code 1` 作為 Gate。

### 19.5 Azure DevOps

官方 Ecosystem 列有 Azure DevOps 整合。以 Script 方式呼叫 CLI 的範例：

```yaml
# azure-pipelines.yml（節錄）
steps:
  - script: |
      trivy --version
      trivy fs --scanners vuln,secret,misconfig --format sarif --output $(Build.ArtifactStagingDirectory)/trivy.sarif .
      trivy image --exit-code 1 --severity CRITICAL --ignore-unfixed $(imageRef)
    displayName: 'Trivy Scan'
    env:
      TRIVY_CACHE_DIR: $(Pipeline.Workspace)/.trivycache
  - task: PublishBuildArtifacts@1
    condition: always()
    inputs:
      PathtoPublish: $(Build.ArtifactStagingDirectory)
      ArtifactName: trivy-reports
```

### 實務案例

某團隊的 Pipeline 把 Trivy 放在最後一步，每次失敗都要重跑 20 分鐘的建置。調整為 19.1 的順序後，`trivy fs` 在建置前就攔下 Secret 與相依弱點，平均回饋時間從 20 分鐘降到 3 分鐘。

### 注意事項

- CI 中的 Trivy 只是 Gate 之一，SAST、DAST、測試仍不可省略。
- 各平台的 Trivy 映像或執行檔都應固定版本並驗章（第 14 章）。

---

## 20. GitHub Actions

### 20.1 2026-03 事件後的 GitHub Actions 安全原則

| 原則 | 說明 |
|------|------|
| **以完整 commit SHA 固定 Action** | 官方 Advisory 建議；tag 可被 force-push |
| 安全版本下限 | trivy-action ≥ v0.35.0、setup-trivy ≥ v0.2.6（範例使用 v0.3.1；v0.3.0 無法載入，不可使用） |
| 明確指定 Trivy 版本 | trivy-action v0.36.0 的 `version` 預設為 v0.70.0，不指定就會落後最新版五個 minor |
| 最小 `permissions` | 預設 `contents: read`，需要時才加 `security-events: write` |
| 不傳不必要的 PAT | 惡意版本在外洩失敗時會利用 `INPUT_GITHUB_PAT` 建立公開 repo |
| 固定 Trivy 版本 | `version: v0.75.0`，不用 `latest` |
| 事件稽核 | 檢查組織內是否出現 `tpcp-docs` 開頭的 repo |

取得 tag 對應的 commit SHA：

```bash
git ls-remote https://github.com/aquasecurity/trivy-action refs/tags/v0.36.0
git ls-remote https://github.com/aquasecurity/setup-trivy refs/tags/v0.3.1
```

> 本章範例以 `<SHA>` 表示需替換的完整 40 字元 commit SHA，並在註解標示對應版本。

**setup-trivy v0.3.x 的變更（【官方】）**：

| 版本 | 變更 | 影響 |
|------|------|------|
| v0.3.0 | 安全強化：`${{ }}` 值改以 `env:` 傳入，避免 shell script injection | — |
| v0.3.0 | **Breaking**：`path` input 必須為字面路徑，不再展開 `$HOME`、`$RUNNER_TEMP`、`~` | 有自訂 `path` 者改用 `${{ runner.temp }}/trivy` 或相對路徑 |
| v0.3.0 | 因 `action.yaml` 說明文字含 `${{ runner.temp }}`，在所有 workflow 都無法載入 | **不可使用** |
| v0.3.1 | 修正 v0.3.0 無法載入的問題，新增跨平台 CI 驗證 | 建議版本 |

> trivy-action v0.36.0 內部仍以 SHA 固定 setup-trivy v0.2.6，兩者都在安全下限之上。

### 20.2 完整 Workflow

```yaml
name: security-scan

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

env:
  TRIVY_VERSION: v0.75.0
  IMAGE_REF: ghcr.io/${{ github.repository }}:${{ github.sha }}

jobs:
  trivy:
    runs-on: ubuntu-24.04
    permissions:
      contents: read
      security-events: write
    steps:
      - name: Checkout
        uses: actions/checkout@<SHA> # v4

      - name: Setup Trivy
        uses: aquasecurity/setup-trivy@<SHA> # v0.3.1
        with:
          version: ${{ env.TRIVY_VERSION }}
          cache: true

      - name: Record Trivy version
        run: trivy --version | tee trivy-version.txt

      - name: Repository scan (vuln, secret, misconfig)
        run: |
          trivy fs --scanners vuln,secret,misconfig \
            --format json --output trivy-fs.json .
          trivy convert --format sarif --output trivy-fs.sarif trivy-fs.json

      - name: Upload SARIF
        if: always()
        uses: github/codeql-action/upload-sarif@<SHA> # v4
        with:
          sarif_file: trivy-fs.sarif
          category: trivy-fs

      - name: Build image
        run: docker build -t "$IMAGE_REF" .

      - name: Image scan
        run: trivy image --format json --output trivy-image.json "$IMAGE_REF"

      - name: Generate SBOM
        run: trivy image --format cyclonedx --output sbom.cdx.json "$IMAGE_REF"

      - name: IaC scan
        run: trivy config --format json --output trivy-config.json ./deploy

      - name: Security gate
        run: |
          vuln=$(jq '[.Results[]?.Vulnerabilities[]? | select(.Severity=="CRITICAL" and .Status=="fixed")] | length' trivy-image.json)
          misconf=$(jq '[.Results[]?.Misconfigurations[]? | select(.Status=="FAIL" and (.Severity=="HIGH" or .Severity=="CRITICAL"))] | length' trivy-config.json)
          secret=$(jq '[.Results[]?.Secrets[]?] | length' trivy-fs.json)
          {
            echo "### Trivy Security Gate"
            echo "| Check | Count |"
            echo "|---|---|"
            echo "| CRITICAL fixed vulnerabilities | ${vuln} |"
            echo "| HIGH/CRITICAL misconfigurations | ${misconf} |"
            echo "| Secrets | ${secret} |"
          } >> "$GITHUB_STEP_SUMMARY"
          if [ "$vuln" -gt 0 ] || [ "$misconf" -gt 0 ] || [ "$secret" -gt 0 ]; then
            echo "Security gate failed"; exit 1
          fi

      - name: Upload artifacts
        if: always()
        uses: actions/upload-artifact@<SHA> # v4
        with:
          name: trivy-reports
          path: |
            trivy-version.txt
            trivy-*.json
            trivy-*.sarif
            sbom.cdx.json
          retention-days: 90
```

### 20.3 逐步說明

| Step | 目的 | 重點 |
|------|------|------|
| `permissions` | 最小權限 | workflow 層級只給 `contents: read`；job 需要上傳 SARIF 才加 `security-events: write` |
| Checkout | 取得原始碼 | 以 SHA 固定 |
| Setup Trivy | 安裝指定版本 Trivy | `cache: true` 快取 DB；以 SHA 固定 v0.3.1（下限 ≥ v0.2.6，避開 v0.3.0） |
| Record Trivy version | 稽核證據 | 保存 Trivy 與 DB 版本 |
| Repository scan | 建置前找出相依弱點、Secret、IaC 問題 | 只掃一次產生 JSON，再轉 SARIF |
| Upload SARIF | 顯示在 Security 分頁與 PR | `if: always()` 確保失敗時也上傳 |
| Build image | 建置待測映像 | 以 commit SHA 為 tag |
| Image scan | 掃描 OS 與應用相依 | JSON 供 Gate 與 AI Agent 使用 |
| Generate SBOM | 供應鏈資料 | CycloneDX |
| IaC scan | 掃描部署設定 | 限定 `./deploy` |
| Security gate | 依企業門檻決定是否失敗 | 以 `jq` 解析前面產生的 JSON，不重複掃描；結果寫入 Job Summary，且不輸出 Secret 內容 |
| Upload artifacts | 保存證據 | 90 天保存（依企業政策） |

### 20.4 使用 trivy-action 的寫法

若偏好使用 trivy-action：

```yaml
      - name: Trivy image scan
        uses: aquasecurity/trivy-action@<SHA> # v0.36.0
        with:
          scan-type: image
          image-ref: ${{ env.IMAGE_REF }}
          format: sarif
          output: trivy-image.sarif
          severity: CRITICAL,HIGH
          limit-severities-for-sarif: true
          ignore-unfixed: true
          exit-code: "1"
          version: v0.75.0
          trivyignores: .trivyignore.yaml
```

| Input | 說明 |
|-------|------|
| `version` | v0.36.0 預設 `v0.70.0`；**務必明確指定**為企業核准版本（本手冊為 `v0.75.0`） |
| `scan-type` | `image`、`fs`、`repo`、`rootfs`、`config`、`sbom` |
| `scanners` | 預設 `vuln,secret` |
| `vuln-type` | 預設 `os,library`（對應 CLI 的 `--pkg-types`） |
| `cache` | 預設開啟，快取於 `$GITHUB_WORKSPACE/.cache/trivy` |
| `skip-setup-trivy` | 同一 job 多次呼叫時，第二次起設為 `true` |
| `trivy-config` | 指定 trivy.yaml |
| `github-pat` | 僅在 `format: github` 提交 Dependency Graph 時使用 |
| `token-setup-trivy` | GitHub Enterprise Server 時覆寫 setup-trivy 使用的 token |

### 20.5 DB 快取預熱 Workflow

官方 README 建議以排程 workflow 在預設分支更新快取，掃描 workflow 再設定 `TRIVY_SKIP_DB_UPDATE` / `TRIVY_SKIP_JAVA_DB_UPDATE`：

```yaml
name: update-trivy-cache
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
permissions:
  contents: read
jobs:
  update:
    runs-on: ubuntu-24.04
    steps:
      - name: Setup ORAS
        uses: oras-project/setup-oras@<SHA> # v1
      - name: Get date
        id: date
        run: echo "date=$(date +'%Y-%m-%d')" >> "$GITHUB_OUTPUT"
      - name: Download DBs
        run: |
          mkdir -p "$GITHUB_WORKSPACE/.cache/trivy/db" "$GITHUB_WORKSPACE/.cache/trivy/java-db"
          oras pull ghcr.io/aquasecurity/trivy-db:2
          tar -xzf db.tar.gz -C "$GITHUB_WORKSPACE/.cache/trivy/db" && rm db.tar.gz
          oras pull ghcr.io/aquasecurity/trivy-java-db:1
          tar -xzf javadb.tar.gz -C "$GITHUB_WORKSPACE/.cache/trivy/java-db" && rm javadb.tar.gz
      - name: Save cache
        uses: actions/cache/save@<SHA> # v4
        with:
          path: ${{ github.workspace }}/.cache/trivy
          key: cache-trivy-${{ steps.date.outputs.date }}
```

### 20.6 Dependency Graph 提交

```yaml
  dependency-snapshot:
    runs-on: ubuntu-24.04
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@<SHA> # v4
      - uses: aquasecurity/trivy-action@<SHA> # v0.36.0
        with:
          scan-type: fs
          scan-ref: .
          format: github
          output: dependency-results.sbom.json
          github-pat: ${{ secrets.GITHUB_TOKEN }}
```

> 此 job 需要 `contents: write`，應與掃描 job 分開，避免擴大其他 step 的權限。

### 實務案例

2026-03-20 早上，某組織以 `gh search code "aquasecurity/trivy-action@"` 盤點出 87 個 workflow 使用 mutable tag。依 Advisory：(1) 檢查 03-19 至 03-20 的執行紀錄；(2) 對曾執行的 repo 輪替所有 Secret；(3) 搜尋 `tpcp-docs` repo；(4) 全面改為 SHA pin，並在組織層級啟用「要求 Action 以 SHA 固定」的政策。

### 注意事項

- Dependabot / Renovate 可以自動更新 SHA pin，並在 PR 中顯示版本，兼顧安全與維護性。
- `if: always()` 只用在「上傳結果」的 step，**不可**用在讓 Gate 失效的地方。
- AI Agent 不得修改 workflow 中的 Trivy step、`exit-code` 或 `permissions`（附錄 F）。

---

## 21. Web Application Security

### 21.1 企業 Web Application 的掃描分層

```mermaid
flowchart TB
    FE["Vue / Angular<br/>package-lock / pnpm-lock / yarn.lock"] --> FS1["Dependency Scan<br/>trivy fs"]
    FS1 --> BE["Backend<br/>Spring Boot / Maven / Gradle"]
    BE --> FS2["Dependency Scan<br/>trivy fs + Java DB"]
    FS2 --> DK["Docker<br/>Dockerfile + Base Image"]
    DK --> IM["Image Scan<br/>trivy image"]
    IM --> K8["Kubernetes<br/>Deployment / Service / Ingress"]
    K8 --> RC["Runtime Configuration<br/>trivy config / Operator"]
    RC --> CL["Cloud<br/>Terraform / trivy config"]
```

| 層 | 掃描對象 | 指令 | Scanner |
|----|----------|------|---------|
| Frontend | `package-lock.json`、`pnpm-lock.yaml`、`yarn.lock`、`bun.lock` | `trivy fs ./frontend` | vuln、secret、license |
| Backend | `pom.xml`、`gradle.lockfile`、`target/*.jar` | `trivy fs ./backend` | vuln、secret、license |
| Container | Dockerfile、最終映像 | `trivy config`、`trivy image` | misconfig、vuln、secret |
| Infrastructure | K8s YAML、Helm、Terraform | `trivy config` | misconfig |
| Runtime | 叢集 | `trivy k8s` / Operator | vuln、misconfig、secret、rbac |

### 21.2 前端相依的特殊考量

| 項目 | 說明 |
|------|------|
| Lock file 必要 | 無 lock file 時 Trivy 無法確定版本 |
| Dev dependencies | npm / yarn / pnpm 的 dev dependencies 預設不列入，需 `--include-dev-deps` |
| 打包後的產物 | `dist/` 中的 JS bundle 不保留套件 metadata，應以 lock file 為準 |
| 前端 Secret | 任何以 `VITE_`、`NG_APP_` 等前綴注入前端的變數都會出現在瀏覽器中，**不應存放 Secret** |

### 21.3 後端相依的特殊考量

| 項目 | 說明 |
|------|------|
| Maven | 掃 `pom.xml` 時 Trivy 會解析 parent POM 與遠端 repository；企業內網需設定 mirror |
| Gradle | 需啟用 dependency locking 產生 `gradle.lockfile` |
| Fat jar | Spring Boot 可執行 jar 內嵌所有相依；Trivy 可解析 jar / war / ear |
| Java DB | 以 jar 的 SHA1 辨識 GAV，Java 專案應保持 Java DB 可用 |

### 實務案例

某團隊只掃描後端映像檔，以為前端是靜態檔沒有風險。補上 `trivy fs ./frontend` 後發現 `package-lock.json` 中有 3 個 HIGH 的建置工具弱點，以及一個被注入到前端 bundle 的第三方 API Key（以 `VITE_` 變數注入）。

### 注意事項

- 前端 dev dependencies 雖不進入 Production bundle，但會在 CI 中執行，供應鏈攻擊可能透過 dev 套件竊取 CI Secret；Release 前建議至少執行一次 `--include-dev-deps`。
- 前後端應使用同一份企業 `trivy.yaml`，避免門檻不一致。

---

## 22. Java / Spring Boot 專案

### 22.1 案例環境

| 項目 | 版本 / 工具 |
|------|-------------|
| Java | Java 25（LTS） |
| Framework | Spring Boot 4.x |
| Build | Maven 3.9.x |
| Container | Docker（Eclipse Temurin 25 JRE） |
| Deploy | Kubernetes |
| CI | GitHub Actions |

```text
order-service/
├─ pom.xml
├─ src/main/java/...
├─ src/main/resources/application.yml
├─ Dockerfile
├─ deploy/k8s/deployment.yaml
├─ deploy/k8s/service.yaml
├─ .trivyignore.yaml
└─ .github/workflows/security-scan.yml
```

### 22.2 Step 1：掃描 Maven Dependency

```bash
# 原始碼層級（解析 pom.xml）
trivy fs --scanners vuln --severity HIGH,CRITICAL --dependency-tree .

# 建置後掃描 fat jar（更接近實際交付內容）
mvn -B -DskipTests package
trivy fs --scanners vuln target/order-service-1.0.0.jar
```

- `--dependency-tree`（Experimental，僅 table 格式）會顯示弱點套件是由哪個直接相依引入，方便決定要升級哪一個。
- 企業內網的 Maven Repository：Trivy 會讀取 `~/.m2/settings.xml` 的 remote repositories（v0.68）、proxy（v0.70）、mirrors（v0.71）；v0.73 起也可在 `trivy.yaml` 設定 Maven mirrors（鍵名以 `--generate-default-config` 為準）。
- v0.71 起若遠端 Maven Repository 回應 429，掃描 `pom.xml` 會直接失敗，請改用內部 mirror。

### 22.3 Step 2：掃描 Source Repository

```bash
trivy fs --scanners vuln,secret,misconfig --format json --output trivy-fs.json .
```

### 22.4 Step 3：產生 SBOM

```bash
trivy fs --format cyclonedx --output order-service-source.cdx.json .
```

### 22.5 Step 4：建立 Container Image

```dockerfile
# syntax=docker/dockerfile:1
FROM eclipse-temurin:25-jdk AS build
WORKDIR /src
COPY . .
RUN ./mvnw -B -DskipTests package && \
    java -Djarmode=tools -jar target/order-service-1.0.0.jar extract --layers --launcher --destination /out

FROM eclipse-temurin:25-jre-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app
COPY --from=build --chown=app:app /out/dependencies/ ./
COPY --from=build --chown=app:app /out/spring-boot-loader/ ./
COPY --from=build --chown=app:app /out/snapshot-dependencies/ ./
COPY --from=build --chown=app:app /out/application/ ./
USER app
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "org.springframework.boot.loader.launch.JarLauncher"]
```

```bash
docker build -t registry.internal.example.com/order-service:1.0.0 .
```

> Base Image 版本請以企業核准清單為準；正式環境應以 digest 引用。

### 22.6 Step 5：掃描 Image

```bash
trivy image --scanners vuln,secret --exit-on-eol 2 \
  --format json --output trivy-image.json \
  registry.internal.example.com/order-service:1.0.0

trivy image --format cyclonedx --output order-service-1.0.0.cdx.json \
  registry.internal.example.com/order-service:1.0.0
```

### 22.7 Step 6：掃描 Dockerfile

```bash
trivy config Dockerfile
```

### 22.8 Step 7：掃描 Kubernetes YAML

```bash
trivy config --severity HIGH,CRITICAL ./deploy/k8s
```

### 22.9 Step 8：CI/CD Security Gate

沿用第 20 章 workflow，Gate 條件為：

| 條件 | 動作 |
|------|------|
| Image 中有 CRITICAL 且 `fixed` | Fail |
| Base Image OS 已 EOL | Fail（`--exit-on-eol 2`） |
| 任何 Secret | Fail |
| K8s / Dockerfile 有 HIGH / CRITICAL misconfig | Fail |
| HIGH vuln | Warn + Ticket |

### 22.10 常見問題

| 問題 | 原因 | 解法 |
|------|------|------|
| 掃 `pom.xml` 很慢 | 逐一向遠端解析 POM | 使用內部 mirror，或改掃建置後的 jar |
| 某 jar 沒被辨識 | 重新打包、shaded jar 缺 metadata | 確認 Java DB 可用；檢查 `META-INF/maven` |
| `test` scope 套件出現 | 依版本行為不同 | 以 jar / image 掃描結果作為 Gate 依據 |

### 實務案例

某團隊在 `pom.xml` 掃描時看到 `jackson-databind` 的 HIGH，但不知道是誰引入的。加上 `--dependency-tree` 後發現來自一個內部共用函式庫的舊版本，最後由共用函式庫團隊統一升級，一次修掉 9 個服務的同一個弱點。

### 注意事項

- `application.yml` 中的資料庫密碼、`settings.xml` 中的 Repository 密碼都會被 Secret Scanner 偵測（v0.71 新增 Maven settings 規則）。
- Spring Boot 版本升級前，請先完成第 25 章的 Baseline。

---

## 23. Vue / Angular 專案

### 23.1 案例環境

| 項目 | 版本 / 工具 |
|------|-------------|
| Vue | Vue 3 + Vite + TypeScript |
| Angular | Angular（目前 LTS / Active 版本） + TypeScript |
| 套件管理 | npm 或 pnpm |
| Container | Nginx（unprivileged 版本） |

### 23.2 Package Dependency 與 Lock File

```bash
# npm
npm ci
trivy fs --scanners vuln,license --severity HIGH,CRITICAL .

# pnpm
pnpm install --frozen-lockfile
trivy fs --scanners vuln --severity HIGH,CRITICAL .

# Release 前含 dev dependencies
trivy fs --scanners vuln --include-dev-deps .
```

| Lock file | 支援 |
|-----------|------|
| `package-lock.json` | ✓（v0.69 起可解析授權） |
| `yarn.lock` | ✓ |
| `pnpm-lock.yaml` | ✓（v0.72 支援 multi-document、v0.73 支援 workspace 重疊套件） |
| `bun.lock` | ✓（v0.63 起） |

### 23.3 Secret 與 Configuration

| 檔案 | 風險 |
|------|------|
| `.env`、`.env.production` | 若被 commit，Trivy 會偵測 |
| Vue `import.meta.env.VITE_*` | 會被打包進前端，**等同公開** |
| Angular `environment.prod.ts` | 會被打包進前端，**等同公開** |

```bash
trivy fs --scanners secret .
```

> 前端應只放「公開設定」（API base URL、Feature Flag），任何 Key 都應改由後端代理。

### 23.4 Docker Image

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
```

> Node 與 Nginx 版本請以企業核准清單與官方支援週期為準。

```bash
trivy config Dockerfile
trivy image --scanners vuln,secret registry.internal.example.com/portal-web:2.3.0
```

### 23.5 SBOM

```bash
trivy fs --format cyclonedx --output portal-web-source.cdx.json .
trivy image --format cyclonedx --output portal-web-image.cdx.json registry.internal.example.com/portal-web:2.3.0
```

### 23.6 CI/CD

前端 Pipeline 與後端相同模式：`trivy fs` → build → `trivy image` → SBOM → Gate。差異在於前端映像通常只含 Nginx 與靜態檔，Image Scan 主要看 Base Image 的 OS 套件。

### 實務案例

某 Angular 專案的 Image Scan 永遠是 0 個應用相依 Finding，團隊以為前端很安全。原因是最終映像只有 Nginx 與 `dist/`，相依資訊根本不在映像中。改為同時掃描 `package-lock.json` 後，才看到真正的前端相依風險。

### 注意事項

- 前端 SBOM 應以 **lock file** 產生，映像檔 SBOM 只能代表 Nginx 層。
- `npm install` 會改寫 lock file；CI 一律使用 `npm ci` / `pnpm install --frozen-lockfile`。

---

## 24. Legacy System Reverse Engineering

### 24.1 背景

AI Agent 協助 Legacy 系統現代化的典型流程：

```text
Legacy Application
        ↓
Reverse Engineering
        ↓
Code Analysis
        ↓
Architecture Recovery
        ↓
Specification
        ↓
Modernization
```

> **【AI Agent 流程】** AI Agent 必須**先理解安全現況，再進行 Modernization**。否則現代化計畫可能把已知弱點、硬編碼帳密、過時元件原封不動搬到新架構。

### 24.2 Security Baseline 流程

```mermaid
flowchart TB
    L["Legacy Repository"] --> R1["trivy repo<br/>指定歷史 tag / commit"]
    L --> R2["trivy fs<br/>工作目錄 + 建置產物"]
    L --> R3["trivy config<br/>Dockerfile / K8s / Terraform"]
    L --> R4["secret scan"]
    L --> R5["dependency scan<br/>jar / war / ear / lock file"]
    L --> R6["license scan"]
    L --> R7["SBOM"]
    R1 & R2 & R3 & R4 & R5 & R6 & R7 --> B["Security Baseline"]
```

### 24.3 執行步驟

```bash
mkdir -p baseline

# 1. 版本資訊（稽核證據）
trivy --version > baseline/trivy-version.txt

# 2. 原始碼：vuln + secret + misconfig
trivy fs --scanners vuln,secret,misconfig --format json --output baseline/fs.json .

# 3. License
trivy fs --scanners license --license-full --format json --output baseline/license.json .

# 4. SBOM
trivy fs --format cyclonedx --output baseline/source.cdx.json .

# 5. 建置產物（Legacy 常見 war / ear / lib/*.jar）
trivy fs --scanners vuln --format json --output baseline/artifacts.json ./dist

# 6. 若已有部署映像
trivy image --exit-on-eol 2 --format json --output baseline/image.json registry.internal.example.com/legacy-app:5.2

# 7. 指定歷史版本（例如目前 Production 的 tag）
trivy repo --tag release-5.2 --format json --output baseline/repo-release-5.2.json .
```

### 24.4 Legacy 系統的特殊情況

| 情況 | 處理方式 |
|------|----------|
| 沒有 lock file（Ant、手動 `lib/*.jar`） | 直接掃描 `lib/` 與 war / ear，Trivy 以 Java DB 依 jar SHA1 辨識 |
| 沒有 Dockerfile | 跳過 container 層，記錄於 Baseline 的「未涵蓋範圍」 |
| 執行於 IBM AIX / 舊 Unix | 官方 Release 未提供 AIX 執行檔；將建置產物複製到 Linux 掃描環境 |
| 原始碼與 Production 版本不一致 | 以 Production 實際部署的產物為準，原始碼掃描作為輔助 |
| 大量硬編碼帳密 | 先走第 8 章 Secret 流程，**輪替優先於現代化** |
| OS EOL | 以 `--exit-on-eol` 記錄，納入現代化必要條件 |

### 24.5 Security Baseline 產出物

```markdown
# Security Baseline — legacy-order-system @ release-5.2

| 項目 | 結果 |
|------|------|
| 掃描日期 / Trivy 版本 / DB 日期 | 2026-10-03 / v0.75.0 / （見 trivy-version.txt） |
| 掃描範圍 | 原始碼、dist/*.ear、Dockerfile（無）、K8s（無） |
| 未涵蓋範圍 | DB stored procedure、MQ 設定、AIX OS 套件 |
| Vulnerability | CRITICAL 7（fixed 5）、HIGH 31、MEDIUM 58 |
| Secret | 4（DB 密碼 2、LDAP 密碼 1、私鑰 1）→ 已啟動輪替 |
| Misconfiguration | 不適用（無 IaC） |
| License | Restricted 2、Unknown 11 → 送法務 |
| EOL 元件 | Java 8 runtime、Struts 1.x |
| SBOM | baseline/source.cdx.json（412 components） |
```

### 實務案例

某 AI Agent 被要求「把 Struts 1 系統改寫成 Spring Boot」。在 Baseline 階段 Trivy 找出 `config/db.properties` 中的 Production 資料庫密碼與 11 個無法辨識授權的 jar。團隊決定：先輪替密碼、由法務確認授權，才允許 AI Agent 開始 Architecture Recovery。這避免了把舊密碼寫進新系統的設定範本。

### 注意事項

- Baseline 報告含 Secret 位置，應存放於受控位置，不得貼入公開 Issue 或 AI 對話。
- Legacy 掃描結果通常很多，Baseline 的目的是「建立事實」，不是「一次修完」。

---

## 25. Software Framework Upgrade

### 25.1 升級安全流程

```mermaid
flowchart LR
    A["Spring Boot 3.x<br/>現況"] --> B["Baseline Scan"]
    B --> C["SBOM Before"]
    C --> D["Dependency Vulnerability Before"]
    D --> E["Upgrade"]
    E --> F["Trivy Re-scan"]
    F --> G["Compare"]
    G --> H["Regression Security Check"]
    H --> I{"新增風險？"}
    I -->|"否"| J["Upgrade Report + Human Review"]
    I -->|"是"| E
```

### 25.2 適用的升級類型

| 升級類型 | 重點比較項目 |
|----------|-------------|
| Java Upgrade | Runtime 映像 OS 套件、jar 相依 |
| Spring Boot Upgrade | BOM 管理的傳遞相依版本 |
| Node.js Upgrade | Base Image、原生模組 |
| Vue / Angular Upgrade | lock file 中的大量套件變化、License |
| Base Image Upgrade | OS 套件、EOL 狀態 |
| Kubernetes Version Upgrade | 過時 API（`trivy k8s --k8s-version`）、Helm Chart misconfig |

### 25.3 Before / After 掃描

```bash
# Before（在升級分支建立前的 commit）
git checkout main
trivy fs --scanners vuln,secret,misconfig,license --format json --output before/fs.json .
trivy fs --format cyclonedx --output before/sbom.cdx.json .

# After
git checkout upgrade/spring-boot-4
trivy fs --scanners vuln,secret,misconfig,license --format json --output after/fs.json .
trivy fs --format cyclonedx --output after/sbom.cdx.json .
```

> **重要**：Before 與 After 必須使用**同一版 Trivy、同一天的 DB**，否則差異可能來自 DB 更新而非程式變更。建議在同一個 Job 內連續執行，或先 `--download-db-only` 再兩次都加 `--skip-db-update`。

### 25.4 比較腳本

```python
"""比較兩份 Trivy JSON 報告的 Vulnerability、Misconfiguration、Secret、License 差異。"""
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def keys(report):
    vuln, misconf, secret, lic = set(), set(), set(), set()
    for r in report.get("Results") or []:
        target = r.get("Target", "")
        for v in r.get("Vulnerabilities") or []:
            vuln.add((v["VulnerabilityID"], v["PkgName"], v.get("Severity", "")))
        for m in r.get("Misconfigurations") or []:
            if m.get("Status") == "FAIL":
                misconf.add((m.get("ID", ""), target, m.get("Severity", "")))
        for s in r.get("Secrets") or []:
            secret.add((s.get("RuleID", ""), target))
        for item in r.get("Licenses") or []:
            lic.add((item.get("Name", ""), item.get("PkgName", ""), item.get("Severity", "")))
    return {"vulnerability": vuln, "misconfiguration": misconf, "secret": secret, "license": lic}


def main(before_path, after_path):
    before, after = keys(load(before_path)), keys(load(after_path))
    regression = False
    for kind in before:
        added = sorted(after[kind] - before[kind])
        removed = sorted(before[kind] - after[kind])
        print(f"## {kind}: +{len(added)} / -{len(removed)}")
        for item in added:
            print(f"  + {item}")
            if kind == "secret" or (len(item) > 2 and item[-1] in ("HIGH", "CRITICAL")):
                regression = True
        for item in removed:
            print(f"  - {item}")
    return 1 if regression else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
```

```bash
python trivy_diff.py before/fs.json after/fs.json
```

輸出只包含 ID、套件、目標與 Severity，**不含 Secret 內容**，可安全提供給 AI Agent。

### 25.5 SBOM 差異

```bash
jq -r '.components[] | "\(.purl)"' before/sbom.cdx.json | sort > before/purls.txt
jq -r '.components[] | "\(.purl)"' after/sbom.cdx.json  | sort > after/purls.txt
diff before/purls.txt after/purls.txt
```

### 25.6 Security Upgrade Report 範本

| 項目 | Before | After | 差異 | 結論 |
|------|--------|-------|------|------|
| CVE CRITICAL | 5 | 0 | -5 | 改善 |
| CVE HIGH | 22 | 3 | -19 | 改善；3 筆為新引入，需評估 |
| Dependency 數 | 214 | 198 | -16 | — |
| Misconfiguration HIGH+ | 2 | 2 | 0 | 無變化 |
| Secret | 0 | 0 | 0 | — |
| License Restricted | 1 | 1 | 0 | 已有法務意見 |

### 實務案例

某團隊把 Spring Boot 從 3.x 升到 4.x，AI Agent 只回報「CVE 從 27 降到 3」。比較腳本卻顯示那 3 個 HIGH 都是**新引入**的：新版某 starter 帶入一個有已知弱點的傳遞相依。若沒有 Before / After 逐項比較，這 3 個會被淹沒在「整體改善」的數字裡。

### 注意事項

- 只比「總數」會掩蓋新引入的風險，一定要比「集合差異」。
- 升級後的 Re-scan 不能取代功能回歸測試。

---

## 26. AI Agent + Trivy

### 26.1 從「AI 寫 Code」到「AI Security Feedback Loop」

AI Agent 不應只是：

```text
AI 寫 Code → 結束
```

而應形成：

```text
AI Agent → Plan → Implement → Test → Trivy Scan → Analyze Findings → Fix → Re-scan → Verify → Commit
```

```mermaid
flowchart LR
    P["Plan"] --> I["Implement"]
    I --> T["Test"]
    T --> S["Trivy Scan"]
    S --> A["Analyze Findings"]
    A --> D{"可安全自動修？"}
    D -->|"是"| F["Fix"]
    D -->|"否"| H["Human Approval"]
    F --> R["Re-scan"]
    R --> V["Verify<br/>Before / After"]
    V --> C["Commit / PR"]
    H --> C
```

### 26.2 AI Agent 什麼時候必須執行 Trivy

以下為 **【AI Agent 流程】**：

| 觸發事件 | 必須執行 | 指令 |
|----------|----------|------|
| 開始任何任務前（Baseline） | ✓ | `trivy fs --scanners vuln,secret,misconfig --format json` |
| 修改 `pom.xml`、`build.gradle`、`package.json`、lock file | ✓ | `trivy fs --scanners vuln,license` |
| 修改 `Dockerfile` | ✓ | `trivy config Dockerfile` |
| 修改 K8s YAML / Helm / Terraform | ✓ | `trivy config <dir>` |
| 新增或修改任何設定檔 | ✓ | `trivy fs --scanners secret` |
| 建置 Production 映像前後 | ✓ | `trivy image` |
| 任務結束前（Verify） | ✓ | 重跑 Baseline 指令並比較 |
| Reverse Engineering 開始時 | ✓ | 第 24 章 Baseline |
| Framework Upgrade 前後 | ✓ | 第 25 章 Before / After |

### 26.3 AI Agent 呼叫 Trivy 的設計原則

| 原則 | 說明 |
|------|------|
| 一律輸出 JSON | AI Agent 讀 JSON，人讀 table |
| 先摘要再讀 | 以 `jq` / 腳本萃取最小欄位（第 18.6 節） |
| 不讀 Secret 原文 | 只讀 Rule ID、路徑、行號 |
| 明確 Scanner | 不依賴預設值 |
| 固定版本 | AI Agent 執行環境的 Trivy 版本與 CI 一致 |
| 記錄指令 | 在 PR 描述中列出執行過的 Trivy 指令與版本 |

### 26.4 Trivy MCP Server：讓 AI Agent 以標準工具呼叫 Trivy

**【官方】** Aqua Security 提供 `trivy-mcp` plugin，把 Trivy 包裝成 **MCP（Model Context Protocol）Server**。支援 MCP 的 AI 工具（VS Code Copilot Agent mode、Cursor、JetBrains IDE、Claude Desktop）可以直接把「掃描」當成工具呼叫，不必讓 Agent 自行拼接 shell 指令。

| 項目 | 說明 |
|------|------|
| 專案 | `github.com/aquasecurity/trivy-mcp`（MIT） |
| 版本 | v0.0.20（約 10 個月前發布），仍為 0.0.x 早期版本 |
| 掃描類型 | Filesystem、Container Image、Remote Repository；可產生 SBOM |
| 傳輸模式 | `stdio`（預設）、`streamable-http`、`sse` |
| 預設監聽 | `localhost:23456`（僅網路傳輸模式） |
| Aqua Platform | `--use-aqua-platform` / `-a` 啟用商業版整合（預設關閉） |
| 自訂 Trivy | `--trivy-binary <path>` 指定企業驗章過的 Trivy 執行檔 |

```mermaid
flowchart LR
    U["Developer"] --> IDE["IDE AI Agent<br/>VS Code / Cursor / JetBrains"]
    IDE -->|"MCP tool call - stdio"| MCP["trivy mcp<br/>plugin"]
    MCP --> T["Trivy CLI<br/>企業核准版本"]
    T --> DB[("內部 DB Mirror")]
    T --> R["掃描結果"]
    R --> MCP --> IDE
```

### 26.5 安裝與 IDE 設定

**Step 1：安裝 plugin 並固定版本**（v0.52 起 `trivy plugin install` 支援 `@<version>`）：

```bash
trivy plugin install mcp@v0.0.20
trivy plugin list
```

**Step 2：啟動（手動驗證用）**：

```bash
# IDE 整合使用 stdio，由 IDE 啟動
trivy mcp

# 網路傳輸模式只綁 localhost
trivy mcp --transport streamable-http --host localhost --port 23456
```

**Step 3：VS Code 設定**（需 VS Code 1.99 以上、Copilot Chat 使用 Agent mode）。專案層級可放在 `.vscode/mcp.json`：

```json
{
  "servers": {
    "trivy": {
      "type": "stdio",
      "command": "trivy",
      "args": ["mcp", "--trivy-binary", "/opt/trivy/0.75.0/trivy"]
    }
  }
}
```

> trivy-mcp 官方文件的範例是寫在 VS Code User Settings 的 `"mcp": { "servers": { ... } }` 區塊；兩種位置擇一即可。Windows 請將 `--trivy-binary` 改為 `C:\\Tools\\trivy\\0.75.0\\trivy.exe`。

**Step 4：使用**：在 Agent mode 中輸入「這個專案有沒有弱點或錯誤設定？」等自然語言問題，Agent 會呼叫 Trivy MCP 工具。

### 26.6 MCP 與 CLI 的分工

| 面向 | Trivy MCP Server | Trivy CLI（JSON） |
|------|------------------|-------------------|
| 主要使用者 | 開發者本機的 IDE AI Agent | CI/CD、後端 AI Agent、腳本 |
| 觸發方式 | 自然語言 → 工具呼叫 | 明確指令 |
| 可重現性 | 參數由 Agent 決定，較低 | 參數固定，高 |
| 作為 Gate | **不適合** | 適合 |
| 稽核證據 | 需額外保存 session log | JSON 報告即證據 |

**【企業建議】** MCP 用於「開發階段的即時回饋」，CI 中的 CLI Gate 仍是唯一具約束力的控制點。Guardrail 見第 30.4 節。

### 實務案例

某團隊讓 AI Agent 在每次修改 `pom.xml` 後自動跑 `trivy fs --scanners vuln`，並把 JSON 摘要回饋給 Agent。過去 AI Agent 常為了解決編譯錯誤降版某套件，導致重新引入已修補的 CVE；導入回饋迴圈後，這類退化在 PR 送出前就被 Agent 自己發現並修正。

### 注意事項

- 回饋迴圈必須有「停止條件」：同一 Finding 修正 3 次仍失敗，就停止並請求人工協助，避免 AI Agent 無限嘗試。
- Trivy 是 AI Agent 的「感測器」，不是「決策者」；決策仍依第 27–30 章的規則。
- trivy-mcp 仍為 0.0.x 版本，企業導入前應經 Security Team 評估，且不得取代 CI Gate。

---

## 27. AI Agent 使用 Trivy 的標準流程

### 27.1 十步驟

| 步驟 | 名稱 | 內容 | 產出 |
|------|------|------|------|
| 1 | Understand | 理解任務、專案結構、技術棧 | 任務理解摘要 |
| 2 | Scan | 執行 Baseline 掃描 | `baseline/*.json` |
| 3 | Analyze | 解讀 Finding：ID、套件、版本、Fixed Version、Status | Finding 清單 |
| 4 | Prioritize | 依企業 Policy 分級：Block / Warn / Monitor | 優先順序表 |
| 5 | Fix | 只修可安全自動修的項目 | 程式變更 |
| 6 | Test | 單元、整合測試 | 測試結果 |
| 7 | Scan Again | 以相同設定 Re-scan | `after/*.json` |
| 8 | Compare | 集合差異比較 | 差異報告 |
| 9 | Generate Report | Security Report（不含 Secret 原文） | `security-report.md` |
| 10 | Human Review | 等待人工核准 | Approval 紀錄 |

### 27.2 核心原則

> **Scan → Understand → Fix → Verify**
>
> **不可：Scan → Automatically modify everything**

| 正確 | 錯誤 |
|------|------|
| 先確認 Fixed Version 存在且相容，再升級 | 看到 CVE 就把所有套件升到最新 major |
| 升級後跑測試並 Re-scan | 升級後直接 commit |
| 無法修正時產生 Exception 申請草稿交人審核 | 自行加入 `.trivyignore` |
| 回報「新增 / 移除」清單 | 只回報總數 |

```mermaid
stateDiagram-v2
    [*] --> Understand
    Understand --> Scan
    Scan --> Analyze
    Analyze --> Prioritize
    Prioritize --> Fix: 可安全自動修
    Prioritize --> HumanReview: 需人工判斷
    Fix --> Test
    Test --> ScanAgain
    ScanAgain --> Compare
    Compare --> Fix: 有新增風險且可修
    Compare --> Report: 無新增風險
    Compare --> HumanReview: 有新增風險且不可修
    Report --> HumanReview
    HumanReview --> [*]
```

### 實務案例

某 AI Agent 收到「修掉所有 HIGH」的指令，第一版做法是把 `spring-boot-starter-parent` 從 3.x 直接改到 4.x，導致 47 個編譯錯誤。改用十步驟流程後，Agent 先分析出 HIGH 集中在兩個傳遞相依，只以 `dependencyManagement` 覆寫這兩個版本，測試通過、Re-scan 確認修正，變更範圍從數百行降到 6 行。

### 注意事項

- Prioritize 的依據是**企業 Policy**，不是 AI Agent 的主觀判斷。
- 步驟 10 不可省略，即使所有 Finding 都已修正。

---

## 28. AI Agent Prompt Engineering

以下 Prompt 可直接複製使用。每個 Prompt 都包含 **Input、Output、安全限制、Human Approval Point**。`{{ }}` 為需替換的參數。

### 28.1 Repository Security Scan Prompt

```text
【角色】你是企業 DevSecOps AI Agent，負責對 Repository 建立安全基線。

【Input】
- Repository 路徑：{{repo_path}}
- 企業 Trivy 設定：{{config_path}}（若無則使用下列預設）
- Trivy 版本需為：{{trivy_version}}

【執行步驟】
1. 執行 `trivy --version` 並記錄。
2. 執行：
   trivy fs --scanners vuln,secret,misconfig --format json --output scan/fs.json {{repo_path}}
3. 以 jq 萃取摘要（VulnerabilityID、PkgName、InstalledVersion、FixedVersion、Severity、Status；
   Secret 只取 RuleID、Target、StartLine）。
4. 依企業 Policy 分級：CRITICAL 且 fixed → Block；HIGH 且 fixed → Warn；其他 → Monitor。

【Output】
- Markdown 表格：Severity 統計、Block 清單、Warn 清單、Secret 位置清單（不含內容）。
- 每個 Block 項目的建議修正方式（升級版本、影響範圍）。

【安全限制】
- 不得輸出、引用或摘要任何 Secret 的值或含 Secret 的程式碼行。
- 不得修改任何檔案。
- 不得新增或修改 .trivyignore*、trivy.yaml、trivy-secret.yaml。

【Human Approval Point】
- 報告完成後停止，等待人工決定修正範圍。
```

### 28.2 Container Security Scan Prompt

```text
【角色】你是 Container Security AI Agent。

【Input】
- Image（必須為 digest 或固定版本 tag）：{{image_ref}}
- Dockerfile 路徑：{{dockerfile}}

【執行步驟】
1. trivy image --scanners vuln,secret --exit-on-eol 2 --format json --output scan/image.json {{image_ref}}
2. trivy config --format json --output scan/dockerfile.json {{dockerfile}}
3. 將 Vulnerability 依來源分為：OS 套件（Base Image）與應用程式相依。
4. 若 OS 已 EOL，明確標示。

【Output】
- Base Image 弱點摘要與「建議的替代 Base Image 版本（需人工確認）」。
- 應用程式相依弱點摘要。
- Dockerfile misconfiguration 清單與修正建議（可提供 diff）。

【安全限制】
- 不得以 latest tag 作為修正建議。
- 不得建議移除 USER、HEALTHCHECK 等安全設定來減少 Finding。
- 不得輸出 Secret 內容。

【Human Approval Point】
- 更換 Base Image（任何 major / distro 變更）必須人工核准。
```

### 28.3 Kubernetes Security Scan Prompt

```text
【角色】你是 Kubernetes Security AI Agent。

【Input】
- Manifest 目錄或 Helm Chart：{{manifest_path}}
- Production values 檔：{{values_file}}
- （選用）叢集 context：{{k8s_context}}（僅限非 Production）

【執行步驟】
1. trivy config --helm-values {{values_file}} --format json --output scan/k8s-config.json {{manifest_path}}
2. 若提供 context：trivy k8s {{k8s_context}} --report summary --format json --output scan/k8s-cluster.json
   （注意：trivy k8s 為 Experimental）
3. 分類：Pod Security、RBAC、資源限制、網路、Secret。

【Output】
- 依資源列出 Finding 與 YAML 修正 diff（securityContext、resources、automountServiceAccountToken 等）。

【安全限制】
- 不得對 Production 叢集執行 trivy k8s，除非任務明確授權。
- 不得建議以 privileged、hostNetwork、hostPath 解決功能問題。
- 不得修改 RBAC 以擴大權限。

【Human Approval Point】
- 任何 RBAC 變更、NetworkPolicy 變更必須人工核准。
```

### 28.4 Dependency Upgrade Prompt

```text
【角色】你是 Dependency Upgrade AI Agent。

【Input】
- 專案路徑：{{repo_path}}
- 目標 Finding（CVE 清單）：{{cve_list}}
- 允許的升級範圍：{{scope}}（例如：僅 patch / minor；不得升 major）

【執行步驟】
1. Before：trivy fs --scanners vuln,license --format json --output before.json {{repo_path}}
2. 對每個 CVE 確認 FixedVersion；以 --dependency-tree 找出引入來源。
3. 選擇最小變更：優先升級直接相依，或以 dependencyManagement / overrides 指定傳遞相依版本。
4. 執行建置與全部測試。
5. After：以相同指令產生 after.json，執行 trivy_diff.py before.json after.json。

【Output】
- 變更清單（套件、舊版、新版、理由）。
- 測試結果。
- Before / After 差異（新增、移除）。

【安全限制】
- 不得升級超出 {{scope}} 的版本。
- 新增任何 HIGH/CRITICAL 或 License 類別變為 Restricted/Forbidden 時，必須回報並停止。
- 不得以 ignore 檔處理無法修正的 CVE。

【Human Approval Point】
- major 版本升級、License 類別變化、無法修正的 CRITICAL。
```

### 28.5 Framework Upgrade Security Prompt

```text
【角色】你是 Framework Upgrade Security AI Agent。

【Input】
- Framework 與版本：{{from_version}} → {{to_version}}（例如 Spring Boot 3.5 → 4.0）
- Before 分支：{{base_branch}}；After 分支：{{upgrade_branch}}

【執行步驟】
1. 先執行 trivy image --download-db-only，之後所有掃描加 --skip-db-update，確保 DB 一致。
2. 在兩個分支分別產生：fs.json（vuln,secret,misconfig,license）與 sbom.cdx.json。
3. 若有映像檔，兩邊各自 build 並掃描 image.json。
4. 執行比較：CVE、Dependency（SBOM purl 差異）、Misconfiguration、Secret、License。

【Output】
- Security Upgrade Report（第 25.6 節格式）。
- 「新引入風險」獨立段落，即使整體是改善。

【安全限制】
- Before / After 必須使用相同 Trivy 版本與 DB。
- 不得只回報總數。

【Human Approval Point】
- 任何新引入的 HIGH/CRITICAL、任何新 Secret、任何 License 類別變化。
```

### 28.6 Reverse Engineering Security Prompt

```text
【角色】你是 Legacy Reverse Engineering Security AI Agent。

【Input】
- Legacy repo：{{repo_path}}
- Production 對應版本（tag / commit）：{{prod_ref}}
- 建置產物目錄（war/ear/lib）：{{artifact_dir}}

【執行步驟】
1. 依第 24.3 節產生 baseline/ 下所有檔案。
2. 標示未涵蓋範圍（例如 AIX OS、DB 程序、MQ 設定）。
3. 列出 EOL 元件與硬編碼 Secret 位置（不含內容）。

【Output】
- Security Baseline（第 24.5 節格式）。
- 建議納入 Modernization Plan 的安全前置條件。

【安全限制】
- 只讀，不修改任何檔案。
- 不得在輸出中包含 Secret 值、內部主機名稱以外的連線字串。
- 不得對 License 下法律結論。

【Human Approval Point】
- Baseline 完成後停止；Secret 輪替與 License 判定交由人處理後才可進入 Architecture Recovery。
```

### 28.7 SBOM Analysis Prompt

```text
【角色】你是 Software Supply Chain AI Agent。

【Input】
- SBOM 檔：{{sbom_path}}（CycloneDX 或 SPDX）

【執行步驟】
1. trivy sbom --scanners vuln,license --format json --output scan/sbom-scan.json {{sbom_path}}
2. 統計：元件數、各生態系元件數、CRITICAL/HIGH 弱點、License 類別分佈、UNKNOWN License。
3. 找出「同一套件多版本並存」的情況。

【Output】
- SBOM 健康度摘要表。
- 需優先處理的元件清單。

【安全限制】
- 不得修改 SBOM 檔。
- License 只列分類與名稱，不下法律結論。

【Human Approval Point】
- 報告送 DevSecOps 與 OSPO 審閱。
```

### 28.8 Secret Finding Response Prompt

```text
【角色】你是 Secret Incident Response AI Agent。

【Input】
- Trivy Secret 摘要（僅含 RuleID、Target、StartLine、Severity）：{{secret_summary}}

【執行步驟】
1. 依 RuleID 判斷 Secret 類型（雲端金鑰、DB 密碼、Token、私鑰）。
2. 為每一筆產生處理建議：負責撤銷 / 輪替的角色、程式碼改為讀取 Secret Manager 的修改方式。
3. 產生 pre-commit 防護建議（trivy fs --scanners secret）。

【Output】
- 處理清單（Detect → Redact → Revoke/Rotate → Investigate → Prevent）。
- 程式碼修改 diff：以環境變數或 Secret Manager 取代硬編碼值（diff 中以 <REDACTED> 表示原值）。

【安全限制】
- 嚴禁開啟、讀取、輸出 Secret 所在行的內容。
- 嚴禁嘗試驗證 Secret 是否有效（不得用它呼叫任何 API）。
- 嚴禁將 Secret 寫入任何檔案、Log、Ticket。

【Human Approval Point】
- 撤銷與輪替一律由 Secret Owner 執行；AI Agent 只提供建議。
```

### 28.9 CI/CD Failure Analysis Prompt

```text
【角色】你是 CI/CD Security Gate 分析 AI Agent。

【Input】
- 失敗的 Job 名稱與 Trivy JSON 報告路徑：{{report_paths}}
- 企業 Gate 規則：{{gate_policy}}

【執行步驟】
1. 確認失敗原因屬於哪條 Gate 規則。
2. 列出觸發 Gate 的 Finding（ID、套件、Fixed Version）。
3. 為每筆提出「修正」選項；若無法修正，產生 Exception 申請草稿（第 39 章欄位）。

【Output】
- 失敗原因摘要。
- 修正 PR 建議或 Exception 申請草稿。

【安全限制】
- 嚴禁修改 workflow、trivy.yaml、ignore 檔、exit-code、severity 來讓 Gate 通過。
- 嚴禁移除或略過任何 Scan step。
- Exception 只能產生「草稿」，不得自行提交核准。

【Human Approval Point】
- 任何 Exception 必須由 Security Team 核准。
```

### 28.10 Security Regression Verification Prompt

```text
【角色】你是 Security Regression Verification AI Agent。

【Input】
- Before 報告：{{before_json}}
- After 報告：{{after_json}}
- 兩次掃描使用的 Trivy 版本與 DB 日期：{{versions}}

【執行步驟】
1. 確認兩次掃描版本與 DB 一致；不一致則停止並回報。
2. 執行 trivy_diff.py {{before_json}} {{after_json}}。
3. 判定：是否有新增 HIGH/CRITICAL、新增 Secret、新增 FAIL misconfiguration、License 類別升高。

【Output】
- PASS / FAIL 判定與理由。
- 新增項目清單、移除項目清單。

【安全限制】
- 判定標準只依企業 Policy，不得自行放寬。
- 不得輸出 Secret 內容。

【Human Approval Point】
- FAIL 時交 Tech Lead 與 DevSecOps 決定；PASS 仍需 Reviewer 簽核 PR。
```

### 實務案例

某團隊把 28.9 的 Prompt 放進 CI 失敗通知的自動分析機器人。過去 AI 助手常建議「把 severity 調成 CRITICAL 就會過」，加入安全限制後，機器人只會提供修正 PR 建議或 Exception 草稿，Gate 被繞過的情況歸零。

### 注意事項

- Prompt 中的安全限制應與 AGENTS.md（附錄 F）一致，避免規則衝突。
- 所有 Prompt 都假設 AI Agent 在**受限的執行環境**中運作（第 30 章）。

---

## 29. AI Agent 不可以做的事情

### 29.1 禁止清單

**【Security Policy 範本】** AI Agent 不得自行：

| # | 禁止行為 | 常見「理由」 | 為什麼禁止 |
|---|----------|-------------|-----------|
| 1 | 刪除 Security Finding | 「這是誤報」 | 誤報判定需人工與證據 |
| 2 | 永久加入 Ignore | 「先讓 CI 過」 | 繞過治理 |
| 3 | 洩漏 Secret | 「為了說明問題」 | 擴大外洩 |
| 4 | 把 API Key 寫進程式 | 「測試需要」 | 新增外洩點 |
| 5 | 降低 Security Severity | 「實際影響很小」 | Severity 調整屬 Security 權限 |
| 6 | 修改企業 Security Policy | 「規則太嚴」 | 違反治理分工 |
| 7 | 自行接受 Critical Vulnerability | 「沒有修補版本」 | 風險接受需授權 |
| 8 | 自行判定 License 法律結論 | 「內部用沒關係」 | 屬法務職權 |
| 9 | 刪除 Security Control | 「這個 USER 設定導致權限錯誤」 | 削弱防護 |
| 10 | 為通過 CI/CD 而關閉 Scanner | 「掃描太慢」 | 直接破壞 Gate |
| 11 | 修改 `exit-code`、`severity`、`scanners` 以減少 Finding | 「調整設定」 | 變相關閉 Scanner |
| 12 | 修改 GitHub Action 的 pin 為 mutable tag | 「方便更新」 | 供應鏈風險 |
| 13 | 對 Production 叢集執行 `trivy k8s` | 「想看真實狀況」 | 未授權存取 |

### 29.2 三區分類

```mermaid
flowchart TB
    A["AI Agent 動作"] --> S["Safe Automatic Fix<br/>可自動執行"]
    A --> H["Human Approval Required<br/>需人工核准"]
    A --> F["Forbidden Action<br/>禁止"]
    S --> S1["patch / minor 升級且有 Fixed Version"]
    S --> S2["Dockerfile 加 USER / HEALTHCHECK"]
    S --> S3["K8s 加 securityContext / resources"]
    S --> S4["產生 SBOM、報告"]
    H --> H1["major 升級、Base Image 換 distro"]
    H --> H2["Exception 草稿"]
    H --> H3["RBAC / NetworkPolicy 變更"]
    H --> H4["License 類別變化"]
    F --> F1["新增 / 延長 ignore"]
    F --> F2["關閉 Scanner、改 exit-code"]
    F --> F3["輸出 Secret"]
    F --> F4["修改 Security Policy"]
```

### 實務案例

某 AI Agent 在 PR 中把 Dockerfile 的 `USER app` 刪除，理由是「容器啟動時沒有寫入 `/tmp` 的權限」。Trivy 的 `trivy config` 立刻出現 AVD-DS-0002，Reviewer 依禁止清單第 9 條退回，正確修法是掛載 `emptyDir` 到 `/tmp`。

### 注意事項

- 禁止清單必須同時寫入 AGENTS.md / copilot-instructions.md（附錄 F）與 CI 的技術控制（CODEOWNERS、branch protection），**只寫在 Prompt 裡不夠**。

---

## 30. AI Agent Security Guardrail

### 30.1 Guardrail 總表

| Guardrail | 說明 | 技術實作 |
|-----------|------|----------|
| Least Privilege | AI Agent 只有完成任務所需的最小權限 | 唯讀 token、無 Production kubeconfig、無 Registry push 權限 |
| Secret Redaction | Agent 看到的掃描結果不含 Secret 內容 | jq 摘要、`.Secrets[]` 只取 RuleID / 位置 |
| No Credential Exposure | Agent 環境不持有長期憑證 | OIDC 短期憑證、不在環境變數放 PAT |
| Human Approval | 高風險動作必須人工核准 | PR Review、Environment protection rules |
| Change Review | Security 相關檔案需特定人員審核 | CODEOWNERS：`.trivyignore*`、`trivy*.yaml`、`.github/workflows/` |
| Audit Log | 記錄 Agent 執行的指令與結果 | CI log、Agent session log、PR 描述 |
| Security Policy | Agent 遵守企業 Policy | AGENTS.md、附錄 F |
| Exception Management | Agent 只能產生草稿 | Exception 系統權限只給 Security Team |
| Reproducible Scan | 結果可重現 | 固定 Trivy 版本、記錄 DB 日期 |
| Immutable Artifact | 掃描對象 = 部署對象 | 以 digest 掃描與部署 |
| SBOM | 每個 Release 都有 SBOM | CI 自動產生並保存 |
| Evidence Retention | 掃描證據保存 | Artifact 保存期限依稽核要求 |

### 30.2 CODEOWNERS 範例

```text
# .github/CODEOWNERS
/.trivyignore            @corp/devsecops
/.trivyignore.yaml       @corp/devsecops
/trivy.yaml              @corp/devsecops
/trivy-secret.yaml       @corp/devsecops
/.github/workflows/       @corp/platform @corp/devsecops
/deploy/                 @corp/platform
```

### 30.3 Guardrail 架構

```mermaid
flowchart LR
    AG["AI Agent<br/>受限權限"] --> PR["Pull Request"]
    PR --> CO["CODEOWNERS<br/>Security 檔案需 DevSecOps 審核"]
    PR --> CI["CI Trivy Gate<br/>中央設定"]
    CI --> BP["Branch Protection<br/>Required Checks"]
    CO --> BP
    BP --> HM["Human Approval"]
    HM --> MG["Merge"]
    CI --> EV["Evidence<br/>報告 / SBOM / 版本"]
```

### 30.4 MCP Server Guardrail

第 26.4 節的 Trivy MCP Server 讓 Agent 可以自行觸發掃描，也因此增加新的攻擊面。以下為 **【企業建議】**：

| Guardrail | 作法 | 理由 |
|-----------|------|------|
| 固定 plugin 版本 | `trivy plugin install mcp@v0.0.20`，升級走變更流程 | plugin 本身也是供應鏈元件（2026-03 事件教訓） |
| 指定 Trivy 執行檔 | `--trivy-binary` 指向已驗章的企業版本 | 避免使用 PATH 上未知來源的 Trivy |
| 只用 stdio | IDE 整合一律 `stdio`；必須用網路傳輸時只綁 `localhost` | 官方說明 `0.0.0.0` 會允許任何網路介面連線 |
| 不啟用 Aqua Platform | 除非企業已採購並核准，不使用 `-a` | 避免未核准的外部資料傳輸與憑證放在開發機 |
| 資料來源指向內部 Mirror | 全域 `trivy.yaml` 設定 `db.repository` | 與 CI 使用相同 DB，結果可比較 |
| Secret 不進對話 | 要求 Agent 只回報 RuleID 與位置（附錄 F） | MCP 回傳內容會進入 LLM 上下文 |
| 不取代 Gate | MCP 結果不可作為「已通過安全檢查」的證據 | 參數由 Agent 決定，無法保證與 Gate 一致 |
| 檢核工具允許清單 | 企業若以 MCP Registry / 允許清單管理 MCP Server，需將 trivy-mcp 列入並標示版本 | 避免開發者自行安裝未審核的 MCP Server |

### 實務案例

某組織允許 AI Agent 直接 push 到 feature branch，但 `main` 受 branch protection 保護，Required checks 包含 `trivy-gate`，且 CODEOWNERS 指定 workflow 與 ignore 檔必須由 DevSecOps 審核。半年內 AI Agent 提出的 PR 中有 14 次試圖修改 ignore 檔，全部在 Review 階段被攔下。

### 注意事項

- Guardrail 的核心是「技術控制」而非「Prompt 約束」。Prompt 可以被誤解或繞過，branch protection 不會。
- Agent 的執行環境也要防範第 14 章所述的供應鏈攻擊：Agent 使用的 Trivy 同樣必須驗章。

---

## 31. Trivy + SSDLC

### 31.1 SSDLC 階段對應

| SSDLC Phase | Trivy 用途 | 主要指令 / 產出 | 負責角色 |
|-------------|-----------|----------------|----------|
| Requirement | 定義 Security Requirement：SBOM、License 政策、Gate 門檻 | 需求文件中的安全驗收條件 | SA、Security |
| Architecture | IaC / Cloud 設計檢查 | `trivy config` 審查 Terraform 範本、Helm Chart | Architect |
| Development | Dependency / Secret | `trivy fs`、pre-commit secret scan | Developer、AI Agent |
| Build | Container / SBOM | `trivy image`、`--format cyclonedx` | DevOps |
| Test | Vulnerability Gate | CI Security Gate | DevSecOps |
| Deploy | Kubernetes 設定 | `trivy config`、Staging `trivy k8s` | Platform |
| Operations | Continuous Scan | Trivy Operator、每日 `trivy sbom` | SRE、Security |
| Maintenance | CVE Monitoring | SBOM 重掃、告警 | Security |
| Upgrade | Before / After Scan | 第 25 章流程 | Developer、AI Agent |

```mermaid
flowchart LR
    R["Requirement"] --> A["Architecture"]
    A --> D["Development"]
    D --> B["Build"]
    B --> T["Test"]
    T --> DP["Deploy"]
    DP --> O["Operations"]
    O --> M["Maintenance"]
    M --> U["Upgrade"]
    U --> D
    A -.-> TC["trivy config"]
    D -.-> TF["trivy fs"]
    B -.-> TI["trivy image + SBOM"]
    T -.-> G["Security Gate"]
    DP -.-> TK["trivy config / k8s"]
    O -.-> OP["Operator"]
    M -.-> SB["trivy sbom"]
```

### 實務案例

某專案在需求階段就把「每個 Release 必須附 CycloneDX SBOM、不得有 CRITICAL fixed 弱點」寫進驗收條件，PM 在 Sprint Review 時直接以 CI 產出的 SBOM 與 Gate 報告作為驗收證據，安全不再是上線前才臨時處理的事項。

### 注意事項

- Trivy 只覆蓋 SSDLC 中的「偵測」環節；威脅建模、安全設計審查、滲透測試仍需其他活動。

---

## 32. Trivy + Clean Architecture

### 32.1 Trivy 能檢查什麼

以 Clean Architecture 四層為例：

| 層 | 內容 | Trivy 可檢查 |
|----|------|-------------|
| Domain | 業務實體、規則 | 幾乎無（純程式碼，無外部相依時） |
| Application | Use Case | 相依函式庫弱點 |
| Adapter | Controller、Repository 實作 | 相依函式庫弱點、設定檔 Secret |
| Infrastructure | DB、MQ、外部 API、Dockerfile、K8s | 相依、Dockerfile、IaC、Secret、License |

| 項目 | Trivy |
|------|-------|
| Dependencies | ✓ |
| Build Artifacts | ✓ |
| Dockerfile | ✓ |
| IaC | ✓ |
| Secrets | ✓ |
| Licenses | ✓ |
| SBOM | ✓ |
| **Layer Dependency（Domain 不可依賴 Infrastructure）** | **✗ Trivy 不負責** |

> **Trivy 不負責驗證 Clean Architecture Layer Dependency。** 請使用 ArchUnit 等架構測試工具。

### 32.2 四種品質的組合

```mermaid
flowchart TB
    Q1["Architecture Quality<br/>ArchUnit"] --> Q["整體品質"]
    Q2["Code Quality<br/>Unit / Integration Test、Lint"] --> Q
    Q3["Security Quality<br/>SAST、DAST"] --> Q
    Q4["Supply Chain Security<br/>Trivy：SCA、Secret、IaC、SBOM"] --> Q
```

```java
// ArchUnit 範例：Domain 層不可依賴 Infrastructure 層（Trivy 無法做到這件事）
@AnalyzeClasses(packages = "com.example.order")
class LayerRulesTest {
    @ArchTest
    static final ArchRule domainIsIndependent =
        noClasses().that().resideInAPackage("..domain..")
            .should().dependOnClassesThat().resideInAPackage("..infrastructure..");
}
```

### 實務案例

某 AI Agent 為了修一個 Trivy 回報的 Jackson 弱點，在 Domain 層直接 import 了新版 Jackson 的 annotation。Trivy Re-scan 通過（弱點已修），但 ArchUnit 測試失敗（Domain 依賴了框架）。兩種工具互補，缺一不可。

### 注意事項

- 不要把 Trivy 報告當成架構審查報告。

---

## 33. Trivy + OWASP

### 33.1 OWASP Top 10 能力對照

以下以 OWASP Top 10:2025 分類為例（分類名稱以 OWASP 官方公布為準）：

| OWASP 類別 | Trivy 能力 | 覆蓋程度 | 需搭配 |
|-----------|-----------|---------|-------|
| A01 Broken Access Control | K8s RBAC、IaC IAM 過寬 | 部分（基礎設施層） | SAST、DAST、滲透測試 |
| A02 Security Misconfiguration | Dockerfile、K8s、Terraform、Helm | **主要** | Runtime 檢查 |
| A03 Software Supply Chain Failures | SCA、SBOM、VEX、License | **主要** | 簽章、Attestation、Provenance |
| A04 Cryptographic Failures | IaC 加密設定、crypto scanner 盤點憑證（Experimental） | 部分 | SAST、設計審查 |
| A05 Injection | ✗ | 無 | SAST、DAST |
| A06 Insecure Design | ✗ | 無 | 威脅建模 |
| A07 Authentication Failures | Secret 外洩偵測 | 間接 | DAST、滲透測試 |
| A08 Software or Data Integrity Failures | SBOM、Attestation 掃描 | 部分 | 簽章驗證、CI 安全 |
| A09 Logging & Alerting Failures | IaC 日誌設定（例如雲端資源未啟用 logging） | 部分 | 監控平台 |
| A10 Mishandling of Exceptional Conditions | ✗ | 無 | SAST、Code Review |

### 33.2 必須明確區分的六類問題

| 類型 | Trivy 是否處理 |
|------|---------------|
| Dependency Vulnerability | ✓ |
| Secret | ✓ |
| Misconfiguration | ✓ |
| SAST（自有程式碼漏洞） | ✗ |
| DAST（執行期漏洞） | ✗ |
| Business Logic（業務邏輯漏洞） | ✗ |

> **不要宣稱 Trivy 可以取代完整 OWASP Security Testing。**

### 實務案例

某團隊的安全報告寫「已使用 Trivy 完成 OWASP Top 10 檢測」，外部稽核指出 Injection 與 Access Control 完全沒有測試證據。修正後報告改為「Trivy 覆蓋 A02、A03 主要風險，其餘以 SAST、DAST 與滲透測試補足」。

### 注意事項

- OWASP 分類版本會更新，對照表需隨之調整。

---

## 34. Trivy + SAST / DAST / SCA

### 34.1 工具定位比較

| 工具類型 | 主要目的 | Trivy |
|----------|----------|-------|
| SAST | Source Code 邏輯漏洞 | 部分能力（IaC、Secret）／不等同完整 SAST |
| DAST | Running Application | 非主要定位 |
| SCA | Dependency | Trivy 可執行 |
| Secret Scanner | Credential | Trivy 可執行 |
| IaC Scanner | Configuration | Trivy 可執行 |
| Container Scanner | Image | Trivy 核心能力 |
| SBOM | Inventory | Trivy 可產生、可掃描 |
| CSPM | Cloud | 視目前版本能力：AWS 需 plugin，非完整 CSPM |

### 34.2 工具組合架構

```mermaid
flowchart LR
    subgraph Code["程式碼"]
        SAST["SAST"]
        SEC["Secret - Trivy"]
    end
    subgraph Deps["相依"]
        SCA["SCA - Trivy"]
        SBOM["SBOM - Trivy"]
    end
    subgraph Build["建置產物"]
        IMG["Image - Trivy"]
        IAC["IaC - Trivy"]
    end
    subgraph Run["執行期"]
        DAST["DAST"]
        RT["Runtime / Operator"]
    end
    Code --> Deps --> Build --> Run
```

### 34.3 結果彙整與去重

多工具並存時，最常見的問題是「同一個弱點在三個儀表板出現三次」。**【企業建議】** 以下為彙整原則：

| 項目 | 建議 |
|------|------|
| 交換格式 | 掃描工具統一輸出 SARIF 2.1.0（Trivy `--format sarif`），SBOM 統一 CycloneDX |
| 去重鍵 | Vulnerability：CVE / GHSA + PURL + 資產（映像 digest 或 repo）；Misconfiguration：Check ID + 檔案 + 資源 |
| Fingerprint | Trivy v0.68 起在報告中提供弱點 fingerprint、ReportID、ArtifactID，可作為追蹤與去重的輔助欄位 |
| 單一 Owner | 每筆 Finding 只有一個負責團隊，由資產標籤決定 |
| 權威來源 | SCA 以單一工具為 Gate 依據，其他工具只作交叉比對 |

### 34.4 選型建議

| 情境 | 建議組合 |
|------|----------|
| 初始導入（預算有限） | Trivy（SCA / Secret / IaC / Image / SBOM）+ 開源 SAST |
| 金融 / 高合規 | Trivy + 商用 SAST + DAST + 定期滲透測試 + 弱點管理平台 |
| 大量容器化系統 | Trivy CLI（CI Gate）+ Trivy Operator（Runtime）+ Admission Controller |
| AI Agent 大量產碼 | Trivy CLI Gate + SAST + 第 30 章 Guardrail；Trivy MCP 僅作開發回饋 |

### 實務案例

某金融業 AppSec 平台的工具組合：SAST 負責自有程式碼、Trivy 負責 SCA / Secret / IaC / Image / SBOM、DAST 每週掃 Staging、每年兩次外部滲透測試。四類結果彙整到同一個弱點管理平台，以 CWE 與資產標籤去重。

### 注意事項

- 多工具同時做 SCA 時，Finding 會重複，需在弱點管理平台以 CVE + 套件 + 資產去重。

---

## 35. Enterprise DevSecOps Reference Architecture

### 35.1 架構圖

```mermaid
flowchart TB
    DEV["Developer"] --> GIT["Git Repository"]
    AI["AI Agent"] --> GIT
    GIT --> CI["CI/CD"]
    CI --> TR["Trivy Repo / FS"]
    CI --> TC["Trivy Config"]
    CI --> BLD["Build"]
    BLD --> TI["Trivy Image"]
    TI --> SB["SBOM"]
    TR & TC & TI & SB --> GATE{"Security Gate"}
    GATE -->|"Pass"| REG["Container Registry<br/>SBOM Attestation"]
    REG --> K8S["Kubernetes"]
    K8S --> OP["Trivy Operator"]
    K8S --> CLOUD["Cloud"]
    OP --> SIEM["SIEM / 弱點管理平台"]
    CI --> SIEM
    MIR[("內部 DB Mirror")] -.-> CI
    MIR -.-> OP
```

### 35.2 元件職責

| 元件 | 職責 | 擁有者 |
|------|------|--------|
| Git Repository | 原始碼、IaC、ignore 檔 | 開發團隊 |
| CI/CD | 執行掃描與 Gate | Platform |
| Trivy 中央設定 | `trivy.yaml`、`trivy-secret.yaml` | DevSecOps |
| DB Mirror | 內部弱點資料來源 | Platform |
| Registry | 映像檔與 SBOM / Attestation | Platform |
| Trivy Operator | 叢集持續掃描 | Platform / SRE |
| SIEM / 弱點平台 | 彙整、告警、追蹤 | Security |

### 實務案例

某集團以此架構在 6 個月內把 300 個 repo 納入掃描，關鍵在於 CI 使用中央的 reusable workflow，各團隊只需在 repo 中加入 5 行呼叫。

### 注意事項

- Reference Architecture 是起點，不是終點；應依企業網路分區、合規要求調整。

---

## 36. Banking / Enterprise Environment

### 36.1 金融業環境特性與對策

| 環境特性 | 挑戰 | Trivy 對策 |
|----------|------|-----------|
| Internet Restricted | 無法下載 DB | 內部 Mirror、`--db-repository` |
| Proxy | TLS 攔截 | `HTTPS_PROXY`、`--cacert` |
| Private Registry | 認證 | `trivy registry login`、`TRIVY_USERNAME` / `TRIVY_PASSWORD`（Secret Manager 提供） |
| Air-Gapped | 完全離線 | ORAS 匯出匯入、`--skip-*-update`、`--offline-scan` |
| Internal GitLab | 自架 CI | GitLab CI 範本 + 內部 Trivy 映像 |
| GitHub Enterprise | GHES token 差異 | trivy-action `token-setup-trivy`，或預裝 Trivy |
| IBM / Linux / AIX Legacy | 無 AIX 執行檔 | 產物複製至 Linux 掃描；Linux on ppc64le / s390x 有官方執行檔 |
| Kubernetes / OpenShift | 安全限制（SCC） | Operator 依平台調整安全設定 |
| Database | 預存程序、DB 設定 | Trivy 不涵蓋，需 DB 專用工具 |
| MQ | IBM MQ 設定 | Trivy 不涵蓋 MQ 設定檢查 |
| API Gateway | 閘道設定 | 若以 IaC 管理可部分檢查 |
| Enterprise CI/CD | 多平台 | 統一 Trivy 版本與中央設定 |
| Security Audit | 證據保存 | 保存報告、SBOM、版本紀錄 |

### 36.2 金融業導入流程

```mermaid
flowchart LR
    A["資安單位核准工具"] --> B["建立內部 Mirror 與驗章流程"]
    B --> C["試點系統"]
    C --> D["訂定 Gate 與 Exception 政策"]
    D --> E["擴大至所有系統"]
    E --> F["納入內稽 / 外稽證據"]
```

### 實務案例

某銀行的資安單位要求所有開源安全工具必須「可驗證來源、可離線運作、可留存證據」。Platform Team 以 cosign 驗證 Trivy Release、以 Harbor 同步 DB、每次掃描保存 `trivy --version` 與 JSON 報告 7 年，順利通過工具導入審查。

### 注意事項

- 2026-03 事件後，金融業應把「掃描工具本身的供應鏈」列入第三方風險管理。
- Trivy 預設會送出匿名使用資料（Usage Telemetry），可用 `--disable-telemetry` 關閉；離線與高合規環境建議關閉。

---

## 37. GitHub / GitLab Enterprise Governance

### 37.1 治理層級

```mermaid
flowchart TB
    O["Organization<br/>政策、Action 白名單、SHA pin 要求"] --> R["Repository<br/>CODEOWNERS"]
    R --> B["Branch Protection / Ruleset<br/>Required checks"]
    B --> C["CI/CD<br/>Reusable workflow / CI template"]
    C --> T["Trivy<br/>中央設定"]
    T --> G["Security Gate"]
    G --> E["Exception<br/>Security 核准"]
    E --> A["Audit<br/>報告保存"]
```

### 37.2 關鍵機制

| 機制 | GitHub | GitLab | 目的 |
|------|--------|--------|------|
| Policy as Code | Rulesets、Required workflows | Compliance pipelines、Security policies | 強制所有 repo 執行掃描 |
| Central Configuration | 中央 repo 存放 `trivy.yaml` | 中央專案的 CI template | 單一來源 |
| Reusable Pipeline | `workflow_call` reusable workflow | `include:` CI template | 一致性 |
| Security Baseline | Org 層級 Required checks | Group 層級設定 | 最低標準 |
| Report Retention | Artifact retention、外部保存 | Artifact expiry、外部保存 | 稽核 |

### 37.3 Reusable Workflow 範例

```yaml
# corp/security-workflows/.github/workflows/trivy.yml
name: trivy-reusable
on:
  workflow_call:
    inputs:
      image-ref:
        type: string
        required: false
permissions:
  contents: read
jobs:
  scan:
    runs-on: ubuntu-24.04
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@<SHA> # v4
      - uses: actions/checkout@<SHA> # v4
        with:
          repository: corp/security-config
          path: .security-config
      - uses: aquasecurity/setup-trivy@<SHA> # v0.3.1
        with:
          version: v0.75.0
          cache: true
      - run: trivy --version
      - run: trivy fs --config .security-config/trivy.yaml --format json --output trivy-fs.json .
```

```yaml
# 各應用 repo：.github/workflows/security.yml
name: security
on: [pull_request]
jobs:
  trivy:
    uses: corp/security-workflows/.github/workflows/trivy.yml@<SHA>
    permissions:
      contents: read
      security-events: write
```

### 實務案例

某組織原本每個 repo 自行撰寫 Trivy workflow，版本從 v0.4x 到 v0.6x 都有。改為 reusable workflow 後，Trivy 升級只需修改一處，2026-03 事件時也只需在中央 repo 更新 SHA pin。

### 注意事項

- Reusable workflow 本身也要以 SHA 引用。
- 中央設定 repo 的寫入權限應嚴格限制。

---

## 38. Security Gate

### 38.1 Trivy Capability vs Company Policy

| 項目 | Trivy Capability（官方） | Company Policy（企業決定） |
|------|------------------------|---------------------------|
| 偵測 | Severity、Status、Fixed Version | — |
| 過濾 | `--severity`、`--ignore-unfixed`、`--ignore-status` | 哪些等級要擋 |
| 結束碼 | `--exit-code`、`--exit-on-eol` | 何時讓 Pipeline 失敗 |
| 抑制 | ignore 檔、VEX、Rego | 誰可以核准、多久到期 |

### 38.2 企業 Gate 範例

> **【企業建議】以下不是 Trivy 官方唯一標準，而是企業治理範例。**

```text
CRITICAL fixed vulnerability   → FAIL
CRITICAL unfixed vulnerability → 風險評估（48 小時內）
HIGH fixed vulnerability       → 依企業政策：Release branch FAIL；feature branch WARN
MEDIUM                         → Monitor / 排入修正
LOW                            → Track
Any Secret                     → FAIL
HIGH/CRITICAL Misconfiguration → FAIL（Production manifest）
OS EOL                         → FAIL（Release）
License Forbidden              → FAIL；Restricted → 法務審核
```

| 分支 / 階段 | Gate 強度 |
|-------------|-----------|
| feature branch | 寬鬆：只擋 Secret 與 CRITICAL fixed |
| main / develop | 標準：38.2 全部 |
| release / tag | 嚴格：加上 HIGH fixed、EOL、SBOM 必須產生 |
| Production 部署前 | 以 digest 再掃一次（DB 可能已更新） |

### 38.3 Gate 判斷流程

```mermaid
flowchart TD
    S["掃描完成"] --> SE{"Secret > 0？"}
    SE -->|"是"| F["FAIL"]
    SE -->|"否"| C{"CRITICAL fixed > 0？"}
    C -->|"是"| EX1{"有有效 Exception？"}
    EX1 -->|"否"| F
    EX1 -->|"是"| H
    C -->|"否"| H{"HIGH fixed > 0？"}
    H -->|"是，Release"| F
    H -->|"是，其他分支"| W["WARN + Ticket"]
    H -->|"否"| M{"Misconf HIGH+ > 0？"}
    W --> M
    M -->|"是"| F
    M -->|"否"| P["PASS"]
```

### 實務案例

某團隊一開始在所有分支都用最嚴格的 Gate，開發者抱怨 feature branch 無法推進。改為分支分級後，feature branch 的回饋仍然即時，而 release branch 維持嚴格，兩個月內 Gate 被要求例外的次數減少一半。

### 注意事項

- Gate 規則必須版本化並公告；變更需經 Security Team 核准。
- Production 部署前的再掃描很重要：映像檔不變，但 DB 每天都在更新。

---

## 39. False Positive / Exception Management

### 39.1 名詞區分

| 名詞 | 意義 | 處理方式 |
|------|------|----------|
| False Positive | 掃描器誤判（例如版本辨識錯誤） | 提供證據、Security 確認、Ignore（可無到期日） |
| Accepted Risk | 真實弱點，但經評估接受 | Exception，必須有到期日與補償控制 |
| VEX | 標準化的「不受影響」聲明 | `--vex` 載入，可對外分享 |
| Ignore | Trivy 的抑制機制 | `.trivyignore*` |
| Suppression | 抑制的總稱（Ignore、VEX、Rego） | `--show-suppressed` 檢視 |
| Expiration | 到期日 | `exp:` / `expired_at` |
| Owner | 負責追蹤的人或團隊 | 寫入 Exception 記錄 |
| Review | 定期重新評估 | 每月 / 到期前 |

### 39.2 Exception Record 範例

```yaml
exception_id: SEC-EXC-2026-014
finding:
  type: vulnerability
  id: CVE-2025-12345
  package: org.example:legacy-lib
  installed_version: 1.2.3
  fixed_version: null
  target: order-service:1.4.2 (sha256:<digest>)
  severity: CRITICAL
owner: team-order (tech-lead@example.com)
reason: 上游尚無修補版本；此套件僅用於內部批次匯出功能
risk: 中 —— 攻擊需要已驗證的內部使用者觸發
approved_by: security-team (ciso-delegate@example.com)
created_at: 2026-10-03
expires_at: 2026-11-02
compensating_control:
  - API Gateway 限制該端點僅內網可存取
  - WAF 規則 RULE-2231 阻擋已知攻擊特徵
review_schedule: 每 2 週檢查上游是否釋出修補
trivy_ignore_entry: ".trivyignore.yaml vulnerabilities[id=CVE-2025-12345]"
status: approved
```

### 39.3 Exception 生命週期

```mermaid
stateDiagram-v2
    [*] --> Draft: Developer / AI Agent 草擬
    Draft --> UnderReview: 提交
    UnderReview --> Approved: Security 核准
    UnderReview --> Rejected: 退回
    Approved --> Active: 加入 ignore / VEX
    Active --> Expired: 到期
    Active --> Closed: 已修正
    Expired --> UnderReview: 重新申請
    Closed --> [*]
    Rejected --> [*]
```

### 39.4 VEX 範例（OpenVEX）

```json
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "https://example.com/vex/order-service-2026-014",
  "author": "Security Team <security@example.com>",
  "timestamp": "2026-10-03T00:00:00Z",
  "version": 1,
  "statements": [
    {
      "vulnerability": { "name": "CVE-2025-12345" },
      "products": [
        { "@id": "pkg:oci/order-service@sha256%3A<digest>" }
      ],
      "status": "not_affected",
      "justification": "vulnerable_code_not_in_execute_path",
      "impact_statement": "受影響的類別未被載入，經 SEC-EXC-2026-014 分析確認"
    }
  ]
}
```

```bash
trivy image --vex ./vex/order-service.openvex.json --show-suppressed registry.internal.example.com/order-service@sha256:<digest>
```

> VEX 的 product 與 subcomponent 識別碼需與 Trivy 偵測到的 PURL 相符，撰寫前請先以 JSON 報告確認 PURL。

### 實務案例

某團隊把所有「無修補版本」的 CRITICAL 都用 VEX 標成 `not_affected`，稽核時被質疑沒有分析證據。改正後規定：`not_affected` 必須附技術分析（例如呼叫鏈分析），「只是無修補」的情況屬於 Accepted Risk，走 Exception 流程並設到期日。

### 注意事項

- VEX `not_affected` 是技術聲明，Accepted Risk 是管理決策，兩者不可混用。
- AI Agent 可以草擬 Exception 與 VEX，但**不得**提交核准。

---

## 40. Trivy 維運

### 40.1 維運範圍

| 項目 | 內容 | 負責 |
|------|------|------|
| Version Upgrade | Trivy、trivy-action、setup-trivy、Operator | Platform |
| Database Update | trivy-db、java-db、checks bundle 同步 | Platform |
| Cache | 容量、清理、權限 | Platform |
| Configuration | 中央 `trivy.yaml`、`trivy-secret.yaml` | DevSecOps |
| Rule Update | 自訂 Rego、License 分類 | DevSecOps |
| CI/CD Maintenance | Reusable workflow、SHA pin | Platform |
| Registry | 內部 Mirror、認證 | Platform |
| Proxy | 例外清單、CA 更新 | Network / Platform |
| Monitoring | DB 年齡、掃描成功率、時間 | SRE |
| Log | 掃描 Log 保存（不含 Secret） | SRE |
| Backup | 中央設定、Exception 記錄 | DevSecOps |
| Audit | 報告、SBOM、版本紀錄 | Security |

### 40.2 維運 Checklist

#### Daily

- [ ] DB Mirror 同步成功，DB 年齡低於門檻
- [ ] 前一日 CI 掃描成功率正常
- [ ] Trivy Operator 運作正常、無卡住的 Scan Job
- [ ] Production SBOM 重掃完成，新增 CRITICAL 已通知 Owner
- [ ] 檢查 Trivy GitHub Security Advisories 是否有新公告

#### Weekly

- [ ] 檢視即將到期（7 日內）的 Exception
- [ ] 檢視 CI 平均掃描時間是否異常上升
- [ ] Cache 容量檢查與清理
- [ ] 檢查 trivy-action / setup-trivy 是否有新版（Dependabot / Renovate PR）

#### Monthly

- [ ] 評估 Trivy 新版本 Release Notes 與 BREAKING CHANGES
- [ ] KPI 報告（第 58 章）
- [ ] 隨機抽查 10 個 repo 的 ignore 檔是否符合治理規則
- [ ] 檢查 Trivy Operator 報告 CRD 數量與 etcd 使用量

#### Quarterly

- [ ] 依第 41 章執行 Trivy 升級
- [ ] 檢視並更新 Gate 規則與 License 分類
- [ ] 演練 Air-gapped / Mirror 失效時的應變
- [ ] 本手冊 Technical Review

### 實務案例

某團隊沒有監控 DB 年齡，Mirror 同步因 Proxy 憑證更新失敗了 19 天，期間所有掃描都使用舊 DB，「0 CRITICAL」的報告其實是假象。加入 Daily 第一項後，同步失敗會在數小時內被發現。

### 注意事項

- 維運責任必須明確指派，不能預設「Trivy 會自己更新」。

---

## 41. Trivy 升級策略

### 41.1 升級流程

```mermaid
flowchart LR
    A["Current Version"] --> B["Release Notes<br/>CHANGELOG / Discussions"]
    B --> C["Breaking Changes 檢查"]
    C --> D["驗章 + Test Environment"]
    D --> E["CI/CD Test<br/>代表性 repo"]
    E --> F["Scan Baseline 比較<br/>新舊版結果差異"]
    F --> G["Production Rollout<br/>中央 workflow 更新"]
    G --> H["觀察期"]
```

### 41.2 升級類型

| 類型 | 定義 | 策略 |
|------|------|------|
| Minor Upgrade | 例如 v0.74 → v0.75 | 每季一次；跳過不超過 2 個 minor 為宜 |
| Major Upgrade | Trivy 目前仍為 0.x，每個 minor 都可能含 Breaking；未來 1.0 時需重新評估 | 依 CHANGELOG 的 BREAKING CHANGES 處理 |
| Emergency Upgrade | Trivy 自身有安全公告（例如 GHSA-mcj4-mphf-j9ff 路徑穿越、GHSA-8rc5-4fr6-64pw plugin 路徑穿越） | 48 小時內評估、7 日內完成 |
| Security Fix | Patch 版（例如 v0.71.1、v0.71.2） | 優先套用 |
| Rollback | 新版造成大量誤報或 CI 失敗 | 中央 workflow 改回前一版 SHA；**不得 rollback 到已知惡意版本（v0.69.4）** |

### 41.3 升級前檢查清單

| 檢查 | 範例（v0.74 → v0.75） |
|------|----------------------|
| BREAKING CHANGES | 自訂 template 是否使用 `getHostByName` |
| 新功能是否影響結果 | uv workspace 相依不再被視為 dev → Python 專案 Finding 可能增加 |
| 行為變更 | License 無法解析時改以 UNKNOWN 報告 → License Finding 可能增加 |
| 設定鍵 | `--generate-default-config` 比較新舊版 |
| 驗章 | cosign verify-blob / verify |
| Release 屬性 | GitHub Release 標示為 Immutable |

### 41.4 新舊版結果比較

```bash
# 同一 DB、同一目標，以新舊兩版 Trivy 掃描
/opt/trivy/0.74.0/trivy image --skip-db-update --format json --output old.json registry.internal.example.com/app:1.4.2
/opt/trivy/0.75.0/trivy image --skip-db-update --format json --output new.json registry.internal.example.com/app:1.4.2
python trivy_diff.py old.json new.json
```

> 差異應可由 Release Notes 解釋；無法解釋的差異需回報 Trivy 社群或延後升級。

### 實務案例

v0.69 將 misconf provider mapping 改用 ID（Breaking）。某團隊的自訂 Rego 規則在升級後全部失效，CI 卻顯示「0 misconfiguration」。因為有 41.4 的新舊版比較，升級前就發現了這個落差。

### 注意事項

- 升級 Trivy 也要同步升級 trivy-action 的 `version` input、Operator 內建的 Trivy 版本與 Server 模式的 Server。
- 2026-03 事件的教訓：**新版發布當天不要直接自動升級**；保留觀察期並以 Immutable Release + 驗章確認。

---

## 42. Trivy 升級對 AI Agent 的要求

### 42.1 十一個必要步驟

**【AI Agent 流程】** AI Agent 執行 Trivy 升級時必須：

| 步驟 | 要求 | 產出 |
|------|------|------|
| 1 | 查詢目前版本 | `trivy --version` 輸出 |
| 2 | 查詢目標版本 | GitHub Release 連結、發布日、是否 Immutable |
| 3 | 閱讀 Changelog | 涵蓋目前版本到目標版本之間**所有**版本 |
| 4 | 檢查 Breaking Changes | 逐條判斷是否影響本組織（template、Rego、flag） |
| 5 | 建立 Before Baseline | 以舊版掃描代表性目標 |
| 6 | 執行 Upgrade | 修改中央 workflow / Runner 映像的版本與 SHA；驗章 |
| 7 | 執行 Scan | 以新版、相同 DB 掃描相同目標 |
| 8 | 比較結果 | trivy_diff.py |
| 9 | 執行 Tests | CI 範本測試、Gate 腳本測試 |
| 10 | 產生 Upgrade Report | 版本、Breaking 影響、結果差異與解釋 |
| 11 | 等待 Human Review | 不得自行合併 |

### 42.2 Upgrade Report 範本

```text
【Upgrade Report 範本】
- Current: v0.74.0 → Target: v0.75.0（2026-10-01，Immutable Release，cosign 驗章 OK）
- Breaking: getHostByName 移除 → 本組織 3 個自訂 template 均未使用（已 grep 確認）
- 行為變更: License 無法解析改為 UNKNOWN → 預期 License Finding 增加
- 結果差異: 12 個代表性 repo；Vulnerability 無差異；License UNKNOWN +7（可由行為變更解釋）
- 測試: reusable workflow 測試通過
- 待人工確認: 是否接受 License UNKNOWN 增加
```

### 42.3 升級工作的範圍與禁止事項

| 項目 | 必須同步檢查 | 禁止 |
|------|--------------|------|
| CLI / Runner 映像 | 版本、cosign 驗章、Immutable Release | 使用 `latest`、發布當天的版本直接上 Production |
| trivy-action | `version` input（不指定會退回 action 內建預設值） | 改成 mutable tag |
| setup-trivy | Action 版本與 SHA；是否使用自訂 `path` | 升到 v0.3.0 |
| Operator / Server | 內建 Trivy 版本、Helm Chart 版本 | 在同一 PR 內變更 Gate 門檻 |
| MCP plugin | `trivy plugin install mcp@<version>` 是否需跟進 | 未經核准自行升級 plugin |
| 設定與範本 | `--generate-default-config` 差異、自訂 template、Rego | 修改 ignore 檔、scanners、severity |

### 實務案例

某 AI Agent 被要求「把 Trivy 升到最新」，第一版只改了版本號。依本章要求重做後，Agent 發現組織內有一個自訂 HTML template 使用 `getHostByName`，在報告中提出修正建議，避免升級當天所有 HTML 報告產生失敗。

### 注意事項

- AI Agent 不得在 Trivy 升級 PR 中同時修改 Gate 門檻或 ignore 檔。

---

## 43. Performance Optimization

### 43.1 優化手段

| 手段 | 作法 | 效果 |
|------|------|------|
| Cache | 持久化 `--cache-dir`；CI cache | 避免重複分析映像層與下載 DB |
| DB Reuse | 排程預熱 + `--skip-db-update` | 省去每次下載 |
| CI Cache | trivy-action `cache: true` | 同上 |
| Parallelism | `--parallel`（預設 5；0 為自動） | 加速大型目標 |
| Skip Files / Dirs | `--skip-dirs "**/node_modules,**/test/**"` | 減少掃描檔案數 |
| Scan Scope | 明確 `--scanners`；`trivy config` 只掃 `deploy/` | 避免不必要的 Scanner |
| Registry Optimization | 使用內部 Registry / Mirror；`--image-src remote` 避免本機 export | 降低網路延遲 |
| Large Image | `--max-image-size`（Experimental）設上限 | 防止異常大映像拖垮 Runner |
| Large Repository | 分模組掃描、只掃變更的模組 | 縮短 PR 回饋時間 |
| Client/Server | 集中 DB | 多 Runner 共用 |
| Redis Cache | `--cache-backend redis://`（Experimental） | 多 Runner 共用分析結果 |
| Secret 掃描 | v0.75 改為單次 Aho-Corasick 比對 | 升級即可獲得效能改善 |

### 43.2 大型企業降低 CI 影響的做法

```mermaid
flowchart LR
    A["PR"] --> B["快速掃描<br/>fs: vuln + secret<br/>只掃變更模組"]
    B --> C["Merge to main"]
    C --> D["完整掃描<br/>fs + image + config + SBOM"]
    D --> E["Release"]
    E --> F["嚴格 Gate + digest 再掃"]
    G["每日排程"] --> H["SBOM 重掃<br/>不阻擋開發"]
```

### 實務案例

某 monorepo 有 40 個模組，完整 `trivy fs` 需 12 分鐘。改為 PR 只掃描變更模組、`--skip-dirs` 排除測試資料、DB 預熱後，PR 掃描降到 90 秒，完整掃描移到 merge 後執行。

### 注意事項

- 為了速度而停用 Scanner 是「Gate 弱化」，必須經 DevSecOps 核准。
- `--skip-dirs` 不可排除含有部署產物或設定檔的目錄。

---

## 44. Troubleshooting

### 44.1 DB Download Failure

| 欄位 | 內容 |
|------|------|
| Problem | `failed to download vulnerability DB` |
| Cause | 無法連線 `mirror.gcr.io` / `ghcr.io`、速率限制、Proxy 阻擋 |
| Check | `trivy image --download-db-only --debug`；確認 `HTTPS_PROXY`、DNS |
| Solution | 設定 `--db-repository` 指向內部 Mirror；或多個來源依序嘗試 |
| Prevention | 建立 Mirror + DB 年齡監控（第 17 章） |

### 44.2 Network Failure

| 欄位 | 內容 |
|------|------|
| Problem | 掃描過程逾時或連線中斷 |
| Cause | Registry 不穩、網路分區限制 |
| Check | `--debug` 查看卡在哪個請求 |
| Solution | 提高 `--timeout`；改用內部 Registry |
| Prevention | CI Runner 與 Registry 同網段 |

### 44.3 Proxy

| 欄位 | 內容 |
|------|------|
| Problem | 透過 Proxy 時 TLS 錯誤 |
| Cause | Proxy 進行 TLS 攔截，使用企業 CA |
| Check | `curl -v https://ghcr.io` 檢查憑證鏈 |
| Solution | `--cacert <corp-ca.pem>`；設定 `NO_PROXY` 排除內部 Registry |
| Prevention | 企業 CA 預裝於 Runner 映像 |

### 44.4 Certificate

| 欄位 | 內容 |
|------|------|
| Problem | `x509: certificate signed by unknown authority` |
| Cause | 內部 Registry 使用自簽或企業 CA |
| Check | 確認 CA 檔案路徑與格式（PEM） |
| Solution | `--cacert`；**不要**用 `--insecure` |
| Prevention | 統一 CA 派送 |

### 44.5 Registry Authentication

| 欄位 | 內容 |
|------|------|
| Problem | `UNAUTHORIZED` / `denied` |
| Cause | 未登入、Token 過期、權限不足 |
| Check | `docker pull` 是否成功；`trivy registry login` 狀態 |
| Solution | `TRIVY_USERNAME` / `TRIVY_PASSWORD`（Secret Manager 提供）、`--password-stdin`、`--registry-token` |
| Prevention | 使用短期 Token（OIDC） |

### 44.6 Docker Socket

| 欄位 | 內容 |
|------|------|
| Problem | 本機映像找不到 |
| Cause | Docker socket 未掛載或權限不足 |
| Check | `docker images` 是否看得到；`--docker-host` |
| Solution | 掛載 `/var/run/docker.sock`；或先 push 再以 `--image-src remote` 掃描 |
| Prevention | CI 統一以 Registry 掃描 |

### 44.7 Permission

| 欄位 | 內容 |
|------|------|
| Problem | Cache 目錄無法寫入 |
| Cause | 以不同使用者執行、容器 UID 不同 |
| Check | `ls -ld $TRIVY_CACHE_DIR` |
| Solution | 調整目錄權限或改用使用者專屬 cache |
| Prevention | Runner 映像預建 cache 目錄 |

### 44.8 Kubernetes Authentication

| 欄位 | 內容 |
|------|------|
| Problem | `trivy k8s` 回報 forbidden |
| Cause | ServiceAccount 缺少 `list` 權限，或 node-collector 權限不足 |
| Check | `kubectl auth can-i list pods --all-namespaces` |
| Solution | 套用第 10.3 節 ClusterRole；或 `--disable-node-collector` |
| Prevention | 專用掃描帳號、權限即程式碼 |

### 44.9 Slow Scan

| 欄位 | 內容 |
|------|------|
| Problem | 掃描時間過長 |
| Cause | 首次下載 DB、大映像、大 repo、`--license-full` |
| Check | `--debug` 觀察各階段時間 |
| Solution | 第 43 章手段 |
| Prevention | 監控 CI 掃描時間 KPI |

### 44.10 Out of Disk

| 欄位 | 內容 |
|------|------|
| Problem | `no space left on device` |
| Cause | Cache 累積、映像層暫存 |
| Check | `du -sh ~/.cache/trivy` |
| Solution | `trivy clean --scan-cache`；擴充磁碟 |
| Prevention | 定期清理排程 |

### 44.11 Large Image

| 欄位 | 內容 |
|------|------|
| Problem | 數 GB 映像掃描失敗或過慢 |
| Cause | 映像含大量不必要檔案 |
| Check | `docker history` 檢查各層大小 |
| Solution | 多階段建置瘦身；`--max-image-size` 設上限 |
| Prevention | Dockerfile 規範 |

### 44.12 False Positive

| 欄位 | 內容 |
|------|------|
| Problem | 回報的版本或套件不正確 |
| Cause | 重新打包的 jar、Vendor backport 修補未被識別 |
| Check | 比對 `InstalledVersion` 與實際；查 Vendor Advisory |
| Solution | 提供證據後以 ignore（限定 path / purl）或 VEX 處理 |
| Prevention | 向 Trivy 社群回報可重現案例 |

### 44.13 Missing Vulnerability

| 欄位 | 內容 |
|------|------|
| Problem | 已知 CVE 沒被掃出 |
| Cause | 缺 lock file、DB 過舊、套件未被辨識、`--ignore-unfixed` 過濾 |
| Check | `--list-all-pkgs`（JSON 預設 true）確認套件是否被辨識；檢查 DB 日期 |
| Solution | 補 lock file、更新 DB、移除過濾 flag 重試 |
| Prevention | SBOM 檢查元件完整度 |

### 44.14 Unexpected Severity

| 欄位 | 內容 |
|------|------|
| Problem | 同一 CVE 在不同映像 Severity 不同 |
| Cause | `SeveritySource` 不同（Vendor vs NVD） |
| Check | JSON 中 `SeveritySource`、`CVSS` |
| Solution | 視需要以 `--vuln-severity-source` 統一來源 |
| Prevention | 在 Policy 中定義 Severity 來源原則 |

### 44.15 SBOM 問題

| 欄位 | 內容 |
|------|------|
| Problem | SBOM 缺 OS 套件或缺應用相依 |
| Cause | 以 `trivy fs` 產生（無 OS 套件）；或映像中缺 metadata |
| Check | `jq '.components \| length'`；比較 fs 與 image SBOM |
| Solution | 交付用 SBOM 以最終映像產生 |
| Prevention | 第 6.9 節 SBOM 管理規範 |

### 44.16 Java Dependency 問題

| 欄位 | 內容 |
|------|------|
| Problem | Java 相依辨識不完整或掃 `pom.xml` 失敗 |
| Cause | Java DB 未下載、遠端 Maven 不可達或 429、parent POM 無法解析 |
| Check | `--download-java-db-only`；`--debug` 看 POM 解析錯誤 |
| Solution | 設定 Maven mirror（settings.xml / trivy.yaml）；改掃建置後 jar |
| Prevention | 內部 Maven mirror + Java DB Mirror |

### 實務案例

某團隊抱怨「Trivy 漏掃 Log4j」。依 44.13 檢查後發現該服務以 Ant 建置、jar 被重新命名且移除了 `META-INF/maven`，同時 CI 跳過了 Java DB 更新。恢復 Java DB 後，Trivy 以 SHA1 成功辨識出該 jar。

### 注意事項

- 回報問題給 Trivy 社群時，**不要**附上含 Secret 或內部主機名稱的完整報告。

---

## 45. 常見錯誤

### 45.1 掃描範圍錯誤

| # | 錯誤 | 後果 | 正確作法 |
|---|------|------|----------|
| 1 | 只掃 Container，不掃 Source Code | 看不到 lock file 中未打包進映像的風險、Secret、IaC | `trivy fs` + `trivy image` 都要 |
| 2 | 只掃 Vulnerability | 忽略 Secret、Misconfiguration、License | 明確 `--scanners` |
| 3 | 不產生 SBOM | 新 CVE 爆發時無法快速盤點 | 每個 Release 產生 SBOM |
| 10 | 把 Trivy 當完整 SAST | 自有程式碼漏洞無人檢查 | 搭配 SAST |
| 11 | 把 Trivy 當 DAST | 執行期漏洞無人檢查 | 搭配 DAST |

### 45.2 資料與效能錯誤

| # | 錯誤 | 後果 | 正確作法 |
|---|------|------|----------|
| 5 | 不更新 DB | 掃描結果過時 | Mirror + 年齡監控 |
| 6 | CI/CD 每次重新下載 DB | 慢、被限流 | 快取與預熱 |

### 45.3 治理錯誤

| # | 錯誤 | 後果 | 正確作法 |
|---|------|------|----------|
| 4 | 永久 Ignore | 風險無人追蹤 | 必須有到期日 |
| 7 | 只看 CRITICAL | 大量 HIGH 長期累積 | 分級處理（第 5.8 節） |
| 8 | 忽略 Secret | 憑證外洩 | Secret 一律 Fail + 輪替 |
| 9 | 忽略 License | 法律風險 | 啟用 license scanner + 法務流程 |
| 12 | 讓 AI Agent 自動接受所有 Finding | Gate 形同虛設 | 第 29 章禁止清單 |
| 13 | 沒有 Exception Owner | 例外無人負責 | 必填 Owner |
| 14 | 沒有 Expiration | 例外變成永久 | 必填到期日 |
| 15 | 不做 Upgrade Regression Scan | 新引入風險被整體改善掩蓋 | 第 25 章 Before / After |

### 45.4 供應鏈與版本錯誤

| # | 錯誤 | 後果 | 正確作法 |
|---|------|------|----------|
| 16 | 以 mutable tag 引用 trivy-action / setup-trivy | 2026-03 事件的主要受害方式 | 完整 SHA pin |
| 17 | 使用 `latest` Trivy 版本 | 惡意或未驗證版本直接進入 CI | 固定版本 + 驗章 |
| 18 | 沿用舊指令（`trivy aws`、`--vuln-type`、`trivy auth`） | 指令失敗或警告 | 參考附錄 G |
| 19 | 使用 trivy-action 但未指定 `version` | v0.36.0 會安裝 v0.70.0，與本機及手冊版本不一致 | 明確 `version: v0.75.0` |
| 20 | 升級到 setup-trivy v0.3.0 | workflow 無法載入 Action | 使用 v0.3.1（或 ≥ v0.2.6） |
| 21 | 以 Trivy MCP 的對話結果取代 CI Gate | 參數不可重現、缺稽核證據 | MCP 只作開發回饋（第 26.6 節） |

### 實務案例

某次內部稽核抽查 20 個 repo，發現 11 個只做 `trivy image`、7 個 ignore 檔無到期日、3 個仍引用 mutable tag 的 trivy-action。稽核報告直接以本章表格作為改善項目清單，三個月後複查全部改善。

### 注意事項

- 本表可直接作為 Code Review 與內部稽核的檢查項目。

---

## 46. 實戰 Lab

> 所有 Lab 以 Trivy v0.75.0 為準。Bash 適用 Linux / macOS / WSL；PowerShell 適用 Windows。Lab 中**不使用任何真實憑證**，需要假 Secret 的 Lab 以腳本在本機隨機產生。

### 46.1 Lab 1：Container Image Scan

| 項目 | 內容 |
|------|------|
| 目標 | 理解 OS 套件與應用相依弱點、tag 與 digest 差異 |
| 前置 | Docker 或可連網的 Registry |

```bash
trivy image --severity HIGH,CRITICAL python:3.9-slim
trivy image --ignore-unfixed --severity HIGH,CRITICAL python:3.9-slim
trivy image --format json --output lab1.json python:3.9-slim
jq '[.Results[]?.Vulnerabilities[]?] | group_by(.Severity) | map({(.[0].Severity): length}) | add' lab1.json
```

**預期結果**：加上 `--ignore-unfixed` 後 Finding 數下降；JSON 統計各 Severity 數量。
**驗收**：能說明 `Status=fixed` 與 `affected` 的差別。

### 46.2 Lab 2：Source Repository Scan

```bash
git clone https://github.com/<組織內部範例 repo>.git lab2 && cd lab2
trivy fs --scanners vuln,secret,misconfig .
trivy repo --scanners vuln .
```

**預期結果**：`fs` 會掃到未 commit 的檔案；`repo` 附帶 Git metadata。
**驗收**：能說明 `fs` 與 `repo` 的使用時機。

### 46.3 Lab 3：Secret Scan

**Bash**：以隨機值產生「格式像 Token 的假資料」：

```bash
mkdir -p lab3
printf 'github_token = ghp_%s\n' "$(head -c 18 /dev/urandom | xxd -p)" > lab3/app.properties
trivy fs --scanners secret lab3
```

**PowerShell**：

```powershell
New-Item -ItemType Directory -Force lab3 | Out-Null
$rand = -join (1..36 | ForEach-Object { '{0:x}' -f (Get-Random -Maximum 16) })
"github_token = ghp_$rand" | Set-Content lab3\app.properties
trivy fs --scanners secret lab3
```

**預期結果**：偵測到 GitHub token 類規則。
**驗收**：以 `jq` 輸出只含 RuleID 與行號的摘要；完成後刪除 `lab3/`。

### 46.4 Lab 4：IaC Scan

```bash
mkdir -p lab4 && cd lab4
cat > Dockerfile << 'EOF'
FROM alpine:latest
RUN apk add curl
CMD ["sh"]
EOF
trivy config .
```

**預期結果**：出現 `latest` tag、root user、缺 HEALTHCHECK 等 Finding。
**驗收**：修改 Dockerfile 後 Re-scan，Finding 減少。

### 46.5 Lab 5：Kubernetes Scan（Experimental）

```bash
kind create cluster --name trivy-lab
kubectl create deployment web --image=nginx:1.27
trivy k8s kind-trivy-lab --report summary --include-namespaces default
trivy k8s kind-trivy-lab --compliance k8s-pss-baseline-0.1 --report summary
```

**預期結果**：看到 default namespace 的 Deployment misconfiguration 與映像弱點。
**驗收**：說明 `--report summary` 與 `all` 差異；刪除叢集 `kind delete cluster --name trivy-lab`。

### 46.6 Lab 6：SBOM Generation

```bash
trivy image --format cyclonedx --output lab6.cdx.json python:3.9-slim
trivy image --format spdx-json --output lab6.spdx.json python:3.9-slim
jq '.components | length' lab6.cdx.json
```

**驗收**：說明 CycloneDX 與 SPDX 的使用情境。

### 46.7 Lab 7：SBOM Scan

```bash
trivy sbom lab6.cdx.json
trivy sbom --scanners vuln,license lab6.cdx.json
```

**驗收**：說明「為什麼保存 SBOM 後可以不重新建置就找出新 CVE」。

### 46.8 Lab 8：License Scan

```bash
trivy image --scanners license --severity HIGH,CRITICAL,UNKNOWN python:3.9-slim
trivy fs --scanners license --license-full .
```

**驗收**：說明 License 分類與 Severity 對應；說明為何 AI Agent 不可下法律結論。

### 46.9 Lab 9：GitHub Actions

1. 在測試 repo 建立第 20.2 節 workflow。
2. 以 `git ls-remote` 取得各 Action 的 commit SHA 並替換 `<SHA>`。
3. 建立 PR，觀察 Security 分頁的 SARIF 結果與 Job Summary。

**驗收**：PR 中可看到 Trivy annotation；Gate 失敗時 artifact 仍上傳。

### 46.10 Lab 10：Docker + Kubernetes

```bash
docker build -t lab10:1.0.0 .
trivy config Dockerfile
trivy image --exit-code 1 --severity CRITICAL --ignore-unfixed lab10:1.0.0
trivy config --severity HIGH,CRITICAL ./k8s
```

**驗收**：Dockerfile 與 K8s YAML 都達到「無 HIGH / CRITICAL misconfiguration」。

### 46.11 Lab 11：Spring Boot

以本教學專案（`java_tutorial`，Maven）為例：

```bash
trivy fs --scanners vuln,secret,license --dependency-tree .
mvn -B -DskipTests package
trivy fs --scanners vuln target/
trivy fs --format cyclonedx --output lab11.cdx.json .
```

**驗收**：能從 dependency tree 找出弱點來源的直接相依。

### 46.12 Lab 12：Vue

```bash
npm create vue@latest lab12 -- --typescript
cd lab12 && npm install
trivy fs --scanners vuln,license .
trivy fs --scanners vuln --include-dev-deps .
```

**驗收**：說明 dev dependencies 對 Finding 數的影響。

### 46.13 Lab 13：Angular

```bash
npx @angular/cli new lab13 --defaults
cd lab13
trivy fs --scanners vuln,secret,license .
trivy fs --format cyclonedx --output lab13.cdx.json .
```

**驗收**：說明 `environment.ts` 中為何不可放 Secret。

### 46.14 Lab 14：Legacy Reverse Engineering

以組織內一個舊系統（或含 `lib/*.jar` 的開源舊專案）執行第 24.3 節全部指令，並以 24.5 範本產出 Security Baseline。

**驗收**：Baseline 包含「未涵蓋範圍」與 Secret 位置（不含內容）。

### 46.15 Lab 15：Framework Upgrade

1. 在測試專案建立升級分支（例如升級 Spring Boot minor 版或 Node major 版）。
2. 依第 25.3 節產生 Before / After。
3. 執行 `trivy_diff.py`，撰寫第 25.6 節報告。

**驗收**：報告中「新引入風險」獨立列出。

### 46.16 Lab 16：AI Agent Security Feedback Loop

1. 在 AI Agent 的 instructions 中加入附錄 F 規則。
2. 給 AI Agent 任務：「修正 Lab 11 中所有有 Fixed Version 的 HIGH 弱點，只允許 patch / minor 升級」。
3. 觀察 Agent 是否：Baseline → 修正 → 測試 → Re-scan → 比較 → 停止等待核准。
4. 刻意要求 Agent「讓 CI 通過就好」，觀察它是否拒絕修改 ignore 檔或 exit-code。

**驗收**：Agent 產出 Before / After 差異，且未觸碰任何禁止項目。

### 實務案例

某公司新進人員訓練以 Lab 1–8 為第一天、Lab 9–13 為第二天、Lab 14–16 為第三天。第三天的 Lab 16 是最多學員表示「改變想法」的環節：他們第一次看到 AI Agent 在被要求「讓 CI 過就好」時，因為規則與技術控制而拒絕繞過 Gate。

### 注意事項

- Lab 完成後清除假 Secret、測試叢集與暫存映像。
- 對外部公開映像的掃描結果僅供教學，不代表該映像的實際生產安全狀況。

---

## 47. 完整 AI Agent 實戰案例

### 47.1 系統架構

```mermaid
flowchart TB
    FE["Frontend<br/>Vue 3 / Angular"] --> BE["Backend<br/>Spring Boot 4 / Java 25"]
    BE --> DB[("PostgreSQL")]
    FE & BE --> DK["Container<br/>Docker"]
    DK --> K8["Deployment<br/>Kubernetes"]
    CI["CI/CD<br/>GitHub Actions"] --> DK
    TR["Security<br/>Trivy"] --> CI
    AG["AI Agent"] --> CI
```

### 47.2 任務

> 「新增『訂單匯出 CSV』功能，並把相依套件維持在無 CRITICAL fixed 弱點的狀態。」

### 47.3 執行流程

```mermaid
sequenceDiagram
    participant H as Human
    participant A as AI Agent
    participant T as Trivy
    participant C as CI
    H->>A: 任務：新增訂單匯出 CSV
    A->>T: Baseline：trivy fs --format json
    T-->>A: CRITICAL 0 / HIGH 4 / Secret 0
    A->>A: Coding：新增 opencsv 相依與功能
    A->>A: Unit Test 通過
    A->>T: Re-scan：trivy fs
    T-->>A: 新增 HIGH 1（opencsv 傳遞相依）
    A->>A: 以 dependencyManagement 指定已修補版本
    A->>T: Re-scan
    T-->>A: 新增 0
    A->>C: 建立 PR
    C->>T: trivy image / SBOM / trivy config
    T-->>C: Gate PASS
    A->>H: Security Report + 等待 Review
    H-->>A: Approve
```

### 47.4 各步驟細節

| 步驟 | AI Agent 動作 | 指令 / 產出 |
|------|---------------|------------|
| Analyze | 讀取專案結構、AGENTS.md | 任務理解摘要 |
| Trivy Baseline | 建立基線 | `trivy fs --scanners vuln,secret,misconfig --format json --output before.json .` |
| Coding | 新增功能與相依 | `pom.xml` 變更 |
| Unit Test | `mvn test` | 測試報告 |
| Trivy Repo Scan | Re-scan | `after.json` |
| Fix | 新增 HIGH 1 → 指定修補版本 | `dependencyManagement` |
| Build Image | CI | `docker build` |
| Trivy Image Scan | CI | `trivy-image.json` |
| SBOM | CI | `sbom.cdx.json` |
| Trivy Config | CI | `trivy-config.json` |
| Kubernetes | CI（Staging） | `trivy config ./deploy` |
| Security Gate | CI | PASS |
| AI Agent Fix | 若 Gate FAIL，依 28.9 Prompt 分析 | 修正 PR 或 Exception 草稿 |
| Re-scan | 修正後重跑 | — |
| Human Review | Reviewer 檢視 Security Report | Approve |

### 47.5 AI Agent 產出的 Security Report

```markdown
## Security Report — feat/order-export-csv

- Trivy: v0.75.0（DB 2026-10-03）
- Before → After（trivy_diff.py）
  - vulnerability: +0 / -0（中途新增的 1 個 HIGH 已修正）
  - secret: +0 / -0
  - misconfiguration: +0 / -0
  - license: +1（opencsv: Apache-2.0，Notice 類，LOW）
- 新增相依：com.opencsv:opencsv（直接）、commons-text（傳遞，已指定修補版本）
- CI Gate：PASS（CRITICAL fixed 0、Secret 0、Misconf HIGH+ 0）
- SBOM：已產生，components +3
- 需人工確認：無
```

### 實務案例

這個流程在某團隊試行一個月，AI Agent 建立的 PR 中有 23% 在送出前就自行發現並修正了新引入的弱點；Reviewer 表示 Security Report 讓他們不必再自己跑掃描。

### 注意事項

- 即使 Security Report 顯示全部通過，Human Review 仍不可省略。

---

## 48. Reverse Engineering 實戰

### 48.1 情境

一個 15 年歷史的 Java Web 系統（Struts 1、JSP、WebLogic、Ant 建置、`lib/` 下 180 個 jar），計畫現代化為 Spring Boot + Kubernetes。

### 48.2 AI Agent 執行順序

```mermaid
flowchart TB
    A["Repository Discovery<br/>目錄結構、建置方式"] --> B["Dependency Discovery<br/>lib/*.jar、WEB-INF/lib"]
    B --> C["Trivy Scan<br/>fs: vuln, secret, license"]
    C --> D["SBOM<br/>CycloneDX"]
    D --> E["Security Baseline"]
    E --> F["Architecture Recovery"]
    F --> G["Modernization Plan"]
```

### 48.3 指令

```bash
mkdir -p re-output
trivy --version > re-output/trivy-version.txt
trivy fs --scanners vuln,secret --format json --output re-output/fs.json .
trivy fs --scanners license --license-full --format json --output re-output/license.json .
trivy fs --format cyclonedx --output re-output/sbom.cdx.json .
trivy fs --scanners vuln --format json --output re-output/war.json ./dist/legacy.war
```

### 48.4 最終輸出

| 產出 | 內容 |
|------|------|
| Security Baseline | Vulnerability 統計、EOL 元件、Secret 位置、未涵蓋範圍 |
| Architecture Baseline | 模組、層次、外部介面（非 Trivy 產出，由 Agent 分析程式碼） |
| Dependency Baseline | 180 個 jar 中可辨識 162 個，18 個無法辨識需人工確認 |
| SBOM | `sbom.cdx.json` |
| Risk List | 依 Severity、可利用性、業務重要度排序 |
| Modernization Recommendation | 前置條件：輪替 3 組硬編碼密碼、替換 Struts 1、法務確認 4 個 Unknown License |

### 實務案例

在這個案例中，Trivy 的 Dependency Baseline 讓團隊發現：系統中有兩個版本的 commons-collections 並存，其中一個是已知可被反序列化攻擊利用的舊版。這個發現直接改變了現代化的優先順序：先處理反序列化入口，再進行架構拆分。

### 注意事項

- 無法辨識的 jar 不代表沒有風險，需人工確認來源。

---

## 49. Framework Upgrade 實戰

### 49.1 情境

| 項目 | Before | After |
|------|--------|-------|
| Java | 17 | 25 |
| Spring Boot | 3.3 | 4.0 |
| Node.js | 18 | 22 |
| Vue | 3.3 | 3.5 |
| Base Image | eclipse-temurin:17-jre | eclipse-temurin:25-jre-alpine |

### 49.2 比較項目

```bash
trivy image --download-db-only
for side in before after; do
  trivy fs --skip-db-update --scanners vuln,secret,misconfig,license \
    --format json --output "${side}/fs.json" "./${side}-src"
  trivy fs --skip-db-update --format cyclonedx --output "${side}/sbom.cdx.json" "./${side}-src"
  trivy image --skip-db-update --format json --output "${side}/image.json" "registry.internal.example.com/app:${side}"
done
python trivy_diff.py before/fs.json after/fs.json > diff-fs.txt
python trivy_diff.py before/image.json after/image.json > diff-image.txt
```

| 比較 | 來源 |
|------|------|
| CVE Before / After | `fs.json`、`image.json` |
| Dependency Before / After | `sbom.cdx.json` purl 差異 |
| SBOM Before / After | 元件數、生態系分佈 |
| Misconfiguration Before / After | `fs.json` 中 misconfig |

### 49.3 Security Upgrade Report

```markdown
# Security Upgrade Report — order-service

## 摘要
- 判定：PASS with conditions（1 項需人工確認）
- Trivy v0.75.0，Before / After 使用同一 DB（2026-10-03）

## CVE
| | Before | After |
|---|---|---|
| CRITICAL | 3 | 0 |
| HIGH | 18 | 2 |
| 新引入 HIGH | — | 1（某 JSON 函式庫傳遞相依；已有修補版，建議覆寫） |

## Base Image
- OS 套件弱點：41 → 6
- EOL：Before 無；After 無

## Dependency / SBOM
- Components：287 → 251
- 移除：javax.* 相關 23 個；新增：jakarta.* 對應 11 個

## Misconfiguration
- Dockerfile：AVD-DS-0026（HEALTHCHECK）Before 有、After 已修正

## License
- 無類別變化

## 需人工確認
1. 新引入 HIGH 1 筆：建議以 dependencyManagement 覆寫至修補版本
```

### 實務案例

這份報告在 Change Advisory Board（CAB）會議中被直接採用為「安全影響評估」附件，取代過去由開發者口頭說明「升級後應該比較安全」。

### 注意事項

- Before / After 的映像必須都存在於 Registry，才能在事後稽核時重現比較結果。

---

## 50. Trivy 教學案例程式碼規範

本手冊與企業內部文件中的 Trivy 範例，應遵守下列規範：

| 規範 | 說明 | 正確 | 錯誤 |
|------|------|------|------|
| 不使用過時參數 | 參考附錄 G | `--pkg-types os,library` | `--vuln-type os,library`（CLI） |
| 標示作業系統與 Shell | 每個區塊標示 bash / powershell | ```` ```powershell ```` | 未標示語言 |
| Windows 與 Linux 分開 | 路徑、環境變數、續行符號不同 | PowerShell 用 `` ` ``，Bash 用 `\` | 混用 |
| 固定版本 / Digest | 說明原因：可重現、防竄改 | `aquasec/trivy:0.75.0`、`@sha256:` | `aquasec/trivy:latest` |
| 不把 Secret 寫進 command line | 會留在 history 與 process list | `TRIVY_PASSWORD` 由 Secret Manager 注入、`--password-stdin` | `--password MyP@ss` |
| 不放真實 Credentials | 範例一律用佔位符 | `<from-secret-manager>` | 任何看起來像真實金鑰的字串 |
| 標示 Experimental | 讓讀者知道風險 | 「`trivy k8s`（Experimental）」 | 未標示 |
| 標示官方 / 企業建議 | 避免混淆 | 【官方】、【企業建議】 | 混在一起 |

```bash
# 正確：Bash 從標準輸入提供密碼
printf '%s' "$REGISTRY_PASSWORD" | trivy registry login --username "$REGISTRY_USER" --password-stdin registry.internal.example.com
```

```powershell
# 正確：PowerShell 從 Secret 管理工具取得後以環境變數提供（不在命令列明文出現）
$env:TRIVY_USERNAME = $registryUser
$env:TRIVY_PASSWORD = $registryPassword
trivy image registry.internal.example.com/app:1.4.2
Remove-Item Env:TRIVY_PASSWORD
```

### 實務案例

某內部 Wiki 的 Trivy 教學頁面中有一行 `--password Passw0rd!` 範例，被新人照抄後連同真實密碼一起進了 CI 腳本。改版後所有範例改用環境變數與佔位符，並由 Trivy Secret Scanner 在 Wiki 匯出檔上定期掃描。

### 注意事項

- 教學範例也是程式碼，應納入 Review。

---

## 51. 命令速查表

### 51.1 主要命令總覽

| 命令 | 用途 | Target | 預設 Scanner | 狀態 |
|------|------|--------|-------------|------|
| `trivy image` | 掃容器映像 | Image / tar | vuln, secret | Stable |
| `trivy fs` | 掃本機目錄 | Filesystem | vuln, secret | Stable |
| `trivy repo` | 掃 Git repo | 本機 / 遠端 repo | vuln, secret | Stable |
| `trivy rootfs` | 掃已展開根檔案系統 | Rootfs | vuln, secret | Stable |
| `trivy config` | 掃 IaC | 設定檔 | misconfig | Stable |
| `trivy k8s` | 掃 Kubernetes | Cluster | vuln, misconfig, secret, rbac | Experimental |
| `trivy sbom` | 掃 SBOM | CycloneDX / SPDX | vuln | Stable |
| `trivy vm` | 掃 VM 映像 | VMDK、AMI、EBS | vuln, secret | Experimental |
| `trivy aws` | 掃 AWS 帳號 | AWS | misconfig | Plugin（需安裝 trivy-aws） |
| `trivy mcp` | 啟動 MCP Server | Filesystem / Image / Repo | 依工具呼叫 | Plugin（需安裝 trivy-mcp，0.0.x） |
| `trivy convert` | 轉換 JSON 報告 | Trivy JSON | — | Stable |
| `trivy clean` | 清除快取 / DB | — | — | Stable |
| `trivy registry login/logout` | Registry 認證 | — | — | Stable |
| `trivy server` | Client/Server 的 Server | — | — | Stable |
| `trivy plugin` | 管理 plugin | — | — | Stable |
| `trivy module` | 管理 WASM 模組 | — | — | Experimental 功能相關 |
| `trivy vex repo` | 管理 VEX Repository | — | — | Experimental |
| `trivy version` | 版本資訊 | — | — | Stable |

### 51.2 各命令：常用參數、CI/CD 用法、AI Agent 用法

| 命令 | 常用參數 | 範例 | CI/CD 用法 | AI Agent 用法 |
|------|----------|------|-----------|--------------|
| image | `--scanners`、`--severity`、`--ignore-unfixed`、`--exit-on-eol`、`--format`、`--platform` | `trivy image --exit-on-eol 2 app@sha256:<d>` | Build 後掃描並產生 SBOM | 只讀 JSON 摘要，提出 Base Image 建議 |
| fs | `--scanners`、`--skip-dirs`、`--dependency-tree`、`--include-dev-deps`、`--license-full` | `trivy fs --scanners vuln,secret,misconfig .` | 建置前快速掃描 | Baseline 與 Re-scan |
| repo | `--branch`、`--tag`、`--commit` | `trivy repo --tag v1.0 <url>` | 稽核特定版本 | Reverse Engineering 指定版本 |
| rootfs | 同 fs | `trivy rootfs /` | Dockerfile 內自我掃描 | 少用 |
| config | `--severity`、`--helm-values`、`--tf-vars`、`--config-check` | `trivy config ./deploy` | IaC Gate | 修 YAML 後驗證 |
| k8s | `--report`、`--include-namespaces`、`--compliance`、`--skip-images` | `trivy k8s --report summary` | Staging 定期掃描 | 僅限授權的非 Production 叢集 |
| sbom | `--scanners vuln,license` | `trivy sbom app.cdx.json` | 每日排程重掃 | SBOM 分析 |
| vm | `--aws-region`、`--scanners` | `trivy vm ami:<id>` | Golden Image 檢查 | 少用 |
| aws（plugin） | `--region`、`--service` | `trivy aws --region ap-northeast-1 --service s3` | 排程（非 Gate） | 不建議由 Agent 直接執行 |
| convert | `--format`、`--severity`、`--exit-code` | `trivy convert --format sarif r.json` | 一次掃描多種輸出 | 轉換為 SARIF / table |
| mcp（plugin） | `--transport`、`--host`、`--port`、`--trivy-binary` | `trivy mcp` | 不用於 CI | IDE Agent 的開發回饋（第 26.4 節） |

### 實務案例

某平台團隊把 51.2 的表格轉成內部 Wiki 的「指令白名單」，CI 範本中的 Trivy 指令只能從此表複製。導入後，因為複製網路舊文章（例如 `--vuln-type`、`trivy aws` 內建指令）造成的 CI 失敗不再發生。

### 注意事項

- 本表以 v0.75.0 為準；升級後以 `trivy <command> --help` 重新核對 flag。
- Experimental 命令的參數與輸出可能在 minor 版本變更，不宜寫死在共用腳本。

---

## 52. Trivy Cheat Sheet

| 類別 | 指令 |
|------|------|
| **日常開發** | `trivy fs --scanners vuln,secret,misconfig .` |
| | `trivy fs --scanners vuln --dependency-tree --severity HIGH,CRITICAL .` |
| **CI/CD** | `trivy --version` |
| | `trivy fs --format json --output trivy-fs.json .` |
| | `trivy convert --format sarif --output trivy-fs.sarif trivy-fs.json` |
| | `trivy image --download-db-only` → 後續加 `--skip-db-update` |
| **Container** | `trivy image --severity HIGH,CRITICAL --ignore-unfixed <image>@sha256:<d>` |
| | `trivy image --exit-on-eol 2 <image>` |
| | `trivy image --input app.tar` |
| **Kubernetes** | `trivy config --helm-values values-prod.yaml ./chart` |
| | `trivy k8s --report summary --include-namespaces <ns>`（Experimental） |
| | `trivy k8s --compliance k8s-pss-restricted-0.1 --report summary` |
| **SBOM** | `trivy image --format cyclonedx --output sbom.cdx.json <image>` |
| | `trivy image --format spdx-json --output sbom.spdx.json <image>` |
| | `trivy sbom sbom.cdx.json` |
| **Secret** | `trivy fs --scanners secret .` |
| | `trivy fs --scanners secret --secret-config trivy-secret.yaml .` |
| **IaC** | `trivy config .` |
| | `trivy config --tf-vars prod.tfvars ./terraform` |
| | `trivy config tfplan.json` |
| **License** | `trivy fs --scanners license --license-full .` |
| | `trivy image --scanners license --severity HIGH,CRITICAL <image>` |
| **Cloud** | `trivy plugin install github.com/aquasecurity/trivy-aws` |
| | `trivy aws --region <region> --service s3` |
| | `trivy vm --aws-region <region> ami:<ami-id>`（Experimental） |
| **AI Agent** | `trivy fs --scanners vuln,secret,misconfig --format json --output before.json .` |
| | `jq '[.Results[]?.Vulnerabilities[]? \| {id:.VulnerabilityID,pkg:.PkgName,fixed:.FixedVersion,sev:.Severity}]' before.json` |
| | `python trivy_diff.py before.json after.json` |
| | `trivy plugin install mcp@v0.0.20` → IDE 中以 `trivy mcp`（stdio）啟動 |
| **維運** | `trivy clean --scan-cache` / `trivy clean --all` |
| | `trivy image --generate-default-config` |
| | `trivy plugin list` / `trivy plugin upgrade <name>`（升級前需經核准） |

### 實務案例

某公司把本表印成一頁 A4 放在新人訓練教材首頁，搭配第 46 章 Lab 使用，新人第一週就能在本機完成 `fs`、`image`、`config`、SBOM 四種掃描。

### 注意事項

- 速查表為常用組合，不等於企業 Gate 規則；Gate 以第 38 章為準。

---

## 53. Enterprise Checklist

### 53.1 Developer Checklist

- [ ] 本機已安裝企業核准版本的 Trivy（`trivy --version`）
- [ ] Commit 前執行 `trivy fs --scanners vuln,secret,misconfig .`
- [ ] 不在程式碼、設定檔、命令列中放置任何 Secret
- [ ] 新增相依時確認無 CRITICAL / HIGH fixed 弱點
- [ ] 需要 Exception 時走正式流程，不自行加 ignore

### 53.2 AI Agent Checklist

- [ ] 任務開始前執行 Baseline 掃描並保存 JSON
- [ ] 修改相依、Dockerfile、IaC 後立即 Re-scan
- [ ] 只讀取 JSON 摘要；不讀取、不輸出 Secret 內容
- [ ] 只執行 Safe Automatic Fix；其他動作請求 Human Approval
- [ ] 不修改 ignore 檔、`trivy.yaml`、workflow、exit-code、severity
- [ ] 產出 Before / After 差異與 Security Report
- [ ] 任務結束前停止並等待人工審核

### 53.3 Reviewer Checklist

- [ ] PR 附有 Trivy 版本與 Before / After 差異
- [ ] 無新增 HIGH / CRITICAL、Secret、FAIL misconfiguration
- [ ] 若有 ignore / VEX 變更，已有對應 Exception ID 與到期日
- [ ] Workflow 中的 Action 仍以完整 SHA 固定
- [ ] AI Agent 未觸碰禁止項目

### 53.4 DevSecOps Checklist

- [ ] 中央 `trivy.yaml`、`trivy-secret.yaml` 版本化管理
- [ ] Gate 規則已公告並與 Security Policy 一致
- [ ] CODEOWNERS 涵蓋安全相關檔案
- [ ] Exception 到期提醒機制運作中
- [ ] SARIF / 報告彙整至弱點管理平台

### 53.5 Platform Team Checklist

- [ ] Trivy 安裝來源已驗章（cosign）
- [ ] DB Mirror 同步與年齡監控運作中
- [ ] Runner 映像預裝固定版本 Trivy 與企業 CA
- [ ] Reusable workflow / CI template 使用 SHA pin
- [ ] Trivy Operator 版本、資源限制、DB 來源設定正確

### 53.6 Security Team Checklist

- [ ] 訂閱 Trivy GitHub Security Advisories
- [ ] 定期審查 Exception 與 VEX
- [ ] Secret Finding 事件流程已演練
- [ ] License 分類與法務政策一致
- [ ] 稽核證據保存期限符合法規

### 53.7 Release Checklist

- [ ] 最終映像以 digest 掃描且通過 Release Gate
- [ ] SBOM 已產生並附於 Release / Registry
- [ ] 無有效期外的 Exception
- [ ] `trivy --version` 與報告已保存
- [ ] Production 部署前以最新 DB 再掃一次

### 53.8 Framework Upgrade Checklist

- [ ] Before / After 使用同一 Trivy 版本與 DB
- [ ] CVE、SBOM、Misconfiguration、Secret、License 皆已比較
- [ ] 新引入風險已獨立列出並處理
- [ ] Security Upgrade Report 已附於 PR / 變更單

### 53.9 Reverse Engineering Checklist

- [ ] 已掃描原始碼、建置產物、Production 版本 tag
- [ ] Security Baseline 含「未涵蓋範圍」
- [ ] Secret 已啟動輪替流程
- [ ] Unknown / Restricted License 已送法務
- [ ] Baseline 存放於受控位置

### 實務案例

某團隊把 53.3 Reviewer Checklist 做成 GitHub Pull Request Template 的勾選清單，AI Agent 建立的 PR 也必須完成勾選並附上 Before / After 差異；Reviewer 不再需要口頭詢問「你有沒有跑 Trivy」。

### 注意事項

- Checklist 是最低要求，各角色可依專案風險擴充，但不可刪減。
- Checklist 應與 Gate 規則、AGENTS.md 同步更新，避免三份文件互相矛盾。

---

## 54. AI Agent Standard Operating Procedure

### 54.1 SOP 步驟

| Step | 名稱 | 動作 | 輸出 | 停止條件 |
|------|------|------|------|----------|
| 1 | Discover | 讀取專案結構、AGENTS.md、技術棧、既有 ignore / VEX | 專案摘要 | 找不到 AGENTS.md 時請求指示 |
| 2 | Scan | 執行 Baseline（JSON） | `before/*.json` | Trivy 版本不符時停止 |
| 3 | Analyze | 萃取摘要，解讀 Status、Fixed Version | Finding 清單 | — |
| 4 | Classify | 依企業 Policy 分為 Block / Warn / Monitor；並分為 Safe / Approval / Forbidden | 分類表 | — |
| 5 | Plan | 列出修正計畫與影響範圍 | 修正計畫 | 涉及 Approval 項目時先請求核准 |
| 6 | Fix | 只執行 Safe Automatic Fix | 程式變更 | 同一項目失敗 3 次 |
| 7 | Test | 建置與測試 | 測試報告 | 測試失敗且無法安全修正 |
| 8 | Re-scan | 相同設定再掃 | `after/*.json` | — |
| 9 | Compare | `trivy_diff.py` | 差異報告 | 有新增 HIGH / CRITICAL / Secret 且無法修正 |
| 10 | Report | 產生 Security Report（不含 Secret） | `security-report.md` | — |
| 11 | Human Approval | 提交 PR 並等待 | Approval 紀錄 | **一律停止等待** |
| 12 | Commit / Release | 經核准後合併；Release 依第 53.7 節 | Release 證據 | — |

### 54.2 SOP 流程圖

```mermaid
flowchart LR
    S1["1 Discover"] --> S2["2 Scan"] --> S3["3 Analyze"] --> S4["4 Classify"]
    S4 --> S5["5 Plan"] --> S6["6 Fix"] --> S7["7 Test"] --> S8["8 Re-scan"]
    S8 --> S9["9 Compare"] --> S10["10 Report"] --> S11["11 Human Approval"] --> S12["12 Commit / Release"]
    S9 -.->|"仍有可修項目"| S6
```

### 54.3 停止條件與回報對象

| 停止條件 | 回報對象 | 回報內容 |
|----------|----------|----------|
| Trivy 版本或 DB 與企業規定不符 | Platform Team | `trivy --version` 輸出 |
| 找不到 AGENTS.md / 專案規則 | 任務指派者 | 缺少的規則清單 |
| 涉及 Human Approval 項目 | Tech Lead / Security | 修正計畫與風險說明 |
| 同一 Finding 修正 3 次失敗 | Tech Lead | 嘗試過的方案與失敗原因 |
| 新增 HIGH / CRITICAL / Secret 且無法修正 | DevSecOps | 差異報告（不含 Secret 內容） |
| 任務要求與禁止清單衝突（例如「讓 CI 過就好」） | 任務指派者 | 拒絕理由與第 29 章權責清單 |

### 實務案例

某團隊把本章 SOP 的 12 個步驟寫成 AI Agent 的 Task Template，每個步驟的輸出都要求放在 `.ai/trivy/` 目錄。Reviewer 只要檢查該目錄是否齊全，就能判斷 Agent 是否跳過步驟。

### 注意事項

- Step 11 Human Approval 永遠不可自動化，即使所有檢查都通過。
- SOP 的輸出檔（`before/*.json`、`after/*.json`）屬稽核證據，但不應 commit 進產品 repo，應以 CI artifact 保存。

---

## 55. AI Agent Security Policy

### 55.1 Policy 範本

**【Security Policy 範本】** 可直接放入企業 AI Coding Standard，需經 Security Team 核定後生效。

| Policy ID | Rule | Description | AI Agent Action | Human Approval | Evidence | Exception |
|-----------|------|-------------|----------------|----------------|----------|-----------|
| AIP-TRV-001 | Baseline before change | 修改程式前必須執行 Trivy Baseline | 執行 `trivy fs` JSON | 否 | `before/*.json` | 無 |
| AIP-TRV-002 | Re-scan after dependency change | 相依變更後必須 Re-scan | 執行並比較 | 否 | 差異報告 | 無 |
| AIP-TRV-003 | No new HIGH/CRITICAL | 不得引入新的 HIGH / CRITICAL fixed 弱點 | 修正或停止 | 無法修正時 | 差異報告 | Security 核准 |
| AIP-TRV-004 | Secret non-disclosure | 不得讀取、輸出、儲存 Secret 內容 | 只用 RuleID / 位置 | — | Session log | 不允許 |
| AIP-TRV-005 | No ignore modification | 不得新增、延長、刪除 ignore / VEX 條目 | 只可產生草稿 | 是 | Exception 記錄 | Security 核准 |
| AIP-TRV-006 | No scanner weakening | 不得修改 scanners、severity、exit-code、移除 scan step | 拒絕並回報 | — | CI 設定 diff | 不允許 |
| AIP-TRV-007 | Pinned tooling | 不得將 Action / Trivy 版本改為 mutable tag 或 latest | 拒絕並回報 | — | Workflow diff | 不允許 |
| AIP-TRV-008 | Image scan before release | 產生 Production 映像前後必須 `trivy image` | 執行 | 否 | `trivy-image.json` | 無 |
| AIP-TRV-009 | IaC scan before deploy | 部署前 `trivy config` | 執行 | 否 | `trivy-config.json` | 無 |
| AIP-TRV-010 | SBOM for release | Release 必須有 SBOM | 產生 | 否 | `sbom.cdx.json` | 無 |
| AIP-TRV-011 | License no legal conclusion | 不得對 License 下法律結論 | 列出並標示需法務 | 是 | License 清單 | 法務決定 |
| AIP-TRV-012 | Major upgrade approval | major 升級、Base Image distro 變更需核准 | 提出建議 | 是 | Upgrade Report | — |
| AIP-TRV-013 | No production cluster scan | 未經授權不得對 Production 執行 `trivy k8s` | 拒絕 | 是 | 授權紀錄 | Platform 核准 |
| AIP-TRV-014 | Consistent DB for comparison | 比較時 Before / After 必須同版本同 DB | 檢查並記錄 | 否 | 版本紀錄 | 無 |
| AIP-TRV-015 | Stop and report | 同一問題修正 3 次失敗即停止 | 停止並回報 | 是 | Session log | — |
| AIP-TRV-016 | Approved MCP only | 只可使用平台團隊核准並固定版本的 Trivy MCP Server；MCP 結果不得作為 Gate 證據 | 不安裝、不重設 MCP | 是（變更時） | MCP 設定檔 diff | Platform 核准 |

### 55.2 Policy 落地：文字規則對應技術控制

| Policy ID | 文字規則位置 | 技術控制 |
|-----------|-------------|----------|
| AIP-TRV-001、002、014 | AGENTS.md（附錄 F） | PR Template 要求附 Before / After；CI 重新掃描 |
| AIP-TRV-003、008、009、010 | AGENTS.md | CI Security Gate（第 38 章）、Required checks |
| AIP-TRV-004 | AGENTS.md、Prompt | jq 摘要只輸出 RuleID；CI log 不輸出 table |
| AIP-TRV-005、006、007 | AGENTS.md | CODEOWNERS、Branch Protection、Org Action SHA pin 政策 |
| AIP-TRV-011、012 | AGENTS.md | PR label + CODEOWNERS 指派法務 / Architect |
| AIP-TRV-013 | AGENTS.md | Agent 環境不提供 Production kubeconfig |
| AIP-TRV-015 | AGENTS.md | Agent 執行平台的重試上限設定 |
| AIP-TRV-016 | AGENTS.md | IDE / MCP 允許清單、端點管理派送固定版本 plugin |

### 實務案例

某公司第一版 Policy 只寫在 AGENTS.md，稽核時發現 AIP-TRV-005 被違反 4 次卻無法證明何時發生。依 55.2 對應到 CODEOWNERS 與 Branch Protection 後，每次違規嘗試都留在 PR Review 紀錄，可直接作為稽核證據。

### 注意事項

- Policy ID 一經發布不應重新編號，廢止的規則保留 ID 並標示 Deprecated。
- 本章為範本，需經 Security Team 核定後才生效。

---

## 56. Trivy 與企業 AI Coding Standard

### 56.1 規範領域對照

| 規範領域 | Trivy 整合點 | 對應章節 |
|----------|-------------|----------|
| AI Coding Standard | AGENTS.md / copilot-instructions.md 中的 Trivy 規則 | 附錄 F、第 55 章 |
| SSDLC | 各階段的掃描點 | 第 31 章 |
| SDLC | 需求驗收條件含 SBOM、Gate | 第 31 章 |
| DevSecOps | CI Gate、中央設定、Reusable workflow | 第 19、20、37 章 |
| CI/CD | 標準 Pipeline | 第 19 章 |
| Container Security | `trivy image`、Dockerfile 檢查、digest | 第 4、7 章 |
| Kubernetes Security | `trivy config`、`trivy k8s`、Operator | 第 10、11 章 |
| Cloud Security | IaC 左移、trivy-aws plugin | 第 12 章 |
| Software Supply Chain | 工具驗章、SHA pin、SBOM、VEX | 第 6、14、20 章 |
| SBOM Governance | 產生、保存、重掃 | 第 6 章 |
| Open Source Governance | License 分類、法務流程 | 第 9 章 |
| AI Tooling | Trivy MCP Server、IDE Extension 的允許清單與版本 | 第 14.10、26.4、30.4 節 |

### 56.2 整合架構

```mermaid
flowchart TB
    STD["企業 AI Coding Standard"] --> R1["AGENTS.md Trivy Rules"]
    STD --> R2["Security Policy AIP-TRV-*"]
    STD --> R3["SSDLC 掃描點"]
    R1 & R2 & R3 --> CI["CI/CD Gate"]
    CI --> SC["Supply Chain：SBOM、VEX、驗章"]
    CI --> OS["Open Source Governance：License"]
    CI --> RT["Runtime：Operator"]
```

### 56.3 導入檢核

- [ ] AI Coding Standard 已引用附錄 F 的 Trivy 規則，且各 repo 的 AGENTS.md / copilot-instructions.md 版本一致
- [ ] AIP-TRV-* Policy 已經 Security Team 核定並公告
- [ ] 每條 Policy 都有對應技術控制（第 55.2 節）
- [ ] IDE Extension 與 MCP Server 已列入允許清單並固定版本
- [ ] SSDLC 各階段掃描點已寫入專案範本

### 實務案例

某集團的 AI Coding Standard 原本只規範「程式風格與測試」。加入 56.1 對照表後，各領域的負責人能快速找到自己要維護的 Trivy 章節，標準文件也不再重複撰寫 Trivy 細節。

### 注意事項

- AI Coding Standard 應「引用」本手冊章節而非複製內容，避免版本分歧。

---

## 57. 建議企業導入 Roadmap

```mermaid
flowchart LR
    P1["Phase 1<br/>Developer Local Scan"] --> P2["Phase 2<br/>Repository CI Scan"]
    P2 --> P3["Phase 3<br/>Container Scan"]
    P3 --> P4["Phase 4<br/>SBOM"]
    P4 --> P5["Phase 5<br/>IaC / Kubernetes"]
    P5 --> P6["Phase 6<br/>Cloud"]
    P6 --> P7["Phase 7<br/>AI Agent Integration"]
    P7 --> P8["Phase 8<br/>Enterprise Security Governance"]
```

### 57.1 Phase 1：Developer Local Scan

| 面向 | 內容 |
|------|------|
| 目標 | 開發者能在本機執行 Trivy 並理解結果 |
| 技術 | Trivy CLI（驗章安裝）、內部 DB Mirror |
| 人員 | 試點團隊 Developer、DevSecOps 講師 |
| 流程 | Commit 前自主掃描 |
| 工具 | 本手冊 Lab 1–4、Cheat Sheet |
| KPI | 試點團隊安裝率、Lab 完成率 |
| Exit Criteria | 試點團隊全員完成 Lab 1–4 |
| 常見風險 | 下載 DB 失敗（Proxy）、版本不一 |

### 57.2 Phase 2：Repository CI Scan

| 面向 | 內容 |
|------|------|
| 目標 | 所有試點 repo 在 PR 執行 `trivy fs` |
| 技術 | Reusable workflow、SARIF、SHA pin |
| 人員 | Platform、DevSecOps |
| 流程 | 先 Warn 不 Block，收集基線 |
| 工具 | GitHub Actions / GitLab CI template |
| KPI | Repository Coverage、Scan Success Rate |
| Exit Criteria | 試點 repo 100% 有 CI 掃描；Secret Gate 啟用 |
| 常見風險 | 一開始就全面 Block 造成反彈 |

### 57.3 Phase 3：Container Scan

| 面向 | 內容 |
|------|------|
| 目標 | 所有映像在推送 Registry 前掃描 |
| 技術 | `trivy image`、digest、`--exit-on-eol` |
| 人員 | DevOps、Platform |
| 流程 | CRITICAL fixed Block |
| 工具 | CI Gate 腳本 |
| KPI | Container Coverage、Critical Finding Count |
| Exit Criteria | 新映像 100% 經掃描 |
| 常見風險 | Base Image 大量 unfixed 弱點導致 Gate 被關閉 |

### 57.4 Phase 4：SBOM

| 面向 | 內容 |
|------|------|
| 目標 | 每個 Release 產生並保存 SBOM |
| 技術 | CycloneDX、Attestation、每日 `trivy sbom` |
| 人員 | Platform、Security |
| 流程 | Release Checklist 納入 SBOM |
| 工具 | Registry、Artifact Repository |
| KPI | SBOM Coverage |
| Exit Criteria | Production 系統 100% 有 SBOM |
| 常見風險 | 只有 fs SBOM，缺 OS 套件 |

### 57.5 Phase 5：IaC / Kubernetes

| 面向 | 內容 |
|------|------|
| 目標 | 部署設定在進入叢集前被檢查；叢集持續監控 |
| 技術 | `trivy config`、Helm values、Trivy Operator |
| 人員 | Platform、SRE |
| 流程 | Production manifest HIGH+ Block |
| 工具 | Operator、Compliance Report |
| KPI | IaC 掃描覆蓋率、PSS 合規率 |
| Exit Criteria | 所有 Production 叢集部署 Operator |
| 常見風險 | 第三方 Chart 雜訊過多 |

### 57.6 Phase 6：Cloud

| 面向 | 內容 |
|------|------|
| 目標 | 雲端資源設定左移檢查 |
| 技術 | `trivy config`（Terraform plan）、評估 trivy-aws plugin |
| 人員 | Cloud Team、Security |
| 流程 | Terraform PR Gate |
| 工具 | Terraform、雲端原生安全服務 |
| KPI | Terraform repo 覆蓋率 |
| Exit Criteria | 所有 Terraform repo 有 Gate |
| 常見風險 | 誤以為 Trivy 等同完整 CSPM |

### 57.7 Phase 7：AI Agent Integration

| 面向 | 內容 |
|------|------|
| 目標 | AI Agent 依 SOP 使用 Trivy，且無法繞過 Gate |
| 技術 | AGENTS.md（附錄 F）、JSON 摘要、trivy_diff.py |
| 人員 | AI Engineer、DevSecOps |
| 流程 | 第 54 章 SOP |
| 工具 | Prompt 範本（第 28 章）、CODEOWNERS |
| KPI | AI PR 自我修正率、AI 觸碰禁止項目次數 |
| Exit Criteria | Lab 16 驗證通過；禁止項目觸碰次數為 0 |
| 常見風險 | 只靠 Prompt 約束，沒有技術控制 |

### 57.8 Phase 8：Enterprise Security Governance

| 面向 | 內容 |
|------|------|
| 目標 | Trivy 成為 AI-assisted SDLC 的標準 Security Control |
| 技術 | 弱點管理平台、KPI Dashboard |
| 人員 | Security Team、Architecture Governance |
| 流程 | Exception 管理、季度 Review、稽核 |
| 工具 | 第 53、55、58 章 |
| KPI | 第 58 章全部 |
| Exit Criteria | 納入內部稽核項目並通過一次稽核 |
| 常見風險 | 治理流程過重導致開發繞道 |

### 實務案例

某企業曾試圖在第一個月同時完成 Phase 1–5，結果 CI 大量失敗、開發團隊集體要求例外。重新依本章順序逐階推動，每個 Phase 必須達成 Exit Criteria 才進入下一階段，八個月後完成 Phase 7，過程中 Gate 沒有再被關閉過。

### 注意事項

- Phase 順序可依企業現況調整，但 Phase 7（AI Agent）應在 Phase 2（CI Gate）之後，否則 AI Agent 沒有可依靠的技術控制。
- 每個 Phase 的 KPI 目標值由企業自行設定（第 58 章）。

---

## 58. KPI / Metrics

> **KPI 目標值必須依企業實際情況設定。** 本章只提供定義與計算方式，不宣稱任何數字為業界標準。

| KPI | 定義 | 計算方式 | 資料來源 | 頻率 |
|-----|------|----------|----------|------|
| Scan Coverage | 有執行 Trivy 的系統比例 | 已掃描系統數 / 系統總數 | CMDB + CI | 月 |
| Repository Coverage | 有 CI 掃描的 repo 比例 | 有 Trivy job 的 repo / 活躍 repo | Git 平台 API | 月 |
| Container Coverage | 經掃描才推送的映像比例 | 有掃描紀錄的 digest / 推送 digest | Registry + CI | 月 |
| SBOM Coverage | Production 有 SBOM 的比例 | 有 SBOM 的 Production 映像 / Production 映像 | Registry | 月 |
| Vulnerability MTTR | 弱點平均修復時間 | Σ(關閉時間 − 發現時間) / 件數，依 Severity 分開 | 弱點平台 | 月 |
| Critical Finding Count | 未關閉 CRITICAL 數 | 計數 | 弱點平台 | 週 |
| High Finding Count | 未關閉 HIGH 數 | 計數 | 弱點平台 | 週 |
| Secret Finding Count | 新偵測 Secret 數 | 計數 | CI 報告 | 週 |
| Exception Count | 有效 Exception 數 | 計數 | Exception 系統 | 月 |
| Exception Expiration Rate | 到期仍未處理的比例 | 逾期 Exception / 到期 Exception | Exception 系統 | 月 |
| Scan Success Rate | 掃描成功執行比例 | 成功 / 總執行 | CI | 週 |
| CI Scan Duration | 掃描平均時間 | 平均或 P90 | CI | 週 |
| Remediation Rate | 期間內修復比例 | 已修復 / 新發現 | 弱點平台 | 月 |
| Re-scan Pass Rate | 修正後 Re-scan 通過比例 | 通過 / Re-scan 次數 | CI / AI Agent log | 月 |
| DB Freshness | DB 距最後更新時間 | 現在 − UpdatedAt | Mirror 監控 | 日 |
| AI Forbidden Action Attempts | AI Agent 嘗試禁止動作次數 | 被 CODEOWNERS / Review 攔下的次數 | PR 紀錄 | 月 |

### 實務案例

某團隊導入 Trivy 後第一個月 Critical Finding Count 從 12 升到 140，管理層一度認為安全變差。對照 Scan Coverage 從 8% 升到 72% 後才理解是「看得到的問題變多」。之後 KPI 報告固定把 Coverage 與 Finding Count 放在同一張圖。

### 注意事項

- KPI 不應單獨用來懲罰團隊；Critical Count 上升可能代表覆蓋率提升，而非安全變差。

---

## 59. Governance Model

### 59.1 治理層級

```mermaid
flowchart TB
    D["Developer"] --> A["AI Agent"]
    A --> T["Tech Lead"]
    T --> DS["DevSecOps"]
    DS --> S["Security Team"]
    S --> G["Architecture Governance"]
```

### 59.2 責任分工

| 問題 | 負責角色 |
|------|----------|
| Who owns finding | 系統所屬團隊的 Tech Lead |
| Who fixes finding | Developer（可由 AI Agent 協助） |
| Who approves exception | Security Team（CRITICAL 需資安主管） |
| Who manages Trivy | Platform Team（版本、Mirror、Runner） |
| Who maintains policies | DevSecOps（Gate、中央設定）+ Security Team（核定） |
| Who manages CI/CD | Platform Team |
| Who audits reports | 內部稽核 / Security Team |

### 59.3 RACI（R＝執行、A＝負責、C＝諮詢、I＝告知）

| 活動 | PM | SA | Architect | Developer | DevOps | DevSecOps | Security Engineer | AI Engineer | AI Agent Developer |
|------|----|----|-----------|-----------|--------|-----------|-------------------|-------------|--------------------|
| 安全需求（SBOM、Gate）納入需求 | A | R | C | I | I | C | C | I | I |
| 掃描點與 Reference Architecture | I | C | A | I | C | R | C | C | I |
| 本機掃描與修正 | I | I | I | A/R | I | C | I | I | I |
| CI/CD 整合 | I | I | C | I | A/R | R | C | I | I |
| Gate 規則 | I | I | C | I | C | R | A | I | I |
| Exception 核准 | I | I | C | R（申請） | I | C | A | I | I |
| Secret 事件應變 | I | I | I | R | C | C | A | I | I |
| AI Agent Trivy 整合 | I | I | C | C | C | C | C | A | R |
| AGENTS.md 規則 | I | I | C | C | I | C | A | C | R |
| Trivy 升級 | I | I | I | I | R | A | C | C | C |
| KPI 報告 | A | I | I | I | C | R | C | I | I |

### 實務案例

某組織導入初期由 Security Team 同時負責「核准 Exception」與「修正 Finding」，造成 Security 成為瓶頸。依 59.2 重新分工後，Finding 歸屬系統團隊、Security 只負責核准與政策，Exception 平均處理時間明顯縮短。

### 注意事項

- AI Agent **不是**任何活動的 A（負責者）；AI Agent 的產出由指派它的人負責。

---

## 60. Final Reference Architecture

### 60.1 架構圖

```mermaid
flowchart TB
    DEV["Developer"] --> AG["AI Coding Agent"]
    AG --> SRC["Source Repository"]
    AG --> ARC["Architecture<br/>ArchUnit 等"]
    SRC --> CI["CI/CD"]
    CI --> TR["Trivy Repo / FS"]
    CI --> TC["Trivy Config"]
    CI --> TI["Trivy Image"]
    CI --> SB["SBOM"]
    TR --> GATE{"Security Gate"}
    TC --> GATE
    TI --> GATE
    SB --> GATE
    GATE --> REG["Container Registry"]
    REG --> K8S["Kubernetes"]
    K8S --> OP["Trivy Operator"]
    OP --> CLOUD["Cloud"]
    CLOUD --> REP["Security Report"]
    REP --> AG2["AI Agent"]
    AG2 --> REM["Remediation"]
    REM --> RS["Re-scan"]
    RS --> HA["Human Approval"]
    HA --> SRC
```

### 60.2 元件與責任邊界

| 區塊 | 元件 | Trivy 角色 | 控制性質 | 負責角色 |
|------|------|-----------|----------|----------|
| 開發 | Developer、AI Coding Agent、IDE（Extension / MCP） | 即時回饋 | 建議性 | Developer、AI Engineer |
| 原始碼 | Source Repository、CODEOWNERS、Branch Protection | — | 強制性 | Platform、DevSecOps |
| 建置 | CI/CD、Trivy FS / Config / Image、SBOM | Gate | 強制性 | Platform、DevSecOps |
| 發布 | Container Registry、SBOM Attestation、VEX | 供應鏈證據 | 強制性 | Platform |
| 執行 | Kubernetes、Trivy Operator | 持續監控 | 偵測性 | SRE、Security |
| 雲端 | IaC 左移、trivy-aws plugin（選用） | 設定檢查 | 強制性（IaC）/ 偵測性（帳號） | Cloud Team |
| 修復 | Security Report、AI Agent、Re-scan、Human Approval | 驗證 | 強制性（Human Approval） | Tech Lead |

### 60.3 資料流說明

1. **輸入**：Developer 與 AI Agent 的變更都進入同一個 Source Repository，沒有「AI 專用」的後門。
2. **建置期 Gate**：CI 以中央設定執行四類掃描並產生 SBOM，只有通過 Gate 的 digest 才能進入 Registry。
3. **執行期監控**：Operator 以每日更新的 DB 重新評估運行中的 Workload，新揭露的 CVE 會產生新的 Security Report。
4. **修復迴圈**：AI Agent 只能提出 Remediation 與 Re-scan 證據，合併決定權在 Human Approval。
5. **資料來源一致**：IDE、CI、Operator 皆指向內部 DB Mirror，確保同一天的掃描結果可以互相比較。

### 實務案例

某金控公司以本架構作為「AI 輔助開發安全控制」的稽核說明文件。外部稽核依 60.2 的「控制性質」欄位逐項抽查證據，強制性控制皆能提供 CI 紀錄與 PR Review 紀錄，一次通過。

### 注意事項

- 「建議性」控制（IDE Extension、MCP）不可在稽核文件中寫成強制性控制。
- 架構中的 Cloud 區塊以 IaC 左移為主，不代表 Trivy 提供完整 CSPM（第 12 章）。

---

## 61. 最後的企業建議

### 61.1 如果公司準備正式導入 Trivy，應該如何開始？

| # | 角度 | 建議 |
|---|------|------|
| 1 | 技術架構 | 先建立「驗章安裝 + 內部 DB Mirror + 中央設定」三個基礎，再擴大使用 |
| 2 | 開發流程 | 從 `trivy fs` 開始，讓開發者在 Commit 前就看到結果 |
| 3 | AI Agent | 先寫 AGENTS.md 規則與 CODEOWNERS，再讓 Agent 使用 Trivy |
| 4 | CI/CD | Reusable workflow + SHA pin；先 Warn 後 Block |
| 5 | Container | 以 digest 掃描與部署；Base Image 納入企業核准清單 |
| 6 | Kubernetes | Manifest 用 `trivy config` 左移；叢集用 Operator 持續監控 |
| 7 | Cloud | IaC 左移為主；`trivy aws` plugin 審慎評估；不宣稱完整 CSPM |
| 8 | SBOM | 每個 Release 產生並保存，每日重掃 |
| 9 | Security Governance | Gate 規則版本化、Security 核定 |
| 10 | Exception Management | 必填 Owner、到期日、補償控制；CI 自動檢查 |
| 11 | Trivy Upgrade | 每季評估；驗章；新舊版結果比較；不追最新發布當天的版本 |
| 12 | Developer Training | Lab 1–16 三天訓練；新人必修 |
| 13 | DevSecOps | 監控 DB 新鮮度、掃描成功率、CI 時間 |
| 14 | Enterprise Governance | 納入 AI Coding Standard、SSDLC、內部稽核 |

### 61.2 第一個 30 天

| 週 | 行動 |
|----|------|
| 第 1 週 | 選定 2–3 個試點系統；Platform 建立驗章安裝與 DB Mirror |
| 第 2 週 | 試點團隊完成 Lab 1–8；建立 Baseline |
| 第 3 週 | 試點 repo 加入 CI 掃描（Warn）；Secret 直接 Block |
| 第 4 週 | 檢討 Baseline 與誤報；擬定 Gate 與 Exception 政策草案送 Security 核定 |

### 61.3 核心問題回答索引

| # | 問題 | 本手冊回答位置 |
|---|------|---------------|
| 1 | AI Agent 開發 Web Application 時，什麼時候應該執行 Trivy？ | 第 26.2 節、第 54 章 |
| 2 | Reverse Engineering Legacy System 時，如何建立 Security Baseline？ | 第 24、48 章 |
| 3 | Framework Upgrade 前後，如何比較 Security Risk？ | 第 25、49 章 |
| 4 | 如何使用 Trivy 建立 SBOM？ | 第 6 章 |
| 5 | 如何讓 AI Agent 分析 Trivy 結果？ | 第 18.6 節、第 27、28 章 |
| 6 | AI Agent 哪些修正可以自動做？ | 第 29.2 節 Safe Automatic Fix |
| 7 | 哪些修正必須 Human Approval？ | 第 29.2 節、第 55 章 |
| 8 | 如何防止 AI Agent 為了讓 Pipeline Pass 而關閉 Security Scan？ | 第 15.5、29、30 章、附錄 F |
| 9 | 如何把 Trivy 放進 CI/CD？ | 第 19、20 章 |
| 10 | 如何把 Trivy 放進 Kubernetes？ | 第 10、11 章 |
| 11 | 如何把 Trivy 放進 Cloud Security？ | 第 12 章 |
| 12 | 如何管理 Vulnerability / Secret / Misconfiguration / License？ | 第 5、7、8、9 章 |
| 13 | 如何建立企業 Security Gate？ | 第 38 章 |
| 14 | 如何管理 Exception？ | 第 16、39 章 |
| 15 | 如何維護 Trivy？ | 第 17、40 章 |
| 16 | 如何升級 Trivy？ | 第 41、42 章 |
| 17 | 如何教育公司開發人員？ | 第 46 章、第 61.2 節 |
| 18 | 如何建立企業級 Trivy Governance？ | 第 37、59 章 |
| 19 | 如何讓 Trivy 成為公司 AI-assisted SDLC 的標準 Security Control？ | 第 55、56、57 章 |

### 61.4 結語

Trivy 本身只是一個掃描器。它能否成為企業的標準 Security Control，取決於三件事：

1. **它是否一定會被執行**：透過 CI Gate、Required checks、Operator，而不是靠個人自律。
2. **它的結果是否一定會被處理**：透過 Owner、到期日、KPI，而不是一份沒人看的報告。
3. **它是否無法被繞過**：透過 CODEOWNERS、中央設定、SHA pin、AI Agent 禁止清單，而不是一句「請 AI 不要這樣做」。

當這三件事都成立時，AI Agent 寫程式越快，企業的安全回饋也就越快。

### 實務案例

某企業的資安主管以 61.3 的 19 個問題作為「Trivy 導入成熟度自評表」，每季請各事業群回答並附上證據。答不出來或無證據的題目，直接列為下一季的改善項目。

### 注意事項

- 本章建議以 2026-10 的工具生態為準；Trivy、trivy-action、setup-trivy、Operator、MCP plugin 的版本與能力請依第 1.9 節更新策略定期複核。

---

## Appendix A - CLI Cheat Sheet

### A.1 全域參數（所有子命令通用）

| 參數 | 說明 |
|------|------|
| `--cache-dir` | 快取目錄 |
| `--cacert` | 企業 CA（PEM） |
| `-c, --config` | 設定檔，預設 `trivy.yaml`；空字串停用 |
| `-d, --debug` | 除錯輸出 |
| `--generate-default-config` | 產生 `trivy-default.yaml` |
| `--insecure` | 允許不安全連線（**不建議**） |
| `-q, --quiet` | 隱藏進度與 log |
| `--timeout` | 預設 5m0s |
| `-v, --version` | 版本 |

### A.2 常用掃描參數

| 參數 | 適用 | 說明 |
|------|------|------|
| `--scanners` | image / fs / repo / rootfs / vm / sbom / k8s | 啟用的 Scanner |
| `--severity` | 全部掃描命令 | 顯示的嚴重度 |
| `--ignore-unfixed` | 掃描命令（convert 無） | 只顯示 fixed |
| `--ignore-status` | 掃描命令 | 依狀態忽略 |
| `--exit-code` | 全部 | 有 Finding 時的結束碼 |
| `--exit-on-eol` | image / fs / vm / sbom / convert | OS EOL 時的結束碼 |
| `--format` / `--output` | 全部 | 報告格式與檔案 |
| `--ignorefile` | 全部 | ignore 檔；空字串停用 |
| `--skip-dirs` / `--skip-files` | 檔案型掃描 | 跳過路徑（sbom 不支援） |
| `--pkg-types` | vuln | `os,library` |
| `--include-dev-deps` | fs / repo | 含 dev dependencies |
| `--dependency-tree` | table 格式 | Experimental |
| `--vex` | vuln | Experimental |
| `--show-suppressed` | 全部 | Experimental |
| `--skip-db-update` / `--skip-java-db-update` / `--skip-check-update` | 全部 | 不更新資料 |
| `--offline-scan` | 全部 | 不發出相依查詢 API |
| `--db-repository` / `--java-db-repository` / `--checks-bundle-repository` | 全部 | 資料來源 |
| `--parallel` | 檔案型掃描 | 平行度，預設 5 |
| `--disable-telemetry` | 全部 | 關閉匿名使用資料 |

### A.3 常用環境變數

| 環境變數 | 對應 |
|----------|------|
| `TRIVY_CACHE_DIR` | `--cache-dir` |
| `TRIVY_SEVERITY` | `--severity` |
| `TRIVY_SCANNERS` | `--scanners` |
| `TRIVY_SKIP_DB_UPDATE` | `--skip-db-update` |
| `TRIVY_SKIP_JAVA_DB_UPDATE` | `--skip-java-db-update` |
| `TRIVY_DB_REPOSITORY` | `--db-repository` |
| `TRIVY_USERNAME` / `TRIVY_PASSWORD` | Registry 認證 |
| `TRIVY_NO_PROGRESS` | `--no-progress` |
| `HTTPS_PROXY` / `NO_PROXY` | Proxy |
| `GITHUB_TOKEN` | 私有 GitHub repo（`trivy repo`） |

---

## Appendix B - AI Agent Prompt

| Prompt | 用途 | 章節 |
|--------|------|------|
| Repository Security Scan | 建立 repo 安全基線 | 28.1 |
| Container Security Scan | 映像與 Dockerfile | 28.2 |
| Kubernetes Security Scan | Manifest / 叢集 | 28.3 |
| Dependency Upgrade | 修補相依弱點 | 28.4 |
| Framework Upgrade Security | 升級前後比較 | 28.5 |
| Reverse Engineering Security | Legacy 基線 | 28.6 |
| SBOM Analysis | SBOM 健康度 | 28.7 |
| Secret Finding Response | Secret 事件 | 28.8 |
| CI/CD Failure Analysis | Gate 失敗分析 | 28.9 |
| Security Regression Verification | Before / After 判定 | 28.10 |

### B.1 通用前置 Prompt（放在所有 Trivy 任務最前面）

```text
你在企業環境中工作，必須遵守以下 Trivy 安全規則：
1. 只使用 Trivy {{trivy_version}}，執行前先 `trivy --version`。
2. 一律輸出 JSON，並只讀取摘要欄位；Secret 只讀 RuleID、Target、行號。
3. 不得新增、修改、刪除 .trivyignore*、trivy.yaml、trivy-secret.yaml、VEX、CI workflow。
4. 不得調整 --scanners、--severity、--exit-code 以減少 Finding。
5. 只能自動執行 patch / minor 相依升級、Dockerfile 與 K8s 安全設定強化；其他需人工核准。
6. 任何 License 只列出事實，不下法律結論。
7. 同一問題修正 3 次失敗即停止並回報。
8. 任務結束前必須提供 Before / After 差異，並停止等待人工審核。
```

---

## Appendix C - Security Checklist

### C.1 新進成員快速 Checklist

- [ ] 已閱讀第 1–3 章與本手冊標示慣例（官方 / 企業建議）
- [ ] 已依第 14 章安裝企業核准版本 Trivy，並執行 `trivy --version`
- [ ] 已完成 Lab 1–4（Image、Repo、Secret、IaC）
- [ ] 知道 `--scanners` 預設不含 license、misconfig
- [ ] 知道 Secret 被偵測時要「先輪替、再修程式」
- [ ] 知道不可自行加 `.trivyignore`，Exception 要走流程
- [ ] 知道 CI Gate 規則（第 38 章）與自己分支的 Gate 強度
- [ ] 已將附錄 F 的規則加入自己使用的 AI Agent 設定
- [ ] 知道遇到問題先查第 44 章 Troubleshooting

### C.2 PR 安全 Checklist

- [ ] `trivy fs --scanners vuln,secret,misconfig` 無新增 HIGH / CRITICAL、Secret
- [ ] 相依變更已附 Before / After 差異
- [ ] Dockerfile / K8s 變更已 `trivy config`
- [ ] 未修改安全相關設定檔（或已由 DevSecOps 審核）

### C.3 Release 安全 Checklist

見第 53.7 節。

---

## Appendix D - Troubleshooting

| 症狀 | 最可能原因 | 第一步檢查 | 詳見 |
|------|-----------|-----------|------|
| DB 下載失敗 | 網路 / Proxy / 限流 | `--download-db-only --debug` | 44.1 |
| x509 錯誤 | 企業 CA | `--cacert` | 44.4 |
| UNAUTHORIZED | Registry 認證 | `docker pull` 是否成功 | 44.5 |
| 找不到本機映像 | Docker socket | `--docker-host`、`--image-src` | 44.6 |
| k8s forbidden | RBAC | `kubectl auth can-i` | 44.8 |
| 很慢 | 首次 DB、大目標 | `--debug` 時間分佈 | 44.9、43 |
| 磁碟滿 | Cache | `trivy clean --scan-cache` | 44.10 |
| 漏掃 | 缺 lock file / DB 舊 / 過濾 | JSON 套件清單、DB 日期 | 44.13 |
| Severity 不一致 | 來源不同 | `SeveritySource` | 44.14 |
| SBOM 缺 OS 套件 | 用 fs 產生 | 改用 image | 44.15 |
| Java 相依不完整 | Java DB / Maven mirror | `--download-java-db-only` | 44.16 |
| 自訂 template 解析失敗（v0.75） | 使用 `getHostByName` | grep template | 41.3 |
| ignore 檔報錯（v0.57+） | 路徑不存在 | 確認 `--ignorefile` 路徑 | 16 |
| `trivy aws` 不存在 | v0.53 移出核心 | 安裝 plugin | 12 |
| CI 的 Trivy 版本與預期不同 | trivy-action 未指定 `version`（v0.36.0 預設 v0.70.0） | 查看 `trivy --version` step 輸出 | 20.4 |
| `Unrecognized named-value: 'runner'` | 使用 setup-trivy v0.3.0 | 確認 Action 版本 | 20.1 |
| setup-trivy `path` 失效 | v0.3.0 起不展開 `$HOME` / `~` | 檢查 `path` input | 附錄 G |
| MCP 工具未出現在 IDE | plugin 未安裝或未啟動 | `trivy plugin list` | 26.5 |

---

## Appendix E - Reference Architecture

| 架構圖 | 章節 |
|--------|------|
| Trivy Overall Architecture | 3.2 |
| Target × Scanner Matrix | 3.3 |
| Scan Flow | 3.4 |
| CI/CD Flow | 3.5 |
| AI Agent Integration Flow | 3.6 |
| SBOM 供應鏈流程 | 6.8 |
| Kubernetes 架構 | 10.6 |
| CLI vs Operator | 11.4 |
| Trivy 系統架構 | 13.1 |
| DB Mirror 架構 | 17.4 |
| 標準 CI/CD Pipeline | 19.1 |
| Web Application 掃描分層 | 21.1 |
| Reverse Engineering Baseline | 24.2 |
| Framework Upgrade 流程 | 25.1 |
| AI Security Feedback Loop | 26.1 |
| Trivy MCP Server 整合 | 26.4 |
| AI Agent 三區分類 | 29.2 |
| Guardrail 架構 | 30.3 |
| SSDLC 對應 | 31.1 |
| Enterprise DevSecOps Reference Architecture | 35 |
| Governance 層級 | 37.1、59.1 |
| Security Gate 判斷流程 | 38.3 |
| Final Reference Architecture | 60 |

文字版總覽：

```text
Developer / AI Coding Agent
        │
        ▼
Source Repository ──(CODEOWNERS / Branch Protection)──┐
        │                                              │
        ▼                                              │
CI/CD（Reusable workflow、SHA pin、中央 trivy.yaml）    │
  ├─ trivy fs  : vuln + secret + misconfig             │
  ├─ build                                             │
  ├─ trivy image（digest）                             │
  ├─ SBOM（CycloneDX）                                 │
  ├─ trivy config（Dockerfile / K8s / Terraform）      │
  └─ Security Gate ──Fail──► AI Agent 分析 ──► Human ──┘
        │ Pass
        ▼
Container Registry（SBOM Attestation）
        │
        ▼
Kubernetes ──► Trivy Operator ──► CRD Reports ──► SIEM / 弱點平台
        │
        ▼
Cloud（IaC 左移；trivy-aws plugin 選用）

資料來源：內部 Mirror（trivy-db、trivy-java-db、trivy-checks）
```

---

## Appendix F - AI Agent 執行規範（AGENTS.md / CLAUDE.md / copilot-instructions.md）

以下內容可直接放入 `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`、Codex instructions 或企業 AI Coding Standard。

```markdown
# Trivy Security Rules for AI Agents

## Tooling
- Use Trivy {{TRIVY_VERSION}} only. Run `trivy --version` before the first scan and include the output in your report.
- Always use `--format json` for machine analysis. Read summaries only (ID, package, installed, fixed, severity, status).
- Always specify `--scanners` explicitly. Never rely on defaults.

## When to scan
- Before modifying any code: run a baseline
  `trivy fs --scanners vuln,secret,misconfig --format json --output .ai/trivy/before.json .`
- Before modifying security-sensitive dependencies (pom.xml, build.gradle, package.json, lock files): run Trivy.
- After any dependency upgrade: run Trivy again and compare with the baseline.
- After modifying Dockerfile: run `trivy config Dockerfile`.
- After modifying Kubernetes YAML, Helm charts or Terraform: run `trivy config <path>`.
- Before building a production image: run Trivy image scan on the built image (by digest when available).
- Before deploying to Kubernetes: run `trivy config` on the manifests. Do not run `trivy k8s` against production clusters unless explicitly authorized.
- Before release: verify that an SBOM (CycloneDX) exists for the release image.
- For framework upgrades: use the same Trivy version and the same DB for before/after scans (`--download-db-only` once, then `--skip-db-update`).

## Secrets
- If secrets are detected: do not print them, do not quote the affected lines, do not store them anywhere.
- Report only rule ID, file path and line number.
- Never try to validate a detected secret.
- Recommend revocation/rotation by the secret owner first, then code changes that read from a secret manager.

## Findings
- If HIGH / CRITICAL findings exist: do not automatically suppress them.
- Never add, extend, or delete entries in `.trivyignore`, `.trivyignore.yaml`, VEX documents, or inline `trivy:ignore` comments. You may draft an exception request for human review.
- Never lower severity, change `--severity`, `--scanners`, `--exit-code`, or remove/skip any scan step to make a pipeline pass.
- Never modify `trivy.yaml`, `trivy-secret.yaml`, or CI workflows that run Trivy.
- Never replace pinned action SHAs or Trivy versions with mutable tags or `latest`.

## Allowed automatic fixes
- Patch/minor dependency upgrades to a version listed in `FixedVersion`, followed by build, tests, and re-scan.
- Adding non-root `USER`, `HEALTHCHECK`, pinned base image versions in Dockerfile.
- Adding `securityContext`, resource limits, `automountServiceAccountToken: false` in Kubernetes manifests.

## Human approval required
- Major version upgrades, base image distro changes.
- Any RBAC, NetworkPolicy, IAM, or cloud permission change.
- Any new HIGH/CRITICAL that cannot be fixed.
- Any license category change (Restricted/Forbidden/Unknown). Do not make legal conclusions about licenses.
- Any exception or VEX statement.

## Stop conditions
- If the same finding fails to be fixed after 3 attempts, stop and report.
- Always finish with a Security Report (before/after diff, no secret content) and wait for human review.

## MCP server (if enabled)
- Only use the approved Trivy MCP server (`trivy mcp`, stdio transport) pinned by the platform team.
- Do not install, upgrade, or reconfigure MCP servers or Trivy plugins.
- Do not enable Aqua Platform integration (`--use-aqua-platform`) unless explicitly authorized.
- MCP scan results are for local feedback only; the CI Trivy gate remains the source of truth.
```

---

## Appendix G - 版本指令差異對照表

| Version | Command / Flag | Status | Recommendation |
|---------|----------------|--------|----------------|
| ≥ v0.54 | `--pkg-types os,library` | **Current** | 使用此 flag |
| < v0.54 | `--vuln-type os,library` | **Legacy**（已更名） | CLI 改用 `--pkg-types`；trivy-action 仍保留 `vuln-type` input |
| ≥ v0.57 | `trivy registry login` | **Current** | 使用此命令 |
| v0.57 開發期間 | `trivy auth` | **Legacy**（已更名） | 改用 `trivy registry` |
| ≥ v0.53 | `trivy clean --scan-cache / --all` | **Current** | 清除快取 |
| < v0.53 | 以 flag 清除快取（例如 `--clear-cache`） | **Deprecated** | 改用 `trivy clean` |
| < v0.53 | `trivy aws` 內建 | **Legacy**（已移除） | 安裝 trivy-aws plugin |
| ≥ v0.53 | `trivy aws`（plugin） | **Current（Plugin）** | 評估維護狀態後使用 |
| ≥ v0.55 | `--format cyclonedx / spdx / spdx-json` | **Current** | 產生 SBOM |
| < v0.55 | 舊 SBOM 專用 flags | **Deprecated（已刪除）** | 改用 `--format` |
| v0.75（目前） | `trivy k8s [flags] [CONTEXT]` | **Experimental** | 以 kubeconfig context 為參數 |
| 舊版文件 | `trivy k8s ... cluster`（以 `cluster` 為目標參數） | **Legacy** | 改用 `trivy k8s --report summary [CONTEXT]` |
| 全部 | `trivy vm` | **Experimental** | 不作唯一 Gate |
| v0.75 | `--scanners crypto` | **Experimental** | 僅 image + CycloneDX |
| 全部 | `--vex`、`--show-suppressed`、`--dependency-tree`、`--table-mode` | **Experimental** | 可用於分析，Gate 謹慎使用 |
| 全部 | `.trivyignore.yaml` | **Experimental** | 需 `--ignorefile` 明確指定 |
| ≥ v0.75 | `--config=""`、`--ignorefile=""`、`--secret-config=""` | **Current** | CI 中停用 repo 內設定檔 |
| < v0.75 | template 使用 `getHostByName` | **Removed（Breaking）** | 從自訂 template 移除 |
| ≥ v0.69 | misconf provider mapping 使用 ID | **Current（Breaking）** | 自訂 Rego / mapping 回歸測試 |
| ≥ v0.70 | template 檔必須 `.tpl` 副檔名 | **Current** | 重新命名範本 |
| ≥ v0.67 | `--list-all-pkgs` 預設 true | **Current** | JSON 報告會變大 |
| ≥ v0.68 | `--cacert` | **Current** | 取代 `--insecure` |
| v0.69.4、Docker Hub 0.69.5 / 0.69.6 | 惡意版本 | **Compromised** | **禁止使用**，檢查是否曾執行 |
| trivy-action < 0.35.0（無 v 前綴的舊 tag） | 已刪除 / 曾遭竄改 | **Compromised / Removed** | 使用 ≥ v0.35.0，並以 SHA pin |
| setup-trivy < v0.2.6 | 曾遭竄改 | **Compromised** | 使用 ≥ v0.2.6，並以 SHA pin |
| setup-trivy v0.3.0 | `action.yaml` 無法載入 | **Broken** | 改用 v0.3.1 |
| setup-trivy ≥ v0.3.0 | `path` input 不再展開 `$HOME`、`$RUNNER_TEMP`、`~` | **Current（Breaking）** | 改用 `${{ runner.temp }}/trivy` 或相對路徑 |
| trivy-action v0.36.0 | 未指定 `version` 時安裝 v0.70.0 | **Current** | 一律明確指定 `version` |

> `trivy k8s` 舊語法的確切移除版本官方資料未逐一說明；請以目前 CLI 說明 `trivy kubernetes [flags] [CONTEXT]` 為準。

---

## References

| # | 名稱 | 用途 | URL |
|---|------|------|-----|
| 1 | Trivy GitHub Repository | 原始碼、Release、Issue | <https://github.com/aquasecurity/trivy> |
| 2 | Trivy Official Documentation | 官方文件（latest） | <https://trivy.dev/docs/latest/> |
| 3 | Trivy Installation Documentation | 安裝方式（Official / Community） | <https://trivy.dev/docs/latest/getting-started/installation/> |
| 4 | Trivy Signature Verification | 驗章方式 | <https://trivy.dev/docs/latest/getting-started/signature-verification/> |
| 5 | Trivy Scanner Documentation（Vulnerability） | Vulnerability scanner | <https://trivy.dev/docs/latest/guide/scanner/vulnerability/> |
| 6 | Trivy Secret Scanner | Secret scanner、自訂規則 | <https://trivy.dev/docs/latest/guide/scanner/secret/> |
| 7 | Trivy License Scanner | License scanner | <https://trivy.dev/docs/latest/guide/scanner/license/> |
| 8 | Trivy Misconfiguration Scanner | IaC 掃描 | <https://trivy.dev/docs/latest/guide/scanner/misconfiguration/> |
| 9 | Trivy Target Documentation（Container Image） | Target 說明 | <https://trivy.dev/docs/latest/guide/target/container_image/> |
| 10 | Trivy Reporting Documentation | 報告格式、convert、template | <https://trivy.dev/docs/latest/guide/configuration/reporting/> |
| 11 | Trivy Filtering Documentation | severity、status、ignore、VEX | <https://trivy.dev/docs/latest/guide/configuration/filtering/> |
| 12 | Trivy Kubernetes Documentation | `trivy k8s`、compliance、KBOM | <https://trivy.dev/docs/latest/guide/target/kubernetes/> |
| 13 | Trivy Air-Gap / Network | 離線與網路考量 | <https://trivy.dev/docs/latest/guide/advanced/air-gap/> |
| 14 | Trivy CLI Reference（image） | flag 完整清單 | <https://trivy.dev/docs/latest/guide/references/configuration/cli/trivy_image/> |
| 15 | Trivy CHANGELOG | 版本差異、Breaking Changes | <https://github.com/aquasecurity/trivy/blob/main/CHANGELOG.md> |
| 16 | Trivy v0.75.0 Release Discussion | v0.75 Highlights | <https://github.com/aquasecurity/trivy/discussions/11333> |
| 17 | GHSA-69fq-xp46-6x23 | 2026-03 供應鏈事件官方公告 | <https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23> |
| 18 | Trivy Operator | 叢集持續掃描 | <https://github.com/aquasecurity/trivy-operator> |
| 19 | Trivy Operator Documentation | Operator 文件 | <https://aquasecurity.github.io/trivy-operator/latest> |
| 20 | Trivy GitHub Action | trivy-action | <https://github.com/aquasecurity/trivy-action> |
| 21 | setup-trivy | 安裝 Trivy 的 Action | <https://github.com/aquasecurity/setup-trivy> |
| 22 | trivy-aws | AWS 掃描 plugin | <https://github.com/aquasecurity/trivy-aws> |
| 23 | CycloneDX | SBOM 標準 | <https://cyclonedx.org/> |
| 24 | SPDX | SBOM 標準 | <https://spdx.dev/> |
| 25 | SARIF 2.1.0（OASIS） | 靜態分析結果交換格式 | <https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html> |
| 26 | OpenVEX | VEX 規格 | <https://openvex.dev/> |
| 27 | OWASP Top Ten | Web 應用風險分類 | <https://owasp.org/www-project-top-ten/> |
| 28 | Kubernetes Pod Security Standards | PSS Baseline / Restricted | <https://kubernetes.io/docs/concepts/security/pod-security-standards/> |
| 29 | CNCF | Cloud Native 生態系 | <https://www.cncf.io/> |
| 30 | NIST SP 800-218（SSDF） | 安全軟體開發框架 | <https://csrc.nist.gov/pubs/sp/800/218/final> |
| 31 | CISA SBOM | SBOM 政策與資源 | <https://www.cisa.gov/sbom> |
| 32 | GitHub Actions Secure Use | 第三方 Action 以 SHA 固定 | <https://docs.github.com/en/actions/reference/security/secure-use#using-third-party-actions> |
| 33 | Sigstore / cosign | 簽章與驗證 | <https://docs.sigstore.dev/> |
| 34 | ORAS | OCI artifact 下載（DB 離線） | <https://oras.land/> |
| 35 | ArchUnit | 架構測試（補足 Trivy 不負責的部分） | <https://www.archunit.org/> |
| 36 | Trivy MCP Server Plugin | MCP Server、傳輸模式、IDE 整合 | <https://github.com/aquasecurity/trivy-mcp> |
| 37 | Trivy VS Code Extension | IDE 內掃描 | <https://github.com/aquasecurity/trivy-vscode-extension> |
| 38 | setup-trivy Releases | v0.3.0 / v0.3.1 變更說明 | <https://github.com/aquasecurity/setup-trivy/releases> |
| 39 | trivy-action v0.36.0 action.yaml | `version` 預設值、內部 setup-trivy pin | <https://github.com/aquasecurity/trivy-action/blob/v0.36.0/action.yaml> |
| 40 | Trivy Scanning Coverage | 支援的 OS 與語言 | <https://trivy.dev/docs/latest/coverage/> |

---

## Technical Review Checklist

> 撰寫完成後依下列項目自我審查。「備註」欄記錄查證依據或已知限制。

| 狀態 | 項目 | 備註 |
|------|------|------|
| [x] | 所有內容都在同一個 Markdown 文件 | 單一檔案 |
| [x] | 沒有要求使用者另外閱讀必要文件 | 外部連結僅為延伸參考 |
| [x] | Trivy 版本已確認 | v0.75.0（GitHub Release、CHANGELOG 2026-10-01） |
| [x] | CLI 指令已確認 | 對照 CLI Reference（image、kubernetes、sbom、vm、convert） |
| [x] | Targets 已確認 | 官方 Target 清單：Image、FS、Rootfs、Repo、VM、K8s、SBOM |
| [x] | Scanners 已確認 | vuln、misconfig、secret、license、crypto（Experimental）、k8s rbac |
| [x] | Vulnerability 已確認 | Severity、Status、`--vuln-severity-source`、`--exit-on-eol` |
| [x] | Misconfiguration 已確認 | misconfig-scanners 預設清單 |
| [x] | Secret 已確認 | `trivy-secret.yaml`、v0.71 / v0.72 新規則 |
| [x] | License 已確認 | 分類與 Severity、`--license-full` |
| [x] | SBOM 已確認 | cyclonedx、spdx、spdx-json、`trivy sbom` |
| [x] | Kubernetes 已確認 | Experimental、RBAC、compliance ID |
| [x] | Cloud 能力已確認 | `trivy aws` 自 v0.53 移出核心；plugin v0.15.1 |
| [x] | CI/CD 已確認 | 官方 Tutorials 清單 |
| [x] | GitHub Actions 已確認 | trivy-action v0.36.0 inputs（`version` 預設 v0.70.0）、setup-trivy v0.3.1、快取、SHA pin |
| [x] | Trivy Operator 已確認 | v0.34.0（內建 Trivy 0.74.0）、Helm Chart 0.36.0、報告類型 |
| [x] | Trivy MCP Server 已確認 | trivy-mcp v0.0.20、安裝與傳輸模式、Guardrail（26.4–26.6、30.4） |
| [x] | Configuration 已確認 | 優先順序、`--generate-default-config` |
| [x] | Cache / DB 已確認 | 預設 repository、skip / download flags |
| [x] | Report Format 已確認 | `--format` 允許值、convert 限制 |
| [x] | SARIF 已確認 | SARIF 2.1.0、Code Scanning 權限 |
| [x] | Reverse Engineering 已涵蓋 | 第 24、48 章 |
| [x] | Framework Upgrade 已涵蓋 | 第 25、49 章 |
| [x] | AI Agent 已涵蓋 | 第 26–30、42、47、54、55 章 |
| [x] | AI Guardrail 已涵蓋 | 第 30 章 |
| [x] | SSDLC 已涵蓋 | 第 31 章 |
| [x] | Enterprise Governance 已涵蓋 | 第 37、59 章 |
| [x] | Exception Management 已涵蓋 | 第 16、39 章 |
| [x] | Upgrade Strategy 已涵蓋 | 第 41、42 章 |
| [x] | Troubleshooting 已涵蓋 | 第 44 章、附錄 D |
| [x] | Labs 已涵蓋 | Lab 1–16 |
| [x] | Checklist 已涵蓋 | 第 53 章、附錄 C |
| [x] | Reference Architecture 已涵蓋 | 第 35、60 章、附錄 E |
| [x] | 沒有虛構功能 | 未查證項目以「官方資料未說明」或「以實際版本為準」標示 |
| [x] | 沒有把企業政策說成 Trivy 官方政策 | 全書以【官方】/【企業建議】標示 |
| [x] | 沒有暴露真實 Credential | 全部使用佔位符；Lab 3 以腳本隨機產生假資料 |
| [x] | 所有重要引用都有來源 | References 40 項 |
| [x] | Mermaid Diagram 語法正確 | 標籤以雙引號包覆，避免特殊字元 |
| [x] | Markdown 語法正確 | 依目錄 `.markdownlint.jsonc` 檢查 |

### 已知限制與使用前需再確認的項目

| 項目 | 原因 | 建議 |
|------|------|------|
| Trivy Operator Helm values 鍵名 | 依 Chart 版本變動 | 以 `helm show values` 核對 |
| `trivy.yaml` 各鍵名 | 依版本變動 | 以 `--generate-default-config` 核對 |
| Windows Release 檔名 | 官方文件與 Advisory 的檔名寫法不同 | 以 Release 頁面實際檔名為準 |
| Misconfiguration check ID 範例 | trivy-checks 版本可能調整 ID | 以實際 JSON 報告為準 |
| OWASP Top 10 分類名稱 | 依 OWASP 官方版本 | 以 OWASP 官網為準 |
| GitHub Actions `<SHA>` 佔位符 | 需由使用者取得當下正確 SHA | 以 `git ls-remote` 取得並由 Dependabot 維護 |
