+++
date = '2025-10-21T17:47:32+08:00'
draft = false
title = 'Jenkins CI_CD 教學手冊'
tags = ['教學','工具' ,'Jenkins']
categories = ['技術']
author = 'Eric Cheng'
summary = 'Jenkins CI_CD 教學手冊，作為新進開發人員的學習指引'
+++

# Jenkins CI/CD 教學手冊

## 📋 目錄 (Table of Contents)

### 第一部分：基礎概念與環境建置

1. [Jenkins 簡介與核心概念](#第1章-jenkins-簡介與核心概念)
2. [環境安裝與基本設定](#第2章-環境安裝與基本設定)
3. [Jenkins 介面導覽](#第3章-jenkins-介面導覽)
4. [Plugin 管理與基礎設定](#第4章-plugin-管理與基礎設定)

### 第二部分：Job 建立與管理

5. [Freestyle Project 入門](#第5章-freestyle-project-入門)
6. [憑證與密碼管理](#第6章-憑證與密碼管理)
7. [Git 整合與版本控制](#第7章-git-整合與版本控制)
8. [Maven 建置整合](#第8章-maven-建置整合)

### 第三部分：Pipeline 進階應用

9. [Pipeline 基礎與 Declarative Syntax](#第9章-pipeline-基礎與-declarative-syntax)
10. [Jenkinsfile 結構深度分析](#第10章-jenkinsfile-結構深度分析)
11. [測試報告與程式碼覆蓋率整合](#第11章-測試報告與程式碼覆蓋率整合)
12. [靜態程式碼分析與品質檢查](#第12章-靜態程式碼分析與品質檢查)

### 第四部分：進階功能與故障排除

13. [Pipeline 故障排除與除錯技巧](#第13章-pipeline-故障排除與除錯技巧)
14. [部署策略與環境管理](#第14章-部署策略與環境管理)
15. [監控、通知與效能優化](#第15章-監控通知與效能優化)

### 第五部分：企業級應用與最佳實務

16. [企業級 CI/CD 架構設計](#第16章-企業級-cicd-架構設計)
17. [容器化與雲端整合](#第17章-容器化與雲端整合)
18. [DevOps 文化與實務](#第18章-devops-文化與實務)
19. [實務案例研究](#第19章-實務案例研究)

### 附錄

- [附錄 A：常用指令參考](#附錄-a常用指令參考)
  - [A.1 Jenkins CLI 指令](#a1-jenkins-cli-指令)
  - [A.2 Git 整合指令](#a2-git-整合指令)
  - [A.3 Docker 容器指令](#a3-docker-容器指令)
  - [A.4 Kubernetes 部署指令](#a4-kubernetes-部署指令)
- [附錄 B：配置範例](#附錄-b配置範例)
  - [B.1 Jenkins 系統配置範例](#b1-jenkins-系統配置範例)
  - [B.2 多環境配置範例](#b2-多環境配置範例)
  - [B.3 安全配置範例](#b3-安全配置範例)
- [附錄 C：故障排除指南](#附錄-c故障排除指南)
  - [C.1 常見 Jenkins 問題](#c1-常見-jenkins-問題)
  - [C.2 網路連接問題](#c2-網路連接問題)
  - [C.3 Docker 建置問題](#c3-docker-建置問題)
  - [C.4 性能調優指南](#c4-性能調優指南)
- [附錄 D：最佳實踐清單](#附錄-d最佳實踐清單)
  - [D.1 安全最佳實踐](#d1-安全最佳實踐)
  - [D.2 效能最佳實踐](#d2-效能最佳實踐)
  - [D.3 維護最佳實踐](#d3-維護最佳實踐)
- [附錄 E：工具和資源](#附錄-e工具和資源)
  - [E.1 推薦工具清單](#e1-推薦工具清單)
  - [E.2 學習資源](#e2-學習資源)
- [附錄 F：認證考試對照](#附錄-f認證考試對照)
  - [F.1 Jenkins 認證考試對應](#f1-jenkins-認證考試對應)
  - [F.2 相關技術認證](#f2-相關技術認證)
- [附錄 G：版本更新歷史](#附錄-g版本更新歷史)

---

## 📖 教學手冊說明

### 🎯 學習目標

本教學手冊旨在幫助新進 Java 開發者從零開始學習 Jenkins 與 CI/CD 自動化流程，涵蓋從基礎概念到實務應用的完整知識體系。

### 👥 目標讀者

- 新進 Java 開發者
- 未接觸過 Jenkins 的技術人員
- 需要建立 CI/CD Pipeline 的開發團隊

### 🛠️ 技術前提

- Java 17+ 基礎知識
- Maven 專案管理經驗
- Git 版本控制基礎
- JUnit 測試框架了解

### 📚 認證對應

本手冊內容對應以下認證考試：

- Jenkins Certified Engineer (JCE)
- Cloudbees Jenkins Platform Engineer
- DevOps Foundation 相關知識點

---

## 第1章 Jenkins 簡介與核心概念

### 🎯 學習目標

- 理解 Jenkins 在 DevOps 中的角色
- 掌握 Jenkins 核心架構概念
- 了解 CI/CD 流程設計原則

### 📚 核心概念

#### 1.1 什麼是 Jenkins？

Jenkins 是一個開源的自動化伺服器，用於實現持續整合（Continuous Integration, CI）和持續部署（Continuous Deployment, CD）。它能夠：

- 自動化建置、測試和部署流程
- 整合各種開發工具和服務
- 提供豐富的插件生態系統
- 支援分散式建置架構

#### 1.2 Jenkins 核心架構

```mermaid
graph TB
    A[Jenkins Master/Controller] --> B[Agent Node 1]
    A --> C[Agent Node 2]
    A --> D[Agent Node 3]
    
    subgraph "Jenkins Master"
        E[Web UI]
        F[Job Scheduler]
        G[Plugin Manager]
        H[Build Queue]
    end
    
    subgraph "Agent Node"
        I[Executor 1]
        J[Executor 2]
        K[Workspace]
    end
    
    B --> I
    B --> J
    B --> K
```

**核心組件說明：**

1. **Master/Controller（主控節點）**
   - 負責管理整個 Jenkins 環境
   - 處理 Web UI 和 API 請求
   - 管理 Job 排程和配置
   - 協調 Agent 節點工作分配

2. **Agent/Node（代理節點）**
   - 執行實際的建置工作
   - 可以是物理機器、虛擬機或容器
   - 提供特定的執行環境（如不同 OS、工具版本）

3. **Executor（執行器）**
   - Agent 上的工作執行單位
   - 決定可同時執行的 Job 數量
   - 每個 Executor 獨立執行一個 Job

4. **Workspace（工作空間）**
   - Job 執行時的文件存放區域
   - 包含原始碼、建置產物等
   - 可設定自動清理政策

5. **Job/Project（工作/專案）**
   - Jenkins 中的基本工作單位
   - 定義了一系列的建置步驟
   - 可以是 Freestyle、Pipeline 等類型

6. **Build Queue（建置佇列）**
   - 等待執行的 Job 排隊機制
   - 根據優先級和資源可用性分配

#### 1.3 CI/CD 流程設計

```mermaid
flowchart LR
    A[程式碼提交] --> B[觸發建置]
    B --> C[原始碼拉取]
    C --> D[編譯]
    D --> E[單元測試]
    E --> F[程式碼品質檢查]
    F --> G[整合測試]
    G --> H[打包]
    H --> I[部署到測試環境]
    I --> J[自動化測試]
    J --> K[部署到生產環境]
    
    subgraph "持續整合 (CI)"
        C
        D
        E
        F
    end
    
    subgraph "持續部署 (CD)"
        G
        H
        I
        J
        K
    end
```

**流程階段說明：**

1. **持續整合 (CI) 階段**
   - **原始碼拉取**：從版本控制系統獲取最新程式碼
   - **編譯**：將原始碼編譯成可執行文件
   - **單元測試**：執行自動化單元測試
   - **程式碼品質檢查**：靜態程式碼分析、格式檢查

2. **持續部署 (CD) 階段**
   - **整合測試**：跨模組測試
   - **打包**：建立部署包（如 JAR、WAR）
   - **環境部署**：部署到各個環境
   - **自動化測試**：端對端測試、效能測試

#### 1.4 Jenkins Job 類型比較

| 類型 | 適用場景 | 優點 | 缺點 |
|------|----------|------|------|
| **Freestyle** | 簡單建置任務 | 易於設定、視覺化配置 | 不易版本控制、複雜邏輯困難 |
| **Pipeline** | 複雜 CI/CD 流程 | 程式碼化、版本控制、強大邏輯 | 學習曲線較陡 |
| **Multibranch** | 多分支開發 | 自動探測分支、獨立建置 | 設定較複雜 |
| **Organization Folder** | 多專案管理 | 自動探測專案、統一管理 | 需要特定目錄結構 |

### 💡 實務案例

#### 案例：Java Web 應用的典型 CI/CD 流程

假設我們有一個 Spring Boot 專案，典型的 Jenkins Pipeline 會包含：

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/company/java-web-app.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        
        stage('Package') {
            steps {
                sh 'mvn package'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker build -t myapp .'
                sh 'docker run -d -p 8080:8080 myapp'
            }
        }
    }
}
```

### ⚠️ 注意事項

1. **資源規劃**：根據專案規模規劃 Master/Agent 資源
2. **安全考量**：設定適當的權限和憑證管理
3. **備份策略**：定期備份 Jenkins 設定和工作空間
4. **監控告警**：建立建置失敗和系統異常的通知機制

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Jenkins 基礎架構 | Master/Agent 概念、Executor、Queue |
| CI/CD 概念 | 持續整合流程、自動化測試 |
| Job 類型選擇 | Freestyle vs Pipeline 比較 |

---

## 第2章 環境安裝與基本設定

### 🎯 學習目標

- 在 Windows 環境中安裝 Jenkins
- 完成基本系統設定
- 了解多種安裝方式的優缺點

### 📚 核心概念

#### 2.1 Jenkins 安裝方式比較

| 安裝方式 | 優點 | 缺點 | 適用場景 |
|----------|------|------|----------|
| **WAR 文件** | 簡單快速、跨平台 | 需手動管理、無服務整合 | 開發測試、快速體驗 |
| **Windows Service** | 系統整合、自動啟動 | 僅限 Windows | Windows 生產環境 |
| **Docker** | 環境隔離、版本管理 | 需 Docker 知識 | 容器化環境 |
| **雲端服務** | 免維護、高可用 | 成本較高、客製化限制 | 企業級應用 |

#### 2.2 系統需求

**最低需求：**

- **RAM**: 256MB（建議 4GB+）
- **磁碟空間**: 1GB（建議 50GB+）
- **Java**: JDK 11 或更高版本
- **瀏覽器**: Chrome、Firefox、Safari、Edge

**建議配置：**

- **CPU**: 4 核心以上
- **RAM**: 8GB 以上
- **磁碟**: SSD 硬碟
- **網路**: 穩定的網際網路連線

### 🛠️ 安裝步驟

#### 方法一：WAR 文件安裝（推薦新手）

**步驟 1：安裝 Java JDK**

```powershell
# 檢查 Java 版本
java -version

# 如果沒有安裝，請下載 OpenJDK 或 Oracle JDK 17+
# 下載地址：https://adoptium.net/
```

**步驟 2：下載 Jenkins WAR**

```powershell
# 建立 Jenkins 目錄
mkdir C:\Jenkins
cd C:\Jenkins

# 下載最新穩定版本
Invoke-WebRequest -Uri "https://get.jenkins.io/war-stable/latest/jenkins.war" -OutFile "jenkins.war"
```

**步驟 3：啟動 Jenkins**

```powershell
# 啟動 Jenkins（指定埠號和主目錄）
java -jar jenkins.war --httpPort=8080 --prefix=/jenkins

# 或使用自訂設定
$env:JENKINS_HOME="C:\Jenkins\data"
java -Xmx2g -jar jenkins.war --httpPort=8080
```

**步驟 4：首次設定**

1. 開啟瀏覽器，前往 `http://localhost:8080`
2. 輸入初始管理員密碼：

```powershell
# 查看初始密碼
Get-Content "C:\Users\%USERNAME%\.jenkins\secrets\initialAdminPassword"
```

3. 選擇「安裝建議的插件」
4. 建立第一個管理員用戶
5. 設定 Jenkins URL

#### 方法二：Docker 安裝（推薦開發環境）

**步驟 1：安裝 Docker Desktop**

- 下載：<https://www.docker.com/products/docker-desktop>

**步驟 2：執行 Jenkins 容器**

```powershell
# 建立 Jenkins 數據目錄
mkdir C:\Jenkins\data

# 執行 Jenkins 容器
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v C:\Jenkins\data:/var/jenkins_home \
  jenkins/jenkins:lts

# 查看初始密碼
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

**步驟 3：進階 Docker 設定**

建立 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    restart: unless-stopped
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - JAVA_OPTS=-Xmx2g
      - JENKINS_OPTS=--prefix=/jenkins

volumes:
  jenkins_home:
```

啟動：

```powershell
docker-compose up -d
```

#### 方法三：Windows Service 安裝

**步驟 1：下載 Windows 安裝程式**

- 下載：<https://www.jenkins.io/download/>

**步驟 2：執行安裝程式**

```powershell
# 以管理員身份執行安裝程式
# 預設安裝路徑：C:\Program Files\Jenkins
# 預設資料目錄：C:\ProgramData\Jenkins\.jenkins
```

**步驟 3：服務管理**

```powershell
# 啟動服務
Start-Service Jenkins

# 停止服務
Stop-Service Jenkins

# 重啟服務
Restart-Service Jenkins

# 查看服務狀態
Get-Service Jenkins
```

### ⚙️ 基本系統設定

#### 2.3 全域安全設定

**步驟 1：設定安全領域**

1. 前往 「Manage Jenkins」→「Configure Global Security」
2. 選擇安全領域：
   - **Jenkins' own user database**：適合小團隊
   - **LDAP**：企業環境整合
   - **Active Directory**：Windows 環境

**步驟 2：授權策略**

```
授權策略選項：
├── Anyone can do anything（僅限開發環境）
├── Legacy mode（不建議）
├── Logged-in users can do anything（基本安全）
├── Matrix-based security（細緻權限控制）
└── Project-based Matrix Authorization（專案層級權限）
```

**步驟 3：設定 CSRF 保護**

- 啟用「Prevent Cross Site Request Forgery exploits」
- 設定「Default Crumb Issuer」

#### 2.4 系統設定優化

**JVM 記憶體設定：**

```powershell
# 設定環境變數
$env:JAVA_OPTS="-Xms1g -Xmx4g -XX:+UseG1GC"

# 或在 jenkins.xml 中設定（Windows Service）
<arguments>-Xrs -Xmx4g -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle</arguments>
```

**磁碟空間管理：**

```groovy
// 在 「Manage Jenkins」→「Script Console」中執行
import jenkins.model.Jenkins

// 設定全域建置記錄保留策略
Jenkins.instance.getAllItems().each { item ->
    if (item.hasProperty('buildDiscarder')) {
        item.buildDiscarder = new hudson.tasks.LogRotator(-1, 10, -1, -1)
        item.save()
    }
}
```

#### 2.5 網路與代理設定

**代理伺服器設定：**

1. 前往「Manage Jenkins」→「Manage Plugins」→「Advanced」
2. 設定 HTTP Proxy 資訊：
   - Server: proxy.company.com
   - Port: 8080
   - Username/Password（如需要）

**防火牆設定：**

```powershell
# 開啟 Windows 防火牆規則
New-NetFirewallRule -DisplayName "Jenkins HTTP" -Direction Inbound -Protocol TCP -LocalPort 8080
New-NetFirewallRule -DisplayName "Jenkins Agent" -Direction Inbound -Protocol TCP -LocalPort 50000
```

### 📊 安裝驗證

#### 2.6 系統健康檢查

**檢查清單：**

```mermaid
flowchart TD
    A[Jenkins 安裝完成] --> B{Web UI 可訪問?}
    B -->|是| C{管理員登入成功?}
    B -->|否| D[檢查服務狀態]
    C -->|是| E{插件安裝完成?}
    C -->|否| F[檢查用戶設定]
    E -->|是| G[建立第一個 Job]
    E -->|否| H[檢查網路連線]
    
    D --> I[重啟 Jenkins 服務]
    F --> J[重設管理員密碼]
    H --> K[設定代理伺服器]
    
    I --> B
    J --> C
    K --> E
```

**系統資訊檢查：**

```groovy
// 在 Script Console 中執行
println "Jenkins 版本: " + Jenkins.instance.getVersion()
println "Java 版本: " + System.getProperty("java.version")
println "作業系統: " + System.getProperty("os.name")
println "記憶體使用: " + Runtime.getRuntime().totalMemory()
println "可用處理器: " + Runtime.getRuntime().availableProcessors()
```

### 💡 實務案例

#### 案例：企業環境快速部署

**情境**：為 20 人開發團隊建立 Jenkins 環境

**建議配置：**

```yaml
# docker-compose.yml for production
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins-prod
    restart: always
    ports:
      - "80:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - JAVA_OPTS=-Xmx8g -XX:+UseG1GC
      - JENKINS_OPTS=--prefix=/
    networks:
      - jenkins-network

  jenkins-agent:
    image: jenkins/inbound-agent:latest
    container_name: jenkins-agent-1
    environment:
      - JENKINS_URL=http://jenkins:8080
      - JENKINS_AGENT_NAME=agent-1
      - JENKINS_SECRET=<agent-secret>
    depends_on:
      - jenkins
    networks:
      - jenkins-network

volumes:
  jenkins_home:

networks:
  jenkins-network:
    driver: bridge
```

### ⚠️ 注意事項

1. **安全第一**：
   - 永遠不要使用預設密碼
   - 定期更新 Jenkins 版本
   - 限制網路存取範圍

2. **效能監控**：
   - 監控記憶體使用量
   - 設定適當的建置保留政策
   - 定期清理工作空間

3. **備份策略**：
   - 定期備份 `JENKINS_HOME`
   - 版本控制重要設定
   - 測試恢復程序

4. **資源規劃**：
   - 根據併發建置數量規劃資源
   - 考慮代理節點的擴展性
   - 監控磁碟空間使用

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Jenkins 安裝 | WAR、Docker、Windows Service 安裝 |
| 系統安全 | 全域安全設定、授權策略 |
| 系統管理 | JVM 調優、磁碟管理、代理設定 |

### 📝 練習作業

1. **基礎練習**：使用 WAR 文件在本機安裝 Jenkins
2. **進階練習**：使用 Docker Compose 建立 Jenkins 叢集
3. **實務練習**：設定企業級安全策略和權限管理

---

## 第3章 Jenkins 介面導覽

### 🎯 學習目標

- 熟悉 Jenkins Web UI 各個區域功能
- 掌握基本操作和導航技巧
- 了解系統監控和管理介面

### 📚 核心概念

#### 3.1 Jenkins 主介面架構

```mermaid
graph TD
    A[Jenkins 主頁] --> B[左側選單]
    A --> C[主要內容區]
    A --> D[頁首區域]
    
    B --> E[New Item]
    B --> F[People]
    B --> G[Build History]
    B --> H[Manage Jenkins]
    B --> I[My Views]
    
    C --> J[Dashboard View]
    C --> K[Job 列表]
    C --> L[Build Queue]
    C --> M[Build Executor Status]
    
    D --> N[使用者資訊]
    D --> O[搜尋功能]
    D --> P[通知區域]
```

#### 3.2 主要功能區域詳解

**1. 左側選單 (Left Navigation)**

| 功能 | 說明 | 權限需求 |
|------|------|----------|
| **New Item** | 建立新的 Job/Pipeline | Job Create |
| **People** | 查看使用者列表和權限 | Overall Read |
| **Build History** | 所有建置歷史記錄 | Overall Read |
| **Manage Jenkins** | 系統管理和設定 | Overall Administer |
| **My Views** | 個人化視圖管理 | View Create |
| **Credentials** | 憑證管理 | Credentials View |

**2. 主要內容區域**

```
Dashboard 內容配置：
├── Jenkins 標頭橫幅
├── 建置佇列 (Build Queue)
├── 建置執行器狀態 (Build Executor Status)
├── 專案/Job 列表
└── 視圖標籤 (View Tabs)
```

**3. Job 狀態圖示說明**

| 圖示 | 狀態 | 說明 |
|------|------|------|
| 🔵 藍色圓球 | Success | 建置成功 |
| 🔴 紅色圓球 | Failed | 建置失敗 |
| 🟡 黃色圓球 | Unstable | 建置不穩定（測試失敗但編譯成功） |
| ⚫ 灰色圓球 | Aborted/Disabled | 建置中止或 Job 停用 |
| ⚡ 閃爍動畫 | Building | 正在建置中 |

#### 3.3 Job 管理介面

**Job 詳細頁面結構：**

```mermaid
graph LR
    A[Job 首頁] --> B[建置歷史]
    A --> C[工作空間]
    A --> D[設定]
    A --> E[狀態]
    
    B --> F[Build #1]
    B --> G[Build #2]
    F --> H[Console Output]
    F --> I[Changes]
    F --> J[Test Results]
    
    C --> K[檔案瀏覽器]
    D --> L[General]
    D --> M[Source Code Management]
    D --> N[Build Triggers]
    D --> O[Build Steps]
    D --> P[Post-build Actions]
```

**建置詳細資訊：**

- **Console Output**：完整的建置日誌
- **Changes**：本次建置包含的程式碼變更
- **Test Results**：測試執行結果和報告
- **Workspace**：建置過程中的檔案內容
- **Build Artifacts**：建置產生的檔案

### 🛠️ 實用操作技巧

#### 3.4 Dashboard 自訂化

**建立自訂視圖：**

1. **List View（列表視圖）**

```
步驟：
1. 點選「New View」
2. 選擇「List View」
3. 設定過濾條件：
   - Job 名稱正則表達式
   - 狀態過濾（成功/失敗/不穩定）
   - 時間範圍
4. 選擇顯示欄位：
   - Status（狀態圖示）
   - Weather（趨勢圖示）
   - Name（Job 名稱）
   - Last Success（最後成功時間）
   - Last Failure（最後失敗時間）
   - Last Duration（執行時間）
```

2. **Build Pipeline View（建置管道視圖）**

```
安裝 Build Pipeline Plugin 後：
1. 新增「Build Pipeline View」
2. 設定上游專案
3. 顯示觸發關係
4. 配置管道視覺化
```

**視圖設定範例：**

```groovy
// 透過 Script Console 批量建立視圖
import hudson.model.*
import hudson.plugins.view.dashboard.*

def jenkins = Jenkins.instance

// 建立開發團隊視圖
def devView = new ListView("Development Team")
devView.setIncludeRegex(".*-dev.*|.*-feature.*")
jenkins.addView(devView)

// 建立生產視圖  
def prodView = new ListView("Production")
prodView.setIncludeRegex(".*-prod.*|.*-release.*")
jenkins.addView(prodView)

jenkins.save()
```

#### 3.5 搜尋和過濾功能

**全域搜尋技巧：**

```
搜尋語法：
├── job:project-name     # 搜尋特定 Job
├── build:123           # 搜尋特定建置編號
├── node:agent-1        # 搜尋特定節點
├── user:john.doe       # 搜尋特定使用者相關項目
└── view:my-view        # 搜尋特定視圖
```

**進階過濾：**

```javascript
// 使用瀏覽器開發者工具執行
// 隱藏已停用的 Job
document.querySelectorAll('tr.job-disabled').forEach(row => {
    row.style.display = 'none';
});

// 只顯示失敗的 Job
document.querySelectorAll('tr:not(.job-status-failed)').forEach(row => {
    if (row.querySelector('.job-status')) {
        row.style.display = 'none';
    }
});
```

#### 3.6 系統管理介面

**Manage Jenkins 主要功能：**

```mermaid
graph TD
    A[Manage Jenkins] --> B[Configure System]
    A --> C[Global Tool Configuration]
    A --> D[Manage Plugins]
    A --> E[Manage Nodes and Clouds]
    A --> F[Configure Global Security]
    A --> G[Manage Credentials]
    A --> H[System Information]
    A --> I[System Log]
    A --> J[Load Statistics]
    
    B --> K[Jenkins Location]
    B --> L[Global Properties]
    B --> M[Email Configuration]
    
    C --> N[JDK Installations]
    C --> O[Git Installations]
    C --> P[Maven Installations]
    
    D --> Q[Available Plugins]
    D --> R[Installed Plugins]
    D --> S[Advanced Settings]
```

**系統資訊查看：**

```groovy
// System Information 頁面顯示的關鍵資訊
println "Jenkins 版本: ${Jenkins.getVersion()}"
println "Java 版本: ${System.getProperty('java.version')}"
println "記憶體使用情況:"
println "  - 總記憶體: ${Runtime.getRuntime().totalMemory() / 1024 / 1024} MB"
println "  - 最大記憶體: ${Runtime.getRuntime().maxMemory() / 1024 / 1024} MB"
println "  - 可用記憶體: ${Runtime.getRuntime().freeMemory() / 1024 / 1024} MB"

// 檢查磁碟空間
def workspace = new File(System.getProperty('JENKINS_HOME'))
println "磁碟空間:"
println "  - 總空間: ${workspace.getTotalSpace() / 1024 / 1024 / 1024} GB"
println "  - 可用空間: ${workspace.getFreeSpace() / 1024 / 1024 / 1024} GB"
```

### 📊 監控和報告

#### 3.7 建置監控

**Load Statistics 解讀：**

```mermaid
graph LR
    A[Load Statistics] --> B[Queue Length]
    A --> C[Executor Utilization]
    
    B --> D[等待建置數量]
    B --> E[等待時間分析]
    
    C --> F[執行器使用率]
    C --> G[空閒時間分析]
    
    style B fill:#ff9999
    style C fill:#99ff99
    style F fill:#ffff99
```

**關鍵指標說明：**

- **Queue Length**：建置佇列長度，高值表示資源不足
- **Executor Utilization**：執行器使用率，應保持在 70-80%
- **Response Time**：系統回應時間，影響使用者體驗

**效能調優建議：**

```bash
# 監控腳本範例
#!/bin/bash

# 檢查建置佇列長度
QUEUE_LENGTH=$(curl -s "http://localhost:8080/queue/api/json" | jq '.items | length')
echo "目前佇列長度: $QUEUE_LENGTH"

# 檢查執行器狀態
BUSY_EXECUTORS=$(curl -s "http://localhost:8080/computer/api/json" | jq '[.computer[].executors[] | select(.currentExecutable != null)] | length')
TOTAL_EXECUTORS=$(curl -s "http://localhost:8080/computer/api/json" | jq '[.computer[].executors[]] | length')
UTILIZATION=$(echo "scale=2; $BUSY_EXECUTORS * 100 / $TOTAL_EXECUTORS" | bc)
echo "執行器使用率: $UTILIZATION%"

# 警告閾值檢查
if [ $QUEUE_LENGTH -gt 10 ]; then
    echo "警告: 建置佇列過長！"
fi

if [ $(echo "$UTILIZATION > 90" | bc) -eq 1 ]; then
    echo "警告: 執行器使用率過高！"
fi
```

#### 3.8 日誌管理

**系統日誌分類：**

| 日誌類型 | 路徑 | 用途 |
|----------|------|------|
| **Jenkins 主日誌** | `$JENKINS_HOME/logs/jenkins.log` | 系統啟動和核心事件 |
| **Job 建置日誌** | Job Console Output | 個別建置執行記錄 |
| **外掛程式日誌** | System Log 頁面 | 外掛程式除錯資訊 |
| **安全日誌** | Security 相關日誌 | 登入、權限變更記錄 |

**日誌等級設定：**

```groovy
// 在 Script Console 中設定日誌等級
import java.util.logging.*

// 設定 Git 插件的日誌等級為 DEBUG
Logger.getLogger("hudson.plugins.git").setLevel(Level.FINE)

// 設定 Pipeline 日誌等級
Logger.getLogger("org.jenkinsci.plugins.workflow").setLevel(Level.FINE)

// 設定根日誌處理器
def rootLogger = Logger.getLogger("")
def handler = new ConsoleHandler()
handler.setLevel(Level.FINE)
rootLogger.addHandler(handler)
```

### 💡 實務案例

#### 案例：團隊 Dashboard 設計

**情境**：為 Java 開發團隊設計 Dashboard

**解決方案：**

1. **主視圖設計**

```
團隊 Dashboard 配置：
├── 視圖 1：「Active Development」
│   ├── 顯示所有 feature 分支建置
│   ├── 過濾條件：job name 包含 "feature"
│   └── 顯示欄位：Status, Weather, Name, Last Success
├── 視圖 2：「Release Pipeline」  
│   ├── 顯示發布相關的建置
│   ├── Pipeline View 格式
│   └── 包含部署階段狀態
└── 視圖 3：「Failed Builds」
    ├── 只顯示失敗的建置
    ├── 按失敗時間排序
    └── 包含負責人資訊
```

2. **監控 Widget 設定**

```html
<!-- 自訂 Dashboard HTML -->
<div class="jenkins-dashboard">
    <div class="metrics-row">
        <div class="metric-card">
            <h3>建置成功率</h3>
            <div class="metric-value" id="success-rate">85%</div>
        </div>
        <div class="metric-card">
            <h3>平均建置時間</h3>
            <div class="metric-value" id="avg-duration">5m 30s</div>
        </div>
        <div class="metric-card">
            <h3>待修復建置</h3>
            <div class="metric-value failure" id="failed-count">3</div>
        </div>
    </div>
</div>
```

### ⚠️ 注意事項

1. **效能考量**：
   - 避免在 Dashboard 顯示過多 Job
   - 適當設定重新整理頻率
   - 使用 View 過濾減少載入時間

2. **權限管理**：
   - 根據團隊角色設定不同視圖
   - 敏感資訊設定適當的存取權限
   - 定期檢查使用者權限

3. **使用者體驗**：
   - 保持介面簡潔明瞭
   - 使用有意義的 Job 命名規則
   - 提供清楚的狀態指示

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Jenkins UI 導航 | Dashboard、Views、Job 管理 |
| 系統監控 | Load Statistics、日誌管理 |
| 使用者管理 | People、權限、安全設定 |

---

## 第4章 Plugin 管理與基礎設定

### 🎯 學習目標

- 掌握 Jenkins 插件管理機制
- 安裝和設定核心插件
- 了解插件版本管理和相依性
- 建立 Java 開發所需的基礎環境

### 📚 核心概念

#### 4.1 Jenkins 插件架構

```mermaid
graph TD
    A[Jenkins Core] --> B[Plugin Manager]
    B --> C[Update Center]
    C --> D[Official Plugins]
    C --> E[Community Plugins]
    C --> F[Third-party Plugins]
    
    A --> G[Extension Points]
    G --> H[Build Steps]
    G --> I[SCM Providers]
    G --> J[Notification Systems]
    G --> K[Authentication]
    
    subgraph "Plugin Categories"
        L[Build Tools]
        M[Source Control]
        N[Testing & Quality]
        O[Deployment]
        P[Monitoring]
    end
```

**插件分類與功能：**

| 類別 | 核心插件 | 功能說明 |
|------|----------|----------|
| **建置工具** | Maven, Gradle, Ant | 專案建置和依賴管理 |
| **版本控制** | Git, SVN, Mercurial | 原始碼管理整合 |
| **測試品質** | JUnit, Jacoco, Checkstyle | 測試報告和程式碼品質 |
| **部署發布** | Deploy to Container, SSH | 應用程式部署 |
| **通知告警** | Email, Slack, Teams | 建置結果通知 |
| **安全認證** | LDAP, Active Directory | 使用者驗證整合 |

#### 4.2 插件生命週期管理

```mermaid
flowchart LR
    A[搜尋插件] --> B[檢查相依性]
    B --> C[下載安裝]
    C --> D[重啟 Jenkins]
    D --> E[配置設定]
    E --> F[測試功能]
    F --> G[監控效能]
    G --> H[版本更新]
    H --> I[移除/停用]
```

### 🛠️ 核心插件安裝與設定

#### 4.3 Java 開發必備插件

**基礎套件（Building 套件）：**

1. **Git Plugin**

```
功能：Git 版本控制整合
安裝方式：Manage Jenkins → Manage Plugins → Available → 搜尋 "Git"
設定位置：Manage Jenkins → Global Tool Configuration → Git
```

2. **Maven Integration Plugin**

```
功能：Maven 專案建置支援
相依插件：Maven Invoker Plugin
設定項目：
- Maven installations
- MAVEN_OPTS 設定
- Local repository 路徑
```

3. **JUnit Plugin**

```
功能：測試結果報告和視覺化
支援格式：JUnit XML, TestNG XML
配置選項：
- Test result archiving
- Failure notification
- Trend analysis
```

**進階功能插件：**

4. **Pipeline Plugin Suite**

```bash
# Pipeline 相關插件組合
Pipeline: Groovy
Pipeline: Stage View  
Pipeline: Build Step
Pipeline: Input Step
Pipeline: Milestone Step
```

5. **Blue Ocean**

```
功能：現代化 Pipeline 視覺化介面
特色：
- 直觀的 Pipeline 編輯器
- 美觀的執行視圖
- 分支探索功能
```

#### 4.4 實務插件安裝腳本

**自動化插件安裝：**

```groovy
// install-plugins.groovy
// 放置於 $JENKINS_HOME/init.groovy.d/ 目錄下

import jenkins.model.*
import hudson.model.*
import hudson.PluginWrapper
import hudson.PluginManager

def jenkins = Jenkins.getInstance()
def pm = jenkins.getPluginManager()
def uc = jenkins.getUpdateCenter()

// 定義必要插件列表
def plugins = [
    'git',
    'maven-plugin', 
    'junit',
    'jacoco',
    'checkstyle',
    'workflow-aggregator',  // Pipeline suite
    'blueocean',
    'build-timeout',
    'timestamper',
    'ws-cleanup',
    'ant',
    'gradle',
    'email-ext',
    'slack',
    'credentials-binding'
]

// 檢查並安裝插件
def needRestart = false
plugins.each { pluginName ->
    if (!pm.getPlugin(pluginName)) {
        println "安裝插件: ${pluginName}"
        def deployment = uc.getPlugin(pluginName).deploy()
        deployment.get()
        needRestart = true
    } else {
        println "插件已安裝: ${pluginName}"
    }
}

// 如果有新插件安裝，重啟 Jenkins
if (needRestart) {
    println "重啟 Jenkins 以啟用新插件..."
    jenkins.restart()
}
```

**批量插件管理腳本：**

```bash
#!/bin/bash
# install-jenkins-plugins.sh

JENKINS_URL="http://localhost:8080"
JENKINS_USER="admin"
JENKINS_TOKEN="your-api-token"

# 核心插件列表
PLUGINS=(
    "git"
    "maven-plugin"
    "junit"
    "jacoco"
    "workflow-aggregator"
    "blueocean"
    "email-ext"
    "slack"
    "credentials-binding"
    "build-timeout"
    "timestamper"
    "ws-cleanup"
)

# 安裝插件函數
install_plugin() {
    local plugin_name=$1
    echo "安裝插件: $plugin_name"
    
    curl -X POST "${JENKINS_URL}/pluginManager/installNecessaryPlugins" \
         --user "${JENKINS_USER}:${JENKINS_TOKEN}" \
         --data-urlencode "plugin.${plugin_name}.default=on"
}

# 批量安裝
for plugin in "${PLUGINS[@]}"; do
    install_plugin "$plugin"
done

echo "插件安裝完成，請重啟 Jenkins"
```

#### 4.5 全域工具設定

**Java JDK 設定：**

```groovy
// 透過 Script Console 設定 JDK
import hudson.model.*
import hudson.tools.*
import hudson.util.DescribableList
import jenkins.model.*

def jenkins = Jenkins.getInstance()
def jdkDesc = jenkins.getDescriptor("hudson.model.JDK")

// 新增 JDK 17 設定
def jdkList = [
    new JDK("JDK-17", "/usr/lib/jvm/java-17-openjdk"),
    new JDK("JDK-11", "/usr/lib/jvm/java-11-openjdk"),
    new JDK("JDK-8", "/usr/lib/jvm/java-8-openjdk")
]

jdkDesc.setInstallations(jdkList as JDK[])
jenkins.save()
```

**Maven 設定：**

```groovy
// Maven 全域設定
import hudson.tasks.Maven
import hudson.tools.*

def mavenDesc = jenkins.getDescriptor("hudson.tasks.Maven\$MavenInstallation")
def mavenInstallations = [
    new Maven.MavenInstallation("Maven-3.9", "/opt/maven", []),
    new Maven.MavenInstallation("Maven-3.8", "/opt/maven-3.8", [])
]

mavenDesc.setInstallations(mavenInstallations as Maven.MavenInstallation[])
jenkins.save()
```

**Git 設定：**

```groovy
// Git 全域設定
import hudson.plugins.git.*
import hudson.tools.*

def gitDesc = jenkins.getDescriptor("hudson.plugins.git.GitTool")
def gitInstallations = [
    new GitTool("Default", "/usr/bin/git", [])
]

gitDesc.setInstallations(gitInstallations as GitTool[])

// 設定全域 Git 配置
def gitSCM = jenkins.getDescriptor("hudson.plugins.git.GitSCM")
gitSCM.setGlobalConfigName("Jenkins CI")
gitSCM.setGlobalConfigEmail("jenkins@company.com")
gitSCM.setCreateAccountBasedOnEmail(false)

jenkins.save()
```

### 📊 插件效能與監控

#### 4.6 插件效能優化

**記憶體使用監控：**

```groovy
// 插件記憶體使用分析
import hudson.PluginManager
import hudson.PluginWrapper
import jenkins.model.Jenkins

def jenkins = Jenkins.getInstance()
def pm = jenkins.getPluginManager()

println "插件記憶體使用統計："
println "=" * 50

pm.getPlugins().sort { it.shortName }.each { plugin ->
    def wrapper = plugin as PluginWrapper
    def classLoader = wrapper.classLoader
    
    // 估算類別載入數量
    def loadedClasses = classLoader.getLoadedClasses()?.size() ?: 0
    
    println sprintf("%-30s | 狀態: %-8s | 類別: %4d", 
                   wrapper.shortName,
                   wrapper.isEnabled() ? "啟用" : "停用",
                   loadedClasses)
}

// 系統記憶體統計
def runtime = Runtime.getRuntime()
println "\n系統記憶體統計："
println "總記憶體: ${runtime.totalMemory() / 1024 / 1024} MB"
println "已用記憶體: ${(runtime.totalMemory() - runtime.freeMemory()) / 1024 / 1024} MB"
println "可用記憶體: ${runtime.freeMemory() / 1024 / 1024} MB"
```

**插件相依性檢查：**

```groovy
// 檢查插件相依性衝突
import hudson.PluginWrapper
import jenkins.model.Jenkins

def jenkins = Jenkins.getInstance()
def pm = jenkins.getPluginManager()

println "插件相依性分析："
println "=" * 60

pm.getPlugins().each { plugin ->
    def wrapper = plugin as PluginWrapper
    def dependencies = wrapper.getDependencies()
    
    if (dependencies.size() > 0) {
        println "\n插件: ${wrapper.shortName} (${wrapper.version})"
        dependencies.each { dep ->
            def depPlugin = pm.getPlugin(dep.shortName)
            def status = depPlugin?.isEnabled() ? "✓" : "✗"
            println "  ${status} ${dep.shortName} (需要: ${dep.version})"
        }
    }
}
```

#### 4.7 插件更新管理策略

**安全更新檢查：**

```bash
#!/bin/bash
# check-plugin-updates.sh

JENKINS_HOME="/var/jenkins_home"
PLUGIN_DIR="${JENKINS_HOME}/plugins"

echo "檢查插件安全更新..."

# 檢查有安全修復的插件
curl -s "https://updates.jenkins.io/current/update-center.json" | \
    jq -r '.plugins | to_entries[] | select(.value.buildDate > "2024-01-01") | 
           "\(.key): \(.value.version) (安全修復: \(.value.securityWarnings // [] | length))"'

# 檢查本地安裝的插件版本
echo -e "\n本地插件版本："
for plugin in ${PLUGIN_DIR}/*.jpi; do
    plugin_name=$(basename "$plugin" .jpi)
    if [ -f "${PLUGIN_DIR}/${plugin_name}/META-INF/MANIFEST.MF" ]; then
        version=$(grep "Plugin-Version" "${PLUGIN_DIR}/${plugin_name}/META-INF/MANIFEST.MF" | cut -d' ' -f2)
        echo "${plugin_name}: ${version}"
    fi
done
```

### 💡 實務案例

#### 案例：Java 開發團隊插件配置

**情境**：為 Java Spring Boot 專案配置完整的 CI/CD 插件環境

**解決方案：**

1. **核心開發插件組合**

```yaml
# jenkins-plugins.yml
core_plugins:
  version_control:
    - git
    - github
    - github-branch-source
  
  build_tools:
    - maven-plugin
    - gradle
    - ant
  
  testing_quality:
    - junit
    - jacoco
    - checkstyle
    - spotbugs
    - sonar
  
  pipeline:
    - workflow-aggregator
    - pipeline-stage-view
    - blue-ocean
  
  deployment:
    - ssh-slaves
    - publish-over-ssh
    - docker-plugin
  
  notification:
    - email-ext
    - slack
    - teams
  
  utilities:
    - build-timeout
    - timestamper
    - ws-cleanup
    - credentials-binding
```

2. **環境配置腳本**

```groovy
// setup-java-environment.groovy
import jenkins.model.*
import hudson.model.*
import hudson.tools.*

def jenkins = Jenkins.getInstance()

// 1. 配置 JDK
def jdkDesc = jenkins.getDescriptor("hudson.model.JDK")
def jdkInstallations = [
    new JDK("JDK-17", System.getenv("JAVA_HOME") ?: "/usr/lib/jvm/java-17-openjdk"),
    new JDK("JDK-11", "/usr/lib/jvm/java-11-openjdk")
]
jdkDesc.setInstallations(jdkInstallations as JDK[])

// 2. 配置 Maven
def mavenDesc = jenkins.getDescriptor("hudson.tasks.Maven\$MavenInstallation")
def mavenInstallations = [
    new Maven.MavenInstallation("Maven-3.9", "/opt/maven", [])
]
mavenDesc.setInstallations(mavenInstallations as Maven.MavenInstallation[])

// 3. 配置 Git
def gitDesc = jenkins.getDescriptor("hudson.plugins.git.GitTool")
def gitInstallations = [
    new GitTool("Default", "/usr/bin/git", [])
]
gitDesc.setInstallations(gitInstallations as GitTool[])

// 4. 設定全域屬性
def globalProps = jenkins.getGlobalNodeProperties()
def envVars = new hudson.slaves.EnvironmentVariablesNodeProperty([
    "MAVEN_OPTS": "-Xmx2g -XX:+UseG1GC",
    "JAVA_TOOL_OPTIONS": "-Dfile.encoding=UTF-8"
])
globalProps.replaceBy([envVars])

jenkins.save()
println "Java 開發環境配置完成！"
```

### ⚠️ 注意事項

1. **插件安全性**：
   - 定期檢查安全通報
   - 避免安裝來源不明的插件
   - 建立插件白名單制度

2. **版本相容性**：
   - 測試環境先行更新
   - 檢查插件相依性
   - 保留版本回滾機制

3. **效能影響**：
   - 監控插件對系統效能的影響
   - 避免安裝過多非必要插件
   - 定期清理未使用的插件

4. **備份策略**：
   - 備份插件配置
   - 記錄插件版本清單
   - 建立災難恢復計劃

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Plugin 管理 | 安裝、更新、相依性管理 |
| 工具配置 | JDK、Maven、Git 設定 |
| 系統最佳化 | 效能監控、記憶體管理 |

### 📝 練習作業

1. **基礎練習**：安裝 Java 開發必備的 10 個核心插件
2. **進階練習**：建立自動化插件管理腳本
3. **實務練習**：設計企業級插件管理策略和標準

---

## 第5章 Freestyle Project 入門

### 🎯 學習目標

- 掌握 Freestyle Project 的建立和配置
- 了解各種建置步驟的設定方法
- 學會設定觸發條件和後置動作
- 建立第一個 Java 專案的自動化建置

### 📚 核心概念

#### 5.1 Freestyle Project 概述

Freestyle Project 是 Jenkins 中最基本的 Job 類型，提供圖形化介面來配置建置流程。雖然功能不如 Pipeline 強大，但學習曲線平緩，適合初學者理解 CI/CD 基本概念。

```mermaid
graph TD
    A[Freestyle Project] --> B[General Settings]
    A --> C[Source Code Management]
    A --> D[Build Triggers]
    A --> E[Build Environment]
    A --> F[Build Steps]
    A --> G[Post-build Actions]
    
    B --> H[Project Name]
    B --> I[Description]
    B --> J[Discard Old Builds]
    
    C --> K[Git/SVN]
    C --> L[Branch Selection]
    C --> M[Credentials]
    
    D --> N[Build Periodically]
    D --> O[Poll SCM]
    D --> P[GitHub Hook]
    
    F --> Q[Execute Shell]
    F --> R[Invoke Maven]
    F --> S[Windows Batch]
    
    G --> T[Archive Artifacts]
    G --> U[Publish Test Results]
    G --> V[Email Notification]
```

#### 5.2 配置區域詳解

**基本設定區域 (General)：**

| 設定項目 | 說明 | 建議值 |
|----------|------|--------|
| **Project Name** | 專案識別名稱 | 使用有意義的命名規則 |
| **Description** | 專案描述 | 包含專案目的和負責人 |
| **Discard Old Builds** | 建置保留策略 | 保留最近 20 次建置 |
| **Restrict Node** | 限制執行節點 | 根據環境需求選擇 |
| **Disable Project** | 暫時停用專案 | 維護期間使用 |

**進階設定選項：**

```groovy
// 透過 Script Console 批量設定專案屬性
import jenkins.model.*
import hudson.model.*

def jenkins = Jenkins.getInstance()

// 設定建置保留策略
jenkins.getAllItems(Job.class).each { job ->
    if (job.name.startsWith("java-")) {
        job.buildDiscarder = new hudson.tasks.LogRotator(
            -1,    // daysToKeep: -1 表示不限制天數
            20,    // numToKeep: 保留最近 20 次建置
            -1,    // artifactDaysToKeep
            5      // artifactNumToKeep: 保留 5 次建置的產物
        )
        job.save()
        println "已更新 ${job.name} 的建置保留策略"
    }
}
```

### 🛠️ 實務配置步驟

#### 5.3 建立第一個 Java 專案

**步驟 1：建立新的 Freestyle Project**

```bash
專案建立流程：
1. 點選「New Item」
2. 輸入專案名稱：java-tutorial-build
3. 選擇「Freestyle project」
4. 點選「OK」
```

**步驟 2：基本資訊設定**

```yaml
# 專案基本設定
project_name: "java-tutorial-build"
description: |
  Java Tutorial 專案自動化建置
  - 編譯 Java 原始碼
  - 執行單元測試
  - 生成測試報告
  
build_retention:
  days_to_keep: -1
  num_to_keep: 20
  artifact_days_to_keep: -1  
  artifact_num_to_keep: 5

restrictions:
  node_label: ""  # 空白表示可在任何節點執行
  concurrent_builds: false  # 不允許並行建置
```

**步驟 3：原始碼管理設定**

```bash
# Git 設定範例
Repository URL: https://github.com/your-org/java-tutorial.git
Credentials: jenkins-github-token
Branches to build: */master
Repository browser: (auto)

# 進階 Git 設定
Additional Behaviours:
- Clean before checkout: 是
- Checkout to sub-directory: src
- Polling ignores commits: 忽略特定路徑變更
```

**設定 Git 憑證：**

```groovy
// 建立 Git 憑證 (透過 Script Console)
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import hudson.util.Secret

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

// 建立 GitHub Token 憑證
def githubToken = new StringCredentialsImpl(
    CredentialsScope.GLOBAL,
    "github-token",
    "GitHub API Token",
    Secret.fromString("your-github-token")
)

store.addCredentials(domain, githubToken)
println "GitHub 憑證建立完成"
```

#### 5.4 建置觸發設定

**觸發方式比較：**

| 觸發方式 | 使用時機 | 設定語法 | 優缺點 |
|----------|----------|----------|--------|
| **手動觸發** | 測試、緊急修正 | - | 完全可控，但需人工介入 |
| **定時建置** | 夜間建置、報告生成 | `H 2 * * *` | 定時執行，但可能建置不必要版本 |
| **SCM 輪詢** | 程式碼變更檢測 | `H/5 * * * *` | 及時檢測，但增加伺服器負載 |
| **Webhook** | 即時觸發 | GitHub Hook | 最即時，但需要網路設定 |

**Cron 語法詳解：**

```bash
# Jenkins Cron 語法 (分 時 日 月 週)
# 使用 H 表示 Hash，避免同時啟動

# 範例設定
H 2 * * *        # 每日凌晨 2 點左右
H H(0-7) * * *   # 每日 0-7 點間的隨機時間
H/15 * * * *     # 每 15 分鐘
H 8-17/2 * * 1-5 # 週一到週五，8-17 點間每 2 小時

# 實際專案建議
H 9,12,17 * * 1-5  # 工作日的 9 點、12 點、17 點
```

**SCM 輪詢最佳實務：**

```bash
# 推薦設定
Poll SCM Schedule: H/10 * * * *  # 每 10 分鐘檢查一次

# 進階設定：忽略特定檔案變更
Included Regions:
src/.*
pom.xml

Excluded Regions:
README\.md
docs/.*
\.gitignore
```

#### 5.5 建置環境設定

**環境變數配置：**

```groovy
// 常用環境變數設定
def envVars = [
    "JAVA_HOME": "/usr/lib/jvm/java-17-openjdk",
    "MAVEN_HOME": "/opt/maven",
    "MAVEN_OPTS": "-Xmx2g -XX:+UseG1GC",
    "PATH": "\${MAVEN_HOME}/bin:\${JAVA_HOME}/bin:\${PATH}"
]

// 在 Job 設定中的環境變數區塊
Environment Variables:
JAVA_TOOL_OPTIONS: -Dfile.encoding=UTF-8
MAVEN_ARGS: -B -V -e
BUILD_TIMESTAMP: ${BUILD_TIMESTAMP}
```

**超時設定：**

```yaml
# 建置超時設定
build_timeout:
  enabled: true
  timeout_minutes: 30
  timeout_action: "abort"  # abort, fail,或 unstable
  
timeout_strategy:
  - absolute_timeout: 30 分鐘
  - no_activity_timeout: 10 分鐘  # 10 分鐘無輸出就中止
  - elastic_timeout: 200%  # 根據歷史建置時間動態調整
```

#### 5.6 建置步驟配置

**Maven 建置步驟：**

```xml
<!-- 建置步驟 1：編譯 -->
Goals: clean compile
Maven Version: Maven-3.9
POM: pom.xml
Properties:
  maven.test.skip=true
  java.awt.headless=true

<!-- 建置步驟 2：測試 -->  
Goals: test
Maven Version: Maven-3.9
Properties:
  maven.test.failure.ignore=true
  junit.jupiter.execution.parallel.enabled=true
```

**Shell 腳本建置步驟：**

```bash
#!/bin/bash
# 建置步驟腳本範例

set -e  # 遇到錯誤立即停止

echo "=== 開始建置 Java Tutorial 專案 ==="
echo "建置編號: ${BUILD_NUMBER}"
echo "建置時間: $(date)"
echo "Git 版本: ${GIT_COMMIT:0:8}"

# 1. 環境檢查
echo "=== 環境檢查 ==="
java -version
mvn -version
echo "工作目錄: $(pwd)"

# 2. 清理舊檔案
echo "=== 清理環境 ==="
mvn clean

# 3. 編譯專案
echo "=== 編譯專案 ==="
mvn compile -B -V

# 4. 執行測試
echo "=== 執行測試 ==="
mvn test -B \
    -Dmaven.test.failure.ignore=true \
    -Djunit.jupiter.execution.parallel.enabled=true \
    -Djunit.jupiter.execution.parallel.mode.default=concurrent

# 5. 檢查測試結果
if [ -f target/surefire-reports/TEST-*.xml ]; then
    echo "測試報告已生成"
    find target/surefire-reports -name "*.xml" -exec basename {} \;
else
    echo "警告: 未找到測試報告"
fi

echo "=== 建置完成 ==="
```

**Windows 批次腳本：**

```batch
@echo off
REM Windows 建置腳本

echo === 開始建置 Java Tutorial 專案 ===
echo 建置編號: %BUILD_NUMBER%
echo 建置時間: %DATE% %TIME%

REM 環境檢查
echo === 環境檢查 ===
java -version
call mvn -version

REM 清理並編譯
echo === 清理並編譯 ===
call mvn clean compile -B -V
if %ERRORLEVEL% neq 0 (
    echo 編譯失敗
    exit /b 1
)

REM 執行測試
echo === 執行測試 ===
call mvn test -B -Dmaven.test.failure.ignore=true
if %ERRORLEVEL% neq 0 (
    echo 測試階段有問題，但繼續執行
)

echo === 建置完成 ===
```

### 📊 後置動作配置

#### 5.7 測試結果發佈

**JUnit 測試報告：**

```yaml
# JUnit 後置動作設定
junit_reports:
  test_results_xml: "target/surefire-reports/*.xml"
  keep_long_stdio: true
  test_data_publishers:
    - claim_test_data_publisher
    - attachment_publisher
  
options:
  allow_empty_results: false
  skip_publishing_checks: false
  skip_marking_build_unstable: false
```

**測試趨勢圖表：**

```groovy
// 透過 Script Console 自訂測試報告
import hudson.tasks.junit.*
import hudson.model.*

def job = Jenkins.instance.getItem("java-tutorial-build")
def testResultAction = job.getLastBuild()?.getAction(TestResultAction.class)

if (testResultAction) {
    println "測試統計："
    println "總測試數: ${testResultAction.totalCount}"
    println "失敗測試: ${testResultAction.failCount}"
    println "跳過測試: ${testResultAction.skipCount}"
    println "成功率: ${((testResultAction.totalCount - testResultAction.failCount) * 100 / testResultAction.totalCount).round(2)}%"
}
```

#### 5.8 產物保存

**Artifact 保存設定：**

```yaml
# 產物保存配置
archive_artifacts:
  files: |
    target/*.jar
    target/site/**/*
    logs/*.log
  excludes: |
    target/*-sources.jar
    target/*-javadoc.jar
  fingerprint: true
  only_if_successful: false
  default_excludes: true
  case_sensitive: true
```

**進階產物管理：**

```groovy
// 自動清理舊產物腳本
import hudson.model.*
import jenkins.model.*

def maxBuildsToKeep = 10
def job = Jenkins.instance.getItem("java-tutorial-build")

job.builds.findAll { build ->
    build.number <= (job.lastBuild.number - maxBuildsToKeep)
}.each { build ->
    println "清理建置 #${build.number} 的產物"
    build.artifacts.each { artifact ->
        artifact.file.delete()
    }
}
```

#### 5.9 通知設定

**Email 通知配置：**

```yaml
# Email 擴展通知設定
email_notification:
  recipients:
    - developer@company.com
    - team-lead@company.com
  
  triggers:
    - always: false
    - failure: true
    - recovery: true
    - unstable: true
    - first_failure: true
    - fixed: true
  
  content:
    subject: "Jenkins 建置通知: $PROJECT_NAME - $BUILD_STATUS"
    body: |
      專案: $PROJECT_NAME
      建置編號: $BUILD_NUMBER
      建置狀態: $BUILD_STATUS
      建置時間: $BUILD_TIMESTAMP
      Git 版本: $GIT_COMMIT
      
      變更摘要:
      $CHANGES
      
      詳細資訊: $BUILD_URL
      
      Console 輸出: $BUILD_URL/console
```

### 💡 實務案例

#### 案例：Java Spring Boot 專案建置

**情境**：為 Spring Boot 專案建立完整的 Freestyle 建置流程

**專案結構：**

```
java-spring-boot-app/
├── src/
│   ├── main/java/
│   └── test/java/
├── pom.xml
├── Dockerfile
└── README.md
```

**完整配置範例：**

```yaml
# Job 設定：spring-boot-build
general:
  name: "spring-boot-build"
  description: "Spring Boot 應用程式自動化建置"
  
scm:
  git:
    url: "https://github.com/company/spring-boot-app.git"
    branch: "*/develop"
    credentials: "github-token"
    
triggers:
  scm_polling: "H/5 * * * *"  # 每 5 分鐘檢查一次
  
build_environment:
  timeout: 20  # 20 分鐘超時
  delete_workspace: true
  
environment_variables:
  SPRING_PROFILES_ACTIVE: "test"
  MAVEN_OPTS: "-Xmx1g"
  
build_steps:
  - maven:
      goals: "clean compile"
      properties:
        maven.test.skip: true
        
  - maven:
      goals: "test"
      properties:
        maven.test.failure.ignore: true
        spring.profiles.active: test
        
  - maven:
      goals: "package"
      properties:
        maven.test.skip: true
        
  - shell: |
      echo "建置 Docker 映像檔"
      docker build -t spring-boot-app:${BUILD_NUMBER} .
      docker tag spring-boot-app:${BUILD_NUMBER} spring-boot-app:latest

post_build:
  archive_artifacts:
    files: "target/*.jar,Dockerfile"
    
  junit:
    results: "target/surefire-reports/*.xml"
    
  email:
    recipients: "dev-team@company.com"
    send_to_requester: true
```

**建置腳本完整版：**

```bash
#!/bin/bash
# spring-boot-build.sh

set -e
export LANG=en_US.UTF-8

echo "=== Spring Boot 專案建置開始 ==="
echo "建置編號: ${BUILD_NUMBER}"
echo "Git 分支: ${GIT_BRANCH}"
echo "Git 版本: ${GIT_COMMIT}"

# 1. 環境準備
echo "=== 環境準備 ==="
java -version
mvn --version
docker --version

# 設定 Maven 本地倉庫
export MAVEN_CONFIG="${WORKSPACE}/.mvn"
mkdir -p ${MAVEN_CONFIG}

# 2. 原始碼分析
echo "=== 原始碼分析 ==="
echo "Java 檔案數量: $(find src/main/java -name "*.java" | wc -l)"
echo "測試檔案數量: $(find src/test/java -name "*.java" | wc -l)"

# 3. 依賴下載
echo "=== 下載依賴 ==="
mvn dependency:resolve -B -q

# 4. 編譯
echo "=== 編譯專案 ==="
mvn clean compile -B -V \
    -Dmaven.compiler.showWarnings=true \
    -Dmaven.compiler.showDeprecation=true

# 5. 單元測試
echo "=== 執行單元測試 ==="
mvn test -B \
    -Dmaven.test.failure.ignore=true \
    -Dspring.profiles.active=test \
    -Djunit.jupiter.execution.parallel.enabled=true

# 6. 程式碼覆蓋率
if [ -f "pom.xml" ] && grep -q "jacoco" pom.xml; then
    echo "=== 生成程式碼覆蓋率報告 ==="
    mvn jacoco:report
fi

# 7. 打包
echo "=== 打包應用程式 ==="
mvn package -B -DskipTests=true

# 8. Docker 映像檔
if [ -f "Dockerfile" ]; then
    echo "=== 建置 Docker 映像檔 ==="
    APP_VERSION=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout)
    docker build -t spring-boot-app:${APP_VERSION} .
    docker tag spring-boot-app:${APP_VERSION} spring-boot-app:${BUILD_NUMBER}
    
    echo "Docker 映像檔建置完成:"
    docker images | grep spring-boot-app
fi

# 9. 建置摘要
echo "=== 建置摘要 ==="
if [ -d "target" ]; then
    echo "JAR 檔案:"
    ls -la target/*.jar 2>/dev/null || echo "無 JAR 檔案"
    
    echo "建置產物大小:"
    du -sh target/ 2>/dev/null || echo "無 target 目錄"
fi

echo "=== 建置完成 ==="
```

### ⚠️ 注意事項

1. **效能優化**：
   - 適當設定建置保留策略
   - 使用 Maven 本地倉庫快取
   - 避免不必要的 clean 操作

2. **安全考量**：
   - 敏感資訊使用憑證管理
   - 限制 Job 執行權限
   - 定期檢查腳本內容

3. **維護性**：
   - 使用有意義的命名規則
   - 添加充分的註解和文件
   - 建立標準化的建置模板

4. **錯誤處理**：
   - 適當的錯誤處理和重試機制
   - 清楚的錯誤訊息
   - 失敗時的清理動作

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Job 建立與配置 | Freestyle Project 設定、建置步驟 |
| 原始碼管理 | Git 整合、分支策略、憑證管理 |
| 建置觸發 | Cron 語法、SCM 輪詢、Webhook |
| 後置動作 | 產物保存、測試報告、通知設定 |

### 📝 練習作業

1. **基礎練習**：建立一個簡單的 Java Hello World 專案建置
2. **進階練習**：設定包含測試報告和程式碼覆蓋率的完整建置
3. **實務練習**：建立多環境部署的建置流程

---

## 第6章 憑證與密碼管理

### 🎯 學習目標

- 掌握 Jenkins 憑證管理系統
- 了解不同類型憑證的使用場景
- 學會安全地管理敏感資訊
- 建立企業級憑證管理策略

### 📚 核心概念

#### 6.1 憑證管理系統架構

Jenkins 憑證管理提供了安全存儲和使用敏感資訊的機制，包括密碼、API 金鑰、SSH 金鑰、憑證檔案等。

```mermaid
graph TD
    A[Credentials Plugin] --> B[Credential Stores]
    B --> C[System Store]
    B --> D[User Store]
    B --> E[Folder Store]
    
    C --> F[Global Credentials]
    D --> G[User-specific Credentials]
    E --> H[Folder-level Credentials]
    
    subgraph "Credential Types"
        I[Username/Password]
        J[SSH Username/Private Key]
        K[Secret Text/File]
        L[Certificate]
        M[Docker Registry]
    end
    
    F --> I
    F --> J
    F --> K
    G --> L
    H --> M
```

#### 6.2 憑證類型與使用場景

| 憑證類型 | 使用場景 | 安全等級 | 範例 |
|----------|----------|----------|------|
| **Username/Password** | 資料庫連線、HTTP 認證 | 中等 | Git HTTPS、數據庫 |
| **SSH Username/Private Key** | Git SSH、遠端伺服器 | 高 | GitHub SSH、部署伺服器 |
| **Secret Text** | API Token、密碼 | 高 | GitHub Token、Slack Token |
| **Secret File** | 設定檔、憑證檔 | 高 | SSL 憑證、設定檔 |
| **Certificate** | SSL/TLS 憑證 | 最高 | HTTPS 客戶端憑證 |

#### 6.3 憑證作用域管理

```mermaid
graph LR
    A[Global] --> B[System-wide Access]
    C[User] --> D[User-specific Access]
    E[Project] --> F[Project-level Access]
    
    B --> G[All Jobs]
    B --> H[All Users]
    
    D --> I[Personal Jobs Only]
    
    F --> J[Folder Jobs Only]
    F --> K[Restricted Access]
    
    style A fill:#ff9999
    style C fill:#99ff99
    style E fill:#ffff99
```

### 🛠️ 憑證建立與管理

#### 6.4 建立 Git 存取憑證

**GitHub Personal Access Token：**

```groovy
// 透過 Script Console 建立 GitHub Token
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import hudson.util.Secret
import jenkins.model.Jenkins

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

// 建立 GitHub Personal Access Token
def githubToken = new StringCredentialsImpl(
    CredentialsScope.GLOBAL,
    "github-pat",
    "GitHub Personal Access Token",
    Secret.fromString("ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
)

store.addCredentials(domain, githubToken)
println "GitHub Personal Access Token 建立完成"
```

**SSH 金鑰憑證：**

```groovy
// 建立 SSH 金鑰憑證
import com.cloudbees.jenkins.plugins.sshcredentials.impl.*
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.domains.*

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

// 從檔案讀取私鑰
def privateKeyFile = new File("/home/jenkins/.ssh/id_rsa")
def privateKey = privateKeyFile.text

def sshKey = new BasicSSHUserPrivateKey(
    CredentialsScope.GLOBAL,
    "github-ssh",
    "jenkins",  // username
    new BasicSSHUserPrivateKey.DirectEntryPrivateKeySource(privateKey),
    "",  // passphrase
    "GitHub SSH Key for Jenkins"
)

store.addCredentials(domain, sshKey)
println "SSH 金鑰憑證建立完成"
```

#### 6.5 資料庫連線憑證

**MySQL 資料庫憑證：**

```groovy
// 建立資料庫連線憑證
import com.cloudbees.plugins.credentials.impl.*
import hudson.util.Secret

def dbCredentials = new UsernamePasswordCredentialsImpl(
    CredentialsScope.GLOBAL,
    "mysql-db",
    "MySQL Database Connection",
    "app_user",  // username
    "secure_password_123"  // password
)

store.addCredentials(domain, dbCredentials)
println "資料庫憑證建立完成"

// 安全連線字串範例
def connectionString = "jdbc:mysql://db.company.com:3306/app_db"
def secretConnectionString = new StringCredentialsImpl(
    CredentialsScope.GLOBAL,
    "mysql-connection-string",
    "MySQL Connection String",
    Secret.fromString(connectionString)
)

store.addCredentials(domain, secretConnectionString)
```

#### 6.6 API 金鑰管理

**第三方服務 API 金鑰：**

```groovy
// 批量建立 API 金鑰
def apiKeys = [
    "slack-webhook": "https://hooks.slack.com/services/YOUR_WORKSPACE/YOUR_CHANNEL/YOUR_TOKEN",
    "sonarqube-token": "squ_YOUR_SONARQUBE_TOKEN_HERE",
    "docker-hub-token": "dckr_pat_YOUR_DOCKER_TOKEN_HERE",
    "aws-access-key": "AKIA_YOUR_AWS_ACCESS_KEY",
    "azure-client-secret": "YOUR-AZURE-CLIENT-SECRET-HERE"
]

apiKeys.each { id, token ->
    def apiCredential = new StringCredentialsImpl(
        CredentialsScope.GLOBAL,
        id,
        "${id.replace('-', ' ').toUpperCase()} API Token",
        Secret.fromString(token)
    )
    
    store.addCredentials(domain, apiCredential)
    println "已建立 ${id} API 憑證"
}
```

#### 6.7 憑證檔案管理

**SSL 憑證和設定檔：**

```groovy
// 建立憑證檔案
import org.jenkinsci.plugins.plaincredentials.impl.*
import hudson.util.Secret

// SSL 憑證檔案
def sslCertFile = new File("/etc/ssl/certs/app.company.com.pem")
def sslCertCredential = new FileCredentialsImpl(
    CredentialsScope.GLOBAL,
    "ssl-cert-file",
    "SSL Certificate File",
    sslCertFile.name,
    SecretBytes.fromBytes(sslCertFile.bytes)
)

// Kubernetes 設定檔
def kubeConfigFile = new File("/home/jenkins/.kube/config")
def kubeConfigCredential = new FileCredentialsImpl(
    CredentialsScope.GLOBAL,
    "kube-config",
    "Kubernetes Config File",
    "config",
    SecretBytes.fromBytes(kubeConfigFile.bytes)
)

store.addCredentials(domain, sslCertCredential)
store.addCredentials(domain, kubeConfigCredential)
println "憑證檔案建立完成"
```

### 📊 憑證使用與整合

#### 6.8 在 Freestyle Job 中使用憑證

**環境變數注入：**

```yaml
# Freestyle Job 中的憑證使用
build_environment:
  bindings:
    - credential_id: "github-pat"
      variable: "GITHUB_TOKEN"
    - credential_id: "mysql-db"
      username_variable: "DB_USER"
      password_variable: "DB_PASS"
    - credential_id: "slack-webhook"
      variable: "SLACK_URL"
```

**Shell 腳本中使用憑證：**

```bash
#!/bin/bash
# 在建置腳本中使用憑證

echo "=== 使用憑證進行 Git 操作 ==="
# GitHub Token 已透過環境變數注入為 GITHUB_TOKEN
git config --global credential.helper store
echo "https://jenkins:${GITHUB_TOKEN}@github.com" > ~/.git-credentials

echo "=== 使用資料庫憑證 ==="
# 資料庫憑證已注入為 DB_USER 和 DB_PASS
mysql -h db.company.com -u ${DB_USER} -p${DB_PASS} app_db <<EOF
SELECT COUNT(*) FROM users;
EOF

echo "=== 發送 Slack 通知 ==="
# Slack Webhook URL 已注入為 SLACK_URL
curl -X POST "${SLACK_URL}" \
     -H 'Content-type: application/json' \
     --data "{\"text\":\"建置 #${BUILD_NUMBER} 完成\"}"
```

#### 6.9 Pipeline 中的憑證使用

**Declarative Pipeline 憑證綁定：**

```groovy
pipeline {
    agent any
    
    environment {
        // 直接使用憑證 ID
        GITHUB_TOKEN = credentials('github-pat')
        
        // 分別取得使用者名稱和密碼
        DB_CREDS = credentials('mysql-db')
    }
    
    stages {
        stage('Checkout') {
            steps {
                // 使用 SSH 金鑰
                git credentialsId: 'github-ssh',
                    url: 'git@github.com:company/java-tutorial.git'
            }
        }
        
        stage('Build') {
            steps {
                withCredentials([
                    string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN'),
                    usernamePassword(credentialsId: 'nexus-deploy', 
                                   usernameVariable: 'NEXUS_USER',
                                   passwordVariable: 'NEXUS_PASS')
                ]) {
                    sh '''
                        mvn clean package sonar:sonar \
                            -Dsonar.login=${SONAR_TOKEN}
                        
                        mvn deploy \
                            -Dnexus.username=${NEXUS_USER} \
                            -Dnexus.password=${NEXUS_PASS}
                    '''
                }
            }
        }
        
        stage('Deploy') {
            steps {
                withCredentials([file(credentialsId: 'kube-config', variable: 'KUBECONFIG')]) {
                    sh '''
                        kubectl apply -f k8s/deployment.yaml
                        kubectl rollout status deployment/java-tutorial
                    '''
                }
            }
        }
    }
}
```

### 🔒 安全最佳實務

#### 6.10 憑證安全策略

**權限控制原則：**

```groovy
// 實施最小權限原則
import com.cloudbees.plugins.credentials.*
import hudson.security.*

// 建立角色基礎的憑證存取控制
def strategy = new ProjectMatrixAuthorizationStrategy()

// 開發者角色 - 只能查看特定憑證
strategy.add(CredentialsProvider.VIEW, "developers")
strategy.add(CredentialsProvider.USE_ITEM, "developers")

// 管理員角色 - 完整憑證管理權限
strategy.add(CredentialsProvider.CREATE, "admins")
strategy.add(CredentialsProvider.UPDATE, "admins")
strategy.add(CredentialsProvider.DELETE, "admins")
strategy.add(CredentialsProvider.MANAGE_DOMAINS, "admins")

Jenkins.instance.setAuthorizationStrategy(strategy)
```

**憑證輪替自動化：**

```groovy
// 憑證過期檢查和通知
import com.cloudbees.plugins.credentials.*
import java.time.*
import java.time.temporal.ChronoUnit

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

def expiringCredentials = []
def now = Instant.now()

store.getCredentials(domain).each { credential ->
    if (credential.hasProperty('expirationDate')) {
        def expirationDate = credential.expirationDate
        if (expirationDate && ChronoUnit.DAYS.between(now, expirationDate.toInstant()) <= 30) {
            expiringCredentials.add([
                id: credential.id,
                description: credential.description,
                daysUntilExpiry: ChronoUnit.DAYS.between(now, expirationDate.toInstant())
            ])
        }
    }
}

if (expiringCredentials.size() > 0) {
    println "即將過期的憑證："
    expiringCredentials.each { cred ->
        println "- ${cred.description} (${cred.id}): ${cred.daysUntilExpiry} 天後過期"
    }
    
    // 發送通知郵件
    def emailSubject = "Jenkins 憑證即將過期通知"
    def emailBody = "以下憑證即將過期，請及時更新：\n\n" + 
                   expiringCredentials.collect { 
                       "- ${it.description}: ${it.daysUntilExpiry} 天後過期" 
                   }.join('\n')
    
    // 這裡可以整合郵件發送邏輯
}
```

#### 6.11 憑證備份與復原

**憑證匯出腳本：**

```groovy
// 憑證備份腳本
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.domains.*
import groovy.json.JsonBuilder
import java.text.SimpleDateFormat

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()

def credentialsList = []
def dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")

store.getCredentials(domain).each { credential ->
    def credInfo = [
        id: credential.id,
        description: credential.description,
        scope: credential.scope.toString(),
        type: credential.class.simpleName,
        exportTime: dateFormat.format(new Date())
    ]
    
    // 不匯出實際的敏感資料，只匯出結構資訊
    switch (credential.class.simpleName) {
        case 'UsernamePasswordCredentialsImpl':
            credInfo.username = credential.username
            credInfo.hasPassword = credential.password != null
            break
        case 'StringCredentialsImpl':
            credInfo.hasSecret = credential.secret != null
            break
        case 'BasicSSHUserPrivateKey':
            credInfo.username = credential.username
            credInfo.hasPrivateKey = credential.privateKey != null
            break
    }
    
    credentialsList.add(credInfo)
}

def backupData = [
    exportDate: dateFormat.format(new Date()),
    jenkinsVersion: Jenkins.getVersion(),
    credentialsCount: credentialsList.size(),
    credentials: credentialsList
]

def json = new JsonBuilder(backupData)
def backupFile = new File("${System.getProperty('JENKINS_HOME')}/credentials-backup-${new Date().format('yyyyMMdd')}.json")
backupFile.text = json.toPrettyString()

println "憑證結構備份完成: ${backupFile.absolutePath}"
println "備份了 ${credentialsList.size()} 個憑證的結構資訊"
```

### 💡 實務案例

#### 案例：企業級憑證管理架構

**情境**：為大型企業建立分層憑證管理體系

**解決方案架構：**

```mermaid
graph TD
    A[企業憑證管理] --> B[全域層級]
    A --> C[部門層級]
    A --> D[專案層級]
    
    B --> E[基礎設施憑證]
    B --> F[企業服務憑證]
    
    C --> G[部門 Git 憑證]
    C --> H[部門工具憑證]
    
    D --> I[專案資料庫憑證]
    D --> J[專案 API 憑證]
    
    subgraph "管理策略"
        K[自動輪替]
        L[權限控制]
        M[稽核日誌]
        N[災難復原]
    end
```

**實施配置：**

```groovy
// 企業憑證管理設定
def setupEnterpriseCredentials() {
    def domain = Domain.global()
    def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()
    
    // 1. 全域基礎設施憑證
    def infrastructureCredentials = [
        [
            id: "ldap-service-account",
            type: "userpass",
            username: "svc-jenkins",
            password: System.getenv("LDAP_SERVICE_PASSWORD"),
            description: "LDAP Service Account for Authentication"
        ],
        [
            id: "backup-storage-key",
            type: "secret",
            secret: System.getenv("BACKUP_STORAGE_ACCESS_KEY"),
            description: "Backup Storage Access Key"
        ]
    ]
    
    // 2. 開發工具憑證
    def developmentCredentials = [
        [
            id: "github-enterprise-token",
            type: "secret",
            secret: System.getenv("GITHUB_ENTERPRISE_TOKEN"),
            description: "GitHub Enterprise API Token"
        ],
        [
            id: "sonarqube-enterprise-token",
            type: "secret", 
            secret: System.getenv("SONARQUBE_TOKEN"),
            description: "SonarQube Enterprise Token"
        ],
        [
            id: "nexus-repository-creds",
            type: "userpass",
            username: "jenkins-deploy",
            password: System.getenv("NEXUS_DEPLOY_PASSWORD"),
            description: "Nexus Repository Manager Credentials"
        ]
    ]
    
    // 3. 雲端服務憑證
    def cloudCredentials = [
        [
            id: "aws-deployment-role",
            type: "secret",
            secret: System.getenv("AWS_ROLE_ARN"),
            description: "AWS Deployment Role ARN"
        ],
        [
            id: "azure-service-principal",
            type: "userpass",
            username: System.getenv("AZURE_CLIENT_ID"),
            password: System.getenv("AZURE_CLIENT_SECRET"),
            description: "Azure Service Principal"
        ]
    ]
    
    // 建立憑證
    [infrastructureCredentials, developmentCredentials, cloudCredentials].flatten().each { credConfig ->
        def credential
        switch (credConfig.type) {
            case "userpass":
                credential = new UsernamePasswordCredentialsImpl(
                    CredentialsScope.GLOBAL,
                    credConfig.id,
                    credConfig.description,
                    credConfig.username,
                    credConfig.password
                )
                break
            case "secret":
                credential = new StringCredentialsImpl(
                    CredentialsScope.GLOBAL,
                    credConfig.id,
                    credConfig.description,
                    Secret.fromString(credConfig.secret)
                )
                break
        }
        
        if (credential) {
            store.addCredentials(domain, credential)
            println "已建立憑證: ${credConfig.id}"
        }
    }
    
    Jenkins.instance.save()
    println "企業憑證管理設定完成"
}

// 執行設定
setupEnterpriseCredentials()
```

### ⚠️ 注意事項

1. **安全原則**：
   - 永遠不要在 Console Output 中顯示敏感資訊
   - 使用最小權限原則分配憑證存取權
   - 定期輪替重要憑證

2. **效能考量**：
   - 避免在高頻率執行的 Job 中重複建立憑證
   - 使用憑證快取機制
   - 監控憑證讀取效能

3. **合規要求**：
   - 記錄憑證存取日誌
   - 實施憑證稽核機制
   - 符合企業安全政策

4. **災難復原**：
   - 定期備份憑證設定
   - 建立憑證復原程序
   - 測試災難復原流程

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| 憑證管理 | 憑證類型、作用域、安全策略 |
| 安全實務 | 權限控制、憑證輪替、稽核 |
| 整合應用 | Pipeline 憑證使用、環境變數注入 |

### 📝 練習作業

1. **基礎練習**：建立 GitHub、資料庫和 API 憑證
2. **進階練習**：實施憑證過期監控和自動通知
3. **實務練習**：設計企業級憑證管理和權限控制策略

---

## 第7章 Git 整合與版本控制

### 🎯 學習目標

- 掌握 Jenkins 與 Git 的深度整合
- 了解分支策略和工作流程
- 學會設定 Git Hook 和自動觸發
- 建立多分支開發的建置策略

### 📚 核心概念

#### 7.1 Git 整合架構

Jenkins 透過 Git Plugin 提供完整的版本控制整合，支援多種 Git 託管平台和工作流程。

```mermaid
graph TD
    A[Git Repository] --> B[Jenkins Git Integration]
    B --> C[SCM Polling]
    B --> D[Webhook Triggers]
    B --> E[Branch Discovery]
    
    C --> F[Scheduled Checks]
    D --> G[Push Events]
    D --> H[Pull Request Events]
    E --> I[Multibranch Pipeline]
    
    subgraph "Git Platforms"
        J[GitHub]
        K[GitLab]
        L[Bitbucket]
        M[Azure DevOps]
    end
    
    B --> J
    B --> K
    B --> L
    B --> M
    
    subgraph "Authentication"
        N[SSH Keys]
        O[Personal Tokens]
        P[OAuth Apps]
    end
    
    B --> N
    B --> O
    B --> P
```

#### 7.2 Git 工作流程與分支策略

**常見分支策略比較：**

| 策略 | 適用場景 | 分支結構 | Jenkins 建置策略 |
|------|----------|----------|------------------|
| **Git Flow** | 大型專案、定期發布 | master/develop/feature/release/hotfix | 針對每種分支類型設定不同建置流程 |
| **GitHub Flow** | 持續部署、敏捷開發 | master/feature | 簡化的建置和部署流程 |
| **GitLab Flow** | 混合環境、多環境部署 | master/production/pre-production | 環境特定的建置配置 |
| **Trunk-based** | 高頻率整合 | master/short-lived-feature | 快速整合和反饋機制 |

```mermaid
gitgraph
    commit id: "Initial"
    branch develop
    checkout develop
    commit id: "Dev Setup"
    
    branch feature/user-auth
    checkout feature/user-auth
    commit id: "Add login"
    commit id: "Add logout"
    
    checkout develop
    merge feature/user-auth
    commit id: "Integration test"
    
    branch release/v1.0
    checkout release/v1.0
    commit id: "Release prep"
    
    checkout main
    merge release/v1.0
    commit id: "v1.0 Release"
    
    checkout develop
    merge main
```

#### 7.3 Git 設定最佳實務

**全域 Git 設定：**

```groovy
// 透過 Script Console 設定 Git 全域配置
import hudson.plugins.git.*
import jenkins.model.*

def jenkins = Jenkins.getInstance()
def gitSCM = jenkins.getDescriptor("hudson.plugins.git.GitSCM")

// 設定全域 Git 使用者資訊
gitSCM.setGlobalConfigName("Jenkins CI/CD")
gitSCM.setGlobalConfigEmail("jenkins@company.com")

// 設定 Git 行為
gitSCM.setCreateAccountBasedOnEmail(false)
gitSCM.setUseExistingAccountWithSameEmail(true)

// 設定 Git 工具路徑
def gitTool = jenkins.getDescriptor("hudson.plugins.git.GitTool")
def installations = [
    new GitTool("Default", "/usr/bin/git", []),
    new GitTool("Git-2.40", "/usr/local/git-2.40/bin/git", [])
]
gitTool.setInstallations(installations as GitTool[])

jenkins.save()
println "Git 全域設定完成"
```

### 🛠️ Git 專案設定

#### 7.4 單一分支專案設定

**基本 Git 設定：**

```yaml
# Freestyle Job Git 設定
source_code_management:
  git:
    repositories:
      - url: "https://github.com/company/java-tutorial.git"
        credentials_id: "github-pat"
        name: "origin"
    
    branches_to_build:
      - "*/master"
      - "*/main"
    
    browser: "github"
    browser_url: "https://github.com/company/java-tutorial"
    
    additional_behaviours:
      - clean_before_checkout: true
      - checkout_to_subdirectory: "source"
      - clone_option:
          shallow: true
          depth: 10
          timeout: 20
      - submodule_option:
          disable_submodules: false
          recursive_submodules: true
          timeout: 20
```

**進階 Git 設定腳本：**

```bash
#!/bin/bash
# git-setup.sh - Git 環境設定腳本

set -e

echo "=== Git 環境設定 ==="

# 1. 檢查 Git 版本
echo "Git 版本檢查:"
git --version

# 2. 設定 Git 配置
echo "設定 Git 全域配置:"
git config --global user.name "Jenkins CI"
git config --global user.email "jenkins@company.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.autocrlf input

# 3. 設定 Git 憑證快取
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    git config --global credential.helper 'cache --timeout=3600'
elif [[ "$OSTYPE" == "darwin"* ]]; then
    git config --global credential.helper osxkeychain
fi

# 4. 設定 Git 別名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --decorate"

# 5. 驗證設定
echo "Git 配置驗證:"
git config --list | grep -E "(user\.|init\.|pull\.|core\.)"

echo "=== Git 環境設定完成 ==="
```

#### 7.5 多分支專案設定

**Multibranch Pipeline 設定：**

```groovy
// 建立 Multibranch Pipeline
import jenkins.branch.*
import jenkins.plugins.git.*
import org.jenkinsci.plugins.workflow.multibranch.*

def jenkins = Jenkins.getInstance()

// 建立 Multibranch Pipeline Job
def job = new WorkflowMultiBranchProject(jenkins, "java-tutorial-multibranch")

// 設定 Git 分支來源
def gitSource = new GitSCMSource(
    "java-tutorial-git",  // source id
    "https://github.com/company/java-tutorial.git",  // repository url
    "github-pat",  // credentials id
    "*",  // includes - 包含所有分支
    "",   // excludes - 排除的分支 
    false // ignore on push notifications
)

// 設定分支探索策略
def branchDiscoveryTrait = new jenkins.plugins.git.traits.BranchDiscoveryTrait()
def originPRDiscoveryTrait = new jenkins.plugins.git.traits.OriginPullRequestDiscoveryTrait(1) // 只建置 merge 後的結果

gitSource.setTraits([
    branchDiscoveryTrait,
    originPRDiscoveryTrait,
    new jenkins.plugins.git.traits.CleanBeforeCheckoutTrait(),
    new jenkins.plugins.git.traits.CloneOptionTrait(false, false, "", 10)
])

// 設定 Branch Source
def branchSourceCriteria = new jenkins.branch.DefaultBranchPropertyStrategy(new jenkins.branch.BranchProperty[0])
def branchSource = new BranchSource(gitSource, branchSourceCriteria)

job.getSourcesList().add(branchSource)

// 設定 Jenkinsfile 路徑
job.setProjectFactory(new org.jenkinsci.plugins.workflow.multibranch.WorkflowBranchProjectFactory())

// 設定建置觸發器
def periodicFolderTrigger = new com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger("5m")
job.addTrigger(periodicFolderTrigger)

jenkins.add(job, job.name)
jenkins.save()

println "Multibranch Pipeline 建立完成: ${job.name}"
```

#### 7.6 分支特定建置策略

**分支條件建置 Jenkinsfile：**

```groovy
// Jenkinsfile - 分支條件建置
pipeline {
    agent any
    
    environment {
        BRANCH_TYPE = "${env.BRANCH_NAME.startsWith('feature/') ? 'feature' : 
                       env.BRANCH_NAME.startsWith('release/') ? 'release' :
                       env.BRANCH_NAME.startsWith('hotfix/') ? 'hotfix' :
                       env.BRANCH_NAME == 'master' ? 'master' :
                       env.BRANCH_NAME == 'develop' ? 'develop' : 'other'}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    env.GIT_COMMIT_SHORT = sh(
                        script: "git rev-parse --short HEAD",
                        returnStdout: true
                    ).trim()
                    
                    env.GIT_COMMIT_MESSAGE = sh(
                        script: "git log -1 --pretty=%B",
                        returnStdout: true
                    ).trim()
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    echo "建置分支類型: ${env.BRANCH_TYPE}"
                    echo "Git 版本: ${env.GIT_COMMIT_SHORT}"
                    echo "提交訊息: ${env.GIT_COMMIT_MESSAGE}"
                    
                    // 基本建置 - 所有分支都執行
                    sh 'mvn clean compile -B'
                }
            }
        }
        
        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'mvn test -B'
                    }
                    post {
                        always {
                            junit 'target/surefire-reports/*.xml'
                        }
                    }
                }
                
                stage('Integration Tests') {
                    when {
                        anyOf {
                            environment name: 'BRANCH_TYPE', value: 'develop'
                            environment name: 'BRANCH_TYPE', value: 'release'
                            environment name: 'BRANCH_TYPE', value: 'master'
                        }
                    }
                    steps {
                        sh 'mvn verify -P integration-tests -B'
                    }
                }
            }
        }
        
        stage('Code Quality') {
            when {
                not {
                    environment name: 'BRANCH_TYPE', value: 'feature'
                }
            }
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    sh '''
                        mvn sonar:sonar \
                            -Dsonar.login=${SONAR_TOKEN} \
                            -Dsonar.branch.name=${BRANCH_NAME}
                    '''
                }
            }
        }
        
        stage('Package') {
            when {
                anyOf {
                    environment name: 'BRANCH_TYPE', value: 'develop'
                    environment name: 'BRANCH_TYPE', value: 'release'
                    environment name: 'BRANCH_TYPE', value: 'master'
                    environment name: 'BRANCH_TYPE', value: 'hotfix'
                }
            }
            steps {
                sh 'mvn package -DskipTests -B'
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
        }
        
        stage('Deploy to Dev') {
            when {
                environment name: 'BRANCH_TYPE', value: 'develop'
            }
            steps {
                echo "部署到開發環境"
                sh './scripts/deploy-dev.sh'
            }
        }
        
        stage('Deploy to Staging') {
            when {
                environment name: 'BRANCH_TYPE', value: 'release'
            }
            steps {
                echo "部署到測試環境"
                sh './scripts/deploy-staging.sh'
            }
        }
        
        stage('Deploy to Production') {
            when {
                anyOf {
                    environment name: 'BRANCH_TYPE', value: 'master'
                    environment name: 'BRANCH_TYPE', value: 'hotfix'
                }
            }
            steps {
                script {
                    def deployApproval = input(
                        message: '確認部署到生產環境？',
                        ok: '部署',
                        parameters: [
                            choice(
                                name: 'DEPLOY_ENVIRONMENT',
                                choices: ['production', 'production-blue', 'production-green'],
                                description: '選擇部署目標環境'
                            )
                        ]
                    )
                    
                    echo "部署到生產環境: ${deployApproval}"
                    sh "./scripts/deploy-prod.sh ${deployApproval}"
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        
        success {
            script {
                if (env.BRANCH_TYPE in ['master', 'develop']) {
                    slackSend(
                        channel: '#ci-cd',
                        color: 'good',
                        message: ":white_check_mark: 建置成功 - ${env.JOB_NAME} #${env.BUILD_NUMBER}\n" +
                                "分支: ${env.BRANCH_NAME}\n" +
                                "提交: ${env.GIT_COMMIT_SHORT}\n" +
                                "訊息: ${env.GIT_COMMIT_MESSAGE}"
                    )
                }
            }
        }
        
        failure {
            slackSend(
                channel: '#ci-cd',
                color: 'danger',
                message: ":x: 建置失敗 - ${env.JOB_NAME} #${env.BUILD_NUMBER}\n" +
                        "分支: ${env.BRANCH_NAME}\n" +
                        "提交: ${env.GIT_COMMIT_SHORT}\n" +
                        "詳情: ${env.BUILD_URL}"
            )
        }
    }
}
```

### 📊 Git Hook 與自動觸發

#### 7.7 GitHub Webhook 設定

**GitHub Webhook 配置步驟：**

1. **在 GitHub 專案設定 Webhook**

```bash
# GitHub Webhook 設定
Payload URL: http://jenkins.company.com/github-webhook/
Content type: application/json
Secret: your-webhook-secret

Events:
- Push events
- Pull request events
- Branch or tag creation
- Branch or tag deletion
```

2. **Jenkins Webhook 接收設定**

```groovy
// 設定 GitHub Webhook
import org.jenkinsci.plugins.github.GitHubPlugin
import org.jenkinsci.plugins.github.config.GitHubPluginConfig

def gitHubConfig = GitHubPluginConfig.get()
gitHubConfig.setManageHooks(true)
gitHubConfig.setOverrideHookUrl("http://jenkins.company.com/github-webhook/")

// 設定 GitHub Server
def githubServer = new org.jenkinsci.plugins.github.config.GitHubServerConfig("github-pat")
githubServer.setName("GitHub.com")
githubServer.setApiUrl("https://api.github.com")
githubServer.setManageHooks(true)

gitHubConfig.setConfigs([githubServer])
gitHubConfig.save()

println "GitHub Webhook 設定完成"
```

3. **Webhook 安全驗證**

```groovy
// Webhook 安全驗證腳本
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import java.security.MessageDigest

def verifyGitHubWebhook(payload, signature, secret) {
    def mac = Mac.getInstance("HmacSHA1")
    def secretKey = new SecretKeySpec(secret.getBytes(), "HmacSHA1")
    mac.init(secretKey)
    
    def expectedSignature = "sha1=" + mac.doFinal(payload.getBytes()).encodeHex().toString()
    
    return MessageDigest.isEqual(
        expectedSignature.getBytes(),
        signature.getBytes()
    )
}

// 在 Pipeline 中使用
if (verifyGitHubWebhook(env.WEBHOOK_PAYLOAD, env.WEBHOOK_SIGNATURE, env.WEBHOOK_SECRET)) {
    echo "Webhook 驗證成功"
} else {
    error "Webhook 驗證失敗"
}
```

#### 7.8 Pull Request 建置

**PR 建置策略：**

```groovy
// Pull Request 建置 Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('PR Validation') {
            when {
                changeRequest()
            }
            parallel {
                stage('Code Style Check') {
                    steps {
                        sh 'mvn checkstyle:check'
                    }
                }
                
                stage('Security Scan') {
                    steps {
                        sh 'mvn spotbugs:check'
                    }
                }
                
                stage('Dependency Check') {
                    steps {
                        sh 'mvn dependency-check:check'
                    }
                }
            }
        }
        
        stage('Build & Test') {
            steps {
                sh 'mvn clean compile test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/site/jacoco',
                        reportFiles: 'index.html',
                        reportName: 'JaCoCo Coverage Report'
                    ])
                }
            }
        }
        
        stage('PR Comment') {
            when {
                changeRequest()
            }
            steps {
                script {
                    def testResults = junit testResults: 'target/surefire-reports/*.xml'
                    def comment = "## 🤖 自動化建置結果\n\n" +
                                 "**建置狀態**: ✅ 成功\n" +
                                 "**測試結果**: ${testResults.totalCount} 個測試，${testResults.failCount} 個失敗\n" +
                                 "**建置時間**: ${currentBuild.durationString}\n\n" +
                                 "[查看詳細報告](${env.BUILD_URL})"
                    
                    // 使用 GitHub API 發布評論
                    withCredentials([string(credentialsId: 'github-pat', variable: 'GITHUB_TOKEN')]) {
                        sh """
                            curl -X POST \
                                -H "Authorization: token ${GITHUB_TOKEN}" \
                                -H "Content-Type: application/json" \
                                -d '{"body": "${comment}"}' \
                                "https://api.github.com/repos/company/java-tutorial/issues/${env.CHANGE_ID}/comments"
                        """
                    }
                }
            }
        }
    }
}
```

### 💡 實務案例

#### 案例：Git Flow 自動化工作流程

**情境**：實施完整的 Git Flow 自動化建置和部署

**架構設計：**

```mermaid
graph TD
    A[Feature Branch] --> B[Feature Build]
    C[Develop Branch] --> D[Dev Build & Deploy]
    E[Release Branch] --> F[Release Build & Test]
    G[Master Branch] --> H[Production Build]
    H --> I[Production Deploy]
    
    B --> J[Code Quality Check]
    B --> K[Unit Tests]
    
    D --> L[Integration Tests]
    D --> M[Deploy to Dev Environment]
    
    F --> N[Full Test Suite]
    F --> O[Deploy to Staging]
    
    I --> P[Blue-Green Deployment]
    I --> Q[Health Check]
    
    R[Hotfix Branch] --> S[Hotfix Build]
    S --> T[Emergency Deploy]
```

**實施配置：**

```yaml
# Git Flow 自動化配置
multibranch_pipeline:
  name: "java-tutorial-gitflow"
  
  branch_strategies:
    feature_branches:
      pattern: "feature/*"
      build_steps:
        - compile
        - unit_test
        - code_quality_check
      notifications:
        - slack_channel: "#development"
        - email: "developers@company.com"
    
    develop_branch:
      pattern: "develop"
      build_steps:
        - compile
        - unit_test
        - integration_test
        - security_scan
        - deploy_to_dev
      notifications:
        - slack_channel: "#ci-cd"
        - email: "team-leads@company.com"
    
    release_branches:
      pattern: "release/*"
      build_steps:
        - compile
        - full_test_suite
        - performance_test
        - deploy_to_staging
        - manual_approval
      notifications:
        - slack_channel: "#releases"
        - email: "qa-team@company.com"
    
    master_branch:
      pattern: "master"
      build_steps:
        - compile
        - regression_test
        - security_final_check
        - deploy_to_production
        - post_deploy_verification
      notifications:
        - slack_channel: "#production"
        - email: "ops-team@company.com"
    
    hotfix_branches:
      pattern: "hotfix/*"
      build_steps:
        - compile
        - critical_tests
        - emergency_deploy
        - immediate_verification
      notifications:
        - slack_channel: "#emergency"
        - email: "all-teams@company.com"
```

### ⚠️ 注意事項

1. **分支策略**：
   - 選擇適合團隊的分支模型
   - 建立清楚的分支命名規則
   - 定期清理已合併的分支

2. **安全考量**：
   - 保護重要分支（master/main）
   - 限制強制推送權限
   - 驗證 Webhook 來源

3. **效能優化**：
   - 使用淺層克隆減少網路傳輸
   - 適當設定 Git 快取
   - 並行處理多分支建置

4. **監控與維護**：
   - 監控建置佇列長度
   - 定期檢查孤立分支
   - 清理舊的建置記錄

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Git 整合 | SCM 設定、分支策略、Webhook |
| 多分支管理 | Multibranch Pipeline、分支條件建置 |
| 自動化觸發 | Pull Request 建置、Git Hook |

### 📝 練習作業

1. **基礎練習**：設定 GitHub 專案的基本 Git 整合
2. **進階練習**：實施 Multibranch Pipeline 與 PR 建置
3. **實務練習**：建立完整的 Git Flow 自動化工作流程

---

## 第8章 Maven 建置整合

### 🎯 學習目標

- 掌握 Jenkins 與 Maven 的完整整合
- 了解 Maven 生命週期在 CI/CD 中的應用
- 學會配置多模組專案的建置策略
- 建立 Maven 建置的最佳實務

### 📚 核心概念

#### 8.1 Maven 與 Jenkins 整合架構

Maven 作為 Java 專案的標準建置工具，與 Jenkins 深度整合提供完整的自動化建置解決方案。

```mermaid
graph TD
    A[Maven Project] --> B[Jenkins Maven Integration]
    B --> C[Maven Plugin]
    B --> D[Maven Invoker Plugin]
    B --> E[Maven Deploy Plugin]
    
    C --> F[Build Lifecycle]
    F --> G[validate]
    F --> H[compile]
    F --> I[test]
    F --> J[package]
    F --> K[verify]
    F --> L[install]
    F --> M[deploy]
    
    subgraph "Maven Features in Jenkins"
        N[Dependency Management]
        O[Multi-module Support]
        P[Test Report Integration]
        Q[Artifact Publishing]
        R[Site Generation]
    end
    
    B --> N
    B --> O
    B --> P
    B --> Q
    B --> R
```

#### 8.2 Maven 生命週期與建置階段

**Maven 標準生命週期：**

| 階段 | 目的 | Jenkins 應用 | 典型耗時 |
|------|------|--------------|----------|
| **validate** | 驗證專案結構 | 專案結構檢查 | < 1 分鐘 |
| **compile** | 編譯原始碼 | 編譯錯誤檢查 | 2-5 分鐘 |
| **test** | 執行單元測試 | 測試報告生成 | 5-15 分鐘 |
| **package** | 打包成 JAR/WAR | 建立部署包 | 1-3 分鐘 |
| **verify** | 整合測試驗證 | 品質門檻檢查 | 10-30 分鐘 |
| **install** | 安裝到本地倉庫 | 依賴快取 | 1-2 分鐘 |
| **deploy** | 部署到遠端倉庫 | 制品發布 | 2-5 分鐘 |

#### 8.3 Maven 設定最佳實務

**settings.xml 配置：**

```xml
<!-- $JENKINS_HOME/.m2/settings.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 
                              http://maven.apache.org/xsd/settings-1.0.0.xsd">
    
    <!-- 本地倉庫設定 -->
    <localRepository>${JENKINS_HOME}/.m2/repository</localRepository>
    
    <!-- 離線模式 -->
    <offline>false</offline>
    
    <!-- 插件群組 -->
    <pluginGroups>
        <pluginGroup>org.sonarsource.scanner.maven</pluginGroup>
        <pluginGroup>org.jacoco</pluginGroup>
    </pluginGroups>
    
    <!-- 伺服器認證 -->
    <servers>
        <server>
            <id>nexus-snapshots</id>
            <username>${env.NEXUS_USERNAME}</username>
            <password>${env.NEXUS_PASSWORD}</password>
        </server>
        <server>
            <id>nexus-releases</id>
            <username>${env.NEXUS_USERNAME}</username>
            <password>${env.NEXUS_PASSWORD}</password>
        </server>
        <server>
            <id>sonarqube</id>
            <username>${env.SONAR_TOKEN}</username>
            <password></password>
        </server>
    </servers>
    
    <!-- 鏡像設定 -->
    <mirrors>
        <mirror>
            <id>nexus-public</id>
            <mirrorOf>central</mirrorOf>
            <name>Nexus Public Repository</name>
            <url>http://nexus.company.com:8081/repository/maven-public/</url>
        </mirror>
    </mirrors>
    
    <!-- 配置檔案 -->
    <profiles>
        <profile>
            <id>nexus</id>
            <repositories>
                <repository>
                    <id>central</id>
                    <url>http://central</url>
                    <releases><enabled>true</enabled></releases>
                    <snapshots><enabled>true</enabled></snapshots>
                </repository>
            </repositories>
            <pluginRepositories>
                <pluginRepository>
                    <id>central</id>
                    <url>http://central</url>
                    <releases><enabled>true</enabled></releases>
                    <snapshots><enabled>true</enabled></snapshots>
                </pluginRepository>
            </pluginRepositories>
        </profile>
        
        <profile>
            <id>ci-cd</id>
            <properties>
                <maven.test.failure.ignore>false</maven.test.failure.ignore>
                <maven.javadoc.skip>true</maven.javadoc.skip>
                <maven.source.skip>true</maven.source.skip>
                <skipITs>false</skipITs>
            </properties>
        </profile>
    </profiles>
    
    <!-- 啟用的配置檔案 -->
    <activeProfiles>
        <activeProfile>nexus</activeProfile>
        <activeProfile>ci-cd</activeProfile>
    </activeProfiles>
</settings>
```

### 🛠️ Jenkins Maven 專案設定

#### 8.4 Freestyle Maven 專案

**Maven 建置步驟設定：**

```yaml
# Freestyle Job Maven 設定
build_steps:
  - maven_step_1:
      goals: "clean compile"
      maven_version: "Maven-3.9"
      pom: "pom.xml"
      properties:
        maven.compiler.source: "17"
        maven.compiler.target: "17"
        project.build.sourceEncoding: "UTF-8"
      
  - maven_step_2:
      goals: "test"
      maven_version: "Maven-3.9"
      properties:
        maven.test.failure.ignore: "true"
        junit.jupiter.execution.parallel.enabled: "true"
        junit.jupiter.execution.parallel.mode.default: "concurrent"
        
  - maven_step_3:
      goals: "package"
      maven_version: "Maven-3.9"
      properties:
        maven.test.skip: "true"
        maven.javadoc.skip: "true"

post_build_actions:
  - archive_artifacts:
      artifacts: "target/*.jar,target/*.war"
      fingerprint: true
      
  - junit_report:
      test_results: "target/surefire-reports/*.xml"
      keep_long_stdio: true
      
  - jacoco_report:
      exec_pattern: "target/jacoco.exec"
      class_pattern: "target/classes"
      source_pattern: "src/main/java"
```

#### 8.5 Pipeline Maven 整合

**完整 Maven Pipeline：**

```groovy
// Jenkinsfile - Maven 完整建置流程
pipeline {
    agent any
    
    tools {
        maven 'Maven-3.9'
        jdk 'JDK-17'
    }
    
    environment {
        MAVEN_OPTS = '-Xmx2g -XX:+UseG1GC -Dmaven.repo.local=$WORKSPACE/.m2/repository'
        MAVEN_CLI_OPTS = '-B -V -e -s $JENKINS_HOME/.m2/settings.xml'
    }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '20'))
        timeout(time: 60, unit: 'MINUTES')
        skipStagesAfterUnstable()
        parallelsAlwaysFailFast()
    }
    
    stages {
        stage('Environment Setup') {
            steps {
                script {
                    // 顯示環境資訊
                    sh '''
                        echo "=== 環境資訊 ==="
                        java -version
                        mvn -version
                        echo "工作目錄: $(pwd)"
                        echo "Maven 本地倉庫: $MAVEN_OPTS"
                    '''
                    
                    // 建立必要目錄
                    sh 'mkdir -p $WORKSPACE/.m2/repository'
                }
            }
        }
        
        stage('Dependency Resolution') {
            steps {
                echo '解析並下載依賴'
                sh "mvn ${MAVEN_CLI_OPTS} dependency:resolve dependency:resolve-sources"
            }
        }
        
        stage('Code Validation') {
            parallel {
                stage('Compile') {
                    steps {
                        echo '編譯原始碼'
                        sh "mvn ${MAVEN_CLI_OPTS} clean compile"
                    }
                }
                
                stage('Validate POM') {
                    steps {
                        echo '驗證 POM 檔案'
                        sh "mvn ${MAVEN_CLI_OPTS} validate"
                    }
                }
                
                stage('Dependency Check') {
                    steps {
                        echo '檢查依賴衝突'
                        sh "mvn ${MAVEN_CLI_OPTS} dependency:analyze"
                    }
                }
            }
        }
        
        stage('Testing') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        echo '執行單元測試'
                        sh """
                            mvn ${MAVEN_CLI_OPTS} test \
                                -Dmaven.test.failure.ignore=true \
                                -Djunit.jupiter.execution.parallel.enabled=true \
                                -Djunit.jupiter.execution.parallel.mode.default=concurrent
                        """
                    }
                    post {
                        always {
                            junit 'target/surefire-reports/*.xml'
                            
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target/site/jacoco',
                                reportFiles: 'index.html',
                                reportName: 'JaCoCo Coverage Report'
                            ])
                        }
                    }
                }
                
                stage('Integration Tests') {
                    when {
                        not { changeRequest() }
                    }
                    steps {
                        echo '執行整合測試'
                        sh """
                            mvn ${MAVEN_CLI_OPTS} verify \
                                -DskipUnitTests=true \
                                -Dfailsafe.rerunFailingTestsCount=2
                        """
                    }
                    post {
                        always {
                            junit 'target/failsafe-reports/*.xml'
                        }
                    }
                }
            }
        }
        
        stage('Code Quality Analysis') {
            parallel {
                stage('SonarQube Analysis') {
                    when {
                        anyOf {
                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps {
                        withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                            sh """
                                mvn ${MAVEN_CLI_OPTS} sonar:sonar \
                                    -Dsonar.login=${SONAR_TOKEN} \
                                    -Dsonar.branch.name=${env.BRANCH_NAME}
                            """
                        }
                    }
                }
                
                stage('Code Style Check') {
                    steps {
                        sh "mvn ${MAVEN_CLI_OPTS} checkstyle:check"
                        
                        recordIssues(
                            enabledForFailure: true,
                            tools: [checkStyle(pattern: 'target/checkstyle-result.xml')]
                        )
                    }
                }
                
                stage('Security Scan') {
                    steps {
                        sh "mvn ${MAVEN_CLI_OPTS} spotbugs:check"
                        
                        recordIssues(
                            enabledForFailure: true,
                            tools: [spotBugs(pattern: 'target/spotbugsXml.xml')]
                        )
                    }
                }
            }
        }
        
        stage('Package') {
            steps {
                echo '打包應用程式'
                sh """
                    mvn ${MAVEN_CLI_OPTS} package \
                        -DskipTests=true \
                        -Dmaven.javadoc.skip=true
                """
                
                archiveArtifacts(
                    artifacts: 'target/*.jar,target/*.war',
                    fingerprint: true,
                    onlyIfSuccessful: true
                )
            }
        }
        
        stage('Documentation') {
            when {
                branch 'master'
            }
            steps {
                echo '生成專案文件'
                sh "mvn ${MAVEN_CLI_OPTS} site"
                
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'target/site',
                    reportFiles: 'index.html',
                    reportName: 'Maven Site Documentation'
                ])
            }
        }
        
        stage('Deploy to Repository') {
            when {
                anyOf {
                    branch 'master'
                    branch 'develop'
                }
            }
            steps {
                echo '部署到 Maven 倉庫'
                withCredentials([
                    usernamePassword(
                        credentialsId: 'nexus-deploy',
                        usernameVariable: 'NEXUS_USERNAME',
                        passwordVariable: 'NEXUS_PASSWORD'
                    )
                ]) {
                    sh """
                        mvn ${MAVEN_CLI_OPTS} deploy \
                            -DskipTests=true \
                            -Dnexus.username=${NEXUS_USERNAME} \
                            -Dnexus.password=${NEXUS_PASSWORD}
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo '清理工作空間'
            sh 'mvn clean'
            
            // 保留重要的建置資訊
            sh '''
                echo "=== 建置摘要 ==="
                echo "建置編號: ${BUILD_NUMBER}"
                echo "Git 版本: $(git rev-parse --short HEAD)"
                echo "建置時間: $(date)"
                
                if [ -f target/*.jar ]; then
                    echo "JAR 檔案: $(ls -la target/*.jar)"
                fi
            '''
        }
        
        success {
            script {
                if (env.BRANCH_NAME in ['master', 'develop']) {
                    emailext(
                        subject: "✅ 建置成功: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                        body: """
                            專案: ${env.JOB_NAME}
                            建置編號: ${env.BUILD_NUMBER}
                            分支: ${env.BRANCH_NAME}
                            建置時間: ${env.BUILD_TIMESTAMP}
                            
                            建置日誌: ${env.BUILD_URL}console
                            測試報告: ${env.BUILD_URL}testReport
                            程式碼覆蓋率: ${env.BUILD_URL}jacoco
                        """,
                        to: "${env.CHANGE_AUTHOR_EMAIL ?: 'dev-team@company.com'}"
                    )
                }
            }
        }
        
        failure {
            emailext(
                subject: "❌ 建置失敗: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    專案: ${env.JOB_NAME}
                    建置編號: ${env.BUILD_NUMBER}
                    分支: ${env.BRANCH_NAME}
                    失敗階段: ${env.STAGE_NAME}
                    
                    錯誤詳情: ${env.BUILD_URL}console
                    
                    請檢查建置日誌並修正問題。
                """,
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'dev-team@company.com'}"
            )
        }
        
        unstable {
            echo '建置不穩定 - 可能有測試失敗'
        }
        
        cleanup {
            cleanWs(
                cleanWhenNotBuilt: false,
                deleteDirs: true,
                disableDeferredWipeout: true,
                notFailBuild: true
            )
        }
    }
}
```

### 📊 多模組專案管理

#### 8.6 多模組專案結構

**典型多模組專案架構：**

```
enterprise-app/
├── pom.xml                    # 父 POM
├── common/                    # 共用模組
│   ├── pom.xml
│   └── src/
├── core/                      # 核心業務邏輯
│   ├── pom.xml
│   └── src/
├── web/                       # Web 層
│   ├── pom.xml
│   └── src/
├── integration-tests/         # 整合測試
│   ├── pom.xml
│   └── src/
└── distribution/              # 打包分發
    ├── pom.xml
    └── src/
```

**父 POM 設定範例：**

```xml
<!-- 父 pom.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.company</groupId>
    <artifactId>enterprise-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    
    <name>Enterprise Application</name>
    <description>多模組企業應用程式</description>
    
    <!-- 子模組定義 -->
    <modules>
        <module>common</module>
        <module>core</module>
        <module>web</module>
        <module>integration-tests</module>
        <module>distribution</module>
    </modules>
    
    <!-- 屬性定義 -->
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        
        <!-- 版本管理 -->
        <spring-boot.version>3.1.0</spring-boot.version>
        <junit.version>5.9.3</junit.version>
        <mockito.version>5.3.1</mockito.version>
        
        <!-- 插件版本 -->
        <maven-compiler-plugin.version>3.11.0</maven-compiler-plugin.version>
        <maven-surefire-plugin.version>3.1.0</maven-surefire-plugin.version>
        <maven-failsafe-plugin.version>3.1.0</maven-failsafe-plugin.version>
        <jacoco-maven-plugin.version>0.8.10</jacoco-maven-plugin.version>
    </properties>
    
    <!-- 依賴管理 -->
    <dependencyManagement>
        <dependencies>
            <!-- Spring Boot BOM -->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            
            <!-- 內部模組依賴 -->
            <dependency>
                <groupId>${project.groupId}</groupId>
                <artifactId>common</artifactId>
                <version>${project.version}</version>
            </dependency>
            <dependency>
                <groupId>${project.groupId}</groupId>
                <artifactId>core</artifactId>
                <version>${project.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
    
    <!-- 構建設定 -->
    <build>
        <pluginManagement>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>${maven-compiler-plugin.version}</version>
                    <configuration>
                        <source>${maven.compiler.source}</source>
                        <target>${maven.compiler.target}</target>
                        <encoding>${project.build.sourceEncoding}</encoding>
                    </configuration>
                </plugin>
                
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>${maven-surefire-plugin.version}</version>
                    <configuration>
                        <parallel>methods</parallel>
                        <threadCount>10</threadCount>
                        <includes>
                            <include>**/*Test.java</include>
                            <include>**/*Tests.java</include>
                        </includes>
                    </configuration>
                </plugin>
                
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <version>${jacoco-maven-plugin.version}</version>
                    <executions>
                        <execution>
                            <goals>
                                <goal>prepare-agent</goal>
                            </goals>
                        </execution>
                        <execution>
                            <id>report</id>
                            <phase>test</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </pluginManagement>
        
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    
    <!-- 配置檔案 -->
    <profiles>
        <profile>
            <id>ci</id>
            <properties>
                <maven.javadoc.skip>true</maven.javadoc.skip>
                <maven.source.skip>true</maven.source.skip>
            </properties>
        </profile>
        
        <profile>
            <id>integration-tests</id>
            <modules>
                <module>integration-tests</module>
            </modules>
        </profile>
    </profiles>
</project>
```

#### 8.7 多模組建置策略

**並行建置 Pipeline：**

```groovy
// 多模組並行建置 Jenkinsfile
pipeline {
    agent any
    
    tools {
        maven 'Maven-3.9'
        jdk 'JDK-17'
    }
    
    environment {
        MAVEN_OPTS = '-Xmx4g -XX:+UseG1GC'
        MAVEN_CLI_OPTS = '-B -V -e -T 4'  // 4 個執行緒並行建置
    }
    
    stages {
        stage('Multi-module Build') {
            parallel {
                stage('Common Module') {
                    steps {
                        dir('common') {
                            sh "mvn ${MAVEN_CLI_OPTS} clean compile test"
                        }
                    }
                    post {
                        always {
                            junit 'common/target/surefire-reports/*.xml'
                        }
                    }
                }
                
                stage('Core Module') {
                    steps {
                        dir('core') {
                            sh "mvn ${MAVEN_CLI_OPTS} clean compile test"
                        }
                    }
                    post {
                        always {
                            junit 'core/target/surefire-reports/*.xml'
                        }
                    }
                }
                
                stage('Web Module') {
                    steps {
                        dir('web') {
                            sh "mvn ${MAVEN_CLI_OPTS} clean compile test"
                        }
                    }
                    post {
                        always {
                            junit 'web/target/surefire-reports/*.xml'
                        }
                    }
                }
            }
        }
        
        stage('Integration Build') {
            steps {
                echo '整合建置所有模組'
                sh "mvn ${MAVEN_CLI_OPTS} clean package -P ci"
            }
        }
        
        stage('Integration Tests') {
            steps {
                echo '執行跨模組整合測試'
                sh "mvn ${MAVEN_CLI_OPTS} verify -P integration-tests"
            }
            post {
                always {
                    junit 'integration-tests/target/failsafe-reports/*.xml'
                }
            }
        }
        
        stage('Aggregate Reports') {
            steps {
                echo '聚合測試報告'
                sh "mvn ${MAVEN_CLI_OPTS} jacoco:report-aggregate"
                
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'target/site/jacoco-aggregate',
                    reportFiles: 'index.html',
                    reportName: 'Aggregated Coverage Report'
                ])
            }
        }
    }
}
```

### 💡 實務案例

#### 案例：企業級 Maven 建置最佳實務

**情境**：為大型 Java 企業應用建立標準化的 Maven 建置流程

**解決方案架構：**

```mermaid
graph TB
    A[企業 Maven 標準] --> B[依賴管理]
    A --> C[建置生命週期]
    A --> D[品質門檻]
    A --> E[制品管理]
    
    B --> F[BOM 管理]
    B --> G[版本策略]
    B --> H[安全掃描]
    
    C --> I[並行建置]
    C --> J[測試策略]
    C --> K[文件生成]
    
    D --> L[程式碼覆蓋率]
    D --> M[程式碼品質]
    D --> N[安全檢查]
    
    E --> O[Nexus 整合]
    E --> P[版本管理]
    E --> Q[發布策略]
```

### ⚠️ 注意事項

1. **效能優化**：
   - 使用並行建置（-T 參數）
   - 設定適當的記憶體配置
   - 利用 Maven 本地倉庫快取

2. **依賴管理**：
   - 定期更新依賴版本
   - 檢查依賴衝突
   - 使用 BOM 統一版本管理

3. **測試策略**：
   - 區分單元測試和整合測試
   - 設定合理的測試超時時間
   - 並行執行測試以提高效率

4. **制品管理**：
   - 建立清楚的版本策略
   - 定期清理舊版本制品
   - 備份重要的發布版本

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Maven 整合 | 生命週期、建置設定、多模組管理 |
| 自動化建置 | Pipeline 整合、並行建置、測試策略 |
| 制品管理 | 倉庫設定、版本管理、發布流程 |

### 📝 練習作業

1. **基礎練習**：設定單一模組 Maven 專案的完整建置流程
2. **進階練習**：建立多模組專案的並行建置策略
3. **實務練習**：實施企業級 Maven 建置標準和最佳實務

---

## 第9章 Pipeline 基礎與 Declarative Syntax

### 🎯 學習目標

- 掌握 Jenkins Pipeline 的核心概念和優勢
- 理解 Declarative 和 Scripted Pipeline 的差異
- 學會撰寫基本的 Declarative Pipeline
- 建立可重用和可維護的 Pipeline 結構

### 📚 核心概念

#### 9.1 Pipeline 概述與優勢

Jenkins Pipeline 將建置流程定義為程式碼（Pipeline as Code），提供比 Freestyle Project 更強大的功能和可維護性。

```mermaid
graph TD
    A[Jenkins Pipeline] --> B[Pipeline as Code]
    A --> C[版本控制整合]
    A --> D[複雜流程支援]
    A --> E[可重用性]
    
    B --> F[Jenkinsfile]
    F --> G[Declarative Syntax]
    F --> H[Scripted Syntax]
    
    C --> I[Git 整合]
    C --> J[分支策略]
    C --> K[Code Review]
    
    D --> L[並行執行]
    D --> M[條件判斷]
    D --> N[錯誤處理]
    
    E --> O[Shared Libraries]
    E --> P[Template Pipeline]
    E --> Q[標準化流程]
    
    subgraph "Pipeline 執行流程"
        R[Checkout] --> S[Build]
        S --> T[Test]
        T --> U[Deploy]
    end
```

**Pipeline vs Freestyle Project 比較：**

| 特性 | Freestyle Project | Pipeline |
|------|------------------|----------|
| **配置方式** | Web UI 圖形介面 | 程式碼定義 |
| **版本控制** | 難以版本控制 | 完整版本控制 |
| **複雜度支援** | 適合簡單流程 | 支援複雜邏輯 |
| **重用性** | 難以重用 | 高度可重用 |
| **維護性** | 手動維護 | 程式化維護 |
| **並行支援** | 有限 | 原生支援 |
| **條件執行** | 基礎條件 | 豐富的條件邏輯 |
| **錯誤處理** | 基本錯誤處理 | 精細錯誤控制 |

#### 9.2 Declarative vs Scripted Pipeline

**語法比較：**

```groovy
// Declarative Pipeline (推薦)
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'mvn compile'
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
}
```

```groovy
// Scripted Pipeline (傳統方式)
node {
    try {
        stage('Build') {
            sh 'mvn compile'
        }
        
        stage('Test') {
            sh 'mvn test'
        }
    } catch (Exception e) {
        currentBuild.result = 'FAILURE'
        throw e
    }
}
```

**選擇指南：**

| 場景 | 建議語法 | 原因 |
|------|----------|------|
| **新專案** | Declarative | 結構清晰、易於理解 |
| **複雜邏輯** | Scripted | 更大的靈活性 |
| **團隊協作** | Declarative | 標準化結構 |
| **維護性** | Declarative | 更好的可讀性 |

### 🛠️ Declarative Pipeline 基礎結構

#### 9.3 基本語法元素

**完整的 Pipeline 結構：**

```groovy
// 基本 Declarative Pipeline 結構
pipeline {
    // 執行代理設定
    agent {
        label 'linux'
    }
    
    // 工具定義
    tools {
        maven 'Maven-3.9'
        jdk 'JDK-17'
    }
    
    // 環境變數
    environment {
        APP_NAME = 'java-tutorial'
        BUILD_VERSION = "${env.BUILD_NUMBER}"
        MAVEN_OPTS = '-Xmx2g'
    }
    
    // 全域選項
    options {
        buildDiscarder(logRotator(numToKeepStr: '20'))
        timeout(time: 60, unit: 'MINUTES')
        skipStagesAfterUnstable()
        parallelsAlwaysFailFast()
        disableConcurrentBuilds()
    }
    
    // 觸發器
    triggers {
        cron('H 2 * * *')  // 每日凌晨 2 點
        pollSCM('H/15 * * * *')  // 每 15 分鐘檢查 SCM
    }
    
    // 參數定義
    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'production'],
            description: '部署環境選擇'
        )
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: '跳過測試階段'
        )
        string(
            name: 'DEPLOY_VERSION',
            defaultValue: 'latest',
            description: '部署版本'
        )
    }
    
    // 建置階段
    stages {
        stage('Preparation') {
            steps {
                echo "開始建置 ${env.APP_NAME} 版本 ${env.BUILD_VERSION}"
                echo "目標環境: ${params.ENVIRONMENT}"
                
                // 環境檢查
                sh '''
                    echo "=== 環境資訊 ==="
                    java -version
                    mvn -version
                    echo "工作目錄: $(pwd)"
                '''
            }
        }
        
        stage('Checkout') {
            steps {
                // Git checkout
                checkout scm
                
                script {
                    // 設定 Git 相關環境變數
                    env.GIT_COMMIT_SHORT = sh(
                        script: "git rev-parse --short HEAD",
                        returnStdout: true
                    ).trim()
                    
                    env.GIT_BRANCH_NAME = sh(
                        script: "git rev-parse --abbrev-ref HEAD",
                        returnStdout: true
                    ).trim()
                }
                
                echo "Git 版本: ${env.GIT_COMMIT_SHORT}"
                echo "Git 分支: ${env.GIT_BRANCH_NAME}"
            }
        }
        
        stage('Build') {
            steps {
                echo '編譯應用程式'
                sh 'mvn clean compile -B'
            }
        }
        
        stage('Test') {
            when {
                not { params.SKIP_TESTS }
            }
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'mvn test -B'
                    }
                    post {
                        always {
                            junit 'target/surefire-reports/*.xml'
                        }
                    }
                }
                
                stage('Integration Tests') {
                    when {
                        anyOf {
                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps {
                        sh 'mvn verify -P integration-tests -B'
                    }
                    post {
                        always {
                            junit 'target/failsafe-reports/*.xml'
                        }
                    }
                }
            }
        }
        
        stage('Package') {
            steps {
                sh 'mvn package -DskipTests -B'
                
                // 保存建置產物
                archiveArtifacts(
                    artifacts: 'target/*.jar',
                    fingerprint: true
                )
            }
        }
        
        stage('Deploy') {
            when {
                anyOf {
                    branch 'master'
                    branch 'develop'
                    expression { params.ENVIRONMENT != 'production' || env.BRANCH_NAME == 'master' }
                }
            }
            steps {
                script {
                    def deployTarget = params.ENVIRONMENT
                    echo "部署到 ${deployTarget} 環境"
                    
                    switch(deployTarget) {
                        case 'dev':
                            sh './scripts/deploy-dev.sh'
                            break
                        case 'staging':
                            sh './scripts/deploy-staging.sh'
                            break
                        case 'production':
                            // 生產環境需要人工確認
                            input message: '確認部署到生產環境？',
                                  ok: '部署',
                                  submitterParameter: 'DEPLOYER'
                            
                            echo "部署者: ${env.DEPLOYER}"
                            sh './scripts/deploy-production.sh'
                            break
                        default:
                            error "未知的部署環境: ${deployTarget}"
                    }
                }
            }
        }
    }
    
    // 後置處理
    post {
        always {
            echo '建置流程完成'
            
            // 清理工作空間
            cleanWs()
        }
        
        success {
            echo '建置成功！'
            
            script {
                // 發送成功通知
                if (env.BRANCH_NAME in ['master', 'develop']) {
                    emailext(
                        subject: "✅ 建置成功: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                        body: """
                            專案: ${env.JOB_NAME}
                            建置編號: ${env.BUILD_NUMBER}
                            Git 版本: ${env.GIT_COMMIT_SHORT}
                            部署環境: ${params.ENVIRONMENT}
                            
                            建置時間: ${currentBuild.durationString}
                            建置日誌: ${env.BUILD_URL}console
                        """,
                        to: 'dev-team@company.com'
                    )
                }
            }
        }
        
        failure {
            echo '建置失敗！'
            
            emailext(
                subject: "❌ 建置失敗: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    專案: ${env.JOB_NAME}
                    建置編號: ${env.BUILD_NUMBER}
                    失敗階段: ${env.STAGE_NAME}
                    Git 版本: ${env.GIT_COMMIT_SHORT}
                    
                    錯誤詳情請查看: ${env.BUILD_URL}console
                """,
                to: 'dev-team@company.com'
            )
        }
        
        unstable {
            echo '建置不穩定 - 測試失敗但編譯成功'
        }
        
        changed {
            echo '建置狀態已改變'
        }
    }
}
```

#### 9.4 Agent 配置策略

**不同的 Agent 配置方式：**

```groovy
pipeline {
    // 1. 任意可用的 Agent
    agent any
    
    // 2. 指定標籤的 Agent
    // agent { label 'linux && maven' }
    
    // 3. Docker 容器 Agent
    // agent {
    //     docker {
    //         image 'maven:3.9.0-openjdk-17'
    //         args '-v /tmp:/tmp'
    //     }
    // }
    
    // 4. Kubernetes Pod Agent
    // agent {
    //     kubernetes {
    //         yaml """
    //             apiVersion: v1
    //             kind: Pod
    //             spec:
    //               containers:
    //               - name: maven
    //                 image: maven:3.9.0-openjdk-17
    //                 command:
    //                 - cat
    //                 tty: true
    //         """
    //     }
    // }
    
    stages {
        stage('Build on Specific Agent') {
            agent {
                label 'windows'  // 在特定階段使用不同的 Agent
            }
            steps {
                bat 'mvn clean compile'
            }
        }
        
        stage('Test in Docker') {
            agent {
                docker {
                    image 'maven:3.9.0-openjdk-17'
                    reuseNode true  // 重用節點避免重新 checkout
                }
            }
            steps {
                sh 'mvn test'
            }
        }
    }
}
```

#### 9.5 條件執行 (When)

**豐富的條件判斷：**

```groovy
pipeline {
    agent any
    
    parameters {
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'])
        booleanParam(name: 'RUN_PERF_TESTS', defaultValue: false)
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'mvn compile'
            }
        }
        
        stage('Unit Tests') {
            when {
                // 總是執行單元測試
                expression { return true }
            }
            steps {
                sh 'mvn test'
            }
        }
        
        stage('Integration Tests') {
            when {
                // 僅在主要分支執行整合測試
                anyOf {
                    branch 'master'
                    branch 'develop'
                    branch 'release/*'
                }
            }
            steps {
                sh 'mvn verify -P integration-tests'
            }
        }
        
        stage('Performance Tests') {
            when {
                allOf {
                    // 同時滿足多個條件
                    branch 'master'
                    params.RUN_PERF_TESTS
                    environment name: 'DEPLOY_ENV', value: 'staging'
                }
            }
            steps {
                sh './scripts/performance-tests.sh'
            }
        }
        
        stage('Security Scan') {
            when {
                // 非特性分支都要執行安全掃描
                not {
                    branch 'feature/*'
                }
            }
            steps {
                sh 'mvn spotbugs:check'
            }
        }
        
        stage('Deploy to Development') {
            when {
                // 使用 Groovy 表達式
                expression {
                    return params.DEPLOY_ENV == 'dev' && 
                           env.BRANCH_NAME != 'master'
                }
            }
            steps {
                sh './scripts/deploy-dev.sh'
            }
        }
        
        stage('Deploy to Staging') {
            when {
                allOf {
                    branch 'develop'
                    environment name: 'DEPLOY_ENV', value: 'staging'
                }
            }
            steps {
                sh './scripts/deploy-staging.sh'
            }
        }
        
        stage('Deploy to Production') {
            when {
                allOf {
                    branch 'master'
                    environment name: 'DEPLOY_ENV', value: 'prod'
                    // 確認是穩定建置
                    expression { 
                        return currentBuild.result == null || 
                               currentBuild.result == 'SUCCESS' 
                    }
                }
            }
            steps {
                // 生產部署需要人工確認
                script {
                    def confirmation = input(
                        message: '確認部署到生產環境？',
                        ok: '部署',
                        parameters: [
                            choice(
                                name: 'DEPLOYMENT_STRATEGY',
                                choices: ['blue-green', 'rolling', 'canary'],
                                description: '選擇部署策略'
                            )
                        ]
                    )
                    
                    echo "部署策略: ${confirmation}"
                    sh "./scripts/deploy-production.sh ${confirmation}"
                }
            }
        }
        
        stage('Cleanup') {
            when {
                // 不論成功失敗都要清理
                expression { return true }
            }
            steps {
                sh './scripts/cleanup.sh'
            }
        }
    }
}
```

### 📊 Pipeline 最佳實務

#### 9.6 模組化和重用

**函式定義和重用：**

```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                buildApplication()
            }
        }
        
        stage('Test') {
            steps {
                runTests()
            }
        }
        
        stage('Deploy') {
            steps {
                deployApplication('staging')
            }
        }
    }
}

// 定義可重用的函式
def buildApplication() {
    echo '開始建置應用程式'
    sh '''
        mvn clean compile -B \
            -Dmaven.compiler.showWarnings=true \
            -Dmaven.compiler.showDeprecation=true
    '''
}

def runTests() {
    echo '執行測試套件'
    sh 'mvn test -B'
    
    // 發布測試結果
    publishTestResults testResultsPattern: 'target/surefire-reports/*.xml'
    
    // 發布程式碼覆蓋率
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'target/site/jacoco',
        reportFiles: 'index.html',
        reportName: 'Coverage Report'
    ])
}

def deployApplication(environment) {
    echo "部署到 ${environment} 環境"
    
    script {
        switch(environment) {
            case 'dev':
                sh './deploy/dev-deploy.sh'
                break
            case 'staging':
                sh './deploy/staging-deploy.sh'
                break
            case 'production':
                input message: '確認生產部署？'
                sh './deploy/prod-deploy.sh'
                break
            default:
                error "未知的環境: ${environment}"
        }
    }
    
    // 部署後驗證
    verifyDeployment(environment)
}

def verifyDeployment(environment) {
    echo "驗證 ${environment} 環境部署"
    
    timeout(time: 5, unit: 'MINUTES') {
        script {
            def healthCheckUrl = getHealthCheckUrl(environment)
            def maxRetries = 30
            def retryCount = 0
            
            while (retryCount < maxRetries) {
                def response = sh(
                    script: "curl -s -o /dev/null -w '%{http_code}' ${healthCheckUrl}",
                    returnStdout: true
                ).trim()
                
                if (response == '200') {
                    echo "部署驗證成功！"
                    break
                } else {
                    echo "等待服務啟動... (${retryCount + 1}/${maxRetries})"
                    sleep 10
                    retryCount++
                }
            }
            
            if (retryCount >= maxRetries) {
                error "部署驗證失敗 - 服務未能正常啟動"
            }
        }
    }
}

def getHealthCheckUrl(environment) {
    def urls = [
        'dev': 'http://dev.company.com/health',
        'staging': 'http://staging.company.com/health', 
        'production': 'http://www.company.com/health'
    ]
    return urls[environment]
}
```

#### 9.7 錯誤處理策略

**全面的錯誤處理：**

```groovy
pipeline {
    agent any
    
    options {
        skipStagesAfterUnstable()
        timeout(time: 60, unit: 'MINUTES')
    }
    
    stages {
        stage('Build with Error Handling') {
            steps {
                script {
                    try {
                        sh 'mvn clean compile'
                        
                        // 檢查編譯警告
                        def warnings = sh(
                            script: "mvn compile 2>&1 | grep -c 'WARNING' || true",
                            returnStdout: true
                        ).trim().toInteger()
                        
                        if (warnings > 10) {
                            echo "警告: 發現 ${warnings} 個編譯警告"
                            currentBuild.result = 'UNSTABLE'
                        }
                        
                    } catch (Exception e) {
                        echo "編譯失敗: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                        
                        // 收集編譯錯誤資訊
                        sh 'mvn compile > compile-error.log 2>&1 || true'
                        archiveArtifacts artifacts: 'compile-error.log'
                        
                        throw e
                    }
                }
            }
        }
        
        stage('Test with Retry') {
            steps {
                retry(3) {
                    script {
                        try {
                            sh 'mvn test'
                        } catch (Exception e) {
                            echo "測試失敗，準備重試..."
                            sh 'mvn clean'  // 清理後重試
                            throw e
                        }
                    }
                }
            }
            post {
                always {
                    junit testResults: 'target/surefire-reports/*.xml',
                          allowEmptyResults: true
                }
                failure {
                    script {
                        // 分析測試失敗原因
                        def failedTests = sh(
                            script: "find target/surefire-reports -name '*.xml' -exec grep -l 'failure\\|error' {} \\;",
                            returnStdout: true
                        ).trim()
                        
                        if (failedTests) {
                            echo "失敗的測試檔案: ${failedTests}"
                            
                            // 保存失敗的測試日誌
                            sh 'tar -czf failed-tests.tar.gz target/surefire-reports/'
                            archiveArtifacts artifacts: 'failed-tests.tar.gz'
                        }
                    }
                }
            }
        }
        
        stage('Deploy with Rollback') {
            when {
                expression { currentBuild.result != 'FAILURE' }
            }
            steps {
                script {
                    def deploymentSuccess = false
                    try {
                        // 備份當前版本
                        sh './scripts/backup-current-version.sh'
                        
                        // 執行部署
                        sh './scripts/deploy.sh'
                        
                        // 驗證部署
                        timeout(time: 5, unit: 'MINUTES') {
                            sh './scripts/verify-deployment.sh'
                        }
                        
                        deploymentSuccess = true
                        echo "部署成功完成"
                        
                    } catch (Exception e) {
                        echo "部署失敗: ${e.getMessage()}"
                        
                        // 自動回滾
                        echo "開始自動回滾..."
                        sh './scripts/rollback.sh'
                        
                        // 驗證回滾
                        sh './scripts/verify-rollback.sh'
                        echo "回滾完成"
                        
                        currentBuild.result = 'FAILURE'
                        throw e
                    } finally {
                        // 清理備份檔案（如果部署成功）
                        if (deploymentSuccess) {
                            sh './scripts/cleanup-backup.sh'
                        }
                    }
                }
            }
        }
    }
    
    post {
        failure {
            script {
                // 收集失敗時的系統資訊
                sh '''
                    echo "=== 系統狀態 ===" > failure-report.txt
                    echo "建置時間: $(date)" >> failure-report.txt
                    echo "Git 版本: $(git rev-parse HEAD)" >> failure-report.txt
                    echo "Java 版本: $(java -version 2>&1)" >> failure-report.txt
                    echo "Maven 版本: $(mvn -version)" >> failure-report.txt
                    echo "磁碟使用率: $(df -h)" >> failure-report.txt
                    echo "記憶體使用率: $(free -h)" >> failure-report.txt
                '''
                
                archiveArtifacts artifacts: 'failure-report.txt'
                
                // 發送詳細的失敗通知
                emailext(
                    subject: "🚨 緊急：建置失敗 - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        ⚠️ 建置失敗詳情 ⚠️
                        
                        專案: ${env.JOB_NAME}
                        建置編號: ${env.BUILD_NUMBER}
                        失敗階段: ${env.STAGE_NAME}
                        失敗時間: ${new Date()}
                        Git 版本: ${env.GIT_COMMIT}
                        
                        🔍 快速診斷：
                        - 建置日誌: ${env.BUILD_URL}console
                        - 測試報告: ${env.BUILD_URL}testReport
                        - 失敗報告: ${env.BUILD_URL}artifact/failure-report.txt
                        
                        🛠️ 建議檢查項目：
                        1. 最近的程式碼變更
                        2. 依賴版本衝突
                        3. 環境設定變更
                        4. 測試資料或測試環境狀態
                        
                        請盡快檢查並修復問題。
                    """,
                    to: 'dev-team@company.com,ops-team@company.com',
                    attachLog: true
                )
            }
        }
    }
}
```

### 💡 實務案例

#### 案例：企業級 Java 應用 Pipeline

**情境**：為企業級 Spring Boot 應用建立完整的 CI/CD Pipeline

**解決方案：**

```groovy
// enterprise-java-app-pipeline.groovy
pipeline {
    agent none
    
    options {
        buildDiscarder(logRotator(
            numToKeepStr: '50',
            artifactNumToKeepStr: '20'
        ))
        timeout(time: 2, unit: 'HOURS')
        skipStagesAfterUnstable()
        parallelsAlwaysFailFast()
        disableConcurrentBuilds()
    }
    
    environment {
        APP_NAME = 'enterprise-java-app'
        REGISTRY_URL = 'registry.company.com'
        SONAR_PROJECT_KEY = 'enterprise-java-app'
        NEXUS_REPO = 'http://nexus.company.com:8081'
    }
    
    parameters {
        choice(
            name: 'BUILD_TYPE',
            choices: ['snapshot', 'release', 'hotfix'],
            description: '建置類型'
        )
        choice(
            name: 'DEPLOY_ENVIRONMENT',
            choices: ['none', 'dev', 'staging', 'production'],
            description: '部署目標環境'
        )
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: '跳過測試（僅限緊急情況）'
        )
        booleanParam(
            name: 'FORCE_DEPLOY',
            defaultValue: false,
            description: '強制部署（跳過確認）'
        )
    }
    
    stages {
        stage('Preparation & Validation') {
            agent {
                label 'maven && jdk17'
            }
            steps {
                // 參數驗證
                script {
                    validateParameters()
                    setupBuildEnvironment()
                }
                
                // 程式碼檢出
                checkout scm
                
                // 設定建置資訊
                script {
                    env.BUILD_VERSION = generateBuildVersion()
                    env.GIT_COMMIT_SHORT = sh(
                        script: "git rev-parse --short HEAD",
                        returnStdout: true
                    ).trim()
                    
                    currentBuild.displayName = "#${env.BUILD_NUMBER} - ${env.BUILD_VERSION}"
                    currentBuild.description = "Type: ${params.BUILD_TYPE}, Target: ${params.DEPLOY_ENVIRONMENT}"
                }
                
                echo "=== 建置資訊 ==="
                echo "應用名稱: ${env.APP_NAME}"
                echo "建置版本: ${env.BUILD_VERSION}"
                echo "建置類型: ${params.BUILD_TYPE}"
                echo "Git 版本: ${env.GIT_COMMIT_SHORT}"
                echo "目標環境: ${params.DEPLOY_ENVIRONMENT}"
            }
        }
        
        stage('Code Quality & Security') {
            parallel {
                stage('Static Analysis') {
                    agent {
                        label 'maven && jdk17'
                    }
                    steps {
                        sh 'mvn clean compile -B'
                        
                        // 程式碼風格檢查
                        sh 'mvn checkstyle:check'
                        recordIssues(
                            enabledForFailure: true,
                            tools: [checkStyle(pattern: 'target/checkstyle-result.xml')]
                        )
                        
                        // SpotBugs 分析
                        sh 'mvn spotbugs:check'
                        recordIssues(
                            enabledForFailure: true,
                            tools: [spotBugs(pattern: 'target/spotbugsXml.xml')]
                        )
                        
                        // PMD 分析
                        sh 'mvn pmd:check'
                        recordIssues(
                            enabledForFailure: false,
                            tools: [pmdParser(pattern: 'target/pmd.xml')]
                        )
                    }
                }
                
                stage('Security Scan') {
                    agent {
                        label 'security-scanner'
                    }
                    steps {
                        // 依賴安全檢查
                        sh 'mvn dependency-check:check'
                        
                        // OWASP 安全掃描
                        publishHTML([
                            allowMissing: false,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: 'target',
                            reportFiles: 'dependency-check-report.html',
                            reportName: 'OWASP Dependency Check'
                        ])
                        
                        // Secrets 掃描
                        sh './scripts/scan-secrets.sh'
                    }
                }
                
                stage('License Check') {
                    agent {
                        label 'maven && jdk17'
                    }
                    steps {
                        // 授權合規檢查
                        sh 'mvn license:check'
                        sh 'mvn license:aggregate-third-party-report'
                        
                        publishHTML([
                            allowMissing: false,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: 'target/site',
                            reportFiles: 'aggregate-third-party-report.html',
                            reportName: 'License Report'
                        ])
                    }
                }
            }
        }
        
        stage('Build & Test') {
            parallel {
                stage('Maven Build') {
                    agent {
                        label 'maven && jdk17'
                    }
                    steps {
                        script {
                            if (!params.SKIP_TESTS) {
                                // 完整建置含測試
                                sh 'mvn clean package -B'
                            } else {
                                // 跳過測試的建置
                                echo "⚠️ 警告：跳過測試建置"
                                sh 'mvn clean package -DskipTests -B'
                            }
                        }
                        
                        // 保存建置產物
                        archiveArtifacts(
                            artifacts: 'target/*.jar,target/*.war',
                            fingerprint: true
                        )
                    }
                    post {
                        always {
                            script {
                                if (!params.SKIP_TESTS) {
                                    // 發布測試結果
                                    junit testResults: 'target/surefire-reports/*.xml',
                                          allowEmptyResults: true
                                    
                                    // 發布程式碼覆蓋率
                                    publishHTML([
                                        allowMissing: false,
                                        alwaysLinkToLastBuild: true,
                                        keepAll: true,
                                        reportDir: 'target/site/jacoco',
                                        reportFiles: 'index.html',
                                        reportName: 'JaCoCo Coverage Report'
                                    ])
                                }
                            }
                        }
                    }
                }
                
                stage('Docker Build') {
                    agent {
                        label 'docker'
                    }
                    when {
                        not { params.BUILD_TYPE == 'none' }
                    }
                    steps {
                        script {
                            // 建置 Docker 映像檔
                            def imageName = "${env.REGISTRY_URL}/${env.APP_NAME}:${env.BUILD_VERSION}"
                            def latestImage = "${env.REGISTRY_URL}/${env.APP_NAME}:latest"
                            
                            sh """
                                docker build -t ${imageName} .
                                docker tag ${imageName} ${latestImage}
                            """
                            
                            // 推送到 Registry
                            withCredentials([usernamePassword(
                                credentialsId: 'docker-registry',
                                usernameVariable: 'REGISTRY_USER',
                                passwordVariable: 'REGISTRY_PASS'
                            )]) {
                                sh """
                                    echo ${REGISTRY_PASS} | docker login ${env.REGISTRY_URL} -u ${REGISTRY_USER} --password-stdin
                                    docker push ${imageName}
                                    docker push ${latestImage}
                                """
                            }
                            
                            env.DOCKER_IMAGE = imageName
                        }
                    }
                }
            }
        }
        
        stage('SonarQube Analysis') {
            agent {
                label 'maven && jdk17'
            }
            when {
                anyOf {
                    branch 'master'
                    branch 'develop'
                    changeRequest()
                }
            }
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    script {
                        def sonarArgs = "-Dsonar.login=${SONAR_TOKEN}"
                        
                        if (env.CHANGE_ID) {
                            // Pull Request 分析
                            sonarArgs += " -Dsonar.pullrequest.key=${env.CHANGE_ID}"
                            sonarArgs += " -Dsonar.pullrequest.branch=${env.CHANGE_BRANCH}"
                            sonarArgs += " -Dsonar.pullrequest.base=${env.CHANGE_TARGET}"
                        } else {
                            // 分支分析
                            sonarArgs += " -Dsonar.branch.name=${env.BRANCH_NAME}"
                        }
                        
                        sh "mvn sonar:sonar ${sonarArgs}"
                    }
                }
                
                // 等待 Quality Gate 結果
                timeout(time: 10, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            echo "SonarQube Quality Gate 失敗: ${qg.status}"
                            currentBuild.result = 'UNSTABLE'
                        }
                    }
                }
            }
        }
        
        stage('Deploy') {
            when {
                allOf {
                    not { params.DEPLOY_ENVIRONMENT == 'none' }
                    expression { currentBuild.result != 'FAILURE' }
                }
            }
            steps {
                script {
                    deployToEnvironment(params.DEPLOY_ENVIRONMENT)
                }
            }
        }
    }
    
    post {
        always {
            node('master') {
                // 建置統計和清理
                script {
                    generateBuildReport()
                }
            }
        }
        
        success {
            node('master') {
                script {
                    sendNotification('success')
                }
            }
        }
        
        failure {
            node('master') {
                script {
                    sendNotification('failure')
                    triggerFailureAnalysis()
                }
            }
        }
    }
}

// === 輔助函式定義 ===

def validateParameters() {
    // 參數驗證邏輯
    if (params.BUILD_TYPE == 'release' && env.BRANCH_NAME != 'master') {
        error "Release 建置只能在 master 分支執行"
    }
    
    if (params.DEPLOY_ENVIRONMENT == 'production' && params.BUILD_TYPE != 'release') {
        error "生產環境只能部署 release 版本"
    }
}

def setupBuildEnvironment() {
    // 設定建置環境
    sh '''
        export MAVEN_OPTS="-Xmx4g -XX:+UseG1GC"
        export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF-8"
    '''
}

def generateBuildVersion() {
    def version = "1.0.0"
    
    switch(params.BUILD_TYPE) {
        case 'snapshot':
            return "${version}-SNAPSHOT-${env.BUILD_NUMBER}"
        case 'release':
            return version
        case 'hotfix':
            return "${version}-HOTFIX-${env.BUILD_NUMBER}"
        default:
            return "${version}-${env.BUILD_NUMBER}"
    }
}

def deployToEnvironment(environment) {
    echo "部署到 ${environment} 環境"
    
    def needsApproval = (environment == 'production') && !params.FORCE_DEPLOY
    
    if (needsApproval) {
        def approval = input(
            message: "確認部署到 ${environment} 環境？",
            ok: '部署',
            parameters: [
                choice(
                    name: 'DEPLOY_STRATEGY',
                    choices: ['blue-green', 'rolling', 'canary'],
                    description: '部署策略'
                )
            ],
            submitterParameter: 'APPROVER'
        )
        
        env.DEPLOY_STRATEGY = approval
        env.DEPLOYMENT_APPROVER = env.APPROVER
    }
    
    // 執行部署
    sh "./scripts/deploy-${environment}.sh ${env.BUILD_VERSION}"
    
    // 部署後驗證
    verifyDeployment(environment)
}

def verifyDeployment(environment) {
    echo "驗證 ${environment} 環境部署"
    
    timeout(time: 10, unit: 'MINUTES') {
        sh "./scripts/verify-${environment}.sh"
    }
    
    // 健康檢查
    sh "./scripts/health-check-${environment}.sh"
}

def generateBuildReport() {
    sh '''
        echo "=== 建置報告 ===" > build-report.txt
        echo "建置時間: $(date)" >> build-report.txt
        echo "建置持續時間: ${currentBuild.durationString}" >> build-report.txt
        echo "建置結果: ${currentBuild.result ?: 'SUCCESS'}" >> build-report.txt
    '''
    
    archiveArtifacts artifacts: 'build-report.txt'
}

def sendNotification(status) {
    def color = status == 'success' ? 'good' : 'danger'
    def emoji = status == 'success' ? '✅' : '❌'
    
    slackSend(
        channel: '#ci-cd',
        color: color,
        message: "${emoji} ${env.APP_NAME} 建置 ${status}\n" +
                "版本: ${env.BUILD_VERSION}\n" +
                "環境: ${params.DEPLOY_ENVIRONMENT}\n" +
                "詳情: ${env.BUILD_URL}"
    )
}

def triggerFailureAnalysis() {
    // 觸發失敗分析工作
    build job: 'failure-analysis',
          parameters: [
              string(name: 'FAILED_JOB', value: env.JOB_NAME),
              string(name: 'BUILD_NUMBER', value: env.BUILD_NUMBER)
          ],
          wait: false
}
```

### ⚠️ 注意事項

1. **效能優化**：
   - 合理使用並行執行
   - 避免不必要的重複操作
   - 適當設定超時時間

2. **可維護性**：
   - 使用函式模組化複雜邏輯
   - 添加充分的註解和文件
   - 遵循一致的命名規則

3. **安全考量**：
   - 謹慎處理敏感資訊
   - 使用憑證管理系統
   - 記錄重要操作的稽核日誌

4. **錯誤處理**：
   - 實施適當的重試機制
   - 提供清楚的錯誤訊息
   - 建立回滾和恢復策略

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Pipeline 語法 | Declarative vs Scripted、基本結構 |
| 條件執行 | When 條件、分支策略 |
| 錯誤處理 | Try-catch、Retry、回滾機制 |
| 最佳實務 | 模組化、重用性、維護性 |

### 📝 練習作業

1. **基礎練習**：建立基本的 Declarative Pipeline
2. **進階練習**：實施複雜的條件執行和錯誤處理
3. **實務練習**：設計企業級的模組化 Pipeline 架構

---

## 第10章 Jenkinsfile 結構深度分析

### 🎯 學習目標

- 深入理解 Jenkinsfile 的結構和最佳實務
- 掌握 Pipeline 進階語法和功能
- 學會建立可重用和可擴展的 Pipeline 庫
- 實施企業級的 Pipeline 治理策略

### 📚 核心概念

#### 10.1 Jenkinsfile 結構剖析

Jenkinsfile 是 Pipeline as Code 的核心，它定義了整個建置流程。深入理解其結構對於建立高品質的 CI/CD 流程至關重要。

```mermaid
graph TB
    A[Jenkinsfile] --> B[Pipeline Block]
    B --> C[Agent Declaration]
    B --> D[Tools Configuration]
    B --> E[Environment Variables]
    B --> F[Options]
    B --> G[Triggers]
    B --> H[Parameters]
    B --> I[Stages]
    B --> J[Post Actions]
    
    I --> K[Stage 1]
    I --> L[Stage 2]
    I --> M[Stage N]
    
    K --> N[Steps]
    K --> O[When Conditions]
    K --> P[Post Actions]
    
    N --> Q[Shell Commands]
    N --> R[Pipeline Steps]
    N --> S[Script Blocks]
    
    subgraph "執行環境"
        T[Jenkins Master]
        U[Build Agent 1]
        V[Build Agent 2]
        W[Docker Container]
    end
    
    C --> T
    C --> U
    C --> V
    C --> W
```

**標準 Jenkinsfile 模板：**

```groovy
#!/usr/bin/env groovy

/**
 * 企業級 Jenkins Pipeline 模板
 * 
 * 功能特性：
 * - 多環境支援
 * - 自動化測試
 * - 程式碼品質檢查
 * - 自動部署
 * - 失敗回滾
 * - 通知整合
 * 
 * @author DevOps Team
 * @version 2.0
 * @since 2024-01-01
 */

// === Pipeline 主體定義 ===
pipeline {
    // 執行代理設定
    agent {
        label 'linux && maven && docker'
    }
    
    // 工具版本定義
    tools {
        maven 'Maven-3.9.5'
        jdk 'OpenJDK-17'
        nodejs 'NodeJS-18'  // 用於前端建置
    }
    
    // 全域環境變數
    environment {
        // 應用程式資訊
        APP_NAME = 'enterprise-app'
        APP_VERSION = readMavenPom().getVersion()
        
        // 建置資訊
        BUILD_TIMESTAMP = sh(script: 'date +%Y%m%d%H%M%S', returnStdout: true).trim()
        BUILD_USER = wrap([$class: 'BuildUser']) {
            script {
                return env.BUILD_USER ?: 'system'
            }
        }
        
        // Docker 設定
        DOCKER_REGISTRY = 'registry.company.com'
        DOCKER_NAMESPACE = 'applications'
        DOCKER_IMAGE_NAME = "${DOCKER_REGISTRY}/${DOCKER_NAMESPACE}/${APP_NAME}"
        
        // SonarQube 設定
        SONAR_PROJECT_KEY = "${APP_NAME}"
        SONAR_HOST_URL = 'https://sonar.company.com'
        
        // 部署設定
        DEPLOYMENT_NAMESPACE = 'default'
        HEALTH_CHECK_URL = "https://${APP_NAME}.company.com/actuator/health"
        
        // 通知設定
        SLACK_CHANNEL = '#ci-cd-notifications'
        EMAIL_RECIPIENTS = 'dev-team@company.com'
        
        // 建置選項
        MAVEN_OPTS = '-Xmx2g -XX:+UseG1GC -XX:+UseStringDeduplication'
        JAVA_TOOL_OPTIONS = '-Dfile.encoding=UTF-8 -Djava.awt.headless=true'
    }
    
    // 全域選項配置
    options {
        // 建置保留策略
        buildDiscarder(logRotator(
            numToKeepStr: '50',           // 保留建置數量
            daysToKeepStr: '30',          // 保留天數
            artifactNumToKeepStr: '20',   // 保留產物數量
            artifactDaysToKeepStr: '14'   // 保留產物天數
        ))
        
        // 超時設定
        timeout(time: 120, unit: 'MINUTES')
        
        // 建置選項
        skipStagesAfterUnstable()         // 不穩定後跳過階段
        skipDefaultCheckout()             // 跳過預設 checkout
        parallelsAlwaysFailFast()         // 並行失敗快速停止
        disableConcurrentBuilds()         // 禁用併發建置
        preserveStashes()                 // 保留 stash
        
        // 記錄選項
        timestamps()                      // 加入時間戳記
        ansiColor('xterm')               // 支援彩色輸出
        
        // Git 選項
        gitLabConnection('GitLab')
        gitlabBuilds(builds: ['build', 'test', 'deploy'])
    }
    
    // 觸發器配置
    triggers {
        // 定時觸發 - 每日凌晨 2 點
        cron(env.BRANCH_NAME == 'master' ? 'H 2 * * *' : '')
        
        // SCM 輪詢 - 主要分支每 5 分鐘檢查一次
        pollSCM(env.BRANCH_NAME in ['master', 'develop'] ? 'H/5 * * * *' : '')
        
        // 上游專案觸發
        upstream(
            upstreamProjects: 'shared-libraries,common-dependencies',
            threshold: hudson.model.Result.SUCCESS
        )
    }
    
    // 參數定義
    parameters {
        // 建置類型選擇
        choice(
            name: 'BUILD_TYPE',
            choices: ['standard', 'quick', 'full', 'release'],
            description: '''
            建置類型說明：
            - standard: 標準建置（包含單元測試）
            - quick: 快速建置（跳過測試，僅編譯）
            - full: 完整建置（包含整合測試和程式碼分析）
            - release: 發布建置（完整流程 + 部署）
            '''
        )
        
        // 部署環境選擇
        choice(
            name: 'DEPLOY_ENVIRONMENT',
            choices: ['none', 'dev', 'staging', 'uat', 'production'],
            description: '選擇部署目標環境'
        )
        
        // 部署策略選擇
        choice(
            name: 'DEPLOY_STRATEGY',
            choices: ['rolling', 'blue-green', 'canary'],
            description: '部署策略選擇'
        )
        
        // 進階選項
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: '跳過測試階段（不建議用於正式環境）'
        )
        
        booleanParam(
            name: 'FORCE_DEPLOY',
            defaultValue: false,
            description: '強制部署（跳過人工確認）'
        )
        
        booleanParam(
            name: 'ENABLE_DEBUG',
            defaultValue: false,
            description: '啟用詳細除錯資訊'
        )
        
        // 字串參數
        string(
            name: 'CUSTOM_VERSION',
            defaultValue: '',
            description: '自訂版本號（留空使用 pom.xml 版本）'
        )
        
        text(
            name: 'DEPLOY_NOTES',
            defaultValue: '',
            description: '部署備註（將記錄在部署日誌中）'
        )
        
        // 密碼參數
        password(
            name: 'EMERGENCY_TOKEN',
            defaultValue: '',
            description: '緊急部署令牌（僅限生產環境緊急部署）'
        )
    }
    
    // === 建置階段定義 ===
    stages {
        stage('🔍 Pre-build Validation') {
            steps {
                script {
                    // 顯示建置資訊
                    displayBuildInfo()
                    
                    // 參數驗證
                    validateBuildParameters()
                    
                    // 環境檢查
                    validateBuildEnvironment()
                    
                    // 設定建置版本
                    setupBuildVersion()
                }
            }
        }
        
        stage('📥 Source Checkout') {
            steps {
                script {
                    // 清理工作空間
                    cleanWs()
                    
                    // 檢出原始碼
                    checkoutSource()
                    
                    // 設定 Git 資訊
                    setupGitEnvironment()
                    
                    // 依賴檢查
                    validateDependencies()
                }
            }
        }
        
        stage('🔧 Build & Compile') {
            when {
                not { params.BUILD_TYPE == 'none' }
            }
            parallel {
                stage('Backend Build') {
                    steps {
                        script {
                            buildBackend()
                        }
                    }
                    post {
                        always {
                            recordCompilerWarnings()
                        }
                    }
                }
                
                stage('Frontend Build') {
                    when {
                        expression {
                            return fileExists('package.json')
                        }
                    }
                    steps {
                        script {
                            buildFrontend()
                        }
                    }
                }
                
                stage('Documentation Build') {
                    when {
                        anyOf {
                            params.BUILD_TYPE == 'full'
                            params.BUILD_TYPE == 'release'
                        }
                    }
                    steps {
                        script {
                            buildDocumentation()
                        }
                    }
                }
            }
        }
        
        stage('🧪 Quality Assurance') {
            when {
                not { params.SKIP_TESTS }
            }
            parallel {
                stage('Unit Tests') {
                    steps {
                        script {
                            runUnitTests()
                        }
                    }
                    post {
                        always {
                            publishTestResults(
                                testResultsPattern: 'target/surefire-reports/*.xml',
                                allowEmptyResults: true
                            )
                            
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target/site/jacoco',
                                reportFiles: 'index.html',
                                reportName: 'Code Coverage Report'
                            ])
                        }
                    }
                }
                
                stage('Integration Tests') {
                    when {
                        anyOf {
                            params.BUILD_TYPE == 'full'
                            params.BUILD_TYPE == 'release'
                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps {
                        script {
                            runIntegrationTests()
                        }
                    }
                    post {
                        always {
                            publishTestResults(
                                testResultsPattern: 'target/failsafe-reports/*.xml',
                                allowEmptyResults: true
                            )
                        }
                    }
                }
                
                stage('Performance Tests') {
                    when {
                        allOf {
                            anyOf {
                                params.BUILD_TYPE == 'full'
                                params.BUILD_TYPE == 'release'
                            }
                            branch 'master'
                        }
                    }
                    steps {
                        script {
                            runPerformanceTests()
                        }
                    }
                    post {
                        always {
                            publishHTML([
                                allowMissing: true,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target/jmeter/reports',
                                reportFiles: 'index.html',
                                reportName: 'Performance Test Report'
                            ])
                        }
                    }
                }
                
                stage('Security Tests') {
                    when {
                        anyOf {
                            params.BUILD_TYPE == 'full'
                            params.BUILD_TYPE == 'release'
                        }
                    }
                    steps {
                        script {
                            runSecurityTests()
                        }
                    }
                }
            }
        }
        
        stage('📊 Code Analysis') {
            when {
                anyOf {
                    params.BUILD_TYPE == 'full'
                    params.BUILD_TYPE == 'release'
                    branch 'master'
                    branch 'develop'
                    changeRequest()
                }
            }
            parallel {
                stage('Static Analysis') {
                    steps {
                        script {
                            runStaticAnalysis()
                        }
                    }
                }
                
                stage('SonarQube Analysis') {
                    steps {
                        script {
                            runSonarQubeAnalysis()
                        }
                    }
                }
                
                stage('Dependency Check') {
                    steps {
                        script {
                            runDependencyCheck()
                        }
                    }
                }
            }
        }
        
        stage('📦 Package & Archive') {
            when {
                expression { currentBuild.result != 'FAILURE' }
            }
            parallel {
                stage('JAR Package') {
                    steps {
                        script {
                            packageApplication()
                        }
                    }
                    post {
                        success {
                            archiveArtifacts(
                                artifacts: 'target/*.jar,target/*.war',
                                fingerprint: true,
                                allowEmptyArchive: false
                            )
                        }
                    }
                }
                
                stage('Docker Image') {
                    when {
                        not { params.BUILD_TYPE == 'quick' }
                    }
                    steps {
                        script {
                            buildDockerImage()
                        }
                    }
                }
                
                stage('Helm Chart') {
                    when {
                        anyOf {
                            params.BUILD_TYPE == 'full'
                            params.BUILD_TYPE == 'release'
                        }
                    }
                    steps {
                        script {
                            packageHelmChart()
                        }
                    }
                }
            }
        }
        
        stage('🚀 Deploy') {
            when {
                allOf {
                    not { params.DEPLOY_ENVIRONMENT == 'none' }
                    expression { currentBuild.result != 'FAILURE' }
                    anyOf {
                        params.BUILD_TYPE == 'release'
                        expression { params.FORCE_DEPLOY }
                        expression { env.BRANCH_NAME in ['master', 'develop'] }
                    }
                }
            }
            steps {
                script {
                    deployApplication(params.DEPLOY_ENVIRONMENT)
                }
            }
        }
        
        stage('✅ Post-Deploy Verification') {
            when {
                allOf {
                    not { params.DEPLOY_ENVIRONMENT == 'none' }
                    expression { currentBuild.result != 'FAILURE' }
                }
            }
            steps {
                script {
                    verifyDeployment(params.DEPLOY_ENVIRONMENT)
                }
            }
        }
    }
    
    // === 後置處理 ===
    post {
        always {
            script {
                // 收集建置資訊
                collectBuildMetrics()
                
                // 清理工作空間
                performCleanup()
                
                echo "建置流程完成於 ${new Date()}"
            }
        }
        
        success {
            script {
                echo "✅ 建置成功完成！"
                
                // 發送成功通知
                sendNotification('success')
                
                // 更新建置狀態
                updateBuildStatus('SUCCESS')
                
                // 觸發下游工作
                triggerDownstreamJobs()
            }
        }
        
        failure {
            script {
                echo "❌ 建置失敗！"
                
                // 收集失敗資訊
                collectFailureInformation()
                
                // 發送失敗通知
                sendNotification('failure')
                
                // 更新建置狀態
                updateBuildStatus('FAILURE')
                
                // 觸發失敗分析
                triggerFailureAnalysis()
            }
        }
        
        unstable {
            script {
                echo "⚠️ 建置不穩定！"
                
                // 發送警告通知
                sendNotification('unstable')
                
                // 更新建置狀態
                updateBuildStatus('UNSTABLE')
            }
        }
        
        aborted {
            script {
                echo "🛑 建置已中止！"
                
                // 發送中止通知
                sendNotification('aborted')
                
                // 清理資源
                cleanupAbortedBuild()
            }
        }
        
        changed {
            script {
                echo "🔄 建置狀態已改變"
                
                // 記錄狀態變化
                logStatusChange()
            }
        }
        
        fixed {
            script {
                echo "🔧 建置已修復！"
                
                // 發送修復通知
                sendNotification('fixed')
            }
        }
        
        regression {
            script {
                echo "📉 建置回歸！"
                
                // 發送回歸警告
                sendNotification('regression')
                
                // 觸發回歸分析
                triggerRegressionAnalysis()
            }
        }
    }
}

// === 輔助函式庫 ===

/**
 * 顯示建置資訊
 */
def displayBuildInfo() {
    echo """
    ╔══════════════════════════════════════════════════════════════════╗
    ║                           建置資訊                                ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║ 應用程式名稱: ${env.APP_NAME}
    ║ 建置編號: ${env.BUILD_NUMBER}
    ║ 建置類型: ${params.BUILD_TYPE}
    ║ Git 分支: ${env.BRANCH_NAME}
    ║ Git 版本: ${env.GIT_COMMIT}
    ║ 建置時間: ${env.BUILD_TIMESTAMP}
    ║ 建置使用者: ${env.BUILD_USER}
    ║ 部署環境: ${params.DEPLOY_ENVIRONMENT}
    ║ 部署策略: ${params.DEPLOY_STRATEGY}
    ╚══════════════════════════════════════════════════════════════════╝
    """
}

/**
 * 驗證建置參數
 */
def validateBuildParameters() {
    echo "驗證建置參數..."
    
    // 檢查建置類型
    if (!params.BUILD_TYPE in ['standard', 'quick', 'full', 'release']) {
        error "無效的建置類型: ${params.BUILD_TYPE}"
    }
    
    // 檢查部署環境權限
    if (params.DEPLOY_ENVIRONMENT == 'production') {
        if (env.BRANCH_NAME != 'master' && !params.FORCE_DEPLOY) {
            error "生產環境部署只能從 master 分支執行，或使用 FORCE_DEPLOY 參數"
        }
        
        if (params.BUILD_TYPE != 'release' && !params.FORCE_DEPLOY) {
            error "生產環境只能部署 release 建置類型"
        }
    }
    
    // 檢查緊急部署令牌
    if (params.DEPLOY_ENVIRONMENT == 'production' && params.FORCE_DEPLOY) {
        if (!params.EMERGENCY_TOKEN) {
            error "生產環境強制部署需要緊急部署令牌"
        }
        // 在實際環境中，這裡應該驗證令牌的有效性
    }
    
    // 檢查自訂版本格式
    if (params.CUSTOM_VERSION) {
        if (!params.CUSTOM_VERSION.matches(/^\d+\.\d+\.\d+(-\w+)?$/)) {
            error "自訂版本格式無效: ${params.CUSTOM_VERSION}，正確格式: x.y.z 或 x.y.z-suffix"
        }
    }
    
    echo "✅ 參數驗證通過"
}

/**
 * 驗證建置環境
 */
def validateBuildEnvironment() {
    echo "檢查建置環境..."
    
    // 檢查必要工具
    def requiredTools = ['java', 'mvn', 'git', 'docker']
    
    requiredTools.each { tool ->
        def result = sh(script: "which ${tool}", returnStatus: true)
        if (result != 0) {
            error "找不到必要工具: ${tool}"
        }
    }
    
    // 檢查 Java 版本
    def javaVersion = sh(script: 'java -version 2>&1 | head -1', returnStdout: true).trim()
    echo "Java 版本: ${javaVersion}"
    
    // 檢查 Maven 版本
    def mavenVersion = sh(script: 'mvn -version | head -1', returnStdout: true).trim()
    echo "Maven 版本: ${mavenVersion}"
    
    // 檢查 Docker 版本
    def dockerVersion = sh(script: 'docker --version', returnStdout: true).trim()
    echo "Docker 版本: ${dockerVersion}"
    
    // 檢查磁碟空間
    def diskUsage = sh(script: "df -h ${env.WORKSPACE} | tail -1 | awk '{print \$5}'", returnStdout: true).trim()
    echo "磁碟使用率: ${diskUsage}"
    
    if (diskUsage.replace('%', '').toInteger() > 90) {
        error "磁碟空間不足: ${diskUsage}"
    }
    
    // 檢查記憶體使用率
    def memUsage = sh(script: "free | grep Mem | awk '{printf \"%.1f\", \$3/\$2 * 100.0}'", returnStdout: true).trim()
    echo "記憶體使用率: ${memUsage}%"
    
    echo "✅ 環境檢查通過"
}

/**
 * 設定建置版本
 */
def setupBuildVersion() {
    script {
        if (params.CUSTOM_VERSION) {
            env.BUILD_VERSION = params.CUSTOM_VERSION
        } else {
            // 從 pom.xml 讀取版本
            def pomVersion = readMavenPom().getVersion()
            
            switch(params.BUILD_TYPE) {
                case 'release':
                    env.BUILD_VERSION = pomVersion.replace('-SNAPSHOT', '')
                    break
                case 'quick':
                case 'standard':
                case 'full':
                    env.BUILD_VERSION = "${pomVersion}-${env.BUILD_NUMBER}"
                    break
                default:
                    env.BUILD_VERSION = "${pomVersion}-${env.BUILD_NUMBER}"
            }
        }
        
        echo "建置版本: ${env.BUILD_VERSION}"
        
        // 更新建置顯示名稱
        currentBuild.displayName = "#${env.BUILD_NUMBER} - v${env.BUILD_VERSION}"
        currentBuild.description = "Type: ${params.BUILD_TYPE} | Target: ${params.DEPLOY_ENVIRONMENT}"
    }
}

/**
 * 檢出原始碼
 */
def checkoutSource() {
    echo "檢出原始碼..."
    
    // 執行 Git checkout
    checkout scm
    
    // 顯示 Git 資訊
    sh '''
        echo "Git 資訊:"
        echo "  當前分支: $(git branch --show-current)"
        echo "  最新提交: $(git log -1 --oneline)"
        echo "  提交作者: $(git log -1 --pretty=format:'%an <%ae>')"
        echo "  提交時間: $(git log -1 --pretty=format:'%ad')"
        echo "  工作目錄: $(pwd)"
        echo "  檔案數量: $(find . -name '*.java' | wc -l) Java 檔案"
    '''
}

/**
 * 設定 Git 環境資訊
 */
def setupGitEnvironment() {
    script {
        // 設定 Git 相關環境變數
        env.GIT_COMMIT_SHORT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
        env.GIT_COMMIT_FULL = sh(script: "git rev-parse HEAD", returnStdout: true).trim()
        env.GIT_BRANCH_NAME = sh(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim()
        env.GIT_AUTHOR_NAME = sh(script: "git log -1 --pretty=format:'%an'", returnStdout: true).trim()
        env.GIT_AUTHOR_EMAIL = sh(script: "git log -1 --pretty=format:'%ae'", returnStdout: true).trim()
        env.GIT_COMMIT_MESSAGE = sh(script: "git log -1 --pretty=format:'%s'", returnStdout: true).trim()
        env.GIT_COMMIT_TIME = sh(script: "git log -1 --pretty=format:'%ai'", returnStdout: true).trim()
        
        // 檢查是否有未提交的變更
        def hasChanges = sh(script: "git status --porcelain", returnStdout: true).trim()
        if (hasChanges) {
            echo "⚠️ 警告: 工作目錄有未提交的變更"
            echo hasChanges
        }
        
        echo "Git 環境設定完成"
    }
}

/**
 * 驗證專案依賴
 */
def validateDependencies() {
    echo "驗證專案依賴..."
    
    // 檢查 Maven 專案結構
    if (!fileExists('pom.xml')) {
        error "找不到 pom.xml 檔案"
    }
    
    // 驗證 pom.xml 語法
    sh 'mvn help:effective-pom -q > /dev/null'
    
    // 檢查依賴衝突
    sh 'mvn dependency:analyze-only -q'
    
    // 下載依賴
    sh 'mvn dependency:resolve-sources -q'
    
    echo "✅ 依賴驗證完成"
}

/**
 * 建置後端應用
 */
def buildBackend() {
    echo "建置後端應用..."
    
    // 清理 target 目錄
    sh 'mvn clean -q'
    
    // 編譯專案
    def compileCmd = 'mvn compile -B'
    
    if (params.ENABLE_DEBUG) {
        compileCmd += ' -X'  // 詳細輸出
    }
    
    if (params.BUILD_TYPE == 'quick') {
        compileCmd += ' -T 1C'  // 並行編譯
    }
    
    sh compileCmd
    
    echo "✅ 後端建置完成"
}

/**
 * 建置前端應用
 */
def buildFrontend() {
    echo "建置前端應用..."
    
    dir('frontend') {
        // 安裝 Node.js 依賴
        sh 'npm ci'
        
        // 執行前端建置
        sh 'npm run build'
        
        // 執行前端測試
        if (!params.SKIP_TESTS) {
            sh 'npm run test:ci'
        }
    }
    
    echo "✅ 前端建置完成"
}

/**
 * 建置文件
 */
def buildDocumentation() {
    echo "建置專案文件..."
    
    // 生成 JavaDoc
    sh 'mvn javadoc:javadoc -q'
    
    // 生成站點文件
    sh 'mvn site -q'
    
    // 發布文件
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'target/site',
        reportFiles: 'index.html',
        reportName: 'Project Documentation'
    ])
    
    echo "✅ 文件建置完成"
}

/**
 * 執行單元測試
 */
def runUnitTests() {
    echo "執行單元測試..."
    
    def testCmd = 'mvn test -B'
    
    if (params.ENABLE_DEBUG) {
        testCmd += ' -X'
    }
    
    // 設定測試參數
    testCmd += ' -Dmaven.test.failure.ignore=true'  // 即使測試失敗也繼續
    testCmd += ' -Djacoco.destFile=target/jacoco.exec'  // 程式碼覆蓋率
    
    sh testCmd
    
    echo "✅ 單元測試完成"
}

/**
 * 執行整合測試
 */
def runIntegrationTests() {
    echo "執行整合測試..."
    
    // 啟動測試用資料庫
    sh 'docker-compose -f docker-compose-test.yml up -d'
    
    try {
        // 等待服務啟動
        sleep 30
        
        // 執行整合測試
        sh 'mvn verify -P integration-tests -B'
        
    } finally {
        // 清理測試環境
        sh 'docker-compose -f docker-compose-test.yml down -v'
    }
    
    echo "✅ 整合測試完成"
}

/**
 * 收集建置指標
 */
def collectBuildMetrics() {
    script {
        def buildDuration = currentBuild.duration ?: 0
        def buildResult = currentBuild.result ?: 'SUCCESS'
        
        // 記錄建置指標
        sh """
            echo "build_duration_ms:${buildDuration}" >> build-metrics.txt
            echo "build_result:${buildResult}" >> build-metrics.txt
            echo "build_timestamp:${env.BUILD_TIMESTAMP}" >> build-metrics.txt
            echo "git_commit:${env.GIT_COMMIT_SHORT}" >> build-metrics.txt
        """
        
        // 保存建置指標
        archiveArtifacts artifacts: 'build-metrics.txt', allowEmptyArchive: true
    }
}

/**
 * 發送通知
 */
def sendNotification(status) {
    def statusMap = [
        'success': [emoji: '✅', color: 'good', title: '建置成功'],
        'failure': [emoji: '❌', color: 'danger', title: '建置失敗'],
        'unstable': [emoji: '⚠️', color: 'warning', title: '建置不穩定'],
        'aborted': [emoji: '🛑', color: '#808080', title: '建置中止'],
        'fixed': [emoji: '🔧', color: 'good', title: '建置修復'],
        'regression': [emoji: '📉', color: 'danger', title: '建置回歸']
    ]
    
    def config = statusMap[status]
    if (!config) return
    
    // Slack 通知
    slackSend(
        channel: env.SLACK_CHANNEL,
        color: config.color,
        message: """
            ${config.emoji} *${config.title}*
            
            *專案:* ${env.APP_NAME}
            *版本:* ${env.BUILD_VERSION}
            *分支:* ${env.BRANCH_NAME}
            *建置:* #${env.BUILD_NUMBER}
            *類型:* ${params.BUILD_TYPE}
            *環境:* ${params.DEPLOY_ENVIRONMENT}
            *時間:* ${currentBuild.durationString}
            
            *詳情:* ${env.BUILD_URL}
        """.stripIndent()
    )
    
    // 電子郵件通知
    emailext(
        subject: "${config.emoji} ${config.title}: ${env.APP_NAME} #${env.BUILD_NUMBER}",
        body: generateEmailBody(status),
        to: env.EMAIL_RECIPIENTS,
        attachLog: status == 'failure'
    )
}

/**
 * 產生電子郵件內容
 */
def generateEmailBody(status) {
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .header { background-color: #f5f5f5; padding: 10px; border-radius: 5px; }
                .content { margin: 20px 0; }
                .footer { margin-top: 30px; font-size: 12px; color: #666; }
                .success { color: #28a745; }
                .failure { color: #dc3545; }
                .warning { color: #ffc107; }
            </style>
        </head>
        <body>
            <div class="header">
                <h2 class="${status}">Jenkins 建置通知</h2>
            </div>
            
            <div class="content">
                <p><strong>專案名稱:</strong> ${env.APP_NAME}</p>
                <p><strong>建置編號:</strong> #${env.BUILD_NUMBER}</p>
                <p><strong>建置版本:</strong> ${env.BUILD_VERSION}</p>
                <p><strong>Git 分支:</strong> ${env.BRANCH_NAME}</p>
                <p><strong>Git 版本:</strong> ${env.GIT_COMMIT_SHORT}</p>
                <p><strong>建置類型:</strong> ${params.BUILD_TYPE}</p>
                <p><strong>部署環境:</strong> ${params.DEPLOY_ENVIRONMENT}</p>
                <p><strong>建置時間:</strong> ${currentBuild.durationString}</p>
                <p><strong>建置狀態:</strong> ${currentBuild.result ?: 'SUCCESS'}</p>
                
                <h3>快速連結</h3>
                <ul>
                    <li><a href="${env.BUILD_URL}">建置詳情</a></li>
                    <li><a href="${env.BUILD_URL}console">建置日誌</a></li>
                    <li><a href="${env.BUILD_URL}testReport">測試報告</a></li>
                    <li><a href="${env.BUILD_URL}artifact/">建置產物</a></li>
                </ul>
            </div>
            
            <div class="footer">
                <p>此郵件由 Jenkins CI/CD 系統自動發送</p>
                <p>建置時間: ${new Date()}</p>
            </div>
        </body>
        </html>
    """.stripIndent()
}
```

#### 10.2 高級 Pipeline 模式

**多分支 Pipeline 策略：**

```groovy
// 多分支建置策略
pipeline {
    agent any
    
    stages {
        stage('Branch Strategy') {
            parallel {
                stage('Master Branch') {
                    when { branch 'master' }
                    stages {
                        stage('Production Build') {
                            steps {
                                echo "執行生產建置流程"
                                sh 'mvn clean package -P production'
                            }
                        }
                        stage('Production Deploy') {
                            steps {
                                script {
                                    input message: '確認部署到生產環境？',
                                          ok: '部署',
                                          submitterParameter: 'DEPLOYER'
                                    
                                    echo "部署者: ${env.DEPLOYER}"
                                    sh './deploy-production.sh'
                                }
                            }
                        }
                    }
                }
                
                stage('Develop Branch') {
                    when { branch 'develop' }
                    stages {
                        stage('Development Build') {
                            steps {
                                echo "執行開發建置流程"
                                sh 'mvn clean package -P development'
                            }
                        }
                        stage('Auto Deploy to Dev') {
                            steps {
                                sh './deploy-development.sh'
                            }
                        }
                    }
                }
                
                stage('Feature Branch') {
                    when { branch 'feature/*' }
                    stages {
                        stage('Feature Build') {
                            steps {
                                echo "執行特性分支建置"
                                sh 'mvn clean compile test'
                            }
                        }
                        stage('Code Review') {
                            steps {
                                script {
                                    // 觸發程式碼審查流程
                                    def reviewResult = sh(
                                        script: './scripts/trigger-code-review.sh',
                                        returnStdout: true
                                    ).trim()
                                    
                                    echo "程式碼審查結果: ${reviewResult}"
                                }
                            }
                        }
                    }
                }
                
                stage('Release Branch') {
                    when { branch 'release/*' }
                    stages {
                        stage('Release Build') {
                            steps {
                                echo "執行發布建置流程"
                                sh 'mvn clean package -P release'
                            }
                        }
                        stage('Release Testing') {
                            steps {
                                sh 'mvn verify -P release-tests'
                            }
                        }
                        stage('Create Release') {
                            steps {
                                script {
                                    def releaseVersion = env.BRANCH_NAME.replace('release/', '')
                                    sh "git tag -a v${releaseVersion} -m 'Release ${releaseVersion}'"
                                    sh "git push origin v${releaseVersion}"
                                }
                            }
                        }
                    }
                }
                
                stage('Hotfix Branch') {
                    when { branch 'hotfix/*' }
                    stages {
                        stage('Hotfix Build') {
                            steps {
                                echo "執行熱修復建置流程"
                                sh 'mvn clean package -P hotfix'
                            }
                        }
                        stage('Emergency Deploy') {
                            steps {
                                script {
                                    def confirmation = input(
                                        message: '這是緊急熱修復，確認立即部署？',
                                        ok: '緊急部署',
                                        submitterParameter: 'EMERGENCY_DEPLOYER'
                                    )
                                    
                                    echo "緊急部署授權者: ${env.EMERGENCY_DEPLOYER}"
                                    sh './deploy-hotfix.sh'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### 🔄 Pipeline 最佳實務模式

#### 10.3 可重用 Pipeline 庫

**建立 Shared Library：**

```groovy
// vars/standardPipeline.groovy
def call(Map config) {
    pipeline {
        agent any
        
        options {
            buildDiscarder(logRotator(numToKeepStr: '20'))
            timeout(time: config.timeout ?: 60, unit: 'MINUTES')
            skipStagesAfterUnstable()
        }
        
        environment {
            APP_NAME = config.appName
            APP_VERSION = config.appVersion ?: '1.0.0'
        }
        
        stages {
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }
            
            stage('Build') {
                steps {
                    script {
                        if (config.buildTool == 'maven') {
                            buildWithMaven(config)
                        } else if (config.buildTool == 'gradle') {
                            buildWithGradle(config)
                        } else {
                            error "不支援的建置工具: ${config.buildTool}"
                        }
                    }
                }
            }
            
            stage('Test') {
                when {
                    expression { config.runTests != false }
                }
                steps {
                    script {
                        runTestSuite(config)
                    }
                }
            }
            
            stage('Deploy') {
                when {
                    expression { config.deploy == true }
                }
                steps {
                    script {
                        deployApplication(config)
                    }
                }
            }
        }
        
        post {
            always {
                script {
                    sendNotifications(config)
                }
            }
        }
    }
}

def buildWithMaven(config) {
    sh "mvn clean ${config.mavenGoals ?: 'package'} -B"
}

def buildWithGradle(config) {
    sh "./gradlew clean ${config.gradleTasks ?: 'build'}"
}

def runTestSuite(config) {
    def testProfiles = config.testProfiles ?: ['unit-tests']
    
    testProfiles.each { profile ->
        echo "執行測試設定檔: ${profile}"
        sh "mvn test -P ${profile}"
    }
    
    publishTestResults testResultsPattern: 'target/surefire-reports/*.xml'
}

def deployApplication(config) {
    def environment = config.deployEnvironment ?: 'dev'
    
    echo "部署到 ${environment} 環境"
    sh "./scripts/deploy-${environment}.sh"
}

def sendNotifications(config) {
    if (config.notifications?.slack) {
        slackSend(
            channel: config.notifications.slack.channel,
            message: "建置 ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        )
    }
    
    if (config.notifications?.email) {
        emailext(
            to: config.notifications.email.recipients,
            subject: "建置通知: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "建置狀態: ${currentBuild.currentResult}"
        )
    }
}
```

**使用 Shared Library：**

```groovy
// Jenkinsfile
@Library('company-shared-library') _

standardPipeline {
    appName = 'my-java-app'
    appVersion = '2.0.0'
    buildTool = 'maven'
    mavenGoals = 'clean package'
    runTests = true
    testProfiles = ['unit-tests', 'integration-tests']
    deploy = true
    deployEnvironment = 'staging'
    timeout = 90
    
    notifications = [
        slack: [
            channel: '#ci-cd'
        ],
        email: [
            recipients: 'dev-team@company.com'
        ]
    ]
}
```

### 💡 實務案例分析

#### 案例：微服務架構的 Pipeline 設計

**情境**：為微服務架構設計統一但靈活的 Pipeline

**解決方案：**

```groovy
// 微服務通用 Pipeline
pipeline {
    agent none
    
    parameters {
        choice(
            name: 'SERVICE_SCOPE',
            choices: ['all', 'modified', 'specific'],
            description: '服務建置範圍'
        )
        string(
            name: 'SPECIFIC_SERVICES',
            defaultValue: '',
            description: '指定服務列表（逗號分隔）'
        )
        booleanParam(
            name: 'PARALLEL_BUILD',
            defaultValue: true,
            description: '並行建置服務'
        )
    }
    
    stages {
        stage('Service Discovery') {
            agent any
            steps {
                script {
                    // 發現所有微服務
                    env.ALL_SERVICES = discoverServices()
                    
                    // 根據參數決定建置服務
                    env.BUILD_SERVICES = determineBuildServices(
                        params.SERVICE_SCOPE,
                        params.SPECIFIC_SERVICES
                    )
                    
                    echo "發現服務: ${env.ALL_SERVICES}"
                    echo "建置服務: ${env.BUILD_SERVICES}"
                }
            }
        }
        
        stage('Build Services') {
            steps {
                script {
                    def services = env.BUILD_SERVICES.split(',')
                    
                    if (params.PARALLEL_BUILD && services.size() > 1) {
                        // 並行建置
                        def parallelStages = [:]
                        
                        services.each { service ->
                            parallelStages[service] = {
                                buildService(service.trim())
                            }
                        }
                        
                        parallel parallelStages
                    } else {
                        // 序列建置
                        services.each { service ->
                            buildService(service.trim())
                        }
                    }
                }
            }
        }
        
        stage('Integration Tests') {
            agent any
            when {
                expression { env.BUILD_SERVICES.split(',').size() > 1 }
            }
            steps {
                script {
                    runIntegrationTests(env.BUILD_SERVICES)
                }
            }
        }
        
        stage('Deploy Services') {
            steps {
                script {
                    def services = env.BUILD_SERVICES.split(',')
                    deployServices(services)
                }
            }
        }
    }
}

def discoverServices() {
    def services = []
    
    // 掃描專案目錄找出所有微服務
    def serviceDirectories = sh(
        script: "find . -name 'pom.xml' -not -path './pom.xml' | dirname | sort",
        returnStdout: true
    ).trim().split('\n')
    
    serviceDirectories.each { dir ->
        def serviceName = dir.replace('./', '')
        services.add(serviceName)
    }
    
    return services.join(',')
}

def determineBuildServices(scope, specificServices) {
    switch(scope) {
        case 'all':
            return env.ALL_SERVICES
            
        case 'specific':
            return specificServices
            
        case 'modified':
            // 檢查 Git 變更，只建置有變更的服務
            def changedFiles = sh(
                script: "git diff --name-only HEAD~1 HEAD",
                returnStdout: true
            ).trim()
            
            def modifiedServices = []
            def allServices = env.ALL_SERVICES.split(',')
            
            allServices.each { service ->
                if (changedFiles.contains(service)) {
                    modifiedServices.add(service)
                }
            }
            
            return modifiedServices.join(',')
            
        default:
            return env.ALL_SERVICES
    }
}

def buildService(serviceName) {
    node('maven') {
        echo "建置服務: ${serviceName}"
        
        dir(serviceName) {
            // 建置服務
            sh 'mvn clean package -B'
            
            // 建置 Docker 映像檔
            def imageTag = "${serviceName}:${env.BUILD_NUMBER}"
            sh "docker build -t ${imageTag} ."
            
            // 推送映像檔
            sh "docker push ${imageTag}"
            
            // 儲存映像檔標籤供後續使用
            writeFile file: "${serviceName}.image", text: imageTag
            stash includes: "${serviceName}.image", name: "${serviceName}-image"
        }
    }
}

def runIntegrationTests(services) {
    echo "執行微服務整合測試: ${services}"
    
    // 啟動測試環境
    sh 'docker-compose -f docker-compose-test.yml up -d'
    
    try {
        // 等待服務啟動
        sleep 60
        
        // 執行整合測試
        sh 'mvn verify -P integration-tests'
        
    } finally {
        // 清理測試環境
        sh 'docker-compose -f docker-compose-test.yml down -v'
    }
}

def deployServices(services) {
    services.each { service ->
        node('kubectl') {
            echo "部署服務: ${service}"
            
            // 獲取映像檔標籤
            unstash "${service}-image"
            def imageTag = readFile("${service}.image").trim()
            
            // 更新 Kubernetes 部署
            sh """
                kubectl set image deployment/${service} ${service}=${imageTag}
                kubectl rollout status deployment/${service}
            """
        }
    }
}
```

### ⚠️ 注意事項

1. **效能優化**：
   - 合理使用 stash/unstash
   - 避免過深的嵌套
   - 適當設定超時時間

2. **錯誤處理**：
   - 使用 try-catch-finally
   - 設定適當的重試機制
   - 提供清楚的錯誤訊息

3. **安全考量**：
   - 避免在日誌中暴露敏感資訊
   - 使用 Jenkins 憑證管理
   - 限制腳本權限

4. **維護性**：
   - 保持 Jenkinsfile 簡潔
   - 使用函式模組化
   - 添加充分的註解

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Jenkinsfile 語法 | 完整結構分析、語法元素 |
| Pipeline 模式 | 多分支策略、微服務模式 |
| 最佳實務 | 可重用庫、錯誤處理 |
| 進階功能 | 並行執行、條件判斷 |

### 📝 練習作業

1. **基礎練習**：分析和改進現有的 Jenkinsfile 結構
2. **進階練習**：建立可重用的 Shared Library
3. **實務練習**：設計微服務架構的 Pipeline 策略

---

## 第11章 測試報告與程式碼覆蓋率整合

### 🎯 學習目標

- 整合各種測試框架到 Jenkins Pipeline
- 設定和配置程式碼覆蓋率工具
- 建立全面的測試報告系統
- 實施測試品質門檻和自動化決策

### 📚 核心概念

#### 11.1 測試框架整合架構

Jenkins 支援多種測試框架的整合，提供統一的測試報告和分析功能。

```mermaid
graph TB
    A[Jenkins Pipeline] --> B[測試執行階段]
    B --> C[單元測試]
    B --> D[整合測試]
    B --> E[功能測試]
    B --> F[效能測試]
    B --> G[安全測試]
    
    C --> H[JUnit]
    C --> I[TestNG]
    C --> J[Spock]
    
    D --> K[Spring Boot Test]
    D --> L[Testcontainers]
    D --> M[WireMock]
    
    E --> N[Selenium]
    E --> O[Cypress]
    E --> P[REST Assured]
    
    F --> Q[JMeter]
    F --> R[Gatling]
    
    G --> S[OWASP ZAP]
    G --> T[SonarQube Security]
    
    H --> U[測試報告]
    I --> U
    J --> U
    K --> U
    L --> U
    M --> U
    N --> V[UI 測試報告]
    O --> V
    P --> W[API 測試報告]
    Q --> X[效能測試報告]
    R --> X
    S --> Y[安全測試報告]
    T --> Y
    
    U --> Z[JUnit Plugin]
    V --> AA[HTML Publisher]
    W --> AA
    X --> AA
    Y --> AA
    
    Z --> AB[Jenkins 測試儀表板]
    AA --> AB
    
    subgraph "程式碼覆蓋率"
        AC[JaCoCo]
        AD[Cobertura]
        AE[Emma]
        AC --> AF[覆蓋率報告]
        AD --> AF
        AE --> AF
        AF --> AB
    end
    
    subgraph "品質門檻"
        AG[測試通過率]
        AH[程式碼覆蓋率]
        AI[效能指標]
        AJ[安全漏洞]
        AG --> AK[Quality Gate]
        AH --> AK
        AI --> AK
        AJ --> AK
    end
```

#### 11.2 JUnit 測試整合

**基本 JUnit 配置：**

```groovy
// Jenkinsfile - JUnit 整合
pipeline {
    agent any
    
    tools {
        maven 'Maven-3.9'
        jdk 'JDK-17'
    }
    
    environment {
        MAVEN_OPTS = '-Xmx2g'
        SUREFIRE_REPORTS = 'target/surefire-reports'
        FAILSAFE_REPORTS = 'target/failsafe-reports'
    }
    
    stages {
        stage('Unit Tests') {
            steps {
                echo "執行單元測試..."
                
                // 執行單元測試並生成報告
                sh '''
                    mvn clean test -B \
                        -Dmaven.test.failure.ignore=true \
                        -Dsurefire.rerunFailingTestsCount=2 \
                        -Dsurefire.parallel=methods \
                        -Dsurefire.threadCount=4
                '''
                
                // 處理測試結果
                script {
                    def testResults = analyzeSurefireResults()
                    env.UNIT_TEST_RESULTS = testResults
                }
            }
            post {
                always {
                    // 發布 JUnit 測試結果
                    junit(
                        testResults: "${env.SUREFIRE_REPORTS}/*.xml",
                        allowEmptyResults: true,
                        keepLongStdio: true,
                        healthScaleFactor: 1.0,
                        testDataPublishers: [
                            // 發布測試穩定性數據
                            [$class: 'StabilityTestDataPublisher']
                        ]
                    )
                    
                    // 記錄測試趨勢
                    recordTestTrend()
                }
                
                failure {
                    script {
                        // 分析測試失敗原因
                        analyzeTestFailures()
                        
                        // 收集失敗測試的詳細資訊
                        collectFailedTestDetails()
                    }
                }
            }
        }
        
        stage('Integration Tests') {
            steps {
                echo "執行整合測試..."
                
                // 啟動測試環境
                sh 'docker-compose -f docker-compose-test.yml up -d'
                
                // 等待服務啟動
                script {
                    waitForServices()
                }
                
                // 執行整合測試
                sh '''
                    mvn verify -P integration-tests -B \
                        -Dmaven.test.failure.ignore=true \
                        -Dfailsafe.rerunFailingTestsCount=1
                '''
            }
            post {
                always {
                    // 停止測試環境
                    sh 'docker-compose -f docker-compose-test.yml down -v'
                    
                    // 發布整合測試結果
                    junit(
                        testResults: "${env.FAILSAFE_REPORTS}/*.xml",
                        allowEmptyResults: true
                    )
                }
            }
        }
        
        stage('UI Tests') {
            when {
                anyOf {
                    branch 'master'
                    branch 'develop'
                    expression { params.RUN_UI_TESTS == true }
                }
            }
            steps {
                echo "執行 UI 測試..."
                
                // 執行 Selenium 測試
                sh '''
                    mvn test -P ui-tests -B \
                        -Dselenium.browser=chrome \
                        -Dselenium.headless=true \
                        -Dmaven.test.failure.ignore=true
                '''
            }
            post {
                always {
                    // 發布 UI 測試結果
                    junit 'target/selenium-reports/*.xml'
                    
                    // 收集螢幕截圖
                    archiveArtifacts(
                        artifacts: 'target/screenshots/**/*.png',
                        allowEmptyArchive: true
                    )
                    
                    // 發布 Selenium 報告
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/selenium-reports',
                        reportFiles: 'index.html',
                        reportName: 'Selenium Test Report'
                    ])
                }
            }
        }
        
        stage('API Tests') {
            steps {
                echo "執行 API 測試..."
                
                // 執行 REST Assured 測試
                sh '''
                    mvn test -P api-tests -B \
                        -Dapi.base.url=http://localhost:8080 \
                        -Dmaven.test.failure.ignore=true
                '''
            }
            post {
                always {
                    // 發布 API 測試結果
                    junit 'target/rest-assured-reports/*.xml'
                    
                    // 發布 API 測試報告
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/rest-assured-reports',
                        reportFiles: 'index.html',
                        reportName: 'API Test Report'
                    ])
                }
            }
        }
    }
    
    post {
        always {
            script {
                // 彙總所有測試結果
                summarizeTestResults()
                
                // 生成測試儀表板
                generateTestDashboard()
            }
        }
    }
}

// === 輔助函式 ===

def analyzeSurefireResults() {
    def surefireDir = "${env.WORKSPACE}/${env.SUREFIRE_REPORTS}"
    
    if (!fileExists(surefireDir)) {
        return "無測試結果"
    }
    
    def testResults = sh(
        script: """
            cd ${surefireDir}
            total=\$(find . -name "TEST-*.xml" -exec grep -l "testcase" {} \\; | wc -l)
            passed=\$(find . -name "TEST-*.xml" -exec grep -L "failure\\|error" {} \\; | wc -l)
            failed=\$(find . -name "TEST-*.xml" -exec grep -l "failure\\|error" {} \\; | wc -l)
            echo "總計:\$total,通過:\$passed,失敗:\$failed"
        """,
        returnStdout: true
    ).trim()
    
    return testResults
}

def waitForServices() {
    timeout(time: 5, unit: 'MINUTES') {
        script {
            def services = ['database:5432', 'redis:6379', 'app:8080']
            
            services.each { service ->
                def (host, port) = service.split(':')
                
                echo "等待 ${service} 服務啟動..."
                
                sh """
                    while ! nc -z ${host} ${port}; do
                        echo "等待 ${service}..."
                        sleep 2
                    done
                    echo "${service} 已啟動"
                """
            }
        }
    }
}

def analyzeTestFailures() {
    script {
        def failureAnalysis = sh(
            script: '''
                # 分析測試失敗模式
                find target -name "*.xml" -exec grep -l "failure\\|error" {} \\; | while read file; do
                    echo "=== $file ==="
                    grep -A 5 -B 5 "failure\\|error" "$file"
                done > test-failure-analysis.txt
            ''',
            returnStatus: true
        )
        
        if (failureAnalysis == 0) {
            archiveArtifacts artifacts: 'test-failure-analysis.txt'
        }
    }
}

def collectFailedTestDetails() {
    script {
        // 收集失敗測試的堆疊追蹤
        sh '''
            mkdir -p failed-tests-details
            
            find target -name "*.xml" -exec grep -l "failure\\|error" {} \\; | while read file; do
                basename_file=$(basename "$file")
                xmlstarlet sel -t -m "//failure" -v "concat(@message, '\\n', text())" "$file" > "failed-tests-details/${basename_file}.failure"
                xmlstarlet sel -t -m "//error" -v "concat(@message, '\\n', text())" "$file" > "failed-tests-details/${basename_file}.error"
            done
        '''
        
        archiveArtifacts(
            artifacts: 'failed-tests-details/**',
            allowEmptyArchive: true
        )
    }
}

def recordTestTrend() {
    script {
        // 記錄測試趨勢數據
        def testStats = sh(
            script: '''
                total_tests=$(find target -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@tests)" {} +)
                failed_tests=$(find target -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@failures)" {} +)
                error_tests=$(find target -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@errors)" {} +)
                skipped_tests=$(find target -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@skipped)" {} +)
                
                echo "${total_tests:-0},${failed_tests:-0},${error_tests:-0},${skipped_tests:-0}"
            ''',
            returnStdout: true
        ).trim()
        
        def (total, failed, errors, skipped) = testStats.split(',')
        
        // 記錄到文件以供趨勢分析
        writeFile file: 'test-trend.csv', text: "${env.BUILD_NUMBER},${total},${failed},${errors},${skipped}\n"
        archiveArtifacts artifacts: 'test-trend.csv'
    }
}

def summarizeTestResults() {
    script {
        def summary = sh(
            script: '''
                echo "=== 測試結果摘要 ==="
                
                # 單元測試
                if [ -d "target/surefire-reports" ]; then
                    unit_total=$(find target/surefire-reports -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@tests)" {} +)
                    unit_failed=$(find target/surefire-reports -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@failures)" {} +)
                    echo "單元測試: ${unit_total:-0} 總計, ${unit_failed:-0} 失敗"
                fi
                
                # 整合測試
                if [ -d "target/failsafe-reports" ]; then
                    integration_total=$(find target/failsafe-reports -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@tests)" {} +)
                    integration_failed=$(find target/failsafe-reports -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@failures)" {} +)
                    echo "整合測試: ${integration_total:-0} 總計, ${integration_failed:-0} 失敗"
                fi
                
                # UI 測試
                if [ -d "target/selenium-reports" ]; then
                    ui_total=$(find target/selenium-reports -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@tests)" {} +)
                    ui_failed=$(find target/selenium-reports -name "TEST-*.xml" -exec xmlstarlet sel -t -v "sum(//testsuite/@failures)" {} +)
                    echo "UI 測試: ${ui_total:-0} 總計, ${ui_failed:-0} 失敗"
                fi
            ''',
            returnStdout: true
        )
        
        echo summary
        writeFile file: 'test-summary.txt', text: summary
        archiveArtifacts artifacts: 'test-summary.txt'
    }
}

def generateTestDashboard() {
    script {
        // 生成測試儀表板 HTML
        def dashboardHtml = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>測試儀表板</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .test-section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; }
                .passed { color: green; }
                .failed { color: red; }
                .skipped { color: orange; }
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Jenkins 測試儀表板</h1>
            <div class="test-section">
                <h2>建置資訊</h2>
                <p>建置編號: ''' + env.BUILD_NUMBER + '''</p>
                <p>建置時間: ''' + new Date() + '''</p>
                <p>Git 版本: ''' + (env.GIT_COMMIT ?: 'N/A') + '''</p>
            </div>
            
            <div class="test-section">
                <h2>測試結果概覽</h2>
                <table>
                    <tr>
                        <th>測試類型</th>
                        <th>總計</th>
                        <th>通過</th>
                        <th>失敗</th>
                        <th>跳過</th>
                        <th>通過率</th>
                    </tr>
                    <tr>
                        <td>單元測試</td>
                        <td id="unit-total">-</td>
                        <td id="unit-passed" class="passed">-</td>
                        <td id="unit-failed" class="failed">-</td>
                        <td id="unit-skipped" class="skipped">-</td>
                        <td id="unit-rate">-</td>
                    </tr>
                    <tr>
                        <td>整合測試</td>
                        <td id="integration-total">-</td>
                        <td id="integration-passed" class="passed">-</td>
                        <td id="integration-failed" class="failed">-</td>
                        <td id="integration-skipped" class="skipped">-</td>
                        <td id="integration-rate">-</td>
                    </tr>
                </table>
            </div>
            
            <div class="test-section">
                <h2>快速連結</h2>
                <ul>
                    <li><a href="testReport/">JUnit 測試報告</a></li>
                    <li><a href="jacoco/">程式碼覆蓋率報告</a></li>
                    <li><a href="HTML_20Report/">詳細測試報告</a></li>
                </ul>
            </div>
        </body>
        </html>
        '''
        
        writeFile file: 'test-dashboard.html', text: dashboardHtml
        
        publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: '.',
            reportFiles: 'test-dashboard.html',
            reportName: 'Test Dashboard'
        ])
    }
}
```

#### 11.3 JaCoCo 程式碼覆蓋率整合

**JaCoCo 配置和整合：**

```xml
<!-- pom.xml - JaCoCo 配置 -->
<project>
    <properties>
        <jacoco.version>0.8.10</jacoco.version>
        <jacoco.destFile>${project.build.directory}/jacoco.exec</jacoco.destFile>
        <jacoco.dataFile>${project.build.directory}/jacoco.exec</jacoco.dataFile>
        <jacoco.minimum.coverage>0.80</jacoco.minimum.coverage>
    </properties>
    
    <build>
        <plugins>
            <!-- JaCoCo Maven Plugin -->
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>${jacoco.version}</version>
                <configuration>
                    <destFile>${jacoco.destFile}</destFile>
                    <dataFile>${jacoco.dataFile}</dataFile>
                    <excludes>
                        <!-- 排除不需要覆蓋率檢查的類別 -->
                        <exclude>**/config/**</exclude>
                        <exclude>**/dto/**</exclude>
                        <exclude>**/Application.class</exclude>
                        <exclude>**/*Test.class</exclude>
                        <exclude>**/*IT.class</exclude>
                    </excludes>
                </configuration>
                <executions>
                    <!-- 準備 agent -->
                    <execution>
                        <id>jacoco-initialize</id>
                        <phase>initialize</phase>
                        <goals>
                            <goal>prepare-agent</goal>
                        </goals>
                    </execution>
                    
                    <!-- 整合測試 agent -->
                    <execution>
                        <id>jacoco-initialize-integration</id>
                        <phase>pre-integration-test</phase>
                        <goals>
                            <goal>prepare-agent-integration</goal>
                        </goals>
                    </execution>
                    
                    <!-- 生成報告 -->
                    <execution>
                        <id>jacoco-site</id>
                        <phase>test</phase>
                        <goals>
                            <goal>report</goal>
                        </goals>
                    </execution>
                    
                    <!-- 整合測試報告 -->
                    <execution>
                        <id>jacoco-integration-report</id>
                        <phase>post-integration-test</phase>
                        <goals>
                            <goal>report-integration</goal>
                        </goals>
                    </execution>
                    
                    <!-- 合併報告 -->
                    <execution>
                        <id>jacoco-merge</id>
                        <phase>post-integration-test</phase>
                        <goals>
                            <goal>merge</goal>
                        </goals>
                        <configuration>
                            <fileSets>
                                <fileSet>
                                    <directory>${project.build.directory}</directory>
                                    <includes>
                                        <include>*.exec</include>
                                    </includes>
                                </fileSet>
                            </fileSets>
                            <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                        </configuration>
                    </execution>
                    
                    <!-- 覆蓋率檢查 -->
                    <execution>
                        <id>jacoco-check</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>check</goal>
                        </goals>
                        <configuration>
                            <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                            <rules>
                                <rule>
                                    <element>BUNDLE</element>
                                    <limits>
                                        <limit>
                                            <counter>INSTRUCTION</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>${jacoco.minimum.coverage}</minimum>
                                        </limit>
                                        <limit>
                                            <counter>BRANCH</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>0.75</minimum>
                                        </limit>
                                        <limit>
                                            <counter>CLASS</counter>
                                            <value>MISSEDCOUNT</value>
                                            <maximum>10</maximum>
                                        </limit>
                                    </limits>
                                </rule>
                                
                                <!-- 套件層級規則 -->
                                <rule>
                                    <element>PACKAGE</element>
                                    <limits>
                                        <limit>
                                            <counter>LINE</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>0.70</minimum>
                                        </limit>
                                    </limits>
                                </rule>
                                
                                <!-- 類別層級規則 -->
                                <rule>
                                    <element>CLASS</element>
                                    <excludes>
                                        <exclude>*.config.*</exclude>
                                        <exclude>*.dto.*</exclude>
                                    </excludes>
                                    <limits>
                                        <limit>
                                            <counter>METHOD</counter>
                                            <value>COVEREDRATIO</value>
                                            <minimum>0.60</minimum>
                                        </limit>
                                    </limits>
                                </rule>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    
    <profiles>
        <!-- 程式碼覆蓋率設定檔 -->
        <profile>
            <id>coverage</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.jacoco</groupId>
                        <artifactId>jacoco-maven-plugin</artifactId>
                        <executions>
                            <!-- 詳細覆蓋率報告 -->
                            <execution>
                                <id>jacoco-detailed-report</id>
                                <phase>post-integration-test</phase>
                                <goals>
                                    <goal>report</goal>
                                </goals>
                                <configuration>
                                    <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                    <outputDirectory>${project.reporting.outputDirectory}/jacoco-detailed</outputDirectory>
                                </configuration>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
        </profile>
    </profiles>
</project>
```

**Jenkins Pipeline 中的 JaCoCo 整合：**

```groovy
// Pipeline 中的程式碼覆蓋率處理
pipeline {
    agent any
    
    environment {
        JACOCO_EXEC_FILE = 'target/jacoco-merged.exec'
        COVERAGE_THRESHOLD = '80'
    }
    
    stages {
        stage('Code Coverage Analysis') {
            steps {
                echo "執行程式碼覆蓋率分析..."
                
                // 執行測試並生成覆蓋率資料
                sh '''
                    mvn clean test verify -P coverage \
                        -Djacoco.destFile=${JACOCO_EXEC_FILE} \
                        -Djacoco.minimum.coverage=0.${COVERAGE_THRESHOLD}
                '''
                
                // 生成詳細覆蓋率報告
                sh 'mvn jacoco:report -P coverage'
                
                script {
                    // 分析覆蓋率結果
                    analyzeCoverageResults()
                    
                    // 檢查覆蓋率門檻
                    checkCoverageThreshold()
                }
            }
            post {
                always {
                    // 發布 JaCoCo 覆蓋率報告
                    jacoco(
                        execPattern: '**/jacoco*.exec',
                        classPattern: '**/target/classes',
                        sourcePattern: '**/src/main/java',
                        inclusionPattern: '**/*.class',
                        exclusionPattern: '**/config/**,**/dto/**,**/*Test*.class',
                        changeBuildStatus: true,
                        minimumInstructionCoverage: '70',
                        minimumBranchCoverage: '65',
                        minimumComplexityCoverage: '60',
                        minimumLineCoverage: '75',
                        minimumMethodCoverage: '70',
                        minimumClassCoverage: '80',
                        maximumInstructionCoverage: '100',
                        maximumBranchCoverage: '100',
                        maximumComplexityCoverage: '100',
                        maximumLineCoverage: '100',
                        maximumMethodCoverage: '100',
                        maximumClassCoverage: '100'
                    )
                    
                    // 發布 HTML 覆蓋率報告
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/site/jacoco',
                        reportFiles: 'index.html',
                        reportName: 'JaCoCo Coverage Report',
                        reportTitles: '程式碼覆蓋率報告'
                    ])
                    
                    // 發布詳細覆蓋率報告
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/site/jacoco-detailed',
                        reportFiles: 'index.html',
                        reportName: 'Detailed Coverage Report'
                    ])
                }
                
                failure {
                    script {
                        // 覆蓋率不足的處理
                        handleCoverageFailure()
                    }
                }
            }
        }
        
        stage('Coverage Trend Analysis') {
            steps {
                script {
                    // 分析覆蓋率趨勢
                    analyzeCoverageTrend()
                    
                    // 生成覆蓋率趨勢報告
                    generateCoverageTrendReport()
                }
            }
        }
    }
}

def analyzeCoverageResults() {
    script {
        // 解析 JaCoCo XML 報告
        if (fileExists('target/site/jacoco/jacoco.xml')) {
            def coverage = sh(
                script: '''
                    xmlstarlet sel -t -v "//counter[@type='INSTRUCTION']/@covered" target/site/jacoco/jacoco.xml
                    xmlstarlet sel -t -v "//counter[@type='INSTRUCTION']/@missed" target/site/jacoco/jacoco.xml
                    xmlstarlet sel -t -v "//counter[@type='BRANCH']/@covered" target/site/jacoco/jacoco.xml
                    xmlstarlet sel -t -v "//counter[@type='BRANCH']/@missed" target/site/jacoco/jacoco.xml
                    xmlstarlet sel -t -v "//counter[@type='LINE']/@covered" target/site/jacoco/jacoco.xml
                    xmlstarlet sel -t -v "//counter[@type='LINE']/@missed" target/site/jacoco/jacoco.xml
                ''',
                returnStdout: true
            ).trim().split('\n')
            
            if (coverage.size() >= 6) {
                def instructionCovered = coverage[0] as Integer
                def instructionMissed = coverage[1] as Integer
                def branchCovered = coverage[2] as Integer
                def branchMissed = coverage[3] as Integer
                def lineCovered = coverage[4] as Integer
                def lineMissed = coverage[5] as Integer
                
                def instructionTotal = instructionCovered + instructionMissed
                def branchTotal = branchCovered + branchMissed
                def lineTotal = lineCovered + lineMissed
                
                def instructionRate = instructionTotal > 0 ? (instructionCovered / instructionTotal * 100).round(2) : 0
                def branchRate = branchTotal > 0 ? (branchCovered / branchTotal * 100).round(2) : 0
                def lineRate = lineTotal > 0 ? (lineCovered / lineTotal * 100).round(2) : 0
                
                env.INSTRUCTION_COVERAGE = instructionRate.toString()
                env.BRANCH_COVERAGE = branchRate.toString()
                env.LINE_COVERAGE = lineRate.toString()
                
                echo """
                程式碼覆蓋率分析結果:
                - 指令覆蓋率: ${instructionRate}% (${instructionCovered}/${instructionTotal})
                - 分支覆蓋率: ${branchRate}% (${branchCovered}/${branchTotal})
                - 行覆蓋率: ${lineRate}% (${lineCovered}/${lineTotal})
                """
            }
        } else {
            echo "找不到 JaCoCo XML 報告"
        }
    }
}

def checkCoverageThreshold() {
    script {
        def instructionCoverage = (env.INSTRUCTION_COVERAGE ?: '0') as Double
        def threshold = env.COVERAGE_THRESHOLD as Double
        
        if (instructionCoverage < threshold) {
            echo "⚠️ 警告: 程式碼覆蓋率 ${instructionCoverage}% 低於門檻 ${threshold}%"
            currentBuild.result = 'UNSTABLE'
            
            // 生成覆蓋率改善建議
            generateCoverageImprovementSuggestions()
        } else {
            echo "✅ 程式碼覆蓋率 ${instructionCoverage}% 達到門檻要求"
        }
    }
}

def handleCoverageFailure() {
    script {
        // 收集未覆蓋的程式碼資訊
        sh '''
            if [ -f target/site/jacoco/jacoco.csv ]; then
                echo "=== 未達覆蓋率門檻的類別 ===" > coverage-analysis.txt
                awk -F',' 'NR>1 && $4+$5>0 { 
                    coverage = $4/($4+$5)*100; 
                    if(coverage < 70) 
                        printf "%s: %.1f%% (%d/%d instructions)\\n", $3, coverage, $4, $4+$5 
                }' target/site/jacoco/jacoco.csv >> coverage-analysis.txt
                
                echo "" >> coverage-analysis.txt
                echo "=== 改善建議 ===" >> coverage-analysis.txt
                echo "1. 增加單元測試覆蓋關鍵業務邏輯" >> coverage-analysis.txt
                echo "2. 檢查並移除死代碼" >> coverage-analysis.txt
                echo "3. 考慮重構複雜的方法以提高可測試性" >> coverage-analysis.txt
            fi
        '''
        
        archiveArtifacts artifacts: 'coverage-analysis.txt', allowEmptyArchive: true
    }
}

def generateCoverageImprovementSuggestions() {
    script {
        def suggestions = """
        📊 程式碼覆蓋率改善建議
        
        目前覆蓋率: ${env.INSTRUCTION_COVERAGE}%
        目標覆蓋率: ${env.COVERAGE_THRESHOLD}%
        
        🎯 改善策略:
        1. 識別未覆蓋的關鍵業務邏輯
        2. 增加邊界條件測試
        3. 提高分支覆蓋率
        4. 檢查異常處理路徑
        5. 重構複雜方法以提高可測試性
        
        📈 覆蓋率提升計劃:
        - 短期目標: 提升至 ${(env.COVERAGE_THRESHOLD as Integer) + 5}%
        - 中期目標: 提升至 85%
        - 長期目標: 維持在 90% 以上
        """
        
        writeFile file: 'coverage-improvement-suggestions.md', text: suggestions
        archiveArtifacts artifacts: 'coverage-improvement-suggestions.md'
    }
}

def analyzeCoverageTrend() {
    script {
        // 記錄覆蓋率趨勢數據
        def coverageData = "${env.BUILD_NUMBER},${env.INSTRUCTION_COVERAGE ?: 0},${env.BRANCH_COVERAGE ?: 0},${env.LINE_COVERAGE ?: 0},${new Date().format('yyyy-MM-dd')}"
        
        writeFile file: 'coverage-trend.csv', text: coverageData + '\n'
        
        // 如果存在歷史數據，合併
        if (fileExists('coverage-history.csv')) {
            sh 'cat coverage-history.csv coverage-trend.csv > temp.csv && mv temp.csv coverage-history.csv'
        } else {
            sh 'echo "build,instruction,branch,line,date" > coverage-history.csv'
            sh 'cat coverage-trend.csv >> coverage-history.csv'
        }
        
        archiveArtifacts artifacts: 'coverage-history.csv'
    }
}

def generateCoverageTrendReport() {
    script {
        // 生成覆蓋率趨勢 HTML 報告
        def trendHtml = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>程式碼覆蓋率趨勢</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .chart-container { width: 800px; height: 400px; margin: 20px auto; }
                .metrics { display: flex; justify-content: space-around; margin: 20px; }
                .metric { text-align: center; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
                .metric-value { font-size: 2em; font-weight: bold; }
                .metric-label { color: #666; }
            </style>
        </head>
        <body>
            <h1>程式碼覆蓋率趨勢分析</h1>
            
            <div class="metrics">
                <div class="metric">
                    <div class="metric-value">''' + (env.INSTRUCTION_COVERAGE ?: '0') + '''%</div>
                    <div class="metric-label">指令覆蓋率</div>
                </div>
                <div class="metric">
                    <div class="metric-value">''' + (env.BRANCH_COVERAGE ?: '0') + '''%</div>
                    <div class="metric-label">分支覆蓋率</div>
                </div>
                <div class="metric">
                    <div class="metric-value">''' + (env.LINE_COVERAGE ?: '0') + '''%</div>
                    <div class="metric-label">行覆蓋率</div>
                </div>
            </div>
            
            <div class="chart-container">
                <canvas id="coverageChart"></canvas>
            </div>
            
            <script>
                // 這裡可以加入 Chart.js 圖表代碼
                const ctx = document.getElementById('coverageChart').getContext('2d');
                const chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['Build #''' + (env.BUILD_NUMBER) + ''''],
                        datasets: [{
                            label: '指令覆蓋率',
                            data: [''' + (env.INSTRUCTION_COVERAGE ?: '0') + '''],
                            borderColor: 'rgb(75, 192, 192)',
                            tension: 0.1
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100
                            }
                        }
                    }
                });
            </script>
        </body>
        </html>
        '''
        
        writeFile file: 'coverage-trend-report.html', text: trendHtml
        
        publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: '.',
            reportFiles: 'coverage-trend-report.html',
            reportName: 'Coverage Trend Report'
        ])
    }
}
```

### 💡 實務案例

#### 案例：多模組專案的測試整合

**情境**：為大型多模組 Maven 專案建立統一的測試和覆蓋率報告

**解決方案：**

```groovy
// 多模組測試整合 Pipeline
pipeline {
    agent any
    
    environment {
        AGGREGATE_COVERAGE_THRESHOLD = '75'
        MODULE_COVERAGE_THRESHOLD = '70'
    }
    
    stages {
        stage('Module Discovery') {
            steps {
                script {
                    // 發現所有模組
                    def modules = discoverModules()
                    env.PROJECT_MODULES = modules.join(',')
                    echo "發現模組: ${env.PROJECT_MODULES}"
                }
            }
        }
        
        stage('Parallel Module Testing') {
            steps {
                script {
                    def modules = env.PROJECT_MODULES.split(',')
                    def parallelStages = [:]
                    
                    modules.each { module ->
                        parallelStages["Test ${module}"] = {
                            testModule(module.trim())
                        }
                    }
                    
                    parallel parallelStages
                }
            }
        }
        
        stage('Aggregate Coverage Report') {
            steps {
                script {
                    generateAggregateCoverageReport()
                }
            }
            post {
                always {
                    // 發布聚合覆蓋率報告
                    jacoco(
                        execPattern: '**/target/jacoco*.exec',
                        classPattern: '**/target/classes',
                        sourcePattern: '**/src/main/java'
                    )
                    
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'target/site/jacoco-aggregate',
                        reportFiles: 'index.html',
                        reportName: 'Aggregate Coverage Report'
                    ])
                }
            }
        }
        
        stage('Quality Gate Evaluation') {
            steps {
                script {
                    evaluateQualityGate()
                }
            }
        }
    }
}

def discoverModules() {
    def modules = []
    
    // 掃描所有包含 pom.xml 的子目錄
    def moduleDirs = sh(
        script: "find . -mindepth 2 -name 'pom.xml' | sed 's|/pom.xml||' | sed 's|./||' | sort",
        returnStdout: true
    ).trim().split('\n')
    
    moduleDirs.each { dir ->
        if (dir && !dir.contains('target')) {
            modules.add(dir)
        }
    }
    
    return modules
}

def testModule(moduleName) {
    echo "測試模組: ${moduleName}"
    
    dir(moduleName) {
        // 單元測試
        sh 'mvn clean test -B'
        
        // 整合測試
        sh 'mvn verify -P integration-tests -B'
        
        // 發布模組測試結果
        junit testResults: 'target/surefire-reports/*.xml', allowEmptyResults: true
        junit testResults: 'target/failsafe-reports/*.xml', allowEmptyResults: true
        
        // 檢查模組覆蓋率
        script {
            checkModuleCoverage(moduleName)
        }
    }
}

def generateAggregateCoverageReport() {
    echo "生成聚合覆蓋率報告..."
    
    // 收集所有模組的 JaCoCo 執行檔
    sh '''
        mkdir -p target/jacoco-aggregate
        find . -name "jacoco*.exec" -path "*/target/*" | while read file; do
            cp "$file" "target/jacoco-aggregate/$(basename $(dirname $(dirname $file)))-$(basename $file)"
        done
    '''
    
    // 合併所有執行檔
    sh '''
        cd target/jacoco-aggregate
        java -jar ${JENKINS_HOME}/tools/jacoco/jacoco-cli.jar merge *.exec --destfile merged-jacoco.exec
    '''
    
    // 生成聚合報告
    sh '''
        mkdir -p target/site/jacoco-aggregate
        java -jar ${JENKINS_HOME}/tools/jacoco/jacoco-cli.jar report target/jacoco-aggregate/merged-jacoco.exec \
            --classfiles */target/classes \
            --sourcefiles */src/main/java \
            --html target/site/jacoco-aggregate \
            --xml target/site/jacoco-aggregate/jacoco.xml
    '''
}

def checkModuleCoverage(moduleName) {
    if (fileExists("target/site/jacoco/jacoco.xml")) {
        def coverage = sh(
            script: "xmlstarlet sel -t -v '//counter[@type=\"INSTRUCTION\"]/@covered' target/site/jacoco/jacoco.xml",
            returnStdout: true
        ).trim() as Integer
        
        def missed = sh(
            script: "xmlstarlet sel -t -v '//counter[@type=\"INSTRUCTION\"]/@missed' target/site/jacoco/jacoco.xml",
            returnStdout: true
        ).trim() as Integer
        
        def total = coverage + missed
        def rate = total > 0 ? (coverage / total * 100).round(2) : 0
        
        echo "模組 ${moduleName} 覆蓋率: ${rate}%"
        
        if (rate < (env.MODULE_COVERAGE_THRESHOLD as Double)) {
            echo "⚠️ 警告: 模組 ${moduleName} 覆蓋率 ${rate}% 低於門檻 ${env.MODULE_COVERAGE_THRESHOLD}%"
            currentBuild.result = 'UNSTABLE'
        }
    }
}

def evaluateQualityGate() {
    script {
        def qualityGateResults = [:]
        
        // 檢查聚合覆蓋率
        if (fileExists('target/site/jacoco-aggregate/jacoco.xml')) {
            def aggregateCoverage = calculateAggregateCoverage()
            qualityGateResults['coverage'] = aggregateCoverage
            
            if (aggregateCoverage < (env.AGGREGATE_COVERAGE_THRESHOLD as Double)) {
                echo "❌ Quality Gate 失敗: 聚合覆蓋率 ${aggregateCoverage}% 低於門檻 ${env.AGGREGATE_COVERAGE_THRESHOLD}%"
                currentBuild.result = 'FAILURE'
            } else {
                echo "✅ Quality Gate 通過: 聚合覆蓋率 ${aggregateCoverage}%"
            }
        }
        
        // 檢查測試通過率
        def testResults = calculateTestPassRate()
        qualityGateResults['testPassRate'] = testResults
        
        if (testResults < 95) {
            echo "❌ Quality Gate 失敗: 測試通過率 ${testResults}% 低於 95%"
            currentBuild.result = 'FAILURE'
        }
        
        // 生成 Quality Gate 報告
        generateQualityGateReport(qualityGateResults)
    }
}

def calculateAggregateCoverage() {
    def coverage = sh(
        script: "xmlstarlet sel -t -v '//counter[@type=\"INSTRUCTION\"]/@covered' target/site/jacoco-aggregate/jacoco.xml",
        returnStdout: true
    ).trim() as Integer
    
    def missed = sh(
        script: "xmlstarlet sel -t -v '//counter[@type=\"INSTRUCTION\"]/@missed' target/site/jacoco-aggregate/jacoco.xml",
        returnStdout: true
    ).trim() as Integer
    
    def total = coverage + missed
    return total > 0 ? (coverage / total * 100).round(2) : 0
}

def calculateTestPassRate() {
    // 計算所有模組的測試通過率
    def totalTests = 0
    def passedTests = 0
    
    sh '''
        find . -name "TEST-*.xml" -path "*/target/*" | while read file; do
            tests=$(xmlstarlet sel -t -v "sum(//testsuite/@tests)" "$file")
            failures=$(xmlstarlet sel -t -v "sum(//testsuite/@failures)" "$file")
            errors=$(xmlstarlet sel -t -v "sum(//testsuite/@errors)" "$file")
            
            total_tests=$((total_tests + tests))
            failed_tests=$((failures + errors))
            passed_tests=$((total_tests - failed_tests))
            
            echo "$total_tests,$passed_tests" >> test-summary.tmp
        done
        
        if [ -f test-summary.tmp ]; then
            tail -1 test-summary.tmp > final-test-summary.txt
        fi
    '''
    
    if (fileExists('final-test-summary.txt')) {
        def summary = readFile('final-test-summary.txt').trim().split(',')
        totalTests = summary[0] as Integer
        passedTests = summary[1] as Integer
    }
    
    return totalTests > 0 ? (passedTests / totalTests * 100).round(2) : 0
}

def generateQualityGateReport(results) {
    def reportHtml = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quality Gate 報告</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .gate-status { padding: 20px; margin: 10px; border-radius: 5px; }
            .pass { background-color: #d4edda; color: #155724; }
            .fail { background-color: #f8d7da; color: #721c24; }
            .metric { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Quality Gate 評估報告</h1>
        <div class="gate-status ${currentBuild.result == 'SUCCESS' ? 'pass' : 'fail'}">
            <h2>總體狀態: ${currentBuild.result ?: 'SUCCESS'}</h2>
        </div>
        
        <h3>品質指標</h3>
        <div class="metric">
            <strong>程式碼覆蓋率:</strong> ${results.coverage ?: 'N/A'}% 
            (門檻: ${env.AGGREGATE_COVERAGE_THRESHOLD}%)
        </div>
        <div class="metric">
            <strong>測試通過率:</strong> ${results.testPassRate ?: 'N/A'}% 
            (門檻: 95%)
        </div>
        
        <h3>建議行動</h3>
        <ul>
            <li>持續提升程式碼覆蓋率</li>
            <li>修復失敗的測試案例</li>
            <li>增加邊界條件測試</li>
            <li>定期檢查和重構測試代碼</li>
        </ul>
    </body>
    </html>
    """
    
    writeFile file: 'quality-gate-report.html', text: reportHtml
    
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '.',
        reportFiles: 'quality-gate-report.html',
        reportName: 'Quality Gate Report'
    ])
}
```

### ⚠️ 注意事項

1. **效能考量**：
   - 合理設定測試超時時間
   - 使用並行測試提高效率
   - 避免產生過大的測試報告

2. **報告品質**：
   - 確保測試報告的可讀性
   - 提供詳細的失敗資訊
   - 建立趨勢分析機制

3. **覆蓋率策略**：
   - 設定合理的覆蓋率門檻
   - 排除不需要測試的代碼
   - 關注程式碼品質而非單純數字

4. **維護性**：
   - 定期清理舊的測試報告
   - 保持測試案例的更新
   - 建立測試最佳實務指南

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| 測試框架整合 | JUnit、TestNG、Selenium 整合 |
| 程式碼覆蓋率 | JaCoCo 配置、報告生成 |
| 品質門檻 | Quality Gate 設定、評估 |
| 報告管理 | HTML 發布、趨勢分析 |

### 📝 練習作業

1. **基礎練習**：設定 JUnit 和 JaCoCo 的基本整合
2. **進階練習**：建立多模組專案的聚合測試報告
3. **實務練習**：實施完整的 Quality Gate 評估機制

---

## 第12章 靜態程式碼分析與品質檢查

### 🎯 學習目標

- 整合多種靜態程式碼分析工具
- 建立全面的程式碼品質檢查機制
- 實施程式碼品質門檻和自動化決策
- 設定 SonarQube 與 Jenkins 的深度整合

### 📚 核心概念

#### 12.1 靜態程式碼分析工具生態系統

靜態程式碼分析是確保程式碼品質的重要環節，透過多種工具的組合可以全面檢查程式碼的各個面向。

```mermaid
graph TB
    A[靜態程式碼分析] --> B[程式碼風格檢查]
    A --> C[程式碼品質分析]
    A --> D[安全漏洞檢測]
    A --> E[效能分析]
    A --> F[架構合規檢查]
    
    B --> G[Checkstyle]
    B --> H[SpotBugs]
    B --> I[PMD]
    B --> J[Google Java Format]
    
    C --> K[SonarQube]
    C --> L[CodeClimate]
    C --> M[Codacy]
    
    D --> N[SpotBugs Security]
    D --> O[Find Security Bugs]
    D --> P[OWASP Dependency Check]
    D --> Q[Snyk]
    
    E --> R[JProfiler]
    E --> S[YourKit]
    E --> T[JVM 分析工具]
    
    F --> U[ArchUnit]
    F --> V[Structure101]
    F --> W[JDepend]
    
    G --> X[Jenkins Warnings Plugin]
    H --> X
    I --> X
    K --> Y[SonarQube Scanner]
    N --> Z[OWASP ZAP]
    P --> Z
    
    X --> AA[Jenkins 報告儀表板]
    Y --> AA
    Z --> AA
    
    subgraph "品質門檻"
        BB[程式碼覆蓋率 > 80%]
        CC[重複程式碼 < 3%]
        DD[複雜度 < 15]
        EE[安全漏洞 = 0]
        FF[程式碼異味 < 5]
        
        BB --> GG[Quality Gate]
        CC --> GG
        DD --> GG
        EE --> GG
        FF --> GG
    end
    
    subgraph "整合流程"
        HH[Git Commit] --> II[Webhook 觸發]
        II --> JJ[Jenkins Pipeline]
        JJ --> KK[並行程式碼分析]
        KK --> LL[品質門檻檢查]
        LL --> MM[合併決策]
        MM --> NN[自動部署/人工審查]
    end
```

#### 12.2 Checkstyle 整合配置

**Maven 配置 (pom.xml)：**

```xml
<project>
    <properties>
        <checkstyle.version>10.12.4</checkstyle.version>
        <checkstyle.config.location>config/checkstyle/checkstyle.xml</checkstyle.config.location>
        <checkstyle.suppressions.location>config/checkstyle/suppressions.xml</checkstyle.suppressions.location>
    </properties>
    
    <build>
        <plugins>
            <!-- Checkstyle Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <configLocation>${checkstyle.config.location}</configLocation>
                    <suppressionsLocation>${checkstyle.suppressions.location}</suppressionsLocation>
                    <encoding>UTF-8</encoding>
                    <consoleOutput>true</consoleOutput>
                    <failsOnError>true</failsOnError>
                    <linkXRef>false</linkXRef>
                    <includeTestSourceDirectory>true</includeTestSourceDirectory>
                </configuration>
                <executions>
                    <execution>
                        <id>validate</id>
                        <phase>validate</phase>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
                <dependencies>
                    <dependency>
                        <groupId>com.puppycrawl.tools</groupId>
                        <artifactId>checkstyle</artifactId>
                        <version>${checkstyle.version}</version>
                    </dependency>
                </dependencies>
            </plugin>
            
            <!-- PMD Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-pmd-plugin</artifactId>
                <version>3.21.0</version>
                <configuration>
                    <sourceEncoding>UTF-8</sourceEncoding>
                    <minimumTokens>100</minimumTokens>
                    <targetJdk>17</targetJdk>
                    <analysisCache>true</analysisCache>
                    <rulesets>
                        <ruleset>config/pmd/pmd-rules.xml</ruleset>
                    </rulesets>
                    <excludeRoots>
                        <excludeRoot>target/generated-sources</excludeRoot>
                    </excludeRoots>
                </configuration>
                <executions>
                    <execution>
                        <id>pmd-check</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>check</goal>
                            <goal>cpd-check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
            <!-- SpotBugs Plugin -->
            <plugin>
                <groupId>com.github.spotbugs</groupId>
                <artifactId>spotbugs-maven-plugin</artifactId>
                <version>4.7.3.6</version>
                <configuration>
                    <effort>Max</effort>
                    <threshold>Low</threshold>
                    <xmlOutput>true</xmlOutput>
                    <htmlOutput>true</htmlOutput>
                    <excludeFilterFile>config/spotbugs/spotbugs-exclude.xml</excludeFilterFile>
                    <includeFilterFile>config/spotbugs/spotbugs-include.xml</includeFilterFile>
                    <plugins>
                        <plugin>
                            <groupId>com.h3xstream.findsecbugs</groupId>
                            <artifactId>findsecbugs-plugin</artifactId>
                            <version>1.12.0</version>
                        </plugin>
                    </plugins>
                </configuration>
                <executions>
                    <execution>
                        <id>spotbugs-check</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
            <!-- OWASP Dependency Check -->
            <plugin>
                <groupId>org.owasp</groupId>
                <artifactId>dependency-check-maven</artifactId>
                <version>8.4.0</version>
                <configuration>
                    <formats>
                        <format>HTML</format>
                        <format>XML</format>
                        <format>JSON</format>
                    </formats>
                    <failBuildOnCVSS>7</failBuildOnCVSS>
                    <suppressionFile>config/dependency-check/suppressions.xml</suppressionFile>
                    <cveValidForHours>4</cveValidForHours>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    
    <profiles>
        <!-- 程式碼品質檢查設定檔 -->
        <profile>
            <id>code-quality</id>
            <build>
                <plugins>
                    <!-- 更嚴格的程式碼檢查 -->
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-checkstyle-plugin</artifactId>
                        <configuration>
                            <configLocation>config/checkstyle/checkstyle-strict.xml</configLocation>
                            <failsOnError>true</failsOnError>
                            <violationSeverity>warning</violationSeverity>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>
        
        <!-- 安全檢查設定檔 -->
        <profile>
            <id>security-check</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.owasp</groupId>
                        <artifactId>dependency-check-maven</artifactId>
                        <configuration>
                            <failBuildOnCVSS>4</failBuildOnCVSS>
                            <enableRetired>true</enableRetired>
                            <enableExperimental>true</enableExperimental>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>
    </profiles>
</project>
```

**Checkstyle 配置檔案 (config/checkstyle/checkstyle.xml)：**

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <property name="charset" value="UTF-8"/>
    <property name="severity" value="warning"/>
    <property name="fileExtensions" value="java, properties, xml"/>
    
    <!-- 抑制警告過濾器 -->
    <module name="SuppressionFilter">
        <property name="file" value="${checkstyle.suppressions.location}"/>
        <property name="optional" value="true"/>
    </module>
    
    <!-- 檔案層級檢查 -->
    <module name="FileTabCharacter">
        <property name="eachLine" value="true"/>
    </module>
    
    <module name="FileLength">
        <property name="max" value="2000"/>
    </module>
    
    <module name="LineLength">
        <property name="max" value="120"/>
        <property name="ignorePattern" value="^package.*|^import.*|a href|href|http://|https://|ftp://"/>
    </module>
    
    <!-- TreeWalker 檢查 -->
    <module name="TreeWalker">
        <!-- 註解檢查 -->
        <module name="AnnotationLocation">
            <property name="id" value="AnnotationLocationMostCases"/>
            <property name="tokens" value="CLASS_DEF, INTERFACE_DEF, ENUM_DEF, METHOD_DEF, CTOR_DEF"/>
        </module>
        
        <module name="AnnotationUseStyle"/>
        <module name="MissingDeprecated"/>
        <module name="MissingOverride"/>
        
        <!-- 程式碼區塊檢查 -->
        <module name="AvoidNestedBlocks"/>
        <module name="EmptyBlock"/>
        <module name="EmptyCatchBlock">
            <property name="exceptionVariableName" value="expected"/>
        </module>
        
        <module name="LeftCurly"/>
        <module name="NeedBraces"/>
        <module name="RightCurly">
            <property name="id" value="RightCurlySame"/>
            <property name="tokens" value="LITERAL_TRY, LITERAL_CATCH, LITERAL_FINALLY, LITERAL_IF, LITERAL_ELSE, LITERAL_DO"/>
        </module>
        
        <!-- 類別設計檢查 -->
        <module name="FinalClass"/>
        <module name="HideUtilityClassConstructor"/>
        <module name="InterfaceIsType"/>
        <module name="OneTopLevelClass"/>
        <module name="VisibilityModifier">
            <property name="packageAllowed" value="true"/>
            <property name="protectedAllowed" value="true"/>
        </module>
        
        <!-- 程式碼複雜度檢查 -->
        <module name="CyclomaticComplexity">
            <property name="max" value="15"/>
        </module>
        
        <module name="JavaNCSS">
            <property name="methodMaximum" value="50"/>
            <property name="classMaximum" value="1500"/>
        </module>
        
        <module name="NPathComplexity">
            <property name="max" value="200"/>
        </module>
        
        <!-- 程式碼風格檢查 -->
        <module name="ArrayTypeStyle"/>
        <module name="CommentsIndentation"/>
        <module name="Indentation">
            <property name="basicOffset" value="4"/>
            <property name="braceAdjustment" value="0"/>
            <property name="caseIndent" value="4"/>
            <property name="throwsIndent" value="8"/>
            <property name="lineWrappingIndentation" value="8"/>
            <property name="arrayInitIndent" value="4"/>
        </module>
        
        <module name="OuterTypeFilename"/>
        <module name="UpperEll"/>
        
        <!-- 匯入檢查 -->
        <module name="AvoidStarImport"/>
        <module name="IllegalImport"/>
        <module name="RedundantImport"/>
        <module name="UnusedImports">
            <property name="processJavadoc" value="false"/>
        </module>
        
        <module name="ImportOrder">
            <property name="groups" value="/^java\./,javax,org,com"/>
            <property name="ordered" value="true"/>
            <property name="separated" value="true"/>
            <property name="option" value="top"/>
        </module>
        
        <!-- 方法設計檢查 -->
        <module name="MethodLength">
            <property name="max" value="150"/>
        </module>
        
        <module name="ParameterNumber">
            <property name="max" value="7"/>
            <property name="ignoreOverriddenMethods" value="true"/>
        </module>
        
        <!-- 命名檢查 -->
        <module name="ClassTypeParameterName">
            <property name="format" value="(^[A-Z][0-9]?)$|([A-Z][a-zA-Z0-9]*[T]$)"/>
        </module>
        
        <module name="ConstantName"/>
        <module name="LocalFinalVariableName"/>
        <module name="LocalVariableName"/>
        <module name="MemberName"/>
        <module name="MethodName"/>
        <module name="MethodTypeParameterName">
            <property name="format" value="(^[A-Z][0-9]?)$|([A-Z][a-zA-Z0-9]*[T]$)"/>
        </module>
        
        <module name="PackageName">
            <property name="format" value="^[a-z]+(\.[a-z][a-z0-9]*)*$"/>
        </module>
        
        <module name="ParameterName"/>
        <module name="StaticVariableName"/>
        <module name="TypeName"/>
        
        <!-- 空白檢查 -->
        <module name="EmptyForInitializerPad"/>
        <module name="EmptyForIteratorPad"/>
        <module name="EmptyLineSeparator">
            <property name="allowNoEmptyLineBetweenFields" value="true"/>
        </module>
        
        <module name="GenericWhitespace"/>
        <module name="MethodParamPad"/>
        <module name="NoWhitespaceAfter"/>
        <module name="NoWhitespaceBefore"/>
        <module name="OperatorWrap">
            <property name="option" value="NL"/>
            <property name="tokens" value="BAND, BOR, BSR, BXOR, DIV, EQUAL, GE, GT, LAND, LE, LITERAL_INSTANCEOF, LOR, LT, MINUS, MOD, NOT_EQUAL, PLUS, QUESTION, SL, SR, STAR, METHOD_REF"/>
        </module>
        
        <module name="ParenPad"/>
        <module name="TypecastParenPad"/>
        <module name="WhitespaceAfter"/>
        <module name="WhitespaceAround">
            <property name="allowEmptyConstructors" value="true"/>
            <property name="allowEmptyMethods" value="true"/>
            <property name="allowEmptyTypes" value="true"/>
            <property name="allowEmptyLoops" value="true"/>
        </module>
    </module>
</module>
```

#### 12.3 Jenkins Pipeline 中的程式碼分析整合

**完整的程式碼品質檢查 Pipeline：**

```groovy
pipeline {
    agent any
    
    tools {
        maven 'Maven-3.9'
        jdk 'JDK-17'
    }
    
    environment {
        SONAR_PROJECT_KEY = 'enterprise-java-app'
        SONAR_HOST_URL = 'https://sonar.company.com'
        QUALITY_GATE_TIMEOUT = '10'
    }
    
    parameters {
        choice(
            name: 'ANALYSIS_LEVEL',
            choices: ['basic', 'standard', 'strict', 'security'],
            description: '程式碼分析級別'
        )
        booleanParam(
            name: 'FAIL_ON_QUALITY_GATE',
            defaultValue: true,
            description: '品質門檻失敗時中止建置'
        )
        booleanParam(
            name: 'GENERATE_REPORTS',
            defaultValue: true,
            description: '生成詳細分析報告'
        )
    }
    
    stages {
        stage('🔍 Code Analysis Setup') {
            steps {
                script {
                    // 根據分析級別設定參數
                    setupAnalysisParameters()
                    
                    // 建立分析結果目錄
                    sh 'mkdir -p target/analysis-reports'
                }
            }
        }
        
        stage('📋 Static Code Analysis') {
            parallel {
                stage('Checkstyle Analysis') {
                    steps {
                        echo "執行 Checkstyle 程式碼風格檢查..."
                        
                        script {
                            def checkstyleProfile = getCheckstyleProfile()
                            sh "mvn checkstyle:check -P ${checkstyleProfile}"
                        }
                    }
                    post {
                        always {
                            // 發布 Checkstyle 結果
                            recordIssues(
                                enabledForFailure: true,
                                aggregatingResults: true,
                                tools: [checkStyle(
                                    pattern: 'target/checkstyle-result.xml',
                                    reportEncoding: 'UTF-8'
                                )]
                            )
                            
                            // 生成 Checkstyle 報告
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target/site',
                                reportFiles: 'checkstyle.html',
                                reportName: 'Checkstyle Report'
                            ])
                        }
                    }
                }
                
                stage('PMD Analysis') {
                    steps {
                        echo "執行 PMD 程式碼品質分析..."
                        
                        sh 'mvn pmd:pmd pmd:cpd'
                    }
                    post {
                        always {
                            // 發布 PMD 結果
                            recordIssues(
                                enabledForFailure: true,
                                tools: [
                                    pmdParser(pattern: 'target/pmd.xml'),
                                    cpd(pattern: 'target/cpd.xml')
                                ]
                            )
                            
                            // 發布 PMD 報告
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target/site',
                                reportFiles: 'pmd.html',
                                reportName: 'PMD Report'
                            ])
                        }
                    }
                }
                
                stage('SpotBugs Analysis') {
                    steps {
                        echo "執行 SpotBugs 錯誤檢測..."
                        
                        sh '''
                            mvn compile spotbugs:spotbugs
                            
                            # 如果是安全分析級別，執行額外的安全檢查
                            if [ "${ANALYSIS_LEVEL}" = "security" ]; then
                                mvn spotbugs:check -Dspotbugs.threshold=Low
                            fi
                        '''
                    }
                    post {
                        always {
                            // 發布 SpotBugs 結果
                            recordIssues(
                                enabledForFailure: true,
                                tools: [spotBugs(
                                    pattern: 'target/spotbugsXml.xml',
                                    useRankAsPriority: true
                                )]
                            )
                            
                            // 發布 SpotBugs 報告
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target/site',
                                reportFiles: 'spotbugs.html',
                                reportName: 'SpotBugs Report'
                            ])
                        }
                    }
                }
                
                stage('Dependency Security Check') {
                    when {
                        anyOf {
                            params.ANALYSIS_LEVEL == 'security'
                            params.ANALYSIS_LEVEL == 'strict'
                        }
                    }
                    steps {
                        echo "執行依賴安全檢查..."
                        
                        script {
                            def cvssThreshold = params.ANALYSIS_LEVEL == 'security' ? '4' : '7'
                            
                            sh """
                                mvn dependency-check:check -Dfailures.cvss=${cvssThreshold}
                            """
                        }
                    }
                    post {
                        always {
                            // 發布依賴檢查報告
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: 'target',
                                reportFiles: 'dependency-check-report.html',
                                reportName: 'OWASP Dependency Check Report'
                            ])
                            
                            // 保存安全報告
                            archiveArtifacts(
                                artifacts: 'target/dependency-check-report.*',
                                allowEmptyArchive: true
                            )
                        }
                    }
                }
            }
        }
        
        stage('🎯 SonarQube Analysis') {
            when {
                anyOf {
                    branch 'master'
                    branch 'develop'
                    changeRequest()
                    params.ANALYSIS_LEVEL == 'strict'
                }
            }
            steps {
                script {
                    withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                        runSonarQubeAnalysis()
                    }
                }
            }
        }
        
        stage('📊 Quality Gate Evaluation') {
            when {
                anyOf {
                    branch 'master'
                    branch 'develop'
                    changeRequest()
                }
            }
            steps {
                script {
                    evaluateQualityGate()
                }
            }
        }
        
        stage('📈 Analysis Report Generation') {
            when {
                params.GENERATE_REPORTS
            }
            steps {
                script {
                    generateAnalysisReport()
                    generateTrendAnalysis()
                }
            }
        }
    }
    
    post {
        always {
            script {
                // 收集所有分析結果
                collectAnalysisResults()
                
                // 生成摘要報告
                generateSummaryReport()
            }
        }
        
        failure {
            script {
                // 分析失敗處理
                handleAnalysisFailure()
            }
        }
    }
}

// === 輔助函式 ===

def setupAnalysisParameters() {
    script {
        switch(params.ANALYSIS_LEVEL) {
            case 'basic':
                env.CHECKSTYLE_CONFIG = 'checkstyle-basic.xml'
                env.PMD_RULESET = 'pmd-basic.xml'
                env.SPOTBUGS_EFFORT = 'Default'
                break
                
            case 'standard':
                env.CHECKSTYLE_CONFIG = 'checkstyle.xml'
                env.PMD_RULESET = 'pmd-rules.xml'
                env.SPOTBUGS_EFFORT = 'Default'
                break
                
            case 'strict':
                env.CHECKSTYLE_CONFIG = 'checkstyle-strict.xml'
                env.PMD_RULESET = 'pmd-strict.xml'
                env.SPOTBUGS_EFFORT = 'Max'
                break
                
            case 'security':
                env.CHECKSTYLE_CONFIG = 'checkstyle-security.xml'
                env.PMD_RULESET = 'pmd-security.xml'
                env.SPOTBUGS_EFFORT = 'Max'
                env.ENABLE_SECURITY_RULES = 'true'
                break
        }
        
        echo "分析級別: ${params.ANALYSIS_LEVEL}"
        echo "Checkstyle 配置: ${env.CHECKSTYLE_CONFIG}"
        echo "PMD 規則集: ${env.PMD_RULESET}"
        echo "SpotBugs 分析強度: ${env.SPOTBUGS_EFFORT}"
    }
}

def getCheckstyleProfile() {
    switch(params.ANALYSIS_LEVEL) {
        case 'strict':
        case 'security':
            return 'code-quality'
        default:
            return 'default'
    }
}

def runSonarQubeAnalysis() {
    echo "執行 SonarQube 分析..."
    
    def sonarArgs = [
        "-Dsonar.login=${SONAR_TOKEN}",
        "-Dsonar.host.url=${env.SONAR_HOST_URL}",
        "-Dsonar.projectKey=${env.SONAR_PROJECT_KEY}",
        "-Dsonar.projectName=${env.JOB_NAME}",
        "-Dsonar.projectVersion=${env.BUILD_NUMBER}",
        "-Dsonar.sources=src/main/java",
        "-Dsonar.tests=src/test/java",
        "-Dsonar.java.binaries=target/classes",
        "-Dsonar.java.test.binaries=target/test-classes",
        "-Dsonar.jacoco.reportPaths=target/jacoco.exec",
        "-Dsonar.junit.reportPaths=target/surefire-reports",
        "-Dsonar.surefire.reportsPath=target/surefire-reports"
    ]
    
    // 根據建置類型添加特定參數
    if (env.CHANGE_ID) {
        // Pull Request 分析
        sonarArgs.addAll([
            "-Dsonar.pullrequest.key=${env.CHANGE_ID}",
            "-Dsonar.pullrequest.branch=${env.CHANGE_BRANCH}",
            "-Dsonar.pullrequest.base=${env.CHANGE_TARGET}"
        ])
    } else {
        // 分支分析
        sonarArgs.add("-Dsonar.branch.name=${env.BRANCH_NAME}")
    }
    
    // 安全分析額外參數
    if (params.ANALYSIS_LEVEL == 'security') {
        sonarArgs.addAll([
            "-Dsonar.security.hotspots.includeNewCode=true",
            "-Dsonar.security.review.enabled=true"
        ])
    }
    
    def sonarArgsString = sonarArgs.join(' ')
    sh "mvn sonar:sonar ${sonarArgsString}"
}

def evaluateQualityGate() {
    echo "等待 SonarQube Quality Gate 結果..."
    
    timeout(time: env.QUALITY_GATE_TIMEOUT as Integer, unit: 'MINUTES') {
        script {
            def qg = waitForQualityGate()
            
            env.QUALITY_GATE_STATUS = qg.status
            
            echo "Quality Gate 狀態: ${qg.status}"
            
            if (qg.status != 'OK') {
                def conditions = qg.conditions ?: []
                conditions.each { condition ->
                    if (condition.status != 'OK') {
                        echo "❌ ${condition.metricKey}: ${condition.actualValue} (門檻: ${condition.errorThreshold})"
                    }
                }
                
                if (params.FAIL_ON_QUALITY_GATE) {
                    error "SonarQube Quality Gate 失敗: ${qg.status}"
                } else {
                    echo "⚠️ Quality Gate 失敗但設定為繼續建置"
                    currentBuild.result = 'UNSTABLE'
                }
            } else {
                echo "✅ SonarQube Quality Gate 通過"
            }
        }
    }
}

def generateAnalysisReport() {
    echo "生成程式碼分析報告..."
    
    script {
        // 收集各工具的分析結果
        def analysisData = [:]
        
        // Checkstyle 結果
        if (fileExists('target/checkstyle-result.xml')) {
            def checkstyleViolations = sh(
                script: "xmlstarlet sel -t -v 'count(//error)' target/checkstyle-result.xml",
                returnStdout: true
            ).trim()
            analysisData['checkstyle'] = checkstyleViolations
        }
        
        // PMD 結果
        if (fileExists('target/pmd.xml')) {
            def pmdViolations = sh(
                script: "xmlstarlet sel -t -v 'count(//violation)' target/pmd.xml",
                returnStdout: true
            ).trim()
            analysisData['pmd'] = pmdViolations
        }
        
        // SpotBugs 結果
        if (fileExists('target/spotbugsXml.xml')) {
            def spotbugsViolations = sh(
                script: "xmlstarlet sel -t -v 'count(//BugInstance)' target/spotbugsXml.xml",
                returnStdout: true
            ).trim()
            analysisData['spotbugs'] = spotbugsViolations
        }
        
        // 生成 HTML 報告
        def reportHtml = generateAnalysisReportHtml(analysisData)
        writeFile file: 'target/analysis-reports/code-analysis-report.html', text: reportHtml
        
        publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: 'target/analysis-reports',
            reportFiles: 'code-analysis-report.html',
            reportName: 'Code Analysis Report'
        ])
    }
}

def generateAnalysisReportHtml(analysisData) {
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>程式碼分析報告</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .header { background-color: #f5f5f5; padding: 15px; border-radius: 5px; }
            .metric-card { 
                display: inline-block; 
                margin: 10px; 
                padding: 15px; 
                border: 1px solid #ddd; 
                border-radius: 5px; 
                text-align: center; 
                width: 150px;
            }
            .metric-value { font-size: 2em; font-weight: bold; }
            .metric-label { color: #666; }
            .good { color: #28a745; }
            .warning { color: #ffc107; }
            .danger { color: #dc3545; }
            .recommendations { margin-top: 30px; }
            .recommendations ul { list-style-type: none; padding: 0; }
            .recommendations li { 
                margin: 10px 0; 
                padding: 10px; 
                background-color: #f8f9fa; 
                border-left: 4px solid #007bff; 
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>程式碼分析報告</h1>
            <p>建置編號: ${env.BUILD_NUMBER}</p>
            <p>分析時間: ${new Date()}</p>
            <p>分析級別: ${params.ANALYSIS_LEVEL}</p>
        </div>
        
        <h2>分析結果概覽</h2>
        <div class="metrics">
            <div class="metric-card">
                <div class="metric-value ${getStatusClass(analysisData.checkstyle)}">${analysisData.checkstyle ?: '0'}</div>
                <div class="metric-label">Checkstyle 違規</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-value ${getStatusClass(analysisData.pmd)}">${analysisData.pmd ?: '0'}</div>
                <div class="metric-label">PMD 違規</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-value ${getStatusClass(analysisData.spotbugs)}">${analysisData.spotbugs ?: '0'}</div>
                <div class="metric-label">SpotBugs 錯誤</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-value ${env.QUALITY_GATE_STATUS == 'OK' ? 'good' : 'danger'}">${env.QUALITY_GATE_STATUS ?: 'N/A'}</div>
                <div class="metric-label">Quality Gate</div>
            </div>
        </div>
        
        <div class="recommendations">
            <h2>改善建議</h2>
            <ul>
                <li>📋 定期檢視並修復 Checkstyle 風格問題</li>
                <li>🔍 關注 PMD 報告的程式碼品質建議</li>
                <li>🐛 優先修復 SpotBugs 發現的潛在錯誤</li>
                <li>🎯 維持 SonarQube Quality Gate 通過狀態</li>
                <li>📈 持續監控程式碼品質趨勢</li>
            </ul>
        </div>
        
        <h2>快速連結</h2>
        <ul>
            <li><a href="../Checkstyle_20Report/">Checkstyle 詳細報告</a></li>
            <li><a href="../PMD_20Report/">PMD 詳細報告</a></li>
            <li><a href="../SpotBugs_20Report/">SpotBugs 詳細報告</a></li>
            <li><a href="${env.SONAR_HOST_URL}/dashboard?id=${env.SONAR_PROJECT_KEY}">SonarQube 儀表板</a></li>
        </ul>
    </body>
    </html>
    """
}

def getStatusClass(value) {
    if (!value || value == '0') return 'good'
    def intValue = value as Integer
    if (intValue <= 5) return 'good'
    if (intValue <= 20) return 'warning'
    return 'danger'
}

def generateTrendAnalysis() {
    script {
        // 記錄趨勢數據
        def trendData = "${env.BUILD_NUMBER},${analysisData.checkstyle ?: 0},${analysisData.pmd ?: 0},${analysisData.spotbugs ?: 0},${env.QUALITY_GATE_STATUS ?: 'UNKNOWN'},${new Date().format('yyyy-MM-dd')}"
        
        writeFile file: 'analysis-trend.csv', text: trendData + '\n'
        
        // 如果存在歷史數據，合併
        if (fileExists('analysis-history.csv')) {
            sh 'cat analysis-history.csv analysis-trend.csv > temp.csv && mv temp.csv analysis-history.csv'
        } else {
            sh 'echo "build,checkstyle,pmd,spotbugs,quality_gate,date" > analysis-history.csv'
            sh 'cat analysis-trend.csv >> analysis-history.csv'
        }
        
        archiveArtifacts artifacts: 'analysis-history.csv'
    }
}

def collectAnalysisResults() {
    script {
        // 收集所有分析結果文件
        sh '''
            mkdir -p target/complete-analysis-results
            
            # 複製所有分析報告
            find target -name "*.xml" -path "*/site/*" -exec cp {} target/complete-analysis-results/ \\;
            find target -name "*.html" -path "*/site/*" -exec cp {} target/complete-analysis-results/ \\;
            
            # 複製 SonarQube 相關文件
            if [ -d ".sonar" ]; then
                cp -r .sonar target/complete-analysis-results/
            fi
        '''
        
        archiveArtifacts(
            artifacts: 'target/complete-analysis-results/**',
            allowEmptyArchive: true
        )
    }
}

def generateSummaryReport() {
    script {
        def summary = """
        ═══════════════════════════════════════════════════════════
                           程式碼品質分析摘要
        ═══════════════════════════════════════════════════════════
        
        建置資訊:
        ├─ 專案: ${env.JOB_NAME}
        ├─ 建置編號: ${env.BUILD_NUMBER}
        ├─ 分析級別: ${params.ANALYSIS_LEVEL}
        ├─ Git 分支: ${env.BRANCH_NAME}
        └─ 分析時間: ${new Date()}
        
        分析結果:
        ├─ Checkstyle 違規: ${analysisData?.checkstyle ?: '0'}
        ├─ PMD 違規: ${analysisData?.pmd ?: '0'}
        ├─ SpotBugs 錯誤: ${analysisData?.spotbugs ?: '0'}
        └─ Quality Gate: ${env.QUALITY_GATE_STATUS ?: 'N/A'}
        
        建置狀態: ${currentBuild.result ?: 'SUCCESS'}
        
        ═══════════════════════════════════════════════════════════
        """
        
        echo summary
        writeFile file: 'code-quality-summary.txt', text: summary
        archiveArtifacts artifacts: 'code-quality-summary.txt'
    }
}

def handleAnalysisFailure() {
    script {
        echo "程式碼分析失敗，收集診斷資訊..."
        
        sh '''
            echo "=== 分析失敗診斷 ===" > analysis-failure-diagnosis.txt
            echo "失敗時間: $(date)" >> analysis-failure-diagnosis.txt
            echo "失敗階段: ${STAGE_NAME}" >> analysis-failure-diagnosis.txt
            echo "" >> analysis-failure-diagnosis.txt
            
            echo "=== 工具版本資訊 ===" >> analysis-failure-diagnosis.txt
            mvn -version >> analysis-failure-diagnosis.txt
            echo "" >> analysis-failure-diagnosis.txt
            
            echo "=== 專案結構 ===" >> analysis-failure-diagnosis.txt
            find . -name "*.java" | head -20 >> analysis-failure-diagnosis.txt
            echo "" >> analysis-failure-diagnosis.txt
            
            echo "=== Maven 依賴樹 ===" >> analysis-failure-diagnosis.txt
            mvn dependency:tree | head -50 >> analysis-failure-diagnosis.txt
        '''
        
        archiveArtifacts artifacts: 'analysis-failure-diagnosis.txt'
        
        // 發送失敗通知
        emailext(
            subject: "🔍 程式碼分析失敗: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """
                程式碼分析失敗通知
                
                專案: ${env.JOB_NAME}
                建置編號: ${env.BUILD_NUMBER}
                失敗階段: ${env.STAGE_NAME}
                分析級別: ${params.ANALYSIS_LEVEL}
                
                請檢查分析日誌並修復相關問題。
                
                建置日誌: ${env.BUILD_URL}console
                分析報告: ${env.BUILD_URL}artifact/analysis-failure-diagnosis.txt
            """,
            to: 'dev-team@company.com'
        )
    }
}
```

### 💡 實務案例

#### 案例：企業級程式碼品質治理

**情境**：為大型企業建立統一的程式碼品質標準和自動化檢查機制

**解決方案包含：**

1. **分層的程式碼品質標準**
2. **自動化的品質門檻**
3. **持續的品質監控**
4. **團隊協作的品質改善流程**

```groovy
// 企業級程式碼品質治理 Pipeline
pipeline {
    agent none
    
    parameters {
        choice(
            name: 'QUALITY_PROFILE',
            choices: ['development', 'integration', 'release', 'critical'],
            description: '品質檢查設定檔'
        )
    }
    
    stages {
        stage('Quality Profile Setup') {
            agent any
            steps {
                script {
                    setupQualityProfile(params.QUALITY_PROFILE)
                }
            }
        }
        
        stage('Multi-Level Analysis') {
            parallel {
                stage('Code Style & Format') {
                    agent { label 'analysis' }
                    steps {
                        runCodeStyleAnalysis()
                    }
                }
                
                stage('Code Quality & Complexity') {
                    agent { label 'analysis' }
                    steps {
                        runCodeQualityAnalysis()
                    }
                }
                
                stage('Security & Vulnerability') {
                    agent { label 'security' }
                    steps {
                        runSecurityAnalysis()
                    }
                }
                
                stage('Architecture Compliance') {
                    agent { label 'architecture' }
                    steps {
                        runArchitectureAnalysis()
                    }
                }
            }
        }
        
        stage('Quality Gate Evaluation') {
            agent any
            steps {
                script {
                    evaluateEnterpriseQualityGate()
                }
            }
        }
        
        stage('Quality Metrics Dashboard') {
            agent any
            steps {
                script {
                    generateQualityDashboard()
                }
            }
        }
    }
}

def setupQualityProfile(profile) {
    def profiles = [
        'development': [
            checkstyleConfig: 'checkstyle-dev.xml',
            pmdRuleset: 'pmd-dev.xml',
            securityLevel: 'basic',
            coverageThreshold: 60
        ],
        'integration': [
            checkstyleConfig: 'checkstyle-standard.xml',
            pmdRuleset: 'pmd-standard.xml',
            securityLevel: 'standard',
            coverageThreshold: 70
        ],
        'release': [
            checkstyleConfig: 'checkstyle-strict.xml',
            pmdRuleset: 'pmd-strict.xml',
            securityLevel: 'strict',
            coverageThreshold: 80
        ],
        'critical': [
            checkstyleConfig: 'checkstyle-critical.xml',
            pmdRuleset: 'pmd-critical.xml',
            securityLevel: 'critical',
            coverageThreshold: 90
        ]
    ]
    
    def config = profiles[profile]
    
    env.CHECKSTYLE_CONFIG = config.checkstyleConfig
    env.PMD_RULESET = config.pmdRuleset
    env.SECURITY_LEVEL = config.securityLevel
    env.COVERAGE_THRESHOLD = config.coverageThreshold.toString()
    
    echo "設定品質檢查設定檔: ${profile}"
    echo "覆蓋率門檻: ${env.COVERAGE_THRESHOLD}%"
}

def runCodeStyleAnalysis() {
    // 程式碼風格分析實作
    sh """
        mvn checkstyle:check -Dcheckstyle.config.location=${env.CHECKSTYLE_CONFIG}
        mvn formatter:validate
        mvn impsort:check
    """
}

def runCodeQualityAnalysis() {
    // 程式碼品質分析實作
    sh """
        mvn pmd:check -Dpmd.ruleset=${env.PMD_RULESET}
        mvn spotbugs:check
        mvn jacoco:check -Djacoco.haltOnFailure=false
    """
}

def runSecurityAnalysis() {
    // 安全分析實作
    def securityCommands = [
        'basic': 'mvn dependency-check:check -DfailBuildOnCVSS=8',
        'standard': 'mvn dependency-check:check -DfailBuildOnCVSS=7',
        'strict': 'mvn dependency-check:check -DfailBuildOnCVSS=5',
        'critical': 'mvn dependency-check:check -DfailBuildOnCVSS=3'
    ]
    
    sh securityCommands[env.SECURITY_LEVEL]
}

def runArchitectureAnalysis() {
    // 架構合規檢查實作
    sh '''
        mvn archunit:test
        mvn dependency:analyze
        mvn enforcer:enforce
    '''
}

def evaluateEnterpriseQualityGate() {
    // 企業級品質門檻評估
    script {
        def qualityResults = [:]
        
        // 收集各項指標
        qualityResults.codeStyle = getCheckstyleViolationCount()
        qualityResults.codeQuality = getPmdViolationCount()
        qualityResults.bugs = getSpotBugsCount()
        qualityResults.coverage = getCodeCoverage()
        qualityResults.security = getSecurityVulnerabilityCount()
        
        // 評估總體品質
        def overallQuality = calculateOverallQuality(qualityResults)
        
        // 決定建置結果
        if (overallQuality < 70) {
            currentBuild.result = 'FAILURE'
            error "程式碼品質不符合企業標準: ${overallQuality}%"
        } else if (overallQuality < 85) {
            currentBuild.result = 'UNSTABLE'
            echo "警告: 程式碼品質需要改善: ${overallQuality}%"
        } else {
            echo "程式碼品質符合企業標準: ${overallQuality}%"
        }
        
        env.OVERALL_QUALITY = overallQuality.toString()
    }
}

def generateQualityDashboard() {
    // 生成企業級品質儀表板
    script {
        def dashboardData = collectQualityMetrics()
        def dashboardHtml = generateEnterpriseQualityDashboard(dashboardData)
        
        writeFile file: 'enterprise-quality-dashboard.html', text: dashboardHtml
        
        publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: '.',
            reportFiles: 'enterprise-quality-dashboard.html',
            reportName: 'Enterprise Quality Dashboard'
        ])
    }
}
```

### ⚠️ 注意事項

1. **工具配置**：
   - 保持工具版本的一致性
   - 定期更新規則集
   - 建立例外處理機制

2. **效能優化**：
   - 使用分析快取
   - 並行執行分析工具
   - 避免重複分析

3. **報告管理**：
   - 建立報告保留策略
   - 提供趨勢分析
   - 確保報告的可存取性

4. **團隊協作**：
   - 建立品質標準文件
   - 提供修復指南
   - 實施品質教育訓練

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| 靜態分析工具 | Checkstyle、PMD、SpotBugs 配置 |
| SonarQube 整合 | Quality Gate、分析配置 |
| 安全檢查 | OWASP 工具、漏洞檢測 |
| 品質治理 | 企業標準、自動化決策 |

### 📝 練習作業

1. **基礎練習**：配置基本的靜態程式碼分析工具
2. **進階練習**：建立多層次的程式碼品質檢查機制
3. **實務練習**：實施企業級的程式碼品質治理策略

---

## 總結

恭喜您完成了 Jenkins CI/CD 教學手冊的前12章！您已經學習了：

### 已完成章節回顧

1. **第1-4章**：Jenkins 基礎架構和環境設定
2. **第5-8章**：專案類型和基本整合
3. **第9-12章**：Pipeline 進階應用和品質控制

### 技能掌握檢核

✅ Jenkins 安裝和基本配置  
✅ 使用者和權限管理  
✅ Plugin 生態系統應用  
✅ Freestyle Project 建立  
✅ 憑證和安全管理  
✅ Git 整合和版本控制  
✅ Maven 專案建置  
✅ Pipeline 語法和結構  
✅ Jenkinsfile 深度應用  
✅ 測試整合和覆蓋率  
✅ 靜態程式碼分析  
✅ 品質門檻和自動化決策  

### 下一步學習建議

繼續學習第13-19章，將涵蓋：

- Pipeline 故障排除和最佳實務
- 部署策略和環境管理
- 監控和效能優化
- 企業級 CI/CD 架構設計

持續實務練習，將理論知識轉化為實際技能！

---

## 第13章 Pipeline 故障排除與除錯技巧

### 🎯 學習目標

- 掌握 Pipeline 常見問題的診斷方法
- 學會使用 Jenkins 內建的除錯工具
- 建立系統性的故障排除流程
- 實施預防性的錯誤處理機制

### 📚 核心概念

#### 13.1 Pipeline 故障診斷架構

Jenkins Pipeline 的故障排除需要系統性的方法，從日誌分析到效能監控的全方位診斷。

```mermaid
graph TB
    A[Pipeline 故障] --> B[初步診斷]
    B --> C[日誌分析]
    B --> D[環境檢查]
    B --> E[資源監控]
    
    C --> F[Console Log]
    C --> G[Build Log]
    C --> H[Agent Log]
    C --> I[System Log]
    
    D --> J[Node 狀態]
    D --> K[工具版本]
    D --> L[權限檢查]
    D --> M[網路連線]
    
    E --> N[CPU 使用率]
    E --> O[記憶體使用]
    E --> P[磁碟空間]
    E --> Q[網路頻寬]
    
    F --> R[錯誤訊息提取]
    G --> R
    H --> R
    I --> R
    
    J --> S[環境修復]
    K --> S
    L --> S
    M --> S
    
    N --> T[資源調整]
    O --> T
    P --> T
    Q --> T
    
    R --> U[問題分類]
    S --> U
    T --> U
    
    U --> V[語法錯誤]
    U --> W[環境問題]
    U --> X[資源問題]
    U --> Y[權限問題]
    U --> Z[整合問題]
    
    V --> AA[解決方案]
    W --> AA
    X --> AA
    Y --> AA
    Z --> AA
    
    subgraph "預防機制"
        BB[健康檢查]
        CC[資源監控]
        DD[自動重試]
        EE[錯誤通知]
        FF[日誌保留]
    end
    
    subgraph "除錯工具"
        GG[Jenkins CLI]
        HH[Script Console]
        II[Blue Ocean]
        JJ[Pipeline Steps Reference]
        KK[Groovy Sandbox]
    end
```

#### 13.2 常見 Pipeline 錯誤類型與解決方案

**語法錯誤診斷：**

```groovy
// 常見錯誤示例和修復方法
pipeline {
    agent any
    
    stages {
        stage('語法檢查示範') {
            steps {
                script {
                    try {
                        // 常見錯誤 1: 未正確引用變數
                        // 錯誤寫法
                        // echo "Build number: $BUILD_NUMBER"  // 在 script 區塊中應使用 env
                        
                        // 正確寫法
                        echo "Build number: ${env.BUILD_NUMBER}"
                        
                        // 常見錯誤 2: 字串插值問題
                        def version = "1.0.0"
                        // 錯誤寫法
                        // sh 'echo "Version: $version"'  // 單引號不支援字串插值
                        
                        // 正確寫法
                        sh "echo 'Version: ${version}'"
                        
                        // 常見錯誤 3: 並行區塊結構錯誤
                        // 錯誤寫法示例（會在實際範例中修正）
                        
                    } catch (Exception e) {
                        echo "捕獲錯誤: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
        stage('環境診斷') {
            steps {
                script {
                    // 系統環境檢查
                    environmentDiagnostics()
                    
                    // 工具版本檢查
                    toolVersionCheck()
                    
                    // 權限檢查
                    permissionCheck()
                }
            }
        }
        
        stage('資源診斷') {
            steps {
                script {
                    // 資源使用情況檢查
                    resourceDiagnostics()
                    
                    // 網路連線檢查
                    networkConnectivityCheck()
                }
            }
        }
    }
    
    post {
        failure {
            script {
                // 失敗時的詳細診斷
                detailedFailureDiagnostics()
                
                // 收集診斷資訊
                collectDiagnosticInfo()
            }
        }
    }
}

// === 診斷函式庫 ===

def environmentDiagnostics() {
    echo "=== 環境診斷 ==="
    
    // 檢查 Jenkins 版本
    def jenkinsVersion = Jenkins.instance.getVersion()
    echo "Jenkins 版本: ${jenkinsVersion}"
    
    // 檢查 Node 資訊
    def nodeInfo = sh(script: 'uname -a', returnStdout: true).trim()
    echo "節點資訊: ${nodeInfo}"
    
    // 檢查環境變數
    sh '''
        echo "=== 重要環境變數 ==="
        echo "JAVA_HOME: ${JAVA_HOME:-未設定}"
        echo "PATH: ${PATH}"
        echo "WORKSPACE: ${WORKSPACE:-未設定}"
        echo "BUILD_NUMBER: ${BUILD_NUMBER:-未設定}"
        echo "JOB_NAME: ${JOB_NAME:-未設定}"
    '''
    
    // 檢查 Java 版本
    try {
        def javaVersion = sh(script: 'java -version 2>&1', returnStdout: true)
        echo "Java 版本:\n${javaVersion}"
    } catch (Exception e) {
        echo "⚠️ Java 版本檢查失敗: ${e.getMessage()}"
    }
}

def toolVersionCheck() {
    echo "=== 工具版本檢查 ==="
    
    def tools = [
        'maven': 'mvn -version',
        'git': 'git --version',
        'docker': 'docker --version',
        'node': 'node --version',
        'npm': 'npm --version'
    ]
    
    tools.each { tool, command ->
        try {
            def version = sh(script: command, returnStdout: true).trim()
            echo "${tool}: ${version}"
        } catch (Exception e) {
            echo "⚠️ ${tool} 未安裝或不可用: ${e.getMessage()}"
        }
    }
}

def permissionCheck() {
    echo "=== 權限檢查 ==="
    
    // 檢查工作空間權限
    sh '''
        echo "工作空間權限:"
        ls -la ${WORKSPACE} || echo "無法存取工作空間"
        
        echo "當前使用者:"
        whoami
        
        echo "使用者群組:"
        groups
        
        echo "可寫入目錄測試:"
        touch ${WORKSPACE}/permission_test.tmp && rm ${WORKSPACE}/permission_test.tmp && echo "✅ 可寫入" || echo "❌ 無法寫入"
    '''
    
    // 檢查 Docker 權限（如果適用）
    try {
        sh 'docker ps > /dev/null 2>&1'
        echo "✅ Docker 權限正常"
    } catch (Exception e) {
        echo "⚠️ Docker 權限問題或 Docker 未安裝"
    }
}

def resourceDiagnostics() {
    echo "=== 資源診斷 ==="
    
    // CPU 使用率
    sh '''
        echo "=== CPU 資訊 ==="
        nproc
        cat /proc/loadavg
        
        echo "=== 記憶體使用 ==="
        free -h
        
        echo "=== 磁碟使用 ==="
        df -h
        
        echo "=== 程序資訊 ==="
        ps aux | head -10
    '''
}

def networkConnectivityCheck() {
    echo "=== 網路連線檢查 ==="
    
    def endpoints = [
        'google.com:80',
        'github.com:443',
        'maven.repository.com:443'
    ]
    
    endpoints.each { endpoint ->
        try {
            def (host, port) = endpoint.split(':')
            sh "timeout 5 bash -c '</dev/tcp/${host}/${port}' && echo '✅ ${endpoint} 可連線' || echo '❌ ${endpoint} 無法連線'"
        } catch (Exception e) {
            echo "⚠️ ${endpoint} 連線測試失敗: ${e.getMessage()}"
        }
    }
}

def detailedFailureDiagnostics() {
    echo "=== 詳細失敗診斷 ==="
    
    // 分析建置失敗原因
    def buildResult = currentBuild.result
    def failedStage = env.STAGE_NAME ?: '未知階段'
    
    echo "建置結果: ${buildResult}"
    echo "失敗階段: ${failedStage}"
    
    // 檢查最近的錯誤日誌
    try {
        def recentLogs = sh(
            script: 'tail -100 /var/log/jenkins/jenkins.log 2>/dev/null || echo "無法存取 Jenkins 日誌"',
            returnStdout: true
        )
        echo "最近的 Jenkins 日誌:\n${recentLogs}"
    } catch (Exception e) {
        echo "無法讀取 Jenkins 日誌: ${e.getMessage()}"
    }
    
    // 檢查 Agent 狀態
    def nodeName = env.NODE_NAME ?: 'master'
    echo "當前節點: ${nodeName}"
    
    // 收集系統狀態
    sh '''
        echo "=== 系統狀態快照 ==="
        date
        uptime
        last | head -5
    '''
}

def collectDiagnosticInfo() {
    echo "收集診斷資訊..."
    
    // 建立診斷報告
    sh '''
        mkdir -p diagnostic-reports
        
        # 基本系統資訊
        {
            echo "=== 診斷報告 - $(date) ==="
            echo "建置編號: ${BUILD_NUMBER}"
            echo "專案: ${JOB_NAME}"
            echo "失敗階段: ${STAGE_NAME:-未知}"
            echo "節點: ${NODE_NAME:-master}"
            echo ""
            
            echo "=== 系統資訊 ==="
            uname -a
            echo ""
            
            echo "=== Java 版本 ==="
            java -version 2>&1
            echo ""
            
            echo "=== 環境變數 ==="
            env | grep -E "(JAVA_HOME|PATH|WORKSPACE|BUILD_)" | sort
            echo ""
            
            echo "=== 磁碟使用 ==="
            df -h
            echo ""
            
            echo "=== 記憶體使用 ==="
            free -h
            echo ""
            
        } > diagnostic-reports/system-info.txt
        
        # Maven 資訊（如果適用）
        if command -v mvn >/dev/null 2>&1; then
            {
                echo "=== Maven 版本 ==="
                mvn -version
                echo ""
                
                echo "=== Maven 設定 ==="
                mvn help:effective-settings 2>/dev/null | head -50 || echo "無法取得 Maven 設定"
                echo ""
                
            } > diagnostic-reports/maven-info.txt
        fi
        
        # Git 資訊
        if [ -d .git ]; then
            {
                echo "=== Git 資訊 ==="
                git status
                echo ""
                git log --oneline -5
                echo ""
                git remote -v
                echo ""
                
            } > diagnostic-reports/git-info.txt
        fi
    '''
    
    // 保存診斷報告
    archiveArtifacts(
        artifacts: 'diagnostic-reports/**',
        allowEmptyArchive: true
    )
}
```

#### 13.3 進階除錯技術

**使用 Jenkins Script Console 進行除錯：**

```groovy
// Script Console 除錯範例
pipeline {
    agent any
    
    stages {
        stage('Script Console 除錯示範') {
            steps {
                script {
                    // 啟用詳細日誌
                    enableVerboseLogging()
                    
                    // 動態調整日誌級別
                    adjustLogLevel('DEBUG')
                    
                    // 即時變數檢查
                    inspectVariables()
                    
                    // Pipeline 狀態檢查
                    checkPipelineState()
                }
            }
        }
        
        stage('Groovy Sandbox 除錯') {
            steps {
                script {
                    // 安全的 Groovy 程式碼除錯
                    debugGroovyCode()
                    
                    // 方法調用追蹤
                    traceMethodCalls()
                }
            }
        }
        
        stage('Blue Ocean 除錯資訊') {
            steps {
                script {
                    // 為 Blue Ocean 添加除錯資訊
                    addBlueOceanDebugInfo()
                }
            }
        }
    }
}

def enableVerboseLogging() {
    echo "啟用詳細日誌記錄..."
    
    // 設定環境變數以啟用詳細日誌
    env.MAVEN_OPTS = "${env.MAVEN_OPTS ?: ''} -X"
    env.JENKINS_DEBUG = 'true'
    
    echo "詳細日誌已啟用"
}

def adjustLogLevel(level) {
    echo "調整日誌級別為: ${level}"
    
    // 動態調整 Logger 級別
    script {
        def logger = java.util.logging.Logger.getLogger("jenkins.pipeline")
        def logLevel = java.util.logging.Level.parse(level)
        logger.setLevel(logLevel)
        
        echo "日誌級別已設定為: ${level}"
    }
}

def inspectVariables() {
    echo "=== 變數檢查 ==="
    
    // 檢查環境變數
    echo "重要環境變數:"
    env.getEnvironment().each { key, value ->
        if (key.startsWith('BUILD_') || key.startsWith('JOB_') || key.startsWith('GIT_')) {
            echo "  ${key} = ${value}"
        }
    }
    
    // 檢查 Pipeline 特定變數
    echo "Pipeline 變數:"
    echo "  currentBuild.number = ${currentBuild.number}"
    echo "  currentBuild.result = ${currentBuild.result ?: 'SUCCESS'}"
    echo "  currentBuild.duration = ${currentBuild.duration ?: 0}"
    
    // 檢查參數
    if (params) {
        echo "建置參數:"
        params.each { key, value ->
            echo "  ${key} = ${value}"
        }
    } else {
        echo "無建置參數"
    }
}

def checkPipelineState() {
    echo "=== Pipeline 狀態檢查 ==="
    
    // 檢查當前階段
    echo "當前階段: ${env.STAGE_NAME}"
    
    // 檢查 Agent 資訊
    echo "執行節點: ${env.NODE_NAME ?: 'master'}"
    echo "工作空間: ${env.WORKSPACE}"
    
    // 檢查建置歷史
    def previousBuild = currentBuild.previousBuild
    if (previousBuild) {
        echo "上次建置結果: ${previousBuild.result}"
        echo "上次建置時間: ${new Date(previousBuild.timeInMillis)}"
    } else {
        echo "這是第一次建置"
    }
    
    // 檢查變更集
    def changeSet = currentBuild.changeSets
    if (changeSet) {
        echo "變更數量: ${changeSet.size()}"
        changeSet.each { change ->
            echo "  變更: ${change.commitId} - ${change.msg}"
        }
    } else {
        echo "無程式碼變更"
    }
}

def debugGroovyCode() {
    echo "=== Groovy 程式碼除錯 ==="
    
    try {
        // 除錯 Groovy 語法
        def testCode = '''
            def message = "Hello, Jenkins!"
            return message.toUpperCase()
        '''
        
        def result = evaluate(testCode)
        echo "Groovy 測試結果: ${result}"
        
        // 除錯物件檢查
        inspectGroovyObjects()
        
    } catch (Exception e) {
        echo "Groovy 除錯失敗: ${e.getMessage()}"
        echo "堆疊追蹤: ${e.getStackTrace().join('\n')}"
    }
}

def inspectGroovyObjects() {
    // 檢查 Jenkins 物件
    echo "Jenkins 實例資訊:"
    def jenkins = Jenkins.instance
    echo "  版本: ${jenkins.version}"
    echo "  根目錄: ${jenkins.rootDir}"
    echo "  節點數量: ${jenkins.nodes.size()}"
    
    // 檢查當前工作
    def job = Jenkins.instance.getItemByFullName(env.JOB_NAME)
    if (job) {
        echo "工作資訊:"
        echo "  顯示名稱: ${job.displayName}"
        echo "  描述: ${job.description ?: '無描述'}"
        echo "  最後建置: ${job.lastBuild?.number ?: '無'}"
    }
}

def traceMethodCalls() {
    echo "=== 方法調用追蹤 ==="
    
    // 包裝方法以進行追蹤
    def originalSh = this.&sh
    
    this.metaClass.sh = { String command ->
        echo "🔍 執行 shell 命令: ${command}"
        def startTime = System.currentTimeMillis()
        
        try {
            def result = originalSh(command)
            def duration = System.currentTimeMillis() - startTime
            echo "✅ 命令執行成功，耗時: ${duration}ms"
            return result
        } catch (Exception e) {
            def duration = System.currentTimeMillis() - startTime
            echo "❌ 命令執行失敗，耗時: ${duration}ms，錯誤: ${e.getMessage()}"
            throw e
        }
    }
}

def addBlueOceanDebugInfo() {
    echo "=== Blue Ocean 除錯資訊 ==="
    
    // 添加 Blue Ocean 可視化的除錯資訊
    def debugInfo = [
        timestamp: new Date(),
        buildNumber: env.BUILD_NUMBER,
        stageName: env.STAGE_NAME,
        nodeName: env.NODE_NAME,
        workspace: env.WORKSPACE
    ]
    
    // 將除錯資訊寫入檔案供 Blue Ocean 顯示
    writeJSON file: 'debug-info.json', json: debugInfo
    
    // 建立除錯標記
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '.',
        reportFiles: 'debug-info.json',
        reportName: 'Debug Info'
    ])
}
```

#### 13.4 效能問題診斷

**Pipeline 效能監控與優化：**

```groovy
pipeline {
    agent none
    
    options {
        // 啟用時間戳記
        timestamps()
        
        // 設定超時
        timeout(time: 60, unit: 'MINUTES')
        
        // 啟用 Profiler
        skipDefaultCheckout()
    }
    
    stages {
        stage('效能基準測量') {
            agent any
            steps {
                script {
                    // 記錄開始時間
                    def stageStartTime = System.currentTimeMillis()
                    
                    // 執行基準測試
                    performanceBenchmark()
                    
                    // 記錄結束時間
                    def stageDuration = System.currentTimeMillis() - stageStartTime
                    echo "階段執行時間: ${stageDuration}ms"
                    
                    // 記錄效能資料
                    recordPerformanceData('benchmark', stageDuration)
                }
            }
        }
        
        stage('並行效能測試') {
            parallel {
                stage('CPU 密集任務') {
                    agent { label 'cpu-intensive' }
                    steps {
                        script {
                            measureExecutionTime('CPU 密集任務') {
                                // 模擬 CPU 密集任務
                                sh 'for i in {1..1000}; do echo $i > /dev/null; done'
                            }
                        }
                    }
                }
                
                stage('I/O 密集任務') {
                    agent { label 'io-intensive' }
                    steps {
                        script {
                            measureExecutionTime('I/O 密集任務') {
                                // 模擬 I/O 密集任務
                                sh 'find /usr -name "*.so" > /dev/null 2>&1 || true'
                            }
                        }
                    }
                }
                
                stage('網路密集任務') {
                    agent { label 'network-intensive' }
                    steps {
                        script {
                            measureExecutionTime('網路密集任務') {
                                // 模擬網路密集任務
                                sh 'for url in google.com github.com; do curl -s $url > /dev/null; done'
                            }
                        }
                    }
                }
            }
        }
        
        stage('記憶體使用分析') {
            agent any
            steps {
                script {
                    analyzeMemoryUsage()
                }
            }
        }
        
        stage('瓶頸識別') {
            agent any
            steps {
                script {
                    identifyBottlenecks()
                }
            }
        }
    }
    
    post {
        always {
            node('master') {
                script {
                    // 生成效能報告
                    generatePerformanceReport()
                    
                    // 分析效能趨勢
                    analyzePerformanceTrends()
                }
            }
        }
    }
}

def performanceBenchmark() {
    echo "執行效能基準測試..."
    
    // CPU 基準測試
    def cpuStartTime = System.currentTimeMillis()
    sh 'dd if=/dev/zero of=/dev/null bs=1M count=100 2>/dev/null'
    def cpuDuration = System.currentTimeMillis() - cpuStartTime
    env.CPU_BENCHMARK = cpuDuration.toString()
    
    // 磁碟 I/O 基準測試
    def ioStartTime = System.currentTimeMillis()
    sh 'dd if=/dev/zero of=test.tmp bs=1M count=10 && rm test.tmp'
    def ioDuration = System.currentTimeMillis() - ioStartTime
    env.IO_BENCHMARK = ioDuration.toString()
    
    echo "CPU 基準: ${cpuDuration}ms"
    echo "I/O 基準: ${ioDuration}ms"
}

def measureExecutionTime(taskName, closure) {
    def startTime = System.currentTimeMillis()
    echo "開始執行: ${taskName}"
    
    try {
        closure()
        def duration = System.currentTimeMillis() - startTime
        echo "✅ ${taskName} 完成，耗時: ${duration}ms"
        
        // 記錄到效能數據
        recordPerformanceData(taskName, duration)
        
        return duration
    } catch (Exception e) {
        def duration = System.currentTimeMillis() - startTime
        echo "❌ ${taskName} 失敗，耗時: ${duration}ms，錯誤: ${e.getMessage()}"
        throw e
    }
}

def recordPerformanceData(taskName, duration) {
    // 建立效能資料記錄
    def performanceData = [
        timestamp: new Date().format('yyyy-MM-dd HH:mm:ss'),
        buildNumber: env.BUILD_NUMBER,
        taskName: taskName,
        duration: duration,
        nodeName: env.NODE_NAME
    ]
    
    // 寫入效能資料檔案
    def dataFile = "performance-data-${env.BUILD_NUMBER}.json"
    def existingData = []
    
    if (fileExists(dataFile)) {
        existingData = readJSON file: dataFile
    }
    
    existingData.add(performanceData)
    writeJSON file: dataFile, json: existingData
}

def analyzeMemoryUsage() {
    echo "=== 記憶體使用分析 ==="
    
    // JVM 記憶體使用
    script {
        def runtime = Runtime.getRuntime()
        def maxMemory = runtime.maxMemory() / 1024 / 1024
        def totalMemory = runtime.totalMemory() / 1024 / 1024
        def freeMemory = runtime.freeMemory() / 1024 / 1024
        def usedMemory = totalMemory - freeMemory
        
        echo "JVM 記憶體使用:"
        echo "  最大記憶體: ${maxMemory} MB"
        echo "  已分配記憶體: ${totalMemory} MB"
        echo "  可用記憶體: ${freeMemory} MB"
        echo "  已使用記憶體: ${usedMemory} MB"
        echo "  使用率: ${(usedMemory/maxMemory*100).round(2)}%"
        
        // 記錄記憶體使用資料
        env.MEMORY_USAGE_PERCENT = ((usedMemory/maxMemory*100).round(2)).toString()
    }
    
    // 系統記憶體使用
    sh '''
        echo "系統記憶體使用:"
        free -h
        
        echo "程序記憶體使用 (前10名):"
        ps aux --sort=-%mem | head -11
    '''
}

def identifyBottlenecks() {
    echo "=== 瓶頸識別分析 ==="
    
    // 分析建置步驟耗時
    def buildSteps = currentBuild.rawBuild.getAction(org.jenkinsci.plugins.workflow.actions.WorkflowRunAction)?.getExecutionPromise()?.get()?.getAllNodes()
    
    if (buildSteps) {
        echo "建置步驟耗時分析:"
        buildSteps.each { node ->
            if (node.getAction(org.jenkinsci.plugins.workflow.actions.TimingAction)) {
                def timing = node.getAction(org.jenkinsci.plugins.workflow.actions.TimingAction)
                def duration = timing ? timing.getDuration() : 0
                echo "  ${node.getDisplayName()}: ${duration}ms"
            }
        }
    }
    
    // 檢查系統瓶頸
    sh '''
        echo "=== 系統瓶頸檢查 ==="
        
        echo "CPU 負載:"
        cat /proc/loadavg
        
        echo "磁碟 I/O 統計:"
        iostat -x 1 1 2>/dev/null || echo "iostat 不可用"
        
        echo "網路統計:"
        netstat -i
        
        echo "程序樹:"
        pstree -p $$ | head -10
    '''
    
    // 分析瓶頸並提供建議
    analyzeBottleneckSuggestions()
}

def analyzeBottleneckSuggestions() {
    script {
        def suggestions = []
        
        // 基於記憶體使用率提供建議
        def memoryUsage = (env.MEMORY_USAGE_PERCENT ?: '0') as Double
        if (memoryUsage > 80) {
            suggestions.add("記憶體使用率過高 (${memoryUsage}%)，建議增加 JVM 記憶體或優化代碼")
        }
        
        // 基於 CPU 基準提供建議
        def cpuBenchmark = (env.CPU_BENCHMARK ?: '0') as Long
        if (cpuBenchmark > 5000) {
            suggestions.add("CPU 效能較慢，建議使用更強的 Agent 或並行化處理")
        }
        
        // 基於 I/O 基準提供建議
        def ioBenchmark = (env.IO_BENCHMARK ?: '0') as Long
        if (ioBenchmark > 3000) {
            suggestions.add("磁碟 I/O 效能較慢，建議使用 SSD 或優化檔案操作")
        }
        
        if (suggestions.isEmpty()) {
            echo "✅ 未發現明顯的效能瓶頸"
        } else {
            echo "⚠️ 效能優化建議:"
            suggestions.each { suggestion ->
                echo "  - ${suggestion}"
            }
        }
        
        // 寫入建議到檔案
        writeFile file: 'performance-suggestions.txt', text: suggestions.join('\n')
        archiveArtifacts artifacts: 'performance-suggestions.txt', allowEmptyArchive: true
    }
}

def generatePerformanceReport() {
    echo "生成效能報告..."
    
    script {
        // 收集所有效能資料
        def allPerformanceData = []
        
        // 讀取本次建置的效能資料
        def currentDataFile = "performance-data-${env.BUILD_NUMBER}.json"
        if (fileExists(currentDataFile)) {
            allPerformanceData = readJSON file: currentDataFile
        }
        
        // 生成 HTML 效能報告
        def reportHtml = generatePerformanceReportHtml(allPerformanceData)
        writeFile file: 'performance-report.html', text: reportHtml
        
        publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: '.',
            reportFiles: 'performance-report.html',
            reportName: 'Performance Report'
        ])
        
        // 保存效能資料
        archiveArtifacts artifacts: 'performance-data-*.json', allowEmptyArchive: true
    }
}

def generatePerformanceReportHtml(performanceData) {
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>效能分析報告</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .metric-card { 
                display: inline-block; 
                margin: 10px; 
                padding: 15px; 
                border: 1px solid #ddd; 
                border-radius: 5px; 
                width: 200px; 
                text-align: center; 
            }
            .metric-value { font-size: 1.5em; font-weight: bold; }
            .metric-label { color: #666; }
            .chart-container { width: 800px; height: 400px; margin: 20px auto; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Pipeline 效能分析報告</h1>
        
        <div class="metrics">
            <div class="metric-card">
                <div class="metric-value">${env.CPU_BENCHMARK ?: 'N/A'}</div>
                <div class="metric-label">CPU 基準 (ms)</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-value">${env.IO_BENCHMARK ?: 'N/A'}</div>
                <div class="metric-label">I/O 基準 (ms)</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-value">${env.MEMORY_USAGE_PERCENT ?: 'N/A'}%</div>
                <div class="metric-label">記憶體使用率</div>
            </div>
        </div>
        
        <h2>任務執行時間</h2>
        <table>
            <tr>
                <th>任務名稱</th>
                <th>執行時間 (ms)</th>
                <th>執行節點</th>
                <th>時間戳記</th>
            </tr>
            ${performanceData.collect { data ->
                "<tr><td>${data.taskName}</td><td>${data.duration}</td><td>${data.nodeName}</td><td>${data.timestamp}</td></tr>"
            }.join('\n')}
        </table>
        
        <div class="chart-container">
            <canvas id="performanceChart"></canvas>
        </div>
        
        <script>
            const ctx = document.getElementById('performanceChart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: [${performanceData.collect { "'${it.taskName}'" }.join(', ')}],
                    datasets: [{
                        label: '執行時間 (ms)',
                        data: [${performanceData.collect { it.duration }.join(', ')}],
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        </script>
    </body>
    </html>
    """
}

def analyzePerformanceTrends() {
    echo "分析效能趨勢..."
    
    // 這裡可以實作跨建置的效能趨勢分析
    // 比較與歷史建置的效能差異
    // 識別效能回歸問題
    // 生成趨勢報告
}
```

### 💡 實務案例

#### 案例：大型專案的 Pipeline 故障排除

**情境**：企業級專案遇到複雜的建置失敗問題，需要系統性診斷

**解決方案：**

```groovy
// 企業級故障排除 Pipeline
pipeline {
    agent none
    
    parameters {
        choice(
            name: 'DIAGNOSTIC_LEVEL',
            choices: ['basic', 'detailed', 'comprehensive'],
            description: '診斷級別'
        )
        booleanParam(
            name: 'ENABLE_PROFILING',
            defaultValue: false,
            description: '啟用效能分析'
        )
        booleanParam(
            name: 'COLLECT_SYSTEM_LOGS',
            defaultValue: true,
            description: '收集系統日誌'
        )
    }
    
    stages {
        stage('故障排除初始化') {
            agent any
            steps {
                script {
                    initializeTroubleshooting()
                }
            }
        }
        
        stage('多層次診斷') {
            parallel {
                stage('環境診斷') {
                    agent any
                    steps {
                        script {
                            comprehensiveEnvironmentDiagnostics()
                        }
                    }
                }
                
                stage('效能診斷') {
                    agent any
                    when {
                        params.ENABLE_PROFILING
                    }
                    steps {
                        script {
                            performanceProfileDiagnostics()
                        }
                    }
                }
                
                stage('網路診斷') {
                    agent any
                    steps {
                        script {
                            networkDiagnostics()
                        }
                    }
                }
                
                stage('安全診斷') {
                    agent any
                    steps {
                        script {
                            securityDiagnostics()
                        }
                    }
                }
            }
        }
        
        stage('問題分析') {
            agent any
            steps {
                script {
                    analyzeCollectedDiagnostics()
                }
            }
        }
        
        stage('解決方案推薦') {
            agent any
            steps {
                script {
                    recommendSolutions()
                }
            }
        }
    }
    
    post {
        always {
            node('master') {
                script {
                    generateTroubleshootingReport()
                }
            }
        }
    }
}
```

### ⚠️ 注意事項

1. **日誌管理**：
   - 設定合適的日誌級別
   - 定期清理舊日誌
   - 保護敏感資訊

2. **效能影響**：
   - 避免過度診斷影響效能
   - 合理使用監控工具
   - 平衡詳細度與速度

3. **安全考量**：
   - 不要在日誌中暴露敏感資訊
   - 限制診斷工具的存取權限
   - 保護診斷報告

4. **可維護性**：
   - 建立標準化的故障排除流程
   - 文件化常見問題解決方案
   - 培訓團隊成員

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| Pipeline 除錯 | Script Console、Groovy Sandbox |
| 故障診斷 | 日誌分析、環境檢查 |
| 效能監控 | 資源診斷、瓶頸識別 |
| 問題解決 | 系統性故障排除流程 |

### 📝 練習作業

1. **基礎練習**：學習使用 Jenkins Script Console 進行基本除錯
2. **進階練習**：建立完整的 Pipeline 效能監控機制
3. **實務練習**：設計企業級的故障排除和診斷流程

---

## 第14章 部署策略與環境管理

### 🎯 學習目標

- 掌握多環境部署的設計模式
- 學會實施零停機部署策略
- 建立環境隔離與配置管理
- 實現自動化的部署流程與回滾機制

### 📚 核心概念

#### 14.1 多環境部署架構

企業級的 CI/CD 需要支援多個環境的自動化部署，每個環境都有其特定的用途和配置需求。

```mermaid
graph TB
    A[Source Control] --> B[CI Pipeline]
    B --> C{Build Success?}
    C -->|Yes| D[Artifact Repository]
    C -->|No| E[Build Failed]
    
    D --> F[Development Environment]
    F --> G{Dev Tests Pass?}
    G -->|Yes| H[Testing Environment]
    G -->|No| I[Dev Failed]
    
    H --> J{Integration Tests Pass?}
    J -->|Yes| K[Staging Environment]
    J -->|No| L[Test Failed]
    
    K --> M{UAT Pass?}
    M -->|Yes| N[Production Environment]
    M -->|No| O[UAT Failed]
    
    subgraph "部署策略"
        P[Blue-Green Deployment]
        Q[Canary Deployment]
        R[Rolling Deployment]
        S[A/B Testing]
    end
    
    N --> P
    N --> Q
    N --> R
    N --> S
    
    subgraph "監控與回滾"
        T[Health Checks]
        U[Metrics Collection]
        V[Automated Rollback]
        W[Manual Rollback]
    end
    
    P --> T
    Q --> U
    R --> V
    S --> W
    
    subgraph "環境配置"
        X[Config Management]
        Y[Secret Management]
        Z[Environment Variables]
        AA[Database Migrations]
    end
    
    F --> X
    H --> Y
    K --> Z
    N --> AA
```

#### 14.2 環境隔離與配置管理

**多環境 Pipeline 配置：**

```groovy
// 多環境部署 Pipeline
pipeline {
    agent any
    
    parameters {
        choice(
            name: 'TARGET_ENVIRONMENT',
            choices: ['dev', 'test', 'staging', 'production'],
            description: '目標部署環境'
        )
        choice(
            name: 'DEPLOYMENT_STRATEGY',
            choices: ['blue-green', 'canary', 'rolling', 'direct'],
            description: '部署策略'
        )
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: '跳過測試（僅限非生產環境）'
        )
        booleanParam(
            name: 'ENABLE_ROLLBACK',
            defaultValue: true,
            description: '啟用自動回滾'
        )
    }
    
    environment {
        // 動態設定環境變數
        ENVIRONMENT = "${params.TARGET_ENVIRONMENT}"
        DEPLOYMENT_STRATEGY = "${params.DEPLOYMENT_STRATEGY}"
        
        // 版本資訊
        BUILD_VERSION = "${env.BUILD_NUMBER}-${env.GIT_COMMIT?.take(7)}"
        ARTIFACT_NAME = "myapp-${BUILD_VERSION}.jar"
    }
    
    stages {
        stage('環境驗證') {
            steps {
                script {
                    validateEnvironmentConfig()
                    validateDeploymentPermissions()
                }
            }
        }
        
        stage('構建與測試') {
            when {
                not { params.SKIP_TESTS }
            }
            parallel {
                stage('單元測試') {
                    steps {
                        script {
                            runUnitTests()
                        }
                    }
                }
                
                stage('整合測試') {
                    when {
                        not { params.TARGET_ENVIRONMENT == 'dev' }
                    }
                    steps {
                        script {
                            runIntegrationTests()
                        }
                    }
                }
                
                stage('安全掃描') {
                    when {
                        anyOf {
                            equals expected: 'staging', actual: params.TARGET_ENVIRONMENT
                            equals expected: 'production', actual: params.TARGET_ENVIRONMENT
                        }
                    }
                    steps {
                        script {
                            runSecurityScans()
                        }
                    }
                }
            }
        }
        
        stage('環境準備') {
            steps {
                script {
                    prepareTargetEnvironment()
                    setupEnvironmentConfiguration()
                }
            }
        }
        
        stage('部署執行') {
            steps {
                script {
                    executeDeploymentStrategy()
                }
            }
        }
        
        stage('部署驗證') {
            steps {
                script {
                    verifyDeployment()
                    runHealthChecks()
                }
            }
        }
        
        stage('煙霧測試') {
            steps {
                script {
                    runSmokeTests()
                }
            }
        }
    }
    
    post {
        success {
            script {
                notifyDeploymentSuccess()
                updateDeploymentRegistry()
            }
        }
        
        failure {
            script {
                if (params.ENABLE_ROLLBACK && params.TARGET_ENVIRONMENT in ['staging', 'production']) {
                    executeAutomaticRollback()
                }
                notifyDeploymentFailure()
            }
        }
        
        always {
            script {
                collectDeploymentMetrics()
                cleanupTemporaryResources()
            }
        }
    }
}

// === 環境管理函式 ===

def validateEnvironmentConfig() {
    echo "驗證環境配置: ${env.ENVIRONMENT}"
    
    // 載入環境特定配置
    def envConfig = loadEnvironmentConfig(env.ENVIRONMENT)
    
    // 驗證必要配置項目
    def requiredConfigs = [
        'database_url', 'api_endpoint', 'log_level',
        'max_heap_size', 'instance_count'
    ]
    
    requiredConfigs.each { config ->
        if (!envConfig.containsKey(config)) {
            error("缺少必要配置: ${config}")
        }
    }
    
    echo "✅ 環境配置驗證通過"
    
    // 設定環境變數
    envConfig.each { key, value ->
        env["ENV_${key.toUpperCase()}"] = value.toString()
    }
}

def loadEnvironmentConfig(environment) {
    def configFile = "config/${environment}/application.properties"
    
    if (!fileExists(configFile)) {
        error("環境配置檔案不存在: ${configFile}")
    }
    
    def config = [:]
    def configContent = readFile(configFile)
    
    configContent.split('\n').each { line ->
        if (line.trim() && !line.startsWith('#')) {
            def parts = line.split('=', 2)
            if (parts.size() == 2) {
                config[parts[0].trim()] = parts[1].trim()
            }
        }
    }
    
    return config
}

def validateDeploymentPermissions() {
    echo "驗證部署權限..."
    
    // 檢查環境特定權限
    def requiredPermissions = getRequiredPermissions(env.ENVIRONMENT)
    
    requiredPermissions.each { permission ->
        if (!hasPermission(permission)) {
            error("缺少必要權限: ${permission}")
        }
    }
    
    echo "✅ 部署權限驗證通過"
}

def getRequiredPermissions(environment) {
    def permissions = [
        'dev': ['deploy:dev', 'read:config'],
        'test': ['deploy:test', 'read:config', 'read:secrets'],
        'staging': ['deploy:staging', 'read:config', 'read:secrets', 'write:monitoring'],
        'production': ['deploy:production', 'read:config', 'read:secrets', 'write:monitoring', 'admin:rollback']
    ]
    
    return permissions[environment] ?: []
}

def hasPermission(permission) {
    // 實際實作中會整合企業的權限管理系統
    // 這裡簡化為檢查環境變數或 Jenkins 權限
    return true  // 簡化實作
}

def prepareTargetEnvironment() {
    echo "準備目標環境: ${env.ENVIRONMENT}"
    
    // 檢查環境健康狀態
    checkEnvironmentHealth()
    
    // 準備部署目錄
    sh """
        # 建立部署目錄結構
        mkdir -p deployment/${env.ENVIRONMENT}/{current,releases,shared}
        
        # 設定權限
        chmod 755 deployment/${env.ENVIRONMENT}
        
        # 建立符號連結
        ln -sf deployment/${env.ENVIRONMENT}/current /opt/myapp-${env.ENVIRONMENT} || true
    """
    
    // 準備資料庫遷移
    if (needsDatabaseMigration()) {
        prepareDatabaseMigration()
    }
    
    echo "✅ 環境準備完成"
}

def checkEnvironmentHealth() {
    echo "檢查環境健康狀態..."
    
    // 檢查必要服務
    def services = ['database', 'cache', 'message_queue']
    
    services.each { service ->
        def healthCheck = getServiceHealthCheckCommand(service)
        try {
            sh healthCheck
            echo "✅ ${service} 服務正常"
        } catch (Exception e) {
            error("❌ ${service} 服務不可用: ${e.getMessage()}")
        }
    }
}

def getServiceHealthCheckCommand(service) {
    def commands = [
        'database': "curl -f ${env.ENV_DATABASE_URL}/health || exit 1",
        'cache': "redis-cli -h ${env.ENV_CACHE_HOST} ping",
        'message_queue': "curl -f ${env.ENV_MQ_MANAGEMENT_URL}/api/health"
    ]
    
    return commands[service] ?: "echo '未知服務: ${service}'"
}

def setupEnvironmentConfiguration() {
    echo "設定環境配置..."
    
    // 生成環境特定的配置檔案
    generateApplicationConfig()
    
    // 設定環境變數
    setupEnvironmentVariables()
    
    // 配置日誌設定
    configureLogging()
    
    // 設定監控配置
    setupMonitoring()
}

def generateApplicationConfig() {
    def configTemplate = """
server:
  port: ${env.ENV_SERVER_PORT ?: 8080}
  
spring:
  profiles:
    active: ${env.ENVIRONMENT}
  datasource:
    url: ${env.ENV_DATABASE_URL}
    username: ${env.ENV_DB_USERNAME}
    password: ${env.ENV_DB_PASSWORD}
    
logging:
  level:
    root: ${env.ENV_LOG_LEVEL ?: 'INFO'}
    com.tutorial: DEBUG
  file:
    name: /var/log/myapp-${env.ENVIRONMENT}.log
    
management:
  endpoints:
    web:
      exposure:
        include: health,metrics,info
  endpoint:
    health:
      show-details: always
"""
    
    writeFile file: "application-${env.ENVIRONMENT}.yml", text: configTemplate
    
    echo "✅ 應用程式配置已生成"
}

def setupEnvironmentVariables() {
    // 設定 JVM 參數
    env.JAVA_OPTS = "-Xmx${env.ENV_MAX_HEAP_SIZE ?: '512m'} -Xms${env.ENV_MIN_HEAP_SIZE ?: '256m'}"
    env.SPRING_PROFILES_ACTIVE = env.ENVIRONMENT
    
    // 設定應用程式參數
    env.APP_CONFIG_FILE = "application-${env.ENVIRONMENT}.yml"
    
    echo "✅ 環境變數設定完成"
}

def configureLogging() {
    def logConfigTemplate = """
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>/var/log/myapp-${env.ENVIRONMENT}.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>/var/log/myapp-${env.ENVIRONMENT}.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="${env.ENV_LOG_LEVEL ?: 'INFO'}">
        <appender-ref ref="FILE" />
    </root>
</configuration>
"""
    
    writeFile file: "logback-${env.ENVIRONMENT}.xml", text: logConfigTemplate
    
    echo "✅ 日誌配置完成"
}

def setupMonitoring() {
    if (env.ENVIRONMENT in ['staging', 'production']) {
        // 設定 Prometheus 監控
        setupPrometheusMonitoring()
        
        // 設定健康檢查
        setupHealthChecks()
        
        // 設定告警規則
        setupAlertingRules()
    }
}

def executeDeploymentStrategy() {
    echo "執行部署策略: ${env.DEPLOYMENT_STRATEGY}"
    
    switch (env.DEPLOYMENT_STRATEGY) {
        case 'blue-green':
            executeBlueGreenDeployment()
            break
        case 'canary':
            executeCanaryDeployment()
            break
        case 'rolling':
            executeRollingDeployment()
            break
        case 'direct':
            executeDirectDeployment()
            break
        default:
            error("不支援的部署策略: ${env.DEPLOYMENT_STRATEGY}")
    }
}
```

#### 14.3 Blue-Green 部署策略

**Blue-Green 部署實作：**

```groovy
def executeBlueGreenDeployment() {
    echo "執行 Blue-Green 部署..."
    
    try {
        // 確定當前活躍環境
        def currentEnvironment = getCurrentActiveEnvironment()
        def targetEnvironment = currentEnvironment == 'blue' ? 'green' : 'blue'
        
        echo "當前活躍環境: ${currentEnvironment}"
        echo "目標部署環境: ${targetEnvironment}"
        
        // 部署到目標環境
        deployToEnvironment(targetEnvironment)
        
        // 驗證目標環境
        validateTargetEnvironment(targetEnvironment)
        
        // 執行煙霧測試
        runSmokeTestsOnEnvironment(targetEnvironment)
        
        // 切換流量
        switchTrafficToEnvironment(targetEnvironment)
        
        // 驗證切換後的狀態
        validateTrafficSwitch(targetEnvironment)
        
        // 更新環境標記
        updateActiveEnvironmentMarker(targetEnvironment)
        
        echo "✅ Blue-Green 部署成功完成"
        
    } catch (Exception e) {
        echo "❌ Blue-Green 部署失敗: ${e.getMessage()}"
        
        // 如果已經開始切換流量，嘗試回滾
        if (env.TRAFFIC_SWITCHED == 'true') {
            rollbackTrafficSwitch()
        }
        
        throw e
    }
}

def getCurrentActiveEnvironment() {
    // 檢查負載均衡器配置或環境標記檔案
    try {
        def activeEnv = sh(
            script: "cat /opt/myapp-${env.ENVIRONMENT}/active_environment.txt 2>/dev/null || echo 'blue'",
            returnStdout: true
        ).trim()
        
        return activeEnv ?: 'blue'
    } catch (Exception e) {
        echo "無法確定當前活躍環境，預設使用 blue"
        return 'blue'
    }
}

def deployToEnvironment(targetEnvironment) {
    echo "部署到 ${targetEnvironment} 環境..."
    
    // 停止目標環境的應用程式
    stopApplicationInEnvironment(targetEnvironment)
    
    // 備份當前版本
    backupCurrentVersion(targetEnvironment)
    
    // 部署新版本
    sh """
        # 建立新的發布目錄
        RELEASE_DIR="deployment/${env.ENVIRONMENT}/releases/${env.BUILD_VERSION}"
        mkdir -p \$RELEASE_DIR
        
        # 複製應用程式檔案
        cp ${env.ARTIFACT_NAME} \$RELEASE_DIR/
        cp application-${env.ENVIRONMENT}.yml \$RELEASE_DIR/
        cp logback-${env.ENVIRONMENT}.xml \$RELEASE_DIR/
        
        # 更新 ${targetEnvironment} 環境的符號連結
        ln -sfn \$RELEASE_DIR deployment/${env.ENVIRONMENT}/${targetEnvironment}
        
        # 設定權限
        chmod +x \$RELEASE_DIR/${env.ARTIFACT_NAME}
    """
    
    // 啟動應用程式
    startApplicationInEnvironment(targetEnvironment)
    
    echo "✅ ${targetEnvironment} 環境部署完成"
}

def stopApplicationInEnvironment(environment) {
    echo "停止 ${environment} 環境的應用程式..."
    
    sh """
        # 停止應用程式程序
        PID_FILE="/var/run/myapp-${env.ENVIRONMENT}-${environment}.pid"
        
        if [ -f \$PID_FILE ]; then
            PID=\$(cat \$PID_FILE)
            if kill -0 \$PID 2>/dev/null; then
                echo "停止程序: \$PID"
                kill \$PID
                
                # 等待程序停止
                for i in {1..30}; do
                    if ! kill -0 \$PID 2>/dev/null; then
                        break
                    fi
                    sleep 1
                done
                
                # 強制終止（如果需要）
                if kill -0 \$PID 2>/dev/null; then
                    echo "強制終止程序: \$PID"
                    kill -9 \$PID
                fi
            fi
            rm -f \$PID_FILE
        fi
    """
}

def backupCurrentVersion(environment) {
    echo "備份 ${environment} 環境的當前版本..."
    
    sh """
        BACKUP_DIR="deployment/${env.ENVIRONMENT}/backups/\$(date +%Y%m%d_%H%M%S)"
        CURRENT_DIR="deployment/${env.ENVIRONMENT}/${environment}"
        
        if [ -d "\$CURRENT_DIR" ]; then
            mkdir -p \$BACKUP_DIR
            cp -r \$CURRENT_DIR/* \$BACKUP_DIR/ 2>/dev/null || true
            echo "備份完成: \$BACKUP_DIR"
        fi
    """
}

def startApplicationInEnvironment(environment) {
    echo "啟動 ${environment} 環境的應用程式..."
    
    def port = environment == 'blue' ? 8080 : 8081
    
    sh """
        cd deployment/${env.ENVIRONMENT}/${environment}
        
        # 設定 JVM 參數
        export JAVA_OPTS="${env.JAVA_OPTS}"
        export SERVER_PORT=${port}
        
        # 啟動應用程式
        nohup java \$JAVA_OPTS -jar ${env.ARTIFACT_NAME} \\
            --spring.config.location=application-${env.ENVIRONMENT}.yml \\
            --logging.config=logback-${env.ENVIRONMENT}.xml \\
            --server.port=\$SERVER_PORT > application.log 2>&1 &
        
        # 記錄程序 ID
        echo \$! > /var/run/myapp-${env.ENVIRONMENT}-${environment}.pid
        
        echo "應用程式已啟動，PID: \$!"
    """
    
    // 等待應用程式啟動
    waitForApplicationStartup(environment, port)
}

def waitForApplicationStartup(environment, port) {
    echo "等待 ${environment} 環境應用程式啟動..."
    
    def maxAttempts = 60
    def attempt = 0
    
    while (attempt < maxAttempts) {
        try {
            sh "curl -f http://localhost:${port}/actuator/health"
            echo "✅ ${environment} 環境應用程式已啟動"
            return
        } catch (Exception e) {
            attempt++
            if (attempt < maxAttempts) {
                sleep(5)
            }
        }
    }
    
    error("❌ ${environment} 環境應用程式啟動超時")
}

def validateTargetEnvironment(environment) {
    echo "驗證 ${environment} 環境..."
    
    def port = environment == 'blue' ? 8080 : 8081
    
    // 健康檢查
    sh "curl -f http://localhost:${port}/actuator/health"
    
    // 檢查關鍵功能
    sh """
        # 檢查應用程式資訊
        curl -f http://localhost:${port}/actuator/info
        
        # 檢查指標
        curl -f http://localhost:${port}/actuator/metrics
        
        # 檢查應用程式版本
        VERSION=\$(curl -s http://localhost:${port}/actuator/info | grep -o '"version":"[^"]*"' | cut -d'"' -f4)
        if [ "\$VERSION" != "${env.BUILD_VERSION}" ]; then
            echo "版本不匹配: 期望 ${env.BUILD_VERSION}，實際 \$VERSION"
            exit 1
        fi
    """
    
    echo "✅ ${environment} 環境驗證通過"
}

def runSmokeTestsOnEnvironment(environment) {
    echo "在 ${environment} 環境執行煙霧測試..."
    
    def port = environment == 'blue' ? 8080 : 8081
    def baseUrl = "http://localhost:${port}"
    
    // 執行關鍵 API 測試
    sh """
        # 測試健康端點
        curl -f ${baseUrl}/actuator/health
        
        # 測試主要 API 端點
        curl -f ${baseUrl}/api/status
        
        # 測試資料庫連線
        curl -f ${baseUrl}/api/health/database
        
        # 測試快取連線
        curl -f ${baseUrl}/api/health/cache
    """
    
    // 執行業務邏輯測試
    runBusinessLogicTests(baseUrl)
    
    echo "✅ ${environment} 環境煙霧測試通過"
}

def runBusinessLogicTests(baseUrl) {
    // 實作業務邏輯相關的煙霧測試
    sh """
        # 測試用戶認證
        TOKEN=\$(curl -s -X POST ${baseUrl}/api/auth/login \\
            -H "Content-Type: application/json" \\
            -d '{"username":"test","password":"test"}' | \\
            grep -o '"token":"[^"]*"' | cut -d'"' -f4)
        
        if [ -z "\$TOKEN" ]; then
            echo "認證測試失敗"
            exit 1
        fi
        
        # 測試受保護的端點
        curl -f -H "Authorization: Bearer \$TOKEN" ${baseUrl}/api/user/profile
        
        echo "業務邏輯測試通過"
    """
}

def switchTrafficToEnvironment(environment) {
    echo "切換流量到 ${environment} 環境..."
    
    // 更新負載均衡器配置
    updateLoadBalancerConfig(environment)
    
    // 等待配置生效
    sleep(10)
    
    // 驗證流量切換
    verifyTrafficRouting(environment)
    
    // 標記流量已切換
    env.TRAFFIC_SWITCHED = 'true'
    
    echo "✅ 流量已切換到 ${environment} 環境"
}

def updateLoadBalancerConfig(environment) {
    def port = environment == 'blue' ? 8080 : 8081
    
    // 更新 Nginx 配置（範例）
    sh """
        # 生成新的 upstream 配置
        cat > /etc/nginx/conf.d/myapp-${env.ENVIRONMENT}.conf << EOF
upstream myapp_${env.ENVIRONMENT} {
    server localhost:${port};
}

server {
    listen 80;
    server_name myapp-${env.ENVIRONMENT}.example.com;
    
    location / {
        proxy_pass http://myapp_${env.ENVIRONMENT};
        proxy_set_header Host \\\$host;
        proxy_set_header X-Real-IP \\\$remote_addr;
    }
    
    location /health {
        proxy_pass http://myapp_${env.ENVIRONMENT}/actuator/health;
    }
}
EOF
        
        # 測試配置
        nginx -t
        
        # 重新載入配置
        nginx -s reload
    """
}

def verifyTrafficRouting(environment) {
    echo "驗證流量路由到 ${environment} 環境..."
    
    def expectedPort = environment == 'blue' ? 8080 : 8081
    
    sh """
        # 多次請求驗證路由
        for i in {1..10}; do
            # 透過負載均衡器發送請求
            RESPONSE=\$(curl -s http://myapp-${env.ENVIRONMENT}.example.com/api/info)
            
            # 檢查回應是否來自正確的環境
            PORT=\$(echo "\$RESPONSE" | grep -o '"port":[0-9]*' | cut -d':' -f2)
            
            if [ "\$PORT" != "${expectedPort}" ]; then
                echo "流量路由錯誤: 期望端口 ${expectedPort}，實際端口 \$PORT"
                exit 1
            fi
            
            sleep 1
        done
        
        echo "流量路由驗證成功"
    """
}

def validateTrafficSwitch(environment) {
    echo "驗證流量切換後的狀態..."
    
    // 監控關鍵指標
    monitorKeyMetrics(environment)
    
    // 檢查錯誤率
    checkErrorRate()
    
    // 檢查回應時間
    checkResponseTime()
    
    echo "✅ 流量切換驗證完成"
}

def monitorKeyMetrics(environment) {
    // 監控 CPU、記憶體、磁碟 I/O 等關鍵指標
    sh """
        echo "監控 ${environment} 環境的關鍵指標..."
        
        # CPU 使用率
        CPU_USAGE=\$(top -bn1 | grep "Cpu(s)" | awk '{print \$2}' | awk -F'%' '{print \$1}')
        echo "CPU 使用率: \${CPU_USAGE}%"
        
        # 記憶體使用率
        MEMORY_USAGE=\$(free | grep Mem | awk '{printf "%.1f", \$3/\$2 * 100.0}')
        echo "記憶體使用率: \${MEMORY_USAGE}%"
        
        # 應用程式 JVM 指標
        curl -s http://localhost:${environment == 'blue' ? 8080 : 8081}/actuator/metrics/jvm.memory.used
    """
}

def checkErrorRate() {
    // 檢查應用程式錯誤率
    sh """
        # 檢查最近的錯誤日誌
        ERROR_COUNT=\$(tail -1000 /var/log/myapp-${env.ENVIRONMENT}.log | grep -i error | wc -l)
        
        if [ \$ERROR_COUNT -gt 10 ]; then
            echo "警告: 錯誤數量過高 (\$ERROR_COUNT)"
            # 可以選擇觸發回滾
        else
            echo "錯誤率正常 (\$ERROR_COUNT 個錯誤)"
        fi
    """
}

def checkResponseTime() {
    // 檢查 API 回應時間
    sh """
        # 測試主要 API 的回應時間
        RESPONSE_TIME=\$(curl -o /dev/null -s -w '%{time_total}' http://myapp-${env.ENVIRONMENT}.example.com/api/status)
        
        # 轉換為毫秒
        RESPONSE_TIME_MS=\$(echo "\$RESPONSE_TIME * 1000" | bc)
        
        echo "API 回應時間: \${RESPONSE_TIME_MS}ms"
        
        # 如果回應時間超過閾值，發出警告
        if [ \$(echo "\$RESPONSE_TIME_MS > 1000" | bc) -eq 1 ]; then
            echo "警告: API 回應時間過長"
        fi
    """
}

def updateActiveEnvironmentMarker(environment) {
    echo "更新活躍環境標記為: ${environment}"
    
    sh """
        echo "${environment}" > /opt/myapp-${env.ENVIRONMENT}/active_environment.txt
        echo "更新時間: \$(date)" >> /opt/myapp-${env.ENVIRONMENT}/deployment_history.log
        echo "版本: ${env.BUILD_VERSION}" >> /opt/myapp-${env.ENVIRONMENT}/deployment_history.log
    """
}

def rollbackTrafficSwitch() {
    echo "執行流量切換回滾..."
    
    def currentActive = getCurrentActiveEnvironment()
    def previousActive = currentActive == 'blue' ? 'green' : 'blue'
    
    echo "回滾到 ${previousActive} 環境"
    
    // 切換回原來的環境
    updateLoadBalancerConfig(previousActive)
    
    // 驗證回滾
    verifyTrafficRouting(previousActive)
    
    echo "✅ 流量回滾完成"
}
```

#### 14.4 Canary 部署策略

**Canary 部署實作：**

```groovy
def executeCanaryDeployment() {
    echo "執行 Canary 部署..."
    
    try {
        // 部署 Canary 版本
        deployCanaryVersion()
        
        // 配置流量分割
        configureTrafficSplitting(5) // 5% 流量到 Canary
        
        // 監控 Canary 版本
        monitorCanaryVersion()
        
        // 逐步增加流量
        graduallIncreaseTraffic()
        
        // 完全切換到新版本
        completeCanaryDeployment()
        
        echo "✅ Canary 部署成功完成"
        
    } catch (Exception e) {
        echo "❌ Canary 部署失敗: ${e.getMessage()}"
        rollbackCanaryDeployment()
        throw e
    }
}

def deployCanaryVersion() {
    echo "部署 Canary 版本..."
    
    // 部署到專用的 Canary 節點
    sh """
        # 建立 Canary 部署目錄
        CANARY_DIR="deployment/${env.ENVIRONMENT}/canary"
        mkdir -p \$CANARY_DIR
        
        # 部署新版本到 Canary 環境
        cp ${env.ARTIFACT_NAME} \$CANARY_DIR/
        cp application-${env.ENVIRONMENT}.yml \$CANARY_DIR/
        
        # 啟動 Canary 實例（使用不同端口）
        cd \$CANARY_DIR
        nohup java ${env.JAVA_OPTS} -jar ${env.ARTIFACT_NAME} \\
            --spring.config.location=application-${env.ENVIRONMENT}.yml \\
            --server.port=8082 > canary.log 2>&1 &
        
        echo \$! > /var/run/myapp-${env.ENVIRONMENT}-canary.pid
    """
    
    // 等待 Canary 實例啟動
    waitForApplicationStartup('canary', 8082)
}

def configureTrafficSplitting(percentage) {
    echo "配置流量分割: ${percentage}% 到 Canary"
    
    // 更新負載均衡器配置以分割流量
    sh """
        cat > /etc/nginx/conf.d/myapp-${env.ENVIRONMENT}-canary.conf << EOF
upstream myapp_${env.ENVIRONMENT}_production {
    server localhost:8080 weight=${100 - percentage};
}

upstream myapp_${env.ENVIRONMENT}_canary {
    server localhost:8082 weight=${percentage};
}

upstream myapp_${env.ENVIRONMENT}_combined {
    server localhost:8080 weight=${100 - percentage};
    server localhost:8082 weight=${percentage};
}

server {
    listen 80;
    server_name myapp-${env.ENVIRONMENT}.example.com;
    
    location / {
        proxy_pass http://myapp_${env.ENVIRONMENT}_combined;
        proxy_set_header Host \\\$host;
        proxy_set_header X-Real-IP \\\$remote_addr;
        
        # 添加 Canary 標頭
        add_header X-Canary-Deployment "active" always;
    }
}
EOF
        
        nginx -t && nginx -s reload
    """
}

def monitorCanaryVersion() {
    echo "監控 Canary 版本..."
    
    def monitoringDuration = 300 // 5分鐘
    def startTime = System.currentTimeMillis()
    
    while ((System.currentTimeMillis() - startTime) < (monitoringDuration * 1000)) {
        // 檢查 Canary 健康狀態
        checkCanaryHealth()
        
        // 檢查錯誤率
        def errorRate = getCanaryErrorRate()
        if (errorRate > 5.0) { // 錯誤率超過 5%
            throw new Exception("Canary 錯誤率過高: ${errorRate}%")
        }
        
        // 檢查回應時間
        def responseTime = getCanaryResponseTime()
        if (responseTime > 2000) { // 回應時間超過 2 秒
            throw new Exception("Canary 回應時間過長: ${responseTime}ms")
        }
        
        sleep(30) // 每 30 秒檢查一次
    }
    
    echo "✅ Canary 監控通過"
}

def graduallIncreaseTraffic() {
    def trafficSteps = [5, 10, 25, 50, 75, 100]
    
    trafficSteps.each { percentage ->
        echo "增加 Canary 流量到 ${percentage}%"
        
        configureTrafficSplitting(percentage)
        
        // 監控一段時間
        monitorCanaryAtPercentage(percentage)
        
        if (percentage < 100) {
            sleep(300) // 等待 5 分鐘再進行下一步
        }
    }
}

def monitorCanaryAtPercentage(percentage) {
    echo "監控 ${percentage}% 流量下的 Canary 表現..."
    
    // 監控關鍵指標
    def metrics = collectCanaryMetrics()
    
    // 檢查業務指標
    validateBusinessMetrics(metrics)
    
    // 記錄監控結果
    recordCanaryMetrics(percentage, metrics)
}

def completeCanaryDeployment() {
    echo "完成 Canary 部署..."
    
    // 停止舊版本
    stopProductionVersion()
    
    // 將 Canary 版本提升為生產版本
    promoteCanaryToProduction()
    
    // 清理 Canary 資源
    cleanupCanaryResources()
}

def rollbackCanaryDeployment() {
    echo "回滾 Canary 部署..."
    
    // 停止 Canary 實例
    sh """
        PID_FILE="/var/run/myapp-${env.ENVIRONMENT}-canary.pid"
        if [ -f \$PID_FILE ]; then
            PID=\$(cat \$PID_FILE)
            kill \$PID 2>/dev/null || true
            rm -f \$PID_FILE
        fi
    """
    
    // 恢復原來的負載均衡器配置
    configureTrafficSplitting(0)
    
    // 清理 Canary 資源
    cleanupCanaryResources()
    
    echo "✅ Canary 回滾完成"
}
```

### 💡 實務案例

#### 案例：微服務架構的漸進式部署

**情境**：大型微服務系統需要協調多個服務的部署，確保服務間的相容性

**解決方案：**

```groovy
// 微服務協調部署 Pipeline
pipeline {
    agent none
    
    parameters {
        string(name: 'SERVICES', defaultValue: 'user-service,order-service,payment-service', description: '要部署的服務列表')
        choice(name: 'DEPLOYMENT_ORDER', choices: ['parallel', 'sequential', 'dependency-based'], description: '部署順序')
    }
    
    stages {
        stage('服務依賴分析') {
            agent any
            steps {
                script {
                    analyzeServiceDependencies()
                    generateDeploymentPlan()
                }
            }
        }
        
        stage('微服務部署') {
            steps {
                script {
                    executeServiceDeployments()
                }
            }
        }
        
        stage('服務整合測試') {
            agent any
            steps {
                script {
                    runCrossServiceTests()
                }
            }
        }
    }
}
```

### ⚠️ 注意事項

1. **資料庫遷移**：
   - 確保向後相容性
   - 使用遷移腳本版本控制
   - 準備回滾計畫

2. **狀態管理**：
   - 考慮會話親和性
   - 處理快取一致性
   - 管理外部服務依賴

3. **監控告警**：
   - 設定關鍵指標閾值
   - 建立自動回滾觸發條件
   - 實作即時通知機制

4. **安全考量**：
   - 保護部署憑證
   - 限制部署權限
   - 記錄部署審計日誌

### 🔍 認證對應知識點

| 認證項目 | 對應章節內容 |
|----------|--------------|
| 部署策略 | Blue-Green、Canary、Rolling |
| 環境管理 | 多環境配置、隔離策略 |
| 自動化部署 | Pipeline 部署流程 |
| 故障處理 | 回滾機制、監控告警 |

### 練習作業 - 第14章

1. **基礎練習**：實作簡單的多環境部署 Pipeline
2. **進階練習**：設計並實作 Blue-Green 部署策略
3. **實務練習**：建立完整的微服務部署協調機制

---

## 第15章 監控、通知與效能優化

### 目標導向

- 建立全面的 CI/CD 監控體系
- 實施智慧化的通知機制
- 掌握效能優化的最佳實務
- 建構可觀測性的完整解決方案

### 核心架構

#### 15.1 監控體系架構設計

現代 CI/CD 需要多層次的監控體系，從基礎設施到應用程式的全方位可觀測性。

```mermaid
graph TB
    A[監控體系] --> B[基礎設施監控]
    A --> C[應用程式監控]
    A --> D[業務指標監控]
    A --> E[安全監控]
    
    B --> F[Jenkins Server]
    B --> G[Agent Nodes]
    B --> H[Database]
    B --> I[Network]
    
    C --> J[Build Metrics]
    C --> K[Deployment Metrics]
    C --> L[Test Results]
    C --> M[Code Quality]
    
    D --> N[Build Success Rate]
    D --> O[Deployment Frequency]
    D --> P[Lead Time]
    D --> Q[MTTR]
    
    E --> R[Security Scans]
    E --> S[Vulnerability Alerts]
    E --> T[Compliance Checks]
    E --> U[Access Logs]
    
    subgraph "監控工具"
        V[Prometheus]
        W[Grafana]
        X[ELK Stack]
        Y[Jaeger]
        Z[SonarQube]
    end
    
    subgraph "通知渠道"
        AA[Email]
        BB[Slack]
        CC[Microsoft Teams]
        DD[Webhook]
        EE[SMS]
    end
    
    subgraph "告警策略"
        FF[閾值告警]
        GG[趨勢預警]
        HH[異常檢測]
        II[智慧降噪]
    end
    
    B --> V
    C --> W
    D --> X
    E --> Y
    
    V --> FF
    W --> GG
    X --> HH
    Y --> II
    
    FF --> AA
    GG --> BB
    HH --> CC
    II --> DD
```

#### 15.2 Jenkins 監控整合

**全方位監控 Pipeline：**

```groovy
// 監控整合 Pipeline
pipeline {
    agent any
    
    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        
        // 啟用監控選項
        parallelsAlwaysFailFast()
    }
    
    environment {
        // 監控配置
        MONITORING_ENABLED = 'true'
        METRICS_ENDPOINT = 'http://prometheus:9090'
        GRAFANA_ENDPOINT = 'http://grafana:3000'
        
        // 通知配置
        SLACK_CHANNEL = '#ci-cd-alerts'
        EMAIL_RECIPIENTS = 'devops@company.com'
        
        // 效能基準線
        BUILD_TIME_THRESHOLD = '300' // 5分鐘
        TEST_COVERAGE_THRESHOLD = '80'
        QUALITY_GATE_THRESHOLD = 'A'
    }
    
    stages {
        stage('監控系統初始化') {
            steps {
                script {
                    initializeMonitoring()
                    setupMetricsCollection()
                    validateMonitoringEndpoints()
                }
            }
        }
        
        stage('建置監控') {
            parallel {
                stage('代碼建置') {
                    steps {
                        script {
                            def buildStartTime = System.currentTimeMillis()
                            
                            try {
                                // 執行建置
                                runBuildWithMonitoring()
                                
                                // 記錄建置指標
                                recordBuildMetrics(buildStartTime, 'SUCCESS')
                                
                            } catch (Exception e) {
                                recordBuildMetrics(buildStartTime, 'FAILED')
                                throw e
                            }
                        }
                    }
                }
                
                stage('依賴監控') {
                    steps {
                        script {
                            monitorDependencies()
                            checkSecurityVulnerabilities()
                        }
                    }
                }
                
                stage('資源監控') {
                    steps {
                        script {
                            monitorResourceUsage()
                            trackSystemPerformance()
                        }
                    }
                }
            }
        }
        
        stage('測試監控') {
            steps {
                script {
                    executeTestsWithMonitoring()
                    analyzeTestResults()
                    generateTestMetrics()
                }
            }
        }
        
        stage('品質監控') {
            steps {
                script {
                    runQualityAnalysisWithMonitoring()
                    evaluateQualityGates()
                    publishQualityMetrics()
                }
            }
        }
        
        stage('部署監控') {
            when {
                branch 'master'
            }
            steps {
                script {
                    deployWithMonitoring()
                    validateDeploymentHealth()
                    monitorPostDeploymentMetrics()
                }
            }
        }
    }
    
    post {
        always {
            script {
                // 收集最終指標
                collectFinalMetrics()
                
                // 生成監控報告
                generateMonitoringReport()
                
                // 更新儀表板
                updateDashboards()
            }
        }
        
        success {
            script {
                sendSuccessNotification()
                updateSuccessMetrics()
            }
        }
        
        failure {
            script {
                sendFailureAlert()
                triggerIncidentResponse()
                updateFailureMetrics()
            }
        }
        
        unstable {
            script {
                sendUnstableWarning()
                analyzeInstabilityTrends()
            }
        }
    }
}

// === 監控初始化函式 ===

def initializeMonitoring() {
    echo "初始化監控系統..."
    
    // 設定監控標籤
    env.BUILD_TIMESTAMP = new Date().format('yyyy-MM-dd HH:mm:ss')
    env.BUILD_ID = "${env.JOB_NAME}-${env.BUILD_NUMBER}"
    env.GIT_BRANCH = env.BRANCH_NAME ?: 'unknown'
    
    // 建立監控上下文
    def monitoringContext = [
        buildId: env.BUILD_ID,
        jobName: env.JOB_NAME,
        buildNumber: env.BUILD_NUMBER,
        gitBranch: env.GIT_BRANCH,
        timestamp: env.BUILD_TIMESTAMP,
        executor: env.NODE_NAME ?: 'master'
    ]
    
    // 儲存監控上下文
    writeJSON file: 'monitoring-context.json', json: monitoringContext
    
    echo "✅ 監控系統初始化完成"
}

def setupMetricsCollection() {
    echo "設定指標收集..."
    
    // 設定 Prometheus 指標
    setupPrometheusMetrics()
    
    // 設定自定義指標
    setupCustomMetrics()
    
    // 設定日誌聚合
    setupLogAggregation()
    
    echo "✅ 指標收集設定完成"
}

def setupPrometheusMetrics() {
    // 設定 Prometheus 監控端點
    sh '''
        # 建立 Prometheus 配置
        cat > prometheus.yml << EOF
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "jenkins_rules.yml"

scrape_configs:
  - job_name: 'jenkins'
    static_configs:
      - targets: ['localhost:8080']
    metrics_path: '/prometheus'
    
  - job_name: 'jenkins-nodes'
    static_configs:
      - targets: ['node1:8080', 'node2:8080']
    metrics_path: '/prometheus'

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093
EOF

        # 建立告警規則
        cat > jenkins_rules.yml << EOF
groups:
  - name: jenkins.rules
    rules:
      - alert: JenkinsBuildDurationHigh
        expr: jenkins_job_duration_milliseconds > 300000
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "Jenkins build duration is high"
          description: "Build {{ \\$labels.job }} took {{ \\$value }}ms"
          
      - alert: JenkinsJobFailureRate
        expr: rate(jenkins_job_failed_total[5m]) > 0.1
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "High job failure rate detected"
          description: "Job failure rate is {{ \\$value }} per second"
EOF
    '''
}

def setupCustomMetrics() {
    // 建立自定義指標收集器
    sh '''
        mkdir -p metrics
        
        # 建置時間指標
        cat > metrics/build_metrics.py << 'EOF'
import json
import time
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

class BuildMetricsCollector:
    def __init__(self):
        self.registry = CollectorRegistry()
        self.build_duration = Gauge('jenkins_build_duration_seconds', 
                                  'Build duration in seconds', 
                                  ['job_name', 'build_number'], 
                                  registry=self.registry)
        self.test_coverage = Gauge('jenkins_test_coverage_percent', 
                                 'Test coverage percentage', 
                                 ['job_name', 'build_number'], 
                                 registry=self.registry)
        self.quality_score = Gauge('jenkins_quality_score', 
                                 'Code quality score', 
                                 ['job_name', 'build_number'], 
                                 registry=self.registry)
    
    def record_build_duration(self, job_name, build_number, duration):
        self.build_duration.labels(job_name=job_name, 
                                 build_number=build_number).set(duration)
    
    def record_test_coverage(self, job_name, build_number, coverage):
        self.test_coverage.labels(job_name=job_name, 
                                build_number=build_number).set(coverage)
    
    def record_quality_score(self, job_name, build_number, score):
        self.quality_score.labels(job_name=job_name, 
                                build_number=build_number).set(score)
    
    def push_metrics(self, gateway_url):
        push_to_gateway(gateway_url, job='jenkins_build', registry=self.registry)
EOF
    '''
}

def setupLogAggregation() {
    // 設定 ELK Stack 日誌聚合
    sh '''
        # 建立 Filebeat 配置
        cat > filebeat.yml << EOF
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/jenkins/*.log
    - /var/log/jenkins/jobs/*/builds/*/log
  fields:
    service: jenkins
    environment: ${ENVIRONMENT}
  fields_under_root: true

output.logstash:
  hosts: ["logstash:5044"]

processors:
  - add_host_metadata:
      when.not.contains.tags: forwarded
  - add_docker_metadata: ~
  - add_kubernetes_metadata: ~
EOF

        # 建立 Logstash 配置
        cat > logstash.conf << EOF
input {
  beats {
    port => 5044
  }
}

filter {
  if [service] == "jenkins" {
    grok {
      match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:message}" }
    }
    
    date {
      match => [ "timestamp", "ISO8601" ]
    }
    
    if [level] == "ERROR" {
      mutate {
        add_tag => [ "error" ]
      }
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "jenkins-logs-%{+YYYY.MM.dd}"
  }
}
EOF
    '''
}

def validateMonitoringEndpoints() {
    echo "驗證監控端點..."
    
    // 檢查 Prometheus
    try {
        sh "curl -f ${env.METRICS_ENDPOINT}/api/v1/query?query=up"
        echo "✅ Prometheus 連線正常"
    } catch (Exception e) {
        echo "⚠️ Prometheus 連線失敗: ${e.getMessage()}"
    }
    
    // 檢查 Grafana
    try {
        sh "curl -f ${env.GRAFANA_ENDPOINT}/api/health"
        echo "✅ Grafana 連線正常"
    } catch (Exception e) {
        echo "⚠️ Grafana 連線失敗: ${e.getMessage()}"
    }
    
    // 檢查 Elasticsearch
    try {
        sh "curl -f http://elasticsearch:9200/_cluster/health"
        echo "✅ Elasticsearch 連線正常"
    } catch (Exception e) {
        echo "⚠️ Elasticsearch 連線失敗: ${e.getMessage()}"
    }
}

// === 建置監控函式 ===

def runBuildWithMonitoring() {
    echo "執行帶監控的建置..."
    
    // 記錄建置開始指標
    recordMetric('build_started', [
        job_name: env.JOB_NAME,
        build_number: env.BUILD_NUMBER,
        timestamp: System.currentTimeMillis()
    ])
    
    // 監控建置步驟
    monitorBuildSteps {
        // 實際建置邏輯
        sh '''
            echo "開始 Maven 建置..."
            mvn clean compile -DskipTests=true
            
            echo "建置完成，檢查產出..."
            ls -la target/classes/
        '''
    }
    
    echo "✅ 建置完成"
}

def monitorBuildSteps(closure) {
    def stepStartTime = System.currentTimeMillis()
    
    try {
        // 執行建置步驟
        closure()
        
        def duration = System.currentTimeMillis() - stepStartTime
        
        // 記錄成功指標
        recordMetric('build_step_duration', [
            step_name: 'compile',
            duration_ms: duration,
            status: 'success'
        ])
        
    } catch (Exception e) {
        def duration = System.currentTimeMillis() - stepStartTime
        
        // 記錄失敗指標
        recordMetric('build_step_duration', [
            step_name: 'compile',
            duration_ms: duration,
            status: 'failed',
            error: e.getMessage()
        ])
        
        throw e
    }
}

def recordBuildMetrics(startTime, status) {
    def duration = System.currentTimeMillis() - startTime
    def durationSeconds = duration / 1000
    
    echo "記錄建置指標: 狀態=${status}, 耗時=${durationSeconds}秒"
    
    // 記錄到 Prometheus
    recordMetric('build_duration', [
        job_name: env.JOB_NAME,
        build_number: env.BUILD_NUMBER,
        status: status,
        duration_seconds: durationSeconds,
        branch: env.GIT_BRANCH
    ])
    
    // 檢查是否超過閾值
    if (durationSeconds > (env.BUILD_TIME_THRESHOLD as Integer)) {
        sendPerformanceAlert("建置時間超過閾值", "建置耗時 ${durationSeconds} 秒，超過閾值 ${env.BUILD_TIME_THRESHOLD} 秒")
    }
    
    // 更新統計資料
    updateBuildStatistics(status, durationSeconds)
}

def monitorDependencies() {
    echo "監控依賴項目..."
    
    // 分析依賴項目
    sh '''
        echo "分析 Maven 依賴..."
        mvn dependency:analyze > dependency-analysis.txt 2>&1
        
        echo "檢查過時的依賴..."
        mvn versions:display-dependency-updates > dependency-updates.txt 2>&1
        
        echo "檢查漏洞..."
        mvn org.owasp:dependency-check-maven:check > security-check.txt 2>&1
    '''
    
    // 解析依賴分析結果
    def analysisResult = readFile('dependency-analysis.txt')
    def unusedDeps = extractUnusedDependencies(analysisResult)
    def outdatedDeps = extractOutdatedDependencies(readFile('dependency-updates.txt'))
    
    // 記錄依賴指標
    recordMetric('dependency_unused_count', [
        job_name: env.JOB_NAME,
        count: unusedDeps.size()
    ])
    
    recordMetric('dependency_outdated_count', [
        job_name: env.JOB_NAME,
        count: outdatedDeps.size()
    ])
    
    // 如果有問題依賴，發送通知
    if (unusedDeps.size() > 0 || outdatedDeps.size() > 0) {
        sendDependencyAlert(unusedDeps, outdatedDeps)
    }
}

def checkSecurityVulnerabilities() {
    echo "檢查安全漏洞..."
    
    try {
        // 使用 OWASP Dependency Check
        sh 'mvn org.owasp:dependency-check-maven:check -DfailBuildOnCVSS=7'
        
        // 解析安全報告
        def securityReport = parseSecurityReport()
        
        // 記錄安全指標
        recordMetric('security_vulnerabilities', [
            job_name: env.JOB_NAME,
            high_severity: securityReport.highSeverity,
            medium_severity: securityReport.mediumSeverity,
            low_severity: securityReport.lowSeverity
        ])
        
        // 如果有高嚴重性漏洞，發送警告
        if (securityReport.highSeverity > 0) {
            sendSecurityAlert(securityReport)
        }
        
    } catch (Exception e) {
        echo "安全檢查失敗: ${e.getMessage()}"
        recordMetric('security_check_failed', [
            job_name: env.JOB_NAME,
            error: e.getMessage()
        ])
    }
}

def monitorResourceUsage() {
    echo "監控資源使用情況..."
    
    // 收集系統資源指標
    sh '''
        # CPU 使用率
        echo "CPU 使用率:" > resource-usage.txt
        top -bn1 | grep "Cpu(s)" >> resource-usage.txt
        
        # 記憶體使用
        echo "記憶體使用:" >> resource-usage.txt
        free -h >> resource-usage.txt
        
        # 磁碟使用
        echo "磁碟使用:" >> resource-usage.txt
        df -h >> resource-usage.txt
        
        # 網路狀態
        echo "網路狀態:" >> resource-usage.txt
        netstat -i >> resource-usage.txt
    '''
    
    // 解析並記錄資源指標
    def resourceData = parseResourceUsage()
    
    recordMetric('system_cpu_usage', [
        node_name: env.NODE_NAME,
        usage_percent: resourceData.cpuUsage
    ])
    
    recordMetric('system_memory_usage', [
        node_name: env.NODE_NAME,
        usage_percent: resourceData.memoryUsage,
        total_gb: resourceData.totalMemory
    ])
    
    recordMetric('system_disk_usage', [
        node_name: env.NODE_NAME,
        usage_percent: resourceData.diskUsage,
        available_gb: resourceData.availableDisk
    ])
    
    // 檢查資源警告閾值
    checkResourceThresholds(resourceData)
}

def trackSystemPerformance() {
    echo "追蹤系統效能..."
    
    // 測量 I/O 效能
    def ioPerformance = measureIOPerformance()
    
    // 測量網路延遲
    def networkLatency = measureNetworkLatency()
    
    // 記錄效能指標
    recordMetric('system_io_performance', [
        node_name: env.NODE_NAME,
        read_mbps: ioPerformance.readMbps,
        write_mbps: ioPerformance.writeMbps
    ])
    
    recordMetric('system_network_latency', [
        node_name: env.NODE_NAME,
        latency_ms: networkLatency
    ])
}

// === 測試監控函式 ===

def executeTestsWithMonitoring() {
    echo "執行帶監控的測試..."
    
    def testStartTime = System.currentTimeMillis()
    
    try {
        // 執行單元測試
        runUnitTestsWithMonitoring()
        
        // 執行整合測試
        runIntegrationTestsWithMonitoring()
        
        // 記錄測試成功指標
        def duration = System.currentTimeMillis() - testStartTime
        recordMetric('test_execution_duration', [
            job_name: env.JOB_NAME,
            duration_seconds: duration / 1000,
            status: 'success'
        ])
        
    } catch (Exception e) {
        def duration = System.currentTimeMillis() - testStartTime
        recordMetric('test_execution_duration', [
            job_name: env.JOB_NAME,
            duration_seconds: duration / 1000,
            status: 'failed',
            error: e.getMessage()
        ])
        throw e
    }
}

def runUnitTestsWithMonitoring() {
    echo "執行單元測試並監控..."
    
    sh '''
        # 執行測試並生成報告
        mvn test -Dmaven.test.failure.ignore=true
        
        # 生成測試覆蓋率報告
        mvn jacoco:report
    '''
    
    // 解析測試結果
    def testResults = parseTestResults('target/surefire-reports')
    def coverageResults = parseCoverageResults('target/site/jacoco')
    
    // 記錄測試指標
    recordTestMetrics(testResults, coverageResults)
    
    // 發布測試報告
    publishTestResults trustExitCode: true, testResultsPattern: 'target/surefire-reports/*.xml'
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'target/site/jacoco',
        reportFiles: 'index.html',
        reportName: 'Coverage Report'
    ])
}

def runIntegrationTestsWithMonitoring() {
    echo "執行整合測試並監控..."
    
    sh '''
        # 啟動測試環境
        docker-compose -f docker-compose.test.yml up -d
        
        # 等待服務就緒
        sleep 30
        
        # 執行整合測試
        mvn failsafe:integration-test failsafe:verify
        
        # 清理測試環境
        docker-compose -f docker-compose.test.yml down
    '''
    
    // 解析整合測試結果
    def integrationResults = parseTestResults('target/failsafe-reports')
    
    // 記錄整合測試指標
    recordMetric('integration_test_results', [
        job_name: env.JOB_NAME,
        total_tests: integrationResults.total,
        passed_tests: integrationResults.passed,
        failed_tests: integrationResults.failed,
        skipped_tests: integrationResults.skipped
    ])
}

def analyzeTestResults() {
    echo "分析測試結果..."
    
    // 分析測試趨勢
    analyzeTestTrends()
    
    // 識別不穩定的測試
    identifyFlakyTests()
    
    // 分析測試覆蓋率趨勢
    analyzeCoverageTrends()
}

def generateTestMetrics() {
    echo "生成測試指標..."
    
    // 生成測試效能報告
    generateTestPerformanceReport()
    
    // 更新測試儀表板
    updateTestDashboard()
    
    // 發送測試總結
    sendTestSummary()
}

// === 品質監控函式 ===

def runQualityAnalysisWithMonitoring() {
    echo "執行代碼品質分析並監控..."
    
    def qualityStartTime = System.currentTimeMillis()
    
    try {
        // SonarQube 分析
        runSonarQubeAnalysis()
        
        // Checkstyle 檢查
        runCheckstyleAnalysis()
        
        // PMD 分析
        runPMDAnalysis()
        
        // SpotBugs 分析
        runSpotBugsAnalysis()
        
        def duration = System.currentTimeMillis() - qualityStartTime
        recordMetric('quality_analysis_duration', [
            job_name: env.JOB_NAME,
            duration_seconds: duration / 1000,
            status: 'success'
        ])
        
    } catch (Exception e) {
        def duration = System.currentTimeMillis() - qualityStartTime
        recordMetric('quality_analysis_duration', [
            job_name: env.JOB_NAME,
            duration_seconds: duration / 1000,
            status: 'failed',
            error: e.getMessage()
        ])
        throw e
    }
}

def runSonarQubeAnalysis() {
    echo "執行 SonarQube 分析..."
    
    withSonarQubeEnv('SonarQube') {
        sh '''
            mvn sonar:sonar \\
                -Dsonar.projectKey=${JOB_NAME} \\
                -Dsonar.projectName="${JOB_NAME}" \\
                -Dsonar.projectVersion=${BUILD_NUMBER}
        '''
    }
    
    // 等待品質閘門結果
    timeout(time: 10, unit: 'MINUTES') {
        def qg = waitForQualityGate()
        
        // 記錄品質閘門結果
        recordMetric('sonarqube_quality_gate', [
            job_name: env.JOB_NAME,
            status: qg.status,
            project_key: env.JOB_NAME
        ])
        
        if (qg.status != 'OK') {
            echo "品質閘門未通過: ${qg.status}"
            sendQualityGateAlert(qg)
        }
    }
}

def evaluateQualityGates() {
    echo "評估品質閘門..."
    
    // 讀取 SonarQube 結果
    def sonarResults = readSonarQubeResults()
    
    // 評估品質標準
    def qualityScore = calculateQualityScore(sonarResults)
    
    // 記錄品質指標
    recordMetric('code_quality_score', [
        job_name: env.JOB_NAME,
        quality_score: qualityScore,
        bugs: sonarResults.bugs,
        vulnerabilities: sonarResults.vulnerabilities,
        code_smells: sonarResults.codeSmells,
        coverage: sonarResults.coverage,
        duplicated_lines: sonarResults.duplicatedLines
    ])
    
    // 檢查品質閾值
    if (qualityScore < (env.QUALITY_GATE_THRESHOLD as Integer)) {
        error("代碼品質不符合標準: ${qualityScore} < ${env.QUALITY_GATE_THRESHOLD}")
    }
}

def publishQualityMetrics() {
    echo "發布品質指標..."
    
    // 發布 Checkstyle 報告
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'target/site',
        reportFiles: 'checkstyle.html',
        reportName: 'Checkstyle Report'
    ])
    
    // 發布 PMD 報告
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'target/site',
        reportFiles: 'pmd.html',
        reportName: 'PMD Report'
    ])
    
    // 發布 SpotBugs 報告
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'target/site',
        reportFiles: 'spotbugs.html',
        reportName: 'SpotBugs Report'
    ])
    
    // 歸檔品質指標檔案
    archiveArtifacts artifacts: 'target/site/**', allowEmptyArchive: true
}

// === 部署監控函式 ===

def deployWithMonitoring() {
    echo "執行帶監控的部署..."
    
    def deployStartTime = System.currentTimeMillis()
    
    try {
        // 預部署檢查
        preDeploymentHealthCheck()
        
        // 執行部署
        executeDeployment()
        
        // 部署後驗證
        postDeploymentVerification()
        
        def duration = System.currentTimeMillis() - deployStartTime
        recordMetric('deployment_duration', [
            job_name: env.JOB_NAME,
            environment: env.ENVIRONMENT,
            duration_seconds: duration / 1000,
            status: 'success'
        ])
        
    } catch (Exception e) {
        def duration = System.currentTimeMillis() - deployStartTime
        recordMetric('deployment_duration', [
            job_name: env.JOB_NAME,
            environment: env.ENVIRONMENT,
            duration_seconds: duration / 1000,
            status: 'failed',
            error: e.getMessage()
        ])
        throw e
    }
}

def validateDeploymentHealth() {
    echo "驗證部署健康狀態..."
    
    // 健康檢查
    def healthCheckResults = performHealthChecks()
    
    // 記錄健康檢查結果
    recordMetric('deployment_health_check', [
        job_name: env.JOB_NAME,
        environment: env.ENVIRONMENT,
        status: healthCheckResults.overall,
        services_healthy: healthCheckResults.healthyServices,
        services_unhealthy: healthCheckResults.unhealthyServices
    ])
    
    if (healthCheckResults.overall != 'healthy') {
        sendDeploymentHealthAlert(healthCheckResults)
    }
}

def monitorPostDeploymentMetrics() {
    echo "監控部署後指標..."
    
    // 監控應用程式指標
    monitorApplicationMetrics()
    
    // 監控業務指標
    monitorBusinessMetrics()
    
    // 設定部署後監控
    setupPostDeploymentMonitoring()
}
```

### 通知與告警機制

#### 15.3 智慧通知系統

**多渠道通知 Pipeline：**

```groovy
def sendSuccessNotification() {
    echo "發送成功通知..."
    
    def notification = buildNotificationPayload('success')
    
    // 發送到多個渠道
    parallel(
        "Email": {
            sendEmailNotification(notification)
        },
        "Slack": {
            sendSlackNotification(notification)
        },
        "Teams": {
            sendTeamsNotification(notification)
        },
        "Webhook": {
            sendWebhookNotification(notification)
        }
    )
}

def sendFailureAlert() {
    echo "發送失敗警告..."
    
    def alert = buildAlertPayload('failure')
    
    // 分級通知
    if (isProductionBranch()) {
        sendUrgentAlert(alert)
    } else {
        sendStandardAlert(alert)
    }
    
    // 觸發事故管理流程
    if (isCriticalFailure()) {
        triggerIncidentManagement(alert)
    }
}

def buildNotificationPayload(status) {
    def payload = [
        status: status,
        jobName: env.JOB_NAME,
        buildNumber: env.BUILD_NUMBER,
        buildUrl: env.BUILD_URL,
        branch: env.GIT_BRANCH,
        commit: env.GIT_COMMIT,
        timestamp: new Date().format('yyyy-MM-dd HH:mm:ss'),
        duration: currentBuild.durationString,
        executor: env.NODE_NAME ?: 'master'
    ]
    
    // 添加測試結果
    if (fileExists('target/surefire-reports')) {
        def testResults = parseTestResults('target/surefire-reports')
        payload.testResults = testResults
    }
    
    // 添加品質指標
    if (fileExists('target/sonar')) {
        def qualityResults = readSonarQubeResults()
        payload.qualityResults = qualityResults
    }
    
    return payload
}

def sendSlackNotification(notification) {
    def color = notification.status == 'success' ? 'good' : 'danger'
    def emoji = notification.status == 'success' ? ':white_check_mark:' : ':x:'
    
    def message = """
${emoji} *${notification.status.toUpperCase()}* - ${notification.jobName} #${notification.buildNumber}
*Branch:* ${notification.branch}
*Duration:* ${notification.duration}
*Executor:* ${notification.executor}
"""
    
    if (notification.testResults) {
        message += """
*Tests:* ${notification.testResults.passed}/${notification.testResults.total} passed
"""
    }
    
    if (notification.qualityResults) {
        message += """
*Quality:* ${notification.qualityResults.qualityGate}
"""
    }
    
    slackSend(
        channel: env.SLACK_CHANNEL,
        color: color,
        message: message,
        teamDomain: 'yourteam',
        token: 'slack-token'
    )
}

def sendEmailNotification(notification) {
    def subject = "${notification.status.toUpperCase()} - ${notification.jobName} #${notification.buildNumber}"
    
    def body = """
<html>
<body>
<h2>Build ${notification.status.toUpperCase()}</h2>
<table border="1" cellpadding="5">
    <tr><td><b>Job</b></td><td>${notification.jobName}</td></tr>
    <tr><td><b>Build Number</b></td><td>${notification.buildNumber}</td></tr>
    <tr><td><b>Branch</b></td><td>${notification.branch}</td></tr>
    <tr><td><b>Duration</b></td><td>${notification.duration}</td></tr>
    <tr><td><b>Timestamp</b></td><td>${notification.timestamp}</td></tr>
</table>

<h3>Links</h3>
<ul>
    <li><a href="${notification.buildUrl}">Build Details</a></li>
    <li><a href="${notification.buildUrl}console">Console Output</a></li>
</ul>
"""
    
    if (notification.testResults) {
        body += """
<h3>Test Results</h3>
<table border="1" cellpadding="5">
    <tr><td><b>Total</b></td><td>${notification.testResults.total}</td></tr>
    <tr><td><b>Passed</b></td><td>${notification.testResults.passed}</td></tr>
    <tr><td><b>Failed</b></td><td>${notification.testResults.failed}</td></tr>
    <tr><td><b>Skipped</b></td><td>${notification.testResults.skipped}</td></tr>
</table>
"""
    }
    
    body += """
</body>
</html>
"""
    
    emailext(
        subject: subject,
        body: body,
        mimeType: 'text/html',
        to: env.EMAIL_RECIPIENTS
    )
}

def sendTeamsNotification(notification) {
    def webhook = env.TEAMS_WEBHOOK_URL
    def color = notification.status == 'success' ? '00FF00' : 'FF0000'
    
    def payload = [
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": color,
        "summary": "Jenkins Build ${notification.status}",
        "sections": [[
            "activityTitle": "Jenkins Build ${notification.status.toUpperCase()}",
            "activitySubtitle": "${notification.jobName} #${notification.buildNumber}",
            "facts": [
                ["name": "Branch", "value": notification.branch],
                ["name": "Duration", "value": notification.duration],
                ["name": "Executor", "value": notification.executor]
            ]
        ]],
        "potentialAction": [[
            "@type": "OpenUri",
            "name": "View Build",
            "targets": [["os": "default", "uri": notification.buildUrl]]
        ]]
    ]
    
    httpRequest(
        httpMode: 'POST',
        url: webhook,
        contentType: 'APPLICATION_JSON',
        requestBody: writeJSON(returnText: true, json: payload)
    )
}
```

### 效能優化策略

#### 15.4 Pipeline 效能優化

**效能優化範例：**

```groovy
// 效能優化 Pipeline
pipeline {
    agent none
    
    options {
        // 並行執行優化
        parallelsAlwaysFailFast()
        
        // 建置保留策略
        buildDiscarder(logRotator(
            numToKeepStr: '10',
            daysToKeepStr: '30',
            artifactNumToKeepStr: '5'
        ))
        
        // 超時控制
        timeout(time: 45, unit: 'MINUTES')
    }
    
    stages {
        stage('快取優化初始化') {
            agent any
            steps {
                script {
                    optimizeCacheStrategy()
                    setupDistributedCache()
                }
            }
        }
        
        stage('並行建置優化') {
            parallel {
                stage('代碼編譯') {
                    agent { label 'compile-agent' }
                    steps {
                        script {
                            // 使用編譯快取
                            restoreCompilationCache()
                            
                            // 增量編譯
                            runIncrementalCompilation()
                            
                            // 儲存編譯快取
                            saveCompilationCache()
                        }
                    }
                }
                
                stage('依賴下載') {
                    agent { label 'maven-agent' }
                    steps {
                        script {
                            // 使用 Maven 本地快取
                            optimizeMavenCache()
                            
                            // 並行下載依賴
                            downloadDependenciesParallel()
                        }
                    }
                }
                
                stage('靜態分析') {
                    agent { label 'analysis-agent' }
                    steps {
                        script {
                            // 只分析變更的檔案
                            runIncrementalAnalysis()
                        }
                    }
                }
            }
        }
        
        stage('測試優化') {
            parallel {
                stage('單元測試') {
                    agent { label 'test-agent' }
                    steps {
                        script {
                            // 並行測試執行
                            runParallelUnitTests()
                        }
                    }
                }
                
                stage('整合測試') {
                    agent { label 'integration-agent' }
                    steps {
                        script {
                            // 測試容器化
                            runContainerizedTests()
                        }
                    }
                }
            }
        }
        
        stage('部署優化') {
            when { branch 'master' }
            agent { label 'deploy-agent' }
            steps {
                script {
                    // 零停機部署
                    runZeroDowntimeDeployment()
                    
                    // 部署驗證
                    validateDeploymentOptimized()
                }
            }
        }
    }
    
    post {
        always {
            node('master') {
                script {
                    // 效能分析
                    analyzePerformanceMetrics()
                    
                    // 優化建議
                    generateOptimizationRecommendations()
                }
            }
        }
    }
}

def optimizeCacheStrategy() {
    echo "優化快取策略..."
    
    // 設定分散式快取
    sh '''
        # 設定 Redis 快取
        redis-cli ping || echo "Redis 快取不可用"
        
        # 設定檔案系統快取
        mkdir -p /opt/jenkins-cache/{maven,gradle,npm,docker}
        
        # 設定 NFS 共享快取（如果可用）
        mount | grep nfs || echo "NFS 共享快取不可用"
    '''
    
    // 快取預熱
    preWarmCache()
    
    echo "✅ 快取策略優化完成"
}

def restoreCompilationCache() {
    echo "恢復編譯快取..."
    
    // 從分散式快取恢復
    sh '''
        CACHE_KEY="${JOB_NAME}-${GIT_COMMIT}"
        
        # 檢查快取是否存在
        if redis-cli exists "compile:${CACHE_KEY}" > /dev/null; then
            echo "找到編譯快取: ${CACHE_KEY}"
            
            # 恢復編譯結果
            redis-cli get "compile:${CACHE_KEY}" | base64 -d | tar -xzf - -C target/ 2>/dev/null || true
        else
            echo "未找到編譯快取"
        fi
    '''
}

def runIncrementalCompilation() {
    echo "執行增量編譯..."
    
    // 檢測變更的檔案
    def changedFiles = sh(
        script: 'git diff --name-only HEAD~1',
        returnStdout: true
    ).trim().split('\n')
    
    if (changedFiles.size() > 0) {
        echo "檢測到 ${changedFiles.size()} 個變更檔案"
        
        // 只編譯變更的模組
        def changedModules = detectChangedModules(changedFiles)
        
        if (changedModules.size() > 0) {
            echo "編譯變更的模組: ${changedModules.join(', ')}"
            sh "mvn compile -pl ${changedModules.join(',')}"
        } else {
            echo "執行完整編譯"
            sh "mvn compile"
        }
    } else {
        echo "無變更檔案，跳過編譯"
    }
}

def runParallelUnitTests() {
    echo "執行並行單元測試..."
    
    // 自動檢測可用的 CPU 核心數
    def availableCores = sh(
        script: 'nproc',
        returnStdout: true
    ).trim() as Integer
    
    def threadCount = Math.max(1, (availableCores * 0.8) as Integer)
    
    echo "使用 ${threadCount} 個執行緒執行測試"
    
    sh """
        mvn test \\
            -Dmaven.test.parallel=classes \\
            -Dmaven.test.perCoreThreadCount=false \\
            -Dmaven.test.threadCount=${threadCount} \\
            -Dmaven.test.forkCount=${threadCount} \\
            -Dmaven.test.reuseForks=true
    """
}

def runContainerizedTests() {
    echo "執行容器化測試..."
    
    // 使用 Docker 容器並行執行測試
    sh '''
        # 啟動測試資料庫容器
        docker run -d --name test-db \\
            -e POSTGRES_DB=testdb \\
            -e POSTGRES_USER=test \\
            -e POSTGRES_PASSWORD=test \\
            -p 5432:5432 \\
            postgres:13
        
        # 等待資料庫就緒
        while ! docker exec test-db pg_isready; do
            sleep 1
        done
        
        # 執行整合測試
        mvn failsafe:integration-test \\
            -Dtest.database.url=jdbc:postgresql://localhost:5432/testdb
        
        # 清理測試容器
        docker stop test-db
        docker rm test-db
    '''
}

def analyzePerformanceMetrics() {
    echo "分析效能指標..."
    
    // 收集建置效能資料
    def performanceData = [
        buildDuration: currentBuild.duration,
        buildNumber: env.BUILD_NUMBER,
        timestamp: new Date().time,
        stages: collectStageMetrics()
    ]
    
    // 分析效能趨勢
    analyzePerformanceTrends(performanceData)
    
    // 識別效能瓶頸
    identifyPerformanceBottlenecks(performanceData)
    
    // 生成效能報告
    generatePerformanceReport(performanceData)
}

def generateOptimizationRecommendations() {
    echo "生成優化建議..."
    
    def recommendations = []
    
    // 基於歷史資料分析
    def historicalData = getHistoricalPerformanceData()
    
    // 檢查建置時間趨勢
    if (isBuildTimeIncreasing(historicalData)) {
        recommendations.add([
            type: 'build_time',
            message: '建置時間呈上升趨勢，建議檢查依賴項目或增加快取策略',
            priority: 'high'
        ])
    }
    
    // 檢查測試執行時間
    if (isTestTimeExcessive(historicalData)) {
        recommendations.add([
            type: 'test_time',
            message: '測試執行時間過長，建議增加並行度或優化測試程式碼',
            priority: 'medium'
        ])
    }
    
    // 檢查資源使用率
    if (isResourceUnderUtilized(historicalData)) {
        recommendations.add([
            type: 'resource_usage',
            message: '資源使用率偏低，可以增加並行任務或使用更小的 Agent',
            priority: 'low'
        ])
    }
    
    // 輸出建議
    if (recommendations.size() > 0) {
        echo "=== 效能優化建議 ==="
        recommendations.each { rec ->
            echo "[${rec.priority.toUpperCase()}] ${rec.type}: ${rec.message}"
        }
        
        // 儲存建議到檔案
        writeJSON file: 'optimization-recommendations.json', json: recommendations
        archiveArtifacts artifacts: 'optimization-recommendations.json'
    } else {
        echo "目前效能表現良好，無特別優化建議"
    }
}
```

### 實務監控案例

#### 案例：企業級監控儀表板

**Grafana 儀表板配置：**

```json
{
  "dashboard": {
    "title": "Jenkins CI/CD 監控儀表板",
    "panels": [
      {
        "title": "建置成功率",
        "type": "stat",
        "targets": [
          {
            "expr": "rate(jenkins_job_success_total[1h]) / rate(jenkins_job_total[1h]) * 100"
          }
        ]
      },
      {
        "title": "平均建置時間",
        "type": "graph",
        "targets": [
          {
            "expr": "avg(jenkins_job_duration_seconds) by (job_name)"
          }
        ]
      },
      {
        "title": "部署頻率",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(jenkins_deployment_total[24h])"
          }
        ]
      },
      {
        "title": "測試覆蓋率趨勢",
        "type": "graph",
        "targets": [
          {
            "expr": "jenkins_test_coverage_percent"
          }
        ]
      }
    ]
  }
}
```

### 注意要點

1. **監控資料保留**：
   - 設定合適的資料保留策略
   - 平衡儲存成本與查詢需求
   - 實施資料壓縮與歸檔

2. **告警降噪**：
   - 避免過度告警造成疲勞
   - 實施智慧告警聚合
   - 設定告警優先級

3. **效能影響**：
   - 監控系統本身的資源消耗
   - 避免影響主要 CI/CD 流程
   - 合理配置採樣頻率

4. **安全隱私**：
   - 保護敏感監控資料
   - 控制監控資料存取權限
   - 遵循資料保護法規

### 認證相關知識

| 認證項目 | 對應內容 |
|----------|----------|
| 監控設定 | Prometheus、Grafana 整合 |
| 通知機制 | 多渠道通知策略 |
| 效能優化 | Pipeline 效能調校 |
| 可觀測性 | 全方位監控體系 |

### 練習實作 - 第15章

1. **基礎練習**：建立基本的 Jenkins 監控配置
2. **進階練習**：實作多渠道智慧通知系統
3. **實務練習**：設計完整的企業級監控解決方案

---

## 第16章 企業級 CI/CD 架構設計

### 架構願景

- 設計可擴展的大規模 Jenkins 架構
- 實現高可用性和負載均衡策略
- 建立災難恢復和業務連續性方案
- 制定 CI/CD 治理和安全框架

### 企業架構藍圖

#### 16.1 大規模 Jenkins 架構設計

企業級 CI/CD 需要支援數千個專案、數萬次建置，並確保系統的穩定性和可擴展性。

```mermaid
graph TB
    subgraph "Load Balancer Layer"
        LB1[Load Balancer 1]
        LB2[Load Balancer 2]
    end
    
    subgraph "Jenkins Master Cluster"
        JM1[Jenkins Master 1<br/>Active]
        JM2[Jenkins Master 2<br/>Hot Standby]
        JM3[Jenkins Master 3<br/>Cold Standby]
    end
    
    subgraph "Agent Pool Management"
        AP1[Static Agent Pool]
        AP2[Dynamic Agent Pool]
        AP3[Cloud Agent Pool]
        AP4[Container Agent Pool]
    end
    
    subgraph "Storage Layer"
        SS1[Shared Storage<br/>NFS/GlusterFS]
        DB1[(Primary Database<br/>PostgreSQL)]
        DB2[(Replica Database)]
        AR1[Artifact Repository<br/>Nexus/Artifactory]
    end
    
    subgraph "Monitoring & Security"
        PM1[Prometheus]
        GF1[Grafana]
        ELK[ELK Stack]
        SEC[Security Scanner]
        LDAP[LDAP/AD]
    end
    
    subgraph "External Integrations"
        SCM[Source Control<br/>Git/SVN]
        CHAT[Chat Integration<br/>Slack/Teams]
        TICK[Ticketing System<br/>Jira/ServiceNow]
        CLOUD[Cloud Providers<br/>AWS/Azure/GCP]
    end
    
    Users --> LB1
    Users --> LB2
    
    LB1 --> JM1
    LB2 --> JM1
    LB1 --> JM2
    LB2 --> JM2
    
    JM1 --> AP1
    JM1 --> AP2
    JM1 --> AP3
    JM1 --> AP4
    
    JM2 --> AP1
    JM2 --> AP2
    JM2 --> AP3
    JM2 --> AP4
    
    JM1 --> SS1
    JM2 --> SS1
    JM3 --> SS1
    
    JM1 --> DB1
    JM2 --> DB1
    DB1 --> DB2
    
    AP1 --> AR1
    AP2 --> AR1
    AP3 --> AR1
    AP4 --> AR1
    
    JM1 --> PM1
    JM1 --> ELK
    JM1 --> SEC
    JM1 --> LDAP
    
    PM1 --> GF1
    
    JM1 --> SCM
    JM1 --> CHAT
    JM1 --> TICK
    JM1 --> CLOUD
    
    style JM1 fill:#e1f5fe
    style JM2 fill:#fff3e0
    style JM3 fill:#fce4ec
    style DB1 fill:#e8f5e8
    style DB2 fill:#fff8e1
```

#### 16.2 高可用性架構實作

**Jenkins Master 高可用性配置：**

```groovy
// 高可用性 Jenkins 配置
pipeline {
    agent none
    
    options {
        // 啟用建置分散式執行
        parallelsAlwaysFailFast()
        
        // 設定重試機制
        retry(3)
        
        // 超時控制
        timeout(time: 2, unit: 'HOURS')
        
        // 啟用檢查點
        checkoutToSubdirectory('source')
    }
    
    environment {
        // 高可用性配置
        HA_ENABLED = 'true'
        CLUSTER_MODE = 'active-standby'
        FAILOVER_THRESHOLD = '30'
        
        // 分散式存儲配置
        SHARED_WORKSPACE = '/shared/jenkins-workspace'
        ARTIFACT_REPOSITORY = 'https://nexus.company.com/repository'
        
        // 資料庫集群配置
        DB_PRIMARY = 'jdbc:postgresql://db-primary:5432/jenkins'
        DB_REPLICA = 'jdbc:postgresql://db-replica:5432/jenkins'
        
        // 監控端點
        HEALTH_CHECK_URL = 'http://localhost:8080/computer/api/json'
        METRICS_ENDPOINT = 'http://prometheus:9090'
    }
    
    stages {
        stage('高可用性初始化') {
            steps {
                script {
                    initializeHAEnvironment()
                    validateClusterHealth()
                    setupFailoverMechanisms()
                }
            }
        }
        
        stage('分散式建置執行') {
            parallel {
                stage('主要建置路徑') {
                    agent { label 'primary-pool' }
                    steps {
                        script {
                            executeWithFailover('primary') {
                                runPrimaryBuildTasks()
                            }
                        }
                    }
                }
                
                stage('備援建置路徑') {
                    agent { label 'backup-pool' }
                    when {
                        expression { params.ENABLE_BACKUP_BUILD == true }
                    }
                    steps {
                        script {
                            executeWithFailover('backup') {
                                runBackupBuildTasks()
                            }
                        }
                    }
                }
                
                stage('雲端建置路徑') {
                    agent { label 'cloud-pool' }
                    when {
                        expression { isCloudBuildRequired() }
                    }
                    steps {
                        script {
                            executeWithFailover('cloud') {
                                runCloudBuildTasks()
                            }
                        }
                    }
                }
            }
        }
        
        stage('集群狀態監控') {
            agent { label 'monitoring-node' }
            steps {
                script {
                    monitorClusterHealth()
                    validateDataConsistency()
                    checkFailoverReadiness()
                }
            }
        }
        
        stage('災難恢復測試') {
            when {
                expression { params.RUN_DR_TEST == true }
            }
            agent { label 'dr-test-node' }
            steps {
                script {
                    runDisasterRecoveryTest()
                    validateBackupIntegrity()
                    testFailoverProcedures()
                }
            }
        }
    }
    
    post {
        always {
            node('monitoring-node') {
                script {
                    collectHAMetrics()
                    updateClusterStatus()
                    generateHAReport()
                }
            }
        }
        
        failure {
            script {
                triggerFailoverIfNeeded()
                notifyOpsTeam()
                escalateToManagement()
            }
        }
    }
}

// === 高可用性管理函式 ===

def initializeHAEnvironment() {
    echo "初始化高可用性環境..."
    
    // 檢查集群配置
    validateClusterConfiguration()
    
    // 設定共享存儲
    setupSharedStorage()
    
    // 初始化資料庫連線池
    initializeDatabaseConnections()
    
    // 設定負載均衡
    configureLoadBalancer()
    
    echo "✅ 高可用性環境初始化完成"
}

def validateClusterConfiguration() {
    echo "驗證集群配置..."
    
    sh '''
        # 檢查集群節點狀態
        echo "=== 集群節點狀態 ==="
        
        # 檢查主節點
        curl -f ${JENKINS_URL}/computer/api/json?pretty=true > cluster-status.json
        
        # 解析節點狀態
        python3 << 'EOF'
import json
import sys

with open('cluster-status.json', 'r') as f:
    data = json.load(f)

total_nodes = len(data['computer'])
online_nodes = sum(1 for node in data['computer'] if not node.get('offline', True))
offline_nodes = total_nodes - online_nodes

print(f"總節點數: {total_nodes}")
print(f"在線節點: {online_nodes}")
print(f"離線節點: {offline_nodes}")

if offline_nodes > total_nodes * 0.3:
    print("警告: 超過30%的節點離線")
    sys.exit(1)

print("集群狀態正常")
EOF
    '''
    
    // 檢查網路連通性
    validateNetworkConnectivity()
    
    // 檢查存儲可用性
    validateStorageAvailability()
}

def setupSharedStorage() {
    echo "設定共享存儲..."
    
    sh '''
        # 檢查 NFS 掛載
        if ! mount | grep -q "${SHARED_WORKSPACE}"; then
            echo "掛載共享存儲..."
            sudo mount -t nfs nfs-server:/shared/jenkins ${SHARED_WORKSPACE}
        fi
        
        # 檢查存儲可用性
        if [ ! -w "${SHARED_WORKSPACE}" ]; then
            echo "錯誤: 共享存儲不可寫入"
            exit 1
        fi
        
        # 建立必要目錄結構
        mkdir -p ${SHARED_WORKSPACE}/{builds,workspaces,artifacts,logs}
        
        # 設定權限
        chmod 755 ${SHARED_WORKSPACE}
        
        echo "✅ 共享存儲設定完成"
    '''
}

def initializeDatabaseConnections() {
    echo "初始化資料庫連線..."
    
    script {
        // 測試主資料庫連線
        try {
            sh "psql '${env.DB_PRIMARY}' -c 'SELECT 1;'"
            echo "✅ 主資料庫連線正常"
            env.DB_PRIMARY_STATUS = 'healthy'
        } catch (Exception e) {
            echo "❌ 主資料庫連線失敗: ${e.getMessage()}"
            env.DB_PRIMARY_STATUS = 'unhealthy'
        }
        
        // 測試備援資料庫連線
        try {
            sh "psql '${env.DB_REPLICA}' -c 'SELECT 1;'"
            echo "✅ 備援資料庫連線正常"
            env.DB_REPLICA_STATUS = 'healthy'
        } catch (Exception e) {
            echo "❌ 備援資料庫連線失敗: ${e.getMessage()}"
            env.DB_REPLICA_STATUS = 'unhealthy'
        }
        
        // 檢查資料同步狀態
        if (env.DB_PRIMARY_STATUS == 'healthy' && env.DB_REPLICA_STATUS == 'healthy') {
            validateDatabaseReplication()
        }
    }
}

def configureLoadBalancer() {
    echo "配置負載均衡器..."
    
    sh '''
        # 更新 HAProxy 配置
        cat > haproxy.cfg << 'EOF'
global
    daemon
    maxconn 4096
    log stdout local0

defaults
    mode http
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms
    option httpchk GET /login

frontend jenkins_frontend
    bind *:8080
    default_backend jenkins_servers

backend jenkins_servers
    balance roundrobin
    option httpchk GET /computer/api/json
    
    server jenkins1 jenkins-master-1:8080 check
    server jenkins2 jenkins-master-2:8080 check backup
    server jenkins3 jenkins-master-3:8080 check backup

listen stats
    bind *:8404
    stats enable
    stats uri /stats
    stats refresh 30s
EOF

        # 驗證配置
        haproxy -c -f haproxy.cfg
        
        # 重新載入配置
        sudo systemctl reload haproxy
        
        echo "✅ 負載均衡器配置完成"
    '''
}

def executeWithFailover(poolType, closure) {
    def maxRetries = 3
    def retryCount = 0
    def lastException = null
    
    while (retryCount < maxRetries) {
        try {
            echo "執行 ${poolType} 建置 (嘗試 ${retryCount + 1}/${maxRetries})"
            
            // 檢查節點池健康狀態
            if (!isPoolHealthy(poolType)) {
                throw new Exception("節點池 ${poolType} 不健康")
            }
            
            // 執行實際任務
            closure()
            
            echo "✅ ${poolType} 建置執行成功"
            return
            
        } catch (Exception e) {
            lastException = e
            retryCount++
            
            echo "❌ ${poolType} 建置失敗 (嘗試 ${retryCount}): ${e.getMessage()}"
            
            if (retryCount < maxRetries) {
                // 等待後重試
                sleep(30)
                
                // 嘗試切換到其他節點池
                if (shouldSwitchPool(poolType, e)) {
                    poolType = getAlternativePool(poolType)
                    echo "切換到備援節點池: ${poolType}"
                }
            }
        }
    }
    
    // 所有重試都失敗，拋出最後的例外
    error("${poolType} 建置在 ${maxRetries} 次嘗試後仍然失敗: ${lastException.getMessage()}")
}

def isPoolHealthy(poolType) {
    try {
        def poolStatus = sh(
            script: "curl -s ${env.JENKINS_URL}/computer/api/json | jq '.computer[] | select(.displayName | contains(\"${poolType}\")) | .offline'",
            returnStdout: true
        ).trim()
        
        return poolStatus == 'false'
    } catch (Exception e) {
        echo "檢查節點池 ${poolType} 狀態失敗: ${e.getMessage()}"
        return false
    }
}

def shouldSwitchPool(currentPool, exception) {
    // 根據錯誤類型決定是否切換節點池
    def errorMessage = exception.getMessage().toLowerCase()
    
    if (errorMessage.contains('timeout') || 
        errorMessage.contains('connection') || 
        errorMessage.contains('network')) {
        return true
    }
    
    if (currentPool == 'primary-pool') {
        return true  // 主節點池失敗時總是嘗試切換
    }
    
    return false
}

def getAlternativePool(currentPool) {
    def poolMapping = [
        'primary-pool': 'backup-pool',
        'backup-pool': 'cloud-pool',
        'cloud-pool': 'primary-pool'
    ]
    
    return poolMapping[currentPool] ?: 'backup-pool'
}

def monitorClusterHealth() {
    echo "監控集群健康狀態..."
    
    // 收集集群指標
    def clusterMetrics = collectClusterMetrics()
    
    // 檢查關鍵指標
    validateClusterMetrics(clusterMetrics)
    
    // 預測潛在問題
    predictClusterIssues(clusterMetrics)
    
    // 更新監控儀表板
    updateClusterDashboard(clusterMetrics)
}

def collectClusterMetrics() {
    echo "收集集群指標..."
    
    def metrics = [:]
    
    // Jenkins Master 指標
    metrics.masterStatus = getMasterStatus()
    
    // Agent 節點指標
    metrics.agentStatus = getAgentStatus()
    
    // 資料庫指標
    metrics.databaseStatus = getDatabaseStatus()
    
    // 存儲指標
    metrics.storageStatus = getStorageStatus()
    
    // 網路指標
    metrics.networkStatus = getNetworkStatus()
    
    return metrics
}

def validateDataConsistency() {
    echo "驗證數據一致性..."
    
    sh '''
        # 檢查主備資料庫一致性
        echo "檢查資料庫一致性..."
        
        # 比較主備資料庫的關鍵表
        PRIMARY_COUNT=$(psql "${DB_PRIMARY}" -t -c "SELECT COUNT(*) FROM builds;")
        REPLICA_COUNT=$(psql "${DB_REPLICA}" -t -c "SELECT COUNT(*) FROM builds;")
        
        echo "主資料庫建置記錄: ${PRIMARY_COUNT}"
        echo "備援資料庫建置記錄: ${REPLICA_COUNT}"
        
        DIFF=$((PRIMARY_COUNT - REPLICA_COUNT))
        if [ ${DIFF#-} -gt 10 ]; then
            echo "警告: 主備資料庫記錄差異過大 (${DIFF})"
        else
            echo "✅ 資料庫同步狀態正常"
        fi
        
        # 檢查共享存儲一致性
        echo "檢查存儲一致性..."
        find ${SHARED_WORKSPACE} -name "*.lock" -mtime +1 -delete
        
        # 驗證關鍵檔案存在
        if [ ! -f "${SHARED_WORKSPACE}/cluster.lock" ]; then
            touch "${SHARED_WORKSPACE}/cluster.lock"
        fi
        
        echo "✅ 存儲一致性檢查完成"
    '''
}

def checkFailoverReadiness() {
    echo "檢查容災準備狀態..."
    
    // 檢查備援節點狀態
    validateStandbyNodes()
    
    // 檢查備份完整性
    validateBackupIntegrity()
    
    // 檢查容災腳本
    validateFailoverScripts()
    
    // 模擬容災場景
    if (params.RUN_FAILOVER_SIMULATION == true) {
        simulateFailoverScenario()
    }
}

def validateStandbyNodes() {
    echo "驗證備援節點..."
    
    sh '''
        # 檢查備援 Jenkins Master
        echo "檢查備援 Jenkins Master..."
        
        # 嘗試連接備援節點
        if curl -f http://jenkins-master-2:8080/computer/api/json > /dev/null 2>&1; then
            echo "✅ 備援 Master 2 狀態正常"
        else
            echo "❌ 備援 Master 2 不可用"
        fi
        
        if curl -f http://jenkins-master-3:8080/computer/api/json > /dev/null 2>&1; then
            echo "✅ 備援 Master 3 狀態正常"
        else
            echo "❌ 備援 Master 3 不可用"
        fi
        
        # 檢查備援節點配置同步
        echo "檢查配置同步狀態..."
        
        rsync -av --dry-run /var/lib/jenkins/ jenkins-master-2:/var/lib/jenkins/ | tail -1
        rsync -av --dry-run /var/lib/jenkins/ jenkins-master-3:/var/lib/jenkins/ | tail -1
    '''
}

def runDisasterRecoveryTest() {
    echo "執行災難恢復測試..."
    
    try {
        // 建立測試環境
        setupDRTestEnvironment()
        
        // 模擬災難場景
        simulateDisasterScenario()
        
        // 執行恢復程序
        executeRecoveryProcedures()
        
        // 驗證恢復結果
        validateRecoveryResults()
        
        echo "✅ 災難恢復測試成功"
        
    } finally {
        // 清理測試環境
        cleanupDRTestEnvironment()
    }
}

def setupDRTestEnvironment() {
    echo "設定災難恢復測試環境..."
    
    sh '''
        # 建立測試命名空間
        kubectl create namespace jenkins-dr-test || true
        
        # 部署測試 Jenkins 實例
        helm install jenkins-dr-test jenkins/jenkins \\
            --namespace jenkins-dr-test \\
            --set persistence.enabled=false \\
            --set rbac.create=true
        
        # 等待部署完成
        kubectl wait --for=condition=Ready pod/jenkins-dr-test-0 \\
            --namespace jenkins-dr-test --timeout=300s
        
        echo "✅ DR 測試環境設定完成"
    '''
}

def simulateDisasterScenario() {
    echo "模擬災難場景..."
    
    sh '''
        # 模擬主節點失效
        echo "模擬主 Jenkins Master 失效..."
        
        # 停止主節點服務（模擬）
        # systemctl stop jenkins  # 在實際環境中不執行
        
        # 模擬網路分割
        echo "模擬網路分割..."
        
        # 模擬資料庫故障
        echo "模擬資料庫故障..."
        
        echo "災難場景模擬完成"
    '''
}

def executeRecoveryProcedures() {
    echo "執行恢復程序..."
    
    sh '''
        # 啟動容災程序
        echo "執行自動容災..."
        
        # 1. 檢測主節點狀態
        if ! curl -f http://jenkins-master-1:8080/computer/api/json; then
            echo "主節點不可用，啟動容災程序"
            
            # 2. 提升備援節點
            echo "提升備援節點為主節點..."
            
            # 3. 更新負載均衡器配置
            echo "更新負載均衡器配置..."
            
            # 4. 重新配置 DNS
            echo "更新 DNS 記錄..."
            
            # 5. 驗證服務可用性
            echo "驗證服務恢復..."
        fi
        
        echo "✅ 恢復程序執行完成"
    '''
}

def validateRecoveryResults() {
    echo "驗證恢復結果..."
    
    // 檢查服務可用性
    def servicesHealthy = checkServicesHealth()
    
    // 檢查數據完整性
    def dataIntact = verifyDataIntegrity()
    
    // 檢查功能正常性
    def functionalityWorking = testBasicFunctionality()
    
    if (!servicesHealthy || !dataIntact || !functionalityWorking) {
        error("災難恢復驗證失敗")
    }
    
    echo "✅ 災難恢復驗證成功"
}

// === 治理和安全函式 ===

def setupGovernanceFramework() {
    echo "設定治理框架..."
    
    // 建立角色權限矩陣
    setupRoleBasedAccessControl()
    
    // 設定合規檢查
    setupComplianceChecks()
    
    // 建立審計日誌
    setupAuditLogging()
    
    // 設定變更管理
    setupChangeManagement()
}

def setupRoleBasedAccessControl() {
    echo "設定角色基礎存取控制..."
    
    sh '''
        # 建立角色定義檔案
        cat > roles-definition.yaml << 'EOF'
roles:
  jenkins-admin:
    permissions:
      - "hudson.model.Hudson.Administer"
      - "hudson.model.Computer.Configure"
      - "hudson.model.Run.Delete"
      - "hudson.model.View.Configure"
    members:
      - "admin@company.com"
      - "devops-team@company.com"
      
  project-lead:
    permissions:
      - "hudson.model.Item.Configure"
      - "hudson.model.Item.Build"
      - "hudson.model.Run.Update"
    members:
      - "project-leads@company.com"
      
  developer:
    permissions:
      - "hudson.model.Item.Read"
      - "hudson.model.Item.Build"
      - "hudson.model.Run.Replay"
    members:
      - "developers@company.com"
      
  read-only:
    permissions:
      - "hudson.model.Item.Read"
      - "hudson.model.Run.Artifacts"
    members:
      - "stakeholders@company.com"

security-realms:
  ldap:
    server: "ldap://ldap.company.com:389"
    root-dn: "dc=company,dc=com"
    user-search-base: "ou=users"
    group-search-base: "ou=groups"
    
  saml:
    idp-metadata-url: "https://sso.company.com/metadata"
    sp-entity-id: "jenkins.company.com"
EOF

        echo "✅ RBAC 配置建立完成"
    '''
}

def setupComplianceChecks() {
    echo "設定合規檢查..."
    
    sh '''
        # 建立合規檢查腳本
        cat > compliance-checks.sh << 'EOF'
#!/bin/bash

# SOX 合規檢查
check_sox_compliance() {
    echo "執行 SOX 合規檢查..."
    
    # 檢查變更控制
    if [ ! -f "/var/lib/jenkins/change-control.log" ]; then
        echo "警告: 缺少變更控制日誌"
        return 1
    fi
    
    # 檢查職責分離
    check_segregation_of_duties
    
    # 檢查審計日誌
    check_audit_logs
    
    echo "✅ SOX 合規檢查完成"
}

# GDPR 合規檢查
check_gdpr_compliance() {
    echo "執行 GDPR 合規檢查..."
    
    # 檢查數據加密
    check_data_encryption
    
    # 檢查數據保留政策
    check_data_retention
    
    # 檢查存取日誌
    check_access_logs
    
    echo "✅ GDPR 合規檢查完成"
}

# ISO 27001 合規檢查
check_iso27001_compliance() {
    echo "執行 ISO 27001 合規檢查..."
    
    # 檢查資訊安全政策
    check_security_policies
    
    # 檢查風險評估
    check_risk_assessment
    
    # 檢查事故回應
    check_incident_response
    
    echo "✅ ISO 27001 合規檢查完成"
}

# 執行所有合規檢查
main() {
    echo "開始合規檢查..."
    
    check_sox_compliance
    check_gdpr_compliance
    check_iso27001_compliance
    
    echo "✅ 所有合規檢查完成"
}

main "$@"
EOF

        chmod +x compliance-checks.sh
        
        echo "✅ 合規檢查腳本建立完成"
    '''
}

def setupAuditLogging() {
    echo "設定審計日誌..."
    
    sh '''
        # 建立審計日誌配置
        cat > audit-logging.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- 審計日誌 Appender -->
    <appender name="AUDIT" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>/var/log/jenkins/audit.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>/var/log/jenkins/audit.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>365</maxHistory>
            <totalSizeCap>10GB</totalSizeCap>
        </rollingPolicy>
        <encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">
            <providers>
                <timestamp/>
                <logLevel/>
                <loggerName/>
                <mdc/>
                <arguments/>
                <message/>
                <stackTrace/>
            </providers>
        </encoder>
    </appender>
    
    <!-- 安全事件日誌 -->
    <logger name="hudson.security" level="INFO" additivity="false">
        <appender-ref ref="AUDIT"/>
    </logger>
    
    <!-- 系統配置變更日誌 -->
    <logger name="hudson.model.UpdateCenter" level="INFO" additivity="false">
        <appender-ref ref="AUDIT"/>
    </logger>
    
    <!-- 用戶操作日誌 -->
    <logger name="hudson.model.User" level="INFO" additivity="false">
        <appender-ref ref="AUDIT"/>
    </logger>
</configuration>
EOF

        echo "✅ 審計日誌配置完成"
    '''
}
```

#### 16.3 可擴展性與效能調校

**動態擴展架構：**

```groovy
// 動態擴展管理 Pipeline
pipeline {
    agent { label 'scaling-controller' }
    
    parameters {
        choice(
            name: 'SCALING_ACTION',
            choices: ['auto', 'scale-up', 'scale-down', 'optimize'],
            description: '擴展操作'
        )
        string(
            name: 'TARGET_CAPACITY',
            defaultValue: '80',
            description: '目標容量百分比'
        )
    }
    
    environment {
        // 擴展配置
        MIN_AGENTS = '10'
        MAX_AGENTS = '100'
        SCALE_UP_THRESHOLD = '80'
        SCALE_DOWN_THRESHOLD = '30'
        
        // 雲端配置
        AWS_REGION = 'ap-northeast-1'
        AZURE_REGION = 'East Asia'
        GCP_ZONE = 'asia-east1-a'
        
        // Kubernetes 配置
        K8S_NAMESPACE = 'jenkins-agents'
        HELM_CHART = 'jenkins/jenkins-agent'
    }
    
    stages {
        stage('容量評估') {
            steps {
                script {
                    assessCurrentCapacity()
                    analyzeBuildQueue()
                    predictCapacityNeeds()
                }
            }
        }
        
        stage('擴展決策') {
            steps {
                script {
                    def scalingDecision = makeScalingDecision()
                    env.SCALING_DECISION = scalingDecision.action
                    env.TARGET_AGENT_COUNT = scalingDecision.targetCount.toString()
                }
            }
        }
        
        stage('執行擴展') {
            parallel {
                stage('AWS 擴展') {
                    when {
                        expression { needsAWSScaling() }
                    }
                    steps {
                        script {
                            scaleAWSAgents()
                        }
                    }
                }
                
                stage('Azure 擴展') {
                    when {
                        expression { needsAzureScaling() }
                    }
                    steps {
                        script {
                            scaleAzureAgents()
                        }
                    }
                }
                
                stage('GCP 擴展') {
                    when {
                        expression { needsGCPScaling() }
                    }
                    steps {
                        script {
                            scaleGCPAgents()
                        }
                    }
                }
                
                stage('Kubernetes 擴展') {
                    when {
                        expression { needsK8sScaling() }
                    }
                    steps {
                        script {
                            scaleKubernetesAgents()
                        }
                    }
                }
            }
        }
        
        stage('擴展驗證') {
            steps {
                script {
                    validateScalingResults()
                    optimizeResourceAllocation()
                    updateCapacityMetrics()
                }
            }
        }
    }
    
    post {
        always {
            script {
                recordScalingMetrics()
                generateScalingReport()
                notifyScalingResults()
            }
        }
    }
}

def assessCurrentCapacity() {
    echo "評估當前容量..."
    
    def capacityData = [:]
    
    // 取得 Agent 狀態
    def agentStatus = sh(
        script: '''
            curl -s ${JENKINS_URL}/computer/api/json | jq -r '.computer[] | [.displayName, .offline, .idle] | @csv'
        ''',
        returnStdout: true
    ).trim()
    
    // 解析 Agent 資料
    def agents = []
    agentStatus.split('\n').each { line ->
        def parts = line.split(',')
        if (parts.size() == 3) {
            agents.add([
                name: parts[0].replaceAll('"', ''),
                offline: parts[1] == 'true',
                idle: parts[2] == 'true'
            ])
        }
    }
    
    capacityData.totalAgents = agents.size()
    capacityData.onlineAgents = agents.count { !it.offline }
    capacityData.busyAgents = agents.count { !it.offline && !it.idle }
    capacityData.utilizationRate = capacityData.onlineAgents > 0 ? 
        (capacityData.busyAgents / capacityData.onlineAgents * 100).round(2) : 0
    
    echo "容量評估結果:"
    echo "  總 Agent 數: ${capacityData.totalAgents}"
    echo "  在線 Agent 數: ${capacityData.onlineAgents}"
    echo "  忙碌 Agent 數: ${capacityData.busyAgents}"
    echo "  使用率: ${capacityData.utilizationRate}%"
    
    // 儲存容量資料
    writeJSON file: 'capacity-assessment.json', json: capacityData
    
    return capacityData
}

def analyzeBuildQueue() {
    echo "分析建置佇列..."
    
    def queueData = sh(
        script: '''
            curl -s ${JENKINS_URL}/queue/api/json | jq -r '{
                "queueLength": .items | length,
                "waitingJobs": [.items[] | {
                    "name": .task.name,
                    "inQueueSince": .inQueueSince,
                    "why": .why
                }]
            }'
        ''',
        returnStdout: true
    )
    
    def queue = readJSON text: queueData
    
    echo "建置佇列分析:"
    echo "  佇列長度: ${queue.queueLength}"
    
    if (queue.queueLength > 0) {
        echo "  等待中的工作:"
        queue.waitingJobs.each { job ->
            def waitTime = (System.currentTimeMillis() - job.inQueueSince) / 1000 / 60
            echo "    ${job.name}: 等待 ${waitTime.round(1)} 分鐘 (${job.why})"
        }
    }
    
    return queue
}

def predictCapacityNeeds() {
    echo "預測容量需求..."
    
    // 分析歷史資料
    def historicalData = getHistoricalCapacityData()
    
    // 預測未來容量需求
    def prediction = runCapacityPredictionModel(historicalData)
    
    echo "容量需求預測:"
    echo "  預測時間範圍: 下一小時"
    echo "  預測最大需求: ${prediction.maxDemand} agents"
    echo "  建議容量: ${prediction.recommendedCapacity} agents"
    echo "  置信度: ${prediction.confidence}%"
    
    return prediction
}

def makeScalingDecision() {
    echo "制定擴展決策..."
    
    // 讀取容量評估結果
    def capacity = readJSON file: 'capacity-assessment.json'
    
    def decision = [
        action: 'maintain',
        targetCount: capacity.onlineAgents,
        reason: '容量充足'
    ]
    
    // 決策邏輯
    if (capacity.utilizationRate > (env.SCALE_UP_THRESHOLD as Integer)) {
        def additionalAgents = Math.ceil(capacity.onlineAgents * 0.2)
        decision.action = 'scale-up'
        decision.targetCount = Math.min(
            capacity.onlineAgents + additionalAgents,
            env.MAX_AGENTS as Integer
        )
        decision.reason = "使用率過高 (${capacity.utilizationRate}%)"
        
    } else if (capacity.utilizationRate < (env.SCALE_DOWN_THRESHOLD as Integer)) {
        def reductionAgents = Math.ceil(capacity.onlineAgents * 0.1)
        decision.action = 'scale-down'
        decision.targetCount = Math.max(
            capacity.onlineAgents - reductionAgents,
            env.MIN_AGENTS as Integer
        )
        decision.reason = "使用率過低 (${capacity.utilizationRate}%)"
    }
    
    echo "擴展決策:"
    echo "  操作: ${decision.action}"
    echo "  目標數量: ${decision.targetCount}"
    echo "  原因: ${decision.reason}"
    
    return decision
}

def scaleKubernetesAgents() {
    echo "擴展 Kubernetes Agents..."
    
    def targetCount = env.TARGET_AGENT_COUNT as Integer
    
    sh """
        # 更新 HelmChart 值
        cat > agent-values.yaml << EOF
replicaCount: ${targetCount}

resources:
  requests:
    cpu: "500m"
    memory: "1Gi"
  limits:
    cpu: "2000m"
    memory: "4Gi"

nodeSelector:
  node-type: jenkins-agent

tolerations:
  - key: "jenkins-agent"
    operator: "Equal"
    value: "true"
    effect: "NoSchedule"

affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 100
      podAffinityTerm:
        labelSelector:
          matchLabels:
            app: jenkins-agent
        topologyKey: kubernetes.io/hostname
EOF

        # 升級 Helm 部署
        helm upgrade jenkins-agents ${env.HELM_CHART} \\
            --namespace ${env.K8S_NAMESPACE} \\
            --values agent-values.yaml \\
            --wait --timeout=300s
        
        # 驗證擴展結果
        kubectl get pods -n ${env.K8S_NAMESPACE} \\
            -l app=jenkins-agent \\
            --field-selector=status.phase=Running \\
            --no-headers | wc -l
    """
    
    echo "✅ Kubernetes Agents 擴展完成"
}

def scaleAWSAgents() {
    echo "擴展 AWS Agents..."
    
    def targetCount = env.TARGET_AGENT_COUNT as Integer
    
    sh """
        # 更新 Auto Scaling Group
        aws autoscaling update-auto-scaling-group \\
            --auto-scaling-group-name jenkins-agents-asg \\
            --desired-capacity ${targetCount} \\
            --region ${env.AWS_REGION}
        
        # 等待實例啟動
        aws autoscaling wait instance-in-service \\
            --auto-scaling-group-name jenkins-agents-asg \\
            --region ${env.AWS_REGION}
        
        echo "✅ AWS Auto Scaling 更新完成"
    """
}

def validateScalingResults() {
    echo "驗證擴展結果..."
    
    // 等待 Agent 註冊
    sleep(60)
    
    // 重新評估容量
    def newCapacity = assessCurrentCapacity()
    
    // 驗證目標是否達成
    def targetCount = env.TARGET_AGENT_COUNT as Integer
    def actualCount = newCapacity.onlineAgents
    
    if (Math.abs(actualCount - targetCount) > 2) {
        echo "警告: 實際 Agent 數量 (${actualCount}) 與目標 (${targetCount}) 差異較大"
    } else {
        echo "✅ 擴展目標達成: ${actualCount}/${targetCount} agents"
    }
    
    // 驗證 Agent 健康狀態
    validateAgentHealth()
}

def optimizeResourceAllocation() {
    echo "優化資源配置..."
    
    // 分析 Agent 工作負載分佈
    analyzeAgentWorkloadDistribution()
    
    // 調整 Agent 標籤和配置
    optimizeAgentLabels()
    
    // 平衡工作負載
    balanceWorkloadDistribution()
}

def generateScalingReport() {
    echo "生成擴展報告..."
    
    def report = [
        timestamp: new Date(),
        scalingAction: env.SCALING_DECISION,
        targetCount: env.TARGET_AGENT_COUNT as Integer,
        beforeScaling: readJSON(file: 'capacity-assessment.json'),
        afterScaling: assessCurrentCapacity(),
        metrics: collectScalingMetrics()
    ]
    
    // 生成 HTML 報告
    def reportHtml = generateScalingReportHtml(report)
    writeFile file: 'scaling-report.html', text: reportHtml
    
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '.',
        reportFiles: 'scaling-report.html',
        reportName: 'Scaling Report'
    ])
    
    // 保存報告資料
    writeJSON file: 'scaling-report.json', json: report
    archiveArtifacts artifacts: 'scaling-report.*'
}
```

### 治理實務案例

#### 案例：多租戶 CI/CD 平台

**組織隔離與資源管理：**

```yaml
# 多租戶配置範例
apiVersion: v1
kind: ConfigMap
metadata:
  name: multi-tenant-config
data:
  tenants.yaml: |
    tenants:
      - name: "team-alpha"
        namespace: "jenkins-team-alpha"
        resources:
          cpu: "4"
          memory: "8Gi"
          storage: "100Gi"
        agents:
          min: 2
          max: 10
        permissions:
          - "Item.Build"
          - "Item.Configure"
        repositories:
          - "git@github.com:company/team-alpha-*"
          
      - name: "team-beta"
        namespace: "jenkins-team-beta"
        resources:
          cpu: "2"
          memory: "4Gi"
          storage: "50Gi"
        agents:
          min: 1
          max: 5
        permissions:
          - "Item.Build"
          - "Item.Read"
        repositories:
          - "git@github.com:company/team-beta-*"
```

### 關鍵注意事項

1. **高可用性設計**：
   - 避免單點故障
   - 實施自動容災切換
   - 定期測試災難恢復程序
   - 監控系統健康狀態

2. **效能最佳化**：
   - 合理配置資源限制
   - 實施智慧化擴展策略
   - 優化建置流程並行度
   - 監控並調整系統效能

3. **安全與合規**：
   - 實施強制存取控制
   - 建立完整審計追蹤
   - 遵循行業合規要求
   - 定期進行安全評估

4. **治理與管理**：
   - 建立清晰的角色權限
   - 實施變更管理流程
   - 監控資源使用情況
   - 提供自助服務能力

### 認證知識對應

| 認證項目 | 對應內容 |
|----------|----------|
| 高可用性設計 | Master 集群、容災機制 |
| 擴展性架構 | 動態擴展、多雲部署 |
| 安全治理 | RBAC、合規檢查 |
| 營運管理 | 監控、維護、優化 |

### 實務練習 - 第16章

1. **基礎練習**：設計簡單的 Jenkins 高可用性架構
2. **進階練習**：實作動態擴展和多雲部署策略
3. **實務練習**：建立完整的企業級治理框架

---

## 第17章 容器化與雲端整合

### 現代化願景

- 掌握 Docker 與 Jenkins 的深度整合
- 實現 Kubernetes 原生 CI/CD 解決方案
- 建立多雲環境的統一部署策略
- 打造彈性可擴展的容器化 Pipeline

### 容器化 CI/CD 架構

#### 17.1 Docker 與 Jenkins 整合

容器化是現代 CI/CD 的核心技術，提供一致的運行環境和高效的資源利用。

```mermaid
graph TB
    subgraph "Jenkins Master"
        JM[Jenkins Master<br/>Container]
        JV[Jenkins Volume<br/>Persistent Storage]
    end
    
    subgraph "Docker Infrastructure"
        DE[Docker Engine]
        DR[Docker Registry<br/>Harbor/ECR/ACR]
        DN[Docker Network<br/>Bridge/Overlay]
    end
    
    subgraph "Agent Containers"
        DA1[Docker Agent 1<br/>Java/Maven]
        DA2[Docker Agent 2<br/>Node.js/npm]
        DA3[Docker Agent 3<br/>Python/pip]
        DA4[Docker Agent 4<br/>Go/Docker]
    end
    
    subgraph "Build Containers"
        BC1[Build Container<br/>Dynamic Creation]
        BC2[Test Container<br/>Isolated Testing]
        BC3[Security Scan<br/>Vulnerability Check]
        BC4[Deploy Container<br/>Deployment Tools]
    end
    
    subgraph "Application Containers"
        AC1[App Container 1<br/>Production Ready]
        AC2[App Container 2<br/>Staging Version]
        AC3[App Container 3<br/>Testing Version]
    end
    
    JM --> DE
    JM --> JV
    DE --> DR
    DE --> DN
    
    JM --> DA1
    JM --> DA2
    JM --> DA3
    JM --> DA4
    
    DA1 --> BC1
    DA2 --> BC2
    DA3 --> BC3
    DA4 --> BC4
    
    BC1 --> DR
    BC2 --> DR
    BC3 --> DR
    BC4 --> DR
    
    DR --> AC1
    DR --> AC2
    DR --> AC3
    
    style JM fill:#e1f5fe
    style DR fill:#e8f5e8
    style BC1 fill:#fff3e0
    style AC1 fill:#f3e5f5
```

**完整的容器化 CI/CD Pipeline：**

```groovy
// 容器化 CI/CD Pipeline
pipeline {
    agent none
    
    parameters {
        choice(
            name: 'BUILD_MODE',
            choices: ['standard', 'multi-stage', 'buildkit', 'kaniko'],
            description: '容器建置模式'
        )
        choice(
            name: 'REGISTRY_TYPE',
            choices: ['docker-hub', 'harbor', 'ecr', 'acr', 'gcr'],
            description: '容器註冊表類型'
        )
        booleanParam(
            name: 'ENABLE_SECURITY_SCAN',
            defaultValue: true,
            description: '啟用安全性掃描'
        )
        booleanParam(
            name: 'DEPLOY_TO_K8S',
            defaultValue: false,
            description: '部署至 Kubernetes'
        )
    }
    
    environment {
        // Docker 配置
        DOCKER_REGISTRY = getDockerRegistry(params.REGISTRY_TYPE)
        DOCKER_REPO = "${DOCKER_REGISTRY}/company/java-tutorial"
        DOCKER_TAG = "${BUILD_NUMBER}-${GIT_COMMIT.take(8)}"
        DOCKER_BUILDKIT = '1'
        
        // Kubernetes 配置
        K8S_NAMESPACE = 'java-tutorial'
        K8S_CLUSTER = 'production-cluster'
        HELM_CHART_VERSION = '1.0.0'
        
        // 安全掃描配置
        TRIVY_CACHE_DIR = '/tmp/trivy-cache'
        SNYK_TOKEN = credentials('snyk-api-token')
        
        // 雲端配置
        AWS_DEFAULT_REGION = 'ap-northeast-1'
        AZURE_LOCATION = 'East Asia'
        GCP_ZONE = 'asia-east1-a'
    }
    
    stages {
        stage('容器環境準備') {
            agent {
                docker {
                    image 'docker:24-dind'
                    args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                script {
                    setupDockerEnvironment()
                    validateDockerDaemon()
                    authenticateRegistry()
                }
            }
        }
        
        stage('原始碼檢出與分析') {
            agent {
                docker {
                    image 'alpine/git:latest'
                    args '-v maven-cache:/root/.m2'
                }
            }
            steps {
                checkout scm
                script {
                    analyzeDockerfile()
                    validateContainerSecurity()
                    generateBuildContext()
                }
            }
        }
        
        stage('多階段容器建置') {
            parallel {
                stage('標準建置') {
                    when {
                        expression { params.BUILD_MODE == 'standard' }
                    }
                    agent {
                        docker {
                            image 'docker:24'
                            args '-v /var/run/docker.sock:/var/run/docker.sock'
                        }
                    }
                    steps {
                        script {
                            buildStandardDockerImage()
                        }
                    }
                }
                
                stage('多階段建置') {
                    when {
                        expression { params.BUILD_MODE == 'multi-stage' }
                    }
                    agent {
                        docker {
                            image 'docker:24'
                            args '-v /var/run/docker.sock:/var/run/docker.sock'
                        }
                    }
                    steps {
                        script {
                            buildMultiStageDockerImage()
                        }
                    }
                }
                
                stage('BuildKit 建置') {
                    when {
                        expression { params.BUILD_MODE == 'buildkit' }
                    }
                    agent {
                        docker {
                            image 'moby/buildkit:latest'
                            args '--privileged'
                        }
                    }
                    steps {
                        script {
                            buildWithBuildKit()
                        }
                    }
                }
                
                stage('Kaniko 建置') {
                    when {
                        expression { params.BUILD_MODE == 'kaniko' }
                    }
                    agent {
                        kubernetes {
                            yaml """
                                apiVersion: v1
                                kind: Pod
                                spec:
                                  containers:
                                  - name: kaniko
                                    image: gcr.io/kaniko-project/executor:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                    volumeMounts:
                                    - name: kaniko-secret
                                      mountPath: /kaniko/.docker
                                  volumes:
                                  - name: kaniko-secret
                                    secret:
                                      secretName: regcred
                            """
                        }
                    }
                    steps {
                        container('kaniko') {
                            script {
                                buildWithKaniko()
                            }
                        }
                    }
                }
            }
        }
        
        stage('容器安全掃描') {
            when {
                expression { params.ENABLE_SECURITY_SCAN == true }
            }
            parallel {
                stage('Trivy 漏洞掃描') {
                    agent {
                        docker {
                            image 'aquasec/trivy:latest'
                            args '--entrypoint="" -v trivy-cache:/root/.cache'
                        }
                    }
                    steps {
                        script {
                            runTrivySecurityScan()
                        }
                    }
                }
                
                stage('Snyk 安全掃描') {
                    agent {
                        docker {
                            image 'snyk/snyk:docker'
                            args '--entrypoint=""'
                        }
                    }
                    steps {
                        script {
                            runSnykSecurityScan()
                        }
                    }
                }
                
                stage('Hadolint Dockerfile 檢查') {
                    agent {
                        docker {
                            image 'hadolint/hadolint:latest'
                            args '--entrypoint=""'
                        }
                    }
                    steps {
                        script {
                            runHadolintDockerfileLint()
                        }
                    }
                }
                
                stage('容器合規檢查') {
                    agent {
                        docker {
                            image 'aquasec/kube-bench:latest'
                            args '--entrypoint=""'
                        }
                    }
                    steps {
                        script {
                            runContainerComplianceCheck()
                        }
                    }
                }
            }
        }
        
        stage('容器測試與驗證') {
            agent {
                docker {
                    image 'docker:24'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                script {
                    runContainerTests()
                    validateContainerHealth()
                    performanceTestContainer()
                    validateImageSize()
                }
            }
        }
        
        stage('容器註冊與發布') {
            agent {
                docker {
                    image 'docker:24'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                script {
                    pushToRegistry()
                    createImageManifest()
                    signContainerImage()
                    updateImageCatalog()
                }
            }
        }
        
        stage('Kubernetes 部署') {
            when {
                expression { params.DEPLOY_TO_K8S == true }
            }
            agent {
                kubernetes {
                    yaml """
                        apiVersion: v1
                        kind: Pod
                        spec:
                          serviceAccountName: jenkins-deployer
                          containers:
                          - name: kubectl
                            image: bitnami/kubectl:latest
                            command:
                            - sleep
                            args:
                            - 99d
                          - name: helm
                            image: alpine/helm:latest
                            command:
                            - sleep
                            args:
                            - 99d
                    """
                }
            }
            steps {
                container('kubectl') {
                    script {
                        deployToKubernetes()
                    }
                }
                container('helm') {
                    script {
                        deployWithHelm()
                    }
                }
            }
        }
    }
    
    post {
        always {
            node('docker') {
                script {
                    collectContainerMetrics()
                    generateContainerReport()
                    cleanupDockerResources()
                }
            }
        }
        
        success {
            script {
                notifyContainerDeploymentSuccess()
                updateContainerCatalog()
            }
        }
        
        failure {
            script {
                analyzeContainerFailure()
                notifyContainerDeploymentFailure()
            }
        }
    }
}

// === 容器化管理函式 ===

def setupDockerEnvironment() {
    echo "設定 Docker 環境..."
    
    sh '''
        # 檢查 Docker 版本
        docker --version
        docker-compose --version
        
        # 設定 Docker 配置
        mkdir -p ~/.docker
        
        # 啟用 Docker BuildKit
        export DOCKER_BUILDKIT=1
        export COMPOSE_DOCKER_CLI_BUILD=1
        
        # 檢查 Docker 守護程序狀態
        docker info
        
        # 清理舊的容器和映像
        docker system prune -f
        
        echo "✅ Docker 環境設定完成"
    '''
}

def authenticateRegistry() {
    echo "認證容器註冊表..."
    
    script {
        switch(params.REGISTRY_TYPE) {
            case 'docker-hub':
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
                break
                
            case 'harbor':
                withCredentials([usernamePassword(credentialsId: 'harbor-credentials', usernameVariable: 'HARBOR_USER', passwordVariable: 'HARBOR_PASS')]) {
                    sh 'echo $HARBOR_PASS | docker login harbor.company.com -u $HARBOR_USER --password-stdin'
                }
                break
                
            case 'ecr':
                sh '''
                    # AWS ECR 認證
                    aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | \\
                        docker login --username AWS --password-stdin ${DOCKER_REGISTRY}
                '''
                break
                
            case 'acr':
                withCredentials([usernamePassword(credentialsId: 'azure-sp-credentials', usernameVariable: 'AZURE_CLIENT_ID', passwordVariable: 'AZURE_CLIENT_SECRET')]) {
                    sh '''
                        # Azure ACR 認證
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant ${AZURE_TENANT_ID}
                        az acr login --name ${ACR_NAME}
                    '''
                }
                break
                
            case 'gcr':
                withCredentials([file(credentialsId: 'gcp-service-account-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        # Google Container Registry 認證
                        gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
                        gcloud auth configure-docker
                    '''
                }
                break
        }
    }
    
    echo "✅ 容器註冊表認證完成"
}

def analyzeDockerfile() {
    echo "分析 Dockerfile..."
    
    sh '''
        # 檢查 Dockerfile 存在
        if [ ! -f "Dockerfile" ]; then
            echo "錯誤: 找不到 Dockerfile"
            exit 1
        fi
        
        # 分析 Dockerfile 結構
        echo "=== Dockerfile 分析 ==="
        
        # 統計層數
        LAYERS=$(grep -c "^FROM\\|^RUN\\|^COPY\\|^ADD" Dockerfile)
        echo "映像層數: $LAYERS"
        
        # 檢查基礎映像
        BASE_IMAGE=$(grep "^FROM" Dockerfile | tail -1 | awk '{print $2}')
        echo "基礎映像: $BASE_IMAGE"
        
        # 檢查是否使用多階段建置
        STAGES=$(grep -c "^FROM" Dockerfile)
        if [ $STAGES -gt 1 ]; then
            echo "多階段建置: 是 ($STAGES 階段)"
        else
            echo "多階段建置: 否"
        fi
        
        # 檢查安全最佳實務
        echo "=== 安全檢查 ==="
        
        if grep -q "USER" Dockerfile; then
            echo "✅ 使用非 root 用戶"
        else
            echo "❌ 警告: 未指定非 root 用戶"
        fi
        
        if grep -q "HEALTHCHECK" Dockerfile; then
            echo "✅ 包含健康檢查"
        else
            echo "❌ 警告: 缺少健康檢查"
        fi
        
        echo "✅ Dockerfile 分析完成"
    '''
}

def buildMultiStageDockerImage() {
    echo "執行多階段 Docker 建置..."
    
    sh '''
        # 建立多階段 Dockerfile
        cat > Dockerfile.multistage << 'EOF'
# 第一階段：建置環境
FROM maven:3.9-eclipse-temurin-17 AS builder

# 設定工作目錄
WORKDIR /app

# 複製 pom.xml 文件先下載依賴（利用 Docker 層快取）
COPY pom.xml .
RUN mvn dependency:go-offline -B

# 複製原始碼並建置
COPY src ./src
RUN mvn clean package -DskipTests -B

# 第二階段：運行環境
FROM eclipse-temurin:17-jre-alpine AS runtime

# 建立非 root 用戶
RUN addgroup -g 1001 appgroup && \\
    adduser -D -u 1001 -G appgroup appuser

# 安裝運行時工具
RUN apk add --no-cache \\
    curl \\
    jq \\
    tzdata \\
    && rm -rf /var/cache/apk/*

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 設定工作目錄
WORKDIR /app

# 從建置階段複製 JAR 文件
COPY --from=builder /app/target/*.jar app.jar

# 設定檔案權限
RUN chown -R appuser:appgroup /app
USER appuser

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8080/actuator/health || exit 1

# 暴露埠號
EXPOSE 8080

# 設定 JVM 參數
ENV JAVA_OPTS="-Xmx512m -Xms256m -XX:+UseG1GC -XX:+UseContainerSupport"

# 啟動應用程式
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
EOF

        # 執行多階段建置
        docker build \\
            --file Dockerfile.multistage \\
            --tag ${DOCKER_REPO}:${DOCKER_TAG} \\
            --tag ${DOCKER_REPO}:latest \\
            --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \\
            --build-arg VCS_REF=${GIT_COMMIT} \\
            --build-arg VERSION=${BUILD_NUMBER} \\
            --target runtime \\
            .
        
        # 顯示建置結果
        docker images ${DOCKER_REPO}:${DOCKER_TAG}
        
        echo "✅ 多階段 Docker 建置完成"
    '''
}

def buildWithBuildKit() {
    echo "使用 BuildKit 進行建置..."
    
    sh '''
        # 啟用 BuildKit
        export DOCKER_BUILDKIT=1
        
        # 建立 BuildKit 建置器
        docker buildx create --name mybuilder --use
        docker buildx inspect --bootstrap
        
        # 執行多平台建置
        docker buildx build \\
            --platform linux/amd64,linux/arm64 \\
            --file Dockerfile.multistage \\
            --tag ${DOCKER_REPO}:${DOCKER_TAG} \\
            --tag ${DOCKER_REPO}:latest \\
            --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \\
            --build-arg VCS_REF=${GIT_COMMIT} \\
            --build-arg VERSION=${BUILD_NUMBER} \\
            --cache-from type=local,src=/tmp/.buildx-cache \\
            --cache-to type=local,dest=/tmp/.buildx-cache-new,mode=max \\
            --push \\
            .
        
        # 更新快取
        rm -rf /tmp/.buildx-cache
        mv /tmp/.buildx-cache-new /tmp/.buildx-cache
        
        echo "✅ BuildKit 建置完成"
    '''
}

def buildWithKaniko() {
    echo "使用 Kaniko 進行建置..."
    
    sh '''
        # 準備 Kaniko 配置
        mkdir -p /workspace
        cp -r . /workspace/
        
        # 執行 Kaniko 建置
        /kaniko/executor \\
            --dockerfile=/workspace/Dockerfile.multistage \\
            --context=/workspace \\
            --destination=${DOCKER_REPO}:${DOCKER_TAG} \\
            --destination=${DOCKER_REPO}:latest \\
            --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \\
            --build-arg VCS_REF=${GIT_COMMIT} \\
            --build-arg VERSION=${BUILD_NUMBER} \\
            --cache=true \\
            --cache-ttl=24h \\
            --compressed-caching=false
        
        echo "✅ Kaniko 建置完成"
    '''
}

def runTrivySecurityScan() {
    echo "執行 Trivy 安全掃描..."
    
    sh '''
        # 更新 Trivy 資料庫
        trivy image --download-db-only
        
        # 執行漏洞掃描
        trivy image \\
            --format table \\
            --exit-code 0 \\
            --severity HIGH,CRITICAL \\
            ${DOCKER_REPO}:${DOCKER_TAG}
        
        # 生成 JSON 報告
        trivy image \\
            --format json \\
            --output trivy-report.json \\
            ${DOCKER_REPO}:${DOCKER_TAG}
        
        # 檢查嚴重漏洞
        CRITICAL_COUNT=$(cat trivy-report.json | jq '[.Results[]?.Vulnerabilities[]? | select(.Severity=="CRITICAL")] | length')
        HIGH_COUNT=$(cat trivy-report.json | jq '[.Results[]?.Vulnerabilities[]? | select(.Severity=="HIGH")] | length')
        
        echo "嚴重漏洞: $CRITICAL_COUNT"
        echo "高危漏洞: $HIGH_COUNT"
        
        # 設定安全閾值
        if [ "$CRITICAL_COUNT" -gt 0 ]; then
            echo "❌ 發現嚴重安全漏洞，建置失敗"
            exit 1
        fi
        
        if [ "$HIGH_COUNT" -gt 5 ]; then
            echo "⚠️ 高危漏洞過多，需要處理"
        fi
        
        echo "✅ Trivy 安全掃描完成"
    '''
    
    publishHTML([
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '.',
        reportFiles: 'trivy-report.json',
        reportName: 'Trivy Security Report'
    ])
}

def runContainerTests() {
    echo "執行容器測試..."
    
    sh '''
        # 啟動測試容器
        docker run -d \\
            --name test-container-${BUILD_NUMBER} \\
            --health-cmd="curl -f http://localhost:8080/actuator/health || exit 1" \\
            --health-interval=10s \\
            --health-timeout=5s \\
            --health-retries=3 \\
            -p 8080:8080 \\
            ${DOCKER_REPO}:${DOCKER_TAG}
        
        # 等待容器啟動
        echo "等待容器啟動..."
        sleep 30
        
        # 檢查容器狀態
        CONTAINER_STATUS=$(docker inspect test-container-${BUILD_NUMBER} --format='{{.State.Health.Status}}')
        echo "容器健康狀態: $CONTAINER_STATUS"
        
        if [ "$CONTAINER_STATUS" != "healthy" ]; then
            echo "❌ 容器健康檢查失敗"
            docker logs test-container-${BUILD_NUMBER}
            exit 1
        fi
        
        # 執行功能測試
        echo "執行功能測試..."
        
        # 測試健康檢查端點
        curl -f http://localhost:8080/actuator/health
        
        # 測試應用程式端點
        curl -f http://localhost:8080/
        
        # 測試 API 端點
        curl -f http://localhost:8080/api/health
        
        echo "✅ 容器測試完成"
    '''
}

def validateImageSize() {
    echo "驗證映像大小..."
    
    sh '''
        # 取得映像資訊
        IMAGE_SIZE=$(docker images ${DOCKER_REPO}:${DOCKER_TAG} --format "table {{.Size}}" | tail -1)
        
        echo "映像大小: $IMAGE_SIZE"
        
        # 檢查映像層數
        LAYER_COUNT=$(docker history ${DOCKER_REPO}:${DOCKER_TAG} --no-trunc | wc -l)
        echo "映像層數: $LAYER_COUNT"
        
        # 分析映像組成
        docker history ${DOCKER_REPO}:${DOCKER_TAG} --no-trunc
        
        # 設定大小閾值（例如 500MB）
        SIZE_MB=$(docker images ${DOCKER_REPO}:${DOCKER_TAG} --format "table {{.Size}}" | tail -1 | sed 's/MB//' | sed 's/GB/*1000/' | bc 2>/dev/null || echo "0")
        
        if [ "$SIZE_MB" -gt 500 ]; then
            echo "⚠️ 警告: 映像大小超過 500MB"
        fi
        
        echo "✅ 映像大小驗證完成"
    '''
}

def pushToRegistry() {
    echo "推送映像到註冊表..."
    
    sh '''
        # 推送映像
        docker push ${DOCKER_REPO}:${DOCKER_TAG}
        docker push ${DOCKER_REPO}:latest
        
        # 建立映像標籤
        docker tag ${DOCKER_REPO}:${DOCKER_TAG} ${DOCKER_REPO}:build-${BUILD_NUMBER}
        docker push ${DOCKER_REPO}:build-${BUILD_NUMBER}
        
        # 如果是主分支，建立 stable 標籤
        if [ "${GIT_BRANCH}" = "origin/main" ] || [ "${GIT_BRANCH}" = "origin/master" ]; then
            docker tag ${DOCKER_REPO}:${DOCKER_TAG} ${DOCKER_REPO}:stable
            docker push ${DOCKER_REPO}:stable
        fi
        
        echo "✅ 映像推送完成"
    '''
}

def signContainerImage() {
    echo "簽署容器映像..."
    
    sh '''
        # 使用 Cosign 簽署映像
        if command -v cosign &> /dev/null; then
            echo "使用 Cosign 簽署映像..."
            
            # 生成金鑰對（如果不存在）
            if [ ! -f cosign.key ]; then
                cosign generate-key-pair
            fi
            
            # 簽署映像
            cosign sign --key cosign.key ${DOCKER_REPO}:${DOCKER_TAG}
            
            # 驗證簽章
            cosign verify --key cosign.pub ${DOCKER_REPO}:${DOCKER_TAG}
            
            echo "✅ 映像簽署完成"
        else
            echo "⚠️ Cosign 未安裝，跳過映像簽署"
        fi
    '''
}
```

#### 17.2 Kubernetes 原生 CI/CD

**Kubernetes 整合架構：**

```yaml
# Kubernetes Jenkins 部署配置
apiVersion: v1
kind: Namespace
metadata:
  name: jenkins-system
  labels:
    name: jenkins-system
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins-master
  namespace: jenkins-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins-master
  template:
    metadata:
      labels:
        app: jenkins-master
    spec:
      serviceAccountName: jenkins
      securityContext:
        runAsUser: 1000
        runAsGroup: 1000
        fsGroup: 1000
      containers:
      - name: jenkins
        image: jenkins/jenkins:lts-jdk17
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 50000
          name: agent
        env:
        - name: JENKINS_OPTS
          value: "--httpPort=8080"
        - name: JAVA_OPTS
          value: "-Xmx2048m -Dhudson.slaves.NodeProvisioner.initialDelay=0 -Dhudson.slaves.NodeProvisioner.MARGIN=50 -Dhudson.slaves.NodeProvisioner.MARGIN0=0.85"
        volumeMounts:
        - name: jenkins-home
          mountPath: /var/jenkins_home
        - name: docker-sock
          mountPath: /var/run/docker.sock
        livenessProbe:
          httpGet:
            path: /login
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /login
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 5
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
      volumes:
      - name: jenkins-home
        persistentVolumeClaim:
          claimName: jenkins-pvc
      - name: docker-sock
        hostPath:
          path: /var/run/docker.sock
---
apiVersion: v1
kind: Service
metadata:
  name: jenkins-service
  namespace: jenkins-system
spec:
  type: LoadBalancer
  ports:
  - name: http
    port: 80
    targetPort: 8080
  - name: agent
    port: 50000
    targetPort: 50000
  selector:
    app: jenkins-master
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jenkins-pvc
  namespace: jenkins-system
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: fast-ssd
```

**Kubernetes 原生 CI/CD Pipeline：**

```groovy
// Kubernetes 原生 CI/CD Pipeline
pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  serviceAccountName: jenkins-agent
                  containers:
                  - name: maven
                    image: maven:3.9-eclipse-temurin-17
                    command:
                    - sleep
                    args:
                    - 99d
                    volumeMounts:
                    - name: maven-cache
                      mountPath: /root/.m2
                  - name: docker
                    image: docker:24-dind
                    securityContext:
                      privileged: true
                    volumeMounts:
                    - name: docker-sock
                      mountPath: /var/run
                  - name: kubectl
                    image: bitnami/kubectl:latest
                    command:
                    - sleep
                    args:
                    - 99d
                  - name: helm
                    image: alpine/helm:latest
                    command:
                    - sleep
                    args:
                    - 99d
                  volumes:
                  - name: maven-cache
                    persistentVolumeClaim:
                      claimName: maven-cache-pvc
                  - name: docker-sock
                    emptyDir: {}
            '''
        }
    }
    
    environment {
        APP_NAME = 'java-tutorial'
        K8S_NAMESPACE = 'java-tutorial'
        HELM_CHART = './k8s/helm-chart'
        DOCKER_REGISTRY = 'harbor.company.com'
        DOCKER_REPO = "${DOCKER_REGISTRY}/library/${APP_NAME}"
        IMAGE_TAG = "${BUILD_NUMBER}-${GIT_COMMIT.take(8)}"
    }
    
    stages {
        stage('原始碼建置') {
            steps {
                container('maven') {
                    sh '''
                        mvn clean compile test package -DskipTests=false
                        mvn sonar:sonar
                    '''
                }
            }
        }
        
        stage('容器建置') {
            steps {
                container('docker') {
                    sh '''
                        # 建置應用程式映像
                        docker build -t ${DOCKER_REPO}:${IMAGE_TAG} .
                        docker push ${DOCKER_REPO}:${IMAGE_TAG}
                    '''
                }
            }
        }
        
        stage('Kubernetes 部署') {
            steps {
                container('helm') {
                    sh '''
                        # 更新 Helm 依賴
                        helm dependency update ${HELM_CHART}
                        
                        # 部署到 Kubernetes
                        helm upgrade --install ${APP_NAME} ${HELM_CHART} \\
                            --namespace ${K8S_NAMESPACE} \\
                            --create-namespace \\
                            --set image.repository=${DOCKER_REPO} \\
                            --set image.tag=${IMAGE_TAG} \\
                            --set environment=production \\
                            --wait --timeout=300s
                    '''
                }
            }
        }
        
        stage('部署驗證') {
            steps {
                container('kubectl') {
                    sh '''
                        # 檢查部署狀態
                        kubectl rollout status deployment/${APP_NAME} -n ${K8S_NAMESPACE}
                        
                        # 檢查 Pod 狀態
                        kubectl get pods -n ${K8S_NAMESPACE} -l app=${APP_NAME}
                        
                        # 執行健康檢查
                        kubectl run health-check --rm -i --restart=Never \\
                            --image=curlimages/curl -- \\
                            curl -f http://${APP_NAME}.${K8S_NAMESPACE}.svc.cluster.local:8080/actuator/health
                    '''
                }
            }
        }
    }
    
    post {
        always {
            container('kubectl') {
                sh '''
                    # 收集部署資訊
                    kubectl describe deployment ${APP_NAME} -n ${K8S_NAMESPACE} > deployment-info.txt
                    kubectl get events -n ${K8S_NAMESPACE} --sort-by=.metadata.creationTimestamp > events.txt
                '''
                archiveArtifacts artifacts: '*.txt'
            }
        }
    }
}
```

#### 17.3 多雲環境整合

**多雲部署策略：**

```groovy
// 多雲環境整合 Pipeline
pipeline {
    agent none
    
    parameters {
        choice(
            name: 'TARGET_CLOUDS',
            choices: ['aws-only', 'azure-only', 'gcp-only', 'multi-cloud', 'all-clouds'],
            description: '目標雲端環境'
        )
        choice(
            name: 'DEPLOYMENT_STRATEGY',
            choices: ['blue-green', 'canary', 'rolling', 'recreate'],
            description: '部署策略'
        )
        booleanParam(
            name: 'ENABLE_DISASTER_RECOVERY',
            defaultValue: true,
            description: '啟用災難恢復'
        )
    }
    
    environment {
        // AWS 配置
        AWS_REGION = 'ap-northeast-1'
        AWS_EKS_CLUSTER = 'production-eks-cluster'
        AWS_ECR_REGISTRY = '123456789012.dkr.ecr.ap-northeast-1.amazonaws.com'
        
        // Azure 配置
        AZURE_LOCATION = 'East Asia'
        AZURE_AKS_CLUSTER = 'production-aks-cluster'
        AZURE_ACR_REGISTRY = 'productionacr.azurecr.io'
        
        // GCP 配置
        GCP_ZONE = 'asia-east1-a'
        GCP_GKE_CLUSTER = 'production-gke-cluster'
        GCP_GCR_REGISTRY = 'gcr.io/company-project'
        
        // 應用程式配置
        APP_NAME = 'java-tutorial'
        APP_VERSION = "${BUILD_NUMBER}"
        NAMESPACE = 'production'
    }
    
    stages {
        stage('多雲環境準備') {
            parallel {
                stage('AWS 環境準備') {
                    when {
                        expression { 
                            params.TARGET_CLOUDS.contains('aws') || 
                            params.TARGET_CLOUDS == 'all-clouds' 
                        }
                    }
                    agent {
                        docker {
                            image 'amazon/aws-cli:latest'
                            args '--entrypoint=""'
                        }
                    }
                    steps {
                        script {
                            setupAWSEnvironment()
                        }
                    }
                }
                
                stage('Azure 環境準備') {
                    when {
                        expression { 
                            params.TARGET_CLOUDS.contains('azure') || 
                            params.TARGET_CLOUDS == 'all-clouds' 
                        }
                    }
                    agent {
                        docker {
                            image 'mcr.microsoft.com/azure-cli:latest'
                            args '--entrypoint=""'
                        }
                    }
                    steps {
                        script {
                            setupAzureEnvironment()
                        }
                    }
                }
                
                stage('GCP 環境準備') {
                    when {
                        expression { 
                            params.TARGET_CLOUDS.contains('gcp') || 
                            params.TARGET_CLOUDS == 'all-clouds' 
                        }
                    }
                    agent {
                        docker {
                            image 'google/cloud-sdk:alpine'
                            args '--entrypoint=""'
                        }
                    }
                    steps {
                        script {
                            setupGCPEnvironment()
                        }
                    }
                }
            }
        }
        
        stage('多雲容器建置與推送') {
            parallel {
                stage('AWS ECR 推送') {
                    when {
                        expression { shouldDeployToAWS() }
                    }
                    agent {
                        docker {
                            image 'amazon/aws-cli:latest'
                            args '--entrypoint="" -v /var/run/docker.sock:/var/run/docker.sock'
                        }
                    }
                    steps {
                        script {
                            buildAndPushToECR()
                        }
                    }
                }
                
                stage('Azure ACR 推送') {
                    when {
                        expression { shouldDeployToAzure() }
                    }
                    agent {
                        docker {
                            image 'mcr.microsoft.com/azure-cli:latest'
                            args '--entrypoint="" -v /var/run/docker.sock:/var/run/docker.sock'
                        }
                    }
                    steps {
                        script {
                            buildAndPushToACR()
                        }
                    }
                }
                
                stage('GCP GCR 推送') {
                    when {
                        expression { shouldDeployToGCP() }
                    }
                    agent {
                        docker {
                            image 'google/cloud-sdk:alpine'
                            args '--entrypoint="" -v /var/run/docker.sock:/var/run/docker.sock'
                        }
                    }
                    steps {
                        script {
                            buildAndPushToGCR()
                        }
                    }
                }
            }
        }
        
        stage('多雲部署執行') {
            parallel {
                stage('AWS EKS 部署') {
                    when {
                        expression { shouldDeployToAWS() }
                    }
                    agent {
                        kubernetes {
                            yaml """
                                apiVersion: v1
                                kind: Pod
                                spec:
                                  containers:
                                  - name: aws-cli
                                    image: amazon/aws-cli:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                  - name: kubectl
                                    image: bitnami/kubectl:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                  - name: helm
                                    image: alpine/helm:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                            """
                        }
                    }
                    steps {
                        container('aws-cli') {
                            script {
                                configureAWSCredentials()
                            }
                        }
                        container('kubectl') {
                            script {
                                deployToEKS()
                            }
                        }
                        container('helm') {
                            script {
                                deployAWSHelmChart()
                            }
                        }
                    }
                }
                
                stage('Azure AKS 部署') {
                    when {
                        expression { shouldDeployToAzure() }
                    }
                    agent {
                        kubernetes {
                            yaml """
                                apiVersion: v1
                                kind: Pod
                                spec:
                                  containers:
                                  - name: azure-cli
                                    image: mcr.microsoft.com/azure-cli:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                  - name: kubectl
                                    image: bitnami/kubectl:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                  - name: helm
                                    image: alpine/helm:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                            """
                        }
                    }
                    steps {
                        container('azure-cli') {
                            script {
                                configureAzureCredentials()
                            }
                        }
                        container('kubectl') {
                            script {
                                deployToAKS()
                            }
                        }
                        container('helm') {
                            script {
                                deployAzureHelmChart()
                            }
                        }
                    }
                }
                
                stage('GCP GKE 部署') {
                    when {
                        expression { shouldDeployToGCP() }
                    }
                    agent {
                        kubernetes {
                            yaml """
                                apiVersion: v1
                                kind: Pod
                                spec:
                                  containers:
                                  - name: gcloud
                                    image: google/cloud-sdk:alpine
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                  - name: kubectl
                                    image: bitnami/kubectl:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                                  - name: helm
                                    image: alpine/helm:latest
                                    command:
                                    - sleep
                                    args:
                                    - 99d
                            """
                        }
                    }
                    steps {
                        container('gcloud') {
                            script {
                                configureGCPCredentials()
                            }
                        }
                        container('kubectl') {
                            script {
                                deployToGKE()
                            }
                        }
                        container('helm') {
                            script {
                                deployGCPHelmChart()
                            }
                        }
                    }
                }
            }
        }
        
        stage('多雲部署驗證') {
            parallel {
                stage('AWS 驗證') {
                    when {
                        expression { shouldDeployToAWS() }
                    }
                    steps {
                        script {
                            validateAWSDeployment()
                        }
                    }
                }
                
                stage('Azure 驗證') {
                    when {
                        expression { shouldDeployToAzure() }
                    }
                    steps {
                        script {
                            validateAzureDeployment()
                        }
                    }
                }
                
                stage('GCP 驗證') {
                    when {
                        expression { shouldDeployToGCP() }
                    }
                    steps {
                        script {
                            validateGCPDeployment()
                        }
                    }
                }
            }
        }
        
        stage('災難恢復配置') {
            when {
                expression { params.ENABLE_DISASTER_RECOVERY == true }
            }
            steps {
                script {
                    setupDisasterRecovery()
                    testFailoverMechanisms()
                    validateBackupStrategies()
                }
            }
        }
    }
    
    post {
        always {
            script {
                collectMultiCloudMetrics()
                generateMultiCloudReport()
            }
        }
        
        success {
            script {
                notifyMultiCloudSuccess()
                updateServiceMesh()
            }
        }
        
        failure {
            script {
                rollbackMultiCloudDeployment()
                notifyMultiCloudFailure()
            }
        }
    }
}

// === 多雲管理函式 ===

def setupAWSEnvironment() {
    echo "設定 AWS 環境..."
    
    sh '''
        # 安裝必要工具
        yum update -y
        yum install -y jq curl
        
        # 配置 AWS CLI
        aws configure set default.region ${AWS_REGION}
        
        # 檢查 AWS 認證
        aws sts get-caller-identity
        
        # 檢查 EKS 集群
        aws eks describe-cluster --name ${AWS_EKS_CLUSTER} --region ${AWS_REGION}
        
        # 更新 kubeconfig
        aws eks update-kubeconfig --name ${AWS_EKS_CLUSTER} --region ${AWS_REGION}
        
        echo "✅ AWS 環境設定完成"
    '''
}

def buildAndPushToECR() {
    echo "建置並推送到 AWS ECR..."
    
    sh '''
        # ECR 登入
        aws ecr get-login-password --region ${AWS_REGION} | \\
            docker login --username AWS --password-stdin ${AWS_ECR_REGISTRY}
        
        # 建置映像
        docker build -t ${AWS_ECR_REGISTRY}/${APP_NAME}:${APP_VERSION} .
        docker tag ${AWS_ECR_REGISTRY}/${APP_NAME}:${APP_VERSION} ${AWS_ECR_REGISTRY}/${APP_NAME}:latest
        
        # 推送映像
        docker push ${AWS_ECR_REGISTRY}/${APP_NAME}:${APP_VERSION}
        docker push ${AWS_ECR_REGISTRY}/${APP_NAME}:latest
        
        echo "✅ ECR 推送完成"
    '''
}

def deployToEKS() {
    echo "部署到 AWS EKS..."
    
    sh '''
        # 更新 kubeconfig
        aws eks update-kubeconfig --name ${AWS_EKS_CLUSTER} --region ${AWS_REGION}
        
        # 檢查集群連接
        kubectl cluster-info
        
        # 建立命名空間（如果不存在）
        kubectl create namespace ${NAMESPACE} --dry-run=client -o yaml | kubectl apply -f -
        
        # 部署應用程式
        kubectl set image deployment/${APP_NAME} \\
            ${APP_NAME}=${AWS_ECR_REGISTRY}/${APP_NAME}:${APP_VERSION} \\
            --namespace=${NAMESPACE}
        
        # 等待部署完成
        kubectl rollout status deployment/${APP_NAME} --namespace=${NAMESPACE} --timeout=300s
        
        echo "✅ EKS 部署完成"
    '''
}

def setupDisasterRecovery() {
    echo "設定災難恢復..."
    
    sh '''
        # 建立跨雲備份策略
        echo "建立災難恢復配置..."
        
        # AWS 備份配置
        if [ "${TARGET_CLOUDS}" = "multi-cloud" ] || [ "${TARGET_CLOUDS}" = "all-clouds" ]; then
            # 配置 AWS Backup
            aws backup create-backup-plan \\
                --backup-plan '{
                    "BackupPlanName": "MultiCloudBackupPlan",
                    "Rules": [{
                        "RuleName": "DailyBackups",
                        "TargetBackupVault": "default",
                        "ScheduleExpression": "cron(0 2 * * ? *)",
                        "Lifecycle": {
                            "DeleteAfterDays": 30
                        }
                    }]
                }' || true
            
            # Azure 備份配置
            az backup policy create \\
                --resource-group backup-rg \\
                --vault-name backup-vault \\
                --name MultiCloudBackupPolicy \\
                --policy disaster-recovery-policy.json || true
            
            # GCP 備份配置
            gcloud compute snapshots create multi-cloud-snapshot \\
                --source-disk=production-disk \\
                --zone=${GCP_ZONE} || true
        fi
        
        echo "✅ 災難恢復配置完成"
    '''
}
```

### 容器化最佳實務

#### 實務案例：微服務容器化

**微服務 Dockerfile 範例：**

```dockerfile
# 微服務最佳實務 Dockerfile
# 階段1：建置階段
FROM maven:3.9-eclipse-temurin-17-alpine AS builder

# 設定建置參數
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# 建立應用程式目錄
WORKDIR /app

# 複製依賴文件（利用 Docker 層快取）
COPY pom.xml ./
COPY .mvn .mvn/
COPY mvnw ./

# 下載依賴
RUN mvn dependency:go-offline -B

# 複製原始碼
COPY src src/

# 執行建置
RUN mvn clean package -DskipTests -B && \
    mkdir -p target/dependency && \
    cd target/dependency && \
    jar -xf ../*.jar

# 階段2：運行時階段
FROM eclipse-temurin:17-jre-alpine AS runtime

# 安裝必要的運行時工具
RUN apk add --no-cache \
    curl \
    jq \
    tzdata \
    tini \
    && rm -rf /var/cache/apk/*

# 建立非特權用戶
RUN addgroup -g 1001 appgroup && \
    adduser -D -u 1001 -G appgroup -h /app appuser

# 設定時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 設定工作目錄
WORKDIR /app

# 複製應用程式依賴
COPY --from=builder /app/target/dependency/BOOT-INF/lib lib/
COPY --from=builder /app/target/dependency/META-INF META-INF/
COPY --from=builder /app/target/dependency/BOOT-INF/classes .

# 設定檔案權限
RUN chown -R appuser:appgroup /app

# 切換到非特權用戶
USER appuser

# 健康檢查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/actuator/health || exit 1

# 暴露埠號
EXPOSE 8080

# 設定標籤
LABEL maintainer="DevOps Team <devops@company.com>" \
      org.opencontainers.image.title="Java Tutorial Microservice" \
      org.opencontainers.image.description="Spring Boot microservice for Java tutorial" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.vendor="Company Name" \
      org.opencontainers.image.licenses="MIT"

# 設定 JVM 參數
ENV JAVA_OPTS="-XX:+UseContainerSupport -XX:+UseG1GC -XX:MaxRAMPercentage=75.0"

# 使用 tini 作為 init 程序
ENTRYPOINT ["/sbin/tini", "--"]

# 啟動命令
CMD ["sh", "-c", "java $JAVA_OPTS -cp .:lib/* com.tutorial.Application"]
```

### 關鍵注意事項

1. **容器安全**：
   - 使用官方基礎映像
   - 定期更新容器映像
   - 實施安全掃描
   - 避免特權容器

2. **效能最佳化**：
   - 多階段建置減少映像大小
   - 適當的資源限制
   - 健康檢查配置
   - 快取策略最佳化

3. **可觀測性**：
   - 結構化日誌輸出
   - 指標收集端點
   - 分散式追蹤
   - 健康狀態監控

4. **生產就緒**：
   - 適當的重啟策略
   - 資源配額管理
   - 網路安全策略
   - 備份與恢復計畫

### 認證知識對應

| 認證項目 | 對應內容 |
|----------|----------|
| 容器技術 | Docker、BuildKit、Kaniko |
| 編排平台 | Kubernetes、Helm |
| 雲端整合 | AWS、Azure、GCP |
| 安全性 | 漏洞掃描、映像簽署 |

### 實務練習 - 第17章

1. **基礎練習**：建立簡單的容器化 CI/CD Pipeline
2. **進階練習**：實作 Kubernetes 原生部署流程
3. **實務練習**：設計完整的多雲容器化架構

---

## 第18章 DevOps 文化與實務

### 文化轉型願景

- 理解 DevOps 的核心理念和價值觀
- 建立高效能團隊協作模式
- 實現持續改進的組織文化
- 推動數位轉型與創新實踐

### DevOps 文化基石

#### 18.1 DevOps 理念與原則

DevOps 不僅是技術實踐，更是文化革命，需要組織、流程和人員的全面轉型。

```mermaid
graph TB
    subgraph "DevOps 核心價值"
        CV1[協作<br/>Collaboration]
        CV2[溝通<br/>Communication]
        CV3[整合<br/>Integration]
        CV4[自動化<br/>Automation]
        CV5[監控<br/>Monitoring]
        CV6[共享<br/>Sharing]
    end
    
    subgraph "組織轉型"
        OT1[打破孤島<br/>Break Silos]
        OT2[跨功能團隊<br/>Cross-functional Teams]
        OT3[共享責任<br/>Shared Responsibility]
        OT4[快速反饋<br/>Fast Feedback]
    end
    
    subgraph "技術實踐"
        TP1[持續整合<br/>Continuous Integration]
        TP2[持續部署<br/>Continuous Deployment]
        TP3[基礎設施即程式碼<br/>Infrastructure as Code]
        TP4[監控與日誌<br/>Monitoring & Logging]
    end
    
    subgraph "業務成果"
        BO1[更快交付<br/>Faster Delivery]
        BO2[更高品質<br/>Higher Quality]
        BO3[更佳穩定性<br/>Better Stability]
        BO4[更強創新<br/>Enhanced Innovation]
    end
    
    CV1 --> OT1
    CV2 --> OT2
    CV3 --> OT3
    CV4 --> TP1
    CV5 --> TP4
    CV6 --> OT4
    
    OT1 --> TP1
    OT2 --> TP2
    OT3 --> TP3
    OT4 --> TP4
    
    TP1 --> BO1
    TP2 --> BO1
    TP3 --> BO2
    TP4 --> BO3
    
    BO1 --> BO4
    BO2 --> BO4
    BO3 --> BO4
    
    style CV1 fill:#e1f5fe
    style TP1 fill:#e8f5e8
    style BO1 fill:#fff3e0
```

**DevOps 成熟度評估 Pipeline：**

```groovy
// DevOps 成熟度評估與改進 Pipeline
pipeline {
    agent { label 'assessment-node' }
    
    parameters {
        choice(
            name: 'ASSESSMENT_SCOPE',
            choices: ['team', 'department', 'organization', 'full-stack'],
            description: '評估範圍'
        )
        choice(
            name: 'ASSESSMENT_TYPE',
            choices: ['culture', 'process', 'technology', 'comprehensive'],
            description: '評估類型'
        )
        booleanParam(
            name: 'GENERATE_IMPROVEMENT_PLAN',
            defaultValue: true,
            description: '生成改進計畫'
        )
    }
    
    environment {
        // 評估配置
        ASSESSMENT_FRAMEWORK = 'DORA'  // DevOps Research and Assessment
        MATURITY_LEVELS = '5'  // 成熟度等級數
        REPORT_FORMAT = 'comprehensive'
        
        // 指標配置
        LEAD_TIME_TARGET = '24h'        // 交付週期目標
        DEPLOYMENT_FREQ_TARGET = '10'   // 每日部署次數目標
        MTTR_TARGET = '1h'             // 平均恢復時間目標
        CHANGE_FAIL_RATE_TARGET = '5%' // 變更失敗率目標
        
        // 團隊配置
        TEAM_SIZE_MIN = '5'
        TEAM_SIZE_MAX = '9'
        CROSS_FUNCTIONAL_RATIO = '80%'
        
        // 工具評估
        TOOL_CATEGORIES = 'scm,ci,cd,monitoring,collaboration,security'
    }
    
    stages {
        stage('評估初始化') {
            steps {
                script {
                    initializeAssessment()
                    loadAssessmentFramework()
                    prepareAssessmentTools()
                }
            }
        }
        
        stage('文化成熟度評估') {
            when {
                expression { 
                    params.ASSESSMENT_TYPE == 'culture' || 
                    params.ASSESSMENT_TYPE == 'comprehensive' 
                }
            }
            parallel {
                stage('協作文化評估') {
                    steps {
                        script {
                            assessCollaborationCulture()
                        }
                    }
                }
                
                stage('學習文化評估') {
                    steps {
                        script {
                            assessLearningCulture()
                        }
                    }
                }
                
                stage('創新文化評估') {
                    steps {
                        script {
                            assessInnovationCulture()
                        }
                    }
                }
                
                stage('透明度文化評估') {
                    steps {
                        script {
                            assessTransparencyCulture()
                        }
                    }
                }
            }
        }
        
        stage('流程成熟度評估') {
            when {
                expression { 
                    params.ASSESSMENT_TYPE == 'process' || 
                    params.ASSESSMENT_TYPE == 'comprehensive' 
                }
            }
            parallel {
                stage('開發流程評估') {
                    steps {
                        script {
                            assessDevelopmentProcess()
                        }
                    }
                }
                
                stage('部署流程評估') {
                    steps {
                        script {
                            assessDeploymentProcess()
                        }
                    }
                }
                
                stage('監控流程評估') {
                    steps {
                        script {
                            assessMonitoringProcess()
                        }
                    }
                }
                
                stage('回饋流程評估') {
                    steps {
                        script {
                            assessFeedbackProcess()
                        }
                    }
                }
            }
        }
        
        stage('技術成熟度評估') {
            when {
                expression { 
                    params.ASSESSMENT_TYPE == 'technology' || 
                    params.ASSESSMENT_TYPE == 'comprehensive' 
                }
            }
            parallel {
                stage('自動化程度評估') {
                    steps {
                        script {
                            assessAutomationLevel()
                        }
                    }
                }
                
                stage('工具鏈評估') {
                    steps {
                        script {
                            assessToolchain()
                        }
                    }
                }
                
                stage('基礎設施評估') {
                    steps {
                        script {
                            assessInfrastructure()
                        }
                    }
                }
                
                stage('安全實踐評估') {
                    steps {
                        script {
                            assessSecurityPractices()
                        }
                    }
                }
            }
        }
        
        stage('DORA 指標測量') {
            steps {
                script {
                    measureLeadTime()
                    measureDeploymentFrequency()
                    measureMTTR()
                    measureChangeFailureRate()
                    calculateDORAScore()
                }
            }
        }
        
        stage('成熟度分析') {
            steps {
                script {
                    analyzeMaturityLevel()
                    identifyStrengthsAndGaps()
                    benchmarkIndustryStandards()
                    prioritizeImprovementAreas()
                }
            }
        }
        
        stage('改進計畫生成') {
            when {
                expression { params.GENERATE_IMPROVEMENT_PLAN == true }
            }
            steps {
                script {
                    generateImprovementRoadmap()
                    createActionItems()
                    defineSuccessMetrics()
                    estimateResourceRequirements()
                }
            }
        }
    }
    
    post {
        always {
            script {
                generateAssessmentReport()
                publishResults()
                scheduleFollowUp()
            }
        }
        
        success {
            script {
                notifyStakeholders()
                updateMaturityDatabase()
            }
        }
    }
}

// === DevOps 評估函式 ===

def initializeAssessment() {
    echo "初始化 DevOps 成熟度評估..."
    
    sh '''
        # 建立評估工作區
        mkdir -p assessment/{culture,process,technology,metrics,reports}
        
        # 載入評估問卷
        cat > assessment/culture-questionnaire.yaml << 'EOF'
culture_assessment:
  collaboration:
    - question: "團隊成員之間是否有定期的跨職能協作會議？"
      weight: 10
      scale: 1-5
    - question: "是否存在明確的溝通渠道和協作工具？"
      weight: 8
      scale: 1-5
    - question: "團隊成員是否願意分享知識和最佳實踐？"
      weight: 9
      scale: 1-5
      
  learning:
    - question: "組織是否鼓勵實驗和從失敗中學習？"
      weight: 10
      scale: 1-5
    - question: "是否有正式的學習和培訓計畫？"
      weight: 7
      scale: 1-5
    - question: "團隊成員是否有時間進行技能提升？"
      weight: 8
      scale: 1-5
      
  innovation:
    - question: "是否鼓勵團隊成員提出改進建議？"
      weight: 9
      scale: 1-5
    - question: "是否有創新時間或黑客松活動？"
      weight: 6
      scale: 1-5
    - question: "新想法是否能快速測試和驗證？"
      weight: 8
      scale: 1-5
      
  transparency:
    - question: "工作進展和問題是否對所有團隊成員可見？"
      weight: 9
      scale: 1-5
    - question: "決策過程是否透明和包容？"
      weight: 8
      scale: 1-5
    - question: "是否有定期的回顧和反思會議？"
      weight: 7
      scale: 1-5
EOF

        echo "✅ DevOps 評估初始化完成"
    '''
}

def assessCollaborationCulture() {
    echo "評估協作文化..."
    
    sh '''
        # 收集協作指標
        echo "收集協作文化指標..."
        
        # 會議頻率分析
        WEEKLY_MEETINGS=$(grep -c "meeting" calendar.log 2>/dev/null || echo "0")
        echo "每週會議次數: $WEEKLY_MEETINGS"
        
        # 跨團隊溝通分析
        CROSS_TEAM_MESSAGES=$(grep -c "cross-team" communication.log 2>/dev/null || echo "0")
        echo "跨團隊溝通: $CROSS_TEAM_MESSAGES"
        
        # 知識分享分析
        KNOWLEDGE_SHARES=$(grep -c "knowledge-share" activity.log 2>/dev/null || echo "0")
        echo "知識分享次數: $KNOWLEDGE_SHARES"
        
        # 計算協作得分
        python3 << 'EOF'
import json

# 協作文化指標權重
weights = {
    'meeting_frequency': 0.3,
    'cross_team_communication': 0.4,
    'knowledge_sharing': 0.3
}

# 收集指標值（模擬）
metrics = {
    'meeting_frequency': min(5, max(1, 3.5)),  # 基於會議頻率
    'cross_team_communication': min(5, max(1, 4.0)),  # 基於溝通品質
    'knowledge_sharing': min(5, max(1, 3.8))   # 基於分享活動
}

# 計算加權得分
collaboration_score = sum(metrics[key] * weights[key] for key in metrics)

# 儲存結果
result = {
    'category': 'collaboration_culture',
    'score': round(collaboration_score, 2),
    'level': 'Developing' if collaboration_score < 3 else 'Performing' if collaboration_score < 4 else 'Optimizing',
    'metrics': metrics,
    'recommendations': []
}

if collaboration_score < 3:
    result['recommendations'].extend([
        '建立定期的跨職能協作會議',
        '引入協作工具和實踐',
        '制定知識分享激勵機制'
    ])
elif collaboration_score < 4:
    result['recommendations'].extend([
        '優化現有協作流程',
        '擴大跨團隊合作範圍',
        '建立最佳實踐分享平台'
    ])

with open('assessment/culture/collaboration.json', 'w') as f:
    json.dump(result, f, indent=2)

print(f"協作文化得分: {collaboration_score:.2f}")
print(f"成熟度等級: {result['level']}")
EOF

        echo "✅ 協作文化評估完成"
    '''
}

def assessDevelopmentProcess() {
    echo "評估開發流程..."
    
    sh '''
        # 分析開發流程指標
        echo "分析開發流程成熟度..."
        
        # 版本控制使用情況
        if [ -d ".git" ]; then
            BRANCH_COUNT=$(git branch -r | wc -l)
            COMMIT_FREQUENCY=$(git log --since="1 week ago" --oneline | wc -l)
            echo "分支數量: $BRANCH_COUNT"
            echo "週提交次數: $COMMIT_FREQUENCY"
        fi
        
        # 程式碼審查覆蓋率
        PR_COUNT=$(find .git -name "*pull*" -type f 2>/dev/null | wc -l || echo "0")
        echo "Pull Request 數量: $PR_COUNT"
        
        # 自動化測試覆蓋率
        if [ -f "target/site/jacoco/index.html" ]; then
            COVERAGE=$(grep -o "Total.*[0-9]\+%" target/site/jacoco/index.html | tail -1 | grep -o "[0-9]\+%" || echo "0%")
            echo "測試覆蓋率: $COVERAGE"
        fi
        
        # 建置頻率
        if [ -f "Jenkinsfile" ]; then
            BUILD_TRIGGERS=$(grep -c "triggers" Jenkinsfile || echo "0")
            echo "建置觸發器: $BUILD_TRIGGERS"
        fi
        
        # 計算開發流程成熟度
        python3 << 'EOF'
import json
import os

def assess_development_process():
    # 收集指標
    metrics = {
        'version_control_usage': 5,  # Git 使用完整性
        'code_review_coverage': 4,   # 程式碼審查覆蓋率
        'automated_testing': 4,      # 自動化測試程度
        'build_automation': 5,       # 建置自動化程度
        'documentation': 3           # 文件化程度
    }
    
    # 權重配置
    weights = {
        'version_control_usage': 0.2,
        'code_review_coverage': 0.25,
        'automated_testing': 0.25,
        'build_automation': 0.2,
        'documentation': 0.1
    }
    
    # 計算總分
    total_score = sum(metrics[key] * weights[key] for key in metrics)
    
    # 判定成熟度等級
    if total_score >= 4.5:
        level = "Optimizing"
        description = "開發流程高度成熟，具備完整的自動化和最佳實踐"
    elif total_score >= 3.5:
        level = "Performing"
        description = "開發流程良好，部分領域仍有改進空間"
    elif total_score >= 2.5:
        level = "Developing"
        description = "開發流程基本建立，需要加強自動化和標準化"
    else:
        level = "Initial"
        description = "開發流程不夠成熟，需要全面改進"
    
    # 生成建議
    recommendations = []
    if metrics['code_review_coverage'] < 4:
        recommendations.append("提高程式碼審查覆蓋率，建立強制審查政策")
    if metrics['automated_testing'] < 4:
        recommendations.append("增加自動化測試，提高測試覆蓋率")
    if metrics['documentation'] < 4:
        recommendations.append("改善文件化，建立標準文件模板")
    
    result = {
        'category': 'development_process',
        'score': round(total_score, 2),
        'level': level,
        'description': description,
        'metrics': metrics,
        'recommendations': recommendations
    }
    
    # 儲存結果
    os.makedirs('assessment/process', exist_ok=True)
    with open('assessment/process/development.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"開發流程得分: {total_score:.2f}")
    print(f"成熟度等級: {level}")
    
    return result

assess_development_process()
EOF

        echo "✅ 開發流程評估完成"
    '''
}

def measureLeadTime() {
    echo "測量交付週期..."
    
    sh '''
        # 計算從提交到生產的時間
        echo "分析交付週期指標..."
        
        python3 << 'EOF'
import json
import datetime
from datetime import timedelta
import random

def measure_lead_time():
    # 模擬交付週期數據收集
    # 在實際環境中，這些數據來自 Git、Jenkins、部署系統等
    
    # 最近30天的交付數據
    deliveries = []
    for i in range(30):
        # 模擬不同的交付週期
        commit_to_prod_hours = random.uniform(4, 72)  # 4小時到3天
        deliveries.append({
            'date': (datetime.datetime.now() - timedelta(days=i)).isoformat(),
            'lead_time_hours': commit_to_prod_hours,
            'commit_id': f"abc{1000+i}",
            'success': random.choice([True, True, True, False])  # 75% 成功率
        })
    
    # 分析指標
    successful_deliveries = [d for d in deliveries if d['success']]
    
    if successful_deliveries:
        lead_times = [d['lead_time_hours'] for d in successful_deliveries]
        
        avg_lead_time = sum(lead_times) / len(lead_times)
        median_lead_time = sorted(lead_times)[len(lead_times)//2]
        p95_lead_time = sorted(lead_times)[int(len(lead_times)*0.95)]
        
        # DORA 基準比較
        if avg_lead_time <= 24:
            performance_level = "Elite"
        elif avg_lead_time <= 168:  # 1週
            performance_level = "High"
        elif avg_lead_time <= 720:  # 1個月
            performance_level = "Medium"
        else:
            performance_level = "Low"
        
        result = {
            'metric': 'lead_time',
            'avg_hours': round(avg_lead_time, 2),
            'median_hours': round(median_lead_time, 2),
            'p95_hours': round(p95_lead_time, 2),
            'performance_level': performance_level,
            'sample_size': len(successful_deliveries),
            'target_hours': 24
        }
        
        # 儲存結果
        with open('assessment/metrics/lead_time.json', 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"平均交付週期: {avg_lead_time:.2f} 小時")
        print(f"效能等級: {performance_level}")
    
    return result

measure_lead_time()
EOF

        echo "✅ 交付週期測量完成"
    '''
}

def measureDeploymentFrequency() {
    echo "測量部署頻率..."
    
    sh '''
        # 分析部署頻率
        echo "收集部署頻率數據..."
        
        python3 << 'EOF'
import json
import datetime
from datetime import timedelta
import random

def measure_deployment_frequency():
    # 模擬部署數據
    deployments = []
    
    # 最近30天的部署記錄
    for i in range(30):
        daily_deployments = random.randint(0, 15)  # 每日0-15次部署
        date = datetime.datetime.now() - timedelta(days=i)
        
        for j in range(daily_deployments):
            deployments.append({
                'date': date.isoformat(),
                'environment': random.choice(['dev', 'staging', 'prod']),
                'success': random.choice([True, True, True, False])
            })
    
    # 分析生產環境部署
    prod_deployments = [d for d in deployments if d['environment'] == 'prod' and d['success']]
    
    # 計算每日部署頻率
    deployment_days = {}
    for deployment in prod_deployments:
        date_key = deployment['date'].split('T')[0]
        deployment_days[date_key] = deployment_days.get(date_key, 0) + 1
    
    daily_avg = len(prod_deployments) / 30 if prod_deployments else 0
    
    # DORA 基準比較
    if daily_avg >= 1:
        performance_level = "Elite"
    elif daily_avg >= 0.2:  # 每週1次
        performance_level = "High"
    elif daily_avg >= 0.03:  # 每月1次
        performance_level = "Medium"
    else:
        performance_level = "Low"
    
    result = {
        'metric': 'deployment_frequency',
        'daily_average': round(daily_avg, 2),
        'total_deployments': len(prod_deployments),
        'deployment_days': len(deployment_days),
        'performance_level': performance_level,
        'target_daily': 1
    }
    
    # 儲存結果
    with open('assessment/metrics/deployment_frequency.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"每日平均部署次數: {daily_avg:.2f}")
    print(f"效能等級: {performance_level}")
    
    return result

measure_deployment_frequency()
EOF

        echo "✅ 部署頻率測量完成"
    '''
}

def generateImprovementRoadmap() {
    echo "生成改進路線圖..."
    
    sh '''
        # 整合所有評估結果
        echo "整合評估結果並生成改進計畫..."
        
        python3 << 'EOF'
import json
import os
from datetime import datetime, timedelta

def generate_roadmap():
    # 讀取評估結果
    assessment_results = {}
    
    # 讀取文化評估
    if os.path.exists('assessment/culture/collaboration.json'):
        with open('assessment/culture/collaboration.json', 'r') as f:
            assessment_results['culture'] = json.load(f)
    
    # 讀取流程評估
    if os.path.exists('assessment/process/development.json'):
        with open('assessment/process/development.json', 'r') as f:
            assessment_results['process'] = json.load(f)
    
    # 讀取 DORA 指標
    metrics = {}
    for metric in ['lead_time', 'deployment_frequency']:
        file_path = f'assessment/metrics/{metric}.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                metrics[metric] = json.load(f)
    
    # 生成改進路線圖
    roadmap = {
        'assessment_date': datetime.now().isoformat(),
        'overall_maturity': 'Developing',  # 基於綜合評估
        'priority_areas': [],
        'improvement_phases': [],
        'success_metrics': {},
        'estimated_timeline': '12 months'
    }
    
    # 第一階段：基礎改進 (0-3個月)
    phase1 = {
        'phase': 1,
        'name': '基礎建設與流程標準化',
        'duration': '3 months',
        'objectives': [
            '建立標準化的開發流程',
            '提高自動化程度',
            '改善團隊協作'
        ],
        'actions': [
            {
                'action': '實施標準化 Git 工作流程',
                'owner': 'Development Team',
                'timeline': '2 weeks',
                'success_criteria': '100% 的程式碼變更通過 PR 流程'
            },
            {
                'action': '建立 CI/CD Pipeline',
                'owner': 'DevOps Team',
                'timeline': '4 weeks',
                'success_criteria': '自動化建置和部署到測試環境'
            },
            {
                'action': '導入程式碼審查實踐',
                'owner': 'Tech Lead',
                'timeline': '2 weeks',
                'success_criteria': '所有 PR 都有至少一位審查者'
            }
        ]
    }
    
    # 第二階段：能力提升 (3-6個月)
    phase2 = {
        'phase': 2,
        'name': '能力提升與文化建設',
        'duration': '3 months',
        'objectives': [
            '提升團隊技能',
            '建立學習文化',
            '改善監控和回饋'
        ],
        'actions': [
            {
                'action': '建立內部技術分享會',
                'owner': 'All Teams',
                'timeline': '1 week setup, ongoing',
                'success_criteria': '每週一次技術分享，全員參與'
            },
            {
                'action': '實施測試驅動開發',
                'owner': 'Development Team',
                'timeline': '6 weeks',
                'success_criteria': '測試覆蓋率達到 80%'
            },
            {
                'action': '建立監控和告警系統',
                'owner': 'DevOps Team',
                'timeline': '4 weeks',
                'success_criteria': '關鍵指標 100% 監控覆蓋'
            }
        ]
    }
    
    # 第三階段：最佳化 (6-12個月)
    phase3 = {
        'phase': 3,
        'name': '持續最佳化與創新',
        'duration': '6 months',
        'objectives': [
            '達到行業領先水準',
            '建立創新文化',
            '實現持續改進'
        ],
        'actions': [
            {
                'action': '實施金絲雀部署',
                'owner': 'DevOps Team',
                'timeline': '4 weeks',
                'success_criteria': '生產部署零停機時間'
            },
            {
                'action': '建立實驗平台',
                'owner': 'Innovation Team',
                'timeline': '8 weeks',
                'success_criteria': '每月至少 2 個新實驗'
            },
            {
                'action': '實施混沌工程',
                'owner': 'SRE Team',
                'timeline': '6 weeks',
                'success_criteria': '系統韌性得分 > 95%'
            }
        ]
    }
    
    roadmap['improvement_phases'] = [phase1, phase2, phase3]
    
    # 成功指標
    roadmap['success_metrics'] = {
        'lead_time': '< 24 hours',
        'deployment_frequency': '> 1 per day',
        'change_failure_rate': '< 5%',
        'mttr': '< 1 hour',
        'team_satisfaction': '> 4.0/5.0',
        'customer_satisfaction': '> 4.5/5.0'
    }
    
    # 儲存路線圖
    os.makedirs('assessment/reports', exist_ok=True)
    with open('assessment/reports/improvement_roadmap.json', 'w') as f:
        json.dump(roadmap, f, indent=2)
    
    print("✅ 改進路線圖生成完成")
    print(f"預估改進時間: {roadmap['estimated_timeline']}")
    print(f"改進階段數: {len(roadmap['improvement_phases'])}")
    
    return roadmap

generate_roadmap()
EOF

        echo "✅ 改進路線圖生成完成"
    '''
}
```

#### 18.2 團隊協作與溝通

**高效能團隊模式：**

```groovy
// 團隊協作效能監控 Pipeline
pipeline {
    agent { label 'collaboration-monitor' }
    
    triggers {
        cron('0 9 * * 1')  // 每週一上午9點執行
    }
    
    environment {
        TEAM_SIZE = '8'
        SPRINT_LENGTH = '2'  // 週
        COLLABORATION_TOOLS = 'slack,jira,confluence,github'
        MEETING_EFFICIENCY_TARGET = '75'  // 百分比
    }
    
    stages {
        stage('團隊健康度檢查') {
            parallel {
                stage('溝通效率分析') {
                    steps {
                        script {
                            analyzeCommunicationEfficiency()
                        }
                    }
                }
                
                stage('協作品質評估') {
                    steps {
                        script {
                            assessCollaborationQuality()
                        }
                    }
                }
                
                stage('知識分享追蹤') {
                    steps {
                        script {
                            trackKnowledgeSharing()
                        }
                    }
                }
                
                stage('團隊滿意度調查') {
                    steps {
                        script {
                            conductTeamSatisfactionSurvey()
                        }
                    }
                }
            }
        }
        
        stage('協作工具最佳化') {
            steps {
                script {
                    optimizeCollaborationTools()
                    updateTeamDashboard()
                    generateCollaborationInsights()
                }
            }
        }
        
        stage('團隊發展建議') {
            steps {
                script {
                    generateTeamDevelopmentPlan()
                    scheduleTeamBuilding()
                    createLearningPaths()
                }
            }
        }
    }
    
    post {
        always {
            script {
                publishTeamHealthReport()
                notifyTeamLeads()
            }
        }
    }
}

def analyzeCommunicationEfficiency() {
    echo "分析溝通效率..."
    
    sh '''
        # 分析溝通模式
        python3 << 'EOF'
import json
import random
from datetime import datetime, timedelta

def analyze_communication():
    # 模擬溝通數據收集
    comm_data = {
        'meetings': {
            'total_hours': random.randint(15, 35),  # 每週會議時間
            'effective_hours': random.randint(10, 25),
            'participants_avg': random.uniform(4, 8),
            'preparation_score': random.uniform(2, 5)
        },
        'async_communication': {
            'messages_per_day': random.randint(50, 150),
            'response_time_hours': random.uniform(0.5, 8),
            'thread_resolution_rate': random.uniform(0.7, 0.95)
        },
        'documentation': {
            'docs_updated_weekly': random.randint(3, 15),
            'wiki_contributions': random.randint(2, 10),
            'knowledge_base_usage': random.uniform(0.6, 0.9)
        }
    }
    
    # 計算溝通效率分數
    meeting_efficiency = comm_data['meetings']['effective_hours'] / comm_data['meetings']['total_hours']
    async_efficiency = min(1, 24 / comm_data['async_communication']['response_time_hours'])
    doc_efficiency = comm_data['documentation']['knowledge_base_usage']
    
    overall_efficiency = (meeting_efficiency * 0.4 + async_efficiency * 0.35 + doc_efficiency * 0.25) * 100
    
    result = {
        'communication_efficiency': round(overall_efficiency, 2),
        'meeting_efficiency': round(meeting_efficiency * 100, 2),
        'async_efficiency': round(async_efficiency * 100, 2),
        'documentation_efficiency': round(doc_efficiency * 100, 2),
        'raw_data': comm_data,
        'recommendations': []
    }
    
    # 生成建議
    if meeting_efficiency < 0.7:
        result['recommendations'].append('改善會議準備和議程設定')
    if async_efficiency < 0.8:
        result['recommendations'].append('建立更快的回應時間標準')
    if doc_efficiency < 0.8:
        result['recommendations'].append('提高文件化品質和使用率')
    
    with open('communication_analysis.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"溝通效率: {overall_efficiency:.2f}%")
    return result

analyze_communication()
EOF
    '''
}

def trackKnowledgeSharing() {
    echo "追蹤知識分享活動..."
    
    sh '''
        # 知識分享指標分析
        python3 << 'EOF'
import json
import random
from datetime import datetime, timedelta

def track_knowledge_sharing():
    # 模擬知識分享數據
    sharing_data = {
        'tech_talks': {
            'monthly_sessions': random.randint(2, 8),
            'avg_attendance': random.uniform(0.6, 0.9),
            'satisfaction_score': random.uniform(3.5, 5.0)
        },
        'documentation': {
            'new_docs_monthly': random.randint(5, 20),
            'doc_updates_monthly': random.randint(10, 40),
            'tutorial_creation': random.randint(1, 5)
        },
        'mentoring': {
            'mentor_pairs': random.randint(2, 6),
            'mentoring_hours_monthly': random.randint(8, 24),
            'skill_transfer_success': random.uniform(0.7, 0.95)
        },
        'cross_training': {
            'cross_functional_sessions': random.randint(1, 4),
            'skill_matrix_coverage': random.uniform(0.6, 0.85),
            'backup_capability': random.uniform(0.5, 0.8)
        }
    }
    
    # 計算知識分享指數
    tech_talk_score = min(5, sharing_data['tech_talks']['monthly_sessions'] / 2) * sharing_data['tech_talks']['avg_attendance']
    doc_score = min(5, sharing_data['documentation']['new_docs_monthly'] / 4)
    mentoring_score = min(5, sharing_data['mentoring']['mentor_pairs'] / 2) * sharing_data['mentoring']['skill_transfer_success']
    cross_training_score = sharing_data['cross_training']['skill_matrix_coverage'] * 5
    
    knowledge_sharing_index = (tech_talk_score + doc_score + mentoring_score + cross_training_score) / 4
    
    result = {
        'knowledge_sharing_index': round(knowledge_sharing_index, 2),
        'component_scores': {
            'tech_talks': round(tech_talk_score, 2),
            'documentation': round(doc_score, 2),
            'mentoring': round(mentoring_score, 2),
            'cross_training': round(cross_training_score, 2)
        },
        'raw_data': sharing_data,
        'improvement_areas': []
    }
    
    # 識別改進領域
    if tech_talk_score < 3:
        result['improvement_areas'].append('增加技術分享會頻率')
    if doc_score < 3:
        result['improvement_areas'].append('提高文件創建和更新')
    if mentoring_score < 3:
        result['improvement_areas'].append('建立正式的導師制度')
    if cross_training_score < 3:
        result['improvement_areas'].append('加強跨職能培訓')
    
    with open('knowledge_sharing_analysis.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"知識分享指數: {knowledge_sharing_index:.2f}/5.0")
    return result

track_knowledge_sharing()
EOF
    '''
}
```

#### 18.3 持續改進文化

**持續改進實踐框架：**

```yaml
# 持續改進配置
continuous_improvement:
  philosophy:
    kaizen: true
    fail_fast: true
    learn_fast: true
    experiment_driven: true
    
  practices:
    retrospectives:
      frequency: "sprint_end"
      duration: "90_minutes"
      participants: "entire_team"
      formats:
        - "start_stop_continue"
        - "mad_sad_glad"
        - "timeline_review"
        - "root_cause_analysis"
        
    experiments:
      hypothesis_driven: true
      time_boxed: true
      measurable_outcomes: true
      learning_focused: true
      
    feedback_loops:
      customer_feedback:
        frequency: "weekly"
        channels: ["surveys", "interviews", "analytics"]
      internal_feedback:
        frequency: "daily"
        channels: ["standups", "slack", "reviews"]
      system_feedback:
        frequency: "real_time"
        channels: ["monitoring", "alerts", "logs"]
        
  metrics:
    improvement_velocity:
      target: "2_improvements_per_sprint"
      tracking: "backlog_items"
    experiment_success_rate:
      target: "60%"
      tracking: "hypothesis_validation"
    cycle_time_reduction:
      target: "5%_per_quarter"
      tracking: "lead_time_metrics"
```

**持續改進 Pipeline：**

```groovy
// 持續改進追蹤 Pipeline
pipeline {
    agent { label 'improvement-tracker' }
    
    triggers {
        cron('0 17 * * 5')  // 每週五下午5點執行
    }
    
    parameters {
        choice(
            name: 'IMPROVEMENT_SCOPE',
            choices: ['process', 'technology', 'culture', 'all'],
            description: '改進範圍'
        )
    }
    
    environment {
        SPRINT_LENGTH = '2'  // 週
        IMPROVEMENT_TARGET = '2'  // 每個 Sprint 的改進項目
        EXPERIMENT_DURATION = '4'  // 週
    }
    
    stages {
        stage('改進機會識別') {
            parallel {
                stage('回顧分析') {
                    steps {
                        script {
                            analyzeRetrospectives()
                        }
                    }
                }
                
                stage('指標分析') {
                    steps {
                        script {
                            analyzePerformanceMetrics()
                        }
                    }
                }
                
                stage('反饋收集') {
                    steps {
                        script {
                            collectStakeholderFeedback()
                        }
                    }
                }
                
                stage('趨勢分析') {
                    steps {
                        script {
                            analyzeTrends()
                        }
                    }
                }
            }
        }
        
        stage('改進實驗設計') {
            steps {
                script {
                    designImprovementExperiments()
                    prioritizeImprovements()
                    createExperimentPlan()
                }
            }
        }
        
        stage('改進執行追蹤') {
            steps {
                script {
                    trackActiveImprovements()
                    measureExperimentProgress()
                    validateHypotheses()
                }
            }
        }
        
        stage('學習與分享') {
            steps {
                script {
                    documentLearnings()
                    shareSuccessStories()
                    updateBestPractices()
                }
            }
        }
    }
    
    post {
        always {
            script {
                generateImprovementReport()
                scheduleNextActions()
            }
        }
    }
}

def designImprovementExperiments() {
    echo "設計改進實驗..."
    
    sh '''
        # 設計改進實驗
        python3 << 'EOF'
import json
import random
from datetime import datetime, timedelta

def design_experiments():
    # 從識別的改進機會中設計實驗
    improvement_opportunities = [
        {
            'area': 'code_review_process',
            'problem': '程式碼審查週期過長',
            'hypothesis': '引入自動化程式碼檢查可以減少 50% 的審查時間',
            'experiment': '實施 SonarQube 自動檢查',
            'metrics': ['review_time', 'defect_rate', 'developer_satisfaction'],
            'duration_weeks': 4,
            'success_criteria': {
                'review_time_reduction': 0.3,
                'defect_rate_increase': 0.1,
                'satisfaction_increase': 0.2
            }
        },
        {
            'area': 'deployment_process',
            'problem': '部署失敗率高',
            'hypothesis': '增加端到端測試可以降低 40% 的部署失敗率',
            'experiment': '建立 E2E 測試套件',
            'metrics': ['deployment_success_rate', 'rollback_frequency', 'customer_complaints'],
            'duration_weeks': 6,
            'success_criteria': {
                'success_rate_increase': 0.4,
                'rollback_reduction': 0.5,
                'complaint_reduction': 0.3
            }
        },
        {
            'area': 'team_communication',
            'problem': '會議效率低',
            'hypothesis': '結構化議程和時間盒可以提高 25% 的會議效率',
            'experiment': '實施會議最佳實踐',
            'metrics': ['meeting_satisfaction', 'decision_speed', 'action_item_completion'],
            'duration_weeks': 3,
            'success_criteria': {
                'satisfaction_increase': 0.25,
                'decision_speed_increase': 0.3,
                'completion_rate_increase': 0.2
            }
        }
    ]
    
    # 為每個實驗生成詳細計畫
    experiments = []
    for i, opp in enumerate(improvement_opportunities):
        experiment = {
            'id': f'EXP-{datetime.now().strftime("%Y%m%d")}-{i+1:02d}',
            'title': opp['experiment'],
            'area': opp['area'],
            'problem_statement': opp['problem'],
            'hypothesis': opp['hypothesis'],
            'start_date': datetime.now().isoformat(),
            'end_date': (datetime.now() + timedelta(weeks=opp['duration_weeks'])).isoformat(),
            'status': 'planned',
            'metrics': opp['metrics'],
            'success_criteria': opp['success_criteria'],
            'baseline_measurements': {},
            'implementation_plan': {
                'phases': [
                    {
                        'phase': 1,
                        'name': '準備階段',
                        'duration_weeks': 1,
                        'tasks': ['收集基線數據', '準備實驗環境', '培訓參與者']
                    },
                    {
                        'phase': 2,
                        'name': '執行階段',
                        'duration_weeks': opp['duration_weeks'] - 2,
                        'tasks': ['實施改進', '監控指標', '收集反饋']
                    },
                    {
                        'phase': 3,
                        'name': '評估階段',
                        'duration_weeks': 1,
                        'tasks': ['分析結果', '驗證假設', '決定下一步']
                    }
                ]
            },
            'risk_mitigation': {
                'risks': ['參與者抗拒', '技術困難', '資源不足'],
                'mitigations': ['溝通變更益處', '技術支援', '階段性實施']
            }
        }
        experiments.append(experiment)
    
    # 儲存實驗計畫
    with open('improvement_experiments.json', 'w') as f:
        json.dump({
            'design_date': datetime.now().isoformat(),
            'experiments': experiments,
            'total_experiments': len(experiments)
        }, f, indent=2)
    
    print(f"設計了 {len(experiments)} 個改進實驗")
    for exp in experiments:
        print(f"- {exp['id']}: {exp['title']}")
    
    return experiments

design_experiments()
EOF
    '''
}
```

### DevOps 轉型案例

#### 案例研究：企業 DevOps 轉型

**轉型前後對比：**

```yaml
transformation_case_study:
  company: "TechCorp Enterprise"
  industry: "Financial Services"
  team_size: 150
  
  before_transformation:
    culture:
      silos: true
      blame_culture: true
      risk_aversion: high
      learning_culture: low
    
    processes:
      release_cycle: "quarterly"
      deployment_time: "4-6 hours"
      rollback_time: "2-4 hours"
      change_approval: "weeks"
    
    technology:
      automation_level: "20%"
      monitoring_coverage: "basic"
      infrastructure: "manual"
      testing: "manual_qa"
    
    metrics:
      lead_time: "3 months"
      deployment_frequency: "quarterly"
      mttr: "8 hours"
      change_failure_rate: "25%"
  
  after_transformation:
    culture:
      collaboration: high
      experimentation: encouraged
      shared_responsibility: true
      continuous_learning: embedded
    
    processes:
      release_cycle: "daily"
      deployment_time: "15 minutes"
      rollback_time: "5 minutes"
      change_approval: "automated"
    
    technology:
      automation_level: "85%"
      monitoring_coverage: "comprehensive"
      infrastructure: "code_managed"
      testing: "automated_pyramid"
    
    metrics:
      lead_time: "2 days"
      deployment_frequency: "multiple_daily"
      mttr: "15 minutes"
      change_failure_rate: "2%"
  
  transformation_journey:
    duration: "18 months"
    phases:
      - name: "Foundation Building"
        duration: "6 months"
        focus: ["culture", "basic_automation", "team_structure"]
        
      - name: "Capability Development"
        duration: "8 months"
        focus: ["advanced_automation", "monitoring", "processes"]
        
      - name: "Optimization"
        duration: "4 months"
        focus: ["fine_tuning", "scaling", "innovation"]
    
    key_success_factors:
      - "Executive sponsorship"
      - "Gradual culture change"
      - "Skill development investment"
      - "Tool standardization"
      - "Measurement and feedback"
    
    challenges_overcome:
      - "Resistance to change"
      - "Legacy system constraints"
      - "Skill gaps"
      - "Regulatory compliance"
      - "Vendor coordination"
```

### 關鍵成功因素

1. **領導力支持**：
   - 高階主管的承諾與支持
   - 明確的願景和目標
   - 充足的資源投入
   - 持續的變革推動

2. **文化轉變**：
   - 建立學習型組織
   - 鼓勵實驗和創新
   - 消除指責文化
   - 促進跨團隊協作

3. **技能發展**：
   - 持續的培訓計畫
   - 知識分享機制
   - 導師制度建立
   - 外部專家支援

4. **測量與改進**：
   - 建立關鍵指標
   - 定期評估進展
   - 快速回饋機制
   - 持續最佳化

### 認證知識對應

| 認證項目 | 對應內容 |
|----------|----------|
| DevOps 文化 | 協作、學習、實驗文化 |
| 團隊協作 | 跨功能團隊、溝通實踐 |
| 持續改進 | 回顧、實驗、學習循環 |
| 變革管理 | 轉型策略、變革領導 |

### 實務練習 - 第18章

1. **基礎練習**：評估當前團隊的 DevOps 成熟度
2. **進階練習**：設計團隊協作改進計畫
3. **實務練習**：制定完整的 DevOps 轉型路線圖

---

## 第19章 實務案例研究

### 案例研究願景

- 深入分析真實企業的 CI/CD 導入經驗
- 學習不同行業和規模的最佳實踐
- 理解常見挑戰及其解決方案
- 提供可復用的實施策略和模板

### 企業導入案例分析

#### 19.1 案例一：大型金融機構 CI/CD 轉型

**公司背景：**

- 公司：亞洲領先銀行集團
- 規模：10,000+ IT人員
- 系統：500+ 核心應用系統
- 挑戰：嚴格合規要求、龐大遺留系統

```mermaid
graph TB
    subgraph "轉型前架構"
        LB1[季度發布週期]
        LB2[手動部署流程]
        LB3[孤島式團隊]
        LB4[紙本審批流程]
        LB5[分離的測試環境]
    end
    
    subgraph "轉型策略"
        TS1[階段性轉型]
        TS2[合規自動化]
        TS3[文化變革]
        TS4[技能提升]
        TS5[工具標準化]
    end
    
    subgraph "轉型後架構"
        TA1[每日發布能力]
        TA2[全自動化流水線]
        TA3[跨功能敏捷團隊]
        TA4[數位化審批]
        TA5[統一測試平台]
    end
    
    LB1 --> TS1 --> TA1
    LB2 --> TS2 --> TA2
    LB3 --> TS3 --> TA3
    LB4 --> TS4 --> TA4
    LB5 --> TS5 --> TA5
    
    style LB1 fill:#ffebee
    style TS1 fill:#fff3e0
    style TA1 fill:#e8f5e8
```

**實施策略與 Pipeline：**

```groovy
// 金融機構合規 CI/CD Pipeline
pipeline {
    agent none
    
    options {
        // 合規要求
        preserveStashes(buildCount: 10)
        timeout(time: 4, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '50'))
        
        // 審計追蹤
        skipDefaultCheckout(true)
        timestamps()
    }
    
    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'sit', 'uat', 'pre-prod', 'prod'],
            description: '目標環境'
        )
        choice(
            name: 'RELEASE_TYPE',
            choices: ['hotfix', 'regular', 'emergency'],
            description: '發布類型'
        )
        booleanParam(
            name: 'SKIP_SECURITY_SCAN',
            defaultValue: false,
            description: '跳過安全掃描（僅緊急發布）'
        )
        booleanParam(
            name: 'REQUIRE_MANUAL_APPROVAL',
            defaultValue: true,
            description: '要求人工審批'
        )
    }
    
    environment {
        // 合規配置
        SOX_COMPLIANCE = 'true'
        PCI_DSS_COMPLIANCE = 'true'
        GDPR_COMPLIANCE = 'true'
        
        // 審計配置
        AUDIT_TRAIL_ENABLED = 'true'
        COMPLIANCE_CHECKER = 'enabled'
        SECURITY_SCANNING = 'mandatory'
        
        // 審批流程
        CHANGE_ADVISORY_BOARD = 'enabled'
        FOUR_EYES_PRINCIPLE = 'enforced'
        SEGREGATION_OF_DUTIES = 'strict'
        
        // 環境配置
        VAULT_ADDR = 'https://vault.bank.com'
        COMPLIANCE_DB = 'jdbc:postgresql://compliance-db:5432/audit'
        NOTIFICATION_CHANNEL = '#devops-compliance'
    }
    
    stages {
        stage('合規檢查初始化') {
            agent { label 'compliance-agent' }
            steps {
                script {
                    initializeComplianceCheck()
                    validateUserPermissions()
                    logAuditTrail('PIPELINE_START')
                }
            }
        }
        
        stage('原始碼檢出與掃描') {
            agent { label 'security-scanner' }
            steps {
                checkout scm
                script {
                    validateSourceIntegrity()
                    scanForSensitiveData()
                    checkLicenseCompliance()
                    generateSourceReport()
                }
            }
        }
        
        stage('合規建置流程') {
            agent { label 'build-agent' }
            steps {
                script {
                    executeSecureBuild()
                    validateBuildIntegrity()
                    createBuildManifest()
                    archiveComplianceArtifacts()
                }
            }
        }
        
        stage('多層安全掃描') {
            when {
                not { params.SKIP_SECURITY_SCAN }
            }
            parallel {
                stage('SAST 掃描') {
                    agent { label 'sast-scanner' }
                    steps {
                        script {
                            runStaticAnalysis()
                            validateSecurityCompliance()
                        }
                    }
                }
                
                stage('DAST 掃描') {
                    agent { label 'dast-scanner' }
                    steps {
                        script {
                            runDynamicAnalysis()
                            validateRuntimeSecurity()
                        }
                    }
                }
                
                stage('依賴性掃描') {
                    agent { label 'dependency-scanner' }
                    steps {
                        script {
                            scanDependencyVulnerabilities()
                            validateLicenseCompliance()
                        }
                    }
                }
                
                stage('容器掃描') {
                    agent { label 'container-scanner' }
                    steps {
                        script {
                            scanContainerVulnerabilities()
                            validateContainerCompliance()
                        }
                    }
                }
            }
        }
        
        stage('合規測試執行') {
            parallel {
                stage('功能測試') {
                    agent { label 'test-automation' }
                    steps {
                        script {
                            runFunctionalTests()
                            validateBusinessRequirements()
                        }
                    }
                }
                
                stage('效能測試') {
                    agent { label 'performance-test' }
                    steps {
                        script {
                            runPerformanceTests()
                            validatePerformanceCompliance()
                        }
                    }
                }
                
                stage('安全測試') {
                    agent { label 'security-test' }
                    steps {
                        script {
                            runSecurityTests()
                            validateSecurityRequirements()
                        }
                    }
                }
                
                stage('合規測試') {
                    agent { label 'compliance-test' }
                    steps {
                        script {
                            runComplianceTests()
                            validateRegulatoryRequirements()
                        }
                    }
                }
            }
        }
        
        stage('變更審批流程') {
            when {
                expression { params.REQUIRE_MANUAL_APPROVAL == true }
            }
            agent { label 'approval-agent' }
            steps {
                script {
                    requestChangeApproval()
                    waitForCABApproval()
                    validateApprovalChain()
                    logApprovalDecision()
                }
            }
        }
        
        stage('合規部署執行') {
            agent { label 'deployment-agent' }
            steps {
                script {
                    validateDeploymentReadiness()
                    executeControlledDeployment()
                    validateDeploymentSuccess()
                    updateConfigurationManagement()
                }
            }
        }
        
        stage('部署後驗證') {
            parallel {
                stage('健康檢查') {
                    agent { label 'health-check' }
                    steps {
                        script {
                            runHealthChecks()
                            validateSystemStability()
                        }
                    }
                }
                
                stage('合規驗證') {
                    agent { label 'compliance-validator' }
                    steps {
                        script {
                            validateCompliancePostDeployment()
                            verifyControlsEffectiveness()
                        }
                    }
                }
                
                stage('煙霧測試') {
                    agent { label 'smoke-test' }
                    steps {
                        script {
                            runSmokeTests()
                            validateCriticalFunctions()
                        }
                    }
                }
            }
        }
        
        stage('合規報告生成') {
            agent { label 'reporting-agent' }
            steps {
                script {
                    generateComplianceReport()
                    createAuditDocumentation()
                    updateRiskRegister()
                    notifyStakeholders()
                }
            }
        }
    }
    
    post {
        always {
            node('compliance-agent') {
                script {
                    finalizeAuditTrail()
                    archiveComplianceEvidence()
                    updateComplianceDashboard()
                }
            }
        }
        
        success {
            script {
                notifySuccessfulDeployment()
                updateChangeManagementSystem()
                schedulePostImplementationReview()
            }
        }
        
        failure {
            script {
                initiateIncidentResponse()
                notifySecurityTeam()
                generateFailureReport()
                logComplianceViolation()
            }
        }
    }
}

// === 金融合規函式 ===

def initializeComplianceCheck() {
    echo "初始化合規檢查..."
    
    sh '''
        # 設定合規環境
        echo "設定金融業合規環境..."
        
        # 檢查必要的合規工具
        which sonarqube-scanner || { echo "SonarQube Scanner 未安裝"; exit 1; }
        which bandit || { echo "Bandit 安全掃描器未安裝"; exit 1; }
        which safety || { echo "Safety 依賴掃描器未安裝"; exit 1; }
        
        # 設定審計日誌
        mkdir -p audit-logs compliance-reports security-scans
        
        # 初始化合規檢查清單
        cat > compliance-checklist.json << 'EOF'
{
  "sox_compliance": {
    "change_control": false,
    "segregation_of_duties": false,
    "audit_trail": false,
    "access_controls": false
  },
  "pci_dss_compliance": {
    "secure_coding": false,
    "encryption": false,
    "access_logging": false,
    "vulnerability_scanning": false
  },
  "gdpr_compliance": {
    "data_classification": false,
    "privacy_by_design": false,
    "consent_management": false,
    "data_retention": false
  }
}
EOF

        echo "✅ 合規檢查初始化完成"
    '''
}

def validateUserPermissions() {
    echo "驗證用戶權限..."
    
    sh '''
        # 檢查用戶權限
        echo "檢查部署權限..."
        
        USER_ID=$(whoami)
        echo "當前用戶: $USER_ID"
        
        # 檢查環境部署權限
        python3 << 'EOF'
import json
import os

def check_deployment_permissions():
    user_id = os.getenv('BUILD_USER_ID', 'unknown')
    environment = os.getenv('ENVIRONMENT', 'dev')
    
    # 權限矩陣（簡化範例）
    permissions = {
        'dev': ['developer', 'tech-lead', 'devops', 'admin'],
        'sit': ['tech-lead', 'devops', 'admin'],
        'uat': ['devops', 'admin', 'business-analyst'],
        'pre-prod': ['devops', 'admin'],
        'prod': ['admin', 'release-manager']
    }
    
    # 模擬用戶角色檢查
    user_roles = ['devops']  # 從 LDAP/AD 獲取
    
    allowed_roles = permissions.get(environment, [])
    has_permission = any(role in allowed_roles for role in user_roles)
    
    result = {
        'user_id': user_id,
        'environment': environment,
        'user_roles': user_roles,
        'required_roles': allowed_roles,
        'permission_granted': has_permission
    }
    
    with open('permission-check.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    if not has_permission:
        print(f"❌ 用戶 {user_id} 沒有 {environment} 環境的部署權限")
        exit(1)
    else:
        print(f"✅ 用戶 {user_id} 具有 {environment} 環境的部署權限")

check_deployment_permissions()
EOF
    '''
}

def runStaticAnalysis() {
    echo "執行靜態程式碼分析..."
    
    sh '''
        # SonarQube 分析
        echo "執行 SonarQube 靜態分析..."
        
        sonar-scanner \\
            -Dsonar.projectKey=banking-app \\
            -Dsonar.sources=src \\
            -Dsonar.host.url=$SONAR_HOST_URL \\
            -Dsonar.login=$SONAR_AUTH_TOKEN \\
            -Dsonar.qualitygate.wait=true \\
            -Dsonar.java.binaries=target/classes
        
        # 檢查品質閾值
        QUALITY_GATE_STATUS=$(curl -s -u $SONAR_AUTH_TOKEN: \\
            "$SONAR_HOST_URL/api/qualitygates/project_status?projectKey=banking-app" | \\
            jq -r '.projectStatus.status')
        
        if [ "$QUALITY_GATE_STATUS" != "OK" ]; then
            echo "❌ SonarQube 品質閾值檢查失敗"
            exit 1
        fi
        
        # Python 安全掃描
        if [ -f "requirements.txt" ]; then
            echo "執行 Python 安全掃描..."
            bandit -r . -f json -o security-scans/bandit-report.json || true
            safety check --json --output security-scans/safety-report.json || true
        fi
        
        # Java 安全掃描
        if [ -f "pom.xml" ]; then
            echo "執行 Java 安全掃描..."
            mvn org.owasp:dependency-check-maven:check \\
                -DfailBuildOnCVSS=7 \\
                -Dformat=JSON \\
                -DoutputDirectory=security-scans/
        fi
        
        echo "✅ 靜態分析完成"
    '''
}

def requestChangeApproval() {
    echo "請求變更審批..."
    
    sh '''
        # 生成變更請求
        echo "生成變更請求文件..."
        
        python3 << 'EOF'
import json
from datetime import datetime, timedelta

def create_change_request():
    change_request = {
        "change_id": f"CHG-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "title": f"Deploy {os.getenv('JOB_NAME', 'Application')} to {os.getenv('ENVIRONMENT', 'Production')}",
        "description": "Automated deployment via Jenkins CI/CD pipeline",
        "risk_level": "Medium",
        "change_type": "Standard",
        "business_justification": "Deliver new features and bug fixes to customers",
        "technical_details": {
            "application": os.getenv('JOB_NAME', 'banking-app'),
            "version": os.getenv('BUILD_NUMBER', '1.0.0'),
            "environment": os.getenv('ENVIRONMENT', 'prod'),
            "deployment_method": "Blue-Green Deployment"
        },
        "testing_evidence": {
            "unit_tests": "Passed",
            "integration_tests": "Passed",
            "security_scans": "Passed",
            "performance_tests": "Passed"
        },
        "rollback_plan": {
            "method": "Automated rollback via Jenkins",
            "estimated_time": "5 minutes",
            "data_recovery": "Database rollback available"
        },
        "approval_workflow": {
            "technical_approver": "tech-lead@bank.com",
            "business_approver": "product-owner@bank.com",
            "security_approver": "security-team@bank.com",
            "cab_review": True
        },
        "implementation_window": {
            "start_time": (datetime.now() + timedelta(hours=2)).isoformat(),
            "end_time": (datetime.now() + timedelta(hours=4)).isoformat(),
            "maintenance_window": True
        },
        "created_by": os.getenv('BUILD_USER_EMAIL', 'jenkins@bank.com'),
        "created_at": datetime.now().isoformat(),
        "status": "pending_approval"
    }
    
    with open('change-request.json', 'w') as f:
        json.dump(change_request, f, indent=2)
    
    print(f"變更請求已創建: {change_request['change_id']}")
    return change_request

import os
create_change_request()
EOF

        # 提交到變更管理系統
        echo "提交變更請求到 CAB..."
        
        # 模擬 API 呼叫到變更管理系統
        curl -X POST \\
            -H "Content-Type: application/json" \\
            -H "Authorization: Bearer $CAB_API_TOKEN" \\
            -d @change-request.json \\
            "$CAB_SYSTEM_URL/api/change-requests" || echo "CAB 系統連接失敗，使用離線模式"
        
        echo "✅ 變更請求已提交"
    '''
}

def executeControlledDeployment() {
    echo "執行受控部署..."
    
    sh '''
        # 執行藍綠部署
        echo "開始藍綠部署流程..."
        
        python3 << 'EOF'
import json
import time
import random

def execute_blue_green_deployment():
    deployment_config = {
        "strategy": "blue-green",
        "environment": os.getenv('ENVIRONMENT', 'prod'),
        "application": os.getenv('JOB_NAME', 'banking-app'),
        "version": os.getenv('BUILD_NUMBER', '1.0.0'),
        "deployment_steps": []
    }
    
    steps = [
        "準備藍色環境",
        "部署新版本到藍色環境",
        "執行藍色環境健康檢查",
        "執行煙霧測試",
        "切換流量到藍色環境",
        "監控系統穩定性",
        "更新綠色環境為備用"
    ]
    
    for i, step in enumerate(steps, 1):
        print(f"步驟 {i}: {step}")
        
        # 模擬部署步驟執行
        time.sleep(2)
        
        success = random.choice([True, True, True, False])  # 75% 成功率
        
        step_result = {
            "step_number": i,
            "description": step,
            "status": "success" if success else "failed",
            "timestamp": time.time(),
            "duration": random.uniform(30, 120)
        }
        
        deployment_config["deployment_steps"].append(step_result)
        
        if not success:
            print(f"❌ 步驟 {i} 失敗，啟動回滾程序")
            break
        else:
            print(f"✅ 步驟 {i} 完成")
    
    # 判斷整體部署結果
    failed_steps = [s for s in deployment_config["deployment_steps"] if s["status"] == "failed"]
    deployment_config["overall_status"] = "failed" if failed_steps else "success"
    
    with open('deployment-result.json', 'w') as f:
        json.dump(deployment_config, f, indent=2)
    
    if failed_steps:
        print("❌ 部署失敗，需要回滾")
        exit(1)
    else:
        print("✅ 部署成功完成")

import os
execute_blue_green_deployment()
EOF
    '''
}

def generateComplianceReport() {
    echo "生成合規報告..."
    
    sh '''
        # 整合所有合規檢查結果
        echo "整合合規檢查結果..."
        
        python3 << 'EOF'
import json
import os
from datetime import datetime

def generate_compliance_report():
    # 收集所有合規相關文件
    compliance_data = {
        "report_metadata": {
            "generated_at": datetime.now().isoformat(),
            "pipeline_id": os.getenv('BUILD_ID', 'unknown'),
            "environment": os.getenv('ENVIRONMENT', 'unknown'),
            "application": os.getenv('JOB_NAME', 'unknown'),
            "version": os.getenv('BUILD_NUMBER', 'unknown')
        },
        "compliance_checks": {},
        "security_scans": {},
        "test_results": {},
        "deployment_evidence": {},
        "audit_trail": []
    }
    
    # SOX 合規檢查
    compliance_data["compliance_checks"]["sox"] = {
        "change_control": True,
        "segregation_of_duties": True,
        "audit_trail": True,
        "access_controls": True,
        "documentation": True,
        "overall_status": "compliant"
    }
    
    # PCI DSS 合規檢查
    compliance_data["compliance_checks"]["pci_dss"] = {
        "secure_coding": True,
        "encryption": True,
        "access_logging": True,
        "vulnerability_scanning": True,
        "network_security": True,
        "overall_status": "compliant"
    }
    
    # GDPR 合規檢查
    compliance_data["compliance_checks"]["gdpr"] = {
        "data_classification": True,
        "privacy_by_design": True,
        "consent_management": True,
        "data_retention": True,
        "breach_notification": True,
        "overall_status": "compliant"
    }
    
    # 安全掃描結果
    compliance_data["security_scans"] = {
        "static_analysis": {
            "tool": "SonarQube",
            "status": "passed",
            "critical_issues": 0,
            "high_issues": 2,
            "medium_issues": 5
        },
        "dynamic_analysis": {
            "tool": "OWASP ZAP",
            "status": "passed",
            "critical_vulnerabilities": 0,
            "high_vulnerabilities": 0,
            "medium_vulnerabilities": 1
        },
        "dependency_scan": {
            "tool": "OWASP Dependency Check",
            "status": "passed",
            "critical_cves": 0,
            "high_cves": 0,
            "medium_cves": 3
        }
    }
    
    # 測試結果
    compliance_data["test_results"] = {
        "unit_tests": {"status": "passed", "coverage": "85%"},
        "integration_tests": {"status": "passed", "coverage": "78%"},
        "security_tests": {"status": "passed", "coverage": "90%"},
        "performance_tests": {"status": "passed", "response_time": "< 2s"}
    }
    
    # 部署證據
    compliance_data["deployment_evidence"] = {
        "change_approval": "CHG-20240310120000",
        "deployment_method": "Blue-Green",
        "rollback_tested": True,
        "monitoring_enabled": True,
        "backup_verified": True
    }
    
    # 計算整體合規得分
    compliance_score = calculate_compliance_score(compliance_data)
    compliance_data["overall_compliance_score"] = compliance_score
    
    # 生成 HTML 報告
    html_report = generate_html_report(compliance_data)
    
    # 儲存報告
    with open('compliance-reports/compliance-report.json', 'w') as f:
        json.dump(compliance_data, f, indent=2)
    
    with open('compliance-reports/compliance-report.html', 'w') as f:
        f.write(html_report)
    
    print(f"✅ 合規報告已生成，得分: {compliance_score}/100")
    return compliance_data

def calculate_compliance_score(data):
    # 簡化的合規得分計算
    base_score = 100
    
    # 安全掃描扣分
    security_deductions = 0
    for scan_type, results in data["security_scans"].items():
        if results.get("critical_issues", 0) > 0 or results.get("critical_vulnerabilities", 0) > 0:
            security_deductions += 20
        elif results.get("high_issues", 0) > 0 or results.get("high_vulnerabilities", 0) > 0:
            security_deductions += 10
    
    # 測試失敗扣分
    test_deductions = 0
    for test_type, results in data["test_results"].items():
        if results["status"] != "passed":
            test_deductions += 15
    
    final_score = max(0, base_score - security_deductions - test_deductions)
    return final_score

def generate_html_report(data):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>合規檢查報告</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; }}
            .section {{ margin: 20px 0; }}
            .compliant {{ color: green; font-weight: bold; }}
            .non-compliant {{ color: red; font-weight: bold; }}
            .warning {{ color: orange; font-weight: bold; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>CI/CD 合規檢查報告</h1>
            <p><strong>應用程式:</strong> {data['report_metadata']['application']}</p>
            <p><strong>版本:</strong> {data['report_metadata']['version']}</p>
            <p><strong>環境:</strong> {data['report_metadata']['environment']}</p>
            <p><strong>生成時間:</strong> {data['report_metadata']['generated_at']}</p>
            <p><strong>整體合規得分:</strong> <span class="compliant">{data['overall_compliance_score']}/100</span></p>
        </div>
        
        <div class="section">
            <h2>合規檢查摘要</h2>
            <table>
                <tr><th>合規框架</th><th>狀態</th><th>詳細結果</th></tr>
                <tr><td>SOX</td><td class="compliant">合規</td><td>所有控制點通過</td></tr>
                <tr><td>PCI DSS</td><td class="compliant">合規</td><td>安全要求滿足</td></tr>
                <tr><td>GDPR</td><td class="compliant">合規</td><td>隱私保護到位</td></tr>
            </table>
        </div>
        
        <div class="section">
            <h2>安全掃描結果</h2>
            <table>
                <tr><th>掃描類型</th><th>工具</th><th>狀態</th><th>高危問題</th></tr>
                <tr><td>靜態分析</td><td>SonarQube</td><td class="compliant">通過</td><td>2</td></tr>
                <tr><td>動態分析</td><td>OWASP ZAP</td><td class="compliant">通過</td><td>0</td></tr>
                <tr><td>依賴性掃描</td><td>OWASP DC</td><td class="compliant">通過</td><td>0</td></tr>
            </table>
        </div>
        
        <div class="section">
            <h2>測試覆蓋率</h2>
            <table>
                <tr><th>測試類型</th><th>狀態</th><th>覆蓋率</th></tr>
                <tr><td>單元測試</td><td class="compliant">通過</td><td>85%</td></tr>
                <tr><td>整合測試</td><td class="compliant">通過</td><td>78%</td></tr>
                <tr><td>安全測試</td><td class="compliant">通過</td><td>90%</td></tr>
                <tr><td>效能測試</td><td class="compliant">通過</td><td>&lt; 2s</td></tr>
            </table>
        </div>
    </body>
    </html>
    """
    return html_template

generate_compliance_report()
EOF

        echo "✅ 合規報告生成完成"
    '''
}
```

**轉型成果與經驗總結：**

```yaml
transformation_results:
  metrics_improvement:
    lead_time:
      before: "12 weeks"
      after: "3 days"
      improvement: "96% reduction"
    
    deployment_frequency:
      before: "quarterly"
      after: "daily"
      improvement: "30x increase"
    
    change_failure_rate:
      before: "35%"
      after: "3%"
      improvement: "91% reduction"
    
    mttr:
      before: "24 hours"
      after: "30 minutes"
      improvement: "98% reduction"
  
  business_impact:
    time_to_market: "80% faster"
    customer_satisfaction: "+25%"
    operational_efficiency: "+60%"
    compliance_overhead: "-70%"
    
  lessons_learned:
    success_factors:
      - "漸進式轉型策略"
      - "強力的高階支持"
      - "合規自動化優先"
      - "持續技能投資"
      
    challenges_overcome:
      - "文化阻力: 透過漸進式變革和成功案例展示"
      - "技術債務: 建立現代化路線圖"
      - "合規複雜性: 自動化合規檢查"
      - "技能缺口: 內部培訓和外部顧問"
```

#### 19.2 案例二：新創科技公司快速成長

**公司背景：**

- 公司：SaaS 新創企業
- 規模：50人技術團隊
- 產品：雲端協作平台
- 挑戰：快速擴展、有限資源

```groovy
// 新創企業敏捷 CI/CD Pipeline
pipeline {
    agent any
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 30, unit: 'MINUTES')
        skipDefaultCheckout(true)
    }
    
    parameters {
        choice(
            name: 'DEPLOYMENT_STRATEGY',
            choices: ['feature-flag', 'canary', 'blue-green', 'rolling'],
            description: '部署策略'
        )
        booleanParam(
            name: 'ENABLE_FEATURE_FLAGS',
            defaultValue: true,
            description: '啟用功能開關'
        )
        string(
            name: 'FEATURE_PERCENTAGE',
            defaultValue: '10',
            description: '新功能流量百分比'
        )
    }
    
    environment {
        // 敏捷配置
        MOVE_FAST_BREAK_THINGS = 'false'  // 現在是 "move fast with stable infra"
        FEATURE_FLAG_SERVICE = 'https://featureflags.startup.com'
        MONITORING_STACK = 'datadog'
        
        // 成長階段配置
        SCALE_OUT_ENABLED = 'true'
        AUTO_SCALING = 'aggressive'
        COST_OPTIMIZATION = 'enabled'
        
        // 實驗配置
        A_B_TESTING = 'enabled'
        ANALYTICS_TRACKING = 'comprehensive'
        USER_FEEDBACK = 'real-time'
    }
    
    stages {
        stage('敏捷開發檢出') {
            steps {
                checkout scm
                script {
                    setupDevelopmentEnvironment()
                    enableFastFeedback()
                }
            }
        }
        
        stage('快速建置與測試') {
            parallel {
                stage('快速建置') {
                    steps {
                        script {
                            executeFastBuild()
                            optimizeBuildCache()
                        }
                    }
                }
                
                stage('並行測試') {
                    steps {
                        script {
                            runParallelTests()
                            generateQuickReport()
                        }
                    }
                }
                
                stage('即時品質檢查') {
                    steps {
                        script {
                            runLightweightQualityChecks()
                            validateCodeStandards()
                        }
                    }
                }
            }
        }
        
        stage('功能開關部署') {
            when {
                expression { params.ENABLE_FEATURE_FLAGS == true }
            }
            steps {
                script {
                    deployWithFeatureFlags()
                    configureTrafficSplitting()
                    setupABTesting()
                }
            }
        }
        
        stage('實時監控與回饋') {
            parallel {
                stage('效能監控') {
                    steps {
                        script {
                            setupPerformanceMonitoring()
                            trackBusinessMetrics()
                        }
                    }
                }
                
                stage('用戶回饋收集') {
                    steps {
                        script {
                            enableUserFeedbackCollection()
                            setupAnalyticsPipeline()
                        }
                    }
                }
                
                stage('即時告警') {
                    steps {
                        script {
                            configureIntelligentAlerting()
                            setupSlackIntegration()
                        }
                    }
                }
            }
        }
        
        stage('數據驅動決策') {
            steps {
                script {
                    analyzeUserBehavior()
                    calculateFeatureSuccess()
                    generateInsights()
                    triggerNextIteration()
                }
            }
        }
    }
    
    post {
        always {
            script {
                updateMetricsDashboard()
                notifyTeam()
            }
        }
        
        success {
            script {
                if (shouldPromoteFeature()) {
                    promoteToAllUsers()
                }
            }
        }
        
        failure {
            script {
                if (params.ENABLE_FEATURE_FLAGS) {
                    disableFeatureFlag()
                }
                rollbackQuickly()
            }
        }
    }
}

def setupDevelopmentEnvironment() {
    echo "設定敏捷開發環境..."
    
    sh '''
        # 新創企業快速開發設定
        echo "設定新創企業開發環境..."
        
        # 安裝快速開發工具
        npm install --global @startup/dev-tools || echo "Dev tools already installed"
        
        # 設定開發環境變數
        export NODE_ENV=development
        export DEBUG=true
        export FAST_REFRESH=true
        
        # 建立開發便利腳本
        cat > quick-dev.sh << 'EOF'
#!/bin/bash
# 快速開發腳本

echo "🚀 啟動快速開發模式..."

# 啟動本地服務
npm run dev &
npm run test:watch &
npm run lint:watch &

echo "✅ 開發環境就緒"
EOF

        chmod +x quick-dev.sh
        
        echo "✅ 敏捷開發環境設定完成"
    '''
}

def deployWithFeatureFlags() {
    echo "使用功能開關部署..."
    
    sh '''
        # 功能開關部署
        echo "配置功能開關部署..."
        
        python3 << 'EOF'
import json
import requests
import os

def deploy_with_feature_flags():
    feature_config = {
        "feature_name": f"feature-{os.getenv('BUILD_NUMBER', '1')}",
        "enabled": True,
        "rollout_percentage": int(os.getenv('FEATURE_PERCENTAGE', '10')),
        "target_groups": ["beta_users", "internal_team"],
        "metadata": {
            "version": os.getenv('BUILD_NUMBER', '1'),
            "environment": "production",
            "deployed_by": os.getenv('BUILD_USER_EMAIL', 'ci@startup.com'),
            "deployment_time": "2024-03-10T12:00:00Z"
        },
        "conditions": {
            "user_type": "premium",
            "region": ["US", "EU"],
            "device_type": "mobile"
        },
        "metrics_tracking": {
            "conversion_rate": True,
            "user_engagement": True,
            "error_rate": True,
            "performance_impact": True
        }
    }
    
    # 模擬功能開關服務 API 呼叫
    try:
        # response = requests.post(
        #     f"{os.getenv('FEATURE_FLAG_SERVICE')}/api/flags",
        #     json=feature_config,
        #     headers={"Authorization": f"Bearer {os.getenv('FF_API_TOKEN')}"}
        # )
        print(f"✅ 功能開關已配置: {feature_config['feature_name']}")
        print(f"📊 流量百分比: {feature_config['rollout_percentage']}%")
    except Exception as e:
        print(f"❌ 功能開關配置失敗: {e}")
    
    # 儲存配置以供後續使用
    with open('feature-flag-config.json', 'w') as f:
        json.dump(feature_config, f, indent=2)
    
    return feature_config

deploy_with_feature_flags()
EOF

        echo "✅ 功能開關部署完成"
    '''
}

def analyzeUserBehavior() {
    echo "分析用戶行為..."
    
    sh '''
        # 用戶行為分析
        echo "執行用戶行為分析..."
        
        python3 << 'EOF'
import json
import random
from datetime import datetime, timedelta

def analyze_user_behavior():
    # 模擬用戶行為數據
    behavior_data = {
        "analysis_period": {
            "start": (datetime.now() - timedelta(hours=24)).isoformat(),
            "end": datetime.now().isoformat()
        },
        "feature_usage": {
            "new_feature_adoption": random.uniform(0.05, 0.25),
            "user_engagement_score": random.uniform(3.0, 5.0),
            "feature_completion_rate": random.uniform(0.6, 0.9),
            "user_satisfaction": random.uniform(3.5, 4.8)
        },
        "performance_metrics": {
            "page_load_time": random.uniform(1.2, 3.5),
            "api_response_time": random.uniform(100, 500),
            "error_rate": random.uniform(0.01, 0.05),
            "uptime_percentage": random.uniform(0.995, 0.999)
        },
        "business_metrics": {
            "conversion_rate": random.uniform(0.02, 0.08),
            "retention_rate": random.uniform(0.7, 0.9),
            "user_lifetime_value": random.uniform(50, 200),
            "churn_rate": random.uniform(0.02, 0.1)
        },
        "cohort_analysis": {
            "new_users": random.randint(100, 500),
            "returning_users": random.randint(1000, 5000),
            "power_users": random.randint(50, 200)
        }
    }
    
    # 計算功能成功分數
    adoption_score = behavior_data["feature_usage"]["new_feature_adoption"] * 100
    engagement_score = behavior_data["feature_usage"]["user_engagement_score"] * 20
    performance_score = (1 - behavior_data["performance_metrics"]["error_rate"]) * 100
    business_score = behavior_data["business_metrics"]["conversion_rate"] * 1000
    
    overall_score = (adoption_score + engagement_score + performance_score + business_score) / 4
    
    # 生成決策建議
    recommendations = []
    if adoption_score < 15:
        recommendations.append("提高功能可發現性和用戶引導")
    if engagement_score < 80:
        recommendations.append("改善用戶體驗和功能完整性")
    if performance_score < 95:
        recommendations.append("優化系統效能和穩定性")
    if business_score < 40:
        recommendations.append("調整功能設計以提高轉換率")
    
    analysis_result = {
        "overall_success_score": round(overall_score, 2),
        "component_scores": {
            "adoption": round(adoption_score, 2),
            "engagement": round(engagement_score, 2),
            "performance": round(performance_score, 2),
            "business": round(business_score, 2)
        },
        "raw_data": behavior_data,
        "recommendations": recommendations,
        "next_actions": []
    }
    
    # 決定下一步行動
    if overall_score >= 70:
        analysis_result["next_actions"].append("擴大功能推廣至更多用戶")
        analysis_result["decision"] = "promote"
    elif overall_score >= 50:
        analysis_result["next_actions"].append("進行小幅改進後重新測試")
        analysis_result["decision"] = "iterate"
    else:
        analysis_result["next_actions"].append("暫停功能推廣，進行重大修改")
        analysis_result["decision"] = "pause"
    
    with open('user-behavior-analysis.json', 'w') as f:
        json.dump(analysis_result, f, indent=2)
    
    print(f"📈 用戶行為分析完成")
    print(f"🏆 功能成功分數: {overall_score:.2f}/100")
    print(f"💡 建議行動: {analysis_result['decision']}")
    
    return analysis_result

analyze_user_behavior()
EOF

        echo "✅ 用戶行為分析完成"
    '''
}
```

#### 19.3 案例三：傳統製造業數位轉型

**公司背景：**

- 公司：傳統汽車零件製造商
- 規模：2000人，其中IT 100人
- 挑戰：遺留系統、保守文化、安全要求

**轉型實施策略：**

```yaml
manufacturing_transformation:
  approach: "Brownfield Modernization"
  timeline: "36 months"
  
  phase_1_foundation:
    duration: "12 months"
    objectives:
      - "建立基礎 CI/CD 能力"
      - "現代化核心開發流程"
      - "培養 DevOps 文化"
    
    initiatives:
      - name: "Legacy System Assessment"
        description: "評估現有系統現代化可能性"
        timeline: "3 months"
        
      - name: "Pilot Project Selection"
        description: "選擇低風險試點專案"
        timeline: "1 month"
        
      - name: "DevOps Training Program"
        description: "全面 DevOps 技能培訓"
        timeline: "6 months"
        
      - name: "Tool Chain Setup"
        description: "建立標準化工具鏈"
        timeline: "4 months"
  
  phase_2_scaling:
    duration: "12 months"
    objectives:
      - "擴展至更多應用系統"
      - "建立自動化測試能力"
      - "實施持續監控"
    
  phase_3_optimization:
    duration: "12 months"
    objectives:
      - "達到完全自動化"
      - "建立持續改進文化"
      - "成為行業標竿"

transformation_challenges:
  technical:
    - "COBOL 遺留系統整合"
    - "AS/400 主機現代化"
    - "網路安全合規性"
    - "即時製造系統連接"
    
  cultural:
    - "保守的工程文化"
    - "變革抗拒"
    - "技能缺口"
    - "世代差異"
    
  business:
    - "製造不能中斷"
    - "嚴格的品質要求"
    - "成本控制壓力"
    - "法規遵循"

solutions_implemented:
  technical_solutions:
    api_gateway: "建立 API 閘道連接遺留系統"
    strangler_pattern: "逐步替換舊系統"
    microservices: "新功能採用微服務架構"
    hybrid_cloud: "混合雲部署策略"
    
  cultural_solutions:
    mentorship: "建立跨世代導師制度"
    success_stories: "內部成功案例分享"
    gradual_adoption: "漸進式技術採用"
    training_investment: "大量培訓投資"
```

### 最佳實踐總結

#### 共同成功因素

1. **漸進式轉型**：
   - 從小規模試點開始
   - 證明價值後再擴展
   - 避免大爆炸式變革
   - 持續學習和調整

2. **文化先行**：
   - 投資於人員培訓
   - 建立學習型組織
   - 獎勵協作和創新
   - 管理變革阻力

3. **技術務實**：
   - 選擇適合的技術棧
   - 重視自動化和監控
   - 建立可觀測性
   - 確保安全性

4. **業務對齊**：
   - 明確的業務價值
   - 持續的投資回報
   - 利害關係人支持
   - 清晰的成功指標

#### 關鍵學習點

1. **不同行業的適應性**：
   - 金融業重視合規和安全
   - 新創公司追求速度和靈活性
   - 製造業需要穩定性和品質

2. **規模化挑戰**：
   - 大企業需要更多治理
   - 小企業需要更多自動化
   - 中型企業需要平衡兩者

3. **技術債務管理**：
   - 遺留系統現代化策略
   - 技術債務償還計畫
   - 新舊系統並存管理

### 案例對比分析

| 維度 | 金融機構 | 新創企業 | 製造業 |
|------|----------|----------|---------|
| **主要驅動力** | 合規性 | 成長速度 | 數位化 |
| **最大挑戰** | 合規複雜性 | 資源限制 | 文化阻力 |
| **成功關鍵** | 自動化合規 | 功能開關 | 漸進轉型 |
| **轉型時間** | 18個月 | 6個月 | 36個月 |
| **投資重點** | 安全工具 | 監控分析 | 培訓文化 |

### 認證知識對應

| 認證項目 | 對應內容 |
|----------|----------|
| 實務應用 | 真實企業案例分析 |
| 行業適應 | 不同行業的特殊需求 |
| 轉型策略 | 漸進式vs革命式方法 |
| 成功因素 | 文化、技術、業務對齊 |

### 實務練習 - 第19章

1. **基礎練習**：分析自己組織的轉型需求和挑戰
2. **進階練習**：設計適合自己行業的 CI/CD 策略
3. **實務練習**：制定完整的企業轉型實施計畫

---

## 附錄

### 附錄 A：常用指令參考

#### A.1 Jenkins CLI 指令

```bash
# Jenkins CLI 基本使用
java -jar jenkins-cli.jar -s http://localhost:8080/ help

# 用戶和權限管理
java -jar jenkins-cli.jar -s http://localhost:8080/ list-jobs
java -jar jenkins-cli.jar -s http://localhost:8080/ create-job job-name < job-config.xml
java -jar jenkins-cli.jar -s http://localhost:8080/ build job-name
java -jar jenkins-cli.jar -s http://localhost:8080/ cancel-quiet-down

# 系統管理
java -jar jenkins-cli.jar -s http://localhost:8080/ restart
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
java -jar jenkins-cli.jar -s http://localhost:8080/ reload-configuration

# 節點管理
java -jar jenkins-cli.jar -s http://localhost:8080/ connect-node node-name
java -jar jenkins-cli.jar -s http://localhost:8080/ disconnect-node node-name
java -jar jenkins-cli.jar -s http://localhost:8080/ online-node node-name
java -jar jenkins-cli.jar -s http://localhost:8080/ offline-node node-name

# Pipeline 相關
java -jar jenkins-cli.jar -s http://localhost:8080/ replay-pipeline build-number
java -jar jenkins-cli.jar -s http://localhost:8080/ stop-builds job-name
```

#### A.2 Git 整合指令

```bash
# Git 基本操作
git clone https://github.com/user/repo.git
git checkout -b feature/new-feature
git add .
git commit -m "feat: 新增功能"
git push origin feature/new-feature

# Git 標籤管理
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
git tag -l
git show v1.0.0

# Git 分支策略
git flow init
git flow feature start feature-name
git flow feature finish feature-name
git flow release start 1.0.0
git flow release finish 1.0.0

# Git 鉤子設定
#!/bin/bash
# pre-commit hook
npm run lint
npm run test
```

#### A.3 Docker 容器指令

```bash
# Docker 基本操作
docker build -t app:latest .
docker run -d -p 8080:8080 app:latest
docker ps
docker logs container-id
docker exec -it container-id /bin/bash

# Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs -f service-name
docker-compose scale service-name=3

# Docker 清理
docker system prune -f
docker image prune -f
docker container prune -f
docker volume prune -f

# 多階段建置
docker build --target production -t app:prod .
docker build --target development -t app:dev .
```

#### A.4 Kubernetes 部署指令

```bash
# kubectl 基本操作
kubectl get pods
kubectl get services
kubectl get deployments
kubectl describe pod pod-name

# 部署管理
kubectl apply -f deployment.yaml
kubectl rollout status deployment/app
kubectl rollout undo deployment/app
kubectl scale deployment app --replicas=5

# 配置和密碼管理
kubectl create configmap app-config --from-file=config.properties
kubectl create secret generic app-secrets --from-literal=password=secret
kubectl get configmap app-config -o yaml
kubectl get secret app-secrets -o yaml

# 日誌和除錯
kubectl logs -f deployment/app
kubectl exec -it pod-name -- /bin/bash
kubectl port-forward service/app 8080:80
```

### 附錄 B：配置範例

#### B.1 Jenkins 系統配置範例

```xml
<!-- Jenkins 全域工具配置 -->
<hudson>
  <tool>
    <name>Maven 3.8.6</name>
    <home>/opt/maven</home>
    <properties>
      <hudson.tasks.Maven_-MavenInstallation>
        <name>Maven 3.8.6</name>
        <home>/opt/maven</home>
      </hudson.tasks.Maven_-MavenInstallation>
    </properties>
  </tool>
  
  <tool>
    <name>OpenJDK 17</name>
    <home>/opt/jdk-17</home>
    <properties>
      <hudson.model.JDK>
        <name>OpenJDK 17</name>
        <home>/opt/jdk-17</home>
      </hudson.model.JDK>
    </properties>
  </tool>
</hudson>
```

```groovy
// Jenkins 全域 Pipeline 庫
@Library('shared-pipeline-library') _

pipeline {
    agent any
    
    tools {
        maven 'Maven 3.8.6'
        jdk 'OpenJDK 17'
    }
    
    environment {
        SONAR_TOKEN = credentials('sonar-token')
        DOCKER_REGISTRY = 'registry.company.com'
    }
    
    stages {
        stage('標準建置流程') {
            steps {
                buildApplication()
                runTests()
                codeQualityCheck()
                buildDockerImage()
                deployToStaging()
            }
        }
    }
}
```

#### B.2 多環境配置範例

```yaml
# config/environments.yaml
environments:
  development:
    jenkins_url: "http://jenkins-dev.company.com:8080"
    git_branch: "develop"
    deployment_strategy: "rolling"
    monitoring:
      enabled: true
      retention_days: 7
    resources:
      cpu_limit: "1"
      memory_limit: "2Gi"
    replicas: 1
    
  staging:
    jenkins_url: "http://jenkins-staging.company.com:8080"
    git_branch: "release/*"
    deployment_strategy: "blue-green"
    monitoring:
      enabled: true
      retention_days: 30
    resources:
      cpu_limit: "2"
      memory_limit: "4Gi"
    replicas: 2
    
  production:
    jenkins_url: "http://jenkins.company.com:8080"
    git_branch: "main"
    deployment_strategy: "canary"
    monitoring:
      enabled: true
      retention_days: 90
    resources:
      cpu_limit: "4"
      memory_limit: "8Gi"
    replicas: 5
    approval_required: true
    backup_enabled: true
```

#### B.3 安全配置範例

```xml
<!-- Jenkins 安全設定 -->
<authorizationStrategy class="hudson.security.GlobalMatrixAuthorizationStrategy">
  <permission>hudson.model.Hudson.Administer:admin</permission>
  <permission>hudson.model.Hudson.Read:authenticated</permission>
  <permission>hudson.model.Item.Build:developers</permission>
  <permission>hudson.model.Item.Read:developers</permission>
  <permission>hudson.model.Run.Delete:admin</permission>
  <permission>hudson.model.Run.Update:admin</permission>
</authorizationStrategy>

<securityRealm class="hudson.security.LDAPSecurityRealm">
  <server>ldap://ldap.company.com:389</server>
  <rootDN>dc=company,dc=com</rootDN>
  <userSearchBase>ou=users</userSearchBase>
  <userSearch>uid={0}</userSearch>
  <groupSearchBase>ou=groups</groupSearchBase>
</securityRealm>
```

```yaml
# RBAC 權限配置
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: jenkins
  name: jenkins-deployer
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["get", "list", "create", "update", "patch", "delete"]
- apiGroups: ["apps"]
  resources: ["deployments", "replicasets"]
  verbs: ["get", "list", "create", "update", "patch", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: jenkins-deployer-binding
  namespace: jenkins
subjects:
- kind: ServiceAccount
  name: jenkins
  namespace: jenkins
roleRef:
  kind: Role
  name: jenkins-deployer
  apiGroup: rbac.authorization.k8s.io
```

### 附錄 C：故障排除指南

#### C.1 常見 Jenkins 問題

```bash
# 問題：Jenkins 無法啟動
# 解決方案：檢查日誌和配置

# 1. 檢查 Jenkins 日誌
tail -f /var/log/jenkins/jenkins.log

# 2. 檢查磁碟空間
df -h

# 3. 檢查記憶體使用
free -h

# 4. 檢查 Jenkins 進程
ps aux | grep jenkins

# 5. 重啟 Jenkins 服務
sudo systemctl restart jenkins
sudo systemctl status jenkins
```

```groovy
// 問題：Pipeline 記憶體不足
// 解決方案：調整 JVM 參數

pipeline {
    agent any
    
    options {
        // 增加建置超時時間
        timeout(time: 60, unit: 'MINUTES')
        // 保留建置歷史
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    environment {
        // 調整 Maven JVM 參數
        MAVEN_OPTS = '-Xmx2g -Xms1g'
        // 調整 Gradle JVM 參數
        GRADLE_OPTS = '-Xmx2g -Dorg.gradle.daemon=false'
    }
    
    stages {
        stage('記憶體優化建置') {
            steps {
                script {
                    // 清理工作空間
                    deleteDir()
                    
                    // 執行建置
                    sh 'mvn clean compile -DskipTests'
                    
                    // 分批執行測試
                    sh 'mvn test -Dtest=UnitTests'
                    sh 'mvn test -Dtest=IntegrationTests'
                }
            }
        }
    }
    
    post {
        always {
            // 清理建置快取
            sh 'mvn dependency:purge-local-repository'
        }
    }
}
```

#### C.2 網路連接問題

```bash
# 問題：Git 克隆失敗
# 解決方案：網路和認證檢查

# 1. 測試網路連接
ping github.com
telnet github.com 443

# 2. 檢查 Git 配置
git config --list
git config --global http.proxy http://proxy.company.com:8080

# 3. 測試 Git 連接
git ls-remote https://github.com/user/repo.git

# 4. 檢查 SSH 金鑰
ssh -T git@github.com
ssh-add -l

# 5. 更新 Git 憑證
git credential-manager-core erase
```

#### C.3 Docker 建置問題

```bash
# 問題：Docker 建置失敗
# 解決方案：映像和權限檢查

# 1. 檢查 Docker 狀態
docker version
docker info
systemctl status docker

# 2. 清理 Docker 資源
docker system prune -f
docker builder prune -f

# 3. 檢查 Dockerfile
docker build --no-cache -t app:debug .
docker history app:debug

# 4. 除錯建置過程
docker build --progress=plain -t app:debug .

# 5. 檢查容器日誌
docker run --rm app:debug
docker logs container-id
```

#### C.4 性能調優指南

```yaml
# Jenkins 性能調優配置
jenkins_optimization:
  jvm_settings:
    heap_size: "-Xmx4g -Xms2g"
    garbage_collector: "-XX:+UseG1GC"
    additional_options: "-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap"
  
  system_settings:
    jenkins_args: "--sessionTimeout=60 --sessionEviction=300"
    build_executors: 4
    quiet_period: 5
    scm_checkout_retry_count: 3
  
  plugin_optimization:
    disabled_plugins:
      - "ant"
      - "translation"
    essential_plugins:
      - "workflow-aggregator"
      - "git"
      - "docker-plugin"
      - "kubernetes"
  
  workspace_management:
    cleanup_policy: "delete_after_days"
    cleanup_days: 7
    concurrent_builds: false
    custom_workspace: "/opt/jenkins/workspace"
```

### 附錄 D：最佳實踐清單

#### D.1 安全最佳實踐

```markdown
## Jenkins 安全檢查清單

### 認證和授權
- [ ] 啟用適當的安全領域（LDAP/AD/SAML）
- [ ] 配置細粒度的授權策略
- [ ] 定期審查用戶權限
- [ ] 禁用匿名讀取權限
- [ ] 啟用雙因素認證

### 網路安全
- [ ] 配置 HTTPS 和有效的 SSL 憑證
- [ ] 限制網路存取（防火牆/VPN）
- [ ] 使用反向代理（Nginx/Apache）
- [ ] 禁用不必要的端口和服務
- [ ] 配置內容安全政策（CSP）

### 系統安全
- [ ] 定期更新 Jenkins 和外掛程式
- [ ] 配置安全的 JVM 參數
- [ ] 限制檔案系統存取權限
- [ ] 使用專用的服務帳戶運行 Jenkins
- [ ] 啟用安全審計日誌

### 憑證管理
- [ ] 使用 Jenkins 憑證存儲
- [ ] 避免在程式碼中硬編碼密碼
- [ ] 定期輪換敏感憑證
- [ ] 限制憑證存取權限
- [ ] 使用外部密碼管理器（Vault）

### Pipeline 安全
- [ ] 驗證和審查 Pipeline 程式碼
- [ ] 限制 Pipeline 權限
- [ ] 使用沙盒執行環境
- [ ] 避免執行不受信任的程式碼
- [ ] 實施程式碼審查流程
```

#### D.2 效能最佳實踐

```yaml
performance_best_practices:
  resource_management:
    - "適當調整 JVM 堆記憶體大小"
    - "使用 G1GC 垃圾收集器"
    - "配置適當的建置執行器數量"
    - "實施工作空間清理策略"
    
  build_optimization:
    - "使用並行建置"
    - "實施建置快取策略"
    - "優化 Maven/Gradle 配置"
    - "使用多階段 Pipeline"
    
  monitoring_alerts:
    - "監控系統資源使用率"
    - "設定建置時間閾值告警"
    - "追蹤磁碟空間使用"
    - "監控外掛程式性能影響"
    
  scaling_strategies:
    - "使用分散式建置代理"
    - "實施動態代理分配"
    - "配置雲端彈性擴展"
    - "使用容器化建置環境"
```

#### D.3 維護最佳實踐

```bash
#!/bin/bash
# Jenkins 維護腳本範例

# 每日維護任務
daily_maintenance() {
    echo "執行每日維護..."
    
    # 清理過期建置
    find /var/lib/jenkins/jobs/*/builds -mtime +30 -delete
    
    # 清理工作空間
    find /var/lib/jenkins/workspace -mtime +7 -delete
    
    # 檢查磁碟空間
    df -h | awk '$5 > 80 { print "警告：磁碟使用率超過 80%：" $0 }'
    
    # 備份重要配置
    tar -czf /backup/jenkins-config-$(date +%Y%m%d).tar.gz /var/lib/jenkins/config.xml
}

# 每週維護任務
weekly_maintenance() {
    echo "執行每週維護..."
    
    # 更新外掛程式
    java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins | \
        grep -E "^[^(]*\([^)]*\)$" | \
        awk '{print $1}' | \
        xargs -I {} java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin {}
    
    # 系統健康檢查
    curl -f http://localhost:8080/manage/systemInfo || echo "系統檢查失敗"
    
    # 日誌輪轉
    logrotate /etc/logrotate.d/jenkins
}

# 每月維護任務
monthly_maintenance() {
    echo "執行每月維護..."
    
    # 完整系統備份
    tar -czf /backup/jenkins-full-$(date +%Y%m).tar.gz /var/lib/jenkins/
    
    # 性能報告生成
    java -jar jenkins-cli.jar -s http://localhost:8080/ groovy = < performance-report.groovy
    
    # 安全審計
    java -jar jenkins-cli.jar -s http://localhost:8080/ groovy = < security-audit.groovy
}

# 主函數
case "$1" in
    daily)   daily_maintenance ;;
    weekly)  weekly_maintenance ;;
    monthly) monthly_maintenance ;;
    *)       echo "用法: $0 {daily|weekly|monthly}" ;;
esac
```

### 附錄 E：工具和資源

#### E.1 推薦工具清單

```yaml
recommended_tools:
  ide_plugins:
    vscode:
      - "Jenkins Pipeline Linter"
      - "Jenkinsfile Support"
      - "GitLens"
      - "Docker"
      
    intellij:
      - "Jenkins Control Plugin"
      - "Pipeline Syntax"
      - "Kubernetes"
      - "Docker Integration"
  
  cli_tools:
    - name: "Jenkins CLI"
      description: "官方命令列工具"
      install: "wget http://localhost:8080/jnlpJars/jenkins-cli.jar"
      
    - name: "Blue Ocean CLI"
      description: "現代化 Pipeline 介面"
      install: "npm install -g blueocean-cli"
      
    - name: "JenkinsFile Runner"
      description: "本地 Pipeline 測試"
      install: "docker pull jenkins/jenkinsfile-runner"
  
  monitoring_tools:
    - name: "Prometheus + Grafana"
      description: "系統監控和視覺化"
      
    - name: "ELK Stack"
      description: "日誌聚合和分析"
      
    - name: "Jenkins Monitoring Plugin"
      description: "內建監控功能"
  
  security_tools:
    - name: "OWASP Dependency Check"
      description: "依賴性漏洞掃描"
      
    - name: "SonarQube"
      description: "程式碼品質和安全分析"
      
    - name: "Trivy"
      description: "容器映像漏洞掃描"
```

#### E.2 學習資源

```markdown
## 學習資源推薦

### 官方文檔
- [Jenkins 官方文檔](https://www.jenkins.io/doc/)
- [Pipeline 語法參考](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [外掛程式索引](https://plugins.jenkins.io/)
- [Jenkins X 文檔](https://jenkins-x.io/docs/)

### 線上課程
- [Jenkins 基礎課程 - Udemy](https://www.udemy.com/course/jenkins-beginner-to-guru/)
- [CI/CD 實戰 - Coursera](https://www.coursera.org/learn/continuous-integration-deployment)
- [DevOps 工程師認證 - A Cloud Guru](https://acloudguru.com/course/devops-engineer)

### 社群資源
- [Jenkins 用戶社群](https://community.jenkins.io/)
- [Stack Overflow - Jenkins](https://stackoverflow.com/questions/tagged/jenkins)
- [Reddit - r/jenkins](https://www.reddit.com/r/Jenkins/)
- [Jenkins 用戶群組](https://www.meetup.com/topics/jenkins/)

### 實戰練習
- [Jenkins 實驗室](https://github.com/jenkins-docs/simple-java-maven-app)
- [Pipeline 範例庫](https://github.com/jenkinsci/pipeline-examples)
- [Katacoda Jenkins 教學](https://www.katacoda.com/courses/jenkins)

### 書籍推薦
- "Jenkins: The Definitive Guide" by John Ferguson Smart
- "Learning Continuous Integration with Jenkins" by Nikhil Pathania
- "Jenkins 2: Up and Running" by Brent Laster
```

### 附錄 F：認證考試對照

#### F.1 Jenkins 認證考試對應

```yaml
jenkins_certification_mapping:
  cloudbees_jenkins_engineer:
    exam_topics:
      - topic: "Jenkins Fundamentals"
        chapters: [1, 2, 3]
        weight: 20%
        
      - topic: "Pipeline Development"
        chapters: [6, 7, 8, 9]
        weight: 30%
        
      - topic: "Build and Test Automation"
        chapters: [4, 5, 10, 11]
        weight: 25%
        
      - topic: "Security and Administration"
        chapters: [12, 14]
        weight: 15%
        
      - topic: "Advanced Features"
        chapters: [13, 15, 16, 17]
        weight: 10%
  
  study_recommendations:
    preparation_time: "8-12 weeks"
    hands_on_practice: "60+ hours"
    sample_projects: 5
    mock_exams: 3
    
  practice_labs:
    - name: "基礎 Pipeline 建立"
      estimated_time: "4 hours"
      difficulty: "beginner"
      
    - name: "多分支 Pipeline 配置"
      estimated_time: "6 hours"
      difficulty: "intermediate"
      
    - name: "企業級安全配置"
      estimated_time: "8 hours"
      difficulty: "advanced"
```

#### F.2 相關技術認證

```yaml
related_certifications:
  devops_certifications:
    - name: "AWS Certified DevOps Engineer"
      relevance: "雲端部署和監控"
      overlap_chapters: [15, 16, 17]
      
    - name: "Azure DevOps Engineer Expert"
      relevance: "微軟生態系統整合"
      overlap_chapters: [6, 8, 15]
      
    - name: "Google Cloud Professional DevOps Engineer"
      relevance: "GCP 平台整合"
      overlap_chapters: [15, 16, 17]
  
  container_certifications:
    - name: "Certified Kubernetes Administrator (CKA)"
      relevance: "容器編排和部署"
      overlap_chapters: [15, 16]
      
    - name: "Docker Certified Associate (DCA)"
      relevance: "容器化應用"
      overlap_chapters: [15]
  
  security_certifications:
    - name: "Certified Ethical Hacker (CEH)"
      relevance: "DevSecOps 安全實踐"
      overlap_chapters: [14, 17]
      
    - name: "CompTIA Security+"
      relevance: "基礎安全概念"
      overlap_chapters: [14]
```

### 附錄 G：版本更新歷史

```markdown
## 教學手冊版本歷史

### Version 1.0.0 (2024-03-10)
- 初始版本發布
- 包含 19 個核心章節
- 完整的 Pipeline 範例和配置
- 三個企業級案例研究

### 預期更新計畫

#### Version 1.1.0 (預計 2024-06-01)
- 新增 Jenkins X 整合章節
- 更新至 Jenkins LTS 2.401.x
- 新增 GitOps 實踐案例
- 強化安全配置範例

#### Version 1.2.0 (預計 2024-09-01)
- 新增機器學習 Pipeline 範例
- 整合 Tekton 比較分析
- 新增邊緣運算部署案例
- 更新認證考試對照

#### Version 2.0.0 (預計 2025-01-01)
- 全面更新至 Jenkins 3.x
- 重構容器化部署章節
- 新增雲原生架構設計
- 整合新興 DevOps 工具
```

---

## 結語

這個 Jenkins CI/CD 教學手冊旨在為 Java 開發人員提供從入門到精通的完整學習路徑。透過系統性的理論學習、豐富的實務範例、真實的企業案例，以及詳盡的參考資料，希望能幫助讀者建立紮實的 CI/CD 基礎，並在實際工作中發揮所學。

### 學習建議

1. **循序漸進**：按章節順序學習，確保基礎紮實
2. **動手實作**：每個章節都要實際操作和練習
3. **持續實踐**：將學到的知識應用到實際專案中
4. **社群交流**：積極參與 Jenkins 社群討論和分享
5. **持續更新**：關注 Jenkins 新版本和最佳實踐演進

### 致謝

感謝 Jenkins 社群的貢獻，以及所有為 DevOps 生態系統發展付出努力的開發者和企業。特別感謝提供真實案例和經驗分享的企業團隊。

### 反馈和貢獻

如果您在使用本教學手冊過程中發現任何問題，或有改進建議，歡迎：

- 提交 Issue 到專案儲存庫
- 發送電子郵件至：<devops-training@company.com>
- 參與社群討論：#jenkins-tutorial

### 授權信息

本教學手冊採用 [MIT License](https://opensource.org/licenses/MIT) 授權，歡迎自由使用、修改和分享。

---

*最後更新：2024年3月10日*  
*版本：1.0.0*  
*作者：DevOps 培訓團隊*
