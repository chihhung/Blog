+++
date = '2026-06-24T20:02:18+08:00'
draft = false
title = 'Gitlab and Gitlab Cli 教學手冊'
tags = ['教學', '工具', 'GitLab']
categories = ['教學']
+++

# GitLab 與 GitLab CLI（glab）完整企業級教學手冊

> 本手冊依據 GitLab 官方文件（docs.gitlab.com）、GitLab CLI 官方文件（docs.gitlab.com/cli，對應 `gitlab-org/cli` 專案原始文件）、GitLab Runner 官方文件與官方發行紀錄撰寫，涵蓋 GitLab.com、GitLab Self-Managed、GitLab Dedicated 三種部署形態，以及 `glab`、GitLab CI/CD、GitLab Runner、GitLab Security、GitLab API、GitLab Duo Agent Platform、GitLab MCP server 等主題。目標是讓初學者、資深架構師與 DevOps／Platform／SRE 團隊都能在同一份文件中找到需要的知識，以及可直接複製執行的指令。
>
> 📌 **使用建議**：
>
> - 第一次接觸 GitLab 的同仁，建議依序閱讀第一章～第七章。
> - 已熟悉 Git 的開發者，可直接從第四章（glab CLI）開始。
> - DevOps／Platform／SRE 團隊，請聚焦第三、八、十一、十九、二十章。
> - 想了解 AI 協作開發（GitLab Duo、Claude Code、GitHub Copilot、MCP）的同仁，請見第十三～十八章。
> - 本文件與既有的《GitLab使用教學.md》為獨立文件，內容不互相依賴，可單獨閱讀。

## 文件資訊

| 項目 | 內容 |
|---|---|
| 文件版本 | v2.0（2026-09-30） |
| GitLab 基準版本 | GitLab 19.4（19.4.0 於 2026-09-16 發布；目前最新修補版 19.4.1） |
| GitLab Runner 基準版本 | 19.4.1（2026-09-24） |
| GitLab CLI（glab）基準版本 | v1.120.0（2026-09-29） |
| 適用部署形態 | GitLab.com、GitLab Self-Managed、GitLab Dedicated |
| 適用對象 | 開發人員、Tech Lead、架構師、DevOps／Platform／SRE、資安團隊、IT 治理與稽核人員 |
| 最後查證日期 | 2026-09-30（查證方式與結果見附錄 23.11） |
| 版本紀錄 | 見附錄 23.10 |

> ⚠️ **閱讀前須知**：GitLab 每月第三個星期四發布一個小版號，`glab` 則約每週發布一次新版。本手冊中標示為 **Beta** 或 **Experimental**（實驗性）的功能與指令，其行為、旗標或方案層級（Tier）可能在後續版本變動。正式導入前，請以當下安裝版本的 `--help` 輸出與官方文件為準。

## 執行摘要

GitLab 是一套把「規劃 → 開發 → 驗證 → 安全 → 套件 → 發布 → 維運 → 治理」整合在單一應用程式、單一資料模型與單一權限模型內的 DevSecOps 平台。`glab` 是 GitLab 官方維護的命令列工具，讓開發者與 AI Agent 能在終端機完成 Merge Request、Issue、CI/CD、Release 等操作。

本版（v2.0）相對於初版（v1.0）的重點變更如下：

1. **glab 指令全面對照官方文件重寫**：
   - `glab pipeline` 別名已棄用，統一改用 `glab ci`。
   - `glab duo` 已改為啟動 GitLab Duo CLI 的 `glab duo cli`。
   - `glab mcp serve` 只提供 stdio transport，且為 Experimental。
   - 移除 `glab project`、`glab runner register`、`glab duo ask` 等官方不存在的指令與旗標。
   - 補齊 `job`、`label`、`milestone`、`token`、`deploy-key`、`packages`、`security`、`dependency-firewall`、`govern` 等 45 個頂層指令的說明。
2. **區分兩種 MCP 整合方式**：
   - GitLab 內建的 MCP server（HTTP 端點 `/api/v4/mcp`，Beta，19.2 起 Free 即可使用）。
   - `glab mcp serve`（本機 stdio，Experimental）。
3. **GitLab Duo 依官方授權模型重整**：
   - Duo Core／Pro／Enterprise 三種 add-on。
   - Duo Agent Platform 以 GitLab Credits 計價，18.8 起 GA。
   - 2026-05-21 起 Duo Core 使用者改用 Agentic Chat。
   - Code Review Flow 取代舊版 Duo Code Review。
4. **安全掃描依官方 Tier 修正**：
   - Secret push protection、Dependency scanning、DAST 皆為 Ultimate。
   - 範本路徑改為 `Jobs/*` 與 `Jobs/Dependency-Scanning.v2`。
   - DAST 改用 `DAST_TARGET_URL`。
   - 舊版 License-Scanning 範本已於 17.0 移除。
5. **維運基準更新**：
   - GitLab 19.x 最低需求為 PostgreSQL 17。
   - 必要升級停靠版本為 19.2／19.5／19.8／19.11。
   - Docker Machine executor 將於 20.0（2027-05）移除。
   - Helm chart 內建的 PostgreSQL／Redis／MinIO 已於 19.0 移除。
6. **新增企業白皮書所需內容**：CI/CD Components 與 Catalog、CI/CD inputs、OIDC ID Token、Runner 自動擴縮、Security Policies、細粒度 Token、升級路徑規劃、版本紀錄、查證紀錄與參考資料。

## 📖 目錄

> 💡 點擊章節可跳至本文對應位置；第一層為章，第二層為節，第三層為編號小節。

<!-- TOC-AUTO-BEGIN -->

- [文件資訊](#文件資訊)
- [執行摘要](#執行摘要)
- [第一章 GitLab 介紹](#第一章-gitlab-介紹)
  - [1.1 GitLab 發展歷史](#11-gitlab-發展歷史)
  - [1.2 GitLab 核心理念](#12-gitlab-核心理念)
  - [1.3 GitLab 與 GitHub 比較](#13-gitlab-與-github-比較)
  - [1.4 GitLab 與 Azure DevOps 比較](#14-gitlab-與-azure-devops-比較)
  - [1.5 GitLab 與 Bitbucket 比較](#15-gitlab-與-bitbucket-比較)
  - [1.6 GitLab SaaS / Self-Managed / Dedicated 差異比較](#16-gitlab-saas--self-managed--dedicated-差異比較)
  - [1.7 版本發布節奏與生命週期](#17-版本發布節奏與生命週期)
  - [✅ 第一章 Checklist](#-第一章-checklist)
- [第二章 GitLab 整體架構](#第二章-gitlab-整體架構)
  - [2.1 端到端架構總覽](#21-端到端架構總覽)
  - [2.2 核心元件運作方式](#22-核心元件運作方式)
  - [2.3 GitLab Architecture Tiers（部署規模分級）](#23-gitlab-architecture-tiers部署規模分級)
  - [2.4 周邊關鍵元件](#24-周邊關鍵元件)
  - [✅ 第二章 Checklist](#-第二章-checklist)
- [第三章 GitLab 安裝與部署](#第三章-gitlab-安裝與部署)
  - [3.1 GitLab CE 與 EE 差異](#31-gitlab-ce-與-ee-差異)
  - [3.2 Linux Package（Omnibus）安裝 — Ubuntu](#32-linux-packageomnibus安裝--ubuntu)
  - [3.3 Linux Package 安裝 — RHEL / AlmaLinux / Oracle Linux](#33-linux-package-安裝--rhel--almalinux--oracle-linux)
  - [3.4 Docker 安裝](#34-docker-安裝)
  - [3.5 Podman 安裝（Rootless）](#35-podman-安裝rootless)
  - [3.6 Helm Chart（Kubernetes）安裝概覽](#36-helm-chartkubernetes安裝概覽)
  - [3.7 系統需求（GitLab 19.x）](#37-系統需求gitlab-19x)
  - [3.8 安裝後的初始強化設定](#38-安裝後的初始強化設定)
  - [✅ 第三章 Checklist](#-第三章-checklist)
- [第四章 GitLab CLI（glab）](#第四章-gitlab-cliglab)
  - [4.1 glab 是什麼](#41-glab-是什麼)
  - [4.2 glab 架構](#42-glab-架構)
  - [4.3 glab 主要功能分類](#43-glab-主要功能分類)
  - [4.4 glab 指令穩定度分級（Stable / Beta / Experimental）](#44-glab-指令穩定度分級stable--beta--experimental)
  - [4.5 安裝 glab](#45-安裝-glab)
  - [4.6 登入與認證](#46-登入與認證)
  - [4.7 設定檔與環境變數](#47-設定檔與環境變數)
  - [4.8 在 CI/CD 中使用 glab](#48-在-cicd-中使用-glab)
  - [4.9 版本升級與相容性管理](#49-版本升級與相容性管理)
  - [✅ 第四章 Checklist](#-第四章-checklist)
- [第五章 GitLab CLI 指令大全](#第五章-gitlab-cli-指令大全)
  - [5.1 `glab auth` — 認證管理](#51-glab-auth--認證管理)
  - [5.2 `glab repo` — 專案管理](#52-glab-repo--專案管理)
  - [5.3 `glab mr` — Merge Request](#53-glab-mr--merge-request)
  - [5.4 `glab issue` — Issue 管理](#54-glab-issue--issue-管理)
  - [5.5 `glab ci` 與 `glab job` — CI/CD 操作](#55-glab-ci-與-glab-job--cicd-操作)
  - [5.6 `glab release` — 版本發布](#56-glab-release--版本發布)
  - [5.7 `glab variable` — CI/CD 變數管理](#57-glab-variable--cicd-變數管理)
  - [5.8 專案層級管理：`label`、`milestone`、`iteration`](#58-專案層級管理labelmilestoneiteration)
  - [5.9 `glab api` — 通用 API 呼叫](#59-glab-api--通用-api-呼叫)
  - [5.10 `glab duo` — GitLab Duo CLI](#510-glab-duo--gitlab-duo-cli)
  - [5.11 `glab mcp` — 啟動本機 MCP Server](#511-glab-mcp--啟動本機-mcp-server)
  - [5.12 `glab stack` — Stacked Diff 管理](#512-glab-stack--stacked-diff-管理)
  - [5.13 `glab search` — 語意程式碼搜尋](#513-glab-search--語意程式碼搜尋)
  - [5.14 `glab schedule` — Pipeline 排程管理](#514-glab-schedule--pipeline-排程管理)
  - [5.15 `glab runner` — Runner 管理](#515-glab-runner--runner-管理)
  - [5.16 `glab orbit` — Orbit 知識圖譜](#516-glab-orbit--orbit-知識圖譜)
  - [5.17 `glab skills` — Agent Skills 管理](#517-glab-skills--agent-skills-管理)
  - [5.18 `glab attestation` — 軟體供應鏈驗證](#518-glab-attestation--軟體供應鏈驗證)
  - [5.19 `glab cluster` — Kubernetes Agent 管理](#519-glab-cluster--kubernetes-agent-管理)
  - [5.20 `glab container-registry` — 容器倉庫管理](#520-glab-container-registry--容器倉庫管理)
  - [5.21 `glab incident` — 事件管理](#521-glab-incident--事件管理)
  - [5.22 `glab work-items` — Work Item 管理](#522-glab-work-items--work-item-管理)
  - [5.23 Token 與金鑰：`token`、`deploy-key`、`ssh-key`、`gpg-key`](#523-token-與金鑰tokendeploy-keyssh-keygpg-key)
  - [5.24 CI/CD 周邊：`securefile`、`packages`、`opentofu`、`changelog`](#524-cicd-周邊securefilepackagesopentofuchangelog)
  - [5.25 安全與治理（Experimental）：`security`、`dependency-firewall`、`govern`、`artifact-registry`](#525-安全與治理experimentalsecuritydependency-firewallgovernartifact-registry)
  - [5.26 個人效率：`alias`、`config`、`completion`、`todo`、`user`](#526-個人效率aliasconfigcompletiontodouser)
  - [5.27 完整指令速查（v1.120.0）](#527-完整指令速查v11200)
  - [✅ 第五章 Checklist](#-第五章-checklist)
- [第六章 GitLab Flow](#第六章-gitlab-flow)
  - [6.1 三種主流分支策略比較](#61-三種主流分支策略比較)
  - [6.2 GitLab Flow 的兩種變體](#62-gitlab-flow-的兩種變體)
    - [6.2.1 Environment Branch 模式](#621-environment-branch-模式)
    - [6.2.2 Release Branch 模式](#622-release-branch-模式)
  - [6.3 企業建議](#63-企業建議)
  - [6.4 合併方式與 Merge Train](#64-合併方式與-merge-train)
  - [✅ 第六章 Checklist](#-第六章-checklist)
- [第七章 CI/CD](#第七章-cicd)
  - [7.1 `.gitlab-ci.yml` 核心概念](#71-gitlab-ciyml-核心概念)
  - [7.2 Java / Spring Boot 完整 CI/CD 範例](#72-java--spring-boot-完整-cicd-範例)
  - [7.3 Node.js / Vue 完整 CI/CD 範例](#73-nodejs--vue-完整-cicd-範例)
  - [7.4 React 完整 CI/CD 範例](#74-react-完整-cicd-範例)
  - [7.5 Python 完整 CI/CD 範例](#75-python-完整-cicd-範例)
  - [7.6 `include` 拆分與共用範本](#76-include-拆分與共用範本)
  - [7.7 CI/CD Components 與 CI/CD Catalog](#77-cicd-components-與-cicd-catalog)
  - [7.8 CI/CD inputs 與 Pipeline 參數化](#78-cicd-inputs-與-pipeline-參數化)
  - [7.9 進階流程控制：`needs`、`parallel:matrix`、Parent-Child Pipeline](#79-進階流程控制needsparallelmatrixparent-child-pipeline)
  - [7.10 以 OIDC ID Token 取代長效雲端密鑰](#710-以-oidc-id-token-取代長效雲端密鑰)
  - [7.11 Pipeline 效能與成本最佳化](#711-pipeline-效能與成本最佳化)
  - [✅ 第七章 Checklist](#-第七章-checklist)
- [第八章 GitLab Runner](#第八章-gitlab-runner)
  - [8.1 Runner 類型總覽](#81-runner-類型總覽)
  - [8.2 安裝 GitLab Runner](#82-安裝-gitlab-runner)
  - [8.3 設定要點](#83-設定要點)
  - [8.4 維護、升級、故障排除](#84-維護升級故障排除)
  - [8.5 Runner 自動擴縮與 Executor 選型](#85-runner-自動擴縮與-executor-選型)
  - [8.6 Runner 安全強化](#86-runner-安全強化)
  - [✅ 第八章 Checklist](#-第八章-checklist)
- [第九章 Container Registry](#第九章-container-registry)
  - [9.1 GitLab Container Registry 概念](#91-gitlab-container-registry-概念)
  - [9.2 基本操作](#92-基本操作)
  - [9.3 Image 掃描（Container Scanning）](#93-image-掃描container-scanning)
  - [9.4 Image Promotion（多環境晉升流程）](#94-image-promotion多環境晉升流程)
  - [9.5 最佳實務](#95-最佳實務)
  - [9.6 Container Virtual Registry（聚合上游倉庫）](#96-container-virtual-registry聚合上游倉庫)
  - [9.7 多架構 Image 支援（Multi-Architecture）](#97-多架構-image-支援multi-architecture)
  - [✅ 第九章 Checklist](#-第九章-checklist)
- [第十章 Package Registry](#第十章-package-registry)
  - [10.1 支援的套件格式總覽](#101-支援的套件格式總覽)
  - [10.2 Maven 設定與發布](#102-maven-設定與發布)
  - [10.3 npm / pnpm 設定與發布](#103-npm--pnpm-設定與發布)
  - [10.4 NuGet 發布](#104-nuget-發布)
  - [10.5 PyPI 發布](#105-pypi-發布)
  - [10.6 Generic Package（任意檔案）](#106-generic-package任意檔案)
  - [10.7 相依套件來源治理：Maven Virtual Registry 與 Dependency Firewall](#107-相依套件來源治理maven-virtual-registry-與-dependency-firewall)
  - [✅ 第十章 Checklist](#-第十章-checklist)
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
  - [11.10 Security Policies（安全政策即程式碼）](#1110-security-policies安全政策即程式碼)
  - [11.11 安全相關角色與權限](#1111-安全相關角色與權限)
  - [✅ 第十一章 Checklist](#-第十一章-checklist)
- [第十二章 GitLab API](#第十二章-gitlab-api)
  - [12.1 REST API 與 GraphQL API 選用建議](#121-rest-api-與-graphql-api-選用建議)
  - [12.2 Access Token 種類](#122-access-token-種類)
  - [12.3 curl 範例](#123-curl-範例)
  - [12.4 Java / Spring Boot 範例](#124-java--spring-boot-範例)
  - [12.5 Python 範例](#125-python-範例)
  - [12.6 TypeScript 範例](#126-typescript-範例)
  - [12.7 分頁、限流與 API 相容性](#127-分頁限流與-api-相容性)
  - [✅ 第十二章 Checklist](#-第十二章-checklist)
- [第十三章 GitLab Duo](#第十三章-gitlab-duo)
  - [13.1 GitLab Duo 功能總覽與授權模型](#131-gitlab-duo-功能總覽與授權模型)
  - [13.2 GitLab Duo Chat](#132-gitlab-duo-chat)
    - [13.2.1 Agentic Chat 與 Non-Agentic Chat](#1321-agentic-chat-與-non-agentic-chat)
    - [13.2.2 GitLab Duo Agent Platform（18.8 GA）](#1322-gitlab-duo-agent-platform188-ga)
  - [13.3 Code Suggestions（程式碼建議）](#133-code-suggestions程式碼建議)
  - [13.4 Code Review Flow（MR 自動審查）](#134-code-review-flowmr-自動審查)
  - [13.5 Vulnerability Explanation 與 Security Analyst Agent](#135-vulnerability-explanation-與-security-analyst-agent)
  - [13.6 Test Generation 與 Refactoring](#136-test-generation-與-refactoring)
  - [13.7 Prompt Engineering 與客製化](#137-prompt-engineering-與客製化)
  - [13.8 AI 治理、稽核與成本控管](#138-ai-治理稽核與成本控管)
  - [✅ 第十三章 Checklist](#-第十三章-checklist)
- [第十四章 GitLab + Claude Code](#第十四章-gitlab--claude-code)
  - [14.1 整合架構總覽](#141-整合架構總覽)
  - [14.2 實戰案例：Claude Code 自動建立並提交 Merge Request](#142-實戰案例claude-code-自動建立並提交-merge-request)
  - [14.3 實戰案例：Claude Code 自動 Review 程式碼](#143-實戰案例claude-code-自動-review-程式碼)
  - [14.4 實戰案例：Pipeline 失敗時自動診斷](#144-實戰案例pipeline-失敗時自動診斷)
  - [14.5 CLAUDE.md 專案規範整合建議](#145-claudemd-專案規範整合建議)
  - [14.6 讓 Claude Code 更懂 GitLab：Agent Skills 與稽核](#146-讓-claude-code-更懂-gitlabagent-skills-與稽核)
  - [14.7 在 GitLab 內執行 Claude Code：External Agents](#147-在-gitlab-內執行-claude-codeexternal-agents)
  - [✅ 第十四章 Checklist](#-第十四章-checklist)
- [第十五章 GitLab + GitHub Copilot](#第十五章-gitlab--github-copilot)
  - [15.1 為什麼會在 GitLab 上使用 GitHub Copilot](#151-為什麼會在-gitlab-上使用-github-copilot)
  - [15.2 Agent Mode 與 Coding Agent 操作模式](#152-agent-mode-與-coding-agent-操作模式)
  - [15.3 如何與 GitLab 協作（實務整合建議）](#153-如何與-gitlab-協作實務整合建議)
  - [✅ 第十五章 Checklist](#-第十五章-checklist)
- [第十六章 GitLab + MCP](#第十六章-gitlab--mcp)
  - [16.1 Model Context Protocol 簡介](#161-model-context-protocol-簡介)
  - [16.2 GitLab 的兩種 MCP Server](#162-gitlab-的兩種-mcp-server)
  - [16.3 設定 Claude Code 連接 GitLab MCP Server](#163-設定-claude-code-連接-gitlab-mcp-server)
  - [16.4 權限管理與工具範圍控制](#164-權限管理與工具範圍控制)
  - [16.5 實際案例：多步驟 Agent 工作流程](#165-實際案例多步驟-agent-工作流程)
  - [16.6 GitLab Orbit（Knowledge Graph）與 AI Agent](#166-gitlab-orbitknowledge-graph與-ai-agent)
  - [✅ 第十六章 Checklist](#-第十六章-checklist)
- [第十七章 AI 協助 Legacy System 逆向工程](#第十七章-ai-協助-legacy-system-逆向工程)
  - [17.1 為什麼 Legacy System 逆向工程適合導入 AI](#171-為什麼-legacy-system-逆向工程適合導入-ai)
  - [17.2 實戰步驟：將 Legacy 程式碼匯入 GitLab 並建立分析基線](#172-實戰步驟將-legacy-程式碼匯入-gitlab-並建立分析基線)
  - [17.3 實戰案例：AI Agent 自動分析 Legacy System](#173-實戰案例ai-agent-自動分析-legacy-system)
  - [17.4 各 Legacy 技術的 AI 逆向工程要點](#174-各-legacy-技術的-ai-逆向工程要點)
  - [17.5 文件生成與架構分析範本](#175-文件生成與架構分析範本)
  - [17.6 逆向工程後的重構規劃](#176-逆向工程後的重構規劃)
  - [✅ 第十七章 Checklist](#-第十七章-checklist)
- [第十八章 Framework 升級專案](#第十八章-framework-升級專案)
  - [18.1 升級專案的 GitLab 治理框架](#181-升級專案的-gitlab-治理框架)
  - [18.2 Spring Boot 2 → 3 / Java 8 → 21 實戰流程](#182-spring-boot-2--3--java-8--21-實戰流程)
  - [18.3 Vue2 → Vue3 升級實戰流程](#183-vue2--vue3-升級實戰流程)
  - [18.4 Angular 升級實戰流程](#184-angular-升級實戰流程)
  - [18.5 升級專案的企業治理建議](#185-升級專案的企業治理建議)
  - [18.6 AI Agent 輔助升級的 GitLab 原生做法](#186-ai-agent-輔助升級的-gitlab-原生做法)
  - [✅ 第十八章 Checklist](#-第十八章-checklist)
- [第十九章 大型企業 DevSecOps 平台設計](#第十九章-大型企業-devsecops-平台設計)
  - [19.1 依規模分級的架構設計原則](#191-依規模分級的架構設計原則)
  - [19.2 大型企業架構圖](#192-大型企業架構圖)
  - [19.3 權限模型設計](#193-權限模型設計)
  - [19.4 Group 策略與 Project 策略](#194-group-策略與-project-策略)
  - [19.5 Branch 策略](#195-branch-策略)
  - [19.6 身分治理：SSO、SCIM、Service Account 與 Custom Roles](#196-身分治理ssoscimservice-account-與-custom-roles)
  - [19.7 合規治理：Compliance Center 與稽核](#197-合規治理compliance-center-與稽核)
  - [✅ 第十九章 Checklist](#-第十九章-checklist)
- [第二十章 GitLab 維運手冊](#第二十章-gitlab-維運手冊)
  - [20.1 備份與還原](#201-備份與還原)
  - [20.2 監控（Prometheus + Grafana）](#202-監控prometheus--grafana)
  - [20.3 Logging](#203-logging)
  - [20.4 升級](#204-升級)
  - [20.5 高可用性（HA）與災難復原（DR）](#205-高可用性ha與災難復原dr)
  - [20.6 升級路徑規劃（GitLab 19.x）](#206-升級路徑規劃gitlab-19x)
  - [20.7 棄用與移除追蹤（GitLab 20.0）](#207-棄用與移除追蹤gitlab-200)
  - [✅ 第二十章 Checklist](#-第二十章-checklist)
- [第二十一章 GitLab 最佳實務](#第二十一章-gitlab-最佳實務)
  - [21.1 命名規範](#211-命名規範)
  - [21.2 Branch Strategy](#212-branch-strategy)
  - [21.3 MR Strategy](#213-mr-strategy)
  - [21.4 Pipeline Strategy](#214-pipeline-strategy)
  - [21.5 Release Strategy](#215-release-strategy)
  - [21.6 Security Strategy](#216-security-strategy)
  - [✅ 第二十一章 Checklist](#-第二十一章-checklist)
- [第二十二章 常見問題 FAQ](#第二十二章-常見問題-faq)
  - [22.1 開發類](#221-開發類)
  - [22.2 CI/CD 類](#222-cicd-類)
  - [22.3 Security 類](#223-security-類)
  - [22.4 Runner 類](#224-runner-類)
  - [22.5 Kubernetes 類](#225-kubernetes-類)
  - [22.6 AI 類](#226-ai-類)
  - [22.7 GitLab Duo 類](#227-gitlab-duo-類)
  - [22.8 glab 類](#228-glab-類)
  - [22.9 版本更新類（v2.0 新增）](#229-版本更新類v20-新增)
  - [✅ 第二十二章 Checklist](#-第二十二章-checklist)
- [第二十三章 附錄](#第二十三章-附錄)
  - [23.1 常用 glab 指令速查表](#231-常用-glab-指令速查表)
  - [23.2 CI/CD 通用範本](#232-cicd-通用範本)
  - [23.3 Spring Boot 範本](#233-spring-boot-範本)
  - [23.4 Vue3 範本](#234-vue3-範本)
  - [23.5 Kubernetes 範本](#235-kubernetes-範本)
  - [23.6 Docker 範本（多階段建置）](#236-docker-範本多階段建置)
  - [23.7 Helm 範本](#237-helm-範本)
  - [23.8 十大 AI Agent 實戰情境總覽](#238-十大-ai-agent-實戰情境總覽)
    - [23.8.1 AI Agent 自動產生 Release Note](#2381-ai-agent-自動產生-release-note)
    - [23.8.2 AI Agent 自動產生架構文件](#2382-ai-agent-自動產生架構文件)
    - [23.8.3 AI Agent 協助大型共用平台開發](#2383-ai-agent-協助大型共用平台開發)
  - [23.9 企業導入檢查清單](#239-企業導入檢查清單)
  - [23.10 版本紀錄](#2310-版本紀錄)
    - [23.10.1 v1.0 → v2.0 主要更正一覽](#23101-v10--v20-主要更正一覽)
  - [23.11 查證紀錄](#2311-查證紀錄)
    - [23.11.1 待確認事項](#23111-待確認事項)
  - [23.12 參考資料](#2312-參考資料)
  - [✅ 第二十三章 Checklist](#-第二十三章-checklist)

<!-- TOC-AUTO-END -->

---

## 第一章 GitLab 介紹

### 1.1 GitLab 發展歷史

GitLab 最初由 Dmitriy Zaporozhets 與 Valery Sizov 於 2011 年以 Ruby on Rails 開發，作為一套開源的 Git 版本控制管理工具。早期僅是「GitHub 的開源替代品」，但 GitLab 團隊很快意識到軟體交付不只是「管程式碼」，而是一個從規劃、開發、測試、安全掃描、部署到監控的完整生命週期。

關鍵發展里程碑：

| 年份 | 重要事件 |
|---|---|
| 2011 | GitLab 專案誕生，作為自架（self-hosted）Git 管理工具 |
| 2013 | 推出 GitLab Enterprise Edition（EE） |
| 2014 | GitLab 公司正式成立，開始以企業形式營運 |
| 2015 | 推出 GitLab CI，內建 CI/CD 能力（不需額外裝 Jenkins） |
| 2016 | 推出內建 Container Registry |
| 2017 | 收購 Gitter；推出 Auto DevOps |
| 2018 | 完成 D 輪募資，Geo 等企業級多地域功能持續強化 |
| 2020 | 收購 Peach Tech 與 Fuzzit，強化 DAST 與 Fuzz Testing 能力 |
| 2021 | NASDAQ 上市（GTLB） |
| 2023 | 推出 GitLab Duo（AI 輔助開發功能套件） |
| 2024 | GitLab Duo Chat 於 16.11 GA（Code Suggestions 已於 2023 年底 GA）；發表 GitLab Duo Workflow（Agentic AI）早期版本 |
| 2025 | GitLab 18.0 推出 Duo Core（Premium/Ultimate 內含）；Duo Agent Platform 於 18.2 以 Beta 推出；GitLab MCP server 於 18.3 以 Experiment 推出、18.6 升為 Beta 並支援 HTTP transport |
| 2026 | GitLab 18.8（1 月）Duo Agent Platform 與 GitLab Credits 正式 GA；GitLab 19.0（5 月）發布，PostgreSQL 17 成為最低需求、Duo Core 使用者改用 Agentic Chat；19.2 起 GitLab MCP server 開放至 Free 層級、GitLab Duo CLI GA；目前最新為 19.4（9 月，詳見 1.7 節） |

GitLab 的核心精神之一是「One DevOps Platform」——將原本散落在 Jira（規劃）、GitHub（程式碼）、Jenkins（CI/CD）、SonarQube（程式碼品質）、Nexus（套件管理）、Snyk（安全掃描）的工具鏈，整合成單一平台、單一資料庫、單一權限模型。

### 1.2 GitLab 核心理念

GitLab 的設計理念可以歸納為以下幾點：

1. **單一應用程式（Single Application）**：所有 DevSecOps 流程都在同一個 Web UI、同一個資料模型下運作，避免「工具鏈拼接」帶來的資料斷層與整合成本。
2. **內建而非外掛（Built-in, not bolted-on）**：CI/CD、Security Scanning、Package Registry、Container Registry 都是 GitLab 原生功能，而非透過外部 plugin 串接。
3. **從 Idea 到 Production 的完整循環**：涵蓋 Plan → Create → Verify → Package → Secure → Release → Configure → Monitor → Govern 九大階段。
4. **DevSecOps 左移（Shift Left Security）**：安全掃描從開發階段就介入，而不是上線前才補檢查。
5. **開源核心（Open Core）**：核心功能開源（GitLab CE），進階企業功能（合規、進階權限、AI）則在 EE / Ultimate 授權中。
6. **AI 原生化（AI-native DevSecOps）**：自 GitLab Duo 推出後，GitLab 將生成式 AI 深度整合在 MR 審查、漏洞解釋、測試產生、Chat 問答等每一個環節；18.x 起更以 GitLab Duo Agent Platform 讓多個 AI Agent 與 Flow 直接參與開發流程（見第十三章）。

#### DevSecOps 平台概念圖

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

### 1.3 GitLab 與 GitHub 比較

| 比較項目 | GitLab | GitHub |
|---|---|---|
| 定位 | One DevSecOps Platform（全生命週期） | 程式碼協作平台，CI/CD 與安全多透過 Actions/Marketplace 擴充 |
| CI/CD | 原生內建（`.gitlab-ci.yml`），無需額外平台 | GitHub Actions（YAML workflow），生態系豐富 |
| 自架能力 | CE/EE 皆可完整自架（含 HA、Geo） | GitHub Enterprise Server 可自架，但功能更新通常落後 SaaS |
| 內建安全掃描 | SAST/DAST/Dependency/Container/Secret 皆原生內建 | 需搭配 CodeQL、Dependabot、第三方 Action |
| 套件/容器倉庫 | 原生 Container Registry + Package Registry（Maven/npm/NuGet/PyPI...） | GitHub Packages（功能較簡） |
| AI 功能 | GitLab Duo（Agentic Chat、Code Suggestions、Code Review Flow、Duo Agent Platform） | GitHub Copilot（Chat、Agent Mode、Coding Agent、Code Review） |
| Issue/專案管理 | Issue + Epic + Roadmap + Iteration（原生敏捷工具） | Issue + Project（Projects v2），敏捷功能較簡單 |
| 權限模型 | Group → Subgroup → Project 多層繼承，企業治理彈性高 | Organization → Team → Repository |
| MCP 支援 | GitLab MCP server（內建於 GitLab，HTTP 端點 `/api/v4/mcp`，Beta） | GitHub MCP Server（官方維護） |
| CLI 工具 | `glab` | `gh` |

> ⚠️ **注意事項**：GitLab 與 GitHub 的核心差異不在「程式碼管理」，而在於**是否把 CI/CD、安全、套件管理視為一等公民功能**。導入評估時，應計算「整合外部工具的隱性成本」（維運、授權、資料同步），而非只比較授權費用。

### 1.4 GitLab 與 Azure DevOps 比較

| 比較項目 | GitLab | Azure DevOps |
|---|---|---|
| 組成 | 單一整合平台 | Boards / Repos / Pipelines / Artifacts / Test Plans 五個子服務組成 |
| Pipeline 語法 | `.gitlab-ci.yml`（YAML，單一檔案為主，可 `include`） | Azure Pipelines YAML，亦支援 Classic UI 編輯器 |
| 與雲端整合 | 雲中立，對 AWS/GCP/Azure/地端皆友善 | 與 Azure 生態（Entra ID、ACR、AKS）整合最深 |
| Self-Managed | 原生支援（CE/EE 一致架構） | Azure DevOps Server（功能落後 Services 版） |
| 授權模式 | Free / Premium / Ultimate（依使用者數計價） | Basic / Basic+Test Plans（依使用者數＋方案計價） |
| AI 功能 | GitLab Duo（含 Duo Agent Platform） | 主要透過 GitHub Copilot（IDE 端）與 Azure DevOps 整合，整合深度依功能而異 |

> 💡 **企業選型建議**：若企業已大量採用 Azure 生態（Entra ID 單一登入、AKS、Azure Monitor），Azure DevOps 整合成本較低；但若企業重視「雲中立」與「單一平台 DevSecOps」，GitLab 在自架彈性與安全左移上更具優勢。

### 1.5 GitLab 與 Bitbucket 比較

| 比較項目 | GitLab | Bitbucket |
|---|---|---|
| 定位 | DevSecOps 全生命週期平台 | 程式碼協作為主，搭配 Bitbucket Pipelines |
| CI/CD 能力 | 功能完整、原生 Runner 架構（Docker/K8s/Shell） | Pipelines 功能簡單，適合中小型專案 |
| 安全掃描 | 原生 SAST/DAST/Dependency/Container/Secret | 需搭配 Snyk 等第三方整合 |
| 與 Jira 整合 | 透過 Webhook/Smart Commit 整合（非原生） | 與 Jira 同屬 Atlassian，整合最深 |
| 企業治理 | Group/Subgroup 階層、Compliance Framework | Workspace/Project 階層，治理功能較簡單 |

> 💡 **企業選型建議**：若團隊已重度投資 Atlassian 生態（Jira + Confluence），Bitbucket 整合體驗最順；但若需要「程式碼到上線」單一平台治理與內建安全掃描，GitLab 仍是業界對比中功能最完整的選項之一。

### 1.6 GitLab SaaS / Self-Managed / Dedicated 差異比較

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

### 1.7 版本發布節奏與生命週期

> 🆕 **v2.0 新增**

企業導入 GitLab 前，必須先理解它的版本節奏，才能規劃升級窗口、評估新功能導入時機，並確保 Self-Managed 環境持續獲得安全修補。

| 項目 | 官方節奏／規則 | 企業規劃重點 |
|---|---|---|
| 小版號（Minor） | 每月第三個星期四發布（例如 19.4.0 於 2026-09 發布） | GitLab.com 持續部署最新程式碼；Self-Managed 需自行排程升級 |
| 大版號（Major） | 每年 5 月發布一次（18.0 於 2025-05、19.0 於 2026-05，20.0 預定 2027-05） | 大版號會集中移除已棄用功能（Breaking Change），需提前盤點 |
| 修補版（Patch） | 不定期發布，安全修補通常同時提供給目前與前兩個小版號（例如 2026-09-22 同日發布 19.4.1、19.3.3、19.2.7） | Self-Managed 至少要維持在官方仍提供修補的版本範圍內 |
| 必要升級停靠版本（Required upgrade stops） | 17.5 起固定在 `x.2`、`x.5`、`x.8`、`x.11`，GitLab 19 為 19.2／19.5／19.8／19.11 | 跨版升級不可跳過停靠版本，每一站都要等背景遷移（Background migrations）完成 |
| 功能成熟度 | Experiment → Beta → Generally Available（GA） | Experiment／Beta 功能不建議納入正式流程或 SLA 範圍 |

```mermaid
flowchart LR
    V194[目前版本 19.4] --> S195[下一個停靠版本 19.5\n預定 2026-10]
    S195 --> S198[19.8]
    S198 --> S1911[19.11]
    S1911 --> V20[20.0\n預定 2027-05\n集中移除棄用功能]
```

> ⚠️ **注意事項**：大版號 20.0 已公告將移除 Compliance pipelines、Docker Machine executor 等功能（詳見第二十章 20.7）。建議 Platform 團隊每季檢視一次官方「Deprecations and removals by version」頁面，將影響項目轉為內部 Issue 追蹤，而不是等到升級前才發現。

### ✅ 第一章 Checklist

- [ ] 已理解 GitLab「One DevSecOps Platform」的核心理念，而非僅是程式碼託管工具
- [ ] 已對照 GitHub / Azure DevOps / Bitbucket 比較表，確認導入 GitLab 的具體理由
- [ ] 已根據資料主權、合規、維運人力評估，選定 SaaS / Self-Managed / Dedicated 部署形態
- [ ] 已將 GitLab 九大階段（Plan～Govern）對應到企業現有工具鏈，列出可被取代或整合的系統清單
- [ ] 已理解 GitLab 月度／年度發布節奏與必要升級停靠版本，並排入年度維運計畫

---

## 第二章 GitLab 整體架構

### 2.1 端到端架構總覽

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

### 2.2 核心元件運作方式

#### Web Service（Puma + Workhorse）

GitLab 的前端 Web 服務由 **Puma**（Ruby 應用伺服器）搭配 **GitLab Workhorse**（Go 撰寫的反向代理）組成。Workhorse 負責處理大型檔案上傳（如 Git push 的 pack 檔、LFS 物件）、靜態資源與長連線（例如 CI Job log 即時串流），把這些 I/O 密集工作從 Puma 卸載，讓 Puma 專注處理 Rails 應用邏輯，大幅降低記憶體壓力與回應延遲。

#### API Service

GitLab REST API 與 GraphQL API 共用同一套 Rails 應用程式碼（Grape 框架實作 REST，graphql-ruby 實作 GraphQL）。在大型部署中，官方建議將 API 流量與 Web UI 流量分離到不同的 Puma 進程群組（`puma['app_role'] = 'api'` / `'web'`），避免 CI/CD 觸發的大量 API 請求拖慢一般使用者的網頁操作體驗。

#### Sidekiq

Sidekiq 是 GitLab 的背景工作佇列引擎，處理所有「不需要即時回應」的工作，例如：Email 通知、Webhook 觸發、Merge Request 的 Merge 動作、Repository Mirror 同步、Elasticsearch 索引更新、CI Pipeline 狀態計算等。Sidekiq 透過 Redis 作為訊息佇列，可依 Queue 類型（`high_priority`, `low_priority`, `mailers` 等）拆分成多個獨立的 Sidekiq 進程進行水平擴展。

> ⚠️ **常見維運陷阱**：當 Sidekiq Queue 堆積（如大量 Webhook 觸發或 Mirror 同步），會造成 MR 合併延遲、通知信延遲。SRE 團隊應針對 `sidekiq_queue_duration_seconds` 等指標設定告警，並評估是否需要依 Queue 類型拆分專屬 Sidekiq Pod/Process。

#### PostgreSQL

GitLab 所有結構化資料（使用者、專案、MR、Issue、Pipeline 紀錄、權限）皆儲存在 PostgreSQL。大型部署建議：

- 採用 Patroni 或雲端代管服務（AWS RDS/Aurora、Cloud SQL）實現 HA 與自動容錯切換。
- 啟用 PgBouncer 進行連線池管理，避免 Rails/Sidekiq 大量連線耗盡資料庫連線數。
- 定期執行 `VACUUM` 與監控 Bloat，PostgreSQL 是 GitLab 效能瓶頸最常見的根源之一。

#### Redis

Redis 用於：Sidekiq 佇列、Rails Session 快取、Rate Limit 計數、CI/CD 即時狀態快取。大型部署通常會將 Redis 依用途拆分為多個獨立實例（Cache / Queues / Shared State / Sessions），避免單一 Redis 成為瓶頸或單點故障。

#### Gitaly 與 Praefect

**Gitaly** 是 GitLab 的 Git 儲存與操作層，所有 `git` 操作（clone、push、diff、blame）最終都透過 gRPC 呼叫 Gitaly 完成，而不是直接呼叫檔案系統上的 `git` binary，目的是讓儲存層可以水平擴展並支援多種儲存後端。

**Praefect** 是 Gitaly Cluster 的路由與複製管理層，負責：

- 將寫入請求（push）同步複製到多個 Gitaly 節點（Replication Factor，通常設定 3）。
- 提供讀取請求的負載平衡，並在寫入時透過 Transaction 投票機制確保各複本的強一致性。
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

#### Object Storage

大型部署必須將 CI/CD Artifacts、LFS 物件、Container Registry 影像層、Package Registry 套件、使用者上傳檔案（Avatar、附件）等全部儲存到 S3 相容的 Object Storage（AWS S3、MinIO、GCS、Azure Blob），而非本機磁碟，原因：

1. 讓 GitLab 應用層（Web/Sidekiq/Runner）可以無狀態化，方便水平擴展與滾動升級。
2. 避免單機磁碟容量爆滿造成服務中斷。
3. 搭配雲端原生的備份、生命週期管理（如冷儲存歸檔）能力。

> 💡 **實務案例**：某製造業客戶在 PoC 階段使用本機磁碟儲存 Artifacts，三個月後因建置產出的 Docker Image 與測試報表暴增，磁碟用量從 50GB 飆升到 800GB，導致硬碟告警與服務中斷。改用 MinIO 後，應用伺服器磁碟使用量穩定維持在 20GB 以下。

### 2.3 GitLab Architecture Tiers（部署規模分級）

> ⚠️ **v2.0 更正**：官方 Reference Architecture 目前以**每秒請求數（RPS，Requests per Second）**作為主要容量規劃指標，「使用者人數」僅是無法取得 RPS 時的替代估算方式。初版以使用者人數粗分 Small／Medium／Large 的表格已改寫如下。

GitLab 官方 Reference Architecture（Linux package 部署）的 RPS 目標如下：

| 規模（使用者數對照） | API RPS | Web RPS | Git（Pull）RPS | Git（Push）RPS | 典型架構 |
|---|---|---|---|---|---|
| 1,000 users | 20 | 2 | 2 | 1 | 單節點 Linux package |
| 2,000 users | 40 | 4 | 4 | 1 | 拆分 PostgreSQL、Redis、Gitaly 為獨立節點 |
| 3,000 users | 60 | 6 | 6 | 1 | 起點為 HA 架構（Gitaly Cluster、Patroni、多個 Rails 節點） |
| 5,000 users | 100 | 10 | 10 | 2 | HA 架構水平擴充 |
| 10,000 users | 200 | 20 | 20 | 4 | HA 架構水平擴充 |
| 25,000 users | 500 | 50 | 50 | 10 | 大型 HA 架構（亦提供 Cloud Native Hybrid 版本） |
| 50,000 users | 1000 | 100 | 100 | 20 | 超大型 HA 架構 |

另有以 Kubernetes 為主的 **Cloud Native First** 架構，分為 Small（≤100 RPS）、Medium（≤200 RPS）、Large（≤500 RPS）、Extra Large（≤1000 RPS）四級。

取得實際 RPS 的方式：

1. 既有 GitLab 環境：用官方提供的 PromQL 查詢（Reference architecture sizing 文件）從 Prometheus 取得尖峰與持續 RPS。
2. 使用官方的 GitLab RPS Analyzer 工具分析既有日誌。
3. 新環境：以預期使用者數對照上表估算，並預留自動化（Bot、CI/CD、AI Agent）產生的 API 流量。

> 💡 **企業導入建議**：容量規劃不能只看人數，**CI/CD 並發量、API 自動化呼叫與 AI Agent 流量**才是 RPS 的主要來源。一個 200 人但每天觸發上萬次 Pipeline Job、又大量使用 AI Agent 呼叫 API 的團隊，所需容量可能遠高於一個 2,000 人但自動化程度低的團隊。官方也特別提醒，AI 驅動的使用模式會改變工作負載組成，導入 Duo Agent Platform 或 MCP 後應重新量測 RPS。

### 2.4 周邊關鍵元件

> 🆕 **v2.0 新增**

除了 2.2 節的核心元件，企業架構設計時還需要納入下列元件：

| 元件 | 用途 | 規劃重點 |
|---|---|---|
| GitLab Shell | 處理 SSH 形式的 Git 操作 | SSH 埠（預設 22）與主機 SSH 服務的埠號衝突需事先規劃 |
| GitLab agent server for Kubernetes（KAS） | 與叢集內的 `agentk` 建立反向連線，支援 GitOps 與 CI/CD 存取叢集 | 叢集不需對外開放 API Server；19.x 起需確認 Helm chart 的 KAS Ingress 設定（20.0 將調整相關 chart value） |
| Container Registry（含 metadata database） | 儲存容器映像 | 新版 Registry 以 PostgreSQL metadata database 支援線上垃圾回收；19.0 起已移除 Azure storage driver 與 S3 Signature v2 支援 |
| 進階搜尋（Advanced Search，Elasticsearch／OpenSearch） | 跨專案程式碼與內容搜尋 | 19.2 起 Self-Managed **Ultimate** 需啟用進階搜尋才能取得完整 Ultimate 功能；Elasticsearch 7.x 已於 19.1 停止支援 |
| Redis 或 Valkey | 快取、佇列、Session | 目前建議 Redis 7.2 或 Valkey 7.2；Redis 6 已於 19.0 停止支援 |
| AI Gateway | GitLab Duo 與 Agent Platform 呼叫大型語言模型的閘道 | 雲端連線（Cloud-connected）授權需允許對外連線；離線環境需評估 Duo Self-Hosted／Agent Platform Self-Hosted |

```mermaid
flowchart LR
    Dev[開發者 / AI Agent] -- HTTPS --> Workhorse[Workhorse + Puma]
    Dev -- SSH --> Shell[GitLab Shell]
    Workhorse --> Gitaly[Gitaly]
    Shell --> Gitaly
    Workhorse --> Search[(Advanced Search\nElasticsearch/OpenSearch)]
    Workhorse --> AIGW[AI Gateway\nDuo / Agent Platform]
    KAS[KAS] <-- 反向連線 --> Agentk[agentk\nKubernetes 叢集內]
    Workhorse --> KAS
    Workhorse --> Registry[Container Registry\n+ metadata DB]
```

### ✅ 第二章 Checklist

- [ ] 已理解 Web/API/Sidekiq/PostgreSQL/Redis/Gitaly/Praefect/Object Storage 各元件職責
- [ ] 已確認目前（或預計）使用者規模對應到哪一個 Reference Architecture 分級
- [ ] 已評估 CI/CD 並發量是否會讓 Runner、Gitaly 成為效能瓶頸
- [ ] 已規劃 Object Storage（而非本機磁碟）作為 Artifacts/LFS/Registry 的儲存後端
- [ ] 已以 RPS（而非僅使用者人數）估算容量，並預留 CI/CD 與 AI Agent 的 API 流量
- [ ] 已確認進階搜尋、KAS、Container Registry metadata database 等周邊元件的規劃

---

## 第三章 GitLab 安裝與部署

### 3.1 GitLab CE 與 EE 差異

GitLab 採用 **Open Core** 模式：

- **GitLab CE（Community Edition）**：開源、免費，包含 Git 管理、基本 CI/CD、基本 Issue/MR 功能。
- **GitLab EE（Enterprise Edition）**：在 CE 基礎上加上 Premium / Ultimate 授權功能，例如：進階權限（Protected Environments、Approval Rules）、Epic/Roadmap、GitLab Duo AI 功能、進階安全掃描（DAST、Container Scanning、Dependency Scanning 完整版）、Compliance Framework、Geo 複寫等。

實務上，**GitLab 官方安裝套件（Linux package / Helm Chart / Docker Image）預設安裝的就是 EE 的程式碼**，只是未啟用授權金鑰時功能等同 CE。這代表企業可以先用 CE 等級功能上線，未來只需「貼授權金鑰」即可解鎖 EE 功能，不需要重新安裝。

> ⚠️ **注意事項**：很多企業誤以為「裝 CE 版」未來要升級到 EE 必須重新安裝，其實只要從一開始就用官方 Linux package / Docker Image（內含 EE 程式碼），未來只需在管理後台輸入授權碼即可，無需停機重裝。

### 3.2 Linux Package（Omnibus）安裝 — Ubuntu

以 Ubuntu 24.04 LTS 安裝 GitLab Self-Managed 為例（官方同時支援 22.04 與 26.04；20.04 已於 19.0 停止支援）：

```bash
# 1. 安裝必要套件
sudo apt update
sudo apt install -y curl openssh-server ca-certificates tzdata perl postfix

# 2. 加入 GitLab 官方套件庫（EE，含 CE 全部功能）
curl --location "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh" | sudo bash

# 3. 安裝 GitLab，並指定外部存取網址
sudo EXTERNAL_URL="https://gitlab.example.com" apt install -y gitlab-ee

# 4. 安裝時套件會自動執行 reconfigure；日後修改 /etc/gitlab/gitlab.rb 後再執行下列指令套用設定
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

> 💡 **自訂初始管理員**：安裝時可一併指定 `GITLAB_ROOT_EMAIL` 與 `GITLAB_ROOT_PASSWORD`（至少 8 個字元）環境變數，例如 `sudo GITLAB_ROOT_EMAIL="admin@example.com" GITLAB_ROOT_PASSWORD="<強密碼>" EXTERNAL_URL="https://gitlab.example.com" apt install gitlab-ee`。`/etc/gitlab/initial_root_password` 會在安裝 24 小時後自動刪除，請及時取得並更換密碼。

### 3.3 Linux Package 安裝 — RHEL / AlmaLinux / Oracle Linux

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
curl --location "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh" | sudo bash

# 4. 安裝
sudo EXTERNAL_URL="https://gitlab.example.com" dnf install -y gitlab-ee

# 5. 日後修改 /etc/gitlab/gitlab.rb 後再執行下列指令套用設定
sudo gitlab-ctl reconfigure
```

> 💡 **RHEL/AlmaLinux 注意事項**：SELinux 預設為 Enforcing 模式時，需確認 Nginx/Puma 監聽埠是否被 SELinux policy 擋下；建議用 `sudo ausearch -m avc -ts recent` 檢查是否有被拒絕的存取，再用 `semanage` 開放對應 port/context，而非直接關閉 SELinux。

### 3.4 Docker 安裝

適合 PoC、開發測試環境，正式生產環境建議使用 Linux package 或 Helm Chart（Kubernetes）。映像標籤請固定為明確版本（格式 `<版本>-ee.0`），`latest` 僅適合測試用途；官方不支援 Docker for Windows，映像也不含郵件傳送代理（MTA），需另行設定 SMTP。

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
  gitlab/gitlab-ee:19.4.1-ee.0
```

驗證：

```bash
docker exec -it gitlab gitlab-ctl status
docker logs -f gitlab   # 第一次啟動約需 3-5 分鐘完成 reconfigure
```

亦可使用 `docker-compose.yml`：

```yaml
services:
  gitlab:
    image: gitlab/gitlab-ee:19.4.1-ee.0
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

### 3.5 Podman 安裝（Rootless）

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
  docker.io/gitlab/gitlab-ee:19.4.1-ee.0
```

> ⚠️ **注意事項**：rootless Podman 下，容器內部 GitLab 使用的 UID/GID 會對應到主機上啟動使用者的 subuid/subgid 映射範圍，掛載 Volume 時務必加上 `:Z`（SELinux 標籤重新標記）並確認 `/etc/subuid`、`/etc/subgid` 已配置足夠的 UID 範圍，否則會出現權限被拒（Permission Denied）錯誤。建議改用 Podman 的 **Quadlet**（例如 `~/.config/containers/systemd/gitlab.container`）交由 `systemd --user` 管理，並執行 `loginctl enable-linger <使用者>` 確保開機自動啟動；舊的 `podman generate systemd` 已被 Podman 官方標示為棄用。

驗證安裝（Podman 與 Docker 相同）：

```bash
podman exec -it gitlab gitlab-ctl status
podman exec -it gitlab gitlab-rake gitlab:check SANITIZE=true
```

### 3.6 Helm Chart（Kubernetes）安裝概覽

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

> ⚠️ **v2.0 更正**：自 GitLab 19.0（Helm chart 10.x）起，官方 Helm chart **已移除內建的 Bitnami PostgreSQL、Bitnami Redis 與 MinIO**（這些元件原本就只建議用於 PoC）。正式環境必須如上例改用外部 PostgreSQL 17、Redis／Valkey 與 S3 相容 Object Storage；既有使用內建元件的環境需先依官方「bundled chart migration」指南遷移後才能升級到 19.x。

> 💡 **企業導入建議**：Kubernetes 部署 GitLab 適合已具備成熟 K8s 維運能力（GitOps、HPA、PodDisruptionBudget、StorageClass 規劃）的 Platform 團隊。若團隊尚無 K8s 維運經驗，建議先以 Linux package 方式上線，待團隊能力到位後再評估遷移，避免「為了用 K8s 而用 K8s」造成維運複雜度不降反升。

### 3.7 系統需求（GitLab 19.x）

> 🆕 **v2.0 新增**

**硬體基準（單節點 Linux package）**：

| 資源 | 官方基準 | 說明 |
|---|---|---|
| CPU | 8 vCPU | 支援 ARM 架構；不建議使用可突發（Burstable）執行個體，效能不穩定 |
| 記憶體 | 16 GB | 記憶體受限環境最低可 8 GB 執行，但需依官方「memory-constrained」指南調校；建議關閉 swap |
| 應用節點磁碟 | 40 GB 起 | 套件本身約 2.5 GB，另含作業系統、日誌與暫存檔 |
| Gitaly 磁碟 | 至少等於所有 Repository 總量 | 依成長趨勢預留空間 |
| PostgreSQL 磁碟 | 5～12 GB 起 | 依資料量成長 |
| 檔案系統 | 避免 NFS、Amazon EFS、Azure Files 等網路檔案系統 | 會顯著影響效能 |

**軟體版本需求**：

| 元件 | GitLab 19.x 需求 |
|---|---|
| PostgreSQL | 最低 17.x、最高 17.x（PostgreSQL 16 已於 19.0 停止支援） |
| Helm chart | 10.x |
| Redis／Valkey | Redis 建議 7.2（最低 7.0）；Valkey 7.2 |
| 進階搜尋 | Elasticsearch 8.x 以上或 OpenSearch 2.x 以上（Elasticsearch 7.x 已於 19.1 停止支援；OpenSearch 1.x 已於 18.5 起棄用；確切支援版本以官方 Advanced search 文件為準） |

**官方支援的 Linux package 作業系統（節錄）**：

| 作業系統 | 架構 | 作業系統 EOL |
|---|---|---|
| Ubuntu 22.04／24.04／26.04 | amd64、arm64 | 2027-04／2029-04／2031-04 |
| Debian 11／12／13 | amd64、arm64 | 2026-08／2028-06／2030-06 |
| AlmaLinux 8／9／10 | x86_64、aarch64 | 2029-03／2032-05／2035-05 |
| Red Hat Enterprise Linux 8／9／10 | x86_64、arm64 | 2029-05／2032-05／2035-05 |
| Oracle Linux 8／9／10 | x86_64 | 2029-07／2032-06／2035-06 |
| Amazon Linux 2023 | amd64、arm64 | 2029-06 |

> ⚠️ **注意事項**：Ubuntu 20.04 與 SUSE 系列已於 19.0 停止提供 Linux package，Amazon Linux 2 於 19.1 停止支援；Debian 11 的作業系統 EOL（2026-08）已過，應盡快規劃遷移。Rocky Linux 不在官方支援清單內，雖然多數情況可比照 RHEL 安裝，但企業正式環境建議選用官方列名的發行版，以免影響原廠支援。

### 3.8 安裝後的初始強化設定

> 🆕 **v2.0 新增**

安裝完成只是開始，正式上線前建議由 Platform 與資安團隊共同完成以下強化項目（均可在 **Admin area → Settings** 設定）：

| 類別 | 建議設定 | 目的 |
|---|---|---|
| 帳號註冊 | 關閉公開註冊，或限制允許的 Email 網域並需管理員核准 | 避免外部人員自行建立帳號 |
| 身分驗證 | 串接企業 SSO（SAML／OIDC／LDAP），並強制所有使用者啟用雙因素驗證（2FA） | 降低帳號被盜風險 |
| Token 效期 | 設定 Access Token 最長效期（預設 365 天，17.6 起可由管理員調整上限） | 避免長期有效 Token 外洩後長期被濫用 |
| 預設可見度 | 將新專案與 Group 預設可見度設為 Private | 避免誤將內部程式碼設為 Internal／Public |
| 外部連線 | 依需求設定 Outbound requests 允許清單（Webhook、整合服務） | 防止 SSRF 與資料外洩 |
| 備份 | 設定每日 `gitlab-backup` 與設定檔備份（見第二十章 20.1） | 確保可復原 |
| 監控 | 啟用內建 Prometheus 並接入企業監控（見第二十章 20.2） | 及早發現效能問題 |
| AI 功能 | 依企業 AI 政策決定是否開啟 GitLab Duo、Agent Platform、MCP server，並設定可使用的群組 | 避免未經評估即對外傳送程式碼上下文 |

### ✅ 第三章 Checklist

- [ ] 已確認要安裝 CE 或 EE（建議一律安裝 EE 套件，未授權時等同 CE 功能）
- [ ] 已依作業系統（Ubuntu/RHEL/AlmaLinux/Oracle Linux）完成套件庫設定與安裝
- [ ] 已執行 `gitlab-ctl reconfigure` 並用 `gitlab-ctl status` / `gitlab-rake gitlab:check` 驗證所有服務正常
- [ ] 已取得並妥善保管初始 root 密碼，登入後立即更換
- [ ] 已依環境性質（PoC/正式）選擇 Docker、Podman 或 Helm Chart 安裝方式
- [ ] 已規劃外部 PostgreSQL / Redis / Object Storage（正式環境不建議全部使用容器內建元件）
- [ ] 已確認作業系統在官方支援清單內，且 PostgreSQL 版本為 17.x
- [ ] 已完成 3.8 節的初始強化設定（SSO、2FA、Token 效期、預設可見度、AI 功能開關）

---

## 第四章 GitLab CLI（glab）

### 4.1 glab 是什麼

`glab` 是 GitLab 官方維護的開源命令列工具（專案位於 `gitlab.com/gitlab-org/cli`），讓開發者可以**不離開終端機**完成 Merge Request、Issue、CI/CD、Release 等操作，定位上等同於 GitHub 的 `gh`。對於重度使用終端機、或想將 GitLab 操作整合進 Shell Script／AI Agent 工作流的工程師而言，`glab` 是不可或缺的工具。

`glab` 以 Go 語言撰寫，為單一執行檔、跨平台（Windows／macOS／Linux／FreeBSD），並透過 REST API 與 GraphQL API 與任意 GitLab 實例（GitLab.com、Self-Managed、Dedicated）互動。

| 項目 | 說明 |
|---|---|
| 目前版本 | v1.120.0（2026-09-29） |
| 發布節奏 | 約每週一版（例如 1.118.0、1.119.0、1.120.0 分別於 2026-09-15、09-22、09-29 發布） |
| 官方支援的 GitLab 版本 | GitLab 16.0 以上；部分指令需要更新的 GitLab 版本（例如 `glab duo cli` 需要 19.2 以上） |
| 官方文件 | docs.gitlab.com/cli（由 `glab` 原始碼自動產生，與指令 `--help` 內容一致） |

### 4.2 glab 架構

```mermaid
flowchart LR
    User[👨‍💻 開發者 / CI Job / AI Agent]
    CLI[glab CLI]
    Cfg[(config.yml\n多 Instance 設定)]
    Keyring[(作業系統 Keyring\nToken 安全儲存)]
    REST[GitLab REST API]
    GQL[GitLab GraphQL API]
    Git[本機 Git Repository]
    Bin[受管理的外部執行檔\nGitLab Duo CLI / Orbit CLI]

    User --> CLI
    CLI --> Cfg
    CLI --> Keyring
    CLI -- 大部分指令 --> REST
    CLI -- glab api graphql 等 --> GQL
    CLI -- glab mr checkout / stack 等 --> Git
    CLI -- glab duo cli / glab orbit --> Bin
    REST --> GitLabServer[GitLab Server\nGitLab.com / Self-Managed / Dedicated]
    GQL --> GitLabServer
```

> 💡 **架構重點**：`glab duo cli` 與 `glab orbit` 並非由 `glab` 本身實作功能，而是由 `glab` 下載、驗證並啟動對應的外部執行檔（GitLab Duo CLI、Orbit CLI），同時代為處理認證。因此這兩個指令的子指令與旗標，需以 `glab duo cli help`、`glab orbit --help` 顯示的外部工具說明為準。

### 4.3 glab 主要功能分類

> ⚠️ **v2.0 更正**：初版列出的 `glab project` 指令並不存在；`glab pipeline` 已是棄用別名，官方要求改用 `glab ci`。下表依官方文件列出 v1.120.0 全部 45 個頂層指令（`glab help` 可查看完整清單）。

| 分類 | 指令 | 用途 |
|---|---|---|
| 認證與設定 | `auth`、`config`、`alias`、`completion` | 登入／登出、Docker credential helper、設定值、指令別名、Shell 自動完成 |
| 專案與程式碼 | `repo`、`snippet`、`deploy-key`、`ssh-key`、`gpg-key` | Clone、建立、Fork、封存、成員管理、發布 CI/CD Catalog、金鑰管理 |
| Merge Request | `mr`、`stack` | 建立、審查、核准、合併 MR；以 Stacked Diff 拆分大型變更 |
| 規劃與追蹤 | `issue`、`incident`、`work-items`、`label`、`milestone`、`iteration`、`todo` | Issue／Incident／Work Item 管理、標籤、里程碑、Iteration、待辦 |
| CI/CD | `ci`、`job`、`schedule`、`variable`、`securefile` | Pipeline 觸發與追蹤、Job artifacts、排程、變數、Secure files |
| Runner | `runner`、`runner-controller` | Runner 查詢、暫停、指派；Runner controller（管理員） |
| 發布與套件 | `release`、`changelog`、`packages`、`container-registry`、`artifact-registry` | Release、Changelog、Package registry、容器倉庫、Artifact Registry 認證 |
| 安全與治理 | `security`、`dependency-firewall`、`attestation`、`govern`、`token` | 掃描設定、相依套件防火牆、SLSA 驗證、AI Agent 稽核、Access Token 管理 |
| AI 與 Agent | `duo`、`mcp`、`skills`、`search`、`orbit` | GitLab Duo CLI、MCP server、Agent Skills、語意程式碼搜尋、Orbit 知識圖譜 |
| 基礎設施 | `cluster`、`opentofu` | GitLab agent for Kubernetes、OpenTofu state |
| 通用與工具 | `api`、`user`、`version`、`check-update`、`whatsnew` | 呼叫任意 API、使用者事件、版本資訊與更新檢查 |

### 4.4 glab 指令穩定度分級（Stable / Beta / Experimental）

`glab` 並非每個子指令都已達到正式（GA）等級。官方會在指令說明的第一行標註 `(BETA)` 或 `(EXPERIMENTAL)`，企業導入前應依下表評估風險。

> ⚠️ **v2.0 更正**：初版將 `orbit` 標為 Beta、將 `search` 標為 Stable，均與官方不符；另漏列 `attestation`、`security`、`dependency-firewall`、`govern`、`artifact-registry` 等實驗性指令。

| 穩定度 | 指令（v1.120.0） | 企業導入建議 |
|---|---|---|
| **GA**（未標註） | `auth`、`repo`、`mr`、`issue`、`ci`、`job`、`release`、`variable`、`api`、`schedule`、`runner`、`label`、`milestone`、`token`、`deploy-key`、`packages`、`container-registry`、`incident`、`duo`（`glab duo cli` 啟動的 GitLab Duo CLI 已於 19.2 GA）等 | 可用於生產環境腳本與 CI/CD 自動化 |
| **Beta** | `search`（`glab search semantic`） | 可在非關鍵流程試用；Beta 可能在大版號以外發生 Breaking Change |
| **Experimental** | `mcp`、`stack`、`skills`、`orbit`、`work-items`、`attestation`、`security`、`dependency-firewall`、`govern`、`artifact-registry`、`runner-controller`、`cluster graph`；以及 `auth dpop-gen`、`repo publish catalog`、`release create --publish-to-catalog`、各指令的 `--attach` 旗標 | 官方明確表示「尚未適合正式環境使用，可能隨時變動或移除」，僅建議用於 PoC、個人環境，**不應**寫入正式 CI/CD 或團隊強制流程 |

> ⚠️ **注意事項**：穩定度會隨版本演進改變。建議將「檢查指令狀態」納入 `glab` 升級 SOP，例如在升級後執行 `glab <command> --help | head -1`，確認說明第一行是否仍帶有 `(EXPERIMENTAL)` 或 `(BETA)`。

### 4.5 安裝 glab

> ⚠️ **v2.0 更正**：WinGet 套件 ID 為 `glab.glab`（初版誤寫為 `GitLab.GLab`）；官方 Linux 套件檔名包含版本號，初版的 `permalink/latest/downloads/glab_amd64.deb` 路徑並不存在。

#### Windows

```powershell
# 方式一：WinGet
winget install glab.glab

# 方式二：Scoop
scoop install glab

# 方式三：Chocolatey
choco install glab

# 方式四：從 Releases 頁面下載 glab_<版本>_Windows_x86_64_installer.exe 安裝程式
```

#### macOS

```bash
# Homebrew（官方正式支援的安裝方式）
brew install glab

# MacPorts
sudo port install glab
```

#### Linux

```bash
# Homebrew on Linux（官方正式支援的安裝方式）
brew install glab

# Debian / Ubuntu：下載官方 .deb（檔名含版本號，請替換為實際版本）
GLAB_VERSION=1.120.0
curl -fsSLO "https://gitlab.com/gitlab-org/cli/-/releases/v${GLAB_VERSION}/downloads/glab_${GLAB_VERSION}_linux_amd64.deb"
sudo apt install "./glab_${GLAB_VERSION}_linux_amd64.deb"

# RHEL / AlmaLinux：下載官方 .rpm
curl -fsSLO "https://gitlab.com/gitlab-org/cli/-/releases/v${GLAB_VERSION}/downloads/glab_${GLAB_VERSION}_linux_amd64.rpm"
sudo dnf install "./glab_${GLAB_VERSION}_linux_amd64.rpm"

# 其他社群維護的方式：Snap、mise、asdf、Arch Linux（extra/glab）、Alpine
```

> 💡 **企業內網建議**：官方 Releases 頁面同時提供 `checksums.txt`。企業應由 Platform 團隊下載指定版本、驗證 SHA256 後放入內部套件庫（如 GitLab Generic Package，見第十章 10.6）統一派送，避免每台開發機直接從網際網路下載不同版本。

#### 驗證安裝

```bash
glab version

# 檢查是否有新版（手動執行時一定會檢查；自動檢查每 24 小時最多一次）
glab check-update
```

### 4.6 登入與認證

#### 互動式登入

```bash
glab auth login
```

執行後會依序詢問：

1. GitLab instance（預設 `gitlab.com`，企業自架環境輸入如 `gitlab.example.com`）。
2. 登入方式：
   - **Token**：貼上 Personal Access Token（PAT）。建議只授予 `api` 與 `write_repository` 範圍；若僅需唯讀操作，可改用 `read_api` 與 `read_repository`。
   - **Web（OAuth）**：開啟瀏覽器完成 OAuth 授權，免手動建立 Token。Self-Managed 實例需先由管理員建立 OAuth Application，並在 `glab` 設定 `client_id`。
3. Git 通訊協定（HTTPS 或 SSH）。
4. Container registry 網域（供 Docker credential helper 使用；無 Registry 可輸入 `none`）。

```bash
# 非互動式：直接帶入 Token（注意：Token 會留在 Shell history，僅限測試）
glab auth login --hostname gitlab.example.com --token glpat-xxxxxxxxxxxxxxxxxxxx

# 非互動式：從標準輸入讀取 Token（建議作法）
glab auth login --hostname gitlab.example.com --stdin < ./token.txt

# 無瀏覽器的遠端主機：使用 OAuth 2.0 Device Authorization Flow
glab auth login --hostname gitlab.example.com --device

# 強制使用 Web/OAuth 登入
glab auth login --hostname gitlab.com --web
```

#### Token 儲存位置（Keyring）

`glab auth login` 預設會把 Token 存進作業系統的 Keyring：

| 作業系統 | Keyring |
|---|---|
| macOS | Keychain |
| Windows | Windows Credential Manager |
| Linux | Secret Service（GNOME Keyring、KWallet 等，透過 D-Bus） |

若主機沒有可用的 Keyring、在 CI/CD 中執行，或加上 `--insecure-storage` 旗標，Token 才會以明文存放在設定檔中。

> ⚠️ **注意事項**：伺服器或容器環境通常沒有 Keyring，Token 會以明文寫入 `config.yml`。這類環境建議改用環境變數 `GITLAB_TOKEN`（見 4.7）或 CI/CD Job Token（見 4.8），不要執行 `glab auth login` 留下明文 Token。

#### 檢查登入狀態

```bash
glab auth status            # 目前預設 instance
glab auth status --all      # 所有已設定的 instance
glab auth status --hostname gitlab.example.com
```

#### 多 GitLab Instance 管理

許多企業同時使用 `gitlab.com`（開源專案／外部協作）與自架的 `gitlab.internal.example.com`（內部專案），`glab` 原生支援多個 Instance 並存：

```bash
# 登入第二個 instance
glab auth login --hostname gitlab.internal.example.com

# 在 Git repository 目錄中，glab 會依 git remote 自動判斷要連線的 instance
cd ~/work/order-service && glab mr list

# 不在 repository 目錄中時，以 GITLAB_HOST 或 -R（完整 URL）指定目標
GITLAB_HOST=gitlab.internal.example.com glab issue list -R platform/ci-templates
glab mr list -R https://gitlab.internal.example.com/platform/ci-templates
```

> ⚠️ **v2.0 更正**：`glab mr list` 等一般指令**沒有** `--hostname` 旗標（只有 `glab auth`、`glab api` 等少數指令提供）；跨 instance 操作請使用 `GITLAB_HOST` 環境變數或 `-R` 帶入完整 URL。

### 4.7 設定檔與環境變數

> 🆕 **v2.0 新增**

**設定檔位置**（依序查找）：

| 範圍 | 位置 |
|---|---|
| 指定目錄 | `$GLAB_CONFIG_DIR/config.yml`（有設定 `GLAB_CONFIG_DIR` 時） |
| 使用者（相容舊版，所有平台優先檢查） | `~/.config/glab-cli/config.yml` |
| 使用者（平台預設） | Linux：`~/.config/glab-cli/config.yml`；macOS：`~/Library/Application Support/glab-cli/config.yml`；Windows：`%LOCALAPPDATA%\glab-cli\config.yml` |
| 系統全域 | `/etc/xdg/glab-cli/config.yml` |
| Repository 本地 | `.git/glab-cli/config.yml`（僅對該 repository 生效） |

**常用設定與環境變數**：

| 環境變數 | 對應設定鍵 | 用途 |
|---|---|---|
| `GITLAB_TOKEN` | `token` | 存取 Token；設定後不需 `glab auth login` |
| `GITLAB_HOST` | `host` | 預設 GitLab 主機 |
| `GITLAB_API_HOST` | `api_host` | API 主機與 Git 主機不同時使用 |
| `GLAB_CA_CERT` | `ca_cert` | 企業自簽憑證或私有 CA 的 PEM 檔路徑 |
| `GLAB_CLIENT_CERT`／`GLAB_CLIENT_KEY` | `client_cert`／`client_key` | mTLS 用戶端憑證 |
| `GLAB_PROXY` | `proxy` | 針對特定主機的 Proxy |
| `GLAB_SKIP_TLS_VERIFY` | `skip_tls_verify` | 略過 TLS 驗證（僅限開發環境，正式環境嚴禁） |
| `GLAB_USE_KEYRING` | `use_keyring` | 是否使用作業系統 Keyring |
| `GLAB_ENABLE_CI_AUTOLOGIN` | — | 在 GitLab CI/CD 中自動以 Job Token 登入（見 4.8） |
| `GLAB_CONFIG_DIR` | — | 覆寫設定檔目錄 |
| `GITLAB_CLIENT_ID` | `client_id` | Self-Managed OAuth Application 的 Client ID |

```bash
# 設定企業私有 CA（僅對指定主機生效）
glab config set ca_cert /etc/pki/ca-trust/source/anchors/corp-root-ca.pem --host gitlab.example.com

# 關閉自動檢查更新（企業統一派送版本時）
glab config set check_update false

# 查看設定檔實際路徑
glab config path
```

### 4.8 在 CI/CD 中使用 glab

> 🆕 **v2.0 新增**

在 GitLab CI/CD Job 中使用 `glab`，建議依以下優先順序選擇認證方式：

| 方式 | 設定 | 適用情境 |
|---|---|---|
| CI Job Token 自動登入（建議） | 設定 `GLAB_ENABLE_CI_AUTOLOGIN=true`，`glab` 會使用 `CI_JOB_TOKEN`、`CI_SERVER_FQDN` 等預設變數自動登入 | 建立 Release、讀取同專案資源等 Job Token 允許的操作 |
| 明確以 Job Token 登入 | `glab auth login --job-token $CI_JOB_TOKEN --hostname $CI_SERVER_FQDN --api-protocol $CI_SERVER_PROTOCOL` | 需要明確控制登入流程時 |
| Project／Group Access Token | 以 Masked + Protected 變數注入 `GITLAB_TOKEN` | Job Token 權限不足的操作（例如留言、建立 MR） |

```yaml
release:
  stage: deploy
  image: registry.gitlab.com/gitlab-org/cli:v1.120.0
  variables:
    GLAB_ENABLE_CI_AUTOLOGIN: "true"
  script:
    - glab release create "$CI_COMMIT_TAG" --notes-file CHANGELOG.md -R "$CI_PROJECT_PATH"
  rules:
    - if: '$CI_COMMIT_TAG'
```

> ⚠️ **注意事項**：官方明確提醒**不要**在 Job 中設定 `GITLAB_TOKEN=$CI_JOB_TOKEN`。`glab` 會把 `GITLAB_TOKEN` 當成一般 PAT 送出，導致認證失敗或行為異常。Job Token 請透過自動登入或 `--job-token` 使用。另外，Job Token 只能存取部分 API 端點（官方文件「Job token access」列有清單），且可在專案的 CI/CD 設定中為 Job Token 設定細粒度權限（Fine-grained permissions，18.3 起 GA）。

### 4.9 版本升級與相容性管理

> 🆕 **v2.0 新增**

`glab` 發版頻率高，企業應建立版本治理機制：

1. **固定版本**：CI/CD 映像使用明確版本標籤，開發機由 Platform 團隊統一派送經過驗證的版本。
2. **升級前閱讀 Changelog**：每個 Release 頁面都列有 Features、Bug Fixes、Maintenance；特別注意 `refactor:`、`remove` 等可能影響腳本的變更（例如 v1.120.0 移除了部分指令自訂的 `--project`／`--hostname` 旗標組合）。
3. **回歸測試**：將團隊常用的 `glab` 指令寫成簡單的 Smoke test（例如 `glab mr list -R <測試專案> --output json`），升級後先在測試專案執行。
4. **棄用追蹤**：留意指令說明中的棄用訊息，例如 `glab pipeline`、`glab pipe` 已棄用，應全面改為 `glab ci`。

### ✅ 第四章 Checklist

- [ ] 已在開發機與 CI/CD 執行環境安裝經驗證的 `glab` 版本，並以 `glab version` 確認
- [ ] 已用 Token 或 OAuth 完成登入，並確認 Token 儲存在作業系統 Keyring 而非明文設定檔
- [ ] 若使用多個 GitLab Instance，已理解 `GITLAB_HOST` 與 `-R` 完整 URL 的切換方式
- [ ] 企業自簽憑證環境已設定 `ca_cert`，未使用 `skip_tls_verify` 略過驗證
- [ ] CI/CD 中已改用 `GLAB_ENABLE_CI_AUTOLOGIN` 或 `--job-token`，未硬編碼個人 PAT，也未設定 `GITLAB_TOKEN=$CI_JOB_TOKEN`
- [ ] 已依 4.4 穩定度分級，確認 Experimental 指令未進入正式流程

---

## 第五章 GitLab CLI 指令大全

> 每個指令分類皆說明用途、常用參數、實際範例與最佳實務。所有範例都已依 glab v1.120.0 官方文件核對，請依實際專案、MR、Issue 編號調整後執行。多數指令都支援 `-R, --repo <group/project>` 指定其他專案，以及 `-F, --output json` 輸出 JSON 供腳本處理。
>
> ⚠️ **v2.0 更正**：本章已移除初版中官方不存在的指令與旗標，包括：
>
> - 不存在的指令：`glab project`、`glab runner register`／`pause`／`resume`、`glab duo ask`、`glab search code`／`issues`／`mrs`、`glab orbit local setup`／`remote`
> - 不存在的旗標：`glab mr list --reviewer-state`、`glab stack create --parent`、`glab schedule create --variables`（正確為 `--variable`）
>
> 同時將 `glab pipeline` 全面改為 `glab ci`。

### 5.1 `glab auth` — 認證管理

**用途**：登入、登出、檢查認證狀態，並可作為 Docker credential helper。

| 子指令／參數 | 說明 |
|---|---|
| `glab auth login` | 登入（`--hostname`、`--token`、`--stdin`、`--web`、`--device`、`--job-token`、`--insecure-storage`） |
| `glab auth status` | 檢查登入狀態（`--all` 檢查全部 instance、`--show-token` 顯示 Token） |
| `glab auth logout` | 登出 |
| `glab auth configure-docker` | 將 `glab` 註冊為 Docker credential helper，讓 `docker login` 使用 `glab` 的認證 |
| `glab auth dpop-gen` | 產生 DPoP 證明 JWT，將 PAT 綁定 SSH 私鑰（Experimental） |

```bash
glab auth login --hostname gitlab.com --web
glab auth status --all
glab auth logout --hostname gitlab.com

# 讓 Docker 透過 glab 取得 GitLab Container Registry 認證（免另存密碼）
glab auth configure-docker
```

**最佳實務**：CI/CD 中不要使用 `--web`（CI 環境沒有瀏覽器），改用第四章 4.8 的 Job Token 自動登入；個人電腦則確認 Token 存在作業系統 Keyring。

### 5.2 `glab repo` — 專案管理

**用途**：Clone、建立、Fork、檢視、封存、搜尋專案，以及管理成員與 Mirror。

| 子指令 | 說明 |
|---|---|
| `glab repo clone <project>` | Clone 專案（可用 `-g <group>` 一次 Clone 整個 Group 的專案） |
| `glab repo create [path]` | 建立新專案（`--private`／`--internal`／`--public`、`-g <group>`、`-d <描述>`） |
| `glab repo fork` | Fork 專案 |
| `glab repo view [repo]` | 在終端機檢視專案資訊，或用 `--web` 開啟瀏覽器 |
| `glab repo archive [repo] [dir]` | 下載專案壓縮檔（`--format`、`--sha`） |
| `glab repo members add`／`remove` | 管理專案成員與角色 |
| `glab repo mirror` | 設定 Push／Pull Mirror |
| `glab repo transfer` | 將專案移轉到其他 Namespace |

```bash
# Clone 專案
glab repo clone mygroup/myproject

# 在指定 Group 下建立私有專案並設定描述
glab repo create new-service --group myteam --private --description "訂單服務 API"

# 在瀏覽器開啟目前專案首頁
glab repo view --web

# 新增成員（Developer 角色，並設定到期日）
glab repo members add --username=jane.smith --role=developer --expires-at=2026-12-31
```

**最佳實務**：建立專案時一律搭配 `--group` 與既定的 Namespace 命名規範（見第二十一章），避免專案散落在個人 Namespace 下難以治理；外包或短期成員務必設定 `--expires-at`。

### 5.3 `glab mr` — Merge Request

**用途**：建立、檢視、審查、核准、合併、Checkout Merge Request。

| 子指令 | 說明 |
|---|---|
| `glab mr create` | 建立 MR（`--fill`、`--draft`、`--reviewer`、`--label`、`--auto-merge`、`--squash-before-merge`、`--remove-source-branch`、`--template`） |
| `glab mr list` | 列出 MR（`--assignee`、`--reviewer`、`--label`、`--draft`、`--target-branch`、`--output json`） |
| `glab mr view <id>` | 檢視 MR 細節（`--web` 開啟瀏覽器） |
| `glab mr diff <id>` | 檢視 MR 程式碼差異 |
| `glab mr checkout <id>` | 將本機切換到該 MR 的分支 |
| `glab mr approve <id>`／`revoke <id>` | 核准／撤回核准 |
| `glab mr approvers <id>` | 查看核准規則與目前核准狀態 |
| `glab mr merge <id>` | 合併 MR（`--squash`、`--rebase`、`--remove-source-branch`、`--sha`、`--auto-merge`） |
| `glab mr note create <id>` | 在 MR 留言（`-m`；`--file` 與 `--line` 可針對 Diff 特定行留言；`--internal` 內部留言） |
| `glab mr note resolve`／`list` | 管理討論串 |
| `glab mr rebase <id>` | 觸發伺服器端 Rebase |

```bash
# 建立 MR：指定 reviewer 與 label，合併後刪除來源分支，所有檢查通過後自動合併
glab mr create \
  --title "feat: 新增訂單退款 API" \
  --description "實作退款流程，含單元測試與整合測試" \
  --target-branch main \
  --reviewer alice,bob \
  --label "feature,backend" \
  --remove-source-branch \
  --auto-merge

# 列出需要自己審查的 MR
glab mr list --reviewer=@me

# Checkout 別人的 MR 到本機測試
glab mr checkout 482

# 核准後以 Squash 方式合併，並確認合併的是已審查過的 commit
glab mr approve 482
glab mr merge 482 --squash --remove-source-branch --sha "$(git rev-parse HEAD)"

# 在 MR 留言（CI Pipeline 失敗通知）
glab mr note create 482 -m "⚠️ Pipeline 失敗，請查看 $CI_PIPELINE_URL"

# 針對 Diff 的特定檔案與行號留言
glab mr note create 482 --file src/main/java/OrderService.java --line 58 -m "這裡缺少負數邊界檢查"
```

**最佳實務**：

- `glab mr create --fill` 會依 commit 資訊自動帶入標題與描述，並**自動 push 分支**（`--fill` 會將 push 設為 true），適合搭配 Conventional Commits 使用。
- 搭配 `--draft` 建立草稿 MR，待 Pipeline 全綠且自我審查完成後才轉為 Ready。
- 合併時使用 `--sha` 可確保「只合併已審查過的 commit」，避免審查後又被推入未審查的變更。

### 5.4 `glab issue` — Issue 管理

**用途**：建立、檢視、更新、關閉、訂閱 Issue，以及管理 Issue Board。

```bash
# 建立 Issue 並指定 Milestone、標籤、負責人
glab issue create \
  --title "登入頁面在 Safari 出現版面錯位" \
  --description "重現步驟：...
預期結果：...
實際結果：..." \
  --label "bug,frontend" \
  --milestone "2026-Q4" \
  --assignee carol

# 列出所有開啟中且帶 bug 標籤的 Issue（預設只列開啟中的 Issue）
glab issue list --label bug

# 列出指派給自己的 Issue，輸出 JSON 供腳本處理
glab issue list --assignee=@me --output json

# 在 Issue 留言並關閉
glab issue note 215 -m "已於 MR !482 修復"
glab issue close 215
```

**最佳實務**：在 commit message 或 MR 描述中使用 `Closes #215`，對應 MR 合併到預設分支後 Issue 會自動關閉，減少手動操作與遺漏。

### 5.5 `glab ci` 與 `glab job` — CI/CD 操作

> ⚠️ **v2.0 更正**：`glab pipeline` 與 `glab pipe` 已是棄用別名，官方要求改用 `glab ci`；`glab pipeline ci view` 這種寫法並不存在。

**用途**：觸發、檢視、重跑、取消 Pipeline，即時追蹤 Job 輸出，驗證 `.gitlab-ci.yml`，下載 Job artifacts。

| 子指令 | 說明 |
|---|---|
| `glab ci list` | 列出 Pipeline（`--ref`、`--status`、`--source`、`--output json`） |
| `glab ci view [branch]` | 以互動式 TUI 檢視 Pipeline 與 Job（可在畫面中重跑、取消、查看 Log） |
| `glab ci status` | 顯示目前分支最新 Pipeline 狀態（`--live` 即時更新、`--wait` 等待結束） |
| `glab ci get` | 以文字／JSON 取得 Pipeline 詳細資訊（`--pipeline-id`、`--merge-request`、`--with-job-details`） |
| `glab ci run` | 手動觸發 Pipeline（`--branch`、`--variables KEY:VALUE`、`--input KEY:VALUE`、`--mr`） |
| `glab ci retry <job-id\|job-name>` | 重跑指定 Job |
| `glab ci cancel pipeline`／`job` | 取消 Pipeline 或 Job |
| `glab ci trace <job-id\|job-name>` | 即時追蹤 Job Log |
| `glab ci lint` | 驗證 CI 設定（`--dry-run` 模擬建立 Pipeline、`--include-jobs` 列出會產生的 Job） |
| `glab ci config compile` | 展開 `include`、`extends` 後輸出完整設定 |
| `glab job artifact <ref> <job>` | 下載指定分支最新 Pipeline 中某個 Job 的 artifacts |

```bash
# 列出 main 分支最近失敗的 Pipeline
glab ci list --ref main --status failed

# 即時追蹤目前分支 Pipeline 狀態，直到結束
glab ci status --live

# 以互動式 TUI 檢視目前分支 Pipeline
glab ci view

# 針對 develop 分支手動觸發 Pipeline，並帶入變數與 CI/CD inputs
glab ci run --branch develop --variables "DEPLOY_ENV:staging" --input "environment:staging"

# 重跑目前分支失敗的 unit-test Job，並追蹤其 Log
glab ci retry unit-test
glab ci trace unit-test

# 以模擬建立 Pipeline 的方式驗證 CI 設定，並列出會產生的 Job
glab ci lint --dry-run --include-jobs

# 下載 main 分支最新 build Job 的 artifacts
glab job artifact main build --path artifacts/
```

**最佳實務**：本機開發時用 `glab ci status --live` 或 `glab ci view` 取代「不斷重新整理瀏覽器看 Pipeline 進度」；提交前先跑 `glab ci lint --dry-run`，可在推送前發現 `rules`、`include` 等錯誤。

### 5.6 `glab release` — 版本發布

```bash
# 建立 Release 並上傳建置產物（檔案可加上 #顯示名稱）
glab release create v2.3.0 \
  --name "v2.3.0 - 訂單模組重構" \
  --notes-file ./CHANGELOG-2.3.0.md \
  --milestone "2026-Q4" \
  './build/order-service-2.3.0.jar#Order Service JAR'

# 對既有 Release 追加附件
glab release upload v2.3.0 ./dist/*.tar.gz

# 列出歷史版本、下載附件
glab release list
glab release download v2.3.0
```

**最佳實務**：

- 在 `tag` Pipeline 中自動執行 `glab release create`（見第四章 4.8 範例），確保每次發版的 Release Note 與實際合併內容一致。
- GitLab 官方已將 CI/CD `release` 關鍵字的執行工具由 `release-cli` 遷移到 `glab`，新的範本應直接使用 `registry.gitlab.com/gitlab-org/cli` 映像。
- `--use-package-registry` 可將附件上傳到專案的 Generic Package Registry，讓附件與 Release 一起受權限與保留政策管理。

### 5.7 `glab variable` — CI/CD 變數管理

```bash
# 新增 Project 層級變數（Masked + Protected，並加上說明）
glab variable set DEPLOY_TOKEN "xxxxxxxx" --masked --protected --description "Production 部署用"

# 新增僅限 production 環境使用的變數
glab variable set DB_URL "jdbc:postgresql://prod-db:5432/app" --scope production --masked

# 新增 Group 層級變數，讓子專案共用
glab variable set DOCKER_REGISTRY_URL "registry.example.com" --group mygroup

# 列出、取得、匯出、刪除變數
glab variable list
glab variable get DOCKER_REGISTRY_URL --group mygroup
glab variable export --output json
glab variable delete DEPLOY_TOKEN
```

**最佳實務**：

- 機密一律加上 `--masked`；只供 Protected Branch／Tag 使用的變數加上 `--protected`，避免 Feature Branch 也能讀到生產環境機密。
- 需要連 UI 都不可檢視值的機密可使用 `--hidden`。
- 以 `--scope` 限定環境。
- `glab variable export` 會輸出變數值，執行結果不可存入版本控制或 CI Log。

### 5.8 專案層級管理：`label`、`milestone`、`iteration`

> ⚠️ **v2.0 更正**：初版的 `glab project` 指令並不存在。專案層級設定請使用下列專屬指令，或以 `glab api` 呼叫對應 REST 端點。

```bash
# 建立標準化標籤（可寫成腳本，於新專案建立時統一套用）
glab label create --name "priority::high" --color "#D9534F" --description "高優先"
glab label list

# 建立專案或 Group 層級 Milestone
glab milestone create --title "2026-Q4" --due-date "2026-12-31"
glab milestone create --title "FY27 Planning" --due-date "2027-01-31" --group 456

# 查詢 Iteration（類似 Sprint）
glab iteration list -g mygroup
```

> 💡 **企業導入建議**：Approval Rules、Protected Environments、Push Rules 等細部設定目前沒有專屬子指令，可透過 `glab api` 呼叫 REST 端點（見 5.9），或以 Compliance Framework、Security Policy 集中治理（見第十九章）。

### 5.9 `glab api` — 通用 API 呼叫

**用途**：當 `glab` 沒有對應子指令時，直接呼叫任意 REST 或 GraphQL 端點，是最具彈性的「萬用指令」。端點中可使用 `:id`、`:fullpath`、`:branch`、`:group`、`:namespace`、`:repo`、`:user`、`:username` 等預留位置，`glab` 會依目前目錄的 repository 自動替換。

| 參數 | 說明 |
|---|---|
| `-X, --method` | HTTP 方法（預設 GET；**只要帶了參數就會自動改成 POST**） |
| `-f, --raw-field` | 以字串型別加入參數 |
| `-F, --field` | 依格式自動轉型（數字、布林、`@檔案`） |
| `--paginate` | 自動抓取所有分頁 |
| `--output ndjson` | 以每行一筆 JSON 輸出，方便搭配 `jq` 串流處理 |
| `--input <file>` | 以檔案（或 `-` 代表 stdin）作為完整 Request Body |

```bash
# REST：取得專案的 Approval Rules
glab api projects/:id/approval_rules

# REST：建立 Protected Branch 規則（帶參數時自動為 POST）
glab api projects/:id/protected_branches \
  -f name="release/*" \
  -F push_access_level=40 \
  -F merge_access_level=30

# GraphQL：查詢專案各嚴重程度的漏洞數量
glab api graphql -f query='
query {
  project(fullPath: "mygroup/myproject") {
    vulnerabilitySeveritiesCount { critical high medium low }
  }
}'

# 分頁取得所有開啟中的 MR（GET 查詢參數請直接寫在 URL，勿用 --field，否則會變成 POST）
glab api "projects/:id/merge_requests?state=opened" --paginate --output ndjson | jq -r '.title'
```

> ⚠️ **v2.0 更正**：初版範例 `glab api projects/:id/merge_requests --paginate --field state=opened` 會因為 `--field` 而自動改用 POST，變成「建立 MR」的請求並失敗；查詢條件應寫在 URL 查詢字串中。

**最佳實務**：將常用的 `glab api` 查詢封裝成 Shell function 或 `glab alias`（見 5.26），存放在團隊共用的工具 repository，避免每次重新查 API 文件拼湊端點。除錯時可設定 `GLAB_DEBUG_HTTP=1` 顯示完整 Request／Response。

### 5.10 `glab duo` — GitLab Duo CLI

> ⚠️ **v2.0 更正**：`glab duo ask` 已不存在。目前的 `glab duo` 只有 `cli` 一個子指令，用來安裝與啟動 **GitLab Duo CLI（`duo`）**，把 GitLab Duo Agent Platform 帶到終端機；`glab` 負責處理認證。

**前提條件**：

- GitLab 19.2 以上（18.11～19.1 需開啟 Beta 與實驗功能）。
- 已執行 `glab auth login`。
- 符合 GitLab Duo Agent Platform 的授權與前置條件（見第十三章）。
- 已設定預設 Duo Namespace，或在具有 GitLab Duo 權限的專案中執行。
- Self-Managed／Dedicated 需由管理員開啟「GitLab Duo CLI access」（預設開啟）。

```bash
# 安裝 GitLab Duo CLI 執行檔（不啟動）
glab duo cli --install

# 開啟互動式工作階段（支援 build 與 plan 模式）
glab duo cli

# Headless 模式：執行單一目標後結束，適用於 Runner、腳本與自動化流程
glab duo cli run --goal "找出這個專案中所有未處理的 NullPointerException 風險並提出修正"

# 查看 GitLab Duo CLI 本身的指令與旗標；檢查並安裝更新
glab duo cli help
glab duo cli --update
```

詳細的授權模型、Agent Platform 與治理建議請見第十三章。

### 5.11 `glab mcp` — 啟動本機 MCP Server

> ⚠️ **v2.0 更正**：`glab mcp serve` 為 **Experimental**，且**只支援 stdio transport**。初版中的 `--transport http --port`、`--read-only`、`--tools` 旗標皆不存在。GitLab 官方建議的 HTTP 端點是 GitLab 伺服器內建的 MCP server（`https://<gitlab>/api/v4/mcp`），兩者差異見第十六章 16.2。

```bash
# 以 stdio transport 啟動，由 AI 工具（如 Claude Code）以子行程方式呼叫
glab mcp serve
```

Claude Code 的設定範例（官方文件提供）：

```json
{
  "mcpServers": {
    "glab": {
      "type": "stdio",
      "command": "glab",
      "args": ["mcp", "serve"]
    }
  }
}
```

提供的工具涵蓋 Issue、MR、專案、CI/CD Pipeline 與 Job 的查詢與操作，使用 `glab` 目前登入的身分與權限。

### 5.12 `glab stack` — Stacked Diff 管理

**用途**：管理「一連串互相依賴、依序疊加」的多個小型 MR（Stacked Diff），讓大型功能可拆成多個易審查的小 MR，同時維護彼此的相依關係。狀態：**Experimental**。

| 子指令 | 說明 |
|---|---|
| `glab stack create <name>` | 建立新的 stack（中繼資料存於 `.git/stacked/`） |
| `glab stack save` | 將已 stage 的變更存成 stack 中的下一層（`-a` 自動 stage、`-m` 描述） |
| `glab stack amend` | 修改目前這一層 |
| `glab stack list`、`next`、`prev`、`first`、`last`、`move`、`switch` | 檢視與切換 stack 中的各層 |
| `glab stack reorder` | 重新排序各層 |
| `glab stack sync` | 推送變更、Rebase 後續各層，並替尚未建立 MR 的分支建立 MR |
| `glab stack delete` | 刪除 stack |

```bash
# 建立 stack，完成第一層變更後存檔（-a 自動 stage 已追蹤檔案）
glab stack create add-order-refund
glab stack save -a -m "新增退款資料模型"

# 繼續開發第二層並存檔
glab stack save -a -m "新增退款 API"

# 推送並自動為每一層建立 MR，同時指定 reviewer 與 label
glab stack sync --reviewer alice --label "feature"

# base 分支更新後，將整個 stack Rebase 到最新 main
glab stack sync --update-base
```

**最佳實務**：大型重構（如第十八章的 Framework 升級）非常適合用 Stacked Diff 拆解，避免單一 MR 動輒上千行造成審查品質下降。由於仍為 Experimental，建議先在小範圍團隊試行，並用 `glab config set branch_prefix <前綴>` 統一分支命名。

### 5.13 `glab search` — 語意程式碼搜尋

> ⚠️ **v2.0 更正**：目前 `glab search` 只有 `semantic` 子指令（**Beta**），以自然語言進行語意程式碼搜尋；初版的 `glab search code`、`issues`、`mrs` 並不存在。跨專案搜尋 Issue／MR 請改用 `glab issue list --search`、`glab mr list --search` 或 `glab api search`。

```bash
# 以自然語言搜尋目前專案中與「認證中介層」相關的程式碼
glab search semantic -q "authentication middleware"

# 限定目錄，並以 JSON 輸出
glab search semantic -q "退款金額計算" -d src/main/java/ --output json

# 搜尋其他專案，限制回傳筆數
glab search semantic -q "rate limiting" -R mygroup/order-service --limit 5

# 關鍵字搜尋 Issue 與 MR
glab issue list --search "退款失敗"
glab mr list --search "資料庫遷移"
```

> 💡 **前提**：專案需透過 GitLab Duo 啟用語意程式碼搜尋（Semantic code search）。

### 5.14 `glab schedule` — Pipeline 排程管理

```bash
# 建立每天凌晨 2 點（台北時間）執行的排程 Pipeline
glab schedule create \
  --description "Nightly Regression Test" \
  --ref main \
  --cron "0 2 * * *" \
  --cronTimeZone "Asia/Taipei" \
  --variable "TEST_SUITE:regression"

# 列出所有排程
glab schedule list

# 立即執行某個排程（不等到下次 cron 時間）
glab schedule run 12
```

> 💡 `--cronTimeZone` 預設為 `UTC`，台灣團隊請明確設定 `Asia/Taipei`，避免排程在非預期時間執行。

### 5.15 `glab runner` — Runner 管理

> ⚠️ **v2.0 更正**：`glab runner` 不提供註冊功能（初版的 `glab runner register` 不存在）。Runner 註冊請在 GitLab UI 或 API 建立 Runner 取得 `glrt-` Token 後，於 Runner 主機執行 `gitlab-runner register`（見第八章）；暫停／恢復改用 `glab runner update --pause`／`--unpause`。

```bash
# 列出目前專案、Group 或整個 instance 的 Runner
glab runner list
glab runner list --group mygroup --output json

# 查看 Runner 正在執行的 Job
glab runner jobs 88 --status running

# 暫停／恢復 Runner（不接收新 Job，不影響執行中的 Job）
glab runner update 88 --pause
glab runner update 88 --unpause

# 將 Runner 指派給其他專案
glab runner assign 88 -R mygroup/payment-service
```

詳細安裝與維運請見第八章。

### 5.16 `glab orbit` — Orbit 知識圖譜

**用途**：透過 `glab` 執行受管理的 **Orbit CLI**，查詢 GitLab Orbit（Knowledge Graph）建立的程式碼關聯圖，協助開發者與 AI Agent 理解「這個函式被誰呼叫」「這個服務依賴哪些上游 API」等語意層級問題。狀態：**Experimental**。

> ⚠️ **v2.0 更正**：`glab orbit` 為 Experimental（初版誤標為 Beta）。所有子指令與旗標都原封不動轉交給 Orbit CLI，初版的 `glab orbit local setup`、`glab orbit remote --query` 並非官方語法。

**前提條件**：已執行 `glab auth login`；該 Namespace 已啟用 Orbit（功能旗標 `knowledge_graph`）。

```bash
# 將 Orbit 連接到本機的 Coding Agent（或以 uninstall 還原）
glab orbit setup

# 查詢遠端 Orbit 圖譜（自動使用 glab 的認證）
glab orbit status
glab orbit graph-status --full-path mygroup/order-service
glab orbit query ./query.json

# 在本機建立並搜尋程式碼圖譜
glab orbit index .
glab orbit grep "processRefund"

# 查看 Orbit CLI 本身的說明；安裝或更新受管理的執行檔
glab orbit --help
glab orbit --update
```

> ⚠️ **注意事項**：Orbit 需要在伺服器端針對 Namespace 啟用功能旗標，且索引建立會消耗額外運算資源。導入前請先與 Platform 團隊確認，詳細概念請見第十六章 16.6。

### 5.17 `glab skills` — Agent Skills 管理

**用途**：安裝 `glab` 內建的 Agent Skills（`SKILL.md` 檔案），讓 AI Agent 學會如何正確使用 `glab`。Skills 遵循 Agent Skills 規格，可被 GitLab Duo Agent Platform、Claude Code、Codex、Gemini CLI 等相容的 Agent 讀取。狀態：**Experimental**。

```bash
# 列出 glab 內建的所有 Skills
glab skills list

# 安裝核心 glab Skill 到目前專案（寫入 .agents/skills/）
glab skills install

# 安裝指定的 Skill（例如 glab-stack）
glab skills install glab-stack

# 安裝到使用者層級（~/.agents/skills/）
glab skills install --global

# 更新已安裝的 Skills
glab skills update
```

> ⚠️ **v2.0 更正**：`glab skills` 安裝的是 `glab` 隨附的 Skills，並非從遠端技能市集下載；初版的 `glab skills install gitlab/mr-create-flow` 並不存在。

**最佳實務**：將 `.agents/skills/` 納入版本控制，並在 `AGENTS.md`／`CLAUDE.md` 中說明（見第十四章），確保新成員與 CI 環境的 Agent 使用同一套 Skills。

### 5.18 `glab attestation` — 軟體供應鏈驗證

**用途**：驗證由 GitLab CI/CD 建置的產物是否帶有合法的 SLSA Provenance 簽署，確認產物確實來自預期的專案與 Pipeline。狀態：**Experimental**，**目前僅適用於 GitLab.com**，且需要先安裝 `cosign`。

```bash
# 驗證 gitlab-org/gitlab 專案產出的 filename.txt
glab attestation verify gitlab-org/gitlab filename.txt

# 以專案 ID 驗證
glab attestation verify 123 ./dist/order-service-2.3.0.jar
```

> ⚠️ **v2.0 更正**：正確語法為 `glab attestation verify <project-id> <artifact-path>`，初版的 `--signing-key` 旗標並不存在。

> 💡 **企業導入建議**：在部署前的 Pipeline Stage 中驗證產物來源，作為軟體供應鏈安全的關卡，並搭配第十一章的 Container Scanning 共同把關。Self-Managed 環境目前無法使用本指令，可改以 `cosign verify-attestation` 搭配企業自建的簽署基礎設施。

### 5.19 `glab cluster` — Kubernetes Agent 管理

**用途**：管理 GitLab agent for Kubernetes，包含 Flux 引導、取得 kubeconfig、檢視叢集物件圖。

```bash
# 列出專案已註冊的 Kubernetes Agent
glab cluster agent list

# 以 Flux 引導 Agent（manifest 路徑需與 flux bootstrap 的 --path 一致）
glab cluster agent bootstrap my-agent --manifest-path manifests/

# 透過 Agent 更新本機 kubeconfig（不需直接存取叢集 API Server）
glab cluster agent update-kubeconfig --agent 123 --use-context

# 檢視叢集物件關聯圖（Experimental）
glab cluster graph --agent 123 --core --apps -n production
```

### 5.20 `glab container-registry` — 容器倉庫管理

**用途**：在終端機管理 Container Registry 的 repository 與 tag（別名 `glab cr`）。

```bash
# 列出專案或 Group 下所有 repository（取得 repository ID）
glab container-registry repository list
glab container-registry repository list --group mygroup

# 列出某個 repository 的所有 tag
glab container-registry tag list 123

# 刪除單一 tag
glab container-registry tag delete 123 pr-1234-test

# 批次刪除：刪除符合 pr-* 且超過 7 天的 tag，但保留最新 5 個（非同步執行）
glab container-registry tag delete 123 --name-regex-delete "pr-.*" --older-than 7d --keep-n 5
```

> ⚠️ **v2.0 更正**：`tag list`／`tag delete` 的參數是 **repository ID**（數字），不是映像名稱；刪除單一 tag 直接給 tag 名稱，初版的 `--tag-name` 旗標並不存在。

詳細的 Registry 治理策略（Cleanup Policy、Image Promotion）請見第九章。

### 5.21 `glab incident` — 事件管理

**用途**：在終端機處理 Incident，適合值班工程師處理告警時，不需切換到瀏覽器即可記錄處理過程。

```bash
# 列出開啟中的 Incident（預設只列開啟中）
glab incident list

# 留言記錄處理進度，並關閉 Incident
glab incident note 58 -m "已確認為 Redis 連線池耗盡，已擴容處理"
glab incident close 58
```

### 5.22 `glab work-items` — Work Item 管理

**用途**：管理 Work Item。GitLab 正逐步把 Issue、Epic、Task、Objective／Key Result 等規劃物件統一為 Work Item 資料模型。狀態：**Experimental**。

```bash
# 列出目前專案開啟中的 Work Item（可用 --type 篩選）
glab work-items list --type task

# 在 Group 建立 Epic 類型的 Work Item
glab work-items create --group mygroup --type epic --title "訂單系統現代化"

# 在專案建立 Task
glab work-items create --type task --title "重構訂單退款流程"

# 更新 Work Item 描述
glab work-items update 42 --description-file description.md
```

> ⚠️ **注意事項**：GitLab 已以 Work Item 模型實作 Epic。舊的 Epics REST API 未來將被取代，新的自動化建議直接使用 Work Items（GraphQL 或 `glab work-items`）。由於 `glab work-items` 仍為 Experimental，正式自動化前請先在測試 Group 驗證。

### 5.23 Token 與金鑰：`token`、`deploy-key`、`ssh-key`、`gpg-key`

> 🆕 **v2.0 新增**

```bash
# 建立專案 Access Token（Developer 角色、read_repository + read_registry、30 天）
glab token create --access-level developer --scope read_repository --scope read_registry ci-reader --duration 30d

# 建立 Group Access Token
glab token create --group platform --access-level maintainer --scope api platform-bot --duration 90d

# 列出與輪替 Token（輪替會產生新 Token 並使舊 Token 失效）
glab token list --output json
glab token rotate ci-reader --duration 30d

# 撤銷 Token
glab token revoke ci-reader

# 新增唯讀 Deploy Key（給部署主機拉取程式碼）
glab deploy-key add ~/.ssh/deploy_ed25519.pub --title "prod-deploy-host"

# 將個人 SSH 公鑰與 GPG 公鑰上傳到帳號
glab ssh-key add ~/.ssh/id_ed25519.pub --title "Work Laptop"
glab gpg-key add ./my-gpg-public-key.asc
```

> 💡 **企業導入建議**：以 `glab token list --output json` 搭配排程 Pipeline，定期盤點即將到期或權限過大的 Token；以 `glab token rotate` 自動化輪替，比人工在 UI 操作更可稽核。

### 5.24 CI/CD 周邊：`securefile`、`packages`、`opentofu`、`changelog`

> 🆕 **v2.0 新增**

```bash
# 上傳 CI/CD Secure File（如 Android keystore、簽章憑證）
glab securefile create "release.keystore" ./secrets/release.keystore
glab securefile list

# 上傳檔案到專案 Package Registry（Generic Package）
glab packages upload ./build/app.zip --name order-tools --version 1.0.0
glab packages list --name order-tools

# 管理 GitLab 託管的 OpenTofu state（別名 terraform、tf）
glab opentofu state list
glab opentofu state lock production

# 依 .gitlab/changelog_config.yml 產生 Changelog
glab changelog generate --version 2.3.0
```

### 5.25 安全與治理（Experimental）：`security`、`dependency-firewall`、`govern`、`artifact-registry`

> 🆕 **v2.0 新增**。本節指令皆為 **Experimental**，僅建議在 PoC 環境評估。

```bash
# 查看／啟用專案的安全掃描設定檔（需 Maintainer 或 Security Manager 角色）
glab security config status dependency_scanning
glab security config enable sast -R mygroup/order-service

# 透過 GitLab Dependency Firewall 執行套件管理工具，依專案政策阻擋或標記有風險的套件
glab dependency-firewall npm install left-pad
glab dependency-firewall maven verify

# 設定本機的 AI Agent 治理（於 ~/.claude/settings.json 安裝 Stop/SessionEnd hook，將 Agent 工作階段同步為 GitLab 稽核事件）
glab govern setup
glab govern doctor

# 以 GitLab 身分換取短效 Artifact Registry Token，設定 Docker／Maven／Gradle／npm 認證
glab artifact-registry login --maven --registry https://ar.example.com --duration 2h
```

> 💡 **企業導入建議**：
>
> - `glab govern` 讓外部 AI Agent（目前以 Claude Code 為主）的工作階段留下 GitLab 稽核軌跡，適合需要稽核 AI 使用情況的金融、醫療產業評估。
> - `dependency-firewall` 則把供應鏈防護延伸到開發者本機。
> - 兩者都在快速演進中，請持續追蹤官方文件。

### 5.26 個人效率：`alias`、`config`、`completion`、`todo`、`user`

> 🆕 **v2.0 新增**

```bash
# 建立指令別名（支援 $1 等位置參數）
glab alias set mrv 'mr view'
glab alias set myissues 'issue list --assignee=@me'
glab alias list

# 安裝 Shell 自動完成（bash / zsh / fish / powershell）
glab completion -s bash > /etc/bash_completion.d/glab

# 個人待辦與活動紀錄
glab todo list --action=assigned
glab todo done 123
glab user events --output json
```

### 5.27 完整指令速查（v1.120.0）

| 指令 | 狀態 | 用途 |
|---|---|---|
| `alias` | GA | 建立、列出、刪除指令別名 |
| `api` | GA | 呼叫任意 REST／GraphQL API |
| `artifact-registry` | Experimental | 以 GitLab 身分換取 Artifact Registry 短效 Token |
| `attestation` | Experimental | 驗證 SLSA Provenance（僅 GitLab.com） |
| `auth` | GA | 登入、登出、狀態、Docker credential helper |
| `changelog` | GA | 產生 Changelog |
| `check-update` | GA | 檢查 `glab` 新版本（別名 `update`） |
| `ci` | GA | Pipeline 與 Job 操作（取代已棄用的 `pipeline`） |
| `cluster` | GA（`graph` 為 Experimental） | GitLab agent for Kubernetes |
| `completion` | GA | Shell 自動完成腳本 |
| `config` | GA | `glab` 設定值 |
| `container-registry` | GA | 容器倉庫 repository／tag 管理（別名 `cr`） |
| `dependency-firewall` | Experimental | 透過相依套件防火牆執行套件管理工具 |
| `deploy-key` | GA | Deploy Key 管理 |
| `duo` | GA | 安裝與啟動 GitLab Duo CLI |
| `govern` | Experimental | AI Agent 治理與稽核同步 |
| `gpg-key` | GA | GPG 金鑰管理 |
| `incident` | GA | Incident 管理 |
| `issue` | GA | Issue 與 Issue Board 管理 |
| `iteration` | GA | Iteration 查詢 |
| `job` | GA | 下載 Job artifacts |
| `label` | GA | 標籤管理 |
| `mcp` | Experimental | 以 stdio 啟動 MCP server |
| `milestone` | GA | 里程碑管理 |
| `mr` | GA | Merge Request 管理 |
| `opentofu` | GA | OpenTofu state 管理（別名 `terraform`、`tf`） |
| `orbit` | Experimental | 執行 Orbit CLI |
| `packages` | GA | Package Registry 上傳、下載、列出、刪除 |
| `release` | GA | Release 管理 |
| `repo` | GA | 專案管理、成員、Mirror、CI/CD Catalog 發布 |
| `runner` | GA | Runner 查詢、暫停、指派、刪除 |
| `runner-controller` | Experimental | Runner controller 管理（管理員） |
| `schedule` | GA | Pipeline 排程 |
| `search` | Beta | 語意程式碼搜尋 |
| `securefile` | GA | CI/CD Secure Files |
| `security` | Experimental | 安全掃描設定檔 |
| `skills` | Experimental | 安裝 `glab` 內建 Agent Skills |
| `snippet` | GA | 建立 Snippet |
| `ssh-key` | GA | SSH 金鑰管理 |
| `stack` | Experimental | Stacked Diff |
| `todo` | GA | 待辦事項 |
| `token` | GA | Personal／Project／Group Access Token 管理 |
| `user` | GA | 使用者活動事件 |
| `variable` | GA | CI/CD 變數 |
| `version` | GA | 顯示版本 |
| `whatsnew` | GA | 顯示版本更新說明 |
| `work-items` | Experimental | Work Item 管理 |

### ✅ 第五章 Checklist

- [ ] 團隊已建立常用 `glab` 指令的內部速查表（可參考第二十三章附錄）
- [ ] 既有腳本中的 `glab pipeline` 已全部改為 `glab ci`，並移除本章列出的不存在指令與旗標
- [ ] CI/CD Pipeline 中已善用 `glab mr`、`glab release` 自動化日常流程（建立 MR、發版）
- [ ] 機密一律透過 `glab variable set --masked --protected`（必要時加上 `--hidden`）管理，未硬編碼於程式或 YAML
- [ ] 對於 CLI 尚未支援的設定，已掌握以 `glab api` 呼叫 REST／GraphQL 的方式，並了解 `--field` 會自動改為 POST
- [ ] 已依第四章 4.4 的穩定度分級，確認 Experimental 指令（如 `mcp`、`stack`、`skills`、`orbit`、`work-items`）僅限於非關鍵流程

---

## 第六章 GitLab Flow

### 6.1 三種主流分支策略比較

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

### 6.2 GitLab Flow 的兩種變體

#### 6.2.1 Environment Branch 模式

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

#### 6.2.2 Release Branch 模式

適合需要同時維護多個正式發行版本（如企業軟體需支援舊版 Patch）的專案：

- 每次發版從 `main` 切出 `release/x.y.0` 分支。
- Hotfix 直接在 `release/x.y.0` 上修復，並 cherry-pick 回 `main`。
- 適合搭配第二十一章 21.5 的 Release Strategy，以及 6.4 節的合併方式設定。

### 6.3 企業建議

> 💡 **企業導入建議**：
> - **新創 / 持續部署的 SaaS 產品**：建議採用 GitHub Flow 或 GitLab Flow 的 Environment Branch 模式，簡化流程、加快交付速度。
> - **需同時維護多個正式發行版本（如賣斷制軟體、Library/SDK）**：建議採用 GitLab Flow 的 Release Branch 模式，方便針對舊版本獨立 Hotfix。
> - **避免直接套用傳統 Git Flow**：develop 分支與 main 分支長期並存容易產生「分支漂移」（兩邊程式碼長期不同步），在高頻率部署的現代 CI/CD 環境下維護成本過高，建議僅在維護週期長、發版頻率低（如每季一次）的傳統專案中保留使用。

> ⚠️ **實戰案例**：某保險業核心系統團隊原採用 Git Flow，develop 與 release 分支長期分歧，每次發版前都要花 2-3 天處理合併衝突。改採 GitLab Flow（Release Branch 模式）並搭配第七章的 `rules` 設定後，發版前置作業降至半天內，且 Hotfix 可直接從對應 release 分支發布，不需等待下個大版本。

### 6.4 合併方式與 Merge Train

> 🆕 **v2.0 新增**

分支策略決定「程式碼怎麼流動」，合併方式則決定「主線歷史長什麼樣子、合併前驗證到什麼程度」。GitLab 專案可在 **Settings → Merge requests** 選擇合併方式：

| 合併方式 | 歷史樣貌 | 適用情境 |
|---|---|---|
| Merge commit | 每次合併產生一個 merge commit，保留分支結構 | 需要完整保留分支脈絡的傳統專案 |
| Merge commit with semi-linear history | 來源分支必須先 Rebase 到最新目標分支才能合併，仍產生 merge commit | 兼顧可讀性與「合併前一定跑過最新程式碼」 |
| Fast-forward merge | 不產生 merge commit，主線呈直線 | 追求線性歷史的團隊（常搭配 Squash） |

**Merged results pipelines 與 Merge Train（Premium／Ultimate）**：

- **Merged results pipeline**：MR Pipeline 會以「來源分支合併到目標分支後的結果」執行，而不是只測來源分支本身，能提早發現「各自測試都通過、合併後卻失敗」的情況。
- **Merge Train**：多個 MR 排隊合併時，每個 MR 的 Pipeline 都會包含排在它前面的 MR 變更；只有全部通過才依序合併，避免高頻合併時主線被破壞。

```mermaid
flowchart LR
    MR1[MR !101] --> T1[Train 車廂 1\nmain + !101]
    MR2[MR !102] --> T2[Train 車廂 2\nmain + !101 + !102]
    MR3[MR !103] --> T3[Train 車廂 3\nmain + !101 + !102 + !103]
    T1 -- 通過 --> M1[合併 !101]
    T2 -- 通過 --> M2[合併 !102]
    T3 -- 通過 --> M3[合併 !103]
```

> 💡 **企業導入建議**：每日合併量超過數十個 MR、且主線經常「莫名其妙」壞掉的團隊，優先開啟 Merged results pipelines，再評估 Merge Train。Merge Train 會增加 Pipeline 執行次數，需同步規劃 Runner 容量（見第八章）。

### ✅ 第六章 Checklist

- [ ] 已依專案性質（持續部署 vs 多版本維護）選定適合的分支策略
- [ ] 團隊已建立分支命名規範（如 `feature/*`、`release/*`、`hotfix/*`）
- [ ] 已確認 CI/CD `rules` 設定與所選分支策略一致（見第七章）
- [ ] 已建立 Hotfix 流程文件，明確規定如何 cherry-pick 回主線
- [ ] 已選定合併方式（Merge commit／Semi-linear／Fast-forward），並評估是否啟用 Merged results pipelines 與 Merge Train

---

## 第七章 CI/CD

### 7.1 `.gitlab-ci.yml` 核心概念

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

#### 基礎結構範例

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

#### Stages / Jobs / Rules

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

#### Artifacts 與 Cache

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

#### Rules 進階條件

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

#### Environment 與 Deployment

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

> ⚠️ **v2.0 更正**：初版範例在 Job 層級同時使用 `rules` 與 `when: manual`，GitLab 會以「`when` 不可與 `rules` 同時使用」拒絕該設定。`when: manual` 必須寫在 `rules` 的條件之內，如上所示。

> 💡 **最佳實務**：正式環境部署一律搭配 `when: manual` + Protected Environment（Premium／Ultimate，可指定允許部署的角色或群組，並可要求部署核准），確保只有被授權人員可觸發「部署」，並留下稽核紀錄（誰、何時執行）。

### 7.2 Java / Spring Boot 完整 CI/CD 範例

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
  image: docker:29
  services:
    - docker:29-dind
  script:
    - docker build -t "$IMAGE_TAG" .
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker push "$IMAGE_TAG"
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

deploy-staging:
  stage: deploy
  image: alpine:3.22
  script:
    - apk add --no-cache kubectl
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

### 7.3 Node.js / Vue 完整 CI/CD 範例

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
  image: alpine:3.22
  script:
    - apk add --no-cache aws-cli
    - aws s3 sync dist/ s3://static-assets-bucket/order-frontend --delete
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

### 7.4 React 完整 CI/CD 範例

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
  image: docker:29
  services:
    - docker:29-dind
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

FROM nginx:1.29-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
```

### 7.5 Python 完整 CI/CD 範例

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

### 7.6 `include` 拆分與共用範本

大型企業通常會將通用的 Pipeline 邏輯抽成共用範本，存放在獨立的 `ci-templates` 專案，各專案透過 `include` 引用，確保安全掃描、部署流程一致且易於統一升級：

```yaml
include:
  - project: 'platform/ci-templates'
    ref: v3.2.0
    file: '/templates/java-spring-boot.yml'
  - project: 'platform/ci-templates'
    ref: v3.2.0
    file: '/templates/security-baseline.yml'
  - local: '.gitlab-ci/deploy.yml'
```

> 💡 `include: project` 的 `ref` 建議固定為 Tag（如 `v3.2.0`）而非 `main`，否則範本任何變更都會立即影響所有引用的專案。新的共用範本建議直接改寫為 **CI/CD Component**（見 7.7），可獲得版本化、輸入參數驗證與 CI/CD Catalog 探索等能力。

> 💡 **企業導入建議**：將安全掃描（SAST/Secret Detection）、品質門檻（Code Coverage 最低標準）、部署核准流程等「治理規則」放進 Platform 團隊維護的共用範本，各應用團隊只需 `include`，既保證合規一致性，又不需要每個團隊重複造輪子。修改範本時透過 Semantic Version 的 `ref`（如 `ref: v3.2.0`）控制升級節奏，避免不預期的 Breaking Change。

### 7.7 CI/CD Components 與 CI/CD Catalog

> 🆕 **v2.0 新增**

**CI/CD Component** 是 GitLab 官方推薦的「可重用 Pipeline 設定單位」（Free／Premium／Ultimate 皆可使用）。相較於傳統 `include: project` 範本，Component 具備語意化版本、輸入參數（inputs）驗證，並可發布到 **CI/CD Catalog** 供全公司搜尋與重用。

**Component 專案結構**：

```text
security-components/
├── templates/
│   ├── secret-detection.yml          # 單檔 Component：名稱為 secret-detection
│   └── java-build/
│       └── template.yml              # 目錄型 Component：名稱為 java-build
├── README.md
└── .gitlab-ci.yml                    # 測試並發布 Component 的 Pipeline
```

**Component 定義（`templates/java-build/template.yml`）**：

```yaml
spec:
  inputs:
    stage:
      default: build
    jdk_version:
      default: "21"
      options: ["17", "21"]
      description: "建置使用的 JDK 版本"
---
"java-build":
  stage: $[[ inputs.stage ]]
  image: maven:3.9-eclipse-temurin-$[[ inputs.jdk_version ]]
  script:
    - mvn -B package -DskipTests
  artifacts:
    paths:
      - target/*.jar
```

**使用端引用**：

```yaml
include:
  - component: $CI_SERVER_FQDN/platform/security-components/java-build@1.2.0
    inputs:
      stage: build
      jdk_version: "21"
  - component: $CI_SERVER_FQDN/platform/security-components/secret-detection@~latest
```

**版本引用方式**：

| 寫法 | 意義 | 建議 |
|---|---|---|
| `@1.2.0` | 固定到完整語意化版本 | 正式專案首選，可重現 |
| `@1.2`、`@1` | 部分版本，取該範圍內最新發布版 | 接受相容更新時使用 |
| `@~latest` | CI/CD Catalog 中最新發布版（可能含 Breaking Change） | 僅限測試或內部工具 |
| `@<commit SHA>` 或分支名 | 指定 Git 參照 | Component 開發測試用 |

> 💡 **企業導入建議**：Platform 團隊把「安全掃描基線、建置、部署」拆成 Component 並發布到 CI/CD Catalog，應用團隊以固定版本引用。Component 專案本身的 `.gitlab-ci.yml` 應包含「引用自己最新 SHA 並驗證 Job 被正確加入」的測試，再以 Tag 觸發 Release 發布新版本。

### 7.8 CI/CD inputs 與 Pipeline 參數化

> 🆕 **v2.0 新增**

除了 Component，一般的 `.gitlab-ci.yml` 與被 `include` 的檔案也可以宣告 `spec:inputs`，取代過去大量依賴 CI/CD 變數傳參的作法：

```yaml
spec:
  inputs:
    environment:
      options: ["staging", "production"]
      default: staging
    e2e_mode:
      options: ["never", "manual", "on_success"]
      default: "never"
      description: "E2E 測試的執行方式"
---
deploy:
  stage: deploy
  script:
    - ./deploy.sh "$[[ inputs.environment ]]"
  environment:
    name: $[[ inputs.environment ]]

e2e-test:
  stage: test
  script:
    - npm run test:e2e
  rules:
    - when: $[[ inputs.e2e_mode ]]
```

inputs 在 Pipeline 建立時就會以文字方式展開，因此可以直接控制 `when`、`stage`、`image` 等關鍵字。手動觸發時可在 UI 選擇 inputs，或使用 `glab ci run --input "environment:production" --input "e2e_mode:on_success"`（見第五章 5.5）。

| 比較 | CI/CD 變數 | CI/CD inputs |
|---|---|---|
| 解析時機 | Job 執行期間 | Pipeline 建立時（設定展開階段） |
| 型別與驗證 | 皆為字串，無驗證 | 支援 `string`、`number`、`boolean`、`array`，可用 `options`、`regex` 驗證 |
| 可影響範圍 | Job 內的指令與部分關鍵字 | 幾乎所有設定（Job 名稱、stage、image、rules） |
| 適合用途 | 機密、環境相關設定 | 範本參數、Pipeline 行為開關 |

### 7.9 進階流程控制：`needs`、`parallel:matrix`、Parent-Child Pipeline

> 🆕 **v2.0 新增**

```yaml
stages: [build, test, deploy]

build-backend:
  stage: build
  script: ["mvn -B package -DskipTests"]

build-frontend:
  stage: build
  script: ["npm ci", "npm run build"]

# needs：只等 build-backend 完成即開始，不必等整個 build stage
test-backend:
  stage: test
  needs: ["build-backend"]
  script: ["mvn -B test"]

# parallel:matrix：一次展開多種組合平行執行
test-matrix:
  stage: test
  needs: []
  image: node:$NODE_VERSION-alpine
  parallel:
    matrix:
      - NODE_VERSION: ["20", "22", "24"]
  script: ["npm ci", "npm test"]

# Parent-child pipeline：Monorepo 依模組觸發子 Pipeline
trigger-payment:
  stage: deploy
  trigger:
    include: services/payment/.gitlab-ci.yml
    strategy: depend
  rules:
    - changes:
        - services/payment/**/*
```

| 功能 | 解決的問題 |
|---|---|
| `needs` | 以 DAG 取代嚴格的 Stage 順序，縮短整體 Pipeline 時間 |
| `parallel:matrix` | 多版本、多平台測試不需複製貼上多個 Job |
| `trigger` + `strategy: depend` | Monorepo 拆分子 Pipeline，並讓父 Pipeline 狀態反映子 Pipeline 結果 |
| `rules:changes` | 只在相關檔案變更時執行，節省 Runner 資源 |

### 7.10 以 OIDC ID Token 取代長效雲端密鑰

> 🆕 **v2.0 新增**

把雲端帳號的長效 Access Key 存成 CI/CD 變數是最常見的機密外洩來源之一。GitLab 支援在 Job 中產生 **OIDC ID Token**（Free／Premium／Ultimate 皆可），讓雲端平台或 HashiCorp Vault 以「信任 GitLab 簽發的短效 JWT」方式授權，完全不需要在 GitLab 保存雲端密鑰：

```yaml
deploy-aws:
  stage: deploy
  image:
    name: amazon/aws-cli:latest
    entrypoint: [""]
  id_tokens:
    AWS_ID_TOKEN:
      aud: https://gitlab.example.com
  script:
    - >
      export $(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s"
      $(aws sts assume-role-with-web-identity
      --role-arn "$AWS_ROLE_ARN"
      --role-session-name "gitlab-$CI_PROJECT_ID-$CI_PIPELINE_ID"
      --web-identity-token "$AWS_ID_TOKEN"
      --duration-seconds 3600
      --query 'Credentials.[AccessKeyId,SecretAccessKey,SessionToken]'
      --output text))
    - aws s3 ls
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

> 💡 **企業導入建議**：
>
> - 在雲端 IAM 信任政策中，以 ID Token 的 `sub` 聲明（包含專案路徑與分支，例如 `project_path:mygroup/order-service:ref_type:branch:ref:main`）限制**只有特定專案的特定分支**可以取得角色，避免任何專案都能冒用。
> - 同一模式可套用到 GCP Workload Identity Federation、Azure Workload Identity 與 Vault JWT 認證。

### 7.11 Pipeline 效能與成本最佳化

> 🆕 **v2.0 新增**

| 手法 | 做法 | 預期效益 |
|---|---|---|
| 避免重複 Pipeline | 以 `workflow:rules` 控制「MR Pipeline」與「Branch Pipeline」只擇一建立 | Runner 用量可能減半 |
| DAG 化 | 以 `needs` 讓不相依的 Job 提早開始 | 縮短等待時間 |
| 精準觸發 | `rules:changes` 搭配 Monorepo 路徑 | 只跑受影響模組 |
| Cache 設計 | `cache:key:files` 以 lockfile 雜湊為 Key；讀多寫少的 Job 使用 `policy: pull` | 減少重複下載 |
| Artifacts 控管 | 設定 `expire_in`，只保留必要檔案 | 降低 Object Storage 成本 |
| 可中斷 Job | 設定 `interruptible: true`，並在專案開啟「自動取消多餘 Pipeline」 | 新 commit 推入時自動取消舊 Pipeline |
| 映像最佳化 | 使用輕量、固定版本的映像，並搭配 Dependency Proxy 或 Virtual Registry 快取 | 加快 Job 啟動、避免 Docker Hub 限流 |

```yaml
workflow:
  auto_cancel:
    on_new_commit: interruptible
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH && $CI_OPEN_MERGE_REQUESTS'
      when: never
    - if: '$CI_COMMIT_BRANCH'

default:
  interruptible: true
```

### ✅ 第七章 Checklist

- [ ] 已理解 `stages` / `jobs` / `rules` / `artifacts` / `cache` / `environment` 各自用途，未混用 cache 與 artifacts
- [ ] 已依語言/框架選用對應的 CI/CD 範本，並確認 Docker 多階段建置已套用（縮小最終 Image 體積）
- [ ] 正式環境部署已設定 `when: manual` + Protected Environment
- [ ] 已評估是否需要建立共用 `ci-templates` 專案統一治理規則
- [ ] Pipeline 中所有機密皆透過 CI/CD Variables 注入，未寫死於 YAML
- [ ] 共用 Pipeline 邏輯已評估改寫為 CI/CD Component，並以固定版本引用
- [ ] 雲端部署已改用 OIDC ID Token，未在 CI/CD 變數存放長效雲端密鑰
- [ ] 已設定 `workflow:rules` 避免重複 Pipeline，並啟用 `interruptible` 自動取消

---

## 第八章 GitLab Runner

### 8.1 Runner 類型總覽

| 類型 | 範圍 | 適用情境 |
|---|---|---|
| Instance Runner（舊稱 Shared Runner） | GitLab Instance 全域共用 | 中小型團隊、輕量工作負載，由 Platform 團隊統一維運 |
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

### 8.2 安裝 GitLab Runner

#### Linux（裸機/VM，Docker Executor）

```bash
# 1. 加入官方套件庫（官方建議先下載腳本、檢查內容後再執行）
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" -o script.deb.sh
less script.deb.sh
sudo bash script.deb.sh

# 2. 安裝 GitLab Runner
sudo apt install gitlab-runner

# 3. 註冊：先在 GitLab UI（專案／Group 的 Settings → CI/CD → Runners，或 Admin area → CI/CD → Runners）
#    或透過 API 建立 Runner，取得 glrt- 開頭的 Runner Authentication Token，再於 Runner 主機執行：
sudo gitlab-runner register \
  --non-interactive \
  --url https://gitlab.example.com \
  --token glrt-xxxxxxxxxxxxxxxxxxxx \
  --executor docker \
  --docker-image alpine:3.22
```

> ⚠️ **v2.0 更正**：使用 Runner Authentication Token 時，Runner 的描述、Tags、是否 Protected、是否執行未標記 Job 等屬性，都在 GitLab UI／API **建立 Runner 時**設定，不能再於 `gitlab-runner register` 指定（初版的 `--description` 旗標在新流程中無效）。舊的 Registration Token 流程自 GitLab 17.0 起預設停用，官方不建議重新啟用。

> 💡 **版本對應**：Runner 版本應與 GitLab 伺服器的 major.minor 版本保持一致（例如 GitLab 19.4 搭配 Runner 19.4.x）。

#### Kubernetes（Helm Chart）

```bash
helm repo add gitlab https://charts.gitlab.io
helm repo update

helm upgrade --install gitlab-runner gitlab/gitlab-runner \
  --namespace gitlab-runner --create-namespace \
  -f runner-values.yaml
```

`runner-values.yaml`（Token 建議改用 `runners.secret` 參照預先建立的 Kubernetes Secret，而非寫在檔案中）：

```yaml
gitlabUrl: https://gitlab.example.com
runnerToken: glrt-xxxxxxxxxxxxxxxxxxxx
concurrent: 20
rbac:
  create: true
runners:
  config: |
    [[runners]]
      [runners.kubernetes]
        namespace = "{{.Release.Namespace}}"
        image = "alpine:3.22"
```

#### 驗證

```bash
sudo gitlab-runner verify
sudo gitlab-runner status

# 在 GitLab 後台 CI/CD Settings → Runners 確認 Runner 顯示為「綠燈」(Online)
glab api projects/:id/runners
```

### 8.3 設定要點

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

### 8.4 維護、升級、故障排除

**維護**：

```bash
# 查看目前所有已註冊 Runner 與其忙碌狀態
glab api runners/all

# 暫停 Runner（不接收新 Job，但不影響執行中的 Job）
glab runner update 88 --pause
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

### 8.5 Runner 自動擴縮與 Executor 選型

> 🆕 **v2.0 新增**

| Executor／機制 | 擴縮方式 | 狀態與建議 |
|---|---|---|
| Kubernetes executor | 每個 Job 建立一個 Pod，搭配叢集 Cluster Autoscaler／Karpenter 擴縮節點 | 雲原生環境首選 |
| Docker Autoscaler executor | 透過 **Fleeting** 外掛（AWS、Google Cloud、Azure 等）依負載建立／回收 VM，每台 VM 內以 Docker 執行 Job | 取代 Docker Machine 的官方方案 |
| Instance executor | 同樣使用 Fleeting 外掛，Job 直接在自動建立的 VM 上執行（不使用 Docker） | 需要完整 VM 權限的建置（例如建置 VM 映像） |
| Docker Machine executor | 以 GitLab 維護的 Docker Machine fork 建立 VM | **17.5 起棄用，預定於 GitLab 20.0（2027-05）移除**，僅修正重大問題，應儘速遷移 |

```mermaid
flowchart LR
    GitLab[GitLab Server] -- 派發 Job --> Mgr[Runner Manager\ndocker-autoscaler]
    Mgr -- Fleeting 外掛 --> Cloud[雲端 Auto Scaling Group / VM Scale Set]
    Cloud --> VM1[VM 1\nDocker]
    Cloud --> VM2[VM 2\nDocker]
    Cloud --> VMn[VM N\nDocker]
```

> ⚠️ **注意事項**：仍在使用 Docker Machine executor 的企業，應在 2026 年內完成 Docker Autoscaler 的 PoC 與遷移計畫，避免升級到 GitLab 20.0 時 Runner 自動擴縮失效。大型 Runner Fleet 的管理員也可評估 `glab runner-controller`（Experimental）管理 Runner controller。

### 8.6 Runner 安全強化

> 🆕 **v2.0 新增**

Runner 會執行任何有權限推送程式碼的人所寫的腳本，是 CI/CD 供應鏈攻擊的主要目標。建議：

| 風險 | 強化措施 |
|---|---|
| 未受信任的程式碼竊取正式環境機密 | 將部署用 Runner 設為 **Protected**（只執行 Protected Branch／Tag 的 Job），並與一般建置 Runner 分開 |
| 任意 Job 被派到敏感 Runner | 關閉敏感 Runner 的「Run untagged jobs」，以 `tags` 明確指定 |
| `privileged` Docker-in-Docker 可取得主機權限 | Instance Runner 避免開啟 `privileged`；容器建置改用 Rootless BuildKit 或 Buildah（Kaniko 已由原維護者封存，不建議新導入） |
| Runner Token 外洩 | 使用 `glrt-` Runner Authentication Token 並定期輪替；Legacy Registration Token 自 17.0 起預設停用，不應重新啟用 |
| Shell executor 缺乏隔離 | 僅在高度信任的內部環境使用，並以專用低權限帳號執行 |
| Job 之間互相污染 | Kubernetes executor 為每個 Job 使用獨立 Pod；Docker executor 避免共用可寫入的主機 Volume |

### ✅ 第八章 Checklist

- [ ] 已依團隊規模選定 Instance/Group/Project Runner 範圍策略
- [ ] 已依工作負載特性選定 Kubernetes/Docker/Shell Executor
- [ ] `concurrent` 與資源限制（cpu/memory request/limit）已依主機容量合理設定
- [ ] 已設定 S3 相容的分散式 Cache，而非僅依賴單機本地快取
- [ ] 已建立 Runner 監控告警（Online/Offline、Job 排隊時間）
- [ ] 仍在使用 Docker Machine executor 者，已排定遷移至 Docker Autoscaler 或 Kubernetes executor 的時程（20.0 前完成）
- [ ] 部署用 Runner 已設為 Protected，且未對 Instance Runner 開啟 `privileged`

---

## 第九章 Container Registry

### 9.1 GitLab Container Registry 概念

GitLab 內建 **Docker/OCI 相容的 Container Registry**，每個專案預設即擁有自己的 Registry 命名空間（`registry.example.com/group/project`），無需額外部署 Harbor 或 Docker Registry。

```mermaid
flowchart LR
    CI[CI/CD Job\ndocker build] -->|docker push| Registry[(GitLab Container Registry)]
    Registry -->|docker pull| K8s[Kubernetes Cluster]
    Registry -->|docker pull| LocalDev[本機開發環境]
    SecurityScan[Container Scanning] -.掃描.-> Registry
```

### 9.2 基本操作

```bash
# 登入 Registry（CI/CD Job 中可用 CI_REGISTRY_USER / CI_REGISTRY_PASSWORD 自動注入）
# 以 stdin 傳入 Token，避免密碼留在 Shell history 與程序清單；或執行 glab auth configure-docker 由 glab 代管認證
echo "$GITLAB_TOKEN" | docker login registry.example.com -u <username> --password-stdin

# Build 並標記 Image
docker build -t registry.example.com/mygroup/order-service:1.4.0 .

# Push
docker push registry.example.com/mygroup/order-service:1.4.0

# 透過 glab 查看 Registry 內的 Image 清單
glab container-registry repository list
```

CI/CD 中的標準範例：

```yaml
build-image:
  stage: package
  image: docker:29
  services:
    - docker:29-dind
  script:
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" -t "$CI_REGISTRY_IMAGE:latest" .
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
    - docker push "$CI_REGISTRY_IMAGE:latest"
```

### 9.3 Image 掃描（Container Scanning）

```yaml
include:
  - template: Jobs/Container-Scanning.gitlab-ci.yml

container_scanning:
  variables:
    CS_IMAGE: "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

Container Scanning 以 Trivy 掃描映像，並可偵測已終止支援（EOL）的作業系統。Free／Premium 可執行掃描並下載 JSON 與 CycloneDX SBOM 報告；**Ultimate** 才會在 MR 的 Security Widget 與 Pipeline 的 Security 分頁列出 CVE 編號、嚴重程度（Critical/High/Medium/Low）與建議修復版本，並提供自動修補建議（見第十一章 11.1 的方案層級對照表）。

### 9.4 Image Promotion（多環境晉升流程）

企業常見作法是「同一個 Image 從測試晉升到生產，不重新建置」，避免 Build 環境差異造成的不一致：

```yaml
promote-to-production:
  stage: deploy
  image: docker:29
  services:
    - docker:29-dind
  script:
    - docker pull "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
    - docker tag "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" "$CI_REGISTRY_IMAGE:production-$CI_COMMIT_SHORT_SHA"
    - docker push "$CI_REGISTRY_IMAGE:production-$CI_COMMIT_SHORT_SHA"
  environment:
    name: production
  rules:
    - if: '$CI_COMMIT_TAG'
      when: manual
```

> 💡 更進一步的作法是改用 `crane copy`、`skopeo copy` 或 `docker buildx imagetools create` 直接在 Registry 之間複製或加上標籤，不需要在 Job 中 pull／push 整個映像，也不需要 Docker-in-Docker。

### 9.5 最佳實務

- **使用不可變標籤（Immutable Tag）**：以 Commit SHA 或語意化版本作為 Tag，避免使用 `latest` 部署到生產環境（無法追溯確切版本）。
- **定期清理舊 Image**：設定 Container Registry 的 **Cleanup Policy**（依保留天數/數量自動清除過期 Tag），避免 Object Storage 用量無限增長。
- **最小化 Base Image**：優先使用 `alpine` 或 `distroless` 映像，縮小攻擊面並加速 Pull 速度。
- **Image 簽章驗證**：對高合規需求的企業，建議搭配 Cosign 對 Image 進行簽章，並在部署前驗證簽章。

```bash
# Cleanup Policy 設定範例（透過 API，以 JSON 作為 Request Body）
cat <<'EOF' | glab api --method PUT projects/:id --input - -H "Content-Type: application/json"
{
  "container_expiration_policy_attributes": {
    "enabled": true,
    "cadence": "1d",
    "keep_n": 10,
    "older_than": "30d",
    "name_regex": ".*",
    "name_regex_keep": "^v\\d+\\.\\d+\\.\\d+$"
  }
}
EOF
```

> 💡 **Protected tags**：對 `v*` 等正式版本標籤設定 Container Registry 的保護規則，可避免被 Cleanup Policy 或權限不足的成員誤刪。

> ⚠️ **注意事項**：Container Registry 的實際儲存空間計算在 Object Storage 用量內，企業若未設定 Cleanup Policy，常見半年內 Registry 用量暴增到數百 GB，務必在第二十章維運手冊中將 Registry 用量監控納入告警項目。

### 9.6 Container Virtual Registry（聚合上游倉庫）

許多企業同時使用 Docker Hub、Harbor、Quay 等多個外部容器倉庫，工程師在本機或 CI/CD 中常需要分別設定多組登入憑證與 Pull 規則，管理成本高且容易因外部倉庫的 Rate Limit（如 Docker Hub 匿名拉取限制）導致 Pipeline 不穩定。

**Container Virtual Registry**（Premium／Ultimate，目前為 **Beta**，GitLab.com 與 Self-Managed 可用）讓 GitLab 扮演「聚合層」的角色：將多個上游倉庫註冊為單一虛擬倉庫的來源，開發者與 CI/CD 只需對接 GitLab 一個端點，即可透明地拉取來自不同上游的映像，同時所有流量會經過 GitLab 的快取與存取控制。

```bash
# 1. 在頂層 Group 建立 Container Virtual Registry（每個 Group 最多 5 個）
glab api --method POST "groups/<group-id>/-/virtual_registries/container/registries" \
  -f name="shared-upstreams" -f description="公用基礎映像快取"

# 2. 為該 Virtual Registry 新增 Docker Hub 上游（每個 Virtual Registry 最多 5 個上游；帳密需同時提供或都不提供）
glab api --method POST "virtual_registries/container/registries/<registry-id>/upstreams" \
  -f name="Docker Hub" -f url="https://registry-1.docker.io" -F cache_validity_hours=24
```

> ⚠️ **v2.0 更正**：初版的 API 路徑 `groups/:id/virtual_registries/packages/container` 與參數 `upstream_url` 均不正確，正確路徑與參數如上（依官方 Container virtual registries API）。

> 💡 **企業導入建議**：將常用的公共基礎映像（如 `nginx`、`postgres`、`eclipse-temurin`）統一透過 Virtual Registry 快取，可同時達到「降低對外流量與 Rate Limit 風險」與「對所有 Image 統一套用第 11 章的 Container Scanning」兩個目的，避免團隊各自從外部來源直接拉取未經掃描的映像。

### 9.7 多架構 Image 支援（Multi-Architecture）

隨著企業逐步導入 ARM 架構的運算資源（如 AWS Graviton、Apple Silicon 開發機），單一映像只支援 x86_64 已不足夠。GitLab Container Registry 支援以 **Manifest List（OCI Image Index）** 的形式，將同一個 Tag 對應到多個 CPU 架構的映像，讓 `docker pull` 時自動依執行環境選擇正確的版本：

```bash
# 使用 buildx 建置並推送同時支援 amd64/arm64 的多架構映像
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag registry.example.com/order-service:1.4.0 \
  --push .

# 在 GitLab UI 可看到同一個 Tag 下列出對應的多個平台；glab 需以 repository ID 查詢
glab container-registry tag list <repository-id>
```

> ⚠️ **注意事項**：多架構映像會讓單一 Tag 對應的儲存空間倍增（每個架構各占一份），務必搭配 9.5 的 Cleanup Policy 一併規劃保留策略；CI/CD Runner 若僅有 x86_64 執行環境，需另外規劃具備 ARM Executor 的 Runner（見第八章）才能完成多架構建置。

### ✅ 第九章 Checklist

- [ ] 已使用不可變標籤（Commit SHA / SemVer），未在生產部署使用 `latest`
- [ ] 已設定 Container Scanning 並納入 MR 合併門檻（Critical 漏洞需阻擋合併）
- [ ] 已設定 Cleanup Policy 定期清除過期 Image
- [ ] 已評估多環境 Image Promotion 流程，避免重複建置造成環境差異
- [ ] 已評估是否需要透過 Container Virtual Registry 聚合外部上游倉庫，降低 Rate Limit 風險
- [ ] 若有 ARM/多架構運算需求，已規劃多架構映像建置與對應的儲存保留策略
- [ ] 正式版本 Tag 已設定保護規則，避免被 Cleanup Policy 或非授權成員刪除

---

## 第十章 Package Registry

### 10.1 支援的套件格式總覽

GitLab Package Registry 原生支援多種套件管理生態系，企業可用單一平台整合 Nexus／Artifactory 的部分用途。各格式的官方成熟度不同，導入前請確認：

| 格式 | 官方狀態 | 用途 |
|---|---|---|
| Maven（含 `mvn`、`gradle`） | GA | Java／Kotlin 函式庫與內部共用模組 |
| npm（pnpm、Yarn 可相容使用） | GA | JavaScript／TypeScript 套件 |
| NuGet | GA | .NET 函式庫 |
| PyPI | GA | Python 套件 |
| Helm | GA | Kubernetes Helm Chart |
| Generic packages | GA | 任意二進位檔案（如內部工具、韌體、報表檔） |
| Terraform module registry | GA | 內部 Terraform／OpenTofu 模組 |
| Composer、Conan 1／Conan 2 | Beta | PHP、C/C++ 套件 |
| Debian、Go、Ruby gems | Experiment | 不建議用於正式環境 |

> ⚠️ **v2.0 更正**：初版把 Gradle、pnpm 列為獨立格式；實際上 Gradle 使用 Maven 格式、pnpm 使用 npm 格式。Conda、CRAN、RPM、Swift 目前尚未支援。

### 10.2 Maven 設定與發布

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

### 10.3 npm / pnpm 設定與發布

`.npmrc`：

```ini
@mygroup:registry=https://gitlab.example.com/api/v4/packages/npm/
//gitlab.example.com/api/v4/packages/npm/:_authToken=${CI_JOB_TOKEN}
```

```bash
npm publish
# 或 pnpm publish（語法相同，pnpm 原生相容 npm registry 協定）
```

### 10.4 NuGet 發布

```bash
dotnet nuget add source "https://gitlab.example.com/api/v4/projects/${CI_PROJECT_ID}/packages/nuget/index.json" \
  --name gitlab --username gitlab-ci-token --password "$CI_JOB_TOKEN" --store-password-in-clear-text

dotnet pack -c Release
dotnet nuget push "bin/Release/*.nupkg" --source gitlab
```

### 10.5 PyPI 發布

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

### 10.6 Generic Package（任意檔案）

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

### 10.7 相依套件來源治理：Maven Virtual Registry 與 Dependency Firewall

> 🆕 **v2.0 新增**

企業使用開源套件時，除了「發布自己的套件」，更重要的是「控管從外部拉進來的套件」：

| 能力 | 狀態／層級 | 用途 |
|---|---|---|
| Virtual Registry（Maven、Container images） | Beta，Premium／Ultimate；建立於頂層 Group | 把 Maven Central 等多個上游聚合為單一端點，統一快取與存取控制，並依設定的上游順序解析 |
| Dependency Proxy for container images | GA | 快取 Docker Hub 映像，降低外部限流風險 |
| Dependency Firewall（`glab dependency-firewall`） | Experimental | 在開發者本機執行 `npm`、`maven`、`pip`、`gradle` 等工具時，依專案政策阻擋或標記有風險的套件（見第五章 5.25） |
| Dependency Scanning（SBOM） | Ultimate | 在 Pipeline 中比對已知漏洞與惡意套件公告（19.4 新增惡意套件公告比對） |

> ⚠️ **注意事項**：GitLab 已公告 **Dependency Proxy for packages** 將於 20.0 移除，已在使用者應改用 Virtual Registry。導入 Virtual Registry 時需注意：每個頂層 Group 有 Virtual Registry 與上游數量上限，且目前仍為 Beta。

### ✅ 第十章 Checklist

- [ ] 已評估是否可用 GitLab Package Registry 取代既有的 Nexus/Artifactory，降低維運系統數量
- [ ] CI/CD 發布套件皆使用 `CI_JOB_TOKEN`，未使用個人 PAT
- [ ] 已建立內部共用套件的版本命名與發布規範（SemVer）
- [ ] 已設定 Package Registry 的存取權限，避免外部成員下載內部專屬套件
- [ ] 已評估以 Virtual Registry 或 Dependency Proxy 統一管理外部套件與映像來源

---

## 第十一章 GitLab Security

### 11.1 GitLab 安全掃描總覽

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

**各掃描功能的方案層級（依官方文件標示）**：

> ⚠️ **v2.0 更正**：初版未區分方案層級。實際上多數安全功能需要 **Ultimate**，Free／Premium 僅能執行部分掃描並下載 JSON 報告，無法在 MR 與 Security Dashboard 呈現結果。

| 功能 | Free／Premium | Ultimate | 官方 CI/CD 範本 |
|---|---|---|---|
| SAST（Semgrep 等開源分析器） | ✅ 可執行、產生報告 | ✅ 並於 MR／Dashboard 呈現 | `Jobs/SAST.gitlab-ci.yml` |
| GitLab Advanced SAST（跨檔案污點分析） | ❌ | ✅ | 同上（Ultimate 自動啟用 Advanced SAST 分析器） |
| Pipeline Secret Detection | ✅ | ✅ 並於 MR／Dashboard 呈現 | `Jobs/Secret-Detection.gitlab-ci.yml` |
| Secret push protection | ❌ | ✅ | 於專案或 Group 安全設定開啟，無需範本 |
| Dependency Scanning（SBOM） | ❌ | ✅ | `Jobs/Dependency-Scanning.v2.gitlab-ci.yml` |
| Container Scanning（Trivy） | ✅ 可執行、產生報告與 SBOM | ✅ 並於 MR 呈現、提供自動修補建議 | `Jobs/Container-Scanning.gitlab-ci.yml` |
| DAST | ❌ | ✅ | `Security/DAST.gitlab-ci.yml` |
| License Scanning（CycloneDX） | ❌ | ✅ | 由 Dependency Scanning 產生的 SBOM 提供，無獨立範本 |
| Security Dashboard、Vulnerability Report | ❌ | ✅ | — |
| Security Policies | ❌ | ✅ | — |

### 11.2 SAST（靜態應用程式安全測試）

```yaml
include:
  - template: Jobs/SAST.gitlab-ci.yml
```

GitLab 會依專案使用的語言自動選用對應的分析器，無需手動指定。Ultimate 方案會額外使用 **GitLab Advanced SAST**，提供跨函式、跨檔案的污點追蹤（Taint analysis），可降低誤判並找出更深層的注入類漏洞。

自訂設定範例（排除測試與產生的程式碼）：

```yaml
sast:
  variables:
    SAST_EXCLUDED_PATHS: "spec, test, tests, tmp, generated"
```

> 💡 **效能建議**：大型 Repository 使用 Advanced SAST 時，官方建議先列出檔案類型分布，把明顯不含風險的目錄（例如自動產生的程式碼、第三方 vendor）加入排除，並在每次調整後比對掃描時間與發現數量，確認沒有排除掉真正需要掃描的程式碼。

### 11.3 DAST（動態應用程式安全測試）

> ⚠️ **v2.0 更正**：目前的 DAST 分析器（瀏覽器式 DAST）使用 `DAST_TARGET_URL` 指定目標、以 `DAST_FULL_SCAN: "true"` 開啟主動掃描，範本為 `Security/DAST.gitlab-ci.yml`；初版的 `DAST_WEBSITE`、`DAST_FULL_SCAN_ENABLED` 為舊版變數。

```yaml
stages:
  - build
  - test
  - deploy
  - dast

include:
  - template: Security/DAST.gitlab-ci.yml

dast:
  variables:
    DAST_TARGET_URL: "https://staging.example.com"
    DAST_FULL_SCAN: "true"
    DAST_AUTH_URL: "https://staging.example.com/login"
    DAST_AUTH_USERNAME: "dast_user"
    DAST_AUTH_USERNAME_FIELD: "name:username"
    DAST_AUTH_PASSWORD_FIELD: "name:password"
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

> 💡 密碼請以 Masked 變數 `DAST_AUTH_PASSWORD` 注入，不可寫在 YAML 中。`DAST_FULL_SCAN` 預設為 `false`（只做被動檢查），設為 `true` 才會同時執行主動攻擊測試。

> ⚠️ **注意事項**：DAST 是對「已部署運行中」的應用程式進行主動掃描（會實際送出測試攻擊請求），務必只對 Staging/測試環境執行，**絕不可直接對生產環境執行 Full Scan**，避免造成非預期的資料異動或服務負載。

### 11.4 Dependency Scanning

> ⚠️ **v2.0 更正**：官方目前的範本為 `Jobs/Dependency-Scanning.v2.gitlab-ci.yml`（以 SBOM 為基礎的分析器，**19.0 起 GA**），初版的 `Security/Dependency-Scanning.gitlab-ci.yml` 為舊版 Gemnasium 路徑。

```yaml
include:
  - template: Jobs/Dependency-Scanning.v2.gitlab-ci.yml
```

掃描 `pom.xml`、`package-lock.json`、`requirements.txt` 等相依清單，比對已知 CVE 資料庫（如 GitLab Advisory Database），於 MR 中標示風險套件與建議升級版本。

目前官方建議的掃描方式已轉為**以 SBOM（Software Bill of Materials，採 CycloneDX 格式）為基礎**：建置階段先產生專案完整的 SBOM 清單，再對 SBOM 進行漏洞比對與後續的持續重新掃描（當 GitLab Advisory Database 有新資料時自動重新比對既有 SBOM，不需重新建置）。

**近期重要變更**：

| 版本 | 變更 |
|---|---|
| 17.9 | 以 Gemnasium 分析器為核心的 Dependency Scanning 標示為棄用，**提議於 20.0 移除** |
| 19.0 | SBOM-based Dependency Scanning GA；Gradle 專案支援預設開啟 |
| 19.2 | 新增 Bun 支援 |
| 19.4 | 新增**惡意套件公告（Malware advisories）**比對，可偵測供應鏈中已知的惡意套件 |

> ⚠️ **棄用提醒**：仍在使用舊版 `Dependency-Scanning.gitlab-ci.yml`（Gemnasium 路徑）的專案，應依官方遷移指南改用 v2 範本；Gemnasium 路徑的移除時程請持續追蹤官方 Deprecations 頁面。

#### 11.4.1 AI 輔助安全：Agentic SAST 與 Duo 誤報偵測

GitLab Duo Agent Platform 已將部分安全掃描工作流程自動化。下列 Flow 限 **Ultimate**，且使用時會消耗 GitLab Credits（見第十三章）：

- **SAST Vulnerability Resolution Flow**（18.9 Beta，18.11 GA）：針對 SAST 偵測到的漏洞，由 AI Agent 分析程式碼上下文後，自動產生對應的修補 Merge Request（含程式碼變更與說明），開發者只需審查並決定是否合併。
- **SAST False Positive Detection Flow**（18.7 Beta，18.10 GA）、**Secret False Positive Detection Flow**（GA）：針對 SAST 與 Secret Detection 的發現判斷是否可能為誤判，協助安全團隊優先處理真實風險。
- **Security Review Flow**（Beta）：在 MR 中偵測商業邏輯類漏洞。
- **Security Analyst Agent**（GA）：協助分級、分析漏洞與產生修補建議。

```mermaid
flowchart LR
    Scan[SAST 掃描偵測到漏洞] --> AIAnalyze[Duo AI 分析程式碼上下文]
    AIAnalyze -- 判定為可能誤判 --> FlagFP[標註信心分數\n供人工優先排序]
    AIAnalyze -- 判定為真實漏洞 --> AutoFix[Agentic SAST\n自動產生修補 MR]
    AutoFix --> Review[開發者人工審查 + 合併]
    FlagFP --> Review2[安全團隊人工確認]
```

> ⚠️ **注意事項**：自動產生的修補 MR 與誤報信心分數**皆為輔助判斷，不可取代人工最終決策**。企業導入時應保留「AI 產生的修補 MR 必須經過至少一位資深工程師核准才能合併」的硬性規則，並定期抽查 AI 判定誤報的案例，確認沒有真實漏洞被錯誤地降低優先度。

### 11.5 Container Scanning

詳見第九章 9.3 節。Container Scanning 以 Trivy 掃描已建置容器映像中作業系統與語言套件層的已知漏洞，並可偵測已終止支援（EOL）的作業系統版本。Free／Premium 可執行掃描並下載 JSON 與 CycloneDX SBOM 報告；Ultimate 才會在 MR 與 Pipeline Security 分頁呈現結果、提供自動修補建議，以及使用完整的 GitLab Advisory Database。

### 11.6 Secret Detection

```yaml
include:
  - template: Jobs/Secret-Detection.gitlab-ci.yml
```

Pipeline Secret Detection 會偵測程式碼中誤提交的 API Key、密碼、私鑰等機密。建議搭配 **Secret push protection**（**Ultimate**，伺服器端在 `git push` 時即時阻擋含機密的提交），比起合併後才掃描更能防止機密外洩：

```bash
# 開啟單一專案的 Secret push protection（Project Security Settings API）
glab api --method PUT "projects/:id/security_settings?secret_push_protection_enabled=true"

# 對整個 Group 的專案開啟（可排除特定專案）
glab api --method PUT "groups/<group-id>/security_settings?secret_push_protection_enabled=true&projects_to_exclude[]=101"
```

> ⚠️ **v2.0 更正**：`secret_push_protection_enabled` 不能透過 `PUT /projects/:id` 修改，必須使用 Project／Group Security Settings API。

> 💡 **排除規則**：針對測試目錄、文件、第三方相依等可設定路徑型排除（Exclusions），並定期檢視排除規則，避免排除過度。

### 11.7 License Compliance

> ⚠️ **v2.0 更正**：舊的 `License-Scanning.gitlab-ci.yml` 範本與 License Compliance 分析器**已於 GitLab 17.0 移除**。目前的 License Scanning 直接使用 Dependency Scanning 產生的 CycloneDX SBOM 判斷套件授權（Ultimate），不需另外加入範本。

授權政策以 **Merge request approval policy** 的 License 規則設定，例如禁止合併新引入 GPL 系列授權套件的 MR，或要求法務團隊核准：

```yaml
# 安全政策專案中的 policy.yml（節錄）：新引入 GPL 授權套件時需法務核准
approval_policy:
  - name: "Block GPL licenses"
    enabled: true
    rules:
      - type: license_finding
        branch_type: protected
        match_on_inclusion_license: true
        license_types:
          - GNU General Public License v3.0 only
          - GNU General Public License v2.0 only
        license_states:
          - newly_detected
    actions:
      - type: require_approval
        approvals_required: 1
        group_approvers:
          - legal-team
```

### 11.8 Security Dashboard 與 Vulnerability Management

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

### 11.9 企業導入策略

1. **分階段導入，避免一次性阻斷所有 Pipeline**：第一階段先「偵測但不阻擋合併」（僅顯示警告），讓團隊熟悉掃描結果與處理流程；第二階段針對 Critical/High 漏洞設定 MR 合併門檻（Merge Request Approval Rules 要求安全團隊核准或必須先解決）。
2. **建立漏洞 SLA**：依嚴重程度訂定修復時限（如 Critical 7 天內、High 30 天內），並透過 Security Dashboard 追蹤逾期項目。
3. **集中化安全規則治理**：在 Platform 團隊維護的 `ci-templates` 共用範本中統一管理 `SAST_EXCLUDED_PATHS`、掃描頻率等設定，各應用團隊不可隨意關閉安全掃描。
4. **安全左移教育訓練**：搭配 GitLab Duo 的 Vulnerability Explanation 功能（第十三章），讓開發者理解漏洞成因與修復方式，而非只是「被擋下合併」卻不知為何。

> 💡 **實務案例**：某零售業集團導入 GitLab Ultimate 後，第一年僅先開啟 SAST + Secret Detection（偵測但不阻擋），蒐集到的真實漏洞修復率僅 40%；第二年正式將 Critical 漏洞設為合併硬性門檻並導入 SLA 追蹤後，修復率提升至 92%，平均修復時間從 45 天降至 11 天。

### 11.10 Security Policies（安全政策即程式碼）

> 🆕 **v2.0 新增**

Security Policies（**Ultimate**）讓 Security 團隊以 YAML 定義政策、存放在獨立的「安全政策專案」，再連結到 Group 或專案強制執行，是大型企業集中治理安全掃描的核心機制：

| 政策類型 | 用途 |
|---|---|
| Scan execution policy | 強制在 Pipeline 或排程中執行指定掃描（例如所有專案的 `main` 分支都必須跑 SAST 與 Secret Detection） |
| Merge request approval policy | 依掃描結果或授權發現，要求特定人員核准才能合併 |
| Pipeline execution policy | 將自訂 CI/CD Job 注入所有專案的 Pipeline（取代即將移除的 Compliance pipelines）；另有排程型版本 |
| Vulnerability management policy | 依條件自動處理漏洞（例如自動解決已不再偵測到的漏洞） |

```yaml
# 安全政策專案中的 policy.yml（節錄）：所有 release 分支 Pipeline 都必須執行 SAST 與 Secret Detection
scan_execution_policy:
  - name: "Enforce SAST and Secret Detection"
    enabled: true
    rules:
      - type: pipeline
        branches:
          - "release/*"
          - main
    actions:
      - scan: sast
      - scan: secret_detection
```

> ⚠️ **注意事項**：**Compliance pipelines 已於 17.3 棄用並將於 GitLab 20.0 移除**，仍在使用者應依官方遷移指南改用 Pipeline execution policy。政策的修改權限應與一般開發者分離（Separation of duties），由 Security 團隊透過安全政策專案的 MR 流程管理。

### 11.11 安全相關角色與權限

> 🆕 **v2.0 新增**

| 角色 | 說明 | 狀態 |
|---|---|---|
| Security Manager | 檢視與管理漏洞、合規設定與稽核事件，**不具程式碼推送權限**，適合資安團隊 | 18.11 起以 Beta 推出，預設停用 |
| Custom roles（Ultimate） | 以既有角色為基礎，加上細粒度權限（例如「Developer + 管理漏洞」） | GA |
| Planner | 專注於規劃（Issue、Epic、Roadmap），不具程式碼權限 | 17.7 起提供 |

> 💡 **企業導入建議**：資安團隊過去常被迫給予 Developer／Maintainer 權限才能處理漏洞，造成權限過大。Security Manager 角色 GA 前，可先以 Custom role（Reporter + `admin_vulnerability` 等權限）實現最小權限。

### ✅ 第十一章 Checklist

- [ ] 已啟用 SAST / Secret Detection / Dependency Scanning（基本安全掃描三件套）
- [ ] DAST 僅對 Staging 等測試環境執行，未對生產環境執行 Full Scan
- [ ] 已啟用 Secret Push Protection，在 push 階段即時阻擋機密外洩
- [ ] 已針對 Critical/High 漏洞設定合併門檻與修復 SLA
- [ ] 已將安全規則治理集中於共用 CI/CD 範本，避免各專案各自為政
- [ ] 已確認 Dependency Scanning 採用 SBOM-based 範本，並排定舊版 Gemnasium 式掃描的遷移時程（20.0 前須完成）
- [ ] 若已啟用 Agentic SAST 自動修補或 Duo 誤報偵測，已建立「AI 產生結果必經人工核准」的硬性規則
- [ ] 範本已改為 `Jobs/SAST`、`Jobs/Secret-Detection`、`Jobs/Dependency-Scanning.v2`、`Security/DAST`，並移除已不存在的 License-Scanning 範本
- [ ] 已確認各安全功能所需的方案層級（Ultimate）與實際授權一致
- [ ] 已以 Security Policies 集中強制安全掃描，並規劃 Compliance pipelines 在 20.0 前的遷移

---

## 第十二章 GitLab API

### 12.1 REST API 與 GraphQL API 選用建議

| 比較項目 | REST API | GraphQL API |
|---|---|---|
| 學習曲線 | 低，符合一般 HTTP 慣例 | 中，需理解 Query/Mutation 語法 |
| 取得巢狀關聯資料 | 需多次請求（如先取 MR 再取其 Discussion） | 單次請求可一次取得巢狀資料，減少 Round-trip |
| 適合情境 | 簡單 CRUD、CLI Script、CI/CD Job | 需要複雜關聯查詢的 Dashboard、報表系統 |
| 版本穩定性 | v4 已長期穩定 | Schema 持續擴充中，部分新功能僅 GraphQL 提供 |

### 12.2 Access Token 種類

> ⚠️ **v2.0 更正**：初版只列出四種 Token。以下依官方「GitLab token overview」補齊企業常用的 Token 類型、前綴與存取範圍。前綴可用於 Secret Detection、DLP 與 Log 遮蔽規則。

| Token 類型 | 前綴 | API | Registry | Repository | 適用情境 |
|---|---|---|---|---|---|
| Personal Access Token（PAT） | `glpat-` | ✅ | ✅ | ✅ | 個人開發機操作、`glab auth login` |
| Fine-grained PAT | `glpat-` | 依授予的細粒度權限 | 依權限 | 依權限 | 取代範圍過大的傳統 PAT（19.2 起 GA） |
| Project Access Token | `glpat-` | 限單一專案 | 限單一專案 | 限單一專案 | 專案層級自動化（部署機器人），與個人帳號脫鉤 |
| Group Access Token | `glpat-` | 限單一 Group | 限單一 Group | 限單一 Group | 跨多專案自動化（集中報表蒐集） |
| Service Account 的 PAT | `glpat-` | ✅（依 Service Account 權限） | ✅ | ✅ | 企業級 Bot 帳號，不佔用真人身分（Free 起可用） |
| CI/CD Job Token（`CI_JOB_TOKEN`） | `glcbt-` | 部分端點 | ❌ | ✅ | Pipeline 執行期間自動產生，Job 結束即失效 |
| Deploy Token | `gldt-` | ❌ | ✅ | ✅ | 部署主機或 Kubernetes 拉取程式碼、映像、套件 |
| Deploy Key（SSH） | — | ❌ | ❌ | ✅ | 部署主機以 SSH 拉取（或推送）程式碼 |
| Runner Authentication Token | `glrt-` | ❌ | ❌ | 受限 | Runner 與 GitLab 之間的認證 |
| Trigger Token | `glptt-` | 觸發 Pipeline | ❌ | ❌ | 外部系統觸發 Pipeline |
| GitLab agent for Kubernetes Token | `glagent-` | — | — | — | `agentk` 與 KAS 之間的認證 |

**Token 效期與治理**：

- 建立 Token 時若未指定到期日，預設為 **365 天後**到期；預設最長也不能超過 365 天。17.6 起管理員可調整上限（最長可延伸至 400 天）。
- **Fine-grained PAT**（18.10 Beta，19.2 GA）可針對個別資源與動作授權，並可由 Duo Agent Platform 的 **Permissions Assistant** 協助挑選最小權限。
- **DPoP**（Demonstrating Proof-of-Possession）可將 PAT 綁定使用者的 SSH 私鑰，即使 Token 外洩也無法單獨使用；可用 `glab auth dpop-gen` 產生證明（Experimental）。
- 建議 Token 命名採用「用途-系統-環境」格式，例如 `ci-deploy-order-service-production`、`api-read-reporting-dashboard`，方便稽核與輪替。

> ⚠️ **注意事項**：個人 PAT 會隨人員離職而失效，導致自動化腳本無預警中斷。**正式環境的自動化應一律使用 Service Account、Project／Group Access Token 或 CI Job Token**，而非個人 PAT，並以 `glab token list`／`glab token rotate`（第五章 5.23）定期盤點與輪替。

### 12.3 curl 範例

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

### 12.4 Java / Spring Boot 範例

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

### 12.5 Python 範例

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

### 12.6 TypeScript 範例

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

### 12.7 分頁、限流與 API 相容性

> 🆕 **v2.0 新增**

| 主題 | 官方行為 | 實作建議 |
|---|---|---|
| Offset 分頁 | 以 `page`、`per_page`（最大 100）分頁，回應 Header 含 `x-next-page` 與 `link` | 小型集合可用；`glab api --paginate` 會自動處理 |
| Keyset 分頁 | 以 `pagination=keyset` 搭配 `order_by`、`sort`，依 `link` Header 取下一頁 | 大型集合（專案、稽核事件）必須優先使用；**20.0 起 Audit events API 將強制使用 keyset 分頁** |
| 未認證請求 | 19.0 起對未認證的 Projects API 請求強制頁數上限 | 自動化一律帶 Token 呼叫 |
| 參數型別驗證 | 19.3 起，整數型路徑參數若傳入非數字會回傳 `400`（例如把 MR 標題誤當 IID） | 腳本需正確區分 `id`、`iid` 與 URL 編碼路徑 |
| 限流（Rate limit） | 超過限制回傳 `429`，並附 `RateLimit-*` 與 `Retry-After` Header | 依 `Retry-After` 指數退避重試；批次作業降低併發 |

```python
import time, requests

def gitlab_get_all(url, headers):
    """以 keyset 分頁取回所有資料，並處理 429 限流。"""
    params = {"pagination": "keyset", "per_page": 100, "order_by": "id", "sort": "asc"}
    results = []
    while url:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 429:
            time.sleep(int(resp.headers.get("Retry-After", "10")))
            continue
        resp.raise_for_status()
        results.extend(resp.json())
        url = resp.links.get("next", {}).get("url")
        params = None  # 下一頁的完整參數已包含在 link URL 中
    return results
```

### ✅ 第十二章 Checklist

- [ ] 已依情境選用 REST 或 GraphQL（複雜關聯查詢優先考慮 GraphQL）
- [ ] 自動化腳本已改用 Project/Group Access Token 或 CI Job Token，未使用個人 PAT
- [ ] API 呼叫已實作 Rate Limit 退避重試與合理 timeout
- [ ] 各語言 SDK/Client 已封裝統一錯誤處理，避免裸露 Token 於 Log 中
- [ ] Token 已依用途命名並設定合理效期，定期以 `glab token list` 盤點、以 `glab token rotate` 輪替
- [ ] 已評估以 Fine-grained PAT 與 Service Account 取代範圍過大的傳統 PAT
- [ ] 大型集合查詢已改用 keyset 分頁，並實作 `Retry-After` 退避重試

---

## 第十三章 GitLab Duo

### 13.1 GitLab Duo 功能總覽與授權模型

GitLab Duo 是 GitLab 內建的 AI 功能套件，深度整合在開發流程的每個環節。自 18.x 起分為兩條產品線，企業導入前必須先分清楚：

> ⚠️ **v2.0 更正**：初版把 Duo add-on（Core／Pro／Enterprise）與訂閱方案（Free／Premium／Ultimate）混為一談，並寫成「Core 方案使用者需升級至 Pro／Ultimate」。正確關係如下表。

| 產品線 | 取得方式 | 計價 | 主要功能 |
|---|---|---|---|
| **GitLab Duo Agent Platform**（18.8 GA） | Premium／Ultimate 內含 **Duo Core**；GitLab.com Free 方案可購買 GitLab Credits 使用（18.10 起） | 依用量扣抵 **GitLab Credits** | Agentic Chat、Code Suggestions、Foundational／Custom／External Agents、Flows（含 Code Review Flow） |
| **GitLab Duo Pro／Enterprise**（Non-Agentic 功能） | Premium／Ultimate 加購，需指派座位（Seat） | 依座位計費，**不消耗** Credits | Code Suggestions、Non-Agentic Chat、IDE 內程式碼解釋／重構／修正／測試產生；Enterprise 另含 Code Review、Root Cause Analysis、Vulnerability Explanation／Resolution 等 |
| GitLab Duo with Amazon Q | 獨立 add-on，僅 Self-Managed | 另計 | Amazon Q Developer 整合 |
| GitLab Duo Agent Platform Self-Hosted（18.8 起） | 離線授權（Offline license）客戶加購 | 企業授權合約（ELA）固定費用 | 在 Agent Platform 中使用自行託管的模型 |

```mermaid
flowchart TB
    Sub[GitLab 訂閱方案\nFree / Premium / Ultimate]
    Sub --> Core[Duo Core\nPremium/Ultimate 內含]
    Sub --> Seat[Duo Pro / Enterprise\n座位制加購]
    Core --> Credits[GitLab Credits\n用量計價]
    Credits --> DAP[Duo Agent Platform\nAgentic Chat / Agents / Flows]
    Seat --> NonAgentic[Non-Agentic 功能\nChat / Code Review / RCA / 漏洞解釋]
```

**Duo Agent Platform 各功能的方案層級（GA 功能，節錄）**：

| 功能 | Free（需購 Credits） | Premium | Ultimate |
|---|---|---|---|
| Agentic Chat、Code Suggestions | ✅ | ✅ | ✅ |
| Custom agents、Custom flows | ✅ | ✅ | ✅ |
| Planner Agent、Data Analyst Agent | ✅ | ✅ | ✅ |
| Developer Flow（Issue 轉 MR）、Software Development Flow | ✅ | ✅ | ✅ |
| Code Review Flow | ✅ | ✅ | ✅ |
| Fix CI/CD Pipeline Flow、Convert to GitLab CI/CD Flow | ✅ | ✅ | ✅ |
| MCP clients（從外部 AI 工具存取 GitLab） | ✅ | ✅ | ✅ |
| External agents、Flow Creator Agent、Resolve merge conflicts、Resolve review discussions | ❌ | ✅ | ✅ |
| SAST／Secret 誤報偵測 Flow、SAST Vulnerability Resolution Flow、Security Analyst Agent、Permissions Assistant | ❌ | ❌ | ✅ |

> 💡 Beta／實驗性功能（例如 CI Expert Agent、Security Review Flow、External MCP servers、AI Governance Dashboard）的方案層級與是否消耗 Credits 變動較快，導入前請查閱官方「GitLab Duo Agent Platform」頁面。

### 13.2 GitLab Duo Chat

在 Web UI 或 IDE 擴充套件（VS Code、JetBrains、Visual Studio）中直接提問，Chat 會結合當前專案上下文（程式碼、Issue、MR、Pipeline）回答：

```text
> 為什麼這個 MR 的 Pipeline 在 unit-test stage 失敗？
> 幫我解釋 OrderRefundService.java 第 42 行的邏輯
> 這個專案最近一週有哪些未解決的 Critical 漏洞？
```

在終端機則使用 **GitLab Duo CLI**（`glab duo cli`，見第五章 5.10）：

```bash
glab duo cli run --goal "比較 main 與 release/2.3.0 分支在 OrderService 的差異，並指出潛在風險"
```

#### 13.2.1 Agentic Chat 與 Non-Agentic Chat

| 模式 | 特性 | 授權 |
|---|---|---|
| **Agentic Chat**（18.8 GA） | 能自主規劃多個步驟、搜尋與讀取檔案、建立或編輯檔案，並串接 Issue／MR／Pipeline 等資料來源 | Duo Agent Platform（消耗 Credits）；Duo Core 使用者 19.0 起可使用 |
| **Non-Agentic Chat**（傳統問答） | 針對單一問題回覆，不具多步驟規劃與動作執行能力 | Duo Pro／Enterprise 座位 |

> ⚠️ **注意事項（已生效的變更）**：自 **2026-05-21**（GitLab 19.0）起，**Duo Core** 使用者在所有 GitLab 版本上都**不再能使用 Non-Agentic Chat**，改為使用 Agentic Chat、Agents、Flows 與 Code Suggestions 等 Agent Platform 功能，並需具備 GitLab Credits。持有 Duo Pro／Enterprise 座位的使用者不受影響。企業應同步更新內部教育訓練教材，並規劃 Credits 預算與用量監控。

#### 13.2.2 GitLab Duo Agent Platform（18.8 GA）

GitLab Duo Agent Platform 是 GitLab Duo 從「單點 AI 輔助功能」邁向「平台化多 Agent 協作」的核心架構：

```mermaid
flowchart TB
    Platform[GitLab Duo Agent Platform]
    Platform --> Agents[Agents]
    Platform --> Flows[Flows]
    Agents --> Foundational["Foundational Agents（內建）\nPlanner、Data Analyst、Security Analyst、\nFlow Creator、Onboarding、Permissions Assistant、\nSupport Assistant、CI Expert（Beta）"]
    Agents --> Custom["Custom Agents（組織自訂）\n可發布至 AI Catalog"]
    Agents --> External["External Agents（Premium+）\n串接 Claude Code 等外部 Agent"]
    Flows --> FFlows["Foundational Flows\nDeveloper、Code Review、Fix CI/CD Pipeline、\nConvert to GitLab CI/CD、Software Development"]
    Flows --> CFlows["Custom Flows\n組合多個 Agent 解決業務流程"]
```

- **Foundational Agents**：GitLab 內建、開箱即用的 Agent。可在 GitLab UI、VS Code 與 JetBrains IDE 使用，也可複製後自訂。
- **Custom Agents**：組織依自身 SOP（例如「Spring Boot 升級檢查 Agent」「內部 API 規範審查 Agent」）建立 Agent，並可透過 **AI Catalog** 分享。
- **External Agents**：將 Claude Code 等第三方 Agent 以受控方式接入 GitLab（例如由 MR 留言觸發，在 GitLab 提供的執行環境中運作）。
- **Flows**：由多個步驟或 Agent 組成的自動化工作流程，例如 **Developer Flow** 可把 Issue 轉成 MR、**Fix CI/CD Pipeline Flow** 可診斷並修正失敗的 Pipeline。

> 💡 **企業導入建議**：
>
> - 先以 Foundational Agents 與 Code Review Flow 熟悉操作模式與權限授權流程。
> - 待團隊掌握「Agent 可以做什麼、不能做什麼、誰來核准動作」的治理模式後，再投入 Custom Agents 與 Custom Flows。
> - 同時建立 Credits 用量監控，避免預算失控。

### 13.3 Code Suggestions（程式碼建議）

在 VS Code、JetBrains IDE、Visual Studio、Neovim 等編輯器安裝官方 GitLab 擴充套件並登入後，輸入程式碼時會即時顯示 AI 建議的補全內容，支援多數主流語言（Java、Python、JavaScript／TypeScript、Go、Vue 等）。Code Suggestions 同時屬於 Agent Platform（依 Credits 計價）與 Duo Pro／Enterprise（座位制）。

> 💡 **最佳實務**：在程式碼中以註解描述意圖（例如「// 依訂單狀態計算可退款金額，已退款部分需扣除」），再接受建議，品質通常優於讓 AI 盲目補全。

### 13.4 Code Review Flow（MR 自動審查）

> ⚠️ **v2.0 更正**：Agent Platform 的 **Code Review Flow**（18.7 Beta、18.8 GA）是目前主力的 AI 審查方式；初版的 `glab duo ask --mr` 指令並不存在。

在 MR 中以下列任一方式請 GitLab Duo 審查：

- 將 `@GitLabDuo` 指派為 Reviewer。
- 在留言輸入快速動作 `/assign_reviewer @GitLabDuo`。
- 在留言中提及 `@GitLabDuo` 並請求審查，之後也可在審查討論串中與 Duo 對話。

Duo 會：

- 摘要 Diff 變更的核心邏輯。
- 標示潛在 Bug、效能問題、安全風險。
- 提出具體修改建議（可一鍵套用為 Suggested Change）。

**自動審查與自訂審查規則**：

- 可在專案或 Group 設定開啟**自動審查**，讓每個新 MR 自動請 Duo 審查，也可設定排除條件。
- 在 `.gitlab/duo/mr-review-instructions.yaml` 定義專案專屬的審查規則（例如依語言、目錄套用不同檢查項目）。

```yaml
# .gitlab/duo/mr-review-instructions.yaml（範例）
instructions:
  - name: Java 後端規範
    fileFilters:
      - "src/main/java/**/*.java"
    instructions: |
      1. 所有金額計算必須使用 BigDecimal，不可使用 double/float。
      2. Service 層方法需處理 null 輸入並拋出明確例外。
      3. 新增的 SQL 查詢需檢查是否有 N+1 問題。
```

> ⚠️ **注意事項**：Duo Code Review 是輔助審查，**不取代人工 Reviewer**。建議把 Duo Review 當成「審查前的第一輪自我檢查」，協助開發者在請真人審查前先抓出明顯問題，而不是把核准責任完全交給 AI。

### 13.5 Vulnerability Explanation 與 Security Analyst Agent

在 Vulnerability Report 的漏洞詳情頁，Duo 能以該專案實際程式碼上下文解釋：

- 此漏洞的成因（例如 SQL Injection 的具體觸發路徑）。
- 可能造成的實際風險情境。
- 具體修復建議（含程式碼範例）。

| 功能 | 授權 |
|---|---|
| Vulnerability Explanation／Vulnerability Resolution（Non-Agentic） | Ultimate + Duo Enterprise |
| Security Analyst Agent、SAST Vulnerability Resolution Flow、誤報偵測 Flow | Ultimate + Agent Platform（Credits） |

對於資安背景較淺的開發團隊，這項功能可大幅降低「看到 CVE 編號卻不知如何下手修復」的情況。

### 13.6 Test Generation 與 Refactoring

```text
> 幫 OrderRefundService.processRefund() 產生單元測試，需覆蓋成功退款、超額退款、訂單不存在三種情境
> 幫我重構這段巢狀 if-else，改用早期返回（Early Return）模式
```

在 IDE 中可使用 Agentic Chat 直接建立或修改測試檔；若持有 Duo Pro／Enterprise 座位，也可使用 IDE 內的 `/tests`、`/refactor` 等 Non-Agentic 指令。產生的變更一律需經開發者審查後才提交。

### 13.7 Prompt Engineering 與客製化

1. **提供具體上下文**：直接點名檔案、函式、MR/Issue 編號，比泛問「這段程式碼有問題嗎」更精準。
2. **拆解大問題為多個小提問**：先問「這個模組的職責是什麼」再問「如何重構」，比一次問「幫我重構整個模組」效果更好。
3. **要求結構化輸出**：例如「請用條列式列出風險，並標註嚴重程度」，方便團隊後續追蹤。
4. **明確說明限制**：例如「不要修改公開 API 介面，只重構內部實作」，避免 AI 建議的修改範圍超出預期。
5. **善用迭代**：第一輪建議不滿意時，提供具體回饋（如「這個方案會破壞既有測試，請改用其他方式」）讓 Duo 修正方向，而非直接放棄重新問。

**客製化 Agent Platform 的四種方式**：

| 方式 | 檔案位置 | 影響範圍 |
|---|---|---|
| Custom rules | `.gitlab/duo/chat-rules.md`（或使用者層級規則） | Chat、Agents、Flows（Code Review Flow 除外） |
| AGENTS.md | 專案根目錄 `AGENTS.md`（Monorepo 可分目錄放置） | Chat、Flows（Code Review Flow 除外） |
| MR review instructions | `.gitlab/duo/mr-review-instructions.yaml` | Code Review Flow |
| Agent Skills | `skills/<skill-name>/SKILL.md` | Chat、Flows（Code Review Flow 除外） |

```text
專案根目錄
├── AGENTS.md                          # 多個 Duo 功能共用的專案指示
├── skills/<skill-name>/SKILL.md       # 可分享的技能與自訂斜線指令
└── .gitlab/duo/
    ├── chat-rules.md                  # Chat 專屬規則
    ├── mr-review-instructions.yaml    # Code Review 標準
    └── ...                            # 自訂 Flow 定義、MCP server 設定等
```

> ⚠️ **v2.0 更正**：初版提到的「`.gitlab/duo/` Context 排除規則」並非官方機制。`.gitlab/duo/` 用來存放規則、審查指示、自訂 Flow 與 MCP 設定；要限制 AI 讀取特定內容，應透過專案／Group 的 GitLab Duo 開關與權限設定控制。

> 💡 **實務案例**：某保險業團隊將「MR 描述自動產生」與「Duo Code Review」納入標準流程後，Code Review 平均耗時從 35 分鐘降至 18 分鐘，主要原因是 Reviewer 不再需要從零理解變更內容，可直接針對 Duo 已標示的風險點進行確認與討論。

### 13.8 AI 治理、稽核與成本控管

> 🆕 **v2.0 新增**

| 治理面向 | 官方機制 | 企業建議 |
|---|---|---|
| 功能開關 | 可在 Instance／Group／專案層級開關 GitLab Duo 與 Agent Platform，並可個別開關 Foundational agents、Beta 與實驗功能 | 先在試點 Group 開啟，其他 Group 維持關閉 |
| 用量與成本 | GitLab Credits 儀表板；Duo Pro／Enterprise 座位管理 | 設定月度預算與告警，定期檢視高用量使用者與 Flow |
| 稽核 | AI audit events、AI audit event report（Beta，Premium+）、AI Governance Dashboard（Beta，Ultimate） | 將 AI 事件納入 SIEM |
| Agent 工具治理 | Agent tool governance（Beta）；外部 Agent 可搭配 `glab govern`（第五章 5.25） | 限制 Agent 可呼叫的工具與權限 |
| 資料與模型 | 雲端連線（AI Gateway）或 Duo Self-Hosted／Agent Platform Self-Hosted | 高合規產業評估自託管模型，並審閱官方資料使用政策 |

### ✅ 第十三章 Checklist

- [ ] 已釐清組織持有的 Duo 授權（Duo Core／Pro／Enterprise、GitLab Credits）與對應功能
- [ ] 已確認 Duo Core 使用者自 2026-05-21 起改用 Agentic Chat，並完成教育訓練與 Credits 預算規劃
- [ ] 開發團隊已安裝並登入 IDE 的 GitLab 擴充套件，啟用 Code Suggestions
- [ ] MR 流程已納入 Code Review Flow（`@GitLabDuo`）作為人工審查前的輔助檢查，並建立 `mr-review-instructions.yaml`
- [ ] 已建立 `AGENTS.md`、`chat-rules.md` 等客製化檔案，統一 AI 行為
- [ ] 已盤點 Foundational Agents 與 Flows 的使用情境，並建立 Custom Agents 的審核與發布流程
- [ ] 已建立 AI 稽核事件、Credits 用量的監控與告警

---

## 第十四章 GitLab + Claude Code

### 14.1 整合架構總覽

Claude Code 可透過兩種方式與 GitLab 協作：

1. **透過 `glab` CLI**：Claude Code 在終端機環境中直接呼叫 `glab` 指令（建立 MR、查 Pipeline、留言），這是目前最直接、免額外設定的整合方式。
2. **透過 GitLab MCP server**：Claude Code 以 MCP 協定連接 GitLab 內建的 MCP server（`https://<gitlab>/api/v4/mcp`，以 OAuth 授權），取得結構化的工具呼叫介面（Issue、MR、Pipeline、Work Item 等）。相較於 CLI 字串輸出，MCP 回傳結構化資料更適合 Agent 進行多步驟推理（詳見第十六章）。

```mermaid
flowchart LR
    Claude[Claude Code]
    Claude -- 終端機指令 --> Glab[glab CLI]
    Claude -- MCP 協定 --> MCP[GitLab MCP Server]
    Glab --> GitLabAPI[GitLab REST/GraphQL API]
    MCP --> GitLabAPI
    GitLabAPI --> Project[GitLab 專案\nMR / Issue / Pipeline]
```

### 14.2 實戰案例：Claude Code 自動建立並提交 Merge Request

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
  --description-file ./mr-description.md \
  --target-branch main \
  --reviewer alice \
  --label "bug,backend"
```

> 💡 **實務建議**：
>
> - MR 描述請 Claude Code 先寫入 `mr-description.md`，再以 `--description-file` 帶入。直接在雙引號中寫 `\n` 不會被 Shell 轉為換行。
> - 建立 MR 前，先在本機跑一次測試，或以 `glab ci status --live` 確認 Pipeline 綠燈，避免建立 MR 後才發現失敗，造成 Reviewer 不必要的等待。

### 14.3 實戰案例：Claude Code 自動 Review 程式碼

**情境**：在 MR 建立後，請 Claude Code 針對該 MR 進行第二輪獨立審查（作為人工 Reviewer 之外的補充視角）。

```bash
# 取得 MR 的程式碼差異供 Claude Code 分析
glab mr diff 482 > /tmp/mr-482.diff
```

對話中請 Claude Code：

```text
請閱讀 /tmp/mr-482.diff，從正確性、安全性、效能三個角度審查，
並將發現的問題透過 glab mr note create 482 留言在 MR 上，每個問題附上具體行號與建議修改方式。
```

Claude Code 會執行：

```bash
glab mr note create 482 -m "## 🤖 Claude Code 審查意見

### 正確性
- \`OrderRefundService.java:58\`：當 \`refundAmount\` 為負數時未做邊界檢查，建議於方法開頭加入 \`if (refundAmount.compareTo(BigDecimal.ZERO) < 0) throw new IllegalArgumentException(...)\`

### 安全性
- 未發現明顯安全風險

### 效能
- \`OrderRefundService.java:71\`：迴圈內重複查詢資料庫，建議改用批次查詢（\`findAllByOrderIdIn\`）避免 N+1 問題"
```

### 14.4 實戰案例：Pipeline 失敗時自動診斷

```text
使用者：MR !482 的 Pipeline 失敗了，幫我看看為什麼
```

Claude Code 會依序執行：

```bash
glab mr view 482
glab ci list --ref fix/order-refund-amount-calculation --status failed
glab ci trace unit-test --branch fix/order-refund-amount-calculation   # 取得失敗 Job 的完整 Log
```

分析 Log 後，Claude Code 直接在本機修正程式碼、重新 push，並可選擇性留言告知已修復：

```bash
glab mr note create 482 -m "已修正 unit-test 失敗原因（測試資料缺少必要欄位 \`refundReason\`），已 push 新的 commit，請重新觸發 Pipeline。"
```

### 14.5 CLAUDE.md 專案規範整合建議

建議在專案根目錄的 `CLAUDE.md` 中明確記載團隊的 GitLab 協作規範，讓 Claude Code 在每次任務中自動遵循，避免每次對話都要重新說明：

```markdown
## GitLab 協作規範

- 所有 MR 標題需符合 Conventional Commits 格式（feat/fix/refactor/docs/test/chore）
- 建立 MR 前必須確認本機測試通過（mvn test 或 npm run test）
- MR 描述需包含「問題」「修改」「測試」三個段落
- 禁止直接 push 到 main，所有變更必須透過 MR
- 本專案使用 GitLab：一律使用 glab（例如 glab ci status、glab mr note create），不要使用 gh 或已棄用的 glab pipeline
- Reviewer 預設指派：backend 變更指派 @alice，frontend 變更指派 @bob
- 機密與 Token 一律透過環境變數讀取，不可寫入程式碼或提交記錄
```

> ⚠️ **注意事項**：讓 AI Agent（Claude Code）自動建立 MR、留言、甚至合併程式碼時，務必確保 **Protected Branch 與 Approval Rules 仍要求至少一位真人核准**，AI 可加速產出與初步審查，但正式合併決策應保留人工把關，尤其是涉及生產環境部署的高風險變更。

### 14.6 讓 Claude Code 更懂 GitLab：Agent Skills 與稽核

> 🆕 **v2.0 新增**

**1. 安裝 `glab` 內建的 Agent Skills**（Experimental，見第五章 5.17）：

```bash
# 在專案中安裝核心 glab Skill（寫入 .agents/skills/，Claude Code 等相容 Agent 可自動發現）
glab skills install

# 需要 Stacked Diff 工作流程時，再安裝對應 Skill
glab skills install glab-stack
```

Skills 讓 Agent 以官方建議的方式呼叫 `glab`，減少猜測旗標造成的錯誤（例如誤用已棄用的 `glab pipeline`）。

**2. 以 `glab govern` 留下 AI Agent 的稽核軌跡**（Experimental，見第五章 5.25）：

```bash
# 在開發機安裝 Claude Code 的 Stop/SessionEnd hook，將 Agent 工作階段同步為 GitLab 稽核事件
glab govern setup
glab govern doctor
```

**3. 以 GitLab MCP server 取代純 CLI 輸出**：若需要結構化工具呼叫，改用 GitLab 內建的 MCP server（第十六章 16.3）。

### 14.7 在 GitLab 內執行 Claude Code：External Agents

> 🆕 **v2.0 新增**

除了開發者在本機使用 Claude Code，GitLab Duo Agent Platform 的 **External Agents**（Premium／Ultimate）也能把 Claude Code 等第三方 Agent 接入 GitLab：由 Issue 或 MR 中的提及觸發，在 GitLab 管理的執行環境中運作，並以 Flow 定義檔（例如 `.gitlab/duo/flows/claude.yaml`）描述執行方式。

| 使用方式 | 執行位置 | 適用情境 |
|---|---|---|
| 本機 Claude Code + `glab`／MCP | 開發者電腦 | 互動式開發、個人生產力 |
| External Agent（Claude Code） | GitLab 管理的 Runner／執行環境 | 團隊共用、可稽核、以 Issue／MR 驅動的自動化 |

> ⚠️ **注意事項**：External Agents 的設定方式、可用的模型供應商與計費會依 GitLab.com／Self-Managed 而不同，導入前請依官方「External agents」文件確認，並由 Platform 團隊集中管理 API 金鑰與執行權限。

### ✅ 第十四章 Checklist

- [ ] 已在開發機安裝並登入 `glab`，確認 Claude Code 可成功呼叫
- [ ] 已建立專案 `CLAUDE.md`，明確記載 MR/Commit/Reviewer 規範
- [ ] Protected Branch 與 Approval Rules 仍要求人工核准，AI 自動化不取代最終把關
- [ ] 已建立「Claude Code 建 MR 前必先跑本機測試」的團隊慣例
- [ ] 已評估 CLI 整合與 MCP 整合（第十六章）兩種方式的適用情境
- [ ] 已評估以 `glab skills` 提供 Agent Skills、以 `glab govern` 留存 AI 稽核軌跡
- [ ] 已評估 External Agents 在團隊共用與可稽核情境的適用性

---

## 第十五章 GitLab + GitHub Copilot

### 15.1 為什麼會在 GitLab 上使用 GitHub Copilot

許多企業的開發者習慣使用 GitHub Copilot 作為 IDE 內的程式碼建議工具，即便版本控制與專案管理主要在 GitLab 上進行。Copilot 與 GitLab 並非互斥關係：

- **Copilot in IDE**：純粹作為編輯器內的程式碼補全/Chat 工具，與後端是 GitLab 或 GitHub 無關。
- **Copilot Agent Mode / Coding Agent**：可在 IDE 中執行多步驟任務（讀檔、改檔、跑測試），這部分行為與 Claude Code 類似，皆可透過終端機呼叫 `glab` 與 GitLab 互動。
- **Copilot Code Review**：原生設計給 GitHub Pull Request 流程，若要在 GitLab MR 上取得類似的 AI 審查體驗，建議優先使用 GitLab Duo 的 Code Review Flow（第十三章 13.4），而非試圖橋接 Copilot Code Review。

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

### 15.2 Agent Mode 與 Coding Agent 操作模式

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

### 15.3 如何與 GitLab 協作（實務整合建議）

1. **統一 Agent 指令說明檔**：無論團隊用 Claude Code 或 Copilot，都在專案根目錄維護一份說明文件（`CLAUDE.md` 或 `AGENTS.md`），記載「本專案使用 GitLab + glab」「MR 規範」「Reviewer 指派規則」，讓不同 AI 工具的行為一致。
2. **以 MCP 作為共同介面**：若團隊同時有人用 Claude Code、有人用 Copilot，可統一透過 GitLab 內建的 MCP server（第十六章）作為兩者都支援的標準化整合層。官方文件說明 GitHub Copilot in VS Code 可連接 GitLab MCP server，設定格式請依 Copilot 的 MCP 設定方式加入 `https://<gitlab>/api/v4/mcp`。
3. **Code Review 仍以 GitLab Duo 為主力**：因為 Duo 與 GitLab 資料模型（MR Diff、Security Dashboard、Vulnerability 資料）整合最深，Copilot Code Review 主要設計給 GitHub Pull Request，跨平台橋接通常體驗不如原生方案。
4. **避免雙重 AI 審查造成噪音**：若同時啟用 Duo Code Review Flow 與 Copilot Agent 的審查建議，留言可能重複或矛盾，建議團隊明確分工（如 Duo 負責安全／正確性，Copilot 僅用於開發階段輔助，不重複留言在 MR 上）。

> 💡 **實務案例**：某跨國企業的前端團隊習慣用 GitHub Copilot（個人授權延續舊習慣），後端團隊已全面採用 GitLab Duo。透過統一維護 `AGENTS.md` 並要求所有 AI 工具的終端機操作一律走 `glab`，兩個團隊的 MR 格式、Commit 規範得以保持一致，未因工具不同而產生治理落差。

### ✅ 第十五章 Checklist

- [ ] 已建立 `AGENTS.md` 或等效說明文件，明確告知 AI 工具本專案使用 GitLab + glab
- [ ] 已避免同時啟用多個 AI 審查工具在同一個 MR 上重複留言
- [ ] 已確認 Copilot Agent Mode 產生的變更仍遵循專案的分支保護與 Approval Rules
- [ ] 團隊已就「何時用 Duo、何時用 Copilot」建立明確分工原則

---

## 第十六章 GitLab + MCP

### 16.1 Model Context Protocol 簡介

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
- **權限可細粒度控管**：工具權限以使用者 OAuth 授權的 GitLab 身分為上限，並可透過 HTTP Header 只啟用特定工具組（Toolset）或特定工具（例如不開放「合併 MR」工具）。
- **跨 Agent 通用**：同一個 MCP Server 設定，可同時被 Claude Code、Copilot 或任何支援 MCP 的工具使用，不需要為每個 Agent 各寫一套整合邏輯。

### 16.2 GitLab 的兩種 MCP Server

> ⚠️ **v2.0 更正**：初版把「GitLab 內建的 MCP server」與「`glab mcp serve`」混為一談，並列出 `glab mcp serve --transport http --port`、`--read-only`、`--tools` 等不存在的旗標。兩者實際差異如下。

| 項目 | GitLab MCP server（內建於 GitLab） | `glab mcp serve`（GitLab CLI） |
|---|---|---|
| 位置 | GitLab 伺服器本身，端點 `https://<gitlab>/api/v4/mcp` | 開發者本機，由 AI 工具以子行程啟動 |
| Transport | HTTP（官方建議）；或透過 `mcp-remote` 以 stdio 轉接 | 僅 stdio |
| 認證 | OAuth 2.0（支援 Dynamic Client Registration），使用者在瀏覽器核准 | 沿用 `glab auth login` 的身分 |
| 狀態 | **Beta**（18.3 Experiment → 18.6 Beta） | **Experimental** |
| 方案層級 | 19.2 起 **Free** 即可使用（先前為 Premium） | 不限 |
| 啟用方式 | GitLab.com 由頂層 Group 開啟；Self-Managed／Dedicated 由管理員在 Instance 設定開啟 | 安裝 `glab` 即可 |
| 工具範圍 | Issue、MR、Pipeline、Job、Work Item、Repository、漏洞、搜尋、語意搜尋、Duo Agent 工作階段等（50 個以上工具，可依 Toolset 篩選） | Issue、MR、專案、Pipeline／Job |
| 支援的 MCP 協定版本 | `2025-03-26`、`2025-06-18`、`2025-11-25` | 依 `glab` 版本 |
| 適合情境 | 團隊與企業正式導入、可集中控管 | 個人快速試用、離線或無法開啟伺服器端 MCP 的環境 |

```mermaid
flowchart LR
    subgraph Local["開發者電腦"]
        CC[Claude Code / Copilot / Cursor]
        Glab[glab mcp serve\nstdio, Experimental]
    end
    subgraph Server["GitLab 伺服器"]
        MCP[GitLab MCP server\n/api/v4/mcp, Beta]
        API[GitLab REST / GraphQL]
    end
    CC -- HTTP + OAuth（建議） --> MCP
    CC -- stdio 子行程 --> Glab
    Glab -- REST API --> API
    MCP --> API
```

### 16.3 設定 Claude Code 連接 GitLab MCP Server

**方式一（官方建議）：連接 GitLab 內建 MCP server（HTTP transport）**

```bash
# 1. 以使用者範圍（所有專案皆可使用）加入 GitLab MCP server
claude mcp add -s user --transport http GitLab https://gitlab.example.com/api/v4/mcp

# 2. 確認設定；若先前已以 local 範圍加入同名項目，需先移除（local 會覆蓋 user）
claude mcp list
claude mcp remove GitLab -s local

# 3. 啟動 Claude Code，在對話中輸入 /mcp，選擇 GitLab 並在瀏覽器核准 OAuth 授權
claude
```

若團隊要把設定納入版本控制，可在專案根目錄的 `.mcp.json`（專案範圍）加入：

```json
{
  "mcpServers": {
    "GitLab": {
      "type": "http",
      "url": "https://gitlab.example.com/api/v4/mcp",
      "headers": {
        "X-Gitlab-Mcp-Server-Tool-Name-Prefix": "gitlab_"
      }
    }
  }
}
```

> 💡 `X-Gitlab-Mcp-Server-Tool-Name-Prefix` 會在工具名稱前加上前綴（最多 32 字元），可避免同時連接多個 GitLab instance 或其他 MCP server 時工具名稱衝突。

**方式二：不支援 HTTP 的用戶端，透過 `mcp-remote` 轉為 stdio**（需要 Node.js 20 以上）：

```json
{
  "mcpServers": {
    "GitLab": {
      "command": "npx",
      "args": ["mcp-remote", "https://gitlab.example.com/api/v4/mcp"]
    }
  }
}
```

**方式三：使用 `glab mcp serve`（Experimental，stdio）**：

```bash
claude mcp add glab -- glab mcp serve
```

> ⚠️ **v2.0 更正**：Claude Code 並沒有 `~/.claude/mcp_settings.json` 這個設定檔。官方作法是以 `claude mcp add` 指令新增（使用者範圍設定存於 `~/.claude.json`），或在專案根目錄使用 `.mcp.json`。HTTP 設定也不需要在 `env` 中放 `GITLAB_TOKEN`，GitLab MCP server 以 OAuth 完成授權。

### 16.4 權限管理與工具範圍控制

GitLab MCP server 的權限控制分成三層：

| 層級 | 控制方式 |
|---|---|
| 伺服器端開關 | GitLab.com：頂層 Group 的「Allow access to the MCP server」設定；Self-Managed／Dedicated：Instance 的可見度與存取控制設定 |
| 使用者身分 | 每位使用者以自己的帳號完成 OAuth 授權，MCP 工具的權限**不會超過該使用者在 GitLab 的權限** |
| 工具範圍 | 以 HTTP Header 限制回傳的工具 |

限制工具範圍的 Header：

- `X-Gitlab-Enabled-Mcp-Server-Toolsets`：指定要啟用的工具組（Toolset）。預設啟用 `meta`、`core`、`merge_requests`、`work_items`、`repository`、`ci`；`duo_agent_platform`、`wikis`、`code_security` 需明確加入，設為 `all` 則啟用全部。此功能於 19.5 以功能旗標 `mcp_toolsets` 推出，預設關閉。
- `X-Gitlab-Enabled-Mcp-Server-Tools`：只啟用明確列出的工具名稱。

```bash
# 只開放核心與 Work Item 工具給 Claude Code
claude mcp add -s user --transport http GitLab https://gitlab.example.com/api/v4/mcp \
  --header "X-Gitlab-Enabled-Mcp-Server-Toolsets: core,work_items"
```

> ⚠️ **注意事項**：
>
> - 官方明確提醒，使用 MCP 工具時**使用者需自行防範 Prompt Injection**，只對可信任的 GitLab 物件使用這些工具。
> - 企業導入時應先以限縮的 Toolset 試行，觀察 Agent 行為符合預期後，才逐步開放寫入類工具（例如 `save_merge_request`、`accept_merge_request`、`manage_pipeline`）。
> - 任何寫入操作仍受 Protected Branch／Approval Rules 約束。MCP 範圍限縮只是第一道防線，不能取代 GitLab 原生的權限模型。
> - 若以預先註冊的 OAuth Application（固定 `clientId`）供多人共用，GitLab 不會驗證是哪一個 MCP 用戶端使用該 `clientId`，且以 REST API 預先註冊的應用程式不強制 PKCE。應確認用戶端會送出 PKCE 參數。

### 16.5 實際案例：多步驟 Agent 工作流程

**情境**：請 Claude Code 透過 MCP「分析本週所有未解決的 Critical 漏洞，產生摘要報告，並對每個漏洞在 GitLab 建立對應的 Work Item 指派給負責團隊」。

Agent 透過 GitLab MCP server 依序呼叫的工具（工具名稱依官方「GitLab MCP server tools」頁面；`code_security` 工具組需明確啟用）：

```text
1. list_vulnerabilities（專案、嚴重程度 = CRITICAL、狀態 = DETECTED）
2. 對每個漏洞 → get_vulnerability 取得細節
3. 對每個漏洞 → save_work_item 建立追蹤項目（標籤 security、critical，指派負責人）
4. 產生彙整報告（Markdown），回覆給使用者確認
```

相較於人工逐筆在 Web UI 建立 Issue，此流程可將原本需要 1-2 小時的彙整作業縮短至數分鐘，且保證每個漏洞都有對應追蹤紀錄不被遺漏。

> 💡 **實務案例**：某金融科技公司導入 GitLab MCP Server 後，將「每週安全漏洞彙整與分派」流程交由 Claude Code 透過 MCP 自動執行，原本需要資安人員人工撈報表、開 Issue、@相關人員的流程，全部自動化，資安人員的角色轉為審核 AI 產出的分派是否合理，而非親自執行重複性的資料蒐集工作。

### 16.6 GitLab Orbit（Knowledge Graph）與 AI Agent

MCP 工具呼叫解決了「Agent 如何結構化存取 GitLab 資料」的問題。但當企業擁有數百個專案、跨團隊的服務相依關係複雜時，Agent 仍可能因為「不知道該查哪個專案、哪個函式」而要花多輪工具呼叫才能找到正確上下文。**GitLab Orbit**（Knowledge Graph，目前為 **Experimental**，需在 Namespace 啟用 `knowledge_graph` 功能旗標）就是為此設計：它建立程式碼與專案之間的關聯圖（誰呼叫誰、哪個服務依賴哪個 API），讓 AI Agent 可以直接查詢語意層級的關聯。

```mermaid
flowchart LR
    Repos[多個 GitLab 專案原始碼]
    Repos --> Orbit[GitLab Orbit\n遠端 Knowledge Graph]
    Local[本機程式碼] --> LocalIdx[Orbit 本機索引\nglab orbit index]
    OrbitCLI[Orbit CLI\n透過 glab orbit 執行]
    OrbitCLI --> Orbit
    OrbitCLI --> LocalIdx
    Agent[AI Agent\nClaude Code / Duo Agent Platform] -- glab orbit setup 連接 --> OrbitCLI
```

```bash
# 將 Orbit 連接到本機的 Coding Agent（見第五章 5.16）
glab orbit setup

# 查詢遠端知識圖譜與建立本機索引
glab orbit status
glab orbit index .
glab orbit grep "OrderRefundService"
```

> ⚠️ **v2.0 更正**：Orbit 目前為 Experimental（初版誤標為 Beta）；`glab orbit local setup`、`glab orbit remote --query` 並非官方語法。Orbit 的索引建立會消耗額外運算與儲存資源，企業應視為「強化 Agent 上下文理解」的評估項目，而非正式流程依賴。

### ✅ 第十六章 Checklist

- [ ] 已確認採用 GitLab 內建 MCP server（HTTP、Beta）或 `glab mcp serve`（stdio、Experimental），並了解兩者差異
- [ ] 已由管理員（Self-Managed）或頂層 Group Owner（GitLab.com）開啟 MCP server 存取
- [ ] 已以 `claude mcp add --transport http` 或 `.mcp.json` 正確設定 Claude Code，並完成 OAuth 授權
- [ ] 已以 Toolset／Tools Header 限縮工具範圍試行，確認 Agent 行為符合預期後才逐步開放寫入工具
- [ ] 高風險操作（合併、刪除、權限變更）仍受 GitLab 原生 Protected Branch／Approval Rules 約束
- [ ] 已建立防範 Prompt Injection 的使用規範（只對可信任物件使用 MCP 工具）
- [ ] 已評估 Orbit（Experimental）的適用性，並確認伺服器端功能旗標狀態

---

## 第十七章 AI 協助 Legacy System 逆向工程

### 17.1 為什麼 Legacy System 逆向工程適合導入 AI

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

### 17.2 實戰步驟：將 Legacy 程式碼匯入 GitLab 並建立分析基線

```bash
# 1. 將既有原始碼（即便是從未版控的 PowerBuilder/Delphi 專案）匯入 GitLab
#    --skipGitInit：只建立遠端專案，不在本機執行 git init／clone，避免與下方手動初始化衝突
glab repo create legacy/order-system-vb6 --private --skipGitInit
git init --initial-branch=main
git remote add origin https://gitlab.example.com/legacy/order-system-vb6.git
git add .
git commit -m "chore: 匯入既有 VB6 訂單系統原始碼（逆向工程基線）"
git push -u origin main

# 2. 在所屬 Group 建立 Epic 追蹤整體逆向工程專案（Epic 屬於 Group 層級，需 Premium 以上）
glab work-items create --group legacy --type epic --title "訂單系統逆向工程與文件化"
```

> ⚠️ **v2.0 更正**：Epic 屬於 **Group** 層級，初版的 `projects/:id/epics` 端點並不存在。GitLab 已以 Work Item 模型實作 Epic，新的自動化建議使用 `glab work-items create --type epic`（Experimental）或 Work Items GraphQL API；若必須使用 REST，端點為 `groups/:id/epics`（舊 Epics API，未來將被 Work Items 取代）。

### 17.3 實戰案例：AI Agent 自動分析 Legacy System

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

### 17.4 各 Legacy 技術的 AI 逆向工程要點

| 技術 | 常見挑戰 | AI 協助重點 |
|---|---|---|
| IBM Notes/Domino | 業務邏輯藏在 Form/View 的 LotusScript 中，UI 與邏輯高度耦合 | 請 AI 萃取 LotusScript 邏輯並對應到現代分層架構（Controller/Service/Repository）草案 |
| Java Legacy（Struts/Spring MVC 舊版） | XML 設定檔（struts-config.xml）與程式碼分離，難以追蹤完整請求流程 | 請 AI 串接 Action 類別與 XML 設定，產出完整請求生命週期圖 |
| VB6 | 全域變數氾濫、無模組化、GOTO 語句 | 請 AI 標示全域變數的所有讀寫位置，評估封裝為類別的可行性 |
| Delphi | Form 與 Business Logic 混雜在同一個 Unit | 請 AI 區分 UI 事件處理與純業務邏輯，作為未來分離的依據 |
| PowerBuilder | DataWindow 將 SQL 與顯示邏輯綁定 | 請 AI 萃取 DataWindow 內嵌的 SQL，整理成獨立的資料存取邏輯文件 |
| COBOL | 大量 GOTO、Copybook 共用資料結構複雜 | 請 AI 將 Paragraph 呼叫關係視覺化，標示出核心交易處理路徑 |

### 17.5 文件生成與架構分析範本

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

### 17.6 逆向工程後的重構規劃

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

## 第十八章 Framework 升級專案

### 18.1 升級專案的 GitLab 治理框架

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

### 18.2 Spring Boot 2 → 3 / Java 8 → 21 實戰流程

**步驟 1：建立 Epic 與盤點 Issue**

```bash
glab work-items create --group core-systems --type epic --title "Spring Boot 2 -> 3 與 Java 8 -> 21 升級"

glab issue create --title "盤點所有相依套件的 Jakarta EE 相容性" \
  --label "upgrade,spring-boot3" --milestone "2026-Q4"
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
  rules:
    - if: '$CI_COMMIT_TAG'
      when: manual
```

### 18.3 Vue2 → Vue3 升級實戰流程

```text
請分析 src/components 目錄下所有 Vue2 Options API 元件，
標示出哪些元件大量使用 this.$refs、Mixins、Filters（Vue3 移除/變更的特性），
並依複雜度排序，產出遷移優先順序建議。
```

```bash
glab issue create --title "Vue3 遷移：移除 Filters 改用 Computed/Methods" \
  --label "upgrade,vue3" --milestone "2026-Q4"

# 逐元件遷移，搭配 Stacked Diff（見第五章 5.12 glab stack，Experimental）拆解大型遷移
glab stack create migrate-order-components
glab stack save -a -m "遷移 OrderList 元件至 Composition API"
glab stack save -a -m "遷移 OrderDetail 元件至 Composition API"
glab stack sync --label "upgrade,vue3"
```

CI/CD 中可並行跑 Vue2/Vue3 建置驗證遷移過程未破壞既有功能：

```yaml
build-vue3-migration:
  stage: build
  script:
    - npm run build
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_LABELS =~ /vue3/'
```

### 18.4 Angular 升級實戰流程

Angular 官方提供 `ng update` 逐版升級機制（一次只升一個主版號，並依官方 Update Guide 處理各版本的破壞性變更），搭配 GitLab CI/CD 可建立自動化升級驗證流程：

```bash
# 將 <N> 替換為「目前主版號 + 1」，每次只升一個主版號
npx ng update @angular/core@<N> @angular/cli@<N>
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

### 18.5 升級專案的企業治理建議

1. **使用 Epic + Roadmap 呈現跨季度時程**，讓管理層與其他團隊清楚掌握升級進度，避免升級工作淹沒在一般功能開發的 Backlog 中。
2. **拆解為小型、可獨立驗證的 MR**，搭配 `glab stack`（Experimental）管理相依關係，避免單一巨型 MR 難以審查。
3. **CI/CD 雙軌並行驗證**：升級分支與主分支的 Pipeline 同時跑，確保升級過程不影響既有版本的穩定發布。
4. **分批上線降低風險**：搭配 Canary Deployment 或 Feature Flag，先讓小比例流量驗證新版本穩定後，才全面切換。
5. **善用 AI Agent 加速重複性遷移工作**（如命名空間批次替換、Options API → Composition API 轉換樣板程式碼），但**關鍵業務邏輯變更仍需人工審查**，不應全權交由 AI 自動合併。

> 💡 **實務案例**：某零售集團的 Spring Boot 2→3 升級專案橫跨 14 個微服務、3 個團隊，透過單一 Epic 與 Roadmap 呈現整體時程，每個微服務各自建立 Issue 與獨立升級分支，CI/CD 雙軌驗證確保升級過程不影響日常發版。AI Agent 協助完成約 60% 的命名空間遷移與設定檔調整等重複性工作，團隊得以將人力集中在驗證業務邏輯正確性，整體專案時程較原預估縮短約三分之一。

### 18.6 AI Agent 輔助升級的 GitLab 原生做法

> 🆕 **v2.0 新增**

除了在本機使用 Claude Code，GitLab Duo Agent Platform 也提供可直接套用在升級專案的 Flow：

| Flow／Agent | 在升級專案中的用途 |
|---|---|
| Developer Flow | 將「javax → jakarta 遷移」等拆好的 Issue 直接轉成 MR 草稿 |
| Fix CI/CD Pipeline Flow | 升級後 Pipeline 失敗時，自動診斷並提出修正 |
| Code Review Flow + `mr-review-instructions.yaml` | 以升級專屬的審查規則（例如禁止殘留 `javax.*` import）檢查每個 MR |
| Agentic Breaking Change Resolution Flow（實驗性，Ultimate） | 協助處理相依套件升級造成的破壞性變更 |

> 💡 **企業導入建議**：把升級規範寫進 `AGENTS.md` 與 `mr-review-instructions.yaml`（見第十三章 13.7），讓不同 AI 工具與審查者用同一套標準檢查升級 MR。

### ✅ 第十八章 Checklist

- [ ] 已建立 Epic 與 Roadmap，呈現升級專案的跨季度時程
- [ ] 升級工作已拆解為可獨立驗證的小型 Issue/MR，避免巨型 MR
- [ ] CI/CD 已設定升級分支與主分支雙軌並行驗證
- [ ] 已規劃 Canary/Feature Flag 分批上線策略，降低正式環境風險
- [ ] AI Agent 已用於加速重複性遷移工作，但關鍵業務邏輯變更仍經人工審查

---

## 第十九章 大型企業 DevSecOps 平台設計

### 19.1 依規模分級的架構設計原則

| 開發者規模 | 架構建議 | Group 策略 |
|---|---|---|
| 100+ | 單一 GitLab Self-Managed 叢集（中型 Reference Architecture），可由 2-3 人 Platform 團隊維運 | 依「部門」分 Top-level Group，專案掛在部門 Group 下 |
| 500+ | 拆分獨立的 PostgreSQL/Redis/Gitaly Cluster，Runner 採用 Kubernetes 動態擴縮，建立專責 Platform Engineering 團隊（5-8人） | 依「事業群 → 部門 → 產品線」三層 Group 結構，搭配 Compliance Framework 套用到特定 Group |
| 1000+ | 評估 GitLab Dedicated 或多地域 Geo 部署，建立 SRE + Platform + Security 三個專責團隊，制定平台 SLA | 四層以上 Group 結構，搭配 SAML/SCIM 自動化人員權限同步，集中式 Policy as Code 治理 |

### 19.2 大型企業架構圖

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

### 19.3 權限模型設計

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

GitLab 預設角色（Role）由低到高：**Guest → Planner → Reporter → Security Manager（18.11 Beta，預設停用）→ Developer → Maintainer → Owner**。Planner 專注規劃工作、Security Manager 專注漏洞與合規管理，兩者都不具程式碼推送權限。企業設計權限模型時應掌握：

- **權限繼承**：上層 Group 的角色會繼承到所有子 Group/Project，治理時優先在較高層級設定通用規則，個別專案再依需求微調（不可低於繼承的最低要求）。
- **最小權限原則**：一般開發者預設 Developer（可推送非保護分支、建立 MR），Maintainer 角色（可管理 Protected Branch、CI/CD Variables、合併到 main）僅授予 Tech Lead/架構師。
- **Service Account 分離**：自動化使用的 Bot 帳號（CI/CD 自動建立 MR、部署機器人）應使用獨立的 Service Account 或 Group/Project Access Token，與真人帳號權限分離，方便稽核與快速撤銷。

### 19.4 Group 策略與 Project 策略

**Group 策略**：

1. 依組織架構建立 Top-level Group（如事業群），避免所有專案散落在扁平結構或個人 Namespace。
2. 共用資源（CI/CD 範本、Runner、Package Registry 共用套件）統一放在 `platform` Group 下，供其他 Group `include`/依賴。
3. 以 **Compliance Framework** 為金融／醫療等受監管專案加上合規標籤，再以 **Security Policies**（Scan execution／Merge request approval／Pipeline execution policy，見第十一章 11.10）指定該 Framework 為政策範圍，集中強制雙重審核與安全掃描，而非逐專案手動設定。

**Project 策略**：

1. 命名規範統一（見第二十一章），避免 `order-service`、`OrderService`、`order_service` 混雜。
2. 每個 Project 必須設定 Owner（通常是 Tech Lead），明確權責歸屬。
3. 模板化新專案建立流程（透過 Project Templates 或 `glab repo create` 搭配標準化的 `.gitlab-ci.yml`、`CODEOWNERS`、Issue Template）。

### 19.5 Branch 策略

```bash
# 透過 API 設定 Protected Branch（大量專案可改用 Group 層級 Protected Branch 或 Security Policy 統一套用）
glab api projects/:id/protected_branches \
  -f name=main \
  -F push_access_level=0 \
  -F merge_access_level=40 \
  -F allow_force_push=false
```

| 分支 | Push 權限 | Merge 權限 | 用途 |
|---|---|---|---|
| `main` | 禁止直接 push（0） | Maintainer（40） | 永遠可部署的穩定分支 |
| `release/*` | 禁止直接 push | Maintainer | 版本維護分支 |
| `feature/*` | Developer 可 push | Developer | 一般開發分支，無需保護 |

> 💡 **企業導入建議**：1000+ 規模企業建議將「Protected Branch 規則」「Approval Rules」「安全掃描必跑」等治理項目，以 **Compliance Framework 標記專案範圍、Security Policies 強制執行**的方式集中定義後套用到整個 Group，而非要求每個專案團隊各自設定（容易遺漏或設定不一致）。Platform/Security 團隊應定期稽核（透過 Audit Events 與 Compliance Center）確認治理規則未被個別專案繞過。

> ⚠️ **注意事項**：大型企業常見的失敗模式是「治理規則訂得很完整，但散落在文件中沒有強制執行」。務必將規則轉化為**可被系統強制的設定**（Protected Branch、Compliance Framework、CI/CD 範本中的必跑 Job），而非僅依賴開發者自律遵守書面規範。

### 19.6 身分治理：SSO、SCIM、Service Account 與 Custom Roles

> 🆕 **v2.0 新增**

| 機制 | 用途 | 企業建議 |
|---|---|---|
| SAML SSO／OIDC | 以企業 IdP（Entra ID、Okta 等）統一登入 | 強制所有使用者透過 SSO 登入，並搭配 2FA 或 IdP 的 MFA |
| SCIM | 由 IdP 自動建立、停用 GitLab 帳號 | 人員離職時帳號自動停用，避免殭屍帳號 |
| SAML Group Sync／LDAP Group Sync | 依 IdP 群組自動指派 GitLab Group 成員與角色 | 權限隨組織異動自動調整，減少人工維護 |
| Service Account | 供自動化使用的非真人帳號（Free 起可用） | 取代以真人帳號產生的 PAT，搭配命名規範與效期管理 |
| Custom Roles（Ultimate） | 以預設角色為基礎加上細粒度權限 | 例如「Reporter + 管理漏洞」給資安人員、「Developer + 管理 CI/CD 變數」給 DevOps 人員 |
| Fine-grained PAT（19.2 GA） | 細粒度授權的 Personal Access Token | 取代 `api` 全權限 Token |

### 19.7 合規治理：Compliance Center 與稽核

> 🆕 **v2.0 新增**

```mermaid
flowchart LR
    CF[Compliance Framework\n標記受監管專案] --> SP[Security Policies\n強制掃描 / 審核 / 必跑 Job]
    SP --> Projects[受監管專案 Pipeline 與 MR]
    Projects --> AE[Audit Events\n稽核事件]
    AE --> Stream[Audit Event Streaming\n送往 SIEM]
    Projects --> CC[Compliance Center\n合規狀態與違規報告]
```

| 元件 | 層級 | 說明 |
|---|---|---|
| Compliance Framework | Premium（進階要求為 Ultimate） | 為專案加上合規標籤，作為 Security Policies 的套用範圍 |
| Security Policies | Ultimate | 強制掃描、審核與必跑 Job（見第十一章 11.10） |
| Compliance Center | Ultimate | 集中檢視合規狀態、違規紀錄與框架套用情形 |
| Audit Events 與 Streaming | Premium／Ultimate | 記錄權限變更、設定變更等事件，並可即時串流至 SIEM |

> ⚠️ **注意事項**：
>
> - **Compliance pipelines 將於 GitLab 20.0 移除**，請改用 Pipeline execution policy。
> - 舊的合規標準遵循儀表板（Standards adherence dashboard）已由 Compliance status dashboard 取代。
> - 靜態合規違規報告已於 18.8 棄用。
> - 規劃合規報表時請以最新的 Compliance Center 功能為準。

### ✅ 第十九章 Checklist

- [ ] 已依開發者規模（100+/500+/1000+）選定對應的架構與團隊配置
- [ ] 已建立符合組織架構的多層 Group 結構，共用資源集中於 Platform Group
- [ ] 已套用最小權限原則，Service Account 與真人帳號權限分離
- [ ] 已用 Compliance Framework 標記受監管專案，並以 Security Policies 集中強制安全與審核規則
- [ ] 已建立 Audit Events 稽核機制，定期確認治理規則未被繞過
- [ ] 已以 SCIM／Group Sync 自動化人員權限，並以 Service Account 取代真人帳號執行自動化
- [ ] 已規劃 Compliance pipelines 在 20.0 前遷移至 Pipeline execution policy，並將 Audit Events 串流至 SIEM

---

## 第二十章 GitLab 維運手冊

### 20.1 備份與還原

```bash
# 完整備份（含資料庫、Git 資料、CI/CD Artifacts、Registry）
sudo gitlab-backup create BACKUP=manual_$(date +%Y%m%d)

# 備份設定檔（gitlab-secrets.json 與 gitlab.rb，務必與資料備份分開存放）
sudo cp /etc/gitlab/gitlab-secrets.json /etc/gitlab/gitlab.rb /backup/config/

# 還原（還原前需先安裝「完全相同版本與版本類型（CE/EE）」的 GitLab，並先還原 gitlab-secrets.json 與 gitlab.rb）
sudo gitlab-ctl stop puma
sudo gitlab-ctl stop sidekiq
sudo gitlab-backup restore BACKUP=manual_20260615
sudo gitlab-ctl restart
sudo gitlab-rake gitlab:check SANITIZE=true
```

> ⚠️ **注意事項**：`gitlab-secrets.json` 遺失將導致備份的加密資料（如 CI/CD Variables、2FA 密鑰）**無法解密還原**，務必將設定檔與資料備份分開保存於不同的儲存位置，且兩者都要納入定期備份驗證演練。

### 20.2 監控（Prometheus + Grafana）

GitLab Linux package 內建 Prometheus 與多種 Exporter（`node_exporter`、`postgres_exporter`、`redis_exporter`、`gitlab-exporter`），預設即收集核心指標：

```ruby
# /etc/gitlab/gitlab.rb
prometheus['enable'] = true
# 允許外部 Grafana／企業監控平台抓取的網段
gitlab_rails['monitoring_whitelist'] = ['127.0.0.0/8', '10.0.0.0/8']
```

> ⚠️ **v2.0 更正**：Linux package **已不再內建 Grafana**（自 GitLab 16.3 移除），初版的 `grafana['enable']` 設定已無效。請將內建 Prometheus 接到企業既有的 Grafana 或監控平台，並可匯入 GitLab 官方提供的 Grafana Dashboard。另外，隨套件內建的 Prometheus 2.x 已於 18.6 起棄用，升級時請留意版本說明。

關鍵監控指標：

| 指標 | 告警閾值建議 | 意義 |
|---|---|---|
| `sidekiq_jobs_queue_duration_seconds` | P95 > 60 秒 | Sidekiq Job 排隊過久，可能影響 MR 合併/通知延遲 |
| `gitlab_database_connection_pool_busy` | > 90% | PostgreSQL 連線池接近耗盡 |
| `grpc_server_handled_total{grpc_code!="OK"}`（Gitaly 端錯誤率） | 錯誤率 > 1% | Gitaly 層級異常，影響 Git 操作 |
| CI/CD Job 排隊時間 | > 5 分鐘 | Runner 容量不足 |
| Object Storage 用量增長率 | 月增 > 20% | 需檢查 Cleanup Policy 是否生效 |

### 20.3 Logging

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

### 20.4 升級

```bash
# 升級前務必先查閱官方 Upgrade Path，逐一經過必要停靠版本（19.x 為 19.2 / 19.5 / 19.8 / 19.11）
# 每一站都要升到該小版號的「最新修補版」，並等待背景遷移完成後才升下一站
sudo apt update
apt-cache madison gitlab-ee | grep ' 19\.5\.'        # 查詢 19.5 的最新修補版
sudo apt-get install gitlab-ee=19.5.<最新修補版>-ee.0

# 確認背景遷移（Batched background migrations）全部完成後才能升級下一站
sudo gitlab-rails runner -e production 'puts Gitlab::Database::BackgroundMigration::BatchedMigration.queued.count'

# 升級後驗證
sudo gitlab-rake gitlab:check SANITIZE=true
sudo gitlab-rake db:migrate:status
```

> 💡 **最佳實務**：
>
> - 正式環境升級前，先在與生產環境規格一致的 Staging 環境完整演練升級流程，並確認備份與還原機制可正常運作。
> - 以官方 Upgrade Path 工具確認所需的中繼版本，不可跳過必要停靠版本；背景遷移完成狀態也可在 **Admin area → Monitoring → Background migrations** 檢視。
> - 大版號升級（例如 18.x → 19.x）前，務必先閱讀該版本的升級說明（Upgrade notes），確認 PostgreSQL 等相依元件已符合新版需求（19.x 需 PostgreSQL 17）。

### 20.5 高可用性（HA）與災難復原（DR）

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

### 20.6 升級路徑規劃（GitLab 19.x）

> 🆕 **v2.0 新增**

以目前最新版 19.4 為例，Self-Managed 環境的升級路徑規劃如下：

| 目前版本 | 建議路徑 | 注意事項 |
|---|---|---|
| 18.x（< 18.11） | 依序升到 18.x 的必要停靠版本（18.2 → 18.5 → 18.8 → 18.11，只需經過比目前版本新的停靠站）→ 19.0 以後 | 升 19.0 前需先把 PostgreSQL 升到 17（18.9 起可用 PostgreSQL 17；單機 Linux package 可能在 18.11 嘗試自動升級，需預留磁碟空間） |
| 18.11 | 19.0 以後 → 19.2（停靠）→ 19.4 | 確認 Redis 7.x、作業系統仍在支援清單內（Ubuntu 20.04、SUSE 已不再提供套件） |
| 19.0／19.1 | 19.2（停靠）→ 19.4 | 每一站等待背景遷移完成 |
| 19.2／19.3 | 19.4 | 19.5 為下一個停靠站，後續升級需經過 19.5 |

**升級前檢查清單**：

1. 閱讀 GitLab 19 升級說明（Upgrade notes），確認每個跨越版本的破壞性變更。
2. 以官方 Upgrade Path 工具產生本環境的升級步驟。
3. 完成備份（含 `gitlab-secrets.json`、`gitlab.rb`），並確認可還原。
4. 確認背景遷移全部完成（見 20.4）。
5. 在 Staging 完整演練，記錄停機時間與異常。
6. 通知使用者維護窗口；Runner 與 `glab`、IDE 擴充套件的相容性一併確認。

> 💡 Helm chart 部署需依官方「Helm chart version mappings」對應 Chart 與 GitLab 版本（GitLab 19.x 對應 Chart 10.x），並注意 19.0 起 Chart 已移除內建 PostgreSQL、Redis、MinIO（見第三章 3.6）。

### 20.7 棄用與移除追蹤（GitLab 20.0）

> 🆕 **v2.0 新增**

GitLab 20.0 預定於 2027 年 5 月發布，官方已公告將移除下列與本手冊相關的功能（節錄，完整清單以官方「Deprecations and removals by version」為準）：

| 移除項目 | 影響 | 替代方案 |
|---|---|---|
| Compliance pipelines | 以 Compliance pipelines 強制必跑 Job 的合規設定將失效 | Pipeline execution policy（第十一章 11.10） |
| Docker Machine executor | Runner 自動擴縮失效 | Docker Autoscaler／Kubernetes executor（第八章 8.5） |
| Dependency Proxy for packages | 套件代理失效 | Maven Virtual Registry（第十章 10.7） |
| Legacy `retry:when` 失敗原因 `stuck_or_timeout_failure`、`job_execution_timeout` | 使用舊值的 `.gitlab-ci.yml` 需調整 | 19.0 起已拆成更細的原因：前者改用 `stuck_pending_with_matching_runners`、`stuck_pending_no_matching_runners`、`no_updates_running`、`no_updates_canceling`；後者改用 `server_timeout_running`、`server_timeout_canceling` |
| Helm chart 值 `gitlab.kas.ingress.grpc.enabled` | KAS Ingress 設定需調整 | 改用 `global.kas.ingress.grpc.enabled`（Chart 11.0 移除舊值） |
| Helm chart 內建的 NGINX Ingress、HAProxy、Traefik chart | 不再隨 Chart 部署 Ingress controller | 使用預設的 Envoy Gateway（Kubernetes Gateway API），或自行部署外部 Ingress controller |
| `kpt` 版本的 `agentk` 部署方式 | 以 kpt 安裝的 Kubernetes Agent 需重新部署 | 改用 Helm（建議）、GitLab CLI 或 Flux 安裝 |
| `gitlab-ctl patroni failover／switchover` 的 `--master` 選項 | DR 演練腳本需調整 | 19.4 起改用 `--leader` |
| GraphQL `CiJob.previousStageJobs` 欄位 | 使用此欄位的報表腳本需調整 | 官方表示不需伺服器端替代方案 |
| Design Management、Go module proxy（實驗性） | 相關功能移除 | 依官方說明遷移 |
| Audit events API 強制 keyset 分頁 | 以 offset 分頁的稽核腳本將失效 | 改用 keyset 分頁（第十二章 12.7） |

另外，Gemnasium 為核心的 Dependency Scanning 已提議於 20.0 移除（見第十一章 11.4）。

> 💡 **企業導入建議**：Platform 團隊可建立「GitLab 棄用追蹤」Epic，每季依官方 Deprecations 頁面更新子項目，並以 `glab api` 或 Advanced Search 盤點各專案是否仍使用即將移除的功能（例如在所有 `.gitlab-ci.yml` 搜尋 `stuck_or_timeout_failure`）。

### ✅ 第二十章 Checklist

- [ ] 已建立每日自動備份，並將資料備份與 `gitlab-secrets.json`/`gitlab.rb` 分開存放
- [ ] 已定期執行還原演練，驗證備份檔案實際可用
- [ ] 已設定 Prometheus + Grafana 監控核心指標並建立告警規則
- [ ] 已將日誌集中收集，並針對異常事件設定告警
- [ ] 升級前已在 Staging 環境完整演練，並依官方 Upgrade Path 操作
- [ ] 已規劃並至少演練過一次 HA Failover 與 DR 流程
- [ ] 已依必要停靠版本規劃年度升級路徑，並確認 PostgreSQL 17 等相依元件需求
- [ ] 已建立 20.0 棄用項目追蹤清單，並排定遷移時程

---

## 第二十一章 GitLab 最佳實務

### 21.1 命名規範

| 項目 | 規範建議 | 範例 |
|---|---|---|
| Group 名稱 | 全小寫、依組織架構分層 | `acme-corp/core-systems` |
| Project 名稱 | kebab-case，名詞+服務性質 | `order-service`、`payment-gateway` |
| 分支名稱 | `<類型>/<簡述>`，類型對應 Conventional Commits | `feature/order-refund`、`fix/login-redirect-bug`、`release/2.3.0` |
| Commit Message | Conventional Commits 格式 | `feat: 新增訂單退款 API`、`fix: 修正登入重導向錯誤` |
| Tag/版本號 | SemVer（語意化版本） | `v2.3.0`、`v3.0.0-rc.1` |
| CI/CD Variable | 全大寫、Snake Case | `DEPLOY_TOKEN`、`DATABASE_URL` |

### 21.2 Branch Strategy

- 優先採用 **GitLab Flow**（見第六章），依專案性質選 Environment Branch 或 Release Branch 模式。
- `main` 永遠保持可部署狀態，禁止直接 push，僅能透過已通過 Pipeline 與審核的 MR 合併。
- Feature 分支生命週期應盡量短（建議 < 3 天），降低與主線分歐的衝突風險；長期功能開發改用 Feature Flag 控制可見性，而非長期維護獨立分支。

### 21.3 MR Strategy

- MR 標題遵循 Conventional Commits 格式，描述需包含「問題」「修改」「測試」三段式結構（見第十四章 CLAUDE.md 範例）。
- 設定 **Approval Rules**：至少 1 位 Code Owner 核准；涉及安全敏感模組（如金流、權限）需額外指定安全團隊核准。
- 善用 `Closes #123` 語法自動關聯並關閉 Issue；大型變更使用 `glab stack` 拆解為多個易審查的小型 MR。
- 合併策略統一採用 **Squash and Merge**，保持 `main` 分支歷史簡潁，同時 MR 內保留完整開發歷程供日後追溯。

### 21.4 Pipeline Strategy

- 安全掃描、品質門檻等治理規則統一放在 Platform 團隊維護的共用 `ci-templates`，各專案 `include` 引用（見第七章 7.6）。
- 依 `rules` 精確控制 Job 觸發條件，避免每次 push 都跑完整 Pipeline（如僅變更文件時跳過建置/部署 Job）。
- 正式環境部署一律 `when: manual` + Protected Environment，留下明確的人工核准軌跡。
- 善用 Cache 加速重複建置，但 Cache Key 務必依賴實際內容（如 lockfile hash）而非固定字串，避免 Cache 失真。

### 21.5 Release Strategy

- 版本號採用 SemVer，搭配 `glab release create` 自動化發布流程，確保 Release Note 與實際合併內容一致。
- 正式發版前先在 Staging 完整驗收，搭配 Image Promotion（第九章 9.4）確保部署到生產環境的 Image 與驗收版本完全一致，不重新建置。
- 高風險發版（大版本/重大架構變更）採用 Canary 或 Blue-Green 部署，先驗證小流量後才全量切換。

### 21.6 Security Strategy

- 安全掃描三件套（SAST/Secret Detection/Dependency Scanning）為所有專案的強制基線，透過 Security Policies（Scan execution policy，Ultimate）統一強制執行，不可由個別專案關閉。
- Critical/High 漏洞設定明確 SLA 並追蹤逾期項目，定期於 Security Dashboard review。
- 機密一律透過 CI/CD Variables（Masked + Protected）或外部 Secret 管理工具（Vault）注入，禁止寫死於程式碼或設定檔。
- AI Agent 的寫入類操作（建立 MR、留言）可逐步開放，但合併、刪除、權限變更等高風險操作仍須人工核准（見第十四、十六章）。

> 💡 **實務案例**：某集團將上述六大策略整理為單一《GitLab 開發規範》內部文件，新進工程師到職第一週即依此規範完成第一個 MR 提交，相較過去依賴口頭傳承規範、新人平均 3 週才能掌握完整流程，導入規範文件後縮短至 5 個工作日。

### ✅ 第二十一章 Checklist

- [ ] 已制定並落實命名規範（Group/Project/分支/Commit/Tag/Variable）
- [ ] Branch/MR/Pipeline/Release/Security 六大策略已文件化並納入新人 Onboarding
- [ ] 治理規則已盡可能轉化為系統強制（Protected Branch、Compliance Framework + Security Policies），非僅依賴自律
- [ ] 已定期檢視並更新最佳實務文件，反映平台版本與團隊規模的變化

---

## 第二十二章 常見問題 FAQ

### 22.1 開發類

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

### 22.2 CI/CD 類

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

### 22.3 Security 類

**Q29. SAST 掃描沒有發現任何問題，代表程式碼絕對安全嗎？**
不代表。SAST 僅能偵測特定模式的已知問題類型，仍需搭配人工 Code Review、DAST、滲透測試等多層防禦。

**Q30. Dependency Scanning 與 Container Scanning 的差異？**
Dependency Scanning 掃描應用程式相依套件（如 `pom.xml`）；Container Scanning 掃描容器映像中作業系統層的套件漏洞，兩者互補。

**Q31. 誤判（False Positive）的漏洞該如何處理？**
在 Vulnerability Management 中標記為 `Dismissed` 並記錄理由，避免每次掃描重複出現干擾真正需要處理的項目。

**Q32. License Compliance 可以自動阻擋特定授權的套件嗎？**
可以（Ultimate）。在 Merge request approval policy 中設定 License 規則，禁止引入特定授權類型（如 GPL 系列）的套件或要求法務核准，未通過會阻擋 MR 合併（見第十一章 11.7）。

**Q33. Secret Push Protection 與 Secret Detection（CI 掃描）有何不同？**
Push Protection 在 `git push` 當下即時阻擋含機密的提交（事前防範）；Secret Detection 是 Pipeline 中事後掃描已提交的程式碼。

**Q34. 如何處理第三方相依套件已停止維護（EOL）但專案仍依賴的情況？**
建立 Issue 追蹤，評估替代方案或自行 Fork 維護，並在 Dependency Scanning 中暫時標記風險等級與處理計畫。

**Q35. DAST 掃描會不會把測試環境弄壞？**
有可能，Full Scan 會主動發送測試攻擊請求，務必僅對獨立的測試/Staging 環境執行，並評估是否需要搭配測試資料隔離。

**Q36. Compliance Framework 與 Protected Branch 的關係？**
Compliance Framework 本身是「合規標籤」，用來標記受監管的專案；真正的強制力來自以該 Framework 為範圍的 Security Policies（強制掃描、MR 審核、必跑 Job）與 Group 層級的 Protected Branch 設定。兩者搭配即可簡化大規模治理（見第十九章 19.7）。

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

### 22.4 Runner 類

**Q42. Instance Runner（舊稱 Shared Runner）與 Project Runner 可以同時使用嗎？**
可以，GitLab 會依 Job 的 `tags` 與設定自動選擇符合條件的 Runner，兩者並存很常見。

**Q43. Runner Registration Token 與 Runner Authentication Token 有何差異？**
新流程是先在 UI／API 建立 Runner（同時設定描述、Tags、是否 Protected 等屬性），再以取得的 `glrt-` Runner Authentication Token 執行 `gitlab-runner register`。舊的 Registration Token 自 GitLab 17.0 起預設停用，官方不建議重新啟用；新流程可追蹤個別 Runner 身分，安全性更高。

**Q44. Kubernetes Executor 的 Job Pod 為何一直 `Pending`？**
常見原因是 Namespace 資源配額不足或無法 Pull Image，使用 `kubectl describe pod` 確認具體原因。

**Q45. 如何讓特定 Job 只在擁有 GPU 的 Runner 上執行？**
為該 Runner 設定特殊 `tags`（如 `gpu`），並在 Job 的 `tags:` 中指定相同標籤。

**Q46. Runner 的 `concurrent` 設多少比較合適？**
依主機 CPU/Memory 容量與單個 Job 平均資源用量估算，並持續觀察 Job 排隊時間動態調整，沒有萬用的固定值。

**Q47. Docker Executor 與 Docker-in-Docker（dind）的差異？**
Docker Executor 是 Runner 本身的執行模式；dind 是當 Job 內需要「在容器裡執行 docker build」時的服務（`services: [docker:dind]`），兩者可同時搭配使用。

**Q48. 如何讓 Runner 自動依負載擴縮？**
Kubernetes Runner 搭配 Cluster Autoscaler／Karpenter，依 Pending Pod 數量自動增減節點；VM 型環境改用 Docker Autoscaler 或 Instance executor（Fleeting 外掛）。Docker Machine executor 已棄用，將於 GitLab 20.0 移除（見第八章 8.5）。

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

### 22.5 Kubernetes 類

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

### 22.6 AI 類

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

### 22.7 GitLab Duo 類

**Q80. GitLab Duo 需要額外付費嗎？**
依授權模型而定：Premium／Ultimate 內含 Duo Core，可使用 Duo Agent Platform（Agentic Chat、Code Suggestions、Agents、Flows），但依用量扣抵 **GitLab Credits**；Duo Pro／Enterprise 為座位制加購，提供 Non-Agentic 功能且不消耗 Credits；GitLab.com Free 方案也可購買 Credits 使用部分 Agent Platform 功能（見第十三章 13.1）。

**Q81. GitLab Duo Chat 能存取私有專案的程式碼嗎？**
能，Chat 會依使用者的權限範圍存取其有權檢視的專案上下文，不會超出該使用者原本的存取權限。

**Q82. Duo Code Suggestions 支援哪些 IDE？**
主流 IDE 如 VS Code、JetBrains 系列、Visual Studio、Neovim 等，透過官方 GitLab 擴充套件安裝。

**Q83. 如何排除特定檔案不被 Duo 用作 Context？**
`.gitlab/duo/` 目錄用於放置 Chat 規則、MR 審查指示、自訂 Flow 等客製化設定，並不是 Context 排除機制。要限制 AI 存取範圍，應透過 Instance／Group／專案層級的 GitLab Duo 開關與成員權限控制；在規則檔（`chat-rules.md`、`AGENTS.md`）中也可指示 Agent 忽略自動產生的程式碼與 vendor 目錄（見第十三章 13.7）。

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
可以。雲端連線（Online license）環境需允許連線至 GitLab AI Gateway；離線（Offline license）環境可採用 GitLab Duo Self-Hosted，Agent Platform 則需加購 Agent Platform Self-Hosted（18.8 起），以自行託管的模型運作。Duo Core 在離線授權的 Self-Hosted 模式下無法使用。

**Q90. Duo 的回答是否會被用於再訓練模型？**
依 GitLab 的資料處理政策而定，企業應於導入前確認資料隱私條款，特別是高合規需求的產業。

**Q91. 如何在 CI/CD Pipeline 中自動呼叫 Duo 功能？**
可使用 GitLab Duo CLI 的 Headless 模式 `glab duo cli run --goal "..."`（需 GitLab 19.2 以上）整合進 Pipeline，例如自動產生 Release Note 草稿；或使用 Agent Platform 的 Flow（如 Fix CI/CD Pipeline Flow）。涉及人工判斷的審查建議仍應留在 MR 互動流程中。

### 22.8 glab 類

**Q92. `glab` 與 `git` 指令可以混用嗎？**
可以，`glab` 是 `git` 的補充工具，專注於 GitLab 平台層面的操作（MR/Issue/Pipeline），版本控制本身仍使用標準 `git` 指令。

**Q93. 如何讓 CI/CD Job 中使用 `glab` 而不需要互動登入？**
在 GitLab CI/CD 中設定 `GLAB_ENABLE_CI_AUTOLOGIN=true` 由 `glab` 以 Job Token 自動登入，或執行 `glab auth login --job-token $CI_JOB_TOKEN`；權限不足時改以 Masked 變數注入 Project／Group Access Token 到 `GITLAB_TOKEN`。注意不要設定 `GITLAB_TOKEN=$CI_JOB_TOKEN`（第四章 4.8）。

**Q94. `glab` 設定檔內的 Token 加密嗎？**
`glab auth login` 預設把 Token 存進作業系統 Keyring（macOS Keychain、Windows Credential Manager、Linux Secret Service）。只有在沒有 Keyring、在 CI 中執行或使用 `--insecure-storage` 時，才會以明文存在設定檔；此時務必確保檔案權限正確（僅該使用者可讀），並避免提交進版本控制（第四章 4.6）。

**Q95. 如何用 `glab` 一次操作多個 GitLab Instance 的資源？**
在 Shell Script 中以 `GITLAB_HOST` 環境變數或 `-R <完整專案 URL>` 切換目標 Instance（一般指令沒有 `--hostname` 旗標），或分別針對不同 Instance 撰寫獨立的自動化腳本。

**Q96. `glab mr create --fill` 是什麼意思？**
自動依當前分支的 Commit Message 與分支名稱推斷 MR 標題與描述，省去手動輸入，適合搭配規範良好的 Conventional Commits。

**Q97. `glab` 是否支援 Windows PowerShell 環境？**
支援，`glab` 是跨平台單一執行檔，PowerShell、CMD、Git Bash 皆可直接呼叫。

**Q98. 如何排查 `glab` 指令回應 401/403 錯誤？**
確認 Token 是否過期或權限範圍（Scope）不足，使用 `glab auth status` 檢查目前登入狀態與對應 Instance。

**Q99. `glab api` 呼叫 GraphQL 時如何傳遞變數？**
在 Query 中宣告 `$variableName`，再以 `-f variableName=value`（字串）或 `-F variableName=value`（自動轉型）傳入；對 `glab api graphql` 而言，除了 `query` 與 `operationName` 以外的欄位都會被當成 GraphQL 變數。

**Q100. `glab` 的設定可以同步到團隊其他成員嗎？**
設定檔本身（含 Token）不應同步分享；但團隊可共用 Shell Alias/Script（不含個人 Token）統一常用指令的呼叫方式。

**Q101. 如何用 `glab` 快速找出「指派給我且即將逾期」的 Issue？**
`glab issue list --assignee=@me --milestone <Milestone ID> --order due_date --sort asc`，再搭配 `--label` 進一步篩選優先級。

**Q102. `glab` 支援自動完成（Shell Completion）嗎？**
支援，可透過 `glab completion -s bash`（或 `zsh`、`fish`、`powershell`）產生對應 Shell 的自動完成腳本並載入設定檔。

**Q103. `glab ci lint` 與 GitLab 後台的 CI Lint 工具差異？**
功能相同（驗證 `.gitlab-ci.yml` 語法），`glab ci lint` 讓開發者無需離開終端機即可在提交前驗證，加快回饋速度。

**Q104. 如何用 `glab` 比較兩個分支的差異後再決定是否建立 MR？**
先用標準 `git diff main...feature/xxx` 檢視差異，確認無誤後再用 `glab mr create`，避免建立 MR 後才發現範圍不如預期。

**Q105. 我們只有 Duo Core（Premium／Ultimate 內含），為什麼同事說 Duo Chat 突然不能用了？**
這不是 Bug。自 2026-05-21（GitLab 19.0）起，**Duo Core** 使用者已不能使用 Non-Agentic（傳統問答）Chat，改為使用 Agentic Chat 等 Duo Agent Platform 功能，且需具備 GitLab Credits。若組織沒有 Credits，或未開啟 Agent Platform，就會出現「Chat 不能用」的情況。解法是購買／分配 Credits 並開啟 Agent Platform，或為需要 Non-Agentic 功能的成員指派 Duo Pro／Enterprise 座位（詳見第十三章 13.2.1）。

**Q106. `glab` 裡標示為 Experimental 的指令（如 `mcp`、`stack`、`skills`、`orbit`、`work-items`）可以放進正式 CI/CD Pipeline 嗎？**
不建議。Experimental 代表指令格式與行為可能在後續版本異動或被移除，官方也明確表示尚未適合正式環境。企業應僅在 PoC、個人開發環境或內部創新專案中使用，且每次升級 `glab` 版本後都要重新驗證是否仍相容（詳見第四章 4.4 的穩定度分級表）。

**Q107. GitLab Orbit 是什麼？跟 MCP 有什麼不同？**
Orbit（Knowledge Graph）是 GitLab 建立的程式碼關聯圖，讓 AI Agent 可以直接查詢「誰呼叫誰、依賴哪些上游服務」等語意層級問題；MCP 則是讓 Agent 用標準化協定呼叫 GitLab 各項功能的「工具呼叫介面」。兩者是互補關係：MCP 負責結構化操作，Orbit 負責補強跨專案的語意上下文。目前 GitLab MCP server 為 Beta，Orbit 則為 Experimental（詳見第十六章 16.2、16.6）。

**Q108. GitLab MCP Server 現在用 stdio 還是 HTTP 比較好？**
官方建議直接以 **HTTP transport** 連接 GitLab 內建的 MCP server（`https://<gitlab>/api/v4/mcp`，OAuth 授權），不需要自行部署任何服務；不支援 HTTP 的用戶端才透過 `mcp-remote` 轉為 stdio。`glab mcp serve` 是另一個只支援 stdio 的本機 MCP server（Experimental），適合個人試用（詳見第十六章 16.2）。

**Q109. Dependency Scanning 為什麼最近開始出現棄用警告？**
舊版以 Gemnasium 引擎為核心的掃描方式已於 GitLab 17.9 起標示為棄用，並提議於 20.0 移除；以 SBOM／CycloneDX 為基礎的新版掃描已於 19.0 GA。若專案的 `.gitlab-ci.yml` 仍引用舊版範本，應改為 `Jobs/Dependency-Scanning.v2.gitlab-ci.yml`（詳見第十一章 11.4）。

### 22.9 版本更新類（v2.0 新增）

**Q110. 腳本裡的 `glab pipeline list` 還能用嗎？**
目前仍可執行，但 `pipeline` 與 `pipe` 都是已棄用的別名，官方要求改用 `glab ci`（例如 `glab ci list`、`glab ci view`、`glab ci trace`）。建議一次性全面替換，避免未來版本移除別名後腳本失效（見第五章 5.5）。

**Q111. `glab duo ask` 為什麼顯示找不到指令？**
`glab duo` 目前只有 `cli` 子指令，用來安裝與啟動 GitLab Duo CLI。互動使用請執行 `glab duo cli`，自動化請用 `glab duo cli run --goal "..."`；需要 GitLab 19.2 以上（見第五章 5.10）。

**Q112. GitLab 19.x 對資料庫有什麼新要求？**
GitLab 19.x 最低（也是最高）支援 PostgreSQL 17，PostgreSQL 16 已於 19.0 停止支援；Redis 建議 7.2（最低 7.0），亦支援 Valkey 7.2。升級到 19.0 前必須先完成 PostgreSQL 升級（見第三章 3.7、第二十章 20.6）。

**Q113. 可以從 18.3 直接升到 19.4 嗎？**
不行。必須依序經過必要停靠版本（18.5 → 18.8 → 18.11 → 19.2），每一站升到該版本的最新修補版，並等待背景遷移完成後才能升下一站（見第二十章 20.4、20.6）。

**Q114. GitLab MCP server 需要 Ultimate 嗎？**
不需要。GitLab 內建的 MCP server 自 19.2 起開放 Free 層級使用（仍為 Beta），但須由管理員（Self-Managed）或頂層 Group Owner（GitLab.com）開啟存取；透過 MCP 使用 Agent Platform 功能時，可能消耗 GitLab Credits（見第十六章）。

**Q115. Secret push protection 為什麼在我們的 Premium 專案找不到？**
Secret push protection 屬於 **Ultimate** 功能。Free／Premium 仍可使用 Pipeline Secret Detection（`Jobs/Secret-Detection.gitlab-ci.yml`）產生報告，但無法在 push 階段阻擋（見第十一章 11.1、11.6）。

**Q116. 為什麼 `License-Scanning.gitlab-ci.yml` 範本會讓 Pipeline 報錯？**
該範本與舊的 License Compliance 分析器已於 GitLab 17.0 移除。目前的 License Scanning 直接使用 Dependency Scanning 產生的 CycloneDX SBOM（Ultimate），請移除舊範本並改用 `Jobs/Dependency-Scanning.v2.gitlab-ci.yml`（見第十一章 11.7）。

**Q117. Docker Machine executor 什麼時候要遷移？**
Docker Machine executor 已於 17.5 棄用，預定在 GitLab 20.0（2027-05）移除，官方只修正重大問題。建議在 2026 年內完成 Docker Autoscaler 或 Kubernetes executor 的遷移（見第八章 8.5）。

**Q118. GitLab Credits 是什麼？會影響哪些功能？**
GitLab Credits 是 GitLab 用量計費的標準單位，用於 Duo Agent Platform（Agentic Chat、Agents、Flows）與部分其他功能。Duo Pro／Enterprise 的 Non-Agentic 功能不消耗 Credits。企業應設定預算與用量監控（見第十三章 13.1、13.8）。

**Q119. 怎麼讓 GitLab Duo 審查 MR 時遵循團隊規範？**
在 `.gitlab/duo/mr-review-instructions.yaml` 撰寫審查指示（可用 `fileFilters` 針對特定檔案），Code Review Flow 會依此審查；注意 Code Review Flow 不會讀取 `AGENTS.md` 與 `SKILL.md`（見第十三章 13.4、13.7）。

**Q120. 為什麼 `glab api ... --field state=opened --paginate` 會失敗？**
`glab api` 只要帶了 `-f`／`-F` 參數就會自動改用 POST。GET 查詢條件應寫在 URL 查詢字串中，例如 `glab api "projects/:id/merge_requests?state=opened" --paginate`（見第五章 5.9）。

**Q121. 我們的腳本用 `glab mr list --hostname ...` 切換 instance，升級後失效了？**
一般指令沒有 `--hostname` 旗標（1.120.0 也移除了部分指令自訂的 `--project`／`--hostname` 組合）。請改用 `GITLAB_HOST` 環境變數，或以 `-R` 帶入完整專案 URL（見第四章 4.6）。

> 💡 **使用建議**：以上 FAQ 依「開發、CI/CD、Security、Runner、Kubernetes、AI、GitLab Duo、glab、版本更新」九大分類整理，共 121 題。建議團隊將此 FAQ 納入新人 Onboarding 文件，並隨著平台版本更新與團隊實際遇到的問題持續擴充。

### ✅ 第二十二章 Checklist

- [ ] 新進團隊成員已閱讀本章 FAQ 並能自行排除常見問題
- [ ] 團隊已建立持續擴充 FAQ 的機制（如每次重大事故後補充對應問答）
- [ ] FAQ 內容已隨 GitLab/glab 版本更新定期校驗是否過時

---

## 第二十三章 附錄

### 23.1 常用 glab 指令速查表

> ⚠️ **v2.0 更正**：本表已依 glab v1.120.0 官方文件全面重寫（`pipeline` 改為 `ci`，並移除 `duo ask`、`mcp serve --transport http`、`orbit remote` 等不存在的用法）。

| 情境 | 指令 |
|---|---|
| 登入（瀏覽器 OAuth） | `glab auth login --hostname <host> --web` |
| 檢查所有 instance 登入狀態 | `glab auth status --all` |
| Clone 專案／整個 Group | `glab repo clone <group/project>`／`glab repo clone -g <group>` |
| 建立 MR（自動帶入 commit 資訊並 push） | `glab mr create --fill --target-branch main` |
| 列出需要我審查的 MR | `glab mr list --reviewer=@me` |
| Checkout MR | `glab mr checkout <id>` |
| 核准並 Squash 合併 | `glab mr approve <id> && glab mr merge <id> --squash` |
| 在 MR 留言 | `glab mr note create <id> -m "..."` |
| 建立 Issue | `glab issue create --title "..." --label bug` |
| 列出 Pipeline | `glab ci list --ref main` |
| 即時追蹤 Pipeline | `glab ci status --live`／`glab ci view` |
| 重跑失敗 Job／追蹤 Log | `glab ci retry <job>`／`glab ci trace <job>` |
| 驗證 CI 設定 | `glab ci lint --dry-run` |
| 下載 Job artifacts | `glab job artifact <ref> <job>` |
| 建立版本 | `glab release create v1.0.0 --notes-file CHANGELOG.md` |
| 設定機密變數 | `glab variable set KEY value --masked --protected` |
| 通用 API 呼叫 | `glab api "projects/:id/<endpoint>?<查詢條件>"` |
| 建立／輪替 Access Token | `glab token create ... --duration 30d`／`glab token rotate <name>` |
| 暫停 Runner | `glab runner update <id> --pause` |
| 容器倉庫 tag 清單 | `glab container-registry tag list <repository-id>` |
| 列出 Incident | `glab incident list` |
| GitLab Duo CLI（Headless） | `glab duo cli run --goal "..."` |
| 本機 MCP server（stdio，Experimental） | `glab mcp serve` |
| 連接 GitLab 內建 MCP server（Claude Code） | `claude mcp add -s user --transport http GitLab https://<gitlab>/api/v4/mcp` |
| 語意程式碼搜尋（Beta） | `glab search semantic -q "..."` |
| Orbit 知識圖譜（Experimental） | `glab orbit setup`／`glab orbit status` |
| 安裝 Agent Skills（Experimental） | `glab skills install` |
| 驗證 SLSA Provenance（Experimental，僅 GitLab.com） | `glab attestation verify <project> <artifact>` |
| 檢查 glab 新版 | `glab check-update` |

### 23.2 CI/CD 通用範本

```yaml
stages: [build, test, security, package, deploy]

workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'
    - if: '$CI_COMMIT_TAG'

include:
  - template: Jobs/SAST.gitlab-ci.yml
  - template: Jobs/Secret-Detection.gitlab-ci.yml
  - template: Jobs/Dependency-Scanning.v2.gitlab-ci.yml   # Ultimate

default:
  retry:
    max: 1
    when: runner_system_failure
```

### 23.3 Spring Boot 範本

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
  image: docker:29
  services: [docker:29-dind]
  script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" .
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

### 23.4 Vue3 範本

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

### 23.5 Kubernetes 範本

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
          image: registry.example.com/mygroup/order-service:1.4.0   # 使用不可變標籤，勿用 latest
          ports: [{ containerPort: 8080 }]
          resources:
            requests: { cpu: "500m", memory: "512Mi" }
            limits: { cpu: "1", memory: "1Gi" }
          readinessProbe:
            httpGet: { path: /actuator/health/readiness, port: 8080 }
          livenessProbe:
            httpGet: { path: /actuator/health/liveness, port: 8080 }
```

### 23.6 Docker 範本（多階段建置）

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

### 23.7 Helm 範本

```yaml
# values.yaml
replicaCount: 3
image:
  repository: registry.example.com/mygroup/order-service
  tag: ""   # 由 CI/CD 以 --set image.tag=$CI_COMMIT_SHORT_SHA 覆寫，避免使用 latest
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

### 23.8 十大 AI Agent 實戰情境總覽

本手冊已於各章節提供完整實戰教學，此處彙整對照表方便快速查找：

| 情境 | 對應章節 |
|---|---|
| 1. Claude Code + GitLab + glab | 第十四章 |
| 2. GitHub Copilot Agent + GitLab + glab | 第十五章 |
| 3. AI Agent 自動建立 Merge Request | 第十四章 14.2 |
| 4. AI Agent 自動 Review 程式碼 | 第十四章 14.3、第十三章 13.4（Code Review Flow） |
| 5. AI Agent 自動產生 Release Note | 見下方 23.8.1 |
| 6. AI Agent 自動分析 Legacy System | 第十七章 |
| 7. AI Agent 自動產生架構文件 | 見下方 23.8.2 |
| 8. AI Agent 協助 Spring Boot 升級 | 第十八章 18.2 |
| 9. AI Agent 協助 Vue 升級 | 第十八章 18.3 |
| 10. AI Agent 協助大型共用平台開發 | 見下方 23.8.3 |

#### 23.8.1 AI Agent 自動產生 Release Note

**情境**：發版前，請 AI Agent 彙整自上一個 Tag 以來所有已合併的 MR，自動產生結構化 Release Note。

```bash
# 取得指定日期後合併到 main 的所有 MR（GET 查詢條件寫在 URL，避免 --field 讓請求變成 POST）
glab api "projects/:id/merge_requests?state=merged&target_branch=main&updated_after=2026-09-01T00:00:00Z" \
  --paginate --output ndjson \
  | jq -r 'select(.merged_at > "2026-09-01") | "- \(.title) (!\(.iid))"'
```

請 Claude Code 或 Duo 依下列 Prompt 整理：

```text
請依照下方 MR 標題清單，依 Conventional Commits 類型（feat/fix/refactor/docs）分類，
產生結構化的 Release Note（含「新功能」「修復」「其他變更」三個段落），
並標示每項變更對應的 MR 編號方便追溯。
```

```bash
glab release create v2.4.0 --notes-file ./CHANGELOG-2.4.0.md

# 若 commit 已遵循 Conventional Commits 並設定 changelog trailer，也可直接由 GitLab 產生
glab changelog generate --version 2.4.0 > ./CHANGELOG-2.4.0.md
```

> 💡 **最佳實務**：搭配 Conventional Commits 規範（第二十一章），AI 產生的 Release Note 分類準確度會大幅提升；若 Commit Message 格式混亂，建議先要求 AI 進行「語意分類」而非單純字串比對。

#### 23.8.2 AI Agent 自動產生架構文件

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
  # 需 GitLab 19.2 以上，且 Runner 映像已安裝 glab、可執行 GitLab Duo CLI（見第五章 5.10）
  script:
    - glab duo cli run --goal "比較目前 docs/architecture.md 與最新程式碼結構，列出需要更新的差異點，不要修改任何檔案" > arch-diff-report.txt
  artifacts:
    paths: [arch-diff-report.txt]
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
  allow_failure: true
```

#### 23.8.3 AI Agent 協助大型共用平台開發

**情境**：Platform 團隊開發供多個應用團隊共用的內部平台（如共用元件庫、API Gateway 設定、CI/CD 範本），需確保變更不會破壞既有使用方。

```text
請分析這次對 ci-templates 共用範本的修改，列出目前所有引用（include）此範本的專案清單，
並評估此次變更是否為 Breaking Change，若是，請列出每個受影響專案需要配合調整的項目。
```

```bash
# 以 Group 程式碼搜尋找出所有引用共用範本的專案（需啟用進階搜尋或精確程式碼搜尋）
glab api "groups/<group-id>/search?scope=blobs&search=ci-templates" --paginate --output ndjson \
  | jq -r '.project_id' | sort -u

# 針對每個受影響專案，AI Agent 可批次建立通知 Issue
glab issue create --title "⚠️ ci-templates v3.0.0 升級，需確認相容性" \
  --description "本次升級包含 Breaking Change：... 請於 2026-07-01 前完成驗證。" \
  --label "platform-notice"
```

> 💡 **企業導入建議**：大型共用平台開發應建立「變更影響分析」為標準流程的一部分，AI Agent 可大幅加速「找出誰受影響」與「產生通知內容」的工作，但**版本相容性策略與 Breaking Change 的發布節奏，仍應由 Platform 團隊架構師決策**，AI 僅負責執行與彙整。

### 23.9 企業導入檢查清單

- [ ] 已完成部署形態選型（SaaS / Self-Managed / Dedicated）並評估資料主權與維運人力
- [ ] 已建立多層 Group 結構與最小權限模型，Service Account 與真人帳號分離
- [ ] 已制定命名規範、分支策略、MR 策略並文件化
- [ ] 已建立共用 CI/CD 範本，安全掃描三件套（SAST/Secret Detection/Dependency Scanning）為強制基線
- [ ] 已設定 Protected Branch、Approval Rules，正式環境部署需人工核准
- [ ] 已建立 Container/Package Registry 的 Cleanup Policy 與版本治理規範
- [ ] 已建立備份/還原、監控告警、HA/DR 演練機制
- [ ] 已導入 GitLab Duo / Claude Code / Copilot 等 AI 工具，並建立對應的使用規範與稽核機制
- [ ] 已確認 Duo 授權（Duo Core／Pro／Enterprise、GitLab Credits），完成 Duo Core 改用 Agentic Chat 的因應，並完成 GitLab Duo Agent Platform 的導入評估
- [ ] 已評估 GitLab MCP server（Beta）與 Orbit（Experimental）整合，並先以限縮的工具範圍試行
- [ ] 已依必要停靠版本排定年度升級計畫，並追蹤 GitLab 20.0 的移除項目
- [ ] 已將所有腳本的 `glab pipeline` 改為 `glab ci`，並固定 `glab` 版本
- [ ] 已建立新人 Onboarding 文件（含本手冊 FAQ 與速查表）
- [ ] 已制定 Legacy System 逆向工程與 Framework 升級的標準作業流程
- [ ] 已建立 DevSecOps 平台的長期治理機制（定期稽核、規則更新、團隊培訓）

### 23.10 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v1.0 | 2026-06-24 | 初版：GitLab、glab、CI/CD、Runner、Security、Duo、MCP、AI 協作開發與企業導入 |
| v2.0 | 2026-09-30 | 依 GitLab 19.4、Runner 19.4.1、glab v1.120.0 全面查證改版：修正 glab 指令、MCP、Duo 授權、安全掃描 Tier 與範本；新增 CI/CD Components、inputs、OIDC、Runner 自動擴縮、Security Policies、Token 治理、升級路徑與 20.0 移除追蹤；修正 Markdown 標題層級並重建目錄 |

#### 23.10.1 v1.0 → v2.0 主要更正一覽

| # | 章節 | 初版內容 | v2.0 更正 |
|---|---|---|---|
| 1 | 4.3、5.5、全文 | 以 `glab pipeline` 操作 CI/CD | `pipeline`／`pipe` 為棄用別名，改用 `glab ci` |
| 2 | 4.3、5.8 | `glab project` 指令 | 不存在；改用 `label`、`milestone`、`repo members` 或 `glab api` |
| 3 | 4.4（原 4.3.1） | `orbit` 為 Beta、`search` 為 Stable | `orbit` 為 Experimental、`search` 為 Beta；補列 `attestation`、`security`、`dependency-firewall`、`govern`、`artifact-registry` 等 Experimental 指令 |
| 4 | 4.5 | WinGet ID `GitLab.GLab`；`permalink/latest/downloads/glab_amd64.deb` | WinGet ID `glab.glab`；Linux 套件檔名含版本號 |
| 5 | 4.5 | `glab mr list --hostname` 切換 instance | 一般指令無 `--hostname`；改用 `GITLAB_HOST` 或 `-R <完整 URL>` |
| 6 | 5.3 | `glab mr list --reviewer-state`；`glab mr note --message` | `--reviewer=@me`；`glab mr note create -m` |
| 7 | 5.9、23.8.1 | `glab api ... --field state=opened` 作為查詢條件 | `--field` 會改為 POST，查詢條件應寫在 URL |
| 8 | 5.10、13.2、13.4 | `glab duo ask`、`--file`、`--mr` | 不存在；改為 `glab duo cli`（GitLab Duo CLI，19.2 GA） |
| 9 | 5.11、16.2、16.4 | `glab mcp serve --transport http --port`、`--read-only`、`--tools` | `glab mcp serve` 僅 stdio 且為 Experimental；HTTP 端點為 GitLab 內建 MCP server `/api/v4/mcp` |
| 10 | 5.12、18.3 | `glab stack create --parent` | 無 `--parent`；以 `glab stack save`、`glab stack sync` 疊加各層 |
| 11 | 5.13 | `glab search code／issues／mrs` | 只有 `glab search semantic`（Beta） |
| 12 | 5.14 | `glab schedule create --variables` | 正確旗標為 `--variable`；新增 `--cronTimeZone` |
| 13 | 5.15、8.4 | `glab runner register／pause／resume` | 不存在；註冊用 `gitlab-runner register`，暫停用 `glab runner update --pause` |
| 14 | 5.16、16.6 | `glab orbit local setup`、`glab orbit remote --query` | 改為 `glab orbit setup`、`status`、`query`、`index`、`grep` |
| 15 | 5.17 | `glab skills install gitlab/mr-create-flow` | 安裝 `glab` 內建 Skills，例如 `glab skills install glab-stack` |
| 16 | 5.18 | `glab attestation verify <image> --signing-key` | `glab attestation verify <project-id> <artifact-path>`，僅 GitLab.com |
| 17 | 5.20 | `tag list order-service`、`--tag-name` | 參數為 repository ID；刪除直接給 tag 名稱或使用批次旗標 |
| 18 | 7.1、9.4、18.2 | Job 層級同時使用 `rules` 與 `when: manual` | 設定無效；`when: manual` 移入 `rules` 內 |
| 19 | 8.2 | `gitlab-runner register --description`；Helm `runners.config=concurrent = 20` | 新流程屬性於 UI／API 建立 Runner 時設定；Helm 使用 `concurrent` 與 `runners.config` values |
| 20 | 9.6 | Virtual Registry API `groups/:id/virtual_registries/packages/container`、`upstream_url` | 正確為 `groups/:id/-/virtual_registries/container/registries` 與 `.../upstreams`（`url`） |
| 21 | 10.1 | Gradle、pnpm 為獨立格式 | 分別使用 Maven、npm 格式；補充各格式 GA／Beta／Experiment 狀態 |
| 22 | 11.x | 範本路徑 `Security/SAST`、`Security/Dependency-Scanning`、`DAST.gitlab-ci.yml` | `Jobs/SAST`、`Jobs/Dependency-Scanning.v2`、`Security/DAST`；DAST 變數改 `DAST_TARGET_URL`、`DAST_FULL_SCAN` |
| 23 | 11.6 | 以 `PUT projects/:id` 開啟 `secret_push_protection_enabled` | 需使用 Project／Group Security Settings API；功能為 Ultimate |
| 24 | 11.7 | `License-Scanning.gitlab-ci.yml` 範本 | 已於 17.0 移除；改由 Dependency Scanning SBOM 提供 |
| 25 | 13.x | 「Core 方案」「Core／Pro／Ultimate」 | Duo add-on 為 Core／Pro／Enterprise；Agent Platform 以 GitLab Credits 計價 |
| 26 | 13.3、22.7 | `.gitlab/duo/` Context 排除規則 | 非官方機制；`.gitlab/duo/` 放置 `chat-rules.md`、`mr-review-instructions.yaml` 等 |
| 27 | 16.3 | Claude Code 設定檔 `~/.claude/mcp_settings.json` | 以 `claude mcp add` 或專案 `.mcp.json` 設定，OAuth 授權 |
| 28 | 17.2、18.2 | `glab api projects/:id/epics` | Epic 為 Group 層級；改用 `glab work-items create --type epic` |
| 29 | 20.2 | `grafana['enable']` | Linux package 自 16.3 起不再內建 Grafana |
| 30 | 20.4 | 升級範例 `gitlab-ee=17.5.0` | 依 19.x 必要停靠版本（19.2／19.5／19.8／19.11）並確認背景遷移 |
| 31 | 2.3 | 以使用者人數分級 Reference Architecture | 官方以 RPS 為主要指標 |
| 32 | 3.3 | Rocky Linux | 官方支援清單為 RHEL、AlmaLinux、Oracle Linux |
| 33 | 格式 | 章節使用 H1、目錄不含小節、`## 4.3.1` 層級錯誤、MD032／MD040 | 章為 `##`、節為 `###`；目錄自動產生並含編號小節；修正格式問題 |

### 23.11 查證紀錄

v2.0 以官方原始文件為主要依據（GitLab 文件原始檔、`gitlab-org/cli` 自動產生的指令文件、GitLab Runner 文件、官方 Release API），查證日期均為 **2026-09-30**。

| # | 查證項目 | 查證結果 | 依據 |
|---|---|---|---|
| 1 | GitLab 最新版本 | 19.4.0（2026-09-16）、19.4.1（2026-09-22，同日發布 19.3.3、19.2.7） | gitlab-org/gitlab 版本標籤 |
| 2 | GitLab Runner 最新版本 | 19.4.1（2026-09-24） | gitlab-org/gitlab-runner Releases |
| 3 | glab 最新版本 | v1.120.0（2026-09-29），約每週一版 | gitlab-org/cli Releases |
| 4 | glab 頂層指令與狀態 | 45 個頂層指令；Experimental／Beta 標示如第四章 4.4 | docs.gitlab.com/cli 各指令頁 |
| 5 | `glab pipeline` 別名 | 已棄用，改用 `glab ci` | `glab ci` 指令頁 |
| 6 | `glab duo` | 僅 `cli` 子指令；需 GitLab 19.2+ | `glab duo`、`glab duo cli` 指令頁 |
| 7 | `glab mcp serve` | Experimental、stdio transport | `glab mcp serve` 指令頁 |
| 8 | glab CI 認證 | `GLAB_ENABLE_CI_AUTOLOGIN`、`--job-token`；勿設 `GITLAB_TOKEN=$CI_JOB_TOKEN` | glab Authentication 文件 |
| 9 | glab 設定檔與環境變數 | 設定檔路徑順序、Keyring 儲存 | glab Configuration／Authentication 文件 |
| 10 | GitLab MCP server | Beta；18.6 支援 HTTP；19.2 移至 Free；支援 2025-03-26／06-18／11-25 協定；Toolset Header（19.5，功能旗標） | MCP server 文件 |
| 11 | Claude Code 連接方式 | `claude mcp add -s user --transport http GitLab https://<host>/api/v4/mcp` | MCP server 文件「Connect Claude Code」 |
| 12 | Duo add-ons | Core／Pro／Enterprise；2026-05-21 起 Duo Core 無 Non-Agentic Chat | GitLab Duo add-ons 文件 |
| 13 | Duo Agent Platform | 18.2 Beta、18.8 GA；功能與方案對照 | GitLab Duo Agent Platform 文件 |
| 14 | Code Review Flow | 18.7 Beta、18.8 GA；`@GitLabDuo`；`mr-review-instructions.yaml` | Code Review Flow、Review instructions 文件 |
| 15 | GitLab Duo CLI | 18.9 Experiment、18.11 Beta、19.2 GA（Duo CLI 9.0.0） | GitLab Duo CLI 文件 |
| 16 | 安全掃描 Tier | Secret push protection、Dependency scanning、DAST、Security Dashboard 為 Ultimate；SAST、Container Scanning 基本功能為 Free | 各安全功能文件 |
| 17 | Dependency Scanning | SBOM 版 19.0 GA；Gemnasium 17.9 棄用、提議 20.0 移除；19.4 新增惡意套件公告比對 | Dependency scanning 文件 |
| 18 | License Scanning | 舊範本 17.0 移除；CycloneDX 授權掃描 | License scanning 文件 |
| 19 | Secret push protection 開關 | 使用 Project／Group Security Settings API | Projects API、Group security settings API |
| 20 | DAST 變數 | `DAST_TARGET_URL`、`DAST_FULL_SCAN`；範本 `Security/DAST.gitlab-ci.yml` | DAST 文件 |
| 21 | 安裝需求 | 8 vCPU／16 GB；19.x 需 PostgreSQL 17；Redis 7.2／Valkey 7.2 | Installation requirements |
| 22 | 支援作業系統 | Ubuntu 22.04／24.04／26.04、Debian 11–13、AlmaLinux／RHEL／Oracle 8–10、Amazon Linux 2023 | Linux package 支援平台 |
| 23 | 必要升級停靠版本 | 17.5 起為 x.2／x.5／x.8／x.11；19.x 為 19.2／19.5／19.8／19.11 | Upgrade paths 文件 |
| 24 | Reference Architecture | 以 RPS 為主要指標；1k～50k 使用者對照表 | Reference architectures 文件 |
| 25 | Runner 註冊 | `glrt-` Token；Registration Token 17.0 起預設停用 | New runner registration workflow |
| 26 | Docker Machine executor | 17.5 棄用，20.0（2027-05）移除 | Docker Machine executor 文件 |
| 27 | Token 類型與前綴 | `glpat-`、`gldt-`、`glrt-`、`glcbt-`、`glptt-`、`glagent-` 等；預設效期 365 天 | GitLab token overview、PAT 文件 |
| 28 | Fine-grained PAT | 18.10 Beta、19.2 GA | Fine-grained access tokens 文件 |
| 29 | Container Virtual Registry API | `groups/:id/-/virtual_registries/container/registries`、`.../upstreams` | Container virtual registries API |
| 30 | Package Registry 格式 | Maven／npm／NuGet／PyPI／Helm／Generic GA；Composer、Conan Beta；Debian、Go、Ruby gems Experiment | Supported package managers |
| 31 | 20.0 移除項目 | Compliance pipelines、Dependency Proxy for packages、retry:when 舊原因、KAS chart 值、kpt agentk、`--master` 等 | Deprecations and removals by version |
| 32 | Helm chart 19.0 變更 | 移除內建 PostgreSQL、Redis、MinIO | Deprecations（GitLab 19.0） |
| 33 | CI/CD Components 與 inputs | `include: component`、版本引用、`spec:inputs` 型別 | CI/CD components、CI/CD inputs 文件 |
| 34 | OIDC ID Token | `id_tokens`、`sub` 格式 `project_path:...:ref_type:...:ref:...` | OpenID Connect authentication 文件 |
| 35 | Security Manager 角色 | 18.11 Beta，預設停用 | Roles and permissions 文件 |

#### 23.11.1 待確認事項

以下項目在本次查證時仍在變動中，建議下次改版優先確認：

1. **GitLab 19.5（預定 2026-10）**：MCP server Toolset 選擇（功能旗標 `mcp_toolsets`）是否預設開啟；Code Review Flow 自動審查預設開啟的範圍。
2. **Security Manager 角色**何時 GA，以及預設權限是否調整。
3. **Orbit** 何時由 Experimental 升級，以及 `glab orbit` 子指令是否穩定。
4. **`glab mcp serve`**、`glab stack`、`glab work-items` 是否脫離 Experimental。
5. **Gemnasium Dependency Scanning** 是否確定於 20.0 移除（目前為「提議移除」）。
6. **GitLab Credits** 的計價、Duo Core 用量上限與 Free 方案可用範圍的後續調整。
7. **GitLab 20.0（2027-05）** 最終移除清單，以及 Helm chart 11.0 的變更。
8. **`glab attestation`** 是否支援 Self-Managed 環境。

### 23.12 參考資料

| 主題 | 官方文件 |
|---|---|
| GitLab 文件首頁 | <https://docs.gitlab.com/> |
| GitLab CLI（glab） | <https://docs.gitlab.com/cli/> |
| glab 原始碼與 Releases | <https://gitlab.com/gitlab-org/cli> |
| 安裝需求 | <https://docs.gitlab.com/install/requirements/> |
| 升級路徑 | <https://docs.gitlab.com/update/upgrade_paths/> |
| 棄用與移除清單 | <https://docs.gitlab.com/update/deprecations/> |
| Reference architectures | <https://docs.gitlab.com/administration/reference_architectures/> |
| CI/CD YAML 語法 | <https://docs.gitlab.com/ci/yaml/> |
| CI/CD Components | <https://docs.gitlab.com/ci/components/> |
| CI/CD inputs | <https://docs.gitlab.com/ci/inputs/> |
| OIDC ID Token | <https://docs.gitlab.com/ci/secrets/id_token_authentication/> |
| GitLab Runner | <https://docs.gitlab.com/runner/> |
| Application security | <https://docs.gitlab.com/user/application_security/> |
| Security policies | <https://docs.gitlab.com/user/application_security/policies/> |
| GitLab token overview | <https://docs.gitlab.com/security/tokens/> |
| GitLab Duo Agent Platform | <https://docs.gitlab.com/user/duo_agent_platform/> |
| GitLab Duo add-ons | <https://docs.gitlab.com/subscriptions/subscription-add-ons/> |
| GitLab MCP server | <https://docs.gitlab.com/user/model_context_protocol/mcp_server/> |
| GitLab Duo CLI | <https://docs.gitlab.com/user/gitlab_duo_cli/> |
| Package registry | <https://docs.gitlab.com/user/packages/package_registry/> |
| Virtual registry | <https://docs.gitlab.com/user/packages/virtual_registry/> |

### ✅ 第二十三章 Checklist

- [ ] 團隊已將本附錄速查表與範本納入內部 Wiki 或 `ci-templates` 共用專案
- [ ] 十大 AI Agent 實戰情境已對應到團隊實際工作流程並至少試行一項
- [ ] 企業導入檢查清單已由 Platform/DevOps/Security 團隊共同確認逐項完成

---

> 📘 **手冊結語**：本手冊（v2.0）以 GitLab 19.4、GitLab Runner 19.4.1、glab v1.120.0 為基準，涵蓋 GitLab 與 GitLab CLI（glab）從基礎概念到企業級大規模導入的完整知識體系，並深度整合 AI 協作開發情境（GitLab Duo Agent Platform、Claude Code、GitHub Copilot、MCP）。建議團隊將本文件作為內部開發規範的基礎，依實際組織狀況調整章節中的命名規範、權限模型與治理流程，並依附錄 23.11.1 的待確認事項，隨 GitLab 版本演進持續更新內容。
