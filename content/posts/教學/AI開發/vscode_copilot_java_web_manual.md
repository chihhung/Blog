+++
date = '2026-06-30T10:00:00+08:00'
draft = false
title = 'Vscode_copilot_java_web_manual(1)'
tags = ['教學', 'AI開發']
categories = ['教學']
+++

# 使用 VS Code 與 GitHub Copilot 開發 Java Web 應用程式教學手冊(1)

> **版本**：2026 年 6 月版（對應 VS Code 1.126）　|　**適用對象**：初中階 Java 開發人員　|　**維護單位**：資深架構師團隊

---

## 目錄

1. [前言與環境概述](#1-前言與環境概述)
   - 1.1 為什麼選擇 VS Code + GitHub Copilot？
   - 1.2 技術棧總覽
   - 1.3 學習路徑建議
2. [安裝與環境設定](#2-安裝與環境設定)
   - 2.1 安裝 Java JDK
   - 2.2 安裝 VS Code
   - 2.3 安裝必要擴充套件
   - 2.4 啟用 GitHub Copilot
   - 2.5 VS Code 設定（settings.json）
3. [專案建立與初始化](#3-專案建立與初始化)
   - 3.1 使用 Spring Initializr 建立專案
   - 3.2 VS Code 開啟與結構說明
4. [GitHub Copilot 核心功能使用](#4-github-copilot-核心功能使用)
   - 4.1 程式碼自動補全（Inline Suggestions）
   - 4.2 Next Edit Suggestions（NES）
   - 4.3 Copilot Chat 對話式開發
   - 4.4 Agent Mode（代理模式）
   - 4.5 使用 Inline Chat
   - 4.6 自訂指令與 Prompt 檔案
   - 4.7 MCP 伺服器整合
5. [Java Web 開發實戰](#5-java-web-開發實戰)
   - 5.1 建立 REST API Controller
   - 5.2 Service 層與 Repository 層
   - 5.3 連接資料庫（JPA + MySQL）
   - 5.4 安全性設定（Spring Security）
6. [除錯與測試](#6-除錯與測試)
   - 6.1 VS Code 除錯設定
   - 6.2 單元測試與 Copilot 輔助
   - 6.3 整合測試
7. [系統維護與升級](#7-系統維護與升級)
   - 7.1 相依套件版本管理
   - 7.2 VS Code 與擴充套件升級
   - 7.3 Java 版本升級指引
8. [最佳實踐與團隊建議](#8-最佳實踐與團隊建議)
   - 8.1 Copilot 使用原則
   - 8.2 程式碼品質規範
   - 8.3 團隊協作建議
   - 8.4 安全與信任控制
9. [常見問題 FAQ](#9-常見問題-faq)
10. [附錄：Prompt 參考範本](#10-附錄prompt-參考範本)
    - 10.1 生成程式碼類
    - 10.2 除錯與分析類
    - 10.3 測試類
    - 10.4 架構與設計類

---

## 1. 前言與環境概述

### 1.1 為什麼選擇 VS Code + GitHub Copilot？

Visual Studio Code 已發展為功能完備的開發平台，最新版本（1.126，2026 年 6 月發布）內建 AI Agent 功能，可直接在編輯器中以自然語言驅動開發流程。VS Code 搭配 GitHub Copilot 的 Agent Mode，開發者僅需描述任務意圖，Agent 便能自動規劃步驟、跨檔案編輯程式碼、執行終端命令並自我修正，直到任務完成。

根據 GitHub 官方統計，使用 Copilot 的開發者平均可節省約 **55% 的編碼時間**，而 Agent Mode 的引入更進一步將多步驟任務的人工介入降低至僅需審查與確認。

**VS Code 作為 Java 開發環境的優勢**：

- 輕量啟動、資源佔用低，適合微服務多專案並行開發
- 內建 AI Agent 系統（Copilot CLI、Local Agent、Cloud Agent），支援端到端自動化
- 透過 Extension Pack for Java 提供完整的 Java 語言伺服器（JDT.LS）支援
- 整合式終端、除錯器、測試執行器一站完備
- 跨平台一致體驗（Windows / macOS / Linux）

### 1.2 技術棧總覽

| 層次 | 技術 | 版本要求 |
|------|------|----------|
| IDE | Visual Studio Code | 1.126+（2026 年 6 月） |
| AI 助理 | GitHub Copilot（Agent Mode、Chat、NES） | 內建於 VS Code |
| 語言 | Java | 21 LTS（建議） / 25（最新） |
| 框架 | Spring Boot | 3.4.x（最新穩定版） |
| 建置工具 | Maven / Gradle | 3.9+ / 8.10+ |
| 資料庫 | MySQL / PostgreSQL | 8.4 / 17 |
| 容器化 | Docker + Docker Compose | 27+ |
| 版本控制 | Git | 2.45+ |

### 1.3 學習路徑建議

```text
安裝環境 → 建立第一個 Spring Boot 專案 → 學習 Copilot 基本操作
→ 掌握 Agent Mode → 開發 REST API → 連接資料庫 → 加入安全性
→ 測試與除錯 → 配置 MCP 伺服器 → 部署上線
```

### 1.4 VS Code 版本演進重要里程碑

| 版本 | 發布日期 | 關鍵功能 |
|------|----------|----------|
| 1.100 | 2025/05 | Agent Mode 正式啟用、NES 預設開啟、MCP Streamable HTTP、Prompt/Instructions 檔案 |
| 1.113 | 2026/03 | Chat Customizations 編輯器、巢狀子代理、Copilot CLI 支援 MCP、新預設主題 |
| 1.126 | 2026/06 | Session 成本管理、多聊天並行、Agents Window（Preview）、統一模型自訂選擇器 |

---

## 2. 安裝與環境設定

### 2.1 安裝 Java JDK

推薦使用 **Eclipse Temurin（AdoptOpenJDK）** 或 **Microsoft Build of OpenJDK**。

#### Windows

```powershell
# 使用 winget 安裝 Java 21
winget install Microsoft.OpenJDK.21

# 驗證安裝
java -version
javac -version
```

#### macOS

```bash
# 使用 Homebrew 安裝
brew install --cask temurin@21

# 驗證安裝
java -version
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install temurin-21-jdk

# 設定 JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/temurin-21' >> ~/.bashrc
source ~/.bashrc
```

> ⚠️ **注意**：請確保 `JAVA_HOME` 環境變數已正確設定，否則 VS Code Java 擴充套件可能無法正常運作。

---

### 2.2 安裝 VS Code

前往 [https://code.visualstudio.com](https://code.visualstudio.com) 下載最新穩定版（目前為 **1.126**，2026 年 6 月發布）。

#### 各平台安裝

| 平台 | 安裝方式 |
|------|----------|
| Windows x64 | 官網下載 `.exe` 安裝程式 或 `winget install Microsoft.VisualStudioCode` |
| Windows Arm64 | 官網下載對應 Arm64 版本 |
| macOS (Universal) | 官網下載 `.dmg` 或 `brew install --cask visual-studio-code` |
| Linux (deb) | `sudo apt install ./<filename>.deb` |
| Linux (rpm) | `sudo rpm -i <filename>.rpm` |

建議勾選安裝選項：
- ✅ 加入 PATH
- ✅ 註冊為支援的檔案類型的編輯器
- ✅ 加入「以 Code 開啟」至右鍵選單

#### 首次開啟注意事項（Workspace Trust）

VS Code 1.126 起，開啟新資料夾時預設進入 **Restricted Mode**（受限模式），瀏覽程式碼後再手動信任。此行為由 `security.workspace.trust.startupPrompt` 設定控制（預設值已從 `once` 改為 `never`）。若需還原舊行為（首次開啟即彈出信任提示），可將設定改回 `once`。

---

### 2.3 安裝必要擴充套件

在 VS Code 中按 `Ctrl+Shift+X`（macOS：`Cmd+Shift+X`）開啟擴充套件面板，搜尋並安裝以下套件：

#### 核心 Java 套件（Extension Pack for Java）

```text
套件 ID：vscjava.vscode-java-pack
```

此套件包含：
- **Language Support for Java™ by Red Hat** — 語法支援、智慧補全
- **Debugger for Java** — 除錯功能
- **Test Runner for Java** — 執行 JUnit/TestNG
- **Maven for Java** — Maven 專案管理
- **Project Manager for Java** — 專案瀏覽器

#### Spring Boot 套件

```text
套件 ID：vmware.vscode-spring-boot
套件 ID：vscjava.vscode-spring-initializr
套件 ID：vscjava.vscode-spring-boot-dashboard
```

#### GitHub Copilot

```text
套件 ID：GitHub.copilot
套件 ID：GitHub.copilot-chat
```

#### 輔助工具套件（建議安裝）

| 套件名稱 | 套件 ID | 用途 |
|----------|---------|------|
| GitLens | eamodio.gitlens | Git 增強功能 |
| REST Client | humao.rest-client | 測試 API |
| Docker | ms-azuretools.vscode-docker | Docker 整合 |
| SonarLint | SonarSource.sonarlint-vscode | 程式碼品質 |
| Lombok Annotations | GabrielBB.vscode-lombok | Lombok 支援 |

---

### 2.4 啟用 GitHub Copilot

自 VS Code 1.100 起，GitHub Copilot 已深度整合於 VS Code 核心，AI 功能內建於編輯器中。

**Step 1：取得授權**

GitHub Copilot 提供以下方案：

| 方案 | 說明 | 適用對象 |
|------|------|----------|
| Free | 每月有限額（補全 2000 次 / Chat 50 次） | 個人開發者試用 |
| Pro | 無限制使用所有功能 | 專業開發者 |
| Pro+ | 進階模型存取、更高用量配額 | 重度使用者 |
| Business | 組織管理、政策控制、IP 保障 | 企業團隊 |
| Enterprise | 企業知識庫整合、進階安全功能 | 大型企業 |

前往 [https://github.com/features/copilot](https://github.com/features/copilot) 訂閱。

**Step 2：在 VS Code 登入**

1. 點選標題列的 **Sign In** 按鈕，或將滑鼠懸停在狀態列 Copilot 圖示上選擇 **Enable AI features**
2. 瀏覽器會開啟授權頁面，完成 GitHub OAuth 授權後回到 VS Code
3. 若未訂閱付費方案，系統自動註冊 Free 方案

**Step 3：驗證 Copilot 運作**

建立一個 `Test.java` 檔案，輸入以下文字後等待建議：

```java
// 計算費氏數列第 n 項
public int fibonacci(
```

Copilot 應自動補全完整方法。

**Step 4：開啟 Agent Mode**

按 `Ctrl+Shift+I` 直接開啟 Chat 並切換至 Agent Mode，或從標題列選擇 **Open in Agents** 啟動 Agents Window。

> ⚠️ **注意**：若組織管理員已停用 Agent 功能（`chat.agent.enabled`），需聯繫管理員啟用。

---

### 2.5 VS Code 設定（settings.json）

按 `Ctrl+Shift+P` → 輸入 `Open User Settings JSON`，加入以下設定：

```json
{
  "java.jdt.ls.java.home": "/path/to/jdk-21",
  "java.compile.nullAnalysis.mode": "automatic",
  "editor.suggestSelection": "first",
  "editor.inlineSuggest.enabled": true,
  "github.copilot.nextEditSuggestions.enabled": true,
  "github.copilot.nextEditSuggestions.fixes": true,
  "github.copilot.chat.agent.autoFix": true,
  "chat.agent.enabled": true,
  "spring-boot.ls.java.home": "/path/to/jdk-21",
  "editor.formatOnSave": true,
  "java.format.settings.profile": "GoogleStyle",
  "[java]": {
    "editor.defaultFormatter": "redhat.java"
  }
}
```

> 💡 **提示**：`github.copilot.enable` 設定已簡化，VS Code 現在預設為所有語言啟用 Copilot。若需針對特定語言停用，可在 settings.json 中配置。

---

## 3. 專案建立與初始化

### 3.1 使用 Spring Initializr 建立專案

**方法一：VS Code 指令面板**

1. 按 `Ctrl+Shift+P` → 輸入 `Spring Initializr: Create a Maven Project`
2. 依序選擇：
   - Spring Boot 版本：**3.4.x**（最新穩定版）
   - 語言：**Java**
   - Group ID：`com.example`
   - Artifact ID：`demo-app`
   - Packaging：**Jar**
   - Java 版本：**21**
3. 選擇相依套件（Dependencies）：
   - ✅ Spring Web
   - ✅ Spring Data JPA
   - ✅ Spring Security
   - ✅ MySQL Driver
   - ✅ Lombok
   - ✅ Spring Boot DevTools
   - ✅ Validation
4. 選擇儲存資料夾，VS Code 自動開啟專案

**方法二：使用 Agent Mode 生成**

在 Agent Mode（`Ctrl+Shift+I`）中輸入：

```
幫我建立一個 Spring Boot 3.4 的 Maven 專案結構，
包含 Controller、Service、Repository 三層架構，
使用 MySQL 資料庫，並加入 Lombok 和 Spring Security。
完成後執行 mvn compile 確認編譯通過。
```

Agent Mode 會自動建立完整專案結構、產生所有必要檔案，並在終端執行編譯驗證。

---

### 3.2 VS Code 開啟與結構說明

```
demo-app/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/demoapp/
│   │   │       ├── DemoAppApplication.java   ← 啟動入口
│   │   │       ├── controller/               ← REST API 層
│   │   │       ├── service/                  ← 業務邏輯層
│   │   │       ├── repository/               ← 資料存取層
│   │   │       ├── model/                    ← Entity 實體
│   │   │       ├── dto/                      ← 資料傳輸物件
│   │   │       ├── config/                   ← 設定類別
│   │   │       └── exception/                ← 例外處理
│   │   └── resources/
│   │       ├── application.yml               ← 主要設定
│   │       ├── application-dev.yml           ← 開發環境設定
│   │       └── static/                       ← 靜態資源
│   └── test/
│       └── java/                             ← 測試程式碼
├── pom.xml                                   ← Maven 設定
└── .gitignore
```

**Spring Boot Dashboard** 擴充套件會在左側面板顯示所有 Spring Boot 應用，可直接點擊 ▶ 啟動。

---

## 4. GitHub Copilot 核心功能使用

### 4.1 程式碼自動補全（Inline Suggestions）

Copilot 在你打字時自動產生建議（灰色文字）：

| 操作 | 快捷鍵 |
|------|--------|
| 接受建議 | `Tab` |
| 拒絕建議 | `Esc` |
| 查看下一個建議 | `Alt+]` |
| 查看上一個建議 | `Alt+[` |
| 開啟建議面板 | `Ctrl+Enter` |

**技巧：善用註解引導 Copilot**

```java
// 建立一個 UserService，實作 CRUD 操作，使用 UserRepository
// 方法需要處理使用者不存在的情況並拋出自定義例外
public class UserService {
    // Copilot 將在此處根據上方註解自動補全
```

---

### 4.2 Next Edit Suggestions（NES）

NES 是 VS Code 1.100 起預設啟用的智慧預測功能，能根據你最近的編輯行為，主動在你「下一步可能要修改的位置」預先提供建議。不同於傳統的 Inline Suggestions 僅在游標位置觸發，NES 會在檔案中其他相關位置顯示預測編輯。

#### 啟用與設定

```json
{
  "github.copilot.nextEditSuggestions.enabled": true,
  "github.copilot.nextEditSuggestions.fixes": true
}
```

#### 功能特點

| 功能 | 說明 |
|------|------|
| 位置預測 | 自動判斷你下一步可能修改的程式碼位置 |
| 低延遲回應 | 新一代模型大幅降低延遲 |
| 匯入建議 | 自動補充遺漏的 `import` 語句（Java/TypeScript） |
| 非侵入式 | 建議與你的編輯節奏一致，不打斷工作流 |

#### 使用方式

- 透過 `Tab` 鍵接受 NES 建議
- 在 Accessible View（`Alt+F2`）中審查建議
- 可配置音效提示：`accessibility.signals.nextEditSuggestion`

---

### 4.3 Copilot Chat 對話式開發

按 `Ctrl+Alt+I`（macOS：`Cmd+Option+I`）開啟 Copilot Chat 側邊欄。

#### Chat 模式

VS Code 提供三種 Chat 模式，各有不同適用場景：

| 模式 | 快捷鍵 | 說明 |
|------|--------|------|
| **Ask** | `Ctrl+Alt+I` | 純問答模式，不修改檔案 |
| **Edit** | — | 已於 1.126 正式移除（改用 Agent Mode） |
| **Agent** | `Ctrl+Shift+I` | 完整自動化代理，可讀寫檔案、執行命令、呼叫工具 |

#### 常用 Chat 指令（Slash Commands）

| 指令 | 說明 | 範例 |
|------|------|------|
| `/explain` | 解釋選取的程式碼 | 選取程式碼 → `/explain` |
| `/fix` | 修復程式碼問題 | 選取錯誤程式碼 → `/fix` |
| `/tests` | 生成單元測試 | 選取方法 → `/tests` |
| `/doc` | 生成 JavaDoc 文件 | 選取類別 → `/doc` |
| `/optimize` | 優化程式碼效能 | 選取方法 → `/optimize` |
| `/new` | 建立新檔案/專案 | `/new Spring Boot REST API` |

#### 使用 `#` 引用上下文

```
#file:UserController.java 這個 Controller 缺少哪些安全性設定？
#codebase 我們的專案中，如何實作分頁查詢？
#terminal 這個 Maven 錯誤怎麼解決？
#githubRepo microsoft/spring-boot 參考官方如何實作快取機制
#extensions 有什麼好的 Java 測試擴充套件推薦？
#fetch https://docs.spring.io/... 幫我整理這頁文件的重點
```

#### 模型選擇與 Thinking Effort

VS Code 1.113 起，可直接在 Chat 模型選擇器中切換語言模型並調整推理深度：

- **GPT-4.1**：快速回應，適合日常問答和快速編輯
- **Claude Sonnet 4.6**：深度推理，適合複雜架構設計和多步驟任務
- **GPT-5.4**：最新旗艦模型，支援 Thinking Effort 調節

Thinking Effort 選項：`Low`（快速回應）/ `Medium`（平衡）/ `High`（深度思考）

---

### 4.4 Agent Mode（代理模式）

Agent Mode 是 VS Code 最核心的 AI 功能，讓 Copilot 以自主代理方式執行完整開發任務。

#### 開啟方式

- 快捷鍵：`Ctrl+Shift+I` 直接進入 Agent Mode
- 從標題列選擇 **Open in Agents** 開啟 Agents Window（Preview）
- Chat 視窗中切換模式選擇器為 "Agent"

#### Agent Mode 能力

| 能力 | 說明 |
|------|------|
| 規劃任務 | 分析需求並產出實作計畫 |
| 跨檔案編輯 | 同時修改多個相關檔案 |
| 執行終端命令 | 自動執行 Maven/Gradle 構建、測試 |
| 自動修正 | 偵測編輯引入的錯誤並自動提出修正（`github.copilot.chat.agent.autoFix`） |
| 瀏覽網頁 | 使用 `#fetch` 工具取得外部文件 |
| 搜尋程式庫 | 使用 `#githubRepo` 搜尋 GitHub 倉庫 |

#### 權限等級

| 等級 | 說明 |
|------|------|
| 確認所有動作 | 每個工具呼叫都需要你批准 |
| 允許唯讀操作 | 讀檔、搜尋自動執行，寫入需批准 |
| 完全自主 | Agent 可獨立完成所有操作 |

#### 使用範例

```
請建立一個完整的使用者管理模組：
1. User Entity（含 JPA 注解）
2. UserRepository
3. UserService（含 CRUD 和分頁查詢）
4. UserController（REST API，/api/v1/users）
5. UserServiceTest（JUnit 5 + Mockito）
所有類別使用 Lombok，並加入適當的 Validation 注解
```

Agent Mode 會自動依序建立所有檔案，並在過程中執行編譯確認正確性。

#### Agents Window（Preview，1.126 新增）

Agents Window 是獨立的代理管理視窗，支援：

- **多聊天並行**：同一 Session 中可開啟多個 Chat 分頁（`+` 按鈕），各自獨立對話
- **跨工作區管理**：從單一視窗管理多個專案的 Agent Session
- **程式碼回饋**：直接對 Agent 產生的程式碼留下註解，Agent 可讀取並回應
- **Session 成本資訊**：查看整個 Session 的信用額度消耗

---

### 4.5 使用 Inline Chat

在程式碼中直接按 `Ctrl+I`（macOS：`Cmd+I`）開啟 Inline Chat：

```java
public List<User> findAll() {
    // [Ctrl+I] 加入快取機制，使用 Spring Cache，TTL 設為 5 分鐘
}
```

VS Code 1.100 引入了 **Inline Chat V2**（可透過 `inlineChat.enableV2` 啟用），使用與 Agent Mode 相同的編輯邏輯，提供更好的上下文理解與程式碼修改品質。啟用 `inlineChat.hideOnRequest` 設定後，送出請求時 Inline Chat 會自動隱藏，最小化至 Chat 編輯覆蓋層。

---

### 4.6 自訂指令與 Prompt 檔案

VS Code 1.100+ 引入了 Markdown 驅動的自訂系統，讓團隊可以標準化 AI 行為。

#### Instructions 檔案（`.instructions.md`）

Instructions 檔案定義通用的編碼規範與上下文指引，Copilot 會自動將其附加至相關請求。

**建立方式**：`Ctrl+Shift+P` → `Chat: New Instructions File...`

**範例**：`.github/instructions/java-style.instructions.md`

```markdown
---
applyTo: '**/*.java'
description: 'Java 編碼風格規範'
---
## Java 開發規範
- 使用 Lombok 減少樣板程式碼（@Data, @Builder, @RequiredArgsConstructor）
- 所有 Service 方法加 @Transactional
- Controller 不直接操作 Entity，一律透過 DTO 轉換
- 使用 SLF4J Logger，禁止 System.out.println
- 例外處理使用自定義 Exception 類別搭配 @RestControllerAdvice
- 方法命名使用小駝峰，類別命名使用大駝峰
```

#### Prompt 檔案（`.prompt.md`）

Prompt 檔案封裝完整的可重複使用 Chat 請求。

**建立方式**：`Ctrl+Shift+P` → `Chat: New Prompt File...`

**範例**：`.github/prompts/create-rest-crud.prompt.md`

```markdown
---
mode: 'agent'
tools: ['file_search', 'read_file', 'create_file', 'replace_string_in_file']
description: '生成標準 CRUD REST API'
---
根據以下規格生成完整的 REST CRUD 模組：
- Entity 名稱：${input:entityName}
- 欄位：${input:fields}

請建立：Controller、Service（介面+實作）、Repository、DTO、Mapper
遵循專案中 .github/instructions/ 下的編碼規範
```

**執行方式**：
1. 在 Chat 輸入 `/create-rest-crud` 觸發
2. 在 Prompt 檔案編輯器中點擊 ▶ Play 按鈕
3. 使用 `Chat: Run Prompt File...` 指令

#### Chat Customizations 編輯器（1.113 Preview）

在 Chat 視窗點擊齒輪圖示，或執行 `Chat: Open Chat Customizations`，可在統一介面中管理所有自訂項目：Instructions、Prompt、Custom Agents、Skills、MCP Servers。

---

### 4.7 MCP 伺服器整合

Model Context Protocol（MCP）讓 Copilot Agent 能連接外部工具與資料源。

#### 設定方式

在專案根目錄建立 `.vscode/mcp.json`：

```json
{
  "servers": {
    "database-tools": {
      "url": "http://localhost:3001/mcp",
      "description": "提供資料庫 Schema 查詢與 SQL 執行"
    },
    "jira-integration": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-jira"],
      "env": {
        "JIRA_URL": "${input:jiraUrl}",
        "JIRA_TOKEN": "${input:jiraToken}"
      }
    }
  }
}
```

#### 支援的傳輸方式

| 方式 | 說明 |
|------|------|
| Streamable HTTP | 標準 HTTP 端點（1.100+ 支援） |
| SSE（Server-Sent Events） | 向下相容 SSE 伺服器 |
| stdio | 透過命令列啟動本地程序 |

#### 安全性考量

- 使用 `inputs` 機制管理密鑰，避免在設定檔中硬編碼敏感資訊
- 標註 `readOnlyHint: true` 的工具可跳過使用者確認自動執行
- VS Code 1.113 起，MCP 伺服器也可在 Copilot CLI 與 Claude Agent 中使用

---

## 5. Java Web 開發實戰

### 5.1 建立 REST API Controller

#### application.yml 基本設定

```yaml
spring:
  application:
    name: demo-app
  datasource:
    url: jdbc:mysql://localhost:3306/demo_db?useSSL=false&serverTimezone=UTC
    username: ${DB_USERNAME:root}
    password: ${DB_PASSWORD:secret}
    driver-class-name: com.mysql.cj.jdbc.Driver
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQLDialect
        format_sql: true

server:
  port: 8080

logging:
  level:
    com.example: DEBUG
```

#### Entity 範例（使用 Lombok）

```java
package com.example.demoapp.model;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true, length = 50)
    private String username;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false, unique = true)
    private String email;

    @Enumerated(EnumType.STRING)
    private Role role;

    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        updatedAt = LocalDateTime.now();
    }

    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }

    public enum Role {
        ADMIN, USER, MODERATOR
    }
}
```

#### REST Controller 範例

```java
package com.example.demoapp.controller;

import com.example.demoapp.dto.UserDTO;
import com.example.demoapp.service.UserService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    // 取得所有使用者（分頁）
    @GetMapping
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Page<UserDTO>> getAllUsers(Pageable pageable) {
        return ResponseEntity.ok(userService.findAll(pageable));
    }

    // 取得單一使用者
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.findById(id));
    }

    // 建立使用者
    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody UserDTO dto) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(userService.create(dto));
    }

    // 更新使用者
    @PutMapping("/{id}")
    public ResponseEntity<UserDTO> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UserDTO dto) {
        return ResponseEntity.ok(userService.update(id, dto));
    }

    // 刪除使用者
    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
```

> **Copilot 提示**：選取上方 Controller 類別，在 Chat 輸入 `/tests` 即可自動生成對應的單元測試。使用 Agent Mode 還可自動建立測試檔案並執行 `mvn test` 驗證。

---

### 5.2 Service 層與 Repository 層

#### Repository

```java
package com.example.demoapp.repository;

import com.example.demoapp.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByUsername(String username);
    Optional<User> findByEmail(String email);
    boolean existsByUsername(String username);
    boolean existsByEmail(String email);

    @Query("SELECT u FROM User u WHERE u.role = :role")
    java.util.List<User> findAllByRole(User.Role role);
}
```

#### Service 介面與實作

```java
// UserService.java（介面）
public interface UserService {
    Page<UserDTO> findAll(Pageable pageable);
    UserDTO findById(Long id);
    UserDTO create(UserDTO dto);
    UserDTO update(Long id, UserDTO dto);
    void delete(Long id);
}

// UserServiceImpl.java（實作）
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final UserMapper userMapper;

    @Override
    public Page<UserDTO> findAll(Pageable pageable) {
        return userRepository.findAll(pageable)
                .map(userMapper::toDTO);
    }

    @Override
    public UserDTO findById(Long id) {
        return userRepository.findById(id)
                .map(userMapper::toDTO)
                .orElseThrow(() -> new ResourceNotFoundException("User not found: " + id));
    }

    @Override
    @Transactional
    public UserDTO create(UserDTO dto) {
        if (userRepository.existsByUsername(dto.getUsername())) {
            throw new DuplicateResourceException("Username already exists");
        }
        User user = userMapper.toEntity(dto);
        user.setPassword(passwordEncoder.encode(dto.getPassword()));
        return userMapper.toDTO(userRepository.save(user));
    }
    // ... 其他方法
}
```

---

### 5.3 連接資料庫（JPA + MySQL）

#### Docker Compose 快速啟動 MySQL

```yaml
# docker-compose.yml
version: '3.8'
services:
  mysql:
    image: mysql:8.0
    container_name: demo-mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: demo_db
      MYSQL_USER: demouser
      MYSQL_PASSWORD: demopass
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  mysql_data:
```

```bash
# 啟動資料庫
docker-compose up -d mysql

# 確認狀態
docker-compose ps
```

#### 使用 Flyway 資料庫版本控管

```xml
<!-- pom.xml 加入 -->
<dependency>
    <groupId>org.flywaydb</groupId>
    <artifactId>flyway-mysql</artifactId>
</dependency>
```

```sql
-- src/main/resources/db/migration/V1__create_users_table.sql
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('ADMIN', 'USER', 'MODERATOR') NOT NULL DEFAULT 'USER',
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    INDEX idx_username (username),
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

### 5.4 安全性設定（Spring Security）

```java
package com.example.demoapp.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.disable())
            .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/v1/auth/**").permitAll()
                .requestMatchers("/actuator/health").permitAll()
                .anyRequest().authenticated()
            )
            // 加入 JWT Filter（使用 Copilot 生成）
            // .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class)
            .build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(12);
    }
}
```

> **Copilot 提示**：在 Agent Mode（`Ctrl+Shift+I`）輸入以下 Prompt 可生成完整 JWT 實作：
> ```
> 幫我實作完整的 JWT 認證流程，包含：
> 1. JwtUtil 工具類（生成、驗證 Token）
> 2. JwtAuthenticationFilter（攔截請求驗證 Token）
> 3. AuthController（登入/登出 API）
> 使用 io.jsonwebtoken:jjwt 函式庫，Java 21，Spring Security 6
> 完成後執行 mvn compile 確認編譯無誤
> ```

---

## 6. 除錯與測試

### 6.1 VS Code 除錯設定

建立 `.vscode/launch.json`：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "java",
      "name": "Debug Spring Boot App",
      "request": "launch",
      "mainClass": "com.example.demoapp.DemoAppApplication",
      "projectName": "demo-app",
      "env": {
        "SPRING_PROFILES_ACTIVE": "dev",
        "DB_USERNAME": "demouser",
        "DB_PASSWORD": "demopass"
      },
      "vmArgs": "-Xmx512m"
    },
    {
      "type": "java",
      "name": "Attach to Remote (8000)",
      "request": "attach",
      "hostName": "localhost",
      "port": 8000
    }
  ]
}
```

**除錯技巧**：
- 點擊行號左側設置斷點（紅點）
- `F5` 啟動除錯模式
- `F10` 逐行執行（Step Over）
- `F11` 進入方法（Step Into）
- `Shift+F11` 跳出方法（Step Out）

---

### 6.2 單元測試與 Copilot 輔助

#### 讓 Copilot 自動生成測試

**方法一：使用 Slash Command**

1. 選取要測試的 Service 類別或方法
2. 在 Chat 輸入 `/tests`
3. Copilot 自動生成對應的 JUnit 5 測試

**方法二：使用 Agent Mode（推薦）**

在 Agent Mode 中輸入：

```
為 UserServiceImpl 的所有方法生成完整的 JUnit 5 單元測試，
使用 Mockito 模擬 UserRepository 和 PasswordEncoder，
覆蓋正常流程和例外情況（帳號重複、資源不存在、驗證失敗等），
測試方法命名使用 [方法名]_[條件]_[預期結果] 格式，
完成後執行 mvn test 確認所有測試通過
```

Agent Mode 會自動建立測試檔案、寫入測試程式碼，並執行測試驗證。

#### 測試範例結構

```java
@ExtendWith(MockitoExtension.class)
class UserServiceImplTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @InjectMocks
    private UserServiceImpl userService;

    @Test
    @DisplayName("建立使用者 - 成功情境")
    void createUser_Success() {
        // Given
        UserDTO dto = UserDTO.builder()
            .username("testuser")
            .email("test@example.com")
            .password("password123")
            .build();

        when(userRepository.existsByUsername("testuser")).thenReturn(false);
        when(passwordEncoder.encode(anyString())).thenReturn("encoded_password");
        when(userRepository.save(any(User.class))).thenAnswer(i -> i.getArgument(0));

        // When
        UserDTO result = userService.create(dto);

        // Then
        assertNotNull(result);
        assertEquals("testuser", result.getUsername());
        verify(userRepository).save(any(User.class));
    }

    @Test
    @DisplayName("建立使用者 - 帳號重複應拋出例外")
    void createUser_DuplicateUsername_ThrowsException() {
        // Given
        when(userRepository.existsByUsername(anyString())).thenReturn(true);

        // When & Then
        assertThrows(DuplicateResourceException.class,
            () -> userService.create(new UserDTO()));
    }
}
```

---

### 6.3 整合測試

#### 使用 REST Client 測試 API

建立 `requests/users.http` 檔案（需安裝 REST Client 擴充套件）：

```http
### 取得所有使用者
GET http://localhost:8080/api/v1/users
Authorization: Bearer {{token}}
Content-Type: application/json

###
### 建立使用者
POST http://localhost:8080/api/v1/users
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "role": "USER"
}

###
### 登入取得 Token
POST http://localhost:8080/api/v1/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "adminpass"
}
```

按 `Send Request` 文字即可直接執行。

#### 使用 TestContainers 整合測試

針對需要真實資料庫的場景，推薦使用 TestContainers：

```java
@SpringBootTest
@Testcontainers
class UserRepositoryIntegrationTest {

    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.4")
        .withDatabaseName("test_db")
        .withUsername("test")
        .withPassword("test");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
    }

    @Autowired
    private UserRepository userRepository;

    @Test
    @DisplayName("儲存並查詢使用者")
    void saveAndFindUser() {
        User user = User.builder()
            .username("integrationtest")
            .email("it@example.com")
            .password("encoded")
            .role(User.Role.USER)
            .build();

        User saved = userRepository.save(user);

        assertThat(saved.getId()).isNotNull();
        assertThat(userRepository.findByUsername("integrationtest"))
            .isPresent()
            .get()
            .extracting(User::getEmail)
            .isEqualTo("it@example.com");
    }
}
```

> **Copilot 提示**：在 Agent Mode 輸入「為 UserRepository 生成使用 TestContainers 的整合測試，測試所有自定義查詢方法」可快速生成完整測試。

---

## 7. 系統維護與升級

### 7.1 相依套件版本管理

#### 查看過時相依套件

```bash
# Maven
./mvnw versions:display-dependency-updates

# Gradle
./gradlew dependencyUpdates
```

#### 升級 Spring Boot 版本

```bash
# 使用 Maven Wrapper 升級
./mvnw spring-boot:help -Ddetail=true -Dgoal=help

# 修改 pom.xml 中的版本
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.4.1</version>  <!-- 更新此版本號 -->
</parent>
```

**升級後驗證清單**：
- [ ] 執行所有單元測試 `./mvnw test`
- [ ] 執行整合測試
- [ ] 確認 API 功能正常
- [ ] 檢查日誌是否有 Deprecation 警告
- [ ] 更新相關文件

---

### 7.2 VS Code 與擴充套件升級

```text
# VS Code 自動更新
檔案 → 喜好設定 → 設定 → 搜尋 "update mode"
建議設定：default（自動下載，重啟後安裝）

# 手動檢查更新
說明 → 檢查更新（Help → Check for Updates）

# 手動更新擴充套件
Ctrl+Shift+X → 點擊擴充套件面板右上方 "..." → 更新所有擴充套件
```

> 💡 **提示**：VS Code 採用漸進式發布策略，新版本會逐步推送給所有使用者。若需立即取得最新版本，可使用 "Check for Updates" 指令。

**定期維護排程建議**：

| 頻率 | 任務 |
|------|------|
| 每週 | 更新擴充套件、檢視 Agent 使用成本 |
| 每月 | 更新 VS Code 版本、Review Copilot 使用情況、更新 Instructions 檔案 |
| 每季 | 評估 Spring Boot Patch 版本升級、審查 MCP 伺服器配置 |
| 每半年 | 評估 Java LTS 版本升級 |

---

### 7.3 Java 版本升級指引

從 Java 21 升級至 Java 25（或未來 LTS）的步驟：

1. **評估相容性**：執行 `jdeps` 分析相依套件
   ```bash
   jdeps --jdk-internals -cp target/demo-app.jar com.example.demoapp.DemoAppApplication
   ```

2. **更新 pom.xml**
   ```xml
   <properties>
       <java.version>25</java.version>
   </properties>
   ```

3. **測試與修正**：執行完整測試套件，解決相容性問題

4. **使用 Copilot 輔助遷移**
   ```
   我的專案使用 Java 21，想升級到 Java 25，
   請分析以下程式碼中有哪些 API 已被棄用，並提供升級建議
   [貼上程式碼]
   ```

---

## 8. 最佳實踐與團隊建議

### 8.1 Copilot 使用原則

#### ✅ 建議做法

- **審查每一個 Copilot 建議**：AI 生成的程式碼不一定正確，必須由工程師負責審查
- **使用清晰的註解引導**：在程式碼上方寫清楚業務邏輯，Copilot 會更準確
- **善用 Chat 解釋複雜程式碼**：遇到不熟悉的程式碼，先問 Copilot `/explain`
- **讓 Copilot 生成測試**：自動生成的測試可快速覆蓋基本情境
- **使用 `#file:` 引用上下文**：讓 Copilot 了解整個專案結構

#### ❌ 避免做法

- 不審查直接採用安全性相關程式碼（如認證、加密）
- 將敏感資料（密碼、API Key）放在對話中
- 依賴 Copilot 處理複雜業務邏輯而不理解內容
- 在 Copilot Chat 分享客戶個人資料

---

### 8.2 程式碼品質規範

#### 命名規範

```java
// 類別：大駝峰式
public class UserAccountService { }

// 方法/變數：小駝峰式
private String userAccountName;
public void getUserAccount() { }

// 常數：全大寫底線
private static final int MAX_RETRY_COUNT = 3;

// 套件：全小寫
package com.example.demoapp.service;
```

#### 提交規範（Conventional Commits）

```
feat: 新增使用者分頁查詢功能
fix: 修復 JWT Token 過期驗證問題
refactor: 重構 UserService 提升效能
test: 新增 UserController 整合測試
docs: 更新 API 文件
chore: 升級 Spring Boot 至 3.4.1
```

---

### 8.3 團隊協作建議

1. **建立團隊共用的 `.vscode/settings.json`** 確保一致的格式化設定
2. **建立 Instructions 檔案** 讓 Copilot 自動遵循專案規範
3. **建立共用 Prompt 檔案庫** 讓同仁透過 `/` 斜線命令共享有效的自動化流程
4. **配置 MCP 伺服器** 整合團隊常用的外部工具（Jira、資料庫、CI/CD）
5. **定期 Copilot 使用心得分享**（建議每月一次）
6. **使用 Chat Customizations 編輯器** 統一管理所有自訂項目

#### Instructions 檔案目錄結構（建議）

```
.github/
├── instructions/
│   ├── java-style.instructions.md      ← Java 編碼規範
│   ├── testing.instructions.md         ← 測試撰寫規範
│   ├── security.instructions.md        ← 安全性規範
│   └── api-design.instructions.md      ← API 設計規範
├── prompts/
│   ├── create-entity.prompt.md         ← 生成 Entity
│   ├── create-rest-crud.prompt.md      ← 生成 CRUD API
│   ├── create-test.prompt.md           ← 生成測試
│   └── code-review.prompt.md           ← 程式碼審查
└── agents/
    └── security-reviewer.agent.md      ← 安全審查 Agent
```

#### `.github/instructions/java-style.instructions.md` 範例

```markdown
---
applyTo: '**/*.java'
description: 'Java 編碼規範與專案慣例'
---
## 程式語言與框架
- Java 21, Spring Boot 3.4, Maven

## 編碼規範
- 使用 Lombok 減少樣板程式碼
- 所有 Service 方法加 @Transactional
- 例外處理使用自定義 Exception 類別搭配 @RestControllerAdvice
- 日誌使用 SLF4J（private static final Logger log = LoggerFactory.getLogger(...)）

## 命名規範
- Entity 類別對應表名（UserProfile → user_profiles）
- DTO 使用 Java record 或 Lombok @Data
- REST API 路徑使用複數名詞小寫（/api/v1/users）

## 禁止事項
- 不使用 System.out.println，改用 SLF4J Logger
- 不在 Controller 直接操作 Entity，需透過 DTO
- 不在程式碼中硬編碼密碼或 API Key
```

---

### 8.4 安全與信任控制

VS Code Agent 系統具備完善的安全機制，組織可從多個層面控制 AI 行為：

#### 權限管理

| 控制項 | 說明 |
|--------|------|
| 工具呼叫審批 | 每次 Agent 呼叫工具（寫檔、執行命令）前需使用者確認 |
| 權限等級設定 | 可選擇 "確認所有" / "允許唯讀" / "完全自主" |
| Agent Sandboxing | 透過 OS 層級限制檔案系統與網路存取 |

#### 企業級 AI 政策

組織管理員可透過 GitHub Organization 設定：

- 控制可用的 AI 功能範圍
- 限制可使用的語言模型
- 管理 MCP 伺服器白名單
- 強制啟用或停用特定 Agent 能力
- 設定 IP 保障與資料保護政策

#### 安全最佳實踐

1. **不在 Chat 中分享敏感資訊**（密碼、API Key、客戶個資）
2. **審查所有安全性相關的 AI 建議**（認證、加密、權限控制）
3. **啟用擴充套件簽章驗證**（VS Code 1.100 起所有平台強制啟用）
4. **使用 Workspace Trust** 安全瀏覽不熟悉的程式碼
5. **配置 MCP 伺服器時使用 `inputs` 管理密鑰**，避免明文存放

---

## 9. 常見問題 FAQ

### Q1：VS Code 找不到 Java，顯示「No JDK found」？

**解決方案**：
```json
// settings.json 手動指定 JDK 路徑
{
  "java.jdt.ls.java.home": "C:\\Program Files\\Eclipse Adoptium\\jdk-21.0.4.7-hotspot",
  // macOS: "/Library/Java/JavaVirtualMachines/temurin-21.jdk/Contents/Home"
  // Linux: "/usr/lib/jvm/temurin-21"
}
```

### Q2：Copilot 建議無法顯示？

**排查步驟**：
1. 確認 Copilot 擴充套件已安裝且啟用
2. 確認已登入 GitHub 帳號（左下角帳號圖示）
3. 確認網路可連線至 `api.github.com`
4. 檢查狀態列的 Copilot 圖示是否顯示錯誤

### Q3：Spring Boot 啟動失敗，找不到資料庫？

**解決方案**：
```bash
# 確認 Docker MySQL 正在執行
docker-compose ps

# 確認連線設定
curl http://localhost:3306 # 應顯示連線被拒（代表 MySQL 有在監聽）

# 查看 Spring Boot 日誌
# VS Code Terminal 中執行：
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev
```

### Q4：如何讓 Copilot 記住我的偏好設定？

建立 `.github/instructions/` 目錄下的 `.instructions.md` 檔案（見 4.6 節），使用 `applyTo` 前端標頭指定適用檔案類型。VS Code 會根據當前檔案自動附加匹配的 Instructions。

另可透過 Chat Customizations 編輯器（`Chat: Open Chat Customizations`）統一管理所有自訂設定。

### Q5：Agent Mode 和舊版 Copilot Edits 有什麼差別？

Copilot Edits（Edit Mode）已於 VS Code 1.126 正式移除。Agent Mode 完全取代其功能，並額外提供：
- 自動執行終端命令（如 `mvn compile`、`npm test`）
- 自動偵測並修正引入的錯誤
- 支援 MCP 工具呼叫
- 可搜尋 GitHub 倉庫和網頁內容
- 對話歷史摘要壓縮，保持長對話效能

### Q6：如何離線使用 VS Code 進行 Java 開發（不使用 Copilot）？

VS Code 本身和 Java 擴充套件可離線使用，但 Copilot 需要網路連線。離線時建議使用：
- 本地 AI 模型（如 Ollama + Continue 擴充套件）作為替代
- VS Code 1.113+ 支援自帶 API Key 連接任意模型提供者

### Q7：VS Code 開啟專案時顯示「Restricted Mode」怎麼辦？

這是 VS Code 1.126 的新預設行為。開啟新資料夾時會先進入受限模式，讓你安全瀏覽程式碼。確認安全後，點擊橫幅中的 **Trust** 按鈕即可解除限制。若要對已知安全的資料夾略過此步驟，可在 Workspace Trust 編輯器中將其加入信任清單。

### Q8：如何查看 Agent 消耗了多少信用額度？

VS Code 1.126 新增 Session-level cost information 功能。在 Chat Session 資訊彈出視窗中可查看：
- 整個 Session 的信用額度消耗
- Context Window Token 使用量
- 各次對話的個別成本

---

## 10. 附錄：Prompt 參考範本

以下為常用的高效 Copilot Prompt 範本，供同仁直接使用：

### 10.1 生成程式碼類

```
# 生成 REST Controller
幫我建立一個 [ProductController]，包含 CRUD 操作的 REST API，
使用 [ProductService]，回傳 [ProductDTO]，
加入適當的 HTTP 狀態碼和 @Valid 驗證，
URL 前綴為 /api/v1/products

# 生成 JPA Entity
建立一個 [Order] Entity，欄位包含：id、訂單編號、使用者ID、總金額、狀態（Enum）、建立時間，
使用 Lombok，加入適當的 JPA 注解和索引

# 生成 Service 實作
幫我實作 [UserService] 介面，使用 [UserRepository]，
包含分頁查詢、根據 Email 查詢、軟刪除功能，
使用 MapStruct 做 DTO 轉換，並處理適當的例外情況
```

### 10.2 除錯與分析類

```
# 分析效能問題
以下程式碼在高並發下有效能問題，請分析原因並提供改善方案：
[貼上程式碼]

# 解釋複雜程式碼
請用繁體中文解釋以下程式碼的運作原理，並說明可能的改善點：
[貼上程式碼]

# 修復錯誤
以下程式碼出現錯誤：[錯誤訊息]，請協助修復並解釋原因：
[貼上程式碼]
```

### 10.3 測試類

```
# 生成完整測試
為以下 Service 方法生成 JUnit 5 + Mockito 單元測試，
覆蓋：正常情境、邊界條件、例外情境，
測試方法命名使用 [方法名]_[條件]_[預期結果] 格式：
[貼上程式碼]

# 生成整合測試
使用 @SpringBootTest 和 TestContainers 為 [UserRepository] 
生成整合測試，測試 CRUD 操作
```

### 10.4 架構與設計類

```
# 架構建議
我正在設計一個電商系統，需要處理高並發訂單，
請建議使用 Spring Boot 的最佳架構設計，
包含：快取策略、非同步處理、資料庫設計建議

# 重構建議
以下程式碼違反了 SOLID 原則，請分析違反了哪些原則，
並提供重構建議和範例程式碼：
[貼上程式碼]

# 安全性審查
請審查以下 Spring Security 設定，
指出潛在的安全性問題並提供修復方案：
[貼上程式碼]
```

---

## 參考資源

| 資源 | 連結 |
|------|------|
| VS Code 官方文件 | https://code.visualstudio.com/docs |
| VS Code 最新更新（1.126） | https://code.visualstudio.com/updates/v1_126 |
| VS Code Agents 文件 | https://code.visualstudio.com/docs/agents/overview |
| VS Code Agent 自訂設定 | https://code.visualstudio.com/docs/agent-customization/overview |
| VS Code MCP 伺服器 | https://code.visualstudio.com/docs/agent-customization/mcp-servers |
| GitHub Copilot 文件 | https://docs.github.com/copilot |
| Spring Boot 官方文件 | https://docs.spring.io/spring-boot/reference/ |
| Spring Initializr | https://start.spring.io |
| Maven Repository | https://mvnrepository.com |
| VS Code Java 開發指南 | https://code.visualstudio.com/docs/languages/java |

---

*本文件由資深架構師團隊維護，最後更新：2026 年 6 月（對應 VS Code 1.126）。如有疑問或建議，請透過內部 Issue Tracker 回報。*
