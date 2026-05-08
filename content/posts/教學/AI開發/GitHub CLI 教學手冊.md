+++
date = '2026-05-08T16:24:49+08:00'
draft = false
title = 'GitHub CLI 教學手冊'
tags = ['教學', 'AI開發','指引']
categories = ['教學']
+++

# GitHub CLI 教學手冊

> **版本**：基於 GitHub CLI v2.74.0（2026-05 最新穩定版）  
> **適用對象**：資深工程師 / DevOps 工程師 / 架構師 / SRE / AI 團隊  
> **技術環境**：企業級 Web Application（Spring Boot / Vue / 微服務架構）  
> **最後更新**：2026-05-08

---

## 目錄

- [第 1 章：GitHub CLI 概述](#第-1-章github-cli-概述)
  - [1.1 GitHub CLI 是什麼](#11-github-cli-是什麼)
  - [1.2 為何企業要導入 GitHub CLI](#12-為何企業要導入-github-cli)
  - [1.3 GitHub CLI 架構](#13-github-cli-架構)
  - [1.4 GitHub CLI 與 Git 的差異](#14-github-cli-與-git-的差異)
  - [1.5 GitHub CLI 與 GitHub API 的關係](#15-github-cli-與-github-api-的關係)
  - [1.6 GitHub CLI 使用情境](#16-github-cli-使用情境)
  - [1.7 GitHub CLI 優缺點](#17-github-cli-優缺點)
- [第 2 章：GitHub CLI 安裝與環境建置](#第-2-章github-cli-安裝與環境建置)
  - [2.1 Windows 安裝](#21-windows-安裝)
  - [2.2 macOS 安裝](#22-macos-安裝)
  - [2.3 Linux 安裝](#23-linux-安裝)
  - [2.4 WSL 安裝](#24-wsl-安裝)
  - [2.5 驗證安裝](#25-驗證安裝)
  - [2.6 Proxy 設定](#26-proxy-設定)
  - [2.7 公司內網設定](#27-公司內網設定)
  - [2.8 SSH Key 建立](#28-ssh-key-建立)
  - [2.9 GPG Key 建立](#29-gpg-key-建立)
  - [2.10 Git 設定](#210-git-設定)
  - [2.11 GitHub Login](#211-github-login)
  - [2.12 Token 管理](#212-token-管理)
  - [2.13 PAT 管理](#213-pat-管理)
- [第 3 章：GitHub Authentication 與安全管理](#第-3-章github-authentication-與安全管理)
  - [3.1 gh auth login](#31-gh-auth-login)
  - [3.2 gh auth status](#32-gh-auth-status)
  - [3.3 gh auth refresh](#33-gh-auth-refresh)
  - [3.4 gh auth logout](#34-gh-auth-logout)
  - [3.5 SSH Authentication](#35-ssh-authentication)
  - [3.6 HTTPS Authentication](#36-https-authentication)
  - [3.7 PAT Token](#37-pat-token)
  - [3.8 Fine-grained Token](#38-fine-grained-token)
  - [3.9 SSO](#39-sso)
  - [3.10 Enterprise Authentication](#310-enterprise-authentication)
  - [3.11 最佳安全實務](#311-最佳安全實務)
  - [3.12 Token Rotation](#312-token-rotation)
  - [3.13 Secret 管理](#313-secret-管理)
  - [3.14 Least Privilege 原則](#314-least-privilege-原則)
- [第 4 章：GitHub Repo 管理](#第-4-章github-repo-管理)
  - [4.1 建立 Repo](#41-建立-repo)
  - [4.2 Clone Repo](#42-clone-repo)
  - [4.3 Fork Repo](#43-fork-repo)
  - [4.4 Rename Repo](#44-rename-repo)
  - [4.5 Delete Repo](#45-delete-repo)
  - [4.6 Archive Repo](#46-archive-repo)
  - [4.7 Template Repo](#47-template-repo)
  - [4.8 Monorepo](#48-monorepo)
  - [4.9 Polyrepo](#49-polyrepo)
  - [4.10 Repo 命名規範](#410-repo-命名規範)
  - [4.11 Repo Governance](#411-repo-governance)
  - [4.12 Repo 權限管理](#412-repo-權限管理)
  - [4.13 Team 管理](#413-team-管理)
- [第 5 章：Source Code 上架與管理](#第-5-章source-code-上架與管理)
  - [5.1 Git 初始化](#51-git-初始化)
  - [5.2 Push Source Code](#52-push-source-code)
  - [5.3 Branch 管理](#53-branch-管理)
  - [5.4 Git Flow](#54-git-flow)
  - [5.5 Trunk Based Development](#55-trunk-based-development)
  - [5.6 Feature Branch](#56-feature-branch)
  - [5.7 Release Branch](#57-release-branch)
  - [5.8 Hotfix Branch](#58-hotfix-branch)
  - [5.9 Commit Convention](#59-commit-convention)
  - [5.10 Pull Request Flow](#510-pull-request-flow)
  - [5.11 Code Review Flow](#511-code-review-flow)
- [第 6 章：文件管理策略](#第-6-章文件管理策略)
  - [6.1 Markdown 文件管理](#61-markdown-文件管理)
  - [6.2 docs 結構](#62-docs-結構)
  - [6.3 ADR 管理](#63-adr-管理)
  - [6.4 Architecture 文件](#64-architecture-文件)
  - [6.5 API 文件](#65-api-文件)
  - [6.6 README 標準化](#66-readme-標準化)
  - [6.7 Wiki 管理](#67-wiki-管理)
  - [6.8 GitHub Pages](#68-github-pages)
- [第 7 章：GitHub CLI 常用指令大全](#第-7-章github-cli-常用指令大全)
  - [7.1 gh repo](#71-gh-repo)
  - [7.2 gh pr](#72-gh-pr)
  - [7.3 gh issue](#73-gh-issue)
  - [7.4 gh release](#74-gh-release)
  - [7.5 gh workflow](#75-gh-workflow)
  - [7.6 gh run](#76-gh-run)
  - [7.7 gh api](#77-gh-api)
  - [7.8 gh alias](#78-gh-alias)
  - [7.9 gh extension](#79-gh-extension)
  - [7.10 gh browse](#710-gh-browse)
  - [7.11 gh codespace](#711-gh-codespace)
  - [7.12 gh gist](#712-gh-gist)
  - [7.13 gh project](#713-gh-project)
  - [7.14 gh search](#714-gh-search)
  - [7.15 gh cache](#715-gh-cache)
  - [7.16 gh attestation](#716-gh-attestation)
  - [7.17 gh ruleset](#717-gh-ruleset)
  - [7.18 gh label](#718-gh-label)
  - [7.19 gh variable](#719-gh-variable)
  - [7.20 gh secret](#720-gh-secret)
  - [7.21 gh status](#721-gh-status)
  - [7.22 gh config](#722-gh-config)
- [第 8 章：GitHub Actions 與 Workflow Automation](#第-8-章github-actions-與-workflow-automation)
  - [8.1 GitHub Actions 架構](#81-github-actions-架構)
  - [8.2 Workflow 基礎](#82-workflow-基礎)
  - [8.3 Runner 與 Self-hosted Runner](#83-runner-與-self-hosted-runner)
  - [8.4 Matrix Build](#84-matrix-build)
  - [8.5 Cache 與 Artifact](#85-cache-與-artifact)
  - [8.6 Secret 與 Environment](#86-secret-與-environment)
  - [8.7 CI Workflow 範例](#87-ci-workflow-範例)
  - [8.8 CD Workflow 範例](#88-cd-workflow-範例)
  - [8.9 Release Workflow 範例](#89-release-workflow-範例)
  - [8.10 Security Scan Workflow](#810-security-scan-workflow)
  - [8.11 AI Workflow](#811-ai-workflow)
- [第 9 章：SSDLC 與 Security](#第-9-章ssdlc-與-security)
  - [9.1 Secret Scanning](#91-secret-scanning)
  - [9.2 Dependabot](#92-dependabot)
  - [9.3 CodeQL](#93-codeql)
  - [9.4 Security Policy](#94-security-policy)
  - [9.5 Branch Protection](#95-branch-protection)
  - [9.6 CODEOWNERS](#96-codeowners)
  - [9.7 Signed Commit](#97-signed-commit)
  - [9.8 Supply Chain Security 與 SBOM](#98-supply-chain-security-與-sbom)
  - [9.9 OWASP 與 DevSecOps](#99-owasp-與-devsecops)
  - [9.10 SAST 與 DAST](#910-sast-與-dast)
- [第 10 章：GitHub CLI 自動化腳本](#第-10-章github-cli-自動化腳本)
  - [10.1 Bash Script](#101-bash-script)
  - [10.2 PowerShell Script](#102-powershell-script)
  - [10.3 Windows Batch](#103-windows-batch)
  - [10.4 Python Script](#104-python-script)
  - [10.5 Repo 初始化自動化](#105-repo-初始化自動化)
  - [10.6 Branch Protection 自動化](#106-branch-protection-自動化)
  - [10.7 Release Automation](#107-release-automation)
- [第 11 章：AI 整合與 Copilot](#第-11-章ai-整合與-copilot)
  - [11.1 GitHub Copilot CLI](#111-github-copilot-cli)
  - [11.2 GitHub Copilot 在 PR Review 中的應用](#112-github-copilot-在-pr-review-中的應用)
  - [11.3 AI-Powered Workflow](#113-ai-powered-workflow)
  - [11.4 Copilot 與 GitHub CLI 整合最佳實務](#114-copilot-與-github-cli-整合最佳實務)
  - [11.5 GitHub CLI Telemetry 管理](#115-github-cli-telemetry-管理)
  - [11.6 AI Agent 整合策略](#116-ai-agent-整合策略)
- [第 12 章：企業級最佳實務](#第-12-章企業級最佳實務)
  - [12.1 Organization 管理](#121-organization-管理)
  - [12.2 Repository Governance](#122-repository-governance)
  - [12.3 Inner Source 策略](#123-inner-source-策略)
  - [12.4 合規與稽核](#124-合規與稽核)
  - [12.5 Token 與權限管理](#125-token-與權限管理)
  - [12.6 GitHub Projects 管理](#126-github-projects-管理)
  - [12.7 多帳戶與跨平台管理](#127-多帳戶與跨平台管理)
- [第 13 章：維運與監控](#第-13-章維運與監控)
  - [13.1 API Rate Limit 監控](#131-api-rate-limit-監控)
  - [13.2 Workflow 執行監控](#132-workflow-執行監控)
  - [13.3 Repo 活躍度監控](#133-repo-活躍度監控)
  - [13.4 Security Alert 監控](#134-security-alert-監控)
  - [13.5 Billing 與用量](#135-billing-與用量)
  - [13.6 通知管理](#136-通知管理)
- [第 14 章：實戰案例](#第-14-章實戰案例)
  - [14.1 案例一：微服務團隊快速啟動](#141-案例一微服務團隊快速啟動)
  - [14.2 案例二：Release 流程自動化](#142-案例二release-流程自動化)
  - [14.3 案例三：Security 合規自動化](#143-案例三security-合規自動化)
  - [14.4 案例四：PR Review 流程優化](#144-案例四pr-review-流程優化)
  - [14.5 案例五：跨 Repo 標準化](#145-案例五跨-repo-標準化)
- [第 15 章：故障排除（Troubleshooting）](#第-15-章故障排除troubleshooting)
  - [15.1 常見錯誤與解決方案](#151-常見錯誤與解決方案)
  - [15.2 CLI 升級與相容性](#152-cli-升級與相容性)
  - [15.3 Debug 模式](#153-debug-模式)
- [第 16 章：最佳實務總覽](#第-16-章最佳實務總覽)
  - [16.1 日常開發](#161-日常開發)
  - [16.2 團隊協作](#162-團隊協作)
  - [16.3 安全](#163-安全)
  - [16.4 CI/CD](#164-cicd)
  - [16.5 自動化](#165-自動化)
- [第 17 章：附錄](#第-17-章附錄)
  - [17.1 Cheat Sheet](#171-cheat-sheet)
  - [17.2 環境變數](#172-環境變數)
  - [17.3 設定檔位置](#173-設定檔位置)
  - [17.4 常用 jq 語法](#174-常用-jq-語法)
  - [17.5 FAQ](#175-faq)
- [檢查清單（Checklist）](#檢查清單checklist)

---

# 第 1 章：GitHub CLI 概述

## 1.1 GitHub CLI 是什麼

GitHub CLI（指令為 `gh`）是 GitHub 官方開發的開源命令列工具，以 Go 語言撰寫，讓開發者直接在終端機中與 GitHub 平台互動。它將 Pull Request、Issue、GitHub Actions、Release 等 GitHub 核心功能帶入命令列，消除在瀏覽器與終端機之間頻繁切換的低效工作模式。

**核心能力**：

| 功能領域 | 指令群 | 說明 |
|---------|----------|------|
| Repository 管理 | `gh repo` | 建立、Clone、Fork、刪除、Archive、同步 Repo |
| PR 管理 | `gh pr` | 建立、Review、Merge、Diff、Checkout PR |
| Issue 管理 | `gh issue` | 建立、編輯、關閉、標籤、轉移 Issue |
| GitHub Actions | `gh workflow` / `gh run` / `gh cache` | 觸發、監控 Workflow；管理 Cache |
| Release 管理 | `gh release` | 建立、發佈、上傳 Asset、自動產生 Release Notes |
| Codespaces | `gh codespace` | 建立、連線、管理雲端開發環境 |
| Project 管理 | `gh project` | 建立、編輯 Projects V2、管理欄位與項目 |
| 搜尋 | `gh search` | 跨 GitHub 搜尋 Code、Issues、PRs、Repos |
| 供應鏈安全 | `gh attestation` | 下載與驗證 Artifact Attestation |
| Ruleset 管理 | `gh ruleset` | 檢視 Repository / Organization Ruleset |
| GitHub API | `gh api` | 直接呼叫任何 GitHub REST / GraphQL API |
| AI 整合 | `gh copilot` | Copilot CLI 自然語言指令建議與解釋 |
| 環境瀏覽 | `gh browse` / `gh status` | 在瀏覽器開啟 Repo、檢視個人狀態 |
| Gist 管理 | `gh gist` | 建立、編輯、列出、檢視 Gist |
| 擴充系統 | `gh extension` / `gh alias` | 安裝社群 Extension、自訂指令縮寫 |

## 1.2 為何企業要導入 GitHub CLI

```mermaid
graph LR
    A[手動操作 GitHub Web UI] --> B[人為失誤率高]
    A --> C[無法自動化]
    A --> D[操作無法追蹤]
    E[導入 GitHub CLI] --> F[腳本化可重複]
    E --> G[CI/CD 整合]
    E --> H[操作可稽核]
    E --> I[跨團隊標準化]
```

**企業導入的關鍵理由**：

1. **自動化優先**：所有 GitHub 操作可腳本化，納入 CI/CD Pipeline
2. **標準化流程**：統一 Repo 建立、Branch Protection、Release 流程
3. **可稽核性**：所有操作留下 CLI 紀錄，滿足金融合規要求
4. **效率提升**：批次建立 Repo、批次設定 Branch Protection，節省 80% 人力
5. **DevOps 整合**：與 GitHub Actions、Terraform、Ansible 無縫銜接
6. **安全性**：Token 管理集中化，避免在瀏覽器中暴露憑證

## 1.3 GitHub CLI 架構

```mermaid
graph TB
    subgraph "開發者終端機"
        CLI[gh CLI]
        Config[~/.config/gh/config.yml]
        Hosts[~/.config/gh/hosts.yml]
    end
    
    subgraph "GitHub 平台"
        REST[REST API v3]
        GraphQL[GraphQL API v4]
        OAuth[OAuth / PAT]
    end
    
    subgraph "擴充生態系"
        Extensions[gh extensions]
        Aliases[gh aliases]
    end
    
    CLI --> Config
    CLI --> Hosts
    CLI -->|HTTPS/SSH| REST
    CLI -->|HTTPS| GraphQL
    CLI -->|認證| OAuth
    CLI --> Extensions
    CLI --> Aliases
```

**架構要素說明**：

- **Config 檔案**：`~/.config/gh/config.yml` 儲存全域設定（預設編輯器、協議偏好、Alias 定義）
- **Hosts 檔案**：`~/.config/gh/hosts.yml` 儲存各 GitHub 平台的認證資訊（支援多帳戶）
- **REST API**：大多數 `gh` 指令底層呼叫 GitHub REST API v3
- **GraphQL API**：複雜查詢（如 Project Board）使用 GraphQL API v4
- **Extension**：社群開發的外掛，可透過 `gh extension install` 安裝
- **Alias**：自訂指令縮寫，存放於 config.yml

## 1.4 GitHub CLI 與 Git 的差異

| 比較項目 | Git (`git`) | GitHub CLI (`gh`) |
|---------|-------------|-------------------|
| 本質 | 分散式版本控制系統 | GitHub 平台互動工具 |
| 範圍 | 任何 Git 伺服器 | 僅 GitHub（含 Enterprise） |
| 主要功能 | Commit / Branch / Merge / Rebase | PR / Issue / Actions / Release |
| 認證方式 | SSH Key / Credential Manager | OAuth / PAT / SSH |
| 離線操作 | 支援（本地操作） | 不支援（需連線 GitHub） |
| API 存取 | 不支援 | 內建 `gh api` |
| 自動化程度 | 低（需搭配 curl/httpie） | 高（原生支援 JSON 輸出） |
| 安裝方式 | OS 內建或獨立安裝 | 獨立安裝 |

**關鍵區別**：`git` 負責版本控制操作（commit、branch、merge），`gh` 負責 GitHub 平台操作（PR、Issue、Actions）。兩者互補而非替代。

**企業實務建議**：

```bash
# 日常開發：用 git 做版本控制
git add . && git commit -m "feat: add user API" && git push

# GitHub 互動：用 gh 做平台操作
gh pr create --title "feat: add user API" --body "新增使用者 API"
gh pr merge 42 --squash --delete-branch
```

## 1.5 GitHub CLI 與 GitHub API 的關係

GitHub CLI 本質上是 GitHub API 的**命令列封裝層**，提供更友善的操作介面：

```
開發者 → gh CLI → GitHub REST/GraphQL API → GitHub 平台
```

**直接使用 API 的場景**：

```bash
# gh api 可直接呼叫任何 GitHub API
# 取得 Repo 資訊
gh api repos/{owner}/{repo}

# 使用 GraphQL 查詢
gh api graphql -f query='
  query {
    repository(owner: "myorg", name: "myrepo") {
      pullRequests(first: 10, states: OPEN) {
        nodes { title number }
      }
    }
  }
'

# 使用 jq 過濾 JSON 輸出
gh api repos/{owner}/{repo}/pulls --jq '.[].title'
```

**設計哲學**：`gh` 指令是 80% 常用操作的簡化；`gh api` 覆蓋 100% API 能力。

## 1.6 GitHub CLI 使用情境

| 情境 | 說明 | 範例指令 |
|------|------|---------|
| 開發日常 | 建立 PR、Review、Merge | `gh pr create`, `gh pr review` |
| DevOps | 觸發 Workflow、監控 Runner | `gh workflow run`, `gh run list` |
| Release | 建立 Release、上傳 Asset | `gh release create v1.0.0` |
| 專案管理 | 管理 Issue、Label、Milestone | `gh issue create`, `gh label list` |
| 自動化腳本 | 批次操作 Repo/Branch/Team | Bash/PowerShell Script |
| CI/CD Pipeline | 在 GitHub Actions 中使用 | `gh pr comment`, `gh release` |
| 安全治理 | 設定 Branch Protection、CODEOWNERS | `gh api` + REST API |
| 跨平台管理 | 同時管理 github.com 和 GHES | `gh auth login --hostname` |

## 1.7 GitHub CLI 優缺點

### 優點

- **官方維護**：GitHub 官方開發，與平台功能同步更新
- **跨平台**：Windows / macOS / Linux 全支援
- **JSON 輸出**：`--json` 旗標方便腳本化處理
- **Extension 生態**：社群貢獻大量擴充功能
- **多帳戶支援**：可同時登入 github.com 和 GitHub Enterprise Server
- **OAuth 整合**：免手動管理 Token（Browser Flow）
- **Telemetry 可控**：可透過 `gh config set telemetry disabled` 或環境變數 `GH_TELEMETRY=false` 關閉遙測，亦可以 `gh config set telemetry log` 檢視遙測內容再決定是否啟用

### 缺點

- **僅限 GitHub**：不支援 GitLab、Bitbucket 等其他平台
- **網路依賴**：所有操作需連線 GitHub
- **學習曲線**：指令數量多，需要時間熟悉
- **部分功能延遲**：GitHub 新功能可能延後數週才在 CLI 中支援
- **Rate Limit**：受 GitHub API Rate Limit 限制（5,000 次/小時）

> **實務建議**：在企業環境中，建議搭配 `gh alias` 建立團隊統一的指令縮寫，降低學習門檻。同時透過 `gh api --cache` 減少 API 呼叫次數，避免觸及 Rate Limit。如需確認當前可用的所有指令，可執行 `gh help` 或查閱 [GitHub CLI 線上手冊](https://cli.github.com/manual/gh)。

---

# 第 2 章：GitHub CLI 安裝與環境建置

## 2.1 Windows 安裝

### 方法一：Winget（推薦）

```powershell
# PowerShell（以系統管理員執行）
winget install --id GitHub.cli
```

### 方法二：Scoop

```powershell
scoop install gh
```

### 方法三：Chocolatey

```powershell
choco install gh
```

### 方法四：MSI 安裝檔

從 [GitHub CLI Releases](https://github.com/cli/cli/releases) 下載 `gh_*_windows_amd64.msi`，雙擊安裝。

```cmd
REM CMD 驗證安裝
gh --version
```

## 2.2 macOS 安裝

```bash
# Homebrew（推薦）
brew install gh

# MacPorts
sudo port install gh

# Conda
conda install gh --channel conda-forge
```

## 2.3 Linux 安裝

### Ubuntu / Debian

```bash
# 新增 GitHub CLI 套件庫
(type -p wget >/dev/null || sudo apt install wget -y) \
  && sudo mkdir -p -m 755 /etc/apt/keyrings \
  && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  && cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
  && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
  && sudo apt update \
  && sudo apt install gh -y
```

### RHEL / CentOS / Fedora

```bash
sudo dnf install 'dnf-command(config-manager)'
sudo dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo dnf install gh -y
```

## 2.4 WSL 安裝

```bash
# WSL2 Ubuntu 環境中，按照 Linux Ubuntu 步驟安裝
# 安裝後需重新認證（WSL 環境與 Windows 環境獨立）
gh auth login
```

> **注意**：WSL 中的 `gh` 與 Windows 中的 `gh` 是獨立的，Token 不共享。建議在 WSL 中使用 SSH 認證，在 Windows 中使用 HTTPS 認證。

## 2.5 驗證安裝

```bash
# Bash / PowerShell / CMD 通用
gh --version
# 預期輸出：gh version 2.74.0 (2026-05-01)

# 檢查認證狀態
gh auth status

# 檢查設定
gh config list
```

## 2.6 Proxy 設定

企業內網通常需要設定 Proxy：

```bash
# Bash - 設定 HTTP Proxy
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,.company.com

# 永久寫入 ~/.bashrc 或 ~/.zshrc
echo 'export HTTP_PROXY=http://proxy.company.com:8080' >> ~/.bashrc
echo 'export HTTPS_PROXY=http://proxy.company.com:8080' >> ~/.bashrc
```

```powershell
# PowerShell - 設定 Proxy
$env:HTTP_PROXY = "http://proxy.company.com:8080"
$env:HTTPS_PROXY = "http://proxy.company.com:8080"
$env:NO_PROXY = "localhost,127.0.0.1,.company.com"

# 永久設定（使用者級別）
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://proxy.company.com:8080", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://proxy.company.com:8080", "User")
```

```cmd
REM CMD - 設定 Proxy
set HTTP_PROXY=http://proxy.company.com:8080
set HTTPS_PROXY=http://proxy.company.com:8080

REM 永久設定
setx HTTP_PROXY http://proxy.company.com:8080
setx HTTPS_PROXY http://proxy.company.com:8080
```

## 2.7 公司內網設定

### GitHub Enterprise Server（GHES）設定

```bash
# 登入公司內部 GHES
gh auth login --hostname github.company.com

# 設定預設 Host
gh config set -h github.company.com git_protocol ssh

# 驗證
gh auth status --hostname github.company.com
```

### 自簽憑證處理

```bash
# 方法一：跳過 SSL 驗證（不建議用於正式環境）
gh config set -h github.company.com http_unix_socket ""

# 方法二：匯入公司 CA 憑證（推薦）
# Linux
sudo cp company-ca.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates

# macOS
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain company-ca.crt

# Windows PowerShell
Import-Certificate -FilePath "company-ca.crt" -CertStoreLocation Cert:\LocalMachine\Root
```

## 2.8 SSH Key 建立

```bash
# 產生 Ed25519 SSH Key（推薦演算法）
ssh-keygen -t ed25519 -C "your.email@company.com" -f ~/.ssh/gh_company

# 啟動 SSH Agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/gh_company

# 將公鑰上傳至 GitHub
gh ssh-key add ~/.ssh/gh_company.pub --title "Company-Laptop-2026"

# 驗證
ssh -T git@github.com
```

```powershell
# PowerShell 版本
ssh-keygen -t ed25519 -C "your.email@company.com" -f "$env:USERPROFILE\.ssh\gh_company"

# 啟動 SSH Agent（需先啟用服務）
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add "$env:USERPROFILE\.ssh\gh_company"

# 上傳公鑰
gh ssh-key add "$env:USERPROFILE\.ssh\gh_company.pub" --title "Company-Laptop-2026"
```

### SSH Config 設定

```bash
# ~/.ssh/config
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/gh_company
    IdentitiesOnly yes

Host github.company.com
    HostName github.company.com
    User git
    IdentityFile ~/.ssh/gh_enterprise
    IdentitiesOnly yes
```

## 2.9 GPG Key 建立

```bash
# 產生 GPG Key
gpg --full-generate-key
# 選擇 RSA and RSA / 4096 bits / 不過期或自訂到期日

# 列出 GPG Key
gpg --list-secret-keys --keyid-format=long

# 匯出公鑰
gpg --armor --export YOUR_KEY_ID

# 上傳至 GitHub
gh gpg-key add <(gpg --armor --export YOUR_KEY_ID)

# 設定 Git 使用 GPG 簽署
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

## 2.10 Git 設定

```bash
# 基本設定
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"

# 使用 gh 作為 Git 認證助手
gh auth setup-git

# 預設分支名稱
git config --global init.defaultBranch main

# 換行符號（Windows 團隊建議）
git config --global core.autocrlf true    # Windows
git config --global core.autocrlf input   # macOS/Linux

# 預設編輯器
git config --global core.editor "code --wait"

# Pull 策略
git config --global pull.rebase true

# 驗證設定
git config --global --list
```

## 2.11 GitHub Login

```bash
# 互動式登入（推薦首次使用）
gh auth login
# 選項：
#   ? What account do you want to log into? GitHub.com
#   ? What is your preferred protocol for Git operations? SSH
#   ? Upload your SSH public key? Yes
#   ? How would you like to authenticate? Login with a web browser

# 使用 Token 登入（適合 CI/CD）
echo $GITHUB_TOKEN | gh auth login --with-token

# 登入 Enterprise Server
gh auth login --hostname github.company.com --git-protocol ssh
```

```powershell
# PowerShell - Token 登入
$env:GITHUB_TOKEN | gh auth login --with-token

# 或使用環境變數
gh auth login --with-token < token.txt
```

## 2.12 Token 管理

```bash
# 檢視目前 Token 狀態
gh auth token
gh auth status

# 重新整理 Token（延展權限）
gh auth refresh --scopes repo,admin:org,workflow

# 設定 Token 至環境變數（用於腳本）
export GH_TOKEN=$(gh auth token)
```

**Token 安全存放策略**：

| 環境 | 存放方式 | 說明 |
|------|---------|------|
| 本機開發 | `gh auth login` | 存放在 OS keyring |
| CI/CD | GitHub Actions Secret | 自動注入 `GITHUB_TOKEN` |
| 自動化腳本 | 環境變數 `GH_TOKEN` | 不可寫入程式碼 |
| 共享伺服器 | Vault / AWS Secrets Manager | 集中管理 |

## 2.13 PAT 管理

### Classic PAT vs Fine-grained PAT

| 比較項目 | Classic PAT | Fine-grained PAT |
|---------|-------------|-------------------|
| 權限粒度 | 粗（repo, admin:org） | 細（個別 Repo、個別 API） |
| Repo 範圍 | 全部 Repo | 可指定特定 Repo |
| 到期日 | 可設定不過期 | 必須設定到期日 |
| 審核 | 無 | Organization 可要求審核 |
| 建議使用 | 舊系統整合 | 新專案（推薦） |

### 建立 Fine-grained PAT

```bash
# 透過 Web UI 建立：Settings > Developer settings > Fine-grained tokens
# 或透過 API
gh api user -H "Authorization: token YOUR_PAT" --jq '.login'
```

> **實務建議**：
> - 所有新專案一律使用 Fine-grained PAT
> - Token 到期日不超過 90 天
> - 權限遵循最小權限原則
> - 定期稽核 Token 使用狀況：`gh api user/installations --jq '.[].permissions'`

---

# 第 3 章：GitHub Authentication 與安全管理

## 3.1 gh auth login

```bash
# 互動式登入 github.com
gh auth login

# 指定登入目標與協議
gh auth login --hostname github.com --git-protocol ssh --web

# 使用 Token 非互動式登入（適合 CI/CD）
echo "ghp_xxxxxxxxxxxx" | gh auth login --with-token

# 登入 GHES
gh auth login --hostname github.company.com

# 指定 Scope
gh auth login --scopes "repo,read:org,workflow"
```

## 3.2 gh auth status

```bash
# 檢視所有已登入帳戶
gh auth status

# 輸出範例：
# github.com
#   ✓ Logged in to github.com account username (keyring)
#   - Active account: true
#   - Git operations protocol: ssh
#   - Token: ghp_****
#   - Token scopes: 'admin:org', 'gist', 'repo', 'workflow'

# 檢視特定 Host
gh auth status --hostname github.company.com

# 顯示 Token（用於除錯）
gh auth token --hostname github.com
```

## 3.3 gh auth refresh

```bash
# 重新整理 Token 權限
gh auth refresh

# 新增額外 Scope
gh auth refresh --scopes admin:org,delete_repo

# 針對特定 Host
gh auth refresh --hostname github.company.com --scopes repo,workflow
```

## 3.4 gh auth logout

```bash
# 登出目前帳戶
gh auth logout

# 指定 Host 登出
gh auth logout --hostname github.company.com

# 登出所有帳戶
gh auth logout --hostname github.com
gh auth logout --hostname github.company.com
```

## 3.5 SSH Authentication

```bash
# 設定 gh 使用 SSH 協議
gh config set git_protocol ssh --host github.com

# 上傳 SSH 公鑰
gh ssh-key add ~/.ssh/id_ed25519.pub --title "work-laptop"

# 列出已上傳的 SSH Key
gh ssh-key list

# 刪除 SSH Key
gh ssh-key delete <key-id>
```

**SSH 認證流程**：

```mermaid
sequenceDiagram
    participant Dev as 開發者終端機
    participant SSH as SSH Agent
    participant GH as GitHub
    
    Dev->>SSH: ssh-add (載入私鑰)
    Dev->>GH: git push / gh repo clone
    GH->>Dev: SSH Challenge
    Dev->>SSH: 簽署 Challenge
    SSH->>GH: 回傳簽章
    GH->>GH: 驗證公鑰匹配
    GH->>Dev: 認證成功
```

## 3.6 HTTPS Authentication

```bash
# 設定 gh 使用 HTTPS 協議
gh config set git_protocol https --host github.com

# 設定 gh 為 Git Credential Helper
gh auth setup-git

# 驗證 Git 認證設定
git config --global credential.helper
# 預期：/usr/bin/gh auth git-credential
```

## 3.7 PAT Token

```bash
# 使用 Classic PAT 登入
export GH_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
gh auth status
# 或
echo "ghp_xxxx" | gh auth login --with-token

# 在 GitHub Actions 中使用
# ${{ secrets.GITHUB_TOKEN }} 自動提供，無需手動設定
```

## 3.8 Fine-grained Token

```bash
# Fine-grained PAT 以 github_pat_ 開頭
export GH_TOKEN=github_pat_xxxxxxxxxxxxxxxxxxxx

# 建立建議：
# 1. Settings > Developer settings > Personal access tokens > Fine-grained tokens
# 2. Token name: ci-deploy-myapp-2026
# 3. Expiration: 90 days
# 4. Repository access: Only select repositories > myorg/myapp
# 5. Permissions:
#    - Contents: Read and write
#    - Pull requests: Read and write
#    - Workflows: Read and write
```

## 3.9 SSO

```bash
# 若 Organization 啟用 SAML SSO，Token 需額外授權
# 步驟：
# 1. 登入 GitHub Web UI
# 2. Settings > Personal access tokens
# 3. 點選 Token 旁的 "Configure SSO"
# 4. 選擇對應 Organization，點選 "Authorize"

# 或使用 gh auth refresh 重新取得 SSO 授權
gh auth refresh --scopes admin:org
```

## 3.10 Enterprise Authentication

```bash
# GitHub Enterprise Server 登入
gh auth login --hostname github.company.com

# 多平台切換
gh auth switch --hostname github.com
gh auth switch --hostname github.company.com

# 列出所有已認證的平台
gh auth status
```

**多帳戶管理策略**：

```bash
# ~/.config/gh/hosts.yml 範例
github.com:
    user: personal-user
    git_protocol: ssh
    oauth_token: ghp_personal_xxxx

github.company.com:
    user: enterprise-user
    git_protocol: ssh
    oauth_token: ghp_enterprise_xxxx
```

## 3.11 最佳安全實務

| 項目 | 建議做法 | 風險 |
|------|---------|------|
| Token 類型 | Fine-grained PAT | Classic PAT 權限過大 |
| Token 到期 | ≤ 90 天 | 永不過期的 Token 是安全漏洞 |
| Token 範圍 | 僅授權必要的 Repo | 全域 Repo 權限造成橫向攻擊面 |
| SSH Key | Ed25519 演算法 | RSA-2048 安全性逐漸不足 |
| GPG 簽署 | 強制所有 Commit 簽署 | 未簽署的 Commit 無法驗證來源 |
| 環境變數 | 不可 Hard-code Token | 寫在程式碼中的 Token 會被 Git 歷史記錄 |
| CI/CD | 使用 `GITHUB_TOKEN` | 避免使用 PAT（權限過大） |

## 3.12 Token Rotation

```bash
#!/bin/bash
# token-rotation.sh - Token 輪換提醒腳本

# 檢查 Token 到期日
TOKEN_EXPIRY=$(gh api user --jq '.created_at')
echo "Token 建立日期：$TOKEN_EXPIRY"

# 列出所有 PAT（需 admin 權限）
gh api user/installations --jq '.[].id'

# 建議流程：
# 1. 每季（90天）輪換一次 Token
# 2. 新 Token 先測試再替換
# 3. 替換後立即撤銷舊 Token
# 4. 更新所有使用該 Token 的 CI/CD Secret
```

```powershell
# PowerShell 版本
# 檢查 Token 到期日
$tokenInfo = gh auth status 2>&1
Write-Host "目前認證狀態：$tokenInfo"

# 定期提醒腳本（可加入 Windows Task Scheduler）
$daysSinceRotation = (New-TimeSpan -Start (Get-Date "2026-03-01") -End (Get-Date)).Days
if ($daysSinceRotation -gt 80) {
    Write-Warning "Token 即將到期，請執行 gh auth refresh"
}
```

## 3.13 Secret 管理

```bash
# 設定 Repo 層級 Secret
gh secret set API_KEY --body "your-api-key-value"
gh secret set DB_PASSWORD < db_password.txt

# 設定 Organization 層級 Secret
gh secret set ORG_SECRET --org myorg --body "org-value"

# 設定 Environment 層級 Secret
gh secret set DEPLOY_KEY --env production --body "deploy-key-value"

# 列出 Secret（僅顯示名稱，不顯示值）
gh secret list
gh secret list --org myorg
gh secret list --env production

# 刪除 Secret
gh secret delete API_KEY

# 設定 Dependabot Secret
gh secret set REGISTRY_TOKEN --app dependabot --body "token-value"
```

## 3.14 Least Privilege 原則

**權限矩陣設計**：

| 角色 | Repo 權限 | Token Scope | 說明 |
|------|----------|-------------|------|
| 開發者 | Write | `repo`, `workflow` | 日常開發 |
| Tech Lead | Admin | `repo`, `admin:org` | 管理 Branch Protection |
| DevOps | Admin | `repo`, `workflow`, `admin:org` | CI/CD 管理 |
| 稽核人員 | Read | `repo:status`, `read:org` | 唯讀檢視 |
| CI/CD Bot | Write | `contents:write`, `pull-requests:write` | 自動化 |

> **實務建議**：使用 Fine-grained PAT 時，每個自動化任務建立獨立的 Token，僅授權該任務需要的最小權限。定期使用 `gh api orgs/{org}/audit-log` 稽核 Token 使用紀錄。

---

# 第 4 章：GitHub Repo 管理

## 4.1 建立 Repo

```bash
# 建立公開 Repo
gh repo create myorg/my-service --public --description "My microservice"

# 建立私有 Repo（企業常用）
gh repo create myorg/my-service \
  --private \
  --description "User Management Service" \
  --license MIT \
  --gitignore Java \
  --clone

# 從現有目錄建立 Repo
cd my-project
gh repo create myorg/my-project --private --source=. --push

# 使用 Template Repo 建立
gh repo create myorg/new-service \
  --template myorg/spring-boot-template \
  --private \
  --clone

# 建立並初始化（含 README）
gh repo create myorg/docs-repo \
  --private \
  --description "Team documentation" \
  --add-readme \
  --clone
```

```powershell
# PowerShell 版本
gh repo create myorg/my-service `
  --private `
  --description "User Management Service" `
  --license MIT `
  --gitignore Java `
  --clone
```

## 4.2 Clone Repo

```bash
# 基本 Clone
gh repo clone myorg/my-service

# Clone 到指定目錄
gh repo clone myorg/my-service ./projects/my-service

# Clone 後自動切換目錄
gh repo clone myorg/my-service && cd my-service

# 淺層 Clone（大型 Repo 加速）
gh repo clone myorg/my-service -- --depth 1

# 批次 Clone（整個 Organization 的所有 Repo）
gh repo list myorg --limit 100 --json name --jq '.[].name' | \
  xargs -I {} gh repo clone myorg/{}
```

## 4.3 Fork Repo

```bash
# Fork 到個人帳戶
gh repo fork upstream-org/project

# Fork 到 Organization
gh repo fork upstream-org/project --org myorg

# Fork 並 Clone
gh repo fork upstream-org/project --clone

# Fork 且僅保留預設分支
gh repo fork upstream-org/project --default-branch-only
```

## 4.4 Rename Repo

```bash
# 重新命名 Repo
gh repo rename new-name --repo myorg/old-name

# 或進入 Repo 目錄後
cd my-repo
gh repo rename new-name
```

## 4.5 Delete Repo

```bash
# 刪除 Repo（需確認）
gh repo delete myorg/deprecated-service --yes

# 建議：先 Archive 再觀察一段時間，確認無人使用後才刪除
```

> ⚠️ **警告**：刪除 Repo 不可逆！請先執行 `gh repo archive` 進行封存，觀察 30 天後再決定是否刪除。

## 4.6 Archive Repo

```bash
# 封存 Repo（唯讀模式）
gh repo archive myorg/legacy-service

# 取消封存
gh repo unarchive myorg/legacy-service

# 批次封存舊 Repo
gh repo list myorg --json name,pushedAt --jq '.[] | select(.pushedAt < "2024-01-01") | .name' | \
  xargs -I {} gh repo archive myorg/{} --yes
```

## 4.7 Template Repo

```bash
# 將現有 Repo 設為 Template
gh api repos/myorg/spring-boot-template \
  -X PATCH \
  -f is_template=true

# 從 Template 建立新 Repo
gh repo create myorg/new-service \
  --template myorg/spring-boot-template \
  --private \
  --clone

# 列出 Organization 的 Template Repo
gh repo list myorg --json name,isTemplate --jq '.[] | select(.isTemplate) | .name'
```

**企業 Template Repo 建議架構**：

```
spring-boot-template/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── cd.yml
│   │   └── security.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
├── src/
│   ├── main/java/com/company/template/
│   └── test/java/com/company/template/
├── docs/
│   └── adr/
├── .gitignore
├── .editorconfig
├── pom.xml
├── README.md
├── SECURITY.md
├── CONTRIBUTING.md
└── LICENSE
```

## 4.8 Monorepo

```bash
# 建立 Monorepo
gh repo create myorg/platform \
  --private \
  --description "Monorepo: frontend + backend + shared" \
  --clone

# Monorepo 建議結構
# platform/
# ├── apps/
# │   ├── web-app/          (Vue 3)
# │   ├── admin-app/        (Vue 3)
# │   └── api-server/       (Spring Boot)
# ├── packages/
# │   ├── shared-types/
# │   ├── ui-components/
# │   └── utils/
# ├── infrastructure/
# │   ├── terraform/
# │   └── kubernetes/
# └── .github/
#     └── workflows/
```

## 4.9 Polyrepo

```bash
# 批次建立 Polyrepo（微服務架構）
services=("user-service" "order-service" "payment-service" "notification-service")

for svc in "${services[@]}"; do
  gh repo create "myorg/$svc" \
    --private \
    --template myorg/spring-boot-template \
    --description "Microservice: $svc" \
    --clone
  echo "Created: myorg/$svc"
done
```

## 4.10 Repo 命名規範

| 類型 | 命名格式 | 範例 |
|------|---------|------|
| 微服務 | `{domain}-service` | `user-service`, `order-service` |
| 前端 | `{product}-web` | `banking-web`, `admin-web` |
| 共用程式庫 | `{scope}-lib` | `common-lib`, `security-lib` |
| 文件 | `{team}-docs` | `platform-docs`, `api-docs` |
| 基礎設施 | `{scope}-infra` | `platform-infra`, `network-infra` |
| Template | `{stack}-template` | `spring-boot-template`, `vue-template` |
| 工具 | `{purpose}-tool` | `deploy-tool`, `migration-tool` |

**命名規則**：
- 全小寫
- 使用 `-`（hyphen）分隔，不使用 `_` 或 camelCase
- 不超過 50 字元
- 含義明確，不使用縮寫

## 4.11 Repo Governance

```mermaid
graph TB
    subgraph "Repo Governance 架構"
        A[Repo 建立申請] --> B{審核}
        B -->|通過| C[自動化建立]
        C --> D[套用 Template]
        D --> E[設定 Branch Protection]
        E --> F[設定 CODEOWNERS]
        F --> G[設定 Workflow]
        G --> H[通知團隊]
        B -->|拒絕| I[退回修改]
    end
```

**Governance 政策要點**：

1. **建立前審核**：新 Repo 必須經 Tech Lead 核准
2. **Template 強制**：所有 Repo 必須從核准的 Template 建立
3. **Branch Protection**：`main` 分支必須啟用保護規則
4. **CODEOWNERS**：每個 Repo 必須有 CODEOWNERS 檔案
5. **定期盤點**：每季盤點 Repo 使用狀況，閒置 Repo 進行 Archive
6. **命名審核**：Repo 名稱必須符合公司命名規範

## 4.12 Repo 權限管理

```bash
# 設定 Repo 可見性
gh repo edit myorg/my-service --visibility private

# 透過 API 設定 Collaborator
gh api repos/myorg/my-service/collaborators/username \
  -X PUT \
  -f permission=push

# 移除 Collaborator
gh api repos/myorg/my-service/collaborators/username -X DELETE

# 列出 Repo Collaborator
gh api repos/myorg/my-service/collaborators --jq '.[].login'
```

## 4.13 Team 管理

```bash
# 建立 Team
gh api orgs/myorg/teams \
  -X POST \
  -f name="backend-team" \
  -f description="Backend Development Team" \
  -f privacy="closed"

# 將 Repo 加入 Team
gh api orgs/myorg/teams/backend-team/repos/myorg/user-service \
  -X PUT \
  -f permission="push"

# 新增 Team 成員
gh api orgs/myorg/teams/backend-team/memberships/username \
  -X PUT \
  -f role="member"

# 列出 Team 成員
gh api orgs/myorg/teams/backend-team/members --jq '.[].login'

# 列出 Team 的 Repo
gh api orgs/myorg/teams/backend-team/repos --jq '.[].full_name'
```

> **實務建議**：
> - 團隊依職能分層：`platform-admins`（Admin）、`backend-team`（Write）、`frontend-team`（Write）、`qa-team`（Triage）
> - 使用 Team 階層（Nested Team）管理大型組織
> - 定期稽核 Team 成員：離職人員須於 24 小時內移除權限

---

# 第 5 章：Source Code 上架與管理

## 5.1 Git 初始化

```bash
# 方法一：先建立 Repo 再 Clone（推薦）
gh repo create myorg/my-service --private --clone --add-readme
cd my-service

# 方法二：從現有目錄推上 GitHub
cd my-existing-project
git init
git add .
git commit -m "chore: initial commit"
gh repo create myorg/my-service --private --source=. --push
```

## 5.2 Push Source Code

```bash
# 日常推送流程
git add .
git commit -m "feat(user): add login endpoint"
git push origin feature/user-login

# 建立 PR
gh pr create \
  --title "feat(user): add login endpoint" \
  --body "## 變更說明
- 新增 /api/v1/users/login 端點
- 整合 JWT 認證
- 新增單元測試

## 測試結果
- [x] Unit Test 通過
- [x] Integration Test 通過" \
  --base main \
  --reviewer "tech-lead,senior-dev" \
  --label "feature,backend"
```

## 5.3 Branch 管理

```bash
# 列出遠端分支
git branch -r

# 建立並切換分支
git checkout -b feature/payment-api

# 推送分支至遠端
git push -u origin feature/payment-api

# 刪除已合併的本地分支
git branch -d feature/payment-api

# 刪除遠端分支
git push origin --delete feature/payment-api

# 批次清理已合併的分支
git branch --merged main | grep -v "main\|develop" | xargs git branch -d
```

## 5.4 Git Flow

```mermaid
gitGraph
    commit id: "init"
    branch develop
    checkout develop
    commit id: "setup"
    branch feature/login
    checkout feature/login
    commit id: "feat: login UI"
    commit id: "feat: login API"
    checkout develop
    merge feature/login id: "merge login"
    branch release/1.0
    checkout release/1.0
    commit id: "bump version"
    commit id: "fix: typo"
    checkout main
    merge release/1.0 id: "release 1.0" tag: "v1.0.0"
    checkout develop
    merge release/1.0 id: "back merge"
    checkout main
    branch hotfix/1.0.1
    commit id: "fix: security"
    checkout main
    merge hotfix/1.0.1 id: "hotfix" tag: "v1.0.1"
    checkout develop
    merge hotfix/1.0.1 id: "hotfix to dev"
```

**Git Flow 分支策略**：

| 分支 | 用途 | 來源 | 合併目標 | 命名規範 |
|------|------|------|---------|---------|
| `main` | 正式環境 | - | - | `main` |
| `develop` | 開發整合 | `main` | `release/*` | `develop` |
| `feature/*` | 功能開發 | `develop` | `develop` | `feature/JIRA-123-description` |
| `release/*` | 版本發佈 | `develop` | `main` + `develop` | `release/1.2.0` |
| `hotfix/*` | 緊急修復 | `main` | `main` + `develop` | `hotfix/fix-auth-bypass` |

## 5.5 Trunk Based Development

```bash
# Trunk Based Development 流程
# 1. 從 main 建立短生命週期分支
git checkout -b feat/JIRA-456-add-cache main

# 2. 開發（保持小範圍變更）
git add . && git commit -m "feat: add Redis cache layer"

# 3. 推送並建立 PR
git push -u origin feat/JIRA-456-add-cache
gh pr create --title "feat: add Redis cache layer" --base main

# 4. Code Review 通過後 Squash Merge
gh pr merge --squash --delete-branch

# 5. 透過 Feature Flag 控制上線
# application.yml
# feature:
#   redis-cache: ${FEATURE_REDIS_CACHE:false}
```

**適用場景比較**：

| 策略 | 適合 | 不適合 |
|------|------|--------|
| Git Flow | 版本式發佈、多版本維護 | 持續部署、快速迭代 |
| Trunk Based | 持續部署、DevOps 成熟團隊 | 多版本平行維護 |

## 5.6 Feature Branch

```bash
# 建立 Feature Branch
git checkout -b feature/JIRA-789-user-profile develop

# 日常開發
git add . && git commit -m "feat(profile): add avatar upload"
git push origin feature/JIRA-789-user-profile

# 建立 PR 到 develop
gh pr create \
  --base develop \
  --title "feat(profile): user profile management" \
  --assignee @me
```

## 5.7 Release Branch

```bash
# 從 develop 建立 Release Branch
git checkout -b release/2.1.0 develop

# 版本號更新
# 更新 pom.xml / package.json 中的版本號
git commit -am "chore: bump version to 2.1.0"

# 修復 Release 階段發現的 Bug
git commit -am "fix: resolve login timeout issue"

# 合併到 main
gh pr create --base main --title "release: v2.1.0"
gh pr merge --merge

# 打 Tag
gh release create v2.1.0 --title "Release 2.1.0" --generate-notes

# 合併回 develop
gh pr create --base develop --head release/2.1.0 --title "chore: merge release/2.1.0 back to develop"
```

## 5.8 Hotfix Branch

```bash
# 從 main 建立 Hotfix
git checkout -b hotfix/fix-sql-injection main

# 修復
git commit -am "fix: sanitize SQL input parameters"

# 合併到 main
gh pr create --base main --title "hotfix: fix SQL injection vulnerability" --label "security,hotfix"
gh pr merge --merge

# 建立 Patch Release
gh release create v2.1.1 --title "Hotfix 2.1.1" --notes "修復 SQL Injection 漏洞"

# 合併回 develop
gh pr create --base develop --head hotfix/fix-sql-injection --title "chore: merge hotfix to develop"
```

## 5.9 Commit Convention

### Conventional Commits 規範

```
<type>(<scope>): <subject>

<body>

<footer>
```

| Type | 說明 | 範例 |
|------|------|------|
| `feat` | 新功能 | `feat(auth): add OAuth2 login` |
| `fix` | Bug 修復 | `fix(api): resolve null pointer in user query` |
| `docs` | 文件 | `docs: update API documentation` |
| `style` | 格式 | `style: fix indentation` |
| `refactor` | 重構 | `refactor(db): extract repository pattern` |
| `perf` | 效能 | `perf(query): add index for user lookup` |
| `test` | 測試 | `test(auth): add login integration test` |
| `build` | 建置 | `build: update Maven dependencies` |
| `ci` | CI/CD | `ci: add SonarQube scan step` |
| `chore` | 雜項 | `chore: update .gitignore` |

**Breaking Change**：

```bash
git commit -m "feat(api)!: change user endpoint from /users to /api/v2/users

BREAKING CHANGE: user endpoint URL changed, all clients need to update"
```

## 5.10 Pull Request Flow

```bash
# 建立 PR（完整範例）
gh pr create \
  --title "feat(order): implement order processing pipeline" \
  --body-file pr-description.md \
  --base develop \
  --reviewer "tech-lead,senior-dev-1,senior-dev-2" \
  --assignee "@me" \
  --label "feature,backend,needs-review" \
  --milestone "Sprint 12" \
  --project "Backend Roadmap"

# 檢視 PR 狀態
gh pr status
gh pr list --state open --assignee @me

# 檢視 PR 差異
gh pr diff 42

# Review PR
gh pr review 42 --approve --body "LGTM, code quality is good"
gh pr review 42 --request-changes --body "Please add unit tests"
gh pr review 42 --comment --body "Consider using Optional here"

# Merge PR
gh pr merge 42 --squash --delete-branch --body "Squash merge: order processing"

# 關閉 PR（不合併）
gh pr close 42 --comment "Superseded by #45"
```

## 5.11 Code Review Flow

```mermaid
graph LR
    A[開發者建立 PR] --> B[自動化檢查]
    B --> C{CI 通過?}
    C -->|否| D[修復問題]
    D --> B
    C -->|是| E[Reviewer 審查]
    E --> F{審查結果}
    F -->|Request Changes| G[開發者修改]
    G --> E
    F -->|Approve| H{≥2 人 Approve?}
    H -->|否| E
    H -->|是| I[Squash Merge]
    I --> J[自動刪除分支]
    J --> K[觸發 CD]
```

**Code Review 政策建議**：

| 項目 | 建議值 |
|------|--------|
| 最少 Reviewer 數 | 2 人 |
| 自動指派 Reviewer | 透過 CODEOWNERS |
| CI 必須通過 | 是 |
| Conversation 必須全部 Resolved | 是 |
| 合併方式 | Squash Merge |
| 分支自動刪除 | 是 |
| PR 大小限制 | ≤ 400 行變更（建議） |

> **實務建議**：使用 `gh pr create --draft` 建立 Draft PR，在開發早期即可獲得回饋，避免完成後才發現方向錯誤。

---

# 第 6 章：文件管理策略

## 6.1 Markdown 文件管理

```bash
# 在 Repo 中建立標準文件
mkdir -p docs/{architecture,adr,api,guides}

# 建立文件結構
touch docs/architecture/system-overview.md
touch docs/architecture/data-flow.md
touch docs/adr/0001-use-spring-boot.md
touch docs/api/rest-api-spec.md
touch docs/guides/getting-started.md
```

**Markdown 撰寫規範**：

- 使用 ATX 風格標題（`#`），不使用 Setext 風格（底線）
- 標題層級不跳級（`##` 後面接 `###`，不可跳到 `####`）
- 程式碼區塊標示語言（\`\`\`java, \`\`\`yaml）
- 使用 Mermaid 繪製架構圖
- 圖片放在 `docs/images/` 目錄

## 6.2 docs 結構

```
docs/
├── architecture/
│   ├── system-overview.md          # 系統架構總覽
│   ├── data-flow.md                # 資料流
│   ├── deployment.md               # 部署架構
│   └── diagrams/                   # Mermaid / Draw.io 原始檔
├── adr/
│   ├── 0001-use-spring-boot-3.md   # 架構決策紀錄
│   ├── 0002-use-postgresql.md
│   └── template.md                 # ADR Template
├── api/
│   ├── rest-api.md                 # REST API 文件
│   └── openapi.yaml                # OpenAPI 規格
├── guides/
│   ├── getting-started.md          # 入門指南
│   ├── development.md              # 開發指南
│   ├── deployment.md               # 部署指南
│   └── troubleshooting.md          # 故障排除
├── runbooks/
│   ├── incident-response.md        # 事件處理
│   └── disaster-recovery.md        # 災難復原
└── README.md                       # 文件索引
```

## 6.3 ADR 管理

```bash
# ADR（Architecture Decision Record）範本
cat > docs/adr/template.md << 'EOF'
# ADR-XXXX: [決策標題]

## 狀態
提議 / 接受 / 棄用 / 取代

## 日期
YYYY-MM-DD

## 背景
[描述促使此決策的技術或業務背景]

## 決策
[明確描述所做的架構決策]

## 理由
[說明為何做此決策，比較過哪些替代方案]

## 影響
[此決策帶來的正面與負面影響]

## 相關
- 取代：ADR-XXXX
- 相關：ADR-YYYY
EOF
```

## 6.4 Architecture 文件

```bash
# 使用 Mermaid 在 Markdown 中繪製架構圖
cat > docs/architecture/system-overview.md << 'EOF'
# 系統架構總覽

```mermaid
graph TB
    subgraph "Frontend"
        Vue[Vue 3 App]
        Admin[Admin Portal]
    end
    
    subgraph "API Gateway"
        GW[Spring Cloud Gateway]
    end
    
    subgraph "Microservices"
        US[User Service]
        OS[Order Service]
        PS[Payment Service]
    end
    
    subgraph "Data Layer"
        PG[(PostgreSQL)]
        Redis[(Redis)]
        MQ[RabbitMQ]
    end
    
    Vue --> GW
    Admin --> GW
    GW --> US
    GW --> OS
    GW --> PS
    US --> PG
    US --> Redis
    OS --> PG
    OS --> MQ
    PS --> PG
    PS --> MQ
```
EOF
```

## 6.5 API 文件

```bash
# 建立 OpenAPI 規格檔
cat > docs/api/openapi.yaml << 'EOF'
openapi: 3.0.3
info:
  title: User Service API
  version: 1.0.0
  description: 使用者管理 API
paths:
  /api/v1/users:
    get:
      summary: 取得使用者列表
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 0
        - name: size
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: 成功
    post:
      summary: 建立使用者
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: 建立成功
EOF
```

## 6.6 README 標準化

```bash
# 企業級 README Template
cat > README-template.md << 'EOF'
# 專案名稱

> 一句話描述專案用途

![CI](https://github.com/myorg/myrepo/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)

## 目錄
- [架構](#架構)
- [前置需求](#前置需求)
- [快速開始](#快速開始)
- [開發指南](#開發指南)
- [測試](#測試)
- [部署](#部署)
- [API 文件](#api-文件)
- [貢獻指南](#貢獻指南)

## 架構
[簡要架構圖]

## 前置需求
- Java 21+
- Maven 3.9+
- Docker 25+
- PostgreSQL 16+

## 快速開始
\```bash
git clone git@github.com:myorg/myrepo.git
cd myrepo
mvn spring-boot:run
\```

## 開發指南
詳見 [docs/guides/development.md](docs/guides/development.md)

## 測試
\```bash
mvn test                    # 單元測試
mvn verify                  # 整合測試
\```

## 部署
詳見 [docs/guides/deployment.md](docs/guides/deployment.md)

## 貢獻指南
詳見 [CONTRIBUTING.md](CONTRIBUTING.md)

## 維護團隊
| 角色 | 人員 |
|------|------|
| Tech Lead | @tech-lead |
| Backend | @backend-team |
EOF
```

## 6.7 Wiki 管理

```bash
# Clone Wiki Repo
gh repo clone myorg/my-service.wiki

# 建立 Wiki 頁面
cd my-service.wiki
echo "# Home Page" > Home.md
echo "# 開發規範" > Development-Standards.md

# 推送 Wiki
git add . && git commit -m "docs: initialize wiki" && git push
```

## 6.8 GitHub Pages

```bash
# 啟用 GitHub Pages
gh api repos/myorg/my-docs \
  -X PUT \
  -f source='{"branch":"main","path":"/docs"}' \
  --input - << 'EOF'
{
  "source": {
    "branch": "main",
    "path": "/docs"
  }
}
EOF

# 使用 GitHub Actions 部署 Pages
# .github/workflows/pages.yml
cat > .github/workflows/pages.yml << 'WORKFLOW'
name: Deploy GitHub Pages
on:
  push:
    branches: [main]
    paths: ['docs/**']

permissions:
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs/
      - uses: actions/deploy-pages@v4
WORKFLOW
```

> **實務建議**：
> - 所有 Repo 必須有 README.md，且符合公司標準化格式
> - 架構決策使用 ADR 紀錄，不可只放在會議紀錄中
> - API 文件使用 OpenAPI 規格，可自動生成文件網站
> - 文件與程式碼放同一 Repo，隨程式碼版本一起管理

---

# 第 7 章：GitHub CLI 常用指令大全

## 7.1 gh repo

Repository 管理的核心指令群。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Repo | `gh repo create myorg/svc --private` |
| `clone` | Clone Repo | `gh repo clone myorg/svc` |
| `fork` | Fork Repo | `gh repo fork upstream/svc` |
| `list` | 列出 Repo | `gh repo list myorg --limit 50` |
| `view` | 檢視 Repo 資訊 | `gh repo view myorg/svc` |
| `edit` | 編輯 Repo 設定 | `gh repo edit --description "New desc"` |
| `delete` | 刪除 Repo | `gh repo delete myorg/old-svc --yes` |
| `archive` | 封存 Repo | `gh repo archive myorg/legacy` |
| `rename` | 重新命名 | `gh repo rename new-name` |
| `sync` | 同步 Fork | `gh repo sync owner/repo` |
| `set-default` | 設定預設 Repo | `gh repo set-default myorg/svc` |

### 進階範例

```bash
# 列出 Organization 所有 Repo（JSON 格式）
gh repo list myorg --limit 200 --json name,visibility,pushedAt \
  --jq '.[] | "\(.name)\t\(.visibility)\t\(.pushedAt)"'

# 批次 Clone 所有私有 Repo
gh repo list myorg --visibility private --json name --jq '.[].name' | \
  xargs -P 4 -I {} gh repo clone myorg/{}

# 查看 Repo 詳細資訊（含語言、Star、Fork）
gh repo view myorg/user-service --json name,description,primaryLanguage,stargazerCount

# 編輯 Repo 設定
gh repo edit myorg/svc \
  --default-branch main \
  --enable-issues \
  --enable-wiki=false \
  --delete-branch-on-merge
```

**使用情境**：DevOps 團隊批次建立微服務 Repo、定期盤點 Repo 使用狀態。

**最佳實務**：搭配 `--json` 和 `--jq` 輸出結構化資料，方便後續腳本處理。

## 7.2 gh pr

Pull Request 管理，開發日常最高頻指令。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 PR | `gh pr create --title "feat: login"` |
| `list` | 列出 PR | `gh pr list --state open` |
| `view` | 檢視 PR | `gh pr view 42` |
| `status` | 目前 PR 狀態 | `gh pr status` |
| `diff` | 檢視差異 | `gh pr diff 42` |
| `review` | Review PR | `gh pr review 42 --approve` |
| `merge` | 合併 PR | `gh pr merge 42 --squash` |
| `close` | 關閉 PR | `gh pr close 42` |
| `reopen` | 重新開啟 | `gh pr reopen 42` |
| `checkout` | 切換到 PR 分支 | `gh pr checkout 42` |
| `ready` | 標記為 Ready | `gh pr ready 42` |
| `comment` | 新增留言 | `gh pr comment 42 --body "LGTM"` |
| `edit` | 編輯 PR | `gh pr edit 42 --title "new title"` |
| `checks` | 檢視 CI 狀態 | `gh pr checks 42` |

### 進階範例

```bash
# 建立 Draft PR
gh pr create --draft --title "WIP: refactor auth module" --base develop

# 建立 PR 並指定 Reviewer、Label、Milestone
gh pr create \
  --title "feat(order): add payment integration" \
  --body "## Changes
- Integrate Stripe API
- Add payment webhook handler
- Add retry mechanism" \
  --reviewer "tech-lead,payment-expert" \
  --label "feature,payment" \
  --milestone "Q2 Release"

# 列出需要我 Review 的 PR
gh pr list --search "review-requested:@me"

# 批次 Approve PR（僅限測試環境）
gh pr list --state open --json number --jq '.[].number' | \
  xargs -I {} gh pr review {} --approve

# 等待 CI 通過後自動 Merge
gh pr merge 42 --squash --delete-branch --auto

# 檢視 PR 的 CI Check 狀態
gh pr checks 42 --watch
```

**使用情境**：日常開發建立 PR、Code Review、自動化 Merge 流程。

**最佳實務**：
- 使用 `--auto` 啟用 Auto-merge，CI 通過後自動合併
- 使用 `--squash` 保持 main 分支歷史乾淨
- 使用 `--delete-branch` 自動清理已合併分支

## 7.3 gh issue

Issue 管理指令。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Issue | `gh issue create --title "Bug: login fails"` |
| `list` | 列出 Issue | `gh issue list --state open` |
| `view` | 檢視 Issue | `gh issue view 123` |
| `close` | 關閉 Issue | `gh issue close 123` |
| `reopen` | 重新開啟 | `gh issue reopen 123` |
| `comment` | 新增留言 | `gh issue comment 123 --body "Fixed"` |
| `edit` | 編輯 Issue | `gh issue edit 123 --add-label "bug"` |
| `status` | 目前 Issue 狀態 | `gh issue status` |
| `transfer` | 轉移 Issue | `gh issue transfer 123 myorg/other-repo` |
| `pin` | 置頂 Issue | `gh issue pin 123` |
| `lock` | 鎖定 Issue | `gh issue lock 123` |
| `delete` | 刪除 Issue | `gh issue delete 123 --yes` |
| `develop` | 建立分支處理 Issue | `gh issue develop 123` |

### 進階範例

```bash
# 建立 Bug Report
gh issue create \
  --title "Bug: 使用者登入後 Session 逾時過快" \
  --body "## 重現步驟
1. 登入系統
2. 等待 5 分鐘
3. 操作任何功能

## 預期結果
Session 應維持 30 分鐘

## 實際結果
5 分鐘後即被登出" \
  --label "bug,priority-high" \
  --assignee "backend-dev-1" \
  --milestone "Sprint 13"

# 列出高優先 Bug
gh issue list --label "bug,priority-high" --state open

# 從 Issue 建立開發分支
gh issue develop 123 --checkout --base develop

# 批次關閉已解決的 Issue
gh issue list --state open --label "resolved" --json number --jq '.[].number' | \
  xargs -I {} gh issue close {} --comment "Closed: resolved in latest release"

# 搜尋 Issue
gh issue list --search "is:open label:bug sort:created-desc"
```

**最佳實務**：使用 Issue Template 標準化 Bug Report 和 Feature Request 格式。

## 7.4 gh release

Release 管理指令。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Release | `gh release create v1.0.0` |
| `list` | 列出 Release | `gh release list` |
| `view` | 檢視 Release | `gh release view v1.0.0` |
| `delete` | 刪除 Release | `gh release delete v1.0.0` |
| `download` | 下載 Asset | `gh release download v1.0.0` |
| `upload` | 上傳 Asset | `gh release upload v1.0.0 app.jar` |
| `edit` | 編輯 Release | `gh release edit v1.0.0 --draft=false` |

### 進階範例

```bash
# 建立 Release（自動產生 Release Notes）
gh release create v2.1.0 \
  --title "Release 2.1.0" \
  --generate-notes \
  --latest

# 建立 Pre-release
gh release create v2.2.0-rc.1 \
  --title "Release 2.2.0 RC1" \
  --prerelease \
  --generate-notes

# 建立 Release 並上傳 Asset
gh release create v2.1.0 \
  --title "Release 2.1.0" \
  --notes-file CHANGELOG.md \
  ./target/app-2.1.0.jar \
  ./target/app-2.1.0.jar.sha256

# 下載最新 Release 的 Asset
gh release download --pattern "*.jar"

# 編輯 Release（取消 Draft）
gh release edit v2.1.0 --draft=false --latest
```

**最佳實務**：使用 `--generate-notes` 自動從 PR 標題產生 Release Notes，搭配 Conventional Commits 效果最佳。

## 7.5 gh workflow

GitHub Actions Workflow 管理。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `list` | 列出 Workflow | `gh workflow list` |
| `view` | 檢視 Workflow | `gh workflow view ci.yml` |
| `run` | 手動觸發 Workflow | `gh workflow run ci.yml` |
| `enable` | 啟用 Workflow | `gh workflow enable ci.yml` |
| `disable` | 停用 Workflow | `gh workflow disable ci.yml` |

### 進階範例

```bash
# 列出所有 Workflow 及狀態
gh workflow list

# 手動觸發 Workflow（帶參數）
gh workflow run deploy.yml \
  -f environment=staging \
  -f version=2.1.0

# 觸發後監控執行結果
gh workflow run ci.yml && sleep 5 && gh run list --workflow=ci.yml --limit 1

# 停用所有 Workflow（維護時使用）
gh workflow list --json id --jq '.[].id' | \
  xargs -I {} gh workflow disable {}
```

## 7.6 gh run

Workflow 執行管理。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `list` | 列出執行紀錄 | `gh run list` |
| `view` | 檢視執行詳情 | `gh run view 12345` |
| `watch` | 即時監控執行 | `gh run watch 12345` |
| `rerun` | 重新執行 | `gh run rerun 12345` |
| `cancel` | 取消執行 | `gh run cancel 12345` |
| `download` | 下載 Artifact | `gh run download 12345` |
| `delete` | 刪除執行紀錄 | `gh run delete 12345` |

### 進階範例

```bash
# 即時監控最新的 CI 執行
gh run watch

# 檢視失敗的 Workflow Run Log
gh run view 12345 --log-failed

# 重新執行失敗的 Job
gh run rerun 12345 --failed

# 下載 Artifact
gh run download 12345 -n test-results

# 列出最近失敗的 Run
gh run list --status failure --limit 10

# 清理舊的 Run 紀錄
gh run list --status completed --json databaseId --jq '.[10:][].databaseId' | \
  xargs -I {} gh run delete {}
```

## 7.7 gh api

直接呼叫 GitHub API，覆蓋 `gh` 原生指令未涵蓋的功能。

### 基本用法

```bash
# GET 請求
gh api repos/{owner}/{repo}

# POST 請求
gh api repos/{owner}/{repo}/issues \
  -f title="New Issue" \
  -f body="Issue body"

# PATCH 請求
gh api repos/{owner}/{repo} \
  -X PATCH \
  -f description="Updated description"

# DELETE 請求
gh api repos/{owner}/{repo}/branches/old-branch -X DELETE

# GraphQL 查詢
gh api graphql -f query='
  query($org: String!) {
    organization(login: $org) {
      repositories(first: 100) {
        nodes { name isArchived pushedAt }
      }
    }
  }
' -f org="myorg"

# 使用 jq 過濾
gh api repos/{owner}/{repo}/pulls \
  --jq '.[] | {number, title, user: .user.login}'

# 分頁查詢
gh api repos/{owner}/{repo}/issues --paginate --jq '.[].title'

# 使用 Cache 減少 API 呼叫
gh api repos/{owner}/{repo} --cache 1h
```

### 企業常用 API 範例

```bash
# 設定 Branch Protection
gh api repos/myorg/my-service/branches/main/protection \
  -X PUT \
  --input - << 'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["ci/build", "ci/test", "security/scan"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 2,
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF

# 取得 Organization Audit Log
gh api orgs/myorg/audit-log \
  --method GET \
  -f phrase="action:repo.create" \
  -f per_page=100 \
  --jq '.[] | "\(.created_at)\t\(.actor)\t\(.action)\t\(.repo)"'

# 列出所有 Organization 成員
gh api orgs/myorg/members --paginate --jq '.[].login'
```

**最佳實務**：
- 使用 `--cache` 避免重複 API 呼叫
- 使用 `--paginate` 處理大量資料
- 使用 `--jq` 在指令層過濾，減少資料傳輸量

## 7.8 gh alias

自訂指令縮寫，提升團隊效率。

```bash
# 設定 Alias
gh alias set prc 'pr create --draft'
gh alias set prs 'pr status'
gh alias set prm 'pr merge --squash --delete-branch'
gh alias set co 'pr checkout'

# 複雜 Alias（帶 Shell 指令）
gh alias set --shell my-repos 'gh repo list myorg --limit 100 --json name --jq ".[].name"'

# 列出所有 Alias
gh alias list

# 刪除 Alias
gh alias delete prc

# 匯出 Alias（團隊共享）
gh config get aliases > team-aliases.yml

# 團隊建議 Alias 清單
gh alias set pr-mine 'pr list --author @me'
gh alias set pr-review 'pr list --search "review-requested:@me"'
gh alias set issue-mine 'issue list --assignee @me'
gh alias set wf-status 'run list --limit 5'
gh alias set repo-info 'repo view --json name,description,primaryLanguage,stargazerCount'
```

**最佳實務**：將團隊共用的 Alias 放在 Repo 的 `scripts/setup-aliases.sh` 中，新人入職時執行即可。

## 7.9 gh extension

擴充 `gh` 功能的外掛系統。

```bash
# 搜尋 Extension
gh extension search dashboard
gh extension search copilot

# 安裝 Extension
gh extension install github/gh-copilot      # GitHub Copilot CLI
gh extension install dlvhdr/gh-dash         # GitHub Dashboard
gh extension install muesli/gh-stats        # Repo 統計
gh extension install vilmibm/gh-screensaver # 螢幕保護程式

# 列出已安裝的 Extension
gh extension list

# 更新 Extension
gh extension upgrade --all
gh extension upgrade gh-copilot

# 移除 Extension
gh extension remove gh-dash

# 使用 Extension
gh dash                    # 開啟 Dashboard TUI
gh copilot suggest "list all running containers"
gh copilot explain "awk '{print $2}' /var/log/syslog"
```

**企業推薦 Extension**：

| Extension | 用途 | 安裝指令 |
|-----------|------|---------|
| `gh-copilot` | AI 指令建議 | `gh extension install github/gh-copilot` |
| `gh-dash` | TUI Dashboard | `gh extension install dlvhdr/gh-dash` |
| `gh-poi` | 清理已合併分支 | `gh extension install seachicken/gh-poi` |
| `gh-markdown-preview` | 預覽 Markdown | `gh extension install yusukebe/gh-markdown-preview` |

## 7.10 gh browse

在瀏覽器中開啟 Repository、Issue、PR 等 GitHub 頁面，減少手動複製 URL 的操作。

```bash
# 開啟目前 Repo 的 GitHub 頁面
gh browse

# 開啟特定檔案
gh browse src/main/java/com/example/App.java

# 開啟特定檔案的某一行
gh browse src/main/java/com/example/App.java:42

# 開啟 Settings 頁面
gh browse --settings

# 開啟 Projects 頁面
gh browse --projects

# 開啟 Wiki 頁面
gh browse --wiki

# 僅輸出 URL 不開啟瀏覽器
gh browse --no-browser

# 開啟其他 Repo
gh browse --repo myorg/other-service
```

**使用情境**：快速在瀏覽器中開啟當前 Repo 的頁面，或將 URL 傳給團隊成員。

## 7.11 gh codespace

管理 GitHub Codespaces 雲端開發環境，適合遠端團隊與標準化開發環境。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Codespace | `gh codespace create` |
| `list` | 列出 Codespace | `gh codespace list` |
| `code` | 在 VS Code 中開啟 | `gh codespace code` |
| `ssh` | SSH 連線 | `gh codespace ssh` |
| `stop` | 停止 Codespace | `gh codespace stop` |
| `delete` | 刪除 Codespace | `gh codespace delete` |
| `ports` | 管理轉發埠 | `gh codespace ports` |
| `cp` | 檔案複製 | `gh codespace cp` |
| `logs` | 檢視日誌 | `gh codespace logs` |
| `rebuild` | 重建容器 | `gh codespace rebuild` |
| `view` | 檢視詳情 | `gh codespace view` |

> **提示**：所有 `gh codespace` 指令皆可用 `gh cs` 簡寫替代。

### 進階範例

```bash
# 建立指定規格的 Codespace
gh codespace create --repo myorg/my-service --machine largePremiumLinux

# 在 Web 版 VS Code 開啟
gh codespace code -w

# 管理埠轉發
gh codespace ports forward 8080:8080

# 批次清理停止的 Codespace
gh codespace list --json name,state --jq '.[] | select(.state=="Shutdown") | .name' | \
  xargs -I {} gh codespace delete -c {}
```

## 7.12 gh gist

管理 GitHub Gist（程式碼片段分享）。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Gist | `gh gist create file.py` |
| `list` | 列出 Gist | `gh gist list` |
| `view` | 檢視 Gist | `gh gist view GIST_ID` |
| `edit` | 編輯 Gist | `gh gist edit GIST_ID` |
| `clone` | Clone Gist | `gh gist clone GIST_ID` |
| `delete` | 刪除 Gist | `gh gist delete GIST_ID` |
| `rename` | 重新命名 | `gh gist rename GIST_ID old new` |

```bash
# 建立公開 Gist
gh gist create --public script.sh

# 從 stdin 建立 Gist
echo "SELECT * FROM users;" | gh gist create --filename query.sql

# 建立多檔案 Gist
gh gist create file1.py file2.py --desc "Utility scripts"

# 列出自己的 Gist
gh gist list --limit 20
```

## 7.13 gh project

管理 GitHub Projects V2，適合團隊專案追蹤與規劃。

> **權限需求**：使用 `gh project` 需要 `project` scope，可透過 `gh auth refresh -s project` 新增。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Project | `gh project create --title "Roadmap"` |
| `list` | 列出 Project | `gh project list` |
| `view` | 檢視 Project | `gh project view 1 --web` |
| `edit` | 編輯 Project | `gh project edit 1 --title "New Title"` |
| `close` | 關閉 Project | `gh project close 1` |
| `delete` | 刪除 Project | `gh project delete 1` |
| `copy` | 複製 Project | `gh project copy 1 --title "Copy"` |
| `item-add` | 新增項目 | `gh project item-add 1 --url ISSUE_URL` |
| `item-list` | 列出項目 | `gh project item-list 1` |
| `item-create` | 建立草稿項目 | `gh project item-create 1 --title "Task"` |
| `item-edit` | 編輯項目 | `gh project item-edit` |
| `item-delete` | 刪除項目 | `gh project item-delete` |
| `item-archive` | 封存項目 | `gh project item-archive` |
| `field-list` | 列出欄位 | `gh project field-list 1` |
| `field-create` | 建立欄位 | `gh project field-create 1` |
| `field-delete` | 刪除欄位 | `gh project field-delete` |
| `link` | 連結 Repo | `gh project link 1 --repo OWNER/REPO` |
| `unlink` | 取消連結 | `gh project unlink 1 --repo OWNER/REPO` |
| `mark-template` | 設為範本 | `gh project mark-template 1` |

```bash
# 建立 Organization Project
gh project create --owner myorg --title "Q3 Roadmap"

# 列出 Organization 的 Project
gh project list --owner myorg

# 將 Issue 加入 Project
gh project item-add 1 --owner myorg --url "https://github.com/myorg/repo/issues/42"

# 建立草稿項目
gh project item-create 1 --owner myorg --title "研究新框架" --body "評估 Quarkus vs Micronaut"

# 檢視 Project 欄位定義
gh project field-list 1 --owner myorg
```

## 7.14 gh search

跨 GitHub 平台搜尋 Code、Issues、PRs、Repos、Commits。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `repos` | 搜尋 Repo | `gh search repos "spring boot"` |
| `issues` | 搜尋 Issue | `gh search issues "bug label:critical"` |
| `prs` | 搜尋 PR | `gh search prs "review-requested:@me"` |
| `code` | 搜尋程式碼 | `gh search code "ClassName"` |
| `commits` | 搜尋 Commit | `gh search commits "fix security"` |

```bash
# 搜尋 Organization 中的 Repo
gh search repos --owner myorg --language java --json name,description

# 搜尋等待自己 Review 的 PR
gh search prs --review-requested=@me --state=open

# 搜尋程式碼中的特定 Pattern
gh search code "password" --owner myorg --filename "*.properties"

# 搜尋高嚴重性 Bug
gh search issues --label "bug,priority-high" --state open --owner myorg

# 排除特定標籤的搜尋（Unix）
gh search issues -- "my-query -label:wontfix"

# 排除特定標籤的搜尋（PowerShell）
gh --% search issues -- "my-query -label:wontfix"
```

> **注意**：在 PowerShell 中使用排除語法時，需要搭配 `--% ` stop-parse 符號與 `--` 引數分隔符，以避免 `-` 被解讀為旗標。

## 7.15 gh cache

管理 GitHub Actions 的 Cache 儲存，可列出與清理 CI/CD 快取。

```bash
# 列出所有 Cache
gh cache list

# 列出 Cache 並顯示大小
gh cache list --json id,key,sizeInBytes --jq '.[] | "\(.key)\t\(.sizeInBytes / 1048576 | floor)MB"'

# 刪除特定 Cache
gh cache delete CACHE_ID

# 刪除所有 Cache
gh cache delete --all

# 刪除符合特定 Pattern 的 Cache
gh cache list --json id,key --jq '.[] | select(.key | startswith("maven-")) | .id' | \
  xargs -I {} gh cache delete {}
```

**使用情境**：CI/CD 快取膨脹時批次清理過期快取，或在依賴版本升級後清除舊快取。

## 7.16 gh attestation

下載與驗證 Artifact Attestation，用於供應鏈安全驗證。這是 GitHub 對 SLSA（Supply-chain Levels for Software Artifacts）框架的實作。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `verify` | 驗證 Attestation | `gh attestation verify artifact.jar` |
| `download` | 下載 Attestation | `gh attestation download artifact.jar` |
| `trusted-root` | 管理信任根 | `gh attestation trusted-root` |

> **別名**：可使用 `gh at` 作為 `gh attestation` 的簡寫。

```bash
# 驗證 JAR 檔的 Attestation
gh attestation verify ./target/app-1.0.0.jar --repo myorg/my-service

# 下載 Attestation 以供離線驗證
gh attestation download ./target/app-1.0.0.jar --repo myorg/my-service

# 在 CI/CD 中驗證建置產物
gh attestation verify ./build/output.zip \
  --repo myorg/my-service \
  --signer-workflow "myorg/my-service/.github/workflows/release.yml"
```

**企業價值**：確保部署的 Artifact 確實由受信任的 CI/CD Pipeline 產出，防止供應鏈攻擊。

## 7.17 gh ruleset

檢視 Repository 和 Organization 層級的 Ruleset 定義。Ruleset 是 Branch Protection 的進化版，提供更細緻的規則管理。

> **別名**：可使用 `gh rs` 作為 `gh ruleset` 的簡寫。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `list` | 列出 Ruleset | `gh ruleset list` |
| `view` | 檢視 Ruleset 詳情 | `gh ruleset view` |
| `check` | 檢查分支是否符合規則 | `gh ruleset check branch-name` |

```bash
# 列出 Repo 的所有 Ruleset
gh ruleset list

# 在瀏覽器中檢視 Ruleset
gh ruleset view --repo myorg/my-service --web

# 檢查特定分支是否符合 Ruleset
gh ruleset check main

# 檢查其他 Repo 的 Ruleset
gh ruleset list --repo myorg/other-service
```

**與 Branch Protection 的差異**：Ruleset 支援 Organization 層級統一套用、支援 Tag 保護、支援 Bypass 清單，且可透過 API 建立（詳見 12.2 節）。

## 7.18 gh label

管理 Repository 的 Label（標籤），適合批次建立與標準化團隊標籤體系。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `create` | 建立 Label | `gh label create "bug" --color "d73a4a"` |
| `list` | 列出 Label | `gh label list` |
| `edit` | 編輯 Label | `gh label edit "bug" --color "ff0000"` |
| `delete` | 刪除 Label | `gh label delete "obsolete"` |
| `clone` | 複製其他 Repo 的 Label | `gh label clone source-repo` |

```bash
# 列出 Repo 的所有 Label
gh label list --json name,color,description

# 建立企業標準 Label
gh label create "priority-critical" --color "b60205" --description "最高優先"
gh label create "priority-high" --color "d93f0b" --description "高優先"
gh label create "priority-medium" --color "fbca04" --description "中優先"
gh label create "priority-low" --color "0e8a16" --description "低優先"

# 從 Template Repo 複製 Label 到新 Repo
gh label clone myorg/label-template --repo myorg/new-service

# 批次建立 Label（搭配 Shell）
labels=("feature:a2eeef" "bug:d73a4a" "security:e4e669" "documentation:0075ca" "dependencies:0366d6")
for entry in "${labels[@]}"; do
  name="${entry%%:*}"
  color="${entry##*:}"
  gh label create "$name" --color "$color" --force
done
```

## 7.19 gh variable

管理 GitHub Actions 的 Variables（非機敏性設定值），與 Secret 搭配使用。

```bash
# 設定 Repo Variable
gh variable set APP_NAME --body "my-service"
gh variable set DEPLOY_REGION --body "ap-northeast-1"

# 列出 Variable
gh variable list

# 設定 Environment Variable
gh variable set APP_URL --env staging --body "https://staging.company.com"
gh variable set APP_URL --env production --body "https://api.company.com"

# 設定 Organization Variable
gh variable set ORG_DOMAIN --org myorg --body "company.com"

# 刪除 Variable
gh variable delete APP_NAME

# 取得 Variable 值
gh variable get APP_NAME
```

**與 Secret 的差異**：Variable 用於非機敏設定（如環境名稱、區域），可在 Log 中顯示；Secret 用於機敏資訊（如 API Key、密碼），永不顯示於 Log。

## 7.20 gh secret

管理 GitHub Actions 的 Secrets（機敏資訊），支援 Repo、Organization、Environment、Dependabot 四個層級。

```bash
# 設定 Repo Secret
gh secret set API_KEY --body "your-api-key-value"
gh secret set DB_PASSWORD < db_password.txt

# 列出 Secret（僅名稱，不顯示值）
gh secret list

# 設定 Organization Secret
gh secret set ORG_SECRET --org myorg --body "org-value"

# 設定 Environment Secret
gh secret set DEPLOY_KEY --env production --body "production-key"

# 設定 Dependabot Secret
gh secret set REGISTRY_TOKEN --app dependabot --body "token-value"

# 刪除 Secret
gh secret delete API_KEY
```

> **安全提醒**：永遠不要在 `--body` 中直接傳入機敏值於共享終端。建議使用 `< file` 或 `echo $VAR | gh secret set NAME` 方式。

## 7.21 gh status

快速檢視個人在 GitHub 上的工作狀態，包含被指派的 Issue、需要 Review 的 PR、CI 狀態等。

```bash
# 檢視個人狀態總覽
gh status

# 輸出範例：
# Assigned Issues
#   myorg/user-service#42  Bug: login timeout
#   myorg/order-service#15 Feature: add payment
#
# Review Requests
#   myorg/user-service#43  feat: add OAuth2
#
# Mentions
#   myorg/docs#7  @username can you review?

# 排除特定 Organization
gh status --exclude myorg-archived

# 指定特定 Organization
gh status --org myorg
```

**使用情境**：每日站會前快速確認自己的待辦事項，取代逐一檢查各 Repo 的通知。

## 7.22 gh config

管理 GitHub CLI 的全域與 Host 特定設定。

### 常用子指令

| 子指令 | 說明 | 範例 |
|--------|------|------|
| `get` | 取得設定值 | `gh config get editor` |
| `set` | 設定值 | `gh config set editor "code -w"` |
| `list` | 列出所有設定 | `gh config list` |
| `clear-cache` | 清除快取 | `gh config clear-cache` |

```bash
# 設定預設編輯器
gh config set editor "code -w"

# 設定 Git 協議
gh config set git_protocol ssh --host github.com

# 啟用互動式提示
gh config set prompt enabled

# 設定分頁程式
gh config set pager "less -R"

# 關閉遙測
gh config set telemetry disabled

# 檢視遙測資料（不實際送出）
gh config set telemetry log

# 列出當前所有設定
gh config list

# 檢視特定 Host 設定
gh config list --host github.company.com

# 清除 HTTP 快取
gh config clear-cache
```

**設定檔位置**：設定存放於 `~/.config/gh/config.yml`（macOS/Linux）或 `%APPDATA%\GitHub CLI\config.yml`（Windows）。

---

# 第 8 章：GitHub Actions 與 Workflow Automation

## 8.1 GitHub Actions 架構

```mermaid
graph TB
    subgraph "GitHub Actions 架構"
        Event[事件觸發<br/>push / PR / schedule] --> Workflow[Workflow<br/>.github/workflows/*.yml]
        Workflow --> Job1[Job: build]
        Workflow --> Job2[Job: test]
        Workflow --> Job3[Job: deploy]
        
        Job1 --> Runner1[Runner<br/>ubuntu-latest]
        Job2 --> Runner2[Runner<br/>ubuntu-latest]
        Job3 --> Runner3[Self-hosted Runner]
        
        Runner1 --> Step1[Step: checkout]
        Runner1 --> Step2[Step: setup-java]
        Runner1 --> Step3[Step: mvn compile]
    end
    
    subgraph "外部整合"
        Secrets[GitHub Secrets]
        Artifacts[Artifacts Storage]
        Cache[Cache Storage]
        Env[Environments]
    end
    
    Job1 --> Secrets
    Job1 --> Cache
    Job2 --> Artifacts
    Job3 --> Env
```

## 8.2 Workflow 基礎

**Workflow 目錄結構**：

```
.github/
├── workflows/
│   ├── ci.yml              # CI Pipeline
│   ├── cd.yml              # CD Pipeline
│   ├── release.yml         # Release Pipeline
│   ├── security.yml        # Security Scan
│   ├── codeql.yml          # CodeQL Analysis
│   └── dependabot-merge.yml # Dependabot Auto-merge
├── ISSUE_TEMPLATE/
│   ├── bug_report.yml
│   └── feature_request.yml
├── PULL_REQUEST_TEMPLATE.md
├── CODEOWNERS
└── dependabot.yml
```

### Workflow 基本語法

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
  workflow_dispatch:        # 允許手動觸發

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # 取消同分支的舊 Run

permissions:
  contents: read
  pull-requests: write

env:
  JAVA_VERSION: '21'
  MAVEN_OPTS: '-Xmx1024m'

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: ${{ env.JAVA_VERSION }}
          distribution: 'temurin'
          cache: 'maven'
      - run: mvn compile -B -q
```

## 8.3 Runner 與 Self-hosted Runner

```bash
# 列出 Workflow Runner
gh api orgs/myorg/actions/runners --jq '.runners[] | "\(.id)\t\(.name)\t\(.status)"'

# 檢視 Runner 使用統計
gh run list --json databaseId,status,conclusion --jq '
  group_by(.conclusion) | 
  map({conclusion: .[0].conclusion, count: length})'
```

**Self-hosted Runner 設定**：

```bash
# 下載 Runner
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.321.0/actions-runner-linux-x64-2.321.0.tar.gz
tar xzf actions-runner-linux-x64.tar.gz

# 設定 Runner
./config.sh --url https://github.com/myorg \
  --token $(gh api orgs/myorg/actions/runners/registration-token -X POST --jq '.token') \
  --name "build-runner-01" \
  --labels "self-hosted,linux,x64,java" \
  --work "_work"

# 啟動為 Service
sudo ./svc.sh install
sudo ./svc.sh start
```

## 8.4 Matrix Build

```yaml
# 多版本、多平台矩陣建置
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        java: ['17', '21']
        os: [ubuntu-latest, windows-latest]
        db: [postgresql, mysql]
        exclude:
          - os: windows-latest
            db: mysql
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: ${{ matrix.java }}
          distribution: 'temurin'
      - run: mvn test -Ddb.type=${{ matrix.db }}
```

## 8.5 Cache 與 Artifact

```yaml
# Maven Cache
- uses: actions/cache@v4
  with:
    path: ~/.m2/repository
    key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
    restore-keys: |
      ${{ runner.os }}-maven-

# 上傳測試報告 Artifact
- uses: actions/upload-artifact@v4
  if: always()
  with:
    name: test-results-${{ matrix.java }}
    path: |
      **/target/surefire-reports/
      **/target/failsafe-reports/
    retention-days: 30

# 下載 Artifact（跨 Job）
- uses: actions/download-artifact@v4
  with:
    name: test-results-21
```

## 8.6 Secret 與 Environment

```bash
# 設定 Secret（CLI）
gh secret set DATABASE_URL --body "jdbc:postgresql://db:5432/mydb"
gh secret set DOCKER_USERNAME --body "deploy-bot"
gh secret set DOCKER_PASSWORD --body "secure-password"

# Environment Secret
gh secret set DEPLOY_KEY --env production --body "production-key"
gh secret set DEPLOY_KEY --env staging --body "staging-key"

# Variable（非機敏資訊）
gh variable set APP_NAME --body "my-service"
gh variable set DEPLOY_REGION --body "ap-northeast-1"
```

```yaml
# 使用 Environment（含審核機制）
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - run: echo "Deploy to staging"

  deploy-production:
    runs-on: ubuntu-latest
    needs: deploy-staging
    environment:
      name: production
      url: https://api.company.com
    steps:
      - run: echo "Deploy to production"
      # 此 Job 會等待 production 環境的審核人員核准
```

## 8.7 CI Workflow 範例

```yaml
# .github/workflows/ci.yml - Spring Boot 完整 CI
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

permissions:
  contents: read
  checks: write
  pull-requests: write

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    timeout-minutes: 20

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: testdb
          POSTGRES_USER: testuser
          POSTGRES_PASSWORD: testpass
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # SonarQube 需要完整歷史

      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'

      - name: Compile
        run: mvn compile -B -q

      - name: Unit Test
        run: mvn test -B

      - name: Integration Test
        run: mvn verify -Pintegration-test -B
        env:
          SPRING_DATASOURCE_URL: jdbc:postgresql://localhost:5432/testdb
          SPRING_DATASOURCE_USERNAME: testuser
          SPRING_DATASOURCE_PASSWORD: testpass

      - name: Publish Test Results
        uses: dorny/test-reporter@v1
        if: always()
        with:
          name: Test Results
          path: '**/target/surefire-reports/*.xml'
          reporter: java-junit

      - name: Upload Coverage
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: target/site/jacoco/

  code-quality:
    runs-on: ubuntu-latest
    needs: build-and-test
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'
      - name: Checkstyle
        run: mvn checkstyle:check -B
      - name: SpotBugs
        run: mvn spotbugs:check -B
```

## 8.8 CD Workflow 範例

```yaml
# .github/workflows/cd.yml - 部署 Pipeline
name: CD Pipeline

on:
  push:
    branches: [main]

permissions:
  contents: read
  packages: write

jobs:
  build-image:
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'

      - name: Build JAR
        run: mvn package -DskipTests -B

      - name: Docker Meta
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=sha,prefix=
            type=raw,value=latest

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and Push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}

  deploy-staging:
    needs: build-image
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to Staging
        run: |
          echo "Deploying ${{ needs.build-image.outputs.image-tag }} to staging"
          # kubectl set image deployment/my-service my-service=$IMAGE_TAG

  deploy-production:
    needs: [build-image, deploy-staging]
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://api.company.com
    steps:
      - name: Deploy to Production
        run: |
          echo "Deploying to production"
```

## 8.9 Release Workflow 範例

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*.*.*'

permissions:
  contents: write
  packages: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'

      - name: Build Release
        run: mvn package -DskipTests -B

      - name: Create GitHub Release
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh release create ${{ github.ref_name }} \
            --title "Release ${{ github.ref_name }}" \
            --generate-notes \
            ./target/*.jar
```

## 8.10 Security Scan Workflow

```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * 1'  # 每週一早上 6 點

permissions:
  security-events: write
  contents: read

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: java
      - uses: github/codeql-action/autobuild@v3
      - uses: github/codeql-action/analyze@v3

  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
      - name: OWASP Dependency Check
        run: mvn org.owasp:dependency-check-maven:check -B
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: dependency-check-report
          path: target/dependency-check-report.html

  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: trufflesecurity/trufflehog@main
        with:
          extra_args: --only-verified
```

## 8.11 AI Workflow

```yaml
# .github/workflows/ai-review.yml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

permissions:
  pull-requests: write
  contents: read

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get PR Diff
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh pr diff ${{ github.event.pull_request.number }} > pr-diff.txt

      - name: AI Review Comment
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # 將 Diff 送至 AI 分析後，將結果寫回 PR Comment
          gh pr comment ${{ github.event.pull_request.number }} \
            --body "## 🤖 AI Code Review
          
          自動化審查已完成，請檢視下方建議。
          
          > 此為 AI 輔助審查，最終判斷仍需人工 Review。"
```

---

# 第 9 章：SSDLC 與 Security

## 9.1 Secret Scanning

```bash
# 檢視 Secret Scanning Alerts
gh api repos/myorg/my-service/secret-scanning/alerts \
  --jq '.[] | "\(.number)\t\(.state)\t\(.secret_type)"'

# 關閉誤報 Alert
gh api repos/myorg/my-service/secret-scanning/alerts/1 \
  -X PATCH \
  -f state="resolved" \
  -f resolution="false_positive"
```

**Push Protection 設定**：

```bash
# 啟用 Push Protection（防止 Secret 被推送）
gh api repos/myorg/my-service \
  -X PATCH \
  --input - << 'EOF'
{
  "security_and_analysis": {
    "secret_scanning": { "status": "enabled" },
    "secret_scanning_push_protection": { "status": "enabled" }
  }
}
EOF
```

## 9.2 Dependabot

```yaml
# .github/dependabot.yml
version: 2
updates:
  # Maven
  - package-ecosystem: "maven"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "06:00"
      timezone: "Asia/Taipei"
    open-pull-requests-limit: 10
    reviewers:
      - "backend-team"
    labels:
      - "dependencies"
      - "security"
    groups:
      spring:
        patterns:
          - "org.springframework*"
      test:
        patterns:
          - "org.junit*"
          - "org.mockito*"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    labels:
      - "ci/cd"
      - "dependencies"

  # Docker
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

```bash
# 使用 CLI 管理 Dependabot Alerts
gh api repos/myorg/my-service/dependabot/alerts \
  --jq '.[] | select(.state=="open") | "\(.number)\t\(.security_advisory.severity)\t\(.dependency.package.name)"'
```

## 9.3 CodeQL

```bash
# 使用 CLI 檢視 CodeQL Alerts
gh api repos/myorg/my-service/code-scanning/alerts \
  --jq '.[] | select(.state=="open") | "\(.number)\t\(.rule.severity)\t\(.rule.description)"'

# 關閉 Alert
gh api repos/myorg/my-service/code-scanning/alerts/1 \
  -X PATCH \
  -f state="dismissed" \
  -f dismissed_reason="won't fix" \
  -f dismissed_comment="False positive in test code"
```

## 9.4 Security Policy

```bash
# 建立 SECURITY.md
cat > SECURITY.md << 'EOF'
# 安全政策

## 支援版本

| 版本 | 支援狀態 |
|------|---------|
| 2.x  | ✅ 支援 |
| 1.x  | ❌ 終止支援 |

## 回報漏洞

請**不要**透過公開 Issue 回報安全漏洞。

請透過以下方式回報：
1. Email: security@company.com
2. GitHub Security Advisory: [建立 Advisory](../../security/advisories/new)

## 回應時間

- 確認收到：24 小時內
- 初步評估：72 小時內
- 修復發佈：依據嚴重程度
  - Critical: 24 小時
  - High: 7 天
  - Medium: 30 天
  - Low: 下個 Release
EOF
```

## 9.5 Branch Protection

```bash
# 使用 gh api 設定 Branch Protection（完整企業級設定）
gh api repos/myorg/my-service/branches/main/protection \
  -X PUT \
  --input - << 'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "CI Pipeline / build-and-test",
      "CI Pipeline / code-quality",
      "Security Scan / codeql",
      "Security Scan / dependency-check"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 2,
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "require_last_push_approval": true
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true
}
EOF

echo "✅ Branch protection configured for main"
```

## 9.6 CODEOWNERS

```bash
# .github/CODEOWNERS
cat > .github/CODEOWNERS << 'EOF'
# 預設 Owner
*                           @myorg/tech-leads

# 後端
src/main/java/              @myorg/backend-team
src/test/java/              @myorg/backend-team

# 前端
src/main/resources/static/  @myorg/frontend-team

# CI/CD
.github/workflows/          @myorg/devops-team
Dockerfile                  @myorg/devops-team

# 安全相關
SECURITY.md                 @myorg/security-team
.github/dependabot.yml      @myorg/security-team

# 文件
docs/                       @myorg/tech-leads
README.md                   @myorg/tech-leads
EOF
```

## 9.7 Signed Commit

```bash
# 設定 Git 使用 GPG 簽署（全域）
git config --global commit.gpgsign true
git config --global tag.gpgsign true
git config --global user.signingkey YOUR_GPG_KEY_ID

# 驗證 Commit 簽署
git log --show-signature -1

# 在 GitHub 上強制要求 Signed Commit
gh api repos/myorg/my-service/branches/main/protection \
  -X PUT \
  --input - << 'EOF'
{
  "required_signatures": true
}
EOF
```

## 9.8 Supply Chain Security 與 SBOM

```bash
# 產生 SBOM（Software Bill of Materials）
# 使用 Maven CycloneDX Plugin
mvn org.cyclonedx:cyclonedx-maven-plugin:makeBom

# 上傳 SBOM 至 GitHub
gh api repos/myorg/my-service/dependency-graph/sbom \
  --jq '.sbom.packages | length'

# 檢視依賴圖
gh api repos/myorg/my-service/dependency-graph/sbom \
  --jq '.sbom.packages[] | "\(.name)\t\(.versionInfo)"'
```

## 9.9 OWASP 與 DevSecOps

```mermaid
graph LR
    subgraph "SSDLC Flow"
        A[Plan] --> B[Code]
        B --> C[Build]
        C --> D[Test]
        D --> E[Release]
        E --> F[Deploy]
        F --> G[Monitor]
        G --> A
    end
    
    subgraph "Security Gates"
        B -.->|Threat Model| S1[設計審查]
        C -.->|SAST / CodeQL| S2[靜態掃描]
        C -.->|Dependency Check| S3[相依性檢查]
        D -.->|DAST| S4[動態測試]
        E -.->|SBOM| S5[供應鏈驗證]
        F -.->|Secret Scan| S6[機敏資訊掃描]
        G -.->|Audit Log| S7[持續監控]
    end
```

## 9.10 SAST 與 DAST

```yaml
# SAST - 靜態分析（在 CI 中執行）
- name: SonarQube Scan
  run: |
    mvn sonar:sonar \
      -Dsonar.host.url=${{ secrets.SONAR_URL }} \
      -Dsonar.token=${{ secrets.SONAR_TOKEN }} \
      -Dsonar.qualitygate.wait=true

# DAST - 動態測試（在部署後執行）
- name: OWASP ZAP Scan
  uses: zaproxy/action-full-scan@v0.12.0
  with:
    target: 'https://staging.company.com'
    rules_file_name: '.zap/rules.tsv'
```

> **實務建議**：
> - SAST 在每次 PR 執行，DAST 在 Staging 部署後執行
> - 使用 `gh api` 定期匯出 Security Alerts 報告
> - 建立 Security Dashboard 追蹤漏洞修復進度
> - 每季進行一次 Security Audit，使用 `gh api orgs/{org}/audit-log` 稽核

---

# 第 10 章：GitHub CLI 自動化腳本

## 10.1 Bash Script

```bash
#!/bin/bash
# repo-health-check.sh - Repo 健康度檢查腳本

set -euo pipefail

ORG="myorg"
REPORT_FILE="repo-health-$(date +%Y%m%d).csv"

echo "Repo,Branch Protection,CODEOWNERS,CI,Dependabot,Last Push" > "$REPORT_FILE"

repos=$(gh repo list "$ORG" --limit 200 --json name --jq '.[].name')

for repo in $repos; do
  echo "Checking $ORG/$repo..."
  
  # Branch Protection
  bp=$(gh api "repos/$ORG/$repo/branches/main/protection" 2>/dev/null && echo "YES" || echo "NO")
  
  # CODEOWNERS
  co=$(gh api "repos/$ORG/$repo/contents/.github/CODEOWNERS" 2>/dev/null && echo "YES" || echo "NO")
  
  # CI Workflow
  ci=$(gh api "repos/$ORG/$repo/actions/workflows" --jq '.total_count' 2>/dev/null || echo "0")
  
  # Dependabot
  dep=$(gh api "repos/$ORG/$repo/contents/.github/dependabot.yml" 2>/dev/null && echo "YES" || echo "NO")
  
  # Last Push
  last=$(gh repo view "$ORG/$repo" --json pushedAt --jq '.pushedAt' 2>/dev/null || echo "N/A")
  
  echo "$repo,$bp,$co,$ci,$dep,$last" >> "$REPORT_FILE"
done

echo "✅ Report saved: $REPORT_FILE"
```

## 10.2 PowerShell Script

```powershell
# repo-init.ps1 - 自動化 Repo 初始化

param(
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    
    [Parameter(Mandatory=$true)]
    [string]$Org,
    
    [string]$Template = "spring-boot-template",
    [string]$Visibility = "private"
)

Write-Host "🚀 Creating repository: $Org/$RepoName" -ForegroundColor Cyan

# 1. 從 Template 建立 Repo
gh repo create "$Org/$RepoName" `
    --template "$Org/$Template" `
    --"$Visibility" `
    --clone

Set-Location $RepoName

# 2. 設定 Branch Protection
$protectionJson = @"
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["CI Pipeline / build-and-test"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 2,
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false
}
"@

$protectionJson | gh api "repos/$Org/$RepoName/branches/main/protection" -X PUT --input -

# 3. 設定 Labels
$labels = @(
    @{name="bug"; color="d73a4a"; description="Bug report"},
    @{name="feature"; color="a2eeef"; description="New feature"},
    @{name="security"; color="e4e669"; description="Security issue"},
    @{name="dependencies"; color="0075ca"; description="Dependency update"}
)

foreach ($label in $labels) {
    gh api "repos/$Org/$RepoName/labels" `
        -X POST `
        -f name=$($label.name) `
        -f color=$($label.color) `
        -f description=$($label.description) 2>$null
}

# 4. 設定 Team 權限
gh api "orgs/$Org/teams/backend-team/repos/$Org/$RepoName" -X PUT -f permission="push"
gh api "orgs/$Org/teams/devops-team/repos/$Org/$RepoName" -X PUT -f permission="admin"

Write-Host "✅ Repository $Org/$RepoName initialized successfully!" -ForegroundColor Green
```

## 10.3 Windows Batch

```cmd
@echo off
REM quick-pr.bat - 快速建立 PR

set /p TITLE="PR Title: "
set /p BODY="PR Body: "

git add .
git commit -m "%TITLE%"
git push origin HEAD

gh pr create --title "%TITLE%" --body "%BODY%" --base main
echo PR created successfully!
pause
```

## 10.4 Python Script

```python
#!/usr/bin/env python3
"""org-audit.py - Organization 稽核報告產生器"""

import subprocess
import json
import csv
from datetime import datetime, timezone

ORG = "myorg"

def gh_api(endpoint: str) -> list | dict:
    """呼叫 gh api 並回傳 JSON"""
    result = subprocess.run(
        ["gh", "api", endpoint, "--paginate"],
        capture_output=True, text=True, check=True
    )
    return json.loads(result.stdout)

def main():
    print(f"🔍 Auditing organization: {ORG}")
    
    # 取得所有 Repo
    repos = json.loads(subprocess.run(
        ["gh", "repo", "list", ORG, "--limit", "500",
         "--json", "name,visibility,pushedAt,isArchived"],
        capture_output=True, text=True, check=True
    ).stdout)
    
    report = []
    for repo in repos:
        if repo["isArchived"]:
            continue
        
        name = repo["name"]
        
        # 檢查 Branch Protection
        try:
            subprocess.run(
                ["gh", "api", f"repos/{ORG}/{name}/branches/main/protection"],
                capture_output=True, check=True
            )
            bp = "✅"
        except subprocess.CalledProcessError:
            bp = "❌"
        
        report.append({
            "repo": name,
            "visibility": repo["visibility"],
            "branch_protection": bp,
            "last_push": repo["pushedAt"][:10]
        })
    
    # 輸出 CSV
    filename = f"audit-{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=report[0].keys())
        writer.writeheader()
        writer.writerows(report)
    
    print(f"✅ Report saved: {filename} ({len(report)} repos)")

if __name__ == "__main__":
    main()
```

## 10.5 Repo 初始化自動化

```bash
#!/bin/bash
# init-microservice.sh - 微服務 Repo 一鍵初始化
# Usage: ./init-microservice.sh myorg order-service

set -euo pipefail

ORG="${1:?Usage: $0 <org> <repo-name>}"
REPO="${2:?Usage: $0 <org> <repo-name>}"
TEMPLATE="$ORG/spring-boot-template"

echo "🚀 Initializing $ORG/$REPO from $TEMPLATE"

# Step 1: 建立 Repo
gh repo create "$ORG/$REPO" --template "$TEMPLATE" --private --clone
cd "$REPO"

# Step 2: 建立 develop 分支
git checkout -b develop
git push -u origin develop

# Step 3: 設定 Branch Protection (main)
gh api "repos/$ORG/$REPO/branches/main/protection" -X PUT --input - << 'PROTECTION'
{
  "required_status_checks": {"strict": true, "contexts": ["CI Pipeline / build-and-test"]},
  "enforce_admins": true,
  "required_pull_request_reviews": {"required_approving_review_count": 2, "dismiss_stale_reviews": true, "require_code_owner_reviews": true},
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": true
}
PROTECTION

# Step 4: 設定 Dependabot Secret（如需私有 Registry）
# gh secret set MAVEN_REGISTRY_TOKEN --body "$MAVEN_TOKEN"

# Step 5: 設定 Team 權限
gh api "orgs/$ORG/teams/backend-team/repos/$ORG/$REPO" -X PUT -f permission="push"
gh api "orgs/$ORG/teams/devops-team/repos/$ORG/$REPO" -X PUT -f permission="admin"
gh api "orgs/$ORG/teams/qa-team/repos/$ORG/$REPO" -X PUT -f permission="triage"

echo "✅ $ORG/$REPO initialized successfully!"
echo "   - Template: $TEMPLATE"
echo "   - Branch Protection: configured"
echo "   - Teams: backend-team(push), devops-team(admin), qa-team(triage)"
```

## 10.6 Branch Protection 自動化

```bash
#!/bin/bash
# apply-branch-protection.sh - 批次套用 Branch Protection
# Usage: ./apply-branch-protection.sh myorg

ORG="${1:?Usage: $0 <org>}"

echo "🔒 Applying branch protection to all repos in $ORG..."

repos=$(gh repo list "$ORG" --json name,isArchived --jq '.[] | select(.isArchived==false) | .name')

for repo in $repos; do
  echo "  Configuring $ORG/$repo..."
  
  gh api "repos/$ORG/$repo/branches/main/protection" -X PUT --input - << 'EOF' 2>/dev/null && \
    echo "    ✅ $repo: configured" || \
    echo "    ⚠️ $repo: skipped (no main branch?)"
{
  "required_status_checks": null,
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
done

echo "🏁 Branch protection applied to all repos."
```

## 10.7 Release Automation

```bash
#!/bin/bash
# release.sh - 自動化 Release 流程
# Usage: ./release.sh 2.1.0

VERSION="${1:?Usage: $0 <version>}"
TAG="v$VERSION"

echo "🚀 Starting release process for $TAG"

# Step 1: 確保在 main 分支且最新
git checkout main && git pull origin main

# Step 2: 建立 Release Branch
git checkout -b "release/$VERSION"

# Step 3: 更新版本號（Maven）
mvn versions:set -DnewVersion="$VERSION" -DgenerateBackupPoms=false
git add pom.xml
git commit -m "chore: bump version to $VERSION"
git push -u origin "release/$VERSION"

# Step 4: 建立 PR 到 main
gh pr create \
  --base main \
  --title "release: v$VERSION" \
  --body "## Release $VERSION

### Changes
$(gh api repos/:owner/:repo/compare/main...release/$VERSION --jq '.commits[] | "- " + .commit.message' | head -20)

### Checklist
- [ ] Version bumped
- [ ] CHANGELOG updated
- [ ] All tests passing
- [ ] Security scan clean" \
  --label "release"

echo "📋 PR created. After merge, run:"
echo "   gh release create $TAG --generate-notes --latest"
```

> **實務建議**：
> - 所有自動化腳本存放在 Repo 的 `scripts/` 目錄，納入版本控制
> - 使用 `set -euo pipefail`（Bash）確保腳本遇錯即停
> - 關鍵操作加上 `--yes` 確認或 Dry-run 模式
> - 定期執行稽核腳本（repo-health-check），產出合規報告

---

# 第 11 章：AI 整合與 Copilot

## 11.1 GitHub Copilot CLI

GitHub Copilot CLI 擴充了 `gh` 的能力，讓開發者能透過自然語言描述來產生指令。

### 安裝與設定

```bash
# 安裝 Copilot Extension
gh extension install github/gh-copilot

# 確認安裝
gh copilot --version

# 更新
gh extension upgrade gh-copilot
```

### 核心功能

```bash
# Suggest - 根據描述產生指令
gh copilot suggest "find all Java files modified in the last 7 days"
gh copilot suggest "list all open PRs that need my review"
gh copilot suggest "create a release with auto-generated notes"

# Explain - 解釋指令用途
gh copilot explain "git rebase -i HEAD~5"
gh copilot explain "awk '{print $2}' /var/log/syslog | sort | uniq -c | sort -rn"

# 指定產生特定 Shell 的指令
gh copilot suggest -t shell "compress all log files older than 30 days"
gh copilot suggest -t gh "list repos with no activity in 90 days"
gh copilot suggest -t git "squash last 3 commits"
```

### 企業使用情境

```bash
# DevOps 場景
gh copilot suggest "deploy the latest image to kubernetes staging namespace"
gh copilot suggest "check which pods are in CrashLoopBackOff state"

# 安全場景
gh copilot suggest "scan all repos in myorg for exposed secrets"
gh copilot suggest "list all dependabot alerts with critical severity"

# 管理場景
gh copilot suggest "list all org members who haven't committed in 90 days"
gh copilot suggest "find repos without branch protection on main"
```

## 11.2 GitHub Copilot 在 PR Review 中的應用

```bash
# 使用 Copilot 進行 PR 摘要（需啟用 Copilot for PRs）
# 在 PR 留言中使用 /summarize 指令

# 使用 CLI 觸發 Copilot Review
gh pr comment 42 --body "/copilot review"

# 使用 CLI 請求 Copilot 摘要
gh pr comment 42 --body "/copilot summarize"
```

## 11.3 AI-Powered Workflow

```yaml
# .github/workflows/ai-assisted-release-notes.yml
name: AI Release Notes

on:
  release:
    types: [created]

jobs:
  enhance-notes:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Collect PR Info
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # 取得自上次 Release 以來的所有 PR
          PREV_TAG=$(git describe --tags --abbrev=0 HEAD^ 2>/dev/null || echo "")
          if [ -n "$PREV_TAG" ]; then
            gh pr list --state merged --search "merged:>=$(git log -1 --format=%ci $PREV_TAG)" \
              --json title,number,labels,author \
              --jq '.[] | "- #\(.number) \(.title) (@\(.author.login))"' > pr-list.txt
          fi

      - name: Update Release Notes
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          TAG="${{ github.event.release.tag_name }}"
          NOTES=$(cat pr-list.txt 2>/dev/null || echo "No PRs found")
          gh release edit "$TAG" --notes "## What's Changed
          
          $NOTES
          
          **Full Changelog**: https://github.com/${{ github.repository }}/compare/...${TAG}"
```

## 11.4 Copilot 與 GitHub CLI 整合最佳實務

| 場景 | 方法 | 範例 |
|------|------|------|
| 不確定指令語法 | `gh copilot suggest` | `gh copilot suggest "archive all repos with no commits in 1 year"` |
| 看不懂別人的腳本 | `gh copilot explain` | `gh copilot explain "$(cat deploy.sh)"` |
| 建立複雜 API 查詢 | `suggest -t gh` | `gh copilot suggest -t gh "get org billing usage"` |
| 偵錯 Workflow 失敗 | 結合 `gh run view` | 先 `gh run view --log-failed`，再請 Copilot 分析 |

> **注意事項**：
> - Copilot CLI 建議的指令請務必人工確認後再執行
> - 避免在 Copilot 提示中輸入機敏資訊（API Key、密碼等）
> - 企業環境需確認 Copilot Business/Enterprise 授權已啟用

## 11.5 GitHub CLI Telemetry 管理

GitHub CLI 預設會收集匿名使用統計資料，幫助 GitHub 改善產品。企業環境可依資安政策選擇停用或記錄遙測資料。

### 停用 Telemetry

```bash
# 方法一：透過 gh config 停用
gh config set telemetry disabled

# 方法二：透過環境變數停用
export GH_TELEMETRY=false        # Unix
$env:GH_TELEMETRY = "false"      # PowerShell

# 方法三：使用通用 DO_NOT_TRACK 標準
export DO_NOT_TRACK=true          # Unix
$env:DO_NOT_TRACK = "true"        # PowerShell
```

### 記錄模式（Log Mode）

在停用前，可先使用記錄模式檢視 CLI 實際送出了哪些資料：

```bash
# 透過 gh config
gh config set telemetry log

# 透過環境變數
export GH_TELEMETRY=log           # Unix
$env:GH_TELEMETRY = "log"         # PowerShell
```

啟用記錄模式後，遙測資料會輸出到 stderr 而非實際送出，可搭配 `2>telemetry.log` 導向至檔案審查。

### 企業建議

| 環境 | 建議 | 說明 |
|------|------|------|
| 開發環境 | `telemetry log` | 先觀察再決定 |
| 正式/合規環境 | `telemetry disabled` | 確保無外部連線 |
| 受管理裝置 | 環境變數 `DO_NOT_TRACK=true` | 透過 MDM 部署設定 |

## 11.6 AI Agent 整合策略

除了 GitHub Copilot，GitHub CLI 可作為各類 AI Agent 的工具介面，在自動化工作流程中扮演橋樑角色。

### CLI 作為 AI 工具層

```text
┌─────────────────────────────────────────────────┐
│              AI Agent / LLM                     │
│  (Copilot, Claude, GPT, Internal Agent...)      │
├─────────────────────────────────────────────────┤
│              GitHub CLI (gh)                    │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌──────────┐   │
│  │ repo  │ │  pr   │ │ issue │ │ workflow │   │
│  └───────┘ └───────┘ └───────┘ └──────────┘   │
├─────────────────────────────────────────────────┤
│              GitHub API / Platform              │
└─────────────────────────────────────────────────┘
```

### 整合模式

| 模式 | 說明 | 適用場景 |
|------|------|---------|
| CLI Wrapping | AI 呼叫 `gh` 指令執行操作 | 簡單的自動化任務 |
| API Bridge | 透過 `gh api` 呼叫 REST/GraphQL | 複雜查詢與資料操作 |
| Script Generation | AI 產生 gh 腳本，人工 Review 後執行 | 批次操作、審計腳本 |
| MCP Tool Server | 將 `gh` 封裝為 MCP Tool 供 Agent 使用 | Agent 框架整合 |

### 安全原則

```bash
# 1. 使用最小權限 Token
gh auth login --scopes "repo,read:org"

# 2. AI 產生的指令一律人工確認
gh copilot suggest "close all stale issues" | tee /dev/tty

# 3. 在 CI/CD 中使用獨立 Token
env:
  GH_TOKEN: ${{ secrets.GH_AUTOMATION_TOKEN }}

# 4. 記錄所有 AI Agent 觸發的操作
gh api ... 2>&1 | tee -a /var/log/ai-agent-actions.log
```

> **企業警告**：AI Agent 透過 GitHub CLI 執行的操作等同於 Token 持有者的操作。請確保 Agent 使用的 Token 權限最小化，並記錄所有操作供事後稽核。

---

# 第 12 章：企業級最佳實務

## 12.1 Organization 管理

```bash
# 檢視 Organization 資訊
gh api orgs/myorg --jq '{login, name, plan: .plan.name, members: .plan.filled_seats}'

# 列出所有 Member
gh api orgs/myorg/members --paginate --jq '.[].login' | sort

# 列出 Outside Collaborator
gh api orgs/myorg/outside_collaborators --paginate --jq '.[].login'

# 列出 Team
gh api orgs/myorg/teams --paginate --jq '.[] | "\(.slug)\t\(.permission)\t\(.members_count)"'

# 建立 Team
gh api orgs/myorg/teams -X POST \
  -f name="platform-team" \
  -f description="Platform Engineering Team" \
  -f privacy="closed"

# 新增 Team 成員
gh api orgs/myorg/teams/platform-team/memberships/username -X PUT -f role="member"
```

## 12.2 Repository Governance

```bash
# 建立 Repo Ruleset（取代 Branch Protection）
gh api orgs/myorg/rulesets -X POST --input - << 'EOF'
{
  "name": "main-branch-rules",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/main"],
      "exclude": []
    }
  },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "required_linear_history" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 2,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": true,
        "require_last_push_approval": true,
        "required_review_thread_resolution": true
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": true,
        "required_status_checks": [
          { "context": "CI Pipeline / build-and-test" },
          { "context": "Security Scan / codeql" }
        ]
      }
    }
  ]
}
EOF
```

## 12.3 Inner Source 策略

```bash
# 設定 Internal Visibility（企業內部開源）
gh repo create myorg/shared-utils \
  --internal \
  --description "Shared utility libraries for all teams" \
  --add-readme

# 設定 Forking Policy
gh api orgs/myorg -X PATCH -f members_can_fork_private_repositories=true

# 建立 Discussion
gh api repos/myorg/shared-utils/discussions -X POST \
  -f title="RFC: Logging Standards" \
  -f body="Proposing a unified logging format..." \
  -f category_id=1
```

## 12.4 合規與稽核

```bash
# 匯出 Audit Log
gh api orgs/myorg/audit-log \
  --method GET \
  -f phrase="action:repo" \
  -f per_page=100 \
  --paginate \
  --jq '.[] | [.created_at, .actor, .action, .repo] | @csv' \
  > audit-log-$(date +%Y%m%d).csv

# 稽核 Repo 設定合規性
audit_repo() {
  local repo=$1
  echo "=== $repo ==="
  
  # 檢查 Branch Protection
  gh api "repos/$repo/branches/main/protection" --jq '.required_pull_request_reviews.required_approving_review_count' 2>/dev/null || echo "NO PROTECTION"
  
  # 檢查 CODEOWNERS
  gh api "repos/$repo/contents/.github/CODEOWNERS" --jq '.size' 2>/dev/null || echo "NO CODEOWNERS"
  
  # 檢查 Security Features
  gh api "repos/$repo" --jq '{
    secret_scanning: .security_and_analysis.secret_scanning.status,
    dependabot: .security_and_analysis.dependabot_security_updates.status
  }' 2>/dev/null
}

# 批次稽核
gh repo list myorg --limit 100 --json nameWithOwner --jq '.[].nameWithOwner' | \
  while read repo; do audit_repo "$repo"; done
```

## 12.5 Token 與權限管理

```bash
# 列出 Organization 的 Fine-grained PAT
gh api orgs/myorg/personal-access-tokens --paginate \
  --jq '.[] | "\(.id)\t\(.owner.login)\t\(.repositories_count)\t\(.permissions)"'

# 建議的 Token 權限矩陣
```

| 角色 | 建議 Token 範圍 | 用途 |
|------|----------------|------|
| 開發者 | `repo`, `read:org` | 日常開發 |
| CI/CD Bot | `repo`, `packages:write`, `actions` | 自動化部署 |
| Security Bot | `security_events`, `repo` | 安全掃描 |
| Admin | `admin:org`, `repo` | 管理作業 |

## 12.6 GitHub Projects 管理

```bash
# 列出 Organization Projects
gh api orgs/myorg/projects --jq '.[] | "\(.id)\t\(.name)\t\(.state)"'

# 使用 Project V2（GraphQL）
gh api graphql -f query='
  query($org: String!) {
    organization(login: $org) {
      projectsV2(first: 10) {
        nodes {
          title
          number
          items(first: 100) {
            totalCount
          }
        }
      }
    }
  }
' -f org="myorg" --jq '.data.organization.projectsV2.nodes[] | "\(.number)\t\(.title)\t\(.items.totalCount) items"'

# 將 Issue 加入 Project
gh api graphql -f query='
  mutation($projectId: ID!, $contentId: ID!) {
    addProjectV2ItemById(input: {projectId: $projectId, contentId: $contentId}) {
      item { id }
    }
  }
' -f projectId="PVT_xxx" -f contentId="I_xxx"
```

## 12.7 多帳戶與跨平台管理

企業開發者常需同時使用 GitHub.com（開源/社群）與 GitHub Enterprise Server（GHES，企業內部），GitHub CLI 原生支援多帳戶切換。

### 多帳戶登入

```bash
# 登入 GitHub.com
gh auth login --hostname github.com

# 登入企業 GHES
gh auth login --hostname github.company.com

# 檢視所有已登入帳戶
gh auth status

# 切換活躍帳戶
gh auth switch

# 切換至特定 Host 的帳戶
gh auth switch --hostname github.company.com
```

### 自動 Host 偵測

CLI 會根據 Git Remote 的 hostname 自動選擇對應帳戶：

```bash
# 在 GHES Repo 中操作時自動使用 GHES Token
cd /path/to/enterprise-repo    # remote → github.company.com
gh pr list                     # 自動使用 github.company.com 的 Token

# 在 GitHub.com Repo 中操作時自動使用 .com Token
cd /path/to/opensource-repo    # remote → github.com
gh pr list                     # 自動使用 github.com 的 Token
```

### 環境變數覆蓋

```bash
# 暫時指定 Host
GH_HOST=github.company.com gh repo list myorg

# 在 CI/CD 中針對不同 Host 使用不同 Token
GH_TOKEN=$GHES_TOKEN GH_HOST=github.company.com gh pr merge 42 --merge
```

### 多帳戶設定建議

| 場景 | 建議 | 說明 |
|------|------|------|
| 同時使用 .com + GHES | 兩者皆登入 | CLI 按 Remote 自動切換 |
| 個人帳號 + 企業帳號 | `gh auth switch` | 視當前工作切換 |
| CI/CD Pipeline | 環境變數 `GH_TOKEN` | 每個 Job 用獨立 Token |
| 多 GHES 實例 | 各別 `gh auth login` | 支援多個 Enterprise 同時登入 |

---

# 第 13 章：維運與監控

## 13.1 API Rate Limit 監控

```bash
# 檢查 API Rate Limit
gh api rate_limit --jq '{
  core: "\(.resources.core.remaining)/\(.resources.core.limit) (reset: \(.resources.core.reset | todate))",
  search: "\(.resources.search.remaining)/\(.resources.search.limit)",
  graphql: "\(.resources.graphql.remaining)/\(.resources.graphql.limit)"
}'
```

```powershell
# PowerShell - Rate Limit 監控
function Get-GitHubRateLimit {
    $rl = gh api rate_limit | ConvertFrom-Json
    [PSCustomObject]@{
        Core = "$($rl.resources.core.remaining)/$($rl.resources.core.limit)"
        Search = "$($rl.resources.search.remaining)/$($rl.resources.search.limit)"
        GraphQL = "$($rl.resources.graphql.remaining)/$($rl.resources.graphql.limit)"
        ResetTime = [DateTimeOffset]::FromUnixTimeSeconds($rl.resources.core.reset).LocalDateTime
    }
}
Get-GitHubRateLimit
```

## 13.2 Workflow 執行監控

```bash
# 列出最近 24 小時失敗的 Workflow Run
gh run list --status failure --json databaseId,name,conclusion,createdAt,headBranch \
  --jq '[.[] | select(.createdAt > (now - 86400 | todate))]'

# 取得 Workflow 成功率
gh run list --limit 100 --json conclusion --jq '
  group_by(.conclusion) | 
  map({conclusion: .[0].conclusion, count: length, pct: (length * 100 / ([.[] | length] | add))}) |
  sort_by(-.count)'

# 監控特定 Workflow
gh run list --workflow=ci.yml --limit 20 --json databaseId,status,conclusion,createdAt \
  --jq '.[] | "\(.databaseId)\t\(.status)\t\(.conclusion // "running")\t\(.createdAt)"'

# 即時 Watch 正在執行的 Run
gh run watch
```

## 13.3 Repo 活躍度監控

```bash
#!/bin/bash
# repo-activity-monitor.sh - Repo 活躍度儀表板

ORG="myorg"

echo "=== Repo Activity Dashboard ($(date +%Y-%m-%d)) ==="
echo ""

# Top 10 最活躍 Repo（依最近 Push 排序）
echo "📊 Top 10 Active Repos:"
gh repo list "$ORG" --limit 100 \
  --json name,pushedAt --jq '
  sort_by(.pushedAt) | reverse | .[0:10] | 
  .[] | "\(.pushedAt[:10])\t\(.name)"'

echo ""

# 超過 90 天未更新的 Repo
echo "⚠️ Inactive Repos (>90 days):"
CUTOFF=$(date -d '90 days ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -v-90d +%Y-%m-%dT%H:%M:%SZ)
gh repo list "$ORG" --limit 200 \
  --json name,pushedAt --jq "
  [.[] | select(.pushedAt < \"$CUTOFF\")] | 
  sort_by(.pushedAt) | .[] | \"\(.pushedAt[:10])\t\(.name)\""

echo ""

# 開放中的 PR 數量統計
echo "📋 Open PRs by Repo:"
for repo in $(gh repo list "$ORG" --limit 50 --json name --jq '.[].name'); do
  count=$(gh pr list -R "$ORG/$repo" --state open --json number --jq 'length' 2>/dev/null || echo 0)
  if [ "$count" -gt 0 ]; then
    echo "  $repo: $count open PRs"
  fi
done
```

## 13.4 Security Alert 監控

```bash
# 列出所有 Repo 的 Dependabot Alert 數量
for repo in $(gh repo list myorg --limit 100 --json name --jq '.[].name'); do
  count=$(gh api "repos/myorg/$repo/dependabot/alerts?state=open" --jq 'length' 2>/dev/null || echo 0)
  if [ "$count" -gt 0 ]; then
    echo "$repo: $count open alerts"
  fi
done

# 取得 Critical/High 等級的 Alert
gh api repos/myorg/my-service/dependabot/alerts \
  --jq '[.[] | select(.state=="open" and (.security_advisory.severity=="critical" or .security_advisory.severity=="high"))] |
  .[] | "\(.number)\t\(.security_advisory.severity)\t\(.dependency.package.name)\t\(.security_advisory.summary)"'
```

## 13.5 Billing 與用量

```bash
# GitHub Actions 用量
gh api orgs/myorg/settings/billing/actions \
  --jq '{
    total_minutes_used: .total_minutes_used,
    total_paid_minutes_used: .total_paid_minutes_used,
    included_minutes: .included_minutes
  }'

# Packages 用量
gh api orgs/myorg/settings/billing/packages \
  --jq '{
    total_gigabytes_bandwidth_used: .total_gigabytes_bandwidth_used,
    total_paid_gigabytes_bandwidth_used: .total_paid_gigabytes_bandwidth_used,
    included_gigabytes_bandwidth: .included_gigabytes_bandwidth
  }'

# Storage 用量
gh api orgs/myorg/settings/billing/shared-storage \
  --jq '{
    days_left: .days_left_in_billing_cycle,
    estimated_paid_storage: .estimated_paid_storage_for_month,
    estimated_storage: .estimated_storage_for_month
  }'
```

## 13.6 通知管理

```bash
# 列出未讀通知
gh api notifications --jq '.[] | "\(.id)\t\(.reason)\t\(.subject.type)\t\(.subject.title)"'

# 標記全部已讀
gh api notifications -X PUT -f read=true -f last_read_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# 僅列出 CI 失敗通知
gh api notifications --jq '.[] | select(.reason=="ci_activity") | "\(.subject.title)"'
```

---

# 第 14 章：實戰案例

## 14.1 案例一：微服務團隊快速啟動

**場景**：新專案需要建立 5 個微服務 Repo，統一設定 Branch Protection、CI/CD、Team 權限。

```bash
#!/bin/bash
# bootstrap-microservices.sh

ORG="myorg"
TEMPLATE="$ORG/spring-boot-template"
SERVICES=("user-service" "order-service" "payment-service" "notification-service" "gateway-service")

for svc in "${SERVICES[@]}"; do
  echo "🚀 Creating $svc..."
  
  # 建立 Repo
  gh repo create "$ORG/$svc" --template "$TEMPLATE" --private
  
  # 等待 Template 複製完成
  sleep 3
  
  # 設定 Branch Protection
  gh api "repos/$ORG/$svc/branches/main/protection" -X PUT --input - << 'EOF'
{
  "required_status_checks": {"strict": true, "contexts": ["CI Pipeline / build-and-test"]},
  "enforce_admins": true,
  "required_pull_request_reviews": {"required_approving_review_count": 2, "dismiss_stale_reviews": true, "require_code_owner_reviews": true},
  "restrictions": null
}
EOF
  
  # 設定 Team 權限
  gh api "orgs/$ORG/teams/backend-team/repos/$ORG/$svc" -X PUT -f permission="push"
  gh api "orgs/$ORG/teams/devops-team/repos/$ORG/$svc" -X PUT -f permission="admin"
  
  # 設定 Secret
  gh secret set SONAR_TOKEN -R "$ORG/$svc" --body "$SONAR_TOKEN"
  
  echo "✅ $svc created and configured"
done

echo "🏁 All microservices bootstrapped!"
```

**效果**：原本需要 2 小時手動設定的工作，現在 5 分鐘即可完成。

## 14.2 案例二：Release 流程自動化

**場景**：團隊每兩週 Release，流程包括版本號更新、Changelog 產生、Release Notes、Asset 上傳。

```bash
#!/bin/bash
# bi-weekly-release.sh

set -euo pipefail

# 計算版本號
CURRENT=$(gh release list --limit 1 --json tagName --jq '.[0].tagName' | sed 's/^v//')
MAJOR=$(echo "$CURRENT" | cut -d. -f1)
MINOR=$(echo "$CURRENT" | cut -d. -f2)
PATCH=$(echo "$CURRENT" | cut -d. -f3)
NEW_VERSION="$MAJOR.$((MINOR + 1)).0"
TAG="v$NEW_VERSION"

echo "📦 Releasing $TAG (previous: v$CURRENT)"

# 確保 main 是最新的
git checkout main && git pull

# Build
mvn versions:set -DnewVersion="$NEW_VERSION" -DgenerateBackupPoms=false
mvn clean package -DskipTests -B

# 建立 Tag
git add pom.xml
git commit -m "chore: release $TAG"
git tag -a "$TAG" -m "Release $TAG"
git push origin main --tags

# 建立 GitHub Release
gh release create "$TAG" \
  --title "Release $NEW_VERSION" \
  --generate-notes \
  --latest \
  ./target/*.jar

echo "✅ Released $TAG"
echo "📋 Release URL: $(gh release view $TAG --json url --jq '.url')"
```

## 14.3 案例三：Security 合規自動化

**場景**：每週產出安全合規報告，確保所有 Repo 符合企業安全基線。

```bash
#!/bin/bash
# security-compliance-report.sh

ORG="myorg"
DATE=$(date +%Y-%m-%d)
REPORT="security-report-$DATE.md"

cat > "$REPORT" << EOF
# Security Compliance Report
**Date**: $DATE
**Organization**: $ORG

## Summary
EOF

total=0; compliant=0; issues=0

for repo in $(gh repo list "$ORG" --json name,isArchived --jq '.[] | select(.isArchived==false) | .name'); do
  total=$((total + 1))
  repo_issues=0
  
  # Check Branch Protection
  if ! gh api "repos/$ORG/$repo/branches/main/protection" &>/dev/null; then
    repo_issues=$((repo_issues + 1))
  fi
  
  # Check Dependabot Alerts
  alerts=$(gh api "repos/$ORG/$repo/dependabot/alerts?state=open&severity=critical,high" --jq 'length' 2>/dev/null || echo 0)
  if [ "$alerts" -gt 0 ]; then
    repo_issues=$((repo_issues + 1))
  fi
  
  if [ "$repo_issues" -eq 0 ]; then
    compliant=$((compliant + 1))
  else
    issues=$((issues + repo_issues))
    echo "- ⚠️ **$repo**: $repo_issues issue(s)" >> "$REPORT"
  fi
done

# 寫入摘要
sed -i "/## Summary/a\\
| Metric | Value |\\
|--------|-------|\\
| Total Repos | $total |\\
| Compliant | $compliant ($((compliant * 100 / total))%) |\\
| Issues Found | $issues |" "$REPORT"

echo "✅ Report saved: $REPORT"
```

## 14.4 案例四：PR Review 流程優化

**場景**：大型團隊 PR Review 效率低，導入自動化指派與追蹤。

```bash
# 自動 Review 指派（依 CODEOWNERS）
# 搭配 .github/CODEOWNERS 檔案自動指派

# 追蹤 PR Review 週期
gh pr list --state merged --limit 50 \
  --json number,title,createdAt,mergedAt,reviews \
  --jq '.[] | {
    number,
    title: .title[:50],
    created: .createdAt[:10],
    merged: .mergedAt[:10],
    review_count: (.reviews | length),
    cycle_hours: ((.mergedAt | fromdateiso8601) - (.createdAt | fromdateiso8601)) / 3600 | floor
  }' | jq -s 'sort_by(-.cycle_hours)'

# PR 瓶頸分析 - 找出等待最久的 PR
gh pr list --state open --json number,title,createdAt,reviewRequests,reviews \
  --jq 'sort_by(.createdAt) | .[] | {
    number,
    title: .title[:40],
    waiting_days: ((now - (.createdAt | fromdateiso8601)) / 86400 | floor),
    pending_reviewers: [.reviewRequests[].login] | join(","),
    reviews_done: (.reviews | length)
  }'
```

## 14.5 案例五：跨 Repo 標準化

**場景**：確保組織中所有 Repo 都有標準的 Issue Template、PR Template、CI Workflow。

```bash
#!/bin/bash
# standardize-repos.sh

ORG="myorg"

# 標準檔案來源
TEMPLATE_REPO="$ORG/.github"

for repo in $(gh repo list "$ORG" --json name,isArchived --jq '.[] | select(.isArchived==false) | .name'); do
  echo "📋 Standardizing $repo..."
  
  # 檢查是否缺少 Issue Template
  if ! gh api "repos/$ORG/$repo/contents/.github/ISSUE_TEMPLATE/bug_report.yml" &>/dev/null; then
    echo "  ⚠️ Missing Issue Template"
    # 從 Template Repo 複製
    content=$(gh api "repos/$TEMPLATE_REPO/contents/.github/ISSUE_TEMPLATE/bug_report.yml" --jq '.content')
    gh api "repos/$ORG/$repo/contents/.github/ISSUE_TEMPLATE/bug_report.yml" \
      -X PUT -f message="chore: add bug report template" -f content="$content"
  fi
  
  # 檢查是否缺少 PR Template
  if ! gh api "repos/$ORG/$repo/contents/.github/PULL_REQUEST_TEMPLATE.md" &>/dev/null; then
    echo "  ⚠️ Missing PR Template"
  fi
  
  # 檢查是否缺少 CI Workflow
  if ! gh api "repos/$ORG/$repo/contents/.github/workflows/ci.yml" &>/dev/null; then
    echo "  ⚠️ Missing CI Workflow"
  fi
done
```

> **案例總結**：
> - 自動化是 GitHub CLI 的最大價值，減少重複人工操作
> - 將常用腳本納入版本控制，作為團隊共享工具
> - 定期執行稽核與合規腳本，確保標準一致性
> - 搭配 `cron` 或 GitHub Actions `schedule` 實現定期自動執行

---

# 第 15 章：Troubleshooting

## 15.1 常見錯誤與解決方案

### 認證錯誤

| 錯誤訊息 | 原因 | 解決方案 |
|----------|------|---------|
| `authentication required` | 未登入或 Token 過期 | `gh auth login` |
| `HTTP 401` | Token 權限不足 | `gh auth refresh -s repo,read:org` |
| `HTTP 403 SSO enforcement` | 需要 SSO 授權 | `gh auth refresh -s admin:org` |
| `SAML SSO required` | Token 未授權 SSO Org | 到 GitHub Settings > Developer settings > Personal access tokens 點選 **Authorize** |
| `ssh: connect to host github.com port 22: Connection timed out` | SSH 被防火牆阻擋 | 改用 `~/.ssh/config` 設定 Port 443 |

**SSH over HTTPS Port 443**：

```bash
# ~/.ssh/config
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

### Proxy 問題

```bash
# 設定 Proxy
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,.company.com

# PowerShell
$env:HTTP_PROXY = "http://proxy.company.com:8080"
$env:HTTPS_PROXY = "http://proxy.company.com:8080"

# Git Proxy 設定
git config --global http.proxy http://proxy.company.com:8080
git config --global https.proxy http://proxy.company.com:8080

# 驗證連線
gh api rate_limit
```

### API Rate Limit

```bash
# 檢查剩餘額度
gh api rate_limit --jq '.resources.core | "Remaining: \(.remaining)/\(.limit), Reset: \(.reset | todate)"'

# 解決方案：
# 1. 使用 --cache 減少 API 呼叫
gh api repos/myorg/my-service --cache 1h

# 2. 使用 GraphQL 合併多次查詢
gh api graphql -f query='query {
  repo1: repository(owner:"myorg", name:"svc1") { name pushedAt }
  repo2: repository(owner:"myorg", name:"svc2") { name pushedAt }
}'

# 3. 使用 Conditional Request（ETag）
gh api repos/myorg/my-service -i 2>&1 | grep -i etag
```

### Workflow 執行問題

| 症狀 | 診斷指令 | 常見原因 |
|------|---------|---------|
| Workflow 不觸發 | `gh workflow list` | Workflow 被 disable |
| Job 一直 Queued | `gh run view --json jobs` | Runner 不足或 Label 不匹配 |
| Step 失敗 | `gh run view --log-failed` | 指令錯誤或環境問題 |
| Secret 為空 | `gh secret list` | Secret 名稱拼錯或環境不對 |

```bash
# 診斷 Workflow 問題
gh run view 12345 --log-failed

# 重新執行失敗的 Job
gh run rerun 12345 --failed

# 啟用 Debug Log
gh secret set ACTIONS_STEP_DEBUG --body "true"
gh secret set ACTIONS_RUNNER_DEBUG --body "true"
```

## 15.2 CLI 升級與相容性

```bash
# 檢查版本
gh version

# 升級（各平台）
# Windows (winget)
winget upgrade GitHub.cli

# macOS (Homebrew)
brew upgrade gh

# Linux (apt)
sudo apt update && sudo apt upgrade gh

# 檢查 Extension 相容性
gh extension list
gh extension upgrade --all --dry-run
```

## 15.3 Debug 模式

```bash
# 啟用 Debug 輸出
GH_DEBUG=1 gh api repos/myorg/my-service

# 啟用 HTTP Trace
GH_DEBUG=api gh pr list

# PowerShell
$env:GH_DEBUG = "1"
gh api repos/myorg/my-service
```

---

# 第 16 章：最佳實務總覽

## 16.1 日常開發

| 實務 | 說明 |
|------|------|
| 使用 `gh pr create --draft` | 先建立 Draft PR，完成後再 `gh pr ready` |
| 使用 `--auto` merge | `gh pr merge --squash --delete-branch --auto` |
| 使用 Alias | 常用指令設定 Alias，提升效率 |
| 使用 `gh pr status` | 快速掌握自己的 PR 狀態 |
| 使用 `gh pr checks --watch` | 即時監控 CI 狀態 |

## 16.2 團隊協作

| 實務 | 說明 |
|------|------|
| CODEOWNERS | 依目錄自動指派 Reviewer |
| PR Template | 標準化 PR 描述格式 |
| Issue Template | 標準化 Bug/Feature 格式 |
| Conventional Commits | 統一 Commit 格式，便於自動產生 Changelog |
| Branch Protection | 至少 2 人 Approve、CI 通過才能 Merge |

## 16.3 安全

| 實務 | 說明 |
|------|------|
| 啟用 Secret Scanning | 防止憑證洩漏 |
| 啟用 Dependabot | 自動更新有漏洞的依賴 |
| 啟用 CodeQL | 自動偵測程式碼安全問題 |
| 使用 Fine-grained PAT | 最小權限原則 |
| 定期輪換 Token | 每 90 天更換 Token |
| Signed Commits | 驗證 Commit 來源 |

## 16.4 CI/CD

| 實務 | 說明 |
|------|------|
| Concurrency Control | 取消同分支的舊 Run |
| Timeout | 設定 Job timeout，避免無限等待 |
| Cache | 快取 Maven/npm 依賴，加速建置 |
| Environment | 使用 Environment 分離 Staging/Production |
| Approval Gate | Production 部署需審核 |
| OIDC | 使用 OIDC 取代 Long-lived Credential |

## 16.5 自動化

| 實務 | 說明 |
|------|------|
| 腳本納入版本控制 | 存放在 `scripts/` 目錄 |
| 錯誤處理 | `set -euo pipefail`（Bash） |
| Dry-run 模式 | 關鍵操作提供 `--dry-run` |
| Log 輸出 | 記錄操作時間與結果 |
| 定期稽核 | 週期性執行合規檢查腳本 |

---

# 第 17 章：附錄

## 17.1 Cheat Sheet

### 認證

```bash
gh auth login                       # 登入
gh auth logout                      # 登出
gh auth status                      # 狀態
gh auth refresh -s repo,read:org    # 更新權限
gh auth token                       # 取得 Token
gh auth setup-git                   # 設定 Git 認證
```

### Repository

```bash
gh repo create ORG/NAME --private          # 建立
gh repo clone ORG/NAME                     # Clone
gh repo fork UPSTREAM/NAME                 # Fork
gh repo list ORG --limit 50               # 列出
gh repo view ORG/NAME                      # 檢視
gh repo edit --description "desc"          # 編輯
gh repo delete ORG/NAME --yes              # 刪除
gh repo archive ORG/NAME                   # 封存
gh repo sync                               # 同步 Fork
```

### Pull Request

```bash
gh pr create --draft                           # 建立 Draft PR
gh pr create --title "feat: X" --base main     # 建立 PR
gh pr list --state open                        # 列出
gh pr view 42                                  # 檢視
gh pr status                                   # 狀態
gh pr diff 42                                  # 差異
gh pr review 42 --approve                      # 核准
gh pr merge 42 --squash --delete-branch        # 合併
gh pr merge 42 --auto --squash                 # 自動合併
gh pr checkout 42                              # 切換分支
gh pr ready 42                                 # 標記 Ready
gh pr checks 42 --watch                        # 監控 CI
```

### Issue

```bash
gh issue create --title "Bug: X" --label bug   # 建立
gh issue list --state open                     # 列出
gh issue view 123                              # 檢視
gh issue close 123                             # 關閉
gh issue develop 123 --checkout                # 建立分支
gh issue comment 123 --body "Fixed"            # 留言
```

### Release

```bash
gh release create v1.0.0 --generate-notes      # 建立
gh release list                                 # 列出
gh release download --pattern "*.jar"           # 下載
gh release upload v1.0.0 app.jar               # 上傳
```

### Workflow & Run

```bash
gh workflow list                               # 列出
gh workflow run ci.yml                         # 觸發
gh workflow run deploy.yml -f env=staging      # 帶參數觸發
gh run list --status failure                   # 列出失敗
gh run view 12345 --log-failed                 # 檢視 Log
gh run watch                                   # 即時監控
gh run rerun 12345 --failed                    # 重跑失敗
gh run download 12345 -n artifact-name         # 下載 Artifact
```

### API

```bash
gh api repos/{owner}/{repo}                    # GET
gh api repos/{owner}/{repo}/issues -f title=X  # POST
gh api repos/{owner}/{repo} -X PATCH -f desc=X # PATCH
gh api graphql -f query='{ viewer { login } }' # GraphQL
gh api rate_limit                              # Rate Limit
```

### Secret & Variable

```bash
gh secret set KEY --body "value"               # 設定 Secret
gh secret list                                 # 列出 Secret
gh secret set KEY --env production --body "v"   # Environment Secret
gh variable set KEY --body "value"             # 設定 Variable
```

### Alias & Extension

```bash
gh alias set prc 'pr create --draft'           # 設定 Alias
gh alias list                                  # 列出 Alias
gh extension install github/gh-copilot         # 安裝 Extension
gh extension list                              # 列出 Extension
gh extension upgrade --all                     # 更新全部
```

## 17.2 環境變數

| 變數 | 說明 | 範例 |
|------|------|------|
| `GH_TOKEN` | 認證 Token | `export GH_TOKEN=ghp_xxx` |
| `GH_ENTERPRISE_TOKEN` | Enterprise Token | `export GH_ENTERPRISE_TOKEN=ghp_xxx` |
| `GH_HOST` | GitHub 主機 | `export GH_HOST=github.company.com` |
| `GH_REPO` | 預設 Repo | `export GH_REPO=myorg/my-service` |
| `GH_EDITOR` | 編輯器 | `export GH_EDITOR=code` |
| `GH_BROWSER` | 瀏覽器 | `export GH_BROWSER=firefox` |
| `GH_DEBUG` | Debug 模式 | `export GH_DEBUG=1` |
| `GH_PAGER` | 分頁程式 | `export GH_PAGER=less` |
| `NO_COLOR` | 停用色彩 | `export NO_COLOR=1` |
| `HTTP_PROXY` | HTTP Proxy | `export HTTP_PROXY=http://proxy:8080` |
| `HTTPS_PROXY` | HTTPS Proxy | `export HTTPS_PROXY=http://proxy:8080` |

## 17.3 設定檔位置

| 平台 | 設定檔路徑 |
|------|-----------|
| Windows | `%APPDATA%\GitHub CLI\config.yml` |
| macOS | `~/.config/gh/config.yml` |
| Linux | `~/.config/gh/config.yml` |

```yaml
# config.yml 範例
git_protocol: ssh
editor: code
prompt: enabled
pager: less
aliases:
  prc: pr create --draft
  prs: pr status
  prm: pr merge --squash --delete-branch
  co: pr checkout
```

## 17.4 常用 jq 語法

```bash
# 基本過濾
--jq '.[].name'                        # 取得陣列中每個元素的 name
--jq '.[] | select(.state=="open")'    # 過濾條件
--jq 'length'                          # 計算數量
--jq 'sort_by(.created_at) | reverse'  # 排序

# 欄位重組
--jq '.[] | {number, title, author: .user.login}'

# CSV 輸出
--jq '.[] | [.number, .title, .state] | @csv'

# TSV 輸出
--jq '.[] | [.number, .title] | @tsv'

# 群組統計
--jq 'group_by(.state) | map({state: .[0].state, count: length})'

# 條件計算
--jq '[.[] | select(.state=="open")] | length'
```

## 17.5 FAQ

**Q1：gh 和 git 有什麼關係？**

`gh` 是 GitHub CLI，專門與 GitHub 平台互動（PR、Issue、Actions 等）。`git` 是版本控制工具。兩者互補，`gh` 不取代 `git`。

**Q2：可以在企業內網使用 gh 嗎？**

可以。設定 `GH_HOST` 指向 GitHub Enterprise Server，並設定 Proxy（`HTTP_PROXY`/`HTTPS_PROXY`）。

**Q3：如何在 CI/CD 中使用 gh？**

在 GitHub Actions 中，`gh` 已預先安裝。使用 `GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}` 環境變數即可認證。

**Q4：Token 需要哪些權限？**

依使用場景而定。日常開發需要 `repo` 和 `read:org`；管理作業需要 `admin:org`。建議使用 Fine-grained PAT，只給予必要權限。

**Q5：如何處理大量 API 呼叫的 Rate Limit？**

使用 `--cache` 快取回應、使用 GraphQL 合併查詢、使用 `--paginate` 避免重複請求、錯開執行時間。

**Q6：gh 支援哪些 Shell？**

支援 Bash、Zsh、Fish、PowerShell。Alias 中使用 `--shell` 旗標可執行 Shell 指令。

---

# ✅ 學習檢核清單

## 基礎篇（Chapter 1-3）

- [ ] 了解 GitHub CLI 與 Git CLI 的差異
- [ ] 安裝 `gh` 並完成版本確認（`gh version`）
- [ ] 完成 `gh auth login` 認證
- [ ] 設定 SSH Key 並驗證連線（`ssh -T git@github.com`）
- [ ] 了解 Token 類型（Classic PAT vs Fine-grained PAT）
- [ ] 設定企業 Proxy（如適用）

## 核心操作篇（Chapter 4-6）

- [ ] 使用 `gh repo create` 建立 Repository
- [ ] 使用 `gh repo clone` Clone Repository
- [ ] 了解 Git Flow 與 Trunk Based Development
- [ ] 使用 Conventional Commits 格式
- [ ] 建立 README.md 標準化範本
- [ ] 設定 `.github/CODEOWNERS`

## 指令篇（Chapter 7）

- [ ] 熟悉 `gh pr` 完整流程（create → review → merge）
- [ ] 熟悉 `gh issue` 管理流程
- [ ] 使用 `gh release create --generate-notes` 建立 Release
- [ ] 使用 `gh api` 呼叫 REST/GraphQL API
- [ ] 設定至少 3 個常用 Alias
- [ ] 安裝至少 1 個 Extension（推薦 `gh-copilot`）

## CI/CD 篇（Chapter 8）

- [ ] 建立基本 CI Workflow（build + test）
- [ ] 了解 Matrix Build 用法
- [ ] 設定 Cache 加速建置
- [ ] 設定 GitHub Secret 與 Variable
- [ ] 建立 CD Workflow（含 Environment 審核）
- [ ] 了解 `concurrency` 設定

## 安全篇（Chapter 9）

- [ ] 啟用 Secret Scanning 與 Push Protection
- [ ] 設定 Dependabot 自動更新
- [ ] 設定 CodeQL 掃描
- [ ] 建立 `SECURITY.md` 安全政策
- [ ] 設定 Branch Protection（至少 2 人 Approve）
- [ ] 了解 SBOM 與 Supply Chain Security

## 自動化篇（Chapter 10）

- [ ] 撰寫 Repo 初始化腳本
- [ ] 撰寫 Branch Protection 批次設定腳本
- [ ] 撰寫 Release 自動化腳本
- [ ] 使用 `gh api --jq` 產生結構化報告

## 進階篇（Chapter 11-14）

- [ ] 安裝並使用 GitHub Copilot CLI
- [ ] 設定 Organization Ruleset
- [ ] 執行 Repo 健康度檢查腳本
- [ ] 產出安全合規報告
- [ ] 監控 API Rate Limit 與 Billing 用量

## 維運篇（Chapter 15-17）

- [ ] 了解常見錯誤的排除方式
- [ ] 設定 Debug 模式（`GH_DEBUG=1`）
- [ ] 掌握 Cheat Sheet 中的核心指令
- [ ] 熟悉 `--json` + `--jq` 輸出格式化
- [ ] 將本手冊作為團隊 Onboarding 教材

---

> **版本紀錄**
>
> | 版本 | 日期 | 變更說明 |
> |------|------|---------|
> | 1.0 | 2026-05-08 | 初版發行，涵蓋 17 章 |
> | 1.1 | 2026-05-22 | Ch7 新增 7.10-7.22（browse/codespace/gist/project/search/cache/attestation/ruleset/label/variable/secret/status/config）；Ch11 新增 Telemetry 管理與 AI Agent 整合策略；Ch12 新增多帳戶與跨平台管理；Ch1 能力表擴充；目錄對齊修正；Markdown 格式修復 |
