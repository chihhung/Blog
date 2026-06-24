+++
date = '2026-06-24T20:02:18+08:00'
draft = false
title = 'Gitlab and Gitlab Cli 教學手冊'
tags = ['教學', '工具']
categories = ['教學']
+++

# GitLab 與 GitLab CLI（glab）完整企業級教學手冊

> 本手冊以 2026 年最新版 GitLab（GitLab.com SaaS / GitLab Self-Managed / GitLab Dedicated）、GitLab CLI（`glab`）、GitLab Duo、GitLab CI/CD、GitLab Runner、GitLab Kubernetes Agent、GitLab Security、GitLab API、GitLab MCP Server 等官方文件與最佳實務為基礎撰寫，目標是讓初學者到資深架構師、DevOps / Platform / SRE 團隊都能在同一份文件中找到所需的知識與可直接複製貼上的操作指令。
>
> 📌 **使用建議**：
> - 第一次接觸 GitLab 的同仁，建議依序閱讀第一章～第七章。
> - 已熟悉 Git 的開發者，可直接從第四章（glab CLI）開始。
> - DevOps / Platform / SRE 團隊，請聚焦第八、十一、十九、二十章。
> - 想了解 AI 協作開發（Claude Code、GitHub Copilot、MCP）的同仁，請見第十三～十八章。
> - 本文件與既有的《GitLab使用教學.md》為獨立文件，內容不互相依賴，可單獨閱讀。

---

## 📖 目錄

> 💡 點擊章節可跳至本文對應位置；每個章節下方的子項為該章節的小節（##）連結。

- [第一章 GitLab 介紹](#第一章-gitlab-介紹)
  - [1.1 GitLab 發展歷史](#11-gitlab-發展歷史)
  - [1.2 GitLab 核心理念](#12-gitlab-核心理念)
  - [1.3 GitLab 與 GitHub 比較](#13-gitlab-與-github-比較)
  - [1.4 GitLab 與 Azure DevOps 比較](#14-gitlab-與-azure-devops-比較)
  - [1.5 GitLab 與 Bitbucket 比較](#15-gitlab-與-bitbucket-比較)
  - [1.6 GitLab SaaS / Self-Managed / Dedicated 差異比較](#16-gitlab-saas--self-managed--dedicated-差異比較)
- [第二章 GitLab 整體架構](#第二章-gitlab-整體架構)
  - [2.1 端到端架構總覽](#21-端到端架構總覽)
  - [2.2 核心元件運作方式](#22-核心元件運作方式)
  - [2.3 GitLab Architecture Tiers（部署規模分級）](#23-gitlab-architecture-tiers部署規模分級)
- [第三章 GitLab 安裝與部署](#第三章-gitlab-安裝與部署)
  - [3.1 GitLab CE 與 EE 差異](#31-gitlab-ce-與-ee-差異)
  - [3.2 Linux Package（Omnibus）安裝 — Ubuntu](#32-linux-packageomnibus安裝--ubuntu)
  - [3.3 Linux Package 安裝 — RHEL / Rocky Linux](#33-linux-package-安裝--rhel--rocky-linux)
  - [3.4 Docker 安裝](#34-docker-安裝)
  - [3.5 Podman 安裝（Rootless）](#35-podman-安裝rootless)
  - [3.6 Helm Chart（Kubernetes）安裝概覽](#36-helm-chartkubernetes安裝概覽)
- [第四章 GitLab CLI（glab）](#第四章-gitlab-cliglab)
  - [4.1 glab 是什麼](#41-glab-是什麼)
  - [4.2 glab 架構](#42-glab-架構)
  - [4.3 glab 主要功能分類](#43-glab-主要功能分類)
  - [4.3.1 glab 指令穩定度分級（Stable / Beta / Experimental）](#431-glab-指令穩定度分級stable--beta--experimental)
  - [4.4 安裝 glab](#44-安裝-glab)
  - [4.5 登入與認證](#45-登入與認證)
- [第五章 GitLab CLI 指令大全](#第五章-gitlab-cli-指令大全)
  - [5.1 `glab auth` — 認證管理](#51-glab-auth--認證管理)
  - [5.2 `glab repo` — 專案管理](#52-glab-repo--專案管理)
  - [5.3 `glab mr` — Merge Request](#53-glab-mr--merge-request)
  - [5.4 `glab issue` — Issue 管理](#54-glab-issue--issue-管理)
  - [5.5 `glab pipeline` 與 `glab ci` — CI/CD 操作](#55-glab-pipeline-與-glab-ci--cicd-操作)
  - [5.6 `glab release` — 版本發布](#56-glab-release--版本發布)
  - [5.7 `glab variable` — CI/CD 變數管理](#57-glab-variable--cicd-變數管理)
  - [5.8 `glab project` — 專案層級設定](#58-glab-project--專案層級設定)
  - [5.9 `glab api` — 通用 API 呼叫](#59-glab-api--通用-api-呼叫)
  - [5.10 `glab duo` — GitLab Duo AI 功能](#510-glab-duo--gitlab-duo-ai-功能)
  - [5.11 `glab mcp` — 啟動 MCP Server](#511-glab-mcp--啟動-mcp-server)
  - [5.12 `glab stack` — Stacked Diff 管理](#512-glab-stack--stacked-diff-管理)
  - [5.13 `glab search` — 跨專案搜尋](#513-glab-search--跨專案搜尋)
  - [5.14 `glab schedule` — Pipeline 排程管理](#514-glab-schedule--pipeline-排程管理)
  - [5.15 `glab runner` — Runner 管理](#515-glab-runner--runner-管理)
  - [5.16 `glab orbit` — Knowledge Graph 查詢](#516-glab-orbit--knowledge-graph-查詢)
  - [5.17 `glab skills` — Agent 技能管理](#517-glab-skills--agent-技能管理)
  - [5.18 `glab attestation` — 軟體供應鏈驗證](#518-glab-attestation--軟體供應鏈驗證)
  - [5.19 `glab cluster` — Kubernetes Agent 管理](#519-glab-cluster--kubernetes-agent-管理)
  - [5.20 `glab container-registry` — 容器倉庫管理](#520-glab-container-registry--容器倉庫管理)
  - [5.21 `glab incident` — 事件管理](#521-glab-incident--事件管理)
  - [5.22 `glab work-items` — 統一規劃項目](#522-glab-work-items--統一規劃項目)
  - [5.23 其他工具型指令速查](#523-其他工具型指令速查)
- [第六章 GitLab Flow](#第六章-gitlab-flow)
  - [6.1 三種主流分支策略比較](#61-三種主流分支策略比較)
  - [6.2 GitLab Flow 的兩種變體](#62-gitlab-flow-的兩種變體)
  - [6.3 企業建議](#63-企業建議)
- [第七章 CI/CD](#第七章-cicd)
  - [7.1 `.gitlab-ci.yml` 核心概念](#71-gitlab-ciyml-核心概念)
  - [7.2 Java / Spring Boot 完整 CI/CD 範例](#72-java--spring-boot-完整-cicd-範例)
  - [7.3 Node.js / Vue 完整 CI/CD 範例](#73-nodejs--vue-完整-cicd-範例)
  - [7.4 React 完整 CI/CD 範例](#74-react-完整-cicd-範例)
  - [7.5 Python 完整 CI/CD 範例](#75-python-完整-cicd-範例)
  - [7.6 `include` 拆分與共用範本](#76-include-拆分與共用範本)
- [第八章 GitLab Runner](#第八章-gitlab-runner)
  - [8.1 Runner 類型總覽](#81-runner-類型總覽)
  - [8.2 安裝 GitLab Runner](#82-安裝-gitlab-runner)
  - [8.3 設定要點](#83-設定要點)
  - [8.4 維護、升級、故障排除](#84-維護升級故障排除)
- [第九章 Container Registry](#第九章-container-registry)
  - [9.1 GitLab Container Registry 概念](#91-gitlab-container-registry-概念)
  - [9.2 基本操作](#92-基本操作)
  - [9.3 Image 掃描（Container Scanning）](#93-image-掃描container-scanning)
  - [9.4 Image Promotion（多環境晉升流程）](#94-image-promotion多環境晉升流程)
  - [9.5 最佳實務](#95-最佳實務)
  - [9.6 Container Virtual Registry（聚合上游倉庫）](#96-container-virtual-registry聚合上游倉庫)
  - [9.7 多架構 Image 支援（Multi-Architecture）](#97-多架構-image-支援multi-architecture)
- [第十章 Package Registry](#第十章-package-registry)
  - [10.1 支援的套件格式總覽](#101-支援的套件格式總覽)
  - [10.2 Maven 設定與發布](#102-maven-設定與發布)
  - [10.3 npm / pnpm 設定與發布](#103-npm--pnpm-設定與發布)
  - [10.4 NuGet 發布](#104-nuget-發布)
  - [10.5 PyPI 發布](#105-pypi-發布)
  - [10.6 Generic Package（任意檔案）](#106-generic-package任意檔案)
- [第十一章 GitLab Security](#第十一章-gitlab-security)
  - [11.1 GitLab 安全掃描總覽](#111-gitlab-安全掃描總覽)
  - [11.2 SAST（靜態應用程式安全測試）](#112-sast靜態應用程式安全測試)
  - [11.3 DAST（動態應用程式安全測試）](#113-dast動態應用程式安全測試)
  - [11.4 Dependency Scanning](#114-dependency-scanning)
  - [11.4.1 AI 輔助安全：Agentic SAST 與 Duo 誤報偵測](#1141-ai-輔助安全agentic-sast-與-duo-誤報偵測)
  - [11.5 Container Scanning](#115-container-scanning)
  - [11.6 Secret Detection](#116-secret-detection)
  - [11.7 License Compliance](#117-license-compliance)
  - [11.8 Security Dashboard 與 Vulnerability Management](#118-security-dashboard-與-vulnerability-management)
  - [11.9 企業導入策略](#119-企業導入策略)
- [第十二章 GitLab API](#第十二章-gitlab-api)
  - [12.1 REST API 與 GraphQL API 選用建議](#121-rest-api-與-graphql-api-選用建議)
  - [12.2 Access Token 種類](#122-access-token-種類)
  - [12.3 curl 範例](#123-curl-範例)
  - [12.4 Java / Spring Boot 範例](#124-java--spring-boot-範例)
  - [12.5 Python 範例](#125-python-範例)
  - [12.6 TypeScript 範例](#126-typescript-範例)
- [第十三章 GitLab Duo](#第十三章-gitlab-duo)
  - [13.1 GitLab Duo 功能總覽](#131-gitlab-duo-功能總覽)
  - [13.2 GitLab Duo Chat](#132-gitlab-duo-chat)
  - [13.3 Code Suggestions（程式碼建議）](#133-code-suggestions程式碼建議)
  - [13.4 Code Review（MR 自動審查）](#134-code-reviewmr-自動審查)
  - [13.5 Vulnerability Explanation](#135-vulnerability-explanation)
  - [13.6 Test Generation 與 Refactoring](#136-test-generation-與-refactoring)
  - [13.7 Prompt Engineering 最佳實務](#137-prompt-engineering-最佳實務)
- [第十四章 GitLab + Claude Code](#第十四章-gitlab--claude-code)
  - [14.1 整合架構總覽](#141-整合架構總覽)
  - [14.2 實戰案例：Claude Code 自動建立並提交 Merge Request](#142-實戰案例claude-code-自動建立並提交-merge-request)
  - [14.3 實戰案例：Claude Code 自動 Review 程式碼](#143-實戰案例claude-code-自動-review-程式碼)
  - [14.4 實戰案例：Pipeline 失敗時自動診斷](#144-實戰案例pipeline-失敗時自動診斷)
  - [14.5 CLAUDE.md 專案規範整合建議](#145-claudemd-專案規範整合建議)
- [第十五章 GitLab + GitHub Copilot](#第十五章-gitlab--github-copilot)
  - [15.1 為什麼會在 GitLab 上使用 GitHub Copilot](#151-為什麼會在-gitlab-上使用-github-copilot)
  - [15.2 Agent Mode 與 Coding Agent 操作模式](#152-agent-mode-與-coding-agent-操作模式)
  - [15.3 如何與 GitLab 協作（實務整合建議）](#153-如何與-gitlab-協作實務整合建議)
- [第十六章 GitLab + MCP](#第十六章-gitlab--mcp)
  - [16.1 Model Context Protocol 簡介](#161-model-context-protocol-簡介)
  - [16.2 GitLab MCP Server 現況與安裝](#162-gitlab-mcp-server-現況與安裝)
  - [16.3 設定 Claude Code 連接 GitLab MCP Server](#163-設定-claude-code-連接-gitlab-mcp-server)
  - [16.4 權限管理](#164-權限管理)
  - [16.5 實際案例：多步驟 Agent 工作流程](#165-實際案例多步驟-agent-工作流程)
  - [16.6 GitLab Orbit（Knowledge Graph）與 AI Agent](#166-gitlab-orbitknowledge-graph與-ai-agent)
- [第十七章 AI 協助 Legacy System 逆向工程](#第十七章-ai-協助-legacy-system-逆向工程)
  - [17.1 為什麼 Legacy System 逆向工程適合導入 AI](#171-為什麼-legacy-system-逆向工程適合導入-ai)
  - [17.2 實戰步驟：將 Legacy 程式碼匯入 GitLab 並建立分析基線](#172-實戰步驟將-legacy-程式碼匯入-gitlab-並建立分析基線)
  - [17.3 實戰案例：AI Agent 自動分析 Legacy System](#173-實戰案例ai-agent-自動分析-legacy-system)
  - [17.4 各 Legacy 技術的 AI 逆向工程要點](#174-各-legacy-技術的-ai-逆向工程要點)
  - [17.5 文件生成與架構分析範本](#175-文件生成與架構分析範本)
  - [17.6 逆向工程後的重構規劃](#176-逆向工程後的重構規劃)
- [第十八章 Framework 升級專案](#第十八章-framework-升級專案)
  - [18.1 升級專案的 GitLab 治理框架](#181-升級專案的-gitlab-治理框架)
  - [18.2 Spring Boot 2 → 3 / Java 8 → 21 實戰流程](#182-spring-boot-2--3--java-8--21-實戰流程)
  - [18.3 Vue2 → Vue3 升級實戰流程](#183-vue2--vue3-升級實戰流程)
  - [18.4 Angular 升級實戰流程](#184-angular-升級實戰流程)
  - [18.5 升級專案的企業治理建議](#185-升級專案的企業治理建議)
- [第十九章 大型企業 DevSecOps 平台設計](#第十九章-大型企業-devsecops-平台設計)
  - [19.1 依規模分級的架構設計原則](#191-依規模分級的架構設計原則)
  - [19.2 大型企業架構圖](#192-大型企業架構圖)
  - [19.3 權限模型設計](#193-權限模型設計)
  - [19.4 Group 策略與 Project 策略](#194-group-策略與-project-策略)
  - [19.5 Branch 策略](#195-branch-策略)
- [第二十章 GitLab 維運手冊](#第二十章-gitlab-維運手冊)
  - [20.1 備份與還原](#201-備份與還原)
  - [20.2 監控（Prometheus + Grafana）](#202-監控prometheus--grafana)
  - [20.3 Logging](#203-logging)
  - [20.4 升級](#204-升級)
  - [20.5 高可用性（HA）與災難復原（DR）](#205-高可用性ha與災難復原dr)
- [第二十一章 GitLab 最佳實務](#第二十一章-gitlab-最佳實務)
  - [21.1 命名規範](#211-命名規範)
  - [21.2 Branch Strategy](#212-branch-strategy)
  - [21.3 MR Strategy](#213-mr-strategy)
  - [21.4 Pipeline Strategy](#214-pipeline-strategy)
  - [21.5 Release Strategy](#215-release-strategy)
  - [21.6 Security Strategy](#216-security-strategy)
- [第二十二章 常見問題 FAQ](#第二十二章-常見問題-faq)
  - [22.1 開發類](#221-開發類)
  - [22.2 CI/CD 類](#222-cicd-類)
  - [22.3 Security 類](#223-security-類)
  - [22.4 Runner 類](#224-runner-類)
  - [22.5 Kubernetes 類](#225-kubernetes-類)
  - [22.6 AI 類](#226-ai-類)
  - [22.7 GitLab Duo 類](#227-gitlab-duo-類)
  - [22.8 glab 類](#228-glab-類)
- [第二十三章 附錄](#第二十三章-附錄)
  - [23.1 常用 glab 指令速查表](#231-常用-glab-指令速查表)
  - [23.2 CI/CD 通用範本](#232-cicd-通用範本)
  - [23.3 Spring Boot 範本](#233-spring-boot-範本)
  - [23.4 Vue3 範本](#234-vue3-範本)
  - [23.5 Kubernetes 範本](#235-kubernetes-範本)
  - [23.6 Docker 範本（多階段建置）](#236-docker-範本多階段建置)
  - [23.7 Helm 範本](#237-helm-範本)
  - [23.8 十大 AI Agent 實戰情境總覽](#238-十大-ai-agent-實戰情境總覽)
  - [23.9 企業導入檢查清單](#239-企業導入檢查清單)

---

# 第一章 GitLab 介紹

## 1.1 GitLab 發展歷史

GitLab 最初由 Dmitriy Zaporozhets 與 Valery Sizov 於 2011 年以 Ruby on Rails 開發，作為一套開源的 Git 版本控制管理工具。早期僅是「GitHub 的開源替代品」，但 GitLab 團隊很快意識到軟體交付不只是「管程式碼」，而是一個從規劃、開發、測試、安全掃描、部署到監控的完整生命週期。

關鍵發展里程碑：

| 年份 | 重要事件 |
|---|---|
| 2011 | GitLab 專案誕生，作為自架（self-hosted）Git 管理工具 |
| 2014 | GitLab Inc. 成立，推出 GitLab Enterprise Edition（EE） |
| 2015 | 推出 GitLab CI，內建 CI/CD 能力（不需額外裝 Jenkins） |
| 2017 | Auto DevOps、Container Registry 上線 |
| 2018 | GitLab.com 達到百萬使用者規模；推出 GitLab Geo |
| 2019 | 收購 Gitter、Peach Tech、Fuzzit，強化即時通訊與安全測試 |
| 2021 | NASDAQ 上市（GTLB） |
| 2023 | 推出 GitLab Duo（AI 輔助開發功能套件） |
| 2024 | GitLab Duo Chat、Code Suggestions 全面 GA；推出 GitLab Duo Workflow（Agentic AI） |
| 2025 | GitLab MCP Server 由 Experimental 起步，逐步開放給 Claude Code、GitHub Copilot 等外部 AI Agent 透過 MCP 協定操作 GitLab 資源 |
| 2026 | GitLab Duo Agent Platform 正式 GA（Foundational/Custom/External Agents 三層架構），GitLab MCP Server 升級為 Beta 並支援 HTTP transport；GitLab Orbit（Knowledge Graph）以 Beta 形式推出；目前主線版本為 GitLab 19.x 系列（詳見第十三、十六章） |

GitLab 的核心精神之一是「One DevOps Platform」——將原本散落在 Jira（規劃）、GitHub（程式碼）、Jenkins（CI/CD）、SonarQube（程式碼品質）、Nexus（套件管理）、Snyk（安全掃描）的工具鏈，整合成單一平台、單一資料庫、單一權限模型。

## 1.2 GitLab 核心理念

GitLab 的設計理念可以歸納為以下幾點：

1. **單一應用程式（Single Application）**：所有 DevSecOps 流程都在同一個 Web UI、同一個資料模型下運作，避免「工具鏈拼接」帶來的資料斷層與整合成本。
2. **內建而非外掛（Built-in, not bolted-on）**：CI/CD、Security Scanning、Package Registry、Container Registry 都是 GitLab 原生功能，而非透過外部 plugin 串接。
3. **從 Idea 到 Production 的完整循環**：涵蓋 Plan → Create → Verify → Package → Secure → Release → Configure → Monitor → Govern 九大階段。
4. **DevSecOps 左移（Shift Left Security）**：安全掃描從開發階段就介入，而不是上線前才補檢查。
5. **開源核心（Open Core）**：核心功能開源（GitLab CE），進階企業功能（合規、進階權限、AI）則在 EE / Ultimate 授權中。
6. **AI 原生化（AI-native DevSecOps）**：自 GitLab Duo 推出後，GitLab 將生成式 AI 視為平台「第十個階段」，深度整合在 MR 審查、漏洞解釋、測試產生、Chat 問答等每一個環節。

### DevSecOps 平台概念圖

```mermaid
flowchart LR
    subgraph Plan["📋 Plan"]
        A1[Issues]
        A2[Epics]
        A3[Roadmap]
    end
    subgraph Create["💻 Create"]
        B1[Repository]
        B2[Merge Request]
        B3[Code Review]
        B4[GitLab Duo Code Suggestions]
    end
    subgraph Verify["✅ Verify"]
        C1[CI/CD Pipeline]
        C2[Unit/Integration Test]
        C3[Code Quality]
    end
    subgraph SecureStage["🔒 Secure"]
        D1[SAST]
        D2[DAST]
        D3[Dependency Scanning]
        D4[Secret Detection]
    end
    subgraph Package["📦 Package"]
        E1[Container Registry]
        E2[Package Registry]
    end
    subgraph Release["🚀 Release"]
        F1[Deployment]
        F2[Feature Flags]
        F3[Release Note]
    end
    subgraph ConfigureStage["⚙️ Configure"]
        G1[GitLab Agent for Kubernetes]
        G2[Infrastructure as Code]
    end
    subgraph Monitor["📊 Monitor"]
        H1[Metrics]
        H2[Logs]
        H3[Incident Management]
    end
    subgraph Govern["🛡️ Govern"]
        I1[Compliance]
        I2[Audit Events]
        I3[Vulnerability Management]
    end

    Plan --> Create --> Verify --> SecureStage --> Package --> Release --> ConfigureStage --> Monitor --> Govern
    Govern -.回饋.-> Plan
```

> 💡 **實務案例**：某金融業客戶將原本 Jira + GitHub + Jenkins + Nexus + Checkmarx 的五個系統整合進 GitLab Ultimate，MR 合併到上線的平均交付時間（Lead Time for Changes）從 9 天降為 2.3 天，主要原因是省去了系統間人工同步狀態與等待整合測試環境排隊的時間。

## 1.3 GitLab 與 GitHub 比較

| 比較項目 | GitLab | GitHub |
|---|---|---|
| 定位 | One DevSecOps Platform（全生命週期） | 程式碼協作平台，CI/CD 與安全多透過 Actions/Marketplace 擴充 |
| CI/CD | 原生內建（`.gitlab-ci.yml`），無需額外平台 | GitHub Actions（YAML workflow），生態系豐富 |
| 自架能力 | CE/EE 皆可完整自架（含 HA、Geo） | GitHub Enterprise Server 可自架，但功能更新通常落後 SaaS |
| 內建安全掃描 | SAST/DAST/Dependency/Container/Secret 皆原生內建 | 需搭配 CodeQL、Dependabot、第三方 Action |
| 套件/容器倉庫 | 原生 Container Registry + Package Registry（Maven/npm/NuGet/PyPI...） | GitHub Packages（功能較簡） |
| AI 功能 | GitLab Duo（Chat、Code Suggestions、Vulnerability Explanation、Duo Agent Platform） | GitHub Copilot（Chat、Agent Mode、Coding Agent） |
| Issue/專案管理 | Issue + Epic + Roadmap + Iteration（原生敏捷工具） | Issue + Project（Projects v2），敏捷功能較簡單 |
| 權限模型 | Group → Subgroup → Project 多層繼承，企業治理彈性高 | Organization → Team → Repository |
| MCP 支援 | GitLab MCP Server（官方維護） | GitHub MCP Server（官方維護） |
| CLI 工具 | `glab` | `gh` |

> ⚠️ **注意事項**：GitLab 與 GitHub 的核心差異不在「程式碼管理」，而在於**是否把 CI/CD、安全、套件管理視為一等公民功能**。導入評估時，應計算「整合外部工具的隱性成本」（維運、授權、資料同步），而非只比較授權費用。

## 1.4 GitLab 與 Azure DevOps 比較

| 比較項目 | GitLab | Azure DevOps |
|---|---|---|
| 組成 | 單一整合平台 | Boards / Repos / Pipelines / Artifacts / Test Plans 五個子服務組成 |
| Pipeline 語法 | `.gitlab-ci.yml`（YAML，單一檔案為主，可 `include`） | Azure Pipelines YAML，亦支援 Classic UI 編輯器 |
| 與雲端整合 | 雲中立，對 AWS/GCP/Azure/地端皆友善 | 與 Azure 生態（Entra ID、ACR、AKS）整合最深 |
| Self-Managed | 原生支援（CE/EE 一致架構） | Azure DevOps Server（功能落後 Services 版） |
| 授權模式 | Free / Premium / Ultimate（依使用者數計價） | Basic / Basic+Test Plans（依使用者數＋方案計價） |
| AI 功能 | GitLab Duo | GitHub Copilot for Azure DevOps Boards（透過整合） |

> 💡 **企業選型建議**：若企業已大量採用 Azure 生態（Entra ID 單一登入、AKS、Azure Monitor），Azure DevOps 整合成本較低；但若企業重視「雲中立」與「單一平台 DevSecOps」，GitLab 在自架彈性與安全左移上更具優勢。

## 1.5 GitLab 與 Bitbucket 比較

| 比較項目 | GitLab | Bitbucket |
|---|---|---|
| 定位 | DevSecOps 全生命週期平台 | 程式碼協作為主，搭配 Bitbucket Pipelines |
| CI/CD 能力 | 功能完整、原生 Runner 架構（Docker/K8s/Shell） | Pipelines 功能簡單，適合中小型專案 |
| 安全掃描 | 原生 SAST/DAST/Dependency/Container/Secret | 需搭配 Snyk 等第三方整合 |
| 與 Jira 整合 | 透過 Webhook/Smart Commit 整合（非原生） | 與 Jira 同屬 Atlassian，整合最深 |
| 企業治理 | Group/Subgroup 階層、Compliance Framework | Workspace/Project 階層，治理功能較簡單 |

> 💡 **企業選型建議**：若團隊已重度投資 Atlassian 生態（Jira + Confluence），Bitbucket 整合體驗最順；但若需要「程式碼到上線」單一平台治理與內建安全掃描，GitLab 仍是業界對比中功能最完整的選項之一。

## 1.6 GitLab SaaS / Self-Managed / Dedicated 差異比較

GitLab 提供三種部署形態，企業導入時必須先確認採用哪一種，因為這會直接影響資料主權、維運責任與客製化彈性。

| 項目 | GitLab SaaS（GitLab.com） | GitLab Self-Managed | GitLab Dedicated |
|---|---|---|---|
| 基礎設施擁有者 | GitLab Inc.（多租戶共用） | 企業自己（地端或自己的雲端帳號） | GitLab Inc.（單租戶，部署在客戶選定的 AWS 區域） |
| 維運責任 | GitLab 負責 | 企業自己負責（升級、備份、HA、監控） | GitLab 負責維運，但資料隔離於單租戶環境 |
| 客製化彈性 | 低（不可改原始碼、不可裝外部 plugin） | 最高（可改設定、可裝第三方 Runner/外掛、可客製 Omnibus 設定） | 中（可調部署區域、維護窗口、IP allowlist，不可改核心架構） |
| 資料主權/合規 | 資料存於 GitLab 的雲端（美國/特定區域） | 完全自主（可滿足金融、政府高合規需求） | 可選擇部署區域，滿足部分資料主權需求，但仍由 GitLab 管理基礎設施 |
| 升級頻率 | 持續自動升級（最新功能最快拿到） | 企業自行排程升級（通常落後 SaaS） | GitLab 依約定維護窗口升級 |
| 適合對象 | 新創、中小企業、希望快速上手者 | 高合規、高客製需求的大型企業（金融、政府、醫療） | 想要「免維運」但又需要單租戶隔離與資料主權保證的中大型企業 |
| 典型規模 | 數人～數千人 | 100～10000+ 人皆可 | 通常 500 人以上之企業客戶 |

```mermaid
flowchart TB
    Q1{企業是否有高度資料主權\n/合規要求？}
    Q2{是否有足夠 Platform 團隊\n可長期維運 GitLab？}
    Q3{是否要免維運但仍要\n單租戶隔離？}

    Q1 -- 否 --> SaaS[GitLab SaaS]
    Q1 -- 是 --> Q2
    Q2 -- 是 --> SM[GitLab Self-Managed]
    Q2 -- 否 --> Q3
    Q3 -- 是 --> Dedicated[GitLab Dedicated]
    Q3 -- 否 --> SaaS
```

> ⚠️ **注意事項**：許多企業初期低估了 Self-Managed 的維運成本（PostgreSQL 調校、Gitaly 儲存擴充、Sidekiq Queue 監控、版本升級路徑），導致「省下 SaaS 授權費」卻付出更高的人力與風險成本。導入前務必依第十九、二十章評估 Platform 團隊人力是否足夠。

### ✅ 第一章 Checklist

- [ ] 已理解 GitLab「One DevSecOps Platform」的核心理念，而非僅是程式碼託管工具
- [ ] 已對照 GitHub / Azure DevOps / Bitbucket 比較表，確認導入 GitLab 的具體理由
- [ ] 已根據資料主權、合規、維運人力評估，選定 SaaS / Self-Managed / Dedicated 部署形態
- [ ] 已將 GitLab 九大階段（Plan～Govern）對應到企業現有工具鏈，列出可被取代或整合的系統清單

---

# 第二章 GitLab 整體架構

## 2.1 端到端架構總覽

下圖描繪一個典型企業導入 GitLab 後，從開發者寫程式碼到應用程式上線到生產環境的完整路徑，涵蓋 GitLab 核心服務、Runner、Registry、安全掃描與 Kubernetes 部署。

```mermaid
flowchart LR
    Dev[👨‍💻 Developer]

    subgraph GitLabPlatform["GitLab Platform"]
        direction TB
        Web[Web Service / Workhorse]
        API[API Service]
        Sidekiq[Sidekiq\n非同步背景任務]
        Gitaly[Gitaly\nGit 儲存層]
        Praefect[Praefect\nGitaly HA 路由層]
        PG[(PostgreSQL)]
        Redis[(Redis)]
        ObjStorage[(Object Storage\nS3/MinIO)]
    end

    Runner[🏃 GitLab Runner]
    Registry[📦 Container Registry]
    PkgReg[📦 Package Registry]
    SecurityScan[🔒 Security Scan\nSAST/DAST/Dependency/Secret]
    K8sAgent[GitLab Agent for Kubernetes]
    K8s[☸️ Kubernetes Cluster]
    Prod[🌐 Production Environment]

    Dev -- git push / MR --> Web
    Web --> API
    API --> PG
    API --> Redis
    API --> Sidekiq
    Web --> Gitaly
    Gitaly <--> Praefect
    Sidekiq --> ObjStorage

    API -- 觸發 Pipeline --> Runner
    Runner -- 執行 Job --> SecurityScan
    Runner -- docker build/push --> Registry
    Runner -- mvn/npm publish --> PkgReg
    Runner -- helm/kubectl --> K8sAgent
    K8sAgent --> K8s
    K8s --> Prod

    SecurityScan -- 回報結果 --> API
```

## 2.2 核心元件運作方式

### Web Service（Puma + Workhorse）

GitLab 的前端 Web 服務由 **Puma**（Ruby 應用伺服器）搭配 **GitLab Workhorse**（Go 撰寫的反向代理）組成。Workhorse 負責處理大型檔案上傳（如 Git push 的 pack 檔、LFS 物件）、靜態資源與長連線（例如 CI Job log 即時串流），把這些 I/O 密集工作從 Puma 卸載，讓 Puma 專注處理 Rails 應用邏輯，大幅降低記憶體壓力與回應延遲。

### API Service

GitLab REST API 與 GraphQL API 共用同一套 Rails 應用程式碼（Grape 框架實作 REST，graphql-ruby 實作 GraphQL）。在大型部署中，官方建議將 API 流量與 Web UI 流量分離到不同的 Puma 進程群組（`puma['app_role'] = 'api'` / `'web'`），避免 CI/CD 觸發的大量 API 請求拖慢一般使用者的網頁操作體驗。

### Sidekiq

Sidekiq 是 GitLab 的背景工作佇列引擎，處理所有「不需要即時回應」的工作，例如：Email 通知、Webhook 觸發、Merge Request 的 Merge 動作、Repository Mirror 同步、Elasticsearch 索引更新、CI Pipeline 狀態計算等。Sidekiq 透過 Redis 作為訊息佇列，可依 Queue 類型（`high_priority`, `low_priority`, `mailers` 等）拆分成多個獨立的 Sidekiq 進程進行水平擴展。

> ⚠️ **常見維運陷阱**：當 Sidekiq Queue 堆積（如大量 Webhook 觸發或 Mirror 同步），會造成 MR 合併延遲、通知信延遲。SRE 團隊應針對 `sidekiq_queue_duration_seconds` 等指標設定告警，並評估是否需要依 Queue 類型拆分專屬 Sidekiq Pod/Process。

### PostgreSQL

GitLab 所有結構化資料（使用者、專案、MR、Issue、Pipeline 紀錄、權限）皆儲存在 PostgreSQL。大型部署建議：

- 採用 Patroni 或雲端代管服務（AWS RDS/Aurora、Cloud SQL）實現 HA 與自動容錯切換。
- 啟用 PgBouncer 進行連線池管理，避免 Rails/Sidekiq 大量連線耗盡資料庫連線數。
- 定期執行 `VACUUM` 與監控 Bloat，PostgreSQL 是 GitLab 效能瓶頸最常見的根源之一。

### Redis

Redis 用於：Sidekiq 佇列、Rails Session 快取、Rate Limit 計數、CI/CD 即時狀態快取。大型部署通常會將 Redis 依用途拆分為多個獨立實例（Cache / Queues / Shared State / Sessions），避免單一 Redis 成為瓶頸或單點故障。

### Gitaly 與 Praefect

**Gitaly** 是 GitLab 的 Git 儲存與操作層，所有 `git` 操作（clone、push、diff、blame）最終都透過 gRPC 呼叫 Gitaly 完成，而不是直接呼叫檔案系統上的 `git` binary，目的是讓儲存層可以水平擴展並支援多種儲存後端。

**Praefect** 是 Gitaly Cluster 的路由與複製管理層，負責：

- 將寫入請求（push）同步複製到多個 Gitaly 節點（Replication Factor，通常設定 3）。
- 提供讀取請求的負載平衡與一致性檢查（Strong Consistency via Raft-like voting）。
- 偵測 Gitaly 節點故障並自動將流量導向健康節點，達成儲存層 HA。

```mermaid
flowchart TB
    Client[Git Client / Workhorse]
    Praefect[Praefect\n路由 + 複製管理]
    G1[Gitaly Node 1\nPrimary]
    G2[Gitaly Node 2\nSecondary]
    G3[Gitaly Node 3\nSecondary]
    PG2[(Praefect PostgreSQL\n儲存複製狀態)]

    Client --> Praefect
    Praefect --> G1
    Praefect --> G2
    Praefect --> G3
    Praefect --> PG2
    G1 -. 複製 .-> G2
    G1 -. 複製 .-> G3
```

### Object Storage

大型部署必須將 CI/CD Artifacts、LFS 物件、Container Registry 影像層、Package Registry 套件、使用者上傳檔案（Avatar、附件）等全部儲存到 S3 相容的 Object Storage（AWS S3、MinIO、GCS、Azure Blob），而非本機磁碟，原因：

1. 讓 GitLab 應用層（Web/Sidekiq/Runner）可以無狀態化，方便水平擴展與滾動升級。
2. 避免單機磁碟容量爆滿造成服務中斷。
3. 搭配雲端原生的備份、生命週期管理（如冷儲存歸檔）能力。

> 💡 **實務案例**：某製造業客戶在 PoC 階段使用本機磁碟儲存 Artifacts，三個月後因建置產出的 Docker Image 與測試報表暴增，磁碟用量從 50GB 飆升到 800GB，導致硬碟告警與服務中斷。改用 MinIO 後，應用伺服器磁碟使用量穩定維持在 20GB 以下。

## 2.3 GitLab Architecture Tiers（部署規模分級）

GitLab 官方依使用者規模提供參考架構（Reference Architecture），常見分級：

| 規模 | 使用者數 | 建議架構 |
|---|---|---|
| Small | < 1,000 | 單機（Linux package 一體式安裝），垂直擴展 CPU/Memory |
| Medium | 1,000 ~ 5,000 | 拆分 PostgreSQL / Redis / Gitaly 為獨立節點 |
| Large | 5,000 ~ 10,000 | 多台 Web/Sidekiq 節點 + Gitaly Cluster + Praefect + PgBouncer |
| Extra Large | 10,000 ~ 50,000+ | 全元件水平擴展、跨可用區、Geo 多地域複寫、專用 Object Storage 叢集 |

> 💡 **企業導入建議**：架構規模不是只看「使用者人數」，更要看 **CI/CD Job 並發量** 與 **Git 操作頻率**。一個 200 人但每天觸發上萬次 Pipeline Job 的團隊，所需的 Runner 與 Gitaly 容量可能遠超過一個 2000 人但 CI 使用率低的團隊。此外，Reference Architecture 的建議節點數與規格會隨 GitLab 大版號（目前主線為 19.x 系列）持續微調，尤其是導入 GitLab Duo Agent Platform、Orbit 等 AI 功能後，Sidekiq 與資料庫的負載特徵會與純 Git/CI 工作負載不同，建議每次規劃容量時直接查閱當下安裝版本對應的官方 Reference Architecture 頁面，而非只依賴本表的靜態分級。

### ✅ 第二章 Checklist

- [ ] 已理解 Web/API/Sidekiq/PostgreSQL/Redis/Gitaly/Praefect/Object Storage 各元件職責
- [ ] 已確認目前（或預計）使用者規模對應到哪一個 Reference Architecture 分級
- [ ] 已評估 CI/CD 並發量是否會讓 Runner、Gitaly 成為效能瓶頸
- [ ] 已規劃 Object Storage（而非本機磁碟）作為 Artifacts/LFS/Registry 的儲存後端

---

# 第三章 GitLab 安裝與部署

## 3.1 GitLab CE 與 EE 差異

GitLab 採用 **Open Core** 模式：

- **GitLab CE（Community Edition）**：開源、免費，包含 Git 管理、基本 CI/CD、基本 Issue/MR 功能。
- **GitLab EE（Enterprise Edition）**：在 CE 基礎上加上 Premium / Ultimate 授權功能，例如：進階權限（Protected Environments、Approval Rules）、Epic/Roadmap、GitLab Duo AI 功能、進階安全掃描（DAST、Container Scanning、Dependency Scanning 完整版）、Compliance Framework、Geo 複寫等。

實務上，**GitLab 官方安裝套件（Linux package / Helm Chart / Docker Image）預設安裝的就是 EE 的程式碼**，只是未啟用授權金鑰時功能等同 CE。這代表企業可以先用 CE 等級功能上線，未來只需「貼授權金鑰」即可解鎖 EE 功能，不需要重新安裝。

> ⚠️ **注意事項**：很多企業誤以為「裝 CE 版」未來要升級到 EE 必須重新安裝，其實只要從一開始就用官方 Linux package / Docker Image（內含 EE 程式碼），未來只需在管理後台輸入授權碼即可，無需停機重裝。

## 3.2 Linux Package（Omnibus）安裝 — Ubuntu

以 Ubuntu 22.04 LTS 安裝 GitLab Self-Managed 為例：

```bash
# 1. 安裝必要套件
sudo apt update
sudo apt install -y curl openssh-server ca-certificates tzdata perl postfix

# 2. 加入 GitLab 官方套件庫（EE，含 CE 全部功能）
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

# 3. 安裝 GitLab，並指定外部存取網址
sudo EXTERNAL_URL="https://gitlab.example.com" apt install -y gitlab-ee

# 4. 套用設定並啟動所有服務
sudo gitlab-ctl reconfigure
```

驗證安裝是否成功：

```bash
# 檢查所有服務狀態
sudo gitlab-ctl status

# 預期輸出範例：
# run: gitaly: (pid 1234) 30s; run: log: (pid 1233) 30s
# run: gitlab-workhorse: (pid 1245) 30s; run: log: (pid 1244) 30s
# run: logrotate: (pid 1246) 30s; run: log: (pid 1247) 30s
# run: nginx: (pid 1248) 30s; run: log: (pid 1249) 30s
# run: postgresql: (pid 1250) 30s; run: log: (pid 1251) 30s
# run: puma: (pid 1252) 30s; run: log: (pid 1253) 30s
# run: redis: (pid 1254) 30s; run: log: (pid 1255) 30s
# run: sidekiq: (pid 1256) 30s; run: log: (pid 1257) 30s

# 執行內建健康檢查
sudo gitlab-rake gitlab:check SANITIZE=true

# 取得初始 root 密碼（24 小時內有效）
sudo cat /etc/gitlab/initial_root_password
```

瀏覽器開啟 `https://gitlab.example.com`，使用帳號 `root` 與上述密碼登入。

## 3.3 Linux Package 安裝 — RHEL / Rocky Linux

```bash
# 1. 安裝必要套件
sudo dnf install -y curl policycoreutils openssh-server perl postfix
sudo systemctl enable sshd --now
sudo systemctl enable postfix --now

# 2. 開放防火牆 HTTP/HTTPS/SSH
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload

# 3. 加入官方套件庫
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash

# 4. 安裝
sudo EXTERNAL_URL="https://gitlab.example.com" dnf install -y gitlab-ee

# 5. 套用設定
sudo gitlab-ctl reconfigure
```

> 💡 **RHEL/Rocky 注意事項**：SELinux 預設為 Enforcing 模式時，需確認 Nginx/Puma 監聽埠是否被 SELinux policy 擋下；建議用 `sudo ausearch -m avc -ts recent` 檢查是否有被拒絕的存取，再用 `semanage` 開放對應 port/context，而非直接關閉 SELinux。

## 3.4 Docker 安裝

適合 PoC、開發測試環境，正式生產環境建議使用 Linux package 或 Helm Chart（Kubernetes）。

```bash
mkdir -p /srv/gitlab/{config,logs,data}

docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 2224:22 \
  --name gitlab \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab \
  --volume /srv/gitlab/logs:/var/log/gitlab \
  --volume /srv/gitlab/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ee:latest
```

驗證：

```bash
docker exec -it gitlab gitlab-ctl status
docker logs -f gitlab   # 第一次啟動約需 3-5 分鐘完成 reconfigure
```

亦可使用 `docker-compose.yml`：

```yaml
version: '3.8'
services:
  gitlab:
    image: gitlab/gitlab-ee:latest
    container_name: gitlab
    restart: always
    hostname: gitlab.example.com
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.example.com'
        gitlab_rails['gitlab_shell_ssh_port'] = 2224
    ports:
      - '80:80'
      - '443:443'
      - '2224:22'
    volumes:
      - ./config:/etc/gitlab
      - ./logs:/var/log/gitlab
      - ./data:/var/opt/gitlab
    shm_size: '256m'
```

## 3.5 Podman 安裝（Rootless）

許多企業因安全政策禁止 Docker Daemon 以 root 權限執行，改用 Podman 的 rootless 容器：

```bash
# 以一般使用者（非 root）執行
mkdir -p ~/gitlab/{config,logs,data}

podman run --detach \
  --hostname gitlab.example.com \
  --publish 8443:443 --publish 8080:80 --publish 2224:22 \
  --name gitlab \
  --restart always \
  --volume ~/gitlab/config:/etc/gitlab:Z \
  --volume ~/gitlab/logs:/var/log/gitlab:Z \
  --volume ~/gitlab/data:/var/opt/gitlab:Z \
  --shm-size 256m \
  docker.io/gitlab/gitlab-ee:latest
```

> ⚠️ **注意事項**：rootless Podman 下，容器內部 GitLab 使用的 UID/GID 會對應到主機上啟動使用者的 subuid/subgid 映射範圍，掛載 Volume 時務必加上 `:Z`（SELinux 標籤重新標記）並確認 `/etc/subuid`、`/etc/subgid` 已配置足夠的 UID 範圍，否則會出現權限被拒（Permission Denied）錯誤。建議將服務註冊為 `systemd --user` unit（透過 `podman generate systemd`）以確保開機自動啟動。

驗證安裝（Podman 與 Docker 相同）：

```bash
podman exec -it gitlab gitlab-ctl status
podman exec -it gitlab gitlab-rake gitlab:check SANITIZE=true
```

## 3.6 Helm Chart（Kubernetes）安裝概覽

大型企業正式環境多採用官方 GitLab Helm Chart，將 Web/Sidekiq/Gitaly/Registry 等元件部署為獨立 Pod，搭配雲端代管 PostgreSQL（RDS）、Redis（ElastiCache）、S3 作為外部依賴：

```bash
helm repo add gitlab https://charts.gitlab.io/
helm repo update

helm upgrade --install gitlab gitlab/gitlab \
  --timeout 600s \
  --set global.hosts.domain=example.com \
  --set global.hosts.https=true \
  --set certmanager-issuer.email=devops@example.com \
  --set global.psql.host=gitlab-rds.example.internal \
  --set global.psql.password.secret=gitlab-postgres-secret \
  --set global.redis.host=gitlab-redis.example.internal \
  --set global.appConfig.object_store.enabled=true \
  --set global.appConfig.object_store.connection.secret=gitlab-object-storage \
  -n gitlab --create-namespace
```

驗證：

```bash
kubectl get pods -n gitlab
kubectl logs -n gitlab deploy/gitlab-webservice-default -f
```

> 💡 **企業導入建議**：Kubernetes 部署 GitLab 適合已具備成熟 K8s 維運能力（GitOps、HPA、PodDisruptionBudget、StorageClass 規劃）的 Platform 團隊。若團隊尚無 K8s 維運經驗，建議先以 Linux package 方式上線，待團隊能力到位後再評估遷移，避免「為了用 K8s 而用 K8s」造成維運複雜度不降反升。

### ✅ 第三章 Checklist

- [ ] 已確認要安裝 CE 或 EE（建議一律安裝 EE 套件，未授權時等同 CE 功能）
- [ ] 已依作業系統（Ubuntu/RHEL/Rocky）完成套件庫設定與安裝
- [ ] 已執行 `gitlab-ctl reconfigure` 並用 `gitlab-ctl status` / `gitlab-rake gitlab:check` 驗證所有服務正常
- [ ] 已取得並妥善保管初始 root 密碼，登入後立即更換
- [ ] 已依環境性質（PoC/正式）選擇 Docker、Podman 或 Helm Chart 安裝方式
- [ ] 已規劃外部 PostgreSQL / Redis / Object Storage（正式環境不建議全部使用容器內建元件）

---

# 第四章 GitLab CLI（glab）

## 4.1 glab 是什麼

`glab` 是 GitLab 官方維護的命令列工具，讓開發者可以**完全不離開終端機**完成 Merge Request、Issue、Pipeline、Release 等操作，定位上等同於 GitHub 的 `gh`。對於重度使用終端機、或想將 GitLab 操作整合進 Shell Script / AI Agent 工作流的工程師而言，`glab` 是不可或缺的工具。

`glab` 以 Go 語言撰寫，單一執行檔、無外部相依、跨平台（Windows / macOS / Linux），並可透過 REST API 與 GraphQL API 與任意 GitLab 實例（SaaS 或 Self-Managed）互動。

## 4.2 glab 架構

```mermaid
flowchart LR
    User[👨‍💻 開發者 / CI Job / AI Agent]
    CLI[glab CLI]
    Cfg[(~/.config/glab-cli/config.yml\n多 Instance 設定與 Token)]
    REST[GitLab REST API]
    GQL[GitLab GraphQL API]
    Git[本機 Git Repository]

    User --> CLI
    CLI --> Cfg
    CLI -- 大部分指令 --> REST
    CLI -- glab api graphql --> GQL
    CLI -- glab mr checkout 等 --> Git
    REST --> GitLabServer[GitLab Server\nSaaS / Self-Managed]
    GQL --> GitLabServer
```

## 4.3 glab 主要功能分類

| 分類 | 涵蓋指令 | 用途 |
|---|---|---|
| 認證管理 | `glab auth` | 登入、登出、檢查狀態、管理多個 GitLab Instance |
| 專案/Repo | `glab repo` | clone、建立、檢視、設定保護分支 |
| Merge Request | `glab mr` | 建立、檢視、核准、合併、checkout MR 分支 |
| Issue | `glab issue` | 建立、檢視、關閉、指派 |
| CI/CD | `glab pipeline` / `glab ci` | 觸發、檢視、重跑 Pipeline，查看 Job Log |
| Release | `glab release` | 建立版本、上傳附件、產生 Release Note |
| 變數管理 | `glab variable` | 管理 CI/CD Variables |
| 通用 API | `glab api` | 直接呼叫任意 REST / GraphQL endpoint |
| AI | `glab duo` | 呼叫 GitLab Duo（Code Suggestions、Chat、Vulnerability Explain） |
| MCP | `glab mcp` | 啟動 GitLab MCP Server，供 Claude Code / Copilot 等 AI Agent 連接 |
| Stack | `glab stack` | 管理「Stacked Diff」（多個相依、分層提交的 MR） |
| 搜尋 | `glab search` | 跨專案搜尋程式碼、Issue、MR |
| 排程 | `glab schedule` | 管理 Pipeline Schedule（定期排程） |
| Runner | `glab runner` | 管理與註冊 Runner |
| 知識圖譜 | `glab orbit` | 存取 GitLab Orbit（Knowledge Graph），提供跨專案程式碼關聯與語意檢索能力 |
| Agent 技能 | `glab skills` | 安裝、列出、更新供 AI Agent 使用的官方技能包（Agent Skills） |
| 軟體供應鏈驗證 | `glab attestation` | 驗證建置產物的 SLSA Provenance 簽署，確認 Artifact 來源可信 |
| Kubernetes 整合 | `glab cluster` | 管理 GitLab Agent for Kubernetes 的叢集連線與拓樸關係 |
| 容器倉庫管理 | `glab container-registry`（別名 `glab cr`） | 列出、檢視、刪除 Container Registry 內的 repository 與 tag |
| 事件管理 | `glab incident` | 建立、檢視、關閉、訂閱/取消訂閱 Incident |
| 統一規劃項目 | `glab work-items` | 管理新一代「Work Item」（整合 Issue/Epic/Task 的統一規劃模型） |
| Runner 路由控制 | `glab runner-controller` | 管理 Runner Fleet 的 Job Router 與 Token 輪替（僅限管理員） |
| 其他工具型指令 | `glab todo` / `iteration` / `snippet` / `securefile` / `opentofu`（別名 `terraform`/`tf`） / `changelog` / `config` / `user` / `completion` / `whatsnew` | 涵蓋待辦事項、Iteration 週期、程式碼片段、CI/CD 安全檔案、OpenTofu/Terraform 狀態管理、變更紀錄產生、CLI 個人設定、使用者資訊查詢、Shell 自動完成安裝、版本更新說明 |

> 💡 **指令分類補充說明**：上表已涵蓋官方 `glab` 目前對外公開的全部子指令分類（共 40 餘個子指令）。其中標示為「其他工具型指令」的項目使用頻率較低，建議團隊依需求查閱 `glab <command> --help` 取得即時、版本對應的參數說明，而不要死記特定參數組合，因為這些工具型指令的旗標（flag）在小版號之間變動較頻繁。

## 4.3.1 glab 指令穩定度分級（Stable / Beta / Experimental）

`glab` 並非每個子指令都已達到正式（Stable）等級，企業導入前應依下表評估風險，避免將 Experimental 指令直接放入正式環境的自動化腳本或 CI/CD Pipeline 中：

| 穩定度 | 子指令範例 | 企業導入建議 |
|---|---|---|
| **Stable**（正式） | `auth`、`repo`、`mr`、`issue`、`pipeline` / `ci`、`release`、`variable`、`api`、`search`、`schedule`、`runner` | 可直接用於生產環境腳本與 CI/CD 自動化 |
| **Beta**（測試版，行為已大致穩定但仍可能微調） | `duo`（部分子指令）、`orbit` | 可在非關鍵流程中試用，正式導入前建議先以非破壞性（唯讀）操作驗證 |
| **Experimental**（實驗性，指令格式與行為可能異動或移除） | `mcp`、`stack`、`skills`、`runner-controller`、`work-items` | 僅建議在 PoC、個人開發環境或內部創新專案中使用，**不應**寫入正式 CI/CD Pipeline 或團隊強制流程，每次升級 `glab` 版本後務必重新驗證指令是否仍相容 |

> ⚠️ **注意事項**：官方文件會在每個指令頁面明確標註目前狀態（Stable/Beta/Experimental），且狀態會隨版本演進改變（例如 Orbit 已由 Experimental 調整為 Beta）。團隊應將「檢查指令狀態」納入 `glab` 版本升級的標準作業程序，而不是只看一次文件就假設狀態永久不變。

## 4.4 安裝 glab

### Windows

```powershell
# 方式一：使用 winget（建議）
winget install GitLab.GLab

# 方式二：使用 Scoop
scoop install glab

# 方式三：使用 Chocolatey
choco install glab
```

### macOS

```bash
# 使用 Homebrew（建議）
brew install glab

# 使用 MacPorts
sudo port install glab
```

### Linux

```bash
# Debian / Ubuntu（官方 .deb）
curl -s https://gitlab.com/gitlab-org/cli/-/releases/permalink/latest/downloads/glab_amd64.deb -o /tmp/glab.deb
sudo dpkg -i /tmp/glab.deb

# RHEL / Rocky（官方 .rpm）
curl -s https://gitlab.com/gitlab-org/cli/-/releases/permalink/latest/downloads/glab_amd64.rpm -o /tmp/glab.rpm
sudo rpm -i /tmp/glab.rpm

# 使用 Homebrew on Linux
brew install glab

# 使用 Go install（任意平台，需先安裝 Go）
go install gitlab.com/gitlab-org/cli/cmd/glab@latest
```

### 驗證安裝

```bash
glab version

# 預期輸出範例（glab 1.9x 系列，版本號會隨小版號持續演進，請以實際安裝結果為準）：
# glab version 1.95.0 (2026-06-09)
# https://gitlab.com/gitlab-org/cli/-/releases/v1.95.0
```

## 4.5 登入與認證

### 互動式登入

```bash
glab auth login
```

執行後會詢問：

1. GitLab instance（預設 `gitlab.com`，企業用戶輸入自架網址，如 `gitlab.example.com`）
2. 認證方式：
   - **Token 驗證**：貼上 Personal Access Token（PAT），需具備 `api`、`read_repository`、`write_repository` 權限範圍。
   - **OAuth 驗證**（瀏覽器登入）：開啟瀏覽器走 OAuth Device Flow，免手動產生 Token，適合個人電腦互動使用。
3. Git 通訊協定（HTTPS 或 SSH）。

```bash
# 非互動式登入（適合 CI/CD 或 Script，使用 Token）
glab auth login --hostname gitlab.example.com --token glpat-xxxxxxxxxxxxxxxxxxxx

# 或透過環境變數
export GITLAB_TOKEN=glpat-xxxxxxxxxxxxxxxxxxxx
glab auth login --hostname gitlab.example.com --stdin <<< "$GITLAB_TOKEN"
```

### 檢查登入狀態

```bash
glab auth status

# 預期輸出：
# gitlab.com
#   ✓ Logged in to gitlab.com as eric.cheng (~/.config/glab-cli/config.yml)
#   ✓ Git operations for gitlab.com configured to use https protocol.
#   ✓ Token: glpat-************************
```

### 多 GitLab Instance 管理

許多企業同時使用 `gitlab.com`（開源專案/外部協作）與自架的 `gitlab.internal.example.com`（內部專案），`glab` 原生支援多 Instance 並存：

```bash
# 登入第二個 instance
glab auth login --hostname gitlab.internal.example.com

# 列出所有已登入的 instance
glab auth status --hostname gitlab.com
glab auth status --hostname gitlab.internal.example.com

# 切換預設 instance（影響未指定 --hostname / GITLAB_HOST 時的行為）
export GITLAB_HOST=gitlab.internal.example.com

# 任意指令都可用 --hostname / GITLAB_HOST 臨時指定目標 instance
glab mr list --hostname gitlab.internal.example.com
```

設定檔位置：`~/.config/glab-cli/config.yml`（Windows 為 `%APPDATA%\glab-cli\config.yml`），內含各 Instance 的 Token、預設協定與偏好設定，**此檔案包含敏感 Token，應視為機密，不可提交進版本控制**。

> ⚠️ **注意事項**：CI/CD Job 中使用 `glab` 時，建議使用 GitLab 自動注入的 `CI_JOB_TOKEN` 或專案層級的 Access Token（透過 Masked Variable 注入），**絕不要將個人 PAT 硬編碼進 `.gitlab-ci.yml`**。

### ✅ 第四章 Checklist

- [ ] 已在開發機與 CI/CD 執行環境安裝 `glab` 並驗證版本
- [ ] 已用 Token 或 OAuth 完成登入，並用 `glab auth status` 確認
- [ ] 若使用多個 GitLab Instance，已分別登入並理解 `--hostname` / `GITLAB_HOST` 的切換方式
- [ ] CI/CD 中使用的 Token 已透過 Masked/Protected Variable 注入，未硬編碼於程式碼

---

# 第五章 GitLab CLI 指令大全

> 每個指令分類皆說明：用途、常用參數、實際範例、最佳實務。所有範例皆可直接複製貼上至終端機執行（請依實際專案/MR/Issue 編號調整）。

## 5.1 `glab auth` — 認證管理

**用途**：登入、登出、檢查認證狀態、管理 Token。

**常用參數**：

| 參數 | 說明 |
|---|---|
| `--hostname` | 指定 GitLab Instance |
| `--token` | 直接帶入 Token（非互動） |
| `--stdin` | 從標準輸入讀取 Token |
| `--web` | 強制使用瀏覽器 OAuth 流程 |

**實例**：

```bash
glab auth login --hostname gitlab.com --web
glab auth status
glab auth logout --hostname gitlab.com
```

**最佳實務**：CI/CD 中一律使用 `--stdin` 搭配 Masked Variable 注入 Token，不要使用 `--web`（CI 環境無瀏覽器）。

## 5.2 `glab repo` — 專案管理

**用途**：clone、建立、檢視、設定專案。

**常用參數**：

| 子指令 | 說明 |
|---|---|
| `glab repo clone <project>` | Clone 專案（自動處理 SSH/HTTPS） |
| `glab repo create` | 建立新專案 |
| `glab repo view` | 在終端機檢視專案資訊，或用 `--web` 開啟瀏覽器 |
| `glab repo archive` | 下載專案壓縮檔 |

**實例**：

```bash
# Clone 專案
glab repo clone mygroup/myproject

# 建立新私有專案並設定描述
glab repo create myteam/new-service --private --description "訂單服務 API"

# 在瀏覽器開啟目前專案首頁
glab repo view --web

# 查看專案基本資訊（在終端機）
glab repo view mygroup/myproject
```

**最佳實務**：建立專案時搭配 `--group` 與既定的 Namespace 命名規範（見第二十一章），避免散落在個人 Namespace 下難以治理。

## 5.3 `glab mr` — Merge Request

**用途**：建立、檢視、核准、合併、checkout Merge Request。

**常用參數**：

| 子指令 | 說明 |
|---|---|
| `glab mr create` | 建立 MR |
| `glab mr list` | 列出 MR（可加 `--assignee`, `--reviewer`, `--label` 篩選） |
| `glab mr view <id>` | 檢視 MR 細節 |
| `glab mr checkout <id>` | 將本機切換到該 MR 的分支 |
| `glab mr approve <id>` | 核准 MR |
| `glab mr merge <id>` | 合併 MR |
| `glab mr diff <id>` | 檢視 MR 的程式碼差異 |
| `glab mr note <id>` | 在 MR 留言 |

**實例**：

```bash
# 建立 MR，自動帶入目前分支與標題，並指定 reviewer 與 label
glab mr create \
  --title "feat: 新增訂單退款 API" \
  --description "實作退款流程，含單元測試與整合測試" \
  --target-branch main \
  --reviewer alice,bob \
  --label "feature,backend" \
  --remove-source-branch

# 列出指派給自己且尚待審核的 MR
glab mr list --assignee=@me --reviewer-state=review_requested

# Checkout 別人的 MR 到本機測試
glab mr checkout 482

# 核准並合併（核准後自動合併，套用 Squash）
glab mr approve 482
glab mr merge 482 --squash --remove-source-branch

# 在 CI Pipeline 失敗時，用 glab 在 MR 留言通知
glab mr note 482 --message "⚠️ Pipeline 失敗，請查看 #${CI_PIPELINE_ID}"
```

**最佳實務**：
- 在 CI/CD Pipeline 中可用 `glab mr create --fill` 搭配 `git push` 自動依 commit message 產生 MR 標題與描述，減少人工撰寫。
- 搭配 `--draft` 建立草稿 MR，待 Pipeline 全綠且自我審查完成才轉為正式 Ready。

## 5.4 `glab issue` — Issue 管理

**用途**：建立、檢視、關閉、指派 Issue。

**實例**：

```bash
# 建立 Issue 並指定 Milestone、標籤
glab issue create \
  --title "登入頁面在 Safari 出現版面錯位" \
  --description "重現步驟：... \n預期結果：... \n實際結果：..." \
  --label "bug,frontend" \
  --milestone "2026-Q3" \
  --assignee carol

# 列出目前 Sprint 所有未關閉的 bug
glab issue list --label bug --state opened

# 在 Issue 留言並關閉
glab issue note 215 --message "已於 MR !482 修復"
glab issue close 215
```

**最佳實務**：搭配 commit message 中的 `Closes #215` 語法，當對應 MR 合併後 Issue 會自動關閉，減少手動操作與遺漏。

## 5.5 `glab pipeline` 與 `glab ci` — CI/CD 操作

**用途**：觸發、檢視、重跑 Pipeline，即時追蹤 Job 輸出。

**實例**：

```bash
# 列出最近的 Pipeline
glab pipeline list

# 檢視特定 Pipeline 細節（含每個 Job 狀態）
glab pipeline view 99231

# 針對目前分支手動觸發 Pipeline（搭配 CI/CD Variable）
glab pipeline run --branch develop --variables "DEPLOY_ENV:staging"

# 重跑失敗的 Job
glab pipeline retry 99231

# 即時追蹤目前分支最新 Pipeline 的執行狀態（互動式 TUI）
glab pipeline ci view

# 直接在終端機跟著看某個 Job 的 Log（類似 tail -f）
glab pipeline ci trace build-job
```

**最佳實務**：本機開發階段可用 `glab pipeline ci view` 取代「不斷重新整理瀏覽器看 Pipeline 進度」，大幅減少 context switch。

## 5.6 `glab release` — 版本發布

**實例**：

```bash
# 建立 Release，自動帶入 Tag 與上傳建置產物
glab release create v2.3.0 \
  --name "v2.3.0 - 訂單模組重構" \
  --notes "## 新功能\n- 退款 API\n## 修復\n- 修正並發扣庫存問題" \
  ./build/order-service-2.3.0.jar

# 用 GitLab Duo 自動產生 Release Note 草稿（見第十三章）後再微調發布
glab release create v2.3.0 --notes-file ./CHANGELOG-2.3.0.md

# 列出歷史版本
glab release list
```

**最佳實務**：搭配第七章 CI/CD 範本，在 `tag` pipeline 中自動執行 `glab release create`，確保每次發版的 Release Note 與實際合併的 MR 清單一致，避免人工漏寫。

## 5.7 `glab variable` — CI/CD 變數管理

**實例**：

```bash
# 新增 Project 層級變數（標記為 Masked + Protected）
glab variable set DEPLOY_TOKEN "xxxxxxxx" --masked --protected

# 新增 Group 層級變數，讓子專案共用
glab variable set DOCKER_REGISTRY_URL "registry.example.com" --group mygroup

# 列出目前專案所有變數（值會被遮蔽顯示）
glab variable list

# 刪除變數
glab variable delete DEPLOY_TOKEN
```

**最佳實務**：機密一律加 `--masked`，僅供 Protected Branch/Tag 使用的變數加 `--protected`，避免 Feature Branch 也能讀到生產環境機密。

## 5.8 `glab project` — 專案層級設定

**實例**：

```bash
# 查看專案層級設定（成員、Visibility、保護分支等）
glab api projects/:id --method GET

# 透過 glab project 子指令管理成員（視版本可能整合於 glab repo / glab api）
glab repo view --web   # 開啟瀏覽器至專案設定頁進行細部調整
```

> 💡 部分細部專案設定（如 Approval Rules、Protected Environments）目前仍須透過 Web UI 或 `glab api` 呼叫對應 REST endpoint 完成，CLI 子指令尚未完整覆蓋所有設定項。

## 5.9 `glab api` — 通用 API 呼叫

**用途**：當 `glab` 尚未提供對應子指令時，直接呼叫任意 REST 或 GraphQL endpoint，是最具彈性的「萬能指令」。

**實例**：

```bash
# REST：取得專案的 Approval Rules
glab api projects/:id/approval_rules

# REST：建立 Protected Branch 規則
glab api projects/:id/protected_branches \
  --method POST \
  --field name="release/*" \
  --field push_access_level=40 \
  --field merge_access_level=30

# GraphQL：查詢專案的漏洞統計
glab api graphql -f query='
query {
  project(fullPath: "mygroup/myproject") {
    vulnerabilities {
      count
    }
  }
}'

# 分頁取得所有開放的 MR（自動處理 Pagination）
glab api projects/:id/merge_requests --paginate --field state=opened
```

**最佳實務**：將常用的 `glab api` 查詢封裝成 Shell function 或小型 Script，存放在團隊共用的工具 repo，避免每次都要重新查 API 文件拼 endpoint。

## 5.10 `glab duo` — GitLab Duo AI 功能

```bash
# 在終端機向 Duo Chat 提問（不需離開終端機查文件）
glab duo ask "如何在 .gitlab-ci.yml 設定 Job 之間的相依關係？"

# 對指定檔案進行程式碼建議/重構提示
glab duo ask "幫我檢查這段程式碼是否有安全性問題" --file src/main/java/OrderService.java
```

詳細功能與最佳實務請見第十三章。

## 5.11 `glab mcp` — 啟動 MCP Server

```bash
# 啟動 GitLab MCP Server（serve 子指令），供 Claude Code 等 AI Agent 連接
glab mcp serve

# 指定僅開放唯讀工具（降低 AI Agent 誤操作風險）
glab mcp serve --read-only
```

詳細整合方式（含目前建議的 HTTP transport 與穩定度狀態）請見第十六章。

## 5.12 `glab stack` — Stacked Diff 管理

**用途**：管理「一連串互相依賴、依序疊加」的多個小型 MR（Stacked MR），讓大型功能可拆成多個易審查的小 MR，又能正確維護彼此的相依關係。

```bash
# 建立第一層 stack
glab stack create add-order-refund-base

# 在目前 stack 上新增下一層
glab stack create add-order-refund-api --parent add-order-refund-base

# 檢視目前 stack 結構
glab stack list

# 將整個 stack 同步（rebase）到最新 main
glab stack sync
```

**最佳實務**：大型重構（如第十八章的 Framework 升級專案）非常適合用 Stacked MR 拆解，避免單一 MR 動輒上千行造成審查品質下降。

## 5.13 `glab search` — 跨專案搜尋

```bash
# 搜尋程式碼
glab search code "OrderRefundService" --group mygroup

# 搜尋 Issue
glab search issues "退款失敗" --state opened

# 搜尋 MR
glab search mrs "資料庫遷移" --group mygroup
```

## 5.14 `glab schedule` — Pipeline 排程管理

```bash
# 建立每天凌晨 2 點執行的排程 Pipeline（執行 nightly 測試）
glab schedule create \
  --description "Nightly Regression Test" \
  --ref main \
  --cron "0 2 * * *" \
  --variables "TEST_SUITE:regression"

# 列出所有排程
glab schedule list

# 手動立即執行某個排程（不等到下次 cron 時間）
glab schedule run 12
```

## 5.15 `glab runner` — Runner 管理

```bash
# 列出專案可用的 Runner
glab runner list

# 註冊新的 Project Runner（建議使用新版 Runner Authentication Token 流程）
glab runner register --url https://gitlab.example.com --token glrt-xxxxxxxx

# 暫停/恢復 Runner
glab runner pause 88
glab runner resume 88
```

詳細安裝與維運請見第八章。

## 5.16 `glab orbit` — Knowledge Graph 查詢

**用途**：查詢 GitLab Orbit（Knowledge Graph）所建立的跨專案程式碼關聯圖，協助開發者與 AI Agent 快速理解「這個函式被誰呼叫」「這個服務依賴哪些上游 API」等語意層級問題，而不必逐一翻找原始碼。

```bash
# 在本機建立/更新目前專案的本地知識圖譜索引
glab orbit local setup

# 查詢遠端（GitLab 伺服器端）知識圖譜中與指定符號相關的關聯
glab orbit remote --query "OrderRefundService 的所有呼叫端"
```

> ⚠️ **注意事項**：`glab orbit` 目前為 Beta 狀態，索引建立需要額外運算資源，且僅在啟用 Orbit 功能旗標的 GitLab 實例上可用，導入前請先與 Platform 團隊確認伺服器端是否已開啟。詳細概念請見第十六章 16.5。

## 5.17 `glab skills` — Agent 技能管理

**用途**：安裝、列出、更新官方或團隊自訂的「Agent Skills」（供 Claude Code、GitLab Duo Agent Platform 等 AI Agent 載入的標準化工作流程包），避免每個工程師各自用不同的 Prompt 重新發明同一套操作。

```bash
# 列出目前可用的 Agent Skills
glab skills list

# 安裝官方提供的「MR 自動建立」技能包
glab skills install gitlab/mr-create-flow

# 更新已安裝的技能包到最新版本
glab skills update
```

**最佳實務**：將團隊常用的技能包清單記錄在專案的 `CLAUDE.md`（見第十四章）中，確保新成員與 CI 環境安裝的是同一套版本，避免「同一個 Prompt 在不同人電腦上行為不一致」。

## 5.18 `glab attestation` — 軟體供應鏈驗證

**用途**：驗證建置產物（容器映像、套件）是否帶有合法的 SLSA Provenance 簽署，確認產物確實來自可信的 CI/CD Pipeline，而非被竄改或從未知來源注入。

```bash
# 驗證指定容器映像的 SLSA Provenance（需先安裝 cosign）
glab attestation verify registry.example.com/order-service:1.4.0 --signing-key cosign.pub
```

> 💡 **企業導入建議**：在「部署到生產環境」前的 Pipeline Stage 中加入 `glab attestation verify`，作為軟體供應鏈安全（Supply Chain Security）的最後一道關卡，搭配第十一章的 Container Scanning 共同把關。此功能目前僅在 GitLab.com 上驗證為可用，Self-Managed 環境需額外確認簽署基礎設施（如內部 Sigstore/Fulcio）是否已部署。

## 5.19 `glab cluster` — Kubernetes Agent 管理

**用途**：管理已註冊的 GitLab Agent for Kubernetes 連線，檢視叢集拓樸，是第十六章 MCP/Orbit 等 AI Agent 取得 Kubernetes 環境上下文的基礎。

```bash
# 列出專案已註冊的 Kubernetes Agent
glab cluster agent list

# 檢視某個 Agent 對應的叢集拓樸圖
glab cluster graph my-k8s-agent
```

## 5.20 `glab container-registry` — 容器倉庫管理

**用途**：在終端機直接管理 Container Registry 內容，取代部分需要登入網頁才能完成的操作。

```bash
# 列出專案下所有 repository
glab container-registry repository list

# 列出某個 repository 下的所有 tag，並刪除過期測試版 tag
glab container-registry tag list order-service
glab container-registry tag delete order-service --tag-name "pr-1234-test"
```

詳細的 Registry 治理策略（Cleanup Policy、Image Promotion）請見第九章。

## 5.21 `glab incident` — 事件管理

**用途**：在終端機處理 Incident（事件），適合值班工程師在處理告警時，不需切換到瀏覽器即可記錄處理過程。

```bash
# 列出目前未關閉的 Incident
glab incident list --state opened

# 在 Incident 留言記錄處理進度，並標記已關閉
glab incident note 58 --message "已確認為 Redis 連線池耗盡，已擴容處理"
glab incident close 58
```

## 5.22 `glab work-items` — 統一規劃項目

**用途**：管理「Work Item」——GitLab 將 Issue、Epic、Task 等規劃物件逐步統一後的新資料模型，未來可能取代部分傳統 `glab issue` 的使用情境。

```bash
# 列出目前專案的 Work Item
glab work-items list

# 建立一個新的 Work Item 並指定類型
glab work-items create --title "重構訂單退款流程" --type Task
```

> ⚠️ **注意事項**：`glab work-items` 與底層的 Work Item 資料模型目前仍為 Experimental，部分團隊既有的 Issue/Epic 流程尚未完全遷移到此模型，導入前建議先以小範圍團隊試行，確認與既有 `glab issue` 工作流程不會產生資料不一致。

## 5.23 其他工具型指令速查

以下指令使用頻率較低，多屬個人開發環境設定或周邊工具整合，建議查閱即時的 `glab <command> --help` 取得對應版本的參數細節：

| 指令 | 用途 |
|---|---|
| `glab todo` | 管理個人待辦清單（標記已完成、列出未處理項目） |
| `glab iteration` | 查詢 Iteration（類似 Sprint）資訊 |
| `glab snippet` | 建立、檢視、管理 Code Snippet |
| `glab securefile` | 管理 CI/CD 用的 Secure File（如憑證、簽署金鑰） |
| `glab opentofu`（別名 `terraform` / `tf`） | 管理 OpenTofu / Terraform State 後端 |
| `glab changelog` | 依 Commit/MR 紀錄自動產生 Changelog |
| `glab config` | 讀取/設定 `glab` 本機設定值 |
| `glab user` | 查詢使用者帳號與活動事件 |
| `glab completion` | 安裝 Shell 自動完成腳本（Bash/Zsh/Fish/PowerShell） |
| `glab whatsnew` | 顯示目前安裝版本的更新說明 |

### ✅ 第五章 Checklist

- [ ] 團隊已建立常用 `glab` 指令的內部速查表（可參考第二十三章附錄）
- [ ] CI/CD Pipeline 中已善用 `glab mr` / `glab release` 自動化日常流程（建立 MR、發版）
- [ ] 機密一律透過 `glab variable set --masked --protected` 管理，未硬編碼於程式或 YAML
- [ ] 對於 CLI 尚未支援的設定，已掌握用 `glab api` 直接呼叫 REST/GraphQL 的能力
- [ ] 已依 4.3.1 的穩定度分級，確認團隊使用的 Experimental 指令（如 `mcp`、`stack`、`skills`、`work-items`）僅限於非關鍵流程，並排定隨版本升級重新驗證的排程

---

# 第六章 GitLab Flow

## 6.1 三種主流分支策略比較

| 比較項目 | Git Flow | GitHub Flow | GitLab Flow |
|---|---|---|---|
| 分支複雜度 | 高（master/develop/feature/release/hotfix） | 低（main + feature branch） | 中（main + 環境分支或 Release 分支，依需求選用） |
| 適合場景 | 有明確版本發布週期的傳統軟體（如桌面應用） | 持續部署的 Web 服務 | 兼顧持續部署與多環境/多版本維護的企業專案 |
| 上線方式 | 透過 release 分支與版本標籤 | main 分支永遠可部署，merge 後立即上線 | 依「環境分支」或「Release 分支」決定上線時機，彈性高 |
| 與 CI/CD 契合度 | 較低（流程繁瑣） | 高（簡單、適合自動化） | 高（GitLab CI/CD 原生支援 `rules`/`environment` 對應分支策略） |

```mermaid
gitGraph
    commit id: "init"
    branch develop
    checkout develop
    commit id: "feature-a"
    branch feature/order-refund
    checkout feature/order-refund
    commit id: "wip-1"
    commit id: "wip-2"
    checkout develop
    merge feature/order-refund
    branch release/2.3.0
    checkout release/2.3.0
    commit id: "rc-fix"
    checkout main
    merge release/2.3.0 tag: "v2.3.0"
    checkout develop
    merge main
```

> 上圖示意 Git Flow 的分支結構；GitHub Flow 則僅有 `main` + 短期 `feature/*` 分支，合併後立即部署；GitLab Flow 在兩者之間，依專案需求採用「Environment Branch」（如 `staging`、`production`）或「Release Branch」（如 `release/2.3.0`）。

## 6.2 GitLab Flow 的兩種變體

### 6.2.1 Environment Branch 模式

適合需要明確區分多環境部署狀態的專案：

```mermaid
flowchart LR
    Feature[feature/*] -->|MR| Main[main]
    Main -->|自動部署| Staging[staging 分支\n對應 Staging 環境]
    Staging -->|手動核准 Promote| Production[production 分支\n對應 Production 環境]
```

- `main`：永遠是最新、通過所有測試的程式碼。
- `staging`：合併到 `main` 後自動（或半自動）同步，部署到 Staging 環境驗收。
- `production`：驗收通過後才合併，觸發正式環境部署。

### 6.2.2 Release Branch 模式

適合需要同時維護多個正式發行版本（如企業軟體需支援舊版 Patch）的專案：

- 每次發版從 `main` 切出 `release/x.y.0` 分支。
- Hotfix 直接在 `release/x.y.0` 上修復，並 cherry-pick 回 `main`。
- 適合搭配第二十三章附錄的版本維護策略。

## 6.3 企業建議

> 💡 **企業導入建議**：
> - **新創 / 持續部署的 SaaS 產品**：建議採用 GitHub Flow 或 GitLab Flow 的 Environment Branch 模式，簡化流程、加快交付速度。
> - **需同時維護多個正式發行版本（如賣斷制軟體、Library/SDK）**：建議採用 GitLab Flow 的 Release Branch 模式，方便針對舊版本獨立 Hotfix。
> - **避免直接套用傳統 Git Flow**：develop 分支與 main 分支長期並存容易產生「分支漂移」（兩邊程式碼長期不同步），在高頻率部署的現代 CI/CD 環境下維護成本過高，建議僅在維護週期長、發版頻率低（如每季一次）的傳統專案中保留使用。

> ⚠️ **實戰案例**：某保險業核心系統團隊原採用 Git Flow，develop 與 release 分支長期分歧，每次發版前都要花 2-3 天處理合併衝突。改採 GitLab Flow（Release Branch 模式）並搭配第七章的 `rules` 設定後，發版前置作業降至半天內，且 Hotfix 可直接從對應 release 分支發布，不需等待下個大版本。

### ✅ 第六章 Checklist

- [ ] 已依專案性質（持續部署 vs 多版本維護）選定適合的分支策略
- [ ] 團隊已建立分支命名規範（如 `feature/*`、`release/*`、`hotfix/*`）
- [ ] 已確認 CI/CD `rules` 設定與所選分支策略一致（見第七章）
- [ ] 已建立 Hotfix 流程文件，明確規定如何 cherry-pick 回主線

---

# 第七章 CI/CD

## 7.1 `.gitlab-ci.yml` 核心概念

GitLab CI/CD 的設定全部集中於專案根目錄的 `.gitlab-ci.yml`（或透過 `include` 拆分至多個檔案）。核心概念：

```mermaid
flowchart TB
    YML[".gitlab-ci.yml"]
    YML --> Stages["stages: 定義執行順序\n(build → test → security → package → deploy)"]
    YML --> Jobs["jobs: 實際執行的任務\n每個 job 屬於某個 stage"]
    Jobs --> Rules["rules: 決定 job 是否觸發\n(依分支/Tag/變數/MR 條件)"]
    Jobs --> Artifacts["artifacts: 保留 job 產出物\n(供下游 stage 或人工下載)"]
    Jobs --> Cache["cache: 加速重複建置\n(如 node_modules / .m2)"]
    Jobs --> Variables["variables: 環境變數"]
    Jobs --> Environment["environment: 對應部署環境\n(staging/production)"]
    Workflow["workflow: 控制整個 Pipeline\n是否該被建立"] --> YML
```

### 基礎結構範例

```yaml
stages:
  - build
  - test
  - security
  - package
  - deploy

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=.m2/repository"

workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_COMMIT_TAG'

default:
  tags:
    - docker
  retry:
    max: 1
    when: runner_system_failure
```

### Stages / Jobs / Rules

```yaml
unit-test:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn test
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
  artifacts:
    when: always
    reports:
      junit: target/surefire-reports/TEST-*.xml
```

### Artifacts 與 Cache

```yaml
build-jar:
  stage: build
  image: maven:3.9-eclipse-temurin-21
  cache:
    key:
      files:
        - pom.xml
    paths:
      - .m2/repository
  script:
    - mvn -B package -DskipTests
  artifacts:
    paths:
      - target/*.jar
    expire_in: 7 days
```

> ⚠️ **Cache 與 Artifacts 差異**：`cache` 是「加速下次建置」用，內容可能過期、不保證存在；`artifacts` 是「本次 Pipeline 產出物」，會在 stage 之間傳遞並可被下載，兩者用途不同不可混用。

### Rules 進階條件

```yaml
deploy-staging:
  stage: deploy
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: on_success
    - if: '$CI_PIPELINE_SOURCE == "schedule"'
      when: never
  environment:
    name: staging
    url: https://staging.example.com
```

### Environment 與 Deployment

```yaml
deploy-production:
  stage: deploy
  script:
    - helm upgrade --install order-service ./charts/order-service -f values-prod.yaml
  environment:
    name: production
    url: https://app.example.com
    deployment_tier: production
  rules:
    - if: '$CI_COMMIT_TAG'
  when: manual
```

> 💡 **最佳實務**：正式環境部署一律搭配 `when: manual` + Protected Environment（見第十一章權限設定），確保只有被授權人員可觸發點擊「部署」按鈕，並留下稽核紀錄（誰、何時點的）。

## 7.2 Java / Spring Boot 完整 CI/CD 範例

```yaml
stages:
  - build
  - test
  - sast
  - package
  - deploy

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"
  IMAGE_TAG: "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"

build:
  stage: build
  image: maven:3.9-eclipse-temurin-21
  cache:
    key: maven-$CI_COMMIT_REF_SLUG
    paths:
      - .m2/repository
  script:
    - mvn -B compile
  artifacts:
    paths:
      - target/classes

unit-test:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  cache:
    key: maven-$CI_COMMIT_REF_SLUG
    paths:
      - .m2/repository
  script:
    - mvn -B test
  artifacts:
    when: always
    reports:
      junit: target/surefire-reports/TEST-*.xml
    paths:
      - target/site/jacoco

include:
  - template: Security/SAST.gitlab-ci.yml

package-jar:
  stage: package
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn -B package -DskipTests
  artifacts:
    paths:
      - target/*.jar
    expire_in: 30 days

build-image:
  stage: package
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker build -t "$IMAGE_TAG" .
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker push "$IMAGE_TAG"
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

deploy-staging:
  stage: deploy
  image: bitnami/kubectl:1.30
  script:
    - kubectl set image deployment/order-service order-service="$IMAGE_TAG" -n staging
  environment:
    name: staging
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

對應的 Spring Boot 專案 `Dockerfile`（多階段建置）：

```dockerfile
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -B dependency:go-offline
COPY src ./src
RUN mvn -B package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## 7.3 Node.js / Vue 完整 CI/CD 範例

```yaml
stages:
  - install
  - lint
  - test
  - build
  - deploy

default:
  image: node:22-alpine
  cache:
    key:
      files:
        - package-lock.json
    paths:
      - node_modules/

install:
  stage: install
  script:
    - npm ci

lint:
  stage: lint
  script:
    - npm run lint

unit-test:
  stage: test
  script:
    - npm run test:unit -- --coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

build-vue:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 7 days

deploy-pages:
  stage: deploy
  image: alpine:3.20
  script:
    - apk add --no-cache aws-cli
    - aws s3 sync dist/ s3://static-assets-bucket/order-frontend --delete
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

## 7.4 React 完整 CI/CD 範例

```yaml
stages:
  - test
  - build
  - container

default:
  image: node:22-alpine

test:
  stage: test
  script:
    - npm ci
    - npm run test -- --watchAll=false --coverage

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - build/

container:
  stage: container
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" .
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

對應 React `Dockerfile`（Nginx 靜態服務）：

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
```

## 7.5 Python 完整 CI/CD 範例

```yaml
stages:
  - test
  - quality
  - package

default:
  image: python:3.13-slim
  cache:
    paths:
      - .cache/pip

before_script:
  - pip install --cache-dir=.cache/pip -r requirements.txt

unit-test:
  stage: test
  script:
    - pytest --cov=app --junitxml=report.xml
  artifacts:
    reports:
      junit: report.xml

lint:
  stage: quality
  script:
    - pip install ruff
    - ruff check .

build-wheel:
  stage: package
  script:
    - pip install build
    - python -m build
  artifacts:
    paths:
      - dist/*.whl
```

## 7.6 `include` 拆分與共用範本

大型企業通常會將通用的 Pipeline 邏輯抽成共用範本，存放在獨立的 `ci-templates` 專案，各專案透過 `include` 引用，確保安全掃描、部署流程一致且易於統一升級：

```yaml
include:
  - project: 'platform/ci-templates'
    ref: main
    file: '/templates/java-spring-boot.yml'
  - project: 'platform/ci-templates'
    ref: main
    file: '/templates/security-baseline.yml'
  - local: '.gitlab-ci/deploy.yml'
```

> 💡 **企業導入建議**：將安全掃描（SAST/Secret Detection）、品質門檻（Code Coverage 最低標準）、部署核准流程等「治理規則」放進 Platform 團隊維護的共用範本，各應用團隊只需 `include`，既保證合規一致性，又不需要每個團隊重複造輪子。修改範本時透過 Semantic Version 的 `ref`（如 `ref: v3.2.0`）控制升級節奏，避免不預期的 Breaking Change。

### ✅ 第七章 Checklist

- [ ] 已理解 `stages` / `jobs` / `rules` / `artifacts` / `cache` / `environment` 各自用途，未混用 cache 與 artifacts
- [ ] 已依語言/框架選用對應的 CI/CD 範本，並確認 Docker 多階段建置已套用（縮小最終 Image 體積）
- [ ] 正式環境部署已設定 `when: manual` + Protected Environment
- [ ] 已評估是否需要建立共用 `ci-templates` 專案統一治理規則
- [ ] Pipeline 中所有機密皆透過 CI/CD Variables 注入，未寫死於 YAML

---

# 第八章 GitLab Runner

## 8.1 Runner 類型總覽

| 類型 | 範圍 | 適用情境 |
|---|---|---|
| Shared Runner | GitLab Instance 全域共用 | 中小型團隊、輕量工作負載，由 Platform 團隊統一維運 |
| Group Runner | 特定 Group 及其子專案共用 | 部門/產品線層級共用建置資源 |
| Project Runner | 綁定特定專案 | 有特殊硬體需求（如 GPU）或高機密性的專案 |

| Executor | 說明 | 適用情境 |
|---|---|---|
| Kubernetes Runner | 每個 Job 動態建立 K8s Pod 執行 | 雲原生環境、需要彈性自動擴縮的大型團隊首選 |
| Docker Runner | 每個 Job 在獨立 Docker 容器執行 | 一般建置/測試，環境隔離且設定簡單 |
| Shell Runner | 直接在主機 Shell 執行 | 需要存取特殊主機資源（如已授權的內部工具、UI 測試需要顯示卡） |

```mermaid
flowchart TB
    GitLabSrv[GitLab Server]
    subgraph K8sCluster["Kubernetes Cluster"]
        RunnerMgr[GitLab Runner\nKubernetes Executor]
        Pod1[Job Pod 1]
        Pod2[Job Pod 2]
        Pod3[Job Pod N]
    end
    DockerHost[Docker Host\nDocker Executor]
    ShellHost[裸機/VM\nShell Executor]

    GitLabSrv -- 派發 Job --> RunnerMgr
    RunnerMgr --> Pod1
    RunnerMgr --> Pod2
    RunnerMgr --> Pod3
    GitLabSrv -- 派發 Job --> DockerHost
    GitLabSrv -- 派發 Job --> ShellHost
```

## 8.2 安裝 GitLab Runner

### Linux（裸機/VM，Docker Executor）

```bash
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash
sudo apt install gitlab-runner

# 註冊（新版採用 Runner Authentication Token，於 GitLab 後台「CI/CD Settings → Runners」建立）
sudo gitlab-runner register \
  --url https://gitlab.example.com \
  --token glrt-xxxxxxxxxxxxxxxxxxxx \
  --executor docker \
  --docker-image alpine:3.20 \
  --description "shared-docker-runner-01"
```

### Kubernetes（Helm Chart）

```bash
helm repo add gitlab https://charts.gitlab.io
helm repo update

helm upgrade --install gitlab-runner gitlab/gitlab-runner \
  --namespace gitlab-runner --create-namespace \
  --set gitlabUrl=https://gitlab.example.com \
  --set runnerToken=glrt-xxxxxxxxxxxxxxxxxxxx \
  --set runners.executor=kubernetes \
  --set "runners.config=concurrent = 20"
```

### 驗證

```bash
sudo gitlab-runner verify
sudo gitlab-runner status

# 在 GitLab 後台 CI/CD Settings → Runners 確認 Runner 顯示為「綠燈」(Online)
glab api projects/:id/runners
```

## 8.3 設定要點

```toml
# /etc/gitlab-runner/config.toml
concurrent = 20

[[runners]]
  name = "k8s-runner"
  url = "https://gitlab.example.com"
  executor = "kubernetes"
  [runners.kubernetes]
    namespace = "gitlab-runner"
    cpu_request = "500m"
    memory_request = "512Mi"
    cpu_limit = "2"
    memory_limit = "4Gi"
    service_account = "gitlab-runner-sa"
  [runners.cache]
    Type = "s3"
    [runners.cache.s3]
      ServerAddress = "s3.example.com"
      BucketName = "gitlab-runner-cache"
```

> ⚠️ **注意事項**：`concurrent` 是整台 Runner 主機/設定可同時處理的 Job 總數，務必依主機 CPU/Memory 容量設定，並搭配 `[runners.kubernetes]` 的 `cpu_limit`/`memory_limit` 避免單一 Job 吃滿整個節點資源，影響其他 Job。

## 8.4 維護、升級、故障排除

**維護**：

```bash
# 查看目前所有已註冊 Runner 與其忙碌狀態
glab api runners/all

# 暫停 Runner（不接收新 Job，但不影響執行中的 Job）
glab runner pause 88
```

**升級**：

```bash
sudo apt update && sudo apt install gitlab-runner
sudo gitlab-runner restart

# Kubernetes 環境
helm upgrade gitlab-runner gitlab/gitlab-runner -n gitlab-runner --reuse-values
```

**故障排除常見情境**：

| 問題 | 可能原因 | 排查方式 |
|---|---|---|
| Job 卡在 `pending` | 無可用 Runner 或 tags 不匹配 | 檢查 Job 的 `tags` 與 Runner 設定的 tags 是否一致 |
| Job 突然失敗 `runner_system_failure` | Runner 主機資源不足或網路中斷 | 檢查 `gitlab-runner.log`，確認資源使用率 |
| Kubernetes Executor Pod 一直 `Pending` | Namespace 資源配額不足 | `kubectl describe pod` 確認是否卡在 ResourceQuota 或 Image Pull |
| Cache 未生效 | Cache Key 設計不當（每次都不同） | 確認 `cache.key` 是否依檔案 hash（如 `package-lock.json`）而非每次變動的變數 |

> 💡 **實務案例**：某電商團隊大促前發現 Pipeline 排隊嚴重，原因是 Shared Runner 的 `concurrent` 設太低（僅 5），尖峰時段上百個 MR 同時觸發 Pipeline 造成大排長龍。改用 Kubernetes Runner 並開啟 Cluster Autoscaler 後，依負載自動擴增 Job Pod 數量，排隊時間從平均 25 分鐘降至 2 分鐘內。

### ✅ 第八章 Checklist

- [ ] 已依團隊規模選定 Shared/Group/Project Runner 範圍策略
- [ ] 已依工作負載特性選定 Kubernetes/Docker/Shell Executor
- [ ] `concurrent` 與資源限制（cpu/memory request/limit）已依主機容量合理設定
- [ ] 已設定 S3 相容的分散式 Cache，而非僅依賴單機本地快取
- [ ] 已建立 Runner 監控告警（Online/Offline、Job 排隊時間）

---

# 第九章 Container Registry

## 9.1 GitLab Container Registry 概念

GitLab 內建 **Docker/OCI 相容的 Container Registry**，每個專案預設即擁有自己的 Registry 命名空間（`registry.example.com/group/project`），無需額外部署 Harbor 或 Docker Registry。

```mermaid
flowchart LR
    CI[CI/CD Job\ndocker build] -->|docker push| Registry[(GitLab Container Registry)]
    Registry -->|docker pull| K8s[Kubernetes Cluster]
    Registry -->|docker pull| LocalDev[本機開發環境]
    SecurityScan[Container Scanning] -.掃描.-> Registry
```

## 9.2 基本操作

```bash
# 登入 Registry（CI/CD Job 中可用 CI_REGISTRY_USER / CI_REGISTRY_PASSWORD 自動注入）
docker login registry.example.com -u <username> -p <token>

# Build 並標記 Image
docker build -t registry.example.com/mygroup/order-service:1.4.0 .

# Push
docker push registry.example.com/mygroup/order-service:1.4.0

# 透過 glab 查看 Registry 內的 Image 清單
glab api projects/:id/registry/repositories
```

CI/CD 中的標準範例：

```yaml
build-image:
  stage: package
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" -t "$CI_REGISTRY_IMAGE:latest" .
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
    - docker push "$CI_REGISTRY_IMAGE:latest"
```

## 9.3 Image 掃描（Container Scanning）

```yaml
include:
  - template: Security/Container-Scanning.gitlab-ci.yml

container_scanning:
  variables:
    CS_IMAGE: "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

掃描結果會出現在 MR 的 Security Widget，列出 CVE 編號、嚴重程度（Critical/High/Medium/Low）與建議修復版本。

## 9.4 Image Promotion（多環境晉升流程）

企業常見作法是「同一個 Image 從測試晉升到生產，不重新建置」，避免 Build 環境差異造成的不一致：

```yaml
promote-to-production:
  stage: promote
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker pull "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
    - docker tag "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" "$CI_REGISTRY_IMAGE:production-$CI_COMMIT_SHORT_SHA"
    - docker push "$CI_REGISTRY_IMAGE:production-$CI_COMMIT_SHORT_SHA"
  environment:
    name: production
  when: manual
  rules:
    - if: '$CI_COMMIT_TAG'
```

## 9.5 最佳實務

- **使用不可變標籤（Immutable Tag）**：以 Commit SHA 或語意化版本作為 Tag，避免使用 `latest` 部署到生產環境（無法追溯確切版本）。
- **定期清理舊 Image**：設定 Container Registry 的 **Cleanup Policy**（依保留天數/數量自動清除過期 Tag），避免 Object Storage 用量無限增長。
- **最小化 Base Image**：優先使用 `alpine` 或 `distroless` 映像，縮小攻擊面並加速 Pull 速度。
- **Image 簽章驗證**：對高合規需求的企業，建議搭配 Cosign 對 Image 進行簽章，並在部署前驗證簽章。

```yaml
# Cleanup Policy 設定範例（透過 API）
# glab api projects/:id --method PUT --field "container_expiration_policy_attributes[cadence]=1d" \
#   --field "container_expiration_policy_attributes[keep_n]=10" \
#   --field "container_expiration_policy_attributes[older_than]=30d"
```

> ⚠️ **注意事項**：Container Registry 的實際儲存空間計算在 Object Storage 用量內，企業若未設定 Cleanup Policy，常見半年內 Registry 用量暴增到數百 GB，務必在第二十章維運手冊中將 Registry 用量監控納入告警項目。

## 9.6 Container Virtual Registry（聚合上游倉庫）

許多企業同時使用 Docker Hub、Harbor、Quay 等多個外部容器倉庫，工程師在本機或 CI/CD 中常需要分別設定多組登入憑證與 Pull 規則，管理成本高且容易因外部倉庫的 Rate Limit（如 Docker Hub 匿名拉取限制）導致 Pipeline 不穩定。

**Container Virtual Registry** 讓 GitLab Container Registry 扮演「聚合層」的角色：將多個上游倉庫註冊為單一虛擬倉庫的來源，開發者與 CI/CD 只需對接 GitLab 一個 endpoint，即可透明地拉取來自不同上游的 Image，同時所有流量會經過 GitLab 的快取與存取控制：

```bash
# 透過 API 將 Docker Hub 註冊為虛擬倉庫的其中一個上游來源
glab api groups/:id/virtual_registries/packages/container \
  --method POST \
  --field name="shared-upstreams" \
  --field upstream_url="https://registry-1.docker.io"
```

> 💡 **企業導入建議**：將常用的公共基礎映像（如 `nginx`、`postgres`、`eclipse-temurin`）統一透過 Virtual Registry 快取，可同時達到「降低對外流量與 Rate Limit 風險」與「對所有 Image 統一套用第 11 章的 Container Scanning」兩個目的，避免團隊各自從外部來源直接拉取未經掃描的映像。

## 9.7 多架構 Image 支援（Multi-Architecture）

隨著企業逐步導入 ARM 架構的運算資源（如 AWS Graviton、Apple Silicon 開發機），單一映像只支援 x86_64 已不足夠。GitLab Container Registry 支援以 **Manifest List（OCI Image Index）** 的形式，將同一個 Tag 對應到多個 CPU 架構的映像，讓 `docker pull` 時自動依執行環境選擇正確的版本：

```bash
# 使用 buildx 建置並推送同時支援 amd64/arm64 的多架構映像
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag registry.example.com/order-service:1.4.0 \
  --push .

# 在 GitLab UI / glab 中可看到同一個 Tag 下列出對應的多個平台徽章
glab container-registry tag list order-service
```

> ⚠️ **注意事項**：多架構映像會讓單一 Tag 對應的儲存空間倍增（每個架構各占一份），務必搭配 9.5 的 Cleanup Policy 一併規劃保留策略；CI/CD Runner 若僅有 x86_64 執行環境，需另外規劃具備 ARM Executor 的 Runner（見第八章）才能完成多架構建置。

### ✅ 第九章 Checklist

- [ ] 已使用不可變標籤（Commit SHA / SemVer），未在生產部署使用 `latest`
- [ ] 已設定 Container Scanning 並納入 MR 合併門檻（Critical 漏洞需阻擋合併）
- [ ] 已設定 Cleanup Policy 定期清除過期 Image
- [ ] 已評估多環境 Image Promotion 流程，避免重複建置造成環境差異
- [ ] 已評估是否需要透過 Container Virtual Registry 聚合外部上游倉庫，降低 Rate Limit 風險
- [ ] 若有 ARM/多架構運算需求，已規劃多架構映像建置與對應的儲存保留策略

---

# 第十章 Package Registry

## 10.1 支援的套件格式總覽

GitLab Package Registry 原生支援多種套件管理生態系，企業可用單一平台取代 Nexus/Artifactory：

| 格式 | 用途 |
|---|---|
| Maven | Java/Kotlin 函式庫與內部共用模組 |
| Gradle | 同 Maven 生態，常見於 Android/Kotlin 專案 |
| npm | JavaScript/TypeScript 套件 |
| pnpm | 同 npm 生態，支援 monorepo workspace |
| NuGet | .NET 函式庫 |
| PyPI | Python 套件 |
| Generic Package | 任意二進位檔案（如內部工具、韌體、報表檔） |

## 10.2 Maven 設定與發布

`pom.xml`：

```xml
<distributionManagement>
  <repository>
    <id>gitlab-maven</id>
    <url>https://gitlab.example.com/api/v4/projects/${env.CI_PROJECT_ID}/packages/maven</url>
  </repository>
</distributionManagement>
```

`settings.xml`（CI/CD 中可動態產生）：

```xml
<servers>
  <server>
    <id>gitlab-maven</id>
    <configuration>
      <httpHeaders>
        <property>
          <name>Job-Token</name>
          <value>${CI_JOB_TOKEN}</value>
        </property>
      </httpHeaders>
    </configuration>
  </server>
</servers>
```

```bash
mvn deploy -s settings.xml
```

CI/CD 範例：

```yaml
publish-library:
  stage: package
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn deploy -s ci_settings.xml
  rules:
    - if: '$CI_COMMIT_TAG'
```

## 10.3 npm / pnpm 設定與發布

`.npmrc`：

```
@mygroup:registry=https://gitlab.example.com/api/v4/packages/npm/
//gitlab.example.com/api/v4/packages/npm/:_authToken=${CI_JOB_TOKEN}
```

```bash
npm publish
# 或 pnpm publish（語法相同，pnpm 原生相容 npm registry 協定）
```

## 10.4 NuGet 發布

```bash
dotnet nuget add source "https://gitlab.example.com/api/v4/projects/${CI_PROJECT_ID}/packages/nuget/index.json" \
  --name gitlab --username gitlab-ci-token --password "$CI_JOB_TOKEN" --store-password-in-clear-text

dotnet pack -c Release
dotnet nuget push "bin/Release/*.nupkg" --source gitlab
```

## 10.5 PyPI 發布

```bash
pip install twine build
python -m build

TWINE_PASSWORD="${CI_JOB_TOKEN}" TWINE_USERNAME=gitlab-ci-token \
  python -m twine upload --repository-url https://gitlab.example.com/api/v4/projects/${CI_PROJECT_ID}/packages/pypi dist/*
```

安裝時指定內部 Index：

```bash
pip install mypackage --index-url https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.example.com/api/v4/projects/${CI_PROJECT_ID}/packages/pypi/simple
```

## 10.6 Generic Package（任意檔案）

```bash
# 上傳
curl --header "JOB-TOKEN: $CI_JOB_TOKEN" \
  --upload-file ./build/report.pdf \
  "https://gitlab.example.com/api/v4/projects/${CI_PROJECT_ID}/packages/generic/audit-reports/2026-Q2/report.pdf"

# 下載
curl --header "JOB-TOKEN: $CI_JOB_TOKEN" \
  -o report.pdf \
  "https://gitlab.example.com/api/v4/projects/${CI_PROJECT_ID}/packages/generic/audit-reports/2026-Q2/report.pdf"
```

> 💡 **企業導入建議**：將內部共用的 Java/Spring Boot 共用模組（如統一錯誤碼、共用 DTO）發布為 Maven Package，搭配第十八章 Framework 升級專案時，可透過 Package Registry 的版本管理，讓各應用團隊清楚知道哪個版本對應哪個 Spring Boot 主版本，避免升級時相依套件版本混亂。

### ✅ 第十章 Checklist

- [ ] 已評估是否可用 GitLab Package Registry 取代既有的 Nexus/Artifactory，降低維運系統數量
- [ ] CI/CD 發布套件皆使用 `CI_JOB_TOKEN`，未使用個人 PAT
- [ ] 已建立內部共用套件的版本命名與發布規範（SemVer）
- [ ] 已設定 Package Registry 的存取權限，避免外部成員下載內部專屬套件

---

# 第十一章 GitLab Security

## 11.1 GitLab 安全掃描總覽

```mermaid
flowchart TB
    Code[原始碼] --> SAST[SAST\n靜態應用程式安全測試]
    Code --> Secret[Secret Detection\n密鑰/憑證偵測]
    Code --> Dependency[Dependency Scanning\n相依套件已知漏洞]
    Code --> License[License Compliance\n授權合規檢查]
    Image[Container Image] --> ContainerScan[Container Scanning]
    RunningApp[執行中的應用程式] --> DAST[DAST\n動態應用程式安全測試]

    SAST --> Dashboard[Security Dashboard]
    Secret --> Dashboard
    Dependency --> Dashboard
    License --> Dashboard
    ContainerScan --> Dashboard
    DAST --> Dashboard
    Dashboard --> VulnMgmt[Vulnerability Management\n分級/指派/追蹤修復]
```

## 11.2 SAST（靜態應用程式安全測試）

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml
```

GitLab 會依專案使用的語言自動選用對應的分析器（Java 用 Semgrep-based analyzer、Node.js 用對應規則集等），無需手動指定，掃描結果於 MR 中顯示為 Security Widget，標示新增/修復的漏洞。

自訂規則範例（排除誤判路徑）：

```yaml
sast:
  variables:
    SAST_EXCLUDED_PATHS: "spec, test, tests, tmp, generated"
```

## 11.3 DAST（動態應用程式安全測試）

```yaml
include:
  - template: DAST.gitlab-ci.yml

dast:
  variables:
    DAST_WEBSITE: "https://staging.example.com"
    DAST_FULL_SCAN_ENABLED: "true"
  stage: dast
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

> ⚠️ **注意事項**：DAST 是對「已部署運行中」的應用程式進行主動掃描（會實際送出測試攻擊請求），務必只對 Staging/測試環境執行，**絕不可直接對生產環境執行 Full Scan**，避免造成非預期的資料異動或服務負載。

## 11.4 Dependency Scanning

```yaml
include:
  - template: Security/Dependency-Scanning.gitlab-ci.yml
```

掃描 `pom.xml`、`package-lock.json`、`requirements.txt` 等相依清單，比對已知 CVE 資料庫（如 GitLab Advisory Database），於 MR 中標示風險套件與建議升級版本。

目前官方建議的掃描方式已轉為**以 SBOM（Software Bill of Materials，採 CycloneDX 格式）為基礎**：建置階段先產生專案完整的 SBOM 清單，再對 SBOM 進行漏洞比對與後續的持續重新掃描（當 GitLab Advisory Database 有新資料時自動重新比對既有 SBOM，不需重新建置）。

> ⚠️ **棄用提醒**：舊版以 Gemnasium 為核心引擎的掃描方式已於 GitLab 17.9 起標示為棄用（Deprecated），預計在 GitLab 20.0 移除。仍在使用舊版 `Dependency-Scanning.gitlab-ci.yml`（非 SBOM 路徑）的專案，應提前規劃遷移到 SBOM-based 掃描範本，避免版本升級後掃描功能直接失效。

## 11.4.1 AI 輔助安全：Agentic SAST 與 Duo 誤報偵測

GitLab Duo 已將部分安全掃描工作流程進一步自動化，目前屬於 Ultimate 方案限定的能力：

- **Agentic SAST Vulnerability Resolution**：針對 SAST 偵測到的漏洞，由 AI Agent 分析程式碼上下文後，自動產生對應的修補 Merge Request（含程式碼變更與說明），開發者只需審查並決定是否合併，而不必從零開始研究修補方式。
- **GitLab Duo 誤報偵測（False Positive Detection）**：針對 SAST 與 Secret Detection 的掃描結果，AI 會標註該發現「可能為誤判」的信心分數，協助安全團隊優先處理真實風險，減少人工逐一複核所有掃描結果的負擔。

```mermaid
flowchart LR
    Scan[SAST 掃描偵測到漏洞] --> AIAnalyze[Duo AI 分析程式碼上下文]
    AIAnalyze -- 判定為可能誤判 --> FlagFP[標註信心分數\n供人工優先排序]
    AIAnalyze -- 判定為真實漏洞 --> AutoFix[Agentic SAST\n自動產生修補 MR]
    AutoFix --> Review[開發者人工審查 + 合併]
    FlagFP --> Review2[安全團隊人工確認]
```

> ⚠️ **注意事項**：自動產生的修補 MR 與誤報信心分數**皆為輔助判斷，不可取代人工最終決策**。企業導入時應保留「AI 產生的修補 MR 必須經過至少一位資深工程師核准才能合併」的硬性規則，並定期抽查 AI 判定誤報的案例，確認沒有真實漏洞被錯誤地降低優先度。

## 11.5 Container Scanning

詳見第九章 9.3 節，掃描已建置的容器映像中作業系統套件層的已知漏洞。

## 11.6 Secret Detection

```yaml
include:
  - template: Security/Secret-Detection.gitlab-ci.yml
```

偵測程式碼中誤提交的 API Key、密碼、私鑰等機密。建議搭配 **Pre-receive Secret Push Protection**（伺服器端在 `git push` 時即時阻擋含機密的提交），比起合併後才掃描更能防止機密外洩：

```bash
# 於專案設定啟用 Push Protection（透過 API）
glab api projects/:id --method PUT --field "secret_push_protection_enabled=true"
```

## 11.7 License Compliance

```yaml
include:
  - template: Security/License-Scanning.gitlab-ci.yml
```

掃描相依套件的開源授權條款（MIT、Apache-2.0、GPL-3.0 等），可設定政策阻擋使用特定授權（如企業通常禁止商業專案引入 GPL 系列授權的套件）。

## 11.8 Security Dashboard 與 Vulnerability Management

Security Dashboard 提供 Group/Project 層級的漏洞總覽，可依嚴重程度（Critical/High/Medium/Low）、狀態（待處理/已確認/已修復/誤判）篩選。

**Vulnerability Management 工作流程**：

```mermaid
flowchart LR
    Detected[掃描偵測到漏洞] --> Triage{安全團隊/開發團隊\n判定}
    Triage -- 確認為真實漏洞 --> Assign[指派負責人 + 設定 Due Date]
    Triage -- 誤判 --> Dismiss[標記為 Dismissed\n並記錄原因]
    Assign --> Fix[開發修復 + 建立 MR]
    Fix --> Rescan[重新掃描驗證]
    Rescan -- 已修復 --> Resolved[標記為 Resolved]
    Rescan -- 仍存在 --> Assign
```

```bash
# 透過 API 查詢專案目前未解決的 Critical 漏洞
glab api graphql -f query='
query {
  project(fullPath: "mygroup/myproject") {
    vulnerabilities(severity: CRITICAL, state: DETECTED) {
      nodes {
        title
        severity
        identifiers { name }
      }
    }
  }
}'
```

## 11.9 企業導入策略

1. **分階段導入，避免一次性阻斷所有 Pipeline**：第一階段先「偵測但不阻擋合併」（僅顯示警告），讓團隊熟悉掃描結果與處理流程；第二階段針對 Critical/High 漏洞設定 MR 合併門檻（Merge Request Approval Rules 要求安全團隊核准或必須先解決）。
2. **建立漏洞 SLA**：依嚴重程度訂定修復時限（如 Critical 7 天內、High 30 天內），並透過 Security Dashboard 追蹤逾期項目。
3. **集中化安全規則治理**：在 Platform 團隊維護的 `ci-templates` 共用範本中統一管理 `SAST_EXCLUDED_PATHS`、掃描頻率等設定，各應用團隊不可隨意關閉安全掃描。
4. **安全左移教育訓練**：搭配 GitLab Duo 的 Vulnerability Explanation 功能（第十三章），讓開發者理解漏洞成因與修復方式，而非只是「被擋下合併」卻不知為何。

> 💡 **實務案例**：某零售業集團導入 GitLab Ultimate 後，第一年僅先開啟 SAST + Secret Detection（偵測但不阻擋），蒐集到的真實漏洞修復率僅 40%；第二年正式將 Critical 漏洞設為合併硬性門檻並導入 SLA 追蹤後，修復率提升至 92%，平均修復時間從 45 天降至 11 天。

### ✅ 第十一章 Checklist

- [ ] 已啟用 SAST / Secret Detection / Dependency Scanning（基本安全掃描三件套）
- [ ] DAST 僅對 Staging 等測試環境執行，未對生產環境執行 Full Scan
- [ ] 已啟用 Secret Push Protection，在 push 階段即時阻擋機密外洩
- [ ] 已針對 Critical/High 漏洞設定合併門檻與修復 SLA
- [ ] 已將安全規則治理集中於共用 CI/CD 範本，避免各專案各自為政
- [ ] 已確認 Dependency Scanning 採用 SBOM-based 範本，並排定舊版 Gemnasium 式掃描的遷移時程（20.0 前須完成）
- [ ] 若已啟用 Agentic SAST 自動修補或 Duo 誤報偵測，已建立「AI 產生結果必經人工核准」的硬性規則

---

# 第十二章 GitLab API

## 12.1 REST API 與 GraphQL API 選用建議

| 比較項目 | REST API | GraphQL API |
|---|---|---|
| 學習曲線 | 低，符合一般 HTTP 慣例 | 中，需理解 Query/Mutation 語法 |
| 取得巢狀關聯資料 | 需多次請求（如先取 MR 再取其 Discussion） | 單次請求可一次取得巢狀資料，減少 Round-trip |
| 適合情境 | 簡單 CRUD、CLI Script、CI/CD Job | 需要複雜關聯查詢的 Dashboard、報表系統 |
| 版本穩定性 | v4 已長期穩定 | Schema 持續擴充中，部分新功能僅 GraphQL 提供 |

## 12.2 Access Token 種類

| Token 類型 | 範圍 | 適用情境 |
|---|---|---|
| Personal Access Token（PAT） | 綁定個人帳號權限 | 個人開發機操作、`glab auth login` |
| Project Access Token | 綁定單一專案，獨立身分 | 專案層級自動化（如部署機器人），與個人帳號脫鉤 |
| Group Access Token | 綁定整個 Group | 跨多專案的自動化（如集中報表蒐集） |
| CI Job Token（`CI_JOB_TOKEN`） | Pipeline 執行期間自動產生，範圍限於該次 Job | CI/CD 內呼叫 API、發布套件，無需另外管理機密 |

> ⚠️ **注意事項**：個人 PAT 會隨人員離職而失效，導致自動化腳本無預警中斷。**正式環境的自動化應一律使用 Project/Group Access Token 或 CI Job Token**，而非個人 PAT。

## 12.3 curl 範例

```bash
# 取得專案資訊
curl --header "PRIVATE-TOKEN: glpat-xxxxxxxxxxxx" \
  "https://gitlab.example.com/api/v4/projects/123"

# 建立 Merge Request
curl --request POST \
  --header "PRIVATE-TOKEN: glpat-xxxxxxxxxxxx" \
  --header "Content-Type: application/json" \
  --data '{
    "source_branch": "feature/order-refund",
    "target_branch": "main",
    "title": "feat: 新增訂單退款 API"
  }' \
  "https://gitlab.example.com/api/v4/projects/123/merge_requests"

# GraphQL 查詢
curl --request POST \
  --header "PRIVATE-TOKEN: glpat-xxxxxxxxxxxx" \
  --header "Content-Type: application/json" \
  --data '{"query": "query { currentUser { username } }"}' \
  "https://gitlab.example.com/api/graphql"
```

## 12.4 Java / Spring Boot 範例

```java
@Service
public class GitLabClient {

    private final WebClient webClient;

    public GitLabClient(@Value("${gitlab.base-url}") String baseUrl,
                         @Value("${gitlab.token}") String token) {
        this.webClient = WebClient.builder()
                .baseUrl(baseUrl)
                .defaultHeader("PRIVATE-TOKEN", token)
                .build();
    }

    public Mono<MergeRequestDto> createMergeRequest(Long projectId, MergeRequestCreateRequest request) {
        return webClient.post()
                .uri("/api/v4/projects/{id}/merge_requests", projectId)
                .bodyValue(request)
                .retrieve()
                .bodyToMono(MergeRequestDto.class);
    }

    public Flux<PipelineDto> listRecentPipelines(Long projectId) {
        return webClient.get()
                .uri("/api/v4/projects/{id}/pipelines?per_page=20", projectId)
                .retrieve()
                .bodyToFlux(PipelineDto.class);
    }
}
```

```yaml
gitlab:
  base-url: https://gitlab.example.com
  token: ${GITLAB_PROJECT_TOKEN}
```

## 12.5 Python 範例

```python
import requests

GITLAB_URL = "https://gitlab.example.com"
TOKEN = "glpat-xxxxxxxxxxxx"
HEADERS = {"PRIVATE-TOKEN": TOKEN}

def create_issue(project_id: int, title: str, description: str):
    resp = requests.post(
        f"{GITLAB_URL}/api/v4/projects/{project_id}/issues",
        headers=HEADERS,
        json={"title": title, "description": description},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()

def list_open_vulnerabilities(project_path: str):
    query = """
    query($fullPath: ID!) {
      project(fullPath: $fullPath) {
        vulnerabilities(state: DETECTED) {
          nodes { title severity }
        }
      }
    }
    """
    resp = requests.post(
        f"{GITLAB_URL}/api/graphql",
        headers=HEADERS,
        json={"query": query, "variables": {"fullPath": project_path}},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()
```

## 12.6 TypeScript 範例

```typescript
import axios from "axios";

const gitlab = axios.create({
  baseURL: process.env.GITLAB_BASE_URL,
  headers: { "PRIVATE-TOKEN": process.env.GITLAB_TOKEN },
});

export async function createRelease(projectId: number, tagName: string, notes: string) {
  const { data } = await gitlab.post(`/api/v4/projects/${projectId}/releases`, {
    tag_name: tagName,
    description: notes,
  });
  return data;
}

export async function getPipelineStatus(projectId: number, pipelineId: number) {
  const { data } = await gitlab.get(
    `/api/v4/projects/${projectId}/pipelines/${pipelineId}`
  );
  return data.status as string;
}
```

> 💡 **最佳實務**：所有語言範例皆應將 Token 透過環境變數或 Secret 管理工具（Vault、K8s Secret）注入，並針對 API 呼叫設定合理 timeout 與重試（429 Rate Limit 時依 `Retry-After` Header 退避重試），避免自動化腳本因瞬時網路問題而誤判失敗。

### ✅ 第十二章 Checklist

- [ ] 已依情境選用 REST 或 GraphQL（複雜關聯查詢優先考慮 GraphQL）
- [ ] 自動化腳本已改用 Project/Group Access Token 或 CI Job Token，未使用個人 PAT
- [ ] API 呼叫已實作 Rate Limit 退避重試與合理 timeout
- [ ] 各語言 SDK/Client 已封裝統一錯誤處理，避免裸露 Token 於 Log 中

---

# 第十三章 GitLab Duo

## 13.1 GitLab Duo 功能總覽

GitLab Duo 是 GitLab 內建的生成式 AI 功能套件，深度整合在開發流程的每個環節，而非獨立的外部工具：

```mermaid
flowchart TB
    Duo[GitLab Duo]
    Duo --> Chat[Duo Agentic Chat\n多步驟推理/可主動執行動作]
    Duo --> Suggest[Code Suggestions\nIDE 即時程式碼補全]
    Duo --> Review[Code Review\nMR 自動審查摘要與建議]
    Duo --> VulnExplain[Vulnerability Explanation\n漏洞成因解釋與修復建議]
    Duo --> TestGen[Test Generation\n自動產生單元測試]
    Duo --> Refactor[Refactoring\n程式碼重構建議]
    Duo --> AgentPlatform[Duo Agent Platform（已 GA）\nFoundational / Custom / External Agents]
```

## 13.2 GitLab Duo Chat

在 Web UI 或 IDE 擴充套件中直接提問，Chat 會結合當前專案上下文（程式碼、Issue、MR）回答：

```text
> 為什麼這個 MR 的 Pipeline 在 unit-test stage 失敗？
> 幫我解釋 OrderRefundService.java 第 42 行的邏輯
> 這個專案最近一週有哪些未解決的 Critical 漏洞？
```

亦可透過 `glab duo ask` 在終端機直接使用（見第五章 5.10 節）：

```bash
glab duo ask "幫我比較 main 分支與 release/2.3.0 分支在 OrderService 的差異，並指出潛在風險"
```

### 13.2.1 Agentic Chat 與 Non-Agentic Chat 退場

GitLab Duo Chat 目前實際上分為兩種運作模式，企業導入時必須先分清楚兩者差異：

| 模式 | 特性 | 目前狀態 |
|---|---|---|
| **Agentic Chat**（多步驟、可執行動作） | 能自主規劃多個步驟、串接 Issue/MR/Pipeline/安全掃描等多項資料來源，並可在獲得授權後實際執行動作（如建立 MR、回覆留言），而非只回答單一問題 | 目前為**正式（GA）主力功能**，是企業應優先導入與訓練團隊使用的模式 |
| **Non-Agentic Chat**（傳統單輪問答） | 僅針對單一問題給出單輪回覆，不具備多步驟規劃與動作執行能力 | **自 2026-05-21 起，Core 方案使用者已無法繼續使用此模式**，須升級至 Pro / Ultimate 方案，或改用 Agentic Chat |

> ⚠️ **注意事項**：若企業目前仍以 Core 方案使用 GitLab，且內部教育訓練教材或操作手冊還停留在「傳統單輪問答」的使用情境，務必同步更新——這項變更已經生效，並非未來計畫。建議 Platform 團隊盤點方案等級，評估是否需要升級訂閱方案，才能讓開發團隊持續使用 Duo Chat 能力。

### 13.2.2 GitLab Duo Agent Platform（已 GA）

GitLab Duo Agent Platform 是 GitLab Duo 由「單點 AI 輔助功能」邁向「平台化多 Agent 協作」的核心架構，目前已正式 GA（General Availability），分為三層：

```mermaid
flowchart TB
    Platform[GitLab Duo Agent Platform]
    Platform --> Foundational["Foundational Agents（內建預設）\n例如：通用 GitLab Duo Agent、\n發佈規劃 Agent、程式碼安全 Agent"]
    Platform --> Custom["Custom Agents（組織自訂）\n依團隊專屬工作流程客製化的 Agent"]
    Platform --> External["External Agents（外部模型整合）\n串接外部 AI 模型供應商或既有 Agent"]
```

- **Foundational Agents**：GitLab 預先建置、開箱即用的通用型 Agent，涵蓋一般問答、release 規劃輔助、程式碼安全分析等常見場景，不需額外設定即可開始使用。
- **Custom Agents**：組織可依自身的 SOP（如「Spring Boot 升級檢查清單 Agent」「內部 API 規範審查 Agent」）建立客製化 Agent，將團隊知識封裝為可重複呼叫的自動化流程。
- **External Agents**：允許串接外部 AI 模型供應商或既有的 Agent 框架（例如透過 MCP 協定，見第十六章），讓企業既有的 AI 投資可以與 GitLab Duo Agent Platform 協同運作，而不必整套重新建置。

> 💡 **企業導入建議**：建議先以 Foundational Agents 熟悉操作模式與權限授權流程，待團隊掌握「Agent 可以做什麼、不能做什麼、誰來核准動作」的治理模式後，再評估是否投入資源建立 Custom Agents，避免一開始就追求高度客製化卻忽略了基本的權限與稽核機制。

## 13.3 Code Suggestions（程式碼建議）

在 VS Code / JetBrains IDE 安裝 **GitLab Workflow** 擴充套件並登入後，輸入程式碼時會即時顯示 AI 建議的補全內容（類似 Copilot），支援多數主流語言（Java、Python、JavaScript/TypeScript、Go、Vue 等）。

> 💡 **最佳實務**：在 `.gitlab/duo/` 設定目錄中可定義專案層級的 Context 排除規則（如排除 `*.generated.ts`、`vendor/`），避免 AI 建議學習到不該參考的自動產生程式碼或第三方套件原始碼。

## 13.4 Code Review（MR 自動審查）

在 MR 頁面點選「Request Duo review」，或在 `.gitlab-ci.yml` / MR 設定中啟用自動觸發，Duo 會：

- 摘要 Diff 變更的核心邏輯。
- 標示潛在 Bug、效能問題、安全風險。
- 提出具體修改建議（可一鍵套用為 Suggested Change）。

```bash
# 透過 glab 對指定 MR 觸發 Duo Review
glab duo ask "請審查 MR !482 的程式碼變更" --mr 482
```

> ⚠️ **注意事項**：Duo Code Review 是輔助審查，**不取代人工 Reviewer**。建議將 Duo Review 設為「審查前的第一輪自我檢查」，協助開發者在請真人 Review 前先抓出明顯問題，加速審查迴圈，而非把核准責任完全交給 AI。

## 13.5 Vulnerability Explanation

在 Security Dashboard 的漏洞詳情頁，點選「Explain this vulnerability」，Duo 會以該專案實際程式碼上下文解釋：

- 此漏洞的成因（例如 SQL Injection 的具體觸發路徑）。
- 可能造成的實際風險情境。
- 具體修復建議（含程式碼範例）。

對於資安背景較淺的開發團隊，這項功能可大幅降低「看到 CVE 編號卻不知如何下手修復」的情況。

## 13.6 Test Generation 與 Refactoring

```text
> 幫 OrderRefundService.processRefund() 產生單元測試，需覆蓋成功退款、超額退款、訂單不存在三種情境
> 幫我重構這段巢狀 if-else，改用早期返回（Early Return）模式
```

產生的測試/重構建議會以 Suggested Change 形式呈現在 MR 或 IDE 中，開發者可選擇套用、修改後套用或忽略。

## 13.7 Prompt Engineering 最佳實務

1. **提供具體上下文**：直接點名檔案、函式、MR/Issue 編號，比泛問「這段程式碼有問題嗎」更精準。
2. **拆解大問題為多個小提問**：先問「這個模組的職責是什麼」再問「如何重構」，比一次問「幫我重構整個模組」效果更好。
3. **要求結構化輸出**：例如「請用條列式列出風險，並標註嚴重程度」，方便團隊後續追蹤。
4. **明確說明限制**：例如「不要修改公開 API 介面，只重構內部實作」，避免 AI 建議的修改範圍超出預期。
5. **善用迭代**：第一輪建議不滿意時，提供具體回饋（如「這個方案會破壞既有測試，請改用其他方式」）讓 Duo 修正方向，而非直接放棄重新問。

> 💡 **實務案例**：某保險業團隊將「MR 描述自動產生」與「Duo Code Review」納入標準流程後，Code Review 平均耗時從 35 分鐘降至 18 分鐘，主要原因是 Reviewer 不再需要從零理解變更內容，可直接針對 Duo 已標示的風險點進行確認與討論。

### ✅ 第十三章 Checklist

- [ ] 開發團隊已安裝並登入 IDE 的 GitLab Workflow 擴充套件，啟用 Code Suggestions
- [ ] MR 流程已納入 Duo Code Review 作為人工審查前的輔助檢查
- [ ] 安全團隊已善用 Vulnerability Explanation 協助開發者理解並修復漏洞
- [ ] 團隊已建立 Prompt Engineering 共用範例庫，避免每個人重新摸索有效提問方式
- [ ] 已確認目前訂閱方案（Core/Pro/Ultimate）是否受 Non-Agentic Duo Chat 退場（2026-05-21 生效）影響，並完成相關升級或改用 Agentic Chat 的教育訓練
- [ ] 已盤點 GitLab Duo Agent Platform 的 Foundational Agents 使用情境，評估是否需要建立 Custom Agents 並建立對應的權限與稽核機制
- [ ] 已設定 `.gitlab/duo/` Context 排除規則，避免 AI 學習到不相關的自動產生程式碼

---

# 第十四章 GitLab + Claude Code

## 14.1 整合架構總覽

Claude Code 可透過兩種方式與 GitLab 協作：

1. **透過 `glab` CLI**：Claude Code 在終端機環境中直接呼叫 `glab` 指令（建立 MR、查 Pipeline、留言），這是目前最直接、免額外設定的整合方式。
2. **透過 GitLab MCP Server**：Claude Code 以 MCP 協定連接 GitLab，取得結構化的工具呼叫介面（建立 Issue、查詢漏洞、操作 MR），相較於 CLI 字串輸出，MCP 回傳結構化資料更適合 Agent 進行多步驟推理（詳見第十六章）。

```mermaid
flowchart LR
    Claude[Claude Code]
    Claude -- 終端機指令 --> Glab[glab CLI]
    Claude -- MCP 協定 --> MCP[GitLab MCP Server]
    Glab --> GitLabAPI[GitLab REST/GraphQL API]
    MCP --> GitLabAPI
    GitLabAPI --> Project[GitLab 專案\nMR / Issue / Pipeline]
```

## 14.2 實戰案例：Claude Code 自動建立並提交 Merge Request

**情境**：開發者在 Claude Code 中描述需求「修正訂單退款金額計算錯誤」，由 Claude Code 完成程式碼修改、撰寫測試、建立分支、commit、push，並建立 MR。

```bash
# Claude Code 在背景依序執行（使用者可在對話中觀察每一步）
git checkout -b fix/order-refund-amount-calculation
# ... Claude Code 編輯 OrderRefundService.java 並新增/修改測試 ...
git add src/main/java/com/example/order/OrderRefundService.java \
        src/test/java/com/example/order/OrderRefundServiceTest.java
git commit -m "fix: 修正訂單退款金額計算未考慮已退款部分金額的問題"
git push -u origin fix/order-refund-amount-calculation

glab mr create \
  --title "fix: 修正訂單退款金額計算錯誤" \
  --description "## 問題\n退款金額計算未排除先前已退款部分，導致重複退款。\n\n## 修改\n- 修正 OrderRefundService.calculateRefundableAmount()\n- 新增邊界測試案例\n\n## 測試\n已新增單元測試覆蓋多次部分退款情境" \
  --target-branch main \
  --reviewer alice \
  --label "bug,backend"
```

> 💡 **實務建議**：要求 Claude Code 在建立 MR 前，先用 `glab pipeline ci view` 或本機跑一次測試確認綠燈，避免建立 MR 後才發現 Pipeline 失敗，造成 Reviewer 不必要的等待。

## 14.3 實戰案例：Claude Code 自動 Review 程式碼

**情境**：在 MR 建立後，請 Claude Code 針對該 MR 進行第二輪獨立審查（作為人工 Reviewer 之外的補充視角）。

```bash
# 取得 MR 的程式碼差異供 Claude Code 分析
glab mr diff 482 > /tmp/mr-482.diff
```

對話中請 Claude Code：

```text
請閱讀 /tmp/mr-482.diff，從正確性、安全性、效能三個角度審查，
並將發現的問題透過 glab mr note 482 留言在 MR 上，每個問題附上具體行號與建議修改方式。
```

Claude Code 會執行：

```bash
glab mr note 482 --message "## 🤖 Claude Code 審查意見

### 正確性
- \`OrderRefundService.java:58\`：當 \`refundAmount\` 為負數時未做邊界檢查，建議於方法開頭加入 \`if (refundAmount.compareTo(BigDecimal.ZERO) < 0) throw new IllegalArgumentException(...)\`

### 安全性
- 未發現明顯安全風險

### 效能
- \`OrderRefundService.java:71\`：迴圈內重複查詢資料庫，建議改用批次查詢（\`findAllByOrderIdIn\`）避免 N+1 問題"
```

## 14.4 實戰案例：Pipeline 失敗時自動診斷

```text
使用者：MR !482 的 Pipeline 失敗了，幫我看看為什麼
```

Claude Code 會依序執行：

```bash
glab mr view 482
glab pipeline list --branch fix/order-refund-amount-calculation
glab pipeline ci trace unit-test   # 取得失敗 Job 的完整 Log
```

分析 Log 後，Claude Code 直接在本機修正程式碼、重新 push，並可選擇性留言告知已修復：

```bash
glab mr note 482 --message "已修正 unit-test 失敗原因（測試資料缺少必要欄位 \`refundReason\`），已 push 新的 commit，請重新觸發 Pipeline。"
```

## 14.5 CLAUDE.md 專案規範整合建議

建議在專案根目錄的 `CLAUDE.md` 中明確記載團隊的 GitLab 協作規範，讓 Claude Code 在每次任務中自動遵循，避免每次對話都要重新說明：

```markdown
## GitLab 協作規範

- 所有 MR 標題需符合 Conventional Commits 格式（feat/fix/refactor/docs/test/chore）
- 建立 MR 前必須確認本機測試通過（mvn test 或 npm run test）
- MR 描述需包含「問題」「修改」「測試」三個段落
- 禁止直接 push 到 main，所有變更必須透過 MR
- Reviewer 預設指派：backend 變更指派 @alice，frontend 變更指派 @bob
- 機密與 Token 一律透過環境變數讀取，不可寫入程式碼或提交記錄
```

> ⚠️ **注意事項**：讓 AI Agent（Claude Code）自動建立 MR、留言、甚至合併程式碼時，務必確保 **Protected Branch 與 Approval Rules 仍要求至少一位真人核准**，AI 可加速產出與初步審查，但正式合併決策應保留人工把關，尤其是涉及生產環境部署的高風險變更。

### ✅ 第十四章 Checklist

- [ ] 已在開發機安裝並登入 `glab`，確認 Claude Code 可成功呼叫
- [ ] 已建立專案 `CLAUDE.md`，明確記載 MR/Commit/Reviewer 規範
- [ ] Protected Branch 與 Approval Rules 仍要求人工核准，AI 自動化不取代最終把關
- [ ] 已建立「Claude Code 建 MR 前必先跑本機測試」的團隊慣例
- [ ] 已評估 CLI 整合與 MCP 整合（第十六章）兩種方式的適用情境

---

# 第十五章 GitLab + GitHub Copilot

## 15.1 為什麼會在 GitLab 上使用 GitHub Copilot

許多企業的開發者習慣使用 GitHub Copilot 作為 IDE 內的程式碼建議工具，即便版本控制與專案管理主要在 GitLab 上進行。Copilot 與 GitLab 並非互斥關係：

- **Copilot in IDE**：純粹作為編輯器內的程式碼補全/Chat 工具，與後端是 GitLab 或 GitHub 無關。
- **Copilot Agent Mode / Coding Agent**：可在 IDE 中執行多步驟任務（讀檔、改檔、跑測試），這部分行為與 Claude Code 類似，皆可透過終端機呼叫 `glab` 與 GitLab 互動。
- **Copilot Review Agent**：原生設計給 GitHub PR 流程，若要在 GitLab MR 上取得類似的 AI 審查體驗，建議優先使用 GitLab Duo Code Review（第十三章），而非試圖橋接 Copilot Review Agent。

```mermaid
flowchart TB
    Dev[開發者]
    IDE[IDE: VS Code / JetBrains]
    Copilot[GitHub Copilot\nChat / Agent Mode]
    Glab[glab CLI]
    GitLab[GitLab 專案]

    Dev --> IDE
    IDE --> Copilot
    Copilot -- Agent Mode 執行終端機指令 --> Glab
    Glab --> GitLab
```

## 15.2 Agent Mode 與 Coding Agent 操作模式

GitHub Copilot 的 Agent Mode 可在獲得使用者授權後執行終端機指令、編輯多個檔案。當專案的版本控制是 GitLab 時，操作模式與第十四章 Claude Code 的整合方式高度相似：

```text
使用者於 Copilot Chat（Agent Mode）：
「請修正 OrderRefundService 的金額計算 bug，寫測試，並建立 MR 到 GitLab」
```

Copilot Agent Mode 會在終端機執行：

```bash
git checkout -b fix/refund-amount-bug
# 編輯程式碼...
git add . && git commit -m "fix: 修正退款金額計算邏輯"
git push -u origin fix/refund-amount-bug
glab mr create --title "fix: 修正退款金額計算邏輯" --target-branch main --fill
```

> ⚠️ **注意事項**：Copilot Agent Mode 預設熟悉 GitHub 生態（會傾向呼叫 `gh` 而非 `glab`），在 GitLab 專案中使用時，建議在專案內的 Copilot 指令說明檔（如 `.github/copilot-instructions.md`，部分團隊亦放在通用的 `AGENTS.md`）中明確指示「本專案使用 GitLab，所有版本控制相關操作請使用 `glab` 指令而非 `gh`」，避免 Agent 誤呼叫不存在的工具或產生混淆的操作建議。

## 15.3 如何與 GitLab 協作（實務整合建議）

1. **統一 Agent 指令說明檔**：無論團隊用 Claude Code 或 Copilot，都在專案根目錄維護一份說明文件（`CLAUDE.md` 或 `AGENTS.md`），記載「本專案使用 GitLab + glab」「MR 規範」「Reviewer 指派規則」，讓不同 AI 工具的行為一致。
2. **以 MCP 作為共同介面**：若團隊同時有人用 Claude Code、有人用 Copilot，可統一透過 GitLab MCP Server（第十六章）作為兩者都支援的標準化整合層，減少各自摸索 CLI 用法的成本。
3. **Code Review 仍以 GitLab Duo 為主力**：因為 Duo 與 GitLab 資料模型（MR Diff、Security Dashboard、Vulnerability 資料）整合最深，Copilot Review Agent 主要設計給 GitHub PR，跨平台橋接通常體驗不如原生方案。
4. **避免雙重 AI 審查造成噪音**：若同時啟用 Duo Code Review 與 Copilot Agent 的審查建議，留言可能重複或矛盾，建議團隊明確分工（如 Duo 負責安全/正確性，Copilot 僅用於開發階段輔助，不重複留言在 MR 上）。

> 💡 **實務案例**：某跨國企業的前端團隊習慣用 GitHub Copilot（個人授權延續舊習慣），後端團隊已全面採用 GitLab Duo。透過統一維護 `AGENTS.md` 並要求所有 AI 工具的終端機操作一律走 `glab`，兩個團隊的 MR 格式、Commit 規範得以保持一致，未因工具不同而產生治理落差。

### ✅ 第十五章 Checklist

- [ ] 已建立 `AGENTS.md` 或等效說明文件，明確告知 AI 工具本專案使用 GitLab + glab
- [ ] 已避免同時啟用多個 AI 審查工具在同一個 MR 上重複留言
- [ ] 已確認 Copilot Agent Mode 產生的變更仍遵循專案的分支保護與 Approval Rules
- [ ] 團隊已就「何時用 Duo、何時用 Copilot」建立明確分工原則

---

# 第十六章 GitLab + MCP

## 16.1 Model Context Protocol 簡介

**Model Context Protocol（MCP）** 是由 Anthropic 提出、現已成為業界共通標準的開放協定，讓 AI Agent（如 Claude Code）可以用標準化方式連接外部工具與資料來源（如 GitLab、Jira、資料庫），而不需要每個 Agent 各自實作對接邏輯。

```mermaid
flowchart LR
    subgraph Agents["AI Agent"]
        Claude[Claude Code]
        Copilot[GitHub Copilot]
        OtherAgent[其他支援 MCP 的 Agent]
    end
    subgraph MCPLayer["MCP 標準化介面"]
        MCPServer[GitLab MCP Server]
    end
    GitLabAPI[GitLab REST/GraphQL API]
    GitLabData[(專案 / MR / Issue / Pipeline / 漏洞資料)]

    Claude -- MCP 協定 --> MCPServer
    Copilot -- MCP 協定 --> MCPServer
    OtherAgent -- MCP 協定 --> MCPServer
    MCPServer --> GitLabAPI
    GitLabAPI --> GitLabData
```

MCP 相較於「Agent 自己呼叫 CLI 或拼 API 請求」的優勢：

- **結構化工具定義**：每個操作（建立 Issue、查詢 MR、觸發 Pipeline）都有明確的輸入輸出 Schema，Agent 呼叫時不易因為猜測指令參數而出錯。
- **權限可細粒度控管**：可設定 MCP Server 僅開放唯讀工具，或限制特定工具（如禁止 Agent 直接呼叫「合併 MR」）。
- **跨 Agent 通用**：同一個 MCP Server 設定，可同時被 Claude Code、Copilot 或任何支援 MCP 的工具使用，不需要為每個 Agent 各寫一套整合邏輯。

## 16.2 GitLab MCP Server 現況與安裝

GitLab 官方維護的 MCP Server 目前狀態為 **Beta**（已脫離早期 Experimental 階段，代表官方對其穩定度有更高信心，但仍建議在正式導入前進行充分測試）。它支援兩種 transport（傳輸方式）：

| Transport | 說明 | 建議使用情境 |
|---|---|---|
| **HTTP**（官方建議） | 以 HTTP 端點對外提供服務，可部署為長駐服務，多個 Agent/使用者可共用同一個 Server | 團隊共用、企業正式導入時的**首選方式** |
| **stdio**（搭配 `mcp-remote`） | 透過標準輸入輸出與本機程序通訊，啟動方式與傳統 CLI 工具類似 | 個人開發機快速試用、相容舊版設定的場景 |

GitLab MCP Server 已支援 MCP 協定的 **2025-03-26** 與 **2025-06-18** 兩個版本規格，連接的 AI Agent 端（如 Claude Code）需確認其 MCP Client 實作版本相容。

```bash
# 確認 glab 版本已支援 mcp 子指令
glab version

# 方式一（建議）：以 HTTP transport 啟動，供團隊共用
glab mcp serve --transport http --port 8585

# 方式二：以 stdio 模式啟動，供本機單一 Agent 連接（相容性選項）
glab mcp serve
```

> ⚠️ **注意事項**：由於目前仍是 Beta 狀態，指令旗標與預設行為可能隨小版號調整，正式導入前請務必查閱當下安裝版本的 `glab mcp serve --help`，不要直接套用本手冊的旗標範例到生產環境腳本中。

## 16.3 設定 Claude Code 連接 GitLab MCP Server

在 Claude Code 的 MCP 設定（`~/.claude/mcp_settings.json` 或專案層級 `.mcp.json`）中加入：

```json
{
  "mcpServers": {
    "gitlab": {
      "url": "https://gitlab-mcp.example.com:8585",
      "transport": "http",
      "env": {
        "GITLAB_TOKEN": "${GITLAB_TOKEN}",
        "GITLAB_HOST": "gitlab.example.com"
      }
    }
  }
}
```

若團隊暫時仍採用 stdio 相容模式，可改為：

```json
{
  "mcpServers": {
    "gitlab": {
      "command": "glab",
      "args": ["mcp", "serve"],
      "env": {
        "GITLAB_TOKEN": "${GITLAB_TOKEN}",
        "GITLAB_HOST": "gitlab.example.com"
      }
    }
  }
}
```

設定完成後，Claude Code 可直接以工具呼叫的方式操作 GitLab，例如「列出我被指派的 MR」「查詢專案目前的 Critical 漏洞」，而不需要使用者手動輸入 `glab` 指令。

## 16.4 權限管理

```bash
# 唯讀模式：僅允許查詢類工具（list/view/search），禁止建立/修改/合併
glab mcp serve --read-only

# 限定特定工具集合（視版本支援，僅開放 MR 與 Issue 相關工具）
glab mcp serve --tools mr,issue
```

> ⚠️ **注意事項**：企業導入 AI Agent + MCP 時，務必先以 **唯讀模式**（`--read-only`）試行一段時間，觀察 Agent 的查詢行為與使用情境是否符合預期，確認無誤後才逐步開放寫入類工具（建立 MR、留言），最後才考慮是否開放高風險操作（合併、刪除分支、修改 Protected 設定）。任何寫入類操作仍應受 Protected Branch / Approval Rules 約束，MCP 權限收緊只是第一道防線，不能取代 GitLab 原生的權限模型。

## 16.5 實際案例：多步驟 Agent 工作流程

**情境**：請 Claude Code 透過 MCP「分析本週所有未解決的 Critical 漏洞，產生摘要報告，並對每個漏洞在 GitLab 建立對應 Issue 指派給負責團隊」。

Agent 透過 MCP 依序呼叫的工具（概念示意，實際工具名稱依 MCP Server 實作版本而定）：

```text
1. gitlab.listVulnerabilities(severity="CRITICAL", state="DETECTED")
2. 對每個漏洞 → gitlab.createIssue(title=..., description=..., labels=["security","critical"])
3. gitlab.assignIssue(issueId=..., assignee=依漏洞所屬模組對應的團隊)
4. 產生彙整報告（Markdown），回覆給使用者確認
```

相較於人工逐筆在 Web UI 建立 Issue，此流程可將原本需要 1-2 小時的彙整作業縮短至數分鐘，且保證每個漏洞都有對應追蹤紀錄不被遺漏。

> 💡 **實務案例**：某金融科技公司導入 GitLab MCP Server 後，將「每週安全漏洞彙整與分派」流程交由 Claude Code 透過 MCP 自動執行，原本需要資安人員人工撈報表、開 Issue、@相關人員的流程，全部自動化，資安人員的角色轉為審核 AI 產出的分派是否合理，而非親自執行重複性的資料蒐集工作。

## 16.6 GitLab Orbit（Knowledge Graph）與 AI Agent

MCP 工具呼叫解決了「Agent 如何結構化存取 GitLab 資料」的問題，但當企業擁有數百個專案、跨團隊的服務相依關係複雜時，Agent 仍可能因為「不知道該查哪個專案、哪個函式」而要花多輪工具呼叫才能找到正確上下文。**GitLab Orbit**（Knowledge Graph，目前為 Beta）正是為了補上這塊拼圖：它在伺服器端預先建立跨專案的程式碼關聯索引（誰呼叫誰、哪個服務依賴哪個 API），讓 AI Agent 可以直接查詢語意層級的關聯，而不必逐專案翻找原始碼。

```mermaid
flowchart LR
    Repos[多個 GitLab 專案原始碼]
    Repos --> Orbit[GitLab Orbit\nKnowledge Graph 索引]
    Orbit --> MCPServer[GitLab MCP Server]
    MCPServer --> Agent[AI Agent\nClaude Code / Duo Agent Platform]
    Agent -- 語意查詢 --> Orbit
```

```bash
# 建立/更新本地知識圖譜索引（見第五章 5.16）
glab orbit local setup

# Agent 透過 MCP 間接呼叫 Orbit 查詢「OrderRefundService 被哪些上游服務呼叫」
glab orbit remote --query "誰呼叫了 OrderRefundService.processRefund"
```

> ⚠️ **注意事項**：Orbit 與 MCP 一樣需要先在伺服器端啟用對應功能，且索引建立會消耗額外運算與儲存資源；目前仍為 Beta 狀態，行為與輸出格式可能隨版本調整，企業導入時應視為「強化 Agent 上下文理解」的加值能力，而非取代既有的 MCP 工具呼叫機制。

### ✅ 第十六章 Checklist

- [ ] 已安裝具備 `mcp` 子指令的 `glab` 版本，並完成 MCP Server 啟動測試
- [ ] 已確認 GitLab MCP Server 目前為 Beta 狀態，並優先採用官方建議的 HTTP transport（而非僅依賴 stdio）
- [ ] 已在 Claude Code（或其他支援 MCP 的工具）設定檔中正確配置 GitLab MCP Server 連線
- [ ] 已先以 `--read-only` 模式試行，確認 Agent 查詢行為符合預期後才逐步開放寫入工具
- [ ] 高風險操作（合併、刪除、權限變更）仍受 GitLab 原生 Protected Branch / Approval Rules 約束
- [ ] 已記錄至少一個多步驟 Agent 工作流程案例，驗證 MCP 整合的實際效益
- [ ] 已評估是否導入 GitLab Orbit 強化 Agent 的跨專案語意查詢能力，並確認伺服器端已啟用對應功能

---

# 第十七章 AI 協助 Legacy System 逆向工程

## 17.1 為什麼 Legacy System 逆向工程適合導入 AI

許多企業核心系統以 **IBM Notes/Domino、Struts、Spring MVC（舊版）、VB6、Delphi、PowerBuilder、COBOL** 等技術撰寫，原開發人員多已離職，文件殘缺，導致：

- 沒人完全理解某些模組的業務邏輯，修改時只能「不敢動」。
- 新進工程師需要數月才能上手，學習曲線陡峭。
- 缺乏自動化測試，任何重構都伴隨高風險。

AI Agent（GitLab Duo / Claude Code / Copilot）可大幅加速「讀懂舊程式碼、產生文件、規劃重構」的過程，但**必須先把舊程式碼納入 GitLab 版本控制**，才能讓 AI Agent 與 CI/CD 流程介入。

```mermaid
flowchart LR
    Legacy[Legacy 原始碼\nCOBOL/VB6/Delphi/PowerBuilder/Domino]
    Legacy -->|匯入| GitLabRepo[GitLab Repository]
    GitLabRepo --> AIAnalysis[AI Agent 分析\nClaude Code / Duo Chat]
    AIAnalysis --> ArchDoc[架構文件\nMermaid 圖 + 模組說明]
    AIAnalysis --> RiskMap[風險地圖\n高複雜度/高耦合模組標示]
    AIAnalysis --> RefactorPlan[重構計畫\nIssue + Epic 拆解]
    RefactorPlan --> MRs[逐步重構 MR]
    MRs --> GitLabRepo
```

## 17.2 實戰步驟：將 Legacy 程式碼匯入 GitLab 並建立分析基線

```bash
# 1. 將既有原始碼（即便是從未版控的 PowerBuilder/Delphi 專案）匯入 GitLab
glab repo create legacy/order-system-vb6 --private
git init
git remote add origin https://gitlab.example.com/legacy/order-system-vb6.git
git add .
git commit -m "chore: 匯入既有 VB6 訂單系統原始碼（逆向工程基線）"
git push -u origin main

# 2. 建立 Epic 追蹤整體逆向工程專案
glab api projects/:id/epics --method POST --field "title=訂單系統逆向工程與文件化"
```

## 17.3 實戰案例：AI Agent 自動分析 Legacy System

以 PowerBuilder 訂單系統為例，請 Claude Code（已透過 MCP 或 CLI 連接該 GitLab 專案）執行分析：

```text
使用者：請分析這個 PowerBuilder 訂單系統，找出核心業務邏輯模組，
並標示出哪些 .srw/.sru 檔案彼此高度耦合、哪些是死代碼（無任何呼叫來源）。
```

Claude Code 會：

1. 掃描所有 `.srw`（Window）、`.sru`（User Object）、`.srf`（Function）檔案。
2. 建立呼叫關係圖（哪個 Window 呼叫哪個 User Object 的哪個函式）。
3. 標示出無外部呼叫來源的疑似死代碼。
4. 將分析結果整理為 Markdown 文件，並提交為 MR：

```bash
git checkout -b docs/legacy-analysis-order-window
# Claude Code 產生 docs/architecture/order-window-analysis.md
git add docs/architecture/order-window-analysis.md
git commit -m "docs: 新增訂單視窗模組逆向工程分析文件"
git push -u origin docs/legacy-analysis-order-window
glab mr create --title "docs: 訂單視窗模組逆向工程分析" --target-branch main --fill
```

## 17.4 各 Legacy 技術的 AI 逆向工程要點

| 技術 | 常見挑戰 | AI 協助重點 |
|---|---|---|
| IBM Notes/Domino | 業務邏輯藏在 Form/View 的 LotusScript 中，UI 與邏輯高度耦合 | 請 AI 萃取 LotusScript 邏輯並對應到現代分層架構（Controller/Service/Repository）草案 |
| Java Legacy（Struts/Spring MVC 舊版） | XML 設定檔（struts-config.xml）與程式碼分離，難以追蹤完整請求流程 | 請 AI 串接 Action 類別與 XML 設定，產出完整請求生命週期圖 |
| VB6 | 全域變數氾濫、無模組化、GOTO 語句 | 請 AI 標示全域變數的所有讀寫位置，評估封裝為類別的可行性 |
| Delphi | Form 與 Business Logic 混雜在同一個 Unit | 請 AI 區分 UI 事件處理與純業務邏輯，作為未來分離的依據 |
| PowerBuilder | DataWindow 將 SQL 與顯示邏輯綁定 | 請 AI 萃取 DataWindow 內嵌的 SQL，整理成獨立的資料存取邏輯文件 |
| COBOL | 大量 GOTO、Copybook 共用資料結構複雜 | 請 AI 將 Paragraph 呼叫關係視覺化，標示出核心交易處理路徑 |

## 17.5 文件生成與架構分析範本

請 AI Agent 產出的逆向工程文件建議統一包含以下結構（可作為 Prompt 範本）：

```text
請針對 [模組名稱] 產生逆向工程文件，包含：
1. 模組職責概述（這個模組在整體系統中負責什麼）
2. 對外介面（被哪些模組呼叫、呼叫哪些外部模組/資料庫表）
3. 核心業務規則條列（特別標示「看起來像 Bug 但可能是刻意設計」的邏輯）
4. Mermaid 流程圖（呈現主要處理流程）
5. 重構風險評估（高/中/低），並說明理由
6. 建議的測試案例清單（即便目前沒有自動化測試，先列出應該測什麼）
```

## 17.6 逆向工程後的重構規劃

將分析結果轉化為可執行的 GitLab Issue/Epic 結構：

```mermaid
flowchart TB
    Epic[Epic: 訂單系統現代化]
    Epic --> I1[Issue: 文件化現有 12 個核心模組]
    Epic --> I2[Issue: 補齊核心交易路徑的特性測試 Characterization Test]
    Epic --> I3[Issue: 拆解全域變數為服務類別]
    Epic --> I4[Issue: 逐模組改寫為 Spring Boot 微服務]
    I2 --> I4
    I3 --> I4
```

> ⚠️ **注意事項**：逆向工程階段請 AI Agent **產出文件與分析，而非直接大規模修改 Legacy 程式碼**。在沒有自動化測試覆蓋的情況下，任何「順手重構」都可能引入無法被偵測的迴歸錯誤。務必先依 AI 產出的建議，補上「特性測試」（Characterization Test，先固化現有行為而非驗證正確性）後，才開始實質重構。

> 💡 **實務案例**：某壽險公司有一套 20 年歷史的 PowerBuilder 核保系統，過去評估「重寫」需要 18 個月且風險極高。改用 AI Agent 先進行 3 個月的逆向工程與文件化，產出完整模組地圖與風險評估後，採用「逐模組替換」策略，搭配 GitLab Epic/Issue 追蹤進度，整體專案風險與時程可控性大幅提升，且每個模組替換完成即可上線，不需要等待整體系統一次性切換。

### ✅ 第十七章 Checklist

- [ ] 已將 Legacy 原始碼匯入 GitLab 版本控制，建立分析基線
- [ ] 已建立 Epic 追蹤整體逆向工程與現代化專案
- [ ] AI Agent 產出的文件已包含模組職責、對外介面、業務規則、風險評估
- [ ] 重構前已補齊特性測試（Characterization Test），而非直接修改 Legacy 程式碼
- [ ] 已將分析結果拆解為具體可執行的 Issue，並排定優先順序

---

# 第十八章 Framework 升級專案

## 18.1 升級專案的 GitLab 治理框架

大型 Framework 升級（如 Spring Boot 2→3、Java 8→21、Vue2→Vue3、Angular 升級）涉及多模組、長時間跨度，建議用 GitLab 的 Epic/Roadmap/Issue/MR/CI/CD/Deployment 完整串接管理：

```mermaid
flowchart TB
    Epic[Epic: Spring Boot 2 → 3 升級]
    Epic --> Roadmap[Roadmap 呈現跨季度時程]
    Epic --> I1[Issue: 相依套件相容性盤點]
    Epic --> I2[Issue: javax.* → jakarta.* 命名空間遷移]
    Epic --> I3[Issue: 設定檔格式調整]
    Epic --> I4[Issue: 整合測試全面驗證]
    I1 --> MR1[MR: 升級父 POM 版本]
    I2 --> MR2[MR: 套件命名空間批次替換]
    I3 --> MR3[MR: application.yml 調整]
    I4 --> MR4[MR: 修正升級後測試失敗]
    MR1 --> CI[CI/CD Pipeline 驗證]
    MR2 --> CI
    MR3 --> CI
    MR4 --> CI
    CI --> Deploy[Staging 部署驗證]
    Deploy --> Prod[正式環境分批上線]
```

## 18.2 Spring Boot 2 → 3 / Java 8 → 21 實戰流程

**步驟 1：建立 Epic 與盤點 Issue**

```bash
glab api projects/:id/epics --method POST --field "title=Spring Boot 2 -> 3 與 Java 8 -> 21 升級"

glab issue create --title "盤點所有相依套件的 Jakarta EE 相容性" \
  --label "upgrade,spring-boot3" --milestone "2026-Q3"
```

**步驟 2：請 AI Agent 協助盤點與批次修改**

```text
請掃描整個專案，列出所有使用 javax.* 命名空間的 import，
分類哪些套件已有對應的 jakarta.* 版本可直接替換，
哪些套件尚無 Spring Boot 3 相容版本需要找替代方案。
```

```bash
# AI Agent 協助批次替換後建立 MR
git checkout -b upgrade/jakarta-namespace-migration
# ... 批次替換 javax.persistence -> jakarta.persistence 等 ...
git commit -am "refactor: 遷移 javax.* 命名空間至 jakarta.*（Spring Boot 3 前置作業）"
glab mr create --title "refactor: Jakarta 命名空間遷移" --target-branch upgrade/spring-boot-3 --fill
```

**步驟 3：CI/CD 雙軌驗證（升級分支與主分支並行）**

```yaml
test-on-java21:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn -B test
  rules:
    - if: '$CI_COMMIT_BRANCH == "upgrade/spring-boot-3"'

test-on-java8-baseline:
  stage: test
  image: maven:3.9-eclipse-temurin-8
  script:
    - mvn -B test
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

**步驟 4：分批上線（Canary/Feature Flag）**

```yaml
deploy-canary:
  stage: deploy
  script:
    - kubectl set image deployment/order-service-canary order-service="$IMAGE_TAG" -n production
    - kubectl scale deployment/order-service-canary --replicas=1 -n production
  environment:
    name: production-canary
  when: manual
  rules:
    - if: '$CI_COMMIT_TAG'
```

## 18.3 Vue2 → Vue3 升級實戰流程

```text
請分析 src/components 目錄下所有 Vue2 Options API 元件，
標示出哪些元件大量使用 this.$refs、Mixins、Filters（Vue3 移除/變更的特性），
並依複雜度排序，產出遷移優先順序建議。
```

```bash
glab issue create --title "Vue3 遷移：移除 Filters 改用 Computed/Methods" \
  --label "upgrade,vue3" --milestone "2026-Q3"

# 逐元件遷移，搭配 Stacked MR（見第五章 5.12 glab stack）拆解大型遷移
glab stack create migrate-order-list-component
glab stack create migrate-order-detail-component --parent migrate-order-list-component
```

CI/CD 中可並行跑 Vue2/Vue3 建置驗證遷移過程未破壞既有功能：

```yaml
build-vue3-migration:
  stage: build
  script:
    - npm run build
  rules:
    - if: '$CI_COMMIT_BRANCH =~ /^migrate-.*-component$/'
```

## 18.4 Angular 升級實戰流程

Angular 官方提供 `ng update` 逐版升級機制，搭配 GitLab CI/CD 可建立自動化升級驗證流程：

```bash
npx @angular/cli update @angular/core@17 @angular/cli@17
```

```yaml
angular-upgrade-validation:
  stage: test
  image: node:22
  script:
    - npm ci
    - npx ng build --configuration production
    - npx ng test --watch=false --browsers=ChromeHeadless
  rules:
    - if: '$CI_COMMIT_BRANCH =~ /^upgrade-angular-.*/'
```

## 18.5 升級專案的企業治理建議

1. **使用 Epic + Roadmap 呈現跨季度時程**，讓管理層與其他團隊清楚掌握升級進度，避免升級工作淹沒在一般功能開發的 Backlog 中。
2. **拆解為小型、可獨立驗證的 MR**，搭配 `glab stack` 管理相依關係，避免單一巨型 MR 難以審查。
3. **CI/CD 雙軌並行驗證**：升級分支與主分支的 Pipeline 同時跑，確保升級過程不影響既有版本的穩定發布。
4. **分批上線降低風險**：搭配 Canary Deployment 或 Feature Flag，先讓小比例流量驗證新版本穩定後，才全面切換。
5. **善用 AI Agent 加速重複性遷移工作**（如命名空間批次替換、Options API → Composition API 轉換樣板程式碼），但**關鍵業務邏輯變更仍需人工審查**，不應全權交由 AI 自動合併。

> 💡 **實務案例**：某零售集團的 Spring Boot 2→3 升級專案橫跨 14 個微服務、3 個團隊，透過單一 Epic 與 Roadmap 呈現整體時程，每個微服務各自建立 Issue 與獨立升級分支，CI/CD 雙軌驗證確保升級過程不影響日常發版。AI Agent 協助完成約 60% 的命名空間遷移與設定檔調整等重複性工作，團隊得以將人力集中在驗證業務邏輯正確性，整體專案時程較原預估縮短約三分之一。

### ✅ 第十八章 Checklist

- [ ] 已建立 Epic 與 Roadmap，呈現升級專案的跨季度時程
- [ ] 升級工作已拆解為可獨立驗證的小型 Issue/MR，避免巨型 MR
- [ ] CI/CD 已設定升級分支與主分支雙軌並行驗證
- [ ] 已規劃 Canary/Feature Flag 分批上線策略，降低正式環境風險
- [ ] AI Agent 已用於加速重複性遷移工作，但關鍵業務邏輯變更仍經人工審查

---

# 第十九章 大型企業 DevSecOps 平台設計

## 19.1 依規模分級的架構設計原則

| 開發者規模 | 架構建議 | Group 策略 |
|---|---|---|
| 100+ | 單一 GitLab Self-Managed 叢集（中型 Reference Architecture），可由 2-3 人 Platform 團隊維運 | 依「部門」分 Top-level Group，專案掛在部門 Group 下 |
| 500+ | 拆分獨立的 PostgreSQL/Redis/Gitaly Cluster，Runner 採用 Kubernetes 動態擴縮，建立專責 Platform Engineering 團隊（5-8人） | 依「事業群 → 部門 → 產品線」三層 Group 結構，搭配 Compliance Framework 套用到特定 Group |
| 1000+ | 評估 GitLab Dedicated 或多地域 Geo 部署，建立 SRE + Platform + Security 三個專責團隊，制定平台 SLA | 四層以上 Group 結構，搭配 SAML/SCIM 自動化人員權限同步，集中式 Policy as Code 治理 |

## 19.2 大型企業架構圖

```mermaid
flowchart TB
    subgraph IdP["身分治理"]
        SSO[企業 SSO / SAML]
        SCIM[SCIM 自動化人員同步]
    end

    subgraph GitLabCluster["GitLab Self-Managed / Dedicated"]
        LB[Load Balancer]
        WebN[Web/API 節點 x N]
        SidekiqN[Sidekiq 節點 x N]
        GitalyCluster[Gitaly Cluster + Praefect]
        PG[(PostgreSQL HA\nPatroni/RDS)]
        RedisCluster[(Redis Cluster)]
        ObjStore[(Object Storage)]
    end

    subgraph RunnerFleet["Runner 叢集"]
        K8sRunners[Kubernetes Runner\nAutoscaling]
    end

    subgraph Observability["可觀測性"]
        Prom[Prometheus]
        Graf[Grafana]
        LogStack[ELK/OpenSearch]
    end

    SSO --> WebN
    SCIM --> WebN
    LB --> WebN
    WebN --> PG
    WebN --> RedisCluster
    WebN --> GitalyCluster
    SidekiqN --> RedisCluster
    SidekiqN --> ObjStore
    WebN -- 觸發 --> K8sRunners
    WebN --> Prom
    SidekiqN --> Prom
    Prom --> Graf
    WebN --> LogStack
```

## 19.3 權限模型設計

```mermaid
flowchart TB
    TopGroup[Top-level Group: ACME Corp]
    TopGroup --> BU1[事業群 A]
    TopGroup --> BU2[事業群 B]
    BU1 --> Dept1[部門: 核心系統]
    BU1 --> Dept2[部門: 數位通路]
    Dept1 --> Proj1[Project: order-service]
    Dept1 --> Proj2[Project: payment-service]
    Dept2 --> Proj3[Project: mobile-app]
```

GitLab 角色（Role）由低到高：**Guest → Reporter → Developer → Maintainer → Owner**，企業設計權限模型時應掌握：

- **權限繼承**：上層 Group 的角色會繼承到所有子 Group/Project，治理時優先在較高層級設定通用規則，個別專案再依需求微調（不可低於繼承的最低要求）。
- **最小權限原則**：一般開發者預設 Developer（可推送非保護分支、建立 MR），Maintainer 角色（可管理 Protected Branch、CI/CD Variables、合併到 main）僅授予 Tech Lead/架構師。
- **Service Account 分離**：自動化使用的 Bot 帳號（CI/CD 自動建立 MR、部署機器人）應使用獨立的 Service Account 或 Group/Project Access Token，與真人帳號權限分離，方便稽核與快速撤銷。

## 19.4 Group 策略與 Project 策略

**Group 策略**：

1. 依組織架構建立 Top-level Group（如事業群），避免所有專案散落在扁平結構或個人 Namespace。
2. 共用資源（CI/CD 範本、Runner、Package Registry 共用套件）統一放在 `platform` Group 下，供其他 Group `include`/依賴。
3. 使用 **Compliance Framework** 將特定法規要求（如需雙重審核、強制安全掃描）套用到金融/醫療相關的 Group，而非逐專案手動設定。

**Project 策略**：

1. 命名規範統一（見第二十一章），避免 `order-service`、`OrderService`、`order_service` 混雜。
2. 每個 Project 必須設定 Owner（通常是 Tech Lead），明確權責歸屬。
3. 模板化新專案建立流程（透過 Project Templates 或 `glab repo create` 搭配標準化的 `.gitlab-ci.yml`、`CODEOWNERS`、Issue Template）。

## 19.5 Branch 策略

```yaml
# 透過 API 設定 Protected Branch（亦可用 Compliance Framework 統一套用）
# glab api projects/:id/protected_branches --method POST \
#   --field "name=main" \
#   --field "push_access_level=0" \
#   --field "merge_access_level=40" \
#   --field "allow_force_push=false"
```

| 分支 | Push 權限 | Merge 權限 | 用途 |
|---|---|---|---|
| `main` | 禁止直接 push（0） | Maintainer（40） | 永遠可部署的穩定分支 |
| `release/*` | 禁止直接 push | Maintainer | 版本維護分支 |
| `feature/*` | Developer 可 push | Developer | 一般開發分支，無需保護 |

> 💡 **企業導入建議**：1000+ 規模企業建議將「Protected Branch 規則」「Approval Rules」「安全掃描必跑」等治理項目，透過 **Compliance Framework** 集中定義後套用到整個 Group，而非要求每個專案團隊各自設定（容易遺漏或設定不一致）。Platform/Security 團隊應定期稽核（透過 Audit Events API）確認治理規則未被個別專案繞過。

> ⚠️ **注意事項**：大型企業常見的失敗模式是「治理規則訂得很完整，但散落在文件中沒有強制執行」。務必將規則轉化為**可被系統強制的設定**（Protected Branch、Compliance Framework、CI/CD 範本中的必跑 Job），而非僅依賴開發者自律遵守書面規範。

### ✅ 第十九章 Checklist

- [ ] 已依開發者規模（100+/500+/1000+）選定對應的架構與團隊配置
- [ ] 已建立符合組織架構的多層 Group 結構，共用資源集中於 Platform Group
- [ ] 已套用最小權限原則，Service Account 與真人帳號權限分離
- [ ] 已用 Compliance Framework 集中治理跨專案的安全與審核規則
- [ ] 已建立 Audit Events 稽核機制，定期確認治理規則未被繞過

---

# 第二十章 GitLab 維運手冊

## 20.1 備份與還原

```bash
# 完整備份（含資料庫、Git 資料、CI/CD Artifacts、Registry）
sudo gitlab-backup create BACKUP=manual_$(date +%Y%m%d)

# 備份設定檔（gitlab-secrets.json 與 gitlab.rb，務必與資料備份分開存放）
sudo cp /etc/gitlab/gitlab-secrets.json /etc/gitlab/gitlab.rb /backup/config/

# 還原（還原前需先安裝相同版本的 GitLab）
sudo gitlab-ctl stop puma
sudo gitlab-ctl stop sidekiq
sudo gitlab-backup restore BACKUP=manual_20260615
sudo gitlab-ctl restart
sudo gitlab-rake gitlab:check SANITIZE=true
```

> ⚠️ **注意事項**：`gitlab-secrets.json` 遺失將導致備份的加密資料（如 CI/CD Variables、2FA 密鑰）**無法解密還原**，務必將設定檔與資料備份分開保存於不同的儲存位置，且兩者都要納入定期備份驗證演練。

## 20.2 監控（Prometheus + Grafana）

GitLab Linux package 內建 Prometheus 與多種 Exporter（`node_exporter`、`postgres_exporter`、`redis_exporter`、`gitlab-exporter`），預設即收集核心指標：

```ruby
# /etc/gitlab/gitlab.rb
prometheus['enable'] = true
grafana['enable'] = true
grafana['admin_password'] = 'changeme-strong-password'
```

關鍵監控指標：

| 指標 | 告警閾值建議 | 意義 |
|---|---|---|
| `sidekiq_queue_duration_seconds` | > 60 秒 | Sidekiq Job 排隊過久，可能影響 MR 合併/通知延遲 |
| `gitlab_database_connection_pool_busy` | > 90% | PostgreSQL 連線池接近耗盡 |
| `gitaly_service_client_requests_total`（錯誤率） | 錯誤率 > 1% | Gitaly 層級異常，影響 Git 操作 |
| CI/CD Job 排隊時間 | > 5 分鐘 | Runner 容量不足 |
| Object Storage 用量增長率 | 月增 > 20% | 需檢查 Cleanup Policy 是否生效 |

## 20.3 Logging

```bash
# 主要日誌位置
/var/log/gitlab/gitlab-rails/production.log   # Web/API 應用日誌
/var/log/gitlab/gitlab-rails/sidekiq/         # 背景任務日誌
/var/log/gitlab/gitaly/                       # Git 操作日誌
/var/log/gitlab/nginx/                        # 存取與錯誤日誌

# 即時追蹤所有元件日誌
sudo gitlab-ctl tail
```

建議將上述日誌統一收集至 ELK/OpenSearch（見團隊另一份《ELK-Stack教學手冊》），並針對異常登入、權限變更、大量 API 失敗等事件建立告警規則。

## 20.4 升級

```bash
# 升級前務必先查閱官方 Upgrade Path（跨多版本升級需依序執行，不可跳版）
sudo apt update
sudo apt-get install gitlab-ee=17.5.0-ee.0

# 升級後驗證
sudo gitlab-ctl reconfigure
sudo gitlab-rake gitlab:check SANITIZE=true
sudo gitlab-rake db:migrate:status
```

> 💡 **最佳實務**：正式環境升級前，務必先在與生產環境規格一致的 Staging 環境完整演練一次升級流程，並確認備份與還原機制可正常運作。大版本升級（如 16.x → 17.x）建議參考官方 Upgrade Path 工具確認所需的中繼版本，避免跳版升級導致資料庫遷移失敗。

## 20.5 高可用性（HA）與災難復原（DR）

```mermaid
flowchart TB
    subgraph RegionA["主要區域 Region A"]
        WebA[Web/API 節點]
        PGPrimary[(PostgreSQL Primary)]
        GitalyA[Gitaly Cluster]
    end
    subgraph RegionB["備援區域 Region B（GitLab Geo Secondary）"]
        WebB[Web 節點\n唯讀]
        PGReplica[(PostgreSQL Replica)]
        GitalyB[Gitaly Cluster 複本]
    end

    PGPrimary -- 串流複寫 --> PGReplica
    GitalyA -- Geo 複寫 --> GitalyB
    WebA -. 故障時人工/自動 Failover .-> WebB
```

- **HA（同區域內）**：Web/Sidekiq 節點水平擴展 + PostgreSQL Patroni 自動容錯切換 + Gitaly Cluster（Replication Factor 3）+ Praefect 自動偵測節點故障。
- **DR（跨區域）**：採用 **GitLab Geo**，在異地建立唯讀 Secondary 站點，主站故障時可手動或自動將 Secondary 提升為 Primary，將 RTO（復原時間目標）控制在可接受範圍內。
- 定期執行 **DR 演練**（非僅紙上計畫），驗證 Failover 流程、資料一致性與回復時間是否符合企業 SLA 要求。

> ⚠️ **注意事項**：許多企業設置了 HA/DR 架構卻從未實際演練過 Failover，直到真正故障才發現流程文件過時或自動化腳本失效。建議至少每半年執行一次完整 DR 演練，並將演練結果（實際 RTO/RPO）回報給管理層。

### ✅ 第二十章 Checklist

- [ ] 已建立每日自動備份，並將資料備份與 `gitlab-secrets.json`/`gitlab.rb` 分開存放
- [ ] 已定期執行還原演練，驗證備份檔案實際可用
- [ ] 已設定 Prometheus + Grafana 監控核心指標並建立告警規則
- [ ] 已將日誌集中收集，並針對異常事件設定告警
- [ ] 升級前已在 Staging 環境完整演練，並依官方 Upgrade Path 操作
- [ ] 已規劃並至少演練過一次 HA Failover 與 DR 流程

---

# 第二十一章 GitLab 最佳實務

## 21.1 命名規範

| 項目 | 規範建議 | 範例 |
|---|---|---|
| Group 名稱 | 全小寫、依組織架構分層 | `acme-corp/core-systems` |
| Project 名稱 | kebab-case，名詞+服務性質 | `order-service`、`payment-gateway` |
| 分支名稱 | `<類型>/<簡述>`，類型對應 Conventional Commits | `feature/order-refund`、`fix/login-redirect-bug`、`release/2.3.0` |
| Commit Message | Conventional Commits 格式 | `feat: 新增訂單退款 API`、`fix: 修正登入重導向錯誤` |
| Tag/版本號 | SemVer（語意化版本） | `v2.3.0`、`v3.0.0-rc.1` |
| CI/CD Variable | 全大寫、Snake Case | `DEPLOY_TOKEN`、`DATABASE_URL` |

## 21.2 Branch Strategy

- 優先採用 **GitLab Flow**（見第六章），依專案性質選 Environment Branch 或 Release Branch 模式。
- `main` 永遠保持可部署狀態，禁止直接 push，僅能透過已通過 Pipeline 與審核的 MR 合併。
- Feature 分支生命週期應盡量短（建議 < 3 天），降低與主線分歐的衝突風險；長期功能開發改用 Feature Flag 控制可見性，而非長期維護獨立分支。

## 21.3 MR Strategy

- MR 標題遵循 Conventional Commits 格式，描述需包含「問題」「修改」「測試」三段式結構（見第十四章 CLAUDE.md 範例）。
- 設定 **Approval Rules**：至少 1 位 Code Owner 核准；涉及安全敏感模組（如金流、權限）需額外指定安全團隊核准。
- 善用 `Closes #123` 語法自動關聯並關閉 Issue；大型變更使用 `glab stack` 拆解為多個易審查的小型 MR。
- 合併策略統一採用 **Squash and Merge**，保持 `main` 分支歷史簡潁，同時 MR 內保留完整開發歷程供日後追溯。

## 21.4 Pipeline Strategy

- 安全掃描、品質門檻等治理規則統一放在 Platform 團隊維護的共用 `ci-templates`，各專案 `include` 引用（見第七章 7.6）。
- 依 `rules` 精確控制 Job 觸發條件，避免每次 push 都跑完整 Pipeline（如僅變更文件時跳過建置/部署 Job）。
- 正式環境部署一律 `when: manual` + Protected Environment，留下明確的人工核准軌跡。
- 善用 Cache 加速重複建置，但 Cache Key 務必依賴實際內容（如 lockfile hash）而非固定字串，避免 Cache 失真。

## 21.5 Release Strategy

- 版本號採用 SemVer，搭配 `glab release create` 自動化發布流程，確保 Release Note 與實際合併內容一致。
- 正式發版前先在 Staging 完整驗收，搭配 Image Promotion（第九章 9.4）確保部署到生產環境的 Image 與驗收版本完全一致，不重新建置。
- 高風險發版（大版本/重大架構變更）採用 Canary 或 Blue-Green 部署，先驗證小流量後才全量切換。

## 21.6 Security Strategy

- 安全掃描三件套（SAST/Secret Detection/Dependency Scanning）為所有專案的強制基線，透過 Compliance Framework 統一套用，不可由個別專案關閉。
- Critical/High 漏洞設定明確 SLA 並追蹤逾期項目，定期於 Security Dashboard review。
- 機密一律透過 CI/CD Variables（Masked + Protected）或外部 Secret 管理工具（Vault）注入，禁止寫死於程式碼或設定檔。
- AI Agent 的寫入類操作（建立 MR、留言）可逐步開放，但合併、刪除、權限變更等高風險操作仍須人工核准（見第十四、十六章）。

> 💡 **實務案例**：某集團將上述六大策略整理為單一《GitLab 開發規範》內部文件，新進工程師到職第一週即依此規範完成第一個 MR 提交，相較過去依賴口頭傳承規範、新人平均 3 週才能掌握完整流程，導入規範文件後縮短至 5 個工作日。

### ✅ 第二十一章 Checklist

- [ ] 已制定並落實命名規範（Group/Project/分支/Commit/Tag/Variable）
- [ ] Branch/MR/Pipeline/Release/Security 六大策略已文件化並納入新人 Onboarding
- [ ] 治理規則已盡可能轉化為系統強制（Protected Branch、Compliance Framework），非僅依賴自律
- [ ] 已定期檢視並更新最佳實務文件，反映平台版本與團隊規模的變化

---

# 第二十二章 常見問題 FAQ

## 22.1 開發類

**Q1. GitLab CE 和 EE 程式碼是同一套嗎？升級會很麻煩嗎？**
是。官方 Linux package/Docker Image 內建即為 EE 程式碼，未授權時功能等同 CE，貼上授權金鑰即可解鎖 EE 功能，無需重新安裝。

**Q2. 一個 GitLab Project 可以對應多個 Git Repository 嗎？**
不可以，一個 Project 對應一個 Git Repository（但可透過 Submodule 或 Monorepo 方式整合多個程式碼來源）。

**Q3. Monorepo 與多個小型 Repository，GitLab 比較適合哪種？**
兩者皆支援。Monorepo 適合高度相依的多模組系統（搭配 `rules: changes` 只跑受影響模組的 Pipeline）；多 Repo 適合獨立部署生命週期的微服務。

**Q4. 如何防止敏感檔案（如 `.env`）被誤提交？**
搭配 `.gitignore` 排除，並啟用 Secret Detection 與 Secret Push Protection（第十一章 11.6）在伺服器端即時阻擋。

**Q5. Fork 與 Branch 有什麼差異，企業內部協作該用哪個？**
Fork 建立獨立的專案複本，適合外部貢獻者或無寫入權限者；企業內部團隊協作建議直接在同一專案內開分支，權限管理更簡單。

**Q6. 如何在 GitLab 管理 Code Owners？**
於專案根目錄建立 `CODEOWNERS` 檔案，指定特定路徑變更需特定人員/群組核准。

**Q7. MR 與 Issue 的關聯如何自動化？**
在 Commit Message 或 MR 描述使用 `Closes #123`、`Relates to #456` 等關鍵字語法。

**Q8. 如何避免大型二進位檔案塞爆 Repository？**
使用 Git LFS（Large File Storage）管理大型檔案，或改用第十章 Generic Package 儲存。

**Q9. GitLab 支援 Code Review 的 Suggested Change（建議修改）嗎？**
支援，Reviewer 可在 Diff 行內提出具體修改建議，作者可一鍵套用。

**Q10. 如何在多個專案間共用 CI/CD 設定？**
透過 `include: project:` 引用集中維護的共用範本（第七章 7.6）。

**Q11. GitLab 是否支援 Trunk-Based Development？**
支援，搭配短生命週期 Feature 分支 + Feature Flag，即為 GitLab Flow 的精簡變體。

**Q12. 如何處理跨團隊的大型 Monorepo 程式碼衝突？**
搭配 `glab stack`（Stacked MR）拆解變更、善用 `CODEOWNERS` 明確權責、並考慮以 `rules: changes` 限縮各團隊 CI 範疇降低互相干擾。

**Q13. Wiki 功能適合用來放什麼內容？**
適合放置不需要版本審核流程的輕量說明文件；正式架構文件/規範建議仍放在 Repository 內以 MR 流程維護，確保歷史可追溯。

**Q14. GitLab 的 Snippet 功能用途是什麼？**
用於分享小段程式碼或設定範例，支援版本控制與留言討論，適合團隊內部知識分享。

## 22.2 CI/CD 類

**Q15. Pipeline 一直卡在 `pending` 怎麼辦？**
通常是 Job 的 `tags` 與可用 Runner 的 tags 不匹配，或無可用 Runner，檢查 Runner 設定與 Job 定義。

**Q16. `rules` 與舊版的 `only`/`except` 有什麼差異？**
`rules` 是新版、更具彈性的條件控制語法，官方建議統一改用 `rules`，`only`/`except` 已不建議於新專案使用。

**Q17. 如何讓 Pipeline 只在特定檔案變更時觸發？**
使用 `rules: changes:` 指定路徑模式，僅當符合的檔案有變更才觸發該 Job。

**Q18. Cache 設定了卻沒有生效？**
檢查 `cache.key` 是否每次執行都不同（如使用了動態時間戳），應改用依檔案內容雜湊的 Key（如 `files: [package-lock.json]`）。

**Q19. 如何在多個 Job 之間傳遞檔案？**
使用 `artifacts` 定義產出路徑，下游 Job 會自動下載上游 Job 的 Artifacts（同一 Pipeline 內）。

**Q20. `needs` 關鍵字的作用是什麼？**
用於定義 Job 之間的相依關係，讓 Job 可跳脫預設的 Stage 順序限制，以 DAG（有向無環圖）方式平行執行，加速整體 Pipeline。

**Q21. 如何手動觸發特定條件下才執行的 Job？**
設定 `when: manual`，Job 會出現在 Pipeline 圖中等待人工點擊執行。

**Q22. Child Pipeline 與 Parent Pipeline 是什麼？**
透過 `trigger:` 關鍵字，可從一個 Pipeline 動態觸發另一個獨立的子 Pipeline，適合 Monorepo 中依模組拆分獨立的 CI 設定。

**Q23. 如何除錯 Pipeline YAML 語法錯誤？**
使用 GitLab 後台「CI/CD → Editor」的 Lint 功能，或執行 `glab ci lint` 提前驗證語法。

**Q24. Pipeline 執行很慢，如何優化？**
善用 Cache、平行化（`needs`/拆分 Job）、僅在必要時跑完整測試（`rules: changes`）、選用更貼近原生環境的輕量 Image。

**Q25. 如何設定 Pipeline 的逾時時間？**
專案層級可設定全域 Timeout（CI/CD Settings），個別 Job 可用 `timeout:` 關鍵字覆寫。

**Q26. Scheduled Pipeline 與一般 Pipeline 有什麼差異？**
Scheduled Pipeline 透過 Cron 表達式定期自動觸發（如每日 Nightly Build），可用 `glab schedule` 管理（第五章 5.14）。

**Q27. 如何避免 Pipeline 中洩漏機密到 Job Log？**
機密一律設為 Masked Variable（Log 中自動遮蔽），且避免在 `script` 中用 `echo` 直接印出機密內容。

**Q28. Merge Train 是什麼，何時該用？**
Merge Train 讓多個 MR 依序排隊合併並逐一驗證，避免多個 MR 同時合併造成 `main` 分支被破壞，適合高頻合併的大型團隊。

## 22.3 Security 類

**Q29. SAST 掃描沒有發現任何問題，代表程式碼絕對安全嗎？**
不代表。SAST 僅能偵測特定模式的已知問題類型，仍需搭配人工 Code Review、DAST、滲透測試等多層防禦。

**Q30. Dependency Scanning 與 Container Scanning 的差異？**
Dependency Scanning 掃描應用程式相依套件（如 `pom.xml`）；Container Scanning 掃描容器映像中作業系統層的套件漏洞，兩者互補。

**Q31. 誤判（False Positive）的漏洞該如何處理？**
在 Vulnerability Management 中標記為 `Dismissed` 並記錄理由，避免每次掃描重複出現干擾真正需要處理的項目。

**Q32. License Compliance 可以自動阻擋特定授權的套件嗎？**
可以，設定 License Approval Policy，禁止引入特定授權類型（如 GPL 系列）的套件，未通過會阻擋 MR 合併。

**Q33. Secret Push Protection 與 Secret Detection（CI 掃描）有何不同？**
Push Protection 在 `git push` 當下即時阻擋含機密的提交（事前防範）；Secret Detection 是 Pipeline 中事後掃描已提交的程式碼。

**Q34. 如何處理第三方相依套件已停止維護（EOL）但專案仍依賴的情況？**
建立 Issue 追蹤，評估替代方案或自行 Fork 維護，並在 Dependency Scanning 中暫時標記風險等級與處理計畫。

**Q35. DAST 掃描會不會把測試環境弄壞？**
有可能，Full Scan 會主動發送測試攻擊請求，務必僅對獨立的測試/Staging 環境執行，並評估是否需要搭配測試資料隔離。

**Q36. Compliance Framework 與 Protected Branch 的關係？**
Compliance Framework 可批次將一組規則（含 Protected Branch、Approval Rules、必跑安全掃描）套用到符合條件的多個專案，簡化大規模治理。

**Q37. 如何稽核「誰核准了哪個 MR」？**
透過 Audit Events（Group/Instance 層級）或 API 查詢 MR 的 Approval 紀錄，企業合規稽核常用此功能。

**Q38. CI Job Token 的權限範圍可以限縮嗎？**
可以，透過「CI/CD → Token Access」設定允許存取的目標專案範圍，避免 Job Token 被用於存取無關專案。

**Q39. 如何防止 Fork 的 MR 被惡意利用以竊取 Secret Variable？**
GitLab 預設不會將 Protected Variable 傳遞給來自 Fork 的 Pipeline，務必勿手動關閉此保護設定。

**Q40. Vulnerability Management 的 SLA 該如何訂定？**
通常依嚴重程度分級，如 Critical 7 天、High 30 天、Medium 90 天，並透過 Dashboard 追蹤逾期項目作為團隊 KPI 之一。

**Q41. 如何將 GitLab 漏洞資訊匯出給外部稽核系統？**
透過 GraphQL API 查詢 `vulnerabilities`，或使用 Security Dashboard 的匯出功能產生報表。

## 22.4 Runner 類

**Q42. Shared Runner 與 Project Runner 可以同時使用嗎？**
可以，GitLab 會依 Job 的 `tags` 與設定自動選擇符合條件的 Runner，兩者並存很常見。

**Q43. Runner Registration Token 與 Runner Authentication Token 有何差異？**
新版 GitLab 改用 Runner Authentication Token（於後台先建立 Runner 再取得 Token），取代舊版的 Registration Token，安全性更高且可追蹤個別 Runner 身份。

**Q44. Kubernetes Executor 的 Job Pod 為何一直 `Pending`？**
常見原因是 Namespace 資源配額不足或無法 Pull Image，使用 `kubectl describe pod` 確認具體原因。

**Q45. 如何讓特定 Job 只在擁有 GPU 的 Runner 上執行？**
為該 Runner 設定特殊 `tags`（如 `gpu`），並在 Job 的 `tags:` 中指定相同標籤。

**Q46. Runner 的 `concurrent` 設多少比較合適？**
依主機 CPU/Memory 容量與單個 Job 平均資源用量估算，並持續觀察 Job 排隊時間動態調整，沒有萬用的固定值。

**Q47. Docker Executor 與 Docker-in-Docker（dind）的差異？**
Docker Executor 是 Runner 本身的執行模式；dind 是當 Job 內需要「在容器裡執行 docker build」時的服務（`services: [docker:dind]`），兩者可同時搭配使用。

**Q48. 如何讓 Runner 自動依負載擴縮？**
Kubernetes Runner 搭配 Cluster Autoscaler，依 Pending Pod 數量自動增減節點；亦可使用 GitLab 的 Runner Autoscaler（搭配雲端 VM Fleet）。

**Q49. Shell Executor 有什麼安全風險？**
Job 直接在主機 Shell 執行，缺乏容器隔離，惡意或有問題的 Script 可能影響主機本身，僅建議在高度信任的內部環境使用。

**Q50. 如何排查「Runner 顯示 Online 但 Job 卻沒被接走」？**
檢查 Runner 的 `tags` 設定、是否啟用 `run_untagged`、以及該 Runner 是否被限制只服務特定 Project/Group。

**Q51. 多個 Runner 同時註冊在同一台主機是否合理？**
合理，常見於需要不同 Executor 或不同資源限制設定（如獨立的高記憶體 Runner）的情境，依 `config.toml` 中的多個 `[[runners]]` 區塊設定。

**Q52. Runner 升級後 Job 突然大量失敗？**
檢查是否有 Breaking Change（如預設 Image 行為變更），建議升級前先在非正式環境的 Runner 驗證，且 Runner 版本與 GitLab Server 版本需符合官方相容性矩陣。

**Q53. 如何監控 Runner 的健康狀態？**
啟用 Runner 的 Prometheus Metrics（`[[runners]] listen_address`），並整合進現有的 Prometheus/Grafana 監控（第二十章）。

**Q54. Windows Runner 是否支援？**
支援，可用於需要 .NET Framework 或 Windows 特定建置環境的專案，安裝方式與 Linux 類似但需另外設定 PowerShell Executor。

## 22.5 Kubernetes 類

**Q55. GitLab Agent for Kubernetes 與傳統的 `kubectl` 部署有何不同？**
Agent 採用 Pull-based 架構（叢集主動向 GitLab 拉取設定），不需要將叢集的 API Server 對外開放給 GitLab 存取，安全性更高，更符合 GitOps 理念。

**Q56. 如何在 CI/CD 中安全地部署到 Kubernetes？**
透過 GitLab Agent 取得授權的 `kubecontext`，避免在 CI/CD Variables 中直接存放完整的 kubeconfig 或長期有效的叢集管理員憑證。

**Q57. GitOps 與傳統 CI/CD 部署的差異？**
GitOps 以 Git Repository 中宣告的期望狀態為唯一真實來源，由 Agent 持續比對並同步叢集實際狀態；傳統部署則是 CI/CD Job 主動執行 `kubectl apply` 推送變更。

**Q58. 一個 GitLab Agent 可以管理多個 Namespace 嗎？**
可以，依 Agent 設定檔（`config.yaml`）中的授權範圍，可管理單一或多個 Namespace，甚至整個叢集。

**Q59. 如何在多環境（dev/staging/production）部署不同設定？**
搭配 Helm Values 檔案分環境管理，或使用 Kustomize Overlay，CI/CD 依 `environment:` 對應不同的設定檔。

**Q60. Kubernetes 部署失敗時如何快速回滾？**
搭配 Helm 的 `helm rollback`，或在部署 Job 中保留前一版本的 Release Revision 供快速還原。

**Q61. 如何在 GitLab 中查看 Kubernetes 部署狀態？**
透過 Environment 頁面整合的 Kubernetes Dashboard（需 Agent 連接），可直接查看 Pod 狀態、Log，無需另外切換到 `kubectl` 或 K8s 原生 Dashboard。

**Q62. Canary Deployment 在 GitLab 中如何實現？**
透過 `environment` 區分 Canary 與正式環境，CI/CD Job 分別控制兩者的副本數與流量比例（可搭配 Service Mesh 如 Istio 做更細緻的流量切分）。

**Q63. 如何避免 CI/CD Job 中的 Kubernetes 認證資訊洩漏？**
優先使用 GitLab Agent 的短期授權機制，而非長期靜態 Token；若仍需 Service Account Token，務必設為 Masked + Protected Variable 並定期輪替。

**Q64. Helm Chart 版本管理建議？**
將自訂 Helm Chart 發布為內部 OCI Registry 套件（GitLab Container Registry 支援 OCI 格式），並以 SemVer 管理版本。

**Q65. 部署到 Kubernetes 後如何驗證健康狀態？**
搭配 Liveness/Readiness Probe，並在 CI/CD 部署 Job 後加入驗證步驟（如 `kubectl rollout status`），確認新版本確實健康運行才視為部署成功。

**Q66. 多叢集（Multi-Cluster）管理如何規劃？**
每個叢集註冊獨立的 GitLab Agent，並透過統一的 CI/CD 範本依環境變數動態選擇目標叢集，避免每個叢集各自維護一套部署腳本。

**Q67. Kubernetes 相關的 Secret 該如何與 GitLab CI/CD Variables 整合？**
建議導入 External Secrets Operator 或 Vault，讓叢集內 Secret 由專責密鑰管理系統同步，CI/CD 僅負責觸發部署，不直接持有最終機密內容。

## 22.6 AI 類

**Q68. 導入 AI Agent 自動化操作 GitLab，最大的風險是什麼？**
誤操作（如錯誤合併、刪除分支）與機密洩漏（Prompt 中夾帶敏感資訊傳給外部 AI 服務）。建議搭配唯讀模式試行、權限分級與 Protected Branch 作為防線。

**Q69. AI 產生的程式碼是否需要額外的安全掃描？**
需要。AI 產生的程式碼與人工撰寫的程式碼一視同仁，皆需通過相同的 SAST/Dependency Scanning 與人工審查流程，不應因為「AI 寫的」而放寬標準。

**Q70. 如何評估該導入 AI Agent 自動化哪些工作？**
優先選擇「重複性高、規則明確、風險可控」的工作（如 MR 描述產生、命名空間批次替換、漏洞彙整），高風險的關鍵業務邏輯決策應保留人工主導。

**Q71. AI Agent 的操作紀錄如何稽核？**
AI Agent 透過 `glab`/API/MCP 執行的操作，最終都會記錄在 GitLab 的 Audit Events 與 Commit/MR 歷史中，與真人操作的稽核軌跡一致。

**Q72. 多個 AI 工具（Claude Code、Copilot）同時使用會有衝突嗎？**
若缺乏協調可能造成重複留言、衝突的修改建議。建議透過 `AGENTS.md`/`CLAUDE.md` 統一規範，明確分工。

**Q73. 如何避免 AI Agent 的 Prompt 洩漏公司機密給外部 AI 服務？**
評估是否需要採用企業私有部署的 AI 模型，或在 Prompt/Context 中過濾敏感資訊（如客戶個資、金鑰），並建立員工使用規範。

**Q74. AI 產生的測試案例品質可信嗎？**
具參考價值但仍需人工檢視，特別注意 AI 是否「為了讓測試通過」而寫出與業務邏輯不符的斷言，務必驗證測試確實檢查了正確的業務規則。

**Q75. 企業導入 AI 協作開發，第一步該做什麼？**
建議先選定 1-2 個低風險的試點專案，建立明確的使用規範與稽核機制，蒐集實際效益數據後再逐步擴大導入範圍。

**Q76. AI Agent 是否能完全取代 Code Review？**
不能。AI 審查是輔助工具，能加速發現明顯問題，但對複雜業務邏輯的判斷、架構決策仍需要有經驗的工程師把關。

**Q77. 如何衡量 AI 協作開發帶來的實際效益？**
可追蹤 Lead Time for Changes、Code Review 平均耗時、MR 往返次數等 DevOps 指標，比較導入前後的變化趨勢。

**Q78. AI Agent 操作 GitLab 時，是否需要獨立的帳號？**
建議使用獨立的 Service Account 或 Project/Group Access Token，與真人帳號區隔，方便追蹤是 AI 還是人工進行的操作，亦方便獨立撤銷權限。

**Q79. 如何避免團隊過度依賴 AI 而喪失基礎能力？**
建立教育訓練機制，要求工程師理解 AI 產出的邏輯而非盲目套用，並保留定期的人工架構討論與設計審查環節。

## 22.7 GitLab Duo 類

**Q80. GitLab Duo 需要額外付費嗎？**
依功能與授權方案而定，部分基礎功能含於 Premium/Ultimate 授權，進階 Agent Platform 功能可能需要額外的 Duo 加購方案，請參考當前官方授權頁面。

**Q81. GitLab Duo Chat 能存取私有專案的程式碼嗎？**
能，Chat 會依使用者的權限範圍存取其有權檢視的專案上下文，不會超出該使用者原本的存取權限。

**Q82. Duo Code Suggestions 支援哪些 IDE？**
主流 IDE 如 VS Code、JetBrains 系列、Neovim 等，透過官方 GitLab Workflow 擴充套件安裝。

**Q83. 如何排除特定檔案不被 Duo 用作 Context？**
透過專案的 `.gitlab/duo/` 設定排除規則（如排除自動產生的程式碼、第三方 vendor 目錄）。

**Q84. Duo Code Review 與真人 Reviewer 的建議衝突時該如何取捨？**
真人 Reviewer 的判斷應優先，Duo 的建議僅供參考；若 Duo 的建議有其道理但 Reviewer 不同意，應留下討論記錄，作為團隊知識累積。

**Q85. Vulnerability Explanation 功能是否會給出修復程式碼？**
會，通常提供具體的修復建議與範例程式碼片段，開發者仍需依實際業務情境調整後套用。

**Q86. GitLab Duo Agent Platform 與一般 Duo Chat 的差異？**
傳統 Duo Chat（Non-Agentic）僅針對單一問題給出單輪回覆；Agentic Chat 與 Duo Agent Platform 則可規劃多個步驟、串接 Issue/MR/Pipeline/安全掃描等多項資料來源，並在獲得授權後實際執行動作（如建立 MR、回覆留言），更接近自主 Agent 而非單純問答工具，目前已是正式 GA 功能（詳見第十三章 13.2.1、13.2.2）。

**Q87. 如何訓練團隊有效使用 GitLab Duo？**
建立內部 Prompt 範例庫，分享有效提問方式（見第十三章 13.7），並定期分享實際提升效率的案例鼓勵採用。

**Q88. Duo 產生的 Commit Message/MR 描述準確嗎？**
通常能準確摘要程式碼層級的變更，但對於「為什麼這樣改」的業務脈絡仍建議由開發者補充，避免描述流於表面。

**Q89. Self-Managed 環境可以使用 GitLab Duo 嗎？**
可以，需滿足對應的 GitLab 版本與授權要求，並完成 AI 閘道（AI Gateway）的網路連線設定。

**Q90. Duo 的回答是否會被用於再訓練模型？**
依 GitLab 的資料處理政策而定，企業應於導入前確認資料隱私條款，特別是高合規需求的產業。

**Q91. 如何在 CI/CD Pipeline 中自動呼叫 Duo 功能？**
可透過 `glab duo ask` 搭配 Script 整合進 Pipeline（如自動產生 Release Note 草稿），但涉及人工判斷的審查建議仍應留在 MR 互動流程中。

## 22.8 glab 類

**Q92. `glab` 與 `git` 指令可以混用嗎？**
可以，`glab` 是 `git` 的補充工具，專注於 GitLab 平台層面的操作（MR/Issue/Pipeline），版本控制本身仍使用標準 `git` 指令。

**Q93. 如何讓 CI/CD Job 中使用 `glab` 而不需要互動登入？**
透過環境變數注入 Token 並使用 `glab auth login --stdin`（第四章 4.5），或部分指令支援直接以環境變數 `GITLAB_TOKEN` 運作免登入。

**Q94. `glab` 設定檔內的 Token 加密嗎？**
設定檔以一般檔案權限保護存放於使用者目錄，不是加密格式，務必確保檔案系統權限正確（僅該使用者可讀），並避免提交進版本控制。

**Q95. 如何用 `glab` 一次操作多個 GitLab Instance 的資源？**
搭配 Shell Script 迴圈搭配 `--hostname` 參數切換，或分別針對不同 Instance 撰寫獨立的自動化腳本。

**Q96. `glab mr create --fill` 是什麼意思？**
自動依當前分支的 Commit Message 與分支名稱推斷 MR 標題與描述，省去手動輸入，適合搭配規範良好的 Conventional Commits。

**Q97. `glab` 是否支援 Windows PowerShell 環境？**
支援，`glab` 是跨平台單一執行檔，PowerShell、CMD、Git Bash 皆可直接呼叫。

**Q98. 如何排查 `glab` 指令回應 401/403 錯誤？**
確認 Token 是否過期或權限範圍（Scope）不足，使用 `glab auth status` 檢查目前登入狀態與對應 Instance。

**Q99. `glab api` 呼叫 GraphQL 時如何傳遞變數？**
使用 `-f variableName=value` 搭配 Query 中的 `$variableName` 宣告，或使用 `--field` 傳遞複雜結構（依版本語法略有差異，請查閱 `glab api graphql --help`）。

**Q100. `glab` 的設定可以同步到團隊其他成員嗎？**
設定檔本身（含 Token）不應同步分享；但團隊可共用 Shell Alias/Script（不含個人 Token）統一常用指令的呼叫方式。

**Q101. 如何用 `glab` 快速找出「指派給我且即將逾期」的 Issue？**
`glab issue list --assignee=@me --milestone="<目前 Milestone>"`，再搭配 `--label` 進一步篩選優先級。

**Q102. `glab` 支援自動完成（Shell Completion）嗎？**
支援，可透過 `glab completion bash/zsh/powershell` 產生對應 Shell 的自動完成腳本並載入設定檔。

**Q103. `glab ci lint` 與 GitLab 後台的 CI Lint 工具差異？**
功能相同（驗證 `.gitlab-ci.yml` 語法），`glab ci lint` 讓開發者無需離開終端機即可在提交前驗證，加快回饋速度。

**Q104. 如何用 `glab` 比較兩個分支的差異後再決定是否建立 MR？**
先用標準 `git diff main...feature/xxx` 檢視差異，確認無誤後再用 `glab mr create`，避免建立 MR 後才發現範圍不如預期。

**Q105. 我們還在用 Core 方案，為什麼同事說 Duo Chat 突然不能用了？**
這不是 Bug。Non-Agentic（傳統單輪問答）版本的 Duo Chat 已於 2026-05-21 起，對 Core 方案使用者下線，此政策已生效。若要繼續使用 Duo Chat 能力，需升級至 Pro 或 Ultimate 方案，或改用已 GA 的 Agentic Chat（視方案授權範圍而定，詳見第十三章 13.2.1）。

**Q106. `glab` 裡標示為 Experimental 的指令（如 `mcp`、`stack`、`skills`）可以放進正式 CI/CD Pipeline 嗎？**
不建議。Experimental 代表指令格式與行為可能在後續版本異動或被移除，企業應僅在 PoC、個人開發環境或內部創新專案中使用，且每次升級 `glab` 版本後都要重新驗證是否仍相容（詳見第四章 4.3.1 的穩定度分級表）。

**Q107. GitLab Orbit 是什麼？跟 MCP 有什麼不同？**
Orbit（Knowledge Graph）是 GitLab 在伺服器端建立的跨專案程式碼關聯索引，讓 AI Agent 可以直接查詢「誰呼叫誰、依賴哪些上游服務」等語意層級問題；MCP 則是讓 Agent 用標準化協定呼叫 GitLab 各項功能的「工具呼叫介面」。兩者是互補關係：MCP 負責結構化操作，Orbit 負責補強跨專案的語意上下文，目前皆為 Beta 狀態（詳見第十六章 16.6）。

**Q108. GitLab MCP Server 現在用 stdio 還是 HTTP 比較好？**
官方目前建議優先採用 **HTTP transport**，適合部署為長駐服務供團隊共用；stdio（搭配 `mcp-remote`）仍可用，主要作為個人開發機或舊版設定的相容選項（詳見第十六章 16.2）。

**Q109. Dependency Scanning 為什麼最近開始出現棄用警告？**
舊版以 Gemnasium 引擎為核心的掃描方式已於 GitLab 17.9 起標示為棄用，預計在 20.0 移除，官方建議的掃描方式已轉為以 SBOM/CycloneDX 為基礎。若專案的 `.gitlab-ci.yml` 仍引用舊版範本，應提前規劃遷移（詳見第十一章 11.4）。

> 💡 **使用建議**：以上 FAQ 依「開發、CI/CD、Security、Runner、Kubernetes、AI、GitLab Duo、glab」八大分類整理，共 109 題。建議團隊將此 FAQ 納入新人 Onboarding 文件，並隨著平台版本更新與團隊實際遇到的問題持續擴充。

### ✅ 第二十二章 Checklist

- [ ] 新進團隊成員已閱讀本章 FAQ 並能自行排除常見問題
- [ ] 團隊已建立持續擴充 FAQ 的機制（如每次重大事故後補充對應問答）
- [ ] FAQ 內容已隨 GitLab/glab 版本更新定期校驗是否過時

---

# 第二十三章 附錄

## 23.1 常用 glab 指令速查表

| 情境 | 指令 |
|---|---|
| 登入 | `glab auth login --hostname <host>` |
| 檢查登入狀態 | `glab auth status` |
| Clone 專案 | `glab repo clone <group/project>` |
| 建立 MR | `glab mr create --title "..." --target-branch main --fill` |
| 列出待審 MR | `glab mr list --reviewer-state=review_requested` |
| Checkout MR | `glab mr checkout <id>` |
| 核准並合併 | `glab mr approve <id> && glab mr merge <id> --squash` |
| 建立 Issue | `glab issue create --title "..." --label bug` |
| 查看 Pipeline | `glab pipeline list` / `glab pipeline view <id>` |
| 即時追蹤 Pipeline | `glab pipeline ci view` |
| 重跑失敗 Job | `glab pipeline retry <id>` |
| 建立版本 | `glab release create v1.0.0 --notes "..."` |
| 設定變數 | `glab variable set KEY value --masked --protected` |
| 通用 API 呼叫 | `glab api projects/:id/<endpoint>` |
| 啟動 MCP Server（建議 HTTP transport） | `glab mcp serve --transport http --port 8585` |
| Duo 問答 | `glab duo ask "問題"` |
| 驗證 CI YAML | `glab ci lint` |
| 查詢 Knowledge Graph | `glab orbit remote --query "問題"` |
| 安裝 Agent 技能包 | `glab skills install <skill>` |
| 驗證軟體供應鏈簽署 | `glab attestation verify <image> --signing-key <key>` |
| 管理容器倉庫 | `glab container-registry tag list <repo>` |
| 列出 Incident | `glab incident list --state opened` |

## 23.2 CI/CD 通用範本

```yaml
stages: [build, test, security, package, deploy]

workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_COMMIT_TAG'

include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml

default:
  retry:
    max: 1
    when: runner_system_failure
```

## 23.3 Spring Boot 範本

```yaml
build:
  stage: build
  image: maven:3.9-eclipse-temurin-21
  cache:
    key: maven-$CI_COMMIT_REF_SLUG
    paths: [.m2/repository]
  script:
    - mvn -B package -DskipTests

test:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - mvn -B test
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml

package-image:
  stage: package
  image: docker:27
  services: [docker:27-dind]
  script:
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" .
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

## 23.4 Vue3 範本

```yaml
default:
  image: node:22-alpine
  cache:
    key: { files: [package-lock.json] }
    paths: [node_modules/]

test:
  stage: test
  script: [npm ci, npm run test:unit]

build:
  stage: build
  script: [npm ci, npm run build]
  artifacts:
    paths: [dist/]
```

## 23.5 Kubernetes 範本

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  replicas: 3
  selector:
    matchLabels: { app: order-service }
  template:
    metadata:
      labels: { app: order-service }
    spec:
      containers:
        - name: order-service
          image: registry.example.com/mygroup/order-service:latest
          ports: [{ containerPort: 8080 }]
          resources:
            requests: { cpu: "500m", memory: "512Mi" }
            limits: { cpu: "1", memory: "1Gi" }
          readinessProbe:
            httpGet: { path: /actuator/health/readiness, port: 8080 }
          livenessProbe:
            httpGet: { path: /actuator/health/liveness, port: 8080 }
```

## 23.6 Docker 範本（多階段建置）

```dockerfile
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -B dependency:go-offline
COPY src ./src
RUN mvn -B package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## 23.7 Helm 範本

```yaml
# values.yaml
replicaCount: 3
image:
  repository: registry.example.com/mygroup/order-service
  tag: latest
resources:
  requests: { cpu: 500m, memory: 512Mi }
  limits: { cpu: "1", memory: 1Gi }
service:
  port: 8080
ingress:
  enabled: true
  host: order-service.example.com
```

```bash
helm upgrade --install order-service ./charts/order-service \
  -f values-prod.yaml \
  --set image.tag="$CI_COMMIT_SHORT_SHA" \
  -n production
```

## 23.8 十大 AI Agent 實戰情境總覽

本手冊已於各章節提供完整實戰教學，此處彙整對照表方便快速查找：

| 情境 | 對應章節 |
|---|---|
| 1. Claude Code + GitLab + glab | 第十四章 |
| 2. GitHub Copilot Agent + GitLab + glab | 第十五章 |
| 3. AI Agent 自動建立 Merge Request | 第十四章 14.2 |
| 4. AI Agent 自動 Review 程式碼 | 第十四章 14.3、第十三章 13.4 |
| 5. AI Agent 自動產生 Release Note | 見下方 23.8.1 |
| 6. AI Agent 自動分析 Legacy System | 第十七章 |
| 7. AI Agent 自動產生架構文件 | 見下方 23.8.2 |
| 8. AI Agent 協助 Spring Boot 升級 | 第十八章 18.2 |
| 9. AI Agent 協助 Vue 升級 | 第十八章 18.3 |
| 10. AI Agent 協助大型共用平台開發 | 見下方 23.8.3 |

### 23.8.1 AI Agent 自動產生 Release Note

**情境**：發版前，請 AI Agent 彙整自上一個 Tag 以來所有已合併的 MR，自動產生結構化 Release Note。

```bash
# 取得自上次 Tag 以來的所有 MR（依 Merge Commit 範圍）
glab api projects/:id/merge_requests --field "state=merged" --field "target_branch=main" \
  --paginate | jq -r '.[] | select(.merged_at > "2026-05-01") | .title'
```

請 Claude Code 或 Duo 依下列 Prompt 整理：

```text
請依照下方 MR 標題清單，依 Conventional Commits 類型（feat/fix/refactor/docs）分類，
產生結構化的 Release Note（含「新功能」「修復」「其他變更」三個段落），
並標示每項變更對應的 MR 編號方便追溯。
```

```bash
glab release create v2.4.0 --notes-file ./CHANGELOG-2.4.0.md
```

> 💡 **最佳實務**：搭配 Conventional Commits 規範（第二十一章），AI 產生的 Release Note 分類準確度會大幅提升；若 Commit Message 格式混亂，建議先要求 AI 進行「語意分類」而非單純字串比對。

### 23.8.2 AI Agent 自動產生架構文件

**情境**：請 AI Agent 為現有專案產生並維護架構文件，且隨程式碼演進自動更新。

```text
請分析這個 Spring Boot 專案的套件結構與 Controller/Service/Repository 分層，
產生一份架構文件，包含：
1. 整體分層架構 Mermaid 圖
2. 主要 API 端點清單與對應的 Service 方法
3. 資料庫表與 Entity 對應關係
4. 對外部系統的依賴（如呼叫的第三方 API、訊息佇列）
```

建議將架構文件產生流程納入 CI/CD，於每次合併到 `main` 後自動檢查文件是否需要更新（而非完全自動覆寫，避免遺失人工補充的脈絡說明）：

```yaml
check-architecture-doc:
  stage: deploy
  script:
    - glab duo ask "比較目前 docs/architecture.md 與最新程式碼結構，列出需要更新的差異點" > arch-diff-report.txt
  artifacts:
    paths: [arch-diff-report.txt]
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
  allow_failure: true
```

### 23.8.3 AI Agent 協助大型共用平台開發

**情境**：Platform 團隊開發供多個應用團隊共用的內部平台（如共用元件庫、API Gateway 設定、CI/CD 範本），需確保變更不會破壞既有使用方。

```text
請分析這次對 ci-templates 共用範本的修改，列出目前所有引用（include）此範本的專案清單，
並評估此次變更是否為 Breaking Change，若是，請列出每個受影響專案需要配合調整的項目。
```

```bash
# 搭配 glab search 找出所有引用共用範本的專案
glab search code "ci-templates" --group platform

# 針對每個受影響專案，AI Agent 可批次建立通知 Issue
glab issue create --title "⚠️ ci-templates v3.0.0 升級，需確認相容性" \
  --description "本次升級包含 Breaking Change：... 請於 2026-07-01 前完成驗證。" \
  --label "platform-notice"
```

> 💡 **企業導入建議**：大型共用平台開發應建立「變更影響分析」為標準流程的一部分，AI Agent 可大幅加速「找出誰受影響」與「產生通知內容」的工作，但**版本相容性策略與 Breaking Change 的發布節奏，仍應由 Platform 團隊架構師決策**，AI 僅負責執行與彙整。

## 23.9 企業導入檢查清單

- [ ] 已完成部署形態選型（SaaS / Self-Managed / Dedicated）並評估資料主權與維運人力
- [ ] 已建立多層 Group 結構與最小權限模型，Service Account 與真人帳號分離
- [ ] 已制定命名規範、分支策略、MR 策略並文件化
- [ ] 已建立共用 CI/CD 範本，安全掃描三件套（SAST/Secret Detection/Dependency Scanning）為強制基線
- [ ] 已設定 Protected Branch、Approval Rules，正式環境部署需人工核准
- [ ] 已建立 Container/Package Registry 的 Cleanup Policy 與版本治理規範
- [ ] 已建立備份/還原、監控告警、HA/DR 演練機制
- [ ] 已導入 GitLab Duo / Claude Code / Copilot 等 AI 工具，並建立對應的使用規範與稽核機制
- [ ] 已確認目前訂閱方案是否受 Non-Agentic Duo Chat 退場影響，並完成 GitLab Duo Agent Platform 的導入評估
- [ ] 已評估 GitLab MCP Server（Beta）與 Orbit（Beta）整合，並先以唯讀模式試行
- [ ] 已建立新人 Onboarding 文件（含本手冊 FAQ 與速查表）
- [ ] 已制定 Legacy System 逆向工程與 Framework 升級的標準作業流程
- [ ] 已建立 DevSecOps 平台的長期治理機制（定期稽核、規則更新、團隊培訓）

### ✅ 第二十三章 Checklist

- [ ] 團隊已將本附錄速查表與範本納入內部 Wiki 或 `ci-templates` 共用專案
- [ ] 十大 AI Agent 實戰情境已對應到團隊實際工作流程並至少試行一項
- [ ] 企業導入檢查清單已由 Platform/DevOps/Security 團隊共同確認逐項完成

---

> 📘 **手冊結語**：本手冊涵蓋 GitLab 與 GitLab CLI（glab）從基礎概念到企業級大規模導入的完整知識體系，並深度整合 2026 年最新的 AI 協作開發情境（GitLab Duo、Claude Code、GitHub Copilot、MCP）。建議團隊將本文件作為內部開發規範的基礎，依實際組織狀況調整章節中的命名規範、權限模型與治理流程，並隨 GitLab 版本演進持續更新內容。

